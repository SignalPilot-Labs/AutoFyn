## Status
solved

**(Round 19, second-pass proof-review: `pigeonhole-subset-sum-upper-bound`'s Case A fix,
applied by this round's second builder in response to the first-pass review's precisely
scoped gap, has been independently re-verified from scratch — symbolically, computationally,
and by two fully independent end-to-end numerical checks of the actual game against the
final answer — and found gap-free. The theorem is SOLVED: `c(n)=2^n/(2^{n+1}-1)` for every
positive integer `n`. See `## Full proof` below and the second-pass verification note at the
end of `## Approaches tried`.)**

## Approaches tried
- `pigeonhole-subset-sum-upper-bound` — **(round 19, SECOND PASS — proof-reviewer independent
  re-verification of the Case A fix. Verdict: APPROVE. Status raised `partial`→`solved` for the
  entire theorem.)** The first-pass review this round found one real gap: Case A's WLOG sentence
  "replace `\varepsilon^*` by `-\varepsilon^*` throughout... without changing `M`" is false
  whenever `M\ne0` (witness `X=(10,9,9)`). A second build applied the reviewer's exact specified
  fix: dropped the WLOG sentence; set `s:=\varepsilon^*(x^*)` to `x^*`'s **actual**, un-normalized
  sign (no case split on `P`/`N` membership); assign the merged token `x^*-y` the sign `s`; derive
  `V(\varepsilon')=V(\varepsilon^*)=M` as one line of pure algebra holding **verbatim** for either
  `s=+1` or `s=-1`, no WLOG needed. **This second-pass review independently re-verified the fix is
  correct and complete, with fresh work not reusing the builder's or the first pass's own scripts:**
  (1) **Re-derived the one-line identity symbolically from scratch** (`sympy`, treating `s` as a
  free symbol, not substituting `\pm1`): `M=\Sigma_{\rm rest}+s(x^*-y)` solved for `\Sigma_{\rm rest}`
  and substituted back into `V(\varepsilon')` simplifies to exactly `M`, confirming the identity is
  genuinely sign-agnostic (no hidden case split, no dropped case) — matches the file's derivation
  exactly. (2) **Wrote an independent, from-scratch verification harness** (`/tmp/round-19-review2/
  fresh_verify2.py`, not derived from either the original builder's `/tmp/round-19-build/` or the
  fix-builder's `/tmp/round-19-build-2/` scripts): re-implements the algorithm literally as newly
  written (global max, actual sign `s`, arbitrary opposite-sign partner, same-sign sub-lemma
  peeling), with an independent brute-force `OPT` oracle and a per-step optimality-invariant check.
  Ran `2{,}095+` fresh exact-`Fraction` trials — the exact witness `X=(10,9,9)` and all `6`
  permutations across `5` random tie-break seeds each (`30` checks, the specific branch that broke
  the old prose: global max `10` carries sign `s=-1`) — **PASS**; wide random integer sweep sizes
  `1`-`13` (`500` trials); tie-heavy small-alphabet (`400`); zero-heavy (`300`); fractional-valued
  (`300`); all-same-value (forces the same-sign degenerate sub-lemma branch heavily, `150`); larger
  sizes `14`-`15` beyond the fix-builder's own tested range with the invariant check confirmed
  separately (`15`); `5` explicit edge cases (`p=1`, all-zero, tied pair, zero pair); `3` independent
  random-tie-break repetitions (`600` more). **`0` failures, `0` invariant violations, `0` "stuck"
  states anywhere.** (3) **Independently re-verified the "unmerge" contradiction argument** (the
  actual optimality-preservation mechanism) composes correctly with the fixed Case A: it is phrased
  purely in terms of an arbitrary `\tau:=\varepsilon''(x^*-y)\in\{\pm1\}`, never references `s` or
  the fixed prose's claimed value of `M`, and was textually unchanged by the fix — confirmed by
  direct symbolic re-derivation (`V(\varepsilon''')=\tau x^*+(-\tau)y=\tau(x^*-y)=V(\varepsilon'')`,
  giving a same-magnitude signing of the original `X`, contradicting `M=\mathrm{OPT}(X)` if
  `M'<M`) — no gap, no silent reliance on the old flawed claim. (4) **Grepped the whole file for
  stale references** to the old `i^*\in P`/`j\in N` framing: only the historical review-note/
  addendum sections (correctly retained, clearly labeled as history) still mention the old
  sentence; the live Full-proof text and the Remark are fully migrated to the sign-agnostic
  `s`/`y` framing with `\varepsilon^*(y)=-s`, no inconsistency found anywhere it is actually used.
  (5) **Independently re-checked the sub-lemma's own internal "WLOG `P`=all; `N`=all is identical
  after negating" step is a genuinely different (and valid) kind of move** from the earlier flawed
  one: the sub-lemma's `M` there is `\mathrm{OPT}(X)`, a sign-independent *magnitude*, and negating
  `\varepsilon^*` trivially preserves `|V(\cdot)|` (a true fact, unlike the earlier bug which
  conflated preserving the *magnitude* under negation with preserving a specific *signed* value
  `V(\varepsilon^*)` that a downstream algebraic identity needed exactly) — no analogous gap here.
  (6) **Full end-to-end retrace of the whole chain** (Step 1 Pigeonhole Margin Lemma, re-derived and
  independently spot-checked again this pass, `640` fresh trials sizes `1`-`8`, `0` failures; Step 2
  both cases, as above; Step 3 Combination; Step 4 Conclusion + citations of the already-certified
  Lemma D/M, Slack Collapse, and the lower bound `all-cycles-resolution.md`+
  `superincreasing-no-early-zero.md`, all confirmed present in `lemmas/` and correctly certified in
  prior rounds) found no other loose thread. **(7) Two independent, from-scratch end-to-end
  numerical validations of the actual final answer against the real (continuous) game — not just
  internal proof-machinery consistency:** for `n=1`, implemented a genuine backward-induction
  alternating-claim solver plus a grid search over Liu Bang's opening point and Xiang Yu's single
  response cut, with no dependence on Lemma G or any of the proof's algebraic apparatus (only a
  from-scratch spot-check that greedy matches backward induction on `20` random small cases) —
  best guaranteed value found `\approx0.6666` at opening point `p\approx0.667`, matching the claimed
  `c(1)=2/3` to grid resolution; for `n=2`, a similar from-scratch two-cut backward-induction/grid
  search confirms that at the specific dyadic-shaped opening `(4/7,2/7,1/7)`, Xiang Yu's best
  response (searched over a fine grid of one- and two-cut strategies) yields exactly `4/7`, matching
  the claimed `c(2)=4/7` exactly, with nearby openings giving strictly worse values — independent
  confirmation of the final answer from outside the proof's own framework. **Conclusion: no
  remaining gap found after a genuinely adversarial, independent re-attempt to break the fix. The
  proof is complete and rigorous: every case is settled (Case A exhaustive over `s\in\{\pm1\}` with
  no case split needed, Case B via the sub-lemma, both exhaustive by construction), every theorem
  invoked is named and correctly cited, and the final answer `c(n)=2^n/(2^{n+1}-1)` is stated
  explicitly and verified by direct substitution (`n=1,2`) plus the general recursion — satisfying
  the `compute_and_prove`/`answer_type: expression` requirement.** **Status raised to `solved` for
  the entire theorem** (both the upper bound constructed by this slug and the already-certified
  lower bound). Verification scripts: `/tmp/round-19-review2/fresh_verify2.py` (`2{,}095+` fresh
  `Fraction` trials, `0` failures), `/tmp/round-19-review2/verify_lemma1.py` (Pigeonhole re-check,
  `640` trials, `0` failures), `/tmp/round-19-review2/verify_n1_n2.py` (`n=1` independent brute-force
  grid search), `/tmp/round-19-review2/verify_n2.py` (`n=2` independent brute-force grid search).
  **Certified the Signed-Sum Realizability Lemma** (§2 of the approach file, now gap-free) into
  `lemmas/signed-sum-realizability.md`.
- `pigeonhole-subset-sum-upper-bound` — **(round 19, new slug, proof-reviewer independent
  re-verification — builder claimed `solved` for the ENTIRE theorem; REJECTED, Status corrected to
  `partial`.)** This slug was opened round 19 (plateau-break mandate) around a genuinely different,
  non-recursive route: pigeonhole on `2^k` subset sums (Step 1, elementary, solid) + a "Signed-Sum
  Realizability Lemma" turning the pigeonhole witness into a legal D/M-merge sequence (Step 2). The
  outline-reviewer had already falsified the explorer's original Step 2 mechanism (counterexample
  `X=(36,48,4)`) before build. This round's builder found a DIFFERENT, structurally sound mechanism
  (merge the global max against any opposite-sign partner under a fixed optimal signing; an "unmerge"
  contradiction shows optimality is preserved) and claimed a complete proof, raising Status to `solved`
  for the whole theorem (upper bound via this route + already-unconditional lower bound). **Independent
  review found the underlying Lemma is very likely TRUE (re-derived it myself from scratch, and
  independently stress-tested up to 10,000+ fresh `Fraction` trials, sizes 1-20, tie/zero-heavy/large-
  value cases, `0` failures) but the WRITTEN PROOF of Case A contains a genuine false claim**: the
  WLOG step "replace `\varepsilon^*` by `-\varepsilon^*` throughout... without changing `M`" is false
  whenever `M\ne0` (negation flips the *signed* value `V(\varepsilon^*)` from `+M` to `-M`, it does not
  preserve it) — concretely demonstrated on `X=(10,9,9)`, where the (essentially unique) `V=+8`-normalized
  optimal signing puts the global max (`10`) on the `-1` side, triggering the flip, and the flip does
  give `V=-8\ne+8`. This is a real rigor gap (a stated-and-used false claim), not a hand-wave. **Crucially,
  it does NOT actually break the theorem**: the specific numeral choice the proof hardcodes for the merged
  token's sign (`+1`) happens to be exactly right regardless (it matches `x^*`'s true post-flip sign), and
  the "unmerge" contradiction argument that does the real optimality-preservation work is purely
  magnitude-based and never uses the mislabeled signed value — so the actual algorithm (which the
  builder's own saved code correctly implements as `newsign = xstar_sign`, NOT the hardcoded `+1` the
  prose literally describes) always produces the true optimum. **The fix is a small, precise rewrite**
  (drop the WLOG sentence; set `\varepsilon'(x^*-y):=s:=\varepsilon^*(x^*)`, the actual current sign,
  and re-derive `V(\varepsilon')=V(\varepsilon^*)` directly, sign-agnostic — given in full in the
  reviewer's note appended to the approach file), not a new mechanism. Everything else (Step 1 pigeonhole,
  the "same-sign forces a zero" sub-lemma, Case B, Step 3 combination, Step 4/final-answer verification,
  all citations of Lemma D/M / Slack Collapse / the lower bound) was independently re-checked and found
  correct. **Verdict: CHANGES REQUESTED, Status corrected `solved`→`partial`.** This is very close to a
  complete proof of the entire theorem's upper-bound direction — the fix is small and the mechanism is
  independently confirmed sound — but per CLAUDE.md's rigor rules a proof containing a stated false claim
  is not yet `solved`, regardless of how easily it repairs. **This is now the single highest-priority item
  for next round**: apply the one-paragraph fix in the reviewer's note, re-verify, and if it holds up this
  slug would close the ENTIRE theorem (both directions) in one round. Full detail (exact fix, counterexample,
  computational re-verification) appended to `approaches/pigeonhole-subset-sum-upper-bound.md`.
- `potential-weighting-upper-bound` — **(round 19, proof-builder §33-§34, proof-reviewer independent
  re-verification, CHANGES REQUESTED — Status confirmed `partial`, real closure of a named sub-target.)**
  Dispatched to close round 18's exact flagged gap: the KEEP `b0<=w1` sub-case of Two-Touch at `|W|=3`
  (target `(*)`: `w1-ThreeTouch(b0,rest) >= TwoTouch({b0},W)` at `|rest|=2`). **New §33 proves this in
  full** via a new **Two-Variable Reflection Bound** (`w1-|b0-w|>=|b0-(w1-w)|`, `0<=b0,w<=w1`, 3 exhaustive
  cases) plus a 5-term case analysis (one term per `ThreeTouch` candidate: `A_1`..`A_5`, the hardest —
  `A_4` match-term and `A_5` keep-all-three term — each needing a further 2-4-way sub-split). **Independently
  re-derived and re-verified by this review**: hand-checked the Reflection Bound's 3 cases and spot-checked
  the `A_4`/`A_5` sub-case algebra by hand; independently re-implemented `TwoTouch`/`ThreeTouch` from
  scratch (not reusing the builder's code) and ran 30,000 fresh integer trials + 20,000 fresh fractional
  trials against both the Reflection Bound and the full target `(*)` — `0` failures throughout, confirming
  the builder's own 462-tuple exhaustive grid + 19,894-trial sweep (also `0` failures) and both negative
  controls (100% failure when a hypothesis is dropped). **§33.5's assembly into "Two-Touch fully,
  unconditionally proved for `|W|<=3`" is correct and non-circular**: traced every ingredient explicitly
  (Empty-Background Lemma for `C=\emptyset`; certified `|W|<=2` base case + Three-Bound Domination for the
  DELETE branch's induction hypothesis; the unconditional `b0>w1` KEEP formula §26.5(c); this round's new
  `(*)` for the `b0<=w1` KEEP sub-case; `match-branch-domination-via-per-partner-domination.md`'s MATCH
  bound with its Per-Partner-Domination dependency correctly discharged at the already-certified `q<=3`)
  — this is genuinely, rigorously the exact missing piece round 18's reviewer identified and rejected, now
  supplied. **§33.7's own scope-discipline note (does NOT extend to `q>=4`, does NOT close Per-Partner
  Domination/Three-Touch's MATCH branch/Gap 1b/1c) is accurate, no overclaim found.** §34 (Generalized
  Touch-Bound Lemma, `|C|=2` attempt) is honest partial/negative progress as reported (one shortcut
  falsified 12.2%, a shape census, a "not independently easier" structural diagnosis) — no overclaim.
  **Certified `lemmas/two-variable-reflection-bound.md`** (general, standalone, reusable). Updated
  `lemmas/match-branch-domination-via-per-partner-domination.md`'s scope note to record that its previously-
  flagged missing dependency is now discharged (Two-Touch `|W|<=3` is genuinely closed). **Net: real,
  independently-verified progress — a concrete named sub-target closed for good, correcting round 18's
  overclaim with an actual proof this time, plus one new certified general lemma.** Status correctly stays
  `partial` for the whole theorem (general-`q` Per-Partner Domination, Three-Touch's own MATCH branch, Gap
  1b/1c all remain open) — route CHANGES REQUESTED.
