## imo-2026-04 (lens: the hard open direction — forcing exact θ for 0°<θ<90°)

### Setup recap (from round 1, verified again by hand + exact-fraction code)
Cut vertex with angle α, other two angles β,γ, parameter x=∠(new vertex, first
sub-vertex) ∈(0,α):
child1={x,β,180−x−β}, child2={α−x,γ,x+β}.
Known 1-move wins: θ=90° (altitude, always available), α=2θ present (bisect).
Known "forced" (single-safe-successor) moves per (vertex,β/γ-assignment), each
puts θ into ONE child so Shan-Yu is compelled to keep the other:
- (i) x=θ ⟹ keeps {α−θ, γ, θ+β}           [needs α>θ]
- (iii) x=α−θ ⟹ keeps {α−θ, β, γ+θ}        [needs α>θ]
- (ii) x=180−β−θ ⟹ keeps {θ−γ, γ, 180−θ}   [needs θ>γ, 0<x<α]
- (iv) x=θ−β ⟹ keeps {θ−β, β, 180−θ}       [needs β<θ<α+β]
(ii)/(iv) are the "supplementary-pin" already flagged by round 1 — I did NOT
re-pursue that as the primary lead per the lens instructions; I instead
quantified its limits below and looked for genuinely different framings.

### Distinct openings (new framings, not the pin-and-pivot already on file)

**1. "Universal shared-value" moves — a second, independent move-family.**
Besides the θ-specific forced moves, there are exactly two move types where
BOTH children share a common angle regardless of β,γ (found by exhausting all
equal-slot combinations of {x,β,180−x−β} vs {α−x,γ,x+β}):
 - **Bisection**: x=α/2 ⟹ both children contain angle α/2 (always valid,
   0<α/2<α automatically). Gives Mulan a "safe experiment": whichever child
   Shan-Yu keeps, angle α/2 is present.
 - **Altitude**: x=90−β ⟹ both children contain angle 90 (valid iff both
   α,β given the acute-angle condition hold) — this is the general form of the
   known θ=90 win, degenerate for θ≠90.
 Neither alone hits generic θ: bisection needs α=2^k·θ (dyadic relation to the
 CURRENT angle, not the original θ — a measure-zero/special condition), so it
 is not a generic escape either. But it is a genuinely different tool from the
 forced-θ moves (it's an AND-node for Shan-Yu, not a forced single successor),
 worth keeping as an ingredient, not a keystone.

**2. Exact linear-recursion argument for why pure single-lineage forced
chaining is dead (sharpens, doesn't just repeat, round 1's residue finding).**
If Mulan always reapplies move (i) at the "same" growing vertex, the triple
evolves by the LINEAR map (α,β,γ) ↦ (α−θ, γ, θ+β). Iterating k times gives
α_k = α−kθ; this is literally the subtractive Euclidean algorithm on (α,θ).
It reaches exactly θ (or lands so the register hits 0 mod θ) only if α/θ is
rational with a specific denominator relationship — for irrational α/θ it
never terminates exactly. **This is now an explicit, checked-by-construction
argument** (not hand-wavy): pure lineage-chaining is provably insufficient,
confirming round 1 but via the cleaner "it's literally a linear recursion /
Euclidean algorithm" lens — worth stating this way in the outline since it
makes the impossibility rigorous rather than heuristic.

**3. Exact computational reachability check (NEW empirical data, exact
fractions, not float simulation) — the forced-menu-only reachable set from a
generic triangle is FINITE and CLOSED, missing the target.**
Ran an exact (Fraction-arithmetic) BFS closure of ALL forced moves (i)-(iv)
above, all vertex/assignment choices, from start=(100°,30°,50°), θ=40°. Result:
the closure is **exactly 14 states** (listed below), and neither θ=40 nor
2θ=80 ever appears — the process is fully closed (BFS terminates, no more new
states), so this isn't "not yet found in finite search depth," it is a
**complete, exact proof that from this particular start, the forced-move
menu alone can NEVER reach a win** (all reachable states have angles that are
multiples of 10°, consistent with gcd(100,30,50,40,180)=10, but even within
that residue class the specific reachable set of 14 triangles never contains
40 or 80). Reachable closure:
(10,20,150),(10,30,140),(10,60,110),(10,70,100),(20,20,140),(20,30,130),
(20,50,110),(20,60,100),(20,70,90),(30,50,100),(30,60,90),(50,60,70),
(60,60,60),(100,30,50) [start].
I then added the bisection move (as a proper AND-node: Mulan only "wins via
bisection" if BOTH resulting children are themselves winning, or one already
contains θ/2θ) to a bounded minimax (memoized, depth ≤6): **still no win
found** for this same start/θ within depth 6. This is a genuinely NEW,
concrete negative data point (round 1 only conjectured a strategy exists but
never checked a hard concrete instance) — it shows the two known move
families (forced-θ menu + bisection) are, together, insufficient even at
modest depth for at least one adversarial start/θ pair. This does not refute
the θ≤90° conjecture (Mulan surely has more freedom — arbitrary real x, not
just the handful of "nice" x values checked), but it is strong evidence that
**any winning strategy must use genuinely continuous/adaptive x-choices with
real two-move (or more) lookahead, not a small closed menu of algebraic
triggers** — recommend the outliner NOT attempt a "bounded case-check over a
short trigger list" proof; it looks empirically false for this instance.

**4. Reframing recommendation for the outliner: full-continuum two-move
lookahead, not a discrete menu.** Since discrete triggers fail on
(100,30,50)/θ=40, the real strategy likely needs: pick x in move 1 not to hit
an exact trigger, but to land the surviving (whichever child Shan-Yu takes)
triangle into a *family* for which move 2 (with x again free, chosen after
seeing which child Shan-Yu kept) can always close. This is a genuine 2-ply
game-tree argument with a continuous free parameter at both plies — harder to
verify by hand/brute force than a trigger search, but plausible as an
IMO-P4-level argument. I did not construct it (out of scope for exploration),
but flag it as the recommended target: "does there exist, for every
non-degenerate triangle and every θ<90°, an x₁ such that for BOTH possible
Shan-Yu replies, some x₂ forces a win (or forces α=2θ for a 1-move finish)?"
— i.e. search for a genuine 2-move (not 1-move) forced/AND win, generalizing
the single successful 1-move analysis in round 1's strategy report.

**5. Density/IVT framing — explicitly ruled out, do not pursue as a
standalone proof.** Because the target is an EXACT angle (not a limit), and
the KB's own Kronecker/Weyl equidistribution entry (knowledge_base.md line
102) only gives density/approximation, NOT exact hits, for irrational
rotation numbers — this matches finding 2 above (linear-recursion dead end)
and should not be resurrected as "eventually gets arbitrarily close, so some
continuity argument finishes it": angles are exact reals fixed by algebra,
there's no rounding/limiting step available in this game.

