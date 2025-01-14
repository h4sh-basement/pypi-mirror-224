
from __future__ import annotations

import asyncio
from asyncio import Event, Queue, Task, TimeoutError
from collections.abc import Mapping, Sequence
from contextlib import suppress
from typing import final, Final, Optional, NoReturn
from weakref import WeakSet, WeakKeyDictionary

from .config import BaseConfig
from .members import Member, Members
from .packet import Packet, Ping, PingReq, Ack, Gossip, GossipAck
from .status import Status
from .tasks import DaemonTask, TaskOwner

__all__ = ['Worker']


class Worker(DaemonTask, TaskOwner):
    """Manages the failure detection and dissemination components of the SWIM
    protocol.

    See Also:
        :ref:`Failure Detection`, :ref:`Dissemination`

    Args:
        config: The cluster configuration object.
        members: Tracks the state of the cluster members.

    """

    def __init__(self, config: BaseConfig, members: Members) -> None:
        super().__init__()
        self.config: Final = config
        self.members: Final = members
        self._recv_queue: Queue[Packet] = Queue()
        self._send_queue: Queue[tuple[Member, Packet]] = Queue()
        self._waiting: WeakKeyDictionary[Member, WeakSet[Event]] = \
            WeakKeyDictionary()
        self._listening: WeakKeyDictionary[Member, WeakSet[Member]] = \
            WeakKeyDictionary()
        self._suspect: WeakKeyDictionary[Member, Task[None]] = \
            WeakKeyDictionary()

    @property
    def recv_queue(self) -> Queue[Packet]:
        """The queue of packets received."""
        return self._recv_queue

    @property
    def send_queue(self) -> Queue[tuple[Member, Packet]]:
        """The queue of packets to be sent."""
        return self._send_queue

    async def _send(self, target: Member, packet: Packet) -> None:
        await self._send_queue.put((target, packet))

    def _add_waiting(self, member: Member, event: Event) -> None:
        waiting = self._waiting.get(member)
        if waiting is None:
            self._waiting[member] = waiting = WeakSet()
        waiting.add(event)

    def _add_listening(self, member: Member, target: Member) -> None:
        listening = self._listening.get(target)
        if listening is None:
            self._listening[target] = listening = WeakSet()
        listening.add(member)

    def _notify_waiting(self, member: Member) -> None:
        waiting = self._waiting.get(member)
        if waiting is not None:
            for event in waiting:
                event.set()

    def _get_listening(self, member: Member) -> Sequence[Member]:
        listening = self._listening.pop(member, None)
        if listening is not None:
            return list(listening)
        else:
            return []

    async def _run_handler(self) -> NoReturn:
        local = self.members.local
        while True:
            packet = await self.recv_queue.get()
            source = self.members.get(packet.source.name,
                                      packet.source.validity)
            if isinstance(packet, Ping):
                await self._send(source, Ack(source=local.source))
            elif isinstance(packet, PingReq):
                target = self.members.get(packet.target)
                await self._send(target, Ping(source=local.source))
                self._add_listening(source, target)
            elif isinstance(packet, Ack):
                self._notify_waiting(source)
                for target in self._get_listening(source):
                    await self._send(target, packet)
            elif isinstance(packet, Gossip):
                member = self.members.get(packet.name)
                ack = self._apply_gossip(local, source, member, packet)
                await self._send(source, ack)
            elif isinstance(packet, GossipAck):
                member = self.members.get(packet.name)
                self.members.ack_gossip(member, source, packet.clock)

    def _build_gossip(self, local: Member, member: Member) -> Gossip:
        if member.metadata is Member.METADATA_UNKNOWN:
            metadata: Optional[Mapping[str, bytes]] = None
        else:
            metadata = member.metadata
        return Gossip(source=local.source, name=member.name,
                      clock=member.clock, status=member.status,
                      metadata=metadata)

    def _apply_gossip(self, local: Member, source: Member, member: Member,
                      gossip: Gossip) -> GossipAck:
        self._handle_status(member, gossip.status)
        self.members.apply(member, source, gossip.clock,
                           status=gossip.status,
                           metadata=gossip.metadata)
        return GossipAck(source=local.source, name=gossip.name,
                         clock=gossip.clock)

    async def _wait(self, target: Member, timeout: float) -> bool:
        event = Event()
        self._add_waiting(target, event)
        with suppress(TimeoutError):
            await asyncio.wait_for(event.wait(), timeout)
        return event.is_set()

    def _handle_status(self, target: Member, status: Status) -> None:
        if status == Status.SUSPECT:
            suspect_task = self._suspect.get(target)
            if suspect_task is None:
                self._suspect[target] = asyncio.create_task(
                    self._suspect_wait(target))
        else:
            suspect_task = self._suspect.pop(target, None)
            if suspect_task is not None:
                suspect_task.cancel()

    async def _suspect_wait(self, target: Member) -> None:
        await asyncio.sleep(self.config.suspect_timeout)
        self.members.update(target, new_status=Status.OFFLINE)
        _ = self._suspect.pop(target, None)

    @final
    async def check(self, target: Member) -> None:
        """Attempts to determine if *target* is responding, setting it to
        :term:`suspect` if it does not respond with an :term:`ack`.

        See Also:
            :ref:`Failure Detection`

        Args:
            target: The cluster member to check.

        """
        local = self.members.local
        await self._send(target, Ping(source=local.source))
        online = await self._wait(target, self.config.ping_timeout)
        if not online:
            count = self.config.ping_req_count
            indirects = self.members.find(
                count, status=Status.AVAILABLE, exclude={target})
            if indirects:
                ping_req = PingReq(source=local.source, target=target.name)
                await asyncio.wait([
                    asyncio.create_task(self._send(indirect, ping_req))
                    for indirect in indirects])
                online = await self._wait(target, self.config.ping_req_timeout)
        new_status = Status.ONLINE if online else Status.SUSPECT
        self._handle_status(target, new_status)
        self.members.update(target, new_status=new_status)

    @final
    async def disseminate(self, target: Member) -> None:
        """Sends any :term:`gossip` that might be needed by *target*.

        See Also:
            :ref:`Dissemination`

        Args:
            target: The cluster member to disseminate to updates to.

        """
        local = self.members.local
        for member in self.members.get_gossip(target):
            packet = self._build_gossip(local, member)
            await self._send(target, packet)

    async def run_failure_detection(self) -> NoReturn:
        """Indefinitely send failure detection packets to other cluster
        members.

        .. note::

           Override this method to control when and how :meth:`.check` is
           called. By default, one random cluster member is chosen every
           :class:`ping_interval <swimprotocol.config.Config>` seconds.

        """
        while True:
            targets = self.members.find(1)
            assert targets
            for target in targets:
                self.run_subtask(self.check(target))
            await asyncio.sleep(self.config.ping_interval)

    async def run_dissemination(self) -> NoReturn:
        """Indefinitely send dissemination packets to other cluster members.

        .. note::

           Override this method to control when and how :meth:`.disseminate` is
           called. By default, one random cluster member is chosen every
           :class:`sync_interval <swimprotocol.config.Config>` seconds.

        """
        while True:
            targets = self.members.find(1, status=Status.AVAILABLE)
            for target in targets:
                self.run_subtask(self.disseminate(target))
            await asyncio.sleep(self.config.sync_interval)

    @final
    async def run(self) -> NoReturn:
        """Indefinitely handle received SWIM protocol packets and, at
        configurable intervals, send failure detection and dissemination
        packets. This method calls :meth:`.run_failure_detection` and
        :meth:`.run_dissemination`.

        """
        await asyncio.gather(
            self._run_handler(),
            self.run_failure_detection(),
            self.run_dissemination())
        raise RuntimeError()
