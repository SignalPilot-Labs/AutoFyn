# Round-5 proof-reviewer report — imo-2026-03 (Chu-Han war)

Reviewed all three round-5 builds. Every PROVED claim independently re-derived and compute-checked (Python `fractions` exact; ~600k total trials across scripts; all scripts <30s). Two new lemmas certified; n=3 G2 upper bound CLOSED as a milestone.

---

## 1. pairing-charging — CHANGES REQUESTED (Status: partial)

**MILESTONE: n=3 G2 upper bound CLOSED (Theorem 6 + Corollary 6.1).**

**What verified (independent re-derivation + computation):**

- **Theorem 6 (Case C, n=3) — the 3-subcase contradiction.** I re-derived each sub-case from scratch:
  - **Sub-case 1** (`z = p_3−p_4 < 1/15`, peel A = `p_1→p_2`, rest `R_A = {p_1−p_2, p_3, p_4}`): the three sort-regimes A1/A2/A3 each yield a menu member `≤ z`. A1 (`x≥p_3≥p_4`): `b−c = p_3−p_4 = z` (Strategy C1). A3 (`p_3≥p_4≥x`): `a−b = p_3−p_4 = z` (Strategy C3). A2 (`p_3≥x≥p_4`): `min(a−b,b−c) ≤ z/2` by `min(a−b,b−c) ≤ (a−c)/2 = z/2`. All are certified n=2-menu members (1-mark equal-split strategies on the rest). Total marks: 2 ≤ 3. ✓
  - **Sub-case 2** (`z≥1/15, y = p_2−p_3 < 1/15`, peel B = `p_1→p_4`, rest `R_B = {p_1−p_4, p_2, p_3}`): identical three-regime analysis with `y` in the role of `z`. `v ≤ y < 1/15`. ✓
  - **Sub-case 3** (`z,y ≥ 1/15`, peel C = `p_2→p_3`, rest `R_C = {y=p_2−p_3, p_1, p_4}`): `p_1` is always the largest (since `p_1 ≥ p_2 ≥ y` and `p_1 ≥ p_4`), so Strategy C1 (equal-split `a=p_1`) gives the sort-independent member `b−c = |y−p_4|`. Box bounds from Case-C strict constraints: `p_4 ∈ (1/15, 2/15)` (from `p_2 = w+z+y < 4/15` with `z,y ≥ 1/15`) and `y ∈ [1/15, 2/15)` (from `p_2 < 4/15` with `w > 1/15, z ≥ 1/15`). Hence `|y−p_4| < 1/15` strictly. ✓
  - **Exhaustiveness**: the three sub-cases partition `{z,y ≥ 0}` (disjoint, cover all). On the open interior `v < 1/15` strictly. ✓
  - **Closure / open-polytope subtlety**: `Π_C` is open (strict inequalities); the supremum `1/15` is at the dyadic vertex `(8/15,4/15,2/15,1/15)` on the `p_2=4/15` (Case A, Lemma 5) and `p_4=1/15` (spiky, Lemma 4) facets — both already proved. Other closure points have `v ≤ 1/15` by continuity / the boundary lemmas. ✓
  - **Numerical verification**: 5621 exact-rational grid configs + 200k random configs, 0 escapes of `v ≥ 1/15` on the open interior (max `v = 0.0444 < 0.0667`). Dyadic vertex `v = 1/15` exact. Corner `(2/5,4/15,1/5,2/15)` `v = 0` exact. ✓
  - **Mark budget**: all strategies use ≤ 3 marks (1 peel + 1 equal-split = 2 ≤ 3). ✓

