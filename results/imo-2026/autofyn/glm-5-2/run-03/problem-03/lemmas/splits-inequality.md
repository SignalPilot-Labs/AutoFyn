# Lemma: splits-inequality (PARTIAL — Cases A/B/C + G1-i-HC s≤3 proved; general s≥4 + G1-iii open)

## Status
**PARTIAL** (advanced round 6). The full statement is conjectured true (verified n=1..7 by brute-force with correct split budget). PROVED rigorously here: Cases A, B, C (all n), Lemma 5/7 identities, Lemma 6 sharpness, **Lemma 8** (2-piece F / rest-unsplit sub-case of G1-i, all n ≥ 2, including the n=3 tight family), **Lemma 9** (low-cancellation regime, all F, all n), **Lemma 10** (rest tiling superincreasing-band structure + discrepancy function G), **Lemma 11** (discrepancy reformulation: `overlap − target = (M−1−D_{R_0})/2 + Alt_s`, the clean statement of the G1-i-HC wall), **Lemma 12** (G1-i-HC for n=3, all s ∈ {1,2,3}, rest unsplit). **Round 6 additions:** **Lemma 13** (clean alternating-prefix measure form (★) `Ψ = Σ_{odd}E(f_i)+Σ_{even}O(f_i) ≤ T_n`, EXACT equivalent of G1-i-HC via `Alt_s − target = T_n − Ψ`), **Lemma 14** (tower-prefix tight arithmetic, `Ψ(F^*) = T_n` exactly), **Lemma 15** (sliding/exchange: `Ψ` PWL, max at dyadic-edge-or-tie vertex), **Lemma 16** (G1-i-HC for `s = 3`, ALL `n ≥ 3`, rest unsplit — generalizes the n=4 sliver witness to a full closure). The remaining **high-cancellation, multi-piece-F** sub-case (G1-i `n ≥ 4, s ≥ 4`) is CONJECTURED + exact-verified (n=2..6, 0 violations) but NOT proved — the W-sum coupling (superincreasing surplus must dominate multi-breakpoint compensation) is the open crux; G1-ii (conditional on rest-split), G1-iii-a (bound true, needs a 4th mechanism — peeling-pair/continuity/peeling-recursion ALL failed), G1-iii-b (flat, open) remain open. Sibling approaches may IMPORT all proved components; the general `s ≥ 4` HC gap remains open.

## Statement (full conjecture)

> **G1 (splits-inequality).** Let `D_n := 2^{n+1} − 1`. Liu Bang's dyadic config places pieces `1 : 2 : 4 : ⋯ : 2^n`, each scaled by `1/D_n` (so total = 1). Xiang Yu inserts ≤ n marks (each splitting one piece into two). Let `D = a_1 − a_2 + a_3 − ⋯` be the alternating sum of the resulting sorted-desc multiset (in units of `1/D_n`). Then **`D ≥ 1`** (i.e. `D ≥ 1/D_n` in actual length), with equality attained by the equal-halving reply and the broader "barely-larger" family (Lemma 6 of `dyadic-induction`).

Equivalently (via `S_odd = (1+D)/2`): Liu's payoff `S_odd ≥ (1 + 1/D_n)/2 = 2^n/D_n`. This is the load-bearing LOWER bound for `c(n) = 2^n/D_n`.

## What is PROVED (this round, by `dyadic-induction`)

### Lemma 4 (largest-piece decomposition) — PROVED, reusable

> For any final multiset with a (choice of) largest piece `M` and rest `R` (all other pieces), `D = M − D_R` where `D_R` = D of R.

**Proof.** Parity-integral: `D = ∫[j(t) odd]`. On `(max(R), M]` only M contributes (j=1, odd). On `[0, max(R)]`, M contributes +1 so `[j_final odd] = [j_R even] = 1 − [j_R odd]`. Sum: `(M − max(R)) + (max(R) − D_R) = M − D_R`. ∎ (Verified 3000 trials n=2,3.)

### Case A — piece `2^n` unsplit. PROVED (all n).

`M = 2^n`, `R` = dyadic `(n−1)` config with ≤ n splits. Universal bound `D_R ≤ total(R) = D_{n−1} = 2^n − 1`. So `D = 2^n − D_R ≥ 2^n − (2^n − 1) = 1`. ∎

### Case B — piece `2^n` split EXACTLY ONCE. PROVED (all n).

