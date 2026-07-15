## Status
solved

## Approaches tried
- Prime-factor multiplicity descent followed by primewise subtractive-Euclidean invariants — worked: the lexicographic monovariant proves termination, and the invariants determine the unique terminal nonunit.

## Current best
For an initial board \((a_1,\ldots,a_{2026})\), let \(P\) be the set of primes dividing at least one \(a_i\), and define
\[
g_p=\gcd\{v_p(a_i):v_p(a_i)>0\}\qquad(p\in P).
\]
Every play terminates with exactly one nonunit, and that nonunit is
\[
M=\prod_{p\in P}p^{g_p}.
\]

## Full proof
Write a board state as \(B=(b_1,\ldots,b_{2026})\). We use the **Invariant / monovariant** method from the Knowledge Base twice: first to prove termination and then to identify the terminal state.

For a positive integer \(t\), let \(\Omega(t)\) denote the number of prime factors of \(t\), counted with multiplicity; in particular, \(\Omega(1)=0\). By the Fundamental Theorem of Arithmetic,
\[
\Omega(uv)=\Omega(u)+\Omega(v)
\]
for all positive integers \(u,v\). Define
\[
S(B)=\sum_{i=1}^{2026}\Omega(b_i),
\qquad
r(B)=\#\{i:b_i>1\}.
\]
We order pairs in \(\mathbb N^2\) lexicographically: \((s',r')<(s,r)\) if either \(s'<s\), or \(s'=s\) and \(r'<r\).

Consider a legal move on entries \(m,n>1\), and put \(d=\gcd(m,n)\) and \(L=\operatorname{lcm}(m,n)\). The two new entries are \(d\) and \(L/d\), both of which are positive integers: indeed, \(d\mid L\), since \(d\mid m\) and \(m\mid L\). The standard gcd-lcm identity gives
\[
L=\frac{mn}{d}.
\]
Using complete additivity of \(\Omega\), first on \(mn=dL\) and then on \(L=d(L/d)\), we obtain
\[
\Omega(m)+\Omega(n)=\Omega(d)+\Omega(L)
\]
and
\[
\Omega(L)=\Omega(d)+\Omega(L/d).
\]
Consequently,
\[
\begin{aligned}
\Omega(d)+\Omega(L/d)
&=\Omega(L)\\
&=\Omega(m)+\Omega(n)-\Omega(d).
\end{aligned}
\]
Thus the exact change in the first coordinate is
\[
S(B)-S(B')=\Omega(d),
\]
where \(B'\) is the board after the move.

There are two disjoint and exhaustive cases.

- If \(d>1\), then the prime factorization of \(d\) contains at least one prime, so \(\Omega(d)>0\). Hence \(S(B')<S(B)\), and therefore \((S(B'),r(B'))<(S(B),r(B))\), regardless of the change in \(r\).
- If \(d=1\), then \(L=mn\), so the selected pair \((m,n)\) is replaced by \((1,mn)\). Since both selected entries were greater than \(1\), they contributed two to \(r(B)\); since \(mn>1\), the new pair contributes one. All other entries are unchanged, so \(S(B')=S(B)\) and \(r(B')=r(B)-1\). Again \((S(B'),r(B'))<(S(B),r(B))\).

Therefore every move strictly decreases \((S,r)\) in the lexicographic order. This order is well-founded for the present process. More explicitly, the nonnegative integer \(S\) can strictly decrease only finitely many times. During any interval of moves for which \(S\) is fixed, every move strictly decreases the nonnegative integer \(r\), and \(0\le r\le2026\), so such an interval has at most \(2026\) moves. It follows that an infinite sequence of moves is impossible. This is the **Infinite descent** principle from the Knowledge Base, applied to the lexicographic monovariant. Hence every play terminates after finitely many moves.

At a terminal board there is at most one entry greater than \(1\): if two such entries occupied different places, they would form a legal pair and another move would be possible. It remains to show that there is a nonunit at the end and that its value is forced.

Fix a prime \(p\). By the standard valuation formulas for gcd and lcm,
\[
v_p(\gcd(m,n))=\min(v_p(m),v_p(n)),
\qquad
v_p(\operatorname{lcm}(m,n))=\max(v_p(m),v_p(n)).
\]
Since valuations turn quotients into differences, if \(x=v_p(m)\) and \(y=v_p(n)\), then the selected pair of exponents changes as
\[
(x,y)\longmapsto
\bigl(\min(x,y),\max(x,y)-\min(x,y)\bigr)
=\bigl(\min(x,y),|x-y|\bigr).
\]
All other \(p\)-exponents remain unchanged.

Suppose that \(p\) occurs somewhere on the current board, and define
\[
I_p(B)=\gcd\{v_p(b_i):v_p(b_i)>0\}.
\]
The set inside this gcd is nonempty. We prove that one move preserves both its nonemptiness and its gcd. It suffices to analyze the two selected exponents \(x,y\); the following cases are disjoint and exhaustive.

1. If \(x=y=0\), they are replaced by \((0,0)\). The list of positive exponents is unchanged.
2. If exactly one exponent is zero, say \(x=0<y\), they are replaced by \((0,y)\); if \(y=0<x\), they are replaced by \((0,x)\). In either subcase the same single positive exponent remains.
3. If \(x,y>0\) and \(x\ne y\), assume without loss of generality that \(x<y\). They are replaced by \((x,y-x)\), both positive. For every positive integer \(c\),
\[
c\mid x\text{ and }c\mid y
\quad\Longleftrightarrow\quad
c\mid x\text{ and }c\mid(y-x).
\]
The forward implication follows because a common divisor divides a difference; the reverse implication follows because \(y=x+(y-x)\). Thus the old pair and new pair have exactly the same common divisors. After adjoining the unchanged positive exponents from all other places, the entire old and new positive-exponent lists also have exactly the same common divisors, and hence the same gcd.
4. If \(x=y>0\), they are replaced by \((x,0)\). Replacing two copies of the same positive integer \(x\) by one copy of \(x\) changes neither the set of common divisors nor its greatest element. In particular, a positive exponent remains.

This proves that \(I_p(B)\) is invariant whenever \(p\) occurs, and it also proves that a prime occurring on a board continues to occur after every move. Notice also that a prime absent from a board cannot appear in the next state: for such a prime the selected exponent pair is \((0,0)\), which remains \((0,0)\). Thus the set of primes occurring on the board is exactly preserved.

Let the initial entries be \(a_1,\ldots,a_{2026}\), and let
\[
P=\{p:p\text{ is prime and }p\mid a_i\text{ for some }i\}.
\]
This is a finite nonempty set by the Fundamental Theorem of Arithmetic, because there are finitely many initial integers and each is greater than \(1\). For each \(p\in P\), put
\[
g_p=\gcd\{v_p(a_i):v_p(a_i)>0\}.
\]
The support persistence just proved implies that every \(p\in P\) still occurs at every later state. In particular, a terminal board cannot consist entirely of ones. Since a terminal board has at most one nonunit, it therefore has exactly one nonunit; call it \(M\). This proves part (a).

For each \(p\in P\), the only positive \(p\)-valuation on the terminal board is now \(v_p(M)\). Reading the invariant at that board gives
\[
v_p(M)=I_p(\text{terminal board})=I_p(\text{initial board})=g_p.
\]
For every prime \(q\notin P\), support preservation gives \(v_q(M)=0\). The uniqueness clause in the Fundamental Theorem of Arithmetic therefore yields
\[
M=\prod_{p\in P}p^{g_p}.
\]
The right-hand side depends only on the initial board and not on any choices made during the play. Hence every possible play ends with the same value of \(M\), proving part (b). ∎

## Promotable lemmas
- **Positive-valuation Euclidean invariant.** Under a blackboard move, for every prime currently occurring, the gcd of its positive valuations is preserved, and the prime continues to occur. Proved in the four-case valuation analysis in the Full proof.
- **Lexicographic multiplicity descent.** For \(S=\sum_i\Omega(b_i)\) and \(r=\#\{i:b_i>1\}\), every legal move strictly decreases \((S,r)\) lexicographically. Proved in the termination portion of the Full proof.
