# Build report — clique-descent (round 2)

**Status: partial.** Retargeted OFF the false Lemma S. File: `results/imo-2026-06/approaches/clique-descent.md`.

## What is now rigorous (new this round)
1. **Import** of the certified reduction §§0–4 → Crux = "finitely many minimal clauses."
2. **Lemma 1 (self-blocking clutter):** minimal clauses M satisfy `T is a clause ⟺ T transversal of M`, so `M = b(M)`. Intrinsic, clean, promotable. Makes explicit that any finiteness must use the arithmetic (small/large split), since self-blocking clutters can be infinite.
3. **Proposition 2 (finite-ground-set reduction):** if `Q = {large primes in some minimal clause}` is finite, then all minimal clauses ⊆ finite Π∪Q, so finitely many ⟹ conclusion. This is the airtight, non-circular replacement for the retracted false Proposition 1. **Key simplification: it removes the need for any per-large-prime / sunflower bound** — ground-set finiteness alone caps M. Sole crux becomes "Q finite."
4. **Lemma 3 (mutual witness):** every q∈Q lies in two distinct minimal clauses C,D with C∩D={q} and disjoint nonempty small-shadows. Gives a reconciliation map Φ: Q → {disjoint shadow-pairs of Π} with FINITE image (≤3^{π(P₁)}). Prop 3: Q finite ⟺ Φ has finite fibers.

## The single remaining gap
**Finite fibers of Φ** (equiv. Q finite): for each disjoint pair (σ,τ) of nonempty subsets of Π, only finitely many large primes reconcile it.
- **Conditional close proved:** IF every minimal clause has ≤1 large prime (**Lemma T**), then for each shadow σ there is one fixed minimal clause W_σ with W_σ∩σ=∅, and every q with a shadow-σ minimal clause must lie in W_σ ⟹ ≤|W_σ| such q ⟹ Q finite. Clean.
- **But Lemma T is NOT established.** Verified for many a₁ (385,4199,255,1001,...), but shallow sim of primorials (a₁=255255, N=1000) shows apparent multi-large minimal clauses — almost certainly truncation artifacts (reviewer flagged 2310 overcounts until N≥1600), but I could not run primorials to convergence in budget. So Lemma T is left open, and with it the fiber bound.

## Spec-concerns (important)
- **Clique-descent's round-2 sunflower step (step 3) is NOT combinatorially free.** "Fixed large q ⟹ its minimal clauses have pairwise-disjoint shadows" cannot be proved from self-blocking-clutter combinatorics alone (self-blocking clutters admit many same-shadow members); it needs the same greedy-size arithmetic as the fiber bound. **Fortunately Proposition 2 makes the per-prime/sunflower bound unnecessary** — so this does not weaken the approach, it re-routes it: the ONLY gap is "Q finite."
- **Shared-gap confirmed.** The fiber bound = descent-shared-prime's Lemma S′ `b≤a₁` branch = one arithmetic fact (a large prime cannot repeatedly reconcile a fixed disjoint small-shadow gap because the greedy prefers smaller reconcilers). If both stall in round 3, open the growth/size framing directly (bound the largest prime in a term via a_n ≤ n·a₁ + mature small-prime admissible density). This is the reviewer's predicted 4th framing.

## Promotable lemmas (for certification)
- Lemma 1 (self-blocking clutter), Proposition 2 (finite-ground-set reduction), Lemma 3 (mutual witness). All proved in full in §§1–3; Proposition 2 is reusable by every approach.

## Line for orchestrator
Proof written to results/imo-2026-06/approaches/clique-descent.md (Status: partial)
