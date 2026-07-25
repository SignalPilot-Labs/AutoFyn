## imo-2026-02 — outline review, round 9

### Independent verification performed (own sympy sessions, not re-typing the outliner's/explorer's transcripts)

1. **`coordinate-bash-resultant-boundary`'s new offset-sinusoid reformulation** (imported
   from `math-explorer-rem-zero-lens.md`, used as the skeleton's step 4 foundation):
   - Defined `f = 2sin(A+B)(sinβ+sinA) − sinB·sin(A+β)`, `g = sinB·sin(A+β) − 2sin(A+B)(sinβ−sinA)`
     (the raw (I)/(II) forms) and the claimed closed forms `P = sin(A−B)/2+3sin(A+B)/2`,
     `Q=−sinA·sinB`, `K=2sinA·sin(A+B)`, `f_claim = K+P sinβ+Q cosβ`.
   - `sympy.expand_trig` + `simplify`: `f − f_claim = 0` exactly. **Confirmed.**
   - `g − (2K−f) = 0` exactly. **Confirmed** — the claimed identity `g = 2K−f` (so
     (I)∧(II) ⟺ `0<f<2K`) is a genuine algebraic fact, not an approximation.
   - `R²−K² − sin²(2A+B) = 0` exactly (`R²=P²+Q²`), re-derived independently and
     double-checked via a separate `cos(4A)`-double-angle reduction. **Confirmed.**
   - `f(β=B) − (2sinA+sinB)sin(A+B) = 0` exactly. **Confirmed.**
   All four claims that the outline imports as "already re-derived, exact zero-residual"
   are genuinely correct. This is a sound foundation for step 4 of the skeleton.

2. **`coordinate-bash-resultant-boundary-pointwise`'s new `D_N` closed form and
   `G2a(s2*) ∝ Y` claim** (imported from `math-explorer-complex-affine-transfer-lens.md`,
   used in the pointwise skeleton's steps 3–4):
   - Re-derived `D_N(s2) := V3·V4` from first principles (not copied from any file):
     with `N=C/2` (midpoint), `V4=C−N=C/2`, `L=C+s2·R(β)(A−C)=C−s2·R(β)C`,
     `V3=L−N=C/2−s2·R(β)C`, and `R(β)C·C=|C|²cosβ` (standard rotation dot-product
     identity), get `V3·V4 = (|C|²/4)(1−2s2cosβ)`, matching the claimed
     `D_N(s2)=(b²+cc²)/4·(1−2s2cosβ)` exactly (`|C|²=b²+cc²`). **Confirmed
     independently from the raw vector definitions**, not just pattern-matched.
   - Took `G2a` directly from `coordinate-bash-resultant.md`'s own displayed formula
     (line 201: `G2a = 2au³+2au−4bs2²u³−4bs2²u−4bs2u³+4bs2u−2bu³−2bu`), substituted
     `s2*=1/(2cosβ)` (rewritten in terms of `u` via `cosβ=(1−u²)/(1+u²)`), and
     `Y=2a(u²−1)²−b(u²+1)²`: `sympy.cancel(G2a(s2*)/Y)` simplifies exactly to
     `u(u²+1)/(u²−1)²`, matching the claimed prefactor exactly, and it is manifestly
     positive for `u∈(0,1)` (since `β<π/2` throughout the valid range, `u=tan(β/2)<1`).
     **Confirmed independently.**
   Both load-bearing new facts this round's explorer supplied are genuine algebraic
   identities, not numeric fits or wishful pattern-matching — good grounds for the
   outline to treat them as "already closed, import."

### Assessment of the outline

Both dispatched approaches target the whole problem end-to-end (both terminate in
`OM=ON` via the already-proven genericity certificate + the still-open branch-selection
gap) — neither is a sub-lemma fragment, and neither duplicates the other's remaining
proof obligation piece-for-piece: `coordinate-bash-resultant-boundary` targets a
single unified sinusoid bound `0<f(β)<2K` over `β`, while `-pointwise` targets a
pointwise sign product `W(r_lo)=D_K(r_lo)D_N(r_lo)>0` split on `sign(Y)`. These are
genuinely different algebraic routes to the *same* known target (round 8's proven
structural-equivalence theorem establishes closing either — or `fixed-point-concyclic`'s
`Rem=0` — closes all three simultaneously), which is why CLAUDE.md's diversity
requirement is being satisfied at the level of *exhaustive prior negative search*
(rounds 3, 5, 8, and this round's `orthogonal-framing-lens`, which decisively refuted
"branch-independence" as a shortcut and found no new top-level target) rather than by
forcing a fresh top-level framing this round — consistent with round 8's rule that
future "new route" proposals should be treated skeptically absent a demonstrated escape
from the shared branch-selection core. I agree with the outliner's choice not to force
a third framing into the build set this round.

Both approaches correctly import only already-certified lemmas as "closed" (genericity,
`disc(Q)`, magnitude bound, G2a selection, `L1<0` selection) — no circular reasoning, no
step assuming the conclusion. Load-bearing lemmas are stated with mechanisms (product-
to-sum collection for `g=2K−f`; rotation dot-product identity for `D_N`'s closed form;
Vieta-midpoint comparison for `G2a(s2*) ∝ Y`), and I independently re-derived each one
rather than trusting the transcript — all check out.

Case coverage: `coordinate-bash-resultant-boundary`'s WLOG `∠B≤∠C` split is justified by
the existing certified σ-symmetry (swap B↔C); `-pointwise`'s `Y>0`/`Y<0` split is
exhaustive since `Y` is a single real scalar, with the measure-zero `Y=0` case flagged
(acceptable — coincides with an already-excluded genericity boundary). No missing cases.

One outline weakness, not fatal: `coordinate-bash-resultant-boundary`'s skeleton (steps
6–7) still needs the *true* effective-domain endpoints (`γ=min(∠B,∠C)` and the `B2>0`
crossing point `β0(A,B)`) computed exactly — these are flagged as open in the outline
itself ("Open gaps"), so this is honestly scoped as a CHANGES-REQUESTED-shaped task, not
a hidden gap dressed as solved. Similarly `-pointwise`'s `Y<0` case (the harder ~16% of
configuration space) is honestly left as the file's sole remaining hard target, with a
concrete, symbolically-derived (not numeric-fit) target expression `num` to attack. Both
outlines correctly distinguish what's proved (import) from what's still open (the
specific remaining trig-sign claim), satisfying the "distinguish proved from conjectured"
rule.

