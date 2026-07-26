# Round-4 proof-reviewer report — imo-2026-03 (Chu-Han war)

Reviewed all four round-4 builds. Every "PROVED" claim independently re-derived and sort/compute-checked (Python `fractions` exact, ~300k total trials). No XOR/parity slips survived this pass. Two new lemmas certified; `splits-inequality.md` confirmed stays PARTIAL.

## Per-slug verdicts

### 1. dyadic-induction — CHANGES REQUESTED (Status: partial)

**What verified (independent re-derivation + computation):**
- **Lemma 4** (`D = M − D_R`): OK on 3000 random trials.
- **Lemma 5/7** (multi-split formula `D = M − D_{R_0} − D_F + 2C` and union-measure `D = M + D_{R_0} + D_F − 2|O_{R_0} ∪ O_F|`): exact identity, 0 failures over 8000 trials (dyadic config, random multi-split F, n=2..4). These are the load-bearing structural identities and they hold.
- **Lemma 8** (2-piece F, rest unsplit, all n ≥ 2): VERIFIED. D ≥ 1 on 80k trials (min D = 1 exactly, 18721 tight configs at n=3). The "rigid top O-block" argument is sound: on `(2^{n−2}, 2^{n−1}]` only the rest's piece `2^{n−1}` survives (`j_{R_0}(t) = 1` odd), so `(2^{n−2}, 2^{n−1}] ⊆ O_{R_0}`. The two-case split (`a ≤ 2^{n−2}`: interval fits below the top O-block; `a > 2^{n−2}`: the part above lies in `O_{R_0}`, contributing 0 to `E`) yields `b + |(b,a] ∩ E_{R_0}| ≤ 2^{n−2}`. The comparison `2^{n−2} ≤ T_n = (2^n − 1 − D_{R_0})/2` is exact (verified n=2..7: `D_{R_0} = (2^n + (−1)^{n−1})/3`, equality at n∈{2,3}). This genuinely closes the n=3 tight Lemma-6 family (F has 2 pieces there) and the entire 2-piece-F regime at n ≥ 4 (slack there, verified worst slack 0 at n=4, positive n≥5). REAL PROGRESS.
- **Lemma 9** (low-cancellation regime, all F, all n): VERIFIED. The trivial overlap bound `|O_F ∩ E_{R_0}| ≤ |E_{R_0}|` yields `D ≥ 1` whenever `D_F ≥ W − D_{R_0} + 1`. 0 failures over 40k trials. Correctly dispatches the "easy" half.
- **Cases A/B/C (round-3 rebuild, now reviewed this pass):** Case A (`2^n` unsplit, all n) — `D = 2^n − D_R ≥ 2^n − (2^n−1) = 1`, sound. Case B (`2^n` split once, all n) — formula `D = 2^n − D_{R_0} − 2·E_1` with `E_1 ≤ 2^{n−1} − D_{R_0}` (sub-measure) gives `D ≥ D_{R_0} ≥ 1` by `G1(n−1)`, sound; boundary `M = 2^{n−1}` saturates to `D = D_{R_0}` (verified n=2..5). Case C (tie, peeling lemma + `G1(n−1)`): sound (peeling lemma certified). All three verified.
- **Full G1 (correct budget ≤ n splits):** n=3,4,5 all give D ≥ 1 (min = 1) over 5000+ trials each with fractional splits. n=2 confirmed by exhaustive-ish grid (split 4&2, split 4 twice): min D = 1.

