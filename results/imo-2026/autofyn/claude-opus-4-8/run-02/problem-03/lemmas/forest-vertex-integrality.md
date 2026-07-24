# Lemmas S & T: minimizer incidence is a forest with an integer solution

**Status: REJECTED (round 4, reviewer).**
The Setup relies on Lemma W ("each component has ≤1 sub-piece per piece except bisection leaves"),
which is FALSE (see `within-piece-tie-p1.md`): the global minimizer piece8={2,3,3} has a
non-bisection multiplicity-2 edge (piece 8 ↔ value 3, degree ≥2), so the incidence matrix is not
the clean 0/1-plus-bisection-leaf structure assumed. Lemma T's conclusion "every sub-piece is a
positive integer" is directly refuted by the non-integer minimizer family piece2={a,2−a},
piece8={4,2,2} (f=1, a∈(0,2)). The Φ-maximal selection may still salvage integrality, but it is
NOT established by the argument as written (Lemma S's proof invokes the false Lemma W premise).
Do NOT certify until an integrality argument valid in the presence of surviving within-piece ties
is supplied.

**Original (rejected) content follows.**

**Status: PROPOSED (round 4, from `self-similar-recursion`) — awaiting certification.**

## Setup
`P*` is a non-degenerate global minimizer of `f` over `≤N`-cut refinements of `W_n`, chosen to
maximize `Φ=Σ_i x_i^2` among all such minimizers. Group sub-pieces into **components** (value
classes) `C_1,…,C_p` with distinct values `w_j>0`. By Lemma W (`within-piece-tie-p1.md`) each
component has `≤1` sub-piece per piece, except `r_k=2` equal bisections (a leaf component of value
`2^{k-1}`). Incidence matrix `U`: `(Uw)_k=Σ_j μ_{k,j}w_j=2^k`, `μ_{k,j}∈\{0,1\}` (or `2` at a
bisection leaf).

## Lemma S (no sum-preserving shift ⇒ forest)
`\ker U=\{0\}` (so `w` is the unique solution of `Uw=(2^k)_k`), and the bipartite
piece–component graph `H` is a forest.

*Proof.* If `Ud=0`, `d≠0`, shifting `w_j(δ)=w_j+δd_j` preserves every piece-sum, giving a feasible
line through `P*`; for small `|δ|` values stay positive, distinct and ordered, so `f` is affine,
`f(δ)=m+γδ`. If `γ≠0`, some `δ` gives `f<m` (contradiction with minimality). If `γ=0`, the segment
lies in the minimizer set `G`, but `Φ(δ)` is a strictly convex quadratic in `δ` (leading coefficient
`Σc_i^2>0`), so it exceeds `Φ(P*)` at some `δ≠0` in `G` — contradiction with `Φ`-maximality. Hence
`\ker U=\{0\}`. A cycle in `H` (through simple edges; multiplicity-2 edges are at leaves) yields a
nonzero `d∈\ker U` (`±1` alternating on the cycle’s components), impossible; so `H` is a forest. ∎

## Lemma T (forest ⇒ integer)
Every `w_j∈ℤ`; hence `P*` is an integer configuration and, with `Σ(P*)=D_n` odd,
`f(P*)≡D_n≡1 (mod 2)` and `f(P*)≥0`, so `f(P*)≥1`.

*Proof.* Peel multiplicity-2 leaves: a bisection piece gives `2w_j=2^k`, `w_j=2^{k-1}∈ℤ`;
substitute (integer subtraction) and delete, keeping a forest with integer right side and unique
solution. The residual `0/1` system `U'w'=b'` has full column rank (uniqueness); a square
invertible submatrix `A` is a bipartite-forest biadjacency, whose determinant equals `±1` times the
number of perfect matchings, and a forest has at most one perfect matching, so `\det A=±1`. By
Cramer, `w'=A^{-1}b'∈ℤ^{p'}`. ∎
