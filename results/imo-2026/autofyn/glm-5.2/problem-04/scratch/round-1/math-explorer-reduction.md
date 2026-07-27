## imo-2026-04 — reduction-to-known lens

### 1. The one-move transition, restated in the most transfer-friendly way

Let θ be the target. Work in **q-units**: q_i = (angle_i)/θ. The angle-sum A+B+C=π becomes q_A+q_B+q_C = S := π/θ (a single real parameter, S>1 since θ<π). Mulan wins iff some coordinate equals 1.

**Move (cut at vertex A, parameter t∈(0,q_A)):** the two children are
- child1 = (q_B, t, q_A+q_C−t)   [angle at P]
- child2 = (q_C, q_A−t, q_B+t)

Shan-Yu keeps one. So Mulan, to guarantee progress, must pick the vertex and t so that **both** children are winning positions W. The winning set W is the least fixed point: a triple is W iff it contains a 1, or ∃ vertex A and t∈(0,q_A) with both children W. θ is **good** iff *every* positive triple summing to S is W (Shan-Yu picks the initial triangle).

**Key forcing move (t=1, i.e. t=θ in real angles):** whenever q_A>1, Mulan sets t=1. Then child1=(q_B,1,q_A+q_C−1) contains 1 ⇒ W. So Shan-Yu (to avoid losing next round) is *forced* to keep child2=(q_C,q_A−1,q_B+1). Net forced transition under t=1 play:

> (q_A,q_B,q_C)  ⟼  (q_C, q_A−1, q_B+1)   [a "transfer 1 from coordinate A to coordinate B"; sum S conserved]

valid while the cut coordinate exceeds 1. So the *greedy* strategy reduces to a **chip-transfer game**: transfer unit mass from one pile (>1) to the next, win when a pile hits exactly 1. But t=1 is NOT the only move — Mulan may use any t, which changes fractional parts and lets her break out of t=1 cycles (verified below). So the t=1 dynamics is the backbone, not the whole game.

### 2. Top retrieved cruxes

