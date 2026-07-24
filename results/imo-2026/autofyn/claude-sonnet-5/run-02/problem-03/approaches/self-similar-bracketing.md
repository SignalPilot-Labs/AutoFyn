## Status
partial

## Approaches tried
- (round 3, this build) Carried out the outline's Step 2 ("re-derive both
  endpoints rigorously"). The $c=0$ endpoint was already certified
  (`untouched-top-piece-lower-bound`); this round gives a full, gap-free
  proof that the specific "rescaled-ladder" Xiang-Yu strategy at $c=n$
  achieves $\Phi=p_1$ **exactly** (Lemma B1 below), replacing the outline's
  two-line sketch with a complete alternation argument. **Then this build
  found a genuine problem with the outline's framing**: achieving $\Phi=p_1$
  with *one* strategy at $c=n$ is not the same as $\Phi=p_1$ being the
  *minimum* Xiang Yu can force at $c=n$ (which is what the lower bound
  actually needs), and Proposition B2 below shows — by running the exact
  same `cross-term-identity-threshold` decomposition that
  `greedy-halving-adversary` already used for general $c$ — that proving
  this minimality is **not an easier sub-problem**: it hits the identical
  unproved cross-term/anti-concentration obstruction (`greedy-halving-
  adversary`'s Proposition 10 "Missing inequality"), just with the roles of
  $F$ and $G$ swapped and $G$ fixed instead of adversarial. So the "$c=n$
  endpoint" is not actually closed by exhibiting the ladder-rescaling
  strategy alone, contrary to what the round-3 outline assumed. Fortunately,
  the *minimality* claim at $c=n$ turns out to already be **fully proved,
  independently, for $n=1$ and $n=2$** by other certified work (reused here,
  not re-derived): $n=1$ by the direct hand computation in
  `greedy-halving-adversary.md`'s Open-gap-3 write-up, and $n=2$ by
  `smoothing-compactness-certificate`'s composition `(2,0,0)` (2 cuts on
  $p_1$, which is exactly $c=2=n$) in `n2-lower-bound-full-closure`. For
  general $n\ge3$ the $c=n$-minimality claim is only numerically supported
  (20000 random-fraction trials per $n\in\{1,2,3,4\}$, zero violations,
  reproduced below), not proved. **Steps 3 and 4 of the outline (the
  cut-count-induction invariant and the exchange/monotonicity fallback for
  the interior $1\le c\le n-1$) were not advanced this round** — no
  candidate invariant or exchange condition was found; see Open gaps.

## Current best

A new, fully rigorous lemma (the exact $c=n$ construction, Lemma B1) plus a
precise structural diagnosis (Proposition B2) of why the bracketing plan is
harder than the outline assumed: the "easy" endpoint $c=n$ is only as easy
as its *achievability* half; its *minimality* half is exactly as hard as the
already-open general lower bound, reducing to the same cross-term
obstruction. Minimality at $c=n$ is nonetheless independently confirmed,
non-numerically, for $n=1,2$ (by reuse of existing certified work) and by
strong numerics for $n=3,4$. The interior $1\le c\le n-1$ (the approach's
actual target) has **no new progress**: neither the cut-count-induction
invariant nor the exchange-monotonicity fallback sketched in the outline was
found or formulated precisely.

## Full proof
(absent — Status is `partial`, not `solved`)

---

## Write-up

Notation as in `lemmas/`: for the $n$-ladder, $p_i=p_i(n)=2^{n+1-i}/(2^{n+1}-1)$
($i=1,\dots,n+1$), $r=r(n):=1-p_1=(2^n-1)/(2^{n+1}-1)$, and
$f(n):=p_1(n)-r(n)=1/(2^{n+1}-1)$ (`ladder-self-similarity-constant`). Recall
$\Phi(S)=(\mathrm{Total}(S)+A(S))/2$ (`integral-alternating-sum-formula`), so
$\Phi(S)\ge p_1(n) \iff A(S)\ge f(n)$ whenever $\mathrm{Total}(S)=1$.

