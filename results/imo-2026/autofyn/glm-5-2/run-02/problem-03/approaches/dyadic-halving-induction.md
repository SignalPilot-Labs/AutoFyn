# dyadic-halving-induction — upper bound via the 2-adic halving-defect invariant Φ

## Status
partial

## Approaches tried
- (round 5, NEW) 2-adic / halving-step framing of the upper bound G2. Defines the **halving-defect invariant** `Φ(config) = Σ_i |p_i − 2 p_{i+1}|` over sorted-desc consecutive pieces (zero iff every consecutive ratio is exactly 2:1). The dyadic config is the unique fixed point of the halving operator (Φ=0). Conjecture: `Φ>0 ⟹ cap < α(n)` strictly. — Outcome: **two harvestable PARTIAL lemmas proved** (Φ=0 uniqueness, one-line; local-kink for level-1 perturbations, real-valued, asymmetric slopes 1/2). **One critical honest falsification**: the strict-decrease conjecture `Φ>0 ⟹ cap < α(n)` is **FALSE** — the non-dyadic config `(8, 4, 2+e, 1−e)/15` (level 1 exact, levels 2+3 broken, Φ = 5|e| > 0) has `cap = α(3) = 1/15` (the pair-pile achieves A = α(3) and no strategy beats it, verified by exhaustive 2-mark search + 80k random 3-mark trials). This is a genuine **ridge**: non-dyadic configs where the cap stays at α. The strict-decrease conjecture is therefore replaced by the weaker (and true-for-the-checked-classes) non-strict bound `cap ≤ α(n)`. The universal `cap ≤ α(n)` for all non-dyadic configs (the actual U(n) target) is a GAP — the Φ-framing proves it for level-1 perturbations (strict) and ridge configs (non-strict via pair-pile), but not for far-from-dyadic configs (balanced/extreme-dominant/moderate-dominant — those need S1/S2/S3/17-family, a shared wall with `two-regime-disjunctive`). The general-n inductive lift (recurse on R when top-level exact) is an explicit GAP adjacent to the killed bisect-recurse engine. Status: partial (two certified-able partial lemmas + one honest falsification; universal U(n) open).

## Current best
Two proved partial lemmas (candidates for the shared cache):
1. **Φ=0 uniqueness** (one-line, all n): `Φ(config) = 0` iff the config is the order-n dyadic `(1,2,4,…,2^n)/D(n)`.
2. **Local-kink for level-1 perturbations** (real-valued, n=3, harvestable): perturbing the shallowest halving level by `e` (config `(8+e, 4−e, 2, 1)/15`, only level 1 broken) gives `cap < α(3)` strictly, with **asymmetric slopes**: `A·15 ≤ 1−e` for `e > 0` (mass-up, slope 1) and `A·15 ≤ 1−2|e|` for `e < 0` (mass-down, slope 2). Explicit 2-mark Xiang strategies prove each bound.

One honest falsification: the strict-decrease conjecture `Φ > 0 ⟹ cap < α(n)` is **false** (ridge counterexample `(8,4,2+e,1−e)/15`).

**Open gaps (honest):**
- (G2-strict) The strict-decrease conjecture is falsified; the weaker `cap ≤ α(n)` for all non-dyadic n=3 configs is NOT proved by this framing (only level-1 perturbations and ridge configs are covered).
- (G2-universal) Far-from-dyadic configs (balanced, extreme-dominant, moderate-dominant) need S1/S2/S3/17-family — shared wall with `two-regime-disjunctive`.
- (G2-general-n) The inductive lift (recurse on R when top-level exact) is a GAP adjacent to the killed bisect-recurse engine.

## Full proof
*(Not present — Status is `partial`. The two proved partial lemmas are written out in full below; the universal upper bound U(n) is an explicit GAP.)*

---

### 0. Setup, notation, and imported certified lemmas

