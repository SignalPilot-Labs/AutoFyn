## Status
solved

## Approaches tried
- pairing-exchange-normal-form — worked (round 1). Lower bound: LB plays the geometric config (pieces 2^0..2^n in units of 1/(2^{n+1}-1)); a graph sign-assignment argument on pair/singleton partitions forces A(M) >= 1 unit. Upper bound: XY pairs nearly-equal subset sums (pigeonhole over 2^{n+1} subsets) and realizes the gap as a single leftover via the Folding Lemma with <= n marks. Reviewer verified all lemmas by hand and both bounds numerically (min-oddsum search n<=3 exact; strategy simulation n<=5 including prior counterexamples). APPROVED.
- geometric-cascade-induction — not built this round (Merge Lemma needed repair).
- parity-alternating-sum — not built this round.
- (superseded within pairing slug) naive greedy pairing upper bound — refuted by explicit counterexamples at n=3,4; sigma-only induction for the Leftover Lemma cannot close.

## Current best
Complete proof of c(n) = 2^n/(2^{n+1}-1), both bounds. Solved.

## Full proof

**Problem.** Liu Bang (LB) marks at most n points on a stick of length 1; then Xiang Yu (XY) marks at most n further points, all marked points distinct. The stick is cut at all marked points. The players alternately claim unclaimed pieces, LB first, each maximizing the total length of his own pieces. Determine the largest c = c(n) that LB can guarantee.

**Answer.** c(n) = 2^n/(2^{n+1} − 1).

Throughout, write D = 2^{n+1} − 1.

### 0. Setup, conventions, notation

A *multiset* M = {a_1, a_2, …, a_N} of nonnegative reals is always listed in decreasing order a_1 ≥ a_2 ≥ … ≥ a_N. Define

- σ(M) = a_1 + a_2 + … + a_N (the total),
- oddsum(M) = a_1 + a_3 + a_5 + … (the sum over odd ranks),
- A(M) = a_1 − a_2 + a_3 − a_4 + … (the alternating sum).

These depend only on the multiset (ties in the sorting do not change the value sequence). Clearly

  oddsum(M) = (σ(M) + A(M)) / 2.  (∗)

Adjoining elements equal to 0 to M changes none of σ, oddsum, A: zeros occupy the lowest ranks and contribute 0.

**Convention on endpoint marks.** A mark at 0 or 1 either produces no piece or a piece of length 0; by the previous paragraph, pieces of length 0 affect nothing in the claiming phase (they have value 0 and sit at the bottom of the sorted order), so we may and do ignore them: all pieces considered have positive length, and each marked point in the open interval (0,1) increases the number of (positive-length) pieces by exactly 1, while marks at 0 or 1 do not increase it.

### 1. The claiming phase: Lemma 0

**Lemma 0 (value of the alternating-claiming game).** Let M be a finite multiset of nonnegative reals (the piece lengths). In the game where two players alternately claim elements of M, the mover claiming first, and each player's payoff is the sum of his claimed elements, the first mover can guarantee himself at least oddsum(M), and the second player can guarantee that the first mover gets at most oddsum(M).

*Proof.* Define V(∅) = 0 and, recursively for nonempty M,

  V(M) = max_{x ∈ M} [ x + σ(M∖x) − V(M∖x) ].

We prove by induction on |M| the two guarantees:

(i) the first mover has a strategy guaranteeing himself ≥ V(M);
(ii) the second player has a strategy guaranteeing that the first mover gets ≤ V(M).

Base |M| = 0: trivial. Induction step: For (i), the mover claims an x attaining the maximum; in the remaining game on M∖x the opponent moves first, and by (ii) for M∖x (roles swapped) the original mover, now second, can hold the opponent to ≤ V(M∖x); since every element of M∖x is claimed by someone, the original mover then collects ≥ σ(M∖x) − V(M∖x), for a total ≥ x + σ(M∖x) − V(M∖x) = V(M). For (ii): whatever x the first mover claims, by (i) applied to M∖x the second player (who moves first there) can guarantee himself ≥ V(M∖x), hence the first mover gets ≤ x + σ(M∖x) − V(M∖x) ≤ V(M). This proves (i) and (ii).

