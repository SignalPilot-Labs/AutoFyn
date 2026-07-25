## imo-2026-02

coordinate-bash-resultant-boundary: advance
Target: for every scalene triangle ABC, the midpoints M,N of AB,AC satisfy
OM=ON where O is the circumcenter of A,K,L (K,L defined by the three
hypothesis angle equalities of imo-2026-02) — i.e. the full original claim,
via the rotation parametrization (A=0,B=(a,0),C=(b,cc), Weierstrass
u=tan(β/2)), reduced (rounds 3-6, certified) to: genericity (closed),
magnitude bound (closed), and G2b full exclusion (open, this round's target).
Technique: resultant/Vieta elimination on the rotation parametrization,
now sharpened this round by a scale-invariant polar reparametrization
(AB=1, vertex angle A, m=AC) that turns the "G2b forbidden pattern
(Y,B2,Z)=(+,+,+)" into a clean 3-sinusoid/quadratic-in-m problem.
Skeleton:
  1. (already certified) Genericity: central identity O·(C−B)=(|C|²−|B|²)/4
     holds on G2a=G3a=0 for every triangle — `lemmas/symbolic-genericity-certificate.md`.
  2. (already certified) Branch G2a=G3a=0 is selected by the containment
     hypotheses at every β, and satisfies the magnitude bound —
     `lemmas/cross-product-sign-selection-G2a.md`, `lemmas/magnitude-bound-and-sign-coincidence.md`.
  3. (open, this round's focus) Exclude the extraneous branch G2b=G3b=0:
     show the forbidden sign pattern (Y,B2,Z)=(+,+,+) never occurs, using
     the certified trig identification `lemmas/yb2z-trig-identification.md`.
  4. Reparametrize by scale invariance: set AB=1, b=m·cosA, cc=m·sinA
     (m=AC>0, A=∠BAC). Then B2 = −2m·sin(A+3β) (single sinusoid — new,
     clean form this round), Y>0 ⟺ m<M0:=2cos²β/cosA (or all m>0 if
     cosA≤0), and Z's sign (after dividing by m>0) is the sign of
     Q(m):=m²sin(A+β) − 4m·sinβ − 4sin(A−β), a quadratic in m.
  5. Prove sin(A+β)>0 unconditionally on the whole domain (β<min(∠B,∠C),
     so A+β<A+∠B<π since ∠C>0 and A+∠B+∠C=π; also A+β>0) — this makes
     Q upward-opening always. [FULLY PROVED this round, 3 lines — certify
     immediately as a standalone reusable lemma.]
  6. Under hypothesis sin(A+3β)<0 (i.e. B2>0), show Q's discriminant ≥0
     (so Q has two real roots r1≤r2) — by a resultant/discriminant
     computation of Q's coefficients against sin(A+3β)<0's defining
     polynomial (same machinery as §§11-12 of this file).
  7. Show M0 ≤ r2 (the larger root) — by comparing Q(M0)'s sign (Q upward-
     opening + Q(M0)≤0 ⟹ M0 is between the roots or below r2) — needs the
     stalled closed form for Q(M0) simplified (try sum-to-product /
     product-to-sum by hand rather than blind sympy.simplify, or compare
     via the quadratic formula directly instead of eliminating m via M0).
  8. Handle the rarer subcase r1>0 (~2.6% of samples): show m>r1 always
     on the valid range — likely a simpler bound given r1>0 is rare and
     may follow from an explicit inequality on β,A.
  9. Conclude Z<0 whenever Y>0∧B2>0, i.e. (Y,B2,Z)=(+,+,+) is impossible,
     closing G2b's exclusion and hence the whole branch-selection gap for
     this route.
Key lemmas (claim + mechanism):
  - sin(A+β)>0 always — because β<∠B and A+∠B+∠C=π with ∠C>0, so A+β<π,
    combined with A+β>0. [Proved, ready to certify.]
  - B2 ∝ −sin(A+3β) — because B2/(1+u²)³=−2(b·sin3β+cc·cos3β) and
    b=m cosA, cc=m sinA gives b sin3β+cc cos3β = m·cos(3β−A)... [note:
    re-derive/verify the exact angle-sum identity carefully; the explorer
    reports B2=−2m sin(A+3β), builder must re-verify this substitution
    symbolically before using it, since a sign/angle-argument slip here
    would invalidate steps 4-9].
  - Q(m)'s sign classification reduces the whole conditional inequality to
    two root-comparison facts (M0≤r2; m>r1 when r1>0) — because Q is an
    explicit quadratic and Y>0/Z<0 are literally "m below M0" / "m outside
    [r1,r2]".
Open gaps: discriminant≥0 under sin(A+3β)<0 (step 6); M0≤r2 (step 7,
including the stalled Q(M0) simplification); the r1>0 subcase (step 8).
Cases to cover: cosA>0 vs cosA≤0 (changes whether Y>0 is a bound on m or
automatic); r1≤0 vs r1>0 (rare subcase, ~2.6% of samples).
Watch out for: the builder must independently re-verify the explorer's
B2=−2m sin(A+3β) claim symbolically (not just trust the report) before
building on it — this is the linchpin of the whole reparametrization; also
must not silently assume Q always has two real roots without proving the
discriminant fact (step 6) first, since that's logically prior to steps 7-8.

coordinate-bash-resultant-boundary-pointwise: advance
Target: same as above (OM=ON, full problem), via the pointwise 4-condition
branch-selection reformulation (Lemma P1/P2): exactly one candidate root of
a degree-4-in-s2 polynomial survives four joint conditions (2,3,4-containment
+ true-equation matching). Now additionally must resolve the newly-surfaced
G2a-side same-root correlation gap (does the L1<0-selected root of G2a also
satisfy the true, non-supplementary equation W>0?).
Technique: same resultant/Vieta machinery as the sibling, PLUS this round's
new lead: reframe the G2a same-root correlation as a "two lines in ℂ"
question via complex-affine functions of s2.
Skeleton:
  1. (already certified) Lemma P1/P2: exact translation of the four
     geometric conditions into algebraic form on the degree-4 polynomial —
     `lemmas/pointwise-branch-selection-criterion.md`.
  2. (already certified, this round) Structural quartic identification
     (Q)=−(b²+cc²)²(u²+1)/[16(u²+1)⁶]·G2a·G2b, and the new parity lemma
     W(r1)W(r2)≤0 on G2a's two roots — `lemmas/g2a-true-supplementary-parity-and-quartic-identification.md`.
  3. (open, this round's priority) Prove the L1<0-selected root of G2a also
     satisfies W>0 (matched sign / "true equation"), by the complex-affine
     "two lines in ℂ" reframing: L1(s2)=Im(d̄·V1(s2)) and DK(s2)∝Re(d̄·V1(s2))
     are the imaginary/real parts of a single complex-affine function
     W1(s2)=d̄·V1(s2) of the real parameter s2, so as s2 ranges over ℝ,
     W1(s2) traces a straight line in ℂ; "L1<0 ∧ DK>0" is exactly "W1(s2)
     lands in the open region {Im<0, Re>0}" — determined by where this
     line crosses the coordinate axes (the zero loci of L1, DK, already
     known) and its direction (a fixed complex number, the "velocity"
     d̄·(coefficient of s2 in V1)). Similarly frame DN via a second
     complex-affine function W2(s2)=V̄4·V3(s2) (V3=L−N affine, V4=C−N
     constant).
  4. Derive, from the two lines' explicit slopes/intercepts (in terms of
     the triangle data and β), an explicit closed-form criterion for when
     the L1<0-selected s2 lands in the region making W>0, and show this
     criterion is always satisfied under the problem's hypotheses (via a
     sign/quadrant argument on the two lines' directions, not resultant
     algebra) — genuinely a different technique in kind from the
     both-roots-product resultant trick already shown insufficient.
  5. Conclude exactly one root survives all four conditions, closing
     branch selection for this route.