**Gap remains (honestly flagged by builder, confirmed):**
- **GAP-G1-i-HC** (high-cancellation, multi-piece F `s ≥ 3`, rest unsplit): the overlap bound `|O_F ∩ E_{R_0}| ≤ (M − D_{R_0} + D_F − 1)/2` is unproved. Lemma 8 (2-piece, single-interval `O_F`) does not extend: with `s ≥ 3`, `O_F` is a union of ≥1 intervals and the "top O-block" trick (which used `O_F` ending at `a`) no longer pins the geometry. Verified TRUE numerically (n=2..6, tight at n=3,4 via multi-piece F).
- **GAP-G1-ii** (`M = 2^{n−1}` fragment, rest's `2^{n−1}` split): Lemma 5's top band shifts; tiling deficit must be re-derived. Verified TRUE; proof open.
- **GAP-G1-iii** (all fragments of `2^n < 2^{n−1}`): the outline's "reduce to `G1(n−1)`" is **UNSOUND** — CONFIRMED. Folded rest total = `3·2^{n−1} − 1 ≠ D_{n−1} = 2^n − 1` (verified n=3..6: 11≠7, 23≠15, 47≠31, 95≠63). The rest is NOT a dyadic `(n−1)` config. This is a near-tie regime symmetric to G1-i, not a clean induction. Route back to outliner for re-framing (the statement is TRUE numerically; the proof route needs re-thinking).
- **GAP-G2** (upper bound): unchanged, conceded (carried by siblings).

**splits-inequality.md status:** confirmed PARTIAL (advanced). Lemmas 7/8/9 added correctly as proved components; the high-cancellation multi-piece gap (G1-i `s≥3`, G1-ii, G1-iii) remains open. No upgrade to FULL this round.

**Outcome recorded:** `advanced` — Lemmas 7/8/9 closed (2-piece F + low-cancellation + union identity), round-3 rebuild (Cases A/B/C) verified, n=3 tight family closed. High-cancellation multi-piece + G1-ii + G1-iii remain; G1-iii reduction unsound as outlined.

**Routing:** CHANGES REQUESTED — re-dispatch dyadic-induction to attack (a) the high-cancellation multi-piece overlap bound (the `s ≥ 3` crux), and (b) G1-ii (split-rest tiling deficit). G1-iii goes back to the outliner for re-framing (the "reduce to G1(n−1)" route is dead).

---

### 2. alternating-potential — CHANGES REQUESTED (Status: partial)

**What verified:**
- **G1-ii r=2 sub-case (subsumed by Case B):** VERIFIED. When `2^n → 2^{n−1} + 2^{n−1}` (one split) and rest's `2^{n−1}` is split, the two `2^{n−1}` fragments (both from `2^n`'s split) form an equal pair occupying ranks 1,2, contributing `+2^{n−1} − 2^{n−1} = 0`; the rest (ranks 3,4,…) gives `D = D_{R_0}`. Equivalently via parity-integral: `+2·1_{[0,2^{n−1})}` is even, parity-neutral. `D = D_{R_0} ≥ 1` by `G1(n−1)`. This is exactly Case B's `M = g_2 = 2^{n−1}` boundary (Case-B bound `D = 2^n − D_{R_0} − 2·E_1` with `E_1 = 2^{n−1} − D_{R_0}` saturates to `D = D_{R_0}`). Verified exact-rational n=2..5.
- **G1-ii r≥3 ⟹ G1-i perturbation/continuity reduction:** the reduction itself is SOUND. Perturb `M = 2^{n−1} → 2^{n−1} + ε` (reduce F's largest fragment by ε, keep `R_0` unchanged) lands in a valid G1-i config (`M > 2^{n−1}`, rest's `2^{n−1}` split — allowed in G1-i). `D = ∫[j odd]` is continuous in ε (piecewise-linear; stable sort at ε=0 since `M` strictly largest in G1-ii). Verified n=3: `D` continuous across sort-boundary crossings, all `D ≥ 1`, `|D_i − D_ii| ≤ 3ε`.

**Critical caveat (the reduction is CONDITIONAL, not unconditional):** the perturbed G1-i config has F with `r−1 ≥ 2` pieces AND rest's `2^{n−1}` SPLIT. dyadic-induction's Lemma 8 closed G1-i with **REST UNSPLIT** only; the "rest split" sub-case of G1-i is part of the still-open high-cancellation multi-piece gap. So the reduction is conditional on a result that did NOT materialize this round. The builder is honest about this ("Conditional on dyadic-induction certifying G1-i").

- **G2 upper bound:** CONCEDED (sound, unchanged from round 2). The `Φ = D − λ·Π` collapse to the factor-of-2 wall is confirmed; no non-pairing Φ found.
- **Band-parity lens:** confirmed as Lemma-4 re-lensing, NOT a bypass (the "shave 1" wall persists). Honest.

**Gap remains:** GAP-L narrowed (G1-ii r=2 closed; r≥3 conditionally reduced to G1-i, which is still open). GAP-U conceded.

**Outcome recorded:** `advanced` — G1-ii r=2 closed (subsumed by Case B); G1-ii r≥3 soundly reduced to G1-i (conditional). G2 conceded.

