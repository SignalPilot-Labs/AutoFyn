"""Regression tests — _collect_tmp_from_sandbox includes memory files.

Before the fix, _collect_tmp_from_sandbox only collected /tmp/round-* dirs
and returned early when none existed. Memory files (run_state.md, rounds.json,
learnings) were never fetched, so clicking them in the dashboard Changes tab
returned "File not found".
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from endpoints.diff import _collect_tmp_from_sandbox


class TestCollectTmpFromSandboxRunState:
    """Memory files are included alongside round files."""

    @pytest.mark.asyncio
    async def test_includes_run_state_md_when_present(self) -> None:
        client = MagicMock()
        client.file_system.ls = AsyncMock(return_value=["round-1"])
        client.file_system.read_dir = AsyncMock(side_effect=[
            {"architect.md": "plan"},  # round-1
            {"run_state.md": "## Goal\n\nFix bugs."},  # memory dir
        ])
        entries = await _collect_tmp_from_sandbox(client)
        paths = [e[0] for e in entries]
        assert "tmp/memory/run_state.md" in paths
        state_entry = next(e for e in entries if e[0] == "tmp/memory/run_state.md")
        assert state_entry[1] == "## Goal\n\nFix bugs."

    @pytest.mark.asyncio
    async def test_run_state_appended_after_round_files(self) -> None:
        client = MagicMock()
        client.file_system.ls = AsyncMock(return_value=["round-1"])
        client.file_system.read_dir = AsyncMock(side_effect=[
            {"report.md": "hi"},  # round-1
            {"run_state.md": "state content"},  # memory dir
        ])
        entries = await _collect_tmp_from_sandbox(client)
        assert ("tmp/memory/run_state.md", "state content") in entries

    @pytest.mark.asyncio
    async def test_excludes_memory_when_empty(self) -> None:
        client = MagicMock()
        client.file_system.ls = AsyncMock(return_value=["round-1"])
        client.file_system.read_dir = AsyncMock(side_effect=[
            {"report.md": "hi"},  # round-1
            None,  # memory dir empty
        ])
        entries = await _collect_tmp_from_sandbox(client)
        paths = [e[0] for e in entries]
        assert not any("memory" in p for p in paths)

    @pytest.mark.asyncio
    async def test_includes_memory_even_with_no_round_dirs(self) -> None:
        """Memory files are fetched even when no round-N dirs exist."""
        client = MagicMock()
        client.file_system.ls = AsyncMock(return_value=["other", "cache"])
        client.file_system.read_dir = AsyncMock(
            return_value={"run_state.md": "## Goal\n\nStarting."},
        )
        entries = await _collect_tmp_from_sandbox(client)
        assert ("tmp/memory/run_state.md", "## Goal\n\nStarting.") in entries

    @pytest.mark.asyncio
    async def test_returns_empty_when_no_rounds_and_no_memory(self) -> None:
        client = MagicMock()
        client.file_system.ls = AsyncMock(return_value=[])
        client.file_system.read_dir = AsyncMock(return_value=None)
        entries = await _collect_tmp_from_sandbox(client)
        assert entries == []
