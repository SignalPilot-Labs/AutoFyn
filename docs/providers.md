# Credential Providers & Model Families

How AutoFyn decides which credential and which API endpoint a run uses. One source of truth for the multi-provider design, so a second gateway for a model slots in without re-litigating any of this.

## The choices

**Anthropic — native, first-class.** Claude models run directly against the Anthropic subscription via `CLAUDE_CODE_OAUTH_TOKEN` (from `claude setup-token`). No proxy, no translation layer, exact SDK model IDs. This is the home turf; every other family is measured against it.

**OpenRouter — gateway for non-Claude families.** Models Anthropic does not serve (GPT-5.6, DeepSeek V4, GLM 5.2, Kimi K3) reach the SDK through OpenRouter's Anthropic-compatible endpoint. OpenRouter is a transport for other vendors' models — it is **never** used to reach Claude (a gateway hop for Claude is strictly worse: extra latency and margin, no upside).

## A model can be served by more than one provider

Provider is **not** a fixed property of a model. The same model may be reachable through several gateways (and a user may hold keys for several), so the model↔provider link is a **relation**, not a per-model field:

```
MODEL_PROVIDER_SLUGS: model_id -> { provider -> API slug }
```

`providers_for_model(model)` returns every provider that can serve a model; `api_model_for(model, provider)` returns that provider's slug for it. Both fail loud on unknown input.

**The user picks the provider per run.** The start modal cascades: pick a model, then pick a provider from a dropdown filtered to the providers you hold keys for (`GET /api/models` returns `providers_by_model`, computed from the token pool). One available provider → auto-selected and shown read-only; zero → a distinct "no keys for this model" state that disables start.

## A run is single-provider

Once picked, a run is pinned to one provider for its whole life. Consequences:

- The broker rotates only over that provider's tokens (`credentials.py` filters the pool by `t.provider == run.provider` before leasing) and round-robins that provider's N keys.
- Credential injection is provider-specific and needs **no cross-provider clearing** — a run never switches providers mid-flight, so there is no stale env to scrub. No cross-gateway spillover mid-run.
- A run whose provider has no tokens fails loudly (`no <provider> credentials configured`) instead of silently borrowing another provider's key.
- The run stores its provider (`Run.provider_name`) so resume re-injects the same one. Pre-migration runs (NULL) backfill it from the model — unambiguous while a model has a single provider.

Today Anthropic serves the Claude models and OpenRouter serves the GPT-5.6, DeepSeek V4, GLM 5.2, and Kimi K3 families, so every model currently has exactly one available provider. The relation is fully general regardless: adding a second gateway for a model is a data-only edit.

## Tiers are roles, not vendor labels

AutoFyn has two capability tiers, anchored on the native family:

- `opus` — the flagship, for hard reasoning and flagship subagents.
- `sonnet` — the fast, capable workhorse for the bulk of subagents.

A tier is a **role**, so another family can be mapped into it. When a developer's subagent declares `tier: opus`, it means "use the flagship of whatever family this run is on" — not literally Claude Opus.

Pairing is **within a family**, keyed on the model's `family` field (not its provider). Several families share the OpenRouter gateway, so provider alone cannot pick the workhorse — a GLM run must not borrow GPT's workhorse.

| Family   | `opus` (flagship)  | `sonnet` (workhorse) |
| -------- | ------------------ | -------------------- |
| claude   | Opus 4.8 / Fable 5 | Sonnet 5             |
| gpt      | Sol                | Terra                |
| deepseek | V4 Pro             | V4 Flash             |
| glm      | GLM 5.2            | GLM 5.2 (self-pairs) |
| kimi     | Kimi K3            | Kimi K3 (self-pairs) |

So on a DeepSeek run, an `opus`-tier subagent runs V4 Pro and a `sonnet`-tier subagent runs V4 Flash. A family with no distinct workhorse (GLM 5.2 and Kimi K3 have no Air/Flash-style variant yet) **self-pairs**: both roles resolve to the flagship. `_resolve_subagent_model` in `autofyn/prompts/subagent.py` implements this via `workhorse_for_model(model)`, which resolves the sonnet-tier model in the run model's own family.

