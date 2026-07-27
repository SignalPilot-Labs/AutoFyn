Every move strictly decreases the lexicographic pair $(\Omega, C)$, with zero violations. All pieces verified. Here is the complete
  solution.

  ---
  Setup and notation

  For a prime $p$ and positive integer $x$, let $v_p(x)$ denote the exponent of $p$ in the factorization of $x$. Recall the two
  identities
  $$v_p(\gcd(m,n)) = \min(v_p(m),v_p(n)), \qquad v_p(\operatorname{lcm}(m,n)) = \max(v_p(m),v_p(n)).$$

  Consider a single move on two entries $m,n$ (both $>1$), which replaces them with
  $$d := \gcd(m,n) \qquad\text{and}\qquad q := \frac{\operatorname{lcm}(m,n)}{\gcd(m,n)}.$$
  Fix a prime $p$ and write $a = v_p(m),\ b = v_p(n)$. Then
  $$v_p(d) = \min(a,b), \qquad v_p(q) = v_p(\operatorname{lcm}(m,n)) - v_p(\gcd(m,n)) = \max(a,b) - \min(a,b) = |a-b|. \tag{$\star$}$$
  Thus each prime evolves independently, and for that prime a move performs
  $$(a,b)\ \longmapsto\ \big(\min(a,b),\ |a-b|\big),$$
  a subtractive Euclidean step.

  Throughout, let $\Omega(x) = \sum_p v_p(x)$ be the number of prime factors of $x$ counted with multiplicity (so $\Omega(x)=0 \iff
  x=1$).

  ---
  Part (a): The process terminates with exactly one entry $>1$

  Step 1: The process terminates (finitely many moves).

  Assign to any board state the pair
  $$\Phi := \big(\Omega_{\text{tot}},\ C\big) \in \mathbb{Z}{\ge 0}^2, \qquad \Omega{\text{tot}} := \sum_{i}\Omega(x_i), \quad C := #{i
  : x_i > 1}.$$

  Consider one move on $m,n$ (both $>1$), producing $d=\gcd(m,n)$ and $q=\operatorname{lcm}(m,n)/\gcd(m,n)$.

  Effect on $\Omega_{\text{tot}}$. By $(\star)$, for each prime the two exponents change from $a+b$ to $\min(a,b)+|a-b| = \max(a,b)$, a
  change of $-\min(a,b)\le 0$. Summing over all primes, $\Omega_{\text{tot}}$ changes by
  $$-\sum_p \min(v_p(m),v_p(n)) = -,\Omega(\gcd(m,n)) \le 0 .$$
  Hence $\Omega_{\text{tot}}$ never increases, and it strictly decreases iff $\gcd(m,n) > 1$.

  Effect on $C$. Both chosen entries were $>1$.
  - If $\gcd(m,n) = 1$: the new entries are $d = 1$ and $q = mn \ge 4 > 1$. So the number of entries $>1$ drops by exactly $1$: $C$
  strictly decreases. (Here $\Omega(\gcd)=0$, so $\Omega_{\text{tot}}$ is unchanged.)
  - If $\gcd(m,n) > 1$: the new entries are $d>1$ and $q\ge 1$, so at most two of them exceed $1$; thus $C$ decreases by $0$ or $1$. In
  particular $C$ never increases.

  Strict lexicographic descent. Every move strictly decreases $\Phi$ in the lexicographic order:
  - if $\gcd(m,n)>1$, the first coordinate $\Omega_{\text{tot}}$ strictly decreases;
  - if $\gcd(m,n)=1$, the first coordinate is unchanged and the second coordinate $C$ strictly decreases.

  Now suppose, for contradiction, the process ran forever. The integer $\Omega_{\text{tot}}\ge 0$ is non-increasing, so it can strictly
  decrease only finitely often; hence from some point on it is constant. After that point, no move can have $\gcd(m,n)>1$ (such a move
  would decrease $\Omega_{\text{tot}}$), so every subsequent move is coprime and strictly decreases the integer $C\ge 0$. But $C$ cannot
  strictly decrease infinitely often. This contradiction shows the process makes only finitely many moves.

  A move is possible exactly when two entries are both $>1$, i.e. when $C\ge 2$. Therefore at termination $C \le 1$: at most one entry
  exceeds $1$.

  Step 2: An invariant forbids $C=0$.

  For each prime $p$ define
  $$g_p := \gcd_i, v_p(x_i),$$
  the gcd of all $p$-exponents on the board (using $\gcd(0,t)=t$, so entries with $v_p=0$ do not affect it; if all exponents are $0$
  then $g_p=0$).

  Claim: each $g_p$ is invariant under every move. A move alters only the $p$-exponents of the two chosen entries, replacing the pair of
  exponents $(a,b)$ by $(\min(a,b),|a-b|)$. Since (for $a\le b$) $\gcd(\min(a,b),|a-b|) = \gcd(a, b-a) = \gcd(a,b)$, the two exponents
  generate the same subgroup of $\mathbb Z$ before and after. Taking the gcd together with all the other (unchanged) exponents therefore
  gives the same value:
  $$\gcd\Big({v_p(x_k)}{k\ne i,j}\cup{a,b}\Big) = \gcd\Big({v_p(x_k)}{k\ne i,j}\cup{\min(a,b),|a-b|}\Big).$$
  Hence $g_p$ is unchanged. $\square$

  Consequently the quantity
  $$P := \prod_{p} p^{,g_p}$$
  is invariant throughout the entire process. Initially all $2026$ numbers are $>1$, so some prime $p$ divides some entry, giving $v_p
  \ge 1$ for that entry and thus $g_p \ge 1$. Therefore
  $$P \ge p^{1} > 1 \qquad\text{at all times.}$$

  Now examine the terminal state, where $C\le 1$. If $C=0$, every entry equals $1$, so every exponent is $0$, every $g_p=0$, and $P = 1$
  — contradicting $P>1$. Hence $C \ne 0$.

  Combining with Step 1 ($C\le 1$): at termination exactly one entry $M$ is greater than $1$. $\blacksquare$

  ---
  Part (b): The value of $M$ is independent of the choices
  
  At termination, by part (a) there is exactly one entry $M>1$; all other entries equal $1$ and hence have $v_p = 0$ for every prime.
  Therefore, for each prime $p$,
  $$g_p = \gcd\big(v_p(M),,0,0,\dots,0\big) = v_p(M).$$

  But $g_p$ is invariant (proved in Step 2), so it equals its initial value, which is determined solely by the starting board:
  $$v_p(M) = g_p = \gcd_i, v_p\big(x_i^{(0)}\big),$$
  where $x_1^{(0)},\dots,x_{2026}^{(0)}$ are the initial integers. Consequently
  $$\boxed{,M = \prod_{p} p^{,\gcd_i, v_p(x_i^{(0)})},}$$
  depends only on the initial configuration and not on any of Confucius's choices. $\blacksquare$

  ---
  Remarks / sanity checks
  
  - Equivalently, $M$ is the largest integer $g$ such that every initial number is a **perfect $g$-... ** — more precisely, $M=\prod_p
  p^{g_p}$ where $p^{g_p}!\parallel M$ and $g_p$ is the gcd of the $p$-adic valuations; e.g. for the board ${8,12,18}$ the valuations
  are $v_2=(3,2,1),,v_3=(0,1,2)$, giving $g_2=\gcd(3,2,1)=1,\ g_3=\gcd(0,1,2)=1$, so $M=2\cdot 3=6$, matching direct computation.
  - The two monovariants play complementary roles: $\Omega_{\text{tot}}$ (falling on non‑coprime moves) and $C$ (falling on coprime
  moves) together force termination; the family of invariants $g_p$ pins down both that one number survives and which number it is.

  The number $2026$ played no special role beyond being $\ge 2$; the argument holds for any initial count of integers greater than $1$.

✻ Baked for 3m 7s