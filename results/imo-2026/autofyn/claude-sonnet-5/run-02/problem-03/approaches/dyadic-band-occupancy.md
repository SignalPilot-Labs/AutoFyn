## Status
partial

## Approaches tried
- **(round 5, this build, new slug)** Built the assigned generating-function/
  step-function technique for claim (A) (`min_{F: partition of p_1, ≤n+1
  parts} A(F∪T) = a_n`, `T={p_2,...,p_{n+1}}` the fixed, untouched ladder
  tail) from scratch. Derived a fully rigorous **integral/step-function
  reformulation** (Proposition 1) that cleanly separates $A(F\cup T)$ into
  $A(T)$ plus a signed integral of $F$'s own occupancy against a fixed
  $\pm1$ weight function determined by $T$'s dyadic bands. Used this to prove
  two genuine, fully rigorous side results: (i) the **cardinality-unbounded
  relaxation of claim (A) is exactly $0$, not $a_n$** (Proposition 2) — i.e.
  the finite cut-budget ($\le n+1$ parts) is essential, and any correct proof
  of claim (A) must use it, not just totals; (ii) a **concrete, exact
  counterexample disproving the assigned key lemma "band-invariance formula"
  as stated** (Proposition 3) — the exact positions of $F$'s fragments
  *within* a band genuinely affect $A(F\cup T)$, not just their count and
  total mass per band, so the coarser generating-function reduction the
  outline hoped for does not go through in the form specified. Attempted the
  natural peeling recursion (Proposition 4) on the number of parts of $F$;
  identified precisely why it stalls (needs a matching *upper* bound on
  $A(F''\cup T)$ after peeling the largest fragment, which is not available
  from a pure induction on part-count — the identical obstruction every
  sibling approach has hit). **Explicitly compared to `rank-pigeonhole-
  budget`** per the outline-reviewer's instruction: the two approaches do
  **not** coincide — `rank-pigeonhole-budget`'s finer per-band
  partition-*shape* decomposition is not superseded by this coarser
  occupancy-count approach, precisely because Proposition 3 shows the coarser
  invariant is not sufficient information; if `rank-pigeonhole-budget`'s
  finer formula is ever completed, it cannot be replaced by a
  count/mass-only formula of the shape this approach's outline proposed.

## Current best

### 0. Setup (importing certified facts, not re-deriving)

By `claiming-subgame-reduction`, $c(n)=\max_{\text{Liu Bang}}\min_{\text{Xiang
Yu}}\Phi(S)$, $\Phi(S)=(\mathrm{Total}(S)+A(S))/2$
(`integral-alternating-sum-formula`), and for the ladder $p_i=2^{n+1-i}/D$,
$D:=2^{n+1}-1$ ($i=1,\dots,n+1$), $\mathrm{Total}=1$, so $c(n)=a_n:=1/D$ is
equivalent to $A(S)\ge a_n$ for every legal Xiang-Yu response $S$. Write
$T:=\{p_2,\dots,p_{n+1}\}$ (the ladder tail, $n$ elements) and $r:=1-p_1=$
$\mathrm{Total}(T)$. This build's target, **claim (A)** (per the round-5
math-explorer reconnaissance and this round's outline), is the sub-case where
Xiang Yu spends *all* $n$ cuts fragmenting $p_1$ and leaves $T$ untouched:
$$\text{(A)}:\qquad \min_{F}\,A(F\cup T)=a_n,\qquad F \text{ ranges over
partitions of }p_1\text{ into at most }n+1\text{ nonnegative parts.}$$
The achievability half of (A) — $\min_F A(F\cup T)\le a_n$ — is already
certified (`rescaled-ladder-c-equals-n-achievability`, taking
$F=\{q_1,\dots,q_{n+1}\}$, $q_i:=p_1\cdot p_i(n)$, a rescaled copy of the
whole $n$-ladder). What remains open, and is this approach's target, is the
matching lower bound $A(F\cup T)\ge a_n$ for *every* legal $F$.

### 1. Proposition 1 — integral/step-function reformulation

