## Status
solved

## Approaches tried
- perprime-gcd-lexmonovariant — APPROVED (solved). Per-prime p-adic exponent tracking + lexicographic monovariant (Ω, K) for termination; invariant d_p = gcd of the p-exponent multiset for choice-independence. Both parts (a) and (b) settled with full exhaustive case analysis (Cases (i)–(iii): g=1; g>1, m≠n; g>1, m=n). The Ω-drop is Ω(gcd(m,n)) (corrected from an earlier `2Ω(gcd)` slip and re-derived per-prime as ∑_p min(v_p(m),v_p(n))). The all-ones terminus is ruled out rigorously via the d_p invariant. M = ∏_p p^{d_p} is correctly derived; the note that M is *not* the gcd of the numbers (it is the product of p^{gcd of valuations}, not p^{min of valuations}) is correct and verified on the example {12,18,30,7,100,9,25} → M=210.
- confluence-newman — CHANGES REQUESTED (partial). Part (a) fully proven on this route (same (Ω,K) monovariant + d_p invariant). Part (b) reduced, via Newman's lemma (correctly stated), to local confluence of the whole-number rewrite system; local confluence reduces to two critical-pair shapes — case A (disjoint redexes, proven by one-step commutation) and case B (overlapping redexes on three entries {a,b,c}). Case B joinability is the open gap: no explicit common reduct is known, the natural symmetric two-step completion fails empirically (4869/5000), and the per-prime 1D local confluence argument does not lift (moves couple primes). Empirically case B holds (2000/2000), but "empirically true" is not a proof. Gap: prove case-B joinability with an explicit common reduct or a genuine lifting argument.

## Current best
Complete proof of both parts via the per-prime invariant + lex monovariant (perprime-gcd-lexmonovariant). Part (a): the lexicographic monovariant (Ω, K) strictly decreases every legal move (exhaustive three-case analysis) and is bounded below, giving termination; the stuck condition gives K ≤ 1, and the d_p invariant rules out K = 0, forcing exactly one M > 1. Part (b): the invariant d_p = gcd of the multiset of initial p-exponents is preserved by the Euclidean step gcd(min(α,β),|α−β|) = gcd(α,β); at the terminus {M,1,…,1} this forces v_p(M) = d_p, hence M = ∏_p p^{d_p}, depending only on the initial board.

## Full proof

**Problem (IMO 2026, Problem 1).** There are 2026 integers greater than 1 written on a blackboard, not necessarily different. In a move, Confucius chooses two integers $m>1$ and $n>1$ from different places on the blackboard and replaces these two integers with $\gcd(m,n)$ and $\dfrac{\operatorname{lcm}(m,n)}{\gcd(m,n)}$. He continues to make moves while it is possible to do so. (a) Prove that, regardless of the choices of Confucius, after finitely many moves, exactly one integer $M$ on the blackboard is greater than $1$. (b) Prove that the value of $M$ does not depend on the choices of Confucius.

---

### Notation and preliminary identities

For a prime $p$ write $v_p(a)$ for the $p$-adic valuation of a positive integer $a$ (the exponent of $p$ in the factorisation of $a$; in particular $v_p(1)=0$). Write
$$\Omega(a) \;=\; \sum_{p} v_p(a)$$
for the total prime-factor multiplicity of $a$, with $\Omega(1)=0$. The function $\Omega$ is *completely additive*: for all positive integers $x,y$,
$$\Omega(xy) \;=\; \Omega(x) + \Omega(y),$$
because $v_p(xy)=v_p(x)+v_p(y)$ for every prime $p$, and the sum over $p$ is finite since only finitely many primes divide a given integer.

We use three standard identities (cf. `knowledge_base.md`, "Divisor analysis: gcd structure"):

