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
    PROVIDER_ANTHROPIC,
    PROVIDER_OPENROUTER,
    SUPPORTED_DEEPSEEK_FLASH,
    SUPPORTED_DEEPSEEK_PRO,
    SUPPORTED_FABLE,
    SUPPORTED_GLM,
    SUPPORTED_GPT_SOL,
    SUPPORTED_GPT_TERRA,
    SUPPORTED_KIMI,
    SUPPORTED_OPUS,
    SUPPORTED_SONNET,
    TIER_OPUS,
    TIER_SONNET,
    family_for_model,
)
from prompts.subagent import _resolve_subagent_model


class TestResolveSubagentModel:
    """_resolve_subagent_model maps tier + user selection to concrete model."""

    # ── User picks supported opus (Anthropic) ──

    def test_opus_run_opus_tier_gets_user_model(self) -> None:
        assert (
            _resolve_subagent_model(TIER_OPUS, SUPPORTED_OPUS, PROVIDER_ANTHROPIC)
            == SUPPORTED_OPUS
        )

    def test_opus_run_sonnet_tier_gets_default_sonnet(self) -> None:
        assert (
            _resolve_subagent_model(TIER_SONNET, SUPPORTED_OPUS, PROVIDER_ANTHROPIC)
            == SUPPORTED_SONNET
        )

    # ── User picks sonnet (cost-conscious) ──

    def test_sonnet_run_opus_tier_becomes_sonnet(self) -> None:
        assert (
            _resolve_subagent_model(TIER_OPUS, SUPPORTED_SONNET, PROVIDER_ANTHROPIC)
            == SUPPORTED_SONNET
        )

    def test_sonnet_run_sonnet_tier_stays_sonnet(self) -> None:
        assert (
            _resolve_subagent_model(TIER_SONNET, SUPPORTED_SONNET, PROVIDER_ANTHROPIC)
            == SUPPORTED_SONNET
        )

    # ── User picks legacy opus ──

    def test_legacy_run_opus_tier_gets_legacy(self) -> None:
        assert (
            _resolve_subagent_model(TIER_OPUS, LEGACY_OPUS, PROVIDER_ANTHROPIC)
            == LEGACY_OPUS
        )

    def test_legacy_run_sonnet_tier_gets_default_sonnet(self) -> None:
        assert (
            _resolve_subagent_model(TIER_SONNET, LEGACY_OPUS, PROVIDER_ANTHROPIC)
            == SUPPORTED_SONNET
        )

    # ── User picks Fable (Anthropic, opus role) ──

    def test_fable_run_opus_tier_gets_fable(self) -> None:
        assert (
            _resolve_subagent_model(TIER_OPUS, SUPPORTED_FABLE, PROVIDER_ANTHROPIC)
            == SUPPORTED_FABLE
        )

    def test_fable_run_sonnet_tier_gets_default_sonnet(self) -> None:
        assert (
            _resolve_subagent_model(TIER_SONNET, SUPPORTED_FABLE, PROVIDER_ANTHROPIC)
            == SUPPORTED_SONNET
        )

    # ── User picks GPT-5.6 Sol (OpenRouter flagship, opus role) ──

    def test_sol_run_opus_tier_gets_sol(self) -> None:
        assert (
            _resolve_subagent_model(TIER_OPUS, SUPPORTED_GPT_SOL, PROVIDER_OPENROUTER)
            == SUPPORTED_GPT_SOL
        )

    def test_sol_run_sonnet_tier_gets_terra(self) -> None:
        assert (
            _resolve_subagent_model(TIER_SONNET, SUPPORTED_GPT_SOL, PROVIDER_OPENROUTER)
            == SUPPORTED_GPT_TERRA
        )

    # ── User picks GPT-5.6 Terra (OpenRouter workhorse, sonnet role) ──

    def test_terra_run_opus_tier_becomes_terra(self) -> None:
        assert (
            _resolve_subagent_model(TIER_OPUS, SUPPORTED_GPT_TERRA, PROVIDER_OPENROUTER)
            == SUPPORTED_GPT_TERRA
        )

    def test_terra_run_sonnet_tier_stays_terra(self) -> None:
        assert (
            _resolve_subagent_model(TIER_SONNET, SUPPORTED_GPT_TERRA, PROVIDER_OPENROUTER)
            == SUPPORTED_GPT_TERRA
        )

    # ── User picks DeepSeek V4 Pro (OpenRouter flagship, opus role) ──

    def test_deepseek_pro_run_opus_tier_gets_pro(self) -> None:
        assert (
            _resolve_subagent_model(TIER_OPUS, SUPPORTED_DEEPSEEK_PRO, PROVIDER_OPENROUTER)
            == SUPPORTED_DEEPSEEK_PRO
        )

    def test_deepseek_pro_run_sonnet_tier_gets_flash(self) -> None:
        """Workhorse stays in the DeepSeek family — never GPT Terra."""
        assert (
            _resolve_subagent_model(TIER_SONNET, SUPPORTED_DEEPSEEK_PRO, PROVIDER_OPENROUTER)
            == SUPPORTED_DEEPSEEK_FLASH
        )

    def test_deepseek_flash_run_all_tiers_stay_flash(self) -> None:
        for tier in (TIER_OPUS, TIER_SONNET):
            assert (
                _resolve_subagent_model(tier, SUPPORTED_DEEPSEEK_FLASH, PROVIDER_OPENROUTER)
                == SUPPORTED_DEEPSEEK_FLASH
            )

    # ── User picks GLM 5.2 (OpenRouter flagship, self-pairing) ──

    def test_glm_run_both_tiers_get_glm(self) -> None:
        """GLM has no workhorse variant, so every tier resolves to GLM itself."""
        for tier in (TIER_OPUS, TIER_SONNET):
            assert (
                _resolve_subagent_model(tier, SUPPORTED_GLM, PROVIDER_OPENROUTER)
                == SUPPORTED_GLM
            )

    # ── User picks Kimi K3 (OpenRouter flagship, self-pairing) ──

    def test_kimi_run_both_tiers_get_kimi(self) -> None:
        """Kimi has no workhorse variant, so every tier resolves to K3 itself."""
        for tier in (TIER_OPUS, TIER_SONNET):
            assert (
                _resolve_subagent_model(tier, SUPPORTED_KIMI, PROVIDER_OPENROUTER)
                == SUPPORTED_KIMI
            )

    # ── Leak guard: an OpenRouter run resolves to NO Claude id, and stays in
    #    its own family (no cross-family borrow) at any tier ──

    def test_openrouter_run_never_resolves_to_a_claude_id(self) -> None:
        """The tier-role fix must keep every OpenRouter run out of Claude."""
        claude_ids = {SUPPORTED_OPUS, SUPPORTED_SONNET, LEGACY_OPUS, SUPPORTED_FABLE}
        openrouter_models = (
            SUPPORTED_GPT_SOL,
            SUPPORTED_GPT_TERRA,
            SUPPORTED_DEEPSEEK_PRO,
            SUPPORTED_DEEPSEEK_FLASH,
            SUPPORTED_GLM,
            SUPPORTED_KIMI,
        )
        for user_model in openrouter_models:
            for tier in (TIER_OPUS, TIER_SONNET):
                assert (
                    _resolve_subagent_model(tier, user_model, PROVIDER_OPENROUTER)
                    not in claude_ids
                )

    def test_no_openrouter_run_borrows_another_family(self) -> None:
        """No run resolves a subagent to a model outside its own family."""
        openrouter_models = (
            SUPPORTED_GPT_SOL,
            SUPPORTED_DEEPSEEK_PRO,
            SUPPORTED_GLM,
            SUPPORTED_KIMI,
        )
        for user_model in openrouter_models:
            fam = family_for_model(user_model)
            for tier in (TIER_OPUS, TIER_SONNET):
                resolved = _resolve_subagent_model(tier, user_model, PROVIDER_OPENROUTER)
                assert family_for_model(resolved) == fam
