# Approach: concyclic-with-w

## Status
partial

## Target
The full claim of imo-2026-02: prove OM = ON for the circumcentre O of triangle AKL.

## Route (one paragraph)
Reformulate the conclusion as a concyclicity with a natural auxiliary point. Let W be the intersection of the perpendicular bisector of BC with the line through A parallel to BC (in coordinates B = (0,0), C = (a,0), A = (A_x, h): W = (a/2, h)). Then W is the reflection of A in the perpendicular bisector V of MN — because A and W have equal heights and (A_x + a/2)/2 = (2A_x + a)/4 = x₀, the abscissa of V. Hence: the circle (AKL) has centre on V ⟺ it passes through the reflection of A in V ⟺ **A, K, L, W are concyclic**. So the whole problem is equivalent to one concyclicity, and (numerically verified, cross-ratio imaginary part ≈ 1e-17) it holds in the form ∠AKW = ∠ALW with K, L on the same side of line AW. The attack: ∠AKW is a *K-side-only* quantity (W depends only on ABC; K only on α, γ) and ∠ALW an *L-side-only* quantity; using the decoupled constraint q_K(τ) = 0, show tan∠AKW satisfies a quadratic whose coefficients are symmetric in B↔C — the same quadratic that tan∠ALW satisfies by the mirrored computation — plus a root-selection argument. Alternatively find a direct angle chase. This is the most "synthetic-flavoured" rival and the one most likely to compress into a short human proof.

## Skeleton (proof with gaps)

**Step 1 (Reformulation Lemma).** W := (perpendicular bisector of BC) ∩ (parallel to BC through A). Then the perpendicular bisector of segment AW equals the perpendicular bisector V of MN. Mechanism: AW is horizontal, its midpoint has x = (A_x + a/2)/2 = (2A_x + a)/4 = midpoint(MN)_x, and V is vertical (MN ∥ BC) through that same abscissa. Consequently, for any circle ω through A: centre(ω) ∈ V ⟺ W ∈ ω. Applying this to ω = (AKL): OM = ON ⟺ O ∈ V ⟺ A, K, L, W concyclic. (Complete; short.)

**Step 2 (Concyclicity criterion).** Since K, L lie below line AW (they are inside the triangle, strictly below the parallel to BC through A — needs one line of justification), A, K, L, W concyclic ⟺ ∠AKW = ∠ALW (equal angles subtending AW from the same side). (Numerically: the two angles agree to 1e-15 in all tested configurations.)

**Step 3 (K-side formula).** With K = (c/2)(cos α − τ sin α)e^{i(B−α)} and the constraint q_K(τ) = 0 (see shared lemmas of fixed-point-t, Steps 1–3 there), compute
  tan ∠AKW = f(τ) := Im[(A−K)conj(W−K)] / Re[(A−K)conj(W−K)],
a ratio of two quadratics in τ with coefficients trig-polynomial in (α, B, C) (and a, c, h = c sin B expressible by the sine rule). Eliminate τ between t·denominator(τ) − numerator(τ) = 0 and q_K(τ) = 0 by resultant: obtain an explicit quadratic equation
  Φ(t; α, B, C) = 0 satisfied by t = tan ∠AKW.
GAP: compute Φ and show its coefficients (after clearing symmetric denominators) are invariant under B ↔ C. [Sanity target: by the mirrored computation, tan ∠ALW satisfies Φ' = Φ with B↔C swapped; symmetry gives Φ' = Φ, so tan∠AKW and tan∠ALW are the two roots (or a common root) of the SAME quadratic.]

**Step 4 (Root selection — the delicate gap).** Φ has two roots; Step 3 only shows {tan ∠AKW} ⊂ roots(Φ) ⊃ {tan ∠ALW}. To conclude ∠AKW = ∠ALW, rule out the crossed pairing. Candidate mechanisms:
  (a) Continuity/limit: as α → limiting value, K → M and L → N; in that limit the circle (AKL) → (AMN), which passes through W (check: (AMN) is the image of (ABC) under the homothety at A with ratio 1/2; W ∈ (AMN) ⟺ 2W − A ∈ (ABC), and 2W − A = (a − A_x, h) is the reflection of A in the perpendicular bisector of BC, which does lie on (ABC)). So the identity ∠AKW = ∠ALW holds at the endpoint; both sides are continuous in α, the two roots of Φ never collide (discriminant ≠ 0 — needs proof) on the α-interval, so the correct pairing persists.
  (b) Or: show the second root of Φ corresponds to the reflected/spurious configuration and violates a sign constraint (e.g. lies outside the admissible angle range).
GAP: make one of these airtight.

**Step 5 (Conclusion).** ∠AKW = ∠ALW with K, L on the same side of AW gives A, K, L, W concyclic (converse of the inscribed angle theorem), hence by Step 1, O ∈ V, hence OM = ON. ∎

## Key lemmas (claim + mechanism)
- Reformulation Lemma (W-equivalence) — reflection of A in the perp bisector of MN is W; a circle through A has centre on a line ℓ ∋ perp-bisector-direction iff it passes through the reflection of A in ℓ.
- Limit fact: (AMN) passes through W — homothety at A ratio 1/2 sends (ABC) to (AMN) and sends 2W − A (the reflection of A in the perpendicular bisector of BC, a point of (ABC)) to W.
- Resultant symmetry — the eliminant of the K-side data is B↔C symmetric, so both tangent values satisfy one common quadratic.

## Open gaps (for the builder)
1. Step 3: the resultant computation and its B↔C symmetry (heavy but mechanical; CAS-assisted, then displayed).
2. Step 4: root selection (the real mathematical content beyond fixed-point-t; if this resists, this approach is strictly harder than fixed-point-t and should be deprioritized).
3. Step 2's side-of-line justification.

## Cases to cover
- Isosceles AB = AC (Φ may degenerate — symmetric case is trivial directly, note it).
- Discriminant-zero locus of Φ in Step 4(a).

## Watch out for
- Do not silently assume the "natural" pairing of roots — that is exactly the gap.
- If Step 3/4 stalls, note that fixed-point-t proves the same reformulated statement (its point T is the centre; W = 2T − A reflection) — do not duplicate effort; this slug's value is a *shorter synthetic* proof, e.g. somebody finding a direct angle chase for ∠AKW = ∠ALW.

## Approaches tried
- (round 1) Outlined; reformulation and concyclicity verified numerically. Not yet built.

## Current best
Reformulation Lemma (Step 1) is complete modulo prose; rest is roadmap.