`GPT-5.6 Luna` is intentionally omitted — it is a third (cheap) tier and AutoFyn has no role for it, so leaving it out costs nothing.

Max-effort membership (`MODELS_SUPPORTING_MAX_EFFORT`) is **per model**, not per tier: only each family's flagship unlocks it (Opus, Fable, Sonnet, Sol, V4 Pro, GLM 5.2, Kimi K3). Workhorses like Terra and V4 Flash do not, and downgrade `max` → `high`.

## Model ID vs. gateway slug

Two identifiers that must stay distinct:

- `id` — AutoFyn's stable identifier. Flows through the picker, `localStorage`, the DB (`Run.model_name`), and `VALID_MODELS`. Drives tier resolution.
- **API slug** — what a provider's API expects, injected into the SDK. Lives per (model, provider) in `MODEL_PROVIDER_SLUGS` and is read only at the SDK boundary via `api_model_for(model, provider)`.

They are separate on purpose: the **same model can have a different slug on a different gateway**. Routing always resolves the slug from (model, provider), never reuses the `id` — so a second gateway for a model is a new key in the relation with its own slug, no translation layer. The slug is never stored or threaded around as a second identity; everything upstream of the SDK boundary uses the `id`.

## Env-var contract per provider

Injected per round by `acquire_and_inject` → `_provider_env`:

| Provider   | Env vars set |
| ---------- | ------------ |
| anthropic  | `CLAUDE_CODE_OAUTH_TOKEN=<token>` |
| openrouter | `ANTHROPIC_BASE_URL=https://openrouter.ai/api`, `ANTHROPIC_AUTH_TOKEN=<key>`, `ANTHROPIC_API_KEY=""` (explicitly empty so the SDK never falls back to a native key and bypasses the gateway), `ANTHROPIC_DEFAULT_OPUS_MODEL=<run api_model>`, `ANTHROPIC_DEFAULT_SONNET_MODEL=<workhorse api_model>` |

## Where things live / adding a provider

Provider and model constants and helpers live in `common/constants.py` (the credential/model domain, shared across the agent, sandbox, dashboard, and broker). DB-row keys and cooldown timing stay in `db/constants.py`.

**Add a gateway for an existing model** (the common case) — a data-only edit: append `PROVIDER_<NAME>: "<slug>"` to that model's entry in `MODEL_PROVIDER_SLUGS`. The picker offers it automatically once the user has a key for it.

**Add a new provider:**

1. `common/constants.py` — add `PROVIDER_<NAME>`, extend `VALID_PROVIDERS`, add the gateway env-var names + base URL, and add `<provider>` keys to the relevant `MODEL_PROVIDER_SLUGS` entries and `_PROVIDER_TIER_MODELS`.
2. `_provider_env` in `autofyn/lifecycle/credentials.py` — add the injection branch for the new provider (fail loud on unknown).
3. `dashboard/frontend/lib/constants.ts` — add the provider to `CREDENTIAL_PROVIDERS` and a `TOKEN_PLACEHOLDERS` entry.

**Add a new model:** add its `id` + `SUPPORTED_MODELS` entry (`id`, `label`, `short`, `description`, `context`, `tier`), a `MODEL_PROVIDER_SLUGS` entry (≥1 provider→slug), and a `_FALLBACK_MAP` entry; add flagships to `MODELS_SUPPORTING_MAX_EFFORT`.

Sync/regression tests enforce the contract: `tests/fast/test_model_sync.py` (every model has the required fields matching the TS `ModelInfo`, and `SUPPORTED_MODELS` ids ↔ `MODEL_PROVIDER_SLUGS` keys are in parity), `tests/fast/test_provider_model_mapping.py` (every model maps to ≥1 valid provider, a tier, and a per-provider slug — all total, fail loud). See also `docs/design-system.md` for the frontend token/primitive rules the settings UI follows.
