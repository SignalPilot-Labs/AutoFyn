# Lemma: budget-ker (Lemma BUDGET-KER, Budget-minimal ⟹ full column rank)

**Certified round 8** (dual-integer-certificate). Reviewer-verified. Budget-Lemma analogue of the
certified S-core reduction (`phimax-trivial-kernel`).

## Statement
Suppose some all-even refinement of `W_n` has `N≤n` cuts. Then there is an all-even refinement of
`W_n` with `N≤n` cuts whose incidence matrix `U∈ℤ_{≥0}^{(n+1)×p}` (distinct values `w_1>…>w_p>0`,
`Uw=b=(2^0,…,2^n)ᵀ`, all column sums `μ_j` even) has `ker U={0}` (full column rank, `p≤n+1`); its
values are the unique rational solution of `Uw=b`.

## Proof
Among all all-even refinements with `N≤n` choose one with minimal `N`, and among those minimal `p`;
call it `R=(U,w)`. Suppose `ker U≠{0}`; pick `0≠δ∈ker U`. Then `U(w+tδ)=b` for all `t`, with `U`
(the incidence) unchanged. Since `U≥0` has no zero column, `δ` cannot be coordinatewise `≥0` (else
some `(Uδ)_k>0`, contradicting `Uδ=0`); so some coordinate is negative and the corresponding value
`w_j(t)` decreases as `t` increases. Let `t^*>0` be the first `t` at which either (i) some
`w_j(t^*)=0`, or (ii) two coordinates first coincide `w_i(t^*)=w_j(t^*)`. (A linearly decreasing
coordinate guarantees `t^*<∞`.)

- **Case (i).** Value class `j` reaches `0`; its `μ_j` (even, `≥2`) sub-pieces vanish. Deleting them
  gives incidence `U'` (column `j` removed) with `U'w'=b` still holding (the removed column
  contributed `0` in the limit), every remaining value positive, and one entire even class gone — so
  an all-even refinement with `N'=N−μ_j<N` cuts, `N'≤n`. Contradicts minimality of `N`.
- **Case (ii).** `w_i=w_j`; merge the two classes into the integer column `(col i)+(col j)` of even
  sum `μ_i+μ_j`. Same `N` (no sub-piece created/destroyed), strictly smaller `p`. Contradicts
  minimality of `p` among minimal-`N` configs.

Either way a contradiction, so `ker U={0}`. Full column rank forces `p≤n+1` and makes `w` the unique
(rational, since `U,b` integral) solution of `Uw=b`. ∎

## Use / scope
Lets the powers-of-two arithmetic (Cramer/2-adic, `degree-2-cycle-exclusion`) apply to the residual
Budget case: values are rational and determined by the integer incidence. It does NOT close the
lemma — `p<n+1` is possible with `ker U={0}` (the `n=2` example has a multiplicity-4 class, `p=2<3`),
so `T≥2p` remains too weak; the residual is still case (b) ≅ Gap A′.
