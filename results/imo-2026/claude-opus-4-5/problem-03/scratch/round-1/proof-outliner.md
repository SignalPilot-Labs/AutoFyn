## imo-2026-03

geometric-direct: new
Target: Prove c(n) = 2^n / (2^{n+1} - 1) for all positive integers n
Technique: Explicit geometric construction (pieces in ratio 1:2:4:...:2^n) plus direct case analysis on XY's mark placement
Skeleton:
  1. Define LB's geometric strategy: marks at (2^k-1)/D for k=1,...,n where D=2^{n+1}-1 -- by construction
  2. Define XY's optimal counter: n-1 marks inside largest piece creating paired configuration -- by construction
  3. Prove greedy picking is optimal for both players -- by exchange argument
  4. Prove upper bound: XY's (n-1)-mark strategy gives LB exactly c(n) -- by explicit computation of alternating sum
  5. Prove lower bound Case A: XY marks outside L_n only --> LB picks L_n >= c(n) -- by geometric dominance
  6. Prove lower bound Case B: XY marks inside L_n --> LB still >= c(n) -- by case analysis (GAP)
  7. Prove upper bound for arbitrary LB: XY can limit any LB strategy to <= c(n) -- by XY's equalizing response (GAP)
Key lemmas (claim + the one-line mechanism that makes it true):
  - Greedy is optimal -- because swapping a smaller pick with a larger one the opponent would take increases the total
  - Geometric dominance (crux aimo-0117) -- because 2^n > 2^{n-1} + ... + 1 = 2^n - 1, the largest piece exceeds all others combined
  - XY's odd-piece penalty -- because with 2n+1 pieces LB picks n+1 vs n, gaining an extra piece
Open gaps: Lower bound Case B (XY marks inside L_n); Upper bound for arbitrary LB strategies
Cases to cover: XY's j marks inside L_n for j=0,1,...,n; LB's m marks for m=1,...,n
Watch out for: Sorted order changes with XY's mark placement; alternating sum is sensitive to exact piece sizes

induction-on-n: new
Target: Prove c(n) = 2^n / (2^{n+1} - 1) for all positive integers n
Technique: Strong induction on n using the recurrence 1/c(n) = 2 - 2^{-n}
Skeleton:
  1. Base case n=1: LB at 1/3, prove LB gets exactly 2/3 against all XY responses -- by exhaustive case analysis (done)
  2. Inductive hypothesis: assume c(k) = 2^k/(2^{k+1}-1) for all k < n
  3. Show LB's n-mark geometric strategy relates to the (n-1)-problem via scaling -- by algebraic identity
  4. Prove lower bound: LB >= c(n) by reducing XY's attack on L_n to the (n-1)-subproblem -- by induction
  5. Prove upper bound: XY can achieve <= c(n) against any LB by inductive argument -- by induction
Key lemmas (claim + the one-line mechanism that makes it true):
  - Recurrence: 1/c(n) = 2 - 2^{-n} -- because D/2^n = (2^{n+1}-1)/2^n = 2 - 2^{-n}
  - Scaling lemma -- because pieces {1,2,...,2^{n-1}}/D rescale to the (n-1)-geometric configuration
  - Base case c(1)=2/3 -- because explicit case analysis on XY's single mark proves LB always gets 2/3
Open gaps: Rigorous inductive step (both lower and upper bound directions)
Cases to cover: Base case n=1 (done); inductive step with j marks by XY inside L_n
Watch out for: The scaling between n and n-1 is not exact; pick order after XY marks is subtle

piece-count-parity: new
Target: Prove c(n) = 2^n / (2^{n+1} - 1) for all positive integers n
Technique: Parity analysis of total piece count to explain XY's optimal mark count (n-1)
Skeleton:
  1. Analyze piece count: m marks total --> m+1 pieces --> LB picks ceil((m+1)/2), XY picks floor((m+1)/2) -- by alternating picks
  2. Show XY prefers even piece count (m+1 even) to avoid giving LB an extra pick -- by parity argument
  3. Show LB should use all n marks to prevent XY from over-equalizing -- by counterexample (LB with k<n marks gets < c(n))
  4. Derive XY's optimal: n-1 marks, creating 2n pieces -- by combining parity preference with mark constraint
  5. Compute LB's value for the optimal configuration -- by explicit alternating sum
  6. Prove lower bound: all other XY responses give LB >= c(n) -- by case analysis
  7. Prove upper bound: all LB strategies get <= c(n) -- by XY's adaptive equalization (GAP)
Key lemmas (claim + the one-line mechanism that makes it true):
  - Parity principle -- because with 2n+1 pieces LB picks n+1 vs XY's n, a 1-pick advantage
  - LB uses all n marks -- because using k<n marks allows XY to create equal pieces giving LB only 1/2
  - Geometric configuration is optimal for LB -- because it maximizes the gap XY must close (GAP)
Open gaps: Upper bound for arbitrary LB strategies; exact alternating sum calculation
Cases to cover: XY uses j=0,1,...,n marks; LB uses m=1,...,n marks
Watch out for: Parity argument alone doesn't prove the exact value c(n); need to combine with value calculation

minimax-value: new
Target: Prove c(n) = 2^n / (2^{n+1} - 1) for all positive integers n
Technique: Game-theoretic minimax formulation; value function on piece configurations
Skeleton:
  1. Formalize as two-player zero-sum game: LB marks -> XY responds -> greedy picks -> payoff = LB's total -- by game theory
  2. Simplify picking phase: V(pieces) = sum of odd-indexed pieces in sorted order -- by greedy optimality
  3. Define W(LB's pieces) = min over XY responses of V(refined pieces) -- by definition
  4. Compute W(geometric) = c(n) by analyzing XY's best response -- by case analysis (GAP)
  5. Show W(any LB config) <= c(n) by showing XY can always achieve c(n) -- by adaptive XY strategy (GAP)
  6. Conclude c(n) is the minimax value and geometric strategies are the saddle point -- by minimax theorem
Key lemmas (claim + the one-line mechanism that makes it true):
  - Greedy optimality (V formula) -- because deviating from largest-first loses a larger piece to opponent
  - XY's refine operation -- because XY can only subdivide pieces, not merge or move them
  - Saddle point existence -- because strategy spaces are compact and payoff is continuous
Open gaps: Compute W(geometric) = c(n); prove W(any LB) <= c(n); verify saddle point
Cases to cover: All XY responses to geometric LB; all LB strategies
Watch out for: Minimax theorem gives existence but not the explicit value; need constructions
