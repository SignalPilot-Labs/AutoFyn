## imo-2026-02

oriented-determinant-elimination: advance
Target: Prove that the circumcentre `O` of `AKL` satisfies `OM=ON` under all the stated interior and angle hypotheses.
Technique: Oriented Cartesian coordinates and Cramer's rule, followed by exact polynomial-remainder/divisibility reduction (knowledge-base entries **Coordinates / complex / barycentric**, **Resultants / “transform the roots”**, **Minimal-polynomial reduction**, and **Trig identities**).
Skeleton:
  1. Normalize `A=(0,0)`, `B=(1,0)`, `C=q(cos gamma,sin gamma)` with `q>0`; define the positive angles `alpha=angle KBA=angle ACL`, `beta=angle LBK=angle LNC`, `delta=angle LCK=angle BMK` — by the given interiority and directed ray order.
  2. Derive the exact signed ray-intersection formulas `K=(1-r cos alpha,r sin alpha)`, `r=sin delta/(2 sin(alpha+delta))`, and `L=q e_gamma-u e_(gamma+alpha)`, `u=q sin beta/(2 sin(alpha+beta))` — by oriented determinants/Cramer's rule on the lines through `B,M,C,N`; prove `sin(alpha+beta),sin(alpha+delta)>0` and every selected ray parameter positive.
  3. Encode the remaining two incidences as `q=F(delta)` and `q^{-1}=F(beta)`, where `F(t)=[cos gamma-cos t cos(gamma+2alpha+t)]/[2 sin^2(alpha+t)]` — by taking exact cross products of the relevant line equations, with no unsigned-angle branch change.
  4. Linearize each incidence via the exact identity `2F(t)=(1+p_t^2)cos gamma+(cot(alpha+t)+p_t^2 cot alpha)sin gamma`, `p_t=sin alpha/sin(alpha+t)` — by the two product-to-sum identities `1-cos t cos(2alpha+t)=sin^2(alpha+t)+sin^2 alpha` and `cos t sin(2alpha+t)=(sin 2(alpha+t)+sin 2alpha)/2`.
  5. Write `(AKL)` as `Y·Y-UY_x-VY_y=0`; prove `[K,L] != 0`, solve for `(U,V)` by Cramer's rule, and reduce `OM=ON` exactly to `R=0`, where `R=2(|K|^2[C-B,L]+|L|^2[K,C-B])-(q^2-1)[K,L]` — by the certified determinant reduction.
  6. Display a hand-checkable remainder certificate: after substituting `q=F(delta)`, rewrite `R=(F(delta)F(beta)-1)Q` using the linear forms from Step 4, and verify the equality coefficient-by-coefficient in `cos gamma,sin gamma`; then the second incidence `F(delta)F(beta)=1` gives `R=0` — by exact polynomial divisibility, not CAS output or promised cancellation.
  7. Substitute `R=0` into the circle-centre calculation to conclude `OM^2=ON^2`, hence `OM=ON` — by nonnegativity of distances.
Key lemmas (claim + the one-line mechanism that makes it true):
  - The two remaining line incidences are `q=F(delta)` and `q^{-1}=F(beta)` — because taking oriented cross products removes the affine ray parameters and the displayed product-to-sum identities compress the result.
  - `R|_(q=F(delta))` is divisible by `F(delta)F(beta)-1` — because `R` is cubic in `q`, the first incidence performs a finite polynomial remainder reduction, and the two `F` expressions are linear forms in `(cos gamma,sin gamma)` after (L); the builder must supply the resulting short quotient and coefficient table.
  - `[K,L] != 0` — because otherwise `A,K,L` would be collinear and the stated circumcentre would not exist; this should be stated as part of the problem's nondegenerate meaning rather than silently divided out.
Open gaps: Step 6 is still unproved in olympiad-readable form. The exact CAS divisibility is discovery evidence only; the builder must produce a displayed compact quotient `Q` (preferably in `p_beta,p_delta`) and verify all coefficients. Steps 2-3 also require the previously omitted complete sign/ray-order derivation.
Cases to cover: General scalene case; `q=1`; possible vanishing coefficients in the linearized incidence forms; configurations with `X=K` or `X=L` are harmless here but no determinant or sine denominator may be divided out without justification.
Watch out for: Do not use the false cyclicity of `B,C,K,L`. One incidence alone leaves the genuine factor `F(delta)F(beta)-1`. Do not present tangent-half-angle CAS factorization or “terms pair” as proof. The cheap structural reduction to the antipode does not by itself close this coordinate route; no parity, extremal, or size argument applies.

