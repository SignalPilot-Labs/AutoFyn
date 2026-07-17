## Status
partial

## Approach: potential-duality

**Framing.** Treat the whole thing as a zero-sum game and certify its value c(n)=2^n/D
(D=2^{n+1}−1) with a SINGLE potential function Φ that squeezes both bounds, rather than
by two separate strategy analyses. This is the LP-duality / monovariant framing, far
from both the constructive strategy-exhibition (approach 1) and the induction-on-n
(approach 2): the object of study is not a strategy but an invariant of configurations.

## Skeleton

1. **Reduce to odd-ranked (shared G1).** As in the other approaches, LB's claim = sum of
   odd-ranked pieces (greedy optimality). Import once certified. [GAP G1]

2. **Define the potential.** For a multiset of pieces sort descending q_1≥q_2≥…≥q_m and
   let R = number of cuts still available to the player about to move. Define a potential
   Φ(pieces, R_LB, R_XY) intended to equal the game value = LB's optimal guaranteed
   odd-sum from that position. Candidate closed form (to be pinned down): a weighted
   truncated sum of the top pieces with weights tied to the dyadic ladder 1,2,4,…,2^n,
   normalized by D. Anchor: Φ of the final geometric interleaving position = 2^n/D.
   [GAP P2 — find the exact Φ]

3. **XY-side monovariant (upper bound).** Show every LB mark, whatever it is, leaves Φ ≤
   its pre-move value scaled appropriately, and that XY has a reply to each LB cut keeping
   Φ ≤ 2^n/D; i.e. Φ is a supermartingale under XY's optimal play from the empty stick.
   Because a single cut of the top piece redistributes weight down the dyadic ladder by
   exactly the factor in the recursion 1/c(n)=2−2^{-n}. [GAP P3a]

4. **LB-side monovariant (lower bound).** Symmetrically, LB's geometric marks make Φ ≥
   2^n/D and no XY cut can drop Φ below 2^n/D (subinvariant under XY moves). The two
   inequalities meet at c(n): complementary slackness ⇔ the threshold-indifference
   observed numerically (XY indifferent between cutting the c(n)-piece and leaving it).
   [GAP P3b]

5. **Assemble / verify.** Φ pins the value at 2^n/D from both sides ⇒ c(n)=2^n/(2^{n+1}−1).
   Cross-check Φ on the exact n=1,2,3 positions from the explorer reports.

## Key lemmas (claim + mechanism)

- **Value-certifying potential (P2).** There is a function Φ of (sorted pieces, remaining
  marks) with Φ(start)=c(n), Φ nonincreasing under XY's optimal cut and nondecreasing
  under LB's optimal cut, and Φ(terminal)=odd-sum. Because the game is finite zero-sum
  with perfect information, such a value function exists (backward induction); the content
  is its CLOSED FORM on the dyadic ladder. Mechanism guess: Φ = (1/D)·Σ 2^{ρ(i)} over a
  matching ρ of LB-claimable slots to ladder rungs.
- **Dyadic redistribution identity (P3).** Cutting the top piece of a dyadic-ladder
  configuration moves weight down one rung, and the map value ↦ new value is the Möbius
  map v ↦ 2v/(2v+1) whose fixed iterate is 2^n/D. This is the same identity the induction
  approach uses, here read as a monovariant step rather than a recursion.
- **Complementary slackness / threshold indifference.** At the optimum XY is indifferent
  between cutting the size-c(n) piece and not; this equality is the dual certificate that
  the two monovariant bounds coincide.

## Open gaps
- **P2**: exhibit the explicit Φ (the matching/weighting closed form). Highest-risk step;
  if no clean Φ exists this framing collapses to backward induction with no shortcut.
- **P3a / P3b**: prove Φ is a super/sub-invariant under the two players' moves.
- Shared **G1**.

## Cases to cover
- Verify Φ reproduces exact values at n=1,2,3 (falsification test BEFORE investing).
- Moves that cut a non-top piece (must still respect the monovariant).

## Watch out for
- Risk of vacuity: "the value function exists by backward induction" is true but useless
  without the closed form. The whole worth of this approach is P2 being explicit; if P2
  stays abstract, prefer approaches 1/2. Run the n=1,2,3 falsification check first.
- Do not conflate weight on pieces with lengths; the potential must reduce to actual
  odd-sum at terminals or it certifies nothing.

## Current best
Framing and the dyadic redistribution identity are in hand (shared with induction-
recursion). The certifying potential Φ (P2) is conjectural; this approach earns its keep
only if the explicit Φ passes the n≤3 check.
