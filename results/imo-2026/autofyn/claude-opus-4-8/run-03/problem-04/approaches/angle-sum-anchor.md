# Approach: angle-sum-anchor (compute_and_prove: the 180°-divisibility characterization)

## Status
solved

## Purpose
This approach owns the **compute_and_prove / characterization** requirement: it states the
winning set of θ explicitly, verifies it, and **refutes both plausible wrong answers**
(θ ≤ 90 and θ | 90). The whole argument is anchored on the single arithmetic constant in
the game — the angle sum 180° — and, as the outline-reviewer required, it **rests on the
rigorous mod-θ covering computation**, not on any "anchor heuristic." The anchor language is
only the narrative for *why* 180 is decisive; the load-bearing steps (the Covering Lemma and
the double-plant construction) are proved from scratch below.

## Answer
> **Mulan can guarantee victory if and only if θ divides 180°**, i.e. iff 180/θ is an integer.
> Equivalently the winning set is
> $$\{\theta : \theta = 180^\circ/n,\ n\in\mathbb Z,\ n\ge 2\} = \{90^\circ,60^\circ,45^\circ,36^\circ,30^\circ,\tfrac{180}{7}^\circ,22.5^\circ,20^\circ,18^\circ,\dots\}.$$

(The constraint n ≥ 2 comes from 0° < θ < 180°: n = 1 gives θ = 180°, excluded.)

## Answer verification and refutation of wrong conjectures (the compute_and_prove content)

Write **θ | 180** for "180/θ ∈ ℤ" and **θ ∤ 180** otherwise. Everything below proves:
θ | 180 ⟹ Mulan wins (§ Sufficiency), and θ ∤ 180 ⟹ Shan-Yu wins (§ Necessity).

**Tabulation of the first winning values** (n = 180/θ):

| n | θ = 180/n | winning? | witnessed by |
|---|-----------|----------|--------------|
| 2 | 90°       | yes      | one-move altitude plant (§Suff., θ=90 case) |
| 3 | 60°       | yes      | plant a θ-multiple in both children, then descend |
| 4 | 45°       | yes      | same construction |
| 5 | 36°       | yes      | same construction |
| 6 | 30°       | yes      | same construction |
| 7 | 180/7 ≈ 25.714° | yes | same construction |

Every winning θ equals 180/n ≤ 180/2 = 90, so **every winning θ is ≤ 90°**; in particular
**every θ > 90° is a loss** (this recovers the "no obtuse traction" intuition). But ≤ 90 is
**not** sufficient:

- **Refutation of "θ ≤ 90 suffices".** θ = 40, 50, 70, 25 are all ≤ 90 yet
  180/40 = 4.5, 180/50 = 3.6, 180/70 = 18/7, 180/25 = 7.2 are non-integers, so θ ∤ 180 for
  each. By the Necessity theorem below, **all four are losses.** Hence "θ ≤ 90" is a strictly
  larger set than the winning set and is the wrong criterion.

- **Refutation of "θ | 90 suffices/is the criterion".** The divisors-of-90 conjecture would
  give the set {90, 45, 30, 22.5, 18, …} and would **exclude θ = 60** (since 90/60 = 1.5 ∉ ℤ).
  But 180/60 = 3 ∈ ℤ, so θ = 60 | 180, and by the Sufficiency theorem **θ = 60 is a WIN.**
  Likewise 36 (180/36 = 5, but 90/36 = 2.5), 20 (180/20 = 9, but 90/20 = 4.5) and 180/7 are
  wins that "θ | 90" would miss. So the criterion is divisibility of **180**, not of 90.
  (Note θ | 90 ⟹ θ | 180, so the divisors of 90 are genuine wins — just an undercount.)

- **Confirmation that θ = 90 (n = 2) is a win**, as the boundary case: proved in the θ = 90
  branch of Sufficiency (drop the altitude from the vertex whose two neighbours are acute).

Thus the criterion is exactly **θ | 180**, refuting both near-misses. The two computational
cross-checks in the outline review (20k random off-lattice triangles for necessity across
θ = 40,50,70,25,80,100,7 with zero covering failures; 3k random triangles per θ for the
double-plant across θ = 90,60,45,36,30,20,180/7) agree; but the proof below stands on its own.