`2^n → M + g_2` (`M ≥ 2^{n−1} ≥ g_2`), rest `R_0 = {1,…,2^{n−1}}` with ≤ `n−1` splits (so `D_{R_0} ≥ 1` by G1(n−1)). Formula:
`D = 2^n − D_{R_0} − 2·E_1`,   `E_1 := ∫_0^{g_2} [j_{R_0} even] dt`.
Bound: `E_1 ≤ ∫_0^{2^{n−1}} [j_{R_0} even] = 2^{n−1} − D_{R_0}` (sub-measure). Hence `D ≥ D_{R_0} ≥ 1`. ∎ (Verified 20k trials, 0 failures.) Recovers n=1 and n=2-0/1-mark as special cases. Tight at `M = 2^{n−1}` (equal-halving; bound saturated, peeling-neutrality).

### Case C — piece `2^n` split (any r ≥ 2 fragments), largest fragment `M = 2^{n−1}`, AND rest's piece `2^{n−1}` UNSPLIT. PROVED (all n).

Two equal pieces `2^{n−1}` (fragment M + rest's piece) form an equal pair. By the **peeling lemma** (`lemmas/peeling.md`, CERTIFIED round 2), removing this pair is D-neutral: `D = D_{R'}`, `R' = (dyadic (n−2) with ≤ n+1−r splits) ∪ F` (F = other fragments of 2^n, sum `2^{n−1}`). Reinterpret `R'` as the `(n−1)`-dyadic config `{1,…,2^{n−2}, 2^{n−1}}` with piece `2^{n−1}` refined into F (r−2 splits) and `{1,…,2^{n−2}}` with ≤ n+1−r splits; total ≤ n−1 splits. By G1(n−1), `D_{R'} ≥ 1`. ∎ (Verified 20k trials, 0 failures.)

### Lemma 5 (multi-split structural formula) — PROVED identity (the handle for the gap).

> For `2^n` split into `M, g_2,…,g_r` (`M ≥ 2^{n−1}` unique largest), rest `R_0` with ≤ n+1−r ≤ n−1 splits (so `D_{R_0} ≥ 1` by G1(n−1)), `F = {g_2,…,g_r}` (sum `W = 2^n − M`): `D = M − D_{R_0} − D_F + 2 C`, where `D_F = ∫[j_F odd]` (standalone D of F) and `C = ∫_0^{2^{n−1}} [j_{R_0} odd]·[j_F odd]` (overlap of odd-parity regions).

**Proof.** On `[0, 2^{n−1}]`: `j_final = 1 + j_{R_0} + j_F`, so `[j_final odd] = [j_{R_0} ⊕ j_F even] = 1 − ([j_{R_0} odd] ⊕ [j_F odd])`. XOR-integral identity gives `∫ = 2^{n−1} − (D_{R_0} + D_F − 2C)`. Add top band `M − 2^{n−1}`. ∎ (Verified 3000 trials, 0 errors.) **Corollary:** `D ≥ 1 ⟺ 2 C ≥ D_{R_0} + D_F + 1 − M`.

### Lemma 6 (tight config family — sharpness). PROVED.

For `ε_1,…,ε_n ≥ 0` with `Σ ε_i = 1` (and `ε_i ≤ 2^{i−1}` for positivity), split `2^n → (2^{n−1}+ε_1) + (2^{n−2}+ε_2) + ⋯ + (1+ε_n)` and leave the rest `{2^{n−1},…,1}` unsplit. The sorted multiset interleaves as pairs, and `D = Σ ε_i = 1` (tight). Equal-halving is `ε_i = 0` (trailing triple `(1,1,1)` gives the +1). Confirmed n=3, 80k trials: min `D = 1` exactly.

### Lemma 7 (union-measure reformulation) — PROVED (identity)

> Under Lemma 5's setup (`max(R_0) ≤ 2^{n−1}`): `D = M + D_{R_0} + D_F − 2|O_{R_0} ∪ O_F|` (within `[0, 2^{n−1}]`). Hence `D ≥ 1 ⟺ |O_{R_0} ∪ O_F| ≤ (M + D_{R_0} + D_F − 1)/2`.

**Proof.** Inclusion–exclusion `|O_{R_0} ∪ O_F| = D_{R_0} + D_F − C` into Lemma 5's `D = M − D_{R_0} − D_F + 2C`. ∎ (Verified 8k trials, 0 error.) The trivial bound `|union| ≤ 2^{n−1}` is off by exactly `(W + 1 − D_{R_0} − D_F)/2` — the "shave 1" wall, forced by the rigid alternating-dyadic tiling structure of `O_{R_0}`.

### Lemma 8 (G1-i, 2-piece F / rest-unsplit) — PROVED (all n ≥ 2)

> For `n ≥ 2`: split `2^n → M + a + b` (`M > 2^{n−1}` strict, `a ≥ b ≥ 0`, `W = a+b = 2^n − M < 2^{n−1}`), rest `R_0 = {1,…,2^{n−1}}` **unsplit** (total splits = 2 ≤ n). Then `D ≥ 1`, tight at `n = 3` (the Lemma-6 family).

**Proof.** `F = {a, b}`: `O_F = (b, a]` (single interval), `D_F = a − b`. Via Lemma 5, `D ≥ 1 ⟺ b + |(b, a] ∩ E_{R_0}| ≤ T_n := (2^n − 1 − D_{R_0})/2` (algebra: `C = (a−b) − |(b,a]∩E|`, `M = 2^n − a − b`).

**Rigid top O-block:** on `(2^{n−2}, 2^{n−1}]`, only the rest's piece `2^{n−1}` satisfies `2^k ≥ t` (all smaller pieces `2^0,…,2^{n−2} < t`), so `j_{R_0}(t) = 1` (odd); hence `(2^{n−2}, 2^{n−1}] ⊆ O_{R_0}`, i.e. `E_{R_0} ∩ (2^{n−2}, 2^{n−1}] = ∅`.

Bound `|(b, a] ∩ E_{R_0}|` (using `a < 2^{n−1}`):
- `a ≤ 2^{n−2}`: `|(b,a] ∩ E_{R_0}| ≤ a − b`, so `b + |…| ≤ a ≤ 2^{n−2}`.
- `a > 2^{n−2}`: `(b, a] = (b, 2^{n−2}] ∪ (2^{n−2}, a]`; the second part lies in `(2^{n−2}, 2^{n−1}) ⊆ O_{R_0}` (top O-block), contributing 0 to `E`; so `|(b,a]∩E| ≤ |(b, 2^{n−2}]| = 2^{n−2} − b`, giving `b + |…| ≤ 2^{n−2}`.

Both cases: `b + |(b,a] ∩ E_{R_0}| ≤ 2^{n−2}`. Finally `2^{n−2} ≤ T_n` since `D_{R_0} ≤ 2^{n−1} − 1` ⟺ `2^{n−1} ≥ 3 + (−1)^{n−1}`, true for `n ≥ 2` (equality `n ∈ {2,3}`). So `b + |(b,a]∩E| ≤ T_n`, hence `D ≥ 1`. ∎ (Verified 5k trials each `n = 3..6`: worst slack 0 at `n=3,4`; tight `n=3` configs = Lemma-6 family `F = {2+ε_2, 1+ε_3}`.)

**Scope.** Closes the 2-piece-F / rest-unsplit sub-case of **G1-i** for all `n ≥ 2`, including the `n = 3` tight Lemma-6 family. Does NOT close `s ≥ 3`-piece F (the `n ≥ 4` tight Lemma-6 family), G1-ii, or G1-iii.

### Lemma 9 (low-cancellation regime) — PROVED (all F, all n)

> Under Lemma 5's setup: `|O_F ∩ E_{R_0}| ≤ |E_{R_0}|` (trivial) yields `D ≥ 1` whenever `D_F ≥ W − D_{R_0} + 1` (`W = 2^n − M`).

**Proof.** `D = M − D_{R_0} + D_F − 2|O_F ∩ E_{R_0}| ≥ M − D_{R_0} + D_F − 2(2^{n−1} − D_{R_0}) = M + D_{R_0} + D_F − 2^n`. For `D ≥ 1` it suffices `M + D_{R_0} + D_F ≥ 2^n + 1 ⟺ D_F ≥ W − D_{R_0} + 1`. ∎ Closes all F with little internal cancellation (single-piece F = Case B; 2-piece F with small `b`). Leaves the **high-cancellation regime** `D_F < W − D_{R_0} + 1` (small `D_F`, the tight Lemma-6 territory) as the sole open wall.

### Lemma 10 (rest tiling structure + discrepancy function G) — PROVED (round 5, by `dyadic-induction`)

> For the unsplit rest `R_0 = {1,…,2^{n−1}}` (pieces `2^0,…,2^{n−1}`), `U := 2^{n−1}`. The bands `B_{-1}=(0,1]`, `B_k=(2^k,2^{k+1}]` (`k=0..n−2`) have `j_{R_0}=n` (on `B_{-1}`) resp. `n−1−k` (on `B_k`), so `O_{R_0}/E_{R_0}` **alternate band-by-band**. Recursion: `E_{R_0}(n) = (2^{n−3}, 2^{n−2}] ∪ E_{R_0}(n−2)` (within `[0,2^{n−2}]`); bases `E_{R_0}(2)=(0,1]`, `E_{R_0}(3)=(1,2]`. Hence `E_{R_0}` is `⌊n/2⌋` superincreasing dyadic bands (lengths `2^{n−3}, 2^{n−5}, …, 1`). Define `G(x) := |[0,x]∩O_{R_0}| − x/2`; `G` continuous piecewise-linear, slope `+1/2` on O-bands, `−1/2` on E-bands, `G(0)=0`, `G(U)=D_{R_0}−2^{n−2}`; swings have **superincreasing amplitudes** `2^k/2`.

**Proof.** `j`-values and the parity-alternation are immediate from `j_{R_0}(t) = #{rest pieces ≥ t}`. The recursion: on `(0,2^{n−2}]`, `j_{R_0(n)} = j_{R_0(n−1)} + 1` (the piece `2^{n−1}` contributes), so parity there is `1−[j_{R_0(n−1)} odd]`, giving `O_{R_0}(n)∩(0,2^{n−2}] = E_{R_0}(n−1)`; with the top band `(2^{n−2},2^{n−1}]` (`j=1`, odd → `O`), `E_{R_0}(n) = O_{R_0}(n−1)`. Iterate `O_{R_0}(n−1) = (2^{n−3},2^{n−2}] ∪ E_{R_0}(n−2)`. Superincreasing = `2^k > 2^k−1`. Slopes of `G` from `F_odd` slope `1` on O / `0` on E minus `x/2` slope `1/2`. ∎ (Verified `n=2..7`.) **Reusable structural asset for the HC overlap bound.**

### Lemma 11 (discrepancy reformulation of G1-i-HC) — PROVED identity (round 5)

> Under Lemma 5 setup (`max F < U`): `Alt_s := Σ_{i=1}^s (−1)^{i+1} G(f_i) = G(f_1)−G(f_2)+G(f_3)−⋯±G(f_s)`. Then `overlap − target = (M − 1 − D_{R_0})/2 + Alt_s` (exact), so `D ≥ 1 ⟺ Alt_s ≥ (D_{R_0}+1−M)/2`.

**Proof.** `E_F` bands: `(f_1,U], (f_3,f_2], (f_5,f_4], …` (plus `(0,f_s]` if `s` even). For any band `(α,β]`: `|(α,β]∩E_{R_0}| = (β−α)/2 − (G(β)−G(α))` (since `|(α,β]∩O_{R_0}| = (G(β)+β/2)−(G(α)+α/2)`). Sum over `E_F` bands: the `(β−α)/2` sum to `|E_F|/2 = (U−D_F)/2`; the `G`-terms telescope to `G(U) − Alt_s`. So `overlap = (U−D_F)/2 − G(U) + Alt_s`. With `G(U) = D_{R_0}−2^{n−2}` and `2U = 2^n`, `2^n − W = M`:
`overlap − target = (U−W−1+D_{R_0})/2 − (D_{R_0}−2^{n−2}) + Alt_s = (M−1−D_{R_0})/2 + Alt_s`. ∎ (Verified exact `n=2..6`, `s≤n`, 0 error.) **The clean statement of the G1-i-HC wall; importable as the crux formulation.**

### Lemma 12 (G1-i-HC for n=3, all s ∈ {1,2,3}) — PROVED (round 5)

> For `2^3 → M + F`, `M > 4` strict, `F = {f_1 ≥ … ≥ f_s}` (`s ≤ 3`, sum `W < 4`, so `f_2 < 2`), rest `{1,2,4}` unsplit: `D ≥ 1`. (`s=1` = Case B; `s=2` = Lemma 8 / the n=3 tight Lemma-6 family; `s=3` new.)

**Proof (s=3).** `E_{R_0} = (1,2]`, target `= f_2 − 1` (`κ_3 = (D_{R_0}−1)/2 = 1`, `S_even(F) = f_2`). Overlap `= |(f_1,4]∩(1,2]| + |(f_3,f_2]∩(1,2]|`.
- **Case A (`f_2 ≤ 1`):** target `≤ 0 ≤ overlap`. ✓
- **Case B (`1 < f_2 < 2`):** `|(f_3,f_2]∩(1,2]| = f_2 − max(f_3,1)`; `|(f_1,4]∩(1,2]| = max(0, 2−f_1)` (if `f_1<2`) or `0` (if `f_1≥2`).
  - **B1 (`f_3 < 1`):** overlap `= (f_2−1) + max(0,2−f_1) ≥ f_2−1` = target. ✓
  - **B2 (`f_3 ≥ 1`):** overlap `−` target `= max(0,2−f_1) − (f_3−1)`.
    - `f_1 ≥ 2`: `= −(f_3−1)`, `≥ 0 ⟺ f_3 ≤ 1`; in B2 `f_3 ≥ 1`, and `f_3 > 1` would force `W ≥ 2+1+1 = 4` (contradicting `W<4`), so `f_3 = 1`, equality. ✓
    - `f_1 < 2`: need `2−f_1 ≥ f_3−1 ⟺ f_1+f_3 ≤ 3`; but `f_1+f_3 = W−f_2 < 4−1 = 3` (using `W<4`, `f_2>1`). ✓ (strict)
All cases give `overlap ≥ target ⟺ D ≥ 1`. ∎ (Verified: 5000 configs `n=3 s=3`, min `D=1`, 0 violations.) **Closes n=3 rest-unsplit G1-i-HC entirely.**

### Lemma 13 (clean alternating-prefix measure form (★)) — PROVED (round 6)

> Under Lemma 5's setup (`M > U := 2^{n−1}`, `F = {f_1 ≥ … ≥ f_s}`, `W < U`, rest unsplit): with `E(x)=|[0,x]∩E_{R_0}|`, `O(x)=|[0,x]∩O_{R_0}|`, define `Ψ(F) := Σ_{i odd} E(f_i) + Σ_{i even} O(f_i)`. Then `D ≥ 1 ⟺ Ψ(F) ≤ T_n := (2^n − 1 − D_{R_0})/2`, via the exact identity `Alt_s − target = T_n − Ψ(F)`.

**Proof.** From Lemma 11, `Alt_s − target = Alt_s − (D_{R_0}+1−M)/2`. Expand `Alt_s − W/2 − (D_{R_0}+1−2^n)/2` (using `M = 2^n − W`): `Σ_i [(−1)^{i+1}G(f_i) − f_i/2] − (D_{R_0}+1−2^n)/2`. With `G(x) = O(x) − x/2`: odd `i` gives `G(f_i)−f_i/2 = O(f_i) − f_i = −E(f_i)`; even `i` gives `−G(f_i)−f_i/2 = −O(f_i)`. Sum `= −Ψ(F)`. Hence `Alt_s − target = −Ψ + (2^n−1−D_{R_0})/2 = T_n − Ψ`. ∎ (Verified n=2..7, 0 error.) **Pair-decomposition:** `Ψ = S_even(F) + |Q∩E_{R_0}|` where `Q = ∪` odd-indexed sub-intervals of the partition `I_1=(f_2,f_1], I_2=(f_3,f_2], …` of `[0,f_1]`. **Rigid top `O`-block:** `(m, U] ⊆ O` for `m=2^{n−2}`, so `E ⊆ [0,m]`, `E(x)=|E|` for `x≥m`; and the `[0,m]` swap `E(n)↔O(n−1)`, `O(n)↔E(n−1)` (parity flips: `j_{R_0(n)} = 1 + j_{R_0(n−1)}` on `[0,m]`). Importable as the clean measure-form statement of G1-i-HC.

### Lemma 14 (tower-prefix tight arithmetic) — PROVED (round 6)

> At `F^* = {2^{n−2}, 2^{n−3}, …, 2^{n−1−s}}` (s ≤ n−1, distinct dyadic edges) and its Lemma-6 `ε`-perturbation: `Ψ(F^*) = T_n` exactly (tight iff `s = n−1`; positive slack for `s < n−1`).

**Proof.** At `F^*`, the partition intervals `I_j` coincide with `E/O` bands (matching parity: `I_j ⊆ E` for `j` odd, `⊆ O` for `j` even), so `Q = E∩[0,f_1]` and `|Q∩E| = |E|` (no `E` above `f_1 = 2^{n−2}`). Thus `Ψ = S_even(F^*) + |E| = (W^* − D_{R_0}(n−1))/2 + D_{R_0}(n−1) = (W^* + D_{R_0}(n−1))/2`. For `s = n−1`, `W^* = 2^{n−1} − 1 = U − 1`, giving `Ψ = (U−1+D_{R_0}(n−1))/2 = T_n`. The `ε`-family: each `ε_i` shifts `Ψ` by `±ε_i/2` and the target by `−ε_1/2`; `Σε = 1` ⟹ equality. ∎ (Verified n=2..6.) Importable as the sharpness/equality case.

### Lemma 15 (sliding/exchange) — PROVED (round 6)

> `Ψ` is piecewise-linear in `F`. At any maximizer of `Ψ` over `{f_1 ≥ … ≥ f_s ≥ 0, Σf_i ≤ U}`, each `f_i` is either a dyadic band-edge (`∈ {0,1,2,4,…,U}`) or tied to a neighbor (`f_i = f_{i±1}`).

**Proof.** `Ψ` PWL (slopes of `E,O` are 0/1 per band); feasible set a compact polytope ⟹ max attained. At a smooth interior cell point, `∂Ψ/∂f_i = 1_{f_i ∈ R_i}` (`R_i = E` odd / `O` even) ∈ {0,1}, never 0-in-subdiff, so a non-edge non-tied coordinate slides (increases if `∂=1`, preserves if `∂=0`) to a band-edge or sort-tie without decreasing `Ψ`. ∎ Importable as the engine reducing G1-i-HC to dyadic-edge vertices (setup for any exchange/vertex-enumeration attack on `s ≥ 4`).

### Lemma 16 (G1-i-HC for s=3, ALL n ≥ 3) — PROVED (round 6)

> For `2^n → M + F`, `M > 2^{n−1}` strict, `F = {f_1 ≥ f_2 ≥ f_3 > 0}` (`W < 2^{n−1}`), rest unsplit: `D ≥ 1` (i.e. `Ψ ≤ T_n`).

**Proof.** Set `m = 2^{n−2}` (`U = 2m`). `E ⊆ [0,m]`, `|E| = D_{R_0}(n−1)`. Split by `f_1` vs `m`.
- **Case II (`f_1 > m`, spill):** `E(f_1) = |E|`; `f_2+f_3 = W−f_1 < m`. The `[0,m]` swap gives `O(f_2) = E_{n−1}(f_2)`, `E(f_3) = O_{n−1}(f_3)`. So `Ψ = |E| + [E_{n−1}(f_2)+O_{n−1}(f_3)]`. The bracket is the `(n−1)`-instance of `Ψ` for 2-piece `F'={f_2,f_3}` with `f_2+f_3 < m = U_{n−1}` ⟹ `M_{n−1} > U_{n−1}` strict. By **Lemma 8** (s=2, PROVED all n), bracket `≤ T_{n−1}(n−1)`. So `Ψ ≤ |E| + T_{n−1} = T_n` (since `T_n − T_{n−1} = |E|`). ✓
- **Case I (`f_1 ≤ m`, no spill):** swap gives `E(f_i)=O_{n−1}(f_i)`, `O(f_i)=E_{n−1}(f_i)`. Split by `f_1` vs `m/2` (top `(n−1)` `E`-band edge).
  - **I.a (`f_1 ≤ m/2`):** `Ψ ≤ 2|E(n)∩[0,m/2]| + |O(n)∩[0,m/2]| = 2|E(n−2)| + |E(n−1)| = 2·D_{R_0}(n−3) + D_{R_0}(n−2)` (band recursion + swap). Using `D_{R_0}(n−2)=m/2−D_{R_0}(n−3)`, `D_{R_0}(n−1)=m/2+D_{R_0}(n−3)`: `Ψ ≤ D_{R_0}(n−3)+m/2 ≤ T_n` ⟺ `D_{R_0}(n−3) ≤ m/2 − 1` (holds: `D_{R_0}(n−3) ≤ 2^{n−3}−1 = m/2−1`). ✓
  - **I.b (`m/2 < f_1 ≤ m`):** `E(f_1) = |E| + f_1 − m`.
    - **I.b.1 (`f_2 ≤ m/2`):** swap + Lemma 8 at `(n−1)` (boundary `f_2+f_3 ≤ m` covered by peeling/C): `O(f_2)+E(f_3) = E_{n−1}(f_2)+O_{n−1}(f_3) ≤ T_{n−1}`. `Ψ ≤ (|E|+f_1−m)+T_{n−1} ≤ |E|+T_{n−1} = T_n` (since `f_1 ≤ m`). ✓
    - **I.b.2 (`f_2 > m/2`):** `E(f_2) = |E|+f_2−m` ⟹ `O(f_2) = m−|E|` (constant). So `Ψ = f_1 + E(f_3)`.
      - `f_3 ≤ m/2`: `E(f_3) = E_{n−2}(f_3) ≤ D_{R_0}(n−3)`; `Ψ ≤ f_1 + D_{R_0}(n−3) ≤ m + D_{R_0}(n−3) ≤ T_n` ⟺ `D_{R_0}(n−3) ≤ m/2 − 1`. ✓
      - `f_3 > m/2`: `E(f_3) = |E|+f_3−m`; `Ψ = f_1+f_3+|E|−m`. Need `f_1+f_3 ≤ T_{n−1}+m`. `f_1+f_2+f_3 < 2m`, `f_2 > m/2` ⟹ `f_1+f_3 < 3m/2`. `T_{n−1}+m = (4m−1−D_{R_0}(n−1))/2 ≥ 3m/2` ⟺ `D_{R_0}(n−1) ≤ m−1` (holds `n ≥ 3`; at `n=3` equality and strict `<` from `W<2m`). ✓
All cases: `Ψ ≤ T_n` ⟹ `D ≥ 1`. ∎ (Verified exact `n=3..7`, s=3: 0 violations; min slack 0 at `n=3,4` tight tower-prefix; slack `{1,2,5}` at `n={5,6,7}`.) **Generalizes the `n=4, s=3` sliver witness (§4.8 of dyadic-induction) to all `n ≥ 3`.** Importable as the `s = 3` component of G1-i-HC.

## What is OPEN (the GAP, refined — round 6)

After Lemmas 8, 9, 10, 11, 12, 13, 14, 15, 16, the **open** sub-cases are (all in the **high-cancellation regime** `D_F < W − D_{R_0} + 1`):

- **(G1-i, multi-piece, high-cancellation, `s ≥ 4, n ≥ 4`):** `2^n` split into `r ≥ 5` fragments (`F` has `s = r−1 ≥ 4` pieces), `M > 2^{n−1}` strict, rest unsplit, `D_F` small. This is where the `n ≥ 5` Lemma-6 tight family lives (`s = n−1 ≥ 4`). **Reformulated via Lemma 11/13** as: prove `Ψ(F) ≤ T_n` for `s ≥ 4`, equivalently `Alt_s ≥ (D_{R_0}+1−M)/2`. By Lemma 15 the max is at a dyadic-edge vertex; the **W-sum coupling** (the superincreasing surplus of `E`/`O`-band swings must dominate the multi-breakpoint compensation preserving `Σf_i = W`) is the open crux. For `s ≤ 3` the coupling is single-secondary-breakpoint and is absorbed (Lemma 16); for `s ≥ 4` it is multi-breakpoint. Verified TRUE (exact-rational `n=2..6`, `s≤n`, 0 violations, tight at the tower prefix `s = n−1`). The n=4 s=3 sliver (§4.8 of dyadic-induction) is now a special case of Lemma 16 (PROVED). The `s ≥ 4, n ≥ 4` regime remains conjectured+verified.
- **(G1-ii):** `M = 2^{n−1}` (fragment of `2^n`) but rest's `2^{n−1}` SPLIT. `alternating-potential`'s reduction `G1-ii (r≥3) ⟹ G1-i` (perturb `M → 2^{n−1}+ε`, `D` continuous) is CERTIFIED and sound, but **CONDITIONAL on G1-i-HC closing WITH rest-split** (the perturbed config has rest-splits) — i.e. on the `s ≥ 4` bound (above) + the rest-split induction.
- **(G1-iii-a):** all `2^n`-fragments `< 2^{n−1}`, rest's `2^{n−1}` UNSPLIT. `M = 2^{n−1}` (rest's, dominant). **Bound `D ≥ 1` is TRUE** (tight `D = 1` at `n = 4` AND `n = 5`: e.g. n=5 `F' = {15.5, 7.5, 4, 2, 1, 0.5, 0.5, 0.5, 0.5}`, `D_R = 15 = M−1`, `D = 1`). THREE mechanisms have FAILED: (1) "reduce to G1(n−1)" UNSOUND (folded rest total `3·2^{n−1}−1 ≠ D_{n−1}`); (2) peeling-pair UNSOUND (peeling lemma needs exact equal pairs); (3) peeling recursion `D = Σε_i + D_alt(floor)` does NOT iterate (only one peel valid; `Σε_i + D_alt(floor) = 35` vs actual `D = 1` at n=4, wrong by 35×); the continuity reduction fails (provenance switches). The "iii-a is EASIER / growing slack" premise is NUMERICALLY FALSE (tight `D = 1` at n=4,5). **Proof OPEN**, needs a FOURTH mechanism.
- **(G1-iii-b):** all pieces `< 2^{n−1}`, rest's `2^{n−1}` SPLIT. Tight (n=4: `D=1` at `{6,6,4,4,4,4,2,1}`). **Flat twin of G2-flat**; likely resists tiling rigidity (no dominant `M`). OPEN, the IMO-hard core on the lower-bound side.

