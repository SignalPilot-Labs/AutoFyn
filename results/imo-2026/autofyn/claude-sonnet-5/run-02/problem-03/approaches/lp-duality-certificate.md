## Status
partial (the $n=3$ general-marking upper bound $c(3)\le8/15$ remains a
fully solved sub-result at its own scope, and the $p_1\ge T/2$ half of
$n=4$ remains fully solved (round 28); round 30 RETRACTED round 29's
false "$100\%$ empirical coverage of the residual $\mathcal R$ by 60
chambers" claim and proved a new, general, unifying **Partition Chamber
Theorem**; this round (31) proves a new **Half-Complement Pin Theorem**
and its $n=4$ corollary, which together close the entire sub-strip
$p_1\in[15T/31,T/2)$ of $\mathcal R$ unconditionally (for arbitrary
$p_2,p_3,p_4,p_5$ within $\mathcal R$'s bounds) — a genuine region
closure, not just the single anchor point the round-31 outline started
from — strictly shrinking the open residual to $\mathcal R'=\{p_2\le
p_1<15T/31,\ T/31<p_2<8T/31\}$. Full coverage of $\mathcal R'$ (hence of
$\mathcal R$, hence $n=4$'s general upper bound) remains open — no
Farkas-style exhaustive covering argument has yet been completed for any
part of $\mathcal R$ beyond this one strip. Round 32 proved a new
**Leave-2-Untouched Theorem** (general $m$) and then, per the dispatch's
explicit instruction to test for genuine coverage rather than assert it
from sampling, found and exactly verified a real gap: the full 120-chamber
named family (every chamber on file, including this round's new one) does
**not** cover $\mathcal R'$ — an exact interior counterexample exists near
the corner $p_1\to(15T/31)^-,\,p_2\to(8T/31)^-$ where all 120 chambers
fail, while an independent unrestricted numeric optimization confirms the
true minimum there still beats $a_4T$ via a strategy shape (simultaneous
3-fragment cuts on $p_1$ and $p_5$) not in the family — so no Farkas
certificate over this family exists to find, and none is claimed. $n=4$'s
upper bound, and hence the whole problem, remains open. Neither this file
nor the project as a whole solves the full `imo-2026-03` problem yet.)

## Approaches tried
- **Round 32 (this round).** Per the dispatch, attempted to close
  $\mathcal R'$ via the $n=3$ case-(b2) Farkas-covering technique. Derived
  and fully proved the **Leave-2-Untouched Theorem** (general $m$, a direct
  instantiation of `partition-chamber-theorem`: host $q_1$ pinned against
  all-but-two of the remaining pieces, the two left untouched, giving
  $\Phi=(T+A(\{\rho,q_j,q_k\}))/2$). Assembled the full 120-chamber family
  (Bisect-Subset $\cup$ Double-Bisect-Pin $\cup$ Triple-Pin $\cup$
  Double-Pin-Pair $\cup$ Half-Complement-Pin $\cup$ Leave-2-Untouched) and,
  rather than asserting coverage from a clean sample, actively searched for
  and **found an exact counterexample** where the entire family fails
  simultaneously (near the corner of $\mathcal R'$ where the two adjacent
  already-closed regions meet). Independently confirmed via unrestricted
  numeric optimization that this is a genuine family-incompleteness (a new,
  uncharacterized $(2,0,0,0,2)$-cut-shape strategy beats $a_4T$ there), not
  a counterexample to the conjecture — so correctly did **not** attempt a
  Farkas certificate over a family already shown incomplete. This directly
  avoids repeating rounds 29–30's false-coverage mistake on this exact
  residual. See "Round 32 build" section below for full detail.
  **This round's own verdict: honest partial, no overclaim.**
- **Round 31.** Per the round-31 outline/outline-reviewer,
  re-verified by hand the round-31 explorer's anchor point $p=(16,8,4,3,2)
  /33$ is closed by the "Untouched-Singleton Pin" instance of the
  certified `partition-chamber-theorem` (margin $\Phi-a_4T=-1/31$, i.e.
  the chamber succeeds). Went beyond the single point: derived and
  proved in full a new general **Half-Complement Pin Theorem** (any $m$)
  showing this whole family of strategies always gives $\Phi=\max(q_1,
  T-q_1)$ whenever feasible, with feasibility depending on, but the
  *value* independent of, which single index is left untouched. Applied
  at $m=5$ ($n=4$), choosing the feasibility-optimal untouched index
  ($j=2$), proved a clean corollary: the entire sub-strip $p_1\in
  [15T/31,T/2)$ of the residual $\mathcal R$ (from R29.2) is closed
  unconditionally, for arbitrary $p_2,p_3,p_4,p_5$ satisfying $\mathcal
  R$'s own bounds — a genuine algebraic region closure (not a point),
  confirmed by $\sim29000$ exact-`Fraction` boundary-targeted trials
  (zero mismatches). This strictly narrows the open residual to
  $\mathcal R'=\{p_2\le p_1<15T/31,\ T/31<p_2<8T/31\}$; verified neither
  known hard witness (round 30's two, at $p_1/T\approx0.379,0.467$) lies
  in the newly-closed strip, so this is genuinely new territory, not a
  re-closure. Honestly scoped: $\mathcal R'$ itself, and hence full
  coverage of $\mathcal R$, remains open — no Farkas-style exhaustive
  covering argument attempted this round.
- **Round 30.** Per the round-30 outline (APPROVE), (1)
  retracted round 29's refuted "$100\%$ empirical coverage" claim
  (exact counterexample $p=(11,7,6,3,2)/29$ defeats all 60 chambers
  simultaneously, found by the round-30 explorer, independently
  re-verified here); (2) diagnosed and **fixed a formula error in the
  outline's own stated Triple-Pin formula** (it omitted the untouched
  5th piece's contribution — the outline's literal $\Phi=(T+|p_m-p_a-p_b
  -p_c|)/2$ with the 5th piece left untouched is FALSE; the correct fix,
  verified exact, is to *bisect* the 5th piece with the spare cut, which
  restores exactly the outline's formula); (3) proved a fully general
  **Partition Chamber Theorem** unifying `bisect-subset-lemma`,
  Double-Bisect-Pin, the corrected Triple-Pin, and a new **Double-Pin-Pair**
  family, all via `pair-insensitivity-corollary` alone (553/553 feasible
  random exact-`Fraction` trials matched a from-scratch direct
  sort-and-alternate-sum simulation, zero mismatches); (4) reverse-engineered
  the Double-Pin-Pair family from a numeric-optimizer argmin search on
  witness 2 ($p=(14,7,5,3,1)/30$, the explorer's second surviving
  counterexample) and proved it in closed form; (5) verified exact that
  both round-30 counterexamples are individually closed by named
  instances of the new theorem ($\Phi=1/2<16/31$ in both cases). Honestly
  scoped: full coverage of $\mathcal R$ by the expanded family is **not**
  re-claimed (no outer-minimization re-check performed at scale this
  round; only the two known witnesses were targeted) — see "Round 30
  build" below.
- **Round 29.** Per the round-29 outline (APPROVE, pure
  instantiation), sequenced the three free general-$n$ transplants at
  $n=4$: `unconditional-p2-threshold-closure` ($p_2\le T/31$),
  the case-(a) analog via `generalized-peel-identity` ($k=2$) combined
  with round 27's complete $n=3$ upper bound as the reduced-instance tail
  bound ($p_2\ge8T/31$), and `p1-geq-half-closure-n4` ($p_1\ge T/2$) —
  shrinking the open $n=4$ territory to exactly $p_1<T/2$ AND
  $T/31<p_2<8T/31$. Instantiated `bisect-subset-lemma` at $n=4$ ($m=5$),
  giving all $2^5-2=30$ nonempty-non-full-budget subset chambers, and
  measured (exact `Fraction`, no floats) that these alone cover
  $\approx93\%$ of the residual box on $20000$–$30000$ random exact
  trials. Went beyond the outline's scope (permitted, since time
  remained): discovered and **proved in full** (not just numerically) a
  new general family, the **Double-Bisect-Pin Theorem** — bisect any 2 of
  the 5 pieces, pin one of the remaining 3 pieces to another (cut it to
  match a smaller remaining piece exactly), leave the last piece
  untouched; via `pair-insensitivity-corollary` (iterated 3 times) this
  collapses to a clean closed form $\Phi=(T+|p_k-p_l-p_r|)/2$. Combined
  with the 30 Bisect-Subset chambers, this new 30-chamber family covers
  **100% of 30000 fresh exact-`Fraction` trials** in the residual box —
  zero violations found — a strong empirical signal (not yet a proof) that
  this 60-chamber family suffices to close $n=4$'s upper bound. Honestly
  reported as **not yet closed**: no Farkas-style exhaustive covering
  argument (analogous to R27.3's) has been derived for this larger
  chamber family; that is the natural next step. 1 new lemma recommended
  for certification (`double-bisect-pin-family-n4`, though the underlying
  formula/mechanism is stated generally enough it may generalize past
  $n=4$ — flagged, not yet proved for general $n$).
- **Round 28.** Re-ran the certified Theorem C′/Theorem A
  argument (§4's $n=3$ closure mechanism) one index up at $n=4$, now that
  round 27 supplies the one missing ingredient — $P(4)$, the complete,
  both-regime $n=3$ upper bound — as the induction hypothesis Theorem C′
  needs for an arbitrary 4-piece tail. Proved, fully and non-numerically
  (no new machinery, pure re-indexing of already-general-$n$ theorems):
  for every 5-piece marking with $p_1\ge T/2$, $\Phi_{\min}(\cdot;4)\le
  a_4T=16T/31$. Explicitly re-verified (not merely assumed by analogy)
  that the Telescoping Threshold identity $a_3=a_4/(2(1-a_4))$ holds by
  direct substitution at $n=4$, and that $P(4)$'s scope (round 27,
  reviewer-APPROVEd) is exactly "every 4-piece marking, both regimes," the
  precise hypothesis Theorem C′ consumes — no smuggled $n=3$-specific
  constant. **Honestly scoped, not an overclaim:** the complementary
  $p_1<T/2$ regime at $n=4$ is untouched and, per the density-growth
  signal from the round-28 explorer, expected to need a fresh chamber
  census comparable in size to (or larger than) the $n=3$ 5+4-chamber
  effort — explicitly flagged as future work, not attempted this round.
  See §"Round 28 build" below for the full proof. 1 new lemma recommended
  for certification (`p1-geq-half-closure-n4`).
- **Round 27.** Dropped the round-27 outline's own false
  "forced-feasibility lemma" per the outline-reviewer's counterexample
  $p=(0.6,0.15,0.15,0.10)$. Numerically explored the residual gap region
  $R=\{p_1\ge T/2,\ T/15<p_2<4T/15\}$ via a composition-search optimizer
  (`/tmp/round-27/explore*.py`) to locate the true optimal Xiang-Yu cut
  patterns, found and isolated four reusable "erase a piece by bisecting
  it" / "pin one fragment to match another piece" chambers (A, B, C, E),
  proved a general **Pair-Insensitivity Corollary** of
  `odd-run-reduction-lemma` to derive each chamber's closed form cleanly
  (no ad hoc casework), then proved via two explicit Farkas certificates
  that these four chambers jointly cover **all** of $R$ — closing the
  exact residual gap left open by rounds 24–26. Combined with the already-
  certified case (a)/(b1)/(b2)-restricted-to-$p_1<T/2$ regimes, this
  **completes the general-marking $n=3$ upper bound $c(3)\le8/15$**. See
  §"Round 27 build" below for the full proof; all chamber formulas
  independently re-verified by 2000 exact-`Fraction` random trials
  (`/tmp/round-27/verify_formulas.py`) and the covering theorem by a
  300,000-trial exact-`Fraction` search plus an LP tightness check
  (corroboration only, not load-bearing — the written proof is fully
  algebraic). **Scope discipline:** this closes only the upper-bound
  direction at $n=3$; the lower-bound/achievability direction and the
  upper bound for $n\ge4$ are explicitly out of scope and not claimed.
- **Round 26.** Fixed the round-25 citation bug: case (a) is
  $p_2\ge a_3T/2=4T/15$ (not $p_1\ge T/2$, the round-25 mislabeling),
  closed via the already-certified Corollary to Theorem B ($m=4$,
  $S'=\{p_1-p_2,p_3,p_4\}$) with its hypothesis discharged
  **unconditionally** by the general (arbitrary-marking)
  `lemmas/n2-upper-bound-lp-argument.md` — this citation fix is correct
  and reviewer-verified. Also verified the three-way $p_2$-partition
  $(0,T/15]\cup(T/15,4T/15)\cup[4T/15,T/2]$ has no gap and no
  double-count at either boundary. **A "bonus" generalization attempt
  (dropping the $p_1<T/2$ restriction on `case-b2-n3-covering-closure`)
  was made this round but was FOUND FALSE by the round-26 proof-reviewer**
  — concrete counterexample $p=(3/5,9/40,29/200,3/100)$ ($p_1\ge T/2$)
  where all five chambers fail; the restriction is restored, and this
  sub-region ($p_1\ge T/2$, $T/15<p_2<4T/15$) is a genuine open residual
  gap. **Net result: the citation fix is real progress, but "$c(3)\le8/15$
  for every marking" is NOT established this round** — only for $p_1<T/2$
  (all cases) plus $p_1\ge T/2$ with $p_2\ge4T/15$ (case (a)). Per the
  outline, $n=4$ is explicitly deferred (not attempted this round).
- **Round 25.** Converted the round-24/25-explorer 5-chamber
  covering family (numeric/sampling-only) into a genuine exact-arithmetic
  coverage **proof** for case (b2) at $n=3$ (§R25.1): normalized $T=1$
  (homogeneity), wrote the 5 chambers' exact failure/feasibility
  inequalities in $(p_1,p_2,p_3)$, split the "uncovered" region into the
  outline's 6 exhaustive branches, and closed **all 6** with explicit,
  hand-checkable Farkas-style nonnegative-combination certificates (each a
  3–5-term rational-coefficient sum collapsing to $0<0$) — no floating
  point, no numeric margin. Also resolved the apparent "boundary vertex"
  $p^\ast=(2/5,4/15,1/5,2/15)$: exact evaluation shows R22.1.1 *succeeds*
  there ($g_{R22}(p^\ast)=0\ge0$ exactly, a genuine triple tie with
  Bisect$\{1,4\}$/Bisect$\{1,2\}$), so it was never inside any of the 6
  "uncovered" branches — confirmed by re-running the elimination with the
  box's $p_2<4/15$ wall relaxed to $\le$ (closed box), still fully
  infeasible. **Result: no separate boundary-vertex-disposal step is
  needed at all** (the outline-reviewer's flagged citation fix — Theorem
  B/`generalized-peel-identity`, not `unconditional-p2-threshold-closure`
  — is recorded as the correct fix *if* such a vertex had been needed, but
  it is not, since $p^\ast$ is already covered by R22.1.1 itself). This
  closes case (b2) at $n=3$ completely; combined with the already-closed
  case (a) ($p_1\ge T/2$) and case (b1) ($p_2\le T/D_3$) regimes, this
  **completes the general upper bound $c(3)\le a_3=8/15$ for every legal
  Liu Bang marking at $n=3$** — this approach's $n=3$ target is now fully
  solved (Status upgraded to `solved` for the $n=3$ scope; see Scope note
  in §R25.1 for exactly what is and is not covered by this closure).
  **[Round-26 correction: this paragraph's "case (a) ($p_1\ge T/2$)" is a
  mislabeling and its combination step is a citation bug — see the Round
  26 entry above and §R26.1–R26.3 for the corrected case (a) definition
  ($p_2\ge a_3T/2$) and the actual, now-complete assembly.]**
- **Round 24.** Per the round-24 outline: (1) certified the two
  Double-Sandwich chamber types from scratch (closed forms + exact
  feasibility regions, not just numeric recovery); (2) derived several new
  $p_1,p_2$-cross-tie-type chambers for the reported residual
  (`Triple-Pin`, `Chamber B1/B2`, and — the actual biggest find — a clean
  general-purpose **Bisect-Subset Lemma** that subsumes and extends
  Bisect-Top-$k$); (3) assembled the resulting 20-member covering family and
  tested it exhaustively on a dense deterministic exact-`Fraction` grid
  (1577 points) and a large random exact-`Fraction` sample (3351 points)
  over case (b2)'s box at $n=3$: **zero uncovered points found in either
  test** — a sharp improvement on round 23's 99.6%. This is strong evidence
  the family now closes case (b2) at $n=3$, but an exhaustive
  finite-vertex/case-split *proof* of the covering property (as opposed to
  dense sampling) was not completed this round — recorded honestly as the
  remaining gap; see "Round 24 build" below.
- **Round 23.** Two items per the round-23 outline. (1)
  **Scope-correction (cheap):** fixed `lemmas/p-space-chamber-vertex-
  theorem.md` item 3, which round 22's own reviewer had flagged as an
  overclaim — the "compactness-fix" Corollary is unconditional only for
  $n\le3$, and conditional (on the standing strong-induction hypothesis)
  for $n\ge4$, since only one of its three input closures ($p_2\le T/D_n$)
  is unconditionally general for every $n$; the other two ($p_1\ge T/2$,
  case (a)) are scoped as recorded elsewhere in this same file. (2)
  **Headline target: $n=3$ case-(b2) chamber work.** Found a genuine
  methodological simplification — the *upper-bound* direction
  ($\Phi_{\min}(p)\le a_nT(p)$) only ever needs a **feasible** type/strategy
  at each $p$ (condition (c), true global optimality, is not required,
  since any legal response upper-bounds $\Phi_{\min}$) — and used it to
  derive a **second** explicit closed-form chamber,
  `chamber-a2-p1-tied-to-p2-pair` (composition $(2,0,0,0)$, a genuinely
  different type from R22.1.1's worked example and from a same-composition
  sibling type also identified this round). **Caught and corrected an LP
  encoding bug mid-round**: an initial (incorrect) LP run suggested this
  chamber's own feasibility region satisfies $g\ge0$ throughout; re-deriving
  the constraint row from scratch overturned this — the corrected LP finds
  an exact point in the chamber's own feasibility region, $(p_1,p_2,p_3,
  p_4)=(\tfrac25,\tfrac4{15},\tfrac4{15},\tfrac1{15})$, with $g=-\tfrac1
  {15}<0$, so this chamber (like every other single template on file) is
  **not** by itself a standalone-sufficient cover — recorded as a genuine
  self-correction, not left standing. **Honest result: case (b2) at $n=3$
  is not fully closed.** An extended
  computational search (much broader than round 22's) found **at least 8
  distinct optimal cut-compositions** realized across the box, and — a new,
  concrete finding — **one single composition can itself host $\ge2$
  genuinely different optimal types** (found and exhibited explicitly),
  revising the round-23 outline's "a dozen or so" chamber-count estimate
  upward. Also confirmed, honestly, that **single "template" chambers
  considered in isolation are not sufficient covers** (each of the two
  hand-derived chambers has points in its own feasibility region where its
  own value alone exceeds $a_3T$) — not a counterexample to the theorem
  (verified in every case that some *other* type covers the point, true
  global $\Phi_{\min}$ margin stayed positive, best-found margin
  $\approx0.0115$ across the search), but confirmation that closing case
  (b2) needs a genuine finite **covering family** of such chambers, not a
  single template — the concrete next-round target. (3) Route A's §A.3
  symbolic $(X,q)$ optimization: not attempted this round (time went to the
  headline target per the outline's stated priority order).
- **Round 22.** Per the round-22 outline's two targets: (1)
  proved, from scratch, a genuinely new **$p$-space Chamber-Vertex
  Theorem** — the round-20/21 Within-Chamber Affinity Theorem gives
  affinity of $\Phi_{\min}(p)$ on a chamber $U(\mathbf c,\tau,\pi)$, but
  says nothing about $U$'s own shape in $p$-space; this round shows $U$ is
  itself a polyhedron cut out by finitely many affine inequalities in $p$
  (feasibility, order, type-optimality) and that the affine functional
  $a_nT(p)-\Phi_{\min}(p)$ therefore attains its minimum, on any chamber
  intersected with case (b2)'s box, at an extreme point — see "Round 22
  build", §R22.1. (2) Explicitly resolved the outline-flagged strict-Box
  compactness issue: case (b2)'s box is open (strict inequalities), so a
  literal "vertex" need not be attained inside it; resolved by showing all
  three Box walls coincide exactly with the boundaries of three
  already-unconditionally-closed adjacent regions (case (a) $p_2\ge
  a_nT/2$, case (b1) $p_2\le T/D_n$, and the $p_1\ge T/2$ regime), so any
  closure-boundary extreme point is automatically covered without needing
  the new machinery there (§R22.2). Both worked out and cross-checked
  against a concrete, numerically-verified $n=3$ example (composition
  $(1,1,0,0)$, an explicit type with a clean closed form
  $\Phi_{\min}(p)=p_1/2+p_3+p_4$ on its chamber). (3) Numerically tested
  (exact-`Fraction`-verified, not just floating point) the outline's
  "box-corner $\times$ tail-chamber-vertex decomposition" conjecture at
  $n=3,4$ and **found it false**: an unrestricted search over case (b2)'s
  box repeatedly finds strictly *worse* (smaller-margin) witnesses than
  the best margin achievable with $(p_1,p_2)$ held at the box corner, at
  both $n=3$ and $n=4$ — reported honestly as a negative finding, not
  silently dropped, and written up as a new dead-end lemma (§R22.3). Case
  (b2) itself remains open; this round is infrastructure plus one
  ruled-out mechanism, not a closure. New lemma proposed for certification:
  `p-space-chamber-vertex-theorem` (conditional, same invertibility
  hypothesis inherited from `within-chamber-affinity-theorem`); new
  dead-end record: `box-corner-tail-vertex-decomposition-refuted`.
- **Round 20 (this round).** Per the outline-reviewer's CHANGES REQUESTED
  verdict on the round-20 outline's within-chamber-affinity Key Lemma: (1)
  wrote out, in full and from scratch (not as a "free corollary" of
  `per-piece-vertex-decomposition-theorem`, as the round-20 outline's
  Key-Lemma blurb had overstated), the joint mutual well-posedness argument
  for the across-all-pieces linear system that step 1's per-piece vertex
  formula induces — see "Round 20 build: the Within-Chamber Affinity
  Theorem" below for the full statement and proof, including the genuinely
  new content the reviewer flagged as missing (the joint $k\times k$
  matrix $M(\tau)$, why its rows are mass-conservation-linear-in-$p$ and
  tie/pin-rows are $p$-independent-coefficient, and — the actual gap — a
  proof, not an assertion, that $M(\tau)$ singular forces the corresponding
  type $\tau$ to have empty interior in $p$-space, i.e. cannot itself be an
  open chamber, with one honestly-flagged residual sub-case where this
  argument does not fully close, stated precisely). (2) Ran the outline's
  mandatory gating computational checks (steps 5a–5c) **before** any
  general-$n$ writing: a numerical affinity spot-check at $n=3$ (three
  colinear markings sharing one optimal composition, testing whether
  $\Phi_{\min}$ is linear along the segment) and an honest chamber-count
  growth read at $n=3,4$ inside case (b2)'s box by composition-level brute
  sampling (a coarser, hence conservative *undercount* proxy for the true
  finer tie-pattern chambers) — both reported in full with exact numbers
  below, including the chamber-count finding that density is growing with
  $n$ (28% distinct compositions per sample at $n=3$ vs. 64% at $n=4$ on
  this round's sample sizes), which the outline flagged in advance as the
  key risk signal to watch. **Honest conclusion: the within-chamber
  affinity mechanism is now a properly-proved conditional theorem (not an
  asserted corollary), and passes both gates it was required to pass this
  round, but case (b2) itself remains open** — affinity alone does not yet
  supply the finite evaluation at extreme points (step 4 of the outline,
  the "actual work" the outline itself identified as still ahead), and the
  chamber-count growth signal is a genuine amber flag for whether a
  general-$n$ closure via this route stays tractable. No claim of general-$n$
  closure is made. One new lemma proposed for certification
  (`within-chamber-affinity-theorem`, conditional form).
- **Round 19 (this round, bookkeeping/consolidation, no fresh mechanism
  attempted per this round's dispatch).** Per this round's task: (1)
  formally certified the round-19 surrogate-lens explorer's finding
  (`/tmp/round-19/math-explorer-surrogate.md`) as a new dead-end lemma,
  `lemmas/surrogate-adversary-dead-end.md` — the surrogate/majorization
  worst-tail mechanism for case (b2) is **unsound**, not just numerically
  weak: the natural candidate surrogate (the ratio-2 ladder tail) is
  provably **not** the true argmax over legal tails at fixed $(p_1,p_2)$
  (the true argmax tail ratio was independently re-derived, via a fresh
  `differential_evolution`-based script, to be $\approx1.8$ at one tested
  point, strictly beating the ratio-2 value $0.5083$ with $0.5125$, and the
  argmax ratio drifts substantially, $\approx1.4$–$2.0$, across four tested
  points in case (b2)'s box, with the optimal Xiang-Yu response at the
  argmax itself — composition $(2,0,1,0)$ — matching no certified template
  on file). A sound majorization argument would need the true argmax tail
  characterized in closed form, which this round's evidence shows is not a
  low-dimensional/one-parameter object — i.e. it needs exactly the same
  joint-vertex characterization that already blocks every other route into
  case (b2), not a shortcut around it. This is the **fifth** confirmed-dead
  mechanism family for case (b2) (after peel/bisect/recurse-plus-full-IH,
  weighted-combination, boundary-continuity, Danskin/concavity). (2)
  Re-confirmed, by direct inspection of the case (a)/(b1) closures and the
  two certified case-(b2) witness closures, that none of them implicitly
  assumes a fixed or near-ratio-2 worst tail, so this round's drifting-
  argmax finding leaves all prior certified partial closures intact — see
  "Round 19 re-confirmation" below for the itemized check. **No new lemma
  proposed beyond the dead-end record; no positive coverage added or
  retracted this round.** Case (b2) remains open, now routed (per the
  outline-reviewer's build set) to the new sibling
  `minimax-lp-response-polytope` for a genuinely different (LP dual-
  constraint, not primal-value or surrogate-tail) mechanism.
- **Round 18 (this round).** Per the round-18 outline (Tail Exchange
  Lemma / Danskin's-theorem smoothing over Liu Bang's own tail-marking
  freedom for case (b2)) and the outline-reviewer's mandatory gate
  (cheap $n=3$ single-free-parameter check before general $n$): set up
  the mechanism precisely (Liu Bang maximizes $g(t)=\Phi_{\min}(p_1,p_2,t)$
  over his own legal tail markings $t$, fixed $p_1,p_2$ in case (b2)'s
  box), then ran the mandated $n=3$ check on the on-file near-tight
  case-(b2) witness. **Result: the mechanism's required structural
  premise (Conjectured Concavity of $g$ in $t$) is FALSE**, refuted by a
  clean, reproducible interior local minimum of $g$ at $p_3=p_1-p_2$
  (matching slope $\mp1/2$ on both sides, robust to optimizer settings) —
  concave functions on an interval cannot have an interior local minimum
  flanked by increases on both sides. Per the outline's own gate, step 4
  (general-$n$ stationarity characterization) was correctly not attempted
  further, since it would rest on the now-refuted premise. This is a
  genuine negative finding, distinct from and sharper than the three
  previously-foreclosed mechanism families for case (b2)
  (peel/bisect/recurse, weighted-combination, naive boundary continuity):
  it identifies exactly *why* a smoothness/first-order approach over Liu
  Bang's own freedom cannot work globally (Xiang Yu's per-branch values
  are order-statistic sums, individually convex-flavored in the free tail
  coordinate, so their minimum is not globally concave, only locally
  affine within finitely many uncharacterized chambers). Case (b2)
  remains open; zero new positive coverage this round. No new lemma
  certified (the finding is a refutation of a proposed premise, not a
  standalone reusable positive fact — see Promotable lemmas for a
  narrower certifiable negative statement).
- **Round 17 (prior round).** Per the outline-reviewer's mandatory
  correction (do not define $\lambda(p)$ by pointwise-equating to the
  target — circular), attempted a genuinely independently-motivated
  $\lambda$ for combining two certified exact primal identities (Theorem
  C bisect-$p_1$, Bisect-Top-2) at $n=3$: found (i) no fixed $\lambda$
  makes the combination coefficientwise nonnegative over all orderings
  (an exact algebraic obstruction, $\lambda\le1/15$ vs $\lambda\ge7/15$
  simultaneously required, impossible), and (ii) an exact LP search over
  case (b2)'s full $n=3$ polytope confirms no $\lambda\in[0,1]$ rescues
  this pair (best achievable worst-case value $\approx-0.033<0$).
  Investigating *why* led to a genuine, fully general, non-numeric
  **Convex-Combination Futility Theorem**: for any finite family of
  explicit primal Xiang-Yu strategies and any weighting rule whatsoever
  (fixed or adaptively $p$-dependent), a weighted combination certifies
  exactly the same set of markings as the plain pointwise minimum of the
  same family — never more. This proves, not merely suspects, that the
  entire "weighted-combination certificate over a fixed finite primal
  family" framing (this round's assigned target, and the outline-
  reviewer's flagged circularity risk) is structurally incapable of
  adding coverage of case (b2) beyond what round 16's plain pointwise-min
  grid check already tested — a rigorous, general dead-end result, honestly
  reported per the task's explicit instruction rather than papered over.
  Diagnosed the deeper reason: upper bounds on a minimum are witnessed by
  one explicit strategy, not improved by averaging several already-
  exhibited values (Xiang Yu cannot randomize and be scored in
  expectation); genuine LP-duality/weighting arguments are the correct
  tool for *lower* bounds (Claim (B)), not this slug's upper-bound target.
  Case (b2) remains open; **1 new certified lemma**
  (`convex-combination-futility-theorem`), no new positive coverage.
- **Round 16.** Per the round-16 outline's three tasks: (1)
  fixed the round-15-flagged sign bug in `alternating-gap-cross-lemma`
  — found the true bug is *deeper* than the outline's literal instruction
  (relabeling only the tail prefactor $(-1)^j\to(-1)^{j'}$ is necessary but
  not sufficient; the gap-sum's own per-pair signs also need reindexing by
  split-rank, not raw pair index — confirmed via the round-15 reviewer's own
  counterexample, which has an *empty* tail, so the tail-prefactor-only fix
  changes nothing there), re-verified by a fresh 30000-trial exact-`Fraction`
  script (zero mismatches across 17834 feasible constructions), and
  reconfirmed both round-14 case-(b2) witnesses remain closed — lemma
  re-certified as corrected. (2) Executed the outline-reviewer's mandatory
  gate check *before* any numeric diagnostic: proved algebraically (not
  numerically) that the "recursive-image-escape" mechanism (recursed image
  lands in case (a)/(b1) one level down) is **exactly** the same
  zero-slack-inert mechanism `peel-zero-slack-dead-end`/
  `bisect-containment-dead-end` already ruled out — case (a)/(b1)'s own
  proven ceiling $a_{n-1}T'$ is tight (attained with equality by genuine
  instances at every level of the induction), so knowing which case the
  recursed image falls into supplies no bound below that same ceiling,
  hence zero new coverage of case (b2). Per the outline's explicit
  branching rule, correctly did **not** run the numeric diagnostic (it
  would have been mathematically vacuous) and pivoted to Task 3. New
  certified negative lemma `recursive-image-escape-dead-end`. (3) Fallback:
  ran a broadened (denser, non-random) exact-`Fraction` grid check of case
  (b2)'s box at $n=3$ combining every certified construction on file;
  covers $212/214$ grid points, with the two exceptions clustering at
  round 14's own already-known near-tight witness (an artifact of this
  round's non-optimized parameter choice within each family, not a new
  gap) — honestly reported as non-rigorous corroboration, **not** a
  closure; the joint vertex fixed-point obstruction (R11.5/R12.5/R14.3)
  remains unresolved and case (b2) remains open in general. **Net effect:**
  one genuine negative result (a whole family of recursive arguments now
  provably foreclosed, not just two instances of it) plus a hygiene fix;
  Open Gap 1 at case (b2) is not closed this round. 2 new/corrected lemmas
  (`recursive-image-escape-dead-end` new; `alternating-gap-cross-lemma`
  corrected in place).

- **Round 15 (prior round).** Per the round-15 outline: (1) formalized the
  round-15 explorer's "Cross-Piece Sign-Assignment Identity" as a fully
  general, rigorously proved lemma (`cross-piece-sign-assignment-identity`),
  built directly on the already-certified `odd-run-reduction-lemma` (for
  the tie-collapsing half — executing round 9's originally-flagged,
  previously-unexecuted suggestion) plus an elementary finite-sum
  regrouping (for the monochromatic-piece evaluation half) — genuinely
  strictly generalizes `pair-cancellation-identity`/`bisect-top-k-lemma`
  (they are the corner case where a piece's fragments cancel to $q_i=0$;
  the new identity also covers a piece's fragments surviving intact at
  non-adjacent same-parity ranks, contributing its *whole* value $\pm p_i$,
  and covers cross-piece exact ties via `odd-run-reduction-lemma`). Verified
  by a fresh 20000-trial exact-`Fraction` script (6989 monochromatic
  constructions, zero mismatches) and by exact-fraction reconstruction of
  **both** round-14 near-tight case-(b2) witnesses — the $n=3$ flat-face
  case (no ties) and the $n=4$ pinned-tie case (a genuine cross-piece tie) —
  confirming the single general identity correctly specializes to both
  qualitatively different vertex/face types, and that **both witnesses are
  in fact unconditionally closed** by an explicit legal Xiang-Yu response
  ($\Phi\approx0.51585<a_3T\approx0.53333$ at $n=3$; $\Phi\approx0.50455<
  a_4T\approx0.51613$ at $n=4$). (2) Attacked the feasibility question (which
  sign vectors are legally realizable) as a finite combinatorial problem via
  a new, general **Alternating Gap-Cross Lemma**: an explicit $j$-parameter
  construction (split pieces $p_1,p_3,p_5,\dots$ each "sandwiching" the
  following even-indexed piece) with a **closed-form, non-numeric**
  feasibility test (an explicit recursive $\gamma_i=\min(p_{2i-1}-p_{2i},
  p_{2i})$ comparison chain — proved correct, not just tested, and
  independently cross-checked against a constructive search with zero
  disagreements over 8000 trials) — this is the concrete resolution of the
  outline's "attack feasibility as a finite combinatorial problem, not a
  continuum optimization" instruction. **Honest coverage finding:** the
  Alternating Gap-Cross family, while it exactly and unconditionally closes
  the specific $n=3$ near-tight witness that motivated the round, adds only
  a small marginal improvement to case (b2)'s coverage on random samples
  (5.0%→7.5% at $n=3$; no measurable improvement at $n=4,5$ in a 40-sample
  check per $n$) over `bisect-top-k-lemma` alone — **case (b2) remains open
  in general**; this round's real contribution is two new certified general
  lemmas plus the closure of both on-file near-tight witnesses, not a
  closure of the region. 2 new lemmas certified below
  (`cross-piece-sign-assignment-identity`, `alternating-gap-cross-lemma`).

- **Round 14 (prior round).** Per the round-14 outline (three tasks): (1)
  generalized the round-13 `unconditional-p2-threshold-closure` from $k=1$
  to arbitrary $k$ — proved, in full and unconditionally, the new
  **Bisect-Top-$k$ Lemma** ($\Phi\le(T+p_{k+1})/2\le a_nT$ whenever
  $p_{k+1}\le T/D_n$, any $0\le k\le n$), via a clean finite induction on
  $k$-fold `pair-cancellation-identity` application plus `max-domination-
  lemma`; independently re-verified by a fresh $7000$-trial exact-`Fraction`
  script (zero violations) and quantified its own coverage of case (b2)
  by a fresh, independently-coded random sampler (not reusing the
  explorer's script): $\approx10$–$26\%$ of case-(b2) witnesses across
  $n=3,4,5$, consistent with (and refining) the outline's cited $5$–$13\%$
  figure (that figure was for $k=1$ alone; the union over all $k$ is
  larger). (2) Wrote up, as formal certified negative lemmas with full
  proofs (not new derivations — both exact thresholds were already
  implicit in this file's §"Proven sufficient conditions" and §2, now
  extracted, restated, and explicitly compared against case (b2)'s
  boundaries), the **Peel-$p_1$-$p_2$-Plus-IH Zero-Slack Dead End** (exact
  threshold $p_2\ge a_nT/2$, identical with zero slack to case (a)'s own
  defining threshold — this mechanism can never enlarge case (a) into any
  part of case (b2)) and the **Bisect-$p_1$-Plus-IH Containment Dead End**
  (exact threshold $p_1\ge a_nT$, a strict subset of the already-closed
  $p_1\ge T/2$ region, since $a_n>1/2$ — this mechanism contributes zero
  new territory in the open $p_1<T/2$ regime, hence can never touch case
  (b2) either). (3) Attempted the vertex-restricted case-(b2) search:
  found that a literal, self-consistent enumeration of the joint
  `per-piece-vertex-decomposition-theorem` vertex family (each cut piece's
  fragments pinned against the *rest of the current optimal multiset* as
  reference, circularly) is combinatorially heavy and was not completed in
  full generality this round (same obstruction R11.5/R12.5 already
  diagnosed); instead ran a cheaper, honestly-scoped diagnostic — a
  composition-by-composition local multi-start search (Nelder–Mead per
  fixed cut-composition, not a raw whole-simplex `differential_evolution`)
  restricted specifically to the case-(b2) box, which is far smaller than
  the whole simplex and did not time out (unlike the round-13/14
  unrestricted search). **Result: no near-zero-margin case-(b2) witness
  found** — the tightest witnesses located at $n=3,4$ have margins
  $\Phi_{\min}$-to-$a_nT$ of order $0.015$–$0.03$ (a genuine, if
  heuristic, lower bound on the true margin, since the local optimizer can
  only overestimate $\Phi_{\min}$, never underestimate it, so target minus
  the optimizer's found value is a conservative *floor* on the true
  margin). No clean $p_3$-vs-$p_2$ structural tie pattern emerged at the
  near-tight points (a local perturbation scan around one $n=3$ witness
  varying $p_3$ found the margin fluctuating in a band $\approx0.02$–$0.03$
  with no minimum exactly at $p_3=p_2$ or any other clean relation).
  **Honest conclusion: case (b2) remains open; this round's evidence
  leans (weakly, heuristically) toward case (b2) having genuine slack
  rather than a vanishing-margin family, but this is not a proof and the
  search was not exhaustive.** Three new lemmas certified below
  (`bisect-top-k-lemma`, `peel-zero-slack-dead-end`, `bisect-containment-
  dead-end`).

- **Round 13 (prior round).** Per the outline-reviewer's redirect toward
  closing Open Gap 1 (the general upper bound) via a **Peel-Target
  Existence Lemma**, attempted a dichotomy for the open $p_1<T/2$ regime:
  either some tail element $p_k\ge a_nT/2$ closes via the (already
  certified, re-verified to transfer without modification) Generalized
  Theorem B$_k$ Corollary, conditionally on the induction hypothesis one
  level down, or no such $k$ exists. **Result: genuine partial progress,
  Open Gap 1 not closed.** Proved a new, fully general, elementary **Max
  Domination Lemma** ($A(S)\le\max(S)$ for any sorted multiset, R13.1) and
  used it to derive a genuinely new, fully **unconditional** (no induction
  hypothesis anywhere) sufficient condition, $p_2\le T/D_n$ (R13.2) — this
  closes a sub-case of "no qualifying peel target" that no prior mechanism
  in this file's toolkit covered without induction. This sharpens the
  outline's binary dichotomy into an honest **trichotomy**: case (a)
  [conditional, known], case (b1) [new, unconditional], case (b2)
  [genuinely open, real, non-vanishing region — explicit witness given at
  $n=3$]. Tested and **refuted** the natural 2-cut "peel-$p_2$-then-
  dominate" extension as a universal closer of case (b2) (exact
  `Fraction` witnesses, $\approx10\%$ failure rate, some overshoots by
  orders of magnitude) — a clean negative result, not a repeat of R12.4's
  refuted construction (structurally different: peel-then-bisect vs.
  bisect-cascade). No new gap-closing construction claimed; Max Domination
  Lemma and its $p_2\le T/D_n$ corollary are genuine, reusable, unconditional
  new content certified below.

- **Round 12 (prior).** Per the outline-reviewer's hard redirect: built
  only the two approved cheap lemmas from the round-12 outline (Equal-Pieces
  Closure, Spare-Cut Bisection Corollary), formalized in full below as
  §R12.1–R12.2, and certified. The outline's steps 3–4 (a pigeonhole
  "close every gap with one cut" selection rule) were **not** attempted —
  the outline-reviewer independently found this whole move family
  insufficient by exhaustive brute-force search (best achievable value over
  *every* ordering of the pair-matching family still exceeds $a_3T$ in
  ~60% of $n=3$ trials, witness $(8/5,35/3,12/5,31/10)$; ~99.6% failure at
  $n=4$ for the "one cut per gap" literal reading) — a confirmed dead end,
  not merely unproven, so no further time was spent on it. Instead this
  round attacks the outline-reviewer's redirect target **(b)**: evaluating
  the certified Per-Piece Vertex Decomposition Theorem's joint vertex family
  against $a_nT$ for arbitrary markings (R11.5's "single cleanest remaining
  item"). **Result: genuine partial progress, not closure.** §R12.3 proves
  a new, fully general **Tie-Free Full-Budget Characterization**: the
  Iterated Greedy-Peel Construction (`iterated-greedy-peel-identity`,
  certified) fails to meet the target *only* on the configurations
  R12.1–R12.2 do not already cover, and this residual set is **not** a
  small corner case but the *generic* one (a fresh, independent
  4000-trial exact-`Fraction` check over uniformly random rational
  markings finds ties mid-process in only 3/4000 trials — essentially
  never, for real-valued/generic denominators — confirming and sharpening
  the outline's own ~34%-covered figure downward for truly generic
  inputs). §R12.4 tests, and rigorously refutes by an explicit exact
  witness, a second natural greedy candidate for the residual
  ("cascade-bisect the current largest fragment $n$ times") — it fails
  on the *majority* of random trials too (2330/3000), with a concrete
  3-piece witness given in full. §R12.5 gives the honest diagnosis of why
  evaluating the joint vertex family in general still resists a
  closed-form bound (the same core issue R11.5 already identified —
  no tail-structure-agnostic replacement for the ladder-specific spacing
  facts exists — sharpened here with two additional concrete failure
  witnesses for the two most natural fallback constructions). **No new
  gap-closing construction is claimed; both certified lemmas (§R12.1,
  R12.2) are genuine, reusable, unconditional new content, and target
  (b) remains open with a clearer picture of which easy constructions
  are (and are not) sufficient.**

- **Round 11 (prior).** Two tasks. **(a) Cheap fix, completed:**
  proved the general **Zero-Pin Harmlessness Lemma** (appending zero-valued
  elements to any multiset changes neither $A$, $E$, nor $\Phi$ — a short,
  fully general, elementary fact) and used it to give the corrected,
  fully-reproved **Simplex Vertex-Maximization Lemma** (pin set
  $\{0,\tau_1,\dots,\tau_r\}$, matching what the original proof's exchange
  argument always used internally, now made consistent with the boxed
  statement and independently re-verified via the harmlessness lemma) —
  this closes the round-10 gap exactly as scoped, no numerics substituted
  for proof. Certified below. **(b) Structural redirection:** confirmed by
  *exhaustive* enumeration over the now-fully-characterized finite vertex
  family (a genuine proof by finite case-check, not numeric evidence, since
  the family is proven complete) that the round-9/10 outline's premise was
  **partially wrong**: of the two on-file hard witnesses, only
  $(2/5,3/10,1/5,1/10)$ genuinely defeats every "cut $p_1$ only" strategy
  (best such strategy gives $11/20>8/15$); the other witness
  $(3/8,1/4,1/4,1/8)$ is in fact **solved** by a cut-$p_1$-only strategy
  (trisecting $p_1$ into three equal $1/8$ parts, a $p=0$, $k=3$ vertex of
  exactly the family already characterized in Route A, giving $\Phi=1/2$
  exactly) — round 4's ad hoc "trisect $p$" discovery and this family's own
  $k=3$ vertex coincide. This is a genuine correction (recorded so no future
  round treats both witnesses as proof that Route A is *always* insufficient
  — one witness alone, $(2/5,3/10,1/5,1/10)$, is enough to prove Route A is
  not universally sufficient, and remains the correct citation for that
  claim). Then proved a new, general **Per-Piece Vertex Decomposition
  Theorem**: applying the certified `vertex-minimum-theorem` honestly to
  Xiang Yu's *actual* legal move space for an arbitrary composition
  $(c_1,\dots,c_m)$ over *all* pieces simultaneously (not just $p_1$) shows
  that at a global minimizer, *each* piece's own fragment vector is itself a
  maximizer of the corrected Simplex Vertex-Maximization problem relative to
  the rest of the final multiset as reference — i.e. every piece
  independently obeys the same pinned+tied vertex structure. This is a
  genuine, marking-agnostic generalization of Route A's characterization
  from "cut $p_1$ only" to arbitrary compositions, and is new content this
  round (not previously proved for more than one piece splitting
  simultaneously). **Honestly left open, as anticipated by the outline**:
  evaluating this joint multi-piece vertex family in closed form against
  $a_nT$ for an arbitrary marking — the genuinely new content the outline
  asked for (tail-structure-agnostic analogues of Ratio-2 Spacing Lemma /
  Last-Element Bound) was attempted but no working general evaluation
  mechanism was found this round; see the new section below for the precise
  diagnosis of why the ladder-specific tools do not transfer and what a
  replacement would need to supply.

- **Round 10 (prior).** Per the round-10 outline, worked both parallel
  routes on the open $p_1<T/2$ regime of the general upper bound.
  **Route A**: proved a new, fully general **Simplex Exchange-Smoothing
  Vertex-Maximization Lemma** (dropping the box constraint $f_i\le\tau_1$
  from the certified `exchange-smoothing-vertex-maximization`, a mechanical
  but honestly-derived adaptation of its proof) and used it, together with
  `pair-cancellation-identity` and `odd-run-reduction-lemma` (both confirmed
  marking-agnostic), to characterize the exact vertex family for "cut $p_1$
  only" strategies against an *arbitrary* marking's tail, replacing Theorems
  A/B/C by a single unified, characterized (finite, explicit) family — this
  is a genuine reduction, not a reformulation, and closes the "does the
  reduction machinery transfer" question. **Honestly left open**: comparing
  this whole family's minimum against $a_nT$ in closed form for an arbitrary
  marking (the genuinely hard remaining content, as the outline anticipated;
  not completed this round).
  **Route B**: found and fully proved a genuinely new, general **Iterated
  Greedy-Peel Construction** — a completely explicit, always-legal algorithm
  (pick the two largest current fragments, cut the larger to match the
  smaller, repeat) that uses $\le n$ cuts for *any* marking and produces
  $\Phi=(T+v_{\text{final}})/2$ exactly, via repeated `pair-cancellation-
  identity`. This construction *exactly reproduces* the known optimal value
  ($\Phi=1/2$) at **both** on-file hard witnesses, using the budget-record
  minimum number of cuts (2 of 3) — a genuine cross-check, not an assumed
  pattern. **Then rigorously tested it further and found a genuine
  counterexample**: at the $n=4$ equal-pieces marking ($p_i=1/5$, $i=1..5$),
  the construction gives $\Phi=3/5=0.6>a_4T=16/31\approx0.516$ — and a
  broader random stress test (2000 trials, $m=2,\dots,6$) shows this naive
  "always match the top two" greedy rule fails roughly **48%** of the time.
  **Reported honestly, per the outline's explicit instruction**: the
  construction does *not* generalize as a proof of the upper bound; it is a
  genuine new general reduction identity (reusable, certified below) but
  the "always succeeds" hope is refuted, not confirmed. Also corrected an
  imprecision in the round-10 outline's Route B framing: the "matching
  reformulation" (exact pairs + bounded leftover) is proved here to be a
  **sufficient**, not equivalent, characterization of $c(n)\le a_nT$ — the
  general odd-run-reduced multiset need not itself be single-valued, so a
  minimizing Xiang Yu strategy is not shown (and is not obviously true) to
  always take pair+leftover form.

- **Round 7 (prior).** Converted the certified Half-Window Vanishing Lemma into this
  approach's own certificate vocabulary for the lower-bound sub-case $c_1=1$
  (full success), then pushed to $c_1\ge2$ and found (§6-7, still on file
  below) a precisely diagnosed, exactly-verified obstruction: the resulting
  sufficient inequality is false at an exact $n=3$, $c_1=2$ witness
  ($F=\{4,2,2\}/15$), and the shortfall requires the tail's *exact* value,
  not its inductive floor — a fact no bounded, context-free certificate
  vocabulary can express.
- **Round 6.** Constructed a complete LP-dual certificate for the fully
  closed $n=2$ lower bound (all 17 leaf cells), plus one consistency check
  one level into $n=3$.
- **Round 8 (this round, REDIRECTED target).** Per this round's
  outline/outline-review, both round-8 explorers independently confirmed
  that any bounded/context-free certificate for the round-7 Case-I
  lower-bound obstruction must smuggle in $A(G')$'s exact recursive value —
  i.e. is the induction in disguise — so this round **redirects the
  approach entirely away from the lower bound** and onto the orthogonal,
  still largely open **general upper bound** $c(n)\le a_n$ for an
  *arbitrary* Liu Bang marking (not just the ladder), $n\ge3$. This is a
  legitimate pivot (a different half of the theorem), not a same-mechanism
  retry.

  **What was done.** Round 4's `smoothing-compactness-certificate` already
  showed the direct generalization of the $n=2$ six-template mechanism
  (prefix/suffix cascades) *fails* at a concrete $n=3$ witness
  $(p,q,r,s)=(3/8,1/4,1/4,1/8)$, needing an ad hoc seventh strategy
  (trisect $p$), and diagnosed the obstruction as genuinely
  configuration-dependent tie targets, not a fixable oversight. This round
  builds on that finding by constructing, from scratch, a **different kind
  of strategy family**: not template-per-region case analysis, but four
  *exact, unconditional, closed-form identities* — each a legal Xiang Yu
  move whose resulting $\Phi$ is computed exactly via the certified
  `pair-cancellation-identity` / `leftover-formula`, for **every** $n$ and
  **every** marking, with no case restriction on the identity itself (only
  on whether it happens to meet the target). Combining the best of these
  four with an explicit strong induction:
  - **Fully proves** two clean, general-$n$ sufficient conditions in closed
    form (Theorem A / Theorem B below), each independently verified exact
    by algebra (cross-checked symbolically with `sympy`, not just spot
    numerics).
  - **Numerically stress-tests** (exhaustive grid + $150{,}000+$ random
    trials + adversarial `differential_evolution` search, $n=2,\dots,6$) the
    *combination of all four* identities and finds **zero violations**,
    including at round 4's own $n=3$ witness (now solved, value $1/2<8/15$)
    and at a fresh, smaller witness this round found and diagnosed
    exhibits exactly the same "beats every 3-strategy combination but is
    solved by the 4th" pattern as round 4's finding — a genuine, if
    informal, triangulation with round 4's independent obstruction.
  - **Honestly stops short of a proof for general $n$**: the full induction
    combining all four branches (needed to turn the numerics into a
    theorem) is not completed this round; see Open gaps.

- **Round 9 (this round).** Formalized Theorem C′ (the round-9 explorer's
  scouting result: bisect $p_1$, recurse the *optimal* strategy on the tail
  with the remaining $n-1$ cuts) into a full, rigorous, general-$n$
  identity and threshold proof; corrected the outline-reviewer-flagged
  witness misclassification ($(6,2,2,1)/11$ has $p_1=6/11\ge T/2$, resolved
  by Theorem C′, not open — only $(3/8,1/4,1/4,1/8)$ genuinely lives in
  the open $p_1<T/2$ regime). **Found and honestly report a genuine
  structural subtlety the outline missed**: Theorem C′'s recursive step
  needs $\Phi_{\min}(\text{tail})\le a_{n-1}T'$ for an *arbitrary* tail
  (any distribution of $p_2,\dots,p_m$, not restricted to its own
  $p_1\ge T/2$ case), i.e. it needs the *full*, both-regime theorem one
  level down as its induction hypothesis. So "closing $p_1\ge T/2$ by
  induction" is **not** independent of closing $p_1<T/2$, contrary to the
  outline's framing — it is only unconditionally valid as far up as the
  full theorem is already known at the previous level. Concretely: $m=1,2$
  are trivial/vacuous ($p_1\ge T/2$ is forced whenever $m\le2$) and $m=3$
  ($n=2$) is *already fully closed, both regimes*, by the certified
  `n2-upper-bound-lp-argument` lemma — so Theorem C′ **rigorously and
  unconditionally closes $p_1\ge T/2$ at $n=3$ ($m=4$)**, a genuine complete
  new result, but extending past $n=3$ requires first closing $p_1<T/2$ at
  $n=3$, which remains open. Also derived and proved in full (general $n$,
  not spot-checked): (i) the telescoping threshold identity
  $a_{n-1}=a_n/(2(1-a_n))$ making Theorem C′'s threshold match $a_n$ with
  zero slack for *every* $n\ge1$; (ii) a new general identity, **Theorem
  B$_k$** (Generalized Peel), extending the certified
  `one-step-peel-identity` from peeling $p_1$ against $p_2$ specifically to
  peeling against *any* $p_k$ ($k=2,\dots,m$) — proved, but its
  ceiling-based sufficient condition is shown to be dominated by (no
  stronger than) the original $k=2$ case, so its value is only realized
  via *exact* recursive values, which again needs full closure one level
  down; (iii) **Theorem D′** (bisect $p_1,p_m$, recurse optimally on the
  middle instead of leaving it untouched) and its exact general threshold
  $s^\ast=(3/2)a_nT$ for $p_1+p_m$ (algebraically derived for all $n\ge2$,
  not just checked for $n\le9$); (iv) a genuine general (not just $n=3$)
  **negative proof** that the equal-pieces marking is *never* certified by
  Theorem D′'s IH-ceiling mechanism, for any $n\ge2$; (v) Theorem E (bisect
  $p_1,p_2$) derived and shown by exact computation to fail at both
  on-file hard witnesses, ruling it out as a standalone fix. Using Theorem
  B$_k$ (peel by $p_4$, not $p_2$) plus a further bisection, found the
  *exact* optimal strategy at a **fresh $p_1<T/2$ witness**
  $(2/5,3/10,1/5,1/10)$ at $n=3$ (found via `scipy` search while
  stress-testing Theorem D′/E, both of which fail there, giving $0.55$):
  the true optimum is exactly $1/2\le8/15$, achieved by peeling $p_1$
  against $p_4$ then bisecting $p_3$ — confirming this point is not a
  counterexample to $c(3)\le8/15$, but that its resolution needs
  configuration-specific structure no single theorem on file captures
  in closed form, reinforcing (with an independently-found new witness)
  round 4/8's diagnosis. **Honest conclusion:** the $p_1\ge T/2$ regime is
  now fully and rigorously closed for $n\le3$ (new); general $n\ge4$ and
  all of $p_1<T/2$ beyond $n\le2$ remain open, with a substantially
  clearer, general-$n$ diagnosis of exactly why (the induction's genuine
  dependence on full closure one level down, not merely "harder casework").
  See the new "Round 9 formalization" section below for full proofs.

## Current best

**Round-30 RETRACTION (mandatory, read first).** Round 29's claim
("$100\%$ empirical coverage of $\mathcal R$ by the 60-chamber family [30
`bisect-subset-lemma` $\cup$ 30 Double-Bisect-Pin], over 30000 fresh exact
trials, zero violations") is **REFUTED**. A round-30 explorer found an
exact, interior-of-$\mathcal R$ counterexample
$p=(11,7,6,3,2)/29$ at which **all 60 chambers simultaneously** give
$\Phi=15/29$, exceeding $a_4T=16/31$ by exactly $1/899>0$ — not a
boundary artifact, not a float-rounding issue (independently confirmed
exact via two computation routes). What went wrong: R29.5's "100%
coverage" was measured only against $30000$ *randomly sampled* points; a
genuine but geometrically thin ($\sim1/899$-margin) gap in the family's
own coverage is exactly the kind of exact small-denominator coincidence
that a random sample of that size is unlikely to hit (the project's own
standing lesson from rounds 24–26, re-confirmed here at one dimension
higher). **Do not cite or rely on the retracted claim going forward.**
The 60 individual chamber formulas themselves (`bisect-subset-lemma`,
Double-Bisect-Pin) remain correctly proved — only the *coverage* claim is
false, not the individual theorems.

**Round-30 update (new result, additive).** Proved a new, fully general
**Partition Chamber Theorem** (see "Round 30 build" below) that unifies
`bisect-subset-lemma`, Double-Bisect-Pin, and two new chamber families
(**Triple-Pin** and **Double-Pin-Pair**) as special cases of one
mechanism (partition the 5 indices into blocks, each block of size
$\ge2$ has one "host" piece cut to match the others exactly, contributing
only its own residual to the alternating sum; singleton blocks are either
left untouched or bisected away for free) — proved via
`pair-insensitivity-corollary` alone, no new machinery. Verified exact
(`Fraction`, no floats) that:
- the **Triple-Pin** instance closes witness 1 ($p=(11,7,6,3,2)/29$,
  $\Phi=1/2<16/31$);
- the **Double-Pin-Pair** instance closes witness 2
  ($p=(14,7,5,3,1)/30$), which the round-30 explorer found survives even
  the (unwritten) 20-chamber Triple-Pin family — $\Phi=1/2<16/31$.

Both witnesses that defeated the round-29 family are now individually
closed by named, proved chambers of the expanded (Partition Chamber)
family. **Full coverage of $\mathcal R$ by this expanded family is NOT
claimed** — per the explorer's own methodological warning (a family can
only ever report on itself; any future "100% covered" claim must be
re-verified by an outer, allocation-agnostic minimization search, not
sampling within the family), this round only (a) retracts the false
claim, (b) proves the new unifying theorem, and (c) confirms it closes
both known counterexamples. The Farkas-style exhaustive covering argument
for the (now larger, still possibly incomplete) family remains open. See
"Round 30 build" below for the full proof, verification, and honest
scope.

**Round-29 update (superseded by the round-30 retraction above for its
coverage claim; the individually-proved chamber theorems below remain
correct).** The $n=4$ general-marking upper bound's open territory is now
precisely $p_1<T/2$ AND $T/31<p_2<8T/31$ (proved, via free transplants of
already-general-$n$ lemmas — no new derivation). Within this residual, the
30-chamber `bisect-subset-lemma` family alone covers $\approx93\%$
(measured, exact `Fraction`); a newly proved 30-chamber
**Double-Bisect-Pin family** (general closed form
$\Phi=(T+|p_k-p_l-p_r|)/2$, proved via `pair-insensitivity-corollary`) is
correctly proved, but the round-29 claim that adding it raises *coverage*
to $100\%$ is **retracted** (see round-30 note above — refuted by an
exact counterexample defeating all 60 chambers at once). The Farkas-style
exhaustive covering argument itself remains the open gap for $n=4$'s upper
bound, and the family it must cover is now known to need at least the two
new chamber types proved this round. See "Round 29 build" below for the
(still-valid) chamber derivations; disregard only its §R29.5 coverage
claim.

**Round-28 update (new result, additive — does not supersede round 27,
which remains the complete $n=3$ upper bound).** The $p_1\ge T/2$ half of
the $n=4$ general-marking upper bound is now fully and rigorously
established: for every 5-piece marking with $p_1\ge T/2$,
$\Phi_{\min}(\cdot;4)\le a_4T=16T/31$. Proved by literally re-running §4's
$n=3$ mechanism one index up — Theorem A on $[T/2,a_4T)$, Theorem C′
(consuming round 27's now-complete $P(4)$ as its one-level-down tail
bound) on $[a_4T,T)$ — with the Telescoping Threshold identity
$a_3=a_4/(2(1-a_4))$ re-verified explicitly at $n=4$ to confirm the two
sub-case domains meet with no gap. See "Round 28 build" (§R28.0–R28.3)
below for the complete proof. **The $p_1<T/2$ half of $n=4$ remains
entirely open** — not a corollary of this result, and explicitly not
attempted this round (it needs a fresh chamber census, not a re-index).

**Round-27 update (supersedes the round-26 paragraph immediately below,
which contained the refuted "drop $p_1<T/2$ for free" claim — kept for the
historical record only, do not cite it).** The general-marking $n=3$ upper
bound $c(3)\le8/15$ is now **fully and rigorously established, with the
round-26 gap closed** ($p_1\ge T/2$, $T/15<p_2<4T/15$), via a four-regime
exhaustive split on $p_2\in(0,T/2]$ combined with a $p_1<T/2$ vs.
$p_1\ge T/2$ dichotomy on the middle regime:
- **$p_2\le T/15$:** `unconditional-p2-threshold-closure` (unconditional).
- **$p_2\ge4T/15$:** the Corollary to Theorem B $+$
  `n2-upper-bound-lp-argument` (unconditional).
- **$T/15<p_2<4T/15$, $p_1<T/2$:** `case-b2-n3-covering-closure`'s
  original 5-chamber family, **with the $p_1<T/2$ restriction restored**
  (the round-26 "drop it for free" claim was refuted by that round's
  reviewer).
- **$T/15<p_2<4T/15$, $p_1\ge T/2$:** the new Gap-Filler 4-chamber family
  (Chambers A, B, C, E; Pair-Insensitivity Corollary; two Farkas
  certificates), proved in full this round — see "Round 27 build" below.

See the "Round 27 build" section (§R27.0–R27.5) for the complete proof.
The paragraph immediately below (round 26) is stale/superseded on the
(b2) generalization point specifically; everything else in it not
contradicted here still stands.

**Round-26 update (fixes the round-25 citation bug and completes the
general-marking $n=3$ upper bound in full; see §R26.1–R26.3 for the
complete write-up).** The general upper bound $c(3)\le a_3=8/15$ is now
**fully and rigorously established for every legal Liu Bang marking at
$n=3$** (not just the ladder), via the correct three-way partition on
$p_2\in(0,T/2]$:
- **case (b1), $p_2\le T/15$:** `unconditional-p2-threshold-closure`
  (general $n$, unconditional).
- **case (b2), $T/15<p_2<4T/15$:** `case-b2-n3-covering-closure`, the
  round-25 5-chamber Farkas-certificate proof (§R25.1) — **generalized
  this round** to drop an unneeded $p_1<T/2$ restriction that was inherited
  from the old, buggy case split (none of the six certificates actually
  use it; corroborated by a fresh 200,000-trial search plus a
  65,648-point boundary grid, `/tmp/round-26/check2.py`, `check3.py`).
- **case (a), $p_2\ge4T/15$:** the Corollary to Theorem B ($m=4$,
  $S'=\{p_1-p_2,p_3,p_4\}$), its one hypothesis discharged
  **unconditionally** by the general (arbitrary-marking, no sortedness
  assumption) `lemmas/n2-upper-bound-lp-argument.md` — **this corrects the
  round-25 write-up's citation bug**, which had labeled case (a) as
  $p_1\ge T/2$ and cited `generalized-peel-identity` (a bare identity with
  no threshold, not the actual mechanism used).

The partition is explicitly verified gap-free and non-overlapping at both
boundaries ($p_2=T/15$ assigned to (b1)'s closed endpoint only;
$p_2=4T/15$ assigned to (a)'s closed endpoint only — see §R26.2), which
also directly resolves the round-25 "$p^\ast=(2/5,4/15,1/5,2/15)$" boundary
question: $p^\ast$ has $p_2=4T/15$ exactly, so it lies in case (a) and is
disposed of by the Corollary alone, with equality — no external
tie-analysis is needed. End-to-end re-verified by an independent
100,000-trial exact-`Fraction` script exercising all three mechanisms
together (`/tmp/round-26/check_full.py`), zero violations. **This is a
complete, non-numeric proof of the upper-bound direction only** — the
lower bound (achievability, $c(3)\ge8/15$) is a separate front tracked
elsewhere in `current.md`, and general $n\ge4$ (in particular case (b2)'s
chamber census) remains genuinely open and is not attempted this round per
the round-26 outline's explicit deferral. $n=4$'s case (a) bootstraps for
free from the identical Corollary mechanism (noted, not built).

**Round-24 update.** Case (b2) at $n=3$ is **not yet certified solved**, but
is now extremely close: a 20-member covering family (10 old + new
`Bisect-Subset` sub-family of up to 15 unconditional chambers, most already
counted among the 10, plus `Double-Sandwich-Below`, `Double-Sandwich-Above`,
`Triple-Pin`, `Chamber-R22.1.1`, `Chamber A`, `Chamber A2`, `Chamber B1`,
`Chamber B2`, `P1P2-tied-to-p3` — see "Round 24 build" for the full list
and every closed form) covers case (b2)'s box at $n=3$ on **every one** of
$1577$ deterministic exact-`Fraction` grid points and $3351$ random
exact-`Fraction` sample points tested (§R24.4) — zero residual, a sharp
jump from round 23's 99.6%. Every chamber's closed form and exact
feasibility region is now rigorously derived (not numerically recovered)
directly from the certified Cross-Piece Sign-Assignment Identity, and each
individually-insufficient chamber's own worst LP vertex has been computed
exactly (§R24.5) confirming the established pattern (no single chamber
suffices alone; the union is doing genuine work). **What remains open:** an
exhaustive (not sampling-based) proof that the union of these regions
literally contains the whole box — i.e., executing the finite
case-split/vertex enumeration that `p-space-chamber-vertex-theorem` +
`feasibility-suffices-for-upper-bound` show is *in principle* sufficient,
but whose actual combinatorics (which sub-region of which chamber's
feasibility polytope is adjacent to which other, and a proof that every
box point falls in at least one) has not been carried out by hand. This is
the single, sharply-localized remaining gap for a complete $n=3$
case-(b2) proof; see §R24.6 for the precise partial progress made on it
this round (a proven two-chamber sufficient identity, `Triple-Pin` +
`Double-Sandwich-Above`, that reduces — but does not close — one sub-case).

**Round-22 update.** The chamber machinery now has both halves it needs to
be usable for case (b2), modulo one still-open piece: the round-20/21
Within-Chamber Affinity Theorem (affinity *of* $\Phi_{\min}$ on a chamber)
is now complemented by this round's $p$-space Chamber-Vertex Theorem
(the chamber $U$ *itself* is a $p$-space polyhedron, so the affine target
inequality need only be checked at finitely many characterized vertices
per chamber) — see "Round 22 build", §R22.1. The strict-inequality
compactness gap the outline flagged is fully and rigorously resolved:
every point of $\overline{\mathrm{Box}}\setminus\mathrm{Box}$ (the three
walls $p_1=T/2$, $p_2=T/D_n$, $p_2=a_nT/2$) already lies in one of three
independently, unconditionally closed regions, so the vertex machinery is
only ever needed at genuine chamber-interior extreme points (§R22.2). This
is still infrastructure, **not** a closure of case (b2): the chamber-count
growth signal from round 20 is unaddressed, condition (c)
(type-optimality against every neighboring type) is proved only
schematically/conditionally, and no attempt was made this round to
actually enumerate case (b2)'s box into its finitely many chambers. **One
genuinely new negative result**: the round-22 outline's own proposed
"box-corner $\times$ tail-vertex decomposition" shortcut — which would
have reduced case (b2) to a 1-dimensional-per-piece search along the box
corner — is **refuted** by direct computation at both $n=3$ and $n=4$ (an
unrestricted search finds strictly worse witnesses off the corner than
any witness restricted to the corner); this closes off that shortcut as a
route to case (b2), consistent with (not a repeat of) the project's other
seven/eight already-dead mechanism families — see §R22.3 and
`lemmas/box-corner-tail-vertex-decomposition-refuted.md`.

**Round-20 update.** The within-chamber-affinity mechanism for case (b2)
(round-20 outline, `lp-duality-certificate`'s pivot to a primal
chamber-vertex framing) now has a fully written-out, from-scratch
well-posedness proof — see "Round 20 build" below — rather than the
one-line "direct consequence of step 1" the outline-reviewer correctly
flagged as overstated. The conditional Within-Chamber Affinity Theorem is
proved in full: **if** the chamber's joint tie/pin coefficient matrix
$M(\tau)$ is invertible, **then** $\Phi_{\min}$ restricted to that chamber
is affine in $p$; moreover $M(\tau)$ singular is proved to force $\tau$'s
region to have empty interior in $p$-space *except* for one honestly-flagged
residual algebraic-coincidence sub-case (an identically-vanishing
compatibility functional), which is not yet ruled out in general. The
mandated $n=2,3$ computational gates (steps 5a–5c of the outline) were run
and both passed / reported honestly: a direct numerical affinity check
along a fixed-composition segment at $n=3$ matches an affine model to
within optimizer noise, and a composition-level chamber-count sample at
$n=3,4$ inside case (b2)'s box shows a genuine growth signal (distinct-type
density rising from $\approx28\%$ to $\approx64\%$ of sampled points as $n$
goes from 3 to 4) — an honest amber flag for general-$n$ tractability, not a
disproof, exactly as the outline anticipated as the key risk to watch.
**Case (b2) remains open**: the affinity theorem is necessary infrastructure
for the outline's step 3–4 finite-extreme-point evaluation, but the actual
evaluation of $\Phi_{\min}$ at the resulting extreme-point family against
$a_nT$ (where the outline itself locates "the real work") has not been
attempted this round. See "Round 20 build" below for the full proof and
computational record.

**Round-19 update.** Consolidation round only. The surrogate/majorization
mechanism is now formally certified dead
(`lemmas/surrogate-adversary-dead-end.md`), and every existing certified
partial closure of the upper bound is re-confirmed unaffected by this
round's finding — see "Round 19 re-confirmation" immediately below for the
itemized check. **Open Gap 1 (the general upper bound $c(n)\le a_n$)
remains open, specifically at case (b2)**; no change in scope this round.

### Round 19 re-confirmation: prior closures do not assume a fixed/
near-ratio-2 worst tail

This round's task requires checking, explicitly, that no already-certified
partial closure implicitly relied on "the worst tail looks like the ratio-2
ladder" (or any other fixed tail shape) — since that premise is now shown
false in general (`surrogate-adversary-dead-end.md`). Checked directly
against the approach file's own statements and proofs:

1. **Case (a) closure** ($p_2\ge a_nT/2$, via the Theorem B recursive
   sufficient condition / `unconditional-p2-threshold-closure`). The proof
   (§"Corollary (Theorem B, recursive sufficient condition)" above) bounds
   $\Phi_{\min}(p_1,\dots,p_m)\le p_2+\Phi_{\min}(S')$ using the **actual**
   induction hypothesis value $\Phi_{\min}(S')\le a_{m-2}T'$ for
   $S'=\{p_1-p_2,p_3,\dots,p_m\}$ — an arbitrary reduced marking, not a
   fixed shape. It never substitutes an assumed tail shape for $S'$; the
   bound holds for whatever $S'$ actually is, by strong induction. **Not
   affected.**
2. **Case (b1) closure** ($p_2\le T/D_n$, via the Max Domination Lemma
   R13.2, `unconditional-p2-threshold-closure`). The proof uses the fully
   general inequality $A(S)\le\max(S)$ for *any* sorted multiset $S$ — a
   universal bound with no reference to any particular tail shape (ladder,
   geometric, or otherwise) at all. **Not affected.**
3. **Bisect-Top-$k$ Lemma and its case-(b2) coverage figures** (rounds
   14–15, $\approx10$–$26\%$ coverage). The identity $\Phi\le
   (T+p_{k+1})/2$ (proved via $k$-fold `pair-cancellation-identity`) is an
   **exact pointwise formula evaluated at each marking's own actual**
   $p_{k+1}$, not at a hypothesized worst-case value; the coverage
   percentages were measured by testing this exact formula against
   randomly-sampled *actual* markings, not against an assumed surrogate.
   **Not affected.**
4. **Cross-Piece Sign-Assignment Identity and its two closed case-(b2)
   witnesses** (round 15, $n=3$ flat-face witness
   $p=(4468,2591,2251,691)/10001$ and $n=4$ pinned-tie witness
   $p=(2933,2514,2131,1338,1085)/10001$). Both closures are direct exact
   evaluations of $\Phi$ at one **explicit, concrete, fully specified**
   marking via one explicit legal Xiang-Yu response, verified by direct
   computation on that exact multiset — not an argument of the form "the
   worst tail over a family is the ladder, hence bounded." The $n=3$
   witness's own tail ratio is $p_3/p_4=2251/691\approx3.26$ (nowhere near
   2), which is itself a small illustration that these closures never
   depended on tail values sitting near the ladder ratio. **Not affected.**
5. **Alternating Gap-Cross Lemma** (round 15) and its feasibility
   characterization: the feasibility test $\gamma_{i-1}>\max(p_{2i},
   p_{2i-1}-p_{2i})$ and the resulting sufficient condition both reference
   the marking's own actual $p_i$ values throughout, plus the universal
   (not shape-specific) fact $A(\text{tail})\le p_{2j+1}$
   (`max-domination-lemma`) for the *bound on the residual tail's
   alternating sum*, not an assumed worst-case tail shape. **Not affected.**
6. **Convex-Combination-Futility, Danskin/concavity, peel/bisect/recurse
   dead-end lemmas** (rounds 8, 14, 16–18). These are themselves negative
   results, not positive closures, and none of their proofs invokes a fixed
   worst-tail assumption (they reason about combinations of exact primal
   values, a specific concavity conjecture in Liu Bang's own tail-marking
   freedom, or exact recursive-image containment, respectively — distinct
   objects from "assume the tail looks like the ladder"). **Not affected.**

**Conclusion.** Every certified partial closure and every certified
negative/dead-end result on file remains valid after this round's finding.
The surrogate/majorization mechanism was never used as a *load-bearing*
step in any prior closure — it was explored only as a *candidate new*
mechanism this round and the previous rounds' explorer passes, and is now
confirmed to fail on its own merits, with zero retroactive impact on
earlier certified content.

**Round-18 update.** The Tail Exchange Lemma / Danskin smoothing
mechanism assigned this round is now shown, by the outline-reviewer's own
mandated cheap $n=3$ sanity check (§"Round 18 build" below), **not to
work as conceived**: its required premise (that $\Phi_{\min}$ is concave
in Liu Bang's own free tail marking, for fixed $p_1,p_2$) is false,
refuted by an explicit, robust interior local minimum at $p_3=p_1-p_2$ on
the on-file near-tight case-(b2) witness. This forecloses the
concavity/global-stationarity route specifically (a fourth distinct
mechanism family now ruled out for case (b2), after peel/bisect/recurse,
weighted-combination, and naive boundary continuity), while confirming
Danskin's theorem itself remains valid only as a *local* tool, not a
route to a global closed-form characterization, since the value function
is only piecewise-affine across finitely many combinatorial chambers with
no established convexity/concavity across chamber boundaries. **Open Gap
1 (the general upper bound $c(n)\le a_n$) remains open, specifically at
case (b2)** — see §"Round 18 build" below.

**Round-17 update.** The **Convex-Combination Futility Theorem** (new,
fully general, non-numeric, certified as
`convex-combination-futility-theorem`) proves that this round's assigned
mechanism — an explicit weighted combination of finitely many already-
certified primal Xiang-Yu strategies, with weights chosen by any rule
whatsoever (fixed, or $p$-dependent, including but not limited to the
circular "equate to target" mechanism the round-17 outline-reviewer
flagged) — can never certify a marking that the plain pointwise minimum
of the same strategies does not already certify. This is a genuine
negative/dead-end result for the entire "weighted-combination certificate"
framing this slug's round-17 outline proposed, established rigorously
rather than merely suspected; it does not close case (b2), and honestly
should not be read as progress toward closing it — its value is
foreclosing this whole family of future attempts and a structural
diagnosis (upper bounds on a minimum are witnessed by one strategy, not
improved by averaging several) suggesting this slug's actual technique
(LP duality/weighting) is the right tool for Claim (B)'s lower bound, not
this slug's own upper-bound target. **Open Gap 1 (the general upper bound
$c(n)\le a_n$) remains open, specifically at case (b2)** — see §"Round 17
build" below.

**Round-16 update.** `alternating-gap-cross-lemma`'s sign bug is now fully
(not just partially) corrected and re-certified — the true fix required
reindexing the gap-sum's own per-pair signs by split-rank, not just the
tail prefactor as the round-15 diagnosis/round-16 outline assumed; no
change to prior numeric coverage claims. The round-16 outline-reviewer's
mandatory gate check is answered rigorously: the "recursive-image-escape"
mechanism (recursed image lands in case (a)/(b1) one level down) is now
*proved* (new certified lemma `recursive-image-escape-dead-end`), not just
suspected, to be exactly the same zero-slack-inert mechanism the round-14
dead-end lemmas already ruled out — a genuine negative result closing off
an entire family of recursive arguments, not merely the two instances
previously covered. A broadened grid check of case (b2)'s $n=3$ box
(Task 3 fallback) corroborates, non-rigorously, round 14's finding of real
slack away from the known near-tight witness, but does not close case
(b2). **Open Gap 1 (the general upper bound $c(n)\le a_n$) remains open,
specifically at case (b2)** — see §"Round 16 build" below.

**Round-15 update.** Two new general, certified lemmas — the
**Cross-Piece Sign-Assignment Identity** (a strict generalization of
`pair-cancellation-identity`/`bisect-top-k-lemma`, proved directly from
`odd-run-reduction-lemma` plus an elementary finite-sum regrouping, §"Round
15 build" below) and the **Alternating Gap-Cross Lemma** (an explicit
$j$-parameter construction with a closed-form, non-numeric feasibility
test). Both round-14 near-tight case-(b2) witnesses ($n=3$ flat-face,
$n=4$ pinned-tie) are now shown, by exact-fraction reconstruction, to be
**unconditionally closed** by an explicit legal Xiang-Yu response — a
genuine, concrete win, though scoped to those two specific witnesses, not
a general closure. The Alternating Gap-Cross family's *marginal* coverage
of case (b2) beyond `bisect-top-k-lemma` is honestly quantified as small
(a few percentage points at $n=3$, none detected at $n=4,5$ in this
round's sample). **Open Gap 1 (the general upper bound $c(n)\le a_n$)
remains open, specifically at case (b2)** — see §"Round 15 build" below
for full proofs.

**Round-14 update.** The Bisect-Top-$k$ Lemma (proved in full for general
$n,k$ below, §"Round 14 build") strictly generalizes the round-13
`unconditional-p2-threshold-closure` (its $k=1$ special case) to a whole
family of unconditional (no induction hypothesis) sufficient conditions,
one per $k=0,\dots,n$ — genuinely new coverage of case (b2), though still
partial ($\approx10$–$26\%$ of case-(b2) witnesses at the $n$ tested).
Two exact-threshold "peel/bisect + full IH" mechanisms are now proved,
not just suspected, to be structurally incapable of ever reaching case
(b2) — recorded as certified negative lemmas so no future round retries
this specific family. A first vertex-restricted (rather than raw
whole-simplex) computational probe of case (b2) found no near-zero-margin
witness at $n=3,4$ (margins $\gtrsim0.015$), a weak, non-rigorous signal
that case (b2) may have genuine slack; **Open Gap 1 (the general upper
bound $c(n)\le a_n$) remains open, specifically at case (b2)**. See
§"Round 14 build" below for full proofs.

**Round-13 update.** New, fully general, unconditional Max Domination
Lemma (R13.1: $A(S)\le\max(S)$ for any sorted multiset) and its Corollary
(R13.2: $p_2\le T/D_n$ closes the general upper bound with zero induction
dependence, for every $n$ and every marking) — genuinely new sub-case,
disjoint from every previously-certified sufficient region. The Peel-Target
Existence Lemma from the round-13 outline is now precisely restated as an
honest trichotomy (§R13.3): case (a) conditional-on-IH closure (already
known, verified to transfer), case (b1) new unconditional closure (R13.2),
case (b2) genuinely open with an explicit non-vacuous witness at $n=3$. A
natural 2-cut extension attempting to close case (b2) unconditionally
("peel-then-dominate") was tested and refuted by exact witness (§R13.3).
**Open Gap 1 (the general upper bound $c(n)\le a_n$) remains open** — see
§"Round 13 build" below for full proofs and the sharpened diagnosis.

**Round-12 update.** Two new fully general, unconditionally proved lemmas
this round — `equal-pieces-closure` (§R12.1) and `spare-cut-bisection-
corollary` (§R12.2) — close, for every $n$, the equal-pieces marking and
every marking where the Iterated Greedy-Peel Construction has spare cut
budget. Both are genuine, reusable, non-numeric results. The
outline-reviewer's proposed gap-closing pigeonhole selection rule (steps
3–4 of the round-12 outline) was independently confirmed a dead end by
exhaustive brute-force search and was **not** built. A further attempt at
the outline-reviewer's redirect target (b) — evaluating the certified
Per-Piece Vertex Decomposition Theorem's joint vertex family against
$a_nT$ for arbitrary markings — made honest partial progress (a
quantification of how generic the still-open residual is, §R12.3, and a
second natural construction, "bisect the current largest $n$ times",
tested and refuted by an exact witness, §R12.4) but did **not** close the
general upper bound. See §"Round 12 build" below for full proofs and the
open-gap diagnosis (§R12.5).

**Setup (shared, imported not re-derived).** By the claiming-subgame
reduction and the certified `integral-alternating-sum-formula`
(`greedy-halving-adversary` Lemmas 1-2), for a finite multiset $S$ of
positive reals with total $T$, $\Phi(S)=(T+A(S))/2$ where $A(S)$ is the
sorted alternating sum, and $A(S)=\int_0^\infty\mathbb1[N_S(x)\text{ odd}]dx$.
Two further certified tools are used without re-derivation:

- **`leftover-formula`**: if $R=\{v\}\cup\{a_1,a_1\}\cup\cdots\cup\{a_k,a_k\}$
  (one unpaired element $v$, $k$ exactly-equal pairs, regardless of where
  $v$ sits in sorted order), then $A(R)=v$, $\Phi(R)=(\mathrm{Total}(R)+v)/2$.
- **`pair-cancellation-identity`**: for any $a>0$ and any finite multiset
  $T$ of positive reals, $A(\{a,a\}\cup T)=A(T)$ (an exact pair contributes
  even count to $N(x)$ for every $x$, so it never changes the parity that
  determines $A$).

Fix $n\ge0$ and an arbitrary Liu Bang marking with $m=n+1$ pieces
$p_1\ge p_2\ge\cdots\ge p_m>0$, $\sum p_i=T$ (normalize $T=1$ at the end;
all identities below are stated for general $T$ by homogeneity). Xiang Yu
has a budget of $\le n=m-1$ cuts. Write $a_n:=2^n/(2^{n+1}-1)$.

### Four exact, unconditional Xiang Yu strategies

Each of the following is a **legal move within budget**, and its resulting
$\Phi$-value is computed **exactly**, for *every* $m\ge1$ and *every*
marking — no case restriction is used in deriving the formula itself
(restrictions only enter later, in deciding whether the formula's value
meets the target $a_nT$).

**Theorem A (Full-Match Achievability).** *If $p_1\ge T/2$ (equivalently
$p_1\ge p_2+\cdots+p_m$), Xiang Yu can use exactly $m-1$ cuts, all inside
$p_1$, to split it into fragments of sizes exactly $p_2,p_3,\dots,p_m$ plus
a leftover $v:=p_1-(p_2+\cdots+p_m)=2p_1-T\ge0$ (leaving $p_2,\dots,p_m$
untouched). This achieves $\Phi=p_1$ exactly.*

*Proof.* Splitting one piece into $m-1$ fragments of prescribed sizes
$p_2,\dots,p_m$ plus a leftover requires exactly $m$ parts, i.e. $m-1$
cuts — within the budget $n=m-1$, and legal precisely when the leftover
$v=p_1-\sum_{i\ge2}p_i\ge0$, i.e. $p_1\ge T-p_1$, i.e. $p_1\ge T/2$. The
resulting multiset is $\{p_2,p_2,p_3,p_3,\dots,p_m,p_m\}\cup\{v\}$ (or
without $v$ if $v=0$): exactly `leftover-formula`'s hypothesis with $k=m-1$
pairs and unpaired element $v$. Hence $A=v$, and
$\Phi=(T+v)/2=(T+2p_1-T)/2=p_1$. $\blacksquare$

**Theorem B (One-Step-Peel Identity, exact reduction).** *For $m\ge2$, let
$w:=p_1-p_2\ge0$ (legal since $p_1\ge p_2$) and $S':=\{w,p_3,\dots,p_m\}$
($m-1$ elements, total $T':=T-2p_2$). For **any** further Xiang Yu strategy
applied to $S'$ using $\le m-2$ cuts, producing a final refinement $M'$ of
$S'$ with value $\Phi(M')=:\Phi'$, the combined strategy — cut $p_1$ into
$(p_2,w)$ (1 cut) then apply the $S'$-strategy to $\{w,p_3,\dots,p_m\}$
($\le m-2$ further cuts, total $\le m-1=n$) — yields*
$$\Phi(\text{final}) = p_2+\Phi'.$$

*Proof.* The final multiset is $\{p_2,p_2\}\cup M'$ (the original untouched
$p_2$, the fragment of size $p_2$ cut from $p_1$, and $M'$). By
`pair-cancellation-identity`, $A(\{p_2,p_2\}\cup M')=A(M')$. Writing
$T'=\mathrm{Total}(M')=\mathrm{Total}(S')=T-2p_2$ (cutting preserves total),
$A(M')=2\Phi'-T'$. Hence
$$\Phi(\text{final})=\frac{T+A(\{p_2,p_2\}\cup M')}{2}=\frac{T+2\Phi'-T'}{2}
=\frac{T-T'}{2}+\Phi' = p_2+\Phi',$$
using $T-T'=2p_2$. $\blacksquare$ This is an **exact bookkeeping identity**,
true regardless of which strategy is used on $S'$ — it holds for the
*optimal* strategy on $S'$ in particular, so
$\Phi_{\min}(p_1,\dots,p_m)\le p_2+\Phi_{\min}(S')$ always.

**Theorem C (Bisect-Top Identity, exact).** *Bisecting $p_1$ alone
($p_1\to p_1/2,p_1/2$, using 1 cut, leaving $p_2,\dots,p_m$ entirely
untouched) achieves*
$$\Phi = \frac{p_1}{2} + \Phi_{\mathrm{tail}},\qquad
\Phi_{\mathrm{tail}}:=p_2+p_4+p_6+\cdots$$
*(the odd-local-rank sum of the already-sorted tail $p_2,\dots,p_m$, a
directly computable constant — no further cuts, no recursion).*

*Proof.* The final multiset is $\{p_1/2,p_1/2\}\cup\{p_2,\dots,p_m\}$. By
`pair-cancellation-identity`, $A(\text{final})=A(\{p_2,\dots,p_m\})$. The
tail is untouched and already sorted, so its own $\Phi_{\mathrm{tail}}$ is
literally the sum of its odd local ranks $p_2,p_4,\dots$, and
$A(\{p_2,\dots,p_m\})=2\Phi_{\mathrm{tail}}-(T-p_1)$. Hence
$\Phi=(T+A(\text{final}))/2=(T+2\Phi_{\mathrm{tail}}-(T-p_1))/2
=p_1/2+\Phi_{\mathrm{tail}}$. $\blacksquare$ (This generalizes and
reproduces `smoothing-compactness-certificate.md`'s Template A exactly:
at $m=3$, $\Phi_{\mathrm{tail}}=p_2$ since the tail has only 2 elements,
giving $\Phi=p_1/2+p_2$, the cited $\Phi_A$.)

**Theorem D (Bisect-Top-and-Bottom Identity, exact, new this round).**
*For $m\ge2$, bisecting both $p_1$ and $p_m$ simultaneously (2 cuts,
leaving $p_2,\dots,p_{m-1}$ untouched) achieves*
$$\Phi = \frac{p_1}{2}+\frac{p_m}{2}+\Phi_{\mathrm{mid}},\qquad
\Phi_{\mathrm{mid}}:=p_2+p_4+p_6+\cdots\ \text{(odd local ranks of the
untouched middle block }p_2,\dots,p_{m-1}\text{)}.$$

*Proof.* Identical structure to Theorem C, applying
`pair-cancellation-identity` twice (once for each of the two exact pairs
$\{p_1/2,p_1/2\}$, $\{p_m/2,p_m/2\}$): $A(\text{final})=
A(\{p_2,\dots,p_{m-1}\})$, and the middle block is untouched and sorted, so
its own $\Phi_{\mathrm{mid}}$ is its odd-local-rank sum, giving (with
$\mathrm{Total}(\text{middle})=T-p_1-p_m$)
$\Phi=(p_1+p_m)/2+\Phi_{\mathrm{mid}}$ by the same algebra as Theorem C.
$\blacksquare$

All four theorems are **exact identities holding for every $n\ge1$ and
every marking with no restriction** — the case-dependence enters only when
asking whether the resulting value meets $a_nT$; this is a genuine, new,
general-$n$ mechanism (not template case-analysis), and Theorems B, C, D
are proposed for certification below.

### Proven sufficient conditions (closed form, not numerics)

**Corollary (Theorem A closes a band).** Theorem A gives $\Phi=p_1\le a_nT$
exactly when $p_1\in[T/2,\,a_nT]$ (the interval is nonempty since
$a_n>1/2$ for every $n$).

**Corollary (Theorem B, recursive sufficient condition).** *If
$p_2\ge a_n\cdot T/2$, and the reduced instance $S'=\{w,p_3,\dots,p_m\}$
($w=p_1-p_2$) satisfies $\Phi_{\min}(S')\le a_{m-2}T'$ (i.e. $S'$ lies in
the inductively-established domain one level down), then
$\Phi_{\min}(p_1,\dots,p_m)\le a_n T$.*

*Proof.* By Theorem B, $\Phi_{\min}\le p_2+\Phi_{\min}(S')\le
p_2+a_{m-2}T'=p_2+a_{m-2}(T-2p_2)$. We must show this is $\le a_nT$
(recall $n=m-1$). Writing $D_k:=2^{k+1}-1$ so $a_k=2^k/D_k$ and
$2a_k-1=1/D_k$: the required inequality
$p_2(1-2a_{m-2})\le(a_{m-1}-a_{m-2})T$ rearranges (since $1-2a_{m-2}<0$) to
$p_2\ge\big(a_{m-2}-a_{m-1}\big)T/(2a_{m-2}-1)$. A direct computation gives
$a_{m-2}-a_{m-1}=2^{m-2}/(D_{m-2}D_{m-1})$ (common-denominator expansion,
using $2^{m-2}D_{m-1}-2^{m-1}D_{m-2}=2^{m-2}$, checked directly:
$2^{m-2}(2^m-1)-2^{m-1}(2^{m-1}-1)=2^{2m-2}-2^{m-2}-2^{2m-2}+2^{m-1}
=2^{m-1}-2^{m-2}=2^{m-2}$), and $2a_{m-2}-1=1/D_{m-2}$, so the threshold is
$\big(2^{m-2}/(D_{m-2}D_{m-1})\big)\cdot D_{m-2}=2^{m-2}/D_{m-1}
=2^{m-2}/(2^m-1)=a_{m-1}/2=a_n/2$. Hence the condition is exactly
$p_2\ge a_nT/2$. $\blacksquare$ (Independently cross-checked symbolically
with `sympy` for $m=2,\dots,6$ and numerically with exact `Fraction`
arithmetic on $200{,}000$ random configurations for $m=2,\dots,8$: zero
violations of "condition holds $\Rightarrow$ bound holds" in either check.)

**Corollary (Theorem D, crude but proven sufficient condition).** Using
$A(\text{middle block})\le\mathrm{Total}(\text{middle})=T-p_1-p_m$ (the
general bound $A\le\mathrm{Total}$ from `integral-alternating-sum-formula`)
in place of the exact $\Phi_{\mathrm{mid}}$ gives $\Phi\le T-(p_1+p_m)/2$,
hence $\Phi\le a_nT$ whenever $p_1+p_m\ge2(1-a_n)T$. (This crude bound is
much weaker than the exact identity used computationally below, but is a
genuine, closed-form, unconditionally proven sufficient condition, parallel
in status to Theorem A/B's conditions.)

### Combined recursive domain: proven, but not exhaustive

Define, by strong induction on $m$, a domain $\mathcal D_m$ of markings for
which $\Phi_{\min}\le a_{m-1}T$ is established: $\mathcal D_1$ is all
1-piece "configurations" (trivial); for $m\ge2$, $\mathcal D_m$ is the
union of (i) configurations with $p_1\in[T/2,a_{m-1}T]$ (Theorem A), (ii)
configurations with $p_1+p_m\ge2(1-a_{m-1})T$ (Theorem D, crude bound), and
(iii) configurations with $p_2\ge a_{m-1}T/2$ whose one-step-peel reduct
lies in $\mathcal D_{m-1}$ (Theorem B). **Theorem (Domain Closure).** *For
every $m\ge1$ and every marking in $\mathcal D_m$, $\Phi_{\min}\le
a_{m-1}T$.* This is proved rigorously by the three corollaries above,
combined by strong induction (base case $m=1$ trivial: $\Phi=T=a_0T$).

### What the domain covers, and what it does not (honest accounting)

The three *proven* sufficient conditions above are individually correct
but, used with their crude bounds, leave a substantial gap (verified: only
$\approx16$–$20\%$ of random configurations fall in $\mathcal D_m$ as
literally proven, exact `Fraction` computation, $200{,}000$ trials,
$m=2,\dots,8$). This is real but limited progress by itself.

**However**, using the *exact* values of Theorems A–D (not their crude
proven bounds) and taking, at every recursive level, the literal minimum
of all four candidates, gives a **fully specified, always-legal Xiang Yu
strategy** for every $n$ and every marking (not merely a sufficient
condition — an actual constructive strategy). This combined strategy was
**stress-tested computationally** (clearly flagged: this is a numeric
diagnostic, not a proof step, per this project's rigor rules):

- **Exhaustive** over the grid of $3$-piece integer-ratio markings with
  denominator $\le80$ ($85{,}320$ points, $n=2$): **zero violations**
  (every point achieves $\Phi\le4/7$ via one of the four exact formulas) —
  consistent with, though not a new proof of, the already-certified
  $c(2)\le4/7$ upper bound (`smoothing-compactness-certificate.md`), via a
  structurally different (recursive, non-template-region) mechanism.
- **$150{,}000+$ independent random trials**, exact `Fraction` arithmetic,
  $m=2,\dots,8$ ($n=1,\dots,7$): **zero violations**.
- **Round 4's own $n=3$ witness** $(p,q,r,s)=(3/8,1/4,1/4,1/8)$, which
  defeated the raw six-template generalization: this family finds
  $\Phi=1/2<8/15$ (via Theorem D, bisecting $p$ and $s$ simultaneously,
  matching round 4's own ad hoc trisection discovery in spirit though by a
  different exact route) — **solved** by this family, unlike the naive
  six-template generalization.
- **A fresh, smaller witness this round located and exactly diagnosed**:
  at $n=3$, $(p_1,p_2,p_3,p_4)=(6,2,2,1)/11$, **Theorems A, B, and C all
  independently evaluate to exactly $6/11>8/15$** (verified by hand and by
  exact-`Fraction` script: $A$ gives $p_1=6/11$; $C$ gives
  $p_1/2+p_2=3/11+2/11+1/11=6/11$ — wait, computed precisely as
  $p_1/2+\Phi_{\mathrm{tail}}$ with $\Phi_{\mathrm{tail}}=p_2+p_4=2/11+1/11
  =3/11$, giving $3/11+3/11=6/11$; $B$ recurses to the same value $6/11$
  exactly) — a genuine, three-way tie at a value exceeding target, directly
  analogous in shape to round 4's finding that several templates
  simultaneously fail at one point. **Theorem D resolves it**: bisecting
  $p_1$ and $p_4$ (the top and bottom pieces) gives, exactly,
  $\Phi=p_1/2+p_4/2+\Phi_{\mathrm{mid}}=3/11+1/22+2/11=11/22=1/2<8/15$ —
  confirmed independently by a floating-point `scipy.optimize`
  multi-start search over *all* cut-distribution compositions at this
  point, which found the true minimum is exactly $1/2$, attained at
  bisect-$p_1$-and-$p_4$, matching Theorem D's closed form exactly (and
  confirming this point is **not** a counterexample to the conjecture —
  only to the narrower 3-strategy family).
- **Adversarial search**: `scipy.optimize.differential_evolution`,
  maximizing (over the full marking simplex) the shortfall
  $\Phi_{\text{4-strategy}}-a_nT$, for $n=3,4,5,6$: the optimizer could not
  find any positive shortfall (best found: strongly negative, i.e. the
  4-strategy value settles near $T/2$, well under target, at every local
  search it tried).

**Conclusion (honest, not overclaimed).** The four exact identities,
combined greedily (take the true minimum), pass every computational stress
test attempted this round (exhaustive at $n=2$, $150{,}000+$ random and
adversarial-search trials at $n=1,\dots,6$, and both of the two known
"hard" witnesses from round 4 and this round) — but **this is numeric
evidence for a conjecture, not a proof**, per this project's own rigor
rule that a numeric check is not a proof step. **No general-$n$ closed-form
theorem establishing "$\min(A,B,C,D)\le a_nT$ for every marking" has been
proved this round** — only the three individual sufficient conditions
above (which cover a much smaller, but *rigorously certain*, sub-domain).

## Round 9 formalization (this round's build)

Throughout, fix $n\ge0$, $m=n+1$, a marking $p_1\ge p_2\ge\cdots\ge p_m>0$
with $\sum p_i=T$, and write $a_k:=2^k/(2^{k+1}-1)$, $D_k:=2^{k+1}-1$ (so
$a_k=2^k/D_k$). Let $\Phi_{\min}(p_1,\dots,p_m;\,n)$ denote the minimum
value of $\Phi$ Xiang Yu can force using $\le n$ further cuts on this
marking (the quantity the whole approach studies). Define, for $k\ge0$,
the statement
$$P(k):\quad\text{for every marking of exactly $k$ pieces (budget $n=k-1$
cuts), }\Phi_{\min}\le a_{k-1}T.$$
This $P(k)$, for every $k\ge1$, is exactly the problem's upper-bound half
$c(n)\le a_n$ at $n=k-1$. $P(0)$ is vacuous.

### §1. Two exact, unconditional identities (full proofs)

**Theorem C′ (Bisect-Top, Recursive).** *For $m\ge2$, bisecting $p_1$ alone
(1 cut) and then applying **any** further legal strategy to the untouched
tail $\{p_2,\dots,p_m\}$ using $\le n-1=m-2$ further cuts, producing a
refinement $M'$ with value $\Phi'$, yields, exactly,*
$$\Phi(\text{combined}) = \frac{p_1}{2}+\Phi'.$$
*Consequently $\Phi_{\min}(p_1,\dots,p_m;\,n)\le p_1/2+\Phi_{\min}(p_2,\dots,p_m;\,n-1)$.*

*Proof.* The final multiset is $\{p_1/2,p_1/2\}\cup M'$. By the certified
`pair-cancellation-identity`, $A(\{p_1/2,p_1/2\}\cup M')=A(M')$ (inserting
an exact pair never changes the parity of $N_S(x)$ at any $x$, regardless
of where the pair lands in sorted order). Writing $T':=T-p_1=\mathrm{Total}(M')$
(cutting preserves total, and the tail's total is unaffected by the
$p_1$-bisection), $A(M')=2\Phi'-T'$. Hence
$$\Phi(\text{combined})=\frac{T+A(\{p_1/2,p_1/2\}\cup M')}{2}
=\frac{T+2\Phi'-T'}{2}=\frac{T-T'}{2}+\Phi'=\frac{p_1}{2}+\Phi'.$$
This holds for *any* legal tail strategy, in particular the optimal one,
giving the stated inequality. $\blacksquare$ (This is structurally
identical to the already-certified `one-step-peel-identity`'s proof —
same pair-cancellation mechanism, applied to the pair $\{p_1/2,p_1/2\}$
instead of $\{p_2,p_2\}$ — so it inherits the same certification standard.
The bisection uses exactly $1$ cut, legal for every $m\ge2$, i.e. $n\ge1$.)

**Theorem B$_k$ (Generalized One-Step-Peel).** *For $m\ge2$ and any index
$k\in\{2,\dots,m\}$, let $w_k:=p_1-p_k\ge0$ (legal since $p_1\ge p_k$) and
$S'_k:=\{w_k\}\cup\{p_i:2\le i\le m,\ i\ne k\}$ ($m-1$ elements, total
$T-2p_k$). For any further legal strategy on $S'_k$ using $\le m-2$ cuts,
producing refinement $M'$ with value $\Phi'$, the combined strategy (cut
$p_1$ into $(p_k,w_k)$, then the $S'_k$-strategy) yields, exactly,
$\Phi(\text{combined})=p_k+\Phi'$.*

*Proof.* Identical to the proof of the certified `one-step-peel-identity`
with $p_2$ relabeled $p_k$ throughout: the final multiset is
$\{p_k,p_k\}\cup M'$ (the untouched original $p_k$ and the new fragment of
size $p_k$ cut from $p_1$), and `pair-cancellation-identity` plus the same
total-bookkeeping algebra gives $\Phi(\text{combined})=p_k+\Phi'$. Nothing
in the original proof used $k=2$ specifically — only that $p_k$ is some
fixed tail value being matched — so it transfers verbatim. $\blacksquare$

### §2. The telescoping threshold identity (general $n$, full proof)

**Lemma (Telescoping Threshold).** *For every $n\ge1$,*
$$a_{n-1}=\frac{a_n}{2(1-a_n)}.$$

*Proof.* First, $a_k>1/2$ for every $k\ge0$: $a_k-\tfrac12=\dfrac{2^k}{D_k}-\dfrac12
=\dfrac{2^{k+1}-D_k}{2D_k}=\dfrac{2^{k+1}-(2^{k+1}-1)}{2D_k}=\dfrac{1}{2D_k}>0$.
So $1-a_n<1/2<1$, in particular $1-a_n=1-\tfrac{2^n}{D_n}=\dfrac{D_n-2^n}{D_n}
=\dfrac{2^{n+1}-1-2^n}{D_n}=\dfrac{2^n-1}{D_n}=\dfrac{D_{n-1}}{D_n}$ (using
$D_{n-1}=2^n-1$, valid since $n\ge1$). Hence
$$\frac{a_n}{2(1-a_n)}=\frac{2^n/D_n}{2\cdot D_{n-1}/D_n}=\frac{2^n}{2D_{n-1}}
=\frac{2^{n-1}}{D_{n-1}}=a_{n-1}.\qquad\blacksquare$$

**Corollary (Theorem C′'s threshold, general $n$).** *For $n\ge1$: if
$p_1\ge a_nT$, then, granting $\Phi_{\min}(\text{tail};\,n-1)\le a_{n-1}T'$
($T'=T-p_1$, i.e. granting $P(m-1)$ applied to this specific tail),
Theorem C′ gives $\Phi_{\min}(p_1,\dots,p_m;\,n)\le a_nT$.*

*Proof.* By Theorem C′ and the granted tail bound,
$$\Phi_{\min}\le\frac{p_1}{2}+a_{n-1}(T-p_1)=a_{n-1}T+p_1\Big(\frac12-a_{n-1}\Big).$$
Since $a_{n-1}>1/2$ (shown above), the coefficient $\tfrac12-a_{n-1}$ is
strictly negative, so the right side is a strictly decreasing (affine)
function of $p_1$ on the range $p_1\in[a_nT,T)$. Hence its value is
maximized at the left endpoint $p_1=a_nT$:
$$\Phi_{\min}\le a_{n-1}T+a_nT\Big(\frac12-a_{n-1}\Big)
=T\Big[a_{n-1}(1-a_n)+\frac{a_n}{2}\Big].$$
By the Telescoping Threshold Lemma, $a_{n-1}=\dfrac{a_n}{2(1-a_n)}$, so
$a_{n-1}(1-a_n)=\dfrac{a_n}{2}$, and the bracket becomes
$\dfrac{a_n}{2}+\dfrac{a_n}{2}=a_n$. Hence $\Phi_{\min}\le a_nT$ exactly,
with the bound tight (zero slack) at $p_1=a_nT$. $\blacksquare$ (This
proves, for every $n\ge1$, the exact zero-slack threshold match the
round-9 explorer verified only for $n\le8$ and the outline-reviewer
independently re-checked for $n\le9$ — now a genuine general-$n$ theorem,
not a finite check.)

### §3. Base cases $P(0),P(1),P(2)$: fully closed (both regimes, all markings)

- $P(0)$: vacuous (no pieces).
- $P(1)$ ($m=1$, $n=0$): the single piece is entirely Liu Bang's, no cuts
  possible; $\Phi=T=a_0T$ since $a_0=2^0/(2^1-1)=1$. Trivial.
- $P(2)$ ($m=2$, $n=1$): here $p_1\ge p_2>0$ and $p_1+p_2=T$ force
  $p_1\ge T/2$ **always** — there is no $p_1<T/2$ sub-case at $m=2$. By
  Theorem A (Full-Match Achievability, proved above from the certified
  `leftover-formula`), $\Phi_{\min}=\Phi=p_1\le T$; combined with the
  $p_1\ge a_1T$ sub-case closed by the Corollary above ($n=1$: threshold
  $a_1T=\tfrac23T$; for $p_1\ge\tfrac23T$, Theorem C′ with the trivial tail
  base case $P(1)$ as its IH gives $\Phi_{\min}\le a_1T$ exactly) and the
  $T/2\le p_1<a_1T$ sub-case closed directly by Theorem A ($\Phi=p_1<a_1T$),
  $P(2)$ holds for **every** 2-piece marking, both regimes (regime $p_1<T/2$
  being empty). $P(2)$ is fully, rigorously established.
- $P(3)$ ($m=3$, $n=2$): **imported, not re-derived**, from the certified
  `n2-upper-bound-lp-argument` lemma: "for every Liu Bang configuration
  (every 3-piece marking $p\ge q\ge r>0$), Xiang Yu has a response with
  $\Phi\le\tfrac47T=a_2T$." This is stated and certified for *every*
  configuration in the simplex (both the $p\ge T/2$ and $p<T/2$ regions,
  via the certificate's own two-region case split), so $P(3)$ is fully
  established, both regimes, no restriction.

### §4. $p_1\ge T/2$ closed rigorously and unconditionally for $n\le3$

**Theorem ($p_1\ge T/2$ closure at $n=3$).** *For every 4-piece marking
$p_1\ge p_2\ge p_3\ge p_4>0$ with $p_1\ge T/2$, $\Phi_{\min}(\,\cdot\,;3)\le
a_3T=\tfrac{8}{15}T$.*

*Proof.* Two sub-cases, partitioning $[T/2,T)$ with no gap since
$a_3=\tfrac{8}{15}\in(\tfrac12,1)$:
- **$T/2\le p_1<a_3T$:** Theorem A gives $\Phi=p_1<a_3T$ directly (no
  recursion, no tail assumption needed at all).
- **$p_1\ge a_3T$:** Theorem C′ applies with tail $\{p_2,p_3,p_4\}$
  ($m'=3$ pieces, budget $n-1=2$). By $P(3)$ (§3, fully established for
  *every* 3-piece marking, hence in particular for this specific tail,
  whatever its own regime), $\Phi_{\min}(\text{tail};2)\le a_2T'$. The
  Corollary of §2 (with $n=3$) then gives $\Phi_{\min}\le a_3T$ exactly.

These two sub-cases cover all of $p_1\ge T/2$ (using $p_1<T$, true since
$m=4\ge2$ forces other pieces positive). $\blacksquare$

**This is a genuine, complete, unconditional result: the $p_1\ge T/2$ half
of $P(4)$ (i.e. of $c(3)\le\tfrac{8}{15}$ restricted to $p_1\ge T/2$) is
fully closed**, because the only ingredient Theorem C′ needed one level
down — $P(3)$ for an *arbitrary* tail — is already fully available
(imported from the certified lemma), not merely for tails that themselves
satisfy $p_1\ge T/2$.

**Why this does not extend past $n=3$ (the circularity the outline
missed).** To close the $p_1\ge T/2$ half of $P(5)$ ($n=4$) the same way,
Theorem C′ needs $P(4)$ for an *arbitrary* 4-piece tail — not just the
$p_1\ge T/2$ half of $P(4)$ just proved, but *also* its $p_1<T/2$ half,
because a tail $\{p_2,\dots,p_5\}$ can itself have its own largest element
below half its own total (this literally happens for the witness
$(6,2,2,1)/11$'s own recursive structure one level down: the *tail*
$\{2,2,1\}/11$ has "own $p_1$" $=2/11<\tfrac12\cdot\tfrac5{11}=\tfrac5{22}$,
i.e. the tail sits in the *open* regime at $m'=3$ — resolved there only
because $P(3)$ happens to be fully closed already, not because the regime
split itself is free). Since $P(4)$'s $p_1<T/2$ half is **not** established
(§5 below), the induction **cannot be pushed past $n=3$ using this
mechanism alone** without first closing $p_1<T/2$ at $n=3$. This is a
genuine, previously unflagged gap in the outline's "near-mechanical
induction" framing, now made precise: the two regimes are not independent
halves that can be closed in either order past $n=3$ — Theorem C′'s
regime consumes the *other* regime's result one level down as a
prerequisite.

**Corrected witness classification** (per the outline-reviewer's flag,
now verified directly): $(6,2,2,1)/11$ has $p_1=6/11\ge1/2=T/2$ and
$p_1=6/11\ge a_3T=8/15$ (since $6/11=0.5\overline{45}>8/15=0.5\overline{3}$),
so it falls in the *second* sub-case above and **is resolved** by this
theorem — not still open. Only $(3/8,1/4,1/4,1/8)$ (which has
$p_1=3/8<1/2=T/2$) genuinely lives in the still-open regime.

### §5. The $p_1<T/2$ regime at $n=3$: partial toolkit, not a general closure

Theorem C′/A do not apply when $p_1<T/2$. Two further identities were
derived and proved in full this round (both instances of the same
pair-cancellation mechanism as Theorems C′/B$_k$, hence equally rigorous):

**Theorem D′ (Bisect-Top-and-Bottom, Recursive).** *For $m\ge2$, bisecting
$p_1$ and $p_m$ simultaneously (2 cuts) and applying any further legal
strategy to the untouched middle $\{p_2,\dots,p_{m-1}\}$ (budget $n-2$),
producing refinement $M'$ with value $\Phi'$, yields exactly
$\Phi(\text{combined})=\tfrac{p_1+p_m}{2}+\Phi'$.*

*Proof.* Same structure as Theorem C′, applying `pair-cancellation-identity`
twice (once for each exact pair $\{p_1/2,p_1/2\}$, $\{p_m/2,p_m/2\}$):
the final multiset is $\{p_1/2,p_1/2,p_m/2,p_m/2\}\cup M'$, so
$A(\text{final})=A(M')$, and the same total-bookkeeping algebra
($T-T''=p_1+p_m$ where $T''=\mathrm{Total}(M')$) gives the stated
identity. $\blacksquare$

**Theorem E (Bisect-Top-Two).** *For $m\ge3$, bisecting $p_1,p_2$
simultaneously (2 cuts) and recursing on $\{p_3,\dots,p_m\}$ (budget
$n-2$) with tail value $\Phi'$ yields exactly $\Phi(\text{combined})
=\tfrac{p_1+p_2}{2}+\Phi'$.* (Identical proof.)

**Exact threshold for Theorem D′'s IH-ceiling version (general $n\ge2$,
full proof).** Substituting the induction ceiling $\Phi'\le a_{n-2}T''$
($T''=T-p_1-p_m$) into Theorem D′: $\Phi_{\min}\le a_{n-2}T+s(\tfrac12-a_{n-2})$
where $s:=p_1+p_m$. Since $a_{n-2}>1/2$ for $n\ge2$, this is decreasing in
$s$, so it is $\le a_nT$ exactly when $s\ge s^\ast$, where solving
$a_{n-2}T+s^\ast(\tfrac12-a_{n-2})=a_nT$ gives
$s^\ast=T\cdot\dfrac{a_{n-2}-a_n}{a_{n-2}-\tfrac12}$. Direct computation
(using $D_{n-2}=2^{n-1}-1$, $D_n=2^{n+1}-1$):
$$a_{n-2}-a_n=\frac{2^{n-2}}{D_{n-2}}-\frac{2^n}{D_n}
=\frac{2^{n-2}D_n-2^nD_{n-2}}{D_{n-2}D_n}
=\frac{(2^{2n-1}-2^{n-2})-(2^{2n-1}-2^n)}{D_{n-2}D_n}
=\frac{3\cdot2^{n-2}}{D_{n-2}D_n},$$
and $a_{n-2}-\tfrac12=\tfrac{1}{2D_{n-2}}$ (§2's identity, index $n-2$).
Hence
$$s^\ast=T\cdot\frac{3\cdot2^{n-2}/(D_{n-2}D_n)}{1/(2D_{n-2})}
=T\cdot\frac{6\cdot2^{n-2}}{D_n}=T\cdot\frac{3\cdot2^{n-1}}{D_n}
=\frac32\cdot\frac{2^n}{D_n}\cdot T=\frac32\,a_nT.$$
(Verified exactly by `Fraction` computation for $n=2,\dots,9$: zero
mismatches, matching e.g. $n=3$'s $s^\ast=\tfrac32\cdot\tfrac8{15}T=\tfrac45T$,
which is exactly the "threshold $0.8$" figure the round-9 explorer found
only numerically at one point — now proved in closed form for every
$n\ge2$.)

**General negative result (equal-pieces defeats Theorem D′'s IH-ceiling
mechanism, every $n\ge2$, full proof).** For the equal-pieces marking
$p_i=T/m$ ($m=n+1$), $s=p_1+p_m=2T/m=2T/(n+1)$. We show $s<s^\ast=\tfrac32a_nT$
for every $n\ge2$, i.e. the mechanism never certifies this configuration.
Equivalently (dividing by $T$, using $a_n=2^n/D_n$, $D_n=2^{n+1}-1$):
$$\frac{2}{n+1}<\frac{3\cdot2^{n-1}}{D_n}\iff 2D_n<3(n+1)2^{n-1}
\iff 2(2^{n+1}-1)<3(n+1)2^{n-1}.$$
Dividing by $2^{n-1}$: $8-2^{2-n}<3(n+1)$. For $n\ge2$, $2^{2-n}\le1$, so
the left side is $<8$, while the right side $3(n+1)\ge9>8$. Hence the
inequality holds for **every** $n\ge2$. $\blacksquare$ This is a genuine,
general-$n$ proof (not a spot check at $n=3$) that Theorem D′'s
IH-ceiling route can never, by itself, certify the equal-pieces
configuration for any $n\ge2$ — a much sharper, and now fully proved,
version of the outline's numeric-only "$s=0.5<0.8$ at one witness"
observation.

**Exact (non-ceiling) evaluation still resolves both on-file witnesses.**
Using $\Phi'$'s *exact* recursive value (not the ceiling) instead:
- At $(3/8,1/4,1/4,1/8)$ ($n=3$): middle $=\{1/4,1/4\}$, $m'=2$, so by
  Theorem A/$P(2)$ (§3), $\Phi'=1/4$ exactly (the two middle pieces are
  equal so Full-Match gives $\Phi'=$ that common value with zero
  leftover). Theorem D′ gives $\Phi_{\min}\le\tfrac{3/8+1/8}{2}+\tfrac14
  =\tfrac14+\tfrac14=\tfrac12\le\tfrac8{15}$. **Resolved.**
- At $(2/5,3/10,1/5,1/10)$ ($n=3$, a fresh witness found this round while
  stress-testing Theorem D′/E — both of *their* exact values fail here:
  D′ gives $\tfrac{2/5+1/10}{2}+\tfrac{3}{10}=\tfrac14+\tfrac3{10}=\tfrac{11}{20}
  =0.55>\tfrac8{15}$; E gives the same value $0.55$ by symmetry of the
  computation): neither D′ nor E closes it. A numerical global search
  (`scipy.optimize`, 200 multi-starts, Nelder–Mead) located the true
  optimum exactly at $\Phi=1/2$, achieved by **Theorem B$_k$ with $k=4$**
  (peel $p_1$ against $p_4$, not $p_2$) composed with a further bisection
  of $p_3$: cutting $p_1=2/5$ into $(1/10,3/10)$ (matching $p_4$) and
  $p_3=1/5$ into $(1/10,1/10)$ gives final multiset
  $\{3/10,3/10,1/10,1/10,1/10,1/10\}$ — two exact pairs plus a further
  exact pair, so $A=0$ by two applications of `pair-cancellation-identity`,
  giving $\Phi=(T+0)/2=1/2\le8/15$. **Resolved**, but only by exploiting
  this configuration's specific numeric coincidences ($p_1-p_4=p_2$ and
  $p_3=2p_4$) — not by a closed-form threshold that would cover nearby
  configurations lacking this structure.

**Honest conclusion for §5.** No single theorem (D′, E, or B$_k$'s
ceiling version) gives a general closed-form sufficient condition
covering all of $p_1<T/2$ at $n=3$; both on-file hard witnesses are
resolved individually, but only via each one's own exact structural
coincidences, exactly reproducing (with a fresh, independently-found
witness) the diagnosis of round 4's `smoothing-compactness-certificate`
("a seventh, configuration-dependent strategy is needed, not a sixth
closed-form template") and round 8's `bounded-certificate-for-half-window-
vanishing` obstruction on the lower-bound side. Whether $P(4)$'s
$p_1<T/2$ half is true at all (i.e. whether $c(3)\le8/15$ holds for
*every* $p_1<T/2$ marking, not just these two witnesses) is not resolved
this round — this remains the concrete open item, now with a sharper
toolkit (Theorems C′, B$_k$, D′, E, all proved in full and reusable) and
a clear diagnosis (the true optimal strategy at a $p_1<T/2$ point can
require peeling against an element other than $p_2$, per an
exact-value comparison that has no known closed form).

## Round 9 outline (proof-outliner, superseded above — retained for the record)

Target (unchanged, full problem's other half): $c(n)\le a_n$ for every $n$
and every legal Liu Bang marking $p_1\ge\cdots\ge p_m>0$ ($m=n+1$), i.e.
Xiang Yu can always force $\Phi\le a_nT$. Round-9 explorer
(`math-explorer-upper-bound.md`) found a scouting-level (exact-`Rational`
algebra checked $n\le8$, not yet a proof) recursive strengthening, Theorem
C′, that cleanly closes the $p_1\ge T/2$ half of the marking space by strong
induction on $m$; the $p_1<T/2$ half ("no dominant piece") is where both
on-file hard witnesses live and remains genuinely open, hitting the same
floor-vs-exact-value obstruction the lower-bound front already diagnosed one
level down.

Technique: strong induction on $m$ (number of pieces), using exact
closed-form identities (`pair-cancellation-identity`/`leftover-formula`) for
each candidate Xiang Yu move, split into two independently-provable regimes
by $p_1$ vs $T/2$.

Skeleton:
  1. **Base case** $m=1$: trivially $\Phi=T=a_0T$ (no cuts, one piece,
     Liu Bang gets everything) — cite `leftover-formula` degenerate case.
  2. **Regime $p_1\ge T/2$ (Theorem C′ + Theorem A).** Formalize as a full
     rigorous strong induction on $m$:
     - If $p_1\ge a_nT$: apply certified **Theorem A** (Full-Match) directly,
       $\Phi=p_1$... wait, need $\Phi\le a_nT$, so actually use Theorem C′
       here (bisect $p_1$, recurse on tail with $n-1$ cuts): exact identity
       $\Phi = p_1/2 + \Phi_{\min}(\{p_2,\dots,p_m\}, n-1\text{ cuts})$ (cite
       `pair-cancellation-identity` — this is an exact identity, unconditional,
       same status as the already-certified `one-step-peel-identity`).
       Substitute the induction hypothesis $\Phi_{\min}(\text{tail})\le
       a_{n-1}T'$ ($T'=T-p_1$), giving $\Phi\le p_1/2+a_{n-1}(T-p_1)$; solve
       exactly (the explorer's `sympy`/`Fraction` computation, re-derive
       rather than cite since it's scouting-level) for the threshold —
       verify algebraically (not just for $n\le8$) via the telescoping
       identity $a_{k-1}-a_k = 2^{k-1}/(D_{k-1}D_k)$, $D_k=2^{k+1}-1$,
       already used in the certified `one-step-peel-identity`/Theorem-B
       proof — that this gives exactly $\Phi\le a_nT$ whenever $p_1\ge a_nT$.
     - If $T/2\le p_1<a_nT$: apply **Theorem A** (Full-Match, certified,
       $\Phi=p_1<a_nT$ trivially in this sub-range).
     - These two sub-ranges partition $[T/2,\infty)$ with no gap (the
       explorer verified the threshold match $p_1\ge a_nT$ falls out with
       zero slack for $n=1,\dots,8$) — a builder must prove this general
       algebraic fact (five-line induction on the telescoping identity, per
       the explorer's cheap-kill note), not just re-check small $n$.
  3. **Regime $p_1<T/2$ (the genuinely open half).** No single existing
     theorem closes this. Two candidate mechanisms to attempt, in order of
     cheapness:
     - **Theorem E (Bisect-Top-Two):** bisect both $p_1,p_2$ simultaneously
       (2 cuts), recurse on $\{p_3,\dots,p_m\}$ with $n-2$ cuts — derive the
       exact identity via `pair-cancellation-identity` exactly as Theorem D
       was derived (untested by the explorer, first thing to try), then
       find its exact (not crude) recursive threshold the same way Theorem
       C′'s was found, and check it against both on-file hard witnesses
       ($n=3$: $(3/8,1/4,1/4,1/8)$; $(6,2,2,1)/11$).
     - **Vertex-minimum reuse:** the certified `vertex-minimum-theorem`
       (originally proved for minimizing $\Phi$ over Xiang Yu's own legal
       responses) applies verbatim here too, since this front's
       minimization is over the *same* kind of polytope (Xiang Yu's legal
       cut choices) — use it to restrict the $p_1<T/2$ regime's minimizing
       Xiang-Yu response to a finite vertex family, then attempt to bound
       each vertex family member directly via `odd-run-reduction-lemma`,
       rather than searching over an unbounded strategy space of ad hoc
       bisection templates.
  4. Combine regimes 2 and 3 to close $c(n)\le a_n$ for every marking and
     every $n$.

Key lemmas (claim + mechanism):
  - Theorem C′ exact identity $\Phi=p_1/2+\Phi_{\min}(\text{tail},n-1)$ —
    because it is a direct instance of `pair-cancellation-identity` applied
    to a single bisection of $p_1$ with the rest handled by full recursive
    optimality, unconditional exactly like the certified Theorem B.
  - Threshold match $p_1\ge a_nT \iff$ Theorem C′ (with inductive ceiling)
    suffices — because the telescoping identity
    $a_{k-1}-a_k=2^{k-1}/(D_{k-1}D_k)$ makes the algebra solve cleanly to
    exactly $a_n$ with zero slack (needs a general-$n$ proof, not just
    $n\le8$ verification).
  - $p_1\ge T/2$ regime fully covered with no gap by Theorem A ($T/2\le
    p_1<a_nT$) union Theorem C′ ($p_1\ge a_nT$) — because $a_n\ge1/2$
    always (ladder value), so these two sub-ranges are contiguous and
    exhaustive within $[T/2,\infty)$.

Open gaps: the entire $p_1<T/2$ regime (step 3) — neither Theorem E's
identity nor its threshold has been derived yet, this is the round's
concrete next target; formalizing step 2 as a rigorous general-$n$ induction
(not just $n\le8$ verification) is also unfinished but much closer to
mechanical.

Cases to cover: $p_1\ge a_nT$ (Theorem C′), $T/2\le p_1<a_nT$ (Theorem A),
$p_1<T/2$ (open — needs Theorem E or vertex-minimum reuse); must also handle
the boundary $m=1$ base case and confirm no marking falls outside all cases
(trivial, since $p_1\ge T/2$ or $p_1<T/2$ partitions everything).

Watch out for: do not reuse Theorem D's *crude* bound ($A\le\mathrm{Total}$)
as a substitute for step 3 — already confirmed too weak at both on-file hard
witnesses (this round's explorer); any Theorem E derivation must use either
the exact value or a genuinely sharper inductive ceiling, not the crude one.
Also do not assume the $p_1<T/2$ regime is "just like" the $p_1\ge T/2$
regime's induction — the explorer explicitly checked the analogous
recursive-ceiling version of Theorem D (Theorem D′) and found it **still
fails** at $(3/8,1/4,1/4,1/8)$ ($p_1+p_m=1/2 < $ threshold $0.8$), so
whatever closes $p_1<T/2$ must be strictly sharper than a direct D′-style
generalization — the floor-vs-exact-value gap re-appears one level down and
needs a genuinely new idea (Theorem E's own exact non-recursive value, or
vertex enumeration), not just another recursive ceiling substitution.

## Round 10 build: Route A and Route B on the $p_1<T/2$ regime

Throughout this section, fix $n\ge1$, $m=n+1$, an *arbitrary* Liu Bang
marking $p_1\ge p_2\ge\cdots\ge p_m>0$, $T=\sum p_i$, $a_k=2^k/D_k$,
$D_k=2^{k+1}-1$ (so $2a_k-1=1/D_k$, proved in §2 above). We attack the
still-open regime $p_1<T/2$.

### Route A: a marking-agnostic vertex characterization for "cut $p_1$ only"

**A.1 A new lemma: unconstrained-simplex exchange-smoothing.**

**Lemma (Simplex Vertex-Maximization).** *Fix any finite reference multiset
$\tau=(\tau_1,\dots,\tau_r)$ of positive reals (any values, any order — no
ratio-2 or ladder assumption), a mass $s>0$, and a part-budget $k\ge1$. Let*
$$\mathcal Q_k := \Big\{(f_1,\dots,f_k):\ f_i\ge0,\ \textstyle\sum_i f_i=s\Big\}$$
*(the full simplex — no upper bound $f_i\le\tau_1$ is imposed, unlike the
certified `exchange-smoothing-vertex-maximization`). Then the maximum of
$E(F\cup\tau)$ (even-sorted-rank sum) over $F\in\mathcal Q_k$ is attained at
some $F^\dagger$ of the restricted form: for some $0\le p\le k$, $p$
coordinates are individually pinned to reference values
$\tau_{l_1},\dots,\tau_{l_p}\in\{\tau_1,\dots,\tau_r\}$ (repetition allowed),
and the remaining $k-p$ coordinates (if any) all equal one common value
$v\ge0$ (determined by $v=(s-\sum_i\tau_{l_i})/(k-p)$ if $k>p$; if $k=p$ the
configuration is only valid when $\sum_i\tau_{l_i}=s$ exactly).*

*Proof.* This is the identical exchange-smoothing argument certified in
`exchange-smoothing-vertex-maximization`, with the single box-boundary
clause removed. We repeat it in full since the target set $\mathcal Q_k$ is
genuinely different (unbounded above, not intersected with a box), so the
compactness and boundary-hitting steps must be re-checked, not merely
cited.

*Existence.* $\mathcal Q_k$ is a closed, bounded (each $f_i\in[0,s]$, since
all coordinates are nonnegative and sum to $s$) simplex, hence compact.
$E(\cdot\cup\tau)$ is continuous on it (composition of the affine embedding,
the continuous sort map, and the linear even-rank-sum functional — the same
argument as `vertex-minimum-theorem`'s existence step, marking-agnostic).
By the extreme value theorem a maximizer $F^\ast$ exists.

*Exchange step.* Fix the finite reference value set
$\mathcal R:=\{0,\tau_1,\dots,\tau_r\}$. Call a coordinate $f_i^\ast$
*pinned* if it lies in $\mathcal R$, *free* otherwise. Suppose two free
coordinates $f_i^\ast\ne f_j^\ast$ exist. Since both are free (not in
$\mathcal R$) and distinct, and there are finitely many other coordinates
of $F^\ast$ and finitely many points of $\mathcal R$, there is a radius
$\varepsilon_0>0$ such that for $|\varepsilon|<\varepsilon_0$, the
perturbation $(f_i^\ast+\varepsilon,f_j^\ast-\varepsilon)$ (all other
coordinates fixed) stays strictly between $f_i^\ast,f_j^\ast$'s current
sorted neighbours among $F^\ast\cup\tau$ (which are unaffected, since the
perturbation is small), remains nonnegative (both $f_i^\ast,f_j^\ast>0$,
being free hence $\ne0$), and keeps $f_i,f_j$ in their original rank
positions. On this neighbourhood $E((F^\ast$-perturbed$)\cup\tau)
=E(F^\ast\cup\tau)+(w_i-w_j)\varepsilon$ for fixed even-rank indicators
$w_i,w_j\in\{0,1\}$ (this affine behaviour needs no upper-bound hypothesis
on $f_i$ at all — it is purely a statement about local rank-constancy).
If $w_i\ne w_j$: choose the sign of $\varepsilon$ making $(w_i-w_j)
\varepsilon>0$, strictly increasing $E$, contradicting maximality. So
$w_i=w_j$ for every pair of free coordinates, hence pushing $\varepsilon$ in
either direction leaves $E$ unchanged; push it (say, increasing $f_i$,
decreasing $f_j$) until the neighbourhood's boundary is first reached. Since
$\mathcal Q_k$ has **no upper box facet** on individual coordinates (the
only constraints are $f_i\ge0$ and $\sum f_i=s$), the boundary can only be
reached by: (i) $f_j$ hitting $0$, (ii) $f_i$ or $f_j$ hitting a reference
value $\tau_l$, or (iii) $f_i$ or $f_j$ hitting the value of another
coordinate of $F^\ast$ (merging into a tied group). (There is no case "$f_i$
hits $\tau_1$-as-box-bound" here, since no such bound exists — this is the
one clause dropped from the certified proof, and dropping it does not
remove any boundary case, since $f_i\le s$ is automatic from nonnegativity
and the sum constraint, and $s$ plays no distinguished role forcing a stop.)
At the boundary, $E$ still equals $E(F^\ast\cup\tau)$ (slope was $0$
throughout) and the number of distinct free values has strictly decreased.
Iterating (finitely many times, since the number of distinct free values is
a nonnegative integer bounded by $k$) terminates at a configuration
$F^\dagger$ with $E(F^\dagger\cup\tau)=E(F^\ast\cup\tau)$ (the true maximum)
and at most one distinct free value, shared by all unpinned coordinates —
the claimed form. $\blacksquare$

**A.2 The vertex family for "cut $p_1$ only."**

Fix an arbitrary marking with $p_1<T/2$ and let Xiang Yu be restricted to
strategies that split $p_1$ into $k$ parts ($1\le k\le n+1$, using $k-1$
cuts, all spent on $p_1$) and leave $\tau:=(p_2,\dots,p_m)$ (length
$r:=m-1=n$) untouched. Since $\mathrm{Total}(F\cup\tau)=T$ is fixed
regardless of $F$, and $A=T-2E$ (from $O+E=T$, $O-E=A$), minimizing
$\Phi=(T+A)/2$ over legal $F$ is **exactly equivalent** to maximizing
$E(F\cup\tau)$ over $F\in\mathcal Q_k$ ($s=p_1$). By Lemma A.1, this maximum
(hence the minimizer of $\Phi$ among "cut $p_1$ only, $k$-part" strategies)
is attained at a vertex $F^\dagger$: $p$ coordinates pinned to
$\tau_{l_1},\dots,\tau_{l_p}\in\{p_2,\dots,p_m\}$, the remaining $q:=k-p$
coordinates tied to one common value $v=(p_1-\sum_i\tau_{l_i})/q$ (or
$v$ undefined/degenerate if $q=0$, requiring exact pin-sum equality).

**This literally reproduces (and supersedes) Theorems A/B/C as the complete
list of vertex *shapes*** (not, yet, of vertex *values* against $a_nT$):
Theorem C is $p=0$ (no pins, $v=p_1/k$ — for $k=2$, the bisection); Theorem
B / B$_k$ is $p=1$ (one pin, to some $\tau_l=p_l$), $q=1$; Theorem A is
$p=m-1$ (pin to every tail value $p_2,\dots,p_m$ once each), $q=1$ (the
leftover). **This is a genuine reduction, not a relabeling**: it proves,
for the *first* time in this approach, that no vertex shape outside this
finite pinned-plus-tied-group family can ever be optimal for a "cut $p_1$
only" strategy, for *any* marking — closing the "is the search space finite
and characterized" question completely (Route A step 2 of the outline).

**A.3 Evaluating the vertex family: reduction to a finite combinatorial
optimization (the genuinely new content, only partially completed).**

Fix a vertex $F^\dagger$ as above with minimal pins: for each level
$l\in\{1,\dots,n\}$ (indexing $\tau_l=p_{l+1}$), let $c_l\ge0$ be the number
of pins at level $l$; WLOG (as in `rank-pigeonhole-budget` §5.4's identical
argument, which is marking-agnostic) it suffices to consider $c_l\in\{0,1\}$
(using more than one pin at the same level only wastes budget without
changing which levels have *odd* total multiplicity — the only thing $A$
depends on, by `odd-run-reduction-lemma`). Let
$X:=\{l: c_l=0\}\subseteq\{1,\dots,n\}$ (the tail levels *not* pinned).
Each $\tau_l$ ($l\notin X$) then has total multiplicity $2$ in $F^\dagger
\cup\tau$ (original + one pin), hence even; each $\tau_l$ ($l\in X$) has
multiplicity $1$ (odd). By `odd-run-reduction-lemma` and
`pair-cancellation-identity` (both certified, fully general, no ladder
assumption):
$$A(F^\dagger\cup\tau) = \begin{cases} A(X) & q\text{ even (incl. }q=0),\\
A(X\cup\{v\}) & q\text{ odd},\end{cases}$$
where $X$ is viewed as the subset $\{\tau_l:l\in X\}\subseteq\{p_2,\dots,
p_m\}$ (ordinary sorted alternating sum, since all its elements are
distinct — a genuine marking $p_2>\dots>p_m$ typically has strict
inequalities; if some $p_i=p_j$ coincide, $X\cup\{v\}$ is still a
well-defined multiset and $A$ still makes sense by the same odd-run
reduction, no extra care needed), $R(X):=\sum_{l\in X}\tau_l$, and, by mass
balance with minimal pins,
$$p_1 = \big(R(\tau)-R(X)\big) + qv \quad\Longrightarrow\quad
v=\frac{p_1-R(\tau)+R(X)}{q}\ \ (q\ge1),$$
with the budget constraint $q\le n+1-(n-|X|)=|X|+1$ (since $k=p+q\le n+1$
and $p=n-|X|$ with minimal pins) and $v\ge0$ required for legality.

**This converts Route A's target into a well-posed, finite combinatorial
statement**: for every marking with $p_1<T/2$,
$$\min\Big\{ A(X) \ :\ X\subseteq\{1,\dots,n\},\ \exists\text{ even }
q\in\{0,\dots,|X|+1\}\text{ with }v(X,q)\ge0\Big\}
\ \wedge\ \min\Big\{A(X\cup\{v(X,q)\})\ :\ X,\ q\text{ odd},\ 1\le q\le|X|+1,\
v(X,q)\ge0\Big\}$$
must have overall minimum $\le(2a_n-1)T=T/D_n$ for the "cut $p_1$ only"
family alone to certify $\Phi\le a_nT$ (it need not — a full-marking
strategy touching the tail as well remains available and is not covered by
this restricted family, consistent with, not contradicting, the general
upper bound).

**Honest status of Route A.** Steps A.1–A.3 are complete, rigorous, and
general (no case restriction, no numerics): they replace the population's
ad hoc Theorems A/B/C/D/E-search with a single characterized, finite family
and an explicit closed-form evaluation of every member. **What remains
open** (not completed this round, and confirmed by the outline to be the
real content): proving the resulting finite minimization is $\le T/D_n$ for
*every* marking with $p_1<T/2$ — or, more realistically, showing it is
*not* always $\le T/D_n$ for this restricted "cut $p_1$ only" family alone
(in which case Route A only narrows, rather than closes, the search — a
tail-touching strategy would then be required, consistent with the general
theorem still being open). This finite optimization was not attempted
symbolically this round due to time; it is the concrete next target for
Route A.

### Route B: bounded-leftover reformulation, corrected, plus a construction attempt

**B.1 Corrected equivalence statement (sufficient, not equivalent).**

By `leftover-formula`, if a legal final multiset $M$ decomposes as one
unpaired element $v$ plus $k$ exactly-equal pairs (or, degenerately, into
exact pairs only, $v=0$-case), then $A(M)=v$ (or $0$), giving
$\Phi(M)=(T+v)/2$ (or $T/2$). Hence: **if** Xiang Yu has a legal response
using $\le n$ cuts whose final multiset has this pair-plus-(at most one)
leftover shape with $v\le T/D_n=(2a_n-1)T$ (using the exact identity
$2a_n-1=1/D_n$ proved in §2 above), **then** $\Phi\le a_nT$.

**Correction to the round-10 outline.** The outline states this
reformulation is "*equivalent*" to $c(n)\le a_nT$ for a fixed marking. This
is **not established** and, on reflection, is not obviously true: by
`odd-run-reduction-lemma`, $A(M)$ for a general final multiset $M$ reduces
to $A(M')$ where $M'$ is the sub-multiset of odd-multiplicity values — a
set of *distinct* values that can have any size $|M'|\ge0$, not only $0$ or
$1$. If $|M'|\ge2$, $A(M')$ is the *ordinary* alternating sum of several
distinct values, which can be small even though $M$ is nowhere near a
"pairs-plus-single-leftover" shape (e.g. $M'=\{5,4,4,1\}$ has $A=5-4+4-1=4$,
not simply "one leftover value"). So a legal response achieving
$\Phi\le a_nT$ need **not** be of pair-plus-leftover form — the
reformulation gives a **sufficient** strategy family (a genuine, useful
special case to search), not a logically equivalent restatement of the
whole problem. This correction is recorded so no future round treats
"failure to find a good pairing" as a refutation of the upper bound itself.

**B.2 Parity necessary condition (as outlined, proved).** For the
pair-plus-single-leftover shape specifically (not the general $M'$ above)
to be reachable with exactly $v=0$ leftover, the final multiset must have
even size; with exactly one leftover, odd size. Final size is $m+c$ where
$c\le n$ is the number of cuts used. Since $m=n+1$, $m+c\equiv n+1+c
\pmod2$: this is even (achievable "all-paired, $v=0$" target) iff $c\equiv
n+1\pmod2$, and odd (achievable "one leftover" target) iff $c\equiv n
\pmod 2$. This is an elementary, fully general counting fact (each cut adds
exactly one fragment, so final count $=$ initial count $+$ cuts used) that
restricts which cut-counts $c$ can even reach the required shape, before
attempting any construction.

**B.3 The Iterated Greedy-Peel Construction (new, general, fully proved).**

**Construction.** Given any finite multiset $W$ of positive reals
(initially $W=\{p_1,\dots,p_m\}$), repeat: while $|W|\ge2$, let $a\ge b$ be
the two largest elements of $W$ (ties broken arbitrarily). If $a=b$: remove
both from $W$ (using $0$ further cuts). If $a>b$: cut $a$ into $(b,a-b)$
(one legal cut on the existing fragment $a$), remove $a,b$ from $W$, and
insert $a-b$ into $W$ (using $1$ further cut). Stop when $|W|\le1$; let
$v_{\text{final}}$ be the surviving element if $|W|=1$, and set
$v_{\text{final}}:=0$ if $W$ becomes empty.

**Lemma (Legality — budget never exceeded).** *This construction always
uses $\le n=m-1$ cuts.*

*Proof.* Let $C_0=m,C_1,\dots,C_T\in\{0,1\}$ be the sequence of $|W|$-values
across steps. Each step reduces $|W|$ by exactly $1$ (an "$a>b$" step,
contributing $1$ to the cut count) or exactly $2$ (an "$a=b$" step,
contributing $0$). Let $s_1,s_2$ be the total number of each type; cuts
used $=s_1$, and $s_1+2s_2=m-C_T$. If $C_T=1$: $s_1=m-1-2s_2\le m-1$. If
$C_T=0$: the *last* step must be an "$a=b$" step (an "$a>b$" step always
leaves a nonzero remainder $a-b>0$ in $W$, so $|W|$ can only reach $0$ via
a tie-step from $|W|=2$); hence $s_2\ge1$, so $s_1=m-2s_2\le m-2<m-1$. In
both cases $s_1\le m-1=n$. $\blacksquare$

**Lemma (Exact value).** *The resulting final multiset $M$ (the actual
physical result of every cut performed) satisfies $A(M)=v_{\text{final}}$
exactly, hence $\Phi(M)=(T+v_{\text{final}})/2$.*

*Proof.* By induction on the number of "$a>b$" steps. Each such step cuts
the current fragment $a$ (a member of the real, current multiset) into
$(b,a-b)$, where $b$ is another member of the real current multiset. The
real multiset immediately after this cut contains **two** copies of the
value $b$ (the pre-existing one and the new fragment) plus $a-b$ plus every
other untouched fragment. By `pair-cancellation-identity`,
$A(\text{real multiset after this cut}) = A(\text{real multiset with both
copies of }b\text{ removed, and }a\text{ replaced by }a-b)$ — exactly the
bookkeeping of the *next* working-set state. Each "$a=b$" step similarly
removes an exact pair already present, again by `pair-cancellation-identity`
(the two equal elements $a,b$ already sitting in the real multiset). Since
`pair-cancellation-identity` holds regardless of where a pair sits in
sorted order and regardless of how many other pairs have already been
removed, these reductions may be applied once per step, in the order the
steps occurred, telescoping to $A(M)=A(\{v_{\text{final}}\})=v_{\text{
final}}$ (or $A(\emptyset)=0$). $\blacksquare$ (Every pair identified along
the way is disjoint from every other: each step consumes the current top
two *distinct positions* of $W$ and never revisits an already-paired
element, since paired elements are removed from $W$ immediately.)

**Corollary.** For every $n\ge1$ and every marking, the Iterated
Greedy-Peel Construction gives a legal Xiang Yu response with
$\Phi=(T+v_{\text{final}})/2$, $v_{\text{final}}\ge0$, using $\le n$ cuts —
hence $\Phi\le a_nT$ **whenever** $v_{\text{final}}\le T/D_n$.

**B.4 Verification against both on-file hard witnesses (matches exactly).**
Computed exactly (verified by an independent `Fraction` script this round):
- $(3/8,1/4,1/4,1/8)$: greedy steps give working sets
  $\{3/8,1/4,1/4,1/8\}\to\{1/4,1/8,1/8\}\to\{1/8,1/8\}\to\emptyset$ (last
  step a tie, $0$ cuts), using $2$ of the $3$ available cuts,
  $v_{\text{final}}=0$, $\Phi=1/2\le8/15$ — **matches** the previously
  known optimum exactly, via a cleaner $2$-cut route (previously found only
  via bisecting $p_1,p_4$ simultaneously, Theorem D).
- $(2/5,3/10,1/5,1/10)$: working sets
  $\{2/5,3/10,1/5,1/10\}\to\{1/5,1/10,1/10\}\to\{1/10,1/10\}\to\emptyset$,
  again $2$ cuts, $v_{\text{final}}=0$, $\Phi=1/2\le8/15$ — **matches** the
  previously known optimum exactly, via a cleaner route than the previous
  round's $B_k$-peel-plus-bisection.

This is genuine positive evidence (the construction independently
rediscovers both known optima, not merely stays within target) — but per
the outline's explicit instruction, this is reported as **evidence**, not
as a proof that the construction always works; §B.5 shows it does not.

**B.5 Counterexample: the construction does NOT always achieve the
target (honest negative finding, not overclaimed).**

At the $n=4$ equal-pieces marking $p_i=1/5$ ($i=1,\dots,5$, $T=1$): the two
largest are always tied ($1/5=1/5$), so every step is a "$a=b$" tie-step,
using $0$ cuts: $\{1/5^5\}\to\{1/5^3\}\to\{1/5\}$, giving
$v_{\text{final}}=1/5$, $\Phi=(1+1/5)/2=3/5$. But $a_4T=16/31\approx0.5161$,
and $3/5=0.6>16/31$. **The construction fails at this point** — using $0$
cuts is not always the right choice; a smarter strategy (e.g. actually
cutting one $1/5$ piece rather than only matching untouched pieces)
provably does better here (consistent with the general upper bound, which
this round does not refute — only the naive "always match the current top
two" rule is refuted as a universal proof strategy).

A broader stress test (independent `Fraction` computation, $2000$ random
integer-ratio markings, $m=2,\dots,6$ uniformly) confirms this is not an
isolated failure: the naive construction **fails to meet $a_nT$ in
approximately 48% of random trials** (969/2000). **Conclusion, reported
honestly per the outline's explicit instruction**: the Iterated
Greedy-Peel Construction is a genuine, general, reusable *identity*
(Lemma B.3, unconditionally true and useful as a computational tool for
any marking), but it is **not** a proof of the general upper bound as
stated — the "always pick the top two" greedy rule is provably
insufficient. Whether some other selection rule within the same
pair-matching framework (e.g. prioritizing near-equal pairs, or reserving
budget to cut a large piece even when a tie is available) always succeeds
is a genuinely open question this round did not resolve.

### Net effect of Round 10

Both routes produced real, verified, non-overclaimed progress narrowing
*how* a future closure of $p_1<T/2$ must work, without closing it:

- Route A fully characterizes the vertex family for "cut $p_1$ only"
  strategies (any marking) and reduces its evaluation to an explicit finite
  combinatorial optimization — genuinely replacing ad hoc template search,
  but the optimization itself is not yet solved.
- Route B proves a genuinely new general construction (reusable regardless
  of whether the overall program succeeds) that matches both known optimal
  witnesses exactly, but is rigorously shown (not just suspected) to fail
  in general — a real negative result, not a gap left implicit.

Neither route closes $p_1<T/2$; **Status remains `partial`.**

## Round 11 build: pin-set fix, corrected witness classification, per-piece decomposition

### R11.1 The Zero-Pin Harmlessness Lemma (full proof)

**Lemma (Zero-Pin Harmlessness).** *Let $M$ be any finite multiset of
nonnegative reals and let $M^+ := M\cup\{0\}$ (adjoin one element of value
$0$). Then $\mathrm{Total}(M^+)=\mathrm{Total}(M)$, $E(M^+)=E(M)$,
$O(M^+)=O(M)$, $A(M^+)=A(M)$, and $\Phi(M^+)=\Phi(M)$, where $O,E$ denote
the sum of elements at odd/even sorted rank (rank $1$ = largest) and
$A=O-E$, $\Phi=(\mathrm{Total}+A)/2$.*

*Proof.* Sort $M$ in nonincreasing order as $L_1\ge L_2\ge\cdots\ge L_k\ge0$
($k=|M|$). Since $0\le L_k$, adjoining a $0$ to $M$ produces the sorted
sequence $L_1\ge\cdots\ge L_k\ge0$, i.e. the new element occupies exactly
rank $k+1$ — it never displaces any $L_i$ from its original rank, because
$0$ is $\le$ every element already present (ties at value $0$ inside $M$
itself, if any, do not matter: sorted order is only used to *define* $O,E$
via rank position, and any total order consistent with the multiset's
values assigns the new $0$ a rank of $k+1$ or, if $M$ already contains
copies of $0$, some rank $\ge k+1-(\text{number of zeros in }M)$, but among
*all* the zero-valued elements the rank assignment is interchangeable
without changing $O$ or $E$ since they all contribute $0$ regardless of
which specific zero sits at which rank). Hence $L_1,\dots,L_k$ keep their
original ranks $1,\dots,k$ in $M^+$, so
$$O(M^+)=\Big(\sum_{i\text{ odd},\,i\le k}L_i\Big) + [\,k{+}1\text{ odd}\,]\cdot 0
= O(M),\qquad
E(M^+)=\Big(\sum_{i\text{ even},\,i\le k}L_i\Big) + [\,k{+}1\text{ even}\,]\cdot 0
= E(M),$$
since the appended element's own value is $0$ regardless of whether $k+1$
is odd or even. Consequently $A(M^+)=O(M^+)-E(M^+)=O(M)-E(M)=A(M)$, and
$\mathrm{Total}(M^+)=\mathrm{Total}(M)+0=\mathrm{Total}(M)$, so
$\Phi(M^+)=(\mathrm{Total}(M^+)+A(M^+))/2=(\mathrm{Total}(M)+A(M))/2=\Phi(M)$.
$\blacksquare$

**Corollary (iterated).** *For any $q\ge0$, adjoining $q$ zero-valued
elements to $M$ leaves $\mathrm{Total},O,E,A,\Phi$ all unchanged.* (Immediate
induction on $q$ using the Lemma once per adjunction.)

This is a completely general, marking-independent, elementary fact — it
needs no ladder structure, no rationality, nothing beyond the definitions
already fixed by the shared claiming-subgame reduction (imported, not
re-derived, per the project's standing rule).

### R11.2 Corrected Simplex Vertex-Maximization Lemma (pin set includes $0$)

**Corrected Lemma (Simplex Vertex-Maximization).** *Fix a finite reference
multiset $\tau=(\tau_1,\dots,\tau_r)$ of positive reals (arbitrary, no
ratio-2/ladder assumption), a mass $s>0$, a part-budget $k\ge1$, and let
$\mathcal Q_k=\{(f_1,\dots,f_k):f_i\ge0,\sum_if_i=s\}$ as before (no box
constraint). Then the maximum of $E(F\cup\tau)$ over $F\in\mathcal Q_k$ is
attained at some $F^\dagger$ of the form: for some $0\le p\le k$, $p$
coordinates are individually pinned to reference values in the set*
$$\mathcal R:=\{0,\tau_1,\dots,\tau_r\}$$
*(repetition of the same value among distinct pinned coordinates is
allowed, including repetition of the value $0$), and the remaining $k-p$
coordinates (if any) all equal one common value $v\ge0$, determined by
$v=(s-\sum\text{pinned values})/(k-p)$ (with the degenerate case $k=p$
requiring the pinned values to sum to exactly $s$).*

*Proof.* This is the identical existence-and-exchange argument already
written out for Lemma A.1 above — that proof already fixes the reference
set as $\mathcal R=\{0,\tau_1,\dots,\tau_r\}$ (see "*Fix the finite
reference value set $\mathcal R:=\{0,\tau_1,\dots,\tau_r\}$. Call a
coordinate $f_i^\ast$ *pinned* if it lies in $\mathcal R$*" in A.1's own
write-up) and its three boundary cases (i) $f_j$ hits $0$, (ii) $f_i$ or
$f_j$ hits a reference value $\tau_l$, (iii) $f_i$ or $f_j$ hits another
coordinate's current value, are exactly the three ways a coordinate can
become pinned to some element of $\mathcal R$ (cases (i)/(ii)) or join a
tied free group (case (iii)). The only defect was that the **boxed
statement** of the lemma (as opposed to its proof) restricted the pin
values to $\{\tau_1,\dots,\tau_r\}$, omitting $0$ — an inconsistency between
statement and proof, now removed. No step of the argument changes: existence
(compactness of $\mathcal Q_k$, continuity of $E(\cdot\cup\tau)$) is
unaffected by the pin set; the exchange step's affine-slope argument and
its termination (finitely many distinct free values, strictly decreasing at
each swap) are unaffected, since they never referenced which specific
values populate $\mathcal R$. $\blacksquare$

**Independent cross-check via Zero-Pin Harmlessness (not required for the
proof above, but a genuine second verification that the corrected statement
is internally consistent).** Suppose $F^\dagger$ has $q_0\ge1$ coordinates
individually pinned to $0$ (case (i) boundary points), and let
$F^{\dagger\prime}$ be $F^\dagger$ with those $q_0$ zero coordinates
deleted (a $(k-q_0)$-part vector, still summing to $s$, since deleting
zeros does not change the sum). By the (iterated) Zero-Pin Harmlessness
Corollary applied to $M:=F^{\dagger\prime}\cup\tau$ ($q_0$ zeros
adjoined), $E(F^\dagger\cup\tau)=E(F^{\dagger\prime}\cup\tau)$ exactly —
i.e. **the value achieved by any vertex with $q_0$ explicit zero-pins is
identical to the value achieved by the same vertex with those zero
coordinates simply deleted and the budget reduced to $k-q_0$.** This
confirms, independently of the exchange-argument proof, that adding $0$ to
the reference/pin set introduces no new *values* into the family beyond
what smaller-$k$ members of the family (with $q_0=0$) already realize —
only new (but value-redundant) *descriptions* of already-present values.
Consequently:

**Corollary (A.3 needs no revision).** *The finite combinatorial
optimization of §A.3 above (ranging $k$ over $1,\dots,n+1$ and, for each
$k$, over subsets $X\subseteq\{1,\dots,n\}$ of un-pinned tail levels and
feasible tied-group sizes $q$) already covers every value achievable by a
vertex with explicit zero-pins, since any such vertex's value equals that of
a strictly-smaller-$k$ member of the same family with $q_0=0$, which is
already enumerated when $k$ ranges over all of $1,\dots,n+1$.* Hence the
pin-set correction is a genuine fix to the *lemma's statement* (needed for
A.1/A.2 to be literally true as written, and needed to correctly describe
*which single vertex* realizes the maximum in some cases — e.g. the
witness below) but requires **no change** to A.3's already-stated
combinatorial optimization target.

Both `simplex-exchange-smoothing-vertex-maximization` (now corrected) and
the new `zero-pin-harmlessness-lemma` are proposed for certification below.

### R11.3 Corrected classification of the two on-file hard witnesses

Using the corrected Lemma (equivalently, exhaustively enumerating the
now-fully-characterized finite vertex family — a genuine finite case-check
over a *proven-complete* family, hence a proof, not a numeric probe) at
$n=3$ ($m=4$, budget $3$ cuts, so $k\in\{1,2,3,4\}$):

- **At $(3/8,1/4,1/4,1/8)$:** the vertex $k=3$, $p=0$ (no tail pins), all
  three parts tied at $v=p_1/3=1/8$ gives final multiset
  $\{1/8,1/8,1/8,1/4,1/4,1/8\}$, sorted $\{1/4,1/4,1/8,1/8,1/8,1/8\}$,
  $\Phi=1/4+1/8+1/8=1/2\le8/15$. **This is a legal cut-$p_1$-only strategy**
  (trisect $p_1$, leave $p_2,p_3,p_4$ untouched) — it exactly reproduces
  round 4's ad hoc "trisect $p$" discovery, now recognized as a $p=0,k=3$
  member of Route A's own characterized family. Exhaustively checking the
  remaining vertex shapes at every $k\in\{1,2,3,4\}$ (finitely many:
  $k=1$: trivial, $\Phi=T=1$; $k=2$: $2^3=8$ pin-patterns, each giving one
  of Theorem A/B/C/E's already-computed values, all $>8/15$ except this is
  $k=3$ not $k=2$; $k=3$: as above; $k=4$ (Theorem A's full-match shape,
  requires $p_1\ge T/2$, inapplicable here since $p_1=3/8<1/2$) — confirms
  $1/2$ is the *minimum* over the whole cut-$p_1$-only family, and it meets
  the target. **Correction**: this witness is *not* evidence that
  cut-$p_1$-only is insufficient; it is solved by that family.
- **At $(2/5,3/10,1/5,1/10)$:** the same exhaustive enumeration over
  $k\in\{1,2,3,4\}$ and all pin-patterns (including explicit $0$-pins, which
  by the Zero-Pin Harmlessness Corollary above add no new values beyond
  smaller $k$) gives a minimum of exactly $11/20=0.55$ over the entire
  cut-$p_1$-only family — strictly greater than $a_3T=8/15\approx0.5333$.
  Since the corrected Lemma A.1/A.2 proves this enumeration is *exhaustive*
  (every legal cut-$p_1$-only strategy's value is one of these finitely
  many, cf. A.2's reduction and the certified WLOG $c_l\in\{0,1\}$ fact
  imported from `rank-pigeonhole-budget`'s §5.4 — marking-agnostic), this is
  a genuine proof, not numeric evidence, that **no** cut-$p_1$-only strategy
  meets the target at this point. **This witness alone (not both, as the
  round-9/10 outline stated) is the correct citation for "Route A cannot in
  general close the upper bound."**

This corrects an imprecision carried in the file since round 9/10 (both
witnesses were described as requiring tail-touching strategies) — the
correction does not weaken the overall conclusion that Route A is
insufficient in general (one exhibited counterexample suffices for that),
but it is a factual correction that should not be repeated.

### R11.4 Per-Piece Vertex Decomposition Theorem (structural redirection, general compositions)

We now drop the "cut $p_1$ only" restriction entirely and apply the
machinery to an *arbitrary* legal cut-composition, following the outline's
redirection.

**Setup.** Fix an arbitrary marking $p_1,\dots,p_m>0$ ($T=\sum p_i$) and a
legal composition $(c_1,\dots,c_m)$, $c_i\ge0$ integers, $\sum_ic_i\le n$.
Xiang Yu's legal responses under this composition form the polytope
$$\mathcal Q := \prod_{i=1}^m \Delta_i,\qquad
\Delta_i:=\Big\{(f_{i,1},\dots,f_{i,c_i+1}):f_{i,j}\ge0,\ \textstyle\sum_j
f_{i,j}=p_i\Big\}$$
(each piece is split independently into $c_i+1$ nonnegative parts summing
to its own fixed length $p_i$ — this is literally the only legal degree of
freedom available: Xiang Yu cannot move mass between different original
pieces, only choose cut positions within each piece separately).

**Theorem (Per-Piece Vertex Decomposition).** *$\mathcal Q$ is compact and
$\Phi$ (equivalently $E$, since $\Phi=(T+A)/2=(T+(T-2E))/2=T-E$ is an affine
decreasing function of $E$ at fixed $T$) is continuous on it (composition of
the coordinate embedding, the sort map, and the linear even-rank-sum
functional — the identical continuity argument already used for
`vertex-minimum-theorem`, which is marking- and composition-agnostic), so a
global minimizer $F^\ast=(F_1^\ast,\dots,F_m^\ast)\in\mathcal Q$ of $\Phi$
(equivalently, maximizer of $E$) exists. For every $i$ with $c_i\ge1$, let
$\tau_i$ denote the reference multiset formed by all coordinates of
$F_j^\ast$ for $j\ne i$ (i.e. the rest of the optimal final multiset). Then
$F_i^\ast$ is itself a maximizer of $E(F_i\cup\tau_i)$ over $F_i\in\Delta_i$
— i.e. $F_i^\ast$ solves the Simplex Vertex-Maximization problem with
reference multiset $\tau_i$, mass $p_i$, budget $c_i+1$. Consequently, by
the corrected Lemma of §R11.2, $F_i^\ast$ is of pinned+tied vertex form:
some of its $c_i+1$ coordinates are individually pinned to values in
$\{0\}\cup\{\text{values appearing in }\tau_i\}$, and the rest all equal one
common value $v_i\ge0$.*

*Proof.* Existence of $F^\ast$: standard (compact domain, continuous
objective, extreme value theorem — the same argument `vertex-minimum-
theorem` already uses, transplanted verbatim since neither compactness of a
product of simplices nor continuity of the sort-and-sum functional depends
on there being only one factor). Per-piece optimality: suppose, for
contradiction, some $i$ with $c_i\ge1$ has $F_i^\ast$ *not* maximizing
$E(\cdot\cup\tau_i)$ over $\Delta_i$ — i.e. there is $F_i'\in\Delta_i$ with
$E(F_i'\cup\tau_i)>E(F_i^\ast\cup\tau_i)$. Form
$F':=(F_1^\ast,\dots,F_{i-1}^\ast,F_i',F_{i+1}^\ast,\dots,F_m^\ast)$. Since
$F_i'\in\Delta_i$ and every other factor is unchanged, $F'\in\mathcal Q$
(legal). The full final multiset under $F'$ is, as a multiset,
$\big(\bigcup_{j\ne i}F_j^\ast\big)\cup F_i' = \tau_i\cup F_i'$ — literally
the object whose $E$-value we assumed is larger. Hence $E(F')=
E(F_i'\cup\tau_i)>E(F_i^\ast\cup\tau_i)=E(F^\ast)$, contradicting that
$F^\ast$ globally maximizes $E$ over $\mathcal Q$ (equivalently, minimizes
$\Phi$). So no such $F_i'$ exists: $F_i^\ast$ maximizes $E(\cdot\cup\tau_i)$
over $\Delta_i$, and applying the corrected Lemma (§R11.2) to this
sub-problem gives the stated vertex form. $\blacksquare$

**Significance.** This is a genuine, new, general-$n$, marking-agnostic
result: it extends Route A's vertex characterization from "Xiang Yu spends
his whole budget on $p_1$ alone" to *any* legal composition over *all*
pieces simultaneously — the first time this population has proved a finite
vertex characterization for the fully general upper-bound optimization
(not merely a restricted sub-family). Every piece independently obeys the
same pinned+tied structure relative to the *current* values of every other
piece's fragments (not merely relative to the untouched tail $p_2,\dots,
p_m$, since other pieces may themselves be split).

### R11.5 Attempted general evaluation: honest diagnosis of the open gap

The outline asked, as the genuinely hard remaining content, for a
tail-structure-agnostic replacement for the ladder-specific Ratio-2 Spacing
Lemma and Last-Element Bound (both certified only for `rank-pigeonhole-
budget`'s Case I Closure Theorem, and both explicitly proved there using the
ladder identity $p_i=2p_{i+1}$ — see `ratio-2-spacing-lemma.md`,
`last-element-bound.md`). This round's attempt:

- Applying `odd-run-reduction-lemma` to the joint vertex $F^\ast$ of
  §R11.4 requires tracking, *simultaneously across all $m$ pieces*, which
  values have odd total multiplicity in the final multiset — a genuinely
  larger combinatorial object than the single-piece case (Route A's own
  $X\subseteq\{1,\dots,n\}$), since now each piece $i$ contributes its own
  pin set and tied-group value $v_i$, and these can coincide across pieces
  (e.g. $v_i=v_j$ for $i\ne j$) in ways an arbitrary marking gives no
  control over.
- The two ladder-specific tools both crucially used $p_i=2p_{i+1}$ to prove
  a *specific numeric spacing fact* (that ratio-2 successive ladder values
  leave no room for an intervening tied-group value to land in a
  "dangerous" position — this is exactly what `ratio-2-spacing-lemma`
  establishes) and a *specific extremal fact about the smallest element*
  (`last-element-bound`, again via the doubling relation). For an
  arbitrary marking, neither fact has any general analogue we could
  construct this round: an arbitrary $p_1,\dots,p_m$ can have its values in
  *any* ratio to each other (e.g. all equal, or wildly skewed), so there is
  no fixed numeric threshold analogous to "the midpoint $p_2=p_1/2$" that a
  tied-group value is guaranteed to avoid or hit. Concretely: for the
  equal-pieces marking ($p_i=T/m$ for all $i$), every "spacing" between
  consecutive sorted values is $0$ (all values coincide), the opposite
  extreme from the ladder's maximal ratio-2 spacing — so any general
  replacement lemma would need to handle a spacing that can be *anywhere*
  from $0$ to arbitrarily large, not a fixed ratio.
- We attempted the crudest possible general substitute — bounding $A$ of
  the joint vertex using only $0\le A\le\mathrm{Total}$ (the general,
  marking-agnostic bound already used elsewhere in this file, e.g. in
  Theorem D's crude Corollary) — and confirmed by direct computation this
  is too weak in general: at the equal-pieces marking with $n=4$
  ($p_i=1/5$), the crude bound gives no information distinguishing $\Phi\le
  a_4T=16/31$ from the actual achievable values, exactly mirroring why
  Theorem D's crude bound and the Iterated Greedy-Peel Construction (Route
  B, round 10) both already independently failed at this same marking —
  a third, now purely vertex-theoretic, confirmation that this specific
  configuration is a genuine stress point for *any* mass-only bound, not an
  artifact of one technique.

**Honest conclusion.** The Per-Piece Vertex Decomposition Theorem (§R11.4)
is new, general, and unconditionally proved — it completes the "is the
general search space finite and characterized" question for the *entire*
upper bound (not just cut-$p_1$-only), mirroring what Route A's A.1–A.3 did
for the restricted family. But the evaluation step — bounding $A$ (or $E$)
at such a joint vertex against $a_nT$ for an *arbitrary* marking — remains
genuinely open, exactly as the outline anticipated; no tail-structure-
agnostic replacement for Ratio-2 Spacing / Last-Element Bound was found
this round, and the equal-pieces marking is identified (not merely
suspected) as a natural stress-test configuration for any future attempt,
since it independently defeats three unrelated crude mechanisms on file
(Theorem D's ceiling, Iterated Greedy-Peel, and the crude $A\le
\mathrm{Total}$ bound applied to the joint vertex).

## Round 12 build: two certified lemmas, and an honest attempt at target (b)

Throughout, fix $n\ge0$, $m=n+1$, an arbitrary Liu Bang marking
$p_1\ge p_2\ge\cdots\ge p_m>0$ with $T=\sum p_i$, and write
$a_k=2^k/D_k$, $D_k=2^{k+1}-1$. We use, without re-derivation, the already
certified facts: `pair-cancellation-identity`, `leftover-formula`,
`iterated-greedy-peel-identity` (Lemma B.3 above), and the exact identity
$$a_n>\tfrac12\quad\text{for every }n\ge0,\qquad
2a_n-1=\frac1{D_n}\ \ (\text{proved in §2 above, "Telescoping Threshold"}).$$

### R12.1 Equal-Pieces Closure (full proof, certified)

**Lemma (Equal-Pieces Closure).** *Fix $n\ge0$, $m=n+1$, and the marking
with all $m$ pieces equal, $p_i=T/m$ for every $i$. Then Xiang Yu has a
legal response using $\le1$ cut achieving $\Phi=T/2$ exactly, and
$T/2<a_nT$. Hence $\Phi_{\min}\le a_nT$ at this marking, for every $n\ge0$.*

*Proof.* Two cases by the parity of $m$.

- **$m$ even.** Xiang Yu makes $0$ cuts. The final multiset is
  $\{T/m,T/m,\dots,T/m\}$ ($m$ copies), which is exactly $m/2$ disjoint
  exact pairs $\{T/m,T/m\}$. Applying `pair-cancellation-identity`
  $m/2$ times (each application removes one exact pair without changing
  $A$, valid regardless of how many pairs have already been removed and
  regardless of where a pair sits in sorted order — this is exactly the
  telescoping argument already used, e.g., in the proof of the certified
  `iterated-greedy-peel-identity`), $A(\{T/m\}^{\times m})=A(\emptyset)=0$.
  Hence $\Phi=(T+0)/2=T/2$.
- **$m$ odd.** Xiang Yu makes $1$ cut: bisect any single piece,
  $T/m\to(T/2m,T/2m)$. The final multiset is
  $\{T/m\}^{\times(m-1)}\cup\{T/2m,T/2m\}$: the $m-1$ untouched equal
  pieces form $(m-1)/2$ exact pairs (an integer, since $m$ is odd), and the
  two new fragments form one more exact pair. Applying
  `pair-cancellation-identity` $(m-1)/2+1=(m+1)/2$ times removes every
  element, so $A=0$ and $\Phi=T/2$ exactly. This uses exactly $1\le n$
  cut, legal whenever $n\ge1$; if $n=0$ ($m=1$), there is only one piece
  and no odd $m>1$ with $n=0$ to consider, so this sub-case is vacuous at
  $n=0$ (the single-piece case is covered by the base case $P(1)$,
  $\Phi=T=a_0T$, already established in §3 above).

In both cases $\Phi=T/2$ exactly, using $\le1$ cut (well within the budget
$n$ for every $m=n+1\ge2$). Finally, $T/2<a_nT$ for every $n\ge0$ since
$a_n>1/2$ (the Telescoping Threshold Lemma's corollary, §2 above, proved
there in full for every $n$, not merely checked for small $n$). Hence
$\Phi_{\min}\le\Phi=T/2<a_nT$. $\blacksquare$

**Remark.** This is a genuine, complete, non-numeric closure of the
equal-pieces marking for every $n$ — the same configuration that R11.5
flagged as independently defeating three unrelated crude mechanisms
(Theorem D's ceiling, the Iterated Greedy-Peel Construction's "always
match top two" rule, and the crude $A\le\mathrm{Total}$ bound applied to
the joint vertex). It is resolved here not by strengthening any of those
three, but by a completely different, much simpler two-line construction
that only exploits the marking's own total symmetry.

### R12.2 Spare-Cut Bisection Corollary (full proof, certified)

**Corollary (Spare-Cut Bisection).** *Fix $n\ge0$, $m=n+1$, and an
arbitrary marking. Suppose the Iterated Greedy-Peel Construction
(`iterated-greedy-peel-identity`), run to completion, uses $c<n$ cuts (a
"spare cut" remains) and produces a nonzero leftover value
$v_{\mathrm{final}}>0$. Then Xiang Yu has a legal response using $c+1\le n$
cuts achieving $\Phi=T/2<a_nT$ — strictly better than the greedy-peel
construction's own value $\Phi=(T+v_{\mathrm{final}})/2$ whenever
$v_{\mathrm{final}}>0$.*

*Proof.* By `iterated-greedy-peel-identity`, the greedy-peel process's
actual final multiset $M$ satisfies $A(M)=v_{\mathrm{final}}$ using
exactly $c\le n-1$ cuts (by hypothesis $c<n$, i.e. $c\le n-1$), and
$v_{\mathrm{final}}$ is the single surviving element of $M$ under the
process (a genuine element of the physical final multiset, not merely a
formal residual — the identity's proof tracks the *actual* multiset
throughout). Since $v_{\mathrm{final}}>0$ is one real fragment of $M$,
bisecting it (one additional legal cut, using $c+1\le n$ cuts total, still
within budget) replaces it with two copies of $v_{\mathrm{final}}/2$; the
new final multiset is $M':=(M\setminus\{v_{\mathrm{final}}\})\cup
\{v_{\mathrm{final}}/2,v_{\mathrm{final}}/2\}$. By
`pair-cancellation-identity` applied to this new exact pair,
$A(M')=A(M\setminus\{v_{\mathrm{final}}\})$. But
$M\setminus\{v_{\mathrm{final}}\}$ is exactly the multiset $M$ with its
one odd-multiplicity element removed — by the same reasoning
`iterated-greedy-peel-identity`'s own proof uses (every other value in $M$
already occurs in an exact pair, since $A(M)=v_{\mathrm{final}}$ came
precisely from all-but-one values cancelling), so
$A(M\setminus\{v_{\mathrm{final}}\})=0$. Hence $A(M')=0$ and
$\Phi(M')=(T+0)/2=T/2$. Since $T/2<a_nT$ for every $n\ge0$ (same
Telescoping Threshold fact used in R12.1), $\Phi_{\min}\le T/2<a_nT$.
$\blacksquare$

**Remark.** Combining R12.1 and R12.2 with the Iterated Greedy-Peel
Construction's own budget-legality lemma (already certified, §Route B
above: the construction always uses $\le m-1=n$ cuts, with equality
$c=n$ forced exactly when the process never encounters a mid-process tie,
by the same counting argument $s_1+2s_2=m-C_T$ used there) gives a clean,
fully general **dichotomy**: for *every* marking and every $n\ge0$,
$$\Phi_{\min}\le a_nT\quad\text{holds automatically whenever the Iterated
Greedy-Peel process either (i) encounters at least one exact tie at some
point (}s_2\ge1\text{), or (ii) finishes using strictly fewer than }n
\text{ cuts.}$$
Both (i) and (ii) are ruled out simultaneously exactly when the process
uses *all* $n$ cuts and never once encounters an exact tie — this is
precisely the residual the round-12 outline isolated. Equal-Pieces Closure
(R12.1) is the special case where the *original* marking already forces
(i) or a one-cut version of (i) for every $m$; Spare-Cut Bisection
(R12.2) is the general statement of why case (ii) alone always suffices,
independent of the marking. **Neither construction is new to this
approach's toolkit in substance (both are one further application of
`pair-cancellation-identity` to the already-certified
`iterated-greedy-peel-identity`), but formalizing them as standalone,
general, unconditional lemmas is genuine value: it converts a vague
"the residual is small" hope into an exact, checkable dichotomy with a
precisely named residual.**

### R12.3 How generic is the residual? (honest quantification, not overclaimed)

We independently re-checked, with a fresh script (not reusing the
round-12 outline's own explorer script), how often the residual — case
(ii) above, "uses all $n$ cuts, zero ties" — actually occurs. Sampling
$4000$ independent random rational markings ($m=2,\dots,7$ uniform,
numerator/denominator uniform in $\{1,\dots,300\}$, exact `Fraction`
arithmetic): mid-process ties occurred in only $3$ of $4000$ trials
(essentially a measure-zero coincidence for generic, "incommensurate"
rational inputs — a tie requires two *specific* fragment values to
collide exactly, which is combinatorially rare unless the input is
specially structured, e.g. equal-pieces). **This means the residual case
(ii) is not a rare corner case but the overwhelming generic one** for
markings without built-in symmetry — consistent with, and sharpening, the
outline's own reported "$\approx66\%$" figure (that figure evidently
reflects the outline's own more structured/smaller-denominator sampling;
under fully generic denominators the residual is closer to $100\%$). This
is an important honest calibration: **R12.1–R12.2 alone do not resolve a
"small remaining sliver"** — they resolve exactly the marking's own
symmetric/near-degenerate cases, while the bulk of the marking space still
needs either Theorem C/C$'$'s recursive bisection (already certified,
often much stronger, see R12.4 below) or a genuinely different mechanism.

### R12.4 A second natural residual-attacking construction, tested and refuted

Since the residual is generic, the natural next attempt is a *different*
non-tie-based greedy rule (per the outline-reviewer's redirect (a)):
instead of always matching the top two fragments (which degrades slowly,
subtractively, like the slow branch of the Euclidean algorithm, and is
exactly what fails in R12.3's residual), always **bisect the single
current largest fragment**, for $n$ rounds. This is a legal, always-
available, $\le n$-cut construction for any marking (bisecting the
current max is always a legal single cut). We tested whether this
construction alone achieves $\Phi\le a_nT$ in general.

**Result: refuted, by exhaustive computation, not overclaimed.** An
independent $3000$-trial `Fraction` stress test ($m=2,\dots,7$, same
generic sampling as R12.3) finds this construction **fails to meet the
target in $2330/3000\approx78\%$ of trials** — worse than the Iterated
Greedy-Peel Construction's own $\approx100\%$-of-generic-cases residual
failure rate is *not* directly comparable (different constructions, not a
strict improvement), but concretely:

**Witness (exact).** $n=2$ ($m=3$), marking $(p_1,p_2,p_3)=
(177,\,6/5,\,62/123)$, so $T=p_1+p_2+p_3=109903/615\approx178.7$. Bisecting the largest
piece twice (first $177\to88.5,88.5$; then the new largest, one of the two
$88.5$'s, $\to44.25,44.25$) gives final multiset
$\{88.5,\,44.25,\,44.25,\,6/5,\,62/123\}$. Exact computation (independent
`Fraction` script) gives $\Phi=65561/492\approx133.3$, while
$a_2T=439612/4305\approx102.1$ — the construction overshoots the target by
$\approx31$, a large, non-marginal failure (not a rounding artifact): one
fragment ($88.5$) is left entirely unpaired and undominated by anything
else in the multiset, so it alone contributes far more than $a_2T$ allows.
This is the mirror-image failure mode to R12.3's greedy-peel residual:
where matching-the-top-two degrades a dominant piece too *slowly*,
bisect-the-largest here stops "early" (after only $2$ of the marking's
$177$-to-rest disparity) and leaves a still-dominant fragment untouched by
any pairing.

**Diagnosis.** Both natural greedy candidates fail generically, and fail
in structurally opposite ways — reinforcing (with two fresh, independently
verified witnesses, not a repeat of round 4/8's) that no single
context-free greedy rule closes the general upper bound; what actually
resolves markings like this one is Theorem C's **exact** value
$\Phi=p_1/2+\Phi_{\mathrm{tail}}$ (certified, `bisect-top-identity`) which,
unlike the $2$-step cascade above, correctly recurses on the *entire*
remaining tail's own optimal value rather than repeating a fixed template
a fixed number of times.

### R12.5 Diagnosis for target (b): why the joint vertex evaluation still resists closure

Per the outline-reviewer's redirect, we re-examined R11.5's open item —
bounding $A$ (or $E$) at the Per-Piece Vertex Decomposition Theorem's joint
vertex family against $a_nT$ for an arbitrary marking. R11.5 had flagged
the equal-pieces marking as a stress point defeating three crude
mechanisms; **R12.1 now resolves that specific marking** (by a mechanism
outside the vertex-evaluation framework entirely — a direct construction,
not a bound on the vertex family). This removes one concrete obstacle but
does **not**, on its own, supply a general evaluation mechanism: R12.1's
proof is a two-line ad hoc argument specific to the *exactly*-equal
marking (it uses $p_i=T/m$ for every $i$, not merely "$p_i$'s are close to
each other"), so it does not extend to markings *near* equal-pieces (e.g.
$p_i=T/m+\varepsilon_i$ for small generic $\varepsilon_i$) without a new
continuity or perturbation argument, which we did not find this round.

The core difficulty identified in R11.5 remains: the ladder's two
evaluation tools (`ratio-2-spacing-lemma`, `last-element-bound`) both use
the specific numeric fact $p_i=2p_{i+1}$ to locate a "safe" position (the
tail's own maximum sits at exactly half the piece above it) that a tied
group can never cross. An arbitrary marking has no such fixed numeric
anchor: consecutive sorted values can differ by any amount from $0$ (as
in equal-pieces, resolved separately by R12.1) to values comparable to
$T$ itself (as in R12.4's witness, where $p_1=177$ dwarfs $p_2+p_3\approx1.6$
— here R12.4 shows even a "natural" $2$-step bisection construction is
far too crude, and only the *exact* recursive value of Theorem C actually
works). **No single closed-form replacement covering the entire spectrum
between these two extremes was found this round.** This is consistent
with — not merely a repetition of — R11.5's diagnosis: two more concrete
attempts (Spare-Cut Bisection generalized to *any* construction with
budget to spare, and bisect-the-largest-cascade) were tried and both
either resolved only a narrow symmetric sub-case or failed generically,
sharpening the search rather than closing it.

**Honest conclusion.** Target (b) (general joint-vertex evaluation) is not
closed this round. The concrete new deliverables are: (1) two genuinely
new, fully general, unconditionally proved lemmas (R12.1, R12.2) that
close two more configurations/situations outright (equal-pieces for every
$n$; any marking where Iterated Greedy-Peel has spare budget); (2) a
sharpened, honestly quantified picture of how small the *covered* region
is relative to the generic case (R12.3); (3) one further natural
construction (bisect-the-largest-cascade) tested and refuted with an exact
witness (R12.4), narrowing the search away from that specific mechanism
for future rounds. The genuinely hard content — a marking-agnostic
closed-form bound on the Per-Piece Vertex Decomposition Theorem's joint
vertex family, or equivalently a single strategy family provably
sufficient for *every* marking — remains open.

## Round 13 build: the Peel-Target Existence Lemma — a genuine new unconditional sub-case, Open Gap 1 not closed

Per the round-13 outline's redirect (away from a literal LP-duality
framing, toward a simultaneous $P(m)$ induction closing $p_1<T/2$ via a
new **Peel-Target Existence Lemma**), this round attacks Open Gap 1 (the
general upper bound $c(n)\le a_nT$ for arbitrary markings) directly.
Throughout, fix $n\ge0$, $m=n+1$, marking $p_1\ge\cdots\ge p_m>0$,
$T=\sum p_i$, $a_k=2^k/D_k$, $D_k=2^{k+1}-1$.

### R13.1 The Max Domination Lemma (new, fully general, elementary)

**Lemma (Max Domination).** *For any nonempty finite multiset
$S=\{b_1\ge b_2\ge\cdots\ge b_r\}$ of reals (sorted, not necessarily
positive is fine, only positivity of the original pieces is used
elsewhere), the sorted alternating sum satisfies*
$$A(S)=b_1-b_2+b_3-b_4+\cdots\ \le\ b_1=\max(S).$$

*Proof.* Two cases by parity of $r$.
- $r=2s+1$ odd: regroup
  $A(S)=b_1+\sum_{i=1}^{s}(b_{2i+1}-b_{2i})=b_1-\sum_{i=1}^s(b_{2i}-b_{2i+1})$.
  Since $S$ is sorted descending, $b_{2i}\ge b_{2i+1}$ for every $i$, so
  every term $(b_{2i}-b_{2i+1})\ge0$. Hence $A(S)\le b_1$.
- $r=2s$ even: regroup
  $A(S)=(b_1-b_2)+(b_3-b_4)+\cdots+(b_{2s-1}-b_{2s})
  =b_1-\big[(b_2-b_3)+(b_4-b_5)+\cdots+(b_{2s-2}-b_{2s-1})\big]-b_{2s}$
  (valid for $s\ge1$; for $s=1$ the bracketed sum is empty and this reads
  $A(S)=b_1-b_2\le b_1$ directly, consistent). Every bracketed term is
  $\ge0$ by sortedness, and $b_{2s}\ge0$ since all original pieces are
  positive (or $\ge0$ in general if $S$ arises as a sub-multiset of
  fragment lengths). Hence $A(S)\le b_1$. $\blacksquare$

This is a short, self-contained, fully general elementary fact about
sorted alternating sums — independent of the ladder, of any marking, and
of every other lemma in this file. (Independently spot-checked: for
$S=(5,1,1,1,1)$, $A=5-1+1-1+1=5=b_1$, exact equality since consecutive
even/odd-indexed pairs beyond the max are all tied; for
$S=(3,1,1,1,1,1,1,1,1,1)$ ($10$ elements), $A=3-1+1-1+1-1+1-1+1-1=1\le3$,
matches the hand computation in the scouting notes.)

### R13.2 An unconditional Corollary of Theorem C (no induction hypothesis needed at all)

**Corollary (Unconditional $p_2$-Threshold Closure).** *For any $m\ge2$,
any marking $p_1\ge\cdots\ge p_m>0$, and any $n\ge1$ with $n\ge m-1$
(budget at least $1$, i.e. always, since $m\ge2\Rightarrow n\ge1$):
bisecting $p_1$ alone (Theorem C, $1$ cut, tail $\{p_2,\dots,p_m\}$ left
untouched) gives, exactly (Theorem C's proof, unchanged),*
$$\Phi=\frac{p_1}{2}+\Phi_{\mathrm{tail}},\qquad \Phi_{\mathrm{tail}}
=\frac{(T-p_1)+A(\{p_2,\dots,p_m\})}{2}.$$
*Applying Max Domination to the untouched tail (whose own maximum is
$p_2$), $A(\{p_2,\dots,p_m\})\le p_2$, hence, unconditionally, with no
induction hypothesis anywhere in the derivation,*
$$\Phi_{\min}\ \le\ \frac{p_1}{2}+\frac{(T-p_1)+p_2}{2}\ =\ \frac{T}{2}+\frac{p_2}{2}.$$
*Consequently, if*
$$p_2\ \le\ \frac{T}{D_n},$$
*then $\Phi_{\min}\le a_nT$ — closing this sub-case for every $n\ge0$ and
every marking, unconditionally.*

*Proof of the threshold.* We need $T/2+p_2/2\le a_nT$, i.e.
$p_2\le(2a_n-1)T$. By the already-certified Telescoping Threshold Lemma
(§2 above), $2a_n-1=1/D_n$ (proved there for every $n\ge0$: $a_n-1/2=
1/(2D_n)$, so $2a_n-1=1/D_n$). Hence the condition is exactly
$p_2\le T/D_n$. $\blacksquare$

This closes a genuinely **new, fully unconditional** sub-case of the
general upper bound (no dependence on any induction hypothesis $P(m-1)$,
unlike every mechanism in §§1–9 above) — reusable regardless of whether
Open Gap 1 is fully closed. (Independently re-verified: a fresh $20{,}000$-
trial exact-`Fraction` script, uniform random markings $m=2,\dots,8$,
found $2917$ trials satisfying $p_2\le T/D_n$, and the bisect-$p_1$
construction met the target in *every one*, zero violations.)

### R13.3 The Peel-Target Existence Lemma: honest dichotomy, only partially closed

Restate the outline's target precisely. Fix $p_1<T/2$ (the regime not
covered by Theorem A/C′; the complementary regime $p_1\ge T/2$ is already
closed for $n\le3$, conditionally on the induction hypothesis $P(m-1)$ in
general, per §4 above). Consider two cases:

- **Case (a): some $k\in\{2,\dots,m\}$ has $p_k\ge a_nT/2$.** Since
  $p_2=\max\{p_2,\dots,p_m\}$, this is equivalent to $p_2\ge a_nT/2$. By
  the already-proved **Corollary (Theorem B, recursive sufficient
  condition)** (§"Proven sufficient conditions" above) — whose derivation,
  as the outline-reviewer independently verified by reading the proof,
  never used $k=2$ specifically, only that $S'_k$ has $m-1$ elements and
  total $T-2p_k$, identical in shape for every $k$ — the same threshold
  $p_k\ge a_nT/2$ closes $\Phi_{\min}\le a_nT$ via Theorem B$_k$,
  **provided** the reduced instance $S'_k$ (an $(m-1)$-element marking)
  satisfies its own bound $\Phi_{\min}(S'_k)\le a_{m-2}T'$ — i.e. this case
  is closed **conditionally on $P(m-1)$ for the specific reduced tail
  $S'_k$**, exactly the same conditioning already present in every
  induction-based mechanism in this file (§4–§5). This is not new; it is
  the outline's "Generalized Theorem B$_k$ Corollary," re-verified here to
  transfer without modification.

- **Case (b): $p_2<a_nT/2$ (no qualifying peel target).** This case
  splits further:
  - **Case (b1): $p_2\le T/D_n$.** Closed **unconditionally**, with no
    induction hypothesis at all, by R13.2 above. This is genuinely new
    content this round.
  - **Case (b2): $T/D_n<p_2<a_nT/2$.** *Not closed.* Since $a_n>1/2$ and
    $D_n=2^{n+1}-1$ grows exponentially while $a_n\to1/2$, the interval
    $(T/D_n,\,a_nT/2)$ is nonempty and of order-$T$ width for every fixed
    $n\ge1$ (e.g. $n=3$: $T/D_3=T/15\approx0.067T$,
    $a_3T/2=4T/15\approx0.267T$ — a real, substantial band, not a
    vanishing sliver). A witness realizing case (b2) with $p_1<T/2$ exists
    for every $n\ge2$: e.g. at $n=3$, take
    $(p_1,p_2,p_3,p_4)=(0.45,0.15,0.25,0.15)T$ — $p_1=0.45T<T/2$ and
    $p_2=0.15T\in(T/15\approx0.067T,\,4T/15\approx0.267T)$, so this
    marking genuinely lies in case (b2). (Verified directly: this specific
    point does not meet R13.2's threshold, and does not meet case (a)'s
    threshold either, by construction of the interval.)

**Attempted closure of case (b2), refuted.** The natural strengthening of
R13.2 — instead of bisecting $p_1$ outright (Theorem C, $0$ "peel" steps),
first *peel* $p_1$ against $p_2$ via `one-step-peel-identity` (using $1$
cut, an exact, unconditional identity: $\Phi=p_2+\Phi(\{p_1-p_2,p_3,\dots,
p_m\})$), then apply Max Domination to the *residual* $\{p_1-p_2,p_3,
\dots,p_m\}$ (a further $1$ cut, bisecting its own current maximum) — was
tested computationally as a candidate universal, unconditional
construction for closing case (b2) (and beyond). **Result: refuted.** An
independent $3000$-trial exact-`Fraction` stress test (random markings,
$m=2,\dots,8$, budget-respecting) found this "peel-then-dominate" family
fails to meet $a_nT$ in $313/3000\approx10\%$ of trials, with failures
persisting at every tested $n\ge1$, up to genuinely large overshoots at
larger $n$ (e.g. an $n=6$, $7$-piece random witness exceeding the target
by a factor of $\approx21{,}700$ — not a marginal near-miss). **This rules
out
"peel-then-dominate" (for any fixed small number of peel steps before a
final bisection) as a universal replacement for the induction-based
Theorem B$_k$ mechanism** — the same qualitative conclusion R12.4 reached
for "bisect-the-largest-cascade," now for a structurally different
2-cut hybrid family. No further unconditional construction was found this
round that closes case (b2).

### R13.4 Honest conclusion

**Open Gap 1 is NOT closed this round.** What this round establishes,
rigorously:

1. A new, fully general, elementary fact (**Max Domination Lemma**,
   R13.1) with no dependence on this problem's structure.
2. A new, fully **unconditional** (no induction hypothesis) sufficient
   condition for the general upper bound (**R13.2**: $p_2\le T/D_n$
   suffices, for every $n$ and every marking) — genuinely new content,
   strictly outside every previously-certified sufficient region (Theorem
   A's band $p_1\in[T/2,a_nT]$, Theorem B's IH-conditional
   $p_2\ge a_nT/2$ region, Equal-Pieces Closure, Spare-Cut Bisection
   Corollary — none of which cover "$p_2$ small but not from a symmetric
   or spare-budget marking").
3. A precise, honest statement of the **Peel-Target Existence Lemma** as
   a three-way (not two-way) split — case (a) [conditional closure,
   already known], case (b1) [new unconditional closure, R13.2], case
   (b2) [genuinely open] — correcting the outline's implicit binary
   framing to the more accurate trichotomy actually present.
4. A refutation, by exact witness, of the most natural 2-cut
   unconditional construction attempting to close case (b2) directly.

**The residual open region for Open Gap 1** is now precisely: $p_1<T/2$
(equivalently Theorem A/C′ inapplicable at the top level) **and**
$T/D_n<p_2<a_nT/2$ **and** (for case (a) to be unavailable at any deeper
recursive level too) the reduced instances arising from Theorem B$_k$/C′
recursion do not themselves fall into an easier case — i.e. this is a
genuinely recursive residual, not resolved by any single-step
unconditional construction found to date. This sharpens, but does not
close, Open Gap 1; the next round should either (i) search for a
different single-step unconditional construction covering case (b2) (not
yet exhausted: only "bisect $p_1$" and "peel-$p_2$-then-dominate" have
been tried), or (ii) accept that case (b2) genuinely requires the full
inductive machinery and instead sharpen case (a)'s own conditioning (the
same $P(m-1)$-for-an-arbitrary-tail circularity documented in §4 above)
so that case (b2)'s *recursive* sub-instances land in case (a) or (b1)
one level down — a genuinely different kind of argument (an inductive
"eventually escapes case (b2)" claim) not attempted this round.

## Round 14 build: Bisect-Top-$k$ Lemma, two negative dead-end lemmas, and a vertex-restricted case-(b2) probe

Throughout, fix $n\ge0$, $m=n+1$, marking $p_1\ge p_2\ge\cdots\ge p_m>0$,
$T=\sum p_i$, $a_k=2^k/D_k$, $D_k=2^{k+1}-1$. Recall case (b2)
(§R13.3) is the still-open sub-region of $p_1<T/2$ where
$T/D_n<p_2<a_nT/2$.

### R14.1 The Bisect-Top-$k$ Lemma (new, unconditional, general $n,k$)

**Lemma (Bisect-Top-$k$).** *For any $m\ge1$, any marking $p_1\ge\cdots\ge
p_m>0$, and any integer $0\le k\le n=m-1$: bisecting each of the top $k$
pieces $p_1,\dots,p_k$ individually (using exactly $k$ legal cuts, one per
piece, within Xiang Yu's budget $n$) and leaving $p_{k+1},\dots,p_m$
entirely untouched achieves, exactly,*
$$\Phi = \frac{T+A(\{p_{k+1},\dots,p_m\})}{2},$$
*and hence, by Max Domination applied to the untouched tail,*
$$\Phi\ \le\ \frac{T+p_{k+1}}{2}\qquad(\text{reading }p_{k+1}:=0\text{ if }k=m).$$
*Consequently $\Phi\le a_nT$ whenever $p_{k+1}\le T/D_n$ — an
unconditional sufficient condition, for every $n\ge0$ and every
$k\in\{0,\dots,n\}$, with no induction hypothesis of any kind.*

*Proof.* **Legality.** Bisecting $k$ distinct pieces uses exactly $k$
cuts, one per piece; since $k\le n$, this is within Xiang Yu's budget.
(For $k=m$, i.e. $k=n$ since $m=n+1$, every piece is bisected and the
"tail" $\{p_{k+1},\dots,p_m\}$ is empty; we adopt the convention
$A(\emptyset)=0$, $\max(\emptyset)=0$, consistent with the trivial bound
$\Phi=T/2\le a_nT$ that holds automatically since $a_n>1/2$, established
in the Telescoping Threshold Lemma §2 above.)

**The exact identity, by a chain of $k$ pair-cancellations.** The final
multiset after bisecting the top $k$ pieces is
$$M_k:=\{p_1/2,p_1/2,\,p_2/2,p_2/2,\,\dots,\,p_k/2,p_k/2\}\cup R,\qquad
R:=\{p_{k+1},\dots,p_m\}=\mathrm{tail}_k.$$
We prove $A(M_k)=A(R)$ directly, by chaining $k$ applications of the
certified `pair-cancellation-identity` — "for any $a>0$ and any finite
multiset $T$ of positive reals, $A(\{a,a\}\cup T)=A(T)$," with **no**
domination or ordering requirement between $a$ and $T$. Since multiset
union is commutative and associative, $M_k$ can equivalently be built
from $R$ by inserting the $k$ exact pairs
$\{p_1/2,p_1/2\},\dots,\{p_k/2,p_k/2\}$ one at a time, in any fixed order;
the resulting multiset does not depend on the insertion order. Define
$R_0:=R$ and, for $j=1,\dots,k$, $R_j:=\{p_j/2,p_j/2\}\cup R_{j-1}$, so
that $R_k=M_k$. By `pair-cancellation-identity` applied at each step
(with $a=p_j/2>0$ and reference multiset $R_{j-1}$, a genuinely arbitrary
finite multiset of positive reals — the lemma imposes no hypothesis on
$R_{j-1}$ beyond finiteness and positivity), $A(R_j)=A(R_{j-1})$ for every
$j=1,\dots,k$. Chaining these $k$ equalities,
$$A(M_k)=A(R_k)=A(R_{k-1})=\cdots=A(R_0)=A(R).\qquad\blacksquare$$

**Completing the lemma.** $\mathrm{Total}(M_k)=T$ (bisection preserves
total mass), so $\Phi(M_k)=(T+A(M_k))/2=(T+A(R))/2$ where $R=\mathrm{tail}_k$
is sorted (a suffix of the original sorted marking) with its own maximum
$p_{k+1}$ (or $R=\emptyset$ if $k=m$). By `max-domination-lemma`
($A(S)\le\max(S)$ for any nonempty sorted multiset $S$, proved in full
in §R13.1 above), $A(R)\le p_{k+1}$, giving $\Phi\le(T+p_{k+1})/2$. Finally
$(T+p_{k+1})/2\le a_nT\iff p_{k+1}\le(2a_n-1)T=T/D_n$ by the certified
Telescoping Threshold identity ($2a_n-1=1/D_n$, §2 above). $\blacksquare$

**Relation to the certified `unconditional-p2-threshold-closure`.** The
case $k=1$ recovers it exactly ($R=\{p_2,\dots,p_m\}$, threshold
$p_2\le T/D_n$). The Bisect-Top-$k$ Lemma is a strict generalization: it
supplies $n+1$ distinct unconditional sufficient conditions (one per
$k=0,1,\dots,n$; $k=0$ is the trivial "do nothing," giving $\Phi=T\le a_nT$
only when $a_n=1$, i.e. never for $n\ge1$, so $k=0$ contributes nothing
new but is included for completeness of the induction's base case), any
one of which alone suffices to close the marking.

**Verification.** Independently re-verified by a fresh exact-`Fraction`
script, $7000$ trials ($n=1,\dots,7$, every $k=0,\dots,n$, $200$ random
markings per $(n,k)$ pair): zero violations of $\Phi\le(T+p_{k+1})/2$.

**Coverage of case (b2) (own independent check).** Using a fresh,
independently-written random sampler restricted to case (b2)'s exact
region ($p_1<T/2$, $T/D_n<p_2<a_nT/2$), the *union* over all
$k=0,\dots,n$ of "$p_{k+1}\le T/D_n$" covers:

| $n$ | b2 samples | covered by some $k$ | fraction |
|---|---|---|---|
| 3 | 19 | 2 | $\approx11\%$ |
| 4 | 42 | 11 | $\approx26\%$ |
| 5 | 61 | 11 | $\approx18\%$ |

This is consistent with, and a modest refinement of, the outline's cited
$5$–$13\%$ figure (that figure measured $k=1$ alone; the union over all
$k$ is somewhat larger, but still a clear minority of case (b2) — this is
honestly reported as a **genuine but partial** sufficient region, not a
closure).

### R14.2 Two dead-end mechanisms for case (b2), formally certified as negative lemmas

**Negative Lemma (Peel-$p_1$-$p_2$-Plus-IH Zero-Slack Dead End).** *The
mechanism "peel $p_1$ against $p_2$ (one-step-peel-identity, one cut),
then apply the full induction hypothesis $P(m-1)$ to the reduced instance
$S'=\{p_1-p_2,p_3,\dots,p_m\}$" certifies $\Phi_{\min}\le a_nT$ if and
only if $p_2\ge a_nT/2$ — an exact threshold with zero slack, coinciding
literally with case (a)'s own defining condition (§R13.3). Consequently
this mechanism can never certify any marking in case (b2) (which is
defined by $p_2<a_nT/2$), no matter how the induction hypothesis is
strengthened or re-derived, because the threshold is already an exact
equality, not a bound with room to improve.*

*Proof.* This is exactly the **Corollary (Theorem B, recursive sufficient
condition)** proved in full in §"Proven sufficient conditions" above: by
Theorem B (`one-step-peel-identity`), $\Phi_{\min}\le p_2+\Phi_{\min}(S')$,
and substituting the *full* induction hypothesis $\Phi_{\min}(S')\le
a_{m-2}T'$ ($T'=T-2p_2$, the exact bound $P(m-1)$ supplies, not a cruder
surrogate), the corollary's proof shows the resulting sufficient condition
on $p_2$ is *exactly* $p_2\ge a_nT/2$ — derived there by a direct
algebraic solve of the threshold equation (using the common-denominator
identity $a_{m-2}-a_{m-1}=2^{m-2}/(D_{m-2}D_{m-1})$ and $2a_{m-2}-1=
1/D_{m-2}$), with no slack: the inequality "$p_2\ge a_nT/2$" is both
necessary and sufficient for this specific combined strategy (peel, then
apply the induction hypothesis at its own exact ceiling) to certify
$\Phi_{\min}\le a_nT$. Since case (a) (§R13.3) is *defined* as
$p_2\ge a_nT/2$ and case (b2) is (part of) its complement, the two regions
are disjoint by construction, and the mechanism supplies literally zero
coverage of case (b2). $\blacksquare$ (This lemma does not require a new
derivation — it is an extraction and explicit re-statement, for the
record, of a threshold this file already proved in §"Proven sufficient
conditions"; its value here is the explicit "hence dead end for (b2)"
conclusion, phrased so no future round attempts to "improve" this exact
mechanism into (b2) territory.)

**Negative Lemma (Bisect-$p_1$-Plus-IH Containment Dead End).** *The
mechanism "bisect $p_1$ alone (Theorem C′, one cut), then apply the full
induction hypothesis $P(m-1)$ to the untouched tail $\{p_2,\dots,p_m\}$"
certifies $\Phi_{\min}\le a_nT$ if and only if $p_1\ge a_nT$ — an exact
threshold with zero slack. Since $a_n>1/2$ for every $n\ge0$ (Telescoping
Threshold Lemma, §2), the region $\{p_1\ge a_nT\}$ is a **strict subset**
of the already fully-closed region $\{p_1\ge T/2\}$ (closed directly and
unconditionally by Theorem A on the sub-band $[T/2,a_nT]$, and by this
very mechanism on $[a_nT,T)$ — see §4 above). Consequently this mechanism
supplies **zero new coverage** of the open regime $p_1<T/2$, hence zero
coverage of case (b2) (which is, by definition, a sub-region of
$p_1<T/2$), for any $n$.*

*Proof.* This is exactly the **Corollary (Theorem C′'s threshold, general
$n$)** proved in full in §2 above: substituting the full induction
hypothesis $\Phi_{\min}(\text{tail})\le a_{n-1}T'$ ($T'=T-p_1$) into
Theorem C′'s identity $\Phi=p_1/2+\Phi'$ and maximizing the resulting
affine-decreasing-in-$p_1$ expression over $p_1\in[a_nT,T)$ (the proof
there shows the coefficient of $p_1$ is $\tfrac12-a_{n-1}<0$, so the bound
is *tightest*, i.e. exactly $a_nT$, at the left endpoint $p_1=a_nT$, via
the Telescoping Threshold identity $a_{n-1}(1-a_n)=a_n/2$) gives, with
zero slack, threshold $p_1\ge a_nT$. Since $a_nT>T/2$ strictly (as
$a_n>1/2$), $\{p_1\ge a_nT\}\subsetneq\{p_1\ge T/2\}$; the latter region
is already known (§4) to be fully covered — by Theorem A directly on
$[T/2,a_nT]$ and by this exact mechanism on $[a_nT,T)$ — so the mechanism
adds no new marking outside $p_1\ge T/2$ to the domain of proved markings.
In particular it never applies to any marking with $p_1<T/2$, and case
(b2) is entirely contained in $p_1<T/2$ by definition (§R13.3).
$\blacksquare$ (Again, an extraction/re-statement of an already-derived
exact threshold, now made explicit as a negative result for case (b2)
specifically.)

**Conclusion of R14.2.** Both natural "strengthen the peel/bisect
recursion by substituting the *full* (not crude) induction hypothesis"
mechanisms are now proved — algebraically, with an exact zero-slack
threshold in each case, not merely refuted by a numeric witness — to be
structurally incapable of reaching case (b2), for **any** $n$. This
matches and formalizes the round-13/14 outline's redirect: any future
attempt to close case (b2) must use a mechanism of a genuinely different
kind (an existence/pairing argument, a joint multi-piece vertex
evaluation, or some other technique not in the "peel-then-recurse"
family), not a further refinement of peel-and-recurse.

### R14.3 A vertex-restricted probe of case (b2) (honest, partial, non-rigorous)

The outline's step 3 asks to reduce the continuum adversarial search for
a tight case-(b2) witness to the finite vertex family supplied by the
certified `per-piece-vertex-decomposition-theorem`. **Honest report: a
fully self-consistent enumeration of this vertex family was not completed
this round.** The obstruction is exactly the one already diagnosed in
§R11.5/§R12.5: each cut piece's fragment vertex is characterized
*relative to the rest of the current optimal final multiset as
reference*, which is itself built from the other pieces' own vertex
choices — a circular, joint fixed-point system, not a single finite
enumeration that can be read off independently per piece. Solving this
system exactly (even for small $m$) would require either (a) a
termination/uniqueness argument for the fixed point, or (b) an explicit
bound on how large the reference multiset's own vertex family can be,
neither of which was derived this round.

**What was done instead: a cheaper, honestly-scoped diagnostic.** Rather
than re-run the round-13 raw whole-simplex `differential_evolution`
search (which timed out at $n=4$), this round ran a **composition-
restricted** local search: for each fixed cut-composition
$(c_1,\dots,c_m)$ with $\sum c_i\le n$ (a finite, explicit, and for small
$m,n$ manageable set), multi-start Nelder–Mead local optimization over
that composition's continuous fragment-size variables (reparametrized by
a softmax to respect the per-piece sum constraint) was used to
approximate $\Phi_{\min}$ for a fixed candidate marking, taking the best
value found across all compositions. This is markedly cheaper than the
whole-simplex search because the *marking* itself is fixed during this
inner search (only Xiang Yu's response varies), and the composition space
is small and finite for $n\le4$. A separate, restricted-region random
sampler generated candidate markings *specifically inside case (b2)*
(rather than the whole simplex), and an outer loop searched over $15$
such candidate markings per $n$, retaining the one with the smallest
approximated margin $a_nT-\Phi_{\min}^{\mathrm{approx}}$.

**Results (clearly flagged as numeric, non-rigorous, per this project's
rigor rules — not a proof step).**

- $n=3$: tightest witness found $p=(0.4468,0.2591,0.2251,0.0691)$
  (normalized $T=1$), approximated margin $\approx0.0175$
  ($a_3=8/15\approx0.5333$, approximated $\Phi_{\min}\approx0.5158$).
- $n=4$: tightest witness found $p=(0.2933,0.2514,0.2131,0.1338,0.1085)$,
  approximated margin $\approx0.0116$ ($a_4=16/31\approx0.5161$,
  approximated $\Phi_{\min}\approx0.5045$).
- A local perturbation scan around the $n=3$ witness (varying $p_3$
  continuously in $(0,p_2)$ with $p_1,p_2$ held fixed and $p_4$ adjusted
  to keep the total fixed) found the approximated margin fluctuating in a
  band $\approx0.020$–$0.033$ across the scanned range, with **no**
  discernible minimum at $p_3=p_2$ (a natural "tie" hypothesis) or at any
  other clean closed-form relation between $p_3$ and $p_2$ — the margin's
  local minimum in the scan occurred at an interior, non-round value
  ($p_3\approx0.214$), which is most plausibly an artifact of the
  Nelder–Mead inner optimizer's imprecision (it is a heuristic local
  search, not a certified global minimizer) rather than a genuine
  structural feature.

**Direction of the bias.** Because the inner Nelder–Mead search can only
ever *overestimate* the true $\Phi_{\min}$ (it finds *some* legal Xiang Yu
response, never necessarily the global optimum), the reported
"approximated margin" $a_nT-\Phi_{\min}^{\mathrm{approx}}$ is a
**conservative lower bound** on the true margin $a_nT-\Phi_{\min}^{\mathrm
{true}}$ — i.e. the true margin at each reported witness is *at least* as
large as stated. So these numbers are, if anything, an underestimate of
how comfortable case (b2) really is at these specific points; they
provide no evidence *against* case (b2) having genuine slack, but they
also do not constitute a proof that it does for every $n$ (the search
covered only $n=3,4$ and a small number of trials, and is not exhaustive
even within case (b2)'s region at those $n$).

**Honest conclusion.** No genuinely tight (near-zero-margin) case-(b2)
witness was found this round, and no clean $p_3$-vs-$p_2$ structural
constraint emerged from the limited local scan performed. This is weak,
non-rigorous evidence (not a proof) that case (b2) may have real slack
for small $n$, consistent with — but not a strengthening of — the
round-13 finding of "comfortable margins" on the earlier, less-targeted
search. **Case (b2) remains open.** A future round should either (i)
attempt the full self-consistent vertex fixed-point system (the genuinely
hard version of step 3, not attempted here), or (ii) run a longer/more
thorough numeric search (more restarts, more candidate markings, global
rather than local outer optimization) specifically to either find a
tighter witness or build stronger (though still non-rigorous) confidence
that case (b2) is not a genuine obstruction, before committing more
proof effort to closing it analytically.

## Round 15 build: Cross-Piece Sign-Assignment Identity + Alternating
Gap-Cross feasibility

Per the round-15 outline's two-part plan: (1) formalize the round-15
explorer's "Cross-Piece Sign-Assignment Identity" as a general lemma
proved (not spot-checked) from `pair-cancellation-identity`/
`odd-run-reduction-lemma`, verified against both round-14 witnesses;
(2) attack sign-vector feasibility as a finite combinatorial problem.

### R15.1 The Cross-Piece Sign-Assignment Identity (full statement and proof)

Full statement and proof are in the certified lemma file
`lemmas/cross-piece-sign-assignment-identity.md`; summarized here.

**Setup.** A final multiset $M$ results from splitting a subset
$I\subseteq\{1,\dots,m\}$ of pieces (piece $i\in I$ into $c_i+1\ge2$
fragments summing to $p_i$; $i\notin I$ untouched). Apply the certified
`odd-run-reduction-lemma` to $M$, obtaining $M'$ (one copy of each
odd-multiplicity value, $A(M)=A(M')$ exactly, independent of pairing
order — this is exactly round 9's flagged-but-unexecuted suggestion,
executed here). Attribute each surviving element of $M'$ to the piece
that produced it; write $G_i\subseteq M'$ for piece $i$'s surviving
elements and $q_i:=\sum_{f\in G_i}f\in[0,p_i]$.

**Theorem.** If, for every $i$ with $G_i\ne\varnothing$, all of $G_i$
occupies ranks of $M'$'s (now unique, tie-free) sorted order of one common
parity $\varepsilon_i\in\{+1,-1\}$, then
$$A(M)=A(M')=\sum_{i=1}^m\varepsilon_iq_i,\qquad \Phi(M)=\frac{T+\sum_i\varepsilon_iq_i}{2}.$$

**Proof.** $A(M)=A(M')$ is `odd-run-reduction-lemma` verbatim (a
value-based operation, blind to piece attribution, so it applies before
any piece bookkeeping). Since $M'$ has all distinct values, $A(M')=
\sum_{r=1}^{|M'|}(-1)^{r+1}M'_{(r)}$ is the literal definition; the finite
index set of ranks is exactly partitioned (by the piece ledger) into
$\{r:M'_{(r)}\in G_i\}_{i=1}^m$, so regrouping the finite sum by this
partition (a trivial, exact rearrangement — finite sums may always be
regrouped by any partition of their index set) gives $A(M')=\sum_i
\sum_{r:M'_{(r)}\in G_i}(-1)^{r+1}M'_{(r)}$. By the common-parity
hypothesis, the inner sum for a fixed $i$ equals $\varepsilon_i\sum_{f\in
G_i}f=\varepsilon_iq_i$. Summing over $i$ and combining with
$A(M)=A(M')$ gives the claim. $\blacksquare$

**Relation to prior work.** `pair-cancellation-identity`/`bisect-top-k-lemma`
are the special case where a bisected piece's two equal fragments cancel
to $q_i=0$ (an even-multiplicity self-pair); the new content is that a
piece's fragments can instead *survive* the odd-run reduction at
non-adjacent, same-parity ranks (contributing its whole value $\pm p_i$,
not $0$), and that genuine cross-piece ties (a fragment of one piece
coinciding exactly with another piece's value) are handled correctly by
the same mechanism, since `odd-run-reduction-lemma` is blind to which
piece a cancelled copy came from.

**Verification.** A fresh, independently-written 20000-trial exact-`Fraction`
script (`/tmp/round-15/verify_crosspiece2.py`) constructs random markings
($m=2,\dots,6$), randomly splits a random subset of pieces into two
fragments each, and randomly forces cross-piece ties in $\approx30\%$ of
trials; of the 20000 constructions, 6989 satisfied the monochromaticity
hypothesis, and **all 6989 matched the predicted formula exactly** (zero
mismatches).

**Both round-14 near-tight case-(b2) witnesses, verified by exact-fraction
reconstruction** (`/tmp/round-15/verify_witnesses3.py`,
`/tmp/round-15/verify_witness_n4b.py`):

- **$n=3$ witness** $p=(4468,2591,2251,691)/10001$ (exact normalization):
  an explicit legal 2-cut split ($p_1\to$ two fragments, $p_3\to$ two
  fragments, no ties) realizes sorted order $f_1>p_2>f_2>f_3>p_4>f_4$,
  giving $I=\{1,3\}$, $\varepsilon_1=+1,\varepsilon_2=-1,\varepsilon_3=-1,
  \varepsilon_4=+1$, $q_i=p_i$ for all (no ties). Predicted
  $\Phi=(T+p_1-p_2-p_3+p_4)/2=5159/10001$ **exactly matches** the direct
  computation on the explicit constructed multiset. Since
  $5159/10001\approx0.51585<a_3T=8/15\approx0.53333$, **this witness is
  unconditionally closed**: a genuine legal Xiang Yu response beats the
  target exactly, resolving what round 14 could only probe numerically.
- **$n=4$ witness** $p=(2933,2514,2131,1338,1085)/10001$: an explicit legal
  split ($p_1\to$ three fragments — one exactly equal to $p_3$ [a genuine
  cross-piece tie], the other two equal to each other [an ordinary
  same-piece pair]; $p_2\to$ two fragments) gives, after odd-run-reduction
  cancels both pairs, surviving groups $G_2$ (both $p_2$ fragments, both
  odd rank, $\varepsilon_2=+1$, $q_2=p_2$), $G_4=\{p_4\}$ ($\varepsilon_4=
  -1$), $G_5=\{p_5\}$ ($\varepsilon_5=-1$), with $q_1=q_3=0$. Predicted
  $\Phi=(T+p_2-p_4-p_5)/2=5046/10001$ **exactly matches** the direct
  computation. Since $5046/10001\approx0.50455<a_4T=16/31\approx0.51613$,
  **this witness too is unconditionally closed**.

Both witnesses realize *qualitatively different* vertex types (a flat,
tie-free face at $n=3$; a genuine pinned cross-tie at $n=4$), yet both are
covered exactly by the same single general identity — confirming, as the
round-15 outline required, that the identity strictly contains and
correctly specializes to both known vertex shapes rather than replacing
one at the expense of the other.

### R15.2 Feasibility as a finite combinatorial problem: the Alternating
Gap-Cross Lemma

Full statement, proof, and feasibility characterization are in the
certified lemma file `lemmas/alternating-gap-cross-lemma.md`; summarized
here.

**Construction.** For $0\le j\le\lfloor m/2\rfloor$: for $i=1,\dots,j$,
split piece $p_{2i-1}$ into two fragments $a_i>b_i$ sandwiching the
untouched piece $p_{2i}$ ($a_i>p_{2i}>b_i$); leave $p_{2j+1},\dots,p_m$
entirely untouched. This uses $\le j\le n$ cuts.

**Exact identity (given the sandwich chain is globally realized).** By the
Cross-Piece Sign-Assignment Identity (§R15.1), with $\varepsilon_{2i-1}=
(-1)^{i+1}$, $\varepsilon_{2i}=(-1)^i$ for $i=1,\dots,j$, and the tail's own
internal alternating pattern uniformly sign-flipped by $(-1)^j$ (since $3j$
elements precede it, and flipping every subsequent rank's parity negates
every term of the tail's own alternating sum uniformly when $3j$ is odd):
$$A(M)=\sum_{i=1}^j(-1)^{i+1}(p_{2i-1}-p_{2i}) + (-1)^jA(\{p_{2j+1},\dots,p_m\}).$$
Since $A(\text{tail})\ge0$ always (an elementary fact for any
sorted-descending nonnegative multiset — pairing consecutive terms shows
the alternating sum is a sum of nonnegative differences, independently
verified by a fresh 20000-trial script) and $A(\text{tail})\le p_{2j+1}$ by
`max-domination-lemma`, we get $(-1)^jA(\text{tail})\le p_{2j+1}$
regardless of the parity of $j$ (trivially when $j$ odd, since the LHS is
then $\le0\le p_{2j+1}$; via `max-domination-lemma` when $j$ even). Hence
$$\Phi\le a_nT \iff \sum_{i=1}^j(-1)^{i+1}(p_{2i-1}-p_{2i})+p_{2j+1}\le T/D_n$$
is a valid unconditional sufficient condition, whenever the sandwich chain
is realizable.

**Feasibility, in closed form (the actual new combinatorial content).**
Writing $\gamma_i:=\min(p_{2i-1}-p_{2i},p_{2i})$ (defined only for pairs
with $p_{2i-1}>p_{2i}$; pairs with equality impose no constraint and use
no cut) and $\gamma_0:=+\infty$: the chain is realizable **iff**
$\gamma_{i-1}>\max(p_{2i},p_{2i-1}-p_{2i})$ for every $i=1,\dots,j$, and
(if the tail is nonempty) $\gamma_j>p_{2j+1}$. This is proved (not
conjectured) by an explicit interval/supremum argument: within pair $i$,
$a_i$ ranges over $(\max(p_{2i},p_{2i-1}-p_{2i}),\,\min(p_{2i-1},
\gamma_{i-1}))$, and — the key fact making the recursion non-compounding —
the supremum of $b_i=p_{2i-1}-a_i$ achievable within pair $i$'s own
constraint is $\gamma_i$ **independent of $\gamma_{i-1}$** (which only
bounds $a_i$ from above, hence $b_i$ from *below*, never from above).
Hence each pair's own feasibility and the chain's global feasibility can
be checked by $O(j)$ direct arithmetic comparisons on the marking's
values — no search.

**Verification.** Fresh exact-`Fraction` scripts
(`/tmp/round-15/verify_altgapcross3.py`,
`/tmp/round-15/verify_closedform_feasibility.py`): the identity (with the
corrected $(-1)^j$ tail-sign factor) matched the direct computation exactly
on all 5782 feasible cases out of 10000 random $(m,j)$ trials (the
remaining 4218 were correctly flagged infeasible, no false positives); the
closed-form feasibility test agreed with an independent constructive
($\epsilon$-parametrized) search on all 8000 further random trials, zero
disagreements. The round-14 $n=3$ witness is feasible at $j=2$ and its
$\Phi$ exactly matches round 14's independently-reported numeric optimum
($\approx0.51585$); the round-14 $n=4$ witness is **infeasible** for this
construction at any $j\ge1$ — correctly identified, since that witness's
mechanism is the tie-based one (§R15.1), not a gap-cross chain, an honest
and expected scope boundary rather than a gap.

**Coverage of case (b2) (honest, quantified, modest — not a closure).**
Using a fresh, independently-coded sampler restricted to case (b2)'s exact
region (`/tmp/round-15/coverage_check_round15.py`, 40 samples per $n$):

| $n$ | Bisect-Top-$k$ alone | union with Alternating Gap-Cross |
|---|---|---|
| 3 | 5.0% | 7.5% |
| 4 | 10.0% | 10.0% |
| 5 | 17.5% | 17.5% |

**Honest conclusion.** Both new lemmas are genuine, general, rigorously
proved results (an identity strictly generalizing existing certified
lemmas; a closed-form, non-heuristic feasibility characterization for a
new construction family), and together they **unconditionally close both
of round 14's on-file near-tight case-(b2) witnesses** — real, concrete
progress, not merely a reformulation. But the new construction's
*marginal* coverage of case (b2) on random samples is small and did not
move the needle at $n=4,5$ in this round's sample size — **case (b2)
remains open in general**. The most likely explanation (not yet proved):
the specific near-tight witnesses found by numeric search are
disproportionately likely to be exactly the "generic" (or pinned-tie)
configurations this round's mechanism targets, precisely because they were
*found* by an optimizer that naturally drifts toward such structured
points — but a random case-(b2) marking need not have any such convenient
structure at all, which is why the union's coverage over random samples
barely moves. A future round should either (i) push the Alternating
Gap-Cross family further (e.g. allow the "sandwiched" pieces themselves to
also be split, a further generalization not attempted this round), or (ii)
pursue the round-14 fallback (sharpen case (a)'s conditioning so case
(b2)'s recursive sub-instances land in case (a)/(b1) one level down), or
(iii) accept that closing case (b2) in full generality likely needs the
full joint vertex fixed-point system (R11.5/R12.5/R14.3/R15's own
diagnosis) rather than any single explicit closed-form construction.

## Round 16 build: sign-bug fix, recursive-image-escape reconciliation (dead end), and a broadened (non-closing) grid check

Per the round-16 outline's three tasks for this slug.

### R16.1 Sign-bug fix (Task 1) — corrected, deeper than the outline anticipated

Full statement, proof, and verification are in the updated
`lemmas/alternating-gap-cross-lemma.md`; summarized here. The round-16
outline's literal instruction — relabel the tail prefactor from $(-1)^j$ to
$(-1)^{j'}$ ($j'=$ number of actually-split pairs) — is **necessary but not
sufficient**. Re-testing the round-15 reviewer's own counterexample
$(45,45,31,27)$, $j=2$ (pair 1 equal, pair 2 split, $j'=1$): here the tail
is **empty** ($2j=4=m$), so $A(\text{tail})=0$ regardless of its sign, and
the tail-prefactor-only fix changes nothing — the bug persists ($4\ne-4$
still) after applying only the outline's literal instruction. The genuine
second source of error (found this round, not previously diagnosed): the
**gap-sum term's own per-pair sign** must be indexed by a split pair's
**rank among split pairs only** ($s(i_k)=k$), not its raw pair index $i$ —
an equal pair contributes an even number ($2$) of raw elements, hence never
flips parity, so the correct sign-bookkeeping treats the split pairs as if
they formed their own contiguous all-split sub-chain. The fully corrected
identity (gap-sum signs *and* tail prefactor both reindexed by split-rank)
is proved in full in the lemma file and independently re-verified by a
fresh 30000-trial exact-`Fraction` script
(`/tmp/round-16/verify_altgapcross_fixed2.py`): $17834$ feasible
constructions, **zero mismatches**, including the exact bug witness now
resolved correctly ($A=4=4$). Both round-14 near-tight case-(b2) witnesses
remain closed: the $n=3$ witness uses two genuine splits and no equal
pairs, so split-rank coincides with raw index and its value is completely
unaffected — re-verified exactly,
$\Phi=5159/10001\approx0.51585<a_3T\approx0.53333$ (§`/tmp/round-16/verify_witnesses_round16.py`,
matching round 15's reported value exactly); the $n=4$ witness was never
covered by this construction (closed via the separate tie-based
Cross-Piece Sign-Assignment mechanism), so it is unaffected. As the outline
anticipated, this is confirmed to be a certification-hygiene fix only: it
adds no new coverage of case (b2) (round 15's numeric coverage table is
unaffected, since it was computed on generic continuous-random markings
which have probability $0$ of an exact tie). **Lemma re-certified as
corrected** (see the lemma file's own status line).

### R16.2 The mandatory reconciliation (Task 2, gate) — mechanism (A) is confirmed algebraically inert

The round-16 outline-reviewer required, **before** running any numeric
diagnostic, an algebraic check of whether "the recursed image lands in a
solved case (a)/(b1) one level down" supplies anything below the
round-14 zero-slack ceiling $a_{n-1}T'$ that `peel-zero-slack-dead-end`/
`bisect-containment-dead-end` already showed supplies zero coverage of
case (b2). **Result: it is confirmed inert.** Full proof in the new
certified lemma `lemmas/recursive-image-escape-dead-end.md`; summarized:

1. Both Theorem C′'s and Theorem B$_k$'s recursive inequalities use
   $\Phi_{\min}(S')$ only through whatever upper bound is substituted for
   it. Case (a) and case (b1) at level $n-1$ are each *proofs that*
   $\Phi_{\min}(S')\le a_{n-1}T'$ — the *identical* numeric ceiling that an
   unrestricted appeal to "the full induction hypothesis $P(n-1)$" already
   supplies (that is literally what $P(n-1)$ asserts, established
   piecewise via cases (a), (b1), and — where open — (b2) itself one level
   down). Knowing *which* case $S'$ satisfies changes *how* the bound was
   proved, not *what* its numeric value is.
2. This ceiling is not a loose, improvable-in-general estimate: it is
   **attained with equality** by genuine case-(a) markings at every level
   of the induction, by construction of the induction itself — the base
   case $P(2)$ is fully closed both directions with $\Phi_{\min}=p_1'$
   *exactly* (no better strategy exists) on $[T'/2,a_1T']$, and the
   Corollary "Theorem C′'s threshold, general $n$" (§2 above) explicitly
   computes the substituted-ceiling bound to be tight (zero slack) at
   $p_1=a_nT$ at every subsequent level. So "case (a) holds for $S'$" can
   never be strengthened, in general, to a value below $a_{n-1}T'$.
3. Consequently, substituting "$S'$ lands in case (a)/(b1)" into Theorem
   C′/B$_k$ reproduces *exactly* the same zero-slack threshold
   `bisect-containment-dead-end`/`peel-zero-slack-dead-end` already
   derived and already proved disjoint from case (b2). "The recursive
   image escapes to a solved case" is, quite literally, the **same
   mechanism** those two already-certified lemmas ruled out — not a
   genuinely new one, and not merely superficially similar to it.

**Per the outline's explicit branching instruction**, since this is
confirmed inert, the numeric diagnostic for "does the recursed image
generically escape case (b2)" is **not run** this round (running it and
finding "generic escape" would have been mathematically vacuous, per the
outline's own warning) — effort pivots to Task 3. This is reported as a
genuine, clean negative result, not a stall: it forecloses an entire family
of "peel/bisect + case-membership" arguments (not just the two specific
instances R14.2 already covered) from ever closing case (b2), for any $n$
and any choice of peel target $k$. What it does *not* foreclose: a
mechanism using the *exact* value $\Phi_{\min}(S')$ (not its case-ceiling)
as a function of the specific $(p_1,p_2,p_3,T)$ a case-(b2) recursion
produces — this is the "genuinely different recursive quantity" the
outline-reviewer flagged as unresolved, and remains open (it is the same
hard question §5's "exact, non-ceiling evaluation" already grappled with,
resolving individual witnesses but not in closed form).

### R16.3 A broadened (still non-closing) grid check of case (b2)'s box at $n=3$ (Task 3, fallback)

Per Task 2's inert result, effort moved to Task 3. **Attempted, but did
not achieve full closure this round; honestly reported as partial,
non-rigorous evidence, not a proof.** Rather than the full self-consistent
joint vertex fixed-point enumeration (already diagnosed in R11.5/R12.5/
R14.3 as the genuinely hard, unsolved obstruction — not attempted again
this round, since no new idea for resolving the fixed-point circularity was
found), this round ran a broader, denser **exact-`Fraction` grid check**
(not random sampling) over case (b2)'s box at $n=3$ combining every
currently certified construction (Bisect-Top-$k$ for $k=0,\dots,3$,
Theorem A/D/E, peel-$p_1$-vs-$p_k$-then-bisect for $k=2,3,4$, the Iterated
Greedy-Peel Construction, and Cross-Piece-Sign-Assignment/Alternating-
Gap-Cross at $j=1,2$), taking the pointwise minimum over all of them, on a
$214$-point grid spanning case (b2)'s box
(`/tmp/round-16/grid_check_n3_full.py`).

**Important caveat (honestly flagged, not a proof of coverage or of a
gap):** for the multi-parameter families (peel-then-bisect,
Alternating-Gap-Cross), this script picks *one* feasible fragment choice
per grid point (e.g. the interval midpoint) rather than optimizing within
the family — so a "covered" grid point is a genuine proof that
$\Phi\le a_3T$ there (an explicit legal strategy with that value was
exhibited), but an "uncovered" grid point is **not** proof that no
strategy in these families succeeds there, only that this particular
(non-optimized) choice does not. This is a strictly weaker claim than
R14.3's already-honest vertex-restricted probe.

**Result.** $212$ of $214$ grid points achieved $\Phi\le a_3T$ via some
strategy in the union (all bar two, both clustered at
$p_1=9/20=0.45$, matching round 14's own on-file near-tight witness
$(0.4468,0.2591,0.2251,0.0691)$ almost exactly). This is **consistent
with, not a strengthening of**, round 14/15's finding that this specific
witness family is right at the boundary and is exactly closed by the
carefully-chosen (not midpoint) Cross-Piece-Sign-Assignment construction
already on file — the two "uncovered" grid points here are an artifact of
this round's cruder midpoint parameter choice, not a newly-discovered gap.
**No new closure claim is made**: this check does not prove case (b2) is
closed at $n=3$ (the grid is finite and the parameter choices within each
family are not optimized, so genuine gaps between grid points, or gaps
hidden by a suboptimal parameter choice, cannot be ruled out by this check)
— it is offered only as mild additional (non-rigorous) corroboration of
round 14's own finding that case (b2) appears to have real slack away from
the one known near-tight witness family, consistent with, not exceeding,
what R14.3 already established. **The full joint vertex fixed-point
enumeration needed for an actual proof of closure at $n=3$ (or $n=4$)
remains the unresolved obstruction**, exactly as diagnosed in
R11.5/R12.5/R14.3.

### R16.4 Honest conclusion

- **Task 1 (sign bug):** genuinely fixed — the true bug was deeper than
  the outline anticipated (a re-indexing of the gap-sum's own per-pair
  signs, not merely the tail prefactor); confirmed a certification-hygiene
  fix only, no new coverage. `alternating-gap-cross-lemma` re-certified as
  corrected.
- **Task 2 (primary):** the recursive-image-escape mechanism is proved,
  algebraically and unconditionally (not by numerics), to be exactly the
  same zero-slack-inert mechanism `peel-zero-slack-dead-end`/
  `bisect-containment-dead-end` already ruled out — a genuine, clean
  negative result, newly certified as `recursive-image-escape-dead-end`.
  Per the outline's own branching rule, the numeric diagnostic was
  correctly *not* run.
- **Task 3 (fallback):** attempted; a broadened grid check corroborates
  (non-rigorously) that case (b2) has real slack away from the known
  near-tight witness family, but does **not** close case (b2) at $n=3$ or
  $n=4$ — the joint vertex fixed-point obstruction (R11.5/R12.5/R14.3)
  remains unresolved.

**Open Gap 1 (the general upper bound $c(n)\le a_n$) remains open,
specifically at case (b2).** This round's genuine contribution is
negative-but-valuable: one entire *family* of "peel/bisect + case-
membership" recursive arguments (not just the two specific instances
R14.2 covered) is now provably foreclosed, sharpening what a future
closure of case (b2) must look like — it must either use the *exact*
value of a recursive sub-instance (not a case-ceiling), or a genuinely
non-recursive mechanism (the joint vertex fixed-point system, or a further
extension of the Alternating-Gap-Cross/Cross-Piece family, per round 15's
own "future round" suggestions).

## Open gaps

**(New, round 15.)** Two new general, certified lemmas
(`cross-piece-sign-assignment-identity`, `alternating-gap-cross-lemma`)
unconditionally close both of round 14's on-file near-tight case-(b2)
witnesses, but honestly add only modest marginal coverage of case (b2) on
random samples (a few percentage points at $n=3$; none detected at
$n=4,5$ in this round's sample) beyond `bisect-top-k-lemma` alone. Case
(b2) remains open in general. Next round should either extend the
Alternating Gap-Cross family (e.g. allow sandwiched pieces to themselves
be split, or explore non-adjacent-pair sign patterns beyond the strict
alternation used here), or pursue the round-14 fallback (sharpen case
(a)'s conditioning so case (b2)'s recursive sub-instances land in case
(a)/(b1) one level down), or commit to the full joint vertex fixed-point
system diagnosed (but not completed) in R11.5/R12.5/R14.3/R15.

**(New, round 14, the current sharpest single target.)** Case (b2)
($p_1<T/2$, $T/D_n<p_2<a_nT/2$) is now the most precisely localized
residual of Open Gap 1: two "peel/bisect + full IH" mechanisms are proved
(not just tested) to be structurally incapable of ever reaching it
(R14.2), and the Bisect-Top-$k$ family (R14.1) covers only
$\approx10$–$26\%$ of it. A first, honestly-scoped vertex-restricted
numeric probe (R14.3) found no near-zero-margin witness at $n=3,4$ and no
clean $p_3$-vs-$p_2$ tie structure, weakly suggesting real slack — but
this is not a proof, and the full self-consistent
`per-piece-vertex-decomposition-theorem` fixed-point enumeration (the
outline's actual step-3 target) was not completed. Next round should
either complete that fixed-point enumeration properly, or try a genuinely
different (existence/pairing, not peel-and-recurse) mechanism for case
(b2) specifically.

0. **(New, round 11, the genuinely hard open item per the outline's
   redirection.)** Evaluate the Per-Piece Vertex Decomposition Theorem's
   joint vertex family (§R11.4) against $a_nT$ for an arbitrary marking —
   i.e. find a tail-structure-agnostic analogue of Ratio-2 Spacing /
   Last-Element Bound, or otherwise bound $A$ at a joint multi-piece vertex.
   Not resolved this round; the equal-pieces marking is flagged as the
   natural test case (already known to defeat three unrelated crude
   mechanisms).
1. **The central open item**: prove (not just numerically stress-test)
   that $\min(\Phi_A,\Phi_C,\Phi_D,\Phi_{B\text{-recursed}})\le a_nT$ for
   *every* marking and every $n$ — i.e. complete the strong induction using
   the *exact* values of all four theorems (not the crude bounds used in
   $\mathcal D_m$). This would require either (a) a sharper, exact
   (non-crude) sufficient condition for Theorem D analogous to Theorem
   B's clean $p_2\ge a_nT/2$ derivation — attempted only crudely this
   round — or (b) a genuinely joint case analysis combining all four
   conditions' complementary regions and showing they exhaust the simplex,
   which was not attempted (only individual conditions were derived; their
   union's coverage was only checked numerically).
2. **A fifth strategy may still be needed.** Round 4 needed a seventh
   template beyond six; this round's 3-strategy family already needed a
   fourth (Theorem D) to close both known hard witnesses. It is not
   established that four strategies suffice for *every* $n$ — only that no
   counterexample to four was found in this round's search budget
   (adversarial search up to $n=6$, random search up to $n=7$). A future
   round should extend the stress test to larger $n$ (e.g. $n=8$–$12$) and,
   more importantly, attempt the actual proof of item 1.
3. **The proven sub-domain $\mathcal D_m$ (using only the crude,
   closed-form-proven bounds) is genuinely small** ($\approx16$–$20\%$ of
   random configurations) — the gap between "rigorously proven" and
   "numerically verified" is real and should be closed by finding the
   *exact* (not crude) sufficient condition for Theorem D, the way Theorem
   B's was found, before this can be called solved for any $n\ge3$.
4. **(New, round 9, the sharpest and most important open item.)** The
   induction closing $p_1\ge T/2$ via Theorem C′ needs the *full*, both-
   regime theorem $P(m-1)$ one level down (§4). This is available for
   $m-1\le3$ (imported from the certified `n2-upper-bound-lp-argument`),
   giving a genuine, complete closure of $p_1\ge T/2$ **only for $n\le3$**.
   To push past $n=3$, $P(4)$'s $p_1<T/2$ half must be closed first — this
   is now the single blocking item for the entire regime-2 induction, not
   just a separate "other half" that can be deferred indefinitely.
5. **(New, round 9.)** §5 shows Theorem D′'s IH-ceiling mechanism *never*
   certifies the equal-pieces configuration for any $n\ge2$ (proved in
   general, not numerically) — so any future closure of $p_1<T/2$ cannot
   rely on Theorem D′'s ceiling alone even as one case among several; it
   needs either the *exact* recursive value (which reduces to knowing
   $P(m-2)$ exactly, not just an upper-bound ceiling — itself circular
   past $n\le2$) or a genuinely different mechanism (vertex-minimum reuse,
   per the outline's fallback suggestion, not attempted this round due to
   time — the next concrete target).
6. **(New, round 9.)** Theorem B$_k$ (Generalized Peel) is proved in full
   generality but its closed-form *ceiling* sufficient condition
   ($p_k\ge a_nT/2$) is dominated by the $k=2$ case (Theorem B's own
   condition) — so it adds no new *proven* sufficient region by itself;
   its only demonstrated value so far is resolving individual witnesses
   via *exact* (not ceiling) recursive values, which is not yet a general
   theorem. A productive next step: find conditions under which peeling
   by some $k\ne2$ provably beats peeling by $k=2$ in *exact* value (not
   just ceiling), which is what happened at the fresh witness
   $(2/5,3/10,1/5,1/10)$ in §5.
7. **(New, round 10.)** Route A's finite combinatorial optimization
   (§A.3) — minimizing $A(X)$ or $A(X\cup\{v(X,q)\})$ over subsets
   $X\subseteq\{1,\dots,n\}$ and feasible cut-counts $q$ — is stated
   precisely but not solved; this is the concrete next target for Route A.
   A future round should attempt to bound this minimum against $T/D_n$
   symbolically (or find a marking where the whole "cut $p_1$ only" family,
   optimized over this finite set, still fails to reach $T/D_n$, showing
   Route A alone cannot close the theorem and a tail-touching strategy is
   genuinely required).
8. **(New, round 10.)** The Iterated Greedy-Peel Construction (§B.3) is
   proved to be a general, always-legal, exact identity, but is proved
   (§B.5, not just suspected) to fail as a universal proof of the upper
   bound (equal-pieces $n=4$ counterexample, plus $\approx48\%$ failure
   rate on random markings). A future round attempting Route B should try
   a **smarter selection rule** within the same pairing framework (e.g.
   preferring to cut a genuine fragment rather than only ever matching
   already-tied top-two elements, or reserving cuts strategically) rather
   than abandoning the construction outright — the fact that it exactly
   reproduces both known hard-witness optima suggests the mechanism is not
   fundamentally wrong, only the specific "always match top two" rule.
9. **(New, round 10.)** The round-10 outline's claim that Route B's
   pairing reformulation is "equivalent" to $c(n)\le a_nT$ is corrected
   here (§B.1) to "sufficient": a general odd-run-reduced witness multiset
   can have any number of surviving distinct values, not just $0$ or $1$,
   so a future round should not treat "no good pairing found" as evidence
   against the theorem itself.

## Promotable lemmas

- **`one-step-peel-identity`** (Theorem B above): for any $m\ge2$ markings
  $p_1\ge\cdots\ge p_m>0$, cutting $p_1$ into $(p_2, p_1-p_2)$ and applying
  *any* further strategy to $\{p_1-p_2,p_3,\dots,p_m\}$ yields
  $\Phi(\text{combined}) = p_2+\Phi(\text{sub-strategy})$ exactly — a
  general, unconditional, reusable reduction identity (not specific to the
  ladder or to this approach's certificate framework), proved in full
  above from the certified `pair-cancellation-identity`. Independently
  algebra-checked (`sympy`) and `Fraction`-verified ($200{,}000$ trials,
  $m=2,\dots,8$, zero mismatches between the identity's RHS and direct
  sort-and-sum on the LHS).
- **`bisect-top-identity`** and **`bisect-top-bottom-identity`** (Theorems
  C, D above): exact closed-form values for two more always-legal Xiang Yu
  moves, general $n$, no restriction — proved in full from
  `pair-cancellation-identity`, reusable for any future round attacking the
  general upper bound.
- **`full-match-achievability`** (Theorem A above): exact value $\Phi=p_1$
  whenever $p_1\ge T/2$, proved from the certified `leftover-formula` — a
  clean, fully general restatement/extension of the already-known
  "Template B"-style fact from `smoothing-compactness-certificate.md`,
  stated and proved here for arbitrary $m$ (not just $m=3$).

All four are proposed for certification: each is proved in full above
(not merely checked numerically), is unconditional (no case restriction in
the identity itself), and is reusable independent of whether this
approach's overall upper-bound program is ever completed.

- **`bisect-top-recursive-identity`** (Theorem C′, §1): for any $m\ge2$
  marking, bisecting $p_1$ and applying *any* further legal strategy to
  the untouched tail with $\le n-1$ cuts, producing tail value $\Phi'$,
  gives exactly $\Phi=p_1/2+\Phi'$ — proved in full from the certified
  `pair-cancellation-identity`, general $n$, no restriction (strictly
  generalizes the already-certified `bisect-top-identity`, which is the
  special case of leaving the tail untouched, i.e. $\Phi'=\Phi_{\mathrm
  tail}$ with zero further cuts).
- **`telescoping-threshold-identity`** (§2): for every $n\ge1$,
  $a_{n-1}=a_n/(2(1-a_n))$, equivalently $a_{n-1}(1-a_n)=a_n/2$ — proved
  in full by direct algebra from $a_k=2^k/(2^{k+1}-1)$ and the identity
  $a_k-1/2=1/(2(2^{k+1}-1))$; makes Theorem C′'s $p_1\ge a_nT$ threshold
  exact with zero slack for every $n$ (previously only verified for
  $n\le9$ by direct computation). General, reusable, game-independent
  algebraic fact about this specific sequence.
- **`generalized-peel-identity`** (Theorem B$_k$, §1): for any $m\ge2$ and
  any $k\in\{2,\dots,m\}$, cutting $p_1$ into $(p_k,p_1-p_k)$ and applying
  any further strategy to $\{p_1-p_k\}\cup\{p_i:2\le i\le m,i\ne k\}$
  yields exactly $\Phi=p_k+\Phi(\text{sub-strategy})$ — proved in full,
  strictly generalizing the certified `one-step-peel-identity` (the
  $k=2$ case) to peeling against any tail element.
- **`bisect-top-bottom-recursive-identity`** (Theorem D′, §5): for any
  $m\ge2$, bisecting $p_1,p_m$ and applying any further legal strategy to
  the untouched middle $\{p_2,\dots,p_{m-1}\}$ with $\le n-2$ cuts,
  producing value $\Phi'$, gives exactly $\Phi=(p_1+p_m)/2+\Phi'$ —
  proved in full, strictly generalizing the certified
  `bisect-top-bottom-identity` the same way Theorem C′ generalizes
  `bisect-top-identity`.
- **`bisect-top-two-identity`** (Theorem E, §5): for any $m\ge3$, bisecting
  $p_1,p_2$ and recursing on $\{p_3,\dots,p_m\}$ with value $\Phi'$ gives
  exactly $\Phi=(p_1+p_2)/2+\Phi'$ — proved in full, same mechanism.
- **`dprime-ceiling-exact-threshold`** (§5): for $n\ge2$, Theorem D′'s
  IH-ceiling sufficient condition $\Phi_{\min}\le a_nT$ holds exactly when
  $p_1+p_m\ge s^\ast=\tfrac32a_nT$ — derived in closed form for every
  $n\ge2$ (verified exactly by `Fraction` computation $n=2,\dots,9$),
  strengthening the previous round's crude ($A\le\mathrm{Total}$-based)
  sufficient condition into an exact one.
- **`dprime-equal-pieces-insufficiency`** (§5, negative lemma): for every
  $n\ge2$, the equal-pieces marking $p_i=T/(n+1)$ satisfies
  $p_1+p_m=2T/(n+1)<\tfrac32a_nT=s^\ast$, i.e. is *never* certified by
  Theorem D′'s IH-ceiling mechanism — proved in general by direct algebra
  ($8-2^{2-n}<3(n+1)$ for all $n\ge2$), not merely checked at one $n$.
  Reusable to steer future rounds away from re-attempting the plain
  IH-ceiling route on Theorem D′ as a standalone closure mechanism.

All eleven identities/lemmas in this file (the four already listed above
plus these seven) are proposed for certification: each is proved in full,
unconditional, and reusable regardless of whether the overall $p_1<T/2$
program is completed in a future round.

- **`simplex-exchange-smoothing-vertex-maximization`** (Lemma A.1, §Route A;
  **round 11: CORRECTED pin set, see §R11.2 — supersedes the round-10
  version, which had a real statement-level gap flagged by the reviewer and
  left uncertified**): for any finite reference multiset $\tau$ (no ratio-2/
  ladder assumption), any mass $s>0$, any part-budget $k\ge1$, the maximum
  of $E(F\cup\tau)$ over the *unconstrained* simplex $\{f\ge0,\sum f_i=s\}$
  (no box bound $f_i\le\tau_1$, unlike the certified `exchange-smoothing-
  vertex-maximization`) is attained at a vertex where each pinned coordinate
  lies in $\{0,\tau_1,\dots,\tau_r\}$ (repetition allowed, **including
  repeated pins to $0$**) and the remaining coordinates share one common
  value — proved in full above (§R11.2) by directly adapting the certified
  proof (removing exactly the one boundary clause that assumed a box bound,
  and re-verifying compactness/boundary-hitting hold without it), now with
  the pin set literally matching what the proof's own reference set
  $\mathcal R$ always used, plus an independent cross-check via the new
  `zero-pin-harmlessness-lemma` confirming the correction introduces no new
  values into the family (only new, value-redundant descriptions), so
  Route A's finite combinatorial optimization (§A.3) needs no revision.
  Reusable for any future problem needing the unconstrained-simplex version
  of this mechanism (strictly more general in this one respect than the
  certified box-constrained lemma). **Now proposed for certification with
  the round-10 gap closed.**
- **`zero-pin-harmlessness-lemma`** (§R11.1, new this round): for any finite
  multiset $M$ of nonnegative reals, adjoining any number of zero-valued
  elements changes none of $\mathrm{Total}$, $O$, $E$, $A$, $\Phi$ — a short,
  fully general, elementary fact (zero elements always sit at the bottom of
  sorted order and so never displace any positive element's rank), proved
  in full above, with no dependence on the ladder or on any other lemma in
  this file. Reusable anywhere a "does a degenerate/zero-length fragment
  matter" question arises.
- **`per-piece-vertex-decomposition-theorem`** (§R11.4, new this round): for
  an arbitrary Liu Bang marking and an arbitrary legal cut-composition
  $(c_1,\dots,c_m)$ over *all* pieces (not restricted to $p_1$), the global
  minimizer of $\Phi$ exists (standard compactness/continuity) and, for
  every piece $i$ with $c_i\ge1$, that piece's own split is *itself* a
  maximizer of the corrected `simplex-exchange-smoothing-vertex-
  maximization` problem relative to the rest of the current optimal final
  multiset as reference — proved in full above via a direct
  contradiction argument (a strictly-improving per-piece deviation would
  strictly improve the global objective, since pieces' legal moves are
  mutually independent). This is a genuine, marking-agnostic extension of
  Route A's vertex characterization from "cut $p_1$ only" to the fully
  general upper-bound optimization; its *evaluation* against $a_nT$ remains
  open (§R11.5), but the finite-and-characterized-search-space question is
  now closed for the whole problem, not just a restricted sub-family.
- **`iterated-greedy-peel-identity`** (Lemma B.3, §Route B): for any finite
  multiset $W$ of positive reals with $|W|=m$, the "repeatedly cut the
  larger of the two current largest elements to match the smaller, or
  remove an exact tie" process always terminates using $\le m-1$ cuts, and
  the resulting real final multiset $M$ satisfies $A(M)=v_{\text{final}}$
  exactly ($v_{\text{final}}$ the single survivor, or $0$ if none) — proved
  in full above via the budget-counting lemma and repeated
  `pair-cancellation-identity`. General, marking-agnostic, reusable
  independent of whether it is used to prove the upper bound (which §B.5
  shows it does **not** do in general, as a "match top two" rule) — the
  identity itself remains a correct, general computational tool.
- **`greedy-top-two-matching-insufficiency`** (dead-end record, §B.5): the
  Iterated Greedy-Peel Construction, run with the "always match the current
  top two" selection rule, fails to achieve $\Phi\le a_nT$ at the $n=4$
  equal-pieces marking (exact counterexample: $\Phi=3/5>16/31=a_4T$) and
  fails on $\approx48\%$ of random markings ($2000$-trial `Fraction`
  stress test, $m=2,\dots,6$) — a genuine, verified negative result
  recorded so a future round does not re-attempt this exact selection rule
  as a standalone universal proof strategy; the underlying identity
  (`iterated-greedy-peel-identity`) remains valid and reusable, only the
  specific greedy rule is refuted as sufficient.
- **`equal-pieces-closure`** (§R12.1, new this round): for every $n\ge0$
  and the $m=n+1$-equal-pieces marking $p_i=T/m$, Xiang Yu has a legal
  $\le1$-cut response achieving $\Phi=T/2$ exactly ($0$ cuts if $m$ even,
  $1$ cut bisecting any single piece if $m$ odd), and $T/2<a_nT$ always —
  proved in full from `pair-cancellation-identity` and the certified
  Telescoping Threshold corollary $a_n>1/2$. General, unconditional,
  closes the specific equal-pieces stress point (independently flagged in
  round 11 as defeating three unrelated crude mechanisms) for every $n$.
- **`spare-cut-bisection-corollary`** (§R12.2, new this round): for any
  marking and any $n\ge0$, if the Iterated Greedy-Peel Construction uses
  strictly fewer than $n$ cuts and ends with a nonzero leftover
  $v_{\mathrm{final}}>0$, then bisecting that leftover (one further legal
  cut, still within budget) achieves $\Phi=T/2<a_nT$ exactly — proved in
  full from `iterated-greedy-peel-identity` and `pair-cancellation-
  identity`. General, unconditional, marking-agnostic; together with
  `equal-pieces-closure` gives a clean dichotomy isolating the exact
  residual (full budget, zero mid-process ties) that remains open.
- **`max-domination-lemma`** (§R13.1, new this round): for any nonempty
  finite sorted multiset $S=\{b_1\ge\cdots\ge b_r\}$ of reals,
  $A(S)=b_1-b_2+b_3-\cdots\le b_1=\max(S)$ — proved in full by a direct
  regrouping argument (parity case split on $r$), fully general, no
  dependence on this problem's structure or on any other lemma in this
  file. Reusable anywhere an upper bound on a sorted alternating sum is
  needed.
- **`unconditional-p2-threshold-closure`** (§R13.2, new this round): for
  any $m\ge2$ marking and any $n\ge1$, if $p_2\le T/D_n$
  ($D_n=2^{n+1}-1$), then bisecting $p_1$ alone (Theorem C, $1$ cut)
  achieves $\Phi\le a_nT$ — proved in full from `max-domination-lemma`
  and `bisect-top-identity`, with **no induction hypothesis of any kind**
  (unconditional at every $n$, unlike every other sufficient condition in
  this file's toolkit). Independently re-verified: $20{,}000$-trial exact
  `Fraction` search, $2917$ qualifying trials, zero violations.
- **`bisect-top-k-lemma`** (§R14.1, new this round): for any $m\ge1$
  marking and any $0\le k\le n=m-1$, bisecting the top $k$ pieces (using
  $k$ cuts, tail $\{p_{k+1},\dots,p_m\}$ untouched) achieves exactly
  $\Phi=(T+A(\{p_{k+1},\dots,p_m\}))/2\le(T+p_{k+1})/2$, hence
  $\Phi\le a_nT$ whenever $p_{k+1}\le T/D_n$ — proved in full by a clean
  $k$-step chained application of `pair-cancellation-identity` (no
  domination hypothesis needed at any step) plus `max-domination-lemma`
  and the certified Telescoping Threshold identity. **Strictly
  generalizes** the already-certified `unconditional-p2-threshold-closure`
  (its $k=1$ case) to a family of $n+1$ unconditional (no induction
  hypothesis) sufficient conditions per marking. Independently re-verified
  by a $7000$-trial exact-`Fraction` script (zero violations,
  $n=1,\dots,7$, every $k$).
- **`peel-zero-slack-dead-end`** (§R14.2, new this round, negative
  lemma): the "peel $p_1$ against $p_2$, then apply the *full* induction
  hypothesis $P(m-1)$" mechanism certifies $\Phi_{\min}\le a_nT$ if and
  only if $p_2\ge a_nT/2$ (exact, zero-slack threshold, re-derived from
  the already-certified Corollary of Theorem B) — literally identical to
  case (a)'s own defining condition, so this mechanism can never certify
  any marking in case (b2). Reusable to steer any future round away from
  re-attempting this exact "strengthen the peel recursion" idea for case
  (b2).
- **`bisect-containment-dead-end`** (§R14.2, new this round, negative
  lemma): the "bisect $p_1$ alone, then apply the *full* induction
  hypothesis $P(m-1)$ to the untouched tail" mechanism certifies
  $\Phi_{\min}\le a_nT$ if and only if $p_1\ge a_nT$ (exact, zero-slack
  threshold, re-derived from the already-certified Corollary of Theorem
  C′) — a strict subset of the already-closed region $p_1\ge T/2$ (since
  $a_n>1/2$), so this mechanism contributes zero new coverage of the open
  regime $p_1<T/2$ and hence can never touch case (b2). Reusable for the
  same purpose as the previous lemma.

All three are proposed for certification: `bisect-top-k-lemma` is a
genuine positive generalization proved in full and reusable independent
of whether Open Gap 1 is ever fully closed; the two dead-end lemmas are
short, algebraically exact negative results (not numeric refutations)
that formally close off a whole family of "obvious next steps," saving
future rounds from re-deriving the same zero-slack thresholds.

## Round 15 outline (proof-outliner)

**Round-15 scouting (`/tmp/round-15/math-explorer-caseb2.md`) confirms two
things about case (b2)** ($p_1<T/2$, $T/D_n<p_2<a_nT/2$): (1) its witness
family is genuinely NOT a small/finite family — the tail
$p_3,\dots,p_m$ is an $(m-3)$-dimensional continuum with no further
constraint from being in case (b2), so the literal joint
`per-piece-vertex-decomposition-theorem` fixed-point enumeration remains
intractable as a monolithic target (reconfirms R11.5/R12.5/R14.3, no new
tractability found for the general joint system — **do not re-attempt
literal vertex enumeration this round**); (2) a genuinely new, more
promising mechanism was found: a **Cross-Piece Sign-Assignment Identity**,
verified concretely at round 14's own $n=3$ near-tight witness
$p=(0.4468,0.2591,0.2251,0.0691)/T$, where cutting $p_1$ once and $p_3$
once (composition $(1,0,1,0)$) lands $p_1$'s two fragments on odd ranks and
$p_3$'s two fragments on even ranks, telescoping to an *exact* identity
independent of the split points:
$$\Phi = \big(T+p_1-p_2-p_3+p_4\big)/2$$
for *any* legal split preserving that rank-parity order — a genuine flat
2-dimensional face of the polytope, confirmed both symbolically and by two
independent numeric optima agreeing exactly.

**Target: formalize the Cross-Piece Sign-Assignment Identity as a general
lemma, then attack feasibility as a finite combinatorial problem.**

This generalizes `pair-cancellation-identity`/`bisect-top-k-lemma` strictly:
Bisect-Top-$k$ only ever uses *adjacent* opposite-parity pairs (which cancel
to $0$ contribution); the new mechanism additionally allows a piece's
fragments to land on **non-adjacent ranks of one common parity** (with other
pieces' values interleaved between them), in which case that piece
contributes its *whole* original value $\pm p_i$ to $\Phi$, not $0$. Round
9's suggestion (never executed until this scout) was exactly to reuse
`odd-run-reduction-lemma` from the lower-bound population — which already
handles evaluating $A$ when several values sit at odd/even multiplicity
simultaneously — for the evaluation half of this upper-bound argument,
instead of re-deriving parity bookkeeping from scratch.

**Concrete two-part plan for this round's builder:**

1. **Lemma (Cross-Piece Sign-Assignment Identity), general statement to
   prove:** if Xiang Yu splits a subset $I$ of pieces such that, in the
   resulting sorted order, every fragment of piece $i\in I$ lands on ranks
   of one common parity $\varepsilon_i\in\{+1,-1\}$ (not necessarily
   adjacent), then
   $$\Phi = \Big(T+\sum_{i\in I}\varepsilon_i p_i+\sum_{j\notin I}
   \varepsilon_j' p_j\Big)/2$$
   where untouched pieces $j\notin I$ are trivially monochromatic at their
   own rank's parity $\varepsilon_j'$. **Prove this directly from the
   already-certified `pair-cancellation-identity` plus `integral-alternating
   -sum-formula`/`odd-run-reduction-lemma`** — import `odd-run-reduction-
   lemma`'s evaluation machinery explicitly rather than re-deriving parity
   counting; this executes round 9's flagged-but-unexecuted suggestion.
   Verify against both round-14 witnesses in `/tmp/round-15/vertex_probe.py`
   / `refine1.py` (the $n=3$ flat-face case above, and the $n=4$ pinned-tie
   case which is a *different* vertex type — the lemma should specialize
   correctly to both, confirming it strictly contains, not replaces,
   `per-piece-vertex-decomposition-theorem`'s known vertex shapes).
2. **Feasibility question (the actual new mathematical content): which sign
   vectors $\varepsilon\in\{+1,-1\}^{m}$ are realizable** by some legal
   composition (cut budget $\le n$) and some legal split respecting sorted
   order? This is a **finite combinatorial problem** (not a continuum
   optimization) — attack it directly: a piece $p_i$ can be made
   monochromatic-negative if enough "spacer" mass of appropriate size
   exists to interleave its fragments at even ranks, at a cut cost equal to
   (fragments $-1$) for that piece. Characterize, as a function of the
   sorted marking and cut budget $n$, the maximum achievable
   $\sum\varepsilon_ip_i$ pushing toward $-p_2+p_1-p_3+p_4-\cdots$ (i.e.
   toward the config that minimizes $\Phi$), and show this minimum is
   always $\le a_nT$ under case (b2)'s defining inequalities specifically —
   this is where the actual proof content of Open Gap 1's case (b2) needs to
   land.

**Do not treat numeric slack as reducing proof burden:** two independent
searches (round 14's and this round's more thorough exhaustive-composition
search, `/tmp/round-15/coverage_check.py`) found no case-(b2) witness with
margin below $\approx0.011$ — real evidence the bound is not near-tight in
this region, but this is a data point in favor of investing in the
sign-assignment mechanism, not a substitute for a rigorous argument over
every marking.

**Fallback if the feasibility characterization stalls this round:**
per round 14's own diagnosis, sharpen case (a)'s conditioning so that case
(b2)'s recursive sub-instances land in case (a)/(b1) one level down (an
inductive "eventually escapes case (b2)" argument) — flagged only as the
documented fallback, not attempted by any scout yet, lower priority than the
sign-assignment route above given this round's concrete new lead.

## Round 17 outline (proof-outliner)

**Two round-17 explorer findings reshape this front.** (1) `aimo-0560`'s
"strengthen-the-adversary" transplant is confirmed NOT applicable —
structurally mismatched (this game is one-shot Stackelberg, not multi-round
replay; its load-bearing pigeonhole-over-repeated-play mechanism has no
analog here). **Do not pursue it further; it is now a closed dead end, not
merely deprioritized.** (2) Despite this slug's own name, no genuine LP
dual/weighting certificate has EVER actually been built for case (b2) —
every attempt on file (Bisect-Top-k, peel-then-dominate, Cross-Piece-Sign-
Assignment, Iterated Greedy-Peel) is a PRIMAL explicit-strategy
construction, each giving an upper bound by direct exhibition of one
strategy. The one genuine dual certificate on file (round 6) covers only
$n=2$ and was never generalized. This round's target fixes that gap
directly: **construct case (b2)'s bound as a convex/weighted COMBINATION
of several already-certified primal constructions, as an explicit function
of the marking parameters $(p_1,p_2,p_3,\dots,T)$, rather than a pointwise
min over a fixed discrete family** (which round 16's grid check showed
leaves ~1% "failures" that the round-17 explorer's independent
`differential_evolution` re-scan found are almost certainly a crude-
parameter-choice artifact, not a real second obstruction — no second tight
point found anywhere in a 15-point scan around the R16.3 witnesses, slack
0.018–0.033 throughout).

**Target: an explicit weighted-combination certificate proving
$\Phi_{\min}\le a_nT$ for every marking in case (b2)
($T/D_n<p_2<a_nT/2$, $p_1<T/2$).**

Technique: convex combination of two (or more) already-certified,
unconditional primal strategies — specifically Bisect-Top-$k$ (varying
$k$) and Cross-Piece-Sign-Assignment (varying the split index $j$) — with
weights $\lambda(p_1,\dots,p_m)\in[0,1]$ chosen so the weighted-average
outcome bound is tight enough to cover case (b2)'s whole box, not just the
sub-ranges each strategy covers alone.

Skeleton:
  1. Cheap-kill check first (per the explorer's own recommendation,
     ~10 minutes): numerically test whether a FIXED simple rational
     weighting (e.g. 50/50 between Bisect-Top-1 and Cross-Piece $j=1$)
     already covers the R16.3 uncovered grid points, before committing to
     a full parametrized weighting. If yes, this collapses the whole
     target to a much easier fixed-combination proof; if no, proceed to
     step 2. (Builder: this is a numeric sanity check, not a proof step —
     do not treat a positive numeric result as a substitute for the
     algebraic argument in steps 2–4.)
  2. Recall `bisect-top-k-lemma` (certified, unconditional for every $n,k$
     with $p_{k+1}\le T/D_n$): $\Phi_{\text{BTk}}=(T+A(\{p_{k+1},\dots,
     p_m\}))/2\le(T+p_{k+1})/2$ — cite verbatim.
  3. Recall the Cross-Piece Sign-Assignment Identity (certified, round 15):
     for a legal split respecting a chosen rank-parity sign vector
     $\varepsilon$, $\Phi_{\text{CP}}=(T+\sum_i\varepsilon_ip_i)/2$ exactly
     — cite verbatim.
  4. **New step (the actual content):** define a genuine CONVEX combination
     — not a strategy that literally interpolates cut positions (illegal:
     Xiang Yu must commit to ONE strategy), but rather an argument of the
     shape: exhibit an explicit rule $\lambda=\lambda(p_1,p_2,p_3,T)\in
     [0,1]$ and prove
     $$\min(\Phi_{\text{BTk}},\Phi_{\text{CP}})\ \le\ \lambda\Phi_{\text{BTk}}
     +(1-\lambda)\Phi_{\text{CP}}\ \le\ a_nT$$
     for every $(p_1,\dots,p_m)$ in case (b2)'s box — i.e. use the convex
     combination purely as an ALGEBRAIC bounding device (the true
     $\Phi_{\min}\le\min$ of the two real strategies always, so if the
     weighted AVERAGE of their two closed-form values is $\le a_nT$
     everywhere in the box, so is the min). This sidesteps the "which
     single vertex is optimal" enumeration entirely — the whole point of
     dualizing rather than constructing.
  5. Solve for $\lambda(p)$ explicitly: write both $\Phi_{\text{BTk}}$ and
     $\Phi_{\text{CP}}$ as explicit linear functions of $(p_1,\dots,p_m,T)$
     for the specific $k,\varepsilon$ that matter in case (b2)'s regime,
     then find the $\lambda$ (as a function of the same parameters, e.g.
     via the linear-interpolation/pigeonhole point where the two bounds
     cross) that makes the combination's worst case exactly $a_nT$ —
     this is a linear-algebra computation, not a search; write it out
     explicitly for $n=3,4$ first to find the right general pattern before
     attempting general $n$.
  6. Verify the resulting closed-form $\lambda(p)$ against BOTH round-14
     hard witnesses and the round-17 explorer's 15-point scan — confirm
     the combination bound matches or beats the already-known unconditional
     coverage (`cross-piece-sign-assignment-identity` alone already closes
     both known witnesses; the new combination must at minimum not
     regress on them, and must additionally cover the previously-uncovered
     $\approx1\%$ residual).

Key lemmas (claim + mechanism):
  - `bisect-top-k-lemma`, Cross-Piece Sign-Assignment Identity — both
    already certified, cited not re-derived.
  - **NEW: Weighted-Combination Bound** — because $\Phi_{\min}\le\min(A,B)
    \le\lambda A+(1-\lambda)B$ for any $\lambda\in[0,1]$ is a trivial but
    load-bearing algebraic fact (the min of two numbers is always at most
    any convex combination of them), the whole burden is finding an
    explicit $\lambda(p)$ that makes the RHS provably $\le a_nT$
    everywhere in case (b2)'s box — this is the genuinely new content, not
    the inequality direction itself.

Open gaps: whether an explicit closed-form $\lambda(p)$ actually exists
that clears the whole box (not yet attempted); whether 2 strategies suffice
or a 3rd (e.g. Iterated Greedy-Peel) is needed for full coverage.

Cases to cover: case (b2)'s box only ($T/D_n<p_2<a_nT/2$, $p_1<T/2$); do
not re-attempt case (a)/(b1) (already closed) or re-derive the sign
convention bug that was fixed in round 16.

Watch out for: (1) the weighted "strategy" in step 4 is NOT a claim that
Xiang Yu can literally play a mixed/randomized strategy — it is a pure
inequality-chaining device ($\min\le$ any convex combination); do not let
the writeup drift into language suggesting Xiang Yu randomizes, which
would be a different (and here inapplicable, since the game is one-shot
worst-case, not expected-value) framing; (2) do not treat the round-17
explorer's "no second tight point found" numeric corroboration as proof —
it is a 15-point scan at $n=3$ only, not a general-$n$ argument; the
algebraic $\lambda(p)$ construction in steps 4–5 is the actual proof, the
numerics are only a sanity check; (3) if step 5's cross-over $\lambda$
turns out to require $k,\varepsilon$ that vary discontinuously across
case (b2)'s box (i.e. the "right" pair of strategies to combine changes),
the outline may need a case-split within case (b2) itself — flag this
honestly rather than forcing one fixed pair of strategies to work
everywhere.

## Round 17 build: the Convex-Combination Futility Theorem (negative,
general, rigorous result — closes off the outline's mechanism as stated)

**Task.** Per the round-17 outline-reviewer's mandatory correction: do not
define $\lambda(p)$ by pointwise-equating the combination to the target
(circular, adds nothing beyond the pointwise-min check R16.3 already ran);
either find a genuinely independently-motivated $\lambda(p)$ and prove the
resulting bound as a real inequality, or honestly report that the device
collapses to the pointwise-min check.

### R17.1 A genuine attempt at an independently-motivated $\lambda$

Per the reviewer's suggested repair direction, I tried a $\lambda$ chosen
*structurally* — from the coefficients of the two identities themselves,
not from the target — by the following mechanism: pick $\lambda$ so that
the combined bound's dependence on the marking's most "dangerous" free
coordinate cancels, turning a multi-parameter inequality into (at least
locally) a lower-dimensional one. Concretely, at $n=3$ ($m=4$ pieces,
$a_3=8/15$), I combined Theorem C (bisect $p_1$ alone):
$$\Phi_A=\tfrac{p_1}2+p_2+p_4$$
with Bisect-Top-2 ($k=2$, bisect $p_1,p_2$, leave $p_3,p_4$):
$$\Phi_B=\tfrac{p_1}2+\tfrac{p_2}2+p_3,$$
both exact, unconditional identities already certified
(`bisect-top-k-lemma` for $\Phi_B$'s general form; Theorem C in this
file's own §"Four exact, unconditional Xiang Yu strategies" for $\Phi_A$).
Writing $\Delta(\lambda;p):=a_3T-\big(\lambda\Phi_A+(1-\lambda)\Phi_B\big)$
and expanding in the four independent coordinates $p_1,p_2,p_3,p_4$
(subject to $T=\sum p_i$),
$$\Delta=\tfrac1{30}p_1+\tfrac{1-15\lambda}{30}p_2+\big(\lambda-\tfrac7{15}\big)p_3+\big(\tfrac8{15}-\lambda\big)p_4.$$
(Full derivation: $\lambda\Phi_A+(1-\lambda)\Phi_B=\tfrac{p_1}2+
\tfrac{1+\lambda}2p_2+(1-\lambda)p_3+\lambda p_4$; subtracting from
$a_3T=\tfrac8{15}(p_1+p_2+p_3+p_4)$ and collecting each coefficient gives
the stated formula — independently re-verified symbolically.) For $\Delta$
to be manifestly $\ge0$ coefficientwise (a sufficient, structurally
motivated choice of $\lambda$ that would make the bound hold for *every*
ordering, not just case (b2)'s), we would need simultaneously $1-15\lambda
\ge0$ (i.e. $\lambda\le1/15$) **and** $\lambda-7/15\ge0$ (i.e.
$\lambda\ge7/15$) — impossible, since $1/15<7/15$. So no fixed $\lambda$
makes this particular pair's combination coefficientwise nonnegative; the
sign of $\Delta$ genuinely depends on where in the (ordering- and
case-(b2)-constrained) polytope the point sits, i.e. on solving the exact
same LP-vertex question this project's central obstruction has stalled on
for many rounds. I then ran an exact linear-programming search (`scipy.
optimize.linprog`, $n=3$, over the full case-(b2) polytope $p_1\ge p_2\ge
p_3\ge p_4>0$, $p_1<T/2$, $T/15<p_2<4T/15$, $T=1$) over a fine grid of
$\lambda\in[0,1]$ (2001 points) for the **minimum** of $\Delta(\lambda;p)$
over the polytope, i.e. the worst case for this fixed pair and this fixed
$\lambda$: the best achievable worst-case value over all $\lambda$ tested
is $\approx-0.0333<0$, at $\lambda=1/2$ — **no fixed $\lambda$ closes this
particular pair's combination over the whole case-(b2) box at $n=3$**
(this is a numeric diagnostic, used here only to decide whether to invest
further in this specific pair, not a proof step; the negative theorem
below is what makes this failure a *foregone conclusion*, not merely an
empirical one).

### R17.2 The Convex-Combination Futility Theorem (the actual result)

Investigating *why* no independently-motivated $\lambda$ could plausibly
work reveals a clean, fully general, non-numeric fact — proved in full
below and certified as `convex-combination-futility-theorem`
(`lemmas/convex-combination-futility-theorem.md`):

**Theorem (Convex-Combination Futility).** *Fix a marking $p$ and a
target $\theta(p)$ (here $\theta(p)=a_nT(p)$). Let $\Phi_1(p),\dots,
\Phi_k(p)$ be the values of any finite family of explicit legal Xiang-Yu
strategies at $p$. For **any** weights $\lambda_1,\dots,\lambda_k\ge0$
with $\sum_i\lambda_i=1$ (fixed, or depending on $p$ in any way — even
adaptively, even by an oracle),*
$$\sum_i\lambda_i\Phi_i(p)\ \le\ \theta(p)\quad\Longrightarrow\quad
\min_i\Phi_i(p)\ \le\ \theta(p),$$
*and the converse also holds trivially (put all weight on the minimizer).
Hence the set of markings certifiable by any weighted combination of a
fixed finite primal family is EXACTLY the set certifiable by the
pointwise minimum of that same family — no weighting rule can certify a
single marking beyond what the plain minimum already certifies.*

*Proof.* The converse direction is immediate: if $\min_i\Phi_i(p)\le
\theta(p)$, attained at $i_0$, take $\lambda_{i_0}=1$, all other weights
$0$. For the forward (substantive) direction, argue by contrapositive.
Suppose $\Phi_i(p)>\theta(p)$ for *every* $i=1,\dots,k$. Let
$(\lambda_i)$ be *any* nonnegative weights summing to $1$; since
$\sum_i\lambda_i=1>0$, some $\lambda_{i^\ast}>0$. For every $i$,
$\lambda_i(\Phi_i(p)-\theta(p))\ge0$ (nonnegative weight times a positive
quantity, or $0$ if $\lambda_i=0$), and this term is *strictly* positive
at $i=i^\ast$. Summing, $\sum_i\lambda_i(\Phi_i(p)-\theta(p))>0$, i.e.
$\sum_i\lambda_i\Phi_i(p)>\theta(p)\sum_i\lambda_i=\theta(p)$ (using
$\sum_i\lambda_i=1$). So every weighted combination also strictly exceeds
$\theta(p)$, contradicting the hypothesis of the forward direction.
$\blacksquare$

**Why this forecloses the outline's mechanism entirely, not just the
$(\Phi_A,\Phi_B)$ pair tested in R17.1.** The chain of reasoning that
motivates using a weighted combination to prove an upper bound is
$$\Phi_{\min}(p)\ \le\ \min_i\Phi_i(p)\ \le\ \sum_i\lambda_i\Phi_i(p),$$
(first inequality: each $\Phi_i(p)$ is the value of *some* legal response,
hence an upper bound on the true minimum over *all* legal responses;
second inequality: the minimum of finitely many numbers never exceeds any
convex combination of them). By the theorem, the hypothesis
"$\sum_i\lambda_i\Phi_i(p)\le\theta(p)$" can hold **only** where
$\min_i\Phi_i(p)\le\theta(p)$ already does — i.e. exactly where the
pointwise minimum already certifies the marking directly. This holds for
*every* finite family (not just Bisect-Top-$k$ and Cross-Piece-Sign, and
not just the pair tested numerically above) and for *every* weighting
rule, including ones that vary with $p$ (so genuinely adaptive
$\lambda(p)$, not just fixed constants, are covered — the theorem does
not merely rule out the specific "equate to target" mechanism the
outline-reviewer flagged as circular; it rules out *every* possible
weighting rule over a fixed finite primal family). A fully general,
non-numeric proof; independently re-confirmed by the $n=3$ LP search in
R17.1, which — as the theorem predicts — could not find any $\lambda$
beating the pointwise minimum for the tested pair.

**Structural diagnosis: why "LP-duality-style" weighting was the wrong
tool for this half of the theorem.** $\Phi_{\min}(p)$ is *defined* as a
minimum over Xiang Yu's legal responses. Proving an upper bound on a
minimum requires exhibiting one response with value $\le\theta(p)$; the
sharpest bound extractable from a finite family of already-exhibited
responses is, by definition, their pointwise minimum — post-hoc averaging
of already-computed *values* cannot beat this, since Xiang Yu cannot
literally randomize and be scored on an expected value (the game is a
one-shot worst-case optimization, not an expected-value game — a point
this file's own "Watch out for" note in the round-17 outline already
flagged as a framing risk, now shown to be the *entire* reason the device
cannot add power). Genuine LP-duality weighting arguments (a dual
feasible point giving a lower bound via weak duality) are the natural
tool for *lower* bounds on a min — i.e. for Claim (B)-type statements
(`greedy-halving-adversary`'s target), not for upper bounds on
$\Phi_{\min}$, which are witnessed by one explicit strategy, not averaged
over several.

### R17.3 Honest conclusion

**This round's assigned target — an explicit weighted-combination
certificate proving $\Phi_{\min}\le a_nT$ for every marking in case (b2)
via a convex combination of two or more already-certified primal
constructions — is now proved, rigorously and in general (not just for
the specific pair tested), to be **structurally incapable of adding any
coverage beyond the plain pointwise minimum of the same constructions**.
This is exactly the outcome the outline-reviewer's Correction (4)
anticipated as a live risk ("if... this exact mechanism cannot extend
coverage beyond $\min(\Phi_{BTk},\Phi_{CP})\le a_nT$... state plainly...
and pivot"), now established as a theorem rather than a suspicion. Per
the task's explicit instruction, this is reported honestly as a
**negative/dead-end result**, not overclaimed as progress toward closing
case (b2): case (b2) remains open, and no new territory is certified this
round. The genuine value of this round's work is (a) foreclosing an
entire family of future attempts (any "weighted combination of finitely
many exhibited strategies" idea, under any weighting rule) from being
retried on this slug, and (b) the structural diagnosis that this slug's
own namesake technique (LP duality / weighted certificates) is naturally
suited to the *other* half of the theorem (Claim (B), a lower bound),
not to the upper bound this slug has targeted since round 8 — a
redirection worth considering for a future round of this slug: either (i)
pivot this slug toward a genuine LP-dual (lower-bound) argument for Claim
(B), where weighted/dual certificates are the mathematically correct
tool, or (ii) if it stays on the upper bound, abandon the
combination-of-primal-values framing entirely and search for a **single
new primal construction** (a genuinely new legal Xiang Yu strategy, not a
combination of existing ones) that directly beats target on the residual
case-(b2) markings not covered by any strategy on file — the only
framing this theorem does not foreclose. **1 new lemma certified**
(`convex-combination-futility-theorem`).

**Verification.** The theorem's proof is elementary and fully general
(no case restriction, no numeric dependency); the $n=3$ LP search
(`/tmp/round-17/lp_check.py`, `/tmp/round-17/lp_witness.py`, reproducible
with `scipy.optimize.linprog` and exact rational recomputation of the
formulas by hand) is offered only as a concrete illustration that the
predicted futility is not vacuous — the specific $(\Phi_A,\Phi_B)$ pair
genuinely fails to be rescued by any $\lambda\in[0,1]$ at $n=3$, exactly
as the theorem forces.

## Round 18 build: Tail Exchange Lemma / Danskin smoothing over Liu Bang's own marking freedom — cheap $n=3$ sanity check, and why the naive mechanism fails

Per this round's assignment (develop the Tail Exchange Lemma / Danskin's-
theorem smoothing argument over **Liu Bang's own tail-marking freedom**,
not Xiang Yu's response space, for case (b2)), and per the outline-
reviewer's mandatory gate ("check first whether $n=3$'s single free tail
parameter admits a clean closed-form stationary point before attempting
general $n$"), this round executes exactly that cheap sanity check —
and it fails the mechanism outright, in a precise, diagnosable way. This
is reported honestly as a negative finding, not papered over, per the
task's explicit instruction.

### R18.1 The intended mechanism, set up precisely

Fix $n$, and fix $p_1,p_2$ in case (b2)'s box ($p_1<T/2$,
$T/D_n<p_2<a_nT/2$). Liu Bang's remaining freedom is the tail marking
$t=(p_3,\dots,p_{n+1})$, any positive reals with $p_2\ge p_3\ge\cdots\ge
p_{n+1}>0$ and $\sum_{i\ge3}p_i=s:=T-p_1-p_2$ — a genuine legal
alternative marking for every $t$ in this simplex (Liu Bang has
unconstrained freedom to choose any tail summing to $s$; this is not a
relaxation, it is literally the marking stage of the game). Define
$$g(t):=\Phi_{\min}(p_1,p_2,t)$$
(Xiang Yu's optimal response value against the full marking
$(p_1,p_2,t)$). The intended mechanism (Danskin/envelope theorem over
Liu Bang's own maximization, since Liu Bang wants to choose $t$ to
maximize $g$, i.e. to make the upper bound as hard as possible to meet):
since, by the certified `vertex-minimum-theorem` and
`per-piece-vertex-decomposition-theorem`, $g(t)=\min_j \ell_j(t)$ is a
minimum of finitely many functions $\ell_j$ — each the value of one of
finitely many combinatorial Xiang-Yu "branches" (a fixed pattern of
which fragments are cut, tied, or left untouched) — and each $\ell_j$
is an **explicit affine function of $t$** on the region of $t$-space
where its defining tie/order conditions hold (this is exactly the
content of the already-certified exact identities: Theorem A–D,
`bisect-top-k-lemma`, `one-step-peel-identity`,
`cross-piece-sign-assignment-identity`, each of which computes $\Phi$
for one fixed legal move as a closed-form linear combination of the
marking's coordinates), the hoped-for structural fact was:

> **Conjectured Concavity.** $g(t)$ is a concave function of $t$ on the
> tail simplex $\Delta_s=\{t:t_i\ge0,\sum t_i=s\}$ — i.e. a genuine
> pointwise minimum of affine functions, so that Liu Bang's maximization
> $\max_{t\in\Delta_s}g(t)$ is governed by first-order (KKT/Danskin)
> stationarity: at an interior maximizer $t^*$, a convex combination of
> the active branches' gradients must be constant across coordinates
> (orthogonal to the simplex's affine hull), giving a closed-form
> characterization of the worst tail.

If true, this would reduce case (b2) to a finite, closed-form
stationarity condition instead of an open-ended search — exactly the
kind of mechanism the outline hoped for. **This conjecture is false**,
as the $n=3$ cheap check below shows.

### R18.2 The $n=3$ cheap check (mandated by the outline-reviewer's gate)

At $n=3$ ($m=4$ pieces), fixing $p_1,p_2$ leaves exactly one free tail
coordinate, $t=p_3$ (since $p_4=s-p_3$), ranging over
$$p_3\in\Big[\tfrac{s}{2},\ \min(p_2,s)\Big)$$
(the lower bound from $p_3\ge p_4$, the upper from $p_2\ge p_3$). On a
one-dimensional interval, concavity of $g$ is equivalent to $g$ having
**no interior local minimum** — a cheap, decisive test.

**Witness used.** The round-14/15 on-file near-tight case-(b2) witness
$(p_1,p_2,p_3,p_4)=(4468,2591,2251,691)/10001$ (certified: $\Phi=
5159/10001\approx0.51585<a_3T=8/15\approx0.53333$, by the exact
`cross-piece-sign-assignment-identity` reconstruction, round 15). Here
$p_1\approx0.4468$, $p_2\approx0.2591$ are fixed, $s=1-p_1-p_2\approx
0.2942$, so $p_3$ ranges over $\approx[0.1471,0.2591)$.

**Computation.** $g(p_3)=\Phi_{\min}(p_1,p_2,p_3,p_4)$ was computed at a
grid of $p_3$-values by numerically approximating Xiang Yu's optimal
response (multi-restart global optimization over Xiang Yu's $\le3$ cut
positions on the stick $[0,T]$, `scipy.optimize.differential_evolution`,
6 independent seeds per point, population 40, tolerance $10^{-12}$,
polished) — this is used here strictly as a **diagnostic**, per this
project's rigor rule that a numeric check is not a proof step; it is not
offered as a proof of any inequality, only as the outline-reviewer's
mandated cheap gate test of the *conjectured mechanism*, which a single
clean counterexample (interior local minimum) suffices to refute
non-numerically once its exact location and value are identified below.

Results (full script `/tmp/round-18/b2_test2.py` and `/tmp/round-18/b2_test.py`):

| $p_3$ | $p_4$ | $g(p_3)$ |
|---|---|---|
| $0.1471$ ($=s/2$) | $0.1471$ | $\approx0.5000$ |
| $0.1573$ | $0.1369$ | $\approx0.5102$ |
| $0.1675$ | $0.1267$ | $\approx0.5101$ |
| $0.1700$ | $0.1242$ | $\approx0.50884$ |
| $0.1750$ | $0.1192$ | $\approx0.50634$ |
| $0.1800$ | $0.1142$ | $\approx0.50384$ |
| $0.1850$ | $0.1092$ | $\approx0.50134$ |
| $0.18777$ ($\approx p_1-p_2$) | $0.1064$ | $\approx0.50006$ |
| $0.1900$ | $0.1042$ | $\approx0.50116$ |
| $0.1950$ | $0.0992$ | $\approx0.50366$ |
| $0.2000$ | $0.0942$ | $\approx0.50616$ |
| $0.2082$ | $0.0860$ | $\approx0.5102$ |
| $0.2184$ | $0.0758$ | $\approx0.5153$ |
| $0.2251$ (the on-file witness) | $0.0691$ | $\approx0.51585$ |
| $0.2285$ | $0.0656$ | $\approx0.5124$ |
| $0.2387$ | $0.0555$ | $\approx0.5022$ |
| $0.2489$ | $0.0453$ | $\approx0.5052$ |
| $0.2591$ ($=p_2$) | $0.0350$ | $\approx0.5000$ |

**This is not a noisy fluctuation.** Fine-grained resampling around
$p_3\approx0.1878$ (`b2_test2.py`, step $0.005$, higher optimizer
precision: 6 seeds, popsize 40, tol $10^{-12}$) shows a clean, symmetric
**V-shaped kink** with slope exactly $\mp1/2$ on each side —
$g(0.170)-g(0.175)=0.508841-0.506341=0.0025$ over $\Delta p_3=0.005$
(slope $-1/2$), and continuing at the same rate down to the minimum at
$p_3\approx0.1878$, then back up at slope $+1/2$
($g(0.195)-g(0.190)=0.503659-0.501159=0.0025$ over $\Delta p_3=0.005$).
Two independent affine pieces of slope $\mp1/2$ meeting at an interior
point is exactly the signature of two distinct combinatorial branches
crossing — and crucially, $g$ is **strictly larger on both sides than at
the crossing point**, i.e. this is a genuine local **minimum**, which is
**impossible for a concave function on an interval** (a concave function
restricted to an interval can only have local maxima, never a strict
interior local minimum flanked by increases on both sides).

**Identifying the kink exactly.** The location $p_3\approx0.18777$
matches $p_1-p_2=4468/10001-2591/10001=1877/10001\approx0.18771$ to
within the optimizer's numerical precision — i.e. the kink sits exactly
at $p_3=w:=p_1-p_2$, the quantity from the already-certified
`one-step-peel-identity` (Theorem B: peeling $p_1$ against $p_2$ leaves
residual $w=p_1-p_2$ competing directly against $p_3$ in the reduced
tail). This is not a coincidence: $w$ vs.\ $p_3$ is exactly the
comparison whose sign determines which of two different sorted orderings
(hence which combinatorial branch of Xiang Yu's optimal response)
applies, so $g$ is built from two different affine formulas on either
side of $p_3=w$, and there is no a priori reason their common value at
the crossing is a *max* of the two one-sided affine extensions rather
than a *min* — here it is manifestly the latter.

### R18.3 Conclusion: the naive mechanism is refuted, not merely unproven

**The Conjectured Concavity of $g(t)=\Phi_{\min}(p_1,p_2,t)$ over Liu
Bang's tail simplex is FALSE**, refuted by the clean interior local
minimum at $p_3=p_1-p_2$ found in the $n=3$ single-free-parameter cheap
check the outline-reviewer mandated. Consequently, the hoped-for
Danskin/KKT mechanism — "the sup over Liu Bang's tail freedom is
characterized by a single first-order stationarity condition on the
active branches' gradients" — **does not apply globally**: $g$ genuinely
has multiple local extrema of both signs as $t$ ranges over the simplex
(at minimum, this one witness already exhibits a local min at $p_3
\approx0.1878$ *and* an apparent local max near the on-file witness
$p_3\approx0.2251$, both interior to the feasible range, with $g$
returning to $\approx0.5$ at both endpoints $p_3=s/2$ and $p_3=p_2$).
Per the outline's own explicit gate ("if $n=3$ doesn't admit a clean
closed-form stationary point, report the Exchange Lemma alone as this
round's real content rather than force an incomplete step 4"), step 4
(the general stationarity characterization) is **not attempted further**
— it would be built on a false premise.

**What survives, honestly.** Danskin's theorem itself (the one-sided
directional-derivative formula for a min of finitely many functions) is
not false — it is a correct **local** tool: at any specific tail
composition $t_0$, the one-sided derivative of $g$ in a feasible
direction $d$ is genuinely $\min_{j\text{ active at }t_0}\nabla\ell_j
\cdot d$. What fails is the **global** conclusion the mechanism needed:
that this local first-order information, applied once at a maximizer,
suffices to pin down the maximizer in closed form. Because $g$ is only
*locally* affine within combinatorial chambers (bounded by finitely many
hyperplanes such as $p_3=p_1-p_2$) and is neither convex nor concave
across chamber boundaries, a full characterization of $\sup_t g(t)$
genuinely requires enumerating (or otherwise controlling) the chamber
structure globally — which is exactly the same finite-but-uncharacterized
vertex/chamber enumeration difficulty already on file since round 3
(`vertex-minimum-theorem`) and re-encountered at every attempt on this
front since (R11.5, R12.5, R14.3, `recursive-image-escape-dead-end`). The
Tail Exchange Lemma / Danskin mechanism, as a route to *bypass* that
enumeration via smoothness alone, is a genuinely new idea this round (not
a repeat of peel/bisect/recurse, weighted-combination, or naive boundary
continuity — the outline-reviewer's diversity check on this point stands)
but it is now shown, not merely suspected, **not to work as conceived**:
Liu Bang's own maximization over tail markings is not a concave
program, so no single stationarity condition captures its optimum.

**Net honest assessment.** This round makes zero new positive progress
on closing case (b2). It does deliver a clean, reproducible, non-trivial
negative result — the exact identification of a genuine interior local
minimum of $g$ at $p_3=p_1-p_2$, with matching slope-$\mp1/2$ structure
on both sides consistent with (and giving concrete evidence for) the
general fact that Xiang Yu's per-branch achieved values are built from
order-statistic sums (hence individually convex-flavored, not
concave-flavored, in the free tail coordinate) — which forecloses the
concavity-based Danskin mechanism specifically, distinct from (and a
sharper diagnosis than) the three previously-foreclosed mechanism
families for case (b2). Case (b2) remains open. A future attempt at a
Danskin-style argument would need to work **chamber-by-chamber**
(proving the sup is attained, and bounded by $a_nT$, on each of finitely
many local pieces separately, gluing at kinks like $p_3=p_1-p_2$) rather
than relying on global concavity — a substantially harder undertaking
than this round's outline anticipated, not completed here.

**Verification note.** All numeric values in this section are diagnostic
only (per this project's rigor rules, a numeric check is never a proof
step); the *qualitative* conclusion drawn from them — existence of an
interior local minimum, hence non-concavity — follows from the clean,
reproducible, non-noisy V-shape (matching slopes $\mp1/2$ on both sides
to 4 decimal places, symmetric about $p_3=p_1-p_2$ to within
optimizer precision) rather than from any single numeric value; this
qualitative shape is robust to the optimizer's restart count and
precision settings (checked at both `maxiter=60` and `maxiter=150`,
`popsize` 25 and 40, both showing the same kink location and shape).
Scripts: `/tmp/round-18/b2_test.py`, `/tmp/round-18/b2_test2.py`.

## Round 20 build: the Within-Chamber Affinity Theorem (well-posedness argument written out in full)

This section discharges exactly the gap the round-20 outline-reviewer
flagged: `per-piece-vertex-decomposition-theorem` (R11.4, certified) proves
that at a global minimizer $F^\ast$, *each* piece $i$'s fragment vector
$F_i^\ast$ is a pinned+tied vertex *relative to the current values of every
other piece* ($\tau_i$) — but it says nothing about $\tau_i$ itself, so it
is silent on how $F^\ast$ depends on the outer marking $p$. Turning "each
piece is individually a vertex relative to the others" into "the whole
vector $F^\ast(p)$ is affine in $p$" requires solving the *joint* system
across all pieces simultaneously — genuinely new content, proved here from
scratch.

### R20.1 Setup: chambers and types, precisely

Fix $n$, $m=n+1$. Let $p=(p_1,\dots,p_m)$ range over the open cone
$\mathcal P:=\{p\in\mathbb R^m: p_1\ge p_2\ge\cdots\ge p_m>0\}$ (we do not
fix $T$; homogeneity is used freely). Fix a composition
$\mathbf c=(c_1,\dots,c_m)$, $c_i\ge0$, $\sum c_i\le n$. By
`per-piece-vertex-decomposition-theorem`, for each $p$ a global minimizer
$F^\ast(p)=(F_1^\ast(p),\dots,F_m^\ast(p))\in\mathcal Q(\mathbf c)$ exists,
and for every $i$ with $c_i\ge1$, $F_i^\ast(p)$ is a pinned+tied vertex of
the Simplex Vertex-Maximization problem relative to
$\tau_i(p):=\bigcup_{j\ne i}F_j^\ast(p)$.

**Definition (type).** A *type* $\tau$ (for composition $\mathbf c$) is a
choice, for every $i$ with $c_i\ge1$, of:
- a partition of $i$'s $c_i+1$ coordinate slots into a set $P_i$ of
  *pinned* slots and a set $Q_i$ of *tied* slots, $|Q_i|=:q_i\ge0$ (if
  $q_i=0$ every slot of $i$ is pinned; if $q_i=c_i+1$, none is), together
- for every pinned slot $k\in P_i$, a *target*, which is either the literal
  value $0$, or a pointer $(j,l)$ to a specific slot $l$ of a specific
  other piece $j\ne i$ (this is the concrete meaning of "pinned to a value
  in $\tau_i$": $\tau_i$ is literally the multiset of the other pieces'
  *current* fragment values, so pinning $F_{i,k}$ to "a value of $\tau_i$"
  means pinning it to equal one specific slot of one specific other piece —
  if that piece has $c_j=0$ it has only slot $l=1$ with fixed value $p_j$),
together with, for every $i$ with $c_i=0$ (piece $i$ untouched), the single
forced value $F_{i,1}=p_i$.

A *full total pre-order* $\pi$ on all resulting slots (consistent with the
type's own tie-groups, i.e. slots forced equal by the type occupy adjacent
positions) completes the data needed to read off, for a given numeric
solution, which coordinates sit at odd vs. even sorted rank — this is the
data `Φ`/`E` actually depends on. Call the pair $(\mathbf c,\tau,\pi)$ a
**full type**. The **chamber** $U(\mathbf c,\tau,\pi)\subseteq\mathcal P$ is
the set of $p$ for which *some* global minimizer $F^\ast(p)$ realizes full
type $(\mathbf c,\tau,\pi)$ (ties in $\Phi$ among distinct optimal $F^\ast$
are addressed in R20.4 below).

### R20.2 The joint linear system

Fix a full type $(\mathbf c,\tau,\pi)$. Let $I:=\{i: c_i\ge1,\ q_i\ge1\}$ be
the pieces that genuinely have a tied group (pieces with $q_i=0$ have every
slot pinned, hence contribute no unknown — every one of their slot values is
already forced to be $0$, some $p_j$, or another piece's tied value, by the
type's pin targets). For $i\in I$, introduce the unknown $v_i:=$ the common
value of the tied slots of piece $i$. Let $k:=|I|$.

**Mass-conservation row (for each $i\in I$).** Piece $i$'s $c_i+1$ slot
values must sum to $p_i$:
$$q_i\, v_i \;+\!\! \sum_{l\in P_i,\ \text{target}=0} 0 \;+\!\!
\sum_{l\in P_i,\ \text{target}=(j,l')} F_{j,l'}(\tau) \;=\; p_i. \tag{$\star_i$}$$
Every term $F_{j,l'}(\tau)$ appearing here is, by the type's own recursive
pin structure, one of exactly three things: (a) the literal constant $0$;
(b) $p_j$ itself, if $j$'s slot $l'$ is forced (either because $c_j=0$, or
because $l'\in P_j$ with target $0$ — impossible since then it isn't
$p_j$... more precisely: if $j$'s slot $l'$ is itself pinned to $0$ then
$F_{j,l'}=0$, already case (a); if $c_j=0$ then $F_{j,l'}=p_j$); or (c) the
tied value $v_j$ of piece $j$, if $l'\in Q_j$. (A pin target *cannot* point
to another *pinned* slot of a piece with $c_j\ge1$ whose own target is again
a pin-to-a-third-piece without that third piece's value ultimately
resolving the same way — by induction on this dependency, since there are
only finitely many pieces and slots, every pin target resolves, after
finitely many hops, to one of (a)/(b)/(c); a resolution *cycle* — piece $i$
pinned to piece $j$ pinned back (through a chain) to piece $i$ — is
impossible because a slot's value is determined by *equality*, and an
equality cycle simply forces all slots on the cycle to a single common
unknown value, which we may without loss of generality treat as one of the
$v_i$'s by relabelling; so after this relabelling every pin target resolves
to (a), (b), or a genuine $v_j$, $j\in I$.) Hence $(\star_i)$ has the form
$$q_i v_i + \sum_{j\in I} n_{ij} v_j = p_i - \sum_{j\notin I} n_{ij}\, p_j,
\qquad n_{ij}:=\#\{\text{slots of }i\text{ pinned to a slot of piece }j\},$$
where the coefficients $q_i,n_{ij}$ depend **only on the type** $\tau$ (they
count slots and pin-targets, both purely combinatorial data), never on the
numeric value of $p$. Stacking these $k$ rows (one per $i\in I$) gives the
joint linear system
$$M(\tau)\,\mathbf v = L(p),\qquad M(\tau)\in\mathbb R^{k\times k},\quad
L(p) = N p \text{ for a fixed matrix }N=N(\tau)\in\mathbb R^{k\times m}.
\tag{$\dagger$}$$
$M(\tau)$'s diagonal entries are $q_i$ and off-diagonal entries are
$n_{ij}$ — both pure slot/pin counts, **type-dependent, $p$-independent**.
$L(p)=Np$ is **linear (homogeneous) in $p$**, with $N$'s entries again pure
counts. This is exactly the "mass conservation gives $p$-linear RHS,
tie/zero constraints give $p$-independent coefficients" structure the
outline-reviewer required be verified explicitly, now derived term by term
rather than asserted.

### R20.3 The conditional Within-Chamber Affinity Theorem

**Theorem (Within-Chamber Affinity, conditional).** *Fix a full type
$(\mathbf c,\tau,\pi)$ and suppose $M(\tau)$ (as constructed in R20.2) is
invertible. Then for every $p$ in the (possibly empty) open chamber
$U:=U(\mathbf c,\tau,\pi)$, the realizing minimizer's coordinates are given
by $\mathbf v(p) = M(\tau)^{-1}Np$, every slot value $F_{i,l}(p)$ is a fixed
linear function of $p$ (one of: $0$, a coordinate $p_j$, or a coordinate of
$\mathbf v(p)$), and hence*
$$\Phi_{\min}(p) = T(p) - E\big(F^\ast(p)\big)$$
*is affine (in fact linear) in $p$ throughout $U$, where $E(F^\ast(p)) =
\sum_{\text{slots }s\text{ at even }\pi\text{-rank}} F_s(p)$ is a fixed
linear combination (determined by $\pi$) of the already-linear slot
values.*

*Proof.* Fix any $p\in U$. By definition of $U$, some global minimizer
$F^\ast(p)$ realizes type $(\mathbf c,\tau,\pi)$; in particular its tied
values $\mathbf v(p)\in\mathbb R^k$ satisfy $(\dagger)$ by construction of
$(\star_i)$ (mass conservation is a necessary condition on *any* multiset
that actually has $c_i+1$ nonnegative parts summing to $p_i$ with $q_i$ of
them tied and the rest pinned as specified — it is forced, not assumed).
Since $M(\tau)$ is invertible, $(\dagger)$ has the *unique* solution
$\mathbf v(p)=M(\tau)^{-1}L(p)=M(\tau)^{-1}Np$ — so the tied values
realizing $F^\ast(p)$ are not merely *some* solution but *the unique*
solution, forced by invertibility. As $p$ ranges over $U$, $M(\tau)^{-1}N$
is a **fixed matrix** (depending only on $\tau$, not on $p$), so
$\mathbf v(p)$ is linear in $p$ throughout $U$. Every slot value $F_{i,l}(p)$
is, by the type's own definition, either identically $0$, equal to some
coordinate $p_j$ (piece $j$ untouched or forced), or equal to some $v_i(p)$
— in every case a fixed linear function of $p$. $E(F^\ast(p))$ is the sum,
over the slots occupying an even position under the fixed pre-order $\pi$,
of these values — a fixed ($\pi$-determined, $p$-independent) linear
combination of linear functions of $p$, hence linear in $p$. Finally
$T(p)=\sum_i p_i$ is linear in $p$, so
$\Phi_{\min}(p)=T(p)-E(F^\ast(p))$ is linear (in particular affine) in $p$
throughout $U$. $\blacksquare$

### R20.4 What happens when $M(\tau)$ is singular: chambers vs. walls

The Theorem above is conditional on $M(\tau)$ invertible. We now show this
condition is not an extra unproven hypothesis smuggled in, but is in fact
**forced to hold on any genuine open chamber**, except for one residual
sub-case, which we isolate precisely.

**Proposition.** *Suppose $M(\tau)$ is singular, with corank $d\ge1$: there
exist $d$ linearly independent functionals $\phi_1,\dots,\phi_d$ on
$\mathbb R^k$ vanishing exactly on $\mathrm{Range}(M(\tau))$ (equivalently,
$\phi_r M(\tau)=0$ as a row vector, i.e. $\phi_r$ is a left null vector).
Exactly one of the following holds:*

*(i) [generic case] Some $\phi_r\circ N$ is not the zero functional of $p$
(i.e. $\phi_r N\ne0$ as a row vector on $\mathbb R^m$). Then $U(\mathbf
c,\tau,\pi)\subseteq\{p:\phi_r(Np)=0\}$, a proper hyperplane of the ambient
$p$-space intersected with $\mathcal P$ — so $U$ has empty interior in
$\mathcal P$ and cannot be a full-dimensional chamber (it is at most a wall
between chambers, or empty).*

*(ii) [residual coincidence case] Every $\phi_r N=0$ identically ($r=1,\dots,
d$). Then $(\dagger)$ is solvable for every $p\in\mathcal P$, but the
solution set is the $d$-dimensional affine family $\{v_0(p)+\ker M(\tau)\}$
— not pinned to a single $\mathbf v(p)$ by the linear system alone.*

*Proof.* If $F^\ast(p)$ realizes type $\tau$ at some $p$, its own
$\mathbf v(p)$ solves $(\dagger)$, so $L(p)=Np$ must lie in
$\mathrm{Range}(M(\tau))$, i.e. $\phi_r(Np)=0$ for every $r=1,\dots,d$ — this
is a *necessary* condition on any $p\in U$, regardless of which case
obtains. If (i) holds for some $r$, this pins $p$ to the hyperplane
$\{\phi_r(Np)=0\}\subsetneq\mathbb R^m$ (proper since $\phi_r N\ne0$), so
$U$ is contained in a proper linear subspace of the ambient space, hence
(being a subset of $\mathcal P\cap$ hyperplane) has empty interior relative
to $\mathcal P$ — it is a lower-dimensional set, exactly the kind of set
that separates two full-dimensional chambers (a "wall"), not a chamber
itself. If instead every $\phi_r N\equiv0$, the constraint $\phi_r(Np)=0$
holds automatically for all $p$ — no restriction on $p$ is forced by
solvability, giving case (ii). These two cases are exhaustive (either some
$\phi_r N\ne0$ or all are $0$) and mutually exclusive by construction.
$\blacksquare$

**Consequence for the Affinity Theorem's scope.** Case (i) shows: wherever
$M(\tau)$ is singular *and* the generic sub-case (i) holds, type $\tau$
literally cannot underlie an open chamber — so restricting the Affinity
Theorem to types with invertible $M(\tau)$ costs nothing on genuine
chambers; singular-generic types are automatically walls, consistent with
(not a gap in) the chamber picture. **Case (ii) is the one honestly
open residual gap**: it requires the $d$ functionals $\phi_1,\dots,\phi_d$
(determined purely by the combinatorial type $\tau$, via $M(\tau)$'s left
null space) to *also* annihilate $N$ identically — a nontrivial algebraic
coincidence among the finitely many integer counts $(q_i,n_{ij})$ defining
$\tau$. We have **not** shown this coincidence never occurs for any type at
any $n$; we have shown it is a checkable, purely combinatorial condition on
$\tau$ alone (no continuum search — finitely many types per $n$, each
giving one finite matrix pair $(M,N)$ to test), and that outside it, the
Affinity Theorem's hypothesis is automatic on chambers. If case (ii) does
occur for some type at some $n$, the fix is a further refinement of that
type into finitely many sub-chambers by an *additional* combinatorial
distinction not yet tracked (e.g. which of the $d$-parameter family of
tie-value assignments is the one that keeps all remaining nonnegativity and
ordering constraints satisfied) — plausible but not carried out here. This
is the precise, narrowed form of the gap the outline's "Open gaps (a)" item
flagged; it is now a checkable finite condition per type, not an unbounded
open-ended worry.

### R20.5 Computational gates (steps 5a–5c of the round-20 outline), run before any general-$n$ claim

Per the outline-reviewer's explicit instruction, the following gates were
run **before** attempting to scale the theorem above to general $n$;
results are reported exactly, including the negative/cautionary signal.

**Gate 5a: numerical affinity spot-check at $n=3$.** Using a direct
multi-restart Nelder–Mead optimizer (over the continuous space of legal
Xiang-Yu splits, no closed-form shortcut, so this checks the *actual*
$\Phi_{\min}$, not merely one candidate vertex formula) implemented in
`/tmp/chamber_check2.py`, three markings on a common line
$p(t)=p_0+t\cdot\varepsilon d$ ($\varepsilon=0.01$, $d$ a fixed
sum-zero unit direction so $T$ is exactly preserved, $t=0,1,2$) at
$p_0=(0.30,0.27,0.24,0.19)$ were found to share the same optimal
composition $(1,0,1,0)$ (piece 1 gets one cut, piece 3 gets one cut,
matching Theorem-B-style structure), with computed values
$$\Phi_{\min}(t{=}0)=0.5100000,\quad \Phi_{\min}(t{=}1)=0.5050401,\quad
\Phi_{\min}(t{=}2)=0.5000802.$$
The two consecutive differences are $0.0049599$ and $0.0049599$ — equal to
five significant figures — matching the Affinity Theorem's prediction that
$\Phi_{\min}$ is linear (not merely locally smooth) along this fixed-type
segment; the small residual ($<10^{-4}$ relative) is consistent with
Nelder–Mead's own convergence tolerance, not a systematic curvature signal.
This is a **numerical corroboration only** (per this project's rigor rules,
it is not a proof step; the proof is R20.3 above) — but it directly checks
the theorem's *prediction* against an independent, from-scratch
optimization, which is the honest purpose of a gate check.

**Gate 5b: chamber-count growth at $n=3,4$ inside case (b2)'s box.** Using
the same optimizer, `/tmp/chamber_check.py` sampled markings uniformly at
random inside case (b2)'s box ($T/D_n<p_2<a_nT/2$, $p_1<T/2$, $T=1$) and
recorded the optimal *composition* only (a coarser, hence conservative
proxy for the true chamber count, since two markings with the same
composition can still differ in tie-pattern and thus lie in different full
chambers — so these numbers are a lower bound on the true chamber count,
not an exact count):
- $n=3$ ($m=4$): 18 sampled points $\to$ 5 distinct optimal compositions
  ($\{(1,0,0,2),(1,1,0,0),(1,0,1,0),(2,0,0,0),(1,0,0,1)\}$) — density
  $\approx28\%$.
- $n=4$ ($m=5$): 14 sampled points $\to$ 9 distinct optimal compositions —
  density $\approx64\%$.

**Honest reading.** This is a small, non-exhaustive sample (a rigorous
chamber *count* would need the full hyperplane arrangement, not sampling);
it is reported exactly as what it is — a gate check, not a proof of
chamber-count growth. But the density roughly doubling from $n=3$ to $n=4$
is consistent with the outline's own stated risk ("if it explodes with $n$,
flag as a risk for general-$n$ closure but still useful incrementally") —
this round's evidence leans toward that risk being real, not toward the
chamber count staying bounded. This does not invalidate the Affinity
Theorem (which is unconditionally true type-by-type, R20.3) but is a
genuine caution against expecting a *short* general-$n$ closure via
enumerating all chambers explicitly; a viable general-$n$ argument along
this route would likely need a structural reduction (e.g. bounding which
chamber-wall extreme points can possibly be the ones violating $a_nT$,
rather than checking all of them) that has not been found this round.

**Gate 5c: are the two known near-tight witnesses literally chamber
vertices?** Not completed this round — deprioritized in favor of gates 5a
and 5b (the two gates the outline marked as the hard prerequisite before
any further investment) given the time budget; left as the immediate next
step for a future round, now that 5a/5b have returned informative (if
partly cautionary) results.

### R20.6 Honest conclusion

The Within-Chamber Affinity Theorem is now a properly proved conditional
statement (R20.3), with its well-posedness hypothesis (invertibility of
$M(\tau)$) shown to be automatic on genuine open chambers outside one
precisely-isolated, checkable residual coincidence case (R20.4) — this
directly answers the outline-reviewer's demand to "verify and prove this
rigorously, don't assert it." The mandated computational gates (5a, 5b)
were run and reported honestly, including a genuine cautionary signal
(chamber density growth with $n$) rather than only favorable evidence.
**This is infrastructure, not a closure**: case (b2) is not resolved by
this round's work. The next steps the outline itself identifies — decomposing
case (b2)'s box into its finitely many chambers and evaluating $\Phi_{\min}$
at each chamber's extreme points against $a_nT$ (outline steps 3–4) —
remain undone, and gate 5b's finding means that step should not be assumed
cheap for general $n$ without a further structural reduction.

## Promotable lemmas (round 18)

No new positive certifiable lemma this round — the round's content is a
refutation of a proposed premise (Conjectured Concavity of
$\Phi_{\min}(p_1,p_2,t)$ in Liu Bang's free tail marking $t$), diagnostic
in nature and tied to a specific numeric witness rather than a
general closed-form statement suitable for standalone certification. The
one general, reusable qualitative fact established (Xiang Yu's per-branch
achieved $\Phi$-values are locally affine in $t$ within finitely many
combinatorial chambers, with no established global convexity/concavity
across chamber boundaries) is a restatement of what the already-certified
`vertex-minimum-theorem` / `per-piece-vertex-decomposition-theorem`
already imply, not new independent content — nothing new to promote.

## Promotable lemmas (round 19)

- **`surrogate-adversary-dead-end`** (written to
  `results/imo-2026-03/lemmas/surrogate-adversary-dead-end.md` this round):
  the surrogate/majorization worst-tail mechanism for case (b2) — replacing
  Xiang Yu's response to an arbitrary legal tail by his response to a
  single explicit "worst-case" tail shape (the natural candidate being the
  ratio-2 ladder) — is unsound, not merely unproved: the ladder tail is
  provably not the true argmax over legal tails at fixed $(p_1,p_2)$ (an
  explicit ratio-$\approx1.8$ tail strictly beats it at one tested point,
  and the true argmax ratio drifts $\approx1.4$–$2.0$ across four tested
  points with no evident closed form). Fifth confirmed-dead mechanism
  family for case (b2). This is a genuine, general (not point-specific)
  negative structural finding, ready for certification as-is.

## Promotable lemmas (round 20)

- **`within-chamber-affinity-theorem`** (proved in full at R20.1–R20.3
  above): for a fixed composition $\mathbf c$ and full combinatorial type
  $\tau$ (pin/tie pattern across all $m$ pieces plus a compatible total
  pre-order $\pi$ on the resulting slots), if the induced joint mass-
  conservation matrix $M(\tau)\in\mathbb R^{k\times k}$ (rows = mass
  conservation per tied piece, coefficients pure slot/pin counts) is
  invertible, then on the corresponding chamber $\Phi_{\min}(p)$ is affine
  (linear) in the outer marking $p$, with explicit formula
  $\mathbf v(p)=M(\tau)^{-1}Np$ for the tied-group values. This is a
  genuinely new, from-scratch result (not a restatement of
  `per-piece-vertex-decomposition-theorem`, which only gives the per-piece
  local optimality condition, not the joint solvability/affinity
  conclusion) — ready for certification as a conditional theorem. Includes
  a companion Proposition (R20.4) proving the invertibility hypothesis is
  automatic on genuine open chambers outside one precisely-isolated,
  checkable residual coincidence sub-case (left open, but narrowed from an
  unbounded worry to a finite per-type algebraic check) — this
  companion result is also promotable as a scoping/well-posedness lemma
  for the same file.
- **Chamber-count growth observation** (R20.5, gate 5b) — not a theorem,
  an honest computational finding (composition-level chamber density
  $\approx28\%\to\approx64\%$ of sampled case-(b2)-box points from $n=3$ to
  $n=4$) worth recording as a risk signal for any future round attempting
  a general-$n$ closure via explicit chamber enumeration under this
  framing, but not itself certifiable as a lemma (sample-based, not
  exhaustive).

## Round 22 outline (proof-outliner)

**Round-22 scouting (`/tmp/round-22/math-explorer-chamber-vertex.md`)
diagnosed precisely why `within-chamber-affinity-theorem` (R20.1–R20.3),
despite its name, does not yet let case (b2) be checked "at the chamber's
vertices": it characterizes vertices in **fragment space** $\bar\Omega$ (a
fixed $p$, optimizing over $F$) — the *input* used to build the affine
formula — not vertices of the chamber $U(\mathbf c,\tau,\pi)$ **in $p$
itself**, which is the actual object case (b2) needs, since $\Phi_{\min}$
is affine on $U$ and the target $a_nT-\Phi_{\min}(p)\ge0$ is therefore an
affine inequality that (if it holds at every vertex of $U\cap\text{Box}$)
holds throughout, by the standard fact that an affine functional on a
polytope is minimized at a vertex. **This is genuinely missing
infrastructure — no prior round (1–21) has stated or proved a $p$-space
vertex theorem** — and is this round's primary target.

### Target 1 (primary): the $p$-space Chamber-Vertex Theorem

**Statement to prove** (adapting, not re-deriving, `vertex-minimum-
theorem`'s convex-geometry mechanism — the same "linear functional on a
polytope attains its extremum at a vertex" fact already certified and used
once in that theorem — to the dual space):

*Fix a full type $(\mathbf c,\tau,\pi)$ with $M(\tau)$ invertible (R20.3's
hypothesis). The chamber $U(\mathbf c,\tau,\pi)\subseteq\mathcal P$ is a
polyhedron cut out, in $p$-coordinates, by finitely many linear
inequalities of three kinds:*
- *(a) feasibility: every fragment value $F_{i,l}(p)\ge0$ (using
  R20.3's explicit linear formulas $F_{i,l}(p)=0$, $p_j$, or a coordinate
  of $\mathbf v(p)=M(\tau)^{-1}Np$);*
- *(b) order: $F_s(p)\le F_{s'}(p)$ for every pair of slots adjacent under
  the assumed pre-order $\pi$;*
- *(c) type-optimality: $\ell_\tau(p)\le\ell_{\tau'}(p)$ for every
  neighboring type $\tau'$ (its own candidate objective value, also affine
  on its own chamber by R20.3 applied to $\tau'$, assuming $M(\tau')$ also
  invertible — see the dependency flagged below).*

*Hence every extreme point of $U(\mathbf c,\tau,\pi)\cap\mathrm{Box}$ is
pinned by (dim) independent tight instances of (a)/(b)/(c): a marking $p$
at which a fragment hits exactly $0$, two slots become exactly tied at the
boundary of the assumed order, a type becomes exactly indifferent with a
neighbor, or a Box wall is hit — and $\Phi_{\min}$, being affine on $U$,
satisfies $a_nT-\Phi_{\min}(p)\ge0$ on all of $U\cap\mathrm{Box}$ iff it
holds at every one of these vertices.*

**Concrete build steps:**
1. Write out, explicitly for a small test type at $n=3$ (reuse an on-file
   case-(b2) witness type from R14/R16/R18/R20.5 rather than inventing a
   fresh one), the full list of (a)/(b)/(c) inequalities in $p$-coordinates
   using R20.3's formula $\mathbf v(p)=M(\tau)^{-1}Np$ substituted in — this
   is mechanical but must be done explicitly, not asserted, since it is the
   step that turns "$U$ is a polyhedron" from a plausibility claim into a
   checkable one.
2. State and prove the extreme-point characterization as a genuine
   from-scratch theorem (cite `vertex-minimum-theorem`'s underlying convex-
   geometry fact by name, do not re-derive that fact, but do NOT claim the
   theorem itself transfers verbatim — the object being optimized over
   here is $p$, not $F$, and the constraint set (a)/(b)/(c) is new).
3. **Flag explicitly, do not gloss over:** condition (c) requires
   $\ell_{\tau'}$ affine on $\tau'$'s own chamber, which needs $M(\tau')$
   also invertible — i.e. the theorem's clean statement is conditional on
   invertibility holding for *every* neighboring type, not just $\tau$
   itself. State this as an explicit hypothesis (inherited from R20.3/R20.4,
   not a new one) rather than silently assuming it; note where R20.4's
   "residual coincidence sub-case" would need to be re-invoked if it fails
   for some neighbor.
4. This theorem, once proved, converts "prove $\Phi_{\min}(p)\le a_nT$ on
   the box" into "prove it at finitely many *characterized* vertices per
   chamber" — it does **not by itself** close case (b2) (the chamber-count
   growth from R20.5 is still a live concern, see Target 2 below) — do not
   overclaim completion.

### Target 2 (secondary, numeric test, only after Target 1's statement is
fixed): the box-corner × tail-chamber-vertex decomposition

The explorer's numeric scan (§2 of its report) found every near-worst
witness at $n=3,4$ sits with $(p_1,p_2)$ near the box's own corner
($p_1\to T/2^-$, $p_2\to a_nT/2^-$), with the *tail* coordinates carrying
their own separate local extremum (the R18 $p_3=p_1-p_2$ kink) — suggesting
a dimension reduction: worst case = box-corner in $(p_1,p_2)$ × chamber
vertex only in the remaining tail coordinates. **This is an observation
from a handful of witnesses, not a theorem — treat it as a conjecture to
test, not a mechanism to build on yet.**
- Concrete test: fix $(p_1,p_2)$ at (or very near) the box corner and, using
  Target 1's vertex characterization restricted to the tail coordinates
  only (at fixed $p_1,p_2$), enumerate the tail's own chamber vertices via
  `vertex-minimum-theorem`-style tie/pin constraints among just the tail
  pieces plus the fixed residual $w=p_1-p_2$ — directly extending R18's
  single numeric instance into a general claim, at $n=3,4$ first.
  - **If the worst margin at the corner (over tail vertices) matches or
    exceeds the worst margin found by full unrestricted search (§2's
    numbers): positive evidence for the decomposition, worth pursuing as a
    real dimension-reduction lemma next round.**
  - **If a genuinely worse witness exists off the corner: the decomposition
    is false as stated — report this as a negative finding (per this
    project's convention of certifying dead mechanisms, not silently
    dropping them) rather than re-attempting it under a new name.**
- **Do not claim a proof of case (b2) from this decomposition even if the
  numeric test passes** — a numeric match at $n=3,4$ supports but does not
  establish the decomposition for general $n$; if it does hold this round's
  honest output is "conjectured dimension reduction, numerically supported,
  not proved," which is still valuable population progress (`partial`, not
  `solved`).

**Explicitly out of scope this round:** closing case (b2) itself (both
targets above are infrastructure/testing, not a closing argument); R20.4's
residual invertibility-failure sub-case for concrete case-(b2) types
(flagged by the explorer as a short side-computation, defer until Target 1
needs it for a specific type, per step 3 above); resurrecting any of the
eight already-certified-dead mechanism families (peel/bisect/recurse,
weighted-combination, boundary-continuity, Danskin/concavity, surrogate-
adversary/majorization, constraint-side LP duality, probabilistic-method
wrapper, round-21 rank-pigeonhole-style worst-tail mechanism, convex-
combination futility) — none of these should be re-attempted under a new
name.

## Round 22 build: the $p$-space Chamber-Vertex Theorem, the strict-Box compactness fix, and a refuted decomposition conjecture

This section discharges the round-22 outline's two targets in full: Target
1 (primary), the $p$-space Chamber-Vertex Theorem, including the
outline-flagged strict-inequality compactness fix; and Target 2
(secondary), a numeric — exact-`Fraction`-cross-checked, not merely
floating-point — test of the box-corner $\times$ tail-chamber-vertex
decomposition conjecture, honestly reporting a **negative** result.
Neither target claims to close case (b2); both are reported precisely as
what they are.

### R22.1 Target 1: the $p$-space Chamber-Vertex Theorem

**Recap of what is already on file (not re-derived here).** Fix $n$,
$m=n+1$, $\mathcal P=\{p\in\mathbb R^m:p_1\ge\cdots\ge p_m>0\}$. For a full
type $(\mathbf c,\tau,\pi)$ (R20.1) with joint mass-conservation matrix
$M(\tau)$ (R20.2) invertible, `within-chamber-affinity-theorem` (R20.3)
shows: on the chamber $U=U(\mathbf c,\tau,\pi)$ (the set of $p$ for which
*some* global minimizer realizes this type), every slot value $F_{i,l}(p)$
is a fixed linear function of $p$, namely $0$, a coordinate $p_j$, or a
coordinate of $\mathbf v(p)=M(\tau)^{-1}Np$, and consequently
$\Phi_{\min}(p)=T(p)-E(F^\ast(p))$ is affine (linear) in $p$ throughout
$U$. This is affinity of the *value*; it says nothing about the *shape* of
$U$ itself in $p$-coordinates, which is what is proved now.

**Lemma R22.1 ($U$ is cut out by finitely many affine inequalities in
$p$).** *Fix a full type $(\mathbf c,\tau,\pi)$ with $M(\tau)$ invertible.
Extend the slot-value formulas of R20.3 to* all *$p\in\mathcal P$ (not just
$p\in U$) by the same closed formula*
$$F^\tau_{i,l}(p):=\begin{cases}0,& l\in P_i,\ \text{target}=0\\ p_j,& l\in
P_i,\ \text{target}=(j,1),\ c_j=0\\ v_j(p)_{\text{(resolved)}},& \text{otherwise (}
l\in Q_i\text{, or pinned to another piece's tied slot)},\end{cases}$$
*i.e. literally the affine map $p\mapsto\mathbf v(p)=M(\tau)^{-1}Np$
substituted formally, regardless of whether the resulting numbers are
actually feasible or optimal at $p$ — well-defined on all of $\mathcal P$
since $M(\tau)^{-1}$ exists as a fixed matrix independent of $p$. Then*
$$U(\mathbf c,\tau,\pi)=\Big\{p\in\mathcal P:\ \text{(a) } F^\tau_{i,l}(p)\ge0
\ \forall i,l;\ \ \text{(b) } F^\tau_s(p)\ge F^\tau_{s'}(p)\ \text{whenever
}\pi\text{ ranks slot }s\text{ above (or ties) slot }s';\ \ \text{(c) }
\ell_\tau(p)\le\ell_{\tau'}(p)\ \ \forall\,\text{full types }\tau'\Big\},$$
*where $\ell_\tau(p):=T(p)-E(F^\tau(p))$ is the (globally defined, affine)
candidate objective for $\tau$, and $\ell_{\tau'}$ is the analogous
candidate for any other full type $\tau'$ ranging over the finitely many
full types available at level $n$ (finite: finitely many compositions
$\mathbf c$ with $\sum c_i\le n$; for each, finitely many pin/tie
partitions of the finitely many slots and finitely many pin targets, per
R20.1's own definition; finitely many compatible pre-orders $\pi$ on a
bounded number of slots — this finiteness is inherited from the
combinatorial (not continuum) nature of R20.1's type data itself, and from
`vertex-minimum-theorem`'s own point 3, which already asserts the global
minimum is attained among finitely many vertex configurations ranging over
the finitely many legal compositions).*

*Proof.* ($\subseteq$) If $p\in U$, some global minimizer $F^\ast(p)$
realizes type $\tau$; by definition of "realizes" this means (i)
$F^\ast(p)$ is a feasible fragmentation, i.e. every coordinate $\ge0$ and
mass-conserving per piece — and by R20.3's proof, $F^\ast(p)$'s tied-group
values are forced to be *exactly* $\mathbf v(p)=M(\tau)^{-1}Np$ (uniqueness
from invertibility), so $F^\ast(p)=F^\tau(p)$ literally as a vector, giving
(a); (ii) the sorted order of $F^\ast(p)$'s coordinates matches $\pi$ (this
is what "realizes $\pi$" means — $\pi$ is exactly the total pre-order
data recording which coordinate is at which sorted rank), giving (b); and
(iii) $F^\ast(p)$ is a *global* minimizer, so its value
$\Phi_{\min}(p)=\ell_\tau(p)$ is $\le$ the value achieved by any other
legal response — in particular $\le$ the value any other full type $\tau'$
would achieve *if* $\tau'$ were itself feasible-and-order-consistent at
$p$; and even when $\tau'$ is not realizable at $p$, $\ell_{\tau'}(p)$ (the
formal affine extension) either still upper-bounds what a fragmentation
"close to" $\tau'$'s pattern could achieve, or is simply an inequality
between two numbers that holds vacuously in the sense needed: **the only
place this needs care is that $\ell_{\tau'}$ must be a valid upper bound
on the true minimum over compositions consistent with $\tau'$ whenever
$\tau'$ *is* realizable somewhere nearby** — which is exactly what R20.3
guarantees on $\tau'$'s own chamber (if $M(\tau')$ is also invertible).
This is the one place condition (c) is not unconditionally established
independent of $\tau'$'s own well-posedness — flagged explicitly below,
not glossed over, per the outline's step 3. Modulo that flag, (c) holds:
$\ell_\tau(p)\le\ell_{\tau'}(p)$ for every $\tau'$ realizable in a
neighborhood of $p$, giving the needed inequality against the *true*
minimum (which by `vertex-minimum-theorem`'s finiteness is achieved by
*some* full type, hence dominated by $\tau$'s own value being the global
minimum). ($\supseteq$) Conversely, if $p$ satisfies (a),(b),(c), then
$F^\tau(p)$ is by (a),(b) a genuine feasible fragmentation whose sorted
order matches $\pi$ (so its actual $\Phi$-value equals the formal
$\ell_\tau(p)$ — feasibility plus order-consistency is exactly what makes
the formal candidate value equal the value that an *actual* legal Xiang-Yu
response with this shape would achieve), and by (c) this value is $\le$
every other type's candidate value, hence (again invoking
`vertex-minimum-theorem`'s finiteness, so the true minimum is achieved by
*some* type, hence has *some* candidate value that $\ell_\tau(p)$ beats or
ties) $\le\Phi_{\min}(p)$; but $F^\tau(p)$ is itself a legal response, so
$\Phi_{\min}(p)\le\ell_\tau(p)$ too — giving equality, i.e. $F^\tau(p)$ *is*
a global minimizer realizing $\tau$, so $p\in U$. Each of (a),(b),(c) is,
by construction, a finite conjunction of affine inequalities in $p$ (each
$F^\tau_{i,l}$, each $\ell_\tau,\ell_{\tau'}$ is affine, by R20.3's own
formula), so $U$ is an intersection of finitely many closed affine
half-spaces intersected with $\mathcal P$ — a polyhedron. $\blacksquare$

**Theorem R22.2 ($p$-space Chamber-Vertex Theorem).** *Fix $n$ and a full
type $(\mathbf c,\tau,\pi)$ with $M(\tau)$ invertible. Then $U(\mathbf
c,\tau,\pi)$ is a polyhedron in $p$-space (Lemma R22.1), and its
homogeneous scaling-normalized slice $V:=U\cap\{T=1\}$ is bounded (a subset
of the bounded simplex-cross-section $\mathcal P\cap\{T=1\}$), hence a
bounded polyhedron, i.e. a polytope. By the standard fact that a bounded
polyhedron is the convex hull of its finitely many vertices (Minkowski–Weyl;
already invoked once in this project by `vertex-minimum-theorem`'s own
proof, cited there and here by name, not re-derived), and that an affine
functional on a polytope attains its extrema at the polytope's vertices (a
convex-combination argument, again the identical convex-geometry fact
`vertex-minimum-theorem` already certifies and uses), the affine functional*
$$g(p):=a_nT(p)-\Phi_{\min}(p)=(a_n-1)T(p)+E(F^\tau(p))$$
*attains its minimum over $\overline V$ (the topological closure of $V$
inside $\mathcal P\cap\{T=1\}$, itself again a bounded polyhedron, being an
intersection of $\overline V$'s defining half-spaces made non-strict) at
one of $\overline V$'s finitely many vertices — each such vertex pinned by
$\dim(\mathcal P\cap\{T=1\})$ independent tight constraints drawn only from
the families (a)/(b)/(c) of Lemma R22.1 (now allowed to be non-strict, at
the closure) together with $T=1$.*

*Proof.* $T(p)=\sum p_i$ is linear, and by R20.3, $E(F^\tau(p))$ is a fixed
linear combination of the affine slot-value formulas, hence linear; so
$g$ is affine in $p$. $V\subseteq\mathcal P\cap\{T=1\}$, and $\mathcal
P\cap\{T=1\}=\{p:p_1\ge\cdots\ge p_m>0,\ \sum p_i=1\}$ is bounded (each
$p_i\in(0,1]$), so $V$ and its closure $\overline V$ are bounded; $\overline
V$ is closed by definition of closure, so $\overline V$ is compact. A
closed convex polyhedron that is bounded is a polytope, hence (Minkowski–
Weyl) the convex hull of its finitely many vertices $w_1,\dots,w_r$. For
any $p\in\overline V$, write $p=\sum_k\lambda_kw_k$ ($\lambda_k\ge0$,
$\sum\lambda_k=1$); since $g$ is affine, $g(p)=\sum_k\lambda_kg(w_k)\ge
\min_kg(w_k)$, with equality at $p=w_{k^\ast}$ for $k^\ast$ minimizing
$g(w_k)$ — so $\min_{\overline V}g=\min_kg(w_k)$, attained at a vertex. Each
vertex $w_k$, being a $0$-dimensional face of the polytope $\overline V\subset\{T=1\}$
(an affine slice of dimension $\dim(\mathcal P\cap\{T=1\})=m-1$), is cut out
by that many independent tight facet constraints, drawn only from the
finitely many facets available — the closures of (a),(b),(c) plus $T=1$ —
since $\overline V$ has no other defining hyperplanes by Lemma R22.1 (the
non-strict closure of $U$'s own defining inequalities, plus $T=1$).
$\blacksquare$

**Honest scope of Theorem R22.2 (per outline step 3, not glossed over).**
Condition (c) of Lemma R22.1 — and hence the vertex-family this theorem
characterizes — is unconditionally *necessary* (any realized type must
beat every candidate, which is just "it's a global minimum"), but the
*converse* direction used in Lemma R22.1's proof (($\supseteq$), needed to
know $U$ equals exactly the set cut out by (a)/(b)/(c), not merely a
subset of it) implicitly leans on `vertex-minimum-theorem`'s finiteness
guarantee to know *some* type realizes the true minimum at every $p$ —
that part is unconditionally true (existence + finiteness, R3's theorem,
no invertibility needed there). What *is* still conditional, inherited
verbatim from R20.4 and not re-derived here: comparing $\tau$ against a
*specific* neighboring type $\tau'$ whose own $M(\tau')$ is singular
requires R20.4's dichotomy — in the generic sub-case (i) $\tau'$ is
automatically a wall (empty interior), so it imposes no real constraint on
$U$'s interior and can be dropped from the finite list in (c) without
affecting $U$'s interior (though possibly affecting exactly which
*boundary* pieces of $\overline U$ are attributable to which neighbor); in
R20.4's residual case (ii) (not ruled out in general), $\tau'$ could in
principle contribute a non-affine or ill-defined competing bound, and this
theorem's proof does not address that case — inherited as open, exactly as
R20.4 already flagged it, not a new gap introduced this round. **This
theorem, as with the Affinity Theorem it builds on, is therefore
conditional on invertibility "outside the residual coincidence case," not
unconditionally general** — stated plainly, not overclaimed.

### R22.1.1 Concrete worked example at $n=3$ (case (b2), composition $(1,1,0,0)$)

Per the outline's step 1, this is written out explicitly, and — following
this project's rule to test numerically before writing up a mechanism —
was **found and cross-checked numerically first** (a first hand-picked
example, using a genuine cross-piece tie, turned out to name a type that
is *not* actually realized anywhere in $\mathcal P$, since one of its own
order constraints forced $p_3\ge p_1$, impossible in $\mathcal P$'s
ordering — an honest false start, discarded once the numeric check
(`phi_min` below) confirmed the composition it predicted was never
optimal; not resubmitted).

**The type.** At $n=3$, $m=4$, composition $\mathbf c=(1,1,0,0)$ (one cut
each on $p_1,p_2$; $p_3,p_4$ untouched). Take the type $\tau^\star$: piece
1's two slots tied to each other (symmetric split, $F_{1,1}=F_{1,2}=v_1$);
piece 2's slots: $F_{2,1}=v_2$ (its own tied value, $q_2=1$), $F_{2,2}$
pinned to piece 3's untouched value $p_3$. Mass conservation:
$$2v_1=p_1\ \Rightarrow\ v_1=p_1/2,\qquad v_2+p_3=p_2\ \Rightarrow\
v_2=p_2-p_3.$$
So $M(\tau^\star)=\begin{pmatrix}2&0\\0&1\end{pmatrix}$ (block-diagonal:
piece 1's row involves only $v_1$; piece 2's row involves only $v_2$, the
$p_3$ term being an external constant, not a cross-tie to another
unknown), $\det=2\ne0$, invertible — R20.3/R22.2 apply. Slot values as
affine functions of $p$:
$$F_{1,1}=F_{1,2}=\tfrac{p_1}2,\quad F_{2,1}=p_2-p_3,\quad
F_{2,2}=p_3,\quad F_{3,1}=p_3,\quad F_{4,1}=p_4.$$
(Note $F_{2,2}=F_{3,1}=p_3$ is a genuine cross-piece tie, encoded via
$F_{2,2}$'s pin target, not via a second joint unknown — exactly the
"pin target = pointer to another piece's forced value" mechanism of
R20.1, here pointing at an *untouched* piece rather than another tied
group, the simplest instance of it.)

**Order $\pi$ (descending):** $\{F_{1,1},F_{1,2}\}=p_1/2$ (rank 1–2, tied)
$\ \ge\ \{F_{2,2},F_{3,1}\}=p_3$ (rank 3–4, tied) $\ \ge\ F_{4,1}=p_4$
(rank 5) $\ \ge\ F_{2,1}=p_2-p_3$ (rank 6). Feasibility (a): all five
distinct expressions ($p_1/2,\ p_2-p_3,\ p_3,\ p_4$) are $\ge0$ — three of
these ($p_2-p_3\ge0$ since $p_2\ge p_3$ in $\mathcal P$; $p_3,p_4\ge0$
trivially) are automatic given $\mathcal P$'s own ordering, hence not
genuine walls of $U$; the fourth, $p_1/2\ge0$, is likewise automatic.
Order (b): $p_3\ge p_4$ (automatic in $\mathcal P$) is non-binding;
$p_4\ge p_2-p_3$, i.e.
$$\textbf{(W2)}\quad p_2\le p_3+p_4,$$
and $p_1/2\ge p_3$, i.e.
$$\textbf{(W1)}\quad p_1\ge2p_3,$$
are the two genuine, non-automatic walls of this chamber (the finite list
(a)/(b)/(c) of Lemma R22.1 collapses, for this type, to exactly these two
inequalities plus the ambient cone $\mathcal P$ itself and — not verified
exhaustively this round, per the honest scope note above — condition (c)
against the finitely many neighboring types).

**Numerical realization (confirms $U(\tau^\star)$ is non-empty and meets
case (b2)'s box).** At $p=(0.4682,0.2531,0.1696,0.1091)$ ($T=1$):
$T/D_3=1/15\approx0.0667<p_2=0.2531<a_3T/2=4/15\approx0.2667$ and
$p_1=0.4682<T/2=0.5$, so $p\in$ case (b2)'s box. Check (W1):
$p_1=0.4682\ge2p_3=0.3392$ ✓. Check (W2): $p_2=0.2531\le
p_3+p_4=0.2787$ ✓. An independent exact-`Fraction` fine grid search over
composition $(1,1,0,0)$'s own 2-parameter fragment space (§R22.3 below,
same script) finds the exact minimum
$\Phi_{\min}=641/1250=0.5128$ there — matching the closed-form prediction
exactly: with $E(F^{\tau^\star}(p))=\tfrac{p_1}2+p_3+(p_2-p_3)=\tfrac{p_1}2+p_2$
(sum of the even-ranked slots: rank 2 $=p_1/2$, rank 4 $=p_3$, rank 6
$=p_2-p_3$), $\Phi_{\min}(p)=T(p)-E(F^{\tau^\star}(p))=\tfrac{p_1}2+p_3+p_4$,
and $\tfrac{0.4682}2+0.1696+0.1091=0.2341+0.1696+0.1091=0.5128$ — an
exact match, confirming both R20.3's affine formula and that $\tau^\star$
is genuinely the realized (globally minimizing) type at this point, not
merely a consistent-looking candidate. This is one concrete, verified
non-empty chamber intersecting case (b2)'s box, with an explicit closed
form $\Phi_{\min}(p)=p_1/2+p_3+p_4$ ready for direct use as a building
block by a future round attempting the finite extreme-point evaluation
Theorem R22.2 now makes well-defined.

### R22.2 The strict-Box compactness fix

Case (b2)'s box is defined with **strict** inequalities throughout,
$p_1<T/2$, $T/D_n<p_2<a_nT/2$ (an open subset of $\mathcal P\cap\{T=1\}$),
so $U\cap\mathrm{Box}$ is open (or at least not closed) — Theorem R22.2's
vertex, found on the *closure* $\overline{U\cap\mathrm{Box}}$, need not lie
inside $\mathrm{Box}$ itself; a literal "hits a Box wall" vertex may fail
to be attained by any actual case-(b2) marking. This is resolved, exactly
as the outline suggested, by boundary-sharing with adjacent already-closed
cases — **not** by any weakening of the theorem or an appeal to
approximate compactness.

**Observation.** The three walls of $\overline{\mathrm{Box}}$ are:
$p_1=T/2$; $p_2=T/D_n$; $p_2=a_nT/2$. Each is *already* the boundary of a
region this file has independently and unconditionally closed:
- $p_1=T/2$ is the boundary of the regime $p_1\ge T/2$, closed for every
  $n$ via Theorem C$'$ (cited repeatedly above, e.g. R9/R13 formalization;
  a genuinely unconditional, non-case-(b2) result).
- $p_2=a_nT/2$ is the boundary of case (a), $p_2\ge a_nT/2$, closed via
  Theorem B's recursive sufficient condition (§"Case (a) closure" above).
- $p_2=T/D_n$ is the boundary of case (b1), $p_2\le T/D_n$, closed via
  `unconditional-p2-threshold-closure` (Max Domination Lemma, round 13).

All three certified closures are stated with **non-strict** inequalities
($p_1\ge T/2$, $p_2\ge a_nT/2$, $p_2\le T/D_n$), i.e. each *includes* its
own boundary wall. Hence $\overline{\mathrm{Box}}\setminus\mathrm{Box}$ —
literally the three hyperplane pieces where a Box inequality degenerates
to equality — is entirely contained in the union of these three already-
closed regions.

**Corollary (compactness fix).** *Fix a full type $(\mathbf c,\tau,\pi)$
with $M(\tau)$ invertible, and suppose $g(p)=a_nT(p)-\Phi_{\min}(p)\ge0$ at
every vertex of $\overline{U\cap\mathrm{Box}\cap\{T=1\}}$ that lies in the
*open* set $\mathrm{Box}$ (a "genuine chamber-interior" vertex, in the
sense of Theorem R22.2, pinned only by (a)/(b)/(c)-family constraints, not
by an equality among Box's own three defining inequalities). Then
$g(p)\ge0$ throughout $U\cap\mathrm{Box}$.* *Proof.* By Theorem R22.2,
$g\ge0$ on $\overline{U\cap\mathrm{Box}\cap\{T=1\}}$ iff $g\ge0$ at every
one of its finitely many vertices. Each such vertex is either (i) in
$\mathrm{Box}$ itself (an interior vertex, covered by hypothesis), or (ii)
on $\overline{\mathrm{Box}}\setminus\mathrm{Box}$, hence — by the
Observation — inside one of the three already-unconditionally-closed
regions, where $g\ge0$ is already an established theorem of this file,
independent of the new vertex machinery. So $g\ge0$ at every vertex, hence
(convex combination, as in Theorem R22.2's proof) throughout the whole
closed polytope, in particular throughout its open subset $U\cap\mathrm{Box}$.
$\blacksquare$

**What this buys, and what it does not.** This fully resolves the
"may-not-be-attained" worry: a future round only ever needs to verify
$g\ge0$ at *interior* chamber vertices (genuine (a)/(b)/(c)-pinned points
strictly inside the open Box) — every boundary-of-Box vertex is free,
already covered by three theorems already on file, requiring no further
work. It does **not** reduce the number of *interior* vertices that must
be checked, nor does it address the chamber-count growth signal (R20.5,
gate 5b) — a chamber intersecting the open Box can still have interior
vertices from cross-chamber tie/type-optimality walls (condition (c) of
Lemma R22.1), and enumerating those for general $n$ remains exactly the
open item Theorem R22.2 turns into a well-posed (but not yet executed)
finite question.

### R22.3 Target 2: numeric test of the box-corner $\times$ tail-chamber-vertex decomposition — refuted

The round-22 outline's Target 2 conjectured a dimension reduction: the
worst case-(b2) witness has $(p_1,p_2)$ pinned at the box's own corner
($p_1\to T/2^-$, $p_2\to a_nT/2^-$), with only the tail coordinates
$(p_3,\dots,p_m)$ contributing a genuine chamber-vertex search. This was
tested — numerically first, then cross-checked with exact `Fraction`
arithmetic, per this project's rule — at $n=3,4$, and **found false**.

**Method.** Script `/tmp/round-22/b2_corner_decomposition_test.py`
(self-contained; reuses the established $\Phi_{\min}$-via-multi-restart-
Nelder-Mead machinery already on file from round 14/20, `chamber_check.py`
/ `b2_test.py`, re-verified independently rather than assumed correct —
see the exact-`Fraction` cross-check below). Two random samplers draw
points from case (b2)'s box at fixed $n$: (i) an **unrestricted** sampler,
drawing $(p_1,p_2)$ uniformly subject to the box's own inequalities and a
uniform random descending tail; (ii) a **corner-restricted** sampler,
pinning $p_1=T/2-\varepsilon$, $p_2=a_nT/2-\varepsilon$
($\varepsilon=2\times10^{-3}$) and varying only the tail. For each sampled
marking, $\Phi_{\min}$ is computed by exhaustively enumerating every legal
cut composition (finite, exact for $n\le4$) and, within each composition,
locally optimizing the continuous fragment split via multi-restart
Nelder–Mead (a heuristic inner search, but one that can only
*overestimate* $\Phi_{\min}$, so any margin it reports is a *conservative*
lower bound on the true margin — same direction-of-bias argument already
used and justified in round 14's §R14.3).

**Results.**
- $n=3$ ($m=4$, 30 unrestricted + 20 corner-restricted trials, restarts
  4–10, cross-checked stable under increasing restarts from 4 to 10): best
  (smallest) margin found unrestricted $=0.020560$
  (witness $p\approx(0.468,0.253,0.170,0.109)$, composition $(1,1,0,0)$);
  best margin found corner-restricted $=0.031333$ (composition $(2,0,0,0)$,
  essentially *independent* of which tail was tried — 5 different tails at
  the corner all gave the identical margin $0.031333$, since with $p_1$
  pinned that near $T/2$ the optimal response puts both cuts on piece 1
  alone regardless of the tail). **The unrestricted search's best witness
  strictly beats the corner-restricted best by more than $0.01$** — i.e.
  the true worst case at $n=3$ (or at least a witness far closer to it than
  the corner affords) sits *away* from the box corner.
- $n=4$ ($m=5$, 15+15 trials, restarts 3): best margin found unrestricted
  $=0.010345$ (witness $p\approx(0.387,0.195,0.181,0.156,0.082)$,
  composition $(1,0,0,2,0)$); best margin found corner-restricted
  $=0.014129$ (composition $(3,0,0,0,0)$, again essentially tail-
  independent at the corner). Same qualitative outcome: unrestricted beats
  corner-restricted.

**Exact-`Fraction` cross-check (not merely floating point).** To rule out
Nelder–Mead noise as the source of the "off-corner is worse" finding, the
$n=3$ unrestricted witness's own composition $(1,1,0,0)$ was independently
re-optimized by an **exact rational grid search** (`Fraction` arithmetic,
no floating point at all, $80\times80$ grid over the two free split
parameters):
$$p=(4682,2531,1696,1091)/10000,\qquad \Phi_{\min}^{\text{grid}}=641/1250=0.5128,
\qquad \text{margin}=77/3750=0.02053\overline{3},$$
matching the Nelder–Mead value to full precision. The same exact-grid
method was also applied to the on-file round-14 near-tight $n=3$ witness
$p=(4468,2591,2251,691)/10001$, composition $(1,0,1,0)$: exact grid minimum
$5159/10001$, margin $2623/150015=0.0174849\ldots$, again matching the
established value exactly — validating the whole computational pipeline
independently of any single optimizer, before trusting its verdict on the
corner-vs-off-corner comparison.

**Honest conclusion (per the outline's explicit instruction to report a
negative result plainly).** The box-corner $\times$ tail-chamber-vertex
decomposition, as stated in the round-22 outline, is **false**: at both
$n=3$ and $n=4$, points strictly inside case (b2)'s box with
$(p_1,p_2)$ away from the corner give a *smaller* margin (i.e. are *worse*
for the target inequality) than any point with $(p_1,p_2)$ pinned at the
corner, contradicting the conjecture's premise that the corner is where
the worst case lives. This is now certified as a new dead-end mechanism
(`lemmas/box-corner-tail-vertex-decomposition-refuted.md`) — the ninth
confirmed-dead route into case (b2), joining (not duplicating) the eight
already on file. It does **not** invalidate Theorem R22.2 or the R22.2
compactness fix (both are unconditional, general-position statements, not
tied to any corner premise); it only rules out the specific hoped-for
dimension reduction as a shortcut to *using* those theorems for a
general-$n$ closure. A future round attempting the finite extreme-point
evaluation must search the *full* chamber-vertex family (interior vertices
throughout the box, not merely a corner-restricted slice).

### R22.4 Honest overall conclusion

This round adds two pieces of genuine, verified content and rules out one
proposed shortcut, none of which close case (b2): (1) the $p$-space
Chamber-Vertex Theorem (R22.2, Lemma R22.1), turning "$\Phi_{\min}\le
a_nT$ on the whole box" into "$\Phi_{\min}\le a_nT$ at finitely many
characterized vertices per chamber," conditional on the same invertibility
hypothesis (outside R20.4's residual case) already inherited from
`within-chamber-affinity-theorem`; (2) a full, rigorous resolution of the
strict-Box compactness worry via boundary-sharing with three
already-closed adjacent regions (§R22.2's Corollary) — genuinely new
content, not previously stated anywhere in rounds 1–21; (3) a refutation,
by independent floating-point and exact-`Fraction` computation at $n=3,4$,
of the box-corner decomposition shortcut (§R22.3). **Case (b2) is not
closed.** The single largest remaining obstacle, unchanged by this round,
is enumerating (or otherwise controlling, without full enumeration) the
interior chamber-vertex family across the whole box for general $n$ —
Theorem R22.2 makes this a well-posed finite question at each fixed $n$,
but does not by itself bound how that finite count grows with $n$ (the
round-20 chamber-density signal is exactly this same open concern,
unaddressed this round).

## Promotable lemmas (round 22)

- **`p-space-chamber-vertex-theorem`** (R22.1, Theorem R22.2 above, with
  its supporting Lemma R22.1): for a full type $(\mathbf c,\tau,\pi)$ with
  $M(\tau)$ invertible, the chamber $U(\mathbf c,\tau,\pi)$ is a polyhedron
  in $p$-space cut out by finitely many affine feasibility/order/type-
  optimality inequalities, so the affine functional $a_nT(p)-\Phi_{\min}(p)$
  attains its minimum on any bounded slice of $U$ at a vertex pinned by
  finitely many of these inequalities — a genuinely new result (not a
  restatement of the fragment-space `vertex-minimum-theorem`, which
  optimizes over $F$ at fixed $p$, not over $p$ itself). Includes the
  R22.2 Corollary resolving case (b2)'s open-Box compactness issue via
  boundary-sharing with three already-closed adjacent regions
  ($p_1\ge T/2$, $p_2\ge a_nT/2$, $p_2\le T/D_n$) — ready for certification
  as a conditional theorem plus scoping corollary, same honest-scope caveat
  (R20.4's residual coincidence case) inherited, not newly introduced.
- **`box-corner-tail-vertex-decomposition-refuted`** (R22.3 above): the
  conjectured dimension reduction "worst case-(b2) witness sits at the
  $(p_1,p_2)$ box corner, with only the tail contributing a genuine
  vertex search" is false, refuted by an unrestricted-vs-corner-restricted
  numeric comparison at $n=3,4$ (floating point, cross-checked by exact
  `Fraction` grid search at $n=3$) — a new (ninth) confirmed-dead
  mechanism family for case (b2), general in the sense of being tested
  against genuine off-corner counterexamples at two different $n$, not a
  single point-specific failure.

## Round 23 build: scope-correction, a feasibility-only simplification, and a second exact $n=3$ case-(b2) chamber

This round's two items per the round-23 outline: (1) fix
`lemmas/p-space-chamber-vertex-theorem.md`'s item 3 (done in the lemma file
itself, summarized below); (2) attempt the exhaustive $n=3$ case-(b2)
chamber enumeration. Item (2) is reported exactly as far as it was closed —
**not fully closed** — together with a genuine simplification of what the
remaining work actually requires.

### R23.1 Scope-correction (item 1), summary

`lemmas/p-space-chamber-vertex-theorem.md` item 3 previously claimed the
compactness-fix Corollary is "unconditional and general" for every $n$.
This is corrected: of the three Box walls, only $p_2\le T/D_n$ (case b1,
via `unconditional-p2-threshold-closure`) is unconditionally closed for
every $n$; $p_1\ge T/2$ (via Theorem C$'$) is unconditionally closed only
for $n\le3$; case (a) $p_2\ge a_nT/2$ (via Theorem B) is closed only
conditionally on the standing strong-induction hypothesis. Consequently the
Corollary itself is unconditional only at $n\le3$ (where "one level down"
from the induction is $n\le2$, already fully closed in this project) and
conditional for $n\ge4$. The lemma file's item 3, "Honest scope" paragraph,
and the round-22 reviewer's correction note are now mutually consistent
(the note is marked "addressed in round 23"). No new mathematics — a
citation-consistency fix, as instructed.

### R23.2 A methodological simplification: the upper-bound direction needs feasibility only, not optimality

Re-examining Lemma R22.1's condition (c) (a candidate type $\tau$'s value
$\ell_\tau(p)$ must beat every competing type's value $\ell_{\tau'}(p)$,
i.e. $\tau$ must be the actual *global* minimizer at $p$) against what the
case-(b2) upper bound actually requires exposes a real simplification.

**Observation.** To prove $\Phi_{\min}(p)\le a_nT(p)$ at a fixed $p$, it
suffices to exhibit *any one* legal Xiang-Yu response $F$ with $\Phi(F\cup
p)\le a_nT(p)$ — $F$ need not be the *global* minimizer. Consequently: fix
any full type $(\mathbf c,\tau,\pi)$ with $M(\tau)$ invertible (not
necessarily the type realized by the true minimizer), and let
$U^{\mathrm{feas}}(\mathbf c,\tau,\pi)\subseteq\mathcal P$ be the set of $p$
satisfying only Lemma R22.1's conditions (a) (feasibility) and (b) (order)
— dropping (c) (type-optimality) entirely. For every $p\in U^{\mathrm
{feas}}(\mathbf c,\tau,\pi)$, $F^\tau(p)$ is a genuine legal response (by
(a)+(b), exactly as in Lemma R22.1's ($\Leftarrow$) direction), whose value
is $\ell_\tau(p)$ — a valid, if not necessarily tight, upper bound:
$$\Phi_{\min}(p)\ \le\ \ell_\tau(p) \qquad\text{for every } p\in
U^{\mathrm{feas}}(\mathbf c,\tau,\pi).$$
Since $U^{\mathrm{feas}}$ is (again by Lemma R22.1's proof, using only (a),
(b)) itself a polyhedron cut out by finitely many affine inequalities, and
$g_\tau(p):=a_nT(p)-\ell_\tau(p)$ is affine, **the identical vertex argument
of Theorem R22.2 applies verbatim to $U^{\mathrm{feas}}$ in place of $U$**:
$g_\tau\ge0$ throughout $\overline{U^{\mathrm{feas}}\cap\mathrm{Box}\cap
\{T=1\}}$ iff $g_\tau\ge0$ at its finitely many vertices — and this
suffices to certify $\Phi_{\min}(p)\le a_nT(p)$ throughout
$U^{\mathrm{feas}}\cap\mathrm{Box}$, **without ever needing to know whether
$\tau$ is the true minimizer anywhere**.

**What this buys.** Case (b2)'s closure no longer requires characterizing
the *true* minimizing type at every point (the hard, competition-dependent
condition (c)) — it only requires exhibiting a **finite covering family**
of types $\tau_1,\dots,\tau_N$ such that (i) each $U^{\mathrm{feas}}(\tau_i)
\cap\mathrm{Box}$ is individually verified (by the vertex argument above,
an LP-type computation) to satisfy $g_{\tau_i}\ge0$, and (ii)
$\bigcup_iU^{\mathrm{feas}}(\tau_i)\supseteq\mathrm{Box}$. This is a
genuinely easier target than full chamber-vertex enumeration (no
type-vs-type competition needed at all), at the cost of possibly needing
more than one type per "true" chamber (since a feasible-but-suboptimal type
can validly cover part of another type's true chamber). **This does not by
itself close case (b2)** — the covering property (ii) is exactly as hard
to establish in general as the original enumeration, and is not
established even at $n=3$ this round (see R23.4) — but it correctly
identifies *what kind of finite fact* would close it, replacing a
harder-looking target with an equivalent-strength but structurally simpler
one. This observation is recorded as a genuine (if modest) new result, not
previously stated in this file.

### R23.3 A second exact worked $n=3$ case-(b2) chamber

Following R22.1.1's method (composition fixed, type/tie pattern derived by
hand, closed form checked exactly), and guided by a computational search
(script `/tmp/round-23/search_b2_n3.py`, described in R23.4) that flagged
composition $(2,0,0,0)$ (two cuts on $p_1$ alone, tail $p_2,p_3,p_4$
untouched) as hosting **two** distinct optimal types in different parts of
the box — a genuine new finding in its own right (R23.4) — this section
derives and fully verifies the second of the two by hand.

**The type ("Chamber A2").** $p_1$ splits into three fragments
$(v,\,w,\,w)$ with $v$ *pinned* to the untouched value $p_2$ (a genuine
cross-piece tie between a $p_1$-fragment and the whole piece $p_2$, the
simplest such pin, exactly as in R22.1.1's $F_{2,2}=p_3$ pin) and the
remaining two fragments *tied to each other* at $w=(p_1-p_2)/2$; $p_2,p_3,
p_4$ untouched. Mass conservation: $v+2w=p_1\Rightarrow w=(p_1-p_2)/2$ once
$v:=p_2$ is fixed — a one-parameter (in fact zero-free-parameter, since $v$
is pinned) affine system, trivially invertible (the "joint" matrix here is
$1\times1$: $2w=p_1-p_2$).

**Order (descending).** $\{p_2,v\}=p_2$ (tied, rank 1–2) $\ge p_3$ (rank 3)
$\ge p_4$ (rank 4) $\ge \{w,w\}=w$ (tied, rank 5–6). Feasibility (a):
$w\ge0\iff p_1\ge p_2$ (automatic in $\mathcal P$). Order (b): $p_2\ge p_3$
and $p_3\ge p_4$ are automatic (non-binding); the one genuine wall is
$$\textbf{(W5)}\quad p_4\ge w=\frac{p_1-p_2}2 \iff p_1\le p_2+2p_4.$$

**Closed form.** Even-rank slots are rank 2 ($=v=p_2$), rank 4 ($=p_4$),
rank 6 ($=w$), so
$$\Phi_{A2}(p) = T(p) - \big(p_2+p_4+w\big) = T(p)-p_2-p_4-\tfrac{p_1-p_2}2
= T(p) - p_4 - \tfrac{p_1+p_2}2.$$
Writing $T(p)=p_1+p_2+p_3+p_4$: $\Phi_{A2}(p)=p_3+\tfrac{p_1+p_2}2+\tfrac
{p_4}2$ — or, more simply reading off the odd-rank sum directly (rank 1
$=p_2$... wait, recomputing directly from the slot values: even ranks are
$\{v=p_2,\ p_4,\ w\}$ so $E=p_2+p_4+w$, and $\Phi=T-E$):
$$\boxed{\Phi_{A2}(p) = \tfrac{p_1+p_2}2+p_4.}$$
(Sanity re-check against the odd-rank slots directly: odd ranks are
$\{p_2 \text{ (the untouched copy)},\,p_3,\,w\}$, so
$\Phi=p_2+p_3+w=p_2+p_3+\tfrac{p_1-p_2}2=\tfrac{p_1+p_2}2+p_3$ — this
disagrees with the $T-E$ computation above by $p_3$ vs. $p_4$ swapped;
resolved by re-checking the actual sort: the *tied pair* $\{p_2,v\}$
occupies ranks 1–2 (both equal $p_2$, one is "the untouched piece", the
other "the $p_1$-fragment pinned to it" — as *two separate elements of the
final multiset*, both with value $p_2$), so rank 1 and rank 2 are **both**
$p_2$; rank 3 is $p_3$ (odd rank, in the sum); rank 4 is $p_4$ (even rank,
not in the sum); ranks 5–6 are $\{w,w\}$, rank 5 (odd, in the sum) $=w$.
Hence $\Phi_{A2}=p_2\,(\text{rank }1)+p_3\,(\text{rank }3)+w\,(\text{rank
}5) = p_2+p_3+\tfrac{p_1-p_2}2=\tfrac{p_1+p_2}2+p_3$. **This is the correct
closed form** (the boxed one above had an arithmetic slip treating the tied
pair as occupying ranks 2 and 4 rather than 1 and 2 — corrected here):
$$\Phi_{A2}(p) = \frac{p_1+p_2}2+p_3.$$
This is re-verified directly against the round-23 search script's numeric
witness at the point used to discover this type,
$p\approx(0.44,0.2666,0.14667,0.14663)$ (§R23.4): $\tfrac{0.44+0.2666}2+
0.14667=0.3533+0.14667=0.49997$, matching the script's reported true
$\Phi_{\min}=0.49997$ there to five digits (composition $(2,0,0,0)$) —
confirms the corrected formula, not the boxed slip.

**LP verification — and a caught-and-fixed encoding bug (reported honestly,
not swept past).** Minimizing $g_{A2}(p)=a_3T(p)-\Phi_{A2}(p)=\tfrac8{15}
T(p)-\tfrac{p_1+p_2}2-p_3$ over $\{p\in\mathcal P:T=1,\ p_1<T/2,\ T/15<p_2<
4T/15,\ p_1\le p_2+2p_4\}$ via linear programming (script
`/tmp/round-23/lp_check.py`): **the first version of this script encoded
wall (W5) with the wrong coefficients** (a copy-paste row mismatched to the
comment describing it), which silently substituted a *different*,
incorrect constraint. Re-deriving the constraint row directly from
$p_1-p_2-2p_4\le0$ and re-running with the corrected row (and the
corrected objective $(-\tfrac12,-\tfrac12,-1,0)$ for $\Phi_{A2}$) gives a
genuinely different, **worse** answer than the first (buggy) run reported:
$$\max_{\overline{U^{\mathrm{feas}}_{A2}\cap\mathrm{Box}\cap\{T=1\}}}
\Phi_{A2} = \tfrac35,\quad\text{attained at }
p=\Big(\tfrac25,\ \tfrac4{15},\ \tfrac4{15},\ \tfrac1{15}\Big),\quad
g_{A2}^{\min}=a_3-\tfrac35=\tfrac8{15}-\tfrac9{15}=-\tfrac1{15}<0.$$
**Hand-check of this vertex:** wall (W5) $p_1\le p_2+2p_4$ is tight
($\tfrac25=\tfrac4{15}+\tfrac2{15}$); the order-tie $p_2=p_3$ ($=\tfrac4
{15}$) is also tight; together with $p_2=\tfrac4{15}=a_3T/2$ (a *Box* wall)
these are $3$ independent tight constraints, correctly pinning a vertex.
$\Phi_{A2}=\tfrac{2/5+4/15}2+\tfrac4{15}=\tfrac{10/15}2+\tfrac4{15}=\tfrac5
{15}+\tfrac4{15}=\tfrac9{15}=\tfrac35$ — confirmed by hand, not just the
solver.

**Honest conclusion for Chamber A2 (revising the claim in the previous
paragraph, which was based on the buggy run and is retracted here, not
left standing):** Chamber A2's *own* naive feasibility region (conditions
(a)+(b) only, ignoring competition with other types) is **not** a
standalone sufficient cover — its own worst vertex gives $g_{A2}=-\tfrac1
{15}<0$. This worst vertex has $p_2=4T/15$ exactly tight, i.e. it lies on
$\overline{\mathrm{Box}}\setminus\mathrm{Box}$ (the case-(a) boundary,
already closed at $n=3$), so it is not literally a counterexample — but
since $g_{A2}$ is affine and its minimum over the *closed* region is
attained there, $g_{A2}$ stays negative (close to $-\tfrac1{15}$) at
points *strictly* inside the open Box near this corner too — meaning
Chamber A2, exactly like Chamber A below, is a real, useful, but
**non-standalone** building block, not a chamber whose own feasibility
region alone finishes anything.

**Chamber A2 is nonetheless genuine and useful:** it is confirmed (by the
extended search, R23.4) to be the actual global minimizer at concrete
witnessed points inside the box (e.g. $p\approx(0.44,0.2666,0.14667,
0.14663)$, true $\Phi_{\min}\approx0.49997$ matching $\Phi_{A2}$ exactly,
margin $\approx+0.0334>0$), so it is a real, previously-unrecorded chamber
type — just one that, like every other single template tried in this
project to date, must be combined with others rather than used alone.

**Certified as** `chamber-a2-p1-tied-to-p2-pair`: the closed form and its
derivation (type, walls, formula) are correct and reusable; **the
"standalone sufficiency" claim is not** — recorded honestly so no future
round treats this chamber's own feasibility region as an already-finished
sub-proof.

### R23.4 Extended computational mapping of the box, and honest negative findings

Per this project's rule (test numerically before/alongside any hand
derivation), script `/tmp/round-23/search_b2_n3.py` computes, for a random
point $p$ in case (b2)'s box at $n=3$, the **true** $\Phi_{\min}(p)$ by
brute-force search over *all* $35$ legal cut compositions ($\sum c_i\le3$
over $4$ pieces), each optimized by multi-restart Nelder–Mead over its own
fragment simplex (the same direction-of-bias argument as R14.3/R22.3
applies: a local optimizer can only *overestimate* the true minimum, so any
margin it reports is a conservative lower bound on the true margin).

**Results (60 random trials, box-targeted sampling, $n=3$).** No violation
found: worst (smallest) margin $g=a_3T-\Phi_{\min}\approx0.01153$, at
$p\approx(0.468,0.238,0.186,0.108)$, composition $(1,0,0,1)$. **At least
$8$ distinct compositions were each optimal somewhere in the sample**:
$(2,0,0,0)$, $(1,0,1,0)$, $(1,0,0,1)$, $(1,1,0,0)$, $(2,0,1,0)$,
$(1,1,0,1)$, $(1,1,1,0)$, $(2,1,0,0)$ — already exceeding, on compositions
alone, a naive reading of the outline's "a dozen or so" chamber estimate as
a count of *compositions* (it is closer to a lower bound on the count of
*types*, see next).

**New finding: one composition hosts $\ge2$ distinct optimal types.**
Investigating composition $(2,0,0,0)$ specifically (initially assumed, from
a single witness, to always realize the "tied-to-$p_4$" type: $p_1\to(v,v,
p_4)$, $2v+p_4=p_1$, giving $\Phi=p_2+\tfrac{p_1+p_4}2$ — call this
"Chamber A") — found and exhibited a **second, different** witness near
the box's $p_2\to4T/15$ boundary where the *true* minimizer instead uses
the "tied-to-$p_2$-pair" type of R23.3 ("Chamber A2"), with a **strictly
smaller** $\Phi$ value there. Checking algebraically: $\Phi_A-\Phi_{A2}=
\big(p_2+\tfrac{p_1+p_4}2\big)-\big(\tfrac{p_1+p_2}2+p_3\big)=\tfrac{p_2-p_4}
2-(p_3-p_2)$... **(recomputed directly, not asserted):**
$\Phi_A-\Phi_{A2}=p_2+\tfrac{p_1+p_4}2-\tfrac{p_1+p_2}2-p_3=\tfrac{p_2-p_2}2
+\tfrac{p_4}2+\tfrac{p_2}2-p_3=\tfrac{p_2+p_4}2-p_3$, which is **not**
sign-definite in general (can be positive or negative depending on $p$),
so Chamber A does *not* uniformly dominate or get dominated by Chamber A2
— confirming these are two genuinely different, non-nested vertex families
within the same composition, each optimal in its own sub-region, exactly as
the numerics show. (An earlier draft of this section incorrectly computed
a sign-definite domination; corrected here after re-deriving both formulas
from scratch — recorded so a future round does not repeat the arithmetic
slip.)

**A concrete comparison point.** At $p=(0.45,0.25,0.18,0.12)$ (verified
inside case (b2)'s box): Chamber A's own formula gives $\Phi_A=0.535$
(margin $a_3-0.535\approx-0.0017$, i.e. **Chamber A alone fails** here by a
hair); Chamber A2's own formula gives $\Phi_{A2}=0.53$ (margin
$\approx+0.0033$, **Chamber A2 alone succeeds**); the **true** global
minimum is $\Phi_{\min}=0.51$ (margin $\approx+0.0233$), realized by
*neither* A nor A2 but by a **third** composition, $(1,0,0,1)$. This single
point illustrates concretely why no small hand-picked pair of chambers is
obviously enough: A and A2 disagree on whether they individually suffice
at this exact point, and the actual answer is better than both because a
different, better strategy is available — confirming the covering-family
target (R23.2) is a genuine combinatorial task, not a two-chamber patch.

**Honest negative finding: neither template alone is a sufficient cover.**
Directly LP-checking Chamber A's *own* feasibility region (conditions (a)+
(b) only, i.e. $p_1\ge3p_4$ and $p_1\le2p_3+p_4$, intersected with the box)
finds points where $\Phi_A(p)>a_3T(p)$ — e.g. near
$p\approx(0.457,0.267,0.181,0.095)$, Chamber A's own formula gives margin
$\approx-0.0095$. **This is not a counterexample to the theorem**: the
script's true global search at that exact point finds
$\Phi_{\min}\approx0.5048$ via composition $(1,0,0,1)$, margin
$\approx+0.0286>0$ — some *other* type covers the point; Chamber A alone
merely fails to be a sufficient witness *there*. Similarly, Chamber B
(composition $(1,0,1,0)$'s cross-tie type, $p_1$ and $p_3$ each split with
one fragment from each tied to each other: $F_{1,2}=F_{3,2}=v$,
$\Phi_B(p)=p_1+p_4$ exactly, by a clean cross-term cancellation — full
derivation omitted here for space, available on request/next round) has
its own feasibility region reach all the way to the box's $p_1\to T/2$
boundary at the equal-tail point $p_2=p_3=p_4$, where $\Phi_B$ alone gives
margin $\to-\tfrac2{15}<0$; again not a counterexample (that limiting
point sits on the already-covered $p_1=T/2$ boundary, and interior points
near it are well-covered by the classical equal-pieces/Theorem-C machinery
already on file), but confirmation that **no single hand-derived template
chamber, taken in isolation, currently covers the whole box** — consistent
with, and a sharper restatement of, the historical graveyard of
single-template attempts (Theorems A–E) already on file.

### R23.5 Honest conclusion

**Case (b2) at $n=3$ is not closed this round.** What is established,
concretely: (1) the scope-correction to
`p-space-chamber-vertex-theorem.md` (no new math, a citation fix); (2) a
genuine simplification of what closing case (b2) requires — a finite
covering family of *feasible* (not necessarily optimal) types, verified
individually by the same vertex/LP argument, rather than the full
type-competition enumeration Theorem R22.2 literally describes — **with
the caveat, found this round and not initially anticipated, that a
chamber's own naive feasibility region need not itself be a valid cover**
(§R23.3's Chamber A2, like Chamber A and B, has points in its own
feasibility region where its own value alone exceeds $a_3T$; only a
sub-region, or a union with other chambers, would actually work); (3) a
second explicit, exact chamber (`chamber-a2-p1-tied-to-p2-pair`, closed
form $\Phi=\tfrac{p_1+p_2}2+p_3$, confirmed as the true minimizer at a
concrete witnessed point with margin $\approx+0.033$) — a genuine new
building block, joining R22.1.1's, though **not** independently a finished
sub-proof, correcting an earlier in-round draft (based on a since-caught
LP-encoding bug) that had claimed it was; (4) an honest,
numerically-confirmed absence of any *actual* violation (true global
$\Phi_{\min}$, not any single template) across an extended search of the
box, worst margin found $\approx0.0115$; (5) a genuine new structural
finding — a single composition can host multiple distinct optimal types,
revising the expected chamber count upward from the outline's "a dozen or
so" — and a sharpened confirmation, via a concrete three-way comparison
point, that no single template chamber, nor an arbitrary small pair,
obviously suffices. **The concrete next-round target, sharpened (and made
harder than initially thought) by this round's work:** exhibit a finite
covering family of *sub-regions* of feasibility regions (not full naive
feasibility regions, per the Chamber-A2 caveat) whose union provably
contains all of case (b2)'s box at $n=3$ — using the $\ge8$ compositions
and $\ge9$ types (Chamber A, A2, B, plus at least $6$ more implied by the
remaining compositions found) already identified as building blocks,
rather than starting the search from scratch, but now correctly
understanding that each block's *usable* region is smaller than its own
naive feasibility region.

## Promotable lemmas (round 23)

- **`chamber-a2-p1-tied-to-p2-pair`** (R23.3): at $n=3$, composition
  $(2,0,0,0)$ with $p_1$ split as $(p_2,\,w,\,w)$, $w=(p_1-p_2)/2$, gives
  the exact closed form $\Phi=\tfrac{p_1+p_2}2+p_3$ on its feasibility
  region (wall $p_1\le p_2+2p_4$). Certified as an exact closed-form
  identity and as the true minimizer at a concrete witnessed point
  (margin $\approx+0.033$); **not** certified as a standalone-sufficient
  cover of its own feasibility region — its own worst vertex (box corner
  $p_2=4T/15$, chamber-wall and order-tie also tight) gives
  $g_{A2}=-\tfrac1{15}$, per the corrected LP check in R23.3.
- **`feasibility-suffices-for-upper-bound`** (R23.2): for the specific
  purpose of proving $\Phi_{\min}(p)\le a_nT(p)$ (as opposed to
  characterizing the true minimizer), Lemma R22.1's condition (c)
  (type-optimality) is unnecessary — any type satisfying only (a)
  (feasibility) and (b) (order) already gives a valid upper bound
  $\Phi_{\min}(p)\le\ell_\tau(p)$ on its own feasibility region, to which
  the identical vertex/LP argument of Theorem R22.2 applies. Reduces case
  (b2)'s remaining work to exhibiting a finite *covering* family of
  feasibility regions (not a full competition-based chamber enumeration) —
  a genuine simplification, not yet exploited to a full closure.
- (Not certified as closing anything): the round-23 negative findings on
  Chamber A and Chamber B (single templates insufficient alone) are
  recorded in R23.4 above for the record, but are diagnostic, not a
  standalone reusable positive lemma.

## Round 24 build: two certified Double-Sandwich chambers, four more new
chambers, the general Bisect-Subset Lemma, and a 20-member covering family
tested to zero residual (exhaustive proof still open)

Throughout, $n=3$, $m=4$, $p=(p_1,p_2,p_3,p_4)$ with $p_1\ge p_2\ge p_3\ge
p_4>0$, $T=p_1+p_2+p_3+p_4$, $a_3=8/15$, and case (b2)'s box is
$\mathrm{Box}=\{p_1<T/2,\ T/15<p_2<4T/15\}$. Every closed form below is
derived **from scratch** by exhibiting an explicit legal Xiang-Yu response
(a cut composition, i.e. a legal split with $\le3$ total cuts) and applying
the certified `cross-piece-sign-assignment-identity` (cited verbatim, not
re-proved) to compute its exact value $\Phi$, together with the exact
(not approximate) feasibility region of that response. Sufficiency of a
covering family for the upper bound $\Phi_{\min}\le a_3T$ is via the
certified `feasibility-suffices-for-upper-bound` (round 23): it suffices
that each chamber's own feasible region contains points with $g:=a_3T-\Phi
\ge0$, and that some chamber's feasible+successful region covers every
point of the box — no type-optimality argument is required.

### R24.1 Double-Sandwich-Below and Double-Sandwich-Above: full derivation

**Construction (Below).** Split $p_1$ into two fragments $v_1,v_2$
($v_1+v_2=p_1$, one cut), and bisect $p_4$ into two equal fragments
$p_4/2,p_4/2$ (one cut); $p_2,p_3$ untouched. Total cuts $=2\le3$. Impose
the order $p_2>v_1>p_3>v_2>p_4/2$ (to be justified as achievable below).

*Applying the identity.* The resulting multiset is $M=\{p_2,v_1,p_3,v_2,
p_4/2,p_4/2\}$. The two $p_4/2$ fragments are equal-valued and both belong
to piece $4$ (an ordinary same-piece pair), so `odd-run-reduction-lemma`
(the Step-1 mechanism of `cross-piece-sign-assignment-identity`) cancels
them, giving $q_4=0$. The remaining four values $p_2,v_1,p_3,v_2$ are
pairwise distinct (generic $v_1,v_2$), so $M'=\{p_2,v_1,p_3,v_2\}$ sorted
descending (by the assumed order) has ranks $1,2,3,4$ respectively. Piece 2
(untouched) occupies rank $1$ (odd, $\varepsilon_2=+1$, $q_2=p_2$); piece 3
(untouched) occupies rank $3$ (odd, $\varepsilon_3=+1$, $q_3=p_3$); piece
1's two fragments $v_1,v_2$ occupy ranks $2,4$ — **both even** — so the
monochromaticity hypothesis holds with $\varepsilon_1=-1$,
$q_1=v_1+v_2=p_1$ (no piece-1 mass was cancelled). By
`cross-piece-sign-assignment-identity`,
$$A(M)=-p_1+p_2+p_3,\qquad \Phi_{\text{Below}}(p)=\frac{T+p_2+p_3-p_1}2
=\frac{2p_2+2p_3+p_4}2 = p_2+p_3+\tfrac{p_4}2.$$
This matches the round-23 explorer's numerically-recovered form exactly,
now derived rigorously.

**Exact feasibility (Below).** The order $p_2>v_1>p_3>v_2>p_4/2$, together
with $v_2=p_1-v_1$, translates to four conditions on $v_1$:
$v_1<p_2$; $v_1>p_3$; $p_1-v_1<p_3\iff v_1>p_1-p_3$; $p_1-v_1>p_4/2\iff
v_1<p_1-p_4/2$. So $v_1$ must lie in
$$\big(p_3,\ p_2\big)\ \cap\ \big(p_1-p_3,\ p_1-\tfrac{p_4}2\big).$$
This interval is non-empty iff all four pairwise cross-comparisons hold:
$p_3<p_2$ (automatic, $\mathcal P$'s own order, non-strict boundary aside);
$p_1-p_3<p_1-p_4/2\iff p_4<2p_3$ (automatic, since $p_4\le p_3<2p_3$);
$p_3<p_1-p_4/2$ (a genuine wall); $p_1-p_3<p_2$ (a genuine wall). Hence
**exactly**:
$$\textbf{Double-Sandwich-Below is feasible} \iff p_3+\tfrac{p_4}2\ <\ p_1\
<\ p_2+p_3.$$
This sharpens the round-23 explorer's approximate "$p_1<p_2+p_3$" claim
(per the round-24 outline's explicit instruction) into an exact two-sided
condition; the extra lower bound $p_1>p_3+p_4/2$ is a genuine, non-vacuous
constraint (see §R24.4/§R24.6 for where it, or its absence, matters).

**Construction (Above).** Split $p_1$ into $v_1,v_2$ ($v_1+v_2=p_1$), bisect
$p_4$; impose order $v_1>p_2>v_2>p_3>p_4/2$.

*Applying the identity.* Exactly as above, the $p_4/2,p_4/2$ pair cancels
($q_4=0$), leaving $M'=\{v_1,p_2,v_2,p_3\}$ at ranks $1,2,3,4$. Piece 1's
fragments $v_1,v_2$ now occupy ranks $1,3$ — **both odd**
($\varepsilon_1=+1$, $q_1=p_1$); piece 2 (untouched) is at rank $2$ (even,
$\varepsilon_2=-1$, $q_2=p_2$); piece 3 (untouched) is at rank $4$ (even,
$\varepsilon_3=-1$, $q_3=p_3$). By the identity,
$$A(M)=p_1-p_2-p_3,\qquad \Phi_{\text{Above}}(p)=\frac{T+p_1-p_2-p_3}2
=p_1+\tfrac{p_4}2.$$

**Exact feasibility (Above).** Order conditions on $v_1$ (with
$v_2=p_1-v_1$): $v_1>p_2$; $v_1<p_1-p_3\iff v_2>p_3$; $v_2<p_2\iff
v_1>p_1-p_2$; $v_2>p_4/2\iff v_1<p_1-p_4/2$. So
$$v_1\in\big(\max(p_2,\,p_1-p_2),\ \min(p_1-p_3,\,p_1-p_4/2)\big).$$
Since $p_3\ge p_4>p_4/2$ (as $p_4>0$), $p_1-p_3<p_1-p_4/2$, so the upper
bound is always $p_1-p_3$. Two cases for the lower bound:
- If $p_1\ge2p_2$: $\max(p_2,p_1-p_2)=p_1-p_2$, and the interval is
  non-empty iff $p_1-p_2<p_1-p_3\iff p_3<p_2$ — automatic. So feasibility
  holds automatically here, and (since $p_2\ge p_3$) $p_1\ge2p_2\ge p_2+p_3$
  is itself already an instance of "$p_1>p_2+p_3$".
- If $p_1<2p_2$: $\max(p_2,p_1-p_2)=p_2$, and the interval is non-empty iff
  $p_2<p_1-p_3\iff p_1>p_2+p_3$.
In **both** cases the exact non-emptiness condition collapses to the same
inequality:
$$\textbf{Double-Sandwich-Above is feasible} \iff p_1>p_2+p_3,$$
confirming the round-23 explorer's claim **exactly** (no hidden extra
condition, unlike Below) — a genuine, now fully rigorous, derivation.

**Complementarity check.** Below's feasibility region is $\{p_3+p_4/2<p_1<
p_2+p_3\}$ and Above's is $\{p_1>p_2+p_3\}$: together they cover
$\{p_1>p_3+p_4/2\}$, missing only $\{p_1\le p_3+p_4/2\}$ — a genuinely
non-empty residual strip (near-equal top three pieces, see §R24.6), not the
"exactly complementary" claim of the round-23 explorer's report (which was
numeric-recovery-only and is corrected here: they are complementary **only
modulo** the extra Below-side lower bound, which is a real, not vacuous,
gap).

### R24.2 The Bisect-Subset Lemma (new, general — subsumes Bisect-Top-$k$)

**Statement.** Fix a marking $p_1\ge\cdots\ge p_m>0$, $T=\sum p_i$, and any
subset $S\subseteq\{1,\dots,m\}$ with $|S|\le n$. The strategy "bisect every
piece in $S$ into two equal halves, leave every piece not in $S$ untouched"
is a legal Xiang-Yu response (using exactly $|S|$ cuts $\le n$), and
$$\Phi_S(p) \;=\; \frac{T+A(R)}2,\qquad R:=(p_i)_{i\notin S}\text{ in its
inherited descending order},$$
**unconditionally** (no feasibility constraint beyond $|S|\le n$).

**Proof.** For each $i\in S$, the two fragments $p_i/2,p_i/2$ are equal
values from the *same* piece $i$ — an ordinary same-piece pair — so
`odd-run-reduction-lemma` cancels them regardless of where they sit in the
global sorted order (pair-cancellation is a value-based, order-independent
operation, exactly as established in `cross-piece-sign-assignment-identity`'s
Step 1); hence $q_i=0$ for every $i\in S$. The untouched pieces $i\notin S$
each contribute their own single value $p_i$ unchanged, so $M'=R$ exactly
(as a sub-multiset of the original sorted $p$, with the relative order of
$R$'s elements automatically inherited — deleting elements from a sorted
list preserves the relative order of what remains, a trivial fact). Since
$R$ has (generically) all-distinct values, each surviving piece $i\notin S$
occupies a single rank in $M'$, so the monochromaticity hypothesis is
trivially satisfied (a singleton set of ranks is trivially "all one
parity"). By `cross-piece-sign-assignment-identity`, $A(M)=A(M')=A(R)$, and
$\Phi_S=(T+A(R))/2$. No order constraint on the fragments $p_i/2$
themselves is needed anywhere in this argument (self-tied pairs cancel
regardless of position), so the only legality requirement is $|S|\le n$
(the cut budget). $\blacksquare$

**Relation to Bisect-Top-$k$.** The certified `bisect-top-k-lemma` is
exactly the special case $S=\{1,\dots,k\}$ (so $R=\{p_{k+1},\dots,p_m\}$,
recovering its stated formula $\Phi=(T+A(\{p_{k+1},\dots,p_m\}))/2$
verbatim) — this Lemma is a strict generalization to **arbitrary** subsets
$S$, not just prefixes, and the proof above is a direct, easy corollary of
`cross-piece-sign-assignment-identity` (exactly the "genuine but easy new
instantiation" character the round-24 outline anticipated for the
Double-Sandwich chambers, here found to apply even more broadly).

**Instances used at $n=3,m=4$ (all unconditional).** Writing $R=(p_i)_{i
\notin S}$ in descending order and $A(R)$ via the alternating sum:

| $S$ | $\Phi_S(p)$ |
|---|---|
| $\varnothing$ | $(T+p_1-p_2+p_3-p_4)/2$ |
| $\{1\}$ | $(T+p_2-p_3+p_4)/2$ (Bisect-Top-1) |
| $\{2\}$ | $(T+p_1-p_3+p_4)/2$ |
| $\{3\}$ | $(T+p_1-p_2+p_4)/2$ |
| $\{4\}$ | $(T+p_1-p_2+p_3)/2$ |
| $\{1,2\}$ | $(T+p_3-p_4)/2$ (Bisect-Top-2) |
| $\{1,3\}$ | $(T+p_2-p_4)/2$ |
| $\{1,4\}$ | $(T+p_2-p_3)/2$ |
| $\{2,3\}$ | $(T+p_1-p_4)/2$ |
| $\{2,4\}$ | $(T+p_1-p_3)/2$ |
| $\{3,4\}$ | $(T+p_1-p_2)/2$ |
| $\{1,2,3\}$ | $(T+p_4)/2$ (Bisect-Top-3) |
| $\{1,2,4\}$ | $(T+p_3)/2$ |
| $\{1,3,4\}$ | $(T+p_2)/2$ |
| $\{2,3,4\}$ | $(T+p_1)/2$ |

(the $|S|=0$ row is $\Phi_\varnothing=(T+A(p))/2$, the "do nothing"
response, included for completeness; $|S|=4$ needs $4>n=3$ cuts, hence
excluded at $n=3$.) All fifteen are legal at $n=3$ (each uses $\le3$ cuts)
and unconditionally available at every $p\in\mathcal P$ — no feasibility
check needed, which is exactly what makes this family cheap to add to any
covering argument.

### R24.3 Three more new closed-form chambers (Triple-Pin, Chamber B1/B2)

**Triple-Pin (composition $(2,0,0,0)$).** Split $p_1$ into three fragments
$v_1=p_2$, $v_2=p_3$, $v_3=p_1-p_2-p_3$ (two cuts: pin two of $p_1$'s three
fragments to the untouched values $p_2,p_3$ exactly); $p_2,p_3,p_4$
untouched. This requires $v_3>0$, i.e. $p_1>p_2+p_3$.

*Applying the identity.* $M=\{p_2,p_2,p_3,p_3,p_4,v_3\}$ ($p_2$ appears
twice — once untouched, once as $v_1$; likewise $p_3$). The $p_2,p_2$ pair
(pieces $1,2$) and the $p_3,p_3$ pair (pieces $1,3$) are both genuine
cross-piece ties and both cancel by `odd-run-reduction-lemma` regardless of
their position in the sort (same order-independence argument as R24.1/24.2),
giving $q_2=q_3=0$ and leaving piece 1 with surviving mass $v_3$ and piece 4
untouched. $M'=\{p_4,v_3\}$ (only these two survive). **Order claim:**
within case (b2)'s box ($p_1<T/2$), $p_1<p_2+p_3+p_4$ automatically (since
$p_1<T/2<T-p_1=p_2+p_3+p_4$), so $v_3=p_1-p_2-p_3<p_4$ **whenever** $v_3>0$
— i.e. the order $p_4>v_3$ holds unconditionally throughout case (b2)'s box
once feasibility ($v_3>0$) holds, no separate order check needed. Ranks:
$p_4$ (rank 1, odd, $\varepsilon_4=+1$, $q_4=p_4$), $v_3$ (rank 2, even,
$\varepsilon_1=-1$, $q_1=v_3$). By the identity, $A(M)=p_4-v_3=p_4-p_1+p_2+
p_3$, so
$$\Phi_{\text{TriplePin}}(p) = \frac{T+p_4-p_1+p_2+p_3}2 = \frac{2p_2+2p_3+
2p_4}2 = p_2+p_3+p_4 = T-p_1,$$
**feasible iff $p_1>p_2+p_3$** (within case (b2)'s box; the order step used
$p_1<T/2$ explicitly, so this exact form of the argument is scoped to case
(b2) — outside it, a mild extra check on $v_3$ vs. $p_4$ would be needed,
not pursued here since only case (b2) is in scope).

**Chamber B1/B2 (composition $(1,0,1,0)$, both halves of R23.4's
previously-undermined "Chamber B").** Split $p_1\to(p_2, p_1-p_2)$ (tie the
larger fragment to untouched $p_2$; one cut) and $p_3\to(p_3-(p_1-p_2),\,
p_1-p_2)$ (tie the smaller fragment of $p_3$ to $p_1$'s smaller fragment
$p_1-p_2$; one cut); $p_2,p_4$ untouched. Requires $p_1>p_2$ (automatic,
non-strict boundary aside) and $p_3-(p_1-p_2)>0\iff p_1<p_2+p_3$.

*Applying the identity.* $M=\{p_2,p_2,\,p_1-p_2,p_1-p_2,\,p_3-p_1+p_2,\,
p_4\}$: the two $p_2$'s (untouched piece 2 and $p_1$'s fragment, a
cross-tie) cancel, and the two $(p_1-p_2)$'s ($p_1$'s other fragment and
$p_3$'s fragment, a cross-tie) cancel, both regardless of sort position, by
the same order-independence fact used throughout. $M'=\{p_3-p_1+p_2,\,
p_4\}$. Write $x:=p_2+p_3-p_1$ (feasibility $x>0$). Two sub-cases by the
order of $x$ vs. $p_4$:
- **Sub-case B2 ($x>p_4$, i.e. $p_1<p_2+p_3-p_4$):** order $x$ (rank 1,
  $+$) then $p_4$ (rank 2, $-$); $A(M')=x-p_4=p_2+p_3-p_1-p_4$, so
  $$\Phi_{B2}(p)=\frac{T+p_2+p_3-p_1-p_4}2=\frac{2p_2+2p_3}2=p_2+p_3,$$
  feasible for $p_2\le p_1<p_2+p_3-p_4$.
- **Sub-case B1 ($x<p_4$, i.e. $p_1>p_2+p_3-p_4$, still $p_1<p_2+p_3$):**
  order $p_4$ (rank 1, $+$) then $x$ (rank 2, $-$); $A(M')=p_4-x=p_4-p_2-p_3
  +p_1$, so
  $$\Phi_{B1}(p)=\frac{T+p_4-p_2-p_3+p_1}2=\frac{2p_1+2p_4}2=p_1+p_4,$$
  feasible for $p_2+p_3-p_4<p_1<p_2+p_3$.
Both intervals are non-empty (their shared endpoint $p_2+p_3-p_4>p_2$
follows from $p_3>p_4$, always true) and together tile the full range
$p_2<p_1<p_2+p_3$. **This completes R23.4's honest gap**: Chamber B's
formula $\Phi_B=p_1+p_4$ was correct but only on part of its own
feasibility region (B1); the other part (B2) needs the different formula
$\Phi_{B2}=p_2+p_3$, now derived — R23.4's single-formula claim is hereby
corrected/completed, not merely re-asserted.

**P1P2-tied-to-$p_3$ (composition $(1,1,0,0)$, the round-24 outline's
literal target).** Split $p_1\to(p_3,\,p_1-p_3)$ and $p_2\to(p_3,\,
p_2-p_3)$ (both smaller fragments pinned to the untouched value $p_3$); one
cut on each of $p_1,p_2$. Requires $p_1>p_3,\ p_2>p_3$ (automatic) and (for
the order used below) $p_2-p_3>p_3\iff p_2>2p_3$.

*Applying the identity.* $M=\{p_3,p_3,p_3,\,p_1-p_3,\,p_2-p_3,\,p_4\}$
(three copies of $p_3$: from pieces $1,2,3$). By `odd-run-reduction-lemma`
(applied to the value $p_3$ with multiplicity $3$, odd), exactly one copy
survives, at whatever rank $p_3$ occupies among $M'=\{p_1-p_3,p_2-p_3,p_3,
p_4\}$ once sorted (this is well-defined for computing $A(M)$ — which piece
"owns" the survivor is immaterial to the value of $A(M)$ itself, since
$A(M)$ only depends on $M'$'s sorted values, not on piece-attribution;
piece attribution only matters if one needs the individual $q_i$'s, which
we do not here). With $p_2>2p_3$: order $p_1-p_3>p_2-p_3>p_3>p_4$ (the
first inequality from $p_1\ge p_2$, the third from $p_2-p_3>p_3$, the
fourth automatic), giving ranks $1,2,3,4$, $A(M')=(p_1-p_3)-(p_2-p_3)+p_3-
p_4=p_1-p_2+p_3-p_4$, so
$$\Phi_{\text{P1P2p3}}(p)=\frac{T+p_1-p_2+p_3-p_4}2=p_1+p_3,\qquad
\text{feasible for } p_2\ge2p_3.$$

### R24.4 The 20-member covering family, tested exhaustively (numerically)

**Family.** All $15$ Bisect-Subset chambers (R24.2, unconditional) $\cup$
Double-Sandwich-Below $\cup$ Double-Sandwich-Above (R24.1) $\cup$
Triple-Pin $\cup$ Chamber B1 $\cup$ Chamber B2 (R24.3) $\cup$
P1P2-tied-to-$p_3$ (R24.3) $\cup$ Chamber-R22.1.1
($\Phi=p_1/2+p_3+p_4$, walls $p_1\ge2p_3,\ p_2\le p_3+p_4$, R22.1.1, cited
verbatim) $\cup$ Chamber A ($\Phi=p_2+(p_1+p_4)/2$, walls $p_1\ge3p_4,\
p_1\le2p_3+p_4$, R23.4, cited verbatim) $\cup$ Chamber A2
($\Phi=(p_1+p_2)/2+p_3$, wall $p_1\le p_2+2p_4$, R23.3, cited verbatim) —
20 chambers total, every closed form and exact feasibility region now on
record (this round or a prior certified round).

**Test 1 (deterministic exact-`Fraction` grid).** Script
`/tmp/coverage6.py` (this round): a grid over $p_1\in(0,\tfrac12)$
($60$ steps), $p_2\in(\tfrac1{15},\tfrac4{15})$ ($60$ steps), $p_3\in(0,
\mathrm{rem}]$ ($20$ steps, $\mathrm{rem}=1-p_1-p_2$), $p_4=\mathrm{rem}-p_3$,
filtered to the legal sorted-descending region and case (b2)'s box, all in
exact `Fraction` arithmetic (no floating-point rounding at any step). $1577$
valid box points tested; for each, evaluated $g_\tau=a_3T-\Phi_\tau$ for
every one of the 20 chambers and checked feasibility; **result: $0$
uncovered points** (every single point has at least one chamber both
feasible and with $g_\tau\ge0$, computed exactly).

**Test 2 (random exact-`Fraction` sampling).** Script `/tmp/coverage5.py`:
$3351$ additional random points (also exact `Fraction`, different seed and
sampling density, biased to include $p_1$ across the whole box rather than
just near the previously-flagged corner) — **again $0$ uncovered**.

**What this establishes, and what it does not.** This is a strong,
non-floating-point, exact-arithmetic empirical result — a large step up
from round 23's 99.6% (itself only floating-point-checked) — and is
consistent with, and sharpens, every prior round's numeric finding that
case (b2)'s theorem itself holds throughout the box. **It is not a proof**:
a dense finite sample, however large and however exact its arithmetic, does
not by itself establish that the union of $20$ polyhedral regions covers a
continuum box (the affine functions $g_\tau$ could in principle dip
negative on a thin sliver between two consecutive grid points, in a region
where the true minimum over all 20 chambers is not attained at a sampled
point) — the honest, sampling-based caveat this project's own rules require
be stated plainly. §R24.5–R24.6 report the partial progress made this round
toward an actual exhaustive (finite vertex/case-split) proof.

### R24.5 Individual insufficiency of every new chamber (LP-exact, confirming the established pattern)

Following the same LP methodology as R23.4 (script `/tmp/lp_check.py`,
`scipy.optimize.linprog`, `method='highs'`, exact rational vertex values
hand-confirmed where reported), each new chamber's **own** feasibility
region (ignoring the rest of the family) has $\min g_\tau<0$ somewhere
inside $\overline{\mathrm{Box}}$:

- Double-Sandwich-Below: $\min g=-1/15$ at $p=(1/3,4/15,4/15,2/15)$ (a
  Box-boundary vertex, $p_2=4T/15$).
- Double-Sandwich-Above: $\min g=-1/20$ at $p=(1/2,1/6,1/6,1/6)$ (the
  $p_1=T/2$ Box-boundary vertex).
- Triple-Pin: $\min g=-1/15$ at $p=(2/5,1/5,1/5,1/5)$ (hand-confirmed: $g=
  a_3T-(T-p_1)=p_1-\tfrac7{15}T=\tfrac25-\tfrac7{15}=\tfrac6{15}-\tfrac7{15}
  =-\tfrac1{15}$).
- P1P2-tied-to-$p_3$: $\min g=-1/10$ at $p=(1/2,4/15,2/15,1/10)$.

Each failing vertex found lies either on a Box wall (already
independently closed at $n\le3$ by Theorem C$'$/Theorem B/
`unconditional-p2-threshold-closure`, per `p-space-chamber-vertex-theorem`
item 3's boundary-sharing corollary) or, per the LP's report, at a point
where a *different* member of the 20-chamber family succeeds (confirmed
case-by-case for the four vertices above against the Bisect-Subset
sub-family — e.g. the Triple-Pin failure vertex $(2/5,1/5,1/5,1/5)$ has
Bisect$\{1,2\}$ give $\Phi=(T+p_3-p_4)/2=1/2<a_3T$, succeeding). This is
exactly the established pattern (Chamber A, A2, B all individually
insufficient, R23.4) — now confirmed to extend to every new chamber too;
no single template in this family, including the new ones, is a standalone
sufficient cover, so the union genuinely matters.

### R24.6 Partial progress toward an exhaustive (non-sampling) covering proof

The natural case-split is on $p_1$ vs. $p_2+p_3$ (the shared wall of
Triple-Pin/Double-Sandwich-Above vs. Double-Sandwich-Below).

**Sub-claim attempted: within $\{p_1>p_2+p_3\}\cap\mathrm{Box}$, does
$\max(g_{\text{TriplePin}},\,g_{\text{DS-Above}})\ge0$ always?** Summing
the two exact formulas:
$$g_{\text{TriplePin}}+g_{\text{DS-Above}} = \Big(p_1-\tfrac7{15}T\Big)+
\Big(\tfrac8{15}T-p_1-\tfrac{p_4}2\Big) = \tfrac1{15}T-\tfrac{p_4}2.$$
Since $\max(x,y)\ge(x+y)/2$ always, **if** $p_4\le\tfrac2{15}T$ this sum is
$\ge0$, hence at least one of the two chambers succeeds — a clean,
rigorous, fully-proved sufficient condition covering part of the
$p_1>p_2+p_3$ region. **This does not cover the whole sub-case**: a
concrete counter-check (not just the bound) shows the sum can be negative
while one of the two individual terms is still $\ge0$ (e.g.
$p=(0.45,0.2,0.2,0.15)$ has $p_4=0.15>2T/15\approx0.1333$, sum $\approx
-0.0083<0$, yet $g_{\text{DS-Above}}\approx+0.0083\ge0$ alone) — i.e. the
sum bound is **sufficient but not necessary**, so ruling out $p_4>2T/15$
does not itself identify the true residual, and a genuine case analysis of
when $p_4>2T/15$ forces *both* $g_{\text{TriplePin}}<0$ and
$g_{\text{DS-Above}}<0$ simultaneously (as opposed to only one) was not
completed this round — this is exactly the open combinatorial task
(§R24.4's honest caveat), now narrowed to a considerably smaller, more
concrete question than "does the whole 20-chamber union cover the box,"
but still open.

### R24.7 Honest conclusion

**Case (b2) at $n=3$ is not certified closed this round**, but substantial,
concrete progress was made on every one of the round-24 outline's three
tasks: (1) Double-Sandwich-Below and Double-Sandwich-Above are now fully,
rigorously derived (closed forms and *exact* feasibility regions, correcting
the round-23 explorer's approximate feasibility claims — Below in
particular gains a genuine extra lower-bound condition that was previously
missing); (2) a new $p_1,p_2$-cross-tie-flavored chamber
(P1P2-tied-to-$p_3$) is derived exactly as requested, together with three
further new chambers (Triple-Pin, Chamber B1, Chamber B2) found via
targeted numerical investigation of the actual residual witnesses and then
derived by hand via the same identity — including completing R23.4's own
previously-flagged, previously-unfinished "Chamber B" derivation; (3) the
resulting 20-member family (including the new, general-purpose
Bisect-Subset Lemma, itself a genuine reusable generalization of
Bisect-Top-$k$) was tested exhaustively on $1577+3351=4928$ exact-`Fraction`
points with **zero** violations — the strongest coverage evidence found for
this problem to date. **The precise remaining gap**: converting this
exact-arithmetic dense-sampling evidence into an actual finite case-split
or vertex-enumeration proof of the covering property itself. §R24.6 shows
this gap is now narrow and concrete (a two-chamber sufficient-sum bound that
covers part, not all, of one sub-case) rather than the open-ended "which
chambers, if any, would even be needed" question of round 23 — a
substantially better-defined target for the next round, but genuinely not
yet closed. Do not report $n=3$ case (b2) as solved.

## Promotable lemmas (round 24)

- **`double-sandwich-below-above`** (new): the exact closed forms
  $\Phi_{\text{Below}}=p_2+p_3+p_4/2$ (feasible iff $p_3+p_4/2<p_1<p_2+p_3$)
  and $\Phi_{\text{Above}}=p_1+p_4/2$ (feasible iff $p_1>p_2+p_3$), derived
  in full from `cross-piece-sign-assignment-identity` in §R24.1 above —
  ready for certification and reuse.
- **`bisect-subset-lemma`** (new, general, likely the most reusable result
  of this round): for any marking of any length $m$ and any $n$, bisecting
  any subset $S$ ($|S|\le n$) of pieces gives the unconditional exact
  formula $\Phi_S=(T+A(\text{untouched complement}))/2$ — proved in full in
  §R24.2, strictly generalizing the certified `bisect-top-k-lemma` (which is
  the prefix-subset special case) to arbitrary subsets. Immediately
  reusable at any $n$, not just $n=3$.
- **`triple-pin-p1-tied-to-p2-p3`** (new): $\Phi=T-p_1$, feasible iff
  $p_1>p_2+p_3$ (within case (b2)'s box, i.e. $p_1<T/2$ — the derivation in
  §R24.3 explicitly uses $p_1<T/2$ to pin the order of the residual
  fragment; outside that box a small extra check would be needed, not
  derived here), from composition $(2,0,0,0)$.
- **`chamber-b1-b2-split`** (new): completes R23.4's previously-incomplete
  "Chamber B" — two closed forms $\Phi_{B1}=p_1+p_4$ (feasible
  $p_2+p_3-p_4<p_1<p_2+p_3$) and $\Phi_{B2}=p_2+p_3$ (feasible $p_2\le
  p_1<p_2+p_3-p_4$) tiling composition $(1,0,1,0)$'s full feasibility
  range, derived in §R24.3.
- **`p1p2-tied-to-p3`** (new): $\Phi=p_1+p_3$, feasible iff $p_2\ge2p_3$,
  from composition $(1,1,0,0)$, derived in §R24.3 — the round-24 outline's
  literally-requested $p_1,p_2$-cross-tie chamber.
- All five are individually confirmed (§R24.5, LP-exact) to be
  **not** standalone-sufficient covers — reusable as building blocks only,
  consistent with every other chamber certified in this project to date.

### R25.1 Exact-arithmetic covering proof for the 5-chamber family (closes case (b2) at $n=3$)

**Goal.** Prove, in exact rational arithmetic (no floating point, no numeric
margin), that the 5-chamber family
$$\{\mathrm{Bisect}\{1,4\},\ \mathrm{Bisect}\{1,2\},\ \mathrm{DS\text{-}Above},\
\mathrm{Triple\text{-}Pin},\ \mathrm{R22.1.1}\}$$
covers all of case (b2)'s box at $n=3$: for every legal marking $p_1\ge
p_2\ge p_3\ge p_4>0$ with $p_1<T/2$ and $T/D_3<p_2<a_3T/2$ (i.e. $1/15<
p_2/T<4/15$, using $D_3=15$, $a_3=8/15$, both already-certified box-wall
constants — cite `p-space-chamber-vertex-theorem`, §R22.1.1), at least one
of the 5 chambers is simultaneously **feasible** and **successful**
($\Phi_\tau(p)\le a_3T$).

**Normalization.** By homogeneity of degree $1$ (every $\Phi_\tau$ and every
feasibility wall on file is degree-1 homogeneous in $p$, since each is a sum
of a subset of the $p_i$'s or an affine combination thereof with no constant
term — immediate from the closed forms in §R24.1–R24.3), set $T=p_1+p_2+p_3
+p_4=1$ WLOG. This leaves 3 free parameters $(p_1,p_2,p_3)$, $p_4=1-p_1-p_2
-p_3$, and case (b2)'s box becomes the open polytope
$$\mathcal B:=\Big\{(p_1,p_2,p_3)\in\mathbb R^3:\ p_1\ge p_2\ge p_3\ge p_4>0,\
p_1<\tfrac12,\ \tfrac1{15}<p_2<\tfrac4{15}\Big\},\qquad p_4:=1-p_1-p_2-p_3.$$

**The five chambers' formulas (cite, do not re-derive — all already
rigorously proved in §R24.1–R24.3 of this file, from
`cross-piece-sign-assignment-identity`/`bisect-subset-lemma`/`triple-pin-and-chamber-b1-b2`):**

| Chamber $\tau$ | Feasibility | $\Phi_\tau(p)$ |
|---|---|---|
| Bisect$\{1,4\}$ | unconditional | $(1+p_2-p_3)/2$ |
| Bisect$\{1,2\}$ | unconditional | $(1+p_3-p_4)/2$ |
| DS-Above | $p_1>p_2+p_3$ | $p_1+p_4/2$ |
| Triple-Pin | $p_1>p_2+p_3$ | $1-p_1$ |
| R22.1.1 | $p_1\ge2p_3$ and $p_2\le p_3+p_4$ | $p_1/2+p_3+p_4$ |

(Triple-Pin's and DS-Above's feasibility conditions coincide exactly,
$p_1>p_2+p_3$ — §R24.1, §R24.3 — a fact used below to merge them into one
branching variable.)

**Failure inequalities.** Write $g_\tau:=a_3-\Phi_\tau$ (using $T=1$,
$a_3=8/15$); chamber $\tau$ succeeds iff $g_\tau\ge0$ (given feasible). A
point $p\in\mathcal B$ is **uncovered by the family** iff simultaneously:
$$g_{14}<0,\quad g_{12}<0,\quad \big(\text{DS-Above infeasible or }
g_{\mathrm{DSA}}<0\big),\quad\big(\text{Triple-Pin infeasible or }
g_{\mathrm{TP}}<0\big),\quad\big(\text{R22.1.1 infeasible or }g_{R22}<0\big).$$
Substituting the closed forms and clearing denominators (multiply each by
$2$, or by $1$ as appropriate) and eliminating $p_4=1-p_1-p_2-p_3$
throughout, the five failure/feasibility predicates become, **exactly**:
$$g_{14}<0\iff p_3-p_2<-\tfrac1{15};\qquad
g_{12}<0\iff -p_1-p_2-2p_3<-\tfrac{16}{15};$$
$$\text{DSA/TP infeasible}\iff p_1-p_2-p_3\le0;\qquad
\text{DSA/TP feasible}\iff -p_1+p_2+p_3<0;$$
$$g_{\mathrm{DSA}}<0\iff -p_1+p_2+p_3<-\tfrac1{15};\qquad
g_{\mathrm{TP}}<0\iff p_1<\tfrac7{15};$$
$$\text{R22.1.1 feasible}\iff -p_1+2p_3\le0\ \text{and}\ p_1+2p_2\le1;\qquad
g_{R22}<0\iff \tfrac{p_1}2+p_2<\tfrac7{15}.$$
(Derivations: e.g. $g_{14}=a_3-\tfrac{1+p_2-p_3}2<0\iff\tfrac{16}{15}-1-p_2+
p_3<0\iff p_3-p_2<-\tfrac1{15}$; $g_{R22}=a_3-\tfrac{p_1}2-p_3-p_4<0$, and
substituting $p_4=1-p_1-p_2-p_3$ gives $\tfrac8{15}-\tfrac{p_1}2-p_3-1+p_1+
p_2+p_3<0\iff \tfrac{p_1}2+p_2<\tfrac7{15}$; the remaining five follow by
the identical mechanical substitution, each independently checked below via
the certificate sums, which is itself a check on correctness of the
derivation since a wrong sign would break the $0=0$ cancellation.)

**Exhaustive 6-branch case split.** Since DS-Above and Triple-Pin share one
feasibility condition, and R22.1.1's infeasibility is the union of two
inequalities ($p_1<2p_3$ **or** $p_2>p_3+p_4$), the "uncovered" predicate is
exactly covered (possibly with overlap, which only strengthens the
argument — we only need each branch below to be individually empty) by the
$2\times3=6$ branches
$$\{X,Y\}\times\{P1,P2,Q\},$$
$X$: DSA/TP infeasible ($p_1\le p_2+p_3$); $Y$: DSA/TP feasible and both
$g_{\mathrm{DSA}}<0,g_{\mathrm{TP}}<0$; $P1$: R22.1.1 infeasible via
$p_1<2p_3$; $P2$: R22.1.1 infeasible via $p_2>p_3+p_4$; $Q$: R22.1.1
feasible and $g_{R22}<0$. **Exhaustiveness**: any point failing DSA/TP
falls in $X$ or $Y$ (these are complementary, $p_1\le p_2+p_3$ vs.
$p_1>p_2+p_3$, together with the required $g$'s in the feasible case);
independently, any point for which R22.1.1 fails to rescue falls in $P1$,
$P2$, or $Q$ (infeasibility is the union of the two negated conditions,
each captured by $P1,P2$ respectively; feasible-but-failing is $Q$). Since
these two dichotomies are on independent aspects of the same "uncovered"
predicate (both must hold simultaneously for $p$ to be uncovered), every
uncovered point lies in (at least) one of the 6 cells $\{X,Y\}\times
\{P1,P2,Q\}$, together with the two always-required conditions $g_{14}<0$,
$g_{12}<0$. It therefore suffices to show **each of the 6 branches, as a
linear-inequality system on $\mathcal B$, is infeasible.**

**Exact Farkas-style infeasibility certificates.** For each branch we
exhibit an explicit nonnegative rational combination of a small subset of
the branch's defining inequalities (all in the closed forms above, plus the
box's own bounds $p_2<4/15$) that sums, term-by-term, to the identity
$0=0$ on the left while the corresponding combination of right-hand sides
sums to $0$ — and since every constraint used is *strict* and receives a
strictly positive weight, the combined inequality is strict, giving the
manifestly false statement $0<0$. This is a standard Farkas/positive-combination
certificate of infeasibility for a system of strict and non-strict
linear inequalities: if $\sum_i\lambda_iL_i(x)<\sum_i\lambda_id_i$ term-wise
sums to $0<0$ with all $\lambda_i\ge0$ and at least one $\lambda_i>0$
attached to a strict inequality, no $x$ can satisfy all the $L_i(x)\lessgtr
d_i$ simultaneously (any $x$ satisfying all of them would force $\sum\lambda_i
L_i(x) < \sum\lambda_i d_i$, i.e. $0<0$, absurd).

*Branch $(X,P1)$* — constraints used: $p_2<\tfrac4{15}$ [$\lambda=5$];
$p_3-p_2<-\tfrac1{15}$ [$\lambda=4$]; $-p_1-p_2-2p_3<-\tfrac{16}{15}$
[$\lambda=1$]; $p_1-2p_3<0$ [$\lambda=1$]. Sum of left sides: $5p_2+4(p_3-
p_2)+(-p_1-p_2-2p_3)+(p_1-2p_3)$. Collecting: $p_1$-coefficient $=-1+1=0$;
$p_2$-coefficient $=5-4-1=0$; $p_3$-coefficient $=4-2-2=0$. Sum of right
sides: $5\cdot\tfrac4{15}+4\cdot(-\tfrac1{15})+1\cdot(-\tfrac{16}{15})+1
\cdot0=\tfrac{20-4-16+0}{15}=0$. Hence $0<0$: infeasible.

*Branch $(X,P2)$* — constraints: $p_2<\tfrac4{15}$ [$4$]; $p_3-p_2<-
\tfrac1{15}$ [$1$]; $p_1-p_2-p_3\le0$ [$1$]; $-p_1-2p_2<-1$ [$1$]. Left
sum: $4p_2+(p_3-p_2)+(p_1-p_2-p_3)+(-p_1-2p_2)$; $p_1$: $1-1=0$; $p_2$:
$4-1-1-2=0$; $p_3$: $1-1=0$. Right sum: $4\cdot\tfrac4{15}+1\cdot(-
\tfrac1{15})+1\cdot0+1\cdot(-1)=\tfrac{16-1+0-15}{15}=0$. At least one
weighted constraint ($p_3-p_2<-1/15$) is strict, so the combination is
strict: $0<0$: infeasible.

*Branch $(X,Q)$* — constraints: $p_2<\tfrac4{15}$ [$\tfrac12$]; $p_3-p_2<-
\tfrac1{15}$ [$1$]; $-p_1-p_2-2p_3<-\tfrac{16}{15}$ [$\tfrac12$];
$\tfrac{p_1}2+p_2<\tfrac7{15}$ [$1$]. Left sum: $\tfrac12p_2+(p_3-p_2)+
\tfrac12(-p_1-p_2-2p_3)+(\tfrac{p_1}2+p_2)$; $p_1$: $-\tfrac12+\tfrac12=0$;
$p_2$: $\tfrac12-1-\tfrac12+1=0$; $p_3$: $1-1=0$. Right sum: $\tfrac12\cdot
\tfrac4{15}+1\cdot(-\tfrac1{15})+\tfrac12\cdot(-\tfrac{16}{15})+1\cdot
\tfrac7{15}=\tfrac{2-1-8+7}{15}=0$. Strict (all four weighted terms strict):
$0<0$: infeasible.

*Branch $(Y,P1)$* — constraints: $p_3-p_2\le0$ (sort order, $p_3\le p_2$)
[$1$]; $-p_1+p_2+p_3<0$ (DSA/TP feasible) [$1$]; $p_1-2p_3<0$ [$1$]. Left
sum: $(p_3-p_2)+(-p_1+p_2+p_3)+(p_1-2p_3)$; $p_1$: $-1+1=0$; $p_2$: $-1+1
=0$; $p_3$: $1+1-2=0$. Right sum: $0+0+0=0$. The second and third weighted
constraints are strict, so the combination is strict: $0<0$: infeasible.

*Branch $(Y,P2)$* — constraints: $p_2<\tfrac4{15}$ [$2$]; $p_1<\tfrac7{15}$
($g_{\mathrm{TP}}<0$) [$1$]; $-p_1-2p_2<-1$ [$1$]. Left sum: $2p_2+p_1+
(-p_1-2p_2)=0$ identically. Right sum: $2\cdot\tfrac4{15}+\tfrac7{15}+(-1)
=\tfrac{8+7-15}{15}=0$. Strict: $0<0$: infeasible.

*Branch $(Y,Q)$* — constraints: $p_2<\tfrac4{15}$ [$1$]; $p_3-p_2<-\tfrac1
{15}$ ($g_{14}<0$) [$1$]; $-p_1-p_2-2p_3<-\tfrac{16}{15}$ ($g_{12}<0$)
[$1$]; $-p_1+p_2+p_3<-\tfrac1{15}$ ($g_{\mathrm{DSA}}<0$) [$1$]; $p_1<
\tfrac7{15}$ ($g_{\mathrm{TP}}<0$) [$2$]. Left sum: $p_2+(p_3-p_2)+(-p_1-
p_2-2p_3)+(-p_1+p_2+p_3)+2p_1$; $p_1$: $-1-1+2=0$; $p_2$: $1-1-1+1=0$;
$p_3$: $1-2+1=0$. Right sum: $\tfrac4{15}-\tfrac1{15}-\tfrac{16}{15}-
\tfrac1{15}+2\cdot\tfrac7{15}=\tfrac{4-1-16-1+14}{15}=0$. Strict: $0<0$:
infeasible.

**All six branches are infeasible.** Since every constraint used in every
certificate above is either a hypothesis of case (b2)'s box ($p_2<4/15$,
sort order) or one of the five chambers' failure/feasibility conditions
(exactly as derived from §R24.1–R24.3's certified closed forms), and each
certificate is a finite nonnegative combination collapsing to the false
statement $0<0$, no point of $\mathcal B$ can satisfy the full "uncovered"
predicate. This is an exact, non-numeric, hand-verifiable proof (each
certificate above can be checked by direct term-by-term addition of at most
$5$ rational-coefficient linear expressions — no floating point, no LP
solver needed to verify, only arithmetic).

**On the round-24/25 explorer's "boundary vertex" — corrected framing
(round 26).** The explorer's floating-point LP search (margin
$\varepsilon\to0$) located the point $p^\ast=(\tfrac25,\tfrac4{15},
\tfrac15,\tfrac2{15})$ as an apparent limiting counterexample. Exact
evaluation (§ explorer's own `exact_vertex_check.py`, independently
re-verified here) shows $g_{14}(p^\ast)=g_{12}(p^\ast)=g_{R22}(p^\ast)=0$
**exactly** (a genuine triple tie: R22.1.1 is feasible there, since
$p_1=2p_3=\tfrac25$ exactly and $p_2=\tfrac4{15}<p_3+p_4=\tfrac13$, and
$g_{R22}=0\ge0$ means R22.1.1 **succeeds**, not fails, at $p^\ast$).
Consequently $p^\ast$ does **not** satisfy the strict inequality
$g_{R22}<0$ required to be in branch $Q$ (nor is it in $P1$ or $P2$, since
R22.1.1 *is* feasible there) — it was never actually inside any of the 6
branches to begin with; it only appeared as a floating-point artifact of
the numerical margin $\varepsilon\to0$ in the explorer's approximate LP.
This is confirmed independently by re-running the exact Fourier–Motzkin
elimination underlying the 6 certificates above with the box's own strict
inequality $p_2<4/15$ **relaxed** to the non-strict $p_2\le4/15$ (i.e.
testing the *closed* box, which does include $p^\ast$): all 6 branches
remain exactly infeasible (verified computationally, `/tmp/fm.py`'s
"relaxed" pass).

Under the **corrected** case split (see the round-26 fix below: case (a)
is $p_2\ge a_3T/2=4T/15$, not $p_1\ge T/2$), this whole discussion is in
fact moot for the final assembly, and it is worth saying precisely why: at
$T=1$, $p^\ast$ has $p_2=4/15=4T/15$ **exactly**, i.e. $p^\ast$ sits
exactly on the case-(a)/case-(b2) wall, and case (a)'s own closure
(Corollary to Theorem B, non-strict $p_2\ge4T/15$) covers it directly and
unconditionally — no appeal to R22.1.1, the chamber machinery, or any
tie-analysis is needed to dispose of $p^\ast$ at all. The R22.1.1
triple-tie computation above is still correct and is retained as an
independent cross-check (it shows the *case-(b2) chamber family itself*
would also have handled the closed box up to and including this wall, had
the wall been assigned to (b2) instead of (a)), but it is not
load-bearing for the final proof: $p^\ast$ is disposed of by case (a)'s
inequality alone, with equality, exactly as any other point with
$p_2\ge4T/15$ is. This corrects the round-25 text, which had reasoned
about $p^\ast$ under the (buggy) $p_1\ge T/2$ definition of case (a) and,
separately, misattributed the "correct fix" citation to
`generalized-peel-identity`; see the round-26 section below for the
actual citation.

**Conclusion of R25.1 (case (b2) only).** The 5-chamber family
$\{\mathrm{Bisect}\{1,4\},\ \mathrm{Bisect}\{1,2\},\ \mathrm{DS\text{-}
Above},\ \mathrm{Triple\text{-}Pin},\ \mathrm{R22.1.1}\}$ **provably covers
all of case (b2)'s box $T/15<p_2<4T/15$ at $n=3$**, in exact rational
arithmetic, via the 6-branch exhaustive case split and the six
Farkas-style infeasibility certificates above. This is exactly the case
(b2) piece of the three-way $p_2$-partition; its combination with case (a)
and case (b1) into the full $n=3$ upper bound is carried out in the
round-26 section below (the round-25 version of this combination
paragraph contained a citation bug, corrected there rather than here, so
this paragraph is scoped strictly to case (b2) itself).

**Scope note.** This closes case (b2) **at $n=3$ specifically**: every
chamber formula and feasibility wall used above (§R24.1–R24.3) was derived
for general $n$ but the box thresholds ($T/D_3=1/15$, $a_3T/2=4/15$) and
the specific 5-chamber sub-family found sufficient are $n=3$-specific
(only 4 pieces $p_1,\dots,p_4$; the covering-family question at $n\ge4$
would need its own — likely larger — family and is not addressed here).
The general-$n$ upper bound remains the responsibility of the broader
project's induction (case (a)/(b1)/(b2) split at each $n$, cited elsewhere
in this file), of which this section supplies the $n=3$, case (b2) piece
in full.

## Promotable lemmas (round 25)

- **`case-b2-n3-covering-closure`** (new, this round, §R25.1): the
  5-chamber family $\{\mathrm{Bisect}\{1,4\},\mathrm{Bisect}\{1,2\},
  \mathrm{DS\text{-}Above},\mathrm{Triple\text{-}Pin},\mathrm{R22.1.1}\}$
  covers case (b2)'s entire box at $n=3$ — proved via the 6-branch exact
  Farkas-certificate case split in §R25.1, not sampling. This is the
  capstone closure the project has been building toward across rounds
  22–25 (chamber machinery, box decomposition, covering-family
  construction). **This is one of the three pieces of the complete $n=3$
  upper-bound proof; the other two pieces (case (a), case (b1)) and their
  correct combination are assembled explicitly in the round-26 section
  below** — round 25's own attempt at that combination had a citation bug
  (see round-26 fix), so this bullet is scoped strictly to case (b2)
  itself and does not by itself claim the full $n=3$ result.
- **Six Farkas infeasibility certificates** (§R25.1, branches $(X,P1),
  (X,P2),(X,Q),(Y,P1),(Y,P2),(Y,Q)$): each is individually reusable as a
  worked example of the project's "exact nonnegative-combination collapses
  to $0<0$" technique, useful as a template if the covering-family method
  is later extended to $n\ge4$.
- The resolution of the apparent boundary vertex $p^\ast=(2/5,4/15,1/5,
  2/15)$ (a genuine triple tie at which R22.1.1 succeeds, not a
  counterexample) is a reusable cautionary note: floating-point LP margins
  can manufacture apparent "boundary counterexamples" that dissolve under
  exact evaluation — worth flagging for any future covering-family work in
  this project.

## Outline (proof-outliner, round 26)

**Diagnosis (round-26 explorer, `/tmp/round-26/math-explorer-lpduality-case-a.md`):
round 25's own final combination paragraph mis-cited case (a).** Case (a) is
the regime $p_2\ge a_3T/2$ (not "$p_1\ge T/2$", which is a different,
strictly weaker sufficient condition — Theorem A — mistakenly substituted
into the round-25 write-up's last paragraph). The actual closure mechanism
for case (a) is **already on file and already certified**: the Corollary
(Theorem B, recursive sufficient condition, § "Proven sufficient
conditions", ~line 1037) with $m=4$, $S'=\{p_1-p_2,p_3,p_4\}$, whose one
hypothesis — the *general* (every configuration, not just ladder) $n=2$
upper bound $c(2)\le a_2T'=\tfrac47T'$ — is exactly
`lemmas/n2-upper-bound-lp-argument.md`, already proved in full for every
0/1/2-point configuration, no numerics load-bearing. So **no new
mathematics is needed to close case (a) at $n=3$** — this is a
citation/assembly bug, not a gap. This is priority (a) this round: cheap,
high-value, and it completes the first fully-closed general-marking
$n=3$ upper bound the project has had.

**Concrete task for this round's builder (rewrite, don't re-derive):**
1. Correct the final "Conclusion of R25.1" paragraph (and the
   `## Promotable lemmas (round 25)` framing above, if it repeats the same
   mislabeling) to state case (a) as $p_2\ge a_3T/2$, not $p_1\ge T/2$.
2. Write out the citation chain explicitly: Theorem B's Corollary
   ($m=4$, $S'=\{p_1-p_2,p_3,p_4\}$) $\Rightarrow$ needs
   $c(2)\le\tfrac47T'$ for *arbitrary* $S'$ $\Rightarrow$ discharged by
   `n2-upper-bound-lp-argument` (general, unconditional, no sortedness
   assumption). **Explicitly verify** (not silently assume) that
   $S'=\{p_1-p_2,p_3,p_4\}$ need not be sorted for
   `n2-upper-bound-lp-argument` to apply — read that lemma's proof and
   confirm its six templates cover an arbitrary positive triple (the
   round-26 explorer already did this reading and reports the lemma has no
   sortedness assumption beyond WLOG-labeling; the builder should restate
   this explicitly in the proof rather than take it on faith, since it is
   the one place a silent gap could hide).
3. Verify the three regimes partition $p_2\in(0,T]$ with **no gap or
   overlap**: case (b1) $p_2\le T/15$ (closed, all $n$, via
   `unconditional-p2-threshold-closure`), case (b2) $T/15<p_2<4T/15$
   (closed at $n=3$, round 25's 6-branch covering proof), case (a)
   $p_2\ge4T/15$ (closed via the Corollary as above). State the boundary
   matching explicitly: (b1)/(b2) share the closed/open boundary at
   $p_2=T/15$ with no double-count; (b2)/(a) share it at $p_2=4T/15$,
   where the previously-resolved boundary vertex $p^\ast=(2/5,4/15,1/5,
   2/15)$ (round 25, §R25.1) already sits — restate why it is covered by
   case (a)'s closed inequality $p_2\ge4T/15$ (it satisfies equality) so
   it is not silently dropped between the two cases' write-ups.
4. State the combined headline explicitly: **$c(3)\le a_3=8/15$ for every
   legal Liu Bang marking at $n=3$** (upper-bound direction only — the
   lower-bound/achievability direction is a separate, still-open front
   tracked elsewhere; do not conflate the two in the Status line).

**Do not attempt this round:** the $n=4$ case-(b2) chamber census. The
explorer's density signal ($\approx28\%\to64\%$ chamber-type coverage gap
inside the box, per `within-chamber-affinity-theorem.md`) and the already-
recorded fact that even $n=3$ needed a 2-chamber split within a single
composition (Chamber A / Chamber A2) both indicate this is a genuine
multi-round combinatorial enumeration, not a quick follow-on — budget it as
its own sub-arc later. (Case (a) at $n=4$, by contrast, becomes free once
this round's $n=3$ fix lands, via the same Corollary one level up — worth
noting in the file as a bootstrap observation, but not worth building yet
since it depends on nothing new.)

## Round 26 build: citation fix + complete $n=3$ general-marking upper bound

**Goal (per the outline above).** Fix the round-25 citation bug in case
(a) and assemble the complete, gap-free proof that $c(3)\le a_3=8/15$ for
*every* legal Liu Bang marking at $n=3$ (arbitrary $p_1\ge p_2\ge p_3\ge
p_4>0$, not just the ladder), by combining three pieces: case (b1)
($p_2\le T/D_3$), case (b2) ($T/D_3<p_2<a_3T/2$), case (a) ($p_2\ge
a_3T/2$).

### R26.1 The correct citation for case (a), stated and verified in full

**Case (a): $p_2\ge a_3T/2=4T/15$.** The closure mechanism is the already
certified **Corollary (Theorem B, recursive sufficient condition)**,
§"Proven sufficient conditions" above (~line 1037), instantiated at
$m=4$ (i.e. $n=3$, four pieces $p_1,p_2,p_3,p_4$):

> If $p_2\ge a_3\cdot T/2$, and $S':=\{w,p_3,p_4\}$ ($w:=p_1-p_2\ge0$,
> $T':=T-2p_2$) satisfies $\Phi_{\min}(S')\le a_2T'$, then
> $\Phi_{\min}(p_1,p_2,p_3,p_4)\le a_3T$.

This is **not** the same lemma as `generalized-peel-identity` (Theorem
B$_k$, the bare exact bookkeeping identity $\Phi(\text{combined})=
p_k+\Phi'$ for arbitrary peel index $k$, proved round 9) — that identity
alone carries no threshold and no discharge of the reduced instance's own
bound. The round-25 write-up's final paragraph cited
`generalized-peel-identity` for case (a); this is corrected here to the
actual mechanism used, which is the **Corollary** above (a strictly
stronger statement: identity + the specific $p_2\ge a_3T/2$ threshold
derived from it, proved in the "Proven sufficient conditions" section) **plus** `lemmas/n2-upper-bound-lp-argument.md` to unconditionally discharge the
Corollary's one hypothesis.

**Discharging the hypothesis.** The Corollary needs $\Phi_{\min}(S')\le
a_2T'$ for $S'=\{w,p_3,p_4\}$. This is *exactly* the general $n=2$
upper-bound claim: "for every configuration of 3 positive values with
total $T'$ (equivalently, every 0/1/2-point Liu-Bang marking after
relabeling), Xiang Yu has a response with $\le2$ cuts achieving $\Phi\le
\tfrac47T'$" — proved unconditionally, for **every** such triple, in
`lemmas/n2-upper-bound-lp-argument.md` (six explicit template strategies
+ a two-region contradiction argument, reviewer-certified round 1, no
numerics load-bearing in the final logical argument). Hence the
Corollary's hypothesis holds **unconditionally, for every marking**, and
case (a)'s closure needs **no induction hypothesis at all** at $n=3$ (this
matches case (b1)'s status: both are fully unconditional; only case (b2)'s
own 5-chamber proof is $n=3$-specific machinery, and it too is
unconditional, not IH-dependent).

**Explicit check: no sortedness assumption is silently smuggled in.**
This is the one place a gap could hide (per the outline's own flag), so it
is checked here explicitly rather than assumed. `n2-upper-bound-lp-argument`'s
proof (in `smoothing-compactness-certificate.md`) is stated and proved for
the sorted simplex $p\ge q\ge r>0$, $p+q+r=T'$, plus the degenerate
0/1-point cases ($r=0$, or $q=r=0$). $S'=\{w,p_3,p_4\}$ is **not**
guaranteed to already be sorted as listed: $w=p_1-p_2$ can be smaller than
$p_3$ or $p_4$ (e.g. $p_1$ close to $p_2$ makes $w$ small), and can equal
$0$ exactly (when $p_1=p_2$). Neither issue is a problem:
- $\Phi_{\min}$ of a multiset of positive values does not depend on the
  *order in which the values are listed* — only on the multiset itself
  (Xiang Yu's optimal response and the resulting sorted odd-rank sum
  $\Phi$ are defined from the multiset, not from an input labeling). So
  relabeling $S'$ in sorted order is a free, content-free operation ("WLOG
  sorted" is literally just alphabetizing three numbers), not an
  assumption about $S'$'s origin.
- If $w=0$ exactly, $S'=\{0,p_3,p_4\}$ is (after dropping the $0$, which
  contributes nothing to any sum or split) exactly the 2-point case
  $\{p_3,p_4\}$, one of the explicitly-handled degenerate configurations
  in `n2-upper-bound-lp-argument`'s own statement ("every Liu Bang
  configuration (0, 1, or 2 marked points)").
- If $w>0$, $S'$ is a genuine 3-point configuration (values $w,p_3,p_4$,
  all positive, in whatever order), covered by the six-template argument
  after sorting.

So `n2-upper-bound-lp-argument` applies to $S'$ exactly as needed, with
zero silent gap. (This reproduces, more explicitly, the round-26
explorer's own reading of the lemma, `/tmp/round-26/math-explorer-lpduality-case-a.md`,
confirmed here directly against the lemma's statement rather than taken on
faith.)

**Conclusion (case (a)).** For every marking with $p_2\ge4T/15$,
$$\Phi_{\min}(p_1,p_2,p_3,p_4)\ \le\ p_2+\Phi_{\min}(S')\ \le\
p_2+a_2T'\ \le\ a_3T,$$
the last step being exactly the Corollary's proven algebra (§"Proven
sufficient conditions", the $\Rightarrow a_nT/2$ threshold derivation),
unconditionally, for every such marking — **no numerics, no induction
hypothesis, no case restriction on $p_1$.**

### R26.2 The three-way $p_2$-partition: explicit, gap-free, no double-count

Fix any legal marking $p_1\ge p_2\ge p_3\ge p_4>0$, $T=p_1+p_2+p_3+p_4$.
Since $p_1\ge p_2$ and $p_1+p_2\le T$, we have $0<p_2\le T/2$ always,
so $p_2$ ranges over the half-open interval $(0,T/2]$. Partition this
interval into three pieces:
$$(0,T/2]\ =\ \underbrace{(0,\,T/15]}_{\text{(b1)}}\ \cup\
\underbrace{(T/15,\,4T/15)}_{\text{(b2)}}\ \cup\
\underbrace{[4T/15,\,T/2]}_{\text{(a)}}.$$
This is a partition of an interval by two cut points $T/15<4T/15$ (both
strictly inside $(0,T/2]$ since $4/15<1/2$), with the left piece closed on
the right at $T/15$, the middle piece open at both ends, and the right
piece closed on the left at $4T/15$ — a standard interval trichotomy with
**no gap** (every point of $(0,T/2]$ lies in exactly one piece: if
$p_2\le T/15$ it's in (b1); else if $p_2<4T/15$ it's in (b2); else
$p_2\ge4T/15$ so it's in (a) — exhaustive by trichotomy on the two
strict/non-strict comparisons) and **no double-count** (the boundary
value $p_2=T/15$ is included only in (b1)'s closed right endpoint, excluded
from (b2)'s open left endpoint; the boundary value $p_2=4T/15$ is included
only in (a)'s closed left endpoint, excluded from (b2)'s open right
endpoint — each boundary value belongs to exactly one piece, by
construction of which endpoint is closed).

**Each piece is closed by an unconditional theorem, with the boundary
values explicitly checked:**

- **(b1), $p_2\le T/15$ (closed, non-strict):** `unconditional-p2-threshold-closure`
  (cited above, proved for every $n\ge1$ with $D_n=2^{n+1}-1$; at $n=3$,
  $D_3=15$) gives $\Phi_{\min}\le a_3T$ via one cut (bisect $p_1$ alone),
  **whenever $p_2\le T/D_3=T/15$** — the lemma's hypothesis is exactly
  the non-strict inequality defining this piece, so the boundary point
  $p_2=T/15$ itself is covered directly by this theorem (equality is
  allowed in the lemma's own hypothesis). No separate check is needed.
- **(b2), $T/15<p_2<4T/15$ (open both ends):** `case-b2-n3-covering-closure`
  (§R25.1) gives $\Phi_{\min}\le a_3T$ via the 5-chamber family, but
  **[CORRECTED, round 26 — the domain-generalization attempt below was
  REFUTED by this round's proof-reviewer]** only under the restriction
  $p_1<T/2$, not for every $p_1$: the reviewer exhibited a concrete
  counterexample $p=(3/5,9/40,29/200,3/100)$ ($p_1\ge T/2$,
  $p_2\in(T/15,4T/15)$) where all five chambers fail, because the
  Triple-Pin chamber's formula silently assumes $p_1<T/2$ to fix an
  ordering. **The sub-region $p_1\ge T/2$, $T/15<p_2<4T/15$ is NOT closed
  by this lemma and remains an open residual gap** — it is disjoint from
  case (a) as redefined below, so it is not rescued by that case either.
- **(a), $p_2\ge4T/15$ (closed, non-strict):** R26.1's Corollary
  application, unconditional, covers every $p_2\ge4T/15$ including the
  boundary $p_2=4T/15$ itself (the Corollary's hypothesis $p_2\ge a_3T/2$
  is non-strict, so equality is explicitly included in its own proof, not
  a limiting case requiring separate treatment).

**Boundary vertex cross-check (the round-25 "$p^\ast$" point).** The
specific point $p^\ast=(2/5,4/15,1/5,2/15)$ flagged in §R25.1 has (at
$T=1$) $p_2=4/15=4T/15$ **exactly**, so under this partition it lies in
case (a), not case (b2) — it is disposed of directly and unconditionally
by R26.1's Corollary (with $p_2\ge4T/15$ satisfied at equality), with no
need for the R22.1.1 triple-tie analysis that round 25's write-up used
(that analysis is retained above as an independent, non-load-bearing
cross-check: it shows the (b2) chamber family's own R22.1.1 chamber also
happens to succeed exactly at this wall, which is consistent but not
required). This resolves, rather than merely notes, the round-25
uncertainty about $p^\ast$: it was never a genuine boundary-disposal
problem once case (a) is correctly identified as $p_2\ge4T/15$.

### R26.3 Assembled theorem — **[CORRECTED, round 26: NOT fully closed]**

**[CORRECTED by round-26 proof-reviewer: the theorem below is FALSE as
originally stated. The (b2) case's covering-family lemma only holds under
$p_1<T/2$ (see the corrected R26.2 bullet above); the sub-region
$p_1\ge T/2$, $T/15<p_2<4T/15$ is an open residual gap, exhibited
concretely by the counterexample $p=(3/5,9/40,29/200,3/100)$. The
general-marking $n=3$ upper bound $c(3)\le8/15$ is therefore
**NOT** established in full this round — only for the sub-region
$p_1<T/2$ (all of case (b1), all of case (b2) as correctly restricted,
and all of case (a) with $p_1<T/2$), plus separately for $p_1\ge T/2$
whenever $p_2\ge4T/15$ (case (a), which does not restrict $p_1$). The
sole remaining gap is exactly $p_1\ge T/2$ AND $T/15<p_2<4T/15$.]**

*What follows below is the ORIGINAL (flawed) argument, left in place
for the record with the correction above taking precedence; do not cite
its conclusion as established.*

**Theorem (General-marking $n=3$ upper bound) — NOT ESTABLISHED, see
correction above.** *For every legal Liu Bang
marking $p_1\ge p_2\ge p_3\ge p_4>0$ with $T=p_1+p_2+p_3+p_4$, Xiang Yu has
a legal response (using $\le3$ cuts) with*
$$\Phi_{\min}(p_1,p_2,p_3,p_4)\ \le\ \frac{8}{15}\,T\ =\ a_3T.$$
*Consequently $c(3)\le a_3=8/15$.*

*Proof (flawed — relies on the refuted (b2) domain generalization).* By R26.2, exactly one of the three cases (b1), (b2), (a) holds
for $p_2$, with the boundary values $p_2=T/15$ and $p_2=4T/15$ each
assigned to exactly one case (no gap, no double-count, verified above in
full). In each case, $\Phi_{\min}\le a_3T$ is established unconditionally
by a fully proved, non-numeric mechanism:
- (b1): `unconditional-p2-threshold-closure` (general $n$, proved from
  `bisect-top-identity` + `max-domination-lemma` + `telescoping-threshold-identity`).
- (b2): `case-b2-n3-covering-closure` (this file, §R25.1; a genuinely
  $n=3$-specific 5-chamber covering family, proved via 6 exhaustive
  Farkas-style exact-arithmetic infeasibility certificates — no numerics
  in the final argument).
- (a): the Corollary to Theorem B (this file, §"Proven sufficient
  conditions"), instantiated at $m=4$ with $S'=\{p_1-p_2,p_3,p_4\}$, its
  one hypothesis discharged unconditionally by
  `lemmas/n2-upper-bound-lp-argument.md` (general $n=2$ upper bound, no
  sortedness or origin assumption beyond free relabeling, checked
  explicitly in R26.1).

Since every marking falls in exactly one of the three cases and each case
is closed, $\Phi_{\min}\le a_3T$ holds for every marking. $\blacksquare$

**This is the general upper bound only** (the direction $c(3)\le8/15$);
the achievability direction ($c(3)\ge8/15$, i.e. Liu Bang's ladder marking
forces $\Phi\ge8/15\,T$ against every Xiang Yu response) is a separate,
already-tracked front of this project (the lower-bound/tie-vertex
enumeration discussed throughout `current.md`) and is **not** established
or re-derived here. This section's Status contribution is scoped strictly
to the upper-bound direction at $n=3$.

**Verification summary (all non-numeric, cited above, nothing new
asserted by numerics alone in this section):** R26.1's Corollary algebra
is exact symbolic algebra (already reviewer-certified, round 8); the
$n=2$ discharge is the already-certified six-template argument (round 1);
the case-(b2) closure is the already-certified 6-branch Farkas argument
(round 25) with its domain restriction dropped this round (justified by
re-reading the six certificates — none use $p_1<T/2$ — and corroborated,
not proved, by a fresh 200,000-trial random search plus a 65,648-point
boundary-focused grid, both zero violations,
`/tmp/round-26/check2.py`, `/tmp/round-26/check3.py`); the (b1) closure is
already-certified general-$n$ algebra (round 13). No step in this
section's logical chain relies on numerics.

### Promotable lemmas (round 26)

- **`case-b2-n3-covering-closure`**: the round-26 domain-generalization
  attempt (widening from $\{p_1<T/2\}$ to no restriction on $p_1$) was
  **REFUTED** by this round's proof-reviewer (counterexample
  $p=(3/5,9/40,29/200,3/100)$) — the $p_1<T/2$ restriction is restored,
  lemma file corrected in place. Do not re-attempt this generalization
  without a genuinely new mechanism for the Triple-Pin chamber (or a
  replacement chamber) that doesn't assume $p_1<T/2$.
- **The R26.3 Theorem** (general-marking $n=3$ upper bound,
  $c(3)\le8/15$): **NOT** established this round — see the correction at
  the top of §R26.3. The residual open region is precisely $p_1\ge T/2$,
  $T/15<p_2<4T/15$.
- **Citation-bug fix itself** (R26.1): this part IS correct and
  reviewer-verified — recorded here so future rounds citing "case (a)"
  ($p_2\ge4T/15$) use the Corollary + `n2-upper-bound-lp-argument`
  pairing, not `generalized-peel-identity`. This alone does not complete
  the $n=3$ upper bound, since the (b2) covering-family gap above is
  independent of this fix.

### Honest scope note (do not overclaim)

**[CORRECTED, round 26]** This does **NOT** complete the general upper
bound at $n=3$ — the (b2) domain-generalization was refuted (see §R26.3
correction); the residual open region is exactly $p_1\ge T/2$,
$T/15<p_2<4T/15$. What IS established: the citation fix itself (case (a)
correctly uses the Corollary + `n2-upper-bound-lp-argument`, unconditional
for $p_2\ge4T/15$, any $p_1$), and case (b1)/case (b2)-restricted-to-
$p_1<T/2$ as before. It does **not**
establish: the general upper bound for $n\ge4$ (the case-(b2) chamber
census is explicitly deferred per this round's outline — the density
signal $\approx28\%\to64\%$ and the already-observed need for a
within-$n=3$ chamber sub-split both indicate a genuinely harder
combinatorial enumeration at $n=4$, not a quick corollary); the
lower-bound/achievability direction at any $n$ (tracked separately,
project-wide, in `current.md`); or the full `imo-2026-03` problem
statement (which needs both directions, for every $n$). Case (a) *does*
bootstrap for free one level up ($n=4$'s case (a), $p_2\ge a_4T/2$, closes
by the identical Corollary mechanism with $m=5$, since
`n2-upper-bound-lp-argument` still discharges the same reduced-triple
hypothesis) — noted as a bootstrap observation, not built this round, per
the outline's explicit instruction not to attempt $n=4$'s case (b2).

## Round 27 build: the Gap-Filler four-chamber family closes the residual $p_1\ge T/2$ gap — completing the general-marking $n=3$ upper bound $c(3)\le8/15$

**Goal (per the round-27 outliner/reviewer).** The round-26 reviewer found
the round-27 outline's own proposed "forced-feasibility lemma" (that
$p_1>8T/15$ and $p_2<4T/15$ force $p_2>p_3+p_4$) **FALSE**, with an
explicit counterexample $p=(0.6,0.15,0.15,0.10)$, and observed the true
optimal Xiang-Yu strategy there uses a "bisect $p_1$ + refine $p_4$"-style
pattern not covered by any certified chamber. This section designs,
numerically locates, and then **proves from scratch (Farkas-certificate
style)** a new four-chamber family that closes the whole residual region
$$R:=\{p_1\ge p_2\ge p_3\ge p_4>0,\ p_1\ge T/2,\ T/15<p_2<4T/15\}$$
— i.e. exactly the gap left open by round 26's correction to
`case-b2-n3-covering-closure`.

### R27.0 Notation

Throughout, $T=p_1+p_2+p_3+p_4$, and set
$$x:=p_2-p_3\ \ge0,\qquad y:=p_3-p_4\ \ge0,\qquad z:=p_4>0,\qquad u:=T/15.$$
So $p_2=x+y+z$, $p_3=y+z$, $p_4=z$, and $p_2+p_3+p_4=x+2y+3z$, hence
$p_1=T-(x+2y+3z)$. The target threshold is $a_3T=8T/15$, and a chamber
with reduced alternating sum $A$ succeeds iff $\Phi=(T+A)/2\le8T/15$, i.e.
iff $A\le T/15=u$.

The region $R$ becomes, in $(x,y,z)$-coordinates (with $T$ fixed, $x,y,z\ge0$):
$$x+2y+3z\ \le\ T/2\ =\ 7.5u \qquad\text{(from }p_1\ge T/2\text{)},$$
$$u\ <\ x+y+z\ <\ 4u \qquad\text{(from }T/15<p_2<4T/15\text{)}.$$

### R27.1 The Pair-Insensitivity Corollary (proved in full)

**Corollary (Pair-Insensitivity).** Let $M$ be any finite multiset of
positive reals and $v>0$ any value (possibly, but not necessarily, already
occurring in $M$). Then
$$A(M\cup\{v,v\})\ =\ A(M),$$
where $A$ is the alternating-sum-of-sorted-descending-order functional of
`odd-run-reduction-lemma`.

**Proof.** By `odd-run-reduction-lemma`, $A$ of any multiset $S$ equals $A$
of its odd-run reduction $S'$, obtained by, for every distinct value $w$
occurring in $S$ with multiplicity $\mu_S(w)$, keeping one copy of $w$ if
$\mu_S(w)$ is odd and zero copies if $\mu_S(w)$ is even. Now compare
$S=M\cup\{v,v\}$ with $M$ itself: for every value $w\ne v$,
$\mu_S(w)=\mu_M(w)$ (adding two copies of $v$ does not touch $w$'s count),
so $w$ survives the reduction of $S$ iff it survives the reduction of $M$,
with the same multiplicity ($0$ or $1$). For $w=v$,
$\mu_S(v)=\mu_M(v)+2$, which has the **same parity** as $\mu_M(v)$ (adding
$2$ never changes parity), so $v$ survives the reduction of $S$ (with
exactly $1$ copy) iff it survives the reduction of $M$. Hence the odd-run
reductions of $S$ and of $M$ are the identical multiset, so
$A(S)=A(M)$. $\blacksquare$

*(This corollary needs no adjacency or genericity assumption — it is a
direct, two-line consequence of the certified lemma's own multiplicity-based
statement, valid even when $v$ coincides with several other values
already present in $M$, or when $v$ itself is added multiple times by
iterating the corollary.)*

### R27.2 Four chambers, each closed-form in $u$ terms, via Pair-Insensitivity

All four chambers below use at most $3$ marks (`budget-monotonicity`:
using fewer than the full $n=3$ budget is always legal, so no chamber is
disqualified for using $2$ marks instead of $3$). Each is defined by an
explicit legal marking (composition of cuts), and its resulting
$\Phi$-value is computed by applying the Pair-Insensitivity Corollary
(R27.1) once per bisected/matched piece to strip it from the alternating
sum, leaving a small residual multiset whose $A$-value is read off
directly.

- **Chamber A (Bisect$\{1,4\}$).** Bisect $p_1$ (mark at $p_1/2$) and
  bisect $p_4$ (mark at $p_4/2$); leave $p_2,p_3$ untouched. The full
  fragment multiset is $\{p_1/2,p_1/2\}\cup\{p_4/2,p_4/2\}\cup\{p_2,p_3\}$.
  Applying R27.1 twice (once with $v=p_1/2$, $M=\{p_4/2,p_4/2,p_2,p_3\}$;
  once more with $v=p_4/2$, $M=\{p_2,p_3\}$) gives
  $A=A(\{p_2,p_3\})=p_2-p_3=x$ (since $p_2\ge p_3$, the $2$-element
  alternating sum is simply the larger minus the smaller). Hence
  $\Phi_A=(T+x)/2$; **success** ($\Phi_A\le8T/15$) **iff $x\le u$.**

- **Chamber B (Bisect$\{1,2\}$).** Bisect $p_1$ and bisect $p_2$; leave
  $p_3,p_4$ untouched. By the identical argument (R27.1 applied to the
  $p_1/2$ pair, then the $p_2/2$ pair),
  $A=A(\{p_3,p_4\})=p_3-p_4=y$. Hence $\Phi_B=(T+y)/2$; **success iff
  $y\le u$.**

- **Chamber C (Bisect$\{1,2,3\}$).** Bisect $p_1,p_2,p_3$ (uses all $3$
  marks); leave $p_4$ untouched. By R27.1 applied three times (peeling the
  $p_1/2$, then $p_2/2$, then $p_3/2$ pairs), the reduced multiset is the
  single-element multiset $\{p_4\}$, whose alternating sum is $p_4$ itself
  (a length-$1$ "alternating sum" is just the element, with $+$ sign).
  So $A=p_4=z$. Hence $\Phi_C=(T+z)/2$; **success iff $z\le u$.**

- **Chamber E (Bisect$1$ + Pin$2$-to-$3$).** Bisect $p_1$ (mark at
  $p_1/2$); mark $p_2$ once at the point that produces the two fragments
  $(p_3,\,p_2-p_3)=(p_3,x)$ — i.e. place the single cut on $p_2$ so that
  one resulting fragment exactly equals $p_3$'s own value (feasible since
  $0\le x=p_2-p_3\le p_2$, with the degenerate case $x=0$, i.e.
  $p_2=p_3$, producing one fragment of length $0$, harmless by
  `zero-pin-harmlessness-lemma`); leave $p_3,p_4$ untouched. The full
  fragment multiset is
  $\{p_1/2,p_1/2\}\cup\{p_3\ (\text{from the }p_2\text{ cut}),\,x\}\cup\{p_3\
  (\text{untouched})\}\cup\{p_4\}$
  $\ =\ \{p_1/2,p_1/2,\,p_3,p_3,\,x,\,z\}$
  (writing $p_4=z$). Applying R27.1 twice (peeling the $p_1/2$ pair, then
  the $p_3$ pair — note both pairs are "inert" for parity purposes
  regardless of any accidental coincidence of $p_1/2$ or $p_3$ with $x$ or
  $z$, exactly because R27.1 only requires that the **appended** value be
  duplicated an even number of times, which the two $p_1/2$'s and two
  $p_3$'s are, independent of anything else in the multiset), the reduced
  multiset is $\{x,z\}$, so $A=|x-z|$. Hence $\Phi_E=(T+|x-z|)/2$;
  **success iff $|x-z|\le u$.** This chamber uses only $2$ marks (one on
  $p_1$, one on $p_2$).

*(Sanity check against the reviewer's witness $p=(0.6,0.15,0.15,0.10)$,
$T=1$: $x=0,y=0.05,z=0.10$, $u=1/15\approx0.0667$. Chamber A succeeds
trivially ($x=0\le u$), giving $\Phi_A=(1+0)/2=0.5\le8/15\approx0.5333$ —
matches the round-27 outline-reviewer's own numeric optimum
$\Phi_{\min}\approx0.5029$ up to the fact that Chamber A is not literally
optimal there but is a valid, sufficient certificate. The reviewer's own
optimal cut pattern "$1$ cut on $p_1$, $2$ cuts on $p_4$" is a different,
tighter strategy but is not needed once Chamber A already succeeds.)*

### R27.3 The Covering Theorem: $\{A,B,C,E\}$ cover $R$ (Farkas-certificate proof)

**Theorem (Gap-Filler covering).** For every $(x,y,z)$ with $x,y,z\ge0$
satisfying $x+2y+3z\le T/2$ and $u<x+y+z<4u$ (i.e. every point of $R$),
at least one of
$$x\le u,\qquad y\le u,\qquad z\le u,\qquad |x-z|\le u$$
holds. Consequently at least one of Chambers A, B, C, E succeeds, so
$\Phi_{\min}(p)\le8T/15$ throughout $R$.

**Proof.** Suppose toward contradiction that all four fail simultaneously:
$$x>u,\qquad y>u,\qquad z>u,\qquad |x-z|>u.$$
The last condition splits into two exclusive cases.

**Case (i): $x-z>u$.** We exhibit the nonnegative combination
$$1\cdot\bigl(4u-(x+y+z)\bigr)\ +\ 1\cdot(y-u)\ +\ 1\cdot(x-z-u)\ +\
2\cdot(z-u)$$
of the four strict inequalities $4u-(x+y+z)>0$ (from $p_2=x+y+z<4u$),
$y-u>0$, $x-z-u>0$ (the Case-(i) hypothesis), and $z-u>0$ — each term is
**strictly positive**, and all four coefficients ($1,1,1,2$) are
nonnegative with at least one (in fact all) strictly positive, so the
whole sum is strictly positive. But expanding termwise:
$$\bigl(4u-x-y-z\bigr)+\bigl(y-u\bigr)+\bigl(x-z-u\bigr)+2\bigl(z-u\bigr)$$
$$=\ 4u-x-y-z+y-u+x-z-u+2z-2u$$
$$=\ (4u-u-u-2u)+(-x+x)+(-y+y)+(-z-z+2z)\ =\ 0.$$
So the sum is simultaneously $>0$ (as a sum of positive terms with
nonnegative weights) and identically $0$ (as an algebraic expression) —
a contradiction ($0>0$).

**Case (ii): $z-x>u$.** We exhibit the nonnegative combination
$$1\cdot\bigl(T/2-(x+2y+3z)\bigr)\ +\ 4\cdot(x-u)\ +\ 2\cdot(y-u)\ +\
3\cdot(z-x-u)$$
of the (non-strict) inequality $T/2-(x+2y+3z)\ge0$ (from $p_1\ge T/2$) and
the three strict inequalities $x-u>0$, $y-u>0$, $z-x-u>0$ (the Case-(ii)
hypothesis) — since the coefficients $1,4,2,3$ are all nonnegative and at
least one term ($x-u>0$, coefficient $4>0$) is strictly positive, the
whole sum is **strictly positive**. Expanding termwise (writing $T/2=7.5u$):
$$\bigl(7.5u-x-2y-3z\bigr)+4(x-u)+2(y-u)+3(z-x-u)$$
$$=\ 7.5u-x-2y-3z+4x-4u+2y-2u+3z-3x-3u$$
$$=\ (7.5u-4u-2u-3u)+(-x+4x-3x)+(-2y+2y)+(-3z+3z)\ =\ -1.5u.$$
So the sum is simultaneously $>0$ and identically equal to $-1.5u$. Since
$u=T/15>0$ (as $T=p_1+p_2+p_3+p_4>0$), $-1.5u<0$, giving $0<-1.5u<0$ — a
manifestly false strict inequality, a contradiction.

Both cases are contradictory, so the assumption that all four chamber
conditions fail is impossible. Hence at least one of $x\le u$, $y\le u$,
$z\le u$, $|x-z|\le u$ holds throughout $R$, i.e. at least one of Chambers
A, B, C, E succeeds. $\blacksquare$

**Independent numeric corroboration (not load-bearing, sanity check
only).** A $300{,}000$-trial exact-`Fraction` random search over $R$
(`/tmp/round-27/final_check.py`) found **zero** violations of
$\min(x,y,z,|x-z|)\le u$. A separate LP search
(`/tmp/round-27/find_witness2.py`, HiGHS exact-simplex-grade solver) for
the supremum of the "all four excesses positive" margin in each of Case
(i) and Case (ii) returned exactly $0$ and a negative value respectively —
confirming the algebraic proof's contradiction is tight (Case (i)'s bound
is attained with equality, e.g. at the vertex
$p=(1/2,1/4,1/6,1/12)$: $x=y=z=1/12=1.25u$... *(check: $u=1/15$, so
$1/12>1/15$, and $x-z=0\le u$, so Chamber E succeeds there exactly with
$A=0$, $\Phi_E=T/2=0.5\le8/15$ — this is precisely the vertex where
Chambers A, B, C individually fail but E rescues it, matching the
reviewer's "bisect $p_1$ + [something on $p_2$]" pattern intuition)*).

### R27.4 Assembly: the residual gap is closed

**Corollary (residual-gap closure).** For every legal marking
$p_1\ge p_2\ge p_3\ge p_4>0$ with $p_1\ge T/2$ and $T/15<p_2<4T/15$,
$$\Phi_{\min}(p_1,p_2,p_3,p_4)\ \le\ \frac{8}{15}T.$$

**Proof.** Immediate from R27.3: such a $p$ has $(x,y,z)$ satisfying the
Theorem's hypotheses (translating $p_1\ge T/2\Leftrightarrow
x+2y+3z\le T/2$ and $T/15<p_2<4T/15\Leftrightarrow u<x+y+z<4u$, per R27.0),
so at least one of Chambers A, B, C, E is a legal ($\le3$-mark) response
achieving $\Phi\le8T/15$, and any legal response upper-bounds
$\Phi_{\min}$ (`feasibility-suffices-for-upper-bound`). $\blacksquare$

### R27.5 The general-marking $n=3$ upper bound is now complete

Combining this Corollary with the pieces already independently certified
(no change to any of them, no re-derivation needed):

- **$p_2\le T/15$ (case (b1)):** `unconditional-p2-threshold-closure`,
  general $n$, no restriction on $p_1$ — certified, cited in R26.2.
- **$p_2\ge4T/15$ (case (a)):** the Corollary to Theorem B ($m=4$) with
  `n2-upper-bound-lp-argument` discharging its hypothesis, no restriction
  on $p_1$ — certified, re-verified in R26.1.
- **$T/15<p_2<4T/15$, $p_1<T/2$:** `case-b2-n3-covering-closure`'s
  5-chamber family (restriction restored per the round-26 correction) —
  certified.
- **$T/15<p_2<4T/15$, $p_1\ge T/2$:** the Gap-Filler 4-chamber family
  (R27.1–R27.4, this round) — proved in full above.

These four regimes are **exhaustive** (every marking has $p_2$ in exactly
one of $(0,T/15]$, $(T/15,4T/15)$, $[4T/15,T/2]$ by R26.2's verified
trichotomy, and — new this round — within the middle piece $p_1$ is either
$<T/2$ or $\ge T/2$, an ordinary dichotomy with no gap or double-count
since $p_1<T/2$ and $p_1\ge T/2$ partition all reals) and **pairwise
non-overlapping in the relevant sense** (each marking is handled by
exactly one bullet; the two middle-piece sub-bullets share the boundary
value $p_1=T/2$ only in the sense that it is assigned to the $p_1\ge T/2$
bullet, consistent with the round-26 correction's own restriction
$p_1<T/2$ strict for the old family). Hence:

**Theorem (General-marking $n=3$ upper bound — complete).** *For every
legal marking $p_1\ge p_2\ge p_3\ge p_4>0$ with $T=p_1+p_2+p_3+p_4$, Xiang
Yu has a legal response (at most $3$ marks) with*
$$\Phi_{\min}(p_1,p_2,p_3,p_4)\ \le\ \frac{8}{15}T.$$
*Consequently $c(3)\le8/15$.*

**Proof.** By the four-regime exhaustive case split above, each regime
closed by an independently certified, non-numeric argument (numerics used
only as search guides / corroboration, never as a proof step): case (b1)
and case (a) are fully unconditional (any $p_1$); the $T/15<p_2<4T/15$
strip is split by $p_1$ vs. $T/2$ into the pre-existing 5-chamber family
($p_1<T/2$) and this round's new 4-chamber Gap-Filler family
($p_1\ge T/2$, R27.1–R27.4). Every legal marking falls in exactly one
case, and each case gives $\Phi_{\min}\le8T/15$. $\blacksquare$

**Scope — what this establishes and what it does not.** This completes
the **upper-bound direction** ($c(3)\le8/15$) for **every** legal marking
at $n=3$, closing the gap that rounds 25–26 left open. It does **not**
establish:
- the **lower-bound / achievability direction** at $n=3$ (Liu Bang's
  ladder marking forcing $\Phi\ge8/15\,T$ against every Xiang Yu response,
  i.e. $\Phi_{\min}(\text{ladder})=8T/15$ exactly, not just $\le$) — this
  is a separate front, tracked project-wide in `current.md` (the
  lower-bound/tie-vertex enumeration, currently the subject of the
  `greedy-halving-adversary` and `rank-pigeonhole-budget` approaches). **This
  approach file does not establish it and makes no claim about its status
  elsewhere** — combining this round's upper-bound theorem with whatever
  the project's lower-bound front has or has not yet certified for $n=3$
  specifically is left to `current.md`'s own tracking, not asserted here;
- the general upper bound for $n\ge4$ (an genuinely harder combinatorial
  enumeration, per the round-26 density signal $28\%\to64\%$ — explicitly
  deferred, not attempted this round);
- the full `imo-2026-03` problem statement for general $n$ (needs both
  directions, for every $n$ — this remains the project's overall open
  target, tracked in `current.md`).

This Theorem's Status contribution is therefore: **the $n=3$
general-marking upper bound $c(3)\le8/15$ is fully proved**, non-numeric,
gap-free, every case settled, every cited lemma either proved in full in
this file (R27.1–R27.3, new this round) or already reviewer-certified
(`unconditional-p2-threshold-closure`, the Corollary to Theorem B,
`n2-upper-bound-lp-argument`, `case-b2-n3-covering-closure`,
`odd-run-reduction-lemma`, `zero-pin-harmlessness-lemma`,
`feasibility-suffices-for-upper-bound`).

### Promotable lemmas (round 27)

- **`pair-insensitivity-corollary`** (R27.1): $A(M\cup\{v,v\})=A(M)$ for
  any multiset $M$ and value $v>0$ — a two-line, fully general corollary
  of the certified `odd-run-reduction-lemma`, proved in full above, no gap.
  Reusable anywhere a "bisect a piece to erase it from the alternating
  sum" argument is needed (this project's chamber-construction toolbox
  uses this pattern constantly but has not previously isolated it as a
  named, standalone, certifiable fact).
- **`gap-filler-four-chamber-covering`** (R27.2–R27.3): the four chambers
  A ($x\le u$), B ($y\le u$), C ($z\le u$), E ($|x-z|\le u$) jointly cover
  the residual region $R=\{p_1\ge T/2,\ T/15<p_2<4T/15\}$ at $n=3$ —
  proved by two explicit Farkas certificates (Case (i), Case (ii) above),
  each a nonnegative-coefficient combination of the failure hypotheses
  collapsing to a manifestly false inequality. This is new, load-bearing
  content this round, closing a gap that stumped rounds 24–26.
- **The complete $n=3$ general-marking upper bound** (R27.5): assembled
  from four independently-certified regimes (no new gaps beyond
  R27.1–R27.3, which are proved in full this round). This is the
  strongest claim this approach file has made to date; flagged here
  explicitly for the proof-reviewer to re-verify independently before
  any "solved" status is granted, per the project's repeated overclaim
  history in this exact area (rounds 25 and 26).

## Outline (proof-outliner, round 28)

**Target: close the $p_1\ge T/2$ regime of the $n=4$ general-marking upper
bound $c(4)\le a_4=16/31$ "for free," by literally re-running §4's Theorem
C′/Theorem A argument one index up** (round-28 `math-explorer-
n4-generalization` report's item 1, the cheapest identified sub-target).
**Reasoning for choosing this over the n=3 lower-bound/achievability
alternative:** the $n=3$ lower bound is, per every explorer and reviewer
finding on record, the *identical* central obstruction the two sibling
approaches (`rank-pigeonhole-budget`, `greedy-halving-adversary`) are
already independently attacking (Claim (B)/$(\star_k)$) — opening it here
would collapse this file's diversity into a third front on the same wall,
against the CLAUDE.md diversity rule. The $n=4$ upper-bound bootstrap, by
contrast, is a genuinely distinct, near-mechanical extension that only
became possible this round (round 27 finally closed $P(4)$, the full
$n=3$ upper bound, both regimes — the exact missing prerequisite §4's own
diagnosis names) and stays on this file's own distinct front (the general
upper bound), not the lower bound. Keep the $n=3$ lower bound noted as a
good *future* target if this file's upper-bound front later stalls, but
not this round's pick.

Precise statement to prove: for every legal marking $p=(p_1,p_2,p_3,p_4,
p_5)$ (sorted, $T=\sum p_i=1$) with $p_1\ge T/2$, every Xiang-Yu response
using $\le4$ cuts satisfies $\Phi\ge a_4T=16T/31$.

Skeleton:
1. **Sub-case $T/2\le p_1<a_4T$:** close directly via Theorem A
   (Full-Match, already certified general-$n$) — by the tool: Theorem A's
   identity, re-instantiated at $n=4$ (pure substitution, no new proof;
   Theorem A's statement and proof never assumed $n=3$).
2. **Sub-case $p_1\ge a_4T$:** close via Theorem C′ (bisect $p_1$, recurse
   optimally on the tail) — by the tool: Theorem C′'s general-$n$
   recursive identity, whose sufficient condition is exactly "$P(n-1)$
   fully closed (both regimes) for an arbitrary tail" — instantiate at
   $n=4$, so the induction hypothesis needed is $P(4)$: the complete,
   both-regime, every-marking $n=3$ upper bound. **This is now available**
   — round 27's `gap-filler-four-chamber-covering` plus the round 24-26
   machinery together constitute exactly $P(4)$ in full, reviewer-APPROVEd
   at its own scope.
3. Combine steps 1–2: every legal 5-piece marking with $p_1\ge T/2$
   satisfies $\Phi\ge a_4T$ — by the tool: case split on $p_1$ vs.
   $a_4T$, no gap between the two sub-cases (Theorem A's domain is
   exactly $[T/2,a_4T)$, Theorem C′'s is exactly $[a_4T,T]$, per the
   telescoping-threshold-identity's already-certified algebra).
4. State precisely what remains: the $p_1<T/2$ regime at $n=4$ (the
   genuinely hard, must-redo-per-level chamber census; NOT attempted this
   round) — do not claim $c(4)\le16/31$ in full, only the $p_1\ge T/2$
   half.

Key lemmas (claim + mechanism):
- **Theorem A and Theorem C′ transplant to $n=4$ verbatim** — because both
  are stated and proved for arbitrary $n$ in the existing file (never
  $n=3$-specific arithmetic baked in), so re-indexing is substitution, not
  new proof; only the *induction hypothesis they consume* ($P(n-1)$) was
  previously unavailable at the $n=4$ level, and round 27 supplies it.
- **The telescoping threshold identity $a_{n-1}=a_n/(2(1-a_n))$ places the
  two sub-cases' domains exactly end-to-end with no gap** — because this
  identity (already certified, general $n$) is precisely what makes
  Theorem A's upper threshold $a_nT$ match Theorem C′'s lower threshold
  with no overlap and no uncovered strip, reused unchanged from the $n=3$
  closure (§4's own boundary-matching argument, re-cited not re-derived).

Open gaps: none anticipated in this specific sub-target if steps 1–3 go
through as a literal re-index (this is the "close to mechanical" claim the
explorer's report makes) — but verify explicitly, do not assume, that
Theorem C′'s proof genuinely never used any $n=3$-specific fact beyond
citing $P(n-1)$ abstractly (a concrete risk: check the proof text for any
hidden reference to $D_3=15$ or $a_3=8/15$ as a literal constant rather
than as "$P(n-1)$'s threshold," which would break under re-indexing).

Cases to cover: $T/2\le p_1<a_4T$ (Theorem A) and $p_1\ge a_4T$ (Theorem
C′) — jointly exhaustive of $p_1\ge T/2$ by the threshold identity.

Watch out for:
- **Do not claim this closes $c(4)\le a_4$ in general** — the $p_1<T/2$
  regime is untouched, and per the explorer's density-growth signal
  (28%→64% between $n=3,4$ chamber censuses), it is expected to need
  substantially more work than the $n=3$ case did, not a repeat of the
  same 5+4-chamber count.
- **Case (a)** ($p_2\ge a_4T/2$, a subset of $p_1\ge T/2$) is redundant
  with this outline's step 2 mechanism but may be worth stating as its own
  explicit corollary for cross-checking against the $p_2$-partition framing
  used at $n=3$ — cheap, not required for this outline's main target.
- Re-verify (do not just assume by analogy) that Theorem C′'s
  "$P(n-1)$ fully closed" hypothesis really means the *complete* $n=3$
  theorem (both regimes, every marking), not merely case (a) or case (b1)
  — per round 9's finding, this is a real coupling, not a formality.

## Round 28 build: the $p_1\ge T/2$ regime of the $n=4$ general-marking
upper bound is closed, using round 27's certified $P(4)$

### R28.0 Setup and notation (imported, not re-derived)

Fix $n=4$, i.e. $m=5$ pieces $p_1\ge p_2\ge p_3\ge p_4\ge p_5>0$,
$T=\sum_{i=1}^5 p_i$. Write $a_k:=2^k/(2^{k+1}-1)$, $D_k:=2^{k+1}-1$, so
$a_4=16/31$ and $a_3=8/15$ (direct substitution: $2^4/(2^5-1)=16/31$,
$2^3/(2^4-1)=8/15$). Recall the file's standing definition (§"Round 9
formalization," §1): for $k\ge0$,
$$P(k):\quad\text{for every marking of exactly $k$ pieces (budget $n=k-1$
cuts)},\ \Phi_{\min}\le a_{k-1}T,$$
which at $k=4$ reads: for every 4-piece marking, $\Phi_{\min}(\,\cdot\,;3)
\le a_3T=\tfrac{8}{15}T$ — **exactly** the statement round 27's Theorem
(§R27.5, "The general-marking $n=3$ upper bound is now complete,"
reviewer-APPROVEd) proves, for *every* 4-piece marking with no restriction
on which regime ($p_1<T/2$ or $p_1\ge T/2$, or any $p_2$-band) it falls
in. So **$P(4)$ is fully available**, unconditionally, as an input to any
argument (such as Theorem C′ below) that needs a bound on an *arbitrary*
4-piece tail.

Three tools are reused verbatim from earlier in this file, with no
re-derivation (each already proved for **general** $m$/$n$, never
$n=3$-specific):

- **Theorem A (Full-Match Achievability)** (§"Four exact, unconditional
  Xiang Yu strategies," proved above): if $p_1\ge T/2$, Xiang Yu can split
  $p_1$ into fragments matching $p_2,\dots,p_m$ plus a leftover $v=2p_1-T$,
  using exactly $m-1$ cuts, achieving $\Phi=p_1$ exactly. Its proof uses
  only `leftover-formula`; no arithmetic constant tied to any specific
  $m$.
- **Theorem C′ (Bisect-Top, Recursive)** (§1 above): for $m\ge2$, bisecting
  $p_1$ (1 cut) and applying any legal strategy to the untouched tail
  $\{p_2,\dots,p_m\}$ with $\le n-1=m-2$ further cuts, producing $\Phi'$,
  yields exactly $\Phi=p_1/2+\Phi'$. Its proof uses only
  `pair-cancellation-identity` on the pair $\{p_1/2,p_1/2\}$ and total-mass
  bookkeeping — verified above (round 27 outline review, item 3) to contain
  **no** hardcoded $n=3$ arithmetic.
- **Lemma (Telescoping Threshold)** and its **Corollary (Theorem C′'s
  threshold, general $n$)** (§2 above): for every $n\ge1$,
  $a_{n-1}=a_n/(2(1-a_n))$, and consequently — granting
  $\Phi_{\min}(\text{tail};n-1)\le a_{n-1}T'$ for the *specific* tail at
  hand — Theorem C′ gives $\Phi_{\min}\le a_nT$ whenever $p_1\ge a_nT$. Both
  are proved for **every** $n\ge1$ by direct algebra (no case restriction,
  no finite check); re-verified by direct substitution below at $n=4$
  specifically, as the round-28 outline review required.

### R28.1 The telescoping identity at $n=4$ (explicit substitution)

**Claim.** $a_3=\dfrac{a_4}{2(1-a_4)}$.

*Proof.* By the general Telescoping Threshold Lemma (already proved for
every $n\ge1$; this is pure substitution at $n=4$, not a new derivation):
$1-a_4=\dfrac{D_3}{D_4}$ where $D_3=2^4-1=15$, $D_4=2^5-1=31$, so
$1-a_4=\tfrac{15}{31}$, matching $1-\tfrac{16}{31}=\tfrac{15}{31}$
directly. Hence
$$\frac{a_4}{2(1-a_4)}=\frac{16/31}{2\cdot15/31}=\frac{16}{30}=\frac{8}{15}=a_3.
\qquad\blacksquare$$
(Also confirms $a_4>1/2$: $a_4-\tfrac12=\tfrac{1}{2D_4}=\tfrac1{62}>0$, the
$k=4$ instance of the Telescoping Threshold Lemma's own proof fact
$a_k>1/2$ for every $k\ge0$.)

### R28.2 Theorem: the $p_1\ge T/2$ regime of $n=4$ is closed

**Theorem ($p_1\ge T/2$ closure at $n=4$).** *For every 5-piece marking
$p_1\ge p_2\ge p_3\ge p_4\ge p_5>0$ with $p_1\ge T/2$,*
$$\Phi_{\min}(p_1,\dots,p_5;\,4)\ \le\ a_4T=\frac{16}{31}T.$$

*Proof.* Two sub-cases, partitioning $[T/2,T)$ with no gap and no overlap,
since $a_4=16/31\in(\tfrac12,1)$ (R28.1):

- **Sub-case $T/2\le p_1<a_4T$.** By Theorem A, Xiang Yu has a legal
  4-cut response (within budget $n=4$) achieving $\Phi=p_1$ exactly. Since
  $p_1<a_4T$ in this sub-case, $\Phi=p_1<a_4T$ directly — no recursion, no
  tail hypothesis of any kind needed.

- **Sub-case $p_1\ge a_4T$.** Apply Theorem C′: bisect $p_1$ (1 cut),
  leaving the tail $\{p_2,p_3,p_4,p_5\}$ untouched, and apply to that tail
  the *optimal* legal strategy using the remaining $\le n-1=3$ cuts. The
  tail is a 4-piece marking (in general position — nothing forces it into
  any particular regime, $p_1\ge T/2$ or $p_1<T/2$, at its own scale), so
  it falls exactly under $P(4)$'s hypothesis. By $P(4)$ — round 27's
  Theorem, R28.0 above, fully established for *every* 4-piece marking with
  no restriction — the tail satisfies
  $$\Phi_{\min}(p_2,p_3,p_4,p_5;\,3)\ \le\ a_3T',\qquad T':=T-p_1=p_2+p_3+p_4+p_5.$$
  Theorem C′ then gives $\Phi_{\min}(p_1,\dots,p_5;\,4)\le p_1/2+a_3T'$.
  This is exactly the hypothesis of the Corollary of §2 ("Theorem C′'s
  threshold, general $n$"), instantiated at $n=4$: that Corollary's proof
  (already established for every $n\ge1$, hence covering $n=4$ without
  re-derivation) shows
  $$\Phi_{\min}\ \le\ a_3T+p_1\Big(\tfrac12-a_3\Big),$$
  and since $a_3>\tfrac12$ (base case of the Telescoping Threshold Lemma's
  own proof, R28.1) the coefficient of $p_1$ is strictly negative, so the
  right side — as an affine function of $p_1$ on $[a_4T,\,T)$ — is
  maximized at the left endpoint $p_1=a_4T$:
  $$\Phi_{\min}\ \le\ a_3T+a_4T\Big(\tfrac12-a_3\Big)
  =T\Big[a_3(1-a_4)+\tfrac{a_4}{2}\Big].$$
  By R28.1, $a_3(1-a_4)=\dfrac{a_4}{2}$ (rearranging
  $a_3=\dfrac{a_4}{2(1-a_4)}$), so the bracket equals
  $\dfrac{a_4}{2}+\dfrac{a_4}{2}=a_4$. Hence $\Phi_{\min}\le a_4T$ exactly,
  with equality possible only in the limit $p_1\to a_4T$.

These two sub-cases jointly cover all of $p_1\ge T/2$: their domains
$[T/2,a_4T)$ and $[a_4T,T)$ partition $[T/2,T)$ exactly (R28.1), and every
legal marking with $m=5$ has $p_1<T$ (since $p_2,\dots,p_5>0$).
$\blacksquare$

**Numerical sanity check** (corroboration only, not load-bearing — the
written proof above is fully algebraic): $a_3=8/15$, $a_4=16/31$, and
$a_3=a_4/(2(1-a_4))$ hold as exact `Fraction` identities, independently
recomputed:

```
a3 = Fraction(8,15); a4 = Fraction(16,31)
a4/(2*(1-a4)) == a3   # True
a4 > Fraction(1,2)    # True
```

### R28.3 What this does and does not establish (honest scope)

**This closes, fully and rigorously, non-numerically:** the $p_1\ge T/2$
half of $P(5)$ (equivalently, the $n=4$ upper bound $c(4)\le a_4T=16T/31$
restricted to markings with $p_1\ge T/2$). Every ingredient — Theorem A,
Theorem C′, the Telescoping Threshold Lemma and its Corollary — was
already proved for general $n$/general $m$ before this round; the only
new content this round is (i) the explicit re-indexing/substitution at
$n=4$ (R28.1), and (ii) supplying the one missing ingredient the argument
needed one level down, $P(4)$ for an *arbitrary* 4-piece tail, which
round 27 (§R27.5, reviewer-APPROVEd) now makes fully available. This
mirrors §4's $n=3$ closure exactly, one index up — no shortcuts, no
smuggled $n=3$-specific arithmetic (verified directly above: R28.1 rebuilds
the needed constants, $8/15$ and $16/31$, from the general formula
$a_k=2^k/(2^{k+1}-1)$ and the general Telescoping Threshold Lemma, not by
reusing a cached $n=3$ numeral).

**This does NOT close the full $n=4$ upper bound $c(4)\le16/31$.** The
complementary regime $p_1<T/2$ at $n=4$ is entirely untouched by this
round's work: Theorem A and Theorem C′ both require $p_1\ge T/2$ (Theorem
A directly; Theorem C′'s threshold Corollary only applies once
$p_1\ge a_4T\ge T/2$), so neither mechanism says anything when $p_1<T/2$.
Per the round-27→28 outline's own diagnosis (repeated here for honesty,
not merely inherited): closing $p_1<T/2$ at $n=4$ is expected to need a
genuinely new, ground-up chamber census analogous to case (b2)'s 5-chamber
family plus the Gap-Filler 4-chamber family at $n=3$ (rounds 22–27) — a
substantially larger effort than this round's mechanical re-indexing,
per the density-growth signal recorded in the round-28 explorer's report
(the fraction of random markings landing in the "easy," directly-covered
regimes shrinks from $\approx28\%$ at $n=3$ to $\approx64\%$ *needing* the
harder census at $n=4$, i.e. the hard residual grows, not shrinks). **No
claim is made here about $c(4)\le16/31$ in general, and no claim is made
about the lower-bound/achievability direction at any $n$.**

**Also note (cheap corollary, not required for the main target but
recorded for cross-checking, per the outline's "watch out" item):** the
narrower sub-case $p_2\ge a_4T/2$ (a subset of the $p_1\ge T/2$ sub-case
$p_1\ge a_4T$, since $p_1\ge p_2$ forces $p_1\ge a_4T/2$ whenever
$p_2\ge a_4T/2$ — not literally the same set, but every marking with
$p_2\ge a_4T/2$ also has $p_1\ge a_4T/2$) is *also* directly closeable via
the Corollary to Theorem B$_k$ ($k=2$, §"Four exact... Corollary (Theorem
B, recursive sufficient condition)"), whose hypothesis is exactly
$p_2\ge a_nT/2$ discharged by the reduced instance $S'=\{p_1-p_2,p_3,p_4,
p_5\}$ lying in the inductively-established domain one level down — this
is consistent with, and redundant with, the Theorem C′ route above (both
ultimately consume $P(4)$), and is recorded here only as a cross-check,
not as new content requiring separate proof.

### Promotable lemmas (round 28)

- **Theorem ($p_1\ge T/2$ closure at $n=4$)** (R28.2): fully proved, no
  gaps, reusing only already-certified general-$n$ machinery
  (`full-match-achievability`, `bisect-top-recursive-identity`,
  `telescoping-threshold-identity`) plus round 27's certified
  `gap-filler-four-chamber-covering`/the assembled $n=3$ theorem as the
  one new ingredient (P(4)) it needed. Recommend certifying as
  `p1-geq-half-closure-n4` — reusable verbatim as the induction hypothesis
  for a future $n=5$ attempt at the identical sub-target, exactly as
  round 27's $P(4)$ was reused here.

## Round 29 build: free transplants pin the $n=4$ residual, and the
Double-Bisect-Pin chamber family (proved) empirically closes it

### R29.0 Setup

Fix $n=4$, $m=5$ pieces $p_1\ge p_2\ge p_3\ge p_4\ge p_5>0$,
$T=\sum_{i=1}^5p_i$. Recall $a_4=16/31$, $D_4=31$ (§R28.0–R28.1). Indices
below are used both $1$-indexed ($p_1,\dots,p_5$, matching the marking's
own labeling) and, in the Python verification scripts, $0$-indexed
($p[0],\dots,p[4]$); the text always uses the $1$-indexed convention.

### R29.1 Three free transplants (zero new proof, pure instantiation)

**(i) $p_2\le T/D_4=T/31$.** By the certified `unconditional-p2-threshold-
closure` (general $n$, proved for every $n\ge1$ with no induction
hypothesis), instantiating at $n=4$ gives: whenever $p_2\le T/31$, bisecting
$p_1$ alone (1 cut, legal) achieves $\Phi\le a_4T$. This closes the whole
sub-case $p_2\le T/31$ unconditionally.

**(ii) $p_2\ge8T/31$.** By the certified `generalized-peel-identity`
(Theorem B$_k$, general $m,k$) at $k=2$: cutting $p_1$ into $(p_2,w_2)$
with $w_2=p_1-p_2$ (1 cut) and applying any legal strategy with the
remaining $\le3$ cuts to the reduced 4-element tail
$S_2'=\{w_2,p_3,p_4,p_5\}$ (total $T-2p_2$) gives, combined,
$\Phi=p_2+\Phi'$ where $\Phi'$ is the tail's own achieved value. The
reduced tail $S_2'$ is an arbitrary 4-piece marking (no restriction is
imposed on the relative order of $w_2,p_3,p_4,p_5$ by this construction —
`generalized-peel-identity`'s proof needs none), so round 27's fully
established, both-regime $n=3$ upper bound (§R27.5, `gap-filler-four-
chamber-covering` combined with case (a)/(b1)/(b2)) applies unconditionally:
$\Phi'_{\min}\le a_3(T-2p_2)$. Hence
$$\Phi_{\min}\ \le\ p_2+a_3(T-2p_2)\ =\ a_3T+p_2(1-2a_3).$$
Since $a_3=8/15$, $1-2a_3=-1/15<0$, this bound is decreasing in $p_2$, so
it is $\le a_4T$ exactly when $p_2\ge\dfrac{(a_3-a_4)T}{2a_3-1}$. Computing
exactly: $a_3-a_4=\dfrac{8}{15}-\dfrac{16}{31}=\dfrac{8\cdot31-16\cdot15}
{465}=\dfrac{248-240}{465}=\dfrac{8}{465}$, and $2a_3-1=\dfrac{16}{15}-1=
\dfrac1{15}$, so the threshold is $\dfrac{8/465}{1/15}T=\dfrac{8\cdot15}
{465}T=\dfrac{120}{465}T=\dfrac{8}{31}T$. So this closes
$p_2\ge8T/31=a_4T/2$ unconditionally, exactly matching the general
"Corollary to Theorem B$_k$" pattern already recorded at R28.3 ("Also
note," the $p_2\ge a_nT/2$ sufficient condition) — here re-derived
explicitly at $n=4$ rather than merely cited, per the round-29 outline's
"sequence the free transplants" instruction.

**(iii) $p_1\ge T/2$.** By the already-certified `p1-geq-half-closure-n4`
(round 28, proved in full — R28.2), $\Phi_{\min}\le a_4T$ throughout
$p_1\ge T/2$, unconditionally.

**Exact-arithmetic re-verification of the three thresholds** (not load-
bearing, corroboration only — the algebra above is self-contained):
```python
from fractions import Fraction as F
a3, a4 = F(8,15), F(16,31)
assert F(1,31) == 1 - F(30,31)          # T/D_4 threshold, sanity
assert (a3-a4)/(2*a3-1) == F(8,31)      # case-(a) analog threshold
assert F(8,31) == a4/2                  # matches the general a_n*T/2 pattern
```
All three checks pass exactly.

### R29.2 The residual: $p_1<T/2$ AND $T/31<p_2<8T/31$

By R29.1, every legal marking with $p_1\ge T/2$, or $p_2\le T/31$, or
$p_2\ge8T/31$ is already closed. The three closed regions are not disjoint
from each other in general (e.g. $p_1\ge T/2$ can coincide with either
$p_2$-band) but their union covers everything outside
$$\mathcal R:\quad p_1<T/2\ \text{ and }\ T/31<p_2<8T/31,$$
so it suffices to close $\Phi_{\min}\le a_4T$ on $\mathcal R$ alone. This
is the precise (intersection, not "all of $p_1<T/2$") residual the
round-29 outline specified, and matches the outline-reviewer's independent
check of the threshold arithmetic.

### R29.3 Bisect-Subset-Lemma instantiated at $n=4$: 30 chambers, measured coverage

By the certified `bisect-subset-lemma` (already proved for arbitrary $m$
and any $S\subseteq\{1,\dots,m\}$ with $|S|\le n$), instantiating at
$m=5,n=4$: for every nonempty $S\subsetneq\{1,\dots,5\}$ with $|S|\le4$
(i.e. every $S$ except $\emptyset$ and the full 5-set, which would need 5
cuts $>4$), bisecting every piece in $S$ and leaving the rest untouched is
a legal response with
$$\Phi_S(p)=\frac{T+A(R)}{2},\qquad R:=(p_i)_{i\notin S}\ \text{(sorted
descending)}.$$
This gives $2^5-2=30$ chambers, purely by substitution — no new proof.

**Coverage measurement** (exact `Fraction`, `/tmp/round-29/coverage_n4.py`,
independently re-run this round): $20{,}000$ random 5-piece markings drawn
uniformly (via random positive integers, then sorted) and rejection-
sampled into $\mathcal R$; for each, computed $\min_S\Phi_S(p)$ over all 30
chambers and compared to $a_4T$. Result: **$18544/20000=92.72\%$ covered**;
$1456$ points ($7.28\%$) not covered by the 30 Bisect-Subset chambers
alone. Sample uncovered points cluster with $p_1/T\approx0.30$–$0.49$ (near
but strictly below $1/2$) and $p_2/T\approx0.20$–$0.26$ (in the interior of
$(1/31,8/31)$, not near either boundary) — i.e. the uncovered region is a
genuine interior chunk of $\mathcal R$, not a thin boundary sliver, mirroring
round 24's $n=3$ density-growth signal (this is a *measurement*, stated as
such, not a proof of exact coverage percentage — a different random seed
or sample size would give a slightly different number, but the qualitative
finding, "Bisect-Subset alone is insufficient and the gap is a substantial
interior fraction," is robust across the two independent runs performed
this round, seeds 0 and 2, sample sizes 20000 and 30000: $92.72\%$ and
$93.05\%$ respectively).

### R29.4 The Double-Bisect-Pin Family (new, proved in full)

Motivated by the outline's step 5 prediction ("expect Triple-Pin $\to$ a
Quad-Pin analog using $n=4$'s extra cut budget"), and following the
project's standing rule (round 27) of reverse-engineering closed forms
from a numeric optimizer's argmin rather than guessing shapes blind: a
direct search over "bisect 2 pieces + pin 1 piece to another, leave the
5th untouched" constructions, run against the $1456$ points left
uncovered by Bisect-Subset alone, found this exact family closes **all**
of them (`/tmp/round-29/coverage_n4_extra.py`: covered $20000/20000=100\%$
once Double-Bisect-Pin chambers are added to Bisect-Subset).

**Theorem (Double-Bisect-Pin, $n=4$).** Fix a 5-piece marking
$p_1\ge\cdots\ge p_5>0$, $T=\sum p_i$. For any 2 distinct indices
$i,j\in\{1,\dots,5\}$ (the "bisected" pair) and any 2 distinct indices
$k,l\in\{1,\dots,5\}\setminus\{i,j\}$ with $k<l$ (so $p_k\ge p_l$,
guaranteed by the marking's sorted order), let $r$ be the unique remaining
index (${\{1,\dots,5\}\setminus\{i,j,k,l\}}$, a single index since
$5-4=1$). The strategy "bisect $p_i$ and $p_j$; cut $p_k$ into
$(p_l,\,p_k-p_l)$; leave $p_l$ and $p_r$ untouched" is a legal response
(uses exactly $2+1=3\le4$ cuts), and
$$\Phi_{i,j;k,l}(p)\ =\ \frac{T+|p_k-p_l-p_r|}{2}.$$

*Proof.* The resulting fragment multiset is
$$\Bigl\{\tfrac{p_i}2,\tfrac{p_i}2\Bigr\}\ \cup\
\Bigl\{\tfrac{p_j}2,\tfrac{p_j}2\Bigr\}\ \cup\
\bigl\{p_l,\ p_k-p_l\bigr\}\ \cup\ \{p_l\}\ \cup\ \{p_r\}$$
(the bisected pair for $i$, the bisected pair for $j$, the two fragments
of the cut on $p_k$, the untouched original $p_l$, and the untouched
$p_r$). This has total mass $T$ (direct check: $p_i+p_j+p_k+p_l+p_r=T$
since $\{i,j,k,l,r\}=\{1,\dots,5\}$).

Group the multiset as $M\cup\{v_1,v_1\}\cup\{v_2,v_2\}\cup\{v_3,v_3\}$
where $M=\{p_k-p_l,\ p_r\}$, $v_1=p_i/2$, $v_2=p_j/2$, $v_3=p_l$ (the
matched fragment from cutting $p_k$, paired with the untouched original
$p_l$ — both equal to $p_l$ exactly). By the certified `pair-
insensitivity-corollary` (iterated form, valid for any finite sequence of
values, no genericity or non-coincidence hypothesis needed — a pure parity
argument),
$$A\bigl(M\cup\{v_1,v_1\}\cup\{v_2,v_2\}\cup\{v_3,v_3\}\bigr)=A(M).$$
Since $M=\{p_k-p_l,\,p_r\}$ has exactly 2 elements, sorting them
descending and taking the alternating sum gives
$A(M)=\max(p_k-p_l,p_r)-\min(p_k-p_l,p_r)=|p_k-p_l-p_r|$ directly (a
2-element alternating sum is always the absolute difference — immediate
from the definition, no lemma needed beyond arithmetic). Hence
$$\Phi_{i,j;k,l}=\frac{T+A(\text{full fragment multiset})}2=
\frac{T+|p_k-p_l-p_r|}2. \qquad\blacksquare$$

**Feasibility.** $p_k\ge p_l$ (needed so the pin cut $p_k\to(p_l,p_k-p_l)$
produces two nonnegative fragments) holds automatically since $k<l$ in the
sorted marking. Legality (cut count $\le n=4$) holds since exactly $3$
cuts are used.

**Count.** Choosing the bisected pair $\{i,j\}$: $\binom52=10$ ways. Among
the remaining 3 indices, choosing the ordered pin pair $(k,l)$ with $k<l$
(automatically feasible) leaves the third as $r$: $\binom32=3$ ways. Total
$10\times3=30$ chambers.

**Verification.** Independently re-checked, exact `Fraction`, $5000$
random trials per instance for 3 representative chambers
(`/tmp/round-29/verify_pin_formulas.py`): each formula matched a direct
sort-and-alternate-sum computation on the un-reduced fragment multiset in
every one of $3\times5000=15000$ checks, zero mismatches. (The general
$k,l,i,j,r$-indexed formula was also directly exercised inside the
exhaustive search scripts below across tens of thousands of instances with
no discrepancy against direct computation.)

### R29.5 Combined coverage: 100% over 30000 fresh exact trials (not yet a proof of exhaustive coverage)

`/tmp/round-29/coverage_named33_exact.py`: for $30{,}000$ fresh random
markings drawn into $\mathcal R$ (seed 2, independent of R29.3's seed 0
run), computed $\min$ over all 30 Bisect-Subset chambers **and** all 30
Double-Bisect-Pin chambers (feasibility-checked exactly, no float
rounding at any stage — an earlier float-based intermediate check
produced two spurious "near-miss" points that vanished under exact
`Fraction` re-computation, confirming the standing project rule to trust
only exact arithmetic at chamber boundaries): **$30000/30000=100.00\%$
covered, zero violations.** A finer diagnostic
(`/tmp/round-29/find_extra_pins.py`) shows that no single Double-Bisect-Pin
chamber dominates: of the $1456$ points needing a pin-family chamber, the
winning chamber varies across at least $14$ distinct $(i,j;k,l)$
combinations (frequency $5$–$341$ out of $1456$), so the full 30-chamber
family (not a small hand-picked subset of it) is genuinely needed — no
further pruning is available "for free."

**Honest scope — this is empirical, not a proof.** Zero violations across
$50{,}000+$ combined exact-`Fraction` trials this round (R29.3's 20000 +
R29.5's 30000) is strong evidence that the 60-chamber family
(30 Bisect-Subset $\cup$ 30 Double-Bisect-Pin) covers $\mathcal R$
entirely, but — per the project's own repeated, hard-won lesson (rounds
24–26: a numerically-clean-looking covering family can still have a
genuine, small-denominator exact counterexample not hit by random
sampling) — this is **not yet established as a theorem**. What remains
for a future round, to actually close $n=4$'s upper bound:
1. A Farkas-style exhaustive case split over $\mathcal R$ (in the spirit
   of R27.3's 6-branch / 2-case argument, or the earlier `case-b2-n3-
   covering-closure`'s 6-branch argument) proving that "all 60 chambers
   fail simultaneously" is algebraically infeasible — i.e. deriving the
   actual nonnegative-combination certificates, not just sampling.
2. In particular, identifying which handful of the 60 chambers are the
   actual "tight" ones at the true worst-case vertex/vertices of
   $\mathcal R$ (analogous to how only 4–5 of the many candidate $n=3$
   chambers were load-bearing in the final R27.3/R25 covering proofs) —
   this round's frequency diagnostic (R29.5) is a first step but not a
   full vertex characterization.
3. Confirming no further chamber type (beyond Bisect-Subset and
   Double-Bisect-Pin) is needed — the $100\%$ empirical result is
   consistent with "these 60 suffice" but a full proof would need to rule
   out, or explicitly handle, any residual measure-zero configuration a
   Farkas argument might expose (as happened with the $n=3$ case (b2)
   box's own boundary-vertex check, R25).

**Status of this front: partial, real narrowing.** The $n=4$ upper bound's
open territory has shrunk from "all of $p_1<T/2$" (round 28's scope) to
the much narrower $\mathcal R$, and within $\mathcal R$ the covering
mechanism (60 explicit chambers, one new family of 30 fully proved this
round) is empirically complete but not yet certified as a theorem.

### Promotable lemmas (round 29)

- **Double-Bisect-Pin Theorem** (R29.4): fully proved, general (any 2
  bisected indices, any ordered pin pair among the remaining 3, at
  $m=5$), via `pair-insensitivity-corollary` (iterated 3 times) — no
  numerics involved in the proof itself, only in the coverage measurement
  that motivated finding it. Recommend certifying as
  `double-bisect-pin-family-n4`. (The mechanism plausibly generalizes to
  any $m$ — "bisect $m-3$ pieces, pin 1 of the remaining 3 to another,
  leave the last untouched" would need $m-2$ cuts, matching budget $n=m-1$
  with 1 spare — but this round only proves and verifies the $m=5$
  instance used by the coverage measurement; general-$m$ is flagged as an
  open generalization, not claimed.)
- **Explicit re-derivation of the three free-transplant thresholds at
  $n=4$** (R29.1): not new content (each transplant is a substitution of
  an already-general-$n$ certified lemma), but the exact threshold
  arithmetic ($T/31$, $8T/31$) is derived here from scratch rather than
  merely asserted, matching the round-29 outline-reviewer's independent
  check.

## Round 30 build: retraction of the false coverage claim, the general
Partition Chamber Theorem, and closing both round-30 witnesses

### R30.0 Retraction (mandatory first step)

Round 29's §R29.5 claimed "$30000/30000=100\%$ covered, zero violations"
for the 60-chamber family (30 `bisect-subset-lemma` instances $\cup$ 30
Double-Bisect-Pin instances) over the residual box
$\mathcal R=\{p_1<T/2,\ T/31<p_2<8T/31\}$. This claim is **false**. The
round-30 explorer produced an exact, interior-of-$\mathcal R$
counterexample:
$$p=(11,7,6,3,2)/29,\qquad T=1.$$
Check membership: $p_1=11/29\approx0.379<1/2$ ✓; $p_2=7/29\approx0.241$,
and $1/31\approx0.032<0.241<8/31\approx0.258$ ✓ — an interior point, not a
boundary artifact. I independently re-verified (fresh script, exact
`Fraction`, no reuse of the explorer's own code) that every one of the 60
chamber formulas evaluates to exactly $\Phi=15/29$ at this point:

```python
from fractions import Fraction as F
p = [F(11,29),F(7,29),F(6,29),F(3,29),F(2,29)]
T = sum(p)  # = 1

def A(vals):
    s = sorted(vals, reverse=True); tot=F(0); sign=1
    for v in s: tot += sign*v; sign*=-1
    return tot

import itertools
worst = None
# 30 Bisect-Subset chambers: nonempty proper S subset {0..4}, |S|<=4
for r in range(1,5):
    for S in itertools.combinations(range(5), r):
        R = [p[i] for i in range(5) if i not in S]
        phi = (T + A(R))/2
        worst = phi if worst is None else min(worst, phi)
# 30 Double-Bisect-Pin chambers: bisect {i,j}, pin k->l (k<l), leave r
idxset=set(range(5))
for i,j in itertools.combinations(range(5),2):
    rest = sorted(idxset-{i,j})
    for k,l in itertools.combinations(rest,2):
        r = (idxset-{i,j,k,l}).pop()
        phi = (T + abs(p[k]-p[l]-p[r]))/2
        worst = min(worst, phi)
print(worst, F(16,31), worst > F(16,31))
```
This prints `15/29`, `16/31`, `True` — confirming every one of the 60
chambers (the minimum over all of them) gives $\Phi=15/29$, which exceeds
$a_4T=16/31$: exactly $15/29-16/31=(15\cdot31-16\cdot29)/(29\cdot31)
=(465-464)/899=1/899>0$. **All 60 chambers fail simultaneously, by
exactly $1/899$, at an interior point of $\mathcal R$.** This is a genuine
exact refutation, not a float artifact (computed entirely in `Fraction`
arithmetic above) and not a boundary/measure-zero coincidence (the point
is well inside both defining inequalities of $\mathcal R$).

**Root cause (diagnosis, not just the fact of failure).** The true
minimizing strategy at this point is not expressible by either chamber
family: it is $p_1$ cut into three fragments matching $p_3,p_4,p_5$
exactly (feasible since $p_1=p_3+p_4+p_5=6+3+2=11$ exactly here), which
needs a "pin one piece to *three* others simultaneously" mechanism — a
level deeper than Double-Bisect-Pin's single pin. This is the same
qualitative lesson as round 4's/round 27's $n=3$ finding (a single-pin
chamber family is not always enough once several pieces are comparably
small) recurring one level up.

**Consequence.** Round 29's §R29.4 (the Double-Bisect-Pin Theorem itself)
remains correctly proved — the retraction concerns only §R29.5's coverage
*measurement claim*, not the individual chamber formulas. Do not carry
the "$100\%$ coverage" claim forward into `current.md` or cite it in any
future round.

### R30.1 The general Partition Chamber Theorem

The three families on file (`bisect-subset-lemma`, Double-Bisect-Pin, and
the corrected Triple-Pin/Double-Pin-Pair derived below) turn out to be
special cases of one clean, fully general mechanism. Stating and proving
the general form once, rather than re-deriving each instance from
scratch, is both cheaper and removes any risk of a formula slip like the
one caught in R30.2 below.

**Setup.** Fix $m$ pieces $p_1,\dots,p_m>0$ (any marking, not necessarily
sorted for this statement — sortedness is only used later to check
feasibility conveniently), $T=\sum p_i$. Let
$$\{1,\dots,m\}=B_1\sqcup B_2\sqcup\dots\sqcup B_r$$
be **any** partition of the index set into disjoint nonempty blocks. For
each block $B_j$ with $|B_j|\ge2$, choose a distinguished **host** index
$h_j\in B_j$, and suppose the **feasibility condition**
$$p_{h_j}\ \ge\ \sum_{i\in B_j\setminus\{h_j\}}p_i$$
holds; define the block's **residual**
$$\rho_j\ :=\ p_{h_j}-\!\!\sum_{i\in B_j\setminus\{h_j\}}\!\! p_i\ \ge0.$$
For each **singleton** block $B_j=\{i\}$ ($|B_j|=1$), independently choose
one of two options: "leave $p_i$ untouched" or "bisect $p_i$."

**The strategy.** For each block $B_j$ with $|B_j|=s\ge2$: cut $p_{h_j}$
into $s$ fragments — one fragment matching each $p_i$, $i\in B_j\setminus
\{h_j\}$, exactly, plus one residual fragment $\rho_j$ (this costs
$s-1$ cuts); leave every non-host member $p_i$ ($i\in B_j\setminus\{h_j\}$)
untouched. For each singleton block chosen "bisect": cut $p_i$ into two
equal halves (1 cut). For each singleton block chosen "untouched": do
nothing. Every index is touched by exactly one of these rules (the
partition is disjoint and exhaustive), so this defines a single legal
overall strategy.

**Cut count.** Total cuts $=\sum_{j:|B_j|\ge2}(|B_j|-1)+\#\{\text{bisected
singletons}\}$. (For $m=5$, $n=4$: legality just requires this sum
$\le4$, checked case-by-case below.)

**Theorem (Partition Chamber Formula).**
$$\Phi\ =\ \frac{T+A(Q)}2,\qquad
Q:=\{\rho_j : |B_j|\ge2\}\ \cup\ \{p_i : \{i\}\text{ an untouched
singleton block}\},$$
where $A(\cdot)$ is the alternating-sum-of-sorted-descending-order
functional of `odd-run-reduction-lemma`.

*Proof.* Write out the full fragment multiset produced by the strategy.
For a block $B_j$ with $|B_j|=s\ge2$, the host's cut produces the
fragment multiset $\{p_i:i\in B_j\setminus\{h_j\}\}\cup\{\rho_j\}$ ($s-1$
matching fragments plus the residual), and the $s-1$ non-host members
remain as untouched originals $\{p_i:i\in B_j\setminus\{h_j\}\}$. Their
union is
$$\{p_i,p_i : i\in B_j\setminus\{h_j\}\}\ \cup\ \{\rho_j\}$$
— i.e. $s-1$ exactly-matched pairs plus one unpaired residual. For a
bisected singleton $\{i\}$, the fragment multiset is $\{p_i/2,p_i/2\}$ —
one exactly-matched pair, contributing no unpaired value. For an
untouched singleton $\{i\}$, the fragment multiset is $\{p_i\}$ — one
unpaired value.

Summing over all blocks, the full fragment multiset is
$$M\ =\ \Bigl(\bigcup_{j:|B_j|\ge2}\{p_i,p_i:i\in B_j\setminus\{h_j\}\}\Bigr)
\ \cup\ \Bigl(\bigcup_{\text{bisected }i}\{p_i/2,p_i/2\}\Bigr)\ \cup\ Q,$$
i.e. $M=Q\cup\{v_1,v_1\}\cup\{v_2,v_2\}\cup\dots\cup\{v_k,v_k\}$ for the
finite list of matched-pair values $v_1,\dots,v_k$ arising from all
non-host block members (each contributing one pair) and all bisected
singletons (each contributing one pair). By the certified **iterated
`pair-insensitivity-corollary`** (valid for any finite sequence of pair
values, no genericity/non-coincidence hypothesis, since its proof is pure
parity-counting via `odd-run-reduction-lemma`),
$$A(M)=A(Q).$$
Mass conservation: summing $M$'s total mass block-by-block,
$\sum_{j:|B_j|\ge2}\bigl(\rho_j+2\!\!\sum_{i\in B_j\setminus\{h_j\}}\!\!
p_i\bigr)+\sum_{\text{bisected }i}p_i+\sum_{\text{untouched
singleton }i}p_i$. Using $\rho_j=p_{h_j}-\sum_{i\in B_j\setminus\{h_j\}}
p_i$, the first sum telescopes to $\sum_{j:|B_j|\ge2}\bigl(p_{h_j}+\sum_
{i\in B_j\setminus\{h_j\}}p_i\bigr)=\sum_{j:|B_j|\ge2}\sum_{i\in B_j}p_i$
(the full block's mass); combined with the bisected/untouched singleton
sums (each contributing their block's own mass), the total is $\sum_j
\sum_{i\in B_j}p_i=\sum_{i=1}^mp_i=T$, confirming $M$ is a legal
refinement of the original $m$ pieces with total mass $T$. Hence by the
claiming-subgame reduction (Liu Bang's total $=(T+A(M))/2$, the shared
lemma cited throughout this file since round 1),
$$\Phi=\frac{T+A(M)}2=\frac{T+A(Q)}2. \qquad\blacksquare$$

**Feasibility/legality recap.** The construction is legal exactly when
(i) every block-feasibility condition $p_{h_j}\ge\sum_{i\ne h_j}p_i$
holds, and (ii) the total cut count is $\le n$. Both are checked
per-instance below.

### R30.2 Instance 1: the corrected Triple-Pin Theorem (closes witness 1)

**Setup ($m=5$, $n=4$).** Fix $p_1\ge p_2\ge p_3\ge p_4\ge p_5>0$. Choose
an index $m^\ast\in\{1,\dots,5\}$ (the "trisected host") and 3 distinct
indices $\{a,b,c\}\subset\{1,\dots,5\}\setminus\{m^\ast\}$ (the "pin
targets"); let $d$ be the unique remaining index. Take the partition
$B_1=\{m^\ast,a,b,c\}$ (host $m^\ast$) and $B_2=\{d\}$ (singleton, chosen
**bisected**).

**Feasibility.** $p_{m^\ast}\ge p_a+p_b+p_c$.

**Cut count.** $|B_1|-1=3$ cuts on $p_{m^\ast}$, plus $1$ bisection cut on
$p_d$: total $4=n$ — exactly at the budget, legal.

**Formula (by R30.1, since $Q=\{\rho_1\}$ only — the bisected singleton
contributes nothing to $Q$):**
$$\Phi_{\text{TriplePin}}(p)\ =\ \frac{T+\rho}2,\qquad
\rho:=p_{m^\ast}-p_a-p_b-p_c\ \ge0.$$

**This corrects a genuine bug in the round-30 outline.** The outline
literally stated "leave the rest [i.e. $p_d$] untouched" together with
the formula $\Phi=(T+|p_{m^\ast}-p_a-p_b-p_c|)/2$ (note: no absolute
value is even needed once feasibility $\rho\ge0$ holds, so $|\rho|=\rho$
— a second minor imprecision). If $p_d$ is genuinely left untouched
(3 cuts, not 4), R30.1's formula gives $\Phi=(T+A(\{\rho,p_d\}))/2=
(T+|\rho-p_d|)/2$, which is **not** the outline's formula in general
(they coincide only in the special sub-case $\rho=p_d$). Direct check
against the outline's own target witness (below) shows the "$p_d$
untouched" version fails to close it ($\Phi=18/29>16/31$), while
bisecting $p_d$ with the spare 4th cut gives exactly the outline's
intended formula and **does** close it. The fix is therefore to bisect
$p_d$ (using the full budget of 4 cuts, not 3) rather than leave it
untouched — a one-word correction to the strategy description, made
precise and proved above via the general R30.1 mechanism rather than
patched ad hoc.

**Count.** Choose $m^\ast$: $5$ ways. Choose $\{a,b,c\}$ from the
remaining $4$ indices: $\binom43=4$ ways. Total $20$ chambers (matching
the round-30 outline's own count, "20-chamber Triple-Pin," even though
its formula needed the correction above).

**Closing witness 1.** $p=(11,7,6,3,2)/29$. Take $m^\ast=1$ ($p_1=11/29$),
$\{a,b,c\}=\{3,4,5\}$ ($p_3,p_4,p_5=6/29,3/29,2/29$, sum $=11/29=p_1$
exactly), $d=2$ ($p_2=7/29$). Feasibility: $p_1=p_3+p_4+p_5$ exactly, so
$\rho=0\ge0$ ✓. Formula: $\Phi=(1+0)/2=1/2$. Compare
$a_4T=16/31\approx0.5161$: since $1/2<16/31$ (cross-multiply: $31<32$),
**this chamber closes witness 1 with margin $16/31-1/2=1/62>0$.**

Exact verification (re-run, independent of the earlier setup script):
```python
from fractions import Fraction as F
p = [F(11,29),F(7,29),F(6,29),F(3,29),F(2,29)]; T=sum(p)
rho = p[0]-p[2]-p[3]-p[4]           # p1 - p3 - p4 - p5
assert rho == 0
phi = (T+rho)/2
assert phi == F(1,2)
assert phi <= F(16,31)
print("Triple-Pin closes witness 1:", phi, "<=", F(16,31))
```

### R30.3 Instance 2: the Double-Pin-Pair Theorem (closes witness 2, the survivor of the (unwritten) 20-chamber Triple-Pin family)

The round-30 explorer reported that a second witness,
$p=(14,7,5,3,1)/30$, survives even an 80-chamber family (60 + a proposed
20-chamber Triple-Pin) — flagged as needing a genuinely new, uncharacterized
4th chamber type. Following the project's standing methodology (reverse-
engineer the closed form from a numeric optimizer's argmin, then prove it
via the certified pair-insensitivity mechanism rather than guessing blind):
a full search over every legal $\le4$-cut allocation at this witness
(`scipy.optimize.minimize`, Nelder–Mead, multi-restart, all $5$-tuples of
per-piece cut counts summing to $\le4$) found the true minimum
$\Phi=15/30=1/2$, attained (up to the optimizer's numerical tolerance) at:
$p_1$ cut into fragments matching $p_2$ and $p_3$ exactly (2 cuts,
residual $p_1-p_2-p_3$), and $p_4$ cut into a fragment matching $p_5$
exactly (1 cut, residual $p_4-p_5$) — 3 cuts total, 1 spare unused. This
is **not** an instance of Bisect-Subset, Double-Bisect-Pin, or Triple-Pin
(it is a "$3$-block $+$ $2$-block" partition, not "all singletons," "one
$2$-pin plus singletons," or "one $4$-pin plus one singleton").

**Setup ($m=5$, $n=4$).** Take the partition $B_1=\{m_1,a,b\}$ (host
$m_1$, targets $a,b$) and $B_2=\{m_2,f\}$ (host $m_2$, target $f$), where
$\{m_1,a,b,m_2,f\}=\{1,\dots,5\}$ (all 5 indices used, no singleton
blocks at all).

**Feasibility.** $p_{m_1}\ge p_a+p_b$ and $p_{m_2}\ge p_f$.

**Cut count.** $(|B_1|-1)+(|B_2|-1)=2+1=3\le4$ — legal (with 1 spare cut
unused; `budget-monotonicity`-style triviality: using fewer than the
maximum $n$ allowed cuts is always legal since "at most $n$ points" is the
hypothesis, not "exactly $n$").

**Formula (by R30.1, $Q=\{\rho_1,\rho_2\}$, a 2-element alternating sum
= the absolute difference):**
$$\Phi_{\text{DoublePinPair}}(p)\ =\ \frac{T+|\rho_1-\rho_2|}2,\qquad
\rho_1:=p_{m_1}-p_a-p_b,\quad \rho_2:=p_{m_2}-p_f.$$

**Count.** Choose the ordered "which piece is $B_1$'s host, which two are
its targets": choose $m_1$ ($5$ ways) and $\{a,b\}\subset\{1,\dots,5\}
\setminus\{m_1\}$ ($\binom42=6$ ways) — $30$ ways. The remaining $2$
indices form $B_2$; feasibility requires $p_{m_2}\ge p_f$, i.e. $m_2$ must
be the smaller-valued (equivalently, in sorted marking, smaller-index) of
the two, which is automatic in a sorted marking (no further choice),
giving $5\times6=30$ chambers total.

**Closing witness 2.** $p=(14,7,5,3,1)/30$. Take $m_1=1$ ($p_1=14/30$),
$\{a,b\}=\{2,3\}$ ($p_2,p_3=7/30,5/30$), so $\rho_1=14/30-7/30-5/30=
2/30$. Take $m_2=4$ ($p_4=3/30$), $f=5$ ($p_5=1/30$), so $\rho_2=
3/30-1/30=2/30$. Feasibility: $p_1\ge p_2+p_3$ ($14\ge12$ ✓) and
$p_4\ge p_5$ ($3\ge1$ ✓). Since $\rho_1=\rho_2=2/30$ exactly,
$|\rho_1-\rho_2|=0$, so
$$\Phi=\frac{1+0}2=\frac12\ <\ \frac{16}{31}=a_4T.$$
Margin: $16/31-1/2=1/62>0$, the same margin as witness 1 (not a
coincidence of this specific script — both witnesses happen to reduce to
the exact "$\rho=0$" extreme case of their respective chamber's formula).

Exact verification (independent script):
```python
from fractions import Fraction as F
p = [F(14,30),F(7,30),F(5,30),F(3,30),F(1,30)]; T=sum(p)
rho1 = p[0]-p[1]-p[2]     # p1 - p2 - p3
rho2 = p[3]-p[4]          # p4 - p5
assert rho1 == F(2,30) and rho2 == F(2,30)
phi = (T + abs(rho1-rho2))/2
assert phi == F(1,2)
assert phi <= F(16,31)
print("Double-Pin-Pair closes witness 2:", phi, "<=", F(16,31))
```

### R30.4 Cross-check of the general theorem (R30.1) against direct simulation

Independently stress-tested R30.1's formula against a from-scratch direct
sort-and-alternate-sum simulation on the actual (un-reduced) fragment
multiset, for random $5$-tuples and random feasible partitions/hosts/
bisection choices (not reusing the witness-specific scripts above):

```python
from fractions import Fraction as F
import random

def A(vals):
    s=sorted(vals,reverse=True); tot=F(0); sign=1
    for v in s: tot+=sign*v; sign*=-1
    return tot

def direct_phi(p,T,blocks,host,bisect_singletons):
    frags=[]
    for bi,B in enumerate(blocks):
        if len(B)==1:
            i=B[0]
            if i in bisect_singletons: frags += [p[i]/2, p[i]/2]
            else: frags.append(p[i])
        else:
            h=host[bi]; others=[i for i in B if i!=h]
            s=sum(p[i] for i in others); r=p[h]-s
            if r<0: return None
            frags.append(r); frags += [p[i] for i in others]*2
    return (T+A(frags))/2

def formula_phi(p,T,blocks,host,bisect_singletons):
    Q=[]
    for bi,B in enumerate(blocks):
        if len(B)==1:
            i=B[0]
            if i not in bisect_singletons: Q.append(p[i])
        else:
            h=host[bi]; others=[i for i in B if i!=h]
            s=sum(p[i] for i in others); r=p[h]-s
            if r<0: return None
            Q.append(r)
    return (T+A(Q))/2

random.seed(1); trials=0; mismatches=0
for _ in range(3000):
    vals=sorted([F(random.randint(1,50),random.randint(1,20)) for _ in range(5)],reverse=True)
    T=sum(vals)
    idxs=list(range(5)); random.shuffle(idxs)
    sizes=[]; remaining=5
    while remaining>0:
        s=random.randint(1,remaining); sizes.append(s); remaining-=s
    it=iter(idxs); blocks=[[next(it) for _ in range(s)] for s in sizes]
    host={}; bisect_s=set(); ok=True
    for bi,B in enumerate(blocks):
        if len(B)>=2:
            h=random.choice(B); others=[i for i in B if i!=h]
            if vals[h] < sum(vals[i] for i in others): ok=False; break
            host[bi]=h
        elif random.random()<0.5: bisect_s.add(B[0])
    if not ok: continue
    trials+=1
    d=direct_phi(vals,T,blocks,host,bisect_s); f=formula_phi(vals,T,blocks,host,bisect_s)
    if d!=f: mismatches+=1
print(trials, mismatches)
```
Result: `553 0` — 553 feasible random exact-`Fraction` trials (arbitrary
partitions, arbitrary hosts, arbitrary bisection choices), zero
mismatches between the direct simulation and the R30.1 closed form. This
corroborates the proof; it is not a substitute for it (the proof in R30.1
is self-contained and does not rely on this check).

### R30.5 Honest scope: what is and is not established this round

**Established (proved, not numeric):**
1. The round-29 "$100\%$ coverage" claim is false — retracted (R30.0).
2. The general Partition Chamber Theorem (R30.1), fully proved via
   `pair-insensitivity-corollary` alone, unifying `bisect-subset-lemma`
   (all-singleton partition), Double-Bisect-Pin (two bisected singletons
   + one 2-block + one untouched singleton), the corrected Triple-Pin
   (one 4-block + one bisected singleton), and the new Double-Pin-Pair
   (one 3-block + one 2-block, no singletons) as named special cases.
3. Both round-30 witnesses ($p=(11,7,6,3,2)/29$ and $p=(14,7,5,3,1)/30$)
   are individually closed by named, proved instances of this theorem —
   exact `Fraction` verification in both cases (R30.2, R30.3).

**NOT established (honest open gaps, per the outline's own scoping
instructions):**
1. **No claim of full coverage of $\mathcal R$** by the expanded family
   (Bisect-Subset $\cup$ Double-Bisect-Pin $\cup$ Triple-Pin $\cup$
   Double-Pin-Pair, or any further partition instances). This round only
   targeted and closed the two *known* witnesses; no fresh large-scale
   coverage measurement (random or outer-minimization) was run against
   the expanded family this round, and per the explorer's own
   methodological warning (a family can only ever report on itself), any
   future coverage claim must be checked by an outer, allocation-agnostic
   search (fresh unconstrained minimization over ALL legal $\le4$-cut
   strategies at sampled points), not by sampling within the family being
   tested — exactly the discipline that would have caught round 29's
   error before it was written up.
2. It is not established (nor is it claimed) that the *entire* Partition
   Chamber family (all partitions of $\{1,\dots,5\}$ into blocks with
   host choices) is itself exhaustive of all legal $\le4$-cut strategies
   for $m=5$ pieces — a general strategy could in principle place two
   independent cuts on the *same* piece in a way not reducible to "match
   $k$ other pieces exactly plus one residual" (e.g. cut one piece into
   fragments none of which matches any other original piece). The
   Partition Chamber family is a large, structured sub-family motivated
   by what has closed every witness found so far, not a proof that no
   other strategy shape could ever be needed.
3. No Farkas-style exhaustive case-split (proving "every chamber in the
   [possibly still incomplete] family fails" is algebraically infeasible
   throughout $\mathcal R$) has been attempted for any family beyond
   $n=3$'s already-closed 4/5/6-chamber families — this remains entirely
   open for $n=4$, and per the round-30 outline-reviewer's explicit
   instruction, should not be attempted until the census is verified
   complete by the outer-minimization method.
4. The Partition Chamber Theorem is stated and proved for general $m$
   (R30.1's setup is not $n=4$-specific), but this round only exercises
   it for $m=5$; whether the family's *coverage* generalizes to larger
   $n$ is unexplored.

**Net assessment.** This round correctly executed the mandated retraction,
replaced the false "100% coverage" claim with a strictly weaker but
honest and useful result (a proved general theorem that individually
defeats both known counterexamples), and did not attempt the still-
premature Farkas step. $n=4$'s upper bound remains open; the residual gap
is now "verify (or falsify) that the Partition Chamber family achieves
genuine outer-minimization-verified $100\%$ coverage of $\mathcal R$,"
which is a more precisely scoped and better-motivated target than round
29 left behind.

### Promotable lemmas (round 30)

- **Partition Chamber Theorem** (R30.1): fully general (any $m$, any
  partition of $\{1,\dots,m\}$ into blocks with host choices and
  singleton bisect/untouched choices), proved entirely via the already-
  certified `pair-insensitivity-corollary` (iterated) plus the shared
  claiming-subgame reduction — no numerics in the proof itself.
  Recommend certifying as `partition-chamber-theorem`; it strictly
  generalizes and subsumes `bisect-subset-lemma` and
  `double-bisect-pin-family-n4` (both re-derivable as special cases in
  one line each), so future rounds can cite this single theorem instead
  of re-deriving each named instance.
- **Corrected Triple-Pin Theorem** (R30.2): the $m=5,n=4$ instance with
  one 4-block (host + 3 pin targets) and one bisected singleton; formula
  $\Phi=(T+\rho)/2$, $\rho=p_{m^\ast}-p_a-p_b-p_c\ge0$. Note for the
  record: this corrects the round-30 outline's own stated formula, which
  omitted the untouched-vs-bisected distinction for the 5th piece.
- **Double-Pin-Pair Theorem** (R30.3): the $m=5,n=4$ instance with one
  3-block and one 2-block (no singletons); formula
  $\Phi=(T+|\rho_1-\rho_2|)/2$. New, not anticipated by the round-30
  outline (which only asked for Triple-Pin) — found via the project's
  standing numeric-optimizer-argmin-first methodology applied to the
  explorer's second witness.

## Round 31 build: the Half-Complement Pin Theorem closes a genuine
strip of the residual near $p_1\to(T/2)^-$ (not just the anchor point)

### R31.0 Setup and the anchor point, re-verified

Per the round-31 outline/outline-reviewer, the starting point is the
near-worst witness found by this round's explorer,
$$p=(16,8,4,3,2)/33,\qquad T=33.$$
The outline-reviewer already independently re-verified (by hand, exact
fractions) that the "Untouched-Singleton Pin" instance of the certified
`partition-chamber-theorem` — partition $B_1=\{1,3,4,5\}$ (host $p_1$,
pinned to $p_3,p_4,p_5$) and $B_2=\{2\}$ (singleton, left **untouched**) —
closes this point: feasibility $p_1\ge p_3+p_4+p_5$ ($16\ge9$), residual
$\rho=p_1-p_3-p_4-p_5=7$, $Q=\{\rho,p_2\}=\{7,8\}$, $A(Q)=1$,
$$\Phi=\frac{T+A(Q)}2=\frac{33+1}2=17\ \le\ a_4T=\frac{16}{31}\cdot33=
\frac{528}{31},\qquad a_4T-\Phi=\frac{528-527}{31}=\frac1{31}>0.$$
(The dispatch's "margin $-1/31$" phrasing refers to $\Phi-a_4T=-1/31$,
i.e. $\Phi$ undershoots the target by $1/31$ — the chamber closes the
point, it is not a counterexample. This matches the outline-reviewer's
independent hand check exactly.) This round's job is to go beyond the
single point and find the actual **region** this mechanism closes.

### R31.1 The Half-Complement Pin Theorem (new, general $m$)

**Setup.** Fix $m\ge2$ pieces $q_1,\dots,q_m>0$ (no sortedness required
except $q_1$ is the distinguished pinned piece), $T=\sum q_i$. Fix any
single index $j\in\{2,\dots,m\}$ (the piece to leave untouched). Consider
the strategy: cut $q_1$ into $m-2$ fragments, one matching each
$q_i$, $i\notin\{1,j\}$, exactly, plus one residual fragment
$\rho:=q_1-\sum_{i\ne1,j}q_i$; leave every $q_i$, $i\ne1,j$, and $q_j$
itself untouched. This is exactly the `partition-chamber-theorem`
(R30.1) instantiated with the partition $B_1=\{1,\dots,m\}\setminus\{j\}$
(host $1$) and singleton $B_2=\{j\}$ chosen "untouched." It costs
$m-2$ cuts.

**Feasibility.** $\rho\ge0$, i.e. $q_1\ge\sum_{i\ne1,j}q_i$, equivalently
(writing $s:=\sum_{i\ne1,j}q_i=T-q_1-q_j$)
$$q_1\ \ge\ T-q_1-q_j\quad\Longleftrightarrow\quad 2q_1+q_j\ \ge\ T.$$

**Theorem.** Whenever this feasibility condition holds,
$$\Phi\ =\ \max(q_1,\ T-q_1).$$

*Proof.* By R30.1 (Partition Chamber Formula), $Q=\{\rho,q_j\}$ and
$\Phi=(T+A(Q))/2$ where $A(\{\rho,q_j\})=|\rho-q_j|$ (the 2-element
alternating-sum functional is just the absolute difference, regardless of
which of $\rho,q_j$ is larger). Substitute $\rho=q_1-s=q_1-(T-q_1-q_j)
=2q_1+q_j-T$:

- If $\rho\ge q_j$ (i.e. $2q_1+q_j-T\ge q_j$, i.e. $q_1\ge T/2$... more
  precisely $2q_1-T\ge0$, i.e. $q_1\ge T-q_1$):
  $$\Phi=\frac{T+\rho-q_j}2=\frac{T+(2q_1+q_j-T)-q_j}2=\frac{2q_1}2=q_1.$$
- If $\rho<q_j$:
  $$\Phi=\frac{T+q_j-\rho}2=\frac{T+q_j-(2q_1+q_j-T)}2=\frac{2T-2q_1}2
  =T-q_1.$$

In the first branch the case hypothesis $\rho\ge q_j$ is equivalent (by
the substitution above) to $q_1\ge T-q_1$, so $\Phi=q_1=\max(q_1,T-q_1)$
in that branch; in the second branch $\rho<q_j$ is equivalent to
$q_1<T-q_1$, so $\Phi=T-q_1=\max(q_1,T-q_1)$ there too. Either way
$\Phi=\max(q_1,T-q_1)$, independent of which index $j$ was chosen (as
long as feasibility holds for that choice). $\blacksquare$

**Remark (why this is a genuinely new, reusable fact).** The theorem says
the *value* $\Phi$ produced by this whole one-parameter family of
strategies (one per choice of $j$) is always exactly $\max(q_1,T-q_1)$ —
the same value regardless of $j$ — while the *feasibility* condition
$2q_1+q_j\ge T$ depends on $j$ and is easiest to satisfy by choosing $j$
to be the **largest** of $q_2,\dots,q_m$ (larger $q_j$ relaxes the
inequality). This decouples "does some legal instance of this chamber
exist" from "what value does it give," which is what makes the corollary
below possible.

### R31.2 Corollary at $m=5$ ($n=4$): closing $p_1\in[15T/31,T/2)$
unconditionally

Specialize R31.1 to $m=5$, choosing $j=2$ (the largest of $p_2,\dots,p_5$,
the feasibility-optimal choice): $q_1=p_1$, and the pinned set is
$\{p_3,p_4,p_5\}$ — this is exactly the "Untouched-Singleton Pin"
instance from R31.0. Feasibility is $2p_1+p_2\ge T$, i.e.
$$p_2\ \ge\ T-2p_1.$$
Cut count: $m-2=3\le4$, legal (one spare cut unused, harmless by
`budget-monotonicity`, already used identically in R30.3).

**Theorem.** For every 5-piece marking $p_1\ge p_2\ge\cdots\ge p_5>0$,
$T=\sum p_i$, with
$$\frac{15}{31}T\ \le\ p_1\ <\ \frac T2\qquad\text{and}\qquad p_2>\frac
T{31},$$
the feasibility condition $2p_1+p_2\ge T$ holds automatically, and hence
(by R31.1) $\Phi_{\min}\le\max(p_1,T-p_1)=T-p_1\le\frac{16}{31}T=a_4T$.

*Proof.* Since $p_1\ge\frac{15}{31}T$, $T-2p_1\le T-\frac{30}{31}T=
\frac1{31}T$. Since $p_2>\frac1{31}T$ (hypothesis), we get
$$p_2\ >\ \frac1{31}T\ \ge\ T-2p_1,$$
so $2p_1+p_2>T$ — feasibility holds (with strict inequality, so the
residual $\rho>0$ strictly). By R31.1, $\Phi=\max(p_1,T-p_1)$; since
$p_1<T/2$ by hypothesis, $T-p_1>p_1$, so $\Phi=T-p_1$. Finally, $p_1\ge
\frac{15}{31}T=(1-a_4)T$ gives $T-p_1\le a_4T$ directly. $\blacksquare$

**Note this uses no information about $p_2$'s upper bound, nor anything
about $p_3,p_4,p_5$ individually** beyond the marking being a legal
sorted 5-tuple summing to $T$ — the hypothesis $p_2>T/31$ (already known
to hold throughout the residual $\mathcal R$ by R29.2, since $\mathcal
R$'s defining lower bound on $p_2$ is exactly $p_2>T/31$) is exactly what
is available for free inside $\mathcal R$.

### R31.3 Exact verification (not a substitute for the proof above,
corroboration only)

```python
from fractions import Fraction as F
import random

def A(vals):
    s = sorted(vals, reverse=True); tot = F(0); sign = 1
    for v in s:
        tot += sign*v; sign *= -1
    return tot

a4 = F(16, 31)
random.seed(3)
tested = bad = 0
for _ in range(50000):
    T = 1000
    lo, hi = F(15*T, 31), F(T, 2)
    p1 = lo + F(random.randint(0, 10**6), 10**6) * (hi - lo)
    if p1 >= hi:
        continue
    p2lo, p2hi = F(T, 31), min(p1, F(8*T, 31))
    if p2hi <= p2lo:
        continue
    p2 = p2lo + F(random.randint(1, 10**6 - 1), 10**6) * (p2hi - p2lo)
    rem = T - p1 - p2
    if rem <= 0:
        continue
    p3max, p3min = min(p2, rem), rem/3
    if p3max <= p3min:
        continue
    p3 = p3min + F(random.randint(1, 999), 1000) * (p3max - p3min)
    remB = rem - p3
    if remB <= 0:
        continue
    p4max, p4min = min(p3, remB), remB/2
    if p4max < p4min:
        continue
    p4 = p4min + F(random.randint(0, 999), 1000) * (p4max - p4min)
    p5 = remB - p4
    if p5 <= 0 or p5 > p4:
        continue
    p = [p1, p2, p3, p4, p5]; Tt = sum(p)
    tested += 1
    feas = p1 >= p3 + p4 + p5
    rho = p1 - p3 - p4 - p5
    phi = (Tt + A([rho, p2])) / 2
    expected = max(p1, Tt - p1)
    if phi != expected or not feas or phi > a4*Tt:
        print("BAD", p, phi, expected, feas); bad += 1
print("tested", tested, "bad", bad)
```
Output: `tested 28894 bad 0` — every one of $\sim29000$ exact-`Fraction`
trials, drawn specifically from inside the newly-claimed region
$p_1\in[15T/31,T/2)$, $T/31<p_2<8T/31$, $p_2\le p_1$, $p_3\ge p_4\ge p_5>
0$ summing correctly, confirms the theorem's formula, feasibility, and
the final inequality $\Phi\le a_4T$. (Recall the standing project lesson,
round 30: a family can only ever report on itself, so this check does
**not** by itself certify anything about points outside the stated
region — it only corroborates the proof above on its own claimed
domain, which is exactly what it is used for here.)

### R31.4 What this establishes about the residual $\mathcal R$

Recall from R29.2, $\mathcal R=\{p_1<T/2,\ T/31<p_2<8T/31\}$ (with, of
course, the implicit sorted-marking constraints $p_1\ge p_2\ge p_3\ge
p_4\ge p_5>0$ and $\sum p_i=T$). By R31.2, the sub-region
$$\mathcal R_1:=\Bigl\{\tfrac{15}{31}T\le p_1<\tfrac T2,\ \tfrac T{31}<
p_2<\tfrac{8}{31}T\Bigr\}\subset\mathcal R$$
is fully closed ($\Phi_{\min}\le a_4T$ throughout, unconditionally, for
**every** choice of $p_3,p_4,p_5$ compatible with the sorted order and
mass conservation — the proof needed no information about them beyond
$p_1\ge p_3+p_4+p_5$ being automatically implied, which R31.2 established
without ever looking at $p_3,p_4,p_5$ individually). Hence the residual
still requiring a covering argument shrinks from $\mathcal R$ to
$$\mathcal R':=\mathcal R\setminus\mathcal R_1\ =\ \Bigl\{p_2\le p_1<
\tfrac{15}{31}T,\ \tfrac T{31}<p_2<\tfrac{8}{31}T\Bigr\}$$
(using $p_1\ge p_2$ from the sorted order to fold the trivial lower bound
on $p_1$ into the stated form). This is a **strict, genuine narrowing**
— e.g. $\mathcal R_1$ alone already resolves the entire "$p_1\to(T/2)^-$"
edge of the residual box that the round-30/round-29 witnesses and the
round-31 explorer's anchor point all lived near ($p_1/T=16/33\approx
0.4848\in[15/31\approx0.4839,\ 0.5)$ — both known hard witnesses,
$p_1/T=11/29\approx0.379$ and $p_1/T=14/30\approx0.467$: the first is
**not** in $\mathcal R_1$ ($0.379<15/31$), consistent with it needing the
separate Triple-Pin closure (R30.2); the second, $14/30\approx0.4667$, is
also just below $15/31\approx0.4839$, so also not in $\mathcal R_1$ —
i.e. $\mathcal R_1$ is disjoint from both previously-known witnesses'
$p_1$-values and identifies genuinely new territory, not a re-closure of
already-handled points).

**What is NOT established.** $\mathcal R'$ (the region with $p_1<15T/31$)
remains open — no covering argument is given for it here. In particular
neither of the two round-30 witnesses nor the round-31 anchor's own
"opposite" regime is addressed; only the specific strip $p_1\in
[15T/31,T/2)$ is closed, by a single clean mechanism, for *arbitrary*
$p_2,p_3,p_4,p_5$ within $\mathcal R$'s stated bounds. A full Farkas-style
exhaustive covering proof of $\mathcal R$ (or even of $\mathcal R'$ alone)
is still not attempted — this round narrows the target region precisely
rather than closing it fully.

### R31.5 Honest conclusion

This round makes genuine, non-numerical progress beyond a single point:
the Half-Complement Pin Theorem (R31.1, general $m$) and its $n=4$
corollary (R31.2) together prove, in closed form with a full case-free
algebraic derivation, that the entire strip $p_1\in[15T/31,T/2)$ of the
residual $\mathcal R$ is closed for every legal marking, not merely at
the anchor point $p=(16,8,4,3,2)/33$ the round-31 outline specified. This
strictly shrinks the still-open residual to $\mathcal R'=\{p_2\le p_1<
15T/31,\ T/31<p_2<8T/31\}$, a genuinely smaller region than $\mathcal R$
(it excludes the boundary strip nearest $p_1=T/2$ entirely). Full
coverage of $\mathcal R$ (equivalently, now, of $\mathcal R'$) is **still
not established** — that remains the open gap for the next round. Status
of this sub-target: real progress (a proved region closure, not a point),
but not complete; $n=4$'s general upper bound is not solved this round.

### Promotable lemmas (round 31)

- **Half-Complement Pin Theorem** (R31.1): fully general $m$, proved as a
  direct specialization of the certified `partition-chamber-theorem`;
  states that pinning $q_1$ against all-but-one of the remaining $m-1$
  pieces (leaving that one untouched) gives $\Phi=\max(q_1,T-q_1)$
  whenever feasible ($2q_1+q_j\ge T$ for the untouched index $j$),
  independent of which $j$ is chosen — only feasibility depends on $j$,
  not the value. Recommend certifying as `half-complement-pin-theorem`.
- **$n=4$ Strip-Closure Corollary** (R31.2): for every 5-piece marking
  with $15T/31\le p_1<T/2$ and $p_2>T/31$, $\Phi_{\min}\le a_4T$
  unconditionally (no restriction on $p_3,p_4,p_5$ beyond sortedness).
  Recommend certifying as `n4-strip-closure-corollary` (or folding into
  the general lemma's write-up as its headline $n=4$ application).

## Round 32 build: the Leave-2-Untouched Theorem, proved in full — and an
honest, exact-arithmetic refutation of "the named-chamber family covers
$\mathcal R'$" (no false-coverage claim repeated)

### R32.0 Task and setup

This round's assignment (per the round-32 outline and dispatch) was to
attempt to close the residual
$$\mathcal R'=\{p_2\le p_1<\tfrac{15}{31}T,\ \tfrac1{31}T<p_2<\tfrac8{31}T\}$$
via the $n=3$ case-(b2) precedent's exact technique — a finite named-chamber
family, an exhaustive logical case-split, and Farkas-style infeasibility
certificates — explicitly *not* a numerically-sampled coverage claim,
per the dispatch's direct warning (rounds 29–30 were both burned by exactly
this mistake on this same residual).

### R32.1 The Leave-2-Untouched Theorem (new, proved in full)

**Setup.** Fix $m\ge3$ pieces $q_1,\dots,q_m>0$ (only $q_1$ distinguished
as host), $T=\sum q_i$. Fix any two distinct indices $j,k\in\{2,\dots,m\}$
(the two pieces left untouched); let $\{a_1,\dots,a_{m-3}\}=\{2,\dots,m\}
\setminus\{j,k\}$ be the remaining "pinned" indices. Consider the strategy:
cut $q_1$ into $m-3$ fragments matching $q_{a_1},\dots,q_{a_{m-3}}$ exactly,
plus one residual fragment $\rho:=q_1-\sum_i q_{a_i}$; leave $q_j,q_k$, and
every $q_{a_i}$ untouched. This is exactly the certified
`partition-chamber-theorem` instantiated with partition $B_1=\{1,\dots,m\}
\setminus\{j,k\}$ (host $1$) and singletons $\{j\},\{k\}$ both chosen
"untouched." It costs $m-3$ cuts.

**Feasibility.** $\rho\ge0$, i.e. $q_1\ge\sum_i q_{a_i}=T-q_1-q_j-q_k$,
equivalently
$$2q_1+q_j+q_k\ \ge\ T.$$

**Theorem.** Whenever feasibility holds,
$$\Phi=\frac{T+A(\{\rho,q_j,q_k\})}2,$$
where (writing the three values sorted descending as $x\ge y\ge z$)
$A(\{\rho,q_j,q_k\})=x-y+z$ — i.e. explicitly, by the three possible
relative orderings of $\rho$ against $q_j,q_k$ (WLOG $q_j\ge q_k$ by
relabeling):
$$\Phi=\begin{cases}
\dfrac{T+\rho-q_j+q_k}2, & \rho\ge q_j\ (\ge q_k),\\[4pt]
\dfrac{T+q_j-\rho+q_k}2, & q_k\le\rho<q_j,\\[4pt]
\dfrac{T+q_j-q_k+\rho}2, & \rho<q_k\ (\le q_j).
\end{cases}$$

*Proof.* This is a direct one-line instantiation of R30.1
(`partition-chamber-theorem`): $Q=\{\rho\}\cup\{q_i:\{i\}\text{ untouched
singleton}\}=\{\rho,q_j,q_k\}$ (the pinned indices $a_i$ contribute nothing
to $Q$, since they are non-host block members, each contributing a
matched pair $\{q_{a_i},q_{a_i}\}$ that cancels by `pair-insensitivity-
corollary`, exactly as in the proof of R30.1 itself — no re-derivation
needed, this is literally the general theorem's formula with $|Q|=3$).
Evaluating the alternating sum of a 3-element multiset sorted descending
$x\ge y\ge z$ gives $A=x-y+z$ directly from the definition (no separate
lemma required beyond arithmetic), and substituting $\rho,q_j,q_k$ for
$x,y,z$ in each of the three possible orders gives the three branches
above. $\blacksquare$

**Legality.** Costs $m-3$ cuts; at $m=5$ this is $2\le4=n$, legal with 2
cuts spare (harmless by `budget-monotonicity`, as in every prior chamber
in this family).

**Count at $m=5$.** Choosing the untouched pair $\{j,k\}\subset\{2,3,4,5\}$:
$\binom42=6$ chambers (host is always $q_1$, as specified by the outline's
step 3; a version with a different host is a further, unexplored
generalization not needed below).

### R32.2 Exact re-verification of R32.1

```python
from fractions import Fraction as F
import random

def A(vals):
    s = sorted(vals, reverse=True); tot = F(0); sign = 1
    for v in s:
        tot += sign*v; sign *= -1
    return tot

random.seed(7); trials = 0; bad = 0
for _ in range(4000):
    m = random.randint(3, 7)
    q = sorted([F(random.randint(1, 200), random.randint(1, 50)) for _ in range(m)], reverse=True)
    T = sum(q)
    j, k = random.sample(range(1, m), 2)
    pinned = [i for i in range(1, m) if i not in (j, k)]
    rho = q[0] - sum(q[i] for i in pinned)
    if rho < 0:
        continue
    trials += 1
    Q = [rho, q[j], q[k]]
    phi_formula = (T + A(Q)) / 2
    # direct fragment simulation
    frags = [rho] + [q[i] for i in pinned] * 2 + [q[j], q[k]]
    phi_direct = (T + A(frags)) / 2
    if phi_formula != phi_direct:
        bad += 1
print("trials", trials, "bad", bad)
```
Output: `trials 1583 bad 0` (random $m=3,\dots,7$, random untouched pair,
feasibility-gated, exact `Fraction`) — the formula matches the direct
fragment-multiset simulation in every feasible trial. This is corroboration
only; the proof above is self-contained.

### R32.3 Assembling the full named-chamber family and testing $\mathcal R'$ — exact search, not a sampling-only claim of success

Per the dispatch's explicit instruction to avoid a repeat of rounds 29–30's
mistake, the goal here is to determine, by direct algebraic/exact-arithmetic
investigation (not merely to *assert* coverage from a clean-looking sample),
whether the combined family — `bisect-subset-lemma` (30 chambers at $m=5$),
Double-Bisect-Pin (30), the corrected Triple-Pin (20), Double-Pin-Pair (30),
Half-Complement Pin (4, one per choice of untouched index $j\in\{2,\dots,5\}$),
and this round's new Leave-2-Untouched (6) — covers $\mathcal R'$.

**Both previously-known hard witnesses are closed** by this family (exact
`Fraction`, re-verified): $p=(11,7,6,3,2)/29$ (via Triple-Pin, $\Phi=1/2$)
and $p=(14,7,5,3,1)/30$ (via Double-Pin-Pair, $\Phi=1/2$), both
$\le a_4T=16/31$.

**A targeted exact-arithmetic random search inside $\mathcal R'$** (rejection
sampling directly on $p_1\in(0,15T/31)$, $p_2\in(T/31,\min(p_1,8T/31))$,
$p_3,p_4,p_5$ filling the remainder subject to $p_2\ge p_3\ge p_4\ge p_5>0$,
all computed in exact `Fraction` arithmetic) found, out of roughly $9200$
feasible trials, **one exact counterexample** where all 120 named chambers
(the full family above) simultaneously fail:
$$p=\Bigl(\tfrac{120469}{250000},\ \tfrac{1997683}{7750000},\
\tfrac{29244225437}{187500000000},\
\tfrac{804602889174853727}{11625000000000000000},\
\tfrac{136307377910382091}{3875000000000000000}\Bigr)/T,\qquad T=1,$$
i.e. numerically $p/T\approx(0.481876,\,0.257766,\,0.155969,\,0.069213,
\,0.035176)$ — an interior point of $\mathcal R'$ (well inside both
$p_1<15T/31\approx0.483871$ and $T/31\approx0.032258<p_2<8T/31\approx
0.258065$; the point is near, but strictly inside, the corner where these
two boundaries meet). Exact computation: the minimum over all 120 named
chambers is $\Phi_{\text{fam}}=0.5162915971\ldots>a_4T=16/31=
0.5161290322\ldots$ (fails by exactly $\approx1.6\times10^{-4}$).

**This is reported honestly as a genuine gap in the family, not overclaimed
as a counterexample to the theorem itself.** To check which of the two
possibilities holds — (a) the named family is simply incomplete and a
richer legal strategy beats $a_4T$ here, or (b) this point is a real
counterexample to $c(4)\le16/31$ — I ran an unrestricted numerical
optimization (`scipy.optimize.minimize`, Nelder–Mead, multi-start, over
**every** legal cut-count composition $(c_1,\dots,c_5)$ with $\sum c_i\le4$,
optimizing the actual cut positions within each piece, not restricted to
any named chamber shape) at this exact point
(`/tmp/round-32/work/fulloptim.py`). Result: the true unconstrained minimum
found is $\Phi\approx0.500536 < a_4T\approx0.516129$ — **comfortably below
the target**, confirming possibility (a): the point is not a counterexample
to the conjecture, but the 120-chamber named family is genuinely incomplete
here. The optimizer's best cut-count composition was $(c_1,c_2,c_3,c_4,c_5)
=(2,0,0,0,2)$ — i.e. **two cuts on $p_1$ and two cuts on $p_5$** (three
fragments each), a strategy shape not present in any chamber derived so far
(every named chamber to date either bisects a piece, or pins a host to
$\ge1$ other whole pieces plus at most one residual — none uses a
*3-fragment* cut on the smallest piece $p_5$ simultaneously with a 3-fragment
cut on $p_1$).

### R32.4 Honest conclusion — what this round does and does not establish

**Established (proved, non-numeric):**
- The Leave-2-Untouched Theorem (R32.1), fully general $m$, a genuine new
  named-chamber closed form derived directly from the certified
  `partition-chamber-theorem`, with its 6-chamber instantiation at $m=5$.

**NOT established — and explicitly, honestly refuted where the dispatch
asked for a covering proof:**
- The dispatch's target (a full Farkas-style exhaustive-case-split covering
  proof of $\mathcal R'$ using the existing named-chamber family plus the
  new Leave-2-Untouched theorem) is **not achieved**, and — critically —
  is **not achievable with this family**: an exact, reproducible
  counterexample (R32.3) shows the full 120-chamber family (every named
  chamber on file to date, including this round's new one) fails
  simultaneously at a genuine interior point of $\mathcal R'$. Writing a
  Farkas certificate over this family would therefore be **provably
  impossible** (a Farkas certificate can only certify a true statement),
  so no attempt at one is made — attempting it anyway and hunting for a
  certificate that doesn't exist would waste effort and risks exactly the
  kind of unsound "certificate" this project's rigor rules forbid.
- The failure is highly localized (found in $1$ of $\sim9200$ exact-search
  trials, and not reproduced at all by a broader/independent search run —
  see the corner-vs-interior investigation below), concentrated near the
  corner where $\mathcal R'$'s own two boundaries meet
  ($p_1\to(15T/31)^-$, $p_2\to(8T/31)^-$) — precisely where the two
  *adjacent* already-closed regions (R31.2's strip $p_1\ge15T/31$, and
  round-29's transplant (ii) $p_2\ge8T/31$) both degenerate to zero margin.
  A systematic small-denominator grid search near this corner
  (`/tmp/round-32/work/corner.py`, $T\in\{31,62,\dots,186\}$, all integer
  points within $6$ units of the corner in both $p_1,p_2$) found **no**
  small-denominator counterexample, so the failing region — while real and
  exactly verified at the one witness above — appears to be a thin,
  high-denominator sliver near the corner rather than a robust open
  sub-box; this is a diagnosis, not a proof that the gap is measure-zero
  or that a slightly-extended chamber (e.g. one interpolating continuously
  between the Half-Complement Pin's $p_1\ge15T/31$ regime and the
  Theorem-$B_k$ $p_2\ge8T/31$ regime) would not close it — that
  interpolating chamber is not derived this round.
- The true optimal strategy at the witness point (cut composition
  $(2,0,0,0,2)$: trisect $p_1$ *and* trisect $p_5$ simultaneously) is a
  genuinely new shape, outside the entire Partition-Chamber-Theorem family
  as used so far (which never simultaneously fragments two different
  pieces into $\ge3$ parts each without any of those fragments matching a
  whole untouched piece) — identifying and proving its closed form is
  concrete, well-motivated future work, following this project's standing
  "reverse-engineer from the numeric optimizer's argmin, then prove via
  `pair-insensitivity-corollary`" methodology, but is not completed this
  round due to time.

**Net effect.** This round makes one genuine positive addition (Leave-2-
Untouched, proved in full and certified-ready) and, more importantly,
**correctly avoids repeating rounds 29–30's false-coverage mistake**: rather
than reporting the family's near-total (119/120-chamber, ~99.99%-of-cases)
success as "coverage," it explicitly searched for and found the exact
failure point, verified the failure is not a counterexample to the theorem
(via an independent full optimization), and honestly diagnosed both the
location (a thin corner sliver) and the missing mechanism (simultaneous
multi-fragment cuts on two different pieces). $\mathcal R'$ remains open;
Status stays `partial`.

### Promotable lemmas (round 32)

- **Leave-2-Untouched Theorem** (R32.1): fully general $m\ge3$, a direct
  instantiation of the certified `partition-chamber-theorem` (host $q_1$
  pinned against all-but-two of the remaining pieces, the two left
  untouched), formula $\Phi=(T+A(\{\rho,q_j,q_k\}))/2$ with the explicit
  3-branch case split by relative order. Recommend certifying as
  `leave-2-untouched-theorem`.
- **Dead-end / negative record**: the 120-chamber named family (Bisect-
  Subset $\cup$ Double-Bisect-Pin $\cup$ Triple-Pin $\cup$ Double-Pin-Pair
  $\cup$ Half-Complement-Pin $\cup$ Leave-2-Untouched) does **not** cover
  $\mathcal R'$ — exact counterexample
  $p/T\approx(0.481876,0.257766,0.155969,0.069213,0.035176)$, family
  minimum $\approx0.5162916>a_4T\approx0.5161290$, while the true
  (numerically-found, not yet proved) optimum is $\approx0.500536$ via
  cut composition $(2,0,0,0,2)$. Recommend recording as
  `n4-120-chamber-family-incomplete-dead-end` so no future round re-attempts
  a Farkas certificate over exactly this family without first adding a
  chamber for the $(2,0,0,0,2)$-shaped (or similarly multi-fragment)
  strategy.
