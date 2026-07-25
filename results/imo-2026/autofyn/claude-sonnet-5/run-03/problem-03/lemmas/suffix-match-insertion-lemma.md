# Certified (round 4): Suffix-Match Insertion Lemma (Theorem 6)

Certified from `approaches/universal-halving-adversary.md` (round 4).
Proof-reviewer independently re-derived the formula and verified it against
direct sorted-sum computation over 8,700+ random trials (generic case, all
`n=1..5`), zero mismatches beyond floating-point noise.

**Statement.** Fix a sorted tuple $p_1\ge p_2\ge\cdots\ge p_{n+1}>0$ summing
to $1$, with tail $R=(p_2,\dots,p_{n+1})$ having pairwise-distinct values
sorted ascending $w_1<\cdots<w_n$. Fix $t\in\{0,\dots,n\}$ with
$\sum_{i\le t}w_i\le p_1$. Write $R_t=(w_1,\dots,w_t)$,
$U=(w_{t+1},\dots,w_n)$ sorted descending $u_1>\cdots>u_{n-t}$, and
$\ell:=p_1-\sum_{i\le t}w_i\ge0$. XY's move: replace $p_1$ by $R_t\cup\{\ell\}$
(a valid split using $\le t$ cuts). The resulting multiset $M=R\cup
R_t\cup\{\ell\}$ has, in the generic case where $\ell$ ties no value of $R$:
$$\mathrm{OddSum}(M)=\sum_{\substack{1\le j\le A\\j\text{ odd}}}u_j
+[A\text{ even}]\cdot\ell+\sum_{\substack{A<j\le n-t\\j\text{ even}}}u_j
+\sum_{i=1}^tw_i,\qquad A:=\#\{j:u_j>\ell\}.$$
Three further exhaustive sub-cases ($\ell=0$; $\ell$ ties a value of $R_t$;
$\ell$ ties a value of $U$) are given explicit closed forms in the source
file, all proved by the same block-counting technique as the Doubling Lemma
and General Insertion Lemma.

**Proof idea (verified).** $R_t$'s values double up with $R$'s matching
copies into even-length blocks (parity-invariant under any starting rank, as
in the Doubling Lemma), contributing $\sum_{i\le t}w_i$ regardless of
position; $U\cup\{\ell\}$ occupies the disjoint top rank-range and is
computed directly by its own order statistics.

**Reduces correctly to known identities.** $t=0$: no-op (identity).
$t=n$ ($U=\varnothing$): reduces exactly to the General Insertion Lemma
($\mathrm{OddSum}=\mathrm{sum}(R)+\ell=p_1$).

**Important caveat proved by the same round's builder and independently
reproduced by the reviewer (order-of-magnitude match, ~45–90% failure
rates across independent samplers):** optimizing over $t$ alone (with or
without a greedy leftover-bisection cleanup) does **not** close the
"balanced region" ($p_1<1/2$, $p_{n+1}>1/(2^{n+1}-1)$) of the general upper
bound — this lemma is a genuine, exact, reusable identity, but insufficient
by itself as a closing construction for that region. Do not re-attempt
"optimize Suffix-Match over $t$ alone" as a route to closing the balanced
region; it is a documented negative result, not merely unexplored.

**Reusable by:** any approach needing an exact-value formula for "partially
duplicate a sub-multiset, insert one leftover element" constructions.
