## Status
solved

## Approaches tried
- **and-or-closure-rank-induction (round 3)** — APPROVE / SOLVED. Complete characterization
  θ = 180°/m (m ≥ 2). ⊇ (certified construction), θ>90 (certified device lemma), and the new ⊆
  survival direction (0<θ<90, 180/θ∉ℤ) closed by the boolean **F-free** invariant: Sub-lemma B
  (every legal cut of an F-free triangle leaves ≥1 F-free child) + rank induction (F-free ⟹ ∉W_k
  ∀k) + F-free start existence. Reviewer verified all four combinations of Sub-lemma B by hand and
  over 201k exact-arithmetic adversarial splits (0 failures).
- **explicit-ffree-strategy (round 3)** — APPROVE / SOLVED. Same characterization, ⊆ direction via
  an explicit Shan-Yu defender strategy Σ ("always keep an F-free child"), well-defined by
  Sub-lemma B, F-freeness maintained by induction on move number. Architecturally distinct from the
  rank-induction sibling; identical engine (Sub-lemma B). Verified.
- **and-or-closure-rank-induction (round 2)** — CHANGES REQUESTED (superseded). Had honestly-marked
  ⊆ closure gap (x=c−B collapse). Closed in round 3 by dropping the unnecessary transcendence
  conjunct.
- **transcendence-genericity-invariant (round 2)** — CHANGES REQUESTED. ⊆ genericity gap; subsumed.
- **explicit-shanyu-peel-potential (round 2)** — RETHINK. Wrong "dyadic 90/θ" conjecture. Dead.

## Current best

The full characterization is proved and reviewer-approved. **Mulan can force victory iff
θ = 180°/m for some integer m ≥ 2** (equivalently 180/θ ∈ ℤ and θ ≤ 90°). All three ingredients are
rigorous and certified: ⊇ construction (`construction-180-over-m`), θ>90 impossibility
(`device-classification-theta-gt-90`), and the ⊆ survival direction via the F-free invariant
(`sub-lemma-b-ffree-split`, `ffree-start-exists`, `ffree-rank-induction`).

## Full proof

### Setup and normal form (certified: `cevian-split-normal-form`)

A game state is an unordered triple (A, B, C) of positive reals with A + B + C = 180 (the angles of
the current triangle, in degrees). Mulan's move (per the problem: choose a point P on the perimeter,
not a vertex, and cut from P to the opposite vertex) is exactly a cevian from a chosen vertex to an
interior point of the opposite side. Writing A for the split vertex's angle and B, C for its
neighbours, and x ∈ (0, A) for the part of A on the B-side of the cevian, the two children are

    child₁ = { x, B, 180 − x − B },      child₂ = { A − x, C, x + B }.

All six angles are positive for x ∈ (0, A) (180 − x − B = (A − x) + C > 0). The two P-angles
180 − x − B and x + B are **supplementary** (they sum to 180, the straight angle at P). Ranging over
all three choices of split vertex and all x enumerates every legal move. Shan-Yu keeps one child;
the game stops with a Mulan win the instant the current triangle has an angle equal to θ.

**AND–OR winning set.** W₀ = { T : some angle = θ }; W_{k+1} = W_k ∪ { T : some legal split has
BOTH children in W_k }; W(θ) = ⋃_{k≥0} W_k. Since a Mulan cut produces two children and Shan-Yu
keeps the worse one, Mulan forces a win from T in finitely many steps ⟺ T ∈ W(θ). Because Shan-Yu
also chooses the starting triangle, **Mulan wins the game for θ ⟺ W(θ) = all triangles**;
equivalently **Shan-Yu survives forever ⟺ some triangle lies outside W(θ)**. (Certified normal form.)

> **Theorem.** Mulan can force victory if and only if θ = 180°/m for some integer m ≥ 2
> (equivalently 180/θ ∈ ℤ and θ ≤ 90°).

Since 0 < θ < 180, the three exhaustive, mutually exclusive cases are: **(I)** 180/θ ∈ ℤ and θ ≤ 90
(θ = 180/m, m ≥ 2); **(II)** θ > 90 (then 180/θ < 2, so 180/θ ∉ ℤ); **(III)** 0 < θ < 90 and
180/θ ∉ ℤ. Mulan wins in exactly Case (I).

### Direction ⊇ — Case (I): θ = 180/m is winnable (certified `construction-180-over-m`)

Let θ = 180/m, m ≥ 2. **Peel:** any triangle with a vertex kθ (1 ≤ k ≤ m−1) is in W(θ): split that
vertex at x = θ; child₁ contains θ ∈ W₀, child₂ carries (k−1)θ, recurse. **Seed:** from any θ-free
triangle, splitting a largest vertex admits a cut placing a multiple jθ in both children (the
interval (B, 180−C) contains a multiple jθ; set x = jθ − B, giving child vertices jθ and (m−j)θ).
Both children then peel to θ. Hence W(θ) = all triangles: Mulan wins from every start. ∎

