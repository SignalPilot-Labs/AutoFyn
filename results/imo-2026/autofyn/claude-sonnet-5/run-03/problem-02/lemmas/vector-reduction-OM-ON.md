## Lemma (Vector reduction of OM=ON)
Let ABC be a triangle, M, N the midpoints of AB, AC, and O any point in the
plane. Placing A at the origin (position vectors B, C for the other
vertices), for any point O with position vector also written O:
$$OM = ON \iff O\cdot(C-B) = \frac{|C|^2-|B|^2}{4}.$$

## Proof
M = B/2, N = C/2. Expand squared norms:
`OM² − ON² = (|O|²−2O·M+|M|²) − (|O|²−2O·N+|N|²) = 2O·(N−M) + |M|²−|N|²`.
Since N−M = (C−B)/2 and |M|²−|N|² = (|B|²−|C|²)/4,
`OM² − ON² = O·(C−B) + (|B|²−|C|²)/4`.
Since OM, ON ≥ 0, OM²=ON² ⟺ OM=ON. Setting OM²−ON²=0 and solving gives the
displayed equivalence. No hypothesis beyond M, N being the midpoints of AB,
AC is used; O is an arbitrary point. ∎

## Source
Independently derived and verified (2026-07-24) in all three of
`results/imo-2026-02/approaches/{fixed-point-concyclic,coordinate-bash,
power-of-point-secants}.md`. Certified by proof-reviewer, round 1: statement
correct as given, proof is a two-line polarization-identity computation with
no gap.

## Status
Certified — reusable by any future approach to imo-2026-02 (or any problem
with the same "OM=ON for midpoints M,N" target) without re-derivation.
