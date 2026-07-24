# Last-Element Bound

**Certified:** round 8, from `rank-pigeonhole-budget.md` §5.5. Reviewer
independently re-verified exhaustively (exact `Fraction`, $m\le10$, every
nonempty subset of a ratio-2 tail, script `/tmp/round-8/verify_lemmas.py`):
zero violations.

**Statement.** For any nonempty $X\subseteq\{\tau_1,\dots,\tau_m\}$ (a
sub-collection of a ratio-2 superincreasing tail), $A(X)\ge\min(X)$.

**Proof.** Strong induction on $j=|X|$, peeling the smallest element
$x_j$. If $j$ odd, $x_j$ sits at an odd (positive-sign) rank, so
$A(X)=A(X\setminus\{x_j\})+x_j\ge x_j$. If $j$ even, $x_j$ sits at an even
(negative-sign) rank, so $A(X)=A(X\setminus\{x_j\})-x_j$; by IH (size $j-1$,
odd), $A(X\setminus\{x_j\})\ge x_{j-1}$ (the new min), and by the Ratio-2
Spacing Lemma $x_{j-1}\ge2x_j$, giving $A(X)\ge2x_j-x_j=x_j$.

**Depends on:** `ratio-2-spacing-lemma.md`.

**Scope.** Ladder/ratio-2-specific.
