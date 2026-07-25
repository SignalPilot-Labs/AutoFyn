# Outline review — round 15 — imo-2026-02

All three candidates are **advance** on already-registered, live slugs (no new
framing proposed this round; the outliner's justification for staying on the
three existing sub-case formulations — 4+ rounds of exhaustive, structurally
confirmed negative search for alternative framings — is consistent with
`current.md`'s history and with CLAUDE.md's own round-10..14 guidance to keep
pushing live sub-case formulations rather than reframe for its own sake).
No new slug registration needed; `copy_approach` not invoked (no branch
request this round).

I independently re-derived and numerically/symbolically re-checked the three
headline claims from raw definitions (own fresh `sympy`/`mpmath` sessions,
50-digit precision where flagged). Findings below.

---

## coordinate-bash-resultant-boundary-pointwise-tangent — APPROVE

**Independent re-verification of Tgt(π/3,π/3).** Rebuilt `X0, β0, K_c, P, Q,
G, RHS(=g), D2(=∂RHS/∂B), T1'` from the raw closed forms in the file and
computed `Tgt(π/3,π/3)` two ways (mpmath 50-dps and sympy exact `nsimplify` +
`N(...,50)`): both give **1.5741362248140625772265137006242409648939164270151**.
This is consistent with the file's `≈1.574` but differs from the file's more
precise citation `1.5741362290964376` at the **9th significant digit**
(Δ≈4.3×10⁻⁹) — too large to be float64 roundoff, small enough not to affect
any conclusion in the outline, but a discrepancy the builder should track
down (likely a stale/rounded number carried from an earlier round) before
citing it as an "exact" value in a final write-up.

**The flagged tight ≈0.0008 margin on 𝒞_hi — re-examined at high precision,
and the characterization in the outline is a numeric artifact, not a real
knife-edge.** I built `Tgt|_{𝒞_hi}(A) := Tgt(A,(π−A)/2)` at 50-dps and swept
the *exact* three-constraint domain membership test (`B>β0(A)`,
`cos²B<X0<cos²β0(A)`) with much finer resolution near the corner than the
explorer's grid. Result: the coarse grid's reported "interior minimum at
A≈1.04696, value≈1.57498, margin≈0.00065–0.0008" is **not** an interior
minimum at all — it is where the coarse grid's domain-membership scan
happened to stop being able to resolve validity near the corner. Refining the
grid, valid points exist arbitrarily close to A=π/3 (e.g. at A≈1.0471974913,
only 6×10⁻⁸ short of the corner), and `Tgt|_{𝒞_hi}(A)` **decreases
monotonically and continuously toward `Tgt(corner)` as A→π/3⁻**, with the
margin shrinking to ≈2×10⁻⁷ at the finest point tested and never going
negative (checked down to that resolution; a 300-point coarse scan over the
whole valid range 0.5575→π/3 also found zero points below the corner value,
confirming the single local max ≈2.2 near A≈0.75–0.8 followed by a single
monotone decreasing branch all the way to the corner, no second interior
extremum). This is the **expected** behavior — the corner (π/3,π/3) is
literally the A→π/3 endpoint of the curve 𝒞_hi (since B=(π−A)/2=π/3 there),
so continuity alone guarantees `Tgt|_{𝒞_hi}→Tgt(corner)` as A→π/3; there was
never a genuine "razor's-edge near-violation" to worry about, only an
under-resolved scan creating the illusion of one.

**Correction for the outline (important for the builder, not a rejection).**
Step 4b should be re-stated: not "compare the two endpoints of the sub-range"
but **"`Tgt|_{𝒞_hi}` has a single interior local max (near A≈0.75–0.8) and is
then strictly monotone decreasing all the way to the corner, so its infimum
on the valid sub-range is exactly `Tgt(corner)`, approached only in the
(excluded) limit."** This is actually an *easier* target than "endpoint
wins over a possible dip below the corner" — it only requires proving
monotone decrease on the single branch `[A_localmax, π/3)`, not ruling out a
separate sub-corner dip. The builder should prove this branch's monotonicity
directly (e.g. via `d(Tgt|_{𝒞_hi})/dA`'s sign on that sub-range), not chase
a fictitious tight numeric margin.

The rest of the outline (no-interior-critical-point step via elimination,
𝒞_lo monotonicity reusing the certified `∂X0/∂B>0`) is a sound, standard
2D-to-1D global-minimum reduction; both remaining sub-targets are honestly
disclosed as numeric-only with concrete, specific mechanisms proposed (not
"then it follows"). No fatal flaw. Verdict: **APPROVE**, with the correction
above folded in as guidance (not a blocking gap — it *removes* risk from the
route rather than adding any).

---

## coordinate-bash-resultant-boundary — APPROVE

Spot-checked the two new degree-6 sign-definite products' closed forms
`(G0·Enum)_00`, `(G0·(−Num))_00` (as given in the explorer report) by dense
random sampling over the reported σ,τ box `(0.156,0.261)×(0.625,0.785)`
(200,000 draws, own sympy `lambdify`): `G0·Enum` stayed strictly positive
(min≈0.0146, consistent with — slightly more conservative than, since a
rectangular box is a superset of the true curved domain — the explorer's
reported true-domain min 0.0277) and `G0·(−Num)` stayed strictly negative
throughout (i.e. `G0·Num>0`), matching the claimed signs exactly. I did not
re-derive `G0, Enum, Num` from the raw geometric primitives from scratch
(too costly in the time budget) — this is a lower rigor bar than a full
independent rebuild, so the builder must still do that full rebuild (as the
proof-reviewer has consistently required of this route in prior rounds)
before certifying a lemma. The claimed grading argument (product of two
`R_10⊕R_01`-graded elements lands in `R_00` automatically) is standard and
low-risk given the population's already-certified round-13 parity theorem.

The remaining content — LP infeasibility with the wider 9-generator set,
r0's structurally harder rank-deficiency — is reported as honest negative
findings (exact rank/LP tests, not numeric fitting), correctly *not*
oversold as progress toward a certificate. The route's central gap (an
actual nonneg-coefficient certificate for either q1 or r0) remains open, but
the skeleton is sound and each new lemma has a stated mechanism. Verdict:
**APPROVE**, with the caveat that a builder must fully re-derive
`G0·Enum, G0·Num` from the raw generator definitions (not just accept the
displayed closed forms) before any lemma is certified.

