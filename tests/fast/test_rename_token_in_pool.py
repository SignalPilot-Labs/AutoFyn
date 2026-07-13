"""Regression tests for rename_token_in_pool.

Renaming a pool credential must change only its label — never its value or
provider — and must go through the same SELECT...FOR UPDATE lock as the other
read-modify-write pool mutators, so a concurrent add/remove/rename can't lose
the update. Out-of-range indices must raise ValueError (surfaced as 404).
"""

from __future__ import annotations

import sys
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

if "db.connection" not in sys.modules:
    sys.modules["db.connection"] = MagicMock()

from backend.utils import rename_token_in_pool
from common.models import Token
from db.constants import PROVIDER_ANTHROPIC


class TestRenameTokenInPool:
    """rename_token_in_pool changes only the label, under the pool lock."""

    @pytest.mark.asyncio
    async def test_rename_calls_read_with_for_update(self) -> None:
        """rename_token_in_pool must pass for_update=True to read_token_pool."""
        captured_kwargs: list[dict] = []

        async def fake_read_token_pool(s: MagicMock, for_update: bool = False) -> list[Token]:
            captured_kwargs.append({"for_update": for_update})
            return [Token(provider=PROVIDER_ANTHROPIC, value="token-a", label=None)]

        s = MagicMock()
        s.commit = AsyncMock()

        with (
            patch("backend.utils.read_token_pool", new=fake_read_token_pool),
            patch("backend.utils._write_token_pool", new=AsyncMock()),
            patch("backend.utils.session") as mock_session_ctx,
        ):
            mock_session_ctx.return_value.__aenter__ = AsyncMock(return_value=s)
            mock_session_ctx.return_value.__aexit__ = AsyncMock(return_value=None)
            await rename_token_in_pool(0, "prod")

        assert len(captured_kwargs) == 1
        assert captured_kwargs[0]["for_update"] is True

    @pytest.mark.asyncio
    async def test_rename_preserves_value_and_provider(self) -> None:
        """Only the label changes; value and provider are carried through untouched."""
        written: list[list[Token]] = []

        async def fake_write(s: MagicMock, tokens: list[Token]) -> None:
            written.append(tokens)

        pool = [Token(provider=PROVIDER_ANTHROPIC, value="secret-val", label="old")]
        s = MagicMock()
        s.commit = AsyncMock()

        with (
            patch("backend.utils.read_token_pool", new=AsyncMock(return_value=pool)),
            patch("backend.utils._write_token_pool", new=fake_write),
            patch("backend.utils.session") as mock_session_ctx,
        ):
            mock_session_ctx.return_value.__aenter__ = AsyncMock(return_value=s)
            mock_session_ctx.return_value.__aexit__ = AsyncMock(return_value=None)
            await rename_token_in_pool(0, "new-name")

        renamed = written[0][0]
        assert renamed.label == "new-name"
        assert renamed.value == "secret-val"
        assert renamed.provider == PROVIDER_ANTHROPIC

    @pytest.mark.asyncio
    async def test_rename_to_none_clears_label(self) -> None:
        """Passing label=None clears the name (renders as the N/A placeholder)."""
        written: list[list[Token]] = []

        async def fake_write(s: MagicMock, tokens: list[Token]) -> None:
            written.append(tokens)

        pool = [Token(provider=PROVIDER_ANTHROPIC, value="secret-val", label="old")]
        s = MagicMock()
        s.commit = AsyncMock()

        with (
            patch("backend.utils.read_token_pool", new=AsyncMock(return_value=pool)),
            patch("backend.utils._write_token_pool", new=fake_write),
            patch("backend.utils.session") as mock_session_ctx,
        ):
            mock_session_ctx.return_value.__aenter__ = AsyncMock(return_value=s)
            mock_session_ctx.return_value.__aexit__ = AsyncMock(return_value=None)
            await rename_token_in_pool(0, None)

        assert written[0][0].label is None

    @pytest.mark.asyncio
    async def test_rename_out_of_range_raises_value_error(self) -> None:
        """Renaming an out-of-range index must raise ValueError."""
        s = MagicMock()
        s.commit = AsyncMock()

        with (
            patch("backend.utils.read_token_pool", new=AsyncMock(return_value=[Token(value="only-token", label=None)])),
            patch("backend.utils.session") as mock_session_ctx,
        ):
            mock_session_ctx.return_value.__aenter__ = AsyncMock(return_value=s)
            mock_session_ctx.return_value.__aexit__ = AsyncMock(return_value=None)
            with pytest.raises(ValueError, match="out of range"):
                await rename_token_in_pool(5, "x")
