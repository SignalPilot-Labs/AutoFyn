# General Consecutive-Block AltSum Formula, and the Bottom-Block-Doubling exact value

Certified round 9. Proved in `approaches/lp-duality-split-polytope.md`
(round 9, "Round 9: the 2-piece sufficiency direction fails for large
$n$" section).

## General Consecutive-Block AltSum Formula

**Statement.** For integers $c\ge0$, $m\ge0$, let
$\mathrm{Blk}(c,m):=\mathrm{AltSum}(\{c+1,c+2,\dots,c+m\})$ (a block of
$m$ consecutive integers starting just above $c$). Then
$$\mathrm{Blk}(c,m)=\begin{cases}0,&m=0\\ m/2,&m>0\text{ even}\\
(m-1)/2+(c+1),&m\text{ odd}.\end{cases}$$

**Proof.** $m=0$ is the empty-sum convention. For $m>0$, sort descending:
$c+m,c+m-1,\dots,c+1$. Pair consecutive terms from the top: each pair
$(c+m-2j)-(c+m-2j-1)=1$. If $m$ is even there are exactly $m/2$ pairs and
nothing left over, giving $m/2$. If $m$ is odd there are $(m-1)/2$ pairs
(using the top $m-1$ elements) plus one unpaired final term — the
smallest element $c+1$, at rank $m$ (odd), taken with a $+$ sign — giving
$(m-1)/2+(c+1)$. $\blacksquare$

(Note: this formula is NOT $\lceil m/2\rceil$ for $c>0$ — that simpler
form only holds at $c=0$. An early hand-derivation this round wrongly
assumed the $c=0$ form holds for all $c$; this is corrected here.)

**Reviewer verification.** Independently re-derived by direct exact
`Fraction` computation of `AltSum` on the literal consecutive-integer set
for every $c\in\{0,\dots,14\}$, $m\in\{0,\dots,14\}$ (225 instances):
exact agreement in every case.

## Bottom-Block-Doubling exact value

**Statement.** Fix $N\ge4$ (triangular-family piece count) and let
$k=k(N)$ be the largest integer with $k(k+1)/2\le2N-1$. Let $L:=\{1,\dots,
N-2\}$ and let $W$ be the multiset consisting of one extra copy of each of
$1,2,\dots,k$ together with two equal filler fragments each of value
$\tfrac12(2N-1-k(k+1)/2)$ (chosen, via a finite coincidence-avoidance rule,
to be distinct from every value in $L\cup\{1,\dots,k\}$). Then, writing
$m:=N-2-k$,
$$\mathrm{AltSum}(L\cup W)=\mathrm{Blk}(k,m).$$

**Proof.** $L\cup W$ decomposes into three contiguous (in sorted order)
blocks: the doubled bottom block $\{1,1,2,2,\dots,k,k\}$ (every value
$\le k$, strictly below the untouched suffix $\{k+1,\dots,N-2\}$), the
untouched suffix itself, and the filler block (an even number of equal
copies of a value distinct from every landmark, sitting below the
suffix). Each doubled pair $j,j$ occupies two consecutive ranks and
contributes $0$ to $\mathrm{AltSum}$ (one $+$, one $-$, equal values); an
even-length block of equal filler values likewise contributes $0$ and,
because it shifts every element below it by an even count, does not
change any other element's rank parity. Both extra blocks sit strictly
below the untouched suffix, so the suffix's own ranks (and hence its
contribution) are unaffected, equal to its standalone value
$\mathrm{Blk}(k,m)$. Summing (suffix $\mathrm{Blk}(k,m)$ + doubled block
$0$ + filler $0$) gives the claim. $\blacksquare$

**Reviewer verification.** Independently re-implemented the construction
from scratch (own script, not the builder's) and directly computed
`AltSum(L ∪ W)` via exact `Fraction` sort-and-alternate for every
$N=4,\dots,59$ (56 instances): exact agreement with $\mathrm{Blk}(k,m)$ in
every case, and the reported $k(N)$ values ($k(4)=3$, $k(7)=4$, $k(20)=8$,
$k(39)=11$) independently reproduced.

**What this does and does not resolve.** These are general-purpose,
reusable exact facts. They do **not**, by themselves, prove that 2-piece
(or any bounded-piece-count) responses are insufficient for the
triangular family in general — that conclusion (see
`approaches/lp-duality-split-polytope.md` round 9) additionally uses the
order-of-magnitude comparison (achieved excess $\Theta(1/N)$ vs. threshold
$\Theta(2^{-N})$, exact for the two specific families tried, but not a
proof ruling out every conceivable 2-piece construction) and is reported
there as strong evidence, not a certified general impossibility theorem.
