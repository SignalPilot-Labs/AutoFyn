## imo-2026-02 (lens: power-of-a-point / radical-axis framing)

### Distinct openings

**Opening 1 (clean, VERIFIED, likely the right first reduction).**
For *any* point O and any segment AB with midpoint M, the "median formula" for the
quadratic function `q(P) = |P-O|^2` gives, purely by the parallelogram law (no circle
needed):
`q(M) = (q(A)+q(B))/2 - AB^2/4`.
Apply this to O = circumcenter of AKL, to (A,B,M) and to (A,C,N):
`OM^2 = (OA^2+OB^2)/2 - AB^2/4`, `ON^2 = (OA^2+OC^2)/2 - AC^2/4`.
Subtracting, OA^2 cancels, and:
`OM = ON  ⟺  OB^2 - OC^2 = (AB^2 - AC^2)/2 = (c^2-b^2)/2` (standard notation b=CA,c=AB).
I verified this identity is exactly equivalent to OM=ON by direct coordinate computation
(not just conjectured — it is elementary vector algebra, true unconditionally).
**Important nuance found by testing:** this step by itself does *not* yet use that O is
the circumcenter of AKL — it is true for any point O. The real content of the problem is
showing this specific O (built from K, L via the three angle conditions) satisfies
`OB^2-OC^2=(c^2-b^2)/2`. So this is a valid, clean *reformulation* of the goal, but not
a proof by itself; the outliner should not mistake reaching "OB²-OC²=(c²-b²)/2" for a
free step — it still requires the angle-condition machinery.

**Opening 2 (power-of-a-point via chords through B, C).**
Since K, L, A all lie on ω = circumcircle(AKL): pow(B,ω) = BO²-R² can be computed as a
signed product along line BK: pow(B,ω) = `\overline{BK}·\overline{BK'}` where K' is the
second intersection of line BK with ω (similarly pow(C,ω) = `\overline{CL}·\overline{CL'}`
via line CL). Combined with pow(A,ω)=0, Opening 1's identity becomes
pow(B,ω) - pow(C,ω) = (c²-b²)/2, i.e. `BK·BK' - CL·CL' = (c²-b²)/2` (signed). This is
the natural place to plug in the angle conditions, since BK and CL are exactly the
segments constrained by ∠KBA = ∠ACL (condition 1). **I checked numerically whether K'
(second intersection of BK with ω) coincides with a natural named point (L, N, or C)
— it does not**, in a generic scalene example; ruling out that naive guess. The second
intersection points do not have an obvious closed form from the given data alone, so
this chord-product route likely needs an auxiliary construction (e.g. locating K', L'
via an explicit angle-chase using the inscribed-angle theorem in ω, or avoiding K'
entirely and instead computing pow(B,ω) via the extended law of sines: for P off a
circle of radius R centered O, and a chord through P and X∈ω making angle φ with the
tangent at X, pow(P)=PX·PX' with PX' derivable from the inscribed angle — needs a
concrete angle-chase to be useful).

**Opening 3 (angle conditions as PARTIAL spiral similarities — checked and only partly
true, an important caution).** The shapes of conditions 2 and 3 (∠LBK=∠LNC, ∠LCK=∠BMK)
look like halves of the "spiral similarity center" configuration (L centered, sending
B→N,K→C; K centered, sending C→M,L→B). I tested this numerically: the *angle* equality
holds (by construction) but the companion *ratio* equality required for full similarity
(LB/LN = LK/LC, resp. KC/KM = KL/KB) does **NOT** hold in general — ratios differ
substantially across the 1-parameter family. So **do not assume L or K is a literal
spiral-similarity center** with the standard SAS-similar-triangles consequence; only the
single angle equality is available, and any lemma built on "triangle LBK ~ triangle LNC"
is unsound. This is a concrete dead-end warning for the outliner.

**Opening 4 (direct angle-chase / trig identity route, untried in detail).** Since the
problem gives exactly 3 angle equalities among 4 unknowns (K has 2 DOF, L has 2 DOF), the
valid (K,L) form a 1-parameter family (confirmed numerically below), and O traces some
locus as the parameter varies — yet OB²-OC² stays constant along the whole family. This
suggests the real proof shows some quantity tied to O (e.g., the projection of O onto BC,
or the power of B and C individually) is controlled by a trig identity from the law of
sines in circle ω applied together with the three angle conditions — i.e., a "moving
point" / trig-Ceva-flavored approach might be more tractable than trying to pin down K'
explicitly.

