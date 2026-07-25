## imo-2026-02

### coordinate-bash-resultant-boundary: advance
Target: For every scalene (and, via the sibling's certified isosceles lemma,
every) triangle ABC with K,L satisfying all five problem hypotheses
(∠KBA=∠ACL; K∈△BMC and K inside ∠LBA; L∈△BNC and L inside ∠ACK), the
circumcenter O of AKL satisfies OM=ON.
Technique: Coordinate/rotation-parametrization + resultant algebra (as
before), but this round's primary lever changes from continuity/IVT-along-β
to a **direct algebraic cross-product-sign selection argument**, per the
f3lens explorer's new finding — this sidesteps the stuck F3/F3' crossing-
tracking question entirely rather than trying to finish it.
Skeleton:
  1. Import verbatim: vector reduction OM=ON ⟺ O·(C−B)=(|C|²−|B|²)/4
     (`lemmas/vector-reduction-OM-ON.md`); rotation parametrization
     K=B+t1(−cosβ,sinβ), L=C+s2·R(β)(A−C); homogeneity decoupling
     (`lemmas/homogeneity-decoupling-rotation-param.md`); symbolic
     genericity certificate T∈⟨G2a,G3a⟩ (`lemmas/symbolic-genericity-certificate.md`).
     — closed, no gap.
  2. **New Step (this round's target).** Formalize the two previously-unused
     hypotheses "K inside ∠LBA" and "L inside ∠ACK" as explicit polynomial
     sign conditions: cross(BL,BK)·sign, cross(BK,BA)·sign (K strictly
     between rays BA and BL) and the mirror pair cross(CA,CL), cross(CL,CK)
     at vertex C — all expressible as explicit polynomials in
     (s2,t1,u,a,b,cc) via the existing rotation-parametrization coordinates
     for K,L (no new machinery, reuses the already-certified closed forms).
  3. Prove: for fixed β, among the (at most 2×2=4) combinations of
     {root of G2a or G2b for s2} × {root of G3a or G3b for t1} that satisfy
     plain triangle containment (K∈△BMC, L∈△BNC), **at most one** combination
     also satisfies both extra cross-product-sign conditions simultaneously
     — by direct algebraic sign analysis of the four cross-product
     polynomials restricted to each of the four branch combinations (not
     resultants/IVT).
  4. Prove that combination is always the one on G2a=G3a=0 (not G2b or G3b)
     — by showing the two extra sign conditions, evaluated on the G2b (resp.
     G3b) branch, reduce to a polynomial with a provably fixed (wrong) sign,
     e.g. by factoring the cross-product polynomial restricted to G2b=0 and
     identifying a manifestly-signed factor (mirroring how F1,F2 were pinned
     down via cross-product factoring in prior rounds).
  5. Combine with Step 1's genericity certificate on G2a=G3a=0 to conclude
     the target identity holds at the unique geometrically valid point, for
     every triangle.
Key lemmas (claim + mechanism):
  - The two extra containment hypotheses (K inside ∠LBA, L inside ∠ACK),
    encoded as two explicit cross-product-sign polynomial inequalities in
    (s2,t1,u,a,b,cc), uniquely select (s2,t1) among all plain-containment-
    valid roots — because plain containment alone is genuinely
    under-determining near an F3/F3'-crossing (explorer verified two
    simultaneously containment-valid roots exist there), but the extra
    hypotheses are a strictly stronger joint condition coupling K and L
    together (not decoupled per-hypothesis like G2a/G2b), which numerically
    (~280 samples, including 15 targeted F3-crossing triangles) always cuts
    the valid set down to exactly one point.
  - That unique point always lies on G2a=G3a=0 — because (conjectured
    mechanism to formalize) the cross-product sign condition, when
    restricted to the G2b/G3b branch, factors through a term whose sign is
    fixed by the branch's own defining quadratic coefficients (to be
    identified via symbolic factoring, per the explorer's cheap-kill
    suggestion).
