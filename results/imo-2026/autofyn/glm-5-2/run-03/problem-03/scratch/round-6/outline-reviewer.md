# Round-6 outline-reviewer report — imo-2026-03 (Chu-Han war)

Reviewed the round-6 outliner field (pairing-charging ADVANCE, dyadic-induction ADVANCE, parity-xor-reachability NEW; lp-dual-region / alternating-potential / minimax KEEP). Read CLAUDE.md, run_state.md, current.md, all approach files, the certified lemmas, the 3 round-6 explorer reports, and round-5 outline-reviewer + proof-reviewer. Ran independent Python (`fractions` exact) verification of every load-bearing numerical claim. Verdicts below.

---

## Independent verification performed (Python `fractions`, all scripts <30s)

1. **f_n conjecture at n=4** (pairing-charging): `f4(p*) = 1/31` EXACTLY; 0 escapes / 3000 random very-flat configs; worst interior `3/124 ≈ 0.0242 < 1/31 ≈ 0.0323`. Slack `≈ ε/2–2ε` along the dyadic ray (direction-dependent; the explorer's `ε/2` is one perturbation direction). The conjecture HOLDS at n=4 numerically. ✓
2. **PWL / max-at-vertex principle**: sound for ANY piecewise-linear function on a polytope (max at a cell vertex of the arrangement, not just polytope vertices — the Bauer convex-max principle is a special case; the general PWL result holds regardless of concavity). f4 = min over 10 peels × recursive f3(min of f2(min of 4 PWL members)) is PWL. ✓
3. **G1-iii-a peeling recursion**: FALSIFIED. For the n=4 tight config `F' = {7.5, 4.5, 2, 1, 0.5, 0.5}` (M=8, floor={4,2,1}): the claimed `D = Σε_i + D_alt(floor)` gives `32 + 3 = 35`, but actual `D = 1`. The recursion does NOT iterate — only ONE peel is valid (`D = ε_1 + D_alt(R'')` holds because M is the top-level dominant; the second peel would need M in R'', but M is gone). See §2 below.
4. **"iii-a is EASIER / growing slack" premise**: FALSIFIED. I found a TIGHT `D = 1` config at n=5: `F' = {15.5, 7.5, 4, 2, 1, 0.5, 0.5, 0.5, 0.5}` (M=16, floor={8,4,2,1}, sum=32, all<16), giving `D_R = 15 = M−1`, `D = 1`. The explorer's "n=5≈3.08, n=6≈4.22" are coarse-grid underestimates that missed the tight configs. iii-a is TIGHT (`D=1`) at both n=4 and n=5 (and almost certainly all n≥4), NOT "easier with growing slack."
5. **D_alt(floor) formula**: the explorer/outliner's `D_alt(floor {1,2,4,…,2^{n−2}}) = (2^{n−1}+(−1)^{n−2})/3` is CORRECT (n=4→3, n=5→5, n=6→11) — the floor is the DYADIC-POWER set `{1,2,4,…,2^{n−2}}`, not consecutive integers. ✓
6. **parity-xor-reachability f-band structure**: VERIFIED n=1..6. `f = [j_Liu odd]` has bands of superincreasing-DISTINCT lengths (n=4: {1,2,8}; n=5: {1,4,16}; n=6: {1,2,8,32}; each > sum of all smaller, the dyadic identity `2^k > 2^k−1`). ✓
7. **Tight equal-halving case**: VERIFIED. Equal-halving the n largest pieces gives toggles `h = XOR_{k=1}^n 1_{[0, 2^k)}`; `f ⊕ h = 1_{(0,1]}` (the smallest band, length `1/D_n`), so `D = 1/D_n` EXACTLY. The obstruction's boundary case is reproduced. ✓
8. **"Single toggle covers at most one band of f perfectly" lemma**: SOUND. A toggle's two intervals have EQUAL length; f's bands have DISTINCT lengths; so at most one interval per toggle can perfectly match a band. ✓

---

## 1. pairing-charging — ADVANCE (n=4 very-flat vertex enumeration)

**Verdict: APPROVE.**

The vertex-enumeration route is sound and tractable:

- **PWL structure** (step 2): f4 = min over 10 peels of f3(rest), each f3 = min over 6 peels of f2, f2 = min(c, |a−b−c|, a−b, b−c) — all PWL in p (the |a−b−c| is V-shaped PWL, the rest linear; min of PWL is PWL). The composition is PWL on the sort-regime arrangement of the 5 pieces. ✓
- **Max-at-vertex** (step 2, Bauer): the max of a PWL function on a compact polytope is attained at a vertex of the cell complex (intersection of arrangement hyperplanes within the polytope, or a polytope vertex). This holds for ANY PWL function (concave, convex, or neither) — on each linear cell, the max is at a cell vertex; the global max is the max over cells. The outliner's invocation is correct (the Bauer convex-max principle is the special case; the general PWL result is what's needed and it holds). ✓
- **Vertex count** (step 3): the top-level arrangement (4 sort-order hyperplanes + 4 boundary hyperplanes in 4D) gives ~C(8,4)=70 base vertices. The recursive peel-then-menu structure induces additional breakpoints (sort-regimes of each peel's rest + menu-active switches), raising H to perhaps 20–80 hyperplanes. C(H,4) could reach 10⁴–10⁵ before feasibility pruning, but the FEASIBLE vertices within Π_4^{cl} are far fewer (most intersections lie outside the polytope or violate sort order). The explorer's "~10²–10³" estimate is optimistic but the anti-stuck fallback (≤30s, ≤10k vertices, emit early, 5-subcase gap table fallback) covers the explosion risk. ✓ tractable.
- **Open-polytope handling** (step 5): Π_4 is open (strict inequalities); the supremum is at the dyadic boundary vertex p* (on the Lemma-5 / Lemma-4 facets, both already proved). This is the SAME pattern certified in round-5 n=3 Theorem 6. ✓
- **f4 ≤ 1/31 verified** (independent): tight at p* exactly, 0 escapes on 3000 random + near-dyadic ray. ✓
- **Cross-piece-equal-pair cheap-kill pre-pass** (watch-out): sound — check whether n=4 worst configs satisfy `p_k = p_i + p_j` (if so, D=0 via the certified lemma, far below 1/31).

**Gaps the builder must close:**
- The n=4 vertex enumeration TABLE (finite, exact-rational, script-verified). Bound the script: ≤30s, ≤10k vertices, emit output early. If the count exceeds budget, FALL BACK to the explorer's 5-subcase gap table (one sub-case per binding peel, `min(a−b,b−c)≤(a−c)/2` absorption, 5-gap box arithmetic) — heavier but maybe hand-checkable.
- State the open-polytope strict-interior handling EXPLICITLY (as in round-5 Theorem 6): interior `f4 < 1/31` strictly; supremum `1/31` at p* on proved facets.
- Do NOT present `f_n` as proved. The n=4 enumeration closes n=4 as a MILESTONE; the uniform-in-n induction (needs a NEW invariant beyond `min(a−b,b−c)≤(a−c)/2` — the sort-independent-member lift breaks at n=4, per the explorer) remains a CONJECTURE (verified n=3,4; n≥5 open).
- Handle "fewer than 4 Liu marks" directly (equal-halve all ≤4 pieces ⇒ D=0 ≤ 1/31).

**Anti-stuck guidance for the builder:** write the proof PROSE FIRST (the PWL/max-at-vertex argument + the open-polytope handling, citing KB *Piecewise-concavity smoothing*), THEN run the enumeration script as VERIFICATION (not as the proof's engine — the proof's engine is the PWL principle; the table is the casework). Bound all Python: ≤10k trials, grid ≤200, each script <30s, emit early. Never assume "obvious." If the vertex count explodes past 10k, switch to the 5-subcase gap-table fallback and flag the enumeration as supplementary verification.

---

## 2. dyadic-induction — ADVANCE (G1-i-HC exchange + G1-iii-a peeling)

**Verdict: CHANGES REQUESTED.** The G1-i-HC exchange/convexity argument is sound and is the headline lower-bound crux; but the G1-iii-a peeling recursion is a THIRD FAILED MECHANISM, and the "iii-a is EASIER / growing slack" premise is NUMERICALLY FALSE.

### G1-i-HC exchange/convexity (steps 1–5): SOUND, proceed

- **Technique right**: the superincreasing-prefix obstruction (crux aimo-0530 adapted) is a genuine engine — `E_{R_0}`'s bands have superincreasing swing amplitudes (Lemma 10, certified), so the largest-band alignment is forced. The dyadic-scale-bracketing contradiction (aimo-0493) is a sound adaptation hint. The tight case (tower-prefix F = {2^{n−2}, 2^{n−3}, …}, breakpoints at G's alternating-sign extrema, tight iff s=n−1) is VERIFIED (n=4 s=3 tight F={4,2,1}; n=5 s=4 tight F={8,4,2,1}; slack at s<n−1). ✓
- **Exchange step (step 3) plausible**: moving a breakpoint off a G-extremum into a band interior changes `G(f_i)` at rate ±1/2 (slope of G within a band); the alternating-sign structure of `Alt_s` means the sign is such that `Alt_s` INCREASES (the extremum was a min of G at an odd-index breakpoint, or a max at even-index). The mechanism is valid in principle.
- **Hard step flagged (step 4, W-sum coupling)**: moving one breakpoint requires adjusting others to preserve `Σ f_i = W`; the superincreasing surplus (largest swing > sum of all smaller) must dominate the coupling. This is the OPEN crux — correctly identified, the builder must make it rigorous. The crux templates are ADAPTATION HINTS, not citations.

