# Round-4 outline-reviewer — imo-2026-03 (Chu-Han war)

Reviewed the outliner's 5-approach field (`/tmp/round-4/proof-outliner.md`) against the problem, prior progress, certified lemmas, three round-4 explorer reports, and the per-role rules. Ran small-case numerics to sanity-check the load-bearing claims BEFORE clearing builders to spend effort. Two claims collapsed under numeric scrutiny — flagged below.

## Per-approach gate verdicts

### 1. dyadic-induction (REVISE) — APPROVE
Target: G1-general (the shared lower-bound wall), via the union-measure / dyadic-tiling rigidity reframe (measure-extremizer Opening A).
- **Technique sound.** The Lemma-5 identity `D = M + D_{R_0} + D_F − 2|O_{R_0} ∪ O_F|` is verified exact (0 error, 8k trials, explorer + dyadic-induction §4.3). The union bound `|union| ≤ (M + D_{R_0} + D_F − 1)/2` is an exact algebraic restatement of the overlap crux `2C ≥ D_{R_0}+D_F+1−M` — the explorer concedes this honestly ("a reframing, not a bypass"). That is fine: the win must come from the dyadic-tiling rigidity making the "deficit ≥ 1" bookkeeping at the dyadic edges clean, NOT from a new inequality. The outline states this correctly (Watch-out line).
- **Load-bearing lemma identified with mechanism:** "O_{R_0} is a rigid alternating-dyadic tiling whose superincreasing complement blocks cannot be perfectly covered by O_F (the odd region of a ≤ n-piece partition of W); each dyadic edge 2^k leaks ≥ its superincreasing surplus." This is the genuine hard step, honestly flagged as a gap (the "deficit ≥ 1" bookkeeping). It has a stated mechanism (superincreasing-block structure of the complement). The tight Lemma-6 family is measure-zero; the outline correctly demands exact interleaving bookkeeping, not an approximate bound.
- **Cases covered:** G1-i (M > 2^{n−1}), G1-ii (M = 2^{n−1}, rest split), G1-iii (all fragments < 2^{n−1}). Disjoint and exhaustive over the multi-split non-tie sub-cases. The G1-iii reduction to G1(n−1) is plausible but the "split accounting" is hand-wavy — flagged as an open gap, acceptable.
- **Avoids dead ends:** explicitly lists the three naive bounds (sub-measure, XOR-sum, D ≥ D_{R_0}) as too loose; does not retry them.
- **Diversity:** genuinely different lens (union-measure / tiling rigidity) from alternating-potential's band-parity on the same overlap wall. Owned sub-cases (G1-i/iii) differ from alternating-potential's (G1-ii). No single-gap trap between the two G1 attackers.
- **Note:** dyadic-induction's round-3 rebuild (Cases A/B/C + splits-inequality.md PARTIAL + Lemma 5 identity + Lemma 6 tight family) was NOT reviewed by the proof-reviewer last round (run_state "Next" item 1). The orchestrator should dispatch the proof-reviewer to verify this rebuild in parallel with the builders this round. The Cases A/B/C proofs look rigorous on read-through (verified by exact-arithmetic 20k trials each); the reviewer should certify splits-inequality.md's proved portion.