- `potential-weighting-upper-bound` — **(round 18, proof-reviewer independent re-verification of §30,
  CHANGES REQUESTED — Status confirmed `partial`, one genuine overclaim caught and corrected, real new
  content retained.)** Independently re-derived §30.1's 3-line "Match-Branch-Domination-via-Per-Partner-
  Domination" proof from scratch (F1 DELETE-branch domination, F2 trivial candidate-list membership, F3
  Per-Partner Domination `q<=3` — all re-checked, all correct; the induction-level/non-circularity trace
  at `|W|=3` is correct) — **`MATCH_j >= min(A1,D_j) >= TT` is genuinely proved**, conditional on Per-
  Partner Domination at the relevant `q`, and Two-Touch's MATCH branch is genuinely no longer independent
  open content (retiring it as a separate line item is correct). **But the file's headline claim — "Item
  1: CLOSED … Two-Touch fully proved for `|W|<=3` unconditionally" — is an OVERCLAIM.** The Corollary
  additionally needs the KEEP branch's `b0<=w1` sub-case at `|W|=3`, for which the file cites "Lemma B
  (Three-Touch base case) already proves it unconditionally" — **this is a non sequitur**: Lemma B proves
  the *value* `OPT_{-1}({b0},rest)=ThreeTouch(b0,rest)` for `|rest|<=3`, not the actually-needed
  inequality `w1-ThreeTouch(b0,rest) >= TwoTouch({b0},W)`. That inequality is a *different* claim, which
  the file's own §27.2(d) (round 17) had explicitly logged as "corroborated `0/1,239`, not proved" — §30.1
  silently treats it as already discharged by Lemma B. Independently re-tested the underlying inequality
  with fresh code (`/tmp/check_gap*.py`): `0` failures across `>14,000` combined trials (random,
  exhaustive small-grid, true-brute-force-`OPT` cross-check, and a wide-value-range sweep to `vmax=500`
  per the round-13/24 "widen past the builder's tested range" lesson) — the claim is very likely TRUE but
  is **not proved anywhere on file**. **Certified only the narrowed Lemma** (`MATCH_j>=TT` conditional on
  F3, without the "Consequently Two-Touch fully proved for `|W|<=3`" clause) to
  `lemmas/match-branch-domination-via-per-partner-domination.md`; rejected the bundled Corollary clause as
  submitted. **§30.2 (Three-Touch MATCH Sibling-Domination) and §30.3 (Gap 1c case (a)) — no overclaim
  found, honestly reported open.** Re-ran 9 of the 16 saved `/tmp/round-18-build/` scripts directly:
  fixed-seed scripts (`t_gap1c_free.py` `148/944`, `t_verify_301.py` `0/400`+`0/625`, `t_verify_F3.py`
  `0/1,837`+`0/9,375`, all three `t_final*.py` numbers incl. `delta_d` `0/949`, `h_d` even `949/949`,
  `delta_c<0` `876/949`, bound-(i) fails `285/419`, bound-(ii) fails `206/419`) **reproduced EXACTLY**;
  unseeded scripts (`t4_union.py`, `t5_general_B.py`, `t7_match2.py`, `t9_wide_sweep.py`) reproduced within
  expected random-reseed variance, same order of magnitude, same conclusion. **No fabricated number found
  — the builder's claim to have actually run its verification scripts before finalizing is substantiated.**
  §30.2's three refuted proof-route candidates (union-of-three-candidates, general-background-size
  induction, second-largest-partner shortcut) all independently confirmed refuted, no missed salvage
  route found. **Net: real new content (MATCH branch of Two-Touch reduces exactly to Per-Partner
  Domination, no longer independent), one real overclaim caught and corrected (the `|W|<=3` Corollary is
  NOT unconditionally proved — the KEEP `b0<=w1` sub-case at `|W|=3` remains an open, strongly-
  corroborated inequality), §30.2/§30.3 honestly open with no issues. Status correctly stays `partial`.**
  Full detail in `approaches/potential-weighting-upper-bound.md` §29-§30; narrowed lemma certified in
  `lemmas/match-branch-domination-via-per-partner-domination.md`.
