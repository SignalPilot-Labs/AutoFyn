## Status
solved

## Approaches tried
- **segment-subset-pigeonhole** (SOLVED, round 6) — unified both bounds on Liu Bang's original
  segments. UB = merge-alignment refinement (L15/UB1) + subset-sum pigeonhole; LB = spanning-tree /
  bipartite signed-sum extraction (L16/LB1) + dyadic integer minimality (L17/LB2). Reviewer-verified
  complete and correct; every step independently reproduced, 0 numeric violations. This is the
  solution.
- **induction-peel** (partial, superseded) — layer-cake strong-induction LB anchor (certified
  L0–L14). Round 6: shard-count/boundary-invariance axis for (CB) FALSIFIED (slack non-constant);
  UB branch-inequality line retired dead (F1, n=5 all-branches counterexample). No gap closed;
  superseded by segment-subset-pigeonhole. Remains the certified-lemma anchor.
- **alternating-sum-potential** (partial, superseded) — layer-cake β-matching; certified L8, L10,
  L14. Same LB wall.
- **global-max-peel / interlacing-bijection** (partial, superseded) — layer-cake reframings.
- **averaging-upper-bound, smoothing-extremal, randomized-xy-cut** (dead, do-not-retry) — refuted.

## Current best
Full proof below (solved).

## Answer
**c(n) = 2^n / (2^{n+1} − 1).** Write D_n := 2^{n+1} − 1.

## Full proof

For a finite multiset X = {x_(1) ≥ x_(2) ≥ ⋯ ≥ x_(N)} of nonnegative reals, define the
**potential** S(X) := Σ_i (−1)^{i+1} x_(i) = x_(1) − x_(2) + x_(3) − ⋯ ≥ 0.

### 0. Reduction (certified L0, L1, L2)
By L0 (claiming = odd-rank sum) and L1 (order irrelevance), the stick game is equivalent to: Liu
Bang picks a multiset A of m ≤ n+1 positive reals summing to 1 (his ≤ n cuts); Xiang Yu performs
≤ n split operations, each replacing a part x by two positive parts summing to x, yielding a
refinement B; Liu Bang's guaranteed value is Σ_odd(B). So c(n) = max_A min_B Σ_odd(B). By L2,
Σ_odd(B) = (1 + S(B))/2, so c(n) = (1 + max_A min_B S(B))/2, and since 2·(2^n/D_n) − 1 = 1/D_n,
the claim c(n) = 2^n/D_n is equivalent to **max_A min_B S(B) = 1/D_n.** S(B) is always the
functional of the OUTPUT multiset B — the same S as in L2 and L4 — so there is no pairing to
reconcile. min_B ranges over refinements reachable with ≤ n splits.

### 1. Upper bound: min_B S(B) ≤ 1/D_n for every A

**Lemma UB1 (= L15).** For A with m parts summing to 1 and disjoint S,T ⊆ {1,…,m}, (S,T)≠(∅,∅),
Xiang Yu has a refinement B using ≤ m−1 splits with S(B) ≤ |Σ(S) − Σ(T)|. *(Proof: bisect the
leftover parts; lay the S-parts on [0,Σ(S)] and T-parts on [0,Σ(T)] and cut both blocks at the
union C of all boundary points in [0,Σ(T)], producing q matched equal pairs on [0,Σ(T)] plus
overhang pieces of mass Σ(S)−Σ(T); by L4, S(B) ≤ cost of the explicit partition {twin pairs 0,
matched pairs 0, overhang paired among themselves} ≤ Σ(S)−Σ(T) using |u−v|≤u+v. Cut budget:
|L| + |T| + (|S|−1) = m−1. See L15.)*

Fix any A with m ≤ n+1 parts.
- **Case m ≤ n.** Xiang Yu bisects every part into two equal halves (m ≤ n splits); B is m equal
  pairs, so by L4 S(B) ≤ 0, hence S(B) = 0 ≤ 1/D_n.
