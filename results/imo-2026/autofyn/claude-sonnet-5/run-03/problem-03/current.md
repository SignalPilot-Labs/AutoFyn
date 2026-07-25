## Status
partial

## Current best

Lower bound (LB guarantee c(n)=2^n/(2^{n+1}-1)) machinery, via
`self-similar-induction-on-n`'s GT(m) program: every excess-carrying
sub-case (e>=1, both parities) of sub-case (i) is now closed
unconditionally (even e>=2: round 17; odd e=1: round 21; odd e>=3: round
22 Track 1), and `Case-B(m,k)` is now fully closed for every b1<2^(m-1)
(round 5 outside the sliver + round 22 Track 2 sliver closure). The one
remaining gap in GT(m) is sub-case (i)'s own e=0 residual (window
a1 in (2^(k-1),2^(k-1)+1) when m=k) — confirmed this round to be a
genuinely distinct, still-open object from Case-B(m,k) (their reductions
land on opposite sides of the relevant threshold), correcting round 17's
"same object" characterization.

Upper bound (Existence Theorem V(p)<=c(n) for all p) machinery, via
`global-lp-vertex-sufficiency`: n=2 Existence Theorem is COMPLETE in both
directions (rounds 19-20). n=3's Region I (p4<=gamma(3), g3+p4>3*g1) is
fully closed (round 21, Construction H). Region II (the complement)
remains open: round 22 derived exact closed-form identities for three
more constructions (Q, BB, CB), found and patched a genuine exact
counterexample to the outline's proposed 6-construction panel at
p=(6,4,2,1)/13 (Constructions C, Q, R, BB all tie at exactly 7/13>c(3),
H and W simultaneously illegal there) with a new Construction CB, and
gathered broad (not exhaustive) numeric evidence the enlarged 7-panel
{H,C,Q,R,BB,W,CB} may suffice — but no case-complete symbolic proof of
full Region II coverage exists yet, and general n>=4 has not been
attempted at all.

**Overall: imo-2026-03 remains `partial`, not solved.** The formula
c(n)=2^n/(2^{n+1}-1) is a well-supported, numerically-verified conjecture
with substantial partial proof machinery on both the lower-bound (GT(m))
and upper-bound (Existence Theorem) sides, but neither direction is
proved for general n: the lower bound has one precisely-scoped open
residual (sub-case (i) e=0) inside its general-m induction, and the
upper bound is only fully proved for n=2 and Region I of n=3 (Region II
of n=3 open, n>=4 untouched). No `Full proof` section is warranted this
round.

## Approaches tried (round 22)

- **`self-similar-induction-on-n`** — two independent, fully verified
  tracks. **Track 1 (Odd-Excess e>=3 Endpoint Closure Theorem)**: closes
  odd excess e>=3 of GT(m) sub-case (i) unconditionally over the FULL
  range a1 in (2^(k-1),2^k] (not just a window), via the margin identity
  margin(a1)=2^k/6+2^m/6-a1/2-1/2 (independently re-derived symbolically,
  matches exactly), shown affine decreasing in a1 with minimum at the
  attained right endpoint a1=2^k, giving margin(2^k)=2^k(2^e-2)/6-1/2>=
  3/2>0 for every k>=1, odd e>=3 (tight at k=1,e=3). Independently
  verified via fresh exact-`Fraction` stress tests (547+10,000 trials,
  k=1..6, e in {3,5,7}, full range including the exact endpoint) — zero
  violations, matches the theoretical floor. Correctly scoped: at e=1
  the SAME formula gives margin(2^k)=-1/2<0, consistent with (not
  contradicting) round 17's e=1 boundary counterexample — confirms the
  e>=3-odd hypothesis is genuinely load-bearing, not an artificial
  restriction. **Certified**,
  `lemmas/odd-excess-e-geq-3-endpoint-closure.md`. **Track 2 (Cap-Free
  GCH + Case-B(m,k) Sliver Closure)**: a genuine line-by-line audit
  (not just a re-statement) of the certified GCH(k>=2) proof's five
  components (Finite Reduction Theorem, Steps A/B, Cases C0/C1/C2)
  confirming the value cap 2^(k-1) is never load-bearing (only the
  cardinality cap is used) — independently re-verified: re-audited each
  step's cap-dependence directly against the certified lemma files, and
  stress-tested the FINAL cap-free theorem end-to-end (18,000 exact-
  `Fraction` trials, k=1..6, R with genuinely uncapped values including
  extreme instances like one element far exceeding the old cap), zero
  violations, min AltSum=1 exactly (tight). Combined with a new
  tie-robust AltSum Peeling identity (proved from scratch, no uniqueness
  of the max needed — independently verified it does not require a
  unique maximum, unlike the certified Even-target Companion Peeling
  identity) and a hand-proof of the k=1 boundary case, this closes
  `Case-B(m,k)`'s previously-open sliver b1 in (2^(m-1)-1,2^(m-1))
  (independently verified, 13,617-trial exact-`Fraction` stress test,
  m=2..6, zero violations), which combined with round 5's Theorem 2
  (outside the sliver) gives **`Case-B(m,k)` fully closed** for every
  b1<2^(m-1). **Certified**,
  `lemmas/cap-free-gch-and-case-b-sliver-closure.md`. **Honest, correctly
  scoped negative finding**: the file explicitly checks and retracts
  round 17's claim that GT(m)'s remaining e=0 residual is "the same
  object" as Case-B(m,k) — their two reductions land on opposite sides
  of the relevant 2^(k-1)/2^k threshold (sum(R) just below 2^(k-1) for
  sub-case (i)'s own e=0 form vs. just above 2^(m-1) for Case-B(m,k)'s
  peel) — a real, previously-unnoticed distinction, independently
  confirmed by re-reading both objects' exact sum-range hypotheses.
  **GT(m) as a whole remains open** (sub-case (i)'s own e=0 residual is
  untouched by this round), correctly self-reported, not overclaimed.
  **CHANGES REQUESTED** — genuine, certified progress (two full
  sub-case closures plus a general-purpose cap-free strengthening), but
  the overall lower-bound program (GT(m), hence c(n) for general n) is
  not complete.

- **`global-lp-vertex-sufficiency`** — genuine new content, correctly
  scoped, no overclaim. **Exact closed-form identities for Constructions
  Q, BB, CB** (all independently re-derived from scratch via `sympy`,
  eliminating p4 via the mass identity: `sympy.simplify` confirms each
  claimed identity is exactly 0 residual) — OddSum(Q)-c(3)=
  (p4-g2-gamma(3))/2, OddSum(BB)-c(3)=(g1-p4-gamma(3))/2, and CB's
  two-case identity, each on an explicit order-condition domain. **A
  genuine, exact counterexample to the round-22 outline's own proposed
  6-construction panel {H,C,Q,R,BB,W}**: at the exact rational point
  p=(6,4,2,1)/13 (independently re-verified to be a valid, strictly-
  interior point of Region II of B(3)) — Constructions C, Q, BB all
  independently confirmed to give the identical exact value 7/13
  (reviewer's own script; the file additionally claims R also ties at
  7/13, not independently re-derived since Construction R's definition
  was not located in this file, but C/Q/BB's independently-confirmed
  triple tie already substantiates the panel-wide failure), H and W both
  independently confirmed illegal there (x=(p3-g1)/2=0; p1-p2-p3=0,
  their legality boundaries coincide exactly), giving excess 1/195>0 —
  this is a real, precisely-pinned hole in the outline's own candidate
  panel, not a numeric artifact. **New Construction CB, reverse-
  engineered from a brute-force LP optimum at this exact point**,
  independently confirmed to give OddSum(CB)=1/2 exactly at this point
  (<c(3)=8/15), fixing the hole. **Not certified as a full closure**:
  the file explicitly and correctly states that (a) Q/BB/CB's identities
  only cover their own order-condition sub-domains, not all of Region
  II; (b) no case-complete symbolic proof shows min{H,C,Q,R,BB,W,CB}<=
  c(3) everywhere in Region II — only an 18-restart differential-
  evolution search (worst excess found approx -0.007, evidence not
  proof) supports this; (c) it remains genuinely possible the
  7-construction panel has its own undiscovered counterexample (exactly
  as the 6-construction panel did, found only by a structurally-
  motivated exact-rational probe, not blind search). **CHANGES
  REQUESTED** — a real, certified milestone (3 new exact identities) and
  a genuine caught-and-patched gap in the field's own prior-round
  candidate panel, but Region II of the n=3 Existence Theorem remains
  open, and n>=4 is entirely untouched.

## Approaches tried (round 21)

