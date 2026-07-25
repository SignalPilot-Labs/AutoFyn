## Lemma (Soundness of the $Q$-rule) and Exact-Correctness Criterion

Fix any finite set of primes $Q\supseteq R(a_1)$ (unconditional — no
assumption that $Q$ is "self-sufficient"). For $n\ge1$ write
$\tau_i:=R(a_i)\cap Q$ and define the **$Q$-prediction**
$$\widehat a_{n+1} := \min\{m>a_n : R(m)\cap Q \text{ meets } \tau_i
\text{ for every } i=1,\dots,n\}.$$
(Well-defined: this set contains every sufficiently large multiple of
$L:=\prod_{q\in Q}q$, and $\tau_i\ne\emptyset$ for every $i\ge1$ by the
certified `prime-factors-a1-cover-forever.md`.)

### Soundness Lemma
For every finite $Q\supseteq R(a_1)$ and every $n\ge1$: $\widehat
a_{n+1}\ge a_{n+1}$ (the true term) — the $Q$-rule never over-accepts a
candidate, so it can only overshoot, never undershoot, the true minimum.

*Proof.* Any candidate $m$ counted in $\widehat a_{n+1}$'s minimum
satisfies $m>a_n$ and, for each $i\le n$, shares a prime $p\in Q$ with
$a_i$ (since $R(m)\cap Q$ meets $\tau_i=R(a_i)\cap Q$); hence
$\gcd(m,a_i)\ge p>1$ for every $i=1,\dots,n$, so $m$ is a valid candidate
for the problem's actual recursive definition of $a_{n+1}$. Since
$a_{n+1}$ is the minimum over *all* valid candidates and $\widehat
a_{n+1}$ is a particular one, $a_{n+1}\le\widehat a_{n+1}$. $\blacksquare$

### Exact-Correctness Criterion
For fixed $n\ge1$ and finite $Q\supseteq R(a_1)$: $\widehat a_{n+1}=a_{n+1}$
**iff** $a_{n+1}$ itself is $Q$-accepted, i.e. $R(a_{n+1})\cap Q$ meets
$\tau_i$ for every $i=1,\dots,n$.

*Proof.* ($\Rightarrow$) If $\widehat a_{n+1}=a_{n+1}$, then $a_{n+1}$
attains the minimum defining $\widehat a_{n+1}$, hence is one of the
candidates counted, i.e. satisfies the $Q$-hitting condition.
($\Leftarrow$) If $R(a_{n+1})\cap Q$ meets every $\tau_i$, $i\le n$, and
$a_{n+1}>a_n$, then $a_{n+1}$ is itself a candidate for $\widehat
a_{n+1}$'s minimum, so $\widehat a_{n+1}\le a_{n+1}$. Combined with
Soundness ($a_{n+1}\le\widehat a_{n+1}$), equality follows. $\blacksquare$

### Provenance
`approaches/active-set-stabilization.md`, round 3, "Soundness Lemma" and
"Exact-Correctness Criterion". Verified by the proof-reviewer round 3:
direct unpacking of the definitions, no other lemma needed beyond
`prime-factors-a1-cover-forever.md`.

### Status
Unconditional. Reduces "the $Q$-rule matches the truth at step $n$" to a
single concrete divisibility statement about the actual term $a_{n+1}$;
does not by itself establish that statement for any $n$ or $Q$ (that is
the central open gap, tracked separately).
