## imo-2026-03 (lens: Xiang Yu's counter-strategy / upper bound on c(n))

### Setup facts established (apply to both bounds, useful for outliner)
- Because pieces are just numbers (no other structure), once the final multiset of
  pieces is fixed, alternating "take the largest remaining piece" is optimal for
  BOTH players simultaneously in the claiming phase (standard exchange-argument
  fact for pick-a-number games). So with pieces sorted descending p_(1)≥p_(2)≥...,
  Liu Bang (first) ends up with Σ p_(odd rank), Xiang Yu with Σ p_(even rank).
  This means the whole problem collapses to a **one-shot optimization**: Liu Bang
  picks a partition of [0,1] into ≤ n+1 pieces; Xiang Yu (seeing it) refines it by
  adding ≤ n more cut points (each splits one existing piece into two); the final
  odd-rank sum is Liu Bang's total.  There is no further real-time adaptivity in
  the claiming phase itself.
- **Alternating-sum identity (key tool).** For m sorted pieces p_(1)≥...≥p_(m),
  writing S = Σ_i (-1)^{i+1} p_(i), Liu Bang's total = (1+S)/2 (since total+S =
  2·(odd-rank sum)). For odd m=2n+1 this telescopes as
  S = p_(1) − (p_(2)−p_(3)) − (p_(4)−p_(5)) − ... − (p_(2n)−p_(2n+1)),
  a sum of nonnegative gaps subtracted from the top piece. Xiang Yu wants S small
  (ideally lets it collapse toward 0, pushing Liu Bang toward 1/2); Liu Bang wants
  to prevent that collapse. This is the natural "potential" for the upper-bound
  argument — recommend the outliner build the upper bound around minimizing S.

### Distinct upper-bound opening ideas
1. **Cancelling-pairs strategy (the strongest one found).** Xiang Yu tries to
   pair up Liu Bang's original pieces into (near-)equal consecutive-rank duos so
   they cancel in S, using at most one extra mark per pair: to pair a big leftover
   piece C against a smaller original piece q, split C into (q, C−q) — the q-chunk
   ties with the original q piece (they become adjacent equal ranks, contribute 0
   net); the remainder C−q becomes the new "leftover" fed into the next pairing
   step. Applied naively as pure greedy pairing down the sorted list this is
   *too strong* and gives a wrong (too-low) bound — see caveat below.
2. **Bisect-vs-match local rule (verified exactly for n=1, likely the right local
   move at each step).** When Xiang Yu must dispose of one mark on a "current
   leftover" piece of size C against the next original piece q, his best choice
   is a = max(C/2, min(C,q)): either bisect C evenly (if q is small, q ≤ C/2) or
   match a chunk of C exactly to q (if q > C/2), whichever produces the larger
   resulting median/rank-2 value. I verified this rigorously by hand for the
   n=1 two-piece case (see below) — the pure "always match" pairing strategy
   (idea 1) is a *strict over-simplification* that is not optimal when the next
   piece is small relative to the leftover; bisecting is better then. **This
   refinement is the actual mechanism**, and it should replace naive pairing in
   any upper-bound writeup.
3. **Degenerate-sliver caution (a dead-end noticed and worth flagging).** Naively
   one might think Xiang Yu can insert near-zero slivers to "flip parity" and
   freely reassign ranks. This is FALSE in general: a sliver, being globally the
   smallest value, always sorts to the very bottom of the whole list, not locally
   after a chosen piece — so it cannot be used to flip parity of an arbitrary
   suffix independent of its size. The only way slivers help is when they are the
   deliberately small "remainder" of a match-split (idea 1), not as a free
   standalone tool. Don't let the outliner assume free parity-flipping.
4. **Recursive / self-similar structure.** The exact optimum (see numeric
   evidence below) has Liu Bang's optimal partition in a geometric 2:1 ratio
   cascade (pieces proportional to 2^n, 2^{n-1}, ..., 2^1, 2^0), i.e. the top
   piece exceeds the sum of all the others by exactly one "unit". This is
   structurally the same idea as the crux `aimo-0117`: "Assign values as a
   two-sided geometric (dyadic) sequence so the single largest value strictly
   exceeds the sum of all the others" — a genuinely relevant analog (see below).
   The upper bound proof likely needs an induction on n peeling off the top piece
   (of size 2^n/(2^{n+1}-1)) and reducing to the size n−1 subgame on the
   remaining stick of total mass (2^n−1)/(2^{n+1}-1).