- **(I1)** $\gcd(m,n)\cdot\operatorname{lcm}(m,n) = mn$ for all positive integers $m,n$.
- **(I2)** $v_p(\gcd(m,n)) = \min(v_p(m),v_p(n))$ and $v_p(\operatorname{lcm}(m,n)) = \max(v_p(m),v_p(n))$.
- **(I3) Euclidean step.** $\gcd(a,b) = \gcd\!\big(\min(a,b),\,|a-b|\big)$ for all non-negative integers $a,b$.

*Proof of (I3).* Assume w.l.o.g. $a\ge b$, so $\min(a,b)=b$ and $|a-b|=a-b$. The classical Euclidean identity $\gcd(a,b)=\gcd(b,a-b)$ (a divisor of both $a$ and $b$ divides $a-b$, and conversely a divisor of $b$ and $a-b$ divides $b+(a-b)=a$) gives the claim; the case $b\ge a$ is symmetric. ∎

We also adopt the convention $\gcd(x,0)=x$ for $x\ge 0$ (consistent with (I3) at $a=0$), extended to a multiset by iterating: $\gcd(x_1,\dots,x_r) = \gcd(\gcd(x_1,\dots,x_{r-1}),x_r)$. In particular $\gcd(0,\dots,0)=0$, and $\gcd(0,k)=k$ so zeros are identities and the gcd of a multiset equals the gcd of its nonzero elements (or $0$ if all are zero).

---

### Step 1 — Per-prime description of a move

Fix a prime $p$ and suppose the two chosen board entries have $p$-valuations $\alpha = v_p(m)$, $\beta = v_p(n)$. The move replaces $m,n$ by $\gcd(m,n)$ and $\operatorname{lcm}(m,n)/\gcd(m,n)$. By (I1)–(I2),
$$v_p(\gcd(m,n)) = \min(\alpha,\beta), \qquad v_p\!\Big(\frac{\operatorname{lcm}(m,n)}{\gcd(m,n)}\Big) = v_p(\operatorname{lcm}(m,n)) - v_p(\gcd(m,n)) = \max(\alpha,\beta) - \min(\alpha,\beta) = |\alpha-\beta|.$$

Hence, prime by prime, **a move sends the pair of $p$-valuations $(\alpha,\beta)$ to $\big(\min(\alpha,\beta),\,|\alpha-\beta|\big)$**, and leaves every other board entry's $p$-valuation untouched. This holds simultaneously for every prime $p$ (the same move acts on all primes at once — we do not run the primes independently).

---

### Step 2 — The invariant $d_p$

For each prime $p$ define, at any state of the board,
$$D_p \;:=\; \gcd\big(v_p(a_1),\, v_p(a_2),\, \dots,\, v_p(a_{2026})\big),$$
the gcd of the multiset of all 2026 $p$-valuations present on the board (with the convention $\gcd(x,0)=x$). Let $d_p := D_p$ at the *initial* board.

**Claim (invariance).** $D_p$ is unchanged by every legal move.

*Proof.* Consider a move on entries whose $p$-valuations are $\alpha,\beta$; the other 2024 $p$-valuations are untouched. Before the move the multiset of $p$-valuations is $\{\alpha,\beta\}\cup S$ where $S$ is the multiset of the remaining 2024 valuations; after the move it is $\{\min(\alpha,\beta),|\alpha-\beta|\}\cup S$. By (I3),
$$\gcd\big(\min(\alpha,\beta),\,|\alpha-\beta|\big) \;=\; \gcd(\alpha,\beta).$$
The gcd of a multiset factors as $\gcd(\text{all elements}) = \gcd(\gcd(\text{pair}),\,\gcd S)$, so replacing the pair $\alpha,\beta$ by any two elements with the same pairwise gcd leaves the gcd of the whole multiset unchanged:
$$\gcd\big(\alpha,\beta,\,\text{elements of }S\big) = \gcd\big(\gcd(\alpha,\beta),\,\text{elements of }S\big) = \gcd\big(\gcd(\min(\alpha,\beta),|\alpha-\beta|),\,\text{elements of }S\big).$$
Since $\gcd(\alpha,\beta)=\gcd(\min(\alpha,\beta),|\alpha-\beta|)$, the two sides coincide. Hence $D_p$ is invariant. ∎

