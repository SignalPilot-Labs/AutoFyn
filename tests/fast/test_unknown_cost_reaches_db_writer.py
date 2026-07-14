"""Regression test: an unsettled cost must reach the DB writer as None.

update_run_cost declared total_cost_usd as `float`, but _persist_cost passes
RunContext.total_cost, which is `float | None`, and _handle_result calls
_persist_cost unconditionally — so a ResultMessage carrying no cost sent None
through a parameter typed to forbid it.

Pyright cannot catch this: `standard` mode leaves strictParameterNoneValue off,
so `float | None` into `float` is accepted silently. This test is the check the
type system won't perform.
"""

from __future__ import annotations

from unittest.mock import AsyncMock, patch

import pytest

from tests.fast.conftest import _make_dispatcher
from tests.fast.test_stream_event_usage import ANTHROPIC_DELTA


class TestUnknownCostReachesDbWriter:
    """The None cost must survive the trip to update_run_cost, not become 0.0."""

    @pytest.mark.asyncio
    async def test_result_without_cost_writes_none(self) -> None:
        """A ResultMessage with no cost and no prior usage persists NULL."""
        dispatcher, _ = _make_dispatcher()
        writer = AsyncMock()

        with patch("agent_session.stream.db.save_session_id", new=AsyncMock()):
            with patch("agent_session.stream.db.update_run_cost", new=writer):
                await dispatcher.dispatch(
                    {"event": "result", "data": {"session_id": "s"}}
                )

        assert writer.await_args is not None
        assert writer.await_args.args[1] is None

    @pytest.mark.asyncio
    async def test_settled_cost_writes_a_float(self) -> None:
        """Once usage settles, the writer receives a real number, not None."""
        dispatcher, _ = _make_dispatcher()
        writer = AsyncMock()

        with patch("agent_session.stream.log_audit", new=AsyncMock()):
            await dispatcher.dispatch(
                {"event": "stream_event", "data": {"event": ANTHROPIC_DELTA}}
            )
        with patch("agent_session.stream.db.save_session_id", new=AsyncMock()):
            with patch("agent_session.stream.db.update_run_cost", new=writer):
                await dispatcher.dispatch(
                    {"event": "result", "data": {"session_id": "s", "total_cost_usd": 1.25}}
                )

        assert writer.await_args is not None
        assert writer.await_args.args[1] == pytest.approx(1.25)
