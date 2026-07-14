"""Regression test: an unknown cost must stay unknown across a resume.

The nullable-cost fix was defeated one file over: _build_run_context seeded
RunContext with `float(prior["total_cost_usd"] or 0)`, so a resumed run whose
cost was NULL came back as a confident 0.0, and teardown then wrote that over
the NULL. The dispatcher-level test passed throughout — it never ran bootstrap.

Fresh runs had the same problem via the `else 0.0` branch: RunContext.total_cost
defaulted to None, but this path never let that default apply.
"""

from __future__ import annotations

from unittest.mock import AsyncMock, patch

import pytest

from lifecycle.bootstrap import _build_run_context

_RESUME_ARGS = {
    "branch_name": "fix/test",
    "base_branch": "main",
    "duration_minutes": 60.0,
    "github_repo": "org/repo",
}

_PRIOR_TOKENS = {
    "total_input_tokens": 100,
    "total_output_tokens": 50,
    "cache_creation_input_tokens": 10,
    "cache_read_input_tokens": 5,
}


class TestUnknownCostSurvivesResume:
    """RunContext must distinguish "no usage reported" from a real $0.00."""

    @pytest.mark.asyncio
    async def test_resumed_null_cost_stays_none(self) -> None:
        """A prior run that never reported usage must not resume at 0.0."""
        prior = {"total_cost_usd": None, **_PRIOR_TOKENS}
        with patch(
            "lifecycle.bootstrap.db.get_run_for_resume", new=AsyncMock(return_value=prior)
        ):
            run = await _build_run_context(run_id="r1", is_resume=True, **_RESUME_ARGS)

        assert run.total_cost is None
        assert run.total_input_tokens == 100

    @pytest.mark.asyncio
    async def test_resumed_real_cost_is_preserved(self) -> None:
        """A prior run with a real cost resumes with that exact figure."""
        prior = {"total_cost_usd": 42.5, **_PRIOR_TOKENS}
        with patch(
            "lifecycle.bootstrap.db.get_run_for_resume", new=AsyncMock(return_value=prior)
        ):
            run = await _build_run_context(run_id="r1", is_resume=True, **_RESUME_ARGS)

        assert run.total_cost == 42.5

    @pytest.mark.asyncio
    async def test_resumed_confirmed_zero_is_preserved(self) -> None:
        """A prior run billed at exactly 0.0 is known, and stays 0.0 — not None."""
        prior = {"total_cost_usd": 0.0, **_PRIOR_TOKENS}
        with patch(
            "lifecycle.bootstrap.db.get_run_for_resume", new=AsyncMock(return_value=prior)
        ):
            run = await _build_run_context(run_id="r1", is_resume=True, **_RESUME_ARGS)

        assert run.total_cost == 0.0

    @pytest.mark.asyncio
    async def test_fresh_run_starts_unknown(self) -> None:
        """A fresh run has reported no usage, so its cost is unknown, not 0.0."""
        run = await _build_run_context(run_id="r1", is_resume=False, **_RESUME_ARGS)

        assert run.total_cost is None
        assert run.total_input_tokens == 0
