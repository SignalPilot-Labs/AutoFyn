# outline-reviewer — round 2 — imo-2026-03 (Chu-Han war)

Goal: prove `c(n) = 2^n/(2^{n+1}−1)`. Two open walls: G1-general (lower-bound splits-inequality `D ≥ 1/D_n` for the dyadic config after ≤ n Xiang splits, n ≥ 3 and the n=2 two-mark sub-case) and G2-general (upper bound `D ≤ 1/D_n` for ARBITRARY Liu marks, n ≥ 2 — the real IMO wall). Round-1 field of four converged on the D-monovariant; round 2 diversifies the upper-bound framings (direct partition vs amortized potential vs minimax-over-family) and closes G1 via convexity/parity-integral.

Verified independently this round (Python, `fractions`):
- **G1 n=2 (two-mark included):** brute-force over all ≤ 2-split refinements of `{4,2,1}/7` (rational grid N=40): min `D = 1` (units of 1/7), attained at equal-halving AND at the "barely-split 4 into 3+1" family. Target `D ≥ 1` confirmed. ✓
- **G1 n=3:** random search (200k trials) over ≤ 3-split refinements of `{8,4,2,1}/15`: min `D = 1` (units of 1/15) = 1/15 actual, at equal-halving and elsewhere. Target confirmed. ✓
- **n=2 upper-bound menu:** `min(p_3, |2p_1−1|, |p_1−p_2|, |p_2−p_3|, |p_1−p_3|)` over 50k random Liu configs: worst `0.1420 ≤ 1/7 = 0.1429`, 0 configs exceed. Worst config ≈ dyadic `(0.573, 0.285, 0.142)`. ✓ The n=2 upper bound IS closeable by finite regime casework this round.
- **n=3 fixed menu INSUFFICIENT:** the same 1–2-mark menu over 100k n=3 configs: worst `0.097 > 1/15 = 0.0667`, 2875 configs exceed. Confirms the fixed menu fails for n ≥ 3 (matches explorer + outliner). ✓
- **Peeling lemma:** `D_final = D_rest` when Xiang splits `p_1 → p_j + (p_1−p_j)` (the original `p_j` stays, the new fragment equals `p_j`, pair contributes +2 to `j` on `[0,p_j)`, even, parity-unchanged). Verified on 20k random configs, max error `0`. ✓ (My first pass had a book-keeping bug — the original `p_j` is NOT removed; after fixing, the lemma is exact.)

## Verdicts

### dyadic-induction — CHANGES REQUESTED

**Technique:** convexity of order statistics (Route A) + parity-integral add/subtract (Route B) + n=2 two-mark finite casework. The LOWER bound is the target this round; G2 (upper) is conceded (peeling-on-n dead — piece count does not close; confirmed by diversity explorer opening E). Honest concession.

**Sound:** the greedy lemma (certified), parity-integral, recursion identity, n=1 both bounds, n=2 0-1 mark cases — all proved. Route B (parity-integral with the full `+1` on `[0,α]` AND `−1` on `[p−α,p]` decomposition) is concrete and computational — the add/subtract structure is the right handle, and `j(t)`-additivity genuinely defeats the sorted-order interleaving obstacle (the obstacle was an artifact of the sorted picture, not the `j` picture). The n=2 two-mark base case is cheap and verified true (min `D = 1` exactly). Promoting `lemmas/splits-inequality.md` is the correct goal — it closes G1 for ALL approaches.

**Gap — the convexity-of-order-statistics route has a rigor hole in its feasible-set claim.** The outliner step 1 asserts "the achievable-refinement polytope is convex." It is NOT. The set of multisets achievable with ≤ n cuts (≤ 2n+1 nonzero pieces) is non-convex: the multiset-average of two ≤ n-cut refinements can land outside the set (I constructed a concrete counterexample: average of `{4,2,1}` and `{3.5,0.5,2,1}` gives `{3.75,1.25,1.5,0.5}` which is NOT a refinement of `{4,2,1}` — no grouping sums to 4). Worse, over the LARGER convex set of all refinements (no cut-count limit), the global min of `S_odd` is 0 (Xiang splits everything into equal pairs), not `1/D_n` — so "convex + local-min ⟹ global min" does NOT apply to the ≤ n-cuts set, and the cut-count constraint is load-bearing.

