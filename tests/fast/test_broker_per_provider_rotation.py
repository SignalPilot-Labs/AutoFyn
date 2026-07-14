"""The broker's per-provider rotation bookmarks must be independent.

acquire() is provider-agnostic: the caller filters the pool to one provider's
tokens and passes that subset plus a per-provider rotation key
(``claude_token_index:{provider}``). Two providers therefore rotate on two
distinct Setting rows. This asserts the property that makes that safe: acquiring
for provider A advances only A's bookmark and never disturbs B's, so interleaved
runs of different providers each cycle their own subset in order.

This drives the REAL broker + REAL rotation_key_for against an in-memory SQLite
session (the acquire path), complementing test_token_pool_per_provider_marker,
which covers only the dashboard's read-side "Next" marker.
"""

from __future__ import annotations

from collections.abc import AsyncIterator
from typing import Any

import pytest
import pytest_asyncio
from sqlalchemy import event
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from db.constants import CLAUDE_TOKEN_INDEX_KEY
from common.broker import CredentialBroker, SelectedCredential
from common.constants import PROVIDER_ANTHROPIC, PROVIDER_OPENROUTER, rotation_key_for
from common.models import Token
from db.models import CredentialHealth, Setting

_ANTHROPIC = [
    Token(provider=PROVIDER_ANTHROPIC, value="sk-ant-aaa", label=None),
    Token(provider=PROVIDER_ANTHROPIC, value="sk-ant-bbb", label=None),
]
_OPENROUTER = [
    Token(provider=PROVIDER_OPENROUTER, value="sk-or-v1-xxx", label=None),
    Token(provider=PROVIDER_OPENROUTER, value="sk-or-v1-yyy", label=None),
    Token(provider=PROVIDER_OPENROUTER, value="sk-or-v1-zzz", label=None),
]
_KEY_ANTHROPIC = rotation_key_for(PROVIDER_ANTHROPIC, CLAUDE_TOKEN_INDEX_KEY)
_KEY_OPENROUTER = rotation_key_for(PROVIDER_OPENROUTER, CLAUDE_TOKEN_INDEX_KEY)


class TestBrokerPerProviderRotation:
    """Each provider's rotation bookmark advances independently on the acquire path."""

    @pytest_asyncio.fixture
    async def session(self) -> AsyncIterator[AsyncSession]:
        """Yield an in-memory SQLite AsyncSession with broker tables created."""
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

    async def _acquire(
        self, session: AsyncSession, tokens: list[Token], key: str
    ) -> int:
        """acquire once, commit, return the picked subset index."""
        result = await CredentialBroker(session).acquire(tokens, key)
        assert isinstance(result, SelectedCredential)
        await session.commit()
        return result.index

    @pytest.mark.asyncio
    async def test_two_providers_rotate_on_independent_bookmarks(
        self, session: AsyncSession
    ) -> None:
        """Interleaved acquires cycle each provider's own subset, in order, unaffected by the other."""
        # Interleave: A, B, A, B, A, B, A ... across differently-sized subsets.
        anthropic_picks = []
        openrouter_picks = []
        for _ in range(3):
            anthropic_picks.append(await self._acquire(session, _ANTHROPIC, _KEY_ANTHROPIC))
            openrouter_picks.append(await self._acquire(session, _OPENROUTER, _KEY_OPENROUTER))

        # A cycles its 2-token subset; B cycles its 3-token subset — neither perturbs the other.
        assert anthropic_picks == [0, 1, 0]
        assert openrouter_picks == [0, 1, 2]

    @pytest.mark.asyncio
    async def test_acquire_writes_only_its_provider_bookmark(
        self, session: AsyncSession
    ) -> None:
        """Acquiring for one provider leaves the other provider's bookmark row absent."""
        await self._acquire(session, _ANTHROPIC, _KEY_ANTHROPIC)

        assert await session.get(Setting, _KEY_ANTHROPIC) is not None
        # OpenRouter was never acquired, so its bookmark must not exist.
        assert await session.get(Setting, _KEY_OPENROUTER) is None
