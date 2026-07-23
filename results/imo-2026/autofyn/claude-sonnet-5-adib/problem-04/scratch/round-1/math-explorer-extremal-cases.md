## imo-2026-04

### Setup used throughout (fix notation for the outliner)
Triangle T=(A,B,C) (angles summing to 180). If Mulan cuts from apex X (angle X) to the
opposite side, choosing a point P that splits the base angles as "Y kept in piece1,
Z kept in piece2" (Y,Z the other two angles of T, Y+Z = 180-X), and lets a1 = angle
between the apex side AB and the cevian (so a1 ranges over the OPEN interval (0,X) since
P cannot be a vertex), then:
- piece1 has angles (Y, a1, 180-Y-a1)
- piece2 has angles (Z, X-a1, Y+a1)
Shan-Yu then picks which of piece1/piece2 survives. Mulan controls (choice of apex, choice
of which of the other two vertices plays "Y" vs "Z", and the real number a1); Shan-Yu only
controls the initial triangle and, at each round, which of the two children survives.

### Distinct openings
1. **One-shot "double hit" search**: look for a1 forcing BOTH piece1 and piece2 to contain
   angle θ simultaneously (so Shan-Yu loses in one move regardless of his choice). Solving
   the 2x2 system of "which slot in each piece equals θ" gives, in general, a *hyperplane*
   condition on the starting triangle (e.g. apex = 2θ) — not available against an adversarial
   Shan-Yu — **except** for one value where the condition collapses to an identity independent
   of the triangle's other angles: **θ = 90°**. Then B,C cancel algebraically and Mulan wins
   in exactly one move from *any* starting triangle (proved below, not just conjectured).
2. **General chaining fact (any θ)**: If the *current* triangle has some angle equal to n·θ
   for a positive integer n, Mulan wins in ≤ n−1 further moves. Proof idea (verified
   algebraically and numerically): cut the (nθ)-angle apex with a1=θ; piece1 = (Y, θ, (n−1)θ−Y)
   already contains θ (immediate win if Shan-Yu picks it); piece2 = (Z, (n−1)θ, Y+θ) inherits
   angle (n−1)θ, so induct. This is a genuinely general fact, true for every θ — but it only
   fires if the triangle already happens to have an angle that's an integer multiple of θ,
   which an adversarial Shan-Yu will simply avoid at the start (finitely many forbidden
   hyperplanes, easy to dodge). So this fact alone does NOT give a universal strategy; it
   only becomes universal when a *further*, sharper identity collapse (see opening 3) removes
   the need for the special starting hyperplane altogether.
3. **Boundary-degeneration lens (this is the crux extremal idea)**: the "double-hit" /
   "chain" identities above involve the quantity n·θ. As P sweeps a side, one of the two
   generated angles ranges over an open interval whose supremum is exactly the un-cut
   angle at the far vertex (or 180 minus it); the case analysis that makes an identity
   "universal" (independent of Y, Z, and hence of the initial triangle) happens exactly
   when n·θ hits the degenerate boundary value 180° — i.e. **θ = 180°/n**. Precisely at
   this value, the y-dependence cancels in the matching equations (verified symbolically,
   see below), producing a construction that works from *every* non-degenerate starting
   triangle, without requiring Shan-Yu's triangle to have any special angle at all.

### Candidate technique(s)
- Direct angle-chasing algebra on the two child-triangle angle triples (as above) — this is
  the natural technique and is fully elementary (no heavy machinery needed).
- Strong induction on n for the sufficiency direction (θ=180°/n ⇒ Mulan wins in ≤ n−1 or fewer
  moves, chaining the "has angle kθ ⇒ wins in k−1" lemma).
- For necessity (θ ≠ 180°/n ⇒ Shan-Yu wins forever), likely an evasion/invariant argument:
  Shan-Yu picks an initial triangle whose three angles avoid the (finite, since angles <180)
  forbidden set {θ, 2θ, 3θ, ...} ∩ (0,180), and needs a rule for always fleeing to the
  "safe" child; this smells like a monovariant/pigeonhole argument along the lines of KB's
  invariant techniques (see below) or a three-distance/continued-fraction style argument on
  180/θ, but this direction is NOT yet established — only the sufficiency (positive)
  direction has been nailed down computationally in this pass.