### Candidate technique(s)
- Power of a point + radical axis (knowledge_base.md: "Synthetic toolkit: angle chasing,
  power of a point ... radical axes"). Opening 1's median-of-power-function identity is a
  standard consequence of this toolkit (parallel-axis-type formula for power/quadratic
  forms — same flavor as the Linear Algebra KB entry on quadratic forms, though here it's
  elementary Euclidean, not that entry specifically).
- Directed angle chase (to handle configuration/orientation issues cleanly given the
  "K inside angle LBA," "L inside angle ACK" configuration constraints).
- Possibly trigonometric Ceva / extended law of sines in ω to convert the three angle
  conditions into length ratios usable in Opening 2's chord-product identity.

### Cheap-kill candidates
- None found that finish the problem outright. But Opening 1 IS a cheap, free,
  unconditionally-true reduction (proved by elementary vector algebra, not casework) that
  every approach should use as the very first step — it turns "prove OM=ON" into "prove
  OB²-OC² = (AB²-AC²)/2," removing O's dependence on A entirely.
- Symmetry check: swapping (B↔C, M↔N, K↔L) swaps the roles in all three angle conditions
  and should map the problem to itself — useful for keeping casework symmetric (not
  independently verified beyond eyeballing the statement's symmetry).

### Knowledge-base entries to use
- "Synthetic toolkit: angle chasing, power of a point (and its concyclicity converse
  PA·PB=PC·PD), radical axes & radical center, similar triangles, trig cevians
  (Ceva/Menelaus), inversion, spiral similarity" — geometry section of knowledge_base.md.
  Directly names power of a point and spiral similarity, both implicated above.
- "Coordinates / complex / barycentric" entry — a fallback if synthetic angle-chase stalls;
  the configuration is coordinate-friendly (I used plain Cartesian coordinates + fsolve
  successfully to explore/verify below).

### Analogous past problems (cruxes)
None. `crux_moves_documentation.md` states explicitly: "geometry — Not in the corpus yet;
the problems DB includes geometry problems with solutions, but no geometry cruxes have
been extracted." So the crux corpus has no geometry entries at all; do not query it for
this problem (would return nothing genuinely analogous).

### Prior progress
None — round 1, workspace `results/imo-2026-02/` was empty (no `current.md`, no approaches,
no lemmas) at start of this round.

### Dead ends (do not retry)
- Assuming K or L is a genuine spiral-similarity center giving full triangle similarity
  (LBK~LNC or KCL~KMB) — numerically false (ratios don't match; only the angle part of
  the hypothesis is actually given). See Opening 3.
- Assuming the second intersection of line BK (or CL) with ω is one of the already-named
  points L, N, C (resp. K, M, B) — numerically false in a generic example. See Opening 2.

### Small-case / intuition notes (all labeled CONJECTURE / numerically checked, not proved)
- Built a concrete numeric model: A=(0,0), B=(6,0), C=(1.5,5) (scalene). Solved the 3 angle
  equations plus one extra scalar constraint (fixing ∠KBA=t) via `scipy.optimize.fsolve`
  for several t in [10°,30°], confirming a 1-parameter family of solutions exists.
- For the valid branches where K is actually inside triangle BMC and L inside triangle BNC
  (checked via barycentric-sign inside-triangle test; t=10° and t=20° gave an invalid
  branch where K fell outside triangle BMC / OM≠ON, correctly excluded), OM = ON held to
  numerical precision (diff < 1e-6) for t = 15°, 25°, 30°.
- For those same valid branches, `pow(B,ω) - pow(C,ω)` was numerically *exactly* constant
  (4.37500 for all three valid t, matching `(AB²-AC²)/2` exactly) even though pow(B,ω),
  pow(C,ω), OM, ON individually all varied with t. This is strong evidence Opening 1's
  reduction is the right target identity and that it's an invariant of the whole family,
  not a coincidence of one configuration.
- This confirms the problem's implicit claim: the three angle conditions do NOT pin down
  (K,L) uniquely (only cut a 1-dim family from the 4-dim space), and OM=ON is invariant
  along that whole family — so any correct proof must show the family-invariance
  structurally (e.g. via the angle conditions controlling `BO²-CO²` directly), not by
  somehow first proving K, L are unique.
