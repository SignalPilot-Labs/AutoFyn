# Round 16 proof-review — `potential-weighting-upper-bound` (imo-2026-03)

## Scope

Reviewed round 16's build on the sole live slug `potential-weighting-upper-bound`, specifically the
newly-appended §25 (outliner) and §26 (builder) of
`results/imo-2026-03/approaches/potential-weighting-upper-bound.md`, and the three newly-claimed
lemma files: `lemmas/sum-bound-base-case.md`, `lemmas/insertion-difference-identity.md`,
`lemmas/delete-suffices-insertion-domination.md`. Cross-read `/tmp/round-16/math-explorer-gap1a-*`,
`*-gap1b-*`, `*-gap1c-*`, `proof-outliner.md`, `outline-reviewer.md` for provenance and to check the
builder's work is responsive to (not blind to) the outline-reviewer's flags.

All verification below uses a **freshly-written harness**
(`/tmp/round-16/proof-reviewer-verify/`), not reusing the explorer's, outliner's, or builder's own
code. The harness (`defs.py`: an `e_sorted` alternating-sum function + a brute-force `OPT_σ` via
full recursive enumeration of every Keep/Delete/Match partition of a list) was validated against the
approach file's own four worked examples first — all four reproduced exactly:
`OPT_{+1}([5,8],(10,8,7,2))=0`, `OPT_{-1}(\cdot)=10`, `OPT_{+1}([1],(10,8,7))=0`,
`OPT_{-1}([2,4],(5,3))=4`.

## Verdict: **CHANGES REQUESTED** (Status: **partial**)

The builder's self-assessed Status (`partial`, none of Gaps 1a/1b/1c fully closed) is **correct and
not overclaimed**. Real, substantial, independently-confirmed progress was made. The technique
remains sound and this slug should continue to be the sole build target.

## Item-by-item independent verification

### (1) Sum-Bound Base Case Lemma — CONFIRMED, genuine complete proof, no gap

This is the round's headline claim: a full, unconditional proof (not merely a corroborated
conjecture) of Gap 1b's `rest=∅` (`q=3`) base case.

- **My own harness caught my own bug first** (worth flagging as a genuine finding about test
  methodology, not the proof): my first independent brute-force sweep produced **135/952** apparent
  violations. Root cause: I checked "trigger at `l`" as merely `A_{3,l}<A_1` without also requiring
  `A_{3,l}` be the actual global minimum over all partners (`k*` must be a genuine *global* argmin,
  not just satisfy a local comparison in isolation) — exactly the kind of sampler bug flagged in
  prior-round review lessons. After fixing this (require `A_{3,l}=\min_m A_{3,m}` **and**
  `A_{3,l}<A_1`), **0/4,473** violations across 20,000 raw trials (mixed integer/rational alphabets,
  `v_max` up to 80), and **0/65,520** on the isolated pure-algebraic core (own random sweep,
  independent of the game-level definitions).
- **Re-derived the ~10-line contradiction proof by hand from the lemma statement alone** (before
  reading the file's own write-up in detail) and it matches line for line: dichotomy
  `M=\min(D_{k^*},w_1-D_{k^*})` (singleton-list enumeration + certified Keep-Top Bound) combined with
  the two free bounds `A_1\le b_0` (Shrink-List Corollary) and `A_1\le w_1-b_0` (Step-1(†), uses
  `h=0`), contradiction resolves the sign of `D_{k^*}=|b_0-d_{k^*}|` and forces `w_1<d_{k^*}<w_1`
  under the negation — airtight.
- **Scope check:** confirmed (by grep and by re-reading §19-20) that restricting to `h=0` at this
  base case is legitimate, not a silent narrowing — the `h=1` and `h=2` sub-cases of `|C_lo|=2` are
  already handled elsewhere by the pre-existing, previously-certified Background-Splitting/No-Gap
  machinery (rounds 12-13), so `h=0` really is the only residual case here. Confirmed the lemma file
  states the scope restriction (`rest=∅` only, general induction still fully open) explicitly and
  prominently — no risk of a future round silently treating "Sum Bound" as proved.
- This is the population's **fourth** independent confirmation (round-16 explorer, outliner,
  builder, and now this review), all agreeing, from four differently-coded harnesses.
