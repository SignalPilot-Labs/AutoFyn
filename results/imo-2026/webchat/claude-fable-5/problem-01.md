## Solution

**Setup and notation.** Regard the board as a tuple $C=(c_1,\dots,c_{2026})$ of positive integers; initially every $c_i\ge 2$. A move picks positions $i\ne j$ with $c_i=m>1$ and $c_j=n>1$ and replaces them by $\gcd(m,n)$ and $\operatorname{lcm}(m,n)/\gcd(m,n)$ (an integer, since $\gcd(m,n)\mid\operatorname{lcm}(m,n)$). All entries stay positive integers, and the number of entries stays $2026$.

For a prime $p$ let $v_p(x)$ denote the exponent of $p$ in $x$. Since $v_p(\gcd(m,n))=\min(a,b)$ and $v_p(\operatorname{lcm}(m,n))=\max(a,b)$, where $a=v_p(m),\,b=v_p(n)$, we get the key local description:

**Observation.** For every prime $p$, a move replaces the exponent pair $(a,b)$ at the two chosen positions by
$$\big(\min(a,b),\ |a-b|\big),$$
and leaves all other exponents unchanged. Note $\min(a,b)+|a-b|=\max(a,b)$.

---

### Part (a)

Let $P(C)=c_1c_2\cdots c_{2026}$ and let $c(C)$ be the number of entries greater than $1$.

**Step 1: Each move either strictly decreases $P$, or keeps $P$ fixed and strictly decreases $c$.**

A move replaces the sub-product $mn$ by $\gcd(m,n)\cdot\frac{\operatorname{lcm}(m,n)}{\gcd(m,n)}=\operatorname{lcm}(m,n)$, so the new product is $P/\gcd(m,n)$.

* If $\gcd(m,n)\ge 2$, then $P$ strictly decreases (and remains a positive integer).
* If $\gcd(m,n)=1$, then $P$ is unchanged, and the two chosen entries change from $m>1,\ n>1$ to $1$ and $mn>1$. All other entries are untouched, so $c$ decreases by exactly $1$.

**Step 2: The process terminates.**

Suppose some sequence of choices produced infinitely many moves. The values of $P$ form a non-increasing sequence of positive integers, so they are eventually constant, say from move $N$ onward. By Step 1, every move after move $N$ must have $\gcd(m,n)=1$ and hence strictly decreases the integer $c$ by $1$. But $0\le c\le 2026$ always, so there cannot be infinitely many such moves — contradiction. Hence every play terminates after finitely many moves.

**Step 3: The terminal board has exactly one entry $>1$.**

*At most one:* if two entries exceeded $1$, a move would still be possible, contradicting terminality.

*At least one:* Fix a prime $p$ dividing the initial entry $c_1\ (\ge 2)$. We claim that at every stage some entry is divisible by $p$. This holds initially; assume it holds before some move acting on $m,n$ with $a=v_p(m),\ b=v_p(n)$. If the $p$-divisible entry is not among $m,n$, it is untouched. If it is, then $\max(a,b)>0$, and since the new exponents $\min(a,b)$ and $|a-b|$ sum to $\max(a,b)>0$, at least one new entry is divisible by $p$. So the claim persists, and at termination the entry divisible by $p$ is $\ge p>1$.

Hence the process always stops after finitely many moves with exactly one integer $M>1$ on the board (all other entries equal $1$). $\blacksquare$

---

### Part (b)

For a tuple $(e_1,\dots,e_k)$ of non-negative integers, let $d(e_1,\dots,e_k)$ be the unique non-negative integer with
$$e_1\mathbb{Z}+e_2\mathbb{Z}+\cdots+e_k\mathbb{Z}=d\,\mathbb{Z},$$
i.e. their greatest common divisor, with $d=0$ exactly when all $e_i=0$. For each prime $p$ and board $C$ define
$$D_p(C)=d\big(v_p(c_1),\dots,v_p(c_{2026})\big).$$

**Lemma. $D_p$ is invariant under every move, for every prime $p$.**

*Proof.* A move changes only two exponents, from $(a,b)$ to $(\min(a,b),\,|a-b|)$. WLOG $a\le b$, so the new pair is $(a,\,b-a)$. Since $b-a$ is an integer combination of $a,b$, and $b=a+(b-a)$ is an integer combination of $a, b-a$, we have
$$a\mathbb{Z}+b\mathbb{Z}=a\mathbb{Z}+(b-a)\mathbb{Z}.$$
Adding the (unchanged) subgroups $v_p(c_\ell)\mathbb{Z}$ for the other positions $\ell$, the total subgroup $\sum_i v_p(c_i)\mathbb{Z}$ — and hence $D_p$ — is unchanged. $\square$

Now take any play of the game, starting from the initial board $C_0=(a_1,\dots,a_{2026})$. By part (a) it ends with a board consisting of one entry $M>1$ and $2025$ entries equal to $1$. For every prime $p$, the terminal exponents are $v_p(M),0,0,\dots,0$, so
$$D_p(\text{terminal board})=v_p(M).$$
By the Lemma, applied to each move in turn,
$$v_p(M)=D_p(C_0)=\gcd\big(v_p(a_1),\dots,v_p(a_{2026})\big)\qquad\text{for every prime }p.$$
(For primes $p$ dividing none of the $a_i$ this gcd is $0$, consistently giving $v_p(M)=0$; only the finitely many primes dividing $a_1\cdots a_{2026}$ contribute.)

Therefore, no matter which moves Confucius makes,
$$M \;=\; \prod_{p\ \mathrm{prime}} p^{\,\gcd\left(v_p(a_1),\,\dots,\,v_p(a_{2026})\right)},$$
which depends only on the initial numbers. In particular, the final value $M$ is independent of all choices made during the process. $\blacksquare$

---

**Sanity check.** For the board $(8,12,10)$: exponents of $2$ are $(3,2,1)$ with gcd $1$; of $3$ are $(0,1,0)$; of $5$ are $(0,0,1)$; so $M=2\cdot3\cdot5=30$. Indeed, e.g. $(8,12,10)\to(4,6,10)\to(2,6,10)\to(2,2,15)\to(2,1,15)\to(1,1,30)$, and every other play also ends at $30$.

time: 3 mins