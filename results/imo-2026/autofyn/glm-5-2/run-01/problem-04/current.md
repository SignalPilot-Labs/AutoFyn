# imo-2026-04 — current

## Status
solved

## Approaches tried
- (round 1) direct-four-case-interval — APPROVED by proof-reviewer. Complete,
  rigorous characterization both directions. Necessity via four-case closure of
  the `B_θ`-free safe set + equilateral witness; sufficiency via Lemma R
  (`mθ → (m−1)θ` induction, `≤ m−1` moves) + Lemma F (interval of length
  `C/θ > 1` contains an integer) + `n=2` special move. All four telescoping
  identities and the strategy verified symbolically and by simulation
  (`n=2,3,4,5`, 2000 random triangles each, worst-case Shan-Yu, 0 failures;
  non-integer `180/θ` escape survives 500 rounds × 9 θ values). Headline proof.
- (round 1) attractor-level-fixpoint — APPROVED by proof-reviewer. Same
  engine as `direct-four-case-interval` (Lemma R + Lemma F + four-case closure
  + `n=2` base), framed as a least-fixed-point attractor recursion. The
  distinctive §5 "determinacy / no-draw dichotomy" is correct but redundant —
  it is a restatement of the exhaustive `180/θ ∈ ℤ` vs `∉ ℤ` partition plus the
  two proven implications, not a new theorem. No gap introduced. Equivalent in
  substance to the headline proof.
- (round 1) chip-transfer-monovariant — CHANGES REQUESTED (partial). The
  `q`-space necessity (Theorem N = four-case closure in residue language) is
  rigorous and correct; Lemma FRAC (fractional-part 3-cycle of the forced
  `t=1` transfer) is a genuine proven micro-invariant. Sufficiency is honestly
  conceded: the bare transfer monovariant is a verified dead-end (greedy `t=1`
  cycles), and smart `t=1` play's descent *is* Lemma R, not a new potential.
  Minor labeling error in the dead-end illustration (the `q=(3,2,3)` fixed
  point comes from cutting index 0, not index 2 as written; the conclusion
  stands). Effectively a `q`-space cross-check of the direct proof.

## Current best
The complete characterization, both directions, proven in full (see Full
proof). Answer: **Mulan wins in finitely many steps iff `180°/θ ∈ ℤ`, i.e.
`θ = 180°/n` for an integer `n ≥ 2`** (`{90°, 60°, 45°, 36°, 30°, …}`).

Key established tools (certified in `lemmas/`):
- `four-case-closure.md` — `S_θ` is Shan-Yu-closed when `180°/θ ∉ ℤ`.
- `lemma-R-multiple-descent.md` — `mθ`-angle ⇒ Mulan wins in `≤ m−1` moves.
- `lemma-F-reach-multiple.md` — generic triangle ⇒ one move to a `B_θ`-angle
  in both children (`n ≥ 3`).
- `interval-contains-integer.md` — open interval of length `> 1` contains an
  integer.
- `lemma-FRAC.md` — fractional-part 3-cycle of the forced `t=1` transfer
  (cross-check invariant; does not by itself prove the escape).

## Full proof

> **Theorem.** For `0° < θ < 180°`, Mulan can guarantee victory in finitely many
> steps (regardless of how Shan-Yu plays) **if and only if** `180°/θ` is an
> integer. Since `θ < 180°`, an integer value of `180°/θ` is automatically
> `≥ 2`; equivalently the winning angles are exactly
> `{180°/n : n = 2, 3, 4, …} = {90°, 60°, 45°, 36°, 30°, …}`.

Write angles in degrees. A *triangle* is a triple `(A,B,C)` of positive reals
with `A+B+C = 180°`. Define the **bad-angle set**
`B_θ = {kθ : k ∈ ℤ_{≥1}, 0 < kθ < 180°}` (strict upper bound: an angle of a
triangle is strictly less than `180°`, so `180° ∉ B_θ`). Note `θ = 1·θ ∈ B_θ`
always (as `0° < θ < 180°`).

### 0. The one-move transition

Let the current triangle have vertices `X, Y, Z` with angles `A = ∠X`, `B = ∠Y`,
`C = ∠Z`. Mulan picks a point `P` on side `XY` (the side opposite `Z`,
`P ≠ X, Y`) and cuts from `P` to `Z`. Let `γ = ∠XZP ∈ (0, C)` be the piece of
`C` adjacent to `X` (so the complementary piece is `C − γ`). Because `P` lies
on segment `XY`, the two angles at `P` are supplementary
(`∠XPZ + ∠ZPY = 180°`). The two children are