`fixed-point-concyclic` and `ptolemy-trig-identity` are correctly left dormant (no build
slot) — the former has zero remaining independent algebraic content (round 8, proven),
the latter's easy reduction levers are exhausted absent a new idea (rounds 6-7). Keeping
both alive in the ranked population (not retiring) is correct per standing rules.

No RETHINK-level flaw found in either dispatched approach. Both are APPROVE.

### Verdicts

- **`coordinate-bash-resultant-boundary`**: APPROVE. Sound continuation; step 4's
  central identities independently re-verified exactly; remaining open items (true
  endpoint values, single-crossing application) are correctly scoped as this round's
  work, not hidden gaps.
- **`coordinate-bash-resultant-boundary-pointwise`**: APPROVE. Sound continuation; the
  new `D_N` closed form and `G2a(s2*) ∝ Y` identity independently re-verified exactly
  from raw definitions; `Y>0` case is nearly mechanical (two short `sympy.simplify=0`
  checks away from full closure per the outline), `Y<0` case correctly identified as the
  harder remaining target with a concrete symbolic (not numeric-fit) expression to attack.
- **`fixed-point-concyclic`** (dormant, not built): correctly kept alive, no action needed.
- **`ptolemy-trig-identity`** (dormant, not built): correctly kept alive as the
  population's technique-diverse fallback.

### Ranking

Updated via `update_ranking` (10 comparisons): both live/advancing approaches
(`coordinate-bash-resultant-boundary`, `coordinate-bash-resultant-boundary-pointwise`)
ranked essentially level (drawn against each other, both real continued progress) and
above the dormant/exhausted approaches (`fixed-point-concyclic`, `ptolemy-trig-identity`,
`coordinate-bash-resultant`) and the confirmed dead-end (`inversion-at-A-collinearity`).
No new approaches to register this round (outliner proposed no new/copy slugs).

Resulting order (best-first): `coordinate-bash-resultant-boundary` (1687),
`coordinate-bash-resultant-boundary-pointwise` (1634), `ptolemy-trig-identity` (1552),
`coordinate-bash-resultant` (1516), `fixed-point-concyclic` (1499),
`inversion-at-A-collinearity` (1462), `power-of-point-secants` (1332, unchanged this
round).

build set: coordinate-bash-resultant-boundary, coordinate-bash-resultant-boundary-pointwise
