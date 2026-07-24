## imo-2026-04 (Mulan's Triangle Game) — forcing/reachability lens

### Setup and core mechanics (derived, verified numerically)
Label the current triangle's angles as apex `A` (the vertex Mulan cuts *from*, opposite the
side she picks a point `P` on) and base angles `β`, `γ`. Writing `x = ∠(apex,near-β vertex)`
for the cut, `x ∈ (0,A)`, the two children are:

- Child 1 (contains the near-β vertex): angles `{β, x, 180−β−x}`
- Child 2 (contains the near-γ vertex): angles `{γ, A−x, β+x}`

Mulan picks the side (hence which vertex plays "apex", 3 choices) and `x` (any real in
`(0,A)`) each move; Shan-Yu picks which child survives. This is the whole game engine —
verified the arithmetic (angle sums, supplementary pair at P) numerically.

### Opening 1 — the "forced attack" move (the real engine of the game)
If Mulan sets `x = θ` (valid iff apex `A > θ`), Child 1 contains angle θ exactly — an
immediate win if kept, so Shan-Yu is **forced** to discard it, and must keep Child 2
`= {γ, A−θ, β+θ}`. Symmetrically, if some base angle `β < θ`, setting `x = θ−β` forces
Child 2 to contain θ, so Shan-Yu is forced into Child 1 `= {β, θ−β, 180−θ}`.
**This is the only kind of move that removes Shan-Yu's freedom** — any other `x` gives him
a genuine free choice, which he will use adversarially. So Mulan's only leverage is: force
an exact transfer of θ between two angles (apex loses θ, a chosen other angle gains θ, the
third is untouched), any time some angle is `>θ` or `<θ` (i.e. essentially always, since not
all three angles can be `≥θ` when `θ>60`, and one can nearly always find a valid apex/base
split otherwise).

### Opening 2 — the double-fork / win condition
Mulan wins outright the instant she can choose `x` so **both** children contain θ
simultaneously (Shan-Yu then has no safe discard). Solving the 4 possible coincidences of
`{x, 180−β−x} vs {A−x, β+x}` matching θ gives exactly:
- **(a)** apex `A = 2θ` exactly (then `x=θ=A−θ` puts θ in both children) — needs a
  pre-existing angle equal to `2θ`.
- **(d)** `θ = 90°`, **universal**, works for *any* triangle without any special angle:
  taking `x = 90−β` (the foot of the altitude from the apex!) gives both children a right
  angle at P, since supplementary angles at P can only both equal a target τ when τ=90.
  Verified numerically on 2000 random triangles: **zero failures** — Mulan always wins
  θ=90° in exactly one move, for any starting triangle.

There is a **third, less obvious route (found by tracking residues mod θ)**: forcing a
θ-attack move can, as a side effect, deposit an exact multiple `mθ` (not just θ) into the
surviving triangle even when no such multiple existed before, precisely when
`180 ≡ 0 (mod θ)`, i.e. **θ divides 180**. Concretely with `θ = 180/n` (integer n≥2): the
move `x = 180−β−θ` forces Child 1 = θ (discarded) and leaves Child 2 = `{γ, θ−γ, 180−θ}` =
`{γ, θ−γ, (n−1)θ}` — an *exact* multiple `(n−1)θ` appears "for free" via the identity
`180−θ=(n−1)θ`. From there, repeated forced apex-attacks (each legally peels off exactly θ,
apex `mθ → (m−1)θ`, always available while `m≥2` since apex `>θ`) walk the multiplier down
to `m=2`, at which point condition (a) fires and Mulan forks to win.

**Verified numerically for n=3 (θ=60°)**: starting triangle (97°,51°,32°) — move 1 gives
child2=(32,28,120) [120 = 2θ, exact], move 2 forks: both possible children are
`(32,60,88)` and `(28,60,92)` — **both contain 60° exactly**. Confirms the 2-move forced
win for θ=60° from a "generic" (no pre-existing coincidence) starting triangle. This
generalizes: n=2 gives θ=90° (0 extra peel moves — matches the universal 1-move result),
n=3 gives θ=60° (0 peels, 2 moves total), n=4 gives θ=45° (1 peel, 3 moves — also
independently reachable in 2 moves via 90°→45° halving, since 4=2², both routes agree),
n=5 gives θ=36°, etc.

### Opening 3 — necessity: the mod-θ invariant (candidate impossibility proof for the rest)
Every forced attack move changes exactly one angle by `+θ` and another by `−θ`, so **the
residue of every angle mod θ is invariant** under forced moves — an angle can never become
`≡0 (mod θ)` unless it already was, UNLESS Mulan can rig `180 ≡ 0 (mod θ)` (Opening 2's
third route) to inject a coincidence "for free." Checking all 4 combinations of which slot
of each child could hit residue 0 shows: 3 of the 4 require a *pre-existing* angle already
`≡0 (mod θ)` (excluded if Shan-Yu starts generic), and the 4th requires exactly
`180 ≡ 0 (mod θ)`. **So if θ does *not* divide 180**, Shan-Yu can pick a starting triangle
with all three angles `genericaly ≢ 0 (mod θ)` (e.g. irrational/transcendental relative to
θ), and this property is provably preserved forever against every possible Mulan move
(verified with a naive greedy simulation for θ=100°, which is *not* a divisor of 180:
after 500 simulated forced moves the triangle settled at (80,80,20), residues stuck at
20 mod 100, angle θ=100 never appeared). This is strong (though not yet fully rigorous —
the simulation used a greedy Mulan/Shan-Yu, not a true minimax over all Mulan strategies)
evidence that **θ not dividing 180 is unforceable**.

