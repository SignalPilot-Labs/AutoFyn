## $\Lambda$-stabilization Lemma

**Statement.** Let $R:=\mathrm{rad}(a_1)$, $U:=\{p\text{ prime}:p\le R\}$
(fixed, finite, $|U|=\pi(R)$), and for $n\ge1$
$$\Lambda_n:=\bigcup_{i=1}^{n-1}\{p\text{ prime}:p\mid\gcd(a_i,a_{i+1})\}$$
(so $\Lambda_1=\emptyset$). By the certified `adjacent-link-lemma.md`,
$\Lambda_n\subseteq U$ for every $n$, and $(\Lambda_n)$ is monotone
non-decreasing. Then there is an index $n_0\le\pi(R)+1$ and a fixed set
$\Lambda\subseteq U$ with $\Lambda_n=\Lambda$ for every $n\ge n_0$.

**Proof.** $(|\Lambda_n|)$ is a non-decreasing integer sequence, starting
at $0$, bounded above by $\pi(R)$; it can strictly increase at most
$\pi(R)$ times, so some $n_0\le\pi(R)+1$ has
$|\Lambda_{n_0}|=|\Lambda_{n_0+1}|=\cdots$. Set $\Lambda:=\Lambda_{n_0}$.
For $n\ge n_0$: $\Lambda_{n_0}\subseteq\Lambda_n$ (monotonicity) and
$|\Lambda_{n_0}|=|\Lambda_n|$; two finite sets with one contained in the
other of equal cardinality are equal, so $\Lambda_n=\Lambda$.
$\blacksquare$

### Why this is not blocked by the certified negative result `monotonicity-obstruction.md`
That lemma rules out arguments of the shape "a *specific state*
$\sigma(n)$ recurs." This lemma claims only that a monotone
non-decreasing sequence of subsets of a *fixed finite universe* eventually
stops growing — no recurrence of any individual index's data is claimed.
The key enabling fact, absent for $Q$ or $S$ directly, is that
$\Lambda_n$'s universe $U=\{p\le R\}$ is fixed and bounded from the start
(a consequence of the Adjacent-Link Lemma).

### Provenance
`approaches/jacobsthal-covering-bound.md`, round 3, "$\Lambda$-stabilization
Lemma". Verified by the proof-reviewer round 3: standard bounded-monotone
argument, correct.

### Status
Unconditional. Does **not** by itself bound the central active prime set
$Q$: see the certified `finite-subtraction-vacuous.md` for a proof that
splitting $Q=\Lambda\cup(Q\setminus\Lambda)$ gives no reduction in
difficulty, since $\Lambda$'s finiteness does not confine
$Q\setminus\Lambda$ to any fixed universe.
