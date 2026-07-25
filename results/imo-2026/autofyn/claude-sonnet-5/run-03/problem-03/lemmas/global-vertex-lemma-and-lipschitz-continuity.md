## Global Vertex Lemma and Lipschitz continuity of $V(p)$

Certified round 8. Proved in `approaches/global-lp-vertex-sufficiency.md`
(round 8, Sections 1–2), a new approach opened this round.

**Setup.** By the certified Reduction Lemma
(`lemmas/reduction-to-multiset-minimax.md`), the game value is
$c(n)=\max_p V(p)$ where $V(p):=\min_{\mathbf m,\text{splits}}
\mathrm{OddSum}(\text{resulting multiset})$ over LB partitions
$p=(p_1,\ldots,p_k)$, $k\le n+1$.

**Global Vertex Lemma (fully proved, assembly of already-certified
content — Vertex Pinning Lemma, Single-Piece-Split Vertex Lemma,
Two-Piece-Split Vertex Lemma).** For fixed $n,k$, there is a finite,
$p$-independent set $\Sigma(n,k)$ of combinatorial "shapes" (cut
allocation + block partition + pin assignment, generalizing the
single/two-piece constructions to any number of simultaneously-split
pieces), each giving an affine-in-$p$ candidate response formula
$x_\sigma(p)$, such that
$$V(p)=\min_{\sigma\in\Sigma,\ x_\sigma(p)\ge0}\mathrm{OddSum}(x_\sigma(p)\cup(\text{untouched }p_j\text{'s})).$$

**Reviewer assessment.** This is a genuine, correctly-justified
generalization: the underlying vertex-characterization argument (a
feasible point of a polyhedron cut out by piece-sum equalities and
order/nonnegativity half-spaces is extreme iff active constraints have
full rank) is exactly the mechanism already spelled out in full, certified
detail in `lemmas/single-piece-split-vertex-lemma.md` and
`lemmas/two-piece-split-vertex-lemma.md`; the claim that it extends
verbatim to any number of simultaneously-split pieces (each contributing
its own independent free block) is a correct, purely local
linear-algebra fact — no new proof technique is needed, and none is
smuggled in. Certified.

**Lipschitz continuity of $V$ (new, fully proved).** For $p,p'$ in the
simplex with the same $k$: $|V(p)-V(p')|\le\|p-p'\|_1$.

*Proof sketch (verified by the reviewer).* Take an optimal response to
$p$ with fragment proportions $\lambda_{i,j}$ per split piece $i$; apply
the identical cut-allocation and proportions to $p'$, giving a legal
response $M'$ to $p'$. Canonically matching $M$ and $M'$ element-by-element
(same piece, same proportion-slot), the total absolute difference is
exactly $\sum_i|p_i-p_i'|=\|p-p'\|_1$ (using $\sum_j\lambda_{i,j}=1$). Since
$\mathrm{OddSum}$ is 1-Lipschitz w.r.t. **any** fixed bijective matching
between two same-size multisets (rank-by-rank in each one's own sorted
order gives the bound via a triangle inequality, and the sorted-rank
matching is the $\ell^1$-optimal-transport minimum, so any other bijection's
total upper-bounds it — a standard rearrangement fact, correctly invoked
here only for an upper bound, not an equality), $\mathrm{OddSum}(M')\le
\mathrm{OddSum}(M)+\|p-p'\|_1=V(p)+\|p-p'\|_1$. By symmetry, $|V(p)-V(p')|
\le\|p-p'\|_1$. $\blacksquare$

**Reviewer check.** The direction of the rearrangement-inequality
invocation (sorted matching minimizes $\ell^1$ transport cost, so the
canonical proportional matching — generally not sorted — gives a valid
upper bound, not a lower bound) is used correctly in the proof; this is
the one place a sign error could hide and it does not occur. The proof is
elementary and self-contained. Certified.

**Consequence (existence of a maximizer, fully proved but modest).** The
closed balanced region is compact and $V$ is continuous (Lipschitz) on it,
so $\sup_p V(p)$ is attained by the extreme value theorem. This gives no
characterization of the maximizer.

**What remains open (not resolved, not claimed).** Concavity of $V(p)$ —
which would let the maximization reduce to finitely many extremal
configurations — is neither proved nor disproved. The approach file
correctly identifies why the classical "LP value is convex in the RHS"
fact does not transfer here (the parameter $p$ enters the objective
directly, not just the constraint RHS), and reports a small, inconclusive
numerical check (15 trials at $n=2$, no violation found but not
exact-arithmetic) honestly as weak evidence only. This approach does
**not** establish the Existence Theorem or any part of the whole
`imo-2026-03` problem; it is a structural toolkit (finite-vertex
structure + continuity) whose main open step (concavity, or a substitute)
is precisely and honestly located.
