# Lemma B — $T\setminus\{q\}$ transverses $\mathcal F_{i-1}$ (smallest-index private witness)

**Setting.** Greedy sequence. $\mathcal F_n=\{S(a_1),\dots,S(a_n)\}$. Let $T\in\operatorname{MT}(\mathcal F_\infty)$ be a minimal transversal of the limit family with $q\in T$. By the private-element characterization of minimal transversals, $q$ is private to some term: there is $a_i$ with $S(a_i)\cap T=\{q\}$. Choose $a_i$ to be the **smallest-index** private witness of $q$ in $T$.

**Lemma B.** *$T\setminus\{q\}$ is a transversal of $\mathcal F_{i-1}=\{S(a_1),\dots,S(a_{i-1})\}$: every $a_j$ with $j<i$ is hit by some prime of $T\setminus\{q\}$.*

*Proof.* $T$ is a transversal of $\mathcal F_\infty\supseteq\mathcal F_{i-1}$, so $T\cap S(a_j)\ne\varnothing$ for every $j\le i-1$. Suppose for some $j<i$ that $T\setminus\{q\}\cap S(a_j)=\varnothing$; then $T\cap S(a_j)\subseteq\{q\}$, and since $T$ hits $S(a_j)$, $T\cap S(a_j)=\{q\}$. This makes $q$ private to $a_j$ as well (i.e. $S(a_j)\cap T=\{q\}$) — but $j<i$, contradicting the *smallest-index* choice of $a_i$ as the private witness of $q$. Hence $T\setminus\{q\}$ hits every $a_j$, $j<i$. ∎ *(Reviewer-verified, round 2.)*

**Import.** Useful for any strip / density argument relying on the private-witness structure: the reduced set $T\setminus\{q\}$ provably covers all earlier terms. (The gap, recorded in `lemma-C-strip-no-go`, is that the $T\setminus\{q\}$-prime hitting $a_j$ need not lie in $S(a_i)$, hence need not divide any candidate $x$ built from $a_i$'s small primes.)
