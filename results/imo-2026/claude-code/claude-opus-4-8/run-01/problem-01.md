
Cooked for 6m 32s
⏺ Solution

  Throughout, for a positive integer $x$ and prime $p$, write $v_p(x)$ for the exponent of $p$ in $x$, and let
  $\Omega(x)=\sum_p v_p(x)$ be the number of prime factors of $x$ counted with multiplicity (so $\Omega(1)=0$).

  At every moment the blackboard holds $2026$ positive integers $x_1,\dots,x_{2026}$. A move picks two positions
  $i\ne j$ with $x_i=m>1$ and $x_j=n>1$ and replaces them by
  $$
  g=\gcd(m,n),\qquad h=\frac{\operatorname{lcm}(m,n)}{\gcd(m,n)} .
  $$
  For every prime $p$, writing $a=v_p(m),\ b=v_p(n)$,
  $$
  v_p(g)=\min(a,b),\qquad v_p(h)=\max(a,b)-\min(a,b)=|a-b|. \tag{$\ast$}
  $$

  A move is available exactly when at least two board entries exceed $1$. Let
  $$
  N=#{,i:x_i>1,}.
  $$
  So Confucius can move iff $N\ge 2$, and he stops precisely when $N\le 1$.

  ---
  Lemma 1 (a per‑prime invariant)

  For each prime $p$ let
  $$
  D_p=\gcd\bigl(v_p(x_1),\dots,v_p(x_{2026})\bigr),
  $$
  the gcd of all $2026$ exponents of $p$ (with the convention $\gcd(\cdot,0)$ ignores the $0$, and the gcd of all
  zeros is $0$). Then $D_p$ is unchanged by every move.

  Proof. A move alters only the two exponents $a=v_p(m)$ and $b=v_p(n)$, replacing them by $\min(a,b)$ and
  $|a-b|$ by $(\ast)$. The Euclidean identity gives
  $$
  \gcd\bigl(\min(a,b),,|a-b|\bigr)=\gcd(a,b).
  $$
  Since the gcd of the whole list equals $\gcd$ of "the untouched entries" together with $\gcd$ of the two
  touched entries, and the latter is preserved, $D_p$ is preserved. $\qquad\blacksquare$

  Define the integer
  $$
  M^*=\prod_p p^{,D_p}.
  $$
  Only primes dividing some board entry have $D_p>0$, so this product is finite; by Lemma 1 $M^*$ never changes 
  during the whole process. Moreover $M^*>1$ initially: every initial entry exceeds $1$, so some prime $p$
  divides some entry, whence $v_p(x_i)\ge1$ for that $i$, giving $D_p\ge1$ and $M^*\ge p>1$. Being invariant,
  $M^*>1$ at all times.

  ---
  Lemma 2 (the process terminates)
  
  Let $\Phi=\sum_{i}\Omega(x_i)$. Then the nonnegative integer quantity
  $$
  \Psi=\Phi+N
  $$
  strictly decreases at every move. Hence only finitely many moves occur.

  Proof. Consider one move on $m,n>1$, producing $g,h$. Using additivity of $\Omega$ and $(\ast)$:
  $$
  \Omega(g)+\Omega(h)=\sum_p\Bigl(\min(a,b)+|a-b|\Bigr)=\sum_p\max(a,b),
  $$
  $$
  \Omega(m)+\Omega(n)=\sum_p\bigl(a+b\bigr)=\sum_p\bigl(\max(a,b)+\min(a,b)\bigr),
  $$
  so
  $$
  \Delta\Phi=\Omega(g)+\Omega(h)-\Omega(m)-\Omega(n)=-\sum_p\min(a,b)=-,\Omega(g).
  $$

  Case $\gcd(m,n)=1$. Then $g=1,\ h=mn>1$, so $\Delta\Phi=-\Omega(g)=0$. The two positions, both $>1$ before,
  become one entry $=1$ and one entry $mn>1$, so $\Delta N=-1$. Thus $\Delta\Psi=-1$.

  Case $\gcd(m,n)>1$. Then $\Omega(g)\ge1$, so $\Delta\Phi=-\Omega(g)\le-1$. The two chosen positions were $>1$;
  afterwards $g>1$ and $h\ge1$, so the count of entries $>1$ among them is $2$ or $1$, giving $\Delta
  N\in{-1,0}$. Thus $\Delta\Psi\le-1$.

  In both cases $\Psi$ drops by at least $1$. As $\Psi\ge0$ is an integer, at most $\Psi_{\text{initial}}$ moves
  can occur. $\qquad\blacksquare$

  ---
  Part (a)

  By Lemma 2 the process ends after finitely many moves, and it can only end with $N\le1$.

  Suppose $N=0$, i.e. every entry equals $1$. Then $v_p(x_i)=0$ for all $i,p$, so every $D_p=0$ and $M^*=\prod_p
  p^{0}=1$. This contradicts $M^*>1$ (established after Lemma 1). Hence $N\ne0$, so $N=1$.

  Therefore, regardless of Confucius's choices, the process terminates with exactly one entry $M>1$ (and all
  other entries equal to $1$). $\qquad\blacksquare$

  ---
  Part (b)

  At termination $N=1$: one entry equals $M>1$ and the other $2025$ entries equal $1$. For each prime $p$, the
  exponents on the board are $v_p(M)$ together with $2025$ zeros, so
  $$
  D_p=\gcd\bigl(v_p(M),0,\dots,0\bigr)=v_p(M).
  $$
  Hence
  $$
  M=\prod_p p^{,v_p(M)}=\prod_p p^{,D_p}=M^*.
  $$

  By Lemma 1, each $D_p$ equals the gcd of the exponents of $p$ in the initial $2026  after Lemma 1). Hence $N\ne0$, so $N=1$.


  Suppose $N=0$, i.e. every entry equals $1$. Then $v_p(x_i)=0$ for all $i,p$, so every $D_p=0$ and $M^*=\prod_p
  p^{0}=1$. This contradicts $M^*>1$ (established after Lemma 1). Hence $N\ne0$, so $N=1$.


  Suppose $N=0$, i.e. every entry equals $1$. Then $v_p(x_i)=0$ for all $i,p$, so every $D_p=0$ and $M^*=\prod_p
  p^{0}=1$. This contradicts $M^*>1$ (established after Lemma 1). Hence $N\ne0$, so $N=1$.

  Therefore, regardless of Confucius's choices, the process terminates with exactly one entry $M>1$ (and all
  other entries equal to $1$). $\qquad\blacksquare$

  ---
  Part (b)

  At termination $N=1$: one entry equals $M>1$ and the other $2025$ entries equal $1$. For each prime $p$, the
  exponents on the board are $v_p(M)$ together with $2025$ zeros, so
  $$
  D_p=\gcd\bigl(v_p(M),0,\dots,0\bigr)=v_p(M).
  $$
  Hence
  $$
  M=\prod_p p^{,v_p(M)}=\prod_p p^{,D_p}=M^*.
  $$

  By Lemma 1, each $D_p$ equals the gcd of the exponents of $p$ in the initial $2026  $$
  Hence
  $$
  M=\prod_p p^{,v_p(M)}=\prod_p p^{,D_p}=M^*.
  $$

  By Lemma 1, each $D_p$ equals the gcd of the exponents of $p$ in the initial $2026$                                                                                  numbers,                                                                            which                                                                               depends
  only on the starting configuration and not on any of Confucius's choices. Therefore
  $$
  \boxed{,M=\prod_p p^{,\gcd_i v_p(x_i^{(0)})},}
  $$
  is completely determined by the initial board, independent of how the moves are made.                                                                                $\qquad\blacksquare$

  ---
  after Lemma 1). Hence $N\ne0$, so $N=1$.


  Suppose $N=0$, i.e. every entry equals $1$. Then $v_p(x_i)=0$ for all $i,p$, so every $D_p=0$ and $M^*=\prod_p
  p^{0}=1$. This contradicts $M^*>1$ (established after Lemma 1). Hence $N\ne0$, so $N=1$.

  Therefore, regardless of Confucius's choices, the process terminates with exactly one entry $M>1$ (and all
  other entries equal to $1$). $\qquad\blacksquare$

  ---
  Part (b)

  At termination $N=1$: one entry equals $M>1$ and the other $2025$ entries equal $1$. For each prime $p$, the
  exponents on the board are $v_p(M)$ together with $2025$ zeros, so
  $$
  D_p=\gcd\bigl(v_p(M),0,\dots,0\bigr)=v_p(M).
  $$
  Hence
  $$
  M=\prod_p p^{,v_p(M)}=\prod_p p^{,D_p}=M^*.
  $$

  By Lemma 1, each $D_p$ equals the gcd of the exponents of $p$ in the initial $2026  $$
  Hence
  $$
  M=\prod_p p^{,v_p(M)}=\prod_p p^{,D_p}=M^*.
  $$

  By Lemma 1, each $D_p$ equals the gcd of the exponents of $p$ in the initial $2026$                                                                                  numbers,                                                                            which                                                                               depends
  only on the starting configuration and not on any of Confucius's choices. Therefore
  $$
  \boxed{,M=\prod_p p^{,\gcd_i v_p(x_i^{(0)})},}
  $$
  is completely determined by the initial board, independent of how the moves are made.                                                                                $\qquad\blacksquare$

  ---
  after Lemma 1). Hence $N\ne0$, so $N=1$.


  Suppose $N=0$, i.e. every entry equals $1$. Then $v_p(x_i)=0$ for all $i,p$, so every $D_p=0$ and $M^*=\prod_p
  p^{0}=1$. This contradicts $M^*>1$ (established after Lemma 1). Hence $N\ne0$, so $N=1$.

  Therefore, regardless of Confucius's choices, the process terminates with exactly one entry $M>1$ (and all
  other entries equal to $1$). $\qquad\blacksquare$

  ---
  Part (b)

  At termination $N=1$: one entry equals $M>1$ and the other $2025$ entries equal $1$. For each prime $p$, the
  exponents on the board are $v_p(M)$ together with $2025$ zeros, so
  $$
  D_p=\gcd\bigl(v_p(M),0,\dots,0\bigr)=v_p(M).
  $$
  Hence
  $$
  M=\prod_p p^{,v_p(M)}=\prod_p p^{,D_p}=M^*.
  $$

  By Lemma 1, each $D_p$ equals the gcd of the exponents of $p$ in the initial $2026$ numbers, which depends only
  on the starting configuration and not on any of Confucius's choices. Therefore
  $$
  \boxed{,M=\prod_p p^{,\gcd_i v_p(x_i^{(0)})},}
  $$
  is completely determined by the initial board, independent of how the moves are made. $\qquad\blacksquare$

  ---
  Remark / sanity checks

  - ${2,3}$: $D_2=\gcd(1,0)=1,\ D_3=\gcd(0,1)=1$, so $M=6$. Indeed ${2,3}\to{1,6}$.
  - ${4,6}={2^2,,2\cdot3}$: $D_2=\gcd(2,1)=1,\ D_3=\gcd(0,1)=1$, so $M=6$. Indeed
  ${4,6}\to{2,6}\to{2,3}\to{1,6}$.
  - ${4,4}$: $D_2=\gcd(2,2)=2$, so $M=4$. Indeed ${4,4}\to{4,1}$.

  The heart of the solution is the observation $(\ast)$: prime‑by‑prime, a move sends an exponent pair $(a,b)$ to
  $(\min(a,b),|a-b|)$ — a subtractive Euclidean step — which preserves $\gcd(a,b)$ and hence the gcd $D_p$ of
  all exponents of $p$. The surviving number $M$ is exactly $\prod_p p^{D_p}$.