- **Certified as submitted, no changes needed.**

### (2) Insertion-Difference Identity — CONFIRMED, fully general, no gap

`e(M∪{d})-e(M)=(-1)^h(d-2e(tail_d))`, general `M`, `d≥0`, no distinctness/size hypothesis.

- Independently re-derived the two-step proof (Fact 3 block extraction to split `M`; General
  Rank-Extraction Identity to extract `d` from `M∪{d}` at rank `h+1`; eliminate `e(head_d)` between
  the two equations) — matches the file's derivation.
- **0/30,000** random trials (mixed-denominator rationals up to `v_max=200`) and **0/780** on a
  genuinely exhaustive small-value grid (5 values including `1/2,3/2` specifically to force ties —
  every `M` up to size 3, every `d`, all combinations) — my exhaustive count (`780`) matches the
  file's own exhaustive count exactly.
- Cross-checked the identity is consistent with the already-certified Fact 4 bound
  (`|e(Y∪{x})-e(Y)|≤x`) as a special case — holds.
- **Certified as submitted, no changes needed.**

### (3) Delete-Suffices Insertion Domination — CONFIRMED, correct, appropriately scoped

`OPT_{+1}(C,W)=e(C) \Rightarrow e(C)\le e(C\cup\{|w_a-w_b|\})` for any `w_a,w_b\in W`. Trivial
two-line proof (the match-`w_a,w_b`-delete-rest selection is one member of the minimization's search
space).

- **0/8,688** violations across genuine "deletion-suffices" trigger instances found in 20,000 raw
  random trials.
- Negative control (dropping the hypothesis): **36.3%** failures in my own fresh instance family —
  confirms the hypothesis is load-bearing, not window-dressing, consistent in substance with the
  builder's own `≈23%` figure (different sampling regime, same qualitative conclusion: a large,
  nonzero, genuinely load-bearing failure rate without the hypothesis).
- **Certified as submitted, no changes needed.**

### (4) The `ξ*=∅` boundary-case reduction (§26.3) — independently traced, confirmed NON-CIRCULAR

This is the round's most delicate claim, and the one most worth adversarial scrutiny per dispatch.
The builder claims: at a genuine top-level `F`-provenance node, if `∅` is the *unique* optimum of
`OPT_{+1}(B_1\cup\{d\},X)`, then the half-step conclusion `OPT_{+1}(B_1,X)\le OPT_{+1}(B_1\cup\{d\},X)`
follows via the chain `OPT_{+1}(B_1,X)\le e(B_1)\le e(B_1\cup\{d\})=OPT_{+1}(B_1\cup\{d\},X)`, where
the middle step uses the new Lemma (3) instantiated with `C=B_1`, `W=\mathrm{Res}=Z_1` (the **full**
top-level residual, not the smaller `X`), `w_a=u_1,w_b=u_j`.