It remains to show V(M) = oddsum(M). Induction on |M|; base clear. Let M = {a_1 ≥ … ≥ a_N}. By the induction hypothesis V(M∖x) = oddsum(M∖x), so the payoff of claiming x is

  P(x) = x + σ(M∖x) − oddsum(M∖x) = x + evensum(M∖x),

where evensum is the sum over even ranks. For x = a_i, deleting a_i shifts ranks j > i down by one, so

  evensum(M∖a_i) = Σ_{j < i, j even} a_j + Σ_{j > i, j odd} a_j.

For i = 1 this gives P(a_1) = a_1 + a_3 + a_5 + … = oddsum(M). For i ≥ 2:

  oddsum(M) − P(a_i) = Σ_{j odd, j ≤ i} a_j − a_i − Σ_{j even, j < i} a_j.

If i is odd, this equals (a_1 − a_2) + (a_3 − a_4) + … + (a_{i−2} − a_{i−1}) ≥ 0; if i is even, it equals (a_1 − a_2) + … + (a_{i−1} − a_i) ≥ 0, since the sequence is decreasing. Hence the maximum is attained at x = a_1 and V(M) = oddsum(M). ∎

So after the cutting is done and produces the multiset M of piece lengths (σ(M) = 1), the claiming phase is worth exactly oddsum(M) = (1 + A(M))/2 to LB: he can guarantee this much and cannot be sure of more. The problem is therefore equivalent to:

  c(n) = max_{LB cuts} min_{XY cuts} oddsum(M) = (1 + max min A(M)) / 2.

We prove: max min A(M) = 1/D, i.e. LB can force A(M) ≥ 1/D (Section 4), and XY can always force A(M) ≤ 1/D (Section 5). By (∗), this gives c(n) = (1 + 1/D)/2 = ((D+1)/D)/2 = 2^{n+1}/(2D) = 2^n/D, as claimed.

### 2. Elementary facts about alternating sums

**Lemma 1.** Let b_1 ≥ b_2 ≥ … ≥ b_c ≥ 0 and U = b_1 − b_2 + b_3 − … + (−1)^{c+1} b_c. Then:

(F1) 0 ≤ U ≤ b_1.
(F2) If c is odd, then U ≥ b_c.
(F3) If c is even and c ≥ 2, then U ≤ b_1 − b_c.

*Proof.* (F1): grouping from the left, U = (b_1 − b_2) + (b_3 − b_4) + … (plus a final +b_c if c is odd), a sum of nonnegative terms, so U ≥ 0. Also U = b_1 − (b_2 − b_3) − (b_4 − b_5) − … (with a final −b_c if c is even), i.e. b_1 minus nonnegative terms, so U ≤ b_1.
(F2): for odd c, U = (b_1 − b_2) + … + (b_{c−2} − b_{c−1}) + b_c ≥ b_c.
(F3): for even c, U = b_1 − (b_2 − b_3) − (b_4 − b_5) − … − (b_{c−2} − b_{c−1}) − b_c ≤ b_1 − b_c. ∎

**Lemma 2 (peeling a singleton).** For any multiset M of nonnegative reals and any x ∈ M:

  A(M) ≤ A(M ∖ {x}) + x.

*Proof.* Say x = a_i in the sorted order of M = {a_1 ≥ … ≥ a_N}. Removing a_i leaves ranks j < i unchanged and shifts ranks j > i down by one (flipping their signs), so

  Δ := A(M) − A(M∖{x}) = (−1)^{i+1} x + 2 Σ_{j>i} (−1)^{j+1} a_j = (−1)^{i+1} x + 2(−1)^i T,

where T = Σ_{s≥1} (−1)^{s+1} a_{i+s} is an alternating sum of the decreasing tail, so 0 ≤ T ≤ a_{i+1} by (F1). If i is odd: Δ = x − 2T ≤ x. If i is even: Δ = −x + 2T ≤ −x + 2a_{i+1} ≤ −x + 2a_i = x. ∎

