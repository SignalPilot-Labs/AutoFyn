## Outline review — imo-2026-02, round 10

### Independent re-derivation of the outliner's two key new claims

**(1) Round-9 Case (b) statement was false as stated; true with `sin(A+3β1)<0` restored.**
Own from-scratch numpy sweep (200k random (A,B) triangles, independent seed/code
from the outliner's), computing `X0 = sinB cosA/(2 sin(A+B))`, `β1=arccos(√X0)`,
`Y(γ)`, `G(β1)=2K-f(β1)`:
- Domain-nonempty + `Y(γ)<0` alone (no `sin(A+3β1)<0`): **8218/25123 violations**
  of `G(β1)≥0` — confirms the outliner's finding independently (their ratio
  35519/80555 ≈ 44%, mine 8218/25123 ≈ 33%, same order, same conclusion: FALSE).
- With `sin(A+3β1)<0` also imposed: **0/5700**, then **0/572351** on a 20M-sample
  sweep — confirms TRUE.
- More importantly, I verified *why* this correction is principled, not an ad-hoc
  numeric patch: `sin(A+3β1)<0 ⟺ β1>β0` where `β0=(π-A)/3` is exactly Claim (I)'s
  domain-nonempty threshold, checked exactly (0 mismatches, 200k samples), and
  **100% of the uncorrected violations occur exactly where `β1≤β0`** — i.e. the
  scenario where the target sub-interval `(β0,β1)` that Case (b) is actually
  meant to control is empty (vacuous). The round-9 statement was testing `G` at a
  point (`β1`) outside the geometrically meaningful range in those cases. This
  confirms the fix is the correct non-vacuity condition, not a patch fitted to
  make numerics agree — solid, approve this correction.

**(2) The `P≤0`/`P>0∧E≥0`/`P>0∧E<0` case split.**
Independently re-derived symbolically (own `sympy` session): confirmed
`f=K+P sinβ+Q cosβ` and `G(β)=K+sinA sinB cosβ - P sinβ` exactly (residual 0),
matching the outline's `x,y,P,Q` notation. Confirmed the squared decomposition
`D=expr1²-P²(1-x²) = A_coef x² + B_coef x + C_coef` exactly (residual 0) with
`A_coef=sin²A sin²B+P²`, `B_coef=4sin²A sinB sin(A+B)=2K sinA sinB`,
`C_coef=4sin²A sin²(A+B)-P²=K²-P²` — all match the outline's displayed
coefficients exactly. On a fresh 500k-sample sweep restricted to the corrected
hypothesis space (dom ∧ caseb ∧ `sin(A+3β1)<0`): `B_coef>0` always (14141/14141);
`P≤0` branch was **never hit** in this restricted space across 20M samples (it
occurs in ≈4.5% of *unrestricted* triangles, so the branch is real algebra, just
apparently vacuous once the corrected hypothesis narrows the domain — worth the
builder noting, not a defect); `P>0∧E≥0` (≈95.5% of the restricted space, same
order as the outliner's ≈91% estimate) gives `min G≈0.22>0`; `P>0∧E<0` (the
residual ≈4.5%) gives `min(B_coef²X0-E²)≈0.0029>0` and correspondingly `min
G≈0.0026>0` — confirming the outline's squaring logic (`D=E+B_coef√X0≥0 ⟺
B_coef²X0≥E²` when `E<0,B_coef≥0`) is valid and the target residual quantity
`B_coef²X0-E²` genuinely is a radical-free function of `A,B` alone (no `β1`),
exactly as claimed. The case split is logically sound and exhaustive; no gap
found in the algebra feeding into it.

### Verdict per approach

**`coordinate-bash-resultant-boundary` — revise: APPROVE.**
Sound skeleton, both squaring steps explicitly flagged with their validity
conditions (non-negativity of both sides before squaring), case split verified
exhaustive and independently re-derived above. The one true open target
(`B_coef²X0-E²≥0` on `E<0∧sin(A+3β1)<0`) is a genuine, well-posed, radical-free
degree-6 trig inequality — not a "prove positivity" hand-wave; the outline
correctly names the concrete next levers (Sturm sequence in `tan(B/2)`, or SOS
via `sympy.polys`) rather than asserting it will close. Builder should also
note (per my check above) that the `P≤0` branch may be vacuous in the corrected
domain — still must be proven rigorously per CLAUDE.md (a vacuous branch is
cheap to dispatch: either show `P≤0` is impossible under the hypotheses, or
handle it as stated; either is fine) but this is worth flagging so the builder
doesn't spend disproportionate effort there.

**`coordinate-bash-resultant-boundary-pointwise` — advance: APPROVE.**
The MVT/degeneration architecture is a genuinely different mechanism from the
sibling's algebraic 3-way split (bounding `G(β1)` via `G` decreasing +
`G(β0)>0` + a Lipschitz/MVT bound on `f'`), and is well-posed: it cites already-
certified facts (`(2K-f)'=-f'<0`, `f(β0)>0`) and states the exact next
computation (make `M=sup|f'|` and `G(β0)>0` explicit enough in `A,B` to compare
`M(β1-β0)` against `G(β0)`) rather than leaving "prove it decreases fast enough"
unspecified. The file is honest that this may turn out too lossy to close and
flags that explicitly (not overclaiming). The numeric degeneration pattern
(min G shrinking linearly in `γ-β0`) is a reasonable a priori signal for an MVT
argument being the right shape. No fatal flaw found.

