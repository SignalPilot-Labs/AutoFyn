# Round-5 outline-reviewer report — imo-2026-03 (Chu-Han war)

Reviewed the outliner's field of 5 (pairing-charging advance, dyadic-induction revise, lp-dual-region new, alternating-potential keep, minimax keep) against the round-4 outcomes, the three round-5 explorer reports, and the certified lemma cache. Adversarially checked each for wrong technique, unjustified leaps, missing cases, circular reasoning, and dead-route revival. Small-case numerics run independently (Python `fractions`): cross-piece cheap-kill gives D=0 on the worst 14-family config (verified); iii-a bound D≥1 holds at n=4..7 (my random search finds min D=1 at n=4 — the explorer's "≥3" claim was too strong, but the outline's weaker D≥1 target is correct).

## Per-approach verdicts

### pairing-charging — APPROVE (advance)
Target: whole G2 upper bound via peel-once + polyhedral-vertex reduction on the Case-C construction value.
- The vertex-reduction skeleton is **sound**: `v(p) = min` over (peel × menu-member) is a minimum of piecewise-linear functions of `p`, hence PWL (piecewise-concave per cell of the sort-regime arrangement); a PWL function on a compact polytope attains its max at an arrangement vertex. The KB entry *Piecewise-concavity smoothing* is the right template. The arrangement vertices are finite and explicit for n=3 (~30–60); an exact-rational script can enumerate them. This is a legitimate, finite, rigorous collapse of the 12-expression casework — the cleanest bookkeeping for the verified 0/30k construction.
- The honest flags are correct: (a) "5 of 12 dominate" is EMPIRICAL (200k configs), NOT proved — the outline correctly falls back to the full 12-expression vertex table if domination can't be shown; (b) the uniform-in-n structural claim for `f_n` is a CONJECTURE (verified n=3 only) — the outline explicitly says "do NOT present it as proved" and treats n=3 Case C as the deepest base that must close directly before n≥4 is attackable (nested induction). Good — no overclaiming.
- **One subtlety the builder must handle (minor, not fatal):** the Case-C polytope `Π_C = {p_2<4/15, p_3<4/15, p_4>1/15}` is OPEN (strict inequalities); the supremum `1/15` is approached at the dyadic boundary vertex `(8/15,4/15,2/15,1/15)` which lies ON the `p_2=4/15` / `p_3=4/15` facet — i.e., on the Case-B side, already PROVED by Lemma 5. So the proof must argue: on the closed arrangement, every vertex has `v ≤ 1/15` with equality ONLY at the dyadic vertex (which is Case-B's, covered); on the open Case-C interior, `v < 1/15` strictly. The outline's phrasing ("equality only at the dyadic vertex") is compatible with this but the builder must state the open-polytope / boundary-handled-by-Case-B point explicitly. APPROVE — build.
- Avoids all recorded dead routes (no naive surplus-chain — explicitly flagged FALSIFIED; no 2-peel subfamily pruning — flagged fails 180/30000).

### dyadic-induction — CHANGES REQUESTED (revise, stays live)
Target: whole G1 lower bound via superincreasing/Zeckendorf dyadic-edge overflow (G1-i-HC) + G1-iii split + rest-split induction.
- **G1-i-HC superincreasing overflow is a legitimate, sound research direction.** The explorer's exact characterization (n=4, s=3 tight family: complement `E_{R_0} ∩ E_F` = sliver `(2, 2+ε_3]` of measure `ε_3` = target exactly) is real evidence. The mechanism — `E_{R_0}`'s dyadic bands are superincreasing, F's breakpoints cannot all align with tower edges because F sums to a non-dyadic W — is a valid pigeonhole/extremal forcing. The hard step (make "total misalignment-measure ≥ (W+1−D_{R_0}−D_F)/2" rigorous for general s≥3 across s−1 breakpoints × ~n/2 dyadic edges) is honestly flagged as the load-bearing unproved crux, with a cheap parity-count variant to try first. Sound.
- **G1-ii boundary lift by continuity (conditional on G1-i-with-rest-split closing) is sound and already certified** (round 4). Correctly noted that the perturbed config lands in G1-i WITH REST SPLIT — the union of G1-i-HC + rest-split induction, not Lemma 8's rest-unsplit case. Honest.
- **Rest-split induction (step 6, Opening B) is the right vehicle** — induct on the number of rest-splits, not on n or s (the merge-induction is DEAD, 1490/2913 merges increase D, correctly flagged). The outline correctly demands a STRUCTURAL inductive hypothesis (rigid-tiling pattern survives the toggle), not a numeric-only one (which would be circular, the round-2 scalar-invariant ruling). Honest.
- **FLAW — G1-iii-a peeling-pair mechanism is UNSOUND as stated (fixable).** The outline claims: "the fragments of `2^n` sum to `2·2^{n−1}`; pair them greedily (largest with second-largest, etc.) and the peeling lemma cancels each near-equal pair (parity-neutral), leaving the dyadic `(n−2)` floor `≥ 1`." This misuses the peeling lemma: `lemmas/peeling.md` requires EXACTLY equal pairs `(p_j, p_j)` for parity-neutrality; "near-equal" pairs do NOT cancel. Greedy pairing of arbitrary fragments of `2^n` does not produce exact equal pairs. The BOUND (D ≥ 1 in iii-a) is TRUE — I verified it independently (min D = 1 at n=4 via random search over r=3..6 fragment partitions; the explorer's "≥ 3" claim was too strong, but the outline's weaker D≥1 target holds). But the stated MECHANISM does not prove it. The builder must replace the peeling-pair argument with a correct one (e.g., a direct parity-integral / dominant-M argument: M = 2^{n−1} IS the rest's largest piece and IS the global largest since all 2^n fragments are < 2^{n−1} = M; so the dominant-M regime applies — but the overlap bound for multi-fragment F is exactly G1-i-HC, so iii-a may not be as "easy" as claimed and may reduce to G1-i-HC itself). This is a real gap in a sub-lemma, not a fatal flaw in the approach — hence CHANGES REQUESTED, not RETHINK. The approach stays live; the builder must prove iii-a correctly (or fold it into G1-i-HC) rather than hand it to a broken mechanism.
- **G1-iii-b (flat, rest's 2^{n−1} SPLIT, all pieces < 2^{n−1}):** correctly flagged as the genuinely-hard flat twin of G2-flat (verified n=4: min D = 1 at `{6,6,4,4,4,4,2,1}`). The outline honestly says it may resist tiling rigidity (no dominant M) and outlines a fallback (route to lp-dual-region's flat machinery). Honest flagging; no overclaim. APPROVE on iii-b's handling.
- Avoids the dead "reduce to G1(n−1)" (explicitly flagged UNSOUND) and merge-induction (DEAD). Good.

### lp-dual-region — APPROVE (register as new)
Target: whole G2 upper bound via per-region LP duality + cross-piece equal-pair cheap-kill. Genuinely-different continuous framing.
- **Cross-piece equal-pair cheap-kill is VERIFIED and sound.** I confirmed independently: for the worst 14-family config `(5/11, 3/11, 2/11, 1/11)` (where `p_1 = p_2 + p_3` exactly), Xiang splits `p_1 → p_2 + p_3` (1 cut) and equal-halves `p_4` (1 cut) ⟹ final multiset `{p_2, p_3, p_2, p_3, p_4/2, p_4/2}` = three equal pairs, each at adjacent ranks ⟹ D = 0 exactly (≤ 2 marks, well under the n=3 budget of 3). This is a real, concrete, NEW lemma that generalizes `pairwise-diff-strategy` (which only equal-halves within pieces) to cross-piece equalities — the lever the round-4 finite family structurally missed. The outline honestly flags it as a cheap-kill for `p_1 ≈ p_2 + p_3` configs ONLY, not the whole proof. Good.
- **Per-region LP-dual framing is genuinely different from pairing-charging's vertex check.** pairing-charging fixes a finite strategy family (3-peel × n=2 menu) and checks the construction value over Liu-config space; lp-dual-region fixes Liu's config and optimizes over Xiang's CONTINUOUS cut-space (reaching cross-piece equal-pair vertices the finite family can't). The explorer's probe (0/80 flat configs exceed 1/15 under continuous optimization; worst 0.0555; D=0 on the worst 14-family config) confirms the continuous optimum is strictly tighter than the finite-family value. The framing difference is real: continuous-construction + LP-dual-certificate language vs. finite-strategy vertex check. Not mechanical casework in disguise — the construction is richer (D=0 kills that the finite family misses).
- **D is linear within each sort-region** (parity-integral: `j(t)` constant on intervals with endpoints linear in β) — sound. **Per-region LP has no integrality gap** (Liu fixed, no info asymmetry — the round-4 "LP-dual dead" verdict was about the Stackelberg-BLIND LP, a different LP; the outline correctly distinguishes them). Sound.
- **Honest hard-step flagging:** the per-region dual weights are config-dependent in the flat regime (not universal dyadic weights); route (a) mechanical enumeration (≤ 630 sort-regions for n=3, rigorous but ugly) is the fallback if route (b) unifying-scheme hunt fails. The outline explicitly offers the builder this choice and flags the "hand-waving by computer" risk. Honest.
- **Avoids ALL dead routes** explicitly: von-Neumann minimax (TRAP — D not convex in cuts, Liu-side convexity = DEAD collapse-theorem/flattening), topological/connectedness (collapses to per-region LP with no leverage), linear-in-D potential (DEAD factor-of-2 wall), Stackelberg-blind LP (DEAD integrality gap). Good.
- The framing is genuinely different from pairing-charging/minimax finite families AND from the dead collapse-theorem (which was Liu-side convexity; this is Xiang-side per-region LP). Register. The builder should prove the cross-piece equal-pair lemma FIRST (it's the verified, concrete, certifiable result) and treat the full per-region dual as the research goal.

### alternating-potential — APPROVE (keep alive, no re-dispatch)
- Conditional machinery (toggle lemma, peeling corollary, G1-ii r=2 closed, G1-ii r≥3 ⟹ G1-i continuity reduction) is CERTIFIED and reusable — real donated contributions to the field. G2 conceded (sound, factor-of-2 wall dead). The G1-ii reduction becomes load-bearing the moment dyadic-induction closes G1-i-with-rest-split. No re-dispatch this round (per outliner; G1-i not yet closed). Correct disposition. Avoids reviving linear-in-D potential (flagged DEAD).

### minimax-strategy-family — APPROVE (keep as n=2-certified baseline, no re-dispatch on n≥3 finite families)
- n=2 upper bound CLOSED + CERTIFIED (5-member menu, 2-case contradiction, tight at dyadic, unique-worst-at-dyadic). `pairwise-diff-strategy` lemma certified and importable by lp-dual-region. G2-flat n≥3 honestly CONCEDED to continuous/inductive siblings (finite-family framing confirmed insufficient: 0.68% residual, worst 0.0876 > 1/15; the continuous LP gives D=0 on the same worst config via cross-piece equal pairs the finite family misses). The outliner correctly does NOT re-dispatch on n≥3 finite families. Correct disposition — stands as the certified baseline + induction base for pairing-charging's `f_n`.

## Registration

- **lp-dual-region** — NEW approach, APPROVE. Registered via `mcp__approach-ranker__register_approach(problem_id="imo-2026-03", slug="lp-dual-region", summary="G2 upper bound via per-region LP duality on Xiang's continuous cut-space + cross-piece equal-pair cheap-kill generalizing pairwise-diff-strategy.")`. Enters the population at cold-start Elo 1500, zero outcomes.
- No copy requested by the outliner this round (skip).
- No RETHINK cuts (no doomed new approach registered; collapse-theorem stays unregistered from round 4).

## Ranking (whole field, head-to-head, anchored to round-4 outcomes)

Comparisons (anchored: pairing-charging is the closest a builder has been to closing the real G2 wall — Case C vertex reduction, certified machinery, 0/30k verified; dyadic-induction has certified Lemmas 7/8/9 but a flawed iii-a sub-mechanism; minimax has a certified n=2 complete sub-result but conceded the n≥3 frontier; lp-dual-region is cold-start with verified cheap-kill but zero outcomes — not ranked above proven-advanced; alternating is deferred/conditional; surrogate is dead):

```
update_ranking(problem_id="imo-2026-03", comparisons=[
  {"winner": "pairing-charging",        "loser": "dyadic-induction"},         // pairing closest to closing real G2 wall; dyadic iii-a mechanism flawed
  {"winner": "pairing-charging",        "loser": "minimax-strategy-family"},  // pairing advancing on open G2; minimax conceded n>=3
  {"winner": "pairing-charging",        "loser": "alternating-potential"},    // pairing headline; alternating conditional/deferred
  {"winner": "pairing-charging",        "loser": "lp-dual-region"},           // proven-advanced vs cold-start (zero outcomes)
  {"winner": "pairing-charging",        "loser": "surrogate-adversary"},      // advanced vs dead-end
  {"winner": "dyadic-induction",        "loser": "minimax-strategy-family"},   // dyadic still advancing on open G1 wall (Lemmas 7/8/9); minimax ceded frontier
  {"winner": "dyadic-induction",        "loser": "alternating-potential"},     // dyadic active lower-bound attacker; alternating deferred
  {"winner": "dyadic-induction",        "loser": "lp-dual-region"},            // proven advanced (certified Lemmas 7/8/9) vs cold-start
  {"winner": "dyadic-induction",        "loser": "surrogate-adversary"},       // advanced vs dead
  {"winner": "minimax-strategy-family","loser": "alternating-potential"},      // minimax has certified n=2 complete sub-result; alternating conditional
  {"winner": "minimax-strategy-family","loser": "surrogate-adversary"},        // advanced vs dead
  {"winner": "minimax-strategy-family","loser": "lp-dual-region", "draw": true}, // minimax proven n=2+lemma vs lp-dual stronger terrain on open wall — balanced
  {"winner": "lp-dual-region",         "loser": "alternating-potential", "draw": true}, // lp-dual fresh active on open wall vs alternating deferred w/ certified machinery — balanced
  {"winner": "lp-dual-region",         "loser": "surrogate-adversary"},        // fresh vs dead
  {"winner": "alternating-potential",  "loser": "surrogate-adversary"}        // advanced vs dead
])
```

Expected post-ranking order (approx): pairing-charging (~1630+) > dyadic-induction (~1590+) > minimax-strategy-family (~1500) ≈ lp-dual-region (~1500) > alternating-potential (~1435) > surrogate-adversary (~1360).

## Diversity assessment

The field has NOT collapsed. The two G2 routes are genuinely far apart: pairing-charging = finite-strategy vertex-check on Liu-config space (peel-once + n=2 menu, the certified construction); lp-dual-region = continuous cut-space optimization + LP-dual certificate (reaches cross-piece equal-pair vertices the finite family structurally misses, verified D=0 on pairing-charging's worst 14-family config). They reach different configs and use different certification language. The lower-bound side (dyadic-induction superincreasing overflow + rest-split induction) is a distinct framing from the upper-bound continuous LP. No two slugs are the same proof split into pieces. Good diversity.

## Build set

Per CLAUDE.md (mix approaches-to-advance + new approach opened this round), and consistent with the outliner's recommendation:

build set: pairing-charging, dyadic-induction, lp-dual-region

- **pairing-charging** — advance: close n=3 Case C via the polyhedral-vertex reduction (enumerate arrangement vertices, evaluate `v` at each, confirm `≤ 1/15` with equality only at the dyadic boundary vertex which is Case-B's). Handle the open-polytope subtlety explicitly. Fall back to full 12-expression table if the 5-of-12 domination can't be proved. Treat the uniform-in-n `f_n` claim as conjecture (do not present as proved).
- **dyadic-induction** — advance: attack G1-i-HC via superincreasing/Zeckendorf dyadic-edge overflow (try the cheap parity-count variant first); CORRECT the G1-iii-a mechanism (peeling-pair is unsound — peeling lemma needs exact equal pairs; find a correct argument for D ≥ 1, likely reducing iii-a to G1-i-HC since M = 2^{n−1} is the dominant piece); flag G1-iii-b as the flat hard twin honestly; induct on rest-splits with a STRUCTURAL hypothesis.
- **lp-dual-region** — new build: prove the cross-piece equal-pair cheap-kill lemma FIRST (verified, certifiable); then attempt the per-region LP-dual certificate for n=3 (route a mechanical enumeration as the rigorous fallback; route b unifying-scheme as the research goal). Do NOT propose von-Neumann minimax / topological / linear-in-D / Stackelberg-blind LP (all DEAD).
