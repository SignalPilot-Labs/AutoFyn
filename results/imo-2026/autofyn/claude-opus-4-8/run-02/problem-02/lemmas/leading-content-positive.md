# Lemma L-pos (positivity of the leading content) — certified round 1

**Frame.** `B=(0,0)`, `C=(a,0)`, `A=(p,q)` with `q>0`; `θ=∠KBA=∠ACL∈(0,π)`,
`s=tan(θ/2)>0`; `K` on the ray from `B` clockwise of `BA`, `L` on the ray from `C` CCW of
`CA`; `K∈△BMC`, `L∈△BNC` (`M,N` midpoints of `AB,AC`).

**Statement.** The condition polynomials `G(t_K)` (encoding `∠LCK=∠BMK`) and `H(t_L)`
(encoding `∠LBK=∠LNC`) have leading coefficients
`lc_{t_K}(G)=\tfrac12(1+s²)²(p²+q²)f`, `lc_{t_L}(H)=\tfrac12(1+s²)²((p−a)²+q²)f`, where
`f=2s(p²+q²)−2aps+aq(1−s²)`. Moreover
`f=(1+s²)·AB·AC·sin(∠A+θ)` and `f>0` on the admissible region.

**Proof.** The leading-coefficient factorizations and the identity
`f=(1+s²)·AB·AC·sin(∠A+θ)` are exact symbolic identities (`verify.py`; reviewer
re-derived both from scratch — `lc_{t_K}(G)/f=(p²+q²)(1+s²)²/2`,
`lc_{t_L}(H)/f=((p−a)²+q²)(1+s²)²/2`, and `f−(1+s²)·AB·AC·sin(∠A+θ)=0`). For positivity:
`∠A,θ>0` give `∠A+θ>0`; ray `BM`=ray `BA` and `K∈△BMC` force `θ=∠KBA<∠ABC`; the angle sum
gives `∠A+∠ABC=π−∠ACB<π`; hence `∠A+θ∈(0,π)`, `sin(∠A+θ)>0`, and with `1+s²,AB,AC>0`,
`f>0`. ∎

**Use.** `f≠0` is exactly the nonvanishing that licenses dividing the polynomial identity
`f·T=Q_G·G+Q_H·H` by `f` at an admissible configuration (closes the `0·∞` hole in the
ideal-membership step).
