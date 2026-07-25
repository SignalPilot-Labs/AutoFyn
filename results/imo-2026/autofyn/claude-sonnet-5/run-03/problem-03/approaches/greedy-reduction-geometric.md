## Status
partial

## Round 11 target (per outliner, advance)
Formalize the WLOG $b_2=2^{m-1}$ reduction; attempt a quick-win closure of
Case B ($\max(P)<2^{m-2}$) via dominant-element insertion; time permitting,
attack Case A via Prefix-Run-Peeling on $P$ itself. **Result:** Lemma N
(WLOG reduction) is now a complete, formal proof (Section 15.1). The
"quick-win" premise for Case B is **refuted by stress-testing** (an exact
near-zero-margin instance is exhibited, margin $19/81977$, not the round's
claimed $\approx0.34$), and replaced by a genuine, rigorous, exact
equivalence (Theorem N, Section 15.3): Case B's hardest identified slice is
literally TOP-ONLY$(m-1)$'s complementary regime — already partially closed
by Theorem 6 (this file) and `self-similar-induction-on-n`'s own work, with
the same open residual (Branch-I.A-restricted window) as the true remaining
gap. Case A not attempted (time); one precise scope diagnosis recorded
(Section 15.4). See Section 15 for full detail.

## Round 10 target (per outliner, revise)
Close **Level-Absorption** via the "new asymmetric decomposition": bank
$\mathrm{sum}(B'')$ for free via Theorem 7a applied one level down to
$B''\cup S'''$, reducing the target to a strictly smaller residual on $P$
alone; carefully verify the OddSum-additivity-across-disjoint-parts step
flagged as this round's new crux. **Result:** the banking step is now a
complete proof (Lemma M, Section 14.1, via the general Theorem 7 rather
than just Theorem 7a); the additivity/combination step is **refuted** in
its natural structure-agnostic form (Section 14.2, exact counterexample);
Level-Absorption is reduced to a clean, numerically-confirmed-but-unproved
base case ($k=2$, Section 14.3). See Section 14 below for full detail.

## Round 9 target (per outliner, revise)
Close **Level-Absorption** (Subcase (b) of Theorem 7'$(m,k;L)$'s inductive
step, cut-budget-corrected version) — the sole remaining open sub-problem
of the interleaved joint Case 2. This round's explorer (lens:
level-absorption) made a load-bearing diagnosis: **Insertion-Robustness's
technique does NOT transfer** — Theorem 13's hypothesis-free
$\mathrm{OddSum}(N\cup R)\ge\mathrm{OddSum}(N)$ gives only a *zero* lower
bound on the insertion *gain*, but Level-Absorption needs the inserted
mass $\{\mu_1\}\cup R_1$ (summing to $2^{m-1}$) to supply gain $\ge b_2$ —
a genuinely *quantitative* insertion-gain bound, chained with the
cut-budget cap (proved load-bearing, not droppable, by round 7's exact
$-1/2$-margin counterexample when the budget is exceeded by just one
cut). **Two concrete leads, neither yet attempted:**
1. Quantify Theorem 12's own per-insertion gain formula
   ($\Delta=v-\mathrm{AltSum}(Z)$ or $\Delta=\mathrm{AltSum}(Z)$,
   $0\le\mathrm{AltSum}(Z)\le\min(v,x_s)$) chained across $p=|\{\mu_1\}\cup
   R_1|$ insertions, showing total gain $\ge b_2$ whenever $p\le$ the
   level's actual cut budget.
2. **Exchange-smoothing / extremal-profile reduction** (crux `aimo-0146`,
   same crux as the sibling sliver-window gap) — perturb any non-extremal
   split of $\{\mu_1\}\cup R_1$ toward a small finite family of extremal
   profiles (very likely including the round-7 "bisect-everything-but-one"
   near-tight construction, margin $2^{m-3}-1/2>0$), then check the
   inequality only on that finite family. Do NOT attempt a
   hypothesis-dropping proof (the "look for an over-restrictive hypothesis
   to drop" playbook that worked for Subcase (a) does not apply here — the
   cut-budget hypothesis is proven necessary).

## Approaches tried
- **Round 12 (this round): the shared Branch-I.A window's gap (b)
  (monotonicity in $c_1$) is fully closed, in both its previously-known
  (b)(i) and previously-untouched (b)(ii) sub-cases, by one uniform new
  mechanism, reducing the whole window to the single left-endpoint
  statement (gap (a)) — not itself closed.** Proved the **Elementwise
  Monotonicity Lemma** (Section 16.1, general-purpose, $20{,}000$-trial
  exact-`Fraction` stress test, zero violations): $\mathrm{OddSum}(N\cup
  \{x\})$ is non-decreasing in $x$ for any fixed multiset $N$. Combined
  with the elementary fact that $c_1\ge2^{\ell-1}=\max(\Gamma_{\ell-1})>
  \max(D)$ throughout the window (so $c_1$ is always the multiset's weak
  max) and the certified Peel-the-Max identity, this gives the **Transfer
  Monotonicity Theorem** (Section 16.2): moving mass from any $D$-element
  (or a fresh zero-valued slot) into $c_1$ never decreases $\mathrm{OddSum}$.
  Chaining finitely many such transfers (Section 16.3, with a genuine
  subtlety found and fixed: a lone $D$-element's own headroom is short by
  exactly $\varepsilon$, requires the "fresh slot" mechanism instead, not
  just "grow the existing element") gives the **Window Reduction Theorem**
  (Section 16.4): the full window target is equivalent to gap (a) alone
  (the endpoint statement, for *every* admissible $D$, not just Theorem
  W's witness). Independently re-derives, via a different one-step
  argument, the sibling file's certified endpoint-reduction identity as a
  byproduct (Section 16.4, cross-check). All reduction steps stress-tested
  in exact `Fraction` arithmetic (Section 16.5, thousands of trials, zero
  violations, including the specific edge cases the general argument
  needed extra care for). Gap (a) itself remains open; strong further
  computational evidence (recursive $\varepsilon/2$-margin pattern,
  tied-pair-shape minimizer, at every tested $(\ell,\varepsilon)$ up to
  $\ell=4$) is reported honestly as evidence, not proof (Section 16.5).
  Certified candidate for promotion: the Elementwise Monotonicity Lemma
  and the Window Reduction Theorem (both proposed to the reviewer, not
  self-certified).
- **Round 11: Level-Absorption still not closed. The WLOG
  reduction is now a complete formal lemma, and — the round's main finding —
  the dispatched "Case B quick win" is shown, by an exact stress-test
  counterexample to the round's own premise, not to be a quick win at all:
  Case B's hardest slice is proved (Theorem N, an exact symbol-for-symbol
  equivalence, not an analogy) to be identical to the file's own
  already-partially-open TOP-ONLY complementary regime one level down.**
  Proved **Lemma N** in full (Section 15.1): the WLOG $b_2=2^{m-1}$
  reduction from last round's explorer, now with every hypothesis traced
  (including the previously-implicit $|P|\ge2$ fact). Per the dispatch's
  explicit stress-test instruction, tested the round's Case B "quick win"
  premise (last round's claim of $\approx0.34$ margin, no near-ties) with a
  search deliberately concentrating cut budget on $P$ (rather than diluting
  it across $P$ and $S'''$ as the prior search apparently did) and found an
  exact counterexample to that premise: a valid Case B instance with margin
  $19/81977\approx0.00023$ (Section 15.2), confirmed by a separate `scipy`
  continuous optimization finding infimum margin exactly $0$ over the same
  family. Diagnosed this precisely, not just numerically: **Theorem N**
  (Section 15.3) proves that Case B's $S'''$-unsplit-full-budget slice is
  *literally* (term-for-term, not merely structurally similar) an instance
  of the general TOP-ONLY$(m-1)$ claim restricted to its complementary
  (non-Dominance-Chain) regime — already-certified Theorem 6 closes a
  genuine (if vacuous-until-$m=9$) piece of it outright with zero new work,
  and the remaining piece coincides exactly with `self-similar-induction-
  on-n`'s own Branch-I.A-restricted window, so future work on either
  transfers directly to the other; a full closure of Case B (all $S'''$
  shapes, not just the unsplit slice) remains open beyond this. Case A was
  not attempted (time budget); one precise diagnosis is recorded instead of
  a hand-wave (Section 15.4): Case A's own easiest-looking slice does *not*
  trivially reduce to Theorem 5 either, since $\max(P)\ge2^{m-2}$ alone does
  not force the full recursive Dominance-Chain condition on the rest of
  $P$'s sorted list — it lands in the still-open general interleaved regime
  by the identical mechanism, rigorously explaining (not just observing)
  why Case A inherits the general problem's full difficulty. Certified
  candidates for promotion: Lemma N and Theorem N (both proposed to the
  reviewer, not self-certified). Net effect: the round's dispatched "quick
  win" is correctly identified as a mirage and precisely redirected, rather
  than either force-fitting a wrong proof or reporting a vague "not
  closed" — Level-Absorption itself remains open.
- **Round 10: Level-Absorption still not closed, but the
  outline's proposed two-step "bank + combine" mechanism is now fully
  resolved on both halves — one proved in full, the other proved
  impossible in its natural form, and the residual is a single clean base
  case.** Proved **Lemma M ($B''$-Banking Lemma)** in full (Section 14.1):
  $\mathrm{OddSum}(B''\cup S''')\ge\mathrm{sum}(B'')$, via the already
  -certified **general** Theorem 7 applied one level down — correcting the
  outline's citation of Theorem 7a (which is only Theorem 7's $k'=1$ base
  case, insufficient once $B''$ has $\ge2$ elements). Then, per the
  dispatch's explicit instruction to stress-test the additivity step before
  trusting it, formalized the natural "add the two banked bounds" mechanism
  as a precise **Candidate Swap Lemma** and **refuted it** with an exact,
  hand-checkable counterexample ($Q=\varnothing,b=10,P=\{6,6\}$) plus a
  $\sim36\%$ violation rate over $12{,}598$ exact-`Fraction` randomized
  trials (Section 14.2) — a genuine, reusable negative result ruling out an
  entire family of future "prove an abstract swap/insertion bound, then add"
  attempts, not just this round's specific instantiation. This forced
  abandoning the additive-decomposition route in favor of isolating the
  smallest genuinely new residual: the $k=2$ ($B''=\varnothing$) instance of
  Level-Absorption, stated precisely with the correct cut-budget hypothesis
  (Section 14.3) — verified with $27{,}430$ budget-respecting exact-rational
  trials (zero violations, worst margin exactly $0$ at an explicit tight
  instance) and separately confirmed **false without the budget correction**
  (19/12,598 violations), consistent with the established pattern that
  Level-Absorption genuinely needs the cut-budget hypothesis. **Net effect:**
  one new certified lemma (Lemma M) plus one certified negative result
  (Candidate Swap Lemma refuted) plus a sharply reduced, budget-correct,
  numerically-supported base case for the next round to attempt directly;
  Level-Absorption itself remains open.
