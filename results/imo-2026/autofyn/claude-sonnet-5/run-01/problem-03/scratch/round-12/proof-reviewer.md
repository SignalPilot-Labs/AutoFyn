# Round 12 proof-reviewer report — `potential-weighting-upper-bound`

**Headline verdict: every claim in §17 (outliner/outline-reviewer skeleton) and §18 (this round's
build) survives independent, from-scratch adversarial re-verification. No error, missing case,
circularity, or overclaim found. Gap 1 (Claim A / "No-Second-Trigger at every depth") is correctly
reported as NOT closed — the theorem remains `partial`, and the round's real, non-overclaimed
progress narrows the sole remaining gap to a precisely-stated existence question on the
non-dominated prefix of each recursion path.**

All verification below uses **fresh Python** (`/tmp/round-12/proof-reviewer-work/mydefs.py` +
seven driver scripts), written directly from the file's own prose definitions in §13.2/§17/§18 —
not copied from or adapted from the builder's, outliner's, or outline-reviewer's harnesses (none of
which I opened). The harness was validated before use against the file's own worked examples
(round-9's `B=\{2,4\},Z=(6,3,2,1)`: got `OPT_{+1}=0`, matching; round-12's `C=\{5,8\},W=(10,8,7,2)`:
got `OPT_{+1}=0,OPT\_KD_{+1}=2`, matching; `c=1,W=(10,8,7)`: got `OPT_{+1}=0,OPT\_KD_{+1}=1`,
matching) and against a brute-force selection-count sanity check (`n=6` gives `499` selections,
matching a hand computation).

## 1. Gap 2 closure (`OPT_KD_σ` DELETE/KEEP trichotomy)

