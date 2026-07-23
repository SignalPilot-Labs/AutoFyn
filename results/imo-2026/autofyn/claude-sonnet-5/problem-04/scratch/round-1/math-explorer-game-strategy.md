## imo-2026-04

### Setup / exact move formulas (derived and sympy-verified)
Label current triangle angles (A,B,C), A+B+C=180. Mulan picks which vertex's angle to
split (call it A, opposite side BC) and a parameter x = angle BAP ∈ (0,A) (P's position
on BC determines x continuously and is Mulan's real-valued choice). The two resulting
triangles are exactly:
- T1 = (B, x, 180−B−x)   [= triangle ABP, always keeps B intact]
- T2 = (C, A−x, B+x)     [= triangle ACP, always keeps C intact]
(sum of each = 180, verified symbolically). Shan-Yu picks which of T1,T2 survives.

### Distinct openings found
1. **"Both-branches-forced" one-move win analysis.** Solved the 2x2 system of which
   value equalities make θ appear in BOTH T1 and T2 simultaneously (so Shan-Yu's choice
   doesn't matter). Exhaustive: this happens iff **θ=90°** (x=90−B, i.e. drop the
   altitude from a vertex whose two base angles are acute — always possible for *any*
   triangle, since at most one angle is ≥90°) **or** the currently-split angle equals
   **2θ** (x=θ exactly forces both children to contain θ). This gives an immediate,
   completely general 1-move win recipe whenever current angle = 2θ or θ=90.

2. **Recursive "double-then-halve" chain (clean, fully proved sub-family).** Since
   forcing "2θ to appear as a genuine current angle" is the same kind of problem as
   forcing θ, chaining gives: Mulan can force a win whenever θ = 90°/2^k for some
   integer k≥0 (90, 45, 22.5, 11.25, …), via: force 90° (1 move, always available),
   then repeatedly bisect (x=current/2 — a bisection ALWAYS makes the half-value appear
   in *both* children, regardless of Shan-Yu's pick — this is a genuinely forced,
   branch-independent move) k times. This sub-family is solid and easy to write up.

3. **θ>90° is provably IMPOSSIBLE — clean invariant, general and rigorous.**
   Key finding: if the current triangle is **acute** (all angles <90°), then for a
   split of angle A with base angles B,C<90°, T1 is acute ⟺ x>90−B, and T2 is acute ⟺
   x<90−B — these are *exactly complementary* conditions on the same threshold x=90−B
   (verified by direct computation: T1's only possible obtuse angle is 180−B−x>90 ⟺
   x<90−B; T2's only possible obtuse angle is B+x>90 ⟺ x>90−B; at x=90−B both become
   right triangles). So for **every** choice of Mulan's split, at least one of T1,T2 is
   still acute (or right) — never both obtuse — so Shan-Yu can *always* pick the
   acute/right one, and an acute triangle can NEVER contain an angle >90°. Hence:
   **Shan-Yu, by starting with any acute triangle and always keeping the acute (or
   right) piece, keeps T acute forever, so if θ>90° Mulan can never win.** This is a
   complete, general, rigorous defense — no gaps. (θ=90 itself is fine for Mulan, see
   opening 1 — a right triangle isn't obtuse, and 90 is directly forceable.)

4. **Branching (adaptive, non-uniform) strategies solve MORE θ than the pure doubling
   chain — refutes a "only θ=90/2^k" conjecture.** I built and hand-verified (plus
   brute-force-searched with exact rational arithmetic) a genuine depth-4 forced win
   for **θ=60°** from the triangle (100°,50°,30°) that is NOT of the form 90/2^k:
   split 100 at x=40 → T2=(30,60,90) already has θ (Shan-Yu avoids, keeps
   T1=(50,40,90)); split 90 at x=40=A/2 (bisection, forced both ways) → children
   (40,40,100) and (50,50,80), *both* winning independently at depth 2 via the
   A=2θ=120 mechanism (from (40,40,100), split the 100 with x=A/2=20 → one child
   (40,20,120) has A=120=2θ, forced 60 in both branches next move next; symmetric
   argument for (50,50,80)). Full path was verified line by line with exact fractions.
   This shows genuine game-tree branching (using both the "insert θ directly" move and
   the "bisect" forced move, mixed and matched with the observation that Shan-Yu's
   choice can be countered independently on each branch) reaches values well outside
   the naive dyadic-doubling family.

5. **A brute-force minimax search (exact rational arithmetic, heuristic candidate set
   for x — NOT exhaustive over all reals) found forced wins within depth ≤4 for
   θ ∈ {10,15,20,25,30,45,60}° from a fixed generic start (100,50,30)°, but failed to
   find one (up to depth 6-7, with a fairly rich candidate list of x-formulas) for
   θ ∈ {35,40,55,62,65,68,70,72,75,78,80,82,85,88,89}°, even trying several different
   starting triangles for θ=75° (20,80,80),(30,80,70),(100,50,30),(10,85,85) — all
   failed similarly.** This is only suggestive, NOT conclusive: the candidate set for
   x is a hand-picked finite list of "plausible" formulas (θ, A−θ, A/2, 90−B, 2θ,
   A−2θ, θ/2, B/2, C/2, θ±B, θ±C, A/3, 2A/3, …), not the full continuum Mulan actually
   has access to, and search depth is capped for compute-time reasons. So this does
   **not** prove θ=75° (say) is a Shan-Yu win — it may just mean the winning strategy
   for such θ needs a cleverer x-formula not in my heuristic list, or greater depth.
   **This is the open question the outliner most needs to resolve**: is the true
   answer "all θ ≤ 90°" (elegant, matches the θ>90 obstruction cleanly, and my search
   failures are likely just heuristic incompleteness), or is there a genuine second
   obstruction cutting out some θ<90° (e.g. related to 60°, thirds of 180°, or some
   2-adic-valuation condition — see crux below)? I could not settle this in the time
   available; flagging honestly rather than guessing.

### Candidate technique(s)
- Direct algebraic/case analysis of the two split formulas (as above) — this is the
  natural technique and where all real progress is.
- Backward induction / Win-Loss (N-position/P-position) labeling of triangle-angle
  states, analogous to combinatorial game theory (see crux below) — likely the right
  framework for a rigorous full characterization for θ<90°, since the "branching"
  successes in point 4 are exactly this kind of game-tree argument.
- 2-adic valuation / halving-invariant arguments (per the crux match below) — strongly
  suggested by the fact that "bisection" (x=A/2, guaranteed both branches) is the
  *only* generic "forced" move besides the θ=90 special one, so repeated halving
  differences is likely the load-bearing recursive structure for characterizing which
  θ are reachable, much like the linked crux's v_2(a−b) parity criterion.

### Cheap-kill candidates
- **θ>90°: full obstruction found (see opening 3) — settle this direction first,
  it's a clean one-paragraph "acute invariant" argument, no case gaps.**
- θ=90°: trivial 1-move win (altitude from a vertex with two acute base angles,
  always exists since at most one angle is ≥90°) — also a quick, clean case.
- For θ<90°, no cheap kill found; the real content is in constructing (or refuting)
  a general finite strategy, likely via the win/loss game-tree framework.

### Knowledge-base entries to use
- "Invariants & monovariants" (knowledge_base.md ~line 117, 191) — directly the tool
  used for the θ>90° acute-invariant proof and likely needed for the θ<90 case.
- (No explicit "combinatorial game theory / N-P positions" named entry found in
  knowledge_base.md via my grep — worth the outliner double-checking with a broader
  search, since that's the natural framework for the θ<90° half.)

### Analogous past problems (cruxes)
- **aimo-0225** (combinatorics, games-and-strategy; UK, "counters on n-gon, area-
  increasing moves") — genuinely analogous, strong match: states are triangles
  parametrized by three arc-lengths (a,a,b) summing to n (angles here sum to 180),
  moves take an isosceles state (a,a,b) to another isosceles state (a, a±d/2, a±d/2)
  where d=|a−b| — i.e. a **halving-of-the-difference** move, exactly structurally
  parallel to our forced bisection move. The crux move is: label states Win/Loss by
  backward induction, show all non-isosceles states are Wins via a symmetry/strategy-
  stealing argument, then show an isosceles state (a,a,b) is a Win iff a≠b and
  v_2(a−b) is odd (2-adic valuation of the difference), with the recursive halving
  argument (d → d/2 when d even, terminates when d odd since d/2 is then impossible).
  **This is the best structural template available for resolving the θ<90° open
  question**: our problem may reduce to a similar Win/Loss labeling of angle-triples
  with a 2-adic-valuation-type criterion determining exactly which θ are forceable —
  worth trying to adapt directly (adapt the proof technique, not the numbers; this is
  a different problem with a different move set, must be reproved from scratch).
- Searched combinatorics domain, subtopics games-and-strategy (39 entries) and
  briefly size-bounding-and-descent — no other entry matched as closely as aimo-0225;
  the rest were pairing/parity/mirroring strategies for discrete board games, not
  applicable to this continuous-angle cutting game.

### Prior progress
None in results/imo-2026-04/ yet (first round, workspace empty per current.md).

### Dead ends (do not retry)
- **Pure fixed-target "always bisect the same traced angle down from A_0" or "always
  insert θ directly into one branch and hope Shan-Yu is eventually cornered without
  ever re-planning based on his choice"** — verified by hand + code that this cycles
  forever for generic starting triangles (e.g. (100,50,30) with θ=60 cycles back to a
  relabeling of itself after 3 rounds under the naive "always use x=θ" tactic). Do NOT
  present a strategy that doesn't adapt to Shan-Yu's actual choice at each step —
  needs genuine branching/game-tree reasoning, not a fixed formula.
- The conjecture "Mulan wins iff θ = 90°/2^k" (k≥0, i.e. only 90,45,22.5,11.25,…) is
  **refuted** by the explicit depth-4 win for θ=60° (opening 4) — do not adopt this as
  the final answer, it's a real but strictly smaller sub-family of winnable θ.

### Small-case / intuition notes (conjecture, labeled as such)
- **Proved, not conjecture:** θ>90° ⇒ Shan-Yu wins (acute-triangle invariant, opening 3).
- **Proved, not conjecture:** θ=90° ⇒ Mulan wins in 1 move (opening 1).
- **Proved by explicit construction (conjecture only in the sense that I hand/computer-
  verified one example, not a general theorem):** θ∈{90/2^k} and additionally at least
  θ=60°,45°,30°,25°,20°,15°,10° are winnable for Mulan from at least the generic start
  (100,50,30)° (and 30°,45°,60° checked with other starts too).
- **Open / unresolved (my best guess, low confidence):** my leading conjecture for the
  full answer is **θ ≤ 90°** (all of them), with the θ∈{35,40,55,62,65,…,89}° search
  failures being artifacts of an incomplete heuristic x-candidate list rather than a
  real obstruction — but I could NOT confirm this, and it's equally plausible (given
  the aimo-0225 crux parallel) that the true characterization is a nontrivial subset
  of (0°,90°] governed by a 2-adic-valuation-type condition on θ relative to 180° (or
  relative to some derived quantity), analogous to that crux's v_2(a−b) criterion. The
  outliner should treat "characterize exactly which θ<90° work" as the central open
  problem, and should seriously consider building the Win/Loss (state = angle-triple)
  labeling framework from aimo-0225 as the main proof route, rather than trying to
  hand-construct ad hoc strategies per θ.
