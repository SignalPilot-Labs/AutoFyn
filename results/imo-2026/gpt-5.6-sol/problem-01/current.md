## Status
solved

## Approaches tried
- Product-support descent followed by primewise Euclidean invariants — worked: the positive-integer monovariant \(2^{r(B)}P(B)\) strictly decreases at every move, while positive valuation support and its gcd persist primewise.
- Prime-factor multiplicity descent followed by primewise Euclidean invariants — worked independently: \((\sum_i\Omega(b_i),r(B))\) strictly decreases lexicographically, and the same primewise invariants identify the unique survivor.

## Current best
Both built approaches are complete. The proof below uses the shorter scalar monovariant. If the initial entries are \(a_1,\dots,a_{2026}\), the unique terminal nonunit is
\[
M=\prod_{p\mid a_1\cdots a_{2026}}p^{g_p},
\qquad
g_p=\gcd\{v_p(a_i):v_p(a_i)>0\}.
\]

## Full proof
Let a board state be \(B\). Define
\[
P(B)=\prod_{b\in B}b,
\qquad
r(B)=\#\{b\in B:b>1\},
\qquad
F(B)=2^{r(B)}P(B).
\]
We prove termination by the **invariant/monovariant method** from the Knowledge Base.

Suppose a move selects \(m,n>1\). Put \(d=\gcd(m,n)\) and \(L=\operatorname{lcm}(m,n)\). The replacement is \((d,L/d)\). By the gcd–lcm identity \(dL=mn\), the product of the replacement pair is
\[
d\frac Ld=L=\frac{mn}{d},
\]
so if \(B'\) is the resulting board, then
\[
P(B')=\frac{P(B)}d. \tag{1}
\]
If \(d=1\), then \(L=mn\), and the pair \((m,n)\) is replaced by \((1,mn)\). Thus \(r(B')=r(B)-1\) and \(P(B')=P(B)\), whence \(F(B')=F(B)/2<F(B)\).

If \(d>1\), the replacement contains the nonunit \(d\), while \(L/d\) is either \(1\) or a nonunit. Hence it contains at most the two nonunits that were selected, so \(r(B')\le r(B)\). By (1),
\[
F(B')=2^{r(B')}\frac{P(B)}d
\le \frac{F(B)}d
\le \frac{F(B)}2<F(B).
\]
Therefore every move strictly decreases the positive integer \(F(B)\). By the **well-ordering/infinite-descent principle** from the Knowledge Base, no infinite play is possible. Every play terminates.

A board is terminal exactly when it contains at most one integer greater than \(1\). We next prove that a terminal board contains exactly one and determine it.

Let \(\mathcal P\) be the finite nonempty set of primes dividing at least one initial entry. Fix \(p\in\mathcal P\). Whenever \(p\) occurs on a board, define
\[
I_p(B)=\gcd\{v_p(b):b\in B,\ v_p(b)>0\}.
\]
For a move on \(m,n\), write \(x=v_p(m)\), \(y=v_p(n)\). The standard valuation formulas for gcd and lcm give the replacement exponents
\[
(x,y)\longmapsto (\min(x,y),\max(x,y)-\min(x,y))
=(\min(x,y),|x-y|). \tag{2}
\]
We check every case:

- If \(x=y=0\), (2) is \((0,0)\); no positive exponent appears or disappears.
- If exactly one is positive, say \(x=0<y\), (2) is \((0,y)\), and similarly when \(y=0<x\). The sole positive exponent is unchanged.
- If \(0<x<y\), the positive pair \((x,y)\) becomes \((x,y-x)\). For every positive integer \(c\),
  \[
  c\mid x,\,c\mid y\quad\Longleftrightarrow\quad c\mid x,\,c\mid(y-x),
  \]
  so the common divisors, and hence the gcd, are unchanged. The case \(0<y<x\) is symmetric by interchanging the selected entries.
- If \(x=y>0\), the pair becomes \((x,0)\); after zero exponents are omitted, two copies of \(x\) have become one, preserving both positivity of the support and its gcd.

The unselected exponents are unchanged. Adjoining them to the selected old and new positive-exponent lists preserves the equivalence of their sets of common divisors. Thus \(p\) continues to occur after every move and \(I_p(B)\) is invariant. Conversely, if a prime is absent, its selected exponent pair is always \((0,0)\), so no new prime can appear.

Let \(T\) be any terminal board. Every \(p\in\mathcal P\) still occurs on \(T\), so \(T\) is not the all-ones board. Since it has at most one nonunit, it has exactly one; call it \(M\). This proves part (a).

For every \(p\in\mathcal P\), define
\[
g_p=\gcd\{v_p(a_i):v_p(a_i)>0\}.
\]
Because \(M\) is the only terminal nonunit and \(p\) still occurs, the terminal list of positive \(p\)-valuations is the singleton \(\{v_p(M)\}\). Invariance therefore yields
\[
v_p(M)=I_p(T)=I_p(B_0)=g_p.
\]
No prime outside \(\mathcal P\) can divide \(M\), because absent primes never appear. By the **Fundamental Theorem of Arithmetic**,
\[
M=\prod_{p\in\mathcal P}p^{g_p}.
\]
This expression depends only on the initial entries, not on the choices of moves. Hence the value of \(M\) is independent of Confucius's choices, proving part (b). ∎