---

## Setup: the one-cut algebra (derived from scratch)

A triangle has vertices A, B, C with angles a, b, c at them, a + b + c = 180°. A legal Mulan
move chooses a point P on one side, not a vertex, and cuts from P to the **opposite** vertex.
Equivalently: choose a **cut vertex** (say A) and a point P on the opposite side BC; the cut
is the cevian AP. This is a bijection between legal moves and pairs (cut vertex, interior
point of the opposite side). Parametrise the cut by
$$x := \angle BAP \in (0, a),$$
so the cevian splits angle a into x and a − x. The two resulting triangles are
$$\text{child}_1 = (x,\ b,\ 180 - x - b), \qquad \text{child}_2 = (a - x,\ c,\ x + b).$$
Indeed triangle ABP has angles ∠BAP = x, ∠ABP = b (angle at B is unchanged), and
∠APB = 180 − x − b; triangle ACP has ∠CAP = a − x, ∠ACP = c, and
∠APC = 180 − (a − x) − c = x + b (using a + b + c = 180). The two cut-point angles
$$\angle APB = 180 - x - b \quad\text{and}\quad \angle APC = x + b$$
are **supplementary**: their sum is 180° (P lies on the straight segment BC). This is the
angle-sum identity that makes 180 the anchor.

**Non-degeneracy.** For any x ∈ (0, a) both children are genuine triangles: their angles are
positive (x > 0, a − x > 0, b, c > 0, 180 − x − b = c + (a − x) > 0, x + b > 0) and each is
< 180 (e.g. x + b = 180 − (180 − x − b) < 180). So **x ∈ (0, a) is the only condition needed**
for a legal, non-degenerate cut. We use this repeatedly.

Two special cuts:
- **Forced θ-plant** at a vertex of angle a > θ, taking x = θ: child₁ = (θ, b, 180 − θ − b)
  carries angle θ, so if Shan-Yu keeps child₁ Mulan wins; otherwise the survivor is
  child₂ = (a − θ, c, θ + b), whose angle at the cut vertex is a − θ.
- **Bisection of a 2θ-vertex** (a = 2θ, x = θ): child₁ = (θ, b, 180 − θ − b) and
  child₂ = (θ, c, θ + b) **both** carry θ, so Mulan wins in one move regardless of Shan-Yu.

Throughout, "an angle lies in the **lattice** θℤ" means it is a positive integer multiple of θ.
We write v ≡ w (mod θ) for congruence of real numbers modulo θ (i.e. v − w ∈ θℤ⁰ := θ·ℤ). A
positive angle v ∈ (0,180) lies in θℤ iff v ≡ 0 (mod θ).

---

## Necessity: if θ ∤ 180, then Shan-Yu wins (Mulan cannot force victory)

Shan-Yu plays to maintain the

> **Invariant I:** the current triangle has *no* angle in the lattice θℤ.

Since θ ∈ θℤ, I implies no angle equals θ, so under I the game never stops with a Mulan win.
If Shan-Yu can maintain I forever, the game runs forever without Mulan winning, so Mulan
cannot guarantee victory in finitely many steps. We show I can be maintained.

### Base case: a legal starting triangle satisfying I exists

The lattice values in range, θℤ ∩ (0,180) = {θ, 2θ, …, ⌈180/θ⌉ − 1)·θ}, form a **finite** set
(it has ⌈180/θ⌉ − 1 elements). Consider the open 2-simplex
Δ = {(a,b,c) : a,b,c > 0, a + b + c = 180}, a 2-dimensional set of positive Lebesgue measure.
The "forbidden" set inside Δ is
$$F = \{(a,b,c)\in\Delta : a\in\theta\mathbb Z \text{ or } b\in\theta\mathbb Z \text{ or } c\in\theta\mathbb Z\}.$$
Each condition "a = kθ" (for one of the finitely many k with 0 < kθ < 180) cuts Δ in a single
line segment; F is therefore a finite union of line segments, a set of 2-dimensional measure
zero. Hence Δ \ F ≠ ∅: there is a triangle with all three angles ∉ θℤ. Shan-Yu starts there.
(A concrete instance is equally available; existence is all we need.)

