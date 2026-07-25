## Theorem 12 (Generalized Subset-Tie Lemma, any index)

Certified round 8. Proved in `approaches/universal-halving-adversary.md`
(round 8, "Theorem 12 (Generalized Subset-Tie Lemma, any index)"). A
direct generalization of the certified Theorem 9 (Singleton-Interleaving
Lemma, `lemmas/singleton-interleaving-and-k-anchor-merge.md`) and Theorem
11 (Subset-Tie Lemma, prior round) from "the piece split is always $p_1$"
to "the piece split may be any index $i$."

**Statement.** Let $p_1,\ldots,p_{n+1}>0$ sum to $1$ ($k=n+1$ pieces, full
budget). Fix any index $i\in\{1,\ldots,n+1\}$ and any subset
$J\subseteq\{1,\ldots,n+1\}\setminus\{i\}$ with $T:=\sum_{m\in J}p_m\le
p_i$; let $r:=p_i-T\ge0$. XY's move: split $p_i$ into fragments
$\{p_m:m\in J\}\cup\{r\}$ (dropping $r$ if $r=0$), leave every $p_m$
($m\in J$) untouched, bisect every other piece $p_\ell$
($\ell\notin J\cup\{i\}$). This uses exactly $n$ (or $n-1$ if $r=0$) cuts
— within budget for every $i,J$. Then
$$\mathrm{OddSum}(M)=\frac{1+r}2=\frac{1+p_i-T}2.$$

**Proof (reviewer's independent verification of the construction).** The
merged multiset $M$ decomposes into an even-block part $B$ — pairs
$\{p_m,p_m\}$ for $m\in J$ (the untouched original piece plus the tied
split-fragment of equal value) and pairs $\{p_\ell/2,p_\ell/2\}$ for
$\ell\notin J\cup\{i\}$ (the two bisection halves) — plus a singleton
$\{r\}$ (or nothing if $r=0$). $\mathrm{sum}(B)=2T+((1-p_i)-T)=1-p_i+T=1-r$.
By the certified Singleton-Interleaving Lemma (Theorem 9),
$\mathrm{OddSum}(M)=\tfrac12\mathrm{sum}(B)+\mathrm{OddSum}(\{r\})=
\tfrac12(1-r)+r=\tfrac{1+r}2$ (or, if $r=0$, by the Doubling Lemma applied
to $B$ alone, giving the same formula in the limit). Coincidence/tie cases
among the block values are handled identically to Theorem 9/11's own
proof (merging blocks preserves even length or is absorbed into the
odd-length-block computation already used there) — no new case beyond
what Theorem 9/11 establish.

**Reviewer verification (round 8, independent, exact `Fraction`
arithmetic, from-scratch script; reviewer's first construction attempt
had a bug — omitted the untouched copy of $p_m$ for $m\in J$, i.e. built
only one copy instead of the required tied pair — corrected and re-run).**
20,000 random trials ($n=2,\ldots,10$, random index $i$, random subset $J$
with $T\le p_i$ built greedily from a random ordering): zero discrepancies
between the direct sort-and-sum computation of $M$ and the closed form
$(1+r)/2$, exact rational arithmetic throughout.

**Cut-count check.** Splitting $p_i$ into $|J|+1$ fragments costs $|J|$
cuts; bisecting the remaining $n-|J|$ pieces costs $n-|J|$ cuts. Total
$n$, matching the full budget for every choice of $i,J$ — confirmed by
direct count, no gap.

**Relation to prior results.** Theorem 11 (prior round, certified as part
of `universal-halving-adversary`'s development) is exactly the special
case $i=1$; this generalizes it to any index, useful precisely when some
non-top piece $p_i$ admits a subset $J$ of the other pieces whose sum is
closer to $p_i$ than any subset of $p_1$'s complement gets to $p_1$.

**Scope note.** This is an incremental additive tool for the
"large-gaps-everywhere" balanced-region residual of the upper-bound
direction. It does **not** by itself close the residual: this round's
own numerics (see `approaches/universal-halving-adversary.md`, "Round 8:
honest re-verification") found the survivor rate of
best-of-$\{k=1,k=2,\text{this theorem}\}$ does not shrink to zero as $n$
grows, so a full Existence Theorem via finite additive constructions
remains open and is not claimed here.
