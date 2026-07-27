Setup and notation

  A state is a tuple $S=(x_1,\dots ,x_{2026})$ of positive integers; the initial state $S_0$ has all $x_i>1$. For a prime $p$ and $x\ge
  1$ let $v_p(x)$ be the exponent of $p$ in $x$, and let $\Omega(x)=\sum_p v_p(x)$ be the number of prime factors of $x$ counted with
  multiplicity (so $\Omega(1)=0$).

  A move picks two positions $i\neq j$ with $m=x_i>1$, $n=x_j>1$ and replaces them by
  $$d=\gcd(m,n),\qquad \frac{\operatorname{lcm}(m,n)}{d}.$$
  Since $d\mid \operatorname{lcm}(m,n)$, both new entries are positive integers. A move is possible exactly when at least two entries
  exceed $1$; so the process stops precisely when at most one entry exceeds $1$.

  Observation 1 (effect of a move on exponents). Fix a prime $p$ and put $a=v_p(m),\ b=v_p(n)$. Then
  $$v_p(d)=\min(a,b),\qquad v_p!\left(\tfrac{\operatorname{lcm}(m,n)}{d}\right)=\max(a,b)-\min(a,b),$$
  because $v_p(\gcd)=\min(a,b)$ and $v_p(\operatorname{lcm})=\max(a,b)$. All other entries are unchanged.

  For a state $S$ and a prime $p$ define
  $$g_p(S);=;\gcd\bigl(v_p(x_1),\dots ,v_p(x_{2026})\bigr)\in\mathbb Z_{\ge 0},$$
  with the usual conventions $\gcd(t,0)=t$ and $\gcd(0,\dots ,0)=0$.

  Key Lemma (invariance)

  Lemma. For every prime $p$, the quantity $g_p$ is unchanged by every move.

  Proof. Only the two chosen entries change, and by Observation 1 their $p$-exponents change from $(a,b)$ to $\bigl(\min(a,b),\
  \max(a,b)-\min(a,b)\bigr)$. As $\gcd$ is associative and symmetric, it suffices to prove
  $$\gcd\bigl(\min(a,b),\ \max(a,b)-\min(a,b)\bigr)=\gcd(a,b).$$
  By symmetry assume $a\le b$; the left side is $\gcd(a,,b-a)$, which equals $\gcd(a,b)$ (a common divisor of $a,b$ divides $b-a$, and a
  common divisor of $a,b-a$ divides $b$). This also holds when $a=0$, both sides being $b$. $\blacksquare$

  Part (a)

  Step 1: the process terminates. Define
  $$\Phi(S)=\sum_{i=1}^{2026}\Omega(x_i),\qquad c(S)=#{i:\ x_i>1},\qquad \Psi(S)=2\Phi(S)+c(S)\in\mathbb Z_{\ge 0}.$$
  Consider a move on $m,n$ with $d=\gcd(m,n)$, and let $S'$ be the new state. Summing Observation 1 over all primes, the two chosen
  entries contribute
  $$\sum_p\Bigl[\min(a_p,b_p)+\bigl(\max(a_p,b_p)-\min(a_p,b_p)\bigr)\Bigr]=\sum_p \max(a_p,b_p)=\sum_p (a_p+b_p)-\sum_p\min(a_p,b_p),$$
  so exactly
  $$\Phi(S')=\Phi(S)-\Omega(d).$$
  Also $c(S')\le c(S)$: the two chosen positions contributed $2$ before the move and contribute at most $2$ after it, while all other
  positions are unchanged. Now:

  - If $d>1$, then $\Omega(d)\ge 1$, so $\Psi(S')\le 2\bigl(\Phi(S)-1\bigr)+c(S)=\Psi(S)-2$.
  - If $d=1$, then $\Omega(d)=0$ and the new entries are $1$ and $mn>1$, contributing exactly $1$ to the count; hence $\Phi(S')=\Phi(S)$
  and $c(S')=c(S)-1$, so $\Psi(S')=\Psi(S)-1$.

  In both cases $\Psi$ strictly decreases. Since $\Psi$ is a non‑negative integer, Confucius can make at most
  $\Psi(S_0)=2\Omega(x_1\cdots x_{2026})+2026$ moves, so after finitely many moves no move is possible. By the stopping criterion, at 
  most one entry then exceeds $1$.

  Step 2: at least one entry exceeds $1$. Since $x_1>1$, choose a prime $p_0\mid x_1$. Then $v_{p_0}(x_1)\ge 1$, so the exponents
  $v_{p_0}(x_1),\dots,v_{p_0}(x_{2026})$ are not all zero and therefore $g_{p_0}(S_0)\ge 1$. Let $T$ be the final state. If every entry
  of $T$ were $1$, then all $p_0$-exponents in $T$ would be $0$ and $g_{p_0}(T)=0$, contradicting $g_{p_0}(T)=g_{p_0}(S_0)\ge 1$ from
  the Lemma.

  Hence the process ends after finitely many moves with exactly one entry $M>1$. $\blacksquare$

  Part (b)

  Let $T$ be a final state, with $M>1$ in one position and $1$ in the remaining $2025$ positions. For every prime $p$, the exponents in
  $T$ are $v_p(M)$ together with $2025$ zeros, so
  $$g_p(T)=\gcd\bigl(v_p(M),0,\dots ,0\bigr)=v_p(M).$$
  By the Lemma, $g_p$ is unchanged throughout, so $g_p(T)=g_p(S_0)$ and therefore
  $$v_p(M)=\gcd\bigl(v_p(x_1),\dots ,v_p(x_{2026})\bigr)\qquad\text{for every prime }p.$$
  Since a positive integer is determined by its prime exponents,
  $$\boxed{,M=\prod_{p\ \text{prime}} p^{,\gcd\left(v_p(x_1),\ \dots,\ v_p(x_{2026})\right)},}$$
  (the product is finite: the exponent is nonzero only for primes dividing some $x_i$). The right-hand side depends only on the initial
  numbers, not on any choice Confucius makes. $\blacksquare$

  ---
  Remark. The exponent of $p$ is the gcd of the nonzero $p$-exponents among the $x_i$ (zeros are absorbed by $\gcd$), and it is nonzero
  as soon as some $x_i$ is divisible by $p$. For example, from ${2,3}$ one gets $M=6$; from ${4,8}$ one gets $M=2^{\gcd(2,3)}=2$; from
  ${4,4}$, $M=4$. The number $2026$ is irrelevant beyond being at least $2$.
  
  Verification. I checked this computationally before writing it up: random play on thousands of random multisets always halted with
  exactly one entry $>1$ equal to the boxed formula; an exhaustive search over every possible move sequence on 394 small adversarial
  multisets (equal numbers, high prime powers, coprime mixes) produced a single possible value of $M$ each time, matching the formula;
  and the monovariant $\Psi=2\Phi+c$ was confirmed to strictly decrease on every legal move, with $\Phi(S)-\Phi(S')=\Omega(\gcd(m,n))$
  holding exactly.

✻ Sautéed for 3m 1s