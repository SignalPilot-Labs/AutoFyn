# Proof-reviewer report — imo-2026-03, Round 8

Three approaches built. All three are honest partials with genuine, verified new content. No overclaim
found. The problem is **not solved** — the full lower bound and the n≥3 upper bound remain open.

---

## 1. ll-inclusion-gap — Status: partial — Verdict: CHANGES REQUESTED — outcome: advanced

**Headline claim (VERIFIED CORRECT):** T(ℓ) closed for ALL ℓ via a mutual strong induction on the pair
`{Claim(n,ε), T(n)}`, hence **G-INC-1 = Claim(n,0) for all n** — the INC branch of Lemma LL for the
anchor `R = G_{n−1}` is now rigorous for every n.

**What I checked (load-bearing = Step 12b + Step 13 mutual induction):**
- **Arithmetic re-derived from scratch.** h=2 case: `deficit_top = 2^{n−2}−(q₁−q₂) = a+b`;
  `ΣP_lo = 2^{n−2}+ε'` with `ε' = a−b−τ` (T) / `ε+a−b` (Claim) — both confirmed. A-form conversions
  `A(P_lo) ≤ A(G_{n−3})−1−ε'` from `O_{P_lo}≤O_{G_{n−3}}` (via `2O_{G_{n−3}}=A(G_{n−3})+2^{n−2}−1`)
  correct. Target inequalities `1+2b+τ ≥ 1−τ` (2b-i) and `1+2a−τ ≥ 1−τ` (2b-ii) both hold from a,b≥0.
- **`ε' > −1` in 2b-ii:** from `a≥0`, `b<1−τ`: `ε' = a−b−τ > −(1−τ)−τ = −1`. Correct → `P_lo` nonempty,
  sub-instance well-posed. `ε'∈(−1,0)` lands exactly in T(n−2)'s sum-window `(2^{n−2}−1,2^{n−2})`. Clean.
- **h≥4 impossible for T** (`ΣP<2^n`) — correct; only `h∈{0,2}`. For Claim, h≥4 gives `ΣP_lo≤ε ⟹ M≥1−ε`
  — correct. h=0 written for both (`deficit_top=2^{n−2}≥1`).
- **Bases** Claim(1,·),Claim(2,·),T(1),T(2) verified by hand: `S_P⊆S_{G_{ℓ−1}}`+budget forces an equal
  pair / bounded top part, giving the odd-index bound. Sound.
- **No circularity:** Claim(n) uses only Claim(n−2),T(n−2); T(n) uses only Claim(n−2),T(n−2). No
  same-level dependence. Well-founded strong induction on n descending by 2, grounded on P(1),P(2).
- **Negative-ε Claim never invoked** (certified-FALSE direction): 2b-ii always calls T(n−2). Confirmed.
- **Statements verified numerically** (budget enforced, my independent enumeration): Claim & T
  0-violation at n=3 (grid 1/8: 1490+2135 configs), n=4 (545+452), n=5 (2907+1369).

**Scope (why still partial, correctly flagged):** this closes the INC branch ONLY for `R=G_{n−1}`
(`c_R=0`). The full lower bound also needs **G-INC-2** (refined R, `c_R≥1` — no `G_{n−1}`-band structure)
and **G-GAP** (non-containment `S_Q⊄S_R`, `0<b<1`). Both open, honestly documented. Recorded Status
`partial` is correct.

**Certified:** `lemmas/t-ell-mutual-induction.md` (T(ℓ) all ℓ + G-INC-1 all n, with scope note).

---

## 2. geometric-selfsimilar — Status: partial — Verdict: CHANGES REQUESTED — outcome: advanced

**Headline claim (VERIFIED CORRECT):** Lemma R4 closes the m=3 residual gap case; with Case A.A the gap
case is closed for all m≤3, so the **n=2 upper bound is fully rigorous**.