### Candidate technique(s)
- 2-ply (or bounded k-ply) minimax over Mulan's continuous x at EACH ply,
  with Shan-Yu's discrete choice as the AND-node — this is the technique
  shape the problem needs; it is NOT a single deterministic chain and NOT a
  discrete trigger-menu search (both empirically fail on the test instance).
- Possibly needs an inductive scheme on a monovariant like "the number of
  angles currently > θ" or "max angle − θ," proved to strictly decrease under
  a well-chosen 2-move combo, rather than a closed-form single formula.

### Cheap-kill candidates
- None new beyond round 1's (θ=90 altitude, α=2θ bisect, θ>90 non-obtuse
  invariant). No cheap kill found for the θ<90 direction itself — this
  confirms round 1's read that θ<90 is the genuinely hard remaining case, not
  amenable to a one-line trick.

### Knowledge-base entries to use
- `Invariants & monovariants` (combinatorics section) — for constructing
  whatever discrete quantity decreases across Mulan's 2-move combos.
- `Kronecker / Weyl equidistribution` (number theory section, line 102) —
  explicitly NOT sufficient here (exact hit needed); cite only to justify
  ruling OUT the density approach, per finding 5.
- `Pigeonhole / extremal principle` — possibly for a "some vertex-choice among
  3 must work" argument at each ply (extremal/exhaustion over the 3 vertices).
- No entry directly gives the win construction; this remains a from-scratch
  construction as round 1 found.

### Analogous past problems (cruxes)
Did not find new analogs beyond round 1's negative result (no geometry cruxes
in corpus; `aimo-0225`/`aimo-0663` are distant cousins only in the general
"invariant/monovariant for adversary-survives-forever" technique, not in
setup). Confirming round 1: no crux to import for the θ<90 direction.

### Prior progress
Still none formally in `results/imo-2026-04/current.md` / `approaches/` (empty
as of this round) — round 1 explorers wrote reports but no outliner/builder
cycle has run yet for this problem. Round-1 findings (θ=90 win, α=2θ win,
θ>90 non-obtuse defense) remain the only *fully proved* pieces; everything for
θ<90° is still open.

### Dead ends (do not retry)
- **Pure single-lineage forced-θ chaining** (repeatedly applying move (i) or
  (ii)/(iv) at one evolving vertex): proved dead via the explicit linear
  recursion (finding 2) — not just "residue mod θ," it literally IS the
  subtractive Euclidean algorithm on (α,θ), which fails to terminate exactly
  for irrational ratios.
- **Discrete "trigger menu" search (forced moves (i)-(iv) + bisection) as a
  bounded-depth complete strategy**: computationally refuted (exact fractions,
  not float) for the concrete instance start=(100°,30°,50°), θ=40° — the
  forced-only closure is a FINITE 14-state set that never contains 40 or 80,
  and adding bisection AND-node search to depth 6 still finds no win. Do not
  present a "short case-check over these ~15 algebraic move types" as a
  complete proof; it is false on this instance. Any winning strategy needs
  genuinely free/continuous x-choices beyond this menu.
- **Density/limiting arguments (Kronecker equidistribution as the finisher)**:
  ruled out because the target must be hit exactly, not approximated.

### Small-case / intuition notes
- **Exact (not simulated) finding**: from (100°,30°,50°), θ=40°, the set of
  triangles reachable via ONLY the four named forced-θ moves is exactly the
  14 states listed in opening 3 above — a closed, finite, fully enumerated
  set, confirmed by BFS-to-closure (no cap hit, no cycle-avoidance shortcut
  needed, genuinely exhausted).
- **Conjecture, now under more doubt than round 1's optimistic take**: Mulan
  wins for all 0°<θ≤90° from any start. Round 1 treated the θ<90 case as
  "very likely true, just needs construction." My exact reachability check
  shows the natural discrete-move candidates are NOT enough even at depth 6
  for a fairly mild instance (θ=40°, no extreme angles) — so either (a) the
  correct strategy is a genuinely richer continuous 2-ply argument not yet
  found (most likely, given this is IMO P4/hard difficulty), or (b) the
  characterization needs refinement beyond "all θ≤90". I recommend the
  outliner explicitly budget a builder-side computational check (a small,
  bounded, TIME-CAPPED continuous-x minimax, e.g. depth ≤3 with x discretized
  finely only as a sanity probe, not a proof) for a couple of hard instances
  before committing to "θ≤90 always winnable" as the target characterization.
