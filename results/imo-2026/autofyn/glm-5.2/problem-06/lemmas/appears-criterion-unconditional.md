# Lemma: appears-criterion-unconditional (Piece A)

**Setting.** The greedy gcd sequence $a_1,a_2,\ldots$ ($a_{n+1}$ = smallest integer $>a_n$ with $\gcd(a_{n+1},a_i)>1$ for every $i\le n$). Define the index-ordered radical partial order
$$a_m\prec a_n \iff m<n\ \text{and}\ P(a_m)\subseteq P(a_n)\quad(\text{equiv.}\ \mathrm{rad}(a_m)\mid\mathrm{rad}(a_n)).$$
A term $a_n$ is **$\prec$-minimal** if no $m<n$ has $a_m\prec a_n$.

**Statement (unconditional — no finiteness hypothesis).** For every integer $x\ge a_1$, the following are equivalent:
(i) $x$ appears in the sequence ($x=a_n$ for some $n$);
(ii) $\gcd(x,a_i)>1$ for every term $a_i<x$;
(iii) $\gcd(x,a_i)>1$ for every $\prec$-minimal term $a_i<x$.

**Proof.** The sequence is strictly increasing, hence $i<n\iff a_i<a_n$, and $a_{n+1}\ge a_n+1$ so $a_n\to\infty$.

**(i)$\Rightarrow$(ii).** If $x=a_n$, then $a_n$ was chosen admissible against $a_1,\ldots,a_{n-1}$, so $\gcd(a_n,a_i)>1$ for $i<n$; and $a_i<x=a_n\iff i<n$.

**(ii)$\Rightarrow$(i).** Let $n$ be the largest index with $a_n\le x$ (exists: $a_n\to\infty$, $x\ge a_1$). If $a_n=x$, done. Else $a_n<x<a_{n+1}$. For every $i\le n$, $a_i\le a_n<x$, so by (ii) $\gcd(x,a_i)>1$; thus $x$ is admissible against $a_1,\ldots,a_n$ and $x>a_n$, contradicting the greedy choice of $a_{n+1}$ as the smallest admissible integer $>a_n$. So $a_n=x$.

**(ii)$\iff$(iii).** (iii)$\Rightarrow$(ii) is immediate (every $\prec$-minimal term is a term). For (ii)$\Rightarrow$(iii): take any non-$\prec$-minimal $a_j<x$; by definition some $m<j$ has $a_m\prec a_j$ ($P(a_m)\subseteq P(a_j)$). Iterating (indices strictly decrease, so it terminates) yields a chain to a $\prec$-minimal $a_{j_t}<a_j<x$ with $P(a_{j_t})\subseteq P(a_j)$. A prime $s\mid\gcd(x,a_{j_t})$ lies in $P(x)\cap P(a_{j_t})\subseteq P(x)\cap P(a_j)$, so $\gcd(x,a_j)\ge s>1$. ∎

**Remark.** This is the unconditional elementary form of the membership criterion. It must NOT be confused with the GAP-conditional lemmas `universal-membership-no-transient` / `transversal-residue-characterization`, which define $L,V$ from $\mathcal M$ (requiring $\mathcal M$ finite) and would make any finiteness proof circular if invoked inside it.

*Source.* Approach `large-prime-descent` (§2), round 130. Reviewer-certified (verified 0 violations across 8 seeds × 200 random $x$).
