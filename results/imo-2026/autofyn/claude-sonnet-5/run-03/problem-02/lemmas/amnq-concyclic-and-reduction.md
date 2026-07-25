## Lemma A (A,M,N,Q concyclic)
Let ABC be a triangle, M, N the midpoints of AB, AC. Let ℓ be the
perpendicular bisector of segment MN and let Q := ρ(A), where ρ is the
reflection in ℓ. Then A, M, N, Q are concyclic (trivially so if Q=A, i.e. in
the isosceles case AB=AC, since then A itself is one of the four points).

### Proof
For the generic case Q≠A (equivalently AB≠AC): M, N, A are not collinear (M
lies on line AB, N on line AC, distinct lines, and M,N≠A since they are
midpoints of nondegenerate segments), so they determine a genuine circle ω
with some center O_ω. Since MN is a chord of ω, O_ω lies on the perpendicular
bisector ℓ of MN (the center of a circle is equidistant from the two
endpoints of any chord). Hence the reflection ρ in ℓ fixes O_ω and preserves
distances, so ρ(ω) = ω (same center, same radius). Also ρ swaps M and N (by
definition, ℓ is the perpendicular bisector of MN). Since A ∈ ω,
Q = ρ(A) ∈ ρ(ω) = ω. ∎

## Lemma B (Reduction: concyclic(A,K,L,Q) ⟹ OM=ON)
With Q as above and O the circumcenter of a triangle A,K,L (A,K,L not
collinear): if A, K, L, Q are concyclic, then OM = ON.

### Proof
If A,K,L,Q concyclic, all four lie on the unique circle through A,K,L, whose
center is O by definition; hence OA = OQ. So O lies on the perpendicular
bisector of segment AQ. For A ∉ ℓ (else Q=A, excluded below) and Q=ρ(A), the
perpendicular bisector of AQ is exactly ℓ (every point of ℓ is equidistant
from A, Q since ρ is an isometry fixing ℓ pointwise; conversely the midpoint
of AQ lies on ℓ with AQ⊥ℓ, by construction of a reflection). Since ℓ is by
definition the perpendicular bisector of MN, O lying on ℓ gives OM=ON. ∎

**Caveat (degenerate case A=Q, i.e. AB=AC):** this argument requires A∉ℓ, so
it does not cover the isosceles case; that case needs a separate argument
(not settled here — this is an explicitly open item, see
`results/imo-2026-02/current.md`).

## Source
`results/imo-2026-02/approaches/fixed-point-concyclic.md`, Lemmas 3 and 5.
Independently re-verified by proof-reviewer, round 1 (numerically on the
builder's own test instance, and by direct re-derivation of the reflection
argument). No gap found in either direction of this lemma pair.

## Status
Certified (with the stated isosceles-case caveat) — reusable by any approach
to imo-2026-02 that adopts the same Q. Note it only supplies a *sufficient*
condition (concyclic(A,K,L,Q) ⟹ OM=ON); the actual difficulty of the problem
is proving that hypothesis, which remains open.