### Lemma B1 (The $c=n$ rescaled-ladder construction attains $\Phi=p_1$ exactly).

*Let Xiang Yu spend all $n$ of his cuts fragmenting $p_1$ into
$q_i := p_1\cdot p_i(n)$ for $i=1,\dots,n+1$ (a rescaled copy of the whole
$n$-ladder, using exactly $n$ cuts since it has $n+1$ pieces), and leave the
tail $p_2,\dots,p_{n+1}$ completely untouched. Then the merge order of the
resulting $2n+1$ pieces is the strict alternation*
$$q_1 > p_2 > q_2 > p_3 > q_3 > \dots > p_{n+1} > q_{n+1},$$
*and consequently $\Phi = \sum_{i=1}^{n+1} q_i = p_1 = 2^n/(2^{n+1}-1)$
exactly.*

**Proof.** First, $\sum_{i=1}^{n+1} q_i = p_1\sum_{i=1}^{n+1}p_i(n) = p_1\cdot1
=p_1$, so this is a legal fragmentation of $p_1$ (correct total, $n$ cuts for
$n+1$ pieces). Write everything over the common denominator
$D:=(2^{n+1}-1)^2$: for $i=1,\dots,n+1$,
$$q_i = p_1\cdot p_i(n) = \frac{2^n}{2^{n+1}-1}\cdot\frac{2^{n+1-i}}{2^{n+1}-1}
= \frac{2^{2n+1-i}}{D},$$
and, over the same denominator, $p_{i+1}=p_{i+1}(n)=\dfrac{2^{n-i}}{2^{n+1}-1}
=\dfrac{2^{n-i}(2^{n+1}-1)}{D}$ for $i=1,\dots,n$ (so $p_{i+1}$ ranges over
$p_2,\dots,p_{n+1}$).

*Claim 1: $q_i > p_{i+1}$ for every $i=1,\dots,n$.* Compare numerators over
the common denominator $D$: $2^{2n+1-i}$ vs. $2^{n-i}(2^{n+1}-1)=2^{2n+1-i}
-2^{n-i}$. Since $2^{n-i}>0$, we get $2^{2n+1-i} > 2^{2n+1-i}-2^{n-i}$,
i.e. $q_i>p_{i+1}$, always (no condition on $n$ needed beyond $n-i\ge0$,
i.e. $i\le n$, which holds).

*Claim 2: $p_{i+1} > q_{i+1}$ for every $i=1,\dots,n$.* Compare numerators:
$2^{n-i}(2^{n+1}-1)$ vs. $2^{2n-i}$. Dividing both by the common positive
factor $2^{n-i}$, this is $2^{n+1}-1$ vs. $2^n$, i.e. we need
$2^{n+1}-1>2^n$, i.e. $2^n>1$, true for every $n\ge1$. So $p_{i+1}>q_{i+1}$
for every $i=1,\dots,n$, i.e. $p_2>q_2,\ p_3>q_3,\ \dots,\ p_{n+1}>q_{n+1}$.

Chaining Claims 1 and 2 by transitivity gives the full strict chain
$$q_1 > p_2 > q_2 > p_3 > q_3 > \dots > p_n > q_n > p_{n+1} > q_{n+1},$$
which has exactly $1 + 2n = 2n+1$ terms, matching the total piece count
(the $n+1$ fragments $q_i$ plus the $n$ untouched tail pieces $p_2,\dots,
p_{n+1}$). This chain **is** the sorted-descending order of the full final
multiset (transitivity of $>$ across the whole chain gives a total order,
and every element of the multiset appears in the chain exactly once). Reading
off parities: position $1$ ($q_1$) is odd, position $2$ ($p_2$) is even,
position $3$ ($q_2$) is odd, ..., in general $q_i$ sits at position $2i-1$
(odd) and $p_{i+1}$ sits at position $2i$ (even), for $i=1,\dots,n+1$
(interpreting the chain's last element $q_{n+1}$ as position $2n+1$, odd,
consistent). So **every** $q_i$ occupies an odd rank and **every** $p_{i+1}$
occupies an even rank. By the claiming-subgame reduction
(`claiming-subgame-reduction`), $\Phi = \sum_{\text{odd rank}} = \sum_{i=1}^{n+1}
q_i = p_1 = 2^n/(2^{n+1}-1)$. $\blacksquare$

