"""Provider and model domain constants — the single source of truth.

These describe the credential/model domain (which providers exist, which
models are served by which provider, how a model maps to SDK env vars), not
database schema. They live in ``common`` because every layer needs them:
the broker, the agent orchestrator, the sandbox session, the dashboard API,
and the CLI-adjacent settings all import from here.

Two-provider model (see docs/providers.md):
  - anthropic  — native, first-class. Claude via CLAUDE_CODE_OAUTH_TOKEN.
  - openrouter — gateway for non-Claude families (GPT-5.6). Routed through
                 OpenRouter's Anthropic-compatible endpoint.

Model↔provider is a relation, not a fixed field: a model may be served by
several providers (MODEL_PROVIDER_SLUGS), each under its own API slug. The user
picks one provider per run, so a run is single-provider — the broker rotates
only over that provider's tokens. Tiers (opus/sonnet) are roles anchored on the
native family: opus is the flagship, sonnet the workhorse. Non-Claude families
map into those roles (Sol plays the opus role, Terra the sonnet role) so a
developer's tier intent is preserved across providers.
"""

from db.constants import EFFORT_HIGH, EFFORT_MAX

# ── Providers ──
PROVIDER_ANTHROPIC: str = "anthropic"
PROVIDER_OPENROUTER: str = "openrouter"
VALID_PROVIDERS: tuple[str, ...] = (PROVIDER_ANTHROPIC, PROVIDER_OPENROUTER)
DEFAULT_PROVIDER: str = PROVIDER_ANTHROPIC
VALID_PROVIDERS_PATTERN: str = f"^({'|'.join(VALID_PROVIDERS)})$"

# OpenRouter's Anthropic-compatible endpoint base URL.
OPENROUTER_BASE_URL: str = "https://openrouter.ai/api"

# ── SDK credential env-var names ──
# Anthropic native: the OAuth token from `claude setup-token`.
ENV_CLAUDE_OAUTH_TOKEN: str = "CLAUDE_CODE_OAUTH_TOKEN"
# OpenRouter routing: point the SDK at OpenRouter, auth with the OpenRouter
# key, and blank ANTHROPIC_API_KEY so the SDK never falls back to a native
# Anthropic key that would bypass the gateway.
ENV_ANTHROPIC_BASE_URL: str = "ANTHROPIC_BASE_URL"
ENV_ANTHROPIC_AUTH_TOKEN: str = "ANTHROPIC_AUTH_TOKEN"
ENV_ANTHROPIC_API_KEY: str = "ANTHROPIC_API_KEY"
# Model-override env vars the SDK reads to route its opus/sonnet tiers to
# concrete provider model slugs (used for OpenRouter runs).
ENV_ANTHROPIC_DEFAULT_OPUS_MODEL: str = "ANTHROPIC_DEFAULT_OPUS_MODEL"
ENV_ANTHROPIC_DEFAULT_SONNET_MODEL: str = "ANTHROPIC_DEFAULT_SONNET_MODEL"

# ── Subagent tiers (roles) ──
# Each subagent declares a tier; the resolver binds it to a concrete model in
# the run's family. opus = flagship, sonnet = workhorse.
TIER_OPUS: str = "opus"
TIER_SONNET: str = "sonnet"
TIER_LEGACY: str = "legacy"

# ── Model families ──
# Groups a flagship with its same-generation workhorse; the tier resolver pairs
# opus/sonnet within a family. A flagship with no workhorse pairs with itself.
FAMILY_CLAUDE: str = "claude"
FAMILY_GPT: str = "gpt"
FAMILY_DEEPSEEK: str = "deepseek"
FAMILY_GLM: str = "glm"

# ── Model IDs ──
# Anthropic native — exact SDK model IDs, no aliases, no translation layer.
SUPPORTED_FABLE: str = "claude-fable-5"
SUPPORTED_OPUS: str = "claude-opus-4-8"
SUPPORTED_SONNET: str = "claude-sonnet-5"
LEGACY_OPUS: str = "claude-opus-4-5"
# OpenRouter — exact OpenRouter model slugs.
SUPPORTED_GPT_SOL: str = "openai/gpt-5.6-sol"
SUPPORTED_GPT_TERRA: str = "openai/gpt-5.6-terra"
SUPPORTED_DEEPSEEK_PRO: str = "deepseek/deepseek-v4-pro"
SUPPORTED_DEEPSEEK_FLASH: str = "deepseek/deepseek-v4-flash"
SUPPORTED_GLM: str = "z-ai/glm-5.2"

VALID_MODELS: tuple[str, ...] = (
    SUPPORTED_FABLE,
    SUPPORTED_OPUS,
    SUPPORTED_SONNET,
    LEGACY_OPUS,
    SUPPORTED_GPT_SOL,
    SUPPORTED_GPT_TERRA,
    SUPPORTED_DEEPSEEK_PRO,
    SUPPORTED_DEEPSEEK_FLASH,
    SUPPORTED_GLM,
)
DEFAULT_MODEL: str = SUPPORTED_OPUS
VALID_MODELS_PATTERN: str = f"^({'|'.join(VALID_MODELS)})$"