Independently re-implemented the claimed closed form (DEL_KD via recursion, KEEP_KD via the
Rank-Extraction-derived formula) and compared against brute-force `OPT_KD` (full `2^{|W|}` subset
enumeration). **4000/4000 trials (both signs, `|C|\le3`, `|W|\le6`), 0 mismatches.** The proof
itself (every subset either contains `w_1` or not, a free two-way split, unlike the three-way
trichotomy which needs the certified Peeling Lemma's bijection argument) is correct and adds
nothing questionable beyond the already-certified Rank-Extraction Identity it reuses.

## 2. Empty-Background Lemma

Re-derived from Fact 1/Fact 2 exactly as claimed; independently verified `OPT_{+1}(\emptyset,W)=0`
and `OPT_{-1}(\emptyset,W)=\max(W)` (or `0`), and that `OPT=OPT\_KD` at empty background.
**2000/2000 trials, 0 mismatches**, exact values confirmed.

## 3. Background-Splitting Lemma and its Corollary

Re-verified the identity for **both** `OPT` and `OPT\_KD` (**3000/3000 each, 0 mismatches**), and,
crucially, independently checked the **pointwise, selection-by-selection** claim underlying the
Corollary — for every individual selection in the *entire* selection space of every one of the 3000
trials (not just the aggregated optimum), `e(C\cup R) = e(C_{\mathrm{hi}}) + (-1)^h e(C_{\mathrm{lo}}
\cup R)` exactly, **0 mismatches**. This is the fact that lets the affine transform commute with
any restricted-class comparison (in particular the DELETE/KEEP/MATCH trichotomy), so I also
independently re-verified the **Corollary itself directly** (Claim A holds at `(C,W,\sigma)` iff it
holds at `(C_{\mathrm{lo}},W,\sigma\cdot(-1)^h)`) rather than merely trusting the derivation:
**1200/1200 trials, 0 mismatches**.

I additionally proved analytically (and it is consistent with every computational check above)
that **domination, once reached, persists forever along any DELETE/KEEP path** (not just the
all-DELETE path the file's own numeric check used): under DELETE, `C` is unchanged and `\max(W)`
is non-increasing, so a dominating `C` stays dominating; under KEEP, the new `C` is `\{c\in C:c\le
w_1\}`, and if `C` was already fully dominating (`\ge w_1$) this can only consist of copies of
`w_1$ itself, which trivially dominates the new (smaller) `\max(W)`. So the *rigorous* content of
§18.2's "Net effect" claim is airtight and general, not path-dependent.

**One minor precision note (not a correctness error, worth a small edit next round).** The file's
"reaches the dominated regime within a handful of steps (`\le4`, `447` base generators)" is
measured **only along the specific all-DELETE path** — the file itself says so precisely
("the simple all-DELETE path reaches..."), but the surrounding prose in §18.2/§18.6 ("confirmed to
be reached within a handful of steps in every case checked", describing the tail as "a genuinely
small, precisely-bounded prefix") reads more generally than what was actually tested. I ran my own
check of domination-speed along random mixed DELETE/KEEP paths and found no counterexample either
(max `6` steps, distribution concentrated near `0`), but my test instances happened to have both
background elements equal (a mild degeneracy of the random generator, not a designed control), so
this does not itself independently confirm the bound generalizes to every mixed path. This does
**not** affect the rigorously-proved part (dominated `\implies` resolved, persists forever) — only
the informal "how fast" characterization should be scoped explicitly to the tested path in a future
edit.

## 4. New structural fact about `B_0`

Re-derived exactly (`A_1=0` via Empty-Background Lemma when `B_0=\emptyset`; `M\ge0` via Fact 1;
hence `M<A_1$ impossible) and independently re-tested: **3000 fresh random `(B_0=\emptyset,Z_0)`
trigger checks, 0 instances where the empty-background trigger fired** (as required — none should).

## 5. Non-Matching-Witness Criterion reduction

Re-traced both directions of the iff from scratch (no gap found — the trivial branch-value bounds
from the already-certified Generalized Multi-Background Peeling Lemma trichotomy are used exactly
as claimed, correctly handling both the `w_1\in D` and `w_1\in K` cases). Independently verified:
**3000/3000 trials, 0 mismatches** between the criterion's existence check and a direct
brute-force computation of Claim A via the trichotomy.

## 6. FSI does not close Gap 1 (negative finding)

The structural diagnosis is sound and non-hand-wavy: FSI (round 11, `lemmas/forced-swap-inequality.md`)
bounds a *specific* top-level-argmin-relative quantity (comparing sibling match partners `i,j` at
the *same* recursion level as the original `k^*`, against `M`), whereas Claim A is a *generic* node
`(C,W)`'s own MATCH branch vs. its own DELETE/KEEP branches — a different pair of quantities
entirely, correctly identified as not directly comparable. I cannot reproduce the builder's exact
instance counts (`417`/`116`/`28`) since I did not use their generator/seed, but I independently
confirmed the substantive underlying claim — a non-`w_1`-matching optimal witness already exists in
every genuine triggered instance, making FSI's occasional agreement never load-bearing — via my own
fresh `\mathcal F`-family sweep: **2379 genuine nodes** (base generators plus 3 full levels of
DELETE/KEEP closure, both branches at every step, exhaustive not sampled, from 491 independently
generated triggered base instances), **0 Claim-A violations** (equivalently, by the Criterion, a
non-matching witness existed at every one of them).

## 7. Background size-boundedness alone is not sufficient (negative finding)

Independently confirmed with a fresh random generator (different distribution from the builder's):
arbitrary (non-`\mathcal F`-provenance) backgrounds violate Claim A already at `|C|=1` (`134/6000`),
at `|C|\le2` (`221/6000`), and at the smallest list sizes `|W|=2` (`268/6000`) and `|W|=3`
(`292/6000`) — while **dominant** backgrounds (every element `\ge\max(W)`) show **0/6000**
violations in both size classes, exactly matching the file's diagnosis (mechanism, not merely
count, reconfirmed: it is the Background-Splitting/Empty-Background lemmas' *dominance* condition,
not raw size, that explains the safety). Exact violation rates differ from the builder's own (as
expected — different random sampling), but the qualitative finding is identical.

**My own adversarial addition (not requested verbatim but a natural extension of "adversarially
judge"):** I ran a from-scratch hill-climbing perturbation search, seeded at the lowest-margin
nodes found along genuine `\mathcal F`-closure walks, explicitly trying to push
`\mathrm{MATCH}-\sigma\text{-opt}(\mathrm{DEL},\mathrm{KEEP})` negative. Within verified
`\mathcal F$-membership: **0 violations** (matches every other sweep on file). The moment the
search perturbs raw integer values (breaking `\mathcal F`'s provenance chain), it immediately finds
violations (margin as low as `-6`) — and inspecting the resulting instance confirms it is
non-dominant and untraceable to any genuine base-generator derivation, i.e. exactly the "arbitrary,
non-provenance" failure mode of finding 7, not a counterexample to Gap 1 within its actual stated
scope.

## Overall assessment against CLAUDE.md's rigor rules

- **No skipped cases** found in Gap 2, the Empty-Background/Background-Splitting Lemmas, or the
  Non-Matching-Witness Criterion — each is a genuinely exhaustive two-way or logically-airtight
  case split, independently re-traced.
- **No hand-waving**: every "clearly"/"immediate" step I checked (e.g. the trivial branch-value
  bound `\mathrm{DEL}\ge V$, the affine-transform commutation) is either elementary and correctly
  justified, or backed by an already-certified lemma cited by name (Fact 1, Fact 2, Fact 3, the
  General Rank-Extraction Identity, the Generalized Multi-Background Peeling Lemma) — no
  uncited/unjustified leap found.
- **Every theorem named**: yes, each new result correctly cites its dependencies.
- **Proved vs. conjectured kept distinct**: the file is scrupulously honest that Gap 1/Claim A is
  NOT proved — this is stated up front, restated in the "Honest assessment" §18.6, and not
  contradicted anywhere else in §17-§18. No overclaim found.
- **Status `partial` is precisely accurate**: neither undersold (Gap 2, two new general lemmas, one
  new structural fact, and one clean reduction really are fully proved, not merely tested) nor
  oversold (Gap 1, the load-bearing central inequality, is honestly still open, and the one
  overreaching phrase I found — the "handful of steps"/"small prefix" characterization — is a minor
  informal-language imprecision about an already-rigorously-proved fact's illustrative speed
  claim, not a false statement about what has been proved).

## Actions taken this round

- Called `mcp__approach-ranker__record_outcome` for `potential-weighting-upper-bound`, round 12,
  outcome `partial`, with a detailed note (see tool output).
- Updated `results/imo-2026-03/current.md`: added a new round-12 `Approaches tried` entry
  documenting this independent re-verification, added a new certified-lemma bullet
  (`lemmas/empty-background-and-background-splitting.md`, which I created this round — the builder
  proved these facts in §18.2/§18.4 but did not itself extract a separate lemma file, so per the
  file contract's "builder proposes, reviewer certifies" I did so after full independent
  verification), updated item 2 of "What remains open" with the round-12 net effect, and updated
  the closing net-effect summary paragraph.
- Created `results/imo-2026-03/lemmas/empty-background-and-background-splitting.md` (new certified
  lemma file: Empty-Background Lemma, Background-Splitting Lemma + Corollary, Non-Matching-Witness
  Criterion).
- Archived all fresh verification code at `/tmp/round-12/proof-reviewer-work/` (`mydefs.py`,
  `test_gap2.py`, `test_empty_and_splitting.py`, `test_b0_empty_and_criterion.py`,
  `test_size_negative.py`, `test_F_family_claimA.py`, `test_domination_speed.py`,
  `test_adversarial_search.py`).

## Verdict

**CHANGES REQUESTED** for the `potential-weighting-upper-bound` slug — real, independently-verified
progress this round (Gap 2 closed, two new certified general lemmas, one new structural fact, a
clean reduction, two decisive negative findings), but the central Gap 1 inequality remains open, so
the approach is not yet solved and should continue to the next round's builder (attack the
non-dominated-prefix case directly via the Non-Matching-Witness Criterion, using `d_{k^*}`'s
global-argmin-over-all-partners property, not yet used anywhere in §18's reductions, per the
builder's own concrete next-step recommendation, which I independently agree is the right lead).
