## imo-2026-03

geometric-direct: revise
Target: Prove c(n) = 2^n / (2^{n+1} - 1) for all positive integers n.
Technique: Case analysis (LB config structure) + Singleton-Pair strategies + Pigeonhole bound
Skeleton:
  1. Lower Bound (PROVED): LB's geometric config [L_0, ..., L_n] achieves c(n). — by strong induction, Geometric Dominance Lemma
  2. Upper Bound Case A (P_1 <= L_0): XY halves P_2, ..., P_{n+1}. LB = 1/2 + P_1/2 <= c(n). — by Halve-All Strategy, Pairing Cancellation
  3. Upper Bound Case B Large (P_{n+1} >= c(n)): XY halves P_{n+1} and applies (n-1)-IH. — by Halve+IH Lemma, identity c(n-1)(1-c(n)) = c(n)/2
  4. Upper Bound Case B Small (P_1 > L_0 AND P_{n+1} < c(n)):
     4a. If any d_j <= L_0: V_j strategy (halve all except {P_j, P_{j+1}}). LB = 1/2 + d_j/2 <= c(n). — by Singleton-Pair Formula
     4b. If ALL d_j > L_0: Pairwise strategies guaranteed by Pigeonhole. — by NEW n=4 Pigeonhole Lemma
  5. Combine cases: XY always limits LB to <= c(n). — by exhaustive case coverage
Key lemmas (claim + the one-line mechanism that makes it true):
  - V_j Strategy Lemma: XY halves all pieces except {P_j, P_{j+1}} (n-1 marks). LB = 1/2 + d_j/2 <= c(n) when d_j <= L_0. — because Pairing Cancellation applied (n-1) times gives LB = (total of halved pieces)/2 + max(P_j, P_{j+1}) = 1/2 + d_j/2
  - n=4 Pigeonhole Lemma (NEW): In B_small (P_5 < c(4)) with all d_j > L_0, SOME pairwise difference among {alpha, beta, gamma, eta, sigma} is <= 1. — because if all pairwise > 1, then after sorting the 5 shifted params have gaps > 1, forcing weighted sum > 20 > 16, contradicting the weighted sum = 16 constraint
  - Pairwise Strategy Lemma: For any two shifted params with difference <= 1, XY creates singletons with difference <= L_0, giving LB <= c(n). — because Singleton-Pair Formula: LB = 1/2 + |s_2 - s_1|/2 <= 1/2 + L_0/2 = c(n)
Open gaps:
  - Extend Pigeonhole argument to n=5: need weighted sum = 42 vs. minimum weighted sum with all pairwise > 1 (should be > 42 as well)
  - Complete algebraic proof for n=5 B_small (currently 99.5%+ computational coverage)
Cases to cover:
  - n=4: V_1, V_2, V_3, V_4 (d_j <= L_0) + 10 pairwise strategies (all d_j > L_0)
  - n=5: V_1, ..., V_5 + pairwise strategies + 5-mark strategies for "all pairwise > 1" sub-region (if non-empty)
Watch out for:
  - The current proof file has WRONG sum constraint direction in "Case B for n=4" section. The text says "4alpha+3beta+2gamma+eta < 5" but this is B_LARGE not B_SMALL. FIX: rewrite to use the correct constraint 5alpha+4beta+3gamma+2eta+sigma = 16 and replace S6/S4/S5/BPP coverage argument with the Pigeonhole lemma.
  - V_j strategies use (n-1) marks, not n marks. For n=4: V_j uses 3 marks.

---

n5-five-mark: new
Target: Prove c(5) = 32/63 by V_j + Pairwise + 5-mark strategies
Technique: V_j strategies + 15 pairwise strategies + 3 five-mark strategies (A, E, F) for bounded "all pairwise > 1" sub-region
Skeleton:
  1. V_j strategies handle any d_j <= L_0 (any shifted param <= 0). — by V_j Strategy Lemma
  2. In "all d_j > L_0" sub-case: the 6 shifted params {alpha, beta, gamma, delta, epsilon, zeta} satisfy weighted sum = 42 and all > 0. — by sum constraint
  3. If SOME pairwise difference <= 1, the corresponding pairwise strategy works. — by Pairwise Strategy Lemma
  4. If ALL pairwise > 1: the sorted params have gap g > 1 between consecutive values. The constraint 21*x_{(1)} + 35*g = 42 forces g in (1, 1.2) and x_{(1)} in (0, 1/3). — by weighted sum identity
  5. In this bounded region, Strategy A (condition |delta - 2 - 2*alpha - beta| <= 1) covers most configs. — by direct computation (explorer verified)
  6. Strategies E and F cover the remainder. — by direct computation (explorer verified)
  7. Three-strategy sub-claim: In "all pairwise > 1" sub-region, at least one of {A, E, F} works. — by case analysis or LP verification
