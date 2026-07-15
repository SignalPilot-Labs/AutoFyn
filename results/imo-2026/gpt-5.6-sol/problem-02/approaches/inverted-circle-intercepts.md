## Status
partial

## Approaches tried
- Convert the distance claim to equal powers and invert the circumcircle at `A` — the reduction is valid in principle, but the proposed inverted-line intercept relation is not established and the approach is deferred from the build set.

## Current best
Let `P` and `Q` be the second intersections of `AB` and `AC` with the circumcircle `omega=(AKL)`, interpreted with directed lengths. Since `Pow_omega(Y)=OY^2-OA^2`, the target is equivalent to `Pow_omega(M)=Pow_omega(N)`, and the intended secant calculation reduces this to
`AB·AP-AC·AQ=(AB^2-AC^2)/2` under a declared signed-length convention.

Invert about `A` with squared radius `rho`. Then `omega` becomes the line through `K'=rho K/AK^2` and `L'=rho L/AL^2`; if its side intercepts are `P'` and `Q'`, inversion gives `AP·AP'=AQ·AQ'=rho`. The desired whole route would derive directly from the six ray incidences
`rho AB/AP' - rho AC/AQ'=(AB^2-AC^2)/2`, and then invert back to the equal-power identity.

The decisive open gap is this inverted-line intercept lemma. Reciprocal-square inversion is nonlinear, so eliminating affine ray parameters is not automatically linear. Before any future build, explicit formulas for `P'` and `Q'` and an actual cancellation from the incidence equations are required. A complete treatment must also settle directed secant signs, tangent/coincident second intersections, an intercept at infinity, and zero-power midpoint cases, or prove each exceptional case impossible. Do not use identities derived from the false assertion that `B,C,K,L` are cyclic.
