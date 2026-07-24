# Lemma CC+ (degree-2-cycle exclusion) — CERTIFIED round 7 (SUPERSEDES isolated-cycle-exclusion)

Source: `self-similar-recursion` §6a. Reviewer independently re-derived and numerically verified.
Strictly stronger than Lemma CC (`isolated-cycle-exclusion`): needs only the **piece** degrees, not
the component degrees.

## Statement
At the `Φ=Σx_i^2`-maximal non-degenerate global minimizer `P*` of a step of (LBL), let `H` be the
bipartite piece–value incidence multigraph. Let `Z=(a_1,Q_1,…,a_r,Q_r)` be a cycle in `H` (`r≥2`,
distinct pieces `2^{a_1},…,2^{a_r}`, distinct components `Q_1,…,Q_r`, each cycle edge multiplicity 1)
in which **every cycle-piece `2^{a_i}` has total degree exactly 2 in `H`** (its only two sub-pieces are
one copy each of `Q_{i-1}` and `Q_i`). Then `(★) Uw=b` has no all-positive solution — contradiction.
(The cycle *components* `Q_i` may carry arbitrary further edges to off-cycle pieces.)

## Proof
Each cycle-piece has degree 2, so its full budget lies on the two cycle components: `(★)` restricted to
the `r` cycle-pieces is the CLOSED system (`Q_0:=Q_r`)
```
    u_{i-1}+u_i = b_i,   b_i:=2^{a_i}  (full distinct powers),  i=1,…,r.   (CYC+)
```
No off-cycle datum enters, so this is a necessary condition on `u_1,…,u_r` alone.

- **Even `r`.** The left null-vector of the even cyclic bidiagonal-of-1's is the alternating pattern
  `v=((-1)^1,…,(-1)^r)` (column `j` receives `v_j+v_{j+1}=0`). Consistency of `(CYC+)` requires
  `vᵀb = Σ_i(-1)^i b_i = 0`. With `b_M=2^{a_max}` the unique largest,
  `|Σ_{i≠M}(-1)^i b_i| ≤ Σ_{ℓ≠M}2^{a_ℓ} ≤ 2^{a_max}-1 < b_M`, so the alternating sum cannot vanish.
  `(CYC+)` has **no solution at all**. (For `r=2`: `u_1+u_2=b_1` and `=b_2`, `b_1≠b_2`, impossible.)
- **Odd `r`.** The odd cyclic bidiagonal has determinant `1-(-1)^r=2≠0`; the unique solution is
  `u_j=½Σ_{t=0}^{r-1}(-1)^t b_{j+1+t}`. Choose the start `j` so the largest budget `b_M` receives sign
  `-1` (the offset `t≡M-j-1` takes every residue mod `r`, and `r≥3` supplies an odd one). Then
  `2u_j ≤ -b_M + Σ_{ℓ≠M}b_ℓ < 0` by the same superincreasing bound, so `u_j<0`, contradicting
  `w(Q_j)>0`. ∎

## Verification (reviewer, independent)
- Even distinct-power arrangements `Σ(-1)^i 2^{a_i}` for `r∈{2,4,6,8}`, exponents `0..9`, all
  permutations: **1,970,730 arrangements, 0 with zero alternating sum.**
- Odd cyclic systems `u_{i-1}+u_i=2^{a_i}`, `r∈{3,5,7}`: **246 distinct-power budget sets, 0 with an
  all-positive solution** (plus the round-6 brute of 197,064 confirming CC).

## Scope / honest limits
Excludes every cycle whose **cycle-pieces are all degree 2** — this contains all isolated cycles (both
parities) AND every cycle whose extra structure lives only on components (a cycle component touching an
off-cycle piece). NOT covered — Gap A′ residual: a cycle with a **cycle-piece of degree ≥3** (a genuine
chord, a non-uniform mult-≥2 cycle edge, or an off-cycle-mass attachment at a cycle-piece). Uses the
distinct-powers-of-two budgets essentially (immune to the pure-incidence 479-instance refutation).

## Supersession
This lemma **supersedes** `isolated-cycle-exclusion.md` (Lemma CC): every isolated cycle has all pieces
of degree 2, so CC is the special case. CC's file is retained for provenance but importers should cite
CC+.
