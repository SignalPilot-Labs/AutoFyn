# Round 16 report — approach `coordinate-bash-resultant-boundary-pointwise-sos`

## Status: partial (unchanged)

## Summary

Two sub-goals dispatched: (A) exact rational Gram-matrix extraction at the
existing hard witness point, (B) promote pointwise multipliers to a joint
bivariate ansatz. Per the outline's priority, focused on (A); (B) was
deferred honestly (see below) once (A) surfaced a real obstruction worth
understanding before building the (much larger) joint SDP on top of it.

## Sub-goal A: what was done

1. **Fixed a latent problem with the round-15 plan itself**: the dispatched
   witness point `(A,B)≈(0.603,1.269)` is a decimal float, hence
   transcendental — "exact Gram-matrix extraction" there is not well-posed
   (no finite-degree number field to certify positivity in). Replaced it
   with a genuine algebraic witness point: `(u,\cos B,\sin B) =
   (93/1000,\ 51/149,\ 140/149)` — `\cos B,\sin B` from the rational
   `\tan(B/2)=7/10` parametrization of the unit circle (the same technique
   round 14's Theorem 3 already used for a different purpose), `u` found by
   scanning small-denominator rationals near `\tan(0.603/6)` for genuine
   Case-(b) domain membership. Verified exactly (`sympy.Rational`
   substitution into the certified Theorem 1/4 polynomials):
   `n_1=0.0667,\ n_2=0.5834,\ n4sq=0.0428,\ \mathrm{Num}=8.560`, all
   strictly positive, all exact rationals.
2. Re-ran round 15's 3-generator (half-degrees 17,12,14,14) SDP at this
   exact point: converges cleanly, `t^*\approx7.8155`, matching round 15's
   float-point result closely — confirms the numeric finding is not a
   float-precision artifact.
3. Attempted the outline's round-then-project method (round Gram entries to
   rationals, compute exact defect against the now-exact target, solve the
   linear correction, verify PSD exactly). **This failed**, and the failure
   was tracked down to a genuine, precisely-characterized cause rather than
   left as "didn't work":
   - `\sigma_0`'s optimal Gram matrix has 4–5 of 18 eigenvalues at
     `\lesssim10^{-7}` (spectral gap `\approx0.0139` to the rest) — forced
     near-exact rank deficiency.
   - Confirmed **independent of the slack `t`**: re-optimizing the joint
     minimum-eigenvalue margin across all four Gram matrices at
     `t\in\{0,2,5,7,7.816\}` (sacrificing up to the *entire* slack) gives
     margin `\approx-2\times10^{-8}$ every time — pinned at the boundary
     regardless of how much `t` is given up. This rules out "just maximizing
     `t` pushed it to the boundary" as the explanation.
   - Confirmed **not discardable**: built `\sigma_0` explicitly as a
     rank-13 `Q^TQ` (exact rational, automatically PSD by construction, no
     verification needed), fed the resulting exact residual target to a
     fresh SDP over `\lambda_1,\lambda_2,\lambda_3` alone — **decisively
     infeasible** (`\lambda^*\approx-0.51`, not marginal). The near-zero
     eigenvalues of `\sigma_0`, though individually tiny, are load-bearing
     for the polynomial's shape.
4. **No exact rational certificate obtained.** This is reported as an open
   gap, not claimed as solved (per CLAUDE.md's rigor rules).

## Sub-goal B: deferred, not attempted

Building the joint (`\lambda_i` as bivariate polynomials in `\cos B,\sin B`)
SDP is a much larger undertaking, and the degeneracy found in (A) would
plausibly recur (or worsen) there too — promoting `\lambda_i` to
polynomials doesn't obviously relieve a real-double-root-forced null
direction. Attempting it before understanding (A)'s obstruction risked
wasted effort. Recommended next step (not taken): use `sympy.resultant` /
`discriminant` to test whether the optimal residual polynomial
`\mathrm{Num}-t^*-\sum\lambda_i^*n_i` has a genuine repeated real root in
`u` at the witness point — this would upgrade the degeneracy from strong
numerical evidence to a proved fact and tell us exactly what any exact
certificate (pointwise or joint) must vanish at.

## Files touched

- `/home/agentuser/repo/results/imo-2026-02/approaches/coordinate-bash-resultant-boundary-pointwise-sos.md`
  — added a "Round 16 (this round)" section (replacing/preceding the
  round-16 outline block, which is kept below for the record) and updated
  the "Open gaps" section. Status remains `partial`.
- No new file in `results/imo-2026-02/lemmas/` this round — no new
  certified theorem resulted (the degeneracy finding is strong numerical
  evidence, not yet an exact symbolic proof, so it isn't lemma-certifiable
  as stated).
- Scratch work (not part of the repo): `/tmp/round-16/*.py`, `.pkl` — exact
  witness-point construction, SDP re-solves, rank-reduction experiment.

## Honest bottom line

The central gap (`Num≥0` on Case (b)'s domain) is still open. This round's
value is diagnostic: it (1) fixes a real methodological flaw in the
round-15 plan (float witness points aren't exact-certifiable), (2)
reproduces round 15's numeric result at a genuine algebraic point, and (3)
identifies and precisely characterizes *why* naive exact extraction fails
here — a `t`-independent, non-discardable near-boundary degeneracy of
`\sigma_0` — which is new, useful structure for whichever round attempts
exact extraction next, but is not itself a certificate or a proof.
