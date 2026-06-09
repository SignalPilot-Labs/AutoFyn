"""Tests: load_repo_subagents reads, merges, and prefetches repo overlays.

Covers the happy path and the two non-error edges: no repo file (shipped
subagents unchanged) and a present overlay (merged specs + prefetched bodies).
A repo entry whose prompt_file is missing fails the run.
"""

import json
from unittest.mock import AsyncMock, MagicMock

import pytest

from config.loader import load_subagents
from utils.run_subagents import load_repo_subagents

_VALID_ENTRY = {
    "name": "ml-trainer",
    "type": "build",
    "description": "trains models",
    "model": "sonnet",
    "tools": ["Read", "Bash"],
    "prompt_file": ".autofyn/subagents/ml-trainer.md",
    "needs_run_state": True,
}


class TestLoadRepoSubagents:
    """load_repo_subagents resolves the per-run subagents and repo bodies."""

    @pytest.mark.asyncio
    async def test_no_repo_file_returns_shipped(self) -> None:
        sandbox = MagicMock()
        sandbox.file_system.read = AsyncMock(return_value=None)
        config = await load_repo_subagents(sandbox)
        assert config.specs == load_subagents()
        assert config.bodies == {}

    @pytest.mark.asyncio
    async def test_overlay_merges_and_prefetches_body(self) -> None:
        sandbox = MagicMock()
        # First read: the JSON. Second read: the new agent's prompt body.
        sandbox.file_system.read = AsyncMock(
            side_effect=[json.dumps([_VALID_ENTRY]), "ML TRAINER BODY"]
        )
        config = await load_repo_subagents(sandbox)
        names = {s.name for s in config.specs}
        assert "ml-trainer" in names
        assert config.bodies == {"ml-trainer": "ML TRAINER BODY"}

    @pytest.mark.asyncio
    async def test_missing_prompt_body_raises(self) -> None:
        sandbox = MagicMock()
        # JSON present, but the body read returns None (file not in repo).
        sandbox.file_system.read = AsyncMock(
            side_effect=[json.dumps([_VALID_ENTRY]), None]
        )
        with pytest.raises(RuntimeError, match="prompt_file not found"):
            await load_repo_subagents(sandbox)

    @pytest.mark.asyncio
    async def test_needs_verification_defaults_false(self) -> None:
        sandbox = MagicMock()
        sandbox.file_system.read = AsyncMock(
            side_effect=[json.dumps([_VALID_ENTRY]), "BODY"]
        )
        config = await load_repo_subagents(sandbox)
        spec = next(s for s in config.specs if s.name == "ml-trainer")
        # _VALID_ENTRY omits needs_verification → defaults to False.
        assert spec.needs_verification is False
