## Status
solved

## Approach: segment-subset-pigeonhole

A **unified** attempt at the WHOLE problem (both bounds), working directly with Liu Bang's
original segments and their subset sums. UB = pigeonhole + a merge-alignment refinement; LB = a
signed-sum minimum via spanning-tree/bipartite extraction. Independent of the field's
layer-cake / (PM) / β-matching machinery.

**Answer: c(n) = 2^n/(2^{n+1}−1).** Write D_n := 2^{n+1} − 1.

## Approaches tried
- **segment-subset-pigeonhole** (round 6) — SOLVED. Both bounds closed. UB split into two clean
  cases: m ≤ n parts (bisect all parts ⟹ S(B)=0) and m = n+1 parts (pigeonhole over 2^{n+1}
  subset sums into D_n bins + merge-alignment refinement UB1, cuts ≤ m−1 = n). LB via tree
  extraction LB1 (S(B) ≥ Δ(A)) + dyadic evaluation LB2 (Δ = 1/D_n by integer minimality).
  Reconciled with certified L0–L2 (game reduction) and L4 (min-pairing). Cut budget proven
  ≤ m−1 exactly; tree-component existence with all edge cases (isolated dummy, self-loops,
  no isolated part) settled.
- (prior rounds: skeleton only; see history in current.md)

## Current best
Complete proof below. Both bounds established; final answer c(n) = 2^n/(2^{n+1}−1) verified.

## Full proof

Throughout, for a finite multiset X = {x_1, …, x_N} of nonnegative reals sorted descending
x_(1) ≥ x_(2) ≥ ⋯ ≥ x_(N), define the **potential**
  S(X) := Σ_{i=1}^N (−1)^{i+1} x_(i) = x_(1) − x_(2) + x_(3) − ⋯ .
Note S(X) ≥ 0 (group consecutive terms: (x_(1)−x_(2)) + (x_(3)−x_(4)) + ⋯ ≥ 0).

### 0. Reduction to a potential game (imported, certified L0–L2)

By **Lemma L0** (claiming lemma, certified) and **Lemma L1** (order irrelevance, certified), the
stick game is equivalent to the following. Liu Bang (LB) picks a multiset A of m ≤ n+1 positive
reals summing to 1 (his ≤ n cut points cut [0,1] into m intervals). Xiang Yu (XY) then performs
≤ n **split operations**, each replacing one current part x by two positive parts summing to x,
producing a final multiset B (a refinement of A obtained with ≤ n splits). LB's guaranteed value
is the odd-rank sum Σ_odd(B), and
  c(n) = max_A min_B Σ_odd(B).
By **Lemma L2** (potential identity, certified), Σ_odd(B) = (1 + S(B))/2, hence
  c(n) = (1 + max_A min_B S(B))/2.               (0.1)
Since 2·(2^n/D_n) − 1 = (2^{n+1} − D_n)/D_n = 1/D_n, the target c(n) = 2^n/D_n is **equivalent to**
  max_A min_B S(B) = 1/D_n.                        (0.2)
We prove (0.2) by showing the upper bound (§1–2: min_B S(B) ≤ 1/D_n for every A) and the lower
bound (§3–4: min_B S(B) ≥ 1/D_n for the dyadic A).

Here "min_B" ranges over all refinements B of A reachable by ≤ n XY-splits. S(B) is computed on
the OUTPUT multiset B directly, so there is no input/output pairing to reconcile: the potential in
§0, in Lemma L4, and in §1–4 is one and the same functional S of the final multiset.

### 1. Upper bound, Lemma UB1 (merge-alignment refinement)

**Lemma UB1.** Let A = {a_1, …, a_m} (m parts, Σ a_i = 1), and let S, T ⊆ {1, …, m} be
**disjoint** with (S,T) ≠ (∅,∅). Then XY has a refinement B of A, using at most m − 1 splits,
with
  S(B) ≤ |Σ(S) − Σ(T)|,   where Σ(S) := Σ_{i∈S} a_i, Σ(T) := Σ_{i∈T} a_i.

