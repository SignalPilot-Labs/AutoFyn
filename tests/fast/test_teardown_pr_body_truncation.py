"""Regression test: the PR body must stay under GitHub's size limit.

Bug: _run_teardown inlined the entire run_state.md (which grows unbounded
across rounds) into the PR --body. On a long run the state exceeded the
kernel's 128KB per-argv limit, so `gh pr create` failed at exec time with
``[Errno 7] Argument list too long``, teardown 500'd, and no PR was created.

Fix: _fit_pr_body truncates the run-state section (keeping round summaries and
footer whole) so the assembled body stays under PR_BODY_MAX_CHARS, inserting a
visible marker where content was cut.
"""

from __future__ import annotations

from unittest.mock import AsyncMock, patch

import pytest

from lifecycle.teardown import _fit_pr_body, _run_teardown
from utils.constants import PR_BODY_MAX_CHARS, PR_BODY_TRUNCATION_MARKER
from utils.models import RoundEntry, RoundsMetadata, RunContext


def _make_run() -> RunContext:
    return RunContext(
        run_id="run-pr-truncation-test",
        agent_role="default",
        branch_name="fix/branch",
        base_branch="main",
        duration_minutes=30.0,
        github_repo="owner/repo",
    )


def _make_metadata(rounds: list[RoundEntry], pr_title: str) -> AsyncMock:
    meta = RoundsMetadata(pr_title=pr_title, rounds=rounds)
    store = AsyncMock()
    store.load = AsyncMock(return_value=meta)
    return store


class TestTeardownPRBodyTruncation:
    """PR body is bounded even when run_state.md is enormous."""

    def test_short_body_passes_through_unchanged(self) -> None:
        body = "- **Round 1:** did a thing"
        section = "\n\n<details><summary>Run State</summary>\n\nshort\n</details>"
        footer = "\n\n---\nfooter"
        result = _fit_pr_body(body, section, footer)
        assert result == body + section + footer
        assert PR_BODY_TRUNCATION_MARKER not in result

    def test_oversized_body_is_truncated_under_limit(self) -> None:
        body = "- **Round 1:** summary line"
        section = "\n\n<details>\n" + ("X" * (PR_BODY_MAX_CHARS * 2)) + "\n</details>"
        footer = "\n\n---\nfooter"
        result = _fit_pr_body(body, section, footer)
        assert len(result) <= PR_BODY_MAX_CHARS
        assert PR_BODY_TRUNCATION_MARKER in result

    def test_round_summaries_and_footer_survive_truncation(self) -> None:
        body = "- **Round 1:** keep-me-summary"
        section = "\n\n<details>\n" + ("X" * (PR_BODY_MAX_CHARS * 2)) + "\n</details>"
        footer = "\n\n---\n**Branch:** keep-me-footer"
        result = _fit_pr_body(body, section, footer)
        assert "keep-me-summary" in result
        assert "keep-me-footer" in result

    def test_body_plus_footer_alone_over_limit_is_hard_capped(self) -> None:
        """When summaries+footer alone exceed the cap, hard-truncate to the limit.

        No room is left for the run-state section, so it (and the marker) are
        dropped entirely and the surviving body+footer is clipped to the cap.
        """
        body = "B" * PR_BODY_MAX_CHARS
        section = "\n\n<details>\nstate\n</details>"
        footer = "F" * 1000
        result = _fit_pr_body(body, section, footer)
        assert len(result) <= PR_BODY_MAX_CHARS
        assert PR_BODY_TRUNCATION_MARKER not in result
        assert "state" not in result

    def test_truncation_budget_is_char_based(self) -> None:
        """Multi-byte run-state is bounded by char count (documents the contract).

        _fit_pr_body budgets on str length (code points), not UTF-8 bytes, so a
        multi-byte body is capped at PR_BODY_MAX_CHARS chars even though its byte
        length is larger. Encoded size stays within the kernel arg limit headroom.
        """
        body = "- **Round 1:** s"
        section = "\n\n<details>\n" + ("é" * (PR_BODY_MAX_CHARS * 2)) + "\n</details>"
        footer = "\n\n---\nf"
        result = _fit_pr_body(body, section, footer)
        assert len(result) <= PR_BODY_MAX_CHARS
        assert PR_BODY_TRUNCATION_MARKER in result

    @pytest.mark.asyncio
    async def test_teardown_passes_bounded_description(self) -> None:
        run = _make_run()
        sandbox = AsyncMock()
        sandbox.file_system.read = AsyncMock(return_value="Y" * (PR_BODY_MAX_CHARS * 3))
        sandbox.repo.teardown = AsyncMock(return_value=AsyncMock(
            auto_committed=False, commits_ahead=1, pushed=True,
            push_error=None, pr_url="https://github.com/o/r/pull/1",
            pr_error=None, diff_stats=[],
        ))
        metadata = _make_metadata(
            [RoundEntry(n=1, summary="did work", ended_at="2025-01-01T00:00:00Z")],
            pr_title="Big run",
        )

        with patch("lifecycle.teardown.log_audit", new_callable=AsyncMock):
            await _run_teardown(sandbox=sandbox, run=run, metadata_store=metadata)

        pr_description: str = sandbox.repo.teardown.call_args.kwargs["pr_description"]
        assert len(pr_description) <= PR_BODY_MAX_CHARS
        assert PR_BODY_TRUNCATION_MARKER in pr_description
