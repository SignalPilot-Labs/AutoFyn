# proof-reviewer report — imo-2026-03 (Chu-Han war, IMO 2026 P3), Round 1

I reviewed all four built approaches independently, re-deriving every load-bearing step. The conjectured answer `c(n) = 2^n/(2^{n+1}−1)` (= `2/3, 4/7, 8/15, 16/31, 32/63` for n=1..5) is arithmetically correct and verified by substitution; the dyadic Liu config is held to *exactly* the target by Xiang's equal-halving reply (tight). The greedy-alternating lemma is airtight (verified by exhaustive computation of the exchange deficit `Δ_k`). No approach is `solved`; the overall problem Status is `partial`.

## Independent verification performed

- **Answer arithmetic:** `c(n) = 2^n/(2^{n+1}−1)` and the D-reduction `(1 + 1/D_n)/2 = 2^n/D_n` and the recursion `1/c(n) = 1/c(n−1) + 1/2^n` — all reproduce exactly (Python `fractions`).
- **Greedy-alternating lemma:** computed `Liu's total(i) = a_i + E_i` for `i = 1..m` on random sorted multisets with ties; the deficit `S_odd − total(i) = Δ_k = Σ_{j=1}^k (a_{2j−1} − a_{2j}) ≥ 0` reproduces exactly for both even and odd `i`. The dyadic-induction proof (explicit `Δ_k` for both parities) is the rigorous version; the pairing-charging version asserts "the odd-i, odd-m variants are identical" without showing them (substantively correct, less rigorous).
- **n=2 lower bound 0- & 1-mark cases (dyadic-induction §4.2):** re-derived by hand and re-ran the casework — `min D` over splitting piece 4 is exactly `1` (attained for smaller-part `b ∈ [1,2]`); splitting piece 2 gives `D = 3`; splitting piece 1 gives `D ≥ 2`. All `≥ 1 = 1/D_2` (scaled). Confirmed correct.
- **n=2 two-mark G1 case (the open n=2 sub-case):** exhaustive grid (50-point) over all 2-mark strategies (two distinct pieces split, or one piece split twice) confirms `min D = 1` exactly — the inequality is *true* but no approach gives a rigorous proof for it; correctly flagged as open/numerical.
- **Equal-split attainment `D = 1/D_n`:** verified exactly (n=1..5) — the lower bound is tight at the dyadic config; any upper-bound argument must have no slack here.
- **n=1 upper bound:** `min(1−b_1, 2b_1−1)` maximized over `b_1 ∈ [1/2,1]` gives exactly `1/3` at `b_1 = 2/3` — the two linear regimes cross at the target. Correct.
- **Even-rank-insertion sub-lemma (alternating-potential §2.5):** verified on 100k random `(R, α)` trials — even-rank insertion gives `S_odd(new) ≤ T_R` automatically; odd-rank insertion's bound `α ≤ S_odd(R)_{≥t} + S_even(R)_{<t}` is the exact iff condition. Correct.
- **Factor-of-2 obstacle (alternating-potential §3.3):** naive dyadic-decrement telescope gives `D ≤ 1/2^n`; target is `1/(2^{n+1}−1)`; ratio `1.5, 1.75, 1.875, 1.94, … → 2`. Confirmed real. Proposed resolutions (a) (D_0 < 1 for worst Liu) is false (`b_1 → 1` gives `D_0 → 1`); (b) (decrements `1/2^{k+1}`) sums to `< 1/2`, far above `1/D_n` for n ≥ 2 — insufficient. The obstacle is a genuine structural wall, not a missing label.

## Per-approach verdicts

### 1. pairing-charging — CHANGES REQUESTED, Status `partial`, outcome `advanced`

**What's proved (correct):**
- Greedy-alternating lemma (§1) — substantively correct, though the exchange-argument write-up is lighter than dyadic-induction's (asserts "the odd-i, odd-m variants are identical telescoping sums" without exhibiting them; the conclusion is verified correct, but for the certified lemma I used the dyadic-induction version which gives explicit `Δ_k` for both parities).
- D-reduction (§2): clean and correct.
- n=1 both bounds (§3 Case A + n=1 Case B; §4.1): correct and rigorous.
- Lower-bound construction + Case A (largest piece unsplit, all n): correct, one-line structural fact.
- Equal-split attainment and answer verification: correct.

**Gaps (real, honestly flagged):**
- **G1-general (lower bound):** the splits-inequality `D ≥ 1/D_n` for the dyadic config when Xiang splits the largest piece — proved only for n=1; for n=2 the write-up is explicitly omitted ("we mark its full write-up as a minor omission rather than a conceptual gap"). This is a real rigor gap: the n=2 two-mark case is *true* (I verified numerically) but not proved in the file. The n ≥ 3 case is genuinely open (the interleaving/rank-shift argument does not close).
- **G2-general (upper bound):** the constructive domino/pairing partition for ARBITRARY Liu marks is built only for n=1. The approach correctly self-flags the circularity risk (a partition that only works for the dyadic config is dead) and the tightness requirement (the telescope must hit `1/D_n` exactly, no slack). This is the approach's defining bet and it is open.

