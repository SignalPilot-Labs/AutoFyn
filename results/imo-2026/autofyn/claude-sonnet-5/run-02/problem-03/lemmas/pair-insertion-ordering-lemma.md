## Statement

**Lemma (Pair-Insertion Ordering, "between" form).** *Let $p\ge q\ge0$
with $p+q=C$, let $w\ge0$ satisfy $q\le w\le p$, and let $x\ge0$ be
arbitrary. Then*
$$A(\{x,p,q,w\})=\begin{cases}
x+w-C, & x\ge p,\\
2p-x+w-C, & w\le x<p,\\
2p-w+x-C, & q\le x<w,\\
C-w-x, & x<q.
\end{cases}$$

**Lemma (Pair-Insertion Ordering, "above" form).** *Let $p\ge q\ge0$ with
$p+q=C$, let $w\ge p$ (the reference value dominates the whole pair), and
let $x\ge0$ be arbitrary. Then*
$$A(\{x,p,q,w\})=\begin{cases}
x-w+2p-C, & x\ge w,\\
w-x+2p-C, & p\le x<w,\\
w+x-C, & q\le x<p,\\
w+C-2p-x, & x<q.
\end{cases}$$

Both forms are elementary, fully general (arbitrary nonnegative $p,q,w,x$
subject only to the stated ordering hypothesis), and give an *exact*
closed form for $A$, not merely a bound.

## Motivation / why this is needed (not a restatement of an existing
lemma)

The certified `single-insert-point-vertex-lemma` proves that $g(b):=
A(\{b\}\cup T)$ is piecewise affine of slope $\pm1$ in $b$ for a single
free coordinate $b$ inserted into a **fixed** rest $T$. It does **not**
apply when two coordinates are coupled by a mass-conservation constraint
(e.g. $p,q$ with $p+q=C$ fixed): varying one under the constraint moves
*two* elements of the multiset simultaneously (one up, one down by the
same amount), giving slope $\pm2$, a genuinely different function. This
was flagged as a citation-mismatch gap by the round-29 outline-reviewer
(round 29, `imo-2026-03`) in the `rank-pigeonhole-budget` approach's
round-29 outline, with a concrete numeric confirmation (exact-`Fraction`
sampling showing slope $\pm2$, not $\pm1$, when varying $f_2$ against a
fixed sum $f_2+f_3=C$). This lemma is the from-scratch fix: rather than
misapplying the single-coordinate lemma to a coupled pair, or invoking
the general `vertex-minimum-theorem` machinery (compactness + exchange
smoothing) for what is really a fully elementary $4$-element sorted-rank
computation, it proves the exact closed form directly by observing that
$q\le w\le p$ (resp. $w\ge p\ge q$) pins the *relative sorted order* of
$\{p,q,w\}$ regardless of the free value $x$, so inserting $x$ is then a
plain $4$-way trichotomy.

## Proof

**"Between" form.** Since $q\le w\le p$, the multiset $\{p,w,q\}$ sorts
(weakly) descending as $p\ge w\ge q$ regardless of ties. Inserting $x$
produces exactly $4$ possible rank positions, by trichotomy of $x$
against $p,w,q$ (boundary cases assigned to the higher bracket, e.g.
$x=p$ to the first):
- $x\ge p$: sorted order $x,p,w,q$; alternating sum ($+,-,+,-$) is
  $x-p+w-q=x-p+w-(C-p)=x+w-C$.
- $p>x\ge w$: sorted order $p,x,w,q$; sum $p-x+w-q=2p-x+w-C$.
- $w>x\ge q$: sorted order $p,w,x,q$; sum $p-w+x-q=2p-w+x-C$.
- $x<q$: sorted order $p,w,q,x$; sum $p-w+q-x=C-w-x$.
The four intervals $[p,\infty),[w,p),[q,w),[0,q)$ partition $[0,\infty)$
exactly since $q\le w\le p$; no case is omitted. The four formulas agree
at every shared boundary (direct substitution: at $x=p$ both give
$p+w-C$; at $x=w$ both give $2p-C=p-q$; at $x=q$ both give $p-w$),
confirming continuity, consistent with $A$'s general continuity in each
coordinate. $\blacksquare$

**"Above" form.** Identical proof method with $w\ge p\ge q$ sorted
instead, giving sorted orders $x,w,p,q$ / $w,x,p,q$ / $w,p,x,q$ /
$w,p,q,x$ in the four respective sub-cases, with the same substitution
$q=C-p$ throughout. $\blacksquare$

## Application (round 29 build)

Used in `rank-pigeonhole-budget`'s §7.17 to close, in full:
- Shape $(2,0,1,0)$'s residual $f_1<4$ (the "between" form, with
  $x=f_3$, $p=g_1$, $q=g_2$, $w=1$, $C=2$), plus a re-confirmation of the
  already-claimed $f_1>4$ branch — giving a complete, both-directions
  closure of this shape.
- Shape $(2,0,0,1)$'s residual $f_1<4$ (the "above" form, with $x=f_3$,
  $p=e$, $q=f$, $w=2$, $C=1$).

Both applications reduce the target inequality $A(U)\ge1$ to an explicit
polynomial in the shape's remaining free parameters ($f_1,f_2$, via
$f_3=8-f_1-f_2$), verified positive by hand in every one of the Lemma's
$4$ cases (no numerics load-bearing in the final proof; exact-`Fraction`
scripts were used only as independent cross-checks, `/tmp/verify_shape.py`,
`/tmp/check_f1_above4.py`, `/tmp/check_2001_full.py`, zero violations in
$200{,}000$–$300{,}000$ trials each).

## Verification

Cross-checked (not substituting for the proof) by exact-`Fraction`
scripts at the point of use: the "between"-form application matched the
lemma's predicted case value exactly across $200{,}000$ random trials
(zero mismatches, `/tmp/verify_shape.py`), and the resulting target
inequality held with zero violations across an additional $500{,}000$
trials spanning the full residual domain plus boundary regimes.

**Reviewer certification (round 29):** independently re-verified both
the "between" and "above" forms from scratch with a fresh exact-`Fraction`
script (200,000 random trials each, arbitrary $p\ge q\ge0$, $C=p+q$,
$w$ ranging over the required order constraint, $x$ arbitrary): zero
mismatches. Also independently re-derived, via `sympy`, all 8 downstream
case-by-case polynomial simplifications used in the lemma's two
applications (shapes $(2,0,1,0)$ and $(2,0,0,1)$): all match exactly.
**Certified.**

## Origin

`results/imo-2026-03/approaches/rank-pigeonhole-budget.md`, §7.17 (round
29), "Lemma (Pair-Insertion Ordering)".
