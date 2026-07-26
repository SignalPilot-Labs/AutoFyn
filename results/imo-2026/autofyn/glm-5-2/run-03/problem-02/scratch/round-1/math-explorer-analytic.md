## imo-2026-02  (analytic / coordinate / computational route)

- **Distinct openings** (each a rival slug the outliner can build):
  1. **Cartesian + tangent-parametrization + Groebner on general triangle.** A=(0,0), B=(2,0), C=(2p,2q) so M=(1,0), N=(p,q). Parametrize K,L by angle tangents (t_a,t_b,t_g) via ray-intersection (see below). Two residual angle equations at M,N. Clear denominators of OM²−ON² and reduce the numerator modulo the ideal (n1,n2). *Symbolically VERIFIED for the special right-isoceles triangle p=0,q=1* (Groebner lex on (tg,tb,ta): 2 basis polynomials, 268-term numerator → remainder **0**). General p,q: the setup itself blows up sympy `cancel/simplify` on K,L (timed out at 9 min just constructing expressions) — so the 5-variable Groebner is the honest gap.
  2. **Cartesian + tangent-parametrization + resultant elimination** (avoids 5-var Groebner). Treat (p,q,t_a) as parameters; eliminate (t_b,t_g) by computing the resultant of the two residual equations w.r.t. (t_b,t_g), then check the resultant divides the numerator of OM²−ON². Smaller polynomial objects than full Groebner; the realistic tractable path for the general case.
  3. **Complex-bash.** A=0, B=2 (real), C=2z complex. Angle equalities become `arg`-conditions (a ratio is real / has a prescribed argument); circumcenter via `o·k=|k|²` style linear solve in complex form; target `|o−1|=|o−z|`. Circumcenter formula in complex is the messy point. Worth one slug because angle encoding is cleanest here.
  4. **Barycentric w.r.t. ABC.** M=(1:1:0), N=(1:0:1) trivial; but circumcenter of the sub-triangle AKL has no clean barycentric form. Likely inferior — listed only to flag it as probably-dead.
  5. **Trig-Ceva / pure-trig form** (boundary of analytic). The angle chain α=∠KBA=∠ACL, β=∠LBK=∠LNC, γ=∠LCK=∠BMK with ∠LBA=α+β, ∠ACK=α+γ and M,N midpoints is exactly the input trig-Ceva consumes. A trig-identity slug showing O lies on the perp-bisector of MN. Hybrid synthetic+trig.

- **Candidate technique(s):** angle-parametrization by tangent (rationalizes all trig), ray-intersection for K,L, linear circumcenter solve, polynomial ideal-reduction (Groebner or resultant). KB entries: `Coordinates / complex / barycentric` (§Geometry), `Synthetic toolkit` (trig cevians Ceva/Menelaus), `Trig identities & interval intersection`. KB geometry section is thin — most machinery must be built in-slug.

- **Cheap-kill candidates:**
  - OM=ON ⟺ O on line `2(p−1)Ox + 2q Oy + 1 − p² − q² = 0` (a fixed line parallel to perp-bisector of BC, through (B+C)/4). Reduces target to a linear collinearity check — halves the work.
  - Circumcenter O of AKL with A=0 satisfies `2 O·K = |K|²`, `2 O·L = |L|²` — a 2×2 linear solve, no quadratic.
  - The 3 angle-equalities are not 3 independent constraints on (K,L): in the tangent-parametrization they are *baked into the construction* (K,L built FROM α,β,γ), leaving only the 2 midpoint-angle conditions as actual equations → 1-parameter family, conclusion is an identity on that curve.
  - Sign/orientation pitfall (see Dead ends): equating *oriented* tangents `cross/dot` produces the wrong (larger) variety; must use the parametric construction that fixes orientation, or squared tangents.

- **Knowledge-base entries to use:** `Coordinates / complex / barycentric`; `Synthetic toolkit` (angle chasing, trig cevians); `Trig identities & interval intersection`. No dedicated circumcenter/coordinate-bash lemma exists in KB — the proof must derive the circumcenter linear-solve identity from scratch and cite it as "standard".

- **Analogous past problems (cruxes):** **none** — `crux_moves_documentation.md` states the corpus has *no geometry cruxes* (only number_theory / combinatorics / algebra). Do not expect a retrieved geometry crux.

- **Prior progress:** none in workspace (round 1, empty). This explorer established (conjecture→now-evidence): the configuration is a genuine 1-parameter family and OM=ON holds on all of it.

- **Dead ends (do not retry):**
  - **Equate oriented tangents as 3 equations in (kx,ky,lx,ly)** (`cross·dot − cross·dot=0`): produces the wrong variety (captures α=β+π branches), Groebner remainder of OM²−ON² is NONZERO (16-term remainder for right-isoceles). Do not use this ideal; the parametric construction is required.
  - **Direct 4-unknown (kx,ky,lx,ly) Groebner** with the 3 oriented-tangent equations: also wrong variety, and anyway slow.
  - **General-triangle full 5-var (p,q,ta,tb,tg) Groebner via sympy `cancel/groebner`**: setup timed out at 9 min just simplifying K,L. Do NOT attempt naive lex Groebner on 5 vars; use the resultant-elimination opening (2) or split the elimination.

- **Small-case / intuition notes (CONJECTURES, labeled):**
  - *Conjecture (strong numeric evidence):* For a scalene triangle A=(0,0), B=(2,0), C=(1,2.5), solving the 2 midpoint-angle equations for (β,γ) at α ∈ {0.15,0.25,0.40,0.55,0.70,0.90} gives OM²−ON² ≈ 0 (≤1e-10) throughout — the 1-parameter family is real and the identity holds on all of it.
  - *Proved (special case):* right-isoceles A=(0,0),B=(2,0),C=(0,2): symbolic Groebner reduction gives remainder exactly 0. This is a complete proof for that one triangle shape, not the general theorem.
  - *Circumcenter formula bug warning:* the linear system is `[[2Kx,2Ky],[2Lx,2Ly]]·[Ox,Oy]ᵀ = [|K|²,|L|²]` — ROWS are K and L (not columns). A transposed matrix silently gives wrong O and false-negative OM²−ON²; verify `|OK|=|OL|=|OA|` before trusting any reduction.
  - *Degree-of-freedom summary:* K,L = 4 unknowns; 3 angle-equalities (correctly oriented) + 2 containment-inequalities → 1-param solution family; the conclusion OM=ON is an algebraic identity on that family, so an ideal-reduction (Groebner/resultant) is the natural proof shape.
  - *Where algebra blows up:* (i) the general-triangle K,L rational expressions in (p,q,t_a,t_b,t_g); (ii) the numerator of OM²−ON² after clearing the circumcenter determinant (268 terms already in the special case). The resultant route keeps these smaller than full lex Groebner.
