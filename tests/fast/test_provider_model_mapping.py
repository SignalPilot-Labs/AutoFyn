"""Totality + shape tests for the provider/model domain in common.constants.

Guards the invariant that every model AutoFyn accepts maps to a valid provider
set, tier, and gateway slug — so no model can be added without wiring its
routing. See docs/providers.md.
"""

import pytest

from common.constants import (
    MODEL_PROVIDER_SLUGS,
    PROVIDER_ANTHROPIC,
    PROVIDER_OPENROUTER,
    SUPPORTED_MODELS,
    SUPPORTED_DEEPSEEK_FLASH,
    SUPPORTED_DEEPSEEK_PRO,
    SUPPORTED_GLM,
    SUPPORTED_GPT_SOL,
    SUPPORTED_GPT_TERRA,
    SUPPORTED_OPUS,
    SUPPORTED_SONNET,
    TIER_LEGACY,
    TIER_OPUS,
    TIER_SONNET,
    VALID_PROVIDERS,
    VALID_MODELS,
    api_model_for,
    fallback_model_for,
    family_for_model,
    openrouter_model_env,
    providers_for_model,
    tier_for_model,
    workhorse_for_model,
    ENV_ANTHROPIC_DEFAULT_OPUS_MODEL,
    ENV_ANTHROPIC_DEFAULT_SONNET_MODEL,
)


class TestProviderModelMapping:
    """providers_for_model / tier_for_model / api_model_for are total over VALID_MODELS."""

    def test_every_model_has_at_least_one_valid_provider(self) -> None:
        for model in VALID_MODELS:
            providers = providers_for_model(model)
            assert providers  # non-empty
            for provider in providers:
                assert provider in VALID_PROVIDERS

    def test_every_model_has_a_tier(self) -> None:
        for model in VALID_MODELS:
            assert tier_for_model(model) in {TIER_OPUS, TIER_SONNET, TIER_LEGACY}

    def test_every_model_provider_pair_has_an_api_slug(self) -> None:
        for model, slugs in MODEL_PROVIDER_SLUGS.items():
            for provider in slugs:
                assert api_model_for(model, provider)  # non-empty

    def test_every_model_has_a_fallback_entry(self) -> None:
        """fallback_model_for must not raise for any accepted model."""
        for model in VALID_MODELS:
            fallback_model_for(model)  # raises if missing

    def test_providers_for_unknown_model_raises(self) -> None:
        with pytest.raises(ValueError):
            providers_for_model("not-a-real-model")

    def test_tier_for_unknown_model_raises(self) -> None:
        with pytest.raises(ValueError):
            tier_for_model("not-a-real-model")

    def test_api_model_for_unknown_raises(self) -> None:
        with pytest.raises(ValueError):
            api_model_for("not-a-real-model", PROVIDER_ANTHROPIC)

    def test_api_model_for_unserving_provider_raises(self) -> None:
        """A provider that does not serve the model fails loudly."""
        with pytest.raises(ValueError):
            api_model_for(SUPPORTED_OPUS, PROVIDER_OPENROUTER)


class TestGptFamilyRouting:
    """GPT-5.6 Sol/Terra are the OpenRouter GPT family, paired within family."""

    def test_sol_is_openrouter_opus(self) -> None:
        assert PROVIDER_OPENROUTER in providers_for_model(SUPPORTED_GPT_SOL)
        assert tier_for_model(SUPPORTED_GPT_SOL) == TIER_OPUS

    def test_terra_is_openrouter_sonnet(self) -> None:
        assert PROVIDER_OPENROUTER in providers_for_model(SUPPORTED_GPT_TERRA)
        assert tier_for_model(SUPPORTED_GPT_TERRA) == TIER_SONNET

    def test_sol_workhorse_is_terra(self) -> None:
        assert workhorse_for_model(SUPPORTED_GPT_SOL) == SUPPORTED_GPT_TERRA

    def test_openrouter_env_routes_both_tiers_to_slugs(self) -> None:
        """Sol run routes SDK opus tier to Sol's slug, sonnet tier to Terra's."""
        env = openrouter_model_env(SUPPORTED_GPT_SOL)
        assert env[ENV_ANTHROPIC_DEFAULT_OPUS_MODEL] == api_model_for(
            SUPPORTED_GPT_SOL, PROVIDER_OPENROUTER
        )
        assert env[ENV_ANTHROPIC_DEFAULT_SONNET_MODEL] == api_model_for(
            SUPPORTED_GPT_TERRA, PROVIDER_OPENROUTER
        )

    def test_openrouter_env_rejects_anthropic_model(self) -> None:
        with pytest.raises(ValueError):
            openrouter_model_env(SUPPORTED_OPUS)


