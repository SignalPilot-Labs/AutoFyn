# attractor-level-fixpoint

Target: the full characterization of `θ ∈ (0°,180°)` for which Mulan guarantees
victory in finitely many steps in the Shan-Yu / Mulan paper-triangle game.
Answer conjecture: `θ = 180°/n` for an integer `n ≥ 2`.

Technique: attractor / winning-region least-fixed-point recursion on the
angle-triple state space, packaged as a game-theoretic **constructive determinacy
(no-draw) dichotomy** with an explicit finite move bound. The sufficiency engine
(Lemma R multiple-descent + Lemma F interval-contains-integer) and the necessity
engine (four-case closure of the `B_θ`-free region) are proved in full below
(no certified lemmas existed in `results/imo-2026-04/lemmas/` at build time, so
they are established here from scratch). The DISTINCTIVE contribution of this
approach is the **determinacy / no-draw clause** for the uncountable angle-triple
state space: a constructive disjunction proving that for every `θ` exactly one
player has an explicit winning strategy, so no `θ` yields an infinite draw —
established without any transfinite reachability-game theorem.

## Status
solved

## Approaches tried
- (round 1) attractor-level-fixpoint — APPROVED by outline-reviewer; distinctive
  hard gap is the determinacy argument. Built: full proof below, including the
  no-draw dichotomy (constructive), Lemma R, Lemma F, four-case closure, and
  exhaustive case coverage (`n=2`, `n≥3`, `θ>90°`, irrational and
  rational-non-`1/n` `180/θ`). All gaps closed.

## Current best
The full characterization: Mulan guarantees victory in finitely many steps **iff**
`180°/θ ∈ ℤ`, i.e. `θ = 180°/n` for an integer `n ≥ 2`. Both directions proved;
the no-draw dichotomy proved constructively. Explicit finite bound in the winning
case: `≤ n−1` Mulan moves.

## Full proof

### 0. Setup and the one-move transition (geometry)

Write the state as the open 2-simplex
`X = {(A,B,C) : A,B,C > 0, A+B+C = 180°}`, the set of all angle triples of valid
(positivity) triangles. A move: Mulan picks a vertex, call it the vertex with
angle `C`, and a point `P` on the opposite side (the side joining the other two
vertices, those bearing angles `A` and `B`). Let
`γ = ∠(vertex with angle A, vertex with angle C, P) ∈ (0, C)` be the piece of
`C` adjacent to `A` (so `C − γ` is adjacent to `B`). The cut `CP` produces two
triangles:

- `T₁ = (A, γ, 180 − A − γ)` — the piece at the `A`-vertex;
- `T₂ = (B, C − γ, A + γ)` — the piece at the `B`-vertex.

Both sums equal `180` (for `T₂`: `B + (C−γ) + (A+γ) = A+B+C = 180`). The two new
angles at `P` are `p₁ := 180 − A − γ` (in `T₁`) and `p₂ := A + γ` (in `T₂`), and

  **`p₁ + p₂ = 180`** (supplementary).

This supplementary identity is the single load-bearing geometric fact (angles at
a point on a straight line are supplementary); it is the only geometry used.
Shan-Yu then discards one child; the kept child is the new `T`. Mulan's move is
fully specified by the choice of split vertex and `γ ∈ (0, C)`. Mulan's
one-move forced win requires **both** children to be in her winning region,
because Shan-Yu is free to keep either.

We invoke no named geometric theorem beyond "angles at a point on a line are
supplementary" and "angle sum of a triangle is `180°`."

### 1. The attractor (least fixed point)

Define `W₀ = {T ∈ X : some angle of T equals θ}` (Mulan's immediate-win region;
the game stops before she moves). Recursively,
```
W_{k+1} = W_k ∪ { T ∈ X : ∃ a Mulan cut of T such that both children lie in W_k }.
```
Set `W = ⋃_{k≥0} W_k`. This is the least fixed point of the "Mulan can force a
win in `≤ k` moves" operator.

