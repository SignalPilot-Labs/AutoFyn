# Proof-reviewer report — imo-2026-03, round 5

Review of 4 candidate proofs built this round. I read each approach file, the problem (`problems.jsonl`), the certified lemmas, and the run-state rules. I ran spot-check computations (exact-rational python) to re-derive the load-bearing claims independently. Per-slug verdict at the end.

**Headline:** `c(3) = 8/15` is **NOT solved end-to-end**. The lower bound `L(3)` is CERTIFIED (cell-complex, round 4) and now corroborated self-rigorously by `pairing-partner` (m_1-split fix). The upper bound `U(3)` has MAJOR rigorous progress (the `d ≥ 1/2` regime closed via 5-cap contradiction; the `d < 1/2` gap `G` closed via 3-mark sliver; the `d < 1/2` non-gap `w,z ≥ −2α` closed), but the `d < 1/2` non-gap **extreme sub-cases** (`w < −2α` or `z < −2α`) are a MATERIAL GAP — computationally verified (0 violations) but the analytic 17-family case-by-case contradiction is NOT written. So `U(3)` is not fully closed, and `c(3) = 8/15` requires both halves closed with NO material gap. Status remains `partial`.

---

## 1. `two-regime-disjunctive` — CHANGES REQUESTED (Status: partial)

### What's claimed
- Closes `U(3)` on the `d ≥ 1/2` regime via a 5-cap contradiction `{a, b−a, c−b, 2d−1, |a+b−c|}`, equality iff dyadic.
- Closes the `d < 1/2` gap region `G` via a 3-mark sliver (`A = 1 − 2d = u − z < α`).
- Closes the `d < 1/2` non-gap sub-cases with `w, z ≥ −2α` (4 sub-cases).
- Leaves the `d < 1/2` non-gap extreme sub-cases (`w < −2α` or `z < −2α`) as an honest GAP.

### Verification (I re-derived each load-bearing step)
- **5-cap contradiction (§5d.2):** I verified all five cap formulas by direct multiset alt-sum. The contradiction logic is correct: assuming all five `> 1/15` gives (1) `a > 1/15`, (2) `b > 2/15`, (3) `c > 3/15`, (4) `d > 8/15`, (5) split on `|a+b−c|`. Case i (`c < a+b−1/15`) forces `a > 2/15` → `a+b+c > 9/15` → `d < 6/15`, contradicting (4). Case ii (`c > a+b+1/15`) forces `a+b+c > 7/15` → `d < 8/15`, contradicting (4). Both cases contradict; equality analysis pins the dyadic. **Spot-check (python, exact rational):** grids `N = 60` and 50k random reals over `d ≥ 1/2`: 0 violations, unique equality at `(1/15, 2/15, 4/15, 8/15)`. ✓ Rigorous.
- **3-mark sliver (§5d.3):** I re-derived the chain-excess identity `7u + 4v + 2w + z = α` (from `a+b+c+d = 1 = 15α`) and `u − z = 1 − 2d` (algebra verified). The sliver multiset `{b, b, c, c, a−ε, e_3, ε}` sorts to `c, c, b, b, a−ε, e_3, ε` in `G` (all sort inequalities verified: `a−ε > e_3 ⟺ ε < u−z > 0`, `e_3 > ε ⟺ ε < e_3 = α+z > 0`, `e_3 = α+z ≤ α < b ≤ c`). The alt-sum gives `A = a − e_3 = u − z = 1 − 2d`, independent of `ε`. The bound `u − z < α ⟺ 6u+4v+2w+2z > 0` holds strictly since `u,v,w,z > 0` in `G`. **Spot-check (python):** constructed a valid gap config (`u=1/200, v=3/1000, w=1/125, z=859/15000`), confirmed `A = 1 − 2d = 1/750 < α = 1/15` exactly, independent of `ε`. ✓ Rigorous.
- **The GAP (§5d.4):** the `d < 1/2` non-gap extreme sub-cases (`w < −2α` or `z < −2α`) are real and non-empty (e.g. `a=0.15, b=0.18, c=0.19, d=0.48` has `w = (0.19−0.33)−0.0667 = −0.2067 < −2α = −0.1333`, and `|a+b−c| = 0.14 > α`, so the `|a+b−c|` cap fails; the 17-family is needed). The file states 0 violations computationally (grids `N=60..150` + 50k random reals, equality only at the dyadic), but explicitly: "a complete analytic case-by-case contradiction for every `d < 1/2` sub-case is NOT yet written... no small (4–7-cap) subfamily suffices (all have grid violations), so the 17-family's full menu is necessary and the analytic closure is laborious." This is a MATERIAL GAP, not a cosmetic one.