- **Case m = n+1.** The 2^{n+1} subsets U ⊆ {1,…,n+1} have sums Σ(U) ∈ [0,1]. Partition [0,1] into
  D_n = 2^{n+1}−1 cells of length 1/D_n. Since 2^{n+1} = D_n + 1 > D_n, by the pigeonhole principle
  two distinct subsets U ≠ V share a cell: |Σ(U) − Σ(V)| ≤ 1/D_n. Put S := U∖V, T := V∖U (disjoint,
  and nonempty-as-a-pair since U△V ≠ ∅); then Σ(S)−Σ(T) = Σ(U)−Σ(V), so |Σ(S)−Σ(T)| ≤ 1/D_n. UB1
  gives B with S(B) ≤ 1/D_n using ≤ m−1 = n splits.

In both cases min_B S(B) ≤ 1/D_n, so **max_A min_B S(B) ≤ 1/D_n.**

### 2. Lower bound: min_B S(B) ≥ 1/D_n for the dyadic A

Take A dyadic: a_i = 2^{i−1}/D_n, i = 1,…,n+1 (Σ a_i = (2^{n+1}−1)/D_n = 1, so m = n+1).

**Lemma LB1 (= L16).** For m = n+1 parts, every ≤ n-split refinement B satisfies S(B) ≥ Δ(A),
where Δ(A) := min over ε ∈ {−1,0,1}^m, ε ≠ 0, of |Σ_i ε_i a_i|. *(Proof: write S(B) = Σ_e d_e
over the edges of a multigraph G on the m parts + a dummy δ (a_δ=0), one edge per consecutive
sorted pair with gap d_e ≥ 0. V = n+2, E = ⌈N/2⌉ ≤ n+1 < V (as N ≤ 2n+1), so V−E ≥ 1 forces a
tree component; a tree component containing a real part-vertex exists (part-vertices are never
isolated; the lone-δ case is excluded by a parity split). 2-color that tree K; the edge-length
identity Σ_{v∈K}σ(v)a_v = Σ_{e∈K} ±d_e (valid since K is a union of components) gives
|Σ_{v∈K}σ(v)a_v| ≤ Σ_{e∈K} d_e ≤ Σ_all d_e = S(B). Reading σ off K as a nonzero ε yields
Δ(A) ≤ S(B). See L16.)*

**Lemma LB2 (= L17).** For the dyadic A, Δ(A) = 1/D_n. *(Δ = (1/D_n)·min|Σ ε_i 2^{i−1}| over
nonzero ε ∈ {−1,0,1}^{n+1}; the top nonzero term dominates Σ_{i<j} 2^{i−1} = 2^{j−1}−1, so the
integer sum is nonzero, ≥ 1, with equality at ε=(1,0,…,0).)*

Hence every refinement of the dyadic A has S(B) ≥ 1/D_n, so min_B S(B) ≥ 1/D_n, giving
**max_A min_B S(B) ≥ 1/D_n.**

### 3. Conclusion
Combining §1 and §2, max_A min_B S(B) = 1/D_n, so
  c(n) = (1 + 1/D_n)/2 = (D_n + 1)/(2 D_n) = 2^{n+1}/(2 D_n) = **2^n / (2^{n+1} − 1).**

*Verification.* n = 1: c(1) = 2/3 (matches the fully-proven base case). Tightness at the dyadic A:
its subset sums are exactly {k/D_n : k = 0,…,D_n} (all distinct integers over D_n), the closest
distinct pair differs by exactly 1/D_n, so §1 gives Xiang Yu a refinement with S(B) = 1/D_n while
§2 shows none does better; min_B S(B) = 1/D_n is attained. ∎

Certified supporting lemmas: L0, L1, L2, L4 (reduction + min-pairing), L15 (UB1), L16 (LB1),
L17 (LB2).
</content>