**Circularity check (the crux of the adversarial task):** I traced exactly what hypothesis this
instantiation of Lemma (3) needs: `OPT_{+1}(B_1,Z_1)=e(B_1)`. I independently confirmed (by re-reading
§21.1) this is *literally* the pre-existing, independently-tracked conjecture "Deletion-Suffices-for-
`k*`" (Gap 1a's Step 2) — a statement about the base generator's own top-level recursive sub-problem,
already proved for `q\le3` since round 14 via a completely different mechanism (the Per-Partner
Domination Lemma), with no dependence on Gap 1c or the half-step anywhere in its own proof (grep-
confirmed: the round-14 proof of Deletion-Suffices-for-`k^*` at `q\le3` cites only Shrink-List
Monotonicity and the Rank-Extraction Identity's case analysis, nothing Gap-1c-related). So the
reduction genuinely runs **one way** (Gap 1a's Step 2 `\Rightarrow` this sub-case of Gap 1c), using an
independently-defined, independently-provable-elsewhere premise — **not** a hidden restatement of the
thing being proved. No circularity found.

Built a fresh end-to-end harness testing the *entire* chain, not just the isolated lemma: generated
genuine `F` base-generator nodes, filtered to genuine trigger+global-`k*`, checked whether
`OPT_{+1}(B_1,Z_1)=e(B_1)` holds at that instance (i.e. whether Deletion-Suffices holds there), and
when it does, for every `(u_1,u_j)` pair where `\emptyset` is confirmed the *unique* optimum of the
RHS problem (verified by exhaustively enumerating all selections of `X`, not just checking the
`OPT` value), checked both the intermediate step `e(B_1)\le e(B_1\cup\{d\})` and the full derived
conclusion `OPT_{+1}(B_1,X)\le OPT_{+1}(B_1\cup\{d\},X)` directly: **0/175** violations of either,
across `q\in\{3,4,5\}` (175 genuine `\xi^*=\emptyset$-unique instances found among 468 genuine
trigger+global-argmin nodes, matching the builder's qualitative finding that this sub-case is common,
not a corner case).

Also confirmed the well-definedness fix (canonical `\xi^*`: nonempty optimum if one exists among the
optima, `\emptyset` only if uniquely optimal) is a genuinely exhaustive, non-overlapping case split —
by construction every instance falls into exactly one of "nonempty optimum exists" (Step 3's target,
still open, §26.4) or "`\emptyset` uniquely optimal" (this reduction). No third case is missed.

**Honest scope, correctly stated by the file and confirmed by me:** this closes the `\xi^*=\emptyset`
sub-case only *conditionally* on Deletion-Suffices-for-`k^*`, which is itself proved only for `q\le3`
and open for `q\ge4`. The file does not overclaim this as an unconditional closure anywhere I could
find (grep-checked all uses of "resolved"/"closed" language in §26.3 — consistently qualified with
"conditional on").

### (5)-(7) Two-Touch Lemma's 5 structural sub-pieces (§26.5) — 3 proved confirmed, 2 open confirmed genuinely open

- **Base case `|W|\le2`:** trivial for `|W|\le1`; for `|W|=2,C=\{b_0\}` re-confirmed this is literally
  the certified Three-Bound Domination Lemma; for `|W|=2,C=\emptyset` the "keep both = match" identity
  is a one-line algebraic fact (`e_{sorted}(\{w_1,w_2\})=w_1-w_2=|w_1-w_2|`) — no proof risk, confirmed
  correct on inspection.
- **DELETE branch:** the candidate-set-inclusion argument (Two-Touch's candidate list only grows as
  `|W|` grows, so a minimum over the smaller list dominates the larger) is a clean, general,
  induction-free-at-this-step argument — re-traced, correct.
- **KEEP branch `b_0>w_1` sub-case — CONFIRMED, but my first test also had a sampler bug (a second
  one, worth flagging).** My first independent test of the claimed closed form
  (`\text{KEEP}=b_0-w_1$) produced widespread mismatches; root cause was **failing to enforce
  `w_1=\max(W)`** (the peeling formula's implicit hypothesis — `w_1` must genuinely be the top element
  being peeled, so every element of `rest` must be `\le w_1`). After enforcing this constraint,
  **0/3,000** mismatches — the formula is exactly correct, confirming the certified Empty-Background
  Lemma's application here (`OPT_{+1}(\emptyset,\mathrm{rest})=0$ unconditionally) is sound.
- **KEEP branch `b_0\le w_1` sub-case and MATCH branch:** both honestly reported as OPEN (needing a
  `\sigma=-1` mirror bound and a novel "Match-Branch Domination" sub-claim respectively), not silently
  assumed. Independently re-ran the Match-Branch Domination check with a fresh generator (own random
  `(b_0,W,w_j)` construction, exhaustive-partner sweep): **0/12,734** violations — strong corroboration
  matching the builder's `0/7,265`+`0/15,958`, but genuinely no proof found by either the builder or by
  my own brief attempt — correctly left open, not overclaimed as closed.
- **The dead-end general `|C|=2` Two-Touch formula — re-confirmed FALSE** with my own fresh test:
  **962/3,000 (32.1%)** failures, same order of magnitude and conclusion as the file's `~24%` and the
  outline-reviewer's own `18.0%` figure (benign sampling-shape variation across three independently
  designed tests, not a discrepancy) — this really is a hard structural wall, and I confirmed (by
  grep) it is correctly **not** used anywhere in the 3 proved sub-pieces or the still-open
  Match-Branch Domination sub-claim (which is explicitly scoped narrower, using the specific
  `d=w_1-w_j` structure, not the general `|C|=2` claim).

## No overclaims found

Checked the file's own Status/summary language against every independently-verified finding above:
every "proved"/"CERTIFIED" claim is genuinely proved (re-derived independently by hand for the
algebraic lemmas, confirmed by exhaustive/wide-random computation plus a from-scratch logical retrace
for the reduction and the Two-Touch sub-pieces); every "corroborated, not proved" claim (Two-Touch's
2 open sub-pieces, Gap 1c's nonempty-`\xi^*$ construction, the general Sum Bound induction, general-`q`
Deletion-Suffices-for-`k^*`) is consistently and honestly flagged as open throughout, never silently
treated as closed elsewhere in the file (grep-checked cross-references). The §26 summary sentence
("None of Gaps 1a, 1b (general induction), 1c is fully closed this round — Status correctly stays
`partial`") is accurate.

## Lemma certification decisions

- `lemmas/sum-bound-base-case.md` — **CERTIFIED as submitted.** Sorry-free, statement correctly scoped
  (`rest=\emptyset$, `q=3` only), proof verified independently by hand and by four independent
  computational harnesses across this round alone.
- `lemmas/insertion-difference-identity.md` — **CERTIFIED as submitted.** Fully general, no gap,
  independently re-derived via a self-contained two-lemma composition.
- `lemmas/delete-suffices-insertion-domination.md` — **CERTIFIED as submitted.** Trivial, correct,
  hypothesis confirmed genuinely load-bearing (not vacuous) by an independent negative control.

## Outcome recorded

`record_outcome(problem_id=imo-2026-03, slug=potential-weighting-upper-bound, round_number=16,
outcome=advanced, note="Gap 1b's rest=empty base case fully closed ...; Gap 1a general-q, Gap 1c
nonempty-xi* construction, and Two-Touch's 2 remaining sub-pieces still open — Status stays partial,
no overclaims found.")`

## current.md updated

Added the round-16 entry to `## Approaches tried` (most-recent-first), `## Status` remains `partial`
(no change needed — was already `partial`).

## What remains open (unchanged in substance from the file's own §26.6, independently confirmed accurate)

1. Gap 1b's general recursion-depth induction (`|Z_1|\ge2`) — untouched, large, fully open.
2. Gap 1c's nonempty-`\xi^*` Step-3 nearest-neighbor construction — two routes attempted and stalled
   this round, precisely diagnosed; case-split (generic/duplicate) is the recommended next attempt.
3. Gap 1a's Two-Touch Lemma's 2 remaining sub-pieces (KEEP branch `b_0\le w_1`'s `\sigma=-1` mirror;
   MATCH branch's "Match-Branch Domination" sub-claim) — both strongly corroborated, well-scoped,
   genuinely more tractable than the confirmed-dead general `|C|=2` route.
4. Even a full Two-Touch closure would not by itself close Gap 1a's general-`q` Per-Partner Domination
   induction — a separate per-`q` case analysis on `A_{3,l}`'s own recursion is still needed on top.
5. The `\sigma=-1` mirrors of the Sum Bound and the half-step remain unstarted.
