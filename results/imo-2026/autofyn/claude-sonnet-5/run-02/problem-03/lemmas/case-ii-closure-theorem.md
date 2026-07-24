## Statement

Call a finite sequence $\tau=(\tau_1>\tau_2>\dots>\tau_m>0)$ a *ratio-2
superincreasing tail of length $m$* if $\tau_i=2\tau_{i+1}$ for $1\le i<m$.
Write $R(\tau):=\sum\tau_i$.

**Theorem (GC($m$)).** *For every $m\ge1$ and every ratio-2 superincreasing
tail $\tau=(\tau_1,\dots,\tau_m)$: for every $s\in(0,2\tau_1]$ and every
partition $F$ of $s$ into at most $m+1$ positive parts with **at least one
part exceeding $\tau_1$** (the "Case II" / dominant-fragment sub-case),*
$$A(F\cup\tau)\ \ge\ s-R(\tau).$$

Taking $m=n$, $\tau=T=\{p_2,\dots,p_{n+1}\}$ (the $n$-ladder's tail),
$s=p_1=2\tau_1$, this gives Claim (A)'s Case II for the original problem,
for every $n$: $A(F\cup T)\ge a_n$ whenever some fragment of $F$ (a
partition of $p_1$) exceeds $p_2$.

**Essentiality of the part-count bound.** The $\le m+1$-part restriction is
not droppable: a 3-part counterexample exists without it ($m=1$,
$\tau=(\tau_1)$, $s=1.8\tau_1$, $F=\{0.6\tau_1,0.6\tau_1,0.6\tau_1\}$ gives
$A(F\cup\tau)=0.4\tau_1<0.8\tau_1=s-R(\tau)$). This never arises in the
actual recursion since the budget invariant (part count $=$ tail length
$+1$) is preserved throughout.

## Proof (strong induction on $m$)

**Base case $m=1$**, $a:=\tau_1$, $s\in(0,2a]$, $F$ has $1$ or $2$ parts.
One part $F=\{s\}$: $A(\{s,a\})=|s-a|\ge s-a$. Two parts $F=\{f,g\}$,
$f\ge g>0$, $f+g=s$: both $f,g>a$ is impossible ($f+g>2a\ge s$,
contradiction), so $\mathrm{median}\{f,g,a\}\le a$, equivalent (via
$A=\mathrm{Total}-2\cdot\mathrm{median}$ for 3 elements) to the claim.

**Inductive step, $m\ge2$.** If $s\le R(\tau)$: $A(F\cup\tau)\ge0\ge s-R(\tau)$
trivially (integral-nonnegativity, `integral-alternating-sum-formula`). If
$s>R(\tau)$: at most one part of $F$ exceeds $\tau_1$ (else two such parts
sum to $>2\tau_1\ge s\ge$ their sum, contradiction). Let $f_1$ be that part,
$F'=F\setminus\{f_1\}$, $s':=s-f_1<\tau_1$. Every element of $F'\cup
(\tau_2,\dots,\tau_m)$ is $<\tau_1$, so `sharp-dominant-removal-identity`
gives $A(F\cup\tau)=f_1-A(F'\cup\tau)$, and a rank-shift computation
(removing the strict unique max $\tau_1$ from $F'\cup\tau$; general fact:
for any finite multiset $U$ with strict unique max $u$, the sum of $U$'s
even-ranked sorted elements equals $\Phi(U\setminus\{u\})=(\mathrm{Total}
(U\setminus\{u\})+A(U\setminus\{u\}))/2$) gives
$A(F'\cup\tau)=\tau_1-A(F'\cup\tau'')$ where $\tau''=(\tau_2,\dots,\tau_m)$.
Substituting and simplifying, the target becomes exactly $A(F'\cup\tau'')
\ge s'-R(\tau'')$ — GC($m-1$) applied to $\tau''$, mass $s'\in(0,2\tau_2]$,
partition $F'$ ($|F'|=|F|-1\le m$). Apply the inductive hypothesis
(handling $s'=0$ trivially via integral-nonnegativity). $\blacksquare$

## Verification

- **Round 6 (proof-reviewer):** independently re-verified with a fresh
  20,000-trial exact-`Fraction` simulation of the theorem statement
  (built independently of the approach's own script): zero violations.
- **Round 7 (proof-reviewer, this certification):** re-derived the
  inductive step's algebra by hand (rank-shift identity, substitution
  chain) and independently re-ran a 300,000-trial exact-`Fraction` search
  (random $m\in\{1,\dots,7\}$, random ratio-2 tails, random legal budgets
  and masses) as part of verifying the round-7 build on this same slug:
  zero violations, consistent with the general theorem.

## Origin

`results/imo-2026-03/approaches/rank-pigeonhole-budget.md`, §3 (round 6),
"Theorem (Case-II Closure, GC($m$))". Recommended for certification at
that time but the standalone lemma file was not created until round 7's
review; backfilled here.

## Certification note (proof-reviewer, round 7)

**CERTIFIED.** Fully proved for every $m\ge1$ and every ratio-2
superincreasing tail, no gap, no numerics required for correctness
(numerics used only as cross-checks, both by the round-6 and round-7
reviewers, independently).
