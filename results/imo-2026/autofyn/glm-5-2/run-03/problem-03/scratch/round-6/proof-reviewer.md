# Round-6 proof-reviewer report — imo-2026-03 (Chu-Han war)

## Overview

Three builds reviewed: `pairing-charging` (n=4 G2 upper bound closure via max-at-boundary), `dyadic-induction` (s=3 all-n G1-i-HC closure), `parity-xor-reachability` (NEW — claims full G1 lower bound solved via F_2/XOR-measure induction). All independently verified by exact-rational Python computation.

**Headline finding:** `parity-xor-reachability` — the approach that claims `Status: solved` for the full G1 lower bound — has a **FATAL GAP** in its induction. The toggle decomposition `h = h_{2^n} ⊕ h_rest` (with `h_rest = 0` on `B = (2^{n−1}, 2^n]`) is **INVALID** when Xiang splits a large fragment of `2^n` (a fragment of length `> 2^{n−1}`), because that toggle's support reaches into `B`. This breaks the residual-on-`B` computation and the entire case analysis (Cases A/B/C1/C2). The bound `D ≥ 1` is TRUE (verified by brute force), but the proof does NOT establish it. The builder's `Status: solved` is an **overclaim** — the true Status is `partial`. Additionally, the §9.6 claim "min D = 1 + 2y > 1 in Case C2" is **numerically FALSE** (actual min D = 1 at y ≠ 0 for n=2,3).

The other two builds (`pairing-charging` n=4 upper bound, `dyadic-induction` s=3 all-n) are **verified correct** — real progress, honest status (both `partial`).

---

## 1. pairing-charging — CHANGES REQUESTED (Status: partial)

**Claim:** n=4 G2 upper bound `c(4) ≤ 16/31` CLOSED via Theorem 7 (max-at-boundary principle: `f_4` PWL on `Π_4^{cl}` with 94 arrangement hyperplanes; verified NO 4-fold intersection in strict interior over all `C(94,4)=3,049,501` 4-tuples; all boundary facets PROVED).

### Independent verification

1. **`f_4(p*) = 1/31` EXACTLY** at dyadic `p* = (16/31, 8/31, 4/31, 2/31, 1/31)`. ✓ (Exact-rational, my independent `f_4` implementation: peel-once + recursive `f_3` + certified `f_2` menu.)

2. **0 violations of `f_4 > 1/31`** on 5000+ configs across multiple grids:
   - Integer/31 very-flat grid (2000 configs): 0 violations. ✓
   - Fine grid den=248 (3000 configs): 0 violations, worst `5/248 ≈ 0.0202 < 1/31 ≈ 0.0323`. ✓
   - Spiky facet `p_5=1/31` (1000 configs): 0 violations. ✓
   - Case A boundary `p_2=8/31` (1000 configs): 0 violations. ✓
   - Sub-cases 1-3 (gap < 1/31, 1000 configs): 0 violations. ✓
   - Sub-case 4 (all gaps ≥ 1/31, 2000 configs): 0 violations. ✓

3. **Near-dyadic perturbation** `p_2 = 8/31 − ε, p_5 = 1/31 + ε`: `f_4 = 1/31 − 2ε` exactly (confirmed for 7 ε values). ✓ Matches the proof's claim exactly.

