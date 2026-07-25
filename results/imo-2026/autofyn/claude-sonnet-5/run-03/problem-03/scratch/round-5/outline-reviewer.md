# Outline review — imo-2026-03, round 5

Read: `proof-outliner.md` (round 5), `current.md`, all 5 approach files,
`.ranking.json`, `knowledge_base.md`. Cross-checked the two riskiest new
numeric claims by independent Python search (see below).

## self-similar-induction-on-n — revise — APPROVE

Target: close `Case-B(m,k)` (the tail-untouched TOP-ONLY sub-case of the
newly-discovered middle regime), via a single-transfer exchange argument on
the extremal shape `B_ε = (2^{m-1}-ε, 2^{m-2}, …, 2, 1+ε)`.

- The reduction chain (Reduction B → specialize to TOP-ONLY → trichotomy
  collapses to Case A ∪ Case B, Case A already closed by Dominant-Chain) is
  correctly built entirely from already-certified lemmas
  (`altsum-reformulation-and-single-insertion.md`, Dominant-Chain Theorem).
  No new unjustified step here.
- I independently stress-tested the extremal-shape claim (step 4) at `m=4`:
  random search over partitions `B` of `16` into `≤4` parts with
  `max(B)<8`, computing `OddSum(B∪Γ_2)` — best found `≈14.9997`, and the
  conjectured near-extremizer `B_ε=(7.999,4,2,1.001)` gives `≈14.999`,
  both approaching the target bound `2^m-1=15` from below and neither
  exceeding it. The claim is numerically well-supported, not just asserted.
- Watch-out clause (step 5 must not silently re-invoke Proposition C's
  peel-and-recurse) is explicitly stated and checkable by the reviewer next
  round: the transfer must move mass *within* `B`, not spawn a recursive
  sub-instance.
- Cases to cover (ties during transfer, boundary `b1→2^{m-1}⁻`, `B` with
  fewer than `m` parts) are all named.

No fatal flaw. Sound skeleton, mechanism stated for the key lemma, numerics
corroborate the extremal-shape target before the builder commits to it.

## greedy-reduction-geometric — revise — APPROVE

Target: fully general lower-bound Case 2 (cuts split between top piece and
tail), via a Joint Dominance-Chain extending Theorem 5's peeling telescope
to the merged sequence.

