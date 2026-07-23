# Proof review — imo-2026-04, round 1

## semigroup-crossing-binary-descent

**Verdict:** APPROVE  
**True Status:** solved  
**Builder-recorded Status:** solved — correct; no downgrade is required.

### Scores
- **Correctness:** 10/10
- **Completeness / rigor:** 10/10
- **Progress:** 10/10

### Raw Goal Progress
- **Exact requested characterization:** established as
  \[
  \boxed{\theta=180^\circ/n\text{ for integers }n\ge2}.
  \]
- **Necessity:** complete. For nonintegral $s=180^\circ/\theta$, Shan-Yu's initial equiangular triangle has three nonintegral normalized angles. The proof exhausts all ways both children could each acquire an integral coordinate and proves that one child remains entirely nonintegral after every legal cut. This is a valid adaptive counterstrategy for every finite stage.
- **Sufficiency:** complete. For integral $s=n\ge2$, if no normalized angle is integral, the strict crossing cut gives each child a positive integral label. Once a label $k$ exists, a legal balanced split replaces it, regardless of Shan-Yu's choice, by a label strictly between $1$ and $k-1$; strong induction forces label $1$ in finitely many moves.
- **Answer verification:** complete. The family lies in the required open angle range, substitution gives integral normalized total, and all other allowed values are excluded by the counterstrategy.

### Adversarial checks
1. **Original statement and move geometry.** A nonvertex perimeter point lies in the open interior of exactly one side, so relabeling it as $P\in BC$ with opposite vertex $A$ loses no legal move. Conversely, a ray strictly inside $\angle A$ exits a convex triangle through the open side $BC$, so every chosen $0<x<a$ corresponds to a legal cut.
2. **Load-bearing transition independently re-derived.** With $\angle BAP=x\theta$, the children have
   \[
   (x,b,s-b-x)=(x,b,a+c-x)
   \]
   and
   \[
   (a-x,c,s-a+x-c)=(a-x,c,b+x).
   \]
   This reproduces formula (2).
3. **Safe-child exhaustion.** Since $b$ and $c$ are already nonintegral, failure of safety in both children yields exactly one of four cross-child pairs. Their sum/difference forces respectively $a,b,c$, or $s$ integral. The four cases are exhaustive and contradict the invariant hypotheses.
4. **Strict crossing edges.** If some coordinate $a>1$, $r=\lfloor b\rfloor+1$ gives strict inequalities because $b$ is nonintegral and $a>1$. Otherwise all coordinates are $<1$; the already-established $n\ge2$ forces $n=2$, and $b<1<a+b=2-c$. The resulting $x=r-b$ satisfies $0<x<a$; also $0<r<n$, so both complementary labels are positive.
5. **Finite descent.** For $k>1$, $j=\lfloor k/2\rfloor$ and $k-j=\lceil k/2\rceil$ both belong to $[1,k-1]$. The marked vertex angle is genuinely split between the two children, so Shan-Yu cannot avoid a smaller positive integral label. Strict integer descent proves finite termination without any hidden uniform-bound assumption.
6. **Independent computational check.** Exhaustive rational-grid tests covered 8,571,420 safe-child instances and 23,705 integral-sum crossing triples, with no counterexample; balanced descent was also checked for $2\le n<100$.
7. **Named-tool compliance.** The proof explicitly identifies reformulation/change of variables, angle chasing, invariant, casework/exhaustion, pigeonhole/extremal crossing, strong induction, and monovariant, all matching entries in `knowledge_base.md`.

### Promotable lemmas
- **Safe-child lemma:** certified and admitted as `results/imo-2026-04/lemmas/safe-child-nonintegrality.md`.
- **Integer-crossing lemma:** certified with the necessary scope $n\ge2$ and admitted as `results/imo-2026-04/lemmas/integer-crossing-three-summands.md`. (Without $n\ge2$ the standalone claim would be false at $n=1$; the builder's promoted statement and application both include $n\ge2$.)
- **Integral-label descent lemma:** certified and admitted as `results/imo-2026-04/lemmas/integral-angle-label-descent.md`.

`results/imo-2026-04/current.md` has been created with Status `solved` and the independently checked full proof.
