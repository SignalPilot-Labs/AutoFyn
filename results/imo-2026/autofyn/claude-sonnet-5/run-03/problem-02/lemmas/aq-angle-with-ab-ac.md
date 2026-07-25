## Lemma: AQ's directed angle against AB and AC

**Statement.** Let `\triangle ABC` be a triangle and `Q` the fixed point of
`q-as-two-line-intersection.md` (equivalently
`q-as-foot-of-perpendicular-from-circumcenter.md`), so `AQ\parallel BC`.
With directed angles of lines mod `\pi` and `\angle B:=\angle(BA,BC)`,
`\angle C:=\angle(CA,CB)`, then
$$\angle(AQ,AB)=-\angle B\pmod\pi,\qquad \angle(AQ,AC)=-\angle C\pmod\pi.$$

**Proof.** Since `AQ\parallel BC` (already certified), a directed angle of
lines mod `\pi` depends only on line direction, so for any third line
`\ell_3`, `\angle(AQ,\ell_3)=\angle(BC,\ell_3)` (Fact (P)). With
`\ell_3=AB`: line `AB=BA`, so `\angle(AQ,AB)=\angle(BC,AB)=\angle(BC,BA)
=-\angle(BA,BC)=-\angle B` (antisymmetry of directed angles). Similarly with
`\ell_3=AC`: line `AC=CA`, so `\angle(AQ,AC)=\angle(BC,AC)=\angle(BC,CA)
=\angle(CB,CA)=-\angle(CA,CB)=-\angle C`. `\blacksquare`

**Where proved (source).** `results/imo-2026-02/approaches/spiral-
similarity-bootstrap.md`, "Round 21" entry, part (a) — a three-line
chain-rule/antisymmetry computation using only `AQ\parallel BC` and the
elementary fact that a directed angle of lines mod `\pi` depends only on
line direction. Zero gaps, no coordinates or numerics needed.

**Independent verification (proof-reviewer, round 21).** Reconstructed the
whole configuration numerically from scratch (own script, `numpy`,
concrete triangle `A=(0.3,1.1),B=(-1,0),C=(1.3,-0.1)`, own circumcenter
formula and own foot-of-perpendicular computation for `Q`, independent of
the builder's code): `\angle(AQ,AB)` and `-\angle B \bmod \pi` match to 14
significant digits (`0.7457078269005368` vs `0.7457078269005377`);
similarly for `\angle(AQ,AC)` vs `-\angle C\bmod\pi`. The hand proof was
also independently re-derived step by step and confirmed correct — a
straightforward, elementary consequence of `AQ\parallel BC` plus the
antisymmetry/chain rule for directed angles of lines. **Certified.**

**Status.** Certified, gap-free, reusable by any future directed-angle
attempt at the `A,K,L,Q` (or related) concyclicity target on this problem.
Does **not** by itself close any open gap of `spiral-similarity-bootstrap.md`
— see that file's "Open gaps (round 21 update)" for what remains.