### 2. pairing-charging (ADVANCE) — CHANGES REQUESTED
Target: G2-flat (n≥3, p_{n+1} > 1/D_n), the real IMO wall, via the surplus-chain telescope.
- **Technique right, but the core gap-fill has a confirmed numeric problem.** I tested the surplus-chain for n=3. The outline claims the chain `p_1 → p_2 + r_1 → p_3 + r_2` (n−1 marks) "creates copy-pairs (p_2,p_2),(p_3,p_3) that cancel in D, leaving a final lone surplus r_{n−1} whose size is forced ≤ 1/D_n." This is WRONG as stated: the chain leaves p_{n+1} (the smallest piece, untouched) in the rest. After peeling the equal pairs, the rest is {r_{n−1}, p_{n+1}}, so **D = |r_{n−1} − p_{n+1}|**, NOT r_{n−1}. My numerics (30k configs, n=3): D = r_2 fails in 18050/30000 cases. The lone surplus is NOT alone.
- The full n-mark chain (p_1 → p_2+r_1 → … → p_{n+1}+r_n, using all n marks) would pair p_{n+1} too, leaving lone r_n = 2p_1 − 1. But this requires each intermediate r_k ≥ p_{k+1} (chain executability), which fails for genuinely flat configs (p_1 < p_2+p_3). And even when executable, |2p_1−1| ≤ 1/D_n requires p_1 ≤ 2^n/D_n — not guaranteed in the flat regime. So the chain alone does not close G2-flat.
- **What to fix (for the builder):** Before attempting a proof, the builder MUST run a falsification sweep (per per-role rule): for n=3, 100k random flat-regime Liu configs (p_4 > 1/15), compute the TRUE optimal Xiang response (brute-force grid) and check whether ANY adaptive n-mark construction achieves D ≤ 1/15. If the true optimum exceeds 1/15 for some flat configs, the construction bet is dead and the approach must concede G2-flat (as alternating-potential did). If the true optimum IS ≤ 1/15 (the answer is TRUE per brute-force minimax n=1..4), the builder must identify the ACTUAL construction (not the broken surplus-chain) and derive its D-formula honestly. The n=2 upper bound (CLOSED) and Lemma 4 (CERTIFIED) stand regardless.
- **Certified imports remain valid:** greedy-alternating, parity-integral, peeling, equal-halve-n-largest, splits-inequality (partial).