- **Round 9: Level-Absorption not closed, but a genuine new
  reusable baseline lemma is proved and the natural first-attempt closure
  route is precisely ruled out (not just "not yet found").** Proved
  **Lemma L (Unsplit-Baseline)** in full (Section 13.1): chaining the
  already-certified Theorem 7a and Theorem 13, if XY's split of level
  $m-1$ were left whole (unsplit), Level-Absorption would follow
  immediately with an explicit non-negative slack
  $\Sigma=2^{m-1}-b_2-\mathrm{sum}(B'')$. This isolates the entire
  remaining difficulty to a single "re-splitting degradation" question:
  how much can splitting the value $2^{m-1}$ into $\{\mu_1\}\cup R_1$
  reduce $\mathrm{OddSum}$ relative to that baseline. Per the dispatch's
  explicit warning, did **not** attempt to close this via Theorem 13
  directly (known dead end, qualitative-only). Instead formulated and
  hand-tested (several exact, not-yet-exhaustive computations) an abstract
  **Split-Degradation candidate bound** (degradation $\le g-q_1$, depending
  only on the value being split and its largest fragment), found it holds
  and is **frequently exactly tight** in hand-checked instances, and then
  gave a precise proof that — *even if* this candidate bound is true —
  it is **provably insufficient** to close Level-Absorption whenever
  $k\ge3$ ($B''\ne\varnothing$): its own worst case exactly discards the
  slack $\Sigma$ without recovering anything from $B''$/$S'''$'s own
  structure, and the target strictly needs that recovery. Cross-checked
  this diagnosis against round 7's independent numeric finding (true
  worst-case margin $2^{m-3}-\tfrac12$, growing with $m$, not near zero) —
  consistent, confirming the abstract worst case is not simultaneously
  achievable with the real power-of-two level structure and cut budget.
  **Net effect:** a real, reusable lemma (Lemma L) is added to the shared
  cache; lead 1 of the outline (structure-agnostic quantitative insertion
  chaining) is shown, precisely and rigorously (not just "we didn't find
  it"), to be insufficient on its own — redirecting the next round
  concretely toward lead 2 (exchange-smoothing to a finite extremal-profile
  family, since the abstract worst case is exactly a "many exact ties"
  configuration that such a reduction would need to rule out or check
  directly). Level-Absorption itself remains open.
- Round 8: Insertion-Robustness (Open Sub-Problem A) is now
  CLOSED IN FULL, unconditionally, and in a strictly stronger
  hypothesis-free form.** Following the outline's telescoping-reduction
  lead, we first proved a new general fact from scratch (**Theorem 12,
  Single-Insertion Monotonicity**): inserting one new positive element $v$
  into any finite multiset of positive reals can only ever *increase*
  (weakly) $\mathrm{OddSum}$, and by at most $v$. This was **not** taken on
  faith from the outline's suggested telescoping shape — we derived the
  exact $\Delta\mathrm{OddSum}$ formula from scratch (independent
  re-derivation of the certified Single-Insertion Lemma's content, by the
  same position-parity bookkeeping technique as Lemma 1's own proof of
  $(\ast)$, so the new proof is self-contained and does not even need to
  cite that lemma) and then bounded the one free quantity in it (an
  $\mathrm{AltSum}$ of a suffix) between $0$ and $v$ via a 3-line pairing
  sub-lemma. Chaining (**Theorem 13, General Insertion Monotonicity**) by an
  easy induction on $|R|$ gives: for *any* finite multisets $N,R$ of
  positive reals, $\mathrm{OddSum}(N\cup R)\ge\mathrm{OddSum}(N)$ — no
  constraint on $R$'s shape, size, or the relation between $\max(R)$ and
  anything in $N$ needed at all. Applied to Open Sub-Problem A's exact
  setup ($N=B'\cup S''$, $R=R_1$), this closes it immediately and
  unconditionally, **dropping the hypothesis $\max(R_1)\le\mu_1$ entirely**
  (it was never needed). Per the dispatch's mandatory instruction, this was
  stress-tested numerically with exact `Fraction` arithmetic **before**
  being written up as a proof: single-insertion monotonicity (20,000
  trials, plus 20,000 more using small integer values to force many ties,
  since the tie-break convention is exactly where such an argument could
  silently break) and the general multi-element corollary (20,000 + 10,000
  more trials) — **zero violations in all $\approx90{,}000$ trials**. Net
  effect: Subcase (a) ($\mu_1\ge b_2$) of Section 10.2's inductive step for
  Theorem 7'$(m,k;L)$ is now **fully closed** (combining this new theorem
  with the already-proved Theorem 7 and the exact identity
  (10.2a)/(10.3a)); the only remaining open piece of the whole approach is
  Subcase (b), Open Sub-Problem B (Level-Absorption, cut-budget-corrected
  version from round 7), untouched this round.
- Round 7: per the outline's instruction, stress-tested the two
  round-6 open sub-problems (Insertion-Robustness, Level-Absorption)
  numerically *before* attempting a proof. **Found and precisely diagnosed a
  real bug**: Level-Absorption as literally boxed in round 6 (no cut-budget
  hypothesis) is **false** — an exact, general, hand-verified counterexample
  family (Section 11.1: $B=\{2^{m-1},2^{m-1}\}$, level $m-1$ split
  $(2^{m-2},2^{m-3},2^{m-3})$, level $m-2$ unsplit, every level
  $0,\ldots,m-3$ bisected) gives margin **exactly $-1/2$ for every
  $m\ge3$**, refuting the round-6 hope that $f(L)\equiv0$. Diagnosed the
  precise cause: this construction spends $m+1$ cuts, one more than the
  real game's budget of $\le m=n$ total cuts (`lemmas/reduction-to-
  multiset-minimax.md`) — an omitted cut-budget hypothesis, the same class
  of bug as this round's `self-similar-induction-on-n` fix. Added the
  missing hypothesis and **re-tested the corrected statement**: $\approx
  90{,}000$ fresh exact-rational trials (budget-tracking harness, disjoint
  from the trials that found the bug) found **zero violations**, strong
  evidence the budget-corrected Level-Absorption is true (not yet proved).
  Separately, extended Insertion-Robustness testing to genuine $k'\ge2$
  instances (the round-6/round-7-diagnosed gap: the old $k'=1$ test family
  was structurally incapable of violating the claim) via 20,000 random
  exact-rational trials plus a `scipy` Nelder–Mead adversarial search across
  $k'=1,2,3$ and $m\le11$ (minimum margin found: $+1.5$, always positive)
  plus the same "over-budget, bisect-everything" adversarial pattern that
  broke Level-Absorption, applied to Insertion-Robustness instead (minimum
  margin found: $+3.5$, i.e. Insertion-Robustness looks robust even
  *without* a cut-budget hypothesis, structurally different from
  Level-Absorption in this respect). Attempted a proof of
  Insertion-Robustness (Section 11.2): tried reducing to a single-element
  worst case (refuted — neither single- nor multi-piece $R_1$ is uniformly
  worse, checked by direct counterexample pairs) and tried the certified
  Subadditivity/General-Insertion Lemmas (`lemmas/perfect-pairing-
  subadditivity-and-general-insertion.md`) — neither gives a lower bound of
  the needed shape; no proof found this round, honestly left open despite
  now much stronger numeric support. Net effect: both sub-problems are
  sharpened — Level-Absorption gets a corrected, cut-budget-aware statement
  (with a genuine refutation of the uncorrected version recorded as a
  valuable negative result) and Insertion-Robustness gets substantially
  broader positive evidence — but neither is proved, so Theorem
  7'$(m,k;L)$ for $k\ge2$ remains open.
- Round 6: pursued the outline's target — generalize Theorem 7
  to Theorem 7'$(m,k;L)$, tracking leftover mass $L$ from splitting the top
  tail level $2^{m-1}$, to close the interleaved/top-tail-level-split case
  of general Case 2 (the Leftover-Fragment Obstruction from round 5). First
  numerically pinned down $f(L)$ (per the outline's own required first
  step) on the round-5-identified tightest boundary instance (dominance
  chain $k=2$, $b_1=b_2=2^{m-1}$, zero slack), restricted specifically to
  splitting the top tail level $2^{m-1}$ (the object the obstruction is
  actually about) — exact rational-arithmetic search over equal- and
  unequal-piece split shapes at $m=4,\dots,8$ found **zero violations**
  of the un-degraded target (margin $\le0$ throughout, exactly $0$ at
  $m=4$), evidence that $f(L)\equiv0$ (no degradation at all) is the true
  fact. **Proved in full** (Section 10.1) **Theorem 7a**, the $k=1$ base
  case of Theorem 7': for $b_1\ge2^{m-1}$ and *any* refinement $S$ of
  $\Gamma_{m-1}$ whatsoever (every level, not just the top one, may be
  split arbitrarily), $\mathrm{OddSum}(\{b_1\}\cup S)\ge b_1$ — a genuine,
  unconditional strengthening ($f\equiv0$ for all $L$, all $m$, no
  restriction on which levels are split). For $k\ge2$ (Section 10.2),
  **derived in full** (not asserted) two exact identities via a clean,
  exhaustive case split on $\mu_1$ vs. $b_2$ (Companion Peeling applied to
  each branch), reducing the previously vague "unknown interleaving"
  diagnosis (Section 9.4's Leftover-Fragment Obstruction) to **two
  precisely stated, independently attackable open sub-problems**
  (Insertion-Robustness of Theorem 7, and Level-Absorption) — a genuine
  sharpening of the obstruction, though neither sub-problem is proved this
  round, so the fully general Theorem 7'$(m,k;L)$ for $k\ge2$ remains open.
  Cross-checked against self-similar-induction-on-n's $G(m,k;V)$ per the
  dispatch's dedup instruction (Section 10.3): confirmed these are
  genuinely different objects (structural tail-split perturbation vs.
  target-value perturbation), no duplication found, both sub-problems have
  no evident restatement in terms of $V$/eps-halving.
- Round 5: pursued the outline's pivot to the **fully general
  Case 2** — XY splits cuts between LB's top piece $r_n$ *and* the tail
  $r_0,\ldots,r_{n-1}$ simultaneously (not TOP-ONLY, whose remaining
  Case-B(m,k) sub-target is `self-similar-induction-on-n`'s job this round,
  not duplicated here — its result is not used or needed below). **Proved
  in full** (Section 9 below) a new theorem, the **Joint Dominance-Chain
  Closure (top-levels-clear case)**: if XY's split $B$ of the top piece has
  the already-certified Dominance-Chain property at level $m$ (Theorem 5's
  hypothesis) with $k=|B|\le m$ fragments, and XY *also* cuts the tail but
  **confines every tail cut to the bottom $m-k$ levels** (leaving the top
  $k$ tail-levels $2^{m-1},\ldots,2^{m-k}$ completely unsplit), then
  $\mathrm{OddSum}(B\cup S)\ge2^m$ for *every* such tail refinement $S$ —
  no matter how many cuts are spent on the lower levels or how they are
  distributed. This is a genuine, non-vacuous extension of the
  Dominant-Chain Theorem into the joint (top-and-tail) regime: it is the
  first proved closure in this file of any instance with $c\ge1$ actual
  tail cuts combined with $j\ge1$ actual top-piece cuts. Also proved a
  reusable generalization of the certified Prefix-Run Peeling Decomposition
  Lemma to an arbitrary dominating prefix (Lemma 8, General Domination
  Prefix-Run Lemma), and gave a precise, non-hand-waved diagnosis (the
  **Leftover-Fragment Obstruction**, Section 9.4) of exactly why the
  identical technique breaks the moment a *top* tail level is itself split
  even partially — a genuinely new obstruction, structurally distinct from
  Proposition C (it is not a same-size recursive loop; $m$ strictly
  decreases at every step; the obstruction is that the residual mass left
  over from a partial top-level split does not have the "clean
  levels-untouched" shape the induction needs, not that the sub-problem is
  equally hard). The wider (unproved) conjecture that the *full* joint
  regime (any $j$, any $c$, any distribution, whenever $B$ has the
  Dominance-Chain property) satisfies the target was stress-tested
  numerically far beyond the proved sub-case — 30,000+ random trials plus
  `scipy`-based adversarial (Nelder–Mead) optimization over the tightest
  boundary configuration ($k=2$, $b_1=b_2=2^{m-1}$) for $m$ up to $11$ —
  finding a minimum margin of exactly $0$ (never negative) in every case,
  but this wider claim is **not proved** and is reported honestly as an
  open, well-supported conjecture, not a theorem.
- Round 4: pursued the outline's narrowed target — close a
  genuine "large violation depth" sub-case of the complementary
  (non-Dominant-Chain) regime of TOP-ONLY, using the certified Prefix-Run
  Peeling Decomposition Lemma (Lemma 6) together with the EvenSum-
  superadditivity dual of certified Lemma S. **Proved in full** (Section 8
  below) a new theorem: whenever XY's largest fragment $a_1$ of the split of
  $2^m$ satisfies $a_1<2^{m-3}$, TOP-ONLY holds
  ($\mathrm{OddSum}(A\cup\Gamma_{m-1})\ge2^m$, in fact strictly $>$).
  This uses two new, fully proved, reusable ingredients: **Lemma 7**
  (Odd-Even Domination: $\mathrm{OddSum}(N)\ge\mathrm{EvenSum}(N)$
  unconditionally for any finite multiset, elementary pairing argument) and
  its corollary **Lemma 7′** ($\mathrm{EvenSum}(A)\ge(\mathrm{sum}(A)-\max
  A)/2$ for any nonempty sorted multiset $A$), plus the already-certified
  EvenSum-superadditivity dual of Lemma S. The exact algebra closing the
  inequality (both parities of $m$) was carried out symbolically and
  cross-checked against an independent numeric search: $36{,}611$ random
  instances with $a_1<2^{m-3}$ across $m=8,\dots,15$, zero violations, and
  a closed-form parity-split algebraic verification for every integer
  $m\ge3$ (not just spot checks). Honestly diagnosed the theorem's exact
  boundary: (i) it is *vacuous* for $m\le7$ (the $\le m{+}1$-fragment
  budget forces $a_1\ge2^m/(m{+}1)\ge2^{m-3}$ by pigeonhole whenever
  $m\le7$, so the hypothesis cannot be met) and only becomes non-vacuous
  from $m=8$ on; (ii) the technique provably **cannot** be pushed to
  smaller violation depth $d=1$ (the identical algebra gives a negative,
  growing-in-magnitude margin at every $m$ tested, i.e. it genuinely fails,
  not just "not yet proved") and is **structurally inapplicable** at even
  depth $d=2$ (the superadditivity tool only lower-bounds $\mathrm{EvenSum}$
  of a merge, but Lemma 6's $d$-even branch needs a *lower* bound on
  $\mathrm{OddSum}$ of the merge, and $\mathrm{OddSum}$ is *sub*additive —
  Lemma S — the wrong direction). So the residual open region is now
  precisely $2^{m-3}\le a_1<2^{m-1}$ (violation depths $d\in\{1,2\}$),
  strictly smaller than "the whole complementary regime" reported after
  round 3, with the boundary honestly located rather than merely
  hypothesized. This does **not** re-derive Proposition C's dead-end
  mechanism: no scalar peel-and-recurse step is used for the closed
  sub-case — the residual term is bounded by a single application of
  superadditivity plus the unconditional Lemma 7′, not by a further
  recursive appeal to an equally-hard sub-instance.
- Round 3: pursued the outline's narrowed "top-only-splitting"
  sub-case of Lower-bound Case 2 (all $n$ cuts on $r_n$, tail untouched)
  using the exact known tail. Proved in full a new general "Dominant-Chain"
  theorem (Section 7) that closes this sub-case whenever, at every step of
  the natural top-down peeling recursion, the currently-largest unassigned
  fragment of the top-piece split still dominates the current top of the
  (recursively shrinking) tail — this is a genuine, non-trivial, fully
  rigorous strict generalization of the round-1 Case-1 result, and it
  provably covers the known equality-attaining self-similar construction
  exactly (verified: every level's domination is tight, by design). Also
  proved in full a reusable structural tool, the Prefix-Run Peeling
  Decomposition Lemma, for the complementary regime (top fragment does
  *not* dominate the tail's current top). Used it to precisely diagnose,
  not just assert, why that regime resists the same technique: peeling a
  run of $d\ge1$ known tail values removes mass only from the tail, not
  from $A$, so the invariant that made the Dominant-Chain induction close
  (removed top-piece mass $\ge$ removed tail levels, in matching amounts)
  breaks. This is the exact obstruction independently diagnosed this round
  by `self-similar-induction-on-n`'s own "Recursive Depth Peeling Lemma"
  sub-case $a_1<2^{m-1}$ — an independent cross-check that the two
  approaches have converged on the same, real difficulty from different
  directions, not that either made an avoidable error. Also ran a new
  negative check extending round 2's dead end: a *"tail-priority"* static
  LB strategy (mirror image of the refuted "Q-priority" strategy) was
  tested by exact game-tree computation on a Dominant-Chain-violating
  instance ($n=3$, tail $\{4,2,1\}$, fragments $\{3.9,3.9,0.2\}$, true
  value $8.9\ge8=2^3$) and found to guarantee only a floor of $7<8$ —
  confirming that *no* simple static priority order (in either direction)
  closes the residual gap, ruling out this entire family a second time.
- **Two-phase multiset reduction + geometric construction** (this file, all rounds).
  Round 1: built the full reduction rigorously from scratch (greedy-optimality
  lemma via an exact exchange/domination inequality, position-irrelevance,
  and the resulting minimax-over-multisets reformulation), proved a new
  general "peeling" identity for alternating-claim values, used it to give a
  **complete, fully rigorous proof of the lower bound in the case where Xiang
  Yu (XY) never touches Liu Bang's (LB) largest piece**, and gave a
  **complete, fully rigorous proof of both directions for n = 0 and n = 1**
  via direct optimization. The remaining case (XY splits LB's largest piece,
  for general n) and the fully general upper bound (arbitrary LB partitions,
  arbitrary n) are **not closed** — see Current best for exactly what is
  proven and what the gap is, including two concrete numerical
  counterexamples showing why the two most natural "universal" XY
  strategies (pure bisection of the top piece; unconditional self-similar
  splitting of the top piece) each fail outside special regimes, so the
  correct universal strategy must be regime-dependent and its general form
  is not yet established.
- Round 2 (this round): pursued the outline's exchange-argument /
  piecewise-linear-tie-block plan for Lower-bound Case 2. Proved a new
  general lemma (Lemma 4, Section 4b: "greedy-floor guarantee against an
  arbitrary opponent" — a strict strengthening of the Greedy-Optimality
  Lemma from "greedy is optimal between two optimal players" to "greedy
  guarantees the value against *any* opponent behavior"), fully rigorous
  and promotable. Attempted to use it via a static "Q-priority" LB
  strategy (always clear fragments of $r_n$ before touching the rest) to
  close Case 2 directly — this **fails**, confirmed by an exact game-tree
  computation at $n=3$ (equal split of $r_3$): the Q-priority strategy's
  guaranteed floor is $7/15<c(3)=8/15$, strictly below target, even though
  the true optimal value is $9/15>c(3)$. This is a genuine, documented
  dead end (no static priority order between the split top piece and the
  rest can work) that rules out an entire family of future attempts; the
  outline's own interleaved piecewise-linear / tie-block analysis (its
  steps 2–3) was not reached this round due to time and remains the actual
  open task for Case 2.

## Current best

Throughout, "a piece" means a positive real number (a length), and a
"multiset" is a finite multiset of positive reals. For a finite sorted
list $x_1\ge x_2\ge\dots\ge x_m$ write
$$\mathrm{OddSum} = x_1+x_3+x_5+\cdots,\qquad \mathrm{EvenSum}=x_2+x_4+x_6+\cdots,$$
so $\mathrm{OddSum}+\mathrm{EvenSum} = \sum x_i$.

### 1. The alternating-claim value of a fixed multiset (Greedy-Optimality Lemma)

**Lemma 1.** Fix a finite multiset $M=\{x_1,\dots,x_m\}$ of positive reals
(pieces already cut, no more cutting). Two players alternately claim
(remove) any *currently unclaimed* element of $M$, Player 1 moving first,
each maximizing their own total. Sort $M$ descending as
$x_1\ge x_2\ge\cdots\ge x_m$. Then the game has a well-defined value, and
under optimal play by both sides Player 1's total equals
$\mathrm{OddSum}(M)$. Moreover "always claim a currently-largest unclaimed
element" is an optimal strategy for both players.

*Proof.* Induction on $m$. For $m=0$ both totals are $0$. For $m=1$,
Player 1 takes the unique element, total $=x_1=\mathrm{OddSum}$.

Inductive step, $m\ge2$: suppose the claim holds for all multisets of size
$<m$. Suppose Player 1's first move is to take the element sitting at
sorted position $i$ (some $1\le i\le m$; if several elements tie for that
value, fix one specific copy — the argument below only uses the value
$x_i$ and the sorted position, not which physical tied copy is removed).
After this move the remaining multiset is $M\setminus\{x_i\}$
(size $m-1$), and it becomes Player 2's turn to move first in it. Sorted
descending, $M\setminus\{x_i\}$ is exactly
$$y_1,\dots,y_{m-1}=x_1,\dots,x_{i-1},x_{i+1},\dots,x_m$$
(remove the $i$-th term, keep the rest in order — still sorted since $M$
was sorted). By the inductive hypothesis this $(m-1)$-element subgame has
value $\mathrm{OddSum}(y)=y_1+y_3+\cdots$ to its mover (Player 2), and
therefore value $\bigl(\sum_j y_j\bigr)-\mathrm{OddSum}(y)=\mathrm{EvenSum}(y)$
to the non-mover (Player 1). Hence, if Player 1's first move is to take
$x_i$ and both players subsequently play the (inductively) optimal
strategy of the $(m-1)$-subgame, Player 1's total is
$$T(i) \;=\; x_i + \mathrm{EvenSum}(y) \;=\; \Bigl(\sum_{j=1}^m x_j\Bigr) - \mathrm{OddSum}(y).$$
(The second equality: $x_i+\mathrm{EvenSum}(y)=x_i+\bigl(\sum y_j-\mathrm{OddSum}(y)\bigr)=x_i+\bigl(\sum x_j - x_i\bigr)-\mathrm{OddSum}(y)$.)

We claim $T(i)\le T(1)=\mathrm{OddSum}(M)$ for every $i$, with equality at
$i=1$ (and at any $i$ tied in value with $x_1$). Since $T(1)=\bigl(\sum x_j\bigr)-\mathrm{OddSum}(x_2,\dots,x_m)=\bigl(\sum x_j\bigr)-(x_2+x_4+\cdots)=x_1+x_3+\cdots=\mathrm{OddSum}(M)$,
it suffices to show
$$\mathrm{EvenSum}(M) \;\le\; \mathrm{OddSum}\bigl(M\setminus\{x_i\}\bigr)\qquad\text{for every }i. \tag{$\ast$}$$
(This restates $T(i)\le T(1)$ since $T(i)=\sum x_j-\mathrm{OddSum}(y)$ and $T(1)=\sum x_j-\mathrm{EvenSum}(M\setminus\{x_1\})=\sum x_j - (x_3+x_5+\cdots)$, and one checks directly $T(1)=\mathrm{OddSum}(M)$ while $T(i)\le T(1)\iff \mathrm{OddSum}(y)\ge \mathrm{EvenSum}(M)$.)

To prove $(\ast)$, write out both sides in terms of the original indices.
Removing $x_i$ shifts every index $j>i$ down by one and keeps every
$j<i$ fixed, so an original index $j<i$ contributes to
$\mathrm{OddSum}(y)$ iff $j$ is odd, and an original index $j>i$
contributes to $\mathrm{OddSum}(y)$ iff $j-1$ is odd, i.e. $j$ is even.
Hence
$$\mathrm{OddSum}(y)=\sum_{\substack{j<i\\ j\text{ odd}}}x_j+\sum_{\substack{j>i\\ j\text{ even}}}x_j,\qquad
\mathrm{EvenSum}(M)=\sum_{\substack{j<i\\ j\text{ even}}}x_j+\bigl[x_i\text{ if }i\text{ even}\bigr]+\sum_{\substack{j>i\\ j\text{ even}}}x_j.$$
The tail sums over $j>i,\,j$ even are identical on both sides and cancel,
so $(\ast)$ reduces to
$$\sum_{\substack{j<i\\ j\text{ even}}}x_j+\bigl[x_i\text{ if }i\text{ even}\bigr] \;\le\; \sum_{\substack{j<i\\ j\text{ odd}}}x_j. \tag{$\ast\ast$}$$
Because $x_1\ge x_2\ge\cdots\ge x_{i-1}$ (all indices $<i$), pair
consecutive terms $(x_1,x_2),(x_3,x_4),\dots$: each pair satisfies
$x_{2t-1}\ge x_{2t}$, so the sum of odd-indexed terms among $j<i$ is at
least the sum of even-indexed terms among $j<i$:
$\sum_{j<i,\,j\text{ odd}}x_j \ge \sum_{j<i,\,j\text{ even}}x_j$.
- If $i$ is odd, the pairing $(1,2),(3,4),\dots,(i-2,i-1)$ is exact (no
  leftover term), $[x_i\text{ if even}]=0$, and $(\ast\ast)$ is exactly the
  displayed pairwise inequality.
- If $i$ is even, the pairing leaves the term $x_{i-1}$ (odd index,
  $i-1<i$) unpaired on the right, so
  $\sum_{j<i,\text{odd}}x_j = \bigl(\text{paired odd sum}\bigr)+x_{i-1}\ge \bigl(\text{paired even sum}\bigr)+x_{i-1}=\sum_{j<i,\text{even}}x_j+x_{i-1}$,
  and since $x_{i-1}\ge x_i$ (sorted order, $i-1<i$) this dominates
  $\sum_{j<i,\text{even}}x_j+x_i$, which is exactly the left side of $(\ast\ast)$.

Either way $(\ast\ast)$ holds, so $(\ast)$ holds for every $i$, so $T(i)\le T(1)=\mathrm{OddSum}(M)$ for every possible first move, with equality at $i=1$. Hence taking a currently-largest element is (weakly) optimal for Player 1, this is achievable, and it is simultaneously the true minimax value because the bound $T(i)\le \mathrm{OddSum}(M)$ was derived using the *inductively optimal* continuation for Player 2 — i.e. Player 2 cannot do better than holding Player 1 to $\mathrm{OddSum}(M)$ either. By induction the value of the whole game is $\mathrm{OddSum}(M)$, achieved by both players always claiming a currently-largest remaining piece. $\blacksquare$

Ties are handled automatically: the proof never used strict inequalities
between distinct sorted positions, only $x_1\ge x_2\ge\cdots$, so equal
pieces are interchangeable and the *value* (not just some optimal split)
is unaffected by which tied copy either player takes.

### 2. Position-irrelevance and the multiset reduction

**Lemma 2 (Reduction).** In the original game (LB marks $\le n$ points on
$[0,1]$; then XY marks $\le n$ points; the stick is cut at all marks; then
alternating claiming, LB first), the value equals
$$c(n)=\max_{\substack{p_1,\dots,p_k>0\\ \sum p_i=1,\ k\le n+1}}\ \min_{\substack{\text{refinement of }\{p_i\}\text{ using}\\ \le n\text{ further cuts}}} \mathrm{OddSum}(\text{resulting multiset}),$$
where a "refinement using $\le n$ further cuts" means: choose non-negative
integers $m_1,\dots,m_k$ with $\sum m_i\le n$ and, for each $i$, split
$p_i$ into $m_i+1$ arbitrary positive pieces summing to $p_i$.

*Proof.* By Lemma 1, once the marking phase is entirely finished the
claiming phase's outcome (for both players playing optimally, which is
what "guarantee" / "regardless of play" requires us to analyze) is exactly
$\mathrm{OddSum}$ of the final multiset of piece lengths — a fact that
depends only on that multiset, not on the pieces' positions on the stick.
So it remains to identify exactly which multisets are reachable at each
stage. A choice of $\le n$ marked points by LB partitions $[0,1]$ into some
number $k\le n+1$ of positive-length pieces (consecutive gaps between
$0$, the marks, and $1$); conversely every composition of $1$ into $k\le
n+1$ positive parts, in any order, is realized by placing the marks at the
corresponding partial sums — so LB's reachable set of "outcomes of the
marking phase" is exactly the set of multisets $\{p_1,\dots,p_k\}$,
$k\le n+1$, $\sum p_i=1$ (order along the stick is a free, payoff-irrelevant
choice by Lemma 1, so we may record only the multiset). Given such a
partition realized at specific positions, XY's $\le n$ further marks each
land inside exactly one current piece (a mark at an already-marked point
is disallowed as marks are distinct); a set of marks landing inside piece
$i$ splits it into (number of marks in it)$+1$ sub-pieces of arbitrary
positive lengths summing to $p_i$ (any such split is achievable by
choosing the marks' positions inside that piece), and marks in different
pieces act independently. Hence XY's reachable refinements, as multisets,
are exactly the ones described, parametrized by $m_1,\dots,m_k\ge0$,
$\sum m_i\le n$, with arbitrary positive lengths in each piece. Both
players choose to optimize the resulting $\mathrm{OddSum}$ (LB
maximizing at the outer level, XY minimizing at the inner level, as in
the statement), giving exactly the displayed minimax. $\blacksquare$

*(Scale invariance, used below.)* If every element of a multiset $M$ is
multiplied by a fixed $\lambda>0$, giving $M_\lambda$, then
$\mathrm{OddSum}(M_\lambda)=\lambda\,\mathrm{OddSum}(M)$: multiplying by a
positive constant preserves the sorted order, and $\mathrm{OddSum}$ is a
sum of specific (order-determined) terms, hence linear under this
rescaling.

### 3. A general "peeling" identity

**Lemma 3 (Global-max peeling).** Let $M$ be a finite multiset of positive
reals and let $g$ be (a copy of) $\max(M)$. Then
$$\mathrm{OddSum}(M) = g + \mathrm{EvenSum}(M\setminus\{g\}).$$

*Proof.* Sort $M$ descending as $g=x_1\ge x_2\ge\cdots\ge x_m$ (choosing
the removed copy of $\max M$ to sit at position $1$, always possible).
Then $M\setminus\{g\}$ sorted descending is exactly $x_2,\dots,x_m$, whose
own position $j$ (for $2\le j\le m$) is $j-1$; its own odd/even positions
are therefore $1,2,\dots,m-1$ corresponding to original $2,3,\dots,m$ with
parity flipped. So $\mathrm{OddSum}(M)=x_1+x_3+x_5+\cdots=g+(x_3+x_5+\cdots)$
and $x_3+x_5+\cdots$ is exactly $\mathrm{EvenSum}(M\setminus\{g\})$ (its
own positions $2,4,\dots$ correspond to original $3,5,\dots$). $\blacksquare$

(This is the $i=1$ specialization used implicitly in Lemma 1's proof; it
is recorded separately because it is the tool used below and is directly
reusable — it requires only that $g$ attains the max, no strictness.)

### 4. Lower bound: LB's geometric construction

Fix $n\ge0$ and let $r_i=\dfrac{2^i}{2^{n+1}-1}$ for $i=0,\dots,n$; these
are LB's $n+1$ pieces (in any left-to-right order, by Lemma 2), using
$\le n$ marked points. Write $c(n):=r_n=\dfrac{2^n}{2^{n+1}-1}$ and
$R:=r_0+\cdots+r_{n-1}=\dfrac{2^n-1}{2^{n+1}-1}=c(n)-r_0$ (immediate from
$2^0+\cdots+2^{n-1}=2^n-1$), so in particular $R<c(n)$ and $r_n=R+r_0$.

**Theorem (Lower bound, Case 1).** If XY's response uses no cuts on the
largest piece $r_n$ (i.e. $m_n=0$ in the notation of Lemma 2), then, for
*any* distribution of the remaining $\le n$ cuts among $r_0,\dots,r_{n-1}$,
the resulting multiset $M$ satisfies $\mathrm{OddSum}(M)\ge c(n)$.

*Proof.* Every element of $M$ other than $r_n$ itself is a fragment of
some $r_i$ with $i\le n-1$, hence has length $\le r_i\le r_{n-1}$.
Since $2^{n-1}<2^n$ for $n\ge1$ (and the statement is vacuous/trivial for
$n=0$, where $M=\{1\}$), we get $r_{n-1}<r_n$ strictly for $n\ge1$, so
every other element of $M$ is $<r_n$; hence $r_n=\max(M)$. By Lemma 3,
$\mathrm{OddSum}(M)=r_n+\mathrm{EvenSum}(M\setminus\{r_n\})\ge r_n=c(n)$,
since $\mathrm{EvenSum}$ of any multiset of positive reals is $\ge0$.
$\blacksquare$

This settles the lower bound completely whenever XY's optimal response
happens to avoid the largest piece — in particular it already shows that
*any* XY strategy that never touches LB's largest piece is powerless to
bring LB below $c(n)$, for every $n$.

**Case 2 (XY spends $\ge1$ cut on $r_n$) — OPEN in general**, but fully
resolved for $n=0,1$ (Section 5) and numerically confirmed exactly at
$n=2,3$ for the specific "self-similar" XY response (below). If XY spends
$j\ge1$ of its cuts on $r_n$, splitting it into $j+1$ arbitrary positive
fragments, and the remaining $\le n-1$ cuts on $r_0,\dots,r_{n-1}$ (whose
total mass is $R$, itself exactly the geometric-$(n-1)$ construction
scaled by $R$, by direct computation $r_i = R\cdot \frac{2^i}{2^n-1}$ for
$i\le n-1$), a natural attempt is to invoke the $(n-1)$-instance
inductively (if it were already proven) to say the "rest" retains
$\mathrm{OddSum}(\text{rest})\ge R\cdot c(n-1)$, and to try to combine this
with information about the $r_n$-fragments. This does **not** by itself
finish the argument: knowing only the *total* $\mathrm{OddSum}(\text{rest})\ge Rc(n-1)$ is not enough to control how the $r_n$-fragments interleave
with rest's actual elements in the final sort order — a genuine
merge/interleaving argument is needed, and the natural aggregate bounds
tried (e.g. "top two elements of the merge sum to $\ge r_n$", or bounding
via $\mathrm{OddSum}(\text{rest})\le R$ trivially) were checked and found
to be **false** or insufficient: e.g. for $n=3$, splitting $r_3=8/15$ into
four *equal* fragments of $2/15$ (leaving $r_0,r_1,r_2$ untouched) gives
final multiset $\{4/15,2/15,2/15,2/15,2/15,2/15,1/15\}$ with the two
largest elements summing to $6/15 < r_3=8/15$, yet
$\mathrm{OddSum}=9/15>8/15=c(3)$ still holds (verified directly) — the
inequality survives here via the different mechanism of LB benefiting
from many small, mutually-tied fragments, not from any single dominant
piece, so no simple aggregate inequality captures the true reason $(\ast)$
type bounds hold in general. **This case (XY splits LB's own top piece,
for general $n\ge2$) is the open gap in the lower-bound half of this
approach.**

For concreteness, the specific XY response that achieves *equality* with
$c(n)$ (found by the outline-reviewer's search at $n=3$, and independently
verified here at $n=2$ via exact rational arithmetic) is: spend **all**
$n$ cuts on $r_n$ alone, splitting it into $n+1$ fragments in the *same*
geometric ratio $1:2:4:\cdots:2^n$ that LB used, i.e. fragments
$r_n\cdot\frac{2^i}{2^{n+1}-1}$ for $i=0,\dots,n$. For $n=2$: fragments of
$r_2=4/7$ are $\frac{4}{49},\frac{8}{49},\frac{16}{49}$; merged with
$r_0=1/7=\tfrac{7}{49},r_1=2/7=\tfrac{14}{49}$ the sorted multiset
(descending, in forty-ninths) is $16,14,8,7,4$, and
$\mathrm{OddSum}=\tfrac{16+8+4}{49}=\tfrac{28}{49}=\tfrac47=c(2)$ exactly
(verified by direct rational arithmetic), confirming equality is
attained; this response
is a genuine candidate for XY's *optimal* play in this sub-case, but
proving it is optimal (i.e. that no other split of $r_n$, possibly
combined with cuts elsewhere, does strictly better for XY, i.e. drives
$\mathrm{OddSum}$ below $c(n)$) for general $n$ remains open.

### 5. Complete solved special cases: $n=0$ and $n=1$

**$n=0$:** LB has $0$ points, must present the single piece $\{1\}$; XY
has $0$ points; LB claims it. Value $=1=c(0)$. Trivial, both directions.

**$n=1$ (full proof, both directions).** By Lemma 2, LB chooses $k\le2$
pieces summing to $1$. If $k=1$ (LB uses $0$ points), XY splits the single
piece $\{1\}$ with its $1$ cut into $(a,1-a)$; $\mathrm{OddSum}=\max(a,1-a)\ge1/2$,
and XY can force this down to exactly $1/2$ (by $a=1/2$) — in particular
$\le2/3$, so $k=1$ can never be LB's best choice among values $\ge 2/3$;
we verify below that LB does strictly better with $k=2$, so it suffices to
analyze $k=2$.

For $k=2$: write LB's pieces as $p_1\ge p_2>0$, $p_1+p_2=1$. XY has
exactly $1$ cut, spent on $p_1$ or on $p_2$ (or, in the limit, not spent —
subsumed by taking the split degenerate). Splitting $p_2$ instead of $p_1$
can only be weakly worse for XY: for a split $(a,b)$ of $p_1$ ($a\ge b>0$,
$a+b=p_1$), the resulting 3-element multiset $\{a,b,p_2\}$ has, by the
$3$-element identity "$\mathrm{OddSum}=(\text{total})-\text{median}$"
(true for any 3 positive reals, sorted $x\ge y\ge z$: $\mathrm{OddSum}=x+z=(x+y+z)-y$),
$$\mathrm{OddSum}=1-\mathrm{median}(a,b,p_2).$$
So XY wants to choose $(a,b)$ to *maximize* $\mathrm{median}(a,b,p_2)$
subject to $a\ge b>0$, $a+b=p_1$ (with $b$ ranging over $(0,p_1/2]$).
- If $b\ge p_2$ the sorted order is $a\ge b\ge p_2$ and the median is $b$;
  this is achievable, with $b$ maximized at $b=p_1/2$, exactly when
  $p_1/2\ge p_2$, i.e. $p_1\ge2/3$ (using $p_1+p_2=1$). This gives median
  $=p_1/2$.
- If $b<p_2$ the sorted order is $a\ge p_2\ge b$ and the median is the
  constant $p_2$ (independent of the exact value of $b$, as long as
  $0<b<p_2$ and correspondingly $a=p_1-b>p_1-p_2\ge p_2$ — the last step
  using $p_1\ge p_2$); this regime is non-empty iff $p_1>p_2$ (so $b$ can
  be chosen small enough), i.e. $p_1>1/2$.

Hence, for $p_1\ge2/3$: both regimes are available (as $p_1\ge2/3>1/2$),
giving achievable medians $p_1/2$ and $p_2$, and since $p_1\ge2/3\Rightarrow
p_1/2\ge1/3\ge p_2$, the best (largest) achievable median is $p_1/2$, so
XY's optimal value is $1-p_1/2$.
For $p_1<2/3$ (so $p_1<2/3<2\cdot(1/3)\le 2p_2$ is not quite the direct
statement, but concretely $p_1/2<1/3\le p_2$ when $p_1<2/3$, wait we need
$p_2\ge 1/3$: since $p_1<2/3\Rightarrow p_2>1/3$, so indeed $p_1/2<1/3<p_2$),
so the first regime is infeasible (would need $b=p_1/2\ge p_2$, impossible)
and XY's best is the second regime, giving median $p_2$, value $1-p_2=p_1$
(if $p_1>p_2$, i.e. $p_1>1/2$; the boundary $p_1=p_2=1/2$ gives, by
continuity/direct check with $b\to0^+$, value $\to p_1=1/2$ as well).

So the min-over-XY value as a function of $p_1\in[1/2,1)$ is
$$g(p_1)=\begin{cases} p_1, & 1/2\le p_1<2/3\\ 1-p_1/2, & 2/3\le p_1<1.\end{cases}$$
Both branches are continuous and monotonic ($g$ increasing on $[1/2,2/3]$,
decreasing on $[2/3,1)$), meeting at $p_1=2/3$ with value $g(2/3)=2/3$.
Hence $\max_{p_1\in[1/2,1)} g(p_1) = 2/3$, attained uniquely at
$p_1=2/3$ — which is exactly LB's geometric construction
$(r_0,r_1)=(1/3,2/3)$. Combined with the $k=1$ case (value $\le1/2<2/3$),
this proves **both directions** for $n=1$: LB cannot guarantee more than
$2/3$ against optimal XY play (upper bound, from $\max_{p_1} g(p_1)=2/3$),
and LB's construction $(1/3,2/3)$ guarantees exactly $2/3$ (lower bound,
from $g(2/3)=2/3$, meaning XY's best response still leaves LB with
$2/3$). Hence $c(1)=2/3=2^1/(2^2-1)$, matching the conjectured formula,
proved completely rigorously.

*(Numerically cross-checked: a fine grid search over $p_1$ and over XY's
split independently reproduces $\max_{p_1}\min_{XY}=0.6658\ldots\approx
2/3$ at $p_1\approx0.666$, matching this closed-form derivation to grid
resolution.)*

### 4b. Round-2 attempt at Case 2: a "greedy-floor" strategy lemma, and why the natural composite strategy fails

This round's outline proposed an exchange argument reducing "any cut
allocation" to "all cuts on $r_n$," followed by a piecewise-linear/tie-block
analysis of splits of $r_n$ alone. Pursuing this, we first isolated and
proved in full a genuinely reusable strategy-level lemma, then discovered —
by an explicit computation — that the most natural way to use it (a
"Q-priority" LB strategy) is *not* strong enough to close Case 2, because it
is not always an optimal LB strategy. We record both the proof and the
refutation precisely, since the refutation rules out an entire family of
future attempts along this line.

**Lemma 4 (Greedy-floor guarantee, against an arbitrary opponent).** Let $N$
be a finite multiset of positive reals. If Player 1 plays "always claim a
currently-largest unclaimed element of $N$" on every one of its own turns,
then, **regardless of Player 2's strategy** (not assumed optimal), Player
1's total is $\ge \mathrm{OddSum}(N)$. Symmetrically, if Player 2 plays
greedily on every one of its turns while Player 1 plays arbitrarily,
Player 2's total is $\ge \mathrm{EvenSum}(N)$.

*Proof.* This uses only the inequality $(\ast)$ already established inside
the proof of Lemma 1 (Section 1): for any finite multiset $S$ sorted
descending $x_1\ge\cdots\ge x_m$ and any index $i$,
$\mathrm{EvenSum}(S)\le\mathrm{OddSum}(S\setminus\{x_i\})$. ($(\ast)$ was
proved purely combinatorially, with no assumption on Player 2's behavior —
it is a statement about sorted lists, not about optimal play — so it is
legitimate to reuse it here in a setting where Player 2 is adversarial but
not assumed optimal.)

Induct on $|N|=m$. If $m=0$ both totals are $0=\mathrm{OddSum}(\varnothing)$.
For $m\ge1$: Player 1's first move takes $g=\max(N)$ (a legal choice since
$N$ is nonempty; if several elements tie for the max, any one of them, by
the tie-argument of Lemma 1). Player 2 then makes an *arbitrary* choice,
claiming some element $x_i$ of $N\setminus\{g\}$ (any position $i$, any
strategy — this is where adversariality enters, but the argument does not
need to know which $i$ Player 2 picks). After this, it is Player 1's turn
again, on the multiset $N\setminus\{g,x_i\}$ (size $m-2$, or $m-1$ if
$N\setminus\{g\}$ was already empty — trivial base case), with Player 1
again committed to greedy for all its remaining turns and Player 2 still
arbitrary. By the inductive hypothesis (applicable since $m-2<m$),
Player 1's total from this point on is
$\ge\mathrm{OddSum}(N\setminus\{g,x_i\})$. Hence Player 1's total overall is
$$\ge g+\mathrm{OddSum}\bigl(N\setminus\{g,x_i\}\bigr)=g+\mathrm{OddSum}\bigl((N\setminus\{g\})\setminus\{x_i\}\bigr)\overset{(\ast)}{\ge} g+\mathrm{EvenSum}(N\setminus\{g\})=\mathrm{OddSum}(N),$$
the last equality being the Global-max Peeling Lemma (Lemma 3). This holds
for the arbitrary $x_i$ Player 2 chose, so Player 1's guaranteed total is
$\ge\mathrm{OddSum}(N)$ against *any* Player-2 behavior, proving the first
statement. The second (Player 2 greedy, Player 1 arbitrary) follows by the
identical argument with the roles of "mover 1" and "mover 2" swapped
throughout (the induction never used which side moves first, only that the
greedy player moves on every one of its own turns); concretely, if Player 2
is the one committed to greedy, then after Player 1's arbitrary first move
$x_{i_1}$, Player 2 claims $g'=\max(N\setminus\{x_{i_1}\})$, and the same
computation with the sides swapped gives Player 2's total
$\ge\mathrm{OddSum}(N\setminus\{x_{i_1}\})$ at the next Player-2-first
subgame, which by $(\ast)$-type bookkeeping (applied with $N$ itself in
place of $N\setminus\{g\}$, and $x_{i_1}$ in place of $x_i$) gives
Player 2's total $\ge\mathrm{EvenSum}(N)$ overall. $\blacksquare$

**Attempted use, and why it fails.** The natural way to try to use Lemma 4
for Case 2 is: split the multiset $M=Q\cup Y$ (fragments $Q$ of $r_n$,
untouched-or-refined rest $Y$) and have LB commit to the *fixed* strategy
"$S$: always claim a currently-largest element of $Q$ while $Q$ is
nonempty; once $Q$ is exhausted, claim a currently-largest element of the
remainder." Lemma 4's induction adapts immediately to show LB's total
*collected from $Q$ alone*, under $S$, is $\ge\mathrm{OddSum}(Q)$ against
any XY behavior (the induction is identical, replacing "$N$" by "$Q$" and
noting XY's moves that claim from $Y$ instead of $Q$ only make Player 1's
job easier, since they leave $Q$ unchanged for the next application of the
inductive step — this sub-case was checked separately and is fine). The
gap is what happens with the *rest*: to reach the full target
$\mathrm{OddSum}(M)\ge r_n=\mathrm{sum}(Q)$ requires additionally that LB's
collection from $Y$ compensates for whatever XY manages to grab from $Q$
(precisely, if XY's total take from $Q$ is $S_b\le\mathrm{EvenSum}(Q)$,
one needs LB's take from $Y$ to be $\ge S_b$ as well) — and this
compensation **does not hold for the fixed strategy $S$**, because $S$ is
not, in general, an *optimal* strategy for LB: it can force LB to ignore a
very large piece of $Y$ in favor of a tiny remaining piece of $Q$, purely
because of the artificial "finish $Q$ first" priority.

This is not a vague worry — it is refuted by an exact computation. Take
$n=3$, $r_i=2^i/15$, and let XY split $r_3=8/15$ into four *equal*
fragments $2/15$ each (using all $3$ of its cuts on $r_3$, none on
$r_0,r_1,r_2$), so $Q=\{2/15,2/15,2/15,2/15\}$, $Y=\{1/15,2/15,4/15\}$. We
already know (Section 4, verified there by direct rational arithmetic)
that the **true value** $\mathrm{OddSum}(M)=9/15=0.6>c(3)=8/15$, so the
target inequality genuinely holds here. But an exact minimax computation
of the value LB obtains if it is *forced* to use strategy $S$ (Q-priority)
while XY plays optimally against that specific fixed strategy gives only
$0.4\overline{6}=7/15$, which is **strictly less than $c(3)=8/15$** (exact
game-tree computation, all $4!\cdot$ branching cases enumerated). So
strategy $S$ by itself does *not* guarantee the target bound — its floor
($7/15$) sits below $c(3)=8/15$ even though the true value ($9/15$) sits
comfortably above it. Concretely, the failure mode is: XY, given LB's
commitment to clear $Q$ first, deliberately claims the single largest
element of $Y$ ($4/15$) at its very first opportunity (rather than
contesting $Q$), and LB — bound by strategy $S$ — is not permitted to
respond by claiming $4/15$ itself even though $4/15$ is at that moment the
global maximum of the remaining pool; LB is instead forced to keep
grinding through the small, equal fragments of $Q$. This is precisely why
optimal LB play is the *global* greedy rule (Lemma 1), not a
Q-then-Y priority rule, and it shows that no proof of Case 2 can proceed
by fixing *any* one static priority order between $Q$ and $Y$ in advance —
the correct account must track the true interleaved sort order, exactly as
the outline's step 2–3 (piecewise-linearity / tie-block analysis) intended,
and exactly as flagged as the crux by the outline reviewer.

**Status of this sub-attempt.** Lemma 4 above is proved in full and is
genuinely new and reusable (it strengthens Lemma 1 from "greedy is optimal
between two optimal players" to "greedy guarantees the value against an
*arbitrary* opponent," a strictly stronger and more widely applicable
statement). But the specific composite strategy built from it
("Q-priority") is now a *documented dead end* for closing Case 2 — it
must not be retried in this or a similar static-priority form by a future
round. Closing Case 2 still requires the genuine interleaving analysis
(piecewise-linear structure of $\mathrm{OddSum}$ in the split of $r_n$,
breakpoints exactly at ties, using the certified generalized Tie-neutrality
block lemma face-by-face) that the outline called for; this analysis was
not completed this round due to time, and remains the open gap.

### 6. What remains open

1. **Lower-bound Case 2** (Sections 4, 4b): for $n\ge2$, when XY spends
   cuts on LB's own largest piece $r_n$, we have not proven
   $\mathrm{OddSum}(\text{final multiset})\ge c(n)$ for *every* such XY
   response — only exhibited the specific self-similar response that
   attains equality, and checked (numerically, exactly, via rational
   arithmetic at $n=2,3$) that several other specific responses (equal
   subdivision) give strictly more than $c(n)$, consistent with but not a
   proof of the general claim. **Round 2 update:** proved a new general
   reusable lemma (Lemma 4, "greedy-floor guarantee against an arbitrary
   opponent," Section 4b) but showed, with an exact computation, that the
   natural composite strategy built from it (LB statically prioritizing
   $Q$ = fragments of $r_n$ over $Y$ = the rest) is *not* strong enough to
   close this case — its guaranteed floor ($7/15$ at the $n=3$ equal-split
   example) sits strictly below $c(3)=8/15$ even though the true value
   ($9/15$) does not. This rules out any static-priority-strategy proof of
   Case 2 and confirms the gap genuinely requires the interleaved
   piecewise-linear / tie-block analysis the outline called for, not yet
   carried out.
2. **General upper bound** (arbitrary LB partition, not just the
   geometric one): not proven for $n\ge2$. Two natural "universal" XY
   strategies were tested and *refuted* as universal (though each is
   correct in some regime):
   - **Pure bisection of the current largest piece, repeated $n$ times**
     — refuted by the outline-reviewer's exact computation at $n=3$
     against LB's geometric construction, giving $0.6$ instead of the
     needed $\le 8/15\approx0.533$.
   - **Unconditional self-similar splitting of LB's largest piece into
     ratio $1:2:\cdots:2^n$** — this is exactly the response that works
     (with equality) against LB's own geometric construction (Section 4),
     but is refuted as a *universal* rule by the following exact
     counterexample at $n=1$: $p_1=0.9,\,p_2=0.1$. The self-similar split
     of $p_1$ gives fragments $(0.3,0.6)$, merged multiset
     $\{0.6,0.3,0.1\}$, $\mathrm{OddSum}=0.6+0.1=0.7>2/3$ — i.e. this
     response *fails* to hold LB below the target here, while the
     bisection response $(0.45,0.45)$ gives $\{0.45,0.45,0.1\}$,
     $\mathrm{OddSum}=0.45+0.1=0.55\le2/3$, i.e. bisection succeeds
     exactly where the self-similar split fails. The $n=1$ analysis in
     Section 5 shows the correct universal rule is the *threshold* rule
     "bisect $p_1$ if $p_1\ge2/3$, otherwise no cut is needed" — a
     genuinely case-dependent (adaptive) strategy, not a single fixed
     splitting pattern. Generalizing this adaptive threshold rule to
     arbitrary $n$ and arbitrary $k\le n+1$ pieces $p_1\ge\cdots\ge p_k$
     is the substance of the open upper-bound direction; it likely
     requires a two-parameter value function (LB pieces available vs. XY
     cuts remaining) tracked by strong induction, along the lines being
     pursued independently in the `self-similar-induction-on-n`
     approach — the two approaches' remaining gaps appear to be the same
     underlying difficulty viewed from two directions (multiset-merge vs.
     whole-game recursion), and closing either would very likely close
     both.

The formula $c(n)=2^n/(2^{n+1}-1)$ itself is not in doubt (proved exactly
for $n=0,1$; the lower-bound Case-1 argument plus the exact equality
witnesses at $n=2,3$ are strong, checkable evidence for general $n$); what
remains is the fully general two-directional inequality proof.

### 7. Round 3: the top-only-splitting sub-case of Case 2, narrowed and partly closed

This round's outline narrowed Lower-bound Case 2 to the **top-only-splitting
sub-problem**: LB's pieces $r_0,\dots,r_{n-1}$ are left completely
untouched by XY, and *all* of XY's $\le n$ cuts are spent splitting the
single top piece $r_n$ into $j+1$ positive fragments ($j\le n$). This
sub-problem is deliberately not "all of Case 2" (the general reduction
showing top-only is WLOG for the whole of Case 2 is `dyadic-potential-
invariant`'s task this round, not this file's) — everything below is
scoped strictly to this sub-problem.

Throughout this section it is more convenient to work **unnormalized**:
write $T:=2^n$ for the top piece and
$$\Gamma_{m-1}:=\{2^{m-1},2^{m-2},\dots,2^1,2^0\}\qquad(m\ge1;\ \Gamma_{-1}:=\varnothing),$$
an explicit $m$-element decreasing geometric sequence (LB's own tail,
$\Gamma_{n-1}=\{r_0,\dots,r_{n-1}\}$ scaled by $2^{n+1}-1$). By the scale
invariance already recorded in Section 2, proving
$\mathrm{OddSum}(A\cup\Gamma_{n-1})\ge 2^n$ for a positive partition $A$ of
$2^n$ is equivalent to the normalized statement
$\mathrm{OddSum}(\text{final multiset})\ge c(n)$ for this sub-problem, since
both sides scale by the same factor $1/(2^{n+1}-1)$.

**Target of this section.**
$$\textbf{(TOP-ONLY)}\qquad \mathrm{OddSum}(A\cup\Gamma_{n-1})\ \ge\ 2^n\quad\text{for every positive partition }A\text{ of }2^n\text{ into }\le n+1\text{ parts.}$$

#### 7.1 A companion identity (proved in full; promotable)

**Lemma 5 (Companion Peeling Lemma).** For any finite multiset $N$ of
positive reals with $g:=\max(N)$ (any one copy, if tied),
$$\mathrm{EvenSum}(N)=\mathrm{OddSum}(N\setminus\{g\}).$$

*Proof.* By the Global-max Peeling Lemma (Lemma 3),
$\mathrm{OddSum}(N)=g+\mathrm{EvenSum}(N\setminus\{g\})$. Also, trivially
(every element of $N$ sits at exactly one sorted rank, and every rank is
odd or even),
$$\mathrm{OddSum}(N)+\mathrm{EvenSum}(N)=\mathrm{sum}(N)=g+\mathrm{sum}(N\setminus\{g\})=g+\mathrm{OddSum}(N\setminus\{g\})+\mathrm{EvenSum}(N\setminus\{g\}).$$
Subtracting the first displayed equation from the second gives
$\mathrm{EvenSum}(N)=\mathrm{OddSum}(N\setminus\{g\})$. $\blacksquare$

(This uses only already-certified facts — Lemma 3 plus the elementary
$\mathrm{OddSum}+\mathrm{EvenSum}=\mathrm{sum}$ decomposition — so it is
itself fully rigorous with no new induction.)

#### 7.2 The Dominant-Chain Theorem (proved in full; closes a genuine sub-case of TOP-ONLY)

**Definition (Dominance-Chain property).** Fix an integer $m\ge -1$. A
finite descending sequence $a_1\ge a_2\ge\cdots\ge a_k>0$ ($k\ge0$) *has the
Dominance-Chain property at level $m$* if either
- $k=0$ (vacuously), or
- $k\ge1$, $m\ge0$, $a_1\ge 2^{m-1}$ (reading $2^{-1}:=0$ when $m=0$, so
  this is automatic when $m=0$), and $(a_2,\dots,a_k)$ has the
  Dominance-Chain property at level $m-1$.

This is a well-founded recursive definition: each unfolding strictly
decreases $k$, so it bottoms out after at most $k$ steps.

**Theorem 5 (Dominant-Chain Theorem).** Let $m\ge0$ and let
$a_1\ge\cdots\ge a_k>0$ ($k\ge0$) satisfy $\sum_i a_i\le 2^m$ and have the
Dominance-Chain property at level $m$. Then
$$\mathrm{OddSum}\bigl(\{a_1,\dots,a_k\}\cup\Gamma_{m-1}\bigr)\ \ge\ \sum_i a_i.$$

*Proof.* Strong induction on $k$.

*Base case $k=0$.* The left side is $\mathrm{OddSum}(\Gamma_{m-1})$, a sum
of finitely many positive reals (or the empty sum if $m=0$), hence $\ge0=\sum_i a_i$ (the empty sum). $\blacksquare$ (this case)

*Inductive step, $k\ge1$.* By the Dominance-Chain property, $a_1\ge
2^{m-1}$ (in particular $m\ge1$, since for $m=0$ we would need $k=0$ by the
definition's own case split unless $2^{-1}:=0$ is used and $a_1\ge0$
trivially — but then $\Gamma_{-1}=\varnothing$ and the "level $m-1=-1$"
recursive call on $(a_2,\dots,a_k)$ needs those to be empty too, i.e.
$k=1$; we handle $m=0,k=1$ directly: $\Gamma_{-1}=\varnothing$, left side
$=a_1=\sum a_i$, trivially $\ge$; so assume from here $m\ge1$, which is the
only case where the induction below is needed).

Write $A=\{a_1,\dots,a_k\}$, $A'=\{a_2,\dots,a_k\}$, $S=\sum_i a_i\le 2^m$,
$S'=\sum_{i\ge2}a_i=S-a_1$. Since $a_1\ge2^{m-1}$ and $S\le2^m$, we get
$$S'=S-a_1\le 2^m-2^{m-1}=2^{m-1}.$$
Because $a_2,\dots,a_k$ are positive and sum to $S'\le2^{m-1}$, each
individual $a_i$ ($i\ge2$) satisfies $a_i\le S'\le 2^{m-1}\le a_1$; and
every element of $\Gamma_{m-1}$ is $\le 2^{m-1}\le a_1$ as well. Hence
$$a_1=\max\bigl(A\cup\Gamma_{m-1}\bigr).$$
By the Global-max Peeling Lemma (Lemma 3),
$$\mathrm{OddSum}(A\cup\Gamma_{m-1})=a_1+\mathrm{EvenSum}\bigl(A'\cup\Gamma_{m-1}\bigr).\tag{7.1}$$
Next, since every element of $A'$ is $\le S'\le2^{m-1}$ and every element of
$\Gamma_{m-1}$ is $\le2^{m-1}$ with $2^{m-1}\in\Gamma_{m-1}$ itself attaining
this bound,
$$2^{m-1}=\max\bigl(A'\cup\Gamma_{m-1}\bigr).$$
By the Companion Peeling Lemma (Lemma 5) applied to $N=A'\cup\Gamma_{m-1}$
with $g=2^{m-1}$, and noting $N\setminus\{g\}=A'\cup\Gamma_{m-2}$ (removing
the single largest element $2^{m-1}$ from $\Gamma_{m-1}$ leaves exactly
$\Gamma_{m-2}$):
$$\mathrm{EvenSum}\bigl(A'\cup\Gamma_{m-1}\bigr)=\mathrm{OddSum}\bigl(A'\cup\Gamma_{m-2}\bigr).\tag{7.2}$$
Now $(a_2,\dots,a_k)$ has the Dominance-Chain property at level $m-1$ (by
definition of the property for $(a_1,\dots,a_k)$ at level $m$), has $k-1<k$
elements, and satisfies $\sum_{i\ge2}a_i=S'\le2^{m-1}$. By the inductive
hypothesis (applicable since $k-1<k$),
$$\mathrm{OddSum}\bigl(A'\cup\Gamma_{m-2}\bigr)\ \ge\ S'.\tag{7.3}$$
Chaining (7.1), (7.2), (7.3):
$$\mathrm{OddSum}(A\cup\Gamma_{m-1})=a_1+\mathrm{OddSum}(A'\cup\Gamma_{m-2})\ \ge\ a_1+S'=a_1+(S-a_1)=S=\sum_i a_i.$$
$\blacksquare$

**Corollary (closes a genuine sub-case of TOP-ONLY).** If XY's split
$a_1\ge\cdots\ge a_{j+1}>0$ of $2^n$ (i.e. $\sum a_i=2^n$, $j\le n$) has the
Dominance-Chain property at level $n$ — i.e. $a_1\ge2^{n-1}$, and (if
$a_1<2^n$, i.e. $j\ge1$) $a_2\ge2^{n-2}$, and so on down the chain, at
every level until the fragments are exhausted — then
$\mathrm{OddSum}(A\cup\Gamma_{n-1})\ge2^n$, i.e. this response does not beat
$c(n)$ for XY. In particular this covers, as a special case, the original
Case-1 theorem ($j=0$: the chain is trivially satisfied since $a_1=2^n\ge
2^{n-1}$ and the rest is empty), and — verified explicitly by direct
computation for $n=4$ (fractions $16/31,32/31,64/31,128/31,256/31$ against
tail $\{8,4,2,1\}$: successive ratios to $8,4,2,1,0.5$ are all $\ge1$, each
barely) — it also covers the specific self-similar equality-attaining
construction from Section 4 for every $n$ tested: the ratio
$a_{i}/2^{n-i}=2^n/(2^{n+1}-1)$ is the *same* constant $>1$ at every level
(since all fragments and all tail values are scaled by the identical
factor $2^n/(2^{n+1}-1)$ relative to the pure-power sequence
$2^n,2^{n-1},\dots$), so the chain condition holds at every level
simultaneously and with the same (minimal, level-independent) margin — this
is exactly why that construction is the tight case: it satisfies
Dominance-Chain everywhere with equality "spread evenly" rather than slack
anywhere, consistent with attaining $\mathrm{OddSum}=2^n$ exactly rather
than strictly more.

#### 7.3 The complementary regime: a proved decomposition tool, and a precise diagnosis of the remaining gap

The Dominant-Chain Theorem does **not** cover every split $A$: it fails
exactly when, at some level of the recursive peeling, the current largest
remaining fragment is *smaller* than the current tail's top value. We
record a general, unconditional structural lemma for this regime, prove it
in full, and use it to give a precise (not hand-waved) account of why it
does not by itself finish the argument — matching, independently, the exact
obstruction diagnosed this round by `self-similar-induction-on-n`'s own
"Recursive Depth Peeling Lemma" for its sub-case $a_1<2^{m-1}$.

**Lemma 6 (Prefix-Run Peeling Decomposition).** Let $m\ge1$, let
$a_1\ge\cdots\ge a_k>0$ ($k\ge0$), and let $d$ be an integer with
$1\le d\le m$ such that $a_1<2^{m-d}$ (vacuously true for every $d$ if
$k=0$). Write $\Gamma_{[m-d,\,m-1]}:=\{2^{m-1},2^{m-2},\dots,2^{m-d}\}$ (the
top $d$ elements of $\Gamma_{m-1}$) and let $\Gamma_{m-d-1}$ be the
remaining $m-d$ elements $\{2^{m-d-1},\dots,2^0\}$ (empty if $d=m$). Then
$$\mathrm{OddSum}\bigl(\{a_1,\dots,a_k\}\cup\Gamma_{m-1}\bigr)=\mathrm{OddSum}\bigl(\Gamma_{[m-d,\,m-1]}\bigr)+\begin{cases}\mathrm{OddSum}\bigl(\{a_1,\dots,a_k\}\cup\Gamma_{m-d-1}\bigr),& d\text{ even},\\[2pt]\mathrm{EvenSum}\bigl(\{a_1,\dots,a_k\}\cup\Gamma_{m-d-1}\bigr),& d\text{ odd}.\end{cases}$$

*Proof.* Write $A=\{a_1,\dots,a_k\}$ and $N=A\cup\Gamma_{m-1}$. Since
$a_1<2^{m-d}\le 2^{m-d+1}\le\cdots\le2^{m-1}$ and $a_1=\max(A)$, every
element of $A$ is strictly smaller than every element of
$\Gamma_{[m-d,m-1]}$. Also every element of $\Gamma_{[m-d,m-1]}$ is
$\ge2^{m-d}$, strictly larger than every element of $\Gamma_{m-d-1}$
(each $\le2^{m-d-1}<2^{m-d}$). Hence, in the descending sort of $N$, the
top $d$ positions are occupied *exactly* by $\Gamma_{[m-d,m-1]}$, in its own
sorted (descending, geometric) order, and the remaining positions
$d+1,\dots,d+k+(m-d)$ are occupied by the descending sort of the multiset
$R:=A\cup\Gamma_{m-d-1}$ — because every element assigned to these
positions is (by the two displayed strict/weak dominance facts) smaller
than every element of $\Gamma_{[m-d,m-1]}$ and the positions among
themselves are exactly sorted by the relative order within $R$ (nothing
from $\Gamma_{[m-d,m-1]}$ can appear among them, and nothing from $R$ can
appear among the first $d$).

Consequently $\mathrm{OddSum}(N)$ splits into a sum over the first $d$
positions (which is exactly $\mathrm{OddSum}(\Gamma_{[m-d,m-1]})$, since
these positions carry $\Gamma_{[m-d,m-1]}$'s own sorted values at its own
ranks $1,\dots,d$) plus a sum over the remaining positions. A position
$p=d+i$ (with $i=1,2,\dots$ indexing $R$'s own sorted rank) is odd in $N$'s
global numbering iff $i$ has the opposite parity to $d$ when $d$ is odd,
and the same parity as $i$ when $d$ is even — concretely: $p$ odd
$\iff d+i$ odd $\iff$ ($i$ odd, if $d$ even) or ($i$ even, if $d$ odd).
Hence the second sum equals $\mathrm{OddSum}(R)$ if $d$ is even, and
$\mathrm{EvenSum}(R)$ if $d$ is odd, which is exactly the claimed formula.
$\blacksquare$

**Why this does not (yet) close the complementary regime.** Apply Lemma 6
with the *maximal* valid $d$ for a given split (i.e. $d$ = the number of
consecutive top tail values exceeding $a_1$). If $d$ is even, the formula
reduces the problem to bounding $\mathrm{OddSum}(A\cup\Gamma_{m-d-1})$ from
below by (an amount that would need to be) $\sum a_i$ minus the known,
computable, nonnegative quantity $\mathrm{OddSum}(\Gamma_{[m-d,m-1]})$. The
obstruction is structural, not a missing computation: in the Dominant-Chain
regime (Section 7.2), each peeling step removed *both* one level of tail
**and** an amount of mass from $A$ that was provably $\ge$ half of the
current budget (since $a_1\ge2^{\text{level}-1}$ exactly matched the
budget the level-drop could "afford"), which is exactly what kept the
invariant "$\sum(\text{remaining }A)\le 2^{\text{remaining level}}$" alive
through the induction. In the complementary regime, Lemma 6's step removes
mass **only from the tail** ($\Gamma_{[m-d,m-1]}$) while leaving $A$
entirely untouched, dropping the tail level by $d\ge1$ without reducing
$\sum a_i$ at all — so the same invariant is violated in general (as it
must be: if $a_1$ is small relative to the tail, $\sum a_i$ can still be
close to $2^m$ even after the tail level has dropped to $m-d-1\ll m$, i.e.
$\sum a_i$ can exceed $2^{m-d}$, taking the reduced sub-problem *outside*
the range where the Dominant-Chain Theorem — or any comparably direct
induction we have found — applies). This is a genuine, verified structural
obstruction (confirmed numerically: brute-force search up to $10^5$ random
instances at $m=2,\dots,6$ finds no violation of the *overall* TOP-ONLY
target, so the full statement is true, but the natural bound needed to
finish this specific decomposition step — an EvenSum/OddSum lower bound on
$A\cup\Gamma_{m-d-1}$ with $\sum a_i$ allowed to exceed $2^{m-d}$ — is
**false** in the unrestricted form and requires exactly the kind of
budget-and-depth-coupled bookkeeping that `self-similar-induction-on-n`'s
own Recursive Depth Peeling Lemma is independently trying to formalize for
its identical sub-case. Two independent approaches hitting the same wall
from different framings this round is corroborating evidence that the
difficulty is real, not an avoidable gap in either write-up.

**A second, new negative check (extends the round-2 dead-end catalog).**
As a further sanity check, we tested whether the natural static
"tail-priority" LB strategy — the mirror image of the round-2 "Q-priority"
strategy: LB always claims the current maximum of the *known tail* while it
is nonempty, only claiming from the (adversary-controlled) fragments once
the tail is exhausted — can substitute for the missing bound. It cannot: an
exact game-tree computation (all branchings enumerated) at $n=3$, tail
$\{4,2,1\}$, fragments $\{3.9,3.9,0.2\}$ (a Dominance-Chain-violating split,
since $a_1=3.9<4=2^{n-1}$) gives a guaranteed floor of exactly $7$ under
tail-priority, strictly below the target $2^3=8$, even though the *true*
value ($\mathrm{OddSum}=8.9$, i.e. optimal greedy play) comfortably clears
it. Combined with round 2's Q-priority counterexample, **both** natural
static priority orders between "known tail" and "unknown fragments" are now
confirmed insufficient — this rules out the entire family of
fixed-priority LB strategies as a route to closing the complementary
regime, for any future attempt.

**Summary of this section's status.** The Dominant-Chain Theorem
(Theorem 5) gives a complete, rigorous proof of TOP-ONLY whenever XY's
split satisfies the Dominance-Chain property — a real, checkable, and
non-vacuous sub-case (it strictly contains the original Case-1 result and
provably contains the equality-attaining construction). The complementary
regime (some fragment fails to dominate the current tail top) is reduced,
via a fully proved general decomposition (Lemma 6), to a residual bound
that is diagnosed precisely to fail in the form tried, with the exact
mechanism of failure identified and cross-confirmed by an independent
approach's parallel finding — this is a real narrowing of the problem, not
a full solve of TOP-ONLY, and TOP-ONLY itself (let alone the un-narrowed
Case 2) remains open.

### 8. Round 4: a genuine "large violation depth" closure of the complementary regime

This section proves a new, fully rigorous theorem closing a real (eventually
non-vacuous, not merely formal) sub-case of the complementary regime left
open in Section 7.3, using the certified Prefix-Run Peeling Decomposition
Lemma (Lemma 6) together with a new elementary domination lemma and the
certified EvenSum-superadditivity dual of Lemma S. All notation is as in
Section 7: $\Gamma_{k}=\{2^k,\dots,2^0\}$ ($\Gamma_{-1}:=\varnothing$),
$T=2^m$ is the (unnormalized) top piece, and $A=\{a_1\ge\cdots\ge a_j>0\}$
is XY's split of $T$ into $j\le m+1$ fragments ($\sum a_i=2^m$).

#### 8.1 Two elementary tools, proved in full

**Lemma 7 (Odd–Even Domination).** For any finite multiset $N$ of positive
reals, $\mathrm{OddSum}(N)\ge\mathrm{EvenSum}(N)$.

*Proof.* Sort $N$ descending as $b_1\ge b_2\ge\cdots\ge b_k$ ($k\ge0$; the
claim is trivial, $0\ge0$, for $k=0$). If $k$ is even, pair
$(b_1,b_2),(b_3,b_4),\dots,(b_{k-1},b_k)$: each pair satisfies
$b_{2t-1}\ge b_{2t}$ since the list is sorted descending, so summing the
$k/2$ pairwise inequalities gives
$b_1+b_3+\cdots+b_{k-1}\ge b_2+b_4+\cdots+b_k$, i.e.
$\mathrm{OddSum}(N)\ge\mathrm{EvenSum}(N)$. If $k$ is odd, pair
$(b_1,b_2),\dots,(b_{k-2},b_{k-1})$ (the same way, leaving $b_k$
unpaired): summing gives $b_1+b_3+\cdots+b_{k-2}\ge b_2+\cdots+b_{k-1}
=\mathrm{EvenSum}(N)$, and $\mathrm{OddSum}(N)=(b_1+b_3+\cdots+b_{k-2})+b_k$
is this quantity plus the strictly positive extra term $b_k>0$, so again
$\mathrm{OddSum}(N)\ge\mathrm{EvenSum}(N)$ (in fact strictly, when $k$ is
odd and $N\ne\varnothing$). $\blacksquare$

**Lemma 7′ (Corollary: a floor for EvenSum in terms of the max).** For any
nonempty finite multiset $X$ of positive reals with $g=\max(X)$ (any one
copy, if tied) and $T'=\mathrm{sum}(X)$,
$$\mathrm{EvenSum}(X)\ \ge\ \frac{T'-g}{2}.$$

*Proof.* Write $X$ sorted descending as $x_1=g\ge x_2\ge\cdots\ge x_k$ and
let $B:=X\setminus\{x_1\}=(x_2,\dots,x_k)$, sorted descending, with
$\mathrm{sum}(B)=T'-g$. By definition $\mathrm{EvenSum}(X)=x_2+x_4+x_6+\cdots$.
Re-index $B$'s own sorted positions as $1,2,\dots,k-1$ (so $B$'s position
$t$ is $X$'s position $t+1$): a term $x_{t+1}$ of $X$ sits at an even
position of $X$ iff $t$ is odd, i.e. iff $x_{t+1}$ sits at an *odd* position
of $B$. Hence $\mathrm{EvenSum}(X)=\mathrm{OddSum}(B)$. By Lemma 7 applied to
$B$, $\mathrm{OddSum}(B)\ge\mathrm{EvenSum}(B)$, and since
$\mathrm{OddSum}(B)+\mathrm{EvenSum}(B)=\mathrm{sum}(B)=T'-g$, this gives
$2\,\mathrm{OddSum}(B)\ge T'-g$, i.e. $\mathrm{OddSum}(B)\ge(T'-g)/2$.
Combining, $\mathrm{EvenSum}(X)=\mathrm{OddSum}(B)\ge(T'-g)/2$. $\blacksquare$

**EvenSum-superadditivity (imported, one-line consequence of certified
Lemma S).** For any two finite multisets $P,Q$ of positive reals,
$\mathrm{EvenSum}(P\cup Q)\ge\mathrm{EvenSum}(P)+\mathrm{EvenSum}(Q)$.
*Derivation:* $\mathrm{OddSum}(X)+\mathrm{EvenSum}(X)=\mathrm{sum}(X)$ for
every finite multiset $X$ (every element sits at exactly one sorted rank,
odd or even), so
$\mathrm{EvenSum}(P\cup Q)=\mathrm{sum}(P)+\mathrm{sum}(Q)-\mathrm{OddSum}(P\cup Q)
\ge \mathrm{sum}(P)+\mathrm{sum}(Q)-\bigl(\mathrm{OddSum}(P)+\mathrm{OddSum}(Q)\bigr)
=\mathrm{EvenSum}(P)+\mathrm{EvenSum}(Q)$,
using certified Lemma S ($\mathrm{OddSum}(P\cup Q)\le\mathrm{OddSum}(P)+\mathrm{OddSum}(Q)$,
`lemmas/perfect-pairing-subadditivity-and-general-insertion.md`) in the
inequality step. $\blacksquare$

#### 8.2 Closed forms for $\mathrm{OddSum}/\mathrm{EvenSum}$ of geometric blocks

These are needed to make the final algebra exact rather than asymptotic.

**Fact G1.** For $k\ge-1$ (with $\Gamma_{-1}:=\varnothing$, sum/Odd/Even all
$0$),
$$\mathrm{OddSum}(\Gamma_k)=\begin{cases}\dfrac{2^{k+2}-1}{3}, & k\text{ even},\\[4pt]\dfrac{2^{k+2}-2}{3}, & k\text{ odd},\end{cases}\qquad
\mathrm{EvenSum}(\Gamma_k)=\begin{cases}\dfrac{2^{k+1}-2}{3}, & k\text{ even},\\[4pt]\dfrac{2^{k+1}-1}{3}, & k\text{ odd}.\end{cases}$$

*Proof.* $\Gamma_k$ has $k+1$ elements $2^k>2^{k-1}>\cdots>2^0$, already
sorted descending (all distinct, so no tie ambiguity). $\mathrm{OddSum}(\Gamma_k)
=\sum_{i=0}^{\lfloor k/2\rfloor}2^{k-2i}$, a finite geometric series with
ratio $1/4$ and $\lfloor k/2\rfloor+1$ terms starting at $2^k$. If $k$ is
even, the number of terms is $k/2+1$ and
$\sum_{i=0}^{k/2}2^{k-2i}=2^k\cdot\dfrac{1-4^{-(k/2+1)}}{1-1/4}
=\dfrac{4}{3}2^k\Bigl(1-\dfrac{1}{4\cdot2^k}\Bigr)=\dfrac{4\cdot2^k-1}{3}
=\dfrac{2^{k+2}-1}{3}$. If $k$ is odd, the number of terms is $(k+1)/2$ and
$\sum_{i=0}^{(k-1)/2}2^{k-2i}=2^k\cdot\dfrac{1-4^{-(k+1)/2}}{3/4}
=\dfrac{4}{3}2^k\Bigl(1-\dfrac{1}{2^{k+1}}\Bigr)=\dfrac{4\cdot2^k-2}{3}
=\dfrac{2^{k+2}-2}{3}$. In both cases,
$\mathrm{EvenSum}(\Gamma_k)=\mathrm{sum}(\Gamma_k)-\mathrm{OddSum}(\Gamma_k)
=(2^{k+1}-1)-\mathrm{OddSum}(\Gamma_k)$, giving the stated formulas by direct
substitution. (Base case $k=-1$: both sides $0$, consistent by convention.)
$\blacksquare$

*(Verified independently by brute-force sort-and-sum for $k=0,\dots,7$;
exact match.)*

**Fact G2 (OddSum of a prefix run).** For $0\le d\le m$,
$\Gamma_{[m-d,m-1]}:=\{2^{m-1},\dots,2^{m-d}\}$ ($d$ elements; empty if
$d=0$) satisfies
$$\mathrm{OddSum}\bigl(\Gamma_{[m-d,m-1]}\bigr)=\begin{cases}\dfrac{2^{m+1}-2^{m-d}}{3}, & d\text{ odd},\\[4pt]\dfrac{2^{m+1}-2^{m-d+1}}{3}, & d\text{ even}.\end{cases}$$

*Proof.* $\Gamma_{[m-d,m-1]}=2^{m-d}\cdot\Gamma_{d-1}$ (each element is
$2^{m-d}$ times the corresponding element of $\Gamma_{d-1}=\{2^{d-1},\dots,2^0\}$,
and scaling by a positive constant preserves sorted order, so
$\mathrm{OddSum}$ scales linearly — the scale-invariance fact already
recorded in Section 2). By Fact G1 with $k=d-1$: if $d$ is odd ($d-1$ even),
$\mathrm{OddSum}(\Gamma_{d-1})=(2^{d+1}-1)/3$, so
$\mathrm{OddSum}(\Gamma_{[m-d,m-1]})=2^{m-d}(2^{d+1}-1)/3=(2^{m+1}-2^{m-d})/3$.
If $d$ is even ($d-1$ odd), $\mathrm{OddSum}(\Gamma_{d-1})=(2^{d+1}-2)/3$, so
$\mathrm{OddSum}(\Gamma_{[m-d,m-1]})=2^{m-d}(2^{d+1}-2)/3=(2^{m+1}-2^{m-d+1})/3$.
$\blacksquare$

*(Verified independently by brute-force sort-and-sum for $m=3,\dots,11$,
all valid $d$; exact match.)*

#### 8.3 Theorem 6 (Large-Violation-Depth closure)

**Theorem 6.** Let $m\ge3$ and let $a_1\ge a_2\ge\cdots\ge a_j>0$ be a
partition of $2^m$ ($j\ge1$, $\sum a_i=2^m$). If
$$a_1<2^{m-3},$$
then
$$\mathrm{OddSum}\bigl(A\cup\Gamma_{m-1}\bigr)>2^m.$$
In particular this XY response does not beat $c(n)$ for $n=m$ in this
sub-case of TOP-ONLY (strictly, in fact — with room to spare).

*Proof.* Apply the certified Prefix-Run Peeling Decomposition Lemma
(Lemma 6, `lemmas/dominant-chain-theorem-and-prefix-run-decomposition.md`)
with $d=3$ (valid since $1\le3\le m$, using $m\ge3$, and $a_1<2^{m-3}$ is
exactly its hypothesis $a_1<2^{m-d}$). Since $d=3$ is odd, Lemma 6 gives
$$\mathrm{OddSum}(A\cup\Gamma_{m-1})=\mathrm{OddSum}\bigl(\Gamma_{[m-3,m-1]}\bigr)+\mathrm{EvenSum}\bigl(A\cup\Gamma_{m-4}\bigr).\tag{8.1}$$
By Fact G2 with $d=3$ (odd), $\mathrm{OddSum}(\Gamma_{[m-3,m-1]})=(2^{m+1}-2^{m-3})/3$.

For the second term, apply EvenSum-superadditivity (Section 8.1) with
$P=A$, $Q=\Gamma_{m-4}$:
$$\mathrm{EvenSum}(A\cup\Gamma_{m-4})\ \ge\ \mathrm{EvenSum}(A)+\mathrm{EvenSum}(\Gamma_{m-4}).\tag{8.2}$$
By Lemma 7′ applied to $X=A$ (nonempty, $g=a_1$, $T'=2^m$):
$$\mathrm{EvenSum}(A)\ \ge\ \frac{2^m-a_1}{2}\ >\ \frac{2^m-2^{m-3}}{2},\tag{8.3}$$
the last step strict since $a_1<2^{m-3}$ by hypothesis. By Fact G1 with
$k=m-4$ (valid as $m\ge3\Rightarrow m-4\ge-1$; if $m=3$, $\Gamma_{-1}=\varnothing$
and $\mathrm{EvenSum}=0$, consistent with the formula below at $k=-1$
interpreted via the $k$ odd branch giving $(2^0-1)/3=0$):
$$\mathrm{EvenSum}(\Gamma_{m-4})=\begin{cases}(2^{m-3}-2)/3,& m\text{ even (i.e. }m-4\text{ even)},\\(2^{m-3}-1)/3,& m\text{ odd.}\end{cases}\tag{8.4}$$

Combining (8.1)–(8.4),
$$\mathrm{OddSum}(A\cup\Gamma_{m-1})\ >\ \frac{2^{m+1}-2^{m-3}}{3}+\frac{2^m-2^{m-3}}{2}+\mathrm{EvenSum}(\Gamma_{m-4}).$$
It remains to check, for each parity of $m$, that the right side is
$\ge 2^m$ (which, combined with the already-strict inequality above, gives
the theorem's strict conclusion).

*Case $m$ even.* Using $\mathrm{EvenSum}(\Gamma_{m-4})=(2^{m-3}-2)/3$, the
right side (dropping the outer strict $>$ for a moment, to check the
non-strict inequality holds so that the genuine strict input above finishes
the job) equals, over a common denominator of $6$:
$$\frac{2(2^{m+1}-2^{m-3})+3(2^m-2^{m-3})+2(2^{m-3}-2)}{6}=\frac{2\cdot2^{m+1}+3\cdot2^m-3\cdot2^{m-3}-4}{6}.$$
We need this $\ge 2^m=\dfrac{6\cdot2^m}{6}$, i.e.
$$2\cdot2^{m+1}+3\cdot2^m-3\cdot2^{m-3}-4\ \ge\ 6\cdot2^m
\iff 4\cdot2^m+3\cdot2^m-3\cdot2^{m-3}-4\ge6\cdot2^m
\iff 2^m-3\cdot2^{m-3}\ge4
\iff 2^{m-3}(2^3-3)\ge4\iff 5\cdot2^{m-3}\ge4.$$
Since $m\ge3$ and $m$ even, $m\ge4$, so $2^{m-3}\ge2$, giving
$5\cdot2^{m-3}\ge10\ge4$. Holds (with room to spare).

*Case $m$ odd.* Using $\mathrm{EvenSum}(\Gamma_{m-4})=(2^{m-3}-1)/3$, the
same computation with $-2$ replaced by $-1$ gives, needing
$2^{m+1}\cdot2+3\cdot2^m-3\cdot2^{m-3}-2\ge6\cdot2^m$, i.e.
$$2^m-3\cdot2^{m-3}\ge2\iff5\cdot2^{m-3}\ge2.$$
Since $m\ge3$ and $m$ odd, $m\ge3$, so $2^{m-3}\ge1$, giving
$5\cdot2^{m-3}\ge5\ge2$. Holds.

In both cases the non-strict inequality
$$\frac{2^{m+1}-2^{m-3}}{3}+\frac{2^m-2^{m-3}}{2}+\mathrm{EvenSum}(\Gamma_{m-4})\ \ge\ 2^m$$
holds for every integer $m\ge3$, and combined with the strict input from
(8.3) ($\mathrm{EvenSum}(A)>(2^m-2^{m-3})/2$ strictly, not merely $\ge$),
the overall chain gives $\mathrm{OddSum}(A\cup\Gamma_{m-1})>2^m$ strictly,
for every $m\ge3$ and every valid split $A$ with $a_1<2^{m-3}$. $\blacksquare$

*(Independently cross-checked, not just by the symbolic algebra above but
also by direct brute-force computation: $36{,}611$ random instances with
$j\le m+1$ fragments and $a_1<2^{m-3}$, for $m=8,\dots,15$ — the first
range of $m$ where the hypothesis is non-vacuous, see below — every single
instance gives $\mathrm{OddSum}(A\cup\Gamma_{m-1})\ge2^m$, in fact strictly
greater in every trial, matching the theorem's strict conclusion; and the
closed-form parity computation above was checked by direct rational
(`Fraction`) arithmetic for $m=2,\dots,19$ against a brute-force
sort-and-sum of the actual multisets $\Gamma_{[m-d,m-1]}$ and $\Gamma_k$,
exact match in every case.)*

#### 8.4 Honest scope: vacuity range, and exactly why $d=1,2$ are not covered

**Vacuity for $m\le7$.** Recall (Section 7) $A$ has at most $m+1$ fragments
(XY has $\le n=m$ cuts to spend on $r_n$ within TOP-ONLY). By pigeonhole,
the largest fragment satisfies $a_1\ge\dfrac{2^m}{j}\ge\dfrac{2^m}{m+1}$.
Theorem 6's hypothesis $a_1<2^{m-3}$ can therefore hold only if
$\dfrac{2^m}{m+1}<2^{m-3}$, i.e. $m+1>2^3=8$, i.e. $m\ge8$. So Theorem 6 is
**vacuously true but asserts nothing new** for $3\le m\le7$ (no split $A$
satisfies its hypothesis in that range — every split of $2^m$ into $\le
m+1\le8$ parts automatically has $a_1\ge2^{m-3}$ there), and becomes a
genuine, non-vacuous closure of real instances starting exactly at $m=8$.
(Direct check at $m=8$: the fully equal split into $9$ parts,
$a_1=256/9\approx28.4<32=2^{8-3}=2^5$, satisfies the hypothesis with room
to spare, confirming non-vacuity concretely.)

**Why $d=1$ fails (not just "not proved" — the identical technique
genuinely does not close it).** Repeat the argument of Section 8.3 with
$d=1$ in place of $d=3$ (the only other odd choice possible before $d=3$,
requiring $a_1<2^{m-1}$). By Fact G2 with $d=1$ (odd),
$\mathrm{OddSum}(\Gamma_{[m-1,m-1]})=\mathrm{OddSum}(\{2^{m-1}\})=2^{m-1}$
(matches $(2^{m+1}-2^{m-1})/3=2^{m-1}(4-1)/3=2^{m-1}$). The residual bound
needed is $\mathrm{EvenSum}(A\cup\Gamma_{m-2})\ge2^m-2^{m-1}=2^{m-1}$, and the
superadditivity chain gives, using $a_1<2^{m-1}$ in Lemma 7′,
$$\mathrm{EvenSum}(A)+\mathrm{EvenSum}(\Gamma_{m-2})\ >\ \frac{2^m-2^{m-1}}{2}+\mathrm{EvenSum}(\Gamma_{m-2})=2^{m-2}+\mathrm{EvenSum}(\Gamma_{m-2}).$$
By Fact G1 with $k=m-2$: if $m$ is even ($k$ even),
$\mathrm{EvenSum}(\Gamma_{m-2})=(2^{m-1}-2)/3$, giving (common denominator
$6$) $2^{m-2}+\mathrm{EvenSum}(\Gamma_{m-2})=\dfrac{3\cdot2^{m-1}+2(2^{m-1}-2)}{6}=\dfrac{5\cdot2^{m-1}-4}{6}$;
comparing to the target $2^{m-1}=\dfrac{6\cdot2^{m-1}}{6}$, the margin is
$\dfrac{5\cdot2^{m-1}-4}{6}-2^{m-1}=\dfrac{-2^{m-1}-4}{6}$, which is
**strictly negative for every $m$**. If $m$ is odd ($k=m-2$ odd),
$\mathrm{EvenSum}(\Gamma_{m-2})=(2^{m-1}-1)/3$, giving margin
$\dfrac{5\cdot2^{m-1}-2}{6}-2^{m-1}=\dfrac{-2^{m-1}-2}{6}$, again strictly
negative for every $m$. In both parities the margin is
$-\Theta(2^{m-1})$, i.e. it does not merely fail to close but fails by an
amount growing exponentially with $m$ (exact values for $m=2,\dots,19$,
computed independently in rational arithmetic and matching these closed
forms term-by-term: $-1,-1,-2,-3,-6,-11,-22,-43,-86,-171,-342,-683,-1366,
-2731,-5462,-10923,-21846,-43691$). So $d=1$ is a **hard, provable failure**
of this specific technique for every $m$ — not an unproved case — because
the only inputs available (Lemma 7′'s floor on $\mathrm{EvenSum}(A)$, which
uses no information about $A$ beyond $\{a_1,\mathrm{sum}(A)\}$, and the
exact value of $\mathrm{EvenSum}(\Gamma_{m-2})$) are jointly insufficient by
a margin that grows, not shrinks, with $m$.

**Why $d=2$ (or any even $d$) is structurally inapplicable, not just
weaker.** For even $d$, Lemma 6's decomposition (8.1)-analogue produces a
residual term $\mathrm{OddSum}(A\cup\Gamma_{m-d-1})$ instead of an
$\mathrm{EvenSum}$ (Section 7.3's formula, parity-dependent). To lower-bound
an $\mathrm{OddSum}$ of a merge from below by the pieces' own OddSums would
require an *OddSum-superadditivity* statement,
$\mathrm{OddSum}(P\cup Q)\ge\mathrm{OddSum}(P)+\mathrm{OddSum}(Q)$ — but the
certified fact (Lemma S) is the *opposite* inequality,
$\mathrm{OddSum}(P\cup Q)\le\mathrm{OddSum}(P)+\mathrm{OddSum}(Q)$
(subadditivity), which is a genuine mathematical fact and not merely an
unproved-in-this-direction gap: OddSum-superadditivity is in general
**false** (e.g. $P=\{3\}$, $Q=\{2,1\}$: $\mathrm{OddSum}(P)+\mathrm{OddSum}(Q)
=3+2=5$ but $\mathrm{OddSum}(P\cup Q)=\mathrm{OddSum}(\{3,2,1\})=3+1=4<5$).
So the entire superadditivity-based mechanism of this section is
*mechanically inapplicable* at even violation depth, for a structural
reason (a true inequality happens to point the wrong way), not merely
because the specific numbers don't work out. Closing even-$d$ instances (or
$d=1$) requires a genuinely different tool — this is now a precisely
located, not vaguely diagnosed, boundary of what the peeling-plus-
superadditivity mechanism can reach.

**Net effect on the open gap.** Combined with the certified Dominant-Chain
Theorem (covers $a_1\ge2^{m-1}$, i.e. "$d=0$" in this language) and Theorem
6 above (covers $a_1<2^{m-3}$, i.e. $d\ge3$), the *only* remaining open
region of TOP-ONLY is
$$2^{m-3}\ \le\ a_1\ <\ 2^{m-1}\qquad(\text{violation depths }d\in\{1,2\}),$$
together with the recursive question of what happens to $a_2,\dots,a_j$
when $a_1$ falls in the covered range but the *rest* of the chain doesn't
dominate (Dominant-Chain requires domination all the way down, not just at
the top level; Theorem 6, by contrast, needs no domination assumption on
$a_2,\dots,a_j$ at all beyond their being sorted and part of the fixed-sum
$A$ — a strictly different, non-nested condition). This is a materially
smaller and more precisely bounded open region than "the whole complementary
regime" as reported after round 3, though it is **not** a closure of
TOP-ONLY in general, and TOP-ONLY (let alone the fully general Case 2)
remains open.

### 9. Round 5: the fully general Case 2 — a joint top-and-tail closure, and a precise obstruction

This section addresses the outline's pivot: instead of TOP-ONLY (all of XY's
cuts confined to the top piece $r_n$, i.e. $A=B$, $S=\Gamma_{m-1}$ exactly),
we now allow XY to spend $j$ cuts on the top piece **and** $c\ge1$ further
cuts on the tail, $j+c\le m$, producing an arbitrary refinement $S$ of
$\Gamma_{m-1}$ (i.e. $S=\bigcup_{i=0}^{m-1}S_i$ where each $S_i$ is a
positive partition of $2^i$, possibly the trivial one-part partition
$\{2^i\}$ itself). Throughout, "level $i$ is unsplit" means $S_i=\{2^i\}$
(a single piece); "level $i$ is split" means $|S_i|\ge2$. As before write
$B=\{b_1\ge\cdots\ge b_k>0\}$ ($k=j+1$) for XY's split of the top piece,
$\sum b_i=2^m$.

**A negative check first (rules out a natural shortcut).** One might hope
that refining the tail can only ever *help* LB, i.e.
$\mathrm{OddSum}(B\cup S)\ge\mathrm{OddSum}(B\cup\Gamma_{m-1})$ for every
refinement $S$ of $\Gamma_{m-1}$, which would immediately reduce the whole
of Case 2 to TOP-ONLY. This is **false**: an exact rational counterexample
at $m=6$, $B=\{64\}$ ($j=0$, top piece untouched), $S$ obtained by
splitting the levels $2$ and $3$ pieces each into two roughly-equal
fragments, gives $\mathrm{OddSum}(B\cup S)=52893/625=84.6288\ldots$ while
$\mathrm{OddSum}(B\cup\Gamma_5)=85$ exactly — strictly less, i.e. this
particular refinement genuinely *helps* XY (lowers LB's guaranteed total)
relative to leaving the tail alone. (Both values still comfortably exceed
the target $2^6=64$ here — $B=\{64\}$ is the trivial $j=0$ case, already
closed unconditionally for any tail refinement by the original Case 1
theorem, Section 4 — so this is *not* a counterexample to the true target,
only to the stronger monotonicity shortcut.) So no monotonicity argument can
shortcut Case 2 to TOP-ONLY; a genuine joint argument is required, exactly
as the outline anticipated.

#### 9.1 A general Domination Prefix-Run Lemma (proved in full; promotable)

**Lemma 8 (General Domination Prefix-Run Lemma).** Let $P=\{p_1\ge\cdots\ge
p_t\}$ ($t\ge0$) and $Q$ be finite multisets of positive reals with
$p_t\ge\max(Q)$ (every element of $P$ is $\ge$ every element of $Q$; the
condition is vacuous if $t=0$ or $Q=\varnothing$). Then
$$\mathrm{OddSum}(P\cup Q) = \mathrm{OddSum}(P) + \begin{cases}\mathrm{OddSum}(Q), & t\text{ even},\\ \mathrm{EvenSum}(Q), & t\text{ odd}.\end{cases}$$

*Proof.* Since every element of $P$ is $\ge$ every element of $Q$, in the
descending sort of $N:=P\cup Q$ the top $t$ positions are occupied exactly
by $P$, in $P$'s own sorted order (ties between $p_t$ and elements of $Q$,
if any, do not affect $\mathrm{OddSum}$: it sums *values* at each rank, and
tied values contribute the same sum to whichever rank they are assigned, by
the tie-invariance already established as part of Lemma 1 — swapping two
positions holding equal values leaves every rank's value, hence every partial
sum, unchanged). The remaining positions $t+1,\ldots,t+|Q|$ are occupied by
$Q$ in its own sorted order. A position $p=t+i$ (with $i$ indexing $Q$'s own
sorted rank $1,2,\ldots$) is odd in $N$'s global numbering iff $t+i$ is odd:
if $t$ is even this means $i$ odd, if $t$ is odd this means $i$ even. Hence
$\mathrm{OddSum}(N)=\mathrm{OddSum}(P)+\mathrm{OddSum}(Q)$ if $t$ is even, and
$\mathrm{OddSum}(N)=\mathrm{OddSum}(P)+\mathrm{EvenSum}(Q)$ if $t$ is odd.
$\blacksquare$

(This is a direct generalization of the certified Prefix-Run Peeling
Decomposition Lemma, Lemma 6 — that lemma is exactly the special case
$P=\Gamma_{[m-d,m-1]}$, $Q=A\cup\Gamma_{m-d-1}$; the proof above uses only
the domination hypothesis, not any geometric structure of $P$ or $Q$, so it
is a strictly more general, directly reusable tool.)

#### 9.2 The Joint Dominance-Chain Closure Theorem (top-levels-clear case)

**Theorem 7 (Joint Dominance-Chain Closure, top-levels-clear).** Let $m\ge0$
and $0\le k\le m$. Let $b_1\ge\cdots\ge b_k>0$ have the Dominance-Chain
property at level $m$ (Section 7.2's definition) with $\sum_i b_i\le2^m$.
Let $S$ be a refinement of $\Gamma_{m-1}=\{2^{m-1},\ldots,2^0\}$ (i.e.
$S=\bigcup_{i=0}^{m-1}S_i$, each $S_i$ a positive partition of $2^i$) such
that the top $k$ levels are unsplit: $S_i=\{2^i\}$ for every
$i\in\{m-1,m-2,\ldots,m-k\}$ (vacuous if $k=0$), while the remaining levels
$i=0,\ldots,m-k-1$ (if any) may be split arbitrarily. Then
$$\mathrm{OddSum}(\{b_1,\ldots,b_k\}\cup S)\ \ge\ \sum_i b_i.$$

*Proof.* Strong induction on $k$.

*Base case $k=0$.* $B=\varnothing$, so the left side is $\mathrm{OddSum}(S)$,
which is $\ge0=\sum_i b_i$ (empty sum) since $\mathrm{OddSum}$ of any
multiset of positive reals is a sum of nonnegative (indeed here, positive if
$S\ne\varnothing$) terms. $\blacksquare$ (this case)

*Inductive step, $k\ge1$ (so $m\ge1$, since $k\le m$).* Write $B=\{b_1,\ldots,b_k\}$,
$B'=\{b_2,\ldots,b_k\}$, $S'_{\text{mass}}:=\sum_i b_i-b_1$. By the
Dominance-Chain property, $b_1\ge2^{m-1}$. Also, exactly as in Theorem 5's
proof: every element of $B'$ is $\le\sum_i b_i-b_1\le2^m-2^{m-1}=2^{m-1}$
(using $\sum_i b_i\le2^m$).

By hypothesis level $m-1$ is unsplit, so $S$ contains the single element
$2^{m-1}$ (call it $g_1$) plus, from levels $m-2,\ldots,m-k$ (also unsplit,
$k-1$ further single elements, each $\le2^{m-2}<2^{m-1}$, vacuous list if
$k=1$) plus fragments from levels $0,\ldots,m-k-1$ (each such fragment is
$\le$ its own level's value $\le2^{m-k-1}\le2^{m-2}<2^{m-1}$, using $k\ge1$).
So every element of $S$ other than $g_1$ itself is $<2^{m-1}$. Combined with
every element of $B'$ being $\le2^{m-1}$, we get: $b_1\ge2^{m-1}\ge$ every
other element of $B\cup S$ (i.e. every element of $B'\cup S$), so
$b_1=\max(B\cup S)$. By the Global-max Peeling Lemma (Lemma 3),
$$\mathrm{OddSum}(B\cup S)=b_1+\mathrm{EvenSum}(B'\cup S).\tag{9.1}$$

Next, within $B'\cup S$: every element of $B'$ is $\le2^{m-1}=g_1$, and every
other element of $S$ is $<2^{m-1}=g_1$ (shown above). So $g_1=\max(B'\cup S)$.
By the Companion Peeling Lemma (Lemma 5),
$$\mathrm{EvenSum}(B'\cup S)=\mathrm{OddSum}\bigl((B'\cup S)\setminus\{g_1\}\bigr)=\mathrm{OddSum}(B'\cup S_{<m-1}),\tag{9.2}$$
where $S_{<m-1}:=S\setminus\{g_1\}$ is exactly the refinement of
$\Gamma_{m-2}=\{2^{m-2},\ldots,2^0\}$ induced by $S$'s own levels
$0,\ldots,m-2$ (unchanged from $S$ itself — removing the single unsplit
level-$(m-1)$ piece leaves precisely the rest).

Now $B'=(b_2,\ldots,b_k)$ has the Dominance-Chain property at level $m-1$
(by definition of the property for $B$ at level $m$), has $k-1$ elements
with $\sum_{i\ge2}b_i=\bigl(\sum_i b_i\bigr)-b_1\le2^m-2^{m-1}=2^{m-1}$, and
$S_{<m-1}$ is a refinement of $\Gamma_{m-2}$ whose top $k-1$ levels
($m-2,m-3,\ldots,m-k$) are unsplit by hypothesis — exactly the inductive
hypothesis's requirement with parameters $(m-1,k-1)$ in place of $(m,k)$
(valid since $k-1\le m-1$, as $k\le m$). By the inductive hypothesis,
$$\mathrm{OddSum}(B'\cup S_{<m-1})\ \ge\ \sum_{i\ge2}b_i.\tag{9.3}$$

Chaining (9.1), (9.2), (9.3):
$$\mathrm{OddSum}(B\cup S)=b_1+\mathrm{OddSum}(B'\cup S_{<m-1})\ \ge\ b_1+\sum_{i\ge2}b_i=\sum_i b_i.$$
$\blacksquare$

**Remark ($k=m+1$ boundary).** If $k=m+1$ (XY spends its *entire* budget on
the top piece, $j=m$), the hypothesis "top $\min(k,m)=m$ levels unsplit"
forces $S=\Gamma_{m-1}$ exactly (all $m$ levels of the tail unsplit, i.e.
$c=0$), and Theorem 7 reduces exactly to the already-certified Dominant-Chain
Theorem (Theorem 5). So Theorem 7 is a genuine strict generalization,
non-trivial precisely when $k\le m$ and $c\ge1$ (i.e. at least one tail
level, necessarily among the *bottom* $m-k$ levels, is actually split).

**Corollary (a real new closed region of the general Case 2).** For any
$j$ with $0\le j\le m$: if XY's split $B$ of the top piece into $j+1$
fragments has the Dominance-Chain property, and XY additionally spends any
number $c$ of cuts ($j+c\le m$) confined entirely to tail levels
$0,1,\ldots,m-j-2$ (i.e. avoiding the top $j+1$ tail levels
$m-1,\ldots,m-j-1$), distributed and split however it likes among those
lower levels, then $\mathrm{OddSum}(B\cup S)\ge2^m$ — this response does not
beat $c(n)$ for $n=m$. Combined with the original (unrefined-tail)
Dominant-Chain Theorem, this closes a genuinely two-dimensional slice of the
general Case 2 (a range of $j$ *and* a range of $c$-with-location
constraints simultaneously), not merely a single new point.

*(Independently cross-checked: 5,000 random instances with $m\in[1,8]$,
random dominance-chain $B$ of random length $k\in[1,m]$, and random
refinements confined to the bottom $m-k$ levels with random cut-count per
level, all give $\mathrm{OddSum}(B\cup S)\ge2^m$, zero violations, exact
rational arithmetic.)*

#### 9.3 How far the numeric evidence goes beyond the proved theorem

Theorem 7 requires the *specific* top $k$ levels to be entirely untouched.
The genuinely open question is whether the target still holds when a *top*
tail level (one of the levels $m-1,\ldots,m-k$) is itself split — the
"interleaved" case the outline's Joint Dominance-Chain sketch aimed at. We
tested this substantially beyond Theorem 7's proved scope:
- 30,000+ fully random trials (random $m\le8$, random dominance-chain $B$,
  random $j,c$ with $j+c\le m$, random unrestricted distribution of the $c$
  tail cuts among *all* $m$ levels, not just the bottom ones) — zero
  violations of the target $\mathrm{OddSum}(B\cup S)\ge2^m$.
- A `scipy` Nelder–Mead adversarial search targeting the single *tightest*
  boundary configuration found (the $k=2$ case, $b_1=b_2=2^{m-1}$ exactly,
  where Theorem 7 gives equality-adjacent behavior at the boundary), over
  every choice of "which single tail level to concentrate the split on" and
  "how many cuts to use there" (up to $6$ cuts per level, $m$ up to $11$) —
  in every case the found minimum margin over $2^m$ is exactly $0$ (never
  negative, matching the exact equality cases already known, e.g. the
  self-similar equality-attaining XY response of Section 4).

This is strong, honest evidence that the **full joint conjecture** — "if $B$
has the Dominance-Chain property, $\mathrm{OddSum}(B\cup S)\ge2^m$ for
*every* refinement $S$ of $\Gamma_{m-1}$, regardless of which levels are
split" — is true. It is **not proved**; Theorem 7 proves only the
"top-levels-clear" sub-case. We record precisely, below, why the natural
attempt to extend the proof technique to the interleaved case does not go
through, rather than asserting the extension works.

#### 9.4 The Leftover-Fragment Obstruction (a precise, proved diagnosis, not a full closure)

Suppose we try to extend Theorem 7's proof by allowing level $m-1$ itself to
be split, say into fragments with largest value $\mu_1<2^{m-1}$. The first
step (peeling $b_1$) still goes through unchanged, *provided* $b_1$ is still
the global max — this requires $b_1\ge\mu_1$ (as well as $b_1\ge2^{m-1}$'s
weaker consequence $b_1\ge$ every element of $B'$, established as before);
since $\mu_1<2^{m-1}\le b_1$, this holds automatically. So (9.1) survives
verbatim: $\mathrm{OddSum}(B\cup S)=b_1+\mathrm{EvenSum}(B'\cup S)$.

The obstruction appears at the *second* step. To continue via Companion
Peeling we need to identify $\max(B'\cup S)$. If $\mu_1\ge$ every element of
$B'$ (i.e. $\mu_1\ge\sum_{i\ge2}b_i$, a genuine extra hypothesis not implied
by anything so far, since $\mu_1$ can be made arbitrarily small — e.g. level
$m-1$ split as $(2^{m-1}-\varepsilon,\varepsilon)$ gives $\mu_1$ close to
$2^{m-1}$, but split as many small equal pieces gives $\mu_1$ close to $0$),
we may still peel $g=\mu_1$ via Companion Peeling:
$$\mathrm{EvenSum}(B'\cup S)=\mathrm{OddSum}\bigl(B'\cup(S\setminus\{\mu_1\})\bigr).$$
But now $S\setminus\{\mu_1\}$ is **not** a refinement of a smaller $\Gamma$:
it still contains the *rest* of level $m-1$'s fragments (the other pieces
that made up the split of $2^{m-1}$, summing to $2^{m-1}-\mu_1>0$, mixed
in among levels $0,\ldots,m-2$'s own fragments) in addition to the genuine
lower-level fragments. This residual object has no clean recursive shape:
it is not $B''\cup(\text{refinement of }\Gamma_{m-2})$ for any smaller
instance of the *same* hypothesis class Theorem 7 was stated for (Dominance-
Chain $B''$ plus a "top-levels-clear" refinement) — the leftover mass
$2^{m-1}-\mu_1$ sits at some *unknown* rank relative to $B''$'s own elements
and the lower tail levels, generically requiring exactly the kind of
"unknown interleaving" analysis this whole line of approaches has
repeatedly identified as the genuine difficulty (Section 4b, Section 7.3).
This is not the *same* obstruction as Proposition C (that was a same-size
recursive loop under scalar peel-and-recurse); here $m$ strictly decreases
at every step and the recursion terminates finitely — the obstruction is
instead that **the residual sub-problem, after peeling into a partially-split
top level, leaves the hypothesis class itself** (an inserted "generic
leftover" element is a strictly harder object than "a clean refinement of a
smaller $\Gamma$"), so no *direct* induction on Theorem 7's exact statement
closes it; a strengthened statement (e.g. tracking the leftover mass as an
extra free parameter, bounded by an explicit inequality, and reproving the
induction with this extra parameter present) would be needed, and this was
not carried out this round. We record this as the **Leftover-Fragment
Obstruction** — a genuine, precisely located gap, not a vague "still open."

**Net effect.** Theorem 7 is a real, unconditional closure of a
two-dimensional new region of the general Case 2 (Section 9.2's Corollary).
The fully general joint case — allowing *any* level, including the top
ones, to be split — remains open, with the exact mechanism of difficulty
(the Leftover-Fragment Obstruction) now precisely identified rather than
merely diagnosed as "the interleaving is hard." This is genuine progress on
this round's assigned target (the fully general Case 2, distinct from and
not dependent on `self-similar-induction-on-n`'s Case-B(m,k), which
concerns only TOP-ONLY): the theorem strictly extends coverage beyond
TOP-ONLY into the truly joint regime, closing it whenever the tail cuts
avoid the top tail-levels matched to $B$'s own length, while honestly
reporting that the interleaved sub-case (top tail levels also split) is not
yet closed and identifying precisely what a future attempt needs
(a strengthened induction carrying the leftover-fragment mass as an
explicit extra parameter).


### 10. Round 6: toward Theorem 7'(m,k;L) — the base case closed, the general
step reduced to two sharply-located residual sub-problems

This round's target (per the outline) is to extend Theorem 7 to allow the
top tail level $2^{m-1}$ itself — the *first* level Theorem 7 required
untouched — to be split, tracking the leftover mass
$L:=2^{m-1}-\mu_1$ (where $\mu_1$ is the largest fragment of that level's
split, and "rest" is an arbitrary-shape multiset of positive reals summing
to $L$) as an extra parameter. All other hypotheses of Theorem 7 are kept:
levels $m-2,\dots,m-k$ remain unsplit, levels $0,\dots,m-k-1$ may be split
arbitrarily as before.

**Numeric reconnaissance first (per the outline's own instruction).** Before
attempting any proof we numerically pinned down $f(L)$ (the conjectural
degradation) by exact rational-arithmetic minimization over the shape of
the split of level $m-1$ (equal-piece splits into $1,\dots,30$ parts, plus
several unequal two-piece splits, at a fine grid of $L$ values), for the
single hardest instance identified by round 5's own adversarial search —
$k=2$, $b_1=b_2=2^{m-1}$ exactly (zero slack in the Dominance-Chain
budget) — at $m=4,\dots,8$. Result: **the worst-case margin
$(\,b_1+b_2-\min\mathrm{OddSum}\,)$ found is $\le0$ at every $m$ tested**
(exactly $0$ at $m=4$, attained by splitting $2^{m-1}=8$ into $\{4,2,2\}$;
strictly negative, i.e. comfortable slack, at $m=5,6,7,8$). No violation of
the un-degraded target $\mathrm{OddSum}(B\cup S)\ge\sum b_i$ was found in
this restricted "split only the designated top tail level" scenario, at
any $m$ or any tested shape. This is a genuinely different (and finer)
search than round 5's, which allowed the split to sit at *any* single tail
level; restricting specifically to level $m-1$ (the level actually named
in the Leftover-Fragment Obstruction) still gives margin $\ge0$
throughout. **This is evidence that $f(L)\equiv0$ — i.e. no degradation at
all — is the true fact, not merely a conjectural bound; we record what we
could prove of this below, honestly marking what remains open.**

#### 10.1 Theorem 7a (the $k=1$ base case, proved in full, unconditional)

**Theorem 7a.** Let $m\ge1$ and let $b_1\ge2^{m-1}$ be a single value
(so $k=1$, trivially satisfying the Dominance-Chain property). Let $S$ be
*any* refinement of $\Gamma_{m-1}$ whatsoever — every level $0,\dots,m-1$
may be split in any shape, with no restriction (this is strictly more
general than "only level $m-1$ split," since it allows every level to be
split). Then
$$\mathrm{OddSum}(\{b_1\}\cup S)\ \ge\ b_1.$$

*Proof.* Every element of $S$ is a fragment of some level $i\le m-1$,
hence has value $\le2^i\le2^{m-1}\le b_1$. So $b_1=\max(\{b_1\}\cup S)$. By
the Global-max Peeling Lemma (Lemma 3),
$$\mathrm{OddSum}(\{b_1\}\cup S)=b_1+\mathrm{EvenSum}(S)\ \ge\ b_1,$$
since $\mathrm{EvenSum}$ of any multiset of positive reals is $\ge0$.
$\blacksquare$

This is the $L\in[0,2^{m-1})$ continuum's $k=1$ case of Theorem 7' in
full: $f(L)=0$ identically, for *every* possible split of level $m-1$ (not
just the two-fragment $(\mu_1,\text{rest})$ shape), and moreover it needs
no restriction on the other levels either — it is a genuine unconditional
strengthening (this is consistent with, and gives an independent
re-derivation in the DC/$\Gamma$ formalism of, the original Case‑1 Theorem
of Section 4, now shown to require only $b_1\ge2^{m-1}$ rather than the
top piece being exactly $2^m$ and completely unsplit). This closes the
$k=1$ instance of Theorem 7'$(m,k;L)$ completely, with $f\equiv0$, for
every $m\ge1$ and every $L$.

#### 10.2 The $k\ge2$ inductive step: an exact two-way reduction to two open sub-problems

Assume $k\ge2$. Write $B=\{b_1,\dots,b_k\}$, $B'=\{b_2,\dots,b_k\}$,
$S'_{\mathrm{mass}}:=\sum_ib_i-b_1$, and let $S$ be a refinement of
$\Gamma_{m-1}$ in which level $m-1$ is split into $\mu_1$ (its largest
fragment) plus a "rest" multiset $R_1$ of arbitrary shape with
$\mathrm{sum}(R_1)=L=2^{m-1}-\mu_1$, levels $m-2,\dots,m-k$ are unsplit
(single elements $2^{m-2},\dots,2^{m-k}$), and levels $0,\dots,m-k-1$ are
split arbitrarily. We attempt to prove
$\mathrm{OddSum}(B\cup S)\ge\sum_ib_i$.

**Step 1 (peel $b_1$; identical to Theorem 7, no leftover issue here).**
Exactly as in the Leftover-Fragment Obstruction's own diagnosis (Section
9.4): since $\mu_1<2^{m-1}\le b_1$ and every other element of $B'\cup S$ is
$\le\max(S'_{\mathrm{mass}},\mu_1)\le2^{m-1}\le b_1$ (using
$S'_{\mathrm{mass}}=\sum_ib_i-b_1\le2^m-2^{m-1}=2^{m-1}$, from
$\sum_ib_i\le2^m$ and $b_1\ge2^{m-1}$), $b_1=\max(B\cup S)$, so by Lemma 3
$$\mathrm{OddSum}(B\cup S)=b_1+\mathrm{EvenSum}(B'\cup S).\tag{10.1}$$
It remains to show $\mathrm{EvenSum}(B'\cup S)\ge\sum_{i\ge2}b_i=:S'$.

**Step 2 (exact case split on $\mu_1$ vs. $b_2$ — both branches derived in
full, both terminate in a precisely stated open residual).** Write
$T:=B'\cup S$. Since every element of $T$ other than $\mu_1,b_2,\dots,b_k$
is $<2^{m-1}$ and $\le\max(\mu_1,2^{m-2})$ (levels $m-2,\dots,m-k$ unsplit
are $\le2^{m-2}$, lower levels and $R_1$ are $\le\mu_1$ or $\le2^{m-k-1}$),
$\max(T)\in\{\mu_1,b_2\}$ exactly (whichever is larger). This gives an
exhaustive, disjoint two-way split of the inductive step, both branches of
which are carried out below to the point of an exact identity plus a
precisely named residual bound — not merely asserted.

**Subcase (a): $\mu_1\ge b_2$.** Then, since $b_2\ge2^{m-2}$ (Dominance-
Chain property of $B'$ at level $m-1$) and $\mu_1\ge b_2\ge2^{m-2}$,
$\mu_1$ dominates every element of $B'\cup S\setminus R_1$ (all
$\le2^{m-2}\le\mu_1$) as well as every element of $R_1$ itself (each
$\le\mu_1$ by definition of $\mu_1$ as the largest level-$(m-1)$
fragment); hence $\mu_1=\max(T)$. By the Companion Peeling Lemma
(Lemma 5),
$$\mathrm{EvenSum}(T)=\mathrm{OddSum}\bigl(T\setminus\{\mu_1\}\bigr)=\mathrm{OddSum}\bigl(B'\cup R_1\cup S''\bigr),\tag{10.2a}$$
where $S'':=$ (levels $m-2,\dots,m-k$ unsplit) $\cup$ (levels
$0,\dots,m-k-1$, arbitrary) is *exactly* a refinement of $\Gamma_{m-2}$
whose top $k-1$ levels are unsplit — i.e. $(B',S'')$ is precisely a
Theorem‑7 instance at parameters $(m-1,k-1)$ with **zero** leftover
($B'$ has the Dominance-Chain property at level $m-1$, $\sum_{i\ge2}b_i\le2^{m-1}$).
By the already-certified Theorem 7 itself,
$$\mathrm{OddSum}(B'\cup S'')\ \ge\ S'.\tag{10.3a}$$
So what remains is exactly: does *inserting* the extra arbitrary-shape
multiset $R_1$ (sum $L$, each element $\le\mu_1$) into an object that
*already* satisfies Theorem 7's bound (possibly with slack) preserve the
bound? We name this precisely:

> **Open Sub-Problem A (Insertion-Robustness of Theorem 7).** If
> $(B',S'')$ is any instance satisfying Theorem 7's hypotheses at
> $(m-1,k-1)$ (so $\mathrm{OddSum}(B'\cup S'')\ge S'$ is already known),
> and $R_1$ is an arbitrary finite multiset of positive reals with
> $\mathrm{sum}(R_1)=L$ and $\max(R_1)\le\mu_1$, is
> $\mathrm{OddSum}(B'\cup S''\cup R_1)\ge S'$ still?

This is **not** an instance of the general "refining the tail can only
help" claim already disproved in Section 9 (that concerned *re-splitting*
existing mass within a fixed-sum multiset, which can lower $\mathrm{OddSum}$
by an exact, verified counterexample); here $R_1$ is *additional* mass
with no counterpart already in $B'\cup S''$, a structurally different
question, and it is neither proved nor disproved in this file. A quick
single-insertion sanity check (inserting one new value $x$ into a sorted
list, tracked via the sorted-position parity argument that underlies
Lemma 1's inequality $(\ast)$) shows an *individual* inserted value can
only ever *decrease* $\mathrm{OddSum}$ by an amount bounded by the value
of the list-element it displaces into an even slot — never by more than
$x$ itself — but chaining this bound over an arbitrary number of inserted
pieces of $R_1$, each potentially degrading the position of the next, was
not carried out rigorously this round; we do not claim a proof of Open
Sub-Problem A.

**Subcase (b): $\mu_1<b_2$.** Then $b_2=\max(T)$ (since $\mu_1<b_2$ and
every other element of $T$ is $\le\max(\mu_1,2^{m-2})\le b_2$, using
$b_2\ge2^{m-2}$). By Companion Peeling,
$$\mathrm{EvenSum}(T)=\mathrm{OddSum}\bigl(T\setminus\{b_2\}\bigr)=\mathrm{OddSum}\bigl(B''\cup\{\mu_1\}\cup R_1\cup S''\bigr),\tag{10.2b}$$
where $B'':=\{b_3,\dots,b_k\}$ ($k-2$ elements, Dominance-Chain property
at level $m-2$ inherited from $B'$'s own definition) and $S''$ is as
above. The needed bound is now
$$\mathrm{OddSum}\bigl(B''\cup\{\mu_1\}\cup R_1\cup S''\bigr)\ \ge\ S'=b_2+\sum_{i\ge3}b_i.\tag{10.3b}$$
This is **not** a clean instance of Theorem 7 at $(m-2,k-2)$: the target
$S'$ exceeds $\mathrm{sum}(B'')=\sum_{i\ge3}b_i$ by exactly $b_2$, and the
extra mass $\{\mu_1\}\cup R_1$ (total $2^{m-1}$, i.e. exactly one full
level's worth) must supply that deficit. We name this precisely as well:

> **Open Sub-Problem B (Level-Absorption).** With $B''$ (Dominance-Chain
> at level $m-2$, $\mathrm{sum}(B'')\le2^{m-2}$) and $S''$ a refinement of
> $\Gamma_{m-2}$ with top $k-2$ levels unsplit, and $\{\mu_1\}\cup R_1$ an
> arbitrary split of the value $2^{m-1}$ (i.e. a full extra "level" of
> mass, with $\mu_1<b_2$ but otherwise arbitrary shape), is
> $\mathrm{OddSum}(B''\cup\{\mu_1\}\cup R_1\cup S'')\ \ge\ b_2+\mathrm{sum}(B'')$?

We observe (but do not prove) that Sub-Problem B "morally" resembles
re-inserting a whole extra dominance-chain level ($\{\mu_1\}\cup R_1$
summing to $2^{m-1}$, comparable in scale to $b_2\ge2^{m-2}$) into a
smaller Theorem‑7 instance and asking the target to absorb $b_2$ using
that inserted mass — plausible given the numeric evidence of Section
10 preamble, but genuinely different in shape from Sub-Problem A (there
the extra mass $R_1$ was "free," here it is exactly what must supply the
extra $b_2$ in the target), so it is recorded as a separate open item, not
conflated with Sub-Problem A.

**Net effect of Section 10.2.** The inductive step of Theorem 7' for
$k\ge2$ is not closed, but it is no longer a single vague "unknown
interleaving": it has been reduced, via two *exact* identities
((10.2a)/(10.2b), both fully derived, not asserted) covering an
exhaustive and disjoint case split ($\mu_1\ge b_2$ vs. $\mu_1<b_2$), to
two precisely stated residual claims (Sub-Problems A and B), each strictly
narrower and more specific than the Leftover-Fragment Obstruction's
original diagnosis (Section 9.4), and each independently well-defined
enough to be attacked or numerically stress-tested on its own in a future
round. Both remain unproved.

#### 10.3 Comparison with self-similar-induction-on-n's $G(m,k;V)$

Per this round's explicit dispatch instruction to check for literal
duplication: self-similar-induction-on-n's $V$-parametrization concerns a
*target-value* perturbation of Case-B$(m,k)$ (TOP-ONLY, tail completely
untouched by construction, target reduced from $2^m$ to
$2^{m-1}+\varepsilon$). The object here, Theorem 7'$(m,k;L)$, concerns a
*structural* perturbation (the tail is no longer untouched — one specific
tail level is split, target unchanged at $\sum b_i$). These remain
genuinely different objects, as the outline-reviewer anticipated; the two
open sub-problems isolated here (Insertion-Robustness, Level-Absorption)
have no evident restatement in terms of $G(m,k;V)$'s eps-halving
recursion, so **no duplication is found this round** — this is recorded
per the outline's STOP-and-import instruction, which does not trigger.

**Numeric evidence supporting the file, in full:** the exact rational
computation supporting Theorem 7a and the Section 10 preamble's $f(L)\le0$
claim is reproducible directly (equal-piece and two-piece-unequal
splits of level $m-1$, exact `Fraction` arithmetic, $m=3,\dots,8$, both
the general $k=1$ case and the $k=2$ tight-boundary case
$b_1=b_2=2^{m-1}$); zero violations found in any configuration tested.

**Correction (round 7, see Section 11.1 below): this preamble's claim
"$f(L)\equiv0$ is the true fact" is false as an unconditional statement.**
Round 6's search restricted the refinement to splitting only *one* tail
level at a time (the level named in the Leftover-Fragment Obstruction),
leaving every other level of the tail exactly as $\Gamma_{m-1}$. Round 7
found that allowing *several* levels to be split simultaneously (still
fully within Section 10's own stated hypothesis, "levels $0,\dots,m-k-1$
may be split arbitrarily") produces an exact counterexample family with
margin $-1/2$, for every $m\ge3$. The precise cause and the corrected,
cut-budget-aware statement are given in Section 11.1.

### 11. Round 7: stress-testing before proof — a real bug found and fixed
in Level-Absorption's statement; Insertion-Robustness corroborated more
broadly but still unproved

Per the outline's explicit instruction this round, both round-6 open
sub-problems are stress-tested numerically *before* any proof attempt:
Level-Absorption first (it was completely untested in round 6), then
Insertion-Robustness extended to genuine $k'\ge2$ instances (round 6's own
test family, $k'=1$, is structurally incapable of ever violating the claim
— by Theorem 7a's own unconditional $f\equiv0$ result for $k=1$, $S'$'s
side of the inequality has zero slack budget to lose, so a $k'=1$ test can
only ever confirm, never refute).

#### 11.1 Level-Absorption: false as boxed, corrected by a missing
cut-budget hypothesis, then re-confirmed by 90,000 fresh trials

**The bug.** Round 6's boxed Open Sub-Problem B places no bound on how many
pieces $R_1$ (or the arbitrarily-split lower tail levels) may be cut into.
Testing this literally, an exact rational search (script:
`/tmp/round-7/stress_test.py`, `test_B`) found genuine violations — not
numerical noise, margins as large as $-0.44$ — all at the smallest
instance size $m=3,k=2$ in the initial random search. Generalizing and
cleaning up the found counterexample by hand gives an exact, fully general
family:

> **Counterexample family (exact, all $m\ge3$).** Take $k=2$,
> $b_1=b_2=2^{m-1}$ (Dominance-Chain at level $m$: $b_1=2^{m-1}$ meets the
> bound with equality, $b_2=2^{m-1}\ge2^{(m-1)-1}=2^{m-2}$; $\sum
> b_i=2^m$, meeting the sum cap with equality). Split level $m-1$
> ($=2^{m-1}$) as $\mu_1=2^{m-2}$ plus $R_1=\{2^{m-3},2^{m-3}\}$; leave
> level $m-2$ unsplit ($=2^{m-2}$); bisect *every* level
> $i=0,\dots,m-3$ into two equal pieces $2^{i-1},2^{i-1}$.

*Exact verification (worked by hand, re-checked by exact `Fraction`
arithmetic for $m=3,4,5,6,8,10$, identical result every time).* Every
distinct power-of-two value from $2^{m-1}$ down to $2^{-1}$ appears with
multiplicity exactly $2$ in the resulting multiset $B\cup S$ (the two
copies of $2^{m-1}$ from $B$; $2^{m-2}$ from $\mu_1$ and the unsplit level
$m-2$; $2^{m-3}$ from the two pieces of $R_1$; $2^{i-1}$ (twice) from
bisecting level $i$, for each $i=m-3,\dots,0$). Sorted descending, each
value occupies two consecutive ranks $(2j-1,2j)$; only the first (odd)
rank of each pair counts toward $\mathrm{OddSum}$, so
$$\mathrm{OddSum}(B\cup S)=\sum_{i=-1}^{m-1}2^i=2^m-\tfrac12<2^m=\sum_i b_i,$$
an exact deficit of $\mathbf{1/2}$, for *every* $m\ge3$. (Worked example,
$m=3$: multiset
$\{4,4\}\cup\{2,1,1\}\cup\{2\}\cup\{0.5,0.5\}=\{4,4,2,2,1,1,0.5,0.5\}$,
sorted $4,4,2,2,1,1,0.5,0.5$; $\mathrm{OddSum}=4+2+1+0.5=7.5=8-0.5$.)

**Why this is not a counterexample to the real game (the missing
hypothesis, found and diagnosed).** Counting cuts: splitting the top piece
$2^m$ into $B=\{b_1,b_2\}$ costs $1$ cut; splitting level $m-1$ into
$\{\mu_1\}\cup R_1$ (3 pieces) costs $2$ cuts; level $m-2$ unsplit costs
$0$; bisecting each of the $m-2$ levels $0,\dots,m-3$ costs $1$ cut each.
Total: $1+2+0+(m-2)=m+1$ cuts — **one more than the real game's budget of
$\le n=m$ total cuts** for the whole response
(`lemmas/reduction-to-multiset-minimax.md`: "$\le n$ further cuts"). This
is exactly the same class of bug this round's `self-similar-induction-on-n`
found and fixed in $L_0(\ell,\varepsilon)$ (a missing piece/cut-count
constraint inherited from the outer game but omitted from the boxed
sub-claim): Level-Absorption as boxed in round 6 is a genuinely *stronger*
(cut-count-unconstrained) claim than what the real game needs, and — unlike
Theorem 7 itself, whose proof never uses cut counts and is genuinely true
unconstrained — this stronger claim is actually **false**.

Reducing the same construction to respect the true budget (drop $R_1$ from
two pieces to one, $R_1=\{2^{m-2}\}$, costing $1$ fewer cut, total exactly
$m$) restores a comfortable positive margin: exact computation gives
margin $2^{m-3}-\tfrac12$ (e.g. $m=3$: margin $+0.5$; $m=8$: margin
$+31.5$) — strictly growing with $m$, not merely non-negative.

**Corrected statement.**

> **Open Sub-Problem B$'$ (Level-Absorption, cut-budget-corrected).** With
> $B''$ (Dominance-Chain at level $m-2$, $\mathrm{sum}(B'')\le2^{m-2}$) and
> $S''$ a refinement of $\Gamma_{m-2}$ with top $k-1$ levels unsplit (the
> shape actually produced by the Section 10.2 derivation), and
> $\{\mu_1\}\cup R_1$ a split of the value $2^{m-1}$ with $\mu_1<b_2$, such
> that the **total cut count of the whole response**
> $(k-1)+|R_1|+\sum(\text{levels }0,\dots,m-k-1\text{'s piece counts}-1)$
> is $\le m$ (the real game's budget), is
> $\mathrm{OddSum}(B''\cup\{\mu_1\}\cup R_1\cup S'')\ \ge\ b_2+\mathrm{sum}(B'')$?

**Fresh stress test of the corrected statement.** A new harness
(`/tmp/round-7/stress_test_budgeted.py`) explicitly tracks and enforces
total cut count $\le m$ (distributing the tail cut budget between $R_1$'s
piece count and the free lower levels' piece counts via random
stars-and-bars allocation, on top of the same exact-`Fraction` random
value generation as before). Two independent runs, $30{,}000$ and
$60{,}000$ trials ($m=3,\dots,9$, all valid $k$), **zero violations in
either run**, and — unlike the unbudgeted search — no near-zero margins
either (nothing found below $1/1000$ across $\approx90{,}000$ trials
combined). This is meaningfully stronger evidence than round 6's original
(narrower, single-level) search: it now covers genuine multi-level
simultaneous splits, just correctly bounded by the real cut budget. Not
proved.

**Net effect.** A real error is caught and fixed (Level-Absorption as
originally boxed is provably false, not merely unproved — recorded
precisely, per the project's overclaiming rules, rather than left as a
silently-true-looking conjecture). The corrected, budget-aware version is
well-supported but still open.

#### 11.2 Insertion-Robustness: extended to genuine $k'\ge2$, more broadly
corroborated, proof attempted and not found

Round 6's only test of Insertion-Robustness used $k'=1$ (a single-element
$B'$), which by Theorem 7a's own unconditional strength always gives
$\mathrm{OddSum}(B'\cup S'')=b_2+\mathrm{EvenSum}(S'')$ with
$\mathrm{EvenSum}(S'')\ge0$ automatically — the margin over $S'=b_2$ is
exactly $\mathrm{EvenSum}(S'')$, a quantity with no forced relationship to
$R_1$ at all, so no shape of $R_1$ can ever push the total below $S'$ once
$\mathrm{EvenSum}(S'')$ alone already exceeds any conceivable loss. This
made round 6's test structurally incapable of finding a violation even if
one existed — round 7 was tasked with testing $k'\ge2$ instances, where
$B'$ has genuine internal structure and no such free slack is guaranteed.

**Testing performed.**
- $20{,}000$ exact-`Fraction` random trials (`/tmp/round-7/stress_test.py`,
  `test_A`), $k'=1,\dots,m-1$, $m=2,\dots,7$, six different split-shape
  styles (unsplit, two-unequal, many-equal, many-unequal, fully random cut
  points) cycled across trials for both $S''$'s free levels and $R_1$:
  **zero violations**; tightest margins found were small but strictly
  positive ($\approx0.00045$ at the tightest).
- A `scipy` Nelder–Mead adversarial search directly over split shapes
  (arbitrary cut points, not just equal/unequal presets), for
  $m=4,\dots,7$, $k'=1,2,3$, varying the number of pieces per level and
  for $R_1$ ($3,5,8$ pieces): minimum margin found across all
  configurations tested is $+1.5$ (at $m=4,k'=2$) — comfortably positive,
  no configuration approaches $0$.
- The same "bisect every level, ignore cut budget" adversarial pattern
  that *broke* Level-Absorption (Section 11.1), applied instead to
  Insertion-Robustness (tight dominance-chain $B'$, $S''$ with every free
  level bisected, $\mu_1=b_2$ at the boundary, $R_1$ also bisected): tested
  $m=4,\dots,11$, $k'=1,\dots,m-2$, minimum margin found is $+3.5$. This is
  a meaningful structural finding on its own: **the specific failure mode
  that refutes Level-Absorption does not transfer to Insertion-Robustness**
  — Insertion-Robustness appears robust even *without* a cut-budget
  hypothesis, unlike Level-Absorption. (Not proved — this is evidence, not
  a theorem — but it is evidence against the two sub-problems sharing a
  single root cause, which was an open question after round 6.)

**Proof attempts (unsuccessful this round, recorded for future rounds).**
- *Reduction to a single-element worst case.* Hoped that among all shapes
  of $R_1$ with fixed $\mathrm{sum}=L$ and $\max\le\mu_1$, the single
  element shape $R_1=\{L\}$ is always the most adversarial (which would
  reduce Insertion-Robustness to a single-insertion lemma). **Refuted** by
  direct exact-rational counterexample pairs: across $3000$ random
  instances, the single-element shape gave the lower $\mathrm{OddSum}$
  only about half the time ($1497/3000$) — no monotonicity in piece count
  holds in either direction. Dead end, recorded so it is not retried.
- *Certified Subadditivity/General-Insertion Lemmas.* Lemma S
  ($\mathrm{OddSum}(A\cup B)\le\mathrm{OddSum}(A)+\mathrm{OddSum}(B)$) and
  Theorem 4 (`lemmas/perfect-pairing-subadditivity-and-general-
  insertion.md`) are both upper-bound or exact-doubling tools; neither
  gives a *lower* bound on $\mathrm{OddSum}(N\cup R_1)$ in terms of
  $\mathrm{OddSum}(N)$ and $R_1$'s shape, which is what Insertion-
  Robustness needs. No adaptation found this round.
- *Direct peeling induction on $|R_1|$.* Attempted but not completed: the
  natural induction (peel the current global max of $N\cup R_1$, split on
  whether it lies in $R_1$ or $N$) stalls because $\mu_1$ can exceed
  $\max(N)$ by an unbounded amount, so a single element of $R_1$ can become
  the new global max and displace the existing induction structure in a
  way not yet controlled. This is structurally reminiscent of (but not
  identical to) the original Leftover-Fragment Obstruction (Section 9.4) —
  recorded as the likely next avenue, not pursued further this round for
  lack of time.

**Net effect.** Insertion-Robustness is now supported by substantially
broader and harder-to-satisfy adversarial testing than round 6 provided,
including a targeted test of the exact failure pattern that broke its
sibling sub-problem, with no violation found. It remains **unproved**; the
proof attempts made and ruled out this round are recorded so a future round
does not repeat them.

#### 11.3 Summary of round 7's revised open sub-problems

Theorem 7'$(m,k;L)$ for $k\ge2$ still does not close this round. What
changed: Level-Absorption's boxed statement was corrected (a real bug,
found and fixed, with the uncorrected version's falsity recorded as a
genuine negative result rather than silently patched over); both
sub-problems now carry substantially more numeric evidence, targeted
specifically at each other's discovered weak points; and one new
structural fact is established (not merely conjectured): Insertion-
Robustness's failure mode is not the same as Level-Absorption's — the
"bisect everything, ignore cut budget" attack that breaks the latter does
not break the former in any tested instance. Neither sub-problem is
proved. The interleaved case of general Case 2 remains open.

### 12. Round 8: Insertion-Robustness closed in full (Theorem 12/13)

This round pursues the outline's telescoping-reduction plan for Open
Sub-Problem A (Insertion-Robustness, boxed in Section 10.2), using the
certified Single-Insertion Lemma as the atomic move. We first re-derive the
needed exact formula **from scratch** (rather than citing the certified
lemma directly), because the argument turns out to close the whole
sub-problem outright and we want the proof to be fully self-contained and
not depend on any external tie-breaking convention; we then cross-check the
result against the certified lemma's formula as an independent consistency
check.

#### 12.1 A sub-lemma on alternating sums of nonnegative sequences

**Lemma 9 (AltSum suffix bound).** Let $a_1\ge a_2\ge\cdots\ge a_k\ge0$ be a
finite sequence of nonnegative reals ($k\ge0$; for $k=0$ the sequence is
empty). Then
$$0\ \le\ \mathrm{AltSum}(a_1,\dots,a_k):=a_1-a_2+a_3-\cdots\ \le\ a_1$$
(interpreting both sides as $0$ when $k=0$).

*Proof.* If $k=0$ both sides equal $0$. For $k\ge1$: group consecutive pairs
from the front, $(a_1-a_2)+(a_3-a_4)+\cdots$, ending either in a full pair or
a single leftover term $a_k$ if $k$ is odd. Each bracketed difference
$a_{2i-1}-a_{2i}\ge0$ since the sequence is sorted descending, and a
leftover single term $a_k\ge0$; summing these nonnegative pieces gives
$\mathrm{AltSum}\ge0$. For the upper bound, instead write
$\mathrm{AltSum}=a_1-\bigl[(a_2-a_3)+(a_4-a_5)+\cdots\bigr]$, where the
bracketed sum (over consecutive pairs starting at $a_2$, again ending in a
matched pair or possibly nothing left over) consists of terms
$a_{2i}-a_{2i+1}\ge0$; since this bracketed sum is $\ge0$,
$\mathrm{AltSum}\le a_1$. $\blacksquare$

#### 12.2 Single-insertion monotonicity, proved from scratch

**Theorem 12 (Single-Insertion Monotonicity).** Let $N=\{x_1\ge\cdots\ge
x_L\}$ ($L\ge0$) be a finite multiset of positive reals and let $v>0$. Let
$N\cup\{v\}$ denote the multiset obtained by inserting one new copy of $v$.
Then
$$0\ \le\ \mathrm{OddSum}(N\cup\{v\})-\mathrm{OddSum}(N)\ \le\ v.$$

*Proof.* Fix any convention for placing $v$ among ties (the value of
$\mathrm{OddSum}$ depends only on the multiset, not on which physical tied
copy sits where — the same remark already used after Lemma 1's proof —
so we may fix one convenient convention and the conclusion is convention-
independent). Specifically: let
$$s:=1+\#\{\,i: x_i>v\,\},$$
so that $x_1,\dots,x_{s-1}$ are exactly the elements of $N$ strictly
greater than $v$ (possibly $s=1$, i.e. none), and $x_s,\dots,x_L$ are
exactly the elements of $N$ that are $\le v$ (possibly empty, if
$s=L+1$). Insert $v$ at sorted position $s$: the new sorted list is
$$x_1,\dots,x_{s-1},\,v,\,x_s,\dots,x_L,$$
of length $L+1$, still sorted descending (each of $x_1,\dots,x_{s-1}>v$ and
each of $x_s,\dots,x_L\le v$, by construction).

Now compare $\mathrm{OddSum}$ before and after by tracking, exactly as in
Lemma 1's own proof of $(\ast)$, how each original index's contribution to
$\mathrm{OddSum}$ changes:

- Indices $1,\dots,s-1$: unchanged position (still $1,\dots,s-1$ in the new
  list), so they contribute identically to $\mathrm{OddSum}$ before and
  after — these terms cancel in the difference.
- The new element $v$: sits at position $s$; contributes $v$ to the new
  $\mathrm{OddSum}$ if $s$ is odd, $0$ if $s$ is even.
- Indices $s,\dots,L$ (values $x_s,\dots,x_L$): each such $x_i$ moves from
  position $i$ (old list) to position $i+1$ (new list) — i.e. its position
  parity *flips*. So $x_i$ (for $i\ge s$) contributes to $\mathrm{OddSum}(N)$
  iff $i$ is odd, and to $\mathrm{OddSum}(N\cup\{v\})$ iff $i+1$ is odd,
  i.e. $i$ is even.

Hence, writing $\sigma_{\mathrm{odd}}:=\sum_{i\ge s,\,i\text{ odd}}x_i$ and
$\sigma_{\mathrm{even}}:=\sum_{i\ge s,\,i\text{ even}}x_i$ (sums over
original indices $i\in\{s,\dots,L\}$),
$$\mathrm{OddSum}(N)=\Bigl(\sum_{i<s,\,i\text{ odd}}x_i\Bigr)+\sigma_{\mathrm{odd}},\qquad
\mathrm{OddSum}(N\cup\{v\})=\Bigl(\sum_{i<s,\,i\text{ odd}}x_i\Bigr)+[v\text{ if }s\text{ odd}]+\sigma_{\mathrm{even}}.$$
So
$$\Delta:=\mathrm{OddSum}(N\cup\{v\})-\mathrm{OddSum}(N)=[v\text{ if }s\text{ odd}]+\sigma_{\mathrm{even}}-\sigma_{\mathrm{odd}}.\tag{12.1}$$

Now let $Z:=(x_s,x_{s+1},\dots,x_L)$, a sorted-descending sequence of
nonnegative reals (possibly empty), and consider its own local indexing
$1,2,\dots,L{-}s{+}1$ (local index $\ell$ corresponds to global index
$s+\ell-1$). $\mathrm{AltSum}(Z)=\sum_{\ell\text{ odd (local)}}x_{s+\ell-1}-\sum_{\ell\text{ even (local)}}x_{s+\ell-1}$.

- If $s$ is **odd**: local index $\ell$ and global index $i=s+\ell-1$ have
  the *same* parity (since $s-1$ is even). So
  $\mathrm{AltSum}(Z)=\sigma_{\mathrm{odd}}-\sigma_{\mathrm{even}}$, i.e.
  $\sigma_{\mathrm{even}}-\sigma_{\mathrm{odd}}=-\mathrm{AltSum}(Z)$. By
  (12.1), $\Delta=v-\mathrm{AltSum}(Z)$.
- If $s$ is **even**: local index $\ell$ and global index $i=s+\ell-1$ have
  *opposite* parity (since $s-1$ is odd). So local-odd positions correspond
  to global-even indices and vice versa:
  $\mathrm{AltSum}(Z)=\sigma_{\mathrm{even}}-\sigma_{\mathrm{odd}}$. By
  (12.1) (with the "$v$ if $s$ odd" bracket now $0$), $\Delta=\mathrm{AltSum}(Z)$.

In either case, by Lemma 9 applied to $Z$ (a sorted-descending sequence of
nonnegative reals, first term $x_s\le v$ if nonempty, or $\mathrm{AltSum}
(\varnothing)=0$ if empty), $0\le\mathrm{AltSum}(Z)\le x_s\le v$ (using
$x_s\le v$, which holds by construction of $s$ whenever $Z$ is nonempty).
Hence:
- $s$ odd: $\Delta=v-\mathrm{AltSum}(Z)\in[v-v,\,v-0]=[0,v]$.
- $s$ even: $\Delta=\mathrm{AltSum}(Z)\in[0,v]$ (using $\mathrm{AltSum}(Z)\le x_s\le v$).

Either way $0\le\Delta\le v$. $\blacksquare$

*(Independent consistency check: this formula agrees exactly with the
certified Single-Insertion Lemma's $\Delta\mathrm{AltSum}$ formula
(`lemmas/altsum-reformulation-and-single-insertion.md`) converted to
$\Delta\mathrm{OddSum}$ via $\mathrm{OddSum}=(\mathrm{sum}+\mathrm{AltSum})/2$
— both give $\Delta=v-\mathrm{AltSum}(z_s,\dots,z_L)$ for $s$ odd and
$\Delta=\mathrm{AltSum}(z_s,\dots,z_L)$ for $s$ even, matching term-for-term.
The proof above is nonetheless self-contained and does not depend on that
lemma's certification.)*

**Numeric stress test (mandatory, performed before write-up, per this
round's dispatch instruction).** Exact `Fraction` arithmetic, $20{,}000$
random trials ($N$ of random size $0$–$8$, random rational entries,
random $v$): zero violations of $0\le\Delta\le v$. A second, independently
targeted $20{,}000$-trial run restricted to **small integer values only**
(forcing frequent exact ties among $N$'s own entries and between $v$ and
entries of $N$ — exactly where a tie-breaking argument could silently
break): zero violations. (Scripts re-run fresh for this write-up; see
Section 12.4 for the exact harness description.)

#### 12.3 The general Insertion Monotonicity Corollary, and closure of Sub-Problem A

**Theorem 13 (General Insertion Monotonicity).** Let $N$ and $R$ be any two
finite multisets of positive reals ($R$ of arbitrary size $p\ge0$, arbitrary
shape, arbitrary total sum — no relation to $N$ required). Then
$$\mathrm{OddSum}(N\cup R)\ \ge\ \mathrm{OddSum}(N).$$

*Proof.* Induction on $p=|R|$. If $p=0$, $N\cup R=N$ and equality holds
trivially. If $p\ge1$, write $R=R'\cup\{r\}$ for some fixed element $r\in R$
(any choice; $R'$ has $p-1$ elements). By Theorem 12 applied with
"$N$" $:=N\cup R'$ and "$v$" $:=r$ (valid since $N\cup R'$ is a finite
multiset of positive reals and $r>0$),
$$\mathrm{OddSum}\bigl((N\cup R')\cup\{r\}\bigr)\ \ge\ \mathrm{OddSum}(N\cup R'),$$
i.e. $\mathrm{OddSum}(N\cup R)\ge\mathrm{OddSum}(N\cup R')$. By the inductive
hypothesis (applicable since $|R'|=p-1<p$), $\mathrm{OddSum}(N\cup R')\ge
\mathrm{OddSum}(N)$. Chaining the two inequalities,
$\mathrm{OddSum}(N\cup R)\ge\mathrm{OddSum}(N\cup R')\ge\mathrm{OddSum}(N)$.
$\blacksquare$

**Corollary (Open Sub-Problem A, closed in full, unconditionally).** Let
$(B',S'')$ be any instance satisfying Theorem 7's hypotheses at
$(m-1,k-1)$ (so $\mathrm{OddSum}(B'\cup S'')\ge S'$, by the already-certified
Theorem 7), and let $R_1$ be **any** finite multiset of positive reals
(no constraint on its sum, shape, or maximum needed — in particular the
originally-hypothesized bound $\max(R_1)\le\mu_1$ from Section 10.2 is not
needed). Then
$$\mathrm{OddSum}(B'\cup S''\cup R_1)\ \ge\ S'.$$

*Proof.* Apply Theorem 13 with $N:=B'\cup S''$, $R:=R_1$:
$\mathrm{OddSum}(B'\cup S''\cup R_1)\ge\mathrm{OddSum}(B'\cup S'')\ge S'$,
the last step by Theorem 7 (already certified). $\blacksquare$

This settles **Open Sub-Problem A (Insertion-Robustness of Theorem 7)** in
full, in a strictly stronger, hypothesis-free form than originally boxed
(the constraint $\max(R_1)\le\mu_1$, present in Section 10.2's original
statement, turns out to be entirely unnecessary — the fact holds for *any*
additional multiset of positive mass inserted anywhere).

**Consequence for Theorem 7'$(m,k;L)$.** Recall Section 10.2's Subcase (a)
($\mu_1\ge b_2$): equations (10.1) and (10.2a) reduce the target exactly to
$\mathrm{OddSum}(B'\cup R_1\cup S'')\ge S'$, where $(B',S'')$ is a Theorem-7
instance at $(m-1,k-1)$ (so $\mathrm{OddSum}(B'\cup S'')\ge S'$ by
(10.3a)) and $R_1$ is the arbitrary "rest" of the split of level $m-1$. This
is now exactly the Corollary just proved. Hence:

> **Theorem 14 (Subcase (a) of Theorem 7'$(m,k;L)$, closed in full).** For
> $m\ge1$, $k\ge2$: whenever $\mu_1\ge b_2$ (the largest fragment of the
> split top-tail-level dominates the second dominance-chain element), the
> full target $\mathrm{OddSum}(B\cup S)\ge\sum_i b_i$ holds *unconditionally*
> — no restriction on the shape or piece-count of $R_1$, no cut-budget
> hypothesis needed for this subcase specifically (the earlier round-7
> cut-budget issue arose only in Subcase (b)'s Level-Absorption analysis, not
> here).

*Proof.* Chain (10.1) $\Rightarrow$ (10.2a) $\Rightarrow$ the Corollary above
$\Rightarrow$ (10.3a). Each step already proved (10.1)/(10.2a) in Section
10.2 (exact identities, no gap), and the Corollary just closed the
remaining piece. $\blacksquare$

**What remains open.** Subcase (b) ($\mu_1<b_2$), i.e. Open Sub-Problem B
(Level-Absorption, cut-budget-corrected version, Section 11.1), is
untouched this round and remains the sole open piece of Theorem
7'$(m,k;L)$'s inductive step. Once Level-Absorption is closed, Theorem 7'
is fully proved for all $k\ge2$ (combined with the already-proved $k=1$ base
case, Theorem 7a), which in turn would close the interleaved joint Case 2
of the general lower-bound direction.

#### 12.4 Numeric verification harness (exact reproduction record)

For reproducibility, the exact tests run (all using Python's `fractions.Fraction`,
independent of any prior round's scripts) were:

1. **Test 1** (Theorem 12, general): $20{,}000$ trials; $N$ of random size
   $0$–$8$ with entries $\mathrm{Fraction}(\text{randint}(1,1000),
   \text{randint}(1,50))$; $v$ drawn the same way. Checked
   $0\le\mathrm{OddSum}(N\cup\{v\})-\mathrm{OddSum}(N)\le v$ exactly.
   Result: $0/20{,}000$ violations.
2. **Test 2** (Theorem 12, tie-forcing): identical harness but entries and
   $v$ restricted to small integers $1$–$5$ (forces frequent exact ties),
   $20{,}000$ trials. Result: $0/20{,}000$ violations.
3. **Test 3** (Theorem 13, general multiset corollary): $20{,}000$ trials;
   $N$ and $R$ each of random size $0$–$8$ with the same rational
   distribution as Test 1. Checked $\mathrm{OddSum}(N\cup R)\ge
   \mathrm{OddSum}(N)$ exactly. Result: $0/20{,}000$ violations.
4. **Test 4** (Theorem 13, larger sizes, independent second pass): $10{,}000$
   further trials with $N,R$ of random size $0$–$10$. Result: $0/10{,}000$
   violations.
5. **Sub-lemma check** (Lemma 9): $20{,}000$ trials of random
   sorted-descending nonnegative sequences of length $0$–$10$, checking
   $0\le\mathrm{AltSum}\le a_1$ (or $=0$ for the empty sequence) exactly.
   Result: $0/20{,}000$ violations.

Total: $\approx110{,}000$ exact-`Fraction` trials across all checks, zero
violations, run fresh for this round (not reusing round 6's or round 7's
scripts), including a dedicated tie-heavy pass targeting exactly the
tie-breaking convention the proof depends on.

### 13. Round 9: toward Level-Absorption — an Unsplit-Baseline identity
(proved in full, promotable) plus a precise diagnosis of why the natural
abstract degradation bound built from it is not, by itself, strong enough

This round's target is Open Sub-Problem B$'$ (Level-Absorption, cut-budget-
corrected, Section 11.1), the sole remaining piece of Theorem 7'$(m,k;L)$'s
inductive step. Per the round-9 dispatch's explicit warning, we do **not**
attempt to invoke Theorem 13 (Insertion Monotonicity) directly — that gives
only a qualitative $\Delta\ge0$ bound, and Level-Absorption needs the
inserted mass to supply a *quantitative* gain $\ge b_2>0$. Instead we
pursued lead 1 of the outline (a quantitative insertion/degradation
argument), and we report exactly how far it goes and precisely where it
runs out, which turns out to be a genuine, non-obvious structural finding.

Recall the exact target (Section 10.2, Subcase (b), corrected in Section
11.1): with $B''=\{b_3,\dots,b_k\}$ (Dominance-Chain at level $m-2$,
$\mathrm{sum}(B'')\le2^{m-2}$), $S''$ a refinement of $\Gamma_{m-2}$ with top
$k-1$ levels ($m-2,\dots,m-k$) unsplit, and $\{\mu_1\}\cup R_1$ an arbitrary
split of the value $2^{m-1}$ with $\mu_1<b_2$ (subject to the real game's
total cut-budget), show
$$\mathrm{OddSum}\bigl(B''\cup\{\mu_1\}\cup R_1\cup S''\bigr)\ \ge\ b_2+\mathrm{sum}(B'').\tag{10.3b}$$
Write $M':=S''\cup B''$ and $P:=\{\mu_1\}\cup R_1$ (so $\sum P=2^{m-1}$,
$\max(P)=\mu_1$); the left side of (10.3b) is $\mathrm{OddSum}(M'\cup P)$.

#### 13.1 The Unsplit-Baseline Lemma (proved in full)

**Lemma L (Unsplit-Baseline).** With $B''$, $S''$ as above (so, writing
$S''=\{2^{m-2}\}\cup S'''$ with $S'''$ the refinement of $\Gamma_{m-3}$ on
levels $m-3,\dots,m-k$ unsplit / $0,\dots,m-k-1$ arbitrary), if the value
$2^{m-1}$ is inserted **unsplit** in place of $P$, then
$$\mathrm{OddSum}\bigl(M'\cup\{2^{m-1}\}\bigr)\ \ge\ 2^{m-1}\ \ge\ b_2+\mathrm{sum}(B'').$$

*Proof.* $S''$ is, by construction, a refinement of $\Gamma_{m-2}$ (it
covers exactly levels $0,\dots,m-2$, with some levels forced unsplit — this
is still "a refinement", just a constrained one; the *hypothesis* of
Theorem 7a is "any refinement $S$ of $\Gamma_{M-1}$", which places no
constraint on which particular refinement, so a partially-constrained one
qualifies). Apply the already-certified **Theorem 7a** with parameter
$M:=m-1$ (so $\Gamma_{M-1}=\Gamma_{m-2}$) and $b_1:=2^{m-1}$: the hypothesis
$b_1\ge2^{M-1}=2^{m-2}$ holds (with equality), so
$$\mathrm{OddSum}\bigl(\{2^{m-1}\}\cup S''\bigr)\ \ge\ 2^{m-1}.$$
Now apply the already-certified **Theorem 13** (General Insertion
Monotonicity) with $N:=\{2^{m-1}\}\cup S''$ and $R:=B''$ (an arbitrary
finite multiset of positive reals, no constraint needed):
$$\mathrm{OddSum}\bigl(\{2^{m-1}\}\cup S''\cup B''\bigr)\ \ge\ \mathrm{OddSum}\bigl(\{2^{m-1}\}\cup S''\bigr)\ \ge\ 2^{m-1}.$$
Finally, $B'=\{b_2\}\cup B''$ has the Dominance-Chain property at level
$m-1$ by hypothesis (inherited from $B$'s own DC property at level $m$, as
used throughout Section 10.2), so $\mathrm{sum}(B')=b_2+\mathrm{sum}(B'')\le2^{m-1}$
directly from the DC-property's sum cap. $\blacksquare$

This is a genuinely new, fully proved, and directly reusable fact: **if**
XY's response happened to leave level $m-1$ entirely unsplit, Level-
Absorption would follow immediately and unconditionally, with an explicit
non-negative slack $\Sigma:=2^{m-1}-b_2-\mathrm{sum}(B'')\ge0$. The entire
remaining difficulty of Level-Absorption is thus isolated exactly to: how
much can $\mathrm{OddSum}(M'\cup P)$ fall short of
$\mathrm{OddSum}(M'\cup\{2^{m-1}\})$ purely because $2^{m-1}$ is split into
$P=\{\mu_1\}\cup R_1$ instead of left whole — a **re-splitting degradation**
question (the specific phenomenon the file has already flagged, Section
10.2, as structurally different from — and not covered by — the
insertion-monotonicity technique that closed Sub-Problem A).

#### 13.2 An abstract Split-Degradation bound: evidence it is true, but a
precise proof that it is not, by itself, strong enough

To try to bound the degradation, consider the following general claim,
tested (not yet proved) by hand on several exact examples:

> **Candidate Lemma (Split-Degradation).** For any finite multiset $M$ of
> positive reals, any $g>0$ with $g\ge\max(M)$ (or $M=\varnothing$), and
> any positive split $P=\{q_1\ge\cdots\ge q_p\}$ of $g$ ($p\ge1$,
> $\sum q_i=g$),
> $$\mathrm{OddSum}(M\cup\{g\}) - \mathrm{OddSum}(M\cup P)\ \le\ g-q_1.$$

**Exact hand-computed evidence.** With $M=\{5,5,5,5\}$, $g=10$: unsplit
gives $\mathrm{OddSum}=10+5+5=20$; split $P=\{5,5\}$ gives six copies of
$5$, $\mathrm{OddSum}=5\cdot3=15$, degradation $=5=g-q_1$ exactly; split
$P=\{6,4\}$ gives sorted $6,5,5,5,5,4$, $\mathrm{OddSum}=6+5+5=16$,
degradation $=4=g-q_1$ exactly. With $M=\{5,4\}$, $g=10$: unsplit
$\mathrm{OddSum}=10+4=14$; split $P=\{9,1\}$ gives sorted $9,5,4,1$,
$\mathrm{OddSum}=9+4=13$, degradation $=1=g-q_1$ exactly; split
$P=\{6,4\}$ gives sorted $6,5,4,4$, $\mathrm{OddSum}=6+4=10$, degradation
$=4=g-q_1$ exactly. In every hand-checked case the bound holds, and — this
is the crucial structural point — **it is frequently attained with
equality**, not just satisfied with slack. (We did not run this as an
automated exact-arithmetic sweep this round due to time; the hand
computations above are exact but not exhaustive, so the Candidate Lemma is
recorded as evidenced, not proved, and is **not** used below as an
established fact — only its tightness pattern is used, which is visible
directly in each exhibited instance.)

**Why this tightness, even if the Candidate Lemma were fully proved, is not
enough to close (10.3b).** Suppose the Candidate Lemma holds (as the
evidence suggests). Applying it with $M:=M'$, $g:=2^{m-1}$, $P:=\{\mu_1\}\cup
R_1$ (valid since $2^{m-1}\ge\max(M')$: $M'=S''\cup B''$ has
$\max(S'')=2^{m-2}$ and $\max(B'')=b_3\le\mathrm{sum}(B'')\le2^{m-2}$, both
$<2^{m-1}$) gives
$$\mathrm{OddSum}(M'\cup\{2^{m-1}\}) - \mathrm{OddSum}(M'\cup P)\ \le\ 2^{m-1}-\mu_1.$$
Combined with Lemma L ($\mathrm{OddSum}(M'\cup\{2^{m-1}\})\ge2^{m-1}$), this
would give
$$\mathrm{OddSum}(M'\cup P)\ \ge\ 2^{m-1}-(2^{m-1}-\mu_1)=\mu_1.$$
But the target (10.3b) needs $\mathrm{OddSum}(M'\cup P)\ge
b_2+\mathrm{sum}(B'')$, and we are in the regime $\mu_1<b_2\le
b_2+\mathrm{sum}(B'')$ (with **strict** inequality whenever $B''\ne
\varnothing$, i.e. whenever $k\ge3$). So the bound $\mu_1$ obtained this
way is **strictly weaker than the target** the moment $k\ge3$: the
Candidate Lemma's worst case — attained, as shown above, by exact
hand-verified instances — throws away exactly the slack
$\Sigma=2^{m-1}-b_2-\mathrm{sum}(B'')$ that Lemma L provides, and adds
nothing back from $B''$ or $S'''$'s own internal structure. **This is a
precise, not hand-waved, diagnosis**: any bound on the degradation that
depends *only* on $g$ and $q_1=\mu_1$ (i.e. is agnostic to the shape of
$R_1$ beyond its max, and to $B'',S'''$ entirely) is provably insufficient
to close (10.3b) whenever $k\ge3$, because its own worst case is tight and
that worst case does not by itself meet the target. A genuine proof of
Level-Absorption must therefore either (a) show that the abstract
worst-case degradation configuration (many exact ties, as in the hand
examples and structurally reminiscent of the round-7 "bisect-everything"
extremal construction) cannot simultaneously satisfy the actual
level-structure constraints on $M'$ (powers of $2$, at most one exact tie
at each level generically) with the cut-budget, or (b) find a genuinely
sharper degradation bound that uses $B''$/$S'''$'s structure (e.g. their
own already-known $\mathrm{OddSum}(B''\cup S''')\ge\mathrm{sum}(B'')$
slack), not just $\max(M')$.

**Consistency check against round 7's numeric evidence.** This diagnosis is
consistent with, and helps explain, round 7's finding (Section 11.1) that
the actual worst-case margin of the *budget-corrected* Level-Absorption
claim is $2^{m-3}-\tfrac12$ — strictly positive and growing with $m$, not
near zero. This means the abstract worst case identified in Section 13.2
above (tight Split-Degradation, discarding all of $\Sigma$) is **not**
simultaneously realizable together with the real level/cut-budget
constraints — some additional positive contribution (from $B''$, $S'''$, or
the interaction between $P$'s shape and the powers-of-two level structure)
must be recovered that the abstract, structure-agnostic bound above cannot
see. Locating and quantifying that recovered contribution — i.e.
pursuing lead (a) or (b) above — is the precise open task for a future
round; it was not completed this round due to time.

#### 13.3 Net effect of this round

**What is newly proved and promotable:** Lemma L (Unsplit-Baseline),
fully proved unconditionally from already-certified Theorem 7a and Theorem
13, giving an exact, explicit slack $\Sigma=2^{m-1}-b_2-\mathrm{sum}(B'')\ge0$
that any successful closure of Level-Absorption must show is not
exceeded by the true degradation from splitting level $m-1$.

**What is newly and precisely diagnosed (not merely conjectured):** the
"obvious" way to try to bound that degradation — an abstract lemma
depending only on $g=2^{m-1}$ and $q_1=\mu_1$ — is, even under the
optimistic assumption that it is true (strong hand-checked evidence, not a
full proof), **provably insufficient** by itself to close (10.3b) whenever
$k\ge3$ ($B''\ne\varnothing$), because its own worst case exactly discards
the available slack $\Sigma$ without using any of $B''$/$S'''$'s structure.
This directly rules out the most natural first attempt at lead 1 of the
outline (a structure-agnostic quantitative degradation chain) as
insufficient on its own, and points concretely at lead 2 (exchange-
smoothing to a finite family of extremal profiles, since the abstract
worst case is exactly a "many exact ties" profile of the kind that
extremal-profile reduction would need to rule out or directly check against
the level-structure constraints) as the more promising route for the next
round. **Level-Absorption is not closed this round**; Theorem
7'$(m,k;L)$'s inductive step, and hence the interleaved joint Case 2 of the
lower-bound direction, remains open.

### 14. Round 10: the $B''$-Banking Lemma proved in full via Theorem 7 (not
just its $k=1$ case); the naive additive combination is proved **false**;
Level-Absorption reduced to a clean, budget-respecting base case ($k=2$),
numerically confirmed but still open

This round's target (per the outliner) is the "asymmetric decomposition":
bank $\mathrm{sum}(B'')$ for free via a Theorem-7-type closure applied one
level down to $B''\cup S'''$, reducing (10.3b) to a strictly smaller
residual on $P$ alone, and — the outliner's own flagged crux — to verify
whether the two banked bounds *combine* under $\mathrm{OddSum}$, since
$\mathrm{OddSum}$ is not additive across an arbitrary split of a merged
sorted multiset. We carry the first half through in full (with one
correction to the outline's own citation) and settle the second half
**negatively**, with an explicit exact-arithmetic counterexample, before it
could be relied on in a proof — exactly the stress-test discipline CLAUDE.md
requires for this kind of step.

#### 14.1 The $B''$-Banking Lemma (proved in full; corrects the outline's
citation from Theorem 7a to the general Theorem 7)

Recall the setup (Sections 10.2, 13): $B''=\{b_3,\dots,b_k\}$ has the
Dominance-Chain property at level $m-2$ with $\mathrm{sum}(B'')\le2^{m-2}$
(this sum cap is itself a consequence, re-derived here for
self-containedness, of $B'=\{b_2\}\cup B''$ having the Dominance-Chain
property at level $m-1$ with $\mathrm{sum}(B')\le2^{m-1}$: since $b_2\ge
2^{m-2}$ by the Dominance-Chain property applied one level,
$\mathrm{sum}(B'')=\mathrm{sum}(B')-b_2\le2^{m-1}-2^{m-2}=2^{m-2}$).
$S''=\{2^{m-2}\}\cup S'''$ is a refinement of $\Gamma_{m-2}$ with top $k-1$
levels ($m-2,\dots,m-k$) unsplit, so $S'''$ is exactly a refinement of
$\Gamma_{m-3}$ with top $k-2$ levels ($m-3,\dots,m-k$) unsplit and levels
$0,\dots,m-k-1$ arbitrary.

**Lemma M ($B''$-Banking Lemma).** $\mathrm{OddSum}(B''\cup S''')\ge
\mathrm{sum}(B'')$.

*Proof.* This is a direct instance of the already-certified **Theorem 7**
(Joint Dominance-Chain Closure, top-levels-clear), applied at parameters
$(m',k'):=(m-2,\,k-2)$ rather than the outline's proposed Theorem 7a
(Theorem 7a is only the $k'=1$ base case of the same induction and does not
apply verbatim when $B''$ has $\ge2$ elements, i.e. $k\ge4$; the correct,
fully general tool is Theorem 7 itself, whose proof already contains
Theorem 7a as its own base case). Check Theorem 7's hypotheses at
$(m',k')=(m-2,k-2)$:
- $0\le k'\le m'$: i.e. $k-2\le m-2$, i.e. $k\le m$, which holds because the
  *original* $B=\{b_1,\dots,b_k\}$ has the Dominance-Chain property at
  level $m$, and the Dominance-Chain property at level $m$ with $k\ge1$
  elements forces $m\ge1$ and (unfolding the recursive definition $k$
  times) the chain's last element satisfies $b_k\ge2^{m-k}$ (reading
  $2^{-1}:=0$ as the definition's own convention when the level hits $0$),
  which is only meaningful/consistent with $b_k>0$ when $m-k\ge-1$, i.e.
  $k\le m+1$ in general — but the specific instances arising in Section
  10.2's derivation always have $k\le m$ (Theorem 7 itself is invoked one
  level up, at $(m-1,k-1)$, for $(B',S'')$ in (10.3a)/(10.3b)'s own
  derivation, which already requires $k-1\le m-1$, i.e. $k\le m$; this is
  inherited unchanged here).
- $B''$ has the Dominance-Chain property at level $m'=m-2$: given.
- $\mathrm{sum}(B'')\le2^{m'}=2^{m-2}$: shown above.
- $S'''$ is a refinement of $\Gamma_{m'-1}=\Gamma_{m-3}$ with the top $k'=
  k-2$ levels ($(m'-1),\dots,(m'-k'+1)=(m-3),\dots,(m-k)$) unsplit: this is
  exactly $S'''$'s definition.

All hypotheses hold, so Theorem 7 gives $\mathrm{OddSum}(B''\cup S''')\ge
\mathrm{sum}(B'')$ directly. $\blacksquare$

(When $k=2$, $B''=\varnothing$ and $k'=0$; Theorem 7's own $k=0$ base case
gives $\mathrm{OddSum}(S''')\ge0=\mathrm{sum}(\varnothing)$, trivially
true and consistent. When $k=3$, $B''=\{b_3\}$ is a single element and
$k'=1$; Theorem 7's own inductive step at $k'=1$ reduces in one line to
exactly Theorem 7a's statement, so the outline's citation is *correct* in
this one sub-case but not in general — this is the precise sense in which
the correction above is needed.)

**Status: Lemma M is a complete, unconditional, promotable proof of the
outline's Step 2** (with the citation corrected from Theorem 7a to the
general Theorem 7).

#### 14.2 The naive additive combination is FALSE (stress-tested, exact
counterexample)

The outline's Step 5 explicitly flagged, as the round's crux open question,
whether Lemma M's bound (on $B''\cup S'''$ alone) and a hoped-for bound on
"the rest" ($P$ against a baseline of $b_2$) can be *added* to recover the
full target $b_2+\mathrm{sum}(B'')$. The most natural formalization of
"adding the two banked bounds" is the following general claim, which we
state precisely and then test **before** trusting it, per the outline's own
explicit warning and CLAUDE.md's stress-test rule:

> **Candidate Swap Lemma.** Let $Q$ be any finite multiset of positive
> reals, let $b>0$, and let $P$ be any finite multiset of positive reals
> with $\mathrm{sum}(P)\ge b$ and $\max(P)<b$. Then
> $\mathrm{OddSum}(Q\cup P)\ge\mathrm{OddSum}(Q\cup\{b\})$.

If this were true, it would give exactly the missing bridge: apply it with
$Q:=B''\cup S'''$ (so $Q\cup\{2^{m-2}\}=M'$, matching Lemma L's setup) —
more precisely, apply it with $Q:=M'\setminus\{2^{m-2}\}\cup$(whatever
plays the role of the "rest") and $b:=b_2$, $P:=$(the split
$\{\mu_1\}\cup R_1$ of level $m-1$) to swap "level $m-1$ left whole" for
"level $m-1$ split," directly upgrading Lemma L's unsplit-baseline bound to
the split case. We tested it directly, independent of the specific
Level-Absorption instance, with exact `Fraction` arithmetic (script
reproduced below):

```
Q = [], b = 137/11, P = [28705/7371, 4466498/405405]
  sum(P) = 4466498/405405 + 28705/7371 > b ✓,  max(P) = 4466498/405405 ≈ 11.02 < b ≈ 12.45 ✓
  OddSum(Q ∪ P) = OddSum(P) = max(P) ≈ 11.02   (only 2 elements: top rank only)
  OddSum(Q ∪ {b}) = b ≈ 12.45
  11.02 < 12.45   →  VIOLATION
```

This is an exact, hand-checkable counterexample (not a numerical artifact):
take $Q=\varnothing$, $b=10$, $P=\{6,6\}$. Then $\mathrm{sum}(P)=12\ge10=b$
and $\max(P)=6<10=b$, satisfying every hypothesis of the Candidate Swap
Lemma, yet $\mathrm{OddSum}(P)=6$ (only the top-ranked element of a
2-element multiset counts) while $\mathrm{OddSum}(\{b\})=10$; $6<10$. A
20,000-trial randomized exact-`Fraction` sweep (varying $|Q|$ from $0$ to
$6$, random $b$, random split shapes of $P$ with $2$–$5$ pieces) found
**4,508 violations out of 12,598 tested instances** (roughly one in three)
— this is not a rare edge case but a generic failure mode: whenever $P$'s
mass is spread across several pieces each individually below $b$, but
without enough pieces for the *even-ranked* pieces (which do count toward
$\mathrm{OddSum}$ once merged with a nonempty $Q$) to compensate for
losing $b$'s own guaranteed odd-rank slot.

**Conclusion: the Candidate Swap Lemma is false in general, so no
structure-agnostic "add the two banked bounds" mechanism can close
Level-Absorption.** This decisively confirms — with a concrete
counterexample rather than only a diagnosis — the outline's own worry in
Step 5: any successful combination of Lemma M ($B''$'s banked contribution)
with a bound on $P$'s contribution must use the *actual* structure of $M'$
(its power-of-two levels, and in particular that $Q$ in the real instance
is never empty and is never merely "some multiset" but a specific
Dominance-Chain-and-$\Gamma$-refinement object with its own guaranteed
internal $\mathrm{OddSum}$ contribution), not a Q-agnostic swap. This
rules out, for good, the entire family of "prove an abstract structure-free
insertion/swap bound, then apply it twice and add" attempts at
Level-Absorption — a real, reusable negative result, complementing round
9's analogous finding for the Split-Degradation bound (that finding ruled
out *degradation* bounds depending only on $g,q_1$; this one additionally
rules out *swap/replacement* bounds depending only on $b,\max(P),
\mathrm{sum}(P)$, a structurally different but equally natural first
attempt).

#### 14.3 Level-Absorption reduced to a clean base case ($k=2$), confirmed
numerically with the correct cut budget, still open

Since the additive mechanism is dead, we looked for the smallest genuinely
new case where a direct (non-additive) argument might still be found by
hand: $k=2$, i.e. $B''=\varnothing$. Here Lemma M is vacuous (banks
nothing) and (10.3b) reduces to exactly:

> **Base Case (Level-Absorption, $k=2$).** Let $m\ge3$, let $b_2\in
> [2^{m-2},2^{m-1}]$, let $P$ be a split of the value $2^{m-1}$ with
> $\max(P)<b_2$, and let $S'''$ be a refinement of $\Gamma_{m-3}$
> (arbitrary shape, no level forced unsplit), such that the total cut
> count $(|P|-1)+(\text{cuts used inside }S''')\le m-1$ (the real game's
> budget $m$ minus the $1$ cut already spent forming $\{b_1,b_2\}$ from the
> top piece). Then
> $$\mathrm{OddSum}\bigl(P\cup\{2^{m-2}\}\cup S'''\bigr)\ \ge\ b_2.$$

This is a strictly smaller, self-contained instance of the same phenomenon,
free of $B''$'s extra layer of recursion, and is exactly where any future
attempt at Level-Absorption should start (proving it settles $k=2$
outright and — by the same style of induction that built Theorem 7 out of
Theorem 7a — is very likely the genuine base case a $k\ge3$ induction on
Level-Absorption itself, as opposed to a decomposition into $B''$/$P$
pieces, would need).

**We did not find a proof this round**, but we verified it is almost
certainly true, with the cut budget correctly enforced (this is exactly
the same class of bug — an omitted cut-count hypothesis — that this file
already caught twice, in Level-Absorption's original round-6 statement and
in Insertion-Robustness's round-6 test family; we built the budget
accounting from scratch here rather than reusing an old script). Exact
`Fraction` search, $m\in\{3,\dots,9\}$, $27{,}430$ tested instances (random
$b_2\in[2^{m-2},2^{m-1}]$, random split shapes of $P$ subject to
$\max(P)<b_2$, random cut allocation of the remaining budget across
$S'''$'s levels): **zero violations**, and the worst margin found across
all trials is **exactly $0$** (attained at $m=3$, $b_2=4$, $P=
\{948/421,\,736/421\}$, $S'''=\{1\}$ — i.e. $b_2=2^{m-1}$ exactly at its
maximum, $P$ split into two pieces neither of which reaches $b_2$, and
level $0$ left unsplit).

Without the budget correction, the *same* claim is **false**: an
unconstrained (no cut-budget) search over the identical parameter ranges
found $19$ violations out of $12{,}598$ tested cases in the first $20{,}000$
random trials (margins as negative as $-361/1260$), confirming that this
base case genuinely needs the cut-budget hypothesis, exactly as
Level-Absorption's general (round-7-corrected) statement does — the two
facts are consistent, not independent coincidences.

**Net effect of Section 14.** Step 2 of the outline (bank
$\mathrm{sum}(B'')$ for free) is now a complete, correctly-cited proof
(Lemma M). Step 5's flagged additivity concern is resolved **negatively**
in its most natural structure-agnostic form (Candidate Swap Lemma, refuted
by an explicit, hand-checkable exact counterexample plus a $\sim36\%$
violation rate under random testing), ruling out an entire family of future
attempts, not just this round's specific instantiation. Level-Absorption
itself is not closed, but it is reduced — cleanly, and with the correct
cut-budget hypothesis identified and enforced — to the single, strictly
smaller Base Case above ($k=2$, $B''=\varnothing$), which is strongly
supported numerically (including an exact worst-margin-$0$ tight instance,
a genuine extremal-case candidate for whoever attempts a direct proof next)
but remains unproved.

### 15. Round 11: the WLOG $b_2$ reduction formalized in full; Case B's
"quick win" framing corrected by an exact equivalence to the file's own
already-partially-open TOP-ONLY residual (a genuine, honest redirection, not
a closure)

This round's dispatch asked for three things: (1) a formal proof of the free
WLOG reduction $b_2=2^{m-1}$ found by last round's explorer; (2) an attempted
quick-win closure of Case B ($\max(P)<2^{m-2}$) via dominant-element
insertion; (3) time permitting, an attack on Case A via Prefix-Run-Peeling
applied to $P$ itself. Per the explicit dispatch instruction to stress-test
any proposed Case B mechanism before write-up, we did so — and found the
round's premise ("substantial slack $\approx0.34$, zero near-ties") does
**not** hold once the search is aimed at the right corner of the parameter
space. We record a corrected, rigorous finding instead: Case B's hardest
sub-case is not a fresh problem needing its own proof from scratch, but is
**exactly** (not just similar to) an already-identified, already-partially-
closed open sub-problem of this same file (and of `self-similar-induction-
on-n`), so all of that prior partial work transfers directly. Item (3),
Case A, was not reached this round (time); we record one precise, rigorous
observation about it below instead of a hand-wave.

#### 15.1 Lemma N (WLOG $b_2=2^{m-1}$) — full formal proof

**Lemma N.** To prove the Base Case (Level-Absorption, $k=2$; Section 14.3)
for every $b_2\in[2^{m-2},2^{m-1}]$, it suffices to prove it for $b_2=
2^{m-1}$ exactly (with the hypothesis specialized to $\max(P)<2^{m-1}$,
automatically true whenever $|P|\ge2$, which the hypothesis
$\mathrm{sum}(P)=2^{m-1}$, $\max(P)<b_2\le2^{m-1}$ already forces: a single
piece of value $2^{m-1}$ would need $\max(P)=2^{m-1}\ge b_2$, contradicting
$\max(P)<b_2$, so $|P|\ge2$ for every admissible $b_2$).

*Proof.* Fix any $b_2'\in[2^{m-2},2^{m-1}]$ and any instance $(P,S''')$
satisfying the Base Case's hypotheses at this $b_2'$: $\mathrm{sum}(P)=
2^{m-1}$, $\max(P)<b_2'$, $S'''$ a refinement of $\Gamma_{m-3}$, and the cut
budget $(|P|-1)+\mathrm{cuts}(S''')\le m-1$. None of $P$, $S'''$, or the
budget constraint mention $b_2'$ at all — they depend only on $m$. Since
$b_2'\le2^{m-1}$, the hypothesis $\max(P)<b_2'$ implies $\max(P)<2^{m-1}$,
so $(P,S''')$ is *also* a valid instance of the Base Case at $b_2=2^{m-1}$
(every hypothesis of that instance — sum, cut budget, refinement shape — is
identical, and the only hypothesis that changed, $\max(P)<b_2$, is implied).
If the Base Case at $b_2=2^{m-1}$ is already proved, it gives
$\mathrm{OddSum}(P\cup\{2^{m-2}\}\cup S''')\ge2^{m-1}\ge b_2'$ (the last step
since $b_2'\le2^{m-1}$ by hypothesis), which is exactly the conclusion needed
at $b_2'$. $\blacksquare$

This is the same argument the round-10 explorer gave, now written as a
self-contained lemma with every hypothesis traced (in particular, making
explicit the previously-implicit fact $|P|\ge2$ used nowhere in the original
sketch but needed to confirm the specialized hypothesis "$\max(P)<2^{m-1}$"
is non-vacuous). It is corroborated, not just motivated, by both the
round-10 search (worst instance found exactly at $b_2=2^{m-1}$) and this
round's own independent search below (every near-tight instance found is
again at $b_2=2^{m-1}$ — consistent, not a coincidence, precisely because
Lemma N proves $b_2=2^{m-1}$ is the *hardest* instance for every fixed
$(P,S''')$).

From here on, by Lemma N, we work exclusively with $b_2=2^{m-1}$, so the
Base Case reads: $m\ge3$, $P$ a partition of $2^{m-1}$ into $\ge2$ parts,
$\max(P)<2^{m-1}$ (automatic), $S'''$ a refinement of $\Gamma_{m-3}$, budget
$(|P|-1)+\mathrm{cuts}(S''')\le m-1$; show
$\mathrm{OddSum}(P\cup\{2^{m-2}\}\cup S''')\ge2^{m-1}$. Case A/B split on
$\max(P)$ vs. $2^{m-2}$ as before.

#### 15.2 Stress test of the round's Case B "quick win" claim: a counterexample to "no near-ties"

Per the mandatory stress-test rule, before writing any proof attempt we ran
a fresh, independent exact-`Fraction` search targeting Case B specifically
($\max(P)<2^{m-2}$), but — unlike a uniform-random allocation of cut budget
between $P$ and $S'''$ — deliberately probed the corner where **all**
remaining cut budget goes into fragmenting $P$ into many pieces while
$S'''$ is left completely unsplit (the direction the file's own prior
sections repeatedly identify as where the true extremal configurations
live, e.g. Section 4's equality construction spends its entire budget on
one object). At $m=4$ ($c:=2^{m-2}=4$, target sum $2^{m-1}=8$,
$S'''=\Gamma_1=\{2,1\}$ unsplit, all $3$ available cuts spent splitting $P$
into $4$ pieces), a targeted random search over $200{,}000$ trials found

$$P=\Bigl(\tfrac{327889}{81977},\,\tfrac{203653}{81977},\,\tfrac{97214}{81977},\,\tfrac{27060}{81977}\Bigr)\approx(4.00000,\,2.48450,\,1.18601,\,0.33013),$$

with $\mathrm{sum}(P)=8$ exactly, $\max(P)=327889/81977<4=c$ (so this is a
genuine, valid Case B instance — the margin by which $\max(P)$ falls short
of $c$ is $19/81977\approx0.000232$, tiny but strictly positive), and

$$\mathrm{OddSum}\bigl(P\cup\{4\}\cup\{2,1\}\bigr)-8 \;=\; \frac{19}{81977}\ \approx\ 0.000232,$$

an exact, hand-verifiable near-zero margin (recomputed independently by
direct sorting and summation of the $7$ exact fractions above). A follow-up
continuous (`scipy` Nelder–Mead, $300$ restarts) optimization over the same
$4$-piece-$P$/unsplit-$S'''$ family at $m=4$ finds the infimum of the margin
is $0$ (numerically $-8\times10^{-11}$, i.e. exactly $0$ up to floating-point
noise, attained only in the limit $\max(P)\to c^-$, never $<0$ in any run).

**This directly contradicts the round's premise** (last round's explorer's
$23{,}905$-trial finding of "substantial slack $\approx0.34$, no near-ties")
— that search evidently diluted the cut budget across both $P$ and $S'''$
(or did not push $\max(P)$ close enough to the boundary $c$), missing the
actual hard corner of Case B's parameter space. Section 15.3 below explains
*why* this corner is hard: it is not an isolated numerical artifact, but the
exact boundary of an already-known, still partially open sub-problem.

#### 15.3 The exact reduction: Case B's hardest sub-case is literally the file's own TOP-ONLY complementary regime, one level down

**Theorem N (Case B $\equiv$ TOP-ONLY$(m-1)$, complementary regime, on the
$S'''$-unsplit-full-budget slice).** Fix $m\ge3$ and set $m':=m-1$. Consider
the sub-case of the Base Case (with $b_2=2^{m-1}$, per Lemma N) in which
$S'''=\Gamma_{m-3}$ exactly (zero cuts spent inside $S'''$), so the entire
budget $m-1$ is available for splitting $P$, i.e. $|P|\le m=m'+1$. Then the
target
$$\mathrm{OddSum}\bigl(P\cup\{2^{m-2}\}\cup S'''\bigr)\ \ge\ 2^{m-1}$$
is **literally identical**, term for term, to the statement
$$\mathrm{OddSum}\bigl(P\cup\Gamma_{m'-1}\bigr)\ \ge\ 2^{m'}, \tag{TOP-ONLY$(m')$}$$
i.e. exactly the general lower-bound TOP-ONLY claim for parameter $m'=m-1$,
applied to the partition $P$ of $2^{m'}$ into $\le m'+1$ parts — and Case
B's hypothesis $\max(P)<2^{m-2}=2^{m'-1}$ is exactly the hypothesis of
TOP-ONLY$(m')$'s **complementary (non-Dominance-Chain) regime**, i.e. the
regime the Dominant-Chain Theorem (Theorem 5, this file) does *not* cover
and which is (per `current.md`'s Current-best summary and
`self-similar-induction-on-n`'s own file) only *partially* closed in
general, with a genuine residual open window remaining near
$\max(P)\to2^{m'-1}{}^-$.

*Proof.* Immediate from matching every symbol. $\{2^{m-2}\}\cup S'''=
\{2^{m-2}\}\cup\Gamma_{m-3}=\Gamma_{m-2}$ exactly (adjoining the single
element $2^{m-2}$ to the top of $\Gamma_{m-3}=\{2^{m-3},\dots,2^0\}$
reproduces $\Gamma_{m-2}=\{2^{m-2},2^{m-3},\dots,2^0\}$ verbatim, by
definition of $\Gamma$), and $\Gamma_{m-2}=\Gamma_{m'-1}$ since $m'=m-1$. So
the left side of the Base Case's target is literally
$\mathrm{OddSum}(P\cup\Gamma_{m'-1})$. The right side $2^{m-1}=2^{m'}$
matches by the same substitution. $\mathrm{sum}(P)=2^{m-1}=2^{m'}$ (Base
Case hypothesis), so $P$ is a genuine partition of $2^{m'}$, and the piece
cap $|P|\le m'+1$ (this sub-case's budget, shown above) matches
TOP-ONLY$(m')$'s own admissible piece count exactly ($j\le m'$ fragments,
i.e. $|P|=j+1\le m'+1$, since XY's marking budget for splitting a single
top piece is $\le n=m'$ cuts in the original two-phase game, exactly the
content of Lemma 2/Reduction). Finally $\max(P)<2^{m-2}=2^{(m-1)-1}=
2^{m'-1}$ is verbatim the "$a_1<2^{m'-1}$" hypothesis defining TOP-ONLY's
complementary regime (the negation of the Dominance-Chain property's own
top-level requirement $a_1\ge2^{m'-1}$). $\blacksquare$

**Consequence.** This is not a resemblance or an analogy — it is an exact,
symbol-for-symbol identification. Every already-proved partial result about
TOP-ONLY's complementary regime therefore transfers immediately, with no
new argument needed, to this slice of Case B:

- **Theorem 6 (Large-Violation-Depth closure, already certified, this
  file)** applies verbatim whenever $m'=m-1\ge3$ (i.e. $m\ge4$) and
  $\max(P)<2^{m'-3}=2^{m-4}$: it gives
  $\mathrm{OddSum}(P\cup\Gamma_{m-2})\ge2^{m-1}$ (in fact strictly $>$),
  **closing this sub-case of Case B outright**, with no new proof required.
  As already documented in Section 8's own honest scope note, this sub-case
  is *vacuous* for $m-1\le7$ (i.e. $m\le8$): the piece cap $|P|\le m$ forces
  $\max(P)\ge\mathrm{sum}(P)/|P|\ge2^{m-1}/m\ge2^{m-4}$ by pigeonhole
  whenever $m\le8$ (identical arithmetic to Section 8's own vacuity
  argument, shifted by one in $m$), so it only becomes a genuine additional
  closure from $m\ge9$ on.
- For $2^{m-4}\le\max(P)<2^{m-2}$ (the region Theorem 6 does not reach): this
  is **exactly** the region `self-similar-induction-on-n`'s own file
  reports as "closed except a narrow residual near $a_1=2^{m'-1}$" (see
  `current.md`'s Current-best summary, and that file's own trichotomy
  sections) — i.e. mostly already handled by that approach's certified
  partial results (imported by name, not re-derived here, since re-deriving
  them is that approach's own job, not this one's), with a genuine open
  residual, the **Branch-I.A-restricted window**, exactly coinciding —
  after the $m'=m-1$ substitution — with the corner Section 15.2's stress
  test found the near-zero-margin instance in.

**This is the round's actual, honest finding: Case B is not a fresh,
independently-easier sub-problem with its own "quick win" — its hardest
instances are the *same* instances (up to the exact bijection given by
Theorem N) as the file's own already-catalogued, still-partially-open
TOP-ONLY residual.** Any future proof that closes the Branch-I.A-restricted
window (currently the joint responsibility of `self-similar-induction-on-n`
and this file) closes this slice of Case B for free, and conversely a direct
attack on Case B that ignored this connection would risk reproving the same
open sub-problem twice under a different name. We record this explicitly so
neither approach re-derives it independently.

**Scope note (what Theorem N does and does not close).** Theorem N handles
only the $S'''$-unsplit-full-budget slice of Case B. The general Case B
statement additionally allows $S'''$ to be split (using some of the budget
there instead of all of it on $P$), a strictly larger configuration space
not covered by Theorem N or by TOP-ONLY$(m')$ as stated (which has no
tail-splitting at all — recall Section 9's Leftover-Fragment Obstruction is
exactly about tail levels being split, and here even the "tail" $S'''$ is,
in the TOP-ONLY correspondence, playing the role of $\Gamma_{m'-1}$ itself,
so splitting $S'''$ would correspond to splitting *part of* TOP-ONLY's own
tail — a strictly different, still harder question than TOP-ONLY as
literally stated). So Theorem N is a **partial** closure (the hardest known
sub-slice, matching where the near-zero-margin instance actually lives, is
handled by transfer, but the full Case B statement, over every possible
$S'''$ shape, remains open). Numerically, this is consistent with the round-
10 search: every one of the $23{,}905$ Case B trials that found "substantial
slack" necessarily spent some budget splitting $S'''$ (diluting away from
the hard corner), which is exactly why they missed the near-tight instances
Section 15.2 found by concentrating the budget on $P$ alone.

#### 15.4 Case A: not attempted this round (time), one precise structural note recorded instead of a hand-wave

Per the dispatch, Case A ($\max(P)\ge2^{m-2}$) was the lower-priority target
this round and was not reached in a proof attempt. We record one honest,
rigorous observation in its place, to redirect (not replace) a future
round's effort: applying the identical $S'''=\Gamma_{m-3}$-unsplit
specialization of Section 15.3 to Case A does **not** trivially reduce to
the already-certified Dominant-Chain Theorem (Theorem 5), even though
$\max(P)\ge2^{m-2}=2^{m'-1}$ looks superficially like Theorem 5's own
hypothesis $a_1\ge2^{m'-1}$. Theorem 5 requires the *full* recursively-
defined Dominance-Chain property of $P$ at level $m'$ (every fragment, all
the way down the sorted list, dominating the corresponding level), not just
a bound on the single largest fragment $\max(P)$ — and nothing in Case A's
hypothesis (`$\max(P)\ge2^{m-2}$` alone) forces the *rest* of $P$'s sorted
list to satisfy the chain condition at the lower levels. So Case A's
$S'''$-unsplit slice is, precisely, an instance of the **still-open general
joint interleaved regime** of TOP-ONLY (top fragment dominates but the
chain may fail further down) — the same "unknown interleaving" difficulty
this file's Section 9.4 (Leftover-Fragment Obstruction) and
`self-similar-induction-on-n`'s own middle-regime gap already document as
unresolved. This gives a rigorous (not merely numeric) explanation for why
last round's explorer found Case A "inherits the identical peel+insert
shortfall as the general problem": it is not a coincidence, it is because
Case A's easiest-looking slice is literally an unclosed instance of that
same general problem, by the identical mechanism identified for Case B in
Section 15.3 above, just landing in the *harder* (Dominance-Chain-adjacent
but not verified) half rather than the complementary half. No proof is
claimed here; this is a scope diagnosis, recorded honestly as unattempted
work, not a closure.

#### 15.5 Net effect of Section 15

**Newly proved in full, promotable:** Lemma N (WLOG $b_2=2^{m-1}$, formal
proof with the previously-implicit $|P|\ge2$ fact made explicit) and
Theorem N (the exact equivalence, on the $S'''$-unsplit-full-budget slice,
between Case B and TOP-ONLY$(m-1)$'s complementary regime), together with
the corollary that Theorem 6 already closes a genuine (if vacuous-until-
$m=9$) piece of Case B outright with no new work.

**Newly and precisely corrected (a real finding, not a failure to find a
proof):** the round's "Case B is a quick win, substantial slack, no near-
ties" premise is **false as searched** — an exact counterexample-to-the-
premise instance is exhibited (margin $19/81977\approx0.00023$, not
$\approx0.34$), and Theorem N explains structurally *why* the true hard
corner was missed (it requires concentrating, not diluting, the cut budget)
and *what* the hard corner actually is (not a new phenomenon, but the file's
own already-partially-worked-on TOP-ONLY residual, one level down). This
redirects future effort: closing Case B in full is now known to require
either closing the Branch-I.A-restricted window (already the target of
`self-similar-induction-on-n`) or finding a genuinely new argument that
handles $S'''$-splitting on top of that — not a standalone "insertion" trick
as the round's skeleton proposed.

**Left open, honestly:** Level-Absorption's Base Case is not closed. Case A
is untouched beyond the Section 15.4 diagnosis. Case B is reduced (on its
hardest identified slice) to an exact restatement of a known partially-open
problem, not resolved. The Base Case as a whole, and hence Level-Absorption
and Theorem 7'$(m,k;L)$'s inductive step, remain open.

## Promotable lemmas

- **Lemma N (WLOG $b_2=2^{m-1}$)** (Section 15.1, new this round): for the
  Level-Absorption Base Case ($k=2$), it suffices to prove the target for
  $b_2=2^{m-1}$ exactly; every smaller admissible $b_2\in[2^{m-2},2^{m-1})$
  follows a fortiori. Proved in full by a direct monotonicity argument
  (neither $P$, $S'''$, nor the cut budget depend on $b_2$), with the
  previously-implicit fact $|P|\ge2$ made explicit and proved. Reusable
  directly by any future attempt at Level-Absorption's Base Case.
- **Theorem N (Case B $\equiv$ TOP-ONLY$(m-1)$'s complementary regime, on
  the $S'''$-unsplit-full-budget slice)** (Section 15.3, new this round):
  Level-Absorption's Base Case, restricted to $S'''=\Gamma_{m-3}$ (unsplit)
  and $b_2=2^{m-1}$ (via Lemma N), is symbol-for-symbol identical to the
  general TOP-ONLY lower-bound claim at parameter $m-1$, restricted to its
  complementary (non-Dominance-Chain) regime $\max(P)<2^{m-2}$. Proved in
  full by direct substitution/identification of every symbol (no numeric
  step). Immediately gives, as corollaries with zero new proof: (a) the
  already-certified Theorem 6 (Large-Violation-Depth closure) closes the
  sub-slice $\max(P)<2^{m-4}$ outright, for $m\ge9$ (vacuous below by the
  identical pigeonhole argument as Theorem 6's own scope note); (b) the
  remaining sub-slice $2^{m-4}\le\max(P)<2^{m-2}$ coincides exactly with
  `self-similar-induction-on-n`'s own Branch-I.A-restricted window, so any
  future closure of that window closes this slice of Case B for free.
  Reusable directly by any future round working on either Level-Absorption
  or the TOP-ONLY complementary-regime / Branch-I.A window, to avoid
  duplicating effort under two different names.
- **Greedy-Optimality Lemma** (Section 1, Lemma 1): for any finite
  multiset of positive reals, the alternating-claim game (first player
  claims any unclaimed element, maximizing own total) has value
  $\mathrm{OddSum}$ (sum of odd-ranked elements sorted descending), and
  "always claim a currently-largest element" is optimal for both players
  including under ties. Proved in full by induction with an explicit
  exchange inequality $(\ast\ast)$. Fully self-contained, reusable by any
  approach that reduces to a fixed-multiset claiming game.
- **Reduction Lemma** (Section 2, Lemma 2): the full two-phase
  marking-then-claiming game's value equals the stated minimax over
  length-multisets (partition into $\le n+1$ parts, refined by $\le n$
  further cuts). Proved in full; establishes position-irrelevance as a
  corollary of the argument (order of pieces on the stick never affects
  reachability of any multiset, nor payoff).
- **Global-max Peeling Lemma** (Section 3, Lemma 3): for any finite
  multiset $M$ with $g=\max(M)$,
  $\mathrm{OddSum}(M)=g+\mathrm{EvenSum}(M\setminus\{g\})$. Proved in full;
  directly reusable and is exactly the tool that gives the clean Case-1
  lower bound (Section 4) with no induction needed.
- **Lower-bound Case 1** (Section 4): if XY's response never cuts LB's
  own largest piece, $\mathrm{OddSum}\ge c(n)$ unconditionally, for every
  $n$ and every such response — proved in full, an immediate corollary of
  the Peeling Lemma plus $\mathrm{EvenSum}\ge0$.
- **Complete $n=0,1$ solution** (Section 5): $c(0)=1$, $c(1)=2/3$, both
  directions proved in full via a direct 3-element median computation.
  Reusable as a certified base case for any inductive approach (e.g.
  `self-similar-induction-on-n`) attempting a strong induction on $n$.
- **Lemma 4 / Greedy-floor guarantee against an arbitrary opponent**
  (Section 4b, new this round): if Player 1 (resp. Player 2) plays the
  greedy rule "always claim a currently-largest unclaimed element" on
  every one of its own turns, its total is $\ge\mathrm{OddSum}(N)$ (resp.
  $\ge\mathrm{EvenSum}(N)$), **regardless of the opponent's strategy** —
  strictly stronger than Lemma 1, which only asserts this when *both*
  players are optimal. Proved in full using only the already-certified
  inequality $(\ast)$ from Lemma 1's own proof plus the Global-max Peeling
  Lemma; self-contained and reusable by any future approach that wants a
  guaranteed floor for one player against an unknown/adversarial opponent
  (e.g. as a building block for a genuine interleaving argument, though —
  as documented in Section 4b — a *naive* static-priority use of it does
  not by itself close Lower-bound Case 2).
- **Companion Peeling Lemma** (Section 7.1, Lemma 5, new this round): for
  any finite multiset $N$ of positive reals with $g=\max(N)$,
  $\mathrm{EvenSum}(N)=\mathrm{OddSum}(N\setminus\{g\})$. Proved in full
  from already-certified facts alone (Lemma 3 plus the elementary
  $\mathrm{OddSum}+\mathrm{EvenSum}=\mathrm{sum}$ identity), no new
  induction. Directly reusable anywhere a multi-step "peel the current
  global max" argument is needed (used twice per level in the Dominant-Chain
  Theorem below, and by the Prefix-Run Decomposition Lemma).
- **Dominant-Chain Theorem** (Section 7.2, Theorem 5, new this round): for
  $m\ge0$, a descending sequence $a_1\ge\cdots\ge a_k>0$ with
  $\sum a_i\le2^m$ that has the recursively-defined "Dominance-Chain
  property at level $m$" ($a_1\ge2^{m-1}$ and the tail
  $(a_2,\dots,a_k)$ has the property at level $m-1$, or $k=0$) satisfies
  $\mathrm{OddSum}(\{a_1,\dots,a_k\}\cup\Gamma_{m-1})\ge\sum a_i$, where
  $\Gamma_{m-1}=\{2^{m-1},\dots,2^0\}$. Proved in full by strong induction
  on $k$ using only Lemma 3 and Lemma 5. A genuine strict generalization of
  the original Lower-bound Case 1 (which is the $k\le1$ special case);
  reusable by any approach needing a lower bound on
  $\mathrm{OddSum}(A\cup\Gamma_{m-1})$ for a split $A$ whose fragments
  dominate the tail level-by-level (in particular applicable directly to
  the known equality-attaining self-similar construction, verified this
  round to satisfy the hypothesis at every level for every $n$ tested).
- **Prefix-Run Peeling Decomposition Lemma** (Section 7.3, Lemma 6, new
  this round): for $a_1\ge\cdots\ge a_k>0$ with $a_1<2^{m-d}$ (top fragment
  smaller than the top $d$ tail values), $\mathrm{OddSum}(A\cup\Gamma_{m-1})$
  decomposes exactly as (known quantity) $\mathrm{OddSum}$ of the removed
  top-$d$ tail run, plus $\mathrm{OddSum}$ or $\mathrm{EvenSum}$ (depending
  on the parity of $d$) of $A$ merged with the shrunk tail
  $\Gamma_{m-d-1}$. Proved in full, unconditionally (no domination
  hypothesis needed — this is a pure structural identity about sorted
  merges). Reusable by any future attempt at the complementary
  (non-dominant) regime; this round's write-up (Section 7.3) also records,
  as a precise (not hand-waved) diagnosis, exactly which residual bound
  this decomposition reduces to and why that residual bound is false in
  its natural unrestricted form — useful negative information for whoever
  attempts this regime next.
- **Lemma 7 (Odd–Even Domination)** (Section 8.1, new this round): for any
  finite multiset $N$ of positive reals, $\mathrm{OddSum}(N)\ge
  \mathrm{EvenSum}(N)$ unconditionally. Proved in full by an elementary
  pairwise-descending-consecutive-pairs argument; fully general (no
  hypothesis on $N$ beyond finiteness/positivity), and directly reusable
  anywhere a floor on $\mathrm{EvenSum}$ (or ceiling on $\mathrm{OddSum}$)
  relative to the total sum is needed.
- **Lemma 7′ (EvenSum floor via max)** (Section 8.1, new this round): for
  any nonempty finite multiset $X$ with $g=\max(X)$,
  $\mathrm{EvenSum}(X)\ge(\mathrm{sum}(X)-g)/2$. Proved in full from Lemma 7
  plus the Companion-Peeling-style rank-shift observation
  ($\mathrm{EvenSum}(X)=\mathrm{OddSum}(X\setminus\{g\})$, the same fact as
  the certified Companion Peeling Lemma, re-derived directly here).
  Reusable anywhere a lower bound on $\mathrm{EvenSum}$ of a fixed-sum
  multiset is needed knowing only its maximum and total.
- **EvenSum-superadditivity (imported dual of certified Lemma S)** (Section
  8.1): $\mathrm{EvenSum}(P\cup Q)\ge\mathrm{EvenSum}(P)+\mathrm{EvenSum}(Q)$,
  an immediate one-line consequence of certified Lemma S
  (`lemmas/perfect-pairing-subadditivity-and-general-insertion.md`) via
  $\mathrm{Odd}+\mathrm{Even}=\mathrm{sum}$. Recorded here as a directly
  reusable fact (not new content beyond Lemma S, but useful to have stated
  in this dual form).
- **Theorem 6 (Large-Violation-Depth closure)** (Section 8.3, new this
  round): for $m\ge3$ and any partition $A=\{a_1\ge\cdots\ge a_j>0\}$ of
  $2^m$ with $a_1<2^{m-3}$, $\mathrm{OddSum}(A\cup\Gamma_{m-1})>2^m$. Proved
  in full by combining the certified Prefix-Run Peeling Decomposition Lemma
  (at $d=3$) with Lemma 7′ and EvenSum-superadditivity, plus exact
  closed-form geometric-sum algebra (Facts G1, G2) checked for both
  parities of $m$; independently cross-verified by $36{,}611$ random
  brute-force instances ($m=8,\dots,15$, the first non-vacuous range) with
  zero violations. A genuine strict extension of the covered TOP-ONLY
  region beyond the Dominant-Chain Theorem — imposes no domination
  condition at all on $a_2,\dots,a_j$, only a bound on $a_1$ alone.
  Reusable by any future attempt at the complementary regime as a certified
  "large $a_1$-deficit" building block; Section 8.4 records, with full
  proof (not just numeric suggestion), that the same mechanism fails hard
  at $d=1$ (negative, exponentially-growing-in-$m$ margin) and is
  structurally inapplicable at any even $d$ (would require the false
  direction of Lemma S), precisely bounding the remaining open region to
  $2^{m-3}\le a_1<2^{m-1}$.
- **Lemma 8 (General Domination Prefix-Run Lemma)** (Section 9.1, new this
  round): for finite multisets $P=\{p_1\ge\cdots\ge p_t\}$ and $Q$ of
  positive reals with $p_t\ge\max(Q)$,
  $\mathrm{OddSum}(P\cup Q)=\mathrm{OddSum}(P)+\mathrm{OddSum}(Q)$ if $t$
  even, $=\mathrm{OddSum}(P)+\mathrm{EvenSum}(Q)$ if $t$ odd. Proved in full,
  unconditionally (no geometric or other structural assumption on $P$ or
  $Q$ beyond the domination hypothesis) — a strict generalization of the
  certified Prefix-Run Peeling Decomposition Lemma (Lemma 6), which is
  exactly the special case $P=\Gamma_{[m-d,m-1]}$. Directly reusable
  anywhere a dominating "run" needs to be peeled off a merge in bulk,
  regardless of whether the dominant block has any particular internal
  structure.
- **Theorem 7 (Joint Dominance-Chain Closure, top-levels-clear)** (Section
  9.2, new this round): for $0\le k\le m$, a Dominance-Chain-property split
  $b_1\ge\cdots\ge b_k>0$ of (at most) $2^m$, and *any* refinement $S$ of
  $\Gamma_{m-1}$ whose top $k$ levels ($2^{m-1},\ldots,2^{m-k}$) are left
  entirely unsplit (arbitrary splitting allowed on the remaining $m-k$
  lower levels), $\mathrm{OddSum}(B\cup S)\ge\sum b_i$. Proved in full by
  strong induction on $k$, using only Lemma 3 (Global-max Peeling), Lemma 5
  (Companion Peeling), and Lemma 8. This is the first proved closure in
  this file's population of any instance of the general Case 2 combining
  $j\ge1$ actual top-piece cuts *with* $c\ge1$ actual tail cuts
  simultaneously (not just TOP-ONLY); it strictly generalizes the certified
  Dominant-Chain Theorem (Theorem 5), which is exactly the $k=m+1$/$c=0$
  boundary case. Reusable by any future attempt at the general Case 2 as
  a certified "clear the top levels first" building block; Section 9.4
  records, as a precise (not hand-waved) diagnosis — the **Leftover-
  Fragment Obstruction** — exactly why the identical technique does not
  extend to allow splitting of the top tail levels themselves, useful
  negative information for whoever attempts the fully interleaved case
  next.
- **Theorem 7a (k=1 base case of Theorem 7'(m,k;L))** (Section 10.1, new
  this round): for $b_1\ge2^{m-1}$ and *any* refinement $S$ of
  $\Gamma_{m-1}$ (every level may be split arbitrarily, not just the top
  tail level), $\mathrm{OddSum}(\{b_1\}\cup S)\ge b_1$. Proved in full by
  a single application of the Global-max Peeling Lemma plus
  $\mathrm{EvenSum}\ge0$; unconditional, $f(L)\equiv0$ for all $L$, no
  restriction on which levels of the tail are split. Directly reusable as
  the clean base case of any future attempt at the general Theorem
  7'$(m,k;L)$ induction, and as an independent re-derivation (in the
  Dominance-Chain/$\Gamma$ formalism) of the original Case-1 Theorem's
  content for $b_1\ge2^{m-1}$ rather than $b_1=2^m$ exactly.
- **Theorem 12 (Single-Insertion Monotonicity)** (Section 12.2, new this
  round): for any finite multiset $N$ of positive reals and any $v>0$,
  $0\le\mathrm{OddSum}(N\cup\{v\})-\mathrm{OddSum}(N)\le v$ — inserting one
  new positive value into a multiset can only weakly *increase*
  $\mathrm{OddSum}$, never decrease it. Proved in full from scratch (a
  direct position-parity argument, the same style as Lemma 1's own proof of
  $(\ast)$, plus a 3-line elementary sub-lemma on alternating sums of
  nonnegative sequences, Lemma 9), independently re-verified against the
  already-certified Single-Insertion Lemma's $\Delta\mathrm{AltSum}$ formula
  as a consistency check (they agree exactly), and independently stress-
  tested with $40{,}000$ exact-`Fraction` trials (including a dedicated
  tie-heavy pass) with zero violations. General-purpose and unconditional:
  no hypothesis on $N$ or $v$ beyond finiteness/positivity. Directly
  reusable anywhere a "new mass is being added" (as opposed to "existing
  mass is being re-split," a genuinely different and, as documented
  elsewhere in this file, *not* monotone operation) argument is needed.
- **Theorem 13 (General Insertion Monotonicity)** (Section 12.3, new this
  round): for any two finite multisets $N,R$ of positive reals (arbitrary
  size/shape/sum for $R$, no relation to $N$ required),
  $\mathrm{OddSum}(N\cup R)\ge\mathrm{OddSum}(N)$. Proved in full by an
  immediate induction on $|R|$ chaining Theorem 12; independently stress-
  tested with $30{,}000$ further exact-`Fraction` trials, zero violations.
  This closes **Open Sub-Problem A (Insertion-Robustness)** in full,
  unconditionally, and in a strictly stronger form than originally boxed
  (drops the hypothesis $\max(R_1)\le\mu_1$ entirely — it is not needed).
  Directly reusable by any future approach needing a lower bound on
  $\mathrm{OddSum}$ after adding arbitrary extra mass to an already-analyzed
  multiset.
- **Lemma L (Unsplit-Baseline)** (Section 13.1, new this round): with
  $B''=\{b_3,\dots,b_k\}$ Dominance-Chain at level $m-2$
  ($\mathrm{sum}(B'')\le2^{m-2}$) and $S''$ a refinement of $\Gamma_{m-2}$
  with top $k-1$ levels unsplit, if the value $2^{m-1}$ (level $m-1$) is
  itself left **unsplit** and merged in, then
  $\mathrm{OddSum}(S''\cup B''\cup\{2^{m-1}\})\ge2^{m-1}\ge b_2+\mathrm{sum}(B'')$
  whenever $\{b_2\}\cup B''$ has the Dominance-Chain property at level
  $m-1$. Proved in full by chaining two already-certified facts (Theorem 7a
  applied at parameter $M=m-1$, then Theorem 13 to insert $B''$), no new
  induction needed. Isolates the entire remaining difficulty of Open
  Sub-Problem B (Level-Absorption) to a single precisely quantified
  "re-splitting degradation" question (Section 13.2), with an explicit
  slack $\Sigma=2^{m-1}-b_2-\mathrm{sum}(B'')\ge0$ available to absorb it.
  Directly reusable by any future attempt at Level-Absorption, or by any
  other approach needing a clean baseline bound for "one dominance-chain
  level, otherwise untouched, inserted into a smaller already-analyzed
  Theorem-7-type object."
- **Lemma M ($B''$-Banking Lemma)** (Section 14.1, new this round): with
  $B''=\{b_3,\dots,b_k\}$ Dominance-Chain at level $m-2$
  ($\mathrm{sum}(B'')\le2^{m-2}$) and $S'''$ a refinement of $\Gamma_{m-3}$
  with top $k-2$ levels unsplit, $\mathrm{OddSum}(B''\cup S''')\ge
  \mathrm{sum}(B'')$. Proved in full as a direct instance of the
  already-certified **general** Theorem 7 (Joint Dominance-Chain Closure)
  applied one level down at parameters $(m-2,k-2)$ — correcting the
  outline's own citation of Theorem 7a, which is only Theorem 7's $k'=1$
  base case and does not apply verbatim once $B''$ has $\ge2$ elements
  ($k\ge4$). Unconditional, no new induction needed. Directly reusable
  anywhere a Dominance-Chain sub-block's own contribution needs to be
  banked independently of an outer/parallel structure.
- **Candidate Swap Lemma — refuted** (Section 14.2, new this round): the
  natural structure-agnostic claim "$\mathrm{OddSum}(Q\cup P)\ge
  \mathrm{OddSum}(Q\cup\{b\})$ whenever $\mathrm{sum}(P)\ge b$ and
  $\max(P)<b$" is **false**, by an exact hand-checkable counterexample
  ($Q=\varnothing$, $b=10$, $P=\{6,6\}$: $\mathrm{OddSum}(P)=6<10$) and a
  $\sim36\%$ violation rate over $12{,}598$ randomized exact-`Fraction`
  trials. This rules out, as a class, any future attempt to close
  Level-Absorption (or a similarly-shaped "split value $b$, still beat the
  unsplit baseline" claim) via a structure-agnostic swap/replacement bound
  that ignores the background multiset $Q$'s own shape — a genuine,
  reusable negative result and a directly reusable counterexample template.

## Round 12 target: Theorem N's residual = the shared Branch-I.A window

**Result:** the window's monotonicity-in-$c_1$ question (gap (b), both the
piece-cap-unsaturated sub-case already covered by Lemma TPI and the
piece-cap-saturated sub-case (b)(ii), previously untouched) is **fully
closed in one uniform argument** (Section 16), via a new general-purpose
**Elementwise Monotonicity Lemma** for $\mathrm{OddSum}$ combined with the
observation that $c_1$ is *always* the (weak) maximum of the whole
multiset throughout the window. This gives the **Window Reduction
Theorem**: the entire window target is equivalent to the single left-
endpoint statement alone (for *every* admissible $D$ there, not just
Theorem W's one witness) — i.e. exactly gap (a) in full generality, with
gap (b) eliminated entirely as a separate difficulty. Independently
re-derives (via a one-line Peel-the-Max computation, a different route)
the sibling file's own certified endpoint-reduction identity, cross-
confirming it. Gap (a) itself (does the target hold for *every* admissible
$D$ at the endpoint, not just the tied-pair witness) is **not** closed;
extensive exact-rational stress-testing (Section 16.5) supports it
strongly (margin exactly $\varepsilon/2$ found as the minimum at every
tested $(\ell,\varepsilon)$, always at the tied-pair-shape witness) but
this is evidence, not proof — consistent with the explorer's diagnosis
that gap (a) is the field's genuinely hard remaining residual. See
Section 16 for full detail, including a full account of a subtlety missed
on a first pass (the $|D|=1$ boundary case needs the "insert a fresh
element" mechanism, not the "grow an existing element" mechanism, since
headroom on a lone element is provably short by exactly $\varepsilon$).

Round 12's `shared-top-only` explorer report
(`/tmp/round-12/math-explorer-shared-top-only.md`) confirmed, symbol-for-
symbol, that Theorem N's residual (the $S'''$-unsplit-full-budget slice
of Level-Absorption's Case B, restricted to the complementary
non-Dominance-Chain regime of TOP-ONLY$(m-1)$) is the *same* open claim as
`self-similar-induction-on-n`'s Branch-I.A-restricted window:
$$c_1\in[2^{\ell-1},\,2^{\ell-1}+1-\varepsilon),\quad
\max(C\setminus\{c_1\})<2^{\ell-1},\quad\mathrm{sum}(C)=2^\ell+\varepsilon,
\quad|C|\le\ell+1,\qquad \ell=m-1,$$
target $\mathrm{OddSum}(C\cup\Gamma_{\ell-1})\ge2^\ell$. Combining this
file's own Dominant-Chain/Large-Violation-Depth closure with the sibling
file's Case-B(m,k) sliver reduction (Theorem 2) narrows what's genuinely
open to exactly this window — much narrower than "the whole complementary
regime," which is what this file alone reports.

**Recommended next step (do not re-derive independently — coordinate with
`self-similar-induction-on-n`, which owns Theorem W and Lemma TPI on this
same object):** attack the window via route (a), a self-referential
strong induction on $\ell$ mirroring round 8's Branch-II mechanism — see
`self-similar-induction-on-n.md`'s Round 12 Target 1 for the full
dichotomy plan, caution about the induction hypothesis possibly needing
strengthening, and the warning that naive numerical search (gradient- or
box-vertex-based) is unreliable here because the true extremal structure
is an internally tied pair, not a box corner (Theorem W's own witness
shape). If this file's builder makes progress on the window from the
Level-Absorption side, write it directly in terms of the shared window
statement above so it is immediately transferable to the sibling file
(and vice versa) — avoid duplicating proof effort on what is now known to
be one object, not two.

## Section 16: the Window Reduction Theorem (gap (b) fully closed)

Throughout this section, fix $\ell\ge2$, $\varepsilon\in(0,1)$; write
$\mathrm{cap}:=2^{\ell-1}$, $T:=\Gamma_{\ell-1}$ (so $\max(T)=\mathrm{cap}$,
$\mathrm{sum}(T)=2^\ell-1$). Recall the shared window: $C$ is
**admissible** if $C=D\cup\{c_1\}$ for a finite multiset $D$ of positive
reals with $\max(D)<\mathrm{cap}$, $c_1\in[\mathrm{cap},\mathrm{cap}+1
-\varepsilon)$, $|C|\le\ell+1$ (i.e. $|D|\le\ell$), and $\mathrm{sum}(C)
=2^\ell+\varepsilon$. The window target is $\mathrm{OddSum}(C\cup T)\ge
2^\ell$ for every admissible $C$.

### 16.1 Elementwise Monotonicity Lemma (new, general-purpose)

**Statement.** Let $N$ be any finite multiset of positive reals (possibly
empty). Then the map $x\mapsto\mathrm{OddSum}(N\cup\{x\})$ is non-decreasing
on $(0,\infty)$.

**Proof.** Fix $0<x_1<x_2$. Sort $N$ descending as $y_1\ge\cdots\ge y_n$
(set $y_0:=+\infty$, $y_{n+1}:=0$ as sentinels). For $x\in(0,\infty)$ let
$r(x):=|\{i:y_i\ge x\}|\in\{0,\dots,n\}$; in $N\cup\{x\}$ sorted descending,
$x$ occupies rank exactly $r(x)+1$, the elements $y_1,\dots,y_{r(x)}$ keep
their original ranks $1,\dots,r(x)$, and $y_{r(x)+1},\dots,y_n$ are shifted
down to ranks $r(x)+2,\dots,n+1$. Hence
$$\mathrm{OddSum}(N\cup\{x\})=\sum_{\substack{1\le i\le r(x)\\ i\text{ odd}}}
y_i\ +\ [\,r(x)+1\text{ odd}\,]\cdot x\ +\!\!\sum_{\substack{r(x)<j\le n\\
j+1\text{ odd}}}\!\! y_j.$$
On any open interval $(y_{r+1},y_r)$ (where $r(x)\equiv r$ is constant),
only the middle term depends on $x$, and it is **linear in $x$ with slope
$[\,r+1\text{ odd}\,]\in\{0,1\}$** — in particular non-negative. The
function $\phi(x):=\mathrm{OddSum}(N\cup\{x\})$ is continuous on all of
$(0,\infty)$ (it is the composition of $x\mapsto N\cup\{x\}$, continuous
into the space of $(n+1)$-tuples of reals with the obvious topology, with
the sort-and-sum-odd-ranks map, which is continuous — a finite composition
of sorting, a continuous operation, and a linear projection). A continuous,
piecewise-linear function on $(0,\infty)$ whose slope is $\ge0$ on every
open piece of a locally finite partition (the finitely many points
$y_1,\dots,y_n$) is non-decreasing on the whole domain: for $x_1<x_2$,
writing $x_1=t_0<t_1<\cdots<t_k=x_2$ for the finitely many $y_i$ strictly
between them (in increasing order), $\phi$ is non-decreasing on each closed
sub-interval $[t_{j-1},t_j]$ (linear there, or continuous limit of the
linear pieces on either open side, matching at the shared endpoint by
continuity — at a tie point $x=y_i$ exactly, $\phi(y_i)$ equals both
one-sided limits since $\mathrm{OddSum}$ does not depend on how ties are
broken, only on the multiset of values), hence non-decreasing on the whole
interval $[x_1,x_2]$ by chaining. $\blacksquare$

*(Independent stress test: $20{,}000$ random exact-`Fraction` trials,
$|N|=0,\dots,7$, values and $x_1\le x_2$ random rationals: zero violations
of $\mathrm{OddSum}(N\cup\{x_1\})\le\mathrm{OddSum}(N\cup\{x_2\})$.)*

**Remark.** This is a genuinely different fact from the already-certified
Theorem 12/13 (Single-/General-Insertion Monotonicity,
`lemmas/insertion-monotonicity-theorems-12-13.md`), which bound the *gain*
from **inserting new mass** into an already-fixed multiset. Lemma EM
instead concerns **moving one existing coordinate's value**, with $N$ held
exactly fixed — the tool needed here, since the window's $c_1$ and $D$'s
elements are not being augmented but reallocated against a fixed budget.

### 16.2 Transfer Monotonicity Theorem

**Statement.** Fix a finite multiset $T_0$ of positive reals with
$\max(T_0)=\mu$, and a finite multiset $D$ of positive reals with every
element $<\mu$. Fix $c\ge\mu$ and $\delta\ge0$, and let $w_0\ge0$ be either
(a) the value of a chosen element $x\in D$ (so $w_0=x$), or (b) $0$
(representing "no element yet," i.e. a slot to be newly created). Assume
the two hypotheses
$$\delta\ \le\ c-\mu \qquad\text{and}\qquad \delta\ \le\ \mu-w_0,$$
(the first keeps $c-t\ge\mu$ throughout; the second keeps $w_0+t\le\mu$
throughout — automatically true for choice (b), $w_0=0$, whenever
$\delta\le\mu$). Let $D_t$ denote $D$ with the chosen element's value
replaced by $w_0+t$ for $t\in[0,\delta]$ (in case (b), $D_t:=D\cup\{t\}$
for $t>0$, and $D_0:=D$). Then
$$t\mapsto\mathrm{OddSum}\bigl(D_t\cup\{c-t\}\cup T_0\bigr)$$
is non-**increasing** on $[0,\delta]$; equivalently, writing $c':=c-\delta$,
$$\mathrm{OddSum}(D_0\cup\{c\}\cup T_0)\ \ge\ \mathrm{OddSum}(D_\delta\cup\{c'\}\cup T_0).$$
(I.e.: moving mass $\delta$ from $c$ into the chosen $D$-coordinate never
*increases* $\mathrm{OddSum}$; equivalently, moving mass from a $D$-element
into $c$ never *decreases* it.)

**Proof.** For every $t\in[0,\delta]$: $c-t\ge c-\delta\ge\mu$ directly by
the first hypothesis. Also the chosen coordinate's value $w_0+t\le w_0+
\delta\le\mu\le c-t$ by the second hypothesis, and every other element of
$D_t$ (unaffected, values $<\mu$ by the standing assumption on $D$) is
likewise $<\mu\le c-t$. A tie ($w_0+t=\mu$, possible only at $t=\delta$
under the second hypothesis' equality case) is harmless: $\mathrm{OddSum}$
does not depend on how tied values are broken, only on the multiset of
values. Hence $c-t=\max\bigl(D_t\cup\{c-t\}\cup T_0\bigr)$ (weakly) for
every $t\in[0,\delta]$. By the certified Global-max Peeling Lemma (Lemma 3,
`lemmas/dominant-piece-lower-bound.md`),
$$\mathrm{OddSum}\bigl(D_t\cup\{c-t\}\cup T_0\bigr)=(c-t)+\mathrm{EvenSum}
\bigl(D_t\cup T_0\bigr).$$
Write $N:=(D\setminus\{x\})\cup T_0$ in case (a) (resp. $N:=D\cup T_0$ in
case (b)), a multiset **fixed** in $t$. Then $D_t\cup T_0=N\cup\{w_0+t\}$,
so by Lemma EM (16.1), $\mathrm{OddSum}(N\cup\{w_0+t\})$ is non-decreasing
in $t$, piecewise-linear with slope $\in\{0,1\}$ a.e. (exactly the slope
computed in Lemma EM's proof, now as a function of $t$ via $x$-coordinate
$w_0+t$, chain rule factor $+1$). Since $\mathrm{EvenSum}(N\cup\{w_0+t\})=
\mathrm{sum}(N)+w_0+t-\mathrm{OddSum}(N\cup\{w_0+t\})$, its slope in $t$ is
$1-(\text{slope of OddSum})\in\{0,1\}$ a.e. as well — wait, we in fact
need the slope of $\mathrm{EvenSum}$, so: slope$(\mathrm{EvenSum})=1-
\text{slope}(\mathrm{OddSum})\in\{1-1,1-0\}=\{0,1\}$ a.e. Therefore
$$\frac{d}{dt}\Bigl[(c-t)+\mathrm{EvenSum}(D_t\cup T_0)\Bigr]=-1+\bigl(
\text{slope of EvenSum}\bigr)\in\{-1,0\}\quad\text{a.e.}$$
So the whole expression is continuous (composition of continuous maps, as
in 16.1) and piecewise-linear with slope $\le0$ a.e. on $[0,\delta]$, hence
non-increasing there, exactly the claim. $\blacksquare$

*(Independent stress test: see 16.5 — the theorem's two mechanisms, (a)
"grow an existing coordinate" and (b) "fill a fresh slot," are each tested
directly against exact-`Fraction` instances built from the window's own
data, not generic random instances, since the theorem's hypotheses
[$D<\mu\le c$] are specific to this setting; $0$ violations in $3{,}000+$
trials for each mechanism.)*

### 16.3 The headroom subtlety (found and fixed this round)

To reduce an admissible interior window point $C=(D,c_1)$, $c_1>\mathrm{cap}$,
down to an admissible point at $c_1=\mathrm{cap}$ using only Theorem 16.2's
mechanism (a) ("grow an existing $D$-coordinate"), one needs enough total
**headroom** $H:=\sum_{d\in D}(\mathrm{cap}-d)$ to absorb $\Delta:=c_1-
\mathrm{cap}$. A direct computation (using $\mathrm{sum}(D)=2^\ell+
\varepsilon-c_1$) gives, for $|D|=k$:
$$H-\Delta=(k-1)\,\mathrm{cap}-\varepsilon.$$
For $k\ge2$: $(k-1)\mathrm{cap}\ge\mathrm{cap}=2^{\ell-1}\ge2>1>\varepsilon$
(using $\ell\ge2$), so $H\ge\Delta$ with room to spare — mechanism (a)
alone suffices (split $\Delta$ across finitely many existing coordinates
one at a time, each step a valid instance of Theorem 16.2(a); this is
always possible in finitely many steps since the *total* headroom
suffices, even though no single coordinate's own headroom need be $\ge
\Delta$).

**But for $k=1$ exactly**, $(k-1)\mathrm{cap}=0<\varepsilon$, so
$H-\Delta=-\varepsilon<0$: the lone element's headroom is **short by
exactly $\varepsilon$**, and mechanism (a) alone is genuinely
insufficient (confirmed by direct construction: with $D=\{d_1\}$, $d_1=
2^\ell+\varepsilon-c_1$, growing $d_1$ up to $\mathrm{cap}$ exactly still
leaves $\varepsilon$ of $\Delta$ unabsorbed, and growing it *past*
$\mathrm{cap}$ would violate admissibility at the endpoint). This is
exactly where mechanism (b) ("fill a fresh slot") is needed instead: since
$\ell\ge2$, $k=1<\ell$ always, so $D_0:=\{d_1,\Delta\}$ has $|D_0|=2\le
\ell$, is a valid multiset ($\Delta\in(0,1-\varepsilon)\subset(0,\mathrm
{cap})$, $d_1<\mathrm{cap}$ unchanged), and $\mathrm{sum}(D_0)=d_1+\Delta=
(2^\ell+\varepsilon-c_1)+(c_1-\mathrm{cap})=\mathrm{cap}+\varepsilon$,
exactly right. Mechanism (b) applies directly (no headroom computation
needed at all for this route, since a fresh slot only needs $\Delta<\mu=
\mathrm{cap}$, always true).

**In fact mechanism (b) alone always suffices whenever $k<\ell$** (not
just $k=1$): insert $\Delta$ as one fresh element, giving $D_0:=D\cup
\{\Delta\}$, $|D_0|=k+1\le\ell$, no headroom check needed. Only the
saturated case $k=\ell$ genuinely requires mechanism (a) (no cardinality
room for a fresh slot) — and there, $k=\ell\ge2$ (since $\ell\ge2$),
exactly the regime where 16.3's headroom bound is ample. So **every**
admissible $(D,c_1)$ with $c_1>\mathrm{cap}$ reduces to an admissible
endpoint configuration $(D_0,\mathrm{cap})$ by a finite sequence of valid
Theorem-16.2 steps, using mechanism (b) if $k<\ell$ and mechanism (a) if
$k=\ell$.

### 16.4 Window Reduction Theorem

**Statement.** Fix $\ell\ge2$, $\varepsilon\in(0,1)$. Suppose the
**Endpoint Statement** holds: for every finite multiset $D_0$ with $|D_0|
\le\ell$, every element $<\mathrm{cap}$, and $\mathrm{sum}(D_0)=\mathrm{
cap}+\varepsilon$,
$$\mathrm{OddSum}\bigl(D_0\cup\{\mathrm{cap}\}\cup\Gamma_{\ell-1}\bigr)\ge2^\ell.$$
Then the full window target holds: $\mathrm{OddSum}(C\cup\Gamma_{\ell-1})
\ge2^\ell$ for **every** admissible $C=D\cup\{c_1\}$ in the window (any
$c_1\in[\mathrm{cap},\mathrm{cap}+1-\varepsilon)$, any admissible $D$).

**Proof.** Let $C=D\cup\{c_1\}$ be admissible, $k:=|D|$. First, $D\ne
\varnothing$: if $D=\varnothing$ then $c_1=\mathrm{sum}(C)=2^\ell+
\varepsilon\ge2^\ell=2\,\mathrm{cap}>\mathrm{cap}+1-\varepsilon$ (since
$\mathrm{cap}\ge2>1-\varepsilon-\varepsilon$, i.e. $\mathrm{cap}-1+2
\varepsilon>0$, true as $\mathrm{cap}\ge2,\varepsilon>0$), contradicting
$c_1<\mathrm{cap}+1-\varepsilon$; so $k\ge1$. If $c_1=\mathrm{cap}$, apply
the Endpoint Statement directly to $D_0:=D$ (valid: $|D_0|=k\le\ell$ since
$|C|=k+1\le\ell+1$). If $c_1>\mathrm{cap}$, by Section 16.3 there is a
finite sequence of admissible intermediate configurations linking $(D,c_1)$
down to some admissible endpoint configuration $(D_0,\mathrm{cap})$, each
consecutive pair related by one instance of Theorem 16.2 (mechanism (a) or
(b) as appropriate); chaining the theorem's conclusion across the finite
sequence gives
$$\mathrm{OddSum}(D\cup\{c_1\}\cup\Gamma_{\ell-1})\ \ge\ \mathrm{OddSum}
(D_0\cup\{\mathrm{cap}\}\cup\Gamma_{\ell-1})\ \ge\ 2^\ell$$
by the Endpoint Statement applied to $D_0$. $\blacksquare$

**Corollary (cross-check with the sibling's certified identity).** At the
endpoint itself, $c_1=\mathrm{cap}=\max(D_0\cup\{\mathrm{cap}\}\cup
\Gamma_{\ell-1})$ (weakly, tying only with $T$'s own top element, which
occurs once), so by Peel-the-Max, $\mathrm{OddSum}(D_0\cup\{\mathrm{cap}\}
\cup\Gamma_{\ell-1})=\mathrm{cap}+\mathrm{EvenSum}(D_0\cup\Gamma_{\ell-1})$.
The Endpoint Statement is thus equivalent to $\mathrm{EvenSum}(D_0\cup
\Gamma_{\ell-1})\ge\mathrm{cap}=2^{\ell-1}$. Since $\mathrm{cap}=\max
(\Gamma_{\ell-1})$ occurs once in $\Gamma_{\ell-1}$ and (as $D_0<\mathrm
{cap}$) is the unique max of $D_0\cup\Gamma_{\ell-1}$ too, the certified
Companion Peeling Lemma (Lemma 5,
`lemmas/dominant-chain-theorem-and-prefix-run-decomposition.md`) gives
$\mathrm{EvenSum}(D_0\cup\Gamma_{\ell-1})=\mathrm{OddSum}(D_0\cup
\Gamma_{\ell-2})$. So the Endpoint Statement is **exactly**
$$\mathrm{OddSum}(D_0\cup\Gamma_{\ell-2})\ge2^{\ell-1},$$
which is symbol-for-symbol the same target as the certified endpoint
reduction identity in
`lemmas/tiny-piece-insertion-monotonicity-and-endpoint-reduction.md`
(there derived via a sum/EvenSum algebraic identity instead of a direct
Peel-the-Max application). **Independent confirmation, by a different
route, that gap (a) — not gap (b) — is the field's one remaining
bottleneck for this window**, and that it is genuinely the same
recursive-in-$\ell$ object the sibling file already identified (not a
new, easier-looking restatement).

### 16.5 Stress testing (exact `Fraction`, not floats — per repo rule)

- **Lemma EM** (16.1): $20{,}000$ random trials, $|N|=0,\dots,7$, random
  rational values and $x_1\le x_2$: $0$ violations.
- **Theorem 16.2, mechanism (a)** ("grow an existing coordinate," used at
  $k=\ell$): $2{,}498$ trials built directly from random admissible
  window instances ($\ell=2,\dots,6$, random $\varepsilon$, random $c_1$
  in-window, random admissible saturated $D$ with $|D|=\ell$), greedily
  redistributing $\Delta$ across existing coordinates by available
  headroom: $0$ violations (and the "insufficient total headroom" case
  never triggered, matching the $k=\ell\ge2\Rightarrow H\ge\Delta$ proof).
- **Theorem 16.2, mechanism (b)** ("fill a fresh slot," used at $k<\ell$,
  specifically stress-tested at the tightest case $k=1$): $567$ trials,
  random admissible window instances with $|D|=1$: $0$ violations.
- **Window Reduction end-to-end** (general $k$, mixed mechanisms via
  proportional headroom split, restricted to trials where the naive
  proportional split happened to be feasible): $3{,}000$ trials, $0$
  violations (consistent with, but not superseding, the two targeted
  mechanism-specific tests above, which cover the genuinely tight case).
- **Gap (a) itself — evidence only, not a proof.** Exact-rational grid
  search (denominators up to $12$–$24$, $\ell=2,3,4$, several $\varepsilon$)
  for the *true* minimum of $\mathrm{OddSum}(D_0\cup\{\mathrm{cap}\}\cup
  \Gamma_{\ell-1})$ over admissible $D_0$ found, at every tested
  $(\ell,\varepsilon)$, minimum margin **exactly $\varepsilon/2$**, always
  attained at a tied-pair-shape $D_0$ generalizing Theorem W's witness
  (e.g. $\ell=4,\varepsilon=1/4$: minimizer $D_0=\{4,\,17/8,\,17/8\}$,
  margin $1/8=\varepsilon/2$ exactly). A separate scan of $c_1$ across the
  *whole* window (not just the endpoint), at several $(\ell,\varepsilon)$
  pairs, found the minimal-margin point always at $c_1=\mathrm{cap}$
  (consistent with, and giving independent numerical support to, the
  Window Reduction Theorem itself). **This is grid-search evidence at
  finitely many rational points, not a proof for continuous $D_0$ or
  general $\ell$** — gap (a) remains open. (Scripts and raw output
  available in this round's build log; not committed as separate files
  per repo convention of keeping only the approach `.md` files.)

### 16.6 Honest scope

**Closed this round:** gap (b) in full — both the piece-cap-unsaturated
sub-case (already covered by the certified Lemma TPI, now subsumed by a
strictly more general and uniform mechanism) and the piece-cap-saturated
sub-case (b)(ii), previously completely untouched by any approach. The
window's dependence on $c_1$ is now fully understood: monotonic, minimized
exactly at the left endpoint, for a clean structural reason (Peel-the-Max
+ elementwise monotonicity), not merely by numerical observation.

**Not closed:** gap (a) — the endpoint statement for *every* admissible
$D_0$, equivalently $\mathrm{OddSum}(D_0\cup\Gamma_{\ell-2})\ge2^{\ell-1}$.
This is now, rigorously and not just heuristically, **the entire remaining
content of the shared window** — confirmed by two independent routes
(this file's Peel-the-Max derivation and the sibling's sum/EvenSum
algebra) to be the same recursive-in-$\ell$ statement. Route (a) from this
round's explorer report (strong induction on $\ell$ mirroring round 8's
Branch-II mechanism) remains the most promising concrete next step; this
round's Elementwise Monotonicity Lemma may also be directly useful inside
that induction's own case analysis (e.g. for peeling/comparing $D_0$'s own
elements against $\Gamma_{\ell-2}$'s levels), a possible reuse not yet
attempted here for lack of time.
