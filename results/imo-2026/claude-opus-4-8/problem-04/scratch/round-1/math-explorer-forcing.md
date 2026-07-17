## imo-2026-04 (Mulan's Triangle Game) — Constructive-forcing lens

NOTE: `problems.jsonl` lists `difficulty_level: "medium"`, `difficulty_rating: 7` for this
id (not "hard"), but the dispatch explicitly assigned it, so I explored it as instructed.
Flag this discrepancy to the orchestrator — per CLAUDE.md the run should target one of the
39 `hard` problems; confirm this assignment is intentional.

### Setup / normal form (verified algebraically and numerically)
Label the current triangle's angles as a triple. When Mulan cuts from the vertex with
angle **X** (opposite side has vertices with angles **Y**, **Z**; X+Y+Z=180°), she picks a
point P via a parameter t = the sub-angle of X on the "Y side", t ∈ (0,X) continuously
(IVT: as P sweeps the whole open side, t sweeps all of (0,X)). The two children are:

- Branch1 (contains Y): angles **{t, Y, X+Z−t}**
- Branch2 (contains Z): angles **{X−t, Z, Y+t}**

Shan-Yu picks which branch survives. Verified numerically in Python (exact arithmetic on
sample triples) that this formula is self-consistent (t=0 and t=X limits reproduce the
original triangle, sum is always 180).

### Forcing gadgets found (each is a genuinely different opening)

**1. θ = 90° is a ONE-STEP forced win, always.** Pick the vertex V such that the other two
angles are both acute (at most one angle in any triangle is ≥90°, so at least two vertices
qualify). Set t = (X+Z−Y)/2, i.e. cut so that the *other two* angles at the new point P are
supplementary halves 90°/90° — concretely both branches get value **exactly 90°** at the
bumped position (verified: X=80,Y=60,Z=40 gives 90-fork at t=30, both branches show a 90°
entry). This is because the two P-angles across the two branches are always supplementary
(sum 180°); forcing them equal forces both to 90°. Independent of Shan-Yu — this is a true
fork, not a threat he can dodge. **θ=90° is solved in 1 move, unconditionally.**

**2. Bisection-fork lemma (the strongest general tool).** Cutting from vertex X at
t = X/2 (the literal angle bisector) makes **both** branches share the value X/2 at the
shared vertex V (verified numerically: X=80,Y=60,Z=40 ⇒ both branches contain 40.0). So
Mulan can, in ONE move, deterministically force "angle X/2 appears in the surviving
triangle" **regardless of Shan-Yu's choice** — because both children literally share vertex
V, and t = X−t forces the same numeric value there. Iterating on the *same* vertex V (which
survives every bisection, since V is common to both branches by construction) she can force
V's angle to hit **A₀/2, A₀/2², …, A₀/2^k** for any k, fully deterministically, no matter
how Shan-Yu plays. If Shan-Yu's starting angle A₀ (at any of his three chosen vertices)
happens to equal θ·2^k for some nonnegative integer k, Mulan wins in k moves via pure
bisection. (This is a genuinely different, purely constructive route from the altitude
trick — no reliance on 90° at all.)

**3. Direct-bait / vertex-transfer move (a third, distinct construction).** More generally,
setting t = θ exactly (when the source angle X > θ) makes Branch1 contain θ directly — an
instant win if Shan-Yu is forced to accept it, i.e. only a real weapon when combined with a
genuine fork (Branch2 also hits θ or ≥). Used alone (no fork), Shan-Yu simply takes Branch2,
producing the deterministic *transfer*: (X,Y,Z) → (X−θ, Y unchanged, Z+θ) — Mulan even
chooses which of Y,Z is "protected" vs "bumped" (cut can be measured from either side).
Treating (A,B,C) as 3 tokens summing to 180°, this move is "steal θ from a token >θ, hand
it to a chosen other token, leave the third alone."

### Cheap-kill / obstruction found (important — rules out the naive approach)

**Mod-θ invariant kills the "always-bait" strategy.** If Mulan always uses gadget 3 (pure
θ-bait every round, never anything else), every token's value only ever changes by ±θ, so
each of the *original* three angles A, B, C keeps a *fixed residue mod θ* forever (only its
integer-multiple-of-θ part gets shuffled by transfers). She can hit θ exactly this way ONLY
if the starting triangle secretly has some angle that is an exact multiple of θ (i.e.
A, B, or C ∈ θ·ℤ₊). Shan-Yu trivially avoids this at t=0 (pick all three angles generic,
e.g. irrational relative to θ). **So pure baiting is not sufficient in general — Mulan must
mix in non-bait moves (bisection, 90°-fork, or moves with t ≠ θ that give Shan-Yu genuine
choice but from which she has a follow-up win in both branches).** This is the real
difficulty of the problem: any approach that relies solely on "always threaten θ directly"
will get stuck and should be flagged as a dead end if a builder proposes it.

### What growth analysis suggests (conjecture, weakly tested numerically)

