"""Routing tests for the Kimi family (Kimi K3 via OpenRouter).

Mirrors the GLM self-pairing contract: Kimi K3 is a flagship with no
distinct workhorse, so both tiers resolve to K3 itself and it has no
rate-limit fallback. See docs/providers.md.
"""

from common.constants import (
    ENV_ANTHROPIC_DEFAULT_OPUS_MODEL,
    ENV_ANTHROPIC_DEFAULT_SONNET_MODEL,
    PROVIDER_OPENROUTER,
    SUPPORTED_GPT_SOL,
    SUPPORTED_KIMI,
    TIER_OPUS,
    api_model_for,
    fallback_model_for,
    family_for_model,
    openrouter_model_env,
    providers_for_model,
    tier_for_model,
    workhorse_for_model,
)


class TestKimiSelfPairing:
    """Kimi K3 has no separate workhorse, so it pairs with itself."""

    def test_kimi_is_openrouter_opus(self) -> None:
        assert PROVIDER_OPENROUTER in providers_for_model(SUPPORTED_KIMI)
        assert tier_for_model(SUPPORTED_KIMI) == TIER_OPUS

    def test_kimi_workhorse_is_itself(self) -> None:
        assert workhorse_for_model(SUPPORTED_KIMI) == SUPPORTED_KIMI

    def test_kimi_env_routes_both_tiers_to_kimi(self) -> None:
        """Both SDK tiers resolve to Kimi's slug — never a foreign workhorse."""
        env = openrouter_model_env(SUPPORTED_KIMI)
        kimi_slug = api_model_for(SUPPORTED_KIMI, PROVIDER_OPENROUTER)
        assert env[ENV_ANTHROPIC_DEFAULT_OPUS_MODEL] == kimi_slug
        assert env[ENV_ANTHROPIC_DEFAULT_SONNET_MODEL] == kimi_slug

    def test_kimi_has_no_fallback(self) -> None:
        """A self-pairing flagship has no distinct rate-limit fallback."""
        assert fallback_model_for(SUPPORTED_KIMI) is None

    def test_kimi_family_is_distinct(self) -> None:
        assert family_for_model(SUPPORTED_KIMI) != family_for_model(SUPPORTED_GPT_SOL)
