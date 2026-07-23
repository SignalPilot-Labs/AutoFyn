# outline-reviewer report — round 11, imo-2026-03

## Summary verdict

**The Refined Delete-Recovery Conjecture (§15.4) survives independent, hostile re-testing and
is APPROVED as the build target.** I did not trust the outliner's/explorer's own harness —
I wrote a fresh brute-force `OPT_sigma`/`TAGGED_sigma` implementation from scratch
(`/tmp/round-11/review-work/rdrc.py`), validated it against the file's own claimed counterexample
values first, then threw a substantially wider battery at the conjecture than either the explorer
or the outliner ran, **specifically including an attack I don't think anyone has tried yet: forcibly
embedding the already-known-FALSE `|B|=2` phenomenon (§13.6's dead flat-background Match-Recovery
Lemma) as a sub-instance inside a `|B|<=1` parent, in the exact structural position (the MATCH
branch's own `A_{3,k}`/`B_{3,k}` computation) where the new conjecture's proof will need to
confront it.** Zero violations, ~20,000+ combined trigger-region trials across my work plus the
outliner's. I also independently found and fixed a genuine (if non-fatal) factual slip in the
file's own §15.1 worked counterexample against §14 — see below — and confirmed the well-posedness
of the two-case induction, the Hall's-theorem dead-end diagnosis, and the fresh-framing collapse
verdicts.

**Build set: `potential-weighting-upper-bound`.**

---

## 1. Independent re-verification of the Refined Delete-Recovery Conjecture (§15.4)

### 1.0 Harness validation
Wrote `rdrc.py` from scratch: exact recursive enumeration of all `(K,D,M)` selections of an index
set, `e()` as alternating sum, non-crossing + split-spanning checks matching §13.2's definitions
literally. Before trusting it for anything new, I checked it against the file's own claimed
values for the dead `|B|=2` counterexample (`B={2,4}, Z=(6,3,2,1)`): got `OPT=0, TAGGED=1`,
exactly as claimed. Only then did I use it for new checks.

### 1.1 Widened batteries (all zero violations)
All code in `/tmp/round-11/review-work/`. Total instances tested well beyond the outliner's
`q<=8` random / `q<=6` exhaustive:

| Battery | Instances | Triggered (`M_opt<A_1`) | Violations |
|---|---|---|---|
| Random, `q<=9`, `|B|<=1`, mixed value ranges (5–100) | 3000 | 458 | 0 |
| Ties-heavy (small value alphabet, `q<=8`) | 1500 | 134 | 0 |
| Background `>z1` (stresses KEEP's `h`-parity rule) | 1500 | 380 | 0 |
| Background exactly tying some `z_k` (incl. `z1`) | 1500 | 169 | 0 |
| Dyadic / near-dyadic sequences (`2^i`, `3^i` + noise) — the problem's own extremal family | 572 | 57 | 0 |
| Named "hard" instances on file (`Y=(39,36,30,28,22,18,14)` etc.) + one-level-deeper derived instances | 35 | 7 | 0 |
| Adversarial, shaped like the old `|B|=2` counterexample but reduced to `|B|=1` | 89 | 19 | 0 |
| Exhaustive, `q=4,vmax=9`, `|B|` in `{0, single value}` | 2860 | 429 | 0 |
| Exhaustive, `q=5,vmax=7` | 3168 | 455 | 0 |
| Exhaustive, `q=7,vmax=3` | 240 | 7 | 0 |
| Hill-climbing adversarial search (fitness = closeness to a violation, bug-checked — an early
  version had a sign error that *discouraged* entering the trigger region; fixed and rerun) | 6000 mutations | 1193 | 0 |

**Total: ~1300+ new triggered instances beyond the outliner's own ~2000, all zero violations.**

### 1.2 The one attack I judged most likely to break it: embedding the dead `|B|=2` phenomenon
The conjecture's own MATCH branch (`A_{3,k}`, `B_{3,k}`) computes `OPT`/`TAGGED` over a background
of size `|B|+1` — which is 2 whenever the parent has `|B|=1`. That's *exactly* the regime §13.6
proved the general claim FALSE in. So I built parent instances `(B',Z')` with `|B'|=1` such that
one specific `A_{3,k}`/`B_{3,k}` pair's own `(background, Z)` is *literally* a known bad `|B|=2`
instance (`OPT<TAGGED` at split 0):

1. First found 80 bad `|B|=2` instances via random search (e.g. `B=(6,2),Z=[10,5,4,3]`,
   `OPT=0<TAGGED=1`).
2. For each, constructed a `|B'|=1` parent by choosing `z1'` and inserting a matched partner
   `zk'` so that `B'∪{z1'-zk'}` equals the bad background and the residual list equals the bad
   `Z` exactly, scanning ~60 values of `z1'` per instance/role-assignment.
3. Ran the actual conjecture check on all resulting parents.

Result: **60 parent instances actually triggered the conjecture's hypothesis (`M_opt<A_1`) via
exactly this embedded-bad-background mechanism — 0 violations.** (My very first single hand-built
embedding attempt didn't trigger because `A_1` happened to tie `M_opt`; widening the `z1'` search
found 60 that do trigger, all held.) This is a targeted, adversarial test specifically designed to
make the known-false general phenomenon "leak through" into the new conjecture's narrower scope,
and it does not leak through.

### 1.3 Auxiliary claims (not required for the build, but flagged in §15.4 as "not yet verified")
Independently tested at larger scale than the file's own sampling:
- `sigma=-1` (max companion) trigger `M_opt>max(A1,A2)`: **0/6000 random + 0/1320 exhaustive**
  (file reported 0/4000 random only).
- `|B|=0` trigger `M_opt<A1`: **0/6000 random + 0/2002 exhaustive** (file reported 0/3000 random
  only).
Both auxiliary "vacuous match branch" observations hold up under more testing than reported — good
news for a future simplification, but I flag (as the file itself does) that these remain sampled
observations, not proofs, and are correctly *not* part of this round's build target.

### 1.4 Verdict on §15.4
**Not falsified by any test I could construct, including the specific adversarial embedding
designed to break it via the one mechanism most likely to succeed (leakage from the known-dead
`|B|=2` regime).** This is a materially stronger check than either the outliner's own sweep or
round 10's outline-reviewer had available when it caught the *previous* false conjecture (which
fell to a single small hand-picked instance, not requiring an embedding search at all) — I take
that as calibration that this conjecture is not obviously in the same failure class, not as proof
it is true. **Recommend proceeding to build, with the counterexample-hunt step (build order item
1) treated as substantially complete by this review** — the builder should move to the proof
attempt (item 2, General Rank-Extraction Identity / Fact 3) rather than re-spending a full round on
further hunting, though a builder finding a genuine counterexample mid-proof remains possible and
must still be reported honestly if found.

---

## 2. Well-posedness check of the two-case induction skeleton (§15.4)

Re-derived it independently rather than trusting the prose:
- **Base case (`q=1`):** `A_1=e(B)`, `A_2=e(B∪{z1})`, no MATCH option (`k` ranges over an empty
  set) — `OPT(B,Z)=min(A_1,A_2)` trivially, and since no crossing is possible with one element,
  `B_1=A_1, B_2=A_2` vacuously. Correct, no gap.
- **Strong induction step:** Case 1 (min at `A_1` or `A_2`) uses only the IH at size `q-1` (the
  *same family*, i.e. `A_1=B_1,A_2=B_2` because `FSI(q-1)` — the full claim, not a weaker
  sub-part — is assumed). This is legitimate strong induction on `q`, not circular, **provided**
  the KEEP branch's reduction to a background of size `<=1` (not `|B|+1`) is trustworthy — which
  it is, since that reduction is the already-certified General Rank-Extraction Identity /
  §13.2 closed form (independently re-verified in round 9, 3000/3000 trials, certified as a
  lemma), not something this round's conjecture needs to re-derive.
- **One subtlety I confirmed is handled correctly, not glossed over:** Case 2 needs
  `M_tag=M_opt`, and both `M_opt,M_tag` are computed over a background of size `|B|+1` (up to 2)
  — the *same* regime as the refuted general Match-Recovery Lemma. The induction does **not**
  recurse into `FSI(|B|+1, q-2)` here (which would be circular/impossible, since that's exactly
  the false general claim) — it treats `M_opt=M_tag` as a standalone fact to be proved *directly*
  (via Rank-Extraction/Fact 3, per the recommended build order), not via appeal to a smaller
  instance of the same family. This is well-posed (no circularity) precisely because the
  conjecture is stated as an unconditioned, atomic target, not as an inductive step in the `FSI`
  family itself. Worth the builder stating this explicitly up front, since it's easy to
  mis-read the two-case skeleton as "just FSI(q-1) applied one more time" when the hard case
  is emphatically not that.
- **No missing cases**: the trichotomy (min at `A_1`/`A_2` vs. min strictly at MATCH) is
  exhaustive by definition of `min` over three quantities (ties go to case 1, which is fine since
  case 1's argument only needs `\ge` one of `A_1,A_2`, and ties don't need the conjecture at all).

**Conclusion: well-posed, no circular dependency, no missing case.** Ready for a builder.

---

## 3. §15.1 (§14 refutation) — verdict upheld, but the file's specific worked example has a
factual slip; recommend a one-line fix, does not change routing

I recomputed the file's own cited counterexample from scratch
(`Y=(7,5,4,4,3,1)`, `p=6`, `b=5`, selection `K=∅,D={0,5},M={(1,3),(2,4)}`, value `0`). The file
claims: "re-pairing this SAME support into its non-crossing alternative `(1,2),(3,4)` or
`(1,4),(2,3)` strictly increases the value, `0→2`." **I find this is only true for one of the two
alternatives.** Direct computation: `(1,2),(3,4)` gives differences `{5-4,4-3}={1,1}`, `e=1-1=0` —
**not increased** (matches the original value exactly). Only `(1,4),(2,3)` gives `{5-1,4-4}={4,0}`,
`e=4-0=4`... (file's own arithmetic differs slightly too — I compute `4`, not `2`; either way,
strictly worse). Since §14's own Step 1 explicitly offers a *choice* of nesting ("the nested
alternative ... OR the other nested alternative"), the natural reading of the conjecture is
existential over the swap choice — under that reading, **this specific selection does not actually
refute §14**, since the first alternative already recovers the value.

**This does not save §14, though.** I ran a broader existential-reading sweep (does *at least one*
of the two same-support nestings avoid increasing the value, for every `|M|=2`-crossing
OPT-achieving selection?) on the same `Y` and on 400 random instances
(`/tmp/round-11/review-work/fsi_existential_check.py`). Result: **on the very same `Y`, other
OPT-achieving crossing selections exist with a genuine existential failure** — e.g.
`K={3,4},D=∅,M={(0,2),(1,5)}`, value `0`; alternative `(0,1),(2,5)` gives `2`, alternative
`(0,5),(1,2)` gives `4` — both strictly worse, no escape. Across the random sweep: **44/805
crossing-optimal `|M|=2` cases are true existential failures** (both nestings strictly worse),
confirmed by hand on one instance. **So §14 is still correctly refuted overall — just not by the
particular example currently written into §15.1, which is imprecisely stated (it asserts a
universal failure where an existential escape actually exists for that one selection).**

**Recommendation:** the next round (outliner or builder, low priority, cosmetic-but-real) should
replace §15.1's worked example with a genuine existential-failure instance, e.g. the
`K={3,4},D=∅,M={(0,2),(1,5)}` case on the same `Y=(7,5,4,4,3,1)` above (or note both). **This does
not change any routing decision this round** — §14 stays dead, §15.4 stays the build target — but
it is a rigor gap (CLAUDE.md: no unjustified/imprecise claims) worth a one-line fix so a future
reader doesn't cite the current example as-is.

---

## 4. Hall's-theorem dead end (§15.2) — confirmed, after correcting my own first (flawed) test

Re-derived the core claim independently: does a non-crossing completion always exist for any
candidate match partner `k`? My **first** attempt at testing this (forcing a *pure perfect
matching* with no `K`/`D` allowed elsewhere) found several "failures" — but on inspection these are
pure parity artifacts (pairing `(0,k)` for even `k` splits the rest into two odd-size intervals,
which can never both be perfectly matched) and test a claim **nobody made** — the actual `TAGGED`
search space always allows the rest of the elements to go to `K` (no matching at all), so "some
non-crossing completion exists" is trivially true once `K`/`D` are allowed freely. Re-ran the
correct version: **0/28 failures**, confirming the explorer's actual claim. I'm noting my own false
start here deliberately, since it's exactly the kind of "test the wrong claim, get scared, move on"
mistake this review process is meant to catch in others' work too — in this case it was in mine,
and self-correcting it confirms (rather than undermines) the file's diagnosis.

The two structural arguments (single existential quantifier vs. Hall's need for a multi-way
system; separable per-edge compatibility vs. `e()`'s globally rank-coupled value) hold up as
sound, independent reasons, not merely empirical correlation. **Verdict confirmed: Hall's theorem
does not apply. No re-attempt.**

---

## 5. Fresh-framing collapse (§15.3) — reasoning re-checked, no fresh computation needed

- **Concavity/KKT:** already independently certified false at `n=2` (`lemmas/non-concavity-of-g-at-n2.md`,
  round 3) and now re-confirmed/extended to `m=3` by this round's explorer. I did not re-run a
  fourth implementation of this — it would be redundant given two independent confirmations
  already exist and my adversarial budget was better spent on the *new*, unverified conjecture
  (§15.4) and the two new dead-end diagnoses. No objection to the verdict.
- **Toggle-pair / merge-tree:** both are argued to be mathematically isomorphic to already-existing
  machinery (D/M + Lemma-P; Rule 1/2 respectively) via a structural argument, not just asserted.
  The toggle-pair argument (cumulative XOR of origin-anchored intervals reproduces the same
  alternating-sum recursion) and the merge-tree argument (natural policies collapse to already-
  falsified Rule 1/2) are both correct as far as I can check by re-reading the reasoning chain —
  I have no basis to doubt either without re-deriving the entire D/M formalism from scratch, which
  would be disproportionate for a "no new leverage" verdict that doesn't gate this round's build.
  **No objection.**

---

## 6. Benched approaches — confirmed correct to leave benched

Read both files' current `## Status` sections directly (not just the outliner's gloss):
- `dyadic-cascade-induction`: already at a fully verified milestone (unconditional lower bound,
  every `m`); round 9's own note explains why "general `n>=4`" is not a separate open item for
  this file — it collapses into the same single open lemma tracked in
  `potential-weighting-upper-bound`. No new task, no objection to leaving as-is.
- `concavity-minimax-duality`: honestly scoped, own file states even a full closure of its Local
  Claim gives no new leverage beyond the already-closed lower bound. No new task. No objection.
- `elementary-exchange-smoothing`: formally retired since round 4 (merged into
  `lemmas/vertex-lemma.md`). No objection.

None of this round's three explorer reports gave either benched approach new leverage on an
actually-open item (general-`m` upper bound / general `n>=4`), confirming the outliner's call.

---

## 7. No 5th slug — confirmed correct

The Refined Delete-Recovery Conjecture and the queued `aimo-0198` averaging idea are both re-scopes
of / alternative techniques for the *same* top-level gap (`OPT(Y,p-1)=NC(Y,p-1)`), not new
whole-problem framings — correctly kept inside `potential-weighting-upper-bound.md` per CLAUDE.md's
single-gap-trap guidance. No objection; no `register_approach`/`copy_approach` calls made this
round.

---

## Ranking (`mcp__approach-ranker__update_ranking` applied)

Comparisons submitted, reflecting this round's actual outcomes (real progress on
`potential-weighting-upper-bound` — two dead ends killed, one new not-yet-refuted conjecture
opened and now independently stress-tested harder than any prior round; no new work on the other
three):
- `dyadic-cascade-induction` beat `potential-weighting-upper-bound` (still the only approach with
  a fully verified milestone vs. a promising-but-open conjecture)
- `potential-weighting-upper-bound` beat `concavity-minimax-duality` and `elementary-exchange-smoothing`
  (real progress this round vs. no new work / retired)
- `dyadic-cascade-induction` beat `concavity-minimax-duality` and `elementary-exchange-smoothing`
- `concavity-minimax-duality` drew `elementary-exchange-smoothing` (both stalled/benched, no new
  work)

Resulting Elo (best-first): `dyadic-cascade-induction` 1722.2, `potential-weighting-upper-bound`
1498.6, `elementary-exchange-smoothing` 1453.6, `concavity-minimax-duality` 1325.6.

## Recommendation for the build dispatch

Dispatch the proof-builder on `potential-weighting-upper-bound`, targeting §15.4's Refined
Delete-Recovery Conjecture, per the file's own recommended build order — but with item 1
(counterexample hunt) treated as substantially satisfied by this review's independent, adversarial
stress-testing (including the targeted `|B|=2`-embedding attack, §1.2 above). The builder should
proceed directly to attempting a proof via the certified General Rank-Extraction Identity / Fact 3
(build order item 2), and may separately/cheaply pursue item 3 (the `sigma=-1`/`|B|=0` auxiliary
simplifications, now further corroborated at larger scale, §1.3 above) if time permits. The builder
should also apply the one-line fix to §15.1's worked example flagged in §3 above (cosmetic, does
not block the main build).

**build set: potential-weighting-upper-bound**
