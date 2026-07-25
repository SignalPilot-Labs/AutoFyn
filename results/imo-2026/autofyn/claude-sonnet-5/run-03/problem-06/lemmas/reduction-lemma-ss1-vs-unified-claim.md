## Reduction Lemma: Hypothesis SS$(Q,1)$ $\iff$ every accepted term is $Q$-Good

**This is the key structural result of round 3** — it proves that the two
gaps the population had tracked separately since round 1/2 (Gap 1:
self-sufficiency of a finite active prime set $Q$ for *some* transient
index $n^*$; Gap 2: extending eventual periodicity down to $n=1$) are, once
$n^*=1$ is targeted directly, **exactly the same open statement**.

### Setup
Fix a finite $Q\supseteq R(a_1)$. For $m>1$, let $R(m)$ be its prime
divisors. Write $\tau_i:=R(a_i)\cap Q$, $\mathcal T:=\{\tau_i:i\ge1\}$
(finite since $Q$ is finite), and
$$\mathrm{Good}_Q(m):\iff R(m)\cap Q\text{ meets every }\tau\in\mathcal T.$$

### Statement
The following are equivalent:

(a) **Hypothesis SS$(Q,1)$**: for every $n\ge1$,
$a_{n+1}=\min\{m>a_n:\mathrm{Good}_Q(m)\}$.

(b) **Unified Central Claim for $Q$**: for every $n\ge1$,
$\mathrm{Good}_Q(a_n)$ holds (equivalently: $\mathcal T$ is a pairwise
intersecting family, realized by *every* actual term of the sequence).

### Proof

**(a)$\Rightarrow$(b).** For $n=1$: $\mathrm{Good}_Q(a_1)$ holds
unconditionally by the certified `self-type-compatibility.md` Corollary
(no need to invoke (a)). For $n=k+1\ge2$: by (a) at index $k$,
$a_{k+1}=\min\{m>a_k:\mathrm{Good}_Q(m)\}$; this set is nonempty (it
contains arbitrarily large multiples of $L:=\prod_{q\in Q}q$, since
$\mathrm{GoodRes}(Q)\ne\emptyset$ — the residue $0$ always qualifies), so
its minimum exists and, being the minimum of a set defined by
$\mathrm{Good}_Q$, trivially satisfies $\mathrm{Good}_Q$. Hence
$\mathrm{Good}_Q(a_{k+1})$ holds.

**(b)$\Rightarrow$(a).** Fix $n\ge1$; let
$\mu:=\min\{m>a_n:\mathrm{Good}_Q(m)\}$ (exists, same nonemptiness
argument). By `soundness-and-exact-correctness.md`'s underlying fact
(every $Q$-Good candidate is a valid candidate for the true recursion,
i.e. shares a prime of $Q$ with each $a_i$, $i\le n$, hence with each
earlier term), every candidate counted in $\mu$'s minimum is also a
candidate counted in $a_{n+1}=\min\{m>a_n:\mathrm{Good}(m)\}$ (writing
$\mathrm{Good}(m)$ for the raw recursive test at step $n$), so $\mu$
ranges over a subset of the latter's candidates, giving $\mu\ge a_{n+1}$.
Conversely, by (b), $\mathrm{Good}_Q(a_{n+1})$ holds, and $a_{n+1}>a_n$, so
$a_{n+1}$ is itself a candidate for $\mu$, giving $\mu\le a_{n+1}$. Hence
$\mu=a_{n+1}$. As $n\ge1$ was arbitrary, (a) holds for all $n$.
$\blacksquare$

### Provenance
`approaches/state-compactness-pigeonhole.md`, round 3, §9.3 ("Reduction
Lemma"). Verified independently by the proof-reviewer round 3: re-derived
both directions from scratch, confirmed no circularity (the definition of
$\mathcal T$ uses the *actual*, already well-defined infinite sequence
$(a_n)$ — legitimate as a mathematical existence statement, not an
assumption of periodicity) and confirmed Fact D (the recursive step
literally equals $\min\{m>a_n:\mathrm{Good}(m)\}$ for every $n\ge1$,
`approaches/state-compactness-pigeonhole.md` §9.1) is used correctly.

### Status and what it does NOT establish
Unconditional equivalence — no gap in the logic. **It does not prove that
a finite $Q$ satisfying (b) exists.** The central open gap of the whole
problem is now precisely: *does there exist a finite set of primes $Q$
such that every two terms $a_i,a_j$ of the sequence share a prime factor
lying in $Q$* (equivalently, statement (b) for some $Q$)? This is
unproved by any approach in the population as of round 3; strong
numerical evidence (not proof) supports it — see
`approaches/state-compactness-pigeonhole.md` §9.5.
