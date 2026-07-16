# Lemma (Shadow strategy, upper bound Regime A)

**Status:** certified (proof-reviewer, round 3). Re-derived independently and verified numerically
(301 random spectra with A_1 ∈ [1/2, c(n)], n ≤ 4: val = A_1 exactly, all ≤ c(n); 0 mismatches).

## Statement
Let Liu Bang's pieces be A_1 ≥ A_2 ≥ … ≥ A_m (m ≤ n + 1, Σ A_i = 1). Suppose the largest piece satisfies
**1/2 ≤ A_1 ≤ c(n)**, where c(n) = 2^n/(2^{n+1} − 1). Then Xiang Yu, using at most n cuts, can force

  val(final) = A_1 ≤ c(n).

## Proof
Set r := A_1 − (A_2 + ⋯ + A_m) = A_1 − (1 − A_1) = 2A_1 − 1 ≥ 0 (using A_1 ≥ 1/2). Xiang Yu cuts the
piece A_1 at the interior partial-sum points A_2, A_2 + A_3, …, A_2 + ⋯ + A_{m−1} (and, if r > 0, also at
A_2 + ⋯ + A_m), splitting A_1 into the parts {A_2, A_3, …, A_m, r}. This uses m − 1 ≤ n cuts (m − 2 if
r = 0), all strictly interior to A_1, hence distinct from Liu Bang's marks (piece boundaries) and from
each other (all sublengths positive). The parts sum to (1 − A_1) + r = A_1, so this is a legal cut of A_1.

The final multiset is the untouched pieces A_2, …, A_m together with the subpieces A_2, …, A_m, r of A_1:

  M_final = {r} ∪ {A_i (doubled) : 2 ≤ i ≤ m}.

For every x, N_{M_final}(x) = 𝟙[r > x] + 2·#{i ≥ 2 : A_i > x}. The second term is even for all x, so
N_{M_final}(x) is odd iff x < r. Thus S_{M_final} = [0, r), and by the measure representation
A(M_final) = measure[0, r) = r. With T = 1,

  val = (1 + A)/2 = (1 + r)/2 = (1 + 2A_1 − 1)/2 = A_1 ≤ c(n). ∎

## Scope note
Requires A_1 ≥ 1/2 (else r < 0 is infeasible) and A_1 ≤ c(n) (to conclude val ≤ c(n)). The regimes
A_1 < 1/2 (flat) and A_1 > c(n) (dominant) are NOT covered and remain open.
