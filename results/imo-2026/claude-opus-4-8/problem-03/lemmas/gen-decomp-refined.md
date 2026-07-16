# Lemma Gen-Decomp (generalized top-band decomposition, refined R, no SET IDENTITY)

**Status:** CERTIFIED (proof-reviewer, round 9). Proposed by `ll-inclusion-gap`. Reviewer re-derived the
identity from the merge/integral rep and verified it (with both summands `≥ 0` and the descent
`S_{Q_lo} ⊆ S_{R_lo}`) with 0 failures over budget-valid `n=3,4,5` INC configs. Generalizes the certified
`top-band-decomposition` (which was `R = G_{n−1}`-specific) to any admissible R; uses NO SET IDENTITY.

## Statement
Let `n ≥ 2`, `thr := 2^{n−2}`, `I_{n−1} := [thr, 2^{n−1})`. Let `R, Q` be finite multisets with
`max(R) ≤ 2^{n−1}` and `S_Q ⊆ S_R`. Put `R_hi = {parts ≥ thr}`, `R_lo = {parts < thr}`,
`h_R := |R_hi|`, and likewise `Q_hi, Q_lo, h`. If `h_R` is even then:
(i) `h` is even; (ii) `S_Q ∩ [0,thr) = S_{Q_lo}`, `S_R ∩ [0,thr) = S_{R_lo}`;
(iii) `S_{Q_lo} ⊆ S_{R_lo}`; and
`A(R) − A(Q) = deficit_top + (A(R_lo) − A(Q_lo))`,
with `deficit_top := measure((S_R ∖ S_Q) ∩ I_{n−1}) ≥ 0` and `A(R_lo) − A(Q_lo) ≥ 0`.

## Proof
By the Forcing Lemma (`forcing-inc-reduction`, uses only `max(R) ≤ 2^{n−1}` and `S_Q ⊆ S_R`),
`max(Q) ≤ 2^{n−1}`, so `S_Q, S_R ⊆ [0,2^{n−1})`.
(i) At `x = thr⁻`, `N_R = h_R` even; `S_Q ⊆ S_R` + Parity-Condition Lemma (`parity-condition-inc`) give
`N_Q(thr⁻) = h` even.
(ii) On `[0,thr)`, each `Q_hi`-part `> x`, so `N_Q ≡ N_{Q_lo} (mod 2)` (`h` even) ⟹ `S_Q ∩ [0,thr) =
S_{Q_lo}`; same for `R`.
(iii) Restrict `S_Q ⊆ S_R` to `[0,thr)` and use (ii): `S_{Q_lo} ⊆ S_{R_lo}`; both live in `[0,thr)`, so
`A(R_lo) − A(Q_lo) = measure(S_{R_lo} ∖ S_{Q_lo}) ≥ 0`.
Identity: split `[0,2^{n−1}) = [0,thr) ⊔ I_{n−1}` (no mass above `2^{n−1}`). By (ii),
`A(Q) = A(Q_lo) + δ_top^Q`, `A(R) = A(R_lo) + δ_top^R` with `δ_top^{·} := measure(S_{·} ∩ I_{n−1})`;
`δ_top^R − δ_top^Q = measure((S_R ∖ S_Q) ∩ I_{n−1}) = deficit_top ≥ 0` (since `S_Q ⊆ S_R`). Subtract. ∎

## Scope
The correct refined-R descent engine: it supplies the clean sub-instance `(Q_lo, R_lo)` with
`S_{Q_lo} ⊆ S_{R_lo}` at level `n−2` — the identity ll-inclusion-gap's G-INC-2 needs. It does NOT by
itself close G-INC-2: `ΣQ_lo` is unpinned and the lower-band ↔ top-piece cross-position recursion is not
yet well-founded (open gaps G-INC-2lb / G-INC-2nt).
