## Lemma (closed-form synthetic characterization of the fixed point Q)

**Setup.** Let `△ABC` be a triangle, `M,N` the midpoints of `AB,AC`, and
`Q` the point defined in `lemmas/amnq-concyclic-and-reduction.md` as the
reflection of `A` across the perpendicular bisector `ℓ` of segment `MN`.
Let `O_{ABC}` denote the circumcenter of `△ABC`.

**Theorem.** `Q` is exactly the foot of the perpendicular from `O_{ABC}`
to the line through `A` parallel to `BC`.

**Proof.** Place `A` at the origin (position vectors `B,C`). Since `M=B/2,
N=C/2`, the perpendicular bisector `ℓ` of `MN` is `{X: X·(N−M)=(|N|²−
|M|²)/2}`, i.e. `{X: X·(C−B)=(|C|²−|B|²)/4}` — a line perpendicular to
`C−B` (i.e. perpendicular to `BC`, hence `MN∥BC` too). Writing
`n̂:=(C−B)/|C−B|`, `c:=(|C|²−|B|²)/(4|C−B|)`, `ℓ=\{X·n̂=c\}`. The
reflection of `A=0` across `ℓ` is `Q=0−2(0·n̂−c)n̂=2c\,n̂ =
\frac{|C|²−|B|²}{2|C−B|²}(C−B)`.

Separately, the circumcenter (with `A=0`) satisfies `|O_{ABC}−B|=
|O_{ABC}−C|`, i.e. (expanding and cancelling `|O_{ABC}|²`)
`O_{ABC}·(C−B)=(|C|²−|B|²)/2`. Comparing,
`Q=\frac{O_{ABC}·(C−B)}{|C−B|²}(C−B)`, which is exactly the orthogonal
projection of `O_{ABC}` onto the line through the origin (`=A`) spanned by
`C−B` — i.e. the foot of the perpendicular from `O_{ABC}` to the line
through `A` parallel to `BC`. `∎`

**Independent numeric confirmation.** Computed both quantities (`Q` via
the reflection formula; the foot-of-perpendicular formula independently,
via the standard circumcenter formula for `O_{ABC}`) from raw coordinates
on 5 random triangles (own fresh Python/numpy session): `|Q − (\text{foot
of perpendicular})| < 5×10^{-16}` at every trial (machine precision).

## Relation to `spiral-similarity-bootstrap.md` (round 19)
That file introduces a point `P`, defined identically (foot of the
perpendicular from `O_{ABC}` to the line through `A` parallel to `BC`),
and proves `OM=ON ⟺ A,K,L,P` concyclic. **`P` and `Q` are literally the
same point** (both defined via the reflection of `A` in the perpendicular
bisector of `MN`, verified above and independently confirmed to machine
precision) — this closed-form characterization is the genuinely new
content of that round; the underlying reduction `OM=ON ⟺ concyclic(A,K,L,
Q)` (unconditional `iff`, no dependence on any problem-specific
hypothesis) was already latent in `lemmas/amnq-concyclic-and-
reduction.md`'s two lemmas (Lemma A, Lemma B) plus
`lemmas/vector-reduction-OM-ON.md`, both certified since round 1 — Lemma
B's proof is step-for-step reversible, so the full `iff` (not merely the
`⟹` direction as stated there) was already available, just not packaged
explicitly.

## Source
`results/imo-2026-02/approaches/spiral-similarity-bootstrap.md` (round 19,
"New result: the fixed point P", Step 3).

## Status
Certified.