```
T1 = △XPZ  with angles  (A, γ, 180° − A − γ),
T2 = △YPZ  with angles  (B, C − γ, A + γ).
```
Write `p1 = 180° − A − γ` (angle of `T1` at `P`), `p2 = A + γ` (angle of `T2`
at `P`). Both sums are `180°`, and
```
p1 + p2 = (180° − A − γ) + (A + γ) = 180°.        (supplementary P-angles)
```
A move is: pick a vertex to split (`Z` above; the others are identical up to
relabeling) and `γ ∈ (0, C)`. The four *new* angles are `γ, p1, C−γ, p2`;
`A` (in `T1`) and `B` (in `T2`) are inherited; `C` does not survive whole.
Mulan wins *in one move* iff **both** children contain a multiple of `θ`
(whichever child Shan-Yu keeps, the next check fires).

### I. Necessity: `180°/θ ∉ ℤ` ⇒ Shan-Yu escapes

Define the **safe set** `S_θ = {(A,B,C) : no angle lies in B_θ}`. A safe
triangle contains no `θ`.

**Lemma (four-case closure).** *If `(A,B,C) ∈ S_θ` and `180°/θ ∉ ℤ`, then for
every Mulan cut at the `C`-vertex with `γ ∈ (0,C)`, at least one child lies in
`S_θ`.*

*Proof.* Suppose both children leave `S_θ`. `T1 = (A, γ, p1)` has a `B_θ`-angle;
since `A ∉ B_θ`, it is `γ` or `p1`. `T2 = (B, C−γ, p2)` has a `B_θ`-angle;
since `B ∉ B_θ`, it is `C−γ` or `p2`. Four disjoint exhaustive cases (the
choice for `T1` crossed with the choice for `T2`):

- **(i)** `γ = k₁θ`, `C−γ = k₂θ`. Adding, `C = (k₁+k₂)θ`. `0 < C < 180°` and
  `k₁+k₂ ≥ 1` give `C ∈ B_θ`, contradicting `C ∉ B_θ`.
- **(ii)** `γ = k₁θ`, `p2 = A+γ = k₂θ`. `A = (k₂−k₁)θ`; `A > 0 ⇒ k₂ > k₁ ⇒ k₂−k₁ ≥ 1`;
  `A < 180° ⇒ A ∈ B_θ`, contradicting `A ∉ B_θ`.
- **(iii)** `p1 = k₁θ`, `C−γ = k₂θ`. `p1 − (C−γ) = 180°−A−C = B = (k₁−k₂)θ`;
  `B > 0 ⇒ k₁ > k₂ ⇒ k₁−k₂ ≥ 1`; `B < 180° ⇒ B ∈ B_θ`, contradicting `B ∉ B_θ`.
- **(iv)** `p1 = k₁θ`, `p2 = k₂θ`. Adding, `p1+p2 = 180° = (k₁+k₂)θ`, so
  `180°/θ = k₁+k₂ ∈ ℤ`, contradicting the hypothesis.

Each case contradicts; the four cases exhaust "both children leave `S_θ`" (the
choice of bad angle in each child is binary). ∎

(The four linear combinations of `γ` telescope to `C, A, B, 180°`
respectively — verified by direct simplification.)

**Lemma (equilateral is safe).** *If `180°/θ ∉ ℤ`, then `(60°,60°,60°) ∈ S_θ`.*

*Proof.* If `60° = kθ` (`k ≥ 1`), then `θ = 60°/k` and `180°/θ = 3k ∈ ℤ`,
contradiction. So `60° ∉ B_θ`, and all three equilateral angles avoid `B_θ`. ∎

**Shan-Yu's escape.** Shan-Yu opens with the equilateral `(60°,60°,60°) ∈ S_θ`
(valid, and Shan-Yu chooses the initial triangle). Inductively suppose the
current `T ∈ S_θ`. Mulan cuts; by closure at least one child lies in `S_θ`;
Shan-Yu keeps that child. The kept triangle is always in `S_θ`, hence never
contains `θ` (as `θ ∈ B_θ`). The stopping condition never fires; Mulan does not
win in any finite number of steps. (Invariant argument.) This works uniformly
for every `θ` with `180°/θ ∉ ℤ` — irrational or rational non-integer — since
the closure is purely algebraic. ∎

### II. Sufficiency: `180°/θ = n ∈ ℤ`, `n ≥ 2` ⇒ Mulan wins in `≤ n−1` moves

Now `θ = 180°/n`, `B_θ = {θ, 2θ, …, (n−1)θ}`.

**Lemma R (descent of the multiple index).** *If `T` has an angle `mθ` at a
vertex, `1 ≤ m ≤ n−1`, Mulan wins in `≤ m−1` moves.*

*Proof by induction on `m`.* Base `m=1`: `T` contains `θ`, game stops, `0`
moves. Step `m ≥ 2`: relabel so `C = mθ`, `A+B = 180°−mθ`. Mulan cuts at `C`
with `γ = θ` (legal: `θ < mθ` since `m ≥ 2`). Children
`T1 = (A, θ, 180°−A−θ)` (contains `θ` — win in `1` move if kept) and
`T2 = (B, (m−1)θ, A+θ)` (contains `(m−1)θ` at vertex `C`). `T2` is a valid
triangle: `B > 0`, `(m−1)θ > 0`, `A+θ > 0`; and `A+θ < 180°` since
`A < 180°−mθ` (as `B > 0`) gives `A+θ < 180°−(m−1)θ ≤ 180°−θ < 180°`. By the
induction hypothesis on `T2` (index `m−1`, `1 ≤ m−1 ≤ n−2`), if Shan-Yu keeps
`T2` Mulan wins in `≤ m−2` further moves, `≤ m−1` total. Either choice of
Shan-Yu gives `≤ m−1` moves. (The positivity bound re-establishes at each
induction level.) ∎

