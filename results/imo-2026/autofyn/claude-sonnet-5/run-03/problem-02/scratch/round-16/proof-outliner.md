# proof-outliner report — round 16 (imo-2026-02)

## What was read
`CLAUDE.md`, `results/imo-2026-02/current.md` (full round-15 adjudication and
history), the three round-16 explorer reports
(`math-explorer-near-corner.md`, `math-explorer-sos-extraction.md`,
`math-explorer-generator-synthetic.md`), and the three live top approach
files (`coordinate-bash-resultant-boundary-pointwise-tangent.md`,
`coordinate-bash-resultant-boundary-pointwise-sos.md`,
`coordinate-bash-resultant-boundary.md`) plus
`ptolemy-trig-identity-synthetic.md`. Sampled the current ranker state
(`mcp__approach-ranker__sample_approaches`, k=10, 13 total approaches on
record) to confirm current Elo/expanded/stale status before deciding the
field.

## Field put up this round

Three approaches advanced with concrete, dispatch-ready skeletons (each
appended as a `### Round 16 outline` section directly in the approach
file, right before its round-15 section — not a full proof, per the file
contract):

1. **`coordinate-bash-resultant-boundary-pointwise-tangent`** (Elo 1699,
   stale — last outcome `advanced`). Skeleton: close the near-corner
   gluing gap via the "quotient sweep" technique —
   `q(ε,t):=(Tgt(π/3-ε,π/3+tε)-Tgt(corner))/ε`, extended continuously to
   `ε=0` (limit already certified `≥δ≈3.5`), certified-interval-swept over
   a generous box `ε∈(0,r₀]` (any `r₀≥5×10⁻⁸` suffices, per the round-15
   quadtree sweep's resolution floor). This avoids the vanishing-target
   degeneracy that defeated the direct 2-D value sweep, and reuses ~90% of
   already-certified machinery (Theorem A's exact `𝒞_lo` parametrization,
   Theorems B/C's derivative-sign-sweep style, New result 9's directional
   derivative). A fallback (explicit Taylor+curvature-bound route) is also
   specified in case the quotient sweep stalls.

2. **`coordinate-bash-resultant-boundary-pointwise-sos`** (Elo 1576,
   stale — last outcome `advanced`). Skeleton with two parallel sub-goals,
   both reusing `/tmp/round-15/sos_work/`:
   - **Sub-goal A** (self-contained, higher near-term value): exact
     rational Gram-matrix extraction at the existing converged witness
     points via round-then-project (eigenvalue/rank diagnostic first, then
     `sympy.nsimplify` rounding + exact linear-algebra correction onto the
     affine constraint subspace + exact PSD re-verification). If
     successful this yields a genuine certifiable pointwise lemma even
     short of the full proof.
   - **Sub-goal B** (larger, could close the whole gap): promote the
     pointwise multipliers `λ₁,λ₂,λ₃,σ₀` to low-degree joint polynomials in
     `(cosB,sinB)` and re-run as one joint SDP, with the ideal-membership
     multiplier `μ·(cosB²+sinB²-1)` built in from the start to avoid a
     known silent-bug class. Start at degree ≤1 (constant λ is expected to
     fail, per round 15's own widely-varying pointwise `t*` values).

3. **`coordinate-bash-resultant-boundary`** (Elo 1701, stale — last
   outcome `partial`, confirmed sign error). Skeleton: **Step 0
   (mandatory)** fix the confirmed round-15 sign error — the true
   sign-definite generator is `(G_0·Num)_00`, not the erroneously-signed
   `B_{G_0N}=(G_0·(-Num))_00`. **Step 1** rerun the full 9-variant
   multiplier LP feasibility sweep (span/rank + nonnegative-coefficient LP
   + phase-1 residual check) with the corrected generator — none of round
   15's 9 LP runs actually used it, so this is a genuinely new search.
   **Step 2** if still infeasible, escalate to a joint Lasserre/Putinar SDP
   (search SOS multipliers directly via Gram-matrix PSD constraints,
   `cvxpy`+SCS/CLARABEL) — the highest-value untried technique per this
   round's explorer, since LP infeasibility with a hand-picked basis never
   rules out a certificate's existence at that degree. **Step 3 (fallback)**
   an explicit ordering/case-split of the residual domain, adapting a
   Schur-domination crux pattern, if Steps 1-2 both stall.

## Decision on `ptolemy-trig-identity-synthetic` (not opened this round)

Read the file and the round-16 `math-explorer-generator-synthetic` report
in full. The report found the auxiliary-circle route is now a proven
structural dead end (K, L trace transcendental, non-conic loci — a fourth
or fifth named-circle attempt would hit the identical wall) but flagged
one untried, genuinely different lever: a direct monotonicity/convexity
comparison of `α(θ)` vs. `β_L(θ)` as functions of the shared parameter
`θ`, working with the implicit equations directly rather than via
resultant-elimination to a sextic.

**Decision: do not dispatch a builder for this today.** Reasoning
recorded in the file (`### Round 16 — outliner decision, not built`):
(a) the population already has substantial framing diversity across five
distinct families (coordinate-bash-resultant-boundary trio,
coordinate-bash-resultant/coordinate-bash, the synthetic-Ptolemy family,
fixed-point/inversion) — no acute collapse risk this specific round; (b)
three independent reformulations of this file's own target gap already
converge on the same `Ψ>0`-type polynomial-positivity wall, suggesting the
difficulty is intrinsic to the gap rather than the framing, so a fourth
reformulation's expected marginal value this round is lower than pushing
the three trio approaches, which all have concrete, un-exhausted,
dispatch-ready next steps identified this round. Flagged explicitly for a
future round: if the trio's three sub-goals above all stall again, this
monotonicity-in-`θ` idea is the recommended next genuinely-different lever
to open, ahead of any further circle-search variant.

## Build set

Exactly the three approaches with skeletons above — no new approach
registered/copied this round (ranker's existing 13-approach population
already covers the live framings; `ptolemy-trig-identity-synthetic`
deliberately not advanced, see above).

**build set: coordinate-bash-resultant-boundary-pointwise-tangent, coordinate-bash-resultant-boundary-pointwise-sos, coordinate-bash-resultant-boundary**