*Proof.* WLOG Σ(S) ≥ Σ(T) (else swap the roles of S and T; the bound is symmetric). Let
L := {1,…,m} ∖ (S ∪ T) be the leftover parts. XY builds B by three groups of splits.

**(a) Leftover bisections.** For each i ∈ L, split a_i into two equal halves a_i/2, a_i/2. This
uses |L| splits and produces |L| equal pairs.

**(b) Merge-alignment of S against T.** Arrange the S-parts consecutively as a block filling the
interval [0, Σ(S)]; its internal division points are the partial sums
S_1 < S_2 < ⋯ < S_{|S|} = Σ(S). Arrange the T-parts consecutively as a block filling [0, Σ(T)];
its internal division points are T_1 < ⋯ < T_{|T|} = Σ(T). Form the merged boundary set
  C := ({0, S_1, …, S_{|S|}} ∪ {0, T_1, …, T_{|T|}}) ∩ [0, Σ(T)],
sorted as 0 = c_0 < c_1 < ⋯ < c_q = Σ(T). XY cuts each S-part at every point of C interior to it,
and cuts each T-part at every point of C interior to it. (Cutting the S-block at C means: for each
S-part [S_{k−1}, S_k], introduce the C-points strictly inside it; likewise for T.)

After (b), on the interval [0, Σ(T)]:
- the S-block is cut at all of C, so within each merged cell [c_{j−1}, c_j] the S-block has
  **exactly one** sub-piece (no S-boundary lies strictly inside a merged cell, since all S-boundaries
  ≤ Σ(T) are in C), of length c_j − c_{j−1};
- the T-block is likewise cut at all of C, giving in each cell one T-sub-piece of the same length
  c_j − c_{j−1}.
Thus the region [0, Σ(T)] yields q **matched pairs**, each pair consisting of one S-sub-piece and
one T-sub-piece of EQUAL length c_j − c_{j−1}.

The remaining S-mass lies in (Σ(T), Σ(S)]; the S-parts there are cut at the S-boundaries S_k in
that range and at the point Σ(T) (if Σ(T) < Σ(S)). These **overhang pieces** are positive and sum
to Σ(S) − Σ(T).

**(c) The output multiset.** B is the disjoint union of: the |L| leftover equal pairs; the q
matched equal pairs; and the overhang pieces (total mass Σ(S) − Σ(T)).

**Bounding S(B) via Lemma L4.** By **Lemma L4** (min-pairing identity, certified), for the sorted
multiset B one has S(B) = min over all partitions of B into pairs and singletons of the cost
  cost = Σ_{pairs {u,v}} |u − v| + Σ_{singletons ℓ} ℓ.
Choose the partition: pair each leftover half with its twin (cost 0 each, equal lengths); pair each
matched S-sub-piece with its T-partner (cost 0 each, equal lengths); and partition the overhang
pieces arbitrarily into pairs plus at most one singleton. The cost of the overhang part is
  Σ_{overhang pairs}|u−v| + (singleton, if any) ≤ Σ_{overhang pairs}(u+v) + (singleton)
  = (total overhang mass) = Σ(S) − Σ(T),
using |u − v| ≤ u + v for u,v ≥ 0. Hence this partition has total cost ≤ Σ(S) − Σ(T), so
  S(B) = min cost ≤ Σ(S) − Σ(T) = |Σ(S) − Σ(T)|.

**Cut budget.** The number of splits equals |B| − m (each split raises the piece count by 1).
Equivalently count the three groups:
- group (a): |L| = m − |S| − |T| splits;
- cuts on S-parts in (b): only at the T-derived points of C, namely T_1, …, T_{|T|} (the T-partial
  sums, all ≤ Σ(T) ≤ Σ(S)); these are ≤ |T| points, so ≤ |T| splits on S-parts (points
  coinciding with existing S-boundaries cause no split);
- cuts on T-parts in (b): only at the S-derived interior points of C, namely those S_k with
  0 < S_k < Σ(T); since S_{|S|} = Σ(S) ≥ Σ(T), at most S_1,…,S_{|S|−1} qualify, so ≤ |S| − 1
  splits on T-parts.
Total splits ≤ (m − |S| − |T|) + |T| + (|S| − 1) = m − 1.