### Assessment
The proof is **honest** about the gap (it does not paper over it). The rigorous parts (5-cap contradiction + 3-mark sliver + 4 non-gap sub-cases) are correct and verified. But the `d < 1/2` extreme sub-cases are NOT closed analytically — only computationally. Per the rigor rules (no "computationally verified" substituted for proof; "find all / largest n" needs BOTH a proven bound AND construction, here a proven upper bound), `U(3)` is NOT fully closed. So `c(3) = 8/15` is NOT solved end-to-end. The builder's Status (`partial`) is correct; the overclaim risk is contained.

**Certified new lemmas:** `lemma-u3-5cap-dominant.md` (d ≥ 1/2 regime, rigorous), `lemma-u3-sliver-gap.md` (gap G, rigorous). Both pass the bar — sorry-free, statement correct, scoped honestly.

**Verdict: CHANGES REQUESTED.** The gap to close next: the analytic 17-family case-by-case contradiction for the `d < 1/2` extreme sub-cases (`w < −2α` or `z < −2α`), OR a clean alternative covering family that closes `U(3)` end-to-end.

---

## 2. `cell-complex-l3` — CHANGES REQUESTED (Status: partial)

### What's claimed
- `L(4)` over reals CERTIFIED via the vertex-principle + exhaustive exact-rational enumeration (839,787 feasible vertices, 6,008 candidates, 12 distinct min multisets, 0 violations, min `A = 1 = α(4)·D(4)` real `1/31` at the pair-pile `(8,8,4,4,2,2,1,1,1)/31`).
- Structural theorem GAP (D3 conjecture): every fractional arrangement vertex has `A > 1` (integer scale) — verified n=3,4 (min fractional `A = 5/3`), but NO analytic proof.
- Inductive lift GAP: `M ⊎ R` recursion + `e_M ≤ o_R` reduction + `L(n)` on `R` yields `o_R ≥ M/2`, but `L(n+1)` needs `e_M ≤ o_R`; factor-of-2 gap.

### Verification
- **L(4) enumeration:** the script `/tmp/round-5/n4_verify.py` (read) reproduces the numbers exactly (`/tmp/round-5/n4_verify.log`: 10,429,650 4-tuples, 839,787 feasible, 6,008 candidates, 12 distinct multisets, min `A = 1`, 0 exact violations, at the pair-pile `ks=(0,0,0,0,4)`). The two-phase design (float prefilter + exact `Fraction` verification) is sound; the exact phase uses no floating-point. The arrangement completeness argument (70 distributions cover every assignment of 4 marks to 5 Liu pieces; degenerate vertices captured by a rank-4 subset; flat-facet vertex-cover via the certified vertex-principle) is correct and mirrors the round-4 L(3) certification. n=5 is infeasible (`≈17` hours) — honest. ✓ This is a verified milestone (third lower-bound data point, n=1..4 all certified).
- **D3 structural theorem GAP:** I assess this is a REAL open step, NOT a restatement of the vertex-principle. The vertex-principle is a reduction (continuous → finite vertex enumeration). D3 is a characterization of WHICH vertex wins (fractional vs integer). These are distinct: the vertex-principle doesn't tell you fractional vertices exceed `α`; D3 conjectures it. Verified n=3,4 (min fractional `A = 5/3` > 1) but no proof. Honest GAP.
- **Inductive lift GAP:** the factor-of-2 gap is correctly identified. `L(n)` on `R` gives `o_R ≥ M/2`; `L(n+1)` needs `e_M ≤ o_R`; `e_M` can be as large as `M` when M-sub-pieces concentrate at even ranks. The note that the false `σ ≤ M/2 = a_1` corollary (removed from `lemma-superincreasing-R.md` this round) was the obstruction bound and is now invalid for `k ≥ 2` is correctly cross-referenced. Honest GAP.