**Routing:** CHANGES REQUESTED — keep alive on the lower-bound half. The G1-ii reduction becomes load-bearing the moment dyadic-induction closes G1-i (with rest split). No re-dispatch needed this round unless G1-i closes; the approach's machinery (toggle lemma, peeling lemma + corollary, G1-ii reduction) is certified and reusable.

---

### 3. pairing-charging — CHANGES REQUESTED (Status: partial)

**What verified:**
- **Naive surplus-chain FALSIFIED:** CONFIRMED. For n=3, the (n−1)-mark chain `p_1 → p_2 → …` leaves `p_4` unpaired; `D = |r_{n−1} − p_{n+1}| = |2p_1 − 1|` (arithmetic: `r_{n−1} = 2p_1 − 1 + p_{n+1}`, so `r_{n−1} − p_{n+1} = 2p_1 − 1`). Verified: 18050/30000 n=3 flat configs fail (`|2p_1−1| > 1/15`). The chain is also non-executable for genuinely flat configs (`p_1 − p_2 < p_3`). All 2-mark chain variants collapse to the single value `|2p_1−1|`. DEAD — recorded to prevent retry.
- **CORRECT construction (peel once + n=2 menu on 3-piece rest):** VERIFIED. Lemma 3 (certified) makes the peel pair `(p_j, p_j)` parity-neutral, `D_final = D_rest` exactly. The n=2 menu (certified) on the 3-piece rest (total `T = 1 − 2 p_j`) gives `D_rest = min(c, |2a−T|, a−b, b−c) ≤ T/7`. Six peel choices; take the min. 0 failures over 30000 n=3 flat configs (max `0.0662 < 1/15`), tight at dyadic `(8/15,4/15,2/15,1/15)` (peel `p_1→p_2`, rest `(4/15,2/15,1/15)`, menu min `= 1/15`).
- **Lemma 5 (peel-once + (n−1)-bound):** PROVED and VERIFIED. The arithmetic `(1 − 2 p_j)/D_{n−1} ≤ 1/D_n ⟺ p_j ≥ 2^{n−1}/D_n = g_{n−1}` is exact (verified n=2..7: at threshold both sides equal `1/D_n`; above/below strictly below/above). The threshold `g_2 = 4/15` for n=3 is exact. **CERTIFIED into `lemmas/peel-once-inductive.md`** (closes "some `p_j ≥ g_{n−1}`" regime for all n, conditional on the (n−1)-bound; base n=2 certified).
- **n=3 Cases A (p_2 ≥ 4/15) & B (p_3 ≥ 4/15):** PROVED via Lemma 5 (loose bound `T/7` suffices).
- **Case C (very-flat, p_2,p_3 < 4/15):** VERIFIED via 3-peel subfamily `{p_1→p_2, p_1→p_4, p_2→p_3}` × full n=2 menu (0 failures / 30000, max `0.0646 < 1/15`, tight at dyadic). But the 12-expression sort-regime casework is UNPROVED.

**Gap remains:**
- **G2-flat Case C (n=3):** the 3-peel subfamily × full n=2 menu is verified (0/30k) but the 12-expression sort-regime casework (each menu member piecewise-linear across ≤3 sort-regimes of the rest triple) is OPEN. This is the immediate next target.
- **G2-flat very-flat residual for n ≥ 4:** unverified, unproven.
- **G1-general (lower, n ≥ 3):** shared, imported from `splits-inequality.md` (PARTIAL).

**Outcome recorded:** `advanced` — naive surplus-chain falsified (recorded dead); correct construction found (peel-once + n=2 menu, verified 0/40k); Lemma 5 PROVED + certified (closes "some `p_j ≥ g_{n−1}`" regime for all n); Cases A & B closed; Case C verified-but-unproved.

**Routing:** CHANGES REQUESTED — re-dispatch pairing-charging to close the Case C 12-expression sort-regime casework (the construction is verified; the casework is the honest wall). The general-n very-flat residual (all `p_j < g_{n−1}`) is the deeper crux.

---

### 4. minimax-strategy-family — CHANGES REQUESTED (Status: partial)

