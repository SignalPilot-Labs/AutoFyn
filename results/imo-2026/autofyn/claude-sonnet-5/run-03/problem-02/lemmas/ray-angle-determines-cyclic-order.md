## Lemma (Ray-angle determines cyclic order on a circle)

Let `ω` be a circle and `A ∈ ω` a fixed point. For `P ∈ ω\{A}`, let `θ(P)`
denote the direction angle of ray `AP`. As `P` traverses `ω` once (starting
immediately after `A` in a fixed rotational sense, ending immediately
before returning to `A`), `θ(P)` is a strictly monotonic function of arc
position (increasing for CCW traversal), sweeping a net total angle of
exactly `π`. Consequently, the cyclic order of any finite set of points on
`ω\{A}` (starting from `A`) equals their order by increasing `θ`.

## Proof
By rotation/translation/scaling invariance, place `ω` as the unit circle,
`A=(1,0)`. For `P=(\cosφ,\sinφ)`, `φ∈(0,2π)`, `P-A =
2\sin(φ/2)(-\sin(φ/2),\cos(φ/2))` (half-angle identities), and since
`φ/2∈(0,π)` gives `\sin(φ/2)>0`, `P-A` is a positive multiple of
`(\cos(φ/2+π/2),\sin(φ/2+π/2))`, so `θ(P)=φ/2+π/2`, strictly increasing on
`(0,2π)`, ranging over `(π/2,3π/2)` (length `π`).

## Independent verification
The half-angle computation was re-checked by hand by the proof-reviewer
(round 3): `\cosφ-1=-2\sin²(φ/2)`, `\sinφ=2\sin(φ/2)\cos(φ/2)` are standard
identities, and the displayed factorization/direction-angle conclusion
follows directly — no gap found.

## Source
`results/imo-2026-02/approaches/ptolemy-trig-identity.md` (round 3, Lemma S1).

## Status
Certified — general-purpose tool (not specific to this problem's
configuration), reusable for determining cyclic order on any circle via
ray-angles from a fixed point on the circle.
