## imo-2026-03

subset-folding-dyadic-frontier: new
Target: Prove for every positive integer n that the largest guaranteed share is c_n=2^n/(2^{n+1}-1), by giving Liu Bang dyadic marks and giving Xiang Yu a matching response to every Liu marking.
Technique: Pigeonhole on subset sums plus constructive interval-overlay pairing for Xiang Yu; superincreasing/dyadic frontier invariant for Liu Bang. This adapts the fixed-pair-with-one-exception move of `aimo-0596` and the distinct-dyadic-scale charging move of `aimo-0019`.
Skeleton:
  1. Reduce the claiming phase to descending order: under optimal play each turn takes a longest remaining piece, so Liu receives odd sorted ranks; for final lengths w_1>=...>=w_q his share is (1+D)/2, where D=w_1-w_2+w_3-... (append a zero when q is even) — by backward induction and total length 1.
  2. Let Liu use n marks giving consecutive parent lengths 1,2,4,...,2^n, normalized by T=2^{n+1}-1 — explicit construction.
  3. Prove the dyadic refinement lemma: every refinement of {1,2,4,...,2^n} obtained with at most n binary splits has sorted alternating discrepancy at least 1 — by a loaded superincreasing frontier invariant: at each dyadic level retain the unmatched excess 2^k-(1+2+...+2^{k-1})=1, and charge each split to at most one frontier level; repeated cuts of one parent must be handled by ancestry rather than by assuming one cut per level.
  4. Conclude from Steps 1–3 that Liu guarantees (1+1/T)/2=2^n/T.
  5. For Xiang's converse, first handle a Liu partition with m<=n parents: if m<=n, use at most m-1 cuts in the folding construction below to obtain equal pairs plus one residual, then use one spare cut to halve the residual, giving only equal pairs and hence Liu exactly 1/2; thus only m=n+1 can be extremal.
  6. For m=n+1 parent lengths a_1,...,a_m, order all 2^m subset sums in [0,1]; two consecutive sums differ by r<=1/(2^m-1). Cancel their common indices to obtain disjoint sign classes P,N and zero class Z with |sum_P a_i-sum_N a_i|=r — by the pigeonhole principle.
  7. Physically realize this signing: lay the P-parents and N-parents end-to-end as two abstract piles, overlay the shorter pile on the longer, and cut at the union of cumulative boundaries. Every overlap cell then occurs once on each side, while the longer pile has one residual interval of length r. Halve every zero-sign parent. Count the genuinely new cuts as at most (|P|+|N|-1)+|Z|=m-1=n — by common-refinement boundary counting.
  8. The resulting multiset consists of equal pairs plus one residual r; hence the descending draft gives Liu one member of every pair and the residual, i.e. (1+r)/2<=2^n/T. If a boundary is degenerate, coincides with an existing mark, or creates a zero piece, perturb the construction so the payoff is at most 2^n/T+epsilon; this suffices to rule out every guarantee larger than 2^n/T.
  9. Combine the matching inequalities and state c_n=2^n/(2^{n+1}-1), checking n=1 and the equality refinement obtained by halving 2,4,...,2^n.
Key lemmas (claim + the one-line mechanism that makes it true):
  - Dyadic refinement lemma: n arbitrary splits of {1,2,...,2^n} leave D>=1 — because each scale has exact unit superincreasing excess, and a split can discharge only one ancestry-tagged frontier obligation; this is the main unproved lemma.
  - Subset-sum signing lemma: n+1 masses admit a nonzero {-1,0,1} signing of magnitude at most 1/(2^{n+1}-1) — because 2^{n+1} subset sums create 2^{n+1}-1 adjacent gaps in an interval of length 1.
  - Folding realization lemma: a disjoint signed support of size s can be converted into equal pairs plus its signed residual using at most s-1 cuts — because the union of the two piles' internal cumulative boundaries gives a common interval refinement, and each new boundary cuts only its containing parent.
  - Pair payoff lemma: equal pairs plus residual r give Liu (1+r)/2 — because descending order places the two copies of every positive length in consecutive ranks, while the sole unmatched mass contributes r.
Open gaps: Step 3 is the hard load-bearing gap and needs a fully stated frontier invariant robust to multiple cuts in one parent. Step 8 needs a precise epsilon/infimum argument. The folding cut count in Step 7 should be written carefully when one sign class is empty (then either r=0 or use the spare-cut/degenerate case directly).
Cases to cover: Liu uses m<=n parents versus m=n+1; fewer than n Xiang marks; zero residual versus positive residual; empty sign class; coincident overlay boundaries; ties among final lengths; n=1.
Watch out for: Do not claim that discrepancy itself is monotone under splitting. Do not assume one Xiang cut per dyadic parent. Marks must be distinct and interior, so limiting zero pieces are not literal legal moves. The cheap structural kill succeeds for Xiang's half (subset-sum pigeonhole plus folding), but no plain parity or smallest-parent bound is sharp for Liu's half.

