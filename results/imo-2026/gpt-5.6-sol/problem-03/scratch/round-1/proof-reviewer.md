## threshold-parity-toggles

**Verdict: APPROVE**  
**True Status: solved** (the builder's `solved` label is correct)

**Scores**
- Correctness: 10/10
- Completeness / rigor: 9.5/10
- Progress: 10/10

The proof answers the actual compute-and-prove question and explicitly gives
\[
\boxed{c_n=\frac{2^n}{2^{n+1}-1}}.
\]
It proves both minimax directions with legal strategies.

### Adversarial verification

1. **Drafting reduction.** The backward induction is valid. After removal of rank \(j\), the opponent's value is the odd-ranked sum of the remaining list. The displayed comparison with \(P(b)\) is a sum of nonnegative adjacent differences, and taking \(b_1\) attains equality. Non-strict inequalities correctly cover ties. Hence Liu's value for a fixed terminal multiset is its odd-ranked sum and
   \[
   P=(1+D)/2.
   \]

2. **Layer-cake and toggle identities.** Independently re-deriving at a threshold \(t\), the sorted alternating indicator sum is \(1\) precisely when the number of surviving pieces is odd, proving \(D=|E|\). Replacing one actual current piece \(x\) by \(u\le v\), \(u+v=x\), changes the survivor count by one on \((0,u]\), zero on \((u,v]\), one on \((v,x]\), and zero above \(x\). Thus the toggle formula is correct and is provenance-safe under repeated cuts.

3. **Load-bearing lower-bound lemma, independently checked.** With exactly \(n\) cuts there are \(2n+1\) fragments and therefore \(n\) ranked pairs. The provenance multigraph has \(n+1\) parent vertices and \(n\) edges, so at least one component has \(e=v-1\) and is a genuine tree; loops or parallel-edge cycles would force \(e\ge v\). Bipartitioning that tree signs every paired edge oppositely. Regrouping all descendant mass gives the signed parent-mass sum on the left and ranked-pair differences, plus the possible singleton, on the right. The signed sum of distinct powers of two is nonzero because its largest term exceeds the sum of every possible smaller term; being an integer, its magnitude is at least one. Therefore the global alternating discrepancy is at least one. I also stress-tested arbitrary repeated random cuts for \(n=1,\ldots,7\); no value below one occurred. The algebraic-zero padding for fewer cuts preserves parent totals and discrepancy and gives exactly the required graph counts, so it is legitimate as a proof device.

4. **Load-bearing upper-bound lemma, independently checked.** Among \(2^V\) subset sums in \([0,S]\), either two coincide or an adjacent pair differs by at most \(S/(2^V-1)\). Removing their intersection gives disjoint \(A,B\) with mass excess \(d\) in the stated range. In the greedy transport, each step extinguishes at least one current remainder. For \(d>0\), if \(r\) positive \(A\)-remainders survive, this gives \(e\le |A|+|B|-r\); hence the fragment count gives at most \(|A|+|B|-r\) cuts in those parents. Bisecting \(C\) raises the total to at most \(V-r\le V-1=n\). Removing equal pairs leaves total residual mass \(d\), whose discrepancy cannot exceed \(d\). For \(d=0\), the final transport step extinguishes both sides and improves the count by one, producing discrepancy zero. The separate \(B=\varnothing\) case is valid: bisecting all but one \(A\)-parent and every \(C\)-parent costs exactly \(V-1\), and the sole unpaired mass is at most the total mass \(d\). For \(V\le n\), bisecting all residual fragments uses at most \(V\) cuts and leaves only equal pairs. These cases are exhaustive.

5. **Legality and minimax quantifiers.** Every prescribed parent fragmentation consists of positive lengths, and successive partial sums give distinct interior marks in that parent; different Liu intervals are disjoint, so marks from different parents cannot coincide. Thus no limiting or perturbation argument is needed. Liu's dyadic marks are distinct and interior. If Liu uses all \(n\) marks, the upper construction applies with \(V=n+1\); if he uses fewer, \(V\le n\) and Xiang can force \(D=0\). Consequently the proof covers every Liu strategy and provides a legal Xiang response. The lower strategy works against every legal Xiang response with at most \(n\) marks. The algebra converting \(D=1/Q\) to the share is correct because \(Q+1=2^{n+1}\).

The source had one typographical form-feed character in equation (14), turning `\frac` into malformed text. This was corrected in reviewer-owned `current.md`; it was not a mathematical gap.

**Recorded outcome:** `verified-milestone` — complete provenance-tree lower bound and subset-sum transport upper bound verified.

**Promotable lemmas certified:**
- Dyadic refinement lemma.
- Universal refinement lemma.
- Single-refinement threshold-toggle lemma.
- The overlapping greedy-drafting and layer-cake lemmas were also certified from the independently proved versions in the other built approach.

## dyadic-reserve-induction

**Verdict: CHANGES REQUESTED**  
**True Status: partial** (the builder's `partial` label is correct)

**Scores**
- Correctness: 9/10 for the claims actually proved
- Completeness / rigor: 6/10
- Progress: 7/10

This file establishes rigorous reusable infrastructure: the finite drafting lemma with ties, \(P=(1+D)/2\), the layer-cake identity, the exact provenance-safe split toggle, legality of Liu's dyadic marking, the full \(n=1\) case, and the correct approximation quantifier if zero fragments were ever used. Its case analysis for \(n=1\) is exhaustive and legal.

It is not a whole-problem solution for general \(n\). The precise missing load-bearing steps are the two statements explicitly identified at lines 20–25:

1. prove that every refinement of parent masses \(1,2,\ldots,2^n\) by at most \(n\) legal binary cuts has alternating discrepancy at least \(1\);
2. prove that every collection of at most \(n+1\) positive parent masses admits, using at most \(n\) provenance-respecting cuts, discrepancy at most \(1/(2^{n+1}-1)\) (or the stated sufficient approximation).

Neither the layer-cake formula nor the one-cut toggle identity implies either global inequality: an admissible toggle can increase or decrease odd-threshold measure, and a sequence of abstract toggles need not correspond to cuts of existing descendants. Therefore this slug remains `partial`. The technique is viable and these gaps can in fact be closed by the tree-provenance and subset-sum transport arguments verified in `threshold-parity-toggles`, but those arguments are absent from this approach file and cannot be silently imported into its status.

**Exact requested change:** incorporate complete proofs of both quantified all-\(n\) refinement inequalities, with cut counts and provenance/positivity checked. Merely repeating reserve or threshold-charging language would not suffice.

**Recorded outcome:** `advanced` — rigorous reductions and the exact \(n=1\) solution were established, while both all-\(n\) refinement inequalities remain open in this slug.

**Promotable lemmas certified:**
- Greedy drafting lemma.
- Alternating discrepancy layer-cake lemma.
- Single-refinement toggle lemma.
- Exact solution for one mark.

The certified statements were written to `results/imo-2026-03/lemmas/`. No promotable lemma was rejected.

## Goal Progress

**Status: solved.** The problem is solved by the approved `threshold-parity-toggles` approach, and reviewer-owned `results/imo-2026-03/current.md` now contains the complete verified proof.

**Raw ranking signal after outcome recording:**
- `threshold-parity-toggles`: Elo 1516.0, expanded 1, last outcome `verified-milestone`, stale `true` pending the next outline-reviewer Elo fold.
- `dyadic-reserve-induction`: Elo 1484.0, expanded 1, last outcome `advanced`, stale `true` pending the next outline-reviewer Elo fold.