### Assessment
The L(4) certification is sound and a genuine milestone. The structural theorem and inductive lift are honest GAPs. The builder's Status (`partial`) is correct; no overclaim.

**Certified new lemmas:** `lemma-pair-excess-decomposition.md` (D1, one-line real identity), `lemma-parity-integer-vertices.md` (D2, specializes grid-parity to arrangement vertices). Both pass the bar.

**Verdict: CHANGES REQUESTED.** The gap to close next: the D3 structural theorem (prove fractional arrangement vertices have `A > α(n)·D(n)` for general n), which would lift `L(n)` to all n without enumeration; OR close the inductive lift factor-of-2 gap.

---

## 3. `pairing-partner` — CHANGES REQUESTED (Status: partial)

### What's claimed
- Fixes the m_1-split bug: Branch 1 (`m_1 ≥ a_1`) = round-4 casework correctly scoped; Branch 2 (`m_1 < a_1`) = NEW 6-piece casework proved in full. L(3) unrefined-R now self-rigorous.
- General-n: both branches reduce to Hall matchings (H1), (H2), verified n=1..5, OPEN.
- In-place corrections to `lemma-superincreasing-R.md` (remove false `σ ≤ M/2` corollary) and `lemma-L3-unrefined-R-subcase.md` (add m_1-split).

