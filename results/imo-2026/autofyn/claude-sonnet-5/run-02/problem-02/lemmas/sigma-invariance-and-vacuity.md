# Lemmas: σ-invariance of the defining system, and vacuity of the naive
σ-antisymmetry mechanism

**Status: certified (round 2 proof-reviewer).** Both results independently
checked: the invariance proof by re-reading the clause-by-clause argument
(sound elementary labeling logic, no gap found); the vacuity claim by a
fresh, unconstrained-variable `sympy` computation (see below).

## Lemma A (σ-invariance of the defining system)

Let σ be the formal relabeling `B↦C, C↦B, M↦N, N↦M, K↦L, L↦K, A↦A`. Writing
`S(A,B,C)` for the 8-clause system (0a,0b: M,N are midpoints; (1) K in
△BMC; (2) L in △BNC; (3) K in ∠LBA; (4) L in ∠ACK; (5) ∠KBA=∠ACL; (6)
∠LBK=∠LNC; (7) ∠LCK=∠BMK), σ permutes the clause list into itself:
{(0a),(0b)} preserved setwise, (5) fixed, (1)↔(2), (3)↔(4), (6)↔(7).
Consequently
```
(K,L) valid for S(A,B,C)  ⟺  (L,K) valid for S(A,C,B).
```

*Proof check.* Each clause substitution is a routine relabeling identity
(e.g. "inside triangle BMC" = "inside triangle CMB" since a triangle's
interior doesn't depend on vertex order; "∠KBA" = "∠ABK" since an angle is
determined by its vertex and unordered ray pair). No step invokes anything
beyond elementary point-set/angle definitions. Verified clause-by-clause,
no gap found.

## Lemma B (vacuity of the naive antisymmetry target)

Define, for arbitrary points `A,B,C,K,L` (`A,K,L` non-collinear),
`O := circumcenter(A,K,L)`, `N9 := ` nine-point center of `ABC`, and
`T(A,B,C,K,L) := (O-N9)·(C-B)`. Then
```
T(A,C,B,L,K) = -T(A,B,C,K,L)
```
identically, for **all** `A,B,C,K,L` — no constraint on `K,L` (in
particular no use of hypotheses (i)-(iii)) is needed.

*Proof.* `circumcenter` and nine-point-center depend only on the
*unordered* vertex set, so `circumcenter(A,L,K)=circumcenter(A,K,L)` and
`N9(A,C,B)=N9(A,B,C)`; hence `T(A,C,B,L,K) = (O-N9)·(B-C) = -T(A,B,C,K,L)`.

*Independent re-verification (this review).* Using the O-free
reformulation `O·(C-B) = ½[α(|K|²-|A|²)+β(|L|²-|A|²)]` (with `α,β` the
explicit determinant ratios), computed with fully free unconstrained
coordinate symbols `Ax,...,Ly` in `sympy` that under the swap `B↔C, K↔L`
the O-dependent term negates identically: `Oterm(swap) + Oterm = 0` as a
rational function of the ten free symbols, with `sympy.simplify` returning
`0` unconditionally (no hypotheses imposed). Confirms the claim.

**Consequence (negative result).** Since this sign-flip identity holds for
*all* `A,B,C,K,L,K,L` with zero use of the problem's hypotheses, it cannot
by itself force `T(A,B,C,K,L)=0` for the specific `(K,L)` satisfying
(i)-(iii): a relation `f(x') = -f(x)` alone never forces `f(x)=0` unless a
second, independent relation (e.g. `f(x')=f(x)`, which relabeling alone
does not supply) is also available. **Any future approach attempting a
"swap labels via σ and conclude antisymmetric ⟹ zero" argument for this
problem is provably dead on arrival** unless it supplies such a second,
non-tautological relation (e.g. by using conditions (ii),(iii) directly,
not just their formal σ-pairing).