**`ptolemy-trig-identity` — kept live, not built: no action needed.**
Not dispatched this round; correctly identified by the outline as the
population's genuinely independent (non-coordinate) route, worth keeping for
diversity even though it has had no new lever since round 7. Nothing to
approve/reject this round since it isn't in the build set.

### Diversity / shared-gap-plateau flag (for the orchestrator)

This is now round 10, and the field has stood on the *same* shared algebraic
wall (`G_2b`-exclusion / `(Y,B_2,Z)` sign classification, equivalently the
Case-(b) `Y(γ)<0` sub-case above) essentially since round 6-7 — 4-5 rounds
running. This round's outliner did the right due diligence (a dedicated
"fresh-framing-lens" explorer re-checked antipode/power-of-point, spiral
similarity, and isogonal framings and found nothing new), which is legitimate
evidence-gathering rather than a rubber-stamped plateau per the round-2 rule in
memory. But if round 10's two independent new levers (the 3-way case split,
and the MVT/degeneration bound) **both** fail to close the `E<0` / `Y<0`
residual next round, the next outliner should not simply try a third lever on
the identical target — it should be required to seed at least one approach
attacking the problem from a framing genuinely far from coordinate-bash (e.g.
a synthetic/inversive route not yet tried, or a fresh resultant-elimination
setup with a different auxiliary point), per CLAUDE.md's plateau-break
guidance, rather than a fourth variation of the same `G_2b`/Case-(b) wall.

### Registration / ranking

No new slugs to register — the build set reuses two already-registered slugs
under `revise`/`advance` (no fresh cold-start entries this round); `ptolemy-
trig-identity` also already registered. Ranked the whole live field
head-to-head via `update_ranking` (anchored to round 9's actual outcomes, the
last real build results): `coordinate-bash-resultant-boundary` (Elo 1666.2,
`advanced`) and `coordinate-bash-resultant-boundary-pointwise` (Elo 1615.0,
`advanced`) both beat `ptolemy-trig-identity` (Elo 1527.4, `partial`, last
built round 7, no recent lever) — reflecting the coordinate-route pair's
larger, fully independently-verified round-9 closures (`(I)` fully closed;
`(II)` Case-a closed; `W(r_lo)>0` fully closed both cases) versus ptolemy's
stalled four-branch parity gap. Stale flags cleared on all three.

build set: coordinate-bash-resultant-boundary, coordinate-bash-resultant-boundary-pointwise
