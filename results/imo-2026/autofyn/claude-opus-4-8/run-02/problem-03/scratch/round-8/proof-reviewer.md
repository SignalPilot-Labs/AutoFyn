# Proof-reviewer report — imo-2026-03 (IMO 2026 P3), Round 8

Three slugs built. I re-derived and numerically verified every new load-bearing claim
(`/tmp/verify8.py`, `verify8b.py`, `verify8c/d.py`). **No overclaim caught** — all three honestly
`partial`. Verdicts routed independently below.

## Independent verification (exact / numeric)
- `f_alt (descending alt-sum) == f_measure (layer-cake M)`: 0 mismatches / 3000. ✓
- **UBI-1** `f(P∪{v}^{2m})=f(P)`: 0 mismatches / 3000 random `(P,v,m)`. ✓
- Worked examples exact: `f({8/3×4,2,4/3,1})=f({2,4/3,1})=5/3`; `f({4,2,1})=3`; `Σ(P*)=15`,
  `f(P*)=5/3`; `n=3` CUT3 witness piece-sums `8,4,2,1`. ✓
- **POS-CHAR**: the `n=2` all-even example `{2,2,1,1,½,½}` has `f=0`; all multiplicities even. ✓
- **Budget `n=2`**: exhaustive incidence search ⇒ min all-even cut count = 3 = `n+1`. ✓
  (`n=3` full brute force times out combinatorially; round-7 certified evidence min=4 stands.)
- **CUT3 arithmetic**: `2^k/2^m=3` impossible (3 not a power of two) — exact. ✓
- **BUDGET-COUNT receiver bound**: distinct-power residual `Σ 2^{k_i}≤2^m−1<2^m` exact; `n=2`
  instance `U=1,R=1,d_1=1,r_1=3≥2`, partial bound `T≥5` vs actual 6. ✓
- **BUDGET-KER**: perturbation argument re-checked by hand — case (i) value→0 drops `N` (even class,
  still all-even), case (ii) merge drops `p`; both contradict minimality. Sound. ✓

---

## 1. self-similar-recursion — VERDICT: CHANGES REQUESTED (Status: partial)
Recorded Status `partial` is CORRECT.

**Progress (real).** Lemma CUT3 (`μ=3` shared even-leaf ≥3 cuts) proven and correct — the donor-cannot-
be-uncut step is a clean power-of-two argument. Corollary is genuinely useful: **Gap B (and, via the
cycle cut-cost floor, Gap A′) is VACUOUS for `N≤2`, so the whole `n=2` lower bound is Gap-free and the
first three induction steps at every `n` are clean.** Honest, correctly-flagged negatives: the assigned
complement-induction is proven insufficient for Gap B (§8, correct — see convergence note), and the
Gap-A′ even-attachment peel is unjustified (M4 permits an odd-block attachment when both cycle-neighbours
are even-blocked — valid observation).

**Gap remaining (name the step).** Gap A′ (a cycle with a degree-`≥3` cycle-piece) and Gap B (`μ=3`
shared even-leaf now confined to budget `3≤N≤n`, so only `n≥3`) are NOT closed. The minimality lever
(Lemma BD / a non-circulation feasible direction) is still unconstructed. CHANGES REQUESTED: close
Gap A′ / Gap B via a genuine minimality argument (NOT the complement peel, NOT the circulation V-kink
— both proven dead).

**Scores.** Correctness 10/10 (CUT3 and all §-imports valid). Rigor 9/10 (residual honestly isolated).
Progress 7/10 (whole `n=2` case closed + budget pinned; core gap still open).

## 2. dual-integer-certificate — VERDICT: CHANGES REQUESTED (Status: partial)
Recorded Status `partial` is CORRECT.