**Claim (attractor = finite-win region).** `T ∈ W_k` iff Mulan can force a win
from `T` in `≤ k` moves, regardless of Shan-Yu's play.

*Proof by induction on `k` (Induction, KB "General Proof Methods").* Base `k=0`:
`T ∈ W₀` iff `T` has angle `θ` iff the game stops immediately, a `0`-move win.
Step: `T ∈ W_{k+1}` iff `T ∈ W_k` (win in `≤ k ≤ k+1` moves) or `T` has a cut
with both children in `W_k`. In the latter case Mulan plays that cut; whichever
child Shan-Yu keeps is in `W_k`, so by induction Mulan then wins in `≤ k` more
moves, total `≤ k+1`. Conversely, if Mulan can force a win in `≤ k+1` moves from
`T`: either she wins in `0` moves (`T ∈ W₀ ⊆ W_{k+1}`), or her first move is a
cut after which, **no matter which child Shan-Yu keeps**, she wins in `≤ k` more
moves — i.e. both children are `≤ k`-move wins, i.e. both children lie in `W_k`
(by induction). Hence `T ∈ W_{k+1}`. ∎ (induction complete)

So `W = {T : Mulan can force a win in finitely many steps from T}`, and "in
finitely many steps" means precisely `T ∈ W_k` for some finite `k`.

### 2. The safe region `S_θ` and the four-case closure

Define `B_θ = {kθ : k ∈ ℤ_{≥1}, 0 < kθ < 180°}` (positive multiples of `θ`
strictly below `180°`; note `180° ∉ B_θ`). Define the **safe region**
`S_θ = {(A,B,C) ∈ X : no angle of the triple lies in B_θ}`.

**Lemma (four-case closure).** *If `180/θ ∉ ℤ`, then `S_θ` is Shan-Yu-closed:
for every `T = (A,B,C) ∈ S_θ` and every Mulan cut at the `C`-vertex with
`γ ∈ (0,C)`, at least one of the two children lies in `S_θ`.*

*Proof.* Suppose both children leave `S_θ` (each acquires a `B_θ`-angle). Child
`T₁ = (A, γ, p₁)` has a `B_θ`-angle among `{A, γ, p₁}`; but `A ∉ B_θ` (parent
in `S_θ`), so it is `γ` or `p₁`. Child `T₂ = (B, C−γ, p₂)` has a `B_θ`-angle
among `{B, C−γ, p₂}`; but `B ∉ B_θ`, so it is `C−γ` or `p₂`. This gives four
exhaustive combinations (disjointness is not required, only exhaustiveness):

- **(i) `γ ∈ B_θ` and `C−γ ∈ B_θ`.** Write `γ = k₁θ`, `C−γ = k₂θ` with
  `k₁,k₂ ≥ 1`. Then `C = γ + (C−γ) = (k₁+k₂)θ`. Since `C ∈ (0,180)`, this is
  `C ∈ B_θ`, contradicting `(A,B,C) ∈ S_θ`.
- **(ii) `γ ∈ B_θ` and `p₂ ∈ B_θ`.** `γ = k₁θ`, `p₂ = A+γ = k₂θ`. Then
  `A = p₂ − γ = (k₂−k₁)θ`. Since `A > 0`, `k₂ − k₁ ≥ 1`, so `A ∈ B_θ`,
  contradicting `S_θ`.
- **(iii) `p₁ ∈ B_θ` and `C−γ ∈ B_θ`.** `p₁ = 180−A−γ = k₁θ`, `C−γ = k₂θ`.
  Subtract: `p₁ − (C−γ) = (180−A−γ) − (C−γ) = 180 − A − C = B` (using
  `A+B+C=180`). So `B = (k₁−k₂)θ`. Since `B > 0`, `k₁ − k₂ ≥ 1`, so
  `B ∈ B_θ`, contradicting `S_θ`.
