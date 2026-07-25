## Lemma (Monotonicity obstruction to prefix-inclusive state-pigeonhole arguments)

Let $\mathcal T_n$ ($n \ge 1$) be any set-valued sequence that is
non-decreasing under $\subseteq$ (e.g. $\mathcal T_n = \{\tau_1,\dots,\tau_n\}$
for some accumulating labels $\tau_i$), taking values in a common finite
universe, and let $\mathcal T := \bigcup_{n\ge1} \mathcal T_n$. Suppose
$\mathcal T_1 \subsetneq \mathcal T$ (i.e. not every value that will ever
occur has already occurred at index $1$). Then for **every** index $m$ with
$\mathcal T_m = \mathcal T$ (in particular, every index in an eventually
stable regime), $\mathcal T_m \neq \mathcal T_1$.

### Proof
By non-decreasingness, $\mathcal T_1 \subseteq \mathcal T_n$ for every
$n \ge 1$, hence $\mathcal T_1 \subseteq \mathcal T_m = \mathcal T$. By
hypothesis $\mathcal T_1 \subsetneq \mathcal T$, so $\mathcal T_1 \neq
\mathcal T = \mathcal T_m$. $\blacksquare$

### Consequence
Consider any enlarged pigeonhole state $\sigma(n) := (x_n, \mathcal T_n)$
(residue, or any other finite-valued component $x_n$, paired with
$\mathcal T_n$). As long as $\mathcal T_1 \subsetneq \mathcal T$, $\sigma(1)$
can **never** equal $\sigma(m)$ for any $m$ with $\mathcal T_m = \mathcal T$
— in particular it cannot coincide with any state in an eventually periodic
regime reached once $\mathcal T_n$ has stabilized. Consequently, **no**
pigeonhole argument phrased in terms of such an enlarged state (regardless of
which specific indices $\ge$ the stabilization point are compared to index
$1$) can ever certify that a periodicity relation involving index $1$ itself
holds, whenever $\mathcal T$ takes more than one value along the way.

### Caveat
This lemma only rules out **this specific family** of arguments (pigeonhole
on a state that includes a monotonically accumulating set component). It
does **not** show that the underlying periodicity-from-index-1 claim is
false — indeed, for imo-2026-06 direct computation ($a_1=15$) confirms the
target periodicity genuinely holds from $n=1$ even though the relevant
accumulating type-set $\mathcal T_n$ only stabilizes at $n=5$. It only shows
that *this type of argument* cannot be the mechanism; some other argument
(not state-recurrence based) is needed.

### Provenance
Proved in `approaches/active-set-stabilization.md`, round 2, in response to
the outline-reviewer's identification of a pigeonhole fallacy in the round-1
write-up of the same approach. General (not specific to imo-2026-06).
Verified by the proof-reviewer, round 2: the proof is an immediate
consequence of monotonicity and is correct as stated.
