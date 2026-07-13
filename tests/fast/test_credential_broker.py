"""Behavior tests for the health-aware credential broker against a real SQLite DB.

Exercises acquire round-robin, cooldown skipping, WaitDirective, and the
report_* health mutators using an in-memory aiosqlite AsyncSession so the
broker's real select/get/add paths run end to end.
"""

from __future__ import annotations

from collections.abc import AsyncIterator
from datetime import datetime, timedelta, timezone
from typing import Any

import pytest
import pytest_asyncio
from sqlalchemy import event
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from db.constants import CREDENTIAL_DEFAULT_COOLDOWN_SECONDS, PROVIDER_ANTHROPIC
from common.broker import CredentialBroker, Lease, WaitDirective, credential_id
from db.models import CredentialHealth

_ROTATION_KEY = "claude_token_index"
_IDS = ["anthropic:aaa", "anthropic:bbb", "anthropic:ccc"]


def _as_utc(dt: datetime) -> datetime:
    """Attach UTC to a naive datetime (SQLite drops tzinfo on round-trip)."""
    return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)


class TestCredentialBroker:
    """Broker selection and health mutation against a real in-memory session."""

    @pytest_asyncio.fixture
    async def session(self) -> AsyncIterator[AsyncSession]:
        """Yield a fresh in-memory SQLite AsyncSession with broker tables created.

        Production runs Postgres; report_exhausted uses its scalar greatest().
        SQLite has no greatest(), so register a Python shim on the connection so
        the real upsert path runs end to end here instead of a weakened variant.
        """
        engine = create_async_engine("sqlite+aiosqlite:///:memory:")

        @event.listens_for(engine.sync_engine, "connect")
        def _register_greatest(dbapi_conn: Any, _record: object) -> None:
            dbapi_conn.create_function("greatest", 2, lambda a, b: max(a, b))

        tables = [CredentialHealth.metadata.tables[t] for t in ("credential_health", "settings")]
        async with engine.begin() as conn:
            await conn.run_sync(lambda c: CredentialHealth.metadata.create_all(c, tables=tables))
        maker = async_sessionmaker(engine, expire_on_commit=False)
        async with maker() as s:
            yield s
        await engine.dispose()

    @pytest.mark.asyncio
    async def test_round_robin_advances_rotation(self, session: AsyncSession) -> None:
        """No rotation bookmark picks index 0; the next acquire picks index 1."""
        broker = CredentialBroker(session)
        first = await broker.acquire(PROVIDER_ANTHROPIC, _IDS, _ROTATION_KEY)
        assert isinstance(first, Lease)
        assert first.index == 0

        second = await broker.acquire(PROVIDER_ANTHROPIC, _IDS, _ROTATION_KEY)
        assert isinstance(second, Lease)
        assert second.index == 1

    @pytest.mark.asyncio
    async def test_skips_cooling_down_id(self, session: AsyncSession) -> None:
        """A future cooldown on ids[0] makes acquire pick a different id."""
        broker = CredentialBroker(session)
        future = datetime.now(timezone.utc) + timedelta(hours=1)
        await broker.report_exhausted(_IDS[0], future)

        result = await broker.acquire(PROVIDER_ANTHROPIC, _IDS, _ROTATION_KEY)
        assert isinstance(result, Lease)
        assert result.credential_id != _IDS[0]

    @pytest.mark.asyncio
    async def test_all_cooling_down_returns_wait(self, session: AsyncSession) -> None:
        """When every id cools down, acquire returns the soonest wait_until."""
        broker = CredentialBroker(session)
        now = datetime.now(timezone.utc)
        soonest = now + timedelta(minutes=5)
        await broker.report_exhausted(_IDS[0], soonest)
        await broker.report_exhausted(_IDS[1], now + timedelta(minutes=10))
        await broker.report_exhausted(_IDS[2], now + timedelta(minutes=20))

        result = await broker.acquire(PROVIDER_ANTHROPIC, _IDS, _ROTATION_KEY)
        assert isinstance(result, WaitDirective)
        assert _as_utc(result.wait_until) == soonest

    @pytest.mark.asyncio
    async def test_empty_ids_raises(self, session: AsyncSession) -> None:
        """acquire with no ids raises ValueError."""
        with pytest.raises(ValueError):
            await CredentialBroker(session).acquire(PROVIDER_ANTHROPIC, [], _ROTATION_KEY)

    @pytest.mark.asyncio
    async def test_report_exhausted_none_uses_default_cooldown(self, session: AsyncSession) -> None:
        """reset_at=None sets cooldown to a future time (~now + default cooldown)."""
        before = datetime.now(timezone.utc)
        await CredentialBroker(session).report_exhausted(_IDS[0], None)

        row = await session.get(CredentialHealth, _IDS[0])
        assert row is not None
        assert row.cooldown_until is not None
        cooldown = _as_utc(row.cooldown_until)
        expected = before + timedelta(seconds=CREDENTIAL_DEFAULT_COOLDOWN_SECONDS)
        assert cooldown > before
        assert cooldown <= expected + timedelta(seconds=5)

    @pytest.mark.asyncio
    async def test_expired_cooldown_becomes_available(self, session: AsyncSession) -> None:
        """A cooldown in the past no longer blocks selection (automatic recovery)."""
        broker = CredentialBroker(session)
        past = datetime.now(timezone.utc) - timedelta(hours=1)
        await broker.report_exhausted(_IDS[0], past)

        result = await broker.acquire(PROVIDER_ANTHROPIC, [_IDS[0]], _ROTATION_KEY)
        assert isinstance(result, Lease)
        assert result.credential_id == _IDS[0]

    @pytest.mark.asyncio
    async def test_report_exhausted_never_shortens_cooldown(self, session: AsyncSession) -> None:
        """A second report with an earlier reset must not shorten an existing cooldown.

        Concurrent runs can both cool the same credential; the longer cooldown wins
        so a credential cannot be un-cooled early by a racing report with a nearer reset.
        """
        broker = CredentialBroker(session)
        now = datetime.now(timezone.utc)
        later = now + timedelta(hours=2)
        earlier = now + timedelta(minutes=5)

        await broker.report_exhausted(_IDS[0], later)
        await broker.report_exhausted(_IDS[0], earlier)

        row = await session.get(CredentialHealth, _IDS[0])
        assert row is not None
        assert row.cooldown_until is not None
        assert _as_utc(row.cooldown_until) == later

    @pytest.mark.asyncio
    async def test_credential_id_stable_and_provider_prefixed(self) -> None:
        """Same input yields the same id; a different provider yields a different id."""
        a = credential_id(PROVIDER_ANTHROPIC, "sk-ant-token")
        b = credential_id(PROVIDER_ANTHROPIC, "sk-ant-token")
        c = credential_id("openai", "sk-ant-token")

        assert a == b
        assert a.startswith(f"{PROVIDER_ANTHROPIC}:")
        assert a != c
