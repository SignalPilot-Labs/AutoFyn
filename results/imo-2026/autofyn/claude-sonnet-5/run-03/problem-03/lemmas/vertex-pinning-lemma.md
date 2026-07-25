# Vertex Pinning Lemma for the split-multiset polytope

**Source.** `approaches/dyadic-potential-invariant.md`, round 5, Sections
0–4.

**Statement.** Fix a partition $p_1,\dots,p_k>0$ ($\sum p_i=1$) and a budget
$n$. For the game value $V^*=\min$ over legal XY responses (cut allocations
$\mathbf m=(m_1,\dots,m_k)\in\mathbb Z_{\ge0}^k$ with $\sum m_i\le n$,
splitting each $p_i$ into $m_i+1$ positive parts) of $\mathrm{OddSum}$ of the
resulting merged multiset:

1. **(Closure Lemma.)** $V^*$ is attained — a genuine minimum, not just an
   infimum — by an honest response with strictly positive fragments (zero
   coordinates can always be discarded without changing `OddSum` or leaving
   the legal-response space).
2. **(Vertex Pinning, counting form.)** For the minimizer's own cut
   allocation $\mathbf m^*$ (after discarding wasted/zero-length cuts, so
   $\sum_i m_i^*$ is the genuine number of cuts used) and its induced sort
   order, at least $\sum_i m_i^*$ *independent* exact ties (pairs of
   elements of the final multiset with exactly equal value — possibly two
   fragments of the same split piece, possibly a fragment and an untouched
   other piece, possibly fragments from two different split pieces) are
   simultaneously active at the minimizer.

**Proof.** Full proof in `approaches/dyadic-potential-invariant.md`,
Sections 1–4:
- Section 1 (Closure Lemma): discarding zero-length fragments preserves
  `OddSum` and legality, reducing the infimum over a union of relatively-open
  simplex-products to a minimum over their closures, a finite union of
  compact polytopes.
- Section 2: `OddSum` restricted to a fixed sort-order region is a fixed
  linear functional (immediate from the definition once the order is
  pinned).
- Section 3: a linear functional on a nonempty compact convex polytope
  attains its minimum at an extreme point (proved from first principles via
  a Krein–Milman-style argument, not cited as a black box).
- Section 4 (Lemma 4.1, the load-bearing step): at a vertex of a sort-order
  region, the $k$ equality constraints (piece-sums, pairwise-disjoint
  support, hence independent) leave an $(N-k)$-dimensional tangent space
  ($N$ = total fragment count); if fewer than $N-k$ zero/tie inequality
  constraints are active, the active-constraint gradients span a proper
  subspace of the tangent space, so there is a nonzero direction $\mathbf d$
  in the tangent space orthogonal to every active-constraint gradient along
  which $\mathbf v\pm t\mathbf d$ stays feasible for small $t$ — contradicting
  that $\mathbf v$ is a vertex (a vertex cannot be a nontrivial midpoint of
  two other feasible points).

**Companion negative result (proved, should travel with the lemma).** The
naive strengthening — "every individual optimal fragment is 0-or-tied," not
just a total *count* of $\ge\sum m_i$ ties — is **false** in general. Exact
counterexample: $k=3$, $(p_1,p_2,p_3)=(0.6,0.3,0.1)$, split $p_1\to(0.5,0.1)$
(one cut). Resulting multiset $\{0.5,0.3,0.1,0.1\}$, sorted descending
$0.5,0.3,0.1,0.1$: $\mathrm{OddSum}=0.5+0.1=0.6=p_1$ exactly (an exact
identity, independent of how $p_1$ is split, as long as exactly one other
fixed element separates the two fragments in sort order — so the whole
interval of splits $a\in[0.1,0.3]$ is optimal). At the vertex $a=0.1$
(active pinning condition: $a=p_3$, exactly $N-k=1$ as required), the other
fragment $b=0.5$ is neither $0$ nor tied with anything — a genuine
counterexample to the per-fragment form, verified by direct substitution.
Only the weaker *counting* form is true in general.

**Independent verification (proof-reviewer, round 5).** Both the
counterexample's arithmetic (`OddSum({0.5,0.3,0.1,0.1}) = 0.6 = p_1`
exactly) and the general LP-vertex argument structure (standard rank/active-
constraint characterization of a polytope vertex) were independently
checked; no error found. The counting statement and its false stronger
cousin are consistent with, and a genuine correction to, the round-5
outline's original conjecture.

**Reuse.** Any approach reasoning about XY's optimal response structure for
a *fixed* LB partition may cite the counting form directly instead of
re-deriving the LP argument. The companion negative result must be cited
alongside it — do not cite or re-derive the stronger, false, per-fragment
form ("every fragment individually is 0-or-tied"). Directly resolves the
round-5 outline's request for a rigorous linear-algebra proof of the
tie-or-zero structural fact (with the necessary correction to a weaker but
true statement).
