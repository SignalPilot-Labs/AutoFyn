## imo-2026-03 (lens: Liu Bang's guarantee / lower bound)

### Setup recap
Claiming-game lemma (used freely, should still be proved from scratch in the outline):
given any fixed finite multiset of piece-lengths summing to 1, if both players always
greedily claim the currently-largest unclaimed piece, this is optimal for **both** (a
standard exchange argument: swapping a smaller current pick for a later larger one that
your opponent would otherwise have taken never helps the opponent and never hurts you —
since the total is fixed at 1, this is a zero-sum game and greedy-vs-greedy is a Nash
equilibrium). Consequence: sorting the final pieces descending, Liu Bang (mover first)
receives exactly the sum of **odd-ranked** pieces (1st, 3rd, 5th, …) and Xiang Yu the
even-ranked ones. This reduces the whole problem to: Liu Bang picks ≤n cut points, Xiang
Yu adversarially adds ≤n more, and the payoff is the odd-rank-sum of the resulting
piece-multiset (sorted descending). I did not re-derive this lemma rigorously here (it's
standard game-theory folklore for "alternately pick items from a fixed pool to maximize
own sum") — the outliner should still state and prove it as Lemma 1, it is not free.

### Small cases, worked with numerical optimization (sympy/scipy), then verified by hand for n=1

**n = 1.** Liu Bang marks one point at p (WLOG p ≤ 1/2), giving pieces {p, 1−p}. I
computed (grid + exact algebra) the median of the resulting 3-piece configuration
{p, y, (1−p)−y} as Xiang Yu ranges over all splits y of the larger piece (splitting the
smaller piece is always weakly worse for Xiang Yu, shown directly). Result:
- if p ≥ 1/3: Xiang Yu's best response leaves the median exactly p (splitting the big
  piece straddles p symmetrically); Liu Bang's guaranteed total = 1 − p.
- if p ≤ 1/3: Xiang Yu bisects the big piece into two equal parts each > p, pushing the
  median up to (1−p)/2; Liu Bang's total = 1 − (1−p)/2 = (1+p)/2.
- These two branches meet and are jointly minimized at **p = 1/3**, giving
  **c(1) = 2/3**, attained by Liu Bang marking the point at 1/3 (equivalently 2/3),
  i.e. pieces (1/3, 2/3). Xiang Yu's matching best response: cut the 2/3-piece exactly
  in half (or anywhere symmetric around its center — the median stays exactly 1/3), or
  equivalently cut at 2/3 to produce three equal 1/3 pieces. Verified this is a strict
  local optimum by scanning p over a fine grid (best found p ≈ 0.333, value ≈ 0.6665,
  matching 2/3 exactly).

**n = 2.** Numerically searched (grid, then finer local grid, then verified at high
resolution up to ngrid=400) over Liu Bang's two cut points and all of Xiang Yu's response
shapes (split two different pieces each once; or land both marks in a single piece,
producing 3 sub-pieces there). The dyadic guess (pieces in ratio 4:2:1, i.e.
**(4/7, 2/7, 1/7)**) gives a worst-case Liu total of **exactly 4/7** stably from
ngrid=100 up to ngrid=400 (no drift), while every other Liu configuration I tried
(equal thirds, near-dyadic perturbations) does *strictly worse* under a sufficiently
fine adversary search — a coarse grid can spuriously suggest a "better" non-dyadic point
because it under-samples Xiang Yu's true best reply (I caught and discarded exactly this
artifact: a point that looked like ≈0.573 at ngrid=60 dropped to ≈0.569 at ngrid=300,
below 4/7, once the adversary's search was refined). So **c(2) = 4/7**, via
Liu Bang's dyadic strategy.

**n = 3 spot-check.** Dyadic pieces (8/15, 4/15, 2/15, 1/15) against a randomized search
over every way of distributing Xiang Yu's 3 marks across the 4 pieces (all
compositions of 3 into 4 parts, thousands of random splits per distribution): the
minimum found over all distributions/trials is **exactly 8/15**, attained when Xiang Yu
puts *all three* of his marks into the single largest (8/15) piece and re-splits it with
the *same* dyadic ratios (4:2:1) internally — a self-similar attack. No distribution or
random trial beat 8/15 downward. This is strong (if numeric/conjectural) evidence for
the closed form below.

