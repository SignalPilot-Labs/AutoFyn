# Anchor-Merge Lemma

**Source:** `approaches/universal-halving-adversary.md`, round 5, Theorem 7.

**Statement.** Let $p_1\ge p_2\ge\cdots\ge p_{n+1}>0$ sum to $1$ ($n\ge1$).
Fix any two indices $i<j$ (so $p_i\ge p_j$ in the sorted order), and let
$\ell:=p_i-p_j\ge0$. XY's move: split $p_i$ into the two fragments
$(\ell,\,p_j)$ (**one** cut), leave $p_j$ untouched, and bisect every other
piece $p_m$ ($m\ne i,j$) into $(p_m/2,p_m/2)$ (one cut each). This uses
exactly $1+(n+1-2)=n$ cuts, the full budget. Assume genericity: $\ell$ does
not equal $p_j$ or any $p_m/2$ ($m\ne i,j$), and no two of the $p_m/2$
coincide by accident of an unrelated tie (holds off a measure-zero set; the
tied case follows by continuity of the resulting explicit formula in
$(p_1,\dots,p_{n+1})$, the same closure argument used for the certified
Suffix-Match Insertion Lemma). Then the resulting multiset $M$ has
$$\mathrm{OddSum}(M)=\frac{1+p_i-p_j}{2}.$$

**Proof.** Group $M$ by value. Value $p_j$ occurs with multiplicity $2$
(once as the untouched original piece, once as the fragment of $p_i$ tied
to it). For each $m\ne i,j$, value $p_m/2$ occurs with multiplicity $2$
(both halves of the bisected piece $p_m$). Value $\ell:=p_i-p_j$ occurs
with multiplicity $1$ (a singleton, generically distinct from every other
value present). So every value in $M$ other than $\ell$ occurs with
**even** multiplicity; sorted descending, $M$ decomposes into a disjoint
union of consecutive-rank blocks, one per distinct value, all of even
length except for exactly one block of length $1$ (the singleton $\ell$).

By the Claim proved inside the certified Doubling Lemma
(`doubling-lemma-and-generalized-duplicate-the-rest.md`, Theorem 1): a
block of even length, wherever it starts in the global sort order, splits
exactly half its copies to the first-mover — this holds regardless of what
other blocks surround it, since the argument depends only on parity of
consecutive integers within the block's own rank interval. Applying this
to the $p_j$-block (length $2$) gives contribution $p_j$; applying it to
each $p_m/2$-block (length $2$) gives contribution $p_m/2$. Summing over
all even blocks:
$$\text{(even-block total)}=p_j+\sum_{m\ne i,j}\frac{p_m}{2}
=p_j+\frac{1-p_i-p_j}{2},$$
independent of where $\ell$ sits among these blocks.

For $\ell$'s own contribution: let $E$ be the number of elements of $M$
strictly exceeding $\ell$. Since $\ell$ is generically untied with
anything else, $M\setminus\{\ell\}$ splits into blocks each lying entirely
above or entirely below $\ell$ (a block of one fixed value cannot straddle
$\ell$). Hence $E$ is a sum of the lengths of exactly those blocks lying
above $\ell$ — each such length is $2$ (or, after merging with an
accidental extra tie, still an even number) — so $E$ is **always even**,
regardless of the specific value of $\ell$ or of the partition.
Consequently $\ell$ occupies rank $E+1$, always **odd**, so $\ell$ is
claimed by the first-mover in full.

Summing: $\mathrm{OddSum}(M)=p_j+\dfrac{1-p_i-p_j}{2}+(p_i-p_j)
=\dfrac{1+p_i-p_j}{2}$. $\blacksquare$

**Independent numerical verification.** Checked by direct simulation
(sort-and-sum, not the closed-form formula) over $3{,}000$ random
partitions with $k\in\{3,\dots,8\}$ pieces, uniformly random valid pairs
$(i,j)$: maximum observed discrepancy between the formula and the
brute-force computation was $2.2\times10^{-16}$ (floating-point roundoff
only) — zero substantive mismatches.

**Corollary (closes a new sub-case of the balanced upper-bound region).**
Applying the lemma with the pair $(i,i+1)$ minimizing the consecutive gap
$g:=\min_{1\le i\le n}(p_i-p_{i+1})$ (minimizing $p_i-p_j$ over all valid
pairs is achieved at an adjacent pair, since $p_i-p_j=\sum_{r=i}^{j-1}
(p_r-p_{r+1})$ is a sum of $\ge1$ nonnegative consecutive gaps) gives
$$\mathrm{OddSum}=\frac{1+g}{2}\le c(n)\iff g\le 2c(n)-1=\frac1{2^{n+1}-1}.$$
This unconditionally closes the sub-case of the balanced region
($p_1<1/2$, $p_{n+1}>1/(2^{n+1}-1)$) where some consecutive gap is
$\le1/(2^{n+1}-1)$, for every $n\ge1$. **Not** a closure of the whole
balanced region: numerically, this sub-case's coverage of the balanced
region shrinks as $n$ grows (from $\approx97\%$ at $n=2$ to $\approx23\%$
at $n=10$ in random sampling) — see `approaches/universal-halving-
adversary.md` for the full table and the (open) residual "all gaps large"
sub-case.

**Reusability.** The underlying structural fact — "a single singleton
value, generically untied, surrounded entirely by even-multiplicity value
blocks, always lands at an odd rank (contributes in full)" — is a clean,
general, reusable sub-lemma independent of this specific merge
construction, and is a genuine strengthening/companion of the
already-certified Doubling Lemma / General Insertion Lemma /
Suffix-Match Insertion Lemma family: it shows the exact-value machinery
extends cleanly to constructions that create ties between *distinct
original pieces* (not just self-duplication of a split piece), which may
be useful for any future multi-piece coordinated construction attempt.
