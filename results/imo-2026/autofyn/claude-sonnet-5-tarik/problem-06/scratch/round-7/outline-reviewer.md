# Round 7 outline-reviewer report — imo-2026-06

## 0. What I read

The full round-7 outliner report (`/tmp/round-7/proof-outliner.md`); all four
touched approach files in full (`persistent-backbone-monovariant.md`,
`forced-primes-well-ordering.md`, `global-recruiter-finiteness.md`,
`core-depth-induction.md`); `current.md`'s round-6 headline and history; all
three round-7 explorer reports in full; the relevant certified lemma files
(`lemma-permanent-inadmissibility.md`,
`lemma-lambda-S-reduction-and-single-companion-finiteness.md`,
`lemma-companion-disjointness-coarsening.md`, and the `.ranking.json`
sidecar).

## 1. Mandatory first check: the cross-explorer tension on Hypothesis (GW)

I did **not** take the outliner's Step 0 framing on faith. I re-implemented
the greedy sequence generator from scratch (fresh Python, exact
`sympy.primefactors`, minimal-antichain-frontier admissibility check for
speed — same algorithmic idea used by prior rounds' simulators but an
independent implementation, not copied from any script in the repo) and
re-derived every load-bearing number myself.

**Simulated `a_1=21528751` to `n=50000`.** Confirmed the already-certified
global-antichain collapse (`~1103→8` around `n=27831–27999`, matching prior
rounds' certified finding to the nearest checkpoint I logged).

**For the depth-2 core `S={103,197}`:**
- `|I_S|=252`, `|J_S|=16` through `n=50000` (matches the multicompanion
  explorer's count exactly).
- `D_S := ⋂_{j∈J_S} rad(a_j) = {2,3,7,1061}`, so `D_S∖P_1={2,3,7}` — matches
  the explorer's and outline's claim exactly.
- The only singleton companion ever realized for this core through `n=50000`
  is `7` (`∈{2,3,7}`, consistent with, not a violation of, the
  Single-Companion Finiteness Lemma's bound `Q_S⊆D_S∖P_1`).
- The bundle `S∪{11,97}` is realized exactly once, at index **863** (matches
  the explorer's report exactly). I searched all 252 elements of `I_S`
  through `n=50000` for any radical that is a **proper subset** of
  `{11,97,103,197}` (i.e. any dominator): **zero found.**
- I then independently re-checked the *proof* (not just the numerics) that
  this bundle is permanent, by reading `lemma-permanent-inadmissibility.md`
  and the Single-Companion Finiteness Lemma's certified statement
  (`Q_S⊆D_S∖P_1`, `lemmas/lemma-lambda-S-reduction-and-single-companion-
  finiteness.md`) directly. The Permanent Pair Lemma's 3-line argument
  (`Q'=∅` excluded by Permanent-Inadmissibility with any `j∈J_S`; `Q'={11}`
  or `{97}` excluded by the contrapositive of Single-Companion Finiteness,
  since `11,97∉D_S∖P_1={2,3,7}`) is **correctly derived from these two
  already-certified facts** — I checked both citations resolve to the
  claimed statements, and the case analysis (`Q'∈{∅,{11},{97}}`, the only
  proper subsets of a 2-element set) is exhaustive. This holds
  unconditionally *given* `J_S` infinite (the same standing, unproved-in-
  general hypothesis every sibling approach already carries — not a new
  weakness introduced here).
- Since `11,97∉{2,3,7}=W(21528751)` (the cross-bucket explorer's claimed
  global recruiter set, itself independently re-derived by me for the
  *singleton* cores `{103}` and `{197}` of this same `a_1` — see below), this
  is a genuine, verified counterexample to Hypothesis (GW) **as literally
  stated** (one global `W(a_1)` working for *every* proper core, nested or
  not).

**Cross-check on the singleton cores (to confirm `W(21528751)={2,3,7}` is
correctly stated for what it *does* cover).** I independently re-derived, from
my own simulation, that the only companions ever recruited by `S={103}` are
within `{2,3,7}` (final antichain `{2,103},{3,103},{7,103}}`, collapse
matching the certified `n≈27832`/"1092→3" finding) and by `S={197}` likewise
(`{2,3,7,197}`, single bundle). So the singleton-core claim is solid; the
counterexample is specifically about *nested* cores, exactly as the outliner
flagged.

**Verdict on Step 0: the tension is REAL. Hypothesis (GW) as literally stated
is FALSE**, not merely in tension. This is not a fatal flaw in the approach —
the file's Step 0 already anticipates exactly this outcome and pre-commits to
pivoting to `(GW-depth)`/`(GW-nested)` rather than to abandoning the
reformulation. A confirmed, cheap refutation of the naive form is real
progress (per `CLAUDE.md`'s "a fast, honest kill is real progress, not
failure"), and it was found *before* any wasted build effort — the process
worked as designed. **I am marking Step 0.1 as already independently
resolved**; the builder should cite this confirmation (and/or redo the check
briefly for the write-up's own self-containedness) and move straight to
Step 0.2 (attempting `(GW-depth)`/`(GW-nested)`), not re-litigate whether the
counterexample is real.

## 2. Independent verification of this round's other new claims

**Escape-Confinement Lemma (`forced-primes-well-ordering`, cited from the
cross-bucket-domination explorer).** Re-derived the proof from Lemma P′
myself (matches the file's 3-line derivation exactly: the nonempty
intersection `rad(a_i)∩rad(a_{j_3})` cannot come from `S` since
`S∩rad(a_{j_3})=∅` follows from `κ∩rad(a_{j_3})=∅` and `S⊆κ`, so it must come
from `comp(a_i)`). I additionally ran my own independent check on
`a_1=247,S={13}`, blocked bucket `{5,7,13}` (blocked by `j_3=7`,
`comp(a_7)={2,3}`): of all **240** escapes (proper supersets of `{5,7,13}`
realized in `I_{\{13\}}` through `n=6000`), **all 240** contain `2` or `3` —
zero exceptions, exactly matching the explorer's claim. The lemma is
correctly derived and numerically confirmed.

**Permanent Pair Lemma (`persistent-backbone-monovariant`).** See §1 above —
independently re-derived and re-verified on both the `a_1=4199,S={17}`
(structurally, via the citation chain) and the `a_1=21528751,S={103,197}`
cases; correct.

**Foreclosure-of-size-induction argument (multicompanion explorer, §3.3).**
This is a genuine structural point, not just a repeated empirical failure:
given a realized 2-element bundle `Q={q_1,q_2}` with both primes outside
`D_S∖P_1`, the *already-proved* Single-Companion Finiteness Lemma itself
(not merely lack of a proof) forbids either `q_1` or `q_2` from ever being a
sole companion — so no `k=2→k=1` reduction can exist for this class of
instances, structurally, not just "not yet found." I agree this is a
qualitatively stronger negative result than `core-depth-induction`'s
Step-3 refutation (which was "a plausible guess turned out empirically
false"), and it correctly forecloses a whole family of future attempts
(companion-count induction, and by the explicitly-flagged analogy,
`T_C`-magnitude or recruitment-count induction should be hand-checked for
the same obstruction before being tried). This reasoning is sound.

## 3. Field diversity / single-gap-trap check

All three live approaches (`persistent-backbone-monovariant`,
`forced-primes-well-ordering`, `global-recruiter-finiteness`) do bear on the
same underlying fact (local FCBC / `𝓥_S`-finiteness), but this round's
orthogonal-mechanism explorer's second exhaustive top-level-technique sweep
(Ramsey/compactness/WQO/analytic-density/crux-corpus, two new candidates
killed this round with quantitative, not hand-wavy, refutations) confirms no
outside technique is waiting to be found. Given that, the three approaches
are genuinely different *routes* to the same target, not restatements of one
line: (a) `persistent-backbone-monovariant` — a companion-**count** bound on
`Λ_S`, now sharpened by a proof of what does *not* work; (b)
`forced-primes-well-ordering` — a **recursion-depth** bound on nested
escape-confinement; (c) `global-recruiter-finiteness` — a **global**
existential reformulation replacing `≤2^k-2` local questions with one. This
matches `CLAUDE.md`'s plateau-break guidance exactly (a global reframing, not
a same-framing bypass) and is not a field collapse. `core-depth-induction`
correctly stays parked (its distinguishing mechanism is doubly dead: refuted
on its own motivating example in round 6, and now reinforced by this round's
independent bundle-size analogue).

No approach in the current build set is doomed by wrong technique,
unjustified leaps, missing cases, or circular reasoning — all three revisions
build only on already-certified facts (Lemma P′, Permanent-Inadmissibility,
Single-Companion Finiteness) with correctly-scoped new targets, and all
honestly flag exactly what remains open rather than overclaiming.

## 4. Ranking actions taken

- Registered `global-recruiter-finiteness` (cold-start Elo 1500) via
  `mcp__approach-ranker__register_approach`.
- Ran `mcp__approach-ranker__update_ranking` with: `persistent-backbone-
  monovariant` vs `forced-primes-well-ordering` (draw — both produced one
  cheap, correct, independently-verified new lemma of comparable value this
  round); both beat `global-recruiter-finiteness` (new, real Step-0 value
  but `unsolved` status and no closed content yet). Resulting Elo:
  `forced-primes-well-ordering` 1620.4, `persistent-backbone-monovariant`
  1588.3, `global-recruiter-finiteness` 1476.8. Both previously-stale
  approaches are now un-staled by this update. `core-depth-induction` and all
  untouched approaches are left as-is (no builder ran on them this round).

## 5. Build set decision

All three touched files pass review: their new lemmas are correctly derived
from already-certified facts (independently re-verified by me, not just
re-read), their next-step targets are well-posed and honestly scoped
(companion-count bound; recursion-depth bound; GW-depth/GW-nested pivot), and
none repeats an already-refuted mechanism. `core-depth-induction` is
correctly left parked (no new work to build on this round). Dispatching one
proof-builder per slug:

- `persistent-backbone-monovariant` — certify the Permanent Pair Lemma in
  full rigor, then attempt the companion-bundle-count bound on `Λ_S` (and,
  if time permits, the permanent-triple generalization).
- `forced-primes-well-ordering` — certify the Escape-Confinement Lemma in
  full rigor, then attempt to bound the escape-confinement recursion's
  depth uniformly (confirmed `≥2` on a concrete instance; connect to the
  Permanent Pair Lemma's counting sub-target per the outline's Step 2(b)).
- `global-recruiter-finiteness` — write up Step 0's refutation formally
  (citing this review's independent confirmation — no need to redo the
  computational check from scratch, though a self-contained restatement for
  the file's own record is fine), then attempt `(GW-depth)`/`(GW-nested)` per
  Steps 0.2/1/2 of the file's own outline. Report honestly if neither
  weakening survives a similarly cheap counterexample search.

build set: persistent-backbone-monovariant, forced-primes-well-ordering, global-recruiter-finiteness
