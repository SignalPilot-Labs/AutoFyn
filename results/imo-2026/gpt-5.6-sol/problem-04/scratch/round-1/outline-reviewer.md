## dyadic-multiples-and-thinness — CHANGES REQUESTED

This is a whole-problem route, and its sufficiency mechanism is sound. With the cut formula
\[
(x,b,1-b-x),\qquad (a-x,c,b+x),
\]
a grid mark \(kt\in(b,b+a)\) gives the legal choice \(x=kt-b\), so the two children contain the complementary positive multiples \(kt\) and \((n-k)t\). If a grid mark is on a cumulative-partition boundary, an original angle is already a positive multiple of \(t\). Splitting an angle \(kt\) into \(\lfloor k/2\rfloor t\) and \(\lceil k/2\rceil t\) then gives the stated recurrence and finite bound. The approach also addresses both directions of the requested characterization.

Required changes before this can become a proof:

1. **Step 5 must use nested finite-horizon sets.** Define
   \[
   W_0=\{\text{states containing }t\},\qquad
   W_{r+1}=W_r\cup\operatorname{Pre}(W_r),
   \]
   where \(\operatorname{Pre}(E)\) consists of states admitting one legal cut with both children in \(E\). As written, omitting \(W_r\) from \(W_{r+1}\) need not produce nested “win within \(r\)” sets. Prove both implications of “finite forced victory iff membership in some \(W_r\).” For the reverse implication, fix the strategy from the fixed initial state, form its binary response tree, and use König’s lemma to obtain a uniform depth for that one tree; do not infer a global depth over all initial states.

2. **Step 6 is load-bearing and is not yet specified enough to hand directly to a routine build.** The builder must state an inductively closed normal form for every affine line/cell in \(W_r\), not merely say that integer coefficients can be traced. For each selected vertex and each ordered pair of child line-types, write the two equations in \((a,b,x)\), including conditions inherited unchanged from a parent angle, and prove that their projection is contained in a proper parent line unless \(1=mt\) for a positive integer \(m\). The exceptional rank-deficient case must be calculated: it is essential to rule out more general relations such as \(p=mt\) with \(p>1\), zero or negative coefficients, or a dependence that is an identity for unrelated reasons. Strict legality \(0<x<a\) can only shrink a projection, but it must remain present in the formal predecessor definition.

3. **The finite-union assertion needs induction.** At fixed depth there are finitely many prior line-types, three vertex choices, and finitely many pairings, so there are finitely many projected pieces. State this explicitly. If projections are line segments or relatively open pieces rather than whole lines, containing each in a proper affine line is sufficient.

4. **The category conclusion should be elementary and relative to the open simplex.** Each proper affine line has empty interior and is nowhere dense there; hence the countable union over \(r\) cannot cover the open simplex. Alternatively, intersect with a suitably chosen transverse line and avoid countably many points. Then use the rank equivalence, rather than only the local complement property, to conclude that the chosen initial state defeats every purported finite-winning strategy.

5. **Sufficiency needs clean indexing and legality.** In the no-multiple case, cyclically orient the cumulative intervals so an interior mark \(kt\) lies in \((b,b+a)\), verify \(0<kt-b<a\), and note \(1\le k\le n-1\). For \(n=2\), the same construction gives two target angles immediately. If an original angle is \(kt\), its coefficient satisfies \(1\le k\le n-1\) because all triangle angles are positive.

The approach has been registered. It is the strongest build candidate because it supplies a complete constructive direction and a plausible, precise finite-rank route for necessity; the affine-thinness theorem remains the decisive gap.

## binary-tree-integer-certificate — RETHINK

This is not sufficiently distinct from `dyadic-multiples-and-thinness`: its necessity direction is the same finite-depth binary-tree elimination argument repackaged as “certificate extraction,” and its sufficiency direction is identical. More importantly, Step 3 currently assumes the difficult conclusion in the phrase “positive leaf multiplicities add.” General linear elimination can introduce subtraction, and the outline gives no invariant showing that the resulting coefficient of \(t\) is a positive integer while the coefficient of the total angle is exactly one. The claim that one combinatorial certificate type “persists on a nonempty open subfamily” is also unjustified when the chosen split can vary arbitrarily with the state; finite leaf labels do not by themselves make the associated projected set open.

Do not build this as a separate rival. Its useful tree interpretation should be incorporated into the affine-thinness lemma of the surviving approach: fix a finite labeled response tree, express all leaf target equations, and prove the required coefficient normal form through the explicit affine-cell induction. A genuinely distinct future certificate route would need an independently proved conservation identity on the whole binary tree that gives nonnegative integer weights without relying on the same predecessor-line classification.

## backward-affine-attractor — RETHINK

The mathematical direction is plausible, but this is the same whole route as `dyadic-multiples-and-thinness`, divided only by presentation: both use the same normalized transition, finite attractor layers, affine pullback/intersection/projection, rank-drop classification, Baire thinness, and the identical grid-fork construction. Registering both would create duplicate population members whose common unresolved lemma would rise or fall together.

Merge its useful details into the surviving slug: use nested layers, retain strict legality inequalities, prove fixed-depth finiteness of the affine-cell description, and explicitly compute the first predecessor. The advertised first-layer sanity check is correct for nonterminal parents: pairing the two possible target equations in the children yields either a selected parent angle \(2t\), the global relation \(2t=1\), or an illegal degenerate angle. But that check does not materially bypass the later coefficient-tracing theorem, so it does not justify a separate build.

## quotient-residue-safe-kernel — RETHINK

The proposed necessity argument is conjectural rather than an outline with a viable load-bearing mechanism. No safe set \(\mathcal S_t\) is given, and the response lemma is only phrased as something a “suitable forbidden-residue pattern should” ensure. Equality modulo \(t\) cannot distinguish the losing target angle \(t\) from other multiples of \(t\), while the game tests exact equality; arbitrary off-grid cuts also invalidate evidence from finite residue kernels. The outline itself acknowledges that rational and irrational cases may require unrelated constructions. Thus Steps 3–5 contain essentially the whole necessity proof, not a fixable omitted sublemma.

Do not register or build this slug. It can return only after an explicit nonempty target-free family is stated for every nonreciprocal \(t\), together with a proof that for every state in the family, every vertex, and every real legal split, at least one child remains in the family. Without that, substituting affine thinness would merely duplicate the surviving approach.

Only one approach survived registration, so no head-to-head Elo update was possible this round.

build set: dyadic-multiples-and-thinness