Key lemmas (claim + the one-line mechanism that makes it true):
  - Pigeonhole FAILS for n=5: min_weighted = 35 < 42, so "all pairwise > 1" sub-region is non-empty. — because 6*0 + 5*1 + 4*2 + 3*3 + 2*4 + 1*5 = 35 < 42
  - Bounded sub-region: In "all pairwise > 1", gap g in (1, 1.2), x_{(1)} = (42-35g)/21 in (0, 1/3). Unweighted = 12 + 5g in (17, 18). — by solving 21*x_{(1)} + 35*g = 42 with g > 1, x_{(1)} > 0
  - Strategy A: XY cuts P_4 at P_3, cuts d_3 at P_2, cuts (d_3-P_2) at P_1, halves P_5, halves d_5. Creates 5 pairs + 1 singleton (d_3-P_2-P_1). LB = 1/2 + |d_3-P_2-P_1|/2 <= c(5) when |delta - 2 - 2*alpha - beta| <= 1. — by Singleton-Pair Formula
  - Three-strategy coverage (TO PROVE): In the bounded "all pairwise > 1" region, at least one of {Strategy A, E, F} has condition <= 1. — by case analysis on the assignment of sorted values to params
Open gaps:
  - Prove the three-strategy sub-claim algebraically (currently verified computationally with 100k samples, 0 failures)
Cases to cover:
  - V_1, ..., V_5 (each shifted param <= 0)
  - 15 pairwise strategies (C(6,2) = 15 pairs)
  - Strategies A, E, F for "all pairwise > 1" sub-region
Watch out for:
  - The "all pairwise > 1" sub-region is non-empty but bounded: gap g in (1, 1.2).
  - Strategy A construction uses 5 marks (not 4). Verify mark count.
  - The three-strategy sub-claim is the key gap to close algebraically.

---

geometric-direct-advance: advance
Target: Prove c(n) = 2^n / (2^{n+1} - 1) for all positive integers n.
Technique: Extend V_j + Pigeonhole to general n
Skeleton:
  1. PROVED: Lower bound (all n), Case A (all n), Case B Large (all n >= 2), Case B Small for n=1,2,3.
  2. n=4 Case B Small: V_j + Pigeonhole (NEW in Round 11). — by n=4 Pigeonhole Lemma
  3. n=5 Case B Small: V_j + Pigeonhole (or V_j + Pairwise + 5-mark). — by n=5 analysis
  4. n >= 6: Conjecture Pigeonhole extends (weighted sum = n(n+1)(n+2)/6, minimum with all pairwise > 1 should exceed this). — by generalized Pigeonhole
Open gaps:
  - Complete n=5 proof (either via Pigeonhole or via 5-mark strategy coverage)
  - Generalize to n >= 6 (formula for minimum weighted sum with m params and all pairwise > 1)
Cases to cover: n=4 (close this round), n=5 (close next), n >= 6 (open)
Watch out for:
  - The Pigeonhole argument uses the constraint that weighted sum is EXACTLY n(n+1)(n+2)/6 (verify this formula)
  - Don't assume Pigeonhole always works - for large n, the bound may be too weak and require explicit strategy enumeration

---

direct-counting: new
Target: Prove c(n) = 2^n / (2^{n+1} - 1) by direct counting argument
Technique: Show the total number of independent conditions (n(n+1)/2 pairwise) exceeds the degrees of freedom (n shifted params) forcing some condition to hold
Skeleton:
  1. In B_small "all d_j > L_0", we have n shifted params with one linear constraint (weighted sum = fixed). — by sum constraint
  2. Each pairwise strategy fails when |x_i - x_j| > 1. These are 2-sided linear constraints. — by strategy condition
  3. The intersection of all failure regions forms a polytope. — by linear inequalities
  4. If this polytope is EMPTY, some strategy must work. — by emptiness implies covering
  5. Prove emptiness via LP/volume argument or by bounding the diameter of the polytope. — by LP feasibility
Key lemmas (claim + the one-line mechanism that makes it true):
  - Diameter Bound: If n shifted params all have pairwise > 1, their range (max - min) > n-1, which forces weighted sum > threshold. — because n values with consecutive gaps > 1 span range > n-1
  - LP Infeasibility: The system {all > 0, weighted = W, all pairwise > 1, unweighted < U} is infeasible for W = 16 (n=4), W = 42 (n=5). — by solving the LP
Open gaps:
  - Formalize the LP approach
  - Extend to general n
Cases to cover: Same as geometric-direct
Watch out for:
  - This is an alternative proof technique, may be cleaner than case enumeration for large n
  - The LP approach requires careful handling of strict inequalities (use epsilon perturbation)
