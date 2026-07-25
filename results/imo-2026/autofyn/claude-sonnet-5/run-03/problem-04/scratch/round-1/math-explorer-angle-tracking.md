## imo-2026-04 (Mulan's Triangle Game) — angle-tracking / angle-arithmetic route

### Setup and exact formulas (verified by exterior-angle theorem)

Triangle T has angles A (at vertex being cut), B, C (A+B+C=180°). Mulan cuts from
vertex A to a point P on side BC, with A split into A1+A2=A (A1 = angle BAP, A2 =
angle CAP; as P ranges continuously over the open side BC, A1 ranges continuously
over the *open* interval (0,A), each value attained exactly once — degenerate as
P→B (A1→0) or P→C (A1→A), never attained at the endpoints since P is not a vertex).

By the exterior-angle theorem, the two children are:
- **child1 = ABP**: angles {B, A1, C+A2}
- **child2 = ACP**: angles {C, A2, B+A1}

(the two new angles at P, namely C+A2 and B+A1, are supplementary: (C+A2)+(B+A1)=
A+B+C=180°, consistent with P lying on a straight line.) This is the whole state
space of one move: Mulan picks a vertex (3 choices) and a real A1 ∈ (0,A) (1
continuous choice); Shan-Yu picks child1 or child2.

### Key structural fact 1 — the doubling fork (single-move double-threat)

