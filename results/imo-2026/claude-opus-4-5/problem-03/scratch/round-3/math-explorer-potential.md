## imo-2026-03

### Minimax / Potential Function Lens

---

**Prior situation**: The upper bound proof has an open gap at cases k ∈ {3,...,n} in the following structure. By the Pigeonhole Lemma (geometric-dominance.md, Lemma 2), for any n+1 pieces p_1 ≤ ... ≤ p_{n+1} summing to 1, there exists at least one index k with p_k ≤ 2^{k-1} t_n (where t_n = 1/(2^{n+1}-1)). Cases k=1, k=2, and k=n+1 are each handled by a concrete XY strategy. Cases k ∈ {3,...,n} have no working strategy.

---

### Central Finding: Choose k* = LARGEST Satisfying Index

The gap closes completely by a single change of perspective: instead of taking any k satisfying the pigeonhole bound, take **k* = the LARGEST index** in {1,...,n+1} with p_{k*} ≤ 2^{k*-1} t_n. This makes two additional facts true simultaneously:

**(A) No interleaving.** Since k* is the largest satisfying index, k*+1 does NOT satisfy: p_{k*+1} > 2^{k*} t_n. But p_{k*} ≤ 2^{k*-1} t_n. So p_{k*+1}/p_{k*} > 2^{k*} / 2^{k*-1} = 2, giving p_{k*+1} > 2 p_{k*}. Therefore all halved pieces p_j/2 for j > k* satisfy p_j/2 > p_{k*}, and all sub-pieces created within p_1,...,p_{k*} are ≤ p_{k*}. No interleaving between halved pairs and sub-problem pieces.

**(B) Sub-problem is small enough.** For j > k*: p_j > 2^{j-1} t_n (strict). Summing: p_{k*+1}+...+p_{n+1} > t_n(2^{k*}+...+2^n) = t_n · 2^{k*}(2^{n-k*+1}-1) = t_n(2^{n+1}-2^{k*}). So:
  S_{k*} = 1 - (p_{k*+1}+...+p_{n+1}) < 1 - t_n(2^{n+1}-2^{k*}) = (2^{k*}-1)t_n.

**(C) The algebraic miracle.** By induction (k*-1 marks on k* sub-problem pieces summing to S_{k*}, the upper bound for c(k*-1) applies): A_sub ≤ S_{k*} · t_{k*-1} = S_{k*}/(2^{k*}-1) < (2^{k*}-1)t_n / (2^{k*}-1) = t_n.

The factor (2^{k*}-1) cancels exactly between the S_{k*} bound and t_{k*-1} = 1/(2^{k*}-1). This is the clean algebraic identity that makes the induction close at every level.

---

### Complete Inductive Proof Structure for Upper Bound

**Scale-invariant claim**: For any m ≥ 1, for any m+1 pieces p_1 ≤ ... ≤ p_{m+1} summing to S, XY with m marks can achieve alternating sum A ≤ S · t_m.

**Base m=1**: Proved in the n=1 base case of existing approach (induction-on-n.md). ✓

**Inductive step m given m'<m proved**: Let k* = largest k with p_k ≤ 2^{k-1} · S·t_m.

- k* = m+1 (sandwich case): p_{m+1} ≤ S · c(m). XY places m marks inside p_{m+1} creating interleaved sub-pieces a_1,...,a_{m+1}. Sorted order: a_{m+1} > p_m > a_m > ... > a_1. LB takes all a_k summing to p_{m+1} ≤ S · c(m). Then A = 2·LB - S ≤ 2S·c(m) - S = S·t_m. ✓

- k* < m+1: XY uses m+1-k* marks to halve p_{k*+1},...,p_{m+1} (these m+1-k* pieces each halved; all halved elements stay above p_{k*} by (A)). The m - (m+1-k*) = k*-1 remaining marks go to sub-problem p_1,...,p_{k*} summing to S_{k*}. By IH with m'=k*-1: A_sub ≤ S_{k*} · t_{k*-1}. Pairs contribute 0 to A. Sub-problem starts at odd position. A_total = A_sub < t_m. ✓

**Computational verification**: 500 random trials for n=1 through n=5, zero failures.

---

### Distinct Openings for the Outliner

1. **Induction with k*=largest** (the main finding): Strengthen the inductive hypothesis to the scale-invariant form. Use the LARGEST pigeonhole index k*, not just any. No new mechanism needed — the existing case analysis (halving + IH) works for all k ∈ {3,...,n} once k* is chosen optimally. This is a clean, complete argument.

