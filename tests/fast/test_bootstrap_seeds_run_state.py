"""Tests that bootstrap seeds an empty run_state.md for fresh runs.

Regression prevention: without the seed file, the orchestrator must
create run_state.md from scratch in Round 1 instead of filling a template.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from config.constants import SANDBOX_KIND_DOCKER, SandboxResources
from common.constants import PROVIDER_ANTHROPIC
from lifecycle.bootstrap import bootstrap_run
from utils.constants import MEMORY_DIR, RUN_STATE_PATH, RUN_STATE_TEMPLATE

_TEST_RESOURCES = SandboxResources(
    kind=SANDBOX_KIND_DOCKER, cpu_count=8, mem_limit_bytes=None,
)


def _mock_sandbox() -> MagicMock:
    """Build a mock SandboxClient."""
    sandbox = MagicMock()
    sandbox.repo.bootstrap = AsyncMock()
    sandbox.file_system.mkdir = AsyncMock()
    sandbox.file_system.write = AsyncMock()
    sandbox.file_system.read = AsyncMock(return_value=None)
    sandbox.resources = AsyncMock(return_value=_TEST_RESOURCES)
    return sandbox


class TestBootstrapSeedsRunState:
    """Bootstrap must write run_state.md template on fresh runs."""

    @pytest.mark.asyncio
    async def test_fresh_run_seeds_run_state(self) -> None:
        sandbox = _mock_sandbox()

        with (
            patch("lifecycle.bootstrap.db") as mock_db,
            patch("lifecycle.bootstrap.log_audit", new_callable=AsyncMock),
            patch("lifecycle.bootstrap.load_run_agent_config", new_callable=AsyncMock),
        ):
            mock_db.cache_repo_subagents = AsyncMock()
            mock_db.get_run_branch_name = AsyncMock(return_value=None)
            mock_db.update_run_branch = AsyncMock()
            mock_db.get_run_for_resume = AsyncMock(return_value=None)

            await bootstrap_run(
                sandbox=sandbox,
                run_id="run-1",
                custom_prompt="Fix auth",
                max_budget_usd=10.0,
                duration_minutes=60,
                base_branch="main",
                github_repo="owner/repo",
                model="claude-sonnet-4-6",
                provider=PROVIDER_ANTHROPIC,
                effort="high",
                mcp_servers=None,
            )

        write_calls = sandbox.file_system.write.call_args_list
        run_state_calls = [c for c in write_calls if c.args[0] == RUN_STATE_PATH]
        assert len(run_state_calls) == 1
        assert run_state_calls[0].args[1] == RUN_STATE_TEMPLATE

    @pytest.mark.asyncio
    async def test_resumed_run_does_not_seed_run_state(self) -> None:
        sandbox = _mock_sandbox()

        with (
            patch("lifecycle.bootstrap.db") as mock_db,
            patch("lifecycle.bootstrap.log_audit", new_callable=AsyncMock),
            patch("lifecycle.bootstrap.load_run_agent_config", new_callable=AsyncMock),
        ):
            mock_db.cache_repo_subagents = AsyncMock()
            mock_db.get_run_branch_name = AsyncMock(return_value="autofyn/existing")
            mock_db.update_run_status = AsyncMock()
            mock_db.get_run_for_resume = AsyncMock(return_value={
                "total_cost_usd": 0, "total_input_tokens": 0,
                "total_output_tokens": 0, "cache_creation_input_tokens": 0,
                "cache_read_input_tokens": 0,
            })

            # Simulate archiver restoring rounds (starting_round > 0)
            with patch.object(
                sandbox, "file_system", sandbox.file_system,
            ):
                from memory.archiver import RoundArchiver
                with patch.object(RoundArchiver, "restore_all", new_callable=AsyncMock, return_value=3):
                    await bootstrap_run(
                        sandbox=sandbox,
                        run_id="run-1",
                        custom_prompt="Fix auth",
                        max_budget_usd=10.0,
                        duration_minutes=60,
                        base_branch="main",
                        github_repo="owner/repo",
                        model="claude-sonnet-4-6",
                        provider=PROVIDER_ANTHROPIC,
                        effort="high",
                        mcp_servers=None,
                    )

        write_calls = sandbox.file_system.write.call_args_list
        run_state_calls = [c for c in write_calls if c.args[0] == RUN_STATE_PATH]
        assert len(run_state_calls) == 0
        # Memory dir must still be created so the first subagent's read of
        # /tmp/memory/<agent>.md doesn't hit a missing directory after a
        # resume whose prior sandbox crashed before writing any memory files.
        sandbox.file_system.mkdir.assert_awaited_once_with(MEMORY_DIR)

    @pytest.mark.asyncio
    async def test_fresh_run_creates_memory_dir(self) -> None:
        sandbox = _mock_sandbox()

        with (
            patch("lifecycle.bootstrap.db") as mock_db,
            patch("lifecycle.bootstrap.log_audit", new_callable=AsyncMock),
            patch("lifecycle.bootstrap.load_run_agent_config", new_callable=AsyncMock),
        ):
            mock_db.cache_repo_subagents = AsyncMock()
            mock_db.get_run_branch_name = AsyncMock(return_value=None)
            mock_db.update_run_branch = AsyncMock()
            mock_db.get_run_for_resume = AsyncMock(return_value=None)

            await bootstrap_run(
                sandbox=sandbox,
                run_id="run-1",
                custom_prompt="Fix auth",
                max_budget_usd=10.0,
                duration_minutes=60,
                base_branch="main",
                github_repo="owner/repo",
                model="claude-sonnet-4-6",
                provider=PROVIDER_ANTHROPIC,
                effort="high",
                mcp_servers=None,
            )

        sandbox.file_system.mkdir.assert_awaited_once_with(MEMORY_DIR)
