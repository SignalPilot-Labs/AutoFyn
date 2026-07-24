# Approach: per-prime-valuation-descent

## Status
solved

## Approaches tried
- (round 1, new) Termination (part a) via a per-prime valuation-mass potential Ω = Σ_i Σ_p v_p(x_i), paired lexicographically with N = #{entries > 1}. Non-coprime moves strictly drop Ω; coprime moves keep Ω fixed and drop N by 1; so the lex pair (Ω, N) strictly decreases every move and is well-founded, giving a fully explicit finite move bound. Part (b) via the per-prime gcd invariant g_p = gcd(v_p(x_1),…,v_p(x_2026)), which is preserved by the subtractive-Euclid identity gcd(min(a,b),|a−b|) = gcd(a,b) and gcd-associativity over the multiset. Distinct framing from global-lex-monovariant (per-prime valuation mass vs global scalar product). Built in full; the redundant extremal fallback was dropped as the direct lex closes cleanly. — WORKED, complete proof below.

## Current best
Complete rigorous proof of both parts (below). Termination bound: at most (Ω₀ + 1)·2026 moves, where Ω₀ = Σ_i Ω(x_i) is the initial total number of prime factors with multiplicity. Value: M = ∏_p p^{g_p} with g_p = gcd(v_p(x_1),…,v_p(x_2026)) the initial per-prime valuation gcd.

## Full proof

### 0. Setup, notation, and valuation form of a move

There are 2026 integers, each greater than 1, in fixed positions 1,…,2026 on the board; write the current multiset of values as $x_1,\dots,x_{2026}$. A **move** picks two positions holding values $m>1$ and $n>1$ and replaces them by
$$g=\gcd(m,n)\qquad\text{and}\qquad h=\frac{\operatorname{lcm}(m,n)}{\gcd(m,n)}.$$
Since $\gcd(m,n)\mid \operatorname{lcm}(m,n)$, $h$ is a positive integer; both new entries are $\ge 1$. Moves are made as long as one is *possible*, i.e. as long as at least two positions hold a value $>1$. All other positions are unchanged by a move.

**Valuation form.** Fix a prime $p$ and let $v_p$ denote the $p$-adic valuation. By the Fundamental Theorem of Arithmetic (unique factorization),
$$v_p(\gcd(m,n))=\min\!\big(v_p(m),v_p(n)\big),\qquad v_p(\operatorname{lcm}(m,n))=\max\!\big(v_p(m),v_p(n)\big).$$
Hence, writing $a=v_p(m)$, $b=v_p(n)$,
$$v_p(g)=\min(a,b),\qquad v_p(h)=v_p(\operatorname{lcm})-v_p(\gcd)=\max(a,b)-\min(a,b)=|a-b|.$$
So a move acts, simultaneously for every prime $p$, on the pair of exponents at the two chosen positions by
$$(a,b)\ \longmapsto\ \big(\min(a,b),\,|a-b|\big),$$
and leaves every other position's exponent unchanged. This is the only structural fact we use; note the position choice is *shared* across all primes (one move, one pair of positions, all primes updated at once).

**Finitely many primes.** Let $P$ be the (finite) set of primes dividing at least one of the 2026 initial values. If $p\notin P$ then $v_p(x_i)=0$ for all initial $i$. We claim no move can ever produce an entry divisible by a prime outside $P$. Indeed $g=\gcd(m,n)$ divides $m$, and $h=\operatorname{lcm}(m,n)/\gcd(m,n)$ divides $\operatorname{lcm}(m,n)$, whose prime divisors are exactly those of $m$ or of $n$; so every prime dividing a newly created entry already divided a pre-existing entry. By induction on the number of moves, every entry on the board at every time has all its prime factors in $P$. Consequently $v_p(x_i)=0$ for all $p\notin P$ and all times, so any sum $\sum_p(\cdots)$ over primes below is effectively a finite sum over $p\in P$.

