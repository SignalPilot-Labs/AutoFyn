"""Tests: load_repo_subagents rejects malformed/untrusted repo overlays.

The repo `.autofyn/subagents.json` is untrusted (the AI agent can write it),
so every entry is validated fail-fast: known type/model tier, whitelisted
tools, a repo-contained prompt_file, and no duplicate names. Each violation
must raise RuntimeError and fail the run, not be silently skipped.
"""

import json
from typing import Any
from unittest.mock import AsyncMock, MagicMock

import pytest

from utils.run_subagents import load_repo_subagents


def _entry(**overrides: Any) -> dict:
    """A valid repo entry; override one field to make it invalid."""
    base = {
        "name": "ml-trainer",
        "type": "build",
        "description": "trains models",
        "model": "sonnet",
        "tools": ["Read", "Bash"],
        "prompt_file": ".autofyn/subagents/ml-trainer.md",
        "needs_run_state": True,
    }
    base.update(overrides)
    return base


def _sandbox_with_json(entries: list[dict]) -> MagicMock:
    """Mock sandbox whose first read returns the subagents.json text."""
    sandbox = MagicMock()
    sandbox.file_system.read = AsyncMock(return_value=json.dumps(entries))
    return sandbox


class TestRepoSubagentsValidation:
    """load_repo_subagents fails fast on every untrusted-input violation."""

    @pytest.mark.asyncio
    async def test_unknown_tool_rejected(self) -> None:
        sandbox = _sandbox_with_json([_entry(tools=["Read", "Sudo"])])
        with pytest.raises(RuntimeError, match="Sudo"):
            await load_repo_subagents(sandbox)

    @pytest.mark.asyncio
    async def test_unknown_model_tier_rejected(self) -> None:
        sandbox = _sandbox_with_json([_entry(model="haiku")])
        with pytest.raises(RuntimeError, match="model tier"):
            await load_repo_subagents(sandbox)

    @pytest.mark.asyncio
    async def test_unknown_type_rejected(self) -> None:
        sandbox = _sandbox_with_json([_entry(type="deploy")])
        with pytest.raises(RuntimeError, match="unknown type"):
            await load_repo_subagents(sandbox)

    @pytest.mark.asyncio
    async def test_absolute_prompt_path_rejected(self) -> None:
        sandbox = _sandbox_with_json([_entry(prompt_file="/etc/passwd")])
        with pytest.raises(RuntimeError, match="repo-relative"):
            await load_repo_subagents(sandbox)

    @pytest.mark.asyncio
    async def test_parent_traversal_prompt_path_rejected(self) -> None:
        sandbox = _sandbox_with_json([_entry(prompt_file="../../secrets.md")])
        with pytest.raises(RuntimeError, match="within the repo"):
            await load_repo_subagents(sandbox)

    @pytest.mark.asyncio
    async def test_mid_segment_traversal_rejected(self) -> None:
        sandbox = _sandbox_with_json([_entry(prompt_file=".autofyn/../../x.md")])
        with pytest.raises(RuntimeError, match="within the repo"):
            await load_repo_subagents(sandbox)

    @pytest.mark.asyncio
    async def test_duplicate_names_rejected(self) -> None:
        sandbox = _sandbox_with_json([_entry(), _entry()])
        with pytest.raises(RuntimeError, match="Duplicate"):
            await load_repo_subagents(sandbox)
