"""SessionEventLog — append-only sequenced event log for SSE streaming.

Replaces the lossy asyncio.Queue. Every event gets a monotonic seq number.
No drops — overflow fails the session loudly. Supports reconnection via
read_after(seq) and memory trimming via trim_through(seq).
"""

import asyncio
import json
import logging
from dataclasses import dataclass

log = logging.getLogger("sandbox.event_log")


class SessionEventLogOverflow(Exception):
    """Raised when the event log exceeds max_bytes."""

    def __init__(self, total_bytes: int, max_bytes: int) -> None:
        self.total_bytes = total_bytes
        self.max_bytes = max_bytes
        super().__init__(f"Event log overflow: {total_bytes}/{max_bytes} bytes")


class SessionEventGap(Exception):
    """Raised when requested after_seq is below the low-water mark (trimmed away)."""

    def __init__(self, requested_seq: int, low_water_mark: int) -> None:
        self.requested_seq = requested_seq
        self.low_water_mark = low_water_mark
        super().__init__(
            f"Event gap: requested after_seq={requested_seq} "
            f"but low_water_mark={low_water_mark}"
        )


@dataclass(frozen=True)
class SessionEvent:
    """A single sequenced event in the log.

    `data` is the raw event payload (kept for readers/tests). `data_json`
    is that payload serialized once at append time (with `seq` merged in),
    so the SSE drain writes it without re-serializing. `payload_bytes` is
    its byte length — derived from the same serialization, never a second
    dumps.
    """

    seq: int
    event: str
    data: dict
    data_json: str
    payload_bytes: int


SESSION_EVENT_LOG_MAX_BYTES: int = 50 * 1024 * 1024  # 50MB


class SessionEventLog:
    """Append-only event log with sequenced reads. One per session.

    Public API:
        append(event, data)          — add an event, fail loudly on overflow
        read_after(after_seq)        — return events with seq > after_seq (async, waits)
        trim_through(seq)            — discard events with seq <= N, free bytes
        latest_seq                   — current sequence number (property)
    """

    def __init__(self, max_bytes: int) -> None:
        self._events: list[SessionEvent] = []
        self._seq: int = 0
        self._total_bytes: int = 0
        self._max_bytes = max_bytes
        self._failed: bool = False
        self._low_water_mark: int = 0
        self._notify: asyncio.Event = asyncio.Event()

    @property
    def latest_seq(self) -> int:
        """Return the latest sequence number."""
        return self._seq

    def append(self, event: str, data: dict) -> int:
        """Append an event. Returns the assigned seq. Fails loudly if log is full.

        Serializes `data` (with `seq` merged in) exactly once here; the SSE
        drain reuses the stored JSON. `payload_bytes` is the byte length of
        that single serialization — no second dumps anywhere on the path.
        """
        if self._failed:
            raise SessionEventLogOverflow(self._total_bytes, self._max_bytes)
        next_seq = self._seq + 1
        data_json = json.dumps({**data, "seq": next_seq})
        payload_bytes = len(data_json)
        if self._total_bytes + payload_bytes > self._max_bytes:
            self._seq = next_seq
            overflow_data = {"total_bytes": self._total_bytes, "max_bytes": self._max_bytes}
            overflow_json = json.dumps({**overflow_data, "seq": next_seq})
            self._events.append(SessionEvent(
                seq=next_seq,
                event="session_event_log_overflow",
                data=overflow_data,
                data_json=overflow_json,
                payload_bytes=len(overflow_json),
            ))
            self._failed = True
            self._notify.set()
            raise SessionEventLogOverflow(self._total_bytes, self._max_bytes)
        self._seq = next_seq
        self._events.append(SessionEvent(
            seq=next_seq, event=event, data=data, data_json=data_json, payload_bytes=payload_bytes,
        ))
        self._total_bytes += payload_bytes
        self._notify.set()
        return next_seq

    async def read_after(self, after_seq: int, timeout: float) -> list[SessionEvent]:
        """Return events with seq > after_seq. Waits if none available.

        Raises SessionEventGap if after_seq < low_water_mark (trimmed away).
        Raises asyncio.TimeoutError if timeout expires with no new events.
        """
        while True:
            if after_seq < self._low_water_mark:
                raise SessionEventGap(after_seq, self._low_water_mark)
            events = [e for e in self._events if e.seq > after_seq]
            if events:
                return events
            self._notify.clear()
            await asyncio.wait_for(self._notify.wait(), timeout=timeout)

    def trim_through(self, seq: int) -> None:
        """Discard events with seq <= N, free their bytes, advance low-water mark."""
        trimmed_bytes = sum(e.payload_bytes for e in self._events if e.seq <= seq)
        self._events = [e for e in self._events if e.seq > seq]
        self._total_bytes = max(0, self._total_bytes - trimmed_bytes)
        self._low_water_mark = max(self._low_water_mark, seq)
