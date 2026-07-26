# proof-reviewer — round 3 — `imo-2026-03`

Reviewer spot-checks (python3, exact `Fraction` + random reals):
- **e_M ≤ o_R reduction (level-3 dyadic, correct budget ≤3 Xiang marks): 0 violations in 50k random real marks.** (Reviewer's first pass had violations — a test bug: Liu's marks were omitted from `pieces_from_marks`. Redone with Liu's marks included, the lower bound L(2), L(3) hold for reals: 0 violations in 300k, min `A = 1/7`, `1/15` respectively. Grid c(2) min `A=1/7` (7 minimizers), c(3) min `A=1/15` (40 minimizers) — match builder.)
- **Integer-grid parity theorem**: verified on grid c(2) (`A·7=1`), c(3) (`A·15=1`). Proof algebra re-derived and correct.
- **CK lemma**: one-line, correct (`A = Σ(p_{2i−1}−p_{2i}) + p_{2m+1} ≥ p_{2m+1}`).
- **Dyadic-ratio overshoot**: core (multiplicity +1 strict / +2 dyadic; even block → 0, odd block → ±a_2) correct. **Corollary "cancels iff a_1 > 2 a_2" is OVERCLAIMED for even m** — counterexample `(6,3,3)`: `m=2`, dyadic ratio, `m+2=4` even → cancels (corollary predicts overshoot). Valid only for m odd (generic m=1, which is the dyadic-config case). "Overshoots at every step" is loose — greedy takes ONE admissible step on the dyadic then `a_1=a_2` (no admissible cut). Certified the core with this caveat stamped on the lemma file.

---

## 1. `pairing-partner` (Engine C, G1) — verdict: CHANGES REQUESTED, Status: partial

**What was built.** Three rigorous results:
- **(R1) Reduction `L(n+1) ⟺ e_M ≤ o_R`** — pure algebra: `oddsum = (M − e_M) + o_R`, so `oddsum ≥ M ⟺ e_M ≤ o_R`. Independent of `k` (no per-`k` classification, no WLOG-`k` exchange). Localizes the interleaving obstruction to a single inequality on the merged sort. Verified 0 violations (n=2,3 grid + 500k reals; reviewer spot-confirmed 50k).
- **(R2) Integer-grid parity theorem** — scale by `D(n)` (odd); even-count uses pair-excess parity `Σ e_i ≡ D(n) ≡ 1 (mod 2)` (non-neg odd ≥ 1); odd-count uses leftover `q_M ≥ 1`. Rigorous but grid-only (honestly admitted: finer odd grid `K·D(n)` gives weaker `A ≥ 1/(K·D(n))`).
- **(R3) n=1 real case** — closes the real lower bound for c(1): every real Xiang response to `(1,2)/3` gives `A ≥ 1/3` (the `±a` cancellation when the mark splits the largest piece; strict when in the smallest). Algebra re-derived and correct.

**Load-bearing step re-derived.** The R1 reduction is the headline. The algebra `oddsum = o_M + o_R = (M − e_M) + o_R` is trivial and correct; the equivalence to `e_M ≤ o_R` is exact. The self-compensation pairing (every RM pair self-compensates by within-pair sortedness `r_odd ≥ m_even`, reducing `e_M ≤ o_R` to the residual Match `Σ_{MM} m_even ≤ Σ_{RR} r_odd`) is also trivial-but-correct algebra. Both certified as lemmas.

**Gaps / honesty.** (R1) is a REFORMULATION, not a proof of `e_M ≤ o_R`. The residual (Match) — a Hall-type matching of `MM`-pair smaller halves to `RR`-pair larger halves — is OPEN for general real `n` (verified 0 violations, no analytic proof). The builder says this explicitly and does not overclaim. (R2) is honestly restricted to grid-aligned marks. The conjecture (S) "smallest ≥ α(n) at minimizer" is reported FALSE for reals (sub-α fragments cancel at odd ranks) — honest. The builder's own Status `partial` is correct.

**Verdict.** Real, rigorous progress: the e_M ≤ o_R reduction + self-compensation localization + n=1 real closure + grid-parity (all-n grid) are all correct and reusable. But G1 (k≥2 reals) remains OPEN (the residual Match). CHANGES REQUESTED — re-dispatch to attack the residual (Match) (the superincreasing structure of R is the flagged lever).

---

## 2. `two-regime-disjunctive` (Engine R-pile, G2) — verdict: CHANGES REQUESTED, Status: partial

**What was built.** Engine R-pile (greedy recursive pile-match: cut `a_2` out of `a_1` when `a_1 ≥ 2 a_2`, bisect fallback when balanced) was dispatched to close G2 (regime-N upper bound n≥3). It is **FALSIFIED** as the universal regime-N strategy by 3 counterexample classes:
- (i) dyadic `(8,4,2,1)/15 → A=1/5` overshoot (characterized cleanly by the dyadic-ratio overshoot lemma);
- (ii) balanced non-dyadic `(.5,.3,.15,.05) → Liu=11/20 > 8/15` (bisect fallback destroys cancellation);
- (iii) extreme-dominant tiny-tail `(.9,1/30,1/30,1/30) → Liu=0.9` (cuts remove only slivers).

The true optimal Xiang cap is `31/60 < 8/15` on every tested non-dyadic n=3 config (brute force), so the regime-N conjecture holds numerically; the greedy just fails to find it. The falsification is honest and recorded with explicit counterexamples (reviewer reproduced the dyadic overshoot `A=1/5` exactly).

**Harvested lemma.** Dyadic-ratio overshoot (one-step characterization). Core correct; corollary overclaimed for even m (caveat stamped on the lemma file). Certified with caveat.

**Honesty.** The builder does NOT present the falsified engine as progress — it is clearly recorded as a ruled-out mechanism. The regime-N gap for n≥3 is explicitly OPEN. A new direction (multiplicity-parity / even-block framing) is flagged as UNPROVED. The inherited progress (U(1), U(2), regime-D all-n pair-pile, n=1,2 end-to-end) stands.

**Verdict.** The ENGINE (R-pile) is dead, but the APPROACH (two-regime disjunctive) is alive — regime D closed, n=1,2 solved, a characterization lemma harvested, a new regime-N direction flagged. CHANGES REQUESTED (partial) — re-plan the regime-N engine (multiplicity-parity / even-block, NOT the greedy pile-match family).

---

## 3. `pairing-partner-transfer` (Engine A, G1) — verdict: RETHINK, Status: partial (inherited)

**What was built.** Engine A (extremal minimizer + non-improving 2-piece transfer; two-tail cancellation `T_M + T_R ≤ 0`) was dispatched as a COPY of `pairing-partner` branched to field a different engine for G1. It is **FALSIFIED** on n=3 brute force: 21 of 33 k≥2 minimizers admit NO single-pair transfer (canonical or most-permissive) preserving minimality; best achievable `A' = 2/15 > α(3) = 1/15`. The two ΔA tails ADD (the same `−2T` wall that killed per-mark induction). The hard-failure counterexample `C* = {8/15, 2/3}` is exhibited concretely (reviewer-verified arithmetic: canonical transfer → pieces `(5,3,2,2,2,1)/15`, `A = 5−3+2−2+2−1 = 3/15 = 1/5 > 1/15`). Honest dead-end recorded with the instruction "do not retry Engine A / 2-piece transfer."

**Harvested lemma.** CK (odd-count cheap-kill) — one-line, correct, certified. Honest limitation noted (odd-count only; doesn't lift to reals; doesn't cover even-count minimizers).

**Honesty.** The builder does not present Engine A as progress — it is recorded as a dead-end-with-reason. Conjecture (S) is reported as VERIFIED-but-not-proved (shares the same `−2T` hard step, not an independent closure) — honest. The inherited partial progress (k=0, k=1, pair-pile, n=1,2) stands; the approach does NOT advance G1.

**Verdict.** The approach's central engine is dead and it is a near-twin of `pairing-partner` (single-gap risk per CLAUDE.md). It has no live engine and its framing (per-mark/transfer) is the same `−2T` wall. RETHINK — back to the outliner to retire or re-conceive far from the per-mark/transfer framing (the CK lemma is certified regardless and available to all approaches).

---

## Summary table

| slug | engine | engine outcome | approach status | verdict | newly certified |
|---|---|---|---|---|---|
| pairing-partner | Engine C (weight-function) | did not close G1; reduction + localization rigorous | partial | CHANGES REQUESTED | e_M≤o_R reduction, self-compensation, grid-parity, (n=1 real) |
| two-regime-disjunctive | Engine R-pile | FALSIFIED (3 counterexample classes) | partial (approach alive) | CHANGES REQUESTED | dyadic-ratio overshoot (with caveat) |
| pairing-partner-transfer | Engine A (two-tail) | FALSIFIED (n=3 brute force) | partial (inherited; no live engine) | RETHINK | CK lemma |

**Overall Status: partial.** `c(1)=2/3` (real case closed round 3) and `c(2)=4/7` stand end-to-end. G1 localized to `e_M ≤ o_R` / residual Match (OPEN for reals); G2 regime-N n≥3 OPEN (R-pile falsified, multiplicity-parity direction unproved). The integer-grid parity theorem proves L(n) on the grid for ALL n (does not lift to reals). Five new lemmas certified into the shared cache: `lemma-em-or-reduction`, `lemma-self-compensation`, `lemma-grid-parity`, `lemma-ck-odd-count`, `lemma-dyadic-ratio-overshoot` (with caveat).
