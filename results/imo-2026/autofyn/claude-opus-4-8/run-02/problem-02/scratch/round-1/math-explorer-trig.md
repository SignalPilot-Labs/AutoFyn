## imo-2026-02 (lens: trigonometric / metric route)

- Distinct openings surfaced in this lens:
  1. **Fixed-line reduction (elementary, proved, no K/L structure needed).** `OM=ON`
     is *by definition* `O ∈ perpendicular bisector ℓ of MN`, and `ℓ` depends only on
     `A,B,C` (not on K, L). Using vectors from `A` as origin (`b=B-A, c=C-A, o=O-A`):
     `OM²-ON² = o·(c-b) + (|b|²-|c|²)/4`. Hence
     **`OM=ON ⟺ vec(AO)·vec(BC) = (AC²-AB²)/4`.**
     Equivalently (via `u·v=(|u|²+|v|²-|u-v|²)/2` and `|AO|=R`, `|OB|=OB` etc.):
     **`OM=ON ⟺ OB² − OC² = (AB² − AC²)/2`.**
     Both forms verified *exactly* (to 1e-12, i.e. floating-point-exact) on a real
     numerically-constructed configuration (see Small-case notes). This is a clean,
     fully rigorous lemma — pure vector algebra, no circle-AKL specifics used — and
     gives the outliner a crisp restated target: locate O (or just the difference
     `OB²-OC²`, or `pow_B(AKL)-pow_C(AKL)` since `OB²-OC² = pow_B - pow_C`) rather
     than chase `OM, ON` directly.
  2. **Power-of-a-point via secants through A.** Since `A` lies on circle(AKL), for
     any point `P` on a line through `A`, `pow_P(AKL) = \overline{PA}\cdot\overline{PA'}`
     where `A'` is the second intersection of that line with circle(AKL). Applied to
     `M` on line `AB` and `N` on line `AC`: `pow_M = AM(AM-t_X)`, `pow_N=AN(AN-t_Y)`,
     where `t_X, t_Y` are the signed chord lengths `AA'` along `AB`, `AC`
     (`t_X = 2·u_{AB}·(O-A)`, i.e. twice the projection of `AO` onto `AB`). This is
     algebraically equivalent to opening 1 (verified numerically to match `powM,powN`
     exactly) but is heavier machinery for the same content — opening 1's forms are
     strictly cleaner and should be preferred as the "restated goal."
  3. **Trig-Ceva / law-of-sines route to pin down triangle AKL.** The three given
     angle equalities (`∠KBA=∠ACL=:θ`, `∠LBK=∠LNC`, `∠LCK=∠BMK`) are the actual input;
     everything above is just restating the *target*. The natural next step (for the
     outliner, not attempted here) is: introduce `θ=∠KBA=∠ACL` as a parameter, use
     law of sines in triangles `ABK` and `ACL` (which share the angle θ at B, C
     respectively) to get `AK, BK` and `AL, CL` in terms of θ and the base angles
     `B=∠ABC, C=∠ACB`; use the remaining two angle conditions (`∠LBK=∠LNC`,
     `∠LCK=∠BMK`, involving the midpoint-triangles `BNC`/`BMC` and points `M,N`) to
     pin the remaining degree of freedom (this is the 2-equations-in-2-unknowns
     step my numerics solved via `fsolve`); then compute `O` (circumcenter of AKL)
     via the standard circumcenter-from-two-angles-and-a-side formula and verify the
     opening-1 identity `OB²-OC²=(AB²-AC²)/2` algebraically. This is where the real
     difficulty of the problem lives — I did NOT carry this out, only confirmed it's
     consistent numerically.

- Candidate technique(s): law of sines / trig Ceva to solve for `AK, AL, BK, CL, ∠KAL`
  in terms of `θ` and the triangle's base angles; then a direct coordinate/vector
  computation of `O`'s power difference (`OB²-OC²`) — i.e. combine **synthetic toolkit
  / power of a point** and **coordinates / trig identities** entries from
  `knowledge_base.md`. Given the messy but pinned-down triangle `AKL`, an explicit
  circumcenter formula (`knowledge_base.md` "Coordinates / complex / barycentric")
  or direct law-of-cosines-in-triangle-OAB / OAC computation is the likely finisher.

