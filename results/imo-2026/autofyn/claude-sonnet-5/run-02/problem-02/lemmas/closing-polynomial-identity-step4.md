# Lemma: closing polynomial identity for the cubic-locus elimination (Step 4)

**Status: certified (round 2 proof-reviewer), independently re-derived from
scratch in a fresh `sympy` script, not merely re-checked against the
builder's numbers.**

## Setup

Work in the WLOG frame `B=(0,0), C=(1,0), A=(p,q)`, `K=(k1,k2)`, `L=(l1,l2)`,
`M=(p/2,q/2)`, `N=((p+1)/2,q/2)`. Define (Dictionary-Lemma translations of
hypotheses (i)/(ii)/(iii), see `dictionary-lemma-equal-signed-angle.md`):

```
eq1 := cross(K-B,A-B)·dot(A-C,L-C) − cross(A-C,L-C)·dot(K-B,A-B)
eq2 := cross(L-B,K-B)·dot(L-N,C-N) − cross(L-N,C-N)·dot(L-B,K-B)
eq3 := cross(L-C,K-C)·dot(B-M,K-M) − cross(B-M,K-M)·dot(L-C,K-C)
```

`eq1` is linear in `l2`, with `l2`-coefficient exactly `-D` where
`D := k1p²-k1p-k1q²+2k2pq-k2q`. Solving `eq1=0` for `l2` (exactly, via
`sympy.solve`, not the sign-inconsistent formula appearing in the
`complex-number-argument-bash` write-up — see note below) gives a rational
function `l2 = l2_expr(k1,k2,l1,p,q)` with denominator `-D`.

Substituting into `eq3`, clearing denominators, gives (fully re-verified)
```
eq3_num = -(l1-1)(p²+q²)·X(k1,k2,p,q)
```
with `X` the explicit irreducible cubic given in `cubic-locus-for-K.md`
(same polynomial, sign notwithstanding).

Substituting into `eq2` gives `eq2_num`, degree 2 in `l1`, degree 3 in
`(k1,k2)` — re-confirmed.

Let `Fn_num_raw` be the numerator of `O_x - (p/2+1/4)` (circumcenter of
`A,K,L` with `l2` eliminated as above), after combining to lowest terms.

## The identity

With
```
D2 := -k1q + k2p - k2
E1 := -2k1pq + k1q + k2p² - k2p - k2q²
E0 := k1p²q + k1pq - k1q³ - k1q - k2p² + 2k2pq² + k2p
```
the polynomial identity
```
Fn_num_raw·D2 − (k2−q)·eq2_num = D·X·(E1·l1+E0)
```
holds identically in `ℤ[p,q,k1,k2,l1]`.

**Independent re-derivation (this review).** Re-derived `eq1,eq2,eq3` from
the raw cross/dot definitions, solved `eq1=0` for `l2` via `sympy.solve`
(ground truth — not the write-up's stated closed form, which has an
overall sign error, see note below), substituted into `eq3` and `eq2`,
computed `Fn_num_raw` from the standard circumcenter formula, and verified
`sympy.expand(LHS - RHS) == 0` exactly. Confirmed both `eq3_num` matches
`X` above (up to overall sign) and `eq2_num` has degree 2 in `l1` / degree
3 in `(k1,k2)`, matching the builder's claims.

**Corollary (also re-verified).** `D_circ|_{l2=l2_expr} = 2·D3/D`, where
`D3` is the cofactor such that `Fn_den_raw = 4·D·D3`. Confirmed exactly
(`sympy.simplify` of the difference is `0`).

## Note on a write-up typo (not a computational error)

The `complex-number-argument-bash` approach file states the elimination
result as `l2 = l2_num/D` for an explicit `l2_num`. This formula does
**not** satisfy `eq1=0` — the correct formula is `l2 = -l2_num/D` (an
overall sign flip; `sympy` confirms `eq1` evaluated at the stated formula
is a nonzero polynomial, while at the negated formula it is identically
zero). This is a genuine sign slip in the prose description of Step 1.
However, independently rebuilding the entire downstream pipeline (Step
2–4) with the *correct* sign of `l2` reproduces exactly the claimed `X`,
`eq2_num` degree data, `Fn_den_raw = 4·D·D3`, and the closing identity
above — so the actual symbolic computation that produced these downstream
artifacts must have used the correct sign (i.e. the flaw is confined to
the human-readable formula in the write-up, not the artifacts derived from
it). The write-up's Step 1 display formula should be corrected to
`l2 = -l2_num/D` (equivalently `l2_num/(-D)`) in the next revision.

## Consequence

At any point with `X=0` (Step 2's cubic locus) and `eq2_num=0` (Step 3),
the identity forces `Fn_num_raw·D2 = 0`; combined with the genericity facts
`D2≠0` and `D≠0` (Step 5) this gives `Fn_num_raw=0`, i.e. the target
`O_x = p/2+1/4`. This is the algebraic core of the elimination — it is
**not**, by itself, a full proof of the theorem, because it presupposes
that `eq1,eq2,eq3` (via the Dictionary Lemma's specific vector pairings)
correctly encode the problem's hypotheses (i)-(iii) with matching
orientation, which remains an **open, unverified gap** (see
`current.md`).