### Conjectured answer
**θ ∈ {180°/n : n = 2, 3, 4, 5, …} = {90°, 60°, 45°, 36°, 30°, 180/7°, 22.5°, 20°, …}**
(a discrete, infinite, decreasing sequence of angles ≤ 90°, all "aliquot" submultiples of
180°). Equivalently: Mulan wins iff `180/θ` is an integer ≥ 2. This is a `characterization`
answer, matching the problem's `answer_type`. NOTE: this is a conjecture built from (i) a
proven sufficiency mechanism for n=2,3,4 (verified numerically, and the general-n
construction sketched but not fully checked for all n, esp. edge cases where the needed
base angle `β<θ` or `γ<θ` isn't available under any of the 3 vertex/2 direction choices)
and (ii) a plausible-but-not-fully-rigorous necessity argument (the mod-θ invariant, needs
a clean formal statement that covers ALL of Mulan's possible x-choices, not just the 4
"forced-attack" family, since in principle she could choose a wild x hoping Shan-Yu's
"safe" choice is still bad two moves later — this needs a genuine backward-induction /
invariant proof, not just single-step case check).

### Cheap-kill candidates
- Immediately rule out θ=180 (out of range) and confirm θ ≤ 90° is necessary for
  membership in the conjectured family (180/n ≤ 90 for all n≥2) — gives a fast sanity
  filter: if θ>90°, Mulan should NOT be able to win (consistent with θ=100°,120° both
  failing in the invariant/simulation).
- The "apex must exceed θ" / "some base angle below θ" existence check is a cheap
  necessary condition for any forced move to exist at all — worth stating as a lemma
  ("some forced move is always available unless all three angles equal θ exactly", trivial
  edge case since that can't happen for a valid triangle unless equilateral with θ=60,
  which is a Mulan-favorable instant win anyway).

### Knowledge-base entries to use
- Read `/home/agentuser/repo/knowledge_base.md` — searched for "games", "adversary",
  "invariant/monovariant" entries; nothing named specifically matches this geometric cutting
  game (no direct hit found via grep on games/adversary/strategy-stealing keywords). The
  outliner should re-grep with more specific angle/invariant terms, but likely this problem
  needs a bespoke invariant (mod-θ residue argument above) rather than an off-the-shelf KB
  theorem. Worth citing generic **pigeonhole** / **invariant-monovariant** framing from KB
  if present, and the **intermediate value / continuity** idea for "any x in a range is
  achievable" (standard IVT usage, should be named explicitly if KB has an IVT entry).

### Analogous past problems (cruxes)
Searched crux corpus (`combinatorics` domain, `games-and-strategy` subtopic, 39 entries) —
none are geometric cutting games; closest thematically is the **"double threat / fork"**
idea (`aimo-0445`: *"Create a double threat where the opponent's single allowed response
cannot block both winning lines simultaneously"*) — this crux move is a genuine structural
analogue of Opening 2 above (the simultaneous-θ-in-both-children fork), worth citing as the
named technique even though the geometric mechanics are unrelated. Also scanned
`past_problems_database.json` for triangle+cut+angle statements (221 hits) — none are a
recognizable analogue of this specific "cevian-splitting adversarial game" (most are static
Olympiad geometry, not games). **Geometry cruxes are not in the corpus at all** per
`crux_moves_documentation.md`, so this problem is largely un-precedented in the retrieval
bank; treat the corpus as offering only the abstract "fork" motif, not a geometric template.

### Prior progress
None — `results/imo-2026-04/approaches/` and `lemmas/` are both empty; this is the first
round of exploration.

### Dead ends (do not retry)
- Trying to win via a **limiting/continuity argument alone** (Mulan "converges" the angle
  toward θ) does NOT suffice — the win condition requires an *exact* equality in *finitely
  many* steps, and Shan-Yu's discard can always keep re-selecting the "wrong" half forever
  under a pure convergence strategy (no forcing). This must be flagged to the outliner: any
  approach resting on "Mulan can get arbitrarily close, hence eventually exact" is invalid
  without an actual finite forcing argument (the residue/multiple mechanism above is the
  real content).
- Assuming Shan-Yu's only lever is the *initial* triangle choice and that all subsequent
  play is forced — false in general (Opening 1 shows Shan-Yu has genuine free choices
  whenever Mulan's x isn't of the "θ-attack" form); the characterization must account for
  Shan-Yu playing adversarially at every step, not just round 0.

### Small-case / intuition notes (all conjectural, numerically checked)
- θ=90°: forceable in 1 move, universally (proven-strength argument: the altitude
  construction is a clean closed-form proof, essentially airtight — this could likely be
  turned into a fully rigorous lemma immediately).
- θ=60°: forceable in 2 moves (numerically verified concrete instance above); general proof
  needs the case-4 mechanism plus the "n=3, 0 peels" specialization, should generalize
  cleanly since `180−θ=2θ` exactly when θ=60.
- θ=45°, 22.5°, 36°: forceable via the doubling-from-90 chain and/or the n=4,5 direct
  mechanism (both partially checked, consistent).
- θ=100°, 120° (non-divisors of 180): simulation suggests Shan-Yu escapes indefinitely
  (conjectural, invariant argument sketched but not fully formalized against arbitrary
  Mulan play).
- Open gap for the outliner: (1) make the sufficiency construction fully general for all
  n≥2 (handle the vertex-labeling casework so a valid forced move always exists at each
  peeling step), and (2) upgrade the necessity argument from "single-step residue
  preservation" to a genuine induction/invariant proof valid against *all* possible Mulan
  strategies (not just the "forced-attack" family) — this is the crux gap likely to
  dominate the proof's difficulty.