**What verified:**
- **M2 XOR bug FIXED:** CONFIRMED. The §3.1 derivation now correctly computes `f' = f ⊕ 𝟙_{[0,p_3)}`: on `[p_3, p_2)` we have `f=0, 𝟙_{[0,p_3)}=0`, so `f'=0⊕0=0` (the previous `0⊕0=1` slip is gone). Derived `∫ f' = p_1 − p_2`. The tiny barely-split toggles `B=[0,ε)⊂[0,p_3)` (contrib `+ε`) and `C=[p_1−ε,p_1)⊂[p_2,p_1)` (contrib `−ε`) cancel. **Sort-verified:** M2 multiset `{p_1−ε, ε, p_3/2, p_3/2, p_2}` gives `j(t) = 5,4,2,1,0` on `[0,ε),[ε,p_3/2),[p_3/2,p_2),[p_2,p_1−ε),above`, hence `D = ε + (p_1−ε−p_2) = p_1−p_2` exactly. 0 failures over 3000 sort-checks (both full and `ε→0` limit). File internally consistent: §3.1 derivation, §3 menu statement, §3.2 theorem, §3.3 table all use `p_1 − p_2`.
- **n=2 upper bound:** stands, 0/30000 exceed. The 5-member menu `{p_3, p_1−p_2, p_2−p_3, p_1−p_3, |2p_1−1|}` caps at `1/7`. The §3.2 contradiction (B+ `p_1>4/7 ⇒ sum>1`; B− `p_1<3/7 ⇒ b<2/7, c>2/7, contradict b≥c`) is valid. Tight at dyadic (M1, M3, M5 tie at `1/7`). Unique-worst-at-dyadic PROVED for n=2.
- **Pairwise-diff realization (n=3, EH complement):** VERIFIED. "EH the `n−1` pieces not in `{i,j}`" gives `D = p_i − p_j` regime-independently. 0 failures over 9000 checks (6 pairs × 3000 configs). Generalizes to all n ≥ 2. **CERTIFIED into `lemmas/pairwise-diff-strategy.md`**.
- **Peel-complement realization (n=3):** VERIFIED. 3-mark peel "p_1 vs p_2, p_3 vs p_4, peel remainders" gives `|2(p_1+p_4)−1|`. 0 failures over 2000 checks.
- **G2-flat n≥3 falsification sweep:** all claims confirmed. Naive chain fails (4938/20000), enriched 14-member clean family fails (204/30000, 0.68%, worst 0.0876), rich fixed-fraction family caps (0/879) but via continuously-tuned splits (continuous optimum ~0.017 on hardest config).

**Gap remains:**
- **G2-upper-n≥3:** no clean finite regime-independent family caps at `1/D_n` for n=3. The §3.2-style contradiction does NOT generalize. The minimax-over-FINITE-family framing may be fundamentally insufficient for n ≥ 3.
- **G1 (lower, shared):** pending `splits-inequality.md` certification.

**Spec concern (flagged for outliner):** the clean finite-family framing is confirmed insufficient for n≥3 (0.68% residual, clean formulas don't cap; capping requires continuous tuning). Route to outliner: G2-flat n≥3 should consider conceding the minimax-over-finite-family framing and pursuing a continuous/LP-dual per-regime argument (the LP-dual explorer's framing B is consistent with this finding).

**Outcome recorded:** `advanced` — M2 XOR bug fixed (file internally consistent); n=2 milestone stands; pairwise-diff + peel-complement realizations verified + certified; G2-flat n≥3 honestly open with spec concern confirmed.

**Routing:** CHANGES REQUESTED — the n=2 milestone + certified realizations stand. The n≥3 crux is honestly open; route the spec concern to the outliner (finite-family framing insufficient; consider continuous/LP-dual re-framing).

---

## Overall status update for current.md

**## Status:** `partial` (unchanged — both walls G1-general and G2-general remain open for n ≥ 3).

