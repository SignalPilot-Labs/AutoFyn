# Security Audit Report: Phantom Connect SDK

**Audit Firm:** AutoFyn SignalPilot

**Audit Model:** Claude Opus (Anthropic)

**Target:** Phantom Connect SDK monorepo (`@phantom/sdk-monorepo`) (https://github.com/phantom/phantom-connect-sdk)

**Repository:** `phantom-connect-sdk`

**Commit Reviewed:** `33efbe59a34a0de25d1bd38f3e91758a802a3f5f`

**Date:** 2026-06-04

**Status:** 5 Medium Vulnerabilities Confirmed (+ 3 Low) + 1 End-to-End Exploit Chain

---

## Executive Summary

This audit reviewed the Phantom Connect SDK TypeScript monorepo — the CLI/MCP agent surface, the browser/embedded provider, the EVM/Solana parsers, the perps client, and the auth2 KMS-RPC client. The root causes cluster around **inconsistent input validation across symmetric code paths**: the SDK builds a defense in one place (private-IP blocking, a payment-transaction schema, a confirmation gate, a pinned EIP-712 domain) and then omits it on a sibling path that handles the same class of data. No RCE, command injection, SQLi, path traversal, or unconditional fund/key exfiltration was found; the browser private-key handling (non-extractable WebCrypto keys, origin-isolated IndexedDB) is sound.

Strongest live-confirmed issues:

- **S1 — Solana RPC SSRF (MEDIUM, 6.5):** the Solana RPC-override path skips the private-IP/loopback/link-local block that the EVM path enforces, reaching cloud IMDS from an MCP tool parameter.
- **S8 — Backend-controlled EIP-712 domain (MEDIUM, 5.3):** `PerpsClient.withdrawFromSpot` signs a backend-supplied EIP-712 struct over an attacker-chosen `verifyingContract` with no allowlist — every sibling signing site pins the domain from constants.
- **S3 — Auto-402 blind-signing asymmetry (MEDIUM, 5.9):** the module-load 402 handler signs any server-supplied `preparedTx` with zero validation, while the explicit `pay_api_access` tool enforces a schema that forbids SOL transfers.
- **S5 — EIP-712 structural validation gap (MEDIUM, 4.3):** `validateEip712TypedData` accepts malformed typed data (primaryType not in types, missing EIP712Domain), directly reachable via the `sign_evm_typed_data` MCP tool.
- **S6 — Confirmation-gate asymmetry (MEDIUM, 4.3):** `buy_token`/perps tools sign in a single call while `transfer_tokens`/`send_solana_transaction` enforce a two-step simulation/confirmation flow.

Three findings are LOW and honestly rated as such (S2 weak OAuth-state PRNG, S4 bug in an unexported never-instantiated legacy class, S7 upstream stale-dependency leak behind a backend/MitM precondition). One exploit chain holds — **CHAIN-A (S1⟶S6)** — a single prompt-injected MCP call that silently amplifies an intended swap; it is live-confirmed on real SDK code for its load-bearing stages, with the on-chain magnitude impact stated as *argued* (bounded by balance, priced by the real quote API), not live-drained. Seven candidate chains were evaluated and rejected with documented source evidence — a deliberate accuracy asset.

---

## Evidence Types

- **Direct Phantom SDK Exploit** — PoC executed against the project's own implementation (real `rpc.ts`, `swap.ts`, `PerpsClient.ts`, `PhantomApiClient.ts`, etc. imported and exercised). The verdict rests on assertions against real SDK code.
- **Direct Phantom SDK Exploit + Attacker Infrastructure** — PoC executed with attacker-controlled auxiliary services (a loopback HTTPS capture server, a loopback HTTP 402 server, or a two-port cross-domain redirect server) driving the real SDK code path.
- **Source-Confirmed / Partial Live** — vulnerable code path confirmed by source review plus limited live probing, where a critical downstream sink (e.g. the opaque KMS) cannot be exercised in the PoC environment.

---

## Findings Table

Sorted by CVSS descending.

| ID | Vulnerability | Severity | CVSS | Status | Evidence |
|----|---------------|----------|------|--------|----------|
| PHANTOM-001 | Inconsistent Solana RPC SSRF — `resolveSolanaRpcUrl` skips private-IP block | MEDIUM | 6.5 | Confirmed | Direct Phantom SDK Exploit + Attacker Infrastructure |
| PHANTOM-002 | Auto-402 blind-signing asymmetry — handler signs unvalidated `preparedTx` | MEDIUM | 5.9 | Confirmed | Direct Phantom SDK Exploit + Attacker Infrastructure |
| PHANTOM-003 | Backend-controlled EIP-712 domain in `PerpsClient.withdrawFromSpot` `authorizeStep` | MEDIUM | 5.3 | Confirmed | Direct Phantom SDK Exploit |
| PHANTOM-004 | `validateEip712TypedData` missing `primaryType`-in-`types` membership check | MEDIUM | 4.3 | Confirmed | Direct Phantom SDK Exploit |
| PHANTOM-005 | MCP financial-action confirmation-gate asymmetry | MEDIUM | 4.3 | Confirmed | Direct Phantom SDK Exploit |
| PHANTOM-006 | follow-redirects 1.15.11 custom-header leak in `@phantom/auth2` (CVE-2026-40895) | LOW | 3.7 | Confirmed | Direct Phantom SDK Exploit + Attacker Infrastructure |
| PHANTOM-007 | Insecure randomness for OAuth state / session ID (weak CSRF-token entropy) | LOW | 3.1 | Confirmed | Direct Phantom SDK Exploit |
| PHANTOM-008 | `BrowserAuthProvider.resumeAuthFromRedirect` conditional CSRF bypass (legacy, unexported) | LOW | 3.1 | Confirmed | Direct Phantom SDK Exploit |

---

## Exploit Chains

### Chain Evidence Matrix

| Chain | Vulnerabilities | Severity | CVSS | Attacker Model | Evidence |
|-------|-----------------|----------|------|----------------|----------|
| CHAIN-A | PHANTOM-001 ⟶ PHANTOM-005 | MEDIUM | 4.3 | M1 — prompt-injected / authorized MCP caller (no backend compromise, no TLS MitM) | Direct Phantom SDK Exploit + Attacker Infrastructure (Stages 1/2/4 live; Stage 3 live, getMint parsed crafted mint) |

Seven additional candidate chains (B–H) were evaluated and **rejected** with documented source evidence (no data-flow edge / per-body credential not replayable / two side-by-side capabilities under one precondition). The rejection rationales are retained at the end of this report as an accuracy asset.

### CHAIN-A — S1⟶S6: RPC-Decimals Amplified Un-Gated Swap

**Severity:** MEDIUM
**CVSS 3.1:** 4.3 `CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N`
**Vulnerabilities:** PHANTOM-001 (Solana RPC SSRF) ⟶ PHANTOM-005 (missing confirmation gate)
**Exploit script:** `autofyn_audit/exploits/c1-rpc-decimals-amplified-swap/run.mjs`
**Evidence tier:** Direct Phantom SDK Exploit + Attacker Infrastructure

A single prompt-injected `buy_token` tool call (`amountUnit:"ui"`, `execute:true`, attacker-controlled `rpcUrl`) composes two MEDIUM M1 findings into a single-call silent magnitude distortion. This is a genuine chain: PHANTOM-001's output (attacker-controlled `getMint` decimals) becomes a *new* input to PHANTOM-005's un-gated execution via `parseUiAmount`.

**Attack flow:**

1. **PHANTOM-001 (Solana rpcUrl un-IP-checked):** `resolveSolanaRpcUrl` accepts the attacker RPC URL without any private-IP/loopback block (`rpc.ts:82-97`, `validateHttpsUrl` checks scheme+hostname only). The EVM path (`validateRpcUrl`) blocks the same URL.
2. **Chain hinge (decimals):** the attacker RPC is consulted for exactly one scalar — `getMint` decimals — at `buy-token.ts:220-223`/`236-239`. The crafted SPL-mint account returns `decimals=<attacker-chosen>`, which flows to `parseUiAmount(amount, decimals!)` at `:247`, then to `sellAmount` in the Phantom quote request (`:283-284`).
3. **PHANTOM-005 (missing confirmation gate):** `buy_token execute:true` → `executeSwap` → `signAndSendTransaction` in a single call with no `runSimulation`, no `pending_confirmation`, no user-visible magnitude preview (`buy-token.ts:302-314` → `swap.ts:335-341`).

**Confirmed output:**

```
  Stage 1 [LIVE]  S1 validator asymmetry:               CONFIRMED
  Stage 2 [LIVE]  S6 single-call no-gate executeSwap:   CONFIRMED
  Stage 3 [LIVE]  attacker RPC controls decimals:       LIVE (getMint parsed attacker decimals)
  Stage 4 [LIVE]  parseUiAmount amplification:          CONFIRMED
       parseUiAmount('1.0', 6)  = 1000000            (10^6, honest)
       parseUiAmount('1.0', 30) = 10^30              (attacker, 24-order inflation)
  Overall CHAIN-A: CONFIRMED
```

**Honest impact ceiling:** silent magnitude distortion of an intended swap, **bounded by the user's token balance**, routed through the real Phantom quote API. An absurd inflation (`decimals=30`) exceeds any real balance and the quote/on-chain execution rejects it; a realistic attacker tunes decimals to inflate within the victim's balance. **NOT** arbitrary-recipient theft, **NOT** key exfil, **NOT** an unconditional drain. The on-chain over-spend is *argued* (the PoC uses a stub client and does not contact the live quote API); the amplification *mechanism* is proven live on real SDK code. The same prompt-injected agent could call `buy_token` with a larger `amount` directly — the chain's novel property is that the over-spend is **silent** (no preview), not that it grants a new privilege.

---

## Vulnerability Details

### PHANTOM-001 — Inconsistent Solana RPC SSRF

**Severity:** MEDIUM — CVSS 3.1 6.5 `CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N`
**CWE:** CWE-918 (Server-Side Request Forgery)
**Affected Code:** `packages/cli/src/utils/rpc.ts` — `validateHttpsUrl` (30-43), `resolveSolanaRpcUrl` (82-97); contrast `validateRpcUrl` (51-76), `resolveEvmRpcUrl` (103-115). Callers: `packages/cli/src/actions/buy-token.ts:105,141,220-223`, `packages/cli/src/actions/transfer-tokens.ts:76,277-278`.

**Description:** The EVM RPC-override path validates with `validateRpcUrl`, which blocks loopback (`localhost`/`127.0.0.1`/`::1`), RFC-1918 ranges, and link-local `169.254.x` (cloud IMDS). The Solana override path validates with `validateHttpsUrl`, which checks only that the protocol is `https:` and the hostname is non-empty — **no IP-range check**. An MCP tool caller can therefore supply a Solana `rpcUrl` pointing at internal/metadata endpoints. The SSRF is session-gated (`getSession()` at `buy-token.ts:141` throws if uninitialized), hence PR:L; C:H is realized on a cloud host with a reachable metadata service.

**Vulnerable Code:**

```typescript
// rpc.ts — resolveSolanaRpcUrl routes through validateHttpsUrl (NO IP check)
function validateHttpsUrl(url: string, label: string): void {
  const parsed = new URL(url);
  if (parsed.protocol !== "https:") throw new Error(`${label} must use https`);
  if (!parsed.hostname) throw new Error(`${label} hostname is empty`);
  // ← no private-IP / loopback / link-local block (validateRpcUrl has it)
}
```

**Attack Scenario:** A prompt-injection payload or malicious upstream tool result supplies `rpcUrl: "https://169.254.169.254/latest/meta-data/"` to `buy_token`; `new Connection(url)` dials cloud IMDS and the response can leak instance credentials. The identical URL on the EVM path throws.

**Proof of Concept:**

```bash
cd packages/cli && npx tsx \
  ../../autofyn_audit/exploits/s1-solana-rpc-ssrf/run.mjs
# LAYER 1: validateRpcUrl(IMDS-IP) throws; resolveSolanaRpcUrl returns it.
# LAYER 2: new Connection(loopback-HTTPS).getLatestBlockhash() dials the capture server.
```

**Remediation:** Route the Solana override through the same `validateRpcUrl` used by the EVM path so private/loopback/link-local IPs are blocked uniformly; optionally add a DNS-resolution-time IP re-check to defend against rebinding.

---

### PHANTOM-002 — Auto-402 Blind-Signing Asymmetry

**Severity:** MEDIUM — CVSS 3.1 5.9 `CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:H/A:N`
**CWE:** CWE-345 (Insufficient Verification of Data Authenticity), CWE-20 (Improper Input Validation)
**Affected Code:** `packages/cli/src/index.ts` — `apiClient.setPaymentHandler` block, lines 50-72 (decode+sign at 60-66); contrast `packages/cli/src/actions/pay-api-access.ts` — `PaymentTransactionSchema` (29-112) + `runSimulation` gate (155-167). `packages/phantom-api-client/src/PhantomApiClient.ts:186-202` builds `PaymentRequiredError` from unvalidated `body.payment`.

**Description:** The module-load 402 handler decodes any server-supplied `payment.preparedTx` and forwards it to `signAndSendTransaction` with **zero validation**. The explicit `pay_api_access` tool enforces `PaymentTransactionSchema` (forbids `SystemProgram` native-SOL transfers, requires ≥1 SPL token transfer, runs a simulation gate). The two paths handle the same payload class with asymmetric defenses. The precondition is controlling a 402 response body (TLS MitM or compromised/substituted backend), hence AC:H — but a `SystemProgram.transfer` SOL drain is precisely what `pay_api_access` was written to forbid, so the auto-handler bypassing that denial crosses a boundary the SDK itself erected.

**Vulnerable Code:**

```typescript
// index.ts:60-66 (auto-handler) — no schema, no simulation gate
const txBytes = Buffer.from(payment.preparedTx, "base64");
const result = await client.signAndSendTransaction({
  walletId: session.walletId,
  transaction: base64urlEncode(txBytes),
  networkId: NetworkId.SOLANA_MAINNET,
  account,
});
```

**Attack Scenario:** An attacker controlling the 402 response injects a `SystemProgram.transfer` `preparedTx`; the auto-handler signs and broadcasts a native-SOL drain that `pay_api_access` would have rejected.

**Proof of Concept:**

```bash
cd packages/cli && npx tsx \
  ../../autofyn_audit/exploits/s3-auto402-blind-signing/run.mjs
# Live: real PhantomApiClient._pay → registered handler (body = verbatim transcription
# of index.ts:60-66) forwards the unvalidated SystemProgram.transfer to the signer.
```

**Remediation:** Route the auto-handler through `PaymentTransactionSchema` and the `runSimulation` gate (same as `pay_api_access`); validate `body.payment` in `handleResponse` before constructing `PaymentRequiredError`.

---

### PHANTOM-003 — Backend-Controlled EIP-712 Domain in `PerpsClient.withdrawFromSpot`

**Severity:** MEDIUM — CVSS 3.1 5.3 `CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:N/I:H/A:N`
**CWE:** CWE-345 (Insufficient Verification of Data Authenticity)
**Affected Code:** `packages/perps-client/src/PerpsClient.ts:356-361` (`authorizeStep` sign); contrast `depositStep` (380-385); `RelayWithdrawalV2Quote.authorizeStep` at `packages/perps-client/src/types.ts:233-241` (`verifyingContract` at `:235`); pinned domains at `packages/perps-client/src/constants.ts:9-13,16-21`.

**Description:** `withdrawFromSpot` passes the four EIP-712 fields `{domain, types, primaryType, message}` from the backend-supplied `authorizeStep` **verbatim** to `signTypedData` — including `domain.verifyingContract` — with no domain pinning and no allowlist. Every other perps signing site pins the domain from constants (`HYPERLIQUID_EXCHANGE_DOMAIN`, `HYPERLIQUID_SIGN_TRANSACTION_DOMAIN`, both with `verifyingContract = 0x000…000`), and `depositStep` only lets the backend extend `types`. `authorizeStep` is the single signing site where the backend controls all four fields. Unlike a generic blind-sign, this grants a capability the backend otherwise lacks: a KMS signature over an attacker-chosen `verifyingContract` (I:H).

**Vulnerable Code:**

```typescript
// PerpsClient.ts:356-361 — backend authorizeStep passed verbatim, no allowlist
const authSignatureRaw = await this.signTypedData({
  domain: authorizeStep.domain,        // includes attacker-chosen verifyingContract
  types: authorizeStep.types,
  primaryType: authorizeStep.primaryType,
  message: authorizeStep.message,
});
```

**Attack Scenario:** A compromised/MitM backend returns a `bridge-initialize` quote whose `authorizeStep` is `Permit{owner:user, spender:attacker, value:MAX_UINT256}` over a real ERC-20 `verifyingContract`; the KMS signs it, yielding an off-platform-redeemable permit (ERC-2612/Permit2/Seaport) that does not route back through Phantom.

**Proof of Concept:**

```bash
cd packages/perps-client && npx tsx \
  ../../autofyn_audit/exploits/s8-perps-eip712-blind-sign/run.mjs
# call[0].domain.verifyingContract === attacker address (PASS)
# negative control: deposit() call uses pinned 0x000...000 (PASS)
```

**Note (honesty cap):** the PoC proves only that the unvalidated attacker domain/message reaches the signer and no allowlist throws (stub signer; KMS opaque). The off-platform-redeemable-permit impact is an *argued* consequence of EIP-712 semantics, not a live-drained demonstration.

**Remediation:** Add a `verifyingContract`/domain allowlist for the `authorizeStep` path (the valid Relay V2 addresses are known and small); or apply the sibling `depositStep` pattern — construct `domain` from a constant and let the backend extend only `types`.

---

### PHANTOM-004 — `validateEip712TypedData` Missing `primaryType`-in-`types` Membership Check

**Severity:** MEDIUM — CVSS 3.1 4.3 `CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N`
**CWE:** CWE-20 (Improper Input Validation)
**Affected Code:** `packages/parsers/src/index.ts` — `validateEip712TypedData` (43-65); caller `packages/cli/src/actions/sign-evm-typed-data.ts:69` (MCP tool `sign_evm_typed_data`); zod schema at `sign-evm-typed-data.ts:20-40`.

**Description:** `validateEip712TypedData` checks top-level shape (object, non-null `types`, non-empty `primaryType`, object `domain`/`message`) but omits three structural membership checks required for well-formed EIP-712 data: (a) `primaryType ∈ keys(types)`, (b) `EIP712Domain ∈ keys(types)`, (c) `types[primaryType]` is a non-empty array. The zod schema (`z.record(z.string(), z.unknown())`) does not enforce them either. This is the only one of the input-validation findings reachable **directly via an MCP tool parameter** with no special privileges.

**Vulnerable Code:**

```typescript
// parsers/src/index.ts:43-65 — checks shape, not membership
// primaryType="MISSING_TYPE" with types={EIP712Domain, Permit}  → accepted
// types={Permit:[]} (no EIP712Domain)                           → accepted
// types={Transfer:[]} with primaryType="Transfer" (empty array) → accepted
```

**Attack Scenario:** A `sign_evm_typed_data` caller supplies structurally invalid EIP-712 data that passes the SDK validator; if the downstream KMS does not independently reject, malformed structures (e.g. zero-field permits) could be signed.

**Proof of Concept:**

```bash
cd packages/parsers && npx tsx \
  ../../autofyn_audit/exploits/s5-eip712-primarytype-gap/run.mjs
# Cases A/B/C: validateEip712TypedData does NOT throw on malformed typed data.
# Negative control: clearly-invalid shape DOES throw (validator is live).
```

**Remediation:** Enforce `primaryType in types`, `EIP712Domain in types`, and that each `types[k]` is a non-empty array of `{name, type}` in `validateEip712TypedData`.

---

### PHANTOM-005 — MCP Financial-Action Confirmation-Gate Asymmetry

**Severity:** MEDIUM — CVSS 3.1 4.3 `CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N`
**CWE:** Missing confirmation step (inconsistent transaction-confirmation control). Deliberately **not** framed as CWE-862 — nothing the caller is unauthorized for is performed; the gap is a missing user-confirmation/preview, not an access-control failure.
**Affected Code:** `packages/cli/src/actions/buy-token.ts:96-103,302-314`; `packages/cli/src/utils/swap.ts:206-404` (Solana branch 320-341); `open-perp-position.ts`, `close-perp-position.ts`, `cancel-perp-order.ts` (no gate). Contrast (gated): `transfer-tokens.ts:81-87,359-373`, `send-solana-transaction.ts:32-37,89-111`.

**Description:** `transfer_tokens` and `send_solana_transaction` enforce a two-step flow: the first call runs `runSimulation()` and returns `{ status: "pending_confirmation" }` without signing; only a second call with `confirmed:true` reaches `signAndSendTransaction`. `buy_token execute:true` and the perps tools have no such gate — a single call signs and broadcasts with no simulation/preview. The missing step is a human-in-the-loop preview, not an authorization boundary (the caller is already authorized to swap), so impact is I:L: bounded economic distortion via the Phantom-priced route, no arbitrary recipient.

**Vulnerable Code:**

```typescript
// swap.ts:335-341 (Solana same-chain branch) — single sign, no gate
const result = await client.signAndSendTransaction({ walletId, transaction, networkId, account });
// vs transfer-tokens.ts:359-373 — runSimulation() → return {status:"pending_confirmation"} unless confirmed
```

**Attack Scenario:** A prompt-injected agent calls `buy_token execute:true` (or a perps tool) and the swap/position executes with no user-visible simulation step or opportunity to reject.

**Proof of Concept:**

```bash
cd packages/cli && npx tsx \
  ../../autofyn_audit/exploits/s6-mcp-confirmation-gate-asymmetry/run.mjs
# PART A (real executeSwap): signAndSendTransaction called once, no simulation.
# PART C (real .ts scan): gate present in transfer/send, absent in buy/perps.
```

**Remediation:** Add a `confirmed`/`dryRun` gate to `buy_token execute:true` and the perps tools matching the `transfer_tokens`/`send_solana_transaction` pattern; establish a policy that every signing tool runs the two-step simulation/confirmation flow.

---

### PHANTOM-006 — follow-redirects 1.15.11 Custom-Header Leak in `@phantom/auth2` (CVE-2026-40895)

**Severity:** LOW — CVSS 3.1 3.7 `CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:N/A:N`
**CWE:** CWE-201 (Sensitive Information in Sent Data) — **CVE-2026-40895**
**Affected Code:** `packages/auth2/node_modules/follow-redirects@1.15.11` (vulnerable) vs `packages/cli/node_modules/follow-redirects@1.16.0` (patched); headers set at `packages/auth2/src/Auth2KmsRpcClient.ts:44-56`.

**Description:** `@phantom/auth2`'s dependency tree pins the vulnerable `follow-redirects@1.15.11`, which on a cross-domain 3xx redirect strips only `authorization`/`proxy-authorization`/`cookie` and forwards custom headers verbatim. The signing credential `x-phantom-stamp` and OIDC subject `x-auth-user-id` that `Auth2KmsRpcClient` adds to every request leak to the redirect destination. This is an **upstream stale-transitive-dependency** issue; the sibling `@phantom/cli` already ships the patched `1.16.0`. The leaked stamp is a per-request-body signature (single-use, not a replayable bearer), and under the redirect/MitM precondition the in-path attacker already receives these headers — hence C:L and AC:H.

**Attack Scenario:** A cross-domain redirect from the KMS backend (or a TLS MitM) causes the per-request signing credential and OIDC subject to be sent to a third-party destination.

**Proof of Concept:**

```bash
cd packages/auth2 && npx tsx \
  ../../autofyn_audit/exploits/s7-follow-redirects-header-leak/run.mjs
# Version guard exits 1 unless follow-redirects is 1.15.11.
# x-phantom-stamp + x-auth-user-id arrive at portB; authorization correctly stripped.
```

**Remediation:** Bump `follow-redirects` to `>=1.16.0` in `@phantom/auth2`'s tree (workspace `resolutions` if hoisting keeps a stale copy); declare custom secret headers in axios's `sensitiveHeaders` so they are stripped before any redirect.

---

### PHANTOM-007 — Insecure Randomness for OAuth State / Session ID

**Severity:** LOW — CVSS 3.1 3.1 `CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:L/I:N/A:N`
**CWE:** CWE-330 (Use of Insufficiently Random Values), CWE-338 (Use of Cryptographically Weak PRNG)
**Affected Code:** `packages/embedded-provider-core/src/utils/session.ts` — `generateSessionId()` (1-9); consumed as OAuth `state` at `packages/auth2/src/auth2Flow.ts:133`, CSRF check at `auth2Flow.ts:178-180`. (The CLI path uses `crypto.randomBytes(32)` at `packages/cli/src/auth/oauth.ts:310` and is NOT affected.)

**Description:** `generateSessionId()` derives the OAuth `state` CSRF token solely from `Math.random()` (V8 xorshift128+ — deterministic, not cryptographically secure), with no `crypto` path. The `state` is the sole CSRF guard at callback time. Published research establishes the theoretical basis for xorshift128+ state recovery, but the base-36 mantissa truncation in the session-ID format substantially increases the difficulty; the PoC demonstrates same-isolate record-and-replay determinism only (I:N — no signing/fund-loss impact shown). The PKCE `code_verifier` is separately CSPRNG (`auth2Flow.ts:89`).

**Attack Scenario:** Under a threat model where an attacker can recover xorshift128+ state from observable outputs, the OAuth-state CSRF guard could be weakened.

**Proof of Concept:**

```bash
cd packages/cli && npx tsx \
  ../../autofyn_audit/exploits/s2-weak-oauth-state-prng/run.mjs
# generateSessionId() makes 2 Math.random() calls, 0 crypto.getRandomValues calls.
# Recorded floats reproduce the session ID exactly (same-isolate determinism).
```

**Remediation:** Replace `Math.random()` in `generateSessionId()` with `crypto.randomUUID()` or `crypto.getRandomValues()`.

---

### PHANTOM-008 — `BrowserAuthProvider.resumeAuthFromRedirect` Conditional CSRF Bypass

**Severity:** LOW — CVSS 3.1 3.1 `CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:L/I:N/A:N`
**CWE:** CWE-352 (Cross-Site Request Forgery), CWE-287 (Improper Authentication)
**Affected Code:** `packages/browser-sdk/src/providers/embedded/adapters/auth.ts:148` (guard); context from `sessionStorage` at `auth.ts:137-145`; `AuthResult` from URL params at `auth.ts:196-203`.

**Description:** The CSRF guard `if (context.sessionId && sessionId !== context.sessionId)` is a no-op whenever `context.sessionId` is falsy. `context` comes from `sessionStorage.getItem("phantom-auth-context")`, which is `null` on first visit / cross-tab / post-refresh, leaving `context = {}` and the guard skipped; `resumeAuthFromRedirect` then returns an `AuthResult` built entirely from attacker-controlled URL params. **Crucially**, `BrowserAuthProvider` is **not exported from the package's public entrypoint** and is **never instantiated anywhere in the repo** — production wires `Auth2AuthProvider`, whose guard is unconditional and sound. Reaching this bug requires an integrator to deliberately wire a legacy, non-default, unexported class (AC:H), and the downstream impact of the injected `walletId`/`organizationId` is undemonstrated (C:L/I:N).

**Vulnerable Code:**

```typescript
// auth.ts:148 — guard skipped when context.sessionId is falsy
if (context.sessionId && sessionId !== context.sessionId) {
  throw new Error("Session ID mismatch - possible session corruption or replay attack");
}
// fail-closed fix: if (!context.sessionId || sessionId !== context.sessionId)
```

**Attack Scenario:** If an integrator wires `BrowserAuthProvider`, an attacker who navigates the victim to the callback URL with attacker-chosen params (empty `sessionStorage`) injects an attacker `walletId`/`organizationId`.

**Proof of Concept:**

```bash
cd packages/browser-sdk && npx tsx \
  ../../autofyn_audit/exploits/s4-browser-auth-csrf-bypass/run.mjs
# Case 1 (empty sessionStorage): attacker walletId accepted (guard skipped).
# Case 2 (present+mismatched): guard fires and throws.
```

**Remediation:** Change the guard to fail-closed: `if (!context.sessionId || sessionId !== context.sessionId)`.

---

## Reproduction Instructions

**Prerequisites:**
- Node.js (the audit baseline used v24; verified live on v22), `corepack`-provisioned `yarn@4.2.2`, `openssl`, and (optional) Docker for pinned-image reproducibility.
- The repo at commit `33efbe59a34a0de25d1bd38f3e91758a802a3f5f`. The findings' source is unchanged at later audit-round commits (only the report/scripts changed).

**Run:**

```bash
# 1. Install workspace deps + build all package dist/ (required for the @phantom/* imports)
bash autofyn_audit/setup.sh

# 2. Run all PoCs (S1–S8 + CHAIN-A), printing CONFIRMED / NOT CONFIRMED per finding
bash autofyn_audit/run_exploits.sh
```

**Expected output:** all nine entries report `CONFIRMED` (exit 0). The S7 PoC's version guard requires `follow-redirects@1.15.11` in `packages/auth2/node_modules` (installed by `setup.sh`); the live tree confirms `auth2` at `1.15.11` while `cli` is at `1.16.0`.

```
  S1: Solana RPC SSRF                           CONFIRMED
  S2: Insecure Randomness (CWE-330/338)         CONFIRMED
  S3: Auto-402 blind-signing asymmetry          CONFIRMED
  S4: BrowserAuthProvider CSRF bypass           CONFIRMED
  S5: EIP-712 primaryType-in-types gap          CONFIRMED
  S6: MCP confirmation-gate asymmetry           CONFIRMED
  S7: follow-redirects 1.15.11 header leak      CONFIRMED
  S8: PerpsClient authorizeStep blind EIP-712   CONFIRMED
  C1 (CHAIN-A): RPC-decimals amplified swap     CONFIRMED
```

**Cleanup:** `bash autofyn_audit/teardown.sh` (stops any audit Docker container and frees PoC ports).

---

## Conclusion

The systemic issue is **asymmetric validation across symmetric code paths**: the SDK demonstrably knows how to defend each surface (the EVM RPC path blocks private IPs, `pay_api_access` enforces a payment schema, `transfer_tokens` gates on simulation, `depositStep` pins its EIP-712 domain) yet ships a sibling path that omits the same control (the Solana RPC path, the auto-402 handler, `buy_token`/perps, `authorizeStep`). The fixes are small and local — route the second path through the same validator/gate/allowlist the first path already uses.

**Priority remediation order:**

1. **PHANTOM-001** — route `resolveSolanaRpcUrl` through `validateRpcUrl` (closes the SSRF and breaks CHAIN-A's hinge).
2. **PHANTOM-003** — add a `verifyingContract` allowlist on the `authorizeStep` signing path (the only off-platform-redeemable signature).
3. **PHANTOM-002** — apply `PaymentTransactionSchema` + simulation gate to the auto-402 handler.
4. **PHANTOM-005** — add the two-step confirmation gate to `buy_token`/perps (also breaks CHAIN-A's execution leg).
5. **PHANTOM-004** — enforce EIP-712 structural membership in `validateEip712TypedData`.
6. **PHANTOM-006 / 007 / 008** (LOW) — bump `follow-redirects` in `auth2`, switch `generateSessionId` to CSPRNG, fail-close the `BrowserAuthProvider` guard.

---

## Files Delivered

```
autofyn_audit/
├── audit_report.md                  (this report)
├── README.md
├── PINNED_COMMIT.txt
├── Dockerfile
├── setup.sh / run_exploits.sh / teardown.sh
├── lib/
│   └── capture-server.mjs
├── docs/                            (advisories + hardening notes)
│   ├── CVE-PHANTOM-001.md           (advisory — Solana RPC SSRF)
│   ├── CVE-PHANTOM-002.md           (advisory — auto-402 blind-signing)
│   ├── CVE-PHANTOM-003.md           (advisory — backend-controlled EIP-712 domain)
│   └── HARDENING-NOTES.md           (PHANTOM-004 + PHANTOM-005 — documented, not filed as advisories)
└── exploits/
    ├── s1-solana-rpc-ssrf/run.mjs
    ├── s2-weak-oauth-state-prng/run.mjs
    ├── s3-auto402-blind-signing/run.mjs        (+ payment-schema.mjs, labeled reference copy)
    ├── s4-browser-auth-csrf-bypass/run.mjs
    ├── s5-eip712-primarytype-gap/run.mjs
    ├── s6-mcp-confirmation-gate-asymmetry/run.mjs (+ confirmation-gate-reference.mjs, labeled)
    ├── s7-follow-redirects-header-leak/run.mjs
    ├── s8-perps-eip712-blind-sign/run.mjs
    └── c1-rpc-decimals-amplified-swap/run.mjs
```

---

## Appendix: Rejected Findings & Chains (Accuracy Asset)

The following candidates were investigated and **rejected** with source evidence. Accurate rejection of false positives is a deliberate quality signal.

**Rejected findings:**
- **R1 — Developer-config `apiBaseUrl`/`authApiBaseUrl` SSRF:** `baseUrl` is developer configuration set at SDK init, not an attacker-reachable input crossing a trust boundary.
- **R2 — EIP-6963 / Wallet Standard provider injection:** in-page provider injection is by specification; an in-page script already has full DOM access.
- **R3 — Plaintext `session.json` / `auth2-stamper.json`:** files are `0o600`, dirs `0o700` — standard local-user secret storage, on par with `~/.ssh/id_rsa`.
- **R4 — No MCP stdio transport auth:** stdio runs under the local user with no network socket; co-user/subprocess threats are out of the documented model.
- **R5 — `execFile` browser-open arg injection:** no shell; URL derived from developer-configured `baseUrl`, not attacker-reachable.
- **R6 — OAuth callback `wallet_id` not server-verified:** superseded by PHANTOM-008 (the conditional `BrowserAuthProvider` guard).
- **R7 — JWT no client-side signature verification:** by design — the token endpoint is the authority and server-side KMS re-validates on stamp use.
- **R8 — Axios CVEs / debug-log leakage / PKCE `.slice(96)`:** axios v1.15.1 is patched for the cited CVEs; the rest require developer misconfiguration or are no-ops.

**Rejected chains (B–H):** each was rejected because the composition has no internal data-flow edge — the leaked `x-phantom-stamp` is a per-request-body signature (not a replayable bearer), the supposed "predicted state" is never needed by the receiving path, faked decimals self-defeat under `TransferChecked`, or two M2 capabilities merely stand side-by-side under one precondition (the union of two independent backend capabilities does not exceed the strongest single part). Full per-chain rationales are retained in the exploit directories' READMEs.
