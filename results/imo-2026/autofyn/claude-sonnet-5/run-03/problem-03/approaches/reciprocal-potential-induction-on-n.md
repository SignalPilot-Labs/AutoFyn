## Status
unsolved

## Approaches tried
- **Round 16 (this round, new slug, first build).** Per the mandatory
  cheap-kill instructions, tested the proposed pointwise reciprocal-recursion
  inequality
  $$\frac1{V(p)}\ \ge\ \frac1{V(p')}+2^{-n}\qquad(\star)$$
  (the pointwise strengthening, along a reduction map $p\mapsto p'$ taking an
  $n$-cut instance to an $(n-1)$-cut instance, that would let downward
  induction on $n$ prove $V(p)\le c(n)$ from the exact closed-form identity
  $1/c(n)=1/c(n-1)+2^{-n}$) against **two different natural reduction maps**,
  in exact `Fraction` arithmetic, using the region vertex $e_0(n)$ (whose
  value $V(e_0(n))=\tfrac12$ exactly, for every $n\ge3$, is already certified,
  `lemmas/twin-anchor-floor-theorem.md`) as the test point. **Both maps fail
  $(\star)$ decisively and exactly**, and a general structural reason for the
  failure was found and proved (see below). **Result: $(\star)$, in this
  literal pointwise form, is refuted as a route to the Existence Theorem — a
  genuine, proved dead end, reported honestly rather than forced.**

## Current best

### 0. Setup: what is being tested and why it is well-posed

Per the certified Reduction Lemma (`lemmas/reduction-to-multiset-minimax.md`),
for a fixed number of available response cuts $n$ and a legal LB partition
$p=(p_1,\dots,p_k)$, $k\le n+1$, $\sum p_i=1$, define
$$V_n(p):=\min_{\substack{\text{legal XY response}\\\text{using}\le n\text{ cuts}}}\mathrm{OddSum}(\text{resulting multiset}).$$
The target Existence Theorem is $V_n(p)\le c(n)$ for every legal $p$ in the
balanced region, where $c(n)=2^n/(2^{n+1}-1)$ satisfies, by direct algebra on
the closed form,
$$\frac1{c(n)}=\frac{2^{n+1}-1}{2^n}=2-2^{-n}=\Bigl(2-2^{-(n-1)}\Bigr)+2^{-(n-1)}-2^{-n}
=\frac1{c(n-1)}+2^{-n}.$$
(Check: $c(0)=1,\ c(1)=2/3$: $1/c(1)=3/2=1/c(0)+1/2=1+1/2$. ✓)

The proposed proof strategy needs a **pointwise** inequality $(\star)$ along
some canonically defined map $p\mapsto p'$ (an $(n-1)$-cut instance obtained
from the $n$-cut instance $p$) so that downward induction on $n$, seeded at
a proved base case, gives $V_n(p)\le c(n)$ for all $p,n$. This is exactly
what the round's dispatch asked to cheap-kill before any proof investment.

### 1. Universal Floor Lemma (elementary, proved in full — needed below)

**Lemma (Universal Floor).** For every finite multiset $M$ of nonnegative
reals, $\mathrm{OddSum}(M)\ge\mathrm{sum}(M)/2$; consequently $V_n(p)\ge
\tfrac12$ for every legal $p,n$.

*Proof.* Sort $M$ in descending order $v_1\ge v_2\ge\cdots\ge v_m$.
$\mathrm{OddSum}(M)=v_1+v_3+v_5+\cdots$, $\mathrm{EvenSum}(M)=v_2+v_4+\cdots$.
Pairing $v_{2i-1}$ with $v_{2i}$ for each $i$ with $2i\le m$, we have
$v_{2i-1}\ge v_{2i}\ge0$ termwise (descending order), so
$\mathrm{OddSum}(M)\ge\mathrm{EvenSum}(M)$ summing these pairs (if $m$ is odd
the unpaired last term $v_m\ge0$ is counted only in $\mathrm{OddSum}$, only
helping the inequality). Since $\mathrm{OddSum}(M)+\mathrm{EvenSum}(M)=
\mathrm{sum}(M)$, we get $2\,\mathrm{OddSum}(M)\ge\mathrm{sum}(M)$, i.e.
$\mathrm{OddSum}(M)\ge\mathrm{sum}(M)/2$. Since every legal response's
resulting multiset $M$ has $\mathrm{sum}(M)=1$ (cuts don't change total
mass), $\mathrm{OddSum}(M)\ge\tfrac12$ for every legal response, hence
$V_n(p)=\min(\cdots)\ge\tfrac12$. $\blacksquare$

### 2. A new, fully general theorem: the Generalized Twin-Anchor Floor Theorem

The certified Twin-Anchor Floor Theorem (`lemmas/twin-anchor-floor-theorem.md`)
proves $V(e_0(n))=\tfrac12$ at one specific point per $n$ (the region vertex
$e_0$, whose common difference is pinned to the specific value
$\delta=1/(2^{N}-1)$, $N=n+1$). Its proof, on inspection, never actually uses
that specific value of $\delta$ — it only uses that $p$ is a strictly
decreasing arithmetic progression with all terms positive. We record this as
a genuinely more general theorem (**new this round, proved below**), because
it is exactly what makes the reciprocal-recursion cheap-kill decisive rather
than a single isolated coincidence.

**Theorem (Generalized Twin-Anchor Floor Theorem).** Fix an integer $N\ge4$
and any real $\delta$ with $0<\delta<\dfrac2{N(N-1)}$. Let
$$a:=\frac{1-\delta N(N-1)/2}{N}>0,\qquad p_i:=a+(N-i)\delta\ \ (i=1,\dots,N),$$
so $p_1>p_2>\cdots>p_N=a>0$ and $\sum_{i=1}^N p_i=1$ (direct check: $\sum_i
(a+(N-i)\delta)=Na+\delta\binom N2=Na+\delta N(N-1)/2=N\cdot\frac{1-\delta
N(N-1)/2}N+\delta N(N-1)/2=1$). Then $p=(p_1,\dots,p_N)$ is a legal LB
partition with $N-1\le N-1$ pieces beyond the first (it needs $N-1$ cuts to
produce, matching an $(N-1)$-cut game budget), and there is a legal XY
response using exactly $N-2\le N-1$ cuts with $\mathrm{OddSum}=\tfrac12$
exactly. Combined with the Universal Floor Lemma, $V_{N-1}(p)=\tfrac12$
exactly.

*Proof (construction and verification).* Exactly the Twin-Anchor
construction, applied verbatim to this $p$ (the construction never uses the
numeric value of $\delta$, only the AP relations below):
- Piece $1$ ($=a+(N-1)\delta$) splits into fragments $p_{N-1}=a+\delta$ and
  $p_1-p_{N-1}=(N-2)\delta$.
- Piece $2$ ($=a+(N-2)\delta$) splits into fragments $p_N=a$ and
  $p_2-p_N=(N-2)\delta$.
- Each piece $j=3,\dots,N-2$ (empty range if $N\le5$) bisects into two exact
  halves $p_j/2,p_j/2$.
- Pieces $N-1,N$ are left untouched.

This uses $2+(N-4)=N-2$ cuts (two piece-splits plus one cut per bisected
middle piece; $0$ middle cuts if $N\le5$), legal since $N-2\le N-1$.

**Positivity.** $p_{N-1}=a+\delta>0$ (since $a>0,\delta>0$); $p_N=a>0$ by
hypothesis; $(N-2)\delta>0$ since $N\ge4\Rightarrow N-2\ge2>0$ and $\delta>0$;
each middle piece $p_j>0$ (as $p_j\ge p_{N-2}=a+2\delta>0$ for $j\le N-2$), so
each half is positive. Every fragment is strictly positive.

**Multiset structure.** The resulting multiset of $2N-2$ fragments is
$$\{p_{N-1},\,p_{N-1}\}\ \cup\ \{p_N,\,p_N\}\ \cup\ \{(N-2)\delta,\,(N-2)\delta\}
\ \cup\ \bigcup_{j=3}^{N-2}\{p_j/2,\,p_j/2\},$$
where the first pair comes from (fragment $p_{N-1}$ of piece $1$) together
with (untouched piece $N-1$, value $p_{N-1}$); the second pair from
(fragment $p_N$ of piece $2$) together with (untouched piece $N$, value
$p_N$); the third pair from piece $1$'s and piece $2$'s *second* fragments,
which are identically equal, $(N-2)\delta=(N-2)\delta$ — this uses only the
AP relations $p_1-p_{N-1}=(N-1-\,1)\delta\cdot\!\!\cdot=(N-2)\delta$ and
$p_2-p_N=(N-2-0)\delta=(N-2)\delta$, computed directly from $p_i=a+(N-i)\delta$
for any $\delta$, no side condition; and each remaining group is a genuine
equal pair from bisection. **Every value occurs with even multiplicity.**

**AltSum vanishes.** By the (already certified, used unchanged) Even-Block-
Neutrality mechanism: an even-sized block of a single repeated value occupies
a set of consecutive ranks in the descending sort of the whole multiset (any
two elements of equal value can be placed adjacent in the sort without loss
of generality, and ties may be broken arbitrarily since we only need
*some* legal response to exist), so an even block contributes $0$ to
$\mathrm{AltSum}$ regardless of how it interleaves with the other groups
(inserting or removing an even-sized equal-value block shifts every later
element's rank by an even number, preserving the odd/even parity of every
other element's rank, and the block's own internal contribution telescopes
to $0$ since it consists of pairs of equal adjacent-rank values with opposite
sign in $\mathrm{AltSum}$). Applying this to each of the $N-1$ pairs above,
$\mathrm{AltSum}=0$ for the whole multiset. Hence
$$\mathrm{OddSum}=\tfrac12\bigl(\mathrm{sum}+\mathrm{AltSum}\bigr)=\tfrac12(1+0)=\tfrac12.$$
$\blacksquare$

**Independent numerical confirmation (exact `Fraction`, this round).**
Re-implemented the construction literally (not the closed-form shortcut) and
checked $N=4,\dots,11$, $20$ random rational $\delta\in\bigl(0,\tfrac2{N(N-1)}\bigr)$
per $N$ ($160$ instances total): every fragment strictly positive,
$\mathrm{OddSum}=\tfrac12$ exactly (as an identical `Fraction`, not a
float), zero deviations.

This theorem strictly generalizes the certified Twin-Anchor Floor Theorem
(which is the single case $\delta=1/(2^{N}-1)$): **an entire one-parameter
continuum of AP-shaped partitions per $N$, not just the specific region
vertex $e_0$, sits exactly at the universal floor $V=\tfrac12$.**

### 3. Cheap-kill: two reduction maps, both exact, both fail $(\star)$

Test point: $p=e_0(n)$, the certified region vertex, for which
$V_n(p)=\tfrac12$ exactly for every $n\ge3$ (`lemmas/twin-anchor-floor-theorem.md`).
Exact coordinates (own computation, matches the cited theorem):
$$n=3:\ p=\Bigl(\tfrac7{20},\tfrac{17}{60},\tfrac{13}{60},\tfrac3{20}\Bigr);
\qquad n=4:\ p=\Bigl(\tfrac{41}{155},\tfrac{36}{155},\tfrac15,\tfrac{26}{155},\tfrac{21}{155}\Bigr).$$

**Reduction map 1: "descend to the same canonical vertex," $e_0(n)\mapsto
e_0(n-1)$.** This is the most literal instantiation of "spend one unit of
the adversary's remaining budget and land on the analogous $(n-1)$-instance"
— both endpoints are the *same* named canonical point at consecutive $n$.
By the certified theorem, $V_{n-1}(e_0(n-1))=\tfrac12$ too (for $n-1\ge3$,
i.e. $n\ge4$). Then
$$\frac1{V_n(p)}=2,\qquad \frac1{V_{n-1}(p')}+2^{-n}=2+2^{-n}>2,$$
so $(\star)$ **fails**, exactly, by exactly $2^{-n}$, for **every** $n\ge4$
(computed exactly for $n=4,5,6,7$: LHS $=2$, RHS $=33/16,\,65/32,\,129/64,\,257/128$
respectively, all $>2$).

**Reduction map 2: "drop the smallest cut, renormalize."** Take $p=e_0(n)$
($N=n+1$ pieces), delete the smallest piece $p_N=a$, and rescale the
remaining $N-1=n$ pieces to sum to $1$: $p'_i:=p_i/(1-a)$ for $i=1,\dots,N-1$.
This is a different, independently natural map (literally the first example
listed in the dispatch). Direct computation shows $p'$ is again a strictly
decreasing arithmetic progression (with a *different* common difference
$\delta'=\delta/(1-a)\ne\delta_{e_0(n-1)}=1/(2^n-1)$ in general — checked
exactly for $n=4,\dots,7$, $p'\ne e_0(n-1)$ termwise in every case), with
$N-1=n$ terms — exactly the cardinality needed for an $(n-1)$-cut instance.
By the Generalized Twin-Anchor Floor Theorem of Section 2 (applicable since
$p'$ is a positive decreasing AP with $n\ge4$ terms and the sum-to-$1$/
positivity hypotheses hold, verified exactly), $V_{n-1}(p')=\tfrac12$ exactly
— **independently re-derived from scratch** (not by assuming $p'=e_0(n-1)$;
own construction and `Fraction` computation), for $n=4,5,6,7$: every
fragment positive, $\mathrm{OddSum}=1/2$ exactly, zero deviation. Then again
$$\frac1{V_n(p)}=2,\qquad \frac1{V_{n-1}(p')}+2^{-n}=2+2^{-n}>2,$$
so $(\star)$ **fails**, by exactly the same margin, for this map too.

### 4. Structural diagnosis (not just two failed data points)

Both maps fail for the *same underlying reason*, which the Generalized
Twin-Anchor Floor Theorem exposes: the set of partitions sitting exactly at
the universal floor $V=\tfrac12$ is **not** a sparse/isolated set — it
contains an entire continuum (a full open interval of $\delta$) of
AP-shaped partitions at every cardinality $N\ge4$. Since $e_0(n)$ is itself
already at this floor, **any** reduction map $p\mapsto p'$ whose image
$p'$ also lands anywhere in this (large, structurally generic) family — as
both of the two independently-natural maps tested here do — forces
$1/V_{n-1}(p')=2$ exactly, and $(\star)$ becomes the false statement
$2\ge2+2^{-n}$. A map could only avoid this if it were specifically
engineered to jump *out* of the floor-attaining family whenever the source
point is already in it — but the two most natural literal readings of "spend
one unit of the adversary's structure" both land back inside it. This is
not a proof that *no* reduction map can ever work (a sufficiently exotic,
non-AP-preserving, non-canonical map is not ruled out in full generality),
but it is a genuine, exact, structural obstruction to the natural candidates,
consistent with the dispatch's own criterion for an honest dead-end
diagnosis: the inequality fails on the first candidate maps tried, for a
provable structural reason, not from an unlucky choice of test point.

### 5. What was not attempted, honestly scoped

Per the dispatch's cheap-kill-first discipline, no attempt was made to
patch $(\star)$ (e.g. by restricting to a sub-family of reduction maps
provably avoiding the floor-attaining set, or by weakening $(\star)$ to a
non-pointwise / averaged form) — the round's job was to test the literal
proposal honestly before any proof investment, and it fails cleanly. A
future round could investigate whether some *non-canonical*, $p$-dependent
reduction map (chosen adversarially against the floor-attaining family)
salvages a version of this framing, but no such map was found or attempted
here, and Section 4's diagnosis suggests it would need to actively detect
and route around an entire continuum of degenerate points at every $n$ —
a nontrivial extra requirement not part of the original proposal.

## Full proof
(none — Status is `unsolved`; the approach's core mechanism, the pointwise
reciprocal-recursion inequality $(\star)$, is refuted in Section 3 above,
with the general structural reason in Section 4. No route to the Existence
Theorem was found this round via this framing.)

## Promotable lemmas

- **Generalized Twin-Anchor Floor Theorem** (Section 2 above): for every
  integer $N\ge4$ and every real $\delta\in\bigl(0,\tfrac2{N(N-1)}\bigr)$,
  the arithmetic-progression partition $p_i=a+(N-i)\delta$
  ($a:=(1-\delta N(N-1)/2)/N$) satisfies $V_{N-1}(p)=\tfrac12$ exactly, via
  an explicit $(N-2)$-cut construction with all fragments positive. This
  strictly generalizes the certified `lemmas/twin-anchor-floor-theorem.md`
  (which is the single case $\delta=1/(2^N-1)$) to an entire one-parameter
  family per $N$. Proved in full above (elementary algebra + the already-
  certified Even-Block-Neutrality mechanism, cited unchanged); independently
  re-verified in exact `Fraction` arithmetic, $N=4,\dots,11$, $20$ random
  rational $\delta$ per $N$ (160 instances), zero deviations. Reusable by
  any future approach needing $V(p)=1/2$ at any AP-shaped partition, not
  just the specific region vertex $e_0$ — in particular it immediately
  supplies a much larger stock of exact-value test points for future
  cheap-kills of proposed general inequalities on $V(p)$, as demonstrated in
  Section 3 above.
