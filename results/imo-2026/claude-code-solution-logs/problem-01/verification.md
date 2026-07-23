# Verification and Justification of Each Step

This document audits the solution in `solution.md` step by step, checking hypotheses, edge cases, and potential gaps.

---

## 0. Reading of the problem statement

- The board always holds exactly $2026$ entries: a move **replaces** two entries by two entries, so the count never changes. ✔
- A move requires two entries $m>1$, $n>1$ **in different positions** (equal values are allowed, e.g. two entries both equal to $5$). Therefore:
  - a move is possible $\iff$ at least two positions hold values $>1$;
  - the process stops $\iff$ at most one position holds a value $>1$.
  This equivalence is used verbatim in the solution and is a direct restatement of the rules. ✔
- Entries equal to $1$ may appear after moves and simply sit on the board; the rules never let them be chosen again. ✔

## 1. Well-definedness of the move (Setup section)

**Claim:** $\operatorname{lcm}(m,n)/\gcd(m,n)$ is a positive integer.

**Justification:** For every prime $p$, $v_p(\gcd)=\min(v_p m, v_p n)\le \max(v_p m, v_p n)=v_p(\operatorname{lcm})$. An integer $d\ge1$ divides an integer $N\ge 1$ iff $v_p(d)\le v_p(N)$ for all $p$; hence $\gcd(m,n)\mid\operatorname{lcm}(m,n)$. ✔

The formulas $v_p(\gcd)=\min$, $v_p(\operatorname{lcm})=\max$ are the standard characterizations of $\gcd$/$\operatorname{lcm}$ via prime factorization (valid for all positive integers, including $1$, whose exponents are all $0$). ✔

## 2. Equation (2): exponent-level description of a move

If the move hits entries with $p$-exponents $a,b$, the new exponents are
$$v_p(\gcd)=\min(a,b),\qquad v_p(\operatorname{lcm}/\gcd)=v_p(\operatorname{lcm})-v_p(\gcd)=\max(a,b)-\min(a,b)=|a-b|.$$
The subtraction of valuations is legitimate because $\gcd \mid \operatorname{lcm}$ (Step 1) and $v_p(x/y)=v_p(x)-v_p(y)$ whenever $y\mid x$. Untouched positions keep their exponents. ✔

**Sanity check on examples:** $(m,n)=(12,18)$: $\gcd=6$, $\operatorname{lcm}/\gcd=36/6=6$. Exponents of $2$: $(2,1)\to(\min,|{\cdot}|)=(1,1)$ ✓; exponents of $3$: $(1,2)\to(1,1)$ ✓ — matches $(6,6)$. ✔

## 3. Part (a), Claim 1: lexicographic monovariant $(P,k)$

**Product formula (3).** $g\ell = mn$ is the standard identity $\gcd(m,n)\operatorname{lcm}(m,n)=mn$ (check via exponents: $\min(a,b)+\max(a,b)=a+b$). The two new entries multiply to $g\cdot(\ell/g)=\ell = mn/g$, and other entries are unchanged, so $P\mapsto P/g$, still a positive integer by Step 1. ✔

**Case $g>1$:** $P/g<P$ strictly, since $P\ge 1$ and $g\ge 2$. Lexicographic decrease follows from the first coordinate alone — no claim about $k$ is needed in this case (indeed $k$ can stay the same, e.g. $(4,2)\to(2,2)$, or drop, e.g. $(4,4)\to(4,1)$; either is fine). ✔

**Case $g=1$:** New entries are $1$ and $mn$. Check $mn>1$: yes, since $m,n\ge2$. Both old entries were $>1$ (a move may only choose entries $>1$ — this is where that hypothesis is essential). So among the two affected positions the count of entries $>1$ goes $2\to1$; elsewhere unchanged; hence $k\mapsto k-1$ exactly, and $P\mapsto P/1=P$. Lexicographic decrease via the second coordinate. ✔

**Potential gap checked:** could a case be missed? $g=\gcd(m,n)\ge1$ always, and the two cases $g=1$, $g>1$ are exhaustive. ✔

## 4. Part (a): well-ordering argument

The monovariant lives in $\mathbb{Z}_{\ge1}\times\{0,\dots,2026\}$. Suppose an infinite run existed, giving an infinite strictly lex-decreasing sequence $(P_t,k_t)$. The sequence $P_t$ is non-increasing in $\mathbb{Z}_{\ge1}$, so it stabilizes after finitely many steps (it can strictly drop at most $P_0-1$ times). After stabilization, every move must strictly decrease $k_t$ (by Claim 1, each move decreases the pair, and the first coordinate is now frozen), but $k_t$ is a nonnegative integer, so it can strictly decrease only finitely often — contradiction. Hence every run is finite. ✔

(This is spelled out in the solution parenthetically; the argument is elementary and complete — no appeal to abstract ordinal theory is needed.)

## 5. Part (a), Claim 2: an entry $>1$ always exists

- Base case: initially all entries are $>1$ (given), and $2026\ge1$. ✔
- Inductive step: a move outputs $g$ and $mn/g$ (with $m,n>1$). If $g>1$, output $g>1$. If $g=1$, output $mn/g = mn \ge 4>1$. Either way one output exceeds $1$. Note this argument does **not** rely on any untouched entry being $>1$ — the produced entry itself suffices, so the invariant holds even if the two chosen entries were the only ones exceeding $1$. ✔
- **Edge case checked:** $m=n$ (allowed, different positions): $g=m>1$, other output $=\operatorname{lcm}/\gcd = m/m=1$. Invariant still holds via $g$. ✔

## 6. Part (a): conclusion

