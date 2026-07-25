## Odd-Anchor Lemma (negative result)

**Statement.** Suppose $a_1$ is odd. Then $2\notin R(a_1)$, so for every
integer $m>0$, the parity of $m$ is logically irrelevant to whether
$\gcd(m,a_1)>1$: there exist even $m$ with $\gcd(m,a_1)=1$ (e.g. $m=2$)
and even $m$ with $\gcd(m,a_1)>1$ (e.g. $m=2p$ for $p\in R(a_1)$).
Consequently, **no argument based on parity/evenness can ever discharge the
index-$1$ constraint $\gcd(a_n+j,a_1)>1$ for an odd seed** — only an actual
shared odd prime factor of $a_1$ can certify it.

### Proof
$a_1$ odd $\iff 2\nmid a_1 \iff 2\notin R(a_1)$. Since $\gcd(m,a_1)>1$ iff
$m$ shares some prime of $R(a_1)$, and every prime of $R(a_1)$ is odd, the
value of $m\bmod2$ has no bearing on this: $m=2$ is even and coprime to
$a_1$ ($a_1$ odd, $a_1>1$ forces $\gcd(2,a_1)=1$); $m=2p$ (any
$p\in R(a_1)$) is even and shares $p$ with $a_1$. So both truth values of
"$\gcd(m,a_1)>1$" occur among even $m$, and (symmetrically) among odd $m$.
$\blacksquare$

### Consequence (refutation of "parity as a free covering agent")
Any mechanism proposing to use "$m$ is even" (or "the sequence is
eventually all-even") as a free, structural certificate that a candidate
$m$ satisfies the constraint against index $1$ is **impossible** whenever
$a_1$ is odd — this is not merely unproven but a proven impossibility.
Note this does not preclude parity from helping against later indices
$i\ge2$ if $a_i$ happens to be even; it only rules out its use against
$a_1$ itself, which by `lemmas/pairwise-non-coprimality.md` is always one
of the simultaneous constraints, for every $n\ge1$.

### Companion negative fact (also proved, same source)
Even restricted to indices $i\ge2$, "once a term is even, every subsequent
term stays even" is false in general: for $a_1=45=3^2\cdot5$, the terms
$a_2,\dots,a_8 = 48,50,54,60,66,70,72$ are all even (seven consecutive
even terms, independently re-simulated and hand-verified by the
proof-reviewer to match exactly), yet $a_9=75$ is odd (verified: $73,74$
are invalid against index $1$ since $\gcd(73,45)=\gcd(74,45)=1$, while
$75=3\cdot5^2$ satisfies $\gcd(75,a_i)>1$ against every $i=1,\dots,8$).

### Provenance
Proved in `approaches/renormalization-induction-on-seed.md`, §8.3–8.4,
round 6. Independently re-derived (elementary) and the $a_1=45$
counterexample independently re-simulated by the proof-reviewer via exact
integer arithmetic (`sympy.gcd`); sequence matches
$45,48,50,54,60,66,70,72,75,\dots$ exactly.
