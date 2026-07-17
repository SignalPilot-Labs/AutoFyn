# Approach: parity-alternating-sum

## Status
solved

## Approaches tried
- Round 1 (outline): reformulate LB's value as (1+A)/2 with A the alternating sorted sum; lower bound planned via integer rounding + parity (GAP A/A'), upper bound via averaging over a response family (GAP B) — superseded; see next item.
- Round 1 (build): both planned gap-closers were replaced by cleaner devices **inside the same alternating-sum framing**, and both bounds closed completely.
  - Lower bound: the parity idea ("signed integer combinations of the piece lengths cannot vanish") is realized WITHOUT any Rounding Lemma: pair the sorted final pieces, build a multigraph on LB's n+1 original pieces with one edge per pair; since XY has at most n cuts there are at most n pairs, so some component is a tree; 2-coloring that tree turns the pair gaps into a signed sum of distinct powers of 2, which is a nonzero integer, forcing A ≥ 1 unit. GAP A and GAP A' are gone (never opened).
  - Upper bound: the averaging family (GAP B) is replaced by a pigeonhole strategy: the 2^{n+1} subset sums of LB's n+1 pieces lie in [0,1], so two differ by at most 1/(2^{n+1}−1); XY realizes that difference as the total of the unpaired leftovers by a subtractive combining scheme (halve every piece outside the two subsets, repeatedly cut the larger of two active pieces to clone the smaller), using at most n cuts. GAP B is gone (never opened).
  - Both mechanisms were verified numerically for n ≤ 8 (random and locally-optimized XY cut patterns for the lower bound; 4000 random LB placements per n for the upper bound); the geometric configuration is the exact equality case of both.

## Current best
Complete proof of c(n) = 2^n/(2^{n+1}−1). No open gaps. Full proof below.

## Full proof

**Answer.** c(n) = 2^n/(2^{n+1}−1).

Throughout, set D = 2^{n+1} − 1, so the claimed answer is 2^n/D. For n = 1 this is 2/3, for n = 2 it is 4/7, etc.

### 0. Setup and conventions

Liu Bang (LB) marks at most n points of the stick [0,1]; then Xiang Yu (XY), seeing LB's marks, marks at most n further points, all marked points being distinct. The stick is cut at all marks, producing pieces; the players alternately claim pieces, LB first, each maximizing his own total length.

A mark at an endpoint 0 or 1 of the stick produces a piece of length 0. We first dispose of zero-length pieces:

**Convention (zero pieces are irrelevant).** The quantity "sum of odd-ranked pieces" computed in Lemma 1 below is unchanged when 0's are appended to the multiset of pieces, because appended zeros occupy the lowest ranks of the sorted order and contribute 0 to every partial sum. All statements below therefore refer to the multiset of **positive** pieces, and a player marking an endpoint of the stick simply wastes a mark. In particular: LB's marks produce k ≤ n+1 positive pieces, and XY's marks give c ≤ n cutting points strictly inside those pieces.

**Lemma 1 (value of the claiming phase).** Let the positive pieces, sorted, be q_1 ≥ q_2 ≥ … ≥ q_m, and write oddsum(Q) = q_1 + q_3 + q_5 + …. In the claiming phase, LB can guarantee a total of at least oddsum(Q), and XY can guarantee that LB's total is at most oddsum(Q); so under optimal play LB's total is exactly oddsum(Q).

