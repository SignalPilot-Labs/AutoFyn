## Chain-Transitivity Obstruction (negative, purely set-theoretic)

**Statement.** Pairwise-consecutive nonempty intersection of a chain of
sets $\sigma_1,\dots,\sigma_m$ (i.e. $\sigma_k\cap\sigma_{k+1}\ne
\emptyset$ for every $1\le k<m$) does **not** imply $\sigma_1\cap
\sigma_m\ne\emptyset$.

**Proof (counterexample).** $\sigma_1=\{1,2\}$, $\sigma_2=\{2,3\}$,
$\sigma_3=\{3,4\}$: $\sigma_1\cap\sigma_2=\{2\}\ne\emptyset$ and
$\sigma_2\cap\sigma_3=\{3\}\ne\emptyset$, yet $\sigma_1\cap
\sigma_3=\emptyset$. $\blacksquare$

This is confirmed to be an actively-occurring pattern for this problem's
own sequences, not merely a hypothetical concern: for $a_1=15$, writing
$\sigma_n:=R(a_n)\cap[2,R]$, adjacent types $\sigma_n,\sigma_{n+1}$ are
disjoint at $50$ of the first $100$ steps (a concrete instance:
$\tau_2=\{3\}$, $\tau_3=\{5\}$ are disjoint even though the underlying
$\sigma_2,\sigma_3$ do intersect via an outside connecting prime).

### Provenance
Proved in `approaches/state-compactness-pigeonhole.md` (round 4, §11.5(b)).
Independently re-verified by the proof-reviewer (round 4): the
set-theoretic counterexample is elementary and correct; it does not
depend on any property of this problem's sequence.

### Status
Unconditional, negative result (pure set theory). Standing warning against
any future attempt to prove a hitting-set/covering claim for this problem
by inducting on the index gap $d=j-i$ via chaining consecutive
intersections (e.g. of `adjacent-link-lemma.md` witnesses) — such chaining
alone cannot conclude non-adjacent pairs intersect, and must be
supplemented with additional information.
