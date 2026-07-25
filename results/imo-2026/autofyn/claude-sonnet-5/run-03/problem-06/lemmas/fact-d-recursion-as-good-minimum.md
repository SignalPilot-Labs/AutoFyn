## Fact D (recursive step $=$ static $\mathrm{Good}$-minimum, every $n\ge1$)

**Statement.** For $m>1$ define $\mathrm{Good}(m):\iff \gcd(m,a_i)>1$ for
every $i\ge1$ with $a_i<m$. Then for every $n\ge1$,
$$a_{n+1} = \min\{m>a_n : \mathrm{Good}(m)\}.$$

**Proof.** For any $m$ with $a_n<m\le a_{n+1}$, the set of indices $i$
with $a_i<m$ is exactly $\{1,\dots,n\}$: for $i\le n$, $a_i\le a_n<m$
(monotonicity, `existence.md`); for $i\ge n+1$, $a_i\ge a_{n+1}\ge m$,
with equality excluded from "$a_i<m$" (strict). Hence on this range,
$\mathrm{Good}(m)$ coincides pointwise with the recursive acceptance test
"$\gcd(m,a_i)>1$ for $i=1,\dots,n$", which is exactly what the problem's
recursive definition tests when producing $a_{n+1}$ as the least such $m$
exceeding $a_n$. $\blacksquare$

### Provenance
`approaches/state-compactness-pigeonhole.md`, round 3, §9.1 ("Fact D").
Verified by the proof-reviewer round 3: elementary, self-contained,
depends only on `existence.md`.

### Status
Unconditional, holds for every $n\ge1$ with no restriction. Slightly more
elementary than the earlier-certified `set-theoretic-acceptance-characterization.md`
(Proposition B): no restriction to $m>a_1$, purely index-local. Used as
the base fact in `reduction-lemma-ss1-vs-unified-claim.md`.
