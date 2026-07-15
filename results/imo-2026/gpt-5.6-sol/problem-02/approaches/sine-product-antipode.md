## Status
partial

## Approaches tried
- Use the antipode of `A` and multiply directed sine-rule ratios around four triangles — the endpoint reduction is sound, but the exact four-triangle product and cancellation remain gaps.

## Current best
Let `X` be the antipode of `A` on the circumcircle of `AKL`. The factor-2 homothety centered at `A` maps `(O,M,N)` to `(X,B,C)`, so it suffices and is necessary to prove `XB=XC`.

Label `alpha=angle KBA=angle ACL`, `beta=angle LBK=angle LNC`, and `delta=angle LCK=angle BMK`. By Thales' theorem, `XK perpendicular AK` and `XL perpendicular AL`. The intended whole route applies the directed sine rule in `XBK`, `XBL`, `XCK`, and `XCL` to form an exact expression for `XB/XC`; then sine rules in the midpoint triangles `BMK`, `CNL` and the triangles cut out by the rays `BK,BL,CK,CL` should replace the side ratios. The desired cancellation leaves only `(2BM/AB)(AC/2CN)=1`, proving `XB/XC=1` and therefore the original claim.

The load-bearing open gap is the exact sine-product identity. The builder must state it before cancellation, including every side and directed sine; derive all angles from the three hypotheses and the two perpendicularities; and provide an accounting showing each non-midpoint side and sine occurs once in numerator and once in denominator. All divided sines require nonvanishing proofs from interiority and all ordinary-angle branch issues must be avoided with directed angles. If an extra scale or angle factor remains, record the approach as partial. Do not assume `B,C,K,L` cyclic or insert an unsupported similarity.
