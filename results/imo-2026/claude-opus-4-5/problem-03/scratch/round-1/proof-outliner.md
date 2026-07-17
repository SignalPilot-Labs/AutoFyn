## imo-2026-03

geometric-dominance: new
Target: Prove c(n) = 2^n / (2^{n+1} - 1) is the largest value LB can guarantee
Technique: Geometric dominance — LB creates pieces in ratio 1:2:4:...:2^n where largest exceeds all others combined; direct case analysis on XY's response
Skeleton:
  1. LB marks at (2^k - 1)/(2^{n+1} - 1) for k=1,...,n creating pieces t, 2t, ..., 2^n t — by construction
  2. Largest piece 2^n t > sum of smaller pieces (2^n - 1)t — by geometric sum
  3. Case A: XY doesn't split largest piece -> LB takes it first, gets >= c(n) — by greedy optimality
  4. Case B: XY splits largest piece -> analyze resulting configuration, show LB >= c(n) — by casework
  5. XY's copy strategy achieves equality c(n) against geometric marking — by explicit calculation
  6. For arbitrary LB marking, XY can limit LB to <= c(n) — by adversarial response
Key lemmas (claim + mechanism):
  - Greedy claiming is optimal — because taking smaller now lets opponent take larger, net loss by exchange
  - Largest piece dominates — because 2^n > 2^{n-1} + ... + 1 = 2^n - 1
  - Case B yields LB >= c(n) — because XY's marks split pieces into sub-pieces that still interleave favorably
Open gaps: Steps 4, 6
Cases to cover: XY uses j marks (j=0,...,n) inside largest piece, n-j elsewhere
Watch out for: Case B needs careful sorted-order analysis; upper bound for non-geometric LB marking is the hard part

induction-on-n: new
Target: Prove c(n) = 2^n / (2^{n+1} - 1) by induction on n
Technique: Strong induction with base n=1; the median-piece argument for base case, reduction to (n-1)-game for step
Skeleton:
  1. Base case n=1: LB at 1/3 creates pieces 1/3, 2/3 — by construction
  2. XY marks at y creates 3 pieces; 1/3 is always median (rank 2) — by interval analysis
  3. LB gets ranks 1 and 3, total 2/3 = c(1) — by sum calculation
  4. Inductive hypothesis: c(n-1) = 2^{n-1}/(2^n - 1)
  5. Observe reciprocal recurrence: 1/c(n) = 1/c(n-1) + 2^{-n} — by algebraic identity
  6. Translate recurrence to game dynamics: after first round, reduced game relates to (n-1) case — by structural argument
  7. Conclude c(n) = 2^n/(2^{n+1} - 1) — by solving recurrence
Key lemmas (claim + mechanism):
  - n=1 median property — because (y-1/3) + (1-y) = 2/3 forces exactly one above and one below 1/3
  - Reciprocal recurrence holds — because f(n) = 2 - 2^{-n} satisfies f(n) - f(n-1) = 2^{-n}
  - Reduction to (n-1)-game — because first-round picks "consume" one effective mark from each player
Open gaps: Steps 5-6 (game-theoretic justification of recurrence)
Cases to cover: n=1 base with all XY positions
Watch out for: The reduction to (n-1)-game is the crux; need to handle how XY's marks are "used up"

pairing-interleave: new
Target: Prove c(n) = 2^n / (2^{n+1} - 1) via dyadic pairing structure
Technique: Interleaving argument — XY's copy strategy creates pairs at each tier; LB claims one from each tier
Skeleton:
  1. LB's geometric marking creates pieces P_k = 2^k t for k=0,...,n — by construction
  2. XY's copy strategy: halve P_n,...,P_2 and split P_1 near P_0 — by explicit mark placement
  3. Result: pairs {P_{k-1}, P_{k-1}} at each tier k=2,...,n, plus {P_1-eps, P_0, eps} — by computation
  4. Sorted order interleaves copies and originals — by size comparison
  5. LB takes odd positions = one from each pair = sum c(n) — by rank calculation
  6. No XY strategy gives LB less — by optimality of copy strategy
  7. For arbitrary LB marking, XY creates similar interleaved structure, limits LB to <= c(n) — by adversarial construction
Key lemmas (claim + mechanism):
  - Copies interleave with originals — because halving P_k gives P_{k-1} which matches existing piece
  - LB's sum = c(n) exactly — because sum of one from each tier = geometric sum = 2^n t
  - Copy strategy is XY-optimal against geometric marking — because it achieves equality
Open gaps: Steps 5-6 (verify calculation), Step 7 (upper bound)
Cases to cover: All possible XY mark distributions against geometric LB marking
Watch out for: The sum calculation in step 5 needs careful verification; dyadic analogy from aimo-0117 guides intuition

---

**Build set recommendation:** geometric-dominance, induction-on-n

**Rationale:** 
- geometric-dominance is the most direct approach matching explorer findings; it needs the Case B casework filled in.
- induction-on-n provides a different angle via recurrence and reduction, potentially cleaner for the upper bound.
- pairing-interleave overlaps with geometric-dominance but frames via the copy strategy; hold as backup if the first two stall.

All three approaches share the same conjectured answer c(n) = 2^n/(2^{n+1}-1) with strong numerical support from explorers. The main gap across all approaches is the upper bound for arbitrary LB marking — geometric-dominance attacks this via case analysis, while induction-on-n may yield a cleaner recurrence-based proof.
