## imo-2026-04 (Mulan's Triangle Game) — lens: Shan-Yu survival / invariant route

### Setup recap (derived from scratch, needed since population is empty)
Current triangle has angles X, Y, Z (X+Y+Z=180). A move: Mulan picks which angle to
"split" (equivalently, which side to put P on — P on side opposite vertex with that
angle) and a real split value Z1 ∈ (0,Z), Z2 = Z − Z1. This produces two candidate
children:
- Child1 = {X, Z1, Y+Z2}
- Child2 = {Y, Z2, X+Z1}
(X, Y are the two *un-split* angles; each survives **unchanged** into exactly one
child, and the third angle in each child is a *compound* sum of the other preserved
angle plus the leftover split piece.) Shan-Yu picks one child to keep. Mulan wants to
force an angle = θ in finitely many moves regardless of Shan-Yu's choices (both at the
very first triangle and at every subsequent pick).

This algebraic form (X,Z1,Y+Z2)/(Y,Z2,X+Z1) is the whole game; everything below follows
from it.

### Main rigorous finding (Shan-Yu's side): θ > 90° ⇒ Shan-Yu survives forever
**Claim.** For every θ ∈ (90°,180°), Shan-Yu wins: start with any non-obtuse triangle
(e.g. equilateral 60-60-60) and always respond by keeping a child whose max angle is
≤ 90°. This is forward-invariant under *every* possible Mulan move, hence the triangle
is non-obtuse forever, so it can never show an angle θ>90°.

**Proof of invariance (worked out in full, not just sketched):**
Let the current triangle have angles a ≤ b ≤ c ≤ 90 (non-obtuse, so a,b < 90 strictly
unless c=90 exactly — either way a,b<90).
- If Mulan splits a or b (not the max c): the child that keeps c unchanged is always
  one of the two options (since exactly one child inherits each un-split angle
  untouched); Shan-Yu takes it — max angle unchanged, still ≤90. Trivial case.
- If Mulan splits the max angle c itself (base angles a,b, both <90 by the above):
  Child1={a,c1,b+c2}, Child2={b,c2,a+c1}, c1+c2=c.
  Child1 exceeds 90 iff b+c2>90 iff c1 < c−90+b.
  Child2 exceeds 90 iff a+c1>90 iff c1 > 90−a.
  Since a+b+c=180 exactly, c−90+b = 90−a, i.e. the two "danger" thresholds *coincide
  exactly* at c1* = 90−a = c−90+b. For c1 < c1*, Child2 is safe (≤90); for c1 > c1*,
  Child1 is safe (≤90); at c1 = c1* exactly, BOTH children have their third angle
  exactly 90 (this is the classical "cut from the vertex to the foot of the altitude"
  point, producing two right triangles) — still non-obtuse, safe. So **it is impossible
  for both children to exceed 90 simultaneously** (their sum b+c2 + a+c1 = a+b+c = 180
  forces at most one of the two can exceed 90). Shan-Yu always has an escape.

This is a clean, complete, self-contained proof (no gaps) that θ>90° is *never*
forceable — I'm confident this is a correct half of the final characterization and
should be the "Shan-Yu wins" branch of the answer.

### The boundary is sharp at θ=90°: Mulan wins θ=90 in ONE move
From ANY triangle, at most one angle is ≥90°, so at least one vertex has both *other*
angles acute. Cut from that vertex to the foot of the perpendicular on the opposite
side (i.e., choose the split value c1 = c1* = 90−a from the analysis above). Both
resulting children get a 90° angle exactly (this is exactly the boundary case worked
out above). So θ=90° is forced in 1 move, universally — Shan-Yu cannot avoid it even
by choice of starting triangle. This pins the survival region to be an **open**
interval below 180 with right endpoint at most 90 (strictly excluding 90).

### Evidence Mulan also wins many/all θ < 90° (so survival region is likely exactly
θ∈(90°,180°), NOT a wider set)
I checked whether Shan-Yu might have a *second* invariant defending some sub-range of
θ<90 (symmetric to the max≤90 idea, e.g. "min ≥ L" or "max < θ"). Findings:
- "Maintain max < θ" for a fixed 60<θ<90 is **not** invariant: redoing the same
  covering computation with threshold θ instead of 90 gives danger intervals that
  overlap into a genuine *gap* c1 ∈ [θ−a, c−θ+b] whenever a+b+c=180 < 2θ (i.e. θ>90) —
  which is exactly backwards: for θ<90, 180>2θ so the two safe regions do NOT cover
  (0,c); there is a nonempty range where **both** children have some angle ≥ θ. This
  shows "keep everything below θ" cannot be maintained for θ<90 — it's the mirror image
  of the θ>90 result, and it points the *opposite* way (toward Mulan, not Shan-Yu).
  (Exact equality of the exceeding angle to θ still needs one further step — see below —
  but the point is this defense structurally fails for θ<90, unlike the θ>90 case where
  it structurally succeeds.)