### G1-iii-a peeling recursion (steps 6–9): UNSOUND — do NOT pursue

- **The peeling recursion `D = Σε_i + D_final` does NOT iterate.** I verified on the n=4 tight config: `D = ε_1 + D_alt(R'')` holds for ONE peel (because M is the top-level dominant piece, `D = M − D_R` is the identity, and peeling the largest fragment `M−ε_1` gives `D = ε_1 + D_alt(floor ∪ (F'\{largest}))`). But the SECOND peel would need `D_alt(R'') = ε_2 + D_alt(R''')`, which requires M to be the dominant of R'' — but M is GONE from R'' (it was the top-level piece, not in the rest). The recursion does NOT telescope. For the n=4 tight config, the claimed `Σε_i + D_alt(floor) = 32 + 3 = 35`, but actual `D = 1`. **The mechanism is wrong by 35×.** This is the THIRD failed iii-a mechanism (after peeling-pair [round 5, unsound — needs exactly equal pairs] and continuity [round 5, provenance switches]).
- **The "iii-a EASIER / growing slack" premise is FALSE.** The explorer's sweep reported "n=4 min D≈1.24, n=5≈3.08, n=6≈4.22" on a coarse grid. I found the TIGHT `D = 1` config at n=5 (`F' = {15.5, 7.5, 4, 2, 1, 0.5, 0.5, 0.5, 0.5}`, verified: `D_R = 15 = M−1`, `D = 1`). The coarse grid missed the tight configs. iii-a is TIGHT (`D=1`) at both n=4 and n=5 (and almost certainly all n≥4 by the same interleaving construction), NOT "easier with growing slack." The outliner's headline rationale for prioritizing iii-a this round ("iii-a is EASIER — confirmed by my sweep") is based on a numerically FALSE claim.
- **The budget-case reduction (step 9)** — "when r is large, the floor needs splits, bound the residual via G1-i-HC at n−1" — is HAND-WAVING. It concedes the peeling recursion doesn't close the large-r case, and the reduction to G1-i-HC at n−1 is unverified (the rest structure differs). This is not a mechanism, it's a deferred gap.

**What the builder should do:**
1. **PURSUE G1-i-HC exchange/convexity** (steps 1–5) — the sound, headline lower-bound crux. Make the W-sum coupling rigorous (the superincreasing surplus dominates the coupling adjustment). Verify the exchange on n=4 s=3, n=5 s=4 tight families (the sliver witness at n=4 s=3 is the exact tight case).
2. **DO NOT pursue the iii-a peeling recursion** — it is the third failed mechanism. Mark G1-iii-a OPEN (bound `D ≥ 1` is TRUE, verified tight at n=4,5; needs a FOURTH mechanism — candidates: direct parity-integral `D = M − D_R` with `D_R ≤ M−1` via the F_2-obstruction sibling, or a direct overlap bound on the floor ∪ F' interleaving).
3. **DO NOT rely on "iii-a easier / growing slack"** — numerically false (tight D=1 at n=4,5). iii-a is as hard as G1-i-HC, not easier.
4. **G1-iii-b** (flat twin, rest's 2^{n−1} SPLIT): flag OPEN (do not attempt this round — it needs the same machinery as iii-a or the parity-xor sibling).
5. **splits-inequality.md stays PARTIAL** — add the exchange argument for G1-i-HC as a proved component if the W-sum coupling closes; do NOT upgrade to FULL (iii-a, iii-b, G1-ii rest-split all open).

**Anti-stuck guidance:** write proof PROSE FIRST for the exchange argument (state the superincreasing-prefix obstruction, the exchange step, the W-sum coupling lemma with its mechanism — the superincreasing surplus dominates). Verify the tight case arithmetic at the tower-prefix EXACTLY (each `ε_i` contributes `±ε_i/2` to `Alt_s` and `−ε_1/2` to target, summing to equality via `Σε=1` — verified n=2..6). Bound all Python ≤10k trials / grid ≤200 / each script <30s / emit early. Never assume "obvious." If the W-sum coupling can't be closed in one round, HONESTLY flag it (do not overclaim) — the exchange argument is the right technique even if the coupling needs another round.

---

## 3. parity-xor-reachability — NEW (F_2-representation impossibility)

**Verdict: APPROVE.** Registered (cold-start 1500). A genuinely different G1 framing with sound structural assets and a sound (if unproven) obstruction mechanism.

### Why genuinely different (not a re-lens of dyadic-induction)
- dyadic-induction attacks via `Alt_s = Σ(−1)^{i+1} G(f_i)` — a REAL-valued alternating-discrepancy inequality at F's breakpoints against `E_{R_0}`'s bands, SPECIFIC to the G1-i-HC rest-unsplit sub-case (the Lemma-5 decomposition requires a top band `(M−U)` with `M > 2^{n−1}`).
- parity-xor-reachability attacks via `f = h in F_2` — a BOOLEAN/algebraic obstruction on `f`'s band structure and the toggle-algebra, AGNOSTIC to the rest-tiling decomposition. It applies to ALL G1 sub-cases (i, ii, iii-a, iii-b) WITHOUT re-derivation, because `f = [j_Liu odd]` and the toggle budget `≤n` are fixed by the dyadic config and the game rules, not by the sub-case.
- The two ask different questions (F_2-reachability vs measure inequality) on different objects (raw toggle-algebra vs rest-tiling decomposition). They share the certified parity-XOR toggle lemma as setup but diverge in the proof engine. ✓ genuinely different.

### Structural assets (VERIFIED)
- **f's bands have superincreasing-distinct lengths** (verified n=1..6): the dyadic config's `f = [j_Liu odd]` is 1 on every other dyadic band, with lengths {1, 2/4, 8/16, …} (e.g. n=4: {1,2,8}; n=5: {1,4,16}), each STRICTLY exceeding the sum of all smaller (the dyadic identity `2^k > 2^k−1`). ✓
- **Tight equal-halving case reproduced** (verified): equal-halving the n largest pieces gives `f ⊕ h = 1_{(0,1]}` (the smallest band, length `1/D_n`), so `D = 1/D_n` EXACTLY. The obstruction's boundary case is the tight case. ✓
- **"Single toggle covers at most one band of f perfectly" lemma** (SOUND): the toggle's two intervals have EQUAL length; f's bands have DISTINCT lengths; so at most one interval per toggle can perfectly match a band. ✓
- **Superincreasing-prefix forcing** (step 5, crux aimo-0530 adapted): the largest band `L_m > L_1+…+L_{m−1}` forces any representation to include a toggle covering it; that toggle's other interval (length `L_m`) creates a residual. SOUND in spirit (the Zeckendorf-style forcing is the right engine).

### Collapse-to-union-bound risk (step 8): the framing does NOT collapse
The Lemma-7 union-measure bound (`D = M + D_{R_0} + D_F − 2|O_{R_0} ∪ O_F|`) is a MEASURE inequality on a SPECIFIC decomposition (rest R_0 + fragments F, with M dominant). The F_2-reachability asks a BOOLEAN question (can `f` be represented as `≤n` paired-equal-length toggles?) on the RAW `f = [j_Liu odd]`, agnostic to the R_0/F decomposition. The two coincide on the G1-i-HC sub-case at the bookkeeping level (both measure the odd-residual), but the F_2 framing's UNIFORM APPLICABILITY across sub-cases (i, ii, iii-a, iii-b) is a genuine advantage the union bound lacks (the union bound needs re-derivation for each sub-case's decomposition). The framing is NOT a re-lens. ✓ The builder must still verify this at the bookkeeping level (the outliner's caveat stands as a check, not a blocker).

### Hard step flagged (the builder's job)
- **Residual quantification** (steps 5–6): the recursion "cover the largest uncovered band, creating a residual from the toggle's other interval" must terminate with an uncovered portion `≥ 1/D_n`. The residual from a toggle's other interval (length `L`) is `|other interval ∩ (f=0)| − |other interval ∩ (f=1)| = L − 2|other interval ∩ (f=1 region)|`, which is NOT obviously `≥ L − (sum of smaller bands)` — the other interval could overlap f=1 regions, REDUCING the residual. The builder must make this quantification rigorous (not heuristic). The tight case (equal-halving, other interval perfectly covers f=0 region, residual = L = the band) is the boundary; the builder must show non-tight-toggle allocations leave a LARGER residual.
- **Toggle-structure constraint** (step 6): the toggles are constrained by the dyadic piece structure (`p_k ∈ {1,2,…,2^n}/D_n`, `v_k ≤ p_k/2`). The builder must check whether this STRENGTHENS the obstruction (fewer reachable f-representations — likely, since the toggle intervals are constrained to dyadic-aligned positions) or WEAKENS it (some dyadic-aligned toggles cover bands more efficiently — the tight equal-halving case is exactly this). The dyadic-config tightness is the boundary the obstruction must reproduce.

**Anti-stuck guidance:** write proof PROSE FIRST (state the F_2-reachability question, the superincreasing-distinct band structure, the obstruction lemmas with mechanisms). Verify the n=2, n=3 cases reproduce `D ≥ 1/7, 1/15` via the F_2-obstruction (the n=2 case: 2 toggles, f-bands {1,2}, the tight case leaves the smallest band uncovered — I verified the n=2 bookkeeping by hand). Verify the tight equal-halving case is the BOUNDARY of the obstruction (D = 1/D_n exactly). Bound all Python ≤10k trials / grid ≤200 / each script <30s / emit early. Check the collapse-to-union-bound at the bookkeeping level FIRST (if it collapses, RETHINK — but my analysis says it does NOT collapse, because the F_2 framing is uniform across sub-cases while the union bound is G1-i-HC-specific). Never assume "obvious."

---

## 4. lp-dual-region — KEEP, no re-dispatch (correct)

The round-6 lp-dual explorer HONESTLY confirmed the per-region LP DUAL COLLAPSES to the finite pairwise-diff/peel/EH-n-largest family (continuous optimum at EH+EH vertices = finite-strategy points, regime-independent for all n≥2 per the certified `pairwise-diff-strategy` lemma). There is NO genuinely-continuous vertex that beats the finite family on n≥4. The `f_n` induction (pairing-charging) is NOT shortcut by the LP-dual. The cross-piece-equal-pair cheap-kill is a genuine certified contribution (already in `lemmas/`). No builder this round. ✓

## 5. alternating-potential — KEEP, no re-dispatch (correct)

Certified baseline + conditional. The G1-ii reduction becomes load-bearing once dyadic-induction closes G1-i-HC with rest-split (conditional, certified round 4). G2 upper bound CONCEDED (factor-of-2 wall dead — do not retry linear-in-D potential). No re-dispatch unless G1-i-HC with rest-split closes. ✓

## 6. minimax-strategy-family — KEEP, no re-dispatch (correct)

n=2-certified baseline + lemma donor (`pairwise-diff-strategy`, certified). G2-flat n≥3 finite-family framing CONCEDED. Do NOT re-dispatch finite families for n≥3. ✓

---

## Diversity assessment

The field has NOT collapsed. On G1, two genuinely different framings (dyadic-induction = alternating-discrepancy / exchange; parity-xor-reachability = F_2-reachability / superincreasing-band obstruction) attack the same wall via different engines (REAL-valued inequality vs BOOLEAN/algebraic obstruction), on different objects (rest-tiling decomposition vs raw toggle-algebra). On G2, pairing-charging advances the n=4 milestone via vertex enumeration (the only live G2 attacker; lp-dual-region collapsed, amortized dyadic-frontier deemed too risky — factor-of-2 wall persists in cheap-kill checks). The G2 side is thin (one live attacker) — if pairing-charging's n=4 enumeration and the `f_n` induction both stall, the outliner should seed a genuinely-different G2 framing next round (the amortized dyadic-frontier is the only candidate on the table, despite its risks; or a fresh reduction).

---

## Ranking (round-6, after update_ranking)

| rank | slug | Elo | last outcome | verdict this round |
|---|---|---|---|---|
| 1 | pairing-charging | 1706 | verified-milestone (r5) | APPROVE (n=4 vertex enumeration) |
| 2 | dyadic-induction | 1605 | advanced (r5) | CHANGES REQUESTED (G1-i-HC exchange sound; iii-a peeling UNSOUND, "growing slack" false) |
| 3 | parity-xor-reachability | 1543 | cold-start (NEW) | APPROVE (registered; genuinely different G1 framing) |
| 4 | minimax-strategy-family | 1479 | advanced (r4) | KEEP (n=2 baseline + lemma donor) |
| 5 | lp-dual-region | 1437 | partial (r5) | KEEP (collapsed to finite family; certified lemma donated) |
| 6 | alternating-potential | 1411 | advanced (r4) | KEEP (conditional on G1-i-HC rest-split) |
| — | surrogate-adversary | 1319 | dead-end (r1) | dead (no re-dispatch) |

Pairwise comparisons anchored to round-5 outcomes: pairing-charging (verified-milestone, closing n=4) > dyadic-induction (advanced, G1-i-HC exchange sound but iii-a unsound) > parity-xor-reachability (cold-start, sound new framing) — the three are ordered by proven infrastructure + proximity to a closed milestone. parity-xor-reachability vs dyadic-induction is a DRAW on the G1 crux (both sound, both unproven at the hard step; dyadic has proven lemmas + sound exchange, parity-xor has uniform applicability + sound obstruction — complementary strengths). parity-xor > lp-dual-region (active G1 attack vs collapsed G2) > minimax (slight, both conceded but minimax's n=2 theorem stands) — both below the active attackers. alternating-potential (conditional) stays below the active lines.

---

## Build set

**build set: pairing-charging, dyadic-induction, parity-xor-reachability**

### Builder 1: pairing-charging (slug `pairing-charging`)
**Gap:** close the n=4 very-flat G2 upper bound as a verified MILESTONE via mechanical vertex enumeration.
**Mechanism:** PWL construction value `f_4 = min` over 10 peels × recursive `f_3` (min of `f_2` = certified n=2 menu); f_4 is PWL on the sort-regime arrangement of the 5 pieces; max of PWL on compact polytope Π_4^{cl} at an arrangement vertex (KB *Piecewise-concavity smoothing*). Enumerate the finitely many feasible vertices of Π_4^{cl} (intersections of sort-order + boundary hyperplanes + induced peel-menu breakpoints), evaluate f_4 at each exactly (rational arithmetic), confirm f_4 ≤ 1/31 with equality ONLY at the dyadic vertex p* = (16/31, 8/31, 4/31, 2/31, 1/31).
**Hard steps:** (a) the vertex enumeration (bound: ≤30s, ≤10k vertices, emit early; FALL BACK to the explorer's 5-subcase gap table — one sub-case per binding peel, `min(a−b,b−c)≤(a−c)/2` absorption, 5-gap box arithmetic — if the count explodes); (b) open-polytope strict-interior handling (interior f_4 < 1/31 strictly; supremum 1/31 at p* on the proved Lemma-5 / Lemma-4 facets — state EXPLICITLY as in round-5 Theorem 6); (c) cross-piece-equal-pair cheap-kill pre-pass (check whether n=4 worst configs satisfy p_k = p_i + p_j → D=0).
**Anti-stuck:** write proof PROSE FIRST (PWL/max-at-vertex principle + open-polytope handling), THEN run the enumeration as VERIFICATION (the table is casework, not the engine). Bound all Python ≤10k trials / grid ≤200 / each script <30s / emit early. NEVER assume "obvious." Do NOT present `f_n` as proved (n=4 is a MILESTONE; uniform-in-n induction is a CONJECTURE — the sort-independent-member lift breaks at n=4, needs a NEW invariant). Handle "fewer than 4 Liu marks" directly (equal-halve all ≤4 pieces ⇒ D=0 ≤ 1/31).

### Builder 2: dyadic-induction (slug `dyadic-induction`)
**Gap:** close the general G1-i-HC discrepancy bound `Alt_s ≥ (D_{R_0}+1−M)/2` for n≥4, s≥3 via EXCHANGE/CONVEXITY (tower-prefix is the unique minimizer of `Alt_s − target`).
**Mechanism:** superincreasing-prefix obstruction (crux aimo-0530 adapted — `E_{R_0}`'s bands have superincreasing swing amplitudes, Lemma 10 certified; the largest-band alignment is forced). Exchange step: moving a breakpoint off a G-extremum into a band interior changes `G(f_i)` at rate ±1/2, and the alternating-sign structure of `Alt_s` means the sign makes `Alt_s` INCREASE. The superincreasing surplus (largest swing > sum of all smaller) must dominate the W-sum coupling adjustment.
**Hard steps:** (a) the W-sum coupling (the OPEN crux — the superincreasing surplus must dominate the coupling adjustment of the other breakpoints preserving `Σ f_i = W`; make this rigorous, prove from scratch, do NOT cite the crux templates); (b) the tight case arithmetic at the tower-prefix (each `ε_i` contributes `±ε_i/2` to `Alt_s` and `−ε_1/2` to target, summing to equality via `Σε=1` — verified n=2..6, use as the equality verification).
**DO NOT pursue G1-iii-a peeling recursion** — it is the THIRD FAILED MECHANISM (verified: the recursion does NOT iterate — only one peel is valid; `Σε_i + D_alt(floor) = 35` but actual `D=1` at n=4). Mark iii-a OPEN (bound `D ≥ 1` is TRUE, tight at n=4,5 — I verified a tight D=1 config at n=5: `F' = {15.5, 7.5, 4, 2, 1, 0.5, 0.5, 0.5, 0.5}`; iii-a is NOT "easier with growing slack" — that claim is numerically FALSE, tight D=1 at n=4,5). DO NOT rely on "iii-a easier." DO NOT retry peeling-pair (unsound) or continuity (provenance switches). G1-iii-b (flat twin): flag OPEN, do not attempt. splits-inequality.md stays PARTIAL.
**Anti-stuck:** write proof PROSE FIRST for the exchange argument (state the obstruction, the exchange step, the W-sum coupling lemma with its mechanism). Bound all Python ≤10k trials / grid ≤200 / each script <30s / emit early. NEVER assume "obvious." If the W-sum coupling can't be closed in one round, HONESTLY flag it (do not overclaim).