*(Verified by direct computation for $n=1,2,3,4$: e.g. $n=2$, $q=(16/49,
8/49,4/49)$, tail $=(2/7,1/7)=(14/49,7/49)$; sorted order
$16/49>14/49>8/49>7/49>4/49$ matches the claimed alternation exactly, and
$\Phi=16/49+8/49+4/49=28/49=4/7=p_1(2)$.)*

This is a genuine new, fully rigorous fact: it shows the $c=n$ slice of
Xiang Yu's strategy space contains a strategy that gives Liu Bang *exactly*
the target value $p_1$ — matching, not beating, the $c=0$ endpoint's bound.
It is **not**, however, a proof that $\Phi\ge p_1$ for *every* $c=n$
strategy — see the next result, which shows that gap is real and non-trivial.

### Proposition B2 (Minimality at $c=n$ is not an easier sub-problem — it embeds the same open obstruction).

*Fix $n$, and let $G:=\{p_2,\dots,p_{n+1}\}$ (Liu Bang's ladder tail, left
completely untouched, so $\mathrm{Total}(G)=r(n)$, a **fixed** multiset — at
$c=n$, Xiang Yu spends nothing on the tail). Let $F$ range over all legal
fragmentations of $p_1$ (any multiset of positive reals summing to $p_1(n)$,
with at most $n+1$ parts, i.e. at most $n$ cuts). The lower-bound claim at
$c=n$ is:*
$$\min_{F} \Phi(F\cup G) = p_1(n),$$
*(Lemma B1 already shows the minimum is $\le p_1(n)$, attained by the
rescaled-ladder $F$; the open direction is $\ge$.) Applying the certified
`cross-term-identity-threshold` lemma (Lemma 8) at threshold $r=r(n)=
\mathrm{Total}(G)$ gives, for every legal $F$,*
$$A(F\cup G) = A(F) + A(G) - 2\int_0^{r(n)} u(x)v(x)\,dx,$$
*where $u,v$ are the odd-parity indicators of $F,G$ respectively, and $A(G)$
is a fixed known constant. Dropping the (always $\ge0$) cross term gives only
the weak bound $A(F\cup G)\ge A(F)+A(G)-2\int_0^{r(n)}uv$, and — exactly as
in `greedy-halving-adversary`'s Proposition 10 — the worst case of $A(F)$ and
$A(G)$ taken at their own trivial extremes independently (which is what
dropping the cross term amounts to) is not enough to conclude
$A(F\cup G)\ge f(n)$: nothing prevents $A(F)$ from being pushed close to its
own trivial maximum $\mathrm{Total}(F)=p_1(n)$ (e.g. by concentrating $F$'s
mass, via the degenerate case of `leftover-formula`, into one dominant
fragment paired with the rest) while simultaneously the cross term is small.
Closing the gap therefore requires the same kind of positive-correlation /
anti-concentration bound on $\int_0^{r(n)}uv\,dx$ that `greedy-halving-
adversary`'s Proposition 10 needed for the fully general $c$, now with the
roles of "adversarially-chosen small piece" and "fixed small piece" swapped
between $F'$ (Xiang Yu's choice) and $G$ (fixed, known shape). **No such bound
is proved here.** Hence the $c=n$ endpoint is genuinely only half-closed:
achievability ($\le p_1$) is now fully rigorous (Lemma B1); minimality
($\ge p_1$, i.e. the actual lower-bound direction) is exactly as hard,
structurally, as the general open problem, not a free corollary of it being
"the other extreme" from $c=0$.*

