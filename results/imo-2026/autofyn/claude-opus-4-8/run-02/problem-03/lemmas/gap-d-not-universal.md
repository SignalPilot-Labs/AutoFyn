# Fact: Gap D (integer dual solvability) is NOT universal — CERTIFIED round 6

Source: `dual-integer-certificate` §3. Reviewer verified.

## Statement
There is an S-core (`ker U=0`) reachable refinement of `W_2={1,2,4}` for which the integer-dual
condition FAILS: `s ∉ Uᵀℤ^{n+1}`. Namely `P = {2, 4/3, 4/3, 4/3, 1}` (cut piece `4` into three equal
thirds), values `w=(2,4/3,1)`, blocks of sizes `1,3,1`:
```
    U = [[0,0,1],[1,0,0],[0,3,0]],  b=(1,2,4),  s=(1,-1,1).
```
Here `det U = ±3 ≠ 0` (S-core) but `Uᵀλ=s` has `3λ_2 = -1`, no integer solution; gcd of the
maximal minors of `U` is `3`. Rationally `λ=(1,1,-1/3)`, `λᵀb = 5/3 = f(P) ∉ ℤ`.

## Verification (reviewer)
`Uw=b` confirmed; `f=sᵀw=5/3`; `det U=3`; no integer `λ`. `P` is NOT a global minimizer (`min f=1`).

## Consequence (why this matters for the route)
Any proof of Gap D (`Uᵀλ=s` integer-solvable) MUST invoke that `P*` is a global minimizer /
Φ-maximal — it is FALSE for general S-core reachable configs. So the integer-dual route does not
cheaply escape the primal difficulty class; it is a genuinely different OBJECT (a lattice/gcd
coprimality condition (GCD-1), not `det=±1`), but it needs minimality just as the primal route does.
Prevents re-attempting a minimality-free lattice closure of Gap D.
