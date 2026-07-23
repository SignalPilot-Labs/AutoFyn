# Round 17 proof-reviewer report — imo-2026-03 / `potential-weighting-upper-bound`

## Verdict: CHANGES REQUESTED (Status: partial — confirmed, no overclaim)

The builder's self-reported Status (`partial`) is correct. No fatal flaw found in any of this
round's new claims. Genuine, independently-verified progress on Three-Touch (3 of its 5 structural
pieces, plus the base case), two certified lemmas, and two hand-verified explicit witnesses closing
a previously-flagged verification gap. One rigor/framing overclaim found (not fatal, does not touch
Status) — see item 6 below. `current.md` and the lemma file have been updated accordingly.

## Method

Wrote a fresh, from-scratch harness (`/tmp/round-17/myverify/defs.py`: `e()`, `all_selections()`,
`OPT(sigma,B,Z)`) — not reusing the builder's or explorers' code — and validated it first against
the file's own worked numeric examples (`e({5,3,1})=3`, `e({6,6,2,2,1})=1`, and the OPT_{+1} witness
values from §28.3) before using it for any new claim. Then independently reproduced the builder's
own saved scripts in `/tmp/round-17/verify_builder/` and `/tmp/round-17/gap1c_probe/` and confirmed
every cited count matches exactly.

## 1. The two precision-note fixes — consistency check

**Fix (a), §28.1 (Deletion-Suffices/Sum-Bound quantifier).** Wording-only fix, as claimed. Checked
its main live invocation, §27.1's 3-line DELETE-vs-KEEP algebraic reduction (`KEEP=w1-OPT_{-1}(C,rest)`,
`DELETE=OPT_{+1}(C,rest)` ⇒ Sum-Bound target ⟺ KEEP≥DELETE) — this reduction is genuinely correct and
uses the "chain-threaded" reading consistently. No contradiction found elsewhere in ~15 other
mentions of "Deletion-Suffices-for-k*" grepped across the file.

