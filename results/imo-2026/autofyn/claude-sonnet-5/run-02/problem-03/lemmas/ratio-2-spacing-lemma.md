# Ratio-2 Spacing Lemma

**Certified:** round 8, from `rank-pigeonhole-budget.md` §5.3. Reviewer
independently re-verified exhaustively (exact `Fraction`, $m\le10$, every
nonempty subset, script `/tmp/round-8/verify_lemmas.py`): zero violations.

**Statement.** Let $\tau=(\tau_1,\dots,\tau_m)$ be a ratio-2 superincreasing
tail ($\tau_i=2\tau_{i+1}$). For any $X\subseteq\{\tau_1,\dots,\tau_m\}$ with
elements $\nu_1<\dots<\nu_j$ (increasing order), $\nu_{i+1}\ge2\nu_i$ for
every $1\le i<j$, hence $\nu_i\ge2^{i-1}\nu_1$, and (corollary)
$\mathrm{Total}(X)\ge(2j-1)\min(X)$.

**Proof.** If $\nu_i=\tau_l,\nu_{i+1}=\tau_{l'}$ with $l'<l$ (smaller index =
larger value), $\nu_{i+1}/\nu_i=2^{l-l'}\ge2$ since $l>l'$ are distinct
integers. Iterate. The Total bound follows since each of the $j-1$ larger
elements is $\ge2\min(X)$.

**Scope.** Ladder/ratio-2-specific (uses $\tau_i=2\tau_{i+1}$).
