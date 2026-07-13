"""Regression test: report_round_outcome consumes rate_limit_resets_at per round.

Bug: Run.rate_limit_resets_at was written when a round hit a rate limit but
never cleared. report_round_outcome read it every round, so a later round that
hit NO limit still saw the stale future timestamp and cooled down its own
(innocent, healthy) credential — the opposite of the broker's goal.

Fix: report_round_outcome clears rate_limit_resets_at in the same transaction
it reads it. It is now a per-round signal: only a round that itself set the
timestamp cools down its credential.
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from lifecycle.credentials import report_round_outcome

_CRED_ID = "anthropic:aaa"


def _session_with_run(run: MagicMock | None) -> tuple[MagicMock, MagicMock]:
    """Build a mock session whose get() returns run, plus its factory."""
    session = MagicMock()
    session.get = AsyncMock(return_value=run)
    session.commit = AsyncMock()
    ctx = AsyncMock()
    ctx.__aenter__ = AsyncMock(return_value=session)
    ctx.__aexit__ = AsyncMock(return_value=False)
    factory = MagicMock(return_value=ctx)
    return session, factory


class TestReportRoundOutcome:
    """report_round_outcome must treat rate_limit_resets_at as a per-round signal."""

    @pytest.mark.asyncio
    async def test_future_timestamp_cools_down_and_clears(self) -> None:
        """A future reset cools down the round's credential and clears the field."""
        future = int((datetime.now(timezone.utc) + timedelta(hours=1)).timestamp())
        run = MagicMock()
        run.rate_limit_resets_at = future
        session, factory = _session_with_run(run)
        broker = MagicMock(report_exhausted=AsyncMock())

        with (
            patch("lifecycle.credentials.get_session_factory", return_value=factory),
            patch("lifecycle.credentials.CredentialBroker", return_value=broker),
        ):
            await report_round_outcome("run-1", _CRED_ID)

        broker.report_exhausted.assert_awaited_once()
        assert broker.report_exhausted.await_args[0][0] == _CRED_ID
        assert run.rate_limit_resets_at is None
        session.commit.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_no_timestamp_cools_down_nothing(self) -> None:
        """A round whose timestamp is already cleared must not cool down its credential."""
        run = MagicMock()
        run.rate_limit_resets_at = None
        session, factory = _session_with_run(run)
        broker = MagicMock(report_exhausted=AsyncMock())

        with (
            patch("lifecycle.credentials.get_session_factory", return_value=factory),
            patch("lifecycle.credentials.CredentialBroker", return_value=broker),
        ):
            await report_round_outcome("run-1", _CRED_ID)

        broker.report_exhausted.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_past_timestamp_clears_without_cooldown(self) -> None:
        """An already-elapsed reset clears the field but cools down nothing."""
        past = int((datetime.now(timezone.utc) - timedelta(hours=1)).timestamp())
        run = MagicMock()
        run.rate_limit_resets_at = past
        session, factory = _session_with_run(run)
        broker = MagicMock(report_exhausted=AsyncMock())

        with (
            patch("lifecycle.credentials.get_session_factory", return_value=factory),
            patch("lifecycle.credentials.CredentialBroker", return_value=broker),
        ):
            await report_round_outcome("run-1", _CRED_ID)

        broker.report_exhausted.assert_not_awaited()
        assert run.rate_limit_resets_at is None
        session.commit.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_missing_run_is_noop(self) -> None:
        """A missing run must not touch the broker or commit."""
        session, factory = _session_with_run(None)
        broker = MagicMock(report_exhausted=AsyncMock())

        with (
            patch("lifecycle.credentials.get_session_factory", return_value=factory),
            patch("lifecycle.credentials.CredentialBroker", return_value=broker),
        ):
            await report_round_outcome("run-1", _CRED_ID)

        broker.report_exhausted.assert_not_awaited()
        session.commit.assert_not_awaited()