Throughout we use the convention $\gcd(x,0)=x$ for $x\ge 0$ (so $\gcd(0,0)=0$), consistent with "$d\mid 0$ for every $d$." Under this convention, for integers $y_1,\dots,y_k\ge 0$ not all zero, $\gcd(y_1,\dots,y_k)$ is a positive integer, and it is $0$ iff all $y_i=0$.

We also record the elementary identity used repeatedly:
$$\min(a,b)+|a-b|=\max(a,b)\qquad(a,b\ge 0),\tag{$\star$}$$
because $|a-b|=\max(a,b)-\min(a,b)$. And $\max(a,b)\le a+b$, with equality iff $\min(a,b)=0$.

---

### Part (a): the process terminates with exactly one entry $>1$

We use the technique **invariant/monovariant** (knowledge_base.md, "Invariants & monovariants" / "General Proof Methods: Invariant / monovariant"): a lexicographic monovariant that strictly decreases every move, plus the **Well-Ordering Principle** for $\mathbb N$.

Define two nonnegative integers of the current board:
$$\Omega=\sum_{i=1}^{2026}\ \sum_{p} v_p(x_i)=\sum_{p}S_p,\qquad S_p=\sum_{i=1}^{2026}v_p(x_i),$$
$$N=\#\{\,i: x_i>1\,\}.$$
Here $\Omega$ is the total number of prime factors of all entries counted with multiplicity (i.e. $\sum_i\Omega(x_i)$, $\Omega$ = big-omega); by the finiteness paragraph the outer sum over $p$ has only finitely many nonzero terms, so $\Omega$ is a well-defined nonnegative integer. $N$ is a nonnegative integer with $0\le N\le 2026$.

#### Step 1 — $\Omega$ is non-increasing; strict drop $\iff\gcd(m,n)>1$.

Consider a move at two positions with values $m,n$, exponents $a_p=v_p(m)$, $b_p=v_p(n)$ for each prime $p$. Only these two positions change. For each $p$, the contribution of these two positions to $S_p$ changes from $a_p+b_p$ to $v_p(g)+v_p(h)=\min(a_p,b_p)+|a_p-b_p|=\max(a_p,b_p)$ by $(\star)$. Hence
$$\Delta\Omega=\sum_p\big(\max(a_p,b_p)-(a_p+b_p)\big)=-\sum_p\min(a_p,b_p)\ \le\ 0.$$
So $\Omega$ never increases. Moreover $\Delta\Omega<0$ iff $\sum_p\min(a_p,b_p)>0$ iff there exists a prime $p$ with $\min(a_p,b_p)>0$, i.e. a prime dividing both $m$ and $n$, i.e. $\gcd(m,n)>1$. Equivalently, $\Omega$ is *unchanged* by the move iff $\gcd(m,n)=1$.

#### Step 2 — behavior of $N$; a coprime move drops $N$ by exactly 1.

A move takes two positions, both holding values $>1$ (a move requires $m,n>1$), and replaces them by $g,h\ge 1$. No other position changes. Since at most two of the two chosen positions can hold a value $>1$ after the move, $N$ can only stay the same or decrease: **$N$ is non-increasing.**

Now split on $\gcd(m,n)$:

- **Coprime move ($\gcd(m,n)=1$).** Then $g=\gcd(m,n)=1$ and $h=\operatorname{lcm}(m,n)/1=mn$. Since $m,n>1$, $mn>1$. So the two positions go from $(m,n)$ (both $>1$) to $(1,mn)$ (exactly one $>1$): $N$ decreases by exactly $1$.

- **Non-coprime move ($\gcd(m,n)>1$).** Then $g=\gcd(m,n)>1$, so the position holding $g$ still has a value $>1$; the other holds $h\ge 1$, which may be $1$ (e.g. $m=n$ gives $h=1$) or $>1$. Thus $N$ decreases by $0$ or $1$. In all cases $N$ does not increase.

#### Step 3 — the lexicographic monovariant $\Phi=(\Omega,N)$ strictly decreases every move.

