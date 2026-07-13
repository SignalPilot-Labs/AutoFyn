"""Tests for _resolve_subagent_model — dynamic subagent model selection.

Pins the contract (tiers are roles, bound within the run's provider family):
- User picks opus → opus-tier gets user model, sonnet-tier gets family workhorse
- User picks sonnet → ALL tiers get user model (cost-conscious)
- User picks legacy opus → opus-tier gets legacy, sonnet-tier gets Claude Sonnet
- OpenRouter (GPT-5.6): Sol run → opus-tier Sol, sonnet-tier Terra; Terra run →
  all tiers Terra. No Claude id ever leaks into a GPT run.
"""

from common.constants import (
    LEGACY_OPUS,
    SUPPORTED_GPT_SOL,
    SUPPORTED_GPT_TERRA,
    SUPPORTED_OPUS,
    SUPPORTED_SONNET,
    TIER_OPUS,
    TIER_SONNET,
)
from prompts.subagent import _resolve_subagent_model


class TestResolveSubagentModel:
    """_resolve_subagent_model maps tier + user selection to concrete model."""

    # ── User picks supported opus (Anthropic) ──

    def test_opus_run_opus_tier_gets_user_model(self) -> None:
        assert _resolve_subagent_model(TIER_OPUS, SUPPORTED_OPUS) == SUPPORTED_OPUS

    def test_opus_run_sonnet_tier_gets_default_sonnet(self) -> None:
        assert _resolve_subagent_model(TIER_SONNET, SUPPORTED_OPUS) == SUPPORTED_SONNET

    # ── User picks sonnet (cost-conscious) ──

    def test_sonnet_run_opus_tier_becomes_sonnet(self) -> None:
        assert _resolve_subagent_model(TIER_OPUS, SUPPORTED_SONNET) == SUPPORTED_SONNET

    def test_sonnet_run_sonnet_tier_stays_sonnet(self) -> None:
        assert _resolve_subagent_model(TIER_SONNET, SUPPORTED_SONNET) == SUPPORTED_SONNET

    # ── User picks legacy opus ──

    def test_legacy_run_opus_tier_gets_legacy(self) -> None:
        assert _resolve_subagent_model(TIER_OPUS, LEGACY_OPUS) == LEGACY_OPUS

    def test_legacy_run_sonnet_tier_gets_default_sonnet(self) -> None:
        assert _resolve_subagent_model(TIER_SONNET, LEGACY_OPUS) == SUPPORTED_SONNET

    # ── User picks GPT-5.6 Sol (OpenRouter flagship, opus role) ──

    def test_sol_run_opus_tier_gets_sol(self) -> None:
        assert _resolve_subagent_model(TIER_OPUS, SUPPORTED_GPT_SOL) == SUPPORTED_GPT_SOL

    def test_sol_run_sonnet_tier_gets_terra(self) -> None:
        assert _resolve_subagent_model(TIER_SONNET, SUPPORTED_GPT_SOL) == SUPPORTED_GPT_TERRA

    # ── User picks GPT-5.6 Terra (OpenRouter workhorse, sonnet role) ──

    def test_terra_run_opus_tier_becomes_terra(self) -> None:
        assert _resolve_subagent_model(TIER_OPUS, SUPPORTED_GPT_TERRA) == SUPPORTED_GPT_TERRA

    def test_terra_run_sonnet_tier_stays_terra(self) -> None:
        assert _resolve_subagent_model(TIER_SONNET, SUPPORTED_GPT_TERRA) == SUPPORTED_GPT_TERRA