### Preservation: the Covering Lemma (the load-bearing computation)

> **Covering Lemma.** Suppose θ ∤ 180 and a triangle has all three angles ∉ θℤ. Then for
> **every** choice of cut vertex and **every** cut parameter x in the open interval, **at least
> one** of the two children has all three of its angles ∉ θℤ.

*Proof.* By symmetry (all three angles play identical roles and all are ∉ θℤ), it suffices to
treat a cut at the vertex of angle a, with neighbours b, c ∉ θℤ; the other two cut-vertex
choices are the same statement with the labels permuted. For x ∈ (0, a) the children are
child₁ = (x, b, 180 − x − b) and child₂ = (a − x, c, x + b).

Because b ∉ θℤ, child₁ can fail I only through its other two angles:
$$\text{child}_1 \text{ bad} \implies x \equiv 0 \ \text{ or }\ 180 - x - b \equiv 0 \pmod\theta.$$
Because c ∉ θℤ, similarly
$$\text{child}_2 \text{ bad} \implies a - x \equiv 0 \ \text{ or }\ x + b \equiv 0 \pmod\theta.$$
Suppose, for contradiction, that **both** children are bad. Then we have an AND of two two-way
ORs, i.e. exactly **four** cases (all congruences mod θ):

- **(i)** x ≡ 0 and a − x ≡ 0. Adding, a ≡ 0, i.e. a ∈ θℤ — contradicts a ∉ θℤ.
- **(ii)** x ≡ 0 and x + b ≡ 0. Subtracting, b ≡ 0 — contradicts b ∉ θℤ.
- **(iii)** 180 − x − b ≡ 0 and a − x ≡ 0. The second gives x ≡ a; the first gives x ≡ 180 − b.
  Hence a ≡ 180 − b, i.e. a + b ≡ 180. Since a + b = 180 − c this is 180 − c ≡ 180, so c ≡ 0 —
  contradicts c ∉ θℤ.
- **(iv)** 180 − x − b ≡ 0 and x + b ≡ 0. **Adding** the two — this is exactly the supplementary
  angle-sum identity — gives (180 − x − b) + (x + b) = 180 ≡ 0 (mod θ), i.e. θ | 180 —
  contradicts θ ∤ 180.

Every case is impossible, so the two children cannot both be bad. ∎

The four cases are jointly exhaustive (they are the four products of the two ORs) and each is
disjoint-in-conclusion; there is no fifth case. This is the sole place where the divisibility
of **180** enters — case (iv) — which is precisely the "anchor": the only way both children can
be lattice-bad is for the constant 180 (the supplement sum) itself to be a lattice point.

### Conclusion of necessity

By induction on the number of moves: I holds at the start (base case); whenever Mulan makes a
cut, the Covering Lemma guarantees a child satisfying I, and Shan-Yu keeps that child, so I is
preserved. Hence I holds forever, no angle ever equals θ, and Mulan never wins. Therefore
**θ ∤ 180 ⟹ Shan-Yu wins.** ∎

---

## Sufficiency: if θ | 180, then Mulan wins

Write n := 180/θ ∈ ℤ, n ≥ 2 (so θ = 180/n ≤ 90). If the initial triangle already has an angle
= θ, Mulan has won; assume not. All references below to "the current triangle" assume the game
has not stopped, i.e. no angle equals θ.

### The double-plant (why θ | 180 gives traction in one move)

> **Double-plant Lemma.** If θ | 180 and a triangle has a vertex of angle v and a neighbour of
> angle p, then cutting that vertex with any x ∈ (0, v) satisfying **x ≡ −p (mod θ)** makes
> **both** children carry a positive multiple of θ (an angle in θℤ ∩ (0,180)). Consequently,
> whichever child Shan-Yu keeps, its kept triangle has an angle in θℤ.

