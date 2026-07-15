# imo-2026-03 — tracking file (reviewer-owned)

## Status
solved

## Approaches tried
- **pairing-defect-strategy-family** — worked (round 1, APPROVED). Complete proof: claiming value = Odd(P) (Lemma C); defect layer-cake identity + pairing duality; upper bound via subset-sum pigeonhole (2^{n+1} sums vs D = 2^{n+1}−1 intervals) + merge process realizing the small signed difference with ≤ n legal marks; lower bound via geometric configuration (pieces 2^j/D) + tree-component ±1-signing + uniqueness of binary representation. Independently re-derived and computationally verified by the reviewer (exact rationals, n = 1..4; numeric minimization at n = 1..3).
- **self-similar-induction** — worked (round 1, APPROVED). Independent complete write-up of the same core mechanism (its original induction line was superseded mid-round): Lemma R superposition realization + pigeonhole for the upper bound; home-graph tree lemma (Lemma T) + dyadic dissociation (Lemma G) for the lower bound. Also verified independently by the reviewer, including its distinct Lemma R construction and mark ledger.
- **exact-value-function** — partial (round 1, honest status). LP/vertex classification of Xiang Yu's best response (Lemma V), integer-vertex parity (its Lemma P), Chain Lemma, cases (a)/(b) of the upper bound — all correct; gaps E2 (deficient case) and E3′ (fractional vertices) remained open and are now subsumed by the solved siblings. No further work needed.

## Current best
Solved. **c(n) = 2^n/(2^{n+1} − 1).** Full proof below (primary write-up from pairing-defect-strategy-family; an independent equivalent write-up is in `approaches/self-similar-induction.md`). Certified reusable lemmas in `lemmas/`: claiming-value, defect-identity, fewer-marks, upper-bound-pigeonhole-realization, lower-bound-tree-signing.

## Full proof

**Problem.** Liu Bang (LB) marks at most n points on a stick of length 1; then Xiang Yu (XY), seeing them, marks at most n further points, all marked points distinct. The stick is cut at all marked points. The players alternately claim unclaimed pieces, LB first, each maximizing the total length claimed. Determine the largest c such that LB can guarantee at least c.

**Answer.** c(n) = 2^n/D where D := 2^{n+1} − 1.

Throughout, for a finite multiset P of nonnegative reals sorted decreasingly p_1 ≥ p_2 ≥ ⋯ (any tie-breaking), write
Odd(P) = p_1 + p_3 + ⋯, Even(P) = p_2 + p_4 + ⋯, defect(P) = Odd(P) − Even(P) ≥ 0,
and N_P(x) = #{i : p_i > x} for x ≥ 0 (independent of tie-breaking), E_P = {x > 0 : N_P(x) odd}.

### Section 0: Conventions and degenerate marks

Marks are distinct; interior marks create positive pieces, and only endpoint marks can create length-0 pieces (or no piece, depending on convention). Appending zero-length pieces to P changes neither Odd(P) nor Even(P): zeros sort last and contribute 0, and the positive pieces keep their positions. Lemma C below is stated and proved for multisets of nonnegative reals, so either convention is covered; we identify a post-cutting position with the multiset P of piece lengths.

### Section 1: Lemma C (claiming value)

**Lemma C.** In the alternating claiming game on a finite multiset P of nonnegative reals (first player moves first; a move claims any unclaimed piece; each player maximizes his own total), optimal play gives the first player exactly Odd(P) and the second exactly Even(P).

*Proof.* Since Odd(P) + Even(P) = ΣP and the total is fixed, it suffices to prove the two one-sided guarantees; each then must be exact.

(i) *First player guarantees ≥ Odd(P).* Induction on |P|. For |P| ≤ 1 clear. Otherwise he claims p_1 and then follows the strategy of (ii) as second player on P′ = P ∖ {p_1} (whose sorted list is p_2 ≥ p_3 ≥ ⋯), collecting in addition at least Even(P′) = p_3 + p_5 + ⋯. Total ≥ p_1 + p_3 + ⋯ = Odd(P).

