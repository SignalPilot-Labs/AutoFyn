# Build report — imo-2026-02, approach `midpoint-reflection-isogonal`, round 1

## What was done

Executed the bounded brief from the outline review: numeric hunt first, proof
effort only on what survived.

### 1. Candidate hunt (all numeric, machine precision, two unrelated scalene
triangles B=(5,0),C=(1.3,4.1) and B=(6,0),C=(3.4,2.2), two φ each) — ALL REFUTED

Probes: `/tmp/round-1/scratch/builder_mri_probe.py`, `builder_mri_probe2.py`.

- **Γ₁ = circle through K\* tangent to AB at M, Γ₂ = circle through L\* tangent
  to AC at N** (the two candidates named in the outline): no nontrivial
  memberships (L\*, K, L, C, N, P, P₁ all off Γ₁ by O(1); symmetric for Γ₂); not
  orthogonal to ω; radical axis of Γ₁,Γ₂ passes through none of A, O, mid(MN),
  K, L, K\*, L\*; centers not collinear with O; unequal radii. Only trivial
  hits: pow(A,Γ₁)=AM², pow(B,Γ₁)=BM² (forced by tangency at M — content-free).
- **Γ₁ᵇ, Γ₂ᵇ = circles through K, L tangent to AB at M / AC at N** (the direct
  tangent–chord reading of ∠BMK, ∠LNC): all memberships fail, no orthogonality,
  radical axis hits nothing.
- **Spiral maps at A:** K\*↦L\* does not carry B↦C (b·BK ≠ c·CL); AK\*·AP₁ ≠
  AL\*·AP₂; AK\*/AK ≠ AL\*/AL; AP₁ ≠ AP₂; AK\*·AK ≠ AL\*·AL; BK·CL ≠ AK·AL.
- **Second meets K₂, L₂ of lines KM, LN with ω:** no incidences (not L/K, not
  P/Q/P₁/P₂, not collinear with A, K₂L₂ ∦ MN, KL₂ ≠ LK₂ — near-miss ~1e-3, not
  a theorem). **No fixed point** on the families of lines K\*L\* or KL across φ.
- One exact relation found, P₁Q = PP₂ (equal chords), but it is automatic from
  isogonality (∠P₁AQ = ∠PAP₂ = ∠A − φ) — no hypothesis content. Recorded so
  nobody mistakes it for progress.

Per the brief, I did NOT fall back to the trig grind.

### 2. Rigorous progress written into the approach file

`results/imo-2026-02/approaches/midpoint-reflection-isogonal.md` now contains
full proofs (directed-length safe, no configuration hand-waving) of:

- **Lemma 1** (reflection dictionary): AKBK\*, ALCL\* parallelograms; AK\* = BK,
  AL\* = CL; ∠K\*AB = ∠L\*AC = φ with the exact side-of-line statement (K\* on
  the non-C side of AB, L\* on the non-B side of AC — exterior isogonal rays);
  ∠AMK\* = ∠BMK = ∠LCK, ∠ANL\* = ∠CNL = ∠LBK. Includes the K ∉ AB, L ∉ AC
  non-degeneracy proofs.
- **Lemma 2** (Apollonius reduction): OM = ON ⟺ pow(K\*,ω) − KK\*²/2 =
  pow(L\*,ω) − LL\*²/2.
- **Lemma 3** (parallelogram law): KK\*² = 2AK² + 2BK² − c², LL\*² = 2AL² +
  2CL² − b².
- **Lemma 4** (directed power along the isogonal secants), giving the exact
  equivalence **OM = ON ⟺ BK·AP₁ + AK² − CL·AP₂ − AL² = (c²−b²)/2** (identity
  (I)), with AP₁, AP₂ directed — unconditional, tangent case included.

Status set to **partial** (correct, fully proven reduction; the problem itself
not closed).

## Remaining gap (single, load-bearing)

Derive identity (I) from the two transferred angle conditions ∠AMK\* = ∠LCK,
∠ANL\* = ∠LBK. The synthetic carrier is still unidentified; the candidate list
mandated this round is exhausted and refuted. Next-round leads recorded in the
file (directed-angle re-probe; inversion at A — one cheap numeric probe each
before any proof effort). The trig route to (I) exists but duplicates
`secant-trig-identity` — if that sibling closes its identity, this file's
Lemmas 1–4 stand as a certified synthetic preamble / promotable lemma, and this
slug should be pruned or merged, per the outline review.

## Promotable lemma proposed

"Reflection reduction for imo-2026-02" (Lemmas 1–4 as a package) — stated at the
bottom of the approach file for the proof-reviewer to consider certifying into
`results/imo-2026-02/lemmas/`.

## Spec concerns:

(none)