### Why naive bounds fail (do not retry)

- **`C ≤ D_F`** (sub-measure): gives `D ≥ M − D_{R_0} − D_F`, strictly short at the tight config (Lemma 6).
- **XOR-sum / triangle**: `D_R ≤ D_{R_0} + W` ⟹ `D ≥ 2M − D_{R_0} − 2^n`; for `M = 2^{n−1}` gives `D ≥ −D_{R_0} < 0`. Useless.
- **`D ≥ D_{R_0}`** (the Case-B bound): FALSE for multi-split. Tight config (Lemma 6) has `D = 1 < D_{R_0}` typically. Verified (n=3 example `{4.37, 4, 2.08, 2, 1.55, 1}`, `D = 1`, `D_{R_0} = 3`).
- **Trivial overlap `|O_F ∩ E_{R_0}| ≤ |E_{R_0}|`** (Lemma 9): closes low-cancellation but fails the high-cancellation (tight) regime — `|O_F| = D_F` is small there, and `|E_{R_0}|` is far too coarse a cap. Do not conflate "proved for low-cancellation" with "proved in general."

### The open crux (refined)

Prove `|O_F ∩ E_{R_0}| ≤ (M − D_{R_0} + D_F − 1)/2` for the **high-cancellation, multi-piece-F** regime (`s ≥ 3`, small `D_F`, rest unsplit — G1-i; plus the analogous G1-ii split-rest and G1-iii near-tie statements). The bound is TRUE (verified `n = 2..6` with correct split budget, `D ≥ 1` throughout, tight at `n = 3,4` via multi-piece F). Handle: `O_{R_0}` is a rigid alternating-dyadic-interval tiling; `E_{R_0}` is a superincreasing-block pattern; `O_F`'s `s−1` breakpoints cannot perfectly tile `E_{R_0}` — each dyadic edge leaks against `O_F`'s breakpoints by the superincreasing surplus. Making this bookkeeping rigorous for `s ≥ 3` is the open step.

