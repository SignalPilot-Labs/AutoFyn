# Exchange-Smoothing Vertex-Maximization Proposition

**Certified:** round 8, from `rank-pigeonhole-budget.md` §5.1. Reviewer
independently checked the exchange argument line-by-line and confirmed it is
a valid dualization (max instead of min) of the already-certified
`vertex-minimum-theorem`'s exchange mechanism — no min-specific step is used.

**Statement.** Fix $m\ge1$, a finite reference set $\tau=(\tau_1,\dots,\tau_m)$
(need not be ratio-2; the proof never uses that structure), a mass $s>0$, and
a part-budget $k\ge1$. Let
$$\mathcal P=\Big\{(f_1,\dots,f_k): f_i\ge0,\ \textstyle\sum f_i=s,\ f_i\le\tau_1\ \forall i\Big\}.$$
Then the maximum of $E(F\cup\tau)$ (the even-sorted-rank sum) over
$F\in\mathcal P$ is attained at some $F^\dagger\in\mathcal P$ of the
restricted form: for some $0\le p\le k$, $p$ coordinates are individually
pinned to reference values $\tau_{l_1},\dots,\tau_{l_p}\in\{\tau_1,\dots,\tau_m\}$
(repetition allowed), and the remaining $k-p$ coordinates (if any) all equal
one common tied value $v\ge0$.

**Proof sketch (full proof in the approach file).** $E(\cdot\cup\tau)$ is
continuous on the compact polytope $\mathcal P$, so a maximizer exists. If
two coordinates are "free" (unpinned, distinct values), a small local
perturbation that increases one and decreases the other by equal amounts
keeps every rank fixed in a small enough neighbourhood (since all values
involved are pairwise distinct there), so $E$ changes affinely in the
perturbation parameter; either a strict increase is available (contradicting
maximality) or the direction is flat, in which case pushing to the
neighbourhood's boundary (hitting $0$, $\tau_1$, some $\tau_l$, or another
coordinate) does not decrease $E$ and strictly reduces the number of
distinct free values. This terminates in finitely many steps at a
configuration with at most one free value, shared by all unpinned
coordinates — the claimed form.

**Scope.** General: applies to any fixed finite reference set and any mass/
part-budget, not ladder-specific.

**Reused by:** `case-i-closure-theorem.md` (below).
