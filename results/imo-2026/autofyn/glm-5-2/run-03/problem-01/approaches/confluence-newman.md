# confluence-newman

## Status
partial

## Approaches tried
- **Round 1 (this build):** Newman's-lemma framing of (b). Proved (a) in full on this route (termination via the (Ω,K) lexicographic monovariant, with the corrected Ω-difference identity Ω(m)+Ω(n)−[Ω(g)+Ω(h)] = Ω(g); and "exactly one M>1" via the stuck⟺≤1 condition plus the d_p invariant ruling out the all-ones terminus). Stated Newman's lemma precisely as a named theorem. Proved local confluence for the **disjoint-redex** critical pairs (case A: they commute in one step each). The **overlapping-redex** critical pairs (case B: three entries {a,b,c}, moves on (a,b) and (a,c)) are the load-bearing gap: empirically every tested triple joins (2000/2000, and full reachable-set intersection nonempty), but no explicit algebraic common reduct is known — the natural symmetric two-step completion fails (4869/5000), and minimal joins run as deep as 3+3=6 steps with no fixed small pattern. The per-prime 1D analogue *is* locally confluent (provable directly via its unique normal form {d_p,0,…,0}), but this does not lift to the whole-number system because a single move fires the per-prime move on all primes simultaneously and the per-prime joining sequences need not synchronize. Hence (b) on this route remains reduced to the open case-B joinability. Outcome: (a) solved on this route, (b) partial — honest gap recorded.

## Current best
**(a) is fully proven on this route** (termination + exactly-one), via the (Ω,K) lexicographic monovariant and the d_p invariant — independent of confluence. **(b) is reduced to a single open step**: by Newman's lemma (stated below), (b) follows once the whole-number rewriting system is locally confluent; local confluence is in turn equivalent (for this system, by an exhaustive pair-of-positions case split) to the joinability of the **overlapping critical pair** {a,b,c}: the two one-step reducts
  B1 = move(a,b) ∪ {c} = {gcd(a,b), lcm(a,b)/gcd(a,b), c},
  B2 = move(a,c) ∪ {b} = {gcd(a,c), lcm(a,c)/gcd(a,c), b}
must have a common reduct. Case A (disjoint redexes) is proven (one-step commutation). The **open gap is case B**: no explicit common reduct is known, and the clean per-prime argument does not lift because moves couple primes. Empirically the gap is true (so (b) is almost certainly true, as the direct route confirms independently), but it is not proven on this route.

## Full proof

Not present: Status is `partial` because (b) is not fully proven on this route. What follows is the complete rigorous account of everything that *is* proven on this route, with the open gap flagged explicitly.

---

### 0. Setup and the move

There are 2026 integers >1 on the board. A **state** is a multiset $S$ of 2026 positive integers (we keep the all-1 entries implicitly; only entries >1 matter for legality). The rewrite rule, applied to two entries $m,n>1$ at two distinct positions, replaces them by
$$
\operatorname{mv}(m,n) \;=\; \bigl(g,\; h\bigr),\qquad g=\gcd(m,n),\quad h=\frac{\operatorname{lcm}(m,n)}{\gcd(m,n)}=\frac{mn}{g^{2}}.
$$
(The equality $h=mn/g^{2}$ uses $\operatorname{lcm}(m,n)=mn/\gcd(m,n)$.) The rule is symmetric: $\operatorname{mv}(m,n)=\operatorname{mv}(n,m)$ as a multiset, so a move is determined by the unordered pair of positions chosen.

A **normal form** is a state admitting no legal move, i.e. a state with at most one entry $>1$ (a move requires two entries $>1$). Part (a) asserts every play reaches a normal form with *exactly* one entry $>1$; part (b) asserts the multiset of that normal form — equivalently the single integer $M>1$ in it — is independent of the play.

### 1. Per-prime move identity (lemma)

Let $p$ range over primes. Write $\nu_p(x)=v_p(x)$ for the $p$-adic valuation. For a single move on $(m,n)$,
$$
\bigl(\nu_p(m),\,\nu_p(n)\bigr)\;\longmapsto\;\bigl(\min(\nu_p(m),\nu_p(n)),\;|\nu_p(m)-\nu_p(n)|\bigr),
$$
because $\nu_p(\gcd(m,n))=\min$ and $\nu_p(\operatorname{lcm}(m,n)/\gcd(m,n))=\nu_p(\operatorname{lcm})-\nu_p(\gcd)=\max-\min=|\nu_p(m)-\nu_p(n)|$ (using $\nu_p(\operatorname{lcm}(m,n))=\max$ and $\gcd\cdot\operatorname{lcm}=mn$). This identity is used in Section 4.

