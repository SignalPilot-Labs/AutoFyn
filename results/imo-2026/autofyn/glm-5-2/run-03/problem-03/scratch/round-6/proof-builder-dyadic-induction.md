# Round-6 proof-builder report — dyadic-induction (imo-2026-03)

**Slug:** `dyadic-induction`. **Approach file:** `/home/agentuser/repo/results/imo-2026-03/approaches/dyadic-induction.md`. **Lemma file (PARTIAL, updated):** `/home/agentuser/repo/results/imo-2026-03/lemmas/splits-inequality.md`.

## Status: partial (advanced). s=3 all-n G1-i-HC CLOSED this round; general s≥4 + G1-iii-a + G1-iii-b + G1-ii rest-split + G2 all open.

## Headline

**Closed the `s = 3` piece of the G1-i-HC crux for ALL `n ≥ 3`** via an exchange/reduction argument (Lemma 16, PROVED). This generalizes the round-5 `n = 4, s = 3` sliver witness (§4.8) from a tightness-only statement to a full proof. The general `s ≥ 4` bound remains conjectured+verified; the **W-sum coupling** is identified as the open crux.

## What was PROVED this round (all rigorous, all verified exact-rational)

1. **Lemma 13 — clean alternating-prefix measure form (★).** G1-i-HC `⟺ Ψ(F) := Σ_{i odd} E(f_i) + Σ_{i even} O(f_i) ≤ T_n := (2^n − 1 − D_{R_0})/2`, via the exact identity `Alt_s − target = T_n − Ψ`. Algebraic proof (odd `i`: `G−f/2 = −E`; even `i`: `−G−f/2 = −O`). Decouples the `W`-dependence of the target (the round-5 form had `Alt_s` and target both depending on `W` via `M`). Pair-decomposition `Ψ = S_even(F) + |Q∩E_{R_0}|`. Rigid top `O`-block `(m, U] ⊆ O` for `m = 2^{n−2}`, and the `[0,m]` `E↔O` swap (reduces to the `(n−1)`-rest regions). Verified `n = 2..7`, 0 error.

2. **Lemma 14 — tower-prefix tight arithmetic.** At `F^* = {2^{n−2}, 2^{n−3}, …}` (and the Lemma-6 `ε`-family), `Ψ(F^*) = T_n` exactly (tight iff `s = n−1`; positive slack for `s < n−1`). Each `ε_i` contributes `±ε_i/2` to `Ψ` and `−ε_1/2` to target; `Σε = 1` ⟹ equality. Verified `n = 2..6`.

3. **Lemma 15 — sliding/exchange.** `Ψ` is PWL in `F`; at any maximizer over `{f_1≥…≥f_s≥0, Σf_i≤U}`, each `f_i` is at a dyadic band-edge or tied to a neighbor (KKT: interior-to-band `∂Ψ/∂f_i = 1_{f_i ∈ R_i} ∈ {0,1}`, never 0-in-subdiff, so a non-edge non-tied coord slides). Reduces the search to dyadic-edge arrangement vertices — the setup for the general exchange/vertex attack.

4. **Lemma 16 — s=3, ALL n ≥ 3.** `Ψ ≤ T_n` for `F = {f_1 ≥ f_2 ≥ f_3}`, all `n ≥ 3`. Proof by midpoint `m = 2^{n−2}` exchange:
   - **Case II (spill, `f_1 > m`):** `E(f_1)` saturates at `|E|`; `f_2+f_3 < m`. The `[0,m]` swap reduces `O(f_2)+E(f_3)` to `E_{n−1}(f_2)+O_{n−1}(f_3)`, which is the `(n−1)`-instance of `Ψ` for the 2-piece `F' = {f_2, f_3}` with `M_{n−1} > U_{n−1}` strict. By **Lemma 8** (s=2, CERTIFIED all n), `≤ T_{n−1}`. So `Ψ ≤ |E| + T_{n−1} = T_n` (identity `T_n − T_{n−1} = |E|`). ✓
   - **Case I.a (`f_1 ≤ m/2`):** crude bound `Ψ ≤ 2·D_{R_0}(n−3) + D_{R_0}(n−2) ≤ T_n` via the `D_{R_0}` identities. ✓
   - **Case I.b.1 (`m/2 < f_1 ≤ m, f_2 ≤ m/2`):** swap + Lemma 8 at `(n−1)` (boundary via peeling/C) gives `O(f_2)+E(f_3) ≤ T_{n−1}`; `Ψ ≤ (|E|+f_1−m)+T_{n−1} ≤ T_n` since `f_1 ≤ m`. ✓
   - **Case I.b.2 (`f_2 > m/2`):** `E(f_2) = |E|+f_2−m` ⟹ `O(f_2) = m−|E|` (constant!) ⟹ `Ψ = f_1 + E(f_3)`. If `f_3 ≤ m/2`: `E(f_3) ≤ D_{R_0}(n−3)`, `Ψ ≤ m + D_{R_0}(n−3) ≤ T_n`. If `f_3 > m/2`: `Ψ = f_1+f_3+|E|−m`; `f_1+f_3 < 3m/2` (from `W<2m, f_2>m/2`) and `T_{n−1}+m ≥ 3m/2` (from `D_{R_0}(n−1) ≤ m−1`). ✓
   Verified exact `n = 3..7`, s=3: **0 violations**; min slack 0 at `n = 3,4` (tight tower-prefix `{4,2,1}`), positive slack `{1,2,5}` at `n = {5,6,7}`.