So $D_p = d_p$ at every reachable state, for every prime $p$. (Cf. `knowledge_base.md`, "Invariants & monovariants".)

---

### Step 3 — The monovariant $(\Omega, K)$

Define at every state
$$\Omega \;:=\; \sum_{i=1}^{2026} \Omega(a_i) \qquad\text{and}\qquad K \;:=\; \#\{\,i : a_i > 1\,\}.$$
Both are non-negative integers; $\Omega\ge 0$, and $0\le K\le 2026$.

**Claim.** Every legal move strictly decreases the lexicographic pair $(\Omega, K)$ (with $\Omega$ the primary, $K$ the secondary coordinate).

*Proof.* Consider a move on two entries $m,n>1$. Put $g:=\gcd(m,n)$ and write $m=g\cdot a$, $n=g\cdot b$ with $\gcd(a,b)=1$ (so $a,b\ge 1$). By (I1)–(I2),
$$\frac{\operatorname{lcm}(m,n)}{\gcd(m,n)} \;=\; \frac{mn}{g^2} \;=\; \frac{g a\cdot g b}{g^2} \;=\; ab.$$
So the move replaces the pair $(m,n)=(ga,gb)$ by $(g,\,ab)$.

We split into three exhaustive cases. (The split is exhaustive: either $g=1$ or $g>1$; in the latter either $m=n$ or $m\ne n$. The combination $g=1$ and $m=n$ is impossible because $m=n>1$ forces $g=m>1$.)

**Case (i): $g=1$ (coprime pair).** Then $m=a$, $n=b$ with $\gcd(a,b)=1$, and the move replaces $(m,n)$ by $(1,ab)$. By complete additivity and $\gcd(a,b)=1$,
$$\Omega(ab) \;=\; \Omega(a)+\Omega(b) \;=\; \Omega(m)+\Omega(n),$$
so $\Omega$ does not change. As for $K$: since $g=1$ and $n=b>1$, we have $b>1$, hence $ab\ge b>1$. So the entry $m>1$ is replaced by $1$ (a drop of one in $K$) while $n>1$ is replaced by $ab>1$ (no change). Thus $K$ drops by exactly $1$. Lexicographically, $(\Omega,K)\to(\Omega,K-1)$, a strict decrease.

**Case (ii): $g>1$ and $m\ne n$.** The move replaces $(ga,gb)$ by $(g,ab)$. First note $ab\ge 2$: since $g>1$ and $m\ne n$, we have $(a,b)\ne(1,1)$ (else $m=n=g$); with $\gcd(a,b)=1$ and not both $1$, we get $ab\ge 2$. Thus both new entries $g>1$ and $ab>1$ are $>1$, so $K$ does not change. It remains to compute the $\Omega$-drop.

By complete additivity,
$$\Omega(ga)+\Omega(gb) \;=\; \big(\Omega(g)+\Omega(a)\big)+\big(\Omega(g)+\Omega(b)\big) \;=\; 2\,\Omega(g) + \Omega(a)+\Omega(b),$$
and
$$\Omega(g)+\Omega(ab) \;=\; \Omega(g) + \Omega(a)+\Omega(b),$$
the last equality using $\gcd(a,b)=1$ hence complete additivity across $a\cdot b$. The drop is
$$\Delta \;=\; \big[\Omega(ga)+\Omega(gb)\big] - \big[\Omega(g)+\Omega(ab)\big] \;=\; \Omega(g).$$

*Per-prime derivation (the load-bearing identity).* Fix a prime $p$ and write $\alpha=v_p(m)$, $\beta=v_p(n)$. The two entries contribute $\alpha+\beta$ to $\Omega$ before and $\min(\alpha,\beta)+|\alpha-\beta|=\max(\alpha,\beta)$ after, for a per-prime drop of $(\alpha+\beta)-\max(\alpha,\beta)=\min(\alpha,\beta)=v_p(g)$. Summing over all primes gives $\Delta=\sum_p v_p(g)=\Omega(g)$. (This is the correct identity; the value is $\Omega(g)$, not $2\,\Omega(g)$.)

