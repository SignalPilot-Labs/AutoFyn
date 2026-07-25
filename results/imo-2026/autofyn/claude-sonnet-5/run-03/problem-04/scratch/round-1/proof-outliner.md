## imo-2026-04 (Mulan's Triangle Game)

**Conjectured full answer (target for every approach below):** Mulan has a
winning strategy iff θ = 180°/n for some integer n ≥ 2. Strong numeric
support from all three round-1 explorers (exact-rational backward-induction
attractor, stable across resolutions, matches on 15+ divisor values and 30+
non-divisor values with no exceptions).

**Shared, already-rigorously-proven facts** (re-derivable by any builder,
safe to cite across approaches — not attributed to one slug):
- Cut formulas: cutting vertex A (angle A) toward the opposite side with
  t=∠(new vertex split) ∈ (0,A) gives child1={B,t,180−B−t},
  child2={C,A−t,B+t}; the two new angles at the cut point are supplementary.
- **θ=90° lemma**: any triangle has ≤1 angle ≥90°, so a vertex with two
  acute "other" angles always exists; the altitude from it gives both
  children a 90° angle. Mulan wins in 1 move, from ANY starting triangle,
  whenever θ=90°.
- **Bisection lemma**: if a vertex angle X=2θ is present, bisecting it
  (t=θ=X−t) puts θ into BOTH children unconditionally.
- **θ>90° defense**: Shan-Yu starts equilateral and maintains "all angles
  <θ" forever — valid because the two supplementary new angles can't both
  be ≥θ when θ>90 (2θ>180 impossible), so Shan-Yu always has a safe child to
  keep. Verified algebraically + 200k-trial simulation (zero breaks).
- **NEW this round — Shave lemma** (derived + numerically checked, see
  `shave-and-halve-forcing.md`): whenever some current angle X>θ, Mulan can
  cut that vertex with t=θ exactly; one child then contains θ (instant loss
  if kept, so Shan-Yu is FORCED to discard it), and the survivor is
  *exactly and deterministically* {Z, X−θ, Y+θ} for Mulan's choice of which
  other angle plays "Y" (recipient) vs "Z" (untouched). This gives Mulan a
  fully forced, Shan-Yu-choice-irrelevant "transfer θ between angle slots"
  move whenever some angle exceeds θ — the key new mechanistic building
  block this round, usable for the "if" direction's induction on n.

Known dead ends (do not retry): flat "min angle ≥ Δ" or "all angles >θ"
invariants for θ≤90 (both refuted, by two independent explorers);
float-based discretized simulation (use exact rationals only); any
"θ ≤ threshold" style answer (refuted — the answer is a divisibility
condition on 180/θ, not a size bound).

---

shave-and-halve-forcing: new
Target: Mulan wins iff θ=180°/n, n≥2 integer — full characterization.
Technique: explicit forced-move algebra (constructive strategy for Mulan;
obstruction argument for Shan-Yu), built around the new Shave lemma and the
Bisection lemma, induction on n.
Skeleton:
  1. Base case n=2 (θ=90°) — altitude construction, done.
  2. Inductive step: from any starting triangle, use repeated Shave moves
     to force all three angles to become exact integer multiples of θ in
     finitely many forced moves (residue-reduction), then finish via a
     discrete follow-up induction (Bisection lemma / recursive Shave on the
     now-integral triple) — by strong induction on n.
  3. θ>90°: import the proved defense.
  4. θ≤90°, θ≠180/n: obstruction via the residue-sum invariant (sum of the
     three angles mod θ is a fixed nonzero constant r₀=180 mod θ, so the
     shave-based algorithm can never drive all three to 0 mod θ) — but this
     only obstructs ONE algorithm, not all of Mulan's play; turning it into
     a genuine universal Shan-Yu strategy is the open gap.
Key lemmas: Shave lemma (proved, exterior-angle algebra + numeric check);
Bisection lemma (proved); θ=90 lemma (proved); residue-sum invariant
(trivial/proved, but insufficient alone for the "only if" direction).
Open gaps: (a) precise finite termination bound/monovariant for the
induction on n in step 2; (b) turning the residue obstruction into a full
Shan-Yu strategy valid against ALL Mulan strategies, for θ≤90°, θ≠180/n.
Cases to cover: n=2 (done), n≥3 (open core), θ>90 (done via import), θ≤90
non-divisor (open core, shared gap with other approaches).
Watch out for: conflating "obstructs one specific Mulan algorithm" with "a
genuine universal Shan-Yu defense" — these are different logical claims.

