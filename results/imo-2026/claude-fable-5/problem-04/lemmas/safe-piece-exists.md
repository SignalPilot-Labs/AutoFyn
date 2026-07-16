# Lemma: safe-piece-exists (Safety Preservation)

**Certification status: CERTIFIED by proof-reviewer, round 2.** Verified: statement no stronger than what is proved; setup (piece formula, t ∈ (0, a), relabeling) self-contained and independently re-derived from coordinates (3000 random coordinate tests, max error 2·10⁻¹¹); four-case argument exhaustive (each piece's inherited angle eliminated by safety of T, leaving a 2×2 disjunction) and each case contradictory; adversarially checked on 436 422 exact-rational cuts across θ ∈ {40, 72, 120, 7/3, 170, 1234/11} incl. multiples-of-θ and θ−r_b parameters — 0 failures. Importable by any approach.
Origin: approach `remainder-forcing`, round 2 (also used by approach `descending-chain` for its necessity direction). The proof below is self-contained: it does not depend on any approach file.

## Definitions

Fix a real θ with 0° < θ < 180°.

- **Congruence mod θ over ℝ.** For x, y ∈ ℝ, write x ≡ y (mod θ) iff (x − y)/θ ∈ ℤ. This is an equivalence relation compatible with addition and subtraction: if x ≡ x′ and y ≡ y′ (mod θ), then x ± y ≡ x′ ± y′ (mod θ), since ℤ is closed under addition and subtraction.
- **Positive multiple.** A real x is a *positive multiple* of θ iff x = mθ for some integer m ≥ 1.
- **Remark R1.** If x > 0 and x ≡ 0 (mod θ), then x/θ is a positive integer, so x is a positive multiple of θ; the converse is clear. Hence for positive reals (in particular triangle angles): *positive multiple ⟺ ≡ 0 (mod θ)*.
- **Safe.** A (nondegenerate) triangle is *safe* for θ iff none of its three interior angles is a positive multiple of θ. By R1, equivalently: each angle x has x ≢ 0 (mod θ).

## Setup: cuts and the piece formula

Let T be a nondegenerate triangle with interior angles a, b, c ∈ (0°, 180°) at vertices A, B, C; a + b + c = 180° (Euclidean angle-sum theorem). A *legal cut* is: a point P on the perimeter of T, distinct from the three vertices, joined by a straight segment to the vertex opposite the side containing P, splitting T into two triangles.

Every legal cut has the following description. P lies in the interior of exactly one side; label its endpoints B, C and the opposite vertex A, and set t = ∠BAP. Then:

1. **t ∈ (0, a).** Since P is interior to segment BC and A ∉ line BC, the vector P − A = (1 − s)(B − A) + s(C − A) for some s ∈ (0, 1) is a positive combination of the linearly independent vectors u = B − A, v = C − A. Placing A at the origin with u on the positive x-axis and v in the open upper half-plane (a reflection if needed; angles are preserved), the closed convex sector spanned by polar angles [0, a] (convex since a < 180°) contains u and v, hence their convex combination P − A ≠ 0; its polar angle ψ lies in [0, a], and ψ ≠ 0, ψ ≠ a because P − A is proportional to neither u nor v (both coefficients 1 − s, s are nonzero). Thus t = ψ ∈ (0, a) and moreover ∠BAP + ∠PAC = ψ + (a − ψ) = a (angle additivity).
2. **Piece formula.** The two pieces are the triangles ABP and APC, both nondegenerate (P ≠ B, C and A ∉ line BC), with angle triples
   - T₁ = ABP: (b, t, a + c − t) — at B: P lies on segment BC with P ≠ B, so ray BP = ray BC and ∠ABP = b; at A: t; at P: 180° − b − t = a + c − t by the angle-sum theorem and a + b + c = 180°.
   - T₂ = APC: (c, a − t, b + t) — at C: ray CP = ray CB, so ∠ACP = c; at A: ∠PAC = a − t by angle additivity above; at P: since B, P, C are collinear with P between B and C, ∠APC = 180° − ∠APB = b + t.
   All six listed angles lie in (0°, 180°): t, a − t ∈ (0, a) by (1); b, c are angles of T; and a + c − t = 180° − (b + t) with a + c − t > a − t > 0 and b + t > b > 0, so both lie strictly between 0° and 180°. The two angles at P are supplementary: (a + c − t) + (b + t) = 180°.
3. **Relabeling remark.** The names B, C of the endpoints of the side containing P are labels: swapping them (B ↔ C) swaps b ↔ c and replaces t by a − t, exchanging the two triples in (2) — the same physical pieces. Hence the parametrization "(cut vertex A, companion B, parameter t ∈ (0, a))", where the *companion* B is the endpoint whose piece receives the new angle t at A, ranges — as the labeling varies — over **all** legal cuts, each legal cut arising from exactly two label-equivalent descriptions.

## Statement

**Lemma (safe-piece-exists).** Suppose 180/θ ∉ ℤ. Let T be a triangle that is safe for θ. Then for **every** legal cut of T — that is, for every choice of cut vertex A, every companion labeling, and every parameter t ∈ (0, a) — at least one of the two pieces T₁, T₂ is safe for θ.

## Proof

By the Setup, it suffices to prove the claim for an arbitrary labeled description: T = (a, b, c) safe, cut to A with companion B and any t ∈ (0, a), pieces T₁ = (b, t, a + c − t) and T₂ = (c, a − t, b + t), all six angles in (0°, 180°). Since the labels (A, B, C) are arbitrary, this covers every vertex choice and every legal cut.

Suppose, toward a contradiction, that both pieces are unsafe.

- T₁ unsafe: by R1 some angle of T₁ is ≡ 0 (mod θ). Its inherited angle b is an angle of the safe triangle T, so b ≢ 0 (mod θ). Hence **t ≡ 0 (mod θ) or a + c − t ≡ 0 (mod θ)**.
- T₂ unsafe: its inherited angle c satisfies c ≢ 0 (mod θ) (T safe). Hence **a − t ≡ 0 (mod θ) or b + t ≡ 0 (mod θ)**.

Crossing the two disjunctions gives four exhaustive cases (they need not be disjoint; each is refuted, which suffices):

**(i) t ≡ 0 and a − t ≡ 0.** By additivity of congruence, a = t + (a − t) ≡ 0 (mod θ). Since a > 0, R1 makes a a positive multiple of θ, contradicting the safety of T.

**(ii) t ≡ 0 and b + t ≡ 0.** Then b = (b + t) − t ≡ 0 (mod θ); b > 0, so b is a positive multiple of θ — contradiction with safety of T.

**(iii) a + c − t ≡ 0 and a − t ≡ 0.** Then c = (a + c − t) − (a − t) ≡ 0 (mod θ); c > 0 — contradiction with safety of T.

**(iv) a + c − t ≡ 0 and b + t ≡ 0.** Then 180° = a + b + c = (a + c − t) + (b + t) ≡ 0 (mod θ), i.e., 180/θ ∈ ℤ — contradicting the hypothesis.

All four cases are impossible, so both pieces cannot be unsafe: at least one piece is safe. ∎

## Remarks for importers

- The hypothesis 180/θ ∉ ℤ is used only in case (iv) and is essential: if 180/θ = n ∈ ℤ, the lemma is false — the Forcing cut t ≡ −b (mod θ) (when valid) makes both pieces unsafe. This dichotomy is exactly the answer to imo-2026-04.
- The lemma holds uniformly for all θ ∈ (0°, 180°) with 180/θ ∉ ℤ, rational or irrational, acute or obtuse.
- A safe triangle has no angle equal to θ (= 1·θ), so a player who keeps a safe piece never triggers the stopping condition.