- `potential-weighting-upper-bound` — **(round 17, proof-reviewer independent re-verification of
  §28, CHANGES REQUESTED — Status confirmed `partial`, no fatal flaw found, real new proved content.)**
  Independently re-derived and/or re-tested every load-bearing claim of §28 from a fresh, from-scratch
  harness (`all_selections`/`OPT_sigma`/`e()` re-implemented independently, validated first against the
  file's own worked examples) — not reusing the builder's or explorers' code, then cross-checked against
  the builder's own saved scripts in `/tmp/round-17/verify_builder/` and `/tmp/round-17/gap1c_probe/`,
  all of which reproduced the file's cited counts exactly (`0/6000`, `0/956`, `0/3000` (basecase),
  `0/3000` (basecase3), `0/1854`+`0/3000` (keep-identity), `0/4475`+`0/2337` (MATCH/KEEP h=0
  threetouch_induction), `55/3000` incl. the exact cited counterexample (match_idea refutation)).
  **(1) Gap 1c case (b) — both witnesses reproduced bit-for-bit.** `B1={16,15},Res=(11,10,9,6,3)`,
  `d=1,X=(9,6,3)`: `OPT_{+1}(\{16,15,1\},(9,6,3))=2`, sparsest nonempty optima `{3,3}` and `{6,6}` (tied
  with `∅`), confirmed by direct brute force. `B1={2,2},Res=(24,23,18,12,6)`, `d=1,X=(18,12,6)`:
  `OPT_{+1}(\{2,2,1\},(18,12,6))=1`, exactly 3 optima (`∅`, `{6,6}`, `{12,12}`), confirming `{6,6}` is a
  genuine, sparsest-nonempty duplicate-pair optimal witness and `e(\{2,2,1,6,6\})=1` matches via Lemma P
  — both witnesses genuine, non-vacuous, correctly extracted from real `𝓕`-provenance instances (the
  extraction script enforces the true global-argmin trigger, not merely a local one — no
  sampler-bug regression of the two recurring patterns in `/tmp/memory/run_state.md`/`proof-reviewer.md`
  Rules). **(2) Lemma A (Max-Element Triple Identity) — CERTIFIED**, re-derived by hand in one line,
  trivial and fully general, no scope issue. **(3) Lemma B (Three-Touch base case `|W|≤3`) —
  CERTIFIED.** Re-derived the "keep-all-three" 4-case domination argument symbolically by hand (each of
  the 4 cases' algebra checked independently, including the two sub-cases of case 1 and the exact
  boundary consistency) — matches the file's proof line for line, no gap. Additionally ran a genuinely
  **exhaustive** (not sampled) check over `c,w1,w2,w3∈{0,…,7}` (`4096`/`4096` instances, all ties and
  orderings) comparing `OPT_{-1}(\{c\},W)` (independent brute force) against the closed form — `0`
  mismatches, plus `8000` random trials across `|W|∈\{0,1,2,3\}` — `0` mismatches. **(4) Three-Touch's
  DELETE, KEEP `h=1`, and KEEP `h=0` branches (§28.4(b)-(d)) — re-derived symbolically and independently
  spot-checked at sizes `|W|∈\{4,5,6\}` using the TRUE recursive `OPT` (not the unclosed IH) for the
  DELETE and KEEP sub-problems: `0/1200` failures of "branch value `≤` ThreeTouch" for all three
  branches simultaneously, plus a trichotomy sanity check (`max(DELETE,KEEP,MATCH)=true OPT`) holding in
  every trial, cross-validating both my harness and §13.2's peeling-trichotomy framework. The
  DELETE-branch argument (candidate-list containment, `ThreeTouch(c,W\{u1})≤ThreeTouch(c,W)`) is
  elementary and correct; KEEP `h=1`'s `c-u1+u2=e(\{c,u1,u2\})` (Lemma A) is correct with genuine
  equality; KEEP `h=0`'s three Lemma-A applications (touch-1, touch-2, touch-3 terms) are each correct
  with equality. **The claimed "genuine mutual/joint induction with Two-Touch" for KEEP `h=0` is
  verified well-founded, non-circular:** traced Two-Touch's own open `b0≤w1` KEEP sub-case (§26.5(d),
  needs an upper bound on `OPT_{-1}(\{b0\},rest)` i.e. exactly Three-Touch's hard direction) and
  Three-Touch's `h=0` KEEP sub-case (needs `OPT_{+1}(\{c\},rest')` i.e. exactly Two-Touch's hard
  direction) — both recursive calls are at the SAME strictly-smaller size `|W|-1`, in both directions,
  confirming no circularity in the cross-dependency. (This does **not** mean either mirror is closed at
  any concrete `q>3` — both still need MATCH closed at every intermediate size too, which the file
  honestly discloses.) **(5) MATCH-idea refutation (§28.4, end) — reproduced exactly**, including the
  literal counterexample `b0=5,W=(8,10,8),wj=8`: `d=2`, `TwoTouch(\{5\},\{8,2\})=1<3=
  TwoTouch(\{5\},\{8,10,8\})`, `55/3000` failures of the proposed reduction, `0/3000` for the free
  (always-true) inequality sanity check — correctly ruled dead, do not re-attempt.
  **(6) One genuine rigor concern found, not fatal — flagged for the next round.** §28.4's closing
  claim that the MATCH-branch mechanism is "now confirmed to be the shared bottleneck for four distinct
  manifestations" **overstates what is actually proved.** Gap 1a/Gap 1b's DELETE-vs-**KEEP** equivalence
  (§27.1) IS a genuine, explicit 3-line algebraic reduction (re-checked, correct) — but no analogous
  explicit reduction is given for the DELETE-vs-**MATCH** half: Two-Touch's own MATCH branch and
  Three-Touch's own MATCH branch are not even the same shape of statement (the file's own §27.2(d) notes
  a genuine, newly-discovered min/max **asymmetry** — Two-Touch needs touch-depth `≤2`, Three-Touch
  needs touch-depth `≤3` — so they cannot be "the same lemma" without further work relating them). The
  "single shared bottleneck, confirmed" language should be softened to "a recurring open sub-problem of
  the same flavor across four instances, not yet proved to be a single reducible lemma" unless a future
  round supplies the missing explicit reduction (mirroring §27.1's KEEP-half derivation). This is a
  framing/rigor issue in the write-up, not a mathematical error — no proved claim in §28 is false, and
  Status is correctly NOT overclaimed to `solved`.
  **Two precision-note fixes (§28.1, §28.2) — verified consistent everywhere they are actually used
  in live proofs** (§27.1's chain-threaded quantifier; §26.3/26.4/27.3's "AUGMENTED-optimal witness"
  reading of `ξ*`, confirmed by re-reading each live usage in context). Two historical/dead-end mentions
  of the old ambiguous "LHS-optimal" phrasing remain unedited at lines ~5877/5886 (by the project's
  own "append, don't rewrite" convention) — read in their surrounding context they are not actually
  mathematically ambiguous (both describe the augmented-problem's witness), but a forward-pointer to
  §28.2 would make this airtight; a minor clarity nit, not a correctness gap.
  **Verdict: CHANGES REQUESTED.** Genuine, independently-verified new content this round (Lemma A,
  Lemma B, 3 of 5 Three-Touch branches, 2 explicit Gap-1c witnesses, 1 refuted idea) — real advance, no
  overclaim of Status (`partial` confirmed correct). **None of Gaps 1a, 1b (general induction), 1c
  (case (a)) is closed; neither Two-Touch nor Three-Touch is fully closed (MATCH branch open in both) —
  Status correctly stays `partial`.** Full detail in `approaches/potential-weighting-upper-bound.md`
  §28; lemma certification in `lemmas/max-element-triple-identity-and-threetouch-basecase.md`.
- `potential-weighting-upper-bound` — **(round 16) Gap 1b's `rest=∅` base case is now a genuine,
  complete, independently-triple-re-verified PROOF (not a reduction); two new general lemmas
  certified in full (Insertion-Difference Identity; Delete-Suffices Insertion Domination); a
  previously-unnoticed, non-circular structural link between Gap 1a's Step 2 and Gap 1c's `ξ*=∅`
  boundary case discovered and proved; 3 of 5 structural sub-pieces of a new Two-Touch Lemma for
  Gap 1a fully proved. None of Gaps 1a, 1b (general induction), 1c is fully closed — Status
  correctly stays `partial`.** Reviewer independently re-verified every claim from scratch with a
  freshly-written harness (`/tmp/round-16/proof-reviewer-verify/`, not reusing the explorer's,
  outliner's, or builder's own code), validated against the file's own four worked `OPT_σ` examples
  first (all four reproduced exactly). **(1) Sum-Bound Base Case Lemma — CONFIRMED, proof re-derived
  by hand independently, no gap.** The reviewer's first attempt at an independent brute-force sweep
  produced 135 apparent "violations" out of 4,000 trials — traced to a bug in the reviewer's own
  harness (failing to require that `k*` be the actual global argmin of `A_{3,l}`, not merely satisfy
  `A_{3,k*}<A_1` in isolation); after fixing this, **0/4,473** violations across a fresh 20,000-trial
  sweep (mixed integer/rational alphabets, `v_max` up to 80) and the pure algebraic core independently
  re-verified symbolically (own from-scratch contradiction argument, matches the file's proof line for
  line) and computationally (**0/65,520** filtered trials). This is now the population's **fourth**
  independent confirmation (round-16 explorer, outline-reviewer, builder, and this review), all
  agreeing. Scope correctly restricted to `rest=∅` (`q=3`) only — the general `|Z_1|≥2` induction
  remains untouched, exactly as the file states; confirmed the `h=0`-only scoping is legitimate (the
  `h=1,h=2` sub-cases are already handled elsewhere, by the pre-existing certified Background-Splitting
  machinery — grep-confirmed, not a new gap). **(2) Insertion-Difference Identity — CONFIRMED, fully
  general.** Independently re-derived via Fact 3 + General Rank-Extraction Identity (same route as the
  builder's), `0/30,000` random (mixed-denominator rationals up to `v_max=200`) plus **`0/780`**
  genuinely exhaustive small-value grid (5-value grid including `1/2,3/2` to stress ties) — exact
  match with the file's own `0/780` exhaustive count. **(3) Delete-Suffices Insertion Domination —
  CONFIRMED, correct, appropriately scoped.** `0/8,688` genuine "deletion-suffices" trigger instances,
  `0` violations of the conclusion; negative control (dropping the hypothesis) gives `36.3%` failures
  (reviewer's own fresh instance family), confirming the hypothesis is load-bearing, consistent in
  substance with the builder's own `≈23%` negative-control figure (different sampling, same
  qualitative conclusion). **(4) The `ξ*=∅` boundary-case reduction (§26.3) — independently traced
  end-to-end and confirmed NON-CIRCULAR.** Verified precisely which quantity the Delete-Suffices
  lemma's hypothesis (`OPT_{+1}(C,W)=e(C)`) is instantiated against in this application (`C=B_1`,
  `W=Res=Z_1`, the FULL top-level residual, not the smaller `X`) and confirmed this is *exactly*
  Gap 1a's already-independently-tracked "Deletion-Suffices-for-`k*`" statement (§21.1 Step 2, proved
  for `q≤3` since round 14, open for `q≥4`) — a genuinely separate, previously-proved-independently
  conjecture, not something that secretly presupposes the half-step or Gap 1c. Built a fresh end-to-end
  harness (base generators → genuine trigger+global-`k*` node → test whether deletion-suffices holds
  at that node → when it does and `ξ*=∅` is the *unique* optimum of the RHS problem, check both the
  intermediate inequality `e(B_1)≤e(B_1∪\{d\})` and the full derived half-step conclusion
  `OPT_{+1}(B_1,X)≤OPT_{+1}(B_1∪\{d\},X)`): **0/175** violations of either, across `q∈{3,4,5}`. The
  well-definedness fix for `ξ*` (canonical choice: nonempty optimum if one exists among the optima,
  `∅` only if uniquely optimal) is a legitimate, exhaustive, non-overlapping case split — confirmed
  by construction, not merely asserted. **(5) Two-Touch Lemma's 3 proved sub-pieces — all CONFIRMED,
  including catching and fixing a second reviewer-side sampler bug.** Base case (`|W|≤2`, both
  `C=∅` and `C=\{b_0\}`) — confirmed trivial/certified-lemma-reuse, correct. DELETE branch — the
  candidate-set-inclusion argument re-traced, correct, no computation needed. **KEEP branch
  `b_0>w_1` sub-case** — the reviewer's first independent test produced widespread "mismatches";
  traced to a second sampler bug (failing to enforce `w_1=\max(W)`, i.e. allowing `rest` to contain
  elements exceeding `w_1`, violating the peeling formula's own implicit hypothesis); after enforcing
  this constraint, **0/3,000** mismatches — the formula `\text{KEEP}=b_0-w_1` is exactly correct.
  **(6) The 2 remaining open Two-Touch sub-pieces (KEEP branch `b_0≤w_1`; MATCH branch / "Match-Branch
  Domination") — confirmed genuinely open, not silently closed, and confirmed strongly corroborated**:
  own fresh Match-Branch Domination test, **0/12,734** violations (vs. the builder's `0/7,265`+
  `0/15,958`) — consistent, real support, but honestly reported as unproved, matching the file. **(7)
  The dead-end `|C|=2` general Two-Touch formula — reconfirmed FALSE**, own fresh test: **962/3,000
  (32.1%)** failures — same order of magnitude and conclusion as the file's `~24%`/outline-reviewer's
  `18.0%` (benign sampling-shape differences, not a discrepancy), confirms this really is a hard
  structural wall correctly *not* used anywhere in the proved sub-pieces. **No overclaim found
  anywhere in §25/§26** — every "proved" claim is genuinely proved (re-derived independently by hand
  where algebraic, and computationally corroborated where the proof is definitional/logical), every
  "corroborated, not proved" claim is honestly reported as such, and the Status/§26 summary sentence
  ("None of Gaps 1a, 1b (general induction), 1c is fully closed... Status correctly stays `partial`")
  matches reality exactly. **Certified all 3 new lemmas as submitted, no changes needed:**
  `lemmas/sum-bound-base-case.md`, `lemmas/insertion-difference-identity.md`,
  `lemmas/delete-suffices-insertion-domination.md`. **Net verdict: a strong, well-verified round — a
  genuine complete proof of a real sub-case (Gap 1b's base case), 2 new general reusable lemmas, one
  previously unnoticed and non-circular link between two open gaps, and 3/5 of a new lemma's structural
  pieces fully closed — but SAR/Claim A's central mechanisms (Gap 1a's general-`q` induction, Gap 1c's
  nonempty-`ξ*` construction, Two-Touch's 2 remaining sub-pieces) all remain open. Status correctly
  stays `partial`, route CHANGES REQUESTED.**
- `potential-weighting-upper-bound` — **(round 15) All 4 outline-review action items addressed;
  none of Gaps 1a/1b/1c closed, but real, precisely-scoped progress on every item, including a
  resolved cross-round discrepancy and 3 new certified general lemmas.** Reviewer independently
  re-verified every claim from scratch, own fresh code (`/tmp/round-15/verify_reviewer/`, not
  reusing the builder's, outliner's, or outline-reviewer's harnesses), validated against the file's
  own four worked examples first (`OPT_{+1}([5,8],(10,8,7,2))=0`, `OPT_{-1}(\cdot)=10`,
  `OPT_{+1}([1],(10,8,7))=0`, `OPT_{-1}([2,4],(5,3))=4`, all reproduced exactly). **(1) The
  contested `\sim15\%` "argmin dropped one level deeper" claim (§23.1) — CONFIRMED not reproduced;
  the outline-reviewer's finding is CORRECT, the builder's re-verification is CORRECT.**
  Independently built genuine `\mathcal F` base generators (real trigger `M<A_1`, real global
  argmin `k^*`) and tested the half-step against **every** second-level match partner at
  `q=5,6,7`: `0/906`, `0/441`, `0/252` violations respectively (`1{,}599` combined checks, smaller
  scale than the builder's `15{,}175` but the same qualitative result, zero exceptions, minimum
  margin exactly `0`) — independently corroborates both the builder's and the outline-reviewer's
  finding from a third, differently-coded harness. Also independently reproduced **both** of the
  builder's diagnostic negative controls: testing against the wrong background root `B_0` instead
  of `B_1` gives `11\%$–`38\%` violations (my own fresh run: `q=5$: `38.5\%`, `q=6`: `33\%`, `q=7`:
  `11\%`); dropping the top-level trigger gives `13\%$–`20\%` violations (`q=5`: `17\%`, `q=6`:
  `20\%`, `q=7`: `14\%`) — both independently land in the same order-of-magnitude ballpark as
  §23.1's originally-reported `\sim15\%$ figure, strongly corroborating the builder's diagnosis
  that the original figure was a scoping/provenance artifact, not a real mathematical fact. **The
  half-step's hypothesis simplification (dropping the recursive second-level-argmin requirement) is
  therefore justified and correctly, honestly scoped** — the file is explicit this is a scoping
  correction, not a proof of the half-step itself, which remains open. **(2) `q=4`'s DELETE/KEEP
  free, MATCH not free — CONFIRMED exactly, including the diagnosed root cause.** Independent
  from-scratch `q=4` sweep (`10{,}500` genuine `(b_0,Z_0,l)` checks, a differently-structured
  brute-force computation of DEL/KEEP/MATCH than the builder's own closed-form derivation):
  `0/10{,}500` DEL-family-certification failures, `0/10{,}500` KEEP-family-certification failures,
  `72/10{,}500` (`\approx0.69\%`) MATCH-family-certification failures — matches the builder's own
  `439/62{,}580$ (`\approx0.70\%`) rate almost exactly, an independent reproduction at a different
  sample size. **Every one of the `72` MATCH failures** was confirmed to occur exactly when
  `A_1<\min(\text{simple bound family})` (`72/72`), independently confirming the builder's exact
  root-cause diagnosis. Also confirmed the TRUE target (`A_{3,l}\ge\min(A_1,D_l)`, using the real
  `A_1`, not a family proxy) holds in **all** `10{,}500` checks — not a counterexample to the
  underlying Per-Partner Domination Lemma, exactly as the builder states. **Three-Bound Domination
  Lemma** — independently re-derived the 3-case symbolic proof from scratch (case-split on the rank
  of `x` among `\{x,y,z\}`) before reading the builder's version, matches exactly; `200{,}000/200{,}000`
  fresh random trials, `0` violations. **CERTIFIED**, together with the Keep-Top Bound, in
  `lemmas/three-bound-domination-and-keep-top-bound.md`. **(3) Gap 1b's base case — CONFIRMED
  reduced but NOT closed, exactly as reported; no overclaim.** Independently re-derived both new
  facts from scratch: the **Keep-Top Bound** (`OPT_{+1}(C,W)\le w_1-|c_1-c_2|$ at `h=0`) — one-line
  proof re-checked, correct; **exact `q=3` dichotomy** (`M=\min(D_{k^*},w_1-D_{k^*})` exactly, since
  a singleton residual has only two candidate selections) — re-derived, correct. Independently
  built genuine `q=3$, `h=0`-triggered base generators (`308$ instances out of `1{,}728` triggered,
  `v_{\max}\in\{1,\dots,50\}`): **`0/308`** Keep-Top-Bound violations, **`0/308`** dichotomy-formula
  mismatches, and `M=D_{k^*}` (DELETE beats KEEP, i.e. the base case holds) in **`308/308`**
  instances — corroborates, but as the file honestly states, does not prove, the still-open base
  case. Independently re-derived the file's one forced-consequence lead symbolically (assuming
  `w_1<2D_{k^*}$, combining the free bound `A_1\le|b_0-w_1|=w_1-b_0` (using `w_1>b_0` from `h=0`)
  with the trigger `M<A_1` gives `w_1-D_{k^*}<w_1-b_0`, i.e. `D_{k^*}>b_0` strictly) — the algebra
  is correct and the derivation is sound, but (as the file states) it is not yet reconciled into a
  full contradiction; genuinely open. **(4) Background-Release Domination Lemma, strengthened form
  — CONFIRMED correct, unconditional, ready to certify.** Independently re-derived the one-line
  search-space-inclusion proof from scratch (bijection between `W`'s full selection space and the
  "`y` forced kept" sub-space of `W\cup\{y\}`'s selection space; minimizing over a superset is
  `\le` minimizing over any subset) — no gap. `0/3{,}000` (`|C|\le4,|W|\le4`) plus a wider
  `0/1{,}500` (`|C|\le5,|W|\le5`) sweep, both signs, `0` violations throughout — independently
  reproduces the builder's own `0/18{,}000`+`0/18{,}000$ figures in substance. **CERTIFIED** in
  `lemmas/background-release-domination.md` (both refuted chaining routes correctly left
  unresurrected, confined to §23.2/§24.4, not silently reused anywhere else in the file — grep-
  checked). **No overclaim found anywhere in §24** — the Status/§24.5 summary ("None of Gaps 1a,
  1b, 1c is closed this round") is accurate and matches every independently-verified finding
  exactly; the file consistently distinguishes "corroborated" from "proved" throughout. **Net
  verdict: real, honestly-scoped progress on all 4 dispatched items — one genuine cross-round
  discrepancy resolved in the simplifying direction (real, independently reproduced from a third
  codebase), one build-order correction that prevents future wasted effort (`q=4` MATCH branch),
  one previously-fully-unattempted lemma given its first real partial attack (Gap 1b base case),
  and 3 new certified general-purpose lemmas — but the central mechanism (the half-step lemma
  itself, Gap 1b's base case, and the generalized `A_1`-bound family) remains unproved. Status
  correctly stays `partial`.**
- `potential-weighting-upper-bound` — **(round 14) Certified a new general Shrink-List Monotonicity
  Lemma in full; found and proved (for `q\le3`) a new, strictly more general "Per-Partner Domination
  Lemma" that closes Gap 1a's Deletion-Suffices-for-`k^*` WITHOUT needing `k^*`'s global-argmin
  property at all — the largest fully-closed chunk of the Gap 1a mechanism to date, though `q\ge4`
  (the actually-needed general case) remains open.** Reviewer independently re-verified everything
  from scratch, own fresh code (`/tmp/round-14/verify/`, not reusing the builder's, outliner's, or
  explorers' harnesses): (1) **Shrink-List Monotonicity** (`OPT_{+1}(C,W)\le OPT_{+1}(C,W\setminus
  \{x\})` for arbitrary `C,W,x\in W`, both signs) — re-derived the one-line bijection proof from
  scratch (extend a `W\setminus\{x\}`-optimal selection by deleting `x`, using the "deleted
  contributes `0`" convention, confirmed to match §13.2's own `OPT_\sigma` definition exactly),
  `800/800` fresh random trials (both signs, `|W|\le5`, arbitrary background), `0` violations;
  independently reproduced the file's own worked example (`C=\{5,8\},W=(10,8,7,2)`: `OPT_{+1}=0`)
  exactly. **CERTIFIED** in `lemmas/shrink-list-monotonicity.md`. (2) **Per-Partner Domination Lemma**
  (`A_{3,l}\ge\min(A_1,D_l)` for every `l`, no trigger, no argmin needed) — independently re-derived
  the full `q=3` case-by-case proof symbolically from scratch (own `sympy`/hand derivation of the
  three Rank-Extraction-Identity cases A/B/C and all sub-orderings, not reading the file's algebra
  first): every case closes exactly as claimed, via either `\mathrm{keepval}\ge A_1$ (using the free
  bound `A_1\le b_0` or `A_1\le|b_0-w|`) or `\mathrm{keepval}\ge D_l` (the "trivial" sub-case) — no
  gap, no missing sub-ordering, no hidden case. Confirmed the reported "false start" (an early pass
  used only the weaker bound `A_1\le|b_0-w|` throughout Case A and got stuck) is a genuine, correctly
  diagnosed and correctly fixed issue — independently re-derived that the fix (switching to `A_1\le
  b_0` in the `w\ge b_0` sub-case, using `d_l\ge w` from Case A's own defining condition) is exactly
  what closes it, matching the file's write-up exactly. Fresh computational corroboration beyond the
  builder's own: random sweep `q\in\{2,\dots,5\}`, `7476` checks, `0` violations; **exhaustive**
  sweeps (not merely random) at `q=4` (half-integer alphabet `0` to `4`, `59{,}049` instances,
  `177{,}147` checks) and `q=5` (integer alphabet `0`-`4`, `15{,}625` instances, `62{,}500` checks),
  both `0` violations — pushing well past the builder's own tested ranges, per the round-13 lesson
  about widening a corroboration sweep before trusting it; the conjecture's open (`q\ge4`) status is
  correctly and honestly reported, not silently assumed elsewhere in the file (verified by grep: the
  only other reference is explicitly conditional, "if proved"). (3) **Deletion-Suffices-for-`k^*` via
  Per-Partner Domination** — independently re-derived the 3-line implication (trigger `M<A_1` at
  `l=k^*` plus Per-Partner Domination forces `\min(A_1,D_{k^*})=D_{k^*}`, hence `M\ge D_{k^*}$,
  combined with the free `M\le D_{k^*}` from Shrink-List's Corollary gives `M=D_{k^*}` exactly) — no
  gap, genuinely does not need `k^*` to be a *global* argmin, only that the trigger holds at that
  specific index; confirmed end-to-end by an independent fresh base-generator harness (own code, not
  the builder's `base_gen.py`) at `q\in\{2,3\}`: `6942` genuine triggered instances, `M=D` exactly in
  **all** of them (`0` mismatches); `q\in\{4,5\}`: `754` triggered instances (open regime), also `0`
  mismatches, consistent with (not proof of) the general conjecture. **No overclaim found: the file's
  own Status/§22 honestly report `q\le3` proved, `q\ge4` open, Gap 1a not fully closed — matches
  reality exactly.** Certified `lemmas/shrink-list-monotonicity.md` outright (general, free, no
  further computation needed). **Status correctly stays `partial`** — real, substantial, precisely
  bounded progress (a full proof for the `q\le2,3` sub-case of the central remaining gap, a new
  reusable general lemma, a cleaner/simplified reduction not needing global-argmin-ness), the general-
  `q` case (which is what the theorem actually needs) remains open.
- `potential-weighting-upper-bound` — **(round 13) Corrected the No-Gap Lemma's scope to the
  precise half-open interval `(\min(b_0,d_{k^*}),\max(b_0,d_{k^*})]` (fixing the round-13
  outline-reviewer's flagged open-interval imprecision), extended computational corroboration of
  this corrected statement (including the previously-untested tie/boundary event) far beyond prior
  rounds, proved one new elementary identity (Coincidence Identity) narrowing what a swap-based
  proof of Gap 1a would need, and proved a decisive negative result on Gap 1c (the cheapest
  possible "fully general, provenance-free" shortcut is FALSE, exact counterexample). **None of
  Gaps 1a/1b/1c is closed — Status correctly stays `partial`.** Reviewer independently
  re-verified every claim from scratch, with fresh code (own `mydefs.py`/`base_gen.py`, not
  reusing the builder's, outliner's, or any explorer's harness), validated against the file's own
  three worked examples first: (1) **No-Gap's half-open correction** — independently re-derived the
  `h=1\iff w_1\in(\min,\max]` case analysis by hand before running code, matches exactly; the
  propagation argument (DELETE/KEEP-at-`h=0` never touch `C`) re-traced and confirmed
  interval-shape-independent; fresh random sweep (`20{,}000` trials, `2955` triggered, `7293`
  checks, `0`/`0`/`0`/`0` on strict/half-open/tie-hi/tie-lo counters), an independent exhaustive
  sweep (`q=3..5,v_{\max}=3,4`, `0` violations throughout), and an independent rational hill-climb
  (own code, step to `1/16`, best margin found `1/8`, never `0` or negative) all corroborate.
  (2) **Coincidence Identity + swap construction** — the identity itself is trivial and correct;
  reviewer went further than the builder's own report and independently implemented and tested the
  associated swap CONSTRUCTION (not just the identity): across `813` triggered instances, `1853`
  genuine "keeps `z_j`" events, the construction gives a valid upper bound on `A_{3,j}` in
  **`1853/1853`** cases, `0` failures — confirms the construction is sound as far as it goes,
  though the sign argument needed to complete Gap 1a via this route remains missing, exactly as
  honestly stated. (3) **A genuine numerical overclaim found and flagged: Sum Bound's
  `rest=\emptyset` sub-case does NOT have a "comfortable `\ge3\times` margin"** — reviewer's own
  wider-range exhaustive/random search (still small, `q=3`, `v_{\max}` up to `50`, well within the
  builder's own tested regime's natural extension) found ratios as low as `8/3\approx2.67` at
  `v_{\max}=10$, and an explicit family `Z_0=(n,n,n+1),b_0=n/2` (checked by hand and in code,
  `n=4,\dots,1000`) drives the ratio `2n/(n-2)` down to an asymptotic infimum of exactly **`2`**
  (never below, matching the Sum Bound's own tightness) — not `3`. Root cause identified precisely:
  the builder's own saved harness (`explore_sumbound.py`) caps `v_{\max}\le6`, too narrow to reach
  where this family separates from `3` (`n\gtrsim8`). **This is a sampling-artifact overclaim, not
  a break of the Sum Bound itself** (which survived every test, `0` violations, including the
  reviewer's own broader `40{,}000`-trial sweep) — but it must be corrected before treated as
  reliable groundwork: the correct framing is "asymptotically tight at ratio `2`, no exploitable
  slack," the opposite of what §20.2 claims. (4) **Gap 1c counterexample
  `C=[3],W=(4,1,0)`** — reproduced exactly bit-for-bit (`OPT_{+1}=0` via two matching-only
  witnesses, `OPT\_KD=1`); independently confirmed this is legitimately OUTSIDE `\mathcal F`'s own
  provenance scope (background size `1`, whereas the base generator's own background is always
  exactly size `2`, an already-established structural fact), so no contradiction with the separate
  "`0` forced-matching events within `\mathcal F`" finding — reviewer's own fresh DELETE/KEEP
  closure walk (`302` triggered generators, `2122` nodes to depth 3) independently reconfirms
  **`0`** forced-matching events, plus (as an extra cross-check) **`0`** Claim-A violations across
  `3426` nodes on the same walk. **Coincidence Identity declined for standalone lemma
  certification** (trivial, single still-incomplete use, per both the builder's own and the
  reviewer's assessment — stays in §20.1 for the next round to build on, not promoted to
  `lemmas/`). **Net verdict: real, correctly-scoped incremental progress (a genuine precision fix,
  a positively-verified construction, a decisive negative result) plus one concrete, previously
  undetected numerical inaccuracy that must be corrected next round (the Sum Bound margin claim) —
  Status correctly stays `partial`, route CHANGES REQUESTED.**
- `potential-weighting-upper-bound` — **(round 12) Gap 2 closed in full; two new general lemmas
  (Empty-Background, Background-Splitting) unconditionally resolve Claim A/Gap 1 on the
  "eventually-dominant" tail of every path in the scope family `\mathcal F`; a new structural fact
  sharpens the base generator; a clean iff-criterion reduces Gap 1's residual content to one crisp
  existence question; the outline's own flagged open question (does an FSI-shaped argument close
  Gap 1?) is answered decisively NO; a sharpened negative result shows background size-boundedness
  alone is not doing the real work. Gap 1 (the central inequality) itself is NOT closed — Status
  correctly stays `partial`.** Reviewer independently re-verified every claim from scratch, with
  fresh code (not reusing the builder's, outliner's, or outline-reviewer's harnesses): (1) **Gap 2**
  (`\mathrm{OPT\_KD}_\sigma`'s own DELETE/KEEP trichotomy with the identical Rank-Extraction KEEP
  closed form) — `4000/4000` fresh exact-integer trials, `0` mismatches. (2) **Empty-Background
  Lemma** (`\mathrm{OPT}_\sigma(\emptyset,W)=\mathrm{OPT\_KD}_\sigma(\emptyset,W)`, explicit values
  `0`/`\max(W)`) — `2000/2000`, `0` mismatches, exact values confirmed. (3) **Background-Splitting
  Lemma** (both the `\mathrm{OPT}` and `\mathrm{OPT\_KD}` versions) — `3000/3000` each, `0`
  mismatches; additionally verified the **pointwise, selection-by-selection** claim underlying the
  Corollary directly (for every individual selection in the full selection space, not just the
  aggregated optimum) — `0` mismatches across every trial's full selection space; and verified the
  **Corollary itself** (Claim A holds at `(C,W,\sigma)` iff it holds at
  `(C_{\mathrm{lo}},W,\sigma\cdot(-1)^h)`) directly and independently — `1200/1200`, `0` mismatches.
  **One minor precision note** (not a correctness error): the file's "reaches the dominated regime
  within a handful of steps" is empirically demonstrated only along the specific all-DELETE path;
  the reviewer's own check of mixed DELETE/KEEP paths on fresh instances found no counterexample
  either, but the test instances happened to be structurally degenerate (both background elements
  equal), so this does not independently confirm the "handful of steps" bound generalizes to
  every mixed path — the surrounding prose should be scoped explicitly to the tested path, though
  the *rigorous* part of the claim (dominated `\implies` resolved, and domination persists once
  reached) was independently re-derived analytically and holds unconditionally, confirmed by the
  Corollary check above. (4) **`B_0=\emptyset` never triggers** — re-derived from the certified
  Empty-Background Lemma and Fact 1 exactly as the file does; `3000` fresh trials (varied `Z_0`),
  `0` counterexamples. (5) **Non-Matching-Witness Criterion** (the iff reducing Claim A to
  existence of a non-`\max(W)`-matching optimal witness) — re-derived the two-directional proof
  from scratch (no gap found) and independently verified computationally, `3000/3000`, `0`
  mismatches. (6) **FSI does not close Gap 1** — the structural diagnosis (FSI relates *sibling*
  match-partner values at one recursion level to each other, not a node's own MATCH branch to its
  own DELETE/KEEP branches) is sound and independently re-confirmed as a real, non-hand-wavy
  distinction; the substantive claim behind it (a non-matching optimal witness already exists in
  every genuine triggered instance) was independently reconfirmed via the reviewer's own fresh
  `\mathcal F`-family sweep (**`2379`** genuine nodes — base generators plus 3 full levels of
  DELETE/KEEP closure, both branches at every step, not sampled — **`0`** Claim-A violations) and
  via the Criterion-equivalence check above (exact instance counts differ from the builder's own,
  as expected from independent sampling, but the qualitative finding matches exactly). (7)
  **Size-boundedness alone is not sufficient** — fresh random sampling of *arbitrary*
  (non-`\mathcal F`-provenance) backgrounds reproduces violations at `|C|=1` (`134`/`6000`), at the
  smallest list sizes `|W|=2,3` (`268`,`292` per `6000`), while *dominant* backgrounds (every
  `C`-element `\ge\max(W)`) show **`0`** violations across `6000+6000` trials — both of the file's
  own illustrative worked examples (`C=\{5,8\},W=(10,8,7,2)`: `\mathrm{OPT}=0,\mathrm{OPT\_KD}=2`;
  `c=1,W=(10,8,7)`: `\mathrm{OPT}=0,\mathrm{OPT\_KD}=1`) were reproduced **exactly** by the
  reviewer's independent brute force. **Reviewer's own adversarial search:** ran a from-scratch
  hill-climbing perturbation search seeded at the lowest-margin nodes found along genuine
  `\mathcal F`-closure walks; found **`0`** violations while confined to verified `\mathcal
  F`-membership, but the search *does* find violations (margin as low as `-6`) the instant it
  perturbs raw values away from the genuine derivation chain (breaking `\mathcal F`-provenance and
  losing background-dominance) — this independently corroborates finding (7) rather than
  contradicting Gap 1's open status: every located "violation" is traceably out of `\mathcal F`'s
  scope, not a counterexample to Claim A within it. **Additionally sanity-checked:** the underlying
  Generalized Multi-Background Peeling Lemma trichotomy itself (`\mathrm{OPT}_\sigma(C,W)=
  \sigma\text{-opt}(\mathrm{DEL},\mathrm{KEEP},\mathrm{MATCH})`), `2000/2000`, `0` mismatches — the
  harness was validated against this and both of the file's own worked examples before being
  trusted for any new claim. **No error, missing case, circularity, or overclaim found anywhere in
  §17–§18.** The reported `partial` status precisely reflects what has been established: real,
  substantial narrowing of the sole remaining gap (now reduced to a crisp existence question on
  the non-dominated prefix), with the central inequality (Gap 1) still genuinely open — neither
  undersold nor oversold.
- `potential-weighting-upper-bound` — **(round 11) Reformulated the Refined Delete-Recovery
  Conjecture (§15.4) into a strictly sharper "Sharp Argmin Recovery" (SAR) claim, proved one new
  general lemma in full (the Forced Swap Inequality), and produced three precise negative results
  narrowing the search for a correct general proof — but did NOT prove or refute SAR/RDRC itself.**
  Reviewer independently re-verified every claim from scratch, with fresh code written from the
  prose statements only (not by reading the builder's harness), across two rounds of adversarial
  design: (1) **Forced Swap Inequality** — re-derived the four-point non-crossing-repair argument
  symbolically (disjoint vs. nested re-pairing of `\{1,i,k^*,j\}`, global-argmin chaining), no gap
  found, no restriction on `|B|` needed; independently coded from scratch (`mydefs.py` +
  `verify_fsi_fresh.py`), `1289/1289` fresh crossing-pair checks (`q=3,\dots,7`, background size
  `0`–`4`), zero violations, corroborating the builder's own `3336/3336`. **Certified** as
  `lemmas/forced-swap-inequality.md`. (2) **Sharp Argmin Recovery** — subjected to a fresh
  adversarial battery of the reviewer's own design (not reusing the builder's or outline-reviewer's
  embedding attack): exhaustive (not sampled) sweeps at `q=4,5,6` (`657` triggered instances, `0`
  violations), a tie-focused random/structured search specifically targeting the "ANY tied argmin"
  quantifier in SAR's statement (dyadic/perturbed-dyadic, arithmetic-progression, and
  heavy-duplicate families; `230` tie-events, `944` per-argmin checks, `0` violations), and a
  from-scratch hill-climbing/simulated-annealing search explicitly designed to minimize the
  "recovery slack" `B_{3,k^*}-A_{3,k^*}` toward a violation (`8508` total triggered evaluations
  across two independent runs, minimal slack found `=0`, never negative). SAR survives every one of
  these genuinely fresh attacks, corroborating but not proving it. (3) **The three negative
  results** — the `|B|=3` counterexample to SAR's unrestricted-background generalization (§16.3.2)
  and the "one-step compatible winner" (GML) counterexample (§16.3.3) were both re-derived exactly
  by the reviewer's own independent computation, bit-for-bit matching the file's claimed values
  (`A_1=1`, `A_{3,k}` values `\{1,1,0,1,2\}`, `A_{3,k^*}=0\ne B_{3,k^*}=1`; and
  `\mathrm{OPT}(C,W)=0=$ DELETE-branch value yet `\mathrm{TAGGED}(C,W,3)=1`). The averaging
  negative result (§16.3.1) was confirmed **in substance** via a properly-rescoped fresh test
  (restricted to the actual SAR argmin branch and `|B|\le1`, matching the conjecture's own scope:
  `0` non-trivial successes out of `5776` argmin-branch crossing instances) — **but the file's one
  specific illustrative worked example does not reproduce**: the reviewer's independent
  recomputation of `B=[1],Z=(9,8,8,8,5,3,0)` gives alternative values `\{0,2\}`, not the claimed
  `\{1,1\}` (the Forced Swap Inequality itself, and the broader negative claim, both still hold —
  only that one transcribed example is mislabeled; flagged for a one-line fix, does not change
  Status). **Self-assessment check: the builder's own honest "not solved, Status stays partial" is
  correct — neither undersold nor oversold.** No hidden error was found that would make this either
  MORE solved (SAR/RDRC remains genuinely open, no proof mechanism succeeded) or LESS solved (the
  one documentation slip does not undermine any certified claim). Status correctly stays `partial`.
- `potential-weighting-upper-bound` — **(round 9) Proved a new General Rank-Extraction Identity
  in full and used it to close the Generalized Multi-Background Peeling Lemma's KEEP branch with
  an exact closed form (previously only "individually tractable, not written down"); then, via a
  careful branch-by-branch accounting (not numerics alone), showed the Full-Slack Insertion
  Lemma (§12.1) is NOT an independently easier base case for the recursive route of §12.2 — its
  own inductive step needs the identical content, recursively, as the aggregated Small-Gap
  Crossing-Domination Lemma (§11.4) — and unified both previously-separately-tracked open items
  into one precisely-stated Core Open Lemma ("Match-Recovery Lemma"), still open.** Reviewer
  independently re-verified every claim from scratch, with fresh code, not trusting the builder's
  own harness: (1) the General Rank-Extraction Identity, 3000/3000 exact-`Fraction` trials,
  0 mismatches, and the two-step Fact-3 derivation re-traced symbolically — correct; certified as
  `lemmas/general-rank-extraction-identity.md`. (2) The KEEP-branch closed form (both the
  `OPT`-side and `TAGGED`-side), verified via an independent from-scratch brute-force enumeration
  of all `(K,D,M)` selections (not reusing the builder's decomposition code) — 800/800 checks,
  0 mismatches, across `|B|=0,\dots,3`. (3) The full DELETE+KEEP+MATCH decomposition reproduces
  the true `OPT`/`TAGGED(\cdot,0)` exactly — reviewer's own independent brute force, 400/400 for
  each of `OPT` and `TAGGED`, 0 mismatches (using the file's own claimed MATCH-branch split point
  `k-1`, independently re-derived and confirmed correct, not merely copied). (4) The reported
  negative sub-result (individual per-`k` match-branch equality fails often, `117/500` in the
  reviewer's own fresh trial, order-matching the builder's `152/500`; the match-only aggregate
  — ignoring DELETE/KEEP — itself fails in a small but nonzero fraction, `7/500` reviewer vs
  `3/500` builder; the FULL DELETE+KEEP+MATCH aggregate never once failed, `0/500`, even when the
  match-only aggregate did) — confirmed exactly, corroborating the DELETE/KEEP-compensation
  mechanism is real and load-bearing, not a hedge. (5) Reviewer additionally checked, as a
  cross-check the file itself does not run, that the raw match-only aggregate (no DELETE/KEEP
  compensation) holds with **zero** failures at the very first recursion level (`|B|=0`, the
  original top-level Small-Gap Crossing-Domination Lemma's own regime, `0/800` fresh trials) —
  consistent with, and sharpening, the builder's own finding that the failures are a phenomenon
  specific to the deeper (`|B|\ge2`) recursion levels the recursive strategy is forced through,
  not a flaw in the originally-targeted narrow statement. **The Match-Recovery Lemma itself
  remains unproved — genuine, well-diagnosed progress (a new certified lemma, a decisive
  "not independently easier" finding narrowing the population's open-lemma bookkeeping from two
  items to one, plus a real negative sub-result ruling out an unconditional strengthening), not a
  closure.** Status correctly stays `partial`.
- `concavity-minimax-duality` — **(round 9) Refuted the outline's specific §14.4 proof mechanism
  for the Distinct-Bucket Lemma with a concrete counterexample, then proved two new general
  lemmas (Superincreasing Preservation Lemma, Slot-Replacement Corollary) and one D_m-specific
  lemma (Value-Order = Dominant-Index-Order Lemma), used them to reduce Distinct-Bucket to one
  precise, still-open "Local Claim," and proved a decisive negative result ruling out the most
  natural route to closing that Local Claim.** Reviewer independently re-verified every claim
  from scratch, fresh code: (1) the §14.4-refuting counterexample (`8\to4\to2\to1` chain on
  `D_3`, three `M`-operations, budget `m=3`, giving `\mathrm{bucket}(1)=1` vs. the naively
  predicted `L+1=4`) — arithmetic and legality re-checked directly, correct. (2) Superincreasing
  Preservation Lemma — re-derived the induction (Key Sub-claim, four-way position case split)
  from scratch and independently confirmed computationally on 60 fresh random (non-power-of-2)
  superincreasing bases, full BFS to depth 4, 8527 states, 0 violations; certified as
  `lemmas/superincreasing-preservation-and-slot-replacement.md`. (3) Slot-Replacement Corollary
  — 3000 fresh random trials, exact integers, comparing the predicted in-place sorted list
  against an independent full re-sort, 0 mismatches; certified in the same file. (4) Value-Order
  = Dominant-Index-Order Lemma — reviewer wrote an independent token-labeled BFS (not reusing the
  builder's code) for `D_m`, `m=1,\dots,5`; state counts `4,15,62,289,1510` matched the file's own
  figures exactly, and `0` order violations found across all `1,9,65,460,3358` simultaneously-active
  token pairs checked; certified as `lemmas/value-order-dominant-index-order.md`. (5) The
  Distinct-Bucket-to-Local-Claim reduction (§15.4) — independently re-traced the case analysis
  (untouched prefix, the two new adjacent pairs at the insertion slot, the "untouched subsequence
  of an already-strictly-decreasing list stays strictly decreasing" fact used for the
  positions-after-`b` case) and found it complete and correct, no missing case; confirmed the
  `D`-step of the parent induction (not spelled out in §15.4, but genuinely trivial — deleting an
  element from a set with pairwise-distinct bucket values keeps them pairwise distinct) needs no
  further justification. (6) The Local Claim itself — reviewer independently re-implemented the
  exhaustive check with fresh code (plain value-multiset BFS, not the builder's token-labeled
  one): `m=0,\dots,6`, `13507` total `M`-transitions checked (matching the builder's own
  `11535`-at-`m=6`-alone figure exactly at that value), `0` violations — genuinely corroborating,
  not merely re-asserting, the open Local Claim's computational support. (7) The `(4,3)`
  counterexample refuting "superincreasing alone implies distinct buckets" — arithmetic
  re-checked (`\mathrm{bucket}(4)=\mathrm{bucket}(3)=3`), correct. **The Local Claim itself
  remains unproved — genuine, well-verified progress (two new certified general lemmas, one new
  certified `D_m`-specific lemma, a sharp reduction of a global claim to one precise local
  inequality, two decisive negative results ruling out entire classes of future proof attempts),
  not a closure.** The file's own honest scope note — that even a full closure of Distinct-Bucket
  would only reproduce the lower bound `dyadic-cascade-induction`'s round-8 all-cycles-resolution
  route already established unconditionally, not provide new leverage on the theorem's actually
  open items (general-`m` upper bound, general `n\ge4`) — is accurate and not overclaimed.
  Status correctly stays `partial`.
- `dyadic-cascade-induction` — **(round 8) The "all-cycles" D/M-completeness caveat is now
  CLOSED, for every cyclic tie-dependency structure (any length, any mix of original/derived
  participants), completing the lower bound `g(D_m,m)\ge e_m\cdot S(D_m)` unconditionally, for
  every `m`.** New §5.5 proves an exhaustive `\#X` (cross-type-edge count) dichotomy:
  `\#X=0` (never the true minimizer, pre-existing), `\#X=1` (never a genuine cycle — always a
  disguised, already-peelable self-bisection, new **Lone-`X`-Edge Vacuity Lemma**), `\#X\ge2`
  even (physically infeasible — closing identity is a nonempty signed subset sum over disjoint
  original indices, never zero, new **Even-`\#X` Infeasibility Lemma**), `\#X\ge3` odd
  (physically infeasible — the unique closed-form solution has a sign-alternating coefficient on
  the most-significant participating index, forced negative by superincreasing dominance, new
  **Generalized Cross-Type Domain-Violation Lemma**, which strictly generalizes and supersedes
  round 7's Cross-Type Cycle Infeasibility Lemma to derived participants). The bridge from
  "abstract cyclic tie system" back to "genuine D/M-reachable tokens" is a new **Cycle
  Common-State Lemma** (§5.5.1): any minimal cyclic component's participants are simultaneously
  active tokens of one common D/M state, obtained by running the already-certified peeling
  induction on everything *outside* every cyclic component and stopping just before touching any
  cycle — a legitimate, non-circular reuse of the already-twice-certified
  `dm-completeness-partial.md` peeling characterization (getting "stuck" at a union of cycles
  means precisely that everything else has already been peeled), not an extension of its scope.
  **Reviewer independently re-verified the core mechanism from scratch**: re-derived the general
  closing-equation/odd-even dichotomy; checked the closed-form odd-cycle solution against direct
  linear solve (`464` random disjoint-support-token trials, `q\in\{3,5,7,9\}`, `0` mismatches);
  confirmed domain violation (infeasibility) in **100% of the 464 trials**; confirmed the
  sign-dominance prediction (which specific block goes negative) matches the actual solution in
  **all 464 trials** (after finding and fixing an off-by-one in the reviewer's *own*
  re-implementation of the file's formula — not a bug in the proof); confirmed even-`\#X`
  inconsistency in `300/300` fresh trials; hand-traced one `q=5` worked example end to end
  (8-element base, disjoint-support derived tokens) matching the closed form and the predicted
  sign pattern exactly at all 5 blocks. **One honestly-flagged residual note (not a concrete
  counterexample, an inherited abstraction-level dependency):** the Cycle Common-State Lemma's
  construction ultimately rests on `dm-completeness-partial.md`'s own peeling argument, whose
  write-up handles the interaction between forest depth ("leaf-parent" eligibility) and the
  tie-dependency graph's in-degree-0 property at "proof sketch" level (that lemma's own file
  says "full detail in `concavity-minimax-duality.md` §8") rather than with a fully spelled-out
  reconciliation for cuts with further-subdivided descendants — this is inherited from the
  already-twice-certified (rounds 4, 7) base lemma, not a new gap introduced this round, and the
  reviewer found no concrete counterexample to it after deliberate attempts to construct one, but
  flags it as the one place maximal rigor would still want a fully explicit reconciliation.
  **Net verdict: a major milestone — the lower bound against the dyadic construction `D_m`
  specifically is now fully, unconditionally proved for every `m`, modulo only the above
  inherited (uncontradicted) abstraction dependency.** This does NOT solve the whole theorem:
  the matching upper bound at general `m` (tracked in `potential-weighting-upper-bound`) and
  general `n\ge4` remain open, so file Status correctly stays `partial`. Certified as
  `lemmas/all-cycles-resolution.md`.
- `dyadic-cascade-induction` — **(round 7) §5.4 Steps 1-2 fully proved, plus a new general
  Cross-Type Cycle Infeasibility Lemma, resolving the "all-cycles" caveat for every UNIFORM
  shallow cycle (all-original participants, all edges the same type).** (1) The
  Guaranteed-Untouched-Original Lemma (pigeonhole: `\le m` cuts touch `\le m` roots, `<k=m+1`
  originals, so at least one original piece of `D_m` is always left untouched) — elementary,
  correct, reviewer-reconfirmed. (2) The Shared-Value Cycle-Breaking Lemma generalizes the old
  `L=2` case to every `L\ge2`: a uniform shared-value tie is never the true minimizer, given a
  guaranteed untouched piece (piecewise-linear breakpoint argument via the certified Vertex
  Lemma) — reviewer spot-checked on `D_2` concretely, confirmed the claimed shape (constant
  then decreasing to a degenerate boundary, never an interior optimum). (3) The new Cross-Type
  Cycle Infeasibility Lemma: for `L\ge3` distinct originals of any strictly superincreasing
  sequence, the cyclic system `u_i+u_{i+1}=b_{i+1}` has NO solution with every `u_i\in(0,b_i)`
  — proved by a clean sum-plus-dominance argument, reviewer-reverified both symbolically and by
  exact `sympy` computation (`L=3,4,5` on `D_2,D_3,D_4`, 100 trials, zero feasible cycles,
  matching the proof's predicted odd/even failure modes exactly). **Reviewer finding (a real,
  precise gap, not previously flagged clearly enough): the file's own Step-3 body text
  ("every...configuration...is now accounted for") mildly overclaims relative to its own,
  more careful section header ("resolved for shallow cycles, honest remaining gap for
  deep/mixed cycles") and "cases covered" bullet — lemmas (2)+(3) only resolve UNIFORM shallow
  cycles (every edge the same type); a cycle mixing shared-value and cross-type edges among
  all-original participants is NOT covered by either lemma as stated, and is not proved either
  way.** The reviewer independently ran an exhaustive (not sampled) search for such mixed-type
  cycles on `D_4` (`L=4,5`) and `D_5` (`L=4,5,6`), zero feasible instances found — suggestive,
  not a proof. Certified as `lemmas/shallow-cycle-resolution.md`, with this precise scope
  caveat included. The all-cycles caveat is narrowed to: (a) any cycle with a derived
  (non-original) participant — shown concretely why the natural dominance-argument extension
  fails for `D_m`; (b) any cycle mixing edge types among all-original participants — untouched,
  newly identified as a distinct residual by this round's review.
- `dyadic-cascade-induction` — **(round 5) The "Superincreasing No-Early-Zero Lemma" is now
  PROVED IN FULL (§5.3 Steps 3.1–3.7), a genuine new theorem, independently re-derived and
  re-verified by the reviewer both symbolically (every step of the token/signed-sum induction
  re-traced from scratch, no gap found) and computationally (exhaustive exact-integer BFS over
  the entire D/M-reachable state space from `D_m`, `m=1..5`, plus 15 fresh random strictly
  superincreasing sequences, zero violations). This closes the D/M-*sequence*-restricted lower
  bound `h(D_m,m)\ge e_m\cdot S(D_m)` unconditionally, for every `m`, via a genuinely different
  mechanism (a parity/non-vanishing-signed-subset-sum invariant) from §5–§5.2''s physical-cut
  casework. Certified as `lemmas/superincreasing-no-early-zero.md`. **Honestly scoped, not
  overclaimed:** promoting this to the *true physical* lower bound `g(D_m,m)\ge\dots` still
  requires the pre-existing, unresolved "all-cycles" caveat in
  `lemmas/dm-completeness-partial.md` — untouched, unworsened, unresolved by this round. File's
  own Status correctly stays `partial` (not `solved`).
- `dyadic-cascade-induction` — **(round 4) Fixed a real gap without reintroducing one, plus
  three new certified general lemmas, plus one more concrete instance closed.** (1) **Step-0
  fix (verified sound):** the round-3 outline had proposed reformulating the lower-bound's
  multi-cut gap purely in D/M-operation language, silently assuming D/M sequences capture
  XY's *entire* physical strategy space (an unproven "completeness" claim). This round's
  builder correctly abandoned that reformulation and instead derived the case split (0 / 1 /
  ≥2 cuts landing inside `a_1`) directly from physical cut points — independently re-verified
  by the reviewer: this is legitimate because a strategy is fully and simply specified by
  *which* final fragments its cut points land in, regardless of temporal order (disjoint cuts
  on disjoint stick segments don't interact), so the case split is exhaustive and well-defined
  with no appeal to any operation-sequence formalism. Confirmed that §5.1 (Branch A, Case B1,
  Case B2 — all already fully proved, every `m`) never actually depended on D/M language, only
  on Lemma P and Fact 2 applied directly to physical multisets — so the fix costs nothing.
  (2) **Three new general lemmas, all independently re-derived/re-verified by the reviewer**
  (exact-`Fraction` random trials for Facts 3–4, an independent from-scratch recursive
  construction for Fact 5): **Fact 3** (block extraction, generalizing Fact 2 to a dominant
  *block*), **Fact 4** (single-insertion changes `e` by at most the inserted value), **Fact 5**
  (chain-cancellation: any `L`-element multiset can be driven to `e=0` exactly with exactly `L`
  cuts; corollary, Fact 2's ceiling is always exactly attainable, never merely approached — a
  genuine proved structural obstruction ruling out a whole class of future "residual stays
  below its ceiling" arguments for the open gap). Now certified as
  `lemmas/insertion-and-cascade-facts.md`. (3) **One new concrete instance** (`m=4,i=3`,
  splitting the post-match leftover into 2 pieces, `R\{a_i}` untouched) closed by hand with
  exact fractions — independently re-verified by the reviewer via exact grid search, minimum
  is exactly `3/31` (comfortably above target `e_4=1/31`) — and two general bounding
  techniques (Fact 2 alone, Fact 4's insertion bound) were shown, with concrete numeric
  witnesses, to be too lossy to generalize; this is honestly scoped (the file does **not**
  claim this closes the general-`m` case). **Step 4 (the general multi-cut gap) remains open.**
  Status correctly stays `partial`, no overclaim found this round.
- `potential-weighting-upper-bound` — **(round 5) The "Slack Collapse" lemma is proved in full**
  (§7.1, immediate corollary of the already-certified Fact 5): if `k\le m` (Liu Bang leaves any
  mark unused), Xiang Yu trivially forces `e=0`, reducing the ENTIRE upper-bound induction
  (Case (i) and (ii), every `m`) to the single tight sub-case `k=m+1` — independently
  re-verified by the reviewer (direct re-derivation from Fact 5, correct). Certified as
  `lemmas/slack-collapse.md`. Also: **falsified** the outline's "sorted-adjacency" conjecture
  with two exact minimal counterexamples (`A=(82,66,47,40),m=3`: unrestricted one-shot-tail
  optimum `5` vs. adjacent-only-restricted `7`; `A=(46,44,31,21,15),m=4`: `0` vs. `2`) — both
  independently reconstructed and re-verified exactly by the reviewer via an independent
  from-scratch exhaustive one-shot-allocation search (bit-for-bit match on both the optimal
  value and the winning selection). Proposed a replacement "non-crossing matching+deletion"
  conjecture, honestly reported as **numerically supported (560+ trials, zero mismatches) but
  NOT proved** — confirmed not overclaimed anywhere in the file. Ruled out a local pairwise
  uncrossing-exchange proof technique for it with an exact counterexample
  (`Y=(43,33,20,16,11,8,2)`, crossing pairing `e=15` vs. both local alternatives' `e=25`) —
  independently reconstructed and confirmed exactly by the reviewer. Status correctly stays
  `partial` — real progress (new certified lemma narrowing the remaining case to `k=m+1`), the
  central Case (ii) mechanism gap remains open.
- `potential-weighting-upper-bound` — **(round 4) A genuine, carefully-diagnosed negative
  result: no fixed lookahead depth (independent of `m`) can rescue the scalar-IH-fallback
  "induction loading" mechanism.** The builder self-caught and fixed a real bug (an early test
  version tautologically compared the bound against itself at the *same* budget, making "0
  failures" vacuous) — the reviewer independently re-implemented a full-width-branching
  lookahead test from scratch and reproduced the same qualitative finding (non-shrinking
  failure rate as `m` grows for fixed lookahead depth, e.g. ~11% at `m=4,\ell=2` vs. the
  builder's reported 12% — different sampling, same conclusion), corroborating the finding is
  genuine, not a residual artifact. All exact-fraction claims independently re-verified
  (the `m=3` counterexample's Rule-1 value `37/500`, the true optimum `1/500` with exactly the
  4 tied optimal first moves claimed, the corrected-Form-E' arithmetic `69/875` and `13/150`,
  the sharpened `m=2` exact Rule-2 counterexample `83/500` vs `1/7`) — all match exactly. The
  certified Lemma D/M (round 3) remains the file's standing theorem-relevant contribution;
  this round's addition is a well-documented dead end for a specific technique (already
  Status `partial` from round 3's Lemma D/M, correctly not re-elevated by this round's
  negative-only result).
- `concavity-minimax-duality` — **(round 5) Two new general lemmas proved in full and
  independently re-verified** (§10 Step 1, §11): the **1-Lipschitz weak-duality lemma**
  (`e(M)\ge e_g(M)` for any 1-Lipschitz `g` with `g(0)=0`, equality at `g=\mathrm{id}`) and,
  building on a new **cascade reachability lemma** (`M(2^j,2^{j-1})` on `D_j` yields exactly
  `D_{j-1}`, so `D_j\to\{1\}` in exactly `j` ops, `D_j\to D_i` in exactly `j-i` ops — confirmed
  exactly by the reviewer for `j=1..6`), the **Forced-Value Lemmas A/B**: any valid certificate
  `g` for this method must have `g(1)=1`, `g(2)=2` exactly, for every `m`. Used these to give
  **exact, closed-form refutations** (not just stress-test observations) of two candidate clips
  `\min(t,1)` (fails at every odd `m`, reviewer-confirmed exactly for `m=1..6`) and `\min(t,2)`
  (fails via the witness `(4,2,\tfrac12,\tfrac12)`, reachable from `D_m` for every `m\ge2`,
  reviewer-confirmed reachable exactly for `m=2..6`). Also ran the dispatched LP-feasibility
  check and found (and proved) it **circular/uninformative by itself** — a genuine
  methodological finding: any finite sample on which the raw claim is already known to hold is
  automatically LP-feasible via the trivial witness `g=\mathrm{id}`. **No working closed-form
  `g_m` found** — reported honestly as still open, no overclaim. Certified as
  `lemmas/lipschitz-certificate-and-forced-values.md`. Status stays `partial`.
- `concavity-minimax-duality` — **(round 4) A genuinely new, real result: proved
  `g(A,m)=h(A,m)` (D/M-search value equals the true physical minimum) for any `A,m`, modulo a
  single, precisely-isolated open case.** Carefully re-verified by the reviewer via an
  independent topological-sort/DAG argument (a valid temporal D/M realization of a configuration
  exists iff its cut "tie-dependency" graph is acyclic; since every node has out-degree ≤1, the
  *only* way every node can have in-degree ≥1 — blocking a safe peel — is if the graph is a
  disjoint union of directed cycles, which requires *every* unresolved cut to be a "cross-tie"
  to another cut's output, no bisections or ties-to-untouched-originals anywhere) —
  independently reproduces the file's own characterization exactly, confirming it is correct,
  not merely plausible-sounding. This closes the lower-bound-direction D/M-completeness gap the
  round-4 outline-reviewer flagged, via a genuinely different route from
  `dyadic-cascade-induction`'s Step-0 fix (which sidesteps D/M language entirely) — **the two
  fixes are independent and complementary, not conflicting**: one shows the physical-reasoning
  route doesn't need D/M completeness at all, the other proves a (conditional) completeness
  result useful to any future approach that *does* want to reason in D/M language for a lower
  bound. Now certified as `lemmas/dm-completeness-partial.md`. Also tested a new candidate
  potential `Φ(M,r)=S(M)/(2^{r+1}-1)`: passes (P1) and (P2) under `D`-moves unconditionally, but
  **fails (P2) under `M`-moves**, with two exact counterexamples independently re-verified by
  the reviewer via exact BFS reachability + Fraction arithmetic (`m=2`: state `(3,2)` at budget
  1, reachable from `D_2` via `M(4,1)`, `\Phi:5/3\to1`; `m=3`: state `(6,4,1)` at budget 2,
  reachable from `D_3` via `M(8,2)`, `\Phi:11/7\to1` — both confirmed exactly, both states
  confirmed reachable). Status correctly upgraded from `unsolved` to `partial` (real reduction
  toward the theorem, not merely a dead-mechanism report) — matches CLAUDE.md's definition.
- **`elementary-exchange-smoothing` — formally retired this round** (proof-reviewer action,
  following the round-4 outliner's recommendation). Its Step A ("tie-or-degenerate lemma" +
  iterated-cuts Corollary) is the same underlying fact as `dyadic-cascade-induction`'s own §3
  "vertex lemma", proved independently by two different builders in two different rounds
  (cross-validating each other) — merged into one canonical `lemmas/vertex-lemma.md`. No
  further builder dispatch to this slug unless a future outliner finds a genuinely new,
  non-redundant target for it.
- `potential-weighting-upper-bound` — **(round 8) Proved the Extreme-Element Peeling Lemma in
  full generality (§11.2): for any sorted `Y` and any budget `b`, `OPT(Y,b)` (resp. `NC(Y,b)`)
  decomposes exactly into DELETE/KEEP/MATCH branches via two clean bijections plus one
  application of the certified Fact 3 — fixing the reviewer's round-7 imprecision about the
  MATCH branch with a genuine proof (not a re-description).** Reviewer independently re-verified
  the decomposition against direct brute-force `OPT` on `150` random trials (`p` up to `6`,
  various budgets) — `0` mismatches. Also **refuted** the natural *per-fixed-partner* reading of
  the round-8 outline's "Small-Gap Crossing-Domination Lemma" with an exact, hand-verified
  counterexample (`Y=(92,89,77,73),b=3,j=3`: `INSERT_OPT=1` vs `INSERT_NC=15`) — reviewer
  independently reconstructed this exactly by brute force, confirming both the mismatch and that
  the *aggregated* (min-over-partner) values still agree (`OPT(Y,3)=NC(Y,3)=1`, via a different
  partner `j=2`). Correctly rescoped to the **aggregated** Small-Gap Crossing-Domination Lemma
  (min/max over all partners `j`, not per-partner) — honestly reported as still **unproved**
  (`2060` fresh exact-integer trials, zero mismatches, `p` up to `9`, but no proof attempt
  completed this round). Status correctly stays `partial` — real progress (a new certified
  general lemma, a decisive negative result narrowing the target to its correct, precise form),
  the central mechanism gap remains open.
- `potential-weighting-upper-bound` — **(round 7) Proved §8 Steps 1-2 in full (Layer-cake
  identity for `e`; Non-crossing inside/outside independence), then DECISIVELY REFUTED the
  general "non-crossing matching+deletion" conjecture with an exact, twice-independently-coded
  counterexample, then correctly rescoped it to the sub-case the parent construction actually
  needs.** Reviewer independently reconstructed `OPT(Y,3)=1` vs `NC(Y,3)=2` for
  `Y=(39,36,30,28,22,18,14)` via an independent from-scratch exhaustive enumeration (925
  selections at cost `\le3`) — matched exactly, including the winning selections
  (`kept={14}`, matched `(39,30),(36,22),(28,18)`) and (`kept={30,28,14}`,
  `deleted={39,18}`, matched `(36,22)`). Also independently reconfirmed the second
  counterexample (`Y=(400,218,194,187,169,27,3)`) and that BOTH counterexamples vanish at
  `b=p-1=6` (`OPT=NC=0`) — matching the file's claims exactly. **Re-traced the dependency
  (per dispatch): the rescoping to `b=p-1` is correctly justified** — in the tight case
  `k=m+1` (Slack Collapse), after a chain-prefix of length `c`, the tail has `p=k-c` elements
  and budget `m-c=p-1` exactly, for every `c\in\{0,\dots,m\}`, a clean algebraic identity
  (`m=k-1`) re-derived independently. Since `OPT\le NC` always (trivial direction), showing
  `NC(Y,p-1)\le` target would suffice regardless of exact equality — but the file's own
  described strategy (§6 Step 2, the "one-shot tail exact optimum") is `OPT`, not `NC`, and
  only `NC` is tractable via the certified Fact-3 peeling recursion, so `OPT=NC` at `b=p-1`
  really is the load-bearing target for turning the numerically-validated family into a
  closed-form general proof. 2218 fresh exact-integer trials (`p=2..10`, `b=p-1` exactly), zero
  mismatches. Honestly still unproved. Both new lemmas certified as
  `lemmas/layer-cake-and-noncrossing-independence.md`. No overclaim found.
- `concavity-minimax-duality` — **(round 8) Fixed round 7's impossible illustrative `m=6`
  example with a verified replacement, corrected the structural description of `g^*`'s
  minimizing mechanism (it collapses to size 1-2, not "many cancelling pairs" — that
  configuration is in fact the *maximum*, not minimum), and proved two new general lemmas.**
  New exact closed forms: `g^*(2^i)=i+1` and (combined with the standard consecutive-integer
  alternating-sum identity) `e_{g^*}(D_m)=\lceil(m+1)/2\rceil` for every `m` — reviewer
  independently re-derived both from scratch, confirmed exactly. Proved an **Integer-Preservation
  Lemma** (`g^*` maps nonnegative integers to nonnegative integers; D/M operations preserve
  integrality), reducing the target `e_{g^*}\ge1` to the strict-sign statement `e_{g^*}>0`.
  Found a **decisive negative result**: single-operation (edge-wise) monovariance of `e_{g^*}`
  is FALSE — exact counterexample `(32,8,4)\to(8,4)` via `D(32)`, dropping `e_{g^*}` from `5` to
  `1` in one step (reviewer independently recomputed via the base-case formula, confirmed exactly)
  — ruling out an entire class of future inductive proof attempts for `g^*`'s general property.
  **`g^*`'s minimum-is-1 property remains an open conjecture**, exhaustively verified through
  `m=6` (inherited from round 7) but honestly not proved for general `m`; a "size-class-wide"
  (not edge-wise) inductive argument is flagged as the concrete next step. Status correctly
  stays `partial` — genuine corrections and two new certified lemmas, central conjecture
  still open.
- `concavity-minimax-duality` — **(round 7) Extended Forced-Value Lemmas A/B to a complete,
  general two-sided characterization: `k+1\le g(2^k)\le2^k` for every `k\ge0` (both bounds
  proved, not numerics alone), equality (forcing) iff `k\in\{0,1\}`; and `g(2^j+1)=g(2^j)+1`
  exactly for every `j`, so forcing propagates identically, giving `g(3)=3` forced but
  `g(5),g(9),g(17),\dots` provably not forced.** Reviewer independently reconstructed the two
  new reachability lemmas' exact operation sequences (Top-Two-Residual-Cancel: `k=2..8`;
  Successor: `j=0..8`) in exact `Fraction` arithmetic — every operation count and final state
  matched exactly, in all 15 cases. The induction/gap arithmetic in the Combined Theorem was
  independently re-derived, no gap found. Certified as
  `lemmas/forcing-characterization-dyadic.md`. **A new candidate certificate `g^*`** (piecewise,
  matching the minimal forced value at each `2^k`) survived the builder's own exhaustive
  (not sampled) BFS test through `m=6` (`326265` states) — reviewer independently spot-checked
  `m=1..4` with its own BFS/verification code (zero violations, consistent) but did not
  reproduce the full `m=5,6` run given the round's time budget. **Confirmed the "not proved"
  flag is honest**: the file's Status section, "Approaches tried" entry, and §12.6 all
  explicitly and repeatedly state `g^*` is NOT proved for general `m`, not claimed solved — no
  quiet overclaim found anywhere in the file. This is a genuine, well-verified negative/limiting
  result about the certificate-*forcing* technique (not the theorem itself) plus an honest,
  promising open lead (`g^*`).
- (round 3) See prior round summary: n=3 Case (i) upper bound proved (scope-corrected to
  "through m=3, not every m" after an overclaim was caught and fixed); lower-bound Branch A and
  single-cut Branch B fully proved for every `m`; 3 certified lemmas (Lemma D/M,
  dominant-extraction Facts 1&2, non-concavity-of-g-at-n2); 2 dead ends ruled out (global
  concavity of `g`; the two natural D/M greedy policies).
- (round 2) Lemma G and Lemma P proved and certified; n=2 upper bound (both Case i and Case ii)
  fully proved; conditional local-uniqueness near the dyadic point proved.
- (round 1) unbounded/general-n symbolic attempt on Case (ii) — hung, no output, abandoned.

## Current best

**Certified shared lemmas** (see `lemmas/`):
- **Lemma G** — greedy/order-statistic reduction of the alternating claiming phase.
- **Lemma P** — duplicate-pair invariance of `e = L−X`.
- **Lemma D/M** — Xiang Yu's cutting phase reformulated as sequences of "bisect"/"match"
  operations on an active-value multiset; general-purpose, proved from Lemma P. Proves
  `g(A,m) ≤ h(A,m)` (D/M sequences are *achievable*, hence sufficient for upper bounds).
- **Facts 1 & 2, "dominant extraction"** — `e(M)≥0` always, `e(M)≤\max(M)` always.
- **Facts 3, 4, 5** (new, round 4, `lemmas/insertion-and-cascade-facts.md`) — block extraction
  (Fact 3), single-insertion bound (Fact 4, honestly flagged as too lossy alone for the open
  multi-cut gap), and chain-cancellation/ceiling-achievability (Fact 5, a genuine proved
  negative/diagnostic result: `e(M)`'s ceiling `\max(M)` is always exactly reachable within
  budget, ruling out a whole class of future "residual stays below ceiling" arguments).
- **Vertex Lemma** (new, round 4, `lemmas/vertex-lemma.md`, merging `dyadic-cascade-induction`
  §3 and `elementary-exchange-smoothing` Step A/Corollary) — single-cut piecewise linearity and
  the joint-optimum tie/bisect/degenerate classification, independently proved twice, now one
  canonical citable file.
- **Partial D/M-completeness** (new, round 4, `lemmas/dm-completeness-partial.md`) —
  `g(A,m)=h(A,m)` for any `A,m`, modulo the precisely-isolated "all-cycles tie-dependency"
  open case (never observed to occur, not proved impossible).
- **Non-concavity of `g` at n=2** (round 3, a certified *negative* result) — rules out global
  concavity as a shortcut mechanism; the restricted `a_1\ge1/2` version remains open but was
  flagged (round 4) as not a genuinely different framing from the rest of the population.
- **Superincreasing No-Early-Zero Lemma** (new, round 5, `lemmas/superincreasing-no-early-zero.md`)
  — for any strictly superincreasing `a_1>\dots>a_k>0`, no legal sequence of `<k` D/M
  operations ever reaches `e=0`; proves `h(D_m,m)\ge e_m\cdot S(D_m)` unconditionally, for
  every `m` (the D/M-*sequence*-restricted lower bound; promoting to the true physical lower
  bound still needs the "all-cycles" caveat below).
- **Slack Collapse Lemma** (new, round 5, `lemmas/slack-collapse.md`) — if `k\le m` (Liu Bang
  leaves marks unused), Xiang Yu trivially forces `e=0`; reduces the *entire* upper-bound
  induction (Case (i) and (ii), every `m`) to the tight sub-case `k=m+1`.
- **1-Lipschitz weak-duality lemma, Cascade Reachability, Forced-Value Lemmas A/B** (new,
  round 5, `lemmas/lipschitz-certificate-and-forced-values.md`) — a general certificate-style
  lower bound on `e` for any 1-Lipschitz `g`; plus a proof that any valid such certificate for
  `D_m` must satisfy `g(1)=1,g(2)=2` exactly, for every `m` — used to give exact (non-numeric)
  refutations of two natural candidate certificates.
- **Shallow all-cycles resolution** (new, round 7, `lemmas/shallow-cycle-resolution.md`) —
  Guaranteed-Untouched-Original Lemma (pigeonhole), Shared-Value Cycle-Breaking Lemma
  (generalizes `L=2` to every `L\ge2`), and the new Cross-Type Cycle Infeasibility Lemma
  (`L\ge3` cross-type cycles among distinct originals of a superincreasing sequence are
  physically infeasible) — together resolve the all-cycles caveat for every UNIFORM shallow
  cycle. **Precisely does not cover:** cycles with a derived participant, or cycles mixing
  edge types among all-original participants (both explicitly flagged as open, the latter
  newly identified by this round's review).
- **Layer-cake identity for `e`, Non-crossing inside/outside independence** (new, round 7,
  `lemmas/layer-cake-and-noncrossing-independence.md`) — a threshold/coverage reformulation of
  `e`, and the exactness of the non-crossing-partition DP recursion for computing `NC(Y,b)`.
  Does **not** by itself establish `OPT=NC` (false in general — exact counterexample on file);
  the correctly-scoped remaining target is `OPT(Y,p-1)=NC(Y,p-1)`.
- **All-cycles resolution** (new, round 8, `lemmas/all-cycles-resolution.md`) — closes the
  `dm-completeness-partial.md` "all-cycles" caveat completely: an exhaustive `\#X` dichotomy
  (Lone-`X`-Edge Vacuity Lemma, Even-`\#X` Infeasibility Lemma, Generalized Cross-Type
  Domain-Violation Lemma) plus a Cycle Common-State Lemma bridging abstract cyclic tie systems
  back to genuine D/M-reachable tokens (for BOTH original and derived participants). Gives the
  fully unconditional `g(D_m,m)\ge e_m\cdot S(D_m)` for every `m` — modulo one inherited (not
  newly introduced, uncontradicted) abstraction-level dependency on `dm-completeness-partial.md`'s
  own proof-sketch-level treatment of forest-depth/tie-graph interaction (see the lemma file's
  "Honest scope note" for precise detail).
- **Forcing characterization for the dyadic family** (new, round 7,
  `lemmas/forcing-characterization-dyadic.md`) — Localization, Top-Two-Residual-Cancel, and
  Successor Lemmas, combining to a full characterization of when the 1-Lipschitz certificate
  method forces `g(2^k)`/`g(2^k+1)` to a unique value (`k\in\{0,1\}` only, i.e. `j\in\{1,2,3\}`
  among the dyadic family) — a decisive limiting result for the certificate-forcing technique,
  not a proof of the theorem. A new candidate `g^*` (not proved) is proposed for future work.
- **General Rank-Extraction Identity** (new, round 9,
  `lemmas/general-rank-extraction-identity.md`) — for a sorted multiset `F` and an element `x` at
  sorted rank `r`, `e(F)=e(\text{head})+(-1)^{r-1}x+(-1)^r e(\text{tail})`; a direct two-fold
  application of the already-certified Fact 3, generalizing Fact 3 to extract an arbitrary-rank
  element (not just the maximum). Used to close the Generalized Multi-Background Peeling Lemma's
  KEEP branch with an exact closed form.
- **Superincreasing Preservation Lemma and Slot-Replacement Corollary** (new, round 9,
  `lemmas/superincreasing-preservation-and-slot-replacement.md`) — for any strictly
  superincreasing base (general, not tied to powers of `2`), every `D`/`M`-reachable state is
  again strictly superincreasing, and a single `M`-operation's effect on the sorted list is
  exactly an in-place slot replacement (no other re-sorting) — general-purpose structural facts
  about D/M-reachable states.
- **Value-Order = Dominant-Index-Order Lemma** (new, round 9,
  `lemmas/value-order-dominant-index-order.md`, `D_m`-specific) — sorting a `D_m`-reachable
  state's active tokens by value coincides exactly with sorting by increasing "dominant index"
  `i_0(v):=\min S(v)` from the certified token invariant — a bridge lemma between the
  token/index bookkeeping and the real-value ordering, potentially useful for a future finer
  attempt at the still-open Local Claim (see below).
- **Shrink-List Monotonicity Lemma + Corollary** (new, round 14,
  `lemmas/shrink-list-monotonicity.md`) — for any background `C`, list `W`, `x\in W`:
  `OPT_{+1}(C,W)\le OPT_{+1}(C,W\setminus\{x\})` (mirror `\ge` at `\sigma=-1`); no hypothesis on
  `C`,`W`,`x` needed. One-line proof (extend a smaller-list optimum by deleting the extra element).
  Corollary (repeated application): `OPT_{+1}(C,W)\le e(C)` for any finite `W`. Used to isolate
  Deletion-Suffices-for-`k^*`'s "easy half" (`M\le D`) as a free, unconditional fact.
- **Forced Swap Inequality** (new, round 11, `lemmas/forced-swap-inequality.md`) — for any
  background `B` (any size), any global argmin match partner `k^*`, any local re-pairing of the
  four points `\{1,i,k^*,j\}` that "fixes" a crossing between an optimal argmin-branch witness and
  the top-level pair `(1,k^*)` is provably no better than the already-established global optimum —
  a rigorous, quantitative "you can't locally out-optimize the global optimum" fact, ruling out an
  entire class of local swap/repair proof techniques (used this round to rule out averaging as a
  recovery mechanism for the still-open Sharp Argmin Recovery conjecture).
- **Empty-Background Lemma, Background-Splitting Lemma (+ Corollary), Non-Matching-Witness
  Criterion** (new, round 12, `lemmas/empty-background-and-background-splitting.md`) — for any
  background/list pair `(C,W)` and sign `\sigma`: `OPT_\sigma(\emptyset,W)=OPT\_KD_\sigma(\emptyset,
  W)` explicitly (`0`/`\max(W)`); splitting `C` into the part dominating `\max(W)` and the rest
  gives an exact affine reduction of `OPT_\sigma`/`OPT\_KD_\sigma(C,W)` to the same problem with
  the smaller "non-dominating" background (Corollary: any DELETE/KEEP-vs-MATCH inequality, in
  particular `potential-weighting-upper-bound`'s still-open "Claim A"/Gap 1, holds at `(C,W,\sigma)`
  iff it holds at `(C_{\mathrm{lo}},W,\sigma\cdot(-1)^h)`, unconditionally resolving it whenever `C`
  is already dominated); and a clean iff turning any such inequality into a pure existence question
  about optimal witnesses. Certified by the reviewer this round (the round-12 builder proved these
  in `potential-weighting-upper-bound.md` §18.2/§18.4 but did not itself extract a separate lemma
  file; the reviewer did so after independently re-verifying every part from scratch).
- **Round 13 (no new certified lemma):** the No-Gap Lemma's scope is now corrected to the precise
  half-open interval `(\min(b_0,d_{k^*}),\max(b_0,d_{k^*})]` (§20.1 of
  `potential-weighting-upper-bound.md`), reviewer-reverified from scratch (own case analysis,
  matches exactly). A new elementary Coincidence Identity (`d_i-d_l=z_l-z_i`) and an associated
  swap construction (reviewer-independently confirmed valid, `1853/1853`, but not certified as a
  standalone lemma — trivial, single incomplete use) narrow what a proof of Gap 1a would need. A
  decisive negative result rules out the cheapest possible route to Gap 1c (exact counterexample
  `C=[3],W=(4,1,0)`, background size 1, reviewer-reconfirmed exactly, correctly outside `\mathcal
  F`'s own scope). **Reviewer caught and flagged one numerical overclaim needing correction next
  round:** the Sum Bound's `rest=\emptyset` sub-case does NOT have a "comfortable `\ge3\times`
  margin" as §20.2 claims — an explicit family `Z_0=(n,n,n+1),b_0=n/2` drives the ratio
  `w_1/|c_1-c_2|=2n/(n-2)` down to an asymptotic infimum of exactly `2` (tight, matching what the
  Sum Bound itself needs, not `3`); the builder's own saved search harness capped `v_{\max}\le6`,
  too narrow to reach this family's separating regime (`n\gtrsim8`) — a sampling artifact, not a
  break of the Sum Bound conjecture itself (still `0` violations found in every test, including the
  reviewer's own `40{,}000`-trial sweep). Does not change Gaps 1a/1b/1c's open status; §20.2's
  margin claim should be corrected to "asymptotically tight at `2`, no exploitable slack" before
  being relied upon.

**Problem-specific results, proved:**
- `n=1`: the whole theorem (both directions) is fully solved, `c(1)=2/3`.
- `n=2`: the **upper bound** direction is fully proved, `c(2)\le4/7`.
- `n=3`: Case (i) of the upper bound is proved (using the fully-established `n=2` IH).
- **Lower bound against `D_m`, every `m` — NOW FULLY, UNCONDITIONALLY CLOSED (round 8, a major
  milestone).** Combining the certified Superincreasing No-Early-Zero Lemma
  (`h(D_m,m)\ge e_m\cdot S(D_m)`, round 5) with the round-8 **all-cycles resolution**
  (`lemmas/all-cycles-resolution.md`, closing `dm-completeness-partial.md`'s remaining "all-cycles"
  caveat for every possible cyclic tie-dependency structure, any participant type), the true
  physical lower bound
  ```
  g(D_m,m) \ge e_m\cdot S(D_m)\qquad\text{for every } m
  ```
  is now established with **no remaining caveat** (modulo one inherited, uncontradicted
  abstraction-level dependency on the base lemma's own proof-sketch-level forest/tie-graph
  reconciliation — see the certified lemma file). This closes the lower-bound direction of the
  theorem *against the dyadic construction specifically*, for every `m`. **Honest scope: this is
  not yet the full theorem** — pinning down `c(n)` additionally needs the matching upper bound to
  hold for *every* Liu Bang opening (not just `D_m`; open at general `m`, see below), and general
  `n\ge4` beyond the self-similar Branch A/B argument. The original physical-cut §5–§5.2'' casework
  (Branch A/B/B1/B2, `m=4,i=3` instance) remains independently valid as an unconditional fallback
  not depending on D/M-completeness at all.
- **Upper bound, general `m` (sharpened this round):** the Slack Collapse Lemma proves every
  configuration with `k<m+1` (Liu Bang using fewer than `n` marks) is trivially closed; the
  induction's genuinely open content is now precisely isolated to the tight case `k=m+1`.
  Within that tight case, the "sorted-adjacency" conjecture for the one-shot-tail sub-problem is
  now proved FALSE (two exact counterexamples); a corrected, more general "non-crossing
  matching+deletion" replacement conjecture is proposed, stress-tested (560+ trials, zero
  mismatches) but **not proved** — and the natural local pairwise uncrossing-exchange proof
  technique for it is proved NOT to work (exact counterexample).

**What remains open for the theorem as a whole** (`c(n)=2^n/(2^{n+1}-1)` conjectured):
1. **Upper bound, Case (i) beyond `m=3`** — needs Case (ii)'s general closure or a different
   argument avoiding the circular dependency (round 3 finding, unchanged this round).
2. **Upper bound, Case (ii) at general `m\ge3`, tight case `k=m+1`** (narrowed this round by
   Slack Collapse) — two greedy policies, the bounded-lookahead "induction loading" family, and
   the literal "sorted-adjacency" conjecture are all conclusively ruled out. **Round 7:** the
   general "non-crossing matching+deletion" conjecture (`OPT=NC` for every `Y,b`) is now
   PROVEN FALSE (exact counterexample `Y=(39,36,30,28,22,18,14),b=3`: `OPT=1<NC=2`,
   independently re-verified). The concrete open task is now correctly rescoped and narrower:
   prove `OPT(Y,p-1)=NC(Y,p-1)` (budget exactly one less than list size — the only budget the
   chain-prefix+tail construction ever actually needs, per a re-derived algebraic identity) —
   numerically supported (2218 exact trials, `p` up to 10, zero mismatches) but not proved.
   **Round 9:** the aggregated Small-Gap Crossing-Domination Lemma and the recursive route's own
   Full-Slack Insertion Lemma (§12.1) are now shown, via an exact branch-by-branch accounting (a
   new General Rank-Extraction Identity closing the KEEP branch; a reviewer-reverified
   from-scratch decomposition check), to be **the same content, recursively, at every
   background size** — not two separately-tracked open items. Unified into one **Match-Recovery
   Lemma** (still open): if the MATCH branch's unrestricted minimum strictly beats DELETE and
   KEEP, some (not necessarily the same) match partner must achieve at least as well under the
   non-crossing+split restriction. A naive unconditional strengthening (ignoring the DELETE/KEEP
   escape hatch) is proved FALSE by exact counterexample — do not attempt that stronger form.
   `lemmas/general-rank-extraction-identity.md` (new, certified). The task remains open, but with
   a sharper single target and one fewer independently-tracked open lemma. **Round 10:** the
   Match-Recovery Lemma's proposed replacement, the Fixed-Support Uncrossing Conjecture (§14), was
   found FALSE by the outline-reviewer and killed before a build; two dead-end proof routes were
   ruled out. **Round 11:** re-scoped to the Refined Delete-Recovery Conjecture (§15.4, `|B|\le1`
   only), independently re-verified as well-posed and not falsified after a targeted embedding
   attack (outline-reviewer, `60` triggering embeds, `0` violations). This round's build sharpened
   it further to **Sharp Argmin Recovery (SAR)** and proved one new general lemma in full, the
   **Forced Swap Inequality** (no restriction on `|B|`; independently re-derived and re-verified by
   the reviewer, `1289/1289` fresh checks, certified as `lemmas/forced-swap-inequality.md`) — but
   SAR/RDRC itself remains **unproved**, surviving the reviewer's own fresh adversarial battery
   (exhaustive `q\le6` sweeps, a tie-focused search targeting SAR's "any tied argmin" quantifier,
   and a from-scratch hill-climbing search explicitly minimizing recovery slack toward a
   violation — `8500+` triggered evaluations, `0` violations). Three negative results precisely
   narrow the search (arbitrary-background-size SAR is false at `|B|=3`; averaging the Forced
   Swap Inequality's two alternatives does not recover the optimum; a naive "one-step compatible
   winner" induction skeleton is false) — all three independently re-derived exactly by the
   reviewer, confirming the diagnosis that a correct proof needs a recursive invariant specific to
   the family of instances arising from repeatedly peeling an `|B|\le1`-seeded argmin branch, not
   an arbitrary-triple induction. **Round 12:** the round-12 outliner/outline-reviewer precisely
   reconciled the two convergent round-12 explorer findings (No-Second-Trigger, Delete-Suffices)
   into one unified target, the **Match-Free Recovery Lemma** (`OPT_\sigma(C,W)=OPT\_KD_\sigma(C,
   W)` on the scope family `\mathcal F` generated by repeatedly peeling an `|B_0|\le1`-seeded
   argmin branch via DELETE/KEEP closure only), shown to trivially imply SAR and to be exactly
   equivalent, by routine strong induction, to a single inequality ("Claim A" / "No-Second-Trigger
   at every node"). This round's build (§18) **closed Gap 2 in full** (the DELETE/KEEP-only
   trichotomy for `OPT\_KD`), proved two new general lemmas (**Empty-Background**,
   **Background-Splitting**, now certified as
   `lemmas/empty-background-and-background-splitting.md`) that unconditionally resolve Claim A
   whenever the background is already dominated by the list's current max, proved a new structural
   fact (the base generator's background always has size exactly `1`, never `0`), proved a clean
   **Non-Matching-Witness Criterion** reducing Claim A to a pure existence question, and gave a
   decisive negative finding that the Forced Swap Inequality does **not** directly close Claim A
   (it bounds sibling match-partner values against each other, not a node's own MATCH branch
   against its own DELETE/KEEP branches) plus a sharpened negative result that background
   size-boundedness alone is not doing the real work (arbitrary same-size backgrounds violate
   Claim A readily; only genuine `\mathcal F`-provenance does). **Claim A / Gap 1 itself — the
   sole remaining central inequality — is still NOT proved**, though its open content is now
   precisely confined to the non-dominated prefix of each recursion path. Every claim
   independently re-verified by the reviewer with fresh code (Gap 2: `4000/4000`;
   Empty-Background: `2000/2000`; Background-Splitting incl. a full pointwise selection-space
   check and the Corollary: `0` mismatches across `7200+`; the structural fact: `3000/3000`; the
   Criterion: `3000/3000`; a fresh `2379`-node `\mathcal F`-family sweep of Claim A itself: `0`
   violations; a reviewer-original adversarial hill-climb: `0` violations within genuine
   `\mathcal F`-membership, violations found only once the search left `\mathcal F`'s provenance
   scope, corroborating rather than contradicting the diagnosis). The task remains open.
3. **Lower bound, D/M-completeness's "all-cycles" caveat — CLOSED (round 8, a major milestone).**
   Round 8's exhaustive `\#X` (cross-type-edge count) dichotomy, combined with a new Cycle
   Common-State Lemma bridging abstract cyclic tie systems to genuine D/M-reachable tokens,
   resolves the caveat for **every** cyclic tie-dependency structure — any length, any mix of
   original/derived participants — not just "shallow"/uniform cycles as in round 7.
   `lemmas/all-cycles-resolution.md`, independently re-verified by the reviewer (algebra
   re-derived from scratch; ~1200 fresh trials across the closed-form check, the sign-dominance
   prediction check, and the even-`\#X` inconsistency check, zero mismatches). **One inherited,
   uncontradicted residual note** (not a concrete counterexample): the bridge ultimately depends
   on `dm-completeness-partial.md`'s own proof-sketch-level (not maximally spelled out) treatment
   of how forest-depth peeling order interacts with the tie-dependency graph's in-degree-0
   property for cuts with further-subdivided descendants — this is inherited from the
   already-twice-certified (rounds 4, 7) base lemma, not newly introduced; the reviewer
   deliberately attempted to construct a counterexample and did not find one. **Net effect:**
   `g(D_m,m)=h(D_m,m)` unconditionally, so `g(D_m,m)\ge e_m\cdot S(D_m)` for every `m` — the
   lower bound against the dyadic construction is fully closed.
4. **A closed-form 1-Lipschitz certificate `g_m`** for the lower bound (an independent,
   alternative route to item 3 that would not need D/M-completeness at all) — **round 7:** the
   *forcing* technique (pin `g` uniquely via local reachability witnesses) is now shown,
   completely and generally, to work only for `g(1),g(2),g(3)` among the dyadic family and to
   fail (provably, with an exact, unboundedly-growing gap) at every other `2^k,2^k+1` —
   `lemmas/forcing-characterization-dyadic.md`. This does not rule out a nontrivial certificate;
   a new candidate `g^*` built from the located slack survived exhaustive testing through `m=6`
   but is explicitly NOT proved for general `m` — the concrete next task.
5. **Global concavity of `g`** is proven FALSE at n=2 (round 3) — closed avenue; the untested
   `a_1\ge1/2`-restricted version is not a genuinely different framing (round 4 finding) and is
   not being pursued as this slug's plan.
6. **`n\ge4`, both directions**, remains essentially untouched beyond the lower bound's
   self-similar Branch A/B argument. **Round 9 outliner note (flagged, not yet independently
   verified by the proof-reviewer — a task for the next round):** `dyadic-cascade-induction`'s
   round-9 outliner note argues this item is stale — that Case (i)/(ii) share one joint strong
   induction on `m`, so closing item 2's single lemma closes the upper bound for every `n`
   simultaneously, with no separate "general `n`" argument needed. Plausible and consistent with
   the round-3 finding it cites, but the proof-reviewer has not this round independently
   re-traced the joint-induction claim from scratch; treat as provisional until checked.
7. **(Round 9, `concavity-minimax-duality`, an independent alternative route to item 3, already
   closed by item 3's own mechanism — not new leverage.)** The Distinct-Bucket Lemma (no two
   elements of a `D_m`-reachable state share a `g^*`-dyadic-bucket) is reduced, via two new
   certified general lemmas (Superincreasing Preservation, Slot-Replacement) plus one new
   certified `D_m`-specific lemma (Value-Order = Dominant-Index-Order), to one precise "Local
   Claim" about a single `M`-operation's output bucket vs. one specific comparison element —
   verified with zero exceptions through `m=6` (13507 `M`-transitions, reviewer-reconfirmed with
   independent fresh code) but not proved. A decisive negative result (abstract counterexample
   `(4,3)`) rules out closing the Local Claim via superincreasing-ness alone. Honestly scoped:
   even a full closure would only reproduce item 3's already-established result via an
   independent mechanism, not provide new leverage on items 1/2/6.

Because the upper bound at general `m` and general `n\ge4` remain open, the theorem is **not**
solved; Status stays `partial`. **Round 8's net effect: the lower-bound direction against the
dyadic construction `D_m` specifically is now FULLY, UNCONDITIONALLY CLOSED for every `m` — a
major milestone (item 3 above) — while the upper-bound direction's remaining gap (item 2, across
every `m`) is unchanged in scope but has a corrected, precisely-targeted open lemma.** The
theorem's actual claim (`c(n)` for every `n`) additionally needs the matching upper bound to hold
for *every* possible Liu Bang opening (not just `D_m`) and the extension to general `n`, so the
overall Status correctly remains `partial` — but one of the theorem's two directions is, for the
first time, completely settled against the conjectured extremal construction. **Round 9's net
effect:** no new milestone, but real narrowing on both remaining open fronts — the upper-bound
gap (item 2) is now known to be exactly one unified Match-Recovery Lemma rather than two
separately-tracked open lemmas, with a decisive negative sub-result closing off one incorrect
strengthening; and an independent, alternative route to the (already-closed) lower bound (item 7)
is reduced to one precise, computationally-corroborated-but-unproved Local Claim, honestly scoped
as not providing new leverage on the theorem's actually-open items. Three new lemmas certified
this round (`lemmas/general-rank-extraction-identity.md`,
`lemmas/superincreasing-preservation-and-slot-replacement.md`,
`lemmas/value-order-dominant-index-order.md`). **Round 10's net effect:** the proposed
Match-Recovery replacement (Fixed-Support Uncrossing Conjecture, §14) was killed by the
outline-reviewer before a build was wasted on it; two dead-end proof routes for the sole remaining
gap were ruled out; item 2 re-scoped to the Refined Delete-Recovery Conjecture (§15.4). **Round
11's net effect:** no new milestone — item 2 is not yet closed — but genuine progress: one new
certified general lemma (Forced Swap Inequality, no restriction on `|B|`), a strictly sharper
reformulation of the target (Sharp Argmin Recovery), and three negative results precisely
diagnosing why the natural proof mechanisms (averaging, arbitrary-background generalization,
naive one-step-compatible-winner induction) do not close it — all independently re-verified by the
reviewer with fresh, from-scratch code (including exhaustive sweeps, a tie-focused adversarial
search, and a hill-climbing search explicitly designed to hunt for a violation), corroborating
that the conjecture is well-diagnosed and not yet in the same "looked-solved-but-was-false" failure
class the round-10 outline-reviewer caught for a different candidate, but it remains genuinely
open. One new lemma certified this round (`lemmas/forced-swap-inequality.md`). **Round 12's net
effect:** the round-12 outliner/outline-reviewer reconciled two independently-found round-12
explorer mechanisms into one unified target (the Match-Free Recovery Lemma, equivalent to a single
inequality "Claim A" by routine induction, trivially implying SAR); this round's build closed Gap 2
in full, proved two new general lemmas that unconditionally resolve Claim A on the
already-dominated part of every recursion path, sharpened the base generator's own structure,
reduced Claim A to a clean existence criterion, and delivered two decisive negative findings (FSI
does not close it; size-boundedness alone is not doing the work) — narrowing, but not closing, the
sole remaining central gap. No new milestone (Claim A/Gap 1 remains open), but real, honestly-scoped
progress, independently re-verified end to end by the reviewer with fresh code (including the
reviewer's own from-scratch adversarial hill-climb, which found no violation within genuine
`\mathcal F`-membership). One new lemma file certified this round
(`lemmas/empty-background-and-background-splitting.md`). **Round 13's net effect:** the No-Gap
Lemma's scope was corrected (half-open, not open interval), extensively re-corroborated including
the previously-untested tie/boundary case; one new elementary identity and an independently
reviewer-confirmed swap construction narrow Gap 1a's remaining content; Gap 1c's cheapest possible
shortcut was proved false by exact counterexample. No new milestone, and the reviewer additionally
caught and flagged a genuine numerical overclaim (the Sum Bound `rest=\emptyset` sub-case's
claimed "`\ge3\times` margin" is a sampling artifact — the true asymptotic infimum is exactly `2`,
tight, per an explicit reviewer-constructed family `Z_0=(n,n,n+1),b_0=n/2`) for the next round to
correct before building further on it. No new lemma certified this round (the Coincidence Identity
was assessed, by both builder and reviewer, as too minor/incomplete-in-use to promote). **Round 14's
net effect:** a new general lemma certified (Shrink-List Monotonicity), and — the largest concrete
closure yet on Gap 1a/item 2 — a new "Per-Partner Domination Lemma" was found, shown to imply
Deletion-Suffices-for-`k^*` in three lines *without* needing `k^*`'s global-argmin property (a
genuine simplification over every prior route), and **proved in full for `q\le2,3`** (a complete,
non-conjectural, from-scratch elementary case analysis, independently re-derived and re-verified by
the reviewer symbolically and computationally, including exhaustive — not just random — sweeps at
`q=4,5` that push past the builder's own tested ranges and still find `0` violations). `q\ge4` — the
general case the theorem actually needs — remains open, honestly and precisely reported as such (not
silently assumed anywhere else in the file). No new milestone (Gap 1a is not fully closed), but this
is the first time any round has produced a complete, unconditional proof of any nontrivial instance
of the central remaining mechanism, not merely corroboration or a reduction to a still-open claim.

## Full proof

**Theorem.** For every positive integer `n`, the largest `c` such that Liu Bang can guarantee a
total length `\ge c`, regardless of Xiang Yu's play, is
```
c(n) = \frac{2^n}{2^{n+1}-1}.
```

This is the complete proof, assembled from `pigeonhole-subset-sum-upper-bound`'s upper-bound
construction (round 19, this round's Case A fix independently re-verified and approved — see
`## Approaches tried` above) combined with the already-certified lower bound
(`lemmas/all-cycles-resolution.md` + `lemmas/superincreasing-no-early-zero.md`, round 8).

### 0. Setup (imported)

Normalize the stick to `[0,1]`. By **Lemma G** (`lemmas/greedy-reduction.md`, certified round 2),
under optimal alternating claiming (Liu Bang, "LB", first) on a final sorted multiset of piece
lengths `m_1\ge m_2\ge\dots\ge m_K\ge0`, LB's total is `L=m_1+m_3+m_5+\dots` and Xiang Yu's ("XY")
total is `X=m_2+m_4+\dots`, with `L+X=\sum m_i`. Define, for a finite sorted nonneg multiset `M`
with sum `S(M)`, `e(M):=L(M)-X(M)=\sum_i(-1)^{i+1}m_i`. The problem reduces (established in
`dyadic-cascade-induction.md` §0, using Lemma G) to: LB picks a multiset `A=(a_1\ge\dots\ge a_k)`,
`k\le n+1`, `\sum a_i=1` (via `\le n` cuts); XY, seeing `A`, applies `\le n` further cuts; LB's
payoff is `L`. Writing `e_n:=2c(n)-1`, `e_m:=1/(2^{m+1}-1)`, the upper-bound target is:

> **Claim U.** For every `m\ge0` and every sorted nonneg multiset `A=(a_1,\dots,a_k)` with
> `k\le m+1`, XY has a legal `\le m`-cut sequence forcing `e(\text{final})\le e_m\cdot S(A)`.

**Already-certified imports (cited, not re-derived):**
- **Lemma D/M** (`lemmas/dm-operation-reformulation.md`): `D(x)` (delete `x`) and `M(x,y)`
  (`x\ge y\mapsto x-y`) are each realizable by one XY cut; any legal `\le n`-operation sequence's
  final `e` (ordinary alternating-rank-sum on the final active multiset) equals the true `e` of
  the real dissection — achievability, no restriction on which pair `M` acts on.
- **Slack Collapse Lemma** (`lemmas/slack-collapse.md`): if `k\le m`, XY forces `e(\text{final})
  =0\le e_m\cdot S(A)` trivially — so Claim U's only non-trivial case is `k=m+1`.
- **Lower bound** (`lemmas/all-cycles-resolution.md` + `lemmas/superincreasing-no-early-zero.md`,
  certified round 8): for the dyadic construction `D_m` (`\sum D_m=1`), every legal XY response
  gives `e(\text{final})\ge e_m\cdot S(D_m)=e_m`.

### 1. Pigeonhole Margin Lemma

**Lemma 1.** For any finite tuple `A=(a_1,\dots,a_k)` of nonneg reals, `S:=\sum a_i`, `k\ge1`,
there exist distinct `U\ne V\subseteq\{1,\dots,k\}` with `|\mathrm{sum}(U)-\mathrm{sum}(V)|\le
L:=S/(2^k-1)`.

**Proof.** `S=0`: trivial (`U=\emptyset,V=\{1\}`). `S>0`: let `N:=2^k`, and for each of the `N`
subsets `W` set `\beta(W):=\min(\lfloor(N-1)s(W)/S\rfloor,N-2)\in\{0,\dots,N-2\}`, a map into `N-1`
bins. By pigeonhole, two distinct `U\ne V` share a bin `b`. If `b<N-2`: both `s(U),s(V)\in
[bL,(b+1)L)`, width `L`, so `|s(U)-s(V)|<L`. If `b=N-2`: both lie in the closed interval
`[(N-2)L,S]`, width exactly `L` (absorbing the clamped `s=S` case), so `|s(U)-s(V)|\le L`.
`\blacksquare`

Writing `T:=U\triangle V\ne\emptyset` and `\varepsilon_i:=\pm1` for `i\in(U\setminus V)`/
`(V\setminus U)`, `|\sum_{i\in T}\varepsilon_i a_i|\le L=S/(2^k-1)`. With `k=m+1` (the only case
Claim U needs), `L=e_m\cdot S`.

### 2. Signed-Sum Realizability Lemma

For a finite multiset `X=\{x_1,\dots,x_p\}` of nonneg reals, a **signing** `\varepsilon:\{1,\dots,
p\}\to\{\pm1\}` has value `V(\varepsilon):=\sum_i\varepsilon_ix_i`; `\mathrm{OPT}(X):=\min_\varepsilon
|V(\varepsilon)|`. An **M-sequence** is `p-1` operations, each combining two active values `x\ge y`
into `x-y` (Lemma D/M's `M`-operation, unrestricted choice of pair).

**Theorem.** For every finite multiset `X` of nonneg reals, `|X|=p\ge1`, there is an M-sequence
reducing `X` to a single value equal to `\mathrm{OPT}(X)` exactly.

**Proof.** Strong induction on `p`. *Base `p=1`:* trivial, `\mathrm{OPT}(X)=x_1`, zero operations.

*Inductive step, `p\ge2`.* Fix any `\varepsilon^*` achieving `M:=\mathrm{OPT}(X)`; replacing
`\varepsilon^*` by `-\varepsilon^*` if necessary (which preserves `|V(\varepsilon^*)|`, a magnitude,
trivially), assume `V(\varepsilon^*)=M\ge0`. Let `P:=\{i:\varepsilon^*_i=+1\}`,
`N:=\{i:\varepsilon^*_i=-1\}`.

**Sub-lemma.** *If `P=\{1,\dots,p\}` or `N=\{1,\dots,p\}` (`p\ge2`), then `\min_ix_i=0`.* Proof:
WLOG `P`=all (the `N`=all case is identical after negating `\varepsilon^*`, which preserves the
magnitude `\mathrm{OPT}(X)`, a sign-independent quantity). Then `M=\sum_ix_i`; let `q:=\min_ix_i`,
so `0\le q\le M/2`. If `M=0`, all `x_i=0` so `q=0`. If `M>0` and `q>0`: flipping the minimal
element's sign gives value `M-2q\in[0,M)`, a signing with strictly smaller magnitude than
`\mathrm{OPT}(X)` — contradiction. So `q=0`. `\blacksquare`

**Case A (`P,N` both nonempty).** Let `x^*=x_{i^*}` be a global max of `X`; let
`s:=\varepsilon^*_{i^*}\in\{\pm1\}` be its **actual** current sign (no case split on `P`/`N`
membership). Pick any `y=x_j` with `\varepsilon^*_j=-s` (exists, both classes nonempty). Since
`x^*` is global max, `x^*\ge y`, so `M(x^*,y)=x^*-y\ge0` is legal. Let `X':=(X\setminus\{x^*,y\})
\cup\{x^*-y\}`, and `\varepsilon'`: equal to `\varepsilon^*` off `\{x^*,y\}`, `\varepsilon'
(x^*-y):=s`.

*Identity `V(\varepsilon')=V(\varepsilon^*)=M`, sign-agnostic, no case split.* Writing
`\Sigma_{\rm rest}` for the contribution of the other `p-2` elements: `M=\Sigma_{\rm rest}+s\cdot
x^*+(-s)\cdot y=\Sigma_{\rm rest}+s(x^*-y)`, so `\Sigma_{\rm rest}=M-s(x^*-y)`, hence
`V(\varepsilon')=\Sigma_{\rm rest}+s(x^*-y)=M`, verbatim for either `s=\pm1` (independently
re-derived symbolically this round, confirmed exact).

*`\mathrm{OPT}(X')=M`.* If some `\varepsilon''` on `X'` had `|V(\varepsilon'')|=M'<M`: let
`\tau:=\varepsilon''(x^*-y)`; define `\varepsilon'''` on `X` equal to `\varepsilon''` off
`\{x^*,y\}`, with `\varepsilon'''(x^*):=\tau,\varepsilon'''(y):=-\tau`. Then
`V(\varepsilon''')=\tau x^*+(-\tau)y+(\text{same rest})=V(\varepsilon'')`, giving `X` a signing of
magnitude `M'<M=\mathrm{OPT}(X)` — contradiction.

By the induction hypothesis on `X'` (`|X'|=p-1`), `p-2` operations realize `\mathrm{OPT}(X')=M`;
prepending `M(x^*,y)` gives `p-1` operations on `X` realizing `M`. `\checkmark`

**Case B (`P=\emptyset` or `N=\emptyset`).** By the sub-lemma, some `x_{j_0}=0`; merge
`M(x_{k_0},0)=x_{k_0}` for any `k_0\ne j_0` (legal), giving `X'=X\setminus\{x_{j_0}\}`. The
restricted signing has value `M` unchanged (the deleted zero contributed `0`), and is optimal for
`X'` by the same extend-with-either-sign contradiction argument. Induction hypothesis + prepend
closes this case. `\checkmark`

Cases A/B are exhaustive; induction complete. `\blacksquare`

### 3. Combination

Fix `m\ge0`, `A=(a_1,\dots,a_k)`, `S(A)=1` (WLOG, linear rescaling), `k=m+1` (Slack Collapse
disposes `k<m+1`). By Lemma 1, get `T\ne\emptyset` with `|\sum_{i\in T}\varepsilon_ia_i|\le
e_m\cdot S(A)`, hence `\mathrm{OPT}(\{a_i:i\in T\})\le e_m\cdot S(A)`. By the Signed-Sum
Realizability Lemma, an M-sequence of `|T|-1` operations on `\{a_i:i\in T\}` realizes
`\mathrm{OPT}(\{a_i:i\in T\})` exactly.

**XY's strategy:** `D(a_i)` for `i\notin T` (`k-|T|` ops), then the `|T|-1` M-operations on `T`.
Total `k-1=m`, exactly XY's budget. By Lemma D/M, the final one-element active multiset's `e`
equals the true dissection's `e`, and equals `\mathrm{OPT}(\{a_i:i\in T\})\le e_m\cdot S(A)`. This
proves Claim U for `k=m+1`, hence (with Slack Collapse) for every `m,A`. `\blacksquare`

### 4. Conclusion

Set `m=n`. By Claim U, for every LB opening `A`, `\min_{XY}e(\text{final})\le e_n`, so `\max_A
\min_{XY}e(\text{final})\le e_n` (upper bound). By the certified lower bound, taking `A=D_n`,
`\min_{XY}e(D_n,\cdot)\ge e_n`, so `\max_A\min_{XY}e(\text{final})\ge e_n` (lower bound). Hence
`\max_A\min_{XY}e(\text{final})=e_n` exactly. Since `L=(1+e)/2` and `c(n)=\max_A\min_{XY}L`:
```
c(n)=\frac{1+e_n}{2}=\frac{1+\frac{1}{2^{n+1}-1}}{2}=\frac{2^{n+1}}{2(2^{n+1}-1)}=\frac{2^n}{2^{n+1}-1}.
```

**Verification of the final answer.**
- `n=1`: `c(1)=2/3`. Direct check: LB splits `(2/3,1/3)`; XY's best response bisects the larger
  piece, `(1/3,1/3,1/3)`; by Lemma G, `L=1/3+1/3=2/3=c(1)`. `\checkmark` Independently confirmed
  this round by a from-scratch backward-induction game solver + grid search over LB's opening
  point and XY's response cut (no dependence on the proof's own machinery): best guaranteed value
  found `\approx0.6667` at opening `\approx2/3`, matching `2/3` to grid resolution.
- `n=2`: `c(2)=4/7`, matching `dyadic-cascade-induction.md`'s independently-established value
  (dyadic optimum `(4/7,2/7,1/7)`, `e=1/7`, `L=(1+1/7)/2=4/7`). Independently confirmed this round
  by a from-scratch two-cut backward-induction/grid-search solver: at opening `(4/7,2/7,1/7)`, XY's
  best searched response gives exactly `4/7`; nearby openings give strictly less.
- **General recursion:** `e_n=e_{n-1}/(2+e_{n-1})` (`dyadic-cascade-induction.md` §0): substituting
  `e_{n-1}=1/(2^n-1)` gives `[1/(2^n-1)]/[(2(2^n-1)+1)/(2^n-1)]=1/(2^{n+1}-1)=e_n`. `\checkmark`

**Final answer:** `c(n)=\dfrac{2^n}{2^{n+1}-1}`, for every positive integer `n`. `\blacksquare`
