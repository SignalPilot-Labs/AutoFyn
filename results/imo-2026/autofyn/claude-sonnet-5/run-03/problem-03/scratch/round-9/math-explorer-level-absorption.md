## imo-2026-03 (lens: Level-Absorption, Subcase (b) of Theorem 7'(m,k;L))

### Exact statement of the target (as currently boxed, `greedy-reduction-geometric.md` Section 11.1)

> **Open Sub-Problem B′ (Level-Absorption, cut-budget-corrected).** Let $B''=\{b_3,\dots,b_k\}$
> have the Dominance-Chain property at level $m-2$ ($\mathrm{sum}(B'')\le2^{m-2}$), let $S''$ be a
> refinement of $\Gamma_{m-2}$ with top $k-1$ levels (i.e. levels $m-3,\dots,m-k$) unsplit and levels
> $0,\dots,m-k-1$ arbitrary, and let $\{\mu_1\}\cup R_1$ be an arbitrary split of the single value
> $2^{m-1}$ with $\mu_1<b_2$ (where $b_2\ge2^{m-2}$ is a *separate, external* target quantity, not
> itself an element of the multiset). **Constraint (the corrected part): the total cut count of the
> whole response — $(k-1)$ [splitting the original top piece into $B$] $+\,|R_1|-1+1$ [splitting
> level $m-1$ into $\{\mu_1\}\cup R_1$] $+\sum(\text{levels }0,\dots,m-k-1\text{'s piece counts}-1)$
> — is $\le m$**, the real game's total budget. Claim:
> $$\mathrm{OddSum}\bigl(B''\cup\{\mu_1\}\cup R_1\cup S''\bigr)\ \ge\ b_2+\mathrm{sum}(B'').$$

This is the sole remaining open piece of Theorem 7'$(m,k;L)$'s inductive step (Subcase (a),
Insertion-Robustness, closed round 8 via Theorems 12/13). Closing it closes Theorem 7' for all
$k\ge2$ (combined with the already-proved $k=1$ base case, Theorem 7a), which closes the entire
interleaved joint Case 2 of the general lower-bound direction.

### Why the naive (uncorrected) version failed — verified, not just asserted

Round 6's boxed version placed **no bound on cut count**. Round 7 found an exact, hand-verifiable
counterexample family: $k=2$, $b_1=b_2=2^{m-1}$ (tight Dominance-Chain, zero slack), level $m-1$
split as $\mu_1=2^{m-2}$, $R_1=\{2^{m-3},2^{m-3}\}$ (**2** pieces), level $m-2$ unsplit, and *every*
level $0,\dots,m-3$ bisected into two equal halves. Every power-of-two value from $2^{m-1}$ down to
$2^{-1}$ then appears with multiplicity exactly 2, so pairing consecutive equal ranks kills exactly
half of every value's contribution: $\mathrm{OddSum}=\sum_{i=-1}^{m-1}2^i = 2^m-\tfrac12 < 2^m$,
margin **exactly $-1/2$ for every $m\ge3$**. This construction spends $m+1$ cuts, exactly one over
the real game's budget of $\le n=m$ (`lemmas/reduction-to-multiset-minimax.md`). Dropping one cut
from $R_1$ (down to a single piece $R_1=\{2^{m-3}\}$, i.e. $\mu_1$ and $R_1$ each a single fragment
of level $m-1$) restores a comfortable margin $2^{m-3}-\tfrac12$, growing with $m$. This is a real,
diagnosed, exact bug — not a hand-wave — and the fix (add the cut-budget constraint) is the correct
minimal one: I independently re-derived the cut count and confirm $1+2+0+(m-2)=m+1$ is exactly one
over budget in the family as given.

I also ran a quick independent sanity script (not a rigorous re-test of the certified corrected
claim — my script did not carefully replicate the exact hypothesis on $S''$'s allowed levels /
budget bookkeeping) and easily reproduced large negative "margins" the moment cut-budget accounting
is even slightly loose. This is consistent with, and reinforces, round 7's own finding: **the
corrected statement is extremely sensitive to getting the budget bookkeeping exactly right** — any
proof attempt must track cut count precisely, not informally. This is the single most important
practical warning for whoever attempts this: get the exact cut-accounting formula right before
attempting any inequality manipulation.

### The real gap: why Insertion-Robustness's technique (Theorem 12/13) does NOT transfer directly

This is the crux structural finding of this pass. Insertion-Robustness (Subcase (a)) needed only
$$\mathrm{OddSum}(B'\cup S''\cup R_1)\ \ge\ S' = \mathrm{OddSum}(B'\cup S'')\ (\text{already} \ge S'),$$
i.e. a **qualitative** monotonicity fact: inserting *any* extra positive mass can only weakly help.
Theorem 13 proves exactly this, unconditionally, with no cap on $R_1$ at all — because the baseline
already meets the target, and 0-or-more extra help is all that's needed.

Level-Absorption (Subcase (b)) is quantitatively different: the baseline instance $(B'',S'')$ (a
genuine Theorem-7 instance at $(m-2,k-2)$) only guarantees
$\mathrm{OddSum}(B''\cup S'')\ge\mathrm{sum}(B'')$ — but the *target* is
$b_2+\mathrm{sum}(B'')$, strictly **larger** by $b_2\ge2^{m-2}$. The inserted mass
$\{\mu_1\}\cup R_1$ (summing to exactly $2^{m-1}$) must therefore supply **at least $b_2$ of
genuine new OddSum**, not just "some nonnegative amount." Theorem 13 only gives
$\mathrm{OddSum}(N\cup R)\ge\mathrm{OddSum}(N)$ — a **zero** lower bound on the *gain*, useless here.
What's needed instead is a **quantitative lower bound on the insertion gain**, and the round-7
counterexample shows this quantitative bound is FALSE without a piece-count (cut-budget) cap: with
enough pieces, the fragmented level can be made to contribute gain arbitrarily close to $0$ (every
inserted piece lands at an even rank via careful pairing), even though its total mass is
$2^{m-1}\gg b_2$ in the limit of few cuts. So: **the over-restrictive hypothesis to drop is not
here** (unlike Insertion-Robustness, where $\max(R_1)\le\mu_1$ was droppable) — instead the
cut-budget hypothesis is *load-bearing and cannot be dropped*, which is the opposite lesson from
Subcase (a). This is worth stating explicitly to the outliner: **do not expect a hypothesis-dropping
result here; the correct generalization of Theorems 12/13 needed is a *quantitative, budget-aware*
insertion-gain lemma, not a hypothesis-free one.**

### Concrete proof leads (not attempted, just identified)

1. **Quantitative single-insertion gain bound, chained with a piece-count budget.** Theorem 12's own
   proof already computes the exact gain of one insertion: $\Delta=v-\mathrm{AltSum}(Z)$ (if $v$
   lands at odd rank) or $\Delta=\mathrm{AltSum}(Z)$ (if even rank), where $Z$ is the displaced
   suffix and $0\le\mathrm{AltSum}(Z)\le\min(v,x_s)$. A "worst chain" of $p=|\{\mu_1\}\cup R_1|$
   insertions can make the *total* gain as low as $0$ only by having every single insertion land at
   an even rank with $\mathrm{AltSum}(Z)\approx0$ each time — this is exactly the "many equal tied
   pairs" mechanism of the round-7 counterexample. The natural next theorem to attempt: bound the
   total gain from below in terms of $p$ (or more precisely the level-value scale $2^{m-1}$ divided
   among $p$ pieces) and show that whenever $p\le$ (the actual cut budget available for that level),
   the total gain is $\ge b_2$. This is the direct generalization of Theorem 12 that Subcase (b)
   actually needs — a genuinely new lemma, not a corollary of Theorem 13.

2. **Exchange-smoothing / extremal-profile reduction (new idea, not previously tried in this file).**
   The crux corpus's `aimo-0146` (combinatorics, `extremal-principle`/`invariants-and-monovariants`)
   proves a bound on a weighted sum of a sorted sequence, subject to a sum constraint and a bounded
   "budget," by **exchange-smoothing**: show that any non-extremal split can be locally perturbed
   (move mass from one position to another) to weakly decrease $\mathrm{OddSum}$ (i.e. move toward
   the adversary's interest) without violating the constraints, until only a small finite family of
   extremal profiles remains, then check those directly. This is structurally very close to what
   Level-Absorption needs: OddSum is (locally) a *weighted* sum of the sorted values with weights
   $1,0,1,0,\dots$ (odd/even rank), the split of $\{\mu_1\}\cup R_1$ (plus the free lower levels) is
   constrained by (a) total sum $=2^{m-1}$ for the level, (b) $\mu_1<b_2$, (c) total piece count
   $\le$ cut budget. An exchange argument (e.g. "if two pieces both sit at even ranks, merging them
   into one piece only shifts one rank without decreasing total gain, freeing a cut") could plausibly
   reduce the adversary's worst case to a small, explicit family of "profiles" — very likely
   including exactly the round-7 tight/near-tight construction (bisect-everything-but-one-cut) as
   the extremal case. If the extremal profile can be pinned down this way, the actual inequality only
   needs verifying at that one family (which round 7 already computed by hand: margin
   $2^{m-3}-\tfrac12>0$ for $m\ge3$) — turning an infinite-dimensional adversary problem into a
   finite check, exactly the shape of the `aimo-0146` crux move. **This is the most promising new
   lead surfaced this round** — it has not been tried by any prior round on this sub-problem (all
   prior work on Level-Absorption was pure numeric stress-testing plus the bug-fix, no proof attempt
   at all yet).

3. **Analogy check requested by dispatch: does Level-Absorption have an over-restrictive hypothesis
   analogous to Insertion-Robustness's droppable $\max(R_1)\le\mu_1$?** Checked directly: the
   hypothesis $\mu_1<b_2$ is *not* obviously droppable (it's what defines Subcase (b) vs (a) in the
   first place — dropping it would just merge into Subcase (a), already closed). The genuinely new
   hypothesis here, the **cut-budget constraint**, is the opposite of over-restrictive: round 7
   proved it is *necessary* (the unconstrained version is false, margin exactly $-1/2$). So the
   Insertion-Robustness playbook ("find and drop an unneeded hypothesis") does **not** transfer here
   — the correct playbook is closer to lead 1/2 above (make the budget hypothesis do real
   quantitative work, don't try to remove it).

### Cheap-kill / structural pruning candidates

- **Dyadic/power-of-two exact-tie counting.** Because every value in this problem is a power of $2$
  (or a sum-preserving split thereof), the "pairing to hide value" mechanism that breaks the
  unconstrained version relies specifically on producing *exact ties* across different source levels
  (e.g. two different fragments both equal to $2^{m-3}$). A parity/multiplicity count of how many
  cuts are needed to manufacture $t$ tied copies of a given dyadic value might give a clean
  closed-form cap on how much "OddSum-loss" a budget of $\le m$ cuts can buy the adversary — worth
  trying as a first pass before the full exchange argument (lead 2), since it may already pin the
  bound $2^{m-3}$ (round 7's tight-case margin) directly as "(budget $m$) implies loss $\le
  2^{m-1}-2^{m-3}\cdot(\text{something})$."
- **Pigeonhole on rank parity.** With only $\le m$ cuts total available for the whole response (not
  just this level), and the pieces of $\{\mu_1\}\cup R_1$ needing to occupy specific sorted ranks
  relative to $B''\cup S''$'s own elements (all bounded by $2^{m-2}$), a pigeonhole argument on how
  many of the $\{\mu_1\}\cup R_1$ pieces can possibly land at *even* ranks (given the total budget
  and the fact each such piece must be paired against a same-or-larger value at the preceding odd
  rank) may directly bound the worst-case loss.

### Knowledge-base entries to use

- No `knowledge_base.md` entry is a ready-made tool for this specific quantitative-insertion
  question (the KB's General Proof Methods / Combinatorics sections are generic pigeonhole /
  extremal-principle entries — worth citing by name once the specific lemma shape is pinned down, but
  none is a direct hit).
- Internal certified lemmas to build on: `lemmas/insertion-monotonicity-theorems-12-13.md` (the
  qualitative tool that does NOT suffice alone but whose proof technique — rank-shift/parity
  bookkeeping via $\mathrm{AltSum}$ of the displaced suffix, Lemma 9 — is exactly the right
  machinery to quantify); `lemmas/greedy-optimality-oddsum.md` (Lemma 1, the underlying
  $(\ast)$-inequality); `lemmas/dominant-chain-theorem-and-prefix-run-decomposition.md` (Theorem 7
  itself, the base of the induction); `lemmas/reduction-to-multiset-minimax.md` (source of the exact
  cut-budget definition — re-read this before writing any budget formula, since round 7's bug was
  exactly a mismatch with this lemma's cut-counting convention).

### Analogous past problems (crux corpus)

- **`aimo-0146`** (combinatorics; subtopics `extremal-principle`, `invariants-and-monovariants`,
  `double-counting`) — genuinely analogous in mechanism: bounds a weighted sum of a sorted sequence
  under a sum constraint and an implicit "budget" via exchange-smoothing, reducing an
  infinite-dimensional adversary choice to a handful of extremal profiles checked directly. This is
  structurally the closest match found in the corpus to what Level-Absorption needs (see Lead 2
  above) — worth reading `past_problems_database.json`'s full statement/solution for `aimo-0146`
  before attempting the exchange argument, to borrow the exact "unit-move strictly raises/lowers the
  objective" bookkeeping style.
- **`aimo-0558`** (combinatorics; `processes-and-algorithms`/`extremal-principle`) — a "bounded-gap
  greedy vs. matching adversarial block construction" problem; only loosely analogous (its greedy is
  a genuine forced-vs-free selection under a positional gap constraint, structurally different from
  OddSum's rank parity), but the general shape "adversary builds alternating same/opposite blocks to
  force a matching bound" echoes the round-7 counterexample's "bisect every level" block structure.
  Weaker analogy than `aimo-0146`; mention only as a secondary reference.
- No crux found that is a close match on `games-and-strategy` specifically (scanned all 39
  combinatorics `games-and-strategy` cruxes) — none concern a quantitative alternating-claim /
  OddSum-style value function with an insertion-budget question; that subtopic's cruxes are mostly
  pairing/mirroring strategy proofs for win/lose games, a different genre from this problem's
  minimax-value computation.

### Prior progress

Everything above Subcase (b) is either certified or closed: Theorem 7 (Dominance-Chain, top-levels-
clear case), Theorem 7a ($k=1$ base case, unconditional $f\equiv0$), Theorem 14 (Subcase (a),
Insertion-Robustness, closed round 8). The exact identities (10.1), (10.2a)/(10.2b) reducing the
$k\ge2$ inductive step to Subcases (a)/(b) are fully derived (not asserted) and not in question.
Level-Absorption itself: **no proof attempt has yet been made** — round 6 found and numerically
tested the wrong (unbudgeted) version, round 7 found the bug, fixed the hypothesis, and re-tested
(≈90,000 trials, zero violations, corrected-version margin strictly growing with $m$ at the one
hand-computed tight-ish case); round 8 did not touch it at all (focus was Subcase (a)). So the state
is: **precisely stated, heavily numerically corroborated, zero prior proof attempts.**

### Dead ends (do not retry)

- **Unbudgeted / cut-count-unconstrained Level-Absorption.** Proved false (round 7, exact
  counterexample family, margin $-1/2$ for all $m\ge3$). Any proof attempt MUST carry the cut-budget
  hypothesis explicitly through every step; do not attempt to prove a budget-free version.
  Independently re-confirmed as clearly correct in this pass (re-derived the cut count $m+1$ by hand
  and independently sanity-triggered violations with sloppy budget bookkeeping).
- **Direct application of Theorem 13 (General Insertion Monotonicity) to close Subcase (b).** Checked
  explicitly this round: Theorem 13 only gives $\mathrm{OddSum}(N\cup R)\ge\mathrm{OddSum}(N)$, a
  zero lower bound on the *gain*; Subcase (b) needs the gain to be $\ge b_2>0$. This is not a subtle
  gap — it is a category mismatch (qualitative monotonicity vs. quantitative gain bound) — flag this
  clearly to the outliner so no approach wastes a round trying to cite Theorem 13 directly for
  Subcase (b).
- **Hoping for a droppable hypothesis analogous to Insertion-Robustness's $\max(R_1)\le\mu_1$.**
  Checked: the natural candidate ($\mu_1<b_2$) is definitional, not over-restrictive, and the
  cut-budget hypothesis is proven necessary, not droppable. Do not repeat the "look for a hypothesis
  to drop" playbook here; it worked for Subcase (a) precisely because that hypothesis was genuinely
  unneeded, which is not the case in Subcase (b).

### Small-case / intuition notes (conjecture, not proof)

- At the one hand-computed near-tight instance ($k=2$, $b_1=b_2=2^{m-1}$, budget-respecting
  1-cut-fewer version of the round-7 counterexample), the margin is $2^{m-3}-\tfrac12$: **positive
  and growing exponentially in $m$**, not merely $\ge0$ — suggesting the true bound has real slack
  once the budget is correctly enforced, and a clean quantitative lemma (rather than a knife-edge
  case analysis) should exist. This is evidence, not proof, but it is a meaningfully strong signal
  that the exchange-smoothing route (Lead 2) is likely to succeed cleanly: the extremal profile is
  not on a knife's edge, so a "worse profiles can only make it larger" monotonicity direction in the
  exchange argument has room to work.
- The $m=3$ exact tight-vs-corrected pair (unbudgeted: margin $-0.5$; budgeted: margin $+0.5$)
  confirms the "one cut" is worth exactly $1$ unit of margin at the smallest scale ($2^{m-3}=1$ at
  $m=3$), consistent with each cut being able to buy the adversary at most one full dyadic "pairing"
  worth of loss — a concrete quantitative hint for Lead 1's chained single-insertion bound (each
  insertion beyond the "no fragmentation" baseline costs at most one unit of the relevant scale).
