## oriented-determinant-elimination — CHANGES REQUESTED

This is a whole end-to-end attempt, and it remains the strongest route in the field. Unlike the round-1 quarter-turn and sine-product promises, its decisive implication has now been checked as an exact rational-function divisibility after imposing both incidence equations: substituting `q=F(delta)` leaves a factor `F(delta)F(beta)-1`, which the second incidence kills. Thus the technique is capable of proving the claim and is not circular.

Before this can be treated as a buildable proof skeleton rather than computational evidence, the builder must close the following load-bearing items.

1. **Step 6 must contain the actual certificate.** The outline currently asks the builder to “display” a quotient `Q` and coefficient table but does not give them. A bare appeal to degree, linearity in `cos gamma,sin gamma`, or CAS divisibility is insufficient. The build must exhibit a compact exact identity for `R|_{q=F(delta)}` and verify it term by term. If the quotient in the proposed `p_beta,p_delta` variables does not become short enough to check by hand, the builder must leave this as an explicit gap rather than call it telescoping.
2. **Steps 2–3 need complete directed-ray derivations.** Derive each line direction from `K` and `L` being interior to the stated triangles/angles, show `alpha,beta,delta>0`, establish the relevant sums lie in `(0,pi)`, and hence justify positivity/nonvanishing of every sine denominator and ray parameter. The formulas for `K,L,F(beta),F(delta)` may not simply be imported from exploratory algebra.
3. **Step 5 must avoid a semantic nondegeneracy shortcut.** The existence of “the circumcentre of triangle `AKL`” is normally understood to imply `A,K,L` are noncollinear, but the build should explicitly invoke that convention before dividing by `[K,L]`; otherwise formulate the circle-centre equations without an unexplained division.
4. **Exceptional-looking algebraic cases must remain covered.** In particular, `q=1` and vanishing coefficients of either linear incidence equation are not separate exclusions: the displayed polynomial identity must remain valid without division by those coefficients. No division by the quotient or by `F(t)` is permitted except where `q>0` and the incidence itself proves it nonzero.

Build direction: first derive the compact quotient/certificate on scratch paper; only then spend prose on the full sign derivation. If only the hundreds-of-monomials half-angle certificate is available, report partial rather than laundering CAS output into an olympiad proof.

## reflected-circle-bilinear — RETHINK

The reflected-point cyclicities are promising and appear genuinely valid, but the proposed endpoint in Step 5 is not supported and is in fact false at the level stated. Writing `A=0`, normalizing `B=(1,0)`, setting `D=B-K` and `E=C-L`, and forming the two standard four-point concyclicity polynomials `Phi_C` and `Phi_B`, an exact symbolic Gröbner reduction of the certified target determinant residual modulo `<Phi_C,Phi_B>` leaves the target residual unchanged and nonzero. Therefore the target residual is not a polynomial consequence—let alone a bilinear linear combination—of just these two cyclicities for unrestricted `B,C,K,L`.

This reveals the structural issue: the two half-turn cyclicities encode only two combinations of the three original angle equalities; they discard additional orientation/angle data needed for the conclusion. “All three circle conditions are bilinear” is neither a mechanism nor sufficient for ideal membership. Step 5 cannot be filled as requested from `Phi_C=Phi_B=0` alone.

Do not register this slug. A viable revision would have to identify and retain a third exact condition coming from the omitted angle equality, then display or computationally validate a concrete identity using all three conditions. That would be a materially revised whole route, not the present two-equation certificate.

## auxiliary-circle-centres — RETHINK

This is nominally a whole attempt, but its decisive Step 4 is only a numerical conjecture. The statement `U+V=3O` is much stronger than the radical-axis facts preceding it, and equal powers at two points determine the line of centres only up to perpendicularity to a radical axis; they do not determine the vector sum of the centres. The phrase “constructing the relevant radical-centre/Miquel bridge” does not name any points, circles, power equalities, ratio, or theorem that yields the factor `3`, so it is an unverified hand-off rather than a mechanism.

Steps 2–3 also require proof, and the case `BK parallel CL` makes the proposed second equal-power point `P` unavailable in ordinary Euclidean power geometry. More importantly, even proving `AP` is the radical axis would not close Step 4. Do not register or build this route until an explicit construction proves `U+V=3O` (or replaces it with a weaker exact centre identity sufficient for the target), including the parallel case without an informal projective limit.

## half-turn-three-circle-miquel — RETHINK

This outline consists of a correct certified prefix followed by a discovery request. Steps 3–5 do not specify the alleged second intersections, common Miquel point, two common-power points, radical axis, or spiral-similarity correspondence. The fallback is equally underdetermined: the parallelogram side equalities do not by themselves show that a composite similarity fixes `X`, maps `B` to `C`, or has unit scale. Those are precisely the theorem-sized conclusions that must be established.

This route also substantially duplicates the reflected-circle opening through Step 2 while offering two speculative alternatives for the same missing bridge, neither with a mechanism. Do not register it and do not branch/copy an existing antipode approach into it. It can return only after reconnaissance identifies a concrete three-circle incidence or a complete image-and-ratio table, with degeneracies handled.

## Ranking gate

The full existing population was compared. `oriented-determinant-elimination` ranks above `antipode-quarter-turn` because it has an explicit certified residual and new exact divisibility evidence, while the quarter-turn route still merely promises the same cancellation. `antipode-quarter-turn` ranks above `sine-product-antipode` because both share the antipode reduction but the latter is recorded only partial and retains an extra angular factor. `sine-product-antipode` ranks above `inverted-circle-intercepts` because it at least has a certified endpoint reduction, whereas the inversion route remains unbuilt and its nonlinear intercept lemma is unsupported. These comparisons clear all stale round-1 outcomes. No new approach survived the gate, so no registration or copy was performed.

build set: oriented-determinant-elimination