Open gaps: Steps 3–4 (the "at most one combination survives, and it's the
G2a/G3a one") are the whole remaining content — currently only ~280-sample
numerical evidence, no algebraic proof of the sign-fixed-factor claim.
Do NOT attempt a literal transfer of the Ptolemy route's IVT+quadratic-
degree argument onto G2a alone (explorer confirmed it doesn't type-check:
eq2 is a quartic in s2 via squaring, not Ptolemy's clean unsquared
quadratic).
Cases to cover: the F3=0/F3'=0-crossing regime (where plain containment is
provably multi-valued) must be checked explicitly, not just generic β —
this is exactly where the new mechanism is doing real work, per the
explorer's targeted 15-triangle test.
Watch out for: don't silently assume the magnitude bound t1<t1max(β) is
free — if Step 3–4 close, check whether full triangle containment
(including the t1max cutoff) is *implied* by G2a=0 + the sign conditions
(explorer's numerics suggest yes) rather than needing yet another separate
inequality proof; if not implied, it must still be established separately.

### ptolemy-trig-identity: advance
Target: same as above (OM=ON), via the fully independent Ptolemy/Law-of-
Sines route (no coordinates).
Technique: Trig identity + explicit closed-form quadratic roots (Steps 0–3,
already proved and certified) + a sharpened algebraic positivity target
F>4 (not merely F>0), attacked via a blow-up/Taylor analysis near the
observed extremal limit A→0.
Skeleton:
  1. Import verbatim (closed, certified): Steps 0–3 of `ptolemy-trig-identity.md`
     — cot-identity, quadratic reduction of (III)/(IV) with explicit
     coefficients a1,b1,c1 (resp. a2,b2,c2), and the IVT+quadratic-degree
     branch-selection theorem (`lemmas/ptolemy-trig-branch-selection.md`)
     pinning the genuine roots x=cotψ, y=cotφ in closed form.
  2. **New target**: prove F(θ,A,B,C) := sinA(p+2x)(p+2y) − sinA −
     cosA(2p+2x+2y) > 4 strictly, for all 0<θ<min(B,C), A,B,C>0, A+B+C=π
     (p=cotθ) — sharper than the population's previous "F>0" target,
     matching the positivitylens explorer's numerical finding inf F = 4
     exactly, approached only as A→0+, never attained.
  3. Compute F−4 symbolically (not just F) and look for a manifestly
     nonnegative closed form (e.g. a sum/product of squared or manifestly-
     positive trig factors), rather than attempting `sympy.simplify` on the
     raw radical expression directly (confirmed not to terminate).
  4. Do the blow-up analysis: set A=εa (a fixed, ε→0+), determine the
     ε→0 limiting form of α,α' (hence of x,y via the quadratic roots) and
     of F−4, to identify which terms combine into a vanishing-at-ε=0
     "boundary" piece versus a manifestly-positive "bulk" piece — this
     pinpoints the algebraic identity to prove for general A>0.
  5. Alternative/fallback sub-route if the direct radical route stalls:
     clear the two square roots one at a time (isolate √D1, square; isolate
     √D2, square) to convert F−4>0 into a fully polynomial (radical-free)
     inequality in cosθ,sinθ,cosA,sinA,cosB,sinB,cosC,sinC subject to
     sin²+cos²=1 (×4) and A+B+C=π — then attempt an explicit SOS
     certificate (by hand or via an SDP solver, cited via knowledge_base.md's
     SOS/Positivstellensatz entry if present).
Key lemmas (claim + mechanism):
  - F>0 is algebraically identical to α+α'<A (∠BAK<∠BAL) — because F is,
    by Step 1 of the file, exactly sin(A−α−α')/(sinα sinα'), and both
    sines are positive on (0,A) (Lemma S3) — already proved, import
    verbatim, do not re-derive.
  - inf F = 4 achieved only as A→0+ (numerically established this round,
    not yet proved) — likely mechanism: as A→0, the triangle degenerates
    with K,L both collapsing toward specific limiting rays, and the
    "extra slack" the population observed (F≥11.3 under naive uniform
    sampling) was an artifact of not sampling the thin A→0 region; the
    true tight case is this degenerate limit, suggesting F−4 vanishes to
    exactly first or second order in A there — worth confirming via the
    Taylor expansion in Step 4.
  - The naive containment-interval bound (cotψ>cot(C−θ) alone) is
    insufficient (refuted, 10.5% violation rate) — do NOT reuse this
    shortcut; any successful bound must use the exact quadratic root, not
    just its containing interval.
Open gaps: F−4>0 itself (Steps 2–5) — the sole remaining gap for a complete,
independent solution via this whole route.
Cases to cover: none beyond the general (θ,A,B,C) domain — no separate case
split needed once the F>4 form is established (unlike the earlier
sign(AB−AC) case split, which is already fully and separately closed by the
Proposition in Round 3's write-up).
Watch out for: do not retry `sympy.simplify`/`trigsimp` on the raw two-
radical expression directly — confirmed not to terminate twice
independently (file + explorer). Do the radical-clearing / blow-up
symbolically first.

### ptolemy-trig-identity-synthetic: copy-of ptolemy-trig-identity
Target: same as ptolemy-trig-identity (OM=ON via A,K,L,Q concyclic route),
but this branch pursues a **fully synthetic** (non-algebraic) proof of the
one remaining gap α+α'<A (equivalently F>0), instead of clearing radicals.
This is a genuine second, independently viable path to the SAME gap
(explorer's own recommendation #2) — worth running in parallel with the
algebraic F>4 push, since success here would close the gap without ever
touching the messy closed-form radicals.
Technique: Direct synthetic angle comparison exploiting the already-proved
containment facts (Lemma S3: 0<α,α'<A) and the specific geometry of M,N as
midpoints — attempt to relate K,L to a common auxiliary circle (e.g. one
through B,C and a fixed point, or the nine-point circle of ABC, since M,N
are midpoints and ψ=∠BMK, φ=∠CNL are angles subtended at those midpoints)
that would make α+α'<A a direct consequence of an inscribed-angle or
power-of-a-point comparison, bypassing the quadratic-root algebra entirely.
Skeleton:
  1. Import verbatim (closed, certified, shared with the sibling): Lemma 1
     (two-ray construction of K,L), Lemma 2 (closed-form angles α,α' via
     tanα=Rsinθ/(1−Rcosθ)), Lemma 3 (decoupled constraints (III),(IV)),
     Lemma S3 (0<α,α'<A).
  2. Reformulate the target α+α'<A as: the two rays AK, AL, together with
     ray AB and ray AC, satisfy a specific interleaving inside angle A —
     restate as "the point where ray AK meets... " or directly as a
     comparison of ∠BAK and ∠CAL against A/2 or against each other via an
     auxiliary circle through B, C, M, N-related points (candidates to try:
     the circle through B, C tangent to something at M or N; the nine-point
     circle of ABC, which passes through M, N and the feet of the
     altitudes — check whether K or L relates to it under the hypothesis
     angles ψ=∠BMK, φ=∠CNL).
  3. If an auxiliary-circle relation is found, derive α+α'<A as an
     inscribed-angle or directed-angle inequality on that circle (a genuine
     synthetic step, no trig identity to verify).
  4. If no clean auxiliary circle is found after a bounded search, fall
     back to a direct comparison via Ceva/trig-Ceva-style ratio comparison
     in triangle ABC using the explicit BK, CL length ratios (Lemma 2)
     rather than an auxiliary circle — a second synthetic fallback before
     conceding to the sibling's algebraic route.
Key lemmas (claim + mechanism):
  - Same target equivalence as the sibling (F>0 ⟺ α+α'<A) — import, don't
    re-derive.
  - New (to find): an auxiliary-circle or ratio-comparison fact tying K
    and L's angular positions together through M, N — motivated by the
    fact that ψ, φ are literally angles subtended at the two midpoints, a
    structure begging for a circle-through-midpoints argument (echoes the
    already-successful A,M,N,Q circle used elsewhere in the population).
Open gaps: the entire synthetic mechanism (Step 2–4) — this is a fresh
search, not yet attempted by anyone in the population; explicitly flagged
by the positivitylens explorer as the most promising alternative to the
radical-clearing route.
Cases to cover: none identified yet (mirrors the sibling: no case split
needed for this single inequality).
Watch out for: don't rediscover the already-ruled-out spiral-similarity-at-A
shortcut (dead end, confirmed false via ~100° angle mismatch, recorded
since round 1) — any auxiliary-circle idea must be checked against the
round-1 exhaustive 4-point-subset concyclicity search (which found only
A,M,N,Q and the target A,K,L,Q among the 8 named points) before assuming
a *new* circle among {A,B,C,K,L,M,N,Q}; a genuinely new circle would need
to involve an auxiliary point not in that set (e.g. a circle through B,C
and the midpoint of KL, or the nine-point circle, which was not part of
that 8-point search).

### fixed-point-concyclic: revise
Target: same as above (OM=ON), via the reduction to "A,K,L,Q concyclic"
(Q = reflection of A in perp-bisector of MN), fully independent of both
the coordinate and the Ptolemy routes.
Technique: unchanged (complex cross-ratio elimination), but this round's
gap is re-planned using a genuinely different lever: **add the problem's
two extra hypotheses (K inside ∠LBA, L inside ∠ACK) as two additional
explicit complex "ratio ∈ ℝ_{>0}" polynomial conditions** P4, P5 (they were
previously used only informally, to fix the *sign* of H1–H3, never as
independent algebraic constraints in the Step-4 elimination) — mirroring
the f3lens explorer's discovery that these same two hypotheses are the
missing selection mechanism in the sibling coordinate route. The prior
elimination attempt (ideal membership of T in ⟨P1,P2,P3⟩ only) left a
nonzero remainder −(B\bar C−\bar BC)·S; the working hypothesis for this
revision is that S lies in the *extended* ideal ⟨P1,P2,P3,P4,P5⟩, i.e. the
two extra hypotheses supply exactly the missing algebraic relation.
Skeleton:
  1. Import verbatim (closed, certified): Lemmas 1–6, (H1)–(H3) as complex
     ratio conditions with rigorously derived signs, the cross-ratio-real
     concyclicity criterion, and the precise diagnosis that
     T ≡ −(B\bar C−\bar BC)·S mod ⟨P1,P2,P3⟩ with S≠0 in the independent-
     conjugate relaxation.
  2. Derive explicit complex forms for "K inside ∠LBA" and "L inside ∠ACK"
     as two more "ratio ∈ ℝ_{>0}" conditions, analogous to (H1)–(H3): e.g.
     "K inside ∠LBA" ⟺ arg((K−B)/(L−B)) and arg((K−B)/(A−B)) have the same
     sign and the K-ray lies between the L-ray and A-ray from B — express
     as (L−B)/(K−B) and (K−B)/(A−B) both having positive imaginary part (or
     the equivalent ratio-positivity form used for H1–H3), giving cleared-
     denominator polynomials P4, P5.
  3. Recompute the Gröbner basis of the extended ideal ⟨P1,P2,P3,P4,P5⟩ in
     the same ring (K,\bar K,L,\bar L over ℚ(B,\bar B,C,\bar C)) and re-
     reduce T; check whether the remainder is now 0 (closing the gap) or
     still nonzero (in which case report the new remainder's exact
     structure — genuine new information either way).
  4. If closed: this gives a fully independent, complex-number proof of
     the whole problem's central identity, distinct in mechanism from both
     the coordinate/resultant route and the Ptolemy/trig route.
Key lemmas (claim + mechanism):
  - The two extra hypotheses, as genuine additional polynomial constraints
    (not just sign-fixers), plausibly supply the missing generator to kill
    S — because the coordinate route's fully independent numerical
    experiment (this round) found these same two hypotheses are load-
    bearing for uniqueness there (plain containment alone under-determines
    the solution near certain loci), suggesting they carry real algebraic
    content beyond orientation-fixing in every formulation, not just the
    coordinate one.
Open gaps: whether P4, P5 actually kill S (Step 3) — untested; this could
fail (S might not lie in the extended ideal either), in which case report
the negative result precisely, as this file has done twice before.
Cases to cover: the two secondary gaps already flagged (collinear
alternative of the cross-ratio criterion; AB=AC degenerate case) — the
degenerate case is now handled for free by the population's already-
certified `lemmas/isosceles-case-symmetry.md` (via a route-independent
argument), so this file should import that instead of re-solving it.
Watch out for: don't conflate this with the coordinate route's own
cross-product-sign mechanism — the complex "ratio ∈ ℝ_{>0}" encoding here
is a different algebraic device (argument/imaginary-part sign, not planar
cross product), even though the underlying geometric hypotheses are the
same; keep the two derivations independent so they remain genuinely
separate certificates if both succeed.
