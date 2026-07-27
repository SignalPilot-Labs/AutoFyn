⏺ Here's a clean writeup of everything I established rigorously, followed by a precise statement of the one gap, with the partial
  progress toward it clearly marked as such.

  Setup

  Let $a_1<a_2<\cdots$ be the sequence, each $a_i>1$. For a positive integer $m$, write $P(m)$ for its set of distinct prime divisors.

  Part A — Fully proven

  Lemma 1 (pairwise non-coprimality). $\gcd(a_i,a_j)>1$ for all $i\ne j$.

  Proof. If $i<j$, then $j-1\ge i$, so the defining condition on $a_j$ (as smallest valid successor of $a_{j-1}$) requires
  $\gcd(a_j,a_i)>1$. $\blacksquare$

  Lemma 2 (bounded gaps). Let $R=\mathrm{rad}(a_1)=\prod_{p\mid a_1}p$. Then $a_{n+1}-a_n\le R$ for every $n\ge1$.

  Proof. Write $P(a_1)={q_1,\dots,q_s}$, so $R=q_1\cdots q_s$. By Lemma 1, every $a_i$ ($i\ge2$) shares a prime with $a_1$, i.e. some
  $q_j\mid a_i$; this is trivially true for $i=1$ too. Let $x$ be the least multiple of $R$ exceeding $a_n$. Since every $q_j\mid R\mid
  x$, for each $i\le n$ we get $\gcd(x,a_i)\ge q_j>1$ for the relevant $q_j\mid a_i$. So $x$ is a legal candidate for $a_{n+1}$, giving
  $a_{n+1}\le x\le a_n+R$. $\blacksquare$

  Domination and the finite-condition reduction. Say $a_i$ dominates $a_j$ if $P(a_i)\subseteq P(a_j)$.

  Lemma 3. If $P(a_i)\subseteq P(a_j)$, then for every integer $x$: $\gcd(x,a_i)>1\Rightarrow\gcd(x,a_j)>1$.

  Proof. A shared prime of $x,a_i$ lies in $P(a_i)\subseteq P(a_j)$, hence divides $a_j$ too. $\blacksquare$

  For $n\ge1$ let $M_n={i\le n: P(a_i)\text{ is minimal (under }\subseteq)\text{ among }{P(a_1),\dots,P(a_n)}}$, and for a finite index
  set $M$ write
  $$\mathrm{Cond}_M(x):\iff \forall i\in M,\ \gcd(x,a_i)>1.$$

  Lemma 4 (reduction). For every $n$ and every $x$: $\mathrm{Cond}{{1,\dots,n}}(x)\iff \mathrm{Cond}{M_n}(x)$. Consequently
  $a_{n+1}=\min{x>a_n:\mathrm{Cond}_{M_n}(x)}$.

  Proof. ($\Rightarrow$) trivial. ($\Leftarrow$) Fix $j\le n$. Among ${k\le n: P(a_k)\subseteq P(a_j)}$ (nonempty, contains $j$), pick
  $i$ with $P(a_i)$ minimal in this subcollection. If some $\ell\le n$ had $P(a_\ell)\subsetneq P(a_i)$, then $P(a_\ell)\subsetneq
  P(a_i)\subseteq P(a_j)$ too, contradicting minimality of $i$ in the subcollection; so $i\in M_n$ and $P(a_i)\subseteq P(a_j)$. By
  Lemma 3, $\gcd(x,a_i)>1\Rightarrow\gcd(x,a_j)>1$. Applying this for every $j\le n$ via its witness $i\in M_n$ proves
  $\mathrm{Cond}{M_n}(x)\Rightarrow \mathrm{Cond}{{1,\dots,n}}(x)$. $\blacksquare$

  Lemma 5. For every $n$ and every $i\ge1$ (not just $i\le n$), $\mathrm{Cond}_{M_n}(a_i)$ holds.

  Proof. For $k\in M_n\subseteq{1,\dots,n}$, Lemma 1 gives $\gcd(a_i,a_k)>1$ whenever $i\ne k$, and trivially when $i=k$. $\blacksquare$

  Lemma 6 (stabilization forces the same rule from step 1). Suppose there is $n^$ with $M_n=M_{n^}=:M$ for all $n\ge n^*$. Then for
  every $n\ge1$ (including $n<n^*$),
  $$a_{n+1}=\min{x>a_n:\mathrm{Cond}_M(x)}.$$

  Proof. Fix $n$. If $n\ge n^$ this is Lemma 4. If $n<n^$: since ${1,\dots,n}\subseteq{1,\dots,n^}$, more constraints only strengthen 
  the condition, so $\mathrm{Cond}M(x)=\mathrm{Cond}{{1,\dots,n^}}(x)\Rightarrow \mathrm{Cond}{{1,\dots,n}}(x)=\mathrm{Cond}{M_n}(x)$
  for every $x$. $(*)$

  By Lemma 5 (applied at $n^*$, with $i=n+1$), $\mathrm{Cond}M(a{n+1})$ holds, so $\min{x>a_n:\mathrm{Cond}M(x)}\le a{n+1}$. $(**)$

  By $()$, every $x$ with $\mathrm{Cond}M(x)$ also has $\mathrm{Cond}{M_n}(x)$, so the minimizer $y:=\min{x>a_n:\mathrm{Cond}M(x)}$ is a
  legal candidate in the original recursive definition, forcing $a{n+1}\le y$. $(**)$

  $()$ and $(*)$ give $y=a_{n+1}$. $\blacksquare$

  Lemma 7 (periodicity of a fixed finite condition). Let $B=\bigcup_{i\in M}P(a_i)$, $L=\prod_{p\in B}p$. Then $\mathrm{Cond}_M(x)$
  depends only on $x\bmod L$. If $T:=#{x\in[a_1,a_1+L): \mathrm{Cond}_M(x)}$, then the greedy walk through $S={x:\mathrm{Cond}M(x)}$ 
  starting at $a_1$ satisfies $a{n+T}=a_n+L$ for all $n\ge1$.

  Proof. Each prime in $P(a_i)\subseteq B$ divides $L$, so divisibility by it is periodic mod $L$; hence $S$ is invariant under
  $x\mapsto x+L$. By Lemma 5, $a_1\in S$. So $S\cap[a_1,a_1+L)$ has exactly $T\ge1$ elements, and by $+L$-invariance
  $S\cap[a_1+kL,a_1+(k+1)L)$ is the shift by $kL$ of that same set for every $k\ge0$. The greedy enumeration of $S$ from $a_1$ therefore
  lists these $T$ elements, then their $+L$ shifts, then $+2L$ shifts, etc., giving exactly $a_{n+T}=a_n+L$ for all $n\ge1$; and by
  Lemma 6 this greedy walk is the original sequence. $\blacksquare$

  Conditional Theorem. If the antichain $M_n$ stabilizes — i.e. $\exists, n^$ with $M_n=M_{n^}$ for all $n\ge n^*$ — then the problem's
  conclusion holds, with $T,L$ as constructed in Lemma 7.

  This chain (Lemmas 1–7) is, to the best of my checking, fully rigorous and requires no unproven input except the stabilization
  hypothesis.

  Part B — The gap: does $M_n$ always stabilize?
  
  This is equivalent to: only finitely many $n$ have $a_n$ not dominated by $M_{n-1}$.

  What I could prove about it (real but insufficient):

  - Let $S_n={x:\mathrm{Cond}{M_n}(x)}$ and $\delta_n$ its density (well-defined by Lemma 7's argument applied to $M_n$). Then 
  $S{n}\subseteq S_{n-1}$ always (more constraints ⇒ smaller set), so $\delta_n$ is non-increasing, and by Lemma 2's construction
  $R\mathbb Z\subseteq S_n$ for all $n$, so $\delta_n\ge 1/R$.
  - $M_n\ne M_{n-1}\iff \delta_n<\delta_{n-1}$ strictly. (Proof of $\Rightarrow$: if $a_n$ isn't dominated, for each $i\in M_{n-1}$ pick
  $p_i\in P(a_i)\setminus P(a_n)$; then $x=\prod p_i$ lies in $S_{n-1}\setminus S_n$.)

  This is a genuine monovariant, but it does not finish the proof: a strictly decreasing sequence of rationals bounded below need not
  stabilize in finitely many steps. I found this obstruction is real, not just theoretical — computing the case
  $a_1=21210=2\cdot3\cdot5\cdot7\cdot101$, the antichain grows to over 120 members of the form ${2,q}$ for distinct large primes $q$
  before finally collapsing (once a term happens to be an exact power of $2$) to $M={2}$, giving the trivial answer $T=1,L=2$. Along the
  way, $\delta_n\to 1/2$ from above but the approach itself took thousands of steps, and I could not rule out — by the density argument
  alone — that such an approach could in principle take infinitely many steps without a hidden reason forcing an exact hit.

  - I also found the actual mechanism that seems to force termination: once "going around" the dominant small-prime pattern requires an
  alternative candidate to be divisible by a fixed product $Q$ of many distinct primes accumulated in non-dominated antichain members,
  achieving that alternative needs $a_n\gtrsim Q$; since $a_n$ grows only linearly (Lemma 2) while $Q$ tends to grow multiplicatively as
  new primes are recruited, the alternative should become permanently unreachable. This is a genuine heuristic and matches everything
  observed computationally, but making "$Q$ grows multiplicatively at a fast enough rate, permanently" into a clean deterministic (not
  density/probabilistic) statement is exactly what I couldn't pin down rigorously — the risk is a scenario where $Q$ stops growing for a
  stretch while $a_n$ catches up, temporarily re-opening an odd/alternative route, and I don't have a proof bounding how many times
  this cat-and-mouse can recur.

  Computational evidence for the conjecture (all consistent with stabilization always occurring): $a_1=15\to(T,L)=(8,30)$;
  $105\to(58,210)$; $143\to(64,858)$; $1001\to(282,2002)$; $35\to(34,210)$; $99\to(72,330)$; all even $a_1$ tested $\to(1,2)$;
  $21210\to(1,2)$ after a large transient. No test case (dozens tried, including adversarial ones) ever failed to stabilize.

  Bottom line

  Lemmas 1–7 give a complete, verified reduction of the whole problem to the single combinatorial finiteness statement in Part B. That
  statement is, as far as I can tell, both true and the genuine crux of the problem's difficulty — and I was not able to prove it to a
  standard I'd stand behind as "verified" within the effort I invested.

  ✻ Churned for 41m 19s