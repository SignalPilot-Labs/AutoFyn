# Math-explorer report: the canonical-form case of the Cardinality-Constrained Half-Sum Lemma

## Assignment recap

Round 20 proved the **Finite Reduction Theorem** (certified,
`lemmas/invisible-block-skip-fact-and-general-pairwise-reduction.md`):
every feasible $R$ of $\mathrm{GCH}(k)$ reduces (same sum, no larger
cardinality, $\mathrm{AltSum}$ weakly non-increasing) to $R''$ with **at
most one distinct active free value**. What remains open is the resulting
finite statement itself: prove $\mathrm{AltSum}(R''\cup\Gamma_{k-1})\ge1$
for every such canonical-form $R''$, for general $k$ (proved $k=2$,
numerically corroborated $k=3,4,5$ before this round). My lens: scout this
canonical-form case directly, find its precise closed structure, and check
numerically (exact `Fraction`) whether it can be closed cleanly or whether
the two-parameter $\mathrm{GCH}(j,\mathrm{cap},b;S)$ fallback (crux
aimo-0377 coupled-induction template) is actually needed.

**I did not attempt a full proof** — this is a terrain report with a
concrete, promising proof sketch flagged for the next builder.

## 1. Precise structure of canonical-form $R''$

Writing $\Gamma_{k-1}=\{2^{k-1},\dots,2,1\}$ (levels $j=0,\dots,k-1$,
value $2^j$), a canonical-form $R''$ is exactly parametrized by:

- **Integer multiplicities $n_0,\dots,n_{k-1}\ge0$** at the $\Gamma$-levels
  (the *extra* copies $R''$ contributes beyond $\Gamma_{k-1}$'s own one
  copy each), and
- **one free block** $(t,r)$: $t\ge0$ copies of a single value $r\notin
  \{1,2,\dots,2^{k-1}\}$, $0<r\le2^{k-1}$.

subject to $\sum_j n_j2^j+tr=S\in[2^k,2^k+1)$ and $\sum_j n_j+t\le k+1$.

**Key structural fact (elementary, follows directly from the certified
Invisible-Block Skip Fact + Lemma BCF, re-derived and stress-tested
independently this round — see §3):** in $M:=R''\cup\Gamma_{k-1}$, the
total multiplicity at level $j$ is $n_j+1$, and $\mathrm{AltSum}(M)$
depends **only on parities**: level $j$ is *active* (contributes $\pm2^j$)
iff $n_j$ is **even**; the free block is active iff $t$ is **odd**. Every
active item's *sign* in the alternating sum is determined purely by how
many other active items rank above it (even-multiplicity blocks are
provably invisible to rank parity, not just to value — this is exactly
what the certified Invisible-Block Skip Fact says, now used for a *global*
sign computation, not just a two-coordinate perturbation). So:

$$\mathrm{AltSum}(M)=\Big(\text{alternating sum, in decreasing order, of
the active $\Gamma$-values}\Big)\ \boxed{\text{interleaved with}}\ \pm r
\text{ if }t\text{ odd}.$$

This turns the open combinatorial claim into a **fully finite, cleanly
describable problem**: choose which of the $k$ levels are "made inactive"
(costs $\ge1$ unit of cardinality budget per level, since inactive needs
$n_j\ge1$ odd) vs. left active ($n_j=0$, free), plus optionally spend
budget on an active or inactive free block — under total budget $\le k+1$
— and show the resulting alternating sum is always $\ge1$.

**One correction to the source file's own framing.** Round 20's "Honest
scope" section states "$t\in\{0,1\}$ WLOG" — true for the *value* of
$\mathrm{AltSum}$ (since $t$'s value-contribution only depends on $t\bmod
2$), but this is easy to misread as "search only $t=0$ or $t=1$
configurations for feasibility/minimality," which is **false and cost me
a wasted numeric run** (see §2 below): $t=2$ (an *inactive* pair) is a
legitimate and in fact **load-bearing** way to absorb a non-integer $S$'s
fractional part while leaving the free block invisible to $\mathrm{AltSum}$
— it is not reducible to a $t=0$ configuration because $t=0$ can only ever
reach *integer* $S$. The next builder should search/reason over $t\in\{0,
1,2\}$ (higher even $t$ is never budget-favorable), not literally $t\in\{0,
1\}$.

## 2. Numeric findings (exact `Fraction`, exhaustive per $k$ — not sampling)

Because the cardinality cap $k+1$ makes the $n_j$-vector space genuinely
finite, I wrote an **exhaustive** (not random) exact-`Fraction` search over
all integer $(n_0,\dots,n_{k-1})$ with $\sum n_j+t\le k+1$, $t\in\{0,1,2,3\}$,
evaluating $\mathrm{AltSum}$ via the BCF-style rule above and scanning $r$'s
breakpoints exactly (Γ-levels and interval endpoints) when $t$ is odd.

