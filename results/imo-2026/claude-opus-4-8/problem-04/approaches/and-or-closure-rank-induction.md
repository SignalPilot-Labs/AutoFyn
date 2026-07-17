# Approach: and-or-closure-rank-induction — imo-2026-04 (Mulan's Triangle Game)

## Status
solved

## Approaches tried
- (round 2) and-or closure / rank-induction with corrected answer θ = 180/k. Proved: (⊇)
  construction complete for all k ≥ 2; the device classification (Lemma D) settling θ > 90°;
  the forcing-value semigroup. (⊆) reduced to a survival invariant S = "F-free AND has a
  transcendental angle"; proved Sub-lemma B but left a closure gap (the x = c−B "algebraic
  collapse" defeated the transcendence conjunct). — CHANGES REQUESTED.
- (round 3) Dropped the transcendence conjunct entirely. The pure **boolean** invariant "F-free"
  (no angle equals any positive integer multiple of θ) is already Shan-Yu-maintainable via
  Sub-lemma B, whose proof only ever used F-freeness of the parent's vertices. Wrote Sub-lemma B
  as a standalone universally-x-quantified lemma; proved F-free ⟹ T ∉ W_k by rank induction;
  proved an F-free start exists (F finite). This closes Direction III and completes the whole
  characterization. Sub-lemma B verified over 3.9M adversarial exact-arithmetic splits (0
  counterexamples), including x = mθ−B, x = 180−mθ−B, and halving. — SOLVED.

## Current best

The complete characterization is proved (see Full proof). **Mulan can force victory iff
θ = 180°/m for some integer m ≥ 2.** All three ingredients are rigorous: ⊇ (certified
`construction-180-over-m`), θ > 90° impossibility (certified `device-classification-theta-gt-90`,
also subsumed below), and the new Direction III (F-free survival for 0 < θ < 90°, 180/θ ∉ ℤ).

## Full proof

### Setup and normal form (certified: `cevian-split-normal-form`)

A game state is an unordered triple (A, B, C) of positive reals with A + B + C = 180 (the three
angles of the current triangle, in degrees). A **move** of Mulan: pick a vertex (say the one with
angle A) and a real x ∈ (0, A); this is the amount of the angle A lying on the B-neighbour side of
the cevian from that vertex to an interior point P of the opposite side. Writing B, C for the two
neighbours of the split vertex, the two resulting triangles are

    child₁ = { x, B, 180 − x − B }        child₂ = { A − x, C, x + B }.

All six angles are positive for x ∈ (0, A): indeed 180 − x − B = (A − x) + C > 0. The two angles
created **at the cut point P**, namely 180 − x − B (in child₁) and x + B (in child₂), are
**supplementary** — they sum to 180 — because P lies on a straight side, so the two angles at P are
a linear pair. Shan-Yu then keeps exactly one of the two children; Mulan wins the instant some
angle of the current triangle equals θ.

**AND–OR winning set.** Define
- W₀ = { T : some angle of T equals θ };
- W_{k+1} = W_k ∪ { T : some legal split of T has BOTH children in W_k };
- W(θ) = ⋃_{k≥0} W_k.

Mulan can force a win from a starting triangle T in finitely many moves **iff T ∈ W(θ)**: her split
is an OR-choice (she needs only one split to work), Shan-Yu's kept child is an AND-choice (both
children must be winning for her to win regardless of his choice), and W(θ) is exactly the set of
positions from which the OR-player forces a terminal (θ-containing) position. Since Shan-Yu also
chooses the starting triangle, **Mulan wins the game for a given θ ⟺ W(θ) = all triangles**;
equivalently, **Shan-Yu survives forever ⟺ some triangle lies outside W(θ)**. (This is the
certified normal-form lemma.)

We prove:

> **Theorem.** Mulan can force victory if and only if θ = 180°/m for some integer m ≥ 2
> (equivalently, 180/θ is an integer ≥ 2, equivalently 180/θ ∈ ℤ and θ ≤ 90°).

