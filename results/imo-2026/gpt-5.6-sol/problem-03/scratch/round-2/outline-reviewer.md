## subset-folding-dyadic-frontier — CHANGES REQUESTED

This is a whole attempt and its Xiang Yu half has a credible, nearly complete mechanism, but the builder must not present the Liu Bang half as proved merely by naming a “loaded frontier invariant.”

- **Step 1:** The draft reduction is sound only after explicitly proving that taking a currently longest piece is optimal at every turn. Since taking a piece does not alter later options, an exchange argument gives Liu the odd sorted ranks and Xiang the even sorted ranks; ties do not affect the total. State the alternating-discrepancy formula with the parity convention carefully.
- **Step 3 / Dyadic refinement lemma:** This is the decisive gap. The proposed mechanism (“each scale has unit excess” and “a split discharges only one ancestry-tagged obligation”) is not yet an invariant: neither a frontier state nor its update under an arbitrary split is defined, and global sorted rank can interleave descendants of many parents. Repeated cuts in one ancestry are exactly the obstruction. The builder must first state a quantified invariant and prove its preservation for every split; otherwise this approach remains partial. Numerical sanity checks for n≤5 support the lemma but do not prove it.
- **Steps 5–8 / Xiang construction:** The split count is plausible but needs exact bookkeeping. For a nonempty positive and negative support of total size s, the common-refinement construction has at most s−2 relevant interior boundaries, not merely a loose unexplained count; adding |Z| halvings leaves at most m−2 cuts, so there is room to split the residual if needed. The builder must give one uniform construction for unequal totals, zero residual, one empty sign class, and coincident boundaries. Do not assert that “equal pairs plus one residual” has payoff (1+r)/2: its total mass is 2P+r=1, so the payoff is P+r=(1+r)/2; this calculation should be written explicitly.
- **Step 5:** The separate m≤n claim is underspecified and, as phrased, invokes an undefined folding construction without first obtaining a signing. A cleaner route is to pad the m parent lengths by n+1−m zeros, apply the same subset-sum argument, then convert zero coordinates/boundary cuts to legal limits. If zeros are not used, supply a complete independent cancellation argument and cut count.
- **Step 8:** A legal-mark approximation must preserve the bound in the correct minimax sense. For every ε>0 construct distinct interior Xiang marks with payoff at most c_n+ε; then any purported guarantee g>c_n is defeated by choosing ε<g−c_n. Explain continuity of the odd-rank sum (equivalently its expression through order statistics) under perturbation. Existing Liu marks cannot be reused.
- **Step 9:** The stated equality refinement is inaccurate: halving parents 2,4,…,2^n creates two copies of 1,2,…,2^{n−1} together with the original 1, whose discrepancy is 1. State this correctly and normalize by T.

What to change: build the already strong Xiang half rigorously and make a serious attempt at a fully formal dyadic invariant. If no invariant surviving arbitrary repeated cuts and global reordering can be written, record the approach as partial rather than filling the gap with prose.

## threshold-profile-loaded-induction — RETHINK

Steps 1–3 are exact and useful, but this is not presently a buildable whole proof. Step 4 is the same unresolved dyadic lower theorem as in `subset-folding-dyadic-frontier`, only translated into symmetric-difference language, while Step 5 adds a second, harder universal upper theorem with no precise inductive statement. “Equal-child cancellation and cross-parent prefix cancellation” does not imply the claimed legal profile reduction, because toggles are constrained by ancestry and the residual interval’s location matters. The outline itself acknowledges both theorems are conjectural. Thus this candidate shares the leader’s main wall and adds another wall; it does not provide useful field diversity this round.

What to change: do not build this slug now. It can be revived only after specifying a profile-valued induction hypothesis (including interval locations and remaining per-ancestry cut structure) and checking every legal-toggle transition. The exact identities in Steps 2–3 may instead inform the selected approach’s lower-bound lemma without registering a duplicate whole route.

## rank-word-polyhedral-minimax — RETHINK

The rank-cell LP encoding in Steps 1–3 is plausible, but the two statements that would solve the problem are wholly unproved: Step 4 asks for a dual certificate for every admissible rank word, and Step 5 asks for a recursive primal cover of the entire parent simplex. The suggested mechanisms (“compress the word” and “first violated dyadic ratio”) do not specify a valid recursion, its cases, or feasibility updates. These are not isolated fillable lemmas; they amount to the complete lower and upper bounds in a much heavier language. The closure argument cannot rescue absent primal cells or dual certificates.

What to change: return to exploration. This route becomes buildable only if an explicit certificate transformation and explicit simplex-region recursion are already formulated and verified, at least symbolically in general n. Finite n computation is evidence, not a mechanism.

## recursive-extremal-splitting — RETHINK

This approach is circular at its load-bearing point. Step 3 says to “choose” a reserve state G so that a desired two-branch recurrence holds, but no definition of G or valid decomposition is given. Global rank pairing generally does not decompose by parent ancestry, so the recurrence asserted in Steps 4–6 is precisely what must be proved, not a consequence of homogeneity or extremality. The claimed simplex theorem and uniqueness of dyadic ratios therefore have no foundation.

What to change: abandon this outline unless exploration first discovers a concrete state whose terminal value equals the globally sorted alternating discrepancy and proves the first-split recurrence in all interleaving cases. The cited induction pattern is only an analogy and cannot justify the decomposition.

## Field assessment and ranking

Only `subset-folding-dyadic-frontier` survives the gate and is registered. The other three new slugs are cut and are not registered, so the population has fewer than two approaches and no pairwise Elo update is possible. The field is not genuinely diverse at the viable level: the subset/frontier and threshold/profile candidates share the same unproved dyadic lower bound, while the LP and recursive candidates merely restate both minimax halves as larger conjectural structures. The next scouting round should challenge the dyadic-gap framing rather than propose another encoding of it.

build set: subset-folding-dyadic-frontier
