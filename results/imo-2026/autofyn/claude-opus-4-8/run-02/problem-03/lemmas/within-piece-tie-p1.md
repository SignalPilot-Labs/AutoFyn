# Lemma W: within-piece-tie elimination via matched-pair invisibility (P1)

**Status: REJECTED (round 4, reviewer) — the STATEMENT IS FALSE.**
Counterexample (n=3): the refinement piece1={1}, piece2={2}, piece4={2,2}, piece8={2,3,3}
is a non-degenerate GLOBAL minimizer (multiset {1,2,2,2,2,3,3}, f=1=min), yet piece8 is cut into
r=3 sub-pieces with two equal (3,3) that are NOT a bisection. So statement (1) fails. A whole
continuum also refutes it AND Lemma T's integrality: piece1={1}, piece2={a,2−a}, piece4={4},
piece8={4,2,2} has f=1 for every a∈(0,2) — non-integer, within-piece tie {2,2} at r=3.
The PROOF is also invalid independently: the move q→v+t,q'→v+t,q''→w−2t is claimed "affine with
nonzero slope", but when q'' lies in an even-size tie-block of the remainder at an odd top rank
(σ_a=+1) the one-sided slopes are −2σ_a (t<0) and −2σ_b=+2σ_a (t>0), giving f=m+2|t| (a strict
V-shaped local MIN, no descent). Confirmed numerically. Do NOT re-propose.

**Original (rejected) content follows.**

**Status: PROPOSED (round 4, from `self-similar-recursion`) — awaiting certification.**

## Setup
Fix a cut pattern on `W_n={2^0,…,2^n}`: piece `2^k` splits into `r_k` sub-pieces of lengths `≥0`
summing to `2^k`. `f` = alternating sum of the full multiset; it depends only on the multiset of
lengths. Certified imports: matched-pair invisibility (P1, from `layer-cake-alt-sum.md`) and the
one-sided cut-slide derivative (Lemma I, `cut-slide-derivative.md`).

## Statement
At any **non-degenerate** (all lengths `>0`) global minimizer `P*` of `f`:
1. if `r_k≥3`, no two sub-pieces of piece `2^k` are equal;
2. if `r_k=2` and its two sub-pieces are equal, each equals `2^{k-1}∈ℤ`.

## Proof
(2) is immediate (`2v=2^k`). For (1), suppose piece `2^k` has `r_k≥3` sub-pieces with `q=q'=v`;
pick a third same-piece sub-piece `q''=w`. For `t` near `0` set `q→v+t, q'→v+t, q''→w−2t` (others
fixed): the piece-sum is preserved (`+t+t−2t=0`), lengths stay positive for small `|t|`, so this is
a feasible line in the domain. Along it `q,q'` stay **equal**, so by P1 they change the parity of
`c(τ)=#{pieces>τ}` for no `τ`; hence `f` varies only through `q''`. By Lemma I,
`∂f/∂(\text{decrease }q'')=−σ_b∈\{±1\}`, and since `q''` moves at rate `−2`, `f(t)=m−2σ_b t` is
affine with nonzero slope near `0`. One sign of `t` gives `f<m`, contradicting minimality. ∎

## Consequence
Every within-piece tie of `P*` is an `r_k=2` equal bisection of integer value `2^{k-1}`; every
other value-class (component) contains at most one sub-piece per original piece.