- Cheap-kill candidates:
  - **Tangency guess — checked and FALSE, do not pursue.** I tested whether `BK` is
    tangent to circle(AKL) at `K` (and `CL` tangent at `L`), which would have made
    `pow_B = BK²`, `pow_C=CL²` and given an immediate finish. Numerically,
    `OK·BK ≈ -1.21` and `OL·CL ≈ -1.59`, both far from 0 — **not tangent**. This is a
    real dead end to record so no approach wastes a round chasing it.
  - Symmetry/parity checks: none obvious beyond opening 1 (which already IS the
    structural reduction — no further pigeonhole/parity move applies to a continuous
    geometry problem like this).

- Knowledge-base entries to use: **Synthetic toolkit** (power of a point, its
  concyclicity converse, trig cevians/Ceva) — `knowledge_base.md` line ~129-131;
  **Coordinates / complex / barycentric** — line ~137-138; **Trig identities &
  interval intersection** — line ~143-144 (likely relevant once θ is introduced as a
  free parameter and an identity must hold for all θ in a range, matching the
  1-parameter-family structure found numerically).

- Analogous past problems (cruxes): **none** — per
  `crux_moves_documentation.md`, the crux corpus (`past_crux_moves_database.json`)
  has **zero geometry entries** ("Not in the corpus yet"); only number_theory,
  combinatorics, algebra are populated. `past_problems_database.json` does contain
  geometry problem statements+solutions but is not crux-tagged/searchable by
  subtopic for geometry, and a blind read of it was out of scope for this lens's
  time budget. Do not force a match here — flag this gap to the outliner.

- Prior progress: none in `results/imo-2026-02/` (workspace empty this round, per
  `current.md` and empty `approaches/`).

- Dead ends (do not retry):
  - `BK` tangent to circumcircle(AKL) at `K` (and symmetrically `CL` tangent at
    `L`) — numerically refuted, not a valid simplification.

- Small-case / intuition notes (**all labeled conjecture/numerical, not proof**):
  - Built an explicit numerical realization: scalene triangle `A=(0,3), B=(-2,0),
    C=(2.5,0)`. Parametrized `θ=∠KBA=∠ACL` (given condition forces these equal), put
    `K` on the ray from `B` at angle `θ` from `BA` (distance `r_K` free), `L` on the
    ray from `C` at angle `θ` from `CA` (distance `r_L` free); solved the remaining
    two angle conditions (`∠LBK=∠LNC`, `∠LCK=∠BMK`) for `(r_K, r_L)` via
    `scipy.optimize.fsolve`, for `θ = 20°, 30°, 40°, 50°` — all converged with
    positive `r_K, r_L` (plausible for the "K inside triangle BMC" etc. containment,
    though I did not fully verify all containment/angle-betweenness side conditions).
    In every case, computed `O=`circumcenter(A,K,L) and found `OM=ON` to ~1e-12
    (float-precision-exact), **and** the value of `r_K, r_L` genuinely varies with
    `θ` (not a fixed point) — so this is a real 1-parameter family, and `OM=ON`
    holds along the *whole* family, not just at one special configuration. This is
    strong numerical confirmation of the target statement itself (not just of
    lens-specific reductions), on a non-isosceles triangle (rules out a
    symmetry-only artifact).
  - The `OB²-OC²=(AB²-AC²)/2` identity was checked to match `powB-powC` and to
    equal `(AB²-AC²)/2` exactly (`-1.125` both sides) in the `θ=30°` instance —
    confirms opening 1's algebra is the right restatement of the goal.
  - Because the invariance holds across a continuous range of `θ`, a proof that
    only handles "a" configuration (e.g. picks a convenient special θ) is
    insufficient; the eventual argument must be either (a) an identity in θ that
    the trig-Ceva computation resolves symbolically, or (b) a synthetic argument
    that never references θ at all (e.g. some invariant point/circle construction).
    Flag this to the outliner as a reason to prefer synthetic/projective arguments
    over "solve for θ then check" if one can be found — though a full symbolic
    (sympy) verification along the lines of the numeric experiment above is a
    legitimate fallback if synthetic insight doesn't materialize.
