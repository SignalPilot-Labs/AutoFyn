## dyadic-reserve-induction — CHANGES REQUESTED

This is a whole-problem attempt and the dyadic construction is consistent with the strongest structural and small-case evidence. The drafting reduction and the identity \(P=(1+D)/2\) are sound. The route is viable, but the two central statements are not yet lemmas in a buildable form.

- Step 4 / dyadic reserve lemma: “adjacent sorted cancellation scale by scale” and “passing an unmatched reserve” do not define an invariant. The builder must state an induction hypothesis with explicit variables and show what happens when a cut is made at an arbitrary real location, including repeated cuts in one dyadic parent. Merely charging a cut to a scale is insufficient because one cut can create fragments that cross several ranks after sorting. A successful build must prove the claimed inequality for every refinement, not only for scale-aligned cuts.
- Step 5 / universal refinement lemma: the proposed “threshold fragment” mechanism is still only a description of the desired induction. The builder must specify which existing daughter/parent is cut, prove that the selected threshold lies inside it, show that the two residual states satisfy the strengthened hypothesis, and account for exactly one unit of cut budget. Provenance cannot be dropped. The statement should be formulated on the closure with nonnegative fragments if necessary, followed by a separate positive perturbation argument.
- Step 6: because legal Xiang marks are interior and distinct, an infimum response is enough for the upper bound, but the quantifiers must be explicit: for every Liu marking and every \(\varepsilon>0\), Xiang has a legal response giving payoff at most \(2^n/(2^{n+1}-1)+\varepsilon\); this rules out every larger guaranteed value. Do not claim Xiang necessarily attains the closed-polytope minimum.
- Step 1: replace the informal exchange with a clean backward-induction argument for the finite drafting game, and explain ties. The value is the odd-ranked sum even though optimal move sequences may not be unique.
- Step 7 should not be only a consistency check. Give the explicit arbitrary two-parent response for \(n=1\), including the one-parent case or explain how it is included in the general lemma.

Proceed only if the builder can make at least one of Steps 4 and 5 substantially precise; reproducing the present reserve language without a preserved inequality is not progress.

## threshold-parity-toggles — CHANGES REQUESTED

This is the strongest proposed route. It is a complete end-to-end plan, and Steps 2–4 provide a correct, useful exact reformulation: a split \(x=u+v\), \(u\le v\), toggles threshold parity on \((0,u]\cup(v,x]\) up to null endpoints. This representation exposes the actual geometry of a cut more precisely than the reserve outline. The main two parity lemmas nevertheless remain unproved.

- Step 5 / dyadic parity lemma: “crossing each dyadic boundary” is not yet a mechanism. State the induction object explicitly, such as a lower bound on odd measure in a specified scale interval together with the number of remaining realizable cuts. Prove the transition for all \(u,v\), not only endpoints aligned to powers of two. A toggle may increase or decrease odd measure according to its overlap with the current odd set.
- Step 6 / universal parity-covering lemma: the claimed charged layers of weights \(1,2,\ldots,2^n\) are not defined, and their asserted disjointness and lower bounds do not presently follow from greedy boundary cancellation. The builder must give an actual selection rule, identify the current piece being split at each step, and prove both realizability and the mass contradiction. An arbitrary symmetric difference with two intervals is not automatically a legal cut operation after earlier cuts.
- Repeated cuts need explicit treatment. After splitting a piece, a later toggle must use the length of one current daughter; it cannot reuse the original parent merely because the abstract threshold intervals have the desired endpoints.
- Step 1 must contain the rigorous minimax/backward-induction drafting argument, including tied lengths. Steps 6–7 must separately handle fewer Liu marks and the legal positive perturbation needed when a boundary cancellation asks for a zero fragment.
- The final answer must be stated explicitly and verified algebraically from \(D\le 1/Q\) and \(D\ge 1/Q\), where \(Q=2^{n+1}-1\).

The layer-cake and exact toggle identities are genuine proved-looking infrastructure, so this approach ranks above the reserve version. It is suitable for building provided the builder treats Steps 5 and 6 as the proof, rather than citing the current charging slogans.

## adjacent-matching-hall — RETHINK

The outline does not yet supply a viable Hall-theorem proof.

- Step 3 never defines the two vertex classes, adjacency relation, or the “unit” demands in a problem with arbitrary real lengths. Ordinary Hall's theorem from the knowledge base is discrete; the proposed continuous charging requires a capacitated measure/matching theorem that is neither stated nor derived.
- Steps 5–6 assert that failure of a greedy equal-fragment process yields a Hall-deficient set and then a binary growth chain, but neither implication has a mechanism. In particular, the process may consume more than \(n\) cuts, and an arbitrary low-cost matching does not by itself control the canonical adjacent sorted matching.
- Thus all load-bearing content is deferred to an undefined graph and an unsupported failure certificate. This is not a fixable omitted case; the proposed technique has not been connected to the refinement operation.

Do not register or build this slug. A future matching approach would need first to prove a precise uncrossing theorem for the canonical adjacent matching and formulate a finite or capacitated network whose capacities are exactly induced by legal cuts.

## polyhedral-minimax-certificate — RETHINK

The finite-chamber observation is correct for fixed \(n\), but the outline does not produce an all-\(n\) proof and its compression step is unsupported.

- Step 3 incorrectly jumps from “a linear objective attains an extremum at a vertex of each chamber” to “only recursively nested order types need be retained.” Vertex attainment does not imply that unexamined chambers can be discarded, nor does it provide a recurrence across \(n\).
- Steps 4–5 merely posit the required uniform dual multipliers and telescoping binary tree. No inequalities, multiplier formulas, or chamber recurrence are given. These assertions are essentially the desired upper and lower bounds restated in LP language.
- Finiteness for each fixed \(n\) is not a symbolic proof for arbitrary \(n\), and exhaustive chamber enumeration cannot serve as the requested olympiad argument.

Do not register or build this slug. LP computation may be used privately to discover an invariant or exact certificate, but a new outline should present that certificate explicitly before returning to the field.

## Ranking and selection

The two surviving approaches are new and were registered. Head-to-head, `threshold-parity-toggles` ranks above `dyadic-reserve-induction` because it already proves an exact layer-cake identity and an exact description of every legal split, whereas the reserve state is still undefined. Both are worth one build because they attack the same two-sided minimax claim through materially different invariants. The Hall and polyhedral slugs were cut and were not registered.

build set: threshold-parity-toggles, dyadic-reserve-induction