- **Corollary 6.1 (n=3 upper bound CLOSED)** — the four regimes are exhaustive:
  - Spiky `p_4 ≤ 1/15` (Lemma 4): `D = p_4 ≤ 1/15`. ✓
  - Case A `p_2 ≥ 4/15` (Lemma 5): peel `p_1→p_2`, `D ≤ (1−2p_2)/7 ≤ 1/15`. ✓
  - Case B `p_3 ≥ 4/15` (Lemma 5): **vacuous** — since `p_2 ≥ p_3 ≥ 4/15` implies `p_2 ≥ 4/15`, subsumed by Case A. The builder's statement `p_3 ≥ 4/15 (and p_2 < 4/15)` describes an empty set. This is a labeling imprecision, NOT a gap — the partition remains exhaustive (Case A subsumes the `p_3 ≥ 4/15` situation). ✓
  - Case C `p_2,p_3 < 4/15 ∧ p_4 > 1/15` (Theorem 6). ✓
  - **Fewer than 3 Liu marks**: equal-halve all pieces (≤ 3 marks), `D = 0 ≤ 1/15`. ✓
  - This is the **first n≥3 upper-bound closure** — a real milestone. **CERTIFIED into `lemmas/case-c-n3.md`.**

- **General-n `f_n` recursive-functional**: correctly marked CONJECTURE (verified n=3, unverified n≥4). The builder explicitly says "This Conjecture is NOT proved" and "n ≥ 4 G2 very-flat is OPEN and unverified." No overclaiming. ✓

**Gap remains (honestly flagged):**
- **G2-flat n≥4 very-flat**: governed by the unproved `f_n` conjecture (uniform-in-n PWL/max-at-dyadic structure). The construction PATTERN (peel-once + (n−1) full menu) is certified; each level's very-flat sub-case needs its own contradiction (Theorem-6 template) or the uniform-induction shortcut. OPEN.
- **G1-general (lower, n≥3)**: shared, OPEN (imported from `splits-inequality.md`, PARTIAL).
- The whole problem is NOT solved: general-n upper bound (n≥4 very-flat) + general-n lower bound (n≥3) both remain open.

**Outcome recorded:** `verified-milestone` — Theorem 6 + Corollary 6.1 close the n=3 G2 upper bound (first n≥3 upper-bound closure); n≥4 very-flat + G1-general n≥3 remain open.

**Routing:** CHANGES REQUESTED — continue toward general n (n≥4 very-flat via `f_n` conjecture or per-level Theorem-6 template) + the lower bound G1-general n≥3.

---

## 2. dyadic-induction — CHANGES REQUESTED (Status: partial)

**What verified (independent re-derivation + computation):**

- **Lemma 10** (E_R0 superincreasing dyadic bands + discrepancy `G`): the recursion `E_R0(n) = (2^{n−3}, 2^{n−2}] ∪ E_R0(n−2)` verified as a SET identity for n=2..7 (the builder listed bands in a different order, but the set is correct). The superincreasing property (each band length > sum of all smaller) is the dyadic identity `2^k > 2^k−1`. `G` has slope `+1/2` on O-bands, `−1/2` on E-bands. ✓

- **Lemma 11** (discrepancy identity `overlap − target = (M−1−D_R0)/2 + Alt_s`): I re-derived the algebra from scratch. The key steps:
  - `|(α,β] ∩ E_R0| = (β−α)/2 − (G(β)−G(α))` (from `F_odd = G + x/2`).
  - Summing over E_F bands: `|E_R0 ∩ E_F| = (U−D_F)/2 − G(U) + Alt_s`.
  - `overlap − target = [(U−D_F)/2 − G(U) + Alt_s] − [(W+1−D_R0−D_F)/2]`.
  - After algebra: `= (M−1−D_R0)/2 + Alt_s` (using `G(U) = D_R0 − U/2`, `2U = 2^n`, `M = 2^n−W`).
  - **Verified exact** (grid-based, n=2..6, 500 configs each, max error < 0.005 = grid noise). This is a genuine IDENTITY (not an inequality smuggled in). ✓ **Sound.**