**Consequence for the outline.** The premise "both endpoints give exactly
$\Phi=p_1$, attained (not just bounded), so bracket the interior between
them" (round-3 outline) needs correcting: only the $c=0$ endpoint is a
genuinely *closed bound* (min over all $c=0$ strategies $\ge p_1$, proved in
`untouched-top-piece-lower-bound`). The $c=n$ endpoint currently has only an
*achieved value* (one strategy hits $p_1$ exactly), with the matching lower
bound (min over all $c=n$ strategies $\ge p_1$) open in general — though, as
shown next, it happens to already be closed for $n=1,2$ by other means.

### Minimality at $c=n$ for $n=1,2$ (reused, not re-derived).

- **$n=1$:** `greedy-halving-adversary.md`'s Open-gap-3 direct proof already
  shows, for the ladder $(2/3,1/3)$, that *every* single cut of the $2/3$
  piece (with the $1/3$ piece untouched — this **is** exactly the $c=1=n$
  case) gives $\Phi=2/3$ exactly, for every valid split point (shown by the
  two-range computation there: $\Phi=(2/3-a)+a=2/3$ for $a\in(0,1/3]$, and
  symmetric for $a\in[1/3,2/3)$). So $\min_F\Phi(F\cup G)=2/3=p_1(1)$,
  matching Lemma B1's value with **equality for every legal $F$**, not just
  the rescaled-ladder one (for $n=1$, "rescaled ladder" and "any single cut"
  coincide, since $F$ has only 2 parts either way).
- **$n=2$:** `smoothing-compactness-certificate`'s composition `(2,0,0)`
  (2 cuts on $p_1=4$ units of $1/7$, tail $=(2,1)$ untouched — exactly the
  $c=2=n$ case) is closed in `n2-lower-bound-full-closure`: full
  case-exhaustive analysis over how $F$'s three parts $x\ge y\ge z$
  ($x+y+z=4$) interleave with the fixed values $2,1$, giving $\Phi\ge4$ in
  every one of the (exhaustively-enumerated) 4 interleaving patterns, with
  equality exactly in the pattern matching Lemma B1's rescaled-ladder
  fragment $(16/7,8/7,4/7)$ in units of $1/7$ — consistent cross-check.
  So $\min_F\Phi(F\cup G)=4/7=p_1(2)$ is **already a certified, non-numeric
  fact**, imported here rather than re-derived.

### Numerical confirmation for $n=3,4$ (not a proof).

Re-ran (this build) 20000 random-fraction trials per $n\in\{1,2,3,4\}$:
random number of cuts $k\in\{0,\dots,n\}$ on $p_1$ at random split points
(exact `Fraction` arithmetic), tail left untouched, computing $\Phi(F\cup G)$
directly by sort-and-sum. Minimum found in every case exactly equals
$p_1(n)$, zero violations across all $80000$ trials total (matching, and
extending by two more values of $n$, the round-2 numerics already reported
in `greedy-halving-adversary`). This is consistent with, but does **not**
prove, minimality at $c=n$ for $n\ge3$.

### Interior $1\le c\le n-1$: no progress this round.

The outline's Step 3 (a "ladder-top dominance" cut-count-induction
invariant) and Step 4 (an exchange/transplant monotonicity lemma moving one
cut between $p_1$ and the tail) were both left as open tasks by the outline.
This build did not find a precise, provable form of either:

- **Step 3 attempt.** The natural invariant candidate — "after $k$ of Xiang
  Yu's cuts, the currently-largest element dominates the rest by exactly
  the residual gap $f(n-k)$, or the configuration is already an
  $(n-k)$-sub-ladder instance" — does not survive contact with Proposition
  B2: even in the *simplest* sub-case ($k=n$, tail entirely untouched, only
  $F$ varying), no such clean dominance invariant was found to hold for
  *every* legal $F$ (only for the specific rescaled-ladder $F$, by
  construction). Formulating an invariant that survives arbitrary
  interleaving of $F$'s fragments with the tail's fixed values would need to
  already resolve Proposition B2's gap, so this is not a strictly easier
  route in.
