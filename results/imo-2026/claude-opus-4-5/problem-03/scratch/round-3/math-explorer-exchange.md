## imo-2026-03

### Exchange / Variational Lens Report

**Status going in:** Answer c(n) = 2^n/(2^{n+1}-1) verified. Lower bound proved. Upper bound gap: Lemma 5 in induction-on-n is FALSE.

---

### Distinct openings

**Opening 1 — Two-case induction: halve vs clone (PARTIALLY COMPLETE)**

The key observation: for n+1 pieces p_1 ≤ ... ≤ p_{n+1} summing to 1 with n XY marks, split on p_{n+1}:

- **Case A (p_{n+1} ≥ c(n)):** XY halves p_{n+1} (1 mark). Residual: n pieces p_1,...,p_n summing to S' = 1-p_{n+1} ≤ (2^n-1)/(2^{n+1}-1). By IH (Q_S(n-1)): A' ≤ S'·t_{n-1}. Then A' ≤ (2^n-1)/(2^{n+1}-1) · 1/(2^n-1) = 1/(2^{n+1}-1) = t_n. ✓ COMPLETE.

- **Case B (p_{n+1} < c(n), first Pigeonhole index = n+1):** All p_j > 2^{j-1}t_n. In particular p_n > 2^{n-1}t_n = c(n)/2, and p_{n+1} ≤ c(n) = 2·c(n)/2 < 2p_n. So p_{n+1} < 2p_n (ALWAYS holds in this case). XY clones p_n inside p_{n+1} (1 mark): creates pair (p_n, p_n) which cancels, and remainder r = p_{n+1}-p_n < p_n. Residual: n pieces {p_1,...,p_{n-1}, r} summing to S'' = 1-2p_n < 1-2·c(n)/2 = (2^n-1)/(2^{n+1}-1). By IH: A'' ≤ S''·t_{n-1} < t_n. ✓ COMPLETE for this sub-case.

**The ALGEBRAIC IDENTITY that makes both cases work:** t_n/t_{n-1} = (2^n-1)/(2^{n+1}-1). In Case A: 1-p_{n+1} ≤ (2^n-1)/(2^{n+1}-1) because p_{n+1} ≥ c(n). In Case B: 1-2p_n < (2^n-1)/(2^{n+1}-1) because p_n > c(n)/2. Both are TIGHT at the boundary: the geometric marking achieves equality.

**The gap:** Case B requires that the Pigeonhole first index k = n+1. If some k ≤ n has p_k ≤ 2^{k-1}t_n, XY may not be able to clone p_n (since p_n might be ≤ c(n)/2).

---

**Opening 2 — Pigeonhole case split with INTERLEAVING (gaps identified)**

Pigeonhole lemma: ∃ first k ∈ {1,...,n+1} with p_k ≤ 2^{k-1}t_n. For each k:

- k=1: XY halves p_2,...,p_{n+1} (n marks). Pair-cancellation gives A = p_1 ≤ t_n. ✓ COMPLETE.
- k=2: XY halves p_3,...,p_{n+1} (n-1 marks). Singletons p_1 ≤ p_2 at bottom. A = p_2-p_1 < 2t_n-t_n = t_n. ✓ COMPLETE. (1 mark unused.)
- k=n+1: This is Case B of Opening 1. Clone p_n, IH on residual. ✓ COMPLETE.
- **k=3,...,n: OPEN.** 

For k=3,...,n, XY could: use k-1 marks inside p_k to "interleave" sub-pieces with p_1,...,p_{k-1}, and use n-k halving marks on p_{k+1},...,p_{n+1}. If XY creates sub-pieces a_1,...,a_k from p_k that interleave as a_k > p_{k-1} > a_{k-1} > ... > p_1 > a_1, then LB takes all a_j and XY takes all p_j (j<k). A = p_k - S_{k-1} where S_{k-1} = p_1+...+p_{k-1}. Since p_k ≤ 2^{k-1}t_n and S_{k-1} > (2^{k-1}-1)t_n, we get A < t_n. ✓

