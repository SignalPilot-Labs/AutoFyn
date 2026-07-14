"""Regression test: a gateway that bills 0.0 is not a gateway that stayed silent.

_round_gateway_cost was a float starting at 0.0, and the branch that chose
between it and the rate estimate tested its truthiness. So a gateway reporting a
genuine `cost: 0.0` was indistinguishable from one that reported nothing, and
the round was billed at the Opus-rate estimate — inventing a charge for a round
the gateway told us was free. It is None until the gateway reports.
"""

from __future__ import annotations

from unittest.mock import AsyncMock, patch

import pytest

from tests.fast.conftest import _make_dispatcher

_FREE_DELTA = {
    "type": "message_delta",
    "usage": {
        "input_tokens": 1200,
        "output_tokens": 340,
        "cache_creation_input_tokens": 0,
        "cache_read_input_tokens": 8000,
        "cost": 0.0,
    },
}

_SILENT_DELTA = {
    "type": "message_delta",
    "usage": {
        "input_tokens": 1200,
        "output_tokens": 340,
        "cache_creation_input_tokens": 0,
        "cache_read_input_tokens": 8000,
    },
}


class TestGatewayZeroCostIsNotUnreported:
    """A reported 0.0 must win over the estimate; a silent gateway must not."""

    @pytest.mark.asyncio
    async def test_reported_zero_is_billed_as_zero(self) -> None:
        """The gateway said free, so the round is free — not rate-estimated."""
        dispatcher, _ = _make_dispatcher()

        with patch("agent_session.stream.log_audit", new=AsyncMock()):
            await dispatcher.dispatch(
                {"event": "stream_event", "data": {"event": _FREE_DELTA}}
            )

        assert dispatcher._run.total_cost == 0.0

    @pytest.mark.asyncio
    async def test_silent_gateway_falls_back_to_estimate(self) -> None:
        """With no cost reported, the same tokens must be rate-estimated."""
        dispatcher, _ = _make_dispatcher()

        with patch("agent_session.stream.log_audit", new=AsyncMock()):
            await dispatcher.dispatch(
                {"event": "stream_event", "data": {"event": _SILENT_DELTA}}
            )

        assert dispatcher._run.total_cost is not None
        assert dispatcher._run.total_cost > 0

    @pytest.mark.asyncio
    async def test_reported_zero_still_beats_the_result_message(self) -> None:
        """A confirmed-free round is not overwritten by the SDK's own figure."""
        dispatcher, _ = _make_dispatcher()

        with patch("agent_session.stream.log_audit", new=AsyncMock()):
            await dispatcher.dispatch(
                {"event": "stream_event", "data": {"event": _FREE_DELTA}}
            )
        with patch("agent_session.stream.db.save_session_id", new=AsyncMock()):
            with patch("agent_session.stream.db.update_run_cost", new=AsyncMock()):
                await dispatcher.dispatch(
                    {
                        "event": "result",
                        "data": {"session_id": "s", "total_cost_usd": 7.5},
                    }
                )

        assert dispatcher._run.total_cost == 0.0
