"""Regression test: SessionEventLog serializes each event exactly once.

Before the fix, append() ran json.dumps(data) only to measure payload_bytes
(discarding the string), and the SSE drain re-serialized the same event with
json.dumps({**data, "seq": seq}). Large payloads were thus JSON-encoded twice
on the event loop, starving the sandbox /health probe under heavy agent load.

After the fix, append() serializes once (with seq merged in), stores the JSON
on the event as `data_json`, and derives payload_bytes from len(data_json).
The drain reuses data_json verbatim — no second dumps anywhere.
"""

import json

import pytest

from sdk.event_log import SessionEventLog, SessionEventLogOverflow


class TestEventLogSingleSerialize:
    """Verify each event is serialized once and data_json is wire-correct."""

    def test_data_json_includes_seq_and_matches_data(self) -> None:
        """data_json equals json.dumps of the payload with seq merged in."""
        log = SessionEventLog(max_bytes=10_000)
        seq = log.append("tool_result", {"value": 42, "name": "x"})

        events = log._events
        assert len(events) == 1
        ev = events[0]

        assert ev.seq == seq
        assert json.loads(ev.data_json) == {"value": 42, "name": "x", "seq": seq}

    def test_payload_bytes_equals_data_json_length(self) -> None:
        """payload_bytes is the byte length of the single serialization."""
        log = SessionEventLog(max_bytes=10_000)
        log.append("e", {"k": "a long-ish string payload to size"})

        ev = log._events[0]
        assert ev.payload_bytes == len(ev.data_json)

    def test_total_bytes_tracks_serialized_size(self) -> None:
        """Running total equals the sum of each event's data_json length."""
        log = SessionEventLog(max_bytes=10_000)
        log.append("a", {"x": 1})
        log.append("b", {"y": [1, 2, 3]})

        expected = sum(len(e.data_json) for e in log._events)
        assert log._total_bytes == expected

    def test_overflow_trips_on_serialized_size(self) -> None:
        """Overflow fires when the serialized total exceeds max_bytes, and the
        overflow event itself carries a wire-ready data_json."""
        # Tiny budget so the second append overflows.
        log = SessionEventLog(max_bytes=40)
        log.append("first", {"a": "x"})

        with pytest.raises(SessionEventLogOverflow):
            log.append("second", {"b": "a value large enough to exceed the budget"})

        overflow = log._events[-1]
        assert overflow.event == "session_event_log_overflow"
        decoded = json.loads(overflow.data_json)
        assert decoded["seq"] == overflow.seq
        assert "total_bytes" in decoded and "max_bytes" in decoded
