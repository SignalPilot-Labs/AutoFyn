## imo-2026-04 (Mulan's Triangle Game) — adversary / Shan-Yu-survival lens

### Reformulation used throughout
Label current triangle's angles (A,B,C), A+B+C=180. A move: Mulan picks a vertex to
"split" (equivalently picks the side opposite it to place P on), say A, and a value
x∈(0,A). The two candidate children are
  child1 = {x, B, 180−x−B},   child2 = {A−x, C, x+B}
(verified algebraically and numerically with sympy: the "new" angle of child2 is
exactly x+B, and 180−x−B and x+B are always supplementary — this is just the
straight-line fact ∠APB+∠APC=180°). Shan-Yu picks one child. So each move: one old
angle survives **untouched** (B or C, Shan-Yu's pick), the split vertex A donates one
fragment (x or A−x, Mulan's pick of which fragment goes with which survivor is fixed
by the pairing above, only the numeric value x is Mulan's choice), and a brand-new
"P-angle" appears, always the supplement partner of the other branch's P-angle.

### Proven (constructive) result: Mulan wins θ = 90°/2^k for every integer k ≥ 0
1. **θ=90 is a universal one-move win, from ANY triangle.** Solving for when BOTH
   children are forced to contain θ regardless of Shan-Yu's choice: need x∈{θ,180−B−θ}
   ∩ {A−θ,θ−B}. The only *state-independent* (works for all A,B,C) solution is θ=90
   (via x=90−B), giving both children a 90° angle at P automatically, because the two
   P-angles are always supplementary and θ=90 is the unique self-supplementary value.
   The other family (x=θ=A−θ) needs A=2θ already, i.e. a pre-existing angle 2θ — state
   dependent, not universal.
   Construction: pick any vertex V whose two OTHER angles are both acute (always
   exists: a triangle has at most one angle ≥90°, and dropping the altitude from the
   vertex with the ≥90° angle, or from any vertex in an acute triangle, lands the foot
   strictly inside the opposite side). Cut along that altitude. Both resulting
   triangles get a 90° angle at the foot — verified numerically for 5 random acute
   triangles (script output: both children always contain 90.0 exactly).
2. **Bisection propagates any forced angle downward by a factor of 2, immune to
   Shan-Yu.** If the CURRENT triangle is guaranteed (regardless of earlier Shan-Yu
   choices) to contain an angle φ, split that angle exactly at x=φ/2. Since x=φ−x=φ/2
   identically, BOTH children get the fragment φ/2 — Shan-Yu's choice is irrelevant
   (the two fragments are literally the same number).
3. Chaining 1 + repeated 2: force 90 in one move (universal), then bisect k times to
   force 90/2, 90/4, ..., 90/2^k. This is a **fully deterministic, non-adaptive**
   (k+1)-move strategy that works against every possible Shan-Yu play and every
   possible Shan-Yu starting triangle. So θ ∈ {90, 45, 22.5, 11.25, 5.625, ...} =
   {90/2^k : k=0,1,2,...} are certainly in Mulan's winning set.

### Why single "direct threats" alone can't extend this to other θ (dodge lemma)
For general θ, if Mulan sets x=θ on some vertex A (0<θ<A), only ONE child (the one
pairing fragment θ with a kept old angle) contains θ; the other child generically does
not. Shan-Yu simply takes the untouched-vertex child and survives that move. The
algebra above shows the ONLY way to make **both** children simultaneously unavoidable
is θ=90 (universal) or "the vertex being split already equals 2θ" (state-dependent,
itself requires 2θ to already be present — pushing the problem to the sub-game of
forcing 2θ, which bottoms out only if some 2^kθ=90, i.e. θ=90/2^k — the *same* dyadic
family found constructively above). So the "shared-value" mechanism, taken alone,
provably yields nothing beyond {90/2^k}. Anything more would need a genuinely
**adaptive** multi-move strategy where Mulan's follow-up differs depending on which
child Shan-Yu chose — I could not find such a construction for a non-dyadic θ (tried
θ=60, θ=135 as test cases; no analog of the altitude trick exists for them, since the
universal-trigger equation algebraically has θ=90 as its unique solution).

### Conjectured win/lose boundary
**Mulan's winning set is exactly {90°/2^k : k = 0,1,2,3,...}; Shan-Yu can survive
forever for every other θ ∈ (0°,180°).** This is a conjecture (the ⊇ direction above
is fully proved/constructive; the ⊆ direction — that Shan-Yu truly survives all other
θ — is NOT yet established and is the key remaining gap).

### Distinct openings for the outliner
1. **Constructive/positive route (solid):** state and prove the (k+1)-move
   deterministic strategy above for θ=90/2^k. This half is essentially done and just
   needs careful write-up (altitude existence lemma + bisection lemma + induction).
2. **Negative/survival route (open, the hard half):** find an explicit Shan-Yu
   invariant/strategy proving no θ outside {90/2^k} is forceable. Candidates:
   - A **potential function / dyadic-valuation** argument: since the only "inescapable"
     single-move device is bisection-of-an-already-guaranteed-angle, try to show by
     strong induction that Shan-Yu can maintain "every current angle differs from θ,
     and no current angle is of the form θ·2^j or arises from a bisection chain
     rooted at 90 targeting θ," i.e. mimic the aimo-0236 style argument (see below):
     maintain a threshold/valuation invariant that holds strictly before AND after
     each of Shan-Yu's turns, self-restoring by induction.
   - A **genericity/transcendence** argument: Shan-Yu picks a starting triangle whose
     angles are algebraically independent of θ and of 90 in a strong sense, and argues
     any single Mulan threat (x=θ) is dodgeable, and shows by induction that the
     "dodge" always keeps the surviving triangle in a state from which future forced
     collisions require another `A=2θ`-type coincidence that genericity prevents. This
     is delicate because Mulan chooses x adversarially each move (she is not
     constrained to algebraic relations), so the invariant must be about what
     Shan-Yu can always avoid, not about what Mulan can't reach.
   - Consider **θ near 90 but not dyadic** (e.g. θ=89.9°) as a stress test: does the
     altitude trick "almost" work, hinting at a continuity argument that could rule
     out near-misses? (Likely no — the construction is exact, not approximate; a
     small perturbation just fails outright since we need an exact angle match.)
3. **A third opening**: question whether Shan-Yu is even required to avoid θ forever
   from a FIXED starting triangle, or whether the characterization could instead be in
   terms of "θ commensurable with 90 as a dyadic fraction" vs not — i.e. reframe the
   answer as θ/90 ∈ {1, 1/2, 1/4, 1/8, ...} and look for the crux corpus's dyadic /
   2-adic-valuation technique (see below) as the exact template for the missing half.

### Cheap-kill candidates
- Check whether θ > 90° can ever be forced at all: the constructive family only
  reaches 90 and below (90/2^k ≤ 90). If Shan-Yu can show angles >90° are NEVER
  forceable except degenerately, that's a clean partial result (a triangle has at
  most one angle >90°, and once such an angle is "spent" by a cut its descendants
  can't recreate a large angle easily) — worth checking as a smaller, more tractable
  sub-claim: **"no θ>90° is in Mulan's winning set."**
- Parity/degree-counting: since only bisection (equal split) is choice-immune, and
  bisection literally halves, any inescapable chain of length n produces values of
  the form (base angle)/2^n; the "base angle" that is itself universally producible
  in one step is uniquely 90 (proved above) — this IS basically the cheap kill that
  bounds the winning set to the dyadic-90 family, modulo ruling out adaptive
  multi-move alternatives.

### Knowledge-base entries to use
- **Invariants & monovariants** (`knowledge_base.md` combinatorics section) — the
  generic tool needed for Shan-Yu's survival half.
- **Synthetic toolkit: angle chasing** (geometry section) — needed to rigorously
  justify the altitude-foot-lands-inside-segment claim and the supplementary-angle
  fact used throughout.
- No specific KB entry currently covers 2-adic/dyadic-valuation game arguments
  directly; the closest is the crux below.

### Analogous past problems (cruxes)
- **aimo-0236** (combinatorics, games-and-strategy): "To show a player can prolong a
  token-game forever, exploit that the prolonging player moves first to carry a
  valuation witness one step ahead of the opponent: maintain a two-phase invariant
  (stronger bound before the opponent moves, weaker bound after) that is
  self-restoring." This is a strong structural analog for the missing "Shan-Yu
  survives outside the dyadic family" half: it is literally a 2-adic-valuation
  survive/terminate dichotomy game, same flavor as our 90/2^k family. Worth adapting
  the technique (not the content) to build Shan-Yu's invariant.
- **aimo-0262** (Cinderella's buckets, games-and-strategy): defender maintains a
  self-reproducing family of invariant configurations, restorable after every
  adversary move — general template for "defender survives forever" proofs, useful
  methodologically even though the setting (continuous water) differs.
- No crux in the corpus involves cevian-cutting or triangle-angle games specifically;
  geometry has no cruxes extracted at all (per `crux_moves_documentation.md`). None of
  the corpus entries are a close configurational match — the above two are technique
  analogs only, not configurational matches.

### Prior progress
None recorded yet in `results/imo-2026-04/` (empty `approaches/`, `current.md` says
unsolved / nothing established). This report supplies the first concrete progress:
the constructive half of the answer.

### Dead ends (do not retry)
- **Single "direct threat" moves (x=θ) as a way to force generic θ**: provably
  dodgeable by Shan-Yu every time (only one child is threatened); do not present this
  as a winning strategy for non-dyadic θ without an adaptive multi-move argument that
  actually closes both branches.
- **Looking for a second "universal" one-move trigger besides θ=90**: algebraically
  ruled out — the system solving for state-independent both-children-forced splits has
  θ=90 as its unique solution (checked by hand and cross-checked structurally via the
  supplementary-angle identity, which only self-matches at 90).

### Small-case / intuition notes (conjectural)
- Numerically verified (sympy/random trials) that the altitude construction always
  produces a 90° angle in both children for acute-adjacent vertices — strong
  confirmation, not just for special triangles.
- Conjecture: winning set = {90/2^k}. This would make the final answer a countable,
  measure-zero, "highly dyadic" set — plausible for an IMO-style clean
  characterization, and it cleanly explains why θ=90° is forceable in exactly 1 move
  while everything else needs either more moves or is outright impossible.
- Untested but worth probing next round: whether Mulan has extra power via choosing
  DIFFERENT vertices to split on alternate moves (not just re-splitting the same
  lineage) — my analysis mostly chased a single "lineage" of cuts; a genuinely
  adaptive strategy interleaving cuts on different vertices, reacting to Shan-Yu's
  choice each time, is the main unexplored territory and could either produce more
  winning θ or (more likely, if Shan-Yu's invariant is robust) simply fail the same
  way single threats fail.