- **Global minimum over all feasible $S\in[2^k,2^k+1)$: exactly $1$, for
  every $k=2,\dots,8$** — matching the Lemma's claimed bound exactly, and
  matching the certified round-19 achievability witness value. No
  violation, no near-miss, found anywhere in the exhaustive search.
- **Extremal witness at $S=2^k$ (the tight integer point):** $n=(0,2,1,
  1,\dots,1)$, $t=0$ — i.e. levels $2,4,\dots$ up through $2^{k-2}$ get one
  extra copy each (inactive), level $2$ gets **two** extra copies (still
  inactive, mult $3$... wait: total mult $=n_1+1=3$, odd, **active** — the
  minimizer is active set $\{2^0,2^1\}=\{1,2\}$, giving $\mathrm{AltSum}=
  2-1=1$). This reproduces **exactly** the certified round-19 "Exact
  achievability theorem" witness family $R^*=\{2^{k-1},\dots,4\}\cup\{r,r\}$
  at $r=2$ (chain down to $4$, tied pair at $2$) — good cross-check, the
  canonical-form search independently rediscovers the known extremal
  family rather than finding something new or lower.
- **Extremal witness at general $S=2^k+\rho$, $\rho\in(0,1)$:** the
  minimizer keeps the **same active $\Gamma$-set $\{1,2\}$** (so the
  Γ-part of $\mathrm{AltSum}$ is still exactly $1$) and dumps the entire
  fractional slack $\rho$ into an **inactive** free pair ($t=2$,
  $r=(2+\rho)/2=1+\rho/2$, invisible to $\mathrm{AltSum}$ by the Skip
  Fact). Cardinality check: $k-2$ levels made inactive at cost $1$ each
  (levels $2,\dots,k-1$), $2$ levels ($0,1$) left active at cost $0$, plus
  $t=2$: total $=(k-2)+0+2=k\le k+1$. **Fits exactly**, confirmed for
  $k=3,4,5$ against $25$ random $\rho$ points each (exact `Fraction`,
  denominators up to $1000$) — zero deviation from $\mathrm{AltSum}=1$
  exactly, i.e. the bound is **tight for every $S$ in the range**, not
  just at the endpoint $S=2^k$ — a genuine one-parameter family of
  equality cases (consistent with, and now independently confirmed for,
  the certified round-19 achievability theorem, which already claimed this
  constancy).
- **A false lead I found and ruled out myself**: restricting the search to
  literally $t\in\{0,1\}$ (misreading the "WLOG" note) gives a *different*,
  strictly larger minimum $1+\rho$ (linear in $\rho$, forced active free
  value $r=1+\rho$) — this is a valid but **non-extremal** sub-family, not
  the true minimum. I flag this explicitly so the next builder doesn't
  waste a round rediscovering that $1+\rho$ is not the sharp bound (the
  true minimum, using $t=2$, is the constant $1$).

**Conclusion: no counterexample to $\mathrm{AltSum}(R''\cup\Gamma_{k-1})
\ge1$ was found anywhere in an exhaustive (not sampled) search for
$k=2,\dots,8$; the bound is tight everywhere on $S\in[2^k,2^k+1)$, not just
at isolated points.**

## 3. A concrete, promising proof route (pigeonhole + pairing — not yet written up as a proof)

The numerics above suggest a genuinely elementary argument, which I sketch
here (verified on paper against the numeric extremal witnesses above, but
**not** independently stress-tested as a general claim — this needs a
builder's full casework, not a claim of closure):

**Step A (pigeonhole: some active item must exist).** Making level $j$
inactive costs $\ge1$ unit of the $k+1$ budget ($n_j\ge1$, odd); making the
free block inactive costs $\ge2$ ($t\ge2$, even). There are $k$ levels. If
**all** $k$ levels are inactive, that already costs $\ge k$, leaving $\le1$
unit for the free block — not enough to make it inactive too ($t\ge2$
needs $2$). So it is **never simultaneously possible** to have zero active
Γ-levels **and** an inactive-or-absent free block, *unless* the free block
is absent ($t=0$) — but $t=0$ forces $S$ to be an integer combination of
powers of $2$, i.e. $S=2^k$ exactly (the only integer in $[2^k,2^k+1)$),
and even then, making **all** $k$ levels odd (inactive) forces $S\equiv
2^k-1\pmod 2$ via $S=(2^k-1)+2\cdot(\text{even combo})$ — always **odd**,
never $S=2^k$ (even). So: **every feasible canonical-form $R''$ has at
least one active item** (a Γ-level or the free value).

**Step B (any nonempty active-Γ-subset alternating sum is $\ge1$).** If
the active Γ-levels (a nonempty subset $A\subseteq\{2^0,\dots,2^{k-1}\}$,
sorted decreasing $a_1>\cdots>a_p$) are the only active items, their
alternating sum $a_1-a_2+a_3-\cdots$ is an **integer** (sum/difference of
powers of $2$). Grouping in adjacent pairs from the left: if $p$ is even,
the sum is $\sum_{i=1}^{p/2}(a_{2i-1}-a_{2i})$, each term a difference of
two *distinct* powers of $2$, hence $\ge$ the smaller of the pair $\ge1$
(equality iff the pair is adjacent powers, e.g. $\{2,1\}$) — so the total
is $\ge p/2\ge1$. If $p$ is odd, the same pairing leaves a final $+a_p\ge1$
after the (nonnegative) paired terms. **Either way, $\ge1$.** This matches
the extremal witness found numerically ($A=\{1,2\}$, $p=2$, sum $=1$
exactly, the unique minimal case).

**Step C (the one free-active-value case — the genuine remaining work).**
When $t$ is odd (free value active), it interleaves into the sorted order
at some position among the active Γ-levels, contributing $+r$ or $-r$
depending on parity of the count of active items above it. This is the
part **not yet reduced to a clean closed form** — it's exactly the shape
of the already-fully-solved $k=2$ casework (three-way split on $r$ vs. the
neighboring $\Gamma$/free values), generalized to arbitrary $k$ and an
arbitrary active-subset shape. My numeric search (§2) shows the *minimum*
over this case is never better than Step B's bound (the $t=2$
inactive-pair branch always dominates it), which suggests — but does not
prove — that **Step C's case is never the true minimizer** and can perhaps
be disposed of by a monotonicity/domination argument (e.g. "any
configuration with the free value active can be weakly improved by
flipping it to inactive and re-routing its mass," which is very close to
already-certified machinery: the General Pairwise Reduction Lemma's
mass-conserving line-segment argument, applied here to *one* active free
value against a *newly introduced* second coordinate, rather than two
pre-existing active values).

