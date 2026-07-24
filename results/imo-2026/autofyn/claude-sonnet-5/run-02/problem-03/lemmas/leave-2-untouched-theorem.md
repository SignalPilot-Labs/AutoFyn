## Statement (CERTIFIED — round 32, proof-reviewer)

**Leave-2-Untouched Theorem.** Fix $m\ge3$ pieces $q_1,\dots,q_m>0$ (only
$q_1$ distinguished as "host"), $T=\sum q_i$. Fix any two distinct indices
$j,k\in\{2,\dots,m\}$ (the two pieces left untouched); let
$\{a_1,\dots,a_{m-3}\}=\{2,\dots,m\}\setminus\{j,k\}$ be the remaining
"pinned" indices. Consider the strategy: cut $q_1$ into $m-3$ fragments
matching $q_{a_1},\dots,q_{a_{m-3}}$ exactly, plus one residual fragment
$\rho:=q_1-\sum_i q_{a_i}$; leave $q_j,q_k$, and every $q_{a_i}$
untouched. This costs $m-3$ cuts and is legal whenever $\rho\ge0$, i.e.
$$2q_1+q_j+q_k\ \ge\ T.$$
Whenever feasible,
$$\Phi\ =\ \frac{T+A(\{\rho,q_j,q_k\})}{2},$$
i.e., writing $x\ge y\ge z$ for $\{\rho,q_j,q_k\}$ sorted descending,
$A(\{\rho,q_j,q_k\})=x-y+z$, giving the explicit 3-branch formula (WLOG
$q_j\ge q_k$):
$$\Phi=\begin{cases}
(T+\rho-q_j+q_k)/2, & \rho\ge q_j\ (\ge q_k),\\
(T+q_j-\rho+q_k)/2, & q_k\le\rho<q_j,\\
(T+q_j-q_k+\rho)/2, & \rho<q_k\ (\le q_j).
\end{cases}$$

## Proof

Direct instantiation of the certified `partition-chamber-theorem` with
partition $B_1=\{1,\dots,m\}\setminus\{j,k\}$ (host $1$) and singletons
$\{j\},\{k\}$ both "untouched": each pinned index $a_i$ contributes a
matched pair $\{q_{a_i},q_{a_i}\}$ (one from $q_1$'s split, one the
original untouched piece), which cancels by `pair-insensitivity-corollary`,
leaving $Q=\{\rho,q_j,q_k\}$. Evaluating the alternating sum of a
3-element multiset sorted descending gives $A=x-y+z$ directly. $\blacksquare$

## Verification

Independently re-derived and re-verified by the proof-reviewer (round
32): built a fresh (not the builder's own) exact-`Fraction` script
comparing the closed-form $\Phi$ formula against a direct full-fragment
multiset simulation (m random in 3..7, random untouched pair $\{j,k\}$,
feasibility-gated) — 1239 feasible trials, zero mismatches.

## Origin / usage

Proved in `results/imo-2026-03/approaches/lp-duality-certificate.md`,
Round 32 build ("R32.1 The Leave-2-Untouched Theorem"). At $m=5$ gives 6
new named chambers ($\binom{4}{2}$ choices of untouched pair). Combined
with the prior chamber family (Bisect-Subset, Double-Bisect-Pin,
Triple-Pin, Double-Pin-Pair, Half-Complement-Pin), the resulting
120-chamber family is proved (same round, see
`n4-120-chamber-family-incomplete-dead-end`, dead-end record in the
approach file) to NOT cover the residual $\mathcal R'$ — a genuine
witness point exists where all 120 chambers simultaneously fail, though
the true optimum there (found by unrestricted numerical optimization,
composition $(2,0,0,0,2)$: simultaneous 3-fragment cuts on $p_1$ and
$p_5$) remains below $a_4T$, so this is not a counterexample to the
conjecture — just evidence the chamber family needs a new member for
this shape.