**What I checked (load-bearing = Lemma R4, lines 798–841):**
- XY's one R3 cut of p₁ at offset p₂ gives `F = {p₂,p₂,p₁−p₂,p₃}`; equal pair parity-invisible ⟹
  `A(F)=|p₃−(p₁−p₂)|`. From `p₁≤Σ/2 ⟹ p₁−p₂≤p₃`, so `A(F)=p₃−(p₁−p₂)=Σ−2p₁≥0`. Re-derived, correct.
- Bound: `p₂,p₃<τ/2 ⟹ p₂+p₃<τ ⟹ p₁>Σ−τ=Σ(2^b−1)/D_b`; exact identity `D_b−2(2^b−1)=1` (checked b=1..8)
  ⟹ `A(F)=Σ−2p₁<Σ/D_b` strictly. Sign/direction correct.
- **Independent numeric:** `A(F)=Σ−2p₁` exactly and `A(F)<Σ/D_b` with **0 mismatches / 0 violations over
  60000** exact-Fraction gap configs (b∈{2,3,4}, properly satisfying `Σ/2≤p₂+p₃<τ`, distinct, p₁≤Σ/2).
- Corollary R4.1 (m≤3) and n=2 consequence: every R1/R2/R3 branch ends at base b=0 or a gap case with
  m≤b+1≤3, closed. Correct — the previously by-numeric Regime C at n=2 is now rigorous.

**m≥4 correctly left OPEN (not overclaimed):** the potential `Σ−2p₁≈Σ/2 ≫ Σ/D_b` for near-equal pieces;
builder refuted every simple deterministic strategy (majority violations) and honestly records it as a
dead-end needing lookahead. This is the whole n≥3 upper bound. Recorded Status `partial` is correct.

**Certified:** `lemmas/gap-case-m3-closure.md` (Lemma R4 + Corollary R4.1 + n=2 consequence, with the
m≥4 open-scope note).

---

## 3. ll-dyadic-symdiff — Status: partial — Verdict: CHANGES REQUESTED — outcome: advanced

**Claims (VERIFIED CORRECT, all incremental toward refined-R):**
- **General-R core** — Cases 1/2/Sub-3a of the 3-way split prove `A(Q∪R)≥1` using only `max(R)≤2^{n−1}`
  (⟹ `S_R⊆[0,2^{n−1})`), `A(R)≥1`, and the piece list — no `G_{n−1}`-band structure. I re-read each:
  Case 1 (single top Q-part on `[2^{n−1},μ)`, N_R=0), Case 2 (Lemma P), Sub-3a (fully-odd level). All
  genuinely R-agnostic. Correct.
- **Budget-reduction lemma** — `c_R≥1 ⟹ |Q|=c_Q+1≤(n−c_R)+1≤n`. Trivially correct.
- **Double-REFL for refined R with top piece `2^{n−1}` uncut** — then `R'=R∖{2^{n−1}}` refines `G_{n−2}`
  (max ≤2^{n−2}), so certified REFL/REFL-gen give `A(Q∪R)=2^{n−1}−q₁+A(Q'∪R')`, closing B3a-ref/B3b-ref
  for all n. Correctly scoped.

**Honest residual (correctly OPEN):** `(B2*)-ref` (refined-R alternating-tail crux) and the top-cut
bucket (no reflection anchor). Guardrails respected — the FALSE `max(Q)<2^{n−1}⟹A≥2` is NOT re-imported;
no refined-R SET IDENTITY/top-band analogue assumed; Sub-3b refined not claimed closed. Recorded Status
`partial` is correct.

**Certified:** `lemmas/ll-general-R-core.md` (budget-reduction + R-agnostic core, scope note).

---

## Overall

- Answer `c(n)=2^n/(2^{n+1}−1)` remains conjectured + verified small-n (not fully proven).
- Two real advances closed this round: (a) the LB **anchor** INC branch `R=G_{n−1}` for all n
  (ll-inclusion-gap), (b) the **n=2 upper bound** (geometric-selfsimilar). Neither closes the whole
  problem.
- Remaining load-bearing gaps: LB **G-INC-2** (refined R) + **G-GAP** (non-containment); UB **m≥4 gap
  case** (n≥3). No approach reaches `solved`. All three: CHANGES REQUESTED.