### Builder 3: parity-xor-reachability (slug `parity-xor-reachability`, NEW)
**Gap:** prove `D ≥ 1/D_n` via F_2-representation impossibility — `f = [j_Liu odd]` (dyadic config) has superincreasing-DISTINCT band lengths, so `≤n` paired-equal-length-interval toggles cannot represent `f` exactly, forcing a residual `≥ 1/D_n` (the smallest band).
**Mechanism:** F_2-algebraic toggle-reachability (NOT a measure inequality). The certified parity-XOR toggle lemma (`lemmas/parity-integral.md`) gives `D = ∫(f ⊕ h) dt`, `D=0 ⟺ f = h` a.e. (f exactly representable as XOR of ≤n paired-equal-length-interval toggles `h_{p_k} = 1_{[0,v_k)} + 1_{[u_k,p_k)}`). The obstruction: (i) f's bands have superincreasing-DISTINCT lengths (verified n=1..6); (ii) a single toggle (two equal-length intervals) covers at most ONE band of f perfectly (distinct lengths); (iii) the largest band `L_m > L_1+…+L_{m−1}` forces any representation to include a toggle covering it (superincreasing-prefix obstruction, crux aimo-0530 adapted); (iv) that toggle's other interval creates a residual; the recursion terminates with an uncovered portion ≥ the smallest band `1/D_n`.
**Hard steps:** (a) the residual quantification (the OPEN crux — the residual from a toggle's other interval is `L − 2|other interval ∩ (f=1 region)|`, NOT obviously `≥ L − (sum of smaller bands)`; the other interval could overlap f=1 regions, REDUCING the residual; make this rigorous — the tight equal-halving case (other interval perfectly covers f=0 region, residual = L = the band, D = 1/D_n) is the BOUNDARY the obstruction must reproduce); (b) the toggle-structure constraint (toggles constrained by dyadic piece structure `p_k ∈ {1,2,…,2^n}/D_n`, `v_k ≤ p_k/2` — check whether this STRENGTHENS [fewer reachable representations] or WEAKENS [dyadic-aligned toggles cover bands more efficiently] the obstruction); (c) the collapse-to-union-bound CHECK (verify at the bookkeeping level that the F_2 framing does NOT coincide with the Lemma-7 union-measure bound — my analysis says it does NOT collapse, because the F_2 framing is uniform across G1 sub-cases while the union bound is G1-i-HC-specific; if it DOES collapse, RETHINK — but proceed assuming it does not).
**Anti-stuck:** write proof PROSE FIRST (F_2-reachability question, superincreasing-distinct band structure, obstruction lemmas with mechanisms). Verify n=2 (f-bands {1,2}, 2 toggles, tight case leaves smallest band — D=1/7) and n=3 (f-bands {1,4}, 3 toggles, tight D=1/15) reproduce the bound. Verify the tight equal-halving case is the BOUNDARY (D = 1/D_n exactly). Bound all Python ≤10k trials / grid ≤200 / each script <30s / emit early. NEVER assume "obvious."
