time 5 min

## Solution

**Setup and notation.** Think of the board as $2026$ fixed *slots* $1,2,\dots ,2026$; let $b_i$ denote the number currently sitting in slot $i$, so initially $b_i=a_i>1$. A move chooses slots $i\ne j$ with $b_i,b_j>1$ and replaces $(b_i,b_j)$ by
$$\big(d,\ell\big):=\Big(\gcd(b_i,b_j),\ \tfrac{\operatorname{lcm}(b_i,b_j)}{\gcd(b_i,b_j)}\Big),$$
leaving all other slots untouched. Since $\gcd,\operatorname{lcm}/\gcd$ of positive integers are positive integers, every entry on the board stays a positive integer forever.

For a prime $p$ and integer $n\ge1$, let $v_p(n)$ be the exponent of $p$ in $n$, and $\Omega(n)=\sum_p v_p(n)$ the number of prime factors of $n$ with multiplicity ($\Omega(1)=0$).

### Step 1. How a move acts on exponents

If a move combines $m=b_i,n=b_j$ into $d,\ell$ as above, then for **every** prime $p$,
$$v_p(d)=\min(v_p(m),v_p(n)),\qquad v_p(\ell)=v_p(\operatorname{lcm}(m,n))-v_p(\gcd(m,n))=|v_p(m)-v_p(n)|.$$

So: *for each prime $p$ separately*, a move at slots $i,j$ replaces the pair of exponents $(x,y)$ by $(\min(x,y),|x-y|)$, leaving all other slots' exponents unchanged.

### Step 2. A prime-by-prime invariant

For nonnegative integers $x_1,\dots,x_{2026}$ let $c(x_1,\dots,x_{2026})$ denote their gcd, with the convention $c(0,\dots,0)=0$.

**Claim.** For each prime $p$, the quantity $G_p:=c(v_p(b_1),\dots,v_p(b_{2026}))$ never changes.

*Proof.* Fix $p$; consider a move at slots $i\neq j$ turning $(x,y)$ into $(x',y')=(\min(x,y),|x-y|)$, with all other exponents fixed. It suffices to show
$$\{\text{common divisors of }x,y\}=\{\text{common divisors of }x',y'\}. \qquad(\ast)$$
Then the full set of common divisors of the $2026$ exponents (the intersection of the common divisors of the $2024$ untouched entries with those of $\{x,y\}$, resp. $\{x',y'\}$) is unchanged, hence so is its maximum $G_p$ (with the convention above).

For $(\ast)$: WLOG $x\ge y$, so $x'=y,\ y'=x-y$. If $c\mid x,c\mid y$ then $c\mid y=x'$ and $c\mid x-y=y'$. Conversely if $c\mid x'=y$ and $c\mid y'=x-y$, then $c\mid y$ and $c\mid (x-y)+y=x$. $\blacksquare$

Consequently, since $G_p$ never changes, at all times
$$G_p=\gcd\big(v_p(a_1),\dots,v_p(a_{2026})\big).$$
If $p$ divides some $a_i$, then not all of $v_p(a_1),\dots,v_p(a_{2026})$ are $0$, so $G_p\ge 1$ **always**.

### Step 3. Termination after finitely many moves, however Confucius plays

Let $\Phi:=\sum_i\Omega(b_i)\ge0$ and $k:=\#\{i:b_i>1\}\in\{0,\dots,2026\}$ describe the current board, and set
$$N:=2027\Phi+k\ \ (\ge 0).$$

Consider a move combining $m,n>1$ into $d=\gcd(m,n),\ \ell=\operatorname{lcm}(m,n)/\gcd(m,n)$.

**Change in $\Phi$.** By Step 1, for each prime $p$ the exponent sum at the two touched slots drops from $x+y$ to $\max(x,y)$, a loss of $\min(x,y)$. Summing over $p$: $\Phi$ decreases by exactly $\sum_p\min(v_p(m),v_p(n))=\Omega(d)$.

**Change in $k$.** Write $m=da,\ n=db$ with $\gcd(a,b)=1$; then $\ell=\operatorname{lcm}(m,n)/d=ab$.
- $\ell=1\iff a=b=1\iff m=n=d$.
- If $m\ne n$ then $(a,b)\ne(1,1)$, so $ab>1$, i.e. $\ell>1$ always when $m\ne n$.

Three exhaustive cases:

1. **$m=n$:** $d=m>1,\ \ell=1$. Both slots were $>1$; now one becomes $1$: $k$ drops by $1$. Also $\Omega(d)=\Omega(m)\ge1$.
2. **$m\ne n,\ \gcd(m,n)=1$:** $d=1,\ \ell=mn>1$: $k$ drops by $1$, and $\Omega(d)=0$.
3. **$m\ne n,\ \gcd(m,n)=d>1$:** then $\ell>1$ too, so both slots remain $>1$: $k$ unchanged, but $\Omega(d)\ge1$.

Hence:
- Case 1: $\Delta N=2027(-\Omega(d))+(-1)\le -2028<0$.
- Case 2: $\Delta N=0+(-1)=-1<0$.
- Case 3: $\Delta N=2027(-\Omega(d))+0\le -2027<0$.

So **every** move strictly decreases the nonnegative integer $N$ by at least $1$. Since $N$ starts at the fixed finite value $N_0=2027\Phi_0+k_0$ determined only by $a_1,\dots,a_{2026}$, Confucius can make at most $N_0$ moves no matter how he plays. In particular the process always halts after finitely many moves.

### Step 4. The process must stop with $k=1$: proof of (a)

A move is possible exactly when $k\ge2$. By Step 3 the process, for **any** sequence of choices, reaches a state with $k\le1$ after finitely many moves.

**$k=0$ is impossible:** if all $b_i=1$ at some point, then for every prime $p$ all exponents vanish there, so $G_p=0$ at that moment. But choosing $p_0$ any prime factor of $a_1$ (which exists as $a_1>1$), Step 2 gives $G_{p_0}\ge1$ always — a contradiction.

Hence the process always terminates with **exactly $k=1$**: a single number $M>1$ remains, all other $2025$ entries equal $1$. This proves **part (a)**.

### Step 5. $M$ depends only on the initial numbers: proof of (b)

Suppose termination occurs with $b_{i_0}=M>1$ and $b_i=1$ for $i\ne i_0$. For a prime $p$, the terminal exponent list has a single possibly-nonzero entry, $v_p(M)$, at slot $i_0$, and zeros elsewhere; its gcd is exactly $v_p(M)$ (this holds under our convention even if $v_p(M)=0$). By the Claim of Step 2,
$$v_p(M)=G_p=\gcd\big(v_p(a_1),\dots,v_p(a_{2026})\big)\qquad\text{for every prime }p.$$

The right-hand side depends only on the original numbers $a_1,\dots,a_{2026}$, not on any move Confucius made. Therefore
$$M=\prod_{p}p^{\,\gcd\left(v_p(a_1),\dots,v_p(a_{2026})\right)}$$
is completely determined by the initial board. This proves **part (b)**. $\blacksquare$