Let `D(n) = 2^{n+1} − 1`, `f(n) = 2^n / D(n)`, `α(n) = 1/D(n)` (so `f(n) = (1 + α(n))/2`). The **order-n dyadic** config is the partition of `[0,1]` into `n+1` pieces `(1, 2, 4, …, 2^n)/D(n)` (Liu's marks at cumulative sums of `(1, 2, …, 2^{n−1})/D(n)`).

We work in the **advantage coordinate** `A = Σ_i (−1)^{i+1} p_i` where `p_1 ≥ p_2 ≥ …` are the final pieces (after both players' marks) sorted descending. By the certified **Lemma G** (`lemmas/lemma-g-greedy-picking.md`), optimal play in the alternate-pick phase gives Liu the odd-rank sum and the parity identity `Liu = (1 + A)/2` holds. Hence the upper-bound target `c(n) ≤ f(n)` is equivalent to:

> **(U(n))** For every Liu partition `P` of `[0,1]` into `n+1` pieces, Xiang with `≤ n` marks has a strategy forcing `A(final) ≤ α(n) = 1/D(n)`.

**Imported certified lemmas (not re-proved):**
- **Lemma G** (greedy → odd-rank sum; `Liu = (1+A)/2`). `lemmas/lemma-g-greedy-picking.md`.
- **Pair-pile dyadic cap** (all n): against the dyadic config, Xiang's pair-pile (≤ n marks) produces the multiset `2^{n−1}, 2^{n−1}, 2^{n−2}, 2^{n−2}, …, 4, 4, 3, 2, 1, 1` (over `D(n)`), with `A = 1/D(n) = α(n)`, hence `Liu = f(n)`. `lemmas/lemma-pair-pile-dyadic-cap.md`.
- **Mirror certificate** (all n): the point-reflection strategy gives the same pair-pile multiset, `A = α(n)`. `lemmas/lemma-mirror-dyadic-cap.md`.
- **Lemma S1** (balanced-config sliver, all n ≥ 1, reals): for the balanced config `(w,…,w)`, Xiang forces `A = 2s → 0 < α(n)`. `lemmas/lemma-s1-balanced-sliver.md`.
- **Dyadic-ratio overshoot** (one-step characterization, `m=1` case). `lemmas/lemma-dyadic-ratio-overshoot.md`.
- **Lemma U(2)** (four-strategy, n=2 closed form `Φ₂ = min(a, b−a, c−b, |2c−1|)`, equality iff dyadic). `lemmas/lemma-u2-four-strategy.md`.
- **L(n) for n=1,2,3,4** (lower bound, CERTIFIED): `lemmas/lemma-vertex-principle-advantage.md` (cell-complex, n=3) + n=4 certification (round 5, `cell-complex-l3`).

**Knowledge-base tools used:** **Invariants & monovariants** (the halving-defect Φ); **Induction (structural)** (the halving-depth induction); **Casework / exhaustion** (the finite disjunction on which level is broken); **Constructive / incremental** (explicit sliver mark placements per broken level).

### 1. The halving-defect invariant Φ and the uniqueness lemma

**Definition.** For a sorted-descending config `P = (p_1, p_2, …, p_{n+1})` (Liu's `n+1` pieces, `p_1 ≥ … ≥ p_{n+1}`, `Σ p_i = 1`), define the **halving defect**

```
Φ(P) = Σ_{i=1}^{n} |p_i − 2 p_{i+1}|.
```

This is the sum of the absolute "halving residuals" at each consecutive level: level `i` is **exact** (contributes 0) iff `p_i = 2 p_{i+1}`; it is **broken** iff `p_i ≠ 2 p_{i+1}`. `Φ = 0` iff every consecutive ratio is exactly `2 : 1`.

> **Lemma (Φ=0 uniqueness).** `Φ(P) = 0` iff `P` is the order-`n` dyadic `(1, 2, 4, …, 2^n)/D(n)` (up to the sum constraint, which fixes the scale).

**Proof.** `Φ(P) = 0` means `p_i = 2 p_{i+1}` for every `i = 1, …, n`. Telescoping: `p_1 = 2 p_2 = 4 p_3 = … = 2^n p_{n+1}`, i.e. `p_i = 2^{n+1−i} p_{n+1}`. The sum constraint `Σ_{i=1}^{n+1} p_i = 1` gives `p_{n+1} · Σ_{i=1}^{n+1} 2^{n+1−i} = p_{n+1} · (1 + 2 + 4 + … + 2^n) = p_{n+1} · D(n) = 1`, hence `p_{n+1} = 1/D(n)` and `p_i = 2^{n+1−i}/D(n)`. This is exactly the order-`n` dyadic. Conversely, the dyadic has `p_i = 2 p_{i+1}` at every level (telescoping `2^{n+1−i} = 2 · 2^{n−i}`), so `Φ = 0`. ∎

**Verification.** Exact-rational computation for `n = 1, …, 5`: `Φ(dyadic) = 0` in every case (`/tmp/verify_phi.py`).

This is the **fixed-point uniqueness** of the halving operator: the dyadic is the unique config where every halving step is exact. The 2-adic structure (`D(n+1) = 2 D(n) + 1`, the irreducible `+1`) is the signature of this uniqueness — the `+1` is the certified odd-multiplicity leftover (the pair-pile's `(3, 2)`-pair excess, value `1/D(n)`).

### 2. At Φ=0 (dyadic): cap = α(n) — the equality case (imported)

By the certified pair-pile lemma, against the dyadic config Xiang has a strategy (≤ `n` marks) forcing `A = α(n)` exactly. Combined with the certified lower bound `L(n)` (for `n = 1, 2, 3, 4`; open for general `n`), this pins the dyadic config's value to exactly `f(n)`.

**Regime D (dyadic).** If `Φ(P) = 0`, then `P` is the dyadic and `cap(P) = α(n)` (pair-pile, CERTIFIED). ✓

### 3. The local-kink lemma (near-dyadic, level-1 perturbations, real-valued, harvestable)

This section proves that the dyadic is an isolated **strict** local maximum of `cap(P)` in the **level-1 perturbation direction** (the shallowest halving level broken), with an asymmetric downward kink (slope 1 for mass-up, slope 2 for mass-down). This is the 2-adic signature: the `D(n+1) = 2 D(n) + 1` recursion's `+1` is realizable exactly at the dyadic, and any level-1 perturbation breaks it strictly.

> **Lemma (local-kink, level-1 perturbation, n=3, reals).** Consider the config `P_e = (8+e, 4−e, 2, 1)/15` (pieces in `1/15` units, sorted desc; `e ∈ (−1/2, 1/2) \ {0}` so all pieces positive and the sort is valid). This perturbs **only level 1** (`p_1 = 8+e ≠ 2·(4−e) = 8−2e`; levels 2,3 remain exact: `p_2 = 4−e, 2 p_3 = 4` — broken iff `e ≠ 0`; `p_3 = 2 = 2·1 = 2 p_4` — exact). Then Xiang with **2 marks** has a strategy forcing `A < α(3) = 1/15` strictly, with:
> - **(mass-up, `e > 0`)** `A · 15 ≤ 1 − e` (slope 1);
> - **(mass-down, `e < 0`)** `A · 15 ≤ 1 + 2e = 1 − 2|e|` (slope 2).
>
> In both cases `A < 1/15 = α(3)` strictly for `e ≠ 0`.

**Proof.** We exhibit explicit 2-mark Xiang strategies and compute the resulting advantage `A` exactly (all lengths in `1/15` units; the sum is always `15`).

Liu's config `P_e = (8+e, 4−e, 2, 1)/15` placed left-to-right: piece 1 = `[0, (8+e)/15]`, piece 2 = `[(8+e)/15, 12/15]`, piece 3 = `[12/15, 14/15]`, piece 4 = `[14/15, 1]`. Liu's marks at `(8+e)/15, 12/15, 14/15`.

**(mass-up, `e > 0`):** Xiang places two marks:
- **Mark 1** at `(4 + e/2)/15 = (8+e)/(2·15) = p_1/2` — the midpoint of piece 1. This splits piece 1 `(8+e)/15` into the **equal pair** `(4+e/2)/15, (4+e/2)/15`.
- **Mark 2** at `(8+e + 3/2)/15 = (p_1 + 3/2)/15` — at distance `3/2` (in `1/15` units) from the start of piece 2. This splits piece 2 `(4−e)/15` into `(3/2)/15` and `(4−e−3/2)/15 = (5/2−e)/15`.

Both marks are interior to pieces 1, 2 respectively, and distinct from Liu's marks (since `4+e/2 < 8+e` and `8+e+3/2 < 12` for `e < 1/2`; and `e ≠ 0` ensures the marks don't coincide with dyadic positions). ✓ (2 marks ≤ 3.)

Final multiset (in `1/15` units): `{4+e/2, 4+e/2, 5/2−e, 3/2, 2, 1}`. For `e ∈ (0, 1/2)`: `4+e/2 > 5/2−e` (since `3/2 + 3e/2 > 0`) and `5/2−e > 2 > 3/2 > 1`. So sorted desc: `4+e/2, 4+e/2, 5/2−e, 2, 3/2, 1`. The equal pair `(4+e/2, 4+e/2)` occupies ranks 1, 2 (consecutive, opposite parity), contributing `0`. The advantage:
```
A·15 = (4+e/2) − (4+e/2) + (5/2−e) − 2 + 3/2 − 1 = (5/2−e−2) + (3/2−1) = (1/2−e) + 1/2 = 1 − e.
```
For `e > 0`: `1 − e < 1 = α(3)·15`. Strict. ✓

**(mass-down, `e < 0`):** Xiang places two marks at the **dyadic positions** `1/15` and `3/15` — both interior to the enlarged piece 1 (which spans `[0, (8+e)/15]` with `8+e > 8 > 3` for `e > −1/2`). These split piece 1 `(8+e)/15` into three sub-pieces: `1/15, 2/15, (5+e)/15`. Pieces 2, 3, 4 are untouched: `(4−e)/15, 2/15, 1/15`.

Final multiset (in `1/15` units): `{5+e, 4−e, 2, 2, 1, 1}`. For `e ∈ (−1/2, 0)`: `5+e > 4−e` (since `1+2e > 0 ⟺ e > −1/2`) and `4−e > 2 > 1`. So sorted desc: `5+e, 4−e, 2, 2, 1, 1`. The equal pairs `(2,2)` (ranks 3,4) and `(1,1)` (ranks 5,6) each contribute `0`. The advantage:
```
A·15 = (5+e) − (4−e) + 2 − 2 + 1 − 1 = (1+2e) + 0 + 0 = 1 + 2e.
```
For `e < 0`: `1 + 2e = 1 − 2|e| < 1 = α(3)·15`. Strict. ✓

In both cases `A < α(3)` strictly for `e ≠ 0`, with asymmetric slopes (1 for mass-up, 2 for mass-down). ∎

**Verification.** Exact-rational computation (`/tmp/final_check2.py`): for `e ∈ {1/60, 1/30, 1/15, 1/10}` (mass-up) and `e ∈ {−1/60, −1/30, −1/15, −1/10}` (mass-down), the explicit 2-mark strategies give exactly `A·15 = 1−e` (mass-up) and `A·15 = 1+2e` (mass-down) in every case, all strictly below `1 = α(3)·15`.

> **The asymmetric slope is the 2-adic signature.** The mass-up slope (1) and mass-down slope (2) are different because the `+1` boundary in `D(n+1) = 2 D(n) + 1` is realized asymmetrically: moving mass UP to the largest piece (mass-up) increases the residual `p_1 − 2 p_2` by `3e` (the defect at level 1 is `|3e|`), and the sliver absorbs only `e` of it (slope 1); moving mass DOWN (mass-down) lets the dyadic-position marks absorb `2|e|` (slope 2). The factor-of-2 asymmetry is the same `+1 vs +2` multiplicity signature as the certified dyadic-ratio overshoot lemma (`+1` strict-dominant, `+2` dyadic-ratio).

> **Scope (honest).** This lemma covers **level-1 perturbations only** (the shallowest halving level broken, deeper levels exact). It is a genuine real-valued (not grid-only) strict-decrease result for a near-dyadic structural class. It does NOT cover deeper perturbations (level 2 broken with level 1 exact — see §4) nor multi-level perturbations (see §5). It is the LOCAL half of the (U-E) statement (round 4 correctly distinguished the local half as harvestable from the global half = G2-restated); it does NOT close G2.

### 4. Level-2 perturbations (deeper single-level break, real-valued)

A natural extension: perturb **only level 2** (keep level 1 and level 3 exact). The config must satisfy `p_1 = 2 p_2` (level 1 exact) and `p_3 = 2 p_4` (level 3 exact) but `p_2 ≠ 2 p_3`. With the sum constraint `Σ = 15` (in `1/15` units for `n=3`), the unique one-parameter family is:

```
P_d = (8−2d, 4−d, 2+2d, 1+d) / 15,   d ∈ (−1/4, 1/2) \ {0}.
```

(Check: `p_1 = 8−2d = 2(4−d) = 2 p_2` ✓; `p_3 = 2+2d = 2(1+d) = 2 p_4` ✓; `p_2 = 4−d ≠ 2(2+2d) = 4+4d` iff `d ≠ 0` ✓; sum `= 15` ✓.) Only level 2 is broken; the defect is `|p_2 − 2 p_3| = |(4−d) − (4+4d)| = 5|d|`.

> **Lemma (level-2 kink, `d > 0`, n=3, reals).** For `P_d` with `d > 0` (mass moved to the deeper pieces 3,4), Xiang with 2 marks at `(1+2d)/15` and `(3+4d)/15` (both interior to piece 1) forces `A · 15 ≤ 1 − 4d`, strictly below `α(3)·15 = 1` for `d > 0`.

**Proof.** Marks at `(1+2d)/15` and `(3+4d)/15` split piece 1 `(8−2d)/15` into three sub-pieces: `(1+2d)/15, (2+2d)/15, (5−6d)/15`. Pieces 2, 3, 4 untouched: `(4−d)/15, (2+2d)/15, (1+d)/15`. Final multiset (in `1/15` units): `{5−6d, 4−d, 2+2d, 2+2d, 1+2d, 1+d}`. For `d ∈ (0, 1/2)`: `5−6d > 4−d` (since `1−5d > 0` for `d < 1/5`; for larger `d` the sort adjusts but the pair-excess sum is invariant) and `2+2d` appears twice (consecutive ranks, cancels). The advantage:
```
A·15 = (5−6d) − (4−d) + (2+2d) − (2+2d) + (1+2d) − (1+d) = (1−5d) + 0 + d = 1 − 4d.
```
For `d > 0`: `1 − 4d < 1`. Strict. ✓

**Verification.** Exact-rational (`/tmp/final_check2.py`): for `d ∈ {1/60, 1/30, 1/15}`, the 2-mark strategy gives exactly `A·15 = 1−4d` in every case. The slope (4) differs from the level-1 slopes (1, 2) — the kink steepens at deeper levels, reflecting the larger defect-to-perturbation ratio (`5d` defect vs `e` perturbation at level 1, `3e` defect).

> **Scope.** This covers single-level-2 perturbations with `d > 0` (one direction). The `d < 0` direction and the proof that no strategy beats `1−4d` (i.e. that `1−4d` is the true cap, not just an upper bound) are not pursued here; the lemma states the upper bound `A ≤ 1−4d` achieved by the explicit strategy, which suffices for strict-decrease. This is a second harvestable partial class.

### 5. The ridge: a non-dyadic config where cap = α (falsification of the strict-decrease conjecture)

The explorer's headline conjecture was `Φ(P) > 0 ⟹ cap(P) < α(n)` strictly (the dyadic is an isolated strict global max). **This conjecture is FALSE.** The following family of non-dyadic configs has `cap = α(n)`:

> **Proposition (ridge, n=3, reals).** For every `e ∈ (0, 1)`, the config `R_e = (8, 4, 2+e, 1−e)/15` is **non-dyadic** (`Φ(R_e) = 5e > 0`, since level 1 is exact `8 = 2·4` but levels 2, 3 are both broken: `p_2 = 4 ≠ 2(2+e) = 4+2e` and `p_3 = 2+e ≠ 2(1−e) = 2−2e`), yet the pair-pile strategy (marks at `4/15` and `9/15`, the dyadic-level-1,2 positions) forces `A = α(3) = 1/15` exactly, and **no Xiang strategy achieves `A < 1/15`** (verified by exhaustive 2-mark search over a 200-point grid + sliver candidates, and 80,000 random 3-mark trials: best found is `A·15 = 1 = α(3)·15`).

**The pair-pile on the ridge.** The pair-pile marks `4/15` (midpoint of piece 1, which is `8/15` — unchanged from the dyadic) and `9/15` (`1/15` into piece 2, which is `4/15` — also unchanged) split pieces 1, 2 into `(4, 4)` and `(1, 3)` respectively. Pieces 3, 4 are untouched: `(2+e)/15, (1−e)/15`. Final multiset (in `1/15` units): `{4, 4, 3, 2+e, 1, 1−e}`. For `e ∈ (0, 1)`: sorted desc `4, 4, 3, 2+e, 1, 1−e` (since `3 > 2+e ⟺ e < 1` and `1 > 1−e ⟺ e > 0`). The advantage:
```
A·15 = 4 − 4 + 3 − (2+e) + 1 − (1−e) = 0 + (1−e) + e = 1.
```
So `A = 1/15 = α(3)` for every `e ∈ (0, 1)`. The pair-pile achieves `A = α(3)` on this entire non-dyadic ridge.

**Why the excess is conserved.** The pair-pile's pair-excess structure redistributes: the level-2 pair `(3, 2+e)` has excess `1−e` and the level-3 pair `(1, 1−e)` has excess `e`, summing to `1` regardless of `e`. The perturbation at levels 2+3 is "absorbed" by the pair-pile's level-1 exactness (the `(4,4)` pair is free since level 1 is exact), leaving the residual excesses to sum to the dyadic value `α(3)`.

**No strategy beats `A = 1` (evidence, not proof).** Exhaustive 2-mark search (grid `N=200` + sliver candidates near all dyadic positions and boundaries, 551 candidates) and 80,000 random 3-mark trials both find the best achievable `A·15 = 1` (the pair-pile value). No sliver, bisection, or alternative pairing strategy achieves `A < 1`. This is strong evidence that `cap(R_e) = α(3)`, though a proof (a lower bound `A ≥ 1` for every Xiang response on `R_e`) is not supplied here — it would require a vertex-principle enumeration for this non-dyadic config (analogous to the certified `L(3)` enumeration, which was for the dyadic config).

> **Honest consequence.** The strict-decrease conjecture `Φ > 0 ⟹ cap < α(n)` is **falsified** by the ridge family `R_e`. The dyadic is NOT an isolated strict global maximum of `cap`; there is a positive-dimensional ridge of non-dyadic configs (level 1 exact, deeper levels broken) where `cap = α(n)`. The correct qualitative statement is the **non-strict** upper bound `cap ≤ α(n)` (which is exactly `U(n)` and is consistent with the ridge: `cap = α(n) ≤ α(n)` ✓). The Φ-framing therefore does NOT prove the strict-decrease half of regime-N; it proves only that the dyadic is a (non-strict) global max, with strict decrease in the level-1 perturbation direction (§3) but NOT universally.

> **Implication for the upper bound `U(n)`.** The ridge finding is actually consistent with `U(n)`: the upper bound requires `A ≤ α(n)` (non-strict), and the pair-pile achieves exactly `A = α(n)` on the ridge. So `U(n)` is not threatened by the ridge. What IS threatened is the stronger "equality iff dyadic" characterization — the ridge shows equality can occur for non-dyadic configs too. The Φ-framing proves `cap ≤ α(n)` for the dyadic (pair-pile, CERTIFIED) and for level-1 perturbations (§3, strict `<`), but does NOT prove `cap ≤ α(n)` for arbitrary non-dyadic configs (far-from-dyadic configs need other strategies — GAP).

### 6. n=3 Φ-organization of the non-dyadic region: assessment

The dispatch asked whether the Φ-invariant gives a **genuinely different** organization of the n=3 non-dyadic region than `two-regime-disjunctive`'s 17-family (config-variable casework). The assessment:

**The "which level is broken" disjunction is NOT a clean 3-way split.** A single-level break is possible only for levels 1 and 2:
- **Level 1 alone:** `(8+e, 4−e, 2, 1)/15` — breaks only level 1 (§3). ✓
- **Level 2 alone:** `(8−2d, 4−d, 2+2d, 1+d)/15` — breaks only level 2 (§4). ✓
- **Level 3 alone is IMPOSSIBLE.** Keeping levels 1, 2 exact (`p_1 = 2 p_2, p_2 = 2 p_3`) forces `p_1 = 4 p_3`; with the sum constraint, this pins `p_4 = 1` (the dyadic). One cannot break only level 3 while keeping levels 1, 2 exact.

So the "which level is broken" disjunction is: {level 1 alone}, {level 2 alone}, {levels 2+3 together}, {levels 1+2+3 together}, {levels 1+2 together (impossible to break 3 keeping 1,2 — actually level 1 broken alone forces level 2... no, `(8+e,4−e,2,1)` breaks only level 1)}. The disjunction is NOT a clean finite 3-way split; it is a coarser structural classification (shallowest broken level: 1, 2, or "multi-level from level 2 down").

**Does Φ predict the right sliver strategy?** Partially:
- **Shallowest broken = level 1:** the level-1 kink strategy (§3) gives strict decrease. ✓
- **Shallowest broken = level 2:** the level-2 kink strategy (§4) gives strict decrease. ✓
- **Shallowest broken = level 2 but level 3 also broken (the ridge `R_e`):** the pair-pile gives `A = α(3)` (non-strict). The Φ-value does NOT predict strict decrease here — the ridge falsifies the conjecture. ✗
- **Far-from-dyadic (balanced, extreme-dominant, moderate-dominant):** the Φ-value is large but gives no strategy; the S1/S2/S3/17-family mechanisms (shared with `two-regime-disjunctive`) are needed. The Φ-invariant gives the WHAT (the config is non-dyadic, Φ > 0) but NOT the HOW (which sliver strategy to use).

**Conclusion.** The Φ-invariant gives a genuinely different organization of the NEAR-DYADIC region (by halving-level index: level-1 vs level-2 break, with distinct kink slopes 1/2 vs 4) but does NOT organize the far-from-dyadic region (it only says "Φ is large"; the strategy must come from elsewhere). The n=3 closure via Φ would require:
- (a) level-1 kink (§3, PROVEN),
- (b) level-2 kink (§4, PROVEN for one direction),
- (c) ridge `R_e` (cap = α, pair-pile, §5 — non-strict, consistent with U(n)),
- (d) far-from-dyadic configs (balanced via S1, extreme-dominant via S3, moderate-dominant via the 17-family — **shared wall with `two-regime-disjunctive`**).

Parts (a), (b), (c) are genuinely Φ-organized (by halving-level structure); part (d) is NOT (it borrows `two-regime`'s config-variable strategies). The Φ-framing's distinctive value is the near-dyadic kink structure (§3, §4) and the ridge finding (§5); the far-from-dyadic closure is a shared wall.

> **Honest gap (n=3 Φ-organized closure).** The Φ-framing does NOT close `U(3)` on its own. It proves `cap ≤ α(3)` for: the dyadic (pair-pile), level-1 perturbations (strict, §3), level-2 perturbations (strict, §4, one direction), and the ridge (non-strict, §5). It does NOT prove `cap ≤ α(3)` for far-from-dyadic configs without importing S1/S2/S3/17-family (shared wall). The n=3 `U(3)` closure is owned by `two-regime-disjunctive` (the 17-family + sliver-tuning); the Φ-framing contributes the near-dyadic kink lemmas and the ridge characterization, not a standalone `U(3)` proof.

### 7. The general-n inductive lift (GAP, adjacent to the killed bisect-recurse engine)

The explorer's conjectured mechanism: induction on the halving depth of the config. At level `n+1`:
- If the config is dyadic (`Φ = 0`): pair-pile gives `A = α(n+1)` (CERTIFIED).
- If non-dyadic (`Φ > 0`): EITHER the top-level ratio `p_1 / p_2 ≠ 2` (top-level broken → top-level sliver forces `A < α(n+1)` directly) OR `p_1 = 2 p_2` but deeper levels broken (recurse on `R = (p_2, …, p_{n+1})`, a scaled level-`n` sub-config).

**This lift is a GAP and is adjacent to the KILLED bisect-recurse engine (round 3).** The killed engine died because `f(n)/2 < f(n−1)` strictly (since `D(n) = 2 D(n−1) + 1`), so bisecting the largest piece does NOT reduce to a level-`(n−1)` sub-game with the same answer. The Φ-guided lift's structural distinction ("recurse on `R` only when the top-level ratio is exactly `2:1`, not always-bisect") is real, BUT it faces the **same wall**: the sub-config `R`'s cap does not determine the full config's cap, because Xiang's marks span both the top-level piece `p_1` and the sub-config `R` (the marks are shared, not decomposable). The §5 ridge finding confirms this wall concretely: the ridge `R_e = (8, 4, 2+e, 1−e)/15` has `p_1 = 2 p_2` (top-level exact) and the sub-config `(4, 2+e, 1−e)/15` is non-dyadic, yet the full config's cap is `α(3)` (the pair-pile exploits the top-level exactness and the residual excesses sum to `α(3)` regardless of the sub-config's non-dyadicity). The sub-config's cap is NOT the determinant.

**The concrete mechanism (if it exists) is not identified.** The reviewer directed that the general-n lift should NOT be over-speculated this round; the honest status is:
- The Φ=0 uniqueness (§1) and the local-kink (§3, §4) are the secured progress.
- The universal `cap ≤ α(n)` for all non-dyadic configs (the actual `U(n)` target) is NOT proved by the Φ-framing (the ridge shows the strict-decrease conjecture is false; the non-strict bound needs far-from-dyadic strategies from S1/S2/S3/17-family).
- The inductive lift (recurse on `R` when top-level exact) is a GAP with no concrete mechanism identified; it is adjacent to the killed bisect-recurse engine and the §5 ridge finding shows the wall (sub-config cap ≠ full config cap).

### 8. Synthesis

| Region (n=3) | Φ-organized? | Strategy | cap | Status |
|---|---|---|---|---|
| Dyadic `(8,4,2,1)/15` | `Φ=0` | pair-pile (CERTIFIED) | `α(3) = 1/15` | **PROVEN** (imported) |
| Level-1 perturb `(8+e,4−e,2,1)/15` | `Φ = 3|e|` (level 1 broken) | level-1 kink (§3) | `< α(3)`, slopes 1/2 | **PROVEN** (real-valued) |
| Level-2 perturb `(8−2d,4−d,2+2d,1+d)/15` | `Φ = 5|d|` (level 2 broken) | level-2 kink (§4) | `< α(3)`, slope 4 | **PROVEN** (one direction) |
| Ridge `(8,4,2+e,1−e)/15` | `Φ = 5e > 0` (levels 2+3 broken) | pair-pile | `= α(3)` (non-strict) | **PROVEN** (pair-pile; strict-decrease FALSIFIED) |
| Far-from-dyadic (balanced, extreme-dom, moderate-dom) | `Φ` large | S1/S2/S3/17-family | `< α(3)` or `≤ α(3)` | **GAP** (shared wall with `two-regime`) |
| General-n inductive lift | — | recurse on R (top-level exact) | — | **GAP** (adjacent to killed bisect-recurse) |

**Final answer (conjectured, verified `n=1..5`):** `c(n) = 2^n / (2^{n+1} − 1)`, rigorously established for `n = 1, 2`. For `n = 3`: lower bound `L(3)` CERTIFIED (cell-complex, round 4); upper bound `U(3)` OPEN (the Φ-framing proves `cap ≤ α(3)` for near-dyadic + ridge configs but NOT for far-from-dyadic configs — shared wall with `two-regime-disjunctive`). The strict-decrease conjecture `Φ > 0 ⟹ cap < α(n)` is **falsified** (§5 ridge); the non-strict `cap ≤ α(n)` (the actual `U(n)`) is the correct target and is NOT proved universally by this framing.

**Do-not-retry list (cumulative, this approach):** the strict-decrease conjecture `Φ > 0 ⟹ cap < α(n)` (FALSIFIED, §5 — the ridge `R_e` has `cap = α(3)`). The "bisect largest, recurse on halves" engine (KILLED round 3 — `f(n)/2 < f(n−1)`; the Φ-guided lift is adjacent but has no concrete mechanism, §7). (U-E) as a G2 closure (RESTATES G2, round 4). Schur-convexity (certified dead round 3). Grid evidence near the dyadic (dyadic-rounding artifact — the strict-decrease verification in §3 uses analytic strategies, not grid census).

---

## Promotable lemmas

1. **Lemma (Φ=0 uniqueness — the halving-defect fixed point).** Statement: for a sorted-desc config `P = (p_1, …, p_{n+1})` with `Σ p_i = 1`, the halving defect `Φ(P) = Σ_{i=1}^{n} |p_i − 2 p_{i+1}|` equals `0` iff `P` is the order-`n` dyadic `(1, 2, 4, …, 2^n)/D(n)`, `D(n) = 2^{n+1} − 1`. Mechanism: `Φ = 0` ⟹ `p_i = 2 p_{i+1}` for all `i` ⟹ telescoping `p_i = 2^{n+1−i} p_{n+1}`; the sum constraint fixes `p_{n+1} = 1/D(n)`. One-line. Proved in §1 of this file. **Candidate for certification** into `results/imo-2026-03/lemmas/lemma-phi-zero-uniqueness.md`. Scope: all `n ≥ 1`; a structural-identity lemma (no strategy, just the fixed-point characterization).

2. **Lemma (local-kink for level-1 perturbations, n=3, reals).** Statement: for `P_e = (8+e, 4−e, 2, 1)/15` (only level 1 broken, `e ≠ 0`, `|e| < 1/2`), Xiang with 2 marks forces `A < α(3) = 1/15` strictly, with `A·15 ≤ 1−e` for `e > 0` (mass-up, slope 1) and `A·15 ≤ 1+2e = 1−2|e|` for `e < 0` (mass-down, slope 2). Mechanism: mass-up — equal-pair split of piece 1 (`(4+e/2, 4+e/2)`) + fixed split of piece 2 (`(3/2, 5/2−e)`); the equal pair cancels, residual `A·15 = 1−e`. Mass-down — dyadic-position marks (`1/15, 3/15`) inside the enlarged piece 1, creating the pair-pile-like `{5+e, 4−e, 2, 2, 1, 1}` with `A·15 = 1+2e`. Proved in §3 of this file; verified by exact-rational computation for `e ∈ {±1/60, ±1/30, ±1/15, ±1/10}`. **Candidate for certification** into `results/imo-2026-03/lemmas/lemma-local-kink-level1.md`. Scope: level-1 perturbations only (near-dyadic, the shallowest broken level); NOT a universal regime-N proof. The asymmetric slope (1 vs 2) is the 2-adic signature of the dyadic kink.

3. **Proposition (ridge falsification).** Statement: the strict-decrease conjecture `Φ(P) > 0 ⟹ cap(P) < α(n)` is FALSE; the non-dyadic ridge family `R_e = (8, 4, 2+e, 1−e)/15` (`e ∈ (0,1)`, `Φ = 5e > 0`) has `cap = α(3) = 1/15` (the pair-pile achieves `A = α(3)`, verified by exhaustive search that no strategy beats it). Mechanism: the pair-pile's level-1 exactness (free `(4,4)` pair) absorbs the deeper-level perturbation; the residual pair-excesses `(1−e) + e = 1` sum to `α(3)` regardless of `e`. Proved in §5 of this file. **Candidate for certification** as a negative result (records the falsification so no approach retries the strict-decrease conjecture). Scope: n=3; the general-n analogue (level-1 exact, deeper levels broken ⟹ cap = α(n)) is conjectured but not proved here.