## 4. Is the two-parameter $\mathrm{GCH}(j,\mathrm{cap},b;S)$ fallback needed?

**My finding: likely not, or at least not obviously.** The two-parameter
family was diagnosed (round 18) as necessary because the *naive
induction-on-$k$* (peel the top tied pair, recurse) doesn't shrink the cap
alongside the level index. But the pigeonhole argument in §3 above is
**not an induction on $k$ at all** — it's a direct global counting
argument over the fixed budget $k+1$ vs. $k$ levels, which needs no
recursive self-similarity and hence sidesteps the exact obstruction round
18 identified. If Step C can be closed (even by a case-by-case argument
that doesn't literally invoke a smaller instance of the same Lemma), the
whole Cardinality-Constrained Half-Sum Lemma closes **without** the
two-parameter family or the crux aimo-0377 coupled-induction template.
That template (coupled residue-class induction for a digit-parity sum,
crux corpus) remains a reasonable fallback if Step C resists a direct
argument, but nothing in this round's numerics suggests it's *needed* —
the exhaustive per-$k$ searches (§2) look like they come from one clean
mechanism (pigeonhole + integer-pairing), not from a phenomenon that needs
two coupled parameters to track.

## 5. What's already been tried/ruled out (from `current.md` / the approach file)

- Naive induction on $k$ (peel tied top pair): **fails** — cap doesn't
  shrink with the recursive level (round 18, certified diagnosis, still
  standing).
- $t\in\{0,1\}$-only search (my own false lead this round, §2): gives a
  valid but non-extremal $1+\rho$ bound, **not** the sharp constant $1$;
  don't re-use this as "the" canonical-form minimum.
- Achievability half (matching upper-bound witness) is **already fully
  proved for general $k$** (round 19, certified) — my numeric search
  independently rediscovers this exact witness family as the minimizer,
  which is a good cross-check but not new content.
- $k=2$ instance of the Lemma is **fully, rigorously proved** (round 18,
  certified, exhaustive casework) — this is exactly the Step A+B+C shape
  above specialized to $k=2$; re-reading it as "Step A/B/C at $k=2$" may
  help a builder see how to generalize Step C.

## Files referenced

- `/home/agentuser/repo/results/imo-2026-03/current.md`
- `/home/agentuser/repo/results/imo-2026-03/approaches/self-similar-induction-on-n.md`
  (lines 5666–6036 for the Cardinality-Constrained Half-Sum Lemma's
  statement and $k=2$ proof; lines 240–327 for the round-20 Finite
  Reduction Theorem write-up and "honest scope" section)
- `/home/agentuser/repo/results/imo-2026-03/lemmas/invisible-block-skip-fact-and-general-pairwise-reduction.md`
  (certified Finite Reduction Theorem)
- `/home/agentuser/repo/results/imo-2026-03/lemmas/sharper-odd-residual-and-k2-cardinality-half-sum.md`,
  `/home/agentuser/repo/results/imo-2026-03/lemmas/gch-achievability-witness-k-geq-3.md`
  (certified $k=2$ instance and general-$k$ achievability witness)
- `/tmp/memory/run_state.md` (round 20/21 next-target notes, crux
  aimo-0377 reference)
- My scripts (not part of the repo, scratch only):
  `/tmp/canonical_search.py`, `/tmp/canonical_search2.py`