Ran a shallow (depth-1, and a partial depth-2 before time cost got prohibitive) brute-force
minimax over a coarse t-grid for θ=170°, starting from (60,60,60) and (100,50,30): **no
forced win found within 1 move**, consistent with the fact that in ONE cut the maximum
angle any branch's "bumped" vertex can reach is bounded by (source angle) + (target angle)
≤ 180° − (third original angle), so reaching very large θ (close to 180°) plausibly needs
many rounds of adaptive, Shan-Yu-dependent branching (not a single deterministic gadget).
I could not, in the time budget, run deep enough search to determine whether large θ (e.g.
θ>90°) is achievable at all or is a genuine obstruction — **this is the open question the
outliner most needs to resolve**: is the answer "all θ ∈ (0°,180°)" (via a smarter adaptive
combination of gadgets 2+3, not yet found) or is there a real barrier (e.g. Shan-Yu has a
stalling invariant preventing angles beyond some bound, giving a restricted characterization
such as θ ≤ 90° or a residue/dyadic-type characterization)? No stalling invariant was
identified for Shan-Yu, but none was ruled out either — this needs directed search, not
brute-force minimax (too slow past depth 2).

### Distinct openings for the outliner (rival approaches)

- **(a) "Bisection-chase":** show for every θ Mulan can, via repeated bisections of a
  cleverly *chosen* (not necessarily original) vertex, converge the guaranteed-shared value
  to exactly θ — needs a way to first steer some vertex's angle to a value of the form
  θ·2^k despite Shan-Yu, i.e. combine gadget 2 with gadget 3's transfer to first *create* a
  multiple-of-θ token, then halve it down. Likely the strongest full-answer route; not yet
  completed here.
- **(b) "90°-then-recurse":** use the θ=90° 1-move win as a base case, and for θ≠90° try to
  reduce to a sub-triangle problem via one dividing cut that isolates θ inside a smaller,
  more constrained configuration (angle-sum arguments on the 2 remaining free angles).
- **(c) "Adversary-invariant / impossibility":** actively hunt for a Shan-Yu stalling
  invariant (e.g. a bound M(θ) such that Shan-Yu can always keep max angle < M, or keep the
  configuration in some closed set avoiding θ) to test whether the answer is ALL θ or a
  restricted set — this is the fastest way to falsify openings (a)/(b) if a genuine barrier
  exists, and should be tried before over-investing in a "works for all θ" full construction.
- **(d) "Transfer-game abstraction":** formalize the (A,B,C)-summing-to-180 token game found
  above (steal θ, or steal arbitrary t, from one token to another) as an abstract
  combinatorial game and ask exactly which θ let Mulan force a token to hit θ or 2θ — this
  might already be a known/solvable sub-game once fully abstracted, separate from the
  geometry (a genuinely different top-level target: solve the abstract token game first).

### Candidate technique(s)
Angle chasing + cevian sub-angle bookkeeping (knowledge_base.md "Synthetic toolkit" —
angle chasing, trig cevians) as the geometric engine; combinatorial game theory / forcing
strategies (adversary argument, strategy stealing) for the game-theoretic layer.

### Knowledge-base entries to use
- knowledge_base.md line ~129-132: "Synthetic toolkit: angle chasing... trig cevians
  (Ceva/Menelaus)..." — relevant for justifying the branch-angle formulas rigorously.
- No dedicated games/strategy-forcing entry found in knowledge_base.md; the game-theoretic
  reasoning here is being built from scratch (no named KB theorem for "adversary game on a
  cevian-splitting process").

### Analogous past problems (cruxes)
Searched combinatorics `games-and-strategy` and `processes-and-algorithms` subtopics (87
cruxes, no geometry cruxes exist in the corpus per crux_moves_documentation.md). Closest by
mechanism, not by geometry:
- `aimo-0445` (USAMO, hexagon-counter game) — crux "create a double threat / fork so the
  opponent's single response cannot block both winning lines" — directly analogous in
  *structure* to gadgets 1 and 2 above (force a value into both surviving branches so
  Shan-Yu's one choice can't escape). Worth citing as the general "fork" pattern, but the
  geometric content must still be built from scratch.
- `aimo-0236` (token/valuation game) — crux "nurse one token so a driving invariant stays
  ahead of the opponent" — thematically close to the "always keep vertex V alive across
  bisections" persistence trick in gadget 2, but the underlying mechanics (p-adic
  valuation) don't transfer.
- Nothing else in the corpus resembles the cevian/angle-splitting structure closely; no
  false-positive matches to warn against.

### Prior progress
`current.md` and `sample_approaches` are both empty — this is the first exploration of the
problem. No approaches or lemmas exist yet.

### Dead ends (do not retry)
- **Pure "always bait exactly θ" strategy** — provably insufficient (mod-θ invariant
  argument above): Shan-Yu can trivially pick a starting triangle with no angle in θ·ℤ₊,
  and pure baiting then never converges. Any approach file proposing this as the *whole*
  strategy should be flagged for revision, not rebuilt from scratch.

### Small-case / intuition notes (all conjecture / numeric, not proof)
- θ=90°: proven in 1 move (rigorous, not just conjectured) via the 90°-fork gadget.
- θ = A₀/2^k for A₀ one of Shan-Yu's actual starting angles: proven forceable in k moves
  (rigorous) via bisection-fork — but Shan-Yu avoids this by choice of starting triangle, so
  by itself this only covers a measure-zero set of "lucky" (θ, triangle) pairs, not a
  θ-only characterization.
- Numeric shallow search suggests large θ (near 180°) is NOT reachable in very few forced
  moves from generic/balanced starting triangles — weak evidence (not proof) that either
  many more rounds are needed, or that a real obstruction exists for large θ. Insufficient
  compute budget to resolve; flag as the single most important open question.
