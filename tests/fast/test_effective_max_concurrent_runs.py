"""Tests for effective_max_concurrent_runs — dashboard setting with config fallback."""

from __future__ import annotations

from unittest.mock import AsyncMock, patch

import pytest

from utils import db


class TestEffectiveMaxConcurrentRuns:
    """The dashboard setting must win; unset falls back to config.yml."""

    @pytest.mark.asyncio
    async def test_uses_setting_when_set(self) -> None:
        with patch("utils.db.get_setting_value", new=AsyncMock(return_value="12")):
            assert await db.effective_max_concurrent_runs() == 12

    @pytest.mark.asyncio
    async def test_falls_back_to_config_when_unset(self) -> None:
        with (
            patch("utils.db.get_setting_value", new=AsyncMock(return_value=None)),
            patch("utils.db.max_concurrent_runs", return_value=7),
        ):
            assert await db.effective_max_concurrent_runs() == 7

    @pytest.mark.asyncio
    async def test_non_integer_setting_raises(self) -> None:
        """A corrupt DB value must fail loudly, not silently fall back."""
        with patch("utils.db.get_setting_value", new=AsyncMock(return_value="lots")):
            with pytest.raises(ValueError):
                await db.effective_max_concurrent_runs()
