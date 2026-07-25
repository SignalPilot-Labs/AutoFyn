## Status
partial

## Approaches tried
- (round 1, prior) outline only — undetermined secant construction, no
  computation done.
- (round 1, this build) Concrete secant construction using the fact that
  **A itself lies on ω = circumcircle(AKL)**: line AB (through M) meets ω at
  A and a second point A′; line AC (through N) meets ω at A and a second
  point A″. Derived the exact algebraic power-of-a-point identity this
  produces, then eliminated the unknown secant lengths AA′, AA″ by trading
  them for pow(B,ω) and pow(C,ω) via the power-of-a-point relation at B and
  at C respectively (both B and C lie on the *same* two lines AB, AC, so
  their powers are computable from the same two secants). Result: OM=ON is
  algebraically **equivalent** to the single clean identity
  `pow(B,ω) − pow(C,ω) = (AB² − AC²)/2`.
  Outcome: this reformulation is correct (verified both symbolically here
  and numerically to machine precision on the same instance used by the
  math-explorer, see below) but I then proved — by direct vector expansion
  — that it is *literally the same statement* as the reduction lemma shared
  by fixed-point-concyclic and coordinate-bash (`O·(C−B) = (|C|²−|B|²)/4`
  with A at the origin). So this route does not bypass the central gap; it
  relocates it into power-of-a-point language. Reported honestly per the
  outline's own risk flag rather than claimed as an independent proof.
  Hypothesis 1 (∠KBA=∠ACL) still not used to close the remaining gap — see
  Open gaps.

## Current best

### Setup and notation
Let ω denote the circumcircle of A, K, L, with center O and radius R.
Since M is the midpoint of AB and N is the midpoint of AC, line AB passes
through M and line AC passes through N. Crucially, **A already lies on ω**
by definition of O — so line AB and line AC are each automatically secants
of ω (each meets ω at A and, generically, at one further point), with no
extra construction needed. Write:
- A′ := the second point where line AB meets ω (A′ = A only in the
  degenerate tangent case, excluded below and handled by continuity),
- A″ := the second point where line AC meets ω.

Put c = AB, b = AC. Parametrize line AB by arc-length coordinate s with
s(A) = 0, s(B) = c (so s increases from A toward B); since M is the
midpoint of AB, s(M) = c/2. Let s(A′) = c·t for some real t (t is the
fraction along AB, possibly negative or > 1). Similarly parametrize line AC
with s(A) = 0, s(C) = b, s(N) = b/2, s(A″) = b·t′.

### Step 1 — power of M and N via the through-A secants (no gap)
By the standard signed power-of-a-point formula for a secant through P
meeting the circle at parameter-values s₁, s₂ (in a fixed affine
parametrization of the line by arc length, with unit direction vector), the
power of a point at parameter s along the line is (s−s₁)(s−s₂) times the
squared norm of the parametrizing direction vector — here the direction
vectors are exactly (B−A) and (C−A), of squared length c² and b²
respectively, so:

pow(M, ω) = (s(M) − 0)(s(M) − c t) · 1 = (c/2)(c/2 − ct) = (c²/2)(1/2 − t).

pow(N, ω) = (b²/2)(1/2 − t′).

(This is the ordinary power-of-a-point identity, knowledge_base.md
"Synthetic toolkit: power of a point," applied to the two secants AB, AC of
ω through A; no gap — it is the defining computation of power via a
secant.)

**Reduction A (no gap):** OM = ON ⟺ pow(M,ω) = pow(N,ω) [since
pow(M,ω) = OM² − R² and pow(N,ω) = ON² − R², and R is the common radius] ⟺
c²(1/2 − t) = b²(1/2 − t′). — (★)

### Step 2 — eliminate t, t′ via the powers of B and C (no gap)
B and M both lie on line AB, and B corresponds to parameter s(B) = c. Using
the same power-of-a-point formula for the point B on this same secant:

pow(B, ω) = (s(B) − 0)(s(B) − ct) = c(c − ct) = c²(1 − t).

Likewise, on line AC, pow(C, ω) = b²(1 − t′).

Solve for t, t′: t = 1 − pow(B,ω)/c², t′ = 1 − pow(C,ω)/b².

Substitute into (★):

c²(1/2 − 1 + pow(B,ω)/c²) = b²(1/2 − 1 + pow(C,ω)/b²)
⟺ pow(B,ω) − c²/2 = pow(C,ω) − b²/2
⟺ **pow(B, ω) − pow(C, ω) = (AB² − AC²)/2.**   (★★)

