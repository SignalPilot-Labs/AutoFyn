# Lemma CC (isolated-cycle exclusion) — CERTIFIED round 6 — SUPERSEDED round 7

**SUPERSEDED by `degree-2-cycle-exclusion.md` (Lemma CC+).** CC+ needs only the cycle-*piece* degrees
(not the component degrees), so every isolated cycle is a special case. Importers should cite CC+.
This file retained for provenance.


Source: `self-similar-recursion` §6. Reviewer independently re-derived and numerically verified.

## Statement
At the `Φ=Σx_i^2`-maximal non-degenerate global minimizer `P*` of a step of (LBL), let `H` be the
bipartite piece–value incidence multigraph (nodes = the `n+1` pieces `2^{a}` and the `p` value
classes `Q_j`, with `μ_{k,j}` edges). Then `H` contains **no isolated cycle** — no connected
component that is a bare 2-regular alternating cycle
`2^{a_1}—Q_1—2^{a_2}—Q_2—…—2^{a_r}—Q_r—2^{a_1}` (`r≥2`) through distinct pieces and distinct
components, every walk-edge of multiplicity 1, with every one of its `2r` nodes of degree exactly 2.

## Proof
On an isolated cycle each piece `2^{a_i}` has its two sub-pieces exactly `Q_{i-1},Q_i` (mult 1), so
the piece-sum equations read `u_{i-1}+u_i = b_i` (CYC), `u_i=w(Q_i)>0`, `b_i=2^{a_i}` distinct
powers of two, indices mod `r`.

- **Even `r`.** Set `d(Q_i)=(-1)^i`, `d=0` elsewhere. Each cycle piece row gives
  `(Ud)=(-1)^{i-1}+(-1)^i=0`; every other row is disjoint from `supp(d)` because the cycle
  components have degree 2 (isolated), touching no piece outside the cycle. Wrap-around closes since
  `r` even. So `d≠0`, `Ud=0`, contradicting `ker U={0}` (Lemma S-core = `phimax-trivial-kernel`).
  (`r=2`: `u_1+u_2=b_1=b_2` impossible since `b_1≠b_2`.)
- **Odd `r`.** (CYC) is nonsingular (cyclic bidiagonal, det `1-(-1)^r=2`); the unique solution is
  `u_j=½Σ_{t=0}^{r-1}(-1)^t b_{j+1+t}`. Let `b_M=2^{a_max}` be the largest budget. As `j` ranges,
  the offset `t≡M-j-1` of `b_M` takes every residue mod `r`; pick `j` giving odd `t`, so `b_M` gets
  sign `-1`. Then `2u_j = -b_M + Σ_{ℓ≠M}(±1)b_ℓ ≤ -b_M + Σ_{ℓ≠M}b_ℓ < 0` by the superincreasing
  bound `Σ_{a<a_max}2^a = 2^{a_max}-1 < b_M`. So `u_j<0`, contradicting `w(Q_j)>0`. ∎

## Verification (reviewer, independent)
- Odd cyclic system `u_{i-1}+u_i=b_i` over all distinct power-of-two budget sets, `r∈{3,5,7}`,
  exponents `0..8`: **197064 systems tested, 0 with an all-positive solution.**
- Even-cycle alternating vector `d(Q_i)=(-1)^i` verified in the kernel of the cyclic incidence for
  `r∈{2,4,6}`.

## Scope / honest limits
Excludes ONLY isolated (bare 2-regular) cycles. Non-isolated cycles (chord, off-cycle degree-≥3
piece, multiplicity-≥2 edge) are NOT covered — the residual of Gap A. Uses the distinct-powers-of-two
budgets essentially, so it is immune to the pure-incidence 479-instance refutation.
