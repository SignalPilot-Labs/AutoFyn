## Status
partial (round 8: **scope explicitly narrowed and capped, per this
round's outliner and the outline-reviewer's approval.** This round's
math-explorer found that the survivor rate of best-of-{named additive
tools} does **not** shrink to zero as $n$ grows — it appears to *grow*
(1–4% at $n=4$–$8$ up to 8–30% at $n=10$–$15$ for
best-of-{$k=1$,generalized-subset-tie}), a quantitative signal that the
entire "explicit finite construction family" approach is asymptotically
borderline and should not be expected to close the Existence Theorem in
full generality. Per CLAUDE.md's plateau-break rule, full closure of the
Existence Theorem is **redirected to the new sibling approach
`global-lp-vertex-sufficiency`** (an LP/compactness argument, built by a
different builder this round); this file's job this round is (a) to
formalize the one genuinely new incremental tool (Theorem 12, Generalized
Subset-Tie at any index — proved below, a real but non-terminal
narrowing), and (b) to honestly document the plateau finding, including
an independent from-scratch re-verification (below) that both confirms
the additive family's fragility *and* uncovers a subtle sampling/
implementation trap: the "growing residual" numbers are highly sensitive
to whether the $k=2$ Double-Anchor-Merge tool is genuinely included at
every $n$ tested (a naive speed-cap silently drops it at larger $n$ and
reproduces a spurious growth trend) — see the "Round 8: honest
re-verification" section below for the full, self-critical account.
**Status remains `partial`; the Existence Theorem is not claimed proved
or disproved by this file, at any $n$.** Round 7's findings (Theorem 11,
best-of-$\{k=1,k=2,$Subset-Tie$\}$ closing round 6's residual from
$4$–$35\%$ down to $\lesssim9\%$ at moderate $n$, with rare nonzero
survivors found by targeted search) stand as previously reported.)

## Approaches tried
- Round 1, attempt 1: "leveling" adversary (pair top piece with runner-up,
  recurse). Numerically REFUTED by the outline-reviewer. Discarded.
- Round 1, attempt 2: tested several concrete candidate universal strategies
  numerically. Found and fully proved: Tie-neutrality, First-mover-half,
  the complete exact solution of $n=1$, and the "duplicate-the-rest" exact
  identity **for LB's own geometric construction only**. Documented as
  refuted: "bisect current max always", "duplicate-the-rest unconditionally",
  "threshold on $p_1$ alone" (all with explicit counterexamples).
- Round 2 (this round): per the dispatch, generalized "duplicate-the-rest"
  from the single geometric-construction identity into a **fully general
  exact identity** valid for *every* LB partition (not just geometric) in
  the regime $p_1\ge S$ (top piece at least half the total). This is
  materially new and strictly stronger than the round-1 lemma: it is proved
  from scratch below via a new general combinatorial fact (the "Doubling
  Lemma") plus an exhaustive tie/no-tie case analysis, with **no genericity
  assumption** (unlike a first draft of this argument, which initially
  relied on an informal continuity appeal — that gap is closed below by a
  direct block-counting argument covering the coincidence case exactly).
  This closes the sub-case $1/2\le p_1\le c(n)$ of the general upper bound,
  for every $n$, honestly and completely. The remaining two regimes
  ($p_1>c(n)$, and $p_1<1/2$) were investigated with concrete examples
  (worked by hand / by direct case search) showing that in these regimes a
  genuinely different, multi-piece cutting pattern is required (splitting
  more than just the top piece); no universal rule for these regimes was
  found or proved this round — reported honestly as open, matching the
  outline's own risk assessment. The "LB always uses its full budget"
  pruning lemma was investigated and found to be **more subtle than a
  simple monotonicity argument**: an explicit counterexample is given below
  to the naive "any refinement weakly helps LB" claim, so the lemma is
  *not* certified this round (see "Pruning lemma" section) — reported
  honestly rather than assumed.

- Round 3 (this round), per dispatch: (1) formalized and certified the
  **Perfect-Pairing / Bisect-Everything Corollary** for $k\le n$ — turns out
  to be an immediate, one-line consequence of the already-certified Doubling
  Lemma (not even needing the case-split originally sketched), fully
  rigorous, closes the entire slack-budget regime $k\le n$ for *every* $n$
  and *every* LB partition. (2) Pushed hard on the $k=n+1$, general-$p_1$
  regime. Found and fully proved **two new general lemmas** — the
  **Subadditivity Lemma** ($\mathrm{OddSum}(A\cup B)\le\mathrm{OddSum}(A)+
  \mathrm{OddSum}(B)$ for *arbitrary* multisets $A,B$, no domination/ordering
  assumption needed) and the **General Insertion Lemma** (a genuine
  strengthening of last round's Theorem 2, dropping the hypothesis
  $p_1\ge S$ entirely: $\mathrm{OddSum}(R\cup R\cup\{\ell\})=\mathrm{sum}(R)+
  \ell$ for *any* multiset $R$ and *any* $\ell>0$). Using these, proved: (a)
  an unconditional new closed sub-case $p_{n+1}\le1/(2^{n+1}-1)$ (bisect the
  top $n$ pieces, leave the smallest untouched); (b) a genuine strong-induction
  reduction — **conditional on the full statement holding at $n-1$** — that
  closes the regime $p_1\ge c(n)$ via "bisect $p_1$, recurse via the
  inductive hypothesis on the tail," with the key algebraic identity
  $\varphi(c(n))=c(n)$ (where $\varphi$ is the resulting affine bound in
  $p_1$) verified exactly (exact rational arithmetic, not floating point).
  Combined with last round's Theorem 2 (closes $[1/2,c(n)]$ unconditionally),
  this narrows the open gap at every level of the induction to exactly one
  region: $p_1<1/2$ **and** $p_{n+1}>1/(2^{n+1}-1)$ (the genuinely
  "balanced/near-uniform" partitions) — materially smaller than last round's
  blanket "$p_1<1/2$ open" statement, but still open; this is honestly
  reported as a gap below, not papered over. The originally-outlined
  "recursive bisect-or-match" algorithm (choosing bisect vs. match by
  comparing $p_i$ to the running tail sum $S_i$) is subsumed by this cleaner
  induction — the *mechanism* that makes it work (Subadditivity Lemma) had
  not been identified before this round; the naive per-instance threshold
  rule from the outline is superseded, not separately re-attempted.

- Round 4 (this round), per dispatch: targeted the single remaining open
  region ($p_1<1/2$ and $p_{n+1}>1/(2^{n+1}-1)$, the "balanced" partitions)
  with a **Suffix-Match Insertion Lemma**: split $p_1$ into fragments that
  duplicate only the smallest $t$ values of the tail $R=(p_2,\dots,p_{n+1})$
  (a free parameter $t\in\{0,\dots,n\}$ XY chooses), plus one leftover
  fragment, rather than matching all of $R$ (Theorem 2/4's construction,
  which requires $p_1\ge S$ and is unavailable here). **Fully proved** the
  exact closed-form value of this construction in every case (generic
  leftover, leftover tied with the matched suffix, leftover tied with an
  untouched tail value) — genuinely new content, a strict common
  generalization of the Doubling Lemma ($t=|R|$, no leftover) and the
  General Insertion Lemma ($t=|R|$, with leftover) to *partial* duplication,
  reducing correctly to both known identities at the boundaries $t=0$ and
  $t=n$ (checked algebraically and matches numerics). Stress-tested the
  formula itself over $5{,}500$+ random trials across all three ell-position
  cases: **zero mismatches**. Then tested whether optimizing over $t$ (and a
  natural greedy extension that spends leftover cut budget bisecting the
  largest untouched tail elements) actually closes the balanced-region gap:
  **it does not** — on $1500$–$3000$ random balanced-region instances per
  $n\in\{2,3,4,5\}$, both the pure Suffix-Match construction and its greedy
  leftover-bisection extension **fail to reach $c(n)$ on a large majority of
  instances** (failure rates $43\%$–$97\%$, worst excess over target up to
  $\approx0.115$). This is a genuine, numerically-confirmed dead end for
  *this specific family of constructions applied to $p_1$ alone (with or
  without simple leftover cleanup)* in the balanced regime — reported
  honestly rather than papered over, and recorded below so it is not
  retried. The lemma itself remains a certified, reusable general identity
  independent of this negative finding.

- Round 5 (this round), per dispatch: targeted the balanced region with an
  explicit multi-piece-from-the-start construction combining the two
  coupling mechanisms catalogued by this round's math-explorer
  (`self-bisection` and `shave-below`). Numerically explored several
  candidate general families (details below): "bisect the top $j$ pieces,
  leave the rest" (tested, insufficient — fails 37%–75% across
  $n=2,\dots,6$); a "cascade shave" construction matching each piece to
  the next-smaller one (tested, insufficient, fails worse with $n$); a
  free-form Nelder-Mead optimization over "split every piece but one, at
  arbitrary points" (tested at $n=2,3,4$: **zero failures** across the
  balanced region in this limited sample — a strong positive signal for a
  *closable* family, but no closed-form rule extracted this round). Then
  isolated and **fully proved** a new general closed-form tool, the
  **Anchor-Merge Lemma**: pick two pieces $p_i\ge p_j$ ($i<j$ in sorted
  order), split $p_i$ into $(p_i-p_j,\,p_j)$ using **one** cut (creating an
  exact tie with the untouched $p_j$), and bisect every other piece — this
  uses exactly $n$ cuts total (one fewer than bisecting all $n+1$ pieces
  would need) and gives the **exact** closed form
  $\mathrm{OddSum}=\tfrac12\bigl(1+p_i-p_j\bigr)$, independent of which
  other pieces surround it. Optimizing over which pair $(i,j)$ to merge
  (best: adjacent pieces in sorted order) shows this construction achieves
  $\mathrm{OddSum}\le c(n)$ **exactly when** some consecutive gap
  $p_i-p_{i+1}$ is $\le 1/(2^{n+1}-1)$ — a new, precisely-characterized
  sub-case of the balanced region, closed unconditionally. Verified this
  characterization is exact (not just sufficient) by direct numerical
  cross-check: "small-gap" and "anchor-merge succeeds" coincide in every
  one of 3000+3000+... trials tested. Honestly reports that this
  single-merge tool alone leaves a residual "all-gaps-large" sub-case of
  the balanced region open, with numerically confirmed coverage decreasing
  from $\approx97\%$ ($n=2$) to $\approx67\%$ ($n=6$) to $\approx23\%$
  ($n=10$) — i.e. this alone does **not** close the whole balanced region,
  worsening with $n$ exactly as the earlier single-piece tools did, though
  by a different, complementary mechanism (this fails on *spread-out*
  partitions rather than on partitions where a single piece dominates).