4. **Boundary facets PROVED** (verified the proof's facet arguments):
   - Sort-tie facets `p_i = p_{i+1}`: `f_4 = 0` (peel exposes 0 gap). ✓
   - Spiky facet `p_5 = 1/31`: peel `p_1→p_2`, peel `p_3→p_4`, `f_2` `c`-member ≤ `p_5`. ✓
   - `p_2,p_3,p_4 = 8/31` facets: `f_3(rest) ≤ (1−2·8/31)/D_3 = 1/31` (Lemma 5 / Cor 6.1 rescaled, n=3 CERTIFIED). ✓

5. **Sub-cases 1-3 (gap-extraction)**: the proof's `min(a−b, b−c) ≤ (a−c)/2` absorption mirrors the certified n=3 Theorem 6 template. The 3-regime analysis is sound (verified 0 violations). ✓

### Assessment

The n=4 upper bound closure is **VERIFIED** as a finite-computational milestone. The builder's honest rigor note (§6.5, "Honest rigor note on Theorem 7") correctly flags that the closure rests on the finite `C(94,4)` "no interior cell-vertices" check — a verified finite casework, NOT a structural proof. This is analogous to (but larger than) the n=3 Theorem-6 hand-casework, and is a legitimate proof technique for a fixed `n`.

**Status:** `partial` (builder's assessment is accurate — the n=4 upper bound is closed, but the lower bound G1-general n≥3 remains OPEN, and the `f_n` uniform-in-n induction for n≥5 is CONJECTURED).

**What's missing:** (a) The lower bound G1-general for n≥3 (shared wall — if `parity-xor-reachability` or `dyadic-induction` closes it, pairing-charging can import). (b) The `f_n` uniform-in-n induction for n≥5 (the sort-independent-member lift breaks at n≥4; the max-at-boundary finite check needs re-verification at each level). The `f_n` conjecture is verified n=3 PROVED / n=4 PROVED / n≥5 OPEN.

**Scores:** Correctness 8/10 (finite computational check is legitimate but not structural); Completeness 7/10 (n=4 closed, n≥5 open, honestly flagged); Progress 8/10 (first n≥4 upper-bound closure, real milestone).

**Verdict: CHANGES REQUESTED.** The n=4 upper bound is a verified milestone, but the overall approach is still `partial` (lower bound + n≥5 open). The builder's status is accurate.

---

## 2. dyadic-induction — CHANGES REQUESTED (Status: partial)

**Claim:** Closed the `s = 3` piece of the G1-i-HC crux for ALL `n ≥ 3` (Lemma 16, PROVED). Plus Lemma 13 (clean measure form (★) `Ψ ≤ T_n`), Lemma 14 (tower-prefix tight), Lemma 15 (sliding/exchange). General `s ≥ 4` remains CONJECTURED+verified.

### Independent verification

1. **(★) identity** `D − 1 = 2·(T_n − Ψ)` (equivalently `Alt_s − target = T_n − Ψ`): Verified exact-rational `n=3..6`, 1500 configs each. The identity `D−1 = 2(T_n−Ψ)` holds EXACTLY (factor of 2 from the inclusion-exclusion `/2` in the target). The bound direction `D ≥ 1 ⟺ Ψ ≤ T_n` is correct (both sides same sign, 0 sign mismatches). ✓

2. **Tower-prefix tight** (Lemma 14): `Ψ(F*) = T_n` exactly at `F* = {2^{n−2}, 2^{n−3}, 2^{n−1−s}}` for `s = n−1`. Verified `n=3,4` (tight, `T_n−Ψ=0, D=1`); `n=5,6,7` (slack `T_n−Ψ = {1,2,5}`, `D = {3,5,11}`). ✓ Matches the claim "tight iff s = n−1".

3. **`[0,m]` swap** (Lemma 13 reading 2): `E_R0(n) ∩ [0, m] = O_R0(n−1)` and `O_R0(n) ∩ [0, m] = E_R0(n−1)` for `m = 2^{n−2}`. Verified `n=3..6`, exact match. ✓

4. **`T_n − T_{n−1} = |E| = D_R0(n−1)`** identity. Verified `n=3..6`, exact. ✓

5. **Spill-case reduction** (Lemma 16 Case II, the KEY step): `f_1 > m` ⟹ `E(f_1) = |E|` (saturated), and the `[0,m]` swap gives `O(f_2) = E_{n−1}(f_2)`, `E(f_3) = O_{n−1}(f_3)`, so `Ψ = |E| + Ψ_{n−1}(F'={f_2,f_3})`. Verified on concrete example (`n=4, F={5,2,1/2}`): `E(f_1)=3=|E|`, `O(f_2)=1=E_{n−1}(f_2)`, `E(f_3)=1/2=O_{n−1}(f_3)`, `Ψ = 9/2 = |E| + Ψ_{n−1}`. ✓ The reduction to Lemma 8 (s=2, CERTIFIED) at `n−1` is sound.

6. **s=3 bound**: 0 violations `n=3..7` (exact-rational, 2000 configs each). Min slack 0 at `n=3,4` (tight tower-prefix), positive slack `{1,2,5}` at `n={5,6,7}`. ✓ Matches the builder's claims exactly.

7. **No-spill cases (I.a, I.b.1, I.b.2)**: the bound holds (verified in the sweep). The `D_R0` identities (`D_R0(n−2) = m/2 − D_R0(n−3)`, `D_R0(n−1) = m/2 + D_R0(n−3)`) are correct (verified from the band structure). The crude bounds in I.a and the constant-`O(f_2)` trick in I.b.2 are sound. ✓

### Assessment

Lemma 16 is **PROVED and VERIFIED**. The `s=3` all-`n` closure is a genuine advance — it generalizes the `n=4, s=3` sliver witness (§4.8) from a tightness statement to a full closure. The clean (★) reformulation (Lemma 13) decouples the `W`-dependence and is a correct, verified identity. The tower-prefix tightness (Lemma 14) and sliding/exchange (Lemma 15) are correct.

**Status:** `partial` (builder's assessment is accurate). The general `s ≥ 4, n ≥ 4` G1-i-HC bound remains CONJECTURED+verified (the W-sum coupling is the open crux — honestly flagged). G1-iii-a (3 failed mechanisms, needs a 4th), G1-iii-b (flat, open), G1-ii (conditional on rest-split) all OPEN. `splits-inequality.md` stays PARTIAL.

**What's missing:** The general `s ≥ 4` W-sum coupling (superincreasing surplus must dominate multi-breakpoint compensation). The `s=3` closure works because its coupling is a single secondary breakpoint (absorbed by the Lemma-8 reduction); `s ≥ 4` has multi-breakpoint coupling. G1-iii-a needs a FOURTH mechanism (peeling-pair, continuity, peeling-recursion ALL failed; bound TRUE, proof OPEN). G1-iii-b (flat twin) OPEN.

**Scores:** Correctness 9/10 (Lemmas 13-16 all verified, the (★) identity exact); Completeness 7/10 (s=3 closed, s≥4 + iii-a/b + ii open); Progress 8/10 (real gap closed — s=3 all-n).

**Verdict: CHANGES REQUESTED.** Real progress (s=3 all-n closed), but the general s≥4 and other sub-cases remain open. Builder's status is accurate.

---

## 3. parity-xor-reachability — CHANGES REQUESTED (Status: partial, NOT solved) ★ HIGHEST-STAKES ★

**Claim:** `Status: solved` — full G1 lower bound `D ≥ 1/D_n` PROVED for ALL `n ≥ 1`, ALL sub-cases (i, ii, iii-a, iii-b), via a single F_2/XOR-measure induction on `n`. Engine: reverse triangle inequality `|g ⊕ 1_I| ≥ ||g| − |I||`.

### The fatal gap (toggle decomposition)

The proof's induction step (§5) decomposes `h = h_{2^n} ⊕ h_rest`, where `h_{2^n}` is the toggle on piece `2^n` and `h_rest` is "the XOR of the remaining ≤ n−1 toggles on `{1, …, 2^{n−1}}` (support ⊆ [0, 2^{n−1}])". The proof's §3 claims: **"Every toggle `h_p` with `p ≤ 2^{n−1}` has support ⊆ [0, p] ⊆ [0, 2^{n−1}], so `h_p = 0` on `B`"** and concludes **`h_rest = 0` on `B`**.

**This is FALSE when Xiang splits a large fragment of `2^n`.** A fragment of `2^n` can have length `p` with `2^{n−1} < p < 2^n` (e.g., `8 → 5 + 3` at `n=3` gives fragment `5 > 4 = 2^{n−1}`). If Xiang then splits this fragment (say `5 → 2.5 + 2.5`), the toggle `h_5 = 1_{[0, 2.5)} + 1_{[2.5, 5)}` has support `[0, 5)`, which reaches into `B = (4, 8]` on `(4, 5)`. This toggle is NOT `h_{2^n}` (it's not on the original piece `2^n = 8`), and it is NOT in `h_rest` as the proof defines it (its support is NOT ⊆ `[0, 2^{n−1}] = [0, 4]`).

**Concrete demonstration (n=3):** Xiang splits `8 → 5 + 3` (toggle `h_8`), then `5 → 2.5 + 2.5` (toggle `h_5`). The proof's Case C1 (`y = 4 − 3 = 1 ≥ 1`) claims residual on `B = (4, 8]` equals `y = 1`. **Actual residual on `B` = 0**: `f_3 = 1` on `B`, `h_8|_B = 1_{[5,8)}`, `h_5|_B = 1_{(4,5)}`, so `h|_B = 1` on `(4,8)`, giving `f_3 ⊕ h = 0` on `B`. The proof's `y = 1` is **wrong by 1** (the toggle on the large fragment `5` cancels the residual on `B` that the proof attributes solely to `h_{2^n}`). Total `D = 2 ≥ 1` (the bound holds — the residual on `L = [0,4]` compensates), but the proof's decomposition-based reasoning does NOT establish this.

**Why this is fatal:** The induction's case analysis (Case A: residual on `B = 2^{n−1}`; Case B/C1/C2: residual on `B = y`) ALL depend on `h_rest = 0` on `B`. When `h_rest ≠ 0` on `B` (Xiang splits a large fragment of `2^n`), the residual on `B` is NOT `y` (or `2^{n−1}`), and the entire Case analysis breaks. The induction does not cover all Xiang strategies — it only covers strategies where ALL non-`2^n` toggles are on pieces `≤ 2^{n−1}`. This misses the G1-iii-a sub-case (where `2^n` is split into ALL small fragments, some of which may be re-split) and many G1-i configurations (where `2^n → M + F` with `M > 2^{n−1}`, then `M` is re-split).

### The §9.6 "min D = 1 + 2y" claim is also FALSE

The proof's §9.6 claims: "Case C2 (non-EH, `0 < y < 1`): min `D = 1 + 2y > 1`" with pattern `n=3: y=1/2 → 2, y=1/4 → 3/2, …`

**Counterexamples (independently computed):**
- `n=2, y=0.5` (Xiang splits only `4 → 1.5 + 2.5`): pieces `{2.5, 2, 1.5, 1}`, `D = 2.5 − 2 + 1.5 − 1 = 1.0`. Proof claims `1 + 2(0.5) = 2`. **Actual = 1, not 2.**
- `n=3, y=0.5` (Xiang splits `8 → 4.5 + 3.5`, then `3.5 → 2.5 + 1`): pieces `{4.5, 4, 2.5, 2, 1, 1}`, `D = 4.5 − 4 + 2.5 − 2 + 1 − 1 = 1.0`. Proof claims `2`. **Actual = 1.**

The "min D = 1 + 2y > 1 in C2" claim is wrong — equality `D = 1` is attained at non-EH points (`y > 0`). The §9.6 verification script had a bug (likely tested single-toggle-only or a restricted strategy family).

### What IS correct (real progress)

1. **Band structure of `f_n`** (§2): verified `n=1..6`, correct. `f_n = 1` on `B = (2^{n−1}, 2^n]`, alternates band-by-band. ✓
2. **Complement-on-L identity** (§2): `f_n = (1 − f_{n−1})` on `L = [0, 2^{n−1}]`, verified `n=1..5`. ✓ (Correct: `j_{Liu_n} = j_{Liu_{n−1}} + 1` on `L`.)
3. **XOR-measure reverse triangle inequality** (§4): `|g ⊕ q| = |g| + |q| − 2|g ∩ q| ≥ ||g| − |q||`. ✓ (Standard set identity `|A Δ B| ≥ ||A| − |B||`; the proof's derivation is correct.)
4. **The bound `D ≥ 1` is TRUE** (verified by brute force `n=2..4`, min `D = 1`).
5. **The toggle decomposition `h = h_{2^n} ⊕ h_rest` IS valid** when all non-`2^n` toggles are on pieces `≤ 2^{n−1}` (the restricted case). The induction is correct for this restricted case.

### Why the gap is not easily closable

The proof's engine (reverse triangle inequality `|g ⊕ 1_I| ≥ |g| − y`) is applied to `g = f_{n−1} ⊕ h_rest`, where `h_rest` is the residual on `L`. But when `h_rest` has components on `B`, the residual on `B` is NOT `y`, and the clean split `D = y + |g ⊕ 1_I|` fails. To fix this, the proof would need to account for the interaction between `h_rest`'s `B`-components and the residual decomposition — the current framework (decompose by "toggle on `2^n` vs rest") cannot do this because "rest" is not cleanly separated by `B`/`L` when fragments of `2^n` are re-split.

A possible fix: decompose the residual on `B` and `L` directly (not by toggle), using `f_n = 1` on `B` and `f_n = (1−f_{n−1})` on `L`. But this loses the `(n−1)`-instance structure on `L` (since `h`'s `L`-component includes parts of toggles that also reach `B`). The induction on `n` does not cleanly recurse.

### Assessment

**The proof does NOT establish `D ≥ 1` for all `n` and all sub-cases.** The toggle decomposition is invalid for a broad class of Xiang strategies (those involving re-splitting large fragments of `2^n`). The builder's `Status: solved` is an **overclaim**. The true Status is **`partial`**.

The approach has **real progress**: the structural facts (band structure, complement-on-L, reverse triangle inequality) are correct and potentially useful tools. But the induction has a fatal gap that prevents it from closing the lower bound. The claim of "uniform applicability across all G1 sub-cases (i, ii, iii-a, iii-b)" is **unjustified** — the proof doesn't even correctly handle all G1-i configurations (those where `M > 2^{n−1}` is re-split).

**Scores:** Correctness 4/10 (structural facts correct, but the load-bearing induction step is broken); Completeness 3/10 (the main theorem is not proved; the gap is fatal); Progress 5/10 (correct tools introduced, but the assembly is broken).

**Verdict: CHANGES REQUESTED.** Real progress (correct structural framework, reverse triangle inequality), but the induction has a fatal gap. The builder's `Status: solved` is overclaimed — must be downgraded to `partial`.

**The specific gap to close:** The toggle decomposition `h = h_{2^n} ⊕ h_rest` must account for toggles on LARGE FRAGMENTS of `2^n` (fragments `> 2^{n−1}` that Xiang re-splits). These toggles have support reaching into `B`, breaking the proof's residual-on-`B` computation. The induction must either (a) handle these toggles explicitly, or (b) use a different decomposition that cleanly separates `B`/`L` residuals regardless of which pieces Xiang splits.

---

## Certification decisions

### Certified (new lemmas)

1. **`lemmas/case-c-n4.md`** (NEW, from pairing-charging Theorem 7): n=4 very-flat upper-bound closure. `f_4 ≤ 1/31` on `Π_4^{cl}`, tight at dyadic `p*`. Mechanism: PWL max-at-boundary (94 arrangement hyperplanes, finite `C(94,4)` "no interior cell-vertices" check, all boundary facets PROVED). **Rigor caveat**: the "no interior cell-vertices" step is a finite computational check (verified), not a structural proof. Verified independently: `f_4(p*)=1/31` exact, 0 violations on 5000+ configs, near-dyadic `f_4 = 1/31−2ε` exact.

2. **`lemmas/xor-reverse-triangle.md`** (NEW, from parity-xor-reachability §4): XOR-measure reverse triangle inequality `|g ⊕ q| ≥ ||g| − |q||` for indicators. Standard set identity, correctly derived. CERTIFIED as a reusable standalone tool. (The G1 F_2-form induction that USES this tool is NOT certified — it has the fatal toggle-decomposition gap.)

3. **`lemmas/splits-inequality.md`** (UPDATED, from dyadic-induction): stays PARTIAL. Lemmas 13 (★ identity `Ψ ≤ T_n ⟺ D ≥ 1`), 14 (tower-prefix tight), 15 (sliding/exchange), 16 (s=3 all-n G1-i-HC) all PROVED + verified + certified as components. The general `s ≥ 4` bound, G1-iii-a, G1-iii-b, G1-ii rest-split all remain OPEN (honestly flagged).

### NOT certified (rejected)

1. **G1 (splits-inequality, F_2/XOR-measure form)** from parity-xor-reachability: **REJECTED** — the induction has the fatal toggle-decomposition gap (§3's claim `h_rest = 0` on `B` is false when Xiang re-splits a large fragment of `2^n`). Do NOT replace `splits-inequality.md` with this version.
2. **Complement-on-L identity** from parity-xor-reachability: correct standalone, but I am NOT creating a separate lemma file for it since its primary use (the broken induction) is uncertified. The identity is verified and noted in the review; future approaches may re-derive it.

---

## Overall problem status

**NOT solved.** The problem remains `partial` overall:
- **Lower bound (G1):** PROVED for `n ≤ 2` (all sub-cases). For `n ≥ 3`: G1-i-HC closed for `s ≤ 3` (Lemma 16, all `n ≥ 3`) and `n = 3` all `s` (Lemma 12); general `s ≥ 4, n ≥ 4` CONJECTURED+verified; G1-iii-a OPEN (3 failed mechanisms); G1-iii-b OPEN (flat); G1-ii conditional. The `parity-xor-reachability` claim of a full G1 closure is **REJECTED** (fatal gap).
- **Upper bound (G2):** PROVED for `n = 1, 2, 3` (Theorem 6 + Cor 6.1, certified) and **`n = 4`** (Theorem 7 + Cor 6.2, certified this round — finite computational milestone). For `n ≥ 5`: very-flat regime OPEN (`f_n` conjecture, verified n=3,4, unverified n≥5).

The answer `c(n) = 2^n/(2^{n+1}−1)` is **ESTABLISHED for `n = 1, 2, 3, 4`** (both bounds proved: lower by dyadic-induction Cases A/B/C + Lemma 8/12/16; upper by case-c-n3 + case-c-n4). For `n ≥ 5`, both bounds remain OPEN.
