ALWAYS: For game/optimization problems, compute c(n) for small n=1,2,3 numerically before theorizing — the numerical values reveal the correct formula quickly. (Because imo-2026-03 answer 2^n/(2^{n+1}-1) was found numerically before any analytic argument, round 1)

ALWAYS: When searching for XY's optimal response in a continuous game, include points near endpoints (near 0 and near 1) in the search grid — endpoints create tiny pieces that XY can exploit. (round 1)

ALWAYS: For alternating-pick (greedy) games from sorted pieces, note LB always gets >= 1/2 since s1>=s2, s3>=s4, etc. This eliminates c(n)=1/2 as a viable conjecture unless the game allows XY to force exactly 1/2. (round 1)

ALWAYS: When LB/XY have "at most n" moves, check that XY might deliberately use fewer than n moves — XY may achieve the minimum with fewer cuts. (Because for n=2, XY uses 1 cut not 2; for n=3, XY uses 2 cuts not 3, round 1)

NEVER: Assume that "equal pieces" is LB's optimal strategy for piece-dividing games — XY can always bring LB to 1/2 by cutting 1 equal piece. The geometric/dyadic structure is correct. (Because equal pieces gave c(2) ≈ 1/2 but the geometric strategy gives c(2) = 4/7, round 1)

ALWAYS: When running minimax grid searches, use dense grids (n_q≥3000 for XY, n_s≥50 for LB) since coarse grids miss the saddle point for continuous game problems. (Because the 60x60 LB grid missed c(2)=4/7 but 25x25x25 LB grid found c(3)=8/15 at the geometric point, round 1)

NEVER: Trust the analytical result about a game saddle point without verifying XY's FULL response space — key XY strategies may not be at midpoints. (Because XY at 2/3 (not midpoint of A=[1/2,1]) achieves LB=1/2 against pieces (1/6,1/3,1/2), which I initially missed, round 1)
