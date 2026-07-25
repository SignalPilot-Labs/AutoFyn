## imo-2026-04 (lens: Shan-Yu's defensive side)

### Setup / key structural fact (derived, not from KB)
Label triangle angles (A,B,C), A+B+C=180, A at the vertex opposite the side where
Mulan places P. As P ranges over the open side (excluding endpoints), the angle
φ = ∠APB ranges continuously over the OPEN interval (C, 180−B), and the two
children are exactly:
- child1 = (B, A+C−φ, φ)   [contains vertex B]
- child2 = (C, φ−C, 180−φ)  [contains vertex C]
(φ and 180−φ are supplementary — the two angles created at P.)
Mulan freely picks (i) which of the 3 angles is "A" (i.e. which side to cut) and
(ii) φ continuously in the resulting range. Shan-Yu then discards one child.

This decomposition is the real engine of the problem; I did not find it named in
knowledge_base.md or in the crux corpus — it has to be derived from scratch (see
"Analogous past problems" below for why nothing pre-existing matches).

### Distinct openings (routes a defensive-side approach could take)
1. **θ=90° instant win (clean, fully proved).** Set φ=90 (drop the altitude from a
   vertex whose two base angles are both acute — always exists, since a triangle
   has at most one non-acute angle). Then child1 and child2 both have angle
   exactly 90 (φ and 180−φ are equal only when both are 90). Shan-Yu has no safe
   choice: **Mulan wins in one move whenever θ=90.** Solid, not just conjectural.

2. **θ>90°: Shan-Yu defends forever (clean, fully proved + numerically verified).**
   Invariant: "all three angles < θ". Shan-Yu picks the equilateral triangle
   (60°,60°,60°) initially (θ>90>60 so it satisfies the invariant). Claim: from any
   triangle with all angles <θ (θ>90 fixed), for **every** legal Mulan move (any
   vertex choice A, any φ in its valid range), **at least one child still has all
   angles <θ**. Proof sketch: child1 safe ⟺ φ ∈ [A+C−θ, θ); child2 safe ⟺
   φ ∈ (180−θ, θ+C]. Since θ>90 ⟹ 180−θ<θ, these two safe sub-intervals *overlap*
   (their union is exactly (A+C−θ, θ+C) ⊇ (C, 180−B) whenever A<θ, which holds by
   the invariant) — so the union covers the *entire* legal range of φ. Hence
   Shan-Yu always has a safe reply, and the invariant is self-closed: **for all
   θ>90°, Shan-Yu can guarantee an angle-θ never appears, forever.** I verified
   this numerically (500k random legal (A,B,C,φ) all respecting the invariant,
   θ=100: zero counterexamples found — see Small-case notes).

3. **θ<90°: the same invariant provably FAILS** (numerically: ~35% of random legal
   cuts at θ=80 break "all<θ" for both children simultaneously) — because
   180−θ>θ now, so the two safe sub-intervals [A+C−θ,θ) and (180−θ,θ+C] are
   *disjoint*, leaving a genuine gap (θ, 180−θ) of φ-values where **neither**
   child can maintain all-angles-<θ. Mulan can always pick φ in this gap
   (nonempty exactly because θ<90) forcing the surviving triangle (whichever
   child Shan-Yu keeps) to contain an angle in (θ,180−θ) — i.e. an angle that's
   *not equal* to θ but *strictly bigger*. This is a genuine breakout, and it's a
   strong signal Mulan wins for θ<90, but is NOT by itself a finite construction.

4. **The "2θ ⟹ forced win in one more move" lemma (clean, exact).** If the SPLIT
   vertex angle A equals exactly 2θ, setting φ=θ+C makes BOTH children contain
   angle θ exactly (child1=(B,θ,θ+C), child2=(C,θ,180−θ−C)) — Shan-Yu is
   trapped regardless of his choice. This generalizes the θ=90 case (which is
   A=2θ with θ=90 ⟹ A=180, degenerate — actually the θ=90 win is really its own
   simpler case via φ=90 directly, not this lemma).

5. **The "insert-θ transfer" move (clean, exact, but limited alone).** Whenever
   some current angle A>θ, Mulan can set φ=A+C−θ (equivalently 180−B−θ), which
   makes child1 = (B, θ, A+C−θ) — an *immediate loss* for Shan-Yu — forcing him
   into child2 = (C, A−θ, B+θ). This is a **fully forced, deterministic** move: Shan-Yu
   has no real choice (the alternative always contains θ). Chaining this move
   shifts value by exactly θ between two angle-registers each time. **Key
   limitation found:** since every use of this move changes an angle by exactly
   ±θ, each angle's value stays in a fixed residue class mod θ forever under pure
   chaining — so pure chaining alone can only hit θ exactly if some *initial*
   angle happens to be an exact integer multiple of θ, which Shan-Yu can trivially
   avoid by choosing a generic initial triangle. **This means the naive "just
   chain the forced transfer" strategy does NOT by itself finish the job for
   generic θ<90 — Mulan must also use "free"/generic φ injections (which give
   Shan-Yu a genuine, non-forced choice) to change the achievable residues,
   and the open question is whether she can do this adaptively to always land
   exactly on θ in finitely many steps.** This is the crux gap for the θ<90 case.

