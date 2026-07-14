"""Regression test: a zero cost must not erase an estimate for a round that spent tokens.

A gateway that does not bill through Anthropic (OpenRouter) reports
total_cost_usd: 0.0 rather than omitting the field. `round_cost is not None`
accepted that zero as authoritative, so the token-derived estimate for a round
that demonstrably burned tokens was rebased to $0.00 — the run then rendered a
confident zero cost while having spent real money. A zero is only authoritative
when the round's token counters also stood still.
"""

from __future__ import annotations

from unittest.mock import AsyncMock, patch

import pytest

from tests.fast.conftest import _make_dispatcher


class TestZeroCostWithTokensDoesNotRebase:
    """A 0.0 cost is authoritative only when the round consumed no tokens."""

    @pytest.mark.asyncio
    async def test_zero_cost_after_spending_tokens_keeps_estimate(self) -> None:
        """Gateway-reported 0.0 must not overwrite an estimate backed by tokens."""
        dispatcher, _ = _make_dispatcher()
        dispatcher._run.total_cost = 0.05
        dispatcher._cost_baseline = 0.0
        dispatcher._run.total_output_tokens = 52147
        dispatcher._output_baseline = 0

        with patch("agent_session.stream.db.save_session_id", new=AsyncMock()):
            with patch("agent_session.stream.db.update_run_cost", new=AsyncMock()):
                await dispatcher.dispatch(
                    {
                        "event": "result",
                        "data": {"session_id": "s", "total_cost_usd": 0.0},
                    }
                )

        assert dispatcher._run.total_cost == 0.05

    @pytest.mark.asyncio
    async def test_zero_cost_after_spending_input_tokens_keeps_estimate(self) -> None:
        """Input-only rounds count as spend too."""
        dispatcher, _ = _make_dispatcher()
        dispatcher._run.total_cost = 0.05
        dispatcher._cost_baseline = 0.0
        dispatcher._run.total_input_tokens = 3487
        dispatcher._input_baseline = 0

        with patch("agent_session.stream.db.save_session_id", new=AsyncMock()):
            with patch("agent_session.stream.db.update_run_cost", new=AsyncMock()):
                await dispatcher.dispatch(
                    {
                        "event": "result",
                        "data": {"session_id": "s", "total_cost_usd": 0.0},
                    }
                )

        assert dispatcher._run.total_cost == 0.05

    @pytest.mark.asyncio
    async def test_zero_cost_with_no_tokens_still_rebases(self) -> None:
        """A round that spent nothing must still settle to zero, not drift."""
        dispatcher, _ = _make_dispatcher()
        dispatcher._run.total_cost = 0.05
        dispatcher._cost_baseline = 0.0

        with patch("agent_session.stream.db.save_session_id", new=AsyncMock()):
            with patch("agent_session.stream.db.update_run_cost", new=AsyncMock()):
                await dispatcher.dispatch(
                    {
                        "event": "result",
                        "data": {"session_id": "s", "total_cost_usd": 0.0},
                    }
                )

        assert dispatcher._run.total_cost == 0.0

    @pytest.mark.asyncio
    async def test_nonzero_cost_after_spending_tokens_still_rebases(self) -> None:
        """A real billed cost stays authoritative regardless of token spend."""
        dispatcher, _ = _make_dispatcher()
        dispatcher._run.total_cost = 0.05
        dispatcher._cost_baseline = 0.0
        dispatcher._run.total_output_tokens = 52147
        dispatcher._output_baseline = 0

        with patch("agent_session.stream.db.save_session_id", new=AsyncMock()):
            with patch("agent_session.stream.db.update_run_cost", new=AsyncMock()):
                await dispatcher.dispatch(
                    {
                        "event": "result",
                        "data": {"session_id": "s", "total_cost_usd": 0.12},
                    }
                )

        assert dispatcher._run.total_cost == pytest.approx(0.12)
