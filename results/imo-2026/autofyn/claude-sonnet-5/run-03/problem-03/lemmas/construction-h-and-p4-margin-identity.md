## Source
`approaches/global-lp-vertex-sufficiency.md`, round 21, Section 12
("Round 21: a new $3$-cut construction closes Region I in full rigor").
Certified by the round-21 proof-reviewer after full independent
re-derivation: a symbolic (`sympy`) re-derivation of the exact identity
and both order-condition formulas from scratch
(`/tmp/verify_sym.py`, confirms `sympy.simplify` gives exactly $0$ for
$\mathrm{OddSum}(H)-c(3)-(p_4-\gamma(3))/2$, and independently reproduces
both $p_2-x$ and $x-g_1$ in closed form, matching the file's claims after
re-expressing in $g_1,g_2,g_3$), a 493-instance random Region-I sweep
(`/tmp/verify_regionI.py`, wide gap range, zero identity mismatches, zero
order-condition failures, zero $\mathrm{OddSum}(H)>c(3)$ violations), and
a 300,000-trial Region-I legality check (`/tmp/verify_regionI_legality.py`,
zero instances of $x\le0$ inside Region I). The Region-II counterexample
was independently re-verified exactly
(`/tmp/verify_regionII_counterex.py`): at the cited point, both
$\mathrm{OddSum}(H)=4339131/8000000$ and $\mathrm{OddSum}(C)=216961/400000$
match the file's claimed values digit-for-digit and both exceed
$c(3)=8/15$, confirming the point is a genuine failure of best-of-$\{C,
H\}$ (and lies outside Region I, since $p_4>\gamma(3)$ there). A
100,000-trial independent Region-II sweep (`/tmp/verify_regionII_stats.py`)
confirms a real, nontrivial (not vanishingly rare) failure rate under a
different sampling distribution than the file's own (15% vs. the file's
reported ~3%; the difference is attributable to differing sampling
distributions over $B(3)$, not a bug — the same pattern documented in
round 16's cross-check of a different construction) — the qualitative
finding (genuine, non-empty residual) is confirmed, not the exact
percentage.

## Setting

$B(3):=\{p\in\Delta_3: p_1<\tfrac12,\ g_i:=p_i-p_{i+1}>\gamma(3)\ (i=1,2,3),\
p_4>0\}$, $\gamma(3)=1/15$, $c(3)=8/15$ (via the already-certified identity
$c(n)=\tfrac12+\tfrac{\gamma(n)}2$). Mass conservation gives $p_4=
\tfrac14-\tfrac{g_1}4-\tfrac{g_2}2-\tfrac{3g_3}4$.

## Construction H

Split $p_1\to(g_1,p_2)$ [1 cut] and $p_3\to(x,x,g_1)$ where $x:=(p_3-g_1)/2$
[2 cuts], leaving $p_2,p_4$ untouched. Response multiset $M_H=\{p_2,p_2,
g_1,g_1,x,x,p_4\}$ (uses all $3$ cuts available at $n=3$).

## Theorem (Order and value identity)

$p_2-x=\tfrac{g_1}2+g_2+\tfrac{g_3}2+\tfrac{p_4}2>0$ unconditionally in
$B(3)$; $x-g_1=\tfrac{g_3+p_4-3g_1}2$ (so $x\ge g_1\iff g_3+p_4\ge3g_1$).
Whenever $x\ge g_1\ge p_4$, the sorted order is $p_2\ge p_2>x\ge x>g_1\ge
g_1>p_4$, and
$$\mathrm{OddSum}(M_H)=p_2+x+g_1+p_4=p_2+\tfrac{p_3}2+\tfrac{g_1}2+p_4.$$
Eliminating $p_4$ via mass conservation and simplifying exactly (no
numerics):
$$\boxed{\ \mathrm{OddSum}(M_H)-c(3)=\dfrac{p_4-\gamma(3)}2\ }$$
valid whenever $x\ge g_1\ge p_4$.

## Theorem (Region I closure)

Define $\text{Region I}:=B(3)\cap\{p_4\le\gamma(3)\}\cap\{g_3+p_4>3g_1\}$.
Inside $\{p_4\le\gamma(3)\}$, $B(3)$'s own hypothesis $g_1>\gamma(3)$
gives $g_1>\gamma(3)\ge p_4$ for free, so both order conditions of the
identity hold throughout Region I automatically, and
$$\mathrm{OddSum}(M_H)-c(3)=\frac{p_4-\gamma(3)}2\le0$$
throughout Region I, by construction of the region itself (exact
algebra, no implicit numeric margin). Region I contains a full-dimensional
open neighborhood of the corner $p^\dagger=(\tfrac6{15},\tfrac5{15},
\tfrac4{15},0)$ (both defining inequalities hold at $p^\dagger$ with
strictly positive margin $1/15$).

## Scope note — Region II is NOT closed

The complement $B(3)\setminus\text{Region I}$ is not proved covered by
Construction H, Construction C, or any combination tested this round: a
genuine, exact-arithmetic counterexample exists at
$g_1=\tfrac{3161}{46875},\,g_2=\tfrac{205073}{3000000},\,
g_3=\tfrac{456719}{3000000},\,p_4=\tfrac{339131}{4000000}$ (valid in
$B(3)$, outside Region I), where both $\mathrm{OddSum}(H)=
\tfrac{4339131}{8000000}\approx0.5424$ and $\mathrm{OddSum}(C)=
\tfrac{216961}{400000}\approx0.5424$ exceed $c(3)\approx0.5333$ — verified
independently exact. This lemma certifies **only** Construction H's
identity and Region I's closure; the $n=3$ Existence Theorem's Region II
and the general-$n$ theorem remain open.