**Lemma 3 (peeling a pair).** For any multiset M of nonnegative reals and any two elements x ≥ y of M:

  A(M) ≤ A(M ∖ {x, y}) + (x − y).

*Proof.* Choose ranks i < j with a_i = x, a_j = y (possible since x ≥ y; if x = y take any two occurrences). Removing both flips the signs exactly of the ranks strictly between i and j (ranks past j shift by two, keeping their signs), so with c = j − i − 1 and U = Σ_{s=1}^{c} (−1)^{s+1} a_{i+s} (an alternating sum of the decreasing block between them, to which Lemma 1 applies),

  Δ := A(M) − A(M∖{x,y}) = (−1)^{i+1} x + (−1)^{j+1} y + 2(−1)^i U.

Four parity cases (note c ≡ j − i − 1 mod 2):

1. i odd, j even (c even): Δ = x − y − 2U ≤ x − y, since U ≥ 0 (F1).
2. i odd, j odd (c odd): Δ = x + y − 2U ≤ x + y − 2a_{j−1} ≤ x + y − 2y = x − y, using (F2) (U ≥ a_{j−1} ≥ a_j = y). (Here c ≥ 1, so a_{j−1} is inside the block.)
3. i even, j odd (c even): if c = 0, Δ = −x + y ≤ x − y since x ≥ y ≥ 0. If c ≥ 2, Δ = −x + y + 2U ≤ −x + y + 2(a_{i+1} − a_{j−1}) ≤ −x + y + 2(x − y) = x − y, using (F3) and a_{i+1} ≤ a_i = x, a_{j−1} ≥ a_j = y.
4. i even, j even (c odd): Δ = −x − y + 2U ≤ −x − y + 2a_{i+1} ≤ −x − y + 2x = x − y, using (F1). ∎

**Definition (pairing partitions and cost).** A *pairing partition* Π of a multiset M is a partition of M into blocks of size two ("pairs") and size one ("singletons"). Its *cost* is

  cost(Π) = Σ_{pairs {a,b}} |a − b| + Σ_{singletons {c}} c.

**Lemma 4 (Partition Lemma).** For every multiset M of nonnegative reals and every pairing partition Π of M,

  A(M) ≤ cost(Π),

with equality for the *adjacent pairing* Π₀ = {a_1,a_2}, {a_3,a_4}, … (final singleton {a_N} if N is odd):

  A(M) = cost(Π₀).

*Proof.* Inequality: peel off the blocks of Π one at a time, applying Lemma 3 for each pair and Lemma 2 for each singleton; after all blocks are removed we reach A(∅) = 0, and the accumulated bound is exactly cost(Π). (Lemmas 2 and 3 hold for arbitrary multisets, so the peeling order is irrelevant.) Equality for Π₀: cost(Π₀) = (a_1 − a_2) + (a_3 − a_4) + … (+ a_N if N odd) = A(M) by definition. ∎

Lemma 4 is the exchange/pairing engine of this approach: the lower bound will bound cost(Π₀) = A(M) from below by bounding **every** pairing partition's cost; the upper bound will exhibit **one** cheap pairing partition.

### 3. LB's configuration

LB places his n marks at the points (2^1 − 1)/D, (2^2 − 1)/D, …, (2^n − 1)/D. These are n distinct points of (0,1). The resulting pieces have lengths

  1/D, 2/D, 4/D, …, 2^n/D  (piece k spans [(2^k − 1)/D, (2^{k+1} − 1)/D], length 2^k/D, k = 0, …, n),

which indeed total (2^{n+1} − 1)/D = 1. From now on we measure lengths in *units* of 1/D; LB's pieces are 2^0, 2^1, …, 2^n and the whole stick is D units.

### 4. Lower bound: A(M) ≥ 1 unit for every XY response

Call LB's n+1 pieces *sources*, indexed 0, …, n with sizes s_i = 2^i (units). XY places m ≤ n marks; by the endpoint convention (Section 0) we may assume all of them lie in (0,1)∖{LB's marks}, i.e. strictly inside sources. The final multiset M consists of N = (n + 1) + m ≤ 2n + 1 *fragments*, each contained in exactly one source; the fragments of source i have positive lengths summing to s_i. (If XY places marks at 0 or 1, N is only smaller, which only helps below.)