### Cheap-kill candidates
- **Parity/pigeonhole on angle sum**: every triangle has some angle ≤60° and some angle
  ≥60° (since the mean is 60°); this rules out any hope of a "STUCK forever, no angle ever
  crosses θ" type trivial argument for θ near 60°, but does not by itself resolve anything
  (60° itself IS in the conjectured winning set 180/3).
- **Range/feasibility check**: whenever invoking a construction, must verify 0 < a1 < X
  (apex angle) strictly — this is the source of the "P cannot be a vertex" constraint and
  is what makes the θ=90°, 60°, 45° constructions require "non-equilateral" or generic
  hypotheses (e.g. the θ=60° two-move construction needs the starting triangle's smallest
  angle < 60°, automatically true unless it's exactly equilateral, in which case θ=60° is
  already present at move 0).

### Knowledge-base entries to use
- Nothing in `knowledge_base.md` (skimmed: mostly synthetic-geometry configuration facts —
  Ceva/Menelaus, Ptolemy, power of a point, spiral similarity) directly matches this
  angle-arithmetic combinatorial-game problem; the relevant content here is really pure
  algebra on angle sums, not classical synthetic geometry. Flag to outliner: KB is likely
  NOT the primary resource for this problem; the crux corpus (below) and direct computation
  are more relevant.

