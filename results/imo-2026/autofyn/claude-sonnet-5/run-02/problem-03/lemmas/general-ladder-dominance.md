# Lemma: General ladder dominance (Lemma 23)

**Source:** `approaches/greedy-halving-adversary.md`, round 10.

**Statement.** For the $n$-ladder ($n\ge1$, $p_i=2^{n+1-i}f(n)$,
$f(n)=1/(2^{n+1}-1)$) and every $i\in\{1,\dots,n+1\}$,
$$p_i \ > \ \sum_{j>i} p_j,\qquad\text{and, for }i\le n,\quad p_i=2p_{i+1}.$$

**Proof.** $p_i=2^{n+1-i}f(n)$ and $\sum_{j=i+1}^{n+1}p_j
=f(n)\sum_{k=0}^{n-i-1}2^k=f(n)(2^{n-i}-1)$ (empty sum $0$ if $i=n+1$).
Since $p_i=2\cdot2^{n-i}f(n)$, the difference is
$p_i-\sum_{j>i}p_j=f(n)\big(2\cdot2^{n-i}-(2^{n-i}-1)\big)=f(n)(2^{n-i}+1)>0$.
The doubling identity $p_i=2^{n+1-i}f(n)=2\cdot2^{n-i}f(n)=2p_{i+1}$ is
immediate from the formula. $\blacksquare$

**Status.** Proved in full, unconditionally, for every $n\ge1$ and every
$i$ (two-line closed-form algebra, no numerics needed, though trivially
spot-checkable).

**Scope.** Generalizes the Key Lemma ("at most one fragment of $p_1$ can
exceed $r$", equivalent to the $i=1$ instance) and `tail-self-similarity`'s
doubling identity (previously only stated for $i=1$) to every level $i$ of
the ladder simultaneously. Used by Proposition 25 (`p2-cut-complement-
branch-closure`) and by Lemma 24 below.

**Certified by:** proof-reviewer, round 10 - independently re-verified (fresh exact-Fraction scripts, corrected for legal-refinement piece-boundary/cut-budget coupling): CERTIFIED.