Since $g>1$, $\Omega(g)\ge 1$. Hence $\Omega$ strictly decreases (by $\Omega(g)\ge 1$), while $K$ is unchanged. Lexicographically this is a strict decrease.

**Case (iii): $g>1$ and $m=n$.** Then $m=n=g$ (since $m=ga$ and $n=gb$ with $m=n$ forces $a=b$; with $\gcd(a,b)=1$ this forces $a=b=1$). The move replaces $(g,g)$ by $(g,1)$ (as $ab=1\cdot 1=1$). The $\Omega$-drop is $\Omega(g)$ (one copy of $g$ is removed, the other kept): formally $\Omega(g)+\Omega(g) - [\Omega(g)+\Omega(1)] = \Omega(g)\ge 1$. And $K$ drops by $1$ (the entry $g>1$ becomes $1$; the other $g>1$ stays). Both coordinates drop; in particular the lex pair strictly decreases.

In all three cases $(\Omega,K)$ strictly decreases in lexicographic order. ∎

---

### Step 4 — Termination

**Claim.** No infinite play is possible: every sequence of legal moves is finite.

*Proof.* The pair $(\Omega,K)$ lies in $\mathbb{N}_0\times\{0,1,\dots,2026\}$ and strictly decreases lexicographically at every move. The lexicographic order on $\mathbb{N}_0\times\{0,1,\dots,2026\}$ is well-founded (contains no infinite descending chain): indeed $\Omega$ is a non-negative integer, so it can strictly decrease only finitely many times; between two consecutive decreases of $\Omega$ the secondary coordinate $K\in\{0,\dots,2026\}$ can strictly decrease at most 2026 times. Summing over the finitely many $\Omega$-levels visited gives a finite total bound on the number of moves. (Cf. `knowledge_base.md`, infinite descent.) Hence every play terminates. ∎

---

### Step 5 — Stuck states have $K\le 1$

A move is legal precisely when two entries $>1$ exist, i.e. when $K\ge 2$. So a *stuck* (terminal) state — one where no legal move is available — has $K\le 1$.

---

### Step 6 — Ruling out $K=0$; hence $K=1$

**Claim.** No reachable stuck state has $K=0$; equivalently, at every terminal state $K=1$.

*Proof.* Suppose for contradiction that a terminal state has $K=0$, i.e. all 2026 entries equal $1$. Then for every prime $p$ every $p$-valuation on the board is $0$, so $D_p=\gcd(0,0,\dots,0)=0$ (with our convention). By the invariance of Step 2, $d_p = D_p = 0$ for every prime $p$.

But $d_p$ is the gcd of the *initial* $p$-valuations $v_p(a_1),\dots,v_p(a_{2026})$, and $d_p=0$ for every $p$ forces $v_p(a_i)=0$ for every $p$ and every $i$ (the gcd of a multiset of non-negative integers is $0$ only when every element is $0$), i.e. every initial $a_i=1$. This contradicts the hypothesis that all 2026 initial integers are $>1$.

Hence $K\ne 0$ at any terminal state. Combined with Step 5 ($K\le 1$ at any terminal state), we get $K=1$ at every terminal state. ∎

(Equivalently, in the positive direction: some initial $a_i>1$ has some prime $p\mid a_i$, so $v_p(a_i)\ge 1$; since zeros are identities for the gcd, $d_p=\gcd(v_p(a_1),\dots)\ge 1$ for that $p$; by invariance $D_p=d_p\ge 1$ at the terminal state, forcing some terminal entry to carry a positive $p$-valuation, i.e. $K\ge 1$.)

---

### Step 7 — Conclusion of part (a)