### Candidate technique(s)
- Direct construction + case analysis on φ-ranges (as above) — this IS the
  technique, there's no more exotic tool needed. Essentially an interval-covering
  / "does the union of two moving safe-subintervals cover the legal range"
  argument, done per-move, chained across rounds.
- For the θ<90 direction: likely needs an explicit finite algorithm (a bounded
  number of forced moves + at most one or two genuinely free "aiming" moves) —
  NOT an existence/compactness argument, since CLAUDE.md rigor rules require an
  explicit finite bound.

### Cheap-kill candidates
- θ=90°: killed in one line (altitude cut), no casework needed. Cheap win, should
  be stated explicitly in the final characterization as the "boundary/easiest"
  case.
- θ>90°: killed by the single invariant "all angles <θ", equilateral start. Cheap,
  fully rigorous, no further casework needed — this whole half of the
  characterization (θ>90° ⟹ Shan-Yu wins) is essentially done and can be lifted
  almost verbatim into the outline.
- Parity/measure-zero point: the target is an EXACT angle, so any argument
  relying on "eventually gets arbitrarily close" is insufficient — must produce
  an exact hit or an exact forced-double-child trap (as in the 2θ lemma).

### Knowledge-base entries to use
- I did not find an entry in `knowledge_base.md` specific to this kind of
  "triangle-cutting game with adversarial vertex angle" — the combinatorics
  section (lines ~106+) and combinatorial-geometry section (~146+) cover
  synthetic angle-chasing / incidence tools (Ptolemy, power of a point, radical
  axis) which are NOT relevant here (no circles). The relevant "tool" is purely
  the elementary vertex-angle-splitting algebra derived above; recommend the
  outliner treat this as the load-bearing lemma to state and prove cleanly
  (it is short: ~10 lines of angle-sum bookkeeping) rather than search the KB
  further for it.

### Analogous past problems (cruxes)
Searched `combinatorics` domain, subtopic `games-and-strategy` (39 cruxes) in the
crux corpus for triangle/angle/cut games. None are genuinely analogous:
- `aimo-0225` (n-gon counter-sliding game, isosceles-triangle symmetry + 2-adic
  valuation recursion) — superficially "triangle" but it's about counters on a
  polygon's vertices, not angle-cutting; the "strategy-stealing via symmetry"
  idea and the "recurse on a halving invariant" idea are both worth keeping in
  mind as *technique* analogies (the θ<90 gap above smells like it might need an
  analogous "recurse on how many θ-multiples away" argument), but the setups are
  not close enough to import a concrete move.
- `aimo-0663` (no-two-consecutive-integers game, pigeonhole-on-components
  argument for "responder never gets stuck") — the general shape ("show the
  responder/defender always has a component/interval left to reply into") is
  structurally similar in spirit to the θ>90 defense I proved above (both are
  "show a covering/pigeonhole argument guarantees a safe reply forever"), but
  again nothing to import concretely; my θ>90 proof is self-contained.
- No geometry cruxes exist in the corpus (per crux_moves_documentation.md), so no
  candidate from the geometry side.
- **Verdict: nothing in the corpus is a genuine analog; the outliner should not
  expect to import a crux move here — this needs to be solved from the raw
  angle algebra.**

### Prior progress
None — this is round 1, no approaches exist yet in `results/imo-2026-04/`.

### Dead ends (do not retry)
- **Pure forced-transfer chaining alone (move type 5 above) as a complete
  strategy for θ<90**: proven insufficient by the residue-mod-θ argument — an
  initial triangle whose three angles all avoid every integer multiple of θ
  (trivially constructible, only finitely many bad values to avoid) defeats it.
  Do not present "just chain the insert-θ move" as a complete proof for θ<90; it
  needs a genuine-choice/adaptive-injection step layered on top, and closing that
  gap is the real remaining difficulty of the whole problem.

### Small-case / intuition notes (numerical, labeled as evidence not proof)
- θ=100°: 500,000 random legal (A,B,C,φ) trials respecting "parent all-angles<θ"
  invariant → **zero** violations of "some child also all-angles<θ" — strong
  evidence (and I also gave an exact proof above) that θ>90° is fully defensible
  by Shan-Yu.
- θ=80°: same experiment (parent legal & all-angles<θ) → **35% of trials** are
  violations (neither child maintains the invariant) — strong evidence the
  θ>90° defense structurally collapses for θ<90°, consistent with Mulan having
  real leverage there, though (per the dead-end above) this alone doesn't yet
  give a complete finite winning strategy.
- **Conjectured final characterization: Mulan wins iff θ ≤ 90°** (i.e. the
  answer is the closed interval/half-open set (0°,90°]), with θ=90° cheap/clean,
  θ>90° cheap/clean (Shan-Yu wins, proved), and **0°<θ<90° being the hard
  direction still requiring a genuine finite explicit strategy** (the residue
  obstruction shows it can't be the naive chain — likely needs an adaptive
  two-phase argument: one "aiming" free move chosen based on Shan-Yu's earlier
  reveals, then forced chaining to the exact target). This last direction is
  where the outliner/builder effort should concentrate; I'd flag θ<90° as the
  hardest part of the problem, NOT θ>90° (which is already essentially solved).