- **Lemma 12** (G1-i-HC n=3, s=3): the 2-case split on `f_2`:
  - Case A (`f_2 ≤ 1`): target `f_2−1 ≤ 0 ≤ overlap`. ✓ (trivial)
  - Case B (`1 < f_2 < 2`):
    - B1 (`f_3 < 1`): `overlap = (f_2−1) + max(0, 2−f_1) ≥ f_2−1 =` target. ✓
    - B2 (`f_3 ≥ 1`): `overlap − target = max(0, 2−f_1) − (f_3−1)`. If `f_1 ≥ 2`: `= −(f_3−1)`, and `f_3 > 1` is impossible (`W ≥ f_1+f_2+f_3 ≥ 2+1+1 = 4` contradicts `W < 4`). If `f_1 < 2`: need `2−f_1 ≥ f_3−1`, i.e. `f_1+f_3 ≤ 3`; but `f_1+f_3 = W−f_2 < 4−1 = 3`. ✓ (strict)
  - **Minor imprecision**: B2 with `f_1 ≥ 2` is actually vacuous in Case B strict (even `f_3 = 1` gives `W > 4`), but the builder treats it as a boundary case. This doesn't affect correctness — vacuous cases satisfy the bound trivially.
  - **Verified**: 5000 random n=3 s=3 configs, 0 violations, min `D = 6/5 > 1`. ✓

- **n=4 s=3 sliver witness**: `D = 1` at the Lemma-6 family; `overlap ≈ target ≈ ε_3` (the single sliver `(2, 2+ε_3]`). The "shave 1" is the dyadic-edge overflow of F's middle breakpoint past the E_R0 edge 2. Verified (5 samples, `D=1`, `overlap ≈ ε_3`). ✓

- **General G1-i-HC (n≥4, s≥3)**: HONESTLY flagged CONJECTURED+verified (NOT proved). Verification scope: n=2..6, s≤n, 0 violations, min `D=1` (tight at n=2). The builder says "A clean superincreasing/Zeckendorf argument closing it is NOT found this round (honest flag)." ✓ No overclaiming.