(ii) *Second player guarantees ≥ Even(P).* Induction on |P|. For |P| ≤ 1, Even(P) = 0. Suppose the first player claims p_j.
- If j = 1: reply p_2; by induction on Q = P ∖ {p_1, p_2} (the original first player moves first in the remaining game), collect in addition ≥ Even(Q) = p_4 + p_6 + ⋯. Total ≥ p_2 + p_4 + ⋯ = Even(P).
- If j > 1: reply p_1; let Q = P ∖ {p_1, p_j} with sorted list q_1 ≥ ⋯ ≥ q_{|P|−2}, where q_i = p_{i+1} for i ≤ j−2 and q_i = p_{i+2} for i ≥ j−1; in both cases q_i ≥ p_{i+2}. Hence
  Even(Q) = Σ_{i even} q_i ≥ Σ_{i even} p_{i+2} = p_4 + p_6 + ⋯ = Even(P) − p_2,
  the index ranges matching exactly. By induction the total is ≥ p_1 + Even(Q) ≥ p_1 + Even(P) − p_2 ≥ Even(P), since p_1 ≥ p_2. ∎

**Consequence.** After the cutting phase produces P, LB's optimal-play take is exactly Odd(P) = (1 + defect(P))/2 (when ΣP = 1). Hence
c(n) = sup_{LB markings} inf_{XY replies} Odd(P),
and everything reduces to the defect.

### Section 2: Lemma D (defect identity) and Lemma P (pairing duality)

**Lemma D.** defect(P) = |E_P| (Lebesgue measure).

*Proof.* By the layer-cake formula p_i = ∫_0^∞ 𝟙[p_i > x] dx,
defect(P) = Σ_i (−1)^{i−1} p_i = ∫_0^∞ Σ_i (−1)^{i−1} 𝟙[p_i > x] dx.
For fixed x the pieces exceeding x are exactly p_1, …, p_{N_P(x)}, so the integrand is Σ_{i=1}^{N_P(x)} (−1)^{i−1} = 𝟙[N_P(x) odd]. ∎

**Corollary D0 (Δ-additivity).** N_{P⊎Q} = N_P + N_Q, hence E_{P⊎Q} = E_P Δ E_Q and defect(P ⊎ Q) = |E_P Δ E_Q| ≤ defect(P) + defect(Q).

**Corollary D1 (strip pairs).** Removing an exactly equal pair {a, a} leaves the defect unchanged (E_{\{a,a\}} = ∅; apply D0).

**Corollary D2 (pairs + leftovers).** If P consists of equal pairs plus a leftover sub-multiset L, then defect(P) = defect(L) ≤ ΣL, so Odd(P) = (ΣP + defect(P))/2 ≤ (ΣP + ΣL)/2.

**Lemma P (pairing duality).** A *pairing* of P is a partition of the multiset into unordered pairs {a, b} and singletons ℓ (*leftovers*); its *cost* is Σ_{pairs} |a − b| + Σ_{leftovers} ℓ. Then defect(P) = min over pairings of the cost.

*Proof.* (≤) Any pairing partitions P into blocks of size ≤ 2; by D0, defect(P) ≤ Σ defect({a,b}) + Σ defect({ℓ}) = Σ |a−b| + Σ ℓ. (≥) The consecutive sorted pairing {p_1, p_2}, {p_3, p_4}, … (last piece a leftover if |P| is odd) costs Σ_{i odd} (p_i − p_{i+1}) = defect(P). ∎

### Section 3: Lemma F (fewer marks)

**Lemma F.** If LB's marks produce at most n positive pieces (fewer than n marks, or marks wasted at endpoints), XY can hold LB to exactly 1/2 < 2^n/D.

*Proof.* Let the positive pieces be r ≤ n. XY marks the midpoint of each (r ≤ n marks, strictly interior to pieces, hence distinct from all existing marks). The final multiset is r equal pairs; by D2 with L = ∅ and Lemma C, LB gets 1/2. Finally 2^n/D = (D+1)/(2D) = 1/2 + 1/(2D) > 1/2. ∎

So for the upper bound we may assume LB uses exactly n interior marks, creating pieces q_1, …, q_{n+1} > 0 with Σ q_i = 1; the bound to prove is that XY can force defect ≤ 1/D, since (1 + 1/D)/2 = 2^n/D.

### Section 4: Theorem UB (upper bound)