By Step 4 every play terminates; by Steps 5–6 every terminal state has $K=1$, i.e. exactly one entry $M>1$ on the board, the other 2025 entries being $1$. This proves part (a): regardless of Confucius's choices, after finitely many moves exactly one integer $M>1$ remains. $\square_{(a)}$

---

### Step 8 — Determining $M$; conclusion of part (b)

Fix any terminal state reached by any play. By Step 7 its board is $\{M,1,1,\dots,1\}$ (one entry $M>1$, 2025 entries equal to $1$). For any prime $p$,
$$v_p(M),\; v_p(1),\dots, v_p(1) \;=\; v_p(M),\; 0,\; \dots,\; 0 \quad (\text{2025 zeros}),$$
so the multiset of $p$-valuations on the board is $\{v_p(M),0,\dots,0\}$ and, with the convention $\gcd(x,0,\dots,0)=x$,
$$D_p \;=\; v_p(M).$$
By the invariance of Step 2, $D_p=d_p$, so
$$\boxed{\,v_p(M) \;=\; d_p\,}$$
for every prime $p$.

The primes with $d_p>0$ are among the (finitely many) primes dividing some initial $a_i$ — there are at most $\sum_i \Omega(a_i)$ of them, a finite number. For every prime $p$ not dividing any $a_i$, every initial $v_p(a_i)=0$, hence $d_p=0$ and $v_p(M)=0$, so $p\nmid M$. Therefore
$$M \;=\; \prod_{p} p^{\,d_p},$$
a finite product over the primes dividing the initial board, with exponents $d_p$ depending *only* on the initial board (specifically on the gcds of the initial $p$-valuation multisets). No move-dependent quantity appears. Hence $M$ is the same at every terminal state, regardless of Confucius's choices. $\square_{(b)}$

---

### Verification on a worked example

For the initial board $\{12,18,30,7,100,9,25\}$ (a 7-number instance of the same process):

| $p$ | $v_p$ of the seven entries | $d_p=\gcd$ |
|---|---|---|
| $2$ | $(2,1,1,0,2,0,0)$ | $1$ |
| $3$ | $(1,2,1,0,0,2,0)$ | $1$ |
| $5$ | $(0,0,1,0,2,0,2)$ | $1$ |
| $7$ | $(0,0,0,1,0,0,0)$ | $1$ |

So $M = 2^1\cdot 3^1\cdot 5^1\cdot 7^1 = 210$. This matches direct simulation (200 random plays all terminate at $M=210$). Note that $\gcd(12,18,30,7,100,9,25)=1\ne M$, illustrating the warning: $M$ is *not* the gcd of the numbers (which would be the *min* of the valuations, not preserved by the move). The invariant is the gcd *of the valuations*, not the valuations of the gcd.

---

### Summary of named tools invoked

- **Complete additivity of $\Omega$** (`knowledge_base.md`, Divisor analysis): $\Omega(xy)=\Omega(x)+\Omega(y)$.
- **Gcd/Lcm identities (I1), (I2)** (`knowledge_base.md`, Divisor analysis): $\gcd\cdot\operatorname{lcm}=mn$; $v_p(\gcd)=\min$, $v_p(\operatorname{lcm})=\max$.
- **Euclidean step (I3)** (`knowledge_base.md`, Divisor analysis): $\gcd(a,b)=\gcd(\min(a,b),|a-b|)$ — the load-bearing identity preserving $D_p$.
- **Invariant / monovariant technique** (`knowledge_base.md`, Invariants & monovariants): $D_p$ invariant for (b); $(\Omega,K)$ lex monovariant for (a).
- **Well-foundedness / infinite descent** (`knowledge_base.md`): lex order on $\mathbb{N}_0\times\{0,\dots,2026\}$ has no infinite descending chain, giving termination.

Both parts are proved with every case settled (Cases (i)–(iii) exhaustive in Step 3, $K=0$ ruled out in Step 6) and every load-bearing identity derived rather than asserted. ∎