threshold-profile-loaded-induction: new
Target: Prove for every positive integer n that c_n=2^n/(2^{n+1}-1), using the odd-threshold profile as the common state for both players.
Technique: Layer-cake double counting and Boolean interval algebra, followed by profile-valued structural induction; this adapts the threshold decomposition move surfaced via `aimo-0127` and the loaded-reserve principle of `aimo-0340`.
Skeleton:
  1. Reduce optimal claiming to odd sorted ranks as above and define E={t>0: the number N(t) of final pieces of length at least t is odd}.
  2. Establish D=|E| by integrating the parity indicator of N(t) across the intervals between consecutive piece lengths — layer-cake/double counting.
  3. Establish the exact local move: splitting x into a and x-a with a<=x/2 replaces E by E triangle ((0,a] union (x-a,x]) — parity in the Boolean algebra of intervals.
  4. Prove the lower profile theorem for initial prefixes (0,1],(0,2],...,(0,2^n]: after at most n legal toggles attached to their parent ancestries, the resulting symmetric difference has measure at least 1 — by induction on the top dyadic band, retaining both the exposed frontier interval and remaining cut reserve.
  5. Prove a universal upper profile theorem for arbitrary n+1 parent prefixes of total length 1: choose at most n legal toggles so that their final symmetric difference has measure at most 1/(2^{n+1}-1), preferably a single interval — by profile-valued induction using equal-child cancellation and cross-parent prefix cancellation, with the residual interval's location carried in the induction hypothesis.
  6. Treat m<=n initial parents separately by constructing complete cancellation (or by a strengthened theorem with spare budget), so the at-most-n-marks quantifier is covered.
  7. Translate Steps 4–6 through D=|E| to the matching bounds and verify the dyadic equality profile E=(0,1/T].
Key lemmas (claim + the one-line mechanism that makes it true):
  - Layer-cake identity D=|E| — because each height layer contributes 1 exactly when its number of covering pieces is odd.
  - Split-toggle identity — because replacing one prefix (0,x] by (0,a] and (0,x-a] cancels the overlap and leaves the bottom and top bands stated in Step 3.
  - Loaded dyadic profile theorem — because the strict geometric-sum excess is one unit, while each ancestry-respecting toggle consumes one unit of cut reserve; the induction must retain the frontier's position.
  - Loaded universal profile theorem — because halving annihilates a prefix in pairs and matching a child length to another parent cancels equal prefixes, with an interval-valued residual surviving recursion.
Open gaps: Steps 4 and 5 are both substantial and presently conjectural; Step 5 is especially vulnerable because scalar induction on |E| is known to fail. The builder should first formulate a precise inductive state before attempting calculations.
Cases to cover: top parent split versus unsplit; cut repeated inside one ancestry; halving cancellation versus cross-parent cancellation; m<=n versus m=n+1; even versus odd final piece count; endpoint/tie conventions.
Watch out for: This is a genuinely profile-valued route, not permission to replace the hard theorem by the already-insufficient scalar claim. Do not cite `aimo-0127` or `aimo-0340`; reproduce any transferred threshold/reserve argument. The cheap subset-sum folding proof is stronger for the upper half, but importing it wholesale would collapse this rival into the first approach.

rank-word-polyhedral-minimax: new
Target: Prove for every positive integer n that c_n=2^n/(2^{n+1}-1), by a complete primal-dual characterization of the continuous splitting minimax problem.
Technique: Parametric linear programming by rank words, explicit LP dual certificates, complementary slackness, and a recursive polyhedral cover of the parent-mass simplex.
Skeleton:
  1. Reduce drafting to the odd-rank sum and encode each ranked final piece by the label of its Liu parent.
  2. For each rank word w, formulate Xiang's closed-cell primal LP: nonincreasing nonnegative ranked lengths, one conservation equality per parent, and objective sum of odd ranks. Prove that positive feasible points are legal refinements and boundary points are legal limits.
  3. Derive the dual inequalities lambda_{w_j}+mu_j-mu_{j-1}<=c_j, with c_j=1 on odd ranks and 0 on even ranks, mu_j>=0 and endpoint mu_0=mu_q=0 — by finite-dimensional weak/strong LP duality proved or stated with hypotheses.
  4. At dyadic parent masses, construct recursively for every admissible word a dual solution of value at least 2^n/T; compress the word by deleting an adjacent odd-even pair or a parent-label run, and update binary parent prices and boundary prices — this proves Liu's guarantee uniformly over all refinements.
  5. For arbitrary parent masses, partition the simplex into finitely described recursive regions, each carrying a primal rank word and feasible lengths with odd sum at most 2^n/T — a primal polyhedral cover proves Xiang's obstruction.
  6. Use complementary slackness to show the dyadic vector lies on equality cells (including the refinement with two copies of each 1,2,...,2^{n-1} and one extra 1), and handle vectors with fewer parents as boundary faces.
  7. Convert boundary LP witnesses to legal distinct interior marks by perturbation, then combine both minimax inequalities and verify the formula.