### Candidate formula for c(n) — CONJECTURE, verified numerically for n=1,2
- **c(n) = 2^n / (2^{n+1} − 1).**
- n=1: c(1) = 2/3. I derived this **exactly by hand** (not just numerically):
  with Liu Bang's single mark at x, if x ≤ 1/3 Xiang Yu's optimal reply is to
  bisect the big piece evenly giving Liu Bang (1+x)/2; if x ≥ 1/3 Xiang Yu's
  optimal reply is to carve a piece of size exactly x off the big piece giving
  Liu Bang exactly 1−x. Liu Bang's total as a function of x is maximized at
  x=1/3, value 2/3, achieved exactly (not just as an infimum) — multiple Xiang
  Yu replies tie at 2/3 (0 marks, or splitting 2/3 into two 1/3's). This is a
  complete, verifiable sub-argument for n=1 the outliner/builder can lift directly.
- n=2: numeric grid search over Liu Bang's 2-parameter partition space, with an
  (near-exhaustive, not just heuristic) grid search over Xiang Yu's ≤2 marks
  distributed among ≤3 pieces (0, 1, or 2 splits, same or different pieces),
  found the optimum essentially exactly at partition (4/7, 2/7, 1/7), giving
  Liu Bang total = 0.571428... = 4/7 to 4 decimal places, matching 2^2/(2^3−1)
  = 4/7 exactly. A broad random/coarse search over all partitions confirmed no
  better partition was found (best ≈ 0.5713, matching 4/7 within grid error).
  **This is strong numeric evidence, not a proof.**
- Caveat: my FIRST guess, c(n) = (n+1)/(2n+1) (motivated by a naive "all 2n+1
  final pieces equal" picture), matches n=1 (2/3) but is **numerically refuted**
  for n=2 — it predicts 3/5 = 0.6, but the true optimum is only ≈0.571 (4/7).
  Flag this as a **dead end / wrong conjecture** so the outliner does not chase
  it: the "equal partition" (0.4,0.4,0.2)-style construction for n=2 is
  catastrophic for Liu Bang — Xiang Yu can push it down to ≈0.5 (numerically
  confirmed, see below), because two equal LB pieces are trivially cancellable by
  Xiang Yu's matching-split trick.

### Cheap-kill candidates
- Any partition where Liu Bang creates **two equal (or near-equal) pieces** is a
  cheap kill for Xiang Yu: he degenerate-splits one to (near-)duplicate the
  other, they cancel adjacent ranks, contributing ≈0 net to the alternating sum.
  Verified numerically: (0.4,0.4,0.2) and (1/3,1/3,1/3) and (0.4472,0.4472,0.1056)
  all collapse to Liu Bang total ≈0.500, far below the 4/7 optimum. **Any
  approach whose construction has ties among Liu Bang's pieces is a dead end for
  the lower bound and a cheap disproof target for the upper bound.**
- Symmetry/scale check: c(n) should be strictly decreasing toward 1/2 as n→∞
  (more marks for Xiang Yu ⇒ better for him); 2^n/(2^{n+1}-1) → 1/2 monotonically
  from above — consistent, good sign for the conjecture's plausibility.

### Knowledge-base entries to use
- `knowledge_base.md` did not have a directly-named "cake-cutting alternation"
  entry; the general induction/extremal-principle and telescoping-and-summation
  style entries are the closest generic tools (see general list near lines
  150-190 of `knowledge_base.md`: Induction — ordinary/strong/structural;
  extremal-principle framing for "must be" claims). The load-bearing tool is the
  **alternating-sum telescoping identity** derived above (Σ(-1)^{i+1}p_(i)); treat
  it as the problem-specific potential function, cite it explicitly as a
  telescoping-sum technique.

### Analogous past problems (cruxes)
- **aimo-0117** (crux: "Assign the played values as a two-sided geometric
  (dyadic) sequence so that the single largest value strictly exceeds the sum of
  all the others" / "Defer committing the extreme value until the opponent's
  move vacates its target cell...") — genuinely analogous: it's a turn-based
  value-game where a **dyadic geometric progression with the top-heavy property**
  (largest > sum of rest) is the extremal construction, exactly matching the
  2^n:2^{n-1}:...:1 structure found numerically here. Worth reading in full for
  the proof technique used to show that structure is optimal.
- I searched `games-and-strategy` (combinatorics, 39 cruxes) and broader keyword
  scans (stick/interval/pieces/alternat/pairing/cake/claim) across the whole
  corpus; most hits are win/lose or pairing-domino games on discrete boards, not
  continuous-value alternating-claim games. **No other crux is a close structural
  match**; aimo-0117 is the best analog found. Do not force the domino/pairing
  win-lose cruxes (aimo-0115, aimo-0461, aimo-0596, aimo-0854 etc.) — they are
  about parity/existence of a legal move, not value-maximization, so their
  "pairing" mechanism is superficially similar in vocabulary but not in what is
  being optimized.

### Prior progress
- None (workspace was empty at round 1 start; this is the first exploration).

### Dead ends (do not retry)
- Guessing c(n) = (n+1)/(2n+1) — matches n=1 by coincidence but numerically
  refuted at n=2 (predicts 0.6, true value ≈0.571). Do not build the lower-bound
  construction around "final 2n+1 pieces all equal."
- Constructing Liu Bang's partition with any tied/equal pieces — Xiang Yu kills
  this down to ≈1/2 via a cheap degenerate-split duplication.
- Treating Xiang Yu's optimal single-piece split as "always match to the next
  piece down" (pure greedy pairing) — this over-shoots and is not optimal when
  the next piece is small; verified by hand that bisecting is sometimes strictly
  better for Xiang Yu (n=1, x<1/3 regime).
- Assuming Xiang Yu can use near-zero slivers to freely "flip parity" of ranks
  independent of position — false; a degenerate sliver always sorts to the very
  bottom of the whole list, not locally after a chosen piece.

### Small-case / intuition notes (all labeled CONJECTURE except where noted PROVED)
- PROVED (by hand, full case analysis): c(1) = 2/3, attained by Liu Bang marking
  at x=1/3 (or 2/3).
- CONJECTURE (strong numeric evidence, grid + local refinement search,
  agreement to 3+ significant figures): c(2) = 4/7, attained by Liu Bang's
  partition (4/7, 2/7, 1/7).
- CONJECTURE (pattern extrapolation from n=1,2, not numerically checked for
  n≥3 due to time budget): **c(n) = 2^n/(2^{n+1}−1)**, with Liu Bang's optimal
  partition being the dyadic cascade (2^n, 2^{n-1}, ..., 2^1, 2^0)/(2^{n+1}−1).
  The outliner should verify n=3 numerically (predicts c(3)=8/15≈0.5333) before
  committing hard to this formula, and should look for a clean recursive/
  inductive proof peeling off the top piece 2^n/(2^{n+1}-1) and reducing to the
  n−1 subgame on the remaining mass, using the alternating-sum identity as the
  invariant that make the induction go through for the upper bound.
