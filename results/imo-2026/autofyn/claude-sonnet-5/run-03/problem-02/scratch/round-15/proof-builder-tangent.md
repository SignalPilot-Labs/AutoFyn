# Round 15 build report — coordinate-bash-resultant-boundary-pointwise-tangent

## Task
Prove GLOBAL minimality of the `(π/3,π/3)` corner for `Tgt` over the true
domain `D` (imo-2026-02), per this round's dispatch (build guidance (a)
interior critical-point elimination, (b) boundary-curve reduction with the
corrected `C_hi` framing from the outline-reviewer).

## Outcome: Status stays `partial`, but with substantial, fully rigorous new progress

**Fully closed this round (rigorous, not numeric sampling):**
- **Theorem A**: an exact closed-form parametrization of the boundary curve
  `C_lo = {X0=cos²B}`: `tan A = -sinB·cos(2B)/(2cos³B)`. Proved via the
  sine-addition identity; verified to recover both known corners of `D`
  exactly/numerically.
- **Theorem B**: `Tgt(A,(π-A)/2) ≥ Tgt(π/3,π/3)` for all `A∈[0.5,π/3)` —
  a superset of the true `C_hi`-valid range — proved via a certified
  directed-rounding interval-arithmetic branch-covering argument (`mpmath.iv`,
  `dps=30`): value-sweep away from the corner (3000 sub-intervals, 0
  failures) + derivative-sign sweep near the corner (4000 sub-intervals, 0
  failures) + MVT/continuity. This resolves the outline-reviewer's flagged
  "tight ≈0.0008 margin" issue completely and rigorously — confirms the
  reviewer's diagnosis that it was a grid-resolution artifact, now replaced
  by an actual gap-free proof, not a finer scan.
- **Theorem C**: the same certified-interval method, using Theorem A's
  parametrization, proves `Tgt(A(B),B) ≥ Tgt(π/3,π/3)` for all `B∈[0.9,π/3)`,
  a superset of the true `C_lo`-valid range.
- Both boundary-curve sub-targets from the dispatch (4a, 4b) are thus now
  **fully and rigorously closed**, not merely numerically supported.

**New structural finding (correction, not invalidation):** direct domain
scanning shows `D` actually has **three** boundary curves, not two — a
third curve `C_mid = {X0=cos²β0(A)}` is active for `A∈(A*,≈0.5579)`,
distinct from `C_hi` (`B=(π-A)/2`, active only for `A≳0.5579→π/3`). This
corrects round 14's "exactly two boundary curves" picture (which was only
ever valid in the corner-adjacent region it was scoped to — nothing
previously proved is invalidated). This finding is disclosed clearly in the
approach file for future rounds' benefit.

**Not closed this round:** the interior-critical-point-elimination step
(dispatch item (a)) was **not completed as a symbolic resultant/Gröbner
elimination** (found to be computationally intractable with the tools/time
available — the full 2-variable `Tgt` expression does not collapse under
`sympy.simplify`, consistent with prior rounds' experience). Instead,
attempted a full 2-D adaptive certified interval-arithmetic sweep (quadtree
refinement to depth 22, side ≈4×10⁻⁹) over a safe superset of `D` (covering
interior + all three boundary pieces at once, sidestepping the need for a
boundary decomposition). Result: **zero** violations found anywhere in `D`
down to sub-10⁻⁷ resolution, **except** in a shrinking neighbourhood of the
corner `(π/3,π/3)` itself (expected, since equality holds exactly there —
an interval method can never resolve a strict inequality arbitrarily close
to a point of equality). This is much stronger evidence than any prior
round's numeric sampling, but is honestly reported as **not a complete
proof**: closing it requires either an explicit quantitative radius for the
already-proved local-minimum theorem (round 14's New result 9, currently
only qualitative "for ε small enough"), or a dedicated quantitative
second-order near-corner argument. Neither was completed this round.

## Also fixed
- Corrected a stale numeric citation: `Tgt(π/3,π/3) = 1.57413622481406257722651370062...`
  (matches the outline-reviewer's independent 50-dps recomputation exactly),
  superseding the imprecise round-13/14 value `1.5741362290964376` (wrong
  from the 9th significant digit). Does not affect any prior proved
  conclusion.

## Files touched
- `results/imo-2026-02/approaches/coordinate-bash-resultant-boundary-pointwise-tangent.md`
  — new "Round 15" section (Theorems A/B/C, the 2-D sweep, net assessment),
  updated Open gap 5, new Round 15 additions in Promotable lemmas.
- `results/imo-2026-02/lemmas/clo-closed-form-parametrization.md` (new,
  certified-ready)
- `results/imo-2026-02/lemmas/tgt-ge-corner-on-both-boundary-curves.md`
  (new, certified-ready)

## Recommendation for next round
The whole route's remaining gap is now extremely narrowly located: a
quantitative-radius bridge between two already-proved results (round 14's
local-minimum theorem and round 15's global boundary/interior sweep) in a
sub-10⁻⁷-radius neighbourhood of the single point `(π/3,π/3)`. The most
promising next step is a quantitative second-order Taylor-remainder bound
near the corner (interval-certified second partial derivatives, giving an
explicit δ), rather than further numeric refinement (which cannot resolve
an equality point) or a full symbolic resultant elimination (found
intractable). Status: `partial`.
