"""Regression test: a run with no usage reported must record NULL, not 0.

runs.total_cost_usd was NOT NULL DEFAULT 0, so "no usage has arrived yet",
"the accounting pipeline is broken", and "this run genuinely cost nothing"
were all stored as 0.0 and rendered as a confident $0.00. StatsBar already
had a correct three-state formatter whose "—" branch was unreachable because
the API could never send null.

RunContext.total_cost now starts as None and only becomes a float once usage
actually arrives, so the distinction survives to the DB and the frontend.
"""

from __future__ import annotations

from unittest.mock import AsyncMock, patch

import pytest

from tests.fast.conftest import _make_dispatcher
from tests.fast.test_stream_event_usage import ANTHROPIC_DELTA


class TestUnknownCostIsNull:
    """Cost stays None until usage is reported, then becomes a real number."""

    def test_fresh_run_has_unknown_cost(self) -> None:
        """Before any usage, cost is unknown — not zero."""
        dispatcher, _ = _make_dispatcher()

        assert dispatcher._run.total_cost is None

    @pytest.mark.asyncio
    async def test_cost_becomes_real_once_usage_arrives(self) -> None:
        """The first delta settles cost into a concrete number."""
        dispatcher, _ = _make_dispatcher()

        with patch("agent_session.stream.log_audit", new=AsyncMock()):
            await dispatcher.dispatch(
                {"event": "stream_event", "data": {"event": ANTHROPIC_DELTA}}
            )

        assert dispatcher._run.total_cost is not None
        assert dispatcher._run.total_cost > 0

    @pytest.mark.asyncio
    async def test_confirmed_zero_is_not_unknown(self) -> None:
        """A round the SDK bills at exactly $0.00 is known, and stays 0.0."""
        dispatcher, _ = _make_dispatcher()

        with patch("agent_session.stream.db.save_session_id", new=AsyncMock()):
            with patch("agent_session.stream.db.update_run_cost", new=AsyncMock()):
                await dispatcher.dispatch(
                    {
                        "event": "result",
                        "data": {"session_id": "s", "total_cost_usd": 0.0},
                    }
                )

        assert dispatcher._run.total_cost == 0.0
