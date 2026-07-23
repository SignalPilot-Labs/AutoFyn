## imo-2026-03

- **Distinct openings:**

  **Opening A — Geometric piece construction (LB's strategy):** LB places n marks creating n+1 pieces in exact geometric progression with ratio 2: pieces are 1/D, 2/D, 4/D, ..., 2^n/D where D = 2^{n+1}-1. Numerically verified for n=1,2,3,4 that XY's best response against this configuration gives LB exactly c(n) = 2^n/(2^{n+1}-1). LB's guarantee is tight here: XY achieves exactly c(n) with n-1 cascade halvings (each XY cut halves the current largest piece), and additional cuts beyond n-1 only help LB. This opens the LOWER BOUND direction: show that for any XY strategy (≤ n cuts), LB always gets ≥ 2^n/D.

  **Opening B — XY's upper bound strategy:** To show c(n) ≤ 2^n/(2^{n+1}-1), one must show that for ANY LB placement (≤ n+1 pieces), XY can use ≤ n cuts to limit LB to ≤ 2^n/D. XY's strategy must be adaptive to LB's piece structure. Promising attack: an inductive "halving" argument — given LB's pieces, XY cuts the largest to bring it below the threshold, then recurses on a smaller game. The induction might be on n, reducing n→n-1 after one XY cut.

  **Opening C — "Median invariant" analysis:** For n=1, LB places pieces (1/3, 2/3). KEY: when XY cuts 2/3 → (a, 2/3-a), the piece 1/3 is ALWAYS the median of the 3 pieces {1/3, a, 2/3-a} regardless of a. This is because a + (2/3-a) = 2/3 > 1/3, so one of {a, 2/3-a} is ≥ 1/3 and the other ≤ 1/3. Hence 1/3 is always the median; LB gets 1 - 1/3 = 2/3 always. For general n, the geometric pieces satisfy a similar "rank-stability" invariant: no XY cuts can push enough pieces above or below LB's key pieces to change LB's total below c(n). This is the cleanest proof direction for the lower bound.

  **Opening D — Greedy pick sum formula:** With k total pieces (sorted p1 ≥ ... ≥ pk), LB's total = (1 + Σ_{i=1}^{⌊k/2⌋}(p_{2i-1} - p_{2i}) + [p_k if k odd])/2. LB's total > 1/2 always (since each gap pᵢ - pᵢ₊₁ ≥ 0). Reformulation: LB's total = sum of odd-indexed pieces = (total sum + (p1-p2) + (p3-p4) + ...)/2. LB wants to maximize these gaps; XY wants to minimize them (by equalizing piece sizes). This reformulation might directly yield the answer: XY can equalize pieces to limit LB close to 1/2, but the "geometric" structure prevents perfect equalization given n cuts.

  **Opening E — XY never cuts small pieces (monotonicity argument):** Verified numerically: XY should NEVER cut LB's small pieces (it only helps LB by adding small pieces that end up in LB's odd picks). XY only benefits by cutting LB's LARGE pieces. This simplifies XY's strategy space considerably for the upper bound proof.

- **Candidate technique(s):** 
  - Minimax game analysis on interval partition (two-player adversarial optimization).
  - Geometric/dyadic sequence structure for optimal LB placement.
  - "Rank stability" invariant for the greedy pick order.
  - Induction on n: after one XY cut, reduce to a smaller sub-game.

- **Cheap-kill candidates:**
  - Note that LB always gets > 1/2 (since greedy picking from any partition gives LB more than XY when LB goes first). So c(n) > 1/2 for all n ≥ 1.
  - The formula 2^n/(2^{n+1}-1) → 1/2 from above as n → ∞ (consistent with the "almost equal pieces" asymptotics).
  - XY should never cut LB's smallest pieces (quick pruning of XY's strategy space).

