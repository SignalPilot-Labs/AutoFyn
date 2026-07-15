## Status
partial

## Approaches tried
- Reduce by the antipode of `A`, then seek a cancellation among six complex directed-ray equations and the two Thales equations — the antipode reduction is established, but the quarter-turn telescoping identity is an explicit gap.

## Current best
Let `X` be the antipode of `A` on the circumcircle of `AKL`. The factor-2 homothety centered at `A` maps `(O,M,N)` to `(X,B,C)`, respectively; hence the original claim is exactly equivalent to `XB=XC`.

Normalize complex coordinates by `a=0`, `b=1`, and `c=q e^{i gamma}`. With `alpha,beta,delta` denoting the three given common angles, derive and sign-justify all six positive-parameter ray equations
`k=1-r e^{-i alpha}=1/2+s e^{i delta}=c-w e^{i(gamma+alpha+delta)}` and
`l=c-u e^{i(gamma+alpha)}=1-v e^{-i(alpha+beta)}=c/2+h e^{i(gamma-beta)}`.

Thales' theorem gives `XK perpendicular AK` and `XL perpendicular AL`, hence `x-k=i lambda k` and `x-l=i mu l` for real `lambda,mu`, equivalently `Re(conj(x)k)=|k|^2` and `Re(conj(x)l)=|l|^2`. The intended endpoint is
`Re(conj(x)(c-b))=(q^2-1)/2`, which is equivalent to `XB=XC`.

The load-bearing open gap is the quarter-turn telescoping lemma. Before prose claims cancellation, the builder must display the exact ordered real/imaginary-part equalities and their multipliers, verify coefficient-by-coefficient cancellation of `r,s,w,u,v,h`, and identify precisely where `2BM/AB=2CN/AC=1` enters. Cases `lambda=0` and `mu=0` must be retained without illegal division. If the cancellation only reproduces the determinant residual of another approach, that dependence must be stated rather than described as an independent synthetic telescoping.