- **(iv) `p₁ ∈ B_θ` and `p₂ ∈ B_θ`.** `p₁ = k₁θ`, `p₂ = k₂θ`. Adding:
  `p₁ + p₂ = 180 = (k₁+k₂)θ`. Hence `180/θ = k₁+k₂ ∈ ℤ`, contradicting the
  hypothesis `180/θ ∉ ℤ`.

The four cases exhaust "both children leave `S_θ`" (the choice of `B_θ`-angle in
each child is binary), and each leads to a contradiction. Hence at least one child
remains in `S_θ`. ∎

(Invariants & monovariants, KB — `S_θ` is an invariant region preserved by
Shan-Yu's "keep a safe child" response.)

**Lemma (non-emptiness of `S_θ` when `180/θ ∉ ℤ`).** *If `180/θ ∉ ℤ`, the
equilateral `(60°,60°,60°)` lies in `S_θ`.*

*Proof.* If `60 = kθ` for some `k ≥ 1` with `0 < 60 < 180`, then
`θ = 60/k` and `180/θ = 3k ∈ ℤ`, contradiction. So `60 ∉ B_θ`, and all three
angles of the equilateral avoid `B_θ`. ∎

(In particular this covers `θ > 90°`: then `180/θ ∈ (1,2) ∉ ℤ`, and `60 < θ`,
so `60 ≠ kθ` for `k ≥ 1` trivially — `B_θ ⊂ (θ,180)`, all of whose elements
exceed `60`, so the equilateral is safe.)

### 3. Sufficiency: `180/θ = n ∈ ℤ, n ≥ 2` ⟹ `W_{n−1} = X` (Mulan wins in `≤ n−1` moves)

Fix `n = 180/θ ∈ {2,3,4,…}` so `θ = 180/n` and `B_θ = {θ, 2θ, …, (n−1)θ}`.

**Lemma R (multiple descent).** *If a triangle `T` has an angle equal to `mθ`
for an integer `m ≥ 1` (with `mθ < 180`), then `T ∈ W_{m−1}`. In particular
(Mulan's strategy) she cuts that `mθ`-angle at `γ = θ` (valid for `m ≥ 2` since
`θ < mθ`), producing a child carrying `θ` and a child carrying `(m−1)θ`.*

*Proof by induction on `m` (Induction, KB).*
- Base `m = 1`: `T` has angle `θ`, so `T ∈ W₀`. ✓
- Step `m ≥ 2`: split the `mθ`-angle (at vertex `C`, say `C = mθ`) with
  `γ = θ ∈ (0, mθ)` (strict, since `m ≥ 2`). Children:
  `T₁ = (A, θ, 180−A−θ)` — carries `θ` at vertex `C`, so `T₁ ∈ W₀ ⊆ W_{m−2}`
  (since `m ≥ 2 ⟹ m−2 ≥ 0`); `T₂ = (B, (m−1)θ, A+θ)` — carries `(m−1)θ` at
  vertex `C`, so by the induction hypothesis `T₂ ∈ W_{(m−1)−1} = W_{m−2}`.
  Both children lie in `W_{m−2}`, hence `T ∈ W_{m−1}`.

  Positivity of `T₂` (all angles `> 0`, so it is a valid triangle): `B > 0` and
  `(m−1)θ > 0` are clear. For the third angle `A+θ`: since `A + B = 180 − mθ`
  (from `A+B+C = 180`, `C = mθ`) and `B > 0`, we have `A < 180 − mθ`, hence
  `A + θ < 180 − (m−1)θ ≤ 180 − θ < 180` (for `m ≥ 2`, `(m−1)θ ≥ θ`), so
  `A+θ ∈ (0,180)` and in particular `> 0`. The sum
  `B + (m−1)θ + (A+θ) = A+B+mθ = 180` is correct. So `T₂` is a valid triangle,
  and the induction applies recursively: at each step the
  (now-smaller) multiple sits at vertex `C` of the kept child (either inherited
  or a `P`-angle, in both cases a vertex angle, hence splittable), and the same
  positivity bound holds at every level (the "third angle" at level `j` is
  bounded above by `180 − jθ`, so adding `θ` keeps it `< 180` while the
  descending index keeps it `> 0`). ∎

**Lemma F (reach a multiple from anywhere, `n ≥ 3`).** *Let `n = 180/θ ≥ 3` be an
integer. From a triangle `T = (A,B,C)` with **no** `B_θ`-angle, Mulan splits the
**largest** angle `C` and finds `γ ∈ (0,C)` such that both `P`-angles `p₁, p₂`
lie in `B_θ`. Consequently both children carry a `B_θ`-angle and (by Lemma R) lie
in `W_{n−2}`, so `T ∈ W_{n−1}`.*

*Proof.* Since `C` is the largest angle of a triangle, `C ≥ 60°`. Since
`n ≥ 3`, `θ = 180/n ≤ 60°`. Hence `C ≥ θ`. If `C = θ` then `C ∈ B_θ`,
contradicting the hypothesis that `T` has no `B_θ`-angle; so `C > θ`, i.e.
`C/θ > 1`. The open interval `(A/θ, (A+C)/θ)` has length `C/θ > 1`.

**Interval fact (Pigeonhole / extremal, KB).** *An open interval of length `> 1`
contains an integer.* Proof: let the interval be `(x, x+L)`, `L > 1`. If
`x ∉ ℤ`, take `k = ⌈x⌉`: then `k > x` and `k ≤ x + 1 < x + L`, so
`k ∈ (x, x+L)`. If `x ∈ ℤ`, take `k = x + 1 ∈ (x, x+L)` since `L > 1`. ∎

Apply the interval fact to `(A/θ, (A+C)/θ)`: there is an integer `k` with
`A/θ < k < (A+C)/θ` strictly. Set `γ = kθ − A`. Then:
- `0 < γ` (from `k > A/θ`, i.e. `kθ > A`) and `γ < C` (from
  `k < (A+C)/θ`, i.e. `kθ < A + C`); so `γ ∈ (0, C)` strictly — the cut is
  non-degenerate, `P` is not a vertex. ✓
- `p₂ = A + γ = kθ`, a multiple of `θ`.
- `p₁ = 180 − A − γ = 180 − kθ = (n − k)θ` (using `180 = nθ`), a multiple of
  `θ`.
- **Range of `k`:** `k > A/θ > 0` (since `A > 0`) gives `k ≥ 1`. And
  `k < (A+C)/θ = (180 − B)/θ = n − B/θ < n` (since `B > 0`) gives `k ≤ n−1`.
  So `k ∈ {1, …, n−1}` and likewise `n − k ∈ {1, …, n−1}`. Hence
  `p₂ = kθ ∈ B_θ` and `p₁ = (n−k)θ ∈ B_θ` (both are positive multiples of `θ`
  strictly below `180°`, since `k, n−k ≤ n−1`).

So child `T₁ = (A, γ, p₁)` carries `p₁ ∈ B_θ` (multiple-index `n − k`), and
child `T₂ = (B, C−γ, p₂)` carries `p₂ ∈ B_θ` (multiple-index `k`). By Lemma R,
`T₁ ∈ W_{(n−k)−1} ⊆ W_{n−2}` (since `n−k ≤ n−1` ⟹ `(n−k)−1 ≤ n−2`) and
`T₂ ∈ W_{k−1} ⊆ W_{n−2}` (since `k ≤ n−1` ⟹ `k−1 ≤ n−2`). Both children lie in
`W_{n−2}`, so `T ∈ W_{n−1}`. ∎

**Base case `n = 2` (`θ = 90°`, special move).** Here `B_θ = {90°}`. A right
triangle already has a `90°` angle, so `T ∈ W₀`. For a non-right triangle `T`,
split its largest angle `C`. We claim both other angles `A, B` are `< 90°`:
- if `T` is acute, all angles `< 90°`, so `A, B < 90°`;
- if `T` is obtuse, the obtuse angle is the largest (`C > 90°`), and
  `A + B = 180 − C < 90°`, so `A, B < 90°`.

(At most one angle can be `≥ 90°`; it is the largest. Triangle fact.) Set
`γ = 90 − A`. Then `γ > 0` (since `A < 90°`) and `γ < C` because
`90 − A < C ⟺ 90 < A + C = 180 − B ⟺ B < 90°`, which holds. So
`γ ∈ (0, C)`. Now `p₁ = 180 − A − γ = 180 − A − (90 − A) = 90` and
`p₂ = A + γ = A + (90 − A) = 90`. Both `P`-angles equal `90° = θ`, so both
children contain `θ`, i.e. both children lie in `W₀`, and `T ∈ W₁`. ✓
The bound `n − 1 = 1` matches.

**Combine (sufficiency).** For `n = 2`: right triangles are in `W₀`, non-right
triangles are in `W₁`; so `W₁ = X`. For `n ≥ 3`: a triple either carries a
`B_θ`-angle `mθ` (`1 ≤ m ≤ n−1`), in which case Lemma R gives
`T ∈ W_{m−1} ⊆ W_{n−2} ⊆ W_{n−1}`; or it carries no `B_θ`-angle, in which case
Lemma F gives `T ∈ W_{n−1}` directly. Hence `W_{n−1} = X`: from **every** opening,
Mulan forces a win in `≤ n − 1` moves, a finite bound. ∎

### 4. Necessity: `180/θ ∉ ℤ` ⟹ Shan-Yu escapes (Mulan cannot guarantee a finite win)

Assume `180/θ ∉ ℤ`. By the non-emptiness lemma, the equilateral
`E = (60°,60°,60°)` lies in `S_θ`. Shan-Yu opens with `E`. After every Mulan cut,
by the four-case closure lemma, at least one of the two children lies in `S_θ`;
Shan-Yu keeps such a child. Inductively the state `T` lies in `S_θ` after every
move. Since `θ = 1·θ ∈ B_θ` (as `0 < θ < 180°`), membership in `S_θ` means in
particular that no angle of `T` equals `θ`, so the stopping condition never
fires and the game never ends. Mulan does not win in finitely many steps.

Formally, `S_θ` is disjoint from `W`: indeed `W₀ ∩ S_θ = ∅` (since
`θ ∈ B_θ`), and inductively if `W_k ∩ S_θ = ∅` then `W_{k+1} ∩ S_θ = ∅`, because
a state of `S_θ` cannot have a cut sending both children into `W_k ⊆ X \ S_θ`
(that would mean both children leave `S_θ`, contradicting closure). Hence
`S_θ ∩ W = ∅`. In particular `E ∉ W`: there is an opening from which Mulan
cannot force a finite win, so Mulan does not guarantee victory. ∎

### 5. Determinacy / no-draw clause (DISTINCTIVE contribution)

A natural worry for an uncountable-state reachability game is whether some `θ`
admits **neither** a finite Mulan win **nor** a perpetual Shan-Yu escape — an
infinite draw with no winning strategy for either player. We resolve this
**constructively**, with no transfinite reachability-game determinacy theorem
(such as Martin's theorem on Borel games) invoked:

**Dichotomy (constructive, no draw).** *For every `θ ∈ (0°,180°)`, exactly one of
the following holds, and in each case the winning strategy is explicit:*
- *(W) `180/θ ∈ ℤ` (say `= n ≥ 2`): Mulan wins from every opening in `≤ n − 1`
  moves, by the explicit Lemma-F-plus-Lemma-R strategy (§3).*
- *(S) `180/θ ∉ ℤ`: Shan-Yu, opening with the equilateral and always keeping a
  `S_θ`-child (which exists by the four-case closure §2), avoids `θ` forever, so
  Mulan does not win in finitely many steps.*

*Proof.* The dichotomy `180/θ ∈ ℤ` vs. `180/θ ∉ ℤ` is logically exhaustive and
mutually exclusive. In case (W), §3 gives `W_{n−1} = X`: every state is a finite
Mulan win, so Shan-Yu has no escape — no draw, Mulan wins. In case (S), §4 gives
a Shan-Yu strategy (`E`-opening, keep-in-`S_θ`) under which `θ` is never
reached — no finite Mulan win, no draw, Shan-Yu escapes. The strategies are
explicit (Lemma F's `γ = kθ − A` with `k` from the interval fact; Lemma R's
`γ = θ`; Shan-Yu's equilateral opening and safe-child choice), so the
partition `X = W ⊔ S` is witnessed by constructions, not by a transfinite
fixed-point theorem. ∎

In fixed-point language: the least fixed point `W = ⋃ W_k` and the greatest fixed
point `S` (the largest Shan-Yu-closed subset of `X \ W₀`) are complements in `X`,
and this complementarity is **proven directly** by the explicit strategies above,
not imported from abstract game theory. Concretely:
- When `180/θ = n ∈ ℤ`: `W = X` (collapses at the finite stage `n−1`), `S = ∅`.
- When `180/θ ∉ ℤ`: `W = X \ S_θ` and `S = S_θ ≠ ∅`. Indeed:
  - `X \ S_θ ⊆ W`: any triple carrying an `mθ`-angle (`m ≥ 1`) is in
    `W_{m−1}` by Lemma R (Lemma R uses only `mθ < 180`, not `180/θ ∈ ℤ`).
  - `S_θ ∩ W = ∅`: proven in §4 (closure).
  Hence `W = X \ S_θ` exactly, and `S_θ` is the greatest Shan-Yu-closed set
  (any closed set `Z` avoiding `W₀` satisfies `Z ∩ W = ∅` by the argument of §4
  generalized, so `Z ⊆ X \ W = S_θ`).

No state is undetermined; no `θ` yields an infinite draw.

### 6. The characterization (combining)

- **(`⟸`)** If `180/θ = n ∈ ℤ, n ≥ 2`: §3 proves `W_{n−1} = X`. Mulan forces a
  win from any Shan-Yu opening in `≤ n − 1` moves. Mulan guarantees victory in
  finitely many steps.
- **(`⟹`)** If Mulan guarantees victory in finitely many steps, then
  `180/θ ∈ ℤ`. Contrapositive (Contrapositive, KB): if `180/θ ∉ ℤ`, §4 exhibits
  (the equilateral opening) a Shan-Yu play under which Mulan never wins, so
  Mulan does not guarantee victory.

Both directions proved; the dichotomy is exhaustive with no draw (§5). The answer
is

  **`θ ∈ {180°/n : n ∈ ℤ, n ≥ 2}` = {90°, 60°, 45°, 36°, 30°, …}**.

### 7. Verification of the answer and case coverage

- **Answer stated explicitly:** `θ = 180°/n`, `n ≥ 2` integer.
- **Tightness / construction:** for each such `n`, `θ = 180°/n` is itself an
  angle in `(0°,180°)` (since `n ≥ 2` ⟹ `θ ≤ 90° < 180°`), and §3 gives the
  finite winning strategy — the set is nonempty and every advertised value
  works. For values `θ` with `180/θ ∉ ℤ` (including all `θ > 90°`, and all
  `θ < 90°` with `180/θ ∉ ℤ` such as `θ = 50°, 72°, 80°, 7°`, plus every
  irrational `180/θ`), §4 gives the Shan-Yu escape — no extra `θ` works. So the
  characterization is tight in both directions.
- **Cases covered (exhaustive, disjoint):**
  - `n = 2` (`θ = 90°`): special move `γ = 90 − A` (§3 base). ✓
  - `n ≥ 3` (`θ ≤ 60°`): Lemma F interval move + Lemma R descent (§3). ✓
  - `θ > 90°` (necessity): `180/θ ∈ (1,2) ∉ ℤ`; equilateral safe since
    `B_θ ⊂ (θ,180°) ∌ 60°` (§2). ✓
  - irrational `180/θ` and rational-non-integer `180/θ = p/q` (`q ≥ 2`): both
    fall under `180/θ ∉ ℤ` and are handled **uniformly** by the four-case
    closure (§2), which uses only the failure of `180 ∈ θℤ`, with no
    discreteness assumption. ✓
  - `θ = 1°` (`n = 180`): covered by the `n ≥ 3` case (Lemma F + R). The
    winning set is infinite and accumulates at `0°`. ✓
- **Final answer check by substitution:** for `θ = 60°` (`n = 3`), `B_θ = {60°,
  120°}`; a generic triple `(50°,55°,75°)` (no `B_θ`-angle) is handled by Lemma
  F: split `C = 75°` (largest), `A = 50°`, interval `(50/60, 125/60) ≈
  (0.833, 2.083)`, pick `k = 2`, `γ = 2·60 − 50 = 70`, `p₁ = 180 − 50 − 70 =
  60`, `p₂ = 50 + 70 = 120`, both in `B_θ`. Both children `(50,70,60)` and
  `(55,5,120)` carry a `B_θ`-angle; by Lemma R (with `m = 1` for the `60`-angle,
  immediate; `m = 2` for the `120`-angle, one descent) both are `≤ 1`-move wins.
  Total `≤ 2 = n − 1` moves. ✓ Substitution confirms.

All cases settled, every lemma proved in full, the final answer stated and
verified by substitution. ∎

## Promotable lemmas

- **Lemma (four-case closure of `S_θ`)** — *If `180/θ ∉ ℤ`, then for every
  `(A,B,C) ∈ S_θ` and every Mulan cut at the `C`-vertex with `γ ∈ (0,C)`, at
  least one child lies in `S_θ`.* Proved in §2 above
  (`results/imo-2026-04/approaches/attractor-level-fixpoint.md`, §2). The four
  linear combinations of `γ` telescope to `A`, `B`, `C`, `180` respectively;
  closure follows because in `S_θ` the first three are excluded and the fourth
  requires `180/θ ∈ ℤ`. Reusable by any approach needing the necessity engine.

- **Lemma R (multiple descent)** — *If a triangle has an angle `mθ` (`m ≥ 1`,
  `mθ < 180`), then it lies in `W_{m−1}`; Mulan's winning move is to cut that
  angle at `γ = θ`.* Proved in §3 above (induction on `m`, with the positivity
  bound `A+θ < 180 − (m−1)θ`). Uses only `mθ < 180`, so applies whether or not
  `180/θ ∈ ℤ`. Reusable by any approach needing the sufficiency descent.

- **Lemma F (reach a multiple from anywhere)** — *For integer `n = 180/θ ≥ 3`,
  any triple with no `B_θ`-angle is in `W_{n−1}`: split the largest angle `C`,
  pick `k` in the open interval `(A/θ, (A+C)/θ)` of length `C/θ > 1`, set
  `γ = kθ − A ∈ (0,C)`, both `P`-angles become multiples of `θ`.* Proved in §3
  above. Reusable by any approach needing the forcing move.

- **Lemma (interval contains integer)** — *An open interval of length `> 1`
  contains an integer.* Proved in §3 above (cases `x ∈ ℤ` / `x ∉ ℤ`).
  Reusable.

- **Lemma (constructive no-draw dichotomy)** — *For every `θ ∈ (0°,180°)`,
  either Mulan has an explicit finite winning strategy (`180/θ ∈ ℤ`) or Shan-Yu
  has an explicit perpetual-escape strategy (`180/θ ∉ ℤ`); no `θ` yields an
  infinite draw.* Proved in §5 above. Reusable as the determinacy clause.