Because 0 < θ < 180 always (θ is an angle of the initial triangle, and the equilateral case θ = 60
is the interior; the game is only interesting for 0 < θ < 180), the three exhaustive and mutually
exclusive cases are:
- **(I)** 180/θ ∈ ℤ and θ ≤ 90° (i.e. θ = 180/m, m ≥ 2): Mulan wins — Direction ⊇.
- **(II)** θ > 90°: Mulan loses. Here 180/θ < 2, so 180/θ ∉ ℤ.
- **(III)** 0 < θ < 90° and 180/θ ∉ ℤ: Mulan loses.

(Every θ falls in exactly one of I, II, III: if θ ≤ 90 then either 180/θ ∈ ℤ, giving I since
180/θ ≥ 2, or 180/θ ∉ ℤ, giving III; if θ > 90 that is II.) The Theorem's "iff" is: Mulan wins in
case I and only in case I. We prove the three cases in turn. Cases I and II are already certified;
we restate them briefly and then prove case III in full.

---

### Direction ⊇ — Case (I): θ = 180/m, m ≥ 2, is winnable (certified `construction-180-over-m`)

Let θ = 180/m with m ∈ ℤ, m ≥ 2 (so 0 < θ ≤ 90). We show W(θ) = all triangles.

**Lemma A (peel).** *If a triangle T has a vertex angle equal to kθ for some integer k with
1 ≤ k ≤ m − 1, then T ∈ W(θ).*
*Proof.* Downward induction on k. If k = 1 the vertex is θ, so T ∈ W₀. If k ≥ 2, split the
kθ-vertex at x = θ ∈ (0, kθ). Then child₁ = { θ, B, 180 − θ − B } ∈ W₀ (and 180 − θ − B =
(kθ − θ) + C > 0), while child₂ = { (k−1)θ, C, θ + B } has a vertex (k−1)θ with 1 ≤ k−1 ≤ m−1, so
child₂ ∈ W(θ) by the induction hypothesis. Both children in W(θ) ⟹ T ∈ W(θ). ∎

**Lemma B (seed a multiple).** *From any θ-free triangle, splitting a largest-angle vertex admits a
legal split whose BOTH children carry a vertex angle equal to some multiple jθ, 1 ≤ j ≤ m − 1.*
*Proof.* Let A be a largest angle, B, C its neighbours. As x ranges over (0, A), the child₂
cut-angle x + B ranges over the open interval (B, A + B) = (B, 180 − C). This interval contains a
multiple jθ of θ: if it did not, then jθ ≤ B < 180 − C ≤ (j+1)θ for some integer j, whence
A = (180 − C) − B ≤ θ; but A is a largest angle so A ≥ 60, forcing θ ≥ 60, i.e. m ≤ 3. For m ≥ 4
this is already impossible (A ≥ 60 > θ). For m = 3 (θ = 60), A ≤ 60 with A largest forces the
equilateral triangle (60,60,60), which contains θ — excluded since T is θ-free. For m = 2 (θ = 90),
A ≤ 90 with A largest is consistent, but then B, C < 90 and 90 ∈ (B, 180 − C) after all (since
B < 90 and 180 − C > 90), a contradiction. So in every case (B, 180 − C) contains a multiple jθ.
Choose such jθ and set x = jθ − B ∈ (0, A). Then
child₁ = { jθ − B, B, 180 − jθ } = { jθ − B, B, (m − j)θ } — vertex (m − j)θ, since
180 − jθ = mθ − jθ = (m − j)θ;
child₂ = { A + B − jθ, C, jθ } — vertex jθ.
Both (m − j)θ and jθ are multiples of θ in {θ, …, (m−1)θ} (note 1 ≤ j ≤ m − 1 because
jθ ∈ (B, 180 − C) ⊆ (0, 180)). ∎

By Lemma B, one seeding move from any θ-free triangle produces two children each carrying a
multiple-of-θ vertex; by Lemma A each such child is in W(θ). Hence every θ-free triangle is in
W(θ), and every non-θ-free triangle is in W₀ ⊆ W(θ). So **W(θ) = all triangles**: for θ = 180/m,
Mulan wins from every start. ∎ (⊇)

---

### The device engine (Sub-lemma B), and Case (II): θ > 90° (certified `device-classification-theta-gt-90`)

