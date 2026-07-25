## Lemmas: Singleton-Interleaving Lemma and General $k$-Anchor-Merge Lemma

**Theorem 9 (Singleton-Interleaving Lemma).** Let $M$ be a finite multiset
of positive reals that decomposes as $M=B\sqcup L$, where:
- $B$ (the "base") is a disjoint union of finitely many **even-length
  blocks**: groups of mutually equal elements, pairwise distinct in value
  across groups, each group occurring with an even multiplicity;
- $L=\{\ell_1,\dots,\ell_k\}$ ($k\ge0$) is a finite multiset of positive
  reals, pairwise distinct, and each distinct from every value occurring in
  $B$ (genericity hypothesis; relaxed by continuity to all tied
  configurations, since the combinatorial rank-parity rule assigning
  $\mathrm{OddSum}$ is a continuous function of the underlying real
  parameters).

Then, under the greedy alternating-claim game (first mover receives the
odd ranks of $M$ sorted descending),
$$\mathrm{OddSum}(M)=\tfrac12\,\mathrm{sum}(B)+\mathrm{OddSum}(L),$$
where $\mathrm{OddSum}(L)$ is $L$'s own value computed by sorting $L$
descending and summing its own odd-ranked entries (i.e. treating $L$ as a
fully independent standalone instance of the same game).

**Proof.** Each block of $B$ occupies a genuinely consecutive, even-length
run of ranks in $M$'s global sort (its elements are literally equal and, by
genericity, distinct from every other value present), so — by the standard
fact that an interval of consecutive integer ranks of even length contains
exactly half odd and half even ranks regardless of where it starts (the
Claim underlying the certified Doubling Lemma,
`lemmas/doubling-lemma-and-generalized-duplicate-the-rest.md`) — each block
contributes exactly half its total value to $\mathrm{OddSum}(M)$,
regardless of its position relative to the rest of $M$; summing over blocks
gives $\tfrac12\,\mathrm{sum}(B)$.

For $L$'s contribution: sort $L$ descending as
$\ell_{(1)}>\cdots>\ell_{(k)}$. For each $t$, let $e_t$ be the number of
$B$-elements strictly between $\ell_{(t-1)}$ and $\ell_{(t)}$
($\ell_{(0)}:=+\infty$). Since $L$'s values are all distinct from $B$'s, no
block of $B$ straddles any $\ell_{(t)}$, so each $e_t$ is a sum of complete
(even) block lengths, hence itself even. Thus
$\mathrm{rank}_M(\ell_{(t)})=t+\sum_{s\le t}e_s\equiv t\pmod2$: $\ell_{(t)}$
sits at an odd global rank in $M$ iff $t$ is odd — exactly its parity as
the $t$-th largest element of $L$ alone. Hence the first mover claims from
$L$ exactly $\{\ell_{(t)}:t\text{ odd}\}$, whose sum is $\mathrm{OddSum}(L)$
by definition. $\blacksquare$

**Theorem 10 (General $k$-Anchor-Merge Lemma).** Let
$p_1\ge\cdots\ge p_{n+1}>0$ sum to $1$. Fix $k\ge1$ pairwise-disjoint index
pairs $(i_1,j_1),\dots,(i_k,j_k)$, $i_m<j_m$, all $2k$ indices distinct.
Let $\ell_m:=p_{i_m}-p_{j_m}\ge0$. XY's move: split each $p_{i_m}$ into
$(\ell_m,p_{j_m})$ (one cut), leave $p_{j_m}$ untouched, and bisect every
other piece $p_r$ ($r\notin\{i_1,j_1,\dots,i_k,j_k\}$) into $(p_r/2,p_r/2)$
(one cut each) — total $n+1-k\le n$ cuts. Then, generically,
$$\mathrm{OddSum}(M)=\tfrac12\Bigl(1-\sum_{m=1}^k\ell_m\Bigr)+\mathrm{OddSum}(\{\ell_1,\dots,\ell_k\}).$$

**Proof.** In $M$: each $p_{j_m}$ occurs with multiplicity $2$ (untouched
copy plus its tied fragment), each bisected $p_r$ occurs with multiplicity
$2$ (as $p_r/2,p_r/2$) — these form $B$ (all even blocks) — and each
$\ell_m$ is a singleton, generically distinct from everything else,
forming $L=\{\ell_1,\dots,\ell_k\}$. Apply Theorem 9. Computing
$\mathrm{sum}(B)$: pieces not chosen as some $i_m$ sum to
$1-\sum_m p_{i_m}$; contribution of each such piece to $\mathrm{sum}(B)$ is
either $2p_{j_m}$ (untouched-plus-tied-fragment) or $p_r$ (two halves).
$$\mathrm{sum}(B)=\sum_m2p_{j_m}+\Bigl(1-\sum_mp_{i_m}-\sum_mp_{j_m}\Bigr)
=1+\sum_mp_{j_m}-\sum_mp_{i_m}=1-\sum_m\ell_m.$$
Substituting into Theorem 9's identity gives the claimed formula.
$\blacksquare$

**Special cases.** $k=1$: recovers the certified Anchor-Merge Lemma
(`lemmas/anchor-merge-lemma.md`) exactly, $\mathrm{OddSum}=\tfrac12(1+\ell_1)$.
$k=2$: $\mathrm{OddSum}(\{\ell_1,\ell_2\})=\max(\ell_1,\ell_2)$, giving
$\mathrm{OddSum}(M)=\tfrac12(1+|\ell_1-\ell_2|)$.

**Independent verification (proof-reviewer, round 6).** Both theorems
re-derived from scratch and checked by exact-`Fraction`-arithmetic
simulation (construct $M$ literally from the stated construction, including
the untouched copy of $p_{j_m}$ at multiplicity 2, and compute $\mathrm{OddSum}$
by direct sort-and-sum): $3000$ random trials each, **zero discrepancy**
(exact rational equality) against the closed-form formulas, for both
theorems, across random $k$, random disjoint pairings, random $p$. (Note:
the reviewer's first draft of the Theorem 10 test omitted the untouched
copy of $p_{j_m}$ — the same class of construction-transcription bug flagged
in round 5's memory note — and produced large spurious discrepancies until
fixed; corrected script gives exact zero diff.) Also independently verified
the $k=3$ non-monotonicity negative finding: at $n=6$, sampled balanced
partitions with every consecutive gap exceeding $\gamma(6)=1/(2^7-1)$, the
best $k=2$ merge (found by exhaustive search over all disjoint pairings)
achieves $\le c(6)$ in several instances while the best $k=3$ merge on the
identical instance is strictly worse (exceeds $c(6)$) — reproduced exactly
via independent brute-force enumeration.

**Source.** Proved in `approaches/universal-halving-adversary.md` (round 6,
Theorems 9 and 10).

**Reuse.** General-purpose closed-form tool for any XY construction that
simultaneously ties several fragments to other pieces while bisecting the
rest; strictly subsumes the single-Anchor-Merge Lemma. The proved
non-monotonicity in $k$ is itself reusable negative information: future
attempts at the residual "large-gaps-everywhere" balanced region should
take a minimum over several small $k$ values (via per-instance search or a
future closed-form optimal-pairing rule), not assume larger $k$ is always
at least as good.