class TestDeepSeekFamilyRouting:
    """DeepSeek V4 Pro/Flash form a two-tier family, paired within family."""

    def test_pro_is_openrouter_opus(self) -> None:
        assert PROVIDER_OPENROUTER in providers_for_model(SUPPORTED_DEEPSEEK_PRO)
        assert tier_for_model(SUPPORTED_DEEPSEEK_PRO) == TIER_OPUS

    def test_flash_is_openrouter_sonnet(self) -> None:
        assert PROVIDER_OPENROUTER in providers_for_model(SUPPORTED_DEEPSEEK_FLASH)
        assert tier_for_model(SUPPORTED_DEEPSEEK_FLASH) == TIER_SONNET

    def test_pro_workhorse_stays_in_family(self) -> None:
        """A DeepSeek run's workhorse is DeepSeek Flash, not a foreign family."""
        assert workhorse_for_model(SUPPORTED_DEEPSEEK_PRO) == SUPPORTED_DEEPSEEK_FLASH

    def test_env_routes_sonnet_tier_to_flash(self) -> None:
        env = openrouter_model_env(SUPPORTED_DEEPSEEK_PRO)
        assert env[ENV_ANTHROPIC_DEFAULT_SONNET_MODEL] == api_model_for(
            SUPPORTED_DEEPSEEK_FLASH, PROVIDER_OPENROUTER
        )


class TestGlmSelfPairing:
    """GLM 5.2 has no separate workhorse, so it pairs with itself."""

    def test_glm_is_openrouter_opus(self) -> None:
        assert PROVIDER_OPENROUTER in providers_for_model(SUPPORTED_GLM)
        assert tier_for_model(SUPPORTED_GLM) == TIER_OPUS

    def test_glm_workhorse_is_itself(self) -> None:
        assert workhorse_for_model(SUPPORTED_GLM) == SUPPORTED_GLM

    def test_glm_env_routes_both_tiers_to_glm(self) -> None:
        """Both SDK tiers resolve to GLM's slug — never a foreign workhorse."""
        env = openrouter_model_env(SUPPORTED_GLM)
        glm_slug = api_model_for(SUPPORTED_GLM, PROVIDER_OPENROUTER)
        assert env[ENV_ANTHROPIC_DEFAULT_OPUS_MODEL] == glm_slug
        assert env[ENV_ANTHROPIC_DEFAULT_SONNET_MODEL] == glm_slug

    def test_glm_has_no_fallback(self) -> None:
        """A self-pairing flagship has no distinct rate-limit fallback."""
        assert fallback_model_for(SUPPORTED_GLM) is None

    def test_glm_family_is_distinct(self) -> None:
        assert family_for_model(SUPPORTED_GLM) != family_for_model(SUPPORTED_GPT_SOL)


class TestAnthropicFamilyRouting:
    """Native Claude models are served by Anthropic; slugs equal ids."""

    def test_claude_models_are_anthropic(self) -> None:
        for model in (SUPPORTED_OPUS, SUPPORTED_SONNET):
            assert PROVIDER_ANTHROPIC in providers_for_model(model)
            assert api_model_for(model, PROVIDER_ANTHROPIC) == model


class TestFamilyPairingInvariants:
    """The (family, tier) pairing that drives workhorse/fallback resolution must
    be unambiguous. _FAMILY_TIER_MODEL is a dict, so a duplicate slot silently
    keeps the last row — these guards make that fail loudly instead."""

    def _families(self) -> set[str]:
        return {m["family"] for m in SUPPORTED_MODELS}

    def test_each_family_has_at_most_one_sonnet(self) -> None:
        """workhorse_for_model reads the sonnet slot; two sonnets in one family
        would make the resolved workhorse depend on list order."""
        for family in self._families():
            sonnets = [
                m["id"]
                for m in SUPPORTED_MODELS
                if m["family"] == family and m["tier"] == TIER_SONNET
            ]
            assert len(sonnets) <= 1, f"family {family!r} has multiple sonnets: {sonnets}"

    def test_each_family_has_exactly_one_flagship(self) -> None:
        """Self-pairing falls back to the family flagship (opus); more than one
        opus per family makes that fallback order-dependent. Claude is the one
        allowed multi-flagship family (Fable + Opus) and never self-pairs, since
        it has a real sonnet workhorse."""
        for family in self._families():
            opuses = [
                m["id"]
                for m in SUPPORTED_MODELS
                if m["family"] == family and m["tier"] == TIER_OPUS
            ]
            has_sonnet = any(
                m["family"] == family and m["tier"] == TIER_SONNET
                for m in SUPPORTED_MODELS
            )
            # A family may only carry multiple flagships if it never self-pairs
            # (i.e. it has a distinct sonnet workhorse to resolve to).
            assert len(opuses) == 1 or has_sonnet, (
                f"family {family!r} self-pairs but has multiple flagships: {opuses}"
            )

    def test_every_flagship_workhorse_is_deterministic(self) -> None:
        """workhorse_for_model must resolve every flagship to a real served model."""
        for m in SUPPORTED_MODELS:
            if m["tier"] != TIER_OPUS:
                continue
            workhorse = workhorse_for_model(m["id"])
            assert workhorse in {sm["id"] for sm in SUPPORTED_MODELS}
            assert family_for_model(workhorse) == m["family"]
