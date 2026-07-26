# proof-builder: transversal-saturation (round 2)

## What I proved (rigorous, new this round)

1. **Lemma A (smallest-multiple structure).** If $q>M_1\ge d_{i-1}$ and $q\mid a_i$ (the private-witness setup), then $a_i$ is the smallest positive multiple of $q$ strictly greater than $a_{i-1}$. Clean proof from the gap bound + uniqueness of multiples of $q$ in intervals of length $<q$.

2. **Corollary A2 (predecessor shares a small prime).** The term $a_{i-1}$ shares a prime $t\ne q$ with $a_i$, and every such shared prime satisfies $t\le d_{i-1}\le M_1$. (From Lemma A: $q\nmid a_{i-1}$; then $t\mid(a_i-a_{i-1})\le M_1$.) This handles the $j=i-1$ case of admissibility transfer completely — $a_{i-1}$ is never an obstruction.

3. **Lemma B ($T\setminus\{q\}$ transverses $\mathcal F_{i-1}$).** With $a_i$ chosen as the smallest-index private witness of $q$ in $T\in\operatorname{MT}(\mathcal F_\infty)$, the reduced set $T\setminus\{q\}$ hits every $a_j$ ($j<i$). This is the reviewer's "half-sound" half, now rigorously proved.

4. **Lemma C (size-bound NO-GO for the multiple-of-$A$ strip).** With $A=$ small radical of $a_i$ minus $q$ (so $A\mid a_i$): the smallest multiple of $A$ above $a_{i-1}$ is $a_i$ itself when $d_{i-1}\le A$, and every multiple of $A$ in $(a_{i-1},a_i)$ is inadmissible (by greedy minimality) when $d_{i-1}>A$. Either way, no admissible multiple of $A$ lies in $(a_{i-1},a_i)$. This is a structural impossibility result, not a missing estimate.

5. **Step 7 factual corrections.** Retracted the false "$a_1=385$ aperiodic through 12000 terms" and "$q\le M_1$ refuted" narrative. Verified: $a_1=385$ is periodic from $n=1$ ($T=5088$, $L=43890=2\cdot3\cdot5\cdot7\cdot11\cdot19$); governing primes all $\le M_1=385$. Properly distinguished governing (factors of $L$) from transient (finite-stage MT primes that drop out) primes. Confirmed $q\le M_1$ for the governing set across 80+ tested starting values.

## What remains open (honest)

**Gap A (finiteness of governing primes / $L$-periodicity of $\mathcal B_\infty$) is OPEN.** The `aimo-0030` minimal-criminal strip, in the two formulations the outliner proposed, does NOT close it:

- **Size bound fails.** Lemma C gives a structural no-go for the "smallest-multiple-of-$A$" version: either $x_0=a_i$ (no shrinking) or the candidates in the gap are inadmissible by the greedy rule. The "$p^kA$" version (prime-power multiplier) blows up exponentially: $x\le p\cdot a_{i-1}$, which exceeds $a_i=a_{i-1}+d_{i-1}\le a_{i-1}+M_1$ for $a_{i-1}>M_1/(p-1)$ — i.e. for all sufficiently large witnesses. Computational confirmation: stripping $q=19$ from witnesses of $a_1=385$ yields $x\in[686,4802]\gg a_i\in[399,1064]$.

- **Admissibility transfer is genuinely obstructed, not merely unproven.** For $a_1=385$ with governing prime $q=19$ (small analogue of the hypothetical $q>M_1$), there are 51 pairs $(a_j,a_i)$ with $S(a_j)\cap S(a_i)=\{q\}$ in the first 700 terms. Computing MT at $n=120$: the smallest-index private witness of $19$ in $T=\{3,7,19\}$ is $a_7=418=2\cdot11\cdot19$, and it is OBSTRUCTED by $a_5=399=3\cdot7\cdot19$ (shares only $19$). So even with the smallest-index-witness choice (Lemma B's precondition), the obstruction arises for some minimal transversals. One may hope to choose an obstruction-free $T$ (and $T=\{2,11,19\}$ is obstruction-free), but no proof forces such a $T$ to exist in the $q>M_1$ regime, and the star counterexample shows the abstract pairwise-intersecting structure cannot force it.

**Fallbacks A and B are sketched but open.** Fallback A (least-multiplier minimality) has no rigorous mechanism — "minimality of $m=a_i/q$" is not a greedy minimality. Fallback B (witness recurrence + density) has a circular covering-capacity bound (bounding primes in intermediate supports IS Gap A); it is the subject of the parallel `witness-density-recurrence` approach, whose crux is also open.

## Honest status

**PARTIAL.** The whole theorem remains reduced to Gap A. The endgame (cyclic-successor bijection $\Rightarrow$ $a_{n+T}=a_n+L$ from $n=1$), pure-from-start (Gap B), and the LOCK sub-case are all certified and unconditional. Round 2 added two clean positive lemmas (A, B) plus the $a_{i-1}$ admissibility case, but also produced a rigorous NO-GO (Lemma C) for the natural strip construction and computational evidence that admissibility transfer is genuinely obstructed. **The strip as formulated is a dead end.** The field's shared wall (Gap A) is now better understood: it is a real structural obstruction in the taming step, not a missing estimate. Future rounds need a different mechanism for "the greedy coupling forces transversal primes into the bounded regime" — neither the one-shot strip (dead, Lemma C + obstruction data) nor the MT-frontier monovariant (broken, reviewer round 2) nor the density covering-capacity (circular) has produced it.

## Promotable lemmas (for reviewer certification)

- **Lemma A** (smallest-multiple structure of a witness divisible by a large prime $q>M_1$). Clean, uses gap bound.
- **Corollary A2** (predecessor $a_{i-1}$ shares a small prime $\le M_1$ with $a_i$). Clean, uses Lemma A + pairwise intersection.
- **Lemma B** ($T\setminus\{q\}$ transverses $\mathcal F_{i-1}$ for smallest-index private witness). Clean, standard minimal-transversal private-element logic.
- **Lemma C** (size-bound no-go for the multiple-of-$A$ strip). A negative lemma — records that the natural strip construction cannot work, to save future rounds from re-trying it.