# Model metadata for /api/models (the dashboard's source of truth; no model
# list is hardcoded in the frontend). Provider routing is not here — a model's
# providers/slugs live in MODEL_PROVIDER_SLUGS, chosen per run.
SUPPORTED_MODELS: list[dict[str, str]] = [
    {
        "id": SUPPORTED_FABLE,
        "label": "Claude Fable 5",
        "short": "Fable 5",
        "description": "Most capable, for demanding agentic work",
        "context": "1M context",
        "tier": TIER_OPUS,
        "family": FAMILY_CLAUDE,
    },
    {
        "id": SUPPORTED_OPUS,
        "label": "Claude Opus 4.8",
        "short": "Opus 4.8",
        "description": "Highly capable, strong for agents",
        "context": "1M context",
        "tier": TIER_OPUS,
        "family": FAMILY_CLAUDE,
    },
    {
        "id": SUPPORTED_SONNET,
        "label": "Claude Sonnet 5",
        "short": "Sonnet 5",
        "description": "Fast and capable",
        "context": "1M context",
        "tier": TIER_SONNET,
        "family": FAMILY_CLAUDE,
    },
    {
        "id": LEGACY_OPUS,
        "label": "Claude Opus 4.5",
        "short": "Opus 4.5",
        "description": "Legacy Opus model",
        "context": "200K context",
        "tier": TIER_LEGACY,
        "family": FAMILY_CLAUDE,
    },
    {
        "id": SUPPORTED_GPT_SOL,
        "label": "GPT-5.6 Sol",
        "short": "Sol",
        "description": "OpenAI flagship, top reasoning",
        "context": "1M context",
        "tier": TIER_OPUS,
        "family": FAMILY_GPT,
    },
    {
        "id": SUPPORTED_GPT_TERRA,
        "label": "GPT-5.6 Terra",
        "short": "Terra",
        "description": "OpenAI balanced workhorse",
        "context": "1M context",
        "tier": TIER_SONNET,
        "family": FAMILY_GPT,
    },
    {
        "id": SUPPORTED_DEEPSEEK_PRO,
        "label": "DeepSeek V4 Pro",
        "short": "V4 Pro",
        "description": "DeepSeek flagship, deep reasoning",
        "context": "1M context",
        "tier": TIER_OPUS,
        "family": FAMILY_DEEPSEEK,
    },
    {
        "id": SUPPORTED_DEEPSEEK_FLASH,
        "label": "DeepSeek V4 Flash",
        "short": "V4 Flash",
        "description": "DeepSeek efficient workhorse",
        "context": "1M context",
        "tier": TIER_SONNET,
        "family": FAMILY_DEEPSEEK,
    },
    {
        "id": SUPPORTED_GLM,
        "label": "GLM 5.2",
        "short": "GLM 5.2",
        "description": "Zhipu open-weight flagship",
        "context": "1M context",
        "tier": TIER_OPUS,
        "family": FAMILY_GLM,
    },
]

# model id -> {provider -> API slug}. A model may be served by several providers,
# each under its own slug. Adding a gateway for a model is a data-only edit.
MODEL_PROVIDER_SLUGS: dict[str, dict[str, str]] = {
    SUPPORTED_FABLE: {PROVIDER_ANTHROPIC: SUPPORTED_FABLE},
    SUPPORTED_OPUS: {PROVIDER_ANTHROPIC: SUPPORTED_OPUS},
    SUPPORTED_SONNET: {PROVIDER_ANTHROPIC: SUPPORTED_SONNET},
    LEGACY_OPUS: {PROVIDER_ANTHROPIC: LEGACY_OPUS},
    SUPPORTED_GPT_SOL: {PROVIDER_OPENROUTER: SUPPORTED_GPT_SOL},
    SUPPORTED_GPT_TERRA: {PROVIDER_OPENROUTER: SUPPORTED_GPT_TERRA},
    SUPPORTED_DEEPSEEK_PRO: {PROVIDER_OPENROUTER: SUPPORTED_DEEPSEEK_PRO},
    SUPPORTED_DEEPSEEK_FLASH: {PROVIDER_OPENROUTER: SUPPORTED_DEEPSEEK_FLASH},
    SUPPORTED_GLM: {PROVIDER_OPENROUTER: SUPPORTED_GLM},
}

# Models that support effort="max". Others get downgraded to "high".
# Per family, only the flagship unlocks max reasoning.
MODELS_SUPPORTING_MAX_EFFORT: frozenset[str] = frozenset(
    {
        SUPPORTED_FABLE,
        SUPPORTED_OPUS,
        SUPPORTED_SONNET,
        SUPPORTED_GPT_SOL,
        SUPPORTED_DEEPSEEK_PRO,
        SUPPORTED_GLM,
    }
)