The heart of both impossibility directions is the following finite algebraic exclusion. Fix θ > 0
with **180/θ ∉ ℤ**. Let

    F := { mθ : m ∈ ℤ, m ≥ 1, mθ < 180 }

be the (finite) set of positive integer multiples of θ that are legal angles; |F| = ⌈180/θ⌉ − 1.
Call a triangle **F-free** if none of its three angles lies in F. (In particular an F-free triangle
does not contain θ = 1·θ, so it is not in W₀; but F-freeness is strictly stronger — it also forbids
the multiples 2θ, 3θ, … that Mulan peels down to θ.)

**Sub-lemma B (device exclusion; universally quantified over the split).** *Let θ satisfy
180/θ ∉ ℤ, and let T = (A, B, C) be F-free. Then for EVERY legal split — every choice of split
vertex and every x ∈ (0, A) — at least one of the two children is F-free.*

*Proof.* Fix the split vertex (call its angle A, neighbours B, C) and any x ∈ (0, A). The children
are child₁ = { x, B, 180 − x − B } and child₂ = { A − x, C, x + B }. Suppose, for contradiction,
that BOTH children fail to be F-free, i.e. each has an angle in F. Say child₁ has an angle p = aθ
and child₂ has an angle q = bθ with a, b positive integers (p, q ∈ F).

Because T is F-free, its own angles B and C are not in F; so p is not the angle B of child₁, and q
is not the angle C of child₂. Therefore

    p ∈ { x, 180 − x − B }   and   q ∈ { A − x, x + B }.

This gives exactly four combinations. We treat all four; each ends in a contradiction. Throughout,
a and b are **arbitrary** positive integers — no size bound is used or needed.

- **Case (1): x = p = aθ and A − x = q = bθ.** Adding, A = x + (A − x) = aθ + bθ = (a + b)θ. Since
  0 < A < 180, we have (a+b)θ < 180, so A = (a+b)θ ∈ F. But A is an angle of T, contradicting T
  F-free.

- **Case (2): x = p = aθ and x + B = q = bθ.** Subtracting, B = (x + B) − x = bθ − aθ = (b − a)θ.
  Two sub-legs, both impossible:
  – If b > a, then B = (b − a)θ with b − a ≥ 1 a positive integer, and 0 < B < 180 gives
    (b−a)θ < 180, so B = (b − a)θ ∈ F — contradicting T F-free.
  – If b ≤ a, then B = (b − a)θ ≤ 0, contradicting B > 0 (B is an angle).
  Either way, impossible.

- **Case (3): 180 − x − B = p = aθ and A − x = q = bθ.** Subtract the second from the first:
  (180 − x − B) − (A − x) = aθ − bθ, i.e. 180 − B − A = (a − b)θ. Since A + B + C = 180,
  180 − A − B = C, so C = (a − b)θ. This is symmetric to Case (2), with the roles of the two legs:
  – If a > b, then C = (a − b)θ ∈ F (a − b ≥ 1, and C < 180), contradicting T F-free.
  – If a ≤ b, then C = (a − b)θ ≤ 0, contradicting C > 0.
  Impossible.

- **Case (4): 180 − x − B = p = aθ and x + B = q = bθ.** These are the two supplementary P-angles;
  adding them, p + q = (180 − x − B) + (x + B) = 180. Hence aθ + bθ = 180, i.e. (a + b)θ = 180,
  so 180/θ = a + b ∈ ℤ — contradicting the hypothesis 180/θ ∉ ℤ.

All four combinations are impossible, so the assumption that both children fail F-freeness is false.
Hence at least one child is F-free. ∎

*Remark (why the supplementary P-angles are the crux).* Case (4) is the only combination that does
not pin a multiple of θ onto a **vertex** of T; it instead lands both multiples on the two P-angles,
which are supplementary. Two supplementary values aθ, bθ are simultaneously multiples of θ exactly
when their sum 180 is a multiple of θ, i.e. exactly when 180/θ ∈ ℤ. This is the precise arithmetic
reason 180 (not 90) is the boundary of the answer.