**Feasibility issue:** The strict interleaving a_k > p_{k-1} > ... > p_1 > a_1 with sum p_k requires p_k > S_{k-1}. When p_k ≤ S_{k-1}: A = p_k - S_{k-1} ≤ 0 ≤ t_n (the bound is trivially satisfied!), but XY can't implement the STRICT alternating order. However, in this case XY just needs A ≤ t_n, not necessarily = p_k - S_{k-1}. 

**Key claim (unverified in full generality, verified computationally):** When p_k ≤ S_{k-1}, XY can still achieve A ≤ t_n by placing marks anywhere in p_k (not needing strict interleaving). The pieces of p_k will all land at or below p_1 in sorted order, and XY controls which positions they occupy.

---

**Opening 3 — DOUBLE PAIR creation (numerically verified, not fully formalized)**

For intermediate k cases, XY's optimal strategy (from grid search) creates TWO pairs:
1. Clone a piece from one LB interval inside another LB interval.
2. Halve one LB piece.

Example (n=3, pieces 2/15, 3/15, 4/15, 6/15, case k=3, p_4<c(3)):
- XY mark in piece 1 at 1/60: creates (1/60, 7/60) from piece [0, 2/15].
- XY mark in piece 2 at 7/30: halves piece [2/15, 1/3] into (1/10, 1/10). **PAIR 1**.
- XY mark in piece 4 at 43/60: creates (7/60, 17/60) from piece [3/5, 1]. The 7/60 from piece 4 MATCHES the 7/60 from piece 1. **PAIR 2**.

After both pairs cancel: residual {1/60, 16/60, 17/60}. A = 17-16+1 = 2/60 = 1/30 < 1/15 = t_3. ✓

This "double pair" strategy is the exchange argument in action: XY exploits non-geometric ratios to create multiple canceling pairs.

---

**Opening 4 — The INTERLEAVING SUFFICIENCY claim (most promising for closing the gap)**

For case k (3 ≤ k ≤ n), XY uses:
- k-1 marks inside p_k → k sub-pieces.
- n-k marks halving p_{k+1},...,p_{n+1} → n-k pairs.
- Total marks: n-1. One mark spare.

After these moves, A_interleave = p_k - S_{k-1}.

**Key identity to prove:** A = p_k - S_{k-1} regardless of where the k sub-pieces of p_k land in the sorted order — as long as the n-k pairs remain adjacent (they always do since equal halves are consecutive).

This holds when the k sub-pieces of p_k are chosen to interleave with p_1,...,p_{k-1} (placing exactly one a_j between each p_{j-1} and p_j). When p_k < S_{k-1}: the strict interleaving is infeasible, but XY can still achieve A < t_n because A = p_k - S_{k-1} < 0 if the interleaving WERE implementable, and any sub-optimal placement only increases A_interleave above p_k - S_{k-1} but may stay below t_n.

**The CRUCIAL gap for the outliner to fill:** Does there always exist a placement of k sub-pieces of p_k (summing to p_k) such that A ≤ t_n? When p_k ≤ S_{k-1}: need A ≤ t_n via some placement. When p_k > S_{k-1}: the standard interleaving gives A = p_k - S_{k-1} < t_n.

---

### Candidate technique(s)

- **Pair-cancellation + induction:** pairs of equal elements at consecutive positions contribute 0 to A; reducing to residual sub-problems.
- **Exchange argument / saddle-point:** geometric marking is the unique saddle point; any deviation gives XY a strictly better pair-creation opportunity.
- **Pigeonhole on 2^{k-1} thresholds:** the first k where p_k ≤ 2^{k-1}t_n determines XY's strategy type.

### Cheap-kill candidates

- **Cases k=1 and k=2:** already complete proofs. No additional work needed.
- **Cases k=1, k=2, k=n+1:** all three complete. The only gap is k=3,...,n.
- **Parity check:** total pieces after XY's moves = 2n+1 (odd), so singleton lands at position 2n+1 (odd = LB). This is the basis for pair-cancellation giving A = singleton.

### Knowledge-base entries to use

