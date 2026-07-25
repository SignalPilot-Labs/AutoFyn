## Theorem (`Q` as the intersection of two elementary lines, simplifying the circumcenter characterization)

**Setup.** Let `\triangle ABC` be a triangle, `M,N` the midpoints of `AB,AC`,
`O_{ABC}` its circumcenter, and let `Q` be the fixed point (already
certified, `lemmas/q-as-foot-of-perpendicular-from-circumcenter.md`)
defined as the foot of the perpendicular from `O_{ABC}` onto the line
through `A` parallel to `BC`; equivalently (already certified,
`lemmas/amnq-concyclic-and-reduction.md`), placing `A` at the origin and
writing `B,C` for the position vectors of the other two vertices,
`$Q=\dfrac{|C|^2-|B|^2}{2|C-B|^2}(C-B)$`.

**Theorem.**
$$Q=(\text{line through }A\text{ parallel to }BC)\ \cap\
(\text{perpendicular bisector of }BC),$$
and consequently `QB=QC` and `AQ\parallel BC`.

**Proof.** With `A` at the origin, the two lines are
`\ell_A:=\{t(C-B):t\in\mathbb R\}` and `\ell_{BC}^\perp:=\{X:X\cdot(C-B)=
\tfrac12(|C|^2-|B|^2)\}` (the standard equidistant-locus description: `X`
equidistant from `B,C$ iff `|X-B|^2=|X-C|^2` iff `X\cdot(C-B)=\tfrac12
(|C|^2-|B|^2)`). These two lines are not parallel (their direction vectors
are `C-B` and a vector orthogonal to `C-B`, coinciding only if `C=B`,
excluded), so they meet in exactly one point. Direct substitution of the
closed form for `Q` shows `Q\in\ell_A` (take `t=(|C|^2-|B|^2)/(2|C-B|^2)`)
and `Q\cdot(C-B)=\tfrac{|C|^2-|B|^2}{2|C-B|^2}(C-B)\cdot(C-B)=
\tfrac12(|C|^2-|B|^2)`, i.e. `Q\in\ell_{BC}^\perp`. By uniqueness of the
intersection point, `Q=\ell_A\cap\ell_{BC}^\perp`. `\blacksquare`

**Where proved.** `results/imo-2026-02/approaches/spiral-similarity-bootstrap.md`, "Round 20" entry (part (a)).

## Independent verification (proof-reviewer, round 20)
Own fresh `numpy` session (random `B,C\in\mathbb R^2`, 3 samples, not
reusing the file's script): computed `Q` via the closed form and
independently confirmed `|Q-B|=|Q-C|` to 14+ digits and
`Q\cdot(C-B)=\tfrac12(|C|^2-|B|^2)` exactly (both sides agree to the
displayed float precision) at every sample — confirms the perpendicular-
bisector membership; membership in `\ell_A` is immediate from the closed
form (`Q` is by construction a scalar multiple of `C-B`). This is an
elementary, fully rigorous vector-algebra fact with no gap.

**Certified.** Strictly simplifies the existing certified `Q`
characterization (no circumcenter arithmetic needed to derive `QB=QC` or
`AQ\parallel BC`); reusable by any future angle-chase attempt on this or
other synthetic approaches.
