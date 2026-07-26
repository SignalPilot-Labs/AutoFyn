# proof-builder — p1-equals-2-direct — round 3

## Status
partial

## What I proved (unconditional, in `results/imo-2026-06/approaches/p1-equals-2-direct.md`)

Two clean structural lemmas for the $|P_1|=2$ NON-LOCK regime, both verified computationally on 8 starting values ($15,35,65,77,91,143,175,847$) and cross-checked against the $|P_1|=3$ case $385$:

1. **`two-entry-lemma` (Step 2).** For $|P_1|=2$ NON-LOCK ($a_1=p^kq$, $p<q$ odd primes, no prime-power term reached), $a_2=a_1+p_{\rm sm}=p_{\rm sm}(p_{\rm sm}^{k-1}q+1)$ is even — equivalently $2\in S(a_2)$, so the prime $2$ enters the active support at $n=2$. Proof: elementary (smallest $p$-multiple above $a_1$ is $a_1+p$; no $m\in(a_1,a_1+p)$ shares a $P_1$-prime; $p^{k-1}q+1$ even since $p,q$ odd). This is the genuinely $|P_1|=2$-specific lever (no single prime dominates for $|P_1|\ge3$). **Promotable to the shared cache.**

2. **`P1-minimal-transversal-lemma` (Step 3).** For $|P_1|=2$ NON-LOCK, $P_1=\{p,q\}$ is itself a minimal transversal of $\mathcal F_\infty$; in particular both $p,q$ are governing. Proof: linchpin ($P_1$ is a transversal) + the implication "$p\mid a_n\,\forall n\Rightarrow a_{n+1}=a_n+p\,\forall n\Rightarrow$ a power $p^j$ is reached $\Rightarrow$ LOCK" (so NON-LOCK forbids $\{p\}$ and $\{q\}$ being transversals). **Promotable.**

Also re-verified computationally the cofactor-bound conjecture (every governing prime $\le M_1=\operatorname{rad}(a_1)$) for all 8 NON-LOCK cases incl. the outliers $a_1=847$ (gov $41\le77$), $a_1=175$ (gov $13\le35$), and $a_1=385$ (gov $19\le385$). Periods ($T,L$) recomputed from scratch with $\ge500$-term diff-match windows; all agree with the explorer's table.

## Gaps remaining

**Step 4 — the cofactor-bound wall (Gap A specialized to $|P_1|=2$) — OPEN.** I could not prove that every governing prime $r\in\bigcup\operatorname{MT}(\mathcal F_\infty)$ satisfies $r\le M_1$. The hoped $2$-density mechanism is REFUTED:

- **Counterexample to "smallest-admissible is always $2$-divisible":** $a_1=15=3\cdot5$, $a_8=42$, the smallest admissible $m>42$ is $a_9=45=3^2\cdot5$ (odd); $44=2^2\cdot11$ is inadmissible because $\{2,11\}\cap\{3,5\}=\varnothing$.
- **$v_2(a_n)$ does not stabilize:** for $a_1=15$, $v_2$ takes all values in $\{0,1,2,3,4,5\}$ over $n=1,\dots,40$ and fluctuates throughout (consistent with the round-2 $a_1=385$ finding).

So the $2$-density lever is a real statistical bias (most terms even) but does NOT rigidify witness cofactors, and the strip (`lemma-C-strip-no-go`, certified dead round 2) is not re-attempted. Conditional on the cofactor bound, the certified endgame (`distinct-supports-stabilize` + `greedy-equals-cyclic-successor` + `cyclic-successor-bijection`) solves $|P_1|=2$ NON-LOCK from $n=1$; the general $|P_1|\ge3$ case is deferred to `crt-period-lifting`.

## Lemma-candidates for the shared cache

1. `two-entry-lemma` (Step 2, unconditional, $|P_1|=2$-specific).
2. `P1-minimal-transversal-lemma` (Step 3, unconditional; the implication "$p\mid a_n\,\forall n\Rightarrow$ LOCK" is a self-contained sub-result worth certifying on its own — it is the contrapositive engine behind several NON-LOCK arguments).

## Single-gap-trap disclosure (per outline-reviewer)

This slug shares the cofactor-bound wall with `crt-period-lifting`. If the bound is unprovable by any of the three routes (direct $2$-density here; CRT fiber-lifting there; the integer-monovariant escape in `integer-monovariant-transfer`), all three die together. I did NOT find a non-circular proof; the partial is honest.