**No overclaim.** Status `partial` is accurate. The builder's own assessment matches mine. The upper-bound mechanism (pairing) is the one with strongest empirical support (the outline-reviewer's numerics show the true minimizer creates near-equal pairs), so this is the most promising upper-bound route of the four — but the construction is not yet closed.

**Gap to close next round:** (1) write out the n=2 two-mark Case B rigorously (it is a finite casework, tractable); (2) attack G1-general (n ≥ 3) via the induction on `g_n = 2 g_{n−1}` with a rigorous interleaving/rank-shift lemma; (3) construct the domino/pairing partition for arbitrary Liu marks (the defining crux).

### 2. dyadic-induction — CHANGES REQUESTED, Status `partial`, outcome `advanced`

**What's proved (correct, most rigorous of the four):**
- Greedy-alternating lemma (§1): full strong-induction proof with explicit `Δ_k` for both even and odd `i` — the version I certified into `lemmas/greedy-alternating.md`. Handles ties correctly (`≥` throughout).
- Parity-integral reformulation (§2, Lemma 3): `D = ∫[j(t) odd]dt` via Fubini on a finite sum — clean and correct.
- Recursion identity (§3, Lemma 2): verified exactly.
- Lower-bound construction + the dyadic "largest exceeds sum of rest" forcing: correct.
- n=1 both bounds (§4.1, §5.1): rigorous.
- n=2 lower bound 0- & 1-mark cases (§4.2): rigorously proved, independently re-verified by me.

**Gaps (real, honestly flagged):**
- **G1-general (lower bound):** the n=2 two-mark sub-case and all n ≥ 3 — stated as **Conjecture 1** (good rigor hygiene: distinguished from proved). The induction obstacle (descendants of the split largest piece interleave with the rest in the sorted order, so the global `D` is not the sum of the two sub-`D`s) is correctly identified. The parity-integral handle is the intended attack but not closed.
- **G2 (upper bound, inductive peeling):** open. The approach honestly incorporates the outline-reviewer's numerics showing (a) the optimal Xiang split on the dyadic n=2 config is *non-equal* (barely-split `4/7 → 0.425+0.146`), not the equal-halving a naive peeling would suggest; and (b) on hard random configs the true minimizer is *pairing-like*, not peeling-like. The approach flags that if no peeling strategy realizes the recursion for arbitrary marks, it must fall back to pairing (conceding to `pairing-charging`) or a direct cap.

**No overclaim.** Status `partial` accurate; the conjecture-vs-theorem hygiene is exemplary.

**Gap to close next round:** (1) close the n=2 two-mark Case B (finite casework) to upgrade that sub-case from conjecture to theorem; (2) attack the G1-general inductive step — the interleaving obstacle is the crux; (3) for G2, either derive the peeling split point from the recursion (not assume equal-splitting) and prove the `≤ n` marks accounting, or honestly report the peeling cannot realize the recursion and concede the upper bound to the pairing route.

### 3. alternating-potential — CHANGES REQUESTED, Status `partial`, outcome `partial`

**What's proved (correct, reusable):**
- Greedy-alternating lemma (§1): proved, but the exchange-argument write-up is sketchy ("A direct computation gives `O_rest(j) − S_even = Σ (a_{2k−1} − a_{2k})`" without the explicit index bookkeeping for general `j`). The statement is correct (verified); for certification the dyadic-induction version was preferred.
- D-reformulation (§1 Corollary) and universal floor `D ≥ 0`: clean.
- Lower-bound construction, `D_init` computed exactly (n=1..4), equal-split attainment `D = 1/D_n` (n=1..5 verified): correct.
- **Even-rank-insertion sub-lemma (§2.5):** a genuine structural contribution. Independently verified on 100k random trials — the iff condition for odd-rank insertion is exactly right. This is the load-bearing mechanism the full G1 reduces to, and it is promotable to `lemmas/insertion-rank.md` if a sibling wants to import it.
- The sub-lemma's corollary (split largest once, rest unsplit ⇒ `D ≥ 1/D_n`) is correctly derived from it.
- n=1 both bounds: rigorous.

