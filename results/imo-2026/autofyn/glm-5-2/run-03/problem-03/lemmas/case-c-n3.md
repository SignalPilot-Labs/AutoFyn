# Lemma: Case C (n=3 very-flat upper-bound closure)

## Status
PROVED (round 5, by `pairing-charging`). Certified round 5 by proof-reviewer (independently re-derived each sub-case; exact-rational sweep 5621 grid configs + 200k random configs, 0 escapes; dyadic vertex v=1/15 exact; corner v=0 exact).

## Statement

> **Theorem 6 (Case C, n=3).** For every Liu config `p_1 ≥ p_2 ≥ p_3 ≥ p_4 ≥ 0`, `Σ p_i = 1`, with `p_2, p_3 < 4/15` and `p_4 > 1/15` (the very-flat regime), Xiang has a `≤ 3`-mark strategy with `D ≤ 1/15`. Moreover, on the OPEN interior (`p_2, p_3 < 4/15` strict, `p_4 > 1/15` strict), the inequality is STRICT: `D < 1/15`; the supremum `1/15` is attained only at the dyadic boundary vertex `(8/15, 4/15, 2/15, 1/15)`, which lies on the `p_2 = 4/15` facet (Case A, closed by `peel-once-inductive`) and the `p_4 = 1/15` facet (spiky, closed by `equal-halve-n-largest`).

## Proof (3-subcase contradiction)

Set `w := p_4`, `z := p_3 − p_4 ≥ 0`, `y := p_2 − p_3 ≥ 0`, `x := p_1 − p_2 ≥ 0`. The construction value `v(p) := min{D_A, D_B, D_C}` is the minimum over the three peels `p_1→p_2`, `p_1→p_4`, `p_2→p_3`, each followed by the certified n=2 menu (§6.3 of `pairing-charging`) on the 3-piece rest (Lemma 3 / `peeling` makes the peel pair parity-neutral, so `D_final = D_rest` exactly).

**Sub-case 1 (`z = p_3 − p_4 < 1/15`): Peel A suffices.** Peel A = `p_1 → p_2`, rest `R_A = {x = p_1−p_2, p_3, p_4}`. Three sort-regimes:
- A1 (`x ≥ p_3 ≥ p_4`): menu member `b−c = p_3−p_4 = z` (Strategy C1: equal-split `a=x`).
- A3 (`p_3 ≥ p_4 ≥ x`): menu member `a−b = p_3−p_4 = z` (Strategy C3: equal-split `c=x`).
- A2 (`p_3 ≥ x ≥ p_4`): `min(a−b, b−c) ≤ z/2 ≤ z` by `min(a−b,b−c) ≤ (a−c)/2 = z/2`.
In every regime `v ≤ z < 1/15`. Total marks: 2 ≤ 3.

**Sub-case 2 (`z ≥ 1/15 ∧ y = p_2 − p_3 < 1/15`): Peel B suffices.** Peel B = `p_1 → p_4`, rest `R_B = {p_1−p_4, p_2, p_3}`. Identical three-regime analysis with `y` in the role of `z`: `v ≤ y < 1/15`. Marks: 2 ≤ 3.

**Sub-case 3 (`z ≥ 1/15 ∧ y ≥ 1/15`): Peel C suffices.** Peel C = `p_2 → p_3`, rest `R_C = {y = p_2−p_3, p_1, p_4}`. `p_1` is always the largest of `R_C` (since `p_1 ≥ p_2 ≥ y` and `p_1 ≥ p_4`), so Strategy C1 (equal-split `a=p_1`, 1 mark) gives the sort-independent member `b−c = |y − p_4|`. Box bounds from Case-C strict constraints: `p_4 ∈ (1/15, 2/15)` (from `p_2 = w+z+y < 4/15` with `z,y ≥ 1/15`) and `y ∈ [1/15, 2/15)` (from `p_2 < 4/15` with `w > 1/15, z ≥ 1/15`). Hence `|y − p_4| < 1/15` strictly. Marks: 2 ≤ 3.

**Exhaustiveness.** The three sub-cases partition `{z,y ≥ 0}`. On the open interior `v < 1/15` strictly.

**Closure.** The boundary facets of `Π_C^{cl}` are: `p_2=4/15` (Case A, Lemma 5), `p_3=4/15` (subsumed by Case A), `p_4=1/15` (spiky, Lemma 4), `p_i=p_{i+1}` (limit of interior, `v ≤ 1/15` by continuity). The supremum `1/15` is attained only at the dyadic vertex `(8/15,4/15,2/15,1/15)` (on the Case-A + spiky facets). ∎

## Usage

This closes the n=3 Case-C (very-flat) regime of the upper bound. Combined with spiky (Lemma 4 / `equal-halve-n-largest`), Case A (`peel-once-inductive`), and Case B (subsumed by Case A), it gives the full n=3 upper bound `c(3) ≤ 8/15`, tight at dyadic. The general-n very-flat residual (n ≥ 4) remains governed by the (unproved) recursive functional `f_n` conjecture.