Solving "θ ∈ child1 AND θ ∈ child2" for A1 (excluding the impossible B=θ, C=θ,
A=θ cases, since if any current angle already equals θ the game already ended):
the *only* consistent solutions are
- **A = 2θ** with A1=A2=θ (bisect the vertex of size 2θ): then BOTH children
  automatically contain θ, so whichever Shan-Yu keeps, Mulan has already won.
  This generalizes to a "doubling cascade": if T has a vertex angle X = 2^k·θ
  (for k≥0, and 2^k·θ<180 so it's a valid angle), Mulan can force a win in
  exactly k more moves by repeatedly bisecting *that same vertex* (ignore
  B, C entirely) — every bisection sends X → X/2, X/2 at *both* children, so
  Shan-Yu's discard is irrelevant. Verified: this cascade needs the current
  triangle to already carry such a vertex; it is not automatic for the actual
  game since Shan-Yu can trivially avoid the finite doubling orbit
  {θ,2θ,4θ,...} in his three initial angles. So this fork alone is a *building
  block*, not the whole proof.
- **θ = 90°, independent of A,B,C** (any triangle): solving the "both P-angles
  hit θ" system forces 2θ=180. Concretely this is the classical altitude
  construction: drop the altitude from whichever vertex has both adjacent
  base angles < 90° (always exists, since a triangle has at most one angle
  ≥ 90°). Both resulting right triangles have a 90° angle at the foot, so
  **θ=90° is an instant, universal 1-move win for Mulan regardless of the
  initial triangle.** This is a clean, fully rigorous sub-result — good
  anchor/base case for an induction.

No other single-move fork exists (the other two of the 4 possible sign
combinations force B=0 or C=0, impossible).

### Key structural fact 2 — numerical safety-game computation (strong evidence, not proof)

I implemented the standard backward-induction "attractor" for this
reachability/safety game: U₀ = triangles already containing angle θ; Uₖ₊₁ =
Uₖ ∪ {T : ∃ a Mulan cut such that BOTH children ∈ Uₖ} (this is exactly "Mulan
forces a win from T in ≤k+1 moves" — standard construction for
reachability-vs-safety games, cf. knowledge_base.md "Invariants & monovariants"
/ "Extremal principle"). I discretized the angle simplex on an exact-rational
grid (Python `fractions.Fraction`, to eliminate floating-point artifacts —
this mattered a lot, see Dead ends) with grid step dividing both θ and 180°,
and iterated to a fixed point. Results (exact-rational, multiple resolutions
each, robust and stable):

- θ = 180/n for n = 2,3,4,5,6,7,9,11,13 (i.e. 90°, 60°, 45°, 36°, 30°,
  180/7°, 20°, 180/11°, 180/13°): **attractor reaches the FULL grid** (every
  triangle is captured, i.e. Mulan wins from any starting triangle),
  stably across step refinements, converging in a small number of iterations
  (iters grows mildly with n: 1 for n=2, 2 for n=3–6, 3 for n=7, 4 for n=9,11,13
  — suggestive of an O(log n) or similar move-count strategy).
- θ = 40, 50, 70, 72, 80, 89, 91, 100, 108, 120, 144, 150 (none of the form
  180/n): **attractor stalls at a small, non-full subset** and this is stable
  under refinement (not a resolution artifact — verified with exact fractions
  at 5 increasing resolutions each, coverage stays a small fraction, e.g.
  θ=100: 2/7 → 22/817 as resolution increases, clearly not approaching 100%).

This is **strong numerical evidence** (not a proof — coarse discretization
can never fully certify a continuum game) for the conjecture:

> **Mulan has a winning strategy iff θ = 180°/n for some integer n ≥ 2**
> (equivalently: 180°/θ is a positive integer ≥ 2, i.e. nθ = 180° exactly).

This is a clean "characterization" answer of exactly the flavor the problem
metadata (`answer_type: characterization`) expects, and it is consistent with
both anchors found analytically: n=2 (θ=90°, proved rigorously above) and the
non-full status of generic θ (89°, 91°, 100°, ... all fail, matching that they
are not 180/n for integer n).

### Distinct openings for the outliner

1. **Direct doubling-cascade construction for θ=180/n (the "if" direction).**
   Try to prove by induction on n that Mulan can always force an angle 2θ (or
   more generally an integer multiple kθ, k<n) to appear in a way that
   survives Shan-Yu's discard, using the fact that A+B+C=180=nθ. The n=2 case
   (altitude, θ=90°) is fully solved and could be the base case. Need to find
   the general one/two-move gadget that reduces "any triangle with angle-sum
   nθ" to "some descendant with angle-sum (n-1)θ has a forceable θ", i.e. an
   induction on n rather than a single global fork. This is the most promising
   concrete route — the n=2 case is a template.

2. **Exclusion argument for θ≠180/n (the "only if" direction) via an
   invariant Shan-Yu maintains.** Candidate: some notion of "θ-freeness" of
   the angle triple that persists under discard — e.g. track angles modulo θ,
   or track the set of rational relations among {A,B,C,θ}, and show Shan-Yu
   can always choose a discard preserving "no angle is within reach of θ via
   the two fork mechanisms." My attempt at a naive "min angle ≥ Δ" invariant
   failed self-consistency (Mulan can always attack the currently-smallest
   vertex and roughly halve it, defeating any fixed lower bound) — flag this
   as a **dead end**, do not retry a static min-angle invariant without
   modification. A more promising angle: since 180=nθ fails only when n is
   not an integer, an invariant based on **irrationality/incommensurability
   of θ with 180°**, or on a discrete residue argument mod θ, is more likely
   to be the right tool — worth checking the crux corpus's
   `cyclotomic-and-roots-of-unity` / `modular-arithmetic-and-CRT` techniques
   for angle-relation arguments (see below).

3. **Direct algebraic route via aimo-0355's technique (tangential, worth
   testing).** That crux shows how integer linear relations among a
   triangle's angles reduce (via A+B+C=180) to statements about cosines of
   integer multiples, i.e. `cos(rα)=±cos(sγ)`, then to rational/Chebyshev
   polynomial identities, then to prime-support-of-denominator arguments.
   This machinery is a candidate for making rigorous exactly *why* the
   forcing works precisely when θ divides 180 evenly (an integer multiplicity
   condition), and could plausibly supply the "only if" (Shan-Yu-survives)
   direction by an analogous denominator/prime-support obstruction when
   180/θ is not an integer.

### Cheap-kill candidates

- **Immediate checks Shan-Yu must satisfy to survive at all**: his initial
  triangle just needs A,B,C ≠ θ — trivial to satisfy, no cheap kill there.
- **θ=90° is fully solved analytically** (see above) — can be lifted directly
  into a proof as the base case; no further exploration needed on that value.
- **Parity/pigeonhole**: a triangle always has an angle ≥60°; this bounds
  180−(max angle) ≤120°, hinting 120° might be some structural threshold, but
  the numerics *refute* a simple "θ≤120° always works" — 120° itself,
  100°, 150° all fail while much smaller non-divisor θ (40°,50°,70°,72°,80°)
  also fail. So the size of θ alone is not the determining quantity — it is
  the divisibility of 180 by θ. This rules out any monotone-in-θ threshold
  characterization; do not pursue a "θ ≤ c" style answer.

### Knowledge-base entries to use

