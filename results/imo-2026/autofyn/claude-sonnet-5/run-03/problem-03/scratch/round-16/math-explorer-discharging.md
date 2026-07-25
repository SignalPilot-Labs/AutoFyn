## imo-2026-03 (lens: discharging-neighbor-transfer relabeling scout)

- **Distinct openings:**
  1. **Direct relabel-and-halve fix** (the one dispatched): keep the Single-Cut
     Rank-Shift Identity's algebra untouched, rename its quantity `AltSum`
     (it already is, by construction — every term is `σ_i m_i`,
     `σ_i=(-1)^{i+1}`, which is literally the definition of AltSum in the
     certified Lemma AS), and separately state the true-OddSum corollary
     `ΔOddSum = ΔAltSum/2` (mass-conservation argument, since `v1+v2=m_j`
     exactly, `Δ(sum)=0` for every single split, so Lemma AS's
     `OddSum=(sum+AltSum)/2` gives the halving exactly, no approximation).
  2. **Work in AltSum coordinates throughout, never translate to OddSum.**
     Since the whole game has fixed total mass (normalize `sum=1`), the
     target inequality `OddSum(final) ≥/≤ c(n)` is *affinely equivalent* to
     `AltSum(final) ≥/≤ 2c(n)-1` (same Lemma AS identity, sum=1 fixed). This
     means the file never actually needed the OddSum label at all — the
     "connecting step" analysis can be redone in native AltSum language,
     which is arguably cleaner (no division by 2 anywhere), and the labeling
     bug, once you see this, is cosmetic to the file's *conclusion* (see
     below) even though it was a real definitional error as written.
  3. **A genuinely different opening the round should consider**: since the
     Region-C suffix term is exactly `-2·AltSum(tail below the cut)` up to
     sign/rank bookkeeping, and `self-similar-induction-on-n`'s whole
     machinery is already built in AltSum-adjacent language (Lemma AS,
     AltSum Corollary, AltSum reformulation of `T(m,k)`), the two
     approaches are not just "isomorphic in structure" but arguably
     **the same recursion in two notations** — worth explicitly checking
     whether the Rank-Shift Identity's region decomposition gives a
     *cleaner statement* of `GT(m)`'s hardest sub-case (sub-case (i),
     `q=1,e≥1`, per round 15) rather than treating them as fully separate
     lines. This is a possible merge/simplification opening, not a new
     result, but could shrink the case analysis. Not pursued further here
     (out of scope for this scouting pass — flagged for the outliner).

- **Candidate technique(s):** none new beyond what's already in play —
  peel-and-recurse induction on suffix (AltSum of the tail below a cut),
  same family as `self-similar-induction-on-n`'s `GT(m)`.

- **Cheap-kill candidates:** none obvious beyond what round 15 already
  ran; the relabel fix is arithmetic, not a new structural pruning.

- **Task 1 result — rederivation + correction, numerically stress-tested:**
  Independently rederived the algebra from the region-`A`/`B`/`C`
  rank-shift argument (matches the file's proof exactly, no error found in
  the *algebra*, confirming round 15's finding that the bug is purely
  the label, not the math). Wrote a fresh exact-`Fraction` script
  (`/tmp/rankshift_test.py`), computing:
  - `oddsum_true(L)` = true OddSum (sum of elements at odd 1-indexed rank
    only, no signs) — the canonical game quantity.
  - the file's formula (literally, unedited) as `Δ_formula` (this is
    `ΔAltSum`, confirmed by direct comparison against `altsum()` on both
    worked examples: matches `Δ=-2` and `Δ=0` exactly).
  - Tested the **corrected claim** `ΔOddSum_true = Δ_formula / 2` on:
    - Both original worked examples: Example 1 gives `ΔOddSum_true = 9-10
      = -1 = -2/2` ✓. Example 2 gives `ΔOddSum_true = 10-10 = 0 = 0/2` ✓.
    - 30,000 random single-split trials, `N` up to 8, generic (mostly
      distinct) rational values, random split ratios: **0 mismatches**.
    - 10,000 more trials, `N` up to 15: **0 mismatches**.
    - 20,000 tie-heavy trials (small value pool `{1,...,5}`, forcing
      repeated original values and ~30% exactly-equal fragments `v1=v2`):
      **0 mismatches**, confirming the Tie-Neutrality Lemma's invocation
      is sound and the corrected identity is tie-robust.
  - **Conclusion: the corrected identity (`ΔOddSum = Δ_formula/2`, i.e.
    relabel the theorem's output as `AltSum` and halve for the true-OddSum
    corollary) holds exactly, unconditionally, verified to 60,000+ trials
    with zero exceptions.** This is expected/forced given Lemma AS is
    already certified and mass is trivially conserved by a split — so this
    is confirmation, not a surprise, but a needed one (the file's own
    numbers were internally consistent for AltSum, so this check also rules
    out any *second*, independent bug beyond the label).