- **aimo-0440 (USAMO 2008, number_theory / size-bounding-and-descent)** — *THE central transferable crux.* Three nonneg reals r1,r2,r3 with an **integer linear relation** a1 r1+a2 r2+a3 r3=0. Operation: replace (x,y), x≤y, by (x, y−x). Crux: the relation is preserved (unimodular on the coefficient vector (a1,a2,a3)), and |a1|+|a2|+|a3| is a strictly decreasing nonneg-integer monovariant, so it bottoms out at a zero coefficient, reducing to the 2-variable Euclidean algorithm. **Transfer rationale:** if θ=π/n then S=n and the four quantities (A,B,C,θ) satisfy the integer relation A+B+C−n·θ=0, i.e. in q-space q_A+q_B+q_C=n. The "reach a coordinate =1" goal is the analogue of "reach a zero". The forcing move (transfer 1, i.e. subtract θ) is precisely an aimo-0440 Euclidean step. This is the engine for the **sufficiency** direction (θ=π/n good). *Fit is strong, not exact* — our op transfers mass between two piles rather than subtracting one pile from another, so the coefficient-vector/L1 monovariant must be re-proved for the transfer dynamics; but the integer-relation-enables-descent principle transfers directly.
- **aimo-0355 (USAMO, number_theory / modular-arithmetic-and-CRT)** — "quirky triangles": when does a triangle's angle triple admit an integer linear relation? Crux: an integer angle-relation r1α+r2β+r3γ=0 is equivalent (via cos) to cos(rα)=±cos(sγ), reduced via Chebyshev polynomials to a rational-coefficient identity, then to a prime-factor-set condition on the denominators. **Transfer rationale:** this characterizes exactly when the aimo-0440 "integer relation" hypothesis holds for a triangle's angles — i.e. when the Euclidean-descent engine even *applies*. It suggests the good-θ set is governed by a commensurability/prime-factor condition, consistent with θ=π/n. *Fit is loose* (different goal — no game), but it is the corpus's only other "integer relation among triangle angles" result.
- **aimo-0785 (IMO-SL 2017, number_theory / divisibility-and-gcd)** — a function f on coprime pairs pinned by the subtractive axiom f(a+b,b)=f(a,b) (Euclidean-step invariance). Crux: f is determined by the sign of the balanced Bezout coefficient, i.e. by which side of b/2 the inverse of a mod b falls. **Transfer rationale:** shows that reachability games whose transition is a Euclidean step have outcomes governed by a continued-fraction / modular-inverse threshold. Useful for the necessity borderline (where the "transfer 1" orbit under +1 mod (pair-sum) lands relative to 1/2). *Fit is real but indirect* — a different game.
- **aimo-0324 (RMM 2019, number_theory / invariants-and-monovariants)** — Amy/Bob game n→n−a² vs n→nᵏ; crux: the *squarefree part* S(n) is a one-sided monovariant (Amy's nᵏ cannot increase S) bounding a descent to 0. **Transfer rationale:** methodological — find a monovariant that the opponent's move cannot increase, forcing eventual arrival at a target. Confirms the "monovariant drives the win" shape. *Fit: methodological only.*
- **aimo-0225 (RMM 2015, combinatorics / games-and-strategy)** — regular n-gon counter-sliding game, "for which n does first player win". Crux: P/N status of isosceles states determined by the 2-adic valuation v_2(a−b) of the difference, via halving steps. **Transfer rationale:** an olympiad "for which parameter" game whose answer is a number-theoretic (valuation) condition on the parameter — same *answer-shape* as our likely θ=π/n. Also uses strategy-stealing via reflective symmetry, a candidate for the symmetric (isosceles) subcases here. *Fit: answer-pattern + symmetry, not the dynamics.*
- **aimo-0893 (RMM 2018, number_theory / size-bounding-and-descent)** — gcd(an+b,cn+d) value set; crux: a Euclidean step on two linear forms replaces the larger leading coeff by its remainder, descent on that coeff. **Transfer rationale:** another instance of "Euclidean step on linear forms + coefficient descent" — reinforces that the sufficiency engine is Euclidean-descent on the angle-linear-forms. *Fit: reinforces aimo-0440.*

Honest note: NO corpus problem is a direct match (the cutting-triangle game is not in the pre-2026 set as stated). aimo-0440 is the closest in *mechanism*; aimo-0355 is closest in *commensurability structure*; aimo-0225 is closest in *answer shape*.

### 3. Best mathematical-home framing

**Primary home: a Euclidean-algorithm / chip-transfer game on three reals, gated by an integer linear relation (the aimo-0440 home).** The forcing move is "subtract θ (transfer 1) from one coordinate to the next"; the descent is feasible exactly when the four quantities (A,B,C,θ) admit an integer relation, i.e. when θ/π is rational — and the clean termination (hitting exactly θ, not overshooting) needs the relation A+B+C=nθ with n a *positive integer*, i.e. θ=π/n.

Why not the alternatives:
- *Circle rotation / β-transformation:* the "transfer 1 mod (pair-sum)" sub-dynamics is literally rotation by +1 on ℝ/(pair-sum), which IS a circle rotation — relevant to the necessity/escape argument (orbits that miss 1 forever when the modulus is irrational or incommensurate), but it does not by itself expose the good set.
- *Stern–Brocot / Farey mediants:* the "both children must be W" branching vaguely resembles mediants, but our operation is subtractive, not a mediant average; no clean fit.
- *Angle-bisector iterated map:* too special (fixed bisection), whereas Mulan controls t freely.

So: **the Euclidean-descent framing makes the winning-θ-set visible**, with the circle-rotation view supplying the escape (necessity) side.

### 4. What that framing predicts for the θ-set

**Leading conjecture (CONJECTURE, not proved):** θ is good ⇔ θ = π/n for an integer n ≥ 2 (i.e. S=π/θ ∈ {2,3,4,…}; θ ∈ {90°,60°,45°,36°,30°,…}).

Reasoning:
- *Sufficiency (θ=π/n):* S=n integer gives the relation q_A+q_B+q_C=n; the aimo-0440 descent engine (adapted to the transfer op) should drive a coordinate to 1. Verified on small cases: equilateral with θ=90° (q=(2/3,2/3,2/3)) — t=1/3 makes BOTH children (2/3,1/3,1), win in 1 move. θ=60° from (90°,42°,48°) (q=(1.5,0.7,0.8)): t=1.3 yields child1=(0.7,1.3,1)✓ and child2=(0.8,0.2,2.0); then cut 2.0 with t=1 gives child1=(0.2,1,1.8)✓, child2=(0.8,1,1.2)✓ — win in 2 moves. (Computed by hand; labeled conjecture.)
- *Necessity (the hard part — flag for outliner):* if θ≠π/n, three sub-cases must each be closed:
  (a) θ/π irrational: no integer relation A+B+C−nθ exists; aimo-0440 descent cannot apply. Expect a Shan-Yu escape via a Kronecker/density argument (maintain all three fractional parts {q_i} off 0 forever). The KB's Kronecker/Weyl equidistribution entry is the candidate tool.
  (b) θ/π = p/q rational, q≥2, p>1 (e.g. θ=2π/5=72°, θ=2π/3=120°): the relation is qA+qB+qC = p·π... still integer, so descent is not obviously blocked — yet the "transfer 1" dynamics exhibits cycles. Concretely for θ=2π/5 from equilateral (q=(5/6,5/6,5/6)), the greedy t=1 play cycles (5/6,1/6,3/2)↔(5/6,1/2,7/6) and the alternative t=4/3 returns to the start. Whether *some* t wins is unresolved — this is the **critical borderline** the outliner must settle. My tentative read: these are Shan-Yu escapes, making the answer π/n (not "rational multiple of π"), but this is unproved.
  (c) θ>π/2 (large angles): fewer cut points have q_A>1; structural upper-bound on S<2 may rule out goodness for θ>π/2 except θ=π/2 itself.

So the framing predicts a **thin, arithmetic answer set** {π/n : n≥2}, with sufficiency via Euclidean descent and necessity via circle-rotation escape + ruling out non-1/n rationals.

### 5. Reusable named theorems from knowledge_base.md

- **Invariants & monovariants** (Combinatorics): the transfer-1 move preserves each {q_i mod 1} (invariant under the greedy strategy); a strictly-decreasing nonneg monovariant (à la aimo-0440's L1 coefficient norm) drives termination. Central to BOTH directions.
- **Kronecker / Weyl equidistribution** (Number Theory): for irrational θ/π, the orbit of fractional parts under +1 mod (pair-sum) is dense — candidate for the Shan-Yu escape (show Mulan cannot pin a coordinate to exactly 1).
- **Three-gap / Steinhaus theorem** (Number Theory): if the escape argument reduces to a circle-rotation gap structure, the three-gap theorem governs the orbit's nearest approaches to 0 (and hence to "1"). Possibly the sharp tool for the irrational necessity.
- **General: Invariant/monovariant, Contradiction, Casework** (General Proof Methods) — for the necessity casework (irrational / rational-non-1/n / large-θ).
- **Pólya: solve a simpler/special case, specialize** — isosceles and equilateral starting triangles are the diagnostic special cases (used above).

No direct game-theory/min-max entry exists in the KB; the "both children must be W" recursion is the game-theoretic core and must be built from scratch.

### 6. Named candidate approach framings for the outliner (distinct from pure angle-dynamics / pure escape)

1. **Euclidean-descent on the 4-tuple (A,B,C,θ) [sufficiency]** — cast as aimo-0440 for four quantities with relation A+B+C−nθ=0 (θ=π/n). Lift the L1-coefficient monovariant from the subtract op to the "transfer θ" op; prove it strictly decreases until a coordinate hits θ. Builds on aimo-0440 + aimo-0893.
2. **Circle-rotation escape [necessity, irrational case]** — show that when θ/π is irrational, Shan-Yu maintains a triple with all {q_i} bounded away from 0 (Kronecker density / three-gap), so no coordinate can be forced to 1. Pair with a "transfer-1 preserves fractional parts" invariant to make Shan-Yu's reply explicit.
3. **Borderline-rational casework [necessity, θ=pπ/q, p>1]** — isolate the 2-pile subsystem (as in the 2π/5 cycle above) and prove Shan-Yu has a periodic escape OR find Mulan's winning t. This is the crux that decides whether the answer is "{π/n}" or "{rational multiples of π}". Frame as a 2D map (x, M−x) ↦ (x+1, M−1−x) and analyze its orbit structure modulo M.
4. **Recursive winning-set characterization [game-theoretic base]** — define W as the least fixed point of "contains 1, or both children W"; prove a structural lemma that W = {triples whose fractional-part triple lies in a specific semigroup}, making the good-θ condition read off from S alone. This is the "right" framing if the answer is clean, and it subsumes 1–3.
5. **Large-θ structural bound** — for θ>π/2, show S<2 forces a Shan-Yu escape (only one coordinate can exceed 1, restricting Mulan's moves); settles the upper end of the parameter range separately from the arithmetic conditions.

### Prior progress / Dead ends / Small-case notes
- Prior progress: none (round 1, workspace empty).
- Dead ends: none yet (no approaches tried).
- Small-case intuition (all CONJECTURE, hand-computed): θ=90° winnable from equilateral in 1 move; θ=60° winnable from (90°,42°,48°) in 2 moves; θ=72° (=2π/5) from equilateral shows a t=1 cycle and resists the obvious breaks — flagged as the decisive test case. Pattern consistent with answer = {π/n : n≥2}.
