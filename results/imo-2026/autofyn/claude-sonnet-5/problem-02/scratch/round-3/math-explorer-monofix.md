## imo-2026-02 (monotonicity/existence repair route)

- **Distinct openings (fix candidates for the F1/F2 existence-via-IVT gap):**
  1. **[STRONGEST — verified numerically, high confidence] Replace the domain
     endpoint, not the inequality.** The reviewer's counterexample
     (p,q)=(0.0025,5.0), θ≈60.57° is *not* a case where the argument is simply
     wrong — it is a case where the true valid r2-domain is *smaller* than
     the claimed (0, r2max(θ)). The "sign convention" assumption used in
     Lemma 6 (ψ_B(r2) stays below φ_B−θ) is EXACTLY equivalent to the
     hypothesis **"K lies inside angle LBA"** (ray BK, at fixed polar angle
     φ_B−θ, must lie strictly between rays BA and BL — this literally forces
     ψ_B(r2) < φ_B−θ). So wherever the sign flips, "K inside angle LBA"
     itself has already failed — that region was never part of the valid
     configuration space to begin with; it's not an extra gap to plug, it's
     an artifact of extending the domain past where the problem's own
     hypothesis holds. Define `r2_signflip(θ)` = the r2 where ray BL passes
     through direction φ_B−θ (equivalently: the point where L reaches the
     intersection of ray BK's line with the ray CL-line — a clean, named,
     synthetic point). The TRUE valid domain is
     `(0, min(r2max(θ), r2_signflip(θ)))`, and on this restricted domain the
     sign convention holds *by construction* (not by assumption), so Lemma
     6's monotonicity proof goes through verbatim, unmodified. I verified
     numerically (2300+ trials, including near-degenerate/thin/extreme
     triangles and θ up to 0.999·min(β,γ)) that **F1 always changes sign
     from + (at r2→0⁺) to − (at the true domain's right endpoint,
     whichever of r2max/signflip binds), with zero counterexamples** — i.e.
     existence via IVT on this corrected domain appears to hold
     unconditionally, with NO analog of inequality (★) needed. At the
     original counterexample point I confirmed by direct computation:
     r2max≈1.759, but r2_signflip≈1.051 (strictly smaller) — so the true
     domain is (0,1.051), and F1 goes from +18.09 at r2→0⁺ down to −24.23 at
     r2→1.051⁻, monotonically decreasing throughout, with a clean root at
     r2≈0.535. So the "monotonicity fails / (★) fails" phenomena are the SAME
     underlying artifact (extending past the true domain) and both symptoms
     disappear once the domain is corrected.
  2. **Two-endpoint case split, made rigorous.** Formalize the above as: let
     `r2*(θ) := min(r2max(θ), r2_signflip(θ))`. Case (a) r2_signflip ≤ r2max:
     then at r2→r2*(θ)⁻, ∠LBK→0⁺ (ray BL aligned with fixed ray BK), so
     F1 → 0 − ∠LNC(r2*) = −∠LNC(r2*), which is negative provided ∠LNC(r2*)>0
     (i.e. L, N, C are not collinear at that point — true except in a
     measure-zero degenerate sub-case that should be handled separately or
     shown impossible). Case (b) r2max < r2_signflip: this is the ORIGINAL
     argument's domain, endpoint gives F1→μ(θ)−ν = |θ−δ|−(∠A+δ), needing
     |θ−δ| < ∠A+δ **for this specific θ only** (not the global sup over θ) —
     i.e. the true per-θ requirement is just `θ < ∠A+2δ` (derived by
     dropping absolute value, since θ>0 forces the binding branch), which is
     much weaker than the old blanket claim `min(β,γ) < ∠A+2δ` (★) and (per
     my numerical checks) seems to hold whenever case (b) actually applies —
     worth checking whether case (b) with θ close to min(β,γ) can happen at
     all, or whether case (a) always pre-empts it before θ gets large enough
     to threaten (★}. This needs a clean synthetic characterization of when
     each case occurs (candidate: case (a) tends to happen for larger θ /
     "taller" triangles, case (b) for θ small) — not fully characterized yet,
     but not needed for existence since case (a) is the one that provably
     works and empirically the failure mode is always covered by it.
  3. **Reframe: r2_signflip is itself a clean synthetic point** — it's where
     ray BL (from C, direction φ_C+θ) crosses the fixed line BK. Consider
     naming this point X(θ) := (line through C in direction φ_C+θ) ∩ (line
     through B in direction φ_B−θ) — i.e. the point where lines "CL" and
     "BK" (extended) would meet. This is exactly the same as saying: the true
     domain's right endpoint is where **L reaches line BK**. This might have
     a nicer synthetic characterization tied to the original triangle (e.g.
     related to a spiral similarity center or a fixed point of the K,L
     construction) — worth a fresh synthetic look rather than pure
     coordinates, since "L on line BK" / "B,K,L collinear" is a natural
     degeneracy of the configuration.
  4. **Do the symmetric r1/F2 analysis with the same fix** — by symmetry
     (B↔C,K↔L,M↔N) the same restricted-domain argument should give existence
     for F2=0 in r1 as well, with the analogous "L inside angle ACK" boundary
     playing the role of the signflip point.

