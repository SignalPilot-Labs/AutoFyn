# Round 18 proof-review: `potential-weighting-upper-bound` (imo-2026-03)

## Verdict: CHANGES REQUESTED (Status: partial)

The builder's headline claim — "§30.1: CLOSED, a complete rigorous proof… Two-Touch fully proved for
`|W|<=3` unconditionally" — is **an overclaim**. I found a genuine, previously-uncaught gap inside the
§30.1 Corollary. The core 3-line Lemma (Match-Branch-Domination-via-Per-Partner-Domination) is sound
and is real progress; the "Two-Touch fully proved for `|W|<=3`" *consequence* bundled with it is **not**
actually established by the proof given. §30.2 and §30.3 are honestly reported as open — no issue found
there, and the builder's own claim to have caught itself pre-empting fabricated numbers checks out: every
number I re-ran reproduces (several exactly, several within expected random-reseed variance).

---

## 1. §30.1 — independent re-derivation of the 3-line proof, and the Corollary's gap

**The core Lemma is correct.** Restated: for a Two-Touch peeling instance `({b0},W)`, `w1=max(W)`,
`MATCH_j := OPT_{+1}({b0,d_j}, rest\{w_j})`, `TT := TwoTouch({b0},W)`:
```
MATCH_j = A_{3,j} >= min(A1, D_j) >= TT
```
conditional only on Per-Partner Domination (F3, certified `q<=3`) at index `l=j`. I independently
re-checked every ingredient:
- **F1 (`A1 >= TT`)**: re-derived by hand — candidate-set inclusion (`TwoTouch(C,rest)`'s candidate list
  is a strict subset of `TwoTouch(C,W)`'s) is elementary and correct, and is genuinely the *inductive
  step* invoked with the IH at `|W|-1`, not a free-standing fact. At `|W|=3` the IH is invoked at
  `|W|-1=2`, the already-certified base case (§26.5(a)) — **not circular**, confirmed by tracing the
  actual induction level used.
- **F2 (`D_j >= TT`)**: trivial, `D_j` is literally a member of `TT`'s own candidate list. Correct.
- **F3 (Per-Partner Domination, `q<=3`)**: re-read §21.3/§22.2's exact statement — genuinely "no trigger
  hypothesis, no argmin requirement," matches how §30.1 invokes it. The `q=2,3` proofs (§22.2) were
  already reviewer-certified in round 14; re-spot-checked, still sound.
- The 3-line combination (`min` of two quantities each `>=TT` is `>=TT`) is elementary and correct.

**So `MATCH_j >= TT` is genuinely proved, conditional on F3 at the relevant `q`.** This is real progress
— the builder's own "precision correction" about F1 being merely the induction's *inductive step* (not a
free-standing fact), and the requirement to verify a well-founded joint-induction level-ordering before
invoking this at general `q`, is **accurate and appropriately cautious** — I traced it myself and agree
it does not (yet) license invoking the Lemma at `q>=4` without first closing Two-Touch/Three-Touch at
every smaller level. No issue there.

**The Corollary has a real gap.** The Corollary ("all three branches of the `|W|=3` trichotomy are
unconditionally `>=TT`, hence Two-Touch fully proved for `|W|<=3`") requires, in addition to F1-based
DELETE and F3-based MATCH, that the **KEEP branch's `b0<=w1` sub-case also satisfies `A2 >= TT`**. The
file's argument for this (lines ~7166-7170) is:

> "the `b0<=w1` sub-case at `|W|=3` needs Three-Touch at size `|W|-1=2`, which Lemma B … already proves
> unconditionally, `|W|<=3` being comfortably within its scope"

**This is a non sequitur.** Lemma B (certified, `lemmas/max-element-triple-identity-and-threetouch-
basecase.md`) proves the *value* `OPT_{-1}({c},W') = ThreeTouch(c,W')` for `|W'|<=3` — a closed form for
a `sigma=-1` (maximization) sub-problem. It says nothing about the actual quantity the Corollary needs:
```
w1 - ThreeTouch(b0, rest) >= TwoTouch({b0}, W)          (rest = W\{w1}, |rest|=2, b0<=w1)
```
This is a **different, unproven inequality** — comparing a `sigma=+1` peeling instance's KEEP branch
against `TT`. The file's own §27.2(d) (round 17) explicitly logged this exact inequality as
**"corroborated `0/1,239`, not proved"** ("This is genuinely new content the file did not have — not
proved, but no longer 'not even formulated.'"). §30.1's Corollary silently treats this as if it had been
proved by Lemma B, which it was not. §29.1 (this round's own outline, written before the build) contains
the identical conflation, so this is not a one-off wording slip — it is baked into both the plan and the
executed proof, and into the "Promotable lemmas" submission itself (the submitted Lemma's *statement*
literally includes "Consequently, at `|W|<=3`, Two-Touch … is unconditionally, fully proved").

**Independent verification of the underlying claim (to check severity — is it even true?).** I wrote a
fresh harness (`/tmp/check_gap.py`, `/tmp/check_gap2.py`, `/tmp/check_gap3.py`) implementing `e()`,
`ThreeTouch`, `TwoTouch`, and a brute-force `OPT_sigma` (full DELETE/KEEP/MATCH-pair partition
enumeration, not either closed form), and tested `w1 - ThreeTouch(b0,rest) >= TwoTouch({b0},W)` for
`b0<=w1`, `rest={u1,u2}`, `W={w1,u1,u2}`:
- `0/3000` random half-integer trials (`vmax<=10`)
- `0/4000` random trials against the **true brute-force `OPT`** on both sides (not the closed forms),
  `vmax<=40`
- `0/1155` fully exhaustive half-integer grid (`vmax=4`, step `1/2`)
- `0/6000` wide-value-range trials (`vmax` up to `500`, per the round-13/24 lesson about widening past a
  builder's own tested range before trusting a margin claim)
- also checked, and found `0/3000` failures for, the *termwise* sufficient condition (every one of
  ThreeTouch's 5 candidates `a'` satisfies `w1-a' >= TT`), which is stronger than needed and would give a
  short Lemma-A-style proof if it can be shown in general — not attempted by the builder.

**The underlying claim appears true** (strong corroboration, no counterexample found by me either), but
**it is not proved in the file** — the file cites an unrelated already-certified fact (Lemma B) as if it
discharged this obligation. This is exactly the "no explicit reduction proof for each claimed link"
failure mode flagged in `run_state.md` Rule 30 (round 17), recurring in a different guise this round.

**Consequence for certification.** I am **certifying only the core Lemma** — `MATCH_j >= min(A1,D_j) >=
TT`, conditional on F3 at the relevant `q` — and **rejecting the "Consequently, Two-Touch fully proved
for `|W|<=3`" clause** as submitted; it is not established by the given proof. The "Two-Touch fully
proved for `|W|<=3`" headline claim in the file's Status block and §30.4 net-verdict is **not correct as
stated** and must be walked back to "MATCH branch closed for `|W|<=3`; the KEEP `b0<=w1` sub-case at
`|W|=3` remains an open (strongly corroborated) inequality, not yet derived from Lemma B or anything
else on file."

## 2. §30.2 — spot-check of refuted candidates and no-overclaim check

Re-ran `t4_union.py` (union-of-three-candidates bound): got `3462/40000` vs cited `3518/40000` — same
order of magnitude (~8.7% vs ~8.8%), unseeded random trial, consistent with a genuine reproducible
phenomenon, not a fabricated number. Re-ran `t5_general_B.py` (general-background-size induction): got
`76/3188` vs cited `64/3217` — again close, same conclusion (general `|B|>=2` fails). Re-ran
`t7_match2.py` (second-largest-partner shortcut): got `3445/7931` vs cited `3458/8005` — matches almost
exactly. All three negative results hold up under independent re-execution; I did not find grounds to
believe any of the three "refuted" routes are secretly salvageable from the numbers shown. The target
itself (`MATCH_val <= max(DELETE_val,KEEP_val)`) remains reported open, with no attempted or implied
closure — correctly not overclaimed as solved. I did not find a proof route the builder missed; my own
brief attempt to find a short argument (e.g., testing whether the KEEP-side witness can always absorb the
MATCH witness's slack) did not turn up anything beyond what's already logged as refuted.

## 3. §30.3 — h_d-even claim and the two refuted δ_c bounds

Re-ran `t_final.py`/`t_final2.py`/`t_final3.py` (the 949-instance combined case-(a) sweep): **every
number reproduces exactly** — `530+201+218=949` total instances, `delta_d<0`: `0/949` (exact match),
`h_d` even: `949/949` (exact match, zero odd occurrences), `delta_c<0`: `497+182+197=876/949` (exact
match to cited "876/949 ≈ 92.3%"), bound (i) `|delta_c|<=|c-d|` failures: `137+148=285/419` (exact match
to cited "285/419 ≈ 68%"), bound (ii) `|delta_c|<=2|c-d|` failures: `96+110=206/419` (exact match to
cited "206/419 ≈ 49%"). Also re-ran `t_gap1c_free.py` (the provenance-free `delta_d` counterexample
sweep): **exact match**, `148/944`. These are fixed-seed scripts and reproduce bit-for-bit — strong
evidence the builder actually ran real code rather than writing plausible-sounding numbers. `h_d` always
even (949/949, no counterexample) is a genuine new empirical finding, correctly reported as
"corroborated, not proved — no argument was found this round for why `h_d` must be even." Both δ_c bound
refutations are real (I reproduced the exact fail counts) and the "no proof found, `δ_c` remains fully
open" self-assessment is accurate — no overclaim in §30.3.

## 4. `/tmp/round-18-build/` scripts — existence and reproduction check

All 16 scripts listed in the file's preamble exist at `/tmp/round-18-build/` with timestamps consistent
with this round's build window. I executed 9 of them directly (`t4_union.py`, `t5_general_B.py`,
`t7_match2.py`, `t_gap1c_free.py`, `t_verify_301.py`, `t_verify_F3.py`, `t9_wide_sweep.py`, `t_final.py`,
`t_final2.py`, `t_final3.py`) — every cited number either reproduced **exactly** (fixed-seed scripts:
`t_gap1c_free.py` 148/944, `t_verify_301.py` 0/400+0/625, `t_verify_F3.py` 0/1837+0/9375, all three
`t_final*.py` numbers) or reproduced within expected random-reseed variance, same order of magnitude,
same conclusion (unseeded scripts: `t4_union.py`, `t5_general_B.py`, `t7_match2.py`, `t9_wide_sweep.py`).
**No fabricated or non-reproducing number was found anywhere in §30.** The builder's claim to have caught
itself before writing plausible-but-unverified numbers, and to have actually run the scripts, is
substantiated.

## 5. Overall Status determination

`potential-weighting-upper-bound` Status: **partial** (unchanged — the whole theorem remains far from
solved: Gap 1a general-`q`, Gap 1b general induction, Gap 1c case (a), Three-Touch's MATCH branch, and
now also the corrected KEEP `b0<=w1` sub-case at `|W|=3` are all open). This round's real, net progress:
- **Genuine new result**: Two-Touch's MATCH branch, at every size, reduces exactly to Per-Partner
  Domination at that size (no longer independent open content) — a real simplification of the theorem's
  dependency graph, correctly retiring "Match-Branch Domination" as a separate line item.
- **Overclaim caught and must be corrected**: "Two-Touch fully, unconditionally proved for `|W|<=3`" is
  false as argued — the KEEP `b0<=w1` sub-case at `|W|=3` needs the inequality `w1-ThreeTouch(b0,rest) >=
  TwoTouch({b0},W)` (`|rest|=2`), which is only numerically corroborated (I independently re-confirmed
  `0` failures across `>14,000` combined trials of my own), not proved — Lemma B does not supply it.
- §30.2 (Three-Touch MATCH Sibling-Domination) and §30.3 (Gap 1c case (a)) are correctly, honestly
  reported as open with real negative-result narrowing — no issues found.

**Action for next round:** either (a) prove `w1 - ThreeTouch(b0,{u1,u2}) >= TwoTouch({b0},{w1,u1,u2})`
directly (my termwise sufficient-condition check, `0/3000`, suggests a Lemma-A-style case split on the
rank of `b0`/`u1`/`u2` — mirroring §28.4(d)'s technique but for a `min` instead of a `max` — is a
promising concrete next attempt, not yet tried), or (b) find a genuinely different argument for the
`|W|=3` base case that bypasses Three-Touch's KEEP `h=0` branch (e.g. a direct "Four-Bound"-style
domination lemma proved from scratch for the `|W|=3, b0<=w1` configuration, analogous to how the
`|W|=2` base case used Three-Bound Domination directly rather than through a recursive KEEP-branch
formula).

## Lemma certification decisions

- **Match-Branch-Domination-via-Per-Partner-Domination — CERTIFIED, but narrowed.** I certify only:
  `MATCH_j >= min(A1,D_j) >= TT`, conditional on Per-Partner Domination (F3) at the relevant `q`
  (unconditional for `q<=3`). I explicitly **reject** the submitted statement's "Consequently, at
  `|W|<=3`, Two-Touch … is unconditionally, fully proved" clause — not established, see §1 above. Filed
  the narrowed version to `lemmas/match-branch-domination-via-per-partner-domination.md`.
- **Lemma A / Lemma B** — already certified round 17, unaffected (Lemma B's own statement, about
  `OPT_{-1}({c},W)` alone, is correct and unaffected by the gap found above — the gap is in how §30.1
  *uses* Lemma B, not in Lemma B itself).
- No new lemma proposed in §30.2/§30.3 (correctly, since nothing there is closed).

## `current.md` update

Updated `## Status` (unchanged, `partial`) and prepended a new `Approaches tried` entry for
`potential-weighting-upper-bound` round 18 recording: the core MATCH-branch reduction as genuine new
certified content, the caught-and-corrected "Two-Touch fully proved for `|W|<=3`" overclaim (with the
precise missing inequality named), and the honest-open status of §30.2/§30.3 with their reproduced
numbers. No `## Full proof` section added (Status is not `solved`).
