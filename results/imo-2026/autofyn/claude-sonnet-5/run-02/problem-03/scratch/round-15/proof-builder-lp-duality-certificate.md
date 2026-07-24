# Round 15 build report — lp-duality-certificate (IMO-2026-03)

## Task recap

Round-15 outline (see `approaches/lp-duality-certificate.md`, "## Round 15
outline" section) asked for two things: (1) formalize the round-15
explorer's "Cross-Piece Sign-Assignment Identity" as a rigorous general
lemma, proving it from `pair-cancellation-identity`/`odd-run-reduction-lemma`
(executing round 9's flagged-but-unexecuted suggestion), and verify it
against both round-14 near-tight case-(b2) witnesses ($n=3$ flat-face,
$n=4$ pinned-tie); (2) attack the resulting sign-vector feasibility question
for case (b2) as a finite combinatorial problem, not continuum optimization.

## What was done

**Part 1 — Cross-Piece Sign-Assignment Identity.** Formalized and proved in
full generality (`lemmas/cross-piece-sign-assignment-identity.md`): given a
final multiset $M$ from any legal Xiang Yu move, apply `odd-run-reduction-
lemma` to collapse exact ties (any pairing, any pieces involved), then
regroup the resulting tie-free multiset's alternating sum by piece — an
elementary partition of a finite sum. If each piece's surviving fragments
occupy one common rank-parity, the piece contributes its whole surviving
mass with that sign; summing gives $A(M)$ exactly. This strictly
generalizes `pair-cancellation-identity`/`bisect-top-k-lemma` (their case is
$q_i=0$ from same-piece cancellation) by also covering (a) non-adjacent
same-parity survival (a piece keeps its *whole* value with a sign) and (b)
genuine cross-piece ties, both via `odd-run-reduction-lemma`. Verified
against 20000 random constructions (6989 monochromatic, zero mismatches)
and, via exact-fraction reconstruction, against **both** round-14 witnesses:
the identity reproduces each exactly, and in doing so shows **both
witnesses are unconditionally closed** by an explicit legal response
($\Phi\approx0.51585<a_3T$ at $n=3$; $\Phi\approx0.50455<a_4T$ at $n=4$) —
a concrete result beyond round 14's own numeric-only probe of these points.

**Part 2 — feasibility as a finite combinatorial problem.** Built the
**Alternating Gap-Cross Lemma** (`lemmas/alternating-gap-cross-lemma.md`):
an explicit $j$-parameter construction (split $p_1,p_3,p_5,\dots$, each
sandwiching the following even piece) with a **closed-form, non-numeric**
feasibility test derived from an explicit interval/supremum argument (not a
search) — proved and independently cross-checked against a constructive
search (8000 trials, zero disagreements). This gives a genuine unconditional
sufficient condition (identity + feasibility test), and it exactly recovers
and closes the $n=3$ witness; the $n=4$ witness is correctly identified as
infeasible for this construction (it needs Part 1's tie-based mechanism
instead — an honest scope boundary, confirming the two witnesses are
genuinely different vertex types, as the round-15 scout found).

**Honest limitation, reported not hidden:** quantified the new
construction's marginal coverage of case (b2) over `bisect-top-k-lemma`
alone via a fresh random sampler: 5.0%→7.5% at $n=3$, no measurable change
at $n=4,5$ (40 samples each). So while this round closes both on-file
near-tight witnesses and adds two new general certified lemmas, **case (b2)
remains open in general** — not overclaimed as solved.

## Bugs caught during derivation (self-corrected before finalizing)

- First draft of the Alternating Gap-Cross identity assumed the tail's own
  alternating contribution was unaffected by how many elements preceded it;
  a failing test case (m=4, j=3 mis-handled, then a genuine m=4,j=2 case
  with nonempty tail) exposed that inserting an odd number of elements
  before the tail flips its parity, requiring the $(-1)^j$ prefactor. Fixed
  and re-verified (10000 trials, zero mismatches after the fix).
  Also caught an early mis-scoped "always realizable" legality claim for
  the single-pair (j=1) case — it is not automatic; derived and verified
  the correct closed-form feasibility condition instead.

## Files changed

- `results/imo-2026-03/lemmas/cross-piece-sign-assignment-identity.md` (new)
- `results/imo-2026-03/lemmas/alternating-gap-cross-lemma.md` (new)
- `results/imo-2026-03/approaches/lp-duality-certificate.md` (updated:
  Status/Approaches-tried/Current-best headers, new "Round 15 build"
  section, new "Open gaps" entry)
- Verification scripts (not persisted into the repo, per project
  convention): `/tmp/round-15/verify_crosspiece2.py`,
  `/tmp/round-15/verify_witnesses3.py`, `/tmp/round-15/verify_witness_n4b.py`,
  `/tmp/round-15/verify_altgapcross3.py`,
  `/tmp/round-15/verify_closedform_feasibility.py`,
  `/tmp/round-15/coverage_check_round15.py`,
  `/tmp/round-15/check_nonneg_A.py`.

## Status of this slug after this round

Still `partial`. Open Gap 1 (general upper bound, case (b2)) remains open.
Genuine new content: two certified general lemmas, both on-file near-tight
witnesses now unconditionally closed (not just numerically probed), and an
honest quantification that the new mechanism's coverage gain is modest.
Recommend next round either extend Alternating Gap-Cross (allow sandwiched
pieces to also be split) or pursue the round-14 fallback (case (a)
conditioning sharpened so case (b2) recursion escapes one level down), per
the "Open gaps" section appended to the approach file.
