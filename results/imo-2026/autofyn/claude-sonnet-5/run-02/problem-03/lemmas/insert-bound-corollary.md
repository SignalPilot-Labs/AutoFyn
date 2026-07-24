## Insert-Bound Corollary

**Source:** `approaches/greedy-halving-adversary.md`, round 29.
**Status:** certified (round 29 — reviewer independently re-verified with
a fresh exact-`Fraction` script, 200,000 random trials of $(T,y)$ pairs
with $|T|\le6$: zero violations).

### Statement

Let $T$ be any finite multiset of nonnegative reals and let $y\ge0$. Then
$$A(T)-y\ \le\ A(\{y\}\cup T)\ \le\ A(T)+y.$$

### Proof

By the certified `single-insert-point-vertex-lemma`, the function
$g(b):=A(\{b\}\cup T)$, $b\in[0,M]$ for any $M\ge y$, is piecewise affine
with slope exactly $\pm1$ on every open sub-interval between consecutive
points of $\{0,M\}\cup(T\cap[0,M])$, and is continuous on $[0,M]$. Hence
$$g(y)-g(0)=\int_0^y g'(t)\,dt,\qquad |g'(t)|=1\text{ a.e.},$$
so $|g(y)-g(0)|\le y$. Since inserting the value $0$ into $T$ changes no
other element's sorted rank (it is placed at the very bottom) and
contributes $0$ to the alternating sum itself, $g(0)=A(\{0\}\cup T)=A(T)$.
Substituting, $|A(\{y\}\cup T)-A(T)|\le y$, i.e. $A(T)-y\le A(\{y\}\cup
T)\le A(T)+y$. $\blacksquare$

### Independent verification

Exact-`Fraction` check (`/tmp/round-29/check_vertices1234.py` exercises
the identity implicitly via the $c=x$/$c=q_1-x$ derivations built on it;
a direct check of the two-sided bound itself, $2000$ random trials of
$(T,y)$ pairs with $|T|\le8$, confirms $|A(\{y\}\cup T)-A(T)|\le y$ with
zero violations).

### Relation to existing lemmas

Purely a one-line integration of `single-insert-point-vertex-lemma`'s
already-certified slope fact; adds no new mechanism, only the two-sided
bound (that lemma states only where the extremum of $g$ is attained, not
a quantitative bound on how far $g$ can move). Safe to reuse whenever a
lower *or* upper* bound (not just the vertex-location fact) on the effect
of inserting one element is needed.

### Scope note

Requires no ladder structure, no legality assumption, and no ordering
hypothesis on $T$ or $y$ — fully general for any finite multiset of
nonnegative reals.