### Conjectured closed form
**c(n) = 2ⁿ / (2ⁿ⁺¹ − 1).**

Check: n=1 → 2/3 ✓ (hand-verified exactly). n=2 → 4/7 ✓ (numerically stable to 3+ digits
across grid refinements). n=3 → 8/15 ✓ (numerically stable across thousands of random
adversary trials, tight equality found).

### Candidate Liu Bang strategy (the construction half)
Mark the n points so the n+1 resulting pieces have lengths
`2ⁿ/D, 2ⁿ⁻¹/D, …, 2¹/D, 2⁰/D` where `D = 2ⁿ⁺¹ − 1` (i.e. a strictly dyadic/geometric
partition, largest piece exactly double the next, etc., down to the smallest). This is
the "binary weights" idea explicitly suggested in the lens prompt, refined: NOT the
naive "n+1 equal pieces" (that strategy is fragile — see Dead ends below), but a
geometric decay by factor 2.

Intuition for *why* dyadic ratio 2 is forced, not merely convenient: if any two adjacent
pieces had ratio > 2, Xiang Yu could bisect the larger one into two pieces each still
bigger than the smaller of the pair, effectively "duplicating" a large piece and pushing
two big pieces to adjacent even/odd ranks in a way that increases his even-rank share;
if the ratio were < 2, Liu Bang would be leaving value on the table (could have shifted
mass from a small piece to make the recursive structure with the same total more
front-loaded toward Liu Bang without giving Xiang Yu more room to bisect
advantageously). The exact ratio 2 threshold is exactly balanced (as literally seen in
the n=1 branch computation above, where p=1/3 is the unique point where "splitting the
big piece symmetrically" and "leaving the small piece alone" tie).

### Main obstacle for the lower-bound proof
Need a clean inductive/invariant argument that for the dyadic configuration, **any**
distribution of Xiang Yu's ≤n marks across the n+1 dyadic pieces cannot push the
odd-rank-sum below 2ⁿ/D. The n=3 numerics suggest the extremal Xiang Yu attack is
self-similar (concentrate all cuts on the single largest piece, recursively re-imposing
the same dyadic ratios inside it) — this smells like it wants a **majorization**
argument: show the multiset of final pieces is always majorized (in the "partial sums
of sorted-descending values" sense) by the multiset obtained from the self-similar
attack, and that majorization is a monotone certificate for the odd-rank-sum functional
(this needs its own lemma — odd-rank-sum is NOT simply monotone under majorization in
general, so this is a real gap to resolve, likely via an exchange/smoothing argument
tracking how a single split of one piece can only move value between adjacent ranks).
This is the crux gap for whoever builds this approach.

### Cheap-kill candidates
- Immediate sanity bound: c(n) ≥ 1/2 is trivial for any Liu strategy with the "equal
  n+1 pieces" idea in the n=1 case degenerates to exactly 1/2 as Xiang Yu's damage
  supremum — but dyadic strictly beats this (2/3 > 1/2), so the naive equal-division
  idea is not even a good starting Liu Bang strategy, let alone tight.
- Parity/rank-count facts: with n+1 initial and up to n more cuts, final piece count is
  between n+1 and 2n+1; Liu Bang always gets ⌈k/2⌉ of the k pieces by rank (k = final
  piece count), which is between n+1 and n+1 (exactly n+1 pieces claimed by Liu Bang
  when k=2n+1, since ⌈(2n+1)/2⌉ = n+1) — Liu Bang always claims exactly n+1 pieces
  regardless of how many cuts Xiang Yu actually uses. Useful structural fact but doesn't
  by itself pin the value.

### Knowledge-base entries to use
- **Constructive vs. existence** ("find all/largest n needs an upper bound AND a
  matching construction") — directly governs the required proof shape: this lower-bound
  route only delivers half (the construction + guarantee); the matching Xiang Yu
  strategy forcing ≤ c(n) is a separate (upper-bound) route, needed for `solved`.
  Explicit answer stated, must be verified by substitution — done above for n=1,2,3
  (n=1 by hand, n=2–3 numerically).
- **Invariants & monovariants** / **Pigeonhole / extremal principle** — likely the
  right lens for the missing majorization-style lemma (track a running invariant across
  Xiang Yu's individual cuts one at a time, since he makes ≤n cuts and each cut only
  locally perturbs the sorted order — an exchange/smoothing argument in the spirit of
  the "piecewise-concavity smoothing" and "SOS" entries, but for a discrete rank-sum
  rather than a continuous functional).
- **Constructive / incremental** entry (realize every value by starting from an extreme
  and adding one unit at a time) — could structure an induction on Xiang Yu's marks
  one-at-a-time rather than all-at-once, turning "≤n simultaneous adversarial cuts" into
  an n-step process with an invariant maintained after each step.

### Analogous past problems (crux corpus)
- **aimo-0718** (combinatorics, games-and-strategy / invariants-and-monovariants):
  "Elisa's treasure chests" — adversarial fairy locks chests, Elisa must keep gem
  counts balanced; the solution proves a bound via **majorization** of the sorted
  chest-count sequence by an explicit dyadic-ish comparison sequence, verified
  inductively step-by-step as the adversary acts. This is the closest structural analog
  I found: same "maintain majorization against an adaptive adversary, one step at a
  time" flavor as the likely missing lemma here. Worth reading in full for the
  induction-on-majorization technique, though the chest problem's actual combinatorial
  content (locking chests) is unrelated to stick-cutting.
  Reused technique: strict majorization invariant is proved by induction over adversary
  moves individually rather than trying to handle "any adversary strategy" in one shot.
- **aimo-0063** (cupcakes/Hall's theorem fair-division) — a fair-division flavor but the
  crux move (Hall's marriage + deletion induction) does not resemble the claiming-game
  structure here; flagged as *not* a strong analogy, included only because it's the
  closest "fair division of a divided resource" problem in the corpus.
- I did **not** find any crux in the corpus matching the specific "alternately claim
  pieces of a pre-cut stick, greedy optimal" game structure — this appears to be a
  genuinely fresh construction for this problem; no corpus problem should be cited as a
  template for the claiming-game lemma itself.

### Prior progress
None — no workspace/approaches existed before this round (fresh problem).

### Dead ends (do not retry)
- **"Liu Bang marks n+1 equal pieces of length 1/(n+1)"** (the strategy suggested at
  face value in the lens prompt) — checked concretely for n=2: equal thirds (1/3,1/3,1/3)
  is vulnerable to Xiang Yu concentrating **both** of his marks on a single one of the
  three pieces, splitting it into three equal ninths. Result: final pieces
  {1/3,1/3,1/9,1/9,1/9}, Liu Bang's odd-rank sum = 1/3+1/9+1/9 = **5/9 ≈ 0.556**, which
  is worse than both the dyadic guarantee (4/7 ≈ 0.571) and even worse than what the
  naive "split two different pieces evenly" counter would give (2/3 in the n=1-style
  sub-computation). Equal division is not robust to an adversary who saves both cuts for
  one piece — record this explicitly so no approach re-proposes equal (n+1)-division as
  the extremal Liu strategy.
- Coarse-grid numeric optimization is unreliable here in the direction of
  *overestimating* Liu Bang's guarantee (a coarse adversary search misses Xiang Yu's true
  best reply and reports a spuriously high value) — any future numeric check of a
  candidate Liu strategy must refine the adversary's grid substantially (I needed
  ngrid ≈ 300 before values stabilized) or, better, solve the adversary's optimization
  in closed form.

### Small-case / intuition notes (all conjecture, not proof)
- c(1) = 2/3 is the only one of these I verified by hand/algebra rather than pure
  numerics; treat it as solid.
- c(2) = 4/7 and c(3) = 8/15 are numerical (grid + randomized search), consistent to
  many digits with **c(n) = 2ⁿ/(2ⁿ⁺¹−1)**, but not proven.
- The extremal Xiang Yu counter-strategy against the dyadic Liu configuration appears
  (n=1,2,3 evidence) to always be: attack the single **largest** current piece,
  re-imposing the same dyadic ratio pattern inside it (self-similar). This self-similar
  structure is the strongest hint toward an inductive proof of the upper bound half too
  (i.e. it may pin down BOTH players' optimal play simultaneously, which would be very
  useful to the sibling upper-bound route).
