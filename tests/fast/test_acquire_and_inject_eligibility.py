"""Regression guard: acquire_and_inject's eligible-token filter is the cross-provider leak gate.

The broker is provider-agnostic — it rotates over whatever token list it is handed
and never checks provider. The ONLY thing stopping a GPT run from leasing a Claude
OAuth token (or a Claude run from leasing an OpenRouter key) is the filter in
acquire_and_inject: ``[t for t in read_pool() if t.provider == provider]``.

These tests drive the real filter + real _provider_env against a mocked broker,
asserting (a) only the run-provider's tokens ever reach broker.acquire, (b) the
injected env matches the selected token's provider, and (c) a run whose provider
has no tokens fails loud rather than borrowing another provider's credential. A
regression that inverted or dropped the filter would make these fail.
"""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from lifecycle.credentials import acquire_and_inject
from common.broker import SelectedCredential, credential_id
from common.constants import (
    ENV_ANTHROPIC_AUTH_TOKEN,
    ENV_ANTHROPIC_BASE_URL,
    ENV_CLAUDE_OAUTH_TOKEN,
    PROVIDER_ANTHROPIC,
    PROVIDER_OPENROUTER,
    SUPPORTED_GPT_SOL,
    SUPPORTED_OPUS,
)
from common.models import Token

_RUN_ID = "run-eligibility-0000"
# A mixed pool: two providers interleaved, so a broken filter would rotate across them.
_MIXED_POOL = [
    Token(provider=PROVIDER_ANTHROPIC, value="sk-ant-aaa", label=None),
    Token(provider=PROVIDER_OPENROUTER, value="sk-or-v1-bbb", label=None),
    Token(provider=PROVIDER_ANTHROPIC, value="sk-ant-ccc", label=None),
]


def _session_factory() -> MagicMock:
    """A no-op async-context session factory (the broker is fully mocked)."""
    session = MagicMock()
    session.commit = AsyncMock()
    ctx = AsyncMock()
    ctx.__aenter__ = AsyncMock(return_value=session)
    ctx.__aexit__ = AsyncMock(return_value=False)
    return MagicMock(return_value=ctx)


def _broker(pool: list[Token]) -> MagicMock:
    """Mock broker that records the token list acquire() is handed and picks index 0."""
    broker = MagicMock()
    broker.read_pool = AsyncMock(return_value=pool)

    async def _acquire(tokens: list[Token], rotation_key: str) -> SelectedCredential:
        broker.acquired_tokens = tokens
        picked = tokens[0]
        return SelectedCredential(
            credential_id=credential_id(picked.provider, picked.value),
            index=0,
            token=picked,
        )

    broker.acquire = AsyncMock(side_effect=_acquire)
    return broker


class TestAcquireAndInjectEligibility:
    """The eligible-token filter must isolate each run to its own provider."""

    async def _run(
        self, model: str, provider: str, pool: list[Token]
    ) -> tuple[MagicMock, MagicMock]:
        """Drive acquire_and_inject with a mocked broker; return (broker, sandbox)."""
        broker = _broker(pool)
        sandbox = MagicMock()
        sandbox.env = MagicMock(set=AsyncMock())
        with (
            patch("lifecycle.credentials.get_session_factory", return_value=_session_factory()),
            patch("lifecycle.credentials.CredentialBroker", return_value=broker),
            patch("lifecycle.credentials.db.update_run_status", new=AsyncMock()),
        ):
            await acquire_and_inject(sandbox, _RUN_ID, model, provider)
        return broker, sandbox

    @pytest.mark.asyncio
    async def test_gpt_run_only_sees_openrouter_tokens(self) -> None:
        """A GPT run hands the broker only OpenRouter tokens and injects the gateway env."""
        broker, sandbox = await self._run(SUPPORTED_GPT_SOL, PROVIDER_OPENROUTER, _MIXED_POOL)

        assert [t.provider for t in broker.acquired_tokens] == [PROVIDER_OPENROUTER]
        env = sandbox.env.set.await_args[0][0]
        # Never the native Claude var — that would be a leaked Anthropic credential.
        assert ENV_CLAUDE_OAUTH_TOKEN not in env
        assert env[ENV_ANTHROPIC_BASE_URL] == "https://openrouter.ai/api"
        assert env[ENV_ANTHROPIC_AUTH_TOKEN] == "sk-or-v1-bbb"

    @pytest.mark.asyncio
    async def test_claude_run_only_sees_anthropic_tokens(self) -> None:
        """A Claude run hands the broker only Anthropic tokens and injects the OAuth env."""
        broker, sandbox = await self._run(SUPPORTED_OPUS, PROVIDER_ANTHROPIC, _MIXED_POOL)

        assert [t.provider for t in broker.acquired_tokens] == [
            PROVIDER_ANTHROPIC,
            PROVIDER_ANTHROPIC,
        ]
        env = sandbox.env.set.await_args[0][0]
        assert env == {ENV_CLAUDE_OAUTH_TOKEN: "sk-ant-aaa"}
        # A GPT gateway var leaking into a Claude run would misroute it.
        assert ENV_ANTHROPIC_BASE_URL not in env

    @pytest.mark.asyncio
    async def test_no_eligible_tokens_fails_loud(self) -> None:
        """A GPT run against an all-Anthropic pool raises rather than borrowing a Claude token."""
        anthropic_only = [t for t in _MIXED_POOL if t.provider == PROVIDER_ANTHROPIC]
        broker = _broker(anthropic_only)
        sandbox = MagicMock()
        sandbox.env = MagicMock(set=AsyncMock())
        with (
            patch("lifecycle.credentials.get_session_factory", return_value=_session_factory()),
            patch("lifecycle.credentials.CredentialBroker", return_value=broker),
            patch("lifecycle.credentials.db.update_run_status", new=AsyncMock()),
            pytest.raises(RuntimeError, match=PROVIDER_OPENROUTER),
        ):
            await acquire_and_inject(sandbox, _RUN_ID, SUPPORTED_GPT_SOL, PROVIDER_OPENROUTER)

        broker.acquire.assert_not_awaited()
        sandbox.env.set.assert_not_awaited()