### 3. minimax-strategy-family (REVISE) — CHANGES REQUESTED
Target: G2-flat via minimax over an adaptive family; also fix the M2 XOR bug.
- **M2 bug CONFIRMED.** I verified: M2's D-value is `p_1 − p_2` (20000/20000 match), NOT `p_1 − p_3` (0/20000 match). The §3.1 derivation writes `h=1` on [p_3, p_2) for the toggle `[0, p_3)`, but `[0, p_3)` has indicator 0 on [p_3, p_2) (t ≥ p_3). Correct: `f' = 0` there, giving `∫f' = p_1 − p_2`. The fix is as the outline states: `h=0` on [p_3, p_2) ⟹ `f'=0` ⟹ D = p_1 − p_2. The n=2 theorem (menu + §3.2 contradiction) stands. The builder should fix §3.1 AND reconcile §3's menu statement (which currently lists M2 as `p_1−p_3`, line 262 — internally inconsistent with §3.2's correct `p_1−p_2`).
- **n≥3 chain shares the gap with pairing-charging.** The split-to-match chain `p_1 → p_2 + r_1 → …` is IDENTICAL to pairing-charging's surplus-chain (both approaches converge to the same construction for n≥3). My numerics above apply: the chain's lone surplus is NOT alone (p_{n+1} remains), D ≠ r_{n−1}. The minimax framing's fallback member is Lemma 4 (D = p_{n+1}), but that only closes the spiky regime (already closed). In the flat regime, the chain is the only new member, and it's broken as stated.
- **CONVERGENCE RISK (critical, flagging for the orchestrator):** pairing-charging and minimax-strategy-family BOTH rely on the same split-to-match chain for n≥3 flat regime. If the chain's D-formula gap can't be closed (and my numerics suggest it can't, as stated), BOTH die on G2. This is a single-gap trap. The minimax framing is slightly more robust (min over family, not single construction) but the core gap is shared. See diversity section below.
- **Distinctiveness (n=2):** genuinely preserved — the n=2 non-pairing ties (M3 barely-split, M5 split-to-match) at dyadic are real and different from pairing-charging's 4-menu. The n=2 milestone stands.

### 4. collapse-theorem (NEW) — RETHINK
Target: G2 via Liu-side flattening / Robin-Hood minimax (no Xiang partition constructed).
- **The load-bearing flattening lemma is NUMERICALLY FALSE.** I tested it exactly for n=2 (using the proven 4-menu formula `min_Xiang D = min(p_3, |2p_1−1|, p_1−p_2, p_2−p_3)`). The claim "Robin-Hood transfer from largest to smallest does NOT increase min_Xiang D" is violated in 25293/49995 cases (~50%). The mechanism of failure is clear: `min_Xiang D = min(p_3, …)`, and flattening (transferring mass to p_3, the smallest) INCREASES p_3, which INCREASES the min when p_3 is the binding constraint. The superincrease direction is equally non-monotone (25873/47982 violations). The flattening lemma does not hold in either direction.
- **The conclusion (worst Liu = dyadic) IS true for n=2** (max min_Xiang D over 100k random = 0.142031 < 1/7 = 0.142857 at dyadic; consistent with the proved unique-worst-at-dyadic). But the flattening-monotonicity PROOF ROUTE is dead. The measure-extremizer explorer already flagged "could not verify numerically in a clean monotone form within budget"; my exact check confirms it is not monotone.
- **This is a RETHINK, not a CHANGES:** the load-bearing lemma is false as stated. The approach cannot be built via the flattening route. The outliner must either find a DIFFERENT proof of "worst Liu = dyadic" (the conclusion is true but the mechanism is wrong), or abandon this line. Per the outliner's own honest flag ("If the flattening lemma fails, the approach dies honestly — flag as high-risk, no partial credit on G2"), I am NOT registering this approach. No builder should spend a round on the flattening lemma.
- **Do NOT register `collapse-theorem`** in the population. A doomed line stays out of the pool.

### 5. alternating-potential (ADVANCE) — APPROVE (cross-check role)
Target: G1-ii (split-rest sub-case) via band-parity t-axis decomposition; G2 upper bound CONCEDED (sound).
- **Technique sound but explicitly a re-lensing.** The telescoping-potential explorer concedes (Opening C): "the multi-split fragmentation reduces EXACTLY to the shared overlap-bound gap `2C ≥ D_{R_0}+D_F+1−M` (Lemma 5) — it is a re-lensing, not a bypass." The outline states this honestly. The value is cleaner bookkeeping for the G1-ii (split-rest) sub-case specifically, where the band-parity survival may be cleaner than the XOR-overlap form.
- **No wrong technique, no circular reasoning.** The band-parity decomposition `D_init = (1/D_n)·Σ_{k odd} 2^{k−1} ≥ 1/D_n` is a valid cheap kill for Case A (verified n=1..5). The G1-ii band handle uses the proved even-rank-insertion sub-lemma (round 1). The G2 concession is the right call (factor-of-2 wall, confirmed dead for linear potentials per per-role rule).
- **Diversity:** genuinely different lens (band-parity / t-axis) from dyadic-induction's XOR-overlap / tiling. Owned sub-case (G1-ii) differs from dyadic-induction's (G1-i/iii). Low-risk cross-check role; certified machinery (peeling corollary, even-rank-insertion) already in the bank.
- **Caveat for the builder:** do NOT over-invest here — this is a cross-check on one sub-case, not a primary wall-cracker. If the band-parity G1-ii proof reduces cleanly to the overlap bound (as the explorer concedes), record it as alternative bookkeeping and move on; do not chase a bypass that the explorer confirmed doesn't exist.

## Diversity check (critical)

**G1 (lower bound):** two lenses on the same overlap wall — dyadic-induction (XOR-overlap / dyadic-tiling rigidity, owns G1-i/iii) and alternating-potential (band-parity t-axis, owns G1-ii). Genuinely different framings on different sub-cases. No single-gap trap. Acceptable.

**G2 (upper bound):** the field is at RISK of collapsing. Of the three G2 attacks:
- **pairing-charging** (surplus-chain telescope) and **minimax-strategy-family** (minimax over adaptive family incl. the SAME split-to-match chain) BOTH rely on the identical chain construction for n≥3 flat regime. My numerics show the chain's core claim (D = r_{n−1}) is false (p_{n+1} is left unpaired). If the chain can't be fixed, BOTH die on G2. This is a single-gap trap between the two strongest G2 routes.
- **collapse-theorem** (the ONLY genuinely orthogonal G2 route — Liu-side, no Xiang partition) is RETHINK'd: its load-bearing flattening lemma is numerically false.
- **All three fresh round-4 explorer angles failed to crack G2-flat:** LP-duality (inherent integrality gap V_blind = 1/6 > 1/7 for n=2, structural info gap), telescoping-potential (no nonlinear invariant escapes the factor-of-2 wall without collapsing to pairing), measure-extremizer (flattening lemma false, confirmed here).

**Recommendation for the orchestrator (next round):** the G2 wall is deep — three independent explorer angles all confirmed it is real (not a technique gap). The field's only live G2 routes are Xiang-side adaptive constructions, and they share a single gap (the chain). If pairing-charging and minimax both stall on the chain for this round, the orchestrator should seed a genuinely different G2 framing next round (e.g. a direct inductive construction on the (n−1)-game with a strengthened hypothesis, or a structural characterization of the true optimal Xiang reply for n=3 via exhaustive computation → pattern extraction). Do NOT seed another pairing variant.

## Registered new approaches

None. The only NEW approach (`collapse-theorem`) is RETHINK'd — its load-bearing flattening lemma is numerically false (50% violations, exact n=2). A doomed line stays out of the pool. No copies requested by the outliner this round.

## Pairwise comparisons fed to `update_ranking`

Anchored to each approach's last recorded outcome (round-3 outcomes already in the ranking; round-4 outline-review adds the field-level head-to-head):

1. pairing-charging > minimax-strategy-family (advanced + n=2 CLOSED + Lemma 4 CERTIFIED vs partial + M2 bug + n≥3 open)
2. pairing-charging > alternating-potential (advanced, live on G2 vs partial, upper conceded)
3. pairing-charging > surrogate-adversary (alive vs dead-end)
4. dyadic-induction > minimax-strategy-family (advanced G1: Cases A/B/C + Lemma 5 identity + tight family vs partial G2 only)
5. dyadic-induction > alternating-potential (G1 structural progress vs conceded upper, machinery-only)
6. dyadic-induction > surrogate-adversary (alive vs dead-end)
7. minimax-strategy-family > alternating-potential (n=2 upper proved [with bug] + live G2 vs upper conceded)
8. minimax-strategy-family > surrogate-adversary (alive vs dead-end)
9. alternating-potential > surrogate-adversary (partial-alive vs dead-end)
10. pairing-charging vs dyadic-induction — DRAW (both advanced; pairing has certified round-3 outcomes [n=2 closed, Lemma 4 certified]; dyadic-induction has more G1 structural progress [Cases A/B/C, Lemma 5, tight family] but its rebuild is pending review)

## Resulting Elo table (best-first)

| Rank | Slug | Elo | Last outcome | Notes |
|------|------|-----|--------------|-------|
| 1 | pairing-charging | 1618 | advanced | n=2 upper CLOSED; Lemma 4 CERTIFIED; G2-flat open (chain gap confirmed). Strongest upper route. |
| 2 | dyadic-induction | 1582 | advanced | G1 Cases A/B/C + Lemma 5 + tight family PROVED; multi-split overlap bound open. Most rigorous G1 route; rebuild pending review. |
| 3 | minimax-strategy-family | 1501 | partial | n=2 upper TRUE (M2 derivation buggy, fix confirmed); n≥3 chain shares gap with pairing-charging. |
| 4 | alternating-potential | 1437 | partial | Upper CONCEDED (factor-of-2 wall, sound); lower-bound machinery CERTIFIED. Cross-check role on G1-ii. |
| 5 | surrogate-adversary | 1362 | dead-end | Dead; do not revive. |

`collapse-theorem`: NOT registered (RETHINK'd; flattening lemma numerically false).

## Build set

Four slugs, attacking BOTH walls (2 G1, 2 G2). Mix of revise/advance; no new approaches (collapse-theorem RETHINK'd).

- **dyadic-induction** (G1 primary): advance the tiling-rigidity "deficit ≥ 1" bookkeeping for the overlap bound (G1-i/ii/iii); verify G1-iii reduction to G1(n−1). Anti-stuck: write proof prose first; bound Python (≤10k trials, grid ≤200, each script <30s); emit output early. Do NOT retry the three naive bounds.
- **alternating-potential** (G1 cross-check): advance the band-parity G1-ii (split-rest) survival as alternative bookkeeping; record as cross-check to dyadic-induction's tiling. Do NOT chase a bypass the explorer confirmed doesn't exist. Concede G2 (already sound).
- **pairing-charging** (G2 primary): re-verify the surplus-chain for n=3 FIRST (falsification sweep: 100k flat-regime configs, true optimal Xiang via grid — does ANY adaptive n-mark construction achieve D ≤ 1/15?). If the chain is broken (my numerics suggest D = |r_{n−1} − p_{n+1}|, not r_{n−1}), identify the ACTUAL construction or honestly concede G2-flat. The n=2 upper bound stands.
- **minimax-strategy-family** (G2 secondary): fix the M2 XOR derivation (confirmed: correct value p_1−p_2; reconcile §3.1 derivation + §3 menu statement [line 262 lists M2 as p_1−p_3, inconsistent with §3.2] + §3.2 table). Then address the n≥3 chain's D-formula honestly (shared gap with pairing-charging).

build set: dyadic-induction, alternating-potential, pairing-charging, minimax-strategy-family
