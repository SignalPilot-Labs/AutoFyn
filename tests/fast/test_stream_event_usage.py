"""Regression test: usage must be read from the message_delta stream event.

Usage was read from AssistantMessage, which reflects message_start. Anthropic
populates that event, but OpenRouter zeroes it and settles usage only in the
final message_delta — so every OpenRouter run recorded 0 tokens and $0.00 while
spending real money. The delta was already reaching the dispatcher as a
stream_event and being dropped: the dispatch table had no handler for it.

message_delta is the only event both providers populate, and OpenRouter's
carries the gateway's actual billed cost, which beats the Opus-rate estimate.
Payloads below are verbatim from live calls to each provider.
"""

from __future__ import annotations

from unittest.mock import AsyncMock, patch

import pytest

from tests.fast.conftest import _make_dispatcher

OPENROUTER_DELTA = {
    "type": "message_delta",
    "usage": {
        "input_tokens": 3,
        "output_tokens": 9,
        "cache_creation_input_tokens": 14665,
        "cache_read_input_tokens": 0,
        "cache_creation": None,
        "service_tier": "standard",
        "cost": 0.09194125,
        "is_byok": False,
    },
}

ANTHROPIC_DELTA = {
    "type": "message_delta",
    "usage": {
        "input_tokens": 3,
        "cache_creation_input_tokens": 1797,
        "cache_read_input_tokens": 8177,
        "output_tokens": 8,
    },
}

OPENROUTER_MESSAGE_START = {
    "type": "message_start",
    "message": {
        "usage": {
            "input_tokens": 0,
            "output_tokens": 0,
            "cache_creation_input_tokens": None,
            "cache_read_input_tokens": None,
        }
    },
}


class TestStreamEventUsage:
    """The dispatcher must count message_delta usage and prefer gateway cost."""

    @pytest.mark.asyncio
    async def test_openrouter_delta_records_tokens_and_gateway_cost(self) -> None:
        """OpenRouter's delta must yield real tokens and its own billed cost."""
        dispatcher, _ = _make_dispatcher()

        with patch("agent_session.stream.log_audit", new=AsyncMock()):
            await dispatcher.dispatch(
                {"event": "stream_event", "data": {"event": OPENROUTER_DELTA}}
            )

        run = dispatcher._run
        assert run.total_input_tokens == 3
        assert run.total_output_tokens == 9
        assert run.cache_creation_input_tokens == 14665
        assert run.total_cost == pytest.approx(0.09194125)

    @pytest.mark.asyncio
    async def test_anthropic_delta_records_tokens_and_estimates_cost(self) -> None:
        """Anthropic sends no cost, so the rate estimate must still apply."""
        dispatcher, _ = _make_dispatcher()

        with patch("agent_session.stream.log_audit", new=AsyncMock()):
            await dispatcher.dispatch(
                {"event": "stream_event", "data": {"event": ANTHROPIC_DELTA}}
            )

        run = dispatcher._run
        assert run.total_input_tokens == 3
        assert run.total_output_tokens == 8
        assert run.cache_read_input_tokens == 8177
        assert run.total_cost is not None and run.total_cost > 0

    @pytest.mark.asyncio
    async def test_message_start_is_ignored(self) -> None:
        """Only the delta settles usage; message_start must not be counted."""
        dispatcher, _ = _make_dispatcher()

        with patch("agent_session.stream.log_audit", new=AsyncMock()):
            await dispatcher.dispatch(
                {"event": "stream_event", "data": {"event": OPENROUTER_MESSAGE_START}}
            )

        run = dispatcher._run
        assert run.total_input_tokens == 0
        assert run.total_output_tokens == 0
        assert run.total_cost is None

    @pytest.mark.asyncio
    async def test_gateway_cost_survives_zero_cost_result(self) -> None:
        """OpenRouter's result reports 0.0; it must not erase the real cost."""
        dispatcher, _ = _make_dispatcher()

        with patch("agent_session.stream.log_audit", new=AsyncMock()):
            await dispatcher.dispatch(
                {"event": "stream_event", "data": {"event": OPENROUTER_DELTA}}
            )
        with patch("agent_session.stream.db.save_session_id", new=AsyncMock()):
            with patch("agent_session.stream.db.update_run_cost", new=AsyncMock()):
                await dispatcher.dispatch(
                    {
                        "event": "result",
                        "data": {"session_id": "s", "total_cost_usd": 0.0},
                    }
                )

        assert dispatcher._run.total_cost == pytest.approx(0.09194125)

    @pytest.mark.asyncio
    async def test_anthropic_result_still_settles_cost(self) -> None:
        """With no gateway cost, ResultMessage stays authoritative."""
        dispatcher, _ = _make_dispatcher()

        with patch("agent_session.stream.log_audit", new=AsyncMock()):
            await dispatcher.dispatch(
                {"event": "stream_event", "data": {"event": ANTHROPIC_DELTA}}
            )
        with patch("agent_session.stream.db.save_session_id", new=AsyncMock()):
            with patch("agent_session.stream.db.update_run_cost", new=AsyncMock()):
                await dispatcher.dispatch(
                    {
                        "event": "result",
                        "data": {"session_id": "s", "total_cost_usd": 0.00932085},
                    }
                )

        assert dispatcher._run.total_cost == pytest.approx(0.00932085)

    @pytest.mark.asyncio
    async def test_gateway_costs_accumulate_across_deltas(self) -> None:
        """Each delta bills its own turn; the round total is their sum."""
        dispatcher, _ = _make_dispatcher()

        with patch("agent_session.stream.log_audit", new=AsyncMock()):
            for _ in range(3):
                await dispatcher.dispatch(
                    {"event": "stream_event", "data": {"event": OPENROUTER_DELTA}}
                )

        assert dispatcher._run.total_cost == pytest.approx(0.09194125 * 3)