---

## coordinate-bash-resultant-boundary-pointwise-sos — APPROVE

**n4→n4sq lossless simplification — independently verified as a correct,
elementary, case-free algebraic fact.** `n4 = w³cosB − u(3−u²)` with
`w=√(1+u²)`. On Case (b)'s domain: (i) `B<π/2` unconditionally — because
`B≤C` and `A+B+C=π, A>0` force `B+C<π`, while `B≥π/2∧B≤C` would force
`C≥π/2` too, hence `B+C≥π`, a contradiction (elementary, checked by hand,
correct); (ii) `u∈(0,2−√3)⊂(0,√3)` gives `u>0, 3−u²>0`, so `u(3−u²)>0`.
Hence `n4` is a difference of two nonnegative quantities `w³cosB≥0` and
`u(3−u²)>0`, so (elementary fact: for `X,Y≥0`, `X≥Y ⟺ X²≥Y²`) `n4≥0 ⟺
w⁶cos²B ≥ u²(3−u²)² ⟺ (1+u²)³cos²B − u²(3−u²)² ≥0`, i.e. exactly `n4sq≥0` as
claimed (`w⁶=(w²)³=(1+u²)³` trivially). I verified this chain of reasoning
directly (not just trusted the report) — it is sound and essentially the
"close to a complete 3-line proof" the outline says it is. This is a genuine,
useful simplification: it removes the algebraic-extension bookkeeping for
`n4` entirely, replacing a 4-generator extended-ring ansatz with a 3-generator
plain-ring one.

The rest of the outline (3-generator SDP with conditioning-discrepancy
resolution first, then exact-rational extraction from any numerically
"solved" run) correctly refuses to treat `optimal_inaccurate`/solver-
disagreeing SDP output as decisive, per the population's own round-13/14
scar tissue on this exact failure mode — good discipline, explicitly called
out as a watch-out. No fatal flaw; central `Num≥0` target remains open but
the setup is now cleaner than before. Verdict: **APPROVE**.

---

## Cross-approach diversity note

All three approved approaches share the same deepest structural core (the
branch-selection/positivity gap on Case (b)'s residual domain), as they have
for many rounds — this is the population's already-documented, structurally
confirmed plateau, not new information. This round's work is legitimate
because each of the three found *independent, non-overlapping* leverage on
its own sub-target this round (a global-min reduction for `-tangent`, a new
generator family for `-boundary`, a ring-simplification for `-sos`) — not
because the field has diversified in overall framing. Per CLAUDE.md's own
guidance, the orchestrator should keep watching: if all three plateau again
on their current specific sub-targets (interior-critical-point elimination /
𝒞_hi monotonicity for `-tangent`; an r0 certificate for `-boundary`; the
3-generator SDP conditioning for `-sos`) for another 2-3 rounds without a
concrete mechanism landing, that is the point to dispatch an explorer on a
genuinely different overall framing rather than a fourth variation of the
same positivity core.

## Dead-end / caution reminders (carried forward, still binding)
- Do not retry the 2-generator (`n1,n2`-only) SOS ansatz in any form
  (Theorem 3, unconditional).
- Do not retry `B1,B4,B6`-alone or the 6-generator-without-B3/B5 linear
  ansatz for `-q1` (exact rank-deficient, reconfirmed this round).
- Do not scan `𝒞_hi` (or any boundary curve) without enforcing all three
  domain inequalities simultaneously — confirmed again this round to
  produce spurious sub-corner values.
- Do not trust a single-solver SDP `optimal_inaccurate` result at degree
  ≥30 as decisive for the `-sos` route; cross-check ≥2 solvers and extract
  an exact rational certificate before certifying anything.

build set: coordinate-bash-resultant-boundary-pointwise-tangent, coordinate-bash-resultant-boundary, coordinate-bash-resultant-boundary-pointwise-sos
