## imo-2026-02

### Context recap (see current.md round 6 update, plus this round's 3 explorer reports)
Three live routes, each reduced to a single "sign/parity pattern over roots of an
explicit polynomial" claim: (a) coordinate-bash-resultant-boundary — G2b full
3-way exclusion; (b) coordinate-bash-resultant-boundary-pointwise — exactly-one-
survivor claim; (c) ptolemy-trig-identity — odd-parity among F(Ui,Vj). This round's
explorers made real progress narrowing (a) and (c), and flagged a genuinely
orthogonal, previously-untried lever for the long-dormant fixed-point-concyclic
route. Field this round: advance (a),(b),(c); copy ptolemy-trig-identity for the
second, independent mechanism found by orthogonallens; revise fixed-point-concyclic
with the new χ-as-explicit-combination lever.

---

coordinate-bash-resultant-boundary: advance
Target: OM=ON for every non-degenerate triangle ABC and valid parameter (branch
selection: the geometric solution always lies on G2a=G3a=0, and G2b=G3b=0 is fully
excluded).
Technique: resultant-ratio sign-cancellation (Sturm-flavored root-position algebra),
continuing the coordinate-bash-resultant-boundary pipeline already certified through
§12 (magnitude bound, closed) and §13 (G2b true/supplementary parity, closed).
Skeleton:
  1. Import certified §12/§13 results unchanged (magnitude bound; G2b's two roots
     share true/supplementary status) — by lemmas/magnitude-bound-and-sign-
     coincidence.md, lemmas/g2b-true-supplementary-parity.md.
  2. Import this round's new proved lemma: D_K(r1)D_K(r2) and D_N(r1)D_N(r2) always
     share sign — by sturmlens's resultant-ratio identity
     D_K(r1)D_K(r2)/D_N(r1)D_N(r2) = Res(G2b,D_K)/Res(G2b,D_N) = -(u²+1)²F2/(4u(b²+cc²)²) > 0
     (unknown factor Y cancels in the ratio; sign follows from already-certified F2<0).
  3. State the reduced target precisely: full G2b exclusion depends ONLY on the signs
     of three explicit polynomials Y(a,b,cc,u) = 2a(u²-1)²-b(u²+1)², B2(a,b,cc,u)
     (G2b's leading coefficient), and Z(a,b,cc,u) (from Res(G2b, Ñ2) = -8u(u²+1)²·F2·Z)
     — by the four resultant factorizations this round (Res(G2b,D_K), Res(G2b,D_N),
     Res(G2b,L1), Res(G2b,Ñ2)), each sharing the F1/F2/Y structure.
  4. Attempt the SAME endpoint/single-crossing-sinusoid technique already used to pin
     down F1<0, F2<0 (§11-12) to classify sign(Y), sign(B2), sign(Z) directly as
     functions of (a,b,cc,u) on the valid domain — this is the natural next
     application of an already-certified technique, not a new invention.
  5. Cheap-kill check first (per sturmlens's flagged lead): before doing the full
     8-way sign classification, run sympy.resultant/groebner on {Y,B2,Z} (as
     polynomials in u, generic a,b,cc) to test whether the sign pattern (+,+,+)
     is ALGEBRAICALLY forbidden (0/8000 numeric occurrences this round) — if
     provably excluded, the case count drops from 8 to 7 for free, and the
     underlying algebraic relation may simplify the remaining 6 non-dominant cases.
  6. For each realized sign pattern of (Y,B2,Z) (up to 7, with the ≈76%-dominant
     (Y>0,B2<0,Z<0) pattern tackled first, per sturmlens's census), re-derive which
     of G2b's two roots is "true," whether it is positive (s2>0), and whether it
     passes containment (L1<0 ∧ Ñ2>0) — concluding G2b is excluded in every case.
  7. Conclude: combined with the already-proved G2a-branch selection theorem
     (Theorem 11.8) and closed magnitude bound, the geometric solution provably
     lies on G2a=G3a=0 for every triangle and valid β — closing branch selection.
Key lemmas (claim + mechanism):
  - D_K/D_N same-both-roots-sign — because the unknown leading/Y factor cancels
    exactly in the ratio of two resultants sharing a common cofactor structure.
  - (NEW TARGET, not yet proved) sign(Y), sign(B2), sign(Z) are each determined
    by finitely many trig-boundary crossings on the valid β-range — because Y,B2,Z
    are, after Weierstrass back-substitution, trig-polynomial-like expressions of
    the same shape as F1,F2 (already closed by the endpoint/no-interior-zero method).
Open gaps: the sign classification of Y,B2,Z (step 4-6) is the entire remaining
gap; the (+,+,+)-forbidden check (step 5) is a cheap probe, not yet attempted
symbolically.
Cases to cover: up to 7 sign patterns of (Y,B2,Z) (all but (+,+,+), which is
conjectured forbidden but not proved) — each needs its own root-tracking argument;
tackle the dominant (+,-,-) pattern first as a pilot case.
Watch out for: the 17-distinct-orderings finding (fixed threshold-ordering / naive
interval chart is REFUTED, do not retry); this is a real case-split, budget builder
time for at least the dominant case plus the (+,+,+)-exclusion check, not a full
7-way sweep in one pass if time runs short — partial coverage with an honest
"N of 7 cases closed" is legitimate `partial` progress.

---

ptolemy-trig-identity: advance
Target: same as always — OM=ON via the Ptolemy/trig route; remaining gap is the
odd-parity claim (an odd number of F(Ui,Vj)-4, i,j∈{1,2}, exceed 0), now reduced by
paritylens to a single pairwise sign-opposition claim.
Technique: resultant-based radical elimination + IVT/continuity on a connected
domain (reusing the certified Ψ(0,A,C)>0 base-point technique, one level down).
Skeleton:
  1. Import certified Steps 1-3 unchanged (multiplicative resultant identity,
     sign lemma P1,P2<0, sextic-to-parity reduction) — by
     lemmas/ptolemy-resultant-elimination-to-sextic.md,
     lemmas/ptolemy-sextic-parity-reduction.md.
  2. Define Ξ(V) := Res_U(q1(U), F(U,V)-4) (radical-free, quadratic in V) — by
     the same "resultant of quadratic vs. linear-form-at-its-roots" formula
     already used throughout the population (Res(f,g)=lc(f)·g(r1)·g(r2)); note
     Ξ(V) = P1·(F(U1,V)-4)(F(U2,V)-4) as a polynomial identity (paritylens,
     symbolically derived).
  3. Prove the logical-sufficiency step (elementary case-count, NOT numeric):
     if sign(Ξ(V1)·Ξ(V2)) < 0, then exactly one of {F(U1,V1),F(U2,V1)} exceeds 4
     (contributing 1 to the count) and the pair {F(U1,V2),F(U2,V2)} has an EVEN
     number exceeding 4 (0 or 2, contributing evenly) — regardless of column 2's
     actual sign — so total count is odd, closing the claim. Write this out fully
     as a short case-exhaustion argument (4 sign combinations of the two products).
  4. Prove Ξ(V1)·Ξ(V2) < 0 on the whole connected domain D = {0<θ<min(B,C)} via
     IVT/continuity: (a) show Ξ(V1)·Ξ(V2) ≠ 0 anywhere on D (no sign change without
     a zero crossing on connected D), and (b) evaluate the sign at one base point
     (τ→0, mirroring the already-proved Ψ(0,A,C)=4sin³A sinB sinC>0 computation).
  5. For step 4(a), isolate the single radical in Ξ(V1) directly (V1 has one
     square root Δ2=Q2²-4P2R2, unlike F's two nested radicals): write
     Ξ(V1) = [a(τ,A,C) + b(τ,A,C)·√Δ2] / (2P2)², reduce non-vanishing to the
     radical-free comparison a² ≠ b²Δ2 on D (standard one-radical-clearing trick)
     — this is the concrete unfinished computation flagged by paritylens.
  6. Conclude the odd-parity claim, hence Ψ(τ,A,C)>0 on D, hence F(U1,V1)>4 is the
     unique exceedance, closing the ptolemy-trig-identity route to a full solve.
Key lemmas (claim + mechanism):
  - Ξ(V) = P1·(F(U1,V)-4)(F(U2,V)-4) — because Res_U(quadratic in U, linear form
    in U) = lc·(value at each root), the standard resultant-roots identity already
    used repeatedly by this population.
  - Sufficiency: opposite sign of Ξ(V1),Ξ(V2) alone forces odd total count — because
    one column contributes exactly 1 (product<0 ⟹ exactly one factor positive) and
    the other contributes an even number (product>0 ⟹ both same sign, hence 0 or 2
    positive), and odd+even=odd is elementary arithmetic (no case left unchecked).
Open gaps: the whole of step 4/5 — global non-vanishing of Ξ(V1) via a²≠b²Δ2
(not yet computed) plus the base-point sign evaluation.
Cases to cover: none beyond the domain D itself (single connected interval, no
further case split needed once non-vanishing is shown).
Watch out for: do NOT re-attempt the Ω=Res_V(q2,Ξ) joint-resultant shortcut —
paritylens confirmed this round it produces a degree-8 polynomial, no simpler than
Ψ itself; go via individual continuity/IVT on Ξ(V1) (or Ξ(V2)) as outlined above.

---

ptolemy-trig-identity-parity-decomposition: copy-of ptolemy-trig-identity
Target: same as ptolemy-trig-identity — closing the odd-parity gap, via a SECOND,
independent mechanism (per CLAUDE.md's "copy when two viable ways to fill the same
gap" — both worth pursuing since the reviewer should see which one actually closes
first, and the two are logically different routes, not variations of one idea).
Technique: direct two-lemma decomposition (orthogonallens's Finding 1) reusing the
already-certified g2b-true-supplementary-parity resultant template verbatim, rather
than paritylens's IVT/single-radical route.
Skeleton:
  1. Import certified Steps 1-3 unchanged (same as sibling approach).
  2. Sharpen the target (orthogonallens, 60,000-sample numeric support, 0
     exceptions including corner stress cases): conjecture the exceeding set is
     ALWAYS exactly {(U1,V1)} — decompose into two independent sub-lemmas:
     Lemma A: if U=U2 (spurious root of q1), then F(U2,V)<4 for BOTH roots V1,V2
       of q2 — a claim about a linear-in-V form (F(U2,·)) evaluated at both roots
       of the fixed quadratic q2.
     Lemma B (mirror, B↔C symmetry): if V=V2, then F(U,V2)<4 for BOTH roots U1,U2
       of q1.
  3. Prove Lemma A via Res_V(q2, L_{U2}) where L_{U2}(V):=F(U2,V)-4 (linear in V)
     — same resultant-of-quadratic-vs-linear-form template as
     lemmas/g2b-true-supplementary-parity.md, giving "both roots same sign of
     L_{U2}"; then pin the actual sign (not just same-sign) via one base-point/
     limit evaluation (e.g. τ→0 or τ→ domain boundary), exactly as that certified
     lemma did for its own product-sign fact.
  4. Prove Lemma B symmetrically (B↔C mirror of Lemma A — reuse the certified
     σ-symmetry structure already used elsewhere in the population).
  5. Combine: Lemma A + Lemma B together rule out (U2,V1),(U2,V2),(U1,V2) — the
     only remaining cell is (U1,V1). Show F(U1,V1)>4 there is FORCED (not just
     "the only candidate") by the already-certified odd-parity claim (an odd
     number exceed 4, and 3 candidates are now known to not exceed, so exactly
     1 must — namely (U1,V1)) — no extra computation needed for this last step,
     it's pure logic given Lemmas A, B and the certified parity-reduction.
Key lemmas (claim + mechanism):
  - Lemma A/B: both use Res(quadratic, linear-at-its-roots)=lc·L(r1)·L(r2), the
    exact template of the already-certified g2b-true-supplementary-parity.md —
    directly reusable machinery, not a new invention.
Open gaps: Lemma A and Lemma B are both unproved beyond "same sign" (need the
sign pinned, via a base-point check, to conclude "<0" not just "both equal"); the
final combination step (5) is logic-only once A, B are proved.
Cases to cover: none (Lemmas A/B are single unconditional claims each).
Watch out for: this route needs the sign pinned in BOTH directions (not just
product sign, unlike the sibling's coincidence-only lemma) — don't stop at "same
sign," the base-point evaluation is load-bearing here.

---

fixed-point-concyclic: revise
Target: same top-level target as always — A,K,L,Q concyclic (equivalently
OM=ON), proved via the complex cross-ratio χ=(A-L)(K-Q)/[(A-Q)(K-L)] ∈ ℝ.
Technique: SWAP the stalled ideal-membership/elimination lever (conclusively
retired round 5) for an explicit algebraic-identity construction: express χ
directly as a rational function of the already-known-real quantities H1, H2, H3
(the three hypothesis ratios), rather than eliminating conjugate variables.
This is the untried lever the file's own §5.4 names, and orthogonallens flags it
as genuinely orthogonal in mechanism to all three root-counting routes above —
directly satisfies CLAUDE.md's "if a plateau persists, bring a genuinely different
framing" requirement without opening a wholly new top-level target (round 3's
exhaustive search already showed no better target exists).
Skeleton:
  1. Import unchanged: (H1),(H2),(H3) as certified real-positive complex ratio
     conditions (Lemma 6, general vertex-sign derivation) — by
     lemmas/vertex-ratio... [existing certified fixed-point-concyclic lemmas],
     cross-ratio-real-concyclic-criterion.md.
  2. Write χ, H1, H2, H3 all as explicit rational functions of the SAME primitive
     variables (K, L, B, C, and the fixed points M=B/2, N=C/2, Q — all expressible
     in B,C alone since Q is a fixed function of B,C): tabulate each as a ratio of
     polynomials in K,L,B,C.
  3. Search for χ as an explicit rational combination of H1,H2,H3 (and possibly
     B,C themselves, since the one numeric sample this round found χ/(H1H2H3) is
     NOT a bare constant) — try χ = R(H1,H2,H3,B,C) for low-degree rational R by:
     (a) symbolic elimination of K,L between the four rational-function
     definitions (treating H1,H2,H3 as free parameters and solving for χ in terms
     of them plus B,C — a genuine 2-step elimination, K,L eliminated using
     (H1),(H2),(H3)'s own defining equations, NOT the same "adjoin more ideal
     generators for reality" lever already retired); (b) if a closed form is
     found, verify it reduces the target χ∈ℝ to a manifestly-real combination of
     the already-real H1,H2,H3,B,C (or a further clean real/imaginary decomposition
     that can be settled directly).
  4. If step 3 finds no clean low-degree closed form, fall back to computing
     χ explicitly as a rational function purely of B,C and the parametrization's
     free variable (β,t1,s2 or equivalent) — using the already-derived closed
     forms elsewhere in the population — and check by direct symbolic substitution
     of the hypothesis equations (H1)=(H2)=(H3)="real" (as EQUATIONS, using their
     already-real values, not as ideal generators) whether χ's imaginary part
     vanishes identically — this differs from the retired lever because it
     substitutes concrete real values for H1,H2,H3 rather than adjoining
     polynomial generators to force reality abstractly.
  5. Conclude χ∈ℝ, hence A,K,L,Q concyclic (cross-ratio-real criterion, already
     certified), hence OM=ON — closing the whole problem via this route.
Key lemmas (claim + mechanism):
  - χ is expressible as an explicit algebraic function of K,L,B,C (trivial, by
    definition) — the substantive open claim is whether, restricted to the
    hypothesis locus (H1),(H2),(H3) real-positive, this function is forced real —
    because Möbius/cross-ratio identities are typically low-degree rational
    combinations of a small generating set of ratios when the configuration has
    enough symmetry (untested here, the actual mechanism to find this round).
Open gaps: the entire closed-form search (step 3) — genuinely unsolved, may fail
to produce a clean identity at all (an honest negative result would still be a
valuable, precisely diagnosed dead end for this dormant approach).
Cases to cover: none identified yet (may emerge from the closed-form search).
Watch out for: do NOT re-attempt "adjoin more ideal generators of the ratio-is-
real species" (round 5's retirement argument is a structural dimension-count, not
a search-depth limitation, and still applies) — this revision is legitimate only
because it uses fundamentally different machinery (explicit rational-function
construction / direct substitution of known-real values), not more of the same
elimination.

---

coordinate-bash-resultant-boundary-pointwise: advance
Target: same top-level target — branch selection via the pointwise architecture
(exactly one of a quartic's real roots survives four joint conditions, sidestepping
the continuity/IVT crossing-classification question the sibling approach faces).
Technique: same resultant/Vieta machinery as the sibling coordinate route, applied
to the single quartic-in-s2 (or equivalent) polynomial from Lemma P1/P2, reusing
this round's ratio-cancellation trick (sturmlens's ONE new methodological
contribution most transferable here) rather than a fresh case census.
Skeleton:
  1. Import certified Lemma P1/P2 unchanged (elementary translation of the four
     joint conditions) — by lemmas/pointwise-branch-selection-criterion.md.
  2. Attempt the SAME resultant-ratio-cancellation technique that closed
     D_K(r1)D_K(r2) ~ D_N(r1)D_N(r2) this round (sturmlens): for each pair of the
     four joint conditions (viewed as low-degree forms evaluated at the roots of
     the governing quartic), compute Res(quartic, condition_i)/Res(quartic,
     condition_j) and check whether unknown leading-coefficient factors cancel,
     producing sign relations between the conditions independent of the quartic's
     unknown coefficients.
  3. Use any such sign relations to prune the 552-sample-confirmed "exactly one
     survivor" claim toward a provable finite case split (analogous to the (Y,B2,Z)
     reduction on the sibling approach), rather than a from-scratch attack.
  4. If the technique transfers cleanly, complete the case split; if not (report
     honestly, as sturmlens's negative "fixed threshold ordering" finding shows
     resultant tricks don't always transfer), document precisely which step fails
     for the record.
Key lemmas (claim + mechanism): none yet proved this branch beyond Lemma P1/P2 —
this round's target is to test transfer of the ratio-cancellation technique, not
assert a new lemma in advance.
Open gaps: the entire uniqueness-of-survivor claim.
Cases to cover: TBD, pending step 2's outcome.
Watch out for: don't duplicate effort with coordinate-bash-resultant-boundary's
G2b work — this is a genuinely different quartic/condition-set (four joint
conditions on one quartic, not a 2x2 product-of-quadratics structure), so the
transfer is a real (if plausible) test, not a copy-paste.

build set: coordinate-bash-resultant-boundary, ptolemy-trig-identity, ptolemy-trig-identity-parity-decomposition, fixed-point-concyclic, coordinate-bash-resultant-boundary-pointwise