**Fixable.** The builder must either (a) restrict the convexity argument to the SINGLE convex face "exactly one cut per piece `2^k` for `k=1,…,n`, piece 1 unsplit" (a product of 1-simplices, genuinely convex) where equal-halving is a local min ⟹ global min ON THAT FACE, then handle all OTHER faces (0 cuts; cuts on piece 1; multiple cuts on one piece with 0 elsewhere) by separate boundary/cross-face checks — the even-rank-insertion sub-lemma + its generalization to multi-cut are the tools; OR (b) lead with Route B (parity-integral add/subtract, the concrete finite verification) as the primary engine and use convexity only as a sanity check. Route B is sound and should be the load-bearing argument; the "convex feasible set" framing as stated is wrong and must not be invoked as-is.

Also: the outliner step 3 boundary directional-derivative check must cover the multi-cut-on-one-piece boundary (2 cuts on `2^n`, 0 on `2^{n−1}`), not just "split piece 1." The even-rank-insertion sub-lemma handles "split largest once, rest unsplit"; the multi-cut case needs the same parity-integral add/subtract tracking.

**Verdict: CHANGES REQUESTED.** The technique is right (convexity of order statistics is a real fact; parity-integral Route B is sound), the n=2 base is cheap and true, and certifying `splits-inequality.md` closes G1 for the whole field. But the convexity step's "feasible set is convex" premise is false as stated — the builder must restrict to the one-cut-per-piece face + cross-face checks, or lead with Route B. Do NOT invoke "convex + local min ⟹ global min" on the non-convex ≤ n-cuts set.

### pairing-charging — APPROVE

**Technique:** parity-XOR toggle framework + peeling lemma (the additivity anchor) + direct combinatorial domino/antipodal partition. The DIRECT PARTITION route — distinct from alternating-potential's amortized potential and from minimax-strategy-family's regime enumeration.

**Sound:** the parity-XOR toggle lemma (split `p` into `u≥v` toggles parity on `[0,v) ∪ [u,p)`) and the peeling lemma (`D_final = D_rest` exactly when a split creates an equal pair — I verified this, error 0 on 20k configs) are both correct and concrete. The n=2 finite casework (step 3) is verified closeable (menu worst 0.142 ≤ 1/7, 0 configs exceed). The tight-at-dyadic requirement (zero slack) is correctly enforced.