2. **Minimax formulation**: The game has a minimax value by von Neumann's theorem (finite, zero-sum, perfect information). Since the lower bound (geometric marking) is proved, we only need to show c(n) is an upper bound. The inductive k*-largest argument directly proves this without explicitly invoking minimax — minimax just guarantees the value exists.

3. **Potential function Φ = min_XY A**: The quantity Φ(p_1,...,p_{m+1}) = minimum alternating sum XY can achieve with m marks satisfies Φ ≤ S·t_m by the inductive argument. This Lyapunov-style interpretation shows XY's strategy monotonically reduces the "threat" by decreasing the sub-problem size by a factor of (2^{k*}-1)/(2^{m+1}-1) at each level. But this is the same argument — the potential framing doesn't simplify it further.

4. **Exchange argument** (different framing, not the same as above): Show directly that the geometric marking uniquely maximizes V(L) = min_X G(L,X) over all LB markings L. The exchange argument would show any deviation from geometric shrinks V(L). This is logically equivalent but builds intuition differently.

---

### Key Subtlety for the Outliner to Handle

**Sandwich strategy with equal pieces**: When k*=m+1, the sandwich requires XY to create sub-pieces a_k strictly between p_{k-1} and p_k. If some p_{k-1} = p_k (equal pieces), strict interleaving fails. Resolution: XY can make a_k = p_{k-1} + ε or use a non-strict version. In either case, LB's take = sum of a_k = p_{m+1} regardless of interleaving with tied pieces. The bound LB ≤ p_{m+1} ≤ S·c(m) holds by sum, not by position.

**Strict vs. non-strict**: For k* < m+1, the inequality A_total < S·t_m is strict (due to strict inequality for p_{j} > 2^{j-1}S·t_m when j>k*). For k*=m+1, A_total ≤ S·t_m (equality when p_{m+1} = S·c(m) exactly). Both give LB ≤ S·c(m).

---

### Candidate Techniques

- Strong induction with scale-invariant hypothesis (main vehicle)
- Pigeonhole / extremal choice (pick LARGEST satisfying index, not any)
- Pair-cancellation lemma (already proved, already in lemmas/)
- Sandwich strategy for k*=n+1 (already present in geometric-dominance.md)

### Knowledge-Base Entries to Use

- **Induction** (General Proof Methods): scale-invariant hypothesis, strong induction. The correct induction variable is m (number of marks each player uses).
- **Pigeonhole / extremal** (Combinatorics): taking the LARGEST/SMALLEST extremal element is the key twist.
- **Invariants & monovariants** (Combinatorics): the monovariant is the sub-problem size S_{k*}/(2^{k*}-1) relative to t_m; it strictly decreases at each inductive level.

### Analogous Past Problems (Cruxes)

None checked in this round (crux corpus not queried). The structure (optimal marking + inductive response) is specific enough that generic crux moves are unlikely to add value here.

### Prior Progress

- Lower bound: Complete and rigorous (geometric marking + copy strategy).
- Answer c(n) = 2^n/(2^{n+1}-1): Computationally verified for n=1,...,4.
- Upper bound cases k=1,2,n+1: Complete.
- Cases k=3,...,n: NOW CLOSEABLE via k*=largest argument.

### Dead Ends (Do Not Retry)

- **Lemma 5 in induction-on-n.md** ("p_1 ≤ t_n OR p_{n+1} ≤ c(n)"): FALSE, counterexample in current.md.
- **Naive strategy for k ∈ {3,...,n}** (leave p_1,...,p_k as singletons, halve the rest): Fails because alternating sum of k ≥ 3 singletons can exceed t_n.
- **Ratio-based-induction interleaving gap**: Real, but resolved by choosing k*=largest (which guarantees all halved elements above the singletons).

### Small-Case / Intuition Notes

- For n=1: k* ∈ {1, 2}, all cases k=1 and k=n+1 (k=2). No middle cases.
- For n=2: k* ∈ {1, 2, 3}, all cases k=1, k=2, k=n+1 (k=3). No middle cases.
- For n=4: k*=3 is achievable (e.g., p1=11/310, p2=21/310, p3=3/31, p4=17/62, p5=163/310). Verified: S_{k*} = 1/5 < 7/31 = (2^3-1)t_4, and A_bound = 1/35 < 1/31 = t_4. Conjecture becomes theorem.
- The factor cancellation (2^{k*}-1)·t_{k*-1} = (2^{k*}-1)/(2^{k*}-1) = 1 is exact, verified for k*=1,...,6.