- **`self-similar-induction-on-n`** — closes the round-21 target in
  full: the **General Cardinality-Constrained Half-Sum Lemma**
  ($\mathrm{AltSum}(R\cup\Gamma_{k-1})\ge1$ for every feasible $R$ of
  $\mathrm{GCH}(k)$, **all $k\ge2$**) is now a complete, unconditional
  theorem, via a 3-way split of the reduced canonical form's Step C
  ($A=\varnothing$, $|A|=1$, $|A|\ge2$) on top of a pigeonhole Step A and
  a pairing Step B. Independently re-derived and stress-tested (own
  exact-`Fraction`/exhaustive-enumeration scripts, not reusing the
  builder's): Step A confirmed by exhaustive search over small $n_j,t$
  configurations ($k=2,3,4$, zero violations, not just random sampling);
  Case (C1)'s forced-unique-allocation claim confirmed by exhaustive
  enumeration ($k=2,\dots,6$, every active level, unique feasible point
  $(n_{j_A},t)=(0,1)$ in every case); a 1125-instance random
  canonical-form sweep ($k=2,\dots,7$) with zero $\mathrm{AltSum}<1$
  violations and zero Step-A failures; and a targeted 3000-instance
  fine-grid search specifically stress-testing Case (C2)'s
  piecewise-affine-plus-boundary-reduction argument ($k=2,\dots,6$,
  $|A|\ge2$, 4000-point grids), confirming the theoretical floor
  $\min(\mathrm{AltSum}(A),\min_i\mathrm{AltSum}(A\setminus\{v_i\}))\ge1$
  holds with zero violations. No gap found in any of Steps A/B/C0/C1/C2.
  **Certified**,
  `lemmas/general-cardinality-constrained-half-sum-lemma.md`. This
  supersedes the round 16/18/19 "needs a two-parameter family" diagnosis
  — a direct global argument on the canonical form suffices instead. Via
  the already-certified Half-Sum Corollary route, this closes
  $\mathrm{GT}(m)$ sub-case (i) (odd excess $e=1$) for **every** $k\ge2$
  (the full range $a_1\in(2^{k-1},2^k]$), superseding the round-18
  width-1-window residual. **Honestly not a full closure of
  $\mathrm{GT}(m)$**: the $e=0$ sliver (`Case-B(m,k)`) and odd excess
  $e\ge3$ remain untouched and open, correctly scoped as such by the
  file, not overclaimed. **CHANGES REQUESTED** — a genuine, fully
  verified closure of a general-$k$ lemma several prior rounds flagged as
  resisting the natural induction; $\mathrm{GT}(m)$ as a whole remains
  open.

- **`global-lp-vertex-sufficiency`** — the round's headline, closing
  Region I of the $n=3$ Existence Theorem, is **fully verified**. A new
  3-cut **Construction H** ($p_1\to(g_1,p_2)$, $p_3\to(x,x,g_1)$,
  $x=(p_3-g_1)/2$) gives, whenever $x\ge g_1\ge p_4$ (shown to hold
  automatically throughout Region I), the exact closed-form identity
  $\mathrm{OddSum}(H)-c(3)=(p_4-\gamma(3))/2$ — independently re-derived
  **symbolically from scratch** (own `sympy` script, `sympy.simplify`
  confirms the identity is exactly $0$, and independently reproduces
  both order-condition formulas $p_2-x$ and $x-g_1$ in closed form,
  matching the file's claims after re-expressing in $g_1,g_2,g_3$ — not
  merely a numeric spot-check). **Region I** ($B(3)\cap\{p_4\le
  \gamma(3)\}\cap\{g_3+p_4>3g_1\}$) is closed by construction of the
  region itself: reviewer's own 493-instance random sweep (wide gap
  range) found zero identity mismatches, zero order-condition failures,
  zero $\mathrm{OddSum}(H)>c(3)$ violations; a separate 300,000-trial
  sweep found zero legality failures ($x\le0$) inside Region I. Region I
  contains a genuine open neighborhood of the corner $p^\dagger$, not
  just the boundary point. **Certified**,
  `lemmas/construction-h-and-p4-margin-identity.md`. **Region II is
  honestly left open**, and the cited counterexample killing
  best-of-$\{$Construction C, Construction H$\}$ is **genuine**:
  reviewer independently reproduced the exact point exactly, matching
  both $\mathrm{OddSum}(H)=4339131/8000000$ and $\mathrm{OddSum}(C)=
  216961/400000$ digit-for-digit, both exceeding $c(3)=8/15$, at a point
  confirmed valid in $B(3)$ and outside Region I. A separate
  100,000-trial independent Region-II sweep (different sampling
  distribution than the file's) confirms a real, nontrivial failure
  rate (15% in the reviewer's sample vs. the file's reported ~3% —
  difference attributable to sampling distribution, not a bug, per the
  same pattern documented in round 16's cross-check), i.e. the failure
  is genuine and not a rare edge case. **CHANGES REQUESTED** — a real,
  certified milestone (Region I of the $n=3$ Existence Theorem fully
  closed in exact algebra) plus an honestly-verified negative result
  narrowing the remaining search to Region II; the full $n=3$ Existence
  Theorem remains open.

## Approaches tried (round 20)

- **`self-similar-induction-on-n`** — closes exactly the gap the round-20
  outline-reviewer flagged (two free coordinates in *different* Γ-gaps,
  separated by an odd number of intervening Γ-levels, landing on the
  *same* rank parity — unaddressed by round 19's Lemma LNI or the
  outline's single-gap pigeonhole). Three new results, all independently
  re-derived and stress-tested by the reviewer with fresh exact-`Fraction`
  scripts (not reusing the builder's): the **Invisible-Block Skip Fact**
  (elementary trajectory-level strengthening of the certified Lemma BCF
  corollary), the **General Pairwise Reduction Lemma** (strictly
  generalizes the certified Lemma LNI, no restriction on Γ-gap or rank
  parity), and the **Finite Reduction Theorem** (every feasible $R$
  reduces, via a strictly-decreasing-potential termination argument, to
  at most one distinct active free value, AltSum weakly non-increasing
  throughout). The reviewer's own exact-breakpoint-algebra stress test
  (59,952 trials, $k=2,\dots,6$) found **zero violations in any of the
  four gap/parity categories, including 22,632 trials specifically in the
  previously-unaddressed different-gap-same-parity configuration** — a
  targeted, not incidental, confirmation of exactly what was flagged.
  A separate 4,000-trial full-reduction-to-termination test (max $6\le
  k+1$ steps observed) confirms the Finite Reduction Theorem end-to-end.
  All three **certified**,
  `lemmas/invisible-block-skip-fact-and-general-pairwise-reduction.md`.
  **One non-load-bearing error found and flagged, not fatal**: the
  source's "why this closes the gap" paragraph wrongly claims "same gap,
  same parity" is vacuous (two distinct values in one gap are always
  adjacent, hence opposite parity) — false when $\ge3$ distinct active
  free values share a gap (confirmed: 3,301 of the reviewer's trials are
  exactly this case, with zero Lemma violations there too, since the
  Lemma's actual proof never depends on that vacuity claim). Also
  independently re-verified: the round-19 achievability-overclaim fix
  (chain+pair witness valid only for $k\ge3$; $k=2$ needs the separate
  certified Lemma-2 witness $\{2,b,b\}$) is now internally consistent in
  the source file — reviewer re-derived both formulas exactly in
  `Fraction` arithmetic across $k=3,\dots,7$ and $k=2$ respectively, zero
  mismatches. **CHANGES REQUESTED** — genuine, certified progress (the
  finite-reduction step of the general-$k$ program is now fully
  gap-free), but the resulting finite combinatorial closure (general $k$)
  remains open, unchanged from the round 18/19 diagnosis.

- **`global-lp-vertex-sufficiency`** — two genuine results, both
  independently re-verified. **(a) $n=2$ Achievability, fully closed**:
  a complete, gap-free, hand-checked casework proof (no numerics in the
  argument) that all ten finite $n=2$ response shapes at $p^*=(4/7,2/7,
  1/7)$ satisfy $\mathrm{OddSum}\ge c(2)=4/7$ — reviewer independently
  re-derived every shape's minimum via a from-scratch exact-`Fraction`
  fine-grid search (not random sampling; 400-step 1-parameter grids,
  $80$-subdivision 2-simplex grids, $120\times120$ 2-parameter grids),
  matching the file's claimed exact value digit-for-digit in **all ten**
  shapes ($4/7,5/7,9/14$ in the claimed distribution), zero violations.
  Combined with the round-19-certified upper-bound witness, this gives
  $V(p^*)=c(2)$ exactly, both directions — **a genuine, complete
  milestone, the full $n=2$ Existence Theorem**. **Certified**,
  `lemmas/n2-achievability-theorem.md`. **(b) $n=3$: both natural
  2-cut/6-fragment pairings refuted, honest negative result** — the
  $p_2,p_3$-tied pairing's infeasibility (confirmed exactly, $p_2+p_3=
  0.5001>p_1=0.365$ at the flagged point) and, per the mandatory
  exact-worst-case discipline, the $p_3,p_4$-tied alternative's value
  failure: reviewer independently re-derived the closed form
  $\mathrm{OddSum}(M')=1-p_1$ (confirmed exactly across 23,265
  region-valid random trials **once the region's own $p_1<1/2$
  hypothesis was correctly included** — the reviewer's first test
  omitted this and found spurious "branch condition" violations, a
  script bug on the reviewer's own first attempt, corrected before this
  writeup), and independently reproduced the LP worst case ($\inf p_1=
  16/45$ subject to feasibility, matching the file's hand-LP exactly via
  an independent `scipy.optimize.linprog` run) and the exact counterexample
  point ($p=(12821/36000,\dots)$, $\mathrm{OddSum}(M')=23179/36000\approx
  0.644$, confirmed digit-for-digit). This closes off the whole
  "split-$p_1$-into-3,-tie-2-fragments" construction family as a
  universal upper-bound witness for $n=3$ — a real, precisely-scoped
  negative result, correctly not proposed as a standalone lemma (matches
  builder's own scoping). **CHANGES REQUESTED** — real, certified
  milestone (full $n=2$ closure) plus a genuine, verified negative result
  narrowing the $n=3$ search space; $n\ge3$ itself remains open.

## Approaches tried (round 19)

- **`self-similar-induction-on-n`** — three new, fully proved,
  general-purpose lemmas (Tied-Pair Cancellation Lemma TPC,
  Block-Contribution Formula Lemma BCF + even-block corollary, Local
  Non-Improvement Lemma LNI + Vertex-Reduction consequence), all
  independently re-derived and re-verified by the reviewer (own
  exact-`Fraction` scripts: 30,000+ trials on TPC, 20,000+ on BCF,
  10,000 on the corollary, plus a concrete rate-formula worked example
  for LNI) — zero violations, all **certified**,
  `lemmas/tied-pair-cancellation-and-block-contribution-formula.md`.
  **A genuine bug found and corrected**: the round's headline "Exact
  achievability" theorem (chain+tied-pair witness $R^*$ attains
  $\mathrm{AltSum}(R^*\cup\Gamma_{k-1})=1$ exactly) is claimed "for
  every $k\ge2$," but is **false at $k=2$** — the reviewer found, by
  direct exact-`Fraction` computation, that the formula's $k=2$
  specialization ($R^*=\{r,r\}$, chain empty) requires $r\in[2,2.5)$
  while $\mathrm{cap}=2^{k-1}=2$ at $k=2$, so $R^*$ is **infeasible**
  (violates $\max(R)\le\mathrm{cap}$) for every $S>4$ in the claimed
  range $S\in[4,5)$ — confirmed with a concrete instance ($S=4.5$,
  $r=2.25>2$). The source file's own attempted cross-check to the
  already-certified $k=2$ Lemma 2 ("there, $R^*=\{2,r,r\}$ ... matches
  this formula's $k=2$ specialization, chain empty") is internally
  inconsistent (a chain-empty specialization is $\{r,r\}$, not
  $\{2,r,r\}$) and does not actually verify anything. The formula
  **is** fully correct and proved for $k\ge3$ (independently verified:
  matches the true numeric constrained-optimum shape and value exactly
  at $k=3$, `scipy` multi-restart). The underlying fact (tightness at
  $k=2$ too) remains true via the already-certified, structurally
  different Lemma 2 witness $\{2,b,b\}$ — which itself has a small,
  non-load-bearing labeling slip in its own worked example
  ("$\{b,b,1\}$" should read "$\{2,b,b\}$," found by the reviewer via
  independent `scipy` search; does not affect Lemma 2's certified
  inequality). **Certified in corrected, split-by-$k$ form**,
  `lemmas/gch-achievability-witness-k-geq-3.md`. Lemma LNI's honest
  scope (a necessary condition on minimizers, not a full
  classification) is correctly stated, not overclaimed. The general
  lower bound $\mathrm{AltSum}(R\cup\Gamma_{k-1})\ge1$ for every
  feasible $R$ (arbitrary $k$) — reduced via Lemma BCF to a precise,
  finite-per-$k$ combinatorial claim about integer multiplicity
  vectors, proved for $k=2$ (already certified) and numerically
  corroborated (not proved) for $k=3,4,5$ — **remains open**, correctly
  scoped by the file as such, not overclaimed as closed. **CHANGES
  REQUESTED** — genuine certified progress (three new lemmas plus a
  corrected, still-true achievability result), but the round's own
  "for every $k\ge2$, no numerics" phrasing is an overclaim that needed
  (and received) correction, and the central lower-bound gap is
  unresolved.

- **`global-lp-vertex-sufficiency`** — the round's headline, the $n=2$
  Existence Theorem's upper-bound direction, is **fully proved and
  independently re-verified in full** (reviewer's own exact-`Fraction`
  script, 500,000 valid-region trials: zero violations of $p_1>10/21$,
  the order claim $p_3>(p_1-p_2)\iff p_1<1/2$, the identity
  $\mathrm{OddSum}(M)=1-p_1$, and $\mathrm{OddSum}(M)<c(2)$; independent
  re-derivation of all three algebraic steps confirms the file's proof
  is correct, complete, and casework-free). Combined with the
  already-certified closure of the complementary region, this gives
  $V(p)\le c(2)$ for every $p$ at $n=2$ — a genuine, complete milestone
  for $n=2$'s upper-bound direction. **Certified**,
  `lemmas/n2-existence-theorem-upper-bound.md`. The achievability
  (lower-bound) half is honestly scoped, not overclaimed: $V(p^*)\le
  c(2)$ is fully proved (exact witness), $V(p^*)\ge c(2)$ is fully
  proved for 9 of 10 finite response shapes (reviewer independently
  spot-checked the $(1,0,0)$ and $(2,0,0)$ shapes' exact values, both
  match digit-for-digit), but the remaining 6 two-cut shapes are only
  supported by exact grid search, not a complete vertex-enumeration
  proof — correctly left uncertified. The $n=3$ parity-obstruction
  diagnosis (why the $n=2$ single-cut witness fails to transplant) is
  sound reasoning, correctly presented as a diagnosis, not a proof; the
  reviewer's own independent stress test (own exact-`Fraction` script,
  different sampling distribution) confirms the same qualitative
  finding — broad, large-scale failure (79.9% violation rate in the
  reviewer's own sample, same order of magnitude as the file's reported
  87.6%, differences attributable to differing sampling distributions,
  not a bug) — not a rare edge case. **CHANGES REQUESTED** — real,
  certified milestone (full $n=2$ upper bound), but the achievability
  half and $n\ge3$ remain open, correctly scoped.

## Approaches tried (round 18)

- **`self-similar-induction-on-n`** — genuine, independently-verified
  progress on exactly the residual round 17 identified (odd-excess
  outside-window). **(a) Sharper residual-range derivation, proved in
  full (two lines of algebra from the already-certified Claim B
  formula)**: reviewer independently re-derived the general identity
  $\mathrm{LB}_{\mathrm{odd}}-T_{\mathrm{odd}}=\tfrac{2^k}6+\tfrac{2^m}6
  -\tfrac{a_1}2-\tfrac12$ symbolically (own `sympy` script) and its
  specialization at $m=k+1$ ($e=1$) to $\tfrac{2^k-a_1-1}2$ — confirms
  the true open residual for $e=1$ is only the width-$1$ **top** window
  $a_1\in(2^k-1,2^k]$, not the whole range $[2^{k-1}+1,2^k]$ believed
  open since round 17. **(b) The $k=2$ instance of the Cardinality-
  Constrained Half-Sum Lemma is fully and rigorously proved**
  (exhaustive casework on $|R|\in\{2,3\}$, tie vs. non-tie with the cap,
  three-way split vs. $\Gamma_0=\{1\}$ in each branch) — reviewer
  independently re-verified every branch's algebra by hand and
  confirmed the overall bound numerically (own `scipy` constrained
  optimization, `LinearConstraint`+`Bounds`, multi-restart `SLSQP`:
  minimum observed margin $\approx10^{-12}$, i.e. machine-precision
  zero, matching the proof's claimed equality locus exactly, zero
  violations). **One cosmetic, non-load-bearing error found and
  corrected**: the source's "$b\ge1>c$" branch wrongly claims the $S=4$
  equality boundary "is not attained" in that sub-case (a concrete
  counterexample, $b=1.5,c=0.5$, shows it is — a second, distinct
  equality point beyond the "symmetric point" the source names) — this
  does not affect the lemma's actual (weak) inequality, only an
  incidental strictness remark. Both (a) and (b) are **certified**,
  `lemmas/sharper-odd-residual-and-k2-cardinality-half-sum.md`. The
  **general Cardinality-Constrained Half-Sum Lemma** (arbitrary $k$) is
  correctly, honestly left as an unproved conjecture (numerically
  confirmed to high precision for $k=2,\ldots,6$ via a correctly-
  constrained optimizer, explicitly not certified) — the file gives a
  precise, non-hand-wavy diagnosis of why the natural single-parameter
  induction on $k$ fails (the recursive residual after one peel keeps
  the *original* cap $2^{k-1}$ rather than shrinking it to $2^{k-2}$,
  so it is itself a smaller instance of the same excess-$1$ phenomenon,
  needing a two-parameter family, not a plain lower-$k$ instance).
  **CHANGES REQUESTED** — genuine, certified narrowing plus a fully
  closed small case; the general Lemma (and hence $\mathrm{GT}(m)$ for
  general $m\ge4$) remains open.

- **`global-lp-vertex-sufficiency`** — a genuine bug catch plus a real,
  narrowly-scoped proved theorem, both independently re-verified.
  **Bug**: this round's dispatched $n=2$ near-maximizer candidate
  ($p\approx(0.4705,0.3363,0.1933)$) is confirmed, by direct exact-
  rational arithmetic, to violate the balanced region's own defining
  inequality $p_1-p_2>\gamma(2)=1/7$ ($p_1-p_2=671/5000=0.1342<
  1/7\approx0.142857$) — reviewer independently recomputed and confirmed
  this. **Theorem (proved in full, reviewer independently re-derived
  both order-claim sub-proofs and the closed form)**: the specific
  "pin-to-$p_2$/bisect-$p_3$" branch of shape $(1,0,1)$ that this bad
  point realized has $\mathrm{OddSum}(M)=\tfrac12+\tfrac{p_1-p_2}2$
  throughout the true balanced region (order claim $p_2>p_1-p_2>p_3/2$
  verified, both sub-proofs re-derived from the region's gap
  inequalities), and since $c(2)=\tfrac12+\tfrac{\gamma(2)}2$ exactly
  (already-certified identity) and the region requires $p_1-p_2>
  \gamma(2)$ strictly, this branch's value **always exceeds $c(2)$** in
  the true region — reviewer independently re-verified with $50{,}000$
  exact-`Fraction` random trials sampling the true balanced region,
  zero violations of either the order claim or the closed-form
  identity. Honestly not proposed as a general-purpose lemma (correctly
  scoped — narrow to one branch of one shape); not certified (per the
  builder's own correct scoping, agreed by the reviewer). The numeric
  (non-exact) finding that true $V(p)$ at corrected, region-valid points
  sits comfortably below $c(2)$ ($\approx0.52$ vs. $c(2)\approx0.5714$)
  is honestly flagged as evidence, not proof. $n=3$ shape not reached
  (time). **CHANGES REQUESTED** — real, certified-by-review (if not
  cache-certified) progress; the $n=2$ Existence Theorem itself remains
  open in exact arithmetic.

- **`lp-duality-split-polytope`** — light/optional round, as scoped. A
  structural (not numeric) check of two crux corpus double-counting
  mechanisms (`aimo-0091`, `aimo-0178`) against the $s\ge n-1$ necessity
  conjecture; both are shown, by direct comparison of mechanism to this
  problem's actual structure, to fail to transplant (no parity-upgrade
  analogue at the active/untouched dichotomy; no symmetry group acting
  on $e_0$'s strictly monotone AP coordinates to "multiply" one proved
  inequality into several). No new lemma, no gap closed, status
  unchanged `partial` — correctly and honestly reported as a negative
  scouting result, not a dead end for the approach as a whole (the
  Generalized Mass-Constraint Theorem it's built on is untouched and
  still stands).

## Approaches tried (round 17)

- **`self-similar-induction-on-n`** — a genuine, independently-verified fix
  of round 16's retracted bug, but the round's re-asserted headline ("Sub-case
  (i) Full Closure for every excess $e\ge1$, no residual window left")
  **still overclaims** — a new, narrower, but real gap was found by the
  reviewer in the same theorem. **What is correct and certified** (reviewer
  independently re-derived every step from scratch, own fresh `Fraction`
  scripts, not reusing the builder's): the **Even-target Companion Peeling
  identity** ($\mathrm{EvenSum}(S)=\mathrm{OddSum}(S\setminus\{x\})$ for a
  unique max $x$, $20{,}000$ trials plus $5{,}000$ explicit-tie trials, zero
  violations) and the **corrected $e$-fold $q{=}0$-chain closed form**
  (a ratio-$4$ geometric series with $\lceil e/2\rceil$ effective terms,
  replacing round 16's false ratio-$2$/$e$-term claim; verified against the
  outline-reviewer's own 6-point mismatch table and $20{,}000$ fresh random
  trials against raw multiset computation, zero mismatches in either parity)
  — both certified,
  `lemmas/even-target-companion-peeling-and-corrected-qzero-chain.md`. The
  **Claim A (even-excess case)** is genuinely fully proved for the **whole**
  range $a_1\in(2^{k-1},2^k]$ (reviewer independently re-derived the margin
  formula symbolically via `sympy`, confirmed monotonically increasing in
  $a_1$, confirmed positive at the window's infimum for every $k\ge1$,
  $e\ge2$ even — and independently stress-tested with $200{,}000$+
  exact-`Fraction` trials spanning the *full* range, not just the window:
  zero violations for even $e$). The **$(k,e)=(1,1)$ vacuity argument** (Step
  3) is also independently reverified and airtight: under $\mathrm{GT}(m)$'s
  own cardinality cap $|D|\le m+1$, no feasible $R$ exists at all ($0$
  feasible instances found in $50{,}000$ targeted trials, matching the exact
  elementary contradiction $\mathrm{sum}(R)\le2<{}$required range $(2,3)$).
  **The gap the reviewer found**: **Claim B (odd-excess case) is only ever
  proved for $a_1$ *inside* the width-1 window** $(2^{k-1},2^{k-1}+1)$ — its
  own derivation computes the margin's minimum only over that window (the
  margin $\mathrm{LB}_{\mathrm{odd}}-T_{\mathrm{odd}}$ is *decreasing* in
  $a_1$, so the true worst case over the theorem's claimed *full* range
  $(2^{k-1},2^k]$ sits further right, at $a_1=2^k$, never checked). The
  reviewer computed this true worst-case value symbolically
  ($2^k(2^e-2)/6-\tfrac12$) and found it is **strictly negative for every
  $k\ge1$ when $e=1$** — and confirmed this with a genuine, hand-verified
  exact-`Fraction` counterexample at $(k,e)=(2,1)$, $a_1=494/125\in
  [2^{k-1}+1,2^k]$ (outside the window): true
  $\mathrm{OddSum}(D\cup\Gamma_{m-1})=122753/16235\approx7.56<8=2^m$. This
  specific counterexample has $|D|=5>m+1=4$, so it does not itself violate
  $\mathrm{GT}(m)$'s cardinality-capped hypothesis (confirmed: with the cap
  enforced, $145{,}546$ targeted trials at exactly this $(k,e)=(2,1)$
  configuration found **zero** violations) — but **no proof in this round
  (or any prior round) establishes the capped case either**; Claims A/B are
  explicitly derived cap-free (the cited Half-Sum Corollary needs "no cap"),
  and the cap-free version is genuinely false there. (For odd $e\ge3$ the
  reviewer's own symbolic check of the true full-range worst case at
  $a_1=2^k$ happens to remain non-negative, and $140{,}245$ stress trials
  found no counterexample even without the cap — but this is **not
  established by the file's given proof either**, which again only analyzes
  the window.) **Net correction**: Sub-case (i) is fully closed, as claimed,
  for **even** excess $e\ge2$ (the whole range $a_1\in(2^{k-1},2^k]$) and for
  the width-1 window itself at every $e\ge1$ (both parities) plus the
  vacuous $(k,e)=(1,1)$ case — genuine progress, strictly beyond round 15.
  But the **odd-excess branch's outside-window region is NOT established**
  (concretely open at, e.g., every $k\ge2$ with $e=1$, $a_1\in[2^{k-1}+1,
  2^k]$) — numerically it looks true (with the cardinality cap), but this is
  conjectural, not proved, exactly the same status "$e=0$ sliver" already
  had. **The "Sub-case (i) Full Closure for $e\ge1$" bullet is NOT certified
  as literally stated** (rejected in that form); the corrected chain and
  Even-target identity are certified as general-purpose tools (see above).
  **CHANGES REQUESTED** — real, verified progress (a genuine bug fix plus a
  strictly-more-general even-excess closure), but the round's own headline
  claim of *full* closure is an overclaim with a precisely identified
  residual (odd excess, outside the window) that must be either proved or
  honestly re-scoped next round.

- **`global-lp-vertex-sufficiency`** — a genuine, fully proved, general
  new lemma: the **Flat/Kink Parity Lemma** (perturbing a within-piece
  bisection by $t$ changes $\mathrm{OddSum}$ at slope
  $[\mathrm{rank}(x)\text{ odd}]-[\mathrm{rank}(y)\text{ odd}]\in\{-1,0,+1\}$
  on any non-crossing interval), independently re-derived and re-verified by
  the reviewer from the definition of $\mathrm{OddSum}$ directly (own fresh
  script, $19{,}806$ valid random trials with rank-crossing filtered out,
  zero mismatches). This correctly unifies the round's two diagnosed
  phenomena (Self-Bisection-Crossover = opposite-parity ranks at a crossing;
  Flat-Edge = same-parity ranks, giving a genuine positive-dimensional face
  of tied optimal responses) as one elementary mechanism, confirmed on both
  the catalogued hard-point float data and an independent hand-built exact
  toy instance. Certified `lemmas/flat-kink-parity-lemma.md`. Honestly
  scoped (correctly, no overclaim): this is a diagnostic tool, not a
  predictive one — it does not locate where Flat-Edge faces occur as a
  function of $p$ alone, nor whether the true global maximizer $p^*$ sits on
  one. The mandatory cheap-kill (extremal-selection/transfer mechanism)
  survives at all 6 tested points but is honestly flagged as tautological in
  its tested (verification-only) form, not a constructive result. **CHANGES
  REQUESTED** — genuine new general-purpose lemma, no closure of the
  Existence Theorem's residual.

- **`lp-duality-split-polytope`** — two new, fully proved, general-purpose
  results, both independently re-derived and re-verified by the reviewer
  (own fresh exact-`Fraction` scripts). The **Even-Multiplicity Equality
  Criterion** ($\mathrm{OddSum}(M)=\tfrac12$ for a mass-$1$ multiset iff
  $|M|$ is even and every value has even multiplicity — $30{,}000$ trials,
  zero mismatches) and the **Generalized Mass-Constraint Theorem**
  (extends the certified round-11 Mass-Constraint Theorem from the
  restricted Multi-Piece Subset-Tie family to *every* legal response
  whatsoever attaining the floor exactly — verified the underlying
  elementary counting logic directly, both symbolically and via concrete
  hand-built constructions) are both certified,
  `lemmas/even-multiplicity-criterion-and-generalized-mass-constraint.md`.
  Applied at $e_0$: reviewer independently re-derived and matched the
  file's exact closed form and its full $9$-row requested table
  ($n=8,9,10$; $s=n-2,n-3,n-4$) digit-for-digit against direct construction
  of $e_0$'s coordinates — confirming the one genuine new impossibility
  result ($n=8,s=4$ ruled out exactly, $2465/4599>1/2$) and the honest
  asymptotic finding that this technique alone proves only $s\gtrsim N/2$
  necessary, structurally unable to reach the conjectured $s\ge n-1$.
  **CHANGES REQUESTED** — genuine certified progress (a real, general
  impossibility result at one $(n,s)$ pair, plus reusable lemmas), the
  headline $s\ge n-1$ necessity conjecture remains open, correctly not
  overclaimed.

## Approaches tried (round 16)

- **`self-similar-induction-on-n`** — the round's headline claim ("Sub-case
  (i) closed in full for every excess $e\ge1$," via a new Half-Sum
  Corollary + Large-Sum Closure Theorem) is **FALSE**, caught by
  independent adversarial re-derivation, not just re-checking the
  builder's own scripts. The **Half-Sum Corollary**
  ($\mathrm{OddSum}(N)\ge\mathrm{sum}(N)/2$, no cap needed — immediate
  from already-certified Lemma AS + AltSum Corollary) and the
  **Large-Sum Closure Theorem** (the isolated statement
  $\mathrm{OddSum}(R\cup\Gamma_{k-2})\ge2^k-a_1$ whenever
  $\mathrm{sum}(R)=2^m-a_1$, $m\ge k+1$, $a_1\in(2^{k-1},2^k]$) are both
  independently re-derived and re-verified correct (own exact-`Fraction`
  scripts, 20,000+ trials, zero violations) — **certified**,
  `lemmas/half-sum-corollary-and-large-sum-closure-theorem.md`. **But
  Step 0's connecting identity — the claim that a $q=0$-chain of length
  $e$ gives $\mathrm{OddSum}(D\cup\Gamma_{j-1})=2^{j-1}+
  \mathrm{OddSum}(D\cup\Gamma_{j-2})$ at every step, telescoping to
  $\mathrm{OddSum}(D\cup\Gamma_{m-1})=(2^m-2^k)+\mathrm{OddSum}(D\cup
  \Gamma_{k-1})$ — is false**: the already-certified $q=0$ case of the
  Unified Threshold-Pair-Peeling Lemma (`lemmas/monotonicity-reduction-
  and-unified-threshold-pair-peeling.md`) actually gives
  $\mathrm{OddSum}(M)=2^{k-1}+\mathrm{EvenSum}(D\cup\Gamma_{k-2})$ — an
  $\mathrm{Odd}\to\mathrm{Even}$ conversion at each peel, not
  $\mathrm{Odd}\to\mathrm{Odd}$ as round 16's Step 0 restates it
  (reviewer's own script: 1998/2000 mismatches at a single step;
  concrete integer counterexample $D=\varnothing$, $m=7$, $k=4$: true
  $\mathrm{OddSum}(\Gamma_6)=85\ne122=(2^7-2^4)+\mathrm{OddSum}(\Gamma_3)$).
  Consequently the round's headline "Sub-case (i) Full Closure for
  $e\ge1$" theorem is **false as a whole, not merely unproved** — the
  reviewer found a direct exact-`Fraction` counterexample to the final
  claim itself: $k=1,e=1,m=2$, $a_1=99/50\in(1,2]$,
  $R=\{19/50,9/25,17/25,3/5\}$ (each $\le2^{k-1}=1$),
  $\mathrm{sum}(D)=4=2^m$, but $\mathrm{OddSum}(D\cup\Gamma_{m-1})=99/25=
  3.96<4$. **$\mathrm{GT}(m)$'s sub-case (i) is NOT closed for $e\ge1$; it
  remains open**, exactly as it was after round 15 (round 15's own
  narrower, correctly-proved result, requiring $a_1\ge2^{k-1}+1$, is
  unaffected and still stands). The round's self-reported `Status: partial`
  and its "residual narrowed to $e=0$ only" claim are **both overclaims**
  that must be corrected: sub-case (i)'s residual is still the full
  width-1 window at every $e\ge0$. **CHANGES REQUESTED** — the two
  isolated lemmas are genuine, certified progress (reusable tools), but
  the round's central closure claim is retracted; next round must redo
  Step 0 correctly (the true recursion is a two-step relation
  $O_j=2^{j-1}+O_{j-2}$ when $q=0$ holds at both levels $j,j-1$,
  independently re-derived and verified by the reviewer, 3000 trials,
  zero violations — not the naive one-step relation used this round).

- **`discharging-neighbor-transfer`** — the round-15 labeling bug (calling
  an $\mathrm{AltSum}$ identity "$\mathrm{OddSum}$") is **fixed
  correctly**: the identity is relabeled $\mathrm{AltSum}$ (no algebra
  changed) and a new **OddSum Corollary**
  ($\Delta\mathrm{OddSum}=\Delta\mathrm{AltSum}/2$, from the already-
  certified Lemma AS plus mass conservation) is added and proved in full.
  Reviewer independently re-derived and re-verified the Single-Cut
  Rank-Shift Identity from scratch (own exact-`Fraction` script, 20,000
  random single-split trials across generic values, zero mismatches) and
  hand-checked both worked examples digit-for-digit. **Certified**
  `lemmas/corrected-single-cut-rank-shift-identity-and-oddsum-corollary.md`.
  The connecting-step gap (bounding the telescoped sum over a sequence of
  cuts) is honestly re-confirmed unchanged under the corrected labels (an
  affine $\times\tfrac12$ rescaling changes nothing about the Region-C
  suffix-term obstruction), and the file correctly recommends retiring
  this approach as an independent line (it reduces, with strictly less
  machinery, to `self-similar-induction-on-n`'s own open $\mathrm{GT}(m)$
  recursion). **CHANGES REQUESTED** (genuine certified fix, approach
  itself now recommended dormant/retired going forward, not revived).

- **`reciprocal-potential-induction-on-n`** (new slug, first build) — the
  mandatory cheap-kill correctly and decisively refutes the approach's
  core mechanism, the pointwise reciprocal-recursion inequality
  $1/V(p)\ge1/V(p')+2^{-n}$: tested against **two independently-natural**
  reduction maps ($p\mapsto e_0(n-1)$, and "drop the smallest piece,
  renormalize") at the certified region vertex $e_0(n)$, both fail
  exactly, by exactly $2^{-n}$ (reviewer independently re-derived and
  re-verified both computations from scratch, exact `Fraction`,
  $n=4,\ldots,7$). The structural reason is genuine and correct: a new,
  independently re-verified **Generalized Twin-Anchor Floor Theorem**
  (every AP-shaped partition $p_i=a+(N-i)\delta$, $N\ge4$,
  $\delta\in(0,2/(N(N-1)))$ — not just the specific $e_0$ value of
  $\delta$ — sits exactly at the universal floor $V=1/2$, via the same
  Twin-Anchor construction; reviewer's own script, $N=4,\ldots,11$, 160
  instances, zero deviations) shows the floor-attaining set is an entire
  continuum, not an isolated point, so any reduction map landing back in
  it (as both natural candidates do) forces $(\star)$'s false conclusion.
  **Certified** `lemmas/generalized-twin-anchor-floor-theorem.md`. Status
  `unsolved` is correctly self-reported (the core mechanism is dead as
  stated; a future non-canonical, floor-avoiding map is not ruled out in
  full generality but was neither found nor attempted). **RETHINK** — this
  specific pointwise-reciprocal framing cannot work; a genuinely different
  mechanism (or an explicitly floor-avoiding map) would be needed to
  revive it.

- **`global-lp-vertex-sufficiency`** — a decisive, honestly-scoped
  **numerical** (not exact-arithmetic, not a proof) classification: at
  all $8$ tested hard points ($3$ catalogued $n=3$, $2$ catalogued $n=4$,
  $3$ found by local ascent), branch-comparison-boundary near-tie
  degeneracy ($\ge2$ to $\ge5$ distinct cut-allocations tied to $<10^{-6}$)
  holds universally, co-occurring with within-branch nonzero-fragment
  ties at $5/8$ points — never in isolation. Redirects future
  $\Sigma$-shape work toward a **joint/combined family** rather than
  treating the two candidate families separately, and is cross-validated
  (not contradicted) against `lp-duality-split-polytope`'s certified
  Perfect-Tie-Family Characterization at $e_0$. A genuine methodological
  finding (a low-restart-count optimizer artifact, $\Delta\approx0.0186$,
  caught and excluded before contaminating any conclusion) is also
  honestly reported. No lemma proposed (correctly — numeric classification
  only). **CHANGES REQUESTED** — real diagnostic narrowing of the search
  target, no gap closed.

- **`lp-duality-split-polytope`** — a light cross-check dispatch, executed
  honestly with a correct negative conclusion on both dispatched items:
  (1) the certified Twin-Anchor Construction at $e_0$ is a genuine
  instance of the sibling's "within-branch-tie" phenomenon, but does not
  narrow that open classification (three checked, confirmed gaps: $e_0$'s
  membership in the sibling's candidate set $Q$ is unverified; the tie
  mechanism is AP-structure-specific, not generic; the sibling's actual
  obstruction is about curvature, which this data point doesn't bear on);
  (2) a soft, non-conclusive numeric lead (Nelder–Mead, $n=8,10$,
  $s=n-2,n-3,n-4$) finds no configuration reaching $1/2$ exactly for
  $s<n-1$, consistent with (not proving) the standing $s=n-1$-necessity
  conjecture — with a documented optimizer pitfall (unconstrained search
  producing illegal negative-fragment artifacts below the universal floor)
  flagged for future numeric work. No new theorem or lemma proposed
  (correctly, per the dispatch). **CHANGES REQUESTED** — honest,
  correctly-scoped null/soft result, no gap closed.

## Approaches tried (round 15)

- **`self-similar-induction-on-n`** — two new results, both independently
  re-verified this round (own exact-`Fraction` scripts): the **AltSum
  Small-Sum Lemma** (for any $m\ge0$, any finite multiset $D$ with no cap
  on count or max value, $\mathrm{sum}(D)\le2^m-1\Rightarrow
  \mathrm{OddSum}(D\cup\Gamma_{m-1})\ge\mathrm{sum}(D)$ — a two-line proof
  from already-certified Lemma AS + AltSum Corollary, confirmed with
  20,000 trials, zero violations, hypothesis confirmed tight) and the
  **Sub-case (i) Window Reduction Theorem** (sub-case (i) of $\mathrm{GT}(m)$
  is now unconditionally closed whenever $a_1\ge2^{k-1}+1$, for every
  excess $e\ge0$ — independently confirmed: zero violations outside the
  window across ~9,100 trials, genuine violations found inside the
  residual width-1 window at every tested $k$). Also correctly diagnosed,
  and independently confirmed, that the dispatched Route-2
  continuity/limiting-transfer premise does not hold (round 5's
  `Case-B(m,k)` safe zone is bounded by a hard, fixed unit-width cap
  $\max(B)\le2^{m-1}-1$, not a shrinking-$\delta$ family — re-derived this
  cap independently). $\mathrm{GT}(m)$, $m\ge4$ remains open, now reduced
  to exactly the width-1 window (with excess) plus `Case-B`'s own sliver.
  Status `partial`, correctly self-reported.

- **`global-lp-vertex-sufficiency`** — star/tree fragment-tying topology
  cheap-kill genuinely refuted (independently reproduced a comparable
  violating value, $\approx0.526>c(4)=16/31$, at one of the reported
  $n=4$ failure points); the new **Zero-Removal Invariance Lemma**
  ($\mathrm{OddSum}$ is unchanged by deleting zero-valued elements) is
  fully proved and independently verified (20,000 trials, zero
  violations) — **certified**. The convexity-diagnosis 4-piece witness
  (slopes $0,+1,-1,0$ on $M(x)=\{x,p_1-x,c\}$) was independently
  reproduced exactly, confirming no uniform-curvature LP-duality
  certificate can work cell-independently. Existence-only route remains
  open on branch-comparison-boundary and within-branch-tie candidates.
  Status `partial`, correctly self-reported.

- **`discharging-neighbor-transfer`** (new slug, first build) — the
  **Single-Cut Rank-Shift Identity** passes its cheap-kill on two worked
  examples, but **independent verification found a real definitional
  error**: the identity's algebra is correct, but it computes $\mathrm{AltSum}$
  (the true alternating sum $m_1-m_2+m_3-\cdots$), not $\mathrm{OddSum}$
  (sum of odd-rank elements only, the canonical game-value quantity
  certified in `greedy-optimality-oddsum.md`) as claimed — the file's own
  two "OddSum" worked examples literally compute alternating sums (e.g.
  "$\mathrm{OddSum}(L)=8-4+2-1=5$", which is $\mathrm{AltSum}$; the true
  $\mathrm{OddSum}(L)=8+2=10$). Since split mass is conserved,
  $\Delta\mathrm{OddSum}=\Delta\mathrm{AltSum}/2$ exactly (via the
  certified Lemma AS), so the identity is salvageable with a relabeling
  and a factor-of-$\tfrac12$ correction, but **as literally written it is
  false for OddSum** and is **not certified this round**. The connecting-
  step diagnosis (reduces to the same stuck $\mathrm{GT}(m)$ recursion, no
  independent leverage) is a genuine finding, not fabricated. Status
  `partial` is the correct call (not a dead end, not solved) — next
  round's builder must fix the labeling before the lemma can be
  certified.

- **`lp-duality-split-polytope`** — the new **Twin-Anchor Construction**
  extends `V(e_0)=1/2` from $n\ge6$ to **every $n\ge3$**, with a strictly
  simpler, side-condition-free proof. Independently re-verified from
  scratch (own exact-`Fraction` script, re-deriving $a$ from the
  sum-to-$1$ constraint) for $n=3,\ldots,40$ (38 instances): every
  fragment positive, $n-1\le n$ cuts legal, $\mathrm{AltSum}(M)=0$ exactly
  in all 38 cases. **Certified** `lemmas/twin-anchor-floor-theorem.md`
  (supersedes the range of `chain-correction-floor-theorem.md`, which is
  kept for reference). $n=2$ correctly confirmed genuinely out of scope
  (not an oversight). Cross-validation against the sibling's fragtie
  negative finding correctly shown to be a non-conflict (disjoint
  objects). Status `partial` (this closes a sub-vertex value exactly, not
  the general-$p$ Existence Theorem).

## Approaches tried (round 14)

- **`lp-duality-split-polytope`** — a new, fully proved, independently
  re-derived-from-scratch theorem: the **Chain-Correction Floor Theorem**.
  At the region vertex $e_0$, for every $n\ge6$, an explicit hybrid
  construction (active set $=$ all pieces except the smallest $2$, $s=n-1$
  active pieces, mixing tie-to-untouched-piece, fragment-vs-fragment chain
  ties, and plain bisection) achieves $\mathrm{OddSum}(M)=\tfrac12$ exactly
  — the universal absolute floor for any legal response at any partition.
  **Reviewer independently re-implemented the construction from its literal
  description (own exact-`Fraction` script, not the builder's)** for
  $n=6,7,8,9,10,12,15,20$: every fragment positive, cut count $n-1\le n$
  legal, total mass exactly $1$, $\mathrm{AltSum}=0$ exactly in all 8 cases
  — matches the theorem digit-for-digit. Also independently re-verified the
  Positivity Lemma's inductive inequality $(n+1)(n+4)<2^{n+2}-2$ for
  $n=6,\dots,24$, and the algebraic identity that piece $3$'s and piece
  $5$'s second fragments both collapse to $a-2\delta$. **Certified**
  `lemmas/chain-correction-floor-theorem.md`. **Genuine correction found and
  fixed**: this result shows $V(e_0)=\tfrac12$ (not $c(n)$) for $n\ge6$,
  contradicting a mis-stated equality claim in
  `global-lp-vertex-sufficiency.md` Section 4.5 ("$V(e_0)=c(n)$ exactly, the
  tightest possible case" — that section's own Section 4.3 only ever proved
  $V(e_0)\le c(n)$ via one upper-bound witness construction, never a
  matching lower bound). **The reviewer corrected that sentence in place**
  this round; verified the fix does not affect the Mass-Constraint
  Theorem's actual derivation (which uses only $e_0$'s coordinates, not the
  value of $V(e_0)$) or any other downstream claim. This is **good news, not
  a threat**, to the overall upper-bound program: the actual target
  ($V(p)\le c(n)$ for every $p$) is strengthened, not weakened, at this
  point. Honest scope: does not resolve whether smaller $s$ also reaches
  the floor, nor $n<6$. **CHANGES REQUESTED** (Status stays `partial` for
  the approach as a whole; this is real, certified, independently-verified
  new content plus a caught-and-fixed cross-file error).

- **`self-similar-induction-on-n`** — two new elementary, general-purpose,
  fully proved lemmas plus one theorem proved modulo an honestly-flagged
  gap. **Reviewer independently re-derived and stress-tested (own
  exact-`Fraction` scripts) the AltSum Corollary** ($0\le\mathrm{AltSum}(N)
  \le\max(N)$, 20000 random trials, zero violations) **and the Growth
  Lemma** (the increasing-direction complement of the certified
  Monotonicity Reduction Lemma; feasibility construction re-verified by
  direct reimplementation, $m=1,\dots,6$, $k=2,\dots,m+1$, 500 trials each,
  zero violations) — both **certified**,
  `lemmas/altsum-corollary-and-growth-lemma.md`. Also independently
  reproduced the $q{=}0$/$p{=}0$ peeling identity underlying the
  "Small-Sum Reduction Theorem" (own script, 5000 trials, zero mismatches)
  and the Step-2 counterexample ($D=\{0.4,0.4\}$, $k=0$) that correctly
  kills the naive "piece-cap-relaxed" generalization of $\mathrm{GT}$. The
  **Small-Sum Reduction Theorem itself is NOT certified**: it is explicitly
  proved only "modulo one flagged tie-boundary detail" (the case where the
  Growth Lemma's saturating construction lands a coordinate exactly at the
  cap $2^{m-1}$) — a real, self-reported, unclosed gap, correctly not
  written up as unconditionally established by the builder. Net effect
  (unchanged from the builder's own honest assessment): $\mathrm{GT}(m)$
  for $m\ge4$ remains open, now precisely reduced to exactly two named
  objects (`Case-B(m,k)`, already under attack since round 4; and sub-case
  (i), $q=1,e\ge1$, newly diagnosed but unsolved). **CHANGES REQUESTED.**

- **`global-lp-vertex-sufficiency`** — two honestly-scoped numerical
  findings on fragment-vs-fragment tying, both correctly not written up as
  lemmas (per the dispatch, and correctly per the reviewer's independent
  check that neither is a general proved theorem). **Cheap-kill 1 (cyclic
  pairwise-tie chain)**: refuted broadly (9/15 to 15/15 failure rates,
  $n=3..6$), in exact rational arithmetic — a clean negative result, no
  further action needed on this specific family. **Cheap-kill 2
  (descending fragment chain)**: a self-caught-and-fixed construction bug
  (via the OddSum Floor sanity check, exactly the kind of self-check the
  rigor rules require) followed by a genuinely mixed finding — exhaustive
  search over subset/order/parameter matches the true $V(p)$ at 2/3
  catalogued hard $n=3$ points and clears $c(3)$ at all three, but no
  tractable (closed-form/greedy) selection rule was found, and restricting
  to natural orderings fails broadly (5/8–8/8). Correctly **not** claimed
  as a survival (the exhaustive search is as expensive as computing $V(p)$
  directly) and correctly **not** escalated to a general closed-form
  theorem on this unproven premise. Two precise open sub-questions left for
  next round (closed-form selection rule; whether $\sigma^*(p)$ always has
  descending-chain shape). Also corrected the round-13 "deprioritized"
  framing for fragment-vs-fragment tying (it is the one route the
  round-11 Mass-Constraint Theorem does not cover) — a legitimate scoping
  correction, verified against the cited theorem's actual hypotheses.
  **CHANGES REQUESTED.**

## Approaches tried (round 13)

- **`self-similar-induction-on-n`** — pursued the depth-parametrized
  induction (Route D) toward $\mathrm{GT}(m)$, $m\ge4$. Two new
  general-purpose results, both **independently re-derived and
  re-verified by the reviewer with fresh exact-`Fraction` scripts**
  (not the builder's own), zero violations, and **certified** into
  `lemmas/monotonicity-reduction-and-unified-threshold-pair-peeling.md`:
  the **Monotonicity Reduction Lemma** (shrinking $D$'s coordinates at
  fixed count/cap can only decrease $\mathrm{OddSum}(D\cup T)$), whose
  corollary **fully and unconditionally removes the round-12 large-sum
  ($p\ge3$) scope restriction on $\mathrm{GT}(m)$ for $m=0,1,2,3$** (the
  file's phrasing "for every $m$" was checked and is correctly scoped: it
  is a conditional reusable tool for every $m$, but only *actually*
  removes the caveat where $\mathrm{GT}(m)$'s boundary case is already
  proved, i.e. $m\le3$); and the **Rank-Shift Identity / Unified
  Threshold-Pair-Peeling Lemma**, which replaces Lemmas P1/P2/R1/R2's
  case-by-case ($p,r\in\{0,1,2\}$) treatment with one mechanism showing
  **every** $q\ge2$ (not just $q=2$) closes unconditionally, collapsing
  the case split to three outcomes ($q=0,1,\ge2$). Reviewer independently
  re-verified: Monotonicity Reduction (2554 trials), Rank-Shift Identity
  (18000 trials), $q\ge2$ closure under adversarial stress on $R$ (12600
  trials) — zero violations in all three. The two remaining open
  sub-cases are confirmed **real and precisely stated, not vague**: (i)
  $q=1$ with excess $e\ge1$, target $2^k-a_1$, not yet reduced to a known
  family; (ii) the small-sum mirror of $\mathrm{GT}(k-1)$ itself
  (target $\mathrm{sum}(R)<2^{k-1}$), needed even at $e=0$. $\mathrm{GT}
  (m)$ for $m\ge4$ (gap (a) of the window for $\ell\ge5$) **remains
  open**. **CHANGES REQUESTED** — genuine, certified progress
  (architecture simplification + full scope-gap closure for $m\le3$),
  but the target sub-case is not closed.

- **`global-lp-vertex-sufficiency`** — tested the one remaining untried
  exchange mechanism (response-side/adversary-tie, per round-12's own
  contingency plan), both single-choice and maximally-weak-existential
  forms. **Reviewer independently reimplemented $V(p)$ and the
  mechanism from scratch** (own exhaustive-cut-allocation +
  multi-restart Nelder–Mead code, not the builder's script) and
  reproduced $V(p)$ to the file's own reported precision at all 3 of
  round 13's hard $n=3$ points; re-running the single-choice exchange
  construction confirms $V(q)<V(p)$ (mechanism fails) at all 3 points,
  same sign as reported (magnitudes differ somewhat between runs,
  consistent with reported restart-count sensitivity, not a bug) —
  **the negative finding is real, not a script artifact.** The
  existential form's exact per-point verdict is more noise-sensitive
  (the reviewer's lighter-restart re-test flipped one of the three
  points), consistent with the file's own acknowledgment that this form
  is a $\sim50\%$-failure, not a clean pass either way. **One genuine
  scoping overclaim found**: §4.7.4's closing sentence states the whole
  exchange-mechanism family is "empirically refuted at $n=3,4$," but
  the response-side mechanism (this round's actual new content) was
  only substantively tested at $n=3$ — its single $n=4$ data point is
  explicitly flagged two paragraphs earlier as "not a substantive test"
  (a near-degenerate trivial tie) and the mechanism *held* there, not
  failed. Only round 12's region-geometry mechanisms were substantively
  tested at $n=4$. **CHANGES REQUESTED** — fix that one sentence to
  scope the $n=4$ claim to region-geometry mechanisms only (response-side
  refuted at $n=3$; untested substantively at $n=4$); no other issue
  found, no lemma was proposed (correctly — negative numeric findings
  are not standalone-certifiable), status correctly stays `partial`.

## Approaches tried (round 12)

- **`self-similar-induction-on-n`** — the round's headline claim. The
  **General Theorem GT($m$)** is proved, and independently re-verified by
  the reviewer (exact `Fraction`, thousands of trials, plus 8000+
  instances in the exact gap-(a) regime, zero violations), for
  $m=0,1,2,3$ via a case split on $p:=\#\{a_i>2^{m-1}\}$ (further split by
  $r$ when $p=0$). **The reviewer found and fixed a real scope gap**: the
  file's boxed statement claims $\mathrm{GT}(m)$ for *every* $D$ with no
  bound on $\mathrm{sum}(D)$, but the proof's "$p\le2$" feasibility
  argument is (by the file's own honest admission, "not asserted
  globally") only justified when $\mathrm{sum}(D)<3\cdot2^{m-1}$ — outside
  that zone $p\ge3$ is possible and genuinely uncovered by the given case
  split. **Certified a corrected, scoped version** (adds the hypothesis
  $\mathrm{sum}(D)<3\cdot2^{m-1}$, automatically true everywhere the
  theorem is actually used in this file) into
  `lemmas/general-peeling-theorem-and-window-endpoint-closure.md`; the
  reviewer's own stress test found no violation outside the certified
  zone either, so the fully general claim is likely true but not
  established by this round's proof. **The corollary that matters is
  unaffected and independently reverified**: gap (a) of the shared
  Branch-I.A-restricted window is closed, for every admissible $D$ (not a
  witness), at $\ell=1,2,3,4$. **CHANGES REQUESTED.**

- **`greedy-reduction-geometric`** — closes gap (b) of the same shared
  window **in full** (both the piece-cap-unsaturated sub-case (b)(i),
  previously covered by the certified Lemma TPI, and the piece-cap-
  saturated sub-case (b)(ii), previously untouched by any approach), via
  a new **Elementwise Monotonicity Lemma**, **Transfer Monotonicity
  Theorem**, and **Window Reduction Theorem** — all independently
  re-verified by the reviewer in exact `Fraction` arithmetic (thousands
  of trials plus a from-scratch 2259-instance end-to-end reduction-chain
  test), zero violations, no gaps found. The round's flagged "headroom
  short by exactly $\varepsilon$ at $|D|=1$" subtlety is genuinely
  resolved (not patched over): the fix correctly switches to a "fresh
  slot" insertion mechanism whenever $|D|<\ell$, proved to need no
  headroom at all, with the "grow existing coordinate" mechanism reserved
  for the cardinality-saturated case where the headroom bound is proved
  ample. Certified
  `lemmas/window-reduction-theorem-and-elementwise-monotonicity.md`.
  **Combined with `self-similar-induction-on-n`'s GT($m$) corollary above,
  the shared window is now fully closed — every gap — at $\ell=1,2,3,4$**,
  a strictly stronger conclusion than either file states alone (the
  sibling file's own round-12 corollary explicitly leaves gap (b)(ii)
  open; this file's Window Reduction Theorem closes it). **CHANGES
  REQUESTED.**

- **`lp-duality-split-polytope`** — a complete, independently-verified
  negative theorem for a new, structurally disjoint construction family
  at $e_0$. The **Integer-Alternating-Sum Lower Bound Lemma**
  (elementary, general-purpose) plus the **Perfect-Tie-Family Exact
  Characterization Theorem** show that, among "perfect" (zero-residual)
  self-tie/fragment-vs-fragment-tie constructions at $e_0$, only
  $s=n-1$ active pieces ever attain $c(n)$ (exactly, never below), so no
  fixed $s_0$ suffices — reviewer independently re-derived this by
  brute-force exact `Fraction` search over every active-set choice,
  $n=2,\dots,12$ (11 values, every $s$ at each), zero mismatches with the
  closed form or the theorem's three consequences. This is genuinely
  independent of (different technique from, disjoint family from) round
  11's Mass-Constraint Theorem — convergent evidence, not a restatement.
  Certified
  `lemmas/integer-altsum-lower-bound-and-perfect-tie-characterization.md`.
  Honestly scoped: does not cover the general nonzero-residual
  fragment-vs-fragment family (a numeric spot-check shows nonzero residual
  strictly helps at one tested point). **CHANGES REQUESTED.**

- **`global-lp-vertex-sufficiency`** — two negative findings on the
  round's primary target (Region-Boundary Monotonicity), reported
  honestly as evidence, not certified (correctly, per the builder — these
  are point/family-specific refutations, not general theorems). (1) The
  literal "fixed target vertex, straight-line, path-monotone" mechanism
  toward $e_0$ or $e_1$, robust at $n=2$, is refuted by noise-controlled
  numerical evidence at $n=3$ (a genuine sign-changing path, confirmed at
  $3\times$ restart count, not optimizer jitter) — the weaker
  actually-needed endpoint inequality was not violated in any test.
  (2) Transplanting the exact $e_0$-closing $k$-Anchor-Merge construction
  unchanged to every point of the region is refuted in **exact**
  arithmetic for $n=2,\dots,8$ (a genuinely stronger, non-numerical
  result than (1)). Both narrow the search space (two clean mechanisms
  ruled out) without resolving the Existence Theorem's $\Sigma$-shape
  residual. **CHANGES REQUESTED.**

- **`structured-randomization-upper-bound`** — first build. A precise,
  general, correct negative result: the **OddSum Floor Lemma**
  ($\mathrm{OddSum}(M)\ge\mathrm{sum}(M)/2$, elementary) plus the
  **Expectation Obstruction Theorem** show any structured-randomization
  scheme with $n$-independent "mediocre-candidate mass" $(\delta,
  \varepsilon)$ fails once $n$ exceeds an explicit threshold — reviewer
  independently re-derived the algebra, matches exactly, and confirms it
  matches the round's two tested schemes' numerical failures
  quantitatively. Certified
  `lemmas/oddsum-floor-and-expectation-obstruction.md`. This is a real,
  general theorem, but it is a structural *impossibility* result about
  this approach's own mechanism (expectation over discrete randomization),
  not a positive step toward the problem's actual bound — **`unsolved`
  is the correct status** (no overclaim: nothing here bounds $V(p)$ or
  constructs anything; no underclaim: the theorem is honestly presented
  as ruling out an entire mechanism, not just "the schemes tried didn't
  work"). A by-product deterministic finding (min-over-index Theorem-12
  beats $c(6)$ robustly near one documented survivor point, but fails
  broadly at other $n$/points, $100\%$ failure at $n=2$) is correctly
  flagged as a lead for other approaches, not a result of this one.
  **RETHINK** — the approach's core mechanism (expectation over a fixed
  discrete randomization) is now shown structurally incapable of working
  except via a concentrating design that would defeat the purpose of
  randomizing; a future round should either find a genuinely
  concentrating design or treat this direction as exhausted.

## Approaches tried (round 11)

- `global-lp-vertex-sufficiency` — two genuine soundness fixes plus one
  precisely-scoped negative result, all independently re-verified by the
  reviewer. (1) A textual bug in Section 1's degrees-of-freedom description
  ("one free block total" vs. the proof's actual "one free block per split
  piece") is corrected. (2) A real gap in Lemma 4.1(b) — it pinned the
  *ordering between* branches $\sigma,\tau$ but never justified that each
  $f_\sigma$ is itself a single affine formula on a cell — is closed by the
  new **Rank-Pinning Lemma** (enlarging $L$ with within-branch pairwise
  differences; reviewer independently re-derived the elementary
  order-theory argument, confirmed correct, confirmed it does not disturb
  the already-closed $Q_{\mathrm{region}}$). (3) The round's main new
  target (bounded-split-piece-count sufficiency) is **refuted for the
  natural General Multi-Piece Subset-Tie construction family**: the new
  **Mass-Constraint Theorem** ($\Pi\ge1/2$ for any legal instance) forces
  $s>(n+1)/3$ split pieces at the region vertex $e_0$ — unbounded as
  $n\to\infty$, ruling out any fixed $s_0$ for this family — reviewer
  independently re-derived the value formula, the mass inequality, and the
  exact coordinate bound $p_1(e_0)<3/(2(n+1))$, all confirmed correct.
  Certified `lemmas/rank-pinning-lemma-and-mass-constraint-theorem.md`. The
  Existence Theorem itself remains open (the $\Sigma$-shape part of $Q$).
  **CHANGES REQUESTED.**

- `self-similar-induction-on-n` — genuine, modest progress, honestly
  scoped. Two new general-purpose lemmas, both independently re-derived by
  the reviewer and confirmed correct: the **Affine-Rank Lemma**
  (cell-wise affineness of OddSum in free coordinates merged with frozen
  values — genuinely simpler here than the sibling approach's version, no
  free-block elimination needed) and the **Vertex-Attainment Lemma**
  (extrema of an affine functional on a compact polytope occur at
  vertices). Combined into a Middle-Regime Vertex Reduction Theorem.
  Applied to the smallest nonempty middle-regime instance $(j,c)=(2,1)$:
  **exact closures at $m=3,4$** (OddSum$=2^m$ exactly at an explicit
  boundary vertex) and **exact strict-slack confirmation at $m=5$**
  (OddSum$=33>32$) — reviewer hand-verified all three multisets and sums
  digit-for-digit, all correct. Honestly reported as not closing general
  $m$, nor the middle regime, `Case-B(m,k)`, or gap (b)(ii) in general (the
  vertex enumeration used is not proved exhaustive). Certified
  `lemmas/affine-rank-and-vertex-attainment-middle-regime.md`. **CHANGES
  REQUESTED.**

- `greedy-reduction-geometric` — the round's dispatched "Case B quick win"
  premise is **refuted by an exact stress-test counterexample**
  (independently re-verified by the reviewer, from-scratch exact
  `Fraction` script: margin $19/81977$ at $m=4$, matching the file's claim
  digit-for-digit, not the round's originally-claimed $\approx0.34$
  slack), and replaced by a genuine positive finding: **Theorem N** proves
  Case B's hardest identified slice (the $S'''$-unsplit-full-budget
  sub-case) is *literally* (symbol-for-symbol, reviewer independently
  re-checked every substitution) an instance of the file's own TOP-ONLY$
  (m-1)$ complementary regime — already-certified Theorem 6 closes a
  genuine (if vacuous-until-$m=9$) piece outright, and the rest coincides
  exactly with `self-similar-induction-on-n`'s Branch-I.A-restricted
  window, unifying two previously-separate lines of work. **Lemma N**
  (WLOG $b_2=2^{m-1}$) is a complete, gap-free formal proof, independently
  re-checked. Case A not attempted (time); one precise scope diagnosis
  recorded, not a hand-wave. Certified
  `lemmas/wlog-b2-and-case-b-topOnly-equivalence.md`. Level-Absorption
  remains open. **CHANGES REQUESTED.**

- `lp-duality-split-polytope` — a clean negative result plus a genuine new
  positive byproduct, both independently re-verified by the reviewer with
  from-scratch exact-`Fraction` scripts. **Finding 1 (negative, exact):**
  the direct multi-landmark transplant of round 10's Multi-Piece
  Sufficiency construction to LB's geometric partition fails, with
  shortfall growing from $\approx1.4\times10^{-7}$ ($n=2$) to
  $\approx0.123$ ($n=8$) — reviewer's independent script matched the
  file's table exactly at every tested $n$. **Finding 2 (new positive
  result): the Top-Duplication Witness Theorem** — splitting only the top
  landmark of LB's partition into $2^{n-1},\dots,2^1,1,1$ achieves
  $\mathrm{OddSum}=c(n)$ *exactly*, for every $n\ge0$ — reviewer
  independently re-implemented the construction from its literal
  description (not the closed-form shortcut) and matched $c(n)$ exactly
  (as identical fractions, not floats) for $n=0,\dots,14$. This proves
  $V(p_{\mathrm{LB}})\le c(n)$ unconditionally, a genuine single-point
  contribution to the upper-bound direction, honestly scoped as not
  proving the reverse inequality nor extending to other points. Certified
  `lemmas/top-duplication-witness-theorem.md`. **CHANGES REQUESTED.**

## Approaches tried (round 10)

- `global-lp-vertex-sufficiency` — **the round-9 gap is closed.** The
  reviewer's found gap (candidate list $L$ missing the functional $p_k$) is
  fixed correctly: adding $p_k$ to $L$ is verified to restore boundedness
  (independently re-derived) while leaving Lemmas 4.1/4.2 and the Finite-Cell
  Affine-Vertex Reduction Theorem's proof unaffected (they use only
  finiteness/affineness of $L$, not an enumerated list). Three new results
  this round, all independently re-verified by the reviewer (own exact
  `Fraction`/algebra, not the builder's scripts): the **Region-Vertex
  Classification Theorem** (exact vertex count and sign pattern of the
  region-only polytope for every $n\ge2$, via three closed sign claims A/B/C
  — re-derived and matched exactly for $n=2,\dots,9$); the **Boundary
  Continuity Theorem** (closes every point of the degenerate face
  $p_k=0$ via a Small-Mass Insertion Lemma + Lipschitz sandwich, algebra
  checked); and the **exact closure of the region-only genuine vertices**
  ($e_0,e_1$, plus $e_2$ at $n=2$) via the certified $k$-Anchor-Merge Lemma,
  giving $\mathrm{OddSum}=1/2$ or $c(n)$ exactly by a parity rule on the pair
  count — independently reconstructed and verified for $n=2,\dots,8$ (14
  instances), zero deviation. This fully closes the region-only candidate
  sub-list $Q_{\mathrm{region}}$. Certified
  `lemmas/finite-cell-vertex-reduction-and-region-classification.md`.
  **Honestly still open** (correctly reported, no overclaim): the
  $\Sigma$-shape part of the candidate set $Q$ is untouched, so the Existence
  Theorem itself remains unproved. **CHANGES REQUESTED.**

- `greedy-reduction-geometric` — genuine progress on Level-Absorption, still
  open. **Lemma M ($B''$-Banking Lemma)** proved in full via the already-
  certified general Theorem 7 (correcting the outline's citation of the
  insufficient special case Theorem 7a) — reviewer traced every hypothesis
  and confirms no gap. The **Candidate Swap Lemma is refuted** by an exact,
  hand-checkable counterexample ($Q=\varnothing,b=10,P=\{6,6\}$: OddSum$(P)=
  6<10=$OddSum$(\{b\})$, independently re-verified by the reviewer), ruling
  out an entire family of future "prove an abstract swap bound, then add"
  attempts. Level-Absorption is reduced to a clean $k=2$ base case,
  numerically supported but not proved. Certified
  `lemmas/level-absorption-banking-lemma-and-swap-refutation.md`. **CHANGES
  REQUESTED.**

- `self-similar-induction-on-n` — genuine, modest progress. **Lemma TPI**
  (Tiny-Piece Insertion Monotonicity) is a clean, correct, elementary fact,
  independently re-derived by the reviewer; its corollary fully closes gap
  (b)(i) of the Branch-I.A window (piece-cap-unsaturated case). The
  **endpoint reduction identity** for gap (a) is an exact equivalence
  (algebra independently re-checked), but honestly reduces gap (a) to the
  file's own still-open $j\ge2$ trichotomy one level down — not a closure.
  Certified
  `lemmas/tiny-piece-insertion-monotonicity-and-endpoint-reduction.md`. Note:
  the round-10 dispatch summary's claim that this approach "corrected a
  stale outliner claim about idx=1" does not match this file (no mention of
  `idx` anywhere in it) — that correction belongs to
  `lp-duality-split-polytope`, evidently a mixup in the round's dispatch
  text, not an actual claim made by this approach. **CHANGES REQUESTED.**

- `lp-duality-split-polytope` — genuine new positive result. Confirmed the
  correction that the `idx=1` Multi-Piece Necessity case was already fully
  closed in round 8 (verified against `current.md`'s own history and
  `lemmas/idx1-closure-and-full-multi-piece-necessity.md`; the round-10
  outliner's dispatch was indeed stale on this point). **New: Multi-Piece
  Sufficiency Theorem for the triangular family**, every $n\ge3$ at once, an
  explicit $(N-1)$-cut construction achieving $\mathrm{OddSum}=\tfrac12+
  \tfrac12(c(n)-\tfrac12)<c(n)$ — independently re-implemented from scratch
  by the reviewer (exact `Fraction`, $N=4,\dots,39$, 36 instances, zero
  deviation; caught and fixed an unrelated bug in the reviewer's own first
  verification script, an AltSum-vs-OddSum mixup, before confirming the
  proof itself is correct). Combined with the already-certified Necessity
  direction, this gives a complete Necessity+Sufficiency picture for the
  triangular family (not the general upper-bound direction). Certified
  `lemmas/multi-piece-sufficiency-triangular-family.md`. **CHANGES
  REQUESTED.**

## Approaches tried (round 9)

- `global-lp-vertex-sufficiency` — real progress, **but the round's
  headline claim ("Finite-Cell Affine-Vertex Reduction Theorem," fully
  proved, concavity-free) has a genuine gap, found by the reviewer**, so
  the pre-written self-certification the builder placed in
  `lemmas/finite-cell-affine-vertex-reduction.md` is **rejected and
  removed** (that file was written directly by the builder this round,
  bypassing review — a process violation; per protocol only the reviewer
  certifies into `lemmas/`). The gap: the theorem's candidate vertex set
  $Q$ is defined as "solutions of $(k-1)$-subsets of $L$ set to zero,"
  where $L$ contains the Global Vertex Lemma's shape-validity/ordering
  functionals plus the balanced region's own two families of defining
  inequalities ($p_1<1/2$ and the $n$ gap inequalities) — but $L$ does
  **not** include $p_k\ge0$ (positivity of the *last* piece). The reviewer
  verified by direct computation that this constraint is genuinely
  non-redundant: the region cut out by $L$ alone (without $p_i\ge0$) is
  **unbounded** and contains points with $p_k<0$ (send one gap to
  $+\infty$ while keeping $p_1\le1/2$ by making $p_k$ correspondingly very
  negative — consistent with every inequality in $L$, since $L$ places no
  upper bound on any individual gap). Since the theorem's own polytope $P$
  is explicitly built by additionally "intersecting with the bounded
  simplex" (i.e. using $p_i\ge0$ for all $i$, not part of $L$), a vertex
  of $P$ lying on the facet $p_k=0$ is possible and is **not** captured by
  any $(k-1)$-subset of $L$. (The reviewer also verified, by the same
  computation, that $p_i\ge0$ for $i=1,\dots,n$ IS automatically
  redundant given the gap constraints and $p_k\ge0$ — so the fix is
  narrow: add the single functional $p_k$ to $L$ and redo the
  vertex-extraction step, not a full re-derivation.) The rest of the
  round's work is solid: Lemma 4.1 (cell-wise constancy of validity and
  ordering) is correctly proved from the finiteness and affineness of
  $L$; Lemma 4.2 (the closed-cell/density-continuity boundary argument,
  explicitly resolving the outline-reviewer's flagged subtlety) is
  correct, elementary point-set topology, correctly applied. Section 5's
  numerical finding (a documented $n=6$ "survivor" is not a true
  counterexample to the Existence Theorem, only a failure of the
  narrower named-tool family — via a numerically-found 3-piece
  generalized-tie response clearing $c(6)$ by a $50\times$ larger margin)
  is honestly reported as numerical, not exact-arithmetic, evidence, not a
  closure. **Status `partial` is correct**; the "fully proved,
  unconditionally" language attached to Section 4's Theorem is an
  overclaim that must be corrected next round (add $p_k$ to $L$, redo the
  vertex step — likely a quick fix, but not yet done). **CHANGES
  REQUESTED.**

- `self-similar-induction-on-n` — real progress, honestly and accurately
  reported. **Theorem W (the Branch-I.A-restricted window's exact value at
  its left endpoint)** is fully proved and reviewer-verified: found and
  fixed a genuine computational slip in the round's dispatched witness
  (the correct filler value is $r=1+\varepsilon/2$, not
  $(1+\varepsilon)/2$ — the latter's multiset sum is off by exactly $1$
  and is inadmissible). The corrected witness's exact value,
  $\mathrm{OddSum}(C\cup\Gamma_{\ell-1})=2^\ell+\varepsilon/2$, was
  independently re-derived by the reviewer (own exact-`Fraction` script,
  not the builder's) for $\ell=2,\dots,8$, $\varepsilon\in\{.1,.3,.5,.7,.9\}$
  (40 instances, zero deviation), and the cited General Insertion Lemma
  (Theorem 4, `lemmas/perfect-pairing-subadditivity-and-general-insertion.md`)
  independently re-stress-tested (2000 fresh trials, zero violations).
  Certified `lemmas/theorem-w-window-endpoint-witness.md`. The
  $c_1$-independence simplification $(\ddagger)$ (the window's closure is
  equivalent to a single, $c_1$-independent target across the whole $W$
  range) is a correct but essentially trivial algebraic restatement
  ($W+c_1=2^\ell+\varepsilon$ identically) — real, but modest. **The
  window is honestly reported as still open**: Theorem W settles only the
  single endpoint, not the endpoint's optimality among all admissible $D$
  there, nor any other $c_1$ in the window's interior — both flagged,
  correctly, as unproved (numerically supported only). **CHANGES
  REQUESTED** — Status `partial` is accurate.

- `greedy-reduction-geometric` — real progress. **Lemma L
  (Unsplit-Baseline)** is fully proved and reviewer-verified: a clean
  two-step chain of two already-certified facts (Theorem 7a, applied at
  parameter $m'=m-1$; then Theorem 13, General Insertion Monotonicity,
  with no hypothesis needed on the inserted $B''$), giving
  $\mathrm{OddSum}(S''\cup B''\cup\{2^{m-1}\})\ge2^{m-1}\ge
  b_2+\mathrm{sum}(B'')$ whenever level $m-1$ is left unsplit. The
  reviewer independently traced both certified inputs' hypotheses and
  confirmed they are met exactly as invoked, with no gap. Certified
  `lemmas/unsplit-baseline-lemma-L.md`. The round's second claim — that
  the natural abstract Split-Degradation candidate bound (degradation
  $\le g-q_1$, depending only on the split's max fragment), even if true,
  is provably insufficient to close Level-Absorption whenever $k\ge3$ — is
  **correctly derived** as a conditional deduction (the reviewer
  independently re-checked the algebra: applying the candidate bound with
  Lemma L gives only $\mathrm{OddSum}(M'\cup P)\ge\mu_1$, strictly weaker
  than the target $b_2+\mathrm{sum}(B'')>\mu_1$ whenever $B''\ne
  \varnothing$), and the file is explicit that the Candidate Lemma itself
  is evidenced by hand-computation only, not proved, and is correctly
  **not** used as an established fact anywhere downstream. Level-Absorption
  remains open, honestly so. **CHANGES REQUESTED** — Status `partial` is
  accurate.

- `lp-duality-split-polytope` — real progress, a genuine **negative
  finding, independently verified in full**: the round's requested
  deliverable (an explicit general-$n$ 2-piece construction generalizing
  the $n=3$ triangular-family witness) does not exist, backed by exact
  computation, not just a failed search. The reviewer independently
  re-derived and re-verified: (1) the **General Consecutive-Block AltSum
  Formula** ($\mathrm{Blk}(c,m)=0,\ m/2,\ (m-1)/2+(c+1)$ by parity, for a
  block of $m$ consecutive integers starting at $c+1$) — re-derived from
  scratch and checked against direct exact computation for $c=0,\dots,14$,
  $m=0,\dots,14$ (225 instances, exact match); (2) the **Bottom-Block-
  Doubling exact value theorem** — re-implemented the construction from
  the prose description independently and matched
  $\mathrm{AltSum}(L\cup W)=\mathrm{Blk}(k,N-2-k)$ exactly for every
  $N=4,\dots,59$ (56 instances); (3) the full excess/threshold/ratio table
  (representative rows $N=4,5,6,7,10,20,39,59$) — recomputed independently
  and matched the file's reported values exactly, confirming the
  crossover at $N=7$ ($n=6$) and the unbounded, monotonically-growing
  failure ratio (up to $\sim1.2\times10^{16}$ at $N=59$). Both formulas
  certified: `lemmas/consecutive-block-altsum-and-bottom-block-doubling.md`.
  The file is explicit and correct about scope: this disproves the
  premise for two specific natural 2-piece construction families (plus a
  general order-of-magnitude argument, $\Theta(1/N)$ achievable excess vs.
  $\Theta(2^{-N})$ required), not a fully general impossibility theorem
  covering every conceivable 2-piece response — and it does **not** by
  itself bear on the problem's general upper-bound direction (the
  triangular family is one specific example, not shown to be LB's actual
  extremal partition). **CHANGES REQUESTED** — Status `partial` is
  accurate.

## Approaches tried (rounds 1-8, retained for history)
See prior versions of this file (git history) for the full round-by-round
account.

## Current best

**Round 17 additions/corrections (reviewer-verified independently with fresh
scripts; see "Approaches tried (round 17)" above for full detail).**
`self-similar-induction-on-n` correctly fixes round 16's retracted Step-0 bug
(certified: **Even-target Companion Peeling identity** and the **corrected
$e$-fold $q{=}0$-chain closed form**,
`lemmas/even-target-companion-peeling-and-corrected-qzero-chain.md`), and
genuinely extends Sub-case (i)'s closure to **every even excess $e\ge2$
across the whole range $a_1\in(2^{k-1},2^k]$**, plus the width-1 window
itself at every $e\ge1$ (both parities), plus the vacuous $(k,e)=(1,1)$ case
— strictly beyond round 15. **But the round's headline ("Sub-case (i) fully
closed for every $e\ge1$, no residual window") is an overclaim**: the
reviewer found the odd-excess branch's proof (Claim B) only ever covers
$a_1$ *inside* the window, and the true worst case over the theorem's
claimed full range sits outside it (at $a_1=2^k$) where, for $e=1$
specifically, the cap-free version is exactly and provably **false**
(explicit counterexample, $(k,e)=(2,1)$, $a_1=494/125$) — though the
cardinality-capped version appears true numerically (zero violations in
$145{,}546$ targeted trials), no proof of the capped case is given. **The
true residual is therefore**: $e=0$ (unchanged, as before) **plus** odd
excess $e\ge1$ outside the width-1 window (newly identified this round,
concretely open at every $k\ge2$, $e=1$) — a real but different and more
precisely stated open set than round 17's own claimed "$e=0$ only."
`global-lp-vertex-sufficiency`'s new **Flat/Kink Parity Lemma**
(`lemmas/flat-kink-parity-lemma.md`) is a genuine, fully proved,
general-purpose diagnostic mechanism unifying its two round-16 phenomena,
correctly not claimed to close the Existence Theorem's residual.
`lp-duality-split-polytope`'s new **Even-Multiplicity Equality Criterion**
and **Generalized Mass-Constraint Theorem**
(`lemmas/even-multiplicity-criterion-and-generalized-mass-constraint.md`)
genuinely strengthen round 11's Mass-Constraint Theorem to any legal
response, giving one new exact impossibility result ($n=8,s=4$) and an
honest asymptotic account of why this technique alone cannot reach the
conjectured $s\ge n-1$ necessity.

**Round 16 additions/corrections (reviewer-verified independently with
fresh scripts; see "Approaches tried (round 16)" above for full detail).**
`self-similar-induction-on-n`'s **Half-Sum Corollary** and **Large-Sum
Closure Theorem** are certified, general-purpose tools
(`lemmas/half-sum-corollary-and-large-sum-closure-theorem.md`), but its
round-16 headline claim ("sub-case (i) of $\mathrm{GT}(m)$ closed for every
excess $e\ge1$") is **false** and is retracted — a direct exact-`Fraction`
counterexample was found by the reviewer. **Sub-case (i)'s residual is
still the full width-1 window at every $e\ge0$**, exactly as after round
15 (no narrowing to $e=0$ only; that claim does not stand).
`discharging-neighbor-transfer`'s round-15 AltSum/OddSum labeling bug is
correctly fixed and certified
(`lemmas/corrected-single-cut-rank-shift-identity-and-oddsum-corollary.md`);
the approach is recommended retired (its connecting-step gap reduces to
`self-similar-induction-on-n`'s own $\mathrm{GT}(m)$ with strictly less
machinery). The new `reciprocal-potential-induction-on-n` cleanly refutes
its own core mechanism (pointwise reciprocal-recursion induction on $n$) —
Status `unsolved`, correctly self-reported — but certifies a genuinely
useful general-purpose byproduct, the **Generalized Twin-Anchor Floor
Theorem** (`lemmas/generalized-twin-anchor-floor-theorem.md`: an entire
continuum of AP-shaped partitions per $N$, not just $e_0$, sits exactly at
the universal floor $V=1/2$). `global-lp-vertex-sufficiency` and
`lp-duality-split-polytope` both report honest, correctly-scoped numeric
findings (a joint branch-comparison/within-branch-tie co-occurrence
pattern; a soft $s<n-1$ numeric lead) with no lemma and no gap closed.

**Round 14 additions (reviewer-verified independently with fresh scripts;
see "Approaches tried (round 14)" above for full detail).**
`lp-duality-split-polytope`'s new **Chain-Correction Floor Theorem**
(`lemmas/chain-correction-floor-theorem.md`) shows $V(e_0)=\tfrac12$ exactly
for every $n\ge6$ (not $c(n)$ as a prior overclaim in
`global-lp-vertex-sufficiency.md` stated — now corrected in place by the
reviewer; the correction does not affect any downstream derivation and
strengthens, rather than threatens, the upper-bound program).
`self-similar-induction-on-n`'s new **AltSum Corollary** and **Growth
Lemma** (`lemmas/altsum-corollary-and-growth-lemma.md`) are certified,
general-purpose tools; the round's "Small-Sum Reduction Theorem" built from
them is honestly reported as incomplete (one flagged tie-boundary gap) and
is *not* certified. $\mathrm{GT}(m)$ for $m\ge4$ (hence gap (a) for
$\ell\ge5$) remains open, now reduced to exactly two named sub-objects
(`Case-B(m,k)`; sub-case $q=1,e\ge1$).
`global-lp-vertex-sufficiency` reports two honestly-scoped negative/mixed
numerical findings on fragment-vs-fragment tying (cyclic chain: refuted
broadly; descending chain: mixed, no tractable closed-form rule found),
correctly not written up as lemmas; the $\Sigma$-shape classification gap
remains the sole open obstruction on the upper-bound side.

**Round 13 additions (reviewer-verified independently with fresh scripts;
see "Approaches tried (round 13)" above for full detail).** The
Monotonicity Reduction Lemma and Unified Threshold-Pair-Peeling Lemma
(`lemmas/monotonicity-reduction-and-unified-threshold-pair-peeling.md`)
fully remove the large-sum scope restriction on $\mathrm{GT}(m)$ for
$m=0,1,2,3$ (no effect on the already-closed $\ell=1,2,3,4$ window result,
which never needed the unrestricted-sum version) and simplify the
case-split architecture for $\mathrm{GT}(m)$, $m\ge4$, to three cases —
but $\mathrm{GT}(m)$, $m\ge4$ itself (hence gap (a) for $\ell\ge5$) is
still open, narrowed to two precisely-stated sub-cases (see above).
`global-lp-vertex-sufficiency`'s response-side exchange mechanism is
refuted at $n=3$ (confirmed by independent reimplementation); the
exchange-mechanism-as-a-class conclusion needs its $n=4$ scoping sentence
corrected (flagged above) but the practical recommendation (stop trying
exchange-move variants) stands.

**Round 12 additions (all reviewer-verified independently, no gaps
introduced beyond one scoped correction; see "Approaches tried (round 12)"
above for full detail).** The shared Branch-I.A-restricted window (see
below) is **fully closed — every gap — at $\ell=1,2,3,4$**, combining
`self-similar-induction-on-n`'s new General Theorem GT($m$) (gap (a), the
top endpoint, for every admissible $D$, $m=\ell-1=0,1,2,3$; certified in a
scope-corrected form, `lemmas/general-peeling-theorem-and-window-endpoint-
closure.md`) with `greedy-reduction-geometric`'s new Window Reduction
Theorem (gap (b), both sub-cases, all $\ell\ge2$; certified
`lemmas/window-reduction-theorem-and-elementwise-monotonicity.md`) and the
already-certified Theorem W (left endpoint, all $\ell$). This is a
genuinely stronger conclusion than either contributing file claims alone.
General $\ell\ge5$ remains open (gated on GT($m$) for $m\ge4$).
`lp-duality-split-polytope` adds the Perfect-Tie-Family Exact
Characterization Theorem, a second, independent, disjoint-technique
negative result ruling out bounded-$s_0$ "perfect" self-/fragment-tie
constructions at $e_0$ (certified
`lemmas/integer-altsum-lower-bound-and-perfect-tie-characterization.md`).
`global-lp-vertex-sufficiency` rules out two proposed bypass mechanisms
for the Existence Theorem (fixed-vertex path-monotonicity, refuted
numerically at $n=3$; the transplanted $e_0$-construction, refuted in
exact arithmetic for $n=2,\dots,8$) without resolving it. A new approach,
`structured-randomization-upper-bound`, proves a genuine structural
impossibility result (Expectation Obstruction Theorem, certified
`lemmas/oddsum-floor-and-expectation-obstruction.md`) for its own
expectation-over-randomization mechanism, remaining `unsolved`. All five
approaches' status otherwise unchanged (`partial` except the new one,
`unsolved`).

**Round 11 additions (all reviewer-verified independently, no gaps
introduced, none change the overall status):** `global-lp-vertex-
sufficiency`'s Finite-Cell Theorem gains a closed soundness gap
(Rank-Pinning Lemma) and a scoped negative result (Mass-Constraint
Theorem, ruling out bounded-$s_0$ tie-to-untouched-piece constructions);
`self-similar-induction-on-n` gains a reusable Middle-Regime Vertex
Reduction mechanism plus three exact small-instance closures;
`greedy-reduction-geometric` unifies Level-Absorption's Case B (on its
hardest slice) with the already-tracked Branch-I.A-restricted window via
an exact equivalence (Theorem N), correcting a stress-tested-false "quick
win" premise; `lp-duality-split-polytope` adds the Top-Duplication Witness
Theorem, an exact single-point upper-bound result at LB's own partition
($V(p_{\mathrm{LB}})\le c(n)$ for every $n$). All four remain `partial`;
see "Approaches tried (round 11)" above for full detail.

**Reduction (proved, all approaches agree, certified
`lemmas/reduction-to-multiset-minimax.md`).** The two-phase game's value is
$$c(n)=\max_{\substack{p_1,\dots,p_k>0\\ \sum p_i=1,\ k\le n+1}}\ \min_{\substack{\text{refinement using}\\ \le n\text{ further cuts}}} \mathrm{OddSum}(\text{resulting multiset}),$$
via the Greedy-Optimality Lemma (`lemmas/greedy-optimality-oddsum.md`).

**Conjectured / strongly evidenced closed form:** $c(n)=\dfrac{2^n}{2^{n+1}-1}$,
attained by LB's geometric partition.

**Proved in full, both directions, small cases:** $c(0)=1$, $c(1)=2/3$.

**Lower-bound direction (LB's geometric construction achieves $\ge c(n)$):**
- `T(2)` fully closed; the Dominant-Chain regime of TOP-ONLY closed for
  every `n`; large violation depth closed. Residual open region of
  TOP-ONLY: `2^(m-3)≤a1<2^(m-1)`.
- Within that region, `Case-B(m,k)` is closed except a narrow residual near
  `a1=2^(m-1)`, equivalent (round 8) to the Branch-I.A-restricted window.
  **As of round 12, the window is fully closed — every gap — for
  $\ell=1,2,3,4$**: the left endpoint (Theorem W,
  `lemmas/theorem-w-window-endpoint-witness.md`), the top endpoint/gap (a)
  for every admissible $D$ (General Theorem GT($m$), $m=\ell-1=0,1,2,3$,
  `lemmas/general-peeling-theorem-and-window-endpoint-closure.md`), and
  monotonicity/gap (b) in full — both the piece-cap-unsaturated sub-case
  (b)(i) and the piece-cap-saturated sub-case (b)(ii) (Window Reduction
  Theorem, all $\ell\ge2$, strictly subsuming the earlier Lemma TPI,
  `lemmas/window-reduction-theorem-and-elementwise-monotonicity.md`).
  **General $\ell\ge5$ remains open**: GT($m$) is proved only for
  $m=0,1,2,3$ (the $r=0$/self-similar-descent sub-case becomes feasible
  only from $m=4$ onward and needs one further level of recursion, not
  yet completed), and endpoint-optimality among all $D$ at the window's
  interior is likewise only settled where GT($m$) is proved.
- The fully general Case 2 (top piece AND tail cut simultaneously): the
  "top-levels-clear" case is closed (Theorem 7); Subcase (a)
  (Insertion-Robustness) of the general interleaved case's inductive step
  is fully closed (Theorems 12/13, certified round 8). Subcase (b)
  (Level-Absorption) remains open; its entire remaining difficulty was
  isolated (round 9) to a "re-splitting degradation" question via Lemma L
  (Unsplit-Baseline, `lemmas/unsplit-baseline-lemma-L.md`). **New this
  round:** Lemma M (B''-Banking Lemma, via the certified general Theorem 7)
  fully closes the "bank $B''$'s contribution" half of a proposed two-step
  mechanism; the natural "add the two banked bounds" combination step (the
  Candidate Swap Lemma) is **refuted** by an exact counterexample, ruling out
  an entire family of future attempts; Level-Absorption is now reduced to a
  single clean, budget-correct $k=2$ base case (numerically supported,
  unproved). Both certified,
  `lemmas/level-absorption-banking-lemma-and-swap-refutation.md`.
- Documented dead ends (do not retry): see round-7/8 lists, plus (round 10)
  the Candidate Swap Lemma (structure-agnostic swap/replacement bounds for
  Level-Absorption).
- Genuinely open: the Branch-I.A-restricted window in general (only its left
  endpoint and gap (b)(i) are settled; gap (a) is reduced but not closed;
  gap (b)(ii) untouched); the general (non-tail-untouched) middle regime
  `μ≤b_1<2^{m-1}`; Level-Absorption (now isolated to a single $k=2$ base
  case, still unproved).

**Upper-bound direction (no LB partition beats $c(n)$):**
- The entire slack-budget regime `k≤n` is closed unconditionally.
- Within the balanced region, Theorem 11/12 (Subset-Tie, Generalized
  Subset-Tie) narrow the residual, but a genuine finding (round 8) is that
  the survivor rate of best-of-named-additive-tools does **not** shrink to
  zero as `n` grows.
- `global-lp-vertex-sufficiency`'s LP/compactness route (opened round 8)
  proved the Global Vertex Lemma and Lipschitz continuity (both certified),
  giving existence of a maximizer. Concavity of $V(p)$ was retired (round 9,
  genuine counterexample). The concavity-free Finite-Cell Affine-Vertex
  Reduction Theorem's round-9 gap (candidate list $L$ missing $p_k$) is
  **fixed and reviewer-verified this round**: adding $p_k$ restores
  boundedness, Lemmas 4.1/4.2 are unaffected. **New this round**: the entire
  region-only candidate sub-list $Q_{\mathrm{region}}\subset Q$ is now fully
  classified (Region-Vertex Classification Theorem, exact vertex count/sign
  pattern for every $n\ge2$) and fully closed ($V(q)\le c(n)$ exactly at
  every such $q$, via a Boundary Continuity Theorem for the degenerate face
  plus exact $k$-Anchor-Merge evaluation at the genuine vertices) — certified
  `lemmas/finite-cell-vertex-reduction-and-region-classification.md`. The
  remaining obstruction (the $\Sigma$-shape part of $Q$, and no bound on
  $|\Sigma(n,k)|$ as a function of $n$) is unaddressed and is a combinatorial
  classification problem, not further missing machinery.
- `lp-duality-split-polytope`'s Multi-Piece Necessity Theorem for the
  triangular family remains complete (all `idx`, all `n≥3`, certified
  round 8). Round 9 found natural 2-piece constructions fail to close this
  family for $n\ge6$. **New this round**: a **Multi-Piece Sufficiency
  Theorem** — an explicit, uniform, all-$n\ge3$ construction using the full
  cut budget (splitting $n$ of the $n+1$ landmarks) *does* close the
  triangular family to $\mathrm{OddSum}=\tfrac12+\tfrac12(c(n)-\tfrac12)<
  c(n)$, exact arithmetic throughout, certified
  `lemmas/multi-piece-sufficiency-triangular-family.md`. This completes a
  full Necessity+Sufficiency picture for the triangular family specifically
  (single-piece responses never suffice; a genuinely multi-piece response
  using the whole budget always does) — it does not resolve the general
  upper-bound direction (this family's landmarks are AP-structured, a
  special feature; a numerical check confirms the analogous construction
  does not work on LB's own geometric partition).

**Open (the two remaining gaps, both narrowed again this round):**
1. **Lower bound, general case.** The Branch-I.A-restricted window is now
   **fully closed at $\ell=1,2,3,4$** (round 12: General Theorem GT($m$)
   for gap (a), Window Reduction Theorem for gap (b) in full including the
   previously-open (b)(ii)); **general $\ell\ge5$ remains open**, gated on
   extending GT($m$) past $m=3$ (a self-similar recursion, identified but
   not completed) and on endpoint-optimality among all $D$ at higher $m$.
   As of round 17, within GT($m$)'s own $r=0$ recursion, Sub-case (i)
   ($q=1$ after a $q=0$ descent) is closed for even excess $e\ge2$ (full
   $a_1$ range) and for both parities' width-1 window at $e\ge1$, but
   **not** for odd excess $e\ge1$ outside that window (concretely open at
   every $k\ge2$, $e=1$) — a corrected, narrower residual than round 17's
   own claimed "$e=0$ only," found by the reviewer; combined with the
   already-known $e=0$ sliver and `Case-B(m,k)`'s own sliver.
   The general middle regime `μ≤b_1<2^{m-1}` remains open; Level-Absorption
   (isolated to a single $k=2$ base case via Lemma M plus a refutation of
   the natural combination mechanism) is untouched this round, still
   unproved.
2. **Upper bound, general case.** The "large gaps everywhere" sub-case of
   the balanced region. `global-lp-vertex-sufficiency`'s LP/compactness
   route has a fully proved existence-of-maximizer step, a fully proved
   concavity-free finite-candidate reduction, and a fully closed
   region-only candidate sub-list; the sole remaining obstruction is the
   $\Sigma$-shape part of the candidate set (a combinatorial classification
   problem: no bound on $|\Sigma(n,k)|$ as a function of $n$). Round 12
   ruled out two more proposed bypasses (fixed-vertex path-monotonicity;
   the transplanted $e_0$-construction), and `lp-duality-split-polytope`'s
   new Perfect-Tie-Family Characterization gives a second, independent,
   disjoint-technique negative result at $e_0$ specifically — three
   separate lines of evidence now converge on "no bounded named-tool
   construction family suffices at $e_0$," reinforcing that
   `global-lp-vertex-sufficiency`'s own reduction-side route (closing the
   $\Sigma$-shape classification, or a genuinely $p$-dependent
   boundary-endpoint argument) is the more promising path, not further
   search for a bounded construction.

## Full proof
(none — Status is `partial`; see "Current best" for exactly what is proved
and the precisely-narrowed open gaps above.)