Key lemmas (claim + mechanism):
  - L1, DK are literally Im/Re of one complex-affine function of s2 —
    because L1 = cross-product and DK = dot-product of the same two
    vectors (d(β), L−B), and cross/dot of the same vector pair are exactly
    Im/Re of the product of one with the conjugate of the other.
  - The "both-roots-product via resultant" trick (used for the already-
    proved W(r1)W(r2)≤0) cannot resolve a same-root question — because
    the target condition is on a single distinguished root (selected by
    L1<0), not a symmetric function of both roots; already confirmed this
    round (degree-20 unfactorable remainder from the direct extension
    attempt) — do not retry that extension.
Open gaps: step 3-4, the complex-affine-line criterion itself (untried,
new this round) — must be built from scratch, no prior partial work exists.
Cases to cover: none new beyond the existing G2a/G2b split; if step 3
succeeds it subsumes the numeric-only 377+15-sample same-root claim.
Watch out for: do not re-attempt the both-roots-product resultant-ratio
extension (confirmed dead end, degree-20 unfactorable, this round) — the
complex-affine-line idea is a genuinely different technique, not a variant
of it. Also confirm the two complex-affine functions' "velocity" directions
are computed from the correct (not conjugated) vector definitions — a sign
slip here would silently invalidate the quadrant argument.

