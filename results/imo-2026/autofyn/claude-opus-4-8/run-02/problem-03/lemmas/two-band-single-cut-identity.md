# Lemma: two-band-single-cut-identity (cut-budget Lemma 3.1)

**Certified round 5** (cut-budget-jacobsthal-recursion). Discrete companion to certified Lemma I
(cut-slide-derivative).

## Statement
Let `Q` be any multiset with count function `c_Q(t)=#{pieces > t}`, and let `Q'` replace one piece
of value `V` by two pieces `V_1 ≤ V_2`, `V_1+V_2=V`, `m:=V_1 ≤ V/2`. Then cutting flips the parity
of `c(t)` exactly on the two disjoint bands `B_low=[0,m)` and `B_high=[V−m, V)`, each of length `m`,
and leaves parity unchanged elsewhere. Hence (via `f=M=∫1[c(t) odd]dt`)
```
    f(Q') − f(Q) = Δ_low + Δ_high,   each Δ ∈ [−m, m],   so |f(Q')−f(Q)| ≤ 2m ≤ V.
```

## Proof
`c'(t)−c(t) = 1[V_1>t] + 1[V_2>t] − 1[V>t]`, which equals `+1` on `[0,V_1)`, `0` on `[V_1,V_2)`,
`−1` on `[V_2,V)`, `0` on `[V,∞)`. So the parity of the count flips precisely on
`[0,V_1)∪[V_2,V) = [0,m)∪[V−m,V)` (using `V−V_2=m`), each of length `m`. Integrating
`1[c' odd]−1[c odd]` (which is `0` off the bands, and `±1` on a flipped band according as `c` was
even/odd) gives the stated `Δ_low, Δ_high ∈ [−m,m]`, hence `|f(Q')−f(Q)| ≤ 2m ≤ V`. ∎

## Notes
Unconditional, follows from certified `layer-cake-alt-sum`. Setting `V_1=V_2` recovers
bisection = removal of `V` plus a P1-invisible matched pair.
