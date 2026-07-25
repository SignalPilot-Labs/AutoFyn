## Lemma (Eventual periodicity, CONDITIONAL on Hypothesis SS — NOT unconditional)

**This lemma is conditional and does not by itself advance the problem's
central gap.** It is certified only as reusable shared machinery once its
hypothesis is discharged; the hypothesis itself (a form of "self-sufficiency"
of a finite active prime set) is the central open gap of imo-2026-06 and is
**not** proved by any approach in the population as of round 2.

### Hypothesis SS (self-sufficiency)
There is a finite set of primes $Q \supseteq R(a_1)$ and an index $n^*$ such
that, writing $L := \prod_{q \in Q} q$ and, for $m > 1$,
$\mathrm{Good}_Q(m) :\iff R(m) \cap Q$ meets $R(a_i) \cap Q$ for every $i \ge 1$
with $a_i < m$, we have: for every $n \ge n^*$,
$$a_{n+1} = \min\{\, m > a_n : \mathrm{Good}_Q(m) \,\}.$$

### Statement
Under Hypothesis SS, there exist $T \ge 1$ and an index $m_0 \ge n^*$ such
that
$$a_{n+T} = a_n + L' \quad \text{for every } n > m_0,$$
where $L'$ is a positive multiple of $L$ (in fact $L' = L$ when $T$ is taken
to be $|\mathrm{GoodRes}(Q)|$, the number of residues mod $L$ satisfying
$\mathrm{Good}_Q$).

### Proof
Two independent derivations exist in the population, both verified correct
by the proof-reviewer and cross-checking each other:

1. **Orbit-pigeonhole route** (`approaches/active-set-stabilization.md`,
   Theorem A): reduces to a deterministic map $g$ on the finite set
   $\mathbb Z/L\mathbb Z$ acting on residues $a_n \bmod L$ for $n \ge n^*$;
   pigeonhole finds a genuine coincidence $r_p = r_q$ among *some* pair of
   indices $p < q \ge n^*$ (not necessarily including $n^*$ itself), and
   induction propagates $a_{p+j+T} = a_{p+j}+L'$ for all $j \ge 0$ with
   $T = q-p$, $L' = a_q - a_p$.
2. **Residue-class-union route**
   (`approaches/state-compactness-pigeonhole.md`, using
   `lemmas/set-theoretic-acceptance-characterization.md` and
   `lemmas/periodicity-of-residue-class-union.md`): shows directly that
   $A \cap (a_{n^*}, \infty)$ equals a set of the form
   $\{m > a_{n^*} : m \bmod L \in \mathrm{GoodRes}(Q)\}$, then applies the
   general residue-class-union periodicity lemma to conclude exact
   periodicity of this tail with $T = |\mathrm{GoodRes}(Q)|$, $L' = L$.

Both routes are correct (verified independently); the second is shorter and
gives $L'=L$ exactly rather than merely a multiple of $L$.

### Caveats (mandatory reading before reuse)
1. **Hypothesis SS is unproved.** No approach in the population has shown
   any finite $Q$ and index $n^*$ satisfying it. This is the single central
   open gap of imo-2026-06.
2. **Only the tail, not the whole sequence.** Even granting Hypothesis SS,
   this lemma gives periodicity only for $n$ beyond a transient cutoff
   $m_0 \ge n^*$, not for all $n \ge 1$ as the problem requires. Extending
   to all $n \ge 1$ is a second, separate open gap (flagged independently by
   both provenance approaches); the "Monotonicity Obstruction Lemma"
   (`lemmas/monotonicity-obstruction.md`) rules out an entire natural family
   of fixes for this second gap.
3. Do not cite this file as closing any part of the problem; it exists so
   that whichever future approach discharges Hypothesis SS does not need to
   re-derive the periodicity-of-the-tail step from scratch.

### Provenance
`approaches/active-set-stabilization.md` (Theorem A, round 2) and
`approaches/state-compactness-pigeonhole.md` (Theorem of Section 5, round
2), independently derived, cross-checked, both verified correct by the
proof-reviewer round 2.