Order pairs of nonnegative integers by the **lexicographic order** with $\Omega$ primary and $N$ secondary: $(\Omega',N')<(\Omega,N)$ iff $\Omega'<\Omega$, or $\Omega'=\Omega$ and $N'<N$. Set $\Phi=(\Omega,N)$. For any single move exactly one of the following holds, and in each $\Phi$ strictly decreases:

- If $\gcd(m,n)>1$: by Step 1, $\Omega$ strictly decreases. Then $\Phi$ decreases lexicographically regardless of what $N$ does (and by Step 2, $N$ does not increase anyway).
- If $\gcd(m,n)=1$: by Step 1, $\Omega$ is exactly unchanged; by Step 2, $N$ decreases by exactly $1$. So the primary coordinate is equal and the secondary strictly drops: $\Phi$ decreases lexicographically.

These two cases are exhaustive and disjoint ($\gcd(m,n)$ is either $1$ or $>1$; note $\gcd(m,n)\ge 1$ always). In particular **no move leaves both $\Omega$ and $N$ unchanged.** Hence $\Phi$ strictly decreases at every move.

#### Step 4 — termination (explicit finite bound).

Both coordinates of $\Phi$ are nonnegative integers, and $\Phi$ strictly decreases each move (Step 3); by the Well-Ordering Principle a strictly decreasing sequence in the well-founded lexicographic order on $\mathbb N\times\mathbb N$ is finite. We give an explicit bound. Let $\Omega_0$ be the initial value of $\Omega$. Since $\Omega$ is a non-increasing nonnegative integer (Step 1), it takes at most $\Omega_0+1$ distinct values during the play. Consider a maximal run of consecutive moves during which $\Omega$ stays constant. By Step 1, every move in such a run has $\gcd(m,n)=1$ (a non-coprime move would strictly drop $\Omega$, ending the run); by Step 2 each such move drops $N$ by exactly $1$. Since $N$ is a nonnegative integer $\le 2026$, such a run has length at most $2026$. As there are at most $\Omega_0+1$ constant-$\Omega$ runs, the total number of moves is at most $(\Omega_0+1)\cdot 2026<\infty$. **Thus the process terminates after finitely many moves.**

#### Step 5 — the terminal board has exactly one entry $>1$.

A move is *impossible* exactly when fewer than two positions hold a value $>1$, i.e. when $N\le 1$. So at termination $N\in\{0,1\}$. We exclude $N=0$.

By Step (b) below (Part (b) does **not** rely on termination, so there is no circularity), the quantity $g_p=\gcd\big(v_p(x_1),\dots,v_p(x_{2026})\big)$ is invariant under every move. Initially some entry $x_i>1$, so it has a prime factor $p_0$ with $v_{p_0}(x_i)\ge 1$; then $g_{p_0}=\gcd(v_{p_0}(x_1),\dots,v_{p_0}(x_{2026}))$ is a gcd of nonnegative integers not all zero (one of them is $\ge 1$), hence $g_{p_0}\ge 1>0$. By invariance, $g_{p_0}>0$ holds at the terminal board too.

Suppose, for contradiction, $N=0$ at termination: then every entry equals $1$, so $v_{p_0}(x_i)=0$ for all $i$, giving $g_{p_0}=\gcd(0,\dots,0)=0$ — contradicting $g_{p_0}>0$. Therefore $N=1$: **the terminal board has exactly one entry $M>1$ (and the other $2025$ entries equal $1$).**

Since termination and $N=1$ hold *regardless of the choices made* along the way (Steps 1–5 use no property of the choices beyond the move rule), part (a) is proved. $\qquad\blacksquare$ (a)

---

### Part (b): the value $M$ is independent of the choices

We prove that $M=\prod_p p^{g_p}$ where $g_p=\gcd\big(v_p(x_1),\dots,v_p(x_{2026})\big)$ is computed from the **initial** board, and hence is the same for every legal play.

#### Step B1 — the subtractive-Euclid identity.

**Lemma 1.** For all integers $a,b\ge 0$, $\ \gcd\big(\min(a,b),\,|a-b|\big)=\gcd(a,b)$, with the convention $\gcd(x,0)=x$.

