## imo-2026-03 — outline review, round 15

Read: `/tmp/round-15/proof-outliner.md`, `results/imo-2026-03/current.md`,
`results/imo-2026-03/approaches/.ranking.json`, `/tmp/round-15/math-explorer-plateau.md`,
`/tmp/round-15/math-explorer-fragtie.md`, `/tmp/round-15/math-explorer-caseb.md`,
`results/imo-2026-03/approaches/dyadic-potential-invariant.md`,
`/tmp/round-15/test_discharge.py` (re-ran it independently — reproduces the
report's numbers exactly, see below).

### 1. `discharging-neighbor-transfer` (new) — APPROVE

- **Genuinely a different top-level framing, not a relabeling.** Checked
  against `dyadic-potential-invariant.md`'s history: that approach's
  Cut-Reallocation Exchange Lemma (round 3-4, dead-ended) was a *single-step
  perturbation/exchange* argument, and its later pivot (round 5) went to
  LP-vertex/compactness (now folded into `global-lp-vertex-sufficiency`'s
  lineage). The new approach's mechanism — a **charge-transfer rule between
  rank-adjacent neighbors**, summed for conservation, Four-Color-Theorem
  style — is structurally different from both: it is neither a one-shot
  exchange perturbation nor a single closed-form potential evaluated per
  object. Per memory rule 14 (verify a "genuinely different mechanism"
  claim, don't take it on trust): confirmed the three prior falsified
  attempts in this family (`Cut-Reallocation Exchange Lemma`,
  `layer-cake` per-cut-additive decomposition, this round's own
  `w(v,s)=v·2^{-|log2 v-s|}`) are all *fixed-formula, rank-local-only*
  potentials — none of them defines a transfer rule between neighbors. The
  new framing is a real escalation in kind, not degree.
- **Independently reran `test_discharge.py`** (fresh execution, not just
  read): reproduces the outline's cited numbers exactly — `s=-i` top-split
  Δ=+0.03125, `s=i` top-split Δ=+0.99875/+1.71875 (frac-dependent, both
  reported instances match), `s=-(i-1)` Δ=+0.0625; middle-split `s=i`
  Δ=-0.34375 (sign flip vs top-split, exactly as claimed); random-trial max
  |Δ| up to 2.78 (order-of-magnitude comparable to piece values). My own
  first hand-rederivation (before finding the script) initially got a
  *different*, near-zero delta for `s=-i`/`s=-(i-1)` because I forgot to
  re-sort after the split — running the actual script (which does re-sort)
  confirms the falsification is real, not an artifact of my own bug. The
  cheap-kill's negative finding is solid.
- **Step 1 of the skeleton IS the mandatory numeric/algebraic hand-check**,
  not a jump to a lemma: it asks the builder to solve for a local transfer
  amount from the algebra of the `(8,4,2,1)/15` top-split example, then
  require the SAME rule to also zero the residual on a second, structurally
  different example (a middle-piece split) before generalizing — exactly
  the "two examples, one consistent rule, or it's not a real cheap-kill"
  discipline CLAUDE.md and the population's established practice require.
  Step 3 explicitly authorizes RETHINK-as-a-clean-negative-result if the
  second example fails, so the approach cannot silently force an invalid
  proof.
- Minor note (not fatal): step 2's "connecting step" (conserved charge ⟹
  OddSum bound) is honestly flagged as a second, entirely separate open
  gap even if step 1 succeeds — good, this is not hidden behind "then it
  follows." No change requested.
- File does not yet exist on disk (only described in the outline) — per
  memory rule 19, not fatal; the builder must create
  `results/imo-2026-03/approaches/discharging-neighbor-transfer.md` from
  the outline skeleton as its first deliverable.

### 2. `global-lp-vertex-sufficiency` (revise) — APPROVE

- **Star-topology cheap-kill (step 1) correctly gates before any lemma
  writing.** The skeleton explicitly requires exhaustive testing (every
  hub choice, every partner subset, exact optimum over free parameters,
  exact rational arithmetic) against the SAME fresh random points that
  killed the descending chain, "BEFORE writing any lemma," and instructs
  recording a dead end and moving to step 2 in the same round if it fails
  — no shortcut to Key-lemma-writing is permitted.
- **Descending-chain family correctly marked DEAD, not silently
  re-attempted.** Cross-checked against `math-explorer-fragtie.md` finding
  3: exact (not grid-approximated) exhaustive optimization over the full
  descending-chain family fails at fresh random points — 2/20 at n=3, 4/12
  at n=4, with an explicit n=3 counterexample
  (`p≈(0.4508,0.2550,0.1852,0.1090)`, best chain value ≈0.5598 > c(3)
  ≈0.5333). The outline states this plainly ("DECISIVELY DEAD ... do NOT
  re-attempt searching harder within this family") and does not schedule
  any further work on it. Correct.
- The fallback (step 2, existence-only Σ(n,k) route via per-cell LP
  certificate) is concrete enough to be a real target (uses the
  already-certified affineness of `f_σ` on cells), though it is honestly
  flagged as "only sketched, not yet attempted."
- No issues found.

### 3. `self-similar-induction-on-n` (revise) — APPROVE, with one note

- **Step 1 (index-match sub-case (i) to G(m,k;V)) is a genuine, concrete,
  cheap mechanical check**, not a vague restatement — it names the exact
  substitution (`m=k-1`, `V=2^k-a_1`, `B=` the specific residual elements)
  and explicitly requires doing this before any proof effort, matching the
  cheap-kill discipline. Matches `math-explorer-caseb.md` opening (A)
  essentially verbatim (index-matching sub-case (i) to the round-3/4
  `G(m,k;V)` object) — not invented by the outliner, traceable to the
  explorer's own finding.
- **Route (3), the continuity/limiting transfer for Case-B(m,k)'s
  boundary**, is concrete and matches `math-explorer-caseb.md`'s
  numeric lead (margin → 0 monotonically as `max(D)→2^{m-1}⁻`, for
  m=3..8) and its "Idea (B)" (push the certified Elementwise/Growth-Lemma
  machinery to the boundary via continuity rather than a fresh
  induction). The outline correctly identifies the actual open content —
  "uniformity in δ," not just "margin→0" — as the thing to prove, not
  assume; this is the right level of skepticism (a pointwise-vanishing
  margin sequence does not automatically give a uniform bounding
  technique).
- **Watch-out clause is present and correct**: explicitly distinguishes
  the new G(m,k;V) route (varying target V) from the already-refuted
  "piece-cap-relaxed generalization of GT(k-1)" (D={0.4,0.4}
  counterexample), and requires the builder to verify this distinction in
  step 1 rather than assume it. Good — this is exactly the kind of
  re-labeling risk memory rule 9 warns about, and the outline pre-empts it.
- Minor: the outline's step 1 also needs to confirm sub-case (i) is
  reached only once `e` grows past `log_2(m+1)` (round 14's feasibility
  diagnosis) actually holds in the regime the continuity argument targets
  — flagged in the outline's own "Cases to cover," not overlooked.
- No fatal issues; this is a legitimate two-pronged attack on the single
  remaining named obstruction, both prongs freshly informed by this
  round's explorer, neither a rehash of a dead end.

### 4. `lp-duality-split-polytope` (advance) — APPROVE

- Straightforward extension (n<6 case of the Chain-Correction Floor
  construction) plus a cross-validation duty (interpret
  `global-lp-vertex-sufficiency`'s star-topology numeric result if any
  near-miss appears) — the outline explicitly instructs NOT duplicating
  the star-topology test itself, avoiding wasted parallel work. No new
  lemma proposed; scope is honest.

### Diversity check

The four approaches now span four structurally distinct mechanisms:
peel-and-recurse induction (`self-similar-induction-on-n`), LP-vertex /
compactness classification (`global-lp-vertex-sufficiency`), explicit
LP-duality constructions at region vertices (`lp-duality-split-polytope`),
and — newly — charge-transfer discharging (`discharging-neighbor-transfer`).
The plateau-check explorer's own finding (both core gaps stalled through
rounds 13-14 under the same two mechanisms) is the correct trigger for
opening the discharging line this round; this is not a repackaging of
either stalled mechanism. No collapse-to-one-framing risk this round.

### Dead ends confirmed not silently re-attempted

- Cyclic pairwise-tie chain, descending fragment chain (as a general
  mechanism), bounded-`s_0` named constructions, region-geometry/exchange
  mechanisms, majorization/Schur monotonicity, structured randomization,
  `w(v,s)=v·2^{-|log2 v-s|}` (all 3 scale conventions) — none reappear as
  a proof step in any of the four outlines above; all are correctly listed
  under "watch out for" / "do NOT re-attempt" where relevant.

### Ranking

Registered `discharging-neighbor-transfer` (new, cold-start 1500). Ranked
the sampled field head-to-head, anchoring the newcomer against established
approaches rather than only against itself:
- `lp-duality-split-polytope` beats `global-lp-vertex-sufficiency` (round
  14: certified new theorem vs. only negative cheap-kill findings this
  cycle).
- `self-similar-induction-on-n` beats `global-lp-vertex-sufficiency` (two
  certified general-purpose lemmas vs. only negative findings).
- `lp-duality-split-polytope` vs `self-similar-induction-on-n`: draw (both
  produced genuine certified content of comparable weight this cycle).
- `global-lp-vertex-sufficiency` beats `discharging-neighbor-transfer`
  (10-round mature machinery, `Q_region` fully closed, vs. an entirely
  untested newcomer).
- `self-similar-induction-on-n` beats `discharging-neighbor-transfer` (same
  reasoning).

Post-update Elo: `lp-duality-split-polytope` 1599.0, `self-similar-
induction-on-n` 1550.9, `global-lp-vertex-sufficiency` 1521.0,
`discharging-neighbor-transfer` 1470.7. All `stale` flags on the four
touched approaches are now cleared.

### Build set

All four outlines pass review with no fatal flaws. Per CLAUDE.md's "few
strongest, normally 1-3" guidance, and because `discharging-neighbor-
transfer`'s entire first-round content is a single cheap 30-60 minute
hand-algebra check (cannot usefully be split further, and per the
plateau-break directive must be tried this round), and the other three all
have concrete, independently-motivated next steps this round — build all
four.

build set: self-similar-induction-on-n, global-lp-vertex-sufficiency, discharging-neighbor-transfer, lp-duality-split-polytope
