## imo-2026-02

All three approaches below are **advance** on live approach files. No new
top-level framing is proposed this round: the population's fresh-framing
search has been exhaustively negative 4+ times (rounds 3,5,8,9,10, reconfirmed
structurally round 8 — every route provably reduces to the same underlying
branch-selection/positivity core), and each of the three routes below has
genuine NEW, not-yet-exploited leverage this round (per the three explorer
reports), so per CLAUDE.md's own guidance ("keep pushing the two/three live
sub-case formulations directly" — rounds 10-14 annotations) this is the
correct move, not a stall requiring reframe. `coordinate-bash-resultant-
boundary-pointwise-tangent-twopoint` remains dormant (deprioritized since
round 13, structurally stranded behind its sibling's full 2D result; no new
relevance surfaced this round) — not revived.

---

coordinate-bash-resultant-boundary-pointwise-tangent: advance
Target: OM=ON for every triangle ABC (the problem's actual claim), via this
route's full chain: central identity (proved, all triangles) + branch
selection reduced to Tgt(A,B)>0 on domain D + (this round's target) global
minimality of the corner (π/3,π/3).
Technique: 2D global-minimum classification via boundary-curve reduction +
interior-critical-point elimination (reduces a 2-variable inequality to two
1-variable ones), reusing the already-certified local structure
(D2(π/3,π/3)≠0, strict local min via tangent cone) as the base case.
Skeleton:
  1. (already certified) Tgt(π/3,π/3) = (9/4)D2(π/3,π/3)², D2(π/3,π/3)≤-0.8
     exactly (rational Taylor+Archimedes bound) — corner value is a genuine
     positive number ≈1.574, not a degenerate vanishing point.
  2. (already certified) (π/3,π/3) is a strict LOCAL min of Tgt on D via a
     tangent-cone/directional-derivative argument (both boundary curves
     meet there with exact rational slopes -1/2, 1/4; min directional
     derivative ≈3.5>0).
  3. NEW — prove Tgt has no interior critical point in the open domain D:
     eliminate ∂Tgt/∂A=∂Tgt/∂B=0 via resultant/Gröbner elimination combined
     with the domain's own polynomial inequalities (n1,n2,n4-style encodings
     already built by the -sos sibling are candidate reusable machinery for
     expressing "inside D" polynomially). fsolve evidence (2000 restarts):
     only 3 unconstrained critical points exist, all provably outside D
     (one is a near-zero of Tgt itself, consistent with Tgt/Ψ not being
     globally positive off-domain; the other two sit at Tgt≈3.15, both fail
     domain membership).
  4. NEW — restrict Tgt to the boundary ∂D = 𝒞_hi ∪ 𝒞_lo (𝒞_hi: B=(π-A)/2 the
     B=C edge; 𝒞_lo: X0(A,B)=cos²B the implicit containment edge), reducing
     to two 1-variable inequalities:
     4a. On 𝒞_lo: show Tgt|_{𝒞_lo} is monotone DECREASING in A toward the
         corner over its whole valid range — reuse the certified
         ∂X0/∂B=sinA cosA/(2sin²(A+B))>0 (lemmas/x0-partial-b-derivative.md)
         to compute d/dA of Tgt restricted to the implicit curve via the
         implicit function theorem. Strong numeric support (comfortable
         margin, range 2.366→1.5815 approaching the corner value 1.57414).
     4b. On 𝒞_hi: Tgt|_{𝒞_hi} is NOT globally monotone (rises to a local max
         ≈2.18 near A≈0.8, then falls toward the corner) — the argument must
         be "the minimum over the valid sub-range is attained at the
         corner-adjacent endpoint," via a 1-variable critical-point
         classification of Tgt|_{𝒞_hi}(A) (d/dA=0, elementary or via the
         same elimination toolkit as step 3) rather than naive monotonicity.
  5. Combine 3+4: no interior critical point (3) plus boundary minimum at
     the corner in both pieces (4a, 4b) ⟹ global min of Tgt on D is at
     (π/3,π/3), value ≈1.574>0, hence Tgt>0 throughout D ⟹ branch selection
     closed ⟹ OM=ON follows via the already-proved central identity chain.
Key lemmas (claim + mechanism):
  - No interior critical point in D — because the unconstrained ∇Tgt=0
    system has only 3 solutions (an algebraic fact provable via resultant
    elimination of the 2×2 gradient system), all of which fail the domain's
    polynomial membership tests.
  - Tgt|_{𝒞_lo} monotone decreasing — because the implicit-curve slope
    dB/dA (from ∂X0/∂B, already certified) combined with the explicit
    A-dependence of Tgt has one sign throughout the curve's valid range.
  - Tgt|_{𝒞_hi} attains its sub-range minimum at the corner-adjacent
    endpoint — because its only interior critical point (if any, via 1-var
    elimination) is a local MAX not a min (matches the observed shape:
    rises then falls), so the minimum is necessarily at an endpoint, and the
    far endpoint (A≈0.558, value≈1.96) is comfortably above the corner value.
Open gaps: all of steps 3, 4a, 4b are currently numeric-only (fsolve
restarts, boundary scans) — no symbolic proof yet for any of the three.
Cases to cover: the two boundary pieces (𝒞_hi, 𝒞_lo) plus the interior — all
three explicitly enumerated above; do not omit the interior-critical-point
step (a common failure mode: proving boundary positivity alone does not
rule out an interior minimum below it).
Watch out for: (i) the 𝒞_hi margin is UNUSUALLY TIGHT (≈0.0008, the tightest
numeric margin anywhere in this population's history) — per the explorer's
explicit flag, get an independent HIGH-PRECISION (mpmath, ≥30 digits)
re-verification of this specific sub-claim before investing heavy symbolic
effort assuming a comfortable margin; if the margin turns out negative or
zero under higher precision, this whole sub-approach's target statement
needs revision, not just a harder proof. (ii) any boundary-curve scan MUST
enforce all three domain inequalities simultaneously (B>β0(A), B≤C,
cos²B<X0<cos²β0(A)) — a naive single-constraint scan gives spurious
sub-corner values (explorer explicitly reproduced this pitfall on 𝒞_hi at
A=0.42, value 1.464<corner, which vanishes once the full domain is enforced).

---

coordinate-bash-resultant-boundary: advance
Target: OM=ON for every triangle ABC, via this route's chain: central
identity (proved) + parity-obstruction-guided Positivstellensatz certificate
for -q1,-r0 on the true residual domain (Case (b) ∧ P>0 ∧ E<0).
Technique: linear Positivstellensatz search over a graded generator basis
(reduces to exact rational linear algebra / LP feasibility, not numeric
fitting), guided by the (Z2)^4-parity structure already proved to constrain
which generators can possibly appear.
Skeleton:
  1. (already certified) q1,r0 live in the graded piece disjoint from
     {G0,E_num,Num} (round 13 parity theorem) — any certificate needs either
     a bare odd-c/d multiplier (round 13-14 recipe) or a same-graded-piece
     PRODUCT of two odd-graded generators (this round's new mechanism).
  2. NEW — adopt the wider basis found this round: the two degree-6 products
     G0·Enum, G0·Num (both proved sign-definite on the true 8729-point
     domain sample, land in R_00 automatically with no multiplier needed,
     exact degree match to q1's own degree 6) plus the existing B1,B4,B6.
  3. NEW — since {B1,-B2,B4,B6,G0Enum,G0Num} alone leaves -q1 outside even
     the UNSIGNED span (exact rank test, rank 20 vs 21) and adding B3,B5
     still leaves it outside (rank 21 vs 22), apply the "multiply the
     target by a known-positive domain slack" trick: -q1·(1-σ) and
     -q1·(1-τ) both land IN the unsigned span at degree 7 using the 9-element
     set {B1,-B2,B3,B4,B5,B6,G0Enum,G0Num,EnumNum} — the span obstruction is
     fixed, but the resulting LP (nonnegativity-constrained combination) is
     still infeasible with THESE exact coefficients. Try alternative positive
     multipliers next: τ(1-σ), σ(1-τ), or (ct-sd) if provably sign-definite,
     with the same 9-generator set, before concluding infeasibility more
     broadly.
  4. NEW (structural finding, must be respected) — r0 is structurally harder
     than q1 for this generator family: -r0 (degree 7, no multiplier) is
     NOT in the unsigned span of the 9-generator set (rank 29 vs 30), and
     -r0·σ (degree 8) with the 35-generator pairwise-product-extended set is
     ALSO not in the span (rank 38 vs 39). Do not assume q1's eventual
     certificate transfers to r0 — dedicate separate generator-search effort
     to r0 (e.g. is there an r0-analogue of G0·Enum built from a different
     generator pairing, or does r0 need a genuinely new base generator beyond
     {G0,Enum,Num,Bc}?).
Key lemmas (claim + mechanism):
  - G0·Enum, G0·Num are sign-definite (>0) on the true residual domain —
    because each factor lives in the odd-graded piece R_10⊕R_01, so their
    product is forced into R_00 (the target's graded piece) with no extra
    multiplier, and both factors individually have already-established or
    numerically-confirmed consistent sign on the domain (G0>0, Enum<0
    combined with Num<0 gives G0·Num>0 in the sign convention used).
  - -q1·(1-σ), -q1·(1-τ) enter the unsigned span at degree 7 (an exact
    linear-algebra fact, not numeric) — because multiplying by the
    trivially-nonnegative slack (1-σ) or (1-τ) shifts the target's monomial
    support enough to be reachable by the 9-generator set's degree-7
    monomial multiples, even though the un-multiplied target at degree 6 is
    not reachable.
Open gaps: the actual nonneg-coefficient certificate for either q1 or r0 is
still NOT found — step 3's LP is infeasible with the exact multipliers tried
so far (needs a different positive multiplier or an additional generator);
step 4's r0 gap is open and explicitly flagged as needing independent
generator work, not a byproduct of closing q1.
Cases to cover: q1<0 and r0<0 must each be established (both needed for the
termwise-sufficient decomposition of T≥0 on the residual sub-domain) — do
not treat closing q1 alone as closing the route.
Watch out for: do not retry the already-ruled-out combinations (B1,B4,B6
alone; the 6-generator set without B3/B5; (1-σ)/(1-τ) multiplier with
EXACTLY the current 9-generator set) — these are exact (not numeric-fit)
negative results this round, recorded as dead ends below.

---

coordinate-bash-resultant-boundary-pointwise-sos: advance
Target: OM=ON for every triangle ABC, via this route's chain: central
identity (proved) + denominators positive (Theorem 1, proved) + Case (b)
domain fully polynomially encoded + (this round's target) Num≥0 via a
3-generator Positivstellensatz certificate.
Technique: Positivstellensatz/SOS certificate search in a plain polynomial
ring (no algebraic extension), enabled by this round's simplification of the
n4 domain-encoding generator.
Skeleton:
  1. NEW — prove n4≥0 ⟺ n4sq≥0 unconditionally on Case (b)'s domain, where
     n4sq := (1+u²)³cos²B − u²(3−u²)² is a PLAIN polynomial in (u,cosB) with
     no √(1+u²) extension needed. Mechanism: on Case (b)'s domain, B<π/2
     unconditionally (since B≤C and A+B+C=π with A>0 force B+C<π, so
     B≥π/2∧B≤C would give B+C≥π, contradiction), so cosB>0; also
     u∈(0,2−√3)⊂(0,√3) gives u>0 and 3−u²>0; hence n4=w³cosB−u(3−u²)
     compares two NONNEGATIVE quantities w³cosB≥0 and u(3−u²)>0, so squaring
     (which eliminates w via w²=1+u²) is a valid iff on this sign-restricted
     comparison. This is close to a complete 3-line proof already — write it
     out fully and have the builder verify the B<π/2 sub-argument and the
     u-range facts are each already-established or trivially provable from
     existing domain definitions.
  2. Replace the 4-generator (n1,n2,n4-via-w) ansatz with the 3-generator
     ansatz Num = σ0 + λ1·n1 + λ2·n2 + λ3·n4sq, entirely in the plain ring
     ℚ(√3)[u,cosB,sinB] — no extension ring, no w-elimination bookkeeping.
  3. First RESOLVE the coefficient-conditioning discrepancy this round's
     explorer flagged (own rescaled-Num dynamic range ≈7×10^10 vs round 13's
     claimed ≈3×10^{-29}–24) before trusting any further SDP numerics — pin
     down exactly which polynomial/normalization round 13's number referred
     to, or redo the rescaling consistently, so future SDP runs are
     comparable across rounds.
  4. Run the 3-generator SDP (multiple bases: monomial, Chebyshev-on-rescaled-
     s) with the conditioning resolved; if a numerically "solved" (not just
     optimal_inaccurate) SDP is obtained, extract the Gram matrices, round to
     nearby exact rationals, and verify the resulting polynomial identity
     EXACTLY in sympy (residual 0) — a floating-point "solved" flag is not
     sufficient per CLAUDE.md's rigor rules.
  5. If step 4's SDP remains numerically unreliable at degree 34, consider a
     targeted hand ansatz using n4sq specifically at the known-hard witness
     point (0.603,1.269) (where the 2-generator ansatz is proved infeasible
     and sits almost exactly on the n4=0 boundary) as a guide for what
     multiplier degree/structure n4sq needs to contribute there.
Key lemmas (claim + mechanism):
  - n4≥0 ⟺ n4sq≥0 on Case (b)'s domain — because both sides of the
    comparison defining n4 (w³cosB and u(3−u²)) are provably nonnegative
    there, making squaring a valid non-lossy equivalence (unlike a squaring
    applied to a signed quantity, which would only give a one-directional
    implication).
  - B<π/2 unconditionally on Case (b) — because B≤C and A+B+C=π, A>0 force
    B+C<π; B≥π/2 combined with B≤C would force C≥π/2 too, hence B+C≥π,
    contradiction.
Open gaps: the central Num≥0 target itself remains fully open — step 1 is
close to closed (needs formal write-up + verification of two elementary
sub-facts), but steps 3-5 (actual certificate construction) are not
complete; the round's SDP evidence (n4sq "helps," crosses positive in 2/3
trials) is explicitly suggestive-not-decisive (solver `optimal_inaccurate`,
Gram-matrix PSD violated at floating-point level, ≈0.72 max identity
residual in the checked run) — do not treat this as a certificate.
Cases to cover: none beyond the single Num≥0 target — the domain is already
fully and correctly encoded (Theorem 2 machinery, now simplified via n4sq).
Watch out for: (i) do not retry the already-proved-infeasible 2-generator
(n1,n2-only) ansatz in any form (Theorem 3, certified, any degree). (ii) do
not report a bare single-solver SDP "feasible/infeasible" at degree 34 as
decisive — round 14's noise-floor confusion and this round's solver
disagreement (CLARABEL vs SCS differing even in sign on some runs) both
demonstrate this is currently an unreliable regime; always cross-check with
≥2 solvers and, ideally, exact rational-witness-point evaluation (the
technique that correctly resolved the round-13/14 contradiction) before
trusting any SDP number here. (iii) resolve the coefficient-scaling
discrepancy (step 3) before spending further SDP compute — comparing
numbers across mismatched normalizations wastes builder effort.

build set: coordinate-bash-resultant-boundary-pointwise-tangent, coordinate-bash-resultant-boundary, coordinate-bash-resultant-boundary-pointwise-sos