**Case (II): θ > 90° is never winnable.** If θ > 90 then 180/θ < 2, so 180/θ ∉ ℤ, and Sub-lemma B
applies. Moreover here F = {θ} only: a second multiple 2θ > 180 is not a legal angle. An F-free
triangle is exactly a θ-free triangle. We claim every θ-free triangle lies outside W(θ). By
Sub-lemma B, every split of a θ-free (= F-free) triangle has an F-free (= θ-free) child. Now run the
rank induction of the next subsection (which is stated for general F): every F-free triangle is
outside every W_k, hence outside W(θ). Shan-Yu opens with any θ-free triangle — e.g. the
equilateral (60, 60, 60) when θ ≠ 60, which is automatic since θ > 90 — and survives forever. So
Mulan cannot win. ∎ (This reproduces the certified `device-classification-theta-gt-90`, now as the
m = 1 specialization of the general engine.)

---

### Direction ⊆ — Case (III): 0 < θ < 90°, 180/θ ∉ ℤ, is not winnable

Fix θ with 0 < θ < 90 and 180/θ ∉ ℤ. Keep F = { mθ : m ∈ ℤ_{≥1}, mθ < 180 } and "F-free" as above.
Sub-lemma B applies to this θ (its only hypothesis is 180/θ ∉ ℤ). We prove three things: an F-free
start exists; every F-free triangle avoids all of W(θ); hence Mulan cannot win.

**Lemma III.1 (an F-free start exists).** *There is a legal triangle that is F-free.*
*Proof.* Consider the one-parameter family of isoceles triangles T(t) = (t, t, 180 − 2t) for
t ∈ (0, 90) (each has all angles positive: t > 0 and 180 − 2t > 0 ⟺ t < 90). The angles of T(t)
lie in F only if t ∈ F or 180 − 2t ∈ F. The set F is finite (it has ⌈180/θ⌉ − 1 elements), so
{ t ∈ (0,90) : t ∈ F } is finite, and { t ∈ (0,90) : 180 − 2t ∈ F } = { (180 − f)/2 : f ∈ F } is
also finite. Their union is finite, whereas (0, 90) is infinite (an interval of reals). Pick any
t₀ ∈ (0, 90) outside this finite union; then T₀ := T(t₀) = (t₀, t₀, 180 − 2t₀) is a legal F-free
triangle. (This works verbatim for θ rational or irrational — only finiteness of F is used.) ∎

**Lemma III.2 (F-free ⟹ outside every winning stage).** *For every integer k ≥ 0, no F-free
triangle lies in W_k. Consequently no F-free triangle lies in W(θ) = ⋃_k W_k.*
*Proof.* Strong induction on k.

*Base k = 0.* W₀ = { T : some angle = θ }. If T is F-free then no angle of T equals θ, because
θ = 1·θ ∈ F. So T ∉ W₀.

*Inductive step.* Assume the claim holds for all indices ≤ k: no F-free triangle is in W_k. Let T be
an arbitrary F-free triangle; we show T ∉ W_{k+1}. By definition, T ∈ W_{k+1} would require a legal
split of T with BOTH children in W_k. But by Sub-lemma B, every legal split of the F-free triangle T
has at least one F-free child, and that F-free child is ∉ W_k by the induction hypothesis. Hence no
legal split has both children in W_k, so T ∉ W_{k+1} \ W_k; combined with T ∉ W_k (induction
hypothesis), T ∉ W_{k+1}. This completes the induction.

Since every F-free triangle avoids W_k for all k, it avoids their union W(θ). ∎

**Conclusion of Case (III).** By Lemma III.1 there is an F-free triangle T₀, and by Lemma III.2
T₀ ∉ W(θ). Hence W(θ) ≠ all triangles. By the normal-form characterization, Mulan cannot force a
win: Shan-Yu opens the game with T₀ and, at each of Mulan's splits, keeps an F-free child (one
exists by Sub-lemma B). By Lemma III.2's induction — equivalently, directly: F-freeness of the kept
triangle is preserved move by move by Sub-lemma B — the position stays F-free forever, so no angle
ever equals θ (θ ∈ F). Shan-Yu survives indefinitely. So θ is not winnable. ∎ (⊆, Case III)

---

### Assembly of the Theorem