**Theorem UB.** For every LB marking, XY has a reply using at most n marks such that LB's optimal-play take is at most 2^n/D. Hence c(n) ≤ 2^n/D.

*Proof.* By Lemma F assume pieces q_1, …, q_m > 0 with m = n + 1 and Σ q_i = 1; note D = 2^m − 1.

**Step 1 (pigeonhole on subset sums).** The 2^m subsets X ⊆ {1, …, m} have sums Σ_{i∈X} q_i ∈ [0, 1]. Partition [0, 1] into the D intervals [(t−1)/D, t/D), t = 1, …, D−1, and [(D−1)/D, 1]. Since 2^m = D + 1 > D, two distinct subsets X ≠ Y have sums in the same interval, so |Σ_X q − Σ_Y q| ≤ 1/D. Put A = X ∖ Y, B = Y ∖ X: disjoint index sets, not both empty (X ≠ Y), and after cancelling X ∩ Y,
|Σ_{i∈A} q_i − Σ_{i∈B} q_i| ≤ 1/D.
WLOG δ := ΣA − ΣB ∈ [0, 1/D] (else swap names). Possibly B = ∅, in which case ΣA = δ ≤ 1/D.

**Step 2 (merge process).** XY maintains two lists of current (physical) pieces, initialized as the LB-pieces indexed by A and by B, and repeats while both lists are nonempty: pick any a from list A and b from list B.
- If a = b: retire {a, b} as an equal pair (0 marks); delete both.
- If a > b: place one mark strictly inside piece a, at distance b from its left end, splitting it into pieces of lengths b and a − b; retire the new length-b piece with b as an equal pair; delete b from list B and replace a by a − b in list A (1 mark).
- If a < b: symmetric (split b into a and b − a).
Each step preserves ΣA − ΣB = δ and deletes at least one list element, so the process terminates with one list empty. It cannot terminate with A = ∅ ≠ B, since then ΣB = −δ ≤ 0 while pieces are positive. So it ends with B = ∅ and a final list A_fin (possibly empty), ΣA_fin = δ ≤ 1/D; its members are retired as leftovers. Finally XY halves every LB-piece not indexed by A ∪ B (one interior mark each).

**Step 3 (mark ledger and legality).** Let s = |A| + |B| initially. Each merge step uses ≤ 1 mark and deletes ≥ 1 element; steps with a = b delete two elements and use 0 marks. If A_fin ≠ ∅, merge marks ≤ s − |A_fin| ≤ s − 1; total marks ≤ (m − s) + (s − 1) = m − 1 = n. If A_fin = ∅, the last step must have a = b (only such a step empties both lists), so merge marks ≤ s − 2 and the total is ≤ n − 1. If B = ∅ from the start, there are no merge steps and the total is m − |A| ≤ n. Every mark is placed strictly inside a current piece, whose interior contains no earlier marks (earlier marks are piece boundaries); hence all marks are distinct from each other and from LB's marks. All XY replies here use at most n marks, as required.

**Step 4 (value).** The final multiset P consists of equal pairs (halved pieces and retired merge pairs) plus the leftovers A_fin with ΣA_fin = δ ≤ 1/D. By Corollary D2, defect(P) ≤ 1/D, so by Lemma C LB obtains
Odd(P) = (1 + defect(P))/2 ≤ (1 + 1/D)/2 = 2^n/D. ∎

### Section 5: Theorem LB (lower bound)

LB marks the n points (2^k − 1)/D, k = 1, …, n (distinct, interior), creating the *geometric configuration*
G_n : blocks g_j of length 2^j u for j = 0, 1, …, n, where u := 1/D (total (2^{n+1} − 1)u = 1).

**Theorem LB.** Let P be any refinement of G_n obtained by cutting the blocks at no more than n additional points (XY's marks; distinct from LB's marks, so each block g_j is partitioned into c_j + 1 positive pieces with Σ_j c_j = k ≤ n; endpoint or wasted marks only decrease k). Then defect(P) ≥ u. Consequently, by Lemma C, LB's take is (1 + defect(P))/2 ≥ (1 + 1/D)/2 = 2^n/D against every XY reply, i.e. c(n) ≥ 2^n/D.

