# Build report — circle-group-quotient (imo-2026-04), round 1

## Status: solved

Full proof written to `results/imo-2026-04/approaches/circle-group-quotient.md`.
**Answer: Mulan wins iff θ = 180°/n, n ∈ ℤ, n ≥ 2 (iff 180/θ ∈ ℤ); when she wins, within ≤ n − 1 cuts.**

## What was built

Layered structure per the approach's contract (reviewer's condition):
- **Lemma 0 (cut model):** legal move ⟺ (attacked vertex, t ∈ (0, attacked angle)); children (P, t, Q+R−t) / (Q, R−t, P+t); realizability of every t via the Crossbar Theorem; nondegeneracy of children.
- **Sections 1–2 (algebra in G = ℝ/θℤ, no sizes):** sum invariant σ = [180]; Lemma 2A (σ ≠ 0 ⟹ "clean" is Shan-Yu-closed — four-case intersection, written once with the relabeling symmetry stated); Lemma 2B (σ = 0 ⟹ class −[P] forks both children into [0]), explicitly deferring legality of a representative to the lifts.
- **Section 3 (necessity):** clean initial triangle (ε, ε, 180−2ε), ε from an interval minus a finite excluded set; maintenance by Lemma 2A; game never stops.
- **Section 4 (sufficiency, sizes only):** Lemma 4.1 (Lift 1: unique representative t₀ ∈ (0, θ), strict); Lemma 4.2 (Lift 2 / L2: angle = kθ ⟹ win in ≤ k−1 cuts, full strong induction with legality 0 < θ < kθ); Lemma 4.3 (main fork, n ≥ 3: t₀ < θ ≤ 60 ≤ R legality chain, both children get an exact multiple); Lemma 4.4 (L1: θ = 90 one-move universal win, t = 90 − P, both legality inequalities proven — n = 2 routed entirely here per the outline-reviewer, no fork patch). Assembly: exhaustive disjoint cases, bound n − 1 in every branch.

## Former gaps — all closed
Lift 1 boundary bookkeeping (incl. equilateral, n = 2), Lift 2 induction, Step 2 enumeration/symmetry. `## Spec concerns` in the approach file records the closures; no GAPs remain.

## Independent verification (not a proof step)
Exact-Fraction implementation of the strategy *verbatim* (fork with t₀ = (−P) mod θ on the largest angle; Lemma 4.2 chain following the chosen kθ; Lemma 4.4 for n = 2): n = 2, 3, 4, 5, 6, 9, 12, 18, ~250–330 starts each including equilateral, (1,2,177), and states pre-loaded with two exact multiples — worst-case cuts ≤ n − 1 everywhere, zero legality failures. One checker artifact worth recording: cutting an *arbitrary* multiple (instead of following the induction's chosen angle) can cycle (kθ and mθ can regenerate each other via A + θ); the proof avoids this because Lemma 4.2's induction is on the k of the chosen angle, which strictly decreases.

## Promotable lemmas (for the proof-reviewer to certify into lemmas/)
- **L1** = Lemma 4.4 (θ = 90 one-move universal win).
- **L2** = Lemma 4.2 (exact multiple kθ finishes in ≤ k − 1 cuts).
- **L0** = Lemma 0 (cut model bijection) — shared move model usable by every approach.
