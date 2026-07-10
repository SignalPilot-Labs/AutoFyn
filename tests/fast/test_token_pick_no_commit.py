"""Regression test for _pick_next_claude_token committing the session internally.

Bug: _pick_next_claude_token called await s.commit() before returning.
This committed the transaction before read_credentials had finished reading
env_vars and host_mounts. If those later reads raised an error, the index
advance was already durably committed, causing token skew on retries.

Fix: Remove s.commit() from _pick_next_claude_token; add it in read_credentials
after the token is picked and only when a token was actually returned. Token
selection now runs through the broker's acquire, which advances the cursor
internally, so the observable contract is: correct token picked, no commit.
"""

from __future__ import annotations

from datetime import datetime, timezone
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from backend.utils import _pick_next_claude_token
from common.broker import Lease, WaitDirective


class TestTokenPickNoCommit:
    """_pick_next_claude_token must NOT commit the session internally."""

    @pytest.mark.asyncio
    async def test_commit_not_called_on_pick(self) -> None:
        """_pick_next_claude_token must not call s.commit()."""
        tokens = ["sk-ant-tokenA", "sk-ant-tokenB"]
        s = MagicMock()
        s.commit = AsyncMock()
        lease = Lease(credential_id="anthropic:aaa", index=0)

        with (
            patch("backend.utils.read_token_pool", new=AsyncMock(return_value=tokens)),
            patch("backend.utils.credential_id", new=MagicMock(side_effect=lambda p, m: m)),
            patch("backend.utils.acquire", new=AsyncMock(return_value=lease)),
        ):
            result = await _pick_next_claude_token(s)

        assert result == "sk-ant-tokenA"
        s.commit.assert_not_called()

    @pytest.mark.asyncio
    async def test_returns_token_at_lease_index(self) -> None:
        """The picked token is tokens[lease.index] from the broker's Lease."""
        tokens = ["sk-ant-tokenA", "sk-ant-tokenB", "sk-ant-tokenC"]
        s = MagicMock()
        s.commit = AsyncMock()
        lease = Lease(credential_id="anthropic:bbb", index=1)

        with (
            patch("backend.utils.read_token_pool", new=AsyncMock(return_value=tokens)),
            patch("backend.utils.credential_id", new=MagicMock(side_effect=lambda p, m: m)),
            patch("backend.utils.acquire", new=AsyncMock(return_value=lease)),
        ):
            result = await _pick_next_claude_token(s)

        assert result == "sk-ant-tokenB"
        s.commit.assert_not_called()

    @pytest.mark.asyncio
    async def test_empty_pool_returns_none_without_commit(self) -> None:
        """With an empty token pool, returns None and does not commit."""
        s = MagicMock()
        s.commit = AsyncMock()

        with patch("backend.utils.read_token_pool", new=AsyncMock(return_value=[])):
            result = await _pick_next_claude_token(s)

        assert result is None
        s.commit.assert_not_called()

    @pytest.mark.asyncio
    async def test_wait_directive_returns_none_without_commit(self) -> None:
        """When the broker returns a WaitDirective (all cooling down), returns None."""
        tokens = ["sk-ant-tokenA", "sk-ant-tokenB"]
        s = MagicMock()
        s.commit = AsyncMock()
        directive = WaitDirective(
            wait_until=datetime.now(timezone.utc), reason="all credentials rate-limited"
        )

        with (
            patch("backend.utils.read_token_pool", new=AsyncMock(return_value=tokens)),
            patch("backend.utils.credential_id", new=MagicMock(side_effect=lambda p, m: m)),
            patch("backend.utils.acquire", new=AsyncMock(return_value=directive)),
        ):
            result = await _pick_next_claude_token(s)

        assert result is None
        s.commit.assert_not_called()