Key lemmas (claim + the one-line mechanism that makes it true):
  - Rank-word equivalence — because fixing parent labels and global rank order leaves only linear monotonicity and conservation constraints.
  - Uniform dyadic dual certificate — because adjacent rank-pair deletion should preserve dual feasibility while powers-of-two parent masses pay exactly for the updated binary prices; this remains unproved.
  - Recursive primal simplex cover — because each mass vector must admit an active refinement cell exposed by its first violated dyadic ratio, after which a lower-dimensional residual problem remains; the exact regions and recursion remain unproved.
  - Closure-to-legal lemma — because strictly positive perturbations within a rank cell approximate every boundary witness without increasing payoff by more than epsilon.
Open gaps: Steps 4 and 5 are major independent gaps; Step 5 is harder. A finite computation for n<=3 is evidence only, not the needed recursive certificate family.
Cases to cover: every number q of final pieces from m through m+n; repeated labels/runs; tied ranks and zero coordinates; parent-simplex boundary (fewer Liu marks); all possible deletion parities in the word recursion.
Watch out for: Dual certificates lower-bound Xiang's minimum and therefore cannot prove his upper-bound strategy; Step 5 must use primal witnesses. Do not brute-force words. LP duality is not an explicit knowledge-base entry, so justify its finite-dimensional use. This route is intentionally far from physical folding, but currently has two hard gaps.

recursive-extremal-splitting: new
Target: Prove for every positive integer n that c_n=2^n/(2^{n+1}-1), by characterizing the maximum of a recursively defined splitting-game functional and its dyadic extremizer.
Technique: Homogeneous minimax recursion, extremal principle on the simplex, and strong induction loaded with a reserve state; this adapts the “one blocked branch spends one resource and preserves the power of two” induction pattern of `aimo-0043`.
Skeleton:
  1. For a multiset A of parent masses and cut budget k, define F_k(A) as the minimum sorted alternating discrepancy over all refinements using at most k splits; show homogeneity and symmetry directly.
  2. Rewrite the desired theorem as max_{a_i>=0, sum a_i=1} F_{m-1}(a_1,...,a_m)=1/(2^m-1), together with the boundary assertion that fewer actual parents and extra budget do no better.
  3. Strengthen F to a two-parameter state G_k(A;R) recording an unmatched reserve/frontier R; choose the definition so a split either creates two viable recursive branches (whose bounds add and introduce a factor 2) or kills one branch while consuming one unit of cut budget, exactly as in the loaded induction pattern of `aimo-0043`.
  4. Prove by induction on m+k the universal inequality F_{m-1}(A)<=sum(A)/(2^m-1), selecting an extremal parent and an explicit first split from the reserve-state dichotomy.
  5. Prove the reverse inequality at A={1,2,...,2^{m-1}} by the same recurrence with equality conditions: every adversarial first split leaves one recursive branch whose reserve is at least the geometric-sum excess 1.
  6. Solve the equality recurrence to obtain the unique interior extremal ratios 1:2:...:2^{m-1}; verify directly that halving all but the smallest parent attains discrepancy 1 before normalization.
  7. Translate through the draft reduction and settle legal-mark limits to obtain c_n=2^n/(2^{n+1}-1).
Key lemmas (claim + the one-line mechanism that makes it true):
  - Loaded minimax recurrence — because after the first selected split the terminal ranked pairing can be decomposed into two residual subgames, except when one branch vanishes, in which case the spent cut is removed from the recursive budget.
  - Simplex extremal theorem — because the recurrence's two live branches force geometric balancing at equality, while a one-branch state lowers dimension and budget together.
  - Dyadic equality lemma — because 2^j=1+(1+2+...+2^{j-1}) supplies exactly one reserve unit at every equality transition.
Open gaps: Step 3 is the decisive gap: F alone has no known valid scalar recurrence, so the builder must define and validate G before claiming Steps 4–6. The decomposition must respect global rank order, not merely parent ancestry.
Cases to cover: both recursive branches live versus one blocked; largest parent split versus another parent split; repeated cuts in one ancestry; simplex boundary/fewer parents; equality and strict-inequality cases.
Watch out for: Numerical partial-budget values are not a neat power sequence, so do not guess G from F alone. The `aimo-0043` move is only an induction template, not a theorem applicable without proving the branch decomposition. This approach is the most speculative but is a genuinely different top-level framing from profile algebra, folding, and LP cells.