### 2. Termination — the $(\Omega,K)$ lexicographic monovariant (proven here)

Let $\Omega(x)=\sum_p \nu_p(x)$ (total prime-factor multiplicity, with $\Omega(1)=0$), and let $K(S)=\#\{i: x_i>1\}$ for a state $S=(x_1,\dots,x_{2026})$. Both are nonnegative integers; $K\in[0,2026]$. Order states by the lexicographic pair $(\Omega(S),K(S))$, where $\Omega(S):=\sum_i\Omega(x_i)$.

**Lemma (Ω-difference identity).** For a move replacing $(m,n)$ by $(g,h)$ with $g=\gcd(m,n)$, $h=\operatorname{lcm}(m,n)/\gcd(m,n)$,
$$
\Omega(m)+\Omega(n)-\bigl[\Omega(g)+\Omega(h)\bigr]\;=\;\Omega(g)\;\ge\;0,
$$
with equality iff $\gcd(m,n)=1$.

*Proof.* By complete additivity $\Omega(ab)=\Omega(a)+\Omega(b)$. Since $\operatorname{lcm}(m,n)=mn/g$,
$$
\Omega(\operatorname{lcm}(m,n))=\Omega(m)+\Omega(n)-\Omega(g).
$$
Since $h=\operatorname{lcm}(m,n)/g$, additivity gives $\Omega(h)=\Omega(\operatorname{lcm}(m,n))-\Omega(g)=\Omega(m)+\Omega(n)-2\Omega(g)$. Hence
$$
\Omega(g)+\Omega(h)=\Omega(g)+\Omega(m)+\Omega(n)-2\Omega(g)=\Omega(m)+\Omega(n)-\Omega(g),
$$
so the difference is $\Omega(g)$. Finally $\Omega(g)=0\iff g=1$. ∎

**Corollary (strict lex decrease).** Every legal move strictly decreases $(\Omega,K)$ lexicographically.

*Proof.* Let the move replace $(m,n)$, $m,n>1$, and put $g=\gcd(m,n)$, $h=mn/g^{2}$.
- **Case (i): $g=1$ (coprime).** Then $m\neq n$ (since $m=n>1\Rightarrow g=m>1$, contradiction). By the identity, $\Omega$ is unchanged. Because $g=1$, $h=\operatorname{lcm}(m,n)=mn>1$. So the old pair $(m,n)$ contributed $2$ to $K$, the new pair $(g,h)=(1,mn)$ contributes $1$; $K$ drops by $1$.
- **Case (ii): $g>1$ and $m\neq n$.** Write $m=ga$, $n=gb$ with $\gcd(a,b)=1$ and $a\neq b$. Then $h=\operatorname{lcm}(m,n)/g=\operatorname{lcm}(a,b)=ab$ (coprimality). Since $a\neq b$ and not both $1$ (both $1$ would force $m=n=g$), we have $ab\ge 2$, so $h>1$. The old pair contributes $2$ to $K$, the new pair $(g,h)$ (both $>1$) contributes $2$; $K$ is unchanged. But $\Omega$ drops by $\Omega(g)\ge 1$ by the identity.
- **Case (iii): $g>1$ and $m=n$.** Then $g=m$ and $h=mn/g^{2}=1$. The old pair contributes $2$ to $K$, the new pair $(g,1)$ contributes $1$; $K$ drops by $1$, and $\Omega$ drops by $\Omega(g)=\Omega(m)\ge 1$.

These three cases are exhaustive: $g=1$ forces $m\neq n$ (case (i) only); $g>1$ splits into $m=n$ (case (iii)) and $m\neq n$ (case (ii)). In every case either $\Omega$ drops (by $\ge 1$) with $K$ not increasing, or $\Omega$ is fixed and $K$ drops by $1$. Hence $(\Omega,K)$ strictly decreases in the lexicographic order. ∎

**Well-foundedness and termination.** $\Omega(S)\in\mathbb N$ is bounded below by $0$ and is nonincreasing along any play (it only drops or stays). Between two consecutive $\Omega$-drops, $K$ can drop at most finitely often (at most $2026$ times, since $K\in[0,2026]$). The number of $\Omega$-drops is finite (each drops $\Omega$ by $\ge 1$, and $\Omega\ge 0$). Hence every play is finite: the process **terminates**. (Equivalently, lexicographic order on $\mathbb N\times[0,2026]$ is well-founded.)