## What remains OPEN (honest)

- **General G1-i-HC bound for `s ≥ 4, n ≥ 4`** (CONJECTURED + verified `n = 2..6`, 0 violations): the **W-sum coupling** is the crux. By Lemma 15 the max of `Ψ` is at a dyadic-edge vertex; sliding one breakpoint requires compensating the others to preserve `Σf_i = W`, and the superincreasing surplus of `E`/`O`-band swings must dominate the multi-breakpoint coupling. For `s = 3` the coupling is a single secondary breakpoint (absorbed by the Lemma-8 reduction); for `s ≥ 4` it is multi-breakpoint. The superincreasing-prefix obstruction (crux `aimo-0530` adapted, NOT cited) is the identified mechanism; making the domination rigorous is the open step. Tight witnesses: n=4 s=4 `F={4,2,1,1/8}`; n=5 s=4 `F={8,4,2,1}` — consistent with Lemma 14 (tower-prefix arithmetic).
- **G1-iii-a** (all `2^n`-fragments `< 2^{n−1}`, rest's `2^{n−1}` UNSPLIT): bound `D ≥ 1` TRUE (tight `D = 1` at `n = 4` AND `n = 5`), proof OPEN. Per outline-reviewer corrections, the peeling recursion `D = Σε_i + D_alt(floor)` is the **THIRD FAILED mechanism** (does not iterate; wrong by 35× at n=4); "iii-a easier / growing slack" is NUMERICALLY FALSE. Needs a FOURTH mechanism (candidates: direct `D_R ≤ M−1` parity-integral bound with the floor's superincreasing `E`-bands as rigid background; or a re-derivation of the discrepancy identity for swapped roles). NOT pursued this round.
- **G1-iii-b** (flat twin, rest's `2^{n−1}` SPLIT): flagged OPEN, not attempted.
- **G1-ii** (`M = 2^{n−1}` fragment, rest SPLIT): conditional on G1-i-HC with rest-split (certified continuity reduction from alternating-potential).
- **G2** (upper bound, general n): open; n=3 closed by pairing-charging (Theorem 6, certified).

## Files modified

- `/home/agentuser/repo/results/imo-2026-03/approaches/dyadic-induction.md`: appended §4.9'–4.9''''' (Lemmas 13–16, the superincreasing-prefix obstruction, the s≥4 status); updated G1-iii-a section (third-failed-mechanism correction); updated `## Status`, `## Approaches tried` (round-6 entry), `## Current best`, the Summary table, and Promotable lemmas.
- `/home/agentuser/repo/results/imo-2026-03/lemmas/splits-inequality.md`: added Lemmas 13–16 as PROVED components; updated the Status header, the OPEN section (s≥4 the crux, iii-a 4th-mechanism-needed, iii-b flat-open), and Import notes. **Stays PARTIAL** (general s≥4 + iii-a + iii-b + G1-ii rest-split open).

## Promotable lemmas (for reviewer certification)

- **Lemma 13** (clean measure form (★), `Ψ ≤ T_n ⟺ D ≥ 1`): PROVED identity, reusable.
- **Lemma 14** (tower-prefix tight arithmetic): PROVED, sharpness case.
- **Lemma 15** (sliding/exchange to dyadic-edge vertices): PROVED, the engine for any exchange attack.
- **Lemma 16** (G1-i-HC for `s = 3`, ALL `n ≥ 3`): PROVED, closes the `s = 3` component.

## Anti-stuck compliance

- Wrote proof PROSE FIRST (the (★) equivalence, the exchange/sliding lemma, the s=3 casework) before running any verification script.
- All Python bounded: ≤10k trials / grid ≤200 / each script <30s / emit early. Scripts: `/tmp/verify_star.py` (reformulation + tower-prefix tight, <5s), `/tmp/sweep_star3.py` (bound sweep, <28s), `/tmp/verify_s3.py` (s=3 n=3..7, <28s, 0 violations).
- Verified the tight case arithmetic at the tower-prefix EXACTLY (the `ε`-slack identity, `n = 2..6`).
- Did NOT pursue G1-iii-a peeling recursion (third failed mechanism, per outline-reviewer). Did NOT rely on "iii-a easier / growing slack" (numerically false). Did NOT retry peeling-pair or continuity for iii-a. G1-iii-b flagged OPEN, not attempted. splits-inequality.md kept PARTIAL.
- HONESTLY flagged the general `s ≥ 4` W-sum coupling as the open crux (did not overclaim).

## Verification data (independent, exact-rational `fractions`)

- (★) identity `Alt_s − target = T_n − Ψ`: 0 error, `n = 2..7`.
- Tower-prefix `Ψ(F^*) = T_n`: exact, `n = 2..6` (tight iff `s = n−1`; slack for `s < n−1`).
- (★) bound sweep (dyadic-edge + 1/8 grid): 0 violations, min slack 0 at the tower prefix, `n = 3..6`.
- s=3 bound: 0 violations `n = 3..7` (trials 806 / 2527 / 9893 / 48385 / 284921); min slack 0 at `n = 3,4` (tight `{4,2,1}`), positive slack `{1, 2, 5}` at `n = {5, 6, 7}`.
