## subset-folding-dyadic-frontier

**Verdict:** APPROVE  
**True Status:** solved (agrees with the builder's recorded Status)  
**Ranking outcome:** `verified-milestone` — already recorded exactly once for round 2; the existing ranking-tool record was retained rather than incorrectly incrementing `expanded` a second time.

### Scores
- **Correctness:** 10/10
- **Completeness / rigor:** 10/10
- **Progress:** 10/10

### Adversarial verification

The candidate answers the actual compute-and-prove problem for every positive integer \(n\), explicitly obtaining
\[
c_n=\frac{2^n}{2^{n+1}-1},
\]
and proves both Liu Bang's guarantee and Xiang Yu's matching upper-bound strategy.

1. **Claiming phase.** The backward induction is valid. After choosing rank \(i\), comparison with the value obtained by choosing \(x_1\) produces exactly the displayed sum of adjacent nonnegative differences. Thus the first player's game value is the odd-rank sum, including ties and both parities of the number of pieces. Independently, I exhaustively recomputed the minimax value for every nonincreasing integer multiset of at most eight pieces with entries in \(\{1,\ldots,5\}\); every value equaled its odd-rank sum.

2. **Load-bearing lower-bound lemma, independently re-derived.** If \(s\le m-1\) splits are made, pairing adjacent final ranks creates
\[
e=\left\lfloor\frac{m+s}{2}\right\rfloor\le m-1
\]
edges on the \(m\) original-parent vertices. Hence some connected component has fewer edges than vertices; as it is connected, it is a tree. Bipartition that tree. The two bipartition classes are different subsets, so their parent-sum difference has magnitude at least \(d\). Every descendant of a vertex in the component appears as an endpoint of one of the component's rank-pair edges, except possibly the unique globally unmatched final piece. Therefore the triangle inequality bounds the parent-sum difference by the corresponding sub-sum of the nonnegative adjacent-rank differences defining \(D\). Hence \(D\ge d\). Loops and parallel-edge cycles are correctly excluded from a tree component, while an isolated vertex is correctly handled using the empty opposite class and, necessarily, the unmatched piece. I also exhaustively checked all integral refinements of dyadic parents for \(m\le5\) under the split budget; none has \(D<1\).

3. **Liu Bang's guarantee.** The normalized powers \(1,2,\ldots,2^n\) sum to \(T=2^{n+1}-1\), and distinct subset sums differ by at least \(1/T\). Xiang Yu's at most \(n=m-1\) new marks are precisely at most \(m-1\) splits of the parent pieces. The lemma gives \(D\ge1/T\), and therefore Liu Bang receives at least
\[
\frac{1+1/T}{2}=\frac{2^n}{T}.
\]
All initial marks are legal distinct interior points.

4. **Consecutive-subset-sum step.** The \(2^m-1\) adjacent gaps between the ordered subset sums telescope to \(1\), even with repeated sums, so one gap \(r\) is at most \(1/(2^m-1)\). After cancelling common indices, the positive and negative supports are disjoint. For each \(p\in P\), the inequality \(a_p<r\) would place the subset sum of \(L\cup\{p\}\) strictly inside the chosen consecutive gap; thus \(a_p\ge r\). When \(N=\varnothing\), this forces \(P\) to be a singleton. When \(r=0\), positivity forces both supports to be nonempty.

5. **Folding legality and cut count.** Placing a selected \(p_*\in P\) last and using \(a_{p_*}\ge r\) ensures all preceding positive parents end by \(B=A-r\), so the entire residual interval \([B,A]\) lies in one parent. The common refinement on \([0,B]\) creates equal pairs. Each internal boundary from one concatenation requires at most one cut on the other side; truncation at \(B\) requires at most one more. Thus the supported construction uses at most \(s-1\) cuts for \(r>0\), or \(s-2\) for \(r=0\). Halving every zero-sign parent adds \(m-s\) cuts. Every counted cut lies strictly inside one original parent, so it is a legal mark distinct from Liu Bang's marks; coincidences only lower the count.

6. **Matching obstruction and case completeness.** For \(m=n+1\), Xiang Yu uses at most \(n\) marks and leaves equal pairs plus residual \(r\). Since every paired value has even multiplicity, while the residual makes exactly its value block odd, the globally sorted odd-rank sum is
\[
H+r=\frac{1+r}{2}\le\frac12\left(1+\frac1{2^{n+1}-1}\right)=\frac{2^n}{2^{n+1}-1}.
\]
This remains valid if the residual equals one of the paired lengths. For \(m\le n\), the \(r=0\) construction pairs everything; for \(r>0\), one additional cut halves the residual, using at most \(m\le n\) marks. Either way Liu Bang then receives exactly \(1/2\). These cases are exhaustive. The explicit dyadic equality strategy and the edge case \(n=1\) also check.

No circularity, omitted case, unsupported crux reference, or incorrect final-answer computation was found.

### Promotable lemmas
- **Tree-component discrepancy lemma:** certified and admitted as `results/imo-2026-03/lemmas/tree-component-discrepancy.md`.
- **Consecutive-subset-sum folding lemma:** certified and admitted as `results/imo-2026-03/lemmas/consecutive-subset-sum-folding.md`; the file explicitly treats a zero residual as absent.
- **Odd-rank draft lemma:** certified and admitted as `results/imo-2026-03/lemmas/odd-rank-draft.md`.

`/home/agentuser/repo/results/imo-2026-03/current.md` already contains the candidate's verified solved proof in the required contract and remains current.

## Goal Progress

- **Raw current Status:** `solved`
- **Raw final expression:** `2^n/(2^(n+1)-1)`
- **Raw ranking record:** slug `subset-folding-dyadic-frontier`; Elo `1500.0`; expanded `1`; last outcome `verified-milestone`; last round `2`; stale `true`.
- **Raw ranking note:** `Complete minimax proof verified: draft identity, tree-component lower invariant, legal folding cut count, and matching upper bound all check out.`
- **Goal result:** complete guarantee and matching obstruction verified; target met.