### Analogous past problems (cruxes)
- Searched `combinatorics` domain, subtopics `games-and-strategy`, `invariants-and-monovariants`,
  `coloring-and-parity`, `induction-and-construction`. None of the 40 `games-and-strategy`
  cruxes and none of the sampled `invariants-and-monovariants` cruxes concern a continuous
  geometric state space (triangle angles) with an adversary discarding one of two pieces;
  they are all discrete combinatorial games (pairing/mirroring strategies, parity invariants,
  2-adic valuation games, token games). The closest in *spirit* (not substance) are the
  "maintain an invariant/monovariant so the opponent is eventually forced into a losing
  configuration" family (e.g. aimo-0236's two-phase valuation invariant, aimo-0631's
  guard-counter argument) — these are useful as a template for how to write the necessity
  (Shan-Yu's forever-evasion) argument once we have the right invariant, but none is a direct
  match. **Conclusion: no genuinely analogous crux found; this problem must be solved from
  first-principles angle algebra**, not adapted from a corpus match.

### Prior progress
None (this is round 1, no approaches file existed yet).

### Dead ends (do not retry)
- **"Naive greedy" Mulan strategy** (always try to force θ directly as a1 on whichever
  vertex has angle > θ, letting Shan-Yu flee to the complementary piece): verified by
  simulation (500+ random trials across θ ∈ {30,45,60,75,90,105,120,135,150,170,...}) that
  this produces short cycles (period 2–3) that repeat forever for essentially every θ tested
  except θ=90 (where it's a guaranteed immediate win) — i.e. this naive strategy is NOT
  Mulan's real strategy and does not detect the θ=60°, 45°, 36°, 30° wins at all (those
  require aiming for an intermediate target of 2θ or 3θ, not θ directly, on the first move).
  Do not present "cycling under naive play" as evidence that Mulan cannot win for a given θ —
  it only shows this *particular* simplistic strategy fails.

### Small-case / intuition notes (labeled: computed/verified vs conjectured)
- **Verified (exact algebra + numeric substitution, not just plausibility)**: θ = 90° —
  Mulan wins in exactly 1 move from ANY starting triangle without a 90° angle (choose apex =
  the vertex with the largest angle, i.e. whichever base pair B,C is both <90°, always
  possible since a triangle has at most one angle ≥90°; then a1 = 90°−B forces piece1 to
  have angle 90° via its third angle and piece2 to have angle 90° via B+a1).
- **Verified (exact algebra + numeric substitution)**: θ = 60° — Mulan wins in ≤2 moves from
  any non-equilateral starting triangle. Move 1: apex = largest angle X, Ybase = middle
  angle, Zbase = smallest angle (<60° unless equilateral); a1 = 120°−Ybase forces piece1 to
  contain 60° directly (Shan-Yu loses immediately if he keeps it) and forces piece2 to
  contain 120° (=2θ). Move 2 (only needed if Shan-Yu fled to piece2): from ANY triangle with
  a 120° angle, apex=120°, a1=60° forces BOTH children to contain 60°. Confirmed numerically
  on 5+ random triangles with exact substitution — all checks passed (a1 in valid range, both
  target angles hit as claimed).
- **Verified (exact algebra + numeric substitution)**: θ = 45° — Mulan wins in ≤2 moves from
  ANY starting triangle: move 1, apex = largest angle, Ybase = middle, a1 = 90°−Ybase forces
  BOTH children to contain 90° = 2θ (no hyperplane condition needed — fully universal, unlike
  the θ=60° case which needed non-equilateral). Move 2: any triangle with a 90° angle wins in
  1 more move by the θ=90° mechanism (with the roles of "θ" replaced appropriately — actually
  here we directly use the general "apex=2θ" lemma: apex=90°, a1=45° forces both children to
  45°). Confirmed numerically.
- **Conjectured, but backed by an exhaustive symbolic (SymPy) search**: extending the
  "which piece-slot equals target, for target ∈ {θ, 2θ}" system exhaustively over all 3×3
  slot/apex combinations and solving for which θ make the match hold *identically in Y, Z, X*
  (i.e. universally, not just on a hyperplane) yields **exactly θ ∈ {45, 60, 90}** — matching
  180°/4, 180°/3, 180°/2. Extending the target set to {θ, 2θ, 3θ} (one level deeper) yields
  **exactly θ ∈ {30, 36, 45, 60, 90}** = 180°/6, 180°/5, 180°/4, 180°/3, 180°/2. This is very
  strong evidence for the clean characterization:
  **Mulan can guarantee victory (for any starting triangle) if and only if θ = 180°/n for
  some integer n ≥ 2** (i.e. θ ∈ {90°, 60°, 45°, 36°, 30°, 180/7°, 22.5°, ...}).
  The sufficiency direction (θ=180°/n ⇒ Mulan wins, in some bounded number of moves ≤ n−1,
  likely fewer via shortcuts as seen for n=2,3,4) looks fully constructible by induction on n
  using the "apex = kθ forces one child to θ, other to (k−1)θ" chaining lemma above, seeded
  by proving the base "apex = 180°−θ, i.e. k=n−1 near the boundary, collapses universally" —
  this needs to be nailed down rigorously and generally (only checked case-by-case for n≤6 so
  far; the outliner should look for the GENERAL symbolic identity, likely of the same
  "B cancels" flavor, for arbitrary n, rather than re-deriving each n by hand).
  The **necessity direction is completely open** — no argument yet for why Shan-Yu can evade
  forever when θ is NOT 180°/n. Plausible approach: Shan-Yu picks a starting triangle with
  all three angles irrational multiples of θ (or more precisely, avoiding the closure of
  the finite forbidden set {θ,2θ,...}, which is easy since only finitely many hyperplanes to
  avoid), then argues by a continued-fraction/three-distance-theorem-style invariant that no
  finite sequence of cuts can force an exact hit unless the "180/θ ∈ ℤ" resonance condition
  holds. This needs real work next round — it is the outline's central remaining gap.
- All findings above are for 0<θ<180 as required; note θ=180°/n for n≥2 automatically gives
  θ≤90°, so if the conjecture is right, **no θ>90° is ever winnable for Mulan** (consistent
  with the STUCK behavior observed for large θ in the naive-strategy simulations, where large
  θ often has no available apex >θ to threaten with at all).
