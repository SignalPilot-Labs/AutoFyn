Solution

  Setup and notation

  For a prime $p$ and a positive integer $x$, let $v_p(x)$ denote the exponent of $p$ in the factorization of $x$ (so $v_p(1)=0$).
  Throughout, "the board" refers to the multiset of $2026$ positive integers occupying the $2026$ fixed positions; a move only ever
  changes the values at two positions, never the number of positions.

  For a set of $2026$ nonnegative integers (indexed by the board positions) we use the convention $\gcd(0,k)=k$ and $\gcd(0,\dots,0)=0$;
  this is the standard extension and makes $\gcd$ on $\mathbb{Z}_{\ge0}$ associative and commutative.

  Key elementary fact used repeatedly: for $a,b\in\mathbb Z_{\ge 0}$,
  $$\gcd(\min(a,b),,|a-b|)=\gcd(a,b).\qquad(\star)$$
  Proof: WLOG $a\ge b$. Then $\min(a,b)=b$ and $|a-b|=a-b$, and $\gcd(b,a-b)=\gcd(a,b)$ is the usual Euclidean subtraction identity
  (valid also when $b=0$, giving $\gcd(0,a)=a$). $\blacksquare$

  Lemma 1 (a hidden invariant)

  For every prime $p$, the quantity
  $$G_p ;:=; \gcd\big(v_p(x_1),\dots,v_p(x_{2026})\big)$$
  (gcd of the exponents of $p$ over all 2026 board entries) is unchanged by every move.

  Proof. Fix a move on values $m,n>1$ sitting at positions $i,j$. Since $v_p(\gcd(m,n))=\min(v_p(m),v_p(n))$ and
  $v_p(\mathrm{lcm}(m,n))=\max(v_p(m),v_p(n))$ for every prime $p$, the new value at position $i$ has $p$-exponent $\min(a,b)$ and the
  new value at position $j$ has $p$-exponent $\max(a,b)-\min(a,b)=|a-b|$, where $a=v_p(m),,b=v_p(n)$. All other $2024$ positions are
  untouched.

  Let $c$ denote the gcd of the exponents at the $2024$ untouched positions. By associativity of $\gcd$,
  $$\text{gcd before move} = \gcd(c,a,b) = \gcd\big(c,\gcd(a,b)\big),$$
  $$\text{gcd after move} = \gcd\big(c,\min(a,b),|a-b|\big) = \gcd\big(c,\gcd(\min(a,b),|a-b|)\big).$$
  By $(\star)$ these two are equal. Hence $G_p$ is invariant. $\blacksquare$

  This holds simultaneously for every prime $p$ — in particular $G_p$ is completely determined by the initial board and never changes
  again, regardless of which moves are made.

  Lemma 2 (the process is finite)

  Let $\Omega(x)$ denote the number of prime factors of $x$ counted with multiplicity ($\Omega(1)=0$), and for a board state let
  $$\Phi = \sum_{i=1}^{2026}\Omega(x_i), \qquad N = #{i : x_i>1}.$$
  Every move strictly decreases the pair $(\Phi,N)$ in lexicographic order (with $\Phi$ non-increasing and $N$ non-increasing at every 
  step).

  Proof. Consider a move on $m,n>1$, with $g=\gcd(m,n)$, $\ell=\mathrm{lcm}(m,n)$, new values $g,\ \ell/g$.

  Using exponents again, for each prime $p$ with $a=v_p(m),b=v_p(n)$: the contribution to $\Omega(m)+\Omega(n)$ is $a+b$, while the
  contribution to $\Omega(g)+\Omega(\ell/g)$ is $\min(a,b)+|a-b| = \max(a,b)$. Summing over all primes,
  $$\big(\Omega(g)+\Omega(\ell/g)\big) - \big(\Omega(m)+\Omega(n)\big) = -\sum_p \min(a,b) = -\Omega(\gcd(m,n)).$$
  So $\Delta\Phi = -\Omega(g) \le 0$.

  Case $g>1$: $\Omega(g)\ge1$, so $\Phi$ strictly decreases. Also, since $g>1$, the new value $g$ is $>1$; and $\ell/g=1$ iff $\ell=g$
  iff $m=n$. So $N$ either stays the same (if $m\ne n$) or drops by exactly $1$ (if $m=n$) — in particular $N$ never increases.

  Case $g=1$: Then $\ell = mn$, so the two new values are exactly $1$ and $mn$. Thus $\Phi$ is unchanged
  ($\Omega(mn)=\Omega(m)+\Omega(n)$), while $N$ strictly decreases by exactly $1$, since two entries $>1$ ($m,n$) become one entry equal
  to $1$ and one entry $mn>1$.

  In both cases $\Phi$ never increases, $N$ never increases, and at least one of the two strictly decreases. Hence $(\Phi,N)$ strictly
  decreases in the lexicographic order on $\mathbb Z_{\ge0}\times\mathbb Z_{\ge0}$ at every move. Since this order is well-founded, only
  finitely many moves can occur, regardless of Confucius's choices. $\blacksquare$

  Part (a): termination with exactly one integer $>1$

  By Lemma 2 the process must stop after finitely many moves. It stops precisely when no legal move is available, i.e. when $N\le 1$
  (fewer than two entries are $>1$). It remains to rule out $N=0$.

  Since every one of the initial $2026$ integers is $>1$, their product exceeds $1$, so some prime $p_0$ divides at least one initial
  number; that is, some initial exponent $v_{p_0}(x_i)>0$. By our convention on $\gcd$ with zeros, the gcd of the $2026$ initial
  exponents at $p_0$ (all $\ge 0$, at least one $>0$) satisfies
  $$G_{p_0} \ge 1.$$

  By Lemma 1, $G_{p_0}$ is the same number at the terminal board. If the terminal board had $N=0$ (all entries equal to $1$), every
  exponent $v_{p_0}$ would be $0$, forcing $\gcd$ of the terminal exponents $=0\ne G_{p_0}$ — a contradiction.

  Hence $N\ne 0$ at termination, and combined with $N\le1$ we conclude:
  $$\boxed{N=1 \text{ at termination.}}$$

  Thus after finitely many moves, no matter how Confucius plays, exactly one integer $M>1$ remains on the board. This proves (a).

  Part (b): $M$ is independent of the choices made

  At termination exactly one position holds a value $M>1$ and all other $2025$ positions hold the value $1$. Fix any prime $p$. The
  terminal exponents of $p$ across the board are $v_p(M)$ at the one special position and $0$ at all other $2025$ positions. Hence
  $$\gcd(\text{terminal exponents of } p) = \gcd\big(v_p(M),0,0,\dots,0\big) = v_p(M).$$

  By Lemma 1, this terminal gcd equals the initial gcd $G_p=\gcd\big(v_p(x_1^{(0)}),\dots,v_p(x_{2026}^{(0)})\big)$, a quantity computed
  purely from the original numbers on the blackboard and completely unaffected by which pairs Confucius chooses or in what order.
  Therefore
  $$v_p(M) = G_p \quad\text{for every prime } p,$$
  and since only finitely many primes have $G_p>0$,
  $$\boxed{M ;=; \prod_{p \text{ prime}} p^{,G_p}}, \qquad G_p=\gcd\big(v_p(x_1^{(0)}),\dots,v_p(x_{2026}^{(0)})\big),$$
  which depends only on the initial $2026$ integers and not at all on the sequence of moves Confucius performs. This proves (b).
  $\blacksquare$

  Sanity check (worked example)

  Board ${4,6,9}$: $G_2=\gcd(2,1,0)=1$, $G_3=\gcd(0,1,2)=1$, predicting $M=2\cdot3=6$.
  - Route 1: $(4,6)\to(2,6)$ on ${4,6,9}$ gives ${2,6,9}$; then $(6,9)\to(3,6)$ gives ${2,3,6}$; then $(2,3)\to(1,6)$ gives ${1,6,6}$;
  then $(6,6)\to(6,1)$ gives ${1,1,6}$. Result: $M=6$.
  - Route 2: $(4,9)\to(1,36)$ gives ${1,6,36}$; then $(6,36)\to(6,6)$ gives ${1,6,6}$; then $(6,6)\to(6,1)$ gives ${1,1,6}$. Result:
  $M=6$.

  Both routes agree with the formula, confirming the invariant.

✻ Crunched for 2m 55s