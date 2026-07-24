## imo-2026-03

greedy-halving-adversary: advance
Target: the whole problem — c(n) = 2^n/(2^{n+1}-1), both directions for
every n (Status currently `partial`; Claim A fully closed, Claim B and the
general upper bound partially closed, current open item is Case (b)'s
"v>=a" branch's T'-cuts-p4 sub-case).
Technique: Vertex-Minimum Theorem + Odd-Run Reduction Lemma applied
directly to the whole residual object B={b}∪T' (not decomposed via the
dead Insert-Element one-sided-bound route), continuing round 23's
mechanism one level further in, per explorer opening (2)/(1).
Skeleton:
  1. Recall Theorem 37 (certified): symmetric-split, p4-untouched vertex
     of B={b}∪T' closes A(B)>=f(n) conditional on (star_{n-4}), unconditional
     n<=6 — cite verbatim, do not re-derive.
  2. Attack the open complementary sub-case: T' DOES cut p4. By the
     Insert-Element slope argument (already derived round 23), the
     candidate worst point in the top region is b=max(T') (a new type-(II)
     tie vertex), giving A(B)=A(T'\{max(T')}) by odd-run pair-cancellation
     — this step is already proved, reuse it, don't re-derive.
  3. NEW step (this round's actual target): the residual T'\{max(T')} =
     {c2}∪T''' where c2 is p4's OTHER fragment (c2 in (0,p4/2]) and T''' is
     a legal refinement of {p5,...,p_{n+1}} with <=n-5 cuts. Define the
     abstract standalone target (explorer's opening 1):
       h(m) := inf over c in (0, q1] and legal (<=m-1)-cut refinements S of
       an m-length ratio-2 tail q, of A({c}∪S).
     Prove by strong induction on m, applying Vertex-Minimum Theorem +
     Odd-Run Reduction Lemma to the WHOLE joint object {c}∪S directly (the
     same recipe Theorem 37 used one level up, and the same recipe that
     succeeded for Claim A's Case I via exchange-smoothing-vertex-
     maximization on an analogous "free coordinate + fixed reference set"
     shape) — NOT by trying to force the ladder-specific Cross-Level
     Rescaling Lemma (confirmed this round, again, to not apply: its
     hypothesis needs the WHOLE tail being refined to already be a rescaled
     ladder, false here since c is an arbitrary non-ladder value).
  4. Show h(m) >= f-analogue for the (m)-scale via one of:
     (a) direct vertex enumeration on {c}∪S using odd-run-reduction (does c
         tie to an element of S, or is c itself pinned to 0/q1?), reducing
         to finitely many cases each evaluable in closed form; or
     (b) exchange-smoothing-vertex-maximization DUALIZED to a minimization
         (it is polarity-agnostic per certified vertex-minimum-theorem, but
         must be explicitly re-verified for this direction per rule #6 in
         proof-outliner memory) applied to bound A(S)-side quantities from
         above independently of c, then combine via the certified triangle
         bound / half-bound-lemma (A>=0, A<=Total).
  5. Conclude A(B)>=f(n) in the T'-cuts-p4 sub-case by substituting the
     h(m)-bound at m=n-4 (or the appropriate depth) back through the
     already-proved reduction chain (step 2).
  6. Combine with Theorem 37 to close the WHOLE "v>=a" branch of Case (b)
     unconditionally (subject to whatever (star_m)-conditionality survives
     from Cross-Level Rescaling in the p4-untouched branch — keep that
     scoping honest, don't silently drop it).
Key lemmas (claim + mechanism):
  - h(m) target well-defined and finite — because A is bounded (0<=A<=Total,
    already certified Fact 2/half-bound-lemma), so an infimum exists; the
    question is only its exact value/lower bound.
  - Vertex-Minimum Theorem applies to {c}∪S jointly — because it is a
    fixed-composition (one free cut position for c, plus S's own legal cut
    budget) continuum optimization of an affine-in-fragment-lengths
    functional (A is a signed sum over sorted order) over a compact
    polytope, exactly the hypothesis the theorem already requires; no new
    proof needed, just a new instantiation.
  - If the vertex ties c to an element of S, odd-run-reduction cancels the
    pair exactly (already proved general fact, reused, not re-derived) —
    reduces h(m) at that vertex to A(S minus one element), an (m-1)-scale
    object.
Open gaps: step 4's actual closed-form/inductive bound on h(m) is THE open
gap (this is the whole point of the round); the (star_m)-conditionality
propagation in step 6 needs bookkeeping care.
Cases to cover: within step 4's vertex enumeration — c tied to an S-element
vs. c pinned at 0 vs. c pinned at q1/2 (forced max value) vs. c ties across
levels (e.g. to an even-deeper element of S after S is itself refined);
enumerate all before claiming exhaustiveness.
Watch out for: do NOT re-attempt forcing the Cross-Level Rescaling Lemma
directly on {c}∪S — confirmed dead again this round (explorer Experiment
1: the "bisect p4 into two copies of p5" special case merely reproduces
Theorem 37's own vertex via a longer path, not new ground, and fails at
n=7 without the same (star_{n-4}) conditional step). Also watch for the
"h(m) is literally isomorphic to the original problem" trap — it is NOT:
c is unconstrained relative to q's own ladder values (no p_i=2p_{i+1}-type
relation pins it), so h(m) is a genuinely different (harder, less
structured) quantity than L(m) itself; do not assume L(m)'s machinery
transfers without re-deriving the vertex family for THIS shape.

rank-pigeonhole-budget: advance
Target: the whole problem, same as above — this sibling reaches the
identical open sub-case via its own independently-derived Single-Insert-
Point Vertex Lemma (no appeal to vertex-minimum-theorem/compactness,
self-contained piecewise-affine slope-±1 argument).
Technique: Single-Insert-Point Vertex Lemma, continued one level further in
(explorer opening 2/3), specifically opening 3 — bound the residual from
ABOVE (dual direction) using exchange-smoothing-vertex-maximization, which
this project has already proved sufficient for the structurally analogous
"maximize over a free coordinate + fixed reference multiset" shape in
Claim (A)'s Case I Closure Theorem.
Skeleton:
  1. Recall the Single-Insert-Point Vertex Lemma (certified, self-contained,
     independent derivation of Theorem 37's content) — cite, don't re-derive.
  2. Restate the open residual precisely in this approach's own notation
     (matching the sibling's {c2}∪T''' object) and confirm (cheap, cross-
     check) it is the identical object greedy-halving-adversary names, not
     a superficially different one — this cross-check convergence is itself
     valuable (as it was for Theorem 37/Single-Insert-Point Vertex Lemma
     the first time).
  3. NEW step (opening 3, distinct route from the sibling's opening 1/2):
     instead of directly lower-bounding A({c2}∪T''') via vertex
     enumeration, upper-bound the COMPLEMENTARY quantity needed by the
     current proof chain (trace exactly which direction — lower vs upper —
     the Insert-Element Identity's slope argument actually needs at this
     point; per round 22's Insert-Element Identity finding, a one-sided
     LOWER bound on A(T')-type quantities is structurally insufficient, so
     this step must supply an upper bound instead) using
     exchange-smoothing-vertex-maximization applied to the free coordinate
     c2 with T''' as the fixed reference multiset — the same shape as
     Case I's F-vs-tau maximization.
  4. Combine the resulting upper bound with the already-certified cheap
     bounds (A<=Total, A>=0) and the pair-cancellation identity from step 2
     of the sibling's skeleton to close the T'-cuts-p4 sub-case, or at
     minimum narrow it to a strictly smaller open residual than before.
  5. If closed: combine with Theorem 37 / the sibling's own p4-untouched
     closure to state the FULL unconditional (or (star_m)-conditional)
     closure of Case (b)'s "v>=a" branch, and note the resulting
     implications for §7.6's general-n Diamond'/sharp' target via the
     already-certified §7.7 iff equivalence.
Key lemmas (claim + mechanism):
  - exchange-smoothing-vertex-maximization is polarity-agnostic for THIS
     shape (free coordinate + fixed reference multiset), because its proof
     is a standard affine-function-on-compact-polytope argument that does
     not use the min/max direction specifically — but this must be
     EXPLICITLY re-verified for the maximization direction here (per rule
     #6 in proof-outliner memory), not assumed free from the min-direction
     usage in Case I.
  - Confirm which direction (upper vs lower bound on the {c2}∪T''' object)
     the proof chain genuinely needs before building either — trace it from
     the Insert-Element Identity's slope formula explicitly as step 3 does,
     rather than guessing.
Open gaps: whether exchange-smoothing-vertex-maximization's polytope
actually has the needed structure once applied one level down (c2's box
constraint c2 in (0,p4/2] plus T'''s own legal-cut polytope) — this
combined polytope's vertex family has not yet been characterized for this
specific nested shape; that characterization is the real open gap.
Cases to cover: same vertex enumeration as sibling's step 4 cases — c2
tied to a T'''-element vs. pinned at 0 vs. pinned at p4/2.
Watch out for: do not silently reuse the min-direction vertex-minimum-
theorem's exact vertex family for a max-direction claim without re-deriving
— this is exactly the trap flagged in memory rule #6, and this shape (free
coordinate + reference set) is precisely where Case I's maximization
direction was validated, so the tool is plausible but must be checked here
specifically, not assumed.

lp-duality-certificate: advance
Target: the whole problem — specifically its open front, the general upper
bound c(n)<=a_n for arbitrary Liu Bang markings, case (b2) (T/D_n < p2 <
a_n*T/2) at n=3, via the feasibility-only covering-family simplification.
Technique: extend the certified covering family (Bisect-Top-k, Cross-Piece
Sign-Assignment, Alternating-Gap-Cross, Chamber A, Chamber A2, Theorem
D'/E, and this round's two new Double-Sandwich chambers) with one more
closed-form chamber type targeting the residual p1->T/2 boundary cluster,
then assemble a complete n=3 covering proof.
Skeleton:
  1. Certify Double-Sandwich-Below and Double-Sandwich-Above as standalone
     lemma files: derive their closed forms
     Phi_Below = (T+p2+p3-p1)/2, Phi_Above = (T+p1-p2-p3)/2
     rigorously from the Cross-Piece Sign-Assignment Identity applied to a
     single p1-split straddling TWO untouched tail elements (p2,p3) at
     once, via the rank-parity bookkeeping already sketched by the
     explorer — not just numeric recovery; write the formal proof.
  2. Derive and prove their feasibility regions exactly (not just "reduces
     essentially to"): interval-nonempty conditions p1<p2+p3 (Below) and
     p1>p2+p3 (Above), confirming they are exactly complementary — a cheap
     algebraic check once the closed forms are pinned down.
  3. Attack the final residual (compositions (1,1,0,0), (1,1,0,1),
     (2,0,0,0), concentrated at p1 in (0.43,0.50)T): derive a new
     p1,p2-cross-tie chamber type (splitting BOTH p1 and p2, per the
     explorer's finding that 2/3 of residual witnesses have this shape,
     NOT the previously-sketched but unverified Chamber B which the
     explorer found does not match the residual composition types) —
     apply the same Cross-Piece Sign-Assignment Identity machinery to a
     two-piece joint split.
  4. LP/vertex-check the new chamber via the already-certified
     p-space Chamber-Vertex Theorem (feasibility region is polyhedral in
     p-space, so g_tau>=0 on it iff it holds at finitely many vertices —
     cite, don't re-derive).
  5. Verify (exact-Fraction, large grid, then ideally exhaustive vertex
     check) that the FULL family (all certified chambers + the two new
     Double-Sandwich types + the new cross-tie type) covers case (b2)'s
     entire box at n=3 with no residual — this is the actual closure
     criterion per feasibility-suffices-for-upper-bound.
  6. If step 5 succeeds: state and prove the completed n=3 case (b2)
     theorem, combine with the already-closed case (a) and case (b1)
     regions to close the ENTIRE general upper bound at n=3 (cite
     unconditional-p2-threshold-closure for b1, and the already-closed
     p1>=T/2 case-(a) regime for n<=3), and honestly scope: this closes
     n=3's upper bound completely but says nothing about n>=4 yet.
  7. If step 5 does NOT fully close: report the exact residual honestly
     (as prior rounds have done), do not overclaim closure.
Key lemmas (claim + mechanism):
  - Double-Sandwich-Below/Above closed forms — because Cross-Piece
    Sign-Assignment Identity's rank-parity cancellation applies unchanged
    when a single split piece straddles two DIFFERENT untouched tail
    elements instead of one (the identity's mechanism is per-split-piece,
    not per-sandwiched-element, so this is a genuine but easy new
    instantiation, not new machinery).
  - Feasibility-suffices-for-upper-bound (certified, cite) — because the
    upper bound only needs SOME strategy in the union to beat a_nT at every
    point, not that any fixed strategy is globally optimal; this is why a
    finite union of polyhedral-feasibility chambers, once shown to cover
    the box, suffices for a complete proof (no further optimality argument
    needed).
Open gaps: the p1,p2-cross-tie chamber's closed form and feasibility region
are NOT yet derived (this round's actual target); whether the resulting
full family provably covers the box with ZERO residual (not just 99.9%+
numerically) is the closure criterion and remains open until step 5's
exact check passes.
Cases to cover: the 3 residual composition types (1,1,0,0), (1,1,0,1),
(2,0,0,0) must each be matched to some chamber in the extended family —
verify all three explicitly, not just the aggregate coverage percentage.
Watch out for: the residual is concentrated exactly at the case-(a)/(b2)
shared boundary p1->T/2, where both Double-Sandwich chambers' own
feasibility intervals degrade to nothing (p2+p3 also grows near that
boundary) — the new chamber must specifically remain feasible AT that
boundary, not just nearby; check the limiting behavior explicitly, don't
just spot-check interior points. Also: do not assume "reduces essentially
to p1<p2+p3" claims from the explorer's report are exact — they were
derived by numeric recovery; the builder must re-derive the exact
feasibility condition algebraically before relying on it in a rigorous
proof.
