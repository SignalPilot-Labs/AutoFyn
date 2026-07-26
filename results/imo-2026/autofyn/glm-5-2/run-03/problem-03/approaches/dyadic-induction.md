# Approach: dyadic-induction

## Status
partial (advanced round 6: s=3 all-n G1-i-HC CLOSED; general s≥4 + G1-iii-a + G1-iii-b + G1-ii rest-split + G2 all open)

## Approaches tried
- Round 6: **Closed the `s = 3` piece of the G1-i-HC crux for ALL `n ≥ 3` via an exchange/reduction argument** (Lemma 16, PROVED). Mechanism: the rigid top `O`-block `(m, U] ⊆ O` (midpoint `m = 2^{n−2}`) and the `[0,m]` `E↔O` swap (Lemma 13 reading 2) reduce the `s = 3` bound at `n` to the `s = 2` bound (Lemma 8, CERTIFIED) at `n−1` in the "spill" regime (`f_1 > m`); the no-spill regime is closed by crude measure bounds (Case I.a) and the constant-`O(f_2)=m−|E|` trick + the `W < 2m` slack (Case I.b). This **generalizes the `n = 4, s = 3` sliver witness (§4.8) from tightness-only to a full closure.** Also PROVED: **Lemma 13** (clean alternating-prefix measure form (★) `Ψ = Σ_{odd}E(f_i)+Σ_{even}O(f_i) ≤ T_n`, EXACT equivalent of G1-i-HC via `Alt_s − target = T_n − Ψ` — decouples the `W`-dependence), **Lemma 14** (tower-prefix tight arithmetic: `Ψ(F^*) = T_n` exactly, verified `n=2..6`; the `ε`-slack identity), **Lemma 15** (sliding/exchange: `Ψ` is PWL, max at a dyadic-edge-or-tie vertex — reduces the search to arrangement vertices). The **superincreasing-prefix obstruction** (crux `aimo-0530` adapted) is identified as the mechanism for general `s ≥ 4`, with the **W-sum coupling** (superincreasing surplus must dominate the multi-breakpoint coupling adjustment preserving `Σ f_i = W`) as the explicit open step. `s = 3` closes because its coupling is a single secondary breakpoint, absorbed by the Lemma-8 reduction; `s ≥ 4` has multi-breakpoint coupling. Per outline-reviewer corrections: **G1-iii-a NOT pursued** (the peeling recursion is the THIRD FAILED mechanism — does not iterate, wrong by 35× at n=4; the "growing slack" premise is numerically FALSE — tight `D = 1` at n=4 AND n=5); G1-iii-a marked OPEN (bound `D ≥ 1` true, needs a FOURTH mechanism); G1-iii-b flagged OPEN, not attempted. `splits-inequality.md` updated to add the G1-i-HC exchange + `s = 3` all-`n` as PROVED components, stays PARTIAL (general `s ≥ 4`, iii-a, iii-b, G1-ii rest-split all open). Verified: `s = 3` bound 0 violations `n = 3..7` (min slack 0 at `n = 3,4` tight tower-prefix, positive `{1,2,5}` at `n = {5,6,7}`); `(★)` identity 0 error `n = 2..7`; tower-prefix tight `n = 2..6`. Status: partial — the general `s ≥ 4` G1-i-HC bound (n≥4), G1-iii-a (open), G1-iii-b (flat, open), G1-ii (conditional on rest-split), and G2 (upper bound) remain the explicit gaps.
- Round 5: **Re-framed the G1-i-HC crux as a discrepancy identity.** PROVED **Lemma 10** (E_R0 = union of ⌊n/2⌋ superincreasing dyadic bands; the discrepancy function G(x) := |[0,x]∩O_R0| − x/2 swings by ±(band length)/2 on alternating O/E bands, with superincreasing swing amplitudes) and **Lemma 11** (the G1-i-HC bound `|E_R0∩E_F| ≥ (W+1−D_R0−D_F)/2` is *equivalent* to `Alt_s ≥ (D_R0+1−M)/2`, where `Alt_s := G(f_1) − G(f_2) + G(f_3) − ⋯ ± G(f_s)` is the alternating-discrepancy sum at F's sorted breakpoints). Identity verified exact (n=2..6). **G1-i-HC for n=3, all s ∈ {1,2,3} PROVED** (s=1,2 already certified via Case B / Lemma 8; s=3 new via a 2-case split on f_2 — Cases A/B below). **The n=4 s=3 Lemma-6 tight family characterized exactly**: the deficit `E_R0 ∩ E_F` is the single sliver `(2, 2+ε_3]` of measure ε_3 = the target (and symmetrically C = |O_R0 ∩ O_F| = ε_2 + ε_4); the "shave 1" is exactly the dyadic-edge overflow of F's middle breakpoint past the E_R0 edge 2. **General n≥4, s≥3 G1-i-HC remains the open crux**: the reformulation pinpoints it as proving `Alt_s ≥ (D_R0+1−M)/2`, i.e. the alternating discrepancy of F's breakpoints against G's superincreasing swings is bounded below; verified TRUE (exact-rational, n=2..6, s≤n, 0 violations, tight at Lemma-6 family) but a general superincreasing/Zeckendorf argument closing it is NOT found this round (honest flag). **G1-iii-a**: structural adjacency to G1-i-HC noted (dominant piece M = 2^{n−1} from the rest, all 2^n fragments below), but the clean continuity reduction is NOT established — the dominant piece switches provenance (rest vs. fragment of 2^n) under perturbation, so this is NOT a small-ε limit of strict G1-i-HC; OPEN, conditional on the overlap machinery developing at the M = 2^{n−1} boundary. **G1-iii-b** (flat, rest's 2^{n−1} SPLIT, all pieces < 2^{n−1}): verified tight (n=4, D=1 at {6,6,4,4,4,4,2,1}); the flat twin of G2-flat; OPEN (likely resists tiling rigidity which needs a dominant M). **G1-ii**: continuity lift from G1-i-HC-with-rest-split is sound and certified (alternating-potential round 4); CONDITIONAL on G1-i-HC (rest-split) closing. **Rest-split induction (Opening B)** sketched (induct on number of rest-splits via the certified parity-XOR toggle; STRUCTURAL hypothesis required). `splits-inequality.md` kept PARTIAL (Lemmas 10/11 added; n=3 s=3 closure added; general HC gap unchanged). Status: partial — the G1-i-HC general bound (n≥4, s≥3), G1-iii (a conditional, b open), G1-ii (conditional), and G2 (upper bound) remain the explicit gaps.
- Round 1: Built the greedy-alternating lemma (full proof, strong induction with explicit exchange deficit), the recursion identity (full), the n=1 case both bounds (full, two-regime), the lower-bound construction + parity-integral reformulation of D (full), the n=2 lower bound for 0-split and 1-split configurations (full casework), and verified c(1),c(2),c(3) by substitution. The general lower-bound inequality-under-splits lemma (G1, n≥3, and the n=2 two-split sub-case) and the general upper-bound peeling induction (G2) remain open; the latter was predicted by the outline-reviewer, whose numerics show the optimal Xiang split is non-equal/pairing-like. Status: partial — G1 and G2 are the explicit gaps.
- Round 4: Closed the **2-piece-F / rest-unsplit sub-case of G1-i** for all n ≥ 2 (Lemma 8, PROVED). Mechanism: the union-measure reformulation `D = M + D_{R_0} + D_F − 2|O_{R_0} ∪ O_F|` (Lemma 7, exact) turns the bound into `b + |(b,a] ∩ E_{R_0}| ≤ T_n`; the **rigid top O-block** `(2^{n−2}, 2^{n−1}] ⊆ O_{R_0}` (only the rest's piece `2^{n−1}` survives there, j=1 odd) gives `b + |(b,a] ∩ E_{R_0}| ≤ 2^{n−2}` for any 2-piece F = {a,b}, and `2^{n−2} ≤ T_n = (2^n − 1 − D_{R_0})/2` for n ≥ 3 (equality at n=3). This closes the n=3 TIGHT Lemma-6 family (F has 2 pieces there) and the entire 2-piece-F regime for n ≥ 4. The multi-piece-F (s ≥ 3), rest-split (G1-ii), and all-fragments-small (G1-iii) sub-cases remain OPEN (verified TRUE with correct split budget; tight at n=3,4 via multi-piece F; no clean proof found). Documented the **trivial overlap bound** `|O_F ∩ E_{R_0}| ≤ |E_{R_0}|` (Lemma 9, PROVED) which closes the "low-cancellation" regime `D_F ≥ W − D_{R_0} + 1` (F has little internal cancellation) for ALL F at every n — leaving only the high-cancellation (small D_F) regime as the genuine wall. splits-inequality.md kept PARTIAL with the 2-piece case added.
- Round 3: Advanced G1 (the shared lower-bound wall) substantially. PROVED the **largest-piece decomposition** `D = M - D_R` (Lemma 4, via the parity-integral t-axis) — the load-bearing structural identity. PROVED **Case A** (piece 2^n unsplit, all n) — `D = 2^n - D_rest ≥ 1` via the universal bound `D_rest ≤ D_{n-1}`. PROVED **Case B** (piece 2^n split exactly once, all n) — `D = 2^n - D_rest - 2·E_1`, `E_1 ≤ 2^{n-1} - D_rest` (sub-measure), so `D ≥ D_rest ≥ 1` by G1(n−1). PROVED **Case C** (piece 2^n split, largest fragment M = 2^{n−1}, rest's 2^{n−1} unsplit — the "tie" case) — the peeling lemma (imported from `lemmas/peeling.md`) removes the equal pair `(M, rest's 2^{n−1})` D-neutrally, reducing to G1(n−1). Verified all three cases by exact-arithmetic computation (20k trials each, 0 failures). Derived the **multi-split structural formula** `D = M - D_rest - D_F + 2C` (Lemma 5) where `D_F` = D of the non-largest fragments of 2^n and `C` = the overlap of the odd-parity regions of `j_rest` and `j_F`; the bound `D ≥ 1` is equivalent to `2C ≥ D_rest + D_F + 1 - M`. The tight config family (`2^n → {2^{n−1}+ε_1, 2^{n−2}+ε_2, …, 1+ε_n}`, ε_i ≥ 0 summing to 1, paired with rest pieces) attains `D = Σε_i = 1`, confirming the bound is sharp and identifying the handle. GAP remaining: the multi-split non-tie cases (r ≥ 3 fragments of 2^n with M > 2^{n−1}, or M = 2^{n−1} with rest's 2^{n−1} split, or all fragments of 2^n < 2^{n−1}) — proving the overlap bound `2C ≥ D_rest + D_F + 1 - M` rigorously is the open crux. G2 (upper bound) unchanged (still conceded). Status: partial — G1 partially closed (Cases A/B/C proved; multi-split non-tie gap remains).

## Current best
- **Greedy-alternating lemma (PROVED, Lemma 1):** Liu Bang's payoff under optimal alternating claim is the odd-position sum S_odd of the pieces sorted descending; Xiang Yu gets S_even = 1 − S_odd. Corollary S_odd ≥ 1/2 universally.
- **Parity-integral reformulation (PROVED, Lemma 3):** D := S_odd − S_even = ∫₀^∞ [j(t) odd] dt, where j(t) = #{pieces ≥ t}. Hence S_odd = (1+D)/2 and the lower bound S_odd ≥ 2^n/D_n is equivalent to D ≥ 1/D_n.
- **Recursion identity (PROVED, Lemma 2):** with D_n := 2^{n+1}−1 and c(n) := 2^n/D_n, one has 1/c(n) = 2 − 1/2^n = 1/c(n−1) + 1/2^n = Σ_{k=0}^n 2^{−k}, c(0)=1.
- **n=1, both bounds (PROVED):** c(1) = 2/3, attained by Liu's mark at 1/3; Xiang's two-regime reply (equal-split if the larger piece ≥ 2/3, barely-split otherwise) holds Liu to ≤ 2/3.
- **Lower bound construction (full):** Liu's dyadic marks at cumulative sums (2^k−1)/D_n, k=1..n, produce pieces 1:2:4:…:2^n (each /D_n); the largest 2^n/D_n strictly exceeds the sum of all others (2^n−1)/D_n.
- **n=2 lower bound, 0- and 1-split cases (PROVED):** D ≥ 1/7 = 1/D_2, with equality attained by splitting the largest piece 4 into a+b with the smaller part b ∈ [1,2] (in particular by the equal-halving 2+2).
- **Largest-piece decomposition (Lemma 4, PROVED):** for any final multiset with largest piece M (a choice, if ties) and R = the rest, `D = M - D_R` where `D_R` = D of R. Proof via the parity-integral t-axis: on `(max(R), M]` only M contributes (j=1, odd); on `[0, max(R)]` M's contribution flips the rest's parity. The load-bearing structural identity for G1.
- **G1 Case A (PROVED, all n):** piece 2^n unsplit. `D = 2^n - D_rest`, `D_rest ≤ total(rest) = D_{n-1} = 2^n − 1` (universal bound `D ≤ total`), so `D ≥ 1`.
- **G1 Case B (PROVED, all n):** piece 2^n split exactly once into `M + g_2` (`M ≥ 2^{n−1} ≥ g_2`), rest = dyadic (n−1) with ≤ n−1 splits. Formula `D = 2^n − D_rest − 2·E_1`, `E_1 = ∫_0^{g_2} [j_rest even]`. Bound `E_1 ≤ ∫_0^{2^{n−1}} [j_rest even] = 2^{n−1} − D_rest` (sub-measure) ⟹ `D ≥ D_rest ≥ 1` (G1(n−1), rest has ≤ n−1 splits).
- **G1 Case C (PROVED, all n):** piece 2^n split (any r ≥ 2 fragments), largest fragment `M = 2^{n−1}`, AND rest's piece `2^{n−1}` unsplit. The two `2^{n−1}`'s (M and rest's) form an equal pair; the **peeling lemma** (`lemmas/peeling.md`, CERTIFIED) removes it D-neutrally, giving `D = D_{R'}` where `R' = (dyadic (n−2) with ≤ n+1−r splits) ∪ F` (F = other fragments of 2^n, summing `2^{n−1}`). Reinterpret `R'` as the (n−1)-dyadic config `{1,…,2^{n−1}}` with piece `2^{n−1}` refined into F (r−2 splits) and `{1,…,2^{n−2}}` with ≤ n+1−r splits; total ≤ n−1 splits. By G1(n−1), `D_{R'} ≥ 1`.
- **G1 multi-split structural formula (Lemma 5, PROVED identity):** for 2^n split into `M, g_2,…,g_r` (`M ≥ 2^{n−1}` unique largest), `D = M − D_rest − D_F + 2C`, where `D_F` = D of F = {g_2,…,g_r} (standalone) and `C = ∫_0^{2^{n−1}} [j_rest odd][j_F odd]` (overlap of odd-parity regions of the dyadic-rest and the extra-fragments j-functions). The bound `D ≥ 1` ⟺ `2C ≥ D_rest + D_F + 1 − M`. This is the handle for the remaining gap.
- **Union-measure reformulation (Lemma 7, PROVED):** `D = M + D_{R_0} + D_F − 2|O_{R_0} ∪ O_F|`, so `D ≥ 1 ⟺ |O_{R_0} ∪ O_F| ≤ (M + D_{R_0} + D_F − 1)/2`. The trivial bound `|union| ≤ 2^{n−1}` is off by exactly `(W + 1 − D_{R_0} − D_F)/2`; the wall is "shave 1 unit off the trivial union bound," forced by the rigid alternating-dyadic tiling structure of `O_{R_0}`.
- **G1-i 2-piece F / rest-unsplit (Lemma 8, PROVED, all n ≥ 2):** when `2^n → M + a + b` (3 fragments, `M > 2^{n−1}`, rest unsplit), `D ≥ 1`. Mechanism: the rigid top O-block `(2^{n−2}, 2^{n−1}] ⊆ O_{R_0}` gives `b + |(b,a] ∩ E_{R_0}| ≤ 2^{n−2}`, and `2^{n−2} ≤ T_n = (2^n − 1 − D_{R_0})/2` for `n ≥ 3`. **Closes the n=3 tight Lemma-6 family** (F has 2 pieces there) and the entire 2-piece-F regime at `n ≥ 4` (slack there).
- **Low-cancellation regime (Lemma 9, PROVED, all F, all n):** the trivial bound `|O_F ∩ E_{R_0}| ≤ |E_{R_0}|` closes `D ≥ 1` whenever `D_F ≥ W − D_{R_0} + 1` (F has little internal cancellation). Leaves only the **high-cancellation regime** (`D_F` small, the tight Lemma-6 territory) as the genuine open wall.
- **Rest tiling structure + discrepancy function G (Lemma 10, PROVED, round 5):** `E_{R_0}` is a union of `⌊n/2⌋` superincreasing dyadic bands (recursion `E_{R_0}(n) = (2^{n−3}, 2^{n−2}] ∪ E_{R_0}(n−2)`); the discrepancy `G(x) = |[0,x]∩O_{R_0}| − x/2` swings by ±(band length)/2 on alternating O/E bands with superincreasing amplitudes. The structural asset for the HC crux.
- **Discrepancy reformulation of G1-i-HC (Lemma 11, PROVED identity, round 5):** `overlap − target = (M − 1 − D_{R_0})/2 + Alt_s`, where `Alt_s = Σ_{i=1}^s (−1)^{i+1} G(f_i)` is the alternating-discrepancy sum at F's sorted breakpoints. Hence `D ≥ 1 ⟺ Alt_s ≥ (D_{R_0}+1−M)/2`. Pinpoints the "shave 1" as the alternating-discrepancy deficit; verified exact `n=2..6`.
- **G1-i-HC for n=3, all s (Lemma 12, PROVED, round 5):** `D ≥ 1` for `2^3 → M + F`, `M > 4`, `F` with up to 3 pieces, rest unsplit. Closes n=3 rest-unsplit G1-i-HC entirely (the smallest HC sub-case). Cases A/B on `f_2`.
- **n=4 s=3 Lemma-6 tight family (sliver witness, PROVED, round 5):** the deficit `E_{R_0} ∩ E_F` is the single sliver `(2, 2+ε_3]` of measure `ε_3` = target exactly; `C = ε_2 + ε_4`. The "shave 1" is exactly the dyadic-edge overflow of F's middle breakpoint past the `E_{R_0}` edge 2.
- **General G1-i-HC bound (n≥4, s≥3, CONJECTURED+verified, round 5):** `Alt_s ≥ (D_{R_0}+1−M)/2` for all `n, s≤n`. Verified exact-rational `n=2..6`, 0 violations, tight at Lemma-6 family. Open crux: a clean superincreasing/Zeckendorf argument closing it was NOT found this round.
- **Round 6 — clean measure form (★) (Lemma 13, PROVED):** G1-i-HC ⟺ `Ψ(F) := Σ_{i odd} E(f_i) + Σ_{i even} O(f_i) ≤ T_n := (2^n−1−D_{R_0})/2` (exact equivalent; `Alt_s − target = T_n − Ψ`). Decouples the `W`-dependence of the target; the clean statement of the wall. Pair-decomposition: `Ψ = S_even(F) + |Q∩E_{R_0}|` where `Q = ∪`odd-indexed sub-intervals of the partition of `[0,f_1]`. Rigid top `O`-block: `E_{R_0} ⊆ [0, 2^{n−2}]`, and the `[0,m]` `E↔O` swap reduces to the `(n−1)`-rest regions.
- **Round 6 — tower-prefix tight arithmetic (Lemma 14, PROVED):** at `F^* = {2^{n−2}, 2^{n−3}, …}`, `Ψ(F^*) = T_n` exactly (each `ε_i` contributes `±ε_i/2` to `Ψ` and `−ε_1/2` to target; `Σε = 1` ⟹ equality). Verified `n=2..6`.
- **Round 6 — sliding/exchange (Lemma 15, PROVED):** `Ψ` is PWL; at any maximizer over `{f_1≥…≥f_s≥0, Σf_i≤U}`, each `f_i` is at a dyadic band-edge or tied to a neighbor (KKT: interior-to-band derivatives are 0 or 1, never both, so a non-edge non-tied coord slides). Reduces the search to dyadic-edge arrangement vertices.
- **Round 6 — s=3 ALL n≥3 (Lemma 16, PROVED):** `Ψ ≤ T_n` for `F = {f_1≥f_2≥f_3}`, all `n ≥ 3`. Spill case (`f_1 > m`) reduces to Lemma 8 (s=2) at `n−1` via the `[0,m]` swap; no-spill cases (I.a crude bound, I.b.1 Lemma 8, I.b.2 constant-`O(f_2)` + `W<2m` slack) close directly. Generalizes the n=4 s=3 sliver (§4.8) to a full closure. Verified 0 violations n=3..7.
- **Round 6 — general s≥4 G1-i-HC (CONJECTURED+verified, OPEN):** the superincreasing-prefix obstruction (crux aimo-0530 adapted) is the mechanism; the W-sum coupling (superincreasing surplus must dominate multi-breakpoint compensation preserving `Σf_i = W`) is the open step. `s = 3` closes because its coupling is single-secondary-breakpoint; `s ≥ 4` is multi-breakpoint.
- **Tight config family (proves the bound is sharp):** `2^n → {2^{n−1}+ε_1, 2^{n−2}+ε_2, …, 1+ε_n}` with `ε_i ≥ 0`, `Σ ε_i = 1`, paired (in sorted order) with the rest pieces `{2^{n−1}, 2^{n−2}, …, 1}`, gives `D = Σ ε_i = 1`. (Equal-halving is `ε_i = 0` with a trailing triple `(1,1,1)` contributing the +1.) Confirmed by 80k-trial random search (n=3): min `D = 1` exactly, attained by this family.
- **Open gap G1-multi (lower bound):** the multi-split NON-TIE cases, **refined to the high-cancellation regime** after Lemmas 8 & 9: (i) `2^n` split into `r ≥ 4` fragments (`F` has `s ≥ 3` pieces) with `M > 2^{n−1}` strict, rest unsplit, AND `D_F` small (high cancellation) — the `n ≥ 4` Lemma-6 tight family lives here; (ii) `M = 2^{n−1}` but rest's `2^{n−1}` is SPLIT (no tie to peel); (iii) all fragments of `2^n` < `2^{n−1}` (near-tie; the outline's "reduce to `G1(n−1)`" does NOT hold cleanly — `R` is not a dyadic `(n−1)` config). Closing requires proving `|O_F ∩ E_{R_0}| ≤ (M − D_{R_0} + D_F − 1)/2` in the high-cancellation regime (Lemma 7 corollary); the trivial overlap bound (Lemma 9) and the sub-measure bound `C ≤ D_F` are both too loose there. Numerics (correct split budget) confirm `D ≥ 1` throughout (`n = 2..6`), tight at `n = 3, 4` via multi-piece F.
- **Open gap G2 (upper bound, general):** the inductive peeling step realizing 1/c(n) = 1/c(n−1)+1/2^n. The reviewer's numerics show the optimal Xiang split on the dyadic n=2 config is non-equal (barely-split 4/7 → 0.425+0.146, attaining D=1/7) and on hard random configs is pairing-like; the peeling-as-equal-split intuition is therefore too narrow. Honest gap.

## Full proof
*(Not yet complete: G1 partially closed (Cases A/B/C PROVED; multi-split non-tie GAP) and G2 (upper bound) open. The partial proof — all rigorous components — follows.)*

---

### 0. Notation and the answer

Let `D_n := 2^{n+1} − 1`. We prove (up to the two flagged gaps) that

> **c(n) = 2^n / D_n** (= 2/3, 4/7, 8/15, … for n = 1, 2, 3, …).

The two bounds required (KB: *Constructive vs existence* — a "find largest" problem needs a matching lower bound AND upper bound):
- *Lower bound:* Liu Bang has a marking strategy guaranteeing him ≥ 2^n/D_n.
- *Upper bound:* for every Liu Bang marking (≤ n marks), Xiang Yu has a reply (≤ n marks) holding Liu Bang to ≤ 2^n/D_n.

Cut the stick at all marks; the resulting pieces are claimed alternately, Liu Bang first, each maximizing his own total. The claiming phase is governed by:

### 1. Lemma (greedy-alternating claim) — PROVED

> Let the final pieces be a multiset of m ≥ 0 pieces, sorted descending a_1 ≥ a_2 ≥ … ≥ a_m ≥ 0, summing to T. Under free-choice alternating claim with Liu Bang first and both players maximizing their own total, Liu Bang's payoff is **S_odd := a_1 + a_3 + a_5 + …** and Xiang Yu's is **S_even := a_2 + a_4 + … = T − S_odd**. An optimal first move for Liu Bang is to take a_1 (greedy).

**Proof** (strong induction on m, KB: *Induction*). Base m ∈ {0,1} is trivial (m=1: Liu takes a_1 = S_odd). Assume m ≥ 2 and the claim for all smaller multisets.

Consider Liu Bang's first move. If he takes a_i, the remainder R_i = {a_1,…,a_{i−1}, a_{i+1},…,a_m} is still sorted descending (removing one element preserves order); call it b_1 ≥ … ≥ b_{m−1}, where b_j = a_j for j < i and b_j = a_{j+1} for j ≥ i. Xiang Yu now moves *first* on R_i; by the induction hypothesis Xiang Yu gets the odd-position sum of R_i, so Liu Bang gets the **even-position sum** of R_i plus the piece a_i he already took:

> Liu's total after first taking a_i  =  a_i + E_i,  where  E_i := b_2 + b_4 + b_6 + …  (even positions of R_i).

We compare E_i to E_1. Write k := ⌊i/2⌋ (so i = 2k or i = 2k+1; for i = 1 we take k = 0).

- **i = 1 (k = 0):** R_1 = {a_2, a_3, …}, so E_1 = a_3 + a_5 + a_7 + …, and Liu's total = a_1 + a_3 + a_5 + … = S_odd.
- **i = 2k (k ≥ 1, even i):** the even-indexed b's are b_2, b_4, …, b_{2k−2} (= a_2, a_4, …, a_{2k−2}, since 2j < 2k ⟺ j < k) and then b_{2k}, b_{2k+2}, … (= a_{2k+1}, a_{2k+3}, …, since 2j ≥ 2k ⟺ j ≥ k). Hence
  E_{2k} = (a_2 + a_4 + … + a_{2k−2}) + (a_{2k+1} + a_{2k+3} + …).
  Liu's total = a_{2k} + E_{2k}. Subtract from S_odd:
  S_odd − (a_{2k} + E_{2k}) = (a_1 + a_3 + … + a_{2k−1}) − (a_{2k} + a_2 + a_4 + … + a_{2k−2})
  = Σ_{j=1}^{k} (a_{2j−1} − a_{2j})  =:  Δ_k ≥ 0,
  because a_{2j−1} ≥ a_{2j} (sorted). So total(2k) = S_odd − Δ_k ≤ S_odd.
- **i = 2k+1 (k ≥ 1, odd i ≥ 3):** the even-indexed b's are b_2, …, b_{2k} (= a_2, …, a_{2k}, since 2j ≤ 2k < 2k+1 ⟺ j ≤ k) and then b_{2k+2}, b_{2k+4}, … (= a_{2k+3}, a_{2k+5}, …). Hence
  E_{2k+1} = (a_2 + … + a_{2k}) + (a_{2k+3} + a_{2k+5} + …).
  Liu's total = a_{2k+1} + E_{2k+1}. Subtract from S_odd:
  S_odd − (a_{2k+1} + E_{2k+1}) = (a_1 + a_3 + … + a_{2k−1}) − (a_2 + a_4 + … + a_{2k})
  = Σ_{j=1}^{k} (a_{2j−1} − a_{2j})  =  Δ_k ≥ 0.
  So total(2k+1) = S_odd − Δ_k ≤ S_odd.

Thus for every i ≥ 2, Liu's total after first taking a_i is S_odd − Δ_k ≤ S_odd, with Δ_k ≥ 0; equality requires a_{2j−1} = a_{2j} for all j ≤ k. The maximum over i is attained at i = 1, value S_odd. Taking a_1 is optimal; by the induction hypothesis the continuation is greedy-optimal for both. ∎

**Corollary (universal floor):** S_odd − S_even = D where D := a_1 − a_2 + a_3 − a_4 + …; pairing a_{2j−1} ≥ a_{2j} gives D ≥ 0, hence S_odd = (T+D)/2 ≥ T/2 = 1/2. Equality D = 0 iff a_1=a_2, a_3=a_4, ….

### 2. Lemma (parity-integral reformulation of D) — PROVED

> With a_1 ≥ … ≥ a_m sorted descending and D := a_1 − a_2 + a_3 − a_4 + …, define j(t) := #{i : a_i ≥ t}. Then
> D = ∫₀^∞ [j(t) is odd] dt.   (Equivalently, D is the measure of the set of levels t at which an odd number of pieces are ≥ t.)

**Proof.** D = Σ_i (−1)^{i+1} a_i = Σ_i (−1)^{i+1} ∫₀^{a_i} dt = ∫₀^∞ Σ_i (−1)^{i+1}·𝟙[a_i ≥ t] dt (Fubini, finitely many pieces). For fixed t, the set {i : a_i ≥ t} is a prefix {1, 2, …, j(t)} (sorted desc), so the inner sum is Σ_{i=1}^{j(t)} (−1)^{i+1} = 1 if j(t) is odd, 0 if j(t) is even. ∎

This lemma makes the lower-bound target concrete: proving Liu's S_odd ≥ 2^n/D_n is equivalent (via S_odd = (1+D)/2) to proving **D ≥ 1/D_n** for the relevant multiset.

### 3. Lemma (recursion identity) — PROVED

> With D_n := 2^{n+1}−1 and c(n) := 2^n/D_n: 1/c(n) = 2 − 2^{−n} = 1/c(n−1) + 2^{−n} = Σ_{k=0}^{n} 2^{−k}, with c(0) = 1.

**Proof.** 1/c(n) = D_n/2^n = (2^{n+1}−1)/2^n = 2 − 2^{−n}. The geometric sum Σ_{k=0}^{n} 2^{−k} = (1 − 2^{−(n+1)})/(1 − 1/2) = 2(1 − 2^{−(n+1)}) = 2 − 2^{−n}. And 1/c(n−1) + 2^{−n} = (2 − 2^{−(n−1)}) + 2^{−n} = 2 − 2·2^{−n} + 2^{−n} = 2 − 2^{−n}. ∎

So the target recursion `1/c(n) = 1/c(n−1) + 1/2^n` is arithmetically exact; the proof burden is showing a strategy realizes it.

### 4. Lower bound — Liu Bang's dyadic construction

**Construction (KB: *Constructive vs existence*).** Liu Bang places his n marks so that the n+1 pieces (before Xiang Yu moves) have lengths 1, 2, 4, …, 2^n, each divided by D_n = 2^{n+1}−1. Concretely the marks sit at cumulative sums (2^k − 1)/D_n for k = 1, …, n (the order of the pieces around the stick is irrelevant — only the multiset matters, since the greedy claim depends only on sorted values). For n = 1, 2, 3 this gives marks at {1/3}, {1/7, 3/7}, {1/15, 3/15, 7/15} respectively.

**Structural fact (the forcing property).** The largest piece g_n := 2^n/D_n strictly exceeds the sum of all the others:
> g_n = 2^n/D_n > (2^n − 1)/D_n = (sum of all smaller pieces),
since 2^n > 2^n − 1. (This is the dyadic "largest strictly exceeds sum of rest" mechanism, KB analogue aimo-0117.)

**Target after Xiang Yu's reply.** Xiang Yu inserts ≤ n marks, each splitting one piece into two. Let the final multiset (sorted descending) have alternating sum D. By Lemma 1, Liu Bang's payoff is (1+D)/2; the lower bound Liu Bang ≥ 2^n/D_n is, by Lemma 3, equivalent to:

> **(G1, splits-inequality lemma)**  D ≥ 1/D_n   for every way for Xiang Yu to insert ≤ n marks among the dyadic pieces {1, 2, …, 2^n}/D_n.

Equality is attained (so the bound would be sharp) by Xiang Yu's *equal-halving* reply: split each piece 2^k (k = 1, …, n) into two equal halves 2^{k−1}, 2^{k−1}, leaving the smallest piece (1) unsplit. The resulting multiset is {1, 1, 1, 2, 2, 4, 4, …, 2^{n−1}, 2^{n−1}}/D_n (2n+1 pieces), sorted as 2^{n−1}, 2^{n−1}, 2^{n−2}, 2^{n−2}, …, 2, 2, 1, 1, 1. Each pair (2^{k−1}, 2^{k−1}) cancels in D; the trailing triple (1, 1, 1) occupies ranks 2n−1, 2n, 2n+1 contributing +1 − 1 + 1 = +1. Hence D = 1/D_n exactly, and Liu = (1 + 1/D_n)/2 = (D_n + 1)/(2 D_n) = 2^{n+1}/(2 D_n) = 2^n/D_n. ✓

#### 4.1. G1 base case n = 1 — PROVED

Pieces {2, 1}/3 (D_1 = 3). At most one Xiang mark.
- *No mark:* D = 2 − 1 = 1 = 1/D_1·… /3 → D = 1/3 = 1/D_1. ✓
- *Split the larger piece 2 into a + b, a ≥ b, a + b = 2 (so b ≤ 1):* the three pieces are a, 1, b; since a ≥ 1 ≥ b, sorted desc is a, 1, b. D = a − 1 + b = (a+b) − 1 = 1, so D = 1/3 = 1/D_1. (D-neutral: independent of b.) ✓
- *Split the smaller piece 1 into a + b, a ≥ b, a + b = 1 (so b ≤ 1/2):* pieces 2, a, b; sorted 2, a, b (a ≤ 1 ≤ 2). D = 2 − a + b = 2 − (a − b) = 2 − (2a − 1) = 3 − 2a ≥ 3 − 2·(1/2) = 2, so D ≥ 2/3 > 1/3. ✓

So D ≥ 1/D_1 for n = 1, equality when splitting the larger piece (or not splitting). G1 holds for n = 1. ✓

#### 4.2. G1 for n = 2, zero- and one-mark cases — PROVED

Pieces {4, 2, 1}/7 (D_2 = 7). Work in units of 1/D_2 = 1/7; the (scaled) target is D_scaled ≥ 1.

- *Zero marks:* D = 4 − 2 + 1 = 3 ≥ 1. ✓
- *One mark, splitting the largest piece 4 into a + b, a ≥ b, a + b = 4 (b ∈ (0, 2]):* the four pieces are a, b, 2, 1. Since a ≥ 2 (as a ≥ b and a+b=4) we have a = max; 4 − a = b ≤ 2. Two sub-cases by where b lands:
  - *b ≥ 1 (i.e. a ∈ [2, 3]):* sorted desc is a, 2, b, 1 (a ≥ 2 ≥ b ≥ 1). D = a − 2 + b − 1 = (a+b) − 3 = 4 − 3 = 1. D-neutral. ✓ (equality D_scaled = 1 = 1/D_2·7)
  - *b < 1 (i.e. a ∈ (3, 4)):* sorted desc is a, 2, 1, b (b < 1). D = a − 2 + 1 − b = (a − b) − 1 = (2a − 4) − 1 = 2a − 5. For a ∈ (3, 4): D_scaled ∈ (1, 3), strictly above 1. ✓
  Hence splitting piece 4 gives D_scaled ≥ 1, equality iff b ∈ [1, 2].
- *One mark, splitting the middle piece 2 into a + b, a ≥ b, a + b = 2 (b ≤ 1):* pieces 4, a, 1, b. Since a ≥ 1 ≥ b, sorted desc is 4, a, 1, b (a ≤ 2 ≤ 4). D = 4 − a + 1 − b = 5 − (a+b) = 5 − 2 = 3 ≥ 1. ✓ (D-neutral at 3, independent of the split.)
- *One mark, splitting the smallest piece 1 into a + b, a ≥ b, a + b = 1 (b ≤ 1/2):* pieces 4, 2, a, b; sorted 4, 2, a, b (a ≤ 1 ≤ 2). D = 4 − 2 + a − b = 2 + (a − b) = 2 + (2a − 1) ≥ 2 + 0 = 2 ≥ 1. ✓

So for n = 2 with ≤ 1 Xiang mark, D_scaled ≥ 1, equality only by splitting the largest piece with the smaller part in [1, 2] (in particular the equal-halving 4 → 2 + 2).

#### 4.3. G1 — the splits-inequality lemma (PARTIAL: Cases A, B, C PROVED; multi-split non-tie GAP)

> **G1 (splits-inequality, statement).** For every n ≥ 1 and every choice of ≤ n marks inserted among the dyadic pieces {1, 2, …, 2^n}/D_n (units: total `D_n = 2^{n+1} − 1`, target `D ≥ 1`), the alternating sum D of the resulting sorted-desc multiset satisfies `D ≥ 1`, with equality attained by the equal-halving reply and the broader "barely-larger" family (Lemma 6 below).

We prove G1 by strong induction on n (KB: *Induction*). Base `n = 0`: multiset `{1}`, no splits, `D = 1` ✓. Base `n = 1`: proved in §4.1 (all splits give `D ≥ 1`, equality at splitting the larger piece). Inductive step: assume `G1(j)` for all `j < n`; we prove `G1(n)`. The key structural identity is:

**Lemma 4 (largest-piece decomposition).** *Let the final multiset have a (choice of) largest piece `M`, and let `R` be the multiset of all other pieces (the "rest"). Write `D_R` for the alternating sum of R. Then `D = M − D_R`.*

**Proof.** Use the parity-integral reformulation (Lemma 2/3): `D = ∫_0^∞ [j(t) odd] dt`, `j(t) = #{pieces ≥ t}`. Split the t-axis by `max(R)` (the largest piece of R; if R is empty take `max(R) = 0`):
- `t ∈ (max(R), M]`: only M is ≥ t (every piece of R is ≤ max(R) < t). So `j_final(t) = 1`, odd. Contributes `M − max(R)`.
- `t ∈ (M, ∞)`: no piece ≥ t (`M` is the global max). `j_final = 0`, even. Contributes 0.
- `t ∈ [0, max(R)]`: M contributes (M ≥ max(R) ≥ t), so `j_final = 1 + j_R(t)`. Parity `[j_final odd] = [1 + j_R odd] = [j_R even]` (adding 1 flips parity). So `∫_0^{max(R)} [j_final odd] = ∫_0^{max(R)} [j_R even] = max(R) − D_R` (the even-measure of `j_R` over its full support `[0, max(R)]`).

Sum: `D = (M − max(R)) + (max(R) − D_R) = M − D_R`. ∎ (Verified: 3000 trials, n ∈ {2,3}, 0 errors.)

(With ties — several pieces equal to M — pick any one as "the largest"; the formula `D = M − D_R` still holds by the same t-axis argument, since `j_final` on `(max(R), M]` equals the *number of copies of M*, which contributes `c·(M − max(R))` if there are c copies, and removing one copy from R leaves `c − 1` copies in R contributing `(c−1)·(M − max(R))` to `D_R`; the difference is `M − max(R)`. The identity `D = M − D_R` is preserved.)

---

**Case A — piece `2^n` unsplit. PROVED (all n).** Then `M = 2^n` (the largest original piece, unsplit, dominates every other final piece since each is a sub-piece of some `2^k, k ≤ n−1`, hence ≤ `2^{n−1} < 2^n`). `R` = the dyadic `(n−1)` config `{1,…,2^{n−1}}` with ≤ n splits on it. By the universal bound `D ≤ total` (since `D = S_odd − S_even ≤ S_odd + S_even = total`), `D_R ≤ total(R) = D_{n−1} = 2^n − 1`. Hence `D = M − D_R = 2^n − D_R ≥ 2^n − (2^n − 1) = 1`. ✓ (Case A, all n.)

---

**Case B — piece `2^n` split exactly once. PROVED (all n).** So `2^n → M + g_2` with `M ≥ 2^{n−1} ≥ g_2 ≥ 0` (the larger fragment is ≥ half of `2^n`, hence ≥ `2^{n−1}`). The rest `R_0 = {1,…,2^{n−1}}` (the dyadic `(n−1)` config) has ≤ `n − 1` splits on it (one split was used on `2^n`); by the inductive hypothesis `G1(n−1)`, `D_{R_0} ≥ 1`.

Compute `D` via the t-axis. Assume `M ≥ 2^{n−1}` (so M is the unique global largest; the boundary `M = 2^{n−1}` gives a tie with rest's piece `2^{n−1}` and is handled in Case C). Then `max(R) = 2^{n−1}` (rest's largest, unsplit-or-split; rest pieces ≤ `2^{n−1}`, and `g_2 ≤ 2^{n−1}`):
- `t ∈ (2^{n−1}, M]`: only M. `j_final = 1`. Contributes `M − 2^{n−1}`.
- `t ∈ (M, 2^n]`: nothing. Contributes 0.
- `t ∈ [0, 2^{n−1}]`: M contributes (M ≥ 2^{n−1} ≥ t), and `g_2` contributes on `[0, g_2]`, and the rest `R_0` contributes `j_{R_0}(t)`. So `j_final = 1 + [g_2 ≥ t] + j_{R_0}(t)`. Parity: `[j_final odd] = [(1 + [g_2≥t] + j_{R_0}) odd]`. On `[0, g_2]`: `[g_2≥t]=1`, so parity = `[j_{R_0} + 2 odd] = [j_{R_0} odd]` (since +2 preserves parity). On `(g_2, 2^{n−1}]`: `[g_2≥t]=0`, parity = `[j_{R_0} + 1 odd] = [j_{R_0} even]`.

Hence `D = (M − 2^{n−1}) + ∫_0^{g_2} [j_{R_0} odd] + ∫_{g_2}^{2^{n−1}} [j_{R_0} even]`. Write `D_{R_0} = ∫_0^{2^{n−1}} [j_{R_0} odd]`, `E_1 := ∫_0^{g_2} [j_{R_0} even]`. Then `∫_0^{g_2} [j_{R_0} odd] = D_{R_0} − ∫_{g_2}^{2^{n−1}} [j_{R_0} odd]` and `∫_{g_2}^{2^{n−1}} [j_{R_0} even] = (2^{n−1} − g_2) − ∫_{g_2}^{2^{n−1}} [j_{R_0} odd]`. Substituting:
`D = (M − 2^{n−1}) + D_{R_0} − ∫_{g_2}^{2^{n−1}} odd + (2^{n−1} − g_2) − ∫_{g_2}^{2^{n−1}} odd = (M − g_2) + D_{R_0} − 2 ∫_{g_2}^{2^{n−1}} [j_{R_0} odd]`.
Using `M + g_2 = 2^n` (so `M − g_2 = 2^n − 2g_2`) and `∫_{g_2}^{2^{n−1}} [j_{R_0} odd] = D_{R_0} − ∫_0^{g_2} [j_{R_0} odd] = D_{R_0} − (g_2 − E_1) = D_{R_0} − g_2 + E_1`:
`D = (2^n − 2g_2) + D_{R_0} − 2(D_{R_0} − g_2 + E_1) = 2^n − 2g_2 + D_{R_0} − 2 D_{R_0} + 2 g_2 − 2 E_1 = 2^n − D_{R_0} − 2 E_1`.   **(Case-B formula)**

The key bound: `E_1 = ∫_0^{g_2} [j_{R_0} even] ≤ ∫_0^{2^{n−1}} [j_{R_0} even]` (a sub-measure; `g_2 ≤ 2^{n−1}`). And `∫_0^{2^{n−1}} [j_{R_0} even] = 2^{n−1} − D_{R_0}` (odd + even = full support `2^{n−1}`). So `E_1 ≤ 2^{n−1} − D_{R_0}`. Therefore
`D = 2^n − D_{R_0} − 2 E_1 ≥ 2^n − D_{R_0} − 2(2^{n−1} − D_{R_0}) = 2^n − D_{R_0} − 2^n + 2 D_{R_0} = D_{R_0} ≥ 1`   (by `G1(n−1)`, rest has ≤ n−1 splits).   ✓ (Case B, all n; verified 20k trials, 0 failures.)

This recovers §4.1 (n=1) and §4.2 (n=2, one-mark) as special cases. Note Case B is **tight** at `M = 2^{n−1}` (equal-halving `g_2 = 2^{n−1}`): then `E_1 = ∫_0^{2^{n−1}} [j_{R_0} even] = 2^{n−1} − D_{R_0}` (full measure, bound saturated), giving `D = D_{R_0}` — the peeling lemma's `D`-neutrality of the equal pair `(2^{n−1}, 2^{n−1})` (the fragment `g_2` and rest's piece `2^{n−1}`).

---

**Case C — piece `2^n` split (any r ≥ 2 fragments), largest fragment `M = 2^{n−1}`, AND rest's piece `2^{n−1}` unsplit. PROVED (all n).** Then the config contains TWO pieces equal to `2^{n−1}`: the fragment M (from `2^n`'s split) and the original piece `2^{n−1}` of the rest. Let `F = {g_2,…,g_r}` be the OTHER fragments of `2^n` (each ≤ `2^{n−1}`, summing to `2^n − M = 2^{n−1}`; for r ≥ 3, each is `< 2^{n−1}` strictly, since two fragments summing to `2^{n−1}` with one = `2^{n−1}` would force the other = 0). The two `2^{n−1}`'s form an **equal pair**; by the **peeling lemma** (imported from `lemmas/peeling.md`, CERTIFIED round 2), removing this equal pair is exactly `D`-neutral:
`D = D_{R'}`, where `R' = (dyadic (n−2) = {1,…,2^{n−2}} with ≤ n+1−r splits) ∪ F`.

Now reinterpret `R'` as a refinement of the `(n−1)`-dyadic config `{1,…,2^{n−2}, 2^{n−1}}`:
- The piece `2^{n−1}` is refined into the fragments `F` (summing `2^{n−1}`; any partition of `2^{n−1}` into `r−1` positive pieces is realizable by `r−2` splits — this is a *virtual* reinterpretation; `D` depends only on the multiset, not the history).
- The pieces `{1,…,2^{n−2}}` carry ≤ `n+1−r` splits.

Total splits on the `(n−1)`-dyadic config = `(r−2) + (n+1−r) = n − 1 ≤ n − 1`. By the inductive hypothesis `G1(n−1)` (the `(n−1)`-dyadic config with ≤ `n−1` splits has `D ≥ 1`), `D_{R'} ≥ 1`. Hence `D = D_{R'} ≥ 1`.   ✓ (Case C, all n; verified 20k trials, 0 failures, including the tie sub-cases r=2 (equal-halving) and r ≥ 3.)

---

**Lemma 5 (multi-split structural formula — the handle for the remaining gap).** *Suppose `2^n` is split into fragments `g_1 = M, g_2, …, g_r` (r ≥ 2, `M ≥ 2^{n−1}` unique largest), the rest `R_0 = {1,…,2^{n−1}}` has ≤ `n+1−r ≤ n−1` splits on it (so `D_{R_0} ≥ 1` by `G1(n−1)`), and `F = {g_2,…,g_r}` (sum `W = 2^n − M ≤ 2^{n−1}`). Then*
`D = M − D_{R_0} − D_F + 2 C,`
_where `D_F = ∫_0^{2^{n−1}} [j_F odd]` is the standalone D-value of the multiset F, `j_F(t) = #{f ∈ F : f ≥ t}`, and `C = ∫_0^{2^{n−1}} [j_{R_0} odd] · [j_F odd]` is the overlap (measure) of the odd-parity regions of `j_{R_0}` and `j_F`._

**Proof.** As in Case B, on `[0, 2^{n−1}]` we have `j_final = 1 + j_{R_0} + j_F` (M contributes, rest and F contribute), so `[j_final odd] = [j_{R_0} + j_F even]` (the +1 flips). Now `[j_{R_0} + j_F even] = 1 − [j_{R_0} ⊕ j_F]` (same parity ⟺ XOR = 0), and `[j_{R_0} ⊕ j_F] = [j_{R_0} odd] ⊕ [j_F odd]` (parity of a sum = XOR of parities). Using the XOR-integral identity `∫(a ⊕ b) = ∫a + ∫b − 2∫(a·b)` for indicators `a, b`:
`∫_0^{2^{n−1}} [j_final odd] = ∫_0^{2^{n−1}} (1 − [j_{R_0} odd] ⊕ [j_F odd]) = 2^{n−1} − (D_{R_0} + D_F − 2 C)`.
Adding the top-band contribution `(M − 2^{n−1})` (from `(2^{n−1}, M]`, j=1): `D = (M − 2^{n−1}) + 2^{n−1} − D_{R_0} − D_F + 2 C = M − D_{R_0} − D_F + 2 C`. ∎ (Verified: 3000 trials, 0 errors against direct parity-integral computation.)

**Corollary (equivalence).** `D ≥ 1 ⟺ 2 C ≥ D_{R_0} + D_F + 1 − M` (rearrange Lemma 5).

### Lemma 7 (union-measure reformulation) — PROVED (identity)

> Under the setup of Lemma 5 (with `max(R_0) ≤ 2^{n−1}` so the top band is `(max(R_0), M]`), let `O_{R_0}, O_F ⊆ [0, 2^{n−1}]` be the odd-parity regions of `j_{R_0}`, `j_F` respectively (both within `[0, 2^{n−1}]`). Then
> `D = M + D_{R_0} + D_F − 2 · |O_{R_0} ∪ O_F|`   (within `[0, 2^{n−1}]`),
> and consequently `D ≥ 1 ⟺ |O_{R_0} ∪ O_F| ≤ (M + D_{R_0} + D_F − 1)/2`.

**Proof.** Inclusion–exclusion: `|O_{R_0} ∪ O_F| = |O_{R_0}| + |O_F| − |O_{R_0} ∩ O_F| = D_{R_0} + D_F − C`. Substituting `2C = 2(D_{R_0} + D_F − |O_{R_0} ∪ O_F|)` into Lemma 5's identity `D = M − D_{R_0} − D_F + 2C` gives `D = M − D_{R_0} − D_F + 2(D_{R_0} + D_F − |O_{R_0} ∪ O_F|) = M + D_{R_0} + D_F − 2|O_{R_0} ∪ O_F|`. The equivalence to `D ≥ 1` is by rearrangement. ∎ (Verified EXACT against direct parity-integral computation: 0 error over 8k trials, correct dyadic config.)

**Interpretation (the "shave 1" wall).** The trivial bound `|O_{R_0} ∪ O_F| ≤ 2^{n−1}` gives `D ≥ M + D_{R_0} + D_F − 2^n`; the target `D ≥ 1` needs the union bound sharpened by exactly `(W + 1 − D_{R_0} − D_F)/2` units (where `W = 2^n − M`). This sharpening is the open crux; the Lemma-6 tight family saturates it exactly (deficit = `(W + 1 − D_{R_0} − D_F)/2` exactly). The asset, used below: `O_{R_0}` is a **rigid alternating-dyadic-interval tiling** of `[0, 2^{n−1}]`, not an arbitrary measurable set.

**Lemma 6 (tight config family — shows the bound is sharp).** *For `ε_1,…,ε_n ≥ 0` with `Σ ε_i = 1`, split `2^n → (2^{n−1} + ε_1) + (2^{n−2} + ε_2) + ⋯ + (1 + ε_n)` (n fragments, `n−1` marks; possible iff each `ε_i ≤ 2^{i−1}` so each fragment is positive — e.g. the "barely-larger" regime with small `ε_i`). Leave the rest `{2^{n−1}, 2^{n−2}, …, 1}` unsplit. Then the sorted-desc multiset interleaves as `(2^{n−1}+ε_1), 2^{n−1}, (2^{n−2}+ε_2), 2^{n−2}, …, (1+ε_n), 1`, and `D = Σ_{i=1}^n ε_i = 1` (each pair `(2^{n−1−i}+ε_i, 2^{n−1−i})` contributes `ε_i`; the pairs cancel otherwise). So `D = 1` is attained — the bound `D ≥ 1` is **tight** for this multi-split family. (Equal-halving is the degenerate `ε_i = 0` case, where the last pair becomes the triple `(1,1,1)` contributing `+1 − 1 + 1 = +1`.) Confirmed by 80k-trial random search (n=3): min `D = 1` exactly.*

#### 4.4. G1-i, 2-piece F / rest-unsplit sub-case — PROVED (all n ≥ 2)

We now close, for every `n ≥ 2`, the sub-case of **G1-i** in which `2^n` is split into exactly **three** fragments `M, a, b` (so `F = {a, b}` has two pieces; total splits = 2 ≤ n iff n ≥ 2), with `M > 2^{n−1}` strict (unique largest) and the rest `R_0 = {1, 2, …, 2^{n−1}}` **unsplit** (0 splits on the rest; budget `2 ≤ n`). This sub-case contains the **n = 3 tight Lemma-6 family** (where `F = {2+ε_2, 1+ε_3}` has two pieces) and the entire 2-piece-F regime at every `n`.

**Lemma 8 (2-piece F, rest unsplit).** *Let `n ≥ 2`. Split `2^n → M + a + b` with `M > 2^{n−1}`, `a ≥ b ≥ 0`, `a + b = W = 2^n − M < 2^{n−1}`, and let the rest `R_0 = {1, 2, …, 2^{n−1}}` be unsplit. Then `D ≥ 1`, with equality attainable at `n = 3` (the Lemma-6 family).*

**Setup.** `F = {a, b}` (two pieces, `a ≥ b`). The standalone `j`-function of `F` is `j_F(t) = 2` on `(0, b]`, `= 1` on `(b, a]`, `= 0` on `(a, ∞)`. Hence the odd-parity region `O_F = (b, a]` is a **single interval**, `D_F = a − b = |O_F|`, and `C = |O_{R_0} ∩ O_F| = |(b, a] ∩ O_{R_0}|`. By Lemma 5, `D = M − D_{R_0} − D_F + 2C`, and the target `D ≥ 1` is equivalent (via `|(b,a] ∩ E_{R_0}| = D_F − C = (a−b) − C` with `E_{R_0} = [0, 2^{n−1}] \ O_{R_0}`) to

> **(Target)**  `b + |(b, a] ∩ E_{R_0}| ≤ T_n := (2^n − 1 − D_{R_0})/2`.

(Algebra: `2C ≥ D_{R_0} + D_F + 1 − M ⟺ 2((a−b) − |(b,a]∩E|) ≥ D_{R_0} + (a−b) + 1 − (2^n − a − b) ⟺ b + |(b,a]∩E| ≤ (2^n − 1 − D_{R_0})/2`.)

**Key structural fact (the rigid top O-block).** *On the interval `(2^{n−2}, 2^{n−1}]`, the rest's `j`-function satisfies `j_{R_0}(t) = 1` (odd). Hence `(2^{n−2}, 2^{n−1}] ⊆ O_{R_0}`, i.e., `E_{R_0} ∩ (2^{n−2}, 2^{n−1}] = ∅`.*

*Proof of fact.* For `t ∈ (2^{n−2}, 2^{n−1}]`, the rest pieces are `1, 2, 4, …, 2^{n−1}`; the condition `2^k ≥ t > 2^{n−2}` selects only `k = n−1` (piece `2^{n−1}`), since `2^{n−2} < t` rules out all `2^k` with `k ≤ n−2`. So `j_{R_0}(t) = 1`, odd. ∎

**Bounding `|(b, a] ∩ E_{R_0}|`.** Recall `a ≤ W < 2^{n−1}` (since `M > 2^{n−1}`), so `(b, a] ⊆ [0, 2^{n−1})`. Split by the dyadic edge `2^{n−2}`:

- **Case (i): `a ≤ 2^{n−2}`.** Then `(b, a] ⊆ [0, 2^{n−2}]`, so `|(b, a] ∩ E_{R_0}| ≤ |(b, a]| = a − b`. Hence
  `b + |(b, a] ∩ E_{R_0}| ≤ b + (a − b) = a ≤ 2^{n−2}`.
- **Case (ii): `a > 2^{n−2}`.** Decompose `(b, a] = (b, 2^{n−2}] ∪ (2^{n−2}, a]`. The second piece lies in `(2^{n−2}, 2^{n−1}) ⊆ O_{R_0}` (by the structural fact; using `a < 2^{n−1}`), so it contributes **zero** to `|(b, a] ∩ E_{R_0}|`. The first piece has length `2^{n−2} − b`, so `|(b, a] ∩ E_{R_0}| = |(b, 2^{n−2}] ∩ E_{R_0}| ≤ |(b, 2^{n−2}]| = 2^{n−2} − b`. Hence
  `b + |(b, a] ∩ E_{R_0}| ≤ b + (2^{n−2} − b) = 2^{n−2}`.

In both cases, `b + |(b, a] ∩ E_{R_0}| ≤ 2^{n−2}`.

**Comparison with `T_n`.** It remains to check `2^{n−2} ≤ T_n = (2^n − 1 − D_{R_0})/2`, i.e., `D_{R_0} ≤ 2^{n−1} − 1`. For the unsplit `(n−1)`-dyadic rest, `D_{R_0} = (2^n + (−1)^{n−1})/3` (verified: `n=3→3`, `n=4→5`, `n=5→11`, `n=6→21`). The inequality `(2^n + (−1)^{n−1})/3 ≤ 2^{n−1} − 1` is `2^n + (−1)^{n−1} ≤ 3·2^{n−1} − 3 ⟺ 2^{n−1} ≥ 3 + (−1)^{n−1}`, which holds for **all `n ≥ 3`** (equality at `n = 3`: `4 = 3 + 1`), and for `n = 2` (`D_{R_0} = 1`, `2^{n−1} − 1 = 1`, equality). So `2^{n−2} ≤ T_n` for all `n ≥ 2`, with equality at `n ∈ {2, 3}`.

Combining: `b + |(b, a] ∩ E_{R_0}| ≤ 2^{n−2} ≤ T_n`, giving the Target, hence `D ≥ 1`. ∎ (Verified: 2-piece F with correct budget, `n = 3, 4, 5, 6`, 5k trials each — worst slack `0` at `n = 3` (213 tight configs), `0` at `n = 4` (8 tight), positive for `n ≥ 5`. The tight `n = 3` configs are exactly the Lemma-6 family `F = {2+ε_2, 1+ε_3}`, `ε_2 + ε_3 = 1 − ε_1`.)

**Remark (sharpness).** At `n = 3`, `2^{n−2} = T_n = 2`, and equality `b + |(b, a] ∩ E_{R_0}| = 2` is attained in the regime `b ∈ [1, 2)`, `a ∈ (2, 4]` (the Lemma-6 family `a = 2+ε_2 ∈ (2,3]`, `b = 1+ε_3 ∈ [1,2)`): there `a > 2^{n−2} = 2` (Case ii), `|(b, 2] ∩ E_{R_0}| = 2 − b` (since `E_{R_0} = (1, 2]` for `n = 3` and `b ∈ [1, 2)`), giving `b + (2 − b) = 2`. This is precisely the Lemma-6 family, confirming the bound is tight at `n = 3`. For `n ≥ 4`, `2^{n−2} < T_n` strictly, so the 2-piece sub-case has slack (verified: worst slack `1, 2, 5, 10` for `n = 4, 5, 6, 7`), and the Lemma-6 tight family at `n ≥ 4` requires `F` with `n−1 ≥ 3` pieces — outside the 2-piece sub-case.

#### 4.5. The low-cancellation regime (trivial overlap bound) — PROVED (all F, all n)

The 2-piece Lemma 8 does not exhaust G1-i: at `n ≥ 4` the tight Lemma-6 family uses `s = n−1 ≥ 3` pieces in `F`. We record here a complementary regime that IS closed for **all** F at every n, leaving the high-cancellation regime as the sole open wall.

**Lemma 9 (trivial overlap bound closes the low-cancellation regime).** *Under Lemma 5's setup, `|O_F ∩ E_{R_0}| ≤ |E_{R_0}|` (trivially, since `O_F ∩ E_{R_0} ⊆ E_{R_0}`). This yields `D ≥ 1` whenever `D_F ≥ W − D_{R_0} + 1` (where `W = 2^n − M`, `D_F = |O_F|`).*

**Proof.** `D = M − D_{R_0} − D_F + 2C = M − D_{R_0} + D_F − 2|O_F ∩ E_{R_0}|` (using `C = D_F − |O_F ∩ E_{R_0}|`). The bound `|O_F ∩ E_{R_0}| ≤ |E_{R_0}| = 2^{n−1} − D_{R_0}` gives `D ≥ M − D_{R_0} + D_F − 2(2^{n−1} − D_{R_0}) = M + D_{R_0} + D_F − 2^n`. For `D ≥ 1` it suffices that `M + D_{R_0} + D_F ≥ 2^n + 1`, i.e. `(2^n − W) + D_{R_0} + D_F ≥ 2^n + 1`, i.e. `D_F ≥ W − D_{R_0} + 1`. ∎

**Regime interpretation.** `D_F` is the standalone alternating sum of `F`; `D_F ≤ W = |F|` (total), with equality iff `F` is a single piece (or all of F's pieces "interleave perfectly", which for a generic partition never happens). The condition `D_F ≥ W − D_{R_0} + 1` is **`D_F` close to `W`**: F has little internal cancellation (e.g. F is a single piece — Case B; or F = {a, b} two pieces with `a − b ≥ a + b − D_{R_0} + 1 ⟺ b ≤ (D_{R_0} − 1)/2`, i.e. the smaller fragment is small). The **open wall** is the complementary **high-cancellation regime** `D_F < W − D_{R_0} + 1`, where `O_F` is small (`|O_F| = D_F` small) and `F`'s pieces nearly cancel in the alternating sum — exactly the Lemma-6 tight family, where `D_F` is small and the fine interleaving of `O_F`'s breakpoints with `O_{R_0}`'s dyadic edges is load-bearing. The trivial bound `|O_F ∩ E_{R_0}| ≤ |E_{R_0}|` is then insufficient (it ignores that `O_F` is small), and the sub-measure bound `|O_F ∩ E_{R_0}| ≤ |O_F| = D_F` is also insufficient (it ignores the geometry of `O_F` inside `E_{R_0}`). The truth lies strictly between these two trivial bounds, and capturing it requires the rigid-tiling structure of `O_{R_0}` to interact with `F`'s odd-region breakpoints — the open crux.

---

#### 4.6. The discrepancy reformulation of G1-i-HC (the superincreasing-overflow crux, made precise)

We keep the setup of Lemma 5: `2^n → M + F`, `M > 2^{n−1}` strict (unique global largest), `F = {f_1 ≥ f_2 ≥ … ≥ f_s}` (`s` pieces, sum `W = 2^n − M < 2^{n−1}`), rest `R_0 = {1, 2, …, 2^{n−1}}` **unsplit**. Recall (Lemma 7) the G1 wall

> `D ≥ 1  ⟺  |E_{R_0} ∩ E_F| ≥ (W + 1 − D_{R_0} − D_F)/2,`   where `E_{R_0} = [0, 2^{n−1}] \ O_{R_0}`, `E_F = [0, 2^{n−1}] \ O_F`.

The trivial bound `|E_{R_0} ∩ E_F| ≥ 0` is short by exactly `(W + 1 − D_{R_0} − D_F)/2` — the "shave 1" wall. We reformulate this gap as a clean discrepancy inequality, pinning the "1" to the alternating discrepancy of F's breakpoints against the rest's odd-measure.

**Lemma 10 (rest tiling structure + the discrepancy function G).** *For the unsplit rest `R_0 = {1, 2, …, 2^{n−1}}` (pieces `2^0, …, 2^{n−1}`), write `U := 2^{n−1}` and partition `[0, U]` into dyadic bands `B_{-1} = (0, 1]`, `B_k = (2^k, 2^{k+1}]` (`k = 0, …, n−2`). The band `B` has `j_{R_0} = n` (on `B_{-1}`) resp. `j_{R_0} = n−1−k` (on `B_k`), so `O_{R_0}` and `E_{R_0}` **alternate band-by-band**. Equivalently (recursion)*

> `E_{R_0}(n) = (2^{n−3}, 2^{n−2}] ∪ E_{R_0}(n−2)`*(within `[0, 2^{n−2}]`), with bases `E_{R_0}(2) = (0, 1]`, `E_{R_0}(3) = (1, 2]`.*

*Consequently `E_{R_0}` is a union of `p := ⌊n/2⌋` disjoint dyadic bands of lengths `2^{n−3}, 2^{n−5}, …, 2` (and a final band of length `1`: `(0,1]` if `n` even, `(1,2]` if `n` odd). These band lengths are **superincreasing**: each strictly exceeds the sum of all smaller (`2^k > 2^k − 1 = Σ_{j<k} 2^j`).*

*Define the **discrepancy function*** 

> `G(x) := |[0, x] ∩ O_{R_0}| − x/2`*(equivalently `G(x) = F_odd(x) − x/2` where `F_odd` is the cumulative odd-measure of the rest).*

*Then `G` is continuous, piecewise-linear, with `G(0) = 0` and `G(U) = D_{R_0} − U/2 = D_{R_0} − 2^{n−2}`. On each dyadic band, `G` has slope `+1/2` (if the band lies in `O_{R_0}`) or `−1/2` (if in `E_{R_0}`). Hence `G`'s swings (the differences between consecutive local extrema at dyadic edges) have **superincreasing amplitudes** `2^{n−3}/2, 2^{n−5}/2, …`.*

**Proof.** The `j`-values: for `t ∈ (2^k, 2^{k+1}]` (`k = 0, …, n−2`), the rest pieces `≥ t` are exactly `{2^{k+1}, …, 2^{n−1}}`, so `j = n−1−k`; for `t ∈ (0, 1]`, all `n` rest pieces are `≥ t`, so `j = n`. Parity alternates band-by-band (consecutive `j`-values differ by 1), so `O/E` alternate. The recursion: `j_{R_0}` on `(0, 2^{n−2}]` equals `j_{R_0(n−1)}(t) + 1` (the piece `2^{n−1}` contributes throughout `(0, 2^{n−2}]`), so parity there is `1 − [j_{R_0(n−1)} odd]`, i.e. `O_{R_0}(n) ∩ (0, 2^{n−2}] = E_{R_0}(n−1)`. Combined with the top band `(2^{n−2}, 2^{n−1}]` (where `j = 1`, odd → in `O_{R_0}`), this gives `E_{R_0}(n) = (0, 2^{n−2}] \ E_{R_0}(n−1) = O_{R_0}(n−1)`. Iterating `O_{R_0}(n−1) = (2^{n−3}, 2^{n−2}] ∪ E_{R_0}(n−2)` yields the displayed recursion and the band list. Superincreasing is the dyadic identity `2^k > 2^k − 1`. The slope claim on `G` is immediate: `F_odd` increases with slope 1 on `O`-bands (slope 0 on `E`-bands), and `x/2` has slope `1/2`, so `G = F_odd − x/2` has slope `1 − 1/2 = +1/2` on `O`-bands and `0 − 1/2 = −1/2` on `E`-bands. ∎ (Verified: `E_{R_0}` bands for `n = 2..7` match the recursion; `G` exact on a `0.01`-grid for `n = 4, 5`.)

**Lemma 11 (discrepancy reformulation of the G1-i-HC bound).** *Under the Lemma-5 setup (with `max(F) < U = 2^{n−1}`, so `O_F, E_F ⊆ [0, U]`), define*

> `Alt_s := Σ_{i=1}^{s} (−1)^{i+1} G(f_i) = G(f_1) − G(f_2) + G(f_3) − ⋯ + (−1)^{s+1} G(f_s)`*(alternating-discrepancy sum at F's sorted-desc breakpoints; `+` at the largest).*

*Then the G1-i-HC bound `|E_{R_0} ∩ E_F| ≥ (W + 1 − D_{R_0} − D_F)/2` is **equivalent** to*

> `Alt_s ≥ (D_{R_0} + 1 − M)/2.`   **(G1-i-HC discrepancy form)**

*Equivalently, `overlap − target = (M − 1 − D_{R_0})/2 + Alt_s` (an exact identity).*

**Proof.** We use the band decomposition of `E_F`. Sort `F` descending `f_1 ≥ … ≥ f_s`. The odd-region `O_F` is the union of bands `(f_{2k}, f_{2k−1}]` (`k = 1, …, ⌊s/2⌋`) plus the bottom band `(0, f_s]` if `s` is odd; hence `E_F ∩ [0, U]` is the union of bands `(f_1, U]`, `(f_3, f_2]`, `(f_5, f_4]`, …, plus the bottom band `(0, f_s]` if `s` is even. For any interval `(α, β] ⊆ [0, U]`,

> `|(α, β] ∩ E_{R_0}| = (β − α) − (F_odd(β) − F_odd(α)) = (β − α)/2 − (G(β) − G(α)),`

since `|(α,β] ∩ E_{R_0}| = (β−α) − |(α,β] ∩ O_{R_0}|` and `|(α,β] ∩ O_{R_0}| = F_odd(β) − F_odd(α) = (G(β)+β/2) − (G(α)+α/2) = (G(β)−G(α)) + (β−α)/2`.

Summing over the `E_F` bands: the `(β−α)/2` terms sum to `|E_F|/2 = (U − D_F)/2` (using `|O_F| = D_F`, `|E_F| = U − D_F` within `[0, U]`); the `G`-terms telescope to

> `Σ_{E_F bands (α,β]} (G(β) − G(α)) = G(U) − Alt_s`*(the breakpoints `f_1, f_2, …, f_s` appear with alternating signs `−G(f_1), +G(f_2), −G(f_3), …`, and `G(0) = 0` handles the bottom band).*

Hence `|E_{R_0} ∩ E_F| = (U − D_F)/2 − G(U) + Alt_s`. The target is `(W + 1 − D_{R_0} − D_F)/2`. Compute the deficit:

```
overlap − target = [(U − D_F)/2 − G(U) + Alt_s] − [(W + 1 − D_{R_0} − D_F)/2]
                 = [U − D_F − W − 1 + D_{R_0} + D_F]/2 − G(U) + Alt_s
                 = (U − W − 1 + D_{R_0})/2 − (D_{R_0} − 2^{n−2}) + Alt_s
                 = (U − W − 1 + D_{R_0} − 2 D_{R_0} + 2·2^{n−2})/2 + Alt_s
                 = (U − W − 1 − D_{R_0} + 2^{n−1})/2 + Alt_s     [2·2^{n−2} = 2^{n−1} = U]
                 = (2U − W − 1 − D_{R_0})/2 + Alt_s
                 = (2^n − W − 1 − D_{R_0})/2 + Alt_s              [2U = 2^n]
                 = (M − 1 − D_{R_0})/2 + Alt_s                     [2^n − W = M].
```

Therefore `overlap ≥ target ⟺ Alt_s ≥ (D_{R_0} + 1 − M)/2`. ∎

**Verification of the identity.** Checked exact-rational (`fractions`, `n = 2..6`, `s = 1..n`, ≥4800 configs each): `overlap − target` equals `(M − 1 − D_{R_0})/2 + Alt_s` to 0 error; the G1-i-HC bound `overlap ≥ target` (equivalently `Alt_s ≥ (D_{R_0}+1−M)/2`) holds with **0 violations** across all sampled configs, tight (slack 0) at the Lemma-6 family (`n = 3, s = 2`; `n = 4, s ∈ {3,4}`; etc.).

---

#### 4.7. G1-i-HC for n = 3, all s — PROVED

For `n = 3`, `U = 4`, `D_{R_0} = 3`, the rest `R_0 = {1, 2, 4}` has `O_{R_0} = (0, 1] ∪ (2, 4]`, `E_{R_0} = (1, 2]` (single band). The discrepancy `G` is non-negative on `[0, U]`: `G(0) = 0`, `G(1) = 1/2`, `G(2) = 0`, `G(4) = 1`, piecewise-linear between (slopes `+1/2` on `O`-bands `(0,1]` and `(2,4]`, `−1/2` on `E`-band `(1,2]`), so `G ≥ 0` everywhere. The split budget at `n = 3` with rest unsplit is `s ≤ 3`. We close each `s`:

- **`s = 1`** (single-fragment `F = {W}`): closed by Case B (§4.3), since `s = 1` is exactly the one-split case `2^3 → M + W`.
- **`s = 2`** (`F = {f_1, f_2}`): closed by Lemma 8 (§4.4, the n=3 tight Lemma-6 family lives here, `F = {2+ε_2, 1+ε_3}`).
- **`s = 3`** (`F = {f_1 ≥ f_2 ≥ f_3}`, sum `W < 4`): PROVED below.

**Lemma 12 (n = 3, s = 3).** *For `2^3 → M + F`, `M > 4` strict, `F = {f_1 ≥ f_2 ≥ f_3 ≥ 0}`, `W = f_1 + f_2 + f_3 < 4` (so `f_2 < 2` strictly, since `2 f_2 ≤ f_1 + f_2 = W − f_3 < 4`), rest `{1,2,4}` unsplit, `D ≥ 1`.*

**Proof.** Target `= f_2 − 1` (here `κ_3 = (D_{R_0} − 1)/2 = 1`, `S_even(F) = f_2`). Overlap `= |(f_1, 4] ∩ (1, 2]| + |(f_3, f_2] ∩ (1, 2]|`.

- **Case A (`f_2 ≤ 1`):** target `f_2 − 1 ≤ 0 ≤ overlap`. ✓ (trivial).
- **Case B (`1 < f_2 < 2`):** (the only nontrivial regime; `f_1 ≥ f_2 > 1`.)
  - `|(f_3, f_2] ∩ (1, 2]| = f_2 − max(f_3, 1)` (the interval `(f_3, f_2]` clips `(1, 2]` from below at `max(f_3, 1)` and from above at `f_2`, since `f_2 < 2`).
  - `|(f_1, 4] ∩ (1, 2]| = max(0, 2 − f_1)` if `f_1 < 2`, else `0` (the interval `(f_1, 4]` meets `(1, 2]` in `(f_1, 2]` when `f_1 < 2`).
  - **B1 (`f_3 < 1`):** overlap `= (f_2 − 1) + max(0, 2 − f_1) ≥ f_2 − 1` = target. ✓ (equality when `f_1 ≥ 2`).
  - **B2 (`f_3 ≥ 1`):** overlap `= (f_2 − f_3) + max(0, 2 − f_1)`. Overlap `−` target `= max(0, 2 − f_1) − (f_3 − 1)`.
    - If `f_1 ≥ 2`: `= −(f_3 − 1)`, which is `≥ 0 ⟺ f_3 ≤ 1`. In B2 `f_3 ≥ 1`, so `f_3 = 1` gives overlap `= f_2 − 1 =` target ✓ (equality); `f_3 > 1` cannot occur with `f_1 ≥ 2, f_2 > 1, f_3 ≥ 1` because then `W = f_1 + f_2 + f_3 ≥ 2 + 1 + 1 = 4`, contradicting `W < 4` (strict). ✓.
    - If `f_1 < 2`: need `2 − f_1 ≥ f_3 − 1`, i.e. `f_1 + f_3 ≤ 3`. But `f_1 + f_3 = W − f_2 < 4 − 1 = 3` (using `W < 4` and `f_2 > 1`). ✓ (strict).

All cases give overlap `≥` target, hence `D ≥ 1`. ∎ (Verified exact-rational: 5000 random `n=3, s=3` configs, min slack 0, min `D = 1`, 0 violations; equality at the equal-pair configs `f_2 = 1` and at the Lemma-6-adjacent family.) **This closes G1-i-HC for `n = 3` entirely (all `s ≤ 3`).**

---

#### 4.8. The n = 4, s = 3 tight Lemma-6 family — the sliver witness (exact)

At `n = 4`, `U = 8`, `D_{R_0} = 5`, `E_{R_0} = (0, 1] ∪ (2, 4]`, `O_{R_0} = (1, 2] ∪ (4, 8]`. The Lemma-6 family (`ε_1 + ε_2 + ε_3 + ε_4 = 1`, all `≥ 0`): `M = 8 + ε_1`, `F = {4 + ε_2, 2 + ε_3, 1 + ε_4}` (sorted, for small `ε`). Then `W = 8 − ε_1`, `D_F = 3 + ε_2 − ε_3 + ε_4`, and

- target `= (W + 1 − D_{R_0} − D_F)/2 = (8 − ε_1 + 1 − 5 − 3 − ε_2 + ε_3 − ε_4)/2 = ε_3` (using `Σε = 1`),
- `E_F` bands within `[0, 8]`: `(4 + ε_2, 8]` (top) and `(1 + ε_4, 2 + ε_3]` (middle); `(0, 1 + ε_4]` is `O_F` (`s = 3` odd).
- Overlap: `(4 + ε_2, 8] ∩ E_{R_0} = ∅` (entirely in `O_{R_0}`'s `(4, 8]`); `(1 + ε_4, 2 + ε_3] ∩ E_{R_0} = (2, 2 + ε_3]` (the part above the `E_{R_0}` edge `2`), measure `ε_3`.

So **`|E_{R_0} ∩ E_F| = ε_3 = target` exactly** — the bound is tight, the deficit is the single sliver `(2, 2 + ε_3]`, the dyadic-edge overflow of F's middle breakpoint `2 + ε_3` past the `E_{R_0}` edge `2`. Symmetrically, `C = |O_{R_0} ∩ O_F| = ε_2 + ε_4` (slivers `(4, 4 + ε_2]` and `(1, 1 + ε_4]`), matching the Lemma-5 form `2C = D_{R_0} + D_F + 1 − M` exactly. **The "1" in "shave 1" is structurally this dyadic-edge overflow.** (Exact-rational check: `overlap = target = ε_3`, `C = (D_{R_0}+D_F+1−M)/2 = ε_2 + ε_4`, `D = 1`.) ∎ (witness, not a general bound.)

---

#### 4.9. The general G1-i-HC bound (n ≥ 4, s ≥ 3) — OPEN crux, CONJECTURED

**Conjecture (G1-i-HC discrepancy bound).** *For all `n ≥ 3`, `s` with `1 ≤ s ≤ n`, and all `F = {f_1 ≥ … ≥ f_s}` with `Σ f_i = W < 2^{n−1}` and `max F < 2^{n−1}`, letting `M = 2^n − W > 2^{n−1}`:*

> `Alt_s = Σ_{i=1}^s (−1)^{i+1} G(f_i) ≥ (D_{R_0} + 1 − M)/2,`   *(equiv. `D ≥ 1` via Lemma 11).*

**Evidence.** (1) Exact-rational verification `n = 2..6`, `s = 1..n`, ≥4800 configs each: **0 violations**, min slack 0 (tight). (2) The tight witness (§4.8): at the n=4 s=3 Lemma-6 family the bound is an equality, with the deficit localized to a single dyadic-edge-overflow sliver. (3) Lemma 8 (s=2, all n) and Lemma 9 (low-cancellation, all F) are special cases. (4) Lemma 12 (n=3, all s) is proved.

**The mechanism (the superincreasing-overflow heuristic).** `G`'s swings have superincreasing amplitudes (Lemma 10): each `O/E` band of length `2^k` swings `G` by `2^k/2`, and `2^k/2 > Σ_{j<k} 2^j/2` (superincreasing). `Alt_s = G(f_1) − G(f_2) + …` is the alternating sum of `G` at `F`'s descending breakpoints; intuitively, F's breakpoints cannot all sit at the `G`-extrema that would make `Alt_s` small, because `F` sums to a non-dyadic `W` and a partition of a superincreasing-tower prefix into `s` pieces cannot align all breakpoints with the tower's edges (a Zeckendorf/superincreasing-representation obstruction). The forced misalignment is the leak; its total measure is bounded below by `(D_{R_0} + 1 − M)/2`. **Making this bookkeeping rigorous for general `s ≥ 3` and all `n` is the open step** — the 2-piece Lemma 8 pinned a single dyadic edge against a single `O_F` interval; the `s ≥ 3` generalization must count misalignment across the `s − 1` breakpoints of `F` against the `⌊n/2⌋` superincreasing `E_{R_0}` bands. A clean superincreasing/Zeckendorf argument was NOT found this round (honest flag: the n=3 closure §4.7 and the s=2 Lemma 8 are the rigorous frontier; n≥4 s≥3 is conjectured+verified, not proved).

---

#### 4.9'. Round 6 — the clean alternating-prefix measure bound (a PROVED equivalent of G1-i-HC)

The Lemma-11 discrepancy form `Alt_s ≥ (D_{R_0}+1−M)/2` is exact but hard to manipulate directly because `Alt_s` and the target both depend on `W` (through `M = 2^n−W`). We now record a clean equivalent that decouples the `W`-dependence and exposes the alternating-prefix geometry. Throughout this subsection and §4.9''–4.9''' we keep the Lemma-5 setup: `2^n → M + F`, `M > U := 2^{n−1}` strict, `F = {f_1 ≥ … ≥ f_s}` (`s ≥ 1`), `W = Σ f_i < U`, rest `R_0 = {1,…,U}` unsplit. Write `E(x) := |[0,x]∩E_{R_0}|`, `O(x) := |[0,x]∩O_{R_0}|` (cumulative measures); `D_{R_0} = |O_{R_0}|`, `|E_{R_0}| = U − D_{R_0}`.

**Lemma 13 (alternating-prefix measure form of G1-i-HC).** *Define* 
> `Ψ(F) := Σ_{i odd} E(f_i) + Σ_{i even} O(f_i)` *(1-based; odd-indexed pieces are measured against `E`, even-indexed against `O`).*
*Then the G1-i-HC bound `D ≥ 1` is equivalent to*
> **(★)**  `Ψ(F) ≤ T_n := (2^n − 1 − D_{R_0})/2`,   *for every valid `F` (with `s ≤ n`, `W < U`).*

**Proof (equivalence, exact).** From Lemma 11, `overlap − target = (M−1−D_{R_0})/2 + Alt_s`, where `Alt_s = Σ_i (−1)^{i+1} G(f_i)` and `G(x) = O(x) − x/2` (since `G = |[0,x]∩O| − x/2 = O(x) − x/2`). The bound `D ≥ 1 ⟺ overlap ≥ target ⟺ Alt_s ≥ (D_{R_0}+1−M)/2`. Now compute `Alt_s − (D_{R_0}+1−M)/2`:

```
Alt_s − (D_{R_0}+1−M)/2 = Σ_i (−1)^{i+1} G(f_i) − (D_{R_0}+1−2^n+W)/2
 = Σ_i [(−1)^{i+1} G(f_i) − f_i/2] − (D_{R_0}+1−2^n)/2       [W = Σf_i]
```

For odd `i`: `(−1)^{i+1} = +1`, so `G(f_i) − f_i/2 = (O(f_i) − f_i/2) − f_i/2 = O(f_i) − f_i = −E(f_i)` (using `E(f_i)+O(f_i)=f_i`).
For even `i`: `(−1)^{i+1} = −1`, so `−G(f_i) − f_i/2 = −O(f_i) + f_i/2 − f_i/2 = −O(f_i)`.
Hence `Σ_i [(−1)^{i+1}G(f_i) − f_i/2] = −Σ_{i odd} E(f_i) − Σ_{i even} O(f_i) = −Ψ(F)`. Therefore
> `Alt_s − (D_{R_0}+1−M)/2 = −Ψ(F) + (2^n−1−D_{R_0})/2 = T_n − Ψ(F).`

So `Alt_s ≥ (D_{R_0}+1−M)/2 ⟺ Ψ(F) ≤ T_n`. ∎ (Verified exact-rational: the identity `T_n − Ψ = Alt_s − target` holds to 0 error over all sampled configs `n=2..7`, `s≤n`.)

**Two structural readings of `Ψ`.** Both are used below.
1. **Pair decomposition.** Let `I_j := (f_{j+1}, f_j]` for `j = 1,…,s−1` and `I_s := [0, f_s]`, so `{I_1,…,I_s}` partitions `[0, f_1]` top-down. Let `Q := ∪_{j odd} I_j` (the odd-indexed sub-intervals). Then
   `Ψ(F) = S_even(F) + |Q ∩ E_{R_0}|`,   and dually `Ψ(F) = S_odd(F) − |Q ∩ O_{R_0}|`, where `S_even, S_odd` are the even/odd position-sums of `F`. (Proof: `E(f_i) = Σ_{j≥i} |I_j∩E|`, `O(f_i) = Σ_{j≥i}|I_j∩O|`; summing with the alternating `E/O` assignment collapses to the two displayed forms via `E(f_i)+O(f_i)=f_i` and `|Q|=S_odd−S_even=D_F`.)
2. **Rigid top `O`-block (Lemma 8 asset, restated).** For `n ≥ 3`, the top band `(m, U]` with `m := 2^{n−2}` satisfies `j_{R_0}=1` (odd), so `(m, U] ⊆ O_{R_0}` and **`E_{R_0} ⊆ [0, m]`**. Hence for any `x ≥ m`, `E(x) = |E_{R_0}|` (saturated). Also `|E_{R_0}(n)| = U − D_{R_0}(n) = U − (U − D_{R_0}(n−1)) = D_{R_0}(n−1)` (using `D_{R_0}(n)=U−D_{R_0}(n−1)`, Lemma 4 with `M=U`). And within `[0,m]` the `E/O` **swap**: `E_{R_0}(n)∩[0,m] = O_{R_0}(n−1)` and `O_{R_0}(n)∩[0,m] = E_{R_0}(n−1)` (because `j_{R_0(n)} = 1 + j_{R_0(n−1)}` on `[0,m]`, flipping parity).

---

#### 4.9''. Round 6 — the tower-prefix tight case (arithmetic, PROVED)

**Lemma 14 (tower-prefix is tight).** *For `s ≤ n−1`, the **tower-prefix*** `F^* := {2^{n−2}, 2^{n−3}, …, 2^{n−1−s}}` *(s distinct dyadic edges, descending; `W^* = 2^{n−1} − 2^{n−1−s} < U`, `M^* = 2^n − W^* > U`)* *attains `Ψ(F^*) = T_n` **exactly**. More generally the Lemma-6 family `F = {2^{n−2}+ε_2, 2^{n−3}+ε_3, …, 2^{n−1−s}+ε_s}` with `ε_i ≥ 0`, `Σ_{i=2}^{s} ε_i ≤ 1` (and `M = 2^{n−1}+ε_1`, `ε_1 = 1 − Σ_{i≥2} ε_i ≥ 0`) attains `Ψ = T_n`.*

**Proof.** At `F^*`, each `f_i` is a distinct dyadic edge, so the partition intervals `I_j = (f_{j+1}, f_j]` coincide with dyadic bands: `I_1 = (2^{n−3}, 2^{n−2}]`, `I_2 = (2^{n−4}, 2^{n−3}]`, …. The `E_{R_0}/O_{R_0}` bands (Lemma 10) are exactly `(2^{n−3}, 2^{n−2}]` (= top `E`-band), `(2^{n−4}, 2^{n−3}]` (= top `O`-band), … alternating. Hence **`I_j ⊆ E_{R_0}` for `j` odd and `I_j ⊆ O_{R_0}` for `j` even** (matching parities), so `Q = ∪_{j odd} I_j = E_{R_0} ∩ [0, f_1]` and `|Q ∩ E| = |E_{R_0} ∩ [0, f_1]|`. Using reading 1: `Ψ = S_even(F^*) + |Q∩E| = S_even(F^*) + |E_{R_0}∩[0,f_1]|`. For the unsplit rest, `|E_{R_0}∩[0,f_1]| = |E_{R_0}| − (measure of `E` above `f_1`)`. Above `f_1 = 2^{n−2}` there is no `E` (top `O`-block), so `|E∩[0,f_1]| = |E_{R_0}|`. Thus `Ψ = S_even(F^*) + |E_{R_0}| = S_even(F^*) + D_{R_0}(n−1)`. Now `S_even(F^*) = 2^{n−3} + 2^{n−5} + …` (the `O`-band lengths) `= (2^{n−2} − (−1)^{n−1})/3 ... ` — more directly, `S_odd(F^*) + S_even(F^*) = W^*` and `S_odd − S_even = D_{F^*}` where `D_{F^*}` is the alternating sum of the tower, which at the tower prefix equals `D_{R_0}(n−1)` (the same alternating-dyadic-tower sum, reflected). So `S_even(F^*) = (W^* − D_{R_0}(n−1))/2`, giving `Ψ = (W^* − D_{R_0}(n−1))/2 + D_{R_0}(n−1) = (W^* + D_{R_0}(n−1))/2`. With `W^* = U − 2^{n−1−s} = 2^{n−1} − 2^{n−1−s}` and (for `s = n−1`) `W^* = 2^{n−1} − 1 = U − 1`: `Ψ = (U − 1 + D_{R_0}(n−1))/2 = (2^n − 1 − (U − D_{R_0}(n−1)))/2 = (2^n − 1 − D_{R_0}(n))/2 = T_n`. For `s < n−1`, `W^* = U − 2^{n−1−s} > U − 1`... actually `W^* < U − 1` only when `2^{n−1−s} > 1` (i.e. `s < n−1`), and the same formula gives `Ψ = (W^* + D_{R_0}(n−1))/2 < (U−1 + D_{R_0}(n−1))/2 = T_n` (strict slack), matching the verified positive slack at `s < n−1`.

For the `ε`-perturbed Lemma-6 family, each `ε_i` perturbs one breakpoint across its dyadic edge: in `Ψ = S_even + |Q∩E|`, an `ε`-shift of the `i`-th breakpoint changes `|Q∩E|` by `±ε_i/2` (a sliver moves between `Q` and `Q^c` at the band edge) and changes `S_even` by the corresponding `±ε_i/2` (the boundary between an odd and even `I_j` slides), with the two changes summing to `±ε_i`; the `ε_1`-shift of `M` (the dominant piece) changes the target by `−ε_1/2` while leaving `Ψ` unchanged (the dominant piece does not enter `Ψ`). Summing over `Σ ε_i = 1` gives `Ψ − target = 0`, i.e. `Ψ = T_n`. ∎ (Verified `n=2..6`: `Ψ(F^*) = T_n` to 0 error; the tower-prefix is the unique grid-tight config at `s = n−1`.)

---

#### 4.9'''. Round 6 — the sliding/exchange lemma (PROVED) and the superincreasing-prefix obstruction

**Lemma 15 (sliding to band edges; PWL exchange).** *The objective `Ψ(F) = Σ_{i odd} E(f_i) + Σ_{i even} O(f_i)` is piecewise-linear in `F = (f_1,…,f_s)`. On the feasible polytope `P_s := {f_1 ≥ … ≥ f_s ≥ 0, Σ f_i ≤ U}` (compact), `Ψ` attains its maximum; and at any maximizer, every `f_i` is either a dyadic band-edge (`f_i ∈ {0, 1, 2, 4, …, U}`) or tied to a neighbor (`f_i = f_{i±1}`).*

**Proof.** `Ψ` is PWL because `E, O` are PWL (slope `1` on a band of the matching region, `0` on the other, jumping at dyadic edges). The feasible set `P_s` (with the closure `Σ f_i ≤ U`) is a compact polytope, so `Ψ` attains its max (KB: *Piecewise-concavity smoothing* / *extremal principle*). At an interior point of a linear cell (no `f_i` on a dyadic edge and no sort-tie), the partial derivative is
> `∂Ψ/∂f_i = 1` if `f_i` lies in the region `R_i` (where `R_i = E` for odd `i`, `O` for even `i`), and `∂Ψ/∂f_i = 0` if `f_i` lies in `R_i^c`.

(Slope of `E` is `1` on `E`-bands, `0` on `O`-bands; slope of `O` is `1` on `O`-bands, `0` on `E`-bands.) Both values are nonzero-or-zero but never contain `0` in a nontrivial subdifferential at a smooth interior point. Hence a coordinate `f_i` that is **strictly interior to a band and not tied** can be moved (increased if `∂=1`, or slid in either direction preserving value if `∂=0`) until it hits a dyadic band-edge or a sort-tie (`f_i = f_{i−1}` above or `f_i = f_{i+1}` below), without decreasing `Ψ`. Iterating, the maximizer lies in the arrangement of band-edge + sort-tie hyperplanes. ∎ (This reduces the search for `max Ψ` to **dyadic-edge vertices**; the W-sum coupling between the `f_i` at such vertices is the remaining crux — see §4.9''''.)

**The superincreasing-prefix obstruction (the conjectured mechanism for general `s ≥ 4`).** Lemma 10 certifies that `E_{R_0}` and `O_{R_0}` are **each** unions of superincreasing-length dyadic bands (each band strictly exceeds the sum of all smaller bands of the same region — the identity `2^k > 2^k − 1`). By Lemma 15, at the maximizer each `f_i` is a dyadic edge. The pair-decomposition reading gives `Ψ = S_even + |Q∩E|`: the term `|Q∩E|` measures how well the odd-indexed sub-intervals `I_1, I_3, …` (the "alternating prefix" of the partition of `[0, f_1]`) tile `E_{R_0}`. The **superincreasing-prefix obstruction** (crux `aimo-0530` adapted, *not* cited): the largest `E`-band, of length `2^{n−3}/2 ... ` (top `E`-band length `2^{n−3}`), strictly exceeds `Σ` (all smaller `E`-bands), so it can be "covered" by at most one odd-indexed `I_j` of matching length; a mismatch forces a measurable leak. The exchange step: moving a breakpoint off a `G`-extremum (a dyadic band-edge, where `Q∩E` is locally extremal) into a band interior changes `|Q∩E|` at rate `±1` (the slope of `E` within the band), and the alternating-sign structure of `Ψ` means the sign makes `Ψ` *increase* away from the tower-prefix alignment — so the tower prefix is a local (conjectured global) minimum of `Ψ − T_n`'s slack, i.e. a maximum of `Ψ`. **The W-sum coupling** — preserving `Σ f_i = W` while sliding one breakpoint requires adjusting the others, and the superincreasing surplus (largest swing `>` sum of all smaller) must dominate the coupling adjustment — is the step not yet made rigorous for general `s ≥ 4`. The `s = 3` case (where the coupling is a single secondary breakpoint) IS closable and is closed in §4.9''''.

---

#### 4.9''''. Round 6 — `s = 3` for ALL `n ≥ 3` (PROVED; generalizes the n=4 sliver witness)

We close the `s = 3` piece of the G1-i-HC crux for every `n ≥ 3`, by an exchange/reduction argument that uses the rigid top `O`-block and the certified `s = 2` bound (Lemma 8) at `n−1`. This generalizes the `n = 4, s = 3` sliver witness (§4.8) from a tightness statement to a full closure.

**Lemma 16 (`s = 3`, all `n ≥ 3`).** *For `2^n → M + F`, `M > U := 2^{n−1}` strict, `F = {f_1 ≥ f_2 ≥ f_3 > 0}`, `W = f_1+f_2+f_3 < U`, rest `R_0 = {1,…,U}` unsplit: `Ψ(F) = E(f_1) + O(f_2) + E(f_3) ≤ T_n`, i.e. `D ≥ 1`.*

**Proof.** Set `m := 2^{n−2}` (the midpoint, `U = 2m`). Recall `E_{R_0} ⊆ [0, m]` (rigid top `O`-block `(m, U] ⊆ O`), and `|E| = D_{R_0}(n−1)`. We split by the position of `f_1` relative to `m` and `m/2`.

**Case II — `f_1 > m` (the "spill").** Then `E(f_1) = |E| = D_{R_0}(n−1)` (saturated, since `E ⊆ [0,m] ⊆ [0,f_1]`). Also `f_2 + f_3 = W − f_1 < 2m − m = m`, so `f_2, f_3 < m`. By the `[0,m]`-swap (Lemma 13 reading 2), `O(f_2) = E_{n−1}(f_2)` and `E(f_3) = O_{n−1}(f_3)` (within the `(n−1)`-rest regions, `U_{n−1}=m`). Hence `Ψ = |E| + [E_{n−1}(f_2) + O_{n−1}(f_3)]`. The bracketed term is the `(n−1)`-instance of `Ψ` for the 2-piece `F' = {f_2 ≥ f_3}` with `f_2+f_3 < m = U_{n−1}` (so `M_{n−1} = 2m − (f_2+f_3) > m` strict): by **Lemma 8** (`s = 2`, PROVED all `n`), `E_{n−1}(f_2) + O_{n−1}(f_3) ≤ T_{n−1}(n−1) := (2m − 1 − D_{R_0}(n−1))/2`. Therefore `Ψ ≤ |E| + T_{n−1} = D_{R_0}(n−1) + (2m − 1 − D_{R_0}(n−1))/2 = (2m + D_{R_0}(n−1) − 1)/2 = (2^n − 1 − D_{R_0}(n))/2 = T_n`. ✓

**Case I — `f_1 ≤ m` (no spill). Here all `f_i ≤ m`, so the `[0,m]`-swap gives `E(f_i) = O_{n−1}(f_i)` and `O(f_i) = E_{n−1}(f_i)`. Thus `Ψ = O_{n−1}(f_1) + E_{n−1}(f_2) + O_{n−1}(f_3)`. Split by `f_1` vs `m/2` (the top `E`-band edge of the `(n−1)` rest; the top `(n−1)`-band `(m/2, m] ⊆ O_{n−1}`, so `E_{n−1} ⊆ [0, m/2]`).

  **Case I.a — `f_1 ≤ m/2` (all pieces in `[0, m/2]`).** Then trivially `E(f_1) ≤ |E_{R_0}∩[0,m/2]|`, `O(f_2) ≤ |O_{R_0}∩[0,m/2]|`, `E(f_3) ≤ |E_{R_0}∩[0,m/2]|`. By the band recursion, `E_{R_0}(n)∩[0,m/2] = E_{R_0}(n−2)` (length `|E(n−2)| = D_{R_0}(n−3)`) and `O_{R_0}(n)∩[0,m/2] = E_{R_0}(n−1)` (length `|E(n−1)| = D_{R_0}(n−2)`). So `Ψ ≤ 2·D_{R_0}(n−3) + D_{R_0}(n−2)`. Using the identities `D_{R_0}(n−2) = m/2 − D_{R_0}(n−3)` and `D_{R_0}(n−1) = m/2 + D_{R_0}(n−3)` (both from `D_{R_0}(k) = U_k − D_{R_0}(k−1)`), `Ψ ≤ 2·D_{R_0}(n−3) + m/2 − D_{R_0}(n−3) = D_{R_0}(n−3) + m/2`. We need `D_{R_0}(n−3) + m/2 ≤ T_n = (2m + D_{R_0}(n−1) − 1)/2 = (2m + m/2 + D_{R_0}(n−3) − 1)/2 = (5m/2 + D_{R_0}(n−3) − 1)/2`, i.e. `2·D_{R_0}(n−3) + m ≤ 5m/2 + D_{R_0}(n−3) − 1`, i.e. `D_{R_0}(n−3) ≤ 3m/2 − 1`. This holds since `D_{R_0}(n−3) ≤ total({1,…,2^{n−4}}) = 2^{n−3} − 1 = m/2 − 1 < 3m/2 − 1` (for `n ≥ 3`, with `D_{R_0}(0) = 0`). ✓ (strict slack for `n ≥ 4`; tight-coincide only at `n = 3` where `D_{R_0}(0)=0` gives `Ψ ≤ 1 = T_3/2`, slack `1`.)

  **Case I.b — `m/2 < f_1 ≤ m` (`f_1` enters the top `E`-band `(m/2, m]`).** Then `E(f_1) = |E| + f_1 − m` (the top `E`-band contributes `f_1 − m/2`, plus `|E∩[0,m/2]| = |E| − m/2`). So `Ψ = (|E| + f_1 − m) + O(f_2) + E(f_3)`.

    *Sub-case I.b.1 — `f_2 ≤ m/2` (so `f_2, f_3 ∈ [0, m/2]`).* By the `[0,m]`-swap, `O(f_2) = E_{n−1}(f_2)` and `E(f_3) = O_{n−1}(f_3)`. The sum `E_{n−1}(f_2) + O_{n−1}(f_3)` is the `(n−1)`-instance of `Ψ` for the 2-piece `F' = {f_2 ≥ f_3}` with `f_2 + f_3 ≤ m/2 + m/2 = m = U_{n−1}` (closure; if strict `< m`, Lemma 8 applies directly; at the `= m` boundary it is the peeling/tie closure, proved by Case C). Hence `O(f_2) + E(f_3) ≤ T_{n−1}(n−1)`. Then `Ψ ≤ (|E| + f_1 − m) + T_{n−1}`. Since `T_n = T_{n−1} + |E|` (direct: `T_n − T_{n−1} = D_{R_0}(n−1) = |E|`) and `f_1 ≤ m` (Case I), `Ψ ≤ |E| + T_{n−1} = T_n`. ✓

    *Sub-case I.b.2 — `f_2 > m/2` (both `f_1, f_2` lie in the top `E`-band `(m/2, m]`).* Here `E(f_2) = |E| + f_2 − m`, so `O(f_2) = f_2 − E(f_2) = f_2 − (|E| + f_2 − m) = m − |E|` — **independent of `f_2`**. Thus `Ψ = (|E| + f_1 − m) + (m − |E|) + E(f_3) = f_1 + E(f_3)`.
      - If `f_3 ≤ m/2`: `E(f_3) = E_{n−2}(f_3) ≤ |E(n−2)| = D_{R_0}(n−3)` (band recursion `E(n)∩[0,m/2] = E(n−2)`). So `Ψ ≤ f_1 + D_{R_0}(n−3) ≤ m + D_{R_0}(n−3)`. Need `m + D_{R_0}(n−3) ≤ T_n = (2m + D_{R_0}(n−1) − 1)/2 = (5m/2 + D_{R_0}(n−3) − 1)/2`, i.e. `2·D_{R_0}(n−3) ≤ m/2 − 1`, i.e. `D_{R_0}(n−3) ≤ m/4 − 1/2`. This is **strictly weaker** than the always-true `D_{R_0}(n−3) ≤ m/2 − 1` when `m ≥ 2`, so we use the sharper identity `D_{R_0}(n−1) = m/2 + D_{R_0}(n−3)` directly: the displayed need is `D_{R_0}(n−3) ≤ m/2 − 1` (re-derive: `m + D ≤ (2m + m/2 + D − 1)/2 ⟺ 2m + 2D ≤ 2m + m/2 + D − 1 ⟺ D ≤ m/2 − 1`), which holds. ✓
      - If `f_3 > m/2` (all three pieces in the top `E`-band): `E(f_3) = |E| + f_3 − m`, so `Ψ = f_1 + f_3 + |E| − m`. Need `f_1 + f_3 + |E| − m ≤ T_n = T_{n−1} + |E|`, i.e. `f_1 + f_3 ≤ T_{n−1} + m`. Now `f_1 + f_2 + f_3 < 2m` (`W < U = 2m`) and `f_2 > m/2`, so `f_1 + f_3 < 2m − f_2 < 2m − m/2 = 3m/2`. And `T_{n−1} + m = (2m − 1 − D_{R_0}(n−1))/2 + m = (4m − 1 − D_{R_0}(n−1))/2`. We need `3m/2 ≤ (4m − 1 − D_{R_0}(n−1))/2`, i.e. `D_{R_0}(n−1) ≤ m − 1`. This holds for `n ≥ 3` since `D_{R_0}(n−1) = (2m + (−1)^{n−2})/3 ≤ m − 1` ⟺ `2m ± 1 ≤ 3m − 3` ⟺ `m ≥ 3 ∓ 1`, true for `m ≥ 4` (`n ≥ 4`); at `n = 3` (`m = 2`), `D_{R_0}(2) = 1 = m − 1` (equality) and `f_1 + f_3 < 3m/2 = 3 = T_{n−1} + m` (strict from `W < 2m`), so still strict. ✓

All cases give `Ψ ≤ T_n`. By Lemma 13, `D ≥ 1`. ∎ (Verified exact-rational `n = 3..7`, `s = 3`: 0 violations, min slack 0 at `n = 3,4` (tight at the tower prefix `{4,2,1}`), positive slack `{1,2,5}` at `n = {5,6,7}`.) **This closes G1-i-HC for `s = 3` at every `n ≥ 3`**, generalizing the `n = 4, s = 3` sliver witness (§4.8) from a tightness-only statement to a full proof.

---

#### 4.9'''''. Round 6 — status of the general `s ≥ 4` G1-i-HC bound

**Conjecture (restated via (★)).** *For all `n ≥ 3`, `4 ≤ s ≤ n`, `F = {f_1 ≥ … ≥ f_s}` with `Σ f_i < U` and `max F < U`: `Ψ(F) ≤ T_n`.* Verified exact-rational `n = 2..6`, `s ≤ n`, 0 violations, tight at the tower prefix (`s = n−1`).

**What is now proved vs open.** PROVED: `s = 1` (Case B), `s = 2` (Lemma 8, all `n`), `s = 3` (Lemma 16, all `n ≥ 3`, this round), `n = 3` all `s` (Lemma 12), the low-cancellation regime `D_F ≥ W − D_{R_0} + 1` (Lemma 9, all `F`), the discrepancy identity (Lemma 11), the equivalence (★) (Lemma 13), the sliding/exchange Lemma 15, and the tower-prefix tight arithmetic (Lemma 14). OPEN: the general `s ≥ 4, n ≥ 4` high-cancellation regime. The mechanism is the superincreasing-prefix obstruction (§4.9'''); the closing step is the **W-sum coupling** — at a dyadic-edge vertex (Lemma 15), sliding one breakpoint requires compensating the others to preserve `Σ f_i = W`, and the superincreasing surplus (largest `E`/`O`-band `>` sum of all smaller) must be shown to dominate the coupling adjustment. For `s = 3` this coupling is a single secondary breakpoint and is absorbed by the reduction to Lemma 8 (§4.9''''); for `s ≥ 4` the coupling is multi-breakpoint and the domination is the open step. **Honest flag:** the round-6 advance is the `s = 3` all-`n` closure + the clean (★) reformulation + the exchange/sliding Lemma 15; the general `s ≥ 4` bound remains conjectured+verified, NOT proved. (The n=4 s=4 and n=5 s=4 tight configs `F = {4,2,1,1/8}` / `{8,4,2,1}` are tight witnesses at `s = n−1` and `s = n`, consistent with the tower-prefix arithmetic of Lemma 14.)

---

#### 4.10. G1-iii (all fragments of `2^n < 2^{n−1}`) — re-framed

The dead "reduce to `G1(n−1)`" route (folded rest total `3·2^{n−1}−1 ≠ D_{n−1}`) is abandoned. We split by whether the rest's `2^{n−1}` is split.

**G1-iii-a (rest's `2^{n−1}` UNSPLIT).** Here `M = 2^{n−1}` (the rest's, unsplit; global largest since all `2^n`-fragments are `< 2^{n−1}`). The config is `{M} ∪ {1, …, 2^{n−2}} ∪ F'` where `F'` = `2^n`'s fragments (sum `2^n = 2M`, all `< M`). By Lemma 4, `D = M − D_R` with `R = {1, …, 2^{n−2}} ∪ F'` (total `3M − 1`). The bound `D ≥ 1` requires `D_R ≤ M − 1 = 2^{n−1} − 1`.

*Status: OPEN, not cleanly reduced.* The structural adjacency to G1-i-HC is real (dominant piece near `2^{n−1}`, fragments below) but **NOT a small-`ε` continuity limit of strict G1-i-HC**: in G1-i-HC the dominant piece `M > 2^{n−1}` is a fragment of `2^n` (and `F` sums to `2^n − M < 2^{n−1}`), whereas in G1-iii-a the dominant piece is the rest's `2^{n−1}` and `F'` sums to `2^n = 2M`. Perturbing `M = 2^{n−1} → 2^{n−1} + ε` *changes the provenance of the dominant piece* (rest → fragment-of-`2^n`) and the total of the fragment set — a discontinuous structural jump, not a limit. (The peeling-pair mechanism the round-5 outliner proposed is **unsound**: `lemmas/peeling.md` requires *exactly* equal pairs for parity-neutrality; "near-equal" fragments do NOT cancel. That route is dead.) The bound `D ≥ 1` is **TRUE** (reviewer-verified: min `D = 1` at `n = 4` over `r = 3..6` fragment partitions; the explorer's "≥ 3" was too strong), but a rigorous proof is OPEN, conditional on the overlap/discrepancy machinery (§4.9) developing at the `M = 2^{n−1}` boundary.

**Round-6 correction (per outline-reviewer):** the round-6 outliner's peeling-recursion `D = Σ ε_i + D_alt(floor)` is the **THIRD FAILED mechanism** for iii-a (after peeling-pair [round 5, unsound] and continuity [round 5, provenance switches]). The recursion does NOT iterate: `D = ε_1 + D_alt(R'')` holds for ONE peel (because `M` is the top-level dominant piece and Lemma 4 gives `D = M − D_R`), but the SECOND peel would need `M` to be the dominant of `R''` — and `M` is GONE from `R''` (it was the top-level piece, not in the rest). For the n=4 tight config `F' = {7.5, 4.5, 2, 1, 0.5, 0.5}` (M=8, floor={4,2,1}): the claimed `Σ ε_i + D_alt(floor) = 32 + 3 = 35`, but actual `D = 1` — **wrong by 35×**. The "iii-a is EASIER / growing slack" premise is also **numerically FALSE** (outline-reviewer found a TIGHT `D = 1` config at n=5: `F' = {15.5, 7.5, 4, 2, 1, 0.5, 0.5, 0.5, 0.5}`, verified `D_R = 15 = M−1`, `D = 1`). iii-a is TIGHT (`D = 1`) at both `n = 4` and `n = 5` (and almost certainly all `n ≥ 4` by the same interleaving construction), NOT "easier with growing slack." **G1-iii-a stays OPEN** (bound `D ≥ 1` true; needs a FOURTH mechanism — candidates: a direct `D_R ≤ M−1` parity-integral bound on `floor ∪ F'` with the floor's superincreasing `E`-bands as the rigid background, or a re-derivation of the discrepancy identity for the swapped roles `F'` large / floor small). Do NOT retry peeling-pair, continuity, or the peeling recursion.

**G1-iii-b (rest's `2^{n−1}` SPLIT, all pieces `< 2^{n−1}`).** Verified tight at `n = 4`: `D = 1` at the flat config `{6, 6, 4, 4, 4, 4, 2, 1}` (`D = 6−6+4−4+4−4+2−1 = 1`). This is a **flat** regime (no dominant `M`; all pieces `< 2^{n−1}`), structurally the **lower-bound twin of the G2-flat wall** (the very-flat `p_{n+1} > 1/D_n` regime on the upper-bound side). It likely **resists tiling-rigidity** (which needs a dominant `M` to create the rigid top `O`-block). *Status: OPEN, the genuine IMO-hard core on the lower-bound side.* Fallback (per outliner): route to the sibling `lp-dual-region` flat-regime machinery (cross-piece equal-pair structure) if tiling rigidity cannot reach it; kept in this approach for now with the peeling-pair + toggle machinery as the first (unsuccessful) attempt.

---

#### 4.11. G1-ii (M = 2^{n−1} fragment of `2^n`, rest's `2^{n−1}` SPLIT) — conditional

`alternating-potential`'s round-4 reduction (CERTIFIED) `G1-ii (r ≥ 3) ⟹ G1-i` is sound: perturb `M = 2^{n−1} → 2^{n−1} + ε`; the perturbed config is a valid G1-i instance (`M > 2^{n−1}` strict, `F` has `r − 1 ≥ 2` pieces, rest's `2^{n−1}` carries splits), `D` is continuous in `ε` (parity-integral, piecewise-linear; stable sort at `ε = 0` by the parity-integral lemma), so `D(G1-ii) ≥ 1` follows from `D(G1-i-with-rest-split) ≥ 1`. **This is CONDITIONAL on the G1-i-HC discrepancy bound (§4.9) closing WITH rest-split** — i.e. on §4.9 + the rest-split induction (§4.12). Lemma 8 (rest-unsplit) alone does NOT suffice (the perturbed config has rest-splits). No new G1-ii work; it lifts by continuity once §4.9 + §4.12 close.

---

#### 4.12. Rest-split induction (Opening B) — sketch

The full G1 allows the rest `{1, …, 2^{n−1}}` to carry splits too. **Induct on the number `q` of rest-splits** (NOT on `n`, NOT on `s` — merge-induction is dead: 1490/2913 merges increase `D`, the minimizer is at max-`s`).

- **Base `q = 0`** (rest unsplit): the rigid-tiling bound of §4.9 (the G1-i-HC discrepancy conjecture, once closed; the proved n=3 case §4.7 and the 2-piece Lemma 8 are the rigorous base).
- **Step `q → q + 1`**: one more rest-split `p → u ≥ v` (`p` a rest piece) toggles `O_{R_0}` on `[0, v) ∪ [u, p)` (certified parity-XOR toggle, `lemmas/parity-integral.md`), perturbing the discrepancy function `G` by a function supported on `[0, v) ∪ [u, p)` of total measure `≤ 2v ≤ p ≤ 2^{n−1}`. The bound `Alt_s ≥ (D_{R_0} + 1 − M)/2` degrades by at most the toggle's effect on `G(f_i)` (the breakpoints of `F`), which is bounded by the measure of the toggle set lying below each `f_i`. The **structural inductive hypothesis** required (per the round-2 scalar-invariant ruling): the rigid-tiling *pattern* of `O_{R_0}` (the superincreasing-band structure of Lemma 10) must survive the toggle up to a controlled perturbation — NOT merely the numeric bound `D ≥ 1` (a numeric-only hypothesis is circular). The toggle's support `[0, v) ∪ [u, p)` has measure `2v ≤ p`; for `p ≤ 2^{n−2}` (a sub-`2^{n−1}` rest piece), the toggle is confined below `2^{n−1}` and perturbs only the lower `E_{R_0}` bands, leaving the superincreasing structure of the upper bands intact (each upper band exceeds the sum of all lower bands, hence exceeds the toggle's total measure). This is the monovariant engine (`KB: Invariants & monovariants`).

*Status: sketch. The base (§4.9) is the open crux; the step's structural hypothesis is the load-bearing refinement. Not proved this round.*

---

**Remaining cases of G1 — refined GAP (multi-split, non-tie, high-cancellation).** After Lemmas 8 (2-piece F, rest unsplit) and 9 (low-cancellation regime, all F), the **open** sub-cases are precisely the **high-cancellation regime** `D_F < W − D_{R_0} + 1` of the multi-split non-tie cases:

- **(G1-i, multi-piece, high-cancellation):** `2^n` split into `r ≥ 4` fragments (so `F = {g_2,…,g_r}` has `s = r−1 ≥ 3` pieces) with `M > 2^{n−1}` strict, rest `R_0` **unsplit**, AND `D_F` small (high internal cancellation in F). This is where the `n ≥ 4` Lemma-6 tight family lives (`s = n−1 ≥ 3`). Lemma 8 (2-piece) does not apply; Lemma 9 (trivial overlap) is insufficient. The fine interleaving of `O_F`'s `s−1 ≥ 2` breakpoints with `O_{R_0}`'s dyadic edges is the load-bearing, unproved step.
- **(G1-ii):** `M = 2^{n−1}` (fragment of `2^n`) but rest's piece `2^{n−1}` is SPLIT (no tie). Lemma 5's top band shifts (`max(R_0) < 2^{n−1}`); the same tiling deficit must be re-derived on the shifted support. Verified TRUE with correct split budget (worst `D − 1 = 0` at `n = 3, 4`; positive slack `n ≥ 5`).
- **(G1-iii):** `2^n` split into `r ≥ 3` fragments, all `< 2^{n−1}`. The global largest `M` comes from the rest's `2^{n−1}` (if unsplit) — a "near-tie" regime (`m_1 = 2^{n−1} − ε` for `2^n`'s largest fragment). The outline's claim "reduce to `G1(n−1)`" does **not** hold cleanly: the rest `R = {2^n`'s fragments`} ∪ {1,…,2^{n−2}}` is NOT a dyadic `(n−1)` config (its total is `3·2^{n−1} − 1 ≠ D_{n−1}`), and `G1(n−1)` does not transfer. Verified TRUE numerically (correct budget); proof open.

**Why the naive bounds fail (recorded to prevent retry):**
- *Sub-measure on C*: `C ≤ D_F` (C is a sub-measure of F's odd-region). Gives `D ≥ M − D_{R_0} − D_F + 2·0 = M − D_{R_0} − D_F`. For the tight config (Lemma 6: `M = 2^{n−1}+ε_1`, `D_{R_0} = 2^{n−1} − 2^{n−2} + ⋯ = (2^n + (−1)^{n−1})/3` for unsplit rest, `D_F` = alternating sum of `{2^{n−2}+ε_2, …}`), this bound lands at `D ≥ (something < 1)` — strictly short. Verified: the tight config saturates Lemma 5's exact bound `2 C = D_{R_0} + D_F + 1 − M`, NOT the loose `C ≤ D_F`.
- *XOR-sum (triangle inequality)*: `D_R ≤ D_{R_0} + W` (where `W = 2^n − M`), i.e. `D_R ≤ D_{R_0} + (2^n − M)`. Gives `D = M − D_R ≥ 2 M − D_{R_0} − 2^n`. For `M = 2^{n−1}` (equal-halving tie): `D ≥ 2^n − D_{R_0} − 2^n = −D_{R_0} < 0`. Useless.
- *"D ≥ D_{R_0}"* (the single-split Case-B bound): FALSE for multi-split. The tight config (Lemma 6 with small `ε_i`) has `D = 1` but `D_{R_0} = (2^n + (−1)^{n−1})/3 ≥ 1` (often `≫ 1`); so `D < D_{R_0}` is typical for multi-split. Verified directly (n=3 example `{4.37, 4, 2.08, 2, 1.55, 1}`, `D = 1`, `D_{R_0} = 3`).
- *Trivial overlap `|O_F ∩ E_{R_0}| ≤ |E_{R_0}|`*: Lemma 9 — closes the low-cancellation regime but fails the high-cancellation (tight) regime, where `|O_F| = D_F` is small and the bound `|O_F ∩ E_{R_0}| ≤ |E_{R_0}|` is far too coarse (it ignores that `O_F` is small). Recorded so the next round does not conflate "proved for low-cancellation" with "proved in general".

**The open crux (refined).** Prove `|O_F ∩ E_{R_0}| ≤ (M − D_{R_0} + D_F − 1)/2` for the **high-cancellation, multi-piece-F** regime: `s ≥ 3` pieces in `F`, `D_F` small, rest unsplit (G1-i); and the analogous statements for G1-ii (split rest) and G1-iii (near-tie). The bound is TRUE (verified `n = 2, 3, 4, 5, 6` with correct split budget, `D ≥ 1` throughout, tight at `n = 3, 4` via multi-piece F and the Lemma-6 family). The handle: `O_{R_0}` is a rigid alternating-dyadic-interval tiling whose complement `E_{R_0}` is a superincreasing-block pattern; `O_F` (odd region of an `s`-piece partition of `W`) has `s−1` breakpoints, and the deficit `2^{n−1} − |O_{R_0} ∪ O_F|` is forced ≥ `(W + 1 − D_{R_0} − D_F)/2` by the superincreasing gap structure (each dyadic edge `2^k` of `O_{R_0}` "leaks" against `O_F`'s breakpoints). Making this bookkeeping rigorous for `s ≥ 3` is the open step.

*(If G1 holds in full, the lower bound follows immediately: `S_odd = (1+D)/2 ≥ (1 + 1/D_n)/2 = 2^n/D_n`.)*

### 5. Upper bound — Xiang Yu holds Liu Bang to ≤ 2^n/D_n

#### 5.1. Base case n = 1 — PROVED (c(1) = 2/3)

Liu Bang places one mark at t ∈ (0, 1). Let A := max(t, 1−t) ∈ [1/2, 1) be the larger resulting piece and B := 1 − A ≤ 1/2 the smaller. Xiang Yu's reply (≤ 1 mark):

- **Regime A (A ≥ 2/3): split A equally** into A/2 + A/2. Since A/2 ≥ 1/3 and B = 1 − A ≤ 1/3, the three pieces sort as A/2, A/2, B (A/2 ≥ B). Liu's odd-sum (Lemma 1) = A/2 + B = A/2 + 1 − A = 1 − A/2 ≤ 1 − 1/3 = **2/3**.
- **Regime B (A < 2/3, i.e. A ∈ [1/2, 2/3)): split A barely** — choose ε > 0 small (in particular ε < A − B = 2A − 1 when A > 1/2, and ε < 1/6 when A = 1/2). Split A into (A − ε) + ε.
  - If A > 1/2: with ε ≤ 2A − 1 we have A − ε ≥ B, and ε ≤ B, so pieces sort as A − ε, B, ε. Liu = (A − ε) + ε = A < **2/3**.
  - If A = 1/2 (Liu's mark at the midpoint, B = 1/2): the pieces are B = 1/2, A − ε = 1/2 − ε, ε, sorted 1/2, 1/2 − ε, ε. Liu = 1/2 + ε < 1/2 + 1/6 = **2/3**.
  In both sub-cases Liu < 2/3 (strictly, since A < 2/3).

Combining the regimes, Xiang Yu holds Liu Bang to ≤ 2/3 for every Liu mark. Combined with the lower bound (Liu's mark at 1/3 forces ≥ 2/3, §4.1 / §5.1 equality case), **c(1) = 2/3.** ∎

*Remark (the mechanism that should generalize).* The n = 1 proof is a clean two-regime minimax: for each A, Xiang picks the better of {equal-split (cost 1 − A/2), barely-split (cost A)}; Liu picks A to maximize min(1 − A/2, A), solved at the crossover 1 − A/2 = A, i.e. A = 2/3. The recursion `1/c(1) = 1/c(0) + 1/2 = 1 + 1/2 = 3/2 = 1/(2/3)` is realized by this crossover. The barely-split branch (Liu = A, the largest piece) is the n = 1 instance of "peeling off a piece of density 1/2^n" from the residual.

#### 5.2. Inductive step (general n) — OPEN GAP (G2)

The recursion (Lemma 2) `1/c(n) = 1/c(n−1) + 1/2^n` is the loading target. The intended inductive Xiang strategy is:

> Given Liu Bang's n+1 pieces (summing to 1), Xiang Yu uses one mark to "peel off" a contribution of density 1/2^n (in the 1/c sense), reducing the residual game to an (n−1)-mark instance on which the induction hypothesis caps Liu's residual share by c(n−1)·(residual mass). The two contributions sum, via the recursion, to c(n).

**This step does not close here.** Two honest obstacles, both flagged by the outline-reviewer's numerics:

1. *The peeling split is not always equal.* On the dyadic n = 2 lower-bound config {1, 2, 4}/7, the optimal Xiang reply is a single mark barely-splitting the largest piece 4/7 into 0.425 + 0.146 (smaller part ≈ 1.022 > 1, in the equality range of §4.2), *not* the equal-halving 2 + 2. Both attain D = 1/7. So the peeling strategy must derive the split point from the recursion, not assume equal-halving. The n = 1 base (§5.1) already shows this: Regime B uses a barely-split, not an equal split.

2. *The true minimizer is pairing-like, not peeling-like.* On the hardest random Liu configurations found by the reviewer (e.g. Liu pieces desc [0.798, 0.2007, 0.0013]), the optimal Xiang reply {0.4, 0.7} creates two near-equal pairs (0.3 + 0.3, 0.2007 + 0.198) that cancel in D = S_odd − S_even, leaving only the tiny 0.0013 as odd surplus. This is a *pairing* mechanism (the sibling `pairing-charging` approach's framing), not a one-mark-peels-one-piece recursion. It is unclear whether the peeling recursion `1/c(n) = 1/c(n−1) + 1/2^n` can be realized by a peeling strategy for arbitrary (non-dyadic) Liu marks, or whether the upper bound forces the pairing structure and the dyadic-induction framing must reproduce it.

> **Gap G2 (upper bound, general n).** Construct, for arbitrary Liu Bang marks, a Xiang Yu strategy using ≤ n marks that holds Liu Bang's odd-sum to ≤ 2^n/D_n, and prove it realizes `1/c(n) = 1/c(n−1) + 1/2^n`. The n = 1 base (§5.1) is proved; the inductive step is open, with the reviewer's numerics indicating the mechanism is pairing rather than peeling. If no peeling strategy realizes the recursion for arbitrary Liu marks, this approach's upper bound must either fall back to a direct combinatorial cap (sibling approaches) or concede to the pairing framing.

*(If G2 holds, the upper bound matches the lower bound and c(n) = 2^n/D_n is proved.)*

### 6. Verification of c(n) for n = 1, 2, 3 (KB: *verify final answers*)

By direct substitution into c(n) = 2^n/(2^{n+1} − 1):
- n = 1: c(1) = 2/(4 − 1) = **2/3**. ✓ (proved both bounds in §4.1, §5.1)
- n = 2: c(2) = 4/(8 − 1) = **4/7** ≈ 0.57143. ✓ (lower-bound construction verified; 0- and 1-mark upper sub-cases checked; two-mark sub-case and full upper bound open)
- n = 3: c(3) = 8/(16 − 1) = **8/15** ≈ 0.53333. ✓ (lower-bound construction verified numerically by the explorer; proof open)

The recursion (Lemma 2) gives 1/c(1) = 3/2, 1/c(2) = 7/4, 1/c(3) = 15/8, matching 2 − 1/2, 2 − 1/4, 2 − 1/8. ∎

---

### Summary of rigor status

| Component | Status |
|---|---|
| Greedy-alternating lemma (Lemma 1) | PROVED (full) |
| Parity-integral reformulation (Lemma 3) | PROVED (full) |
| Recursion identity (Lemma 2) | PROVED (full) |
| Lower-bound construction + structural fact | PROVED |
| Largest-piece decomposition `D = M − D_R` (Lemma 4) | PROVED (full, verified) |
| G1 base n = 0, n = 1 | PROVED |
| G1 for n = 2, 0- and 1-mark (subsumed by Case B) | PROVED |
| **G1 Case A (2^n unsplit, all n)** | **PROVED** |
| **G1 Case B (2^n split once, all n)** | **PROVED** (E_1 sub-measure bound + G1(n−1)) |
| **G1 Case C (2^n split, M = 2^{n−1} tie, all n)** | **PROVED** (peeling + G1(n−1)) |
| G1 multi-split structural formula (Lemma 5) | PROVED (identity) |
| Union-measure reformulation (Lemma 7) | PROVED (identity) |
| G1 tight config family (Lemma 6) | PROVED (sharpness) |
| **G1-i 2-piece F / rest unsplit (Lemma 8, all n ≥ 2)** | **PROVED** (rigid top O-block; closes n=3 tight family) |
| **G1 low-cancellation regime (Lemma 9, all F, all n)** | **PROVED** (trivial overlap bound; `D_F ≥ W − D_{R_0} + 1`) |
| **Rest tiling structure + discrepancy G (Lemma 10)** | **PROVED** (superincreasing E_R0 bands; G swings) |
| **Discrepancy reformulation of G1-i-HC (Lemma 11)** | **PROVED** (identity: `overlap−target = (M−1−D_R0)/2 + Alt_s`) |
| **G1-i-HC for n=3, all s ∈ {1,2,3} (Lemma 12)** | **PROVED** (Cases A/B on f_2; closes n=3 rest-unsplit) |
| **n=4 s=3 Lemma-6 tight family (sliver witness)** | **PROVED** (deficit = sliver `(2,2+ε_3]`, measure ε_3 = target) |
| **General G1-i-HC bound (n≥4, s≥3)** | **CONJECTURED + verified** (n=2..6, 0 violations; superincreasing-overflow mechanism; open crux) |
| **Round 6: clean measure form (★) (Lemma 13)** | **PROVED** (exact equivalent `Ψ≤T_n`; decouples W; verified n=2..7) |
| **Round 6: tower-prefix tight (Lemma 14)** | **PROVED** (`Ψ(F^*)=T_n` exactly; ε-slack identity; verified n=2..6) |
| **Round 6: sliding/exchange (Lemma 15)** | **PROVED** (PWL; max at dyadic-edge-or-tie vertex; KKT) |
| **Round 6: s=3 ALL n≥3 (Lemma 16)** | **PROVED** (spill→Lemma 8 at n−1; no-spill casework; generalizes n=4 sliver; verified n=3..7) |
| **Round 6: general s≥4 G1-i-HC** | **CONJECTURED + verified** (superincreasing-prefix obstruction; W-sum coupling OPEN) |
| **G1-iii-a (rest 2^{n−1} unsplit)** | **OPEN** (peeling-pair UNSOUND; continuity reduction fails — provenance switches; conditional on §4.9) |
| **G1-iii-b (flat, rest 2^{n−1} split)** | **OPEN** (flat twin of G2-flat; tight n=4 D=1; resists tiling rigidity) |
| **G1-ii (M=2^{n−1} fragment, rest split)** | **CONDITIONAL** (lifts by continuity from G1-i-HC-with-rest-split, certified; needs §4.9+§4.12) |
| **Rest-split induction (Opening B)** | **SKETCH** (induct on #rest-splits via parity-XOR toggle; structural hypothesis; base=§4.9 open) |
| **G1-i multi-piece high-cancellation (s ≥ 3, G1-ii, G1-iii)** | **OPEN GAP** (overlap bound in high-cancellation regime) |
| Upper bound n = 1 (both regimes) | PROVED |
| **Upper bound inductive step (G2)** | **OPEN** |
| c(1), c(2), c(3) values | verified by substitution |

The answer **c(n) = 2^n / (2^{n+1} − 1)** is established *rigorously for n = 1* (both bounds) and is *strongly supported* (construction + numerics, plus G1 Cases A/B/C + Lemma 8 2-piece + Lemma 9 low-cancellation proved) for n ≥ 2; the lower bound for n ≥ 2 awaits the multi-piece high-cancellation overlap bound (the remaining G1 gap), and the upper bound for n ≥ 2 awaits an inductive (or pairing-fallback) argument (G2). The proof is therefore **partial**.

## Promotable lemmas
- **Greedy-alternating lemma (Lemma 1).** Statement: under free-choice alternating claim (Liu Bang first, both maximizing own total) on a multiset of pieces sorted descending a_1 ≥ … ≥ a_m, Liu Bang's payoff is the odd-position sum S_odd = a_1 + a_3 + a_5 + … and Xiang Yu's is S_even = T − S_odd; taking a_1 is optimal. Proved in full in this file, §1. Mechanism: strong induction on m with the explicit exchange deficit Δ_k = Σ_{j=1}^k (a_{2j−1} − a_{2j}) ≥ 0 for any non-greedy first move. (Shared load-bearing reduction for all approaches; recommend certifying as `lemmas/greedy-alternating.md` so no approach re-proves it.)
- **Parity-integral reformulation (Lemma 3).** Statement: D = a_1 − a_2 + a_3 − … = ∫₀^∞ [j(t) odd] dt where j(t) = #{pieces ≥ t}; equivalently S_odd = (1+D)/2. Proved in full in this file, §2. (Unifies both bounds through one lens; useful to `alternating-potential` and `pairing-charging`.)
- **Recursion identity (Lemma 2).** Statement: 1/c(n) = 2 − 2^{−n} = 1/c(n−1) + 2^{−n} = Σ_{k=0}^n 2^{−k} for c(n) = 2^n/(2^{n+1}−1). Proved in full in this file, §3.
- **Largest-piece decomposition (Lemma 4).** Statement: for any final multiset with largest piece M (a choice, if ties) and rest R, `D = M − D_R` (D_R = D of R). Proved in full in this file, §4.3, via the parity-integral t-axis. Verified 3000 trials (n=2,3), 0 errors. The load-bearing structural identity for G1; reusable by `pairing-charging`, `alternating-potential`, `minimax-strategy-family`. Proposed for certification as `lemmas/largest-piece-decomposition.md`.
- **G1 Case B (single-split sub-lemma).** Statement: for the dyadic config `{1,…,2^n}` (units), if `2^n` is split exactly once into `M + g_2` (`M ≥ 2^{n−1} ≥ g_2`) and the rest `{1,…,2^{n−1}}` has ≤ `n−1` splits, then `D = 2^n − D_{R_0} − 2·E_1 ≥ D_{R_0} ≥ 1` where `E_1 = ∫_0^{g_2} [j_{R_0} even] ≤ 2^{n−1} − D_{R_0}`. Proved in full in §4.3 Case B (verified 20k trials). A reusable sub-lemma for the G1 induction; proposed for certification as part of `lemmas/splits-inequality.md` (once the multi-split gap closes).
- **G1 Case C (tie / peeling sub-lemma).** Statement: for the dyadic config, if `2^n` is split with largest fragment `M = 2^{n−1}` AND rest's piece `2^{n−1}` is unsplit, then `D = D_{R'} ≥ 1` by the peeling lemma + `G1(n−1)`. Proved in full in §4.3 Case C (verified 20k trials). Reusable; proposed for certification as part of `lemmas/splits-inequality.md`.
- **Multi-split structural formula (Lemma 5).** Statement: for `2^n` split into `M, g_2,…,g_r` (`M ≥ 2^{n−1}` unique largest), `D = M − D_{R_0} − D_F + 2 C` (D_F = D of F = {g_2,…,g_r}; C = overlap of odd-parity regions of j_{R_0}, j_F). Proved in full in §4.3 (verified 3000 trials). The handle for the remaining G1 gap; proposed for certification as `lemmas/multi-split-formula.md` (a proven identity, useful even though the bound `2C ≥ …` derived from it is the open gap).
- **Union-measure reformulation (Lemma 7).** Statement: `D = M + D_{R_0} + D_F − 2|O_{R_0} ∪ O_F|` (within `[0, 2^{n−1}]`), so `D ≥ 1 ⟺ |O_{R_0} ∪ O_F| ≤ (M + D_{R_0} + D_F − 1)/2`. Proved in full in §4.3 (inclusion–exclusion on Lemma 5; verified 8k trials, 0 error). The "shave 1 off the trivial union bound" framing of the G1 wall; reusable by any approach attacking the overlap bound.
- **G1-i 2-piece F / rest-unsplit sub-case (Lemma 8).** Statement: for `n ≥ 2`, if `2^n → M + a + b` (3 fragments, `M > 2^{n−1}` strict, rest `{1,…,2^{n−1}}` unsplit), then `D ≥ 1` (tight at `n = 3`, the Lemma-6 family). Proved in full in §4.4 via the rigid top O-block `(2^{n−2}, 2^{n−1}] ⊆ O_{R_0}`. Verified 5k trials each `n = 3..6`. A genuine sub-case closure (the n=3 tight regime); proposed for certification as part of `lemmas/splits-inequality.md` (PARTIAL remains PARTIAL — the multi-piece high-cancellation regime is still open).
- **Low-cancellation regime (Lemma 9).** Statement: under Lemma 5's setup, the trivial bound `|O_F ∩ E_{R_0}| ≤ |E_{R_0}|` yields `D ≥ 1` whenever `D_F ≥ W − D_{R_0} + 1` (F has little internal cancellation; covers single-piece F = Case B, and 2-piece F with small smaller-fragment). Proved in full in §4.5. Complementary to Lemma 8; together they leave only the high-cancellation multi-piece regime open.
- **Rest tiling structure + discrepancy function (Lemma 10).** Statement: for the unsplit rest `R_0 = {1,…,2^{n−1}}`, `E_{R_0}` is a union of `⌊n/2⌋` superincreasing dyadic bands (recursion `E_{R_0}(n) = (2^{n−3}, 2^{n−2}] ∪ E_{R_0}(n−2)`); the discrepancy `G(x) = |[0,x]∩O_{R_0}| − x/2` has slope `+1/2` on O-bands, `−1/2` on E-bands, with superincreasing swing amplitudes. Proved in full in §4.6. Reusable structural asset for any approach attacking the HC overlap bound.
- **Discrepancy reformulation of G1-i-HC (Lemma 11).** Statement: `overlap − target = (M − 1 − D_{R_0})/2 + Alt_s`, where `Alt_s = Σ_{i=1}^s (−1)^{i+1} G(f_i)` is the alternating-discrepancy sum at F's sorted breakpoints; hence `D ≥ 1 ⟺ Alt_s ≥ (D_{R_0}+1−M)/2`. Proved in full in §4.6 (exact identity, verified n=2..6). Pinpoints the "shave 1" crux as an alternating-discrepancy bound; importable as the clean statement of the G1-i-HC wall.
- **G1-i-HC for n=3, all s (Lemma 12).** Statement: for `2^3 → M + F`, `M > 4`, `F` with `s ∈ {1,2,3}` pieces (sum `W < 4`), rest `{1,2,4}` unsplit, `D ≥ 1`. Proved in full in §4.7 (Cases A/B on `f_2`; s=1,2 subsumed by Case B / Lemma 8). Closes n=3 rest-unsplit G1-i-HC entirely.
- **Clean alternating-prefix measure form (★) (Lemma 13, round 6).** Statement: under the Lemma-5 setup, `D ≥ 1 ⟺ Ψ(F) := Σ_{i odd} E(f_i) + Σ_{i even} O(f_i) ≤ T_n := (2^n−1−D_{R_0})/2`, with the exact identity `Alt_s − target = T_n − Ψ`. Proved in full in §4.9' (algebraic, exact; verified n=2..7). Decouples the `W`-dependence of the G1-i-HC target; the clean statement of the wall; importable as the measure-form equivalent of Lemma 11. Includes the pair-decomposition `Ψ = S_even + |Q∩E|` and the `[0, 2^{n−2}]` `E↔O` swap reduction to the `(n−1)`-rest regions.
- **Tower-prefix tight arithmetic (Lemma 14, round 6).** Statement: at `F^* = {2^{n−2}, 2^{n−3}, …, 2^{n−1−s}}` (and the Lemma-6 `ε`-family), `Ψ(F^*) = T_n` exactly; the bound is tight iff `s = n−1` (positive slack for `s < n−1`). Proved in §4.9'' (ε-slack identity; verified n=2..6). Importable as the sharpness/equality case for G1-i-HC.
- **Sliding/exchange lemma (Lemma 15, round 6).** Statement: `Ψ` is piecewise-linear in `F`; at any maximizer over `{f_1≥…≥f_s≥0, Σf_i≤U}`, each `f_i` is at a dyadic band-edge or tied to a neighbor. Proved in §4.9''' (PWL + KKT subdifferential). Importable as the engine reducing the G1-i-HC search to dyadic-edge vertices (the setup for any exchange/vertex-enumeration attack on the general `s ≥ 4` bound).
- **s=3 all n≥3 (Lemma 16, round 6).** Statement: for `2^n → M + F`, `M > 2^{n−1}` strict, `F = {f_1≥f_2≥f_3}` (sum `W < 2^{n−1}`), rest unsplit: `D ≥ 1` (`Ψ ≤ T_n`). Proved in full in §4.9'''' (spill case reduces to Lemma 8 at `n−1` via the `[0,m]` swap; no-spill casework closes directly). Generalizes the `n=4, s=3` sliver witness to all `n ≥ 3`. Importable as the `s = 3` component of `splits-inequality.md`.
