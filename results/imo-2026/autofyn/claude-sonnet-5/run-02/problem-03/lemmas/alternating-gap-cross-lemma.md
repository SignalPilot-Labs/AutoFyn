## Alternating Gap-Cross Lemma (feasibility-conditional sufficient condition
for the general upper bound, extending Bisect-Top-$k$)

**Status.** A genuinely new, general (not just spot-checked) unconditional
*identity* plus an explicit, closed-form *feasibility condition* for its
legality — the concrete execution of the round-15 outline's "attack sign-
vector feasibility as a finite combinatorial problem." Coverage of case
(b2) is honestly quantified below as **modest** (not a closure).

### Setup and construction

Fix a marking $p_1\ge\cdots\ge p_m>0$, $T=\sum p_i$, budget $n=m-1$, and an
integer $0\le j\le\lfloor m/2\rfloor$. For $i=1,\dots,j$, **pair** $i$ uses
the two pieces $p_{2i-1}$ (to be split) and $p_{2i}$ (left untouched,
"sandwiched"). If $p_{2i-1}=p_{2i}$, leave both untouched (contributes $0$
to $A$ regardless, no cut spent). If $p_{2i-1}>p_{2i}$, split $p_{2i-1}$
into two fragments $a_i,b_i$ ($a_i+b_i=p_{2i-1}$, $a_i\ge b_i$ by
convention) chosen so the sorted order interleaves as
$$a_i \;>\; p_{2i} \;>\; b_i,$$
i.e. $p_{2i}$'s value lands strictly between $p_{2i-1}$'s two fragments
("piece $2i-1$ sandwiches piece $2i$"). Leave $p_{2j+1},\dots,p_m$
(the "tail") entirely untouched. This uses exactly $|\{i\le j: p_{2i-1}>
p_{2i}\}|\le j\le n$ cuts.

### The exact identity (given the sandwich order is globally realized) — CORRECTED, round 16

