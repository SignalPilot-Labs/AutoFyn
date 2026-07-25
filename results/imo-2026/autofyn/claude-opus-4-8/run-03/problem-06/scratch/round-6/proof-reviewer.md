# Proof-reviewer — imo-2026-06, Round 6

Two built slugs judged independently. Neither claims a solve; the whole theorem remains reduced to
the single open inequality **E5″**. Status of the problem stays **partial**.

---

## 1. redundant-constraint-antichain — CHANGES REQUESTED (Status: partial)

**Round 6 deliverable:** consolidation only (§14) — no new E5″ lever. Two parts: (14.1) the reduction
chain `E5″ ⟹ (W) ⟹ E5 ⟹ Crux ⟹ theorem` verified link-by-link; (14.2) the impossibility map
cross-linking the new Rejection-Budget guardrail alongside R4 Collapse / R5 JSC / R2 obstruction.

**Load-bearing check — I re-derived the chain link-by-link against the certified files:**
- **E5″ ⟹ (W).** Case split on `∏G`: if `∏G < a₁` then `redMax(G) = ∏(G∖{p_max}) ≤ ∏G < a₁`
  unconditionally; if `∏G ≥ a₁`, E5″ gives it directly. Exhaustive, disjoint, correct. ✓
- **(W) ⟹ E5.** Prop 12.B (certified `realizer-value-pincer.md`): `G∖{p_max}` has `|G|−1` primes with
  product `< a₁`, so by primorial bound R2 `P_{|G|−1} ≤ ∏(G∖{p_max}) < a₁`, giving `|G| ≤ 1+K(a₁)`.
  Re-checked R2 (product of `r` distinct primes `≥` r-th primorial): correct. ✓
- **E5 ⟹ Crux.** E4 (certified `size-bound-reduction.md`): `𝓐_∞` finite ⟺ `sup|G| < ∞`. Re-read the
  chain-descent proof — Anchor base, Case A impossibility via Lemma 11.0, Case B pigeonhole — sound and
  unconditional. ✓
- **Crux ⟹ theorem.** Endgame §4–§5 (Lemmas 9,10, Cor 11) + no-transient L7–L8 (certified). Uses
  ONLY finiteness of `Π`; never E5″ or E4. ✓

**Non-circularity:** confirmed — the endgame consumes only `Π` finite; E4/12.B/R2 use only
E1/E2/Anchor/antichain/primorial arithmetic, all certified independently of the endgame. No hidden
lemma. The honesty note (only sufficiency `E5″ ⟹ theorem` is claimed, not the reverse) is correct.

**Overclaim check:** none. Status `partial` is honest; §14 explicitly asserts nothing beyond the
certified chain and recorded guardrails; E5″ is flagged as the single open gap. The builder's recorded
Status is correct.

**Scores:** Correctness 10/10 (chain is airtight modulo the flagged E5″), Rigor 10/10 (no
hand-waving, no skipped case in the deduction), Progress modest (consolidation, no new sub-result —
but the link-by-link audit has independent certification value). The E5″ gap remains fully open.

**Verdict: CHANGES REQUESTED** (partial). The technique is right and the reduction is now
reviewer-audited end-to-end; the sole remaining gap is E5″ (`∏G ≥ a₁ ⟹ ∏(G∖{p_max}) < a₁`).

---

## 2. joint-recruitment-budget — RETHINK (Status: partial; certified negative guardrail salvaged)

**Round 6 deliverable:** a NEW far-framing pole whose positive route (a disjoint per-recruit cost on
the greedy rejection stream, forcing `c_q → ∞` against a bounded budget, to contradict Π infinite) is
proven to FORK — delivered as the certified **Rejection-Budget Dichotomy** negative guardrail.

