## Lemma (Self-Type-Compatibility)

**Statement.** Fix a finite set of primes $Q\supseteq R(a_1)$. For $k\ge1$
write $\tau_k := R(a_k)\cap Q$ (the "$Q$-type" of $a_k$), where $R(m)$
denotes the set of distinct prime divisors of $m$. If $R(a_i)\subseteq Q$
for some index $i$, then
$$\tau_i\cap\tau_j\ne\emptyset\qquad\text{for every }j\ne i.$$

**Corollary ($n=1$ / base-case, unconditional).** Since $Q\supseteq R(a_1)$,
i.e. $R(a_1)\subseteq Q$, taking $i=1$ gives: $\tau_1$ meets $\tau_j$ for
every $j\ne1$, and $\tau_1\cap\tau_1=\tau_1\ne\emptyset$ trivially. Hence
$\tau_1$ meets **every** $\tau_j$, $j\ge1$ — equivalently
$\mathrm{Good}_Q(a_1)$ holds for every admissible finite $Q\supseteq R(a_1)$,
with no dependence on any stabilization index.

**Corollary (propagation).** If $R(a_i)\subseteq Q$ for every $i<n$, then
$\tau_n$ meets every $\tau_i$, $i<n$, regardless of $a_n$'s own type
(apply the Lemma with the roles of $i,j$ exchanged for each $i<n$).

### Proof
By the certified `pairwise-non-coprimality.md`, $\gcd(a_i,a_j)>1$ for all
$i\ne j$, so there is a prime $p$ with $p\mid a_i$ and $p\mid a_j$. Since
$R(a_i)\subseteq Q$, $p\in R(a_i)\subseteq Q$; hence $p\in R(a_i)\cap Q=
\tau_i$ (using $R(a_i)\subseteq Q$ once more, $\tau_i=R(a_i)\cap Q=R(a_i)$).
Also $p\mid a_j$ and $p\in Q$ give $p\in R(a_j)\cap Q=\tau_j$. So
$p\in\tau_i\cap\tau_j$. $\blacksquare$

### Provenance
Independently derived and cross-checked in `approaches/active-set-stabilization.md`
(round 3, "Self-Type-Compatibility Lemma") and
`approaches/state-compactness-pigeonhole.md` (round 3, §9.2, identical
statement and proof). Verified by the proof-reviewer round 3: short, correct,
depends only on `pairwise-non-coprimality.md`.

### Status
Unconditional (no dependence on Hypothesis SS or any self-sufficiency
assumption). Does **not** by itself close the central gap; it is a base-case
/ propagation tool usable by any approach reasoning about $Q$-type
acceptance.