**## Current best deltas (round 4):**
- **dyadic-induction Lemma 8** (2-piece F, rest unsplit, all n ≥ 2): PROVED + verified (closes n=3 tight Lemma-6 family + 2-piece-F regime at n≥4). Added to `splits-inequality.md`.
- **dyadic-induction Lemma 9** (low-cancellation regime, all F, all n): PROVED + verified (trivial overlap bound; closes `D_F ≥ W − D_{R_0} + 1` regime). Added to `splits-inequality.md`.
- **dyadic-induction Lemma 7** (union-measure identity `D = M + D_{R_0} + D_F − 2|O_{R_0} ∪ O_F|`): PROVED identity + verified (0 error/8k). Added to `splits-inequality.md`. The "shave 1 off the trivial union bound" wall is now framed precisely.
- **alternating-potential G1-ii r=2** (subsumed by Case B): closed + verified.
- **alternating-potential G1-ii r≥3 ⟹ G1-i** (perturbation/continuity): sound conditional reduction, verified (CONDITIONAL on dyadic-induction closing G1-i with rest split — not yet closed).
- **pairing-charging Lemma 5** (peel-once + (n−1)-bound): PROVED + verified + **CERTIFIED** (`lemmas/peel-once-inductive.md`). Closes "some `p_j ≥ g_{n−1} = 2^{n−1}/D_n`" regime for all n (conditional on (n−1)-bound; base n=2 certified). n=3 threshold `g_2 = 4/15` exact.
- **pairing-charging n=3 Cases A & B** (`p_2 ≥ 4/15`, `p_3 ≥ 4/15`): PROVED via Lemma 5.
- **pairing-charging correct construction** (peel-once + n=2 menu, falsified naive surplus-chain): verified 0/40k, tight at dyadic. Case C (very-flat) verified 0/30k but casework OPEN.
- **minimax M2 XOR bug:** FIXED + sort-verified (file internally consistent). n=2 upper bound stands.
- **minimax pairwise-diff realization:** PROVED + verified + **CERTIFIED** (`lemmas/pairwise-diff-strategy.md`). General n ≥ 2: EH complement gives `D = p_i − p_j`.
- **minimax peel-complement realization (n=3):** PROVED + verified (3-mark peel gives `|2(p_i+p_j)−1|`).
- **minimax G2-flat n≥3 spec concern:** confirmed — clean finite-family framing insufficient for n≥3 (0.68% residual; capping requires continuous tuning).

**## Newly certified lemmas (round 4):**
- `lemmas/peel-once-inductive.md` — peel-once + (n−1)-bound (closes "some `p_j ≥ g_{n−1}`" upper-bound regime for all n).
- `lemmas/pairwise-diff-strategy.md` — equal-halve complement gives `D = p_i − p_j` (general n ≥ 2).

**## Approaches tried (round 4 update):**
- dyadic-induction: CHANGES REQUESTED. Lemmas 7/8/9 closed (2-piece F + low-cancellation + union identity); round-3 Cases A/B/C verified. High-cancellation multi-piece (s≥3) + G1-ii + G1-iii open. **G1-iii "reduce to G1(n−1)" UNSOUND — route to outliner** (folded rest total `3·2^{n−1}−1 ≠ D_{n−1}`).
- alternating-potential: CHANGES REQUESTED. G1-ii r=2 closed; G1-ii r≥3 soundly reduced to G1-i (conditional). G2 conceded (sound).
- pairing-charging: CHANGES REQUESTED. Naive surplus-chain falsified; correct construction found (peel-once + n=2 menu); Lemma 5 certified; Cases A&B closed; Case C casework open.
- minimax-strategy-family: CHANGES REQUESTED. M2 fixed (file consistent); n=2 milestone stands; pairwise-diff + peel-complement certified; G2-flat n≥3 open (spec concern: finite-family insufficient).

**## Per-slug routing for next round:**
- **dyadic-induction:** re-dispatch to attack (a) high-cancellation multi-piece overlap bound (s≥3, the crux), (b) G1-ii split-rest tiling deficit. G1-iii → outliner for re-framing.
- **alternating-potential:** keep alive (lower-bound machinery certified); G1-ii reduction becomes load-bearing if dyadic-induction closes G1-i (rest split).
- **pairing-charging:** re-dispatch to close Case C 12-expression sort-regime casework (construction verified; casework is the wall). General-n very-flat residual is the deeper crux.
- **minimax-strategy-family:** n=2 milestone + certified realizations stand. Route G2-flat n≥3 spec concern to outliner (finite-family insufficient; consider continuous/LP-dual re-framing).

## Open walls (unchanged, both real)
- **G1-general** (lower, n≥3): high-cancellation multi-piece overlap bound `|O_F ∩ E_{R_0}| ≤ (M − D_{R_0} + D_F − 1)/2` for `s ≥ 3`; G1-ii (split rest); G1-iii (near-tie, unsound induction). `splits-inequality.md` PARTIAL.
- **G2-general** (upper, n≥3 flat regime): Case C (n=3) casework open; general-n very-flat residual open. Both pairing-charging and minimax confirm clean finite-family insufficient for n≥3 flat; continuous/adaptive tuning needed.
