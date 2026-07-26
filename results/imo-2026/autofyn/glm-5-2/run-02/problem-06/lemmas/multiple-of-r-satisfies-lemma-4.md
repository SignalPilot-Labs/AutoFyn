# Lemma (multiple-of-R satisfies Lemma 4)

**Statement.** Let $a_1,a_2,\ldots$ be the greedy sequence of IMO 2026 P6, and let $R:=\operatorname{rad}(a_1)=\prod_{p\mid a_1}p$. If $a_j$ is a multiple of $R$, then for every $i<j$ the pair $(a_i,a_j)$ shares a prime $q\le R$; in particular the pair $(a_i,a_j)$ satisfies Lemma 4 (pairwise small-prime intersection) for the bound $R$.

**Proof.** Suppose $a_j$ is a multiple of $R$. Since $R=\prod_{p\mid a_1}p$, every prime divisor $p$ of $a_1$ divides $R$, hence divides $a_j$. By Lemma 1 (the cheap structural anchor: every term of the greedy sequence is divisible by some prime divisor of $a_1$, because the greedy rule at stage $j-1$ forces $\gcd(a_j,a_1)>1$), the term $a_i$ is divisible by some prime $q\in P(a_1)$. Now $q\mid a_1$, so $q\mid R$, and $R\mid a_j$ by hypothesis, hence $q\mid a_j$. Thus $q$ is a prime dividing both $a_i$ and $a_j$. Finally $q\in P(a_1)\subseteq Q_R:=\{p\text{ prime}:p\le R\}$, since every prime divisor of $a_1$ is at most $R=\prod_{p\mid a_1}p\ge q$. Hence $q\le R$ is a small prime shared by $(a_i,a_j)$. $\square$

**Corollary (counterexample constraint).** Any counterexample to Lemma 4 — i.e. any pair $(a_i,a_j)$, $i<j$, sharing no prime $\le R$ — must have $a_j$ not divisible by $R$ (i.e. $a_j\bmod R\ne 0$).

**Where proved.** `results/imo-2026-06/lemmas/multiple-of-r-satisfies-lemma-4.md` (round 2). Uses Lemma 1, proved in `results/imo-2026-06/approaches/essential-monovariant.md` §1.

**Note.** This lemma is subsumed by the full Lemma 4' (every pair of terms shares a prime $\le a_1$), proved in `approaches/essential-monovariant.md` §5–6 via the game-of-numbers equivalence. It is retained as a clean, self-contained one-paragraph partial result.