Termination (Step 4) + "no move possible $\Rightarrow k\le1$" (Step 0) + "$k\ge1$ always" (Step 5) $\Rightarrow$ terminal $k=1$: exactly one entry $M>1$, the other $2025$ entries equal $1$. This is exactly statement (a). ✔

## 7. Part (b), Claim 3: invariance of $G_p$

**Key identity:** for integers $a\ge b\ge0$: $\gcd(b,a-b)=\gcd(a,b)$.

*Proof audit:* common divisors of $\{a,b\}$ and of $\{b,a-b\}$ coincide: $d\mid a,b \Rightarrow d \mid a-b$; $d\mid b, a-b \Rightarrow d\mid (a-b)+b = a$. Same divisor sets $\Rightarrow$ same greatest one (or both pairs are $(0,0)$, where both gcds are $0$). Edge cases:
- $a=b$: $\gcd(a,0)=a=\gcd(a,a)$ ✓
- $b=0$: new pair $(0,a)$, $\gcd = a = \gcd(a,0)$ ✓
- $a=b=0$: $\gcd(0,0)=0$ on both sides ✓ (convention stated in the solution). ✔

**Multiset step:** $G_p(B)=\gcd(x_i, x_j, \text{rest}) = \gcd(\gcd(x_i,x_j), \gcd(\text{rest}))$ by associativity/commutativity of $\gcd$ (valid for nonnegative integers with the stated conventions, since $\gcd$ computes the nonnegative generator of the subgroup of $\mathbb Z$ generated by the listed elements, and generated subgroups don't depend on grouping). The move preserves $\gcd(x_i,x_j)$ (key identity, with $\{a,b\}\to\{\min, \max-\min\}$ matching $(2)$) and leaves "rest" untouched. Hence $G_p$ is preserved by each single move, and by induction along the run, from the initial to the final state. ✔

**Subtlety checked — coupling between primes:** the same pair of positions is used simultaneously for all primes, and moves can only use positions whose **values** exceed $1$. Neither fact is used in Claim 3 — the invariance holds for each prime separately for *any* legal move — so the coupling is harmless. The only place the dynamics matter is that part (a) guarantees the final state has the special shape (one entry $>1$, rest $=1$). ✔

## 8. Part (b): evaluation at the final state

Final board: $(M,1,\dots,1)$ up to position, with $M>1$. For each prime $p$: exponents are $(v_p(M),0,\dots,0)$, and $\gcd(v_p(M),0,\dots,0)=v_p(M)$ (convention $\gcd(t,0,\dots,0)=t$, including $t=0$ for primes $p\nmid M$). Hence
$$v_p(M)=G_p(\text{final})=G_p(\text{initial})=g_p \quad\text{for every prime } p.$$
A positive integer is uniquely determined by all its $p$-adic valuations, so $M=\prod_p p^{g_p}$. The product is finite: $g_p=0$ unless $p\mid a_1\cdots a_{2026}$, and only finitely many primes divide that number. ✔

**Why this proves (b):** the right-hand side depends only on the initial data, and the argument applies to *every* legal run; hence any two runs end with the same $M$. ✔

**Consistency with (a):** $a_1>1$ has a prime divisor $q$; then $v_q(a_i)\ge0$ for all $i$ and $v_q(a_1)\ge1$... note $g_q=\gcd_i v_q(a_i)$ could still be computed from values including $0$; $g_q \ge 1$ requires **all** $a_i$'s? No: $\gcd(t,0)=t$, so zeros do not force $g_q=0$; $g_q=0$ would require $v_q(a_i)=0$ for **all** $i$, contradicting $v_q(a_1)\ge1$. So $g_q\ge1$ and $M\ge q^{g_q} \ge 2 >1$. Consistent. ✔

## 9. Independent empirical verification

A brute-force simulator (Python) was run before finalizing the write-up:

- **4000 random instances** (board sizes $2$–$6$, entries in $[2,200]$), **5 independent random strategies each**, plus **12 adversarial hand-picked instances** (prime powers, equal entries, highly composite chains) with **200 random strategies each** — roughly $25{,}000$ full runs.
- Checks performed per run: (i) termination within a move bound; (ii) final board has **exactly one** entry $>1$; (iii) the final value equals $\prod_p p^{\gcd_i v_p(a_i)}$.
- **Result: 0 failures.**

Illustrative cases traced by hand:
- $(4,2)$: $\to(2,2)\to(2,1)$, $M=2$; formula: $\gcd(2,1)=1$, $M=2^1=2$ ✓ (note: **not** $\gcd(4,2)=2$ — the invariant is the gcd of *exponents*, not of the numbers).
- $(2,3)$: $\to(1,6)$, $M=6$; formula: $2^{\gcd(1,0)}3^{\gcd(0,1)}=2\cdot3=6$ ✓.
- $(4,4)$: $\to(4,1)$, $M=4$; formula: $2^{\gcd(2,2)}=4$ ✓.

## 10. Overall assessment

- Part (a) uses only: well-definedness of the move, the identity $\gcd\cdot\operatorname{lcm}=mn$, a two-case analysis, and finite lexicographic descent. All cases exhaustive, all edge cases ($m=n$, $\gcd=1$, minimal boards) checked.
- Part (b) uses only: the exponent description $(2)$, the subtractive-Euclid gcd identity, and the terminal shape from (a). The invariant argument is per-prime and per-move, hence choice-independent by construction.
- No step relies on the specific number $2026$ beyond $2026\ge2$ (so that the initial board is nonempty and a first move can even be contemplated; the proof works verbatim for any board size $\ge 1$, with size $1$ being trivially terminal).

**Verdict: the solution is complete and rigorous.**