### The engine — Sub-lemma B (certified `sub-lemma-b-ffree-split`)

Fix θ with **180/θ ∉ ℤ**. Let F := { mθ : m ∈ ℤ_{≥1}, mθ < 180 } (finite, |F| = ⌈180/θ⌉ − 1). A
triangle is **F-free** if none of its angles lies in F (in particular no angle equals θ = 1·θ).

> **Sub-lemma B.** If 180/θ ∉ ℤ and T = (A,B,C) is F-free, then for EVERY legal split (every split
> vertex, every x ∈ (0,A)) at least one child is F-free.

*Proof.* Fix the split vertex A (neighbours B,C) and x ∈ (0,A). Suppose both children carry an
F-angle: child₁ has p = aθ, child₂ has q = bθ (a, b ∈ ℤ_{≥1}). Since T is F-free, B ∉ F and C ∉ F,
so p ∈ {x, 180−x−B} and q ∈ {A−x, x+B}. Four combinations:

- **(1) x = aθ, A−x = bθ:** A = (a+b)θ; since a+b ≥ 2 and A < 180, A ∈ F — contradicts T F-free.
- **(2) x = aθ, x+B = bθ:** B = (b−a)θ. If b > a, B ∈ F (positive multiple < 180) — contradiction;
  if b ≤ a, B ≤ 0 — contradicts B > 0.
- **(3) 180−x−B = aθ, A−x = bθ:** subtracting, 180−A−B = C = (a−b)θ. If a > b, C ∈ F —
  contradiction; if a ≤ b, C ≤ 0 — contradicts C > 0.
- **(4) 180−x−B = aθ, x+B = bθ:** these supplementary P-angles sum to 180, so (a+b)θ = 180, i.e.
  180/θ = a+b ∈ ℤ — contradicts 180/θ ∉ ℤ.

All four are contradictory, so at least one child is F-free. ∎

*(Case (4) is the crux: two supplementary values aθ, bθ are both multiples of θ exactly when their
sum 180 is, i.e. exactly when 180/θ ∈ ℤ — the precise arithmetic reason 180, not 90, is the
boundary.)*

### Case (II): θ > 90 (certified `device-classification-theta-gt-90`)

If θ > 90 then 180/θ < 2, so 180/θ ∉ ℤ and F = {θ}; an F-free triangle is a θ-free triangle.
Sub-lemma B + the rank induction below give: every θ-free triangle avoids W(θ). Shan-Yu opens with
e.g. (60,60,60) and survives. Mulan cannot win. ∎

### Direction ⊆ — Case (III): 0 < θ < 90, 180/θ ∉ ℤ, is not winnable

**F-free start exists (certified `ffree-start-exists`).** In the isosceles family
T(t) = (t, t, 180−2t), t ∈ (0,90), an angle lies in F only if t ∈ F or 180−2t ∈ F; both exclude
only finitely many t (F finite), while (0,90) is infinite. Pick t₀ outside the finite union;
T₀ = (t₀, t₀, 180−2t₀) is a legal F-free triangle.

**F-free ⟹ outside W(θ) (certified `ffree-rank-induction`).** Strong induction on k: no F-free
triangle lies in W_k. Base k=0: F-free ⟹ no angle = θ ∈ F ⟹ ∉ W₀. Step: an F-free T in W_{k+1}
would need a split with both children in W_k; but Sub-lemma B gives an F-free child, which ∉ W_k by
the hypothesis. So T ∉ W_{k+1}. Hence every F-free triangle avoids W(θ) = ⋃_k W_k.

**Conclusion.** T₀ is F-free, so T₀ ∉ W(θ); W(θ) ≠ all triangles. Equivalently, Shan-Yu opens with
T₀ and always keeps an F-free child (one exists by Sub-lemma B); by induction the position stays
F-free forever, so no angle ever equals θ. Mulan cannot force a win. ∎

### Assembly

Cases (I), (II), (III) are exhaustive and mutually exclusive, and Mulan wins in exactly Case (I).
**Therefore Mulan can force victory if and only if θ = 180°/m for some integer m ≥ 2.** ∎

**Answer verification.** θ=90=180/2 and θ=60=180/3 are winnable (⊇; the θ=60 two-move win from
(100,50,30) is explicit). θ=72 (180/72=2.5), θ=40 (4.5), θ=120 (1.5) are not winnable (F-free start
survives). Sub-lemma B verified over 201,352 exact-arithmetic adversarial splits (0 failures),
including the collapse cuts x = mθ−B, x = 180−mθ−B and halving.