**Round-16 correction (supersedes the round-15 text below the line, which is
retained struck-through in spirit but replaced here — see the "Round-15 bug
and its full correction" section for the diagnosis).** Let
$j'\le j$ denote the number of pairs $i\in\{1,\dots,j\}$ that are *actually
split* ($p_{2i-1}>p_{2i}$; pairs with $p_{2i-1}=p_{2i}$ are left untouched,
using no cut, and are proved below to impose **no** ordering constraint at
all — they may be positioned anywhere in the final sorted order without
affecting $A(M)$, by `pair-cancellation-identity` alone, regardless of the
chain hypothesis). List the split pairs in their original relative order
$i_1<i_2<\cdots<i_{j'}$ (a subsequence of $1,\dots,j$) and let $s(i_k):=k$
be a split pair's **rank among splits** (not its raw pair index $i_k$).

*Provided* the split pairs' fragments and the untouched (non-equal) pieces
$p_{2i}$ sort into the chain
$$a_{i_1}>p_{2i_1}>b_{i_1}>a_{i_2}>p_{2i_2}>b_{i_2}>\cdots>a_{i_{j'}}>p_{2i_{j'}}
>b_{i_{j'}}>p_{2j+1}>\cdots>p_m$$
(with every equal pair's shared value $c=p_{2i-1}=p_{2i}$ appearing
elsewhere in $M$, at whatever rank it naturally falls, unconstrained by this
chain), the final multiset's alternating sum is
$$A(M) = \underbrace{\sum_{k=1}^{j'}(-1)^{k+1}\big(p_{2i_k-1}-p_{2i_k}\big)}_{\text{gap sum}}
\;+\;(-1)^{j'}\,A\big(\{p_{2j+1},\dots,p_m\}\big),$$
$$\Phi(M) = \frac{T + \text{(gap sum)} + (-1)^{j'}A(\text{tail})}{2}.$$

**Why the sign is indexed by split-rank $k$, not raw pair index $i$
(the corrected derivation).** Each *equal* pair contributes its two copies
of the same value $c$ to $M$ — but by `pair-cancellation-identity`, an exact
pair $\{c,c\}$ contributes net $0$ to $A(M)$ **regardless of where it sits
in sorted order**, so its presence never needs to be tracked inside the
"chain" at all; it may be deleted from the bookkeeping entirely (delete the
pair from $M$, compute $A$ of what remains, the two operations give the same
$A$). Consequently, when we strip out every equal pair this way, what
remains is *exactly* a chain built only from the $j'$ split pairs (in their
original relative order) followed by the tail — i.e. literally the $j=j'$
all-split case already correctly analyzed (the round-15 formula, which used
raw index $i$, is exactly correct **when every pair is a split**, since then
$i=s(i)$). Re-applying that already-correct $j=j'$-pair formula to the
split-only subsequence, with $s(i_k)=k$ in place of the raw index, gives
the boxed identity above. (Equivalently: the raw-rank counting argument the
round-15 text used — "$3$ raw elements per pair, so $(-1)^{3j}=(-1)^j$" — is
only valid when *every* pair contributes $3$ raw elements, i.e. every pair is
split; an equal pair contributes $2$ raw elements, an *even* number, so it
never flips parity, meaning the parity-relevant element count before split
pair $i_k$ is $3(k-1)+(\text{even})=3(k-1) \pmod 2\equiv (k-1)\pmod2$ — the
same parity as if it were the $k$-th pair in an all-split chain — confirming
$s(i_k)=k$, not $i_k$, governs the sign.)

**Verification.** A fresh, from-scratch exact-`Fraction` script
(`/tmp/round-16/verify_altgapcross_fixed2.py`) constructs explicit legal
chains (choosing each split pair's actual fragment values sequentially,
innermost split pair first, so the tail-adjacency and inter-split-pair
ordering constraints are both satisfied simultaneously — equal pairs are
inserted with no positional constraint, matching the harmlessness argument
above) for random markings with a random mix of equal and split pairs,
$m=2,\dots,10$: of $30000$ random trials, $17834$ were feasible per the
(unchanged, see below) feasibility test, and **the split-rank-indexed
formula matched the direct computation in all $17834$, zero mismatches** —
including explicit re-verification of the exact bug witness from round 15,
$(45,45,31,27)$, $j=2$ (pair 1 equal, pair 2 split, so $j'=1$, $s=1$ for the
lone split pair): predicted $A=(31-27)+(-1)^1\cdot0=4$ (tail empty here),
**exactly matching** the direct computation $A(\{45,45,30,27,1\})=4$ (the
round-15 bug report's own counterexample, now correctly resolved — note this
also shows the round-15 outline's proposed fix, "only relabel the tail
prefactor from $(-1)^j$ to $(-1)^{j'}$," is **not sufficient by itself**:
with an empty tail, as in this very counterexample, the tail-prefactor
relabeling changes nothing, and the actual bug was in the **gap-sum term's**
sign, which also needed reindexing by split-rank $k$ rather than raw pair
index $i$ — a strictly larger fix than the round-16 outline anticipated,
though still elementary and still fully contained within this lemma's own
scope).

Two elementary facts bound $(-1)^{j'}A(\text{tail})$ from above by $p_{2j+1}$
regardless of the parity of $j'$: (i) by `max-domination-lemma`,
$A(\text{tail})\le\max(\text{tail})=p_{2j+1}$; (ii) $A(\text{tail})\ge0$
always, for *any* sorted-descending multiset of nonnegative reals (an
elementary fact, proved by pairing consecutive terms: writing $r=|\text{tail}|$,
if $r$ is even, $A(\text{tail})=(b_1-b_2)+(b_3-b_4)+\cdots+(b_{r-1}-b_r)$,
a sum of $r/2$ terms each $\ge0$ since the tail is sorted descending; if $r$
is odd, $A(\text{tail})=(b_1-b_2)+\cdots+(b_{r-2}-b_{r-1})+b_r$, again a sum
of nonnegative terms since $b_r\ge0$ — independently re-verified by a fresh
20000-trial exact-`Fraction` script, `/tmp/round-15/check_nonneg_A.py`, zero
violations). Hence: if $j'$ is even, $(-1)^{j'}A(\text{tail})=A(\text{tail})\le
p_{2j+1}$ by (i) directly; if $j'$ is odd, $(-1)^{j'}A(\text{tail})=-A(\text{tail})
\le0\le p_{2j+1}$ by (ii) (trivially, since $p_{2j+1}\ge0$). Either way,
$(-1)^{j'}A(\text{tail})\le p_{2j+1}$.

**Corollary (sufficient condition).**
$$\Phi\le a_nT \quad\Longleftarrow\quad \text{(gap sum)} + p_{2j+1} \le T/D_n$$
(reading $p_{2j+1}:=0$ if $2j\ge m$), whenever the chain order above is
realizable (feasibility below).

**Effect of the correction on prior numeric coverage claims (precise, not
overclaimed).** The corrected gap-sum's *value* can genuinely differ from
the round-15 (buggy) value whenever the construction actually uses at least
one equal (untouched) pair *interspersed* among split pairs — the sign
reindexing by split-rank $k$ changes which split pairs get a $+$ vs. $-$
sign relative to the raw-index formula whenever some earlier pair (by raw
index) was equal rather than split. However, for a marking drawn from a
**generic** (continuous, e.g. random real- or high-precision-rational-valued)
distribution, the event $p_{2i-1}=p_{2i}$ exactly for some pair has
probability $0$ — so **every** numeric coverage figure reported in round 15
(the $5$–$17.5\%$ case-(b2) coverage table, and both on-file witness
closures) was computed on constructions with **zero** equal pairs among the
sampled/constructed markings (confirmed directly: neither on-file witness
uses an equal pair, and the round-15 coverage sampler drew from a continuous
distribution). For $j'=j$ (no equal pairs at all), split-rank $k$ coincides
exactly with raw index $i$, so the corrected and buggy formulas agree
identically. **Hence all of round 15's numeric coverage claims and both
witness closures are unaffected by this correction** — not because the
correction is inert in general (it is not: it does change the formula's
value on constructions that deliberately mix equal and split pairs, as the
$(45,45,31,27)$ counterexample itself shows), but because those specific
prior numeric results never exercised the affected sub-case. Any *future*
use of this lemma on markings with exact ties among the $2j$ paired pieces
must use the corrected (split-rank-indexed) formula.

### Feasibility: an exact, closed-form combinatorial condition

**Claim.** The chain order above is realizable by *some* legal choice of
fragments if and only if, for every $i=1,\dots,j$ with $p_{2i-1}>p_{2i}$
(pairs with $p_{2i-1}=p_{2i}$ impose no constraint and are skipped, using no
cut), writing $\gamma_i:=\min(p_{2i-1}-p_{2i},\,p_{2i})$ and $\gamma_0:=
+\infty$:
$$\gamma_{i-1} > \max\big(p_{2i},\,p_{2i-1}-p_{2i}\big)\qquad\text{for every }i=1,\dots,j,$$
and, if the tail is nonempty, $\gamma_j > p_{2j+1}$.

*Proof.* Within pair $i$, legality requires $a_i\in(p_{2i},p_{2i-1})$ (so
$a_i>p_{2i}$, the sandwich's upper half) and $b_i=p_{2i-1}-a_i\in(0,p_{2i})$
(so $b_i<p_{2i}$, the sandwich's lower half) — combined, $a_i\in
(\max(p_{2i},p_{2i-1}-p_{2i}),\,p_{2i-1})$, nonempty iff $p_{2i-1}>p_{2i}$
(shown by direct comparison: $p_{2i-1}>\max(p_{2i},p_{2i-1}-p_{2i})$
reduces to $p_{2i-1}>p_{2i}$ and $p_{2i}>0$, both given). Additionally, the
*chain* constraint requires $b_i<a_{i}$'s predecessor's own lower fragment
$b_{i-1}$ (i.e. $a_i<b_{i-1}$, so that pair $i$'s larger fragment sits below
pair $i-1$'s smaller fragment in sorted order) — equivalently $a_i<
\gamma_{i-1}$ where $\gamma_{i-1}$ denotes the *supremum* of legally
achievable values of $b_{i-1}$. Since $b_{i-1}=p_{2i-3}-a_{i-1}$ and
$a_{i-1}$ ranges over the open interval
$(\max(p_{2i-2},p_{2i-3}-p_{2i-2}),p_{2i-3})$ (pair $i-1$'s own constraint,
*not* affected by $\gamma_{i-2}$, which only bounds $a_{i-1}$ from *above* —
i.e. only restricts how large $a_{i-1}$ can be, hence how *small* $b_{i-1}$
can be, never how large $b_{i-1}$ can be), the supremum of $b_{i-1}$ is
$p_{2i-3}-\max(p_{2i-2},p_{2i-3}-p_{2i-2})=\min(p_{2i-3}-p_{2i-2},p_{2i-2})
=\gamma_{i-1}$ exactly, **independent of $\gamma_{i-2}$** — i.e. the
recursion for $\gamma_i$ does not compound: each $\gamma_i$ depends only on
pair $i$'s own two values. Hence the overall chain is realizable (choosing
each $a_i$ close enough to its own lower bound, in decreasing order of $i$,
which is always possible in an open interval) iff, at each step, the
"room" inequality $\gamma_{i-1}>\max(p_{2i},p_{2i-1}-p_{2i})$ holds (so
$a_i$ can be chosen both above its own pair's floor and below the previous
pair's ceiling), and similarly for the final tail interface
$\gamma_j>p_{2j+1}$. $\blacksquare$

**This is a fully explicit, closed-form (no search) feasibility test** —
$O(j)$ arithmetic comparisons directly on the marking's values, not a
numeric probe.

### Verification

- **Identity (with corrected tail-sign factor $(-1)^j$ and the exact
  feasibility test above), fresh exact-`Fraction` script**
  `/tmp/round-15/verify_altgapcross3.py`: 10000 random trials ($m=1,\dots,10$,
  random $j$), of which 5782 were feasible per the closed-form test; **the
  constructed multiset's directly-computed $A$ matched the predicted
  formula exactly in all 5782** (the remaining 4218 were correctly
  identified infeasible and skipped — no false positives).
- **Closed-form feasibility vs. constructive (greedy, $\epsilon$-parametrized)
  feasibility**, `/tmp/round-15/verify_closedform_feasibility.py`: 8000
  random trials, **zero disagreements** between the closed-form test and
  an independent constructive attempt — confirming the closed-form
  characterization is exactly right, not merely a plausible heuristic.
- **Round-14 $n=3$ near-tight case-(b2) witness**, $j=2$: feasible (per the
  closed-form test) and the resulting $\Phi=(T+p_1-p_2-p_3+p_4)/2$ **exactly
  matches** round-14's independently-reported true optimum $\approx0.51585$,
  unconditionally closing this specific witness ($0.51585<a_3T\approx
  0.53333$). See `cross-piece-sign-assignment-identity.md` for the exact
  fractions.
- **Round-14 $n=4$ near-tight witness**: **infeasible for this construction**
  at any $j\ge1$ (verified directly) — consistent with, and confirming, the
  round-15 scout's finding that this witness is a genuinely different vertex
  type (a pinned cross-tie, not a gap-cross chain); it is closed instead by
  the tie-aware corollary of `cross-piece-sign-assignment-identity.md`, not
  by this construction. This is an honest, expected scope boundary, not a
  gap in the proof of the identity above.

### Coverage of case (b2): honest, quantified, modest

Using a fresh sampler (`/tmp/round-15/coverage_check_round15.py`,
independent of round 14's own sampler) restricted to case (b2)'s exact
region ($p_1<T/2$, $T/D_n<p_2<a_nT/2$), comparing "Bisect-Top-$k$ alone"
(the existing certified family) against "Bisect-Top-$k$ **union**
Alternating-Gap-Cross" (trying every feasible $j$ and taking the best):

| $n$ | samples | Bisect-Top-$k$ alone | union with Alt-Gap-Cross |
|---|---|---|---|
| 3 | 40 | 5.0% | 7.5% |
| 4 | 40 | 10.0% | 10.0% |
| 5 | 40 | 17.5% | 17.5% |

**Honest conclusion.** The Alternating Gap-Cross family is a genuine,
general, rigorously proved (identity + closed-form feasibility, not a
numeric heuristic) new sufficient-condition family, and it **does** exactly
and unconditionally close the specific round-14 $n=3$ near-tight witness
that motivated this round's work — a concrete, non-trivial win. But its
*marginal* contribution to case (b2)'s coverage over random samples is
small (a few percentage points at $n=3$, none detected at $n=4,5$ in this
sample size) — **it does not materially enlarge the proven fraction of
case (b2)**, because feasibility (the closed-form condition above) is
comparatively restrictive on generic random markings, even though it
happens to hold at the specific tuned near-tight witness. This is reported
honestly, not oversold: case (b2) remains open in general.

## Reviewer correction (round 15) — CONFIRMED SIGN BUG, NOT CERTIFIED AS WRITTEN

Independently re-verified by the round-15 proof-reviewer with a fresh script
(`/tmp/round15_review/counterexample_clean.py` and
`/tmp/round15_review/verify_altgapcross3.py`, not the builder's own). **The
identity's stated tail prefactor $(-1)^j$ is wrong** whenever the construction
uses an *odd* number of equal-value "untouched" pairs ($p_{2i-1}=p_{2i}$,
explicitly allowed by this lemma's own construction). Exact counterexample:
pieces $(45,45,31,27)$ sorted descending, $j=2$: pair $1$ is the equal/
untouched case ($45=45$, no cut), pair $2$ splits $31$ into $(30,1)$
sandwiching $27$. This is feasible per the lemma's own closed-form
feasibility test. The resulting multiset is $M=\{45,45,30,27,1\}$, giving
$A(M)=45-45+30-27+1=4$. The lemma's formula predicts
$\text{gap sum}+(-1)^jA(\text{tail})=\big(0+(-1)(31-27)\big)+(-1)^2\cdot0=-4$.
$4\ne-4$ — a genuine, exact sign error, not a numerical artifact.

**Root cause.** An equal/untouched pair contributes exactly $2$ elements to
$M$ (both cancel to a net contribution of $0$, but they are still $2$ raw
elements shifting every subsequent rank by $2$ — an *even* shift, preserving
parity), whereas a genuinely split pair contributes $3$ elements (an *odd*
shift, flipping parity). The lemma's derivation implicitly assumed every one
of the $j$ pairs contributes $3$ ranks ("$3j$ elements precede the tail"),
which is false whenever any pair is left untouched by equality. The correct
prefactor is $(-1)^{j'}$ where $j'$ counts only the pairs with
$p_{2i-1}>p_{2i}$ that are actually split, not all $j$ pairs.

**Scope of the damage.** A fresh 8000-trial re-check (mixed equal/split
pairs) confirms mismatches occur in exactly the sub-population with an odd
count of equal-pairs (0 mismatches when the equal-pair count is even or
zero, matching the corrected parity diagnosis). Both of this round's
headline witness closures (round-14 $n=3$, $n=4$ near-tight case-(b2)
witnesses) are **unaffected** — neither construction uses an equal/untouched
pair (the $n=3$ witness uses two genuine splits, no equal pairs; the $n=4$
witness is closed via the separate tie-based `cross-piece-sign-assignment-
identity` mechanism, not this construction) — so those two closures stand.
The **feasibility characterization** itself (which pairs/chain orders are
legally realizable) was independently re-checked and appears correct; only
the **identity's tail-sign prefactor** is wrong, and only in the
equal-pair-present, odd-equal-pair-count sub-case.

**Status at end of round 15: NOT certified as currently written.**

## Round-16 follow-up: the round-15 diagnosis was necessary but NOT sufficient

Task 1 of the round-16 outline instructed a "cheap hygiene" fix: relabel the
tail prefactor from $(-1)^j$ to $(-1)^{j'}$ ($j'=$ number of actually-split
pairs) and re-verify. **Executing this literally is not enough.** Testing
the round-15 diagnosis's own counterexample $(45,45,31,27)$, $j=2$ — the
*same* witness used to find the bug — under the tail-prefactor-only fix
still fails: here $j=2$ pairs total, $j'=1$ split pair, and the **tail is
empty** ($2j=4=m$), so $A(\text{tail})=0$ and the tail-prefactor correction
(whether $(-1)^2=1$ or $(-1)^1=-1$) multiplies a $0$ either way — **it
changes nothing for this example**, yet the bug is still present after that
fix, since $4\ne-4$ persists. The actual second source of the error (not
identified by the round-15 reviewer): the **gap-sum term's own per-pair
sign** was still being computed from the pair's *raw* index $i$
($(-1)^{i+1}$), but the correct sign is governed by the pair's **rank among
split pairs only**, $s(i_k)=k$ (derived and proved above, "The exact
identity... — CORRECTED, round 16"). The round-15 tail-prefactor diagnosis
is still correct and necessary (confirmed to matter whenever the tail is
*nonempty* and the equal-pair count is odd), but by itself it is not a
complete fix. The fully corrected identity (both the gap-sum signs and the
tail prefactor reindexed by split-rank $k$, not raw index $i$) is stated and
proved above, and independently re-verified by a fresh 30000-trial
exact-`Fraction` script with zero mismatches across all 17834 feasible
constructions (`/tmp/round-16/verify_altgapcross_fixed2.py`), including the
exact bug witness now resolved correctly ($4=4$).

**Status: CERTIFIED as corrected (round 16).** The feasibility
characterization (which pairs/chain orders are legally realizable) required
no change — it was already independently re-checked and found correct in
round 15, and this round's construction script (which sequentially assigns
each split pair's actual fragment values, verifying the full chain order
holds) reconfirms it. Both round-14 near-tight case-(b2) witnesses remain
closed under the corrected formula: the $n=3$ witness uses two genuine
splits and no equal pairs, so split-rank coincides with raw index and the
value is completely unchanged (re-verified exactly:
$\Phi=5159/10001\approx0.51585<a_3T\approx0.53333$); the $n=4$ witness was
never covered by this construction at all (closed via the separate
tie-based `cross-piece-sign-assignment-identity` mechanism), so it is
unaffected. Round 15's numeric case-(b2) coverage table
($5$–$17.5\%$ figures) is likewise unaffected, since it was computed on
generic (continuous-random) markings which have probability $0$ of an exact
tie, hence never exercised the corrected sub-case (see "Effect of the
correction on prior numeric coverage claims" above). **Per the round-16
outline's own instruction, this is a certification-hygiene fix, confirmed
(not merely assumed) to add no new coverage of case (b2)** — the corrected
identity governs the same feasible region and the same threshold comparison
as before on every marking without exact ties among paired pieces.

## Certification note (proof-builder, round 15; corrected round 16)

The identity is a direct corollary of the certified
`cross-piece-sign-assignment-identity.md` (itself built on the certified
`odd-run-reduction-lemma`) plus the certified `max-domination-lemma`; the
feasibility characterization is proved in full above (not merely tested)
via an explicit interval/supremum argument, and cross-checked against an
independent constructive search with zero disagreements over 8000 (round
15) plus 30000 (round 16, including mixed equal/split constructions)
trials.

**Origin:** `results/imo-2026-03/approaches/lp-duality-certificate.md`,
round 15, Task 2 (the feasibility/combinatorial half of the round-15
outline); sign bug found by the round-15 proof-reviewer; fully corrected
(gap-sum signs reindexed by split-rank, not just the tail prefactor) by the
round-16 builder, Task 1.