- Correctly scoped as the complement of `self-similar-induction-on-n`'s
  target this round (Case-B(m,k) vs. the genuinely-general middle regime,
  `j+c≤m`) — no duplicated target, per the outliner's own explicit
  partition and the round-4 memory rule ("assign shared crux to exactly
  ONE approach").
- Step 5 ("identify precisely where the joint induction breaks, honestly
  diagnose a new obstruction... rather than asserting success") is the
  right instruction — this is genuinely open, exploratory content, and the
  outline does not pretend the Joint Dominance-Chain closure is already
  known to work ("Key lemmas" section explicitly labels it "candidate...
  must be checked, not assumed").
- The watch-out about silently rediscovering Proposition C's circularity is
  named and given a concrete falsifiable test (residual sub-problem must
  shrink in fragment count or scale). Good — this is exactly the kind of
  explicit circularity check round 4's plateau-break needed.

No fatal flaw; this is honest exploratory work on a genuinely new target,
correctly flagged as possibly-negative in outcome.

## universal-halving-adversary — revise — APPROVE with one required check

Target: explicit multi-piece "shave-below + self-bisection" construction
for the balanced region, cross-checked against the two known worked
examples (`n=2`: 0.505, `n=3`: ≈0.5004).

- Correctly imports only certified lemmas (Doubling, General Insertion,
  Subadditivity, Tie-neutrality, Single-Insertion).
- Step 2's "sidestep the limit" claim (choose the smaller shaved fragment
  to exactly equal an existing lower-rank value, rather than taking
  `ε→0`) is a good simplification **but must be numerically verified by
  the builder before being used as the proof mechanism**, per the standing
  memory rule ("ALWAYS numerically stress-test any explicitly-described
  adversary/algorithmic step... before writing it up as a lemma") — flag
  this explicitly as a required first action, since it is new to this
  round's construction and not yet checked anywhere in the corpus.
- Step 5 (the "matching rule" — general assignment + worst-case bound) is
  correctly labeled the real open target, not asserted proved.
- Note directly for the record: `dyadic-potential-invariant`'s round-4
  counterexample construction (`n=2`, `(0.35,0.34,0.31)`, mixed allocation
  giving 0.505) is *exactly* an instance of this approach's own
  shave-below+self-bisect mechanism (shave `p1` just above `p2`, bisect
  `p3`) — this is a good sign of convergent evidence, not a contradiction;
  the outliner should note in the write-up that this counterexample IS the
  n=2 worked example, not merely "consistent with" it.

## dyadic-potential-invariant — revise — APPROVE

Target: pivot away from local exchange/perturbation mechanisms (both
already refuted, twice) to a genuinely different mechanism — LP
extreme-point / vertex characterization proving the Tie-or-zero Lemma.

- This is a real pivot, not a third attempt at the same refuted mechanism:
  rounds 3–4 both used *local* single-transfer exchange arguments (refuted
  by exact counterexample both times); this round's target is a *global*
  compactness/vertex argument, structurally unrelated to a local exchange
  step, so it does not repeat the documented dead end.
- Step 3's cited tool ("Extreme value theorem / Lagrange multipliers on a
  compact manifold") is a real entry in `knowledge_base.md` (line 47) —
  confirmed present, correctly named.
- The vertex characterization ("active constraints = dimension ⟹ a
  coordinate is 0 or two order-constraints are simultaneously tight") is
  the standard LP-vertex fact and is stated correctly at a high level; the
  outline appropriately flags this must be "proved rigorously... not just
  an appeal to intuition" rather than asserted.
- Step 4's "min over finite union of regions attained at a vertex of one
  of them" is flagged by the outline itself as needing careful, non-hand-
  waved treatment (regions can share boundary ties) — good, this is
  exactly the kind of subtlety that sinks LP-vertex arguments if glossed
  over; keep it as a required proof point, not an aside.
- Step 5 is honestly scoped as possibly existence-only, not necessarily an
  explicit closure — correctly distinguished in kind from
  `universal-halving-adversary`'s explicit-construction attempt.

No fatal flaw. This is a legitimate new technique for this approach, with
its foundational tool correctly sourced from the knowledge base.

## lp-duality-split-polytope — new — APPROVE (register)

Target: the whole problem via LP/KKT duality on the split polytope; this
round's concrete deliverable is Multi-piece Necessity for the upper-bound
balanced region.

- Genuinely new top-level framing relative to the other 5 (peel-based x2,
  explicit-construction, LP-primal-vertex, layer-cake/measure) — it uses
  the *dual*/KKT side of the LP formulated in step 1, a different
  mechanism from `dyadic-potential-invariant`'s *primal*-vertex approach
  even though both sit on the same underlying "split polytope" object.
- Diversity risk, flagged explicitly for the orchestrator: three approaches
  (`universal-halving-adversary`, `dyadic-potential-invariant`,
  `lp-duality-split-polytope`) now all target the same narrow balanced-
  region gap. This is not the CLAUDE.md single-gap trap in the strict
  sense — they attack it with three different mechanisms (explicit
  construction / primal vertex structure / dual necessity) producing three
  independently-valuable and independently-falsifiable results, and the
  outliner's own text explicitly designs them as complementary (one
  produces a constraint the other two can consume), not as three
  redundant attempts at an identical claim. But if the underlying LP/
  split-polytope framing itself turns out to be insufficient for the
  balanced region, all three die together — watch this over the next 1-2
  rounds; if all three stall on genuinely-LP-specific obstructions, that
  is the signal to open a 4th, non-LP framing for the upper bound (the
  layer-cake framing, currently lower-bound-only, does not cover this).
- Step 4 (the actual necessity proof) is correctly labeled as the target,
  not asserted; the outline explicitly requires the argument work
  structurally for every `n`, not per-case verified only at `n=2,3` — good,
  since a per-case-only "proof" would not be a proof.
- Step 6 (extending to the lower bound) is correctly marked optional/
  stretch, not required — keeps this round's deliverable honest and
  scoped.
- Watch-out clause about not silently re-deriving the (already twice-
  refuted) "top-only is optimal" claim in disguise is well-placed — the
  necessity claim is literally the negation of that refuted claim, so this
  is a real risk to check, not boilerplate.

No fatal flaw. Register and build.

## layer-cake-parity-reframing — not requested this round — hold

The outliner correctly leaves this out of this round's active work: it
remains registered, no new lead was found for its Coupling Obstruction this
round, and none of the other 5 approaches duplicate its territory. Consistent
with the standing memory rule to hold back approaches with no fresh
concrete content this round while keeping them ranked. Not RETHINK — it has
real proved content (layer-cake identity, per-piece additivity, Coupling
Obstruction) and stays live for a future round when a new lead surfaces.

## Overall field assessment

All 6 registered approaches (5 continuing + 1 new) are genuinely
non-duplicated this round: each targets a distinct, previously-open gap
(Case-B(m,k) vs. the fully general Case 2 on the lower-bound side;
explicit construction vs. primal-vertex structure vs. dual-necessity on the
upper-bound side; layer-cake held). No approach repeats a documented dead
end (checked each skeleton against `current.md`'s dead-end list: static
Q-priority, static tail-priority, literal/restricted Cut-Reallocation
Exchange Lemma, peel-at-depth-1/even-depth, Suffix-Match-alone — none
reappear). No circular step found. Diversity is real: two structurally
different lower-bound mechanisms (peel-based induction, dominance-chain
telescope) and three structurally different upper-bound mechanisms
(explicit construction, primal LP vertex, dual LP/KKT), plus the held
layer-cake framing as a fourth lower-bound angle in reserve.

Flagged risk (not fatal, watch next round): the three upper-bound
approaches share the same underlying "split polytope" object even though
their mechanisms differ — if all three stall on an LP-specific obstruction
for 2+ rounds, treat that as the plateau signal per CLAUDE.md and open a
non-LP 4th upper-bound framing (the layer-cake identity's own budget-to-
measure step, or a fresh explorer lens, are the natural candidates).

## Ranker actions taken

- Registered new approach `lp-duality-split-polytope`.
- Ranked the field: established approaches anchored on round-4 `last_note`
  strength (universal-halving-adversary's certified reusable lemma +
  documented negative result > greedy-reduction-geometric's closed
  sub-regime > self-similar-induction-on-n's trichotomy discovery >
  layer-cake-parity-reframing's single-round new-framing content >
  dyadic-potential-invariant's pure negative result, no positive closure);
  new entrant `lp-duality-split-polytope` compared against established
  peers at cold-start (paired against a mid-field established approach as
  a draw-ish newcomer anchor, and against the currently-lowest-rated
  established approach as a win, since it enters with more design-stage
  structure than dyadic-potential-invariant had entering round 3).

build set: self-similar-induction-on-n, greedy-reduction-geometric, universal-halving-adversary, dyadic-potential-invariant, lp-duality-split-polytope
