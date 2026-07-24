## Statement

At $n=3$ ($m=4$ pieces $p_1>p_2>p_3>p_4$, $T=p_1+p_2+p_3+p_4$), consider the
Xiang-Yu response of type "Chamber A2": composition $(2,0,0,0)$ (two cuts on
$p_1$, tail $p_2,p_3,p_4$ untouched), with $p_1$ split into three fragments
$(v,w,w)$ where $v$ is *pinned* to the untouched value $p_2$ (a cross-piece
tie between a $p_1$-fragment and the whole piece $p_2$) and the remaining two
fragments are tied to each other at $w=(p_1-p_2)/2$.

This is a valid partition of $p_1$ whenever $w\ge0$, i.e. $p_1\ge p_2$
(automatic in $\mathcal P$). On the region where the descending order is
$$p_2\,(\text{untouched})=v\ \ge\ p_3\ \ge\ p_4\ \ge\ w=w,$$
i.e. subject to the one genuine (non-automatic) wall
$$\textbf{(W5)}\quad p_4\ \ge\ w=\frac{p_1-p_2}2\quad\Longleftrightarrow\quad p_1\le p_2+2p_4,$$
the resulting value of $\Phi$ (sum over odd sorted ranks of the final
6-element multiset $\{p_2,v,p_3,p_4,w,w\}$) has the exact closed form
$$\Phi_{A2}(p)\ =\ \frac{p_1+p_2}2+p_3.$$

**Scope — this is a building block, not a standalone closure.** Chamber
A2's own naive feasibility region (conditions (a) feasibility + (b) order
only, ignoring competition with other Xiang-Yu strategies) is **not** by
itself a sufficient witness for $\Phi_{\min}(p)\le a_3T(p)$ everywhere in
that region: its worst vertex, at
$p=(2/5,\,4/15,\,4/15,\,1/15)$ (three tight constraints: wall (W5), the
order-tie $p_2=p_3$, and the Box wall $p_2=a_3T/2=4T/15$), gives
$g_{A2}:=a_3T-\Phi_{A2}=8/15-3/5=-1/15<0$. This point lies on the closure of
case (b2)'s box boundary (where $p_2=4T/15$ exactly, the already-separately-
handled case-(a) boundary), so it is not a counterexample to the theorem —
but it shows Chamber A2 must be combined with other chambers/sub-regions,
never cited as a standalone sufficient cover.

## Derivation of the closed form

Sorted descending, the six-element multiset is
$$\{\,p_2\ (\text{rank }1),\ \ v=p_2\ (\text{rank }2),\ \ p_3\ (\text{rank }3),\ \ p_4\ (\text{rank }4),\ \ w\ (\text{rank }5),\ \ w\ (\text{rank }6)\,\}$$
(the tied pair $\{p_2,v\}$, both equal to $p_2$, occupies the *first two*
ranks — not ranks 2 and 4 — since both exceed $p_3\ge p_4\ge w$). Odd ranks
are $1,3,5$, contributing $p_2+p_3+w$. Substituting $w=(p_1-p_2)/2$:
$$\Phi_{A2}=p_2+p_3+\frac{p_1-p_2}2=\frac{p_1+p_2}2+p_3,$$
exactly the boxed formula above. (An earlier in-round draft misassigned the
tied pair to ranks 2 and 4, giving the different — and wrong — expression
$\tfrac{p_1+p_2}2+p_4$; this was caught and corrected before certification,
see the sanity re-check in the approach file.)

Mass conservation: $v+2w=p_2+(p_1-p_2)=p_1$, confirming $(v,w,w)$ is a valid
partition of $p_1$.

## Verification

- **Hand-checked at the reported worst vertex**
  $p=(2/5,4/15,4/15,1/15)$: $T=1$; $w=(2/5-4/15)/2=(6/15-4/15)/2=1/15=p_4$
  (wall (W5) tight); $\Phi_{A2}=(2/5+4/15)/2+4/15=(10/15)/2+4/15=5/15+4/15
  =9/15=3/5$; $g_{A2}=a_3-3/5=8/15-9/15=-1/15$, matching the corrected LP
  run (`/tmp/round-23/lp_check.py`, re-derived after an initial run had a
  wall-(W5)-encoding bug, since caught and fixed).
- **Confirmed as the true global minimizer at a distinct interior witness**
  $p\approx(0.44,0.2666,0.14667,0.14663)$: $\Phi_{A2}\approx0.49997$,
  matching the brute-force true $\Phi_{\min}$ found by
  `/tmp/round-23/search_b2_n3.py` (multi-restart Nelder–Mead over all $35$
  legal cut compositions) to five digits, margin $\approx+0.0334>0$ there.
- **Reviewer spot-check (this round, independent):** re-derived the odd-rank
  sum directly from the sorted list and the wall (W5) inequality by hand;
  confirms $\Phi_{A2}=(p_1+p_2)/2+p_3$ and the worst-vertex numbers above,
  matching the approach file's own (corrected) computation exactly.

## Relation to existing lemmas

Companion building block to `within-chamber-affinity-theorem`'s
Chamber-Vertex machinery (R22.1.1's Chamber "A", tied to $p_4$ instead of
$p_2$) — a second explicit exact chamber for the same composition
$(2,0,0,0)$, confirming (together with `feasibility-suffices-for-upper-
bound`) that a single composition can host multiple distinct optimal
vertex types in different sub-regions of the box.