*Proof.* With cut vertex of angle v and neighbour p, the children are (x, p, 180 − x − p) and
(v − x, q, x + p) where q is the other neighbour. Since x ≡ −p (mod θ):
- child's angle **x + p ≡ 0 (mod θ)**; and x + p ∈ (0,180), so x + p ∈ θℤ;
- child's angle **180 − x − p ≡ 180 − 0 ≡ 0 (mod θ)** — here we use **θ | 180** so that
  180 ≡ 0, together with x + p ≡ 0 so −x − p ≡ 0; and 180 − x − p ∈ (0,180), so it is in θℤ.

Thus (x, p, 180 − x − p) contains the θ-multiple 180 − x − p, and (v − x, q, x + p) contains the
θ-multiple x + p. Both children carry a positive multiple of θ. ∎

The identity used is exactly the supplement 180 = (x + p) + (180 − x − p): the two planted
angles are supplementary, their residues mod θ sum to 180 ≡ 0, so if one is 0 the other is too.
This is the "anchor" made precise — and it works **only** because θ | 180.

### θ = 90 (n = 2): win in one move

Every triangle has at least two acute angles: at most one angle can be ≥ 90 (two angles ≥ 90
would sum to ≥ 180, impossible alongside a positive third angle). Choose the cut vertex A so
that its two neighbours b, c are both **acute** (< 90): if the triangle is acute any vertex
works; if it is obtuse, take A to be the obtuse vertex, whose two neighbours are then the two
acute angles. Apply the Double-plant Lemma at A with neighbour b, taking x = 90 − b:
- x ≡ −b (mod 90) since (90 − b) + b = 90 ≡ 0; and x = 90 − b > 0 because b < 90;
- x < a because x < a ⟺ 90 − b < a ⟺ a + b > 90 ⟺ 180 − c > 90 ⟺ c < 90, true since c is acute.

So x ∈ (0, a) is legal. The planted multiples lie in θℤ ∩ (0,180) = {90}, so both children have
an angle exactly 90 = θ. Whichever Shan-Yu keeps, it has angle θ: **Mulan wins in one move.**
(Geometrically, x = 90 − b makes ∠APB = 180 − x − b = 90, i.e. AP is the altitude; its foot P
lies strictly inside BC because both base angles b, c are acute.)

### θ | 180 with θ ≤ 60 (n ≥ 3): plant, then descend

Let a = max(a, b, c) be the largest angle, so a ≥ 60. We first check **a > θ**:
- If n ≥ 4 (θ < 60): a ≥ 60 > θ.
- If n = 3 (θ = 60): a ≥ 60 = θ; and a = 60 forces a = b = c = 60, an equilateral triangle,
  which already has angle 60 = θ — but we assumed the game has not stopped, contradiction. So
  a > 60 = θ.

In all cases **a > θ**. Apply the Double-plant Lemma at the largest vertex with a neighbour b,
choosing x to be the unique representative of the class −b (mod θ) in (0, θ]. Then
0 < x ≤ θ < a, so x ∈ (0, a) is legal, and by the lemma **both children carry a positive
multiple of θ.** Whichever child Shan-Yu keeps, it has an angle equal to **mθ** for some
integer m with 1 ≤ m ≤ n − 1 (a positive multiple of θ that is < 180 = nθ).

Now **descend on m**. Mulan repeatedly applies the forced θ-plant at the vertex of angle mθ:
- **If m = 1:** the survivor already has angle θ — Mulan has won.
- **If m ≥ 2:** cut that vertex with x = θ (legal since 0 < θ < mθ). The children are
  (θ, p, 180 − θ − p) and ((m − 1)θ, q, θ + p), where p, q are the neighbours and the second
  triangle is non-degenerate (all three angles positive — (m − 1)θ > 0 as m ≥ 2 — and each
  < 180: (m − 1)θ ≤ (n − 2)θ < 180, q < 180, θ + p = 180 − (m − 1)θ − q < 180). The first child
  carries angle θ.
  - If m ≥ 3: the second child's cut-vertex angle is (m − 1)θ ≥ 2θ ≠ θ. If Shan-Yu keeps the
    first child he loses immediately; otherwise the survivor is ((m − 1)θ, q, θ + p), which has
    the angle (m − 1)θ. Either way Mulan is at least as well off with the counter m decreased
    by 1.
  - If m = 2: the second child is (θ, q, θ + p), which **also** carries angle θ. So **both**
    children carry θ (this is the bisection-of-2θ move, x = θ = half of 2θ), and Mulan wins
    regardless of Shan-Yu's choice.