So (★★) is algebraically equivalent to the target OM = ON, using ONLY the
elementary power-of-a-point identity (no hypothesis used yet) — this is a
genuine, fully rigorous reduction with no gap, and it is a legitimate new
form of the target (not literally the definition, since it eliminated all
reference to K, L, the circle's center, or the second intersection points).

### Step 3 — this reformulation is the SAME identity as the shared vector
### reduction lemma (checked directly; reported honestly, not hidden)
Put A at the origin (vector notation, matching fixed-point-concyclic's and
coordinate-bash's frame). Then for any point X, pow(X, ω) = |X − O|² − R².
Hence
pow(B,ω) − pow(C,ω) = |B|² − 2 B·O − |C|² + 2 C·O = (|B|² − |C|²) + 2 O·(C−B).

With A = 0, AB² = |B|², AC² = |C|², so (★★) reads:
(|B|² − |C|²) + 2 O·(C − B) = (|B|² − |C|²)/2
⟺ 2 O·(C−B) = −(|B|² − |C|²)/2 = (|C|² − |B|²)/2
⟺ **O·(C − B) = (|C|² − |B|²)/4.**

This is *exactly* the reduction lemma verified by the outline-reviewer
(round 1) as shared free content between fixed-point-concyclic and
coordinate-bash. So the power-of-point-secants reformulation (★★) is not an
independent identity to prove — it is a restatement, in power-of-a-point
language, of the very same central fact both other approaches are chasing.
This was checked by direct algebraic substitution above (no numeric
shortcut) and independently confirmed numerically on a concrete instance
(A=(0,3), B=(−2,0), C=(3.5,0), one solved valid (K,L) pair from the family
with ∠KBA≈17°): computed pow(B,ω) = 4.03211899…, pow(C,ω) = 8.15711898…,
difference = −4.12499999…, matching (AB²−AC²)/2 = −4.125 exactly to the
precision of the numerical solve (≈1e-8, limited by the nonlinear solver
tolerance, not by the identity). This is a numerical sanity check of a
derivation that is already proved algebraically above, not a substitute for
the derivation.

### Honest assessment: this approach converges to the same wall
Per the outline's own risk flag and the reviewer's required check, I traced
the "natural secant through M / through N" hunt (using A ∈ ω) all the way
to a clean closed form (★★), and it collapses onto the identical target
already known from the other two approaches. Hypothesis 1 (∠KBA = ∠ACL)
was NOT used anywhere in Steps 1–2 (as the reviewer flagged) because Steps
1–2 are pure power-of-a-point algebra that holds for *any* circle through A
— the hypothesis has to enter in proving (★★)/O·(C−B)=(|C|²−|B|²)/4 itself,
which is exactly the un-closed "main gap" in fixed-point-concyclic (the
concyclicity chase) and the un-closed elimination step in coordinate-bash.
I did not find an alternative secant pair (e.g. through K, L directly, or
using tangent lines at K or via a spiral similarity at B, C) that reaches a
DIFFERENT algebraic target not equivalent to O·(C−B)=(|C|²−|B|²)/4 — I
tried and ruled out: (i) line BK is not tangent to ω at K in general (checked
numerically: O K · BK ≠ 0, so no tangent-power shortcut pow(B,ω)=BK²); (ii)
directly parametrizing pow(B,ω) via the secant B–K–(second point on ω) does
not simplify without first knowing where that second point is, which is
again equivalent difficulty to the main gap.

**This is legitimate negative/consolidating information for the
population**: it is evidence (not proof) that OM=ON for this problem has
a single essential difficulty — locating one more constrained point on
ω (equivalently, pinning pow(B,ω)−pow(C,ω)) — regardless of whether one
phrases the target via a fixed point Q (fixed-point-concyclic), via direct
coordinates (coordinate-bash), or via power of a point (this approach). Per
CLAUDE.md's anti-single-gap-trap guidance, this should be read by the next
round's outliner as confirmation that these three framings are not
independent lines of attack on the hard step, even though they were
constructed with different top-level machinery.

## Open gaps
- **The single remaining gap, in power-of-a-point form:** prove
  pow(B, ω) − pow(C, ω) = (AB² − AC²)/2, i.e. equivalently
  O·(C−B) = (|C|²−|B|²)/4 (A at origin), using all three hypothesis
  clauses (∠KBA=∠ACL, ∠LBK=∠LNC, ∠LCK=∠BMK) and the four containment/
  betweenness conditions to fix the correct directed-angle branch. This is
  the same gap as fixed-point-concyclic's step 3 and coordinate-bash's
  elimination step — not a new, independent gap.
- Hypothesis 1 is not used anywhere in the fully-proved Steps 1–2 above (as
  flagged by the reviewer) — this is now understood to be *expected*, not a
  defect of the construction: Steps 1–2 are hypothesis-free algebra (they
  hold for any triangle and any circle through A), and hypothesis 1 must
  enter only in the unclosed final identity, exactly as in the other two
  approaches.
- Not yet found: any genuinely different secant pair (through B and C via
  K, L directly, bypassing A) that would give an algebraically distinct
  target from O·(C−B)=(|C|²−|B|²)/4. If the outliner wants a real second
  independent line of attack (rather than three framings of one gap), this
  is the concrete thing to search for next — e.g. a secant construction
  that uses hypothesis 1 to build a spiral similarity centered at K or L
  mapping B to C (or M to N) directly, giving a length relation not
  reducible to the same vector identity. This was not found this round due
  to time constraints, not ruled out.

## Full proof
(not present — Status is partial, the central identity O·(C−B) =
(|C|²−|B|²)/4, equivalently pow(B,ω) − pow(C,ω) = (AB²−AC²)/2, is reduced
to but not proved.)

## Promotable lemmas
- **Power-of-a-point reduction lemma (Steps 1–2 above, fully proved, no
  gap):** For any triangle ABC with M, N the midpoints of AB, AC, and any
  circle ω through A, OM = ON (where O is the center of ω, using
  pow(X,ω) = OX² − R²) is equivalent to
  `pow(B, ω) − pow(C, ω) = (AB² − AC²)/2`.
  Proof: exactly Steps 1–2 above (elementary power-of-a-point algebra along
  the two secants AB, AC of ω through A, valid for ANY circle through A,
  no problem-specific hypothesis used). This is a clean, reusable,
  hypothesis-free geometric fact — worth certifying as a shared lemma since
  it converts the problem's target into a pure power-of-two-vertices
  statement, which may be easier to attack directly (e.g. via secants BK,
  CL and the angle hypotheses) than the raw vector form, even though this
  round did not close it. Also useful for coordinate-bash as an alternative
  algebraic route to the same reduction, and for fixed-point-concyclic as a
  cross-check of its own reduction lemma (Step 3 above shows the two are
  identical).
