# Proof-reviewer report — round 6 — imo-2026-03 (IMO 2026 P3)

Two slugs built. Both reviewed independently and adversarially. Every new claim was
re-derived from scratch and numerically verified. **No overclaim in either** — both builders
honestly self-report `partial` with explicit open gaps, and both are genuinely `partial`.

---

## Slug: self-similar-recursion — Verdict: CHANGES REQUESTED (Status: partial)

**Scores.** Correctness 10/10 (what is written is valid) · Completeness 6/10 (two named open
gaps A′, B) · Progress: real — closes the isolated-cycle half of Gap A.

**New content this round: Lemma CC (isolated-cycle exclusion).** Independently verified:
- **Even cycle:** the alternating vector `d(Q_i)=(-1)^i` (zero off-cycle) lies in `ker U` because
  every cycle piece row gives `(-1)^{i-1}+(-1)^i=0` and, since the cycle components have degree
  exactly 2 (isolated), no off-cycle piece touches them, so all other rows vanish on `supp(d)`. This
  contradicts the certified `ker U={0}` (Lemma S-core). I confirmed the alternating `d` is in the
  cyclic-incidence kernel for `r=2,4,6`. The `r=2` sub-case (`b_1=b_2` forced, impossible) is correct.
- **Odd cycle:** the unique cyclic solution `u_j=½Σ_t(-1)^t b_{j+1+t}`; choosing the start so the
  largest budget `b_M=2^{a_max}` gets sign `-1` gives `2u_j ≤ -b_M+Σ_{ℓ≠M}b_ℓ < 0` by the
  superincreasing bound `Σ_{a<a_max}2^a<2^{a_max}`, contradicting `w(Q_j)>0`. I re-derived the `r=3`
  case by hand (reduces to the triangle inequality, which distinct powers of two always violate) and
  ran a brute-force check: **0 all-positive solutions among 197064 odd cyclic systems** (`r∈{3,5,7}`,
  exponents `0..8`). The load-bearing use of the numeric powers-of-two budgets is genuine (immune to
  the explorer's pure-incidence 479-instance refutation, whose examples all have off-cycle degree-≥3
  pieces = non-isolated).

Lemma CC is sound and CERTIFIED → `lemmas/isolated-cycle-exclusion.md`.

**Remaining gap (precisely).** Gap A is narrowed but NOT closed:
- **(A′) non-isolated cycles** — chord / off-cycle degree-≥3 piece / multiplicity-≥2 edge. The
  restricted equations become inequalities `u_{i-1}+u_i ≤ b_i` and the telescoping no longer forces a
  sign contradiction. The builder honestly reports the full-cycle superincreasing telescoping did not
  close (off-cycle surplus terms enter with uncontrolled signs). OPEN.
- **(B) `μ=3` even-block piece-leaf** `{v,v,v}`, `v=2^k/3` shared — no local move excludes it; the
  degenerate-Φ-dominator (Lemma BD) was not constructed. OPEN, unchanged.

Steps 0–5 (reduction, induction, degenerate leg, S-core, M2/M3/M4, block formula, conditional
integrality via leaf-peeling) are complete and sound; §5 correctly labels itself CONDITIONAL on A+B.
No re-introduction of the refuted Lemmas W/S/T or the V-kink move. The recorded self-status `partial`
is CORRECT. Elo → 1671 (lead).

---

## Slug: dual-integer-certificate — Verdict: CHANGES REQUESTED (Status: partial)

**Scores.** Correctness 10/10 · Completeness 4/10 (two open gaps, neither closed) · Progress:
moderate — a proven identity and a decisive negative finding, but no gap closed.

**New content: Lemma DUAL (dual value identity).** Verified: for full-column-rank integer `U` with
`Uw=b`, and any `s`, the system `Uᵀλ=s` is rationally solvable and `λᵀb=sᵀw` for EVERY solution `λ`
(value-independent since solutions differ by `δ∈ker Uᵀ` and `δᵀb=δᵀUw=0`). I confirmed
value-independence across two distinct `λ` on random `5×3` systems and on the Gap-D config. This is
elementary linear algebra, correct and unconditional. CERTIFIED → `lemmas/dual-value-identity.md`.

**Decisive negative finding: Gap D is NOT universal.** Verified independently: the S-core config
`{2,4/3,4/3,4/3,1}` (cut `4` into thirds) has `U=[[0,0,1],[1,0,0],[0,3,0]]`, `det U=±3`, `Uw=b`,
`f=5/3`, and `Uᵀλ=s` gives `3λ_2=-1` — no integer `λ`. So the integer-dual route needs minimality; it
is a different OBJECT (a GCD-1/lattice condition) but the same difficulty class as the primal route.
This is a valuable, honest negative result. CERTIFIED as a fact → `lemmas/gap-d-not-universal.md`.

**Remaining gaps (both open, neither closed this round):**
- **Gap D at minimizers:** `s∈Uᵀℤ^{n+1}` (equivalently GCD-1 of the maximal minors of `U`). Only
  numerical evidence (`n=2`: 9/9; `n=3`: 34/34 at `f=1`).
- **Pos (`f≠0`):** an independent gap — the all-even (budget) and odd-cancellation sub-cases are both
  unproven. Correctly noted as non-circular.

The route is a legitimately distinct framing (mandated diversity) and contributes a proven identity +
a sharp reformulation, but it did not close the residual. Self-status `partial` is CORRECT. Registered
Elo 1523.

---

## Certified this round (3, total now 19)
- `isolated-cycle-exclusion.md` (Lemma CC) — self-similar.
- `dual-value-identity.md` (Lemma DUAL) — dual-integer.
- `gap-d-not-universal.md` (fact) — dual-integer.

## Goal Progress (for run state)
- Status stays **partial**; still one gap from solved, but the sole residual is further narrowed.
- **self-similar-recursion (advanced, Elo 1671, lead):** Gap A's isolated-cycle half CLOSED via
  Lemma CC (powers-of-two essential). Residual = **(A′) non-isolated cycles** + **(B) μ=3 even-leaf**.
- **dual-integer-certificate (partial, Elo 1523, new framing):** Lemma DUAL proven; Gap D shown
  minimality-dependent (not universal). Residual = **Gap D at minimizers (GCD-1)** + **Pos (f≠0)**.
- Both routes now bottom out on a minimality-forcing structural fact about the incidence matrix `U`
  at the Φ-max minimizer (A′: no non-isolated cycle survives; Gap-D: minors coprime). These are the
  same underlying wall viewed two ways — the primal "no surviving cycle/forest" and the dual
  "coprime minors" are Smith-normal-form duals. Next round should attack THAT (the minimality⇒
  benign-`U` step) directly — e.g. a degenerate-Φ-domination / rank-contiguity (laminar) argument
  that a minimizer cannot host either a non-isolated cycle or a concentrated multiplicity-≥2 block.
- Numerically `min f = 1` for `n≤4` (answer and both bounds still TRUE; upper bound certified).
