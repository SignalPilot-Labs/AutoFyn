"""Per-provider active-marker tests for list_pool_tokens.

Rotation is per-provider: each provider's next-up token is marked "active" from
its own bookmark (claude_token_index:{provider}), independently. A mixed pool
can have one active token per provider. See docs/providers.md.
"""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from backend.utils import list_pool_tokens, remove_token_from_pool
from common.constants import (
    PROVIDER_ANTHROPIC,
    PROVIDER_OPENROUTER,
    rotation_key_for,
)
from db.constants import CLAUDE_TOKEN_INDEX_KEY
from common.models import Token


def _session_with_rotations(rotations: dict[str, str]) -> MagicMock:
    """Mock AsyncSession whose .get(key) returns a row per rotation key.

    ``rotations`` maps a per-provider rotation key to its stored string value.
    Any key not present resolves to None (provider never used).
    """
    s = MagicMock()

    async def _get(_model: object, key: str) -> MagicMock | None:
        if key in rotations:
            row = MagicMock()
            row.value = rotations[key]
            return row
        return None

    s.get = AsyncMock(side_effect=_get)
    return s


async def _run(tokens: list[Token], rotations: dict[str, str]) -> list[dict]:
    s = _session_with_rotations(rotations)
    with (
        patch("backend.utils.read_token_pool", new=AsyncMock(return_value=tokens)),
        patch("backend.utils.session") as mock_session,
    ):
        mock_session.return_value.__aenter__ = AsyncMock(return_value=s)
        mock_session.return_value.__aexit__ = AsyncMock(return_value=None)
        return await list_pool_tokens()


class TestPerProviderActiveMarker:
    """Each provider's bookmark marks its own next-up token, translated to full-pool index."""

    @pytest.mark.asyncio
    async def test_each_provider_marks_its_own_subset(self) -> None:
        """Mixed pool: anthropic and openrouter each mark one active token."""
        tokens = [
            Token(provider=PROVIDER_ANTHROPIC, value="sk-ant-A", label=None),   # pool idx 0, anthropic[0]
            Token(provider=PROVIDER_OPENROUTER, value="sk-or-B", label=None),   # pool idx 1, openrouter[0]
            Token(provider=PROVIDER_ANTHROPIC, value="sk-ant-C", label=None),   # pool idx 2, anthropic[1]
            Token(provider=PROVIDER_OPENROUTER, value="sk-or-D", label=None),   # pool idx 3, openrouter[1]
        ]
        # anthropic stored=1 -> last-picked subset idx (1-1)%2=0 -> pool idx 0
        # openrouter stored=2 -> last-picked subset idx (2-1)%2=1 -> pool idx 3
        rotations = {
            rotation_key_for(PROVIDER_ANTHROPIC, CLAUDE_TOKEN_INDEX_KEY): "1",
            rotation_key_for(PROVIDER_OPENROUTER, CLAUDE_TOKEN_INDEX_KEY): "2",
        }
        result = await _run(tokens, rotations)
        active = {t["index"] for t in result if t["active"]}
        assert active == {0, 3}

    @pytest.mark.asyncio
    async def test_unused_provider_marks_nothing(self) -> None:
        """A provider with no bookmark yet marks none of its tokens active."""
        tokens = [
            Token(provider=PROVIDER_ANTHROPIC, value="sk-ant-A", label=None),
            Token(provider=PROVIDER_OPENROUTER, value="sk-or-B", label=None),
        ]
        # only anthropic used (stored=1 -> subset idx 0 -> pool idx 0)
        rotations = {rotation_key_for(PROVIDER_ANTHROPIC, CLAUDE_TOKEN_INDEX_KEY): "1"}
        result = await _run(tokens, rotations)
        active = {t["index"] for t in result if t["active"]}
        assert active == {0}

    @pytest.mark.asyncio
    async def test_openrouter_wraps_within_its_subset(self) -> None:
        """Stored=0 wraps to the last token of that provider's subset only."""
        tokens = [
            Token(provider=PROVIDER_OPENROUTER, value="sk-or-A", label=None),  # openrouter[0], pool 0
            Token(provider=PROVIDER_OPENROUTER, value="sk-or-B", label=None),  # openrouter[1], pool 1
            Token(provider=PROVIDER_OPENROUTER, value="sk-or-C", label=None),  # openrouter[2], pool 2
        ]
        # stored=0 -> (0-1)%3 = 2 -> pool idx 2
        rotations = {rotation_key_for(PROVIDER_OPENROUTER, CLAUDE_TOKEN_INDEX_KEY): "0"}
        result = await _run(tokens, rotations)
        active = {t["index"] for t in result if t["active"]}
        assert active == {2}


class TestRemoveAdjustsOnlyRemovedProviderRotation:
    """Removing a token adjusts only that token's provider rotation bookmark."""

    @pytest.mark.asyncio
    async def test_remove_adjusts_only_removed_provider_key(self) -> None:
        """Removing an anthropic token decrements the anthropic key, not openrouter's."""
        tokens = [
            Token(provider=PROVIDER_ANTHROPIC, value="sk-ant-A", label=None),   # pool 0, anthropic[0]
            Token(provider=PROVIDER_OPENROUTER, value="sk-or-B", label=None),   # pool 1
            Token(provider=PROVIDER_ANTHROPIC, value="sk-ant-C", label=None),   # pool 2, anthropic[1]
        ]
        ant_key = rotation_key_for(PROVIDER_ANTHROPIC, CLAUDE_TOKEN_INDEX_KEY)
        # anthropic bookmark = 1 (points at anthropic subset idx 1). Removing
        # anthropic[0] (pool idx 0, subset idx 0 < 1) must decrement it to 0.
        rows = {ant_key: MagicMock(value="1")}

        upserts: list[tuple[str, str]] = []

        s = MagicMock()

        async def _get(_model: object, key: str) -> MagicMock | None:
            return rows.get(key)

        s.get = AsyncMock(side_effect=_get)
        s.delete = AsyncMock()
        s.commit = AsyncMock()

        async def _upsert(_s: object, key: str, value: str, _enc: bool) -> None:
            upserts.append((key, value))

        with (
            patch("backend.utils.read_token_pool", new=AsyncMock(return_value=tokens)),
            patch("backend.utils._write_token_pool", new=AsyncMock()),
            patch("backend.utils.upsert_setting", new=_upsert),
            patch("backend.utils.session") as mock_session,
        ):
            mock_session.return_value.__aenter__ = AsyncMock(return_value=s)
            mock_session.return_value.__aexit__ = AsyncMock(return_value=None)
            await remove_token_from_pool(0)

        # Only the anthropic rotation key was adjusted, to 0.
        assert upserts == [(ant_key, "0")]
