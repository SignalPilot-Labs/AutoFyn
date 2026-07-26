# Lemma C — NO-GO: the "smallest-multiple-of-small-radical" strip cannot close Gap A

**Dead-end record.** This is a *negative* lemma (reviewer-certified, round 2): it records that the natural `aimo-0030`-style minimal-criminal prime-factor strip, in its "smallest-multiple-of-$A$" and "$p^kA$" formulations, is structurally incapable of producing an admissible $x<a_i$ that contradicts greedy minimality. Future rounds need not re-try these formulations.

**Setting.** Greedy sequence, $M_1=\operatorname{rad}(a_1)$. Minimal-criminal hypothesis: $q>M_1$ is a governing prime entering $T\in\operatorname{MT}(\mathcal F_\infty)$, private to $a_i$ (smallest-index private witness). By `linchpin-and-gap-bound`, $d_{i-1}=a_i-a_{i-1}\le M_1<q$. Define the **small radical of $a_i$ minus $q$**:
$$A:=\prod_{r\in S(a_i),\,r\le M_1,\,r\ne q}r\qquad(\text{so }A\mid a_i).$$
The strip plan: build $x$ from $a_i$'s small primes, land it in $(a_{i-1},a_i)$, prove it admissible against $\mathcal F_{i-1}$, contradicting greedy minimality of $a_i$.

---

**Lemma C (size-bound no-go).** *Let $x_0:=$ the smallest multiple of $A$ strictly greater than $a_{i-1}$. Then:*
- *(i) If $d_{i-1}\le A$, then $x_0=a_i$ (no shrinking — the next multiple of $A$ above $a_{i-1}$ is $a_i$ itself).*
- *(ii) If $d_{i-1}>A$, then every multiple of $A$ in $(a_{i-1},a_i)$ is inadmissible against $\mathcal F_{i-1}$ (by greedy minimality of $a_i$).*
- *In either case, no admissible multiple of $A$ lies in $(a_{i-1},a_i)$.*

*Proof.* Since $A\mid a_i$ and $a_i=a_{i-1}+d_{i-1}$, we have $a_{i-1}\equiv -d_{i-1}\pmod A$.
- If $d_{i-1}<A$ (and $d_{i-1}>0$): $a_{i-1}\bmod A=A-d_{i-1}\in[1,A-1]$, so the smallest multiple of $A$ strictly above $a_{i-1}$ is $a_{i-1}+d_{i-1}=a_i$.
- If $d_{i-1}=A$: $a_{i-1}\equiv0\pmod A$, so the next multiple is $a_{i-1}+A=a_i$.
- If $d_{i-1}>A$: the interval $(a_{i-1},a_i)$ has length $d_{i-1}>A$ and so contains at least one multiple of $A$; but $a_i$ is by definition the *smallest admissible* integer exceeding $a_{i-1}$, so every integer in $(a_{i-1},a_i)$ — hence every multiple of $A$ there — is inadmissible. ∎

**Reviewer computation (round 2).** For $a_1=385=5\cdot7\cdot11$ (using governing prime $q=19$ as a small analogue of the hypothetical $q>M_1$ regime), the witness $a_7=418=2\cdot11\cdot19$ has $A=2\cdot11=22$, $a_6=406$: $22\lceil407/22\rceil=22\cdot19=418=a_7$. Case (i) realized — $x_0=a_i$, no shrinking. ✓

---

**The $p^kA$ version (prime-power multiplier) blows up exponentially.** The alternative $x=p^kA$ with $p\in P_1\cap S(a_i)$ and $k$ least with $p^kA>a_{i-1}$: from $p^{k-1}A\le a_{i-1}<p^kA$ we get $x=p^kA\le p\cdot a_{i-1}$. For $x<a_i=a_{i-1}+d_{i-1}\le a_{i-1}+M_1$ this requires $p\cdot a_{i-1}<a_{i-1}+M_1$, i.e. $(p-1)a_{i-1}<M_1$, which fails for $a_{i-1}>M_1/(p-1)$ — i.e. for all sufficiently large witnesses (the sequence grows without bound, so eventually $a_{i-1}\gg M_1$).

**Reviewer computation (round 2).** For $a_1=385$, stripping $q=19$ and forming $x=p^kA$ for the smallest-index private witnesses:
- witness $a_5=399=3\cdot7\cdot19$: $A=3\cdot7=21$, $p=7\in P_1\cap S(a_5)$, smallest $k$ with $7^k\cdot21>396$ is $k=2$, giving $x=7^2\cdot21=1029\gg a_5=399$.
- witness $a_7=418=2\cdot11\cdot19$: $A=2\cdot11=22$, $p=11\in P_1\cap S(a_7)$, smallest $k$ with $11^k\cdot22>406$ is $k=2$, giving $x=11^2\cdot22=2662\gg a_7=418$.
Across all smallest-index private witnesses of $19$ in the stabilized MT, $x\in[686,4802]\gg a_i\in[399,1064]$ — the size bound fails by an order of magnitude. ✓

---

**The admissibility-transfer obstruction is REAL (not merely unproven).** The strip's second load-bearing step requires: for each $a_j$ ($j<i$), the stripped $x$ shares a prime with $a_j$. The obstruction is "$a_j$ shares ONLY $q$ with $a_i$" — then $x$ (built from $a_i$'s small primes) misses $a_j$.

**Reviewer computation (round 2).** For $a_1=385$ with $q=19$, in the first $700$ terms there are $51$ pairs $(a_j,a_i)$ with $S(a_j)\cap S(a_i)=\{19\}$. Computing $\operatorname{MT}(\mathcal F_n)$ at stabilization and the smallest-index private witnesses of $19$ in each MT containing it:
- $T=\{2,11,19\}$: private witness $a_5=399=3\cdot7\cdot19$ — **no obstruction** (every earlier $a_j$ shares a small prime with $a_5$: $385\to7$, $390\to3$, $392\to7$, $396\to3$).
- $T=\{3,7,19\}$: private witness $a_7=418=2\cdot11\cdot19$ — **OBSTRUCTED** by $a_5=399=3\cdot7\cdot19$ (shares only $19$ with $a_7$).

So even with the smallest-index-witness choice (Lemma B's precondition), the obstruction **does** arise for some minimal transversals. One may *choose* an obstruction-free $T$ (the first one above is), but **no proof exists that such a $T$ must always exist in the hypothetical $q>M_1$ regime**, and the abstract star counterexample $\{\{1,j\}:j\ge2\}$ (pairwise-intersecting family with unbounded transversal primes, no greedy coupling) shows the greedy coupling is the only thing that could force it — yet no mechanism taming the obstruction has been produced.

---

**Conclusion.** The `aimo-0030` minimal-criminal strip, in the formulations tried (multiple-of-$A$; $p^kA$), does **NOT** close Gap A: the size bound has a structural no-go (Lemma C) and the $p^kA$ version blows up exponentially; admissibility transfer is empirically obstructed even for smallest-index private witnesses in the small-prime analogue. A viable route must use a different mechanism — not the one-shot prime-factor strip.