**Lemma F (reach a multiple from a `B_θ`-free triangle, `n ≥ 3`).** *Let `T =
(A,B,C)` be `B_θ`-free. Mulan makes one move after which both children carry a
`B_θ`-angle.*

*Proof.* Relabel so `C` is largest: `C ≥ 60°`. Since `n ≥ 3`, `θ ≤ 60°`, so
`C ≥ θ`; `C ≠ θ` (`T` `B_θ`-free, `θ ∈ B_θ`), so `C > θ`, i.e. `C/θ > 1`. The
open interval `I = (A/θ, (A+C)/θ)` has length `C/θ > 1`. By the
*interval-contains-integer* fact, pick an integer `k` with
`A/θ < k < (A+C)/θ`. Set `γ = kθ − A`: `γ > 0` (`k > A/θ`) and `γ < C`
(`kθ < A+C`). So `γ ∈ (0, C)`. Mulan cuts at `C`. Then
`p2 = A+γ = kθ`, `p1 = 180°−A−γ = 180°−kθ = (n−k)θ`. Bounds: `k ≥ 1` (as
`k > A/θ > 0`) and `k ≤ n−1` (as `k < (A+C)/θ = n − B/θ < n`). So
`k, n−k ∈ {1,…,n−1}`; both `p1 = (n−k)θ` and `p2 = kθ` lie in `B_θ`. Both
children carry a `B_θ`-angle. ∎

**Base `n = 2` (`θ = 90°`).** `B_θ = {90°}`. If `T` already has `90°`, win in
`0` moves. Otherwise `T` is non-right; relabel `C` largest. At most one angle
`≥ 90°` (two would sum to `≥ 180°`), and it is the largest, so `A, B < 90°`
(covers acute and obtuse openings). Mulan cuts at `C` with `γ = 90° − A`
(legal: `γ > 0` since `A < 90°`; `γ < C` iff `90° < A+C = 180°−B` iff
`B < 90°`, which holds). Then `p2 = A+γ = 90°`, `p1 = 180°−A−γ = 90°`. Both
`P`-angles equal `90° = θ`; both children contain `θ`. Win in `1 = n−1` move. ∎

**Combine (`n ≥ 3`).** Let `T` be any opening.
- `T` already contains `θ`: `0` moves.
- `T` `B_θ`-free but contains `mθ` (`2 ≤ m ≤ n−1`): Lemma R, `≤ m−1 ≤ n−2 ≤ n−1` moves.
- `T` `B_θ`-free and contains no `B_θ`-angle: Lemma F (one move → both children
  carry `m'θ`, `1 ≤ m' ≤ n−1`), then Lemma R (`≤ m'−1 ≤ n−2` further); total
  `≤ 1 + (n−2) = n−1` moves.

These three cases are disjoint and exhaustive. In every case Mulan wins in at
most `n−1` moves, regardless of Shan-Yu. For `n = 2` this is the special move
(`≤ 1` move). The bound is finite. ∎

### III. The characterization

- (**Necessity**, §I) If `180°/θ ∉ ℤ`, Shan-Yu opens the equilateral and
  maintains `B_θ`-freeness forever (four-case closure); Mulan never wins.
- (**Sufficiency**, §II) If `180°/θ = n ∈ ℤ` (`n ≥ 2`), Mulan wins from every
  opening in at most `n−1` moves, regardless of Shan-Yu.

The two cases partition all `θ ∈ (0°, 180°)`. Therefore

```
Mulan guarantees victory in finitely many steps  ⇔  180°/θ ∈ ℤ,
```
i.e. `θ ∈ {180°/n : n = 2, 3, 4, …} = {90°, 60°, 45°, 36°, 30°, …}`.

**Tightness (both directions).**
- *Attainment.* For each integer `n ≥ 2`, `θ = 180°/n` makes Mulan win (§II), so
  every advertised value is a genuine winning angle.
- *Upper bound.* For every `θ` with `180°/θ ∉ ℤ` (all `θ > 90°`, and all
  `θ < 90°` with non-integer `180°/θ`), §I exhibits an explicit Shan-Yu
  strategy (equilateral opening, keep a `B_θ`-free child) preventing Mulan
  from ever winning.

Both halves are constructive (explicit strategies for both players), so there
is no "neither-can-force" middle ground. ∎

*Proof taken from `direct-four-case-interval` (round 1), APPROVED; the
`attractor-level-fixpoint` approach establishes the same proof with an
equivalent fixed-point framing.*