**Theorem A (lower bound).** For every XY response, every pairing partition Π of M has cost(Π) ≥ 1 unit. Consequently A(M) = cost(Π₀) ≥ 1 unit = 1/D, and by Lemma 0 and (∗), LB is guaranteed at least (1 + 1/D)/2 = 2^n/D.

*Proof.* Fix a pairing partition Π of M. Build a multigraph H:

- vertices: the sources 0, 1, …, n;
- edges: one edge {i, j} for each pair {a, b} of Π with a a fragment of source i and b a fragment of source j (a loop at i if i = j).

The number of edges of H equals the number of pairs of Π, which is at most ⌊N/2⌋ ≤ ⌊(2n+1)/2⌋ = n.

Call a connected component C of H *good* if there is a map δ: V(C) → {+1, −1} with δ_i ≠ δ_j for every edge {i, j} of C (in particular, C has no loops), i.e. C is bipartite as a multigraph; otherwise *bad*.

**Claim: a bad component C has at least |V(C)| edges.** Indeed, C is connected, so it has at least |V(C)| − 1 edges that join distinct vertices (loops do not contribute to connectivity: if C had a loop and only |V(C)| − 2 non-loop edges, its vertices could not all be connected). If C has exactly |V(C)| − 1 edges, then none is a loop and, counted with multiplicity, they connect |V(C)| vertices, which forces the underlying graph to be a tree with no repeated edges (a multi-edge would leave ≤ |V(C)| − 2 distinct adjacencies, disconnecting C); a tree is properly 2-colorable, so C would be good. Hence a bad C has ≥ |V(C)| edges. ∎(Claim)

If **every** component were bad, summing the claim over components would give

  #edges(H) ≥ Σ_C |V(C)| = n + 1 > n ≥ #edges(H),

a contradiction. So some component K is good; fix a valid δ: V(K) → {±1}.

Assign to each fragment f whose source lies in V(K) the sign ε_f = δ_{source(f)}. Note that the blocks of Π split cleanly along components of H: a pair joins fragments whose sources are adjacent in H, hence in the same component; a singleton's source lies in one component. Let cost_C(Π) denote the cost contribution of the blocks whose fragments have sources in component C; then cost(Π) = Σ_C cost_C(Π) and every cost_C(Π) ≥ 0 (it is a sum of absolute differences and nonnegative singleton values).

For the good component K:

- for each pair {a, b} with sources in V(K): the sources are adjacent, so ε_a = −ε_b, hence ε_a a + ε_b b = ±(a − b) ≤ |a − b|;
- for each singleton {c} with source in V(K): ε_c c ≤ c (as c ≥ 0).

Summing over all blocks in K, and noting that the fragments with sources in V(K) are exactly all fragments of the sources in V(K) (each such fragment lies in some block of Π, and its block stays inside K as just observed), we get

  cost_K(Π) ≥ Σ_{f: source(f) ∈ V(K)} ε_f f = Σ_{i ∈ V(K)} δ_i · (sum of fragments of source i) = Σ_{i ∈ V(K)} δ_i s_i =: W.

Replacing δ by −δ (also valid) gives cost_K(Π) ≥ −W, so cost_K(Π) ≥ |W|.

Finally, W = Σ_{i ∈ V(K)} δ_i 2^i is a ±1-signed sum of **distinct** powers of two over the nonempty set V(K). Let t = max V(K). Then

  |W| ≥ 2^t − Σ_{i ∈ V(K), i < t} 2^i ≥ 2^t − (2^t − 1) = 1.

Hence cost(Π) ≥ cost_K(Π) ≥ 1 unit. Applying this to the adjacent pairing Π₀ and using Lemma 4 (equality part), A(M) = cost(Π₀) ≥ 1 unit = 1/D. By (∗), oddsum(M) ≥ (1 + 1/D)/2 = 2^n/D, and by Lemma 0(i) LB can claim at least this much. ∎

