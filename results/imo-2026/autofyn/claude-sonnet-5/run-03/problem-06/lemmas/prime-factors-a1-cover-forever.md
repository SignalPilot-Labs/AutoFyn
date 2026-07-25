## Lemma (The prime factors of $a_1$ cover every term, unconditionally)

Let $(a_n)_{n\ge1}$ be the problem's greedy sequence and let $P := R(a_1)$
(the set of distinct prime divisors of $a_1$). Then for **every** $n \ge 1$,
$$R(a_n) \cap P \neq \emptyset,$$
i.e. every term of the sequence, with no exception and no pigeonhole
argument required, shares a prime factor with $a_1$.

### Proof
For $n=1$ this is immediate: $R(a_1) \cap P = P \neq \emptyset$ (as $a_1>1$
has at least one prime factor). For $n \ge 2$, the defining property of the
sequence, applied at step $n-1 \ge 1$ with constraint index $i=1$, requires
$\gcd(a_n, a_1) > 1$. Hence $a_n$ shares a prime factor with $a_1$, i.e. some
prime of $P$ divides $a_n$. $\blacksquare$

### Remark
This is strictly stronger, and requires no pigeonhole, compared to the
"every term meets the recurring set $S$" lemma
(`lemmas/every-term-meets-recurring-set.md`): here the covering set $P$ is
explicit, finite, and known the instant $a_1$ is fixed, whereas $S$ is only
known nonempty via an infinite-tail pigeonhole argument. $P$ is a genuine
witness that a finite covering set exists unconditionally; it is **not**,
by itself, known to be *self-sufficient* (see the Caveat below).

### Caveat (do not overclaim from this lemma)
This lemma shows a finite covering set exists trivially — it does **not**
resolve the central open gap of the problem, which is whether some finite
set of primes $Q \supseteq P$ eventually governs *validity* of every
candidate exactly (the "self-sufficiency" hypothesis used across the
population, e.g. Hypothesis SS in `active-set-stabilization.md` and
`state-compactness-pigeonhole.md`). Additional primes outside $P$ are, in
fact, recruited into the eventual period $L$ in computed examples (e.g.
$a_1=35$ eventually incorporates the prime $2$ into $L=210$), precisely
because $P$-membership alone is not a valid minimality certificate — see
`lemmas/covering-membership-not-safety-certificate.md`.

### Provenance
This fact already appears, unlabeled, as the internal "Fact" inside the
proof of `lemmas/bounded-gap-via-rad-a1.md` (round 1, growth-rate-contradiction).
It was independently re-derived and used explicitly as a standalone
statement, this round, in both `approaches/jacobsthal-covering-bound.md`
(Section 0, "unconditional covering by $P$") and
`approaches/state-compactness-pigeonhole.md` (Lemma $Q_0$, Section 0).
Certified by the proof-reviewer, round 2, as a standalone lemma so it can be
cited directly without pulling in the whole bounded-gap derivation.