### 3. "Exactly one $M>1$" — the $d_p$ invariant (proven here)

For a prime $p$, define
$$
d_p(S)\;=\;\gcd\bigl(\nu_p(x_1),\nu_p(x_2),\dots,\nu_p(x_{2026})\bigr),
$$
using the convention $\gcd(a,0)=a$ and $\gcd(0,\dots,0)=0$.

**Lemma (invariance of $d_p$).** $d_p$ is invariant under every move.

*Proof.* A move touches only two entries, with $p$-exponents $\alpha,\beta$; it replaces them by $\min(\alpha,\beta)$ and $|\alpha-\beta|$ (Section 1). The other $2024$ exponents are untouched. It remains to use the Euclidean identity
$$
\gcd\bigl(\min(\alpha,\beta),\,|\alpha-\beta|\bigr)\;=\;\gcd(\alpha,\beta),
$$
which holds because the Euclidean step $\gcd(a,b)=\gcd(a,b-a)$ is gcd-preserving, and $\{\min(\alpha,\beta),|\alpha-\beta|\}$ is exactly the pair obtained from $(\alpha,\beta)$ by one such step (if $\alpha\le\beta$: $\min=\alpha$, $|\alpha-\beta|=\beta-\alpha$, and $\gcd(\alpha,\beta-\alpha)=\gcd(\alpha,\beta)$). Replacing $\alpha,\beta$ in the multiset of exponents by $\min(\alpha,\beta),|\alpha-\beta|$ therefore leaves the gcd of the whole multiset unchanged. ∎

**Lemma (stuck $\Leftrightarrow$ $\le 1$ entry $>1$).** A state is a normal form iff it admits no legal move iff it has at most one entry $>1$.

*Proof.* A legal move exists iff two entries are $>1$. ∎

**Proposition (exactly one entry $>1$ at every terminus).** Every normal form reachable from the initial board has exactly one entry $>1$.

*Proof.* By Section 2 every play terminates at a normal form, which by the previous lemma has $\le 1$ entry $>1$. Suppose for contradiction some reachable normal form $S_\infty$ has **zero** entries $>1$, i.e. all entries equal $1$. Then every $p$-exponent of every entry is $0$, so the multiset of $p$-exponents is $\{0,\dots,0\}$ and $d_p(S_\infty)=0$ for every prime $p$. By invariance (previous lemma), $d_p(S_0)=0$ for every $p$, where $S_0$ is the initial board. But $d_p(S_0)=0$ means every initial $p$-exponent is $0$, i.e. **no** initial entry is divisible by $p$; holding for every prime $p$ means every initial entry equals $1$, contradicting the hypothesis that all 2026 initial integers are $>1$. Hence a reachable normal form has at least one entry $>1$; combined with $\le 1$, it has **exactly one** entry $>1$. ∎

**This completes part (a) on this route:** regardless of choices, after finitely many moves exactly one integer $M>1$ remains. ∎(a)

### 4. Part (b) via Newman's lemma — reduction to local confluence

The remaining claim is that the integer $M$ is the same for every play, i.e. that the rewriting system has a **unique normal form**. The intended engine is:

> **Theorem (Newman's lemma, 1942).** *Let $R$ be an abstract rewriting system that is terminating (no infinite rewrite sequence). If $R$ is locally confluent — meaning for every state $x$ and every pair of one-step reducts $y,z$ of $x$ (i.e. $x\to y$ and $x\to z$) there exists a state $w$ with $y\to^{*}w$ and $z\to^{*}w$ (where $\to^{*}$ is the reflexive–transitive closure) — then $R$ is confluent: for every $x$ and every $y,z$ with $x\to^{*}y$ and $x\to^{*}z$, there is $w$ with $y\to^{*}w$ and $z\to^{*}w$.*

This is the standard diamond-lemma for terminating systems (Newman, *A theorem in abstract rewriting*, 1942); it is **not** in the project `knowledge_base.md` and is invoked here as a named theorem of abstract rewriting theory. A terminating + confluent system has a **unique normal form** reachable from each state: if two normal forms $y,z$ are reachable from $x$, confluence gives $w$ with $y\to^{*}w$ and $z\to^{*}w$; but normal forms reduce only to themselves, so $w=y=z$.

By Section 2 the system is terminating. So Newman's lemma reduces (b) to **local confluence**.

#### 4.1 Local confluence reduces to two critical-pair shapes

Local confluence concerns a state $S$ and two one-step reducts. Each one-step move is determined by an unordered pair of positions both holding entries $>1$. Given two such pairs $\{i,j\}$ and $\{k,\ell\}$, the configuration of positions falls into exactly three cases:

- **(A) Disjoint:** $\{i,j\}\cap\{k,\ell\}=\varnothing$ (four distinct positions).
- **(B) Overlapping:** $|\{i,j\}\cap\{k,\ell\}|=1$ (three distinct positions).
- **(C) Coincident:** $\{i,j\}=\{k,\ell\}$ (same pair).

In case (C) the two "moves" are the same move: the rule $\operatorname{mv}(m,n)$ is symmetric in $m,n$, so both reducts are identical — there is no divergence, hence no critical pair. Thus genuine one-step divergences are exactly cases (A) and (B); these are disjoint and exhaustive, so local confluence is equivalent to joinability in case (A) and in case (B).

#### 4.2 Case (A): disjoint redexes commute (proven)

If the two chosen pairs are disjoint, the two moves act on independent entries. Concretely, move 1 replaces positions $i,j$ by $\operatorname{mv}(x_i,x_j)$, move 2 replaces positions $k,\ell$ by $\operatorname{mv}(x_k,x_\ell)$; since $\{i,j\}\cap\{k,\ell\}=\varnothing$, move 1 does not alter the values at $k,\ell$ and vice versa. Applying move 1 then move 2 yields the same final multiset as move 2 then move 1: both entries $i,j$ become $\operatorname{mv}(x_i,x_j)$ and both entries $k,\ell$ become $\operatorname{mv}(x_k,x_\ell)$. Hence from the two one-step reducts $S_1$ (move 1 applied) and $S_2$ (move 2 applied), one more move on each reaches the common state $T=\operatorname{move}_2(\operatorname{move}_1(S))=\operatorname{move}_1(\operatorname{move}_2(S))$:
$$
S_1\;\xrightarrow{\text{move 2}}\;T,\qquad S_2\;\xrightarrow{\text{move 1}}\;T.
$$
So disjoint redexes are joinable in one step each. ∎ (case A)

#### 4.3 Case (B): overlapping redexes — the open gap

The remaining configuration has three distinct positions carrying entries $a,b,c$ (all $>1$), with the two competing moves on the pairs $(a,b)$ and $(a,c)$ (the shared entry is $a$; up to relabeling this is the only shape). The two one-step reducts are
$$
B_1=\{g_{ab},\,h_{ab},\,c\},\qquad B_2=\{g_{ac},\,b,\,h_{ac}\},
$$
where $g_{xy}=\gcd(x,y)$ and $h_{xy}=\operatorname{lcm}(x,y)/\gcd(x,y)=xy/g_{xy}^{2}$. Local confluence requires a state $T$ with $B_1\to^{*}T$ and $B_2\to^{*}T$.

**Status of case B: open.** I cannot exhibit, for arbitrary $\{a,b,c\}$, an explicit common reduct, and I record the failed attempts honestly:

1. **Symmetric two-step completion fails.** The natural candidate — from $B_1$ apply the move on $(g_{ab},c)$, and from $B_2$ apply the move on $(g_{ac},b)$, in imitation of the shared-entry pattern — does *not* produce equal multisets in general. A brute-force check on 5000 random triples gave equal multisets only 131 times (4869 failures), e.g. $\{17,39,36\}$: $B_1\to\{1,663,36\}$ then $\to\{1,663,36\}$ (move on $(g_{ab}=1,c=36)$ leaves the state, since $g_{ab}=1$ is not $>1$, so no move fires), while $B_2\to\{1,39,612\}$ similarly stuck — the two stuck states differ. So no fixed symmetric 1-step completion works.

2. **No fixed 1-step mutual completion exists.** Exhaustively testing, for each triple, *all* one-step completions from $B_1$ against *all* one-step completions from $B_2$: a common reduct exists for most triples but fails for some (e.g. $\{35,16,42\}$: $B_1=\{1,560,42\}$, $B_2=\{7,16,30\}$; no single move on each side produces equal multisets). Hence case B sometimes requires $\ge 2$ moves on a side.

3. **Joins are real but deep and patternless.** Bidirectional search shows minimal joins of depth up to $3+3=6$ total moves, with no fixed small bound or fixed completion strategy. (Distribution over 1500 random triples: depths range $(1,1)$ through $(3,3)$, with $(1,1)$ most common but $(2,3),(3,2),(3,3)$ present.) So an explicit common reduct is not a simple function of $\{a,b,c\}$ via one or two named moves.

4. **The per-prime 1D analogue is locally confluent, but does not lift.** Restrict to one prime $p$, so the state is a multiset of nonneg exponents and the move is $(\alpha,\beta)\mapsto(\min(\alpha,\beta),|\alpha-\beta|)$. This 1D system is terminating (the sum of exponents drops by $\min(\alpha,\beta)$ each move) and has a unique normal form $\{d_p,0,\dots,0\}$: at a normal form at most one exponent is nonzero, and the $d_p$ invariant (Section 3, identical proof) forces that one to equal $d_p=\gcd$ of the initial exponents. Hence (by uniqueness of normal form for a terminating system) the 1D system *is* locally confluent. **But** this does *not* prove local confluence of the whole-number system: a whole-number move fires the per-prime move on *every* prime simultaneously, and the per-prime joining sequences for different primes need not be synchronizable into a single valid whole-number move sequence. The coupling of primes across moves is exactly the obstruction the outline flagged ("do not prove (a) by running per-prime Euclidean algorithms to completion (moves couple primes)").

5. **Empirical confirmation that case B is true.** Computed the full reachable sets $\{T:B_1\to^{*}T\}$ and $\{T:B_2\to^{*}T\}$ for 2000 random triples $\{a,b,c\}$ with $a,b,c\in[2,80]$; in every case the intersection is nonempty. So case-B joinability almost certainly holds, and hence (b) is almost certainly true (as the direct invariant route confirms independently). But "empirically true" is not a proof step; I do not present it as one.

Because I cannot close case B with an explicit common reduct or a lifting argument, **Newman's lemma cannot be applied on this route**, and (b) is not proven here.

### 5. What is proven, and the precise open gap

- **(a): proven on this route.** Termination (Section 2, $(\Omega,K)$ lex descent with the identity $\Omega(m)+\Omega(n)-[\Omega(g)+\Omega(h)]=\Omega(g)$, exhaustive case analysis) + exactly-one (Section 3, stuck$\Leftrightarrow\le 1$ and $d_p$ rules out the all-ones terminus).
- **(b): reduced to the open case B.** Newman's lemma (stated, Section 4) reduces (b) to local confluence; local confluence reduces (Section 4.1) to cases A and B; case A is proven (Section 4.2); **case B (overlapping redexes on three entries) is open** — no explicit common reduct is known, the natural completions fail, and the per-prime argument does not lift (Section 4.3).

**Consistency note (not a proof step).** If case B were closed, the unique normal form would be the multiset $\{M,1,\dots,1\}$ with $M=\prod_p p^{d_p}$ where $d_p=\gcd$ of the initial $p$-exponents; e.g. for $\{12,18,30,7,100,9,25\}$ this gives $M=210$, matching a greedy play. This is a check, not part of the confluence argument.

## Promotable lemmas
- **Per-prime move identity** $(\nu_p(m),\nu_p(n))\mapsto(\min,|\Delta|)$ — proven in Section 1; reusable across all approaches to this problem. (Likely already present in the sibling approach `perprime-gcd-lexmonovariant`; listed here for completeness.)
- **$d_p$ invariance** ($d_p=\gcd$ of $p$-exponent multiset is preserved by every move, via the Euclidean identity $\gcd(\min(\alpha,\beta),|\alpha-\beta|)=\gcd(\alpha,\beta)$) — proven in Section 3; reusable; the load-bearing shared sub-lemma for ruling out the all-ones terminus.
- **$(\Omega,K)$ lexicographic termination** with the corrected identity $\Omega(m)+\Omega(n)-[\Omega(g)+\Omega(h)]=\Omega(g)$ and the three-case ($g=1$; $g>1,m\neq n$; $g>1,m=n$) exhaustive analysis — proven in Section 2; reusable.
- **Stuck$\Leftrightarrow\le 1$ entry $>1$** — Section 3; trivial but reusable.
(These four are all proven in full here; if not already certified in `results/imo-2026-01/lemmas/`, the reviewer may certify any of them. The genuinely route-specific content — Newman's lemma and the case-B gap — is not promotable, since case B is open.)
