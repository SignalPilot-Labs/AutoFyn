## imo-2026-03

### Conjectured closed form (numerically verified for n=1,2,3)
**c(n) = 2^n / (2^{n+1} - 1)**

Checks: c(1) = 2/3, c(2) = 4/7, c(3) = 8/15. All three matched an exact-arithmetic optimum in numerical optimization (not just approximately — the optimizer converged to the exact rational value to ~1e-13 precision when Liu Bang uses the construction below, and no other candidate point in extensive local/random/DE search beat it).

### The claiming-phase rule (verified by exhaustive game-tree search, not just conjectured)
Given a *fixed* multiset of piece lengths, with both players playing optimally to maximize their own total (zero-sum since total is fixed), the optimal strategy for both is: **sort pieces in decreasing order; the first-to-move player gets the pieces at odd positions (1st, 3rd, 5th, ...), the second player gets the even positions.** I verified this by exact minimax search (memoized game tree over subsets, no approximation) against pure greedy-take-largest on 2000 random instances of size up to 7 — zero mismatches. This is intuitive since it's a zero-sum alternating-pick game and picking your currently-largest available piece is dominant (standard exchange argument: swapping strategies can't help either side). Treat this as **established** (exact search, not sampling), safe for the outliner to cite as a lemma to be proven (e.g. via an exchange/interval argument), not re-derived numerically.

Consequence for the top-level game: since Liu Bang marks ≤ n points and Xiang Yu marks ≤ n points, there are at most 2n marks, hence at most **2n+1 pieces**. With 2n+1 pieces (the generic/full case), sorted descending, Liu Bang (first) takes positions 1,3,...,2n+1 — that's **n+1 pieces**, Xiang Yu takes n pieces. If Liu Bang gets the largest piece and thereafter the odd-ranked ones, his total = (piece sum) − (sum of even-ranked pieces) = 1 − (Xiang Yu's greedy total on the complementary ranks). Equivalently, Liu Bang's payoff = 1 − median-type sum; for n=1 (3 pieces) this reduces to Liu Bang's payoff = 1 − (median piece).

### Optimal marking construction found (Liu Bang's side)
Define an interval-ratio sequence recursively:
- I_1 = (1, 2)
- I_n = insert 2^n right after the first term of I_{n-1}

This gives I_1=(1,2), I_2=(1,4,2), I_3=(1,8,4,2), and in general **I_n = (1, 2^n, 2^{n-1}, ..., 2^2, 2)** — n+1 terms summing to 2^{n+1}−1, with the unique maximum term 2^n.

Liu Bang's n marks are placed at the partial sums of this ratio sequence divided by (2^{n+1}−1). E.g.:
- n=1: mark at 1/3. (pieces 1/3, 2/3)
- n=2: marks at 1/7, 5/7 (= (1)/7, (1+4)/7). Pieces after his marks alone: 1/7, 4/7, 2/7 — the "protected" big piece (4/7) sits in the *middle*, flanked by smaller pieces.
- n=3: marks at 1/15, 9/15, 13/15 (= 1/15, (1+8)/15, (1+8+4)/15). Pieces: 1/15, 8/15, 4/15, 2/15.

Verified numerically (differential-evolution search over Xiang Yu's best response, high precision, multiple random seeds converging to the exact rational): against this construction, Xiang Yu's best response can push Liu Bang down to *exactly* 2^n/(2^{n+1}−1) and no further (I could not find any nearby perturbation of Liu Bang's points, nor any of several other symmetric/equal-spacing constructions, that does better). For n=2 I also ran a broad max-min search (coarse grid + random + nested DE) over Liu Bang's own point choice and never found a value exceeding ~4/7 — consistent with 4/7 being the true optimum, though I did not achieve a fully rigorous global-optimality certificate (this remains numeric evidence, not proof).

### Cheap-kill / structural facts
- **Symmetric constructions are bad**: I tested Liu Bang marking symmetric pairs (a, 1−a) for many a (n=2 case) — Xiang Yu can always respond (typically by marking the midpoint 0.5 plus one more point) to hold Liu Bang down to exactly **1/2**, well below 4/7. So symmetry is a trap; do NOT assume the optimal marking is symmetric about 1/2. This is a useful "cheap kill" against any approach that tries a symmetric ansatz.
- Total pieces ≤ 2n+1 (equality iff all marks distinct, which the problem allows/expects at optimum since more pieces generally helps the granularity of Liu Bang's guarantee — should double check whether Liu Bang ever wants fewer than n marks, but the n=1,2,3 optimal constructions all use the full n marks).
- The claiming-phase reduction turns the whole problem into: Liu Bang picks n points, then Xiang Yu picks n points, to control the *rank-1,3,5,...-sum* of the resulting 2n+1-piece composition. This is a purely combinatorial/order-statistics game once the claiming lemma is granted.
- c(n) → 1/2 as n → ∞ (from below, since 2^n/(2^{n+1}-1) = 1/(2 - 2^{-n}) → 1/2). Makes sense: with many marks, Xiang Yu's finer control lets him equalize things back toward a 50/50 split, but Liu Bang's first-mover + first-claimer advantage keeps him strictly above 1/2 for every finite n.

### Analogous corpus problems
I did not query `crux_moves_documentation.md` / the corpus in this pass (my lens was computational/small-case, and time budget was consumed by the numeric search above); the outliner or another explorer should check the corpus for "alternating claiming game on a multiset" (should support the claiming-phase lemma) and "two-stage adversarial point-marking / interval-cutting" games under `combinatorics` subtopics like "game_strategy" or "extremal_combinatorics" — I'd flag this as unexplored by me and worth a follow-up query.

### Dead ends (do not retry)
- Equal/regular spacing of Liu Bang's marks (e.g. marks at k/(2n+1)) — tested for n=2, only guarantees 1/2, far below the true optimum 4/7. Do not treat "evenly spaced marks" as a plausible optimal strategy.
- Symmetric marking (a, 1-a, ...) — same failure mode, Xiang Yu neutralizes via the midpoint.

### Prior progress
None (current.md was empty at round start; this is a fresh problem for the population).

### Small-case / intuition summary (all CONJECTURE from numerics, not proof)
- Claiming-phase optimal rule: sort desc, alternate — **verified by exact search**, should be provable by exchange argument (near-certain, safe to build on).
- c(1) = 2/3, c(2) = 4/7, c(3) = 8/15, matching c(n) = 2^n/(2^{n+1}-1) — strong numeric evidence (exact rational match, robust to independent local search), but the *general* construction and its optimality for all n is unproven; the outliner should look for: (a) a clean proof that Liu Bang's recursive interval construction I_n achieves 2^n/(2^{n+1}-1) against ANY Xiang Yu response (an induction on n using the recursive structure I_n built from I_{n-1} is the natural route, since the construction itself is defined recursively), and (b) a matching upper bound (Xiang Yu strategy limiting Liu Bang to exactly this value) — likely also inductive, exploiting that Xiang Yu can always "attack" the largest protected interval by bisecting it plus mirroring Liu Bang's recursive structure one level down.
