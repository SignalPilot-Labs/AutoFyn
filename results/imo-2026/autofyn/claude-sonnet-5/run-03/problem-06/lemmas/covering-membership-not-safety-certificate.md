## Lemma (Covering-set membership alone is not a validity certificate)

Let $Q$ be a finite set of primes and let $H(Q) := \{m \in \mathbb Z_{>0} :
p \mid m \text{ for some } p \in Q\}$ (the "hit set"). If a candidate $m$ is
known only to satisfy $m \in H(Q)$ (i.e. $m$ is divisible by *some* prime of
$Q$), this does **not** guarantee $\gcd(m, a_i) > 1$ for every past term
$a_i$ that is itself known only to be divisible by *some* (possibly
different) prime of $Q$. The only bound that **is** provably safe in this
weak-information setting is via $L_Q := \prod_{p \in Q} p$: if $m$ is a
multiple of $L_Q$, then $m$ is divisible by *every* prime of $Q$
simultaneously, and this — not mere $H(Q)$-membership — is what certifies
$\gcd(m, a_i) > 1$ against any $a_i$ divisible by some prime of $Q$.

### Proof (by concrete counterexample)
Take the problem's greedy sequence with $a_1 = 35$, so $Q = P = \{5,7\}$.
Direct computation of the greedy rule gives $a_1=35$, $a_2=40$, $a_3=42$.
$H(Q)$ near $40$ is $\{35,40,42,45,\dots\}$, so $42 \in H(Q)$ (via the prime
$7$). But $\gcd(42,40) = 2$, and $2 \notin Q$: the constraint against
$a_2=40$ is satisfied **only** because $42 = 2\cdot3\cdot7$ carries an extra
factor of $2$, a prime entirely outside $Q$ and incidental to the
$H(Q)$-membership criterion. Consequently, $H(Q)$-membership of $42$ does not
by itself certify $\gcd(42,40)>1$; this instance works only because of the
uncounted factor $2$. In contrast, $L_Q = 35$: had we instead only known that
$40$ is divisible by *some* prime of $Q$ without knowing which, the
guaranteed-safe fallback candidate would have been the next multiple of
$L_Q$'s constituent primes common to *all* prior terms via full
$L_Q$-divisibility, i.e. $45$ (next multiple of $5$, verified $45=9\cdot5$,
$\gcd(45,35)=5$, $\gcd(45,40)=5$) — strictly larger than $42$, showing the
$H(Q)$-based bound and the $L_Q$-based bound genuinely differ and only the
latter is unconditionally valid. $\blacksquare$

### Why this matters
This forecloses a natural but unsound simplification: replacing the safe
"multiple-of-$L_Q$" fallback bound with a weaker "hits $H(Q)$" criterion in
any covering/self-sufficiency argument for the sequence's active prime set.
Any termination or self-sufficiency argument for this problem must track,
for each past term, *which* prime of $Q$ covers it (or otherwise use the
strictly stronger $L_Q$-divisibility criterion), not merely whether it lies
in $H(Q)$.

### Caveat
This is a **negative** result: it rules out one specific (unsound)
simplification. It does **not** by itself make progress toward the central
open gap (self-sufficiency / finiteness of the active prime set) — it only
prevents a future approach from wasting effort on this particular unsound
shortcut.

### Provenance
Proved in `approaches/jacobsthal-covering-bound.md`, Section 1, round 2.
Verified independently by the proof-reviewer via direct computation of the
sequence for $a_1=35$ (confirms $a_1=35,a_2=40,a_3=42$ and the stated gcd
values).