reflected-circle-bilinear: new
Target: Prove that the circumcentre `O` of `AKL` satisfies `OM=ON` under all the stated interior and angle hypotheses.
Technique: Midpoint half-turns, directed-angle concyclicity, and parameter-free vector circle equations (knowledge-base entries **Synthetic toolkit**, **Coordinates / complex / barycentric**, **Reformulate**, and **Introduce a substitution**).
Skeleton:
  1. Put `A=0`, `B=b`, `C=c`, and define `D=b-k`, `E=c-l`, the reflections of `K,L` in `M=b/2,N=c/2` — by midpoint half-turns; thus `AKBD` and `ALCE` are parallelograms.
  2. Prove `A,C,K,D` cyclic and `A,B,L,E` cyclic — by directed angles: `angle ADK=angle(BK,MK)=alpha+delta=angle ACK`, with the symmetric equality at `E`; write the symmetric chain explicitly and justify every line direction from the parallelograms.
  3. Translate these two cyclicities into two exact low-degree equations `Phi_C(b,c,k,l)=0` and `Phi_B(b,c,k,l)=0` — by the determinant criterion for four concyclic points, substituting `D=b-k`, `E=c-l` before expansion.
  4. Write `(AKL)` as `y·y-u·y=0`; from `u·k=|k|^2` and `u·l=|l|^2`, identify the target residual `T=2u·(c-b)-(|c|^2-|b|^2)` — by expanding `OM^2-ON^2` with `O=u/2`.
  5. Establish and display an exact bilinear certificate `T=A(b,c,k,l)Phi_C+B(b,c,k,l)Phi_B`, after eliminating `u` only through its two circle equations — by oriented determinant algebra; check every dot-product/determinant coefficient and sign directly.
  6. Apply `Phi_C=Phi_B=0` to obtain `T=0`, hence `OM=ON` — by the distance-square identity.
Key lemmas (claim + the one-line mechanism that makes it true):
  - `(A,C,K,D)` and `(A,B,L,E)` are genuine cyclic quadrilaterals — because the midpoint reflections turn the original rays into parallel sides, so each prescribed sum of two angles becomes equality of directed angles subtending the same chord.
  - The target circle-centre residual lies in the span of the two reflected-circle residuals — because all three circle conditions are bilinear after `D=b-k,E=c-l`; the builder must give the exact multipliers, not merely claim ideal membership.
  - This route is parameter-free — because the half-turn variables absorb the midpoint constraints and the angle hypotheses are used only to establish cyclicity, avoiding all `F(beta),F(delta)` and sine denominators.
Open gaps: Steps 3 and 5: choose a concise determinant form for each cyclicity and derive the explicit coefficient-by-coefficient bilinear certificate. Step 2's second directed-angle chain must be written rather than called symmetric.
Cases to cover: Signs when `D,E` lie outside the original triangles; possible parallel auxiliary lines are avoided because no new intersections are introduced; noncollinearity of each three-point circle definition; `AB=AC` must remain included.
Watch out for: This is a genuinely different algebraic route only if it never reintroduces the old trigonometric `F` residual. Do not infer `B,C,K,L` cyclic. A CAS ideal-membership test may discover the certificate but cannot replace the displayed identity. The cheap kill is precisely the two one-move midpoint-reflection cyclicities; exploit them before expanding.

auxiliary-circle-centres: new
Target: Prove that the circumcentre `O` of `AKL` satisfies `OM=ON` under all the stated interior and angle hypotheses.
Technique: Linked cyclic quadrilaterals, radical axes/radical centre, and a final exact centre-vector calculation (knowledge-base entries **Synthetic toolkit**, **Circle/triangle configuration facts**, **Work backward**, and **Reformulate**). This adapts the crux of `aimo-0644` (midpoint homothety followed by radical-axis geometry) and `aimo-0525` (identify two common equal-power points to determine a radical axis), with every transferred fact to be proved here.
Skeleton:
  1. Define `Gamma_C=(CMK)` and `Gamma_B=(BNL)`, with centres `U,V`; define `Q=BK∩AC`, `R=CL∩AB`, and `P=BK∩CL` on extended lines — by construction, using directed lines throughout.
  2. Prove the linked cyclicities `B,L,N,Q`, `C,K,M,R`, and `B,C,Q,R` — by translating each of `alpha,beta,delta` into an equality of directed angles; explicitly settle the extension orientations.
  3. Use those cyclicities and power of a point to prove `Pow_Gamma_C(A)=Pow_Gamma_B(A)` and `Pow_Gamma_C(P)=Pow_Gamma_B(P)` — by writing both products on the relevant secants; conclude `AP` is the radical axis of `Gamma_C,Gamma_B` by the two-point characterization.
  4. Prove the centre relation `U+V=3O` — by constructing the relevant radical-centre/Miquel bridge from `Gamma_C,Gamma_B,(AKL)` and converting its perpendicular-bisector information into this vector identity; every intermediate common-power point must be named.
  5. In vectors based at `A`, write the exact centre equations `2U·(c-b/2)=|c|^2-|b|^2/4`, `2V·(b-c/2)=|b|^2-|c|^2/4`, and the equal-power equation `U·b-|b|^2/4=V·c-|c|^2/4` — by subtracting squared radii along the known points of each auxiliary circle.
  6. Add/subtract those three equations to obtain `(U+V)·(c-b)=3(|c|^2-|b|^2)/4`; insert `U+V=3O` to get `O·(c-b)=(|c|^2-|b|^2)/4` — by exact linear algebra.
  7. Expand `OM^2-ON^2=O·(c-b)+( |b|^2-|c|^2)/4=0`, hence `OM=ON` — by the midpoint identities.