mod-theta-invariant: new
Target: same full characterization, approached from the invariant/potential
side rather than an explicit algorithm (KB "Invariants & monovariants").
Technique: classical invariant/monovariant method — reuses the proved
θ>90 invariant as the template, generalizes to a residue-class /
distance-to-nearest-multiple-of-θ invariant for θ≤90 non-divisor case;
phrases the θ=180/n direction as a monovariant Φ = #angles that are exact
integer multiples of θ, strictly increasing toward Φ=3.
Skeleton:
  1. Import θ>90 invariant (proved).
  2. θ=180/n: define Φ(triangle) and show Mulan has a forced move weakly
     increasing it (via Shave/Bisection lemmas), finishing at Φ=3.
  3. θ≤90, θ≠180/n: define "distance to nearest multiple of θ" invariant
     min(x mod θ, θ − x mod θ) per angle; conjecture Shan-Yu can always keep
     a child preserving a positive (possibly shrinking, but never exactly 0)
     lower bound on this quantity across all three angles, using that only
     finitely many moves occur before any purported win.
Key lemmas: residue-sum invariant ρ(A)+ρ(B)+ρ(C)≡180 (mod θ) (trivial,
proved); θ>90 invariant (proved); "distance-to-multiple non-degeneracy"
(open, the central new conjecture of this approach).
Open gaps: proving the distance-to-multiple invariant actually survives
every possible Mulan move (not just an average/heuristic argument) — the
central open gap, shared in spirit with shave-and-halve-forcing's gap (b)
but attacked directly as an invariant rather than as an algorithm
obstruction; worth cross-checking against that approach for consistency or
merge.
Cases to cover: θ>90 (done), θ=180/n (monovariant, shares mechanism with
sibling), θ≤90 non-divisor (open core).
Watch out for: the metric must wrap correctly at the boundary (θ itself is
0 mod θ); do not reintroduce the refuted flat "all angles <Δ" style bound.

ngon-arc-reduction: new
Target: same full characterization, via a genuinely different top-level
REDUCTION: encode θ=180/n triangles as compositions of n into 3 parts
(dividers on n unit arcs), reducing the endgame to a finite discrete
combinatorial game modeled on the crux `aimo-0225` (RMM 2015 counters-on-
an-n-gon, 2-adic-valuation halving recursion) — different framing from the
raw real-angle induction of the other two approaches, even though it reuses
the same underlying cut formulas and Shave lemma for the "normal form"
reduction step.
Skeleton:
  1. Reachable-interval fact (proved): one A-cut's single-child new-angle
     range is (0,A)∪(C,180−B)∪(B,180−C).
  2. "If" direction: (a) normal-form reduction — force, in finitely many
     moves, a triangle whose 3 angles are all exact integer multiples of θ
     (shared step with shave-and-halve-forcing); (b) solve the resulting
     FINITE discrete "divider game" on compositions of n into 3 parts by
     its own from-scratch induction (work out n=2,3,4,5 by hand first),
     explicitly NOT assuming aimo-0225's mechanics transfer — only the
     methodological shape (reduce to normal form, then recurse on a
     discrete residual game) is borrowed.
  3. "Only if" direction: a "no closing necklace" argument — when 180/θ is
     not an integer, no exact tiling of 180° by θ-arcs exists (or, for
     rational non-divisor θ=180p/q, the natural period is qθ not θ, giving
     Shan-Yu more room) — reframe as (or show equivalent to) the residue
     obstruction in mod-theta-invariant.md.