*Proof.* Both $\min(a,b)$ and $|a-b|$ are symmetric in $a,b$, as is $\gcd$; so we may assume $a\ge b$. Then $\min(a,b)=b$ and $|a-b|=a-b$, and we must show $\gcd(b,a-b)=\gcd(a,b)$. It suffices to show the two pairs $\{a,b\}$ and $\{a-b,b\}$ have the *same set of common divisors*, for then their greatest common divisors coincide (the convention makes $\gcd$ the largest common divisor, or $0$ when everything is $0$). Let $d\ge 1$. If $d\mid a$ and $d\mid b$ then $d\mid(a-b)$, so $d$ is a common divisor of $\{a-b,b\}$. Conversely, if $d\mid(a-b)$ and $d\mid b$ then $d\mid\big((a-b)+b\big)=a$, so $d$ is a common divisor of $\{a,b\}$. Hence the common-divisor sets coincide.

Boundary cases (all covered by the above, but made explicit):
- $a=b$: then $\min=b=a$, $|a-b|=0$, so LHS $=\gcd(a,0)=a=\gcd(a,a)=$ RHS.
- $b=0$ (with $a\ge 0$): $\min=0$, $|a-b|=a$, LHS $=\gcd(0,a)=a=\gcd(a,0)=$ RHS.
- $a=b=0$: LHS $=\gcd(0,0)=0=$ RHS.

$\square$

#### Step B2 — $g_p$ is invariant under every move.

**Lemma 2 (gcd is associative / determined pairwise over a multiset).** For nonnegative integers $y_1,\dots,y_k$ and any $1\le r<s\le k$,
$$\gcd(y_1,\dots,y_k)=\gcd\Big(\gcd(y_r,y_s),\ \{y_t: t\neq r,s\}\Big).$$
More precisely, if $y_r,y_s$ are replaced by two nonnegative integers $y_r',y_s'$ with $\gcd(y_r',y_s')=\gcd(y_r,y_s)$, the gcd of the whole tuple is unchanged.

*Proof.* Define, for a tuple, $G=\gcd(y_1,\dots,y_k)$ = the largest integer dividing every $y_i$ (or $0$ if all are $0$). The universal property of $\gcd$ of two numbers states: for any integer $d$, $\ d\mid y_r$ and $d\mid y_s$ $\iff$ $d\mid\gcd(y_r,y_s)$. Therefore the set of common divisors of the full tuple $(y_1,\dots,y_k)$ equals the set of common divisors of the tuple obtained by replacing the pair $(y_r,y_s)$ with the single value $\gcd(y_r,y_s)$ (the remaining coordinates $y_t$, $t\ne r,s$, being identical). Two tuples with the same set of common divisors have the same greatest common divisor. This proves the first display. For the second claim: replacing $(y_r,y_s)$ by $(y_r',y_s')$ with $\gcd(y_r',y_s')=\gcd(y_r,y_s)$ leaves the common-divisor set of the whole tuple unchanged, since $\{d: d\mid y_r', d\mid y_s'\}=\{d:d\mid\gcd(y_r',y_s')\}=\{d:d\mid\gcd(y_r,y_s)\}=\{d:d\mid y_r,d\mid y_s\}$; hence the overall gcd is unchanged. $\square$

Now fix a prime $p$ and a move at positions $r,s$ with exponents $a=v_p(x_r)$, $b=v_p(x_s)$. The move replaces $(a,b)$ by $(\min(a,b),|a-b|)$ and leaves all other exponents $v_p(x_t)$, $t\ne r,s$, unchanged. By Lemma 1, $\gcd(\min(a,b),|a-b|)=\gcd(a,b)$; by Lemma 2 (second claim) the gcd of the whole exponent tuple, namely $g_p$, is unchanged. This holds for every prime $p$. **Thus each $g_p$ is invariant under every move.** (In particular, this invariance is proved with no reference to termination, so importing it in Part (a) Step 5 is not circular.)

#### Step B3 — reading off $M$ at the terminal board.