Key lemmas (claim + the one-line mechanism that makes it true):
  - `AP` is the radical axis of the auxiliary circles — because `A` and `P` separately have equal secant-product powers after the three linked cyclicities are established.
  - `U+V=3O` — because the intended Miquel/radical configuration should determine the midpoint of `UV` on the line `AO` with the fixed ratio found numerically; this remains a conjectural load-bearing lemma and must be proved, not inferred from a diagram.
  - The two centre identities imply the target once the package is available — because subtracting their defining equal-distance equations gives the three displayed linear equations, whose exact combination has already been specified.
Open gaps: Steps 2-4, especially the precise proof of `U+V=3O`. Numerical tests support the package but certify nothing. The builder should abandon rather than overclaim if no named radical/Miquel chain proves Step 4.
Cases to cover: `BK parallel CL` (so `P` is at infinity: either use a projective/directed-power limiting formulation or split it off); `Q` or `R` on extensions; coincident/tangent auxiliary circles; `AB=AC`.
Watch out for: Equal powers determine a radical axis but not the sum of the centres; Step 4 needs an independent exact argument. Do not let a numerical centre relation masquerade as a theorem. The final linear identity has fixed factors `3` and `1/4`; sign errors there invalidate the route. The analogy to `aimo-0644`/`aimo-0525` is a strategy hint, not a citation.

half-turn-three-circle-miquel: new
Target: Prove that the circumcentre `O` of `AKL` satisfies `OM=ON` under all the stated interior and angle hypotheses.
Technique: Antipode homothety, midpoint half-turn circles, Miquel/radical-axis geometry, with a scale-aware spiral-similarity fallback (knowledge-base entries **Synthetic toolkit**, **Circle/triangle configuration facts**, and **Work backward**). This adapts `aimo-0389`'s crux of transporting an antipode through an actual spiral similarity, but here the correspondences and scale must be rebuilt from scratch.
Skeleton:
  1. Let `X` be the antipode of `A` on `(AKL)`; use the factor-2 homothety about `A` to reduce `OM=ON` to `XB=XC`, and record `XK perpendicular AK`, `XL perpendicular AL` by Thales — using the reviewer-certified reduction, with no division by `XK` or `XL`.
  2. Reflect `K,L` in `M,N` to points `D,E`; prove the parallelograms `AKBD`, `ALCE` and the directed cyclicities `(A,C,K,D)`, `(A,B,L,E)` — by the exact angle chains from the hypotheses.
  3. Introduce and name the second intersections of these two circles with the lines naturally through `K,L` and identify a common Miquel point for these circles and `(AKLX)` — by directed-angle equalities; the chosen intersections must be specified before any claim of Miquel concurrency.
  4. Use the resulting two common-power points to identify a radical axis passing through `X`, then prove that this axis is the perpendicular bisector of `BC` — by equal powers plus the parallelogram vector equalities; conclude `XB=XC`.
  5. If Step 4 is more naturally metric, replace it by composing the two circle-induced spiral similarities: use `AD=BK`, `DK=AK`, `AE=CL`, `EL=AL` as directed vector equalities to prove that the composite fixes `X`, maps `B` to `C`, and has scale `1`; then `XB=XC` — by similarity ratios, not angle equality alone.
  6. Transfer `XB=XC` back under the factor-2 homothety to conclude `OM=ON`.
Key lemmas (claim + the one-line mechanism that makes it true):
  - The two half-turn circles are valid — because reflection in each midpoint creates a parallelogram whose parallel sides convert the given angle sums into concyclicity.
  - A direct three-circle bridge can force `X` onto the perpendicular bisector of `BC` — because two explicitly identified common-power points determine the relevant radical axis; the points and power products are the missing content, not a generic invocation of Miquel.
  - Any spiral-similarity fallback has unit scale — because the parallelograms supply actual side equalities, repairing the scale defect of the dead naive similarity attempt; the exact product of ratios must be displayed.
Open gaps: Steps 3-5 are discovery gaps. The builder must either identify the exact Miquel/radical chain or a complete correspondence-and-ratio table for the composite similarity. Merely restating that such a relation is plausible is not progress.
Cases to cover: `X=K` or `X=L`; tangency/coincidence among auxiliary circles; directed orientations when reflected points lie outside; possible degeneration of a proposed second intersection.
Watch out for: Do not assume any extra cyclicity among `B,C,K,L,X`; generic tests refute simple candidates. One angle equality never proves a similarity scale. Exact equal-power identities and ratio signs are mandatory. This is the highest-variance route in the field and should be built only if the reviewer sees a concrete Step-3 opening.