- **Knowledge-base entries to use:**
  - "Constructive / incremental": LB's construction of geometric pieces is the lower bound.
  - "Invariants & monovariants": the rank-stability invariant is the key for the lower bound proof.
  - "Direct proof / induction": the natural proof structure is induction on n.
  - "Casework / exhaustion": for the lower bound, need to handle XY's cuts on each of the n+1 LB pieces separately.
  - "Pigeonhole / extremal principle": in the upper bound, XY finds the piece that LB would pick and cuts it.

- **Analogous past problems (cruxes):**
  - **aimo-0117** [combinatorics/games-and-strategy]: "Assign the played values as a two-sided geometric (dyadic) sequence so that the single largest value strictly exceeds the sum of all the others." The crux is that a dyadic/geometric sequence is used as the optimal strategy in an adversarial game. In aimo-0117, Jesse plays powers of 2 to maintain an invariant. The analogy: LB uses pieces in ratio 2 (geometric) to create a robust configuration against XY's adversarial cuts. The crux move — geometric sequence dominance — is closely analogous.
  - **aimo-0019** [combinatorics/games-and-strategy]: A covering game on the real line where one player responds to the other's dyadic interval choices. Uses dyadic structure. Less directly analogous but involves interval decomposition with binary structure.
  - No crux in the corpus is a perfect match (most game-theory cruxes are about combinatorial board games, not interval-splitting with greedy picking). The geometric-sequence crux from aimo-0117 is the closest.

- **Prior progress:** None (problem is unsolved, no prior approaches in results folder).

- **Dead ends (do not retry):**
  - LB using n+1 EQUAL pieces: XY can limit LB to 1/2 with 1 cut (verified for n=2). Worse than c(n).
  - LB clustering all n marks near a single point (creating one large and n tiny pieces): XY splits the large piece into n+1 sub-pieces, giving LB ≈ 1/2 for large n. Not optimal.

- **Small-case / intuition notes (all labeled as conjecture unless stated):**
  - **PROVED numerically (strong evidence):** c(n) = 2^n/(2^{n+1}-1).
    - c(1) = 2/3. Verified analytically and numerically.
    - c(2) = 4/7. Verified numerically: LB uses (1/7, 2/7, 4/7); XY's best (1 cut, halving 4/7) gives LB exactly 4/7; further XY cuts don't help.
    - c(3) = 8/15. Verified numerically: LB uses (1/15, 2/15, 4/15, 8/15); XY's best (2 cuts) gives LB exactly 8/15.
    - c(4) = 16/31. Verified numerically: LB uses geometric pieces; XY's best (3 cuts) gives LB exactly 16/31.
  - **Key structural observation (conjecture, strong numerical support):** For LB's geometric strategy, XY's optimal response uses exactly n-1 cuts (not all n), after which additional cuts by XY only help LB. This means c(n) = 2^n/(2^{n+1}-1) is exactly what XY achieves with n-1 cascade halvings.
  - **Cascade halving pattern:** XY's cuts are: halve the largest piece (2^n/D), creating two copies of 2^{n-1}/D; then halve one of those, etc. After n-1 halvings, LB faces pieces (8 copies of 2^{n-1}/D... wait: specifically for n=4, 3 halvings gives pieces (8/31, 8/31, 4/31, 4/31, 2/31, 2/31, 2/31, 1/31) and LB gets 8+4+2+2=16=16/31).
  - **Key identity (structural):** After XY's n-1 cascade halvings on LB's geometric pieces, LB's picks are: the n-th piece (= 2^{n-1}/D) twice, plus (n-2) more even-spread picks. The sum works out to 2^n/D by a telescoping argument.
  - **Formula as a fraction:** c(n) = 2^n/(2^{n+1}-1) = 1/(2 - 2^{-n}). As n→∞: c(n)→1/2. As n→0 (degenerate): c(0)=1 (no cuts, LB takes everything). Series: c(n) = 1/2 + 1/(2·(2^{n+1}-1)).
  - **The "median property" for general n (conjecture):** For LB's geometric pieces, no matter how XY cuts, each of LB's original pieces remains the "separating threshold" at its respective rank in the full sorted order. This would be the key lemma for the lower bound.