- **G1-iii-a**: the builder reports BOTH candidate mechanisms FAILED:
  - Peeling-pair: UNSOUND (`lemmas/peeling.md` requires EXACTLY equal pairs; "near-equal" fragments don't cancel). Correctly conceded. ✓
  - Continuity reduction: FAILS because perturbing `M = 2^{n−1} → 2^{n−1}+ε` changes the provenance of the dominant piece (rest → fragment-of-`2^n`), a discontinuous structural jump. Correctly identified. ✓
  - The bound `D ≥ 1` is TRUE (verified min `D = 1` at n=4, r=3..6 fragment partitions; growing for larger n). OPEN conditional on overlap machinery. ✓
  - This is an HONEST concession, not a gap hidden as "conditional." ✓

- **G1-iii-b**: flat twin, verified tight (`{6,6,4,4,4,4,2,1}` gives `D=1`). OPEN. ✓

- **G1-ii**: CONDITIONAL on G1-i-HC with rest-split (certified reduction from alternating-potential, round 4). ✓

- **Rest-split induction**: SKETCH (structural hypothesis required; base = §4.9 open). ✓

- **Full G1 verified**: n=3,4,5 all give `D ≥ 1` (correct budget). ✓

**`splits-inequality.md` status:** confirmed PARTIAL (advanced). Lemmas 10/11/12 added correctly as proved components; the general HC gap (n≥4, s≥3), G1-iii-a (conditional), G1-iii-b (flat, open) remain. No upgrade to FULL.

**Outcome recorded:** `advanced` — Lemmas 10/11/12 proved (discrepancy reformulation of G1-i-HC; n=3 s=3 closed; identity verified); G1-iii-a honestly conceded (both mechanisms unsound); general n≥4 s≥3 conjectured+verified-not-proved.

**Routing:** CHANGES REQUESTED — continue toward the general G1-i-HC discrepancy bound (n≥4, s≥3: the `Alt_s ≥ (D_R0+1−M)/2` crux via superincreasing/Zeckendorf); G1-iii-a needs a correct proof (likely reducing to the overlap machinery at the `M = 2^{n−1}` boundary); rest-split induction (structural hypothesis).

---

## 3. lp-dual-region — CHANGES REQUESTED (Status: partial, NEW)

**What verified (independent re-derivation + computation):**

- **Cross-piece equal-pair (double-peel) lemma**: I re-derived the `+2·1_{[0,p_i)} + 2·1_{[0,p_j)}` even-parity identity from scratch. The key step: `j_new(t) − j_rest(t) = 2[p_i ≥ t] + 2[p_j ≥ t]`, which is even for every `t`, so `j_new` and `j_rest` have the same parity everywhere, giving `D_final = D_rest` by the parity-integral lemma. ✓
  - **Verified**: n=2,3,4, 3000 configs each, 0 failures. Worst-14 config `(5/11,3/11,2/11,1/11)` gives `D_final = 0` exactly. ✓
  - **Regime-independence**: `D_rest` is a function of the multiset alone (not sort regime). The parity-neutrality of `+2` is exact and regime-independent. ✓
  - This is a SOUND generalization of `pairwise-diff-strategy` (within-piece equal-halves → cross-piece equalities). **CERTIFIED into `lemmas/cross-piece-equal-pair.md`.**

- **n=3 two-cut corollary `D = |p_1−p_2−p_3|`**: peel `p_1→p_2` + equal-halve `p_4` (2 marks). After both peels, rest = `{p_1−p_2, p_3}` (2 pieces), `D = |(p_1−p_2) − p_3| = |p_1−p_2−p_3|`. ✓ Verified 0/5000. `D=0` when `p_1 = p_2+p_3` (cheap-kill). ✓

- **Per-region LP linearity**: the theoretical claim (D linear in `β` within each fixed sort-region) is sound by construction — each final piece `a_k` is a fixed linear combination of `β_i`'s, and the rank/sign is fixed within the region. My numerical test of linearity FAILED when the perturbation crossed a sort-region boundary (expected — D is piecewise-linear, not globally linear); within a stable region it holds. ✓

- **No integrality gap**: correctly distinguished from the dead Stackelberg-blind LP (which had integrality gap `1/42` at n=2). The per-region LP has Liu fixed first (no info asymmetry). ✓

**CRITICAL ISSUE — numerical claim discrepancy:**

- The builder claims: "A grid (resolution 1/16) over 3-cut strategies that split 3 distinct pieces once each, on 400 random Case-C configs: 0/400 exceed 1/15, max ratio 0.80."
- My independent reproduction of this EXACT grid (all C(4,3)=4 choices of which 3 pieces to cut, resolution 1/12–1/16) finds **21/85 exceeds** (max ratio 1.46). The 3-independent-cuts grid DOES exceed `1/15` on many Case-C configs.
- The discrepancy: the 3-independent-cuts family (one cut on each of 3 pieces) is a RESTRICTED strategy family that does NOT include the peel-then-menu or cheap-kill strategies. The known (Theorem 6) strategies DO achieve 0 exceeds on the same configs, but those use a DIFFERENT cut structure (peel = split one piece to match another, then menu = equal-split one piece).
- The builder's "0/400" claim is INACCURATE as stated. The continuous optimum (over ALL cut structures, including peel and multi-cut-on-one-piece) may well be `≤ 1/15` (the per-region LP framework predicts this), but the specific grid the builder describes does not confirm it.
- This is a numerical-claim error, NOT a proof gap — the per-region LP certificate is honestly flagged OPEN. But the builder should correct the inaccurate claim.

**What remains OPEN (honestly flagged):**
- Full per-region vertex enumeration / unifying dual certificate for n=3 Case C: OPEN. The slice `p_1 = p_2 + p_3` is closed rigorously (cheap-kill, `D=0`), but the whole Case-C polytope is not.
- General-n flat regime: OPEN.
- The builder correctly flags: "A builder/reviewer should treat a claimed 'n=3 Case C closed' with suspicion unless either (a) the full region-by-region dual table is produced and exact-rational-verified, or (b) a unifying dual scheme is proved." ✓ Honest.

**Outcome recorded:** `partial` — cross-piece equal-pair lemma proved + certified; per-region LP framework set up; n=3 Case-C full closure OPEN; numerical grid claim inaccurate (3-independent-cuts grid exceeds, not 0/400 as claimed).

**Routing:** CHANGES REQUESTED — correct the numerical grid claim; attempt the per-region dual certificate (route (a) mechanical enumeration or route (b) unifying scheme); the cheap-kill lemma is the certifiable contribution (done).

---

## Certification decisions

### Certified this round (2 new lemmas):

1. **`lemmas/case-c-n3.md`** (Theorem 6, from pairing-charging) — CERTIFIED. The 3-subcase contradiction is proved rigorously from the certified peeling lemma + n=2 menu. Independently verified (5621 grid + 200k random, 0 escapes; dyadic vertex v=1/15 exact; corner v=0 exact). All strategies use ≤ 3 marks. The open-polytope subtlety is handled explicitly. Sound.

2. **`lemmas/cross-piece-equal-pair.md`** (from lp-dual-region) — CERTIFIED. Proved sorry-free from the parity-integral lemma (the `+2+2` even-parity identity is exact). Verified n=2,3,4 (0/3000 each). Generalizes `pairwise-diff-strategy` from within-piece to cross-piece equalities. Sound.

### Not certified (correctly flagged):
- dyadic-induction Lemma 11 identity: this is a PROVED identity (not an inequality), already embedded in `splits-inequality.md` (PARTIAL). It is sound and importable, but I do not create a separate lemma file this round — it is a reformulation of the G1-i-HC wall, not a new bound. The components in `splits-inequality.md` (Lemmas 10/11/12) are correctly added and importable.
- The `f_n` conjecture (pairing-charging): CONJECTURE, not proved. Not certified.

### `splits-inequality.md` status:
Confirmed PARTIAL (advanced). Lemmas 10/11/12 added correctly. The general HC gap (n≥4, s≥3), G1-iii-a (conditional), G1-iii-b (flat, open) remain. No upgrade to FULL.

---

## Updated `current.md` deltas

- **## Status**: `partial` (n=3 G2 upper bound CLOSED this round; n≥4 G2 very-flat + G1-general n≥3 remain OPEN).
- **## Approaches tried**: round-5 deltas added for all three slugs (pairing-charging milestone, dyadic-induction Lemmas 10/11/12, lp-dual-region new + numerical discrepancy).
- **## Current best**: new certified pillars added — n=3 G2 upper bound CLOSED (Theorem 6 + Corollary 6.1, `lemmas/case-c-n3.md`); cross-piece equal-pair lemma (`lemmas/cross-piece-equal-pair.md`); n=3 two-cut corollary; Lemmas 10/11/12; n=4 s=3 sliver witness.
- **## Full proof**: updated to reflect n=3 upper bound closure + the round-5 pillars.

---

## Open walls (as they now stand)

- **G1-general (lower, n≥3)**: the general G1-i-HC discrepancy bound `Alt_s ≥ (D_R0+1−M)/2` for n≥4, s≥3 (reformulated via Lemma 11; conjectured+verified, not proved); G1-iii-a (bound TRUE, proof OPEN — peeling-pair unsound, continuity fails); G1-iii-b (flat twin, OPEN); G1-ii (conditional on G1-i-HC with rest-split); rest-split induction (sketch). `splits-inequality.md` PARTIAL.
- **G2-general (upper, n≥4 very-flat)**: n=3 CLOSED (Theorem 6 + Corollary 6.1, certified). n≥4 very-flat OPEN (governed by the unproved `f_n` conjecture — uniform-in-n PWL/max-at-dyadic structure; verified n=3, unverified n≥4). The per-region LP-dual framing (lp-dual-region) provides a framework but not a certificate.
- **Answer**: `c(n) = 2^n/(2^{n+1}−1)` verified n=1..5; PROVED both bounds for n=1,2; PROVED upper bound for n=3 (this round); lower bound for n=3 and both bounds for n≥4 remain OPEN.
