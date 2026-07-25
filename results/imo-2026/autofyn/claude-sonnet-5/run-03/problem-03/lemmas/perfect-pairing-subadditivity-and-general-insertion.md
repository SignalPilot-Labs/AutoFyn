# Certified (round 3): Perfect-Pairing Corollary, Subadditivity Lemma, General Insertion Lemma

Certified from `approaches/universal-halving-adversary.md` (round 3 section),
replacing `CANDIDATE-perfect-pairing-and-subadditivity.md`. Proof-reviewer
independently re-derived/verified all three claims below (numeric stress
tests with zero violations across tens of thousands of random trials each,
plus exact-rational spot checks); see round-3 review for details.

## Theorem 3 (Perfect-Pairing / Bisect-Everything Corollary)

**Statement.** Let $p_1\ge\cdots\ge p_k>0$ sum to $1$ with $k\le n$ (LB used
strictly fewer than the full $n+1$-piece budget). XY has a response using
exactly $k\ (\le n)$ cuts (bisect every piece) achieving
$\mathrm{OddSum}=1/2\le c(n)$ **exactly**, for every $n\ge0$ and every such
partition.

**Proof.** XY bisects every piece, $p_i\mapsto(p_i/2,p_i/2)$. Let
$R:=(p_1/2,\dots,p_k/2)$ ($\mathrm{sum}(R)=1/2$); the response multiset is
exactly $R\cup R$. By the certified Doubling Lemma
(`doubling-lemma-and-generalized-duplicate-the-rest.md`, Theorem 1),
$\mathrm{OddSum}(R\cup R)=\mathrm{sum}(R)=1/2$. Since
$c(n)=2^n/(2^{n+1}-1)>1/2$ for every $n\ge0$ ($2\cdot2^n=2^{n+1}>2^{n+1}-1$),
this gives $\mathrm{OddSum}\le c(n)$. $\blacksquare$

Closes the entire slack-budget regime $k\le n$ unconditionally, for every
$n$ and every LB partition with fewer than $n+1$ pieces.

*(Reviewer verification: $c(n)>1/2$ checked exactly by rational arithmetic
$n=1..7$; Doubling Lemma itself independently re-verified below.)*

## Lemma S (Subadditivity of OddSum)

**Statement.** For any two finite multisets $A,B$ of positive reals,
$$\mathrm{OddSum}(A\cup B)\ \le\ \mathrm{OddSum}(A)+\mathrm{OddSum}(B),$$
unconditionally — no domination/interleaving hypothesis needed.

**Proof.** Strong induction on $|A|+|B|$. Base cases: either multiset empty,
trivial equality. Inductive step: let $x^*=\max(A\cup B)$, WLOG $x^*\in A$
(so $x^*=\max A$ too), $A':=A\setminus\{x^*\}$. Using the removal identity
$g(X)=f(X\setminus\{\max X\})$ (immediate from the certified Global-max
Peeling Lemma, `dominant-piece-lower-bound.md`'s underlying Lemma 3, plus
$f+g=\mathrm{sum}$) applied to both $A\cup B$ and $A$:
$f(A\cup B)=x^*+f(A'\cup B)$, $f(A)=x^*+f(A')$. The claim
$f(A\cup B)\le f(A)+f(B)$ reduces to $f(A'\cup B)\le f(A')+f(B)$, the
identical statement one element smaller, closed by the induction hypothesis.
$\blacksquare$

*(Reviewer verification: $5\times10^4$ random trials (multiset sizes 0-5,
values uniform in $(0,5)$), zero violations beyond float noise
$<2\times10^{-15}$; reviewer independently reproduced with a fresh script.)*

## Theorem 4 (General Insertion Lemma)

**Statement.** For any finite multiset $R$ of positive reals with
$\mathrm{sum}(R)=S$ and any real $\ell>0$ (no relation to $R$'s values
required),
$$\mathrm{OddSum}(R\cup R\cup\{\ell\}) = S+\ell.$$

Strictly generalizes `doubling-lemma-and-generalized-duplicate-the-rest.md`'s
Theorem 2 (which required $\ell=p_1-S\ge0$ under $p_1\ge S$) by dropping the
ordering hypothesis entirely.

**Proof.** Identical block-counting case split as Theorem 2's proof (whether
$\ell$ coincides with a distinct value of $R$ or not); re-examining that
argument shows it uses only "the count of $R\cup R$-elements exceeding
$\ell$ is even" (hence $\ell$'s own rank, or its merged block's start rank,
is odd), a purely combinatorial fact holding for *any* $\ell>0$ relative to
$R$'s values — the hypothesis $\ell=p_1-S\ge0$ in Theorem 2 was needed only
to make $\ell$ a valid non-negative fragment length in that specific
application, not anywhere inside the counting argument. $\blacksquare$

*(Reviewer verification: $5\times10^4$ random trials, $R$ size 0-5, $\ell$
unconstrained relative to $R$'s range (including above max$(R)$ and below
min$(R)$): zero violations beyond float noise $3.6\times10^{-15}$;
independently reproduced.)*

## Reuse notes
- Lemma S is a general-purpose merge upper bound usable by any approach
  needing to bound $\mathrm{OddSum}$ of a merged multiset without tracking
  exact interleaving.
- Theorem 4 justifies "bisect the top $n$ pieces, leave the smallest" as an
  exact-value construction, closing $T(n)$'s sub-case
  $p_{n+1}\le1/(2^{n+1}-1)$ unconditionally (proved in
  `approaches/universal-halving-adversary.md`, "Corollary: new closed
  sub-case").
