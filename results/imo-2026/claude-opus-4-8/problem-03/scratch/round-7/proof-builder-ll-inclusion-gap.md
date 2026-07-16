# Build report — imo-2026-03 / ll-inclusion-gap (Round 7)

Status: **partial** (advanced). File: `results/imo-2026-03/approaches/ll-inclusion-gap.md`.

## What is now rigorous (new this round)

Converted the two-step strong induction `n → n−2` for the crux **G-INC-1** into rigorous prose.

1. **SET IDENTITY + self-similar identity + `A(G_k)` odd ≥ 1** — proved; proposed as new lemma file
   `lemmas/set-identity-selfsimilar.md` (SET IDENTITY = clean 3-line parity argument, N-difference
   exactly 2; verified 0-mismatch n=3..7).
2. **Generalized (ΣQ-free) top-band decomposition** — showed the certified identity
   `A(G_{n−1}) − A(Q) = deficit_top + M` holds for ANY `Q` with `S_Q ⊆ S_{G_{n−1}}` (the certified
   proof never used `ΣQ = 2^n`; the "no mass above `2^{n−1}`" step is automatic from
   `S_Q ⊆ S_{G_{n−1}} ⊆ [0,2^{n−1})`). This is what makes the recursion legal at perturbed sums.
3. **Clean ε-reformulation:** `Claim(n,ε) ⟺ O_Q ≤ O_{G_{n−1}} + ε`. Induction cycles with
   `ε ∈ [0,1)` only; confirmed `ε' = ε+a−b ∈ [0,1)` at every step of 2b-i (never negative).
4. **Two-step induction, all four cases of the step closed** (general n ≥ 3): h≥4, 2a, 2b-i
   (invokes `Claim(n−2,ε')`), 2b-ii (invokes the companion `T(n−2)`). Base cases `Claim(1,·)`,
   `Claim(2,·)`, `T(1)`, `T(2)` proved outright (only equal-pair configs feasible).

**Net result: G-INC-1 (= `Claim(n,0)`) fully PROVEN for n ∈ {1,2,3,4}**, hence
`A(Q∪G_{n−1}) ≥ 1` (INC branch, R=G_{n−1}) for n ≤ 4. For general n, G-INC-1 holds **iff** the single
residual lemma `T(ℓ)` (ℓ ≥ 3) holds.

## Residual gaps (honest)

- **2b-ii / `T(ℓ)`, ℓ ≥ 3** (the sole obstruction to G-INC-1 for all n): `O_P ≤ O_{G_{ℓ−1}}` for INC
  `P`, `|P| ≤ ℓ+1`, `ΣP ∈ (2^ℓ−1, 2^ℓ)`. Verified 0-violation ℓ=2,3,4 (budget enforced). NOT proven
  ℓ ≥ 3. The two-step machinery cannot self-close it (its ε<0 regime would feed `Claim` at negative
  ε, which is FALSE); and the sum window is essential (ε-free `O_P ≤ O_{G_{ℓ−1}}` is false, e.g.
  `P={7/2,7/2,7/2,2}` at ℓ=3 has `O_P=7>5` but `ΣP=12.5∉(7,8)`).
- **G-INC-2 (refined R):** vacuous at n=3 (budget+parity), first nontrivial n=4 (|Q|=3, c_R=1). Open;
  needs `S_R`'s own level structure (the dyadic band decomposition breaks for refined R).
- **G-GAP** (non-containment alignment cost): unchanged from R6, still open.

## Corrections to the outline honored

- The strengthened IH `Claim(n,ε)` is used ONLY for ε ∈ [0,1); the ε<0 direction is never invoked.
- No use of the decertified Structural Lemma; A(Q) bounded by arithmetic on part values only; even-
  multiplicity interior pairs `{s,s}` handled (they force `S=∅` in the base cases).
- The n=3 "INC-parity shortcut" is NOT used as a general proof — instead n=3 is handled uniformly by
  the two-step induction reducing to n=1 (base) + T(1).
- Every numeric check was tiny/bounded (<55s), joint cut budget enforced.
- One outline refinement: the outline's 2b-ii target `A(Q_lo) ≤ deficit_top` is too lossy (discards
  `A(G_{n−3})−1`); the correct, tight reduction is `O_{Q_lo} ≤ O_{G_{n−3}}` (= companion `T(n−2)`),
  which I verified holds where the outline's cruder bound fails.

## Proposed lemma for certification
- `results/imo-2026-03/lemmas/set-identity-selfsimilar.md` (SET IDENTITY + self-similar + A(G_k) odd).

## Spec concerns:
None. Answer c(n)=2^n/(2^{n+1}−1) unchanged; this slug attacks the lower-bound crux only, and its
result (G-INC-1 for n≤4 + conditional reduction to T(ℓ)) is consistent with the pinned answer.
