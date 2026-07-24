# Lemma: two-invisible-pairs-mult-bound (Move M2)

**Certified round 5** (self-similar-recursion). Verified 0/30000.

## Statement
At a `Φ=Σx_i^2`-maximal minimizer `P*` of the alternating sum over the product-of-simplices domain,
no single piece `2^k` has `≥4` sub-pieces equal to a common value `v`. Hence every within-piece
multiplicity satisfies `μ_{k,j} ≤ 3`.

## Proof
If piece `2^k` had four sub-pieces equal to `v`, replace, for small `t`,
`{v,v,v,v} → {v+t, v+t, v−t, v−t}` inside piece `2^k`. The piece sum is preserved (`+t+t−t−t=0`)
and all lengths stay positive for `|t|` small. Before and after, the four form two equal pairs
(`{v,v},{v,v}` resp. `{v+t,v+t},{v−t,v−t}`); by matched-pair invisibility (P1) each equal pair
leaves `M`, hence `f`, unchanged. So `f(P*)` is exactly unchanged — the point stays a minimizer —
while `Φ` gains `2(v+t)^2+2(v−t)^2−4v^2 = 4t^2 > 0`, contradicting `Φ`-maximality. ∎

## Notes
Parity-independent: excludes ALL `μ_{k,j}≥4` (even or odd), so no "μ even ⇒ power of 2"
inference is needed. Unconditional.