def resolve_effort(model: str, effort: str) -> str:
    """Return the effort the model will actually run at, downgrading max if unsupported."""
    if effort == EFFORT_MAX and model not in MODELS_SUPPORTING_MAX_EFFORT:
        return EFFORT_HIGH
    return effort

# model id -> tier / family, derived from SUPPORTED_MODELS (single source of truth).
_MODEL_TIER: dict[str, str] = {m["id"]: m["tier"] for m in SUPPORTED_MODELS}
_MODEL_FAMILY: dict[str, str] = {m["id"]: m["family"] for m in SUPPORTED_MODELS}

# (family, tier) -> model id, derived. Pairs opus/sonnet within a family so a
# run never mixes generations. TIER_LEGACY is excluded — it is not a role.
_FAMILY_TIER_MODEL: dict[tuple[str, str], str] = {
    (m["family"], m["tier"]): m["id"]
    for m in SUPPORTED_MODELS
    if m["tier"] != TIER_LEGACY
}


def family_tier_model(family: str, tier: str) -> str:
    """Resolve a (family, tier) role to a model id, self-pairing if the family
    has no distinct workhorse. Fails loudly on an unknown family."""
    model = _FAMILY_TIER_MODEL.get((family, tier))
    if model is not None:
        return model
    flagship = _FAMILY_TIER_MODEL.get((family, TIER_OPUS))
    if flagship is None:
        raise ValueError(f"no flagship for family '{family}'")
    return flagship


# Rate-limit fallback: flagship falls back to its family workhorse; a workhorse
# (or a self-pairing flagship) has none. Derived from the family pairing.
_FALLBACK_MAP: dict[str, str | None] = {
    m["id"]: (
        family_tier_model(m["family"], TIER_SONNET)
        if m["tier"] == TIER_OPUS
        and family_tier_model(m["family"], TIER_SONNET) != m["id"]
        else None
    )
    for m in SUPPORTED_MODELS
}


def api_model_for(model: str, provider: str) -> str:
    """Return the API slug ``provider`` uses for ``model``. Fails loudly."""
    slugs = MODEL_PROVIDER_SLUGS.get(model)
    if slugs is None:
        raise ValueError(f"unknown model '{model}'")
    slug = slugs.get(provider)
    if slug is None:
        raise ValueError(f"provider '{provider}' does not serve model '{model}'")
    return slug


def providers_for_model(model: str) -> tuple[str, ...]:
    """Return every provider that can serve ``model``. Fails loudly if unknown."""
    slugs = MODEL_PROVIDER_SLUGS.get(model)
    if slugs is None:
        raise ValueError(f"unknown model '{model}'")
    return tuple(slugs)


def tier_for_model(model: str) -> str:
    """Return the tier (role) of an AutoFyn model ID. Fails loudly if unknown."""
    tier = _MODEL_TIER.get(model)
    if tier is None:
        raise ValueError(f"no tier for model '{model}' (not in SUPPORTED_MODELS)")
    return tier


def fallback_model_for(model: str) -> str | None:
    """Return the rate-limit fallback model, or None. Fails loudly if unknown."""
    if model not in _FALLBACK_MAP:
        raise ValueError(f"no fallback entry for model '{model}'")
    return _FALLBACK_MAP[model]


def family_for_model(model: str) -> str:
    """Return the family of an AutoFyn model ID. Fails loudly if unknown."""
    family = _MODEL_FAMILY.get(model)
    if family is None:
        raise ValueError(f"no family for model '{model}' (not in SUPPORTED_MODELS)")
    return family


def workhorse_for_model(model: str) -> str:
    """Resolve the sonnet-tier workhorse in ``model``'s family, self-pairing when
    the family has no distinct workhorse. Fails loudly if the model is unknown."""
    return family_tier_model(family_for_model(model), TIER_SONNET)


def rotation_key_for(provider: str, base_key: str) -> str:
    """Per-provider rotation bookmark key.

    Each provider rotates over its own token subset, so each needs its own
    bookmark — a shared index would index the wrong subset once providers mix.
    """
    if provider not in VALID_PROVIDERS:
        raise ValueError(f"unknown provider '{provider}'")
    return f"{base_key}:{provider}"


def openrouter_model_env(model: str) -> dict[str, str]:
    """Build the SDK model-override env for an OpenRouter run.

    Routes the SDK's opus tier to the run's model and its sonnet tier to the
    workhorse in the same family, both by their OpenRouter slug so subagents
    resolve through the gateway. Fails loudly if OpenRouter does not serve them.
    """
    workhorse = workhorse_for_model(model)
    return {
        ENV_ANTHROPIC_DEFAULT_OPUS_MODEL: api_model_for(model, PROVIDER_OPENROUTER),
        ENV_ANTHROPIC_DEFAULT_SONNET_MODEL: api_model_for(workhorse, PROVIDER_OPENROUTER),
    }
