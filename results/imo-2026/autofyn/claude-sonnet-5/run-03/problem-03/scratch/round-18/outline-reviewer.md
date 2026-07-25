# Outline review — round 18 (imo-2026-03)

Reviewed: `/tmp/round-18/proof-outliner.md` against `results/imo-2026-03/current.md`
(reviewer-owned record through round 17), the three revised approach files,
and the three round-18 math-explorer reports. All three candidates are
**revisions of existing whole-attempt slugs** (no new slug, no split-off
fragment) — each still targets the problem's actual claim end to end
(lower-bound direction / upper-bound direction / a secondary necessity
lemma feeding the upper-bound direction). No single-gap-trap risk this
round: the field genuinely diversifies (integer telescoping-identity
problem on the LB side vs. continuous LP-vertex/perturbation problem on
the UB side vs. a mass-counting necessity lemma) — the plateau-check
explorer explicitly re-confirmed these are NOT converging into one wall.
Good, no action needed on diversity this round.

## Independent verification performed

**(a) Cardinality-cap scoping of the (k,e)=(2,1) counterexample.**
Re-derived from scratch (own `Fraction` script, not reusing the builder's
or the round-18 explorers' code). At $k=2,m=3$ ($e=1$), $\Gamma_{k-1}=
\{1,2\}$, target $T_{\mathrm{odd}}(a_1)=2^m-2^k-\tfrac{2^{m+1}-2^{k+2}}3$.
For $a_1=494/125\approx3.952$, the round-17 counterexample's $R$ has
$|R|=4$ (i.e. $|D|=5>m+1=4$) — confirmed out of `GT(m)`'s own scope.
Enforcing $|R|\le m=3$ and scanning both random (200k+ trials) and
structured extremal shapes ("all-equal" vs "as-many-at-cap-plus-one-
remainder") over $a_1\in[3,4]$: **zero violations**, margin strictly
decreasing to exactly **0** at the boundary $a_1=2^k=4$ (attained exactly
by $R=\{2,2\}$, matching $\Gamma_1\cup R$'s $\mathrm{OddSum}=4=T$
exactly), and the minimizing extremal shape transitions from "all-equal"
to "cap-fill+remainder" as $a_1\to2^k$ — this independently corroborates
both round 17's finding and the round-18 explorer's numeric report
(margins $0.65\to0.5\to0.2\to0.05\to0.01$ as $a_1\to4$, matching the
reported $\approx0.006$ at $a_1=3.99$ closely). **The outline's premise
is correct and independently re-confirmed**: the counterexample is
genuinely out of scope once the cap is enforced, and the proposed
extremal-shape mechanism (forced odd/near-cap count leaves an unpaired
element) is directionally the right one — but this is still only
numeric/structured-search corroboration at one $(k,e)$ pair, not a
general proof. The outline correctly does NOT claim the
Cardinality-Constrained Half-Sum Lemma is proved — it is listed under
"Open gaps," exactly as it should be.

**(b) The "$V(p)$ sup strictly below $c(n)$, gap shrinking with $n$"
claim.** Confirmed this is explicitly flagged float/Nelder-Mead,
two-data-point ($n=2,3$), by the round-18 explorer report itself
(`math-explorer-flat-edge-maximizer.md`, "Small-case / intuition notes
(all conjectural, float-based, not exact)"). The outline's "Watch out
for" section correctly forbids certifying "gap ~0.042," "gap ~0.012," or
"shrinks with $n$" until re-derived in exact arithmetic, and Step 2
explicitly mandates converting to exact rational optimization
(sympy/Fraction) before any proof investment. **This is handled
correctly — the outline does not let a heuristic numeric lead pass as
established.**

## Per-approach verdicts

### `self-similar-induction-on-n` — APPROVE
- Correctly and precisely restates the *only* open residual (odd $e=1$,
  outside window, under the cap; odd $e\ge3$ separately flagged as
  unconfirmed) — matches `current.md`'s round-17 entry exactly, no
  restatement drift.
- Cheap-kill-before-lemma sequencing (step 2 before step 3) is sound
  practice and appropriately ordered.
- The proposed **Cardinality-Constrained Half-Sum Lemma** has a genuine,
  checkable mechanism (an odd/near-cap-forced count leaves an unpaired
  element contributing at full value, not half) — independently spot
  verified above; this is a real candidate mechanism, not a hand-wave.
- "Watch out for" explicitly bans reusing the cap-free Half-Sum
  Corollary — correct, since that is exactly the tool that produces the
  genuine (cap-free) counterexample at $(k,e)=(2,1),a_1=494/125$; also
  correctly flags the recurring Odd$\to$Odd vs Odd$\to$Even telescoping
  bug class (round 16's dead end) for re-verification inside the new
  lemma's proof — a legitimate standing risk, worth the explicit
  reminder.
- Step 5 (odd $e\ge3$) is correctly scoped as a separate, NOT-yet-closed
  deliverable, not folded silently into the headline — avoids repeating
  round 16/17's overclaim pattern.
- No fatal flaw found. One thing to watch during the build: the
  "worst-case-at-endpoint" monotonicity claim (margin shrinks
  monotonically to 0 as $a_1\to2^k$) is asserted from numeric evidence
  only (4 values of $k$) — the outline correctly lists this as
  "supports... being the unique worst point," not as proved; the builder
  must not silently upgrade this to a proved monotonicity fact without
  actually establishing it (it is likely provable directly from the
  extremal-shape argument once constructed, but that is not yet done).

### `global-lp-vertex-sufficiency` — APPROVE
- Correctly treats this round's own numeric lead as conjectural
  (verified above) and mandates exact re-derivation as the very first
  step before any proof investment — sound gate.
- Step 1's pivot (defer Flat-Edge classification, since the two located
  near-optima are tie-free or a kink, not a Flat-Edge plateau) is
  consistent with the certified Flat/Kink Parity Lemma and does not
  discard certified machinery, only reprioritizes it — appropriate,
  reversible scoping, not a technique change that risks a dead end.
- Step 3's reduction (Existence Theorem $\Leftrightarrow$ a finite list
  of exact cell-vertex values, since $\Sigma(n,k)$ is finite and each
  $f_\sigma$ affine — both already certified) is a valid application of
  already-proved machinery, not a new unproven leap.
- Honestly scopes the open items (general-$n$ tractability of the cell
  list; whether every non-located cell can be pruned cheaply) as open,
  not glossed over.
- No fatal flaw found. Correctly reiterates that $p_{LB}$ is confirmed
  out of the balanced region (round-18 explorer independently
  reconfirmed $p_{LB}\notin$ balanced region again) — a documented dead
  end correctly not revisited.

### `lp-duality-split-polytope` — APPROVE (light/optional, as scoped)
- Correctly demotes this approach's headline ($s\ge n-1$ necessity) to
  out-of-reach-by-refinement per the plateau-check explorer's asymptotic
  (not just numeric) argument that Mass-Constraint provably caps at
  $s\gtrsim N/2$ — this is the right call; continuing to sharpen the
  same technique would be wasted effort.
- The dispatched fallback (a cheap 30-minute double-counting/cyclic-sum
  sketch analogous to aimo-0091/aimo-0178) is explicitly and honestly
  flagged as a weak analogy (different target objects — grid seams/cube
  beams vs. split-fragment masses) and capped at a lottery-ticket-scale
  time budget, not framed as a committed proof line. No overclaim risk.
- Appropriately light dispatch, consistent with CLAUDE.md's framing of
  this approach as secondary/optional this round.

## Diversity check

The three approaches attack genuinely different objects: an integer
telescoping/peeling identity under a hard cardinality cap (LB direction);
a continuous LP-vertex/perturbation classification over a compact region
(UB direction, Existence Theorem); and a mass-counting necessity bound at
one region vertex (a secondary lemma feeding the UB direction, now
explicitly de-emphasized). The plateau-check explorer re-confirmed these
do not share one underlying wall. No collapse-to-one-framing risk this
round — no action needed.

## Verdicts summary

- `self-similar-induction-on-n`: APPROVE
- `global-lp-vertex-sufficiency`: APPROVE
- `lp-duality-split-polytope`: APPROVE (light/optional dispatch, per outline)

No new slugs to register this round (all three revise existing,
already-registered approaches); no branch/copy requested by the
outliner. Ranking updated via `update_ranking` (self-similar-induction-on-n
and global-lp-vertex-sufficiency both edge past lp-duality-split-polytope,
which is now explicitly de-prioritized for its headline conjecture;
self-similar-induction-on-n edges past global-lp-vertex-sufficiency this
round on the strength of its narrower, independently-verified-as-nearly-
tight residual vs. global-lp's still-heuristic numeric lead).

build set: self-similar-induction-on-n, global-lp-vertex-sufficiency, lp-duality-split-polytope