*Proof.* By Lemma P it suffices to show that **every pairing μ of P costs at least u**.

**The pair graph.** P has (n + 1) + k ≤ 2n + 1 pieces, so μ has at most ⌊(2n+1)/2⌋ = n pairs. Define a multigraph H on the vertex set {0, 1, …, n} (one vertex per block): for each μ-pair {a, b}, put an edge joining the block containing a to the block containing b (a loop if they are sub-pieces of the same block). Then H has n + 1 vertices and at most n edges.

**A tree component exists.** Summing over connected components C of H: Σ_C e(C) ≤ n < n + 1 = Σ_C v(C), so some component C has e(C) < v(C). A connected multigraph satisfies e ≥ v − 1, with equality iff it is a tree (acyclic; in particular loopless and without parallel edges, since loops and parallel edges are cycles). So C is a tree on the block set V(C) ≠ ∅.

**Signing and telescoping.** Two-color the tree C properly: ε_j ∈ {+1, −1} for j ∈ V(C) with opposite signs on adjacent blocks. Key closure property: every μ-pair containing a piece of a block in V(C) is an edge of C (by definition of connected component), so its other piece also lies in a block of V(C). Therefore each piece of each block j ∈ V(C) is either matched along an edge of C or is a leftover. Since block j has total mass 2^j u,
Σ_{j∈V(C)} ε_j 2^j u = Σ_{edges {a,b} of C} (ε_{j(a)} a + ε_{j(b)} b) + Σ_{leftovers ℓ in blocks of V(C)} ε_{j(ℓ)} ℓ,
and for each edge, ε_{j(a)} = −ε_{j(b)}, so ε_{j(a)} a + ε_{j(b)} b = ±(a − b). Taking absolute values,
|Σ_{j∈V(C)} ε_j 2^j| · u ≤ Σ_{edges of C} |a − b| + Σ_{leftovers in V(C)} ℓ ≤ cost(μ).

**Binary uniqueness.** The integer Σ_{j∈V(C)} ε_j 2^j is a nonempty signed sum of distinct powers of 2 with coefficients ±1; it is nonzero, since Σ_{j: ε_j = +1} 2^j = Σ_{j: ε_j = −1} 2^j would equate the sums of two disjoint sets of distinct powers of 2, contradicting uniqueness of binary representation (one of the two sets is nonempty; if the other is empty the sum is a nonempty sum of distinct powers, again nonzero). Hence |Σ_{j∈V(C)} ε_j 2^j| ≥ 1 and cost(μ) ≥ u. ∎

*Tightness.* XY halving each of g_1, …, g_n (n marks) leaves n equal pairs {2^{j−1}u, 2^{j−1}u} plus the leftover g_0 = u, so defect = u exactly and LB gets exactly 2^n/D: the bound of Theorem LB is attained, and it matches Theorem UB at the same configuration.

### Section 6: Conclusion and verification

By Theorem UB, c(n) ≤ 2^n/D; by Theorem LB (with the geometric marking), c(n) ≥ 2^n/D. Hence
**c(n) = 2^n/(2^{n+1} − 1).**
Both bounds are attained by explicit strategies meeting at the geometric configuration with XY's halving reply, where LB's take is exactly 2^n/D.

Verification of the answer: n = 1: 2/3 (matches exact-fraction minimax over a grid, reviewer-run); n = 2: 4/7; n = 3: 8/15. Formula sanity: c(n) = 1/2 + 1/(2D) → 1/2 as n → ∞, and c(n) > 1/2 always (LB can always secure ≥ 1/2 by Lemma D nonnegativity; XY can always come within 1/(2D) of 1/2 by Theorem UB). ∎

### Reviewer verification record (round 1)

- Lemma C: brute-force game-tree search matches Odd(P) on 300 random multisets (ties and zeros included).
- Theorem UB: independent re-implementation of both the merge process and the superposition realization (self-similar-induction Lemma R) in exact rationals; 400 random configurations for each n = 1..4 — marks ≤ n and defect ≤ 1/D always, defect equal to the leftover total exactly.
- Theorem LB: multistart numerical minimization over all cut assignments gives min defect exactly 1/D at n = 1, 2, 3.
- n = 1 minimax on an exact-fraction grid returns 2/3.
