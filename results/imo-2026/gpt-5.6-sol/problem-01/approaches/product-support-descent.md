## Status
solved

## Approaches tried
- Product-support descent followed by primewise Euclidean invariants — worked: the integer monovariant \(2^{r(B)}P(B)\) proves termination, and the gcds of the positive prime exponents determine the unique terminal nonunit.

## Current best
The complete proof below establishes both requested claims and, more precisely, identifies the terminal integer as
\[
M=\prod_{p\in\mathcal P}p^{g_p},
\qquad
g_p=\gcd\{v_p(a_i):v_p(a_i)>0\},
\]
where \(a_1,\dots,a_{2026}\) are the initial entries and \(\mathcal P\) is the set of primes dividing at least one initial entry.

## Full proof
Let a *board* mean the ordered collection of the 2026 positive integers currently occupying the 2026 places. Although all entries are initially greater than \(1\), entries equal to \(1\) may be produced by moves.

We first prove termination by the **invariant/monovariant method** from the Knowledge Base. For a board \(B\), define
\[
P(B)=\prod_{b\in B}b,
\qquad
r(B)=\#\{b\in B:b>1\},
\qquad
F(B)=2^{r(B)}P(B).
\]
Thus \(F(B)\) is a positive integer.

Consider a legal move, and denote the two selected entries by \(m,n>1\). Put
\[
d=\gcd(m,n),\qquad L=\operatorname{lcm}(m,n).
\]
The two new entries are \(d\) and \(L/d\). Both are positive integers: \(d\geq 1\), and \(d\mid L\) because every common divisor of \(m,n\), in particular their greatest common divisor, divides every common multiple of \(m,n\). The standard gcd–lcm identity
\[
dL=mn
\]
gives
\[
d\cdot\frac Ld=L=\frac{mn}{d}.
\]
Consequently, if \(B'\) is the board after the move, then
\[
P(B')=\frac{P(B)}d. \tag{1}
\]
We now separate two exhaustive cases.

If \(d=1\), then the new pair is
\[
\left(1,\frac{L}{1}\right)=(1,mn),
\]
since coprimality gives \(L=mn\). As \(m,n>1\), their product \(mn\) is greater than \(1\). Thus two nonunit entries have been replaced by exactly one nonunit entry, while all other places are unchanged. Hence
\[
r(B')=r(B)-1,
\qquad P(B')=P(B),
\]
and therefore
\[
F(B')=2^{r(B)-1}P(B)=\frac{F(B)}2<F(B). \tag{2}
\]

If \(d>1\), the first new entry \(d\) is greater than \(1\). The second new entry \(L/d\) is a positive integer and may either equal \(1\) or exceed \(1\). Therefore the new pair contributes either one or two entries greater than \(1\), whereas the old pair contributed two. This includes the case \(m=n\), for then \(d=L=m\) and the new pair is \((m,1)\). In every subcase,
\[
r(B')\leq r(B).
\]
Combining this with (1) and \(d\geq2\), we obtain
\[
F(B')=2^{r(B')}\frac{P(B)}d
\leq 2^{r(B)}\frac{P(B)}d
=\frac{F(B)}d
\leq\frac{F(B)}2<F(B). \tag{3}
\]

Equations (2) and (3) show that every legal move strictly decreases the positive integer \(F(B)\). By the **well-ordering principle**, equivalently the **infinite-descent principle** from the Knowledge Base, there cannot be infinitely many legal moves: an infinite play would produce an infinite strictly decreasing sequence of positive integers. Hence every play stops after finitely many moves.

A move is legal precisely when two different places both contain integers greater than \(1\). Therefore a terminal board has at most one entry greater than \(1\). It remains to prove that it has exactly one such entry and that this entry is independent of the choices.

We use **divisor analysis** prime by prime. Let \(a_1,\dots,a_{2026}\) be the initial entries, and let \(\mathcal P\) be the set of all primes dividing at least one \(a_i\). This set is finite because it is the set of prime divisors of the fixed positive integer \(a_1a_2\cdots a_{2026}\). It is nonempty because every \(a_i>1\) has a prime divisor.

Fix \(p\in\mathcal P\). For every board \(B\), consider the nonzero \(p\)-adic valuations of its entries and define
\[
I_p(B)=\gcd\{v_p(b): b\in B,\ v_p(b)>0\}, \tag{4}
\]
provided the displayed set is nonempty. We prove simultaneously that this set remains nonempty and that \(I_p(B)\) is invariant under every move.

For a move on \(m,n\), write
\[
x=v_p(m),\qquad y=v_p(n).
\]
The elementary prime-valuation formulas for gcd and lcm are
\[
v_p(\gcd(m,n))=\min(x,y),
\qquad
v_p(\operatorname{lcm}(m,n))=\max(x,y).
\]
Since valuations turn quotients into differences whenever the quotient is an integer, the valuations at the two new places are
\[
\left(\min(x,y),\,\max(x,y)-\min(x,y)\right)
 =\left(\min(x,y),\,|x-y|\right). \tag{5}
\]
We check all possible zero and equality configurations in (5).

- If \(x=y=0\), the pair \((0,0)\) remains \((0,0)\). It contributes no positive valuation either before or after the move.
- If exactly one valuation is zero, say \(x=0<y\), then the new pair is \((0,y)\). If instead \(y=0<x\), it is \((0,x)\). Thus the sole positive valuation contributed by the selected places is unchanged.
- If \(x,y>0\) and \(x\ne y\), suppose without loss of generality that \(x<y\). The positive pair \((x,y)\) is replaced by \((x,y-x)\). A positive integer divides both \(x\) and \(y\) if and only if it divides both \(x\) and \(y-x\): one direction uses divisibility of a difference, and the reverse direction uses \(y=x+(y-x)\). Hence
\[
\gcd(x,y)=\gcd(x,y-x).
\]
The case \(y<x\) is the same computation with \(x,y\) interchanged.
- If \(x=y>0\), the new pair is \((x,0)\). The gcd of the two old positive valuations is \(x\), and after zero valuations are omitted, the gcd of the selected places' positive valuations is still \(x\).

These four cases are exhaustive. They show, first, that the selected places contain a positive \(p\)-valuation after the move if and only if they contained one before it. Since the unselected places do not change and \(p\in\mathcal P\) occurs initially, the set in (4) is nonempty on every reachable board.

They also show that replacing the selected valuations does not change their common positive divisors. To include the unselected valuations explicitly, an integer \(c>0\) divides every positive \(p\)-valuation on the old board if and only if it divides every positive valuation at the unselected places and every positive valuation among \(x,y\). By the case analysis above, the latter condition is equivalent to divisibility of every positive valuation at the unselected places and every positive valuation in \((\min(x,y),|x-y|)\). This is exactly the assertion that \(c\) divides every positive \(p\)-valuation on the new board. Thus the old and new collections have the same set of common divisors and therefore the same greatest common divisor. We have proved
\[
I_p(B')=I_p(B). \tag{6}
\]

Now let \(T\) be the terminal board reached by an arbitrary play. For each \(p\in\mathcal P\), the support-persistence just proved ensures that some entry of \(T\) has positive \(p\)-valuation. In particular, \(T\) is not the all-ones board. Since terminality already showed that \(T\) has at most one nonunit entry, it has exactly one; call that entry \(M\). This proves part (a).

For each \(p\in\mathcal P\), define from the initial board
\[
g_p=\gcd\{v_p(a_i):v_p(a_i)>0\}.
\]
On the terminal board, \(M\) is the only entry that can have positive \(p\)-valuation, and support persistence says that this valuation is indeed positive. Therefore the set of positive \(p\)-valuations on \(T\) is the singleton \(\{v_p(M)\}\). Applying invariance (6) from the initial board to \(T\) yields
\[
v_p(M)=I_p(T)=I_p(B_0)=g_p \qquad(p\in\mathcal P). \tag{7}
\]

We must also exclude the appearance of new primes. If a prime \(q\notin\mathcal P\), every initial \(q\)-valuation is zero. Formula (5), specifically its \((0,0)\) case, shows inductively that after every move all \(q\)-valuations are still zero. Hence no prime outside \(\mathcal P\) divides \(M\).

Finally, the **Fundamental Theorem of Arithmetic** says that a positive integer is uniquely determined by all its prime exponents. Equation (7), together with the absence of primes outside \(\mathcal P\), gives
\[
M=\prod_{p\in\mathcal P}p^{g_p}.
\]
The right-hand side depends only on the initial entries and not on any choices made during the play. Thus every play has the same terminal integer \(M\), proving part (b). ∎

## Promotable lemmas
- **Product-support termination lemma.** For any finite board of positive integers on which a legal move selects two nonunits \(m,n\) and replaces them by \(\gcd(m,n)\) and \(\operatorname{lcm}(m,n)/\gcd(m,n)\), the quantity \(2^{r(B)}P(B)\), where \(r(B)\) is the number of nonunits and \(P(B)\) is the board product, strictly decreases. Proved in the first half of the Full proof, including both gcd cases and the equal-input subcase.
- **Positive-valuation Euclidean invariant.** Under the same operation, for each prime that occurs on the board, the gcd of all positive valuations at that prime is invariant, and the prime continues to occur. Proved in the four-case valuation analysis in the Full proof.
