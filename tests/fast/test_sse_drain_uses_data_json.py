"""Regression test: handle_events streams the event's stored data_json.

The SSE drain must write SessionEvent.data_json verbatim (which already
includes the merged seq) rather than re-serializing the payload. This
guards the production wiring in api.session.handle_events that pairs with
the single-serialization change in sdk.event_log.
"""

from __future__ import annotations

import json
from unittest.mock import MagicMock

import pytest
from aiohttp import web
from aiohttp.test_utils import make_mocked_request

from sandbox.api.session import handle_events
from sdk.event_log import SessionEventLog


class _CapturingStreamResponse(web.StreamResponse):
    """StreamResponse that records written bytes instead of needing a transport."""

    def __init__(self) -> None:
        super().__init__()
        self.written: list[bytes] = []

    async def prepare(self, request: web.Request) -> None:  # type: ignore[override]
        return None

    async def write(self, data: bytes) -> None:  # type: ignore[override]
        self.written.append(data)


class TestSseDrainUsesDataJson:
    """handle_events must emit the stored data_json (with seq) verbatim."""

    @pytest.mark.asyncio
    async def test_streamed_frame_contains_data_json_with_seq(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """The SSE data line equals the event's data_json and carries seq."""
        log = SessionEventLog(max_bytes=10_000)
        seq = log.append("tool_use", {"value": 42})
        # session_end terminates the drain loop so the coroutine returns.
        log.append("session_end", {})

        request = make_mocked_request(
            "GET",
            "/session/sess-1/events?after_seq=0",
            match_info={"session_id": "sess-1"},
        )
        sessions = MagicMock()
        sessions.get_event_log = MagicMock(return_value=log)
        request.app["sessions"] = sessions

        captured = _CapturingStreamResponse()
        monkeypatch.setattr(web, "StreamResponse", lambda: captured)

        await handle_events(request)

        frames = b"".join(captured.written).decode("utf-8")
        # The first event's data line must be exactly its stored data_json.
        assert f"data: {json.dumps({'value': 42, 'seq': seq})}\n\n" in frames
        assert f"id: {seq}\nevent: tool_use\n" in frames