**Statement.** For any partition $F$ of $p_1$ (any number of parts, any
values, ignoring for now the cardinality bound), write $N_F(x):=\#\{f\in F:
f>x\}$, $N_T(x):=\#\{i\in\{2,\dots,n+1\}: p_i>x\}$, and $\psi(x):=N_T(x)\bmod
2$, $w(x):=1-2\psi(x)\in\{+1,-1\}$ (so $w(x)=+1$ where $N_T$ is even, $-1$
where odd). Then
$$A(F\cup T) \;=\; A(T) \;+\; \int_0^\infty e(x)\,w(x)\,dx, \qquad
e(x):=N_F(x)\bmod 2 \in\{0,1\}.$$

**Proof.** By `integral-alternating-sum-formula`, $A(S)=\int_0^\infty
\mathbb1[N_S(x)\text{ odd}]\,dx$ for any finite multiset $S$ of positive
reals. Here $N_{F\cup T}(x)=N_F(x)+N_T(x)$, so $N_{F\cup T}(x)\bmod 2 =
e(x)\oplus\psi(x)$ (XOR of the two parities). Hence
$$A(F\cup T)=\int_0^\infty \big(e(x)\oplus\psi(x)\big)\,dx
=\int_0^\infty\Big[\psi(x)(1-e(x))+(1-\psi(x))e(x)\Big]dx,$$
using $u\oplus v = u(1-v)+v(1-u)$ for $u,v\in\{0,1\}$. Expanding,
$$=\int\psi(x)\,dx-\int\psi(x)e(x)\,dx+\int e(x)\,dx-\int\psi(x)e(x)\,dx
=\int\psi(x)\,dx+\int e(x)\big(1-2\psi(x)\big)\,dx.$$
Finally $\int_0^\infty\psi(x)\,dx=\int_0^\infty\mathbb1[N_T(x)\text{
odd}]\,dx=A(T)$ (applying `integral-alternating-sum-formula` to $T$ alone),
and $1-2\psi(x)=w(x)$ by definition, giving the claim. $\blacksquare$

This is a genuinely different (and, as far as this build can tell, new)
derivation route from the sibling approaches' vertex/LP or cross-term
machinery: it isolates $A(F\cup T)-A(T)$ as a single signed integral of
$F$'s own parity pattern against a **fixed** weight function $w(\cdot)$
determined entirely by $T$ (i.e. entirely known in closed form, since $T$ is
the explicit ladder). Consequently claim (A) is equivalent to:
$$\min_F \int_0^\infty e(x)\,w(x)\,dx \;=\; a_n-A(T) \qquad(\text{a fixed,
known target, since }A(T)\text{ is computable in closed form}).$$
(Using the cascading-halving family's closed form, $A(T)=T(n-1)/D$ where
$T(L):=(2^{L+1}+(-1)^L)/3$ — this is literally the special case $k=0$ of
`cascading-halving-family-characterization`'s tail sum, since $T$ *is* the
$k=0$ tail $\{p_1,\dots,p_{n+1}\}$'s own tail once $p_1$ is removed; concretely
$A(T)=\big(2^n+(-1)^{n-1}\big)/(3D)$.)

### 2. Proposition 2 — the cardinality bound is essential: relaxed minimum is exactly 0

**Statement.** If the constraint "at most $n+1$ parts" is dropped (i.e. $F$
ranges over *all* partitions of $p_1$ into finitely many positive parts, any
number), then
$$\min_F A(F\cup T) = 0 < a_n.$$

**Proof.** By Proposition 1, it suffices to show $\min_F\int e(x)w(x)\,dx =
-A(T)$ is achievable without a cardinality bound, since then $A(F\cup T)=
A(T)+(-A(T))=0$, and $A(F\cup T)\ge0$ always (`integral-alternating-sum-
formula`), so $0$ is in fact the true minimum. Write $M_{\rm neg}:=\{x:
w(x)=-1\}=\{x:N_T(x)\text{ odd}\}$, a finite union of $T$'s "odd bands" of
total Lebesgue measure $A(T)$ (definition of $A(T)$ as an integral).