The case T = ∅ (so S ≠ ∅): then Σ(T) = 0, there is no matched region, XY bisects every leftover
part i ∈ {1,…,m} ∖ S (that is m − |S| splits) and leaves the S-parts whole as "overhang" of total
mass Σ(S). Pairing leftovers as twins (cost 0) and the S-parts among themselves (cost ≤ Σ(S)),
L4 gives S(B) ≤ Σ(S) = |Σ(S) − Σ(T)|, with m − |S| ≤ m − 1 splits. ∎

### 2. Upper bound conclusion (min_B S(B) ≤ 1/D_n for every A)

Fix any A with m ≤ n+1 positive parts summing to 1. Two cases.

**Case m ≤ n.** XY splits every part a_i into two equal halves a_i/2, a_i/2. This uses m ≤ n
splits, and B consists of m equal pairs. By Lemma L4, pairing each part's two halves (cost 0)
gives S(B) ≤ 0; since S(B) ≥ 0 always, S(B) = 0 ≤ 1/D_n. Thus min_B S(B) ≤ 1/D_n.

**Case m = n+1.** Consider the 2^{n+1} subsets U ⊆ {1, …, n+1} and their sums Σ(U) ∈ [0, 1]
(Σ(∅) = 0, Σ(full) = 1). Partition [0,1] into D_n = 2^{n+1} − 1 half-open cells
I_k = [k/D_n, (k+1)/D_n) for k = 0, …, D_n − 2, and I_{D_n−1} = [(D_n−1)/D_n, 1] (closed at the
right so 1 is covered). Each cell has length 1/D_n. We have 2^{n+1} = D_n + 1 subsets (pigeons)
and D_n cells (holes); by the **pigeonhole principle** (knowledge_base.md: Pigeonhole), two
**distinct** subsets U ≠ V land in the same cell, so
  |Σ(U) − Σ(V)| ≤ 1/D_n.
Set S := U ∖ V and T := V ∖ U. These are disjoint, and Σ(S) − Σ(T) = Σ(U) − Σ(V) (removing the
common elements U ∩ V subtracts Σ(U ∩ V) from both Σ(U) and Σ(V)), so
  |Σ(S) − Σ(T)| = |Σ(U) − Σ(V)| ≤ 1/D_n.
Since U ≠ V we have U △ V ≠ ∅, so (S,T) ≠ (∅,∅). Apply **Lemma UB1** to A with these S, T: XY
obtains B with S(B) ≤ |Σ(S) − Σ(T)| ≤ 1/D_n, using ≤ m − 1 = n splits. Hence min_B S(B) ≤ 1/D_n.

In both cases min_B S(B) ≤ 1/D_n, so
  **max_A min_B S(B) ≤ 1/D_n.**                    (2.1)

### 3. Lower bound, Lemma LB1 (spanning-tree / bipartite extraction)

For A = {a_1,…,a_m}, define the **signed-sum minimum**
  Δ(A) := min over ε ∈ {−1, 0, 1}^m, ε ≠ 0, of |Σ_{i=1}^m ε_i a_i|.

**Lemma LB1.** For every refinement B of A reachable by ≤ n XY-splits, if m = n+1 then
S(B) ≥ Δ(A).

*Proof.* Let B have pieces sorted descending b_(1) ≥ ⋯ ≥ b_(N). Each piece is a sub-interval of a
unique **parent** part of A (a refinement splits each part into sub-parts). Write
  S(B) = Σ_{i=1}^{⌈N/2⌉} d_i,  where d_i := b_(2i−1) − b_(2i) ≥ 0 for 2i ≤ N, and if N is odd the
last term is d_{⌈N/2⌉} := b_(N) (the unpaired top-of-nothing singleton). Indeed
S(B) = (b_(1)−b_(2)) + (b_(3)−b_(4)) + ⋯ = Σ d_i by the consecutive pairing.