**Gaps (honestly flagged by the outliner):**
- **Step 4 (G2-general, the defining bet):** the explicit domino partition for ARBITRARY Liu marks — `D_1,…,D_k` (domino intervals), antipodal Xiang marks, per-domino deficits `δ_k`, and `Σ δ_k + residual = 1/D_n` EXACTLY. This is the approach's defining crux and is still a BET (no closed-form construction for general marks, as the round-1 approach file honestly admitted). The outliner adds the parity-XOR framework and peeling lemma as concrete tools, which is real progress, but the construction itself is not specified. The builder must either find the construction or honestly report it as still open after this round.
- **Step 5 (strengthened derived-rest hypothesis):** the naive "any (n−1)-piece rest has `D ≤ 1/D_{n−1}`" is too weak (gives `(1−2p_{n+1})/D_{n−1}`, loose at dyadic n=3: 1/3 ≫ 1/15). The rest is derived (largest piece `p_1−p_j`, inheriting Liu's structure). This gap is SHARED with alternating-potential (see below).

**Diversity check:** the direct-partition framing (step 4) is genuinely distinct from the alternatives. But step 5 (peeling-induction with strengthened hypothesis) overlaps with alternating-potential step 4 — if both fall back to peeling-induction and the shared hypothesis is wrong, both die together. The builder should prioritize the PRIMARY crux (step 4, direct partition) over the shared peeling-induction (step 5).

**Verdict: APPROVE.** Strongest upper-bound route; empirically-correct mechanism (pairing); concrete tools (parity-XOR, peeling) and a closeable n=2 milestone. The G2-general construction is a bet, but it is the approach's defining bet and the tools are sound.

### alternating-potential — CHANGES REQUESTED

**Technique:** amortized-potential / linear-invariant on the parity-XOR framework (crux aimo-0019 hint), pivoting AWAY from the confirmed-dead direct-D-cap (factor-of-2 telescope). The lower-bound half (even-rank-insertion sub-lemma + shared G1) is KEPT.

**Sound (kept):** the D-reformulation, even-rank-insertion sub-lemma (proved, verified 100k trials), `D_init` computed, equal-split attainment, n=1 both bounds — all solid. The lower-bound contribution is real and reusable.

**Gap — the pivoted upper-bound crux (step 3) is under-specified and risks the same factor-of-2 wall.** The outliner defines `Φ = D − α·M` with "candidate: `M = Σ (splits used)·2^{−k}`" — a weighted split count. But:
1. At peeling splits, `D_final = D_rest` exactly (D-neutral), so the potential is ALSO neutral there — no progress to charge. The peeling-anchored induction (step 4) then gives `D_final = D_rest ≤ (1−2p_j)/D_{n−1}` — the SAME loose bound as round 1.
2. At NON-peeling splits, the potential's non-increase requires `ΔD ≤ α·ΔM`, i.e. a dyadic-decrement schedule — which is exactly the factor-of-2 wall the diversity explorer confirmed dead (opening C: "Measure / parity-integral control — DEAD (same wall)"). A linear potential `Φ = D − α·M` with `M` a linear function of split-progress collapses into the dead direct-D-cap.

The outliner claims the amortized potential is distinct from the direct-D-cap because it "wraps around" the peeling structure. But the peeling structure is D-neutral (no charge), and the non-peeling splits hit the factor-2 wall. The potential does not obviously escape the wall unless `M` captures something BEYOND linear split-progress — and the outliner does not specify what.

**Shared gap (step 4):** the strengthened derived-rest hypothesis is shared with pairing-charging step 5. If the primary crux (step 3) fails and both fall back to peeling-induction, the shared hypothesis is the single point of failure for both — the single-gap trap the dispatch warns about.

**Fixable direction:** the builder must either (a) find a SPECIFIC, non-trivial potential `Φ` (not a linear function of split count) that provably beats the factor-2 wall — e.g. a potential that charges against the PAIRING STRUCTURE implicitly, or a potential defined on the parity-profile `j(t)` rather than on `D` directly; or (b) concede the upper bound to pairing-charging / minimax-strategy-family and consolidate the approach's contribution to the lower-bound half (even-rank-insertion + shared G1). The outliner's watch-out (a) correctly warns to keep distinct from pairing-charging — if the potential collapses into "exhibit a pairing," it has merged and lost its value.

**Verdict: CHANGES REQUESTED.** The pivot direction is reasonable (the direct-D-cap IS dead and must not be retried), but the new crux (step 3) is a "candidate" `M`, not a defined potential, and risks collapsing into the same factor-2 wall. The builder must specify a concrete non-trivial potential or concede the upper bound. The lower-bound contribution is solid and worth keeping the approach alive. Flag the shared strengthened-hypothesis (step 4) as a single-point-of-failure risk with pairing-charging.

### minimax-strategy-family — APPROVE (new slug, register)

**Technique:** minimax over a finite family of explicit Xiang strategies + regime casework (crux aimo-0198 hint: `min(A,B) ≤ (A+B)/2` crossover, generalized to a family). The genuinely-different upper-bound framing — far from pairing-charging's direct partition and alternating-potential's potential.

**Sound:** the n=1 template (`min(1−p_1, 2p_1−1) ≤ 1/3` at crossover `p_1 = 2/3`) is clean and proved. The n=2 milestone (full 6-member family: 3 choices of barely-split piece × 2 choices of equal-halve piece, plus the all-equal-halve member) is verified closeable — I confirmed the menu suffices (worst 0.142 ≤ 1/7, 0 configs exceed, worst config ≈ dyadic). The barely-split branch (`D = |p_i − p_{i'}|`, a DIFFERENCE of two Liu pieces) is genuinely non-pairing and ties with pairing at the dyadic config — exactly what a minimax-over-family proof needs.

**Gaps (honestly flagged):**
- **Step 2 (per-strategy regime guard — CONJECTURE):** each barely-split strategy's `D`-formula holds in a stated regime; outside, the value only DECREASES. Probed on 20k n=2 configs (holds). Needs proof. If it fails, the regime tree does not collapse and the approach gets complicated.
- **Step 4 (unique-worst-at-dyadic — CONJECTURE):** the dyadic config is the unique maximizer of `min_S D(S, Liu)`. Strong numerics for n=2. Needs proof for general n.
- **Step 5 (n ≥ 3 family enumeration — the real crux):** a fixed 1–2-mark menu is VERIFIED insufficient for n ≥ 3 (I confirmed: worst 0.097 > 1/15, 2875 configs exceed). The family must use "the full n-mark adaptive refinement." The outliner honestly warns this risks collapsing into "construct the optimal Xiang strategy" (= the original problem, no simplification). The LP-dual-within-regime (framing B) is a possible rigor handle per regime if the combinatorial tree stalls.

**Diversity check:** the minimax-over-family framing is genuinely distinct from pairing-charging (single direct partition) and alternating-potential (single potential). Pairing is ONE family member, not the whole family. The builder must keep the family-based minimax framing distinct — watch-out (c) correctly warns against collapsing into pairing. The n=3 crux (step 5) is the main risk: if the family must be infinitely rich to cap n ≥ 3, the approach stalls. But the n=2 milestone is a concrete, closeable advance, and the framing is the only genuinely-different upper-bound line that survived probing.

**Verdict: APPROVE.** Genuinely-different framing; verified closeable n=2 milestone; clean n=1 template. The n ≥ 3 crux is honestly flagged. Register the new slug (re-plan of the dead surrogate-adversary).

### surrogate-adversary — DEAD (no action)

Already in the population as `dead-end` (round 1 RETHINK). The falsification sweep (all non-pairing restricted strategies fail for n ≥ 2) stands. The re-plan into minimax-strategy-family (new slug) is the correct resolution. Do NOT revive the old slug; leave it as a dead record. Do not register.

## Shared-gap / diversity assessment (for the orchestrator)

**The single-gap trap (flagged by the dispatch):** pairing-charging step 5 and alternating-potential step 4 BOTH lean on the "strengthened derived-rest hypothesis" (the rest after a peeling split is not arbitrary — its largest piece is `p_1−p_j`, inheriting Liu's structure). If this hypothesis is wrong, BOTH approaches die on the upper bound when they fall back to peeling-induction. MITIGATION: each has a PRIMARY crux that does NOT use peeling-induction (pairing-charging step 4 = direct partition; alternating-potential step 3 = amortized potential). The builder should prioritize the primary crux; the shared peeling-induction is the fallback, not the engine. If BOTH primary cruxes fail next round, the field should seed a genuinely different framing (LP-duality, measure-concentration) per the round-1 reviewer rule.

**Field diversity is GOOD this round.** The three upper-bound framings are genuinely distinct: direct combinatorial partition (pairing-charging), amortized linear potential (alternating-potential), minimax over explicit-strategy family with regime casework (minimax-strategy-family). The lower bound is consolidated (dyadic-induction closes G1, certifies `splits-inequality.md` for all). No two approaches are the same proof divided into pieces.

**Caveat on alternating-potential:** if its step 3 potential collapses into a linear decrement schedule (the factor-2 wall), it effectively dies and the upper-bound field narrows to pairing-charging + minimax-strategy-family. The builder must report honestly if this happens.

## Ranking (K=32, soft floor 1000)

Anchored to round-1 outcomes + round-2 terrain:
- pairing-charging (1546, advanced) stays the leader: it targets G2 (the real IMO wall) with the empirically-correct pairing mechanism, has concrete tools (parity-XOR, peeling), and a closeable n=2 milestone. The G2-general construction (step 4) is a bet but the approach is alive on both bounds.
- dyadic-induction (1517, advanced) rises: it can CLOSE G1 this round (convexity Route A fixable, Route B sound, n=2 base cheap) and certify `splits-inequality.md` — a shared advance for the whole field. But its own G2 is conceded (peeling dead), so it cannot solve the whole problem alone this round. Stays behind pairing-charging.
- minimax-strategy-family (cold-start 1500, new) enters strong: genuinely-different framing, closeable n=2 upper-bound milestone, clean n=1 template. Ranks above alternating-potential (fresh viable line vs a pivoting-from-dead line) but below the two established leaders.
- alternating-potential (1485, partial) stays low: the direct-D-cap is dead (do not retry), the pivoted amortized-potential crux is under-specified and risks the same factor-2 wall. The lower-bound contribution keeps it alive but the upper-bound half is the weakest in the field.
- surrogate-adversary (1452, dead-end) is the floor: dead, re-slugged into minimax-strategy-family. Loses to everyone.

## build set: dyadic-induction, pairing-charging, alternating-potential, minimax-strategy-family