- Direct constructive verification that Mulan forces specific θ<90 values: I verified
  by hand (exact arithmetic, not just numerics) that θ=45° is forced in exactly 2 moves
  from an arbitrary example: start (50,60,70) → altitude-move gives {50,40,90} or
  {60,30,90} (both contain 90, Shan-Yu picks either) → bisect the 90° angle into 45+45:
  from {50,40,90}, splitting the 90 gives {50,45,85} and {40,45,95} — **both contain
  45 exactly**, regardless of which Shan-Yu picked at step 1. This generalizes: from ANY
  starting triangle, "force 90 (1 move, universal) then bisect repeatedly" forces every
  θ = 90/2^k (k=0,1,2,...) in k+1 moves, universally (dyadic-from-90 family). This
  directly refutes any hope that Shan-Yu survives *all* of θ<90 — some values there are
  definitely lost for him.
- I attempted (but did not complete — this is the real gap for the outliner/builder)
  a *general* argument for arbitrary θ<90 via: force a right triangle {90,V,90-V} (V
  adversarial, whatever Shan-Yu steers to), then split the small leg-angle V into
  (V−θ, θ): the branch preserving the right angle becomes {90,θ,90−θ} (contains θ,
  Shan-Yu declines) and the other becomes {90−V, V−θ, 90+θ} (obtuse, escapes). So a
  single such move only threatens one branch; Shan-Yu can always fee into an obtuse
  triangle with angle exactly 90+θ. Whether Mulan can always eventually corner Shan-Yu
  from there (using further such splits, recursively, since 90+θ>90 is now a "big"
  angle Mulan can attack again) is NOT yet established — this is the key missing lemma.
  I recommend the outliner either (a) find a smarter direct 2-move (or O(log) move)
  universal construction for general θ<90 generalizing the θ=90/2^k trick (e.g. does
  splitting the *acute* angle of a forced right triangle into (θ, V−θ) and then chasing
  the escaped obtuse branch with a **second** altitude-style double-force work?), or
  (b) set up an induction/potential argument (e.g. on the "gap" |current forceable
  value − θ| or on integer k such that 2^k·θ crosses some threshold) proving Mulan
  always wins for θ<90.

### Distinct openings for this lens
1. **Non-obtuse invariant (COMPLETE)** — proves θ>90° is Shan-Yu-safe. Ready to drop
   into an approach as a fully rigorous lemma.
2. **Altitude / right-angle universal one-move force (COMPLETE)** — proves θ=90° is a
   forced Mulan win in 1 move from any starting triangle. Also the technical engine
   behind item 1 (same computation, boundary case).
3. **Bisection cascade from 90 (dyadic family, COMPLETE for θ=90/2^k, k≥0)** — gives
   Mulan wins for a countable dyadic subfamily of θ<90; refutes any "θ<90 is entirely
   safe" hypothesis.
4. **Right-triangle-shrinking / escape-to-obtuse chase (OPEN, sketched not proved)** —
   the likely route to close the gap for all θ<90; needs a recursive/potential
   argument. This is the natural next target for the outliner.
5. Alternative framing to consider: think of the problem as "Mulan always has 1-move
   universal double-force exactly at θ=90 (only solution to X+Y+Z=180 symmetric
   equation), everything else needs adaptive multi-move play" — the outliner could look
   for an inductive scheme on "the smallest number of moves to reduce max(θ,180−θ...)"
   type potential, or try a change of variables (e.g. work with 90−angle or tan of
   half-angle) to see if the recursion linearizes.

### Cheap-kill candidates
- Immediate structural fact used above: **every triangle has at least one angle ≤60°
  and at least one angle ≥60°** (sum=180, avg=60) — did not end up load-bearing for the
  θ=90 boundary (which is the one that matters), but flag it: if further work reveals
  60° behaves specially (it doesn't, per my analysis — 90° is the load-bearing constant,
  not 60°), revisit.
- Parity/degenerate-case check: split value Z1 ranges over an **open** interval (0,Z);
  boundary values Z1→0 or Z1→Z are never attained (P must differ from the vertices), so
  any "exactly at the boundary" construction (like the altitude trick, or exact
  bisection) must be double-checked to lie strictly inside (0,Z) — I verified this in
  both the altitude trick (c1*=90−a ∈ (0,c) since a<90<... need 0<90−a<c, i.e. a<90 ✓
  and c>90−a i.e. a+c>90 i.e. b<90 ✓, both hold since a,b<90) and the bisection
  (Z1=Z2=Z/2 ∈(0,Z) whenever Z>0, always true). So no degenerate-boundary issue in the
  constructions found so far — a "cheap kill" the outliner should still verify in any
  final writeup but it holds up.

