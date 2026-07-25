## proof-builder report: coordinate-bash-resultant-boundary-pointwise, round 10

Status: partial (unchanged from round 9; real, honestly-scoped progress this round, gap not closed).

### Task
Dispatched to pursue the MVT/Lipschitz degeneration mechanism (independent of the
sibling `coordinate-bash-resultant-boundary`'s algebraic 3-way case split) to close
the shared G2b-exclusion gap (Theorem 16.2 Case (b), Y(gamma)<0).

### What was found and proved this round

1. **Corrected an unverified claim in the dispatch itself**: "G(β0)>0 already
   established" is FALSE in general (checked, 23% violations on a full random
   sweep) — the certified Theorem B only proves f(β0)>0, a different quantity.
   Restricted to the genuine Case-(b) domain it does hold (0 violations, 3M
   samples) but is not itself symbolically proved.

2. **Fully proved, unconditional, zero-gap MVT reduction chain** (Steps 1-4 in
   the approach file): Lipschitz bound f'(t) ≤ 1+cos B; exact MVT/integration
   bound G(β1) ≥ G(β0) − (1+cos B)(β1−β0); a second exact MVT bound β1−β0 ≤
   (cos β0 − cos β1)/sin β0; combined via a trivial-vs-square split into a
   single **radical-free** target
     (1+cos B)² X0 ≥ RHS²,  RHS := (1+cos B) cos β0 − sin β0 · G(β0)
   (only needed when RHS>0; the RHS≤0 branch is fully closed trivially). This
   requires only ONE squaring, versus the sibling's TWO for its own
   `B_coef²X0 − E² ≥ 0` target — a structurally simpler, genuinely different
   reduction of the same underlying gap.

3. **Extensive numerical testing via global optimization** (differential_evolution
   + many Nelder-Mead restarts, not just random sampling) of this final target:
   global minimum ≈ 1.5e-9 (never negative), attained exactly at the same
   degenerate corner (γ−β0→0) that the sturm-sos-lens explorer independently
   identified as where G(β1)→0 itself — strong structural evidence the MVT
   chain is asymptotically tight where it matters.

4. **Negative finding, ruling out an easier route**: the cruder bound using the
   full domain width (γ−β0) instead of (β1−β0) is FALSE (confirmed violation
   ≈ −0.078 via global optimization, away from the degenerate corner) — the
   finer β1-dependent bound is genuinely necessary.

### What remains open
The final radical-free inequality (1+cos B)²X0 ≥ RHS² is NOT proved symbolically
— attempted sympy simplification stalls on triple-angle (A/3) terms from
β0=(π−A)/3. This is now the concrete open target for this route (a single
squaring, single-radical object — likely more tractable than the sibling's
two-squaring target, but not yet closed).

### Whole-problem status
The shared G2b-exclusion gap is NOT closed by either mechanism this round (this
approach's new (⋆) target, or the sibling's B_coef²X0−E² target). The whole
imo-2026-02 proof therefore remains partial — every other link in the chain
(Claim I, Claim II Case (a), the pointwise root-selection machinery, W(r_lo)>0
both cases) is already certified, but this one shared sub-case is still open.
Status correctly kept `partial`, not `solved`.

### Files touched
- results/imo-2026-02/approaches/coordinate-bash-resultant-boundary-pointwise.md
  (updated in place, Round 10 section + 2 new Promotable lemma entries)
- No new lemma files certified (the round's fully-proved MVT reduction is
  recorded as "Promotable" in the approach file for the reviewer to certify,
  but I did not self-certify into lemmas/ per the builder/reviewer split).