fixed-point-concyclic: advance
Target: same as above (OM=ON / A,K,L,Q concyclic), via the bilinear complex
cross-ratio / Cramer's-rule machinery (Theorem 6/7: χ=−D0/D1), reduced to
proving Rem(H1,H2,H3,B,C)=0 on the genuine geometric branch (H1,H2,H3 the
real hypothesis-ratio values, degree 2 each in Rem).
Technique: same underlying resultant/elimination toolkit as the coordinate
route, now explicitly reframed (per this round's finding) as substituting
the coordinate route's already-derived rational parametrization K(θ),L(θ)
(equivalently u,t1,s2) into H1,H2,H3's definitions and checking whether the
resulting Rem, as a polynomial in the shared parameter, is a multiple of
already-certified G2a/G3a/T — i.e. testing whether this route's gap is a
formal corollary of `lemmas/symbolic-genericity-certificate.md`, not new
content.
Skeleton:
  1. (already certified) Theorem 6: Δ=BC(1−h2h3)/4, D_pΔ=D_KD_L
     (Cramer's-rule compatibility) — `lemmas/bilinear-chi-cramer-formula.md`.
  2. (already certified) Theorem 7: χ=−D0/D1 exact closed form.
  3. (this round's task, per explorer finding 1) Take the coordinate
     route's explicit rational parametrization of K,L in terms of u=tan(β/2)
     and t1,s2 (the G2a/G3a-branch solutions) — already fully derived and
     certified via `lemmas/symbolic-genericity-certificate.md` — and
     substitute into H1(K,L),H2(K,L),H3(K,L) to get h1(u),h2(u),h3(u) as
     explicit rational functions of u (and the triangle data a,b,cc).
  4. Substitute h1(u),h2(u),h3(u) into Rem's displayed polynomial (degree 2
     in each hi) to obtain Rem(u) as a single-variable rational function.
  5. Test (sympy, resultant/gcd) whether Rem(u)'s numerator, restricted to
     the branch G2a=G3a=0, is IDENTICALLY zero (i.e. Rem(u) reduces to 0
     modulo the ideal ⟨G2a,G3a⟩, the same Gröbner-basis test already used
     for the central identity T in `lemmas/symbolic-genericity-certificate.md`).
  6a. If Rem(u) ≡ 0 mod ⟨G2a,G3a⟩: Rem=0 is a FORMAL COROLLARY of the
     already-certified genericity certificate — this route's gap closes
     immediately, needing only the translation lemma (step 3-5) as new
     content. This would be a major result: three approaches' gaps
     (G2b exclusion, G2a same-root correlation, Rem=0) would collapse to
     "already proved," since G2a=G3a=0 is exactly the branch selected by
     the already-certified containment/magnitude-bound theorems.
  6b. If Rem(u) is NOT in the ideal ⟨G2a,G3a⟩ (nonzero remainder): this
     confirms (per explorer finding 4) that Rem=0 needs genuinely separate
     content beyond the already-proved genericity certificate — report
     honestly, and the remaining task becomes proving Rem(u)=0 directly as
     a new sign/root fact on the branch, structurally parallel to the
     coordinate route's own G2b exclusion.
  7. Before either 6a/6b, independently re-run a careful (≥100 sample,
     arg-based not arccos-based angle formulas, checked for fsolve
     convergence) numeric sweep of Rem along the true geometric branch —
     current evidence (3 successful samples) is too thin, per this round's
     finding 3 (the explorer's own quick replication got Rem≈−3.12, likely
     a setup bug, but the discrepancy must be resolved before trusting the
     conjecture further).
Key lemmas (claim + mechanism):
  - Φ=0 (Theorem 6) is a tautology for ANY K,L, not a constraint — because
    it's an algebraic identity from Cramer's rule alone, so it carries no
    geometric content; the real content is in the specific rational
    functions h_i(u) once K,L are substituted with their geometric,
    branch-selected values — this is why step 3-5 (not more Φ-algebra) is
    the right next move.
  - If successful, step 6a would be the single biggest possible win this
    round: it converts three routes' distinct-looking gaps into one already-
    solved fact, since G2a=G3a=0 is the branch the coordinate route has
    already fully validated (containment + magnitude bound, rounds 5-6).
Open gaps: the entire substitution-and-ideal-membership test (steps 3-6) is
new and untried; the numeric re-validation (step 7) is also unfinished/thin.
Cases to cover: none beyond the standard genericity domain (scalene
triangle, K≠L).
Watch out for: Δ=0 (h2h3=1) as a possible non-degeneracy failure of the
Cramer's-rule division defining χ — check (cheaply) whether it can occur on
the genuine branch before trusting χ=−D0/D1 pointwise; also use the
σ-antisymmetry check (Rem+σ(Rem)=0, σ: B↔C,h2↔h3) as a free regression
test on any re-derivation of Rem. Do not re-attempt "Rem=0 follows from
Φ=0 plus bare realness alone" — confirmed dead end twice now (round 7 and
this round, independently).

inversion-at-A-collinearity: new
Target: same as above (A,K,L,Q concyclic, hence OM=ON), via a genuinely
different top-level reduction: apply inversion centered at A (any fixed
radius r) to the whole configuration. Since A,K,L,Q concyclic through A
inverts to K*,L*,Q* being COLLINEAR (a circle through the center of
inversion maps to a line not through the center), the target becomes a
pure linear-algebra/determinant statement: det[K*−L*, Q*−L*] = 0 (as
vectors), instead of a "cross-ratio ∈ ℝ" realness statement.
Technique: inversion (classical, per knowledge_base.md's synthetic
toolkit entry on power of a point/inversion/spiral similarity), combined
with `fixed-point-concyclic`'s already-certified bilinear Cramer's-rule
apparatus (Theorem 6/7) — reuse its H1,H2,H3 hypothesis encodings and its
Q construction, but reformulate the FINAL target as collinearity of the
inverted images rather than cross-ratio realness.
Skeleton:
  1. Import `fixed-point-concyclic`'s certified constructions: Q (reflection
     of A in the perpendicular bisector of MN, `lemmas/amnq-concyclic-and-reduction.md`),
     and the closed forms for K,L as functions of the hypothesis parameters.
  2. Apply inversion ι centered at A, radius r=1 (WLOG, since the
     collinearity target is scale-invariant): K*=K̄/|K|² (in complex-number
     coordinates with A=0), similarly L*,Q* (all well-defined since
     K,L,Q≠A generically).
  3. Show A,K,L,Q concyclic ⟺ K*,L*,Q* collinear — standard inversion fact
     (a circle through the inversion center maps to a line); state and cite
     this classical lemma explicitly with a short proof (cross-ratio
     (A,K;L,Q) real ⟺ (K*,L*,Q*) collinear, via the Möbius map z↦1/z̄ or
     z↦1/z composed with conjugation — needs care about which inversion
     convention preserves/reverses orientation, but collinearity is
     insensitive to that).
  4. Express K*,L*,Q* explicitly in terms of the triangle data and the
     hypothesis parameter(s) (reusing the already-certified rational
     parametrizations from the coordinate route or fixed-point-concyclic's
     own h_i-based forms).
  5. Reduce collinearity to a single determinant/cross-product identity:
     Im[(L*−K*)·conj(Q*−K*)] = 0, and attempt to show this is EITHER (a) a
     direct polynomial identity on the already-certified branch G2a=G3a=0
     (testable the same way as the fixed-point-concyclic advance's step 5
     above — if so, this may ALSO reduce to a corollary of the genericity
     certificate, giving a second independent check on that possibility),
     OR (b) a genuinely new, smaller-looking target if the inverted
     coordinates simplify the algebra (e.g. rational functions of lower
     degree than the un-inverted h_i's).
Key lemmas (claim + mechanism):
  - Concyclic-through-center ⟺ inverted images collinear — because
    inversion is a Möbius transformation and circles/lines through the
    pole map to lines (classical fact, short proof via z↦1/z̄).
  - This reformulation does not obviously reduce difficulty (the explorer
    flagged this honestly) — its value is diversity (a determinant target
    instead of a realness target) and the chance that inverted coordinates
    happen to simplify algebraically; must be evaluated empirically before
    investing heavily.
Open gaps: everything past step 1 is untried; step 5's outcome (whether
inversion actually simplifies the algebra, or just restates the same
difficulty in new coordinates) is unknown and must be checked early
(cheap sympy substitution) before committing further effort.
Cases to cover: none beyond standard genericity (K,L,Q≠A).
Watch out for: per the explorer's own honest caveat, this is NOT known to
be easier than the cross-ratio form — abandon quickly (within this round)
if step 5's determinant does not visibly simplify relative to Rem/Φ,
rather than sinking further effort into re-deriving the same difficulty in
new coordinates. Also double check orientation conventions in the
inversion map (z↦1/z̄ vs 1/z) since collinearity itself is orientation-
insensitive but intermediate sign computations are not.

Dormant this round (no new lever, per dispatch instructions): ptolemy-trig-identity,
ptolemy-trig-identity-parity-decomposition, ptolemy-trig-identity-synthetic,
coordinate-bash, coordinate-bash-resultant, power-of-point-secants,
spiral-similarity-bootstrap. All have either fully-closed sub-goals folded
into the population's shared "Current best," or two already-pruned levers
with no new idea surfaced this round.