**Fix (b), §28.2 (ξ* labeling).** The declared canonical reading ("ξ* = AUGMENTED-optimal witness,
i.e. optimal witness of `OPT_{+1}(B1∪{d},X)`, the right-hand/augmented problem") is verified
consistent with every LIVE usage checked (§26.3's `argmin` construction explicitly names
`OPT_{+1}(B1∪{d},X)` right at the point ξ* is introduced — unambiguous in context). Two
historical/dead-end mentions of the old "LHS-optimal" phrase remain un-edited at lines ~5877/5886
(the file explains this is deliberate, per the project's "append, don't rewrite" convention). Read
in context these are not actually mathematically ambiguous (both describe the augmented problem's
witness, matching the new convention), but they lack a forward-pointer to §28.2 — a minor clarity
nit for the next round, not a correctness gap.

## 2. Gap 1c case (b) — both witnesses reproduced bit-for-bit

Independently ran `python3 /tmp/round-17/gap1c_probe/extract_caseb.py` (uses `find_F_instance` from
`probe1.py`, which enforces the TRUE global-argmin trigger `M=min_l A_{3,l} < A1`, not a merely local
one) and separately recomputed both cited witnesses with my own harness:

- `B1={16,15}, Res=(11,10,9,6,3), d=1, X=(9,6,3)`: `OPT_{+1}({16,15,1},(9,6,3))=2`, with 3 optima:
  `∅`, `{3,3}`, `{6,6}` — matches the file exactly.
- `B1={2,2}, Res=(24,23,18,12,6), d=1, X=(18,12,6)`: `OPT_{+1}({2,2,1},(18,12,6))=1`, with exactly 3
  optima: `∅`, `{6,6}`, `{12,12}` — matches the file exactly, and `e({2,2,1,6,6})=1` confirmed via
  Lemma P (duplicate pair `{6,6}` cancels, leaving `e({2,2,1})=1`).

Both witnesses are genuine, non-vacuous, and correctly extracted from real 𝓕-provenance instances.
No sampler-bug regression of either recurring pattern flagged in memory (global-argmin-ness and
implicit `w1=max(W)` are both structurally enforced, not independently sampled, in
`find_F_instance`/`extract_caseb.py`).

## 3. Three-Touch's 4 of 5 pieces (§28.4)

**Base case `|W|≤3` (Lemma B).** Re-derived the "keep-all-three" 4-case domination argument by hand,
symbolically, case by case (including both sub-cases of case 1 and the boundary consistency between
adjacent cases) — matches the file line for line, no gap. Cross-checked with a genuinely **exhaustive**
grid `c,w1,w2,w3∈{0,…,7}` (4096/4096 instances) against direct brute-force `OPT_{-1}({c},W)` — 0
mismatches — plus 8000 random trials over `|W|∈{0,1,2,3}` — 0 mismatches. Reproduced the builder's
own `verify_basecase_proof.py`/`basecase3.py`/`verify_keep_identity.py` outputs exactly
(`0/6000`, `0/956`, `0/3000`, `0/3000`, `0/1854`, `0/3000`).

**DELETE branch.** Elementary candidate-list containment argument (`ThreeTouch(c,W\{u1})≤
ThreeTouch(c,W)` since the smaller candidate list is a literal subset) — correct, verified.

**KEEP `h=1` (c>u1).** `c-u1+u2=e({c,u1,u2})` via Lemma A — re-derived, correct, exact equality (a
literal touch-2 candidate). Uses the already-certified Empty-Background Lemma
(`OPT_{-1}(∅,W')=max(W')`) — independently re-verified this too (0/2000 mismatches, fresh sweep).

**KEEP `h=0` (c≤u1) — the "joint/mutual induction" claim.** Re-derived all three Lemma-A applications
(touch-1, touch-2, touch-3 terms) symbolically — each correct, with equality. **Checked the
well-foundedness/non-circularity claim specifically requested**: traced Two-Touch's own open `b0≤w1`
KEEP sub-case (§26.5(d): needs an upper bound on `OPT_{-1}({b0},rest)`, i.e. exactly Three-Touch's hard
direction, at `rest=W\{w1}`, size `|W|-1`) against Three-Touch's own `h=0` KEEP sub-case (needs
`OPT_{+1}({c},rest')`, i.e. Two-Touch's hard direction, at `rest'=W\{u1}`, size `|W|-1`). **Both
cross-dependencies are at strictly smaller size in both directions — confirmed well-founded, no
circularity.** (This does not mean either mirror is closed at any concrete `q>3`: both still need
their own MATCH branch closed at every intermediate size to get a concrete value — correctly and
honestly disclosed in the file, not overclaimed.)

**All three branches, independently spot-checked at genuine larger sizes** (`|W|∈{4,5,6}`, 1200
trials, using the TRUE recursive `OPT` for the DELETE/KEEP sub-problems, not an unclosed IH): 0
failures of "branch value ≤ ThreeTouch" for DELETE, KEEP-h=1, and KEEP-h=0 simultaneously, plus a
trichotomy sanity check (`max(DELETE,KEEP,MATCH) = true OPT`) holding in every trial — this
cross-validates both my independent harness and the file's §13.2 peeling-trichotomy machinery.
Reproduced the builder's own `threetouch_induction.py` exactly: `KEEP h=0 target failures: 0/2337`,
`MATCH branch failures: 0/4475`.

**MATCH branch.** Correctly reported OPEN — no proof attempted, only corroboration (`0/4475`,
reproduced exactly).

## 4. Refuted MATCH-branch reduction idea — counterexample confirmed

Reproduced `match_idea.py` exactly: the free inequality sanity check (`OPT_{+1}({b0,d},X)≥
OPT_{+1}({b0},X∪{d})`) gives `0/3000` violations (always true, as claimed); the proposed reduction
target `TwoTouch({b0},X∪{d})≥TwoTouch({b0},W)` FAILS `55/3000`, including the literal cited
counterexample: `b0=5, W=(8,10,8), wj=8`: `d=2`, `TwoTouch({5},{8,2})=1 < 3 = TwoTouch({5},{8,10,8})`
— confirmed bit-for-bit with my own independent computation of `TwoTouch`. Correctly ruled dead.

## 5. Lemma file — `max-element-triple-identity-and-threetouch-basecase.md` — CERTIFIED

Both Lemma A (Max-Element Triple Identity) and Lemma B (Three-Touch's base case `|W|≤3`) pass the
full bar: sorry-free (prose), statement correct, proof correct and re-derived independently by hand,
scope note is accurate and non-overclaiming (explicitly states it closes only the base case, not the
general induction). **Certified** — Status line in the lemma file updated to reflect this.

## 6. Overclaim check — "MATCH branch is now a single shared bottleneck across 4 manifestations"

**Found a genuine but non-fatal overclaim.** §28.4's closing language ("this is now confirmed to be
the shared bottleneck for four distinct manifestations") overstates what is actually proved. The
Gap 1a/Gap 1b DELETE-vs-**KEEP** equivalence (§27.1) IS a real, explicit, re-checked 3-line algebraic
reduction — a genuine single lemma whose proof would close both at once. **No analogous explicit
reduction is given for the DELETE-vs-MATCH half.** In particular, Two-Touch's own MATCH branch and
Three-Touch's own MATCH branch are not even provably the same shape of statement: the file's own
§27.2(d) documents a genuine, newly-discovered min/max **asymmetry** (Two-Touch needs touch-depth
≤2, Three-Touch needs touch-depth ≤3, because the maximizer can adversarially exploit Lemma P's
duplicate-pair cancellation, a mechanism with no minimization-side analogue) — so "the same
mechanism" is, at best, a structural/thematic analogy across four separately-defined open problems,
not a proven equivalence that solving one hands you the others. Recommend softening the language
next round ("a recurring open sub-problem of the same flavor," not "confirmed... single shared
bottleneck") unless an explicit reduction (mirroring §27.1's derivation) is actually supplied. This
is a framing/rigor issue in the write-up's summary prose, not a mathematical error — no proved claim
in §28 is false, and it does not affect the correctly-reported `partial` Status.

## Files updated

- `results/imo-2026-03/current.md` — new top `Approaches tried` entry recording this independent
  review (Status stays `partial`; no `Full proof` section, correctly not solved).
- `results/imo-2026-03/lemmas/max-element-triple-identity-and-threetouch-basecase.md` — Status
  updated to CERTIFIED with the reviewer's independent re-verification summary.

## Ranking

`record_outcome` called for `potential-weighting-upper-bound`, round 17, outcome `advanced`, noting
the verified progress and the one framing-overclaim flag for the next round to address.
