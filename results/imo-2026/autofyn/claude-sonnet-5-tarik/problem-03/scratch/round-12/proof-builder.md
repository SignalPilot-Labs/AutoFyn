# Round 12 proof-builder report — `potential-weighting-upper-bound`

**Headline (honest, per CLAUDE.md): Gap 1 (Claim A / "No-Second-Trigger at every depth" — the sole
remaining gap toward Sharp Argmin Recovery and hence the whole upper bound) is NOT closed this
round.** Real, checked, non-overclaimed progress was made and written into
`results/imo-2026-03/approaches/potential-weighting-upper-bound.md` §18 (new). Status stays
`partial`.

## What was proved in full (new §18.1–§18.4)

1. **Gap 2 closed in full** (§18.1): `OPT_KD_σ` obeys the identical DELETE/KEEP-only trichotomy,
   with the identical General-Rank-Extraction-Identity-derived KEEP closed form, as `OPT_σ`
   restricted to no matching. A real proof (case split on subset membership), not an assertion;
   cross-checked against brute force, 4000/4000 exact-integer checks, 0 mismatches.
2. **Two new general-purpose lemmas** (§18.2), both proved from already-certified facts (Fact 1,
   Fact 2 `lemmas/dominant-extraction.md`; Fact 3 `lemmas/insertion-and-cascade-facts.md`) and
   independently cross-checked computationally (0/8000+ mismatches combined):
   - **Empty-Background Lemma**: `OPT_σ(∅,W) = OPT_KD_σ(∅,W)` for every `σ,W` — explicit values
     `0` (σ=+1) / `max(W)` (σ=-1).
   - **Background-Splitting Lemma**: for *any* `C,W,σ`, splitting `C` into the part dominating
     `max(W)` and the rest gives an exact affine reduction of `OPT_σ(C,W)` (and `OPT_KD_σ`
     identically) to the same problem with the smaller "non-dominating" background. **Corollary**:
     Claim A holds unconditionally on the "eventually dominant" tail of every DELETE/KEEP path in
     the scope family `F` (confirmed to be reached within ≤4 steps in every one of 447 genuine
     base-generator paths sampled) — narrowing Gap 1's open content to a bounded prefix of each
     recursion path.
3. **New structural fact** (§18.3): the base generator's trigger condition can *only* fire when
   `|B_0|=1` exactly — `B_0=∅` always forces `A_1=0≤M`, making the trigger `M<A_1` impossible.
   Confirmed computationally (0/617 genuine triggered instances had `B_0=∅`).
4. **Non-Matching-Witness Criterion** (§18.4): a clean, fully general iff — Claim A holds at a node
   iff `OPT_σ(C,W)` has *some* optimal witness that does not match `max(W)`. Reduces Gap 1's entire
   remaining content to one crisp existence question.

## Decisive negative findings

- **FSI does not close Gap 1** (§18.4) — the outline's own explicitly-flagged open question,
  answered negatively with the actual mechanism traced through, and re-checked computationally after
  an earlier draft's guessed numbers were caught as unverified and replaced with real ones
  (`fsi_adapt_check.py`: 417 genuine instances, 116 FSI-applicable crossing cases, only 28
  coincidental value-matches — and a separate, decisive check (`check_nonmatching_exists.py`) shows
  a non-matching witness *already* exists in all 417/417 cases regardless, so FSI's occasional
  numerical agreement is never load-bearing).
- **Size-boundedness of the background is not, by itself, doing the real work** (§18.5): arbitrary
  (non-`F`-provenance) backgrounds of size ≤1 or ≤2 already violate Claim A/MFR at scale (6523/40000
  and 4416/40000 violations respectively), including at the smallest list sizes `|W|=2,3`
  (2608/40000, 6386/40000) — correcting the outline's implicit expectation that small `|W|` would be
  an easy base case. Genuine trigger+argmin provenance, not size, is doing essentially all the work.

## What remains open

Exactly: for `(C,W,σ)∈F` with the background not yet dominated by `max(W)`, prove `OPT_σ(C,W)`
always has a non-`max(W)`-matching optimal witness. Corroborated by every test on file
(this round's fresh 35,566-node independent sweep plus 417 forced-matching checks, all 0
violations/0 forced cases; the outline-reviewer's own ~200,000+), but no proof mechanism tried so
far (domination, FSI-adaptation, direct construction) closes it. Concrete next step recorded in the
file: attack existence of the non-matching witness directly, using that `d_{k*}`'s *global-argmin*
property (over all partners, not just `k*`) has not yet been used anywhere in §18's reductions.

## Where to look

- `results/imo-2026-03/approaches/potential-weighting-upper-bound.md` §18 (new, ~230 lines) —
  Status header also updated with a round-12 builder note.
- Code archived at `/tmp/round-12/work/`: `defs.py`, `gen_F.py` (fresh generator/harness),
  `verify_gap2.py`, `verify_writeup_claims.py`, `test_general_mfr.py`, `test_size2_mfr.py`,
  `test_size1.py`, `test_small_W.py`, `test_dominant.py`, `check_b0_empty.py`,
  `check_nonmatching_exists.py`, `fsi_adapt_check.py`, `investigate.py`, `investigate2.py`.