By Part (a), the terminal board has exactly one entry $M>1$, say at position $j$, and $x_i=1$ for all $i\ne j$. For each prime $p$ the exponent tuple at the terminal board is $v_p(M)$ at position $j$ and $0$ elsewhere, so
$$g_p^{\text{(terminal)}}=\gcd\big(v_p(M),0,\dots,0\big)=v_p(M),$$
using $\gcd(c,0,\dots,0)=c$ for $c\ge 0$. By Step B2, $g_p^{\text{(terminal)}}=g_p^{\text{(initial)}}=:g_p$. Hence $v_p(M)=g_p$ for every prime $p$, and by unique factorization
$$\boxed{\,M=\prod_{p} p^{\,g_p},\qquad g_p=\gcd\big(v_p(x_1),\dots,v_p(x_{2026})\big)\text{ computed on the initial board.}\,}$$
The right-hand side depends only on the initial 2026 numbers, not on any choices Confucius makes. Therefore $M$ is the same for every legal play. (The product is finite: $g_p=0$ for all $p\notin P$, so $M=\prod_{p\in P}p^{g_p}$; and $M>1$ since some $g_{p_0}>0$ by Part (a) Step 5, consistent with $M>1$.) $\qquad\blacksquare$ (b)

---

### Verification of the value on a sanity example

Take the tiny analogue with values $\{4,6\}$ ($v_2:(2,1)$, $v_3:(0,1)$): $g_2=\gcd(2,1)=1$, $g_3=\gcd(0,1)=1$, predicted $M=2\cdot3=6$. Play the (only) move on $4,6$: $\gcd=2$, $\operatorname{lcm}/\gcd=12/2=6$, board $\{2,6\}$; move on $2,6$: $\gcd=2$, $\operatorname{lcm}/\gcd=6/2=3$, board $\{2,3\}$... wait, both $>1$, move again on $2,3$: coprime, $\to\{1,6\}$. Terminal $M=6=\prod p^{g_p}$. A different order — move on $2,6$ first from $\{2,6\}$ gives the same $\{2,3\}\to\{1,6\}$. The value $6$ matches $\prod p^{g_p}$, and is choice-independent, confirming both the mechanism and the formula. (This is an illustrative check, not part of the proof; the proof above stands on its own.)

$\blacksquare$

## Promotable lemmas
- **Lemma 1 (subtractive-Euclid via min/|·|).** For all integers $a,b\ge 0$, $\gcd(\min(a,b),|a-b|)=\gcd(a,b)$ (convention $\gcd(x,0)=x$, $\gcd(0,0)=0$). Proved in Part (b) Step B1, all boundaries ($a=b$, $b=0$, $a=b=0$) included.
- **Lemma 2 (gcd determined pairwise over a multiset).** Replacing two entries $y_r,y_s$ of a nonnegative-integer tuple by any $y_r',y_s'$ with $\gcd(y_r',y_s')=\gcd(y_r,y_s)$ leaves the tuple's overall gcd unchanged. Proved in Part (b) Step B2 via the universal (common-divisor) property of gcd.
- **Termination lemma (lex valuation-mass monovariant).** For the gcd/lcm-split board process, the pair $(\Omega,N)$ — $\Omega=\sum_i\Omega(x_i)$ total prime-factor count with multiplicity, $N=\#\{x_i>1\}$ — strictly decreases in lex order (Ω primary) every move, giving termination in $\le(\Omega_0+1)\cdot 2026$ moves. Proved in Part (a) Steps 1–4.

## Spec concerns
None. Both parts are proven in full: termination with an explicit finite move bound, the terminal state has exactly one entry $>1$ (with $N=0$ excluded via an invariant $g_{p_0}>0$), and $M=\prod_p p^{g_p}$ is shown choice-independent. Every invoked result (Fundamental Theorem of Arithmetic, Well-Ordering Principle, subtractive Euclidean identity, universal property of gcd, lexicographic well-foundedness) is named and either standard or proved inline. No case is left open; the coprime/non-coprime split is exhaustive and disjoint, and all gcd-identity boundaries are checked.