**(a) Φ_N identity + O(N) bound — CORRECT.** `Φ_N = Σ_{n<N}(a_{n+1}−a_n−1) = (a_N−a₁)−(N−1)` is a
telescoping identity; `≤ (M−1)(N−1)` from Gap-bound L2 (each gap `≤ M`). I re-ran the greedy
simulation for `a₁ ∈ {375,385,867,105}`, `N=400`: `Φ_N` equals `a_N−a₁−(N−1)` **exactly** (1466 /
3044 / 798 / 1046), every max gap `≤ M`, `Φ_N ≤ (M−1)(N−1)` — reproduces the file's table exactly.

**(b) Tautology + rate-not-count — RIGOROUS.** `Σ_q|C_q| ≤ Φ_N` for disjoint subsets of a size-`Φ_N`
set is trivial. The load-bearing move — that a bounded sum `Σ_{k≤r} c_k ≤ (M−1)(N−1)` with `c_k → ∞`
forces `r(N) ≤ K_T + (M−1)(N−1)/T` (sub-linear) but NEVER bounds `r(N)` — is correct, and correctly
witnessed by the certified obstruction family `{p*, q_k}` (density(A)→positive, `r(N)→∞` sub-linearly,
Π infinite, no contradiction). This is the honest heart: cardinality of a disjoint budget bounds
recruit RATE, never COUNT. Sound.

**(c) The three forks — SOUND.** Horn A (window of length `<M` holds `≤ M−1` integers ⇒ `|C_q|≤M−1`
bounded) is rigorous. Horn B(ii) reduces to certified-dead JSC (`t_k−t'_k = q_k(A_k−B_k)`,
`A_k≠B_k` ⇒ spread bound = magnitude bound). The vocabulary variant reduces to certified-dead R4
Collapse, and is **correctly flagged circular** (assuming `B` ranges over a finite set is `∏B < a₁`,
which IS E5″). Each fork is a valid pointer to an already-certified negative.

**(d) Scope honesty — CORRECT.** The "exhausts all attribution rules" slogan is explicitly flagged as
heuristic (no formal quantifier), exactly as JSC scoped itself. What is certified is rule-independent:
RBT holds for ANY disjoint attribution. No overclaim; Status `partial` in-file is honest.

This is a genuine, correct negative guardrail — but it does NOT close E5″ and provably cannot as a
positive route. Per the established pattern for proven-fork poles (JSC, Collapse), the honest routing
is **RETHINK** with the guardrail certified as salvage.

**Scores:** Correctness 10/10 (every claimed part of the dichotomy is correct — no part is wrong or
escapable), Rigor 9/10 (the certified core is tight; the "exhausts all rules" slogan honestly
downgraded to heuristic), Progress as a positive route 0 (forks), as negative content real (closes the
last joint-accounting thread).

**Verdict: RETHINK** (unsolved as a positive route). Certified salvage recorded.

---

## Lemma certification

Both promotable lemmas admitted into `results/imo-2026-06/lemmas/rejection-budget-dichotomy.md`:
- **RBT (Rejection-Budget Tautology)** — CERTIFIED (fully rigorous, unconditional): telescoping
  identity + Gap-bound L2 + disjoint-cardinality. Numerically reproduced.
- **RBD (Rejection-Budget Dichotomy)** — CERTIFIED as a scoped negative guardrail: the rate-not-count
  consequence, Horn A's `M−1` bound, and the two reductions (Horn B(ii)⟶JSC, vocabulary⟶Collapse) are
  certified; the "exhausts all rules" slogan is admitted only as heuristic (flagged in-file), exactly
  as JSC. Third certified negative around E5″, companion to `two-anchor-scaffold.md` and
  `anchor-partition.md`.

Leader proposed no new promotable lemma this round (consolidation only) — nothing to certify from it.

## Recorded outcomes
- redundant-constraint-antichain — `partial` (Elo 1690.6, LIVE leader).
- joint-recruitment-budget — `dead-end` (Elo 1530.0, RETHINK, salvage certified).

## Problem status: partial. Sole open gap: E5″ — every ⊆-minimal support `G` with `∏G ≥ a₁` has
`∏(G∖{p_max}) < a₁`. Plateau confirmed structural; all single-support/pair/disjoint-cost levers
certified dead.
