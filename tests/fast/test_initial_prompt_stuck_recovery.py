"""Tests that build_initial_prompt surfaces a prior stuck-recovery to the next round.

When a subagent is force-interrupted for being stuck, the round ends and the
orchestrator never reads the injected recovery message. The next round must be
told explicitly so it adapts instead of re-dispatching the same agent blind.
"""

from prompts.orchestrator import build_initial_prompt
from utils.constants import ROUND_DIR_PREFIX, STUCK_RECOVERY_REPORT_NAME


class TestInitialPromptStuckRecovery:
    """build_initial_prompt's stuck-recovery callout."""

    def test_includes_callout_and_path_when_prior_round_was_stuck(self) -> None:
        prompt = build_initial_prompt(
            round_number=3,
            task="audit the repo",
            is_grace_round=False,
            prior_round_had_stuck_recovery=True,
        )
        assert "force-interrupted" in prompt
        assert f"{ROUND_DIR_PREFIX}2/{STUCK_RECOVERY_REPORT_NAME}" in prompt

    def test_no_callout_when_prior_round_was_clean(self) -> None:
        prompt = build_initial_prompt(
            round_number=3,
            task="audit the repo",
            is_grace_round=False,
            prior_round_had_stuck_recovery=False,
        )
        assert "force-interrupted" not in prompt
        assert STUCK_RECOVERY_REPORT_NAME not in prompt

    def test_callout_coexists_with_grace_round_notice(self) -> None:
        prompt = build_initial_prompt(
            round_number=5,
            task="audit the repo",
            is_grace_round=True,
            prior_round_had_stuck_recovery=True,
        )
        assert "force-interrupted" in prompt
        assert "final round" in prompt
