## Bounded-Lookahead Insufficiency (negative)

**Statement.** For $a_1=65=5\cdot13$: the Third-Term Dichotomy Lemma
correctly predicts $p=5$ wins the race at step 3 ($a_3=75$), yet direct
computation shows the lock already breaks at step 4 ($a_4=78\ne
a_3+5=80$). Consequently, no induction scheme that certifies "$p$ locked
forever" via a *fixed, bounded* number of look-ahead race comparisons
(checking only $a_1,\dots,a_j$ for $j$ bounded independent of how far the
sequence has run) can be correct in general — for any fixed bound $k\ge1$
up to at least $k=2$, an explicit counterexample exists.

**Proof.** By `third-term-dichotomy-lemma.md`, $a_3=75$ for $a_1=65$.
Direct computation of $a_4$: candidates $76=4\cdot19$ ($\gcd(76,65)=1$,
invalid), $77=7\cdot11$ ($\gcd(77,65)=1$, invalid), $78=2\cdot3\cdot13$
($\gcd(78,65)=13>1$, $\gcd(78,70)=2>1$, $\gcd(78,75)=3>1$: valid). So
$a_4=78$, not $a_3+5=80$: the lock on $p=5$ breaks at step 4, one step
after surviving the step-3 race. $\blacksquare$

### Provenance
Proved in `approaches/renormalization-induction-on-seed.md` (round 4/5,
§4.3, §5). Independently re-verified by the proof-reviewer (round 4) via
exact-integer simulation: the sequence for $a_1=65$ is exactly
$65,70,75,78,80,90,100,105,\dots$, confirming $a_3=75$, $a_4=78$.

### Status
Unconditional, negative result. Standing counterexample against any
future "check $k$ steps ahead" proposal for certifying permanent prime
locking in this problem's greedy sequence, for fixed $k$ at least up to
$k=2$. Consonant with (but independently derived from, on a different
instance) `windowed-epsilon-automaton-failure.md`, which shows no bounded
window of a fixed relative-gap statistic determines the exceptional-step
indicator in general — together the two findings support the diagnosis
that whatever measure eventually certifies periodicity must encode
information that grows with the sequence, not a fixed-size window of
recent history.
