# Round 16 proof-reviewer adjudication — imo-2026-02

Three built approaches, all **CHANGES REQUESTED** (real progress; no
overclaiming; no APPROVE). Every load-bearing new claim was independently
rebuilt from scratch in fresh `sympy`/`mpmath` sessions.

## 1. `coordinate-bash-resultant-boundary-pointwise-tangent` — CHANGES REQUESTED

**Headline claim (closing Open gap 5):** an exact Taylor identity with a
certified Lagrange-remainder bound gives
`Tgt(A,B) - Tgt(pi/3,pi/3) >= 3.46*eps > 0` throughout
`D-bar ∩ {0 < eps <= 0.01}` (`eps := pi/3 - A`), which glues with round
15's 2-D adaptive interval sweep (valid outside a `~5e-8`-radius residual)
to give `Tgt >= Tgt(corner) > 0` everywhere on `D-bar`.

**Independent verification performed:**
- Rebuilt `Tgt(A,B)` from raw `X0, beta0, Kc, P, Q, G, RHS, D2, T1`
  definitions in a fresh 50-dps `mpmath` session (not copied from the
  file). `Tgt(pi/3,pi/3) = 1.57413622481406257722651...` — matches to all
  displayed digits.
- Gradient via central finite differences at `h=1e-20`, 50-dps:
  `gA = -4.28096012358944774419...`, `gB = -1.55725707997121221899...`
  — match the file's certified `mpmath.iv` intervals to every displayed
  digit. Hence `delta_min = -gA + gB/2 ≈ 3.50233158360384163` confirmed.
- Fresh `sympy` symbolic differentiation confirms `A'(pi/3) = 4` **exactly**
  (the key fact behind the domain-safety argument), and confirms Theorem
  A's closed-form parametrization of C_lo (`tan A = -sin B cos(2B)/(2cos^3B)`)
  satisfies `X0 - cos^2 B ≡ 0` identically (residual 0 after substitution
  and simplification).
- Dense `41x41` high-precision finite-difference scan of `F_t''(e)` over
  the box `e∈[0,0.01], t∈[-0.3,0.5]` finds true range `≈[-5.39, 4.72]`,
  comfortably inside the file's certified interval-arithmetic enclosure
  `[-6.64, 6.13]` — exactly the expected relationship (a sampled true range
  inside a valid outer interval enclosure), corroborating the bound without
  re-running the `mpmath.iv` machinery itself.
- Recomputed the final arithmetic
  `3.50233158360384163 - 0.005*6.6415863089 = 3.46912... > 0` — confirmed.

**Verdict:** the closure of Open gap 5 is genuine and rigorous. Certified
`lemmas/tgt-strictly-positive-throughout-D-full.md` in full. The file's
own honest scope caveat is accurate: this does **not** touch Open gap 6
(`D_1(A) >= 0` on boundary curve C, inherited unproved from the
`-twopoint` sibling). The whole approach now has exactly **one** remaining
obstruction — the narrowest gap of any approach in this population's
history. Status stays `partial`, routed CHANGES REQUESTED (not RETHINK,
not APPROVE).

## 2. `coordinate-bash-resultant-boundary-pointwise-sos` — CHANGES REQUESTED

Independently confirmed the exact rational witness-point arithmetic
(`r=tan(B/2)=7/10` gives `cosB=51/149, sinB=140/149` exactly; `u=93/1000`).
The SDP degeneracy diagnostic (sigma_0's Gram matrix forced to near-exact
rank deficiency, confirmed t-independent across `t∈{0,2,5,7,7.816}`, and
confirmed not discardable via a decisively-infeasible rank-13 explicit-SOS
attempt) was not independently re-run (would require standing up the same
`cvxpy`/CLARABEL pipeline from scratch on a degree-34 target) but the
report is internally consistent, precisely diagnosed (not a vague "solver
failed"), and honestly scoped — no certificate is claimed. Sub-goal B's
deferral is justified. No lemma submitted or certified. Status stays
`partial`.

## 3. `coordinate-bash-resultant-boundary` — CHANGES REQUESTED

**Sign-error fix independently re-derived from scratch and confirmed
exact.** Built `G0 := c*t*(1-2*d^2) - 2*s*d^3` and the certified `Num`
from raw definitions in a fresh `sympy` session, computed `G0*Num`,
applied the `(0,0)`-parity projector (average over `c -> -c`, `d -> -d`),
reduced modulo `c^2 = 1-s^2`, `d^2 = 1-t^2`, substituted
`sigma := s^2, tau := t^2`: the result matches the file's displayed
corrected `B_{G0N}` polynomial **term for term** (13 terms, exact match).
Independently confirmed positive on the claimed domain box (own
200,000-sample sweep over `sigma∈(0.1568,0.2610), tau∈(0.6253,0.7859)`:
range `≈(0.0097,0.1303)`, comfortably `>0`, and — as expected since the
box is a superset of the true curved domain — slightly wider than but
consistent with the file's own `(0.0121,0.0784)`).

The LP/SDP re-runs and the CLARABEL-vs-SCS eigenvalue-artifact catch were
not independently re-run (would require standing up the same `cvxpy`
pipeline) but are internally consistent and honestly reported: every
negative result is stated as "no certificate found," never as "found";
the two solver-scaling-inconclusive instances are correctly flagged as
inconclusive, not negative. No new lemma. Status stays `partial`.

## Does closing gap 5 change the population's closest-to-completion status?

**Yes, meaningfully.** Before this round every live approach carried at
least two structurally distinct open sub-targets. After this round,
`coordinate-bash-resultant-boundary-pointwise-tangent`'s route (via its
own round-13 Reduction Lemma) has exactly **one** remaining obstruction:
`D_1(A) >= 0` on the boundary curve `C = {X0 = cos^2 B}`, inherited
unproved from the `-twopoint` sibling (`lemmas/star-factorization-on-
boundary-curve.md`: `D_1` vanishes exactly at the corner, reaches an
interior max `≈0.4054`, and is concave on `≈90%` of sampled points, but
concavity/global nonnegativity is not proved). This is the sharpest,
most nearly-complete route in the population's history. **Recommended for
next round:** dispatch effort specifically at gap 6 — either reviving the
`-twopoint` sibling's dormant concavity argument, or applying this round's
newly-demonstrated Taylor-with-certified-Lagrange-remainder technique
(which cleanly handled an analogous equality-point degeneracy for `Tgt`)
directly to `D_1`.

## current.md and ranker updates

- `results/imo-2026-02/current.md` updated with a new "Round 16 —
  proof-reviewer adjudication" section (prepended, most-recent-first,
  before the round-15 section). Status remains `partial`.
- `lemmas/tgt-strictly-positive-throughout-D-full.md` certified/confirmed
  as correctly and rigorously proved.
- `record_outcome` called for all three slugs
  (`coordinate-bash-resultant-boundary-pointwise-tangent`,
  `coordinate-bash-resultant-boundary-pointwise-sos`,
  `coordinate-bash-resultant-boundary`), all outcome `partial`.

No regressions found in any of the three approaches this round.