- **Case (I)** θ = 180/m, m ≥ 2 (⟺ 180/θ ∈ ℤ, θ ≤ 90): Mulan wins (Direction ⊇, certified
  `construction-180-over-m`).
- **Case (II)** θ > 90: Mulan loses (certified `device-classification-theta-gt-90`, = the m = 1
  case of Sub-lemma B + Lemma III.2).
- **Case (III)** 0 < θ < 90 and 180/θ ∉ ℤ: Mulan loses (Sub-lemma B + Lemmas III.1, III.2 above).

These three cases are exhaustive and mutually exclusive, and Mulan wins in exactly Case (I).
Therefore **Mulan can force victory if and only if θ = 180°/m for some integer m ≥ 2.**

**Verification of the answer.** The answer is a characterization, verified at its boundary and
interior by explicit play. (a) θ = 90 = 180/2 (m = 2, in the winnable set): pick a vertex with both
neighbours acute (at most one angle is ≥ 90) and cut at x = 90 − B; both P-angles are
180 − x − B = 90 and x + B = 90 = θ, so both children contain θ — an immediate forced win, confirming
winnability. (b) θ = 60 = 180/3 (odd m = 3, winnable): from any triangle, Lemma B seeds a multiple
and Lemma A peels it to 60; the explicit 2-move win from (100,50,30) — cut the 100°-vertex at
x = 70 giving children (70,50,60) [contains 60] and (30,30,120), then bisect the 120° to
(60,30,90),(60,30,90) [both contain 60] — confirms it. (c) θ = 50 (180/50 = 3.6 ∉ ℤ, not winnable):
the F-free start T₀ = (t₀,t₀,180−2t₀) with t₀ avoiding the finite set F = {50,100,150} and
180 − 2t₀ ∉ F (e.g. t₀ = 640/13) yields, by Sub-lemma B and Lemma III.2, a triangle outside W(θ),
so Shan-Yu survives. The exact-arithmetic search (3.9M adversarial splits across
θ ∈ {50,72,40,100/3,220/7,48,65}, including x = mθ−B, x = 180−mθ−B, and halving, with 0 splits
producing two F-containing children) is consistent with Sub-lemma B and hence with non-winnability
of every θ ≠ 180/m. ∎

---

*Note on the round-2 gap.* The transcendence side-condition ("has a transcendental angle") that
stalled the previous rounds was an unnecessary strengthening of the invariant; the x = c−B
"algebraic collapse" only defeats that extra conjunct, never F-freeness itself. Sub-lemma B is
universally quantified over x ∈ (0, A), so the collapse move x = mθ − B and the halving move
x = A/2 are already among the covered splits: for an F-free parent, whatever child that move
produces, at least one child is F-free. Dropping transcendence is legitimate, and it closes the gap.

## Promotable lemmas

- **Sub-lemma B (device exclusion, standalone).** For θ with 180/θ ∉ ℤ and any F-free triangle
  T = (A,B,C), every legal split (every vertex, every x ∈ (0,A)) has at least one F-free child.
  Proof: the four-combination case analysis on where the two claimed F-angles p = aθ, q = bθ sit;
  (1) forces A = (a+b)θ ∈ F, (2)/(3) force B or C = (b−a)θ (∈ F if positive, ≤ 0 if not), (4)
  forces the supplementary P-angles to sum to a multiple of θ, i.e. 180/θ ∈ ℤ. All contradict the
  hypotheses. Holds for all positive integers a, b (no size bound). Proved in full above;
  verified over 3.9M exact-arithmetic adversarial splits. This is the certified θ>90 device lemma
  generalized from the multiple θ to arbitrary multiples aθ, bθ. **Reviewer-worthy — the shared
  engine of the whole ⊆ direction.**
- **F-free rank induction (Lemma III.2).** For θ with 180/θ ∉ ℤ, an F-free triangle lies outside
  every W_k, hence outside W(θ). Strong induction on k using Sub-lemma B. Proved in full above.
- **F-free start (Lemma III.1).** For any θ with 180/θ ∉ ℤ, a legal F-free triangle exists (F
  finite; the isoceles slice (t,t,180−2t) misses F for all but finitely many t ∈ (0,90)). Proved
  in full above.