- **Step 4 attempt.** A transplant/exchange argument (move one cut's worth
  of budget from the tail to $p_1$, holding the rest of the configuration
  fixed at its own adversarial optimum) requires comparing two different
  adversarial optima (before and after the transplant) rather than a single
  fixed configuration, which is a strictly harder object to reason about
  than either fixed endpoint; no monotonicity direction (Φ increasing,
  decreasing, or non-monotone in $c$) was established even heuristically
  beyond the numeric fact (both endpoints tie exactly at $p_1$, so if
  monotone it would have to be constant $=p_1$ across all of
  $c\in\{0,\dots,n\}$ — plausible given the $n=1,2$ full closures found no
  strict violations anywhere, but not demonstrated for general $n$). This
  constant-across-$c$ possibility, if provable, would be a strong and useful
  reformulation of the target (worth flagging for the next round even though
  not established): **conjecturally, $\min_{\text{Xiang Yu}}\Phi = p_1(n)$
  is attained not on an isolated configuration but on a whole
  positive-dimensional family, for every split $c$, tied exactly at $p_1$,
  with no $c$ ever strictly better for Xiang Yu than any other** — consistent
  with every case checked ($n=1$ exactly, $n=2$ exactly via the (2,0,0) and
  other compositions, $n=3,4$ numerically) but unproved.

## Open gaps

1. **(Main gap, unchanged in kind, sharpened in location.)** The general-$n$
   lower bound for $1\le c\le n-1$ — the approach's actual target — has zero
   new progress this round: no invariant (Step 3) or exchange lemma (Step 4)
   was found or even precisely stated.
2. **(New this round.)** Even the $c=n$ endpoint, which the outline treated
   as already closed, is only half-closed in general: Lemma B1
   (achievability, $\le p_1$) is now fully rigorous for all $n$; minimality
   ($\ge p_1$) is proved only for $n=1,2$ (by reuse of other approaches'
   work) and open for $n\ge3$, and Proposition B2 shows this is not a
   shortcut — it requires resolving essentially the same cross-term
   obstruction identified in `greedy-halving-adversary`'s Proposition 10.
3. The general upper bound (arbitrary Liu Bang marking) remains completely
   untouched by this approach, as by every approach except
   `smoothing-compactness-certificate`'s closed $n=2$ case.
4. A concrete, checkable-but-unproved reformulation worth carrying into the
   next round (see "Step 4 attempt" above): is $\min_{\text{Xiang Yu with
   budget split }c}\Phi$ *constant*, equal to $p_1(n)$, across every
   $c\in\{0,\dots,n\}$, or does it merely tie at the two endpoints while
   possibly dipping in between (ruled out only by $n\le2$ closures and
   $n\le4$ numerics so far)? Determining which of these is true — and why —
   would settle whether "bracketing" (this approach's core idea) can work at
   all, or whether it was mis-diagnosing the problem (dips could exist for
   larger $n$ that neither endpoint sees).

## Files consulted

`results/imo-2026-03/current.md`; `results/imo-2026-03/lemmas/` (all files,
especially `claiming-subgame-reduction`, `integral-alternating-sum-formula`,
`untouched-top-piece-lower-bound`, `dominant-element-removal-identity`,
`cross-term-identity-threshold`, `ladder-self-similarity-constant`,
`budget-monotonicity`, `must-use-all-n-points`, `alternating-sum-scaling`,
`n2-lower-bound-full-closure`); `results/imo-2026-03/approaches/
greedy-halving-adversary.md` (Lemmas 1–9, Key Lemma, Proposition 10, and the
$n=1$ direct proof in Open gap 3, all reused); `results/imo-2026-03/
approaches/smoothing-compactness-certificate.md` (composition `(2,0,0)`,
reused for $n=2$ minimality at $c=n$). Numerical checks this round: a
`Fraction`-exact Python script, 20000 random trials per $n\in\{1,2,3,4\}$,
confirmed (not proved) $c=n$ minimality; script and results not committed
(reproducible from the description above), consistent with the
already-reported round-2 numerics in `greedy-halving-adversary`.
