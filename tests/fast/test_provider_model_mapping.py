"""Totality + shape tests for the provider/model domain in common.constants.

Guards the invariant that every model AutoFyn accepts maps to a valid provider,
tier, and gateway slug — so no model can be added without wiring its routing.
See docs/providers.md.
"""

import pytest

from common.constants import (
    PROVIDER_OPENROUTER,
    SUPPORTED_GPT_SOL,
    SUPPORTED_GPT_TERRA,
    SUPPORTED_OPUS,
    SUPPORTED_SONNET,
    TIER_OPUS,
    TIER_SONNET,
    VALID_PROVIDERS,
    VALID_MODELS,
    api_model_for,
    fallback_model_for,
    openrouter_model_env,
    provider_for_model,
    tier_for_model,
    tier_model_for,
    ENV_ANTHROPIC_DEFAULT_OPUS_MODEL,
    ENV_ANTHROPIC_DEFAULT_SONNET_MODEL,
)


class TestProviderModelMapping:
    """provider_for_model / tier_for_model / api_model_for are total over VALID_MODELS."""

    def test_every_model_has_a_valid_provider(self) -> None:
        for model in VALID_MODELS:
            assert provider_for_model(model) in VALID_PROVIDERS

    def test_every_model_has_a_tier(self) -> None:
        for model in VALID_MODELS:
            assert tier_for_model(model) in {TIER_OPUS, TIER_SONNET, "legacy"}

    def test_every_model_has_an_api_slug(self) -> None:
        for model in VALID_MODELS:
            assert api_model_for(model)  # non-empty

    def test_every_model_has_a_fallback_entry(self) -> None:
        """fallback_model_for must not raise for any accepted model."""
        for model in VALID_MODELS:
            fallback_model_for(model)  # raises if missing

    def test_provider_for_unknown_model_raises(self) -> None:
        with pytest.raises(ValueError):
            provider_for_model("not-a-real-model")

    def test_tier_for_unknown_model_raises(self) -> None:
        with pytest.raises(ValueError):
            tier_for_model("not-a-real-model")

    def test_api_model_for_unknown_raises(self) -> None:
        with pytest.raises(ValueError):
            api_model_for("not-a-real-model")


class TestGptFamilyRouting:
    """GPT-5.6 Sol/Terra map into the OpenRouter family roles."""

    def test_sol_is_openrouter_opus(self) -> None:
        assert provider_for_model(SUPPORTED_GPT_SOL) == PROVIDER_OPENROUTER
        assert tier_for_model(SUPPORTED_GPT_SOL) == TIER_OPUS

    def test_terra_is_openrouter_sonnet(self) -> None:
        assert provider_for_model(SUPPORTED_GPT_TERRA) == PROVIDER_OPENROUTER
        assert tier_for_model(SUPPORTED_GPT_TERRA) == TIER_SONNET

    def test_openrouter_tier_models(self) -> None:
        assert tier_model_for(PROVIDER_OPENROUTER, TIER_OPUS) == SUPPORTED_GPT_SOL
        assert tier_model_for(PROVIDER_OPENROUTER, TIER_SONNET) == SUPPORTED_GPT_TERRA

    def test_openrouter_env_routes_both_tiers_to_slugs(self) -> None:
        """Sol run routes SDK opus tier to Sol's slug, sonnet tier to Terra's."""
        env = openrouter_model_env(SUPPORTED_GPT_SOL)
        assert env[ENV_ANTHROPIC_DEFAULT_OPUS_MODEL] == api_model_for(SUPPORTED_GPT_SOL)
        assert env[ENV_ANTHROPIC_DEFAULT_SONNET_MODEL] == api_model_for(SUPPORTED_GPT_TERRA)

    def test_openrouter_env_rejects_anthropic_model(self) -> None:
        with pytest.raises(ValueError):
            openrouter_model_env(SUPPORTED_OPUS)


class TestAnthropicFamilyRouting:
    """Native Claude models stay on Anthropic; slugs equal ids."""

    def test_claude_models_are_anthropic(self) -> None:
        for model in (SUPPORTED_OPUS, SUPPORTED_SONNET):
            assert provider_for_model(model) == "anthropic"
            assert api_model_for(model) == model
