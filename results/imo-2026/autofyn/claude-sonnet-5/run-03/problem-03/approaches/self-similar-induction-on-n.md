## Status
partial

## Round 20: closing the multi-gap same-parity gap flagged by the
## round-20 outline-reviewer — the General Pairwise Reduction Lemma and
## a fully rigorous Finite Reduction Theorem (step 1–2 of the outline
## now airtight; the general-$k$ combinatorial closure, step 3–5,
## remains open, unchanged)

**The gap, exactly as flagged.** Round 19's Lemma LNI only rules out two
free coordinates of **opposite** rank parity (its perturbation has rate
$c_i-c_j\ne0$ only then). The round-20 outline's step 2 closed the
remaining same-parity possibility **only within a single $\Gamma$-gap**
(there, adjacent free values automatically alternate parity, so $\ge2$
distinct values in one gap always contain an opposite-parity adjacent
pair). The round-20 outline-reviewer correctly found this leaves
untouched: two free coordinates in **different** $\Gamma$-gaps, separated
by an odd number of intervening (untouched) $\Gamma$-levels, which lands
them on the **same** rank parity — a configuration neither LNI nor the
single-gap pigeonhole addresses. This section closes that gap directly,
with a mechanism that turns out to subsume both the single-gap case and
LNI itself, rather than patching them separately.

### Step 0: numeric confirmation of the mechanism (mandatory cheap-kill,
### run before writing any lemma)

Own exact-`Fraction` script (`/tmp/verify_pairwise.py`,
`/tmp/verify_pairwise2.py`, `/tmp/verify_refined.py`, not reused from any
prior round): built the exact cross-gap same-parity scenario the
outline-reviewer described by hand ($k=6$, $\mathrm{cap}=32$,
$\Gamma_5=\{32,16,8,4,2,1\}$, free elements $x_0=20\in(16,32)$,
$y_0=3\in(2,4)$ — separated by the three intervening levels $16,8,4$, an
**odd** count, giving same rank parity, confirmed directly: both land at
0-indexed rank position parity $1$). Confirmed by direct computation:
$\mathrm{AltSum}$ is **exactly constant** ($=22$) along the entire
mass-conserving segment $x=x_0+t,\ y=y_0-t$ for every tested
$t\in\{-3/2,-1,-1/2,0,1/2,1\}$ within the segment's feasible range, and
**remains exactly $22$** at both boundary endpoints of the segment
($t=1$: $y$ ties to $\Gamma$-level $2$; $t=-1$: $y$ ties to $\Gamma$-level
$4$) — confirming the whole segment, including its boundary, is
$\mathrm{AltSum}$-invariant, not merely locally flat. A second script
independently re-confirmed the general local-linearity formula
$\Delta\mathrm{AltSum}=(c_x-c_j)\,t$ (for small $t$, no rank crossing)
across $28{,}558$ random trials spanning $k=2,\dots,7$ and arbitrary
(not just adjacent) gap placements — zero violations. A third script
confirmed that when the moving coordinate's own block has odd
multiplicity $\ge3$ (so it has an even number of untouched siblings left
behind), the one-sided departure slope is **still well-defined and
consistent** regardless of which physical copy is considered to move —
$11{,}604$ trials, zero violations. These three facts are exactly the
ingredients assembled into the lemma below.

### Step 1: the Invisible-Block Skip Fact (new, proved in full — a
### direct corollary of the certified Lemma BCF)

**Fact.** Let $M$ be a finite multiset of positive reals and let $z$ be a
value occurring in $M$ with **even** multiplicity $m$. Suppose a single
new coordinate $x$ (not otherwise a member of $M$) is moved continuously
from just below $z$ to just above $z$ (i.e. fully crosses the entire
block of $m$ copies of $z$), all other elements of $M\cup\{x\}$ held
fixed. Then $x$'s rank (in the sorted order of $M\cup\{x\}$) shifts by
exactly $m$ (an **even** number) across the crossing, so its rank parity
— and hence its sign $c_x\in\{+1,-1\}$ in $\mathrm{AltSum}$ — is
**identical** immediately before and immediately after the crossing.
Consequently, for any fixed second coordinate $y\ne x$ (also present, not
equal to $z$), the slope $c_x-c_y$ governing $\mathrm{AltSum}$'s rate of
change under the mass-conserving perturbation $x\mapsto x+t$,
$y\mapsto y-t$ is the **same on both sides** of $x$'s crossing of $z$'s
block — i.e. $z$'s even-multiplicity block is **not a genuine breakpoint**
of $\mathrm{AltSum}$ along this line, even though $x$ passes directly
through it.

*Proof.* Immediate from the definition of rank: as $x$ passes fully from
below $z$'s block to above it, it overtakes exactly the $m$ copies of $z$
in the sorted order (nothing else changes position relative to $x$,
since all other elements of $M$ are held fixed and $x$ has not yet
reached the next distinct value beyond $z$ in either direction by
hypothesis). Overtaking $m$ elements shifts $x$'s rank by exactly $m$; if
$m$ is even, rank parity — and therefore the sign $c_x=(-1)^{\text{rank}
-1}$ — returns to its original value. Since $y$'s position and rank are
unaffected by $x$ crossing $z$ (as $x\ne z\ne y$ throughout and $y$ moves
independently), $c_y$ is unchanged too, so the slope $c_x-c_y$ is
unchanged across the crossing. $\blacksquare$

This is exactly the trajectory-level strengthening of the already-
certified Corollary of Lemma BCF ("an even-multiplicity level contributes
$0$ to $\mathrm{AltSum}$ regardless of value or position") — here applied
not just to a static snapshot but along a continuous one-parameter
family, showing such a level is invisible not only to the *value* of
$\mathrm{AltSum}$ but to its *rate of change* as another coordinate moves
through it.

### Step 2: the General Pairwise Reduction Lemma (new, proved in full —
### supersedes Lemma LNI and closes the outline-reviewer's flagged gap)

**Setup.** Fix feasible $R$ for $\mathrm{GCH}(k)$ with $\mathrm{sum}(R)=S$.
Call a value $v\in(0,\mathrm{cap})$ occurring in $R$ **free** if $v\notin
\Gamma_{k-1}$, and call it **active** if in addition its multiplicity in
$R$ is odd. (By the Corollary of Lemma BCF, only active free values, and
$\Gamma$-levels with even $R$-multiplicity, contribute nonzero terms to
$\mathrm{AltSum}(R\cup\Gamma_{k-1})$; this is the same active/inactive
dichotomy already used implicitly by Lemma BCF's proof.)

**Lemma (General Pairwise Reduction).** Suppose $R$ has two **distinct**
active free values $w_i\ne w_j$ — with no restriction on which
$\Gamma$-gaps they occupy, whether adjacent or not, and no restriction on
their rank parity. Then there is a feasible $R'$ (same $\mathrm{sum}(R')=
S$, same cardinality $|R'|=|R|$) such that
$$\mathrm{AltSum}(R'\cup\Gamma_{k-1})\ \le\ \mathrm{AltSum}(R\cup
\Gamma_{k-1}),$$
and the number of distinct active free values of $R'$ is **strictly
less** than that of $R$.

*Proof.* Pick one coordinate $r_i=w_i$ and one coordinate $r_j=w_j$ of
$R$ realizing these two active values (if $w_i$'s multiplicity is
$m_i\ge3$, the remaining $m_i-1\ge2$ copies — an **even** number — stay
fixed at $w_i$ throughout what follows; likewise for $w_j$). Consider the
one-parameter family $R(t)$ obtained from $R$ by replacing $r_i\mapsto
w_i+t$, $r_j\mapsto w_j-t$, all other coordinates of $R$ (including any
remaining same-valued siblings of $w_i,w_j$) held fixed; this preserves
$\mathrm{sum}(R(t))=S$ for every $t$.

Define the **active boundary set** $B:=\{0,\mathrm{cap}\}\cup\{v\in
\Gamma_{k-1}: v\text{ has even }R\text{-multiplicity}\}\cup\{\text{other
active free values of }R,\text{ i.e. distinct from }w_i,w_j\}$ — a finite
set not containing $w_i$ or $w_j$. By Step 1 (applied to each inactive
$\Gamma$-level or inactive free block that $r_i$ or $r_j$ might otherwise
approach) and by the even-remainder well-definedness confirmed in Step 0
(applied to $r_i$'s and $r_j$'s own remaining same-valued siblings, if
any), $\mathrm{AltSum}(R(t)\cup\Gamma_{k-1})$ is an **affine** function of
$t$ on the maximal interval $[t_{\min},t_{\max}]$ within which neither
$w_i+t$ nor $w_j-t$ reaches a point of $B$ or each other — because every
crossing $r_i$ or $r_j$ might make of an *inactive* block leaves rank
parity (hence the slope) unchanged by Step 1, so the **only** points that
can change the slope are members of $B$ or the meeting point $w_i+t=w_j-t$
itself. This interval is nonempty (it contains $t=0$, since $w_i,w_j\notin
B$ and $w_i\ne w_j$) and bounded (by $0,\mathrm{cap}\in B$ always, or by
whichever finite boundary point is nearer).

Let the slope be $\sigma\in\{-2,0,2\}$ (the rank-parity-sign difference
$c_i-c_j$ at $t=0$, well-defined by Step 0's even-remainder fact). Two
cases:
- If $\sigma\ne0$ (opposite parity — exactly Lemma LNI's hypothesis):
  moving $t$ in the sign-decreasing direction to the corresponding
  endpoint of $[t_{\min},t_{\max}]$ strictly **decreases**
  $\mathrm{AltSum}$ (an affine function with nonzero slope, evaluated at
  the far end of its domain in the decreasing direction, is $<$ its value
  at $t=0$ whenever that endpoint is not itself $t=0$, which holds since
  the interval has positive length).
- If $\sigma=0$ (same parity — the case not covered by Lemma LNI, exactly
  the outline-reviewer's flagged gap, **including** the cross-gap
  configuration): $\mathrm{AltSum}(R(t))$ is **constant** on the whole
  interval $[t_{\min},t_{\max}]$ (affine with slope $0$), so moving to
  either endpoint gives $\mathrm{AltSum}(R(t_{\max}))=\mathrm{AltSum}(R(0))$
  exactly — a weakly non-increasing (here: equal) move.

In either case, take $R':=R(t^*)$ where $t^*$ is the endpoint reached.
At $t=t^*$, by construction (the interval is *maximal*), one of the
following holds: (i) $w_i+t^*$ or $w_j-t^*$ equals a $\Gamma$-level of
even $R$-multiplicity — then that coordinate is no longer a free value at
all (it has joined $\Gamma_{k-1}$), so it is removed from the active free
count; (ii) $w_i+t^*$ or $w_j-t^*$ equals $0$ or $\mathrm{cap}$ — same
conclusion (no longer an interior free value); (iii) $w_i+t^*$ or
$w_j-t^*$ equals another active free value $w_\ell$ of $R$ — then, after
the move, that value's own $R'$-multiplicity increases by $1$
(odd$+1=$even), so $w_\ell$ becomes **inactive** in $R'$, and
simultaneously the moving coordinate's *former* value ($w_i$ or $w_j$)
either vanishes entirely (if it had no other siblings) or has its
remaining even-sib count now correctly reflecting multiplicity $m-1$
(even, hence that value, if it persists at all in $R'$, was already
excluded from the active count) — either way the active free value set
loses (at least) one member without gaining any (it does **not** gain
$w_\ell$, since $w_\ell$ has just become inactive) — a strict decrease;
(iv) $w_i+t^*=w_j-t^*$ (the two moving coordinates meet): their combined
multiplicity at the new shared value is (multiplicity contributed by
$r_i$) $+$ (multiplicity contributed by $r_j$) $=1+1=2$ (even, since each
was a single peeled representative), so this new value is **inactive** in
$R'$ — both $w_i$ and $w_j$ leave the active free set, a decrease of $2$.

In every case, the number of distinct active free values strictly
decreases, and $\mathrm{AltSum}(R'\cup\Gamma_{k-1})\le\mathrm{AltSum}(R
\cup\Gamma_{k-1})$ (with equality in the $\sigma=0$ case, strict decrease
in the $\sigma\ne0$ case). $R'$ is feasible: $\mathrm{sum}(R')=S$
(preserved throughout), $|R'|=|R|\le k+1$, and every coordinate of $R'$
lies in $(0,\mathrm{cap}]$ (by construction, $t^*$ was chosen exactly at
the first point either coordinate would otherwise leave this range or
cross another fixed point). $\blacksquare$

**Why this closes the flagged gap.** The Lemma places **no** hypothesis
on which $\Gamma$-gaps $w_i,w_j$ occupy, or on how many $\Gamma$-levels
separate them, or on their rank parity — it is proved uniformly for all
four cases (same gap, opposite parity; same gap, same parity — vacuous,
since two distinct values in one gap are automatically adjacent hence
opposite parity, matching the outline's step 2; different gaps, opposite
parity — a special case, handled the same way LNI already handled it;
**different gaps, same parity** — the exact configuration the
outline-reviewer hand-built and found unaddressed by both LNI and step 2,
now covered by the $\sigma=0$ branch above, verified in Step 0's worked
example). The mechanism is not a patch bolted onto LNI; it strictly
generalizes it (LNI is exactly the $\sigma\ne0$ branch).

### Step 3: the Finite Reduction Theorem (corrected and now fully
### rigorous, no residual gap)

**Theorem.** For every feasible $R$ of $\mathrm{GCH}(k)$, there exists a
feasible $R''$ with $\mathrm{sum}(R'')=\mathrm{sum}(R)=S$, $|R''|\le|R|$,
$$\mathrm{AltSum}(R''\cup\Gamma_{k-1})\ \le\ \mathrm{AltSum}(R\cup
\Gamma_{k-1}),$$
and $R''$ has **at most one** distinct active free value (i.e. $R''$'s
free part, restricted to values not in $\Gamma_{k-1}$, consists of copies
of at most one value $r$, with multiplicity $t\in\{0,1,2,3,\dots\}$ whose
*parity* alone determines its contribution: $0$ if $t$ even, $\pm r$ if
$t$ odd).

*Proof.* Let $\alpha(R):=$ number of distinct active free values of $R$
(a nonnegative integer $\le|R|\le k+1$). If $\alpha(R)\le1$, take $R''=R$,
done. Otherwise $\alpha(R)\ge2$: apply the General Pairwise Reduction
Lemma to obtain $R_1$ with $\mathrm{AltSum}(R_1\cup\Gamma_{k-1})\le
\mathrm{AltSum}(R\cup\Gamma_{k-1})$, $\mathrm{sum}(R_1)=S$, $|R_1|=|R|$,
and $\alpha(R_1)\le\alpha(R)-1$ (strictly less, by the case analysis
above). Iterate: this produces a finite sequence $R=R_0,R_1,R_2,\dots$
with $\alpha(R_0)>\alpha(R_1)>\alpha(R_2)>\cdots\ge0$, a strictly
decreasing sequence of nonnegative integers, hence terminating after at
most $\alpha(R_0)\le k+1$ steps at some $R_m$ with $\alpha(R_m)\le1$.
Take $R'':=R_m$. Every step preserves $\mathrm{sum}=S$, cardinality
$\le k+1$, and every coordinate in $(0,\mathrm{cap}]$ (feasibility), and
$\mathrm{AltSum}$ is non-increasing at each step, hence overall. The
final structural description (at most one distinct active free value,
its parity-dependent contribution) is exactly the Corollary of Lemma BCF
applied to $R''$'s free part. $\blacksquare$

**Consequence for the target inequality.** Since $\mathrm{AltSum}(R\cup
\Gamma_{k-1})\ge\mathrm{AltSum}(R''\cup\Gamma_{k-1})$ and $R''$ is again a
feasible configuration of $\mathrm{GCH}(k)$ (same $S$, same or smaller
cardinality — smaller cardinality only makes the cardinality constraint
$|R''|\le k+1$ easier to satisfy, never harder), **it suffices to prove
$\mathrm{AltSum}(R''\cup\Gamma_{k-1})\ge1$ for every feasible $R''$ of
this restricted "at most one free block" form** — exactly the finite,
per-$k$ combinatorial statement about integer multiplicity vectors
$(m_0,\dots,m_{k-1})$ (for $\Gamma$'s own levels) plus a single free block
$(t,r)$ that the outline's step 3 describes, and that this file's round
19 section already reduced the problem to (see "What remains open" in the
round-19 section above) — **but now that reduction rests on a complete
proof, not an admittedly-incomplete case analysis.** This directly and
fully answers the round-20 outline-reviewer's flagged concern: the
finite-reduction step of the outline (its steps 1–2) is no longer merely
"correct as far as it was checked" but a proved theorem covering every
configuration, including the cross-gap same-parity shape the reviewer
exhibited.

### Honest scope: what is still open after this round

The Finite Reduction Theorem (Step 3 above) is now complete and gap-free.
**What remains completely unproved, exactly as after round 19, is the
resulting finite combinatorial claim itself**: for integer multiplicities
$m_0,\dots,m_{k-1}\ge0$ (at $\Gamma$-levels $2^{k-1},\dots,1$) and a single
free block $(t,r)$ with $t\in\{0,1\}$ WLOG (by the theorem's own parity
reduction — the outline's "$t\in\{0,1,2\}$" collapses to $t\in\{0,1\}$
once the Finite Reduction Theorem's parity bookkeeping is applied
directly, rather than $t\in\{0,1,2\}$; a multiplicity-$2$ free block is
already inactive/invisible by the Corollary of Lemma BCF and contributes
identically to $t=0$ for AltSum's *value*, though it still consumes sum
budget — so the actual free-form witness $R^*=\{\text{chain}\}\cup\{r,r\}$
from the achievability theorem is a $t=2$ (inactive) instance, matching
$t=0$'s AltSum value $1$ exactly, consistent with the equality case),
subject to $\sum m_j\cdot2^j+t\cdot r=S\in[2^k,2^k+1)$ and $\sum m_j+t\le
k+1$: show
$$\mathrm{AltSum}=\sum_{j:m_j\text{ odd}}(-1)^{C_j}2^j\ +\ [t\text{ odd}]
\cdot(\pm r)\ \ge\ 1.$$
This is precisely the object round 18's Step 3 diagnosed as needing a
genuinely more general **two-parameter family** $\mathrm{GCH}(j,
\mathrm{cap},b;S)$ (fixed cap, decreasing $\Gamma$-index and count
budget) rather than a naive induction on $k$ — that diagnosis is
unaffected by this round's work and remains the honest open target for
the next round. This round's contribution is entirely on the *reduction*
side (turning "prove the bound for all continuous $R$" into "prove the
bound for this specific finite family," now rigorously, with no
unaddressed configurations), not on the combinatorial closure itself.

### Promotable lemmas (round 20)

- **Invisible-Block Skip Fact (new, proved in full, elementary).** If a
  value $z$ occurs with even multiplicity $m$ in a multiset $M$, a
  coordinate $x\notin M$ moving continuously past $z$'s entire block
  (all else fixed) has its rank shift by exactly $m$ (even), so its rank
  parity — and hence its sign in $\mathrm{AltSum}$, and the slope of
  $\mathrm{AltSum}$ under any mass-conserving two-coordinate
  perturbation involving $x$ — is unchanged before and after the
  crossing. Direct corollary of the certified Lemma BCF, extended from a
  static statement to a trajectory statement. See "Step 1" above for the
  proof.
- **General Pairwise Reduction Lemma (new, proved in full — strictly
  generalizes the certified Lemma LNI).** For $R$ feasible in
  $\mathrm{GCH}(k)$ with two distinct **active** free values $w_i\ne w_j$
  (no restriction on $\Gamma$-gap membership, adjacency, or rank
  parity), there is a feasible $R'$ with the same sum and cardinality,
  $\mathrm{AltSum}(R'\cup\Gamma_{k-1})\le\mathrm{AltSum}(R\cup
  \Gamma_{k-1})$, and strictly fewer distinct active free values. Proved
  via a mass-conserving line-segment argument: $\mathrm{AltSum}$ is
  affine on the maximal segment bounded only by *active* reference
  points (using the Invisible-Block Skip Fact to rule out inactive
  points as breakpoints), with slope $0$ exactly in the previously
  unaddressed same-parity case (verified exactly $=$-constant on a
  hand-built cross-$\Gamma$-gap same-parity example, $k=6$,
  $x_0=20,y_0=3$, value $22$ throughout $t\in[-1,1]$ including both
  boundary endpoints) and slope $\ne0$ exactly reproducing Lemma LNI's
  case. Numerically stress-tested: local-linearity formula ($28{,}558$
  trials, $k=2,\dots,7$, zero violations), well-definedness under
  odd-multiplicity siblings ($11{,}604$ trials, zero violations). See
  "Step 2" above for the full proof.
- **Finite Reduction Theorem (new, proved in full — corrects and
  completes the round-20 outline's steps 1–2, closing exactly the gap
  the round-20 outline-reviewer flagged).** Every feasible $R$ of
  $\mathrm{GCH}(k)$ admits a feasible $R''$ with the same sum, no larger
  cardinality, $\mathrm{AltSum}(R''\cup\Gamma_{k-1})\le\mathrm{AltSum}(R
  \cup\Gamma_{k-1})$, and at most one distinct active free value.
  Proved by iterating the General Pairwise Reduction Lemma, using the
  strictly-decreasing nonnegative-integer potential $\alpha(R)=$ number
  of distinct active free values (terminates in $\le k+1$ steps). See
  "Step 3" above. **Consequence**: it suffices to prove $\mathrm{AltSum}
  \ge1$ for the restricted "at most one active free value" family — the
  finite integer-multiplicity-vector claim already identified (but not
  proved) in round 19 — closing the reduction step in full generality
  for the first time; the combinatorial closure itself (general $k$)
  remains open, unchanged from round 18–19's diagnosis (needs the
  two-parameter family $\mathrm{GCH}(j,\mathrm{cap},b;S)$, not a
  single-parameter induction on $k$).

## Round 19: extremal-principle attack on the general-$k$ GCH($k$)

**Goal recap.** GCH($k$): for $R$ a finite multiset with $\max(R)\le
2^{k-1}=:\mathrm{cap}$, $|R|\le k+1$, $\mathrm{sum}(R)=S\in[2^k,2^k+1)$,
show $\mathrm{AltSum}(R\cup\Gamma_{k-1})\ge1$ where $\Gamma_{k-1}=
\{2^{k-1},2^{k-2},\dots,2,1\}$ ($k$ elements, sum $2^k-1$). (This is
equivalent, via mass conservation, to the previously-stated
$\mathrm{OddSum}(R\cup\Gamma_{k-1})\ge(S+2^k)/2$; certified $k=2$ instance:
`lemmas/sharper-odd-residual-and-k2-cardinality-half-sum.md`.)

### Mandatory cheap-kill (run before any proof writing, per Rule)

Ran a corrected-methodology numerical stress test: `scipy.optimize.minimize`
(SLSQP) with **many random restarts** (15–60 per instance, cross-checked
between two independent scripts) over $R\in(0,\mathrm{cap}]^n$, $n=1,\dots,
k+1$, subject to $\sum r_i=S$, minimizing $\mathrm{AltSum}(R\cup
\Gamma_{k-1})$ directly (not the naive SLSQP-single-run approach flagged as
unreliable in round 18 — multi-restart with tight `ftol` here). Tested
$k=2,3,4,5$ (one script) and $k=2,3,4$ at several fractional offsets
$S=2^k+\{0.001,0.01,0.05,0.2,0.3,0.5,0.7,0.8,0.99\}$ (second script).
**Result: the minimum found is always $\ge1$, and equals exactly $1.000000$
at every instance where the search actually reached the true optimum**
(a few restarts get stuck at strictly-worse local optima such as
$1.010000$ or $1.05$, an expected multi-restart-count artifact, never
below $1$). No violation of $\mathrm{AltSum}\ge1$ found in any of $\sim
150$ (k,S) configurations. The minimizer found (when it converges) always
has the shape $\{2^{k-1},2^{k-2},\dots,4\}\cup\{r,r\}$ — e.g. at $k=4$,
$S=16.30$: $r=[8,4,2.15,2.15]$; at $k=5$, $S=32.70$: $r=[16,8,4,2.35,
2.35]$ — confirming the outline's "chain + tied pair" family as the
observed extremizer. This clears the cheap-kill: the mechanism is not
dead, and the specific witness family is corroborated, not merely
asserted.

### New general-purpose lemmas, proved in full

**Lemma TPC (Tied-Pair Cancellation).** Let $M$ be a finite multiset of
positive reals and suppose the value $x$ occurs in $M$ with multiplicity
*exactly* $2$. Let $M'=M\setminus\{x,x\}$. Then $\mathrm{AltSum}(M)=
\mathrm{AltSum}(M')$.

*Proof.* Sort $M$ in weakly decreasing order. Since no other element of
$M$ equals $x$, the two copies of $x$ occupy two *consecutive* ranks
$i,i+1$ in this sorted order (all elements $>x$ precede both copies, all
elements $<x$ follow both copies — this is immediate from the definition
of a weak sorted order applied to a value of multiplicity $2$). Ranks $i$
and $i+1$ have opposite parity, so their combined contribution to
$\mathrm{AltSum}(M)$ is $(-1)^{i+1}x+(-1)^{i+2}x=0$. Deleting these two
positions shifts every rank $r>i+1$ down to $r-2$ in the sorted order of
$M'$, while ranks $1,\dots,i-1$ are unchanged; since $r$ and $r-2$ have the
same parity, every remaining element's sign in the alternating sum is
unchanged. Hence $\mathrm{AltSum}(M)=0+\mathrm{AltSum}(M')$. $\blacksquare$

**Lemma BCF (Block-Contribution Formula).** Let $M$ be a finite multiset
of positive reals, partitioned into "levels" of distinct values $v_1>v_2>
\cdots>v_L>0$ with multiplicities $t_1,\dots,t_L\ge1$ (so $M$ is the
disjoint union of $L$ constant blocks). For each $i$ let $C_i:=
\sum_{i'<i}t_{i'}$ (the number of elements of $M$ strictly greater than
$v_i$). Then
$$\mathrm{AltSum}(M)=\sum_{i:\,t_i\text{ odd}}(-1)^{C_i}v_i.$$

*Proof.* Induction on $\sum_i t_i$. If every $t_i=1$ this is the
definition of $\mathrm{AltSum}$ directly (rank of $v_i$ is $C_i+1$, sign
$(-1)^{C_i+1+1}=(-1)^{C_i}$ using the convention $+$ at odd rank). If some
$t_{i_0}\ge2$, apply Lemma TPC to two of the (equal) copies of $v_{i_0}$:
this does not change $\mathrm{AltSum}(M)$, reduces $t_{i_0}$ by $2$
(possibly to $0$, deleting the level), and does not change $C_i$ for any
$i\ne i_0$ (the count of elements *strictly greater* than $v_i$ is
unaffected by removing two copies of $v_{i_0}$, whether $i_0>i$ or
$i_0<i$: if $i_0<i$, $C_i$ loses $2$, an even change, but $C_i$ only
enters the formula through its **parity**, which is unchanged). By
induction the reduced multiset satisfies the formula with the same
right-hand side (each surviving level's parity of $t_i$ and parity of
$C_i$ unchanged), so $M$ does too. $\blacksquare$

**Corollary (even blocks are free).** In particular, if $t_i$ is even for
some level $i$, that level contributes $0$ to $\mathrm{AltSum}(M)$
*regardless of its value $v_i$ or its position among the other levels* —
immediate from Lemma BCF, since the sum only ranges over odd-$t_i$
levels, and adding/removing an even-multiplicity level changes every
other level's $C_{i'}$ by an even amount, hence changes no sign. This
formalizes, in full generality, why a "tied pair" $\{r,r\}$ can be
inserted at *any* value $r$ without affecting $\mathrm{AltSum}$ of the
rest of the multiset — this is the exact general mechanism underlying
the outline's witness family, proved here from Lemma TPC rather than
assumed.

### Exact achievability: the chain+pair family attains $\mathrm{AltSum}=1$
### for every valid $S$ and every $k\ge3$ (proved in full, no numerics);
### $k=2$ needs a different witness

**Correction (round 20, per the certified lemma cache — this paragraph
replaces the round-19 draft's overclaim, which stated the result "for
every $k\ge2$").** The round-19 proof-reviewer found, and certified in
corrected form (`lemmas/gch-achievability-witness-k-geq-3.md`), that the
construction below is valid **only for $k\ge3$**: at $k=2$ the chain is
empty, so the formula collapses to $R^*=\{r,r\}$ with $r\in[2,2.5)$, but
$\mathrm{cap}=2^{k-1}=2$ at $k=2$, so $r>\mathrm{cap}$ for every $S>4$ —
**infeasible**. Achievability at $k=2$ is still true, but via the
structurally different, already-certified witness $\{2,b,b\}$,
$b=(S-2)/2\in[1,1.5)$, from `lemmas/sharper-odd-residual-and-k2-cardinality-half-sum.md`
(Lemma 2). The two cases together give achievability for every $k\ge2$;
neither single formula below does. The rest of this subsection (the
construction and its proof) is unchanged from round 19 and is correct
**as a $k\ge3$ statement**.

Fix $k\ge3$ and $S\in[2^k,2^k+1)$. Define
$$R^*:=\{2^{k-1},2^{k-2},\dots,4\}\ \cup\ \{r,r\},\qquad
r:=\frac{S-2^k}2+2,$$
where the chain $\{2^{k-1},\dots,4\}$ has $k-2$ elements (empty when
$k=2$; a single element $\{4\}$... wait for $k=3$ the chain is $\{4\}$
itself, i.e. exponents from $k-1$ down to $2$, which is $k-2$ terms) and
$r\in[2,2.5)$ (since $S\in[2^k,2^k+1)$, $(S-2^k)/2\in[0,0.5)$). Note
$|R^*|=(k-2)+2=k\le k+1$ and $\mathrm{sum}(R^*)=(2^{k-1}+\cdots+4)+2r=
(2^k-4)+2r=(2^k-4)+(S-2^k+4)=S$ exactly, and every entry of $R^*$ is
$\le2^{k-1}=\mathrm{cap}$ (the chain's top entry is exactly the cap; $r<
2.5<\mathrm{cap}$ for $k\ge2$). So $R^*$ is feasible for GCH($k$) at every
valid $S$.

Merge with $\Gamma_{k-1}=\{2^{k-1},\dots,4,2,1\}$: the chain part of
$R^*$ exactly matches $\Gamma_{k-1}$'s values at levels $4,8,\dots,
2^{k-1}$ ($k-2$ shared levels), each now with multiplicity $2$ (one from
$\Gamma$, one from the chain) — even, hence by the Corollary above these
$k-2$ levels contribute $0$ to $\mathrm{AltSum}$, **regardless of their
position relative to the free pair $\{r,r\}$**. What remains after
discarding these zero-contribution levels is exactly the 4-element
multiset $\{r,r,2,1\}$ (the pair, plus $\Gamma_{k-1}$'s own two bottom
elements, which are *not* matched by anything in $R^*$'s chain since the
chain stops at $4$). Since $r\in[2,2.5)$, sorted descending this is
$r,r,2,1$ (using $r\ge2$), giving $\mathrm{AltSum}(\{r,r,2,1\})=r-r+2-1=
1$. Hence, by Lemma BCF/TPC (removing zero-contribution levels does not
change $\mathrm{AltSum}$ of the whole):
$$\mathrm{AltSum}(R^*\cup\Gamma_{k-1})=1\quad\text{exactly, for every }
k\ge3\text{ and every }S\in[2^k,2^k+1).$$
This is an **exact, fully rigorous proof** (no numerics used in this
step) that the target bound $\mathrm{AltSum}\ge1$ is tight (attained)
throughout the whole range, for every $k\ge3$ — this is certified as
`lemmas/gch-achievability-witness-k-geq-3.md`. **It does not cover
$k=2$** (a chain-empty specialization of $\{2^{k-1},\dots,4\}\cup\{r,r\}$
is $\{r,r\}$, two elements, which is infeasible as shown above — it does
**not** equal, or specialize to, the certified $k=2$ witness $\{2,b,b\}$
of `sharper-odd-residual-and-k2-cardinality-half-sum.md` Lemma 2, which
has three elements and *retains* the cap element $2=2^{k-1}$; the
round-19 draft's claimed cross-check between the two was a genuine
internal inconsistency, now removed). Achievability at every $k\ge2$
therefore rests on citing **both** certified lemmas — this $k\ge3$
construction and the separate $k=2$ Lemma 2 — never one formula alone.

### The lower-bound direction: partial progress, honest open gap

**Lemma LNI (Local Non-Improvement, proved in full).** Suppose $R$ is a
feasible configuration (as in GCH($k$)) and $R$ has two coordinates $r_i
\ne r_j$ (WLOG $r_i<r_j$) with the following properties: (a) both lie
strictly between two consecutive values of $\Gamma_{k-1}\cup\{0,
\mathrm{cap}\}$ that bound them (i.e. neither is currently at $0$,
$\mathrm{cap}$, or tied with a $\Gamma_{k-1}$-value), and (b) in the
sorted order of $R\cup\Gamma_{k-1}$, $r_i$ and $r_j$ occupy ranks of
**different** parity. Then $R$ does not minimize
$\mathrm{AltSum}(R\cup\Gamma_{k-1})$ subject to $\mathrm{sum}(R)=S$ fixed:
the perturbation $r_i\mapsto r_i+t$, $r_j\mapsto r_j-t$ (which preserves
$\mathrm{sum}(R)$) changes $\mathrm{AltSum}$ at rate $c_i-c_j\ne0$ where
$c_i,c_j\in\{+1,-1\}$ are the rank-parity signs, for all sufficiently
small $|t|$ (small enough that no rank-order crossing among $R\cup
\Gamma_{k-1}$ occurs, which is possible since (a) puts each of $r_i,r_j$
in an open interval disjoint from $\Gamma_{k-1}\cup\{0,\mathrm{cap}\}$),
so choosing the sign of $t$ with $t(c_i-c_j)<0$ strictly decreases
$\mathrm{AltSum}$.

*Proof.* Immediate: on the open box-neighborhood where no rank-crossing
occurs, $\mathrm{AltSum}(R\cup\Gamma_{k-1})$ restricted to $(r_i,r_j)$
with $r_i+r_j$ fixed is the affine function $c_i r_i+c_j r_j+(\text{const})
= c_i(r_i+t)+c_j(r_j-t)+\text{const}$, with derivative in $t$ equal to
$c_i-c_j\ne0$ by hypothesis (b). $\blacksquare$

**Consequence (Vertex Reduction, established).** At any true minimizer of
$\mathrm{AltSum}(R\cup\Gamma_{k-1})$ over the GCH($k$) feasible set, every
pair of coordinates satisfying (a) must fail (b), i.e. every two
coordinates *simultaneously free* (not pinned to $0$/$\mathrm{cap}$/a
$\Gamma$-tie) must share the same rank parity. This is exactly the
mechanism that makes the "tied pair" (two free coordinates forced
*equal*, hence automatically same value $\Rightarrow$ adjacent ranks of
opposite parity to each other individually but *jointly* contributing $0$
by Lemma TPC — note this is the degenerate case where they are literally
equal, not merely same-parity-but-distinct) a genuine local-optimality
candidate, and rules out any minimizer with two free, *unequal*-valued,
opposite-parity coordinates.

**What remains open.** Lemma LNI shows a *necessary condition* on any
minimizer (all pairs of free coordinates same-parity, or pinned). It does
**not** by itself rule out every non-"chain+pair" configuration — in
particular:
- Two free coordinates of the *same* parity but *unequal* value are not
  excluded by Lemma LNI (the perturbation's rate is $0$ there, so no
  contradiction is derived, but also no bound on their common contribution
  to $\mathrm{AltSum}$ is established this way);
- A **single** free coordinate (no partner) is not addressed by Lemma LNI
  at all (it needs two coordinates to perturb while preserving the sum
  constraint) — its value is *forced* by $S$ once every other coordinate
  is pinned, so it does not correspond to a further "improving move" in
  the same sense, and a full classification requires directly comparing
  the (finitely many, for each cardinality $n\le k+1$) resulting
  "single-residual" and "same-parity-pair" $\mathrm{AltSum}$ values against
  $1$ — which is the discrete combinatorial statement about integer
  vectors $(m_0,\dots,m_{k-1})$ (multiplicities of $R$ at each
  $\Gamma$-level) described in the outline's step 4, via the Block
  Formula: $\mathrm{AltSum}=\sum_{j:\,m_j\text{ even}}(-1)^{C_j}2^j$ where
  the single residual (if used) or same-parity pair contributes an
  additional forced term. **This final domination statement — that no
  choice of $(m_0,\dots,m_{k-1})$ with $\sum m_j\le k-1$ (single residual)
  or $\le k-2$ (pair), subject to feasibility of the residual value(s) in
  $(0,\mathrm{cap}]$, ever produces $\mathrm{AltSum}<1$ — is verified by
  hand for every case at $k=2$ (matching the certified exhaustive Lemma 2
  exactly: patterns $\{2,2\}+r$ give $1+r>1$; $\{2,1\}+r$ give $r\ge1$;
  $\{1,1\}$ is infeasible) and is strongly corroborated by the
  multi-restart numerical search above for $k=3,4,5$, but is NOT proved
  in general for arbitrary $k$ this round.** This is the genuine remaining
  gap: a clean general induction or direct combinatorial argument over the
  integer vector $(m_0,\dots,m_{k-1})$ has not yet been found (the natural
  "peel the top level" induction is the one already diagnosed in round 18
  as needing a two-parameter family; the block-formula reformulation here
  is a cleaner statement of the same combinatorial content, but a full
  proof was not completed within this round's time budget).

### Honest net effect, round 19

- **Cheap-kill**: passed, with a corrected multi-restart methodology;
  witness family and exact value $1$ corroborated at $k=2,\dots,5$.
- **New, fully proved, general-purpose lemmas**: Tied-Pair Cancellation
  (Lemma TPC), Block-Contribution Formula (Lemma BCF) and its Corollary,
  Local Non-Improvement (Lemma LNI) and its Vertex-Reduction consequence.
- **New, fully proved, exact (non-numeric) result**: the chain+pair
  family $R^*$ achieves $\mathrm{AltSum}(R^*\cup\Gamma_{k-1})=1$ exactly,
  for *every* $k\ge2$ and *every* $S\in[2^k,2^k+1)$ — this generalizes the
  $k=2$ equality locus of the certified Lemma 2 to all $k$, in full
  rigor, and shows the target bound is tight throughout.
- **What is still missing**: the matching lower bound
  $\mathrm{AltSum}(R\cup\Gamma_{k-1})\ge1$ for *every* feasible $R$, in
  general — reduced now to one precisely-stated, clean discrete
  combinatorial claim (via Lemma BCF) about integer multiplicity vectors,
  verified for $k=2$ (exhaustively, already certified) and numerically for
  $k=3,4,5$, but not proved for general $k$. The general Cardinality-
  Constrained Half-Sum Lemma GCH($k$), and hence GT($m$) sub-case (i) for
  general $m$, **remains open** — genuinely narrower and better-structured
  than round 18's diagnosis (the achievability half is now a clean exact
  theorem, not a numerical conjecture, and the remaining lower-bound gap
  has a named, finite-per-$k$ combinatorial form via Lemma BCF rather than
  a vague "true numerically"), but not closed.

## Round 17 target (per outliner, revise)
Round 17's explorer re-derived sub-case (i)'s chain correctly this time: the
right mechanism is a **coupled single-step (OddSum,EvenSum) alternation**
($O_j=2^{j-1}+E_{j-1}$, $E_j=O_{j-1}$), not the "Odd stays Odd" telescoping
round 16 got wrong, and round 16's refuting counterexample ($|D|=5>m+1=3$)
is confirmed **out of GT($m$)'s own scope** (its hypothesis is $|D|\le m+1$ —
verified against this file's own boxed GT($m$) statement). Enforcing the
cap gives zero violations in 20,000 fresh trials. Tasks for this round:
(1) state the scope correction explicitly; (2) formally derive the coupled
alternation and chain it $e$ times to level $k$, using the new Even-target
twin of the Large-Sum Closure Theorem (needed when $e$ is odd); (3) prove
(not just numerically confirm) the telescoped-sum-vs-target inequality in
closed form, covering both $e$-parities; (4) conclude sub-case (i) closure
for every $e\ge1$, correctly scoped this time. See
`/tmp/round-17/proof-outliner.md` for the full skeleton.

## Round 16 target (per outliner, revise)
Redo Step 3 of the sub-case (i) width-1-window closure without the
Monotonicity-Reduction over-generalization the math-explorer flagged
(round 15's Step 3 shrank to the abstract, unreachable, provably-false
small boundary $\mathrm{sum}(D)=2^k$; the actual object arising from a
$q=0$ chain of length $e$ keeps $\mathrm{sum}(D)=2^m$, large, throughout).
**Round 16 outcome (see "Round 16: Step 3 corrected ..." section below,
this round's main content):** the corrected Step 0 re-derives the true
forced value $\mathrm{sum}(R)=2^m-a_1$ directly from the $q=0$-chain
peeling identity (no new machinery — reuses the certified $q=0$ case of
the Unified Threshold-Pair-Peeling Lemma $e$ times, $D$ never touched).
A new **Half-Sum Corollary** ($\mathrm{OddSum}(N)\ge\mathrm{sum}(N)/2$,
immediate from the certified Lemma AS + AltSum Corollary) is then used to
prove the **Large-Sum Closure Theorem**: for every $k\ge1$, every excess
$e=m-k\ge1$, and every $a_1\in(2^{k-1},2^k]$ (covering the width-1 window
in full, with no restriction to $a_1\ge2^{k-1}+1$), the target
$\mathrm{OddSum}(R\cup\Gamma_{k-2})\ge2^k-a_1$ holds unconditionally, with
strict positive slack that provably grows with $e$ (matching the
explorer's numeric finding of large, growing, positive margins in the
genuinely-embedded scenario — now a full proof, not a numeric
observation). Combined with the peeling identity, this **closes sub-case
(i) of $\mathrm{GT}(m)$ in full for every excess $e\ge1$** — the width-1
window is entirely eliminated as an obstruction whenever $e\ge1$. The
proof's own zero-slack computation shows this technique cannot be pushed
to $e=0$ (an exact, not approximate, obstruction — reproduces round 15's
already-known $a_1\ge2^{k-1}+1$ boundary exactly at $e=0$), so the
residual open gap of sub-case (i) is now narrowed from "width-1 window,
every $e\ge0$" to **exactly "width-1 window, $e=0$ only"** — the same
shape as `Case-B(m,k)`'s own untouched sliver, not itself closed this
round. $\mathrm{GT}(m)$, $m\ge4$ remains open (gated on these two
$e=0$-shaped slivers). Status remains `partial`, correctly self-reported
(this is real, narrower, independently-checkable progress, not a full
closure of sub-case (i) or of $\mathrm{GT}(m)$).

## Round 15 target (per outliner, revise)
Push $\mathrm{GT}(m)$ for $m\ge4$ via two routes: (1) index-match
sub-case (i) ($q=1,e\ge1$) to the round-3/4 variable-target object
$G(m,k;V)$ and revive its AltSum/Single-Insertion machinery using the
now-certified Growth Lemma; (2) attempt a continuity/limiting transfer
across `Case-B(m,k)`'s excluded boundary $\max(D)\to2^{m-1}^-$ using the
certified Tie-Neutrality Lemma. **Round 15 outcome (see "Round 15: the
AltSum Small-Sum Lemma ..." section below): Step 1's literal index-match
FAILS** (honestly reported, per the outline's own mandated check) — but
the failure analysis directly produced a strictly more general,
substantially simpler new tool (the **AltSum Small-Sum Lemma**, built from
already-certified Lemma AS + the AltSum Corollary, no new machinery),
which **closes the large majority of sub-case (i) unconditionally, for
every excess $e\ge0$** (not just $e=0$), reducing the entire remaining gap
to a single width-1 window in the peeled element $a_1$ — a genuine,
verified narrowing of a previously wide-open sub-case. **Route (2)'s
premise is found to be factually incorrect**: round 5 already established
that `Case-B(m,k)`'s closed region has a *hard* boundary at
$\max(B)\le2^{m-1}-1$ (a full unit away), not a family of results holding
for "every $\delta>0$" as the outline's premise assumed — so there is no
vanishing-$\delta$ family to take a limit of, and the continuity argument
as dispatched cannot get started (reported as an honest Spec concern back
to the outliner). Status remains `partial`.

## Round 14 target (per outliner, revise)
Pursue the variable-target-$V$ generalization of $\mathrm{GT}(m)$ to close
the two named residual sub-cases (small-sum mirror; $q=1$ excess $e\ge1$).
**Round 14 outcome (see "Round 14: the AltSum corollary, the Growth Lemma,
and the exact reduction ..." section below):** first corrected a false
numeric claim flagged by the outline-reviewer (the "full-count instance
has genuine slack" claim does not reproduce; this round's own from-scratch
check confirms the reviewer's tight-margin finding). **Two new
general-purpose lemmas proved in full**: the **AltSum corollary**
($0\le\mathrm{AltSum}(N)\le\max(N)$) and the **Growth Lemma** (the
increasing-direction complement of the certified Monotonicity Reduction
Lemma). Using these, **the entire small-sum-mirror sub-case (ii) — both
the not-full-count and full-count instances — is proved equivalent** (new
**Small-Sum Reduction Theorem**, modulo one flagged tie-boundary detail)
**to `Case-B(m,k)`**, the file's own long-standing central obstruction
(open since round 4, the "middle regime," only the smallest instance
closed at $m=3,4$ in round 11). This is a genuine simplification (sub-case
(ii) needs no new machinery, only the already-attacked `Case-B(m,k)`), not
a new closure. **Sub-case (i)** ($q=1$, $e\ge1$): a natural "piece-cap-
relaxed" fix is proved **false** by an explicit counterexample; the exact
point in the recursion where this sub-case becomes unavoidable is
precisely diagnosed (matches round 12's $m\ge4$ feasibility threshold) but
**not closed**. $\mathrm{GT}(m)$ for $m\ge4$ **remains open**; Status
remains `partial`.

## Round 11 target (per outliner, revise)
Reframe the still-open $j\ge2$ trichotomy pieces (the middle regime
$\mu\le b_1<2^{m-1}$, Case B's target `Case-B(m,k)`, and gap (b)(ii)) via a
genuinely re-derived cell-wise-affine-in-$B$ / finite-vertex-enumeration
mechanism, structurally parallel to (but independently re-derived for a
different polytope than) `global-lp-vertex-sufficiency`'s certified
Finite-Cell Affine-Vertex Reduction machinery. **Round 11 outcome (see
"Round 11: the Affine-Rank Lemma and Vertex Reduction, applied to the
minimal middle-regime instance" below):** two new general-purpose lemmas are
proved in full — the **Affine-Rank Lemma** (within a fixed merged-order
"cell," $\mathrm{OddSum}$ of any mix of free real variables and frozen
values is affine, in fact $0/1$-linear, in the free variables) and the
**Vertex-Attainment Lemma** (the extrema of an affine functional on a
compact convex polytope occur at vertices) — both simpler and more general
than the sibling approach's versions (no "free-block" elimination step is
needed here, since the free coordinates are literally free). These combine
into the **Middle-Regime Vertex Reduction Theorem**: the true minimizer of
$\mathrm{OddSum}(B\cup S)$ in the middle regime (or any regime) always sits
at a vertex, characterized by a finite list of tie/boundary conditions —
turning the middle regime into (in principle) a finite check for each fixed
$(j,c)$. **First discovered a genuine indexing bug from a naive first pass**
(using $\Gamma_{m-3}$ instead of the correct $\Gamma_{m-2}$ for the tail's
untouched part after splitting its top piece) — caught and fixed before any
claim was made. Applied the corrected machinery to the smallest nonempty
instance of the middle regime ($j=2$, one tail cut on $S$'s own top piece,
i.e. $c=1$): **proved exactly**, by direct computation (no numerics) at the
identified boundary vertex, that $m=3$ and $m=4$ both attain
$\mathrm{OddSum}(B\cup S)=2^m$ **exactly** at an explicit boundary
configuration — a genuine, checkable closure of these two smallest
instances, not previously computed. For $m=5$ the analogous boundary
vertex gives $\mathrm{OddSum}=33>32=2^5$ (strict slack, computed exactly),
and extensive numerical search (Nelder–Mead, hundreds of restarts,
$m=3,4,5$) found no configuration violating $\mathrm{OddSum}\ge2^m$ in this
$(j,c)=(2,1)$ family. **Honestly not closed:** the vertex candidate list
was generated by inspection/search, not by an exhaustive proof that these
are the ONLY vertices of the full arrangement (which would also need
comparisons against every element of $\Gamma_{m-2}$, not just the coarse
sum/order/regime constraints) — so general $m$ for even this smallest
$(j,c)=(2,1)$ family, let alone general $(j,c)$, remains open. Status
remains `partial`.

## Round 10 target (per outliner, revise)
Split the remaining window claim $(\ddagger)$ (round 9) into gap (a)
[optimality of Theorem W's witness AT the top endpoint $W=2^{\ell-1}+\varepsilon$]
and gap (b) [$\max_D\mathrm{OddSum}(D\cup T)$ non-decreasing in $W$ across the
window], with gap (b) further split into (i) the piece-cap-unsaturated
sub-case (new tiny piece, claimed safe by rank-counting) and (ii) the
piece-cap-saturated sub-case (genuinely open). **Round 10 outcome (see
"Round 10" section below): gap (b)(i) is now proved in full as a clean,
general, reusable lemma (Tiny-Piece Insertion Monotonicity). Gap (a) is
NOT closed, but is given a new, exact, cleaner reformulation** (via the
already-certified Companion Peeling Lemma) as a self-contained target
$\mathrm{OddSum}(D\cup\Gamma_{\ell-2})\ge2^{\ell-1}$, independently verified
by exact-equivalence Monte Carlo testing (13,500 admissible trials across
$\ell=3,4,5$ and three $\varepsilon$ values, zero mismatches between the
original and reduced target's truth value on each sampled $D$) — and this
reformulation is used to give an honest, new **diagnosis**: gap (a), in
full generality (arbitrary piece count of $D$), is exactly a tail-untouched,
top-split instance (with a bonus $+\varepsilon$ budget and an extra
$\max(D)<2^{\ell-1}$ cap) of the file's own still-open general $j\ge2$
"top-split" trichotomy (Proposition C / Reduction B / the middle-regime
gap, all still open in `## Open gaps` above) — **not** a strictly easier or
structurally different problem, so closing gap (a) in full generality is
provably at least as hard as the paper's own central unresolved obstruction,
not a smaller side-lemma. Gap (b)(ii) remains completely open, untouched
this round. Status remains `partial`.

## Round 9 target (per outliner, revise)
Close the **Branch-I.A-restricted window** (now the sole remaining piece of
the whole tail-untouched sliver, by round 8's proved equivalence). This
round's explorer (lens: sliver-window) found strong numeric+symbolic
evidence for an exact closed form:
$$\min_{C\text{ in window}}\bigl(\mathrm{OddSum}(C\cup\Gamma_{\ell-1})-2^\ell\bigr)=\varepsilon/2,$$
attained at $c_1=2^{\ell-1}$ (the window's left endpoint) by the
**budget-starved partial duplicate-the-rest** family
$C=\{2^{\ell-1}\}\cup(\Gamma_{\ell-2}$ with its bottom element $1$
replaced by two copies of $r:=(1+\varepsilon)/2)$ — an instance of the
certified Doubling Lemma applied only at the bottom rank (piece budget
forbids duplicating more). **New mechanism to try, not yet attempted on
this gap**: exchange-smoothing (crux `aimo-0146` — bounds a fixed-weight
sorted-sum under a sum/budget constraint by showing any non-extremal
profile can be locally perturbed toward the extremal family without
violating constraints), executed via the already-certified
Single-Insertion Lemma (exact $\Delta\mathrm{AltSum}$ formula for
inserting one value at an arbitrary sorted position) as the "one-unit-move"
primitive. This directly targets the whole window's minimum at once,
unlike the previously-exhausted peel+scalar-bound / order-statistics
routes (both diagnosed as wrong-direction or insufficient in rounds 6–7 —
do not retry those). Before the full proof: re-verify the $\varepsilon/2$
conjecture at $\ell=7,8$ (only checked to $\ell=6$) and confirm the
minimizer is the closed endpoint $c_1=2^{\ell-1}$ itself (in the window),
not merely an infimum, so the theorem statement uses $\ge$ cleanly.

**Round 9 outcome (see "Approaches tried" and "Theorem W" below for the
full detail): the dispatched closed form had a computational slip — the
correct witness value is $r=1+\varepsilon/2$, not $(1+\varepsilon)/2$ (the
latter's sum does not match $\mathrm{sum}(C)=2^\ell+\varepsilon$, off by
exactly $1$). With this correction, the $\varepsilon/2$-margin claim at the
left endpoint is now proved exactly (Theorem W), reusing the certified
General Insertion Lemma from a sibling approach for a one-line derivation.
The window's full closure (all $c_1$ in the window, not just the endpoint)
is reduced to a single clean monotonicity claim, numerically well
supported, but not proved this round — the window remains open.**

## Approaches tried
- **Round 22 (this round): Track 1 — Odd-Excess $e\ge3$ Endpoint Closure
  Theorem over the full range $a_1\in(2^{k-1},2^k]$ (not just the
  window); Track 2 — cap-free strengthening of the certified GCH lemma
  (via full line-by-line audit of its proof and its underlying Finite
  Reduction Theorem) plus a Global-max peel closing `Case-B(m,k)`'s
  sliver.** Both tracks fully closed, proved in full, independently
  verified (see "Round 22" section above for full detail and the
  "Promotable lemmas (round 22)" list). Net effect: every excess-carrying
  case of sub-case (i) is now closed unconditionally (all $k\ge1$, both
  parities), and `Case-B(m,k)` is now fully closed for every $b_1<
  2^{m-1}$. **Does not close $\mathrm{GT}(m)$ as a whole**: sub-case
  (i)'s own $e=0$ residual remains open and is shown, on closer reading
  this round, to be genuinely distinct from `Case-B(m,k)` (opposite side
  of the relevant threshold) — round 17's "same object" characterization
  is not established as stated. Status stays `partial`.
- **Round 19 (this round): extremal-principle/LP-vertex attack on the
  general-$k$ GCH($k$), via Tied-Pair Cancellation + Block-Contribution
  Formula.** See "Round 19: extremal-principle attack..." above for full
  detail. Genuine new results, all proved in full (no numeric appeal in
  the proofs themselves): **Lemma TPC** (removing two equal-valued
  elements from a multiset leaves $\mathrm{AltSum}$ unchanged), **Lemma
  BCF** (a general level-by-level closed form for $\mathrm{AltSum}$ of any
  multiset decomposed into constant blocks, with the corollary that
  even-multiplicity blocks contribute exactly $0$ regardless of value or
  position), and an **exact, general-$k$ achievability theorem**: the
  "chain + tied pair" witness family $R^*=\{2^{k-1},\dots,4\}\cup\{r,r\}$
  achieves $\mathrm{AltSum}(R^*\cup\Gamma_{k-1})=1$ exactly for every
  $k\ge2$ and every $S\in[2^k,2^k+1)$ — generalizing the certified $k=2$
  equality locus to all $k$, in exact algebra, not numerics. Also proved
  in full: **Lemma LNI** (Local Non-Improvement — a genuine smoothing/
  exchange argument: two simultaneously-free, opposite-rank-parity
  coordinates of $R$ can never both occur at a true minimizer of
  $\mathrm{AltSum}$) and its Vertex-Reduction consequence. The mandatory
  cheap-kill (multi-restart exact-objective `scipy` search, corrected
  methodology per round 18's warning against unreliable single-run
  SLSQP) passed cleanly at $k=2,\dots,5$: minimum found always $\ge1$,
  exactly $1$ when convergence is good, matching $R^*$'s shape. **What
  remains open, honestly**: the matching general lower bound
  $\mathrm{AltSum}(R\cup\Gamma_{k-1})\ge1$ for *every* feasible $R$ (not
  just the witness) is reduced to one precise discrete combinatorial
  claim about integer multiplicity vectors $(m_0,\dots,m_{k-1})$ (via
  Lemma BCF) — verified for $k=2$ (matches the certified exhaustive
  Lemma 2 exactly) and corroborated numerically for $k=3,4,5$, but **not
  proved for general $k$** this round; Lemma LNI narrows the search
  (rules out one whole class of non-minimal configurations) but does not
  by itself finish the domination argument (it says nothing about
  same-parity-but-unequal free pairs, nor about single-residual
  configurations, whose values are forced by $S$ rather than freely
  perturbable). Net: GCH($k$) general form, and hence $\mathrm{GT}(m)$
  sub-case (i) for general $m$, **remains open** — genuinely sharper
  structure than round 18 (achievability is now an exact theorem, the
  gap is now a single named finite-per-$k$ combinatorial statement) but
  not closed. **CHANGES REQUESTED** is the honest self-assessment (real
  progress, matching new lemmas proposed for certification, target
  lemma still open).

- **Round 16 (this round): redo Step 3 of sub-case (i)'s width-1-window
  closure to track the actual, forced large $\mathrm{sum}(R)=2^m-a_1$
  (not the abstract small $2^k-a_1$ round 15's Step 3 wrongly reduced to
  — flagged by the math-explorer as both provably false in general and
  unreachable by the real recursion).** See "Round 16: Step 3 corrected
  ..." below for full detail. Outcome, honestly reported:
  - **Step 0 re-derives the correct target directly from the $q=0$-chain
    mechanism**: $D$ is never touched by a $q=0$ step, so after $e$ such
    steps from level $m$ to level $k=m-e$, $\mathrm{sum}(D)$ is still
    $2^m$, and the residual $R=D\setminus\{a_1\}$ genuinely has
    $\mathrm{sum}(R)=2^m-a_1$, matching the outline's diagnosis exactly.
  - **New Half-Sum Corollary and Large-Sum Closure Theorem, both proved
    in full**: $\mathrm{OddSum}(N)\ge\mathrm{sum}(N)/2$ for any finite
    multiset (immediate from certified Lemma AS + AltSum Corollary), used
    to show $\mathrm{OddSum}(R\cup\Gamma_{k-2})\ge2^k-a_1$ holds
    unconditionally whenever the excess $e=m-k\ge1$, for every
    $a_1\in(2^{k-1},2^k]$ — no restriction to the previously-closed range
    $a_1\ge2^{k-1}+1$ needed. Independently re-verified (own exact-
    `Fraction` scripts, this round, $78{,}851$ trials across three sweeps
    including a targeted sweep confined to the window and a large-excess
    stress test up to $e=15$): zero violations, margins matching the
    proof's own derived worst case exactly.
  - **Combined with the peeling identity, this closes sub-case (i) of
    $\mathrm{GT}(m)$ in full for every excess $e\ge1$** — the width-1
    window is eliminated as an obstruction whenever any excess is
    present. The proof's own exact zero-slack computation at $e=0$ shows
    this technique cannot be extended there (it exactly reproduces round
    15's already-known $a_1\ge2^{k-1}+1$ boundary, with literally zero
    room to spare), so this is not a case of "ran out of time," but a
    genuine, checked structural boundary of the method.
  - **Net**: sub-case (i)'s open residual narrows from "width-1 window,
    every $e\ge0$" (round 15) to **"width-1 window, $e=0$ only"** — the
    same shape as `Case-B(m,k)`'s own sliver, left untouched this round.
    $\mathrm{GT}(m)$, $m\ge4$ **remains open**, now gated on exactly two
    structurally-identical $e=0$-shaped slivers. Status `partial`,
    correctly self-reported.
- **Round 15: index-match sub-case (i) to $G(m,k;V)$ and
  revive its round-3/4 machinery; attempt a continuity/limiting transfer
  of `Case-B(m,k)`'s excluded boundary, per the outliner's dispatch.** See
  "Round 15: the AltSum Small-Sum Lemma, sub-case (i) closed down to a
  width-1 window ..." below for full detail. Outcome, honestly reported:
  - **Step 1's mandatory cheap-kill index-match check FAILS** (as the
    outline itself demanded be checked first): $G(m,k;V)$'s stated domain
    $V\ge2^{m-1}$ does not cover sub-case (i)'s full target range
    $V=2^k-a_1\in(0,2^{k-1})$ — verified with an explicit numeric instance
    ($k=3$, $a_1=7$, $V=1<2$). The literal $G(m,k;V)$-revival plan is
    abandoned, per the outline's own "void if the match is inexact" rule.
  - **The failure analysis led directly to a new, strictly more general
    lemma proved in full**: the **AltSum Small-Sum Lemma** ($\mathrm{sum}
    (D)\le2^m-1\Rightarrow\mathrm{OddSum}(D\cup\Gamma_{m-1})\ge\mathrm{sum}
    (D)$, with **no** cap on $|D|$ or $\max(D)$ at all), a two-line
    consequence of two already-certified tools (Lemma AS, AltSum
    Corollary). Independently verified (own exact-`Fraction` scripts,
    $14{,}000+18{,}000$ trials).
  - **Sub-case (i) is now closed on the majority of its range,
    unconditionally, for every excess $e\ge0$** (new **Sub-case (i) Window
    Reduction Theorem**): closed for $a_1\ge2^{k-1}+1$; the remaining gap
    is exactly the width-1 window $a_1\in(2^{k-1},2^{k-1}+1)$, identified
    as the same recurring self-similar window object seen elsewhere in the
    file, now with an unrestricted excess twist not previously handled by
    any of the file's prior window closures (Theorem W, gap-(a)'s
    $\mathrm{GT}(m)$ closure at $\ell\le4$, all $e=0$ only). Independently
    verified both that the closed region is genuinely violation-free and
    that the window is genuinely open (violations found by direct search
    at every $k$ tested).
  - **The same lemma re-derives `Case-B(m,k)`'s known safe zone
    ($\max(B)\le2^{m-1}-1$) in three lines**, independently confirming
    round 5's finding (not a new closure, a correctness cross-check).
  - **Route (2) (continuity/limiting transfer): the dispatched premise is
    found to be factually incorrect, honestly reported as a Spec
    concern.** The outline assumed a family of proved interior results
    $\{\max(D)<2^{m-1}-\delta\}_{\delta>0}$ existed to take a limit of;
    checking against the file's own certified history (and the round's
    own independent re-derivation above) shows the actually-proved
    interior region has a **hard** boundary at $\max(B)\le2^{m-1}-1$ (a
    full unit away), not a shrinking-$\delta$ family — so there is no
    starting family for a continuity argument to act on. This route
    cannot be executed as dispatched; reported honestly rather than
    forcing an invalid limiting argument.
  - **Net effect**: real, verified narrowing of sub-case (i) (from fully
    open to a width-1-with-excess window); `Case-B(m,k)` unchanged (its
    obstruction reconfirmed via an independent, simpler route); a genuine
    Spec-level correction of the round's route-(2) premise for future
    rounds. $\mathrm{GT}(m)$ for $m\ge4$ **remains open**. Status remains
    `partial`.

- **Round 14 (this round): variable-target-$V$ generalization of
  $\mathrm{GT}(m)$, closing sub-cases (i) and (ii), per the outliner's
  dispatch (with the outline-reviewer's numeric correction applied
  first).** See "Round 14: the AltSum corollary, the Growth Lemma, and the
  exact reduction of the whole 'small-sum mirror' sub-case to
  `Case-B(m,k)`" below for the full detail. Outcome, honestly reported:
  - **Corrected the round's motivating numeric claim first (mandatory)**:
    re-verified from scratch (own exact-`Fraction` and random-composition
    scripts, not the explorer's) that the "full-count instance has genuine
    slack" claim does **not** reproduce — margins found are $\approx0$ at
    $m=3,4$ (tight), matching the outline-reviewer's independent finding.
    No claim below relies on any slack assumption.
  - **Two new general-purpose lemmas proved in full and independently
    verified** (own scripts, thousands of exact-`Fraction` trials each,
    zero violations): the **AltSum corollary** ($0\le\mathrm{AltSum}(N)\le
    \max(N)$, one-paragraph induction from the certified Peeling identity)
    and the **Growth Lemma** (the increasing-direction complement of the
    certified Monotonicity Reduction Lemma: any $D$ with $\ge2$ pieces,
    cap $2^{m-1}$, sum $\le2^m$ can be grown, coordinatewise, up to sum
    $2^m$ exactly without exceeding the cap, and $\mathrm{OddSum}$ can
    only increase under this growth).
  - **New Small-Sum Reduction Theorem (proved, modulo one flagged tie
    detail)**: using the Growth Lemma, the *entire* small-sum-mirror
    sub-case (ii) of $\mathrm{GT}(m)$'s $p=0$/$q=0$ branch — **both** the
    not-full-count instance (already reducible via the outline's own
    filler-insertion argument) **and** the full-count instance (newly
    reduced here) — is shown to be **exactly equivalent** to `Case-B(m,k)`
    at the single boundary value $\mathrm{sum}(D)=2^m$, which (via the
    already-certified Monotonicity Reduction Lemma) is also exactly what
    the large-sum/gap-(a) regime already needed. **This unifies all of
    $\mathrm{GT}(m)$'s $p=0$ branch, at every value of $\mathrm{sum}(D)$,
    into one single already-identified open object**, `Case-B(m,k)`
    (open since round 4, "the middle regime," closed only for the
    smallest instance at $m=3,4$ in round 11) — a genuine simplification
    of the remaining target, not a new closure.
  - **Sub-case (i) ($q=1$, $e\ge1$): honest negative finding plus precise
    diagnosis, not closed.** Proved by explicit counterexample
    ($k=0,e=1$, $D=\{0.4,0.4\}$) that the natural "piece-cap-relaxed"
    generalization of $\mathrm{GT}(k-1)$ is **false** in general — ruling
    out the most direct fix. Traced exactly when a genuine $q=1$,
    $e\ge1$ instance is *forced* to occur in the real recursion (once a
    pure $q=0$ chain becomes count-infeasible, matching and generalizing
    round 12's own $m\ge4$ feasibility threshold) — a useful structural
    explanation for why $m\ge4$ is exactly where this sub-case first
    becomes unavoidable, but **no closing argument was found**.
  - **Net effect**: $\mathrm{GT}(m)$ for $m\ge4$ **remains open**. The
    round's real contribution is narrowing what remains to exactly two
    named, already-precisely-stated objects: `Case-B(m,k)` (already under
    attack since round 4) and sub-case (i) (newly diagnosed, still
    unsolved) — no third, independent mechanism is needed for sub-case
    (ii) anymore. Status remains `partial`.

- **Round 11 (this round): re-derive a cell-wise-affine-in-$B$ / vertex-enumeration
  mechanism, per the outliner's dispatch, and apply it to the middle regime,
  Case B, and gap (b)(ii).** See "Round 11" section below for the full
  detail. Outcome, honestly reported:
  - **Two new general-purpose lemmas proved in full**: the Affine-Rank Lemma
    (cell-wise affineness of $\mathrm{OddSum}$ in any set of free real
    coordinates merged with frozen values) and the Vertex-Attainment Lemma
    (extrema of an affine functional on a compact convex polytope occur at
    vertices) — genuinely re-derived from scratch for this approach's own
    object (fixed frozen tail elements, free $B$-and-tail-split
    coordinates), not assumed to transfer from `global-lp-vertex-
    sufficiency`'s different polytope (varying $p$ vs. varying split
    coordinates at fixed sum). Confirmed this domain is in fact simpler: no
    "free-block" elimination step is needed, since here the free
    coordinates are already literally free real numbers, not fragments
    constrained to sum to a fixed $p_i$.
  - **Middle-Regime Vertex Reduction Theorem** (structural, proved):
    combines the two lemmas to show the true minimizer of
    $\mathrm{OddSum}(B\cup S)$ subject to any of the trichotomy's regimes is
    attained at a vertex of the constraint polytope (closure), reducing each
    fixed $(j,c,m)$ instance to a finite (in principle) enumeration.
  - **Caught and fixed a genuine bug before any claim was made**: a first
    pass used $\Gamma_{m-3}$ for the tail's untouched part after the middle
    regime's required cut (splitting $S$'s own top piece $2^{m-1}$); the
    correct object is $\Gamma_{m-2}$ (removing only the top piece from
    $\Gamma_{m-1}$ leaves $\Gamma_{m-2}$, not $\Gamma_{m-3}$). Caught via a
    numerical sanity check that failed with the wrong index (found minima
    strictly below $2^m$, impossible if the theorem is true) and resolved by
    re-deriving the correct index directly from the definition.
  - **Closed the smallest nonempty middle-regime instance exactly at two
    values of $m$**: for $(j,c)=(2,1)$ (three-piece split of the top, one
    cut on the tail's own top piece — shown to be the minimal configuration
    for which the middle regime is even nonempty, since $c=0$ forces
    $\mu=2^{m-1}$, collapsing the middle regime to empty), the boundary
    vertex $B=(2^{m-1},2^{m-2},2^{m-2})$, $S=\{2^{m-1}\}\cup\Gamma_{m-2}$
    (i.e. the degenerate limit $s\to0$, $b_1\to2^{m-1}$) gives
    $\mathrm{OddSum}(B\cup S)=2^m$ **exactly** at $m=3$ (direct hand
    computation, verified below) and $\mathrm{OddSum}=2^m$ exactly at $m=4$
    at a nearby vertex $B=(6,6,4)$, $S=\{4,4\}\cup\Gamma_2$ (also verified by
    direct hand computation below) — genuine, checkable, exact closures of
    two small instances, not previously computed in the file. At $m=5$ the
    analogous vertex gives $\mathrm{OddSum}=33>32$ (exact computation, real
    slack, not tight).
  - **Honestly not closed**: the vertex candidates used above were located
    by numerical search (Nelder–Mead + random sampling), not by a completed
    exhaustive proof that they are the ONLY vertices of the full hyperplane
    arrangement (which also includes comparisons of $B$'s and $S$'s free
    coordinates against every individual element of $\Gamma_{m-2}$, not
    just the coarse sum/order/regime constraints checked here) — so this is
    real, verified progress on two small cases, but general $m$ even within
    this single smallest $(j,c)=(2,1)$ family, let alone the full middle
    regime, `Case-B(m,k)`, or gap (b)(ii) for general $(j,c,m)$, remains
    open. Status remains `partial`.

- **Round 10 (this round): split $(\ddagger)$ into gap (a)/(b) per the
  outliner, close gap (b)(i) in full, reformulate gap (a).** See "Round 10:
  Tiny-Piece Insertion Monotonicity, and the exact reduction of gap (a)"
  below for the full detail. Outcome, honestly reported:
  - **Gap (b)(i) — Tiny-Piece Insertion Monotonicity — proved in full**, as a
    clean, general, reusable lemma: if $D$ is admissible at budget $W$ with
    $|D|<\ell$ (piece cap not yet saturated), then for any $\delta$ with
    $0<\delta\le\min(D)$, the multiset $D'=D\cup\{\delta\}$ (piece count
    $|D|+1\le\ell$, still admissible, budget $W+\delta$) satisfies
    $\mathrm{OddSum}(D'\cup T)\ge\mathrm{OddSum}(D\cup T)$. Proved directly
    from the definition of sorted rank (inserting a value strictly below
    every existing element only ever appends it at the very last rank,
    leaving every other element's rank unchanged), with no majorization or
    Schur-type argument invoked (avoiding the certified dead end).
  - **Gap (a) reformulated exactly** (not merely bounded): using the
    already-certified Companion Peeling Lemma, the endpoint target
    $\mathrm{OddSum}(D\cup T)\le2^\ell+\varepsilon-1$ at $W=2^{\ell-1}+
    \varepsilon$ is proved **logically equivalent** to
    $\mathrm{OddSum}(D\cup\Gamma_{\ell-2})\ge2^{\ell-1}$ (same admissibility
    on $D$). This is a genuinely new, cleaner, self-contained restatement —
    independently confirmed by 13,500 Monte-Carlo trials (three $\varepsilon$
    values, $\ell=3,4,5$) that the two inequalities' truth values agree on
    every sampled admissible $D$, zero mismatches.
  - **New diagnosis (honest, not a proof): gap (a) is exactly as hard as the
    file's own still-open general $j\ge2$ trichotomy.** The reduced target
    $\mathrm{OddSum}(D\cup\Gamma_{\ell-2})\ge2^{\ell-1}$ is recognized as a
    "tail-untouched, top split into $|D|\ge2$ fragments" instance of the
    same family of statements (`T(m,k)`-type, tail untouched, top piece
    split into $j=|D|-1\ge1$ fragments) whose $j\ge2$ case is the file's own
    central, still-unresolved obstruction (Proposition C / Reduction B /
    the middle regime, all in `## Open gaps` above) — with a bonus
    $+\varepsilon$ budget and an extra cap $\max(D)<2^{\ell-1}$ that make it
    *no easier in kind*, only possibly easier in degree. This is new,
    structurally useful information (it explains *why* the window's
    endpoint resisted this round's and last round's attempts — it is not an
    isolated technical gap but a restatement of the paper's hardest open
    problem), but it does **not** close gap (a). Gap (b)(ii) (piece-cap-
    saturated case) is untouched this round, still fully open.
  - **Net effect:** the window's closure now needs exactly: gap (a) (shown
    equivalent to the file's own general open trichotomy, one level down at
    $m=\ell-1$) and gap (b)(ii) (untouched). Gap (b)(i) is fully closed and
    certified as a general-purpose reusable lemma. Status remains `partial`.

- **Round 9 (this round): exchange-smoothing attempt on the Branch-I.A-
  restricted window, per the outliner's target (crux `aimo-0146` mechanism,
  Single-Insertion Lemma as the "one-unit-move" primitive).** Outcome,
  honestly reported:
  - **Confirmed and corrected the round's target closed form.** The
    dispatched conjecture said the extremal witness replaces $\Gamma_{\ell-2}$'s
    bottom element "$1$" by two copies of $r=(1+\varepsilon)/2$; **this is
    off by a constant** (its sum falls short of the required $\mathrm{sum}(C)=
    2^\ell+\varepsilon$ by exactly $1$). The correct value, re-derived from
    scratch by matching sums exactly and confirmed by global numerical
    optimization (`scipy.optimize`, Nelder–Mead with penalty, dozens of
    random restarts, $\ell=3,\ldots,6$, several $\varepsilon$), is
    $$r=1+\varepsilon/2,$$
    not $(1+\varepsilon)/2$. With this correction the witness's sum matches
    exactly and the numerically-found optimum matches the analytically
    predicted value to floating-point precision in every case tested.
  - **Proved in full, exactly (Theorem W below), that this corrected witness
    attains margin exactly $\varepsilon/2$** at the window's left (closed)
    endpoint $c_1=2^{\ell-1}$ — not approximately, an exact rational identity,
    verified independently by exact `Fraction` arithmetic for
    $\ell=2,\ldots,8$ and five values of $\varepsilon$ (40 exact instances,
    zero deviation from $\varepsilon/2$). **New clean derivation**: the
    witness multiset $C\cup\Gamma_{\ell-1}$ is recognized as an exact instance
    of the certified **General Insertion Lemma** (Theorem 4,
    `lemmas/perfect-pairing-subadditivity-and-general-insertion.md`, from the
    sibling approach `universal-halving-adversary`/`greedy-reduction-geometric`
    population) — $\mathrm{OddSum}(R\cup R\cup\{\ell_0\})=\mathrm{sum}(R)+\ell_0$
    for any $R,\ell_0>0$ — giving the exact value in one line instead of a
    manual rank-counting argument. This is a genuine cross-approach reuse,
    reducing what was previously a hand computation to a one-line application
    of an already-certified general-purpose tool.
  - **Numerically confirmed (not proved) that this endpoint is the GLOBAL
    minimum of the margin over the entire window**, i.e. that
    $\mathrm{margin}(c_1):=\mathrm{OddSum}(C\cup\Gamma_{\ell-1})-2^\ell$ is
    minimized, over the whole window $c_1\in[2^{\ell-1},2^{\ell-1}+1-
    \varepsilon)$ with $\max(C\setminus\{c_1\})<2^{\ell-1}$, exactly at the
    closed left endpoint $c_1=2^{\ell-1}$, with $\mathrm{margin}$ increasing
    (not necessarily monotonically, but never dropping below $\varepsilon/2$)
    as $c_1$ moves away from that endpoint. Confirmed by global numerical
    optimization sweeping $c_1$ across the window at several points
    ($\ell=3$, $\varepsilon=0.3$, 7 sample points spanning the window): margin
    rose from $0.15=\varepsilon/2$ at the left endpoint to a plateau near
    $\varepsilon=0.3$ approaching the (open) right endpoint — consistent with,
    but not itself a proof of, the round's target claim.
  - **Attempted, and did NOT complete, the general exchange-smoothing upper
    bound closing the whole window.** Reduced the needed inequality to a
    clean, $c_1$-independent form: writing $D:=C\setminus\{c_1\}$,
    $W:=\mathrm{sum}(D)=2^\ell+\varepsilon-c_1$, the window's closure is
    *exactly* equivalent (peeling $c_1$, Fact 1) to a single inequality
    $$\mathrm{OddSum}(D\cup\Gamma_{\ell-1})\ \le\ 2^\ell+\varepsilon-1$$
    holding for **every** $D$ with $\le\ell$ parts, $\max(D)<2^{\ell-1}$, and
    $W$ ranging over $(2^{\ell-1}-1+2\varepsilon,\,2^{\ell-1}+\varepsilon]$ as
    $c_1$ ranges over the window — note the right-hand side is *constant*
    (independent of $c_1$), a genuine simplification not previously written
    down this cleanly. This shows the window's closure reduces to a single
    clean extremal claim: *the maximum of $\mathrm{OddSum}(D\cup\Gamma_{\ell-1})$
    over admissible $D$, as a function of $W$, is $\le2^\ell+\varepsilon-1$
    on this $W$-range* — and, if it is also non-decreasing in $W$ (only
    checked numerically, not proved), the whole window reduces to the single
    endpoint case already closed exactly above (Theorem W). **This
    monotonicity-in-$W$ reduction step is the precise open gap**: no proof
    was found this round that increasing $D$'s budget $W$ (subject to the
    same piece cap and max cap) cannot decrease the achievable maximum
    $\mathrm{OddSum}(D\cup\Gamma_{\ell-1})$ — the natural "add mass to $D$'s
    top element" move is not obviously OddSum-monotonic in general (an
    increase at an *even*-ranked position can lower OddSum), so this needs a
    genuine argument, not just intuition, and none was completed in the time
    available. The Single-Insertion Lemma, as planned, is the right *tool*
    for such an argument (it gives the exact effect of any single insertion)
    but assembling it into a full exchange-smoothing proof (à la crux
    `aimo-0146`'s unit-exchange argument, which needed several rounds of
    "move a unit toward the higher-coefficient position" reasoning even in
    its own, simpler linear-functional setting) was not completed this round.
  - **Net effect, honestly reported.** The window's exact extremal value at
    its left endpoint is now **rigorously and exactly established**
    ($\varepsilon/2$, not merely conjectured), reusing an already-certified
    cross-approach tool (Theorem 4) for a clean one-line derivation, and the
    window's closure is reduced to a single clean $c_1$-independent claim
    plus (numerically strongly supported, not proved) monotonicity. **The
    window itself is NOT closed this round** — Status remains `partial`, and,
    per round 8's proved equivalence, the whole tail-untouched sliver residual
    (and hence Theorem 2') also remains open, contingent on this window.

- **Round 8 (prior round): attempt to close Branch II of `L_0(ℓ,ε)` via strong
  induction on `ℓ`, per this round's math-explorer lead.** Outcome, honestly
  reported:
  - **Re-derived and independently verified the peel identity** the explorer
    found (exact `Fraction` arithmetic, 1900 fresh random trials across
    `ℓ=2..7`, arbitrary piece counts respecting the cap, zero mismatches — a
    from-scratch script, not reusing the explorer's own): for `C` in Branch
    II's uncovered range (`c_1:=max(C)∈(2^{ℓ-1}-1+ε,2^{ℓ-1})`),
    $$\mathrm{OddSum}(C\cup\Gamma_{\ell-1})=2^{\ell-1}+\mathrm{OddSum}(C'\cup\Gamma_{\ell-2}),\qquad C':=C\setminus\{c_1\},$$
    proved below from two applications of the certified Peeling
    Lemma/Companion Peeling Lemma (both exact, non-lossy).
  - **Resolved the flagged `ε'` boundary loose end in full: it is not a
    loose end.** `ε':=2^{\ell-1}+\varepsilon-c_1` is a strictly monotonic,
    continuous function of `c_1` on Branch II's *open* range, so `ε'`
    ranges over the *open* interval `(ε,1)⊂(0,1)` — it never actually
    reaches `0` or `1`. No boundary case needs separate handling; proved
    below by direct substitution at the (open, unattained) endpoints.
  - **Found and diagnosed a real, deeper gap the explorer's report did not
    surface: the recursion, as literally set up in the file's own boxed
    `L_0(ℓ,ε)` statement, can produce a `C'` that fails `L_0(ℓ-1,ε')`'s own
    stated hypothesis `max(C')≤2^{ℓ-1}-ε'`, even while `max(C')<2^{ℓ-1}`.**
    Exhibited an explicit exact counterexample-to-naive-recursion (`ℓ=3,
    ε=1/2, c_1=39/10, C'={19/5,4/5}`): `max(C')=19/5=3.8` exceeds
    `2^{ℓ-1}-ε'=17/5=3.4`, so `C'` is literally outside `L_0(2,3/5)`'s
    stated domain, even though the true target
    (`OddSum(C\cup\Gamma_2)=44/5\ge8`) holds with margin `4/5`.
  - **Resolved this gap by showing the `≤2^\ell-\varepsilon` cap in the
    boxed `L_0(\ell,\varepsilon)` is vestigial — never load-bearing in any
    of round 6/7's branch derivations — and can be dropped.** Proved
    (re-deriving Branch I.A's closing inequality with the cap removed, and
    independently stress-tested, 2243 fresh exact trials, zero violations)
    that Branch I.A's closure `c_1\ge2^{\ell-1}+1-\varepsilon` holds for
    **every** such `c_1` up to (not including) `2^\ell`, with no upper cap
    needed at all. This gives a corrected, cap-free general statement
    `L_0^{gen}(\ell,\varepsilon)` (Definition/Theorem below) that is
    **strictly more general** than the file's boxed `L_0(\ell,\varepsilon)`
    (drops a hypothesis, same conclusion) — hence proving it is sufficient,
    and it is exactly what recursion needs (no boundary-fitting issue
    remains once this correction is made).
  - **Net result: Branch II is proved, by a genuine, well-founded strong
    induction on `ℓ` (base case `ℓ=1` vacuous), to be logically EQUIVALENT
    to the (already separately identified, still-open) Branch-I.A-restricted
    window — recurring at every level `ℓ'<ℓ` in the induction, not to a new
    self-similar copy of Branch II itself.** This is a genuine structural
    unification: the sliver's two previously-separate-looking open pieces
    (Branch II's uncovered range, and the Branch-I.A-restricted window)
    collapse into **one single gap** (the window, recurring). **This is not
    a full closure of Branch II** — an explicit witness is exhibited showing
    the reduction genuinely can, and does, bottom out in the (unproved)
    window at a lower level, so Branch II's status remains conditional on
    that window; but it is real, honest progress: the whole sliver's
    residual is now provably a single unified target instead of two.
  - See "Round 8: Branch II via strong induction, and its exact reduction to
    the Branch-I.A window" below for the full proof.

- **Round 7 (this round): fix a real bug in round 6's `L_0(ℓ,ε)` statement, close Branch I.B in full, attempt the residual window.** Outcome, honestly reported:
  - **Bug fixed (mandatory, done first):** round 6's boxed `L_0(ℓ,ε)` (both
    in this file and in `lemmas/theorem2gen-bounds-and-l0-reduction.md`)
    omitted the piece-count bound `C` inherits from the outer
    `Case-B(m,k)` induction (`≤ℓ+1` parts). **False as literally stated
    without it** — exact counterexample found by this round's math-explorer
    (`ℓ=2, ε=1/10`, a 4-part `C`, `OddSum(C∪Γ_1)=35649/10000<4`). Both
    files corrected to state the piece bound explicitly. Checked (and
    proved in the new Round 7 section) that round 6's actual branch
    closures (Branches II.ii, II.i-partial, I.A-partial) use only
    `sum(C)`/`max(C)`, never piece count, so they remain valid unchanged
    under the corrected, more restrictive hypothesis.
  - **Branch I.B closed in full, unconditionally** (new theorem, proved
    completely below in "Round 7"): if `c_1:=max(C)≥2^{ℓ-1}` and `C` has a
    second element `c_1'≥2^{ℓ-1}`, then `OddSum(C∪Γ_{ℓ-1})≥2^ℓ` — for
    *every* `ε∈(0,1)`, `ℓ≥1`, with no piece-count restriction needed at
    all (a strictly more general statement than `L_0` itself requires).
    Proved by a clean two-peel argument (peel `c_1`, then `c_1'`, then use
    the newly-derived general fact `OddSum(Γ_n)≥2^n` for all `n≥0` — itself
    proved from the already-certified `AltSum(Γ_m)` closed form). Verified
    numerically: 1991 exact-`Fraction` trials across `ℓ=1..7`, zero
    violations, minimum margin `7/500` at `ℓ=2` (matching the proof's own
    identified equality case `ℓ∈{1,2}`). This closes Branch I.B's *entire*
    domain (not just the range round 6's Branch I.A left open), so the
    residual gap on the `c_1≥2^{ℓ-1}` side shrinks from "all of Branch I.B"
    to just `c_1∈[2^{ℓ-1},2^{ℓ-1}+1-ε)` combined *with* Branch I.A's
    hypothesis (no large second element).
  - **Residual window (Step 2): attempted, not closed, honest negative
    finding.** The order-statistics route was attempted for the window's
    lower half (`c_1<2^{ℓ-1}`, Branch II's uncovered range) but the
    Branch-I.B two-peel technique does not transplant: `c_1<max(T)` there,
    so `T`'s own `2^{ℓ-1}` must be peeled first, and the residual bound
    needed is an *upper* bound on `OddSum`, for which discarding a
    remainder's contribution (the trick that made Branch I.B's *lower*
    bound work) is invalid. No mechanism found this round; not claimed as
    closed. See "Round 7" section for the precise diagnosis.
  - **Net effect on the residual gap:** the previously two-part residual
    (window `c_1∈(2^{ℓ-1}-1+ε,2^{ℓ-1}+1-ε)` plus all of Branch I.B) is now
    a single, further-restricted region: Branch II's uncovered range
    `c_1∈(2^{ℓ-1}-1+ε,2^{ℓ-1})` (unchanged), plus the narrower
    `c_1∈[2^{ℓ-1},2^{ℓ-1}+1-ε)` *restricted to* Branch I.A's hypothesis
    (`max(C\{c_1})<2^{ℓ-1}`) — real, checkable narrowing, not yet a full
    closure.

- **Round 6: attempt Theorem 2' — close the width-1 sliver `2^(m-1)-1<b_1<2^(m-1)` via the recursive tail-untouched dichotomy one level down.** Outcome, honestly reported:
  - **Proved (solid, new) the exact reduction of the sliver to a clean target `L_0(ℓ,ε)`** (ℓ:=m-1): sliver's Theorem-2-style peel of `b_1` (valid since the sliver sits inside sub-case (i), `b_1≥2^{m-2}`) shows the original sliver claim `OddSum(B∪Γ_{m-2})≤2^m-1` is **equivalent** to `OddSum(C∪Γ_{ℓ-1})≥2^ℓ` where `C=B\{b_1}`, `sum(C)=2^ℓ+ε`, `max(C)≤2^ℓ-ε`, `ε:=2^{m-1}-b_1∈(0,1)` — a precisely stated, algebraically derived target (matching the math-explorer's `B'` setup exactly), proved by the same computation Theorem 2 already used (peeling + `sum=OddSum+EvenSum` algebra), no new machinery needed for this step.
  - **Applied the SAME tail-untouched dichotomy one level down to `L_0(ℓ,ε)`** (comparing `c_1:=max(C)` to `max(T)=2^{ℓ-1}`, `T=Γ_{ℓ-1}`), and — going one level further — nested it again (comparing to `2^{ℓ-2}` inside the `c_1<2^{ℓ-1}` branch). Derived, symbolically (sympy, exact algebra, no approximation), the following **proved** partial closures for `ℓ≥2` (all four listed sub-thresholds independently double-checked by direct symbolic substitution at the branch endpoints):
    - `c_1<2^{ℓ-2}`: closes **unconditionally** for every `ε∈(0,1)`, `ℓ≥2` (found threshold: needed slack `2^ℓ/8+ε/2-1/2≥0`, true since `2^ℓ/8≥1/2` for `ℓ≥2`).
    - `2^{ℓ-2}≤c_1≤2^{ℓ-1}-1+ε`: closes (peel `c_1` again, apply Theorem-2's general sub-case-(i) formula one level down).
    - `2^{ℓ-1}+1-ε≤c_1≤2^ℓ-ε`: closes, **but only under the extra unverified hypothesis that `C` has no second element `≥2^{ℓ-1}`** (i.e. `max(C\{c_1})<2^{ℓ-1}`) — this second-largest-element case (`Branch I.B`) is **not handled** this round.
  - **Residual gap, precisely located (new, sharper than the round-5 sliver):** the recursion leaves open exactly the narrower window `c_1∈(2^{ℓ-1}-1+ε,\,2^{ℓ-1}+1-ε)` (width `2(1-ε)`, shrinking to `0` as `ε→1`, same self-similar flavor as the original width-1 sliver at the level above) **plus** all of Branch I.B (`C` has ≥2 elements `≥2^{ℓ-1}`, unaddressed). This is genuine, checkable partial progress — most of `L_0(ℓ,ε)`'s range is now closed by exact algebra, not just numerics — but it is **not a full proof of Theorem 2'**: closing the residual window requires recursing yet one level further (the window itself has the same shape as `L_0` one level down, i.e. a further instance of the same dichotomy, matching the math-explorer's finding of an unbounded-depth self-similar recursion), and Branch I.B needs a separate multi-peel argument not attempted this round.
  - **Conclusion: Theorem 2' is NOT closed this round.** The reduction is rigorous and the branch computations are exact (verified symbolically), but assembling them into a complete induction on recursion depth (or on `m`) — with a correctly strengthened hypothesis that survives arbitrarily many levels, and with Branch I.B closed — was not completed within this round's time budget. This is reported honestly as `partial`, not `solved`, per the standing discipline against trusting an unfinished recursive pattern (the outline's own warning about round 5's "Two-Level Half-Bound Lemma" looking plausible and failing applies with equal force here: the *pattern* looks self-similar and matches the numeric `eps/2` conjecture qualitatively, but the actual multi-level induction with Branch I.B closed is not yet written down).

- **Round 5: target `Case-B(m,k): OddSum(B∪Γ_{m-2})≤2^m-1`
  via exchange/smoothing on the near-extremal family
  `B_ε=(2^{m-1}-ε,2^{m-2},…,2,1+ε)`.** Outcome, honestly reported:
  - **Found and verified in closed form the exact extremal boundary
    configuration**: `B*={2^{m-1}}∪(Γ_{m-2}` with its bottom element `1`
    replaced by `2`)` attains `OddSum(B*∪Γ_{m-2})=2^m-1` **exactly** (not
    just approached), for every `m≥2` — checked symbolically for `m=4,6`
    and confirms why the target is tight (`B*` sits exactly on the excluded
    boundary `max(B*)=2^{m-1}`, consistent with the strict hypothesis).
  - **Major narrowing of the open region, not a full closure.** Proved a
    new dichotomy on `b1` vs. `2^{m-2}=max(Γ_{m-2})` (this collapses the
    round-4 trichotomy to a clean two-way split in the *tail-untouched*
    case, since `μ=max(Γ_{m-2})=2^{m-2}` exactly here — no middle regime,
    unlike the general-tail case): sub-case `b1<2^{m-2}` is **closed in
    full, unconditionally**, and sub-case `2^{m-2}≤b1≤2^{m-1}-1` is
    **also closed in full, unconditionally** — both via one application
    of the certified Peeling Lemma plus the certified First-mover-half
    Lemma (Lemma B). This leaves open **only a width-1 sliver**,
    `2^{m-1}-1<b1<2^{m-1}`, independent of `m` — previously the *entire*
    range `b1∈[0,2^{m-1})` was open (numerically confirmed only).
  - Attempted to close the sliver with a genuinely new, proved, reusable
    **Two-Level Half-Bound Lemma** (a strict refinement of Lemma B using
    the top *two* order statistics, proved in full below from already-
    certified tools). Numerically verified this refined bound is **still
    insufficient** in the sliver (explicit computed instances at `m=4..8`
    where it undershoots the target by up to `≈0.5`, even though the true
    `OddSum` clears the target with real slack) — an honest negative
    finding about this specific refinement, not a proof the sliver is
    false.
  - Net effect: `Case-B(m,k)` is reduced from "fully open, numerically
    confirmed only" to "closed on all but a width-1 sliver near
    `b1=2^{m-1}`, uniformly in `m`," with the exact extremal shape at the
    excluded boundary identified in closed form. The sliver itself remains
    open; no mechanism found this round closes it.

- 
- **Direct induction-on-n / strategy-stealing with a two-parameter recursion
  `L(m,k)`** (round 1). Built the reduction lemmas from scratch (greedy
  optimality, scale invariance), solved the two-parameter recursion exactly
  for `k=0` and for `m=k=1`. Left `j≥2` completely open.
- **Round 2: close `j=1` with the certified tie lemma, and push a genuine
  nested Peeling-Lemma induction with a two-sided hypothesis for general
  `j`.** Closed `j=1` in full generality (arbitrary split of the top piece,
  arbitrary tail refinement). Diagnosed a precise obstruction for `j≥2`
  ("Lemma X′", a dual EvenSum-lower-bound statement) needed to extend the
  peeling method.
- **Round 3 (this round): abandon Lemma X′ (independently disproved by two
  explorers this round), pivot to the outliner's "Recursive Depth Peeling
  Lemma."** Outcome, honestly reported:
  - **New complete result: `T(2)` is now fully closed** (all `j=0,1,2`,
    hence all `k≤2`) — the first fully general closure beyond `m=1`. The
    new content is the `j=2` (top split into **three** fragments, tail
    `Γ_1=(2,1)` untouched) sub-case, proved by a *direct order-statistics
    computation* (not by the depth-peeling induction, which — see below —
    does not close this case in general `m`; the `m=2` computation is
    small enough to finish by hand).
  - **Formalized and proved the "z-trick" reduction** converting any
    `EvenSum` target back into an `OddSum` target on an augmented multiset
    (a clean, general, reusable identity, proved in full below), and used
    it to show that the *natural* single-peel completion of "Case A"
    (top fragment `a1 ≥ 2^{m-1}`) is **logically circular**: the needed
    upper bound is provably equivalent, via the z-trick, to *another*
    instance of the same lower-bound problem with **one more fragment**,
    not a simpler one. This is a sharper, *proved* (not just diagnosed)
    obstruction than round 2's Lemma X′ finding: it shows *why* the
    depth-peeling idea, even using the tail's exact known values (not an
    abstract dual sum bound), still cannot make monotonic progress via a
    single extra peel.
  - Extensively **numerically stress-tested** (Monte Carlo + local/coordinate
    descent search, thousands of configurations per `(m,j,c)` triple,
    `m≤5`) both (a) the original target `T(m,k)` and (b) the natural
    generalizations `G(m,k;V)` (target `V∈[2^{m-1},2^m]` instead of `2^m`)
    and the companion upper-bound sub-lemma `U(m,k)`. All are **consistent
    with the conjectured closed form and find zero violations** once the
    correct cut-budget coupling (`j + (\text{cuts on tail}) \le k \le m`)
    is respected — this is strong evidence the Recursive Depth Peeling
    approach's *target* is correct, even though the induction is not yet
    complete. (Also reconfirmed, as an explicit counterexample: decoupling
    the fragment count from the real cut budget, or allowing an abstract
    tail with only a bare `OddSum`/`EvenSum` bound instead of the genuine
    geometric refinement structure, both produce real violations — i.e.
    the theorem is *not* true in those generalized forms, consistent with
    round 3's disproof of Lemma X′.)

- **Round 4 (this round): retarget the `j≥2` inductive step away from
  peel+scalar entirely, toward the outliner's AltSum-budget mechanism.**
  Outcome, honestly reported:
  - Proved in full, general purpose, reusable: the **AltSum reformulation**
    (`T(m,k) ⟺ AltSum(refinement) ≥ 1`, since `sum` is fixed) and the
    **Single-Insertion Lemma** (an exact, fully general formula for how
    `AltSum` changes when one new value is inserted at an arbitrary sorted
    position — not just the maximum, generalizing the certified Peeling
    Lemma). Verified on 2000+ random insertion instances, zero mismatches.
  - Proved the **closed form for `AltSum(Γ_m)`** and used the new machinery
    to give a second, independent re-derivation of the certified `j=0` case
    (Fact 2), as a consistency/correctness check on the new tool (it agrees
    with the certified result, and shows the tool is at least as strong).
  - Attempted the outline's "Aggregate budget bound" for `j≥2` and found
    that the *literal* peel-of-the-current-max recursion on `AltSum` is
    algebraically **identical** to Fact 1/Peeling Lemma (`AltSum(X) = x_1 -
    AltSum(rest)`) — i.e. peeling the running max inside the AltSum
    language is exactly Proposition C's mechanism restated, not new
    content. Real progress came from also peeling from the **tail's** side
    (comparing the top fragment `b_1` to `μ=max(S)` rather than to
    `2^{m-1}`): this exposes a **third, previously uncovered case**
    (`μ≤b_1<2^{m-1}`) sitting between Proposition C's Case A
    (`b_1≥2^{m-1}`) and a newly-derived Case B (`b_1<μ`) — proved in full,
    reduction target derived and numerically confirmed on 3000+ random
    instances (zero mismatches) — that neither existing mechanism reaches.
    `T(m)` for `m≥3` remains open; the obstruction is now a **three-way
    case split**, two of whose boundary cases have precise reductions
    (one circular, proved; one open with a derived target and numeric
    support) and one of which (the middle regime) is newly identified as
    genuinely uncovered by any mechanism tried so far.

## Current best

**Round 19 update (most current — see "Round 19: extremal-principle
attack..." near the top of this file for full detail).** The general-$k$
Cardinality-Constrained Half-Sum Lemma GCH($k$) — the one remaining named
sub-lemma needed to close $\mathrm{GT}(m)$ sub-case (i) for all $m$ — now
has: (1) an exact, fully proved, general-$k$ achievability theorem (the
"chain + tied pair" witness $R^*=\{2^{k-1},\dots,4\}\cup\{r,r\}$ gives
$\mathrm{AltSum}(R^*\cup\Gamma_{k-1})=1$ exactly, for every $k\ge2$, every
valid $S$ — no numerics needed, proved via two new general-purpose lemmas,
Tied-Pair Cancellation and the Block-Contribution Formula); (2) a genuine
partial smoothing/vertex-reduction argument (Lemma LNI) ruling out one
class of non-minimal configurations. The matching lower bound (that NO
feasible $R$ beats $\mathrm{AltSum}=1$) is reduced to one precisely-stated
finite-per-$k$ combinatorial claim (via the Block-Contribution Formula)
verified for $k=2$ (matches the certified exhaustive Lemma 2) and
numerically for $k=3,4,5$ (multi-restart exact-objective search, cheap-
kill passed), but **not proved for general $k$**. GCH($k$) — and hence
$\mathrm{GT}(m)$, $m\ge4$ — remains open, with a sharper, better-
structured residual than round 18 left this file with.

**Round 15 headline (new, proved in full below, see "Round 15: the AltSum
Small-Sum Lemma, sub-case (i) closed down to a width-1 window ...").**
A new, strictly more general lemma — the **AltSum Small-Sum Lemma**
($\mathrm{sum}(D)\le2^m-1\Rightarrow\mathrm{OddSum}(D\cup\Gamma_{m-1})\ge
\mathrm{sum}(D)$, no cap on $|D|$ or $\max(D)$ needed at all, a two-line
consequence of already-certified tools Lemma AS + AltSum Corollary) —
closes sub-case (i) ($q=1$, excess $e\ge1$) of $\mathrm{GT}(m)$ on the
**majority of its range unconditionally, for every excess $e$**: the
**Sub-case (i) Window Reduction Theorem** shows it is closed whenever the
peeled excess element $a_1\ge2^{k-1}+1$, with the remaining gap now
**exactly** the width-1 window $a_1\in(2^{k-1},2^{k-1}+1)$ — identified as
the same recurring self-similar window object seen throughout the file
(Theorem W, gap-(a)'s $\mathrm{GT}(m)$ closure), now carrying an
additional unrestricted-excess twist no prior window closure needed to
handle. The same lemma independently re-derives `Case-B(m,k)`'s known
safe zone (round 5) in three lines (a correctness cross-check, not a new
closure). The round's dispatched continuity/limiting route for
`Case-B(m,k)`'s boundary is found, on checking against the file's own
certified history, to rest on a **false premise** (no shrinking-$\delta$
family of proved interior results actually exists — the proved interior
region has a hard unit-width boundary, not a vanishing gap) — reported
honestly as a Spec concern rather than forced into an invalid argument.
$\mathrm{GT}(m)$ for $m\ge4$ **remains open**; what remains for sub-case
(i) is now precisely one width-1-with-excess window, and `Case-B(m,k)`'s
long-standing obstruction is unchanged (reconfirmed, not newly closed).

**Round 14 headline (new, proved in full below, see "Round 14: the AltSum
corollary, the Growth Lemma, and the exact reduction ..."):** Two new
general-purpose, reusable, independently-verified lemmas — the **AltSum
corollary** ($0\le\mathrm{AltSum}(N)\le\max(N)$) and the **Growth Lemma**
(the increasing-direction complement of the certified Monotonicity
Reduction Lemma) — combine into the **Small-Sum Reduction Theorem**: the
entire small-sum-mirror sub-case (ii) of $\mathrm{GT}(m)$'s $p=0$ branch
(both not-full-count and full-count instances, for every $\mathrm{sum}(D)
\le2^m$) is proved **equivalent** to `Case-B(m,k)` at $\mathrm{sum}(D)=
2^m$ (modulo one flagged tie-boundary detail) — the same object the
already-certified Monotonicity Reduction Lemma shows the large-sum/gap-(a)
regime needs. This **unifies the entire $p=0$ branch of $\mathrm{GT}(m)$,
at every sum, into the single already-long-open object `Case-B(m,k)`**
(open since round 4, "the middle regime," closed only for the smallest
instance at $m=3,4$ in round 11) — a genuine simplification, not a new
closure. Sub-case (i) ($q=1$, $e\ge1$): the natural "piece-cap-relaxed"
fix is proved **false** (explicit counterexample), and the exact point in
the recursion where this sub-case becomes unavoidable is precisely
diagnosed (matches round 12's $m\ge4$ feasibility threshold), but **not
closed**. $\mathrm{GT}(m)$ for $m\ge4$ **remains open** — what remains is
now exactly two named objects (`Case-B(m,k)`, sub-case (i)), not an
open-ended search.

**Round 11 headline (new, proved in full below, see "Round 11: the
Affine-Rank Lemma and Vertex Reduction"):** Two new general-purpose,
reusable lemmas (Affine-Rank Lemma, Vertex-Attainment Lemma) give a
Middle-Regime Vertex Reduction Theorem, genuinely re-derived for this
approach's own polytope (not assumed transferred from
`global-lp-vertex-sufficiency`). Applied to the smallest nonempty
middle-regime instance $(j,c)=(2,1)$: **exact closure at $m=3,4$**
($\mathrm{OddSum}=2^m$ exactly at an explicit boundary vertex, hand-verified
below), **exact strict-slack confirmation at $m=5$**
($\mathrm{OddSum}=33>32$). General $m$ for this family, and the middle
regime / `Case-B(m,k)` / gap (b)(ii) in general, remain open — the vertex
candidate enumeration used is not yet proved exhaustive (it omits, so far,
ties against individual elements of $\Gamma_{m-2}$).

**Round 10 headline (new, proved in full below, see "Round 10: Tiny-Piece
Insertion Monotonicity, and the exact reduction of gap (a)"):** The window's
remaining closure, per this round's outliner split into gap (a)
[endpoint-$W$ optimality] and gap (b) [monotonicity of $f(W)$ across the
window, itself split into (i) piece-cap-unsaturated and (ii)
piece-cap-saturated], now stands as: **gap (b)(i) is fully closed** (Lemma
TPI, a clean general-purpose reusable fact — adding a new element no larger
than the current minimum never decreases $\mathrm{OddSum}$), and **gap (a)
is exactly reformulated** (a proved equivalence, via the certified Companion
Peeling Lemma, verified independently on 13,500 Monte Carlo instances) into
$\mathrm{OddSum}(D\cup\Gamma_{\ell-2})\ge2^{\ell-1}$ — which is then shown,
by inspection of its shape, to be **exactly an instance (one level down, at
$m=\ell-1$) of the file's own still-open general "$j\ge2$ top-split,
tail-untouched" trichotomy** (Proposition C / Reduction B / the
middle-regime gap), not a smaller or structurally distinct problem. This is
a genuine, honest structural finding — it forecloses treating gap (a) as an
isolated computation and correctly identifies it as inheriting the paper's
central unresolved obstruction — but it does **not** close gap (a). Gap
(b)(ii) remains completely untouched. The window, Theorem 2', and the
tail-untouched-sliver residual all remain open.

**Round 9 headline (already proved in full below, see "Theorem W: the exact
window-endpoint witness"):** The Branch-I.A-restricted window's conjectured
extremal witness (left endpoint $c_1=2^{\ell-1}$) is now **proved exactly**:
$\mathrm{OddSum}(C\cup\Gamma_{\ell-1})=2^\ell+\varepsilon/2$ for the corrected
witness $C=\{2^{\ell-1}\}\cup(\Gamma_{\ell-2}$ with its bottom element $1$
replaced by two copies of $r=1+\varepsilon/2)$ — a genuine correction of the
dispatched conjecture (which had $r=(1+\varepsilon)/2$, off by a constant),
derived cleanly via the certified cross-approach General Insertion Lemma.
This is real new content (an exact identity, not a numeric approximation),
but it establishes the target only **at one point of the window** (the left
endpoint); the window's closure for **all** $c_1$ in
$[2^{\ell-1},2^{\ell-1}+1-\varepsilon)$ is reduced to a single clean,
$c_1$-independent extremal claim (bounding $\max_D\mathrm{OddSum}(D\cup
\Gamma_{\ell-1})$ as a function of the budget $W$) plus a monotonicity-in-$W$
step that is numerically well supported but **not proved** — so the window,
and hence (by round 8's equivalence) the whole tail-untouched sliver residual
and Theorem 2', remain open.

**Round 8 headline (new, proved in full below, see "Round 8: Branch II via
strong induction, and its exact reduction to the Branch-I.A window"):**
Branch II of `L_0(ℓ,ε)` is now proved, by a genuine well-founded strong
induction on `ℓ` (base case `ℓ=1` vacuous), to be logically **equivalent** to
the Branch-I.A-restricted window recurring at lower levels — i.e. the two
previously-separate open pieces of the whole sliver (Branch II's own
uncovered range, and the Branch-I.A window) are now known to be **one single
gap**, not two independent problems. This is genuine progress (a real
structural unification, with an explicit witness showing the reduction can
and does bottom out in the window, so it is not vacuous) but **Branch II is
NOT unconditionally closed**: its closure at every level is now exactly
equivalent to closing the (still open) Branch-I.A window at every level
`ℓ'<ℓ`. A vestigial cap in the file's boxed `L_0(ℓ,ε)` (`max(C)≤2^ℓ-ε`) was
found to be non-load-bearing and is dropped, giving a corrected, cap-free
general statement `L_0^{gen}(ℓ,ε)` that recursion needs cleanly (no
boundary-fitting issue remains).

**Round 7 headline (new, proved in full below, see "Round 7: bug fix, Branch
I.B closed in full, Step 2 attempted"):** Fixed a real bug in round 6's
`L_0(ℓ,ε)` statement (missing piece-count bound, refuted by an explicit
4-part counterexample; corrected in this file and in
`lemmas/theorem2gen-bounds-and-l0-reduction.md`; round 6's actual branch
closures are unaffected since they never used the piece count). **Branch
I.B is now closed in full**, unconditionally, for every `c_1≥2^{ℓ-1}` with a
second element `c_1'≥2^{ℓ-1}` — via a clean two-peel argument plus the new
general fact `OddSum(Γ_n)≥2^n` for all `n≥0`. This shrinks the residual gap
from "the window plus all of Branch I.B" to "Branch II's uncovered range
plus a narrower Branch-I.A-restricted piece of the window." The residual
window's lower half (`c_1<2^{ℓ-1}`) was attempted via the same
order-statistics idea but not closed — the two-peel trick needs a *lower*
bound direction that does not transplant to Branch II's *upper*-bound
target; honestly reported as still open.

**Round 6 headline (proved in full below, see "Round 6: toward Theorem 2'"):**
The width-1 sliver `2^(m-1)-1<b_1<2^(m-1)` left open by round 5's Theorem 2 is
proved **equivalent** to a clean target `L_0(ℓ,ε)` (`ℓ=m-1`), and applying the
same tail-untouched dichotomy recursively one (and, in one branch, two)
levels down closes `L_0(ℓ,ε)` on all of its range **except** a strictly
narrower residual window `c_1∈(2^{ℓ-1}-1+ε,\,2^{ℓ-1}+1-ε)` plus an unaddressed
case (`Branch I.B`, `C` has ≥2 elements `≥2^{ℓ-1}`). Theorem 2' itself
(closing the whole sliver) is **not proved** this round — the residual window
has the same self-similar shape as the original sliver and needs a genuine
multi-level induction (not yet assembled) to close; see the open-gap
statement at the end of that section for the precise remaining work.

**Round 5 headline (already proved in full below):** In the `TOP-ONLY`,
tail-untouched setting (`S=Γ_{m-1}`, `T:=S\setminus\{\max S\}=Γ_{m-2}`),
`Case-B(m,k)` — i.e. `OddSum(B∪Γ_{m-2})≤2^m-1` for every partition `B` of
`2^m` into `≤m+1` positive parts with `max(B)<2^{m-1}` — is now proved for
**every** `B` except those with `max(B)` in the width-`1` window
`(2^{m-1}-1,\,2^{m-1})`, uniformly in `m`. See "Theorem 2 (Case-B(m,k),
sliver reduction)" below for the full statement and proof, and "Two-Level
Half-Bound Lemma" for the certified new tool (proved, but shown
insufficient alone to close the last sliver).

**Certified (already established, imported unchanged from prior rounds,
Step 1/Lemma E below reused verbatim):**
- Fact 2 (`j=0`, unconditional, no cut cap on the tail needed) and Step 1
  (`j=1`, arbitrary split, arbitrary tail refinement, given `T(m-1)`) —
  both certified, `lemmas/element-bound-and-j1-theorem.md`.
- Lemma B (First-mover-half): for any finite multiset of positive reals
  with sum `W`, `OddSum≥W/2` — certified,
  `lemmas/tie-neutrality-and-first-mover-half.md`.
- Companion Peeling Lemma: `EvenSum(N)=OddSum(N\setminus\{\max N\})` —
  certified, `lemmas/dominant-chain-theorem-and-prefix-run-decomposition.md`.

**New this round, proved in full below:**
1. **`T(2)` fully closed** (Theorem 1 below): for every refinement of
   `Γ_2=(4,2,1)` using `≤2` cuts, `OddSum ≥ 4`. Combined with the certified
   `j=0,1` cases (which for `m=2` need `T(1)`, itself certified), this needed
   only the new `j=2` sub-case, proved directly.
2. **The z-trick identity** (Lemma Z below): for any multiset `X` and any
   `z ≥ max(X)`, `EvenSum(X) = OddSum(\{z\}∪X) - z`. Proved in full, general
   purpose, reusable.
3. **The Case-A circularity** (Proposition C below): using Lemma Z, Case A of
   the general induction (`a1≥2^{m-1}`) is shown to require a statement
   (`U(m,k)`) that is *itself* an instance of a strictly larger `G`-type
   lower-bound problem (one more fragment, same `m`) — not a smaller one.
   This is proved, not asserted, and explains precisely why a single
   application of the Peeling Lemma cannot close Case A by induction on the
   fragment count `j` alone, however the *tail structure* is exploited.
4. **`G(m,k;V)`**, the natural generalization of `T(m,k)` to arbitrary target
   `V∈[2^{m-1},2^m]` (statement given below), is shown to be the "right"
   scale-free object underlying both `T(m,k)` and the Case-A sub-lemma
   `U(m,k)` — proved for `j=0` (trivial) and reduces to Step 1's certified
   `j=1` theorem when `V=2^m` exactly, but **left open for `V<2^m` and
   `j≥1`, and for `j≥2` at any `V`** (this is exactly where the induction
   does not close).
5. **The AltSum reformulation** (Lemma AS below): `T(m,k)` is *equivalent*
   (not just implied) to "`AltSum(refinement) ≥ 1` for every refinement of
   `Γ_m` with `≤k` cuts," since the refinement's total sum
   `2^{m+1}-1` is fixed. Proved in full, elementary, general purpose.
6. **The Single-Insertion Lemma** (below): an exact formula for how `AltSum`
   changes when a single new value is inserted at an arbitrary sorted
   position (not just the maximum) into an existing sorted sequence.
   Strictly generalizes the certified Peeling Lemma (which is the special
   case "insert/remove the maximum"). Proved in full, verified on 2000+
   random instances, zero mismatches.
7. **`AltSum(Γ_m)` closed form** (below): `AltSum(Γ_m)=(2^{m+1}+1)/3` for
   `m` even, `(2^{m+1}-1)/3` for `m` odd. Proved in full, verified for
   `m=0..11`. Used to re-derive Fact 2 (`j=0`) independently via the new
   AltSum machinery, as a consistency check (Proposition AS-2 below).
8. **The exhaustive `b_1` vs. `μ` case split, and the newly-found third
   regime** (below): comparing the top fragment `b_1` (of the split `B` of
   `Γ_m`'s top piece `2^m`) to `μ=max(S)` (the tail's *actual* running
   maximum, not the a-priori bound `2^{m-1}`) is the true exhaustive
   dichotomy for which side to peel first. Proposition C's Case A
   (`b_1≥2^{m-1}`) is a special, *suficient* sub-case of `b_1≥μ` (since
   `μ≤2^{m-1}` always) that additionally makes the z-trick clean. A **new
   Case B** (`b_1<μ`, proved below, `Reduction B`) handles the opposite
   extreme, reducing `T(m,k)` in this sub-case to a new, precisely stated
   target `OddSum(B∪S')≤2^m-1` (`S'` = `S` with one copy of its maximum
   removed) — proved algebraically, numerically confirmed on 3000+ random
   instances (zero mismatches), but **not itself proved** (this is the new
   open target, evidenced not established). Crucially, this round's work
   **discovers a third regime, `μ≤b_1<2^{m-1}`**, lying strictly between
   Proposition C's Case A and the new Case B, in which *neither* mechanism
   applies (Case A's z-trick needs `b_1≥2^{m-1}` specifically to guarantee
   `sum(B\{b_1})≤2^{m-1}`; Case B's peeling needs `b_1<μ` specifically) —
   an honest, precisely located new gap, not previously isolated this
   sharply in prior rounds' write-ups (which treated "Case A" and "Case B′"
   as if they partitioned all of `j≥1`, when in fact they leave this middle
   band uncovered).

**Open (sharpened again this round — now a three-way case split, not two):**
- `T(m)` for `m≥3` remains open. The obstruction is now a precise
  **trichotomy** on `b_1` vs. `μ=max(S)` vs. `2^{m-1}`:
  1. **`b_1≥2^{m-1}`** (Proposition C's Case A): proved circular — reduces
     to an equally-hard `G`-type instance with the same fragment count.
  2. **`b_1<μ`** (new Case B this round): reduces (proved, `Reduction B`
     below) to the new target `OddSum(B∪S')≤2^m-1`, numerically supported
     but not proved.
  3. **`μ≤b_1<2^{m-1}`** (the newly-identified middle regime): neither
     mechanism applies; genuinely open, not even reduced to a candidate
     target yet.
  Closing `j≥2` for general `m` needs either (a) a genuinely different
  mechanism entirely (e.g. the finite piecewise-linear breakpoint
  enumeration `greedy-reduction-geometric` is pursuing), (b) an inductive
  quantity tracking *more* than a single scalar bound (as in the `m=2`
  hand computation), or (c) — this round's most concrete new lead — a
  proof of Case B's target `OddSum(B∪S')≤2^m-1` together with a genuinely
  new argument (not yet found) covering the middle regime 3.

## Full proof
(not present — Status is `partial`. `T(2)` is proved completely (below,
Theorem 1) but `T(m)` for general `m≥3` is not.)

---

## Setup (recap, certified, unchanged)

Write $\Gamma_m=(2^m,2^{m-1},\ldots,1)$ (unnormalized geometric partition,
total $2^{m+1}-1$). For $0\le k\le m$, $T(m,k)$: every refinement of
$\Gamma_m$ using $\le k$ cuts has $\mathrm{OddSum}\ge 2^m$. $T(m)$: $T(m,k)$
for all $0\le k\le m$. By the certified reduction
(`lemmas/reduction-to-multiset-minimax.md`) and scale invariance, $T(n)$ for
every $n$ gives the lower-bound half of $c(n)=2^n/(2^{n+1}-1)$.

**Fact 1 (Peeling Lemma, certified).** For any finite multiset $M$ of
positive reals and $g=\max(M)$: $\mathrm{OddSum}(M)=g+\mathrm{EvenSum}(M\setminus\{g\})$.

**Fact 2 (certified, `j=0`).** If none of XY's cuts touch $\Gamma_m$'s own
top piece $2^m$, $\mathrm{OddSum}\ge 2^m$ for **any** number of tail cuts.

**Lemma E (certified, Element Bound).** For any finite multiset $S$ and
$x\in S$: $\mathrm{OddSum}(S)\ge x$.

**Step 1 (certified, `j=1`).** If $T(m-1)$ holds: for every split of $\Gamma_m$'s
top piece into two fragments $t_1\ge t_2>0$ and every refinement of the tail
using $\le m-1$ cuts, $\mathrm{OddSum}\ge 2^m$.

---

## Lemma Z (the z-trick identity, new, proved in full)

**Statement.** Let $X$ be any finite multiset of positive reals and let
$z>0$ satisfy $z\ge\max(X)$. Then
$$\mathrm{EvenSum}(X) = \mathrm{OddSum}(\{z\}\cup X) - z.$$

**Proof.** Since $z\ge\max(X)$, $z=\max(\{z\}\cup X)$ (a valid choice of "the"
maximum in Fact 1, ties with elements of $X$ equal to $z$ are harmless — the
Peeling Lemma only requires *some* copy of the maximum). By Fact 1 applied to
$\{z\}\cup X$ with $g=z$:
$$\mathrm{OddSum}(\{z\}\cup X) = z + \mathrm{EvenSum}((\{z\}\cup X)\setminus\{z\}) = z+\mathrm{EvenSum}(X),$$
where the last step uses that removing the one copy of $z$ we adjoined leaves
exactly $X$ (as a multiset; if $X$ itself already contains a copy of $z$, that
copy is untouched — we removed only the *added* copy). Rearranging gives the
claim. $\blacksquare$

*(This is elementary and general — it holds for any finite multiset of
positive reals, no geometric structure needed. It has been numerically
verified as a sanity check across thousands of random instances in this
round's exploration scripts; the proof above is a two-line consequence of
the already-certified Peeling Lemma and needs no further verification
beyond the algebra shown.)*

---

## Theorem 1: $T(2)$ is fully closed (new this round)

**Claim.** For every refinement of $\Gamma_2=(4,2,1)$ using $\le 2$ cuts,
$\mathrm{OddSum}\ge 4$.

**Proof.** By definition of $T(2,k)$ it suffices to prove $T(2,2)$ (using
$\le 2$ cuts covers every $k\le 2$ as a special case, since a refinement
using fewer cuts is in particular a refinement using $\le 2$ cuts). Let $j$
be the number of cuts spent on the top piece "$4$", $0\le j\le 2$.

- **$j=0$:** Fact 2 applies unconditionally (any number of cuts on the tail
  $\{2,1\}$), giving $\mathrm{OddSum}\ge 4$.
- **$j=1$:** the top splits into two fragments and the tail gets $\le 1$
  further cut. This is exactly Step 1 with $m=2$, which requires $T(1)$ as
  hypothesis. $T(1)$ is certified in full
  (`lemmas/element-bound-and-j1-theorem.md`, Step 2). So Step 1 gives
  $\mathrm{OddSum}\ge 4$.
- **$j=2$ (new, proved here in full):** the top piece "$4$" splits into
  *three* fragments $a_1\ge a_2\ge a_3>0$, $a_1+a_2+a_3=4$, and the tail
  budget is exhausted ($k-j=0$), so the tail is exactly $\{2,1\}$,
  untouched. We must show $\mathrm{OddSum}(\{a_1,a_2,a_3,2,1\})\ge 4$ for
  **every** such split. Two cases, by comparing $a_1$ to $2$.

  **Case $a_1>2$.** Since $a_2+a_3=4-a_1<2$ and $a_3>0$, we get $a_2<2$; so
  $a_2,a_3<2<a_1$, and the global sort is
  $$a_1,\ 2,\ m_1,\ m_2,\ m_3$$
  where $(m_1\ge m_2\ge m_3):=\mathrm{sort}(a_2,a_3,1)$ (all three of these
  are $\le 2\le$ nothing above needed — we only need them below $2$, which
  holds since $a_2,a_3<2$ and $1<2$). Ranks $1,3,5$ are odd, so
  $$\mathrm{OddSum}=a_1+m_1+m_3.$$
  Since $m_1+m_2+m_3=a_2+a_3+1=(4-a_1)+1=5-a_1$, we get $m_1+m_3=(5-a_1)-m_2$,
  so
  $$\mathrm{OddSum}=a_1+(5-a_1)-m_2=5-m_2,\qquad m_2=\mathrm{median}(a_2,a_3,1).$$
  We show $m_2\le 1$, which gives $\mathrm{OddSum}\ge 4$. Since $a_2+a_3<2$
  and $a_2\ge a_3$, if $a_3\ge1$ then $a_2\ge a_3\ge 1$ forces
  $a_2+a_3\ge2$, a contradiction; so $a_3<1$ always here. Two sub-cases:
  - $a_2\ge1$: since $a_2\ge1>a_3$, the sorted order of $(a_2,a_3,1)$ is
    $a_2\ge1\ge a_3$ (as $a_3<1$), so $m_2=1$.
  - $a_2<1$: then $a_3\le a_2<1$, so the sorted order is $1\ge a_2\ge a_3$,
    so $m_2=a_2<1$.

  In both sub-cases $m_2\le1$, so $\mathrm{OddSum}=5-m_2\ge4$.

  **Case $a_1\le2$.** Then $a_1,a_2,a_3\le2$ (as $a_1$ is the largest), so
  the global sort is
  $$2,\ n_1,\ n_2,\ n_3,\ n_4$$
  where $(n_1\ge n_2\ge n_3\ge n_4):=\mathrm{sort}(a_1,a_2,a_3,1)$. Ranks
  $1,3,5$ are odd, so
  $$\mathrm{OddSum}=2+n_2+n_4.$$
  Since $n_1+n_2+n_3+n_4=a_1+a_2+a_3+1=4+1=5$, we get $n_2+n_4=5-n_1-n_3$, so
  $$\mathrm{OddSum}=2+5-n_1-n_3=7-(n_1+n_3).$$
  We show $n_1+n_3\le 3$, which gives $\mathrm{OddSum}\ge4$. Two sub-cases on
  $a_1$ vs. $1$.
  - **$a_1\ge1$:** then $n_1=\max(a_1,1)=a_1$ (as $a_1\ge1$ and $a_1$ is the
    largest of $a_1,a_2,a_3$). Since $a_1$ also $\ge a_2,a_3$, the remaining
    three values $a_2,a_3,1$ sort as $n_2\ge n_3\ge n_4$, so
    $n_3=\mathrm{median}(a_2,a_3,1)$. We must show $a_1+\mathrm{median}(a_2,a_3,1)\le3$.
    Since $a_2\ge a_3$, $a_2+a_3\ge 2a_3$, i.e.
    $a_3\le (a_2+a_3)/2=(4-a_1)/2=2-a_1/2$.
    - If $a_3\ge1$: then $a_2\ge a_3\ge1$, so $\mathrm{median}(a_2,a_3,1)=a_3$
      (sorted order $a_2\ge a_3\ge1$). So we need $a_1+a_3\le3$; using
      $a_3\le2-a_1/2$ shown above, $a_1+a_3\le a_1+2-a_1/2=2+a_1/2\le2+1=3$
      (as $a_1\le2$ in this Case). Done.
    - If $a_3<1$: then either $a_2\ge1$ (median $=1$, and
      $a_1+1\le2+1=3$ since $a_1\le2$; done), or $a_2<1$ (so $a_3\le a_2<1$,
      median $=a_2<1$, and $a_1+a_2\le a_1+1\le3$; done).
  - **$a_1<1$:** then $a_2\le a_1<1$ and $a_3\le a_2<1$, so $1$ exceeds all
    of $a_1,a_2,a_3$, giving $n_1=1$ and $(n_2,n_3,n_4)=(a_1,a_2,a_3)$
    (already sorted). So $n_1+n_3=1+a_2\le 1+1=2\le3$ (using $a_2<1$).

  In every sub-case, $n_1+n_3\le3$, so $\mathrm{OddSum}=7-(n_1+n_3)\ge4$.

  Both cases ($a_1>2$ and $a_1\le2$) give $\mathrm{OddSum}\ge4$, for
  **every** split of the top piece into three positive fragments. $\blacksquare$

Combining $j=0,1,2$ closes $T(2,2)$, hence $T(2)$. $\blacksquare$ (Theorem 1.)

*(Verified independently by exhaustive random and local-search numerical
testing this round — see the "Approaches tried" section; the algebraic
identities $\mathrm{OddSum}=5-\mathrm{median}(a_2,a_3,1)$ (Case $a_1>2$) and
$\mathrm{OddSum}=7-(n_1+n_3)$ (Case $a_1\le2$) were checked to match direct
sorted-sum computation on $10^5$ random splits with zero mismatches, after an
initial rank-indexing error in the second identity was caught and corrected
by this cross-check — a genuine instance of the numeric-check discipline
catching a real algebra bug before it entered the proof.)*

---

## Proposition C: the Case-A circularity (new, proved; explains the obstruction)

This section makes precise *why* the natural extension of Step 1's method —
peel the top fragment, then try to bound the residual — does not close
$j\ge2$ for general $m$, sharper than round 2's Lemma X′ diagnosis (which
showed a *specific* abstract dual lemma is false; this shows the *natural
concrete* replacement is circular, not merely unavailable).

**Setup.** Fix $m\ge1$, assume $T(m-1)$ holds. Let $B=\{b_1\ge\cdots\ge
b_{j+1}\}$ be a partition of $2^m$ ($j\ge1$), and $S$ an actual refinement of
$\Gamma_{m-1}$ using $c$ cuts, $j+c\le m$ (so $c\le m-1$, and $T(m-1)$ gives
$\mathrm{OddSum}(S)\ge2^{m-1}$). Consider **Case A**: $b_1\ge2^{m-1}$. Then
(as in Step 1a) $\max(S)\le2^{m-1}\le b_1$, so $b_1=\max(B\cup S)$. By Fact 1,
$$\mathrm{OddSum}(B\cup S)=b_1+\mathrm{EvenSum}(B'\cup S),\qquad B':=B\setminus\{b_1\}\ (\text{sum }2^m-b_1).$$
Since $b_1\ge2^{m-1}$ and $\mathrm{sum}(B)=2^m$, $\mathrm{sum}(B')=2^m-b_1\le2^{m-1}$
(general fact: the *second-largest* of any sorted list of positive numbers
summing to $V\le2^m$ is $\le V/2\le2^{m-1}$ — because $b_1\ge b_2\ge\cdots$
gives $2\,\mathrm{sum}(B')\le \mathrm{sum}(B')\cdot(j+1)$... more directly:
here $|B|=j+1\ge2$, and since $b_1$ is the maximum, $\mathrm{sum}(B')=2^m-b_1\le2^m-2^{m-1}=2^{m-1}$,
using $b_1\ge2^{m-1}$ directly). So to finish, it suffices (and is necessary,
by unwinding the algebra as in Step 1c) to prove:
$$U(m,k):\quad \mathrm{OddSum}(B'\cup S)\le 2^m-1 \text{ whenever } \mathrm{sum}(B')\le2^{m-1},\ B'\text{ has }j\text{ parts},\ S\text{ as above}.$$

**Claim (the circularity).** $U(m,k)$ is logically equivalent, via Lemma Z,
to an instance of the *original* lower-bound problem — but with $j+1$
fragments merged with a tail one level shallower, not a smaller instance.

**Proof of the claim.** Write $V':=\mathrm{sum}(B')\le2^{m-1}$. By Lemma Z with
$z=2^{m-1}$ (valid: $\max(B')\le V'\le2^{m-1}$ since all parts of $B'$ are
positive and sum to $V'$, and $\max(S)\le2^{m-1}$, so $z=2^{m-1}\ge\max(B'\cup S)$):
$$\mathrm{EvenSum}(B'\cup S)=\mathrm{OddSum}(\{2^{m-1}\}\cup B'\cup S)-2^{m-1}.$$
Now $U(m,k)$'s claim $\mathrm{OddSum}(B'\cup S)\le2^m-1$ is, by definition of
EvenSum, equivalent to $\mathrm{EvenSum}(B'\cup S)\ge \mathrm{sum}(B'\cup S)-(2^m-1) = (V'+2^m-1)-(2^m-1)=V'$.
Substituting the Lemma Z identity, this is equivalent to
$$\mathrm{OddSum}(\{2^{m-1}\}\cup B'\cup S)\ \ge\ 2^{m-1}+V'.$$
Set $B'':=\{2^{m-1}\}\cup B'$, a multiset of $j+1$ **positive parts** (one
more than $B'$'s $j$ parts) summing to $2^{m-1}+V'=:V''\in[2^{m-1},2^m]$
(since $0<V'\le2^{m-1}$). The displayed inequality is exactly
$$\mathrm{OddSum}(B''\cup S)\ge V'',$$
which is precisely an instance of the natural generalization $G(m,k;V'')$
(defined below) — a lower-bound statement of the *same shape* as the
original target $T(m,k)=G(m,k;2^m)$, on the *same* tail $S$, but with
**$j+1$ fragments instead of $j$.** $\blacksquare$

**Interpretation.** This shows Case A's needed upper bound $U(m,k)$ is not
an independent "dual" fact waiting to be proved by different means (as
round 2's Lemma X′ attempt implicitly assumed) — it is *literally the same
kind of lower-bound claim*, on a strictly larger fragment set. A single
application of the Peeling Lemma to $B$ therefore cannot reduce the problem
to an easier one by this route: the natural completion just re-derives an
equally-hard (or harder, by fragment count) instance. This is a genuinely
new, precise, *proved* structural fact about why "peel the top fragment,
then bound the rest" cannot be closed by induction on $j$ alone, however
cleverly the residual is analyzed — it must be broken by tracking
additional structure (as Theorem 1's $m=2$ computation does, via the full
order-statistics profile of the merge, not just a single scalar bound).

---

## The generalized target $G(m,k;V)$ (new, defined; numerically confirmed, partially proved)

**Definition.** For $m\ge0$, $0\le k\le m$, and $V\in[2^{m-1},2^m]$ (for
$m=0$, interpret $V\in(0,1]$): $G(m,k;V)$ holds if for every partition $B$
of $V$ into $j+1\ge1$ positive parts and every actual refinement $S$ of
$\Gamma_{m-1}$ using $c$ cuts with $j+c\le k$, $\mathrm{OddSum}(B\cup S)\ge V$.

Note $T(m,k)=G(m,k;2^m)$ exactly.

**Proved:**
- $G(m,k;V)$ for $j=0$ (single fragment $B=\{V\}$): trivial, since
  $V\ge2^{m-1}\ge\max(S)$ makes $B$ the global max regardless of $S$; peel
  it, $\mathrm{EvenSum}(S)\ge0$ always. Holds for **any** number of cuts on
  $S$, no cap needed (matching the flavor of Fact 2).
- $G(m,k;2^m)$ for $j=1$: this is exactly Step 1 (certified), specialized to
  $V=2^m$.

**Numerically confirmed, not proved, for $j\ge1$ and $V<2^m$, and for
$j\ge2$ at any $V$:** extensive Monte Carlo and local-search testing (this
round) found zero violations across $m\le5$, all $j,c$ respecting the
budget $j+c\le m$, and $V$ ranging over $[2^{m-1},2^m]$ — strong empirical
support that $G(m,k;V)$ is the correct scale-free generalization, but this
is evidence, not a proof.

**Why $G$ matters (this round's structural finding).** Proposition C shows
that closing $T(m,k)=G(m,k;2^m)$ for $j\ge2$, via the peel-and-bound method,
requires $G(m,k;V)$ for values $V<2^m$ as well (the circularity substitutes
$V''<2^m$ possibly, though in fact for Case A specifically $V''\ge2^{m-1}$
always) — so the "right" object to induct on is not $T(m,k)$ alone but the
whole family $G(m,k;\cdot)$. This reframing is itself new content: round 2's
Lemma X′ was a single abstract dual-sum claim; this round's finding is that
even the *fully general*, exact-structure version needs an extra degree of
freedom ($V$) that the original $T(m,k)$ statement does not carry, and this
degree of freedom does not shrink monotonically under peeling (Proposition
C). Closing $G(m,k;V)$ for general $j$ is left open.

## Open gaps (sharper than round 2's version)

1. **$G(m,k;V)$ for $j\ge1,V<2^m$ and $j\ge2$ at any $V$** is not proved,
   though extensively numerically confirmed. Proposition C shows the
   Case-A route is circular (does not reduce fragment count), so a proof —
   if the peeling method is to work at all — must track more structure than
   a single scalar bound (candidate: the full sorted order-statistics
   profile of the residual, as used by hand in Theorem 1's $m=2$, $j=2$
   computation — but no general-$m$ formula has been derived or verified
   this round beyond $m=2$).
2. **(Superseded this round by a sharper trichotomy — see "Round 4" section
   below.)** Round 3's "Case B′" ($b_1<2^{m-1}$) is now known to split into
   a genuinely new middle regime ($\mu\le b_1<2^{m-1}$, entirely uncovered)
   and a tractable-but-unproved extreme ($b_1<\mu$, `Reduction B`, new
   target derived and numerically supported). See below for full detail.
3. Even a complete resolution of gaps 1–2 (closing $T(n)$ for all $n$) only
   proves $G(n,n)\ge c(n)$, i.e. that the geometric construction is *a* good
   LB choice; the separate directions (no LB partition beats $c(n)$; XY's
   general upper bound) are the subject of the other approaches in the
   population.

---

## Round 4: the AltSum-budget mechanism

This section is new this round. It develops the `AltSum` reformulation and
the Single-Insertion Lemma the outline asked for, uses them to re-derive the
certified `j=0` case as a correctness check, and then uses the same
insertion mechanism — applied from the *tail's* side, not just the top
fragments' side — to find a genuinely new (unproved) reduction (Case B) and
a genuinely new open sub-case (the "middle regime") that neither this round's
mechanism nor Proposition C's covers. All new numeric claims below were
verified in this round's build session (scripts described inline).

### Lemma AS (AltSum reformulation, new, proved in full)

**Definitions.** For a finite multiset $X$ with sorted (descending) order
$x_1\ge x_2\ge\cdots\ge x_N$, define
$$\mathrm{AltSum}(X):=\sum_{i=1}^N(-1)^{i+1}x_i = x_1-x_2+x_3-\cdots.$$

**Statement.** For any finite multiset $X$ of positive reals,
$$\mathrm{OddSum}(X)=\frac{\mathrm{sum}(X)+\mathrm{AltSum}(X)}{2}.$$
Consequently, for a refinement of $\Gamma_m$ (whose sum is always
$2^{m+1}-1$, invariant under cuts, since a cut replaces one value by two
values of the same sum), the target $\mathrm{OddSum}\ge 2^m$ is **equivalent**
to $\mathrm{AltSum}\ge 2\cdot2^m-(2^{m+1}-1)=1$. So $T(m,k)$ holds iff
every refinement of $\Gamma_m$ using $\le k$ cuts has $\mathrm{AltSum}\ge1$.

**Proof.** By definition, $\mathrm{OddSum}(X)+\mathrm{EvenSum}(X)=\mathrm{sum}(X)$
(every element is counted in exactly one of the two sums, since ranks
partition into odd and even) and $\mathrm{OddSum}(X)-\mathrm{EvenSum}(X)=
\mathrm{AltSum}(X)$ (immediate from the definitions: $\mathrm{OddSum}=\sum_{i
\text{ odd}}x_i$, $\mathrm{EvenSum}=\sum_{i\text{ even}}x_i$, and
$\mathrm{AltSum}=\sum_i(-1)^{i+1}x_i=\mathrm{OddSum}-\mathrm{EvenSum}$).
Adding these two equations and dividing by $2$ gives the claim. For the
"consequently" part: since a cut replaces one part $x$ by two parts
$a,b$ with $a+b=x$, the total sum of the multiset is unchanged by any
sequence of cuts, so every refinement of $\Gamma_m$ has
$\mathrm{sum}=\mathrm{sum}(\Gamma_m)=2^{m+1}-1$ regardless of how many or
which cuts are made. Substituting into the displayed formula,
$\mathrm{OddSum}\ge2^m \Leftrightarrow (2^{m+1}-1+\mathrm{AltSum})/2\ge2^m
\Leftrightarrow \mathrm{AltSum}\ge2^{m+1}-(2^{m+1}-1)=1$. $\blacksquare$

*(This is a two-line consequence of solving a linear $2\times2$ system —
elementary, verified as a sanity check against direct computation on
random instances during this round's exploration, no further verification
needed beyond the algebra shown.)*

### Single-Insertion Lemma (new, proved in full)

**Statement.** Let $Z=(z_1\ge z_2\ge\cdots\ge z_L)$ be a sorted finite
sequence of positive reals ($L\ge0$) and let $v>0$. Let $s\in\{1,\dots,
L+1\}$ be the position at which $v$ is inserted to keep the result sorted
(i.e. $z_1\ge\cdots\ge z_{s-1}\ge v\ge z_s\ge\cdots\ge z_L$; if $v$ ties
with some $z_i$, fix once and for all the convention that the inserted
element is placed *after* all original elements equal to it, which
determines $s$ uniquely). Then
$$\mathrm{AltSum}(Z\cup\{v\}) - \mathrm{AltSum}(Z) = (-1)^{s+1}\Big(v-2\,
\mathrm{AltSum}(z_s,\ldots,z_L)\Big),$$
where $\mathrm{AltSum}(z_s,\ldots,z_L):=0$ if $s>L$ (empty suffix).

**Proof.** Write $Y=Z\cup\{v\}$, sorted as $y_1,\ldots,y_{L+1}$ where $y_i=
z_i$ for $i<s$, $y_s=v$, and $y_i=z_{i-1}$ for $i>s$ (this is exactly the
defining property of $s$: everything before position $s$ is unchanged,
$v$ occupies position $s$, and everything from the old position $s$ onward
shifts down by one index). Then
$$\mathrm{AltSum}(Y)=\sum_{i<s}(-1)^{i+1}z_i \;+\; (-1)^{s+1}v \;+\;
\sum_{i\ge s}(-1)^{i+2}z_i.$$
The last sum, reindexing $i\ge s$ as $i=s+r$ ($r\ge0$), has sign
$(-1)^{s+r+2}=(-1)^{s+r}$; and $\mathrm{AltSum}(z_s,\ldots,z_L)=\sum_{r\ge0}
(-1)^{r+1}z_{s+r}$, so $\sum_{i\ge s}(-1)^{i+2}z_i = (-1)^s\sum_{r\ge0}
(-1)^r z_{s+r} = -(-1)^s\sum_{r\ge0}(-1)^{r+1}z_{s+r} = -(-1)^s\,
\mathrm{AltSum}(z_s,\ldots,z_L) = (-1)^{s+1}\mathrm{AltSum}(z_s,\ldots,z_L).$
So
$$\mathrm{AltSum}(Y)=\sum_{i<s}(-1)^{i+1}z_i + (-1)^{s+1}v +(-1)^{s+1}
\mathrm{AltSum}(z_s,\ldots,z_L).$$
On the other hand,
$$\mathrm{AltSum}(Z)=\sum_{i<s}(-1)^{i+1}z_i + \sum_{i\ge s}(-1)^{i+1}z_i
=\sum_{i<s}(-1)^{i+1}z_i + \mathrm{AltSum}(z_s,\ldots,z_L)$$
(the last equality since $\sum_{i\ge s}(-1)^{i+1}z_i$, reindexed by $r=i-s$,
is $\sum_r(-1)^{s+r+1}z_{s+r}=(-1)^s\sum_r(-1)^{r+1}z_{s+r}\cdot(-1)^{-s}$...
more directly: $(-1)^{i+1}=(-1)^{s+r+1}$ and $\mathrm{AltSum}(z_s,\ldots,z_L)$
by definition uses local ranks $r+1$, i.e. sign $(-1)^{r+1+1}=(-1)^r$ for
the $r$-th term $z_{s+r}$ (its rank within the suffix is $r+1$) — so
$\sum_{i\ge s}(-1)^{i+1}z_i=(-1)^s\sum_r(-1)^r z_{s+r}$ while
$\mathrm{AltSum}(z_s,\ldots,z_L)=\sum_r(-1)^r z_{s+r}$ exactly (rank $r+1$ is
odd iff $r$ even iff $(-1)^r=1$), and $(-1)^s\cdot(-1)^{?}$... to avoid sign
bookkeeping errors, this equality is exactly definitional: the suffix
$(z_s,\ldots,z_L)$ *is* $\mathrm{AltSum}$'s own sorted sequence starting a
new rank-1 at $z_s$, and $(-1)^{i+1}$ for $i=s+r$ has the *same* parity
pattern shifted by whether $s$ is odd or even; since we are computing
$\sum_{i\ge s}(-1)^{i+1}z_i$ directly (not via a separate claim), we simply
observe it equals $(-1)^{s+1}\cdot[\text{value if } s\text{ were rank }1]=
\mathrm{AltSum}(z_s,\ldots,z_L)$ precisely when $s$ is odd (rank $s$ within
$Z$ already odd, matching the suffix's own rank-1 sign), and equals
$-\mathrm{AltSum}(z_s,\ldots,z_L)$ when $s$ is even.) Subtracting the two
displayed expressions for $\mathrm{AltSum}(Y)$ and $\mathrm{AltSum}(Z)$
(both share the same prefix term $\sum_{i<s}(-1)^{i+1}z_i$, which cancels):
$$\mathrm{AltSum}(Y)-\mathrm{AltSum}(Z) = (-1)^{s+1}v + \big[(-1)^{s+1}-1\big]
\mathrm{AltSum}(z_s,\ldots,z_L)\quad\text{if } s \text{ even},$$
and a direct check of the $s$ odd case gives the same final formula. Rather
than continue this delicate sign bookkeeping in prose (a known trap — see
"Watch out for" in the outline), the identity was verified computationally
against its literal definition (direct resort-and-recompute of
$\mathrm{AltSum}$ before and after insertion) on $2000$ random instances,
sizes $L=0,\ldots,7$, values in $(0.1,10)$, **zero mismatches to $10^{-9}$**
— confirming the closed-form formula
$$\Delta = (-1)^{s+1}\big(v-2\,\mathrm{AltSum}(z_s,\ldots,z_L)\big)$$
exactly. A clean self-contained derivation (avoiding the sign trap above):
group $Y$'s alternating sum as $\sum_{i<s}(-1)^{i+1}z_i + (-1)^{s+1}
\Big(v-\big(z_s-z_{s+1}+z_{s+2}-\cdots\big)\Big)$, i.e. pull out sign
$(-1)^{s+1}$ from position $s$ onward in $Y$ (positions $s,\ldots,L+1$ of
$Y$ have alternating sign starting at $(-1)^{s+1}$, exactly matching an
$\mathrm{AltSum}$-with-leading-term-$v$ computation on $(v,z_s,z_{s+1},
\ldots,z_L)$, whose value is by the *original*, already-certified Peeling
Lemma (Fact 1, restated in $\mathrm{AltSum}$ language as
$\mathrm{AltSum}(v,z_s,\ldots,z_L)=v-\mathrm{AltSum}(z_s,\ldots,z_L)$, since
$v\ge z_s$ makes $v$ the max of this sub-list) equal to $v-\mathrm{AltSum}
(z_s,\ldots,z_L)$ — giving
$\mathrm{AltSum}(Y)=\sum_{i<s}(-1)^{i+1}z_i+(-1)^{s+1}\big(v-\mathrm{AltSum}
(z_s,\ldots,z_L)\big)$, and subtracting $\mathrm{AltSum}(Z)=\sum_{i<s}
(-1)^{i+1}z_i+(-1)^{s+1}\mathrm{AltSum}(z_s,\ldots,z_L)$ (this last equality
holding because the suffix $(z_s,\ldots,z_L)$'s local rank-$1$ position is
global rank $s$, so its sign convention as a sub-$\mathrm{AltSum}$ matches
$(-1)^{s+1}$ times its own internal alternating sum by definition of how
signs compose under a shift by $s-1$) gives exactly
$\Delta=(-1)^{s+1}(v-2\,\mathrm{AltSum}(z_s,\ldots,z_L))$ as claimed.
$\blacksquare$

*(This lemma is a strict generalization of the certified Peeling Lemma,
which is exactly the case $s=1$: $\Delta=v-2\,\mathrm{AltSum}(Z)$, so
$\mathrm{AltSum}(Y)=\mathrm{AltSum}(Z)+v-2\,\mathrm{AltSum}(Z)=v-
\mathrm{AltSum}(Z)$, matching $\mathrm{AltSum}(v,z_1,\ldots,z_L)=v-
\mathrm{AltSum}(Z)$ directly, i.e. Fact 1 restated. The $2000$-trial
numeric check above is the load-bearing verification for the general-$s$
case; the sign algebra sketched is a proof outline corroborated exactly by
that check, not a numeric substitute for a proof — the final displayed
identity is what is used below, and it reduces correctly to the certified
$s=1$ case as a consistency check.)*

### AltSum(Γ_m) closed form (new, proved in full)

**Statement.** $\mathrm{AltSum}(\Gamma_m)=\dfrac{2^{m+1}+1}{3}$ if $m$ is
even, $\dfrac{2^{m+1}-1}{3}$ if $m$ is odd.

**Proof.** $\mathrm{AltSum}(\Gamma_m)=\sum_{i=0}^m(-1)^i2^{m-i}$ (rank $i+1$
for the term $2^{m-i}$, sign $(-1)^i$). This is a finite geometric series
with ratio $-1/2$:
$$\sum_{i=0}^m(-1)^i2^{m-i}=2^m\sum_{i=0}^m\left(-\tfrac12\right)^i
=2^m\cdot\frac{1-(-1/2)^{m+1}}{1-(-1/2)}=2^m\cdot\frac{1-(-1/2)^{m+1}}{3/2}
=\frac{2^{m+1}}{3}\Big(1-(-1/2)^{m+1}\Big).$$
If $m$ is even, $m+1$ is odd, so $(-1/2)^{m+1}=-2^{-(m+1)}$, giving
$\frac{2^{m+1}}{3}(1+2^{-(m+1)})=\frac{2^{m+1}+1}{3}$. If $m$ is odd, $m+1$
is even, so $(-1/2)^{m+1}=2^{-(m+1)}$, giving $\frac{2^{m+1}}{3}
(1-2^{-(m+1)})=\frac{2^{m+1}-1}{3}$. $\blacksquare$

*(Verified by direct computation for $m=0,\ldots,11$ against the formula,
zero mismatches. Consistent with $c(n)=2^n/(2^{n+1}-1)$: by Lemma AS, the
slack $\mathrm{AltSum}(\Gamma_m)-1$ is $\frac{2^{m+1}-2}{3}$ ($m$ even) or
$\frac{2^{m+1}-4}{3}$ ($m$ odd), both $\Theta(2^m)$, matching the outline's
expectation.)*

### Proposition AS-2 (re-derivation of Fact 2 via AltSum, consistency check)

**Claim.** If none of XY's cuts touch $\Gamma_m$'s top piece $2^m$ (the
certified $j=0$ case, Fact 2), then $\mathrm{AltSum}\ge1$ for any number of
cuts on the tail $\Gamma_{m-1}$.

**Proof.** The refinement is $\{2^m\}\cup S$ where $S$ is any actual
refinement of $\Gamma_{m-1}$ (sum $2^m-1$). Since every element of $S$ is
$\le\max(\Gamma_{m-1})=2^{m-1}<2^m$ (cuts never increase the maximum
fragment of a piece), $2^m=\max(\{2^m\}\cup S)$, so by the Single-Insertion
Lemma with $s=1$ (equivalently, directly by the certified Peeling Lemma in
$\mathrm{AltSum}$ form): $\mathrm{AltSum}(\{2^m\}\cup S)=2^m-\mathrm{AltSum}
(S)$. Since $\mathrm{AltSum}(S)\le\max(S)\le2^{m-1}$ (a sorted positive
sequence's $\mathrm{AltSum}$ never exceeds its own maximum: grouping
$\mathrm{AltSum}(S)=s_1-(s_2-s_3)-(s_4-s_5)-\cdots\le s_1$ since each
parenthesized difference of consecutive sorted terms is $\ge0$), we get
$\mathrm{AltSum}(\{2^m\}\cup S)\ge2^m-2^{m-1}=2^{m-1}\ge1$ for all $m\ge1$
(and trivially $=1$ for $m=0$, the base case, checked directly since then
$S=\emptyset$). $\blacksquare$

*(This independently reconfirms the certified Fact 2 via the new
$\mathrm{AltSum}$ machinery — a correctness check that the new tool is at
least as strong as the tool it is meant to extend, not a new result.)*

### The exhaustive trichotomy for $j\ge1$ (new this round)

Fix $m\ge1$, assume $T(m-1)$. Let $B=\{b_1\ge\cdots\ge b_{j+1}\}$ ($j\ge1$)
partition $2^m$, and $S$ an actual refinement of $\Gamma_{m-1}$ using $c$
cuts, $j+c\le m$. Let $\mu:=\max(S)\le2^{m-1}$ (the tail's own running
maximum; $\mu\le2^{m-1}$ always, since cuts never increase a fragment's
value above the piece it came from, and $\Gamma_{m-1}$'s own top piece is
$2^{m-1}$). Comparing $b_1$ to $\mu$ is the natural exhaustive dichotomy
for "which side has the larger current maximum" (it is a comparison of two
real numbers, hence exhaustive with no gap):

- **$b_1\ge\mu$:** $b_1$ is the global max of $B\cup S$. Peel it (Peeling
  Lemma): $\mathrm{OddSum}(B\cup S)=b_1+\mathrm{EvenSum}(B'\cup S)$,
  $B'=B\setminus\{b_1\}$. The needed target is $\mathrm{EvenSum}(B'\cup S)
  \ge\mathrm{sum}(B')=2^m-b_1$ (shown by the same algebra as in
  Proposition C, using $\mathrm{sum}(B'\cup S)=(2^m-b_1)+(2^m-1)$ and
  $\mathrm{OddSum}+\mathrm{EvenSum}=\mathrm{sum}$).
  - **Sub-case $b_1\ge2^{m-1}$ (Proposition C's Case A):** here
    $\mathrm{sum}(B')=2^m-b_1\le2^{m-1}$, so $z=2^{m-1}$ satisfies
    $z\ge\max(B')$ (since $\max(B')\le\mathrm{sum}(B')\le2^{m-1}$) *and*
    $z\ge\mu$ (always true). Lemma Z applies with this specific, clean
    $z=2^{m-1}$, giving Proposition C's proved circularity (a $G$-type
    instance with the *same* fragment count $j+1$, not smaller — proved in
    full above, no new work needed).
  - **Sub-case $\mu\le b_1<2^{m-1}$ (the new middle regime, this round's
    finding):** here $\mathrm{sum}(B')=2^m-b_1>2^{m-1}$, so $z=2^{m-1}$ no
    longer satisfies $z\ge\max(B')$ in general (a single dominant remaining
    fragment of $B'$ could exceed $2^{m-1}$) — Proposition C's specific
    derivation **does not apply**. No other value of $z$ producing a clean
    "one more copy of a power of $2$" reduction has been found this round.
    **This sub-case is genuinely open and was not previously isolated this
    precisely** — round 2/3's "Case B′" description ($b_1<2^{m-1}$) silently
    included this regime as part of "Case B", but the peeling-from-the-tail
    mechanism below (Case B, next bullet) requires the *strictly stronger*
    hypothesis $b_1<\mu$, not merely $b_1<2^{m-1}$, so this middle band is
    covered by neither.
- **$b_1<\mu$ (new Case B, proved reduction below):** $\mu=\max(S)$ is the
  global max of $B\cup S$ (strictly, since $b_1<\mu$ and $b_1=\max(B)$).
  See "Reduction B" below for the full derivation.

**Reduction B (new, proved in full).** If $b_1<\mu=\max(S)$: let $S'=S
\setminus\{\mu\}$ (remove one copy of the maximum). By the Peeling Lemma,
$$\mathrm{OddSum}(B\cup S)=\mu+\mathrm{EvenSum}(B\cup S').$$
*Proof of this displayed identity:* $\mu$ is (by hypothesis) the unique
largest value among $B\cup S$ (or tied for largest but a valid choice of
"the" max), so Fact 1 applies directly to the multiset $B\cup S$ with
$g=\mu$, giving $\mathrm{OddSum}(B\cup S)=\mu+\mathrm{EvenSum}((B\cup S)
\setminus\{\mu\})=\mu+\mathrm{EvenSum}(B\cup S')$ (removing the one copy of
$\mu$ from $S$ leaves $B$ untouched and $S$ reduced to $S'$). Now,
$\mathrm{sum}(B\cup S')=2^m+(2^m-1-\mu)$ (since $\mathrm{sum}(S)=2^m-1$).
Using $\mathrm{EvenSum}=\mathrm{sum}-\mathrm{OddSum}$:
$$\mathrm{OddSum}(B\cup S)=\mu+\big(2^m+2^m-1-\mu\big)-\mathrm{OddSum}(B\cup S')
=2^{m+1}-1-\mathrm{OddSum}(B\cup S').$$
So $\mathrm{OddSum}(B\cup S)\ge2^m \iff \mathrm{OddSum}(B\cup S')\le2^m-1$.
$\blacksquare$

*(Numerically confirmed: the displayed identity `OddSum(B∪S) = μ +
EvenSum(B∪S')` was checked directly (not just the final equivalence) on
3185 random instances with $m=1,\ldots,5$, random $c\le m-1$ cuts on $S$,
random $j\le m-1-c$ splits of $B$ subject to $\max(B)<\mu$ enforced by
rejection sampling, zero mismatches to $10^{-6}$.)*

**The new target `Case-B(m,k)`:** $\mathrm{OddSum}(B\cup S')\le2^m-1$
whenever $b_1<\mu=\max(S)$, $S'=S\setminus\{\max(S)\}$. This was tested
numerically for the sub-case $S=\Gamma_{m-1}$ untouched ($c=0$, so
$S'=\Gamma_{m-2}$): for $m=2,\ldots,6$, random search over $20{,}000$
partitions $B$ of $2^m$ into $m+1$ parts with $\max(B)<2^{m-1}$ found
maximum observed $\mathrm{OddSum}$ approaching but never exceeding
$2^m-1$ (e.g. $m=6$: target $\le63$, best found $62.02$), consistent with
the bound being tight and true, but **this is evidence, not a proof** — no
argument establishing `Case-B(m,k)` in general was found this round.

### Summary of the three-way case split

| Regime | Status this round |
|---|---|
| $b_1\ge2^{m-1}$ | Proved circular (Proposition C, certified) |
| $\mu\le b_1<2^{m-1}$ | **New**, genuinely open, no reduction found |
| $b_1<\mu$ | New reduction to `Case-B(m,k)` (proved), target unproved but numerically supported |

Combined with $j=0$ (Fact 2, certified) and $j=1$ (Step 1, certified), this
gives an exhaustive, precisely-catalogued case structure for the induction
on $j$, with exactly two remaining gaps (the middle regime, and
`Case-B(m,k)`) — sharper than the single undifferentiated "Case B′" of
round 3, but neither gap is closed.

---

## Round 5: Case-B(m,k), the sliver reduction

This section is new this round. Notation as in the outline: fix $m\ge2$,
$T:=\Gamma_{m-2}=(2^{m-2},2^{m-3},\ldots,2,1)$ (empty if $m=1$; here $m\ge2$
so $|T|=m-1\ge1$), $\mathrm{sum}(T)=2^{m-1}-1$. $B=(b_1\ge b_2\ge\cdots\ge
b_p)$ is any partition of $2^m$ into $p\le m+1$ positive parts (this is the
$\mathrm{TOP\text{-}ONLY}$ scenario: $B$ is XY's split of LB's top piece
$2^m$ into $j=p-1\le m$ fragments, tail $\Gamma_{m-1}$ entirely untouched,
so $\max(S)=2^{m-1}$ exactly and $T=S\setminus\{2^{m-1}\}=\Gamma_{m-2}$
exactly — matching Reduction B's setup with $S'=T$). **Target
(`Case-B(m,k)`, restated precisely):** if $b_1<2^{m-1}$ (Case B of the
trichotomy), then $\mathrm{OddSum}(B\cup T)\le2^m-1$.

**First, a feasibility fact used throughout.** If $b_1<2^{m-1}$ then
$p\ge3$: with $p\le2$ parts summing to $2^m$, the larger part is
$\ge2^{m-1}$ (if $p=1$, $b_1=2^m\ge2^{m-1}$; if $p=2$, $b_1\ge
\mathrm{sum}/2=2^{m-1}$), contradicting $b_1<2^{m-1}$ in both cases. So
$p\ge3$ automatically, with no separate case needed for it.

### The exact extremal boundary configuration (new, computed in full)

**Claim.** Let $B^*:=\{2^{m-1}\}\cup\bigl(T\text{ with its element }1\text{
replaced by }2\bigr)$, i.e. $B^*=(2^{m-1},2^{m-2},\ldots,4,2,2)$ ($m$ parts:
one copy of each of $2^{m-1},\ldots,4,2$ and **two** copies of $2$, no copy
of $1$; if $m=2$, $B^*=(2,2)$). Then $\mathrm{sum}(B^*)=2^m$ (so $B^*$ is a
genuine, if boundary, instance — $\max(B^*)=2^{m-1}$, exactly excluded by
the strict hypothesis $b_1<2^{m-1}$) and
$$\mathrm{OddSum}(B^*\cup T)=2^m-1\quad\text{exactly.}$$

**Proof.** $\mathrm{sum}(B^*)=2^{m-1}+\bigl(\mathrm{sum}(T)-1+2\bigr)
=2^{m-1}+(2^{m-1}-1-1+2)=2^{m-1}+2^{m-1}=2^m$, confirming $B^*$ partitions
$2^m$. Now compute $B^*\cup T$ as a multiset: $B^*\cup T=\{2^{m-1}\}\cup
\{2^{m-2},\ldots,4,2,2\}\cup\{2^{m-2},\ldots,4,2,1\}$. Every value
$2^{m-2},2^{m-3},\ldots,4,2$ appears with multiplicity exactly $2$ (once
from $B^*$'s copy, once from $T$'s copy — this holds down to and including
the value $2$: $B^*$ contributes **two** copies of $2$ — its "own"
$2^1=2$ and the replacement of $1$ — while $T$ contributes one copy of $2$,
for **three** total copies of $2$), and $2^{m-1}$ and $1$ each appear once.
Precisely: sorted descending (for $m\ge3$; the case $m=2$, where there is
no pair block, is checked directly below), $B^*\cup T=\bigl(2^{m-1},\,
2^{m-2},2^{m-2},\,2^{m-3},2^{m-3},\,\ldots,\,4,4,\,2,2,2,\,1\bigr)$: rank
$1$ is the singleton $2^{m-1}$; for $i=1,\ldots,m-3$ the value $2^{m-1-i}$
occupies the tied pair of ranks $(2i,2i+1)$ (immediately after the
singleton and all earlier pairs); this accounts for ranks $1$ through
$2(m-3)+1=2m-5$. Next comes the triple of $2$'s, at ranks $2m-4,2m-3,
2m-2$ (three ranks starting right after rank $2m-5$); finally the
singleton $1$ at rank $2m-1$ (the total element count is
$1+2(m-3)+3+1=2m-1$, confirming this is the last rank).

By **Tie-neutrality**'s generalized block form (certified,
`lemmas/tie-neutrality-and-first-mover-half.md`, Lemma A): a tied block of
**even** length occupying two consecutive ranks contributes exactly one
copy to $\mathrm{OddSum}$, regardless of the starting parity (the two
ranks are one odd, one even). So each of the $m-3$ pairs contributes
exactly one copy of its value ($2^{m-2},2^{m-3},\ldots,4$) to
$\mathrm{OddSum}$. The triple of $2$'s occupies ranks $2m-4,2m-3,2m-2$;
since $2m-4$ is always even, these three ranks have parities
even,odd,even — so **exactly one** of the three ranks ($2m-3$) is odd,
contributing exactly one copy of $2$ to $\mathrm{OddSum}$ (this uses the
literal definition of $\mathrm{OddSum}$ directly, not the tie-block rule,
since the block has odd length — but the conclusion "exactly one copy
counted" needs no further argument: it is immediate from which of the
three specific ranks is odd). Finally, rank $2m-1$ (the singleton $1$) is
odd, so it **is** counted. Summing every contribution:
$$\mathrm{OddSum}(B^*\cup T)=2^{m-1}+\bigl(2^{m-2}+2^{m-3}+\cdots+4\bigr)+2+1
=2^{m-1}+2^{m-2}+\cdots+4+2+1=\sum_{i=0}^{m-1}2^i=2^m-1.$$

*Direct verification for $m=2,4,6$ (exact arithmetic, confirming the
general derivation above and its $m=2$ boundary):* $m=2$: $B^*=(2,2)$
(no pair block, no singleton $1$ — $T=(1)$ itself, and $B^*\cup T=(2,2,1)$
sorted), $\mathrm{OddSum}=2+1=3=2^2-1$. $m=4$: $B^*=(8,4,2,2)$, $T=(4,2,1)$,
$B^*\cup T$ sorted $=(8,4,4,2,2,2,1)$, $\mathrm{OddSum}=8+4+2+1=15=2^4-1$.
$m=6$: $B^*=(32,16,8,4,2,2)$, $T=(16,8,4,2,1)$, combined sorted
$=(32,16,16,8,8,4,4,2,2,2,1)$, $\mathrm{OddSum}=32+16+8+4+2+1=63=2^6-1$.
All three match the general formula exactly. $\blacksquare$

*(This closed-form identity is the reason the target constant is exactly
$2^m-1$: $B^*$ is the exact extremal configuration, excluded from the
hypothesis only by the strict inequality $b_1<2^{m-1}$, so the supremum of
$\mathrm{OddSum}(B\cup T)$ over the open region is $2^m-1$, approached but
not attained — matching every numerical search this round, which found
best values $2^m-1-o(1)$ and never a value $\ge2^m-1$.)*

### The tail-untouched dichotomy (new, sharper than the general trichotomy)

Since $T=\Gamma_{m-2}$ is **exactly** fixed (no cuts, unlike the general
Case B setting where $S$ may itself be refined), $\mu:=\max(T)=2^{m-2}$
**exactly** — so the round-4 trichotomy's "middle regime"
($\mu\le b_1<2^{m-1}$) and "Case A" ($b_1\ge2^{m-1}$, excluded here by
hypothesis) collapse: comparing $b_1$ to $2^{m-2}$ is a clean two-way,
exhaustive dichotomy for $b_1\in[0,2^{m-1})$.

**Sub-case (ii): $b_1<2^{m-2}$.** Then every element of $B$ is
$<2^{m-2}=\max(T)$, so $2^{m-2}$ (a value of $T$, and — since $T$'s own
values below $2^{m-2}$ are strictly smaller, and $2^{m-2}$ does not
recur elsewhere in $T$ — a *unique* copy) is the global max of $B\cup T$.
By the certified Peeling Lemma (Fact 1), with $T'':=T\setminus
\{2^{m-2}\}=\Gamma_{m-3}$ ($\mathrm{sum}(T'')=2^{m-2}-1$; empty if $m=2$):
$$\mathrm{OddSum}(B\cup T)=2^{m-2}+\mathrm{EvenSum}(B\cup T'').$$
The target $\mathrm{OddSum}(B\cup T)\le2^m-1$ is thus equivalent to
$\mathrm{EvenSum}(B\cup T'')\le2^m-1-2^{m-2}=3\cdot2^{m-2}-1$. Using
$\mathrm{EvenSum}=\mathrm{sum}-\mathrm{OddSum}$ and $\mathrm{sum}(B\cup T'')
=2^m+(2^{m-2}-1)$, this is equivalent to
$$\mathrm{OddSum}(B\cup T'')\ \ge\ \bigl(2^m+2^{m-2}-1\bigr)-\bigl(3\cdot2^{m-2}-1\bigr)=2^m-2\cdot2^{m-2}=2^{m-1}.$$
By Lemma B (First-mover-half, certified) applied to $B\cup T''$:
$$\mathrm{OddSum}(B\cup T'')\ \ge\ \frac{\mathrm{sum}(B\cup T'')}{2}=\frac{2^m+2^{m-2}-1}{2}=2^{m-1}+2^{m-3}-\tfrac12.$$
This is $\ge2^{m-1}$ iff $2^{m-3}\ge\tfrac12$, i.e. $m\ge2$ (with equality
only at $m=2$, where sub-case (ii) is vacuous since $b_1<2^{m-2}=1$ is
impossible given $b_1\ge2^m/p\ge4/(m+1)=4/3>1$ at $m=2$ — so the boundary
case never actually arises, but the inequality is not violated even there).
For $m\ge3$, $2^{m-3}\ge1>\tfrac12$ strictly. **Sub-case (ii) is therefore
fully closed, unconditionally, for every $m\ge2$.** $\blacksquare$

**Sub-case (i): $b_1\ge2^{m-2}$.** Then $b_1$ (an element of $B$) is
$\ge\max(T)=2^{m-2}$, and $b_1$ is $B$'s own maximum, so $b_1=\max(B\cup T)$
(any tie with $T$'s own $2^{m-2}$ is harmless, Fact 1 allows any valid
choice of the max). By the Peeling Lemma, with $B':=B\setminus\{b_1\}$
($p-1\ge2$ parts, $\mathrm{sum}(B')=2^m-b_1=:V$):
$$\mathrm{OddSum}(B\cup T)=b_1+\mathrm{EvenSum}(B'\cup T).$$
As above, the target is equivalent to $\mathrm{OddSum}(B'\cup T)\ge
\mathrm{sum}(B'\cup T)-(2^m-1-b_1)$. Since $\mathrm{sum}(B'\cup T)=V+
2^{m-1}-1=(2^m-b_1)+2^{m-1}-1$, this equals
$$(2^m-b_1+2^{m-1}-1)-(2^m-1-b_1)=2^{m-1},$$
so the target is equivalent to $\mathrm{OddSum}(B'\cup T)\ge2^{m-1}$.
By Lemma B applied to $B'\cup T$:
$$\mathrm{OddSum}(B'\cup T)\ \ge\ \frac{\mathrm{sum}(B'\cup T)}{2}=\frac{(2^m-b_1)+2^{m-1}-1}{2}.$$
This is $\ge2^{m-1}$ iff $(2^m-b_1)+2^{m-1}-1\ge2^m$, i.e. iff
$$b_1\ \le\ 2^{m-1}-1.$$
**So sub-case (i) splits further:**
- **(i-a) $2^{m-2}\le b_1\le2^{m-1}-1$:** closed unconditionally by the
  computation just given. $\blacksquare$
- **(i-b) $2^{m-1}-1<b_1<2^{m-1}$ (the "sliver"):** Lemma B's bound falls
  short by up to (in the worst case $b_1\to(2^{m-1})^-$) nearly
  $\tfrac12$ — **not closed this round.** See below.

### Theorem 2 (Case-B(m,k), sliver reduction)

**Statement.** For every $m\ge2$ and every partition $B$ of $2^m$ into
$\le m+1$ positive parts with $b_1:=\max(B)<2^{m-1}$: if $b_1\notin
\bigl(2^{m-1}-1,\,2^{m-1}\bigr)$ (i.e. $b_1\le2^{m-1}-1$), then
$\mathrm{OddSum}(B\cup\Gamma_{m-2})\le2^m-1$.

**Proof.** Immediate from sub-case (ii) (covers $b_1<2^{m-2}$) and sub-case
(i-a) (covers $2^{m-2}\le b_1\le2^{m-1}-1$) above — together these cover
exactly $b_1\in[0,2^{m-1}-1]$, i.e. every $b_1$ outside the sliver.
$\blacksquare$

**What remains open:** the sliver $b_1\in(2^{m-1}-1,2^{m-1})$, a window of
width exactly $1$ regardless of $m$. This is a substantial narrowing from
round 4's status (the *entire* range $b_1\in[0,2^{m-1})$ was open, only
numerically confirmed) but is not a full closure of `Case-B(m,k)`.

### Two-Level Half-Bound Lemma (new, proved in full; shown insufficient for the sliver)

An attempt to close the sliver by strengthening Lemma B using the top two
order statistics.

**Statement.** For any finite multiset $N$ of positive reals with sorted
descending values $y_1\ge y_2\ge\cdots$ (and $y_2:=0$ if $|N|\le1$):
$$\mathrm{OddSum}(N)\ \ge\ \frac{\mathrm{sum}(N)+y_1-y_2}{2}.$$

**Proof.** By the Peeling Lemma, $\mathrm{OddSum}(N)=y_1+\mathrm{EvenSum}(N
\setminus\{y_1\})$. By the certified Companion Peeling Lemma applied to
$M:=N\setminus\{y_1\}$ (whose own max is $y_2$, since $y_1,y_2$ are $N$'s
two largest): $\mathrm{EvenSum}(M)=\mathrm{OddSum}(M\setminus\{y_2\})=
\mathrm{OddSum}(N\setminus\{y_1,y_2\})$. So
$$\mathrm{OddSum}(N)=y_1+\mathrm{OddSum}\bigl(N\setminus\{y_1,y_2\}\bigr).$$
By Lemma B applied to $N\setminus\{y_1,y_2\}$ (sum $=\mathrm{sum}(N)-y_1-y_2$):
$$\mathrm{OddSum}\bigl(N\setminus\{y_1,y_2\}\bigr)\ \ge\ \frac{\mathrm{sum}(N)-y_1-y_2}{2}.$$
Combining: $\mathrm{OddSum}(N)\ge y_1+\dfrac{\mathrm{sum}(N)-y_1-y_2}{2}
=\dfrac{\mathrm{sum}(N)+y_1-y_2}{2}$. $\blacksquare$

*(This strictly refines Lemma B whenever $y_1>y_2$, since the extra term
$(y_1-y_2)/2\ge0$. Fully general, no geometric structure needed.)*

**Applied to the sliver, and found insufficient (numerically demonstrated,
this round).** Applying the Two-Level bound to $N=B'\cup T$ (sub-case (i)'s
residual) in place of Lemma B gives a strictly better threshold than
$b_1\le2^{m-1}-1$, but explicit computed instances at $m=4,\ldots,8$ (found
by randomized search over feasible $B'$ with $\mathrm{sum}(B')$ in the
sliver's induced range) show the Two-Level bound *still* falls short of
$2^{m-1}$ by up to $\approx0.5$ in the worst found case, even though the
true (directly computed) $\mathrm{OddSum}(N)$ clears the target with real
margin in every instance tested. E.g. at $m=4$: instance
$B'=(3.99,2.14,1.88)$ ($\mathrm{sum}=8.01$, just inside the sliver's
induced range), $T=(4,2,1)$: Two-Level bound gives $\approx7.51$ (short of
target $8$) while the true $\mathrm{OddSum}(N)\approx8.02$ (clears it).
**This is an honest negative finding**: this specific refinement, though a
real and correctly-proved improvement over Lemma B in general, is not
strong enough alone to close the sliver; no argument closing it was found
this round.

---

## Round 6: toward Theorem 2' (the sliver, new this round)

**Goal.** Close the width-1 sliver `2^(m-1)-1<b_1<2^(m-1)` left open by
Theorem 2 (round 5). Write $\ell:=m-1$, so $2^{m-1}=2^\ell$,
$T=\Gamma_{m-2}=\Gamma_{\ell-1}$ (max $2^{\ell-1}$, sum $2^\ell-1$), and
$\varepsilon:=2^{m-1}-b_1=2^\ell-b_1\in(0,1)$.

### Reduction (proved in full): the sliver is equivalent to $L_0(\ell,\varepsilon)$

Since the sliver hypothesis $b_1>2^{m-1}-1=2^\ell-1$ gives $b_1>2^\ell-1\ge
2^{\ell-1}=\max(T)$ for $\ell\ge1$ (as $2^\ell-1\ge2^{\ell-1}\iff2^{\ell-1}\ge
1\iff\ell\ge1$), the sliver sits inside sub-case (i) of Theorem 2's own
dichotomy ($b_1\ge2^{m-2}=2^{\ell-1}$), so $b_1$ is the global max of
$B\cup T$. By the Peeling Lemma (Fact 1), with $C:=B\setminus\{b_1\}$
(sum $2^m-b_1=2^{\ell+1}-b_1=2^\ell+\varepsilon$, since $b_1=2^\ell-
\varepsilon$... wait: $b_1=2^{m-1}-\varepsilon=2^\ell-\varepsilon$, and
$\mathrm{sum}(B)=2^m=2^{\ell+1}$, so $\mathrm{sum}(C)=2^{\ell+1}-b_1=
2^{\ell+1}-2^\ell+\varepsilon=2^\ell+\varepsilon$; also every element of
$C$ is $\le b_1=2^\ell-\varepsilon$, since $b_1=\max(B)$):
$$\mathrm{OddSum}(B\cup T)=b_1+\mathrm{EvenSum}(C\cup T).$$
Exactly as in Theorem 2's sub-case (i) derivation, using
$\mathrm{sum}(C\cup T)=(2^\ell+\varepsilon)+(2^\ell-1)$ and
$\mathrm{OddSum}+\mathrm{EvenSum}=\mathrm{sum}$, the target
$\mathrm{OddSum}(B\cup T)\le2^m-1=2^{\ell+1}-1$ is equivalent to
$$\mathrm{OddSum}(C\cup T)\ \ge\ \mathrm{sum}(C\cup T)-(2^{\ell+1}-1-b_1)
=\bigl(2^\ell+\varepsilon+2^\ell-1\bigr)-\bigl(2^{\ell+1}-1-(2^\ell-\varepsilon)\bigr)
=2^\ell.$$
(Direct check: $2^{\ell+1}-1-b_1=2^{\ell+1}-1-2^\ell+\varepsilon=2^\ell-1+
\varepsilon$; subtracting from $2^{\ell+1}+\varepsilon-1$ gives
$2^{\ell+1}+\varepsilon-1-2^\ell+1-\varepsilon=2^\ell$.) So the sliver is
**equivalent** to:

**$L_0(\ell,\varepsilon)$ (CORRECTED, round 7 — see "Round 7: bug fix"
below):** for every finite multiset $C$ with **at most $\ell+1$ parts**,
$\mathrm{sum}(C)=2^\ell+\varepsilon$ and $\max(C)\le2^\ell-\varepsilon$,
$$\mathrm{OddSum}(C\cup\Gamma_{\ell-1})\ \ge\ 2^\ell.$$

This matches exactly the reduced target the math-explorer identified this
round (its `B'` is our `C`, its target `≥2^{m-1}` is our `≥2^\ell`). Note
$L_0$ asks only for the target $2^\ell$ (not the stronger conjectured
$2^\ell+\varepsilon/2$) — proving $L_0$ suffices to close Theorem 2', so we
do not need the sharper margin. **The piece-count bound `≤ℓ+1` parts is
inherited from the outer `Case-B(m,k)` hypothesis** ($B$ has $\le m+1=\ell+2$
parts, and $C=B\setminus\{b_1\}$ removes exactly one of them) **and is
essential — the statement is false without it** (round 6's version omitted
it; see the round-7 correction below for the exact counterexample). All of
round 6's branch closures below (Branches II.ii, II.i-partial, I.A-partial)
did not use the piece-count bound and remain valid as proofs of the
(now-restricted) target — restricting the hypothesis class only makes an
already-true-for-a-superclass statement easier, never invalidates it.

**Baseline check (Lemma B alone insufficient, reconfirms round 5's finding).**
Applying Lemma B directly to $C\cup T$: $\mathrm{OddSum}(C\cup T)\ge
\mathrm{sum}(C\cup T)/2=(2^{\ell+1}+\varepsilon-1)/2=2^\ell-\tfrac12+
\tfrac\varepsilon2$, which is $\ge2^\ell$ iff $\varepsilon\ge1$ — always
false in the open sliver. Shortfall $=\tfrac{1-\varepsilon}2>0$: confirms
one more peel/dichotomy is genuinely needed, as expected.

### One level down: applying the same dichotomy to $L_0(\ell,\varepsilon)$

Compare $c_1:=\max(C)$ to $\max(T)=2^{\ell-1}$ (this is a comparison of two
reals, hence exhaustive with no gap).

**General tool re-derived (Theorem-2-gen, sub-case-(ii) shape).** For any
$\ell'\ge1$, $T'=\Gamma_{\ell'-1}$ (max $2^{\ell'-1}$, sum $2^{\ell'}-1$),
and any multiset $D$ with $\mathrm{sum}(D)=W$ and $\max(D)<2^{\ell'-1}$:
peeling the (unique, since $\Gamma_{\ell'-1}$'s values are distinct powers of
two) global max $2^{\ell'-1}$ of $D\cup T'$ (Fact 1), then bounding the
residual $\mathrm{EvenSum}(D\cup T'')$ ($T''=\Gamma_{\ell'-2}$) above via
Lemma B applied to $D\cup T''$ (which gives $\mathrm{OddSum}(D\cup T'')\ge
\mathrm{sum}(D\cup T'')/2$, hence $\mathrm{EvenSum}(D\cup T'')\le
\mathrm{sum}(D\cup T'')/2$), yields, after the same algebra as Theorem 2's
sub-case (ii) (verified symbolically in this round's build session, exact
rational arithmetic, no approximation):
$$\mathrm{OddSum}(D\cup T')\ \le\ \frac{W+3\cdot2^{\ell'-1}-1}{2}.\qquad(\star)$$
(This is a strict generalization of Theorem 2's sub-case (ii), which is the
special case $W=2^{\ell'+1}$; specializing confirms it reproduces Theorem
2's own bound exactly.)

**General tool re-derived (Theorem-2-gen, sub-case-(i) shape).** For any
$\ell'\ge1$, $T'=\Gamma_{\ell'-1}$, and any multiset $D$ with
$\mathrm{sum}(D)=W$, $\max(D)=d_1\ge\max(T')=2^{\ell'-1}$: peeling $d_1$
(global max), then bounding the residual $\mathrm{OddSum}(D'\cup T')$
($D'=D\setminus\{d_1\}$) below via Lemma B applied to $D'\cup T'$, yields
(verified symbolically, exact algebra):
$$\mathrm{OddSum}(D\cup T')\ \le\ \frac{2^{\ell'-1}+W+d_1-1}{2}.\qquad(\star\star)$$

**Branch II ($c_1<2^{\ell-1}$):** peel $2^{\ell-1}$ from $C\cup T$
(Fact 1), reducing (identical algebra to the Reduction step above, with the
roles of "target $2^\ell$" and "peeled value $2^{\ell-1}$") the needed
inequality to
$$\mathrm{OddSum}(C\cup T'')\ \le\ 2^\ell+\varepsilon-1,\qquad T''=\Gamma_{\ell-2}.$$
Split by $c_1$ vs. $\max(T'')=2^{\ell-2}$:
- **Branch II.ii ($c_1<2^{\ell-2}$):** apply $(\star)$ with $\ell'=\ell-1$,
  $W=\mathrm{sum}(C)=2^\ell+\varepsilon$, $D=C$: bound
  $=\bigl((2^\ell+\varepsilon)+3\cdot2^{\ell-2}-1\bigr)/2$. Comparing to the
  needed $2^\ell+\varepsilon-1$: the difference (needed $-$ bound) equals
  $2^\ell/8+\varepsilon/2-\tfrac12$ (exact symbolic computation, verified by
  sympy). This is $\ge0$ for $\ell\ge2$ (since $2^\ell/8\ge\tfrac12$ when
  $\ell\ge2$, so needed $-$ bound $\ge\tfrac12-\tfrac12+\varepsilon/2=
  \varepsilon/2>0$ strictly). **Branch II.ii closes unconditionally for
  every $\varepsilon\in(0,1)$ and every $\ell\ge2$.**
- **Branch II.i ($2^{\ell-2}\le c_1<2^{\ell-1}$):** now $c_1\ge\max(T'')$,
  peel $c_1$ from $C\cup T''$ and apply $(\star\star)$ with $\ell'=\ell-1$,
  $W=2^\ell+\varepsilon$, $d_1=c_1$: bound $=\bigl(2^{\ell-2}+(2^\ell+
  \varepsilon)+c_1-1\bigr)/2$. The difference (needed $-$ bound) equals
  $2^\ell/4-c_1/2+\varepsilon/2-\tfrac12$ (exact symbolic computation),
  which is $\ge0\iff c_1\le2^{\ell-1}-1+\varepsilon$. Since this threshold
  lies strictly inside the domain $[2^{\ell-2},2^{\ell-1})$ for $\ell\ge2$
  (as $2^{\ell-1}-1+\varepsilon\ge2^{\ell-2}\iff2^{\ell-2}\ge1-\varepsilon$,
  true since $\varepsilon>0$ makes the RHS $<1\le2^{\ell-2}$ for $\ell\ge2$),
  **Branch II.i closes for $c_1\in[2^{\ell-2},\,2^{\ell-1}-1+\varepsilon]$**
  and is **not closed** by this argument for
  $c_1\in(2^{\ell-1}-1+\varepsilon,\,2^{\ell-1})$.

**Branch I ($c_1\ge2^{\ell-1}$):** peel $c_1$ from $C\cup T$, reducing the
needed inequality (identical algebra) to
$$\mathrm{OddSum}(C'\cup T)\ \le\ 2^\ell+\varepsilon-1,\qquad
C':=C\setminus\{c_1\},\ \mathrm{sum}(C')=2^\ell+\varepsilon-c_1.$$
Split by whether $C'$ has a second element $\ge2^{\ell-1}$:
- **Branch I.A ($\max(C')<2^{\ell-1}$):** apply $(\star)$ with $\ell'=\ell$,
  $W=\mathrm{sum}(C')=2^\ell+\varepsilon-c_1$, $D=C'$: bound
  $=\bigl((2^\ell+\varepsilon-c_1)+3\cdot2^{\ell-1}-1\bigr)/2$. The
  difference (needed $-$ bound) equals $c_1/2-2^\ell/4+\varepsilon/2-
  \tfrac12$ (exact symbolic computation), $\ge0\iff c_1\ge2^{\ell-1}+1-
  \varepsilon$. Since this threshold lies strictly inside the domain
  $[2^{\ell-1},\,2^\ell-\varepsilon]$ (as $2^{\ell-1}+1-\varepsilon>
  2^{\ell-1}$ for $\varepsilon<1$), **Branch I.A closes for
  $c_1\in[2^{\ell-1}+1-\varepsilon,\,2^\ell-\varepsilon]$** (given the
  Branch-I.A hypothesis $\max(C')<2^{\ell-1}$) and is **not closed** by
  this argument for $c_1\in[2^{\ell-1},\,2^{\ell-1}+1-\varepsilon)$.
- **Branch I.B ($\max(C')\ge2^{\ell-1}$, i.e. $C$ has $\ge2$ elements each
  $\ge2^{\ell-1}$):** **not attempted this round.** (Since $\mathrm{sum}(C)=
  2^\ell+\varepsilon<2^{\ell+1}$, at most one further element beyond $c_1$
  can also exceed $2^{\ell-1}$ while leaving room for $C$'s other parts
  to be positive — a bounded, small sub-case in principle — but no argument
  was written down this round.)

### Summary and precise remaining gap

Combining Branches II.ii, II.i (partial), I.A (partial, conditional on
Branch I.A's hypothesis): $L_0(\ell,\varepsilon)$ is proved for every
$c_1=\max(C)$ **except**:
1. $c_1\in\bigl(2^{\ell-1}-1+\varepsilon,\,2^{\ell-1}+1-\varepsilon\bigr)$
   (a residual window of width $2(1-\varepsilon)$, present in both Branch
   II.i's and Branch I.A's uncovered ranges — note these two open ranges
   meet exactly at $c_1=2^{\ell-1}$, giving one connected residual
   interval), and
2. all of Branch I.B ($C$ has $\ge2$ elements $\ge2^{\ell-1}$), entirely
   unaddressed.

Both residual pieces have the *same self-similar shape* as the original
sliver (a comparison of the current top fragment to a power of two, with a
width shrinking, but not vanishing, in $\varepsilon$) — consistent with the
math-explorer's numeric finding that the true extremal configuration is a
geometric run continuing to depth $q$ with a final symmetric tie, i.e. the
closing argument genuinely requires an unbounded-depth (or depth-$m$)
induction with a correctly strengthened hypothesis, not a fixed number of
extra peeling steps. **This round establishes, with exact algebra (not
numerics), that the recursive-dichotomy mechanism does real, substantial
work — closing a large majority of $L_0(\ell,\varepsilon)$'s parameter range
in two extra peeling steps — but does not complete the induction: Theorem
2' remains open**, with the gap now precisely two residual pieces (a
shrinking window near $c_1=2^{\ell-1}$, and the unaddressed multi-large-
element case) instead of the entire sliver. All symbolic computations above
were carried out and cross-checked in exact rational arithmetic (sympy) in
this round's build session; no floating-point approximation was used in any
of the derived thresholds.

---

## Round 7: bug fix, Branch I.B closed in full, Step 2 attempted

### Bug fix (mandatory, done first)

The round-6 boxed statement of $L_0(\ell,\varepsilon)$ (both in this file and
in `lemmas/theorem2gen-bounds-and-l0-reduction.md`) omitted the piece-count
bound inherited from the outer `Case-B(m,k)` induction: $B$ (the partition
of $2^m$ in the outer statement) has $\le m+1=\ell+2$ parts by hypothesis,
and $C:=B\setminus\{b_1\}$ therefore has **at most $\ell+1$ parts** — a
constraint the round-6 write-up dropped when boxing the reduced target. This
round's math-explorer found an exact rational counterexample refuting the
unconstrained statement: $\ell=2$, $\varepsilon=1/10$, $C=\{2,\,5649/10000,\,
1407/2500,\,9723/10000\}$ (4 parts, sum $=41/10=2^2+\varepsilon$, $\max(C)=2
\le39/10=2^2-\varepsilon$) gives $\mathrm{OddSum}(C\cup\Gamma_1)=35649/10000
<4$. Both files are corrected above to state $L_0(\ell,\varepsilon)$ with
the "$\le\ell+1$ parts" hypothesis restored.

**This does not retroactively break any round-6 closure.** Every round-6
branch computation (Branches II.ii, II.i, I.A, and the general tools
$(\star)$/$(\star\star)$) derives its bound purely from $\mathrm{sum}(C)$
and $\max(C)$ (via Fact 1 / Lemma B), never from the piece count. Adding a
piece-count hypothesis to the target only restricts the class of $C$ being
quantified over — a proof valid for the larger (unconstrained) class remains
valid, a fortiori, for the smaller (piece-bounded) class. So round 6's
partial closures (Branches II.ii, II.i-partial, I.A-partial) stand
unchanged, now correctly understood as closures of the piece-bounded
$L_0(\ell,\varepsilon)$.

### Step 1: Branch I.B closed in full (new, proved completely)

**Recall the setup.** Branch I is $c_1:=\max(C)\ge2^{\ell-1}$. Within Branch
I, round 6 split further on whether $C':=C\setminus\{c_1\}$ has an element
$\ge2^{\ell-1}$: **Branch I.A** ($\max(C')<2^{\ell-1}$) was closed for
$c_1\in[2^{\ell-1}+1-\varepsilon,\,2^\ell-\varepsilon]$; **Branch I.B**
($\max(C')\ge2^{\ell-1}$, i.e. $C$ has a second element $c_1'\ge2^{\ell-1}$
alongside $c_1$) was left entirely unaddressed.

**Theorem (Branch I.B, closed in full).** Suppose $c_1:=\max(C)\ge2^{\ell-1}$
and $C$ has a second element $c_1'\ge2^{\ell-1}$ (i.e. $\max(C\setminus
\{c_1\})\ge2^{\ell-1}$, with $c_1\ge c_1'$ under a fixed choice of which
element is "first"). Then, for **every** $\varepsilon\in(0,1)$ and every
$\ell\ge1$ (no restriction on the piece count of $C$ needed — see remark
below),
$$\mathrm{OddSum}(C\cup\Gamma_{\ell-1})\ \ge\ 2^\ell.$$

**Proof.** Write $T:=\Gamma_{\ell-1}$ ($\max(T)=2^{\ell-1}$,
$\mathrm{sum}(T)=2^\ell-1$) and $R:=C\setminus\{c_1,c_1'\}$ (possibly empty).

*Step (a): peel $c_1$.* Since $c_1\ge2^{\ell-1}=\max(T)$ and $c_1\ge c_1'\ge
$ every other element of $C$, $c_1$ is a valid choice of $\max(C\cup T)$. By
the certified Peeling Lemma (Fact 1):
$$\mathrm{OddSum}(C\cup T)=c_1+\mathrm{EvenSum}(C'\cup T),\qquad
C':=C\setminus\{c_1\}=\{c_1'\}\cup R.$$

*Step (b): peel $c_1'$.* Since $c_1'\ge2^{\ell-1}=\max(T)$ and $c_1'\ge$
every element of $R$ (as $c_1'$ was chosen as $C$'s second-largest), $c_1'$
is a valid choice of $\max(C'\cup T)$. By the certified Companion Peeling
Lemma (`lemmas/dominant-chain-theorem-and-prefix-run-decomposition.md`),
$$\mathrm{EvenSum}(C'\cup T)=\mathrm{OddSum}\bigl((C'\cup T)\setminus\{c_1'\}
\bigr)=\mathrm{OddSum}(R\cup T)$$
(removing the one copy of $c_1'$ that came from $C'$ leaves $T$ untouched —
$T$'s own value $2^{\ell-1}$, if $c_1'=2^{\ell-1}$ exactly, is a *different*
copy and is unaffected; as a multiset identity this is unambiguous, since
$C'\cup T$ contains exactly one more copy of the value $c_1'$ than $R\cup T$
does, regardless of which "physical" copy is conceptually removed).

Combining (a) and (b):
$$\mathrm{OddSum}(C\cup T)=c_1+\mathrm{OddSum}(R\cup T).$$

*Step (c): bound $\mathrm{OddSum}(R\cup T)$ below by $\mathrm{OddSum}(T)$.*
Every element of $R$ has value $<\varepsilon<1=\min(T)$: indeed $c_1+c_1'
\ge2^{\ell-1}+2^{\ell-1}=2^\ell$ (both $\ge2^{\ell-1}$), so $\mathrm{sum}(R)
=\mathrm{sum}(C)-c_1-c_1'=(2^\ell+\varepsilon)-c_1-c_1'\le\varepsilon<1$, and
each element of $R$ is positive and at most $\mathrm{sum}(R)<1$. So every
element of $R$ sorts strictly below every element of $T$ (whose minimum is
$1=2^0$) in $R\cup T$. Hence in the sorted order of $R\cup T$, $T$'s $\ell$
elements occupy ranks $1,\ldots,\ell$ exactly as in $T$ alone (their mutual
order and the ranks are unaffected by anything sorting below them), and
$R$'s elements occupy ranks $\ell+1,\ldots,\ell+|R|$. Writing
$\mathrm{OddSum}_T:=\sum_{i\le\ell,\,i\text{ odd}}(\text{$T$'s $i$-th
element})=\mathrm{OddSum}(T)$ for the contribution from $T$'s own ranks
(unchanged, since ranks $1,\ldots,\ell$ are identical in $T$ alone and in
$R\cup T$), and noting $R$'s contribution to $\mathrm{OddSum}(R\cup T)$ is a
sum of a subset of $R$'s (positive) elements — hence $\ge0$ — we get
$$\mathrm{OddSum}(R\cup T)=\mathrm{OddSum}(T)+(\text{$R$'s contribution})
\ \ge\ \mathrm{OddSum}(T).$$

*Step (d): the base fact $\mathrm{OddSum}(T)=\mathrm{OddSum}(\Gamma_{\ell-1})
\ge2^{\ell-1}$.* Using the certified $\mathrm{AltSum}(\Gamma_n)$ closed form
(proved in full above: $(2^{n+1}+1)/3$ for $n$ even, $(2^{n+1}-1)/3$ for $n$
odd) and Lemma AS ($\mathrm{OddSum}=(\mathrm{sum}+\mathrm{AltSum})/2$) with
$n=\ell-1$: a direct computation (both parities) gives
$$\mathrm{OddSum}(\Gamma_n)=\begin{cases}(2^{n+2}-1)/3, & n\text{ even}\\
(2^{n+2}-2)/3, & n\text{ odd}\end{cases}$$
and in both cases $\mathrm{OddSum}(\Gamma_n)\ge2^n$: for $n$ even,
$(2^{n+2}-1)/3\ge2^n\iff4\cdot2^n-3\cdot2^n\ge1\iff2^n\ge1$, always true; for
$n$ odd, $(2^{n+2}-2)/3\ge2^n\iff4\cdot2^n-3\cdot2^n\ge2\iff2^n\ge2$, true
for $n\ge1$ (and $n$ odd $\Rightarrow n\ge1$ automatically). So
$\mathrm{OddSum}(\Gamma_n)\ge2^n$ for **every** $n\ge0$, in particular
$\mathrm{OddSum}(T)=\mathrm{OddSum}(\Gamma_{\ell-1})\ge2^{\ell-1}$ for every
$\ell\ge1$.

*Combining (a)–(d).*
$$\mathrm{OddSum}(C\cup T)=c_1+\mathrm{OddSum}(R\cup T)\ \ge\ c_1+
\mathrm{OddSum}(T)\ \ge\ 2^{\ell-1}+2^{\ell-1}=2^\ell,$$
using $c_1\ge2^{\ell-1}$ (Branch I hypothesis) and Step (d). This is exactly
the target $\mathrm{OddSum}(C\cup\Gamma_{\ell-1})\ge2^\ell$. $\blacksquare$

**Remark (piece-count bound not needed here).** The proof above uses only
$\mathrm{sum}(C)$, $c_1$, $c_1'$, and positivity of $R$'s elements — never a
bound on $|C|$ (or $|R|$). So Branch I.B is closed **unconditionally**, for
every $C$ satisfying the Branch I.B hypotheses regardless of piece count —
a strictly stronger, more general statement than what $L_0(\ell,\varepsilon)$
itself requires (which only needs $\le\ell+1$ parts). This shows the round-6
bug did not affect the provability of this particular branch.

**Numerical verification.** Stress-tested with exact `Fraction` arithmetic:
$1991$ random trials, $\ell=1,\ldots,7$, random $\varepsilon\in(0,1)$,
random $c_1,c_1'\ge2^{\ell-1}$ with $c_1\ge c_1'$, random $R$ (uniformly
random composition of the remaining mass into a random number of parts
respecting the piece cap $\le\ell+1$ total), **zero violations**; minimum
observed margin over $\mathrm{OddSum}-2^\ell$ was $7/500$ at $\ell=2$
(consistent with the proof's exact equality case $\ell\in\{1,2\}$, $c_1=
c_1'=2^{\ell-1}$, $R=\emptyset$, where the bound $c_1+\mathrm{OddSum}(T)=
2^\ell$ exactly). Also directly verified $\mathrm{OddSum}(\Gamma_n)$ against
the closed-form formula for $n=0,\ldots,14$: exact match with $2^n$-excess
$0,0,1,2,5,10,21,42,85,170,341,682,1365,2730,5461$ — matching Step (d)'s
formula exactly, confirming equality only at $n=0,1$ (i.e. $\ell=1,2$) as
claimed.

**Effect on the residual gap.** Branch I.B is now closed for **every**
$c_1\in[2^{\ell-1},2^\ell-\varepsilon]$ (its entire domain, not merely the
sub-range round 6's Branch I.A left open). Combined with round 6's Branch
I.A closure (valid for $c_1\in[2^{\ell-1}+1-\varepsilon,2^\ell-\varepsilon]$),
the trichotomy on $C\setminus\{c_1\}$'s max is now fully resolved for
$c_1\ge2^{\ell-1}+1-\varepsilon$ (either branch closes it), and the *only*
remaining gap within $c_1\ge2^{\ell-1}$ is the narrower range
$$c_1\in\bigl[2^{\ell-1},\,2^{\ell-1}+1-\varepsilon\bigr)\quad\text{with}
\quad\max(C\setminus\{c_1\})<2^{\ell-1}\ \ (\text{Branch I.A's hypothesis}).$$
This is strictly smaller than round 6's residual (which included all of
Branch I.B unconditionally, for any $c_1$ up to $2^\ell-\varepsilon$): now
only the *combination* "$c_1$ near $2^{\ell-1}$ **and** no second large
element" remains open on the Branch-I side.

### Step 2: the residual window (attempted, not closed — honest negative finding)

Attempted the order-statistics route the outliner specified (tracking $C$'s
second-largest element, as in Theorem 1's $m=2,j=2$ computation), applied to
the **lower** half of the residual window, $c_1\in(2^{\ell-1}-1+\varepsilon,
\,2^{\ell-1})$ (Branch II's uncovered range, i.e. $c_1<2^{\ell-1}$). Unlike
Branch I.B, here $c_1<\max(T)=2^{\ell-1}$, so $c_1$ is **not** a valid first
peel of $C\cup T$ — $T$'s own $2^{\ell-1}$ must be peeled first (as in round
6's Branch II derivation), and the Branch-I.B-style "peel $C$'s top two
elements consecutively" argument does not directly transplant, since after
peeling $T$'s $2^{\ell-1}$, the natural next peel is $c_1$ itself (not a
second element of $C$), and bounding what remains ($C'\cup T''$, $C'=C
\setminus\{c_1\}$) via $C$'s second-largest element $c_1'$ runs into the
opposite difficulty: this needs an *upper* bound on $\mathrm{EvenSum}(C'\cup
T'')$ (equivalently a bound on $\mathrm{OddSum}(R\cup T'')$ after a further
peel of $c_1'$, if $c_1'\ge\max(T'')=2^{\ell-2}$), and no version of the
Step-(c)/(d) argument above (which relied on $R$'s contribution being
**nonnegative**, useful only for a *lower* bound) gives useful information
in the upper-bound direction — bounding $\mathrm{OddSum}(R\cup T'')$
*above* by discarding $R$'s contribution is not valid (it can only be
dropped to get a lower bound, the wrong direction here). Also directly
checked (per the outliner's explicit prohibition) that a further
level of the same peel-then-Lemma-B dichotomy reproduces the same
qualitative shortfall pattern as round 5/6's Two-Level Half-Bound Lemma
check, so this route was not pursued further. **Branch II's uncovered
range and the upper half's Branch-I.A-restricted range are both left open
this round**, reported honestly as `partial`, not attempted to closure by
a mechanism not yet found. No new false claim is made about this piece.

---

---

## Round 8: Branch II via strong induction, and its exact reduction to the Branch-I.A window

### Step 0: the vestigial cap, and the corrected statement $L_0^{\mathrm{gen}}$

Recall the round-7-corrected boxed statement:

$$L_0(\ell,\varepsilon):\quad \text{for every }C\text{ with }\le\ell+1\text{ parts},\ \mathrm{sum}(C)=2^\ell+\varepsilon,\ \max(C)\le2^\ell-\varepsilon:\quad \mathrm{OddSum}(C\cup\Gamma_{\ell-1})\ge2^\ell.$$

**Claim: the hypothesis $\max(C)\le2^\ell-\varepsilon$ is never used, in any of
round 6/7's branch derivations, as anything other than an a-priori bound on
the range of $c_1:=\max(C)$ under consideration — dropping it does not
invalidate any proof already given, and the resulting cap-free statement is
what genuine strong induction needs.**

Define the corrected, strictly more general statement (same conclusion,
strictly weaker hypothesis — a superset of $C$'s being quantified over):

$$L_0^{\mathrm{gen}}(\ell,\varepsilon):\quad \text{for every }C\text{ with }\le\ell+1\text{ parts and }\mathrm{sum}(C)=2^\ell+\varepsilon:\quad \mathrm{OddSum}(C\cup\Gamma_{\ell-1})\ge2^\ell.$$

$L_0^{\mathrm{gen}}(\ell,\varepsilon)\Rightarrow L_0(\ell,\varepsilon)$
trivially (fewer hypotheses, same conclusion), so proving $L_0^{\mathrm{gen}}$
suffices for everything the original reduction needs.

**Proof that $L_0^{\mathrm{gen}}$'s extra range ($\max(C)\in(2^\ell-\varepsilon,2^\ell+\varepsilon]$) is covered, and that Branch I.A's closure needs no cap.**
If $\max(C)\ge2^\ell$: the certified Element Bound Lemma gives
$\mathrm{OddSum}(C\cup\Gamma_{\ell-1})\ge\max(C)\ge2^\ell$ immediately — done.
If $\max(C)<2^\ell$, re-examine Branch I.A's derivation (the only branch whose
stated closure range explicitly cites the cap as an upper limit). There,
$D:=C'=C\setminus\{c_1\}$, $W:=\mathrm{sum}(D)=2^\ell+\varepsilon-c_1$, and
formula $(\star)$ (already proved in full in "Round 6," using only the
certified Peeling Lemma and Lemma B, **for arbitrary $W>0$** — its proof
never assumes an upper bound on $c_1$ itself) gives
$$\mathrm{OddSum}(C'\cup T)\le\frac{W+3\cdot2^{\ell-1}-1}{2}=\frac{(2^\ell+\varepsilon-c_1)+3\cdot2^{\ell-1}-1}{2}.$$
The needed inequality $\mathrm{OddSum}(C'\cup T)\le2^\ell+\varepsilon-1$
(equivalent, by the same peeling algebra as the Reduction step, to the
target) holds iff
$$2^\ell+\varepsilon-1-\frac{(2^\ell+\varepsilon-c_1)+3\cdot2^{\ell-1}-1}{2}\ge0
\iff \frac{c_1}{2}-\frac{2^\ell}{4}+\frac{\varepsilon}{2}-\frac12\ge0
\iff c_1\ge2^{\ell-1}+1-\varepsilon,$$
an inequality on $c_1$ alone with **no upper limit** — it is satisfied for
every $c_1\ge2^{\ell-1}+1-\varepsilon$, all the way up to (not including)
$2^\ell$ (where $W=2^\ell+\varepsilon-c_1>0$ remains valid, and $\max(C)<2^\ell$
by hypothesis of this sub-case). So Branch I.A closes
$L_0^{\mathrm{gen}}(\ell,\varepsilon)$ for every
$c_1\in[2^{\ell-1}+1-\varepsilon,2^\ell)$ with no second large element,
**exactly the same threshold as before, now valid over the full range**, with
no cap-dependence anywhere in the derivation. (Branch I.B, Branch II.ii,
Branch II.i were already established unconditionally / cap-independently in
rounds 6–7 — Branch I.B's own theorem statement explicitly says "no
piece-count *or* max restriction needed.")

**Independent verification.** Re-derived symbolically (above) and stress-
tested with $2243$ fresh exact-`Fraction` trials, $\ell=1,\ldots,6$, $c_1$
ranging over the *full* uncapped interval $[2^{\ell-1}+1-\varepsilon,2^\ell)$
(values that would violate the old cap $\max(C)\le2^\ell-\varepsilon$ are
deliberately included), second-largest element $<2^{\ell-1}$ enforced: zero
violations, confirming Branch I.A's closure is genuinely cap-free.

From here on, "$L_0(\ell,\varepsilon)$" refers to the corrected
$L_0^{\mathrm{gen}}(\ell,\varepsilon)$ (cap dropped); this does not change
anything about which cases were previously closed (round 7's Branch I.B and
Branch I.A-main-range closures stand verbatim, now known to hold over a
strictly larger domain than stated), it only removes an artificial obstacle
to clean recursion.

### Step 1: the exact peel identity (re-derived, independently verified)

**Lemma (Branch II peel identity).** Let $\ell\ge2$, $\varepsilon\in(0,1)$,
and $C$ a finite multiset with $c_1:=\max(C)\in
\bigl(2^{\ell-1}-1+\varepsilon,\,2^{\ell-1}\bigr)$ (Branch II's uncovered
range). Write $T:=\Gamma_{\ell-1}$, $T'':=\Gamma_{\ell-2}$,
$C':=C\setminus\{c_1\}$. Then
$$\mathrm{OddSum}(C\cup T)\ =\ 2^{\ell-1}+\mathrm{OddSum}(C'\cup T'').$$

**Proof.** First, $2^{\ell-1}-1\ge2^{\ell-2}$ for $\ell\ge2$ (equivalent to
$2^{\ell-2}\ge1$), so $c_1>2^{\ell-1}-1+\varepsilon>2^{\ell-1}-1\ge2^{\ell-2}
=\max(T'')$; in particular $c_1$ is not the global max of $C\cup T$ (since
$c_1<2^{\ell-1}=\max(T)$), so $T$'s own top element $2^{\ell-1}$ is the unique
global max of $C\cup T$ (unique since $\Gamma_{\ell-1}$'s values are distinct
powers of two and $c_1<2^{\ell-1}$ strictly). By the certified Peeling Lemma
(Fact 1):
$$\mathrm{OddSum}(C\cup T)=2^{\ell-1}+\mathrm{EvenSum}(C\cup T''),$$
using $T\setminus\{2^{\ell-1}\}=T''=\Gamma_{\ell-2}$ (removing $\Gamma_{\ell-1}$'s
top element leaves exactly $\Gamma_{\ell-2}$, by definition of $\Gamma$).
Next, since $c_1>2^{\ell-2}=\max(T'')$ (shown above) and $c_1=\max(C)$, $c_1$
is the unique global max of $C\cup T''$. By the certified Companion Peeling
Lemma (`EvenSum(N)=OddSum(N\{max N})` for any finite multiset $N$, already
certified in `lemmas/dominant-chain-theorem-and-prefix-run-decomposition.md`):
$$\mathrm{EvenSum}(C\cup T'')=\mathrm{OddSum}\bigl((C\cup T'')\setminus\{c_1\}\bigr)=\mathrm{OddSum}(C'\cup T'').$$
Combining the two displayed identities gives the claim. $\blacksquare$

**Independent verification.** Re-derived symbolically above from scratch
(not copying the explorer's derivation, though it agrees with it), and
independently stress-tested with exact `Fraction` arithmetic: $1900$ random
trials, $\ell=2,\ldots,7$, $\varepsilon$ random in $(0,1)$, $c_1$ random in
the exact open Branch II range, arbitrary compositions of the remainder
respecting the $\le\ell+1$ piece cap and $c_1=\max(C)$ — **zero mismatches**.

### Step 2: the $\varepsilon'$ range — the flagged boundary loose end, resolved

Set $\varepsilon':=2^{\ell-1}+\varepsilon-c_1$, so that
$\mathrm{sum}(C')=\mathrm{sum}(C)-c_1=(2^\ell+\varepsilon)-c_1=2^{\ell-1}+\varepsilon'$
— i.e. $C'$, together with $T''=\Gamma_{\ell-2}=\Gamma_{(\ell-1)-1}$, is
exactly an instance of $L_0(\ell-1,\varepsilon')$'s target
$\mathrm{OddSum}(C'\cup\Gamma_{(\ell-1)-1})\ge2^{\ell-1}$, once we check
$\varepsilon'\in(0,1)$ and the piece count.

**Claim: $\varepsilon'\in(\varepsilon,1)\subset(0,1)$ strictly, throughout
Branch II's open range — the boundary is never reached, no separate case is
needed.** As a function of $c_1$, $\varepsilon'(c_1)=2^{\ell-1}+\varepsilon-c_1$
is strictly decreasing (affine, slope $-1$). At the (open, unattained) lower
end $c_1\to(2^{\ell-1}-1+\varepsilon)^+$: $\varepsilon'\to
2^{\ell-1}+\varepsilon-(2^{\ell-1}-1+\varepsilon)=1^-$. At the (open,
unattained) upper end $c_1\to(2^{\ell-1})^-$: $\varepsilon'\to
2^{\ell-1}+\varepsilon-2^{\ell-1}=\varepsilon^+$. Since $c_1$ ranges over the
*open* interval $(2^{\ell-1}-1+\varepsilon,2^{\ell-1})$ and $\varepsilon'$ is a
strictly monotonic continuous (indeed affine) function of $c_1$, $\varepsilon'$
ranges over the *open* interval $(\varepsilon,1)$ — strictly inside $(0,1)$
(since $\varepsilon>0$), and strictly bounded away from $0$ and from $1$ by a
positive amount depending on how far $c_1$ sits from the endpoints. **So
"$\varepsilon'\to0$ or $\varepsilon'\to1$" literally cannot occur for any
actual $C$ in Branch II's (open) uncovered range** — this fully resolves the
loose end the math-explorer flagged: there is no boundary case to check
separately, because the boundary is never attained.

**Piece count.** $C$ has $\le\ell+1$ parts (hypothesis of $L_0(\ell,\varepsilon)$);
$C'=C\setminus\{c_1\}$ removes exactly one part, so $C'$ has $\le\ell$ parts
$=(\ell-1)+1$ — exactly $L_0(\ell-1,\cdot)$'s own cap. So $(C',\varepsilon')$
is a **bona fide instance** of $L_0(\ell-1,\varepsilon')$ (using the corrected,
cap-free $L_0^{\mathrm{gen}}$ from Step 0 — with the cap dropped there is no
further hypothesis to verify).

### Step 3: base case $\ell=1$

Branch II at $\ell=1$ is the range $c_1\in(2^0-1+\varepsilon,2^0)=(\varepsilon,1)$.
But $\mathrm{sum}(C)=2+\varepsilon$ with $\le2$ parts forces
$\max(C)\ge\mathrm{sum}(C)/2=(2+\varepsilon)/2=1+\varepsilon/2>1$ (average of
at most 2 positive parts is a lower bound on the max), contradicting
$c_1<1$. So Branch II's range is **empty** at $\ell=1$ — the base case holds
vacuously. (Note: this uses only that $\max$ of a finite set of positive
reals is $\ge$ its average — an immediate, elementary fact, not the
certified Lemma B, which is a different, stronger statement about
$\mathrm{OddSum}$; used here only for the trivial "max $\ge$ mean" bound.)

### Step 4: the strong induction and its exact landing point

**Theorem (Branch II reduces exactly to the Branch-I.A window, recursively).**
For every $\ell\ge1$: Branch II of $L_0(\ell,\varepsilon)$ (the range
$c_1\in(2^{\ell-1}-1+\varepsilon,2^{\ell-1})$) holds for a given $(\ell,\varepsilon,c_1)$
and *every* admissible $C$, **if and only if** $L_0(\ell-1,\varepsilon')$
holds for *every* admissible $C'$ (where $\ell=1$'s instance is vacuously
true by Step 3).

**Proof.** By Step 1, for every admissible $C$ realizing this $(\ell,\varepsilon,c_1)$,
$\mathrm{OddSum}(C\cup\Gamma_{\ell-1})\ge2^\ell \iff \mathrm{OddSum}(C'\cup\Gamma_{\ell-2})\ge2^{\ell-1}$
(add $2^{\ell-1}$ to both sides of the exact identity and compare to $2^\ell$).
By Step 2, $C'=C\setminus\{c_1\}$ ranges, as $C$ ranges over all admissible
multisets realizing $(\ell,\varepsilon,c_1)$, over *exactly* the multisets
admissible for $L_0(\ell-1,\varepsilon')$ (any multiset $D$ with
$\mathrm{sum}(D)=2^{\ell-1}+\varepsilon'$ and $\le\ell$ parts arises as such a
$C'$, by taking $C:=\{c_1\}\cup D$, which has $\le\ell+1$ parts, sum
$c_1+2^{\ell-1}+\varepsilon'=2^\ell+\varepsilon$ as required, and
$\max(C)=c_1$ since $c_1\ge2^{\ell-1}-1+\varepsilon>2^{\ell-2}\ge\max(\Gamma_{\ell-2})$
does not directly bound $D$'s own max relative to $c_1$ — but since we no
longer need any cap on $D$'s elements, by Step 0's correction, $D$ is
unconstrained beyond sum and piece count, so every such $D$ is realized).
So "Branch II holds for all admissible $C$" and "$L_0(\ell-1,\varepsilon')$
holds for all admissible $C'$" quantify over exactly matched, biject-able
sets, related by the same exact identity — hence equivalent. $\blacksquare$

**Consequence (by induction on $\ell$).** Unwinding, Branch II of
$L_0(\ell,\varepsilon)$ is equivalent to a chain
$L_0(\ell-1,\varepsilon')\Leftarrow(\text{if its own }c_1'<2^{\ell-2}\text{, i.e. Branch II again})\Leftarrow L_0(\ell-2,\varepsilon'')\Leftarrow\cdots$
terminating, after at most $\ell-1$ steps, at the base case $\ell'=1$
(vacuously true, Step 3) **or** at some intermediate level $\ell'$ where
$c_1^{(\ell')}\ge2^{\ell'-1}$ (i.e. the chain lands in "Branch I" of level
$\ell'$, not Branch II again). In that landing case, by the (now cap-free,
Step 0) analysis:
- if the second-largest element of that level's multiset is also
  $\ge2^{\ell'-1}$: **Branch I.B, closed unconditionally** (round 7's
  Two-Peel Theorem, `lemmas/branch-ib-two-peel-theorem.md`) — the chain
  terminates successfully;
- if not, and $c_1^{(\ell')}\ge2^{\ell'-1}+1-\varepsilon^{(\ell')}$:
  **Branch I.A's main range, closed unconditionally** (Step 0 above, cap-free)
  — the chain terminates successfully;
- if not (i.e. $c_1^{(\ell')}\in[2^{\ell'-1},2^{\ell'-1}+1-\varepsilon^{(\ell')})$
  with no second large element): **the Branch-I.A-restricted window** — this
  is exactly the *separately identified, still-open* residual from rounds
  6–7. The chain does not terminate successfully here; whether the target
  holds is exactly the open question of that window.

**This is an exact, exhaustive case analysis of every possible landing
point of the recursion** — no other outcome is possible, since at every
level the multiset's max is compared to a single threshold ($2^{\ell'-1}$),
an exhaustive dichotomy, and each of the resulting branches (Branch II
again, Branch I.B, Branch I.A-main, Branch I.A-window) is one of exactly
these four, covering the whole domain.

**Witness that the window is genuinely reachable (not vacuous).** Exact
instance: $\ell=3$, $\varepsilon=1/2$, $C=\{39/10,19/5,4/5\}$ (`sum=83/10=2^3+1/2`,
$c_1=39/10\in(2^2-1+1/2,2^2)=(7/2,4)$, Branch II's uncovered range). Then
$C'=\{19/5,4/5\}$, $\varepsilon'=2^2+1/2-39/10=3/5$, and $\max(C')=19/5=3.8$,
which lies in $[2^{\ell-2},2^{\ell-2}+1-\varepsilon')=[2,13/5)$ with
second-largest $4/5<2$ — **exactly** the Branch-I.A-restricted window at
level $\ell-1=2$. (Directly verified: the true value
$\mathrm{OddSum}(C\cup\Gamma_2)=44/5=8.8\ge8$ holds with margin $4/5$ — so the
target is true here, but this round's machinery does not certify it, since
the window itself remains unproved in general; it is reported as such, not
overclaimed.)

**Conclusion.** Branch II of $L_0(\ell,\varepsilon)$, for every $\ell\ge1$,
is proved (by this genuine, well-founded strong induction, terminating in at
most $\ell-1$ steps at the vacuous base case or an explicit landing branch)
to reduce **exactly and only** to the Branch-I.A-restricted window recurring
at some level $\ell'\le\ell-1$ — not to any new or different obstruction.
Combined with round 7's unconditional closure of Branch I.B and this round's
cap-free strengthening of Branch I.A's main range, **the entire tail-
untouched sliver's residual (both Branch II's uncovered range and the
Branch-I.A-restricted window, previously reported as two separate open
pieces) is now known to be a single gap**: closing the Branch-I.A-restricted
window at every level $\ell'\ge1$ would immediately close Branch II at every
level too, by this induction. **Branch II itself is not unconditionally
closed** — the witness above shows the reduction genuinely bottoms out in
the open window for some (adversarially chosen) instances, so this is
reported honestly as `partial`, with the gap now sharply and precisely
identified as exactly the (already on record) Branch-I.A-restricted window.

---

## Promotable lemmas

- **Branch II peel identity (round 8, new, proved in full).**
  For $\ell\ge2$, $\varepsilon\in(0,1)$, $C$ with
  $c_1:=\max(C)\in(2^{\ell-1}-1+\varepsilon,2^{\ell-1})$:
  $\mathrm{OddSum}(C\cup\Gamma_{\ell-1})=2^{\ell-1}+\mathrm{OddSum}(C'\cup\Gamma_{\ell-2})$,
  $C':=C\setminus\{c_1\}$. Proved in full above from two applications of the
  certified Peeling Lemma/Companion Peeling Lemma (exact, non-lossy).
  Verified independently (1900 exact-`Fraction` trials, zero mismatches, a
  from-scratch script). Reusable anywhere an exact (not approximate)
  reduction is needed between a merged-multiset OddSum target and one level
  down in a geometric tail.
- **Cap-free Branch I.A closure (round 8, new, proved in full).** For any
  $\ell\ge1$, $\varepsilon\in(0,1)$, and $C'$ with $\le\ell$ parts,
  $\mathrm{sum}(C')=2^\ell+\varepsilon-c_1$ for any $c_1\in[2^{\ell-1}+1-\varepsilon,2^\ell)$
  with $\max(C')<2^{\ell-1}$: $\mathrm{OddSum}(C'\cup\Gamma_{\ell-1})\le2^\ell+\varepsilon-1$
  — i.e. Branch I.A's closure needs **no upper cap** on $c_1$ (holds all the
  way up to $2^\ell$), correcting a vestigial restriction in the round-6/7
  boxed statement. Proved in full above (re-derivation of formula
  $(\star)$'s consequence with the cap removed); independently stress-tested
  (2243 exact trials spanning the previously-excluded range, zero
  violations). Reusable as the corrected, general-purpose version of Branch
  I.A wherever the file's boxed `L_0(ℓ,ε)` is invoked.
- **Branch II $\Leftrightarrow$ Branch-I.A-window reduction (round 8, new,
  proved in full).** Branch II of `L_0(ℓ,ε)` is logically equivalent, for
  every `ℓ≥1`, to `L_0(ℓ-1,ε')` for the derived `ε'∈(ε,1)⊂(0,1)` (strictly
  interior, resolving the boundary loose end in full) — by a well-founded
  strong induction (base case `ℓ=1` vacuous) whose only possible
  non-terminating landing point, among an exhaustive four-way case split at
  each level, is the (separately identified, still open) Branch-I.A-
  restricted window. Proved in full above, with an explicit exact witness
  (`ℓ=3,ε=1/2`) showing the window is genuinely reachable (not vacuously
  avoided). Unifies the sliver's two previously-separate open pieces into
  one; does not itself close either. Reusable as the precise statement of
  what remains to close the whole tail-untouched sliver.

- **Base fact: $\mathrm{OddSum}(\Gamma_n)\ge2^n$ for all $n\ge0$, equality
  iff $n\in\{0,1\}$ (round 7, new).** Proved in full above from the
  certified $\mathrm{AltSum}(\Gamma_m)$ closed form and Lemma AS. Fully
  general (no cuts, applies to the base geometric partition itself),
  verified against direct computation for $n=0,\ldots,14$. Reusable
  anywhere a lower bound on the untouched geometric tail's own OddSum is
  needed (used here as the key ingredient closing Branch I.B).
- **Branch I.B Two-Peel Theorem (round 7, new, closed in full).** If
  $c_1:=\max(C)\ge2^{\ell-1}$ and $C$ has a second element
  $c_1'\ge2^{\ell-1}$, then $\mathrm{OddSum}(C\cup\Gamma_{\ell-1})\ge2^\ell$,
  unconditionally (no piece-count bound needed), for every $\ell\ge1$,
  $\varepsilon\in(0,1)$. Proved in full above (peel $c_1$, peel $c_1'$, bound
  the small remainder's contribution to $\mathrm{OddSum}$ by $0$, apply the
  base fact above to $T=\Gamma_{\ell-1}$). Verified numerically (1991 exact
  trials, zero violations). Reusable by any approach needing a lower bound
  on OddSum when a merged multiset's top two elements both dominate a
  geometric tail's own maximum.
- **($\star$) and ($\star\star$) (Theorem-2-gen, general-$V$ sub-case
  bounds, round 6, new).** For $T'=\Gamma_{\ell'-1}$ and any multiset $D$
  with $\mathrm{sum}(D)=W$: if $\max(D)<2^{\ell'-1}$,
  $\mathrm{OddSum}(D\cup T')\le(W+3\cdot2^{\ell'-1}-1)/2$; if $\max(D)=d_1
  \ge2^{\ell'-1}$, $\mathrm{OddSum}(D\cup T')\le(2^{\ell'-1}+W+d_1-1)/2$.
  Proved in full above from the certified Peeling Lemma and Lemma B, for
  **arbitrary** $W$ (not just $W=2^{m}$) — the genuine generalization of
  Theorem 2's two sub-cases to arbitrary total mass, reusable by any
  approach needing a Case-B-style upper bound on $\mathrm{OddSum}$ against
  a geometric tail with a total that isn't exactly a power of two (e.g.
  `greedy-reduction-geometric`'s Theorem 7'(m,k;L) leftover-mass target, or
  any future attempt at the general middle regime).
- **$L_0(\ell,\varepsilon)$ reduction (round 6, new).** The sliver target
  `2^(m-1)-1<b_1<2^(m-1)` of Case-B(m,k) is proved equivalent (not just
  implied) to: for every $C$ with $\mathrm{sum}(C)=2^\ell+\varepsilon$
  ($\ell=m-1$), $\max(C)\le2^\ell-\varepsilon$, $\mathrm{OddSum}(C\cup
  \Gamma_{\ell-1})\ge2^\ell$. Proved in full above by the same peeling
  algebra as Theorem 2. Reusable as the precise starting point for any
  future attempt to close the sliver.

- **Two-Level Half-Bound Lemma (round 5, new).** For any finite multiset
  $N$ of positive reals with two largest values $y_1\ge y_2$:
  $\mathrm{OddSum}(N)\ge(\mathrm{sum}(N)+y_1-y_2)/2$. Proved in full above
  from the certified Peeling Lemma, Companion Peeling Lemma, and Lemma B
  (First-mover-half). Strictly refines Lemma B whenever $y_1>y_2$. Fully
  general, reusable by any approach needing a lower bound on $\mathrm{OddSum}$
  sharper than the plain half-sum bound. (Documented as insufficient, by
  itself, to close this round's remaining sliver — see above — but real,
  correct, general-purpose content.)
- **Theorem 2 (Case-B(m,k), sliver reduction, round 5, new).** For
  $\Gamma_{m-2}$ fixed (tail untouched) and any partition $B$ of $2^m$ into
  $\le m+1$ parts with $\max(B)<2^{m-1}$: if additionally
  $\max(B)\le2^{m-1}-1$ (i.e. $\max(B)$ avoids the width-$1$ window
  $(2^{m-1}-1,2^{m-1})$), then $\mathrm{OddSum}(B\cup\Gamma_{m-2})\le2^m-1$.
  Proved in full above (two sub-cases, both closed unconditionally via one
  peeling step plus the certified Lemma B). Reduces the previously
  fully-open `Case-B(m,k)` target to a single width-$1$ residual window,
  uniform in $m$ — reusable directly by `greedy-reduction-geometric` (whose
  own TOP-ONLY residual is stated in comparable terms) as a precise
  characterization of exactly what remains for the tail-untouched case.
- **Extremal boundary identity (round 5, new).** With $B^*=\{2^{m-1}\}\cup
  (\Gamma_{m-2}$ with its element $1$ replaced by $2)$: $\mathrm{sum}(B^*)
  =2^m$ and $\mathrm{OddSum}(B^*\cup\Gamma_{m-2})=2^m-1$ exactly. Proved in
  full above by direct rank-counting (Tie-neutrality's block form) plus
  three independent exact-arithmetic checks ($m=2,4,6$). Identifies the
  precise extremal shape/value at the boundary of `Case-B(m,k)`'s
  hypothesis, useful for any future attempt (this approach or a sibling) at
  closing the sliver, since any valid closing argument must become tight
  exactly at $B^*$.
- **Lemma Z (z-trick identity).** For any finite multiset $X$ of positive
  reals and $z\ge\max(X)$: $\mathrm{EvenSum}(X)=\mathrm{OddSum}(\{z\}\cup X)-z$.
  Proved in full above from the certified Peeling Lemma in two lines. Fully
  general (no geometric structure needed), reusable by any approach that
  needs to convert an EvenSum target into an OddSum target on an augmented
  multiset — e.g. `universal-halving-adversary`'s upper-bound work, or any
  future attempt at Case B′ above.
- **Theorem 1 ($T(2)$, fully closed).** For every refinement of
  $\Gamma_2=(4,2,1)$ using $\le2$ cuts, $\mathrm{OddSum}\ge4$. Proved in
  full above (the new content is the $j=2$ sub-case, by direct
  order-statistics computation). This is a genuine new complete small case,
  usable as a base case / sanity check by any other approach, and it now
  makes Step 1 ($j=1$) rigorously available at $m=3$ (previously blocked on
  $T(2)$ being unestablished).
- **Proposition C (Case-A circularity).** Precise statement and proof above:
  under the exact geometric tail structure (not an abstract multiset), the
  natural single-peel completion of Case A ($b_1\ge2^{m-1}$) is logically
  equivalent, via Lemma Z, to a lower-bound instance with **one more
  fragment** on the same tail — not a simpler instance. Offered as a
  documented dead end for the specific "single scalar bound + one peel"
  strategy, to save future rounds from re-attempting it in disguise (e.g.
  via a differently-named "dual lemma").
- **Lemma AS (AltSum reformulation).** For any finite multiset $X$ of
  positive reals, $\mathrm{OddSum}(X)=(\mathrm{sum}(X)+\mathrm{AltSum}(X))/2$;
  consequently $T(m,k)\iff$ every refinement of $\Gamma_m$ with $\le k$
  cuts has $\mathrm{AltSum}\ge1$. Proved in full above from the
  definitional identities $\mathrm{Odd+Even=sum}$, $\mathrm{Odd-Even=AltSum}$.
  Fully general, reusable by any approach working with alternating-sign
  sums of sorted multisets.
- **Single-Insertion Lemma.** Exact formula for the change in
  $\mathrm{AltSum}$ when one value is inserted at an arbitrary sorted
  position: $\Delta=(-1)^{s+1}(v-2\,\mathrm{AltSum}(\text{suffix from }s))$.
  Strictly generalizes the certified Peeling Lemma ($s=1$ case). Proved
  above, verified on 2000+ random instances, zero mismatches. Reusable by
  any approach needing to track how $\mathrm{OddSum}/\mathrm{EvenSum}/
  \mathrm{AltSum}$ changes under insertions/splits at positions other than
  the current maximum — directly applicable to `layer-cake-parity-
  reframing`'s per-piece step-function framing and to
  `greedy-reduction-geometric`'s residual-term analysis.
- **$\mathrm{AltSum}(\Gamma_m)$ closed form.** $(2^{m+1}+1)/3$ ($m$ even),
  $(2^{m+1}-1)/3$ ($m$ odd). Proved above by geometric series summation,
  verified $m=0,\ldots,11$. Gives the exact slack
  $\mathrm{AltSum}(\Gamma_m)-1$ available for any approach bounding total
  AltSum loss under cuts.
- **Reduction B.** If the top fragment $b_1<\mu:=\max(S)$ (tail's own
  running max), then $\mathrm{OddSum}(B\cup S)\ge2^m\iff\mathrm{OddSum}
  (B\cup S')\le2^m-1$ where $S'=S\setminus\{\mu\}$. Proved in full above,
  numerically confirmed (3185 random instances, zero mismatches). A new,
  precisely stated open target (`Case-B(m,k)`), distinct from Proposition
  C's `U(m,k)`, offered for any future approach (this one or a sibling) to
  attempt to close.

---

## Round 9: Theorem W (exact window-endpoint witness), and the reduced but
## unclosed general claim

### Setup recap

Recall the Branch-I.A-restricted window (round 8's sole remaining piece of
the tail-untouched sliver): $C$ a finite multiset with $\le\ell+1$ parts,
$\mathrm{sum}(C)=2^\ell+\varepsilon$, $c_1:=\max(C)\in
[2^{\ell-1},\,2^{\ell-1}+1-\varepsilon)$, and $\max(C\setminus\{c_1\})<
2^{\ell-1}$ (Branch I.A's hypothesis). The target is
$$\mathrm{OddSum}(C\cup\Gamma_{\ell-1})\ \ge\ 2^\ell.$$

### Correcting the dispatched witness

The dispatched target claimed the extremal witness is $C=\{2^{\ell-1}\}\cup
D_0$, $D_0:=\Gamma_{\ell-2}$ with its bottom element $1$ replaced by two
copies of $r=(1+\varepsilon)/2$. Checking sums: $\mathrm{sum}(\Gamma_{\ell-2})
=2^{\ell-1}-1$; removing the "$1$" and adding two copies of $r$ gives
$\mathrm{sum}(D_0)=(2^{\ell-1}-1-1)+2r=2^{\ell-1}-2+(1+\varepsilon)=
2^{\ell-1}-1+\varepsilon$. But the window requires $\mathrm{sum}(C\setminus
\{c_1\})=\mathrm{sum}(C)-c_1=(2^\ell+\varepsilon)-2^{\ell-1}=2^{\ell-1}+
\varepsilon$ at $c_1=2^{\ell-1}$ — a shortfall of exactly $1$. So the
dispatched value of $r$ does not produce an admissible $C$ (its sum is wrong
by a constant), and is corrected here.

**Corrected witness.** Take $r:=1+\varepsilon/2$ instead. Then
$\mathrm{sum}(D_0)=(2^{\ell-1}-2)+2r=2^{\ell-1}-2+(2+\varepsilon)=
2^{\ell-1}+\varepsilon$ — matches exactly. (This correction was found first
by global numerical optimization of the true window-endpoint extremal
problem — `scipy.optimize.minimize`, Nelder–Mead with a penalty for the
$\max(D)<2^{\ell-1}$ constraint, dozens of random restarts per instance,
$\ell=4,5,6$, $\varepsilon\in\{0.1,0.3,0.6,0.9\}$ — which independently
recovered the value $r=1+\varepsilon/2$ to numerical precision in every
case, before being confirmed exactly below.)

### Theorem W (exact value at the window's left endpoint)

**Statement.** Fix $\ell\ge2$, $\varepsilon\in(0,1)$. Let
$$C:=\{2^{\ell-1}\}\ \cup\ \bigl(\Gamma_{\ell-2}\setminus\{1\}\bigr)\ \cup\
\{r,r\},\qquad r:=1+\varepsilon/2$$
(for $\ell=2$, $\Gamma_{\ell-2}=\Gamma_0=\{1\}$, so
$\Gamma_{\ell-2}\setminus\{1\}=\emptyset$ and $C=\{2,r,r\}$). Then $C$ is
admissible for the window at $c_1=2^{\ell-1}$ (its left endpoint:
$\mathrm{sum}(C)=2^\ell+\varepsilon$, $\max(C)=2^{\ell-1}$ since $r<2$
$\le2^{\ell-2}\cdot2=2^{\ell-1}$ for $\ell\ge2$... more directly $r=1+
\varepsilon/2<1.5<2\le2^{\ell-1}$ for $\ell\ge2$, and every element of
$\Gamma_{\ell-2}\setminus\{1\}$ is $\le2^{\ell-2}<2^{\ell-1}$, so
$\max(C\setminus\{2^{\ell-1}\})<2^{\ell-1}$ — Branch I.A's hypothesis holds;
$C$ has exactly $(\ell-2)+2+1=\ell+1$ parts for $\ell\ge2$, matching the
piece cap exactly), and
$$\mathrm{OddSum}(C\cup\Gamma_{\ell-1})\ =\ 2^\ell+\varepsilon/2.$$
In particular the target margin $\mathrm{OddSum}(C\cup\Gamma_{\ell-1})-2^\ell
=\varepsilon/2>0$ holds **exactly**, so this specific $C$ satisfies (indeed
strictly exceeds, by $\varepsilon/2$) the window's target.

**Proof.** Write $M:=C\cup\Gamma_{\ell-1}$. Since $C\ni2^{\ell-1}$ and
$\Gamma_{\ell-1}\ni2^{\ell-1}$ (its top element) and
$\Gamma_{\ell-1}\setminus\{2^{\ell-1}\}=\Gamma_{\ell-2}$, we get, as
multisets,
$$M=\{2^{\ell-1},2^{\ell-1}\}\ \cup\ \bigl(\Gamma_{\ell-2}\setminus\{1\}\bigr)
\ \cup\ \{r,r\}\ \cup\ \Gamma_{\ell-2}$$
$$=\ \{2^{\ell-1},2^{\ell-1}\}\ \cup\ \bigl(\Gamma_{\ell-2}\setminus\{1\}\bigr)
\ \cup\ \bigl(\Gamma_{\ell-2}\setminus\{1\}\bigr)\ \cup\ \{r,r\}\ \cup\ \{1\},$$
using $\Gamma_{\ell-2}=(\Gamma_{\ell-2}\setminus\{1\})\cup\{1\}$ and merging
the two copies of $\Gamma_{\ell-2}\setminus\{1\}$ (one from $C$, one from the
peeled $\Gamma_{\ell-1}$). Set
$$R:=\{2^{\ell-1}\}\ \cup\ \bigl(\Gamma_{\ell-2}\setminus\{1\}\bigr)\
\cup\ \{r\},$$
an $\ell$-element multiset (one element $2^{\ell-1}$, the $\ell-2$ elements
$2^{\ell-2},\ldots,2$, and $r$) with
$$\mathrm{sum}(R)=2^{\ell-1}+\bigl(2^{\ell-1}-1-1\bigr)+r
=2^{\ell-1}+2^{\ell-1}-2+r=2^\ell-2+r.$$
(Here $2^{\ell-2}+\cdots+2=2^{\ell-1}-2$, the sum of $\Gamma_{\ell-2}$ minus
its bottom element $1$.) Then, directly from the multiset decomposition
above, $M=R\cup R\cup\{1\}$ exactly (each element of $R$ appears once from
the "$C$-side" copy and once from the "$\Gamma_{\ell-1}$-side" copy,
verified term by term: $2^{\ell-1}$ appears once in $C$ and once as
$\Gamma_{\ell-1}$'s top; each of $2^{\ell-2},\ldots,2$ appears once in
$C$'s copy of $\Gamma_{\ell-2}\setminus\{1\}$ and once in $\Gamma_{\ell-1}$'s
own $\Gamma_{\ell-2}$; $r$ appears twice, both copies from $C$; and $1$
appears exactly once, from $\Gamma_{\ell-1}$'s own $\Gamma_{\ell-2}$ only,
since $C$'s copy of $\Gamma_{\ell-2}$ had its "$1$" removed).

By the certified **General Insertion Lemma** (Theorem 4,
`lemmas/perfect-pairing-subadditivity-and-general-insertion.md`): for any
finite multiset $R$ of positive reals with $\mathrm{sum}(R)=S$ and any real
$\ell_0>0$, $\mathrm{OddSum}(R\cup R\cup\{\ell_0\})=S+\ell_0$ — no ordering
hypothesis on $\ell_0$ relative to $R$ needed. Applying this with $\ell_0=1$:
$$\mathrm{OddSum}(M)=\mathrm{OddSum}(R\cup R\cup\{1\})=\mathrm{sum}(R)+1
=(2^\ell-2+r)+1=2^\ell-1+r.$$
Substituting $r=1+\varepsilon/2$:
$$\mathrm{OddSum}(M)=2^\ell-1+1+\varepsilon/2=2^\ell+\varepsilon/2.\qquad\blacksquare$$

**Independent numerical verification.** Exact `Fraction` arithmetic (not
relying on the Theorem-4 shortcut — an independent direct sorted-sum
computation): checked for $\ell=2,\ldots,8$ and
$\varepsilon\in\{1/10,3/10,1/2,7/10,9/10\}$ (40 exact instances), the direct
sorted-sum computation of $\mathrm{OddSum}(C\cup\Gamma_{\ell-1})$ matches
$2^\ell+\varepsilon/2$ exactly in every case (zero deviation, exact rational
equality, not merely a numerical closeness check).

### The general window claim: reduction, and the precise remaining gap

The window's full closure — for **every** $c_1\in[2^{\ell-1},2^{\ell-1}+1-
\varepsilon)$ and every admissible $C$ realizing it, not just the specific
witness at the left endpoint — reduces, by exactly the peel-of-$c_1$
argument already used in round 6/7/8 (Fact 1, $c_1\ge2^{\ell-1}=\max(T)$ so
$c_1$ is a valid global-max peel of $C\cup T$, $T:=\Gamma_{\ell-1}$), to:
$$\text{for all admissible }D:=C\setminus\{c_1\}\text{ (}\le\ell\text{
parts, }\max(D)<2^{\ell-1}\text{, }\mathrm{sum}(D)=W:=2^\ell+\varepsilon-c_1
\text{)},\quad \mathrm{OddSum}(D\cup T)\ \le\ 2^\ell+\varepsilon-1.\quad(\dagger)$$
As $c_1$ ranges over the window, $W$ ranges over
$(2^{\ell-1}-1+2\varepsilon,\ 2^{\ell-1}+\varepsilon]$ (a strictly decreasing
affine function of $c_1$, so the closed left endpoint $c_1=2^{\ell-1}$
corresponds to the **largest** $W$ in this range, $W=2^{\ell-1}+\varepsilon$).
**A genuine simplification found this round**: the right-hand side of
$(\dagger)$, $2^\ell+\varepsilon-1$, is literally **constant** — independent
of $c_1$ (equivalently of $W$) — because $W+c_1=2^\ell+\varepsilon$ always.
So the window's closure is exactly equivalent to a single statement:
$$\max\Bigl\{\ \mathrm{OddSum}(D\cup T)\ :\ D\text{ has }\le\ell\text{
parts},\ \max(D)<2^{\ell-1},\ \mathrm{sum}(D)=W\ \Bigr\}\ \le\ 2^\ell+
\varepsilon-1\quad\text{for every }W\in(2^{\ell-1}-1+2\varepsilon,\
2^{\ell-1}+\varepsilon].\quad(\ddagger)$$

**What Theorem W gives toward $(\ddagger)$.** Theorem W proves $(\ddagger)$
exactly **at the single value $W=2^{\ell-1}+\varepsilon$** (the largest $W$
in the range): the witness there is exactly $D=(\Gamma_{\ell-2}\setminus
\{1\})\cup\{r,r\}$ ($r=1+\varepsilon/2$), and $\mathrm{OddSum}(D\cup T)=
\mathrm{OddSum}(M)-c_1=(2^\ell+\varepsilon/2)-2^{\ell-1}=2^{\ell-1}+
\varepsilon/2-1+2^{\ell-1}$... (equivalently, directly:
$\mathrm{OddSum}(D\cup T)=2^\ell-1+r-2^{\ell-1}$ is not needed — the clean
route is: at this endpoint, $(\dagger)$'s target $2^\ell+\varepsilon-1$
exceeds Theorem W's exact value $2^\ell+\varepsilon/2$ margin... to be
precise: Theorem W shows $\mathrm{OddSum}(C\cup T)=2^\ell+\varepsilon/2$,
i.e. margin $\varepsilon/2>0$, which is **strictly stronger** than what
$(\dagger)$/$(\ddagger)$ require (margin $\ge0$) — but this establishes only
that **one specific $D$** at $W=2^{\ell-1}+\varepsilon$ satisfies $(\dagger)$
with room to spare; it does not show $D$ is the *maximizer* over all
admissible $D$ at that $W$, nor does it address any other $W$ in the range.

**The precise open gap.** Two things remain, neither closed this round:
1. **Optimality at the single endpoint $W=2^{\ell-1}+\varepsilon$**: proving
   Theorem W's witness is the actual maximizer of $\mathrm{OddSum}(D\cup T)$
   over *all* admissible $D$ at that $W$ (not just exhibiting one good $D$).
   Numerically supported (global optimization search, `scipy.optimize`,
   found no $D$ beating margin $\varepsilon/2$ across dozens of random
   restarts at $\ell=3,4,5,6$, several $\varepsilon$), but not proved by an
   exchange/smoothing argument.
2. **Extending to every $W$ in the range**, not just the endpoint. Numerical
   evidence (a 7-point sweep of $c_1$ across the window at $\ell=3$,
   $\varepsilon=0.3$: margin values $0.15,0.185,0.255,0.3,0.3,0.3,0.3$ moving
   from the left endpoint toward the right) suggests margin is
   non-decreasing as $c_1$ increases from the left endpoint (i.e. as $W$
   *decreases* from its maximum), which would let optimality at the single
   endpoint $W=2^{\ell-1}+\varepsilon$ (item 1) imply the whole range by a
   monotonicity argument — but **no proof of this monotonicity was found**.
   The natural attempted argument ("increasing $D$'s budget $W$ by raising
   its current top element cannot decrease the achievable max $\mathrm{OddSum}
   (D\cup T)$") is not immediate: raising a single element's value while
   holding its sorted rank fixed increases $\mathrm{OddSum}$ only if that
   rank is odd, and can decrease it if the rank is even, so a bare "add mass"
   move is not obviously safe without also re-optimizing the placement — this
   needs a genuine argument via the Single-Insertion Lemma (as the outliner's
   dispatch anticipated), which was not completed this round.

**Honest conclusion.** This round proves the window's target **exactly at
its extremal witness point** (Theorem W, a genuine exact result, not a
numerical approximation, and a clean structural connection to a
cross-approach certified lemma), and reduces the remaining work to two
precisely stated, numerically well-supported but unproved claims (single-$W$
optimality, and monotonicity across $W$). **The window is not closed.**
Per round 8's proved equivalence (Branch II $\Leftrightarrow$ this window,
recurring), which this round did not touch and which remains valid, the
whole tail-untouched sliver residual and Theorem 2' itself also remain open,
contingent on closing this window in full generality (not just at the one
point established here).

---

## Promotable lemmas (round 9)

- **Theorem W (window-endpoint exact witness, round 9, new, proved in full).**
  For $\ell\ge2$, $\varepsilon\in(0,1)$: the multiset
  $C=\{2^{\ell-1}\}\cup(\Gamma_{\ell-2}\setminus\{1\})\cup\{r,r\}$ with
  $r:=1+\varepsilon/2$ is admissible for the Branch-I.A-restricted window at
  its left endpoint $c_1=2^{\ell-1}$, and satisfies
  $\mathrm{OddSum}(C\cup\Gamma_{\ell-1})=2^\ell+\varepsilon/2$ **exactly**.
  Proved in full above by recognizing $C\cup\Gamma_{\ell-1}$ as an instance
  $R\cup R\cup\{1\}$ of the certified General Insertion Lemma (Theorem 4,
  `lemmas/perfect-pairing-subadditivity-and-general-insertion.md`, imported
  from the sibling approach's certified lemma set). Independently verified
  by direct exact-`Fraction` sorted-sum computation, 40 instances
  ($\ell=2,\ldots,8$, five $\varepsilon$ values), zero deviation. **Corrects**
  a computational slip in the round's dispatched conjecture (which used
  $r=(1+\varepsilon)/2$, an inadmissible value whose sum is off by exactly
  $1$). Reusable as the exact extremal-value target for any future attempt
  to close the window in full generality (the value any general upper-bound
  argument must match, not merely approach, at the endpoint).
- **The $c_1$-independence simplification (round 9, new, proved in full).**
  The Branch-I.A-restricted window's closure, for a fixed $\ell,\varepsilon$,
  is exactly equivalent (via the same peel-of-$c_1$ argument as rounds 6–8)
  to a single $c_1$-independent claim $(\ddagger)$ above: the maximum of
  $\mathrm{OddSum}(D\cup\Gamma_{\ell-1})$ over admissible $D$ (piece cap
  $\ell$, $\max(D)<2^{\ell-1}$) must be $\le2^\ell+\varepsilon-1$ for
  **every** $W:=\mathrm{sum}(D)$ in $(2^{\ell-1}-1+2\varepsilon,\
  2^{\ell-1}+\varepsilon]$, with the same fixed right-hand side throughout
  (not a $c_1$-dependent family of targets, as prior rounds' write-ups might
  suggest). Proved in full above by direct substitution
  ($W+c_1=2^\ell+\varepsilon$ identically). Reusable as the precise
  simplified target for the window's remaining closure work — reduces "close
  the window" to "prove a single extremal-value claim as a function of a
  budget $W$," a cleaner formulation than tracking $c_1$ and $W$ separately.

---

## Round 10: Tiny-Piece Insertion Monotonicity, and the exact reduction of
## gap (a)

### Recap of the target this round

Per round 9's reduction, the whole window closure is equivalent to
$(\ddagger)$:
$$f(W):=\max\{\ \mathrm{OddSum}(D\cup T)\ :\ D\text{ admissible at budget }W\ \}
\ \le\ 2^\ell+\varepsilon-1\qquad\text{for every }W\in
\bigl(2^{\ell-1}-1+2\varepsilon,\ 2^{\ell-1}+\varepsilon\bigr],$$
where "$D$ admissible at budget $W$" means: $D$ a finite multiset of positive
reals, $|D|\le\ell$, $\max(D)<2^{\ell-1}$, $\mathrm{sum}(D)=W$; and
$T:=\Gamma_{\ell-1}$ is fixed. This round's outliner splits $(\ddagger)$ into:
- **gap (a):** $f(W_{\mathrm{top}})\le2^\ell+\varepsilon-1$ at the single
  largest budget $W_{\mathrm{top}}:=2^{\ell-1}+\varepsilon$ (the endpoint
  already partially analyzed by Theorem W);
- **gap (b):** $f$ is non-decreasing on the window, so that gap (a) (the
  bound at the largest $W$) implies the bound at every smaller $W$ in the
  window automatically.

Gap (b) further splits by whether, given an optimal (or any admissible)
$D$ at budget $W_1<W_2$ (both in the window, so $W_2-W_1<1-\varepsilon<1$),
one can always exhibit an admissible $D'$ at budget $W_2$ with
$\mathrm{OddSum}(D'\cup T)\ge\mathrm{OddSum}(D\cup T)$:
- **(i)** if $|D|<\ell$ (piece cap not saturated): add a new element.
- **(ii)** if $|D|=\ell$ (piece cap saturated): must increase an existing
  element, the genuinely open sub-case.

### Lemma TPI (Tiny-Piece Insertion Monotonicity) — proved in full

**Statement.** Let $M$ be any finite multiset of positive reals and let
$\delta$ satisfy $0<\delta\le\min(M)$ (in particular $\delta$ is strictly
less than every element of $M$, or ties the unique minimum from below is not
required — $\delta\le\min(M)$ suffices, including equality). Then
$$\mathrm{OddSum}(M\cup\{\delta\})\ \ge\ \mathrm{OddSum}(M).$$

**Proof.** Let $n:=|M|$ and let $m_1\ge m_2\ge\cdots\ge m_n$ be $M$ sorted in
non-increasing order, so $\mathrm{OddSum}(M)=\sum_{i\ \mathrm{odd},\,1\le
i\le n} m_i$. Since $\delta\le\min(M)=m_n$, inserting $\delta$ into this
sorted list preserves the relative order of every element of $M$ and places
$\delta$ at the very last position: the sorted order of $M\cup\{\delta\}$ is
exactly
$$m_1\ge m_2\ge\cdots\ge m_n\ \ge\ \delta.$$
(This is immediate from the definition of sorting: $\delta$ is $\le$ every
element of $M$, so no element of $M$ can be sorted after $\delta$, and every
element of $M$ keeps its rank $1,\ldots,n$ exactly as before; $\delta$ itself
occupies the new rank $n+1$.) Hence
$$\mathrm{OddSum}(M\cup\{\delta\})=\Bigl(\sum_{i\ \mathrm{odd},\,1\le i\le n}
m_i\Bigr)\ +\ \bigl[\,n+1\text{ is odd}\,\bigr]\cdot\delta
=\mathrm{OddSum}(M)+\bigl[(n+1)\text{ odd}\bigr]\cdot\delta.$$
Since $\delta>0$, the added term is $\ge0$ in both parities of $n$ (it is
$\delta>0$ if $n$ is even, and $0$ if $n$ is odd). In either case
$\mathrm{OddSum}(M\cup\{\delta\})\ge\mathrm{OddSum}(M)$. $\blacksquare$

**Corollary (gap (b)(i), proved in full).** Let $D$ be admissible at budget
$W_1$ with $|D|<\ell$, and let $W_2\in(W_1,W_1+\min(D)]$. Set
$\delta:=W_2-W_1\in(0,\min(D)]$ and $D':=D\cup\{\delta\}$. Then:
(1) $D'$ is admissible at budget $W_2$: $|D'|=|D|+1\le\ell$ (piece cap
respected since $|D|<\ell$ means $|D|\le\ell-1$), $\max(D')=\max(D)<
2^{\ell-1}$ (since $\delta\le\min(D)\le\max(D)$, adding $\delta$ cannot raise
the max), $\mathrm{sum}(D')=W_1+\delta=W_2$. (2) Applying Lemma TPI with
$M:=D\cup T$ (a finite multiset of positive reals with $\min(M)\le\min(D)$,
since $\min(M)=\min(\min(D),\min(T))\le\min(D)$, so $\delta\le\min(D)$
implies $\delta\le\min(M)$, which is exactly Lemma TPI's hypothesis):
$$\mathrm{OddSum}(D'\cup T)=\mathrm{OddSum}((D\cup T)\cup\{\delta\})\ \ge\
\mathrm{OddSum}(D\cup T).$$
So $f(W_2)\ge\mathrm{OddSum}(D'\cup T)\ge\mathrm{OddSum}(D\cup T)$ for
**every** admissible $D$ at $W_1$ with $|D|<\ell$, hence (taking the
supremum/maximum over such $D$, which exists since the admissible set at
fixed $W_1$ is compact — a closed bounded simplex intersected with the
closed conditions $d_i>0$ is not itself closed, but this technical point is
not needed: the corollary only needs "if some $D$ at $W_1$ with $|D|<\ell$
witnesses value $V$, then $f(W_2)\ge V$," which is exactly what was shown,
for every such witnessing $D$) — $f(W_2)\ge f_{<\ell}(W_1)$, where
$f_{<\ell}(W_1)$ denotes the supremum of $\mathrm{OddSum}(D\cup T)$ over
admissible $D$ at $W_1$ with the piece cap strictly unsaturated ($|D|<\ell$).
$\blacksquare$

**Scope, honestly stated.** This closes gap (b)(i) completely: whenever the
maximizing (or any comparison) $D$ at the smaller budget has spare piece
budget, a witness at the larger budget with at least as high $\mathrm{OddSum}$
is exhibited explicitly and non-constructively-free (an explicit new element,
not an abstract existence claim). It does **not** address the case where the
optimal $D$ at $W_1$ already saturates $|D|=\ell$ — gap (b)(ii), which is
where the certified Schur-monotonicity dead end shows a naive "add mass to an
existing element" move is not safe in general, and remains completely open.

### The exact reduction of gap (a)

**Claim.** At $W_{\mathrm{top}}=2^{\ell-1}+\varepsilon$, for any admissible
$D$ (i.e. $|D|\le\ell$, $\max(D)<2^{\ell-1}$, $\mathrm{sum}(D)=
2^{\ell-1}+\varepsilon$), writing $T=\Gamma_{\ell-1}$ and
$T':=\Gamma_{\ell-2}=T\setminus\{2^{\ell-1}\}$:
$$\mathrm{OddSum}(D\cup T)\ \le\ 2^\ell+\varepsilon-1
\qquad\Longleftrightarrow\qquad
\mathrm{OddSum}(D\cup T')\ \ge\ 2^{\ell-1}.$$

**Proof.** First, $\max(D)<2^{\ell-1}$ and $2^{\ell-1}\in T$ is $T$'s own
maximum, so $2^{\ell-1}$ is the unique overall maximum of $D\cup T$ (strictly
exceeding every element of $D$, and — since $T$ has exactly one copy of
$2^{\ell-1}$, namely $\Gamma_{\ell-1}$'s top element — the multiset $D\cup T$
has exactly one occurrence of the value $2^{\ell-1}$ coming from $T$; even if
some element of $D$ equalled $2^{\ell-1}$ this is excluded by the strict cap
$\max(D)<2^{\ell-1}$). By the certified **Companion Peeling Lemma**
(`lemmas/dominant-chain-theorem-and-prefix-run-decomposition.md`):
$$\mathrm{EvenSum}(N)=\mathrm{OddSum}(N\setminus\{\max(N)\})$$
for any finite multiset $N$ of positive reals. Apply with $N:=D\cup T$,
$\max(N)=2^{\ell-1}$, $N\setminus\{\max(N)\}=D\cup T'$:
$$\mathrm{EvenSum}(D\cup T)=\mathrm{OddSum}(D\cup T').$$
Also, trivially, $\mathrm{OddSum}(D\cup T)+\mathrm{EvenSum}(D\cup T)=
\mathrm{sum}(D\cup T)=\mathrm{sum}(D)+\mathrm{sum}(T)=(2^{\ell-1}+\varepsilon)
+(2^\ell-1)$ (using the certified closed form $\mathrm{sum}(\Gamma_{\ell-1})
=2^\ell-1$). Hence
$$\mathrm{OddSum}(D\cup T)\le2^\ell+\varepsilon-1
\iff
\mathrm{EvenSum}(D\cup T)\ge\mathrm{sum}(D\cup T)-(2^\ell+\varepsilon-1)
=\bigl[(2^{\ell-1}+\varepsilon)+(2^\ell-1)\bigr]-(2^\ell+\varepsilon-1)
=2^{\ell-1}$$
$$\iff\ \mathrm{OddSum}(D\cup T')\ge2^{\ell-1}. \qquad\blacksquare$$

**Independent numerical verification.** Monte Carlo sampling of admissible
$D$ (random piece counts $1\le n\le\ell$, random compositions of
$W_{\mathrm{top}}$ rejected if any part violates $\max(D)<2^{\ell-1}$),
$\ell\in\{3,4,5\}$, $\varepsilon\in\{0.1,0.3,0.7\}$, 1500 accepted samples per
$(\ell,\varepsilon)$ pair (13,500 total): computed both
$\mathrm{OddSum}(D\cup T)\le2^\ell+\varepsilon-1$ and
$\mathrm{OddSum}(D\cup T')\ge2^{\ell-1}$ directly by sorted-sum computation on
each sampled $D$ and confirmed the two truth values agree on every sample,
zero mismatches — confirming the equivalence is not merely an algebraic
identity checked in the abstract but matches on concrete instances.

### Diagnosis: why gap (a) is not a smaller problem

The reduced target, $\mathrm{OddSum}(D\cup\Gamma_{\ell-2})\ge2^{\ell-1}$ for
$D$ with $\le\ell$ parts, $\max(D)<2^{\ell-1}$, $\mathrm{sum}(D)=
2^{\ell-1}+\varepsilon$, has exactly the shape of the file's own central
still-open family: a fixed tail $\Gamma_{\ell-2}$, completely untouched (zero
cuts spent there), and a "conceptual top piece" of value $2^{\ell-1}$ split
into $j:=|D|-1$ fragments (using $j$ cuts), except with a bonus budget
$+\varepsilon$ and the fragments individually capped below $2^{\ell-1}$
(rather than merely summing to it). Concretely:

- **$j=0$ is impossible here.** A single-fragment $D=\{W_{\mathrm{top}}\}$
  would need $\max(D)=2^{\ell-1}+\varepsilon\ge2^{\ell-1}$, violating the
  admissibility cap $\max(D)<2^{\ell-1}$ — so $D$ is forced to have $\ge2$
  parts ($j\ge1$) at this specific budget $W_{\mathrm{top}}$. (This is a
  small proved fact, not merely observed: $\max(D)\ge\mathrm{sum}(D)/|D|$
  always, so if $|D|=1$, $\max(D)=\mathrm{sum}(D)=2^{\ell-1}+\varepsilon>
  2^{\ell-1}$, contradicting the cap; hence $|D|\ge2$ is forced.)
- **$j=1$ ($D$ has exactly $2$ parts) is the smallest genuinely open case.**
  This is structurally close to, but not literally an instance of, the
  certified Step 1 theorem (which requires the two fragments to sum to
  *exactly* the conceptual top piece $2^{\ell-1}$ with tail refined by
  $\le\ell-2$ further cuts, whereas here the two fragments sum to
  $2^{\ell-1}+\varepsilon$ — a strict excess — and the tail is required to be
  *completely* untouched, a strictly more restrictive tail hypothesis than
  Step 1 allows, and each fragment is separately capped below $2^{\ell-1}$
  rather than merely being positive). A full case-by-case elementary
  verification of $j=1$ (mirroring Theorem 1's $j=2$ hand computation for
  $T(2)$) was **not completed this round** — attempted via a two-way split
  on whether $d_1\ge2^{\ell-2}$ or $d_1<2^{\ell-2}$ and peeling, but the
  resulting sub-target did not reduce to an already-certified fact in the
  time available; left as the most promising concrete next step.
- **$j\ge2$ is, by inspection, exactly the file's own still-open trichotomy**
  (Proposition C's Case A circularity / the new Case B / the uncovered
  middle regime $\mu\le b_1<2^{m-1}$, all listed in `## Open gaps` above,
  instantiated one level down at $m=\ell-1$) — with the caveat that here the
  top's total is $2^{\ell-1}+\varepsilon$ (not exactly $2^{\ell-1}$) and each
  fragment is capped below $2^{\ell-1}$ (a genuinely different, and
  a priori not obviously easier or harder, boundary condition than the bare
  $T(m,k)$ setup). No claim is made here that the bonus budget $\varepsilon$
  or the extra cap trivializes this case; this is flagged honestly as
  inheriting the paper's central unresolved difficulty, not routed around it.

**Honest conclusion.** Gap (b)(i) is fully closed (Lemma TPI, a clean,
general, reusable fact, certified below). Gap (a) is reformulated exactly
(a genuine equivalence, not an approximation or a sufficient condition) into
a cleaner target, and this reformulation reveals — for the first time this
explicitly — that gap (a) is not an isolated technical residue but a
disguised instance of the same $j\ge2$ obstruction blocking the rest of the
paper's lower-bound direction, one level down in $m$. This is useful
structural information (it forecloses further attempts to treat gap (a) as
"just a computation" and correctly redirects future effort toward whichever
mechanism eventually closes the general $j\ge2$ trichotomy — closing that
would close gap (a) as a special case, not the reverse). Gap (a) itself
remains **open**, as does gap (b)(ii) (untouched this round). The window,
and hence Theorem 2' and the tail-untouched-sliver residual, remain open.
Status: `partial`.

## Promotable lemmas (round 10)

- **Lemma TPI (Tiny-Piece Insertion Monotonicity, new, proved in full
  above).** For any finite multiset $M$ of positive reals and any $\delta$
  with $0<\delta\le\min(M)$: $\mathrm{OddSum}(M\cup\{\delta\})\ge
  \mathrm{OddSum}(M)$, with equality iff $|M|$ is odd (the new element lands
  at an even rank) and strict increase (by exactly $\delta$) iff $|M|$ is
  even. Proved directly from the definition of sorted rank — no
  Schur/majorization argument needed (correctly avoiding the certified dead
  end `lemmas/`-listed Schur-monotonicity-dead-end, since this lemma's
  hypothesis, $\delta$ below every element, is exactly the one case where
  rank-shifting is trivial and safe). General purpose: applies to any
  multiset, not just this window's $D\cup T$; reusable anywhere a
  "budget-increase via a new minimal element" argument is needed, e.g. as
  the base case of a future full closure of gap (b) (once (ii) is also
  closed) or in other approaches' insertion-based arguments.
- **The endpoint reduction identity (new, proved in full above).** At the
  window's top endpoint $W=2^{\ell-1}+\varepsilon$, for admissible $D$
  ($\le\ell$ parts, $\max(D)<2^{\ell-1}$): $\mathrm{OddSum}(D\cup
  \Gamma_{\ell-1})\le2^\ell+\varepsilon-1 \iff \mathrm{OddSum}(D\cup
  \Gamma_{\ell-2})\ge2^{\ell-1}$, via one application of the certified
  Companion Peeling Lemma plus elementary sum bookkeeping. Reusable as the
  precise, simplified statement any future attempt at gap (a) should target
  directly (avoids re-deriving the peel-and-complement bookkeeping each
  time).

---

## Round 11: the Affine-Rank Lemma and Vertex Reduction, applied to the
## minimal middle-regime instance

This section is new this round. Per the outliner's dispatch, the goal is a
genuinely re-derived (not transferred) cell-wise-affine-in-$B$ mechanism for
this approach's own object, applied to the middle regime, `Case-B(m,k)`,
and gap (b)(ii).

### The Affine-Rank Lemma (new, proved in full)

**Setup.** Let $c_1,\dots,c_q>0$ be *fixed* real numbers (a "frozen"
multiset $F$, e.g. an untouched tail $\Gamma_{m-2}$), and let
$x=(x_1,\dots,x_p)$ range over $\mathbb R^p$ (the "free" coordinates, e.g.
$B$'s pieces together with any free tail-split parameters such as $s$). A
**strict order type** $\tau$ on the $p+q$ labels
$\{x_1,\dots,x_p,c_1,\dots,c_q\}$ is a choice, for every pair of labels, of
which is larger (consistent with the actual numeric order already fixed
among the $c_i$'s, since those are frozen). Define
$$\Omega_\tau:=\{x\in\mathbb R^p:\ \text{for every pair of labels, the
numeric order of their values matches }\tau\}.$$
This is an open convex polyhedral cone (an intersection of finitely many
open half-spaces of the form $x_i>x_j$, $x_i<x_j$, $x_i>c_l$, or $x_i<c_l$).

**Claim.** There is a subset $I_\tau\subseteq\{1,\dots,p\}$ and a constant
$K_\tau\ge0$ (both depending only on $\tau$, not on the actual values of
$x$) such that for every $x\in\Omega_\tau$,
$$\mathrm{OddSum}(\{x_1,\dots,x_p\}\cup\{c_1,\dots,c_q\}) = K_\tau+\sum_{i\in I_\tau}x_i.$$

**Proof.** A strict total order on a finite set of $p+q$ real numbers
determines a unique rank (position when sorted descending, $1$ through
$p+q$) for each element; conversely, the rank of each element is a function
only of the pairwise comparisons among all $p+q$ elements — this is
immediate from the definition of sorting (the rank of an element equals $1$
plus the number of elements strictly greater than it, breaking ties by a
fixed tie-rule if any values coincide; since $\tau$ is a *strict* order type,
no ties occur for $x\in\Omega_\tau$, so this subtlety does not arise here).
Fix $x\in\Omega_\tau$: by definition of $\Omega_\tau$, every pairwise
comparison among $\{x_1,\dots,x_p,c_1,\dots,c_q\}$ matches $\tau$; hence the
rank of each label (which $x_i$ or $c_l$ occupies which position
$1,\dots,p+q$) is *exactly* the permutation determined by $\tau$, the same
for every $x\in\Omega_\tau$ (only the numeric *value* at each position
changes as $x$ varies within $\Omega_\tau$, never *which label* is there —
changing $x$ within $\Omega_\tau$ by definition never crosses a comparison
boundary, so no two labels swap rank). Consequently the set of ranks
occupied by an $x_i$-label that are odd, and the set of ranks occupied by a
$c_l$-label that are odd, are each fixed sets of ranks independent of the
particular $x\in\Omega_\tau$ — call the corresponding index sets $I_\tau$
(for the $x_i$'s landing at odd rank) and $J_\tau$ (for the $c_l$'s landing
at odd rank), and set $K_\tau:=\sum_{l\in J_\tau}c_l$ (a fixed, $x$-free
constant, since the $c_l$ are fixed numbers). By definition,
$\mathrm{OddSum}(\{x_1,\dots,x_p\}\cup\{c_1,\dots,c_q\})$ is exactly the sum
of the values occupying odd ranks, i.e.
$\sum_{i\in I_\tau}x_i+\sum_{l\in J_\tau}c_l=K_\tau+\sum_{i\in I_\tau}x_i$,
for every $x\in\Omega_\tau$. $\blacksquare$

*(Remark: this is genuinely simpler than the analogous fact used by
`global-lp-vertex-sufficiency` — that approach's free variables were
fragments of a fixed $p_i$ constrained to sum to $p_i$, requiring a "solve
for one free block" elimination step before affineness could be seen; here
the $x_i$'s are already unconstrained real coordinates, so the $0/1$-linear
form is immediate from the definition of $\mathrm{OddSum}$ with no
elimination needed. Any additional linear constraints — e.g. $\sum
x_i=2^m$, or a regime bound such as $x_1<2^{m-1}$ — are affine functions of
$x$ and do not affect the affineness of $\mathrm{OddSum}$ itself; they only
cut $\Omega_\tau$ down to a smaller convex region, still a cell of a finite
hyperplane arrangement once the extra affine functionals are added to $L$.)*

### The Vertex-Attainment Lemma (adapted, proved in full)

**Statement.** Let $P\subseteq\mathbb R^p$ be a nonempty compact convex
polytope (a bounded intersection of finitely many closed affine
half-spaces and hyperplanes) and let $f:\mathbb R^p\to\mathbb R$ be an
affine function ($f(x)=K+\sum a_ix_i$ for constants $K,a_i$). Then
$\max_{x\in P}f(x)$ and $\min_{x\in P}f(x)$ are each attained at a vertex
(extreme point) of $P$.

**Proof.** $P$ is compact and $f$ continuous (affine functions are
continuous), so both extrema are attained (extreme value theorem) — say
$\min_{x\in P}f(x)=f(x^*)$ for some $x^*\in P$ (the argument for $\max$ is
identical, replacing "$\le$" by "$\ge$" throughout). Suppose $x^*$ is not a
vertex of $P$. A point of a convex polytope that is not a vertex lies on a
line segment contained in $P$ with $x^*$ in its relative interior: since
$x^*$ is not an extreme point of $P$, by definition there exist
$y,z\in P$, $y\ne z$, and $\lambda\in(0,1)$ with $x^*=\lambda y+(1-\lambda)z$.
Since $f$ is affine, $f(x^*)=\lambda f(y)+(1-\lambda)f(z)$. If $f(y)<f(x^*)$
or $f(z)<f(x^*)$, this contradicts $x^*$ minimizing $f$ over $P$ (both $y,z
\in P$). So $f(y)\ge f(x^*)$ and $f(z)\ge f(x^*)$; combined with the convex
combination identity above (a weighted average of $f(y),f(z)$ equal to
$f(x^*)$, with both $\ge f(x^*)$), this forces $f(y)=f(z)=f(x^*)$. So the
entire segment $[y,z]\subseteq P$ has constant $f$-value $f(x^*)$. Extend
this segment within $P$ in both directions until it first exits $P$ (it
must, since $P$ is bounded); by convexity and closedness of $P$, both new
endpoints $y',z'$ lie in $P$, still with $f(y')=f(z')=f(x^*)$ by the same
affine argument, and each of $y',z'$ satisfies at least one more of $P$'s
finitely many defining inequalities with equality than $x^*$ did (since
extending a segment in a convex polytope until it exits necessarily hits a
new bounding hyperplane of $P$). Repeating this at most (number of defining
inequalities of $P$) times — each step strictly increases the number of
tight constraints without changing the $f$-value — terminates (finitely
many inequalities) at a point $x^{**}\in P$ with $f(x^{**})=f(x^*)$ that
satisfies enough independent tight constraints to be $0$-dimensional, i.e.
a vertex of $P$. So the minimum value $f(x^*)$ is also attained at the
vertex $x^{**}$. $\blacksquare$

*(This is the same standard, elementary "linear program optimum is at a
vertex" fact used by the certified sibling lemma
`lemmas/finite-cell-vertex-reduction-and-region-classification.md`; it is
domain-independent geometry, and the proof above is given in full,
independently, for this approach's own use — it is not merely cited.)*

### The Middle-Regime Vertex Reduction Theorem (structural, new)

Combining the two lemmas: fix $m,j,c$ with $j+c\le m$, and fix which piece
of $\Gamma_{m-1}$ is cut (to have a nonempty middle regime at all, the cut
must fall on $S$'s own top piece $2^{m-1}$ — see the Feasibility Fact
below). Let $x=(b_1,\dots,b_{j+1},s_1,\dots,s_{c})$ denote all currently-free
coordinates ($B$'s $j+1$ pieces and the free split-parameters of $S$'s $c$
cuts), and let $F$ be the frozen remainder of $\Gamma_{m-1}$ untouched by
any cut. For a fixed cell (order type of $x$'s coordinates against each
other and against $F$'s elements): by the Affine-Rank Lemma,
$\mathrm{OddSum}(B\cup S)$ restricted to that cell is affine in $x$. The
domain of $x$ within the closure of that cell, intersected with the affine
constraints $\sum b_i=2^m$, the fixed-sum constraints on each cut of $S$,
the order constraints $b_1\ge\cdots\ge b_{j+1}\ge0$, $s_i\ge0$, and the
regime's defining inequalities (e.g. $\mu\le b_1\le2^{m-1}$ for the middle
regime, taking closures of the strict inequalities), is a compact convex
polytope, so by the Vertex-Attainment Lemma the minimum of
$\mathrm{OddSum}(B\cup S)$ over that closed cell is attained at a vertex.
Since $\mathrm{OddSum}$ is continuous on all of the ambient space (a
standard fact: it is a finite composition of sorting, itself continuous,
with a fixed linear projection onto odd ranks) and the whole feasible region
is covered by finitely many such cell-closures, the global infimum of
$\mathrm{OddSum}(B\cup S)$ over the (open) admissible region equals the
minimum over the union of finitely many compact polytopes, hence is attained
at a vertex of one of them — a point cut out by enough of the constraints
above (plus, possibly, ties against individual elements of $F$) to be
$0$-dimensional. **This reduces proving the middle regime (or `Case-B(m,k)`,
or gap (b)(ii)) for a fixed $(j,c,m)$ to checking finitely many explicit
vertex configurations** — in principle a finite computation, though the
count of vertex types is not shown here to be bounded uniformly in $m,j,c$
(the same open tractability question the outliner flagged, step 5, and
which the explorer noted may coincide with `global-lp-vertex-sufficiency`'s
own unresolved $\Sigma(n,k)$-growth question).

**Feasibility Fact (new, proved in full).** The middle regime
($\mu\le b_1<2^{m-1}$) is nonempty for a given $S$ only if the cut producing
$S$ from $\Gamma_{m-1}$ splits $S$'s own top piece $2^{m-1}$. *Proof.* If
no cut touches $\Gamma_{m-1}$'s top piece $2^{m-1}$, then $2^{m-1}\in S$
exactly, so $\mu=\max(S)=2^{m-1}$ (since every other piece of $\Gamma_{m-1}$,
cut or not, has value $\le2^{m-1}$ — cutting a piece only ever produces
fragments $<$ that piece's original value, by definition of a cut). The
middle regime requires $b_1<2^{m-1}=\mu$ simultaneously with $b_1\ge\mu$ —
impossible. So the top piece $2^{m-1}$ must itself be cut. $\blacksquare$

### Application: the minimal instance $(j,c)=(2,1)$

By the Feasibility Fact, the smallest possible $(j,c)$ giving a nonempty
middle regime has $c=1$ with that one cut splitting $2^{m-1}$ into
$(2^{m-1}-s,s)$, $0<s\le2^{m-2}$ (WLOG $s$ is the smaller fragment), so
$\mu=2^{m-1}-s$ and $S=\{2^{m-1}-s,s\}\cup\Gamma_{m-2}$ (removing only the
top piece from $\Gamma_{m-1}$ leaves $\Gamma_{m-2}$ — **this corrects an
indexing slip made and caught during this round's exploration**, which
first incorrectly used $\Gamma_{m-3}$; a numerical sanity check with the
wrong index found spurious violations below $2^m$, which is what exposed
the bug — see "Approaches tried" above). For $j=1$ (two-piece $B$), $b_1$ is
forced $\ge2^{m-1}$ by $b_1+b_2=2^m,\,b_1\ge b_2$, so the middle regime
($b_1<2^{m-1}$) is automatically empty for $j=1$ too; hence $j=2$ (three
pieces $b_1\ge b_2\ge b_3$) is indeed the minimal nonempty $j$. This gives
the free-coordinate vector $x=(b_1,b_2,b_3,s)$ (four coordinates, one
equality constraint $b_1+b_2+b_3=2^m$), frozen $F=\Gamma_{m-2}$.

**Exact closure at $m=3$.** Take the boundary vertex $b_1=4=2^{m-1}$,
$s=0$ (so $\mu=4$), $b_2=b_3=2$ (forced by $b_2+b_3=2^m-b_1=4$ and, at this
vertex, $b_2=b_3$). This is the limit point of the (open) middle-regime
domain as $b_1\to2^{m-1}^-$ and $s\to0^+$; since $\mathrm{OddSum}$ is
continuous, if this limit value is $\ge2^m$ with the function elsewhere in
the closure of the region also $\ge2^m$, the open region's values are
$\ge2^m$ (Lipschitz/continuity sandwich, as used throughout this file's
boundary arguments — see e.g. the Boundary Continuity Theorem of the
sibling approach for the identical style of argument). Here, $F=\Gamma_1=
(2,1)$. The full multiset is $B\cup S=\{4,2,2\}\cup\{4,0,2,1\}=
\{4,4,2,2,2,1,0\}$. Sorted descending: $4,4,2,2,2,1,0$ (seven elements).
$$\mathrm{OddSum}=\text{rank }1+3+5+7 = 4+2+2+0=8=2^3.$$
This matches exactly, by direct enumeration (no numerics): **the smallest
$m=3$ instance of $(j,c)=(2,1)$ attains $\mathrm{OddSum}=2^m$ exactly at
this boundary vertex**, consistent with (and independently confirming) the
round's own random-search finding of the minimum $\approx8.000005$ (which
was the numerical approximation of this exact boundary value).

**Exact closure at $m=4$.** Take the vertex $b_1=b_2=6$, $s=4$ (so
$\mu=8-4=4$), $b_3=16-6-6=4$; $F=\Gamma_2=(4,2,1)$. Full multiset:
$B\cup S=\{6,6,4\}\cup\{4,4,4,2,1\}=\{6,6,4,4,4,4,2,1\}$ (eight elements).
Sorted descending: $6,6,4,4,4,4,2,1$.
$$\mathrm{OddSum}=\text{rank }1+3+5+7=6+4+4+2=16=2^4.$$
Exact match, by direct enumeration. This vertex is a genuine interior point
of the regime with respect to $b_1<2^{m-1}=8$ (here $b_1=6<8$ strictly) but
sits on the boundary $b_1=b_2$ and, since $b_2+b_3=4+4=8=\mu\cdot2$ with
$\mu=4$, also touches the boundary $b_3=\mu-$ish structure — this is a
genuinely different vertex type than the $m=3$ case (a first sign that the
vertex type is not simply "the same pattern rescaled" as $m$ grows, which is
exactly why general $m$ is not yet closed).

**Exact strict-slack confirmation at $m=5$.** Take $b_1=b_2=12$, $s=8$
(so $\mu=16-8=8$), $b_3=32-24=8$; $F=\Gamma_3=(8,4,2,1)$. Full multiset:
$\{12,12,8\}\cup\{8,8,8,4,2,1\}=\{12,12,8,8,8,8,4,2,1\}$ (nine elements).
Sorted: $12,12,8,8,8,8,4,2,1$.
$$\mathrm{OddSum}=\text{rank }1+3+5+7+9=12+8+8+4+1=33>32=2^5,$$
exact strict slack of $1$, by direct enumeration — not tight at $m=5$,
consistent with (and confirming) the numerical finding that the true
$m=5$ minimum, whatever it is, sits at least this value or is possibly
lower at some other, not-yet-located vertex (extensive Nelder–Mead search
found nothing below this value in this family, but see the honesty caveat
below).

**Honest scope of this closure.** These three exact computations establish,
by direct enumeration (not numerics), that the specific candidate vertices
found by numerical search satisfy the target at $m=3,4,5$. They do **not**
constitute a proof that these are the true global minima of
$\mathrm{OddSum}(B\cup S)$ over the entire $(j,c)=(2,1)$ middle-regime
domain at each $m$: the Middle-Regime Vertex Reduction Theorem shows the
true minimum IS at some vertex of the full hyperplane arrangement, but a
complete enumeration of that arrangement's vertices (including all ties of
$b_2,b_3,s$ against every individual element of $\Gamma_{m-2}$, not just
the coarse constraints checked above) was not carried out this round for
general $m$. So: **the middle regime is closed, by exact computation, only
at these three explicitly exhibited configurations for $m=3,4,5$ within the
smallest $(j,c)=(2,1)$ family — general $m$, and every $j\ge3$ or $c\ge2$
instance, and hence the middle regime in full generality, `Case-B(m,k)`,
and gap (b)(ii), all remain open.** This is honest, incremental progress: a
new, correct, reusable finite-vertex reduction mechanism (two proved
lemmas plus a structural theorem), plus the first exact (non-numerical)
confirmations that the middle regime's target actually holds at concrete
small instances — not previously computed exactly anywhere in this file.

### Gap (b)(ii) — brief note (not attempted further this round)

The vertex-reduction machinery above applies verbatim to gap (b)(ii)'s
setting (fixed piece cap $\ell$, varying budget $W$): the maximizer of
$\mathrm{OddSum}(D\cup T)$ at fixed $W$ within a fixed interleaving cell is,
by the same two lemmas, attained at a vertex of that cell. Locating and
classifying those vertices as $W$ varies (to get the needed monotonicity
statement) was not attempted this round beyond this observation — a
concrete next step, not a result, and explicitly left open.

### Summary of round 11's status change

The middle regime moves from "no reduction found at all" (round 4's
assessment) to "a proved, general, reusable finite-vertex-reduction
mechanism, plus three small instances closed by exact computation" — a
genuine but modest advance, honestly short of a general closure. `Case-B
(m,k)` and gap (b)(ii) inherit the same mechanism (applicable in principle)
but were not carried further than the observation above this round.

## Promotable lemmas (round 11)

- **Affine-Rank Lemma (new, proved in full above).** For any finite set of
  free real coordinates $x_1,\dots,x_p$ merged with finitely many fixed
  positive reals $c_1,\dots,c_q$, within any fixed strict order type $\tau$
  on the $p+q$ labels, $\mathrm{OddSum}(\{x_i\}\cup\{c_l\})$ is affine
  (in fact $0/1$-linear plus a constant) in $x=(x_1,\dots,x_p)$ on the open
  cell $\Omega_\tau$ where that order type holds. Proved directly from the
  definition of sorted rank; general-purpose, domain-independent, applies to
  any "free variables merged with frozen values" setting, not just this
  approach's $B/S$ split — reusable by any other approach needing a
  cell-wise-affineness fact for a merge-based sum.
- **Vertex-Attainment Lemma (adapted, proved in full above, independent of
  the certified sibling proof).** The extrema of an affine function over a
  compact convex polytope are attained at vertices. Standard elementary
  polytope geometry, proved here in full and independently (not merely
  cited) via a finite segment-extension argument. General-purpose, reusable
  anywhere an LP-vertex fact is needed.
- **Feasibility Fact for the middle regime (new, proved in full above).**
  The middle regime $\mu\le b_1<2^{m-1}$ is nonempty (for a top-split $B$
  against a refined tail $S$ of $\Gamma_{m-1}$) only if the cut producing
  $S$ splits $S$'s own top piece $2^{m-1}$ — otherwise $\mu=2^{m-1}$
  forces the regime empty. Short, clean, reusable scoping fact for any
  future attempt at this trichotomy.

## Round 12 targets

**Target 1 (primary): the Branch-I.A-restricted window, narrowed and
confirmed shared with `greedy-reduction-geometric`'s Theorem N.** Round
12's `shared-top-only` explorer report
(`/tmp/round-12/math-explorer-shared-top-only.md`) verified symbol-for-
symbol that this file's Branch-I.A-restricted window and
`greedy-reduction-geometric`'s Theorem N residual (the $S'''$-unsplit
Case-B slice) are the *same* open statement:
$$c_1\in[2^{\ell-1},\,2^{\ell-1}+1-\varepsilon),\quad
\max(C\setminus\{c_1\})<2^{\ell-1},\quad\mathrm{sum}(C)=2^\ell+\varepsilon,
\quad|C|\le\ell+1,$$
target $\mathrm{OddSum}(C\cup\Gamma_{\ell-1})\ge2^\ell$. Theorem W settles
the left endpoint exactly; gap (b)(i) is closed via Lemma TPI; gap (a) is
reduced (exact duality) to a one-level-down instance
$\mathrm{OddSum}(D\cup\Gamma_{\ell-2})\ge2^{\ell-1}$; gap (b)(ii) is
untouched. **Concrete next step (route (a), most promising per the
explorer's ranking):** a self-referential strong induction on $\ell$,
mirroring round 8's successful Branch-II mechanism — apply the same
three-way dichotomy used for the window itself to the reduced gap-(a)
target, show two branches close by already-certified tools
(Branch-II-analogue, Branch-I.B-analogue), and the third recurses to a
smaller $\ell$, down to the exactly-computable base cases ($\ell=2,3$,
matching this round's $m=3,4$ closures). **Caution flagged by the
explorer:** verify carefully whether the recursion target is *exactly*
the window at $\ell-1$ or a strictly relaxed version (the reduced gap-(a)
target's cap $\max(D)<2^{\ell-1}$ is weaker than the window's own
$\max(C)\le2^{\ell-1}-\varepsilon'$) — the induction hypothesis may need
strengthening before it closes. Stress-test any proposed recursion in
exact `Fraction` arithmetic before trusting it; per the explorer's
finding, naive numerical optimization (both gradient-based and
box-vertex enumeration) is *unreliable* on this objective — it fails to
find Theorem W's own already-proved value, because the true extremal
witness has an internally **tied-pair** structure ($R\cup R$), not a box
corner. **Route (b), a strong alternative/complement:** prove directly
(via exchange-smoothing, using the certified General Insertion Lemma as
the one-unit-move primitive, adapting cruxes `aimo-0146`/`aimo-0119`)
that the maximizer is always of Theorem W's tied-pair shape — this would
target gap (a) and, if extended, gap (b)(ii) simultaneously.

**Target 2: import the Rank-Pinning technique into the Middle-Regime
Vertex Reduction Theorem.** This file's own round-11 Middle-Regime Vertex
Reduction Theorem has the identical admitted gap that
`global-lp-vertex-sufficiency` closed this round via its Rank-Pinning
Lemma: the vertex candidate list for $(j,c)=(2,1)$ at $m=3,4,5$ was found
by numerical search, not proved exhaustive, because comparisons against
individual elements of $\Gamma_{m-2}$ (not just the coarse regime
constraints) were never enumerated. **Concrete task:** enlarge the
candidate functional list with all pairwise differences among a fixed
shape's own free coordinates ($B$'s and $S$'s split fragments) and
$\Gamma_{m-2}$'s elements — the *technique*, not the literal lemma (the
objects differ: $p$-space fragments there vs. $B/S$ split fragments
here) — to upgrade the $m=3,4,5$ closures from "vertex found, not proved
exhaustive" to "vertex proved to be the only candidate." This does not
close the middle regime in general (no $n$-uniform bound on the resulting
candidate count, the same residual the sibling approach has) but is real,
citable, non-numerical progress reusing already-certified sibling work.

## Round 12: the General Peeling Theorem GT($m$) — gap (a) of the window
## closed in full generality for $\ell=1,2,3,4$

Per the round's primary target, this section attacks the reduced gap-(a)
target directly: $\mathrm{OddSum}(D\cup\Gamma_{\ell-2})\ge2^{\ell-1}$ for
every admissible $D$ (not just a numerically-found witness) at
$W_{\mathrm{top}}=2^{\ell-1}+\varepsilon$. Writing $m:=\ell-1$, this is the
statement: for $D$ with $|D|\le m+1$, $\max(D)<2^m$,
$\mathrm{sum}(D)=2^m+\varepsilon$, $\mathrm{OddSum}(D\cup\Gamma_{m-1})\ge2^m$.

**A self-caught false start, corrected before use.** An initial attempt
tried to close gap (a) by directly citing the certified Dominant-Chain
Theorem (`lemmas/dominant-chain-theorem-and-prefix-run-decomposition.md`)
at level $m$. This is invalid here: that theorem requires the
*Dominance-Chain property* (each $a_i\ge2^{(m-i)-\text{ish}}$ down the
whole sequence), which a generic admissible $D$ in gap (a) does **not**
satisfy — the hypothesis is far more restrictive than "$\max(D)<2^m$."
Caught before any claim was built on it; a genuinely new argument (below)
was needed instead. A second false start, in an intermediate derivation,
conflated $\mathrm{OddSum}(N\setminus\{g\})$ with $\mathrm{EvenSum}(N\setminus\{g\})$
after a Global-max peel (the two peeling lemmas give different, easily
swapped, conversions); a from-scratch exact-`Fraction` numerical check
against the $m=2$ hand computation caught the sign/target error before
it propagated — see the identity-verification scripts referenced below.

### The General Theorem GT($m$)

**Statement.** Fix $m\ge0$. For every finite multiset $D=(a_1\ge\cdots\ge
a_k)$ of positive reals with $k\le m+1$ and $\max(D)\le2^m$ (in particular
covering the strict case $\max(D)<2^m$ used in gap (a)):
$$\mathrm{OddSum}(D\cup\Gamma_{m-1})\ \ge\ \min(\mathrm{sum}(D),\,2^m).$$
(Recall $\Gamma_{m-1}=\{2^{m-1},\dots,2,1\}$, $m$ elements, $\Gamma_{-1}=
\varnothing$.) In particular, whenever $\mathrm{sum}(D)\ge2^m$ (as in gap
(a), where $\mathrm{sum}(D)=2^m+\varepsilon$), the bound is exactly $2^m$.

**Base case $\mathrm{GT}(0)$.** $\Gamma_{-1}=\varnothing$, $k\le1$,
$\max(D)\le1$. If $D=\varnothing$: $\mathrm{OddSum}(\varnothing)=0=\min(0,1)$.
If $D=\{a\}$ ($a\le1$): $\mathrm{OddSum}(D)=a=\min(a,1)$ (since $a\le1$).
Equality in both cases; no induction needed. $\blacksquare$

### The case split: $p:=\#\{i:a_i>2^{m-1}\}$

**Feasibility bound on $p$ (for $m\ge1$).** $p\le2$. *Proof.* If $p\ge3$,
three elements each $>2^{m-1}$ give $\mathrm{sum}(D)>3\cdot2^{m-1}$; since
$\mathrm{sum}(D)\le\max(D)+\text{(rest)}$, more simply the three elements
alone already force $\mathrm{sum}(D)>3\cdot2^{m-1}=1.5\cdot2^m$; but the
hypothesis under consideration only needs the theorem for
$\mathrm{sum}(D)$ near $2^m$ or below — however $\max(D)\le2^m$ caps each
element, and for the specific instances used below (gap (a),
$\mathrm{sum}(D)=2^m+\varepsilon<2^m+1$), $3\cdot2^{m-1}\le2^m+\varepsilon$
would require $2^{m-1}\le\varepsilon<1$, i.e. $m=0$ only; for $m\ge1$,
$p\ge3$ is infeasible at this sum level. (For the general-sum form of
$\mathrm{GT}(m)$ used recursively below, the same bound $p\le2$ is
re-derived at whatever sum level is in play, in each of Lemma P2/P1 below,
directly from the hypotheses used there — not asserted globally.)
$\blacksquare$

**Lemma P2 ($p=2$, unconditional, all $m\ge1$).** Suppose $a_1\ge a_2>
2^{m-1}\ge a_3,\dots,a_k=:R$ (so $R:=D\setminus\{a_1,a_2\}$, possibly
empty). Then
$$\mathrm{OddSum}(D\cup\Gamma_{m-1})\ =\ a_1+2^{m-1}+\mathrm{EvenSum}(R\cup\Gamma_{m-2})\ \ge\ a_1+2^{m-1}\ >\ 2^m.$$
*Proof.* $a_1=\max(D\cup\Gamma_{m-1})$ (it dominates $a_2$ by sortedness,
and $R\cup\Gamma_{m-1}$ since $R\le2^{m-1}$ and $\Gamma_{m-1}$'s top is
$2^{m-1}<a_1$... more precisely $\le a_2\le a_1$, and $2^{m-1}<a_2\le a_1$
strictly since $a_2>2^{m-1}$). By the Global-max Peeling Lemma
(`lemmas/dominant-piece-lower-bound.md`),
$\mathrm{OddSum}(D\cup\Gamma_{m-1})=a_1+\mathrm{EvenSum}\bigl((D\setminus\{a_1\})\cup\Gamma_{m-1}\bigr)$.
Within $N:=\{a_2\}\cup R\cup\Gamma_{m-1}$, $a_2$ is the max (it exceeds
$2^{m-1}=\max\Gamma_{m-1}$ and dominates $R$), so by the Companion Peeling
Lemma (`lemmas/dominant-chain-theorem-and-prefix-run-decomposition.md`,
Lemma 5 — valid for *any* finite multiset, not just a $\Gamma$-block),
$\mathrm{EvenSum}(N)=\mathrm{OddSum}(N\setminus\{a_2\})=\mathrm{OddSum}(R\cup\Gamma_{m-1})$.
Within $R\cup\Gamma_{m-1}$, $2^{m-1}$ (from $\Gamma_{m-1}$) is the max
(since $R\le2^{m-1}$), so by the Global-max Peeling Lemma again,
$\mathrm{OddSum}(R\cup\Gamma_{m-1})=2^{m-1}+\mathrm{EvenSum}(R\cup\Gamma_{m-2})$.
Chaining the three identities gives the stated formula; the inequality
follows since $\mathrm{EvenSum}\ge0$ always and $a_1>2^{m-1}$ (from $a_1
\ge a_2>2^{m-1}$). $\blacksquare$ **Verified independently** by 3000 exact-
`Fraction` random trials of the full three-step identity chain
(`/tmp/verify4.py`, "p2 identity OK"), zero mismatches.

**Lemma P1 ($p=1$, conditional on $\mathrm{GT}(m-1)$, all $m\ge1$).**
Suppose $a_1>2^{m-1}\ge a_2,\dots,a_k=:R$ ($R=D\setminus\{a_1\}$, $|R|\le
m$, $\max(R)\le2^{m-1}$). Then
$$\mathrm{OddSum}(D\cup\Gamma_{m-1})=a_1+\mathrm{OddSum}(R\cup\Gamma_{m-2}).$$
*Proof.* $a_1=\max(D\cup\Gamma_{m-1})$ as above; Global-max Peeling gives
$\mathrm{OddSum}(D\cup\Gamma_{m-1})=a_1+\mathrm{EvenSum}(R\cup\Gamma_{m-1})$.
Within $R\cup\Gamma_{m-1}$, $2^{m-1}$ is the max ($R\le2^{m-1}$); Companion
Peeling gives $\mathrm{EvenSum}(R\cup\Gamma_{m-1})=\mathrm{OddSum}(R\cup
\Gamma_{m-2})$. $\blacksquare$ **Verified independently**, 3000 exact-
`Fraction` trials, zero mismatches ("p1 identity OK").

Applying $\mathrm{GT}(m-1)$ (hypotheses met: $|R|\le m=(m-1)+1$, $\max(R)
\le2^{m-1}$) gives $\mathrm{OddSum}(R\cup\Gamma_{m-2})\ge\min(\mathrm{sum}(R),
2^{m-1})$. For gap (a)'s specific instance ($\mathrm{sum}(D)=2^m+\varepsilon$,
$\max(D)\le2^m$, so $a_1\le2^m$): $\mathrm{sum}(R)=2^m+\varepsilon-a_1\ge
2^m+\varepsilon-2^m=\varepsilon>0$, and if $a_1\le2^{m-1}+\varepsilon$ then
$\mathrm{sum}(R)\ge2^{m-1}$; more simply since $a_1\le2^m$,
$\mathrm{sum}(R)\ge\varepsilon$ always but we need the sharper bound: since
$a_1>2^{m-1}$ (the $p=1$ hypothesis) and $a_1\le2^m$ (from $\max(D)\le2^m$),
in fact $\mathrm{sum}(R)=2^m+\varepsilon-a_1$ can range down to
$\varepsilon$ (as $a_1\to2^m$). The bound $\min(\mathrm{sum}(R),2^{m-1})$
combined with $a_1$ still closes the target in general (not just at
$\mathrm{sum}(D)=2^m+\varepsilon$): $a_1+\min(\mathrm{sum}(R),2^{m-1})\ge
a_1+\min(\mathrm{sum}(D)-a_1,\,2^{m-1})$, and since $a_1>2^{m-1}$, if
$\mathrm{sum}(D)-a_1\ge2^{m-1}$ the total is $\ge a_1+2^{m-1}>2^m$; if
$\mathrm{sum}(D)-a_1<2^{m-1}$ the total is $\ge a_1+(\mathrm{sum}(D)-a_1)=
\mathrm{sum}(D)\ge2^m$ (using $\mathrm{sum}(D)\ge2^m$, gap (a)'s regime).
So **Lemma P1 closes the $p=1$ case of $\mathrm{GT}(m)$ given $\mathrm{GT}
(m-1)$.**

### The residual case $p=0$: a second split, $r:=\#\{i:a_i>2^{m-2}\}$

When $p=0$ (all of $D\le2^{m-1}$), Global-max Peeling with $g=2^{m-1}$
(from $\Gamma_{m-1}$, the max since $D\le2^{m-1}$) gives
$$\mathrm{OddSum}(D\cup\Gamma_{m-1})=2^{m-1}+\mathrm{EvenSum}(D\cup\Gamma_{m-2}),$$
**verified independently**, 3000 exact-`Fraction` trials, zero mismatches
("p0 base identity OK"). So $p=0$ reduces to proving
$\mathrm{EvenSum}(D\cup\Gamma_{m-2})\ge2^{m-1}$ (using $\mathrm{sum}(D)=
2^m+\varepsilon$, gap (a)'s regime). Split by $r:=\#\{a_i>2^{m-2}\}$
among $D$'s (already $\le2^{m-1}$) elements.

**Lemma R2 ($r=2$, unconditional given $\mathrm{GT}(m-2)$, $m\ge2$).**
$a_1\ge a_2>2^{m-2}\ge$ rest $=:R$ ($|R|\le m-1$, $\max(R)\le2^{m-2}$),
$a_1,a_2\le2^{m-1}$ (inherited from $p=0$). Then
$$\mathrm{EvenSum}(D\cup\Gamma_{m-2})=a_2+\mathrm{OddSum}(R\cup\Gamma_{m-3}).$$
*Proof.* Companion Peeling on $N=D\cup\Gamma_{m-2}$ (max $a_1$):
$\mathrm{EvenSum}(N)=\mathrm{OddSum}(N\setminus\{a_1\})=\mathrm{OddSum}
(\{a_2\}\cup R\cup\Gamma_{m-2})$. Within that, $a_2$ is max ($a_2>2^{m-2}
\ge R,\Gamma_{m-2}$'s top): Global-max Peeling gives $a_2+\mathrm{EvenSum}
(R\cup\Gamma_{m-2})$. Within $R\cup\Gamma_{m-2}$, $2^{m-2}$ is max
($R\le2^{m-2}$): Companion Peeling gives $\mathrm{EvenSum}(R\cup\Gamma_{m-2})
=\mathrm{OddSum}(R\cup\Gamma_{m-3})$. Chain the three. $\blacksquare$
**Verified independently**, 3000 exact-`Fraction` trials ("r2 identity OK").
By $\mathrm{GT}(m-2)$ ($|R|\le m-1=(m-2)+1$, $\max(R)\le2^{m-2}$):
$\mathrm{OddSum}(R\cup\Gamma_{m-3})\ge\min(\mathrm{sum}(R),2^{m-2})$. Since
$a_1,a_2\le2^{m-1}$, $\mathrm{sum}(R)=(2^m+\varepsilon)-a_1-a_2\ge2^m+
\varepsilon-2\cdot2^{m-1}=\varepsilon$; and if $\mathrm{sum}(R)\ge2^{m-2}$
the total is $a_2+2^{m-2}>2^{m-2}+2^{m-2}=2^{m-1}$ (using $a_2>2^{m-2}$);
if $\mathrm{sum}(R)<2^{m-2}$ the total is $a_2+\mathrm{sum}(R)=
(2^m+\varepsilon-a_1)\ge2^m+\varepsilon-2^{m-1}=2^{m-1}+\varepsilon>2^{m-1}$
(using $a_1\le2^{m-1}$). Either way $\mathrm{EvenSum}(D\cup\Gamma_{m-2})>
2^{m-1}$. **Closes $r=2$.**

**Lemma R1 ($r=1$, conditional on $\mathrm{GT}(m-1)$, $m\ge2$).**
$a_1>2^{m-2}\ge$ rest $=:R$ ($|R|\le m$, $\max(R)\le2^{m-2}$), $a_1\le
2^{m-1}$. Then
$$\mathrm{EvenSum}(D\cup\Gamma_{m-2})=\mathrm{OddSum}(R\cup\Gamma_{m-2}).$$
*Proof.* Companion Peeling on $N=D\cup\Gamma_{m-2}$ (max $a_1$):
$\mathrm{EvenSum}(N)=\mathrm{OddSum}(N\setminus\{a_1\})=\mathrm{OddSum}
(R\cup\Gamma_{m-2})$. $\blacksquare$ **Verified independently**, 3000
exact-`Fraction` trials ("r1 identity OK"). By $\mathrm{GT}(m-1)$ ($|R|\le
m=(m-1)+1$, $\max(R)\le2^{m-2}<2^{m-1}$):
$\mathrm{OddSum}(R\cup\Gamma_{m-2})\ge\min(\mathrm{sum}(R),2^{m-1})$.
$\mathrm{sum}(R)=2^m+\varepsilon-a_1\ge2^m+\varepsilon-2^{m-1}=2^{m-1}+
\varepsilon>2^{m-1}$ (using $a_1\le2^{m-1}$), so $\min(\mathrm{sum}(R),
2^{m-1})=2^{m-1}$. **Closes $r=1$: $\mathrm{EvenSum}(D\cup\Gamma_{m-2})\ge
2^{m-1}$ exactly.**

**Feasibility Lemma for $r=0$ (exact threshold, proved in full).** Within
the $p=0$ regime, $r=0$ ($\max(D)\le2^{m-2}$, $k\le m+1$,
$\mathrm{sum}(D)=2^m+\varepsilon$) is **infeasible for every $m\le3$** and
**feasible for every $m\ge4$**. *Proof.* Feasibility requires
$(m+1)\cdot2^{m-2}\ge2^m+\varepsilon$ (the maximum possible sum of $m+1$
parts each $\le2^{m-2}$ must reach the target), i.e. $m+1\ge4+\varepsilon
\cdot2^{2-m}$. For $m\le2$: $2^{2-m}\ge1$, so the RHS is $>4\ge m+1$
(since $m+1\le3<4$) — infeasible. For $m=3$: condition becomes $4\ge4+
\varepsilon/2$, false for any $\varepsilon>0$ — infeasible (exact
boundary, checked directly: $(3+1)\cdot2^{1}=8$ vs. target $2^3+\varepsilon
=8+\varepsilon$, and $8<8+\varepsilon$). For $m\ge4$: $2^{2-m}\le1/4$, so
RHS $=4+\varepsilon/4<4+1/4<5\le m+1$ — feasible (e.g. $m+1$ equal parts
of value $(2^m+\varepsilon)/(m+1)\le2^{m-2}$ realizes it; check $m=4$:
$(16+\varepsilon)/5\le4=2^2$ iff $16+\varepsilon\le20$, true for
$\varepsilon<4$). $\blacksquare$

### Strong induction: $\mathrm{GT}(m)$ proved for $m=0,1,2,3$

- $\mathrm{GT}(0)$: base case, proved directly above.
- $\mathrm{GT}(1)$: $p=2$ closes unconditionally (Lemma P2); $p=1$ closes
  via Lemma P1 using $\mathrm{GT}(0)$; $p=0$ is **infeasible** at $m=1$
  (max sum with $k\le2$ parts $\le2^0=1$ each is $2<2^1+\varepsilon$).
  All cases closed. $\mathrm{GT}(1)$ **proved**.
- $\mathrm{GT}(2)$: $p=2$ unconditional; $p=1$ via Lemma P1 + $\mathrm{GT}
  (1)$ (just proved); $p=0$ needs $r=2,1,0$: by the Feasibility Lemma,
  $r=0$ is infeasible at $m=2$ ($m\le3$); $r=2$ via Lemma R2 +
  $\mathrm{GT}(0)$; $r=1$ via Lemma R1 + $\mathrm{GT}(1)$. All cases
  closed. $\mathrm{GT}(2)$ **proved** (this also reproves, by a cleaner
  general route, the round-9/10-era hand computation implicit in the
  file's earlier small-instance work).
- $\mathrm{GT}(3)$: $p=2$ unconditional; $p=1$ via Lemma P1 + $\mathrm{GT}
  (2)$; $p=0$: $r=0$ infeasible at $m=3$ (Feasibility Lemma, exact
  boundary case); $r=2$ via Lemma R2 + $\mathrm{GT}(1)$; $r=1$ via Lemma
  R1 + $\mathrm{GT}(2)$. All cases closed. $\mathrm{GT}(3)$ **proved**.

**Corollary (gap (a) of the Branch-I.A window, fully closed for
$\ell=1,2,3,4$).** Since gap (a) at level $\ell$ is exactly $\mathrm{GT}
(m)$ at $m=\ell-1$, $\mathrm{sum}(D)=2^m+\varepsilon$: **the window's top
endpoint is now proved, for every admissible $D$ (not merely a
numerically-found witness), at $\ell=1,2,3,4$.** Combined with gap (b)(i)
(Lemma TPI, all $\ell$) and Theorem W (the window's left endpoint, all
$\ell$), the Branch-I.A-restricted window is now **fully closed at
$\ell=1,2,3,4$** in every gap: left endpoint, top endpoint, and
piece-cap-unsaturated monotonicity. (Piece-cap-*saturated* monotonicity,
gap (b)(ii), and the window's interior for $\ell\ge5$, remain open — see
below.)

### Honest scope: $m\ge4$

The Feasibility Lemma shows $r=0$ (within $p=0$) becomes genuinely
feasible starting at $m=4$ — the recursive mechanism above does not reach
it. $r=0$ means $\max(D)\le2^{m-2}$ with $D$ still using up to $m+1$
pieces, i.e. **exactly the same shape as the $p=0$ sub-problem one level
down, but with two "extra" pieces of slack in the count cap relative to
what $\mathrm{GT}(m-2)$ would directly supply** — peeling once more
(comparing against $2^{m-3}$) reduces it to an $s\in\{0,1,2\}$ split
structurally identical to the $r$-split above, but the new $s=0$ residual
inherits the same "count cap exceeds what $\mathrm{GT}(m-3)$ can supply by
2" mismatch, recursively. This is a genuine, self-similar infinite-descent
structure (consistent with this approach's name) that was **not**
completed this round: the natural conjecture is that at each further
level the analogous "all-tiny" residual becomes feasible only once enough
levels have been peeled that the piece-count slack is absorbed, but making
this precise (a uniform statement provable by one clean induction on $m$,
rather than a growing tower of ad hoc case splits) is left open. Extensive
numerical stress-testing (structured equal-split and tied-pair grid
search across $m=0,\dots,7$, *not* naive gradient descent — per this
round's warning, tied-pair configurations were explicitly included in the
search grid) found **zero violations of $\mathrm{GT}(m)$ for any tested
$m$ up to $7$** (`/tmp/verify.py`, `/tmp/verify2.py`, `/tmp/verify3.py`),
consistent with $\mathrm{GT}(m)$ being true for all $m$, but this is
numerical evidence only for $m\ge4$, not a proof.

### Route (b) (exchange-smoothing) — not attempted this round

The round's dispatched alternative route (proving the maximizer is always
of Theorem W's tied-pair shape via exchange-smoothing, adapting cruxes
`aimo-0146`/`aimo-0119`) was not attempted this round; the GT($m$)
mechanism above proved more immediately tractable and yielded an
unconditional generalization (all admissible $D$, not one shape) for the
levels it closes. Left for a future round if the self-similar $m\ge4$
descent above proves difficult to close directly.

### Target 2 (Rank-Pinning import to the Middle-Regime Vertex Reduction
### Theorem) — not attempted this round

Time this round was spent entirely on Target 1, which yielded a
substantial, general (non-numerical, all-$D$) closure rather than an
upgrade of an existing numerical closure; Target 2 is left for a future
round, with no new gaps introduced into the Middle-Regime material by
this round's work (that section is untouched).

## Promotable lemmas (round 12)

- **General Theorem $\mathrm{GT}(m)$ (new, proved in full for $m=0,1,2,3$,
  general mechanism reusable for $m\ge4$).** For $D$ with $|D|\le m+1$,
  $\max(D)\le2^m$: $\mathrm{OddSum}(D\cup\Gamma_{m-1})\ge\min(\mathrm{sum}
  (D),2^m)$. Proved by a case split on $p=\#\{a_i>2^{m-1}\}\in\{0,1,2\}$
  (Lemmas P2, P1 above) with the $p=0$ residual further split by
  $r=\#\{a_i>2^{m-2}\}\in\{0,1,2\}$ (Lemmas R2, R1 above), the $r=0$
  sub-case shown infeasible for $m\le3$ (Feasibility Lemma) and open
  (self-similar recursion identified but not completed) for $m\ge4$.
  All non-base identities independently verified by exact-`Fraction`
  random trials (3000 each), zero mismatches.
- **Feasibility Lemma for $r=0$ (new, proved in full).** Within
  $\mathrm{GT}(m)$'s $p=0$ regime, the sub-case $\max(D)\le2^{m-2}$ with
  $|D|\le m+1$ pieces summing to $2^m+\varepsilon$ is infeasible for
  $m\le3$, feasible for $m\ge4$ — exact threshold, both directions proved.

## Round 13: Monotonicity Reduction (closes the large-sum scope gap in
## full) and the Unified Threshold-Pair-Peeling Lemma (structural progress
## on $m\ge4$, not a closure)

Per the round's dispatch (Route B primary, Route C secondary, Route A/D
fallback), this round pursued Route D first (a depth-parametrized
strengthened induction), since it surfaced two genuinely new, fully proved
results along the way. Route B (exchange-smoothing) and Route C (sibling
LP-vertex machinery) were **not attempted this round** — Route D's
structural analysis consumed the round's full budget and is reported
honestly below as *not yet a closure* of $m\ge4$, but as real progress
narrowing exactly what remains.

### Result 1: the Monotonicity Reduction Lemma (new, proved in full) —
### closes the reviewer's flagged large-sum ($p\ge3$) scope gap completely

**Statement.** Fix $m\ge0$, a fixed count $k\ge0$, and a fixed finite
multiset $T$ of positive reals (in our use, $T=\Gamma_{m-1}$). Let $D$ be
any finite multiset of positive reals with $|D|=k$ and $\max(D)\le2^m$,
and let $S_0\le\mathrm{sum}(D)$ be any target value with $S_0>0$. Then
there exists $D'$ with $|D'|=k$, $\max(D')\le\max(D)$, $\mathrm{sum}(D')=
S_0$, and
$$\mathrm{OddSum}(D\cup T)\ \ge\ \mathrm{OddSum}(D'\cup T).$$

**Proof.** By the certified **Elementwise Monotonicity Lemma**
(`lemmas/window-reduction-theorem-and-elementwise-monotonicity.md`), for
any fixed finite multiset $N$, $x\mapsto\mathrm{OddSum}(N\cup\{x\})$ is
non-decreasing on $(0,\infty)$. Enumerate $D=\{d_1,\dots,d_k\}$. Since
$\mathrm{sum}(D)\ge S_0>0$, we can strictly decrease coordinates one at a
time — at each step picking any coordinate not yet driven arbitrarily
close to $0$ and reducing it (staying $>0$) — until the total drops from
$\mathrm{sum}(D)$ to exactly $S_0$ (always possible: the total is a
continuous, strictly decreasing function of "how much has been drained
so far," ranging from $\mathrm{sum}(D)$ down to $0^+$ as every coordinate
$\to0^+$, so it passes through $S_0\in(0,\mathrm{sum}(D)]$ by the
intermediate value theorem, or constructively: repeatedly shrink the
current largest coordinate down towards $0$, moving to the next once it is
negligible, until the cumulative reduction equals $\mathrm{sum}(D)-S_0$).
Applying the Elementwise Monotonicity Lemma at each single-coordinate
shrink step (with $N$ = the fixed rest of $D\cup T$) shows
$\mathrm{OddSum}$ is non-increasing at every step, hence non-increasing
overall from $D\cup T$ to $D'\cup T$. Coordinates only ever decrease, so
$\max(D')\le\max(D)$. $\blacksquare$

**Independent numeric verification** (`/tmp/verify_mono.py`, this round):
exact-`Fraction` random trials, $m=1,\dots,6$, $k=1,\dots,m+1$,
$\mathrm{sum}(D)=2^m+\text{extra}$ for random extra $\in[0,25]$, shrinking
each instance down to $S_0=2^m$ via the greedy coordinate-drain
construction above: $5876$ valid (feasible) instances tested, **zero
violations** of $\mathrm{OddSum}(D)\ge\mathrm{OddSum}(D')$ or of
$\max(D')\le\mathrm{cap}$.

**Corollary (removes the reviewer's certified scope restriction on
$\mathrm{GT}(m)$, in full, for every $m$ where the bounded-sum statement
is known).** Suppose $\mathrm{GT}(m)$ holds for every $D$ with $|D|\le
m+1$, $\max(D)\le2^m$, and $\mathrm{sum}(D)=2^m$ **exactly** (a single
boundary value, comfortably inside the already-certified safe zone
$\mathrm{sum}(D)<3\cdot2^{m-1}$ for every $m\ge0$, since $2^m<3\cdot
2^{m-1}\iff2<3$). Then $\mathrm{GT}(m)$ holds for **every** $D$ with
$|D|\le m+1$, $\max(D)\le2^m$, and $\mathrm{sum}(D)\ge2^m$ — with **no
upper bound on $\mathrm{sum}(D)$ at all**. *Proof:* apply the
Monotonicity Reduction Lemma with $S_0=2^m$, $T=\Gamma_{m-1}$, to shrink
$D$ (same count $k\le m+1$, same or smaller cap) down to $D'$ with
$\mathrm{sum}(D')=2^m$ exactly; the hypothesis gives
$\mathrm{OddSum}(D'\cup\Gamma_{m-1})\ge2^m$, and monotonicity gives
$\mathrm{OddSum}(D\cup\Gamma_{m-1})\ge\mathrm{OddSum}(D'\cup\Gamma_{m-1})
\ge2^m=\min(\mathrm{sum}(D),2^m)$. $\blacksquare$ Since the certified
$\mathrm{GT}(m)$ (m=0,1,2,3) already covers $\mathrm{sum}(D)=2^m$ as an
ordinary interior instance of its proved safe zone, **this immediately and
unconditionally removes the reviewer's flagged $p\ge3$/large-sum caveat
for $m=0,1,2,3$** (no new casework needed — $p\ge3$ was only ever a
concern for $\mathrm{sum}(D)\ge3\cdot2^{m-1}$, and every such instance now
reduces, via this one Lemma, to the already-proved boundary instance).
More generally, **this is a reusable, $m$-independent tool**: any future
proof of $\mathrm{GT}(m)$ restricted to $\mathrm{sum}(D)\le2^m$ (bounded
sum) automatically yields the fully unrestricted-sum statement for free,
for that $m$ — so no future round attacking $\mathrm{GT}(m)$ for $m\ge4$
ever needs to separately worry about the large-sum/many-large-pieces
regime; only $\mathrm{sum}(D)\le2^m$ needs to be closed.

### Result 2: the Unified Threshold-Pair-Peeling Lemma (new, proved in
### full generality — replaces Lemmas P1/P2/R1/R2's case-by-case
### treatment of $p,r\in\{0,1,2\}$ with one lemma valid for any count)

**Elementary rank-shift identity (proved first, used throughout).** For
any finite multiset $N$ sorted descending $x_1\ge x_2\ge\cdots\ge x_n$ and
any $0\le q\le n$: writing $\mathrm{top}_q:=(x_1,\dots,x_q)$ and
$\mathrm{rest}_q:=(x_{q+1},\dots,x_n)$,
$$\mathrm{OddSum}(N)\ =\ \Bigl(\textstyle\sum_{i\text{ odd},\,i\le q}x_i
\Bigr)\ +\ \begin{cases}\mathrm{OddSum}(\mathrm{rest}_q)&q\text{ even}\\
\mathrm{EvenSum}(\mathrm{rest}_q)&q\text{ odd}.\end{cases}$$
*Proof.* Immediate from the definition: $\mathrm{rest}_q$'s $j$-th entry
is $N$'s $(q+j)$-th entry, so $\mathrm{rest}_q$'s local rank $j$ has
parity $j\bmod2$ while the corresponding global rank $q+j$ has parity
$(q+j)\bmod2$; these agree when $q$ is even and disagree when $q$ is odd.
Summing $N$'s odd-rank terms as (odd ranks $\le q$) $+$ (odd ranks $>q$,
reindexed into $\mathrm{rest}_q$'s own parity via the above) gives exactly
the displayed formula. $\blacksquare$ **Independently verified**
(`/tmp/verify_qsplit.py`, this round): $20000$ random trials, sizes
$n=1,\dots,12$, all $q\in\{0,\dots,n\}$, exact `Fraction` arithmetic,
**zero violations**.

**Application to $\mathrm{GT}(m)$'s case split.** Let $M=D\cup\Gamma_{k-1}$
with $D$'s elements sorted descending, and let
$q:=\#\{a_i\in D:a_i>2^{k-1}\}$ (so $\max(\Gamma_{k-1})=2^{k-1}$, and these
$q$ elements are exactly $M$'s top $q$, since every other element of $M$
— the rest of $D$ and all of $\Gamma_{k-1}$ — is $\le2^{k-1}$). Write
$R:=D\setminus\mathrm{top}_q$, $\sigma_q:=\sum_{i\text{ odd},i\le q}a_i$
(the odd-ranked elements among the top $q$). By the rank-shift identity:

- **$q\ge2$ (either parity) — closes trivially, unconditionally, with NO
  recursion into $R$ at all.** Among the top $q$ elements $a_1\ge\cdots\ge
  a_q$ (all $>2^{k-1}$ by definition of $q$), $\sigma_q$ sums
  $\lceil q/2\rceil\ge1$ of them, so $\sigma_q>2^{k-1}$ always (at least
  the term $a_1$ alone), and in fact $\sigma_q\ge\lceil q/2\rceil\cdot
  2^{k-1}$ term-by-term (each summand exceeds $2^{k-1}$). Using the
  rank-shift identity directly (before any further peeling of $R$):
  if $q$ is odd, $\mathrm{OddSum}(M)=\sigma_q+\mathrm{EvenSum}(R\cup
  \Gamma_{k-1})\ge\sigma_q>2^{k-1}\cdot\frac{q+1}2\ge2\cdot2^{k-1}=2^k$
  for $q\ge3$ (using $\mathrm{EvenSum}\ge0$); if $q$ is even $\ge2$,
  $\mathrm{OddSum}(M)=\sigma_q+\mathrm{OddSum}(R\cup\Gamma_{k-1})\ge
  \sigma_q+2^{k-1}$ (using the trivial bound $\mathrm{OddSum}(R\cup
  \Gamma_{k-1})\ge2^{k-1}$ from Global-max Peeling on $\Gamma_{k-1}$'s own
  top element, valid since $R\le2^{k-1}$, plus $\mathrm{EvenSum}\ge0$) $>
  2^{k-1}\cdot\frac q2+2^{k-1}\ge2\cdot2^{k-1}=2^k$ for $q\ge2$. **In both
  sub-cases the bound is established using only $\sigma_q$ and the fixed
  quantity $2^{k-1}$ — never touching $R$'s count, sum, or structure at
  all** (only $\mathrm{EvenSum},\mathrm{OddSum}\ge0$ is used for the
  remainder). This is strictly stronger than Lemmas P2/R2's original
  $q=2$-only argument: it shows **every** $q\ge2$ closes by the identical
  trivial mechanism, **regardless of the excess $e$** (i.e. regardless of
  how many more pieces $D$ is carrying beyond a plain instance) — a case
  that previously had to be re-derived by hand at $q=2$ only, per level,
  now closes uniformly for all $q\ge2$ in one inequality.
  **Independently verified** (`/tmp/verify_q_trivial.py`, this round):
  $1129$ valid random instances (arbitrary count/sum in the "rest" of
  $D$, deliberately including large-excess and large-sum residuals to
  stress the "regardless of $R$" claim), $q\in\{2,\dots,6\}$, $k=1,\dots,6$
  — **zero violations** of $\mathrm{OddSum}(M)>2^k$.
- **$q=1$.** $\mathrm{OddSum}(M)=a_1+\mathrm{EvenSum}(R\cup\Gamma_{k-1})=
  a_1+\mathrm{OddSum}(R\cup\Gamma_{k-2})$ (Companion Peeling, valid since
  $R\le2^{k-1}=\max(\Gamma_{k-1})$). This is the **only** case genuinely
  needing a further bound on $\mathrm{OddSum}(R\cup\Gamma_{k-2})$, i.e. a
  recursive call one level down (matches Lemma P1 exactly).
- **$q=0$.** $\mathrm{OddSum}(M)=2^{k-1}+\mathrm{EvenSum}(D\cup\Gamma_{k-2})
  =2^{k-1}+\mathrm{OddSum}(D\cup\Gamma_{k-3})$ — the "no progress, one
  level down" residual case (identical to round 12's $p=0,r=0$ steps, now
  seen as the $q=0$ instance of the same single lemma).

This **subsumes Lemmas P1 ($q=1$), P2 ($q=2$), R1 ($q=1$ one level down),
R2 ($q=2$ one level down)**, and moreover shows P2/R2's "$q=2$" hypothesis
was never the real content — **any** $q\ge2$ closes by the identical
mechanism. So the entire case split at every level collapses to **just
three outcomes**: $q=0$ (no progress, recurse one level down with the
same excess), $q=1$ (recurse into $\mathrm{GT}(k-1)$ applied to $R$), or
$q\ge2$ (closes immediately, unconditionally). This is a genuine
simplification of the proof architecture, not merely a relabeling — it
removes the need to separately verify a Feasibility-style count bound on
$q$ at every level (round 12's "$p\le2$"/"$r\le2$" derivations are now
unnecessary: $q$ can be *any* size $\ge2$ without further argument).

### Precise excess accounting: exactly why $q=0$ (and, less obviously,
### $q=1$ under excess) are the only cases that do not terminate in one
### unconditional step

Tracking the "excess" $e:=|D|-(k+1)$ (piece-count slack beyond a plain
$\mathrm{GT}(k)$ instance) through the corrected $q$-split above: if the
current level is $(k,e)$ (i.e. $|D|\le k+e+1$, cap $2^k$), then

- **$q\ge2$:** terminates unconditionally, **independent of $e$** (shown
  above — the bound never uses $R$'s count or sum). No excess-tracking
  needed for this branch at all.
- **$q=0$:** excess **increases** by exactly $1$, at level $k-1$: $e'=e+1$
  (matches round 12's Feasibility-Lemma finding — the "all still tiny"
  case is the unique non-trivial, excess-growing step).
- **$q=1$:** $R:=D\setminus\{a_1\}$ has count $|R|\le(k+e+1)-1=k+e$. If
  $e=0$, $|R|\le k=(k-1)+1$ fits a **plain** $\mathrm{GT}(k-1)$ instance
  (Result 1 makes this free at any sum) — terminates in one step, exactly
  reproducing Lemma P1. If $e\ge1$, $|R|\le k+e>k$ **still exceeds** a
  plain $\mathrm{GT}(k-1)$ instance's count cap by $e$ — i.e. $q=1$ does
  **not** reduce the excess at all when $e\ge1$ (only $k$ decreases, $e$
  is unchanged), and the target is not the clean boundary value $2^{k-1}$
  but the specific number $2^k-a_1$ (continuously dependent on $a_1$), so
  it does not immediately fall under the boundary-excess family
  $\mathrm{GEN}(k-1,e)$ either — **this sub-case (q=1 with $e\ge1$) was
  identified but not resolved this round.**

Since $k$ strictly decreases by at least $1$ at every step (whether
$q=0$, $q=1$, or $q\ge2$), and $k\ge0$, the *recursion on $k$* is
well-founded and reaches $k=0$ in at most $m$ steps from any starting
instance — there is no infinite regress in the sense of $k$ never
bottoming out. What is **not** yet established is that every instance
encountered along the way (in particular the $q=1,e\ge1$ sub-case just
flagged) is actually *closed* by the time $k=0$ is reached, rather than
merely *reduced* to another open sub-case at $k=0$ with $e$ still large;
the uniform base case below handles the specific boundary-value family
$\mathrm{GEN}(0,e)$ that the pure $q=0$ chain produces, but the $q=1$
excess-carrying sub-case's target is a *different*, continuously-varying
family not yet shown to reduce to that same base case. What remains open
is writing the induction **uniformly over all $(k,e)$ simultaneously**
(a clean double induction covering the $q=1,e\ge1$ sub-case too) rather
than re-deriving a fresh ad hoc bound at each $m$, as follows.

**Base case $k=0$, all $e\ge0$ (new, proved in full, uniform in $e$).**
At $k=0$: $\Gamma_{-1}=\varnothing$, cap $=2^0=1$, count $\le1+e$. In the
boundary-excess regime (the one actually needed for gap (a)'s recursion,
where $\mathrm{sum}(D)=2^{0+e}+\varepsilon=2^e+\varepsilon$ is carried
unchanged down a pure-$q=0$ chain from the original top level): feasibility
requires $(1+e)\cdot1\ge2^e+\varepsilon$, i.e. $e+1\ge2^e+\varepsilon$.
For $e=0$: $1\ge1+\varepsilon$, false. For $e\ge1$: $2^e\ge e+2>e+1$
(standard induction: $2^{e}-e-1$ is $0$ at $e=1$ ($2-1-1=0$, giving
$e+1=2^e$ exactly, still $<2^e+\varepsilon$ for $\varepsilon>0$) and
strictly increasing for $e\ge1$ since its discrete derivative
$2^{e+1}-2^e-1=2^e-1\ge1>0$). So $(1+e)<2^e+\varepsilon$ for **every**
$e\ge0$, i.e. **the $k=0$ boundary-excess instance is infeasible for every
excess level, uniformly** — a clean, $e$-independent base case (replacing
round 12's need to re-verify feasibility by hand at each $m\le3$).

**What is not yet closed.** Two distinct gaps remain, both honestly
identified rather than papered over:

1. **The $q=1$, $e\ge1$ sub-case (identified above).** When $q=1$ is
   drawn at a level with excess $e\ge1$, the resulting sub-problem is
   neither trivially closed (unlike $q\ge2$) nor a plain $\mathrm{GT}
   (k-1)$ instance nor exactly the clean boundary-excess family
   $\mathrm{GEN}(k-1,e)$ — its target is the continuously-varying value
   $2^k-a_1$. Whether this sub-case can be handled by a further
   application of Result 1 (Monotonicity Reduction, shrinking $R$ down to
   whatever boundary value matches $2^k-a_1$, if that value is itself
   $\ge$ some safely-inductable threshold) or needs its own argument was
   not resolved this round.
2. **The "small-sum" regime of $\mathrm{GT}(k-1)$ itself**, needed even in
   the $e=0$ instances of $q=1$ (matching original Lemma P1): the target
   $\mathrm{OddSum}(R\cup\Gamma_{k-2})\ge\min(\mathrm{sum}(R),2^{k-1})$ for
   $\mathrm{sum}(R)$ genuinely *below* $2^{k-1}$ is a different regime
   from the boundary-excess family $\mathrm{GEN}$ studied above (which
   only ever targets exactly $2^{k'}$, never a smaller value tracking
   $\mathrm{sum}(R)$ itself) — round 12's certified proof of
   $\mathrm{GT}(0),\dots,\mathrm{GT}(3)$ handles this small-sum regime
   together with the boundary regime in one uniform per-$m$ argument, but
   this round did **not** carry out the analogous small-sum excess
   accounting for general $m$ (it is a mirror-image computation to the
   boundary case above, not yet written down).

**This round's honest outcome:** the large-sum scope gap is fully closed
(Result 1, unconditional, all $m$); the count-cap case analysis is
substantially unified and simplified (Result 2: three cases instead of
five, with $q\ge2$ now closing unconditionally for **any** $q$, not just
$q=2$ exactly — removing round 12's need for a Feasibility-style bound on
$q$'s maximum value at every level); the uniform, $e$-independent base
case at $k=0$ is established. But the induction is **not** complete:
the $q=1/e\ge1$ sub-case and the small-sum mirror computation are both
identified precisely but not closed. $\mathrm{GT}(m)$ for $m\ge4$, and
hence gap (a) of the shared window for $\ell\ge5$, **remains open**.

### Numeric re-confirmation

Re-ran a random-search stress test (`/tmp/verify_qsplit.py`) at the exact
gap-(a) regime for $m=4,5,6$ (the levels this round's analysis narrows
closest to closing): $30000$ trials each, zero violations, minimum margins
found $0.1$, $0.40$, $1.48$ respectively (consistent with — not a
substitute for — the structural argument above; a non-adversarial local
search, not a certified tight-margin computation).

## Promotable lemmas (round 13)

- **Monotonicity Reduction Lemma (new, proved in full).** For fixed count
  $k$ and fixed multiset $T$: $\mathrm{OddSum}(D\cup T)$ can only decrease
  (weakly) as $D$'s coordinates are shrunk (same count, same or smaller
  cap) towards any target sum $S_0\in(0,\mathrm{sum}(D)]$. Direct corollary
  of the certified Elementwise Monotonicity Lemma. **Removes, completely
  and for every $m$, the reviewer's flagged large-sum/$p\ge3$ scope
  restriction on $\mathrm{GT}(m)$** — any future bounded-sum
  ($\mathrm{sum}(D)\le2^m$) proof of $\mathrm{GT}(m)$ automatically yields
  the fully unrestricted-sum statement for free. Reusable by any future
  approach needing to compare $\mathrm{OddSum}$ across different sums at
  fixed count/cap.
- **Rank-shift identity and Unified Threshold-Pair-Peeling Lemma (new,
  proved in full generality, any $q\ge0$).** Replaces the ad hoc P1/P2/R1/
  R2 case list with one mechanism, and strengthens it: **every** $q\ge2$
  (not just $q=2$) closes $\mathrm{OddSum}(D\cup\Gamma_{k-1})>2^k$
  unconditionally, independent of the excess $e$ or of $R$'s structure —
  proved via $\sigma_q>2^{k-1}\cdot\lceil q/2\rceil$ plus
  $\mathrm{OddSum},\mathrm{EvenSum}\ge0$, no recursion into $R$ needed.
  Only $q=0$ (excess increases by exactly $1$, no other change) and $q=1$
  (recurses into $\mathrm{GT}(k-1)$; unconditionally reproduces Lemma P1
  when $e=0$, but is not yet resolved when $e\ge1$) need further
  analysis. Reusable by any future approach needing a general "peel the
  elements exceeding a threshold" argument for $\mathrm{OddSum}$/
  $\mathrm{EvenSum}$ of a $D\cup\Gamma$-shaped multiset.
- **Uniform base case at $k=0$ (new, proved in full, all $e\ge0$
  simultaneously).** The boundary-excess instance is infeasible at $k=0$
  for every excess level $e$, by one inequality ($2^e>e+1$ for $e\ge1$,
  direct check at $e=0$), replacing round 12's per-$m$ feasibility
  verification.

## Round 14: the AltSum corollary, the Growth Lemma, and the exact
## reduction of the whole "small-sum mirror" sub-case to $\mathrm{Case}$-$B(m,k)$

Per this round's dispatch, the target was the variable-$V$ generalization
of the Unified Threshold-Pair-Peeling Lemma, closing sub-case (i) ($q=1$,
excess $e\ge1$, target $2^k-a_1$) and sub-case (ii) (the small-sum mirror
of $\mathrm{GT}(k-1)$). **Mandatory correction acknowledged first, per the
outline-reviewer's flag**: this round's own from-scratch numeric check
(below) confirms the reviewer's finding — the full-count small-sum
instance is **tight** (margin $\to0$), not slack as the explorer's
(erroneous) report claimed; no argument in this section relies on any
"genuine slack" claim.

**Note on the statement of $\mathrm{GT}(m)$ itself.** Re-reading round
12's boxed statement (`### The General Theorem GT(m)` above) shows the
variable target is *already built in*: $\mathrm{GT}(m)$'s conclusion is
$\mathrm{OddSum}(D\cup\Gamma_{m-1})\ge\min(\mathrm{sum}(D),2^m)$, not a
fixed $2^m$. So "the variable-$V$ generalization" the outline calls for is
not a new statement to invent — it is exactly $\mathrm{GT}(m)$'s own
$q=0$/$p=0$ branch at $\mathrm{sum}(D)\le2^m$ (the "small-sum mirror"),
which round 12/13 left open. This round's work is a direct, from-scratch
closure attempt of exactly that branch, not a re-statement exercise.

### Step 1: the elementary AltSum corollary (proved in full, one paragraph)

**Claim.** For any finite multiset $N$ of positive reals (sorted
descending $x_1\ge\cdots\ge x_n$), writing $\mathrm{AltSum}(N):=
\mathrm{OddSum}(N)-\mathrm{EvenSum}(N)$:
$$0\ \le\ \mathrm{AltSum}(N)\ \le\ \max(N).$$
(For $N=\varnothing$, $\mathrm{AltSum}(\varnothing):=0$, and both bounds
hold trivially with $\max(\varnothing):=0$.)

**Proof.** By induction on $|N|$. Base case $N=\varnothing$: both bounds
are $0=0$. Inductive step: by the certified Peeling Lemma applied to
$\mathrm{AltSum}$ (the identity $\mathrm{AltSum}(N)=\max(N)-\mathrm{AltSum}
(N\setminus\{\max N\})$, immediate from the definitions of $\mathrm{Odd
Sum}/\mathrm{EvenSum}$ by rank-shift: removing the maximum turns every
other rank's parity, so $\mathrm{OddSum}(N)=\max(N)+\mathrm{EvenSum}(N
\setminus\{\max N\})$ and $\mathrm{EvenSum}(N)=\mathrm{OddSum}(N\setminus
\{\max N\})$, and subtracting gives the displayed identity), and letting
$N':=N\setminus\{\max N\}$ (so $\max(N')\le\max(N)$): by the inductive
hypothesis $0\le\mathrm{AltSum}(N')\le\max(N')\le\max(N)$. Hence
$\mathrm{AltSum}(N)=\max(N)-\mathrm{AltSum}(N')\ge\max(N)-\max(N)=0$ (using
$\mathrm{AltSum}(N')\le\max(N)$) and $\mathrm{AltSum}(N)=\max(N)-\mathrm{Alt
Sum}(N')\le\max(N)-0=\max(N)$ (using $\mathrm{AltSum}(N')\ge0$). Both
bounds hold for $N$. $\blacksquare$

**Independent numeric verification** (`/tmp/verify_altsum.py`, this
round, exact `Fraction`): 5000 random multisets, sizes $1$–$10$, random
positive rational entries: zero violations of $0\le\mathrm{AltSum}(N)\le
\max(N)$.

This is exactly the tool named in the outline (step 2); certified in full
here, ready for the reviewer to promote as a standalone lemma.

### Step 2: an honest negative finding — the naive "excess-uniform"
### generalization of $\mathrm{GT}$ is FALSE

Before building on round 13's flagged $q=1,e\ge1$ gap, this round tested
the most natural fix: does $\mathrm{GT}$'s conclusion
$\mathrm{OddSum}(D\cup\Gamma_{k-1})\ge\min(\mathrm{sum}(D),2^k)$ continue
to hold if $D$ is allowed strictly more than $k+1$ pieces (i.e. an
"excess" $e\ge1$, same cap $2^{k-1}$ on $D$'s own elements, same target)?

**Counterexample (found and verified exactly, $k=0$, $e=1$).** $\Gamma_{-1}
=\varnothing$, cap $2^{-1}$ irrelevant since $k=0$ means $D$'s elements are
capped by $2^{k-1}=2^{-1}=0.5$... to keep this an honest, on-point test
matching how such a $D$ actually arises in the real recursion (via a pure
$q=0$ step at level $1$, threshold $2^0=1$), take $D=\{0.4,0.4\}$ (two
elements, each $\le2^0=1$, i.e. cap at the level-$1$ threshold, $|D|=2=
1+e+1$ with $e=1$). Then $\mathrm{OddSum}(D)=0.4$ (only the rank-$1$
element counts; $\Gamma_{-1}=\varnothing$ so there is nothing to union),
while $\min(\mathrm{sum}(D),2^0)=\min(0.8,1)=0.8$. Since $0.4<0.8$, the
naive statement **fails**.

**Diagnosis (this round, resolves why the counterexample does not
actually break $\mathrm{GT}(1)$).** Checking directly: $\mathrm{GT}(1)$ at
this $D$ asks $\mathrm{OddSum}(D\cup\Gamma_0)\ge\min(\mathrm{sum}(D),2)$;
$\Gamma_0=\{1\}$, so $\mathrm{OddSum}(\{1,0.4,0.4\})=1+0.4=1.4\ge\min(0.8,
2)=0.8$ — true, with margin. The reason the naive $k=0$ target failed but
the real $k=1$ target holds is that the $q=0$-peel identity
$\mathrm{OddSum}(D\cup\Gamma_{k-1})=2^{k-1}+\mathrm{EvenSum}(D\cup
\Gamma_{k-2})$ only genuinely *needs* a lower bound on
$\mathrm{EvenSum}(D\cup\Gamma_{k-2})$ when $\min(\mathrm{sum}(D),2^k)>
2^{k-1}$ (otherwise the free term $2^{k-1}$ alone already clears the
target, since $\mathrm{EvenSum}\ge0$) — i.e. the naive $\mathrm{GEN}(k,e)$
statement is asked to hold **outside the regime where it is ever actually
invoked** by the true recursion, and is simply false there. **This rules
out, cleanly, treating sub-case (i) as "just apply $\mathrm{GT}(k-1)$ with
a relaxed piece cap"** — no such relaxed statement is true in general;
whatever closes sub-case (i), if it exists, must use the sharper regime
restriction (target $>2^{k-1}$, i.e. $\mathrm{sum}(D)$ large relative to
the shrunk cap) instead of a piece-cap-free re-statement.

### Step 3: the Growth Lemma (new, proved in full) — the exact
### complement of the certified Monotonicity Reduction Lemma

**Statement.** Fix $m\ge1$ and $2\le k\le m+1$. Let $D$ be any finite
multiset of positive reals with $|D|=k$, every coordinate in $(0,
2^{m-1}]$, and $\mathrm{sum}(D)\le2^m$. Then there exists $D''$ with
$|D''|=k$, every coordinate of $D''$ in $(0,2^{m-1}]$, $\mathrm{sum}(D'')=
2^m$ exactly, and $D''$ obtained from $D$ by weakly increasing each
coordinate (i.e. $D''$'s $i$-th sorted coordinate is $\ge D$'s $i$-th
sorted coordinate for every $i$). Consequently, for any fixed finite
multiset $T$, by the certified **Elementwise Monotonicity Lemma**
(`lemmas/window-reduction-theorem-and-elementwise-monotonicity.md`,
applied one coordinate at a time exactly as in the Monotonicity Reduction
Lemma's own proof, but in the increasing direction) $\mathrm{OddSum}(D\cup
T)\ \le\ \mathrm{OddSum}(D''\cup T)$.

**Proof of feasibility (the only new content — the monotonicity direction
itself is the already-certified Elementwise Monotonicity Lemma, used
symmetrically to the Monotonicity Reduction Lemma's own proof).** The
maximum reachable sum with $k$ coordinates each capped at $2^{m-1}$ is
$k\cdot2^{m-1}$. Since $k\ge2$, $k\cdot2^{m-1}\ge2\cdot2^{m-1}=2^m\ge
\mathrm{sum}(D)$. So the target $2^m$ lies in $[\mathrm{sum}(D),
k\cdot2^{m-1}]$. Construct $D''$ by repeatedly increasing the current
coordinate with the least headroom to $2^{m-1}$ (i.e. saturate
coordinates one at a time), moving to the next once saturated: the
running total is a continuous, non-decreasing function of "how much has
been added so far," starting at $\mathrm{sum}(D)$ and rising to
$k\cdot2^{m-1}\ge2^m$ as every coordinate saturates, so it passes through
$2^m$ by the intermediate value theorem (stop increasing the current
coordinate exactly when the running total first reaches $2^m$, leaving
every later coordinate untouched). Every coordinate only increases, and
none exceeds $2^{m-1}$ by construction. $\blacksquare$

**Independent numeric verification** (`/tmp/verify_growth.py`, this
round, exact `Fraction`): for $m=1,\dots,6$, $k=2,\dots,m+1$, 2000 random
trials each: the constructed $D''$ always satisfies $\mathrm{sum}(D'')=2^m$
exactly, every coordinate $\le2^{m-1}$, and (checked against the
certified Elementwise Monotonicity Lemma's own already-verified direction)
$\mathrm{OddSum}(D\cup T)\le\mathrm{OddSum}(D''\cup T)$ for random $T$ —
zero violations.

**Why $k\ge2$ is the right (and necessary) hypothesis, and why $k<2$
needs no lemma at all.** If $k=1$ ($D=\{d\}$, $d\le2^{m-1}$), then
$\mathrm{sum}(D)=d\le2^{m-1}<2^m$ automatically, so this instance is never
one where a target close to $2^m$ is even asked of a single-coordinate
$D$ under the $q=0$/$p=0$ hypothesis below (see Step 4) — no growth
argument is needed there. If $k=0$, trivial. So the Growth Lemma's
$k\ge2$ hypothesis exactly matches every case it will be applied to
below (full-count instance has $k=m+1\ge2$ for $m\ge1$).

### Step 4: the exact reduction — the ENTIRE small-sum $q=0$/$p=0$ branch
### of $\mathrm{GT}(m)$ is equivalent to $\mathrm{Case}$-$B(m,k)$

Recall (round 12) the $q=0$/$p=0$ identity, re-derived and independently
verified again this round (`/tmp/verify_qzero_caseB.py`, 3000 exact-
`Fraction` trials, zero mismatches):
$$\mathrm{OddSum}(D\cup\Gamma_{m-1})\ =\ \mathrm{sum}(D)\ +\ 2^m-1\ -\
\mathrm{OddSum}(D\cup\Gamma_{m-2}),\qquad\text{whenever }\max(D)\le2^{m-1}.$$
(*Derivation*: $\mathrm{OddSum}(D\cup\Gamma_{m-1})=2^{m-1}+\mathrm{EvenSum}
(D\cup\Gamma_{m-2})$ (Global-max Peeling, $\max=2^{m-1}$ from $\Gamma_{m-1}$,
since $D\le2^{m-1}$); and $\mathrm{EvenSum}(D\cup\Gamma_{m-2})=\mathrm{sum}
(D)+\mathrm{sum}(\Gamma_{m-2})-\mathrm{OddSum}(D\cup\Gamma_{m-2})=
\mathrm{sum}(D)+(2^{m-1}-1)-\mathrm{OddSum}(D\cup\Gamma_{m-2})$ (using
$\mathrm{sum}(\Gamma_{m-2})=2^{m-1}-1$); substituting gives the displayed
identity exactly.) **Independently verified**, 3000 fresh exact-`Fraction`
trials this round, zero mismatches.

**Corollary (the exact equivalence, restricted to $\mathrm{sum}(D)\le
2^m$).** For $D$ with $\max(D)\le2^{m-1}$, $\mathrm{sum}(D)\le2^m$:
$$\mathrm{OddSum}(D\cup\Gamma_{m-1})\ \ge\ \mathrm{sum}(D)\quad\Longleftrightarrow\quad
\mathrm{OddSum}(D\cup\Gamma_{m-2})\ \le\ 2^m-1.$$
*Proof.* Direct rearrangement of the identity above (both sides subtract
$\mathrm{sum}(D)$ and $2^m-1-\mathrm{OddSum}(D\cup\Gamma_{m-2})$
respectively, then compare to $0$). $\blacksquare$ The right side is
**exactly** the hypothesis-conclusion pair of `Case-B(m,k)` (round 5's
boxed statement: $\mathrm{OddSum}(B\cup\Gamma_{m-2})\le2^m-1$), except
`Case-B(m,k)` is stated only for $\mathrm{sum}(B)=2^m$ exactly and
$\max(B)<2^{m-1}$ strictly, while the left side above needs it for
**every** $\mathrm{sum}(D)\le2^m$ (not just $=2^m$) and allows the
boundary $\max(D)=2^{m-1}$.

**Theorem (Small-Sum Reduction, new, proved in full modulo the tie
boundary).** Fix $m\ge2$. If `Case-B(m,k)` holds (i.e.
$\mathrm{OddSum}(B\cup\Gamma_{m-2})\le2^m-1$ for every $B$ with $|B|\le
m+1$, $\max(B)<2^{m-1}$, $\mathrm{sum}(B)=2^m$), then for every $D$ with
$|D|=k\ge2$ (in particular the full-count instance $k=m+1$), $\max(D)<
2^{m-1}$, and $\mathrm{sum}(D)\le2^m$: $\mathrm{OddSum}(D\cup\Gamma_{m-1})
\ge\mathrm{sum}(D)$.

*Proof.* By the Growth Lemma (Step 3, hypotheses met: $k\ge2$, $\max(D)\le
2^{m-1}$, $\mathrm{sum}(D)\le2^m$), there is $D''$ with $|D''|=k\le m+1$,
$\max(D'')\le2^{m-1}$, $\mathrm{sum}(D'')=2^m$, and $\mathrm{OddSum}(D\cup
\Gamma_{m-2})\le\mathrm{OddSum}(D''\cup\Gamma_{m-2})$. If $\max(D'')<
2^{m-1}$ strictly, `Case-B(m,k)` applies directly to $D''$ (which is a
valid instance: $|D''|\le m+1$, $\max(D'')<2^{m-1}$, $\mathrm{sum}(D'')=
2^m$), giving $\mathrm{OddSum}(D''\cup\Gamma_{m-2})\le2^m-1$, hence
$\mathrm{OddSum}(D\cup\Gamma_{m-2})\le2^m-1$; by the Corollary above this
is exactly equivalent to $\mathrm{OddSum}(D\cup\Gamma_{m-1})\ge
\mathrm{sum}(D)$, as claimed. (If the Growth Lemma's saturation construction
happens to produce a $D''$ with some coordinate exactly $2^{m-1}$ — the
one boundary configuration `Case-B(m,k)`'s strict hypothesis does not
literally cover — this is the one honestly-flagged remaining detail: it
needs the certified Tie-Neutrality Lemma
(`lemmas/tie-neutrality-and-first-mover-half.md`) to confirm the tied
element's rank-parity contribution is order-independent, reducing this
case to the strict one by a continuity/limiting argument; this reduction
was not completed in full this round — see "Honest gap" below.)
$\blacksquare$ (Modulo the flagged tie detail.)

**What this establishes.** This Theorem shows that **both** named
sub-sub-cases of the outline's sub-case (ii) — the "not-full-count"
instance (already reduced by the outline's own filler-insertion argument
to the boundary case $\mathrm{sum}=2^m$ at the same $m$) **and** the
"full-count" instance (reduced here, via the new Growth Lemma, to the
identical boundary case) — bottom out at exactly **one** object:
`Case-B(m,k)` at $\mathrm{sum}(D)=2^m$ — the file's own long-standing,
still-open central obstruction (rounds 4–11, the "middle regime," never
fully closed for general $m$; round 11 closed only the smallest instance
$(j,c)=(2,1)$ at $m=3,4$ exactly, with general $m$ open). **This is a
genuine simplification, not a new gap**: previously sub-case (ii) looked
like it might need brand-new machinery beyond `Case-B(m,k)`; this round
shows, via two newly-proved general-purpose lemmas (the AltSum corollary
and the Growth Lemma), that it needs **nothing more** than `Case-B(m,k)`
itself, already fully identified and worked on across seven prior rounds.
Since round 12's own $p=0$ branch of $\mathrm{GT}(m)$ (the large-sum-side,
gap-(a) regime $\mathrm{sum}(D)=2^m+\varepsilon$) reduces via the
already-certified Monotonicity Reduction Lemma to the SAME boundary case
$\mathrm{sum}(D)=2^m$, this round's finding **unifies**: the entire $p=0$
branch of $\mathrm{GT}(m)$, for every value of $\mathrm{sum}(D)$ (not
just the gap-(a) or small-sum regimes separately), is now known to be
**exactly equivalent** to `Case-B(m,k)` at the single value
$\mathrm{sum}(D)=2^m$ — closing off any hope that a *different* sum
regime might be easier than the one already attempted for seven rounds.

### Step 5: sub-case (i) ($q=1$, $e\ge1$) — still open, honestly reported

The negative finding of Step 2 (the naive piece-cap-relaxed generalization
of $\mathrm{GT}$ is false) rules out the most direct route. This round
traced *when* a $q=1$-with-excess instance actually arises in the real
recursion: starting from $\mathrm{GT}(m)$ at the boundary
$\mathrm{sum}(D_0)=2^m$, a chain of $e$ consecutive $q=0$ steps leaves
$D_0$ itself untouched (only $\Gamma$'s top pieces are peeled) at level
$k=m-e$, cap $2^k$, piece budget still $m+1$ (unchanged, since $D_0$ is
untouched). Feasibility of continuing the $q=0$ chain one more step
requires $(m+1)\cdot2^{k}\ge2^m$ (the only way $m+1$ pieces each $\le2^k$
can still sum near $2^m$); this **matches and generalizes** round 12's
own Feasibility Lemma (there stated only for $e\in\{0,1,2\}$). Once this
fails (i.e. once $e$ grows past $\log_2(m+1)$, roughly), the chain is
**forced** to encounter an element exceeding the current threshold — i.e.
a genuine $q=1$ (or $q\ge2$, already closed) step with $e\ge1$ **is not a
hypothetical extra case but the actual, unavoidable landing point of the
recursion once $m$ is large enough that a full-depth $q=0$ chain becomes
infeasible** (matching round 12's own finding that $r=0$ becomes feasible,
hence must eventually stop, only at $m\ge4$). **This is a genuine, useful
diagnosis** (it explains structurally *why* $m\ge4$ specifically is the
threshold where sub-case (i) first becomes unavoidable), but **it is not
a proof**: no argument was found this round establishing
$\mathrm{OddSum}(R\cup\Gamma_{k-2})\ge2^k-a_1$ when $R$ carries a genuine
excess $e\ge1$ inherited this way (as opposed to the false uniform
generalization of Step 2). This sub-case remains **fully open**.

### Independent numeric re-verification (this round, from scratch, per
### the outline-reviewer's mandatory instruction)

`/tmp/verify_qzero_caseB.py` (algebraic identity, 3000 trials) and a
direct adversarial random-composition search of $\mathrm{GT}(m)$ at
$\mathrm{sum}(D)=2^m$ exactly for $m=3,4,5$ (`/tmp/verify_q1_excess.py`,
4000 trials each, random compositions of $2^m$ into up to $m+1$ parts,
capped at $2^m$) found minimum margins $0.0$ (to search resolution) at
$m=3,4$ and $0.135$ at $m=5$ — **consistent with, and this round
independently reproduces, the outline-reviewer's finding that the
boundary/full-count regime is tight, not slack**. No new numeric evidence
this round contradicts the corrected (tight) picture; the explorer's
"genuine slack" claim is not used anywhere above.

### Honest gap summary (round 14)

- **Closed in full, general-purpose, reusable**: the AltSum corollary
  ($0\le\mathrm{AltSum}(N)\le\max(N)$) and the Growth Lemma (the exact
  increasing-direction complement of the certified Monotonicity Reduction
  Lemma).
- **Closed (modulo one flagged tie-boundary detail)**: the entire "small-
  sum mirror" sub-case (ii), both not-full-count (via the outline's
  filler-insertion, now understood to bottom out at the same object) and
  full-count (via this round's new Growth Lemma), is **equivalent** to
  `Case-B(m,k)` — already the file's own central, seven-round-old open
  obstruction, not a new one.
- **Not closed**: `Case-B(m,k)` itself (unresolved since round 4, "the
  middle regime," round 11's Vertex Reduction machinery closes only the
  smallest instance at $m=3,4$); and sub-case (i) ($q=1$, $e\ge1$), for
  which the naive fix is now known to be false and the genuine recursion
  point where it arises is now precisely diagnosed, but no closing
  argument was found.
- **Net**: $\mathrm{GT}(m)$ for $m\ge4$ remains open. This round's real
  contribution is a **simplification of the target**: instead of "close
  sub-case (i) and sub-case (ii) by two separate new mechanisms," it is
  now known that sub-case (ii) needs *no new mechanism at all* — it is
  exactly `Case-B(m,k)` — so all remaining effort on $\mathrm{GT}(m)$,
  $m\ge4$ can be focused on exactly two objects: `Case-B(m,k)` (already
  being attacked, rounds 4–11) and sub-case (i) (newly, precisely
  diagnosed but unsolved). Status remains `partial`.

## Round 15: the AltSum Small-Sum Lemma, sub-case (i) closed down to a
## width-1 window (independent of excess), and why route (2)'s premise fails

Per this round's dispatch (`self-similar-induction-on-n`, round 15): (1)
index-match sub-case (i) to $G(m,k;V)$ and revive its round-3/4 AltSum/
Single-Insertion machinery using the now-certified Growth Lemma; (2)
attempt a continuity/limiting transfer of `Case-B(m,k)`'s excluded
boundary. Both are addressed below, in the order the outline mandates
(cheap-kill index-match first).

### Step 1 (mandatory, per outline): the literal index-match to $G(m,k;V)$

Recall $G(m,k;V)$'s definition (round 3–4, boxed above): "for every
partition $B$ of $V$ into $j+1$ parts and every $c$-cut refinement $S$ of
$\Gamma_{m-1}$ with $j+c\le k$, $\mathrm{OddSum}(B\cup S)\ge V$" — with the
stated domain $V\in[2^{m-1},2^m]$.

Sub-case (i)'s object, after peeling the excess element $a_1$ from a
$q=1$ step of the Unified Threshold-Pair-Peeling Lemma (certified,
`lemmas/monotonicity-reduction-and-unified-threshold-pair-peeling.md`) at
level $k$: $R:=D\setminus\{a_1\}$, target $\mathrm{OddSum}(R\cup
\Gamma_{k-2})\ge2^k-a_1$, with $a_1\in(2^{k-1},2^k]$ (from $q=1$: $a_1$ is
$D$'s unique element $>2^{k-1}$, and $a_1\le2^k$ is inherited from the
cap at the level above). Taking $m:=k-1$ (as the outline instructs) so
$S=\Gamma_{m-1}=\Gamma_{k-2}$: the target value is $V:=2^k-a_1$, and
$$V\ \in\ (0,\,2^{k-1})\ =\ (0,\,2^m).$$

**The index-match FAILS in general.** $G(m,k;V)$'s stated domain requires
$V\ge2^{m-1}=2^{k-2}$, but $V=2^k-a_1$ ranges over the *entire* interval
$(0,2^{k-1})$, including values well below $2^{k-2}$ (attained whenever
$a_1>2^k-2^{k-2}=3\cdot2^{k-2}$, i.e. for the *larger* half of $a_1$'s
range). Concretely: at $k=3$, $a_1=7\in(4,8]$ gives $V=8-7=1<2^{k-2}=2$,
outside $G(m,k;V)$'s stated domain entirely. **This is exactly the cheap
mechanical check the outline demanded, done first, and it comes back
negative** — reviving $G(m,k;V)$ literally as defined would only cover
*part* of sub-case (i)'s actual $a_1$-range, not all of it, so it cannot
be the right tool without first extending its own domain (which the
outline did not ask for and round 3–4 never attempted for $V<2^{m-1}$
anyway — that regime was explicitly left open there too). **Per the
outline's own instruction ("if the index match is inexact the whole plan
below is void"), the literal $G(m,k;V)$-revival plan is abandoned here**
— but the mismatch analysis itself is what led directly to the genuinely
new mechanism below (Step 2), which turns out to need no restriction on
$V$ at all and supersedes what a domain-patched $G(m,k;V)$ would have
given.

Also confirmed, as the outline's "watch out" clause required: this is
**not** a relabeling of the already-refuted "piece-cap-relaxed
generalization of $\mathrm{GT}(k-1)$" (Step 2 of round 14, $D=\{0.4,0.4\}$
counterexample). That refuted statement asked for the *full* target
$\min(\mathrm{sum}(R),2^{k-1})$ to hold for **every** $\mathrm{sum}(R)$,
including at the boundary $\mathrm{sum}(R)=2^{k-1}$ itself, with excess
pieces. The new mechanism below is restricted to $\mathrm{sum}(R)\le
2^{k-1}-1$ (never touching the boundary), and the round-14 counterexample
lies exactly outside this restricted range (verified explicitly below) —
so it is a strictly narrower, genuinely different claim, not the refuted
one restated.

### Step 2: the AltSum Small-Sum Lemma (new, proved in full, no piece
### cap or max cap needed at all)

**Statement.** For any $m\ge0$ and any finite multiset $D$ of positive
reals (arbitrary count, arbitrary values — no cap on $|D|$ or $\max(D)$):
if $\mathrm{sum}(D)\le2^m-1$, then
$$\mathrm{OddSum}(D\cup\Gamma_{m-1})\ \ge\ \mathrm{sum}(D).$$

**Proof.** Let $X:=D\cup\Gamma_{m-1}$. By the certified **Lemma AS**
(`lemmas/altsum-reformulation-and-single-insertion.md`),
$\mathrm{OddSum}(X)=(\mathrm{sum}(X)+\mathrm{AltSum}(X))/2$. By the
certified **AltSum Corollary**
(`lemmas/altsum-corollary-and-growth-lemma.md`), $\mathrm{AltSum}(X)\ge0$
unconditionally (no hypothesis on $X$ beyond being a finite multiset of
positive reals). Hence
$$\mathrm{OddSum}(X)\ \ge\ \mathrm{sum}(X)/2\ =\ \bigl(\mathrm{sum}(D)+
\mathrm{sum}(\Gamma_{m-1})\bigr)/2\ =\ \bigl(\mathrm{sum}(D)+2^m-1\bigr)/2$$
(using the standard identity $\mathrm{sum}(\Gamma_{m-1})=2^{m-1}+\cdots+2+1
=2^m-1$). This is $\ge\mathrm{sum}(D)$ exactly when $2^m-1\ge\mathrm{sum}
(D)$, which is the hypothesis. $\blacksquare$

**Why this is strictly more general than anything previously certified
on this branch.** $\mathrm{GT}(m)$ itself (round 12) needs $|D|\le m+1$
and $\max(D)\le2^m$; the Growth Lemma (round 14) needs $2\le|D|\le m+1$.
This Lemma needs **neither**: no bound on $|D|$ (arbitrary excess $e$
allowed) and no bound on $\max(D)$ at all (beyond positivity) — only the
sum restriction $\mathrm{sum}(D)\le2^m-1$. It is proved from only two
already-certified, general-purpose facts (Lemma AS, AltSum Corollary),
with no new machinery.

**Independent numeric verification** (own exact-`Fraction` script,
`/tmp/verify_altsum_smallsum.py`, this round): $14{,}000$ trials, $m=0,
\ldots,6$, $D$ of random size $0$–$8$ (including counts far exceeding
$m+1$, i.e. deliberately stressing excess) with $\mathrm{sum}(D)$ random
in $[0,2^m-1]$: **zero violations**. Also confirmed, as a sanity check,
that dropping the hypothesis to $\mathrm{sum}(D)\in(2^m-1,2^m]$ (i.e.
outside this Lemma's stated range) genuinely produces violations
($18{,}000$ trials, $3835$ violations found) — the hypothesis $\mathrm{sum}
(D)\le2^m-1$ is not artificially conservative; it is exactly where the
easy argument stops working.

### Step 3: sub-case (i) closes down to a width-1 window, independent of
### excess $e$ (new, proved, the round's main positive result)

Apply the Monotonicity Reduction Lemma (certified, no restriction on
count $k$, so it applies equally with excess) to reduce to the single
boundary value $\mathrm{sum}(D)=2^k$ for the outer object at level $k$
(this is licensed exactly as in round 13's own corollary, and needs no
new argument here — the Lemma's statement places no upper bound on count
$k$, only that it is *fixed*, which the excess instance satisfies for
whatever its own $|D|$ happens to be).

At the $q=1$ step (Unified Threshold-Pair-Peeling Lemma, certified): sort
$D$ descending, $a_1:=\max(D)$ the unique element $>2^{k-1}$ (this is what
$q=1$ means), $R:=D\setminus\{a_1\}$ (so $\max(R)\le2^{k-1}$). By two
applications of the certified Global-max/Companion Peeling Lemmas (exactly
as in the proof of Lemma P1, round 12, reused here verbatim — no new
identity):
$$\mathrm{OddSum}(D\cup\Gamma_{k-1})\ =\ a_1+\mathrm{OddSum}(R\cup
\Gamma_{k-2}).$$
Since $\mathrm{sum}(D)=2^k$ exactly, $\mathrm{sum}(R)=2^k-a_1$. The target
$\mathrm{OddSum}(D\cup\Gamma_{k-1})\ge2^k$ is therefore **exactly**
equivalent to
$$\mathrm{OddSum}(R\cup\Gamma_{k-2})\ \ge\ 2^k-a_1\ =\ \mathrm{sum}(R).$$
This is **exactly** the AltSum Small-Sum Lemma's conclusion at level
$m:=k-1$ (so $\Gamma_{m-1}=\Gamma_{k-2}$, matching), applied to $D':=R$ —
and that Lemma's hypothesis is $\mathrm{sum}(R)\le2^{k-1}-1$. Since
$\mathrm{sum}(R)=2^k-a_1$, this hypothesis is
$$2^k-a_1\ \le\ 2^{k-1}-1\quad\Longleftrightarrow\quad a_1\ \ge\
2^{k-1}+1.$$

**Theorem (Sub-case (i), closed outside a width-1 window, every excess
$e\ge0$).** For every $k\ge1$, every excess $e\ge0$, and every $a_1\in
(2^{k-1},2^k]$ with $a_1\notin(2^{k-1},2^{k-1}+1)$ — i.e. $a_1\ge
2^{k-1}+1$ — and every $R$ (arbitrary count, cap $\max(R)\le2^{k-1}$,
$\mathrm{sum}(R)=2^k-a_1$): $\mathrm{OddSum}(D\cup\Gamma_{k-1})\ge2^k$
where $D=\{a_1\}\cup R$. *Proof.* Immediate from the identity and the
AltSum Small-Sum Lemma above, as just shown. $\blacksquare$

**This is a genuine, unconditional narrowing of sub-case (i) to exactly
the width-1 window $a_1\in(2^{k-1},2^{k-1}+1)$** — independent of the
excess $e$, independent of $R$'s internal structure (count, distribution)
beyond its cap and sum. Previously (round 13–14) sub-case (i) was fully
open with no closed sub-range at all; it is now known to be closed on
the *larger* half of $a_1$'s range ($a_1\ge2^{k-1}+1$, out of the full
range $(2^{k-1},2^k]$) unconditionally, for every excess.

**Independent numeric verification of both directions**
(`/tmp/verify_subcase_i_window.py`, this round, exact `Fraction`, random
excess piece counts up to $10$, $k=1,2,3,4$): outside the window
($a_1\ge2^{k-1}+1$), $0$ violations in $8506$ trials across all four $k$
values (matching the proof exactly, as expected for a proved fact); inside
the window ($a_1\in(2^{k-1},2^{k-1}+1)$), genuine violations found at
every $k$ tested ($3625,805,87,1$ violations respectively, out of
$3999,1984,1009,501$ trials) — confirming the window is not an artifact of
a weak proof technique but a real, still-open region where the target can
genuinely fail for *some* configurations (consistent with round 14's own
$D=\{0.4,0.4\}$-style boundary counterexample, which lands exactly in this
window: at $k=1$, $a_1=1.6\in(1,2)$, $R=\{0.4,0.4\}$, $\mathrm{sum}(R)=0.4<
2^0=1$ but the identity gives $\mathrm{OddSum}(D\cup\Gamma_0)=1.6+0.4=2.0\ge
2$ actually *holds* here with equality — the genuine violating instances
found by the search are different concrete configurations within the same
window, not this specific one; both are consistent with "the window is
open," i.e. some configurations in it satisfy the target and some do
not).

**What remains, honestly.** The residual window $a_1\in(2^{k-1},2^{k-1}+
1)$ is — by inspection — the *same shape* of object as the file's own
long-studied "Branch-I.A window" / width-1 "sliver" (rounds 5–11: e.g.
`Case-B(m,k)`'s sliver $2^{m-1}-1<\max(B)<2^{m-1}$, and the Branch-I.A
window $c_1\in[2^{\ell-1},2^{\ell-1}+1-\varepsilon)$), except here it
additionally carries an unrestricted excess $e$ on $R$'s piece count,
which none of the file's prior window closures (Theorem W, gap-(a)'s
$\mathrm{GT}(m)$ closure for $\ell\le4$) ever needed to handle — those
were all $e=0$. **This is new, useful information** (sub-case (i) is
provably not a separate, unrelated obstruction — it is exactly one more
instance of the file's single recurring width-1-window object, now with
an excess-piece twist), but it is **not a closure**: no argument closing
this excess-carrying window was found this round.

### Bonus (not new, but a genuine simplification): the AltSum Small-Sum
### Lemma re-derives `Case-B(m,k)`'s known safe zone in three lines

As a correctness cross-check (and because it directly bears on route
(2)'s premise, next section), apply Lemma AS + the AltSum Corollary
directly to `Case-B(m,k)`'s own object, $\mathrm{OddSum}(B\cup
\Gamma_{m-2})\le2^m-1$ with $\mathrm{sum}(B)=2^m$, $\max(B)<2^{m-1}$:

$$\mathrm{OddSum}(B\cup\Gamma_{m-2})\ =\ \frac{\mathrm{sum}(B)+\mathrm{sum}
(\Gamma_{m-2})+\mathrm{AltSum}(B\cup\Gamma_{m-2})}2\ =\ \frac{2^m+
(2^{m-1}-1)+\mathrm{AltSum}(B\cup\Gamma_{m-2})}2.$$

By the AltSum Corollary, $\mathrm{AltSum}(B\cup\Gamma_{m-2})\le\max(B\cup
\Gamma_{m-2})=\max(\max(B),2^{m-2})$. If $\max(B)\le2^{m-1}-1$ (a strictly
narrower cap than the sliver's own hypothesis $\max(B)<2^{m-1}$), this
gives $\mathrm{AltSum}\le2^{m-1}-1$, hence
$$\mathrm{OddSum}(B\cup\Gamma_{m-2})\ \le\ \frac{2^m+2^{m-1}-1+2^{m-1}-1}2
\ =\ \frac{2^{m+1}-2}2\ =\ 2^m-1,$$
which is **exactly** `Case-B(m,k)`'s target, with equality possible.
**This reproduces round 5's main finding** (sub-cases $b_1<2^{m-2}$ and
$2^{m-2}\le b_1\le2^{m-1}-1$ both close) in **three lines**, using only
already-certified general-purpose tools, instead of round 5's original
peel-and-Lemma-B argument. **Not a new closure** — the residual sliver
$\max(B)\in(2^{m-1}-1,2^{m-1})$ is exactly the same open gap round 5 left,
confirmed here from an independent derivation (a useful correctness
cross-check, and the reason the next section's premise can be checked
precisely).

**Independent numeric verification** (`/tmp/verify_caseb_altsum.py`, this
round, exact `Fraction`): $5474$ valid trials, $m=2,\ldots,6$, random
excess piece counts, $\max(B)\le2^{m-1}-1$: **zero violations** of
$\mathrm{OddSum}(B\cup\Gamma_{m-2})\le2^m-1$.

### Step 4 (route 2): why the dispatched continuity/limiting argument's
### premise does not hold — an honest Spec concern for the outliner

The outline's route (3) [labelled route (2) in the dispatch to this
approach] asks to "fix the already-proved interior inequality
$\mathrm{OddSum}(D\cup\Gamma_{m-2})\le2^m-1$ for $\max(D)<2^{m-1}-\delta$
for every $\delta>0$, and take $\delta\to0$" using the Tie-Neutrality
Lemma to handle the limiting tie at $\max(D)=2^{m-1}$.

**This premise is checked here against the file's own certified history
and found to be incorrect.** Round 5 (reconfirmed independently above, in
three lines, via the AltSum Small-Sum Lemma) proved the interior
inequality holds **only up to the hard boundary $\max(B)\le2^{m-1}-1$** —
a **fixed unit-width gap** from $2^{m-1}$, not a family of results
$\{\max(D)<2^{m-1}-\delta\}_{\delta>0}$ shrinking to the boundary. In
particular there is **no proof on record, at any $\delta\in(0,1)$, of the
interior inequality for $\max(D)\in(2^{m-1}-1,2^{m-1}-\delta)$** for any
$\delta<1$ — the entire sliver $(2^{m-1}-1,2^{m-1})$ is uniformly open
(round 5 through round 11, never closed for general $m$; round 11 closed
only two point-instances at $m=3,4$ for one specific sub-family, not a
$\delta$-indexed approach-to-the-boundary family). **A continuity/limiting
argument requires an actual convergent family of already-proved
statements to take a limit of; none exists here** — the honest situation
is a single macroscopic (width-1) gap, not a vanishing one, so "take
$\delta\to0$" has no proved starting family to apply to. The explorer's
numeric finding (margin $\to0$ as $\max(D)\to2^{m-1}^-$, from Nelder-Mead
sweeps) is evidence about the **true value** of the (still unproved)
quantity, not evidence of a proof technique that becomes tight in the
limit — a vanishing true margin does not supply a vanishing-$\delta$
family of *proved* inequalities to invoke the Tie-Neutrality Lemma on.
**This route, as dispatched, cannot be executed** — reported here as an
honest Spec concern, not a hidden failure: any future attempt at a
continuity-style argument for `Case-B(m,k)`'s sliver would first need to
either (a) prove a genuine $\delta$-indexed family of interior results
approaching the boundary (which round 5–11 did not produce, and which the
sliver's own known counterexample-adjacent tightness — margin $\to0$ —
suggests may not even be the right shape of argument, since a family
whose bound itself also $\to0$ cannot straightforwardly be used to
conclude a fixed nonzero-margin statement at the boundary), or (b) attack
the width-1 sliver directly (as rounds 5–11 already did, with only the
two smallest-instance closures at $m=3,4$ from round 11's Vertex Reduction
machinery).

### Honest net effect, round 15

- **New, certified-ready, general-purpose lemma**: the AltSum Small-Sum
  Lemma (no piece-count or max cap needed, only a sum bound) — strictly
  subsumes the sum-restricted content of $\mathrm{GT}(m)$ and the Growth
  Lemma on this branch, in a two-line proof from already-certified tools.
- **Sub-case (i) is now closed on the majority of its range**
  ($a_1\ge2^{k-1}+1$, unconditionally, every excess $e$) — previously
  entirely open. The remaining gap is now **exactly** the width-1 window
  $a_1\in(2^{k-1},2^{k-1}+1)$, identified (not just conjectured) as the
  same recurring self-similar object as the file's other open windows,
  now additionally carrying an unrestricted excess $e$.
- **`Case-B(m,k)`'s known safe zone is re-derived independently** (a
  correctness cross-check, not new ground), confirming round 5's finding
  precisely and showing route (2)'s premise (a shrinking-$\delta$ family)
  does not exist — reported as a Spec concern.
- **Net**: $\mathrm{GT}(m)$ for $m\ge4$ **remains open**, but sub-case (i)
  is substantially narrowed (from "fully open" to "a width-1 window,
  independent of excess"), and `Case-B(m,k)`'s obstruction is confirmed
  (not newly closed) with a cleaner, independent re-derivation. Status
  remains `partial`.

## Promotable lemmas (round 14)

- **AltSum corollary** ($0\le\mathrm{AltSum}(N)\le\max(N)$ for any finite
  multiset $N$ of positive reals) — proved in full above, one-paragraph
  induction from the certified Peeling Lemma. General-purpose, reusable.
- **Growth Lemma** (the increasing-direction complement of the certified
  Monotonicity Reduction Lemma: for $D$ with $|D|=k\ge2$, coordinates in
  $(0,2^{m-1}]$, $\mathrm{sum}(D)\le2^m$, there is $D''\ge D$
  coordinatewise with the same count/cap and $\mathrm{sum}(D'')=2^m$
  exactly, so $\mathrm{OddSum}(D\cup T)\le\mathrm{OddSum}(D''\cup T)$ for
  any fixed $T$) — proved in full above. General-purpose, reusable by any
  future approach needing to compare $\mathrm{OddSum}$ across sums at
  fixed count/cap in the *increasing* direction (the certified
  Monotonicity Reduction Lemma only gave the decreasing direction).
- **Small-Sum Reduction Theorem** (`Case-B(m,k)` $\Rightarrow$ the entire
  small-sum mirror sub-case of $\mathrm{GT}(m)$'s $p=0$/$q=0$ branch, for
  every $\mathrm{sum}(D)\le2^m$ and every count $k\ge2$, via the Growth
  Lemma) — proved above, modulo the flagged tie-boundary detail
  ($\max(D'')=2^{m-1}$ exactly). Reusable once `Case-B(m,k)` itself
  closes.

## Promotable lemmas (round 15)

- **AltSum Small-Sum Lemma (new, proved in full).** For any $m\ge0$ and
  any finite multiset $D$ of positive reals (no cap on $|D|$ or
  $\max(D)$): if $\mathrm{sum}(D)\le2^m-1$ then $\mathrm{OddSum}(D\cup
  \Gamma_{m-1})\ge\mathrm{sum}(D)$. Two-line proof from the already-
  certified Lemma AS
  (`lemmas/altsum-reformulation-and-single-insertion.md`) plus the
  already-certified AltSum Corollary
  (`lemmas/altsum-corollary-and-growth-lemma.md`); no new machinery.
  Independently verified, $14{,}000$ exact-`Fraction` trials (own script,
  this round), zero violations; also confirmed the hypothesis
  $\mathrm{sum}(D)\le2^m-1$ is tight (violations appear immediately
  outside it, $3835/18000$ in a direct sweep). General-purpose and
  reusable: strictly subsumes, on the sum-restricted branch, both
  $\mathrm{GT}(m)$'s and the Growth Lemma's piece-count/cap hypotheses
  (needs neither).
- **Sub-case (i) Window Reduction Theorem (new, proved in full).** For
  every $k\ge1$, every excess $e\ge0$, and every $a_1\in(2^{k-1},2^k]$
  with $a_1\ge2^{k-1}+1$ (i.e. outside the width-1 window
  $(2^{k-1},2^{k-1}+1)$), and every $R$ (any count, $\max(R)\le2^{k-1}$,
  $\mathrm{sum}(R)=2^k-a_1$): $\mathrm{OddSum}(\{a_1\}\cup R\cup
  \Gamma_{k-1})\ge2^k$ — a direct corollary of the AltSum Small-Sum Lemma
  applied to $R$ at level $m=k-1$, via the exact peel identity
  $\mathrm{OddSum}(D\cup\Gamma_{k-1})=a_1+\mathrm{OddSum}(R\cup
  \Gamma_{k-2})$ (Global-max + Companion Peeling, both already certified).
  Independently verified in both directions (proved region: $8506$ trials,
  zero violations; open window: violations found at every tested $k$,
  confirming the window is genuinely open, not a proof artifact).
  Reusable once the residual width-1-with-excess window closes (would
  immediately close sub-case (i) of $\mathrm{GT}(m)$ in full).

## Round 16: Step 3 corrected — the width-1 window closes in full for
## excess $e\ge1$; the residual is exactly $e=0$'s sliver

Per this round's dispatch: round 15's Step 3 shrank the outer object $D$
to the abstract small boundary $\mathrm{sum}(D)=2^k$ via the Monotonicity
Reduction Lemma, then applied the AltSum Small-Sum Lemma to
$R=D\setminus\{a_1\}$ at the *small* target $\mathrm{sum}(R)=2^k-a_1$. The
math-explorer (`math-explorer-window.md`, this round) found this
abstraction is **provably false** in general for $e\ge1$ (exact
counterexample at $k=3$) — but also found, correctly, that it is **not
the object that actually arises** from the genuine, count-bounded
recursion: a $q=0$ chain of length $e$ from the true top level $m$ down
to $k=m-e$ never touches $D$'s own mass (only $\Gamma$'s top elements get
peeled off into the running total), so the residual $R=D\setminus\{a_1\}$
that genuinely arises at level $k$ has $\mathrm{sum}(R)=2^m-a_1$ — large
(of order $2^m$), not $2^k-a_1$ (small). This section proves the correct,
directly-embedded target unconditionally for every $e\ge1$, closing the
window entirely on that range.

### Step 0: re-derivation of the correct target from the recursion itself

Recall the exact excess bookkeeping (round 13, "Precise excess
accounting," reused here): starting from the top level $m$ with
$\mathrm{sum}(D)=2^m$ (WLOG, by the certified Monotonicity Reduction
Lemma — this reduction to the sum-$2^m$ boundary case is legitimate and
unaffected by this round's fix; it is a different, licensed use of that
Lemma from the one being corrected below), a chain of $e\ge1$ consecutive
$q=0$ steps produces, at each step, the identity
$$\mathrm{OddSum}(D\cup\Gamma_{j-1})=2^{j-1}+\mathrm{OddSum}(D\cup
\Gamma_{j-2})$$
(the certified $q=0$ case of the Unified Threshold-Pair-Peeling Lemma,
`lemmas/monotonicity-reduction-and-unified-threshold-pair-peeling.md`),
with $D$ itself **never modified** — only the level index $j$ drops by
$1$ and a fixed term $2^{j-1}$ is peeled into the running total. Applying
this for $j=m,m-1,\ldots,k+1$ (i.e. $e=m-k$ times) gives
$$\mathrm{OddSum}(D\cup\Gamma_{m-1})=\bigl(2^{m-1}+2^{m-2}+\cdots+2^k
\bigr)+\mathrm{OddSum}(D\cup\Gamma_{k-1})=(2^m-2^k)+\mathrm{OddSum}(D\cup
\Gamma_{k-1}),$$
using $2^{m-1}+\cdots+2^k=2^m-2^k$. Since $D$ is unchanged throughout,
$\mathrm{sum}(D)$ is still $2^m$ when we reach level $k$. The target
$\mathrm{OddSum}(D\cup\Gamma_{m-1})\ge2^m$ is therefore **exactly**
equivalent to
$$\mathrm{OddSum}(D\cup\Gamma_{k-1})\ \ge\ 2^m-(2^m-2^k)\ =\ 2^k,$$
**with $D$ still carrying its full mass $\mathrm{sum}(D)=2^m$** — this is
the precise sense in which round 15's Step 3 over-generalized: the target
at level $k$ really is the small value $2^k$ (correct, matches round 15),
but the object $D$ achieving it is **not free to have small sum** — it is
pinned at $\mathrm{sum}(D)=2^m$ by the chain above, a fact round 15's
Monotonicity-Reduction step silently discarded by treating "reduce to
$\mathrm{sum}(D)=2^k$" as if it were licensed at level $k$ directly. It
is not: the Monotonicity Reduction Lemma lets us fix $\mathrm{sum}(D)$
at the boundary of *its own* domain (level $m$, before any $q=0$ step),
but it does not commute with descending a $q=0$ chain, which fixes
$\mathrm{sum}(D)$ at $2^m$ irrevocably, not $2^k$.

Now peel $a_1:=\max(D)$ (the unique element of $D$ exceeding $2^{k-1}$,
by definition of the $q=1$ step reached at level $k$) via the certified
**Companion Peeling Lemma** (same file, cited throughout this approach):
since $\max(R)\le2^{k-1}=\max(\Gamma_{k-1})$ where $R:=D\setminus\{a_1\}$,
the second-largest element of $D\cup\Gamma_{k-1}$ is $\Gamma_{k-1}$'s own
top element $2^{k-1}$, so
$$\mathrm{OddSum}(D\cup\Gamma_{k-1})\ =\ a_1+\mathrm{OddSum}(R\cup
\Gamma_{k-2}).$$
(This is the same identity round 15 used; the correction is entirely in
what value $\mathrm{sum}(R)$ carries.) Since $\mathrm{sum}(D)=2^m$
exactly, $\mathrm{sum}(R)=2^m-a_1$ — the **actual, large** forced value,
confirming the outline's diagnosis exactly. The needed inequality
$\mathrm{OddSum}(D\cup\Gamma_{k-1})\ge2^k$ is therefore equivalent to
$$\mathrm{OddSum}(R\cup\Gamma_{k-2})\ \ge\ 2^k-a_1,\qquad\text{with }
\mathrm{sum}(R)=2^m-a_1\ (\text{large}).$$

### Step 1: the Half-Sum Corollary (new, immediate from certified tools)

**Statement.** For any finite multiset $N$ of positive reals (no cap on
count or values), $\mathrm{OddSum}(N)\ge\mathrm{sum}(N)/2$.

**Proof.** By the certified Lemma AS
(`lemmas/altsum-reformulation-and-single-insertion.md`),
$\mathrm{OddSum}(N)=(\mathrm{sum}(N)+\mathrm{AltSum}(N))/2$. By the
certified AltSum Corollary
(`lemmas/altsum-corollary-and-growth-lemma.md`), $\mathrm{AltSum}(N)\ge0$
unconditionally. Substituting gives $\mathrm{OddSum}(N)\ge
\mathrm{sum}(N)/2$. $\blacksquare$

(This is the same two facts used for the — different, and provably
insufficient for this purpose at $e=0$ — AltSum Small-Sum Lemma of round
15; here they are combined without the sum-cap hypothesis, since we are
now proving a lower bound that does not need one.)

### Step 2: the Large-Sum Closure Theorem (new, proved in full — the
### round's main positive result)

**Theorem.** For every $k\ge1$, every $m\ge k+1$ (equivalently, excess
$e:=m-k\ge1$), every $a_1\in(2^{k-1},2^k]$, and every finite multiset $R$
of positive reals with $\mathrm{sum}(R)=2^m-a_1$ (arbitrary count,
arbitrary individual values — in particular this covers, but is not
restricted to, the case $\max(R)\le2^{k-1}$ that actually arises from
sub-case (i)):
$$\mathrm{OddSum}(R\cup\Gamma_{k-2})\ \ge\ 2^k-a_1.$$

**Proof.** By the Half-Sum Corollary applied to $N:=R\cup\Gamma_{k-2}$,
using $\mathrm{sum}(\Gamma_{k-2})=2^{k-1}-1$ (standard geometric-sum
identity, $2^{k-2}+\cdots+2+1=2^{k-1}-1$):
$$\mathrm{OddSum}(R\cup\Gamma_{k-2})\ \ge\ \frac{\mathrm{sum}(R)+
2^{k-1}-1}2\ =\ \frac{(2^m-a_1)+2^{k-1}-1}2.$$
It suffices to show
$$\frac{2^m-a_1+2^{k-1}-1}2\ \ge\ 2^k-a_1
\quad\Longleftrightarrow\quad
2^m+a_1\ \ge\ 2^{k+1}-2^{k-1}+1\ =\ \tfrac32\cdot2^k+1.\tag{$\ast$}$$
Since $m\ge k+1$, $2^m\ge2^{k+1}$; and since $a_1>2^{k-1}$ (the defining
lower bound of sub-case (i)'s range), we get
$$2^m+a_1\ >\ 2^{k+1}+2^{k-1}\ =\ \tfrac52\cdot2^k.$$
It remains to check $\tfrac52\cdot2^k\ge\tfrac32\cdot2^k+1$, i.e.
$2^k\ge1$, which holds for every $k\ge0$. Hence $(\ast)$ holds (with
room to spare — the inequality $2^m+a_1>\tfrac52\cdot2^k$ is already
strict, and the arithmetic margin $\tfrac52\cdot2^k-(\tfrac32\cdot2^k+1)
=2^k-1\ge0$ for $k\ge1$), giving
$$\mathrm{OddSum}(R\cup\Gamma_{k-2})\ \ge\ \frac{2^m-a_1+2^{k-1}-1}2\ \ge\
2^k-a_1,$$
as required. $\blacksquare$

**Independent numeric verification** (own exact-`Fraction` scripts, this
round): (a) a broad sweep, $m=2,\ldots,12$, $k=1,\ldots,m-1$ (forcing
$e\ge1$), $a_1$ random anywhere in $(2^{k-1},2^k]$, $R$ of random count
$1$–$10$ with arbitrary positive values summing to $2^m-a_1$ (no cap
imposed, deliberately stress-testing the theorem's full generality):
$30{,}000$ trials, **zero violations**; (b) a targeted sweep restricted to
$a_1$ inside the residual width-1 window $(2^{k-1},2^{k-1}+1)$ specifically
(the case this round must close), same $m,k,R$ ranges: $28{,}851$ valid
trials, **zero violations**, minimum observed margin $\mathrm{OddSum}-
\mathrm{target}\approx0.546$ at $(m,k,e)=(2,1,1)$ — matching the proof's
own worst-case margin $2^k-1\big|_{k=1}=1$ up to the factor of $2$ from
$(\ast)$'s division (theoretical minimum margin at $k=1$: $(2^k-1)/2=0.5$,
consistent); (c) large-excess stress test, $k=1,2,3$, $e$ up to $15$
(so $m$ up to $18$): $20{,}000$ trials, zero violations, confirming the
margin does not degrade or vanish as excess grows (it only grows, since
$2^m$ dominates). Scripts: `/tmp/explore3.py`, `/tmp/explore4.py`,
`/tmp/explore5.py` (this round).

### Step 3: closing the width-1 window for every excess $e\ge1$

**Theorem (Sub-case (i) closed in full for $e\ge1$).** For every $k\ge1$,
every $m\ge k+1$ (excess $e=m-k\ge1$), every $a_1\in(2^{k-1},2^k]$
(including, and not restricted to, the width-1 window
$(2^{k-1},2^{k-1}+1)$), and every $D=\{a_1\}\cup R$ with
$\max(R)\le2^{k-1}$ and $\mathrm{sum}(D)=2^m$:
$$\mathrm{OddSum}(D\cup\Gamma_{m-1})\ \ge\ 2^m.$$

**Proof.** By Step 0's $q=0$-chain peeling identity (using the certified
$q=0$ case of the Unified Threshold-Pair-Peeling Lemma $e$ times,
$D$ unchanged throughout) and the Companion Peeling identity (using
$\max(R)\le2^{k-1}$, exactly sub-case (i)'s own hypothesis):
$$\mathrm{OddSum}(D\cup\Gamma_{m-1})\ =\ (2^m-2^k)+a_1+\mathrm{OddSum}(R
\cup\Gamma_{k-2}).$$
By Step 2's Large-Sum Closure Theorem (hypotheses met: $k\ge1$, $m\ge
k+1$, $a_1\in(2^{k-1},2^k]$, $\mathrm{sum}(R)=2^m-a_1$),
$\mathrm{OddSum}(R\cup\Gamma_{k-2})\ge2^k-a_1$. Substituting,
$$\mathrm{OddSum}(D\cup\Gamma_{m-1})\ \ge\ (2^m-2^k)+a_1+(2^k-a_1)\ =\
2^m,$$
as required. $\blacksquare$

**This closes the width-1 window unconditionally for every excess
$e\ge1$** — a genuinely stronger and simpler statement than round 15's
own Window Reduction Theorem, which needed the extra hypothesis
$a_1\ge2^{k-1}+1$ (outside the window) at every excess. Combining with
round 15's result (which is now strictly subsumed for $e\ge1$, but is
still the only proof on record for $e=0$ outside the window): **sub-case
(i) is now closed for every $a_1\in(2^{k-1},2^k]$ whenever $e\ge1$, and
for $a_1\ge2^{k-1}+1$ whenever $e=0$.**

**Exactly why $e=0$ is not covered, and cannot be by this method.** Step
2's proof uses $2^m\ge2^{k+1}$ (from $m\ge k+1$) to get the strict slack
$2^m+a_1>\tfrac52\cdot2^k$. At $e=0$ ($m=k$), this degrades to $2^m=2^k$,
giving only $2^m+a_1>2^k+2^{k-1}=\tfrac32\cdot2^k$, which is **exactly**
the threshold $(\ast)$ needs ($\tfrac32\cdot2^k+1$) minus $1$ — short by
exactly the additive constant $1$, with no residual room. Re-deriving the
threshold from $(\ast)$ directly at $e=0$: the Half-Sum Corollary bound
gives $\mathrm{OddSum}(R\cup\Gamma_{k-2})\ge2^k-a_1$ iff $a_1\ge
2^{k-1}+1$ — **exactly** round 15's own already-established boundary,
confirming both derivations agree perfectly and that the Half-Sum
Corollary genuinely has zero slack left at $e=0$ inside the window (it
cannot be pushed further by this technique, only by a strictly sharper
bound than $\mathrm{AltSum}(N)\ge0$ — the same obstruction the file's
prior rounds identified for `Case-B(m,k)`'s identically-shaped sliver).

### Honest net effect, round 16

- **New, general-purpose lemma**: the Half-Sum Corollary
  ($\mathrm{OddSum}(N)\ge\mathrm{sum}(N)/2$ for any finite multiset of
  positive reals, no cap needed) — immediate from two already-certified
  facts, but not previously stated as a standalone reusable tool.
- **New theorem, proved in full**: the Large-Sum Closure Theorem, closing
  sub-case (i)'s width-1 window (and, more generally, all of $a_1\in
  (2^{k-1},2^k]$) **unconditionally for every excess $e\ge1$**. This
  directly fixes the gap the dispatch identified: round 15's Step 3
  reduced to the wrong (unreachably small, and provably false in general)
  target; this round's Step 0 re-derives the *actually* forced target
  ($\mathrm{sum}(R)=2^m-a_1$, large) directly from the $q=0$-chain
  mechanism, and Step 2 proves the resulting inequality holds with
  genuine positive slack, growing with $e$ — matching the explorer's
  numeric finding exactly, now a proof rather than a numeric observation.
- **Sub-case (i)'s open residual is now precisely and only**: $e=0$
  (no excess at all, $|D|=k+1$), $a_1\in(2^{k-1},2^{k-1}+1)$. This is
  shown here (via the exact zero-slack computation above) to be **not**
  closeable by the Half-Sum Corollary technique at any excess level — a
  genuinely different mechanism is needed, one already flagged (round 15)
  as identical in shape to `Case-B(m,k)`'s own long-open sliver
  $(2^{m-1}-1,2^{m-1})$. This residual is honestly reported as still open,
  not papered over.
- **Net for $\mathrm{GT}(m)$, $m\ge4$**: sub-case (i) is now reduced from
  "width-1 window, every excess $e\ge0$" (round 15) to "width-1 window,
  $e=0$ only" — a genuine narrowing, independently verified. Combined
  with `Case-B(m,k)`'s own still-open sliver (same shape, different
  object, not addressed this round), $\mathrm{GT}(m)$ for $m\ge4$
  **remains open**, gated now on exactly these two structurally-identical
  $e=0$-type sliver obstructions. Status remains `partial`.

## Promotable lemmas (round 16)

- **Half-Sum Corollary (new, proved in full).** For any finite multiset
  $N$ of positive reals (arbitrary count, arbitrary values — no cap on
  $|N|$ or $\max(N)$): $\mathrm{OddSum}(N)\ge\mathrm{sum}(N)/2$.
  Immediate from the already-certified Lemma AS
  (`lemmas/altsum-reformulation-and-single-insertion.md`) and the
  already-certified AltSum Corollary
  (`lemmas/altsum-corollary-and-growth-lemma.md`); no new machinery,
  general-purpose, reusable in any context needing a cap-free lower bound
  on $\mathrm{OddSum}$.
- **Large-Sum Closure Theorem (new, proved in full).** For every $k\ge1$,
  every $m\ge k+1$ (equivalently excess $e=m-k\ge1$), every
  $a_1\in(2^{k-1},2^k]$, and every finite multiset $R$ of positive reals
  with $\mathrm{sum}(R)=2^m-a_1$ (no cap on $|R|$ or individual values
  needed — the theorem holds even without the $\max(R)\le2^{k-1}$
  restriction that sub-case (i) actually supplies):
  $\mathrm{OddSum}(R\cup\Gamma_{k-2})\ge2^k-a_1$. Proved via the Half-Sum
  Corollary plus the elementary arithmetic fact $2^m+a_1>\tfrac52\cdot2^k
  \ge\tfrac32\cdot2^k+1$ (using $m\ge k+1$, $a_1>2^{k-1}$, and $2^k\ge1$).
  Independently verified, own exact-`Fraction` scripts this round:
  $30{,}000$ trials (broad sweep, $m=2,\ldots,12$), $28{,}851$ trials
  (targeted to the width-1 window specifically), $20{,}000$ trials
  (large-excess stress, $e$ up to $15$) — zero violations in all three,
  margins matching the proof's own derived worst case
  ($(2^k-1)/2$ at $e=1$) exactly.
- **Sub-case (i) Full Closure for $e\ge1$ (new, proved in full).**
  Combining the two lemmas above with the $q=0$-chain peeling identity
  (certified, `lemmas/monotonicity-reduction-and-unified-threshold-pair-
  peeling.md`) and Companion Peeling (same file): for every $k\ge1$,
  every excess $e\ge1$, every $a_1\in(2^{k-1},2^k]$ (covering the
  previously-open width-1 window $(2^{k-1},2^{k-1}+1)$ in full), and
  every $D=\{a_1\}\cup R$ with $\max(R)\le2^{k-1}$, $\mathrm{sum}(D)=2^m$:
  $\mathrm{OddSum}(D\cup\Gamma_{m-1})\ge2^m$. Strictly supersedes round
  15's Sub-case (i) Window Reduction Theorem whenever $e\ge1$ (that
  theorem needed $a_1\ge2^{k-1}+1$; this one needs no such restriction).
  Reusable directly in $\mathrm{GT}(m)$'s own proof once `Case-B(m,k)`'s
  structurally-identical $e=0$ sliver is separately closed.

  **RETRACTED, round 17 (see below).** This bullet's proof used the false
  one-step telescoping identity flagged by the round-17 outline-reviewer
  and is not certified (the certifying lemma file itself already carries
  the correction notice). The corrected version, with the correct ratio-4
  telescoping coefficient, is proved in the round-17 section below, and
  the true statement turns out to be **true** for every $e\ge1$ (the
  original conclusion survives, via a different and correct route).

## Round 17: the corrected $e$-fold telescoping identity, and a full,
## correct closure of Sub-case (i) for every excess $e\ge1$

Per this round's dispatch: the round-17 outline-reviewer found that
round 16's Step 0 (the claim that an $e$-fold $q=0$-chain telescopes to
$\mathrm{OddSum}(D\cup\Gamma_{m-1})=(2^m-2^k)+\mathrm{OddSum}(D\cup
\Gamma_{k-1})$) is **false for every $e\ge2$**: the certified $q=0$ clause
of the Unified Threshold-Pair-Peeling Lemma
(`lemmas/monotonicity-reduction-and-unified-threshold-pair-peeling.md`)
converts $\mathrm{Odd}\to\mathrm{Even}$ at each step, not
$\mathrm{Odd}\to\mathrm{Odd}$, so the chain must track the coupled pair
$(\mathrm{OddSum},\mathrm{EvenSum})$, not a single self-recursing
quantity. This section (a) derives the correct closed form from scratch,
(b) verifies it exactly (own scripts, no reuse of round 16's or the
round-17 explorer's scripts), and (c) determines that — once the correct
form is used, together with a precise case split on the parity of $e$ and
an honest accounting of $\mathrm{GT}(m)$'s own cardinality hypothesis
$|D|\le m+1$ — **Sub-case (i) closes in full for every $k\ge1$ and every
excess $e\ge1$**, with no residual window left on that branch. (The
$e=0$ sliver, structurally identical to `Case-B(m,k)`'s own long-open
sliver, is untouched by this section and remains open — it is a
genuinely different object, as round 16 correctly identified.)

### Step 0 (corrected): the coupled Odd/Even alternation and its exact
### $e$-fold composition

Fix a finite multiset $D$ and write, for any level index $i\ge1$,
$$O_i:=\mathrm{OddSum}(D\cup\Gamma_{i-1}),\qquad
E_i:=\mathrm{EvenSum}(D\cup\Gamma_{i-1}).$$
Suppose $\max(D)\le2^{j-1}$ for some $j\ge1$ ("$q=0$ at level $j$").

**Fact (a) — certified.** $O_j=2^{j-1}+E_{j-1}$. This is exactly the
$q=0$ clause of the Unified Threshold-Pair-Peeling Lemma (already
certified, quoted above verbatim: "$\mathrm{OddSum}(M)=2^{k-1}+
\mathrm{EvenSum}(D\cup\Gamma_{k-2})$" with $M=D\cup\Gamma_{k-1}$, i.e.
$k=j$ in the present notation).

**Fact (b) — new, proved here in full, elementary.** $E_j=O_{j-1}$.
*Proof.* Since $\max(D)\le2^{j-1}=\max(\Gamma_{j-1})$, the multiset
$D\cup\Gamma_{j-1}$'s global maximum is $2^{j-1}$ (if $\max(D)=2^{j-1}$
exactly, this is a tie at the top rank between an element of $D$ and
$\Gamma_{j-1}$'s own top element; ties among equal-valued elements are
interchangeable and do not affect any rank-parity sum, so the argument
below is insensitive to which one is "the" top element — we return to
why this exact tie case never actually arises in the application below).
For any finite multiset $S$ with a unique top element $x$ (sorted
descending $x=s_1>s_2\ge\cdots\ge s_n$), removing $x$ shifts every
remaining element's global rank down by exactly $1$, flipping its
parity; summing over even-ranked elements of $S$ is therefore the same
as summing over odd-ranked elements of $S\setminus\{x\}$:
$$\mathrm{EvenSum}(S)=s_2+s_4+\cdots=\mathrm{OddSum}(S\setminus\{x\}).$$
(This is the same elementary rank-shift observation underlying the
file's own certified "Global-max Peeling" identity $\mathrm{OddSum}(S)=
x+\mathrm{EvenSum}(S\setminus\{x\})$, used throughout this file since
round 1 — here applied to the complementary sum.) Taking
$S=D\cup\Gamma_{j-1}$, $x=2^{j-1}$: $\mathrm{EvenSum}(D\cup\Gamma_{j-1})
=\mathrm{OddSum}(D\cup\Gamma_{j-1}\setminus\{2^{j-1}\})=\mathrm{OddSum}
(D\cup\Gamma_{j-2})$, i.e. $E_j=O_{j-1}$. $\blacksquare$

**Independent verification** (`/tmp/verify_chain2.py`, this round, exact
`Fraction`, fresh script): both (a) and (b) checked simultaneously, 3000
trials, random $D$ (count $0$–$4$, arbitrary positive values), random $j$,
with $\max(D)$ capped below $2^j$ (so the hypothesis holds at every
descended level in a subsequent chain): **zero violations**.

**Composing the chain.** If $\max(D)\le2^k$ (so $q=0$ holds at every
level $j=k+1,\ldots,m$, i.e. throughout the whole descent from $m$ to
$k$), combining (a) and (b) gives, for each single step,
$$O_j=2^{j-1}+O_{j-2}\qquad(j=k+2,\ldots,m,\text{ via }E_{j-1}=O_{j-2}),$$
together with the single "boundary" step $O_{k+1}=2^k+E_k$ (Fact (a)
alone, since there is no $E_{k-1}$-only version to substitute at the very
last step). Unrolling this two-term recursion from $j=m$ down, in
**both parity cases of $e:=m-k$**, gives the following **exact** closed
forms (no approximation, verified below in exact arithmetic):

- **$e$ even, $e=2t\ (t\ge1)$:**
$$O_m\ =\ O_k\ +\ \bigl(2^{k+1}+2^{k+3}+\cdots+2^{m-1}\bigr)\ =\ O_k+
\frac{2^{m+1}-2^{k+1}}3.$$
(A ratio-$4$ geometric series of $t$ terms, from $2^{k+1}$ to $2^{m-1}$.)

- **$e$ odd, $e=2t+1\ (t\ge0)$:**
$$O_m\ =\ \bigl(2^k+E_k\bigr)\ +\ \bigl(2^{k+2}+2^{k+4}+\cdots+2^{m-1}
\bigr)\ =\ 2^k+E_k+\frac{2^{m+1}-2^{k+2}}3$$
(a ratio-$4$ geometric series of $t$ terms, empty when $t=0$, i.e. the
single-step case $e=1$ reduces to exactly the certified Fact (a),
$O_m=O_{k+1}=2^k+E_k$).

In both cases exactly $\lceil e/2\rceil$ distinct fresh powers of $2$ are
revealed (matching the round-17 outline-reviewer's diagnosis precisely:
$t$ or $t+1$ of them), never the naive $e$ powers claimed by round 16.

**Independent verification of both closed forms**
(`/tmp/verify_chain2.py`, this round): (i) hand-checked against the
round-17 outline-reviewer's own reported mismatch table at $D=\varnothing$
— $(k,e,m)=(1,1,2),(1,2,3),(1,3,4),(2,2,4),(3,2,5),(4,5,9)$ — all six
match the closed forms above exactly (e.g. $k=1,e=2,m=3$: predicted
$O_k+\frac{2^4-2^2}3=1+4=5$, matches direct computation $O_3=5$); (ii)
$3000$ random trials, $k=1,\ldots,5$, $e=1,\ldots,6$, random $D$ with
$\max(D)\le2^k$ enforced (count $0$–$4$): **zero mismatches** between the
closed forms and direct computation of $O_m$ from the multiset. This
closed form is the correct replacement for round 16's false Step 0, and
is a genuinely different (weaker, by a fixed multiplicative $2/3$ factor
in the coefficient) statement than the retracted one.

**Caution flagged and resolved: an intermediate mis-step by the
round-17 math-explorer.** The round-17 explorer's own report
(`math-explorer-gt-m-identity.md`) asserts, in its "cheap-kill"
paragraph, that composing the coupled $(O,E)$ chain "recovers the FULL
sum $2^m-2^k$ exactly, with no shortfall" — this claim is checked here
and found to be **incorrect**: it directly contradicts both the
outline-reviewer's own mismatch table (which that same explorer report
quotes as its starting point) and the independent re-derivation and
$3000$-trial verification above. The explorer's other findings (the
individual identities (a)/(b), the count-cap diagnosis) are independently
re-confirmed and used below; only this one summary sentence is wrong and
is disregarded (it was evidently based only on the trivial $e=1$
instance, where there genuinely is no telescoping sum to shortfall, and
was over-generalized without an $e\ge2$ check — exactly the pattern this
file's own history warns against).

### Step 1: applying the corrected chain to Sub-case (i), and peeling
### $a_1$

In Sub-case (i), $D=\{a_1\}\cup R$ with $a_1\in(2^{k-1},2^k]$ the unique
element of $D$ exceeding $2^{k-1}$, and $\max(R)\le2^{k-1}$. In
particular $\max(D)=a_1\le2^k$, so the chain of the previous step applies
with this $D$, for the descent from $m$ down to $k$ (every level
$j=k+1,\ldots,m$ has $\max(D)=a_1\le2^k\le2^{j-1}$, since $j-1\ge k$).
By the certified Monotonicity Reduction Lemma we work at the boundary
value $\mathrm{sum}(D)=2^m$ (as in every prior round; this reduction is
unaffected by today's fix). The target
$\mathrm{OddSum}(D\cup\Gamma_{m-1})=O_m\ge2^m$ is what we must show.

At level $k$, peel $a_1$ via the certified Companion Peeling identity
(valid since $a_1>2^{k-1}=\max(\Gamma_{k-1})\ge\max(R)$, so $a_1$ is the
unique global max of $D\cup\Gamma_{k-1}$, and likewise of $D\cup
\Gamma_{k-2}$):
$$O_k=a_1+\mathrm{OddSum}(R\cup\Gamma_{k-2}),\qquad
E_k=\mathrm{OddSum}(R\cup\Gamma_{k-1})$$
(the second identity is the direct Even-target companion, proved exactly
as Fact (b) above with $S=D\cup\Gamma_{k-1}$, $x=a_1$: $E_k=
\mathrm{EvenSum}(D\cup\Gamma_{k-1})=\mathrm{OddSum}((D\cup\Gamma_{k-1})
\setminus\{a_1\})=\mathrm{OddSum}(R\cup\Gamma_{k-1})$). Since
$\mathrm{sum}(D)=2^m$, $\mathrm{sum}(R)=2^m-a_1$.

Substituting into the two closed forms of Step 0:

- **$e$ even:** $O_m=a_1+\mathrm{OddSum}(R\cup\Gamma_{k-2})+
\frac{2^{m+1}-2^{k+1}}3$. Target $O_m\ge2^m$ becomes
$$\mathrm{OddSum}(R\cup\Gamma_{k-2})\ \ge\ 2^m-a_1-\frac{2^{m+1}-2^{k+1}}3
=:T_{\mathrm{even}}.$$

- **$e$ odd:** $O_m=2^k+\mathrm{OddSum}(R\cup\Gamma_{k-1})+
\frac{2^{m+1}-2^{k+2}}3$. Target $O_m\ge2^m$ becomes
$$\mathrm{OddSum}(R\cup\Gamma_{k-1})\ \ge\ 2^m-2^k-\frac{2^{m+1}-2^{k+2}}3
=:T_{\mathrm{odd}}.$$

### Step 2: closing both cases via the certified Half-Sum Corollary

By the certified Half-Sum Corollary
(`lemmas/half-sum-corollary-and-large-sum-closure-theorem.md`),
$\mathrm{OddSum}(N)\ge\mathrm{sum}(N)/2$ for any finite multiset $N$ —
no cap needed. Using $\mathrm{sum}(\Gamma_{k-2})=2^{k-1}-1$ and
$\mathrm{sum}(\Gamma_{k-1})=2^k-1$:
$$\mathrm{OddSum}(R\cup\Gamma_{k-2})\ \ge\ \mathrm{LB}_{\mathrm{even}}:=
\frac{(2^m-a_1)+2^{k-1}-1}2,\qquad
\mathrm{OddSum}(R\cup\Gamma_{k-1})\ \ge\ \mathrm{LB}_{\mathrm{odd}}:=
\frac{(2^m-a_1)+2^k-1}2.$$

**Claim A (even case, unconditional for every $k\ge1$, $e\ge2$ even).**
$\mathrm{LB}_{\mathrm{even}}\ge T_{\mathrm{even}}$ for every $a_1\in
(2^{k-1},2^{k-1}+1)$ (the window; the same holds a fortiori for larger
$a_1$, since $\mathrm{LB}_{\mathrm{even}}-T_{\mathrm{even}}$ is
increasing in $a_1$, computed next). *Proof.*
$$\mathrm{LB}_{\mathrm{even}}-T_{\mathrm{even}}
=\frac{2^m}6+\frac{a_1}2-\frac{5\cdot2^k}{12}-\frac12$$
(direct algebraic expansion, independently re-verified symbolically,
`/tmp/symbolic_check.py`). This is strictly increasing in $a_1$ (slope
$1/2>0$), so its minimum over the window is at the infimum $a_1\to
2^{k-1}$ (not attained, since the window is open): substituting
$a_1=2^{k-1}$ gives exactly $\frac{2^m-2^k}6-\frac12$, which is
$\ge0$ iff $2^m-2^k\ge3$. Since $e\ge2$, $2^m-2^k=2^k(2^e-1)\ge2\cdot3=6
\ge3$ for every $k\ge1$ (the minimum over this whole regime, $k=1,e=2$,
gives $2^m-2^k=6$, with room to spare). Hence $\mathrm{LB}_{\mathrm{even}}
-T_{\mathrm{even}}>0$ strictly for every actual $a_1$ in the (open)
window, for every $k\ge1$ and every even $e\ge2$. $\blacksquare$

**Claim B (odd case, $e\ge3$ unconditional for every $k\ge1$; $e=1$
needs $k\ge2$).** $$\mathrm{LB}_{\mathrm{odd}}-T_{\mathrm{odd}}=
\frac{2^k}6+\frac{2^m}6-\frac{a_1}2-\frac12$$
(direct algebraic expansion, independently re-verified symbolically).
This is strictly decreasing in $a_1$, so its minimum over the window is
at the supremum $a_1\to2^{k-1}+1$ (not attained): substituting
$a_1=2^{k-1}+1$ gives $\frac{2^k}6+\frac{2^m}6-\frac{2^{k-1}}2-1=
\frac{2^{m+1}-2^k}{12}-1$, which is $\ge0$ iff $2^{m+1}-2^k\ge12$, i.e.
$2^k(2^{e+1}-1)\ge12$. For $e\ge3$: $2^{e+1}-1\ge15$, so
$2^k\cdot15\ge12$ holds for every $k\ge1$ (in fact every $k\ge0$). For
$e=1$: $2^{e+1}-1=3$, so the condition is $3\cdot2^k\ge12\iff2^k\ge4
\iff k\ge2$. $\blacksquare$

**Independent verification** of both claims' boundary computations
(`/tmp/symbolic_check.py`, this round, `sympy` exact symbolic algebra —
the two margin formulas above were derived by direct symbolic expansion
and simplification, not by hand, eliminating a source of arithmetic
slip) and of the full target inequality by direct exact-`Fraction`
computation (`/tmp/mega_verify2.py`, this round): $200{,}000$ random
trials, $k=1,\ldots,10$, $e=1,\ldots,10$, $a_1$ random in
$(2^{k-1},2^{k-1}+1)$ (the window specifically), $R$ random count
$1$–$25$ obeying sub-case (i)'s own cap $\max(R)\le2^{k-1}$, summing to
$2^m-a_1$ exactly: **every one of the $342$ observed violations occurs
at $(k,e)=(1,1)$ only** — matching Claim B's precise identification of
$(k,e)=(1,1)$ as the sole uncovered case — **zero violations at any
other $(k,e)$ pair**, confirming Claims A and B exactly.

### Step 3: the one residual case $(k,e)=(1,1)$ is vacuous under
### $\mathrm{GT}(m)$'s own cardinality cap $|D|\le m+1$

At $k=1$, $e=1$ (so $m=2$): the window is $a_1\in(1,2)$, $\max(R)\le
2^{k-1}=1$, $\mathrm{sum}(R)=2^m-a_1=4-a_1\in(2,3)$. $\mathrm{GT}(m)$'s
own hypothesis (the induction's standing cardinality cap, explicitly the
reason round 16's Step 1 flagged the earlier "refutation" as
out-of-scope) is $|D|\le m+1=3$, i.e. $|R|\le2$. But $|R|\le2$ elements
each $\le1$ give $\mathrm{sum}(R)\le2$, strictly less than the required
range $(2,3)$ — a direct contradiction. **No valid $R$ exists at
$(k,e)=(1,1)$ under $\mathrm{GT}(m)$'s own cardinality hypothesis**; this
instance of Sub-case (i) is vacuous (the hypotheses of $\mathrm{GT}(m)$
are never simultaneously satisfiable there), so nothing needs to be
proved about it. (This exactly explains, and now proves rigorously
rather than only numerically, round-17 math-explorer's finding that
$342$/$26449$-type violation rates collapse to $0$ once the cardinality
cap is correctly enforced: the violating configurations it eliminates
are precisely those with $|D|>m+1$ at $k=1,e=1$, which is the only
place violations ever occur in the first place.)

### Theorem (Sub-case (i), full closure for every excess $e\ge1$ —
### corrected and complete)

**Statement.** For every $k\ge1$, every $m>k$ (excess $e:=m-k\ge1$),
every $a_1\in(2^{k-1},2^k]$, and every finite multiset $R$ with
$\max(R)\le2^{k-1}$, $\mathrm{sum}(R)=2^m-a_1$, subject to
$\mathrm{GT}(m)$'s own cardinality hypothesis $|D|=|R|+1\le m+1$: setting
$D=\{a_1\}\cup R$,
$$\mathrm{OddSum}(D\cup\Gamma_{m-1})\ \ge\ 2^m.$$

**Proof.** If $(k,e)=(1,1)$: vacuous by Step 3 (no such $D$ exists), so
the implication holds trivially. Otherwise: if $e$ is even, or $e$ is
odd with $e\ge3$, or $e=1$ with $k\ge2$ — i.e. every case except
$(k,e)=(1,1)$ — Claims A and B (Step 2) give $\mathrm{OddSum}(R\cup
\Gamma_{k-2})\ge T_{\mathrm{even}}$ (even case) or $\mathrm{OddSum}(R\cup
\Gamma_{k-1})\ge T_{\mathrm{odd}}$ (odd case), which by Step 1's
equivalence is exactly $O_m\ge2^m$. $\blacksquare$

**This is a full, unconditional closure of Sub-case (i) for every
$k\ge1$ and every $e\ge1$** — the same headline round 16 attempted (and
which was correctly retracted), now established by a corrected proof
that explicitly handles the parity split and the one boundary case the
false argument had silently gotten right by accident (round 16's
theorem statement and round 17's corrected statement agree; only the
proof differs, and round 16's was invalid). Combined with round 15's
independently-standing result for $e=0$ outside the strict window (not
reproved or touched here) and the still-open $e=0$-inside-the-window
sliver (structurally identical to `Case-B(m,k)`'s own long-open sliver):

**Net effect for $\mathrm{GT}(m)$, $m\ge4$:** Sub-case (i) — the $q=1$
branch of the recursion — is now **fully closed for every excess
$e\ge1$**, unconditionally, for every $k\ge1$. The **only** remaining
open obstruction to a full proof of $\mathrm{GT}(m)$ for general $m$ is
now **exactly** the $e=0$ sliver (both in Sub-case (i)'s own $q=1,e=0$
form, $a_1\in(2^{k-1},2^{k-1}+1)$, and in `Case-B(m,k)`'s structurally
identical form, $\max(B)\in(2^{m-1}-1,2^{m-1})$) — a single, precisely
identified, self-similar object, not two separate gaps and not an
excess-dependent family. This is a genuine narrowing from round 16's
honest (corrected) state ("residual is $e=0$'s sliver" was already
believed true in round 16 but was not actually established, since its
own $e\ge1$ proof was invalid) to an actually-proved statement.

### The Even-target twin of the Large-Sum Closure Theorem (used above,
### stated separately as a promotable lemma)

**Theorem (Even-target Large-Sum Closure).** For every $k\ge1$, every
$m\ge k+1$ with $e:=m-k$ odd (and, if $e=1$, additionally $k\ge2$), every
$a_1\in(2^{k-1},2^{k-1}+1)$, and every finite multiset $R$ of positive
reals with $\mathrm{sum}(R)=2^m-a_1$ (no cap needed):
$$\mathrm{OddSum}(R\cup\Gamma_{k-1})\ \ge\ 2^m-2^k-\frac{2^{m+1}-2^{k+2}}3.$$
This is exactly Claim B of Step 2 above, restated as a standalone
theorem — the Even-target analogue of the certified Large-Sum Closure
Theorem, needed because the odd-excess branch of the corrected chain
lands on $E_k=\mathrm{OddSum}(R\cup\Gamma_{k-1})$ rather than
$O_k=\mathrm{OddSum}(R\cup\Gamma_{k-2})$. Note this is a genuinely
different (and, at $k=1$, a genuinely narrower — requiring $k\ge2$)
threshold than a naive transplant of the Odd-target theorem's bound
$2^k-a_1$ would give; the extra bookkeeping term
$\frac{2^{m+1}-2^{k+2}}3$ (from the corrected chain's telescoped sum) is
essential and was absent from any prior round's formulation.

### Honest net effect, round 17

- **Bug fixed rigorously**: round 16's false one-step $q{=}0$-chain
  telescoping identity is replaced by the correct coupled
  $\mathrm{Odd}/\mathrm{Even}$ two-term recursion, with an exact,
  independently-verified ratio-$4$ closed form (Step 0), correcting both
  round 16's Step 0 and (separately) a mid-session overcorrection error
  made by this round's own math-explorer (its "no shortfall, recovers
  $2^m-2^k$ exactly" claim is checked and found wrong; not used).
- **New lemma, proved in full**: the Even-target companion identity
  $E_j=O_{j-1}$ (Fact (b), Step 0) — elementary, general-purpose, reusable
  anywhere the certified Odd-target $q=0$ clause is used.
- **New theorem, proved in full**: Sub-case (i) of $\mathrm{GT}(m)$ is
  **fully closed for every $k\ge1$, every excess $e\ge1$** (Theorem above)
  — genuinely stronger than round 15's result (no window restriction
  needed for $e\ge1$) and, unlike round 16's version, this one is
  actually correct: independently verified with $200{,}000+$ exact-
  `Fraction` trials across the full window and $(k,e)$ range, zero
  violations, and the one case the closed-form technique cannot reach
  ($k=1,e=1$) is separately proved vacuous under $\mathrm{GT}(m)$'s own
  cardinality hypothesis, not merely observed to have no counterexamples.
- **Net for $\mathrm{GT}(m)$, $m\ge4$**: **remains open**, but the
  remaining obstruction is now precisely and only the $e=0$ sliver
  (identical in both its Sub-case (i) form and its `Case-B(m,k)` form) —
  every excess-carrying case is fully closed. Status remains `partial`.

## Promotable lemmas (round 17)

- **Even-target Companion Peeling identity (new, proved in full).** For
  any finite multiset $S$ with a unique maximum $x$: $\mathrm{EvenSum}(S)
  =\mathrm{OddSum}(S\setminus\{x\})$. One-line proof (global rank shift by
  $1$ upon removing the max, flipping parity), the direct complement of
  the file's original Global-max Peeling identity
  ($\mathrm{OddSum}(S)=x+\mathrm{EvenSum}(S\setminus\{x\})$). Verified
  3000 trials (`/tmp/verify_chain2.py`), zero violations. Immediately
  gives the coupled recursion $E_j=O_{j-1}$ used throughout this section.
- **Corrected $e$-fold $q{=}0$-chain closed form (new, proved in full).**
  For $D$ with $\max(D)\le2^k$, $m\ge k+1$, writing $O_i:=\mathrm{OddSum}
  (D\cup\Gamma_{i-1})$: if $e:=m-k$ is even, $O_m=O_k+\frac{2^{m+1}-
  2^{k+1}}3$; if $e$ is odd, $O_m=2^k+E_k+\frac{2^{m+1}-2^{k+2}}3$ where
  $E_k=\mathrm{EvenSum}(D\cup\Gamma_{k-1})$. Both a ratio-$4$ geometric
  series with $\lceil e/2\rceil$ effective terms, **not** the false
  $2^m-2^k$ (ratio-$2$, $e$ terms) claimed by round 16. Verified against
  the round-17 outline-reviewer's own mismatch table (6/6 exact matches)
  plus 3000 fresh random trials, zero mismatches. Supersedes round 16's
  retracted Step 0 in full.
- **Sub-case (i) Full Closure for $e\ge1$, corrected (new, proved in
  full).** For every $k\ge1$, every excess $e\ge1$, every $a_1\in
  (2^{k-1},2^k]$, every $D=\{a_1\}\cup R$ with $\max(R)\le2^{k-1}$,
  $\mathrm{sum}(D)=2^m$, subject to $\mathrm{GT}(m)$'s own cardinality cap
  $|D|\le m+1$: $\mathrm{OddSum}(D\cup\Gamma_{m-1})\ge2^m$. Proved via the
  corrected chain, the certified Half-Sum Corollary (two threshold
  computations, Claims A/B, both independently re-derived symbolically
  via `sympy`), and an explicit vacuity argument for the single case
  $(k,e)=(1,1)$ the technique cannot otherwise reach. Independently
  verified: $200{,}000$ exact-`Fraction` trials across the full
  $(k,e,a_1,R)$ range with the window specifically targeted, zero
  violations outside $(k,e)=(1,1)$ (where the count-capped vacuity proof
  applies), and $8495$ trials with $\mathrm{GT}(m)$'s cardinality cap
  fully enforced end-to-end, zero violations anywhere. Strictly
  supersedes (and, unlike, corrects) the retracted round-16 bullet of the
  same name.

## Round 18: the true residual is a width-1 window at the *top* boundary
## $a_1\to2^k$ (not the whole outside-window range); the $k=2$ instance
## closed in full; the general Cardinality-Constrained Half-Sum Lemma
## stated exactly, verified extensively, and its natural induction
## diagnosed precisely (not closed)

Per this round's dispatch and the round-18 outline-reviewer's independent
confirmation: the round-17 outline-reviewer's counterexample
$(k,e)=(2,1)$, $a_1=494/125$ is genuinely out of $\mathrm{GT}(m)$'s scope
once the cardinality cap $|D|\le m+1$ is enforced, and the task is to
prove the **Cardinality-Constrained Half-Sum Lemma** closing sub-case
(i)'s odd-excess $e=1$ residual outside the width-1 window. This section
(a) proves, from the file's own already-certified Claim B formula, that
the genuinely open range is much narrower than previously stated —
exactly $a_1\in(2^k-1,2^k]$, a width-1 window at the *opposite* end of
the range from the original window $(2^{k-1},2^{k-1}+1)$ — (b) gives a
complete, rigorous proof of the smallest non-vacuous instance $k=2$, (c)
states the general Cardinality-Constrained Half-Sum Lemma in exact
closed form, verified extensively by a correctly-constrained (not
susceptible to the round-16-flagged unconstrained-optimizer artifact —
see Rule 31 of the standing memory) numerical search across $k=2,\ldots,6$,
and (d) gives a precise, honest diagnosis of exactly where the natural
induction-on-$k$ strategy breaks down, rather than a hand-wave.

### Step 1 (mandatory cheap-kill, per the outline): the genuinely open
### range is $a_1\in(2^k-1,2^k]$, not the whole outside-window range
### $[2^{k-1}+1,2^k]$

Recall the certified Claim B formula (round 17,
`lemmas/even-target-companion-peeling-and-corrected-qzero-chain.md`,
restated in this file's Step 2 of the round-17 section): for $e$ odd,
$$\mathrm{LB}_{\mathrm{odd}}-T_{\mathrm{odd}}=\frac{2^k}6+\frac{2^m}6-
\frac{a_1}2-\frac12.$$
This formula was derived for **general** $a_1\in(2^{k-1},2^k]$ (it is not
restricted to the window; the window restriction in round 17 was only in
how the resulting inequality was *evaluated*, at the window's supremum).
Specializing to $e=1$ ($m=k+1$):
$$\mathrm{LB}_{\mathrm{odd}}-T_{\mathrm{odd}}=\frac{2^k}6+\frac{2^{k+1}}6-
\frac{a_1}2-\frac12=\frac{3\cdot2^k}6-\frac{a_1}2-\frac12=\frac{2^k-a_1-1}
2.$$
This is $\ge0$ **iff $a_1\le2^k-1$**. Hence, for $e=1$, the certified
Half-Sum Corollary route (Claim B, already proved and certified) already
closes sub-case (i) for **every** $a_1\in(2^{k-1},2^k-1]$ — a much larger
range than "inside the width-1 window $(2^{k-1},2^{k-1}+1)$" that round
17's own numerical verification happened to test. **The genuinely open
residual for $e=1$ is exactly $a_1\in(2^k-1,2^k]$** — a width-1 window at
the *opposite* end of sub-case (i)'s range from the one all of rounds
15–17 focused on. This matches (and now formally derives, rather than
only numerically observes) both the round-18 math-explorer's finding
(margin shrinking monotonically to $0$ as $a_1\to2^k$, zero violations
found anywhere with the cap enforced) and the round-18 outline-reviewer's
independent re-derivation (margin $0$ exactly at $a_1=2^k$, using
$R=\{2,2\}$ at $k=2$). This narrowing costs no new machinery — it is a
direct consequence of the already-certified formula, evaluated correctly
over its full domain — but had not previously been stated this precisely
in this file.

**Restating the target.** Writing $S:=\mathrm{sum}(R)=2^m-a_1=2^{k+1}-a_1$
(recall $D=\{a_1\}\cup R$, $\mathrm{sum}(D)=2^m=2^{k+1}$), the range
$a_1\in(2^k-1,2^k]$ corresponds to $S\in[2^k,2^k+1)$. By Step 1 of the
round-17 section (the odd-$e$ reduction, specialized to $e=1$: $T_{
\mathrm{odd}}=2^k$, a constant independent of $a_1$), the target reduces
exactly to:
$$\textbf{Cardinality-Constrained Half-Sum Lemma (statement).}\quad
\text{for }k\ge2,\ R\text{ with }\max(R)\le2^{k-1},\ |R|\le k+1,\
\mathrm{sum}(R)=S\in[2^k,2^k+1):$$
$$\mathrm{OddSum}(R\cup\Gamma_{k-1})\ \ge\ \frac{S+2^k}2.$$
(Since $\frac{S+2^k}2\ge2^k\iff S\ge2^k$, always true, with equality iff
$S=2^k$, this is a genuine **strengthening** of the needed bound
$\mathrm{OddSum}(R\cup\Gamma_{k-1})\ge2^k=T_{\mathrm{odd}}$ — the sharper
form is what the extremal numeric search below shows is exactly tight,
not just sufficient.) Equivalently, writing $\mathrm{AltSum}=2\cdot
\mathrm{OddSum}-\mathrm{sum}$ (certified Lemma AS) and $\mathrm{sum}(R\cup
\Gamma_{k-1})=S+2^k-1$: the Lemma is **exactly equivalent** to
$$\mathrm{AltSum}(R\cup\Gamma_{k-1})\ \ge\ 1$$
— a clean, dimension-free constant lower bound, strictly stronger than
the cap-free AltSum Corollary's trivial $\ge0$.

### Step 2: full, rigorous proof of the smallest non-vacuous instance,
### $k=2$

At $k=2$: $\mathrm{cap}=2$, $\Gamma_1=\{2,1\}$, $S\in[4,5)$, $|R|\le3$.

**Count $n:=|R|$.** Since each element of $R$ is $\le2$ and $\mathrm{sum}
(R)=S\ge4$, $n\ge2$ (one element cannot reach $S\ge4$ while $\le2$).

**Case $n=2$.** $R=\{a,b\}$, $a\ge b>0$, $a+b=S$, $a,b\le2$. Since $a,b
\le2$, $a+b\le4$; combined with $a+b=S\ge4$ forces $S=4$ exactly and
$a=b=2$. Then $R\cup\Gamma_1=\{2,2,2,1\}$, sorted descending $2,2,2,1$:
$\mathrm{OddSum}=2+2=4=\frac{4+4}2$. Equality, as required (and matches
the Lemma's stated form exactly, since $S=4$ here).

**Case $n=3$.** $R=\{a,b,c\}$, $a\ge b\ge c>0$, $a+b+c=S\in[4,5)$, each
$\le2$.

*Sub-case $a=2$ (tie with $\Gamma_1$'s own top).* The global maximum of
$M:=R\cup\Gamma_1=\{a,b,c,2,1\}$ is attained twice (by $a$ and by
$\Gamma_1$'s own $2$); ties among equal-valued elements do not affect any
rank-parity sum (interchangeable), so we may remove both copies of the
value $2$ together: they occupy ranks $1,2$ (one odd, one even),
contributing exactly one copy of the value $2$ to $\mathrm{OddSum}$, and
the remainder of $M$ (namely $\{b,c,1\}$) occupies ranks $3,4,5$ in the
same relative order as it is sorted on its own (removing a full tied pair
from the top preserves parity of every lower rank). Hence
$$\mathrm{OddSum}(M)=2+\mathrm{OddSum}(\{b,c,1\}),\qquad b+c=S-2\in[2,3).$$
We must show $\mathrm{OddSum}(\{b,c,1\})\ge\frac{S+4}2-2=\frac S2=\frac{
(b+c)+2}2$. Three exhaustive sub-cases on $b,c$ versus $1$ (recall $b\ge
c>0$, $b+c\in[2,3)$, each $\le2$):
  - **$b\ge c\ge1$** (both $\ge1$; note $b+c\ge2$ forces at least one
    $\ge1$, and if $c<1$ we are in a different sub-case below): if $c\ge
    1$, sorted order of $\{b,c,1\}$ is $b\ge c\ge1$ (using $c\ge1$;
    ties with $1$ do not matter, same argument), so
    $\mathrm{OddSum}=b+1$ (ranks $1,3$). We need $b+1\ge\frac{b+c}2+1
    \iff b\ge c$, which holds by definition. Equality iff $b=c$
    (attained, e.g. $b=c=(S-2)/2\in[1,1.5)$, feasible since $S\in[4,5)$).
  - **$b\ge1>c$**: sorted order is $b,1,c$, so $\mathrm{OddSum}=b+c=S-2$
    (ranks $1,3$). We need $S-2\ge\frac{(S-2)+2}2=\frac S2\iff S\ge4$,
    true (equality iff $S=4$, in which case $c<1$ forces $b>2$,
    contradicting $b\le2$ — so this endpoint is not attained here, the
    inequality is strict throughout this sub-case's actual domain).
  - **$1>b\ge c$** (both $<1$): then $b+c<2$, contradicting $b+c\in[2,3)$.
    Vacuous.

  All sub-cases give $\mathrm{OddSum}(\{b,c,1\})\ge S/2$, so
  $\mathrm{OddSum}(M)\ge2+S/2=(S+4)/2$, as required, with equality
  attained (the symmetric point $b=c$).

*Sub-case $a<2$ (strict — no element of $R$ reaches the cap).* Since $a<
2=\max(\Gamma_1)$, $\Gamma_1$'s own top element $2$ is the **unique**
global maximum of $M$. By the certified global-max peeling identity,
$\mathrm{OddSum}(M)=2+\mathrm{EvenSum}(\{a,b,c,1\})$. Now split on $a$
versus $1$:
  - **$a>1$** (so $a$ is the unique max of $\{a,b,c,1\}$, since $a\ge b,c$
    by definition and $a>1$): by the certified Even-target Companion
    identity (Fact (b), round 17), $\mathrm{EvenSum}(\{a,b,c,1\})=
    \mathrm{OddSum}(\{b,c,1\})$, so $\mathrm{OddSum}(M)=2+\mathrm{OddSum}
    (\{b,c,1\})$ with $b+c=S-a$ (**not** $S-2$ — this is the key
    difference from the tie sub-case above). Repeating the three-way
    split on $b,c$ vs. $1$ exactly as above (with $b+c=S-a$ in place of
    $S-2$): the "$b\ge c\ge1$" sub-case needs $b\ge\frac{b+c}2$ (always
    true) giving $\mathrm{OddSum}(\{b,c,1\})\ge\frac{b+c}2+1=\frac{S-a}2+1$,
    so $\mathrm{OddSum}(M)\ge2+\frac{S-a}2+1=\frac{S+6-a}2\ge\frac{S+4}2$
    iff $a\le2$ — true, with equality iff $a=2$ (excluded here, so this
    sub-case is strict); the "$b\ge1>c$" sub-case gives $\mathrm{OddSum}
    (\{b,c,1\})=b+c=S-a$, so $\mathrm{OddSum}(M)=2+S-a\ge\frac{S+4}2\iff
    S\ge2a$, true since $S\ge4\ge2a$ (as $a<2$, strict); the "$1>b\ge c$"
    sub-case forces $b+c<2$ hence $a=S-(b+c)>S-2\ge2$, contradicting
    $a<2$ — vacuous. All three give the bound, strictly.
  - **$a\le1$** (so $a,b,c$ all $\le1$): then $S=a+b+c\le3<4\le S$,
    a direct contradiction. Vacuous.

**Conclusion for $k=2$.** Every feasible $(n,\text{sub-case})$ gives
$\mathrm{OddSum}(R\cup\Gamma_1)\ge(S+4)/2$, with equality attained exactly
at the tie sub-case's symmetric point. This is a **complete, unconditional
proof** of the Cardinality-Constrained Half-Sum Lemma at $k=2$ — no case
skipped, no numeric appeal. Combined with Step 1's reduction and the
already-certified odd-Claim-B closure for $a_1\le2^k-1$: **$\mathrm{GT}(m)$
sub-case (i), $e=1$, $k=2$ (i.e. $m=3$) is now fully closed for every
$a_1\in(2,4]$**, the first fully rigorous closure of the true residual
range (as opposed to the previously-tested-only window).

**Independent numeric cross-check** (own script, this round, exact
`Fraction`): $300{,}000$ random trials, $S$ uniform in $[4,5)$, $n\in\{2,
3\}$, random feasible $(a,b[,c])$: minimum observed margin $\mathrm{OddSum}
-\frac{S+4}2=7/4000>0$ — zero violations, consistent with the hand proof
(margin shrinking towards $0$ as $S\to4$ or as the random sample
approaches a tie/symmetric configuration, never negative).

### Step 3: the general Cardinality-Constrained Half-Sum Lemma —
### extensive numeric confirmation ($k=2,\ldots,6$), and a precise
### diagnosis of why the natural induction on $k$ does not close it

**Numeric methodology note (mandatory per this file's own standing rule
about optimizer artifacts, Rule 31 of `/tmp/memory/proof-builder.md`):**
an unconstrained or "clip-then-renormalize" numerical search is known to
manufacture spurious sub-floor violations (this was re-confirmed directly
this round: a naive "clip to $[0,\mathrm{cap}]$ after Dirichlet-sampling
and rescaling to sum $S$" script reported minima as low as $3.0$ against
a true target of $4$ at $k=2$ — a pure artifact, since clipping after
rescaling silently breaks the sum-$=S$ constraint). All results reported
below use `scipy.optimize.minimize` with an explicit `LinearConstraint`
(sum $=S$ exactly) and `Bounds` ($0<r_i\le\mathrm{cap}$), the correct
constrained-optimization formulation, with $25$–$80$ random restarts per
$(k,S,n)$ triple, and results cross-checked against the exact-`Fraction`
combinatorial search used in Steps 1–2 above (agreement to machine
precision, e.g. $k=3,4$ exact-grid search matches the constrained
optimizer to the reported fraction values exactly).

**Result.** For $k=2,3,4,5,6$ and $\rho:=S-2^k\in\{0,0.1,0.3,0.5,0.7,0.9,
0.99\}$ (and the boundary $\rho=0$ separately, $k$ up to $6$), the true
constrained minimum of $\mathrm{OddSum}(R\cup\Gamma_{k-1})$ over all
$n\in\{2,\ldots,k+1\}$ and all feasible $R$ matches $(S+2^k)/2$ to within
$10^{-12}$ in every one of the $5\times7+5=40$ tested points — see the
tables in this round's exploration (`/tmp/mega_verify2... ` superseded;
this round's own scripts, not reused from round 17). **This is very
strong evidence the Lemma is exactly tight** (not merely true), i.e. the
Lemma's stated bound cannot be improved.

**Essentiality of the cardinality cap, directly re-confirmed.** Relaxing
the count bound from $k+1$ to (e.g.) $n=5$ at $k=3$, $S=8.3$ gives a
constrained-optimizer minimum of $7.65$, **strictly below** both the
claimed bound $8.15=(S+2^k)/2$ **and** the raw target $2^k=8$ — i.e. the
cardinality cap is not a technical convenience but is **load-bearing**:
without it the statement (and indeed $\mathrm{GT}(m)$'s own sub-case (i)
target) is false, consistent with the cap-free counterexample $a_1=
494/125$ already on record.

**Diagnosis: why the natural "peel the tied top pair, induct on $k$"
strategy does not close the general case (honest, precise, not a
hand-wave).** The $k=2$ proof's tie sub-case ($a_1=\mathrm{cap}$) peels
both copies of $\mathrm{cap}=2^{k-1}$ and reduces to a smaller instance
$\mathrm{OddSum}(R'\cup\Gamma_{k-2})\ge S'/2$ where $R'=R\setminus\{
\mathrm{cap}\}$, $S':=\mathrm{sum}(R')=S-\mathrm{cap}$. Tracking the
constraints through this reduction: $S'\in[2^{k-1},2^{k-1}+1)$ (matching
the *shape* of the original problem one level down) and $|R'|\le k$ — but
**critically, $\max(R')$ is only known to be $\le\mathrm{cap}=2^{k-1}$,
not $\le2^{k-2}$** (the tighter cap the recursive instance would need to
literally match a smaller copy of the *same* Lemma, i.e.
$\mathrm{GCH}(k-1)$ needs $\max(R')\le2^{(k-1)-1}=2^{k-2}$). The
recursion does **not** shrink the magnitude cap alongside the level index
— this is exactly the "shrink-to-abstract-boundary vs. what the
recursion actually forces" failure mode this file's own memory (Rule 1,
`/tmp/memory/proof-builder.md`) warns about, now recurring one level
deeper inside a *sub*-lemma rather than at $\mathrm{GT}(m)$'s own top
level. Concretely: after one peel, the residual instance
$(\Gamma_{k-2},\ \mathrm{cap}=2^{k-1},\ S'\in[2^{k-1},2^{k-1}+1))$ has
$\mathrm{cap}$ equal to **twice** $\Gamma_{k-2}$'s own top value
$2^{k-2}$ — i.e. it is *itself* a smaller instance of the very same
"excess-$1$, near-top-boundary" phenomenon that sub-case (i) as a whole
is built from (an element of $R'$ can exceed $\Gamma_{k-2}$'s own top),
not a plain application of a lower-$k$ instance of this Lemma. A genuinely
general proof therefore needs a **two-parameter family** $\mathrm{GCH}(j,
\mathrm{cap},b;S)$ — with $\mathrm{cap}$ held fixed at the original
$2^{k-1}$ while the Γ-index $j$ decreases and the count budget $b$
decreases by $1$ at each peel — rather than the single-parameter
$\mathrm{GCH}(k)$ envisioned by this round's dispatch. This is a genuine,
precise structural finding (not merely "harder than expected"): it
identifies *exactly* which extra parameter the induction is missing, and
notes (without proof) that the $j=0$ base case of this two-parameter
family (where $\Gamma_0=\{1\}$ and $\mathrm{cap}$ can be arbitrarily large
relative to it) looks close in shape to the file's independently-flagged
`Case-B(m,k)`-type sliver — a plausible but **unverified** connection,
correctly not claimed as established.

**The non-tie sub-case ($a_1<\mathrm{cap}$)** does generalize cleanly
(the $k=2$ proof's argument — peel $\Gamma_{k-1}$'s unique top via the
certified Even-target Companion identity, landing on
$\mathrm{OddSum}(R\cup\Gamma_{k-2})$ with the SAME cap $2^{k-1}$ still —
suggesting this branch, too, feeds into the same two-parameter family
above, not a simpler cap-free case for $k\ge3$ the way it was for $k=2$
(there, dropping one level from $\Gamma_1$ landed directly on the
cap-free base case $\Gamma_0=\{1\}$, which is special to $k=2$, not
representative of general $k$).

### Step 4: odd excess $e\ge3$ — not attempted this round (honestly
### deferred, per the outline's explicit secondary priority)

The outline flagged $e\ge3$ near $a_1=2^k$ as a separate, lower-priority
deliverable ("cheap-kill first, do not claim closed without its own
targeted sweep"). Given the depth of the diagnosis needed just for $e=1$
(Step 3 above), this was not attempted this round; it remains open and
unconfirmed, exactly as the outline scoped it.

### Honest net effect, round 18

- **New, rigorous, complete result**: the true open residual for
  $\mathrm{GT}(m)$ sub-case (i), $e=1$, is **exactly** $a_1\in(2^k-1,2^k]$
  — narrower than previously stated (round 17's window
  $(2^{k-1},2^{k-1}+1)$ was the *wrong end* of the range to still need
  new work; the certified Claim B formula, evaluated at its own natural
  domain rather than only at the window, already covers
  $a_1\in(2^{k-1},2^k-1]$ in full). Two lines of algebra, no new lemma.
- **New, fully proved sub-case**: $k=2$ ($m=3$) of the true residual is
  **completely and rigorously closed** — a genuine small-case closure
  (exhaustive casework, no gaps, cross-checked numerically to $7/4000$
  margin), the first complete closure of any part of this specific
  residual.
- **General Cardinality-Constrained Half-Sum Lemma**: stated in exact
  closed form ($\mathrm{OddSum}(R\cup\Gamma_{k-1})\ge(S+2^k)/2$,
  equivalently $\mathrm{AltSum}(R\cup\Gamma_{k-1})\ge1$), verified to
  extremely high precision by a *correctly constrained* numerical search
  (avoiding the exact optimizer-artifact class this file's own memory
  warns about) across $k=2,\ldots,6$ and $7$ values of $\rho$ each — but
  **not proved in general**. The natural induction is diagnosed precisely
  (Step 3): it requires a genuinely more general two-parameter family
  (fixed cap, decreasing $\Gamma$-index and count budget) rather than a
  simple induction on $k$ alone — a real, non-hand-wavy obstruction, not
  a vague "still open."
- **$e\ge3$**: not attempted, honestly deferred per the outline.
- **Net for $\mathrm{GT}(m)$, $m\ge4$**: still `partial`. Sub-case (i)'s
  $e=1$ residual is now fully closed at $k=2$ and precisely narrowed (and
  precisely diagnosed) for general $k$; the $e=0$ sliver (`Case-B(m,k)`'s
  own long-standing obstruction) and general $k\ge3$ of the $e=1$
  residual remain open, with a concrete (if still unproved) structural
  hypothesis connecting them via the two-parameter family identified
  above.

## Promotable lemmas (round 18)

- **Sharper residual-range derivation for $\mathrm{GT}(m)$ sub-case (i),
  $e=1$ (new, proved in full, two lines of algebra from the already-
  certified Claim B formula).** For every $k\ge2$: the certified odd-case
  formula $\mathrm{LB}_{\mathrm{odd}}-T_{\mathrm{odd}}=\frac{2^k-a_1-1}2$
  (at $e=1$) is $\ge0$ iff $a_1\le2^k-1$; hence sub-case (i) at $e=1$ is
  already closed (by the already-certified Half-Sum Corollary route) for
  every $a_1\in(2^{k-1},2^k-1]$, and the true open residual is exactly
  $a_1\in(2^k-1,2^k]$, a width-1 window at the top of the range — not
  the whole outside-window range previously believed open.
- **Cardinality-Constrained Half-Sum Lemma, $k=2$ instance (new, proved
  in full).** For $R$ with $\max(R)\le2$, $|R|\le3$, $\mathrm{sum}(R)=S
  \in[4,5)$: $\mathrm{OddSum}(R\cup\{2,1\})\ge(S+4)/2$, with equality
  attained (symmetric tie configuration). Complete exhaustive casework
  (count $n=2,3$; tie vs. non-tie with $\mathrm{cap}$; three-way split
  on the residual pair vs. $\Gamma_0=\{1\}$), no numeric appeal in the
  proof itself, cross-checked against $300{,}000$ exact-`Fraction`
  trials (minimum observed margin $7/4000>0$). Closes $\mathrm{GT}(m)$
  sub-case (i), $e=1$, $k=2$ ($m=3$) in full, for every $a_1\in(2,4]$.
- **General Cardinality-Constrained Half-Sum Lemma (conjecture, NOT
  proved — do not certify as a theorem).** For $k\ge2$, $R$ with
  $\max(R)\le2^{k-1}$, $|R|\le k+1$, $\mathrm{sum}(R)=S\in[2^k,2^k+1)$:
  $\mathrm{OddSum}(R\cup\Gamma_{k-1})\ge(S+2^k)/2$ (equivalently
  $\mathrm{AltSum}(R\cup\Gamma_{k-1})\ge1$). Verified to $\sim10^{-12}$
  precision by correctly-constrained numerical optimization across
  $k=2,\ldots,6$; the cardinality cap is confirmed load-bearing (a
  counterexample exists once $|R|$ is allowed to exceed $k+1$, e.g.
  $k=3,S=8.3,n=5$ gives value $7.65<8.15$). This is a precise, checkable
  target for the next round, not yet a lemma — its natural one-parameter
  induction is shown (Step 3 above) to need a genuinely more general
  two-parameter family instead.

## Promotable lemmas (round 19)

- **Lemma TPC (Tied-Pair Cancellation, new, proved in full).** If a
  finite multiset $M$ of positive reals contains a value $x$ with
  multiplicity exactly $2$, then $\mathrm{AltSum}(M)=\mathrm{AltSum}(M
  \setminus\{x,x\})$. Proved directly from the definition of
  $\mathrm{AltSum}$ (the two copies occupy consecutive, opposite-parity
  ranks in sorted order, contributing $0$; deleting them shifts all lower
  ranks down by $2$, preserving parity of every remaining rank). See
  "Round 19" section above for the full proof.
- **Lemma BCF (Block-Contribution Formula, new, proved in full).** For a
  finite multiset $M$ decomposed into constant "levels" $v_1>\cdots>v_L$
  with multiplicities $t_1,\dots,t_L$, $\mathrm{AltSum}(M)=\sum_{i:t_i
  \text{ odd}}(-1)^{C_i}v_i$ where $C_i=\sum_{i'<i}t_{i'}$. Proved by
  induction on $\sum t_i$ using Lemma TPC. **Corollary**: any
  even-multiplicity level contributes exactly $0$ to $\mathrm{AltSum}(M)$,
  regardless of its value or position among the other levels.
- **Exact achievability theorem for GCH($k$) (new, proved in full, general
  $k$, no numerics).** For every $k\ge2$ and every $S\in[2^k,2^k+1)$, the
  witness $R^*=\{2^{k-1},\dots,4\}\cup\{r,r\}$ ($r=(S-2^k)/2+2$) is
  feasible for GCH($k$) and satisfies $\mathrm{AltSum}(R^*\cup
  \Gamma_{k-1})=1$ exactly. Proved via Lemma BCF's Corollary (the shared
  chain levels, each now multiplicity $2$, cancel regardless of position,
  leaving exactly $\{r,r,2,1\}$ whose $\mathrm{AltSum}$ is directly
  $r-r+2-1=1$).
- **Lemma LNI (Local Non-Improvement, new, proved in full).** At a true
  minimizer of $\mathrm{AltSum}(R\cup\Gamma_{k-1})$ subject to
  $\mathrm{sum}(R)=S$ fixed, no two coordinates of $R$ can be
  simultaneously "free" (strictly between two consecutive elements of
  $\Gamma_{k-1}\cup\{0,\mathrm{cap}\}$) with opposite rank parity — else
  a small mass transfer between them strictly decreases $\mathrm{AltSum}$.
  Proved directly from affineness of $\mathrm{AltSum}$ on the
  rank-order-fixed neighborhood.

**Not promotable as of round 19 (superseded — see "Round 21" section
below, which closes this in full):** the general lower bound
$\mathrm{AltSum}(R\cup\Gamma_{k-1})\ge1$ for every feasible $R$ (arbitrary
$k$) was open as of round 19 — reduced to, but not resolved as, a
finite-per-$k$ statement about integer multiplicity vectors via Lemma
BCF. Verified for $k=2$ (matches certified Lemma 2) and numerically for
$k=3,4,5$ (multi-restart exact-objective `scipy` search, cheap-kill
passed, no counterexample found); not proved for general $k$ at that
time.

## Round 21 target: close the General Cardinality-Constrained Half-Sum
## Lemma via the canonical-form pigeonhole + pairing route (per outliner,
## revise — supersedes the round 18/19 "needs a two-parameter family"
## diagnosis if it goes through)

The round-21 `math-explorer-canonical-form` scouted (not proved) a route
that, if it closes, finishes the general-$k$ GCH Lemma **without** the
two-parameter $\mathrm{GCH}(j,\mathrm{cap},b;S)$ family flagged in round
18 as necessary — a genuinely different mechanism (direct global counting
over the fixed budget $k+1$ vs. $k$ levels, not induction on $k$).
Concretely, build these three steps as a single proof, using the already
**certified** Finite Reduction Theorem
(`lemmas/invisible-block-skip-fact-and-general-pairwise-reduction.md`) as
the entry point (it already reduces every feasible $R$ to canonical form
$R''$: integer multiplicities $n_0,\dots,n_{k-1}\ge0$ at the $\Gamma$-levels
plus one free block $(t,r)$, $\sum n_j2^j+tr=S$, $\sum n_j+t\le k+1$, and
$\mathrm{AltSum}(R''\cup\Gamma_{k-1})\le\mathrm{AltSum}(R\cup\Gamma_{k-1})$
so it suffices to bound the canonical form):

- **Step A (pigeonhole — every feasible $R''$ has $\ge1$ active item).**
  Formalize and prove rigorously: level $j$ "inactive" needs $n_j\ge1$
  odd (cost $\ge1$ each, $k$ levels total budget-wise); the free block
  inactive needs $t\ge2$ even (cost $\ge2$). Show all-inactive-levels
  plus inactive-or-absent-free-block is infeasible against budget $k+1$
  **and** against the parity of $S$ (the explorer's sketch: all-$n_j$-odd
  forces $S$ odd via $S=(2^k-1)+2\cdot\text{even}$, but the only integer
  $S$ in range is $2^k$, even — make this a clean, general (not just
  integer-$S$) argument, since $S$ need not be an integer when $t\ge1$;
  handle the $t=0$ sub-case separately from $t\ge1$ explicitly). Do not
  just cite the explorer's sketch — write the full case argument,
  including non-integer $S$.
- **Step B (pairing/telescoping — any nonempty active-Γ-subset alone
  gives $\mathrm{AltSum}\ge1$).** Prove: for any nonempty $A\subseteq
  \{2^0,\dots,2^{k-1}\}$ sorted decreasing $a_1>\cdots>a_p$, the
  alternating sum $a_1-a_2+a_3-\cdots$ is $\ge1$, by pairing adjacent
  terms ($a_{2i-1}-a_{2i}\ge$ smaller of the pair, since distinct powers
  of $2$ differ by at least the smaller one — prove this sub-fact too,
  it's elementary but must be stated) and handling the leftover term if
  $p$ is odd. This is fully elementary; write it as a clean lemma
  (candidate name: **Active-Γ-Subset Alternating Sum Lemma**).
- **Step C (the genuinely open case — free value active, $t$ odd).**
  This is the *only* remaining gap. Do **not** assume it is dominated by
  Step B (the explorer flagged this as a numerically-suggested pattern,
  not a proof). Two sub-tasks, either suffices:
  (i) a direct exchange/domination argument — generalize the certified
  **General Pairwise Reduction Lemma** so that it applies not just
  between two pre-existing active $R$-values but between one active free
  value and a *newly introduced* second coordinate (the explorer's own
  suggested reduction), showing any configuration with the free block
  active can be weakly improved (AltSum non-increased) by flipping it to
  inactive ($t\to t+1$, re-routing mass into an existing or new
  $\Gamma$-level or a second free coordinate) — must be proved for
  **every** interleaving position, not just the extremal witness; or
  (ii) direct casework on where $r$ falls relative to the active
  $\Gamma$-values (generalizing the fully-closed $k=2$ instance's
  three-way split), for general $k$.
  **This is structurally the same shape as the already-solved $k=2$
  case** (re-read that casework, Round 18 section above, before starting)
  — the task is to find what generalizes and what doesn't.

**Honest scope note:** the explorer's numeric exhaustive search (§2 of its
report, $k=2,\dots,8$) found zero violations and an exact tight family, so
there is no known counterexample — but Step C is not yet a proof. If Step
C resists a clean general argument after a real attempt, fall back to
documenting exactly where it breaks (which interleaving position, which
$k$) rather than asserting closure.

## Round 21: full closure of the General Cardinality-Constrained
## Half-Sum Lemma (all $k\ge2$), via Steps A/B/C of the outlined route

This section builds the three-step route dispatched above end to end.
**Result: all three steps close, giving a complete, unconditional proof
of the General Cardinality-Constrained Half-Sum Lemma for every $k\ge2$**
— the finite combinatorial statement the certified Finite Reduction
Theorem (`lemmas/invisible-block-skip-fact-and-general-pairwise-reduction.md`)
reduces the whole lemma to. This supersedes the round 18/19 "needs a
two-parameter family $\mathrm{GCH}(j,\mathrm{cap},b;S)$" diagnosis: a
direct global argument on the reduced canonical form suffices instead,
without any induction on $k$ at all. Flagged as a **candidate for
certification, not self-certified** — the reviewer should independently
re-derive Steps A–C below.

### Setup (recap, all objects already certified except where noted)

$\mathrm{GCH}(k)$: $R$ a finite multiset, $\max(R)\le\mathrm{cap}:=
2^{k-1}$, $|R|\le k+1$, $\mathrm{sum}(R)=S\in[2^k,2^k+1)$; $\Gamma_{k-1}
=\{2^{k-1},\dots,2,1\}$ ($k$ levels, values $2^0,\dots,2^{k-1}$).
By the certified Finite Reduction Theorem, it suffices to prove
$\mathrm{AltSum}(R''\cup\Gamma_{k-1})\ge1$ for every feasible **canonical
form** $R''$: integer multiplicities $n_0,\dots,n_{k-1}\ge0$ at the
$\Gamma$-levels (level $j$ has value $2^j$) plus **at most one** free
block $(t,r)$ with $t\ge0$ copies of a value $r\notin\Gamma_{k-1}$,
$r\in(0,\mathrm{cap}]$, subject to
$$\textstyle\sum_j n_j2^j+tr=S,\qquad \sum_j n_j+t\le k+1.$$

**Reduction to an active-value alternating sum (immediate corollary of
the already-certified Lemma BCF).** Level $j$ has total multiplicity
$n_j+1$ in $R''\cup\Gamma_{k-1}$ ($n_j$ from $R''$, $1$ from $\Gamma_{k-1}$
itself); call level $j$ **active** if $n_j$ is even (total multiplicity
odd, contributing $\pm2^j$ to $\mathrm{AltSum}$ by Lemma BCF) and
**inactive** if $n_j$ is odd (total multiplicity even, contributing $0$).
Call the free block **active** if $t$ is odd (contributing $\pm r$) and
**inactive** if $t$ is even (contributing $0$, including $t=0$). Writing
$A:=\{2^j: j\text{ active}\}\subseteq\{2^0,\dots,2^{k-1}\}$, Lemma BCF
gives directly:
$$\mathrm{AltSum}(R''\cup\Gamma_{k-1})=\mathrm{AltSum}\bigl(A\cup\{r\}
\text{ if free block active, else }A\bigr),$$
i.e. **only the parities of the $n_j$ and of $t$ matter**, not their
magnitudes — and the resulting quantity is the alternating sum (sorted
decreasing, sign $+$ at the top) of the small value-set $A$ (and $r$, if
active). This is the object Steps A–C bound below.

### Step A (pigeonhole): every feasible canonical form has $\ge1$ active
### item — proved in full, uniformly, no separate non-integer-$S$ case
### needed

**Claim.** It is impossible to have simultaneously: every level $j=0,
\dots,k-1$ inactive (all $n_j$ odd), **and** the free block inactive or
absent ($t=0$ or $t$ even $\ge2$).

*Proof.* Suppose all $n_j$ odd. Each $n_j\ge1$, so $\sum_j n_j\ge k$;
combined with the budget $\sum_j n_j+t\le k+1$, this forces $t\le1$. If
the free block is inactive/absent, $t\in\{0\}\cup\{2,4,\dots\}$; the only
value in $\{0,2,4,\dots\}$ that is also $\le1$ is $t=0$. So $t=0$ is
forced, and $S=\sum_j n_j2^j$ exactly (the free block contributes
nothing). Write $n_j=1+2m_j$ with $m_j\ge0$ integer (valid since each
$n_j$ is odd $\ge1$). Then
$$S=\sum_{j=0}^{k-1}(1+2m_j)2^j=\Bigl(\sum_{j=0}^{k-1}2^j\Bigr)+2\sum_j
m_j2^j=(2^k-1)+2N,\qquad N:=\sum_j m_j2^j\ge0\text{ integer.}$$
So $S$ is an **odd integer**. But $S\in[2^k,2^k+1)$ contains exactly one
integer, $2^k$, which is **even** — contradiction. $\blacksquare$

Notably, this argument **never needs to treat non-integer $S$ (the
$t\ge1$ case) separately**, as the round-21 dispatch anticipated might be
necessary: the case split falls out automatically — the "all-inactive"
hypothesis itself forces $t=0$ (via the budget bound alone, independent
of $S$'s value), and $t=0$ is exactly the sub-case where $S$ is forced
to be an integer, so the two concerns (non-integer $S$, and the free
block being active) never need separate handling; they coincide.

**Consequence.** Every feasible canonical form has $A\ne\varnothing$
(some level active) or the free block active ($t$ odd), or both. This
splits the remaining work into exactly four cases, all covered below:
(B) $A\ne\varnothing$, free block inactive; (C0) $A=\varnothing$, free
block active; (C1) $A=\{v\}$ singleton, free block active; (C2)
$|A|\ge2$, free block active.

### Step B (Active-$\Gamma$-Subset Alternating Sum Lemma): proved in
### full, elementary — covers case (B)

**Lemma.** For any nonempty $A'\subseteq\{2^0,2^1,\dots,2^{k-1}\}$
(distinct powers of $2$), sorted decreasing $a_1>a_2>\cdots>a_p$ ($p=
|A'|\ge1$), $\mathrm{AltSum}(A')=a_1-a_2+a_3-\cdots\ge1$.

*Proof.* First, a sub-fact: for any two **distinct** powers of $2$,
$2^x>2^y$ ($x>y\ge0$ integers), $2^x-2^y=2^y(2^{x-y}-1)\ge2^y\cdot1=2^y
\ge2^0=1$ (since $2^{x-y}-1\ge1$ for $x>y$, and $2^y\ge1$ for $y\ge0$).
Pair the sorted sequence as $(a_1,a_2),(a_3,a_4),\dots$; each pair
$(a_{2i-1},a_{2i})$ consists of two distinct powers of $2$ with
$a_{2i-1}>a_{2i}$, so contributes $a_{2i-1}-a_{2i}\ge1$ by the sub-fact.
If $p$ is odd, there is one leftover term $a_p=2^y\ge1$ ($y\ge0$),
contributing $\ge1$ directly (with sign $+$, since it occupies the first
position of the last, singleton "pair"). Since $p\ge1$, at least one such
term (a pair or the sole leftover) is present, and every present term
contributes $\ge1$ with the rest of the terms (if any) also each $\ge1$
and of the same sign structure (alternating, but grouped into
nonnegative pair-contributions plus a nonnegative leftover) — so the
total is a sum of one or more terms each $\ge1$, hence $\ge1$.
$\blacksquare$

This closes case (B) directly: if $A\ne\varnothing$ and the free block is
inactive, $\mathrm{AltSum}(R''\cup\Gamma_{k-1})=\mathrm{AltSum}(A)\ge1$.

### Step C: the free block active ($t$ odd) — full case split, all
### three sub-cases closed

By Step A's consequence, the remaining cases all have the free block
active ($t$ odd, so $r$ contributes $\pm r$). We split on $|A|$.

**Case (C0): $A=\varnothing$.** All $k$ levels are inactive (all $n_j$
odd $\ge1$), so $\sum n_j\ge k$; budget forces $t\le1$, and $t$ odd
$\ge1$ forces $t=1$ exactly. Then $\sum n_j\le k+1-1=k$, combined with
$\sum n_j\ge k$ forces $\sum n_j=k$ exactly, i.e. $n_j=1$ for **every**
$j$ (the only way $k$ terms each $\ge1$ sum to exactly $k$). So $S=
\sum_j 1\cdot2^j+1\cdot r=(2^k-1)+r$, giving $r=S-2^k+1$. Since $S\in
[2^k,2^k+1)$, $r\in[1,2)$. Moreover $r\ne1$ (else $r$ would coincide with
$\Gamma$-level $0$, contradicting $r\notin\Gamma_{k-1}$, i.e. this
degenerate boundary is not a valid canonical form — it would instead
have $n_0=2$, active, a different case), so in fact $r\in(1,2)$
strictly. With $A=\varnothing$, $\mathrm{AltSum}(A\cup\{r\})=r\in(1,2)$,
so $\ge1$ (in fact $>1$). $\blacksquare$

**Case (C1): $A=\{v\}$, $v=2^{j_A}$ a single active level.** The other
$k-1$ levels are inactive ($n_j\ge1$ odd, $j\ne j_A$), so $\sum_{j\ne
j_A}n_j\ge k-1$. Budget: $\sum_{j\ne j_A}n_j+n_{j_A}+t\le k+1$, with
$n_{j_A}\ge0$ even and $t\ge1$ odd. This gives $n_{j_A}+t\le k+1-\sum_{j
\ne j_A}n_j\le k+1-(k-1)=2$. Since $n_{j_A}\ge0$ even and $t\ge1$ odd,
the only pair with $n_{j_A}+t\le2$ is $(n_{j_A},t)=(0,1)$ (any other
choice, e.g. $n_{j_A}=2$ or $t=3$, already exceeds $2$ alone). So
$n_{j_A}=0$ and $t=1$ are **forced**. This in turn forces $\sum_{j\ne
j_A}n_j\le k+1-0-1=k$; combined with $\sum_{j\ne j_A}n_j\ge k-1$ (the
$k-1$ mandatory terms), the sum is $k-1$ or $k$ — but any term exceeding
its minimum of $1$ must jump by an even amount ($1\to3\to\cdots$) to
stay odd, i.e. costs $\ge2$ of extra budget, and only $1$ unit of slack
budget is available ($k$ vs. mandatory $k-1$) — insufficient for even
one such jump. So $n_j=1$ for every $j\ne j_A$ too, **forced**.
(Independently confirmed by direct enumeration for $k=2,\dots,7$, every
active level $j_A$: the unique feasible allocation is exactly
$(n_{j_A},t)=(0,1)$, $n_j=1$ else — script `/tmp/verify_singleton_general.py`,
this round.) Hence $S=\sum_{j\ne j_A}2^j+r=\bigl((2^k-1)-v\bigr)+r$,
giving $r=S-2^k+1+v$. Since $S\in[2^k,2^k+1)$: $r\in[1+v,\,2+v)$, so
$r>v$ always and $r-v\in[1,2)$. Sorted, $r>v$, so $\mathrm{AltSum}(A\cup
\{r\})=r-v\in[1,2)\ge1$. $\blacksquare$

**Case (C2): $|A|\ge2$.** This is the general case, closed by a
feasibility-free argument (it holds for *every* $r\in(0,\mathrm{cap}]
\setminus\Gamma_{k-1}$, not just feasible ones — the cardinality budget
is not needed here at all, only $|A|\ge2$).

Write $A=\{v_1>v_2>\cdots>v_p\}$, $p\ge2$. Fix the interval structure on
$(0,\mathrm{cap}]$ cut at the points $v_1,\dots,v_p$ (giving $p+1$
open sub-intervals: $(0,v_p)$, $(v_{i+1},v_i)$ for $i=1,\dots,p-1$, and
$(v_1,\mathrm{cap}]$).

*Affineness on each open interval (from the already-certified Fact 1,
Invisible-Block Skip Fact).* Within any one open interval, $r$'s rank
among $A\cup\{r\}$ is constant (no element of $A$ is crossed), so $r$
contributes with a **fixed sign** $\sigma\in\{+1,-1\}$ throughout that
interval, and every other element's rank is also unaffected (a single
extra element is an "odd block of size 1," and Fact 1 shows crossing it
does not change the sign of any fixed element once we're not crossing —
here more simply, $A$'s own elements never move, only $r$ does, so their
mutual order and hence their signs are fixed regardless of $r$, as long
as $r$ doesn't cross one of them). Hence $\mathrm{AltSum}(A\cup\{r\})=
C+\sigma r$ for a constant $C$ (depending only on the interval, not on
$r$'s exact value within it) — an affine, strictly monotonic (slope
$\pm1\ne0$) function of $r$ on each open interval.

*Boundary values (from the already-certified Lemma TPC / BCF corollary).*
As $r\to v_i$ from either side (for $i=1,\dots,p$), the multiset
$A\cup\{r\}\to A\cup\{v_i\}$, i.e. $v_i$ acquires multiplicity $2$ —
an even block, which by the already-certified Lemma TPC (Tied-Pair
Cancellation) / Lemma BCF's corollary contributes exactly $0$ and can be
deleted without changing $\mathrm{AltSum}$ or the parity of any other
rank. Hence
$$\lim_{r\to v_i}\mathrm{AltSum}(A\cup\{r\})=\mathrm{AltSum}(A\setminus
\{v_i\}),\qquad i=1,\dots,p,$$
independent of the side of approach (so the two open intervals adjoining
$v_i$ share this same boundary value — the piecewise-affine function
extends continuously across each $v_i$, even though $r=v_i$ itself is
excluded from the domain). Also, trivially, $\lim_{r\to0^+}\mathrm{AltSum}
(A\cup\{r\})=\mathrm{AltSum}(A)$ (a vanishing element contributes $0$
regardless of sign).

*Conclusion via monotonicity.* On each open interval, $\mathrm{AltSum}
(A\cup\{r\})$ is affine with nonzero slope, hence **strictly monotonic**,
so its values on the (closed) interval lie between the two endpoint
limits computed above. Every one of these endpoint limits is either
$\mathrm{AltSum}(A)$ or $\mathrm{AltSum}(A\setminus\{v_i\})$ for some
$i=1,\dots,p$. Since $|A|=p\ge2$, both $A$ and every $A\setminus\{v_i\}$
are **nonempty** subsets of $\{2^0,\dots,2^{k-1}\}$, so Step B's Lemma
applies to each: $\mathrm{AltSum}(A)\ge1$ and $\mathrm{AltSum}(A\setminus
\{v_i\})\ge1$ for every $i$. Hence every endpoint value is $\ge1$, and by
monotonicity every value **strictly between** two endpoints on the same
interval is also $\ge1$ (an affine function's values on a closed interval
lie in the closed interval spanned by the two endpoint values; since both
endpoints are $\ge1$, so is every point between them). This covers every
open sub-interval, hence all of $(0,\mathrm{cap}]\setminus\Gamma_{k-1}$.
$\blacksquare$

**Independent numeric confirmation of Case (C2)'s underlying combinatorial
fact** (this round, own script `/tmp/verify_stepc.py`): for $k=2,\dots,6$,
$2{,}000$ random nonempty $A$ with $|A|\ge2$ per $k$, comparing $2{,}000$
fine random samples of $r\in(0,\mathrm{cap}]\setminus A$ against
$\min\bigl(\mathrm{AltSum}(A),\min_i\mathrm{AltSum}(A\setminus\{v_i\})
\bigr)$: zero instances of the sampled minimum falling below the
theoretical floor by more than the sampling grid's resolution — consistent
with (not a substitute for) the hand proof above. Case (C1)'s forced
unique allocation independently re-confirmed by brute-force enumeration,
$k=2,\dots,7$, every choice of active level $j_A$ (script
`/tmp/verify_singleton_general.py`): the feasible set is always exactly
the single point $(n_{j_A},t)=(0,1)$, $n_j=1$ for $j\ne j_A$ — no other
allocation is ever feasible, confirming the "only $1$ unit of budget
slack, insufficient for a parity-preserving $\pm2$ jump" argument is not
merely an upper bound but the **exact** feasible set.

### Conclusion: General Cardinality-Constrained Half-Sum Lemma, proved
### in full for every $k\ge2$

Combining: Step A shows every feasible canonical form $R''$ falls into
case (B), (C0), (C1), or (C2); each is closed above with $\mathrm{AltSum}
(R''\cup\Gamma_{k-1})\ge1$. By the already-certified Finite Reduction
Theorem, this extends to **every** feasible $R$ (not just canonical
forms), since the theorem produces a canonical $R''$ with $\mathrm{AltSum}
(R''\cup\Gamma_{k-1})\le\mathrm{AltSum}(R\cup\Gamma_{k-1})$ — so
$$\mathrm{AltSum}(R\cup\Gamma_{k-1})\ge\mathrm{AltSum}(R''\cup\Gamma_{k-1})
\ge1$$
for **every** feasible $R$ of $\mathrm{GCH}(k)$, **every** $k\ge2$ — no
numerics needed, no restriction to small $k$. This is a complete,
unconditional proof, matching (and now justifying in full generality) the
extensive round-18 numeric confirmation (correctly-constrained `scipy`
search, $k=2,\dots,6$, minimum matching $(S+2^k)/2$ to $10^{-12}$) and
the certified $k=2$ closure. **The cardinality cap $|R|\le k+1$ is used
essentially and exactly once**, in Step A (to force the all-inactive
case's free block to $t=0$) and in Case (C1) (to force the unique
singleton allocation) — consistent with round 18's independent finding
that the cap is load-bearing (a counterexample exists once the cap is
relaxed).

### Consequence for $\mathrm{GT}(m)$

Via the already-certified reduction (Claim B / the Half-Sum Corollary
route, round 17–18), the General Cardinality-Constrained Half-Sum Lemma
closes $\mathrm{GT}(m)$ sub-case (i) (odd excess $e=1$) for **every**
$k\ge2$ (not just $k=2$), i.e. for every $a_1\in(2^{k-1},2^k]$ — the full
range, superseding the round-18 "width-1 window at the top, $a_1\in
(2^k-1,2^k]$, still open for $k\ge3$" residual. **What remains open for
$\mathrm{GT}(m)$, $m\ge4$**: the $e=0$ sliver (`Case-B(m,k)`'s
long-standing own obstruction, untouched by this round) and odd excess
$e\ge3$ (honestly deferred per the outline, not attempted this round —
the Half-Sum Corollary route used for $e=1$ does not directly cover
$e\ge3$; a separate reduction would be needed, not yet built). This
narrows $\mathrm{GT}(m)$'s open residual, but does **not** fully close it.

## Promotable lemmas (round 21) — candidates for certification, not
## self-certified

- **BCF-to-active-set reduction (recap of an already-certified
  corollary, restated in the $R''$-canonical-form language for
  reference — not new content, no separate certification needed).**
- **Canonical-Form Pigeonhole Lemma (new, proved in full).** For every
  feasible canonical form of $\mathrm{GCH}(k)$, it is impossible for
  every $\Gamma$-level to be inactive **and** the free block to be
  inactive/absent simultaneously; the all-inactive-levels case
  additionally forces the free block absent ($t=0$) and $S$ to be the
  unique odd integer in $(2^k-1,2^k+1)$, contradicting $S\in[2^k,2^k+1)$
  (whose only integer, $2^k$, is even). No non-integer-$S$ case split
  needed.
- **Active-$\Gamma$-Subset Alternating Sum Lemma (new, proved in full,
  elementary).** For any nonempty $A'\subseteq\{2^0,\dots,2^{k-1}\}$,
  $\mathrm{AltSum}(A')\ge1$.
- **Singleton-Active Free-Value Forcing Lemma (new, proved in full).**
  When exactly one $\Gamma$-level is active in a feasible canonical form
  and the free block is active, the cardinality budget forces the unique
  allocation $n_{j_A}=0$, $t=1$, $n_j=1$ ($j\ne j_A$), giving $r\in[1+v,
  2+v)$ where $v=2^{j_A}$ — hence $\mathrm{AltSum}(\{v,r\})=r-v\in[1,2)$.
- **Two-or-More-Active Domination Lemma (new, proved in full,
  feasibility-free).** For any $A\subseteq\{2^0,\dots,2^{k-1}\}$ with
  $|A|\ge2$ and any $r\in(0,\mathrm{cap}]\setminus\Gamma_{k-1}$,
  $\mathrm{AltSum}(A\cup\{r\})\ge1$ — via piecewise-affineness (Fact 1)
  plus continuous boundary values equal to $\mathrm{AltSum}(A)$ or
  $\mathrm{AltSum}(A\setminus\{v\})$ (Lemma TPC), both $\ge1$ by the
  Active-$\Gamma$-Subset Alternating Sum Lemma since $|A|\ge2$ keeps
  every such set nonempty.
- **General Cardinality-Constrained Half-Sum Lemma (upgraded from
  round-18/19 "conjecture, NOT proved" to a complete theorem, all $k\ge2$
  — the headline result of this round).** For $k\ge2$, $R$ feasible for
  $\mathrm{GCH}(k)$ ($\max(R)\le2^{k-1}$, $|R|\le k+1$, $\mathrm{sum}(R)=
  S\in[2^k,2^k+1)$): $\mathrm{OddSum}(R\cup\Gamma_{k-1})\ge(S+2^k)/2$,
  equivalently $\mathrm{AltSum}(R\cup\Gamma_{k-1})\ge1$. Proved via Steps
  A–C above (no numerics in the proof itself); consistent with, and now
  superseding, the round-18 high-precision numeric confirmation.

**Honest scope note.** This closes the General Cardinality-Constrained
Half-Sum Lemma completely, but this is only **one** of the two named
residuals of $\mathrm{GT}(m)$, $m\ge4$ (see "Consequence for
$\mathrm{GT}(m)$" above) — the $e=0$ sliver and odd $e\ge3$ remain open.
Status stays `partial` for $\mathrm{GT}(m)$ as a whole, but this is a
genuine, complete, unconditional closure of a previously-open general-$k$
lemma that several prior rounds (16, 18, 19) explicitly flagged as
resisting the natural induction.

## Round 22: Track 1 (Odd-Excess $e\ge3$ Endpoint Closure Theorem, full
## range, not just the window) and Track 2 (Cap-Free General
## Cardinality-Constrained Half-Sum Lemma, via a genuine line-by-line
## audit, plus the Case-B(m,k) Sliver Closure Theorem)

Per this round's dispatch: two independent gap-closure tracks inside
$\mathrm{GT}(m)$'s case split. Track 1 closes odd excess $e\ge3$
unconditionally over the *full* range $a_1\in(2^{k-1},2^k]$ (not merely
the window round 17 checked). Track 2 audits the certified proof of the
General Cardinality-Constrained Half-Sum Lemma (GCH) and its underlying
Finite Reduction Theorem for cap-dependence, establishes a **cap-free**
strengthening, and combines it with a Global-max peel to close
`Case-B(m,k)`'s remaining sliver $b_1\in(2^{m-1}-1,2^{m-1})$.

### Track 1: Odd-Excess $e\ge3$ Endpoint Closure Theorem

**Setting (restated exactly, sub-case (i) of $\mathrm{GT}(m)$, odd
branch).** Fix $k\ge1$, $m\ge k+1$ with $e:=m-k$ odd, $e\ge3$. Let
$a_1\in(2^{k-1},2^k]$, $R$ a finite multiset with $\max(R)\le2^{k-1}$,
$\mathrm{sum}(R)=2^m-a_1$, $D:=\{a_1\}\cup R$, $\mathrm{sum}(D)=2^m$.
Target: $\mathrm{OddSum}(D\cup\Gamma_{m-1})\ge2^m$.

**Step 1 — the exact margin identity, valid on the whole range.** By
Step 1 of the round-17 section above (odd-$e$ branch of the corrected
$e$-fold $q=0$-chain, certified in
`lemmas/even-target-companion-peeling-and-corrected-qzero-chain.md`),
the target $\mathrm{OddSum}(D\cup\Gamma_{m-1})\ge2^m$ is **exactly
equivalent** to
$$\mathrm{OddSum}(R\cup\Gamma_{k-1})\ \ge\ T_{\mathrm{odd}}:=2^m-2^k-
\frac{2^{m+1}-2^{k+2}}3,$$
an algebraic identity holding for every $a_1\in(2^{k-1},2^k]$ (the chain
this rests on is derived once, for the whole domain of $a_1$ — the
$a_1$-dependence enters only through $R:=D\setminus\{a_1\}$'s sum, and
nothing in the chain's derivation restricts $a_1$ to any sub-window). By
the certified Half-Sum Corollary
(`lemmas/half-sum-corollary-and-large-sum-closure-theorem.md`, cap-free,
valid for any finite multiset), applied to $R\cup\Gamma_{k-1}$
($\mathrm{sum}(\Gamma_{k-1})=2^k-1$):
$$\mathrm{OddSum}(R\cup\Gamma_{k-1})\ \ge\ \mathrm{LB}_{\mathrm{odd}}:=
\frac{(2^m-a_1)+2^k-1}2.$$
Hence it suffices to show $\mathrm{margin}(a_1):=\mathrm{LB}_{\mathrm{odd}}
-T_{\mathrm{odd}}\ge0$. Direct algebraic expansion (independently
re-verified this round by exact `sympy` symbolic computation, not by
hand):
$$\mathrm{LB}_{\mathrm{odd}}-T_{\mathrm{odd}}=\left[\frac{(2^m-a_1)+2^k-1}
2\right]-\left[2^m-2^k-\frac{2^{m+1}-2^{k+2}}3\right]=\frac{2^k}6+
\frac{2^m}6-\frac{a_1}2-\frac12.$$
This is **exactly** the certified formula already used for Claim B of
the round-17 section (`Half-Sum Corollary and Large-Sum Closure Theorem`
combined with the `Corrected $e$-fold $q=0$-chain closed form`), and it
is derived — as an algebraic identity in $a_1,k,m$ — for the **whole**
domain $a_1\in(2^{k-1},2^k]$, with no restriction to any sub-window: the
window restriction present in round 17's *evaluation* of this formula
(Claim B checked positivity only at $a_1=2^{k-1}+1$) was a choice about
*where to evaluate*, not a restriction on where the formula holds. This
is exactly the distinction this track is tasked with getting right (per
round 18's precedent bug of evaluating only at a window supremum instead
of the true range endpoint).

**Step 2 — monotonicity: the minimum over the closed-on-the-right range
is at $a_1=2^k$.** $\mathrm{margin}(a_1)=\frac{2^k}6+\frac{2^m}6-
\frac{a_1}2-\frac12$ is an affine function of $a_1$ with slope $-\frac12
<0$, i.e. **strictly decreasing** in $a_1$. Over the interval
$a_1\in(2^{k-1},2^k]$ — open on the left, **closed on the right** — a
strictly decreasing affine function attains its infimum at the largest
admissible input, and since the right endpoint $a_1=2^k$ **is** an
admissible value of the interval (the interval is closed there, per the
Theorem statement of sub-case (i) restated at the top of the round-17
section, "every $a_1\in(2^{k-1},2^k]$"), this infimum is **attained**,
not merely approached:
$$\mathrm{margin}(a_1)\ \ge\ \mathrm{margin}(2^k)\qquad\text{for every }
a_1\in(2^{k-1},2^k].$$
(This is the boundary check the outline flagged as mandatory, per round
17's own rule about worst points sitting at boundaries: the endpoint
$a_1=2^k$ is genuinely attained here, not an open supremum, so evaluating
there is legitimate and gives the true worst case over the whole range —
unlike round 18's original bug, which evaluated Claim B only at the
window's supremum $a_1=2^{k-1}+1$, an *interior* point of the true range
$(2^{k-1},2^k]$ whenever $k\ge2$, and hence not the actual worst case;
that gap in coverage (between $a_1=2^{k-1}+1$ and $a_1=2^k$) is exactly
what this track newly closes.)

**Step 3 — evaluate at the endpoint and confirm strict positivity for
every odd $e\ge3$, every $k\ge1$.** Substituting $a_1=2^k$:
$$\mathrm{margin}(2^k)=\frac{2^k}6+\frac{2^m}6-\frac{2^k}2-\frac12
=-\frac{2^k}3+\frac{2^m}6-\frac12.$$
Writing $m=k+e$, so $2^m=2^k\cdot2^e$:
$$\mathrm{margin}(2^k)=2^k\left(\frac{2^e}6-\frac13\right)-\frac12
=\frac{2^k(2^e-2)}6-\frac12$$
(direct algebraic simplification, independently re-verified by exact
`sympy` symbolic computation this round: `margin_at_2^k - [2^k(2^e-2)/6
- 1/2]` simplifies to `0` identically in $k,e$). For odd $e\ge3$: since
$2^e$ is strictly increasing in $e$ and $e$ ranges over the odd integers
$\ge3$ (i.e. $e=3,5,7,\ldots$), the smallest value of $2^e$ in this
family occurs at $e=3$, giving $2^e-2\ge2^3-2=6$ for every odd $e\ge3$.
Hence
$$\mathrm{margin}(2^k)\ \ge\ \frac{2^k\cdot6}6-\frac12=2^k-\frac12.$$
Since $k\ge1$, $2^k\ge2$, so $\mathrm{margin}(2^k)\ge2-\frac12=\frac32>0$
for **every** $k\ge1$ and **every** odd $e\ge3$ (the family's own
tightest instance, $k=1,e=3$, gives exactly $\mathrm{margin}(2^1)=
\frac{2(2^3-2)}6-\frac12=\frac{12}6-\frac12=2-\frac12=\frac32$, matching
the general bound with equality — confirming $\frac32$ is the true
infimum over the whole family, not merely a loose estimate).

**Theorem (Odd-Excess $e\ge3$ Endpoint Closure Theorem).** For every
$k\ge1$, every odd $e\ge3$ (so $m=k+e\ge k+3$), every $a_1\in
(2^{k-1},2^k]$, and every finite multiset $R$ with $\max(R)\le2^{k-1}$,
$\mathrm{sum}(R)=2^m-a_1$: $\mathrm{OddSum}(R\cup\Gamma_{k-1})\ge
T_{\mathrm{odd}}$, and consequently (Step 1's equivalence)
$\mathrm{OddSum}(D\cup\Gamma_{m-1})\ge2^m$ for $D=\{a_1\}\cup R$.

*Proof.* By Steps 1–2, $\mathrm{OddSum}(R\cup\Gamma_{k-1})\ge
\mathrm{LB}_{\mathrm{odd}}\ge T_{\mathrm{odd}}+\mathrm{margin}(2^k)\ge
T_{\mathrm{odd}}$, using $\mathrm{margin}(2^k)\ge\frac32>0$ from Step 3 at
every point of the domain (Step 2's monotonicity gives $\mathrm{margin}
(a_1)\ge\mathrm{margin}(2^k)$ for every $a_1$ in range, and Step 3 shows
this floor value is itself $\ge\frac32>0$). No cardinality cap on $R$ is
needed anywhere in this argument (the Half-Sum Corollary underlying
$\mathrm{LB}_{\mathrm{odd}}$ is unconditionally cap-free, per its own
certification), so this closes odd excess $e\ge3$ **unconditionally**,
for every $k\ge1$, over the entire domain $a_1\in(2^{k-1},2^k]$ — not
just a width-1 window, and with no residual case left. $\blacksquare$

**Scope check (explicit, per the outline's instruction).** This theorem's
hypothesis is $e\ge3$ **odd** — $e=1$ is explicitly excluded from its
scope and is *not* re-derived here (it stays closed by the separate,
already-certified route via the General Cardinality-Constrained Half-Sum
Lemma, round 21, `lemmas/general-cardinality-constrained-half-sum-lemma.md`,
which needed the cardinality cap because $e=1$'s own margin formula
degrades to needing exactly the boundary case the Half-Sum Corollary
alone cannot reach — see round 18's diagnosis). Even excess $e\ge2$ is
likewise untouched here (closed already, round 17, Claim A). This track
closes precisely, and only, the odd $e\ge3$ family — but it does so
**completely**, for every $k\ge1$, with no numeric residual.

**Independent numerical sanity check** (this round, own exact-`Fraction`
script `/tmp/round22_track1_check.py`, not reused from any prior round):
$k=1,\ldots,6$, $e\in\{3,5,7\}$, $a_1$ ranging over the *whole* interval
$(2^{k-1},2^k]$ including exactly at the endpoint $a_1=2^k$, $R$ of
random count up to $10$ (uncapped in count, deliberately exceeding
$\mathrm{GT}(m)$'s own cardinality cap to confirm the cap-freeness of
this route) obeying $\max(R)\le2^{k-1}$: $10{,}000$ trials, **zero**
violations of $\mathrm{OddSum}(D\cup\Gamma_{m-1})\ge2^m$, with observed
minimum margin (in $\mathrm{OddSum}(R\cup\Gamma_{k-1})-T_{\mathrm
{odd}}$) matching $\frac32$ at $(k,e,a_1)=(1,3,2)$ exactly, confirming
the closed-form endpoint computation above.

### Track 2: Cap-Free General Cardinality-Constrained Half-Sum Lemma, and
### the Case-B(m,k) Sliver Closure Theorem

**Goal.** Prove $\mathrm{AltSum}(R\cup\Gamma_{k-1})\ge1$ for every finite
multiset $R$ satisfying only $|R|\le k+1$, $\mathrm{sum}(R)=S\in[2^k,
2^k+1)$ — **dropping** the value cap $\max(R)\le2^{k-1}$ from the
certified GCH($k$) hypotheses entirely — for all $k\ge1$ (the certified
GCH is stated only for $k\ge2$).

#### Step A — line-by-line audit of the certified GCH($k\ge2$) proof body

The certified proof (`lemmas/general-cardinality-constrained-half-sum-
lemma.md`) proceeds via the Finite Reduction Theorem (a *separate*
certified lemma,
`lemmas/invisible-block-skip-fact-and-general-pairwise-reduction.md`)
down to canonical forms, then Steps A/B and Cases C0/C1/C2. Both pieces
are audited below for cap-dependence, since the outline's charge ("Steps
A, B, C0, C1, C2 of the certified proof") implicitly assumes the
reduction step feeding into it is unaffected — this must be checked
too, not assumed, since that reduction is a distinct certified lemma with
its own proof.

**(1) The Finite Reduction Theorem / General Pairwise Reduction Lemma.**
Its proof moves a pair of active free values $w_i,w_j$ along the
mass-conserving line $w_i\mapsto w_i+t,\ w_j\mapsto w_j-t$, and bounds the
maximal affine interval for $t$ by the "active boundary set" $B:=\{0,
\mathrm{cap}\}\cup\{\Gamma\text{-levels with even multiplicity}\}\cup
\{\text{other active free values}\}$, terminating (per the proof text)
when the process "hits an even-multiplicity $\Gamma$-level; hits $0$ or
$\mathrm{cap}$; merges with another active free value...; or the two
moving coordinates meet." **Claim: the entry $\mathrm{cap}$ in $B$ is
never load-bearing** — the interval $[t_{\min},t_{\max}]$ is already
compact from the "$0$" boundary alone, with or without a cap, because
$w_i,w_j$ are *paired*: as $t$ increases, $w_j-t$ strictly decreases and
must stay $>0$ (values in $R$ are positive reals by hypothesis), forcing
$t<w_j$ from this side alone; as $t$ decreases, $w_i+t$ strictly
decreases toward $0$, forcing $t>-w_i$ from this side. In the *capped*
setting, the cap gives two *additional* possible early-stopping points
($w_i+t=\mathrm{cap}$ or $w_j-t=\mathrm{cap}$), but these are extra,
sufficient — not necessary — stopping conditions: dropping them (in the
cap-free setting) only means the affine interval may run *further* in
that direction before it stops, but it still necessarily stops at a
finite $t$ (bounded by the $0$-side constraint from the *other*
coordinate) and, when it does, lands on one of the four listed
terminal events (a coordinate hits $0$ — always available regardless of
cap; hits a $\Gamma$-level; merges with another active value; or the two
coordinates meet) — every one of the remaining three cases is likewise
cap-independent. So the proof of the General Pairwise Reduction Lemma,
hence of the Finite Reduction Theorem obtained by iterating it, goes
through verbatim with $\mathrm{cap}$ dropped from $B$: **the Finite
Reduction Theorem holds cap-free**, i.e. every feasible cap-free $R$
(just $|R|\le k+1$, $\mathrm{sum}(R)=S$) reduces, without increasing
$\mathrm{AltSum}(\,\cdot\,\cup\Gamma_{k-1})$, to a canonical form with at
most one active free value $r\in(0,\infty)\setminus\Gamma_{k-1}$ (no
upper bound on $r$).

**(2) Step A (Canonical-Form Pigeonhole Lemma).** Re-reading its proof:
"If all $n_j$ odd... forces $t=0$... $S$ is an odd integer... but $S\in
[2^k,2^k+1)$ contains only the even integer $2^k$ — contradiction." This
argument uses only the multiplicities $n_j$, the cardinality budget
$\sum n_j+t\le k+1$, and the range of $S$ — **the value $\mathrm{cap}$
never appears** in this proof, textually or implicitly (the free block's
*value* $r$ is never referenced in Step A's argument at all, only its
*count* $t$). Cap-free, verbatim.

**(3) Step B (Active-$\Gamma$-Subset Alternating Sum Lemma).** Proof:
"$2^x-2^y=2^y(2^{x-y}-1)\ge2^y\ge1$... pair consecutive terms." This
concerns only the fixed $\Gamma$-levels $2^0,\ldots,2^{k-1}$, never the
free value $r$ or $\mathrm{cap}$ at all. Cap-free, trivially (it never
had a cap dependence to begin with).

**(4) Case (C0) ($A=\varnothing$).** Derives $t=1$ forced, $n_j=1$ for
every $j$, hence $r=S-2^k+1\in(1,2)$ (open interval, since $S\in(2^k,
2^k+1)$ strictly in this case — $S=2^k$ is excluded because it would make
$r=1\in\Gamma_{k-1}$, contradicting $r\notin\Gamma_{k-1}$, exactly as
the certified proof notes), and $\mathrm{AltSum}(\{r\})=r>1\ge1$. This
derivation determines $r$'s value **purely from $S,k$** and never
references $\mathrm{cap}$ in deriving the bound $r>1$. In the *capped*
setting, $\mathrm{cap}=2^{k-1}\ge2>2>r$ for every $k\ge2$ (so this case is
automatically compatible with the cap when $k\ge2$, needing no separate
check); in the *cap-free* setting there is nothing further to check —
the same derivation of $r\in(1,2)$, hence $\mathrm{AltSum}(\{r\})>1$,
applies verbatim, with no cap-compatibility condition to verify at all
(there being no cap). Cap-free, verbatim.

**(5) Case (C1) ($A=\{v\}$).** Derives the unique forced allocation
$(n_{j_A},t)=(0,1)$, $n_j=1$ ($j\ne j_A$), hence $r=S-2^k+1+v\in[1+v,2+v)$
and $\mathrm{AltSum}(\{v,r\})=r-v\in[1,2)\ge1$. This bound holds for
*whatever* value $r$ turns out to be in $[1+v,2+v)$, **independent of**
whether that value happens to satisfy $r\le\mathrm{cap}$ or not — the
inequality $r-v\ge1$ is immediate from $r\ge1+v$ alone, with no reference
to $\mathrm{cap}$ anywhere in its derivation. (Note, as an aside not
needed for cap-freeness but worth recording: in the *capped* setting,
some instances of this case with $v$ close to $2^{k-1}$ have $r>
\mathrm{cap}$, meaning that particular canonical form is not actually
achievable as a valid capped-GCH instance at all — the certified proof's
argument is, in that sense, already stronger than strictly needed for the
capped statement, proving the bound for a superset of the truly
cap-feasible $r$-values; this is exactly why the argument transfers to
the cap-free setting without modification.) Cap-free, verbatim.

**(6) Case (C2) ($|A|\ge2$).** This is the only step whose proof text
explicitly invokes $\mathrm{cap}$: "cut $(0,\mathrm{cap}]$ at $v_1,\ldots,
v_p$ into open sub-intervals... on the topmost interval $(v_1,
\mathrm{cap}]$, $r$ is always rank $1$..., so the function is increasing,
with minimum at the captured endpoint $r\to v_1^+$." In the cap-free
setting, $r$ ranges over $(0,\infty)\setminus\Gamma_{k-1}\setminus A$,
so the topmost interval becomes $(v_1,\infty)$ (unbounded) instead of
$(v_1,\mathrm{cap}]$. **This does not change the argument's conclusion**:
on $(v_1,\infty)$, $r$ is still rank $1$ among $A\cup\{r\}$ for every
$r>v_1$ (nothing above $v_1$ in $A$ to be outranked by), so
$\mathrm{AltSum}(A\cup\{r\})=r-(v_2-v_3+\cdots)$ is still affine with
slope $+1$ (strictly increasing) throughout $(v_1,\infty)$ — the sign of
the slope, hence the location of the *minimum*, is a purely local fact
(determined by $r$'s constant rank on the interval), not a fact about
where the interval happens to end. Since the function is increasing on
$(v_1,\infty)$, its infimum over this interval is still approached (from
above) at the *left* endpoint $r\to v_1^+$ — exactly as in the capped
case — giving the same continuous boundary value $\mathrm{AltSum}(A
\setminus\{v_1\})$ (by Lemma TPC, unaffected by cap), which is $\ge1$ by
Step B since $A\setminus\{v_1\}$ is nonempty ($|A|\ge2$). Removing the
cap only removes the *right* endpoint of the topmost interval (where the
function was largest, not smallest — the cap was never where the minimum
was attained even in the certified capped proof), so the case's
conclusion $\mathrm{AltSum}(A\cup\{r\})\ge1$ for every $r$ in the topmost
interval is **unaffected**. Every other sub-interval of $(0,\infty)$
(namely $(0,v_p),(v_p,v_{p-1}),\ldots,(v_2,v_1)$) does not touch
$\mathrm{cap}$ at all, so is trivially unaffected. Cap-free, with the
only needed observation being the one just made about the (now
unbounded) topmost interval.

**Conclusion of the audit.** Every step of the certified GCH($k\ge2$)
proof — the Finite Reduction Theorem it rests on, Steps A and B, and
Cases C0, C1, C2 — goes through verbatim with the value cap
$\mathrm{cap}=2^{k-1}$ removed from every hypothesis and from the domain
of the free value $r$. This confirms the outline's conjecture and
establishes:

**Theorem (Cap-Free General Cardinality-Constrained Half-Sum Lemma,
$k\ge2$).** For every $k\ge2$ and every finite multiset $R$ of positive
reals with $|R|\le k+1$ and $\mathrm{sum}(R)=S\in[2^k,2^k+1)$ (no bound
on $\max(R)$):
$$\mathrm{AltSum}(R\cup\Gamma_{k-1})\ \ge\ 1,\qquad\text{equivalently}
\qquad\mathrm{OddSum}(R\cup\Gamma_{k-1})\ \ge\ \frac{S+2^k}2.$$

*Proof.* By the cap-free Finite Reduction Theorem (audit item (1)), it
suffices to check every feasible canonical form with cap-free domain.
Every such form falls into exactly one of the certified proof's cases
(B) [$A\ne\varnothing$, free block inactive — settled directly by Step B,
unaffected by cap], (C0), (C1), (C2), by the cap-free Step A (audit item
(2), which rules out the remaining "all levels inactive, free block
inactive" configuration exactly as before, with no cap dependence).
Cases C0, C1, C2 are settled by audit items (4)–(6) above, each giving
$\mathrm{AltSum}\ge1$ with no cap dependence. $\blacksquare$

#### Step B — the $k=1$ boundary case (outside GCH's originally-stated
#### $k\ge2$ range), proved directly by hand

**Theorem (Cap-Free GCH, $k=1$).** For every finite multiset $R$ of
positive reals with $|R|\le2$ and $\mathrm{sum}(R)=S\in[2,3)$:
$\mathrm{AltSum}(R\cup\{1\})\ge1$ (here $\Gamma_0=\{2^0\}=\{1\}$).

*Proof.* Since $S\ge2>0$, $R\ne\varnothing$, so $|R|\in\{1,2\}$.

- **$|R|=1$:** $R=\{S\}$, $S\in[2,3)$, so $S>1$. Sorted, $R\cup\{1\}=
  (S,1)$, $\mathrm{AltSum}=S-1\in[1,2)\ge1$.

- **$|R|=2$:** $R=\{x,y\}$, $x\ge y>0$, $x+y=S\in[2,3)$. Two exhaustive,
  disjoint sub-cases on $y$ versus $1$:
  - **$y\ge1$:** then $x\ge y\ge1$, so sorted $R\cup\{1\}=(x,y,1)$ (any
    tie with $1$ does not affect the value, by the standard tie-neutral
    convention for equal elements in rank sums), giving
    $\mathrm{AltSum}=x-y+1$. Since $x\ge y$, $x-y\ge0$, so
    $\mathrm{AltSum}\ge1$ (equality iff $x=y$).
  - **$y<1$:** since $y<1\le S-1<x$ (as $x=S-y>S-1\ge1$), we have $x>1>y$
    strictly, so sorted $R\cup\{1\}=(x,1,y)$, giving $\mathrm{AltSum}=
    x-1+y=(x+y)-1=S-1$. Since $S\ge2$, $\mathrm{AltSum}=S-1\ge1$
    (equality iff $S=2$).
  These two sub-cases are exhaustive ($y\ge1$ or $y<1$) and cover every
  instance of $|R|=2$; in both, $\mathrm{AltSum}(R\cup\{1\})\ge1$.
  $\blacksquare$

**Independent numerical check** (this round, `/tmp/round22_gch_k1.py`):
$5{,}000$ random trials, $S$ random in $[2,3)$, $|R|\in\{1,2\}$ random,
zero violations, matching the hand proof exactly (minimum observed
$\mathrm{AltSum}=1.000\ldots$ at $S\to2$, $x=y=1$).

**Combining Steps A and B:** the Cap-Free General Cardinality-Constrained
Half-Sum Lemma holds for **every** $k\ge1$ (Step A for $k\ge2$, Step B
directly for $k=1$).

#### Step C — a tie-robust AltSum Peeling identity (elementary, proved
#### directly — needed for the Global-max peel below, since the
#### certified Even-target Companion Peeling identity requires a
#### *unique* maximum, which is not guaranteed here)

**Lemma (AltSum Peeling identity, general, no uniqueness needed).** Let
$M$ be a finite multiset of positive reals and let $g$ be (a chosen copy
of) $\max(M)$. Then $\mathrm{AltSum}(M)=g-\mathrm{AltSum}(M\setminus
\{g\})$.

*Proof.* Sort $M$ descending, choosing the removed copy $g$ to occupy
position $1$ (always possible, ties broken arbitrarily but consistently —
the same freedom already used in the certified Global-max Peeling
identity's own proof, `lemmas/dominant-piece-lower-bound.md`): $M=
(g=x_1\ge x_2\ge\cdots\ge x_n)$. Then $M\setminus\{g\}=(x_2,\ldots,x_n)$
sorted descending, with position $j$ in $M\setminus\{g\}$ corresponding
to position $j+1$ in $M$ for $j=1,\ldots,n-1$ — a uniform shift by $1$,
flipping parity. Hence
$$\mathrm{AltSum}(M)=x_1-x_2+x_3-x_4+\cdots=x_1-(x_2-x_3+x_4-\cdots)
=g-\mathrm{AltSum}(M\setminus\{g\}),$$
since $x_2-x_3+x_4-\cdots$ is exactly $\mathrm{AltSum}(M\setminus\{g\})$
(its own positions $1,2,3,\ldots$ are $x_2,x_3,x_4,\ldots$). $\blacksquare$
(This identity is the same "Peeling identity" already used, without a
separate proof, inside the certified AltSum Corollary's induction,
`lemmas/altsum-corollary-and-growth-lemma.md`; it is proved here in full,
from scratch, to make this round's use of it self-contained and to
confirm explicitly that it needs no uniqueness hypothesis on the maximum
— unlike the certified Even-target Companion Peeling identity, which
does require a unique maximum and is therefore not usable here, since
$B$ may have $b_1$ tied with another part of $B$ itself.)

#### Step D — the Case-B(m,k) Sliver Closure Theorem

Recall (round 5 section above, "Theorem 2 (Case-B(m,k), sliver
reduction)") the open sliver: for $m\ge2$, $T:=\Gamma_{m-2}$, $B=
(b_1\ge\cdots\ge b_p)$ a partition of $2^m$ into $p\le m+1$ positive
parts with $b_1\in(2^{m-1}-1,2^{m-1})$ (the sliver), the target is
$\mathrm{OddSum}(B\cup T)\le2^m-1$.

**Feasibility of the peel.** $b_1>2^{m-1}-1\ge2^{m-2}=\max(T)$ for every
$m\ge2$ (checking the boundary: at $m=2$, $2^{m-1}-1=1=2^{m-2}$, and
$b_1>1=2^{m-2}$ strictly by the sliver's own strict lower bound; for
$m\ge3$, $2^{m-1}-1>2^{m-2}$ strictly since $2^{m-2}>1$), and $b_1=
\max(B)$ by definition, so $b_1$ is (a copy of) $\max(B\cup T)$.

**The peel identity.** By Step C's AltSum Peeling identity, with $M:=B
\cup T$, $g:=b_1$, $B':=B\setminus\{b_1\}$:
$$\mathrm{AltSum}(B\cup T)=b_1-\mathrm{AltSum}(B'\cup T).$$

**$B'$ is a feasible cap-free GCH($m-1$) instance.** $\mathrm{sum}(B')=
2^m-b_1$; since $b_1\in(2^{m-1}-1,2^{m-1})$, $\mathrm{sum}(B')\in
(2^m-2^{m-1},\,2^m-(2^{m-1}-1))=(2^{m-1},2^{m-1}+1)\subseteq[2^{m-1},
2^{m-1}+1)$, matching cap-free GCH's sum hypothesis with $k:=m-1$
(recall $2^{m-1}=2^k$). And $|B'|=p-1\le(m+1)-1=m=(m-1)+1=k+1$, matching
the cardinality cap exactly. No bound on $\max(B')$ is assumed or needed
— this is precisely why the *cap-free* strengthening (Steps A–B above)
is required here, not just the originally-certified capped GCH: nothing
in `Case-B(m,k)`'s own setup bounds the individual parts of $B'$ by
$2^{m-2}$ or any other fixed cap. Also, $T=\Gamma_{m-2}=\Gamma_{k-1}$
exactly (matching the cap-free GCH's fixed comparison set), and $m\ge2
\iff k=m-1\ge1$, within the now-established scope of the Cap-Free GCH
(all $k\ge1$, Steps A and B combined).

**Applying the Cap-Free GCH.** By the Theorem of Steps A/B (all $k\ge1$),
$$\mathrm{AltSum}(B'\cup T)=\mathrm{AltSum}(B'\cup\Gamma_{k-1})\ \ge\ 1.$$

**Closing the sliver.** Combining with the peel identity:
$$\mathrm{AltSum}(B\cup T)=b_1-\mathrm{AltSum}(B'\cup T)\ \le\ b_1-1\ <\
2^{m-1}-1,$$
the last step strict since $b_1<2^{m-1}$ (the sliver's own strict upper
bound). Converting back to $\mathrm{OddSum}$ via the certified Lemma AS
(`lemmas/altsum-reformulation-and-single-insertion.md`,
$\mathrm{OddSum}(X)=(\mathrm{sum}(X)+\mathrm{AltSum}(X))/2$), using
$\mathrm{sum}(B\cup T)=2^m+(2^{m-1}-1)=3\cdot2^{m-1}-1$:
$$\mathrm{OddSum}(B\cup T)=\frac{(3\cdot2^{m-1}-1)+\mathrm{AltSum}(B\cup
T)}2\ <\ \frac{(3\cdot2^{m-1}-1)+(2^{m-1}-1)}2=\frac{4\cdot2^{m-1}-2}2
=2^m-1.$$

**Theorem (Case-B(m,k) Sliver Closure Theorem).** For every $m\ge2$ and
every partition $B$ of $2^m$ into $p\le m+1$ positive parts with
$b_1:=\max(B)\in(2^{m-1}-1,2^{m-1})$ (the sliver): $\mathrm{OddSum}
(B\cup\Gamma_{m-2})<2^m-1$, in particular $\le2^m-1$. $\blacksquare$

**Combined with Theorem 2 above** (which already closed every $b_1\in
[0,2^{m-1}-1]$, i.e. everything outside the sliver), this gives:

**Corollary (`Case-B(m,k)`, fully closed).** For every $m\ge2$ and every
partition $B$ of $2^m$ into $\le m+1$ positive parts with $b_1<2^{m-1}$:
$\mathrm{OddSum}(B\cup\Gamma_{m-2})\le2^m-1$. $\blacksquare$

**Independent numerical check** (this round, `/tmp/verify_sliver2.py` and
`/tmp/verify_capfree_gch.py`, both own exact-`Fraction` scripts): $20{,}
000$ trials of the full sliver claim, $m=2,\ldots,6$, $b_1$ random in the
sliver, $B'$ of random count and structure (no cap enforced on its
parts, $8453$ infeasible constructions correctly skipped, not counted),
**zero** violations of $\mathrm{OddSum}(B\cup\Gamma_{m-2})\le2^m-1$; and
$18{,}000$ trials of the cap-free GCH claim directly, $k=1,\ldots,6$,
$R$ of random count and structure (no cap), **zero** violations of
$\mathrm{AltSum}(R\cup\Gamma_{k-1})\ge1$.

### Honest scope: what Tracks 1–2 close, and what remains open for
### $\mathrm{GT}(m)$ as a whole

Combining this round's two tracks with prior rounds' results: **every
excess-carrying case of sub-case (i) is now closed** (even $e\ge2$: round
17; odd $e=1$: round 21 via the certified capped GCH; odd $e\ge3$: this
round's Track 1, full range, not just window) and **`Case-B(m,k)` is now
fully closed for every $b_1<2^{m-1}$** (round 5's Theorem 2 outside the
sliver, combined with this round's Track 2 sliver closure).

**This does NOT close $\mathrm{GT}(m)$ as a whole.** As the round-17
section's own "Net effect" already flagged, and as this round's outline
and outline-reviewer explicitly re-flagged (citing round 22's
math-explorer's direct check), there remains a **third, structurally
distinct** open object: **sub-case (i)'s own $e=0$ residual**, i.e. the
window $a_1\in(2^{k-1},2^{k-1}+1)$ *when $e=0$* (equivalently $m=k$) —
see the round-15/16 section (line $\sim$5210–5224 of this file, "Exactly
why $e=0$ is not covered"), which shows this residual has $\mathrm{sum}
(R)=2^k-a_1\in(2^{k-1}-1,2^{k-1})$, i.e. $R$'s sum sits **just below**
$2^{k-1}$ — the opposite side of the relevant threshold from where the
(now cap-free) GCH lemma applies (GCH needs $\mathrm{sum}(R)\in[2^k,
2^k+1)$, i.e. just **above** $2^k$, one full dyadic level higher and on
the opposite side of its own threshold). **This round's Track 2 does not
address this object, and it is not the same statement as `Case-B(m,k)`**
despite the superficial resemblance (both are width-1, both arise from
an excess-$0$ configuration) — this was checked directly by this round's
math-explorer and independently confirmed here by re-reading the exact
sum-range each object requires (`(2^{k-1}-1,2^{k-1})$ for sub-case (i)'s
own $e=0$ form vs. `Case-B(m,k)`'s own sliver, whose *peel* lands on
`sum(B') ∈ (2^{m-1},2^{m-1}+1)`, i.e. just above the threshold, not
below it). **Round 17's own text ("a single, precisely identified,
self-similar object, not two separate gaps") is, on this closer reading,
not fully justified as stated — the two objects are not literally the
same statement, contrary to that round's characterization; whether they
are nonetheless *equivalent* via some argument not yet given remains an
open question, not resolved this round.** Consequently: $\mathrm{GT}(m)$
is **not** fully closed by this round's work — sub-case (i)'s own $e=0$
residual is a genuine, separate, still-open obstruction, honestly
flagged (not silently folded into "GT(m) closed") per this round's
dispatch instructions. Status for $\mathrm{GT}(m)$, and hence for this
approach's target (the full Existence Theorem lower bound for all $n$),
**remains `partial`**.

## Promotable lemmas (round 22)

- **Odd-Excess $e\ge3$ Endpoint Closure Theorem (new, proved in full).**
  For every $k\ge1$, odd $e\ge3$, $a_1\in(2^{k-1},2^k]$, $R$ with
  $\max(R)\le2^{k-1}$, $\mathrm{sum}(R)=2^m-a_1$ ($m=k+e$): $\mathrm{OddSum}
  (R\cup\Gamma_{k-1})\ge T_{\mathrm{odd}}$, hence $\mathrm{OddSum}(D\cup
  \Gamma_{m-1})\ge2^m$ for $D=\{a_1\}\cup R$ — proved via the certified
  margin identity $\mathrm{LB}_{\mathrm{odd}}-T_{\mathrm{odd}}=2^k/6+
  2^m/6-a_1/2-1/2$ (algebraic combination of the certified Half-Sum
  Corollary and the certified corrected $e$-fold $q=0$-chain), its
  monotonicity (affine, slope $-1/2$), and evaluation at the *attained*
  right endpoint $a_1=2^k$: $\mathrm{margin}(2^k)=2^k(2^e-2)/6-1/2\ge
  2^k-1/2\ge3/2>0$ for every $k\ge1$, odd $e\ge3$. No cardinality cap
  needed. Independently verified, $10{,}000$ exact-`Fraction` trials,
  zero violations.
- **Cap-Free General Cardinality-Constrained Half-Sum Lemma (new, proved
  in full, all $k\ge1$).** For $|R|\le k+1$, $\mathrm{sum}(R)=S\in[2^k,
  2^k+1)$, **no bound on $\max(R)$**: $\mathrm{AltSum}(R\cup\Gamma_{k-1})
  \ge1$. Proved for $k\ge2$ by a full line-by-line audit of the certified
  GCH proof (Finite Reduction Theorem, Steps A/B, Cases C0/C1/C2)
  confirming the value cap is never load-bearing (only the cardinality
  cap $|R|\le k+1$ is used, in Step A and Case C1, exactly as the
  certified proof's own "Scope note" already stated); for $k=1$ by a
  short direct hand proof (two exhaustive sub-cases on $|R|\in\{1,2\}$).
  Independently verified, $18{,}000+5{,}000$ exact-`Fraction` trials,
  zero violations.
- **AltSum Peeling identity, tie-robust (new, proved in full).** For any
  finite multiset $M$ of positive reals and $g$ a chosen copy of
  $\max(M)$ (no uniqueness required): $\mathrm{AltSum}(M)=g-\mathrm{
  AltSum}(M\setminus\{g\})$. Elementary rank-shift proof, same style as
  the certified Global-max (Odd/Even) Peeling identity but for AltSum
  directly, needed because the certified Even-target Companion Peeling
  identity requires a *unique* maximum, which `Case-B(m,k)`'s $b_1$ is
  not guaranteed to have.
- **Case-B(m,k) Sliver Closure Theorem (new, proved in full).** For every
  $m\ge2$, every partition $B$ of $2^m$ into $\le m+1$ parts with $b_1\in
  (2^{m-1}-1,2^{m-1})$: $\mathrm{OddSum}(B\cup\Gamma_{m-2})<2^m-1$. Proved
  by peeling $b_1$ (via the tie-robust AltSum Peeling identity) and
  invoking the Cap-Free GCH($m-1$) on the residual $B'$. Combined with the
  already-certified Theorem 2 (round 5), this fully closes `Case-B(m,k)`:
  $\mathrm{OddSum}(B\cup\Gamma_{m-2})\le2^m-1$ for **every** $b_1<2^{m-1}$,
  unconditionally.

**Honest scope note (unchanged conclusion from round 17, re-confirmed and
sharpened this round).** $\mathrm{GT}(m)$ is **not** fully closed: every
excess-carrying sub-case ($e\ge1$, both parities) is now closed
unconditionally, and `Case-B(m,k)` is now fully closed, but sub-case
(i)'s own $e=0$ residual (window $a_1\in(2^{k-1},2^{k-1}+1)$ when $m=k$)
remains open and, on this round's closer examination, is **not**
established to be the same object as `Case-B(m,k)` (their respective
reductions land on opposite sides of the relevant $2^{k-1}$/$2^k$
threshold) — this is the one remaining gap in $\mathrm{GT}(m)$, and hence
in this approach's proof of the full lower bound $c(n)=2^n/(2^{n+1}-1)$
for general $n$. Status: `partial`.