Key lemmas: reachable-interval decomposition (proved); normal-form
reduction (shared, open per shave-and-halve-forcing); discrete n-gon
divider game is a Mulan win for all n≥2 (open, new — needs from-scratch
finite induction, not borrowed from aimo-0225's actual proof).
Open gaps: the discrete divider-game induction itself (new content, not yet
attempted at all — start with small n by hand); the "no closing necklace"
argument's rigor, and its consistency with the proved θ>90 result at
overlapping values like θ=120°.
Cases to cover: n=2..5 discrete game by hand; θ>90 (import, no rework
needed since n<2 there).
Watch out for: don't assume aimo-0225's actual game rules transfer — it is
a different game, only the two-phase "normal form then recurse" strategy
shape is analogous, every step must be reproved.

maximal-safe-set-fixedpoint: new
Target: same full characterization, via explicit game-theoretic
formalization: define Mulan's win region W (least fixed point) and
Shan-Yu's safe region S (greatest fixed point, Knaster–Tarski on the
"some child stays safe" operator); reduce the whole problem to
"characterize exactly when S=∅" — a different top-level route from
constructing strategies directly (the other three approaches), since here
both directions are proved by exhibiting/refuting membership in S rather
than describing a strategy step by step.
Skeleton:
  1. Formalize W = ∪ₖ Wₖ (win in ≤k moves) and S = complement / greatest
     fixed point of "for every cut, some child stays in S"; note
     S=∅ ⟺ Mulan wins the whole game (Shan-Yu otherwise picks any T₀∈S).
  2. θ>90°: exhibit S ⊇ {all angles <θ} (proved, same content as the other
     approaches' θ>90 defense, repackaged as a closure verification).
  3. θ=180/n: proof by contradiction — assume S≠∅, pick T∈S, apply the
     Shave lemma repeatedly (forced membership propagation through S),
     derive a well-founded-descent contradiction via a monovariant (e.g.
     Σ⌊angle/θ⌋) that must strictly decrease along the forced S-sequence
     but is bounded below — exploiting that 180=nθ is an exact integer
     multiple only when θ=180/n.
  4. θ≤90°, θ≠180/n: construct S_θ directly (e.g. via the residue
     obstruction of mod-theta-invariant.md) and verify it is closed under
     "some child survives" — i.e. a genuine pre-fixed-point, hence ⊆ S.
Key lemmas: S/W well-defined via Knaster–Tarski on P(triangle space) (needs
one paragraph, standard); θ>90 closure (proved); Shave-forced descent
monovariant for θ=180/n (open, new mechanism — find the right quantity by
hand on small n first); S_θ closure verification for non-divisor θ≤90
(open, shared gap with mod-theta-invariant.md).
Open gaps: the descent monovariant in step 3 (new, not yet nailed down);
the S_θ closure check in step 4 (shared open core with mod-theta-invariant
— if either approach's builder cracks it, the other should import rather
than re-derive); care needed since the triangle state space is a continuum,
not finite — use the Wₖ formulation for any finiteness claim, not an
abstract fixed point alone.
Cases to cover: θ>90 (done), θ=180/n (open, new descent argument), θ≤90
non-divisor (open, shared core).
Watch out for: don't conflate the abstract (possibly transfinite in
principle) fixed point S with the problem's actual finite-move win
condition — always ground finiteness claims in the Wₖ = "win in ≤k moves"
increasing union, matching what `math-explorer-angle-tracking.md`'s
attractor computation numerically approximates.

---

**Note on the shared open core:** three of the four approaches
(shave-and-halve-forcing gap (b), mod-theta-invariant's central gap, and
maximal-safe-set-fixedpoint step 4) all ultimately need the SAME hard
fact — a genuine, universal Shan-Yu defense for θ≤90°, θ≠180/n, valid
against every possible Mulan strategy, not just an obstruction to one
algorithm. This is flagged explicitly in each file so builders/reviewers
treat a breakthrough on any one of them as importable into the others
rather than re-deriving three times. The ngon-arc-reduction approach is the
most likely to produce a genuinely different angle on this shared core
(via the discrete "closing necklace" framing) since it doesn't reduce to
the same residue computation by construction — this is the best candidate
for breaking a future plateau if the other three all stall on the same
wall.

**Build set recommendation for the outline-reviewer:** all four are fresh
(round 1, no prior population) and genuinely diverge in top-level framing
(explicit algorithm / classical invariant / discrete combinatorial
reduction / formal fixed-point game theory) while all correctly reuse the
same rigorously-proven anchors (θ=90° lemma, θ>90° defense, Bisection
lemma, and this round's new Shave lemma). Recommend building all four in
parallel this round to see which framing makes the fastest progress on the
shared open core (θ≤90°, non-divisor θ, universal Shan-Yu defense) and
which best completes the θ=180/n induction.
