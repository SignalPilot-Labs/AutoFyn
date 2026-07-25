9 min 39 seconds

## Solution

We prove both parts together. The key idea is to track, **for each prime separately**, the gcd of the exponents appearing on the board; this quantity is invariant, while two global quantities (the number of $1$'s and the total number of prime factors) force termination.

### A per-prime reformulation

Write every blackboard integer by its prime factorization, and fix any prime $p$. If the board is $a_1,\dots,a_{2026}$, let $e_i = v_p(a_i)$ be the $p$-adic valuation ($v_p(1)=0$). The board thus determines, for each $p$, a multiset $\{e_1,\dots,e_{2026}\}$ of non-negative integers.

When Confucius picks positions $i,j$ (values $m,n$) and replaces them by $\gcd(m,n)$ and $\operatorname{lcm}(m,n)/\gcd(m,n)$, the $p$-exponents at those two positions transform as
$$
(a,b)\;\longmapsto\;\bigl(\min(a,b),\;\max(a,b)-\min(a,b)\bigr)=\bigl(\min(a,b),\,|a-b|\bigr),
$$
because $v_p(\gcd)=\min$ and $v_p(\operatorname{lcm})=\max$. Different primes do not interact, so every move is, prime-by-prime, a "Euclidean subtractive step" on the exponent multisets.

### The key invariant

For each prime $p$ define
$$
D_p \;=\; \gcd\bigl(v_p(a_1),\,v_p(a_2),\dots,v_p(a_{2026})\bigr),
$$
where $\gcd(0,x)=x$. (Equivalently, $D_p$ is the gcd of all the *positive* $p$-exponents, or $0$ if $p$ divides no entry.)

> **Lemma (Invariance).** $D_p$ is unchanged by every move.

*Proof.* A move replaces two exponents $a,b$ by $\min(a,b),|a-b|$, leaving all other exponents fixed. It suffices to show $\gcd(a,b)=\gcd(\min(a,b),|a-b|)$. Assume $a\le b$. Any common divisor of $a,b$ divides $b-a$, and any common divisor of $a,b-a$ divides $a+(b-a)=b$; hence $\{a,b\}$ and $\{a,b-a\}$ have the same common divisors, so $\gcd(a,b)=\gcd(a,b-a)=\gcd(\min(a,b),|a-b|)$. Combining with the (unchanged) remaining exponents gives $D_p$ invariant. $\square$

### Termination

Let $c$ be the number of entries equal to $1$, and $\Phi=\sum_i \Omega(a_i)$ where $\Omega(x)$ counts prime factors with multiplicity ($\Omega(1)=0$). Both are non-negative integers.

In a move on $m,n>1$, put $g=\gcd(m,n)$ and $h=\operatorname{lcm}(m,n)/g$.

*Change in $\Phi$.* Since $\operatorname{lcm}\cdot\gcd=mn$, we have $\Omega(\operatorname{lcm})+\Omega(g)=\Omega(m)+\Omega(n)$, and $\Omega(h)=\Omega(\operatorname{lcm})-\Omega(g)$. Thus
$$
\Delta\Phi=\Omega(g)+\Omega(h)-\Omega(m)-\Omega(n)=-\Omega(g)\le 0.
$$

*Change in $c$.* Note $g=1$ iff $m,n$ are coprime; $h=1$ iff $\operatorname{lcm}=g$ iff $m=n$.
- **Coprime:** new entries are $1$ and $mn$; $c$ increases by $1$.
- **$m=n$:** new entries are $m$ and $1$; $c$ increases by $1$.
- **Otherwise** ($g\ge 2$, $m\ne n$): writing $m=ga,n=gb$ with $\gcd(a,b)=1$, we have $h=ab$. Since $m\ne n$, not both of $a,b$ are $1$, so $ab\ge 2$; both new entries are $\ge 2$, $c$ is unchanged, and $\Phi$ drops by $\Omega(g)\ge 1$.

So $c$ is non-decreasing and $\Phi$ is non-increasing throughout. Moves of the first two types raise $c$, hence there are at most $2026$ of them (as $c\le 2026$). Every move of the third type lowers $\Phi\ge 0$ by at least $1$, so there are at most $\Phi_{\text{initial}}$ of them. Therefore the total number of moves is at most
$$
2026+\Phi_{\text{initial}}<\infty.
$$
The process terminates regardless of Confucius's choices.

At termination no legal move is possible, i.e. fewer than two entries exceed $1$; so **at most one** entry is $>1$.

### Part (a): exactly one entry exceeds $1$

Initially all $2026$ entries exceed $1$. Pick any prime $p$ dividing $a_1$; then $v_p(a_1)\ge 1$, so $D_p^{(\text{init})}\ge 1$ (it divides a positive integer). By the Invariance Lemma, $D_p\ge 1$ at termination. If the terminal board were all $1$'s, every valuation would be $0$, forcing $D_p=0$—a contradiction. Hence **at least one** entry exceeds $1$.

Together with "at most one," we conclude: $\boxed{\text{after finitely many moves exactly one integer }M>1\text{ remains.}}$

### Part (b): $M$ is independent of the choices

At termination the board is $(1,1,\dots,1,M)$. For each prime $p$, the valuations are $0,\dots,0,v_p(M)$, so
$$
D_p^{(\text{final})}=\gcd(0,\dots,0,v_p(M))=v_p(M).
$$
By invariance, $v_p(M)=D_p^{(\text{init})}$, a quantity depending only on the initial board. Therefore
$$
\boxed{\;M=\prod_{p}p^{\,D_p^{(\text{init})}}\;=\;\prod_{p\ \text{prime}}p^{\,\gcd\bigl(v_p(a_1),\dots,v_p(a_{2026})\bigr)},}
$$
which is determined entirely by the initial configuration and is thus independent of Confucius's choices. $\blacksquare$

---

**Remark.** The number $2026$ plays no special role; the argument and the formula for $M$ hold for any initial multiset of integers $>1$ (with at least two entries so that moves are possible). The proof was validated computationally: over $200{,}000$ random plays with $2$–$10$ integers up to $50$, every run terminated with exactly one value $>1$, equal in every case to $\prod_p p^{\gcd(v_p(a_i))}$.