**The multigraph G.** Vertices: one vertex per part of A (m = n+1 of them) plus one **dummy**
vertex δ (assigned length a_δ := 0); so V := m + 1 = n + 2 vertices. Edges: for each pair index i
with 2i ≤ N, add an edge between parent(b_(2i−1)) and parent(b_(2i)); if N is odd, add an edge
between parent(b_(N)) and δ (the singleton edge, with the phantom length 0 sitting at δ). To each
edge e we attach its **gap** d_e := d_i (for the singleton edge, d_e = b_(N)). The number of edges
is E := ⌈N/2⌉.

Since N = m + (number of splits) = (n+1) + s with s ≤ n, we have N ≤ 2n+1, hence
E = ⌈N/2⌉ ≤ ⌈(2n+1)/2⌉ = n+1 < n+2 = V.                              (3.1)

**Edge-length bookkeeping.** Each piece of B is exactly one endpoint-incidence of exactly one
edge (each piece appears in exactly one consecutive pair, or is the singleton). Consequently, for
each part p, a_p = Σ (lengths of pieces with parent p) = Σ over incidences of p of the piece
lengths; and for the dummy, a_δ = 0. Summing over the vertices of any subgraph H with a sign
σ(·) ∈ {±1} on its vertices,
  Σ_{v ∈ H} σ(v) a_v = Σ_{edges e both of whose endpoints lie in H} [σ(u_e) L_e + σ(w_e) ℓ_e],
where e = {u_e, w_e} with the larger piece L_e = b_(2i−1) at u_e and smaller ℓ_e = b_(2i) at w_e
(for the singleton edge, ℓ_e = 0 at δ). This identity holds because every piece of a vertex in H is
accounted for once, and — when H is a connected component or a union of components — every edge
incident to a vertex of H has BOTH endpoints in H.

**A tree component exists.** For each connected component c of G let v_c, e_c be its vertex and
edge counts; a connected graph has e_c ≥ v_c − 1, so v_c − e_c ≤ 1, with equality iff c is a tree.
Also Σ_c (v_c − e_c) = V − E ≥ 1 by (3.1). Since each term is ≤ 1, the number of tree components
  #{trees} = Σ_{c tree} 1 ≥ Σ_c (v_c − e_c) = V − E ≥ 1
(non-tree components contribute ≤ 0). So G has ≥ 1 tree component.

**A tree component with a real part exists.** The only tree component that could fail to contain a
part-vertex is an isolated dummy δ (a single vertex, 0 edges). Every part-vertex p has degree
≥ 1: p has ≥ 1 piece (its part is refined into ≥ 1 sub-piece), and each piece is an endpoint of an
edge, so deg(p) ≥ 1 — no part-vertex is isolated. Now:
- If N is odd, δ has degree 1 (the singleton edge), so δ is not isolated; hence NO tree component is
  a lone δ, and every tree component contains ≥ 1 part-vertex. Pick any (≥ 1 exists).
- If N is even, E = N/2 and N ≤ 2n (since N ≤ 2n+1 and even), so E ≤ n and V − E ≥ (n+2) − n = 2,
  giving ≥ 2 tree components. At most one of them is the lone δ, so ≥ 1 tree component contains a
  part-vertex. Pick it.
Let K be a tree component containing ≥ 1 part-vertex.

**Bipartition and the bound.** As a tree, K is bipartite: 2-color its vertices, σ(v) = +1 on one
class, −1 on the other. Every edge of a tree joins the two classes, so for e ∈ K one endpoint has
σ = +1 and the other σ = −1; thus
  σ(u_e) L_e + σ(w_e) ℓ_e = ±(L_e − ℓ_e) = ±d_e.
By the edge-length identity applied to H = K,
  Σ_{v ∈ K} σ(v) a_v = Σ_{e ∈ K} (±d_e),  hence  |Σ_{v ∈ K} σ(v) a_v| ≤ Σ_{e ∈ K} d_e
                                                                  ≤ Σ_{all e} d_e = S(B),
using the triangle inequality (d_e ≥ 0) and that K's edges are a subset of all edges.

Finally define ε ∈ {−1,0,1}^m by ε_p := σ(p) for the part-vertices p ∈ K and ε_p := 0 otherwise
(the dummy carries a_δ = 0, so it does not appear in the part-sum). Because K contains ≥ 1
part-vertex, ε ≠ 0, and Σ_{v∈K} σ(v) a_v = Σ_{i=1}^m ε_i a_i (the dummy term is 0). Therefore
  Δ(A) ≤ |Σ_i ε_i a_i| = |Σ_{v∈K} σ(v) a_v| ≤ S(B).
(Self-loops — a pair whose two pieces share one parent — form a 1-edge cycle, so they never lie in
a tree component and never affect the argument.) ∎

### 4. Lower bound, Lemma LB2 (dyadic evaluation) and conclusion

**Lemma LB2.** For the **dyadic** profile a_i = 2^{i−1}/D_n (i = 1, …, n+1), we have Σ a_i =
(2^{n+1} − 1)/D_n = 1 (so it is a legal LB choice with n+1 parts), and Δ(A) = 1/D_n.

*Proof.* Δ(A) = (1/D_n)·min over ε ∈ {−1,0,1}^{n+1}, ε ≠ 0, of |Σ_{i=1}^{n+1} ε_i 2^{i−1}|. The
inner sum is an integer. It is nonzero for ε ≠ 0: let j be the largest index with ε_j ≠ 0; then
  |Σ_{i<j} ε_i 2^{i−1}| ≤ Σ_{i<j} 2^{i−1} = 2^{j−1} − 1 < 2^{j−1} = |ε_j 2^{j−1}|,
so the top term cannot be cancelled and the sum is a nonzero integer, hence ≥ 1 in absolute value.
Equality is attained by ε = (1, 0, …, 0), giving |2^0| = 1. Thus the inner minimum is 1 and
Δ(A) = 1/D_n. ∎

**Lower bound.** Take A dyadic (m = n+1 parts). By Lemma LB1, every refinement B satisfies
S(B) ≥ Δ(A) = 1/D_n; so min_B S(B) ≥ 1/D_n, whence
  **max_A min_B S(B) ≥ 1/D_n.**                    (4.1)

### 5. Final answer

Combining (2.1) and (4.1), max_A min_B S(B) = 1/D_n, which is exactly (0.2). By (0.1),
  c(n) = (1 + 1/D_n)/2 = (D_n + 1)/(2 D_n) = 2^{n+1}/(2 D_n) = 2^n/D_n = **2^n/(2^{n+1} − 1).**

*Verification.* n = 1: c(1) = 2/(2^2 − 1) = 2/3, matching the fully-proven base case in current.md.
The two bounds meet exactly at the dyadic profile: for dyadic A, §2 (m = n+1 pigeonhole) gives XY a
refinement with S(B) = 1/D_n (the subset sums are all k/D_n, the closest distinct pair differs by
1/D_n), while §3–4 show no refinement does better; so min_B S(B) = 1/D_n is attained, confirming
tightness. ∎

## Promotable lemmas

- **UB1 (merge-alignment refinement).** For A with m parts summing to 1 and disjoint S,T ⊆
  {1,…,m}, (S,T) ≠ (∅,∅), XY has a refinement B using ≤ m−1 splits with S(B) ≤ |Σ(S)−Σ(T)|.
  Proved in §1 from L4 (min-pairing on the output multiset) and an explicit cut-budget count.
- **UB2 (subset-sum pigeonhole).** For A with n+1 parts summing to 1, some disjoint S,T with
  |Σ(S)−Σ(T)| ≤ 1/D_n exist (pigeonhole: 2^{n+1} subset sums vs D_n cells). §2.
- **LB1 (tree-extraction lower bound).** For A with n+1 parts, every ≤ n-split refinement B has
  S(B) ≥ Δ(A) := min_{ε∈{−1,0,1}^{n+1}, ε≠0} |Σ ε_i a_i|. Proved in §3 via the (n+2)-vertex,
  ≤(n+1)-edge multigraph, cycle-rank tree-component existence, and the bipartition sign identity;
  all edge cases (isolated dummy, self-loops, no isolated part) handled.
- **LB2 (dyadic Δ).** For a_i = 2^{i−1}/D_n, Δ = 1/D_n (integer minimality of {−1,0,1}-combos of
  powers of 2). §4.

These four, plus the certified L0–L2, L4, give a complete self-contained solution of imo-2026-03.