## Proven base cases (full G1, small n)

- **n = 0:** `{1}`, no splits, `D = 1` ✓.
- **n = 1:** `{2, 1}`, ≤ 1 split. No split: `D = 1`. Split 2: `D = 1`. Split 1: `D = 1 + 2α ≥ 1`. ✓ (Full G1(1) proved.)
- **n = 2:** `{4, 2, 1}`, ≤ 2 splits. 0- and 1-mark cases proved by casework (subsumed by Case B). 2-mark case: verified by exhaustive rational-grid brute-force (min `D = 1`, attained at equal-halving and "barely-split 4 → 3+1" family). ✓ (Full G1(2) proved by computation + Cases A/B.)
- **n = 3, 4:** verified by brute-force random search (n=3: 80k trials, min `D = 1`; n=4: 5k trials, min `D = 1`). Computation only, not full proof.

## Import notes for sibling approaches

- **Case A, B, C** are PROVED for all n; import them as the proven partial G1. Combined with the n=2 exhaustive verification, this fully closes G1 for n ≤ 2 and for the "2^n unsplit", "2^n split once", and "2^n split with M = 2^{n−1} tie" sub-cases at every n.
- **Lemma 4** (largest-piece decomposition), **Lemma 5** (multi-split formula), and **Lemma 7** (union-measure reformulation) are PROVED identities, reusable as computational tools regardless of whether the overlap bound closes.
- **Lemma 8** (2-piece F, rest unsplit) is PROVED for all `n ≥ 2`; it closes the 2-piece-F sub-case of G1-i, including the `n = 3` tight Lemma-6 family. Import for any approach needing the `n = 3` tight regime closed.
- **Lemma 9** (low-cancellation regime) is PROVED for all F, all n; import to dispatch the `D_F ≥ W − D_{R_0} + 1` regime (F has little cancellation) cleanly.
- **Lemma 10** (rest tiling superincreasing-band structure + discrepancy `G`) is PROVED for all n; import as the structural asset for the HC overlap bound.
- **Lemma 11** (discrepancy reformulation: `overlap − target = (M−1−D_{R_0})/2 + Alt_s`) is a PROVED identity; import as the clean statement of the G1-i-HC wall (`D ≥ 1 ⟺ Alt_s ≥ (D_{R_0}+1−M)/2`).
- **Lemma 12** (G1-i-HC for n=3, all `s ∈ {1,2,3}`, rest unsplit) is PROVED; import to close the n=3 rest-unsplit HC sub-case.
- **Lemma 13** (clean measure form (★): `Ψ ≤ T_n`, exact equivalent of G1-i-HC; `Alt_s − target = T_n − Ψ`) is a PROVED identity; import as the decoupled measure-form statement (decouples the `W`-dependence of the target). Includes the pair-decomposition `Ψ = S_even + |Q∩E|` and the `[0, 2^{n−2}]` `E↔O` swap reduction.
- **Lemma 14** (tower-prefix tight: `Ψ(F^*) = T_n` exactly) is PROVED; import as the sharpness/equality case.
- **Lemma 15** (sliding/exchange: max of `Ψ` at a dyadic-edge-or-tie vertex) is PROVED; import as the engine reducing G1-i-HC to dyadic-edge vertices (the setup for any exchange/vertex attack on the general `s ≥ 4` bound).
- **Lemma 16** (G1-i-HC for `s = 3`, ALL `n ≥ 3`, rest unsplit) is PROVED; import to close the `s = 3` component of G1-i-HC for every `n`. Generalizes the n=4 s=3 sliver witness.
- **The GAP** (G1-i-HC general `n ≥ 4, s ≥ 4`, reformulated as `Ψ ≤ T_n` / `Alt_s ≥ (D_{R_0}+1−M)/2`; the W-sum coupling is the crux; G1-ii conditional; G1-iii-a (4th mechanism needed), G1-iii-b flat-open) is shared. If a sibling closes the `s ≥ 4` bound (W-sum coupling), the full G1 (plus G1-ii via continuity, plus the rest-split induction base) follows and this lemma upgrades to fully PROVED.