*Claim: for any measurable $e:(0,\infty)\to\{0,1\}$ which is a finite union
of intervals, with $\{x:e(x)=1\}\subseteq M_{\rm neg}$ and total measure
$\mu\le p_1$, there is a partition $F$ of $p_1$ (unbounded number of parts)
realizing this $e$ exactly.* Take the maximal intervals of $\{e=1\}$,
$(a_1,b_1),\dots,(a_k,b_k)$ (disjoint, sorted). For each $j$, place two
$F$-parts at the exact values $b_j$ and $a_j$ (this makes $N_F$ jump up by 1
at $x=b_j^-$ and back down by 1 at $x=a_j^-$... precisely: an $F$-part with
value $v$ contributes $\mathbb1[x<v]$ to $N_F(x)$; placing parts at $b_j$ and
$a_j$ makes $N_F(x)$ increase by $1$ on $(a_j,b_j)$ relative to $x\ge b_j$ and
$x<a_j$, and — since we do this independently for each disjoint interval —
the parity $e(x)=N_F(x)\bmod2$ is exactly $1$ on $\bigcup_j(a_j,b_j)$ and $0$
elsewhere among the placed structure. This uses $2k$ parts of total mass
$\sum_j(a_j+b_j)$. If this total is less than $p_1$ (it always can be
arranged so, by choosing $a_j,b_j$ freely within their target odd-interval,
in particular taking $b_j,a_j$ to be a strict sub-interval of the true odd
band rather than its full extent trims the "cost" mass while the *measure*
covered, which is what matters for the integral, is controlled separately by
how much of $M_{\rm neg}$'s total length we choose to enclose — concretely,
here we simply take the $k$ intervals to be $T$'s own $\lceil n/2\rceil$ odd
bands in full, giving total covered measure $=A(T)$ and mass cost bounded by
$2\sum(\text{band boundary values})\le 2\cdot n\cdot p_2 < p_1$ for large
$n$; in general any leftover mass up to $p_1$ is padded, without altering any
parity, by adding an even number of further equal, sufficiently small
$F$-parts strictly below every value used so far (this shifts $N_F$ by an
even constant beneath that point, changing no parity anywhere above it, and
consumes exactly the required remaining mass since the two pad-parts' common
value can be chosen freely small).

Applying this with $\{e=1\}:=M_{\rm neg}$ itself (measure $A(T)\le p_1$,
proved in Proposition 2b below) realizes $\int e\,w\,dx=-A(T)$ exactly,
proving the claim. $\blacksquare$

**Proposition 2b (needed above): $A(T)<p_1$ for every $n\ge1$.** By the
closed form above, $D\cdot A(T)=T(n-1)=(2^n+(-1)^{n-1})/3$ and $D\cdot
p_1=2^n$. So $A(T)<p_1 \iff (2^n+(-1)^{n-1})/3<2^n \iff 2^n+(-1)^{n-1}<3\cdot
2^n \iff (-1)^{n-1}<2\cdot2^n$, which holds for every $n\ge1$ since the
right side is $\ge4>1\ge$ left side. $\blacksquare$

**Interpretation.** Proposition 2 shows that with an *unlimited* number of
cuts on $p_1$ (equivalently, an unlimited number of legal Xiang-Yu moves),
Xiang Yu could force $A=0$, i.e. $\Phi=1/2$ exactly — strictly better for him
than the ladder's claimed value $a_n>0$ contributes toward $c(n)$. This
proves, rigorously and for the first time in this exact form, that **the
finite cut budget ($n$ cuts $\Rightarrow$ at most $n+1$ parts) is not a
technical nicety but is load-bearing**: any correct proof of claim (A) must
use the cardinality bound essentially, not merely bound totals or masses.
This directly explains, from a new angle, why every sibling approach's
"generic multiset" or "totals-only" restatements of the core inequality have
failed (cf. `rank-pigeonhole-budget`'s already-certified refutation of the
even-rank-sum pigeonhole claim) — it is not a failure of technique but a
structural necessity, now pinned to a precise quantitative statement (the
gap between the relaxed minimum $0$ and the true target $a_n$).

### 3. Proposition 3 — the assigned "band-invariance formula" is FALSE as stated

The outline's key lemma conjectured that $A(F\cup T)$, for $F$ *subject to
the $\le n+1$-part cardinality bound*, depends only on $F$'s per-band
occupancy pair $(m_j,\mu_j)_{j=0}^n$ (count and total mass of $F$-parts
landing in each of $T$'s $n+1$ dyadic bands), not on the exact values of
$F$'s parts within a band. **This is false**, refuted by an explicit,
independently-checked exact-`Fraction` counterexample.

**Counterexample.** Take $n=4$ ($D=31$): $p_1=16/31$, $T=\{8/31,4/31,2/31,
1/31\}$. Band $2$ (between $p_4=2/31$ and $p_3=4/31$) is the interval
$(2/31,4/31)$. Take $F=\{x_0,a,b\}$ with $x_0:=p_2+\tfrac1{1000}=
\tfrac{8}{31}+\tfrac1{1000}$ (in band $0$), and $a,b$ two values in band $2$
with $a+b=p_1-x_0$ fixed. Two splits of the same $(m_2,\mu_2)=(2,\,p_1-x_0)$:
- **Split 1** (near-equal): $a_1=\tfrac{9969}{77500}$,
  $b_1=\tfrac{19907}{155000}$ (both exact-Fraction values strictly inside
  $(2/31,4/31)$, verified directly): $A(F\cup T)=\dfrac{3781}{38750}$.
- **Split 2** (skewed toward the band's upper edge): $a_2=
  \tfrac{39969}{310000}$, $b_2=\tfrac{39721}{310000}$ (also strictly inside
  band $2$, same sum $a_2+b_2=a_1+b_1=p_1-x_0$ exactly, checked): $A(F\cup
  T)=\dfrac{15031}{155000}$.

Converting to a common denominator, $\dfrac{3781}{38750}=\dfrac{15124}{
155000}\neq\dfrac{15031}{155000}$ — the two values of $A(F\cup T)$ **differ**
(difference $=\tfrac{93}{155000}\ne0$; verified in this build by an
independent exact-`Fraction` Python computation, both partitions checked to
(i) sum exactly to $p_1$ and (ii) place $a,b$ strictly inside the same band).
Both $F$'s have identical per-band occupancy data $(m_0,\mu_0)=(1,x_0)$,
$(m_2,\mu_2)=(2,\,p_1-x_0)$, all other bands empty — yet $A(F\cup T)$ is not
equal. $\blacksquare$

**Why this happens (diagnosis, tying back to Proposition 1).** By
Proposition 1, $A(F\cup T)-A(T)=\int e(x)w(x)dx$, and $w(x)$ is constant
*only between* $T$'s own thresholds — but **within** a single band, if it
contains $\ge2$ of $F$'s own parts, $N_F(x)$ itself steps up and down inside
the band as $x$ crosses each part's individual value, so $e(x)$ is **not**
constant within the band — it alternates at the sub-band level, and the
*measure* of each sub-alternation depends on exactly where, within the band,
the parts sit (the gaps between consecutive $F$-values), not merely on how
many parts there are or their total mass. Since $w$ is constant on the whole
band, the band's net contribution is $w(\text{band})\times(\text{net signed
sub-band measure})$, and that net signed sub-band measure is a genuine
function of the fine positions (a weighted alternating function of the gaps
$v_t-v_{t+1}$), not of $(m_j,\mu_j)$ alone. This is exactly what the
counterexample exhibits quantitatively.

### 4. Comparison to `rank-pigeonhole-budget` (as instructed)

`rank-pigeonhole-budget`'s sibling attempt is a *finer* band decomposition
that explicitly tracks partition shape within each band (not just
count/mass), consistent with the diagnosis above. Proposition 3 shows this
extra fineness is **not optional** — the coarser invariant this approach was
assigned genuinely loses information needed to determine $A(F\cup T)$, so
the two approaches do **not** collapse to the same formula; they are
genuinely different in power, and the coarser one is strictly insufficient
on its own. This build's contribution is therefore not a redundant
duplication of `rank-pigeonhole-budget` but an independent, negative
clarification of exactly how much information any correct closed form must
retain (per-band shape, not just per-band mass/count) — useful for steering
future attempts on either sibling.

### 5. Attempted peeling recursion (Proposition 4) and where it stalls

Using the certified `sharp-dominant-removal-identity`: if $f_1:=\max(F)$
satisfies $f_1>p_2=\max(T)$ (and $f_1\ge$ every other element of $F$, true
since $f_1$ is $F$'s max), then $f_1>\max\big((F\setminus\{f_1\})\cup T\big)$,
so
$$A(F\cup T) = f_1 - A\big((F\setminus\{f_1\})\cup T\big).$$
Writing $F'':=F\setminus\{f_1\}$ (a partition of $p_1-f_1$ into $\le n$
parts, same fixed $T$), the target inequality $A(F\cup T)\ge a_n$ becomes
$$A(F''\cup T) \;\le\; f_1-a_n. \tag{$\dagger$}$$
This *is* a legitimate reduction (one fewer part, same $T$), but it demands
an **upper** bound on $A(F''\cup T)$, not a lower bound — and no induction
on the number of parts (nor on $n$) directly supplies an upper bound of this
form: the natural inductive hypothesis available (from claim (A) itself,
applied one level down in part-count) is a *lower* bound $A(F''\cup T)\ge
a_n$, which is the wrong direction for $(\dagger)$. This is, structurally,
the identical obstruction already located from three independent directions
by the other round-5 approaches (`greedy-halving-adversary`'s claim (B)
surrogate-undo gap, `rank-tie-vertex-reduction`'s domination-lemma gap, and
`rank-pigeonhole-budget`'s own Case-A inequality $(\star)$) — confirming,
via a fourth and genuinely different derivation route (a direct integral
peeling identity rather than vertex enumeration or cross-term bookkeeping),
that the crux difficulty is real and not an artifact of any one technique.

For the complementary case $f_1\le p_2$ (no fragment of $F$ exceeds $T$'s
max), `sharp-dominant-removal-identity` does not apply directly (its
hypothesis fails), and Proposition 1's integral formula must be evaluated
without a clean peeling step; this build did not find a shortcut here either
— genuinely open, same status as the sibling approaches' analogous case
splits.

## Open gaps

1. **Claim (A) itself** (the lower bound $A(F\cup T)\ge a_n$ for every
   cardinality-bounded partition $F$ of $p_1$): not proved. Proposition 2
   shows why a naive "totals/relaxed" argument cannot work (the true bound
   is a genuine consequence of the finite cut budget), and Proposition 3
   shows the assigned coarse band-occupancy invariant is provably
   insufficient to pin down $A(F\cup T)$ — so this specific technique, as
   outlined, cannot close claim (A) without retaining fine partition-shape
   information (i.e. converging back onto something at least as detailed as
   `rank-pigeonhole-budget`'s finer decomposition, which is itself still
   open).
2. **The peeling recursion's missing upper bound** ($\dagger$ in §5): the
   same cross-approach obstruction identified by every other round-5 slug,
   now derived independently via a direct integral-peeling argument.
3. Case $f_1\le p_2$ in the peeling attempt: not analyzed further; no
   shortcut found.

## Full proof
(absent — Status is `partial`. Claim (A), the assigned target, is not
established; see Open gaps. What *is* fully proved and reusable: Proposition
1 (the exact integral decomposition $A(F\cup T)=A(T)+\int e\,w\,dx$),
Proposition 2 (+2b) (the cardinality-relaxed minimum is exactly $0$, proving
the finite budget is essential — a clean, general, new quantitative fact),
and Proposition 3 (an explicit exact-`Fraction` counterexample disproving
the outline's band-invariance conjecture as stated).

## Promotable lemmas

- **Integral band-decomposition identity** (Proposition 1): for any finite
  multiset $F$ of positive reals and any finite reference multiset $T$,
  $A(F\cup T) = A(T) + \int_0^\infty e(x)w(x)\,dx$ where $e(x)=N_F(x)\bmod2$
  and $w(x)=1-2(N_T(x)\bmod2)$. This is fully general (no ladder-specific
  structure used) and could be useful to any future approach needing to
  isolate one multiset's contribution against a fixed reference multiset.
  Proved in full in §1 above.
- **Cardinality-relaxed collapse** (Proposition 2/2b): for the ladder tail
  $T=\{p_2,\dots,p_{n+1}\}$, $A(T)<p_1$ for every $n\ge1$ (closed-form proof
  via `cascading-halving-family-characterization`'s $T(L)$ formula), and
  consequently the cardinality-unbounded version of claim (A) has minimum
  exactly $0$. Reusable as a clean "why the finite budget matters" fact for
  any future write-up of the general lower bound.

## Outline (proof-outliner, round 6)

This approach's own assigned technique (coarse per-band mass/count
occupancy) is now certified insufficient by its own round-5 counterexample
— it cannot close claim (A) without at least as much positional information
as `rank-pigeonhole-budget`'s finer decomposition. Not recommended for
further building this round unless paired with a genuinely finer invariant;
deprioritize in favor of the three new round-6 framings
(`lp-duality-certificate`, `integer-lattice-reduction`,
`bijective-mersenne-pairing`) and the two lemmas already promoted here
remain available for reuse by any of them.