### 5. Upper bound: XY can force A(M) ≤ 1/D against every LB configuration

Now LB's marks are arbitrary: they produce k pieces of positive length p_1 ≥ p_2 ≥ … ≥ p_k with Σ p_i = 1 and k ≤ n + 1 (each of LB's ≤ n marks in (0,1) adds at most one piece). We exhibit an XY response (≤ n marks, all distinct from each other and from LB's marks) after which the final multiset M admits a pairing partition of cost ≤ 1/D; then A(M) ≤ 1/D by Lemma 4, and by Lemma 0(ii) XY can hold LB to oddsum(M) ≤ (1 + 1/D)/2 = 2^n/D in the claiming phase.

Two cutting primitives, each using at most one mark; all marks placed by XY will be strictly inside a *current* piece (a piece of the partition of [0,1] generated by all marks chosen so far), hence automatically distinct from all previously placed marks and from LB's marks — XY of course computes all positions in advance and places them simultaneously; the sequential description below merely defines those positions.

- **Halve(p):** mark the midpoint of piece p, creating two pieces of length p/2 (an equal pair). Cost contribution 0. One mark.
- **Fold(a, b)** for two current pieces with a > b: mark the point of piece a at distance b from its left endpoint, creating a piece of length b — which we pair with piece b, an exactly equal pair, cost contribution 0 — and a remainder piece of length a − b, which stays in play. One mark. If a = b, Fold(a,b) simply pairs the two pieces with **no mark at all**.

**Lemma 5 (Folding Lemma).** Let A and B be disjoint sets of current pieces, all of positive length, with v := σ(A) − σ(B) ≥ 0. Then using at most |A| + |B| − 1 marks XY can cut so that all resulting fragments of the pieces of A ∪ B are matched into exactly equal pairs, except for at most one leftover fragment of length ≤ v.

*Proof.* Run the following process on the working multisets (A, B), which maintains the invariant σ(A) − σ(B) = v:

While A ≠ ∅ and B ≠ ∅: take any a ∈ A, b ∈ B and apply Fold(a, b) (to the larger of the two; if a = b no mark is used). If a > b, the pair (b, b) is banked at cost 0 and the remainder a − b replaces a in A: the new sums are (σ(A) − a + (a − b), σ(B) − b), difference unchanged. If b > a, symmetrically the remainder b − a replaces b in B; difference again unchanged. If a = b, both are removed; difference unchanged. Each iteration uses ≤ 1 mark and decreases |A| + |B| by at least 1.

The loop ends with A = ∅ or B = ∅. If A = ∅ and B ≠ ∅ we would have σ(B) = −v ≤ 0, impossible for a nonempty set of positive lengths; so B = ∅ at termination, and the remaining set A′ satisfies σ(A′) = v.

Now fold A′ down: while |A′| ≥ 2, take any two pieces a ≥ a′ of A′ and apply Fold(a, a′); each step banks an equal pair, uses ≤ 1 mark, decreases |A′| by ≥ 1, and does not increase σ(A′) (the sum drops by 2a′ ≥ 0). Termination leaves at most one piece, of length ≤ σ(A′) = v.

Mark count: every iteration of either loop removes at least one piece from the working collection and uses at most one mark; we start with |A| + |B| pieces and end with ≥ 0, and the last surviving piece never needs a mark, so at most |A| + |B| − 1 marks are used in total. ∎

**Theorem B (upper bound).** For every LB configuration, XY has a response with at most n marks after which A(M) ≤ 1/D. Hence LB cannot guarantee more than (1 + 1/D)/2 = 2^n/D.

*Proof.* Case 1: k ≤ n. XY applies Halve to every piece: k ≤ n marks, and M consists of k exactly equal pairs. The pairing partition into those pairs has cost 0, so A(M) ≤ 0, i.e. A(M) = 0 (A ≥ 0 always, by (F1)); LB gets at most 1/2 < 2^n/D (indeed 2·2^n = 2^{n+1} > D). 

Case 2: k = n + 1. Consider all 2^{n+1} subsets T ⊆ {1, …, n+1} and their sums σ_T = Σ_{i∈T} p_i ∈ [0, 1]. Sorting these 2^{n+1} numbers, the 2^{n+1} − 1 consecutive gaps span at most 1, so by the pigeonhole principle (knowledge_base.md, "Pigeonhole / extremal principle") two **distinct** subsets T ≠ T′ satisfy |σ_T − σ_{T′}| ≤ 1/(2^{n+1} − 1) = 1/D.

Let A* = {p_i : i ∈ T ∖ T′} and B* = {p_i : i ∈ T′ ∖ T}; these use disjoint index sets, S := (T ∖ T′) ∪ (T′ ∖ T) ≠ ∅, and σ(A*) − σ(B*) = σ_T − σ_{T′}. Swapping if necessary, assume v := σ(A*) − σ(B*) ≥ 0; then 0 ≤ v ≤ 1/D.

XY's marks: apply the Folding Lemma (Lemma 5) to (A*, B*): at most |S| − 1 marks, producing equal pairs plus at most one leftover fragment r ≤ v ≤ 1/D. Then apply Halve to each of the n + 1 − |S| pieces not in S: n + 1 − |S| marks. Total marks ≤ (|S| − 1) + (n + 1 − |S|) = n. ✓ (Fewer marks are used when some Fold meets equal lengths; "at most n" is legal.)

The final multiset M consists of exactly equal pairs plus at most one leftover fragment of length r ≤ 1/D. Take the pairing partition Π: all those equal pairs (cost 0 each) and the singleton {r} (if present). Then by Lemma 4,

  A(M) ≤ cost(Π) = r ≤ 1/D.

By (∗) and Lemma 0(ii), XY holds LB to oddsum(M) = (1 + A(M))/2 ≤ (1 + 1/D)/2 = 2^n/D. ∎

### 6. Conclusion and verification

By Theorem A, LB's geometric configuration guarantees him at least 2^n/D against every XY response and every claiming play (Lemma 0(i)); by Theorem B, against every LB configuration XY can hold LB to at most 2^n/D (Lemma 0(ii)). Therefore the largest guaranteeable value is exactly

  **c(n) = 2^n / (2^{n+1} − 1).**

Verification.
- Tightness at LB's configuration: XY can cut LB's piece 2^n (units) into fragments 2^{n−1}, 2^{n−2}, …, 2, 1, 1 using exactly n marks; the final multiset is {2^{n−1}, 2^{n−1}, …, 2, 2, 1, 1, 1}: n equal pairs plus one leftover unit, so A(M) = 1 unit exactly (Lemma 4 both directions: ≤ 1 by the pair/singleton partition, ≥ 1 by Theorem A) and LB gets exactly (1 + 1/D)/2 = 2^n/D. Both bounds are attained, confirming consistency.
- n = 1: c(1) = 2/3. LB marks 1/3, pieces (1/3, 2/3); if XY halves the 2/3-piece, the pieces are (1/3, 1/3, 1/3) and LB takes two of three: 2/3. ✓ Formula: 2^1/(2^2 − 1) = 2/3. ✓
- Sanity of the answer's form: the constant D = 2^{n+1} − 1 is exactly the pigeonhole count of nontrivial gaps among the 2^{n+1} subset sums (upper bound), and exactly the total 1 + 2 + … + 2^n of LB's geometric pieces, whose distinct-signed-sums property (|Σ δ_i 2^i| ≥ 1) drives the lower bound.
- Numerical checks performed during construction (checks only, not proof steps): Lemma 0 against brute-force minimax on 300 random games; Lemmas 2–3 on 20 000 random peel instances; the Theorem B strategy on 5 010 configurations (including the outline-reviewer's counterexamples to the naive greedy, (0.4608, 0.2307, 0.1561, 0.1524) and (0.4388, 0.2228, 0.1296, 0.1271, 0.0817), and all geometric configs n ≤ 7), always with ≤ n marks and value ≤ 2^n/D; 200 000-trial randomized minimization of oddsum over XY responses at n = 2, 3 bottoming out at exactly 2^n.

∎