- **Pair-cancellation lemma** (proved in geometric-dominance): equal pairs contribute 0 to alternating sum regardless of position.
- **Minimax theorem** (von Neumann): guarantees saddle point existence; useful to frame the result.
- **Pigeonhole lemma** (proved in geometric-dominance): for n+1 pieces summing to 1, ∃k with p_k ≤ 2^{k-1}t_n.
- **Greedy Optimality Lemma** (proved in geometric-dominance, induction-on-n): both players taking the largest available piece is optimal.

### Analogous past problems (cruxes)

None found in the crux corpus with directly analogous structure (stick-splitting + alternating greedy claim). The problem is genuinely novel in combining: (a) both players marking, (b) greedy claiming, (c) optimal marking strategy.

### Prior progress

- Lower bound: COMPLETE. LB's geometric marking achieves exactly c(n) against XY's copy strategy.
- Upper bound: Cases k=1, k=2, k=n+1 COMPLETE. Cases k=3,...,n OPEN.
- Lemma 5 (induction-on-n) is FALSE: "p_1 ≤ t_n OR p_{n+1} ≤ c(n)" is false — both can fail simultaneously.
- The FALSE Lemma 5 was trying to reduce ALL cases to k=1 or k=n+1. The actual Pigeonhole gives more cases.

### Dead ends (do not retry)

- **Lemma 5 (pigeonhole bound):** FALSE. The claim "for n+1 pieces summing to 1, either p_1 ≤ t_n or p_{n+1} ≤ c(n)" has counterexamples (e.g., pieces [107/700, 93/350, 407/700] for n=2). Do NOT retry.
- **"Halve n largest pieces" as universal strategy:** FAILS for non-geometric markings. For equal pieces, XY's optimal uses different placements.
- **Naive halve-then-IH for k=3,...,n:** halving p_{k+1},...,p_{n+1} and applying IH to k singletons gives IH bound S_k·t_{k-1} which can exceed t_n. FAILS.

### Small-case / intuition notes (labeled conjectures)

- **VERIFIED:** For k=3,...,n cases, XY CAN always achieve A ≤ t_n (verified by grid search for n=3 over 60^3 strategies).
- **CONJECTURE:** The interleaving A = p_k - S_{k-1} < t_n (since p_k ≤ 2^{k-1}t_n and S_{k-1} > (2^{k-1}-1)t_n) can ALWAYS be achieved when p_k > S_{k-1}, and when p_k ≤ S_{k-1}: A < 0 automatically with any placement strategy + the halving marks. This conjecture, if true, CLOSES the gap.
- **KEY OBSERVATION (algebraic, not yet proved fully):** The condition p_k > S_{k-1} (strict interleaving feasible) is equivalent to A_interleave > 0. When this fails, A_interleave < 0 ≤ t_n, but XY needs to verify a placement achieving A ≤ t_n exists. For k=2: the condition p_2 > p_1 always holds (pieces are sorted), and the 2-piece interleaving is trivial (just split p_2 into pieces above and below p_1).

### What the outliner should focus on

**The single most promising route:** Fill the gap for k=3,...,n using the interleaving argument with the following claim: "XY uses k-1 marks inside p_k and n-k halving marks. The resulting A = p_k - S_{k-1} < t_n." The key proof obligation is to show XY can ACHIEVE A = p_k - S_{k-1} via some placement (or show A ≤ t_n with any placement).

For this, the sub-problem reduces to: given k pieces summing to p_k and k-1 XY marks, show XY can achieve alternating sum ≤ p_k - S_{k-1} (which is the target since S_{k-1} = the sum of the "partner" singletons XY takes).

This is essentially: XY splits p_k to TAKE ALL the split pieces while LB takes p_1,...,p_{k-1}. This is the "sandwich" strategy within p_k, giving A = p_k - S_{k-1} < t_n.

The sandwich within p_k requires: p_k > S_{k-1} for strict interleaving. When p_k ≤ S_{k-1}: A = p_k - S_{k-1} ≤ 0, but XY needs a valid placement. One valid placement: XY puts all k-1 marks in p_k as equal divisions. Then the k equal pieces from p_k are all at the BOTTOM of the sorted order (below p_1), and XY uses the n-k halving marks to create pairs at the top. The alternating sum of the bottom cluster depends on parity, but XY can use the 1 spare mark to correct this.

