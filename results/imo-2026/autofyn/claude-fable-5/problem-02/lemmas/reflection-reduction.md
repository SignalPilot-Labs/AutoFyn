# Lemma: reflection-reduction (certified, round 1)

**Statement.** In the imo-2026-02 configuration set K\* = 2M − K, L\* = 2N − L. Then:
(a) AKBK\* and ALCL\* are parallelograms; AK\* = BK, AL\* = CL;
(b) ∠K\*AB = ∠L\*AC = φ with K\*, L\* on the non-triangle sides of AB, AC (exterior isogonal rays at A);
(c) ∠AMK\* = ∠BMK = ∠LCK and ∠ANL\* = ∠CNL = ∠LBK;
and, with P₁, P₂ the second meets of lines AK\*, AL\* with ω = ⊙(AKL) and AP₁, AP₂ directed along the rays A→K\*, A→L\*:

OM = ON ⟺ BK·AP₁ + AK² − CL·AP₂ − AL² = (c² − b²)/2.  (I)

**Proof.** Point-reflection dictionary, Apollonius median formula at M and N, parallelogram law for the diagonals KK\*, LL\*, and directed power of the point K\* (resp. L\*) along the secant through A. Full details: `approaches/midpoint-reflection-isogonal.md`, Lemmas 1–4 (directed-length safe; tangent-at-A case included).

**Certification.** sorry-free; re-derived by hand and confirmed numerically to 1e-15 (`/tmp/round-1/review/check_mri.py`) by the proof-reviewer, round 1. Note: only the reduction is certified; deriving (I) synthetically from the transferred hypotheses remains open in that approach.
