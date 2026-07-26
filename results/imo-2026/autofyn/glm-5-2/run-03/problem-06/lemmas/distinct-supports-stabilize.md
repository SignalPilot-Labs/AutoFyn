# Lemma — distinct-supports-stabilize (conditional on Gap A/C)

**Conditional lemma** (reviewer-certified, round 2). This reduces Gap A/C to $\mathcal B_\infty$ being $L$-periodic: once the set of primes appearing in any minimal transversal of $\mathcal F_n$ is bounded, the minimal-transversal family stabilizes, hence $\mathcal B_\infty$ is periodic.

**Setting.** Greedy sequence. $\mathcal F_n=\{S(a_1),\dots,S(a_n)\}$, distinct-support set-system $\mathcal D_n:=\{S(a_i):1\le i\le n\}$. $\mathcal F_\infty=\{S(a_i):i\ge1\}$.

**Hypothesis (Gap A/C).** *There is a finite bound $B$ with every prime appearing in any $\operatorname{MT}(\mathcal F_n)$ (and every prime of $P_1=S(a_1)$) lying in $\{p\le B\}$.* (Equivalently, only finitely many primes ever enter a minimal transversal of $\mathcal F_\infty$.)

**Lemma (distinct-supports-stabilize).** *Assuming the hypothesis, there exists $N_0$ such that for all $n\ge N_0$, $\operatorname{MT}(\mathcal F_n)=\operatorname{MT}(\mathcal F_\infty)$.*

*Proof.* Consider $\mathcal D_n\subseteq 2^{\{p\le B\}}$ (every prime in every $S(a_i)$ lies in $\{p\le B\}$ under the hypothesis — term primes are a subset of MT-primes $\cup$ $P_1$, both bounded by hypothesis). The finite power set $2^{\{p\le B\}}$ has $\le 2^{\pi(B)}$ elements. The sequence $(\mathcal D_n)$ is **increasing** ($\mathcal D_n\subseteq\mathcal D_{n+1}$, since adding a term only adds its support). An increasing sequence in a finite poset stabilizes: there is $N_0$ with $\mathcal D_n=\mathcal D_{N_0}=:\mathcal D_\infty$ for all $n\ge N_0$. By `mt-depends-on-set-system`, $\operatorname{MT}(\mathcal F_n)=\operatorname{MT}(\mathcal D_n)$; for $n\ge N_0$ this equals $\operatorname{MT}(\mathcal D_\infty)=\operatorname{MT}(\mathcal F_\infty)$. ∎ *(Reviewer-verified, round 2.)*

**Corollary ($\mathcal B_\infty$ is $L$-periodic, conditional on Gap A/C).** *Assume the hypothesis. Let $G$ be the (finite) set of primes appearing in $\operatorname{MT}(\mathcal F_\infty)\cup P_1$ and $L:=\prod_{p\in G}p$. Then $\mathcal B_\infty=\bigcup_{T\in\operatorname{MT}(\mathcal F_\infty)}\{m:\operatorname{rad}(T)\mid m\}$, and membership $m\in\mathcal B_\infty$ depends only on $m\bmod L$. Hence $\mathcal B_\infty$ is $L$-periodic.*

*Proof.* For $n\ge N_0$, $\mathcal B_\infty=\mathcal B_{N_0}=\bigcup_{T\in\operatorname{MT}(\mathcal F_\infty)}\{m:\operatorname{rad}(T)\mid m\}$, a finite union. Divisibility by each $p\in G$ is determined by $m\bmod L$ (since $L=\prod_{p\in G}p$). ∎

**Import.** The rigorous replacement for the false "MT is non-increasing under set addition" claim. Importable by any approach that closes Gap A/C and needs to deduce $\mathcal B_\infty$ is $L$-periodic (then the certified `cyclic-successor-bijection` + `greedy-equals-cyclic-successor` finish the proof).