### Knowledge-base entries to use
- **Invariants & monovariants** (combinatorics section, line ~117, and General Proof
  Methods line ~191) — directly the technique used for the θ>90 result.
- **Synthetic toolkit: angle chasing** (Geometry section, line ~129) — the whole
  problem is angle chasing under a controlled/adversarial split.
- **Piecewise-concavity smoothing** (Algebra, line ~20) is NOT directly relevant here
  (that's for optimizing a function over a simplex) but the "at most one of two linear
  quantities can exceed a threshold when their sum is fixed" argument in my θ>90 proof
  has the same flavor (a fixed-sum linear covering argument) — worth citing loosely as
  a technique pattern, not a named theorem.
- No number-theory KB entries apply; this is a pure real-angle combinatorial game.

### Analogous past problems (crux corpus)
Searched crux corpus filtered on `domain=combinatorics`, `subtopic ∈
{games-and-strategy, invariants-and-monovariants, processes-and-algorithms}` plus
keyword scan for "angle"/"triangle". Findings:
- **aimo-0355** (quirky triangle / integer relations among angles θ1,θ2,θ3 of a
  (n-1,n,n+1) triangle) — same *domain* (triangle angle relations) but a totally
  different mechanism (Chebyshev-polynomial / algebraic-number technique for rational
  linear relations among fixed angles). **Not analogous** to this game — no adversarial
  process, no cutting. Do not force this crux; it's superficially about triangle angles
  only.
- **aimo-0225** ("strategy-stealing symmetry", "2-adic valuation recursion for P/N
  status") — an adversarial combinatorial game with a valuation-based recursive
  win/loss classification. The *flavor* (finding the exact recursive threshold /
  invariant that separates player-1-wins from player-2-wins positions) is the closest
  structural analogy I found to what's needed to close the θ<90 gap, but the actual
  mechanics (2-adic valuation on integers) don't transfer.
- **aimo-0121 / aimo-0193** (monovariant = running max, bound moves by "total rise");
  **aimo-0196** (potential/monovariant games with adversarial responses, draining a
  window's total by a fixed amount each round) — general pattern-match for "maintain an
  invariant against an adversary" but no triangle/angle content.
- **Verdict: no crux in the corpus is a close structural analog of this specific
  cut-a-triangle game.** The corpus doesn't seem to contain a continuous-geometry
  pursuit game like this one; recommend leaning on the direct computation above rather
  than trying to force-fit a crux.

### Prior progress
None — population was empty at the start of this round (results/imo-2026-04/approaches/
and lemmas/ both empty). This report is first-round reconnaissance.

### Dead ends (do not retry)
- **"Shan-Yu maintains min angle ≥ L forever" for any fixed L>0** — false. Mulan can
  always bisect the current minimum angle a into a/2,a/2; both children get an angle
  a/2 forced (verified: a/2 remains the new minimum in both children), so min angle can
  be driven below any threshold in finitely many forced moves. Do not propose this as a
  Shan-Yu defense for small θ.
- **"Shan-Yu maintains all angles < θ forever" for 60<θ<90** — false; shown above the
  safe-interval covering argument fails in exactly the wrong direction for θ<90 (leaves
  a gap where both children exceed θ), unlike the θ>90 case where the same argument
  shows no gap can exist. Don't waste a round re-deriving this; the sum-of-angles
  identity a+b+c=180 makes it *provably* impossible to mirror the θ>90 defense below
  90.
- **"θ<90 is entirely safe for Shan-Yu" (naive complement-of-90 conjecture)** — false,
  refuted by the explicit θ=45° 2-move construction verified above with exact
  arithmetic on a concrete example (50,60,70)→{50,40,90}/{60,30,90}→{50,45,85}/{40,45,95}.

### Small-case / intuition notes (labeled conjecture where not proved)
- **Conjectured final answer:** Mulan guarantees victory iff **θ ∈ (0°,90°]**; Shan-Yu
  survives forever iff **θ ∈ (90°,180°)**. The θ>90 half is PROVED (rigorous, see
  above). The θ≤90 half is proved only for θ=90 (1 move) and the dyadic family
  90/2^k (k+1 moves); general θ<90 is a real open gap needing a genuinely new
  construction or induction — flag this clearly to the outliner as the one lemma that
  must be filled to reach `solved`.
- Sanity check of the conjecture against the problem's own difficulty (`difficulty_rating:
  7`, listed `medium` not `hard` in problems.jsonl despite being IMO P4 — worth noting to
  the run, though CLAUDE.md says target only "hard"-tagged problems; this run may be a
  deliberate exception since it was explicitly assigned) — a clean θ>90/θ≤90 threshold
  at exactly 90° (a single geometrically meaningful constant, tied to the altitude/right
  -angle construction) matches the "clean characterization" style expected of an IMO
  answer, reinforcing the conjecture but not proving it.
