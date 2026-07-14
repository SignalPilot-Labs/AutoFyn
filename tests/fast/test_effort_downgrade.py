"""Tests that session options carry the effort they are handed.

The max->high downgrade used to live inside _build_base_session_options, which
meant the session downgraded but the audit and the runs row recorded the raw
request. resolve_effort now owns the downgrade and bootstrap_run applies it once
before anything consumes it — see test_run_effort_recorded.py for that logic.

What matters here is the other half of that split: these options must pass the
resolved value through untouched, since a second downgrade would be a no-op that
hides which layer is responsible.
"""

from common.constants import LEGACY_OPUS, PROVIDER_ANTHROPIC, SUPPORTED_OPUS, SUPPORTED_SONNET
from db.constants import EFFORT_HIGH, EFFORT_LOW, EFFORT_MAX
from lifecycle.bootstrap import _build_base_session_options
from utils.models import RunContext


class TestEffortPassedThrough:
    """Session options must not re-resolve the effort they are given."""

    def _make_run(self) -> RunContext:
        return RunContext(
            run_id="test-run",
            agent_role="worker",
            branch_name="test-branch",
            base_branch="main",
            duration_minutes=0,
            github_repo="owner/repo",
        )

    def _options_for(self, model: str, effort: str) -> dict:
        return _build_base_session_options(
            run=self._make_run(),
            model=model,
            provider=PROVIDER_ANTHROPIC,
            fallback_model=SUPPORTED_SONNET,
            max_budget_usd=0,
            effort=effort,
            run_start_time=0.0,
            mcp_servers=None,
        )

    def test_max_survives_on_supporting_model(self) -> None:
        """A flagship's resolved max reaches the session as max."""
        assert self._options_for(SUPPORTED_OPUS, EFFORT_MAX)["effort"] == EFFORT_MAX

    def test_resolved_high_is_not_re_resolved(self) -> None:
        """A downgraded effort arrives already resolved and passes through."""
        assert self._options_for(LEGACY_OPUS, EFFORT_HIGH)["effort"] == EFFORT_HIGH

    def test_low_effort_unchanged(self) -> None:
        """Efforts the downgrade never touches reach the session verbatim."""
        for model in (SUPPORTED_OPUS, SUPPORTED_SONNET, LEGACY_OPUS):
            assert self._options_for(model, EFFORT_LOW)["effort"] == EFFORT_LOW