- **Task 2 result — does the fix unlock new leverage? Checked fresh, not
  assumed:** No. The correction is a global affine rescaling
  (`OddSum=(sum+AltSum)/2`, `sum` fixed at 1 for the normalized game), so
  it changes no boundedness property of any term. Specifically:
  - The obstruction identified in round 15 (Region C's magnitude is a
    suffix AltSum, not bounded by anything local to the cut, so no
    per-cut charge budget can bound `Σ_s Δ_s`) is a statement about
    *unboundedness relative to the split*, which is invariant under
    multiplying every `Δ_s` by a fixed constant `1/2`. A term that is
    "as large as the whole untouched tail" stays exactly as unbounded
    after halving.
  - The target inequality itself transforms affinely too: proving
    `OddSum(final) ≥ c(n)` is *identical content* to proving
    `AltSum(final) ≥ 2c(n)-1` (Lemma AS, sum=1). So there is no
    "translation gap" that the mislabeling could have hidden — the file's
    connecting-step analysis (telescoping over cuts reduces to the same
    peel-and-recurse structure as `GT(m)`) was examining the *same*
    recursion whether the quantity is called OddSum or AltSum, just off
    by a global affine reparametrization that does not touch case
    structure, feasibility regions, or which sub-case (`q`, `e`, `p`) is
    hard. I re-examined the file's own worked reduction (Example 1's
    Region-C recursion, §"The connecting step") under this lens and
    confirm it is genuinely the same shape GT(m) already formalizes (peel
    top piece, bound residual multiset's alternating/odd sum) — the
    relabeling changes no term's boundedness or dependence structure.
  - **Verdict: the round-15 self-diagnosis ("reduces to the same stuck
    GT(m) recursion, no independent leverage") is correct and is
    unaffected by fixing the OddSum/AltSum label.** This is not a case
    where the wrong quantity was analyzed and the right one behaves
    better — Lemma AS's affine equivalence means the two are
    interchangeable for exactly this kind of "is there a per-cut bound"
    question.

- **Task 3:** N/A — the corrected identity DOES hold (see Task 1), so no
  failure characterization needed.

- **Task 4 — deprioritize or keep going?** The Single-Cut Rank-Shift
  Identity itself is real, general, correct (once relabeled `AltSum`) and
  reusable — it is a strictly more general single-cut analogue of the
  already-certified insertion-only identities
  (`suffix-match-insertion-lemma.md`,
  `altsum-reformulation-and-single-insertion.md`). It is worth certifying
  into `lemmas/` (with the fix: rename to AltSum, state the OddSum
  corollary via Lemma AS with the 1/2 factor) purely as a reusable tool,
  since it strictly generalizes the existing insertion lemmas (arbitrary
  split of an existing element, not just inserting brand-new mass) and
  costs nothing to certify — future approaches needing "effect of one cut"
  can cite it directly. **But as an approach toward closing either open
  gap (the `GT(m)`, `m≥4` obstruction, or the upper-bound `Σ`-shape
  classification), this line is now confirmed (not just suspected) to
  have no independent leverage** — it is isomorphic, after the affine
  fix, to the identical recursion `self-similar-induction-on-n` already
  works with strictly more developed machinery (Theorem 7, AltSum
  Corollary, Growth Lemma, GT(m)'s case split). Recommend: certify the
  corrected identity as a lemma (cheap, real value), but **retire this
  approach as a distinct line toward the open gaps** — do not dispatch
  another builder round chasing the connecting step here; any future work
  on "bound the region-C suffix term" should be filed as a contribution
  to `GT(m)`/`self-similar-induction-on-n` directly (opening 3 above:
  check whether the region-A/B/C decomposition gives a cleaner statement
  of `GT(m)`'s open sub-case (i), as a possible simplification, not a new
  route).

- **Knowledge-base entries to use:** none new; the relevant tools are
  already all internal to this workspace (`greedy-optimality-oddsum.md`,
  `reduction-to-multiset-minimax.md`, `altsum-reformulation-and-single-
  insertion.md` i.e. Lemma AS).

- **Analogous past problems (cruxes):** not queried this round (out of
  scope for a narrow relabeling-scout lens; prior rounds' explorers have
  already covered the crux corpus for this problem — see earlier
  round reports).

- **Prior progress:** see `current.md` — shared window closed at
  `ℓ=1..4`; `GT(m)` for `m≥4` open (now narrowed to a width-1 window,
  round 15); `V(e_0)=1/2` for every `n≥3` certified
  (`lemmas/twin-anchor-floor-theorem.md`); upper-bound direction stuck on
  the `Σ`-shape classification gap.

- **Dead ends (do not retry):** the Single-Cut Rank-Shift Identity's
  *connecting step* as an independent route to either open gap — now
  confirmed dead even under the corrected labeling (this round's finding,
  not just round 15's). Do retry/keep: the identity itself as a citable
  lemma (positive, just needs the relabel-and-certify step, not a proof
  attempt).

- **Small-case / intuition notes:** the affine relation `OddSum =
  (sum+AltSum)/2` with `sum` fixed by normalization is the reason the
  mislabeling turned out to be low-stakes for the file's *qualitative*
  conclusion (still true after fixing it) but was still a real error
  worth catching, since a downstream lemma citing this file's "OddSum"
  numbers by value (not just by shape of argument) would have been off by
  exactly a factor of 2 plus an additive shift — exactly the kind of
  silent unit error that would corrupt any lemma built directly on top of
  the numeric outputs (not yet observed to have happened, since no other
  approach has cited this file's specific numbers, only its qualitative
  diagnosis).
