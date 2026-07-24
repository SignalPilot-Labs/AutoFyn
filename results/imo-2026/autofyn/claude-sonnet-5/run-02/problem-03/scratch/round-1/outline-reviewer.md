# Outline review — imo-2026-03, round 1

Problem: Liu Bang / Xiang Yu stick game. Determine c(n), the largest value
Liu Bang can guarantee. All three explorers/outliner agree on the target
c(n) = 2^n/(2^{n+1}-1), verified for n=1 (2/3) by hand. This is `compute_and_prove`,
so both the bound (upper bound argument) and the matching construction
(lower bound) are required for `solved`.

All three approaches correctly share and rely on the **claiming-subgame
reduction lemma** (fixed final multiset → greedy-largest-first is optimal
for both players → Liu Bang's value = sum of odd-sorted-ranks). This is a
sound exchange argument (swapping a non-greedy choice for the current max
weakly helps the swapper and weakly hurts the opponent — payoffs are
additive over the remaining multiset with no cross-terms) and is a fair
common prerequisite; not a diversity problem since it is a genuine shared
sub-lemma, not the whole proof.

## greedy-halving-adversary — APPROVE (build)

Whole-attempt: yes, targets full minimax value via one direct architecture
(explicit strategies both directions, no induction on n).

- Lower bound (ladder + superincreasing domination, Steps 5–6): the core
  mechanism is sound — a strictly superincreasing sequence dominates any
  refinement's odd-rank sum by its top term, because the total of
  everything below L_1 stays < L_1 regardless of subdivision. The flagged
  open sub-case (Xiang Yu subdividing L_1 itself) is a real gap but looks
  tractable by the stated peel-and-induct-on-k scheme; keep it flagged for
  the builder, not fatal to the outline.
- Upper bound (bisect-the-max + potential function, Steps 3–4): this is
  the crux, and it is honestly flagged as open (the "charging scheme").
  I checked this isn't circular — the claim is a genuine strong induction
  on remaining Xiang-Yu moves with a to-be-derived invariant, not an
  "it follows" hand-wave; the gap is real but the setup is legitimate and
  falsifiable/verifiable by the builder (e.g. hand-check n=2, n=3 by
  brute-force search over Liu Bang configs against this specific Xiang Yu
  strategy before attempting the general induction — cheap sanity check
  the builder should do first).
- Watch-outs (ties, "≤n" vs "=n" points) are correctly identified, not
  omitted.

No fatal flaw found. Ship as-is; the two open gaps (Step 4 charging
scheme, Step 6 L_1-split case) are exactly the right things to attack.

## induction-first-move-reduction — RETHINK, do not build this round

Whole-attempt: yes in intent (induction on n via first-move peel), but the
central mechanism is now **confirmed false**, not merely an "arithmetic
mismatch" as the outliner phrased it. I recomputed directly:

```
p = c(n) = 2^n/(2^{n+1}-1), c(n-1) = 2^{n-1}/(2^n-1)
p + c(n-1)*(1-p)  =  3*2^{n-1}/(2^{n+1}-1)   (n=2: 6/7)
actual c(n)                                  =  2*2^{n-1}/(2^{n+1}-1)   (n=2: 4/7)
```
6/7 > 4/7. This is not just "doesn't simplify to the right thing" — it is
strictly *larger* than the value the other two approaches (and all three
explorers) independently derive and numerically confirm as optimal. Since
c(n) is defined as the max Liu Bang can guarantee, a construction that
supposedly guarantees strictly more than c(n) is impossible — which means
the underlying strategic premise of Step 4 ("Xiang Yu cannot profitably
touch the protected piece p, so Liu Bang banks p in full and inherits
c(n-1) on the untouched rescaled remainder") **must be false**: Xiang Yu
evidently CAN profitably spend moves attacking the piece p, contradicting
the exchange-argument claim in Step 4 outright, not just leaving Step 6's
algebra unfinished.

This means the "protected piece, recurse on remainder" architecture is
fatally flawed as stated — no patch to Step 6 alone fixes it, because
Step 4's premise, not just the arithmetic, is wrong. Building on this
outline would waste builder effort re-deriving a recursion whose
governing assumption is already refuted. Per the RETHINK criteria (wrong
premise in a load-bearing step, confirmed by direct computation), this
approach is not buildable as-is.

If the outliner wants to keep an induction-on-n framing alive, it needs a
genuinely different inductive statement — e.g. a two-parameter induction
tracking both players' remaining points where Xiang Yu is also credited
partial optimal play on the protected region (not a clean "piece is fully
banked" split), or induct on a stronger claim about the whole value
function rather than a literal peel of one piece. Not registering this
slug this round per protocol (RETHINK approaches stay out of the
population so a refuted line can't pollute ranking).

## smoothing-compactness-certificate — CHANGES REQUESTED (build, lower priority)

Whole-attempt: yes, and it is a genuinely different top-level target
(uniqueness-of-extremizer via compactness + local perturbation) rather
than "construct explicit strategies," so it adds real framing diversity
against greedy-halving-adversary rather than just a technique variant.

- Step 2 (compactness/piecewise-linearity of the minimax value) is
  correctly reasoned: finitely many linear cells from sorted-rank
  combinatorial type, Weierstrass gives existence of a maximizer. Sound,
  and cheap to formalize.
- Step 3 (the smoothing lemma) is the entire load-bearing claim of the
  approach and is honestly flagged as having **no mechanism at all** —
  only numerical search evidence, which the outline correctly refuses to
  treat as a proof. This is the right amount of caution; it is not a
  buried "then it follows," it's explicitly marked open. But it means
  this approach currently has zero proven content beyond the shared
  lemmas and the existence-of-a-maximizer fact.
- Real risk (flagged by the outliner too): if Step 3 can't be closed with
  a mechanism distinct from re-deriving greedy-halving-adversary's
  potential function, this collapses into a more expensive restatement of
  approach 1. This is a legitimate diversity concern for future rounds,
  not a reason to cut it now — it's cheap to test.

Given the total lack of a derived mechanism, this is CHANGES REQUESTED,
not a clean APPROVE: the builder's job this round should explicitly be a
feasibility probe (attempt the n=2 local-optimality computation by hand
or computer algebra, as the outliner suggested) before committing to the
general perturbation argument. If no distinct mechanism emerges this
round, recommend deprioritizing next round in favor of doubling down on
greedy-halving-adversary's Step 4 gap or opening a fresh, farther-away
framing.

## Diversity assessment

Two live approaches after this cut: greedy-halving-adversary (explicit
dynamic strategy + potential function) and smoothing-compactness-certificate
(static uniqueness-of-extremizer + compactness). Both attack the same hard
direction (upper bound over arbitrary Liu Bang configurations) but via
genuinely different mechanisms, so the field is not fully collapsed to one
framing — acceptable for round 1, but thin. The lower bound
(ladder + superincreasing domination) is shared and essentially the same
across both, which is fine since that half is close to fully proved. If
both approaches stall on their respective upper-bound gaps for another
round or two, the next outliner pass should add a genuinely distant third
framing (e.g. an LP-duality / adversary-argument style bound, or a direct
combinatorial coupling argument) rather than another variant of "bound the
minimax directly."

## Ranking

Population seeded this round: greedy-halving-adversary (1516, winner),
smoothing-compactness-certificate (1484, loser) — greedy-halving-adversary
ranked higher because its open gap (Step 4's induction) is concrete and
directly attackable, whereas smoothing-compactness-certificate's core lemma
(Step 3) has no derived mechanism at all yet, only numerical evidence.
induction-first-move-reduction is not registered (RETHINK, refuted premise).

build set: greedy-halving-adversary, smoothing-compactness-certificate
