## Lemma (Minimal-type reduction for hitting families of subsets)

Let $Q$ be a finite set and $\mathcal F \subseteq 2^Q \setminus \{\emptyset\}$
a family of nonempty subsets. Say $r$ (an element, or more generally a
subset of $Q$ representing "the primes of $Q$ dividing some integer $m$")
*meets* $\tau \in \mathcal F$ if $r \cap \tau \neq \emptyset$. Then $r$ meets
every $\tau \in \mathcal F$ if and only if $r$ meets every $\subseteq$-minimal
element of $\mathcal F$.

### Proof
($\Leftarrow$) Suppose $r$ meets every minimal element of $\mathcal F$, and
let $\tau \in \mathcal F$ be arbitrary. Since $\mathcal F$ is a finite
nonempty poset under $\subseteq$, $\tau$ contains some $\subseteq$-minimal
element $\tau_0 \in \mathcal F$ with $\tau_0 \subseteq \tau$. Since $r$ meets
$\tau_0$ (shares an element with it) and $\tau_0 \subseteq \tau$, that shared
element also lies in $\tau$, so $r$ meets $\tau$.

($\Rightarrow$) Immediate: minimal elements of $\mathcal F$ are themselves
elements of $\mathcal F$. $\blacksquare$

### Provenance
Proved in `approaches/active-set-stabilization.md`, round 2, as "Lemma M."
General finite-poset fact, no dependence on imo-2026-06's specific sequence.
Verified by the proof-reviewer, round 2: correct as stated (a standard
"minimal elements suffice for an upward-closed-hitting test" fact).

### Caveat
Applying this reduction to the sequence's accumulating type family
$\mathcal T_n$ shows the *minimal*-type set $\mathcal T_n^\ast$ can stabilize
strictly earlier than $\mathcal T_n$ itself, but the Monotonicity Obstruction
Lemma (`lemmas/monotonicity-obstruction.md`) applies verbatim to
$\mathcal T_n^\ast$ as well (it is still non-decreasing in $n$), so this
reduction alone does **not** close the prefix-extension gap (periodicity
from $n=1$) for imo-2026-06 — it only narrows the residual gap in one worked
example (from index 5 down to index 3, out of a target of index 1).
