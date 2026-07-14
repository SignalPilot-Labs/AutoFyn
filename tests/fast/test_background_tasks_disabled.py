"""Regression test: the CLI must not be able to background subagents.

AgentDefinition.background=False does not stop it — the CLI backgrounds by
default regardless, producing runs with N subagent_start and zero
subagent_complete. The CLI gates the Agent and Bash schemas on
CLAUDE_CODE_DISABLE_BACKGROUND_TASKS: when set, run_in_background is omitted
from both schemas, so backgrounding stops being representable at all.

Passing it via ClaudeAgentOptions.env is what makes the ban real; the env
field defaulting to None is exactly how backgrounding reached production.
"""

from __future__ import annotations

from constants import (
    CLI_DISABLE_BACKGROUND_TASKS_ENV_VAR,
    CLI_DISABLE_BACKGROUND_TASKS_VALUE,
    SESSION_ENV,
)
from sdk.session import Session

_OPTS = {
    "run_id": "test-run",
    "model": "claude-fable-5",
    "effort": "high",
    "system_prompt": "sys",
    "disallowed_tools": [],
    "cwd": "/home/agentuser/repo",
    "add_dirs": [],
    "setting_sources": [],
    "max_budget_usd": 10,
    "github_repo": "owner/repo",
    "branch_name": "test-branch",
    "initial_prompt": "go",
}


class TestBackgroundTasksDisabled:
    """Every session must start with backgrounding disabled at the CLI."""

    def test_session_env_disables_background_tasks(self) -> None:
        """The constant must carry the var the CLI actually gates on."""
        assert SESSION_ENV[CLI_DISABLE_BACKGROUND_TASKS_ENV_VAR] == (
            CLI_DISABLE_BACKGROUND_TASKS_VALUE
        )

    def test_env_var_name_matches_the_cli_contract(self) -> None:
        """The CLI reads this exact name; a typo silently re-enables backgrounding."""
        assert CLI_DISABLE_BACKGROUND_TASKS_ENV_VAR == (
            "CLAUDE_CODE_DISABLE_BACKGROUND_TASKS"
        )

    def test_session_passes_the_env_to_the_sdk(self) -> None:
        """The env must reach ClaudeAgentOptions — unset is the bug."""
        options = Session("test-session", dict(_OPTS))._build_options()

        assert options.env is not None
        assert options.env[CLI_DISABLE_BACKGROUND_TASKS_ENV_VAR] == (
            CLI_DISABLE_BACKGROUND_TASKS_VALUE
        )