Since m starts at most n − 1 and strictly decreases by 1 on each forced move that Shan-Yu
survives, after at most (n − 1) − 2 = n − 3 forced moves the counter reaches m = 2, at which
Mulan wins outright; and at any earlier step where Shan-Yu keeps a θ-child, Mulan wins sooner.
Total number of Mulan moves ≤ 1 (plant) + (n − 2) (descent) = n − 1, which is finite.
Therefore **θ | 180 ⟹ Mulan wins.** ∎

---

## Why 180 is the anchor (summary of the mechanism)

Necessity case (iv) and the Double-plant Lemma are two faces of one identity: the two
cut-point angles 180 − x − b and x + b are **supplementary**, so their residues mod θ always
sum to 180 (mod θ). If θ ∤ 180, that sum is a fixed nonzero residue, so the two cut-point
angles can never be simultaneously 0 — Shan-Yu always has a lattice-free child (Covering
Lemma), and I survives forever. If θ | 180, that sum is 0, so a single cut with x ≡ −b (mod θ)
drives **both** cut-point angles into θℤ at once — Mulan plants a lattice angle in both children
and then walks it down to θ. The constant 180 is the *only* value the algebra supplies for
free; Mulan gains traction exactly when 180 is itself a lattice point of θℤ, i.e. **θ | 180**.

## Final answer (restated and verified)

**Mulan wins ⟺ θ | 180°**, winning set {180/n : n ∈ ℤ, n ≥ 2} = {90°, 60°, 45°, 36°, 30°,
180/7°, 22.5°, 20°, …}. Verified: both directions proved above; θ = 90,60,45,36,30 confirmed
winning by explicit construction; θ = 40,50,70,25 (≤ 90, ∤ 180) confirmed losing by the
Necessity theorem; and θ = 60 (∤ 90) confirmed winning, refuting both the "θ ≤ 90" and "θ | 90"
conjectures. ∎

---

## Approaches tried
- Round 2 (angle-sum-anchor): filled the outline into a complete proof. Rewrote the "anchor"
  intuition to REST on the rigorous 4-case Covering Lemma (proved inline, self-contained, not
  depending on the not-yet-created shared lemma file) as the outline-reviewer required; proved
  the Double-plant Lemma, the θ=90 altitude case, and the plant→descend construction with full
  range/non-degeneracy checks; supplied the explicit answer tabulation and refuted both wrong
  conjectures (θ≤90 via θ=40,50,70,25; θ|90 via θ=60). Outcome: **solved** (both directions
  complete, answer stated and verified).

## Current best
Complete characterization with both directions fully proved. No open gap. The two computations
that carry the proof — the Covering Lemma (necessity) and the Double-plant Lemma with
plant-then-descend (sufficiency) — are both written out from scratch here, with all
x-range and non-degeneracy conditions checked and the descent move-count bounded by n − 1.

## Full proof
The complete proof is the sections above: **Setup** (one-cut algebra + non-degeneracy),
**Necessity** (base via measure-zero forbidden set + Covering Lemma + induction), and
**Sufficiency** (Double-plant Lemma + θ=90 altitude case + plant/descend for θ≤60), followed by
the verified **Final answer**. ∎

## Promotable lemmas
- **Covering Lemma** (necessity core): *If θ ∤ 180 and a triangle has all three angles ∉ θℤ,
  then for every cut vertex and every x in the open interval, at least one child has all angles
  ∉ θℤ.* Proved in full in §Necessity (4-case exhaustion). Matches the shared
  `lemmas/lattice-covering.md` the reviewer asked the primary builder to certify; this file
  gives an independent self-contained proof.
- **Double-plant Lemma** (sufficiency core): *If θ | 180, cutting a vertex of angle v with a
  neighbour p at any x ∈ (0,v) with x ≡ −p (mod θ) puts a positive multiple of θ in both
  children.* Proved in full in §Sufficiency (uses only the supplement identity 180 = (x+p) +
  (180−x−p) and θ | 180).
