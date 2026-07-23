## Lemma: Antipode reduction of OM=ON to A*B=A*C

**Source approach:** antipode-perp-bisector (round 2). Certified by
proof-reviewer, round 2 (independently re-derived vector algebra and Thales
argument from scratch; confirmed correct, no gaps).

### Statement
For a triangle `ABC` with `M`, `N` the midpoints of `AB`, `AC`, and any
circle `Γ` through `A` with center `O`, let `A* := 2O − A` (the antipode of
`A` on `Γ`, i.e. the reflection of `A` through `O`; since `O` is the center
of `Γ`, `A*` is the second intersection of line `AO` with `Γ`). Then:

1. **(Vector identity, no circle/angle hypotheses needed.)**
   `A*−B = 2(O−M)` and `A*−C = 2(O−N)`, hence `|A*B| = 2·OM`,
   `|A*C| = 2·ON`, and therefore
   $$OM = ON \iff A^*B = A^*C.$$
2. **(Thales / synthetic characterization of `A*`.)** If `K, L ∈ Γ`,
   `K,L ∉ {A,A*}`, then `∠AKA* = ∠ALA* = 90°` (angle inscribed in the
   semicircle on diameter `AA*`), so `A*` lies on the line through `K`
   perpendicular to `AK` and on the line through `L` perpendicular to `AL`.
   If `A,K,L` are not collinear, these two perpendiculars are non-parallel
   and meet in exactly one point, so
   $$A^* = (\text{line through }K\perp AK)\ \cap\ (\text{line through }L\perp AL),$$
   a characterization making no reference to `O` or `Γ`'s center.

### Proof
*(1)* Since `M=(A+B)/2`: `A*−B = (2O−A)−B = 2O−(A+B) = 2(O−M)`, so
`|A*−B| = 2|O−M| = 2·OM`. Identically with `N=(A+C)/2` for `C`. Both `OM,ON`
nonnegative, so `OM=ON ⟺ 2OM=2ON ⟺ A*B=A*C`.

*(2)* `A* ∈ Γ` since `|O−A*|=|O−A|=R`; `O` is the midpoint of `AA*` (by
definition of `A*`), so `AA*` is a diameter of `Γ`. For `K ∈ Γ`: `OK=OA=OA*=R`
makes triangles `OAK`, `OA*K` isosceles, so `∠OAK=∠OKA=:x`,
`∠OA*K=∠OKA*=:y`. Since `O` lies on segment `AA*`, `∠AKA* = ∠OKA+∠OKA*=x+y`.
The angle sum of triangle `AKA*` gives `∠KAA*+∠AA*K+∠AKA* = 180°`, i.e.
`x+y+(x+y)=180°`, so `x+y=90°`, i.e. `∠AKA*=90°`. Identically for `L`. The
perpendicularity gives the two lines through `K,L`; since `AK ∦ AL` (as
`A,K,L` form a genuine triangle, being distinct points on `Γ` with `A,K,L`
not collinear), the perpendiculars to two non-parallel lines are themselves
non-parallel, so they meet in a unique point, forced to be `A*`. ∎

### Status and scope
Fully general (no dependence on this problem's specific angle hypotheses).
Reusable for any problem relating a circumcenter to the midpoints of two
sides from a shared vertex. In this problem's specific application
(`Γ = circumcircle(AKL)`), this reduces `OM=ON` to showing the point `A*`
(defined purely from `K,L,A` via the two perpendiculars above, no reference
to `O`) satisfies `A*B=A*C`, i.e. lies on the perpendicular bisector of `BC`.
**This reduction is complete and gap-free; proving `A*B=A*C` from the three
angle hypotheses of the problem is a separate, still-open task** — see
`approaches/antipode-perp-bisector.md` for the (still open) remaining work
and three refuted mechanisms that should not be re-attempted verbatim.