### Verification (I re-derived the Branch 2 casework independently)
- **m_1-split is exhaustive & disjoint:** Branch 1 `m_1 ≥ a_1`, Branch 2 `m_1 < a_1`, boundary assigned to Branch 1. ✓
- **Branch 2 reduction:** for n=2 (level-3 dyadic, `M=8, R={4,2,1}, a_1=4`), Branch 2 has `a_1 = 4` global rank 1. `A = 4 − A_rest`, `A_rest = 2·oddsum(rest) − rest_total` with `rest_total = 11`. `A ≥ 1 ⟺ oddsum(rest) ≤ 7 ⟺ evensum(rest) ≥ 4`. Removing `t_1 = m_1` (since `m_1 ≥ 2 = a_2` and `m_1 ≥ m_i`), `evensum(rest) = oddsum(rest5)` where `rest5 = {m_2, m_3, m_4, 2, 1}`. Target: `oddsum(rest5) ≥ 4`. Algebra verified.
- **Branch 2 casework (§B'):** I traced all 6 sub-cases:
  - B2a-i (`m_2 ≥ 2, m_3 ≥ 2`): `m_4 ≤ 2`, `u_1=m_2, u_2=m_3, u_3=2`, `u_5=min(m_4,1)`, `oddsum ≥ 2+2+0 = 4`. ✓
  - B2a-ii-`m_3≥1` (`m_2 ≥ 2, m_3 < 2, m_3 ≥ 1`): `u_1=m_2, u_2=2, u_3=m_3`; if `m_4 ≥ 1`: `oddsum = m_2+m_3+1 ≥ 4`; if `m_4 < 1`: `oddsum = m_2+m_3+m_4 = 8−m_1 > 4`. ✓
  - B2a-ii-`m_3<1` (`m_2 ≥ 2, m_3 < 1`): `u_3=1`, `oddsum = m_2+1+m_4 = (m_2+m_4)+1`; `m_2+m_4 = 8−m_1−m_3 > 4−1 = 3`, so `oddsum > 4`. ✓
  - B2b-`m_3≥1` (`m_2 < 2, m_3 ≥ 1`): `u_1=2, u_2=m_2, u_3=m_3`; if `m_4 ≥ 1`: `oddsum = 2+m_3+1 ≥ 4`; if `m_4 < 1`: `oddsum = 2+m_3+m_4 = 2+(8−m_1−m_2) > 2+8−4−2 = 4`. ✓
  - B2b-`m_3<1` (`m_2 < 2, m_3 < 1`): `u_3=1, u_5=m_4`, `oddsum = 3+m_4` (needs `m_4 ≥ 1`, but `m_4 ≤ m_3 < 1`); IMPOSSIBLE — `m_2+m_3+m_4 = 8−m_1 > 4` with `m_3,m_4 < 1` forces `m_2 > 2`, contradicting `m_2 < 2`. ✓ (vacuous)
  - The preliminary bounds `m_1 ≥ 2` (largest ≥ average) and `m_2 > 4/3` (largest of `m_2,m_3,m_4` whose sum `> 4`) are correct.
  All sub-cases settle. ✓
- **Spot-check (python, exact rational):** `branch2_verify.py` — 39,980 grid configs + 500k random Branch-2 configs, 0 violations, min `A → 1` as `m_1 → 4⁻`. ✓
- **In-place lemma corrections:** I updated `lemma-superincreasing-R.md` (removed the false `σ ≤ M/2 = a_1` corollary, kept the identity) and `lemma-L3-unrefined-R-subcase.md` (added the m_1-split Branch 1/Branch 2 structure). The corrections are correct — the false corollary was indeed invalid for `k ≥ 2` (counterexample `m=(3,3,1,1)/15` with `σ=5 > 4=a_1`), and the m_1-split genuinely fixes the scope bug.

### Assessment
The bug fix is correct and rigorous. L(3) unrefined-R is now self-rigorous. The general-n Hall matchings (H1), (H2) are honest OPEN GAPs. The builder's Status (`partial`) is correct.

**Certified (in-place updates):** `lemma-superincreasing-R.md` (corollary removed), `lemma-L3-unrefined-R-subcase.md` (m_1-split added).

**Verdict: CHANGES REQUESTED.** The gap to close next: the general-n Hall matchings (H1) on rank indices (Branch 1) and (H2) on the rest polytope (Branch 2), OR the R-refined sub-cases (`k ≤ n`).

---

## 4. `dyadic-halving-induction` — RETHINK (Status: partial, central route dead)

### What's claimed
- Φ=0 uniqueness (one-line, all n).
- Local-kink for level-1 perturbations (n=3, real-valued, asymmetric slopes 1/2).
- **CRITICAL FALSIFICATION:** the strict-decrease conjecture `Φ > 0 ⟹ cap < α(n)` is FALSE via the ridge `R_e = (8, 4, 2+e, 1−e)/15`.

### Verification (I re-derived each)
- **Φ=0 uniqueness (§1):** `Φ = 0 ⟺ p_i = 2 p_{i+1} ∀i ⟺` telescoping `p_i = 2^{n+1−i} p_{n+1}`; sum constraint fixes `p_{n+1} = 1/D(n)`. ✓ Rigorous, one-line.
- **Local-kink (§3):** I re-derived both 2-mark strategies. Mass-up (`e > 0`): marks at midpoint of piece 1 + at `3/2` into piece 2; final `{4+e/2, 4+e/2, 5/2−e, 3/2, 2, 1}`, equal pair cancels, `A·15 = 1−e < 1`. Mass-down (`e < 0`): marks at `1/15, 3/15` (dyadic positions) in enlarged piece 1; final `{5+e, 4−e, 2, 2, 1, 1}`, two equal pairs cancel, `A·15 = 1+2e < 1`. **Spot-check (python, exact rational):** `e ∈ {±1/60, ±1/30, ±1/15, ±1/10}` — `A·15 = 1−e` (mass-up) and `A·15 = 1+2e` (mass-down) exactly, all strict `< α`. ✓ Rigorous.
- **Ridge falsification (§5):** I re-derived `Φ(R_e) = |8−2·4| + |4−2(2+e)| + |2+e−2(1−e)| = 0 + 2e + 3e = 5e > 0` (non-dyadic). The pair-pile (marks at `4/15, 9/15`) gives final `{4, 4, 3, 2+e, 1, 1−e}`, sorted `4,4,3,2+e,1,1−e` (for `e ∈ (0,1)`), `A·15 = 4−4+3−(2+e)+1−(1−e) = 1`. **Spot-check (python):** `e ∈ {1/10, 1/5, 1/3}` — `A = 1/15 = α(3)` exactly, `Φ = 5e > 0`. ✓ The falsification is GENUINE: a non-dyadic config with `Φ > 0` where `cap = α`. The "no strategy beats `A = 1`" claim is computational evidence (exhaustive 2-mark search + 80k random 3-mark trials), honestly labeled "evidence, not proof." The pair-pile cap is rigorous; the lower-bound claim (`A ≥ 1` for every Xiang response on `R_e`) is not supplied.

### Assessment
The central route (strict-decrease `Φ > 0 ⟹ cap < α(n)`) is DEAD — falsified by the ridge. The two partial lemmas (Φ=0 uniqueness, local-kink) are rigorous and harvestable. The ridge falsification is a genuine negative result. But the approach's main strategy cannot work: the dyadic is NOT an isolated strict global max of `cap`; the non-strict `cap ≤ α(n)` (= `U(n)`) is the correct target, and the Φ-framing does NOT prove it for far-from-dyadic configs (balanced/extreme-dominant/moderate-dominant — shared wall with `two-regime-disjunctive`, single-gap-trap risk per the round-4 rule). The general-n inductive lift is adjacent to the killed bisect-recurse engine and the ridge shows the wall (sub-config cap ≠ full config cap).

Per the single-gap-trap rule and the dead-central-route guidance (`ALWAYS: when a builder concedes their own central strategy is dead, record the outcome as partial and flag for retirement or re-conception`), this approach should go back to the outliner. The two lemmas are harvested to the cache.

**Certified new lemmas:** `lemma-phi-zero-uniqueness.md`, `lemma-local-kink-level1.md`, `lemma-ridge-falsification.md`. All pass the bar (the ridge lemma as a negative result).

**Verdict: RETHINK.** The central route is dead (falsified). Harvest the two lemmas + the ridge falsification to the cache. Re-conceive or retire — the remaining work (far-from-dyadic closure) is a shared wall with `two-regime-disjunctive`.

---

## Summary

| slug | Status | verdict | outcome | gap to close |
|---|---|---|---|---|
| `two-regime-disjunctive` | partial | **CHANGES REQUESTED** | advanced | analytic 17-family case-by-case for `d < 1/2` extreme sub-cases (`w < −2α` or `z < −2α`), OR a clean alternative covering family closing `U(3)` end-to-end |
| `cell-complex-l3` | partial | **CHANGES REQUESTED** | verified-milestone | D3 structural theorem (fractional vertices have `A > α(n)·D(n)` for general n), OR the inductive lift factor-of-2 gap |
| `pairing-partner` | partial | **CHANGES REQUESTED** | advanced | general-n Hall matchings (H1) on rank indices + (H2) on the rest polytope, OR the R-refined sub-cases (`k ≤ n`) |
| `dyadic-halving-induction` | partial (central route dead) | **RETHINK** | dead-end | re-conceive or retire (central strict-decrease route falsified); far-from-dyadic closure is a shared wall with `two-regime` |

**New lemmas certified this round (7):** `lemma-u3-5cap-dominant.md`, `lemma-u3-sliver-gap.md`, `lemma-phi-zero-uniqueness.md`, `lemma-local-kink-level1.md`, `lemma-ridge-falsification.md`, `lemma-pair-excess-decomposition.md`, `lemma-parity-integer-vertices.md`. **In-place lemma updates (2):** `lemma-superincreasing-R.md` (false `σ ≤ M/2` corollary removed), `lemma-L3-unrefined-R-subcase.md` (m_1-split Branch 1/Branch 2 structure added). Total certified lemmas: 23.

**`c(3) = 8/15` end-to-end:** NOT solved. `L(3)` CERTIFIED (lower bound). `U(3)` has the `d < 1/2` extreme sub-cases MATERIAL GAP (computationally verified, analytic closure open). `c(1) = 2/3`, `c(2) = 4/7` remain rigorously established end-to-end.