**Gaps (real, honestly flagged):**
- **GAP-L (lower bound, general n):** the inductive sub-claim "for the dyadic rest after ≤ n−1 splits, an extra `α` at odd rank `t` still satisfies `α ≤ S_odd(R)_{≥t} + S_even(R)_{<t}`" — the genuine inductive content of G1, not closed. (Also the case "largest piece unsplit + smaller pieces split" is not explicitly treated in this file, though it is trivially `D ≥ 1/D_n` by the same argument as pairing-charging's Case A — a minor omission, not a deep gap.)
- **GAP-U (upper bound, the approach's DISTINCTIVE crux): UNBRIDGEABLE in the direct-D-cap framing.** The factor-of-2 obstacle is confirmed (I verified the ratio → 2). The proposed resolutions are correctly identified as false/insufficient. No non-dyadic decrement schedule reaching `1/D_n` was found, and the obstruction is structural (a single-mark split's net reduction is at most half the naive "remove the piece" estimate because re-sorting displaces other pieces and flips their signs). **The approach's defining bet (upper bound via direct D-cap) is dead.** The builder honestly reports this and notes the true upper bound would require reproducing the pairing structure — at which point the approach collapses into `pairing-charging`'s framing.

**No overclaim** — the dead crux is reported honestly as a GAP, not papered over with a fake decrement schedule. Status `partial` is accurate (real reusable progress: D-reformulation + even-rank-insertion sub-lemma + n=1 + lower-bound base).

**Gap to close next round:** the upper-bound direct-D-cap is a confirmed *structural* dead-end, not a gap a builder can simply "close more" — it needs a framing pivot. The lower-bound GAP-L is the live, shared, tractable front. **Recommendation to the outliner:** either re-plan this approach's upper bound around a different framing (recursive min-of-strategies = dyadic-induction's route, or pairing = pairing-charging's route, in which case the approach loses distinctiveness and should be retired/merged), or re-seed a genuinely different upper-bound framing (LP/minimax-duality, measure-concentration). Do NOT send the builder back to "close" the direct-D-cap — it is structurally impossible.

### 4. surrogate-adversary — RETHINK, Status `unsolved`, outcome `dead-end`

**What's established (a NEGATIVE result only):** an exhaustive falsification sweep over many candidate non-pairing restricted Xiang strategies (equal-split largest, threshold-gated, barely-split, mirror, halve-each, balance-top-two, fixed-fraction, split-to-match-next, dyadic-fixed, dyadic-offset-mirror, myopic greedy-min-D, 2-ply lookahead, fixed dyadic grids) shows EVERY one fails to cap Liu at `2^n/D_n` for n ≥ 2 (worst ratio > 1.0 in every case). The only mechanisms that cap reproduce the pairing structure of the optimal Xiang response (near-equal consecutive pairs that cancel in `D`) — which is `pairing-charging`'s framing, not a distinct surrogate. The fine-grid `{k/(m·D_n)}` strategies approach the cap as `m → ∞` but only by being a near-dense discretization of the optimal; proving such a grid caps is equivalent to proving the upper bound directly (no analytical simplification).

**Why the approach can't work as set up:** the surrogate-adversary *technique* (aimo-0560, weaker-minimizer direction) is sound in direction (a restricted strategy's cap transfers up to real Xiang), but it is *moot without a working restricted strategy to apply it to*. The approach's defining bet — that a distinct non-pairing restricted strategy exists — is falsified. The approach has no correct positive progress on the upper bound (only a negative result); the lower bound and greedy lemma are shared and not reproduced.

**The builder's own RETHINK recommendation is correct.** I confirm it. The approach should be retired (in favor of `pairing-charging`, which directly formalizes the empirically-correct mechanism) or re-seeded with a genuinely different upper-bound *framing* (not a fourth D-monovariant surrogate — the field's three D-monovariant routes are converging on pairing, and a fourth would hit the same wall).

**No overclaim** — the negative result is honestly reported, the falsified strategies are recorded to prevent retry. Status `unsolved` is accurate (no correct positive progress; the upper-bound half is unproved and the defining mechanism is dead).

## Lemma certifications

- **`lemmas/greedy-alternating.md` — CERTIFIED.** Source: dyadic-induction §1 (the most explicit version). Statement proved `sorry`-free; every case (even `i`, odd `i`, ties) handled by the explicit `Δ_k` formula; conclusion no stronger than proved. Importable by all four approaches; the pairing-charging and alternating-potential versions may be replaced by a reference.
- **`lemmas/splits-inequality.md` — NOT CERTIFIED.** The splits-inequality `D ≥ 1/D_n` for the dyadic config under arbitrary Xiang splits is open for n ≥ 3 (and the n=2 two-mark sub-case is asserted-but-unproved in every approach). Per the dispatch instruction, do not certify.
- **Even-rank-insertion sub-lemma (alternating-potential §2.5):** correct and reusable, but it is a *piece* of G1 (it handles one structural case), not a standalone load-bearing lemma for the whole problem. Left in the approach file for now; promotable to `lemmas/insertion-rank.md` if a sibling builder wants to import it next round.

## Overall

The problem is `partial`. The verified pillars: greedy-alternating lemma (certified), D-reduction, n=1 fully solved both bounds, lower-bound construction + Case A, n=2 base cases, parity-integral reformulation, recursion identity, even-rank-insertion sub-lemma. The two open fronts are G1-general (shared, tractable — the inductive interleaving step) and G2-general (the upper bound — the pairing construction is the empirically-supported route, via `pairing-charging` and/or `dyadic-induction`'s recursion). The `alternating-potential` direct-D-cap and `surrogate-adversary` restricted-strategy routes are confirmed dead-ends for the upper bound.
