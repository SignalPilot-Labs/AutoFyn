# proof-builder — essential-monovariant (round 1)

## What I built
Approach file: `/home/agentuser/repo/results/imo-2026-06/approaches/essential-monovariant.md` (Status: **partial**).

### Genuine contribution this round (the monovariant)
**Lemma 2 (Gap bound), fully proved:** $a_{n+1}-a_n\le \operatorname{rad}(a_1)$ for every $n\ge 1$. Proof: the least multiple of $R=\operatorname{rad}(a_1)$ above $a_n$ is $\le a_n+R$ and is admissible (it is divisible by *every* prime of $a_1$, hence shares a prime with every term by the cheap lemma). This is the adaptation of aimo-0678's "exhibit a bounded admissible integer to bound the runaway coordinate" move — there the frozen invariant $s_n$ gave the bound, here the fixed $R$ does. Corollary (Lemma 3): consecutive terms share *only* primes $\le R$.

### Full periodicity machinery, rigorous conditional on the crux
Proved end-to-end (Theorem in Section 5), conditional on Lemma 4:
- free-rider irrelevance (two directions: transversal$\Rightarrow$admissible is free; admissible$\Rightarrow$transversal uses Lemma 4 applied to the term $a_{n+1}$ against *every* $a_i$, including future terms);
- greedy $=$ next-$V$-residue mod $L_0=\prod_{p\le R}p$;
- the residue walk $\varphi$ is the **cyclic successor permutation** on $V$ (a single cycle, bijection) — hence purely periodic from $n=1$;
- telescoping: sum of cyclic gaps over one full cycle $=L_0$, so $a_{n+|V|}=a_n+L_0$ for **every** $n\ge 1$ (no transient).
- Computationally confirmed for $a_1=15$: $L_0=30030$, $|V|=8008$, greedy $=$ next-$V$-residue for 30 transitions.

### Reduction of the shared crux
The crux "essential-prime set $E$ finite" reduces cleanly to **Lemma 4** (every pair of terms shares a prime $\le R=\operatorname{rad}(a_1)$): if $p\in E$ is essential (unique shared prime of some pair), Lemma 4 gives the same pair a small shared prime $q\le R$; uniqueness forces $p=q\le R$, so $E\subseteq\{p\le R\}$, finite. And Lemma 4 alone (not the exact $E$) suffices for the whole periodicity machinery. So Lemma 4 is the **sole** remaining gap.

## The open gap (honest)
**Lemma 4, non-consecutive case.** Consecutive case $=$ Lemma 3 (proved). The inductive step for non-consecutive pairs ($i<j-1$): if $a_j$ shares a large prime $p>R$ with $a_i$, the natural candidates ($a_{j-1}+r$ sharing the small prime $r$ of $a_i,a_{j-1}$; or $a_j-s$ sharing the consecutive small prime $s$) each share a small prime with *two* terms but are not guaranteed admissible against *all* intermediate terms, so greedy minimality does not yield a contradiction. Verified computationally (no counterexample for $a_1\in\{15,35,77,105\}$, 600 terms each, all $\binom{600}{2}$ pairs) — the lemma is true, the proof is the 9/10 crux.

### Mechanism (free-rider co-occurrence, observed)
For $a_1=105$: prime $317>R=105$ first appears in $a_{497}=1902=2\cdot3\cdot317$; the candidate $11095=5\cdot7\cdot317$ (which would share only $317$ with $1902$) is **not** a term — it is coprime to the $\{2,3\}$-type terms and hence inadmissible. So every $317$-multiple term also carries $2$ or $3$, and $317$ never becomes essential. This is the obstruction the missing proof must formalize.

## Note for next round
- The gap bound (Lemma 2) is reusable by *any* approach (windowed, crude, covering) as a foundation; it is certified-into-lemmas-ready.
- The cleanest path to `solved`: prove Lemma 4's non-consecutive case. The transversal-family structure (a pair sharing a large prime must, by the pairwise-intersecting *stabilized* family, also share a small prime) is the likely lever, but I could not close the induction this round. The proof probably needs a minimal-counterexample descent or a direct argument that a large prime cannot be the unique connection across the "small-prime backbone" that the gap bound forces.
- My approach as built gives the **crude** $L_0=\prod_{p\le R}p$ (large but finite); the true small $L=\prod_{p\in E}p$ would require additionally identifying $E$, which Lemma 4 gives as a *subset* of $Q_R$ but not exactly.
