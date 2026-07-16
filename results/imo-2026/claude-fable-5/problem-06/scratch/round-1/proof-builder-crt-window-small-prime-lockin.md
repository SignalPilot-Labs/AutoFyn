# Build report — crt-window-small-prime-lockin (imo-2026-06, round 1)

## Outcome
**Status: solved.** Full rigorous, self-contained proof written to
`results/imo-2026-06/approaches/crt-window-small-prime-lockin.md`.

## How the reviewer's two issues were resolved
1. **Lead 3(a) vacuity** — recast statically as required. The static residue of greedy
   minimality is the **Exclusion Principle (Lemma EP, Step 4)**: every integer m > a_1 that is
   not a term has an EARLIER term t < m with gcd(t, m) = 1. This is a genuine fact beyond the
   sorted-V identity (exclusion is always witnessed by an earlier term, never only a later one),
   proved in four lines from greedy minimality. It is exactly the number-theoretic leverage the
   pure clutter setting lacks.
2. **Lead 3(b) sub-hole** — it dissolves: any G ∈ H* with G ∩ X_r = ∅ has G ∩ F_i ⊆ {ρ} and
   G ∩ F_i ≠ ∅, forcing ρ ∈ G. Recorded in the file — but the whole maximal-collection spine
   (3b/3c) and the CRT dodging machinery turned out to be unnecessary and were dropped.

## The new mechanism (closes GAP A, hence GAP 1)
- **Lemma QW (quantitative witness):** for Y ∈ M, ρ ∈ Y, |Y| ≥ 2, and ANY m ≥ a_1 with
  P(m) = Y∖{ρ}: some U ∈ M has U ∩ Y = {ρ} and ∏U < m. (EP applied to m, which is a non-term
  since its type Y∖{ρ} ∉ H*.)
- **Descent (Step 6):** if ρ ≥ a_1·g were in a member, iterate QW with the cheapest realization
  of Y_i∖{ρ}: either c_i = ∏(Y_i∖{ρ}) ≥ a_1 (take m = c_i, get ρ·c_{i+1} < c_i, so c strictly
  drops) or c_i < a_1 (pad with the A-prime s_i ≤ g of Y_i: a realization m < s_i·a_1 ≤ g·a_1 ≤ ρ
  exists, and QW gives ρ < m ≤ ρ — contradiction). Well-ordering kills the infinite descent.
- **Result:** ∪M ⊆ {primes < a_1·g} — finite. Then E = ∪M, L = ∏E, T = |V ∩ [a_1, a_1+L)| give
  a_{n+T} = a_n + L for all n ≥ 1 via the (restated in full) finale.

## Key discovery for the field
**The strict lock-in target of this slug's outline (∪M ⊆ {p ≤ g}) is FALSE.**
Computation: a_1 = 385 = 5·7·11 gives A = {2,7}, g = 14, but {2,11,19} ∈ M with 19 > 14.
The round-1 empirical claim "∪M ⊆ {p ≤ g} in all tests" was an artifact of small seeds. The
proof therefore establishes the weakened (and sufficient) bound ρ < a_1·g. This also matters for
the rival approaches: any route aiming at the strict bound is dead.

## Numerical verification performed (checks, not proof steps)
- EP verified exhaustively on the term ranges of seeds 15, 35, 77, 143, 202, 221, 303, 309, 385,
  899, 1001 — no failures.
- Full conclusion verified from n = 1: a_1 = 385: (T, L) = (5088, 43890), 15278 terms;
  a_1 = 899: (T, L) = (4778, 188790), 14339 terms; plus the reviewer's earlier seeds.

## Promotable lemmas (proposed for lemmas/, reviewer to certify)
1. `exclusion-principle` — Lemma EP (Step 4 of my file).
2. `quantitative-witness` — Lemma QW (Step 5).
3. `essential-prime-bound` — Step 6 theorem (∪M ⊆ {p < a_1·g}); note this makes the crux of
   valid-set-sunflower-core (GAP 1) and self-blocking-clutter-induction (GAP B) unconditional —
   though as a pure clutter statement GAP B may still be false; EP is sequence-specific.
4. Steps 1–3, 8 restate the shared foundation (terms-equal-valid-set, realization,
   finite-core-implies-periodicity) so the file is standalone; certification can source from
   either file.

## Spec concerns
None.