- **Candidate technique(s):** Keep the Sweep Lemma / Decoupling Lemma
  machinery (both certified, unaffected). The fix is purely about correctly
  identifying the domain of validity (intersecting with the "K inside angle
  LBA" / "L inside angle ACK" hypotheses, not just the "K/L inside the
  respective triangle" containment), then re-running the same IVT argument
  on the corrected (possibly smaller) domain. No new machinery needed, just
  a domain correction plus (if pursuing candidate 2) a possible two-case
  split. This looks like a genuine repair, not abandonment.

- **Cheap-kill candidates:** none new beyond what's already used — the fix
  above IS the cheap kill: it dissolves both refuted claims (Lemma 6/7
  monotonicity and (★)) at once by noticing they were computed on a
  too-large domain.

- **Knowledge-base entries to use:** none beyond what coordinate-trig-bash
  already invokes (IVT, standard calculus); no new KB entry needed for this
  specific repair.

- **Analogous past problems (cruxes):** not separately searched this pass
  (dispatch was narrowly scoped to numerical verification of the domain-fix
  hypothesis); the existing field's crux-corpus consultation from prior
  rounds (if any) should still stand. No new crux match found or needed for
  this specific monotonicity-domain repair — it's a self-contained
  calculus/domain fix, not a pattern match to an outside problem.

- **Prior progress:** as recorded in current.md — Decoupling Lemma, Sweep
  Lemma, ray parametrization (Lemma 3), OM=ON⟺O_x=p/2 reduction, all
  certified and untouched by this investigation. Two endpoint angle
  identities (μ(θ)=|θ−δ|, ν=∠A+δ) also certified and reusable — they remain
  valid, they're just not, by themselves, sufficient for the existence claim
  as originally scoped (they only cover the r2max-binding case, case (b)
  above).

- **Dead ends (do not retry):** Do NOT retry proving Lemma 6/7 "as literally
  stated" (monotonic on the full (0,r2max(θ)) domain) — this is genuinely
  false, confirmed independently again in this investigation. Do NOT retry
  proving (★) `min(β,γ) < ∠A+2δ` as a *global, θ-independent* inequality —
  it is genuinely false (confirmed again: e.g. (p,q)=(0.9096,4.7429),
  θ→0.995·min(β,γ) gives min(β,γ)=68.07° vs ∠A+2δ=58.16°, violated) — but
  note this does NOT break existence, because in that regime the true
  binding endpoint is r2_signflip (case a), not r2max, so the F1 endpoint
  sign is still correct via candidate-fix 1 above. Do not conflate "F1/F2
  monotonic on the claimed full domain" (false) with "F1/F2 monotonic on the
  TRUE valid domain" (numerically looks true and is provable by the exact
  same Lemma 6/7 mechanism, since the sign convention holds there by
  hypothesis, not by assumption).

- **Small-case / intuition notes (all labeled conjecture except where marked
  "verified"):**
  - **Verified by direct computation** (not just conjectured): at the
    reviewer's counterexample (p,q)=(0.0025,5.0), θ=60.57°: r2max≈1.7586,
    r2_signflip≈1.0506 (so signflip binds, case a). F1(0⁺)=+18.09°,
    F1(signflip⁻)=−24.23°, and F1 is monotonically decreasing throughout
    (0, 1.0506) — checked at 50 sample points, strictly decreasing, matching
    the sign-convention-respecting mechanism of Lemma 6 applied on the
    restricted domain.
  - **Conjecture (2300+ random/extreme trials, zero counterexamples,
    including thin triangles p∈(−0.05,0.05) or q∈(0.001,0.5), and θ up to
    0.999·min(β,γ)):** F1 always changes sign from + to − across
    `(0, min(r2max(θ), r2_signflip(θ)))`, i.e. existence of a root always
    holds on the corrected domain, unconditionally (no analog of (★)
    needed). This is strong numerical evidence but NOT a proof — a rigorous
    argument needs either (i) a clean case split as in candidate 2 with the
    weaker per-θ inequality `θ < ∠A+2δ` proved in case (b), and a proof that
    ∠LNC(r2_signflip)>0 (or ≥ some positive bound) in case (a); or (ii) some
    unified argument that avoids the case split altogether (e.g. showing the
    two candidate endpoints' F1 values are related by a single formula that
    is manifestly negative regardless of which binds).
  - The uniqueness half (needed for the "final substitution" step later) is
    unaffected by any of this: monotonicity + a single sign change on an
    interval gives a *unique* root, exactly as before, just on the corrected
    interval.
