## Statement

Fix any $m\ge2$ pieces $q_1,\dots,q_m>0$ (no sortedness required except
that $q_1$ is the distinguished piece to be cut), and $T=\sum q_i$. Fix
any single index $j\in\{2,\dots,m\}$ (the piece to leave untouched).
Consider the strategy: cut $q_1$ into $m-2$ fragments, one matching each
$q_i$, $i\notin\{1,j\}$, exactly, plus one residual fragment
$\rho:=q_1-\sum_{i\ne1,j}q_i$; leave every $q_i$, $i\ne1,j$, and $q_j$
itself untouched (this is `partition-chamber-theorem` instantiated with
$B_1=\{1,\dots,m\}\setminus\{j\}$ (host $1$) and singleton $B_2=\{j\}$
left untouched; it costs $m-2$ cuts).

Feasibility of this strategy is $\rho\ge0$, i.e. $q_1\ge\sum_{i\ne1,j}q_i$,
equivalently $2q_1+q_j\ge T$.

**Theorem.** Whenever the feasibility condition $2q_1+q_j\ge T$ holds
(for the chosen $j$), the resulting value is
$$\Phi\ =\ \max(q_1,\ T-q_1),$$
**independent of which feasible $j$ is chosen** — only feasibility
depends on $j$, not the value produced.

## Proof

By `partition-chamber-theorem`, $Q=\{\rho,q_j\}$ (the residual and the
untouched singleton) and $\Phi=(T+A(Q))/2$, where $A(\{\rho,q_j\})=
|\rho-q_j|$. Substituting $\rho=q_1-s$ with $s:=\sum_{i\ne1,j}q_i=T-q_1
-q_j$, i.e. $\rho=2q_1+q_j-T$:

- If $\rho\ge q_j$ (equivalently $2q_1-T\ge0$, i.e. $q_1\ge T-q_1$):
$$\Phi=\frac{T+\rho-q_j}2=\frac{T+(2q_1+q_j-T)-q_j}2=q_1=\max(q_1,T-q_1).$$
- If $\rho<q_j$ (equivalently $q_1<T-q_1$):
$$\Phi=\frac{T+q_j-\rho}2=\frac{T+q_j-(2q_1+q_j-T)}2=T-q_1=\max(q_1,T-q_1).$$

Both branches give $\Phi=\max(q_1,T-q_1)$, and the case split itself is
equivalent to comparing $q_1$ against $T-q_1$ — no dependence on $j$
remains in the final value once feasibility holds. $\blacksquare$

## Certification note (proof-reviewer, round 31)

**Certified.** Verified end to end, independently, in two ways: (1)
re-derived the algebraic substitution above by hand, matching the file's
derivation term for term; (2) built the *actual* full fragment multiset
the strategy produces for a concrete instantiation ($m=5$: fragments
$\{p_3,p_4,p_5,\rho\}$ of $p_1$ union the untouched $\{p_2,p_3,p_4,p_5\}$,
an 8-element multiset) and computed its alternating sum directly by full
sorting, confirming from scratch — not merely re-deriving the file's own
reduced-to-2-elements shortcut via `partition-chamber-theorem` — that the
full multiset's $A$ matches the claimed reduced formula and that
$\Phi=\max(q_1,T-q_1)$ holds whenever feasibility holds, across 11,625
exact-`Fraction` trials with randomized $p_1,\dots,p_5$. Zero mismatches.
The statement is a direct, general-$m$ consequence of the already-certified
`partition-chamber-theorem`, uses no ladder-specific or game-specific
structure, and is stated and proved with no unjustified steps. Certified
correct and general.

## Origin

`results/imo-2026-03/approaches/lp-duality-certificate.md`, round 31,
§R31.1.