*Proof.* (LB's guarantee.) Let LB always claim a longest unclaimed piece. Before LB's i-th claim, exactly 2(i−1) pieces have been claimed in total, so at most 2i−2 of the 2i−1 pieces q_1, …, q_{2i−1} are claimed; hence some unclaimed piece has length ≥ q_{2i−1}, and LB's i-th claim is ≥ q_{2i−1}. Summing over i, LB gets at least q_1 + q_3 + … (LB makes ⌈m/2⌉ claims).

(XY's guarantee.) Let XY always claim a longest unclaimed piece. Before XY's i-th claim, exactly 2i−1 pieces have been claimed, so at most 2i−1 of the 2i pieces q_1, …, q_{2i} are claimed; hence XY's i-th claim is ≥ q_{2i}, and XY's total is at least q_2 + q_4 + … = σ − oddsum(Q), where σ = Σ q_i. Since the two totals add up to σ, LB's total is then at most oddsum(Q). ∎

So the whole game reduces to: LB chooses a partition of [0,1] into k ≤ n+1 pieces; XY refines it with c ≤ n cuts; the payoff to LB is oddsum of the final multiset. Define the **alternating sum**
A(Q) = q_1 − q_2 + q_3 − q_4 + … (sorted decreasingly).
Since oddsum + evensum = σ and oddsum − evensum = A,

**oddsum(Q) = (σ + A(Q))/2**, and in our game σ = 1.

Note A(Q) depends only on the sorted sequence of values, hence not on any tie-breaking among equal pieces. Two basic facts:

**Lemma 2 (alternating-sum toolkit).** For a finite multiset Q of positive reals:
(a) (Layer-cake form) A(Q) = ∫_0^∞ π_Q(t) dt, where π_Q(t) ∈ {0,1} is the parity of N_Q(t) = #{q ∈ Q : q > t}.
(b) (Pair removal) A(Q ∪ {x, x}) = A(Q) for any x > 0; consequently, if Q can be split into pairs of equal pieces plus a sub-multiset E of "extras", then A(Q) = A(E).
(c) 0 ≤ A(Q) ≤ σ(Q) := Σ_{q∈Q} q, and A(Q) ≤ max Q.

*Proof.* (a) Let q_1 ≥ … ≥ q_m and set q_{m+1} = 0. For t ∈ [q_{i+1}, q_i) we have N_Q(t) = i (this is correct also when some q's tie: N counts strictly larger pieces, and on that interval — empty when q_{i+1} = q_i — exactly q_1, …, q_i exceed t). Hence
∫_0^∞ π_Q = Σ_{i odd, i ≤ m} (q_i − q_{i+1}) = q_1 − q_2 + q_3 − … = A(Q),
the last equality holding for both parities of m because q_{m+1} = 0.
(b) N_{Q∪{x,x}}(t) = N_Q(t) + 2·1[x > t], which has the same parity as N_Q(t) for every t; now apply (a). Iterating gives the "pairs plus extras" statement.
(c) Grouping consecutively, A = Σ_i (q_{2i−1} − q_{2i}) (+ q_m if m is odd), a sum of nonnegative terms, so A ≥ 0; A ≤ σ is clear since the subtracted terms are nonnegative; and A = q_1 − (q_2 − q_3) − (q_4 − q_5) − … ≤ q_1 = max Q, since each bracketed difference is ≥ 0 (append a final 0 if needed). ∎

By Lemma 1, proving c(n) = 2^n/D amounts to proving:
- **Lower bound:** LB has a placement such that every XY response leaves oddsum ≥ 2^n/D, i.e. A ≥ 1/D.
- **Upper bound:** for every LB placement, XY has a response with oddsum ≤ 2^n/D, i.e. A ≤ 1/D.

### 1. Lower bound: LB guarantees 2^n/D

**LB's placement.** LB marks the n points t_j = (2^j − 1)/D, j = 1, …, n. These are distinct points strictly inside (0,1), and together with t_0 = 0 and t_{n+1} = 1 they cut [0,1] into n+1 pieces of lengths
t_1 − t_0 = 1/D, t_{j+1} − t_j = (2^{j+1} − 2^j)/D = 2^j/D (j = 1, …, n−1), t_{n+1} − t_n = 1 − (2^n − 1)/D = 2^n/D.
So the pieces have lengths 2^0/D, 2^1/D, …, 2^n/D. **Rescale all lengths by the factor D** (i.e. work in units u = 1/D): the original pieces are P_0, …, P_n of integer lengths 2^0, 2^1, …, 2^n, of total σ = D. We must show: after any XY response, A ≥ 1 in these units.

Let XY make c ≤ n cuts, each strictly inside some piece (endpoint marks are wasted, by the Convention). Say piece P_i receives c_i ≥ 0 cuts, Σ c_i = c; it is divided into c_i + 1 **fragments**, positive reals summing to 2^i. The final multiset Q consists of all m = (n+1) + c fragments; each fragment f belongs to exactly one original piece p(f) ∈ {P_0, …, P_n}.

Fix any nonincreasing ordering q_1 ≥ q_2 ≥ … ≥ q_m of the fragments (any tie-breaking; the argument below works for every choice). Form the **pairs** e_i = (q_{2i−1}, q_{2i}) for 1 ≤ i ≤ ⌊m/2⌋, with gaps d_i = q_{2i−1} − q_{2i} ≥ 0; if m is odd, the smallest fragment q_m is unpaired. By the grouping in Lemma 2(c),

A(Q) = Σ_i d_i (+ q_m if m is odd); in particular **A(Q) ≥ Σ_{i∈I} d_i + q_m·1[m odd] for every subset I of the pairs.** (†)

**The pair graph.** Let G be the multigraph with vertex set {P_0, …, P_n} (n+1 vertices) and one edge per pair e_i, joining p(q_{2i−1}) to p(q_{2i}) (a loop if the two paired fragments come from the same original piece). The number of edges is
⌊m/2⌋ = ⌊(n + 1 + c)/2⌋ ≤ ⌊(2n+1)/2⌋ = n < n + 1 = #vertices.

**Claim: some connected component C of G is a tree** (no loops, no parallel edges, no cycles). Indeed, every connected component satisfies e_C ≥ v_C − 1 (edges vs. vertices, loops and parallel edges each counted separately). If every component had e_C ≥ v_C, then summing over components would give #edges ≥ n+1, contradicting #edges ≤ n. So some component C has e_C = v_C − 1; a connected multigraph with exactly one fewer edge than vertices contains no cycle of any kind (adding a loop, a parallel edge, or a longer cycle to a connected spanning structure would force e_C ≥ v_C), i.e. C is a tree. ∎ (Claim)

**2-coloring.** Since C is a tree it is bipartite: assign to each vertex (piece) P_i of C a sign λ_i ∈ {+1, −1} so that the two endpoints of every edge of C get opposite signs (choose a root, alternate signs with the distance from the root; this is consistent because the two endpoints of each tree edge are at distances differing by exactly 1).

**The key identity.** Consider
S := Σ_{P_i ∈ C} λ_i · 2^i = Σ_{P_i ∈ C} λ_i · ( Σ_{f : p(f) = P_i} q_f ) = Σ_{f : p(f) ∈ C} λ_{p(f)} · q_f ,
where the first equality is just "the fragments of P_i sum to 2^i". Now group the fragments on the right-hand side by pairs. Every pair either has both fragments in pieces of C or both fragments in pieces outside C: a pair with exactly one fragment in C would be an edge of G joining C to the rest of G, which is impossible since C is a connected component. A pair (f, f′) inside C lies on an edge of C, so λ_{p(f′)} = −λ_{p(f)}, and its contribution to S is λ_{p(f)}·(q_f − q_{f′}) = ±d for its gap d. If m is odd and the unpaired fragment q_m has p(q_m) ∈ C, it contributes λ_{p(q_m)}·q_m = ±q_m; otherwise it contributes nothing. Therefore
S = Σ_{pairs inside C} (±d_i) (± q_m if m is odd and p(q_m) ∈ C). (‡)

**Conclusion.** S is a signed sum of distinct powers of two over the nonempty index set {i : P_i ∈ C}: writing j = min{i : P_i ∈ C}, we get S/2^j = ±1 + (even integer), an odd integer; hence S ≠ 0 and |S| ≥ 2^j ≥ 1. On the other hand, by (‡) and the triangle inequality,
1 ≤ |S| ≤ Σ_{pairs inside C} d_i + q_m·1[m odd] ≤ A(Q),
the last step by (†). So A(Q) ≥ 1 in units of 1/D, i.e. A ≥ 1/D in true length. By Lemma 1 and oddsum = (1+A)/2, LB's total under his greedy claiming strategy is at least
(1 + 1/D)/2 = (D+1)/(2D) = 2^{n+1}/(2D) = 2^n/D.
This holds for every XY response (any c ≤ n, any positions), so LB guarantees 2^n/D. ∎ (Lower bound)

*Remark (where the budget enters).* The single inequality #edges = ⌊(n+1+c)/2⌋ ≤ n < n+1 is the only place the cut budget c ≤ n is used, and it is exactly what forces a tree component. With n+1 cuts XY could halve every piece, making every component a single loop and A = 0 — consistent with the bound failing there.

### 2. Upper bound: XY can hold LB to 2^n/D

Let LB place his marks arbitrarily, producing k ≤ n+1 positive pieces p_1, …, p_k with Σ p_i = 1 (endpoint marks are wasted, by the Convention). We exhibit an XY response with at most n cuts after which A(final) ≤ 1/D; by Lemma 1 and oddsum = (1+A)/2, XY's greedy claiming then holds LB to at most (1 + 1/D)/2 = 2^n/D.

**Case 1: k ≤ n.** XY cuts every piece exactly in half (k ≤ n cuts, each strictly interior to its piece; all cut points are distinct since they lie in distinct pieces, and none is an LB mark). The final multiset consists of k equal pairs {p_i/2, p_i/2}; by Lemma 2(b) with E = ∅, A = 0, so LB's total is exactly 1/2 < 2^n/D (indeed 2·2^n = 2^{n+1} > D). Done. (In particular LB must use all n marks, all interior, to have any hope of exceeding 1/2.)

**Case 2: k = n+1.**

*Pigeonhole step.* Consider the 2^{n+1} subset sums s_S = Σ_{i∈S} p_i over S ⊆ {1, …, n+1}. All lie in [0, 1] (with s_∅ = 0, s_{full} = 1). Sort them; the 2^{n+1} − 1 = D consecutive differences are nonnegative and sum to exactly 1, so at least one is ≤ 1/D: there are **distinct** subsets S ≠ S′ with |s_S − s_{S′}| ≤ 1/D. Replace S, S′ by S ∖ S′ and S′ ∖ S: this changes neither the difference s_S − s_{S′} nor the distinctness (S ∖ S′ = S′ ∖ S would force S = S′), and makes the two sets disjoint and not both empty. Swapping names if necessary, we obtain disjoint A_0, B_0 ⊆ {1, …, n+1}, not both empty, with
δ := Σ_{i∈A_0} p_i − Σ_{i∈B_0} p_i ∈ [0, 1/D].

*Combining step.* XY cuts as follows. Maintain two disjoint multisets A, B of **currently existing physical pieces**, initialized A = {p_i : i ∈ A_0}, B = {p_i : i ∈ B_0}; call the pieces in A ∪ B active, and the k − |A_0| − |B_0| original pieces outside A_0 ∪ B_0 inactive.

1. Cut every inactive piece exactly in half (one cut each). Each becomes an equal pair.
2. While A ≠ ∅ and B ≠ ∅: choose any a ∈ A, b ∈ B (we identify a piece with its length).
   - If a = b: remove a from A and b from B (no cut); these two pieces form an equal pair.
   - If a > b: cut the piece a at distance b from one of its ends (one cut, strictly interior since 0 < b < a), producing fragments of lengths b and a − b. The new fragment of length b together with the piece b removed from B forms an equal pair; remove a from A and insert the fragment a − b into A.
   - If b > a: symmetrically, cut b into fragments (a, b − a): the new fragment of length a pairs with the piece a removed from A; remove b from B and insert b − a into B.
3. When the loop stops, the pieces remaining in A ∪ B are left uncut ("extras").

*Invariants.* (i) All active pieces are positive at all times (the inserted fragments a − b, b − a are positive by the strict inequalities). (ii) Σ_A − Σ_B = δ throughout: it holds initially, and each iteration changes (Σ_A, Σ_B) as follows — "a = b": (−a, −a); "a > b": (−a + (a − b), −b) = (−b, −b); "b > a": (−a, −b + (b − a)) = (−a, −a) — in every case both sums drop by the same amount. (iii) |A| + |B| strictly decreases each iteration, so the loop terminates.

*The loop ends with B = ∅.* The loop stops when A or B is empty. If A = ∅ and B ≠ ∅, invariant (ii) gives Σ_B = −δ ≤ 0, impossible for a nonempty set of positive pieces. So at the end B = ∅, and by (ii) the extras (the final content of A) have total sum exactly δ ≤ 1/D.

*Cut count.* Let t = |A_0| + |B_0| ≤ n + 1 be the initial number of active pieces and j ≥ 0 the final number of extras. Step 1 uses (n+1) − t cuts. In step 2, each cutting iteration ("a > b" or "b > a") reduces |A| + |B| by 1 and each free iteration ("a = b") reduces it by 2; if u and g are the respective counts then u + 2g = t − j, so step 2 uses u = t − j − 2g cuts. Total cuts = (n + 1 − t) + (t − j − 2g) = n + 1 − j − 2g. If j ≥ 1 this is ≤ n. If j = 0 then A and B became empty simultaneously, which only a free iteration can do (a cutting iteration leaves the multiset it inserts into nonempty), so g ≥ 1 and the total is ≤ n − 1. In all cases XY uses at most n cuts.

*Legality of the cuts.* Every cut point is strictly interior to the (positive-length) piece being cut at that moment. Pieces existing at any given moment have pairwise disjoint interiors, so cuts made at the same "stage" differ; and a cut made later inside a previously created fragment lies strictly inside that fragment, hence differs from all earlier cut points (which are boundary points of current pieces) and from all LB marks (also boundary points). So all marks are distinct, as required, and XY places at most n of them. (Since XY's marks are computed deterministically from LB's pieces, XY can place them all at once, as the rules demand.)

*Value.* The final multiset F consists of: an equal pair for each inactive piece (step 1), an equal pair for each iteration of step 2, and the j extras of total δ. By Lemma 2(b), A(F) = A(extras), and by Lemma 2(c), A(extras) ≤ Σ extras = δ ≤ 1/D. Hence LB's total under optimal play is
oddsum(F) = (1 + A(F))/2 ≤ (1 + 1/D)/2 = 2^n/D. ∎ (Upper bound)

### 3. Conclusion and verification

By the lower bound, LB's placement at t_j = (2^j − 1)/D (j = 1, …, n) guarantees him at least 2^n/D against every XY response and every play of the claiming phase (Lemma 1 supplies his claiming strategy: always take a longest unclaimed piece). By the upper bound, against every LB placement XY has a response (plus the greedy claiming strategy of Lemma 1) holding LB to at most 2^n/D. Therefore the largest value LB can guarantee is exactly

**c(n) = 2^n / (2^{n+1} − 1).**

*Verification.*
- n = 1: c(1) = 2/3. Construction: pieces (1/3, 2/3). If XY cuts inside 2/3 at a point splitting it into x and 2/3 − x, the three pieces are {x, 2/3 − x, 1/3}; the two largest sum to 1 minus the smallest, and the smallest is ≤ 1/3, so LB (taking largest, then the remaining better piece) gets ≥ 2/3. If XY cuts inside 1/3 or not at all, LB's first claim 2/3 already suffices. Conversely, for any LB placement (a, 1 − a) with a ≥ 1/2: if a ≥ 2/3, XY halves a, leaving (a/2, a/2, 1 − a) with oddsum = a/2 + (1 − a) = 1 − a/2 ≤ 2/3; if 1/2 ≤ a < 2/3, XY cuts a into (1 − a, 2a − 1), leaving the pair {1 − a, 1 − a} plus extra 2a − 1, with oddsum = (1 + (2a − 1))/2 = a < 2/3; if LB used no interior mark, XY halves the whole stick, giving 1/2. So c(1) = 2/3 = 2^1/(2^2 − 1). ✓
- Equality mechanism: at the geometric configuration the subset sums of {2^i/D} are exactly {0/D, 1/D, …, D/D}, so the pigeonhole gap is exactly 1/D, and both bounds meet at 2^n/D; the lower-bound argument shows no XY response does better.
- Numerical checks: for n ≤ 3, exhaustive cut-allocation with local optimization of XY's response against the geometric placement gives min oddsum = 2^n/D exactly; for n ≤ 5, 30000 random responses never beat 2^n/D; the explicit XY strategy of §2, run on 4000 random LB placements for each n ≤ 8, always used ≤ n cuts and never let LB exceed 2^n/D, with equality exactly at the geometric placement.

∎

## Promotable lemmas
- **Lemma: alternating claiming value (Lemma 1, proved in §0).** In the game where two players alternately claim elements of a fixed finite multiset of positive reals (first player moves first), each maximizing his own total, the first player's optimal total is exactly the sum of the odd-ranked elements in decreasing order. (Both guarantees via "always take a longest remaining piece".) Needed by every approach to this problem.
- **Lemma: alternating-sum toolkit (Lemma 2, proved in §0).** For finite multisets of positive reals, with A the alternating sorted sum: (a) A(Q) = ∫_0^∞ (N_Q(t) mod 2) dt where N_Q(t) = #{q > t}; (b) A(Q ∪ {x,x}) = A(Q), hence "equal pairs + extras E ⟹ A(Q) = A(E)"; (c) 0 ≤ A(Q) ≤ min(σ(Q), max Q). This is the clean form of the "Pairs Lemma" wanted by all approaches.
- **Lemma: tree-component bound (lower-bound engine, §1).** If pieces of lengths a_0, …, a_N such that every nonempty ±1-signed sum Σ ε_i a_i has absolute value ≥ 1 (e.g. distinct powers of 2) are refined by at most N further cuts, then the alternating sum A of the final fragment multiset is ≥ 1. The proof in §1 uses only this property of the lengths.
- **Lemma: pigeonhole-and-combine (upper-bound engine, §2).** Given k pieces with total σ and a budget of k − 1 cuts, the cutter can reach a final multiset consisting of equal pairs plus extras of total at most σ/(2^k − 1); consequently the first claimant gets at most (σ + σ/(2^k − 1))/2. Proved in full in §2 Case 2 (Case 1 covers smaller k with value exactly σ/2).
