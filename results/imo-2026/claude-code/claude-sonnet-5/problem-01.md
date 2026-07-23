Solution

  Setup and notation. For a prime $p$ and a positive integer $a$, write $v_p(a)$ for the exponent of $p$ in $a$ (the $p$-adic valuation), and $\Omega(a)=\sum_p v_p(a)$ for the number of prime factors of $a$ counted with
  multiplicity (so $\Omega(1)=0$). Recall the standard facts
  $$v_p(\gcd(m,n))=\min(v_p(m),v_p(n)),\qquad v_p(\operatorname{lcm}(m,n))=\max(v_p(m),v_p(n))$$
  for every prime $p$. Since gcd and lcm only involve primes already dividing $m$ or $n$, no move ever introduces a new prime: throughout the whole process every number on the board is supported on the finite set of primes
  dividing the original $2026$ numbers.

  Let $a_1,\dots,a_{2026}$ denote the numbers currently on the board (positions are fixed labels $1,\dots,2026$, even though the values change). A move chooses two positions $i\ne j$ with $a_i,a_j>1$, sets $g=\gcd(a_i,a_j)$,
  $h=\operatorname{lcm}(a_i,a_j)/g$, and replaces $(a_i,a_j)$ by $(g,h)$.

  ---
  Lemma 1 (Euclidean subtraction identity)
  
  For nonnegative integers $a,b$,
  $$\gcd(a,b)=\gcd\big(\min(a,b),,|a-b|\big).$$

  Proof. WLOG $a\ge b$. The right side is $\gcd(b,a-b)$. This equals $\gcd(a,b)$ by the standard Euclidean identity $\gcd(a,b)=\gcd(b,a-b)$ (valid also when $b=0$, since both sides equal $a$). $\blacksquare$

  Lemma 2 (Per‑prime effect of a move)

  Fix a prime $p$ and a move on positions $i,j$ with values $m=a_i,n=a_j$, producing $g,h$ as above. Then
  $$v_p(g)=\min(v_p(m),v_p(n)),\qquad v_p(h)=|v_p(m)-v_p(n)|.$$

  Proof. Immediate from $v_p(g)=\min(v_p(m),v_p(n))$, $v_p(\operatorname{lcm}(m,n))=\max(v_p(m),v_p(n))$, and $v_p(h)=v_p(\operatorname{lcm}(m,n))-v_p(g)=\max-\min=|v_p(m)-v_p(n)|$. $\blacksquare$

  Lemma 3 (Key invariant)

  For every prime $p$, the quantity
  $$G_p:=\gcd\big(v_p(a_1),\dots,v_p(a_{2026})\big)$$
  (using the convention $\gcd(x,0)=x$) is unchanged by every move.

  Proof. A move alters only $v_p(a_i),v_p(a_j)$ (for the two chosen positions), replacing the pair $(c,c')=(v_p(m),v_p(n))$ by $(\min(c,c'),|c-c'|)$, by Lemma 2. By Lemma 1, $\gcd(c,c')=\gcd(\min(c,c'),|c-c'|)$. Since gcd of a
  multiset can be computed by first taking the gcd of any two chosen entries and then combining with the rest (associativity/commutativity of $\gcd$),
  $$\gcd(v_p(a_1),\dots,v_p(a_{2026})) = \gcd\Big(\gcd(v_p(a_i),v_p(a_j)),\ {v_p(a_l)}_{l\ne i,j}\Big),$$
  and the inner gcd is unchanged by the move while the other entries are untouched. Hence $G_p$ is invariant. $\blacksquare$

  Note $G_p$ is computed from the original numbers only, since it's invariant from the start.

  Lemma 4 (Effect of a move on $\Omega$-sum and count)

  Let $T=\sum_{i=1}^{2026}\Omega(a_i)$ and $k=#{i:a_i>1}$. Consider a move on $m=a_i,n=a_j$ with $g=\gcd(m,n)$.

  1. $T$ decreases by exactly $\Omega(g)\ge 0$.
  2. $k$ never increases.
  3. If $g=1$, then $T$ is unchanged and $k$ strictly decreases (by exactly $1$).

  Proof. (1) Using Lemma 2, summing over all primes $p$:
  $$\Omega(g)+\Omega(h)=\sum_p\big(\min(v_p(m),v_p(n))+|v_p(m)-v_p(n)|\big)=\sum_p\max(v_p(m),v_p(n)),$$
  while $\Omega(m)+\Omega(n)=\sum_p\big(\max(v_p(m),v_p(n))+\min(v_p(m),v_p(n))\big)$. Subtracting,
  $$\big(\Omega(m)+\Omega(n)\big)-\big(\Omega(g)+\Omega(h)\big)=\sum_p\min(v_p(m),v_p(n))=\Omega(g).$$
  So $T$ decreases by exactly $\Omega(g)$; in particular $T$ is non-increasing.

  (2) The move touches only positions $i,j$; before the move both count toward $k$ (as $m,n>1$), and after, only $g,h$ can count. So the contribution of these two positions to $k$ cannot increase, hence $k$ is non-increasing.

  (3) If $g=1$: since $m,n>1$ are coprime, $h=mn>1$. So the pair $(m,n)$, both $>1$, becomes $(g,h)=(1,mn)$, of which exactly one ($mn$) exceeds $1$. Thus $k$ drops by exactly $1$. Also $\Omega(g)=\Omega(1)=0$, so by part (1),
  $T$ is unchanged. $\blacksquare$

  ---
  Part (a): The process terminates with exactly one number $>1$

  Termination. By Lemma 4, each move either:
  - (Case A) has $g>1$, so $\Omega(g)\ge 1$ and $T$ strictly decreases; or
  - (Case B) has $g=1$, so $T$ is unchanged but $k$ strictly decreases by $1$.

  Let $T_0=\sum_i \Omega(a_i)$ be the initial value of $T$ (a fixed finite number depending only on the initial board) and $k_0=2026$. Since $T\ge 0$ always and only decreases (by at least $1$) in Case A moves, there are at most 
  $T_0$ Case‑A moves in total. Since $k\ge 0$ always and only decreases (by exactly $1$) in Case B moves, there are at most $k_0=2026$ Case‑B moves in total. Hence the total number of moves is at most $T_0+2026$, a finite number.
  So Confucius can make only finitely many moves, regardless of his choices.

  The process stops exactly when at most one number exceeds 1. A move requires two positions with value $>1$; conversely, if two such positions exist, a legal move is available (any two positions with values $>1$ may be chosen,
  whether or not the values coincide). So the process halts precisely when $k\le 1$; since only finitely many moves are possible, some state with $k\le 1$ is reached.

  Ruling out $k=0$. Since each $a_i>1$ initially, some prime $p_0$ divides $a_1$, so $v_{p_0}(a_1)\ge 1$; hence the initial multiset of valuations ${v_{p_0}(a_1),\dots,v_{p_0}(a_{2026})}$ contains a positive entry, so $G_{p_0}\ge
  1$. By Lemma 3, $G_{p_0}$ stays $\ge 1$ forever. If the terminal state had $k=0$ (all numbers equal to $1$), then all valuations $v_{p_0}(a_i)$ would be $0$, forcing $G_{p_0}=\gcd(0,\dots,0)=0$ — contradicting $G_{p_0}\ge1$.

  Hence the terminal state has $k=1$: after finitely many moves, exactly one number $M>1$ remains on the board, proving part (a). $\blacksquare$

  ---
  Part (b): $M$ is independent of Confucius's choices
  
  At the terminal state, position (say) $i^*$ holds $M>1$ and every other position holds $1$. Fix any prime $p$ dividing $M$ (the argument below works the same, trivially, if $p\nmid M$, giving $0=0$). At the terminal state the
  valuations are
  $$v_p(a_{i^*}) = v_p(M), \qquad v_p(a_l)=0 \text{ for all } l\ne i^*,$$
  so
  $$G_p ;=; \gcd\big(v_p(M),0,0,\dots,0\big) ;=; v_p(M).$$

  But by Lemma 3, $G_p$ equals its initial value $\gcd\big(v_p(a_1^{(0)}),\dots,v_p(a_{2026}^{(0)})\big)$, computed from the original numbers on the board — a quantity that does not depend on any move Confucius made. Therefore,
  for every prime $p$,
  $$v_p(M) ;=; \gcd\Big(v_p(a_1^{(0)}),\dots,v_p(a_{2026}^{(0)})\Big),$$
  which determines $M$ completely:
  $$\boxed{M=\prod_{p}; p^{,\gcd\left(v_p(a_1^{(0)}),,\dots,,v_p(a_{2026}^{(0)})\right)}}$$
  the product over all primes $p$ dividing at least one of the original numbers $a_1^{(0)},\dots,a_{2026}^{(0)}$.

  Since the right-hand side depends only on the initial numbers on the blackboard and not on the sequence of moves chosen, $M$ is the same for every valid play of Confucius. $\blacksquare$

  ---
  Remarks (consistency checks)
  
  - This formula also independently re-confirms $M>1$: since some prime $p_0$ divides some $a_i^{(0)}$, the exponent $\gcd(v_{p_0}(a_1^{(0)}),\dots)\ge 1$ (gcd of nonnegative integers not all zero is positive), so $M\ge p_0>1$.
  - Small hand-check: board ${4,6,9}$ (analogous smaller version). Here $\gcd(v_2(4),v_2(6),v_2(9))=\gcd(2,1,0)=1$ and $\gcd(v_3(4),v_3(6),v_3(9))=\gcd(0,1,2)=1$, predicting $M=2\cdot3=6$. Simulating two different move orders —
  $(4,6)\to(2,6)$, then $(6,9)\to(3,6)$, then $(2,3)\to(1,6)$, then $(6,6)\to(6,1)$; versus $(4,9)\to(1,36)$, then $(6,36)\to(6,6)$, then $(6,6)\to(6,1)$ — both terminate at $M=6$, matching the formula and confirming
  path-independence.

✻ Churned for 3m 26s