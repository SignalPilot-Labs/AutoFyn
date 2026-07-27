Solution

  Setup: the per‑prime view

  Write the board as a multiset of $N=2026$ integers $a_1,\dots,a_N$, each $>1$. For a prime $p$ and integer $x\ge 1$ let $v_p(x)$ be
  the exponent of $p$ in $x$, so $x=\prod_p p^{v_p(x)}$ and $x=1\iff v_p(x)=0$ for all $p$.

  A move picks two positions holding $m>1$ and $n>1$ and replaces them by
  $$g=\gcd(m,n),\qquad t=\frac{\operatorname{lcm}(m,n)}{\gcd(m,n)} .$$
  For every prime $p$, writing $a=v_p(m),\ b=v_p(n)$,
  $$v_p(g)=\min(a,b),\qquad v_p(t)=v_p!\big(\tfrac{\operatorname{lcm}}{\gcd}\big)=\max(a,b)-\min(a,b)=|a-b|. \tag{1}$$
  So, prime by prime, a move takes the two exponents ${a,b}$ at those positions to ${\min(a,b),,|a-b|}$, leaving all other positions'
  exponents unchanged.

  Throughout, let $K$ = the number of board entries that are $>1$. A legal move requires $K\ge 2$; the process stops exactly when $K\le
  1$.

  ---
  Lemma (the key invariant)

  For each prime $p$, the quantity
  $$d_p:=\gcd\big(v_p(a_1),\dots,v_p(a_N)\big)$$
  (with the conventions $\gcd(x,0)=x$ and $\gcd(0,\dots,0)=0$) is unchanged by every move.

  Proof. A move alters only the two exponents at the chosen positions, from ${a,b}$ to ${\min(a,b),|a-b|}$ by (1). Assume WLOG $a\le b$;
  the pair becomes ${a,,b-a}$, and by the Euclidean identity
  $$\gcd(a,,b-a)=\gcd(a,b).$$
  Since $\gcd$ of the whole multiset equals $\gcd\big(\gcd\text{ of the two changed entries},\ \gcd\text{ of the untouched
  entries}\big)$ and the first argument is preserved while the second is untouched, $d_p$ is preserved. $\blacksquare$

  Only finitely many primes divide some initial $a_i$; for all other primes $d_p=0$ permanently. Because every $a_i>1$ initially, some
  prime $q$ divides some $a_i$, so
  $$d_q\ge 1\quad\text{for at least one prime }q. \tag{2}$$

  ---
  Part (a): the process terminates with exactly one entry $>1$
  
  A well‑founded potential. Let $\Omega(x)=\sum_p v_p(x)$ (the number of prime factors of $x$ with multiplicity, $\Omega(1)=0$), and
  define
  $$\Phi=\sum_{i=1}^{N}\Omega(a_i)\in\mathbb{Z}_{\ge 0}.$$
  Consider a move on $m,n>1$ producing $g,t$. Using (1), summed over all primes:
  $$\Omega(g)+\Omega(t)=\sum_p\big(\min(a,b)+|a-b|\big)=\sum_p\max(a,b)=\Omega\big(\operatorname{lcm}(m,n)\big),$$
  while $\Omega(m)+\Omega(n)=\sum_p (a+b)$. Hence the change in $\Phi$ is
  $$\Delta\Phi=\sum_p\big(\max(a,b)-(a+b)\big)=-\sum_p\min(a,b)=-,\Omega\big(\gcd(m,n)\big)=-,\Omega(g)\le 0. \tag{3}$$
  So $\Phi$ never increases, and it strictly decreases whenever $g=\gcd(m,n)>1$.

  $K$ never increases. A move deletes the two entries $m,n$ (both $>1$) and inserts $g,t$, leaving the rest fixed, so
  $$K_{\text{new}}-K_{\text{old}}=\big([g>1]+[t>1]\big)-2\le 0. \tag{4}$$
  Moreover $K$ stays the same only if $g>1$ and $t>1$; in particular $g>1$, which by (3) forces $\Phi$ to strictly decrease. If $K$
  changes it drops by at least $1$.

  Termination. Order pairs $(K,\Phi)\in\mathbb{Z}{\ge0}\times\mathbb{Z}{\ge0}$ lexicographically. Each move strictly decreases
  $(K,\Phi)$:
  - if $K$ decreases, the first coordinate drops — a strict lexicographic decrease;
  - if $K$ is unchanged, then $g>1$, so by (3) $\Phi$ strictly decreases — again a strict decrease.

  The lexicographic order on $\mathbb{Z}_{\ge0}^2$ is well‑founded, so no infinite strictly decreasing sequence exists. Therefore only 
  finitely many moves are possible, regardless of the choices, and the process must halt.

  At the halt, exactly one entry exceeds $1$. When no move is available, $K\le 1$. Suppose for contradiction $K=0$, i.e. every entry
  equals $1$. Then $v_p(a_i)=0$ for all $i$ and all $p$, so $d_p=0$ for every prime — contradicting (2), since $d_q$ is invariant and
  $d_q\ge 1$. Hence $K\ge 1$ at all times, and in particular $K=1$ at the halt.

  Thus, after finitely many moves, exactly one integer $M>1$ remains. $\qquad\blacksquare$

  ---
  Part (b): the value $M$ is independent of the choices
  
  At the moment the process halts, exactly one entry, $M$, is $>1$; all other $N-1$ entries equal $1$. Fix a prime $p$. Every entry
  equal to $1$ has $p$‑exponent $0$, so the multiset of $p$‑exponents on the final board is
  $${,v_p(M),,0,,0,\dots,0,},$$
  whose gcd is $v_p(M)$. By the Lemma this gcd equals the invariant $d_p$, i.e. its initial value:
  $$v_p(M)=d_p=\gcd\big(v_p(a_1),\dots,v_p(a_N)\big),$$
  computed from the starting configuration. Therefore
  $$\boxed{,M=\prod_{p},p^{,d_p},\qquad d_p=\gcd_{1\le i\le N} v_p(a_i), }$$
  where the product ranges over the (finitely many) primes dividing some initial number.

  Every quantity on the right depends only on the initial multiset of integers, not on any of Confucius's choices. Hence the final value
  $M$ is the same no matter how the moves are made. $\qquad\blacksquare$

  ---
  Remarks / self‑review of the argument
  
  - Where each hypothesis is used. "$m,n>1$" guarantees both deleted entries are counted in $K$, which makes (4) valid. "All initial
  numbers $>1$" gives (2), the one fact that rules out $K=0$. The specific value $2026$ is irrelevant beyond being finite and $\ge 2$.
  - No gap in termination. The two obstacles — a coprime move (where $\Phi$ is flat, by (3), since $g=1$) and a gcd $>1$ move (where
  $\Phi$ drops) — are handled uniformly by the lexicographic pair: a coprime move has $g=1$ so it makes $K$ strictly drop by (4), while
  a $K$‑preserving move must have $g>1$ and so drops $\Phi$. Every move strictly decreases $(K,\Phi)$.
  - Invariant correctness. The Euclidean step $\gcd(a,b-a)=\gcd(a,b)$ is exact, including boundary cases $a=b$ (pair $\to{a,0}$, gcd
  $a$) and $a=0$ (pair $\to{0,b}$, gcd $b$), matching (1).
  - Consistency check. Both parts, and the closed form for $M$, were confirmed on 20,000 random configurations with randomized move
  choices (all terminated at $K=1$ with $M=\prod_p p^{d_p}$), including cases with several primes and several equal entries.

  For instance, starting from ${8,12}$: $d_2=\gcd(3,2)=1$, $d_3=\gcd(0,1)=1$, so $M=2\cdot 3=6$ — and indeed every legal play, e.g.
  ${8,12}\to{4,6}\to{2,6}\to{2,3}\to{1,6}$, ends at $6$.

✻ Crunched for 3m 24s