## Statement

Fix $n$ and the case-(b2) setting of `p-space-chamber-vertex-theorem`. For
the specific purpose of proving the one-sided bound
$\Phi_{\min}(p)\le a_nT(p)$ (as opposed to characterizing the true global
minimizer everywhere), the type-optimality condition (c) of
`p-space-chamber-vertex-theorem`'s item 1 — that a candidate type $\tau$
must be the actual global minimizer at $p$, i.e. beat every competing type
$\tau'$ — is **not needed**.

Precisely: fix any full type $(\mathbf c,\tau,\pi)$ with joint
mass-conservation matrix $M(\tau)$ invertible (not necessarily the type
realized by the true minimizer anywhere), and let
$U^{\mathrm{feas}}(\mathbf c,\tau,\pi)\subseteq\mathcal P$ be the set of $p$
satisfying only conditions (a) (feasibility, $F^\tau_{i,l}(p)\ge0$ for every
slot) and (b) (order, the slots respect $\pi$'s ranking) — dropping (c)
entirely. Then for every $p\in U^{\mathrm{feas}}(\mathbf c,\tau,\pi)$, the
configuration $F^\tau(p)$ is a genuine legal Xiang-Yu response (by (a)+(b)
alone, exactly as in the ($\Leftarrow$) direction of
`p-space-chamber-vertex-theorem`'s Lemma R22.1), whose value is the affine
candidate $\ell_\tau(p):=T(p)-E(F^\tau(p))$ — a valid, if not necessarily
tight, upper bound:
$$\Phi_{\min}(p)\ \le\ \ell_\tau(p)\qquad\text{for every }p\in U^{\mathrm{feas}}(\mathbf c,\tau,\pi).$$

Since $U^{\mathrm{feas}}$ is (by the same argument used for $U$ itself,
using only (a)+(b)) a polyhedron cut out by finitely many affine
inequalities, and $g_\tau(p):=a_nT(p)-\ell_\tau(p)$ is affine, the identical
vertex argument of the Chamber-Vertex Theorem (item 2) applies verbatim
with $U^{\mathrm{feas}}$ in place of $U$: $g_\tau\ge0$ throughout
$\overline{U^{\mathrm{feas}}\cap\mathrm{Box}\cap\{T=1\}}$ iff $g_\tau\ge0$
at its finitely many vertices.

## Consequence (what this buys)

Closing case (b2) no longer requires characterizing the *true* minimizing
type at every point of the box (the hard, competition-dependent condition
(c)) — it suffices to exhibit a **finite covering family** of types
$\tau_1,\dots,\tau_N$ such that:
1. each $U^{\mathrm{feas}}(\tau_i)\cap\mathrm{Box}$ individually satisfies
   $g_{\tau_i}\ge0$ (verified by the vertex/LP argument above, no
   type-vs-type competition needed at all), and
2. $\bigcup_iU^{\mathrm{feas}}(\tau_i)\supseteq\mathrm{Box}$ (a covering
   property).

This is a genuinely simpler *kind* of target than the full chamber-vertex
enumeration described in `p-space-chamber-vertex-theorem`'s item 1(c) (no
competition between types needs to be resolved), at the cost of possibly
needing more than one type per "true" chamber, since a feasible-but-
suboptimal type can validly cover part of another type's true chamber.

**This does not by itself close case (b2).** The covering property (2) is
exactly as hard to establish in general as the original enumeration, and is
not established even at $n=3$ (see `chamber-a2-p1-tied-to-p2-pair`'s own
finding that a chamber's naive feasibility region need not be a valid cover
on its own — its worst vertex can violate $g\ge0$, requiring the union with
other chambers/sub-regions to actually work). This lemma correctly
identifies *what finite fact* would close case (b2); it does not supply
that fact.

## Proof

Immediate from `p-space-chamber-vertex-theorem`'s own proof: Lemma R22.1's
($\Leftarrow$) direction (feasibility (a) + order (b) $\Rightarrow$
$F^\tau(p)$ is a genuine legal response with value $\ell_\tau(p)$) never
uses condition (c) — that direction only shows a *particular* response is
legal and has that value, not that it is optimal. Since
$\Phi_{\min}(p)\le\Phi(\text{any legal response})$ trivially (by definition
of $\Phi_{\min}$ as a minimum), $\Phi_{\min}(p)\le\ell_\tau(p)$ follows for
every $p$ where $F^\tau(p)$ is legal, i.e. every $p\in U^{\mathrm
{feas}}(\tau)$ — with no appeal to (c) anywhere. The vertex/LP argument
(Theorem R22.2, the standard bounded-polyhedron/affine-functional fact)
applies to any polyhedron cut out by finitely many affine constraints,
which $U^{\mathrm{feas}}(\tau)\cap\mathrm{Box}\cap\{T=1\}$ is by
construction (conditions (a)+(b) plus the Box and simplex-slice
constraints, all affine), regardless of whether the polyhedron happens to
equal a "true" chamber $U(\tau)$ or a strictly larger feasible-but-
suboptimal region. $\blacksquare$

## Relation to existing lemmas

A methodological simplification layered on top of
`p-space-chamber-vertex-theorem` and `within-chamber-affinity-theorem`
(R20.1/R22.1): drops the hardest of the three defining conditions (c)
type-optimality) for the specific purpose of one-sided upper-bound
certification, converting "characterize every true chamber" into "exhibit
a finite feasible covering family." Directly enables
`chamber-a2-p1-tied-to-p2-pair` to be recorded and used as a building block
even though it is not, by itself, a standalone sufficient chamber.