- `knowledge_base.md` **Combinatorics**: "Invariants & monovariants" (for the
  Shan-Yu survival direction) and "Pigeonhole / extremal principle" (used
  above for the max-angle≥60° fact, though it turned out not to be the
  determining threshold).
- `knowledge_base.md` **Geometry**: "Synthetic toolkit" (angle chasing,
  exterior-angle theorem — already the backbone of the child-angle formulas
  above) and "Trig identities & interval intersection" style reasoning may be
  useful for turning the continuum choice of A1 into precise interval
  arguments.
- `knowledge_base.md` **General Proof Methods** / **Meta-Strategy**: this is
  fundamentally a two-player reachability/safety game — standard
  backward-induction (attractor) framing, which is what the numerical check
  used; the outliner should consider stating the proof in these terms
  explicitly (Mulan = reachability player, Shan-Yu = safety player).

### Analogous past problems (cruxes)

- **aimo-0355** (number_theory, subtopics `modular-arithmetic-and-CRT` /
  `cyclotomic-and-roots-of-unity` / `p-adic-valuation`): triangle-angle
  problem using `A+B+C=180°` to collapse an integer linear relation among the
  angles into `cos(rα)=±cos(sγ)`, then Chebyshev-polynomial and
  denominator/prime-support arguments. Not the same problem, but the
  *technique* (turning a triangle-angle-sum relation into an integer-multiple
  cosine identity, then an algebraic obstruction) is the best candidate found
  in the corpus for proving the "only if" direction rigorously. Genuinely
  analogous in spirit (angle relations forced by 180° sum), though the
  mechanics differ (that problem is about a fixed triangle's own angles being
  related; ours is about a *process* generating new angles).
- I searched `domain=combinatorics`, `subtopic=games-and-strategy` (39
  entries) and `subtopic=processes-and-algorithms`; none involve a
  continuous/geometric parameter (all are discrete combinatorial games —
  pairing/mirroring strategies, parity invariants, valuation-based token
  games). **None of these are genuinely analogous** — this game's defining
  feature (Mulan has a *continuum* of moves each turn, Shan-Yu has a *binary*
  choice) has no discrete-game analogue in the sampled corpus. Do not force a
  mirroring/pairing strategy template onto this problem; the structure is
  fundamentally different (continuous choice vs discrete matching).

### Prior progress

None (results/imo-2026-04/ was empty at start of this round).

### Dead ends (do not retry)

- **Naive static "min angle ≥ Δ" invariant for Shan-Yu**: fails
  self-consistency — Mulan can always attack whichever vertex currently has
  the smallest angle m (< 2Δ once the invariant is tight) and bisect it,
  putting an angle < Δ into *both* children, defeating any fixed positive
  lower bound. Any survival-invariant proposal must be more refined than a
  single scalar bound.
- **Floating-point grid simulation**: using Python floats for grid steps that
  are non-terminating decimals (e.g. θ=180/7) produces *spurious* "not full"
  results purely from rounding/misalignment of the grid — do NOT trust
  float-based discretized game simulations for this problem; always use
  exact rational arithmetic (`fractions.Fraction`) with the grid step chosen
  to exactly divide both θ and 180°, or the negative results are unreliable
  artifacts, not real obstructions.
- **A simple "θ ≤ threshold" style answer** is refuted by the numerics (90°
  works, but 80°, 70°, 50°, 40° — all smaller than 90° — do not; 120°, 100°
  fail while 180/7≈25.7° works). The answer is a divisibility/rationality
  condition, not a size threshold.

### Small-case / intuition notes (all conjectural, numerically supported)

- θ=90°: **proved** (not just conjectured) — universal 1-move win via
  altitude from the vertex with two acute base angles (always exists).
- θ=60°, 45°, 36°, 30°, 180/7°, 20°, 180/11°, 180/13° (all = 180/n, n=3..13
  tested): conjectured wins, strongly supported by exact-rational
  backward-induction computation reaching 100% of a fine discretized grid,
  stable across resolution refinements.
- θ=40°,50°,70°,72°,80°,89°,91°,100°,108°,120°,144°,150° (none of the form
  180/n): conjectured Shan-Yu survives, supported by the attractor stalling
  at a small, stable (non-artifact) fraction of the grid across multiple
  resolutions.
- Overall conjectured answer: **Mulan wins iff θ = 180°/n for some integer
  n ≥ 2.**
