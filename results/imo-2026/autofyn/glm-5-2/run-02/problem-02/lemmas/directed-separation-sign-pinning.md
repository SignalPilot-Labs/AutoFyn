# Lemma (directed-separation sign-pinning of B/C sine-arc equations — round 3)

*On the inside-hypothesis branch, the cross-ratios `(A,P;R,V)` and `(A,Q;S,W)` are both NEGATIVE (separating pairs: cyclic orders `R,A,V,P` and `Q,W,A,S` on `Γ=(AKL)`), and the sine-of-arc slot-by-slot resolution gives*
> **(B)** `sin(α+u)·sin(γ−a)/[sin(α+a)·sin(γ−u)] = −2·MP/PB`
> **(C)** `sin(α−w)·sin(b+β)/[sin(b−α)·sin(w+β)] = +2·QN/QC`

*(the C-side carries one extra overall sign flip vs the B-side; the signs are constant on the connected inside-hypothesis region).*

## Where proved
`approaches/power-secant-product.md`, Step 9a (round 3, reviewer-certified). Verified to `~1e-15` on the verified configuration.

## Mechanism
The sign of a real cross-ratio of four concyclic points is `−` iff the two pairs separate on the circle (interleave in the cyclic order). The inside-hypothesis region is connected (convex open subset of configuration space), and the cross-ratio sign is locally constant on configurations with four distinct concyclic points, so a single representative pins the sign everywhere on the branch. The sine-of-arc form (Step 8) resolves the `±` ambiguity slot-by-slot from the directed half-arcs. This replaces the numpy acute-angle `arccos`/`arctan2` pick that corrupted the round-1/2 sign claims.

## Transferable technique
The **directed-separation sign rule**: to pin the `±` of a cross-ratio-on-a-circle in directed-angle form, compute the cyclic order of the four points on ONE representative (by angular coordinate `θ = atan2(y−O_y, x−O_x)`, NOT by acute-angle picks), apply the interleave rule, and use connectedness of the branch to extend. Importable by any Γ-projective approach needing the directed sign of a midpoint cross-ratio.
