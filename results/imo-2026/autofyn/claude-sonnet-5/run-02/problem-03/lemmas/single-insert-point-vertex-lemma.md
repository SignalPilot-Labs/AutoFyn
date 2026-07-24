## Statement

Let $T$ be any finite multiset of nonnegative reals and let $[0,M]$ be a
closed interval ($M\ge0$). Consider the function
$$g(b):=A(\{b\}\cup T),\qquad b\in[0,M].$$
Then $g$ is piecewise-affine with slope $\pm1$ on every open sub-interval
between consecutive points of $\{0,M\}\cup(T\cap[0,M])$, and in particular
**$g$ has no flat (slope-$0$) sub-interval anywhere on $[0,M]$.** Consequently
$$\min_{b\in[0,M]}g(b)\ =\ \min_{b\,\in\,\{0,M\}\,\cup\,(T\cap[0,M])}g(b),$$
i.e. the minimum of $g$ over the whole interval is attained at one of the
finitely many breakpoints $\{0,M\}\cup(T\cap[0,M])$ (the two endpoints and
the values of $T$'s own elements that lie in $[0,M]$) — never at a generic
interior point. The symmetric statement holds verbatim for $\max_b g(b)$.

## Proof

Fix $T=\{t_1\ge\dots\ge t_k\ge0\}$ (sorted descending) and let
$0=\beta_0<\beta_1<\dots<\beta_r=M$ enumerate $\{0,M\}\cup(T\cap[0,M])$ in
increasing order ($r\le k+1$). Fix an open sub-interval
$(\beta_{i},\beta_{i+1})$ and $b$ ranging over it. By construction $b$ does
not equal any $t_j\in[0,M]$ throughout this open interval (all such $t_j$
are among the $\beta$'s), so as $b$ varies within $(\beta_i,\beta_{i+1})$,
the strict sorted order of $b$ relative to every element of $T$ is fixed:
writing $j:=|\{l: t_l>b\}|$ (constant on this sub-interval, since $b$ never
crosses a $t_l$-value there), $b$ occupies local rank $j+1$ in
$\{b\}\cup T$ throughout the sub-interval, contributing $(-1)^jb$ to
$A(\{b\}\cup T)$ (odd/even alternating-sum convention: rank $j+1$ has sign
$(-1)^{(j+1)-1}=(-1)^j$). Every element of $T$ keeps its own rank fixed
too (nothing about $b$'s movement within the open interval changes any
$t_l$ vs. $t_{l'}$ comparison, and $b$ stays on the same side of every
$t_l$), so the total contribution of $T$ to $A(\{b\}\cup T)$ is a constant
$c$ (independent of $b$, for $b$ in this sub-interval). Hence
$$g(b)=c+(-1)^jb\qquad\text{for }b\in(\beta_i,\beta_{i+1}),$$
an affine function of $b$ with slope $(-1)^j\in\{-1,+1\}$ — never $0$. By
continuity of $g$ (the sort map and the alternating-sum functional are both
continuous, `integral-alternating-sum-formula`/standard), the same affine
formula extends to the closed sub-interval $[\beta_i,\beta_{i+1}]$. Since a
nonconstant ($\pm1$-slope) affine function on a closed interval attains its
minimum only at an endpoint of that interval, $\min_{[\beta_i,\beta_{i+1}]}g$
is attained at $\beta_i$ or $\beta_{i+1}$ — one of the global breakpoints.
Taking the min over the finitely many sub-intervals $i=0,\dots,r-1$ gives
$\min_{[0,M]}g=\min_i g(\beta_i)$, exactly the claim. The $\max$ case is
identical with "attains its minimum only at an endpoint" replaced by
"attains its maximum only at an endpoint" (same fact about nonconstant
affine functions). $\blacksquare$

## Relation to existing lemmas

This is the single-free-variable (box-constrained, no partition/sum
constraint) special case of the general
`exchange-smoothing-vertex-maximization` / `vertex-minimum-theorem` vertex
reduction — proved here directly and elementarily (no compactness/LP-vertex
machinery needed at all, just a one-line slope computation), because with
only one free coordinate the general multi-variable "two free coordinates,
compensated perturbation" argument collapses to an ordinary single-variable
piecewise-affine minimization. It is also the special case $j\equiv$
(as used by) the certified `insert-element-identity`
($A(\{b\}\cup T)=2A(T_{>b})-A(T)+(-1)^jb$, $j=|T_{>b}|$): differentiating
that closed form in $b$ on a fixed-$j$ interval reproduces the slope
$(-1)^j$ derived above directly, confirming the two derivations agree.

## Independent verification

Exact-`Fraction` check, `/tmp/check_insert_vertex.py`: for $n=3,\dots,7$,
$200$ random legal budget-$(n-4)$ refinements $T'$ of $\{p_4,\dots,p_{n+1}\}$
per $n$, comparing $\min_{b\in[0,p_4]}A(\{b\}\cup T')$ (computed by dense
random + breakpoint sampling) against $\min$ over the breakpoint set
$\{0,p_4\}\cup(T'\cap[0,p_4])$ alone: the breakpoint minimum always matches
(no dense sample ever beats it), confirming the lemma's claim in this
specific ladder application. A second script,
`/tmp/check_argmin_location.py` ($n=4,\dots,8$, $300$ trials each),
confirms the true minimizing breakpoint is genuinely distributed across all
three types ($b=0$: 515/1500, $b=p_4$: 513/1500, interior tie with a $T'$
fragment: 472/1500) — i.e. the interior case is not a numerically negligible
edge case, consistent with it being the genuinely open sub-case identified
in `rank-pigeonhole-budget.md` §7.8.
