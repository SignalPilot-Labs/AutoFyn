"""Concurrency-safety guards for the credential broker.

Production runs Postgres, where acquire() serializes on a FOR UPDATE lock of the
rotation row and report_exhausted() upserts with GREATEST. SQLite cannot
reproduce a live row-lock race (FOR UPDATE is a no-op and writes serialize
anyway), so these tests assert the observable outcomes the lock and the GREATEST
upsert exist to guarantee, by driving the real broker under sequential
interleaving:

- rotation advances exactly once per acquire and cycles the pool in order;
- a later report with a nearer reset never shortens an existing cooldown.

Both are mutation-verified: reverting the write-back or the GREATEST makes the
matching test fail. The live race itself only manifests on Postgres.
"""

from __future__ import annotations

from collections.abc import AsyncIterator
from datetime import datetime, timedelta, timezone
from typing import Any

import pytest
import pytest_asyncio
from sqlalchemy import event
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from common.broker import CredentialBroker, Lease
from db.constants import PROVIDER_ANTHROPIC
from db.models import CredentialHealth

_ROTATION_KEY = "claude_token_index"
_IDS = ["anthropic:aaa", "anthropic:bbb", "anthropic:ccc"]


def _as_utc(dt: datetime) -> datetime:
    """Attach UTC to a naive datetime (SQLite drops tzinfo on round-trip)."""
    return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)


class TestBrokerConcurrency:
    """The broker's rotation lock and cooldown upsert must survive concurrent runs."""

    @pytest_asyncio.fixture
    async def session(self) -> AsyncIterator[AsyncSession]:
        """Yield an in-memory SQLite AsyncSession with a greatest() shim."""
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
    async def test_rotation_advances_once_per_acquire(self, session: AsyncSession) -> None:
        """N sequential acquires cycle the pool exactly once each, in order."""
        broker = CredentialBroker(session)
        picked = []
        for _ in range(len(_IDS) * 2):
            result = await broker.acquire(PROVIDER_ANTHROPIC, _IDS, _ROTATION_KEY)
            assert isinstance(result, Lease)
            picked.append(result.index)
            await session.commit()
        assert picked == [0, 1, 2, 0, 1, 2]

    @pytest.mark.asyncio
    async def test_interleaved_reports_keep_longest_cooldown(self, session: AsyncSession) -> None:
        """A later report with a nearer reset never shortens an existing cooldown."""
        broker = CredentialBroker(session)
        now = datetime.now(timezone.utc)
        far = now + timedelta(hours=3)

        await broker.report_exhausted(_IDS[0], now + timedelta(minutes=10))
        await broker.report_exhausted(_IDS[0], far)
        await broker.report_exhausted(_IDS[0], now + timedelta(minutes=1))

        row = await session.get(CredentialHealth, _IDS[0])
        assert row is not None
        assert row.cooldown_until is not None
        assert _as_utc(row.cooldown_until) == far