**Progress (real).** Three new Budget-Lemma sub-lemmas proven in full, all correct: BUDGET-A
(self-contained-top induction, base `n=0`), BUDGET-COUNT (reformulation + receiver residual bound
`T≥2(n+1)−R`), BUDGET-KER (Budget-minimal ⇒ `ker U=0`). Each re-derived and verified. The receiver
bound and the `ker U=0` perturbation are genuinely rigorous structural reductions, not heuristics.

**Gap remaining (name the step).** Budget-case (b) (a top-value copy off piece `2^n`, or positive
residual mass on `2^n`) — the "`−R` deficit" in BUDGET-COUNT — is unproven; it is proven `≡ (D′)
|det U★|=1` on the visible reduced subsystem `≡` Gap A′ (Cramer, certified). This is the single shared
wall. CHANGES REQUESTED: close case (b) / `(D′)` via minimality on the visible reduced subsystem.

**Scores.** Correctness 10/10. Rigor 9/10. Progress 7/10 (Budget Lemma cut down to one crisp residual
with three proven sub-lemmas; Positivity now hinges only on case (b)).

## 3. unified-residual-budget-induction — VERDICT: RETHINK (Status: partial for the workspace; the
approach's own finisher is unsolved/dead)
Recorded Status `partial` is accurate for the artifact, but the approach's central mechanism is
proven dead, so the slug routes to RETHINK (re-plan), not CHANGES REQUESTED.

**What is real.** Lemma UBI-1 (measure-form BF-invisibility) is a clean, correct, strictly-more-general
"even blocks are `f`-invisible" statement — verified 0/3000 — and worth caching. CERTIFIED.

**Why RETHINK.** The approach's designed finisher — the unified complement peel with `Claim(N−k)` on
the complement — is PROVEN insufficient by the builder itself: it is an `f`-preserving isomorphism of
difficulty (`min_C f = min_{refinements} f`), logically equivalent to the original residual over a
strictly larger domain, and its all-odd base is outside the reach of `tiefree-minimizer-monochromatic`.
This is correct and honest, but it means the framing cannot finish and must be re-planned by the
outliner — the definition of RETHINK. (The salvaged UBI-1 lives in the shared cache regardless.)

**Scores.** Correctness 10/10 (UBI-1 and the negative both correct). Rigor 9/10. Progress 3/10 (one
reusable lemma + a decisive dead-end map; the slug's own route cannot advance).

---

## Certified this round (6)
`measure-form-bf-invisibility` (UBI-1), `mu3-shared-leaf-cut-cost` (CUT3), `budget-case-a` (BUDGET-A),
`budget-count` (BUDGET-COUNT), `budget-ker` (BUDGET-KER). Total certified ~30. The
complement-induction obstruction is recorded as a do-not-retry NEGATIVE (not a positive lemma).

## Decisive round finding
Two independent approaches PROVE the complement / residual-budget induction is DEAD for the shared
gap (a shared non-power-of-two even block carries a non-dyadic total, so BF-preservation and
`W_m`-landing are mutually exclusive). Genuine obstruction, not bookkeeping — retire the framing.

## Goal Progress (for Eval History)
Status = **partial** (IMPROVED — whole `n=2` case closed (CUT3, Gap A′/B vacuous for `N≤2`); Budget
Lemma reduced to one residual (case b) with 3 proven sub-lemmas; complement-induction PROVEN dead
across 2 approaches; 6 lemmas certified, ~30 total; NO solve, NO overclaim). Ranking snapshot:
self-similar-recursion Elo **1725** (advanced, lead) > dual-integer-certificate **1573** (advanced) >
unified-residual-budget-induction **1524** (dead-end, RETHINK). Sole gap unchanged in essence:
minimality ⇒ benign visible reduced subsystem = Budget-case (b) ≡ `(D′) |det U★|=1` ≡ Gap A′
(deg≥3 cycle-piece). `min f=1` confirmed `n≤4`. Round 9: attack `|det U★|=1` on the visible subsystem
via a genuine minimality/rigidity argument, and seed ≥1 approach from a framing far from the
now-dead complement peel.