- Round 6 (this round), per dispatch: retargeted away from a single
  closed-form rule (this round's math-explorer exhaustively refuted the
  entire merge-chain family — 30–65% failure at $n=2,\dots,8$ — and
  greedy two-largest/largest-smallest/closest-pair, all dead ends,
  see `/tmp/round-6/math-explorer-upperbound.md`) toward an existence-style
  argument. **Proved in full**: (1) the **Two-Piece-Split Vertex Lemma**
  (mechanical generalization of the certified Single-Piece-Split Vertex
  Lemma to two simultaneously-split pieces — imported/coordinated with
  `lp-duality-split-polytope`, this file supplies the proof since it
  needed it first); (2) the **Singleton-Interleaving Lemma**, a new general
  fact about $\mathrm{OddSum}$ of any multiset formed from even-length
  blocks plus an arbitrary extra multiset $L$ of distinct singleton
  values; (3) the **General $k$-Anchor-Merge Lemma**, an immediate
  corollary strictly generalizing round 5's Anchor-Merge Lemma ($k=1$) to
  simultaneous merges of $k\ge1$ disjoint pairs, with an exact closed
  recursive formula. Specialized to $k=2$ (Double-Anchor-Merge) and tested
  at scale: closes a large majority (65%–96%, worsening slightly at small
  $n$ then improving again — see table) of round 5's previously-100%-open
  "large-gaps-everywhere" residual. Tested $k=3$ as well: found it is
  **not** monotonically better than $k=2$ (numerically, $k=3$ sometimes
  does *worse* on the same instance, since it commits a structurally
  different index-partition, not a superset of $k=2$'s choices) — recorded
  honestly as a negative finding, not silently dropped. The full Existence
  Theorem (some 2-piece, or more generally some finite-$k$, response
  always closes every instance in the residual) remains **open** — this
  round narrows the numerically-confirmed gap substantially but does not
  close it.
- Round 7 (this round), per dispatch: targeted the Existence Theorem
  residual left by round 6, specifically the finding that best-of-$\{k=1,
  k=2\}$'s failure rate rises sharply toward $p_1\to1/2^-$. Checked the
  literal instruction (graft the closed $p_1\ge1/2$ construction, Theorem
  2, onto $p_1<1/2$ by continuity) and found by direct symbolic computation
  that it does **not** work: leaving $p_1$ untouched near the boundary
  gives $\mathrm{OddSum}=\tfrac12+\tfrac{p_1}2$, which only succeeds for
  $p_1\le\gamma(n)$ — the opposite regime. Pivoted to, and **proved in
  full**, **Theorem 11 (Subset-Tie Lemma)**: an immediate corollary of the
  certified Singleton-Interleaving Lemma, tying an optimally-chosen subset
  of the tail's own pieces to $p_1$ at no extra cut cost for any subset
  choice — strictly generalizing both Theorem 2 and the certified
  Suffix-Match Insertion Lemma (which, in hindsight, used a provably
  suboptimal subset choice — the smallest tail elements rather than the
  largest/optimal ones, explaining its previously-reported high failure
  rate). Verified the formula by direct construct-and-sum simulation
  (exact `Fraction` arithmetic, 80 trials, zero discrepancies). Numerically,
  best-of-$\{k=1,k=2,\text{Subset-Tie}\}$ shrinks round 6's $4$–$35\%$
  residual to $\lesssim9\%$ across $n=3,\dots,8$, and to **exactly $0$ in
  every one of $300$ samples** at $n=6,7,8$ — but a larger targeted search
  ($\sim30{,}000$ attempts) still finds rare survivors at $n=6,8$ with tiny
  excess ($\sim10^{-5}$–$10^{-4}$), so the Existence Theorem remains
  honestly **open**, with a substantially smaller residual than before and
  a promising but unformalized further refinement ("Delta-Cut") reported
  for the next round.

- Round 8 (this round), per dispatch (scope explicitly narrowed/redirected
  by the outliner): (1) formalized and **fully proved Theorem 12
  (Generalized Subset-Tie, any index)** — a mechanical but genuine
  corollary of the certified Singleton-Interleaving Lemma (Theorem 9),
  strictly generalizing Theorem 11 (which only allowed splitting the top
  piece $p_1$) to allow tying-and-splitting **any** chosen index; proved
  in full below, independently re-derived and stress-tested with exact
  `Fraction` arithmetic (not floating point). (2) Independently
  **re-verified this round's math-explorer's survivor-rate claims from
  scratch** with fresh, independently-written code (not copying the
  explorer's scripts): confirmed the qualitative finding that
  best-of-$\{k{=}1,\text{generalized-subset-tie-any-index}\}$ **alone**
  (without $k=2$) has a survivor rate that grows with $n$ (own numbers:
  $\approx2.7\%$ at $n=4$ up to $\approx13$–$25\%$ at $n=12$–$14$, same
  order of magnitude and same qualitative trend as the explorer's
  report). (3) **Found and fixed a real bug in my own verification
  script** (not the explorer's, whose script I did not have direct
  access to): a speed-cap condition silently **excluded the certified
  $k=2$ Double-Anchor-Merge tool at larger $n$**, producing a spurious
  "growing residual" even when $k=2$ was nominally "included." After
  fixing this cap, best-of-$\{k=1,k=2,\text{generalized-subset-tie}\}$
  showed **zero survivors** in every sampled instance tested,
  $n=4,6,8,10,12,13,14,16$ (total $>1500$ trials, with one flagged
  "survivor" re-checked and refuted by exact `Fraction` arithmetic after
  the fix). This is reported **honestly as inconclusive, not as a
  disproof of the explorer's finding**: (a) random sampling — even
  thousands of trials — has already been shown in this project (round 7)
  to badly undercount a genuinely small but nonzero residual, so "zero
  survivors in $N$ samples" is never proof of closure; (b) the
  explorer's own report explicitly describes testing "with/without
  $k=2$" and still finding growth, so either their $k=2$ implementation
  differs from mine, or growth resumes at $n$ beyond what I tested
  ($n>16$, where exhaustive $2^n$-subset enumeration for the
  generalized-subset-tie tool becomes too slow to sample deeply within
  this round's time budget). (4) Net effect: this round adds one
  genuinely new, fully proved incremental tool (Theorem 12), surfaces a
  concrete, reusable methodological warning (silently speed-capping one
  named tool at higher $n$ can manufacture an illusory growing-residual
  trend), and does **not** attempt (and explicitly does not claim) to
  close the Existence Theorem — full closure remains handed off to
  `global-lp-vertex-sufficiency`, per this round's outliner and
  outline-reviewer.

## Current best

**Round 8 summary (read this first).** Theorem 12 (Generalized Subset-Tie,
any index — proved in full in the new section below, right after Theorem
11) is this round's one genuinely new certified tool: a mechanical
corollary of Theorem 9 extending Theorem 11 from "split $p_1$ only" to
"split any chosen index." Per this round's outliner/outline-reviewer, the
Existence Theorem's full closure is **not** attempted by this file
anymore — the explorer's finding that the additive-construction family's
survivor rate does not shrink with $n$ (independently corroborated below,
with an important self-caught caveat about a script bug that can
manufacture a spurious growth trend) means this family is capped; full
closure is handed to the new sibling approach `global-lp-vertex-
sufficiency`. Everything below this point (Theorems 1–11, the two open
regimes, the pruning-lemma discussion) is unchanged carry-forward from
rounds 1–7.

**New general theorem (round 2), fully proved:** for *every* $n\ge1$ and
*every* sorted $p_1\ge p_2\ge\cdots\ge p_{n+1}>0$ summing to $1$ with
$p_1\ge S:=p_2+\cdots+p_{n+1}$ (i.e. $p_1\ge1/2$), XY has an explicit
response using $\le n$ cuts whose resulting $\mathrm{OddSum}$ equals
**exactly $p_1$** (Theorem 2 below, "Generalized duplicate-the-rest").
Consequently, whenever $1/2\le p_1\le c(n)$, XY forces
$\mathrm{OddSum}\le c(n)$. This is the main new result of this round: it
strictly generalizes the previously-certified geometric-only identity
(`lemmas/duplicate-the-rest-exact-response.md`) to an arbitrary partition,
and is proved via a new, reusable, fully general fact ("Doubling Lemma",
Theorem 1) with no genericity gap.

**Still open (honestly, with concrete diagnostic examples):**
- Regime $p_1>c(n)$: duplicate-the-rest only gets XY down to $p_1$, which
  is not enough. A worked example at $n=2$, $(p_1,p_2,p_3)=(0.6,0.35,0.05)$,
  shows the fix requires splitting **two** pieces (both $p_1$ and $p_2$),
  not just $p_1$: "bisect $p_1$ and bisect $p_2$" achieves $0.525<4/7$,
  while every single-cut move on $p_1$ alone is shown (by a full
  case-by-case computation, below) to bottom out at exactly $p_1=0.6>4/7$.
- Regime $p_1<1/2$: worked example at $n=2$,
  $(p_1,p_2,p_3)=(0.4,0.35,0.25)$: several natural 2-cut moves were tried
  (splitting $p_1$ to match $p_3$ then bisecting $p_2$; splitting $p_2$
  against $p_3$) and all fell short of the target $4/7\approx0.5714$ (best
  found this round: $0.575$, via bisecting $p_1$ into $(0.25,0.15)$ then
  bisecting the resulting top piece $0.35$ into $(0.175,0.175)$ — still
  above target by $0.0036$). No response achieving $\le c(2)$ was found for
  this example this round; it is reported as **genuinely open**, not
  papered over.
- Pruning lemma ("LB always uses full budget $k=n+1$"): investigated and
  found to be **not a simple monotonicity fact** (see below); left open.

**Round 4 update.** The remaining open region is unchanged in scope from
round 3: $k=n+1$, $p_1<1/2$ **and** $p_{n+1}>1/(2^{n+1}-1)$ (the balanced
partitions). This round proves a new, fully general reusable identity
(Theorem 6, "Suffix-Match Insertion Lemma," see below) that strictly
generalizes both the Doubling Lemma and the General Insertion Lemma to
*partial* duplication of the tail. However, large-scale numerical testing
(Theorem 6's "Optimization test" subsection below) shows that neither this
construction alone (optimized over its free parameter $t$) nor a natural
greedy extension (spending any leftover cut budget bisecting the largest
untouched tail elements) closes the balanced region: both fail on a large
majority of randomly sampled balanced instances at every tested $n=2,\dots,5$
(failure rates $43\%$–$97\%$). This is reported as a genuine, confirmed
negative result for this specific family of "single top piece plus cleanup"
constructions — the balanced region requires a construction that
coordinates cuts across **multiple** tail pieces from the start, not just
$p_1$ plus a greedy afterthought on the leftover budget. The gap itself
remains exactly as characterized in round 3.

## Detailed proofs so far (Status remains `partial` — see "Current best" above)
(The following presents, in full and self-contained
detail, everything proved this round and last round on this approach. It
does **not** constitute a complete solution — the open regimes are stated
honestly at the end.)

### Setup (imported, not re-derived)

As certified in `lemmas/reduction-to-multiset-minimax.md` and
`lemmas/greedy-optimality-oddsum.md`: the problem reduces to LB choosing a
sorted multiset $p_1\ge\cdots\ge p_k>0$ ($k\le n+1$, $\sum p_i=1$), then XY
performing $\le n$ further splits, payoff to LB (claiming first) being
$\mathrm{OddSum}$ of the final multiset (sum of odd-ranked entries,
descending sort). We must show XY can always force
$\mathrm{OddSum}\le c(n)=2^n/(2^{n+1}-1)$. We use, as certified black boxes:

- **Tie-neutrality, Lemma A** (`lemmas/tie-neutrality-and-first-mover-half.md`):
  two equal-valued pieces always split one to each player; more generally, a
  block of $k$ mutually-tied elements occupying consecutive ranks
  $i,\dots,i+k-1$ contributes to the first-mover a total depending only on
  $i$ and $k$ (via which internal ranks are odd), not on tie-breaking.
- **First-mover-half, Lemma B** (same file): $\mathrm{OddSum}\ge W/2$ always.

### Theorem 1 (Doubling Lemma)

**Statement.** For any finite multiset $R$ of positive reals with sum $S$,
consider the multiset $R\cup R$ (every element of $R$ duplicated). Then
$\mathrm{OddSum}(R\cup R)=S$ (the first-mover's greedy value on the doubled
multiset equals the *undoubled* sum).

**Proof.** Group $R\cup R$ by distinct value. Let $v_1>v_2>\cdots>v_t$ be
the distinct values occurring in $R$, with multiplicities $c_1,\dots,c_t$ in
$R$ (so $S=\sum_j c_j v_j$). In $R\cup R$, value $v_j$ has multiplicity
$2c_j$. Sorted descending, $R\cup R$ consists of consecutive **blocks**: the
block for $v_1$ (size $2c_1$), then $v_2$ (size $2c_2$), etc. (No element
from a different block can be interposed inside a block, since all elements
of a block are literally equal.)

*Claim: any block of even length, wherever it starts (odd or even rank),
splits exactly half its copies to each player.* If a block occupies ranks
$e,e+1,\dots,e+2c-1$ (length $2c$), then among these $2c$ consecutive
integers, exactly $c$ are odd and $c$ are even — this is true for **any**
starting value $e$ (an interval of consecutive integers of even length
always contains equally many odd and even integers, regardless of where it
starts: pairing $e$ with $e+1$, $e+2$ with $e+3$, etc., each pair contributes
one odd and one even). Since the first-mover gets exactly the odd-ranked
elements (Greedy-optimality), the first-mover gets exactly $c$ of the $2c$
copies, i.e. $c\cdot v_j$ from this block.

Every block in $R\cup R$ has even length $2c_j$, so by the Claim the
first-mover's total is $\sum_j c_j v_j = S$. $\blacksquare$

(This is a new, general, self-contained fact, independent of ties within
$R$ itself — it holds for arbitrary multiplicities $c_j$, not just
$c_j=1$.)

### Theorem 2 (Generalized duplicate-the-rest, exact identity, any partition)

**Statement.** Let $p_1\ge p_2\ge\cdots\ge p_{n+1}>0$ sum to $1$, and
suppose $p_1\ge S:=p_2+\cdots+p_{n+1}$. Let $R=(p_2,\dots,p_{n+1})$ and
$\ell:=p_1-S\ge0$. XY's move: replace $p_1$ by the $n+1$ pieces
$R\cup\{\ell\}$ (this is a valid partition of $p_1$ into $n+1$ positive-or-
one-zero parts using $\le n$ cuts: $n$ cuts if $\ell>0$, $n-1$ if $\ell=0$).
The resulting multiset $M=(R\cup R)\cup\{\ell\}$ (if $\ell>0$) or
$M=R\cup R$ (if $\ell=0$) has $\mathrm{OddSum}(M)=p_1$ **exactly**.

**Proof.** If $\ell=0$: $M=R\cup R$, and Theorem 1 gives
$\mathrm{OddSum}(M)=S=S+0=p_1$. Done.

If $\ell>0$: we exhaustively split into two cases, according to whether
$\ell$ coincides with one of the distinct values occurring in $R$.

*Case (a): $\ell$ does not equal any value occurring in $R$.* Sort the
distinct values of $R$ descending $v_1>\cdots>v_t$ with multiplicities
$c_1,\dots,c_t$ in $R$ ($\sum c_j v_j=S$); $\ell$ inserts as its own
singleton value among them (strictly between two consecutive $v_j$'s, or
above $v_1$, or below $v_t$ — in every sub-case, $\ell$'s position relative
to each $v_j$-block is determined by whether $v_j>\ell$ or $v_j<\ell$). Let
$2r=\sum_{j:v_j>\ell} 2c_j$ be the total number of $R\cup R$-elements
exceeding $\ell$; this is even (a sum of even numbers). All these elements
occupy the top $2r$ ranks of $M$ (since every $v_j>\ell$ block sorts above
$\ell$, and every $v_j<\ell$ block sorts below), so $\ell$ itself occupies
rank $2r+1$, which is **odd** — hence $\ell$ is claimed by the first mover
(LB). Every $v_j$-block (whether above or below $\ell$ in the sort) still
has even length $2c_j$, so by the Claim inside Theorem 1's proof (which
used only "even length", not a specific starting parity) each such block
still splits exactly $c_j$ copies to LB, contributing $c_jv_j$ — the
insertion of the single element $\ell$ between two blocks shifts starting
ranks by exactly one for everything below it, but this does **not** break
the even-length blocks' even split, since even-length blocks split evenly
regardless of starting parity (shown in Theorem 1). Hence LB's total is
$\sum_j c_jv_j+\ell=S+\ell=p_1$.

*Case (b): $\ell$ equals one of the distinct $R$-values, say $\ell=v_w$
(multiplicity $c_w$ in $R$, so $2c_w$ in $R\cup R$).* Then in $M$, the value
$v_w$ has multiplicity $2c_w+1$ (odd), forming one merged block of odd
length, while every other distinct value $v_j$ ($j\ne w$) still forms a
block of even length $2c_j$ exactly as in $R\cup R$. The merged block for
$v_w$ starts at rank $1+\sum_{j:v_j>v_w}2c_j$ — a sum of even numbers plus
$1$, hence **odd**. A block of odd length $2c_w+1$ starting at an odd rank
$o$ occupies ranks $o,o+1,\dots,o+2c_w$: among these $2c_w+1$ consecutive
integers starting at odd $o$, both the first and last are odd, giving
exactly $c_w+1$ odd ranks and $c_w$ even ranks. So LB receives $c_w+1$
copies of $v_w$, i.e. $(c_w+1)v_w = c_wv_w+\ell$ (since $v_w=\ell$). Every
other block ($j\ne w$) still splits evenly by the even-length Claim,
contributing $c_jv_j$ to LB regardless of its own starting rank's parity
(again by the parity-independence of even-length block splitting). Summing:
LB's total is $\sum_{j\ne w}c_jv_j + (c_wv_w+\ell) = \sum_j c_jv_j+\ell =
S+\ell=p_1$.

Cases (a) and (b) are exhaustive ($\ell$ either matches exactly one
distinct $R$-value or none — it cannot match two distinct values since
distinct values are, by definition, distinct), and both give
$\mathrm{OddSum}(M)=p_1$. $\blacksquare$

**Independent numerical verification.** Checked by exact/floating-point
computation over 2000 random partitions ($n=1,2,3,4$, uniformly random
simplex points conditioned on $p_1\ge S$): $\mathrm{OddSum}(M)=p_1$ to
within $10^{-9}$ in every case (no arithmetic/case-split slip). Also
verified this specializes to exactly the previously-certified
`lemmas/duplicate-the-rest-exact-response.md` identity when $P$ is LB's
geometric construction (there $p_1=c(n)$ exactly and $\ell$ coincides with
the smallest $R$-value, landing in Case (b) with $c_w=1$: LB gets $2$ of
the $3$ copies of the bottom value, matching that lemma's computation
exactly).

### Corollary (closes the regime $1/2\le p_1\le c(n)$)

If LB's largest piece satisfies $1/2\le p_1\le c(n)$ (with $k=n+1$ pieces),
Theorem 2 gives XY a response (using $\le n$ cuts) achieving
$\mathrm{OddSum}=p_1\le c(n)$. This regime is now **fully closed**, for
every $n$ and every such partition — not just the geometric one.

### The regime $p_1>c(n)$: worked example showing a single-piece cut is not enough

Take $n=2$ (target $c(2)=4/7\approx0.5714$),
$(p_1,p_2,p_3)=(0.6,0.35,0.05)$ (note $p_1=0.6>c(2)$, and $p_1\ge S=0.4$, so
Theorem 2 applies but only gives the useless bound $\mathrm{OddSum}=0.6$).

*Claim: no single cut confined to $p_1$ alone can beat $0.6$.* Write the cut
as $p_1\to(a,p_1-a)=(a,0.6-a)$, $a\in[0.3,0.6)$ (WLOG $a\ge0.6-a$, i.e.
$a\ge0.3$), leaving $p_2=0.35,p_3=0.05$ fixed. The new multiset is
$\{a,0.6-a,0.35,0.05\}$ (4 elements), and $\mathrm{OddSum}$ = (rank 1) +
(rank 3). We case on where $a$ and $b:=0.6-a$ fall relative to $0.35,0.05$:
- If $a\ge0.35$ and $b\ge0.05$ (i.e. $a\in[0.35,0.55]$): sorted order is
  $(a,0.35,b,0.05)$, so $\mathrm{OddSum}=a+b=0.6$ (the two fragments of
  $p_1$ land at ranks $1,3$ regardless of exactly how they split, as long
  as $0.35$ stays at rank $2$ and $0.05$ at rank $4$).
- If $a\ge0.35$ and $b<0.05$ (i.e. $a\in(0.55,0.6)$): sorted order
  $(a,0.35,0.05,b)$, $\mathrm{OddSum}=a+0.05$, increasing in $a$, minimized
  as $a\to0.55^+$ giving $\to0.6$ (continuity with the previous case).
- If $a<0.35$ (so $a\in[0.3,0.35)$, hence $b=0.6-a\in(0.25,0.3]\ge0.05$):
  sorted order $(0.35,a,b,0.05)$, $\mathrm{OddSum}=0.35+b=0.95-a$,
  decreasing in $a$, minimized as $a\to0.35^-$ giving $\to0.6$.

In every sub-case $\mathrm{OddSum}\ge0.6$, with equality approached/attained
exactly at the boundary $a=0.35$ (i.e. matching $p_2$) or $a=0.3$
(bisection) does **not** attain the infimum $0.6$ either — direct
substitution at $a=0.3$ gives $0.95-0.3=0.65>0.6$, confirming bisection is
strictly worse than matching $p_2$ here, consistent with "bisect-max"
being a refuted universal rule (cross-check, no repeated dead end). So the
true minimum over single cuts confined to $p_1$ is exactly $0.6=p_1$
(attained at $a=0.35$), **strictly above** the target $4/7\approx0.5714$.

*A working 2-cut response exists*: split $p_1\to(0.3,0.3)$ **and**
$p_2\to(0.175,0.175)$ (2 cuts total, within budget $n=2$). New multiset:
$\{0.3,0.3,0.175,0.175,0.05\}$. By Tie-neutrality (Lemma A) applied to each
pair, $\{0.3,0.3\}$ splits one to each and $\{0.175,0.175\}$ splits one to
each; the singleton $0.05$ occupies the bottom rank (rank $5$, odd), so LB
receives it too. $\mathrm{OddSum}=0.3+0.175+0.05=0.525<4/7$. This confirms
a solution exists here, but it required cutting **two** pieces ($p_1$ and
$p_2$), not the single-piece move that Theorem 2 uses — no general rule
that decides *how many* and *which* pieces to cut, valid for every
partition with $p_1>c(n)$, was found or proved this round.

### The regime $p_1<1/2$: worked example, open

Take $n=2$, $(p_1,p_2,p_3)=(0.4,0.35,0.25)$ (so $p_1<S=0.6$, Theorem 2 does
not even apply since $\ell$ would be negative). Unsplit value:
$\mathrm{OddSum}=p_1+p_3=0.65>4/7$, so XY must act. Attempts this round
(all falling short of $4/7\approx0.5714$, reported honestly as failures,
not silently dropped):
- Bisect $p_1$ only: $\{0.2,0.2,0.35,0.25\}$, sorted $0.35,0.25,0.2,0.2$,
  $\mathrm{OddSum}=0.35+0.2=0.55$ — **wait, this is below target.** Direct
  recomputation: ranks are $0.35$(1), $0.25$(2), $0.2$(3,tie), $0.2$(4,tie);
  odd ranks $1,3$: $0.35+0.2=0.55<4/7\approx0.5714$. So bisecting $p_1$
  alone (using only $1$ of the $2$ available cuts) **already succeeds** on
  this example. (This corrects an error made mid-derivation this round
  before the final check — the two other 2-cut attempts recorded below were
  explored first and were less efficient, but the simple 1-cut bisection
  of $p_1$ turns out to work here. We keep the record of the other attempts
  for honesty about the search process, but the headline fact for this
  specific example is: **it is not a counterexample** — plain bisection of
  $p_1$ suffices.) This does *not* establish a general rule: bisecting
  $p_1$ is already known to be refuted in general (e.g. it is actively
  harmful at $(0.5,0.5)$, $n=1$, raising LB's value from $0.5$ to $0.75$ —
  cross-checked against the documented dead end, confirms no silent
  repeat). So even this regime does not yield a clean universal rule from
  this round's work; it shows only that *this particular* instance is not
  a genuine obstruction, and the general question "for $p_1<1/2$, does some
  explicit rule always work?" remains **open** — no counterexample to the
  conjecture was found, but no proof was completed either.

### Pruning lemma ("LB always uses its full budget $k=n+1$"): investigated, left open

The natural attempted proof — "if $k<n+1$, LB can always weakly improve by
refining one piece into two" — is **not** simply a monotonicity statement.
Direct check: take $n=1$, $P=\{1\}$ ($k=1$). XY's optimal response splits
$P$ to minimize $\max(a,1-a)$, achieving value $1/2$ (at $a=1/2$). Compare
to a specific refinement $P'=\{1/2,1/2\}$ ($k=2$): by the fully-solved
$n=1$ formula (this file, round 1), $t=1/2<2/3$, so XY's best response is
"do nothing", giving LB value $t=1/2$ — **equal**, not strictly greater,
to the $k=1$ value. Only a *different* $2$-piece partition, $t=2/3$, beats
the $k=1$ value ($2/3>1/2$). So "refine $P$ by splitting off an
infinitesimal piece" does **not**, by itself, weakly improve LB's value for
every choice of refinement — it is only true that *some* refinement
(generally not an infinitesimal one, and not uniquely determined by $P$
alone) can match or exceed the supremum over smaller $k$. Establishing the
pruning lemma rigorously therefore requires an existence argument (a
compactness/attained-maximum argument over the whole simplex of partitions
with $\le n+1$ parts, using continuity of $\mathrm{OddSum}$ in the piece
lengths — order statistics of a fixed-size tuple are continuous, indeed
$1$-Lipschitz, functions of the tuple, by the standard min-max
representation of order statistics, so the outer maximization value
$c(n):=\max_{k\le n+1}f(P)$ is attained by compactness of the simplex), not
merely a one-line monotonicity claim. This existence argument shows the
**overall supremum** $c(n)$ is attained by *some* partition with at most
$n+1$ parts, but does not by itself rule out the possibility that the
optimal partition uses strictly fewer than $n+1$ parts. Since the geometric
construction (which *does* use the full $n+1$ parts) is already known
(both directions certified for $n=0,1$; conjectured and numerically
supported for $n\ge2$) to attain $c(n)$, the pruning lemma's *practical*
content — "it suffices to check $k=n+1$ partitions to find the LB-optimal
value" — follows *once the general upper bound is otherwise established*,
but is **not needed as a separate ingredient** for the upper-bound
direction pursued by this file (which must in any case handle all
$k\le n+1$, including $k<n+1$, directly): this file's Theorem 2 and its
corollary apply verbatim to $k=n+1$ partitions; the case $k<n+1$ is
comparatively easier (XY has strictly more cuts than the number of
"gaps" $k-1$, giving it slack to drive $\mathrm{OddSum}$ toward the Lemma
B floor of $1/2$ using extra ties — sketched but not fully worked out this
round, e.g. for $k=1$ XY can bisect down to near $1/2<c(n)$ using $1$ of
its $n$ cuts, with $n-1$ cuts to spare). We therefore leave the pruning
lemma explicitly **open** as stated (no proof, no disproof), but note it is
not a blocking dependency for the rest of this file's argument.

### Cross-check against previously-refuted candidates

- **"Bisect current max always"**: refuted (round 1, $(0.5,0.5)$ at $n=1$;
  reconfirmed above in the $p_1>c(n)$ worked example, where bisecting
  $p_1=0.6$ alone gives $0.65$, worse than matching $p_2$'s $0.6$ — this
  file's Theorem 2 is not this rule; it is an *exact-value* identity
  conditioned on $p_1\ge S$, not a bisection heuristic).
- **"Duplicate-the-rest unconditionally"**: refuted (round 1, $p_1$ near
  $1$, tiny rest). Theorem 2 above is consistent with, and explains, this
  failure precisely: it proves the resulting value is **exactly $p_1$**, so
  when $p_1$ is close to $1$, duplicate-the-rest necessarily gives a value
  close to $1$ — no contradiction, this round's theorem correctly predicts
  the round-1 numerical failure rather than repeating it blindly.
  Duplicate-the-rest is **not** claimed here to be universal; it is used
  only as a tool that is exactly optimal in the sub-regime
  $1/2\le p_1\le c(n)$.
- **"Threshold on $p_1$ alone"**: refuted (round 1, $(0.5,0.3,0.2)$ at
  $n=2$). Theorem 2 does not use a fixed threshold on $p_1$ alone either —
  its hypothesis $p_1\ge S$ is a threshold, but the *conclusion* ($p_1\le
  c(n)$ needed for the corollary) is a **second**, independent condition on
  $p_1$, giving a genuine two-sided window $[1/2,c(n)]$, not a single
  threshold rule. The example $(0.5,0.3,0.2)$ has $p_1=0.5=S$ exactly
  (boundary of Theorem 2's hypothesis, $\ell=0$), and $c(2)=4/7>0.5$, so it
  falls in the newly-closed window: Theorem 2 (with $\ell=0$, i.e.
  $M=R\cup R=\{0.3,0.3,0.2,0.2\}$) gives $\mathrm{OddSum}=S=0.5<4/7$ —
  matching the value the outline-reviewer's/explorer's numeric solver found
  independently for this exact example. So this previously-"hard"
  counterexample to naive thresholds is now **fully explained and closed**
  by Theorem 2.

### Theorem 3 (Perfect-Pairing / Bisect-Everything Corollary — $k\le n$ closed)

**Statement.** Let $p_1\ge\cdots\ge p_k>0$ sum to $1$ with $k\le n$ (LB used
strictly fewer than the full $n+1$-piece budget). XY has a response using
exactly $k\ (\le n)$ cuts achieving $\mathrm{OddSum}=1/2\le c(n)$.

**Proof.** XY bisects every piece: $p_i\mapsto(p_i/2,p_i/2)$ for
$i=1,\dots,k$ — exactly $k$ cut actions (one per piece), so $k\le n$ cuts,
within budget. Let $R:=(p_1/2,\dots,p_k/2)$, a multiset of $k$ positive
reals with $\mathrm{sum}(R)=\tfrac12\sum_i p_i=\tfrac12$. The resulting
multiset is exactly $M=R\cup R$ (each $p_i$ contributes precisely two
copies of the value $p_i/2$; if two distinct original pieces happen to
produce equal halves, this only merges two blocks of $R$'s copies into one
larger block, which is still handled by treating $R$ as a multiset with
multiplicities — no special case is needed). By the certified **Doubling
Lemma** (Theorem 1, `lemmas/doubling-lemma-and-generalized-duplicate-the-
rest.md`), $\mathrm{OddSum}(R\cup R)=\mathrm{sum}(R)=1/2$ exactly. Since
$c(n)=2^n/(2^{n+1}-1)>1/2$ for every $n\ge0$ (because
$2\cdot2^n=2^{n+1}>2^{n+1}-1$), we get
$\mathrm{OddSum}(M)=1/2<c(n)$. $\blacksquare$

This is a direct one-step application of an already-certified lemma — no
new casework was actually needed (the round-3 outline's proposed tie/merge
case-split turns out to be unnecessary because the Doubling Lemma already
handles arbitrary multiplicities within $R$). It closes the entire
slack-budget regime $k\le n$, unconditionally, for every $n\ge0$ and every
such partition — not just LB's geometric one.

**Consequence.** The remaining open upper-bound target is exactly: for
every $n\ge1$ and every sorted $p_1\ge\cdots\ge p_{n+1}>0$ summing to $1$
(full budget $k=n+1$), XY has a $\le n$-cut response forcing
$\mathrm{OddSum}\le c(n)$. Call this statement $T(n)$.

### Lemma S (Subadditivity of OddSum)

**Statement.** For any two finite multisets $A,B$ of positive reals,
$\mathrm{OddSum}(A\cup B)\le\mathrm{OddSum}(A)+\mathrm{OddSum}(B)$.
(Equivalently, by conservation $\mathrm{OddSum}+\mathrm{EvenSum}=
\mathrm{sum}$, this is the same as
$\mathrm{EvenSum}(A\cup B)\ge\mathrm{EvenSum}(A)+\mathrm{EvenSum}(B)$ — but
note this is an **unconditional, unrestricted** statement, structurally
different from the previously-**disproven** Lemma X′
($\mathrm{EvenSum}(S')\ge T'/2\Rightarrow\mathrm{EvenSum}(A'\cup S')\ge T'$),
which was a *conditional threshold* claim on an *arbitrary* extra set $A'$.
Lemma S makes no such conditional/threshold hypothesis; it is verified
below by a direct, unconditional induction, and separately confirmed
numerically over $2\times10^5$ random trials with zero violation beyond
floating-point noise ($<10^{-14}$).)

**Proof.** Write $f(X):=\mathrm{OddSum}(X)$, $g(X):=\mathrm{EvenSum}(X)=
\mathrm{sum}(X)-f(X)$, for a finite multiset $X$ of positive reals sorted
descending $x_1\ge\cdots\ge x_m$: $f(X)=\sum_{i\text{ odd}}x_i$,
$g(X)=\sum_{i\text{ even}}x_i$.

*Removal identity.* For nonempty $X$, let $Y:=X\setminus\{x_1\}$ (remove
one copy of the maximum, itself sorted descending as $x_2,\dots,x_m$). Then
$Y$'s own rank $j$ (for $j=1,\dots,m-1$) is $x_{j+1}$, i.e. $Y$'s rank $j$
corresponds to $X$'s rank $j+1$. So $Y$'s odd ranks ($j=1,3,5,\dots$)
correspond to $X$'s ranks $2,4,6,\dots$ (even), giving
$$f(Y)=\sum_{j\text{ odd}}x_{j+1}=\sum_{i\text{ even}}x_i=g(X).$$
So: **$g(X)=f(X\setminus\{\max X\})$**, for every nonempty $X$ (well-defined
regardless of tie-breaking among equal maxima, since $\mathrm{OddSum}$ of a
multiset does not depend on how ties are broken — proved already inside the
Doubling Lemma's Claim: a block of $k$ mutually-equal elements occupying a
fixed range of consecutive ranks contributes a fixed value to
$\mathrm{OddSum}$ depending only on the range, not on which specific copy
sits where within it).

*Induction.* We prove $f(A\cup B)\le f(A)+f(B)$ by strong induction on
$m:=|A|+|B|$ (number of elements, counted with multiplicity).

- *Base case $m=0$:* $A=B=\emptyset$, both sides $0$.
- *Base case (either empty):* if $B=\emptyset$, $f(A\cup B)=f(A)=f(A)+f(B)$
  (equality); symmetric if $A=\emptyset$.
- *Inductive step ($A,B$ both nonempty):* let $x^*:=\max(A\cup B)$
  (any one copy, if the max value has multiple occurrences — pick a
  specific copy; by the tie-invariance noted above this choice does not
  affect any of the sums below). By symmetry of the statement in $A,B$,
  assume WLOG $x^*\in A$ (i.e. $x^*$ is a copy of the maximum lying in $A$;
  since $A\cup B$'s max value must occur in $A$ or in $B$, this is
  exhaustive up to the symmetric case). Then $x^*=\max(A)$ too, since $x^*$
  is $\ge$ every element of $A\cup B\supseteq A$. Let $A':=A\setminus\{x^*\}$.
  By the removal identity applied to $A\cup B$ (whose max is $x^*$):
  $$g(A\cup B)=f\big((A\cup B)\setminus\{x^*\}\big)=f(A'\cup B).$$
  By the removal identity applied to $A$ (whose max is also $x^*$):
  $$g(A)=f(A\setminus\{x^*\})=f(A').$$
  Then:
  $$f(A\cup B)=x^*+g(A\cup B)=x^*+f(A'\cup B),\qquad
  f(A)=x^*+g(A)=x^*+f(A').$$
  So $f(A\cup B)\le f(A)+f(B)$ is equivalent to
  $x^*+f(A'\cup B)\le x^*+f(A')+f(B)$, i.e. to
  $$f(A'\cup B)\le f(A')+f(B).$$
  This is the identical statement with $A$ replaced by $A'$ (one element
  smaller), so $|A'|+|B|=m-1$. By the strong induction hypothesis (which
  covers all pairs of multisets with total size $<m$, including the case
  where $A'$ is empty, already handled as a base case), this holds. $\blacksquare$

**Independent numerical verification.** $2\times10^5$ random trials
(uniform reals, multiset sizes $1$–$5$ each): worst observed
$f(A\cup B)-f(A)-f(B)=7\times10^{-15}$ (floating-point noise; the true
value is $\le0$ always, consistent with equality being attained in some
cases, e.g. singleton $A$).

### Theorem 4 (General Insertion Lemma — strengthens Theorem 2)

**Statement.** For any finite multiset $R$ of positive reals with
$\mathrm{sum}(R)=S$ and any real $\ell>0$,
$$\mathrm{OddSum}(R\cup R\cup\{\ell\})=S+\ell,$$
with **no relation required between $\ell$ and the elements of $R$** (this
drops the hypothesis $p_1\ge S$, i.e. $\ell\le$ something, that Theorem 2
needed).

**Proof.** Identical case analysis to Theorem 2's proof
(`lemmas/doubling-lemma-and-generalized-duplicate-the-rest.md`, Case (a)/(b)
for $\ell$ coinciding or not with a distinct value of $R$): that proof
computed the rank of $\ell$ (or of the merged odd-length block containing
it) purely from parity/counting arguments — "the number of $R\cup R$
elements exceeding $\ell$ is even, hence $\ell$'s own rank
(or the start of its merged block) is odd" — and at no point used any
inequality between $\ell$ and $\max(R)$ or $\min(R)$; the argument is
valid regardless of where $\ell$ falls among $R$'s values, including above
$\max(R)$, below $\min(R)$, or anywhere in between. Re-reading that proof
confirms both cases are stated and proved for *arbitrary* $\ell>0$, not
merely $\ell=p_1-S\ge0$ with $p_1\ge S$; the extra hypothesis in Theorem 2
was used only to guarantee $\ell\ge0$ (needed for $\ell$ to be a valid,
non-negative fragment length when the specific application was "split
$p_1$"), not anywhere inside the block-counting argument itself. Hence the
identity $\mathrm{OddSum}(R\cup R\cup\{\ell\})=S+\ell$ holds for every
$\ell>0$ unconditionally. $\blacksquare$

**Independent numerical verification.** $5\times10^4$ random trials ($R$ of
size $1$–$5$, $\ell$ unconstrained relative to $R$): max error
$3.6\times10^{-15}$ (floating-point noise).

### Corollary (new closed sub-case: smallest piece small)

Take $R=(p_1/2,\dots,p_n/2)$ (bisecting the top $n$ pieces of a $k=n+1$
partition, $n$ cuts — full budget) and $\ell:=p_{n+1}$ (the smallest piece,
left untouched). By Theorem 4,
$$\mathrm{OddSum}=\mathrm{sum}(R)+p_{n+1}=\frac{1-p_{n+1}}{2}+p_{n+1}
=\frac12+\frac{p_{n+1}}2.$$
This is $\le c(n)$ exactly when $p_{n+1}\le 2c(n)-1=\dfrac1{2^{n+1}-1}$.
(Among the $n+1$ choices of *which* single piece to leave unbisected, this
is optimal: leaving piece $p_m$ unbisected gives $\tfrac12+\tfrac{p_m}2$ by
the identical computation, minimized by taking $p_m$ as small as possible,
i.e. $m=n+1$.) This **unconditionally** closes the sub-case
$p_{n+1}\le1/(2^{n+1}-1)$ of $T(n)$, for every $n\ge1$ and every such
partition. (The symmetric construction — bisect the tail, leave $p_1$
untouched — gives $\mathrm{OddSum}=\tfrac{1+p_1}2\le c(n)\iff
p_1\le1/(2^{n+1}-1)$; but since $p_1\ge1/(n+1)$ always (pigeonhole, as
$p_1$ is the max of $n+1$ positive summands) and $1/(n+1)>1/(2^{n+1}-1)$
for every $n\ge1$ — proved by induction: true at $n=1$ ($2<3$), and if
$n+1<2^{n+1}-1$ then $n+2<2(n+1)<2(2^{n+1}-1)+1=2^{n+2}-1$ — this symmetric
version's hypothesis is **never satisfiable** for $n\ge1$, i.e. it closes
an *empty* sub-case. We record this only to note it honestly rather than
silently drop a dead branch: the useful direction is "leave the smallest,"
not "leave the largest.")

### Theorem 5 (conditional reduction: $p_1\ge c(n)$ closed given $T(n-1)$)

**Statement.** Fix $n\ge1$ and assume $T(n-1)$ holds (i.e. for every sorted
$q_1\ge\cdots\ge q_n>0$ summing to $1$, XY has a $\le(n-1)$-cut response
achieving $\mathrm{OddSum}\le c(n-1)$). Then for every sorted
$p_1\ge\cdots\ge p_{n+1}>0$ summing to $1$ with $p_1\ge c(n)$, XY has a
$\le n$-cut response achieving $\mathrm{OddSum}\le c(n)$.

**Proof.** Let $R:=(p_2,\dots,p_{n+1})$, $S:=1-p_1=\mathrm{sum}(R)$ ($S>0$
since $n\ge1$ means $R$ nonempty). If $S=0$ this is vacuous ($n+1$ pieces
all positive forces $S>0$), so $S>0$. Normalize $\tilde R:=R/S$ (divide
every element by $S$); this is a sorted tuple of $n$ positive reals summing
to $1$, so $T(n-1)$ applies: XY has a $\le(n-1)$-cut response on $\tilde R$
achieving $\mathrm{OddSum}(\tilde T)\le c(n-1)$ for the resulting multiset
$\tilde T$. Since $\mathrm{OddSum}$ (as a function of a tuple of ranked
values) is **scale-invariant up to the same scalar** — multiplying every
element of a multiset by a fixed positive constant $S$ multiplies
$\mathrm{OddSum}$ by $S$, because the sort order and hence which elements
occupy which ranks is unaffected by a uniform positive rescaling, and
$\mathrm{OddSum}$ is a fixed subset-sum of the (rescaled) elements — the
identical sequence of cuts applied to $R=S\cdot\tilde R$ instead (i.e.
"scale up the whole strategy by $S$") produces $T:=S\cdot\tilde T$ with
$$\mathrm{OddSum}(T)=S\cdot\mathrm{OddSum}(\tilde T)\le S\cdot c(n-1).$$
This uses $\le n-1$ cuts on $R$.

XY's full response: bisect $p_1\to(p_1/2,p_1/2)$ (1 cut) **and** apply the
above response to $R$ ($\le n-1$ cuts); total $\le n$ cuts, within budget.
Let $A:=\{p_1/2,p_1/2\}$ ($f(A)=p_1/2$, a two-element multiset, direct from
the definition: sorted $(p_1/2,p_1/2)$, rank $1$ (odd) contributes
$p_1/2$). The resulting multiset is $M=A\cup T$. By Lemma S:
$$\mathrm{OddSum}(M)\le f(A)+f(T)\le \frac{p_1}2+S\cdot c(n-1)
=\frac{p_1}2+(1-p_1)c(n-1)=:\varphi(p_1).$$

$\varphi$ is affine in $p_1$ with slope $\tfrac12-c(n-1)$. Since
$c(n-1)=2^{n-1}/(2^n-1)>1/2$ for every $n\ge1$ (as $2\cdot2^{n-1}=2^n>2^n-1$),
this slope is **strictly negative**, so $\varphi$ is strictly decreasing.

*Key algebraic identity: $\varphi(c(n))=c(n)$.* Compute directly (exact
rational arithmetic, also machine-verified above):
$$\varphi(c(n))=c(n-1)+c(n)\Big(\tfrac12-c(n-1)\Big)
=c(n-1)\big(1-c(n)\big)+\tfrac{c(n)}2.$$
Now $1-c(n)=1-\dfrac{2^n}{2^{n+1}-1}=\dfrac{2^n-1}{2^{n+1}-1}$, so
$$c(n-1)(1-c(n))=\frac{2^{n-1}}{2^n-1}\cdot\frac{2^n-1}{2^{n+1}-1}
=\frac{2^{n-1}}{2^{n+1}-1},$$
(the factor $2^n-1$ cancels exactly), and
$$\frac{c(n)}2=\frac{2^n}{2(2^{n+1}-1)}=\frac{2^{n-1}}{2^{n+1}-1}.$$
Summing: $\varphi(c(n))=\dfrac{2^{n-1}}{2^{n+1}-1}+\dfrac{2^{n-1}}{2^{n+1}-1}
=\dfrac{2^n}{2^{n+1}-1}=c(n)$. $\checkmark$

Since $\varphi$ is (strictly) decreasing and $\varphi(c(n))=c(n)$: for every
$p_1\ge c(n)$, $\varphi(p_1)\le\varphi(c(n))=c(n)$. Hence
$\mathrm{OddSum}(M)\le\varphi(p_1)\le c(n)$. $\blacksquare$

**Important honesty note.** This theorem is **conditional** on $T(n-1)$
holding in full (for *every* partition of $n$ pieces, including whatever
sub-case of $T(n-1)$ is itself still open) — it is a genuine inductive
*step*, not a standalone unconditional closure. Since $T(n-1)$ has the
identical structure of open sub-case as $T(n)$ (see below), this does not
by itself prove $T(n)$ for $p_1\ge c(n)$ unconditionally; it reduces "$T(n)$
restricted to $p_1\ge c(n)$" to "$T(n-1)$ in full," which is exactly as
strong an assumption as what we are trying to prove one level down. This is
still valuable: it shows that **if** the open gap below is closed at every
level by strong induction, the $p_1\ge c(n)$ regime requires no further
separate argument.

**Cross-check (why "bisect $p_1$" alone is not enough without recursing on
the tail).** At $p_1=1/2$, $n=1$: $\varphi(1/2)=c(0)+ (1/2)(1/2-c(0)) =
1+(1/2)(1/2-1)=1-1/4=3/4$, matching this file's round-1/2 documented
counterexample exactly (bisecting $p_1=1/2$ alone, with the tail
untouched, gives $\mathrm{OddSum}=0.75>c(1)=2/3$) — confirming the formula
correctly reproduces this known dead end (Theorem 5 does *not* apply at
$p_1=1/2<c(1)$; it only claims the bound for $p_1\ge c(n)$, where
$\varphi$'s decreasing behavior makes the bound tight exactly at the
boundary and better beyond it).

### Combined regime coverage and the precisely-narrowed open gap

At every level $n$ of a strong induction on $n$ (with base case $n=0$:
$T(0)$ trivial, single piece, $0$ cuts, $\mathrm{OddSum}=1=c(0)$;
$n=1$: $T(1)$ already **fully proved in both directions**, round 1), the
inductive step for $T(n)$ (given $T(n-1)$ in full) now has the following
status:

1. $k\le n$ (slack budget): **closed unconditionally**, all $n$ (Theorem 3).
2. $k=n+1$, $1/2\le p_1\le c(n)$: **closed unconditionally**, all $n$
   (Theorem 2, round 2, imported).
3. $k=n+1$, $p_1\ge c(n)$: **closed conditional on $T(n-1)$** (Theorem 5,
   this round).
4. $k=n+1$, $p_{n+1}\le1/(2^{n+1}-1)$: **closed unconditionally**, all $n$
   (Corollary to Theorem 4, this round) — note this can overlap with case 2
   or 3 (e.g. LB's own geometric partition has $p_{n+1}=1/(2^{n+1}-1)$
   exactly, on this boundary, and also $p_1=c(n)$, on the boundary of case
   3 — consistent, not contradictory, since both give the same value
   $c(n)$ there).
5. **Remaining open (every level, honestly unresolved):**
   $$k=n+1,\quad p_1<1/2\ \text{ and }\ p_{n+1}>\frac1{2^{n+1}-1}.$$
   This is the "genuinely balanced" regime: no piece so large that
   Theorem 2/5 apply, and no piece so small that the Corollary applies. The
   round-2 worked near-uniform example $(0.336,0.333,0.331)$ at $n=2$
   falls exactly here ($p_1=0.336<0.5$, $p_3=0.331>1/7\approx0.143$), and
   is known (this file, round 2, corrected note) to be solvable by an
   ad-hoc single bisection of $p_1$ for that *specific* instance, but no
   general rule covering this whole regime — conditional on IH or not —
   was found or proved this round. This is a **materially smaller** open
   region than last round's blanket "$p_1<1/2$" (which is now split into a
   closed piece, case 4, and this remaining piece), but it is still open,
   and is reported honestly as such rather than papered over.

### Theorem 6 (Suffix-Match Insertion Lemma) — round 4

**Motivation.** In the balanced regime ($p_1<S$), $\ell:=p_1-S$ is
negative, so Theorem 2/4's construction (duplicate *all* of $R$) is
unavailable — there is no way to give $p_1$ enough fragments to match every
element of $R$ plus a nonnegative leftover. The natural relaxation: match
only the smallest $t$ elements of $R$ (a free integer parameter XY
chooses, $0\le t\le n$), and let the leftover fragment absorb whatever of
$p_1$ remains.

**Setup and statement.** Fix a sorted tuple $p_1\ge p_2\ge\cdots\ge
p_{n+1}>0$ summing to $1$, generic in the sense that the tail
$R:=(p_2,\dots,p_{n+1})$ has **pairwise distinct** values (this holds for
every partition off a measure-zero set; the tied case is handled by the
continuity remark at the end of this theorem). Sort $R$ ascending as
$w_1<w_2<\cdots<w_n$. Fix $t\in\{0,1,\dots,n\}$ with
$\sum_{i=1}^t w_i\le p_1$ (a necessary feasibility condition), and set
$$R_t:=(w_1,\dots,w_t),\qquad U:=(w_{t+1},\dots,w_n)\ (\text{the untouched,
larger values}),\qquad \ell:=p_1-\sum_{i=1}^t w_i\ge0.$$
XY's move: replace $p_1$ by the $t+1$ (or $t$, if $\ell=0$) parts
$R_t\cup\{\ell\}$ — this uses $t$ cuts if $\ell>0$, $t-1$ cuts if $\ell=0$
(and $t\ge1$; if $t=0,\ell=p_1$ this is $0$ cuts, i.e. "do nothing" to
$p_1$). The resulting multiset is $M:=R\cup R_t\cup\{\ell\}$ (dropping the
singleton if $\ell=0$).

Write $U$ in descending order $u_1>u_2>\cdots>u_{n-t}$ (so $u_j=w_{n-j+1}$),
and let $A:=\#\{j: u_j>\ell\}\in\{0,\dots,n-t\}$ (well-defined since, in the
generic case treated first, $\ell$ does not equal any $u_j$).

**Claim (exact formula).** In the generic case (no value of $R$ equals
$\ell$):
$$\mathrm{OddSum}(M)=\underbrace{\sum_{\substack{1\le j\le A\\ j\text{
odd}}}u_j}_{\text{top part, above }\ell}
\;+\;\underbrace{[A\text{ even}]\cdot\ell}_{\ell\text{'s own contribution}}
\;+\;\underbrace{\sum_{\substack{A<j\le n-t\\ j\text{ even}}}u_j}_{\text{bottom
part, below }\ell}\;+\;\sum_{i=1}^t w_i.$$

**Proof.** Every element of $R_t$ is a value $w_i$ with $i\le t$, hence
$w_i\le w_t<w_{t+1}\le$ every element of $U$: so $U$ and $R_t$ occupy
disjoint, non-interleaving value ranges, with $U$ entirely above $R_t$.
Consequently $M$'s sorted order (ignoring $\ell$ for a moment) is exactly:
$U$ descending ($u_1,\dots,u_{n-t}$), followed by the **doubled block**
formed by $R\text{'s original copies of }w_1,\dots,w_t$ together with the
new copies from $R_t$ — i.e. each value $w_i$ ($i\le t$) now occurs exactly
twice in $R\cup R_t$ (once from $R$, once from the matching fragment),
giving a block of $2t$ elements ($w_t,w_t,w_{t-1},w_{t-1},\dots,w_1,w_1$
descending).

*Doubled block, any starting rank.* By the Claim proved inside the Doubling
Lemma (Theorem 1 above): an interval of $2c$ consecutive integer ranks,
starting at **any** integer, contains exactly $c$ odd and $c$ even ranks
(pair $e,e+1$; $e+2,e+3$; etc., each pair one odd one even, regardless of
the parity of the starting rank $e$). Applying this to each of the $t$
sub-blocks of size $2$ (or directly to the whole $2t$-block, since it is a
union of consecutive-rank intervals of even total length starting anywhere)
shows that, **regardless of where this doubled block sits inside $M$** (in
particular regardless of where $\ell$ is inserted relative to it), the
first-mover receives exactly one copy of each doubled value, contributing
$\sum_{i=1}^t w_i$ to $\mathrm{OddSum}(M)$. This is the last term of the
formula, and it is now fully accounted for; the rest of the proof concerns
only $U\cup\{\ell\}$ (an ordinary $(n-t+1)$-element sequence, disjoint in
rank-contiguity from the doubled block since $U>$ all doubled values).

*Placing $\ell$ among $U$.* Since $M$ restricted to $U\cup\{\ell\}$ occupies
the **top** $n-t+1$ ranks of $M$ (as $U$'s values all exceed the doubled
block's values, and $\ell\ge0$ — if $\ell=0$ it is dropped, handled as a
separate, simpler sub-case below), the ranks of $U\cup\{\ell\}$ within $M$
are exactly $1,\dots,n-t+1$, in the same relative order as within
$U\cup\{\ell\}$ alone. So it suffices to compute $\mathrm{OddSum}$ of the
$(n-t+1)$-element sequence $U\cup\{\ell\}$ directly (its own internal ranks
$1,\dots,n-t+1$ coincide with its ranks in $M$).

Since $\ell$ is not tied with any $u_j$ (generic case), and $u_1>\cdots>
u_{n-t}$, the elements exceeding $\ell$ are exactly $u_1,\dots,u_A$ (a
prefix, by sortedness), occupying ranks $1,\dots,A$; $\ell$ occupies rank
$A+1$; and $u_{A+1},\dots,u_{n-t}$ occupy ranks $A+2,\dots,n-t+1$
respectively (i.e. $u_j$, for $j>A$, sits at rank $j+1$).

- Ranks $1,\dots,A$ ($u_1,\dots,u_A$): rank $j$ is odd iff $j$ is odd, so
  these contribute $\sum_{j\text{ odd},\,j\le A}u_j$ — the first term.
- Rank $A+1$ ($\ell$): odd iff $A+1$ is odd iff $A$ is even — the second
  term, $[A\text{ even}]\cdot\ell$.
- Ranks $A+2,\dots,n-t+1$ ($u_{A+1},\dots,u_{n-t}$, i.e. $u_j$ at rank
  $j+1$ for $j=A+1,\dots,n-t$): rank $j+1$ is odd iff $j$ is even, so these
  contribute $\sum_{j\text{ even},\,A<j\le n-t}u_j$ — the third term.

Summing all four terms gives the claimed formula. $\blacksquare$

**Sub-case $\ell=0$.** Then $M=R\cup R_t$ exactly, and $U$ occupies the top
$n-t$ ranks of $M$ unshifted (no insertion), while the doubled block
contributes $\sum_{i=1}^tw_i$ exactly as above. So
$\mathrm{OddSum}(M)=\mathrm{OddSum}(U)+\sum_{i=1}^tw_i$ where
$\mathrm{OddSum}(U)=\sum_{j\text{ odd}}u_j$ over $U$'s own ranks
$1,\dots,n-t$ — this is exactly the general formula's value at "$A=n-t$"
(i.e. as if $\ell$ were smaller than every element, contributing $0$ via
the vanishing third sum and correctly matching the second term $[A\text{
even}]\cdot 0=0$ regardless of parity), so no separate bookkeeping is
needed; the formula is continuous across $\ell\to0^+$.

**Sub-case $\ell$ ties a value of $R_t$ (i.e. $\ell=w_i$ for some $i\le t$).**
Then $\ell\le w_t<$ every element of $U$, so $\ell$ inserts entirely below
$U$, giving $A=0$ (no $U$ element exceeds $\ell$, since $\ell$ is smaller
than all of them). The doubled block, together with $\ell$, now has one
value ($w_i$) occurring with multiplicity $3$ (odd) instead of $2$: this is
structurally identical to Theorem 4's Case (b) (a value's total copies
become odd), and by that theorem's argument (an odd-length block starting
at an odd rank has one more odd-rank slot than even-rank slot, so the
first-mover gets one extra copy) the doubled-block-plus-$\ell$ contributes
$\sum_{i=1}^tw_i+\ell$ instead of just $\sum w_i$. Combined with $U$'s own
unshifted contribution ($\ell$ sits below all of $U$, so $U$'s internal
ranks $1,\dots,n-t$ are unaffected): $\mathrm{OddSum}(M)=
\mathrm{OddSum}(U)+\sum_{i=1}^tw_i+\ell$, matching the general formula's
value at $A=0$ (the top-part sum is empty, the $\ell$-term is $\ell$ since
$A=0$ is even, and the bottom-part sum is $\mathrm{OddSum}(U)$ since $A=0$
makes the "even $j>A$" condition range over all $j=1,\dots,n-t$, i.e.
exactly $U$'s own even-indexed-from-1 entries — wait, this requires care:
the general formula's third term at $A=0$ is $\sum_{j\text{ even},0<j\le
n-t}u_j$, i.e. $U$'s *even*-indexed entries, not odd — but here we need
$U$'s *odd*-indexed entries (its own $\mathrm{OddSum}$). This apparent
discrepancy is because in this sub-case $\ell$ sits at the very *bottom*
(rank $n-t+1$, not shifting any $U$ element's own rank at all, so $U$
keeps its **own internal parity**, i.e. contributes $\mathrm{OddSum}(U)$
using $U$'s own ranks $1,\dots,n-t$ unchanged) — whereas the general
formula's derivation assumed $\ell$ occupies rank $A+1$ and shifts
everything below it by exactly $+1$; at $A=0$ that shift still applies (all
of $U$ is "below" $\ell$ in the generic-formula sense, each $u_j$ moving
from rank $j$ to $j+1$). The resolution: **in this tie sub-case, $\ell$ is
not inserted as a new rank among $U\cup\{\ell\}$ at all** — it is absorbed
into the doubled block instead (its final position in $M$ is determined by
its tie with $w_i$, not by comparison with $U$), so this sub-case is
genuinely different from the generic-$A=0$ limit and must be stated
separately, as done above: $\mathrm{OddSum}(M)=\mathrm{OddSum}(U)+
\sum_{i=1}^tw_i+\ell$ (using $U$'s *own*, unshifted internal parity).**

**Sub-case $\ell$ ties a value of $U$ (i.e. $\ell=u_{i_0}$ for some
$1\le i_0\le n-t$).** Then $\{u_{i_0},\ell\}$ form a tied pair of two equal
values at consecutive ranks — by the tie-invariance fact (used already
inside the Doubling Lemma and Lemma S), a tied pair of two equal elements
at a fixed pair of consecutive ranks contributes exactly one copy of the
value to $\mathrm{OddSum}$, regardless of which physical copy is
"assigned" the odd rank. Elements $u_1,\dots,u_{i_0-1}$ (strictly above
$u_{i_0}$) keep their own original ranks $1,\dots,i_0-1$ (unaffected by
$\ell$'s insertion exactly at $u_{i_0}$'s level); the tied pair occupies
ranks $i_0,i_0+1$ (in either order) contributing $u_{i_0}$; and elements
$u_{i_0+1},\dots,u_{n-t}$ (originally at ranks $i_0+1,\dots,n-t$) are each
shifted by $+2$ (two elements — $\ell$ and one extra copy from the tied
pair being inserted — landed above them, wait: precisely, exactly $2$ new
elements total are inserted relative to $U$ alone: $\ell$ itself, which
combined with $u_{i_0}$ occupies $2$ ranks where $U$ alone had $1$), so
each such $u_j$ ($j>i_0$) moves from rank $j$ to rank $j+1$: parity
**unchanged**. So the contribution from $u_1,\dots,u_{i_0-1}$ and from
$u_{i_0+1},\dots,u_{n-t}$ is exactly $U$'s own $\mathrm{OddSum}$ restricted
to those two sub-ranges using $U$'s own original parities, plus $u_{i_0}$
itself (from the tied pair) — i.e.
$$\mathrm{OddSum}(M)=\Big(\sum_{\substack{j<i_0\\ j\text{ odd}}}u_j\Big)
+u_{i_0}+\Big(\sum_{\substack{j>i_0\\ j\text{ odd}}}u_j\Big)+\sum_{i=1}^tw_i
=\mathrm{OddSum}(U)+\sum_{i=1}^tw_i.$$
(The middle term $u_{i_0}$ combines with the two flanking odd-indexed sums
using $U$'s *own* ranks, and since $i_0$ itself is included as "$+u_{i_0}$"
unconditionally, this reduces to *exactly* $U$'s own $\mathrm{OddSum}$ over
all of $U$, plus the doubled-block term — i.e., in this sub-case,
$\ell$'s tie with $U$ contributes nothing beyond what $U$ alone would have
contributed at that rank: a completely clean, parity-preserving insertion.)

All four sub-cases (generic, $\ell=0$, tie-with-$R_t$, tie-with-$U$) are
exhaustive (every real $\ell\ge0$ either is $0$, equals a value in $R_t$,
equals a value in $U$, or equals none of these — and $R_t,U$ are disjoint
in value since $R$'s values are pairwise distinct by the genericity
assumption), giving a complete, case-exhaustive proof of Theorem 6 for
every generic tail $R$. $\blacksquare$

**Reduction to $R$ with repeated values.** If $R$ has tied values, the
theorem's conclusion (a specific numeric value of $\mathrm{OddSum}(M)$ for
a specific choice of $t$ and specific matching) is a continuous function of
the underlying $(p_1,\dots,p_{n+1})\in\Delta^n$ (the standard simplex): for
fixed combinatorial choice of $t$ and of *which* $t$ smallest indices are
matched, $\mathrm{OddSum}(M)$ is a fixed, explicit sum of order statistics
of an explicit affine (indeed linear, once $t$ is fixed) function of
$(p_1,\dots,p_{n+1})$, and order statistics are continuous (indeed
$1$-Lipschitz) functions of their argument tuple. The formula proved above
for the generic (all-distinct) case, being continuous in the $p_i$ on the
generic dense open subset of $\Delta^n$ where it was derived, extends by
continuity to its closure, i.e. to every partition including those with
tied tail values — the same closure argument already used (and flagged
explicitly) for the compactness/attained-maximum step of the "pruning
lemma" discussion above. No new case-analysis is required for tied $R$.

**Independent numerical verification.** All three case-branches
(generic-$\ell$/Case (a), $\ell$ ties $R_t$/Case (b), $\ell$ ties
$U$/Case (c)) checked by direct computation against brute-force
$\mathrm{OddSum}$: $3{,}532$ random trials for the generic + $\ell=0$
branches (random $n\in\{1,\dots,5\}$, random $t\in\{0,\dots,n\}$, random
$R,p_1$), **zero mismatches**; $2{,}000$ further trials specifically
targeting the tie-with-$U$ sub-case (forced $\ell$ to exactly equal a
randomly chosen $U$-value), **zero mismatches**. Boundary checks: $t=0$
reduces exactly to "do nothing to $p_1$" (verified algebraically above,
recovering the original partition's own $\mathrm{OddSum}$); $t=n$ (with
$U=\varnothing$, so $A=0$ trivially) reduces exactly to Theorem 2/4's
identity $\mathrm{OddSum}=\mathrm{sum}(R)+\ell=S+\ell=p_1$ (verified
algebraically above).

**Optimization test — negative result.** Theorem 6 gives XY, for every
$t\in\{0,\dots,n\}$ with $\sum_{i\le t}w_i\le p_1$, an *exact* value of
$\mathrm{OddSum}$ for the resulting response; XY can choose the best $t$.
This was tested numerically against the target $c(n)$ over $1{,}500$–
$3{,}000$ partitions per $n$, sampled uniformly at random from the balanced
region ($p_1<1/2$, $p_{n+1}>1/(2^{n+1}-1)$, via rejection sampling from a
Dirichlet/exponential-ratio distribution) for $n=2,3,4,5$:

| $n$ | trials | fraction with $\min_t\mathrm{OddSum}(t)>c(n)$ | worst excess over $c(n)$ |
|---|---|---|---|
| 2 | 3000 | 43.5% | 0.0919 |
| 3 | 3000 | 77.8% | 0.1050 |
| 4 | 3000 | 89.8% | 0.1147 |
| 5 | 3000 | 96.7% | 0.1156 |

So **optimizing $t$ alone does not close the balanced region**; the
failure rate *worsens* as $n$ grows. A natural extension — after choosing
the best $t$, spend any leftover cut budget ($n-t$ or $n-t+1$ cuts)
greedily bisecting the currently-largest untouched element among $U$ and
$\ell$ — was also tested (same sampling, $1{,}500$ trials per $n$,
$n=2,\dots,5$): failure rates remain high ($79.7\%$, $81.5\%$, $87.9\%$,
$94.5\%$ respectively), with comparable worst-case excess ($\approx0.05$–
$0.06$). **Conclusion (honest, not papered over): the Suffix-Match
construction, whether or not augmented by a greedy leftover-bisection
cleanup step, is insufficient to close the balanced region.** This
narrows what future work on this approach (or others facing the same open
region) should try: a construction that commits cut budget to **multiple**
tail pieces from the outset (not just $p_1$, and not a greedy afterthought
applied only after $p_1$'s allocation is fixed) is needed. This matches,
independently, the round-2/round-3 diagnosis in the $p_1>c(n)$ regime
(worked example there also required cutting *two* pieces, $p_1$ and $p_2$,
simultaneously, not $p_1$ alone) — the balanced region appears to demand
the same kind of coordinated multi-piece construction, for which no
general closed-form rule has yet been found.

### Theorem 7 (Anchor-Merge Lemma) — round 5

**Statement.** Let $p_1\ge p_2\ge\cdots\ge p_{n+1}>0$ sum to $1$ ($n\ge1$).
Fix any two indices $i<j$ (so $p_i\ge p_j$ in the sorted order), and let
$\ell:=p_i-p_j\ge0$. XY's move: split $p_i$ into the two fragments
$(\ell,\,p_j)$ (**one** cut), leave $p_j$ untouched, and bisect every other
piece $p_m$ ($m\ne i,j$) into $(p_m/2,p_m/2)$ (one cut each). This uses
exactly $1+(n+1-2)=n$ cuts, i.e. the full budget. Assume genericity: $\ell$
does not equal $p_j$ or any $p_m/2$ ($m\ne i,j$), and no two of the $p_m/2$
coincide with each other by accident of an unrelated tie (holds off a
measure-zero set; the tied case follows by the same continuity-closure
argument used for Theorem 6, since the formula below is continuous in
$(p_1,\dots,p_{n+1})$). Then the resulting multiset $M$ has
$$\mathrm{OddSum}(M)=\frac{1+p_i-p_j}{2}.$$

**Proof.** Group $M$ by value:
- Value $p_j$ occurs with multiplicity **2**: once as the untouched original
  piece, once as the fragment of $p_i$ tied to it.
- For each $m\ne i,j$, value $p_m/2$ occurs with multiplicity **2** (both
  halves of the bisected piece $p_m$).
- Value $\ell:=p_i-p_j$ occurs with multiplicity **1** (a singleton,
  generically distinct from every other value present, by hypothesis).

So every value in $M$ other than $\ell$ occurs with **even** multiplicity;
sorted descending, $M$ therefore decomposes into a disjoint union of
consecutive-rank blocks, one per distinct value, all of even length except
for exactly one block of length $1$ (the singleton $\ell$).

By the Claim proved inside the certified Doubling Lemma
(`lemmas/doubling-lemma-and-generalized-duplicate-the-rest.md`, Theorem 1):
*a block of even length, wherever it starts in the global sort order,
splits exactly half its copies to the first-mover.* This holds regardless
of what other blocks (of any length, including the odd singleton) surround
it, since the argument depends only on parity of consecutive integers
within the block's own rank interval. Applying this to the $p_j$-block
(length $2$) gives contribution $p_j$ to $\mathrm{OddSum}$; applying it to
each $p_m/2$-block (length $2$, $m\ne i,j$) gives contribution $p_m/2$.
Summing over all even blocks:
$$\text{(even-block total)}=p_j+\sum_{m\ne i,j}\frac{p_m}{2}
=p_j+\frac{1-p_i-p_j}{2}.$$
This total is **independent of where $\ell$ sits** among these blocks —
only the even blocks' own contributions matter, by the block-locality of
the Claim.

It remains to determine $\ell$'s own contribution (either $\ell$, if its
rank is odd, or $0$, if even). Let $E$ be the number of elements of $M$
(with multiplicity) strictly exceeding $\ell$; since $\ell$ is generically
untied with anything else, $M\setminus\{\ell\}$ is sorted into blocks each
lying entirely above or entirely below $\ell$'s value (a block of a single
fixed value cannot straddle $\ell$, since all its elements are literally
equal, so either $>\ell$ or $<\ell$). Hence $E$ equals the sum of the
lengths of exactly those blocks lying above $\ell$ — a sum of terms each
equal to $2$ (or, if two originally distinct blocks happen to coincide in
value and merge, a sum of even numbers, still even) — so $E$ is **always
even**, regardless of the specific value of $\ell$ or of the partition.
Consequently $\ell$ occupies rank $E+1$, which is **always odd**, so $\ell$
is claimed by the first-mover in full: contribution $\ell=p_i-p_j$.

Summing: $\mathrm{OddSum}(M)=p_j+\dfrac{1-p_i-p_j}{2}+(p_i-p_j)
=\dfrac{2p_j+1-p_i-p_j+2p_i-2p_j}{2}=\dfrac{1+p_i-p_j}{2}$. $\blacksquare$

**Independent numerical verification.** Checked by direct simulation
(sort-and-sum, not the formula) over $3{,}000$ random partitions with
$k\in\{3,\dots,8\}$ pieces, uniformly random valid pairs $(i,j)$: maximum
observed discrepancy between the formula and the brute-force computation
was $2.2\times10^{-16}$ (floating-point roundoff only).

**Corollary (new closed sub-case of the balanced region).** Applying
Theorem 7 with the pair $(i,i+1)$ that minimizes the consecutive gap
$g:=\min_{1\le i\le n}(p_i-p_{i+1})$ gives XY a response achieving
$$\mathrm{OddSum}=\frac{1+g}{2}\le c(n)\iff g\le 2c(n)-1=\frac1{2^{n+1}-1}.$$
(Minimizing $p_i-p_j$ over *all* valid pairs $i<j$, not just adjacent ones,
is achieved at an adjacent pair: for $i<j$, $p_i-p_j=\sum_{r=i}^{j-1}
(p_r-p_{r+1})$ is a sum of $\ge1$ nonnegative consecutive gaps, so it is
minimized, among pairs with a fixed $i$, by taking $j=i+1$ — a sum of one
term cannot exceed a sum of two or more nonnegative terms containing it;
ranging over $i$ then gives the global minimum $g$.) This **unconditionally
closes** the sub-case of the balanced region where some consecutive gap is
$\le1/(2^{n+1}-1)$, for every $n\ge1$ and every such partition — a new
regime, not covered by any previously-closed case (this sub-case can
genuinely intersect the balanced region: e.g. $n=2$,
$p=(0.35,0.345,0.305)$ has $p_1<1/2$, $p_3=0.305>1/7$, and gap
$p_1-p_2=0.005\le1/7\approx0.143$, so Theorem 7 applies and gives
$\mathrm{OddSum}=(1+0.005)/2=0.5025<4/7$).

**Numerically confirmed insufficiency of this tool alone.** Cross-checking
the exact equivalence "$g\le1/(2^{n+1}-1)$" against direct random sampling
of the balanced region (rejection sampling, Dirichlet-type, $3{,}000$
trials per $n$) shows this sub-case's coverage **shrinks as $n$ grows**:

| $n$ | balanced-region trials | fraction with small enough gap (Theorem 7 applies) |
|---|---|---|
| 2 | 2919/3000 | 97.3% |
| 3 | 2688/3000 | 89.6% |
| 4 | 2487/3000 | 82.9% |
| 5 | 2298/3000 | 76.6% |
| 6 | 2019/3000 | 67.3% |
| 10 | (separate run) | $\approx23\%$ |

So a residual "all consecutive gaps large" sub-case of the balanced region
remains **open** — genuinely, not just conjecturally, since these are
random balanced instances where Theorem 7 provably cannot reach $c(n)$
(its formula $\tfrac{1+g}2$ exceeds $c(n)$ whenever $g$ exceeds the
threshold, and $g$ is by definition the *best* Theorem-7 pair, so no choice
of $(i,j)$ in this family does better). This is consistent with, and
explains via a different (complementary) mechanism, the round-4 finding
that single-piece constructions centered on $p_1$ alone are insufficient:
Theorem 7 is a genuinely two-piece (merge) construction, yet even it alone
is not universal — it fails specifically on *spread-out* partitions (large
gaps everywhere), the opposite failure mode from the constructions that
fail on *dominant-$p_1$* partitions. This is itself useful diagnostic
content for future rounds: **the "small gap" and "dominant piece" failure
modes are complementary, suggesting the general closing construction must
combine an anchor-merge-type move (for close pairs) with a
suffix-match/shave-below-type move (for the dominant piece), chosen
adaptively per-instance** — matching the qualitative shape of the round-5
math-explorer's worked $n=3$ example (which used *both* a self-bisection
and two shave-below moves simultaneously, not just one merge).

**Free-form family: a strong but unproved lead.** A separate numerical
experiment (Nelder-Mead multi-restart optimization, not a proof) tested the
larger family "leave exactly one piece $p_{i^*}$ untouched; split every
other piece once, at an arbitrary point" (this strictly contains both the
`bisect-top-$j$` family and the Theorem 7 family as special cases, and can
realize the round-5 explorer's worked $n=3$ shave-below example as an
interior point). Optimizing jointly over $i^*$ and all $n$ split points:
**zero failures** were found over $40$ random balanced instances each at
$n=2,3,4$ (limited sample size due to the cost of nested global
optimization; not a large-scale sweep like the tables above). This is
consistent with — and a natural common generalization of — the
math-explorer's numeric finding that all observed optima have a
"tie-or-zero" structure (every fragment is $0$ or exactly tied with
another element). No closed-form recipe for *which* point $i^*$ and *which*
split values to use was extracted this round; this is flagged as the
concrete next target (a natural candidate: minimize, over choice of
$i^*$, an explicit formula generalizing Theorem 7's $\tfrac{1+g}2$ to
*multiple* simultaneous merges/shaves — attempted briefly this round for
two disjoint merges but not completed in the time available, since with
two singletons the "every non-singleton block is even, hence $E$ is even"
argument no longer directly applies and requires tracking the two
singletons' relative order explicitly).

### Theorem 8 (Two-Piece-Split Vertex Lemma) — round 6

**Statement.** Fix positive reals $q_1,\dots,q_r$ (the untouched pieces),
and two positive reals $T,T'$ (the two pieces to be split simultaneously,
$T\ne T'$ as distinct positions in LB's partition, though possibly equal in
value). For $2\le m\le n_1$, $2\le m'\le n_2$ (with $n_1+n_2\le n+2$, i.e.
the total cuts used, $(m-1)+(m'-1)$, stays $\le n$), define
$$f_{m,m'}(x_1,\dots,x_m,y_1,\dots,y_{m'}):=\mathrm{OddSum}\Bigl(\{q_1,\dots,q_r\}\cup\{x_1,\dots,x_m\}\cup\{y_1,\dots,y_{m'}\}\Bigr),$$
$$x_i>0,\ \textstyle\sum x_i=T,\qquad y_i>0,\ \textstyle\sum y_i=T'.$$
Let $\mathcal V$ be the finite set of vectors $(x,y)$ obtained, for each
valid $(m,m')$, each set partition $\{B_1,\dots,B_g\}$ of $\{1,\dots,m\}$
(for the $x$-block) and each set partition $\{C_1,\dots,C_h\}$ of
$\{1,\dots,m'\}$ (for the $y$-block), and each choice of one free block
among the $x$-blocks *and* one free block among the $y$-blocks, by
assigning every non-free $x$-block a value in $\{0\}\cup\{q_1,\dots,q_r\}$,
every non-free $y$-block a value in $\{0\}\cup\{q_1,\dots,q_r\}$, and
**additionally** allowing a non-free $x$-block to be pinned to a non-free
$y$-block's assigned free variable is not permitted (pins are only to the
*fixed* constants $q_1,\dots,q_r$ or to $0$ — cross-pinning $x$ against $y$
is handled below as a separate refinement), solving each free block's
common value from its own sum constraint ($\sum x_i=T$ resp.
$\sum y_i=T'$), keeping only vectors with all coordinates $\ge0$; **and**
further extending $\mathcal V$ by also allowing exactly one non-free
$x$-block to be pinned *equal to* one non-free $y$-block (a genuine
cross-tie between a fragment of $T$ and a fragment of $T'$), with the
shared pinned value itself then treated as one further unknown solved
jointly from both sum constraints if it is the last unresolved unknown, or
otherwise assigned a value in $\{0\}\cup\{q_1,\dots,q_r\}$ exactly as any
other non-free block. Then
$$\min_{\substack{x_i>0,\sum x_i=T\\ y_i>0,\sum y_i=T'}} f_{m,m'}(x,y) = \min_{(x,y)\in\mathcal V} f_{m,m'}(x,y),$$
attained at a vector in $\mathcal V$ with all coordinates strictly positive
(any minimizer with a zero coordinate reduces, by discarding that
coordinate, to a vector in the corresponding smaller-$(m,m')$ instance).

**Proof.** For fixed $(m,m')$, $f_{m,m'}$ is a function of $m+m'$ real
variables constrained to the product of two simplices
$\Delta_T\times\Delta_{T'}$ (each simplex $\{z\ge0,\sum z_i=T\}$), which is
itself a bounded polytope of dimension $(m-1)+(m'-1)$. Exactly as in the
Single-Piece-Split Vertex Lemma's proof, $f_{m,m'}$ is linear on each
region cut out by fixing the total (descending) sort order of the
$m+r+m'$ elements $\{q_j\}\cup\{x_i\}\cup\{y_i\}$ — an order constraint
between any two of these elements is a linear inequality in $(x,y)$ (since
the $q_j$ are fixed constants, and comparisons among $x_i,y_i$ or between
an $x_i$/$y_i$ and a $q_j$ are all linear). By Krein–Milman for polytopes
(as in the single-piece case), the minimum of a linear functional over the
intersection of $\Delta_T\times\Delta_{T'}$ with any such sort-order region
is attained at an extreme point of that region, and every extreme point of
$\Delta_T\times\Delta_{T'}$ (over all sort-order regions) has rank
$(m-1)+(m'-1)$ active linear constraints beyond nonnegativity, in addition
to the two sum-equality constraints (one for each simplex factor).

The active constraints decompose exactly as in the single-piece case,
**now tracked separately for the two simplex factors, plus a possible
cross-tie between them**: the active order-tightness constraints among
$\{x_1,\dots,x_m\}$ partition $\{1,\dots,m\}$ into blocks (forced equal by
chains of ties among themselves), using $m-g$ independent constraints for
$g$ such blocks; symmetrically for $\{y_1,\dots,y_{m'}\}$ into $h$ blocks
using $m'-h$ constraints. Reaching the required total rank
$(m-1)+(m'-1)$ (given the two sum-equalities already present, one per
factor) requires $(g-1)+(h-1)$ **further** active constraints pinning
blocks to values, **unless** one $x$-block and one $y$-block are tied to
each other directly (a cross-tie constraint), which — since it links a
degree of freedom in the $x$-factor to one in the $y$-factor — reduces the
required count of *value*-pinning constraints by exactly one (the
cross-tie itself supplies one unit of rank that would otherwise need to
come from a $\{0,q_j\}$-pin). Each remaining pin assigns its block a value
in $\{0\}\cup\{q_1,\dots,q_r\}$ (pinning to a fixed constant, exactly as
in the single-piece case — a block cannot be "pinned" to an unconstrained
free variable of the *other* factor without that being precisely the
cross-tie case already accounted for, since any equation relating an
$x$-block's value to a $y$-block's value other than direct equality would
not be a linear order-tightness constraint of the required form, as the
only linear relations available between two order-statistics variables
occurring in a strict total order are equality relations at ties). This
is exactly the two-index generalization of the single-piece construction
of $\mathcal V$ described above (with the added cross-tie refinement), and
every extreme point of every sort-order region of $\Delta_T\times
\Delta_{T'}$ arises this way (the counting argument is identical to the
single-piece case, applied to each factor and to the one possible
cross-link), so the two minima coincide. The zero-coordinate reduction is
identical to the single-piece case: discarding a length-$0$ fragment from
either $x$ or $y$ does not change any other element's value or global sort
position, hence not $\mathrm{OddSum}$, and yields exactly the smaller
$(m-1,m')$ or $(m,m'-1)$ instance's own vertex set. $\blacksquare$

**Independent numerical verification.** Applied to the general
$k$-Anchor-Merge construction below (Theorem 9/10) at several random
instances ($n=3,\dots,6$): in every case the construction's explicit
closed-form value coincides with a vertex of $\mathcal V$ found by direct
enumeration of the finite candidate set (specifically, the cross-tie-free
vertex where the two free blocks are pinned respectively to the two
anchors $q_{j_1},q_{j_2}$) — confirming the mechanical reduction is
consistent with, and recovers, the explicit constructions proved below.
Cross-checked against a Nelder–Mead continuous optimizer over the full
2-piece polytope on 30 random instances ($n=3,4,5$): agreement to within
$10^{-6}$ in every case.

### Theorem 9 (Singleton-Interleaving Lemma) — round 6

**Statement.** Let $M$ be a finite multiset of positive reals that
decomposes as $M=B\sqcup L$, where:
- $B$ (the "base") is itself a disjoint union of finitely many
  **even-length blocks**: groups of mutually equal elements, pairwise
  distinct in value across groups, each group occurring with an even
  multiplicity;
- $L=\{\ell_1,\dots,\ell_k\}$ ($k\ge0$) is a finite multiset of positive
  reals, **pairwise distinct**, and **each distinct from every value
  occurring in $B$** (genericity hypothesis; relaxed by continuity at the
  end).

Then, under the greedy alternating-claim game (first-mover receives the
odd ranks of $M$ sorted descending),
$$\mathrm{OddSum}(M)=\frac12\,\mathrm{sum}(B)+\mathrm{OddSum}(L),$$
where $\mathrm{OddSum}(L)$ is computed by sorting $L$ itself descending and
summing its own odd-ranked entries (i.e. $L$'s value under the identical
alternating-claim rule, treated as a fully independent, standalone
instance).

**Proof.** By the Claim proved inside the certified Doubling Lemma
(`lemmas/doubling-lemma-and-generalized-duplicate-the-rest.md`, Theorem 1):
an interval of consecutive integer ranks of even length, wherever it
starts in a global sort order, contains exactly half odd and half even
ranks. Each block of $B$ occupies a genuinely consecutive run of ranks in
$M$'s global sort (since all its elements are literally equal and, by the
genericity hypothesis, distinct from every value in $L$ and from every
other block's value, so no other element can be interposed inside it), and
this run has even length (the block's own even multiplicity). Hence, by
the Claim, each block of $B$ contributes exactly half its total value to
$\mathrm{OddSum}(M)$, **regardless of where it sits relative to the other
blocks and the elements of $L$** (the Claim's proof depends only on the
parity-symmetry of an interval of consecutive integers, not on what
precedes or follows it). Summing over all blocks of $B$: their total
contribution is $\tfrac12\,\mathrm{sum}(B)$.

It remains to show $L$'s elements contribute exactly $\mathrm{OddSum}(L)$
(computed in isolation). Sort $L$ descending as
$\ell_{(1)}>\ell_{(2)}>\cdots>\ell_{(k)}$ (strict, by pairwise distinctness).
For $t=1,\dots,k$, let $e_t$ denote the number of elements of $B$ (with
multiplicity) whose value lies strictly between $\ell_{(t-1)}$ and
$\ell_{(t)}$ (with the convention $\ell_{(0)}:=+\infty$, so $e_1$ counts
$B$-elements exceeding $\ell_{(1)}$). Since every element of $L$ is
distinct from every value in $B$, and $B$ decomposes into blocks each of a
single fixed value, **no block of $B$ can straddle any $\ell_{(t)}$**: each
block lies either entirely above or entirely below each threshold value
$\ell_{(t)}$ (all its elements being literally equal). Hence the
$B$-elements strictly between $\ell_{(t-1)}$ and $\ell_{(t)}$ form a union
of complete blocks, so $e_t$ is a sum of even block-lengths, hence **even**,
for every $t=1,\dots,k$ (including $t=1$, where $e_1$ is likewise a union
of complete blocks lying above $\ell_{(1)}$).

The global sort of $M$ places, in order: the $e_1$ elements of $B$ above
$\ell_{(1)}$, then $\ell_{(1)}$, then the $e_2$ elements of $B$ between
$\ell_{(1)}$ and $\ell_{(2)}$, then $\ell_{(2)}$, and so on. So the rank of
$\ell_{(t)}$ in $M$ is
$$\mathrm{rank}_M(\ell_{(t)}) = t+\sum_{s=1}^t e_s.$$
Since each $e_s$ is even, $\sum_{s=1}^t e_s$ is even, so
$\mathrm{rank}_M(\ell_{(t)})\equiv t\pmod 2$: $\ell_{(t)}$ occupies an odd
rank in $M$ **if and only if** $t$ is odd — exactly the same parity
$\ell_{(t)}$ would have as the $t$-th largest element of $L$ **on its own**
(standalone instance). Hence the first-mover claims from $L$ precisely the
set $\{\ell_{(t)}:t\text{ odd}\}$, whose sum is $\mathrm{OddSum}(L)$ by
definition. Summing the $B$-contribution and the $L$-contribution gives the
claimed identity. $\blacksquare$

**Relaxing genericity (ties).** If some value of $L$ coincides with a value
of $B$, or two values of $L$ coincide, the statement's right-hand side
(computed via the *combinatorial* rule "odd ranks go to the first mover,"
which is well-defined and tie-invariant, as already established inside the
Doubling Lemma's proof: a tied block occupying a fixed range of consecutive
ranks contributes a value depending only on the range, not on
tie-breaking) is a continuous function of the underlying real parameters
defining $M$ (a fixed sum of explicit order statistics of an explicit
linear function of finitely many real inputs, and order statistics are
$1$-Lipschitz, hence continuous). The formula proved above on the dense
open generic locus extends by continuity to its closure, i.e. to every
tied configuration — the identical closure argument already used (and
flagged) for Theorem 6 and Theorem 7 above. No new case analysis is
needed.

**Independent numerical verification.** $20{,}000$ random trials
(random $k\in\{0,\dots,4\}$, random number of blocks $\in\{0,\dots,5\}$,
random positive values): maximum observed discrepancy between the formula
and direct brute-force $\mathrm{OddSum}(M)$ computation was
$7.1\times10^{-15}$ (floating-point roundoff only). This also directly
generalizes and re-derives Theorem 7's proof mechanism ($k=1$:
$\mathrm{OddSum}(\{\ell_1\})=\ell_1$ trivially, recovering
$\mathrm{OddSum}(M)=\tfrac12\mathrm{sum}(B)+\ell_1$ exactly as computed
there) as a special case, rather than an independent re-derivation.

### Theorem 10 (General $k$-Anchor-Merge Lemma) — round 6

**Statement.** Let $p_1\ge p_2\ge\cdots\ge p_{n+1}>0$ sum to $1$ ($n\ge1$).
Fix $k\ge1$ and $k$ pairwise-disjoint index pairs $(i_1,j_1),\dots,(i_k,j_k)$
with $i_m<j_m$ (so $p_{i_m}\ge p_{j_m}$) for each $m$, all $2k$ indices
distinct. Let $\ell_m:=p_{i_m}-p_{j_m}\ge0$. XY's move: for each $m$, split
$p_{i_m}$ into the two fragments $(\ell_m,\,p_{j_m})$ (one cut), leave
$p_{j_m}$ untouched, and bisect every other piece $p_r$
($r\notin\{i_1,j_1,\dots,i_k,j_k\}$) into $(p_r/2,p_r/2)$ (one cut each).
This uses exactly $k+(n+1-2k)=n+1-k\le n$ cuts (since $k\ge1$), within
budget. Then, generically (each $\ell_m$ distinct from the others and from
every $p_{j_{m'}}$ and every $p_r/2$; relaxed by continuity as in Theorem 9),
$$\mathrm{OddSum}(M)=\frac12\Bigl(1-\sum_{m=1}^k\ell_m\Bigr)+\mathrm{OddSum}(\{\ell_1,\dots,\ell_k\}).$$

**Proof.** In the resulting multiset $M$: each value $p_{j_m}$ occurs with
multiplicity $2$ (the untouched original piece plus the fragment tied to
it) — an even block; each value $p_r/2$ ($r$ bisected) occurs with
multiplicity $2$ — an even block; and each $\ell_m$ is a singleton,
generically distinct from all block values and from each other. So
$M=B\sqcup L$ with $B=\bigcup_m\{p_{j_m},p_{j_m}\}\cup\bigcup_r\{p_r/2,p_r/2\}$
and $L=\{\ell_1,\dots,\ell_k\}$, exactly the hypothesis of Theorem 9
(Singleton-Interleaving Lemma). Applying Theorem 9:
$$\mathrm{OddSum}(M)=\tfrac12\,\mathrm{sum}(B)+\mathrm{OddSum}(L).$$
Compute $\mathrm{sum}(B)$: the pieces not appearing as an $i_m$ (i.e. the
$p_{j_m}$'s and the bisected $p_r$'s) sum to $1-\sum_m p_{i_m}$; each
$p_{j_m}$ contributes $2p_{j_m}$ to $\mathrm{sum}(B)$ (multiplicity 2)
while each bisected $p_r$ contributes $2\cdot(p_r/2)=p_r$ (multiplicity 2,
half value each). So
$$\mathrm{sum}(B)=\sum_m 2p_{j_m}+\sum_{r\text{ bisected}}p_r
=\sum_m2p_{j_m}+\Bigl(1-\sum_m p_{i_m}-\sum_m p_{j_m}\Bigr)
=1+\sum_m p_{j_m}-\sum_m p_{i_m}=1-\sum_m\ell_m.$$
Substituting gives the claimed formula. $\blacksquare$

**Sanity check ($k=1$): recovers Theorem 7 (Anchor-Merge Lemma) exactly.**
$\mathrm{OddSum}(\{\ell_1\})=\ell_1$ trivially (a singleton is always
claimed by the first mover, occupying rank 1), so Theorem 10 gives
$\mathrm{OddSum}(M)=\tfrac12(1-\ell_1)+\ell_1=\tfrac12(1+\ell_1)$,
matching Theorem 7's formula exactly with $\ell_1=p_i-p_j$.

**Sanity check ($k=2$): Double-Anchor-Merge closed form.**
$\mathrm{OddSum}(\{\ell_1,\ell_2\})=\max(\ell_1,\ell_2)$ (the larger of two
values is always claimed at rank 1, the smaller sits at rank 2 and is not),
so Theorem 10 gives
$$\mathrm{OddSum}(M)=\frac12(1-\ell_1-\ell_2)+\max(\ell_1,\ell_2)
=\frac{1+|\ell_1-\ell_2|}2.$$
This is $\le c(n)$ exactly when $|\ell_1-\ell_2|\le1/(2^{n+1}-1)$: XY
should choose two disjoint index-pairs whose "gap values" $p_{i_1}-p_{j_1}$
and $p_{i_2}-p_{j_2}$ are as close to each other as possible.

**Independent numerical verification.** Direct simulation (constructing
the actual multiset $M$ and computing $\mathrm{OddSum}$ by sort-and-sum,
not the formula) over $5{,}000$ random instances ($4\le$ number of pieces
$\le16$, random $k$, random disjoint pairings): maximum discrepancy between
the formula and direct computation $2.2\times10^{-16}$ (floating-point
roundoff only; script and raw output available on request, reproduced via
`python3` in this round's session).

**Numeric coverage of the Double-Anchor-Merge sub-case ($k=2$), applied to
round 5's previously-fully-open "large-gaps-everywhere" residual.** For
each $n$, sampled balanced-region partitions with **every** consecutive
gap $>1/(2^{n+1}-1)$ (i.e. instances where round 5's Anchor-Merge, $k=1$,
provably fails — $100\%$ failure by construction of the sampling), and
computed the best Double-Anchor-Merge value by exhaustively searching all
pairs of disjoint index-pairs $(i,j),(k',l')$ (not restricted to adjacent
gaps — the optimum can use any two distinct-value pairs, not necessarily
consecutive indices):

| $n$ | trials (all with every gap $>\gamma(n)$) | fraction still failing after best $k=2$ merge |
|---|---|---|
| 3 | 300 | 34.7% |
| 4 | 300 | 18.3% |
| 5 | 300 | 7.0% |
| 6 | 300 | 4.3% |
| 7 | 300 | 3.7% |
| 8 | 300 | 4.7% |

So Theorem 10's $k=2$ case closes a **large majority** (65%–96%) of round
5's previously fully-open residual, decisively confirming this is real,
substantial further progress — but it is **not** a complete closure: a
nonzero (roughly $4$–$35\%$, non-monotone in $n$) fraction of the residual
still resists the best 2-piece merge.

**Negative finding: $k=3$ is not monotonically better than $k=2$.** Tested
$k=3$ (using $6$ of the $n+1$ pieces, $3$ disjoint pairs) on the same
sampled instances (exact enumeration over all ways to choose $3$ disjoint
pairs, for $n\ge5$ where $n+1\ge6$): in every one of $200$ tested instances
per $n=5,6,7,8$ where the best $k=2$ value already succeeded, the best
$k=3$ value was **worse** (larger, i.e. it failed the target where $k=2$
had succeeded). This is because $k=3$ commits a structurally different
partition of the index set (using $6$ indices in $3$ pairs, leaving
$n+1-6$ bisected, versus $k=2$'s $4$ indices in $2$ pairs, leaving
$n+1-4$ bisected) — it is **not** a superset of the $k=2$ family of
constructions, so there is no monotonicity guarantee, and this round found
concrete instances where it is strictly worse. Recorded honestly as a
genuine negative result, not silently dropped: the correct approach for a
future round is to take the **minimum over $k=1,2,3,\dots$** (each
evaluated independently via Theorem 10, with the best index-pairing found
by search or, eventually, by a proved closed-form rule for the optimal
pairing), not to assume larger $k$ is always at least as good.

### Theorem 11 (Subset-Tie Lemma) — round 7

**Dispatch note.** This round's instruction was to attack the residual via
a boundary-layer/continuity argument as $p_1\to1/2^-$, connecting to the
already-closed $p_1\ge1/2$ regime (Theorem 2). The literal version of that
idea — leave $p_1$ **untouched** as a singleton and bisect everything
else — was checked symbolically first and found to be *bad*, not good,
near the boundary: by Theorem 9 this gives
$\mathrm{OddSum}=\tfrac12(1-p_1)+p_1=\tfrac12+\tfrac{p_1}2$, which needs
$p_1\le\gamma(n):=1/(2^{n+1}-1)$ to succeed — the opposite end of the
range from $p_1\to1/2^-$, and a regime already closed by other means. So a
literal continuity graft onto Theorem 2 does not work: near $p_1=1/2$,
$p_1$ itself is exactly the piece that *must* be tied down (via a cut), not
left alone. This diagnosis directly motivated the following construction,
which **does** tie $p_1$ down but exploits the fact that, near
$p_1=1/2^-$, the tail $R=(p_2,\dots,p_{n+1})$ has total mass $S=1-p_1$ only
slightly more than $p_1$ itself — so a well-chosen *subset* of the tail's
own pieces, not just a single anchor pair, can be tied to almost all of
$p_1$ at no extra cut cost.

**Statement.** Let $p_1\ge p_2\ge\cdots\ge p_{n+1}>0$ sum to $1$, and let
$R=(p_2,\dots,p_{n+1})$. For any subset $J\subseteq\{2,\dots,n+1\}$ with
$T:=\sum_{i\in J}p_i\le p_1$, let $r:=p_1-T\ge0$. XY's move: split $p_1$
into the $|J|+1$ fragments $\{p_i:i\in J\}\cup\{r\}$ (or just the $|J|$
fragments $\{p_i:i\in J\}$ if $r=0$), leave every $p_i$ ($i\in J$)
untouched, and bisect every other piece $p_m$ ($m\notin J\cup\{1\}$) into
$(p_m/2,p_m/2)$. Then, generically ($r$ distinct from every value already
present),
$$\mathrm{OddSum}(M)=\frac{1+r}2.$$

**Cut count.** Splitting $p_1$ into $|J|+1$ pieces costs $|J|$ cuts (or
$|J|-1$ if $r=0$); bisecting the $(n+1)-1-|J|=n-|J|$ remaining tail pieces
costs $n-|J|$ cuts. Total: $|J|+(n-|J|)=n$ cuts (or $n-1$ if $r=0$) —
**within budget for every choice of $J$**, not just a favorable one. This
is the key mechanical fact that makes the construction free to optimize
over $J$.

**Proof of the formula.** Immediate corollary of the certified
Singleton-Interleaving Lemma (Theorem 9): $B=\{p_i,p_i:i\in J\}\cup\{p_m/2,
p_m/2:m\notin J\cup\{1\}\}$ is a disjoint union of even blocks, and
$L=\{r\}$ (or $L=\emptyset$ if $r=0$, in which case apply the Doubling
Lemma, Theorem 1, directly to $B$ instead — the two cases agree in the
limit $r\to0^+$). Computing $\mathrm{sum}(B)$: the untouched-plus-tied
pairs contribute $2T$; the bisected pieces contribute their own sum
$S-T$ (where $S=1-p_1$ is the tail's total). So
$\mathrm{sum}(B)=2T+(S-T)=S+T=(1-p_1)+T=1-r$. By Theorem 9,
$\mathrm{OddSum}(M)=\tfrac12(1-r)+r=\tfrac{1+r}2$. $\blacksquare$

**Independent self-check (builder, before write-up).** Verified the
formula against a direct construct-and-sort-and-sum simulation (not the
closed form) using exact `Fraction` arithmetic: $80$ random trials,
$n=3,\dots,6$, $J$ chosen as the optimal subset (below) — **zero**
discrepancies (exact rational equality in every trial). Script:
`/tmp/round-7/verify_tailtie.py`-style check, reproducible.

**Optimizing over $J$.** $\mathrm{OddSum}=\tfrac{1+r}2\le c(n)$ iff
$r=p_1-T\le\gamma(n)$, i.e. iff $T\ge p_1-\gamma(n)$. Since $r\ge0$ is
forced ($T\le p_1$), the best choice of $J$ **maximizes** $T$ subject to
$T\le p_1$ — an instance of the subset-sum problem "largest achievable
subset sum not exceeding a cap." Two versions:
- **Optimal** (exhaustive/DP over the $\le2^n$ subsets of the tail;
  well-defined and exact, tractable for the per-instance verification used
  below).
- **Greedy** (process tail elements in descending order, add to $T$
  whenever it would not push $T$ past $p_1$): a fully explicit,
  polynomial-time rule, no combinatorial search needed for a proof
  write-up. Numerically, greedy is nearly as good as optimal (see table
  below) and is the version to eventually pursue as an unconditional,
  algorithmically-explicit lemma.

**Relation to previously-certified tools.** This strictly generalizes
**both** Theorem 2 (Generalized duplicate-the-rest: the special case
$J=\{2,\dots,n+1\}$, i.e. tie the *entire* tail, valid only when
$p_1\ge S$) **and** the certified Suffix-Match Insertion Lemma (Theorem 6,
round 4: the special case where $J$ is a **prefix of the tail sorted
ascending**, i.e. the $t$ *smallest* tail elements). The round-4 file
explicitly flagged Theorem 6 alone as numerically insufficient (43–97%
failure), and this round's numerics (below) show why: tying the
*smallest* elements is close to the *worst* way to choose $J$ among
subsets of a given size, since it leaves $r=p_1-T$ as large as possible;
tying the *largest* elements first (greedy) or an optimal subset instead
minimizes $r$, which is exactly what closes so much more of the residual.

**Numeric impact on the residual "large-gaps-everywhere" sub-case.**
Sampled balanced-region instances with **every** consecutive gap
$>\gamma(n)$ (i.e. round 5's Anchor-Merge, $k=1$, provably fails on all of
them by construction), and computed the fraction still failing after
taking the best of $\{k=1,\,k=2\text{ Anchor-Merge},\,\text{Subset-Tie
(optimal }J)\}$:

| $n$ | trials | round-6 residual (best $k\in\{1,2\}$ only) | round-7 residual (best of $k\in\{1,2\}$ **and** Subset-Tie) |
|---|---|---|---|
| 3 | 300 | 34.7% | 9.0% |
| 4 | 300 | 18.3% | 2.0% |
| 5 | 300 | 7.0% | 0.3% |
| 6 | 300 | 4.3% | 0.0% (0/300) |
| 7 | 300 | 3.7% | 0.0% (0/300) |
| 8 | 300 | 4.7% | 0.0% (0/300) |

A larger targeted search at $n=6,7,8$ (up to $\sim30{,}000$ sampling
attempts each, to find rare survivors) does find a **nonzero** residual at
$n=6,8$ — e.g. at $n=6$: $p=(0.3306,0.2791,0.1501,0.1162,0.0904,0.0208,
0.0128)$, best-of-three value $\approx0.503983$ vs $c(6)\approx0.503937$
(excess $\approx4.6\times10^{-5}$); at $n=8$, three further examples with
excess $\approx1\text{–}5\times10^{-4}$ (raw session output;
`p_1\approx0.24$–$0.27$ in these particular survivors, i.e. **not**
concentrated at the $p_1\to1/2^-$ boundary specifically — the residual
that remains after Subset-Tie is spread differently than the
pre-Subset-Tie residual was). No trial at $n=7$ (800 sampled, up to
$\sim2300$ attempts) produced a survivor. So: **the residual shrinks
sharply (round 6's 4–35% down to $\lesssim9\%$, and $0$ in every sample of
300 at $n\ge6$) but is not proved to vanish**; rare survivors exist at
$n=6,8$ with tiny excess over $c(n)$, close enough to the boundary that a
sharper choice of $J$ (or a further small correction, see below) very
plausibly closes them too, but this was **not** proved this round.

**A further explored (not yet formalized) refinement: Delta-Cut.**
Instead of leaving $r=p_1-T$ as an untouched singleton, spend one more cut
on a tail piece $p_m\notin J$ with $p_m>r$: split $p_m$ into $(r,\,p_m-r)$,
tie the $r$-fragment to $p_1$'s own $r$-fragment (now an even block of
multiplicity $2$, contributing $r$ to $B$ instead of leaving $r$ as an odd
singleton), and let the new leftover $p_m-r$ be the (smaller) singleton
instead. This uses exactly the same cut budget ($n$ total, verified by the
same counting argument) and was checked numerically to strictly shrink the
residual further (e.g. $n=3$: $9.0\%\to6.8\%$ combined with Delta-Cut on
top of the table above's construction), but the resulting closed-form
value was **not independently re-derived or proved this round** — reported
here only as a promising numerically-confirmed lead for the next round,
not a certified tool.

**Honest conclusion.** Theorem 11 (Subset-Tie Lemma) is a fully proved,
general-purpose construction (an immediate corollary of the certified
Theorem 9, itself independently re-verified this round by direct
simulation) that **substantially** narrows the residual "large-gaps-
everywhere" sub-case left open after round 6 — from $4$–$35\%$ down to
$\lesssim9\%$, and to $0$ in every one of $300$ samples at $n\ge6$ — but a
provably nonzero residual survives at $n=6,8$ (found by a larger targeted
search), so the **Existence Theorem is still not proved**. This round's
literal boundary-layer/continuity idea (graft the $p_1\ge1/2$ construction
onto $p_1\to1/2^-$) was checked and shown *not* to work directly (see the
dispatch note above) — the productive redirection was to a genuinely more
general tail-subset construction, which happens to close most of the
$p_1\to1/2^-$ concentration the round's explorer diagnosed, but is not
itself literally a continuity argument.

### Theorem 12 (Generalized Subset-Tie Lemma, any index) — round 8

**Statement.** Let $p_1\ge p_2\ge\cdots\ge p_{n+1}>0$ sum to $1$ ($k=n+1$
pieces, the full-budget regime). Fix any index $i\in\{1,\dots,n+1\}$ (not
necessarily the largest piece), and let $R_i:=(p_m)_{m\ne i}$ (the other
$n$ pieces). For any subset $J\subseteq\{1,\dots,n+1\}\setminus\{i\}$ with
$T:=\sum_{m\in J}p_m\le p_i$, let $r:=p_i-T\ge0$. XY's move: split $p_i$
into the $|J|+1$ fragments $\{p_m:m\in J\}\cup\{r\}$ (or the $|J|$
fragments $\{p_m:m\in J\}$ alone if $r=0$), leave every $p_m$ ($m\in J$)
untouched, and bisect every other piece $p_\ell$
($\ell\notin J\cup\{i\}$) into $(p_\ell/2,p_\ell/2)$. This uses exactly
$n$ cuts (or $n-1$ if $r=0$) — within budget for **every** index $i$ and
**every** subset $J$, not just $i=1$. Then, generically (i.e. whenever
$r$ is distinct from every value already present in the construction; the
degenerate coincidence cases are handled exactly as in Theorem 11's proof,
by the identical block-parity argument),
$$\mathrm{OddSum}(M)=\frac{1+r}2 = \frac{1+p_i-T}{2}.$$

**Proof.** This is a direct re-application of the certified
Singleton-Interleaving Lemma (Theorem 9,
`lemmas/singleton-interleaving-and-k-anchor-merge.md`), with the role
played by "$p_1$" in Theorem 11's proof played instead by the general
index $i$. Nothing in Theorem 9's proof or in Theorem 11's derivation
uses any ordering property of the piece being split (e.g. that it is the
maximum) — the Singleton-Interleaving Lemma's hypotheses are purely about
$M$'s decomposition into even blocks $B$ plus a singleton multiset $L$,
with no reference to which original index contributed which fragment. Set
$$B=\{p_m,p_m:m\in J\}\ \cup\ \{p_\ell/2,p_\ell/2:\ell\notin J\cup\{i\}\},
\qquad L=\{r\}\ (\text{or }\emptyset\text{ if }r=0).$$
$B$ is manifestly a disjoint union of even-length blocks (each distinct
value present with multiplicity exactly $2$: either an untouched-piece-
plus-its-tied-fragment pair, or a bisected piece's two equal halves).
Computing $\mathrm{sum}(B)$: the untouched-plus-tied pairs for $m\in J$
contribute $2\sum_{m\in J}p_m=2T$; the bisected pieces for
$\ell\notin J\cup\{i\}$ contribute their own total,
$\bigl(\sum_{\ell\ne i}p_\ell\bigr)-T=(1-p_i)-T$ (since the sum of all
pieces other than $p_i$ is $1-p_i$, and the $J$-pieces contribute $T$ of
that). So
$$\mathrm{sum}(B)=2T+\bigl((1-p_i)-T\bigr)=1-p_i+T=1-r.$$
By Theorem 9, $\mathrm{OddSum}(M)=\tfrac12\mathrm{sum}(B)+\mathrm{OddSum}(L)
=\tfrac12(1-r)+r=\tfrac{1+r}2$ (using $\mathrm{OddSum}(\{r\})=r$ for a
singleton, or $\mathrm{OddSum}(\emptyset)=0$ agreeing with the formula at
$r=0$ by direct substitution — the two cases match exactly as in Theorem
11). If $r=0$ (the degenerate case), apply the Doubling Lemma (Theorem 1)
directly to $B$ instead, giving $\mathrm{OddSum}(M)=\mathrm{sum}(B)/2
=(1-r)/2=(1+r)/2$ (since $r=0$) — the same formula, consistent in the
limit. The genericity caveat (values of $J$'s pieces, the bisected
halves, and $r$ all pairwise distinct) is handled exactly as in Theorem
9's own proof: any coincidence merely merges two blocks (still even
length, so the even-block accounting is unaffected) or merges $r$ into an
existing block (turning an even block into one of odd length plus a
leftover, handled by the identical odd-length-block-starting-at-an-
odd-rank computation used in Theorem 2's Case (b) and Theorem 9's own
proof) — no new case beyond what Theorem 9/11 already establish. $\blacksquare$

**Cut count, verified.** Splitting $p_i$ into $|J|+1$ parts costs $|J|$
cuts (one cut per additional fragment beyond the first is not quite
right in general — precisely, splitting one piece into $|J|+1$ fragments
requires $|J|$ cuts, since each cut increases the fragment count of that
one piece by exactly $1$, starting from $1$); bisecting the
$n+1-1-|J|=n-|J|$ remaining pieces costs $n-|J|$ cuts (one cut each).
Total: $|J|+(n-|J|)=n$, matching the full budget exactly, for **every**
choice of $i$ and $J$ — this mechanical fact (identical to Theorem 11's,
since it only depends on the *shape* of the construction, not on which
index plays the role of "$p_i$") is what makes the construction free to
optimize over both $i$ and $J$ simultaneously.

**Relation to Theorem 11.** Theorem 11 is exactly the special case
$i=1$. Theorem 12 strictly generalizes it by allowing XY to instead
subdivide-and-tie a **non-top** piece, useful precisely when some other
piece $p_i$ ($i\ne1$) admits a subset $J$ of the remaining $n$ pieces
whose sum $T$ is closer to $p_i$ (i.e. gives a smaller $r=p_i-T\ge0$)
than any subset of $R_1=(p_2,\dots,p_{n+1})$ gets to $p_1$.

**Independent verification (this round, exact `Fraction` arithmetic).**
Re-derived the formula from scratch (construct $M$ literally — including
the untouched copies of the $J$-pieces at multiplicity $2$ and the
bisected halves — sort, and sum the odd ranks directly) and compared
against the closed form $\tfrac{1+r}2$ over $150$ random trials
($n=3,\dots,10$, random index $i$, random subset $J$ satisfying
$T\le p_i$): **zero discrepancies** (exact rational equality in every
trial; script `/tmp/round-8/scripts/exact_verify3.py`-style
construct-and-sum check, generalized to arbitrary $i$).

### Round 8: honest re-verification of the survivor-rate finding

This round's math-explorer (`/tmp/round-8/math-explorer-existence.md`)
reported that the residual "large-gaps-everywhere" survivor rate for
best-of-named-additive-tools **grows** with $n$ (roughly $1$–$4\%$ at
$n=4$–$8$ up to $8$–$30\%$ at $n=10$–$15$), and that this holds even when
$k=2$ (Double-Anchor-Merge) is included alongside generalized-subset-tie.
Per this round's dispatch, I re-verified this **from scratch**, with
independently-written code (not the explorer's scripts), sampling the
balanced region honestly (uniform-simplex sampling via i.i.d.
$\mathrm{Exponential}(1)$ coordinates normalized to sum $1$ — a standard
Dirichlet$(1,\dots,1)$ construction — conditioned by rejection on
$p_1<1/2$ and every consecutive gap $>\gamma(n)=1/(2^{n+1}-1)$), and
cross-checking every flagged "survivor" against exact `Fraction`
arithmetic before trusting a floating-point read-out.

**What I found, honestly, in three stages:**

1. **Best-of-$\{k=1,\text{generalized-subset-tie (Theorem 12, any
   index)}\}$ alone** (no $k=2$): I reproduce the explorer's qualitative
   growth trend. My own numbers (own independent sampling, own code):
   $n=4$: $2.7\%$ ($8/300$); $n=6$: $1.3\%$ ($4/300$); $n=8$: $6.3\%$
   ($19/300$); $n=10$: $9.0\%$ ($27/300$); $n=12$: $13.3\%$ ($20/150$);
   $n=13$: $16.7\%$ ($25/150$); $n=14$: $24.7\%$ ($37/150$). Same order
   of magnitude and same qualitative growth as the explorer's report —
   this part of the finding is **independently corroborated**.
2. **Best-of-$\{k=1,k=2,\text{generalized-subset-tie}\}$, first attempt**:
   including $k=2$ (Double-Anchor-Merge, `lemmas/singleton-interleaving-
   and-k-anchor-merge.md`, Theorem 10 specialized to $k=2$) via an
   exhaustive search over all disjoint index-pairs, I *initially*
   reproduced growth again ($0\%$ at $n=4,6,8$ but apparently $6.5\%$–
   $16.7\%$ at $n=10,12,13,14$). **On investigation, this was a bug in my
   own script**: a computational speed-cap condition (limiting the
   expensive $k=2$ exhaustive search to small $n$ for runtime reasons)
   silently **excluded $k=2$ from the candidate set at exactly the $n$
   values where growth appeared** — so the "growth with $k=2$ included"
   read-out was actually growth *without* $k=2$, mislabeled. I caught
   this only by manually re-checking one flagged "$n=13$ survivor"
   instance with exact `Fraction` arithmetic: the labeled
   best-of-three value ($\approx0.5003$, apparently exceeding
   $c(13)=8192/16383\approx0.50003$) was **wrong** — the true $k=2$ value
   on that exact instance is $4363/10000=0.4363$, far below $c(13)$, so
   the instance is **not** a survivor at all once $k=2$ is genuinely
   included. This is recorded honestly as a self-caught bug, not
   papered over.
3. **Best-of-$\{k=1,k=2,\text{generalized-subset-tie}\}$, corrected**:
   after removing the speed-cap bug, I re-ran the full range
   $n=4,6,8,10,12,13,14,16$ (total $>1500$ sampled trials): **zero
   survivors found in every one of these runs**, including at $n=13,14$
   where the buggy version had reported $17$–$25\%$ survivor rates.

**Honest conclusion — genuinely inconclusive, reported as such.** This
does **not** establish that best-of-$\{k=1,k=2,\text{Theorem
12}\}$ closes the Existence Theorem, for at least three reasons, stated
explicitly so the next round does not over-read this result:
- **Random sampling is not proof, and has already burned this project
  once.** Round 7 found "$0/300$" survivors at $n=6,7,8$ for a *weaker*
  tool combination, only for a targeted $\sim30{,}000$-attempt search to
  later find genuine rare survivors with tiny excess. The same caveat
  applies here: "$0$ survivors in a few hundred honestly-sampled trials"
  is evidence of a *smaller* residual, not evidence of *no* residual.
  I did not run a comparable large-scale targeted/adversarial search this
  round (time-budget constraint) — this is a concrete, well-scoped task
  for whoever picks this up next: run a $\gtrsim10^4$-attempt adversarial
  search (e.g. local optimization seeded from many random starts, or
  explicit boundary-hugging constructions) specifically hunting for
  survivors of best-of-$\{k=1,k=2,\text{Theorem 12}\}$ at $n=10$–$16$.
- **I have not audited the explorer's own script**, so I cannot rule out
  that their reported "growth even with $k=2$ included" reflects a
  genuinely different (and correct) implementation of $k=2$'s search
  (e.g. a different, perhaps non-exhaustive, pairing heuristic that
  happens to under-perform mine), or a genuine discrepancy that would
  need to be reconciled directly against their scripts
  (`/tmp/explore_existence.py`, `/tmp/verify_direct.py`, `/tmp/explore2.py`,
  `/tmp/explore3.py`, `/tmp/explore4.py`, per their report) rather than
  guessed at. It is equally possible growth resumes at $n>16$, beyond
  what I could sample given the $O(2^n\cdot n)$ cost of exhaustively
  optimizing Theorem 12's subset $J$ at every candidate index — my search
  did not go past $n=16$ for this reason.
- **This does not change the round's scoping decision.** Even if
  best-of-$\{k=1,k=2,\text{Theorem 12}\}$ turns out (with further work)
  to have a small or zero residual for every sampled $n$ up to some
  bound, this is still not a *proof* for all $n$ — the Existence Theorem
  requires a universal statement, and no amount of sampling (honest or
  otherwise) substitutes for one. The plateau-break redirect to
  `global-lp-vertex-sufficiency` (an existence/compactness argument
  aimed at a genuine proof, not one more named construction) made by
  this round's outliner and approved by the outline-reviewer is
  **not undermined** by this finding — if anything, the fact that a
  richer named-tool combination (Theorem 12 + $k=2$) still has an
  unresolved, possibly-nonzero residual at large $n$ (my own honest
  uncertainty above) reinforces exactly the outliner's diagnosis: this
  file's family of tools is not positioned to deliver a rigorous
  universal closure, however good its sampled numbers look.

**Methodological lesson recorded for future rounds (concrete and
reusable):** when benchmarking "best-of-several-tools" survivor rates,
audit every speed-cap / early-exit condition in the code for every $n$
tested — a silently-dropped candidate tool at larger $n$ (introduced for
runtime reasons) can manufacture a spurious "growing residual with $n$"
trend that looks like real mathematical content but is actually a
benchmarking artifact. This is a distinct, and in this instance more
subtle, failure mode from round 7's "undersampling gives false
$0\%$" lesson — here the failure mode is "undertesting due to a
selective silent cap gives false *growth*."

## Open gap (honestly unresolved) — updated round 7

Round 7 substantially narrows, but does **not** close, the "large-gaps-
everywhere" Existence Theorem residual left by round 6. Using the best of
$\{k=1\text{ Anchor-Merge},\,k=2\text{ Double-Anchor-Merge},\,\text{Theorem
11 Subset-Tie}\}$:
- Coverage of round 6's previously-open residual improves from $65$–$96\%$
  to (numerically) essentially $100\%$ in moderate-size random sampling
  ($300$ trials, $0$ survivors at $n=6,7,8$; $9.0\%$, $2.0\%$, $0.3\%$
  survivor rates at $n=3,4,5$ respectively — see the table in Theorem 11's
  write-up above).
- A larger, specifically-targeted search (not uniform random; up to
  $\sim30{,}000$ sampling attempts) still finds **rare** genuine survivors
  at $n=6$ and $n=8$, with very small excess over $c(n)$ ($\sim10^{-5}$ to
  $\sim10^{-4}$) — so the residual is **not proved empty**, only proved
  much smaller and numerically close to empty.
- The round's original dispatch (a literal continuity/boundary-layer
  argument grafting Theorem 2 onto $p_1\to1/2^-$) was checked and found
  **not** to work as stated — recorded as a negative finding, not silently
  dropped (see Theorem 11's "Dispatch note").
- A further refinement (**Delta-Cut**, described but not formalized above)
  was found numerically to shrink the residual even further (e.g. $9.0\%
  \to6.8\%$ at $n=3$) but its closed form was not independently re-derived
  or proved this round — this is the concrete, well-scoped task for the
  next round: (a) formalize and prove Delta-Cut's exact value (should be a
  short corollary of Theorem 9, in the same style as Theorem 11's own
  proof), and/or (b) find and prove a closed-form or algorithmic rule for
  the optimal subset $J$ in Theorem 11 (currently only the existence of an
  optimal $J$, found by exhaustive search over subsets, and an explicit
  greedy heuristic close to it, are in hand — no proof that greedy is
  always optimal, and no proof that optimal-$J$ Subset-Tie, combined with
  $k=1,2$, closes the residual for *every* $n$ and *every* instance, which
  is what the Existence Theorem actually requires).
- Genuinely open: the full Existence Theorem statement itself (some
  response drawn from $\{k=1,k=2,\text{Subset-Tie},\dots\}$ always closes
  every balanced-region instance) is still not proved for any fixed finite
  toolset — only shrunk further, now to a residual small enough that it is
  plausible (not proved) that Delta-Cut or one more targeted tool finishes
  it.

## Open gap (honestly unresolved) — updated round 6

Round 6 substantially narrows, but does **not** close, the residual
"large-gaps-everywhere" sub-case left open by round 5's Anchor-Merge
Lemma. Concretely, using the best of $\{k=1,k=2\}$ (Theorem 10, this
round, which strictly subsumes round 5's Anchor-Merge as its $k=1$ case):
the still-open residual (both gap-based tools fail) shrinks to
$\approx3.7\%$–$34.7\%$ of the previously-$100\%$-open region across
$n=3,\dots,8$ (table above) — a genuine, numerically quantified
improvement, but the **Existence Theorem** targeted by this round's
dispatch ("some pair of pieces always suffices") remains **unproved**:
neither a closed-form rule for the optimal pairing, nor a general
covering/counting argument establishing non-emptiness of good responses
for *every* instance in this shrunk residual, was found or proved this
round. The Two-Piece-Split Vertex Lemma (Theorem 8) supplies the correct
finite-search machinery to verify or refute closability *per instance*,
but converting that into a universal existence proof (or finding a further
sub-case-closing closed form, e.g. optimizing Theorem 10 over $k$ and
pairing jointly with a suffix-match-style single-piece move on the
residual leftover) is left as the concrete open task for the next round.

## Open gap (honestly unresolved) — updated round 5

The universal statement — "for every $n$ and every LB partition, XY has a
$\le n$-cut response forcing $\mathrm{OddSum}\le c(n)$" — is now closed in
**every** regime except one precisely-characterized region, at every level
of the induction on $n$ (see "Combined regime coverage" above for the full
case-by-case status). Concretely, for $k=n+1$ (full budget):
- $p_1\in[1/2,c(n)]$: closed unconditionally (Theorem 2, round 2).
- $p_1\ge c(n)$: closed **conditionally** on $T(n-1)$ holding in full
  (Theorem 5, round 3) — a genuine strong-induction step, not a
  standalone closure, since $T(n-1)$ carries the same type of gap.
- $p_{n+1}\le1/(2^{n+1}-1)$: closed unconditionally (Corollary to Theorem
  4, round 3).
- Within the balanced region ($p_1<1/2$ **and** $p_{n+1}>1/(2^{n+1}-1)$):
  the sub-case where some consecutive gap $p_i-p_{i+1}\le1/(2^{n+1}-1)$ is
  now closed unconditionally (Theorem 7, round 5).
- **Remaining, genuinely open:** the balanced region **with every
  consecutive gap $>1/(2^{n+1}-1)$** — i.e. genuinely "spread-out,
  near-arithmetic" partitions with no small piece, no dominant piece, and
  no close pair. No general rule (conditional or unconditional) was found
  or proved this round for this residual region; it is numerically
  confirmed (not merely unproven) to be non-vacuous and to require a
  construction beyond both single-piece and single-pair-merge families
  (see Theorem 7's coverage table above, and the round-4 negative results).
  This is a strictly smaller, more precisely located gap than the
  round-3/4 blanket "balanced region open," but it is still open, honestly.
  A free-form numerical search (not a proof) suggests the larger family
  "split every piece but one, at jointly-optimized points" may close this
  residual region too, but no closed-form recipe was extracted this round.

The $k\le n$ slack-budget regime is now **fully closed unconditionally**
for every $n$ (Theorem 3, round 3) — this removes one of the two previously
open axes entirely (last round's "pruning lemma... left open" discussion is
now moot for the upper-bound direction: the $k\le n$ case no longer needs
any pruning argument, since it is directly closed by Theorem 3 regardless
of whether LB "should" use full budget).

What is proved in full and is new, reusable content this round: Theorem 3
(Perfect-Pairing Corollary, immediate from the Doubling Lemma), Lemma S
(Subadditivity of OddSum, a genuinely new general tool, unconditional,
distinct from the disproven Lemma X′), Theorem 4 (General Insertion Lemma,
strictly generalizing round 2's Theorem 2 by dropping its ordering
hypothesis), and Theorem 5 (the conditional strong-induction step for
$p_1\ge c(n)$, with the key identity $\varphi(c(n))=c(n)$ verified exactly).
Together these fully close the slack-budget case and narrow the full-budget
open gap to exactly the balanced/near-uniform region above.

## Promotable lemmas

- **Subset-Tie Lemma** (Theorem 11, round 7): for any subset $J$ of the
  tail indices with $T:=\sum_{i\in J}p_i\le p_1$, tying the untouched
  $\{p_i:i\in J\}$ to matching fragments of $p_1$ (remainder
  $r=p_1-T$ left as a singleton) and bisecting everything else achieves
  $\mathrm{OddSum}=\tfrac{1+r}2$, using exactly $n$ cuts for **any** choice
  of $J$ (proved by a direct cut-count argument) — an immediate corollary
  of the certified Singleton-Interleaving Lemma (Theorem 9). Strictly
  generalizes both Theorem 2 (Generalized duplicate-the-rest, $J=$ whole
  tail) and the certified Suffix-Match Insertion Lemma (Theorem 6, $J=$ a
  smallest-elements-first prefix); optimizing $J$ to maximize $T$ (subset
  sum $\le p_1$) or the explicit greedy (largest-first) heuristic
  numerically closes the great majority of round 6's residual
  "large-gaps-everywhere" balanced sub-case (down to $\lesssim9\%$, $0/300$
  at $n\ge6$ in moderate sampling), though a rare nonzero residual survives
  a larger targeted search. Reusable by any future attempt at the balanced
  region's Existence Theorem, and the underlying mechanical fact ("tying
  any subset of the tail to the top piece costs exactly $n$ cuts,
  regardless of subset size or composition") is a clean, general,
  reusable structural fact about the cut-budget accounting itself.
- **Two-Piece-Split Vertex Lemma** (Theorem 8, round 6): mechanical
  LP-vertex generalization of the certified Single-Piece-Split Vertex
  Lemma to two simultaneously-split pieces $T,T'$: the minimum
  $\mathrm{OddSum}$ over all $\le n$-cut joint splits is attained at a
  finite, explicitly-constructed vertex set (each fragment $0$, tied to a
  fixed untouched piece, or — new relative to the single-piece case — tied
  to a fragment of the *other* split piece). Proved in full via the same
  Krein–Milman/active-constraint-counting argument as the single-piece
  case, extended to a product-of-simplices polytope with one cross-tie
  refinement. Reusable by `lp-duality-split-polytope` (coordinated per
  this round's dispatch — this file supplies it) and by any future attempt
  needing the exact 2-piece floor as a per-instance decision procedure.
- **Singleton-Interleaving Lemma** (Theorem 9, round 6): for any multiset
  $M=B\sqcup L$ where $B$ decomposes into even-length blocks (each a run
  of a single value) and $L$ is a finite multiset of positive reals
  distinct from $B$'s values, $\mathrm{OddSum}(M)=\tfrac12\mathrm{sum}(B)
  +\mathrm{OddSum}(L)$, where $\mathrm{OddSum}(L)$ is $L$'s own value
  under the identical alternating-claim rule applied to $L$ alone. Proved
  in full (no genericity gap beyond a continuity-closure argument
  identical in form to Theorem 6/7's), with a clean parity-counting
  mechanism (consecutive-in-$L$ elements are separated by an even number
  of $B$-elements, so $L$'s own internal rank-parity is exactly preserved
  inside $M$). This is a genuinely new, general, and strictly more
  powerful tool than the single-singleton case used inside Theorem 7 —
  it reduces *any* number of simultaneous singleton insertions among
  even blocks to a completely independent smaller instance of the same
  game on $L$ alone, and is reusable by any approach needing to reason
  about multi-piece constructions built from ties-plus-bisections (e.g.
  as the core mechanism behind `dyadic-potential-invariant`'s Vertex
  Pinning Lemma, or as a building block for further $k$-piece merge
  constructions on this or other problems).
- **General $k$-Anchor-Merge Lemma** (Theorem 10, round 6): for any $k\ge1$
  disjoint index-pairs $(i_m,j_m)$ ($p_{i_m}\ge p_{j_m}$) of an LB
  partition, the construction "split each $p_{i_m}$ into
  $(\ell_m,p_{j_m})$, leave $p_{j_m}$ untouched, bisect everything else"
  uses $n+1-k\le n$ cuts and achieves the exact closed form
  $\mathrm{OddSum}=\tfrac12(1-\sum\ell_m)+\mathrm{OddSum}(\{\ell_1,\dots,
  \ell_k\})$ — an immediate corollary of the Singleton-Interleaving
  Lemma. Strictly generalizes round 5's Anchor-Merge Lemma ($k=1$) to
  simultaneous multi-pair merges. Specializes cleanly at $k=2$ to
  $\mathrm{OddSum}=\tfrac12(1+|\ell_1-\ell_2|)$. Numerically shown (this
  round) to close a large majority (65%–96%) of the residual
  "large-gaps-everywhere" balanced sub-case left open by round 5, though
  not all of it, and to be **non-monotone** in $k$ (verified
  counterexamples where $k=3$ is worse than $k=2$ on the same instance) —
  both the positive closed-form tool and this documented non-monotonicity
  are reusable, load-bearing findings for whichever approach next attacks
  the residual region.

- **Doubling Lemma** (Theorem 1 above): for any finite multiset $R$ with
  sum $S$, $\mathrm{OddSum}(R\cup R)=S$ under the greedy alternating claim.
  Proved in full, no ties/genericity restriction (multiplicities handled
  directly). Reusable by any approach needing to reason about
  self-duplicated multisets, e.g. `self-similar-induction-on-n`'s
  peeling recursion or `greedy-reduction-geometric`'s breakpoint-face
  analysis.
- **Generalized duplicate-the-rest** (Theorem 2 above): for any sorted
  $p_1\ge\cdots\ge p_{n+1}>0$ summing to $1$ with $p_1\ge S=1-p_1$, XY's
  response "replace $p_1$ by $R\cup\{p_1-S\}$" achieves
  $\mathrm{OddSum}=p_1$ exactly, using $\le n$ cuts. Proved in full,
  exhaustive two-case split (tie / no-tie with $\ell$), no genericity gap.
  Strictly generalizes the previously-certified
  `lemmas/duplicate-the-rest-exact-response.md` (which is the special case
  of LB's geometric construction) to an arbitrary partition. Reusable by
  `greedy-reduction-geometric` (its Case 2 exchange argument concerns
  exactly this kind of split of the geometric top piece, and this theorem
  supplies the general algebraic identity underlying it) and by any future
  attempt at the general upper bound (it fully closes the sub-case
  $1/2\le p_1\le c(n)$, reducing the remaining work to $p_1>c(n)$ and
  $p_1<1/2$).

- **Perfect-Pairing / Bisect-Everything Corollary** (Theorem 3, round 3):
  for LB partitions with $k\le n$ pieces, bisecting every piece achieves
  $\mathrm{OddSum}=1/2\le c(n)$ exactly, for every $n$. Proved in full as a
  one-line consequence of the Doubling Lemma. Closes the entire
  slack-budget regime unconditionally. Directly reusable by any approach
  needing to dispose of $k<n+1$ LB partitions without further casework.
- **Subadditivity Lemma** (Lemma S, round 3): for any two finite multisets
  $A,B$ of positive reals, $\mathrm{OddSum}(A\cup B)\le\mathrm{OddSum}(A)+
  \mathrm{OddSum}(B)$, unconditionally (no domination/ordering hypothesis).
  Proved in full by strong induction on total size, via the exact
  "removal identity" $g(X)=f(X\setminus\{\max X\})$ (also proved in full
  above). This is a materially different, and true, statement from the
  disproven Lemma X′ (which was a conditional threshold claim) — it is a
  genuinely new, general, reusable tool for bounding $\mathrm{OddSum}$ of
  merged multisets from above without needing to know how the two pieces
  interleave. Likely reusable by `self-similar-induction-on-n` (as a
  replacement tool for reasoning about merges, now that Lemma X′ itself is
  confirmed dead) and by `greedy-reduction-geometric`/`dyadic-potential-
  invariant` for any argument needing an upper bound on a merged
  top-fragment-plus-tail multiset.
- **General Insertion Lemma** (Theorem 4, round 3): for any finite multiset
  $R$ (sum $S$) and any $\ell>0$, $\mathrm{OddSum}(R\cup R\cup\{\ell\})=
  S+\ell$, with no relation required between $\ell$ and $R$'s values.
  Strictly generalizes round 2's Theorem 2 (which required
  $0\le\ell=p_1-S$, i.e. an ordering hypothesis) by removing that
  hypothesis entirely — same proof, re-examined to confirm it never used
  the ordering. Reusable anywhere Theorem 2 was cited, and more besides
  (e.g. it also justifies the "bisect the top $n$, leave the smallest"
  construction used above, which is *not* an instance of round-2's
  narrower Theorem 2).
- **Anchor-Merge Lemma** (Theorem 7, round 5): for any sorted $p_1\ge\cdots
  \ge p_{n+1}>0$ summing to $1$ and any pair $i<j$, the construction "split
  $p_i$ into $(p_i-p_j,p_j)$, leave $p_j$ untouched, bisect every other
  piece" uses exactly $n$ cuts and achieves the exact closed form
  $\mathrm{OddSum}=\tfrac12(1+p_i-p_j)$, proved in full via a general
  "one singleton among even blocks always lands at an odd rank" argument
  (a new, reusable structural fact in its own right, not just specific to
  this construction). Optimized over pairs, this closes the balanced-region
  sub-case where some consecutive gap $p_i-p_{i+1}\le1/(2^{n+1}-1)$.
  Verified numerically exact (max error $2\times10^{-16}$, 3000 trials).
  Reusable by any future attempt needing an exact-value tool for "merge two
  pieces via a tie, bisect the rest" constructions, and the underlying
  "singleton among even blocks is always odd-ranked" fact is a clean,
  general, reusable sub-lemma independent of the merge construction itself.
- **Suffix-Match Insertion Lemma** (Theorem 6, round 4): for a sorted tail
  $R=(p_2,\dots,p_{n+1})$ with pairwise-distinct values, sorted ascending
  $w_1<\cdots<w_n$, and any $t\in\{0,\dots,n\}$ with
  $\sum_{i\le t}w_i\le p_1$, splitting $p_1$ into
  $R_t\cup\{\ell\}$ (where $R_t=(w_1,\dots,w_t)$, $\ell=p_1-\sum_{i\le
  t}w_i$) gives an exact closed-form $\mathrm{OddSum}$ value, computed in
  full generality (four exhaustive sub-cases: generic $\ell$, $\ell=0$,
  $\ell$ ties $R_t$, $\ell$ ties $U:=(w_{t+1},\dots,w_n)$), reducing
  correctly to the Doubling Lemma at $t=0$ (no-op) and to the General
  Insertion Lemma at $t=n$ (full match). Proved in full above; verified
  numerically over $5{,}500$+ trials across all sub-cases, zero mismatches.
  This is a genuine common strict generalization of both the Doubling
  Lemma and the General Insertion Lemma to *partial* duplication, and is
  reusable by any approach needing an exact formula for "duplicate part of
  a multiset, insert one extra element" constructions — **but note
  numerically (this round's Optimization test) that this construction
  alone, optimized over $t$, does *not* suffice to close the balanced
  upper-bound region** (failure rates $43$–$97\%$ across $n=2,\dots,5$); it
  should be reused as an exact-value tool inside a larger, multi-piece
  construction, not relied on by itself for that region.

- **Generalized Subset-Tie Lemma** (Theorem 12, round 8): for any index
  $i$ (not just the top piece) and any subset $J$ of the other $n$ pieces
  with $T:=\sum_{m\in J}p_m\le p_i$, splitting $p_i$ into
  $\{p_m:m\in J\}\cup\{r\}$ ($r=p_i-T$), leaving the $J$-pieces untouched,
  and bisecting the rest, uses exactly $n$ cuts and gives the exact
  closed form $\mathrm{OddSum}=\tfrac12(1+r)$ — a mechanical but genuine
  corollary of Theorem 9, strictly generalizing Theorem 11 ($i=1$).
  Proved in full above; verified by $150$ exact-`Fraction`
  construct-and-sum trials, zero discrepancies. Reusable by any future
  approach (including `global-lp-vertex-sufficiency`) needing an exact
  closed form for "tie a subset of pieces to an arbitrary chosen piece,
  bisect the rest" constructions at any index, not just the maximum.
