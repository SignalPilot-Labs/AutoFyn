## imo-2026-02 — lens: GLOBAL minimality of the (π/3,π/3) corner for Tgt

Scope note: this is scouting for `coordinate-bash-resultant-boundary-pointwise-tangent`'s
open gap 5(global part). I did NOT attempt a proof; below are mechanisms + fresh
numerics (own independent Python/numpy/scipy re-derivation of `X0, β0, RHS, D2,
T1', Tgt` from the file's own closed forms, `domain_ok` rebuilt from the file's
own 3-constraint characterization `B>β0(A), B≤C, cos²B<X0<cos²β0(A)`).

### Sanity check (reproduced exactly)
`Tgt(π/3,π/3) = 1.5741362290964376`, `X0=1/4`, `D2=-0.8364305707…`,
`T1'≈1.1e-16≈0` — matches the file's certified New results 6/7/9 to full
float precision.

### Distinct openings (viable mechanisms toward global minimality)

1. **Full boundary-curve reduction (most promising, concrete numeric support).**
   Restrict Tgt to each of the two boundary curves of D and show each restriction
   is minimized exactly at the corner:
   - Curve `𝒞_hi = {B=(π−A)/2}` (the `B=C` edge): scanning A over its *actually
     valid* sub-range (domain_ok forces roughly A∈(0.558,1.0467) for this edge —
     see caveat below), Tgt|_{𝒞_hi} is **not monotone globally** (rises from
     ≈1.96 at A≈0.558 to a local max ≈2.18 around A≈0.8, then decreases toward
     the corner), but its minimum over the whole valid sub-range is
     ≈1.57498 at A≈1.04696 — i.e. **1.57498 > 1.57414 = Tgt(corner)**, consistent
     with (not a counterexample to) global minimality, margin only ≈0.0008 (tight
     — this is the closest numeric approach to a violation found in this
     exploration; worth double-checking with higher precision before building on
     it). Distance in A from the true corner A=π/3≈1.0472 is small (~0.0002).
   - Curve `𝒞_lo = {X0=cos²B}` (the implicit lower edge): scanned A from 0.42 up
     to the corner, Tgt|_{𝒞_lo} **decreases monotonically** toward the corner
     over the whole tested range (2.366 at A=0.42 down to 1.5815 at A≈1.0456,
     approaching 1.57414 at the corner) — no violation, comfortable margin.
   If a symbolic proof can show `d(Tgt|_{𝒞_lo})/dA` has a single sign (or is
   monotone decreasing) toward the corner over the whole curve, and separately
   that `Tgt|_{𝒞_hi}` attains its minimum at the corner end (even though NOT
   monotone throughout — it has an interior local max, so the argument must be
   "endpoint wins," not naive monotonicity, OR split into two monotone pieces),
   that + no-interior-critical-point (opening 2) would fully close global
   minimality. This is a genuinely different, tractable sub-target from what's
   currently open, and reuses the already-certified `∂X0/∂B>0`,
   `𝒞_lo` implicit-curve machinery (New result 8's slope computation) as
   building blocks.

2. **Interior critical-point classification (cheap-kill candidate, done numerically here).**
   Ran `scipy.fsolve` on `∇Tgt=0` from 2000 diverse random starting points across
   a region generously covering D (`A,B∈(0.05,1.4)`). Found only **3 distinct
   critical points** of the raw (domain-unrestricted) `Tgt`:
   `(0.1471,0.4987)` (Tgt≈2×10⁻⁸, essentially a zero of Tgt — consistent with
   the known fact, round 6, that Tgt/Ψ is NOT globally positive off-domain) and
   two coincident points near `(0.647,0.851)` (Tgt≈3.15). **All three tested
   `domain_ok=False`** — none lies inside the true domain D. This is strong
   (numeric-only, not proof) evidence that **Tgt has NO interior critical point
   inside D at all**, meaning any global minimum over the closed domain D must
   occur on the boundary (∂D = 𝒞_lo ∪ 𝒞_hi, meeting only at the two corners
   (π/3,π/3) and (A*,B*)) — reducing the whole 2D global-min question to a
   1D problem on the boundary via opening 1, PLUS ruling out the other corner
   (A*,B*), where Tgt≈2.27 (file's own report) is comfortably above 1.574. If
   this "no interior critical point" claim can be proved symbolically (e.g. via
   a resultant/Gröbner elimination of ∂Tgt/∂A=∂Tgt/∂B=0 combined with the
   domain's own polynomial inequalities — the population has done this style of
   computation repeatedly, e.g. Theorem 11.8, the Q(m) discriminant machinery),
   this is arguably the cleanest path: it converts a genuinely 2-variable
   inequality into two 1-variable ones.

3. **Global optimization sweep (done here) — corner reconfirmed as the sole minimizer.**
   Ran 300 Nelder-Mead restarts (penalized objective enforcing the 3 domain
   constraints, random starts across `A,B∈(0.01,1.3)`) — **every converged run
   landed within 10⁻⁵ of the exact corner (π/3,π/3)**, best found value
   `1.5741362170962678` vs. exact corner value `1.5741362290964376` (agreement
   to 8 significant figures). A separate large random domain scan (3,000,000
   candidate points, 203,424 valid, own from-scratch `domain_ok`) found minimum
   ≈1.588 near the corner, no point below it anywhere. This reconfirms (not
   proves) round 13-14's finding with an independent optimizer/codebase and a
   larger, correctly-domain-restricted sample.

4. **Convexity.** Not pursued/not promising: Tgt is a difference `4(1+cosB)²X0D2²
   −T1'²` of two nontrivial trig-polynomial pieces, no sign of joint convexity
   near the corner (D2² term itself need not be convex), and the domain D is
   itself a curvilinear (non-convex-looking) region. Given the population's
   consistent finding (round 6, round 11) that this whole family of targets
   fails global SOS/PSD certificates off-domain, a convexity argument seems
   unlikely to be the right lever; not recommended as a priority.

### Cheap-kill candidates
- **domain_ok filtering before trusting any boundary-curve numeric claim** —
  confirmed the WARNING in `/tmp/memory/math-explorer.md` rule #4 is directly
  relevant here: a naive scan along `B=(π−A)/2` WITHOUT enforcing
  `X0<cos²β0(A)` gives a spurious value 1.464 < corner (looks like a
  counterexample!) at A=0.42 — but that point fails the third domain
  constraint and is NOT actually in D. Any future symbolic/numeric work on
  this gap MUST enforce all three domain inequalities simultaneously, not just
  `B≤C` and `B>β0(A)`.
- **No interior critical point in D** (opening 2 above) is itself a strong,
  cheap structural pruning fact if provable — would immediately reduce the
  2-variable global-min problem to two 1-variable boundary problems.

### Candidate technique(s)
- Symbolic monotonicity-in-A along each boundary curve (reuse `∂X0/∂B`,
  `D6`/`D7` slope machinery already certified in this file) — most promising
  for closing opening 1 on 𝒞_lo (looks genuinely monotone).
- For 𝒞_hi (`B=C`), NOT globally monotone — a "compare the two endpoints of
  the relevant sub-arc + rule out interior extrema via d/dA=0" argument is
  needed instead (essentially a 1-variable critical-point classification on a
  curve, likely tractable via the same resultant/elimination toolkit the
  population has used throughout — e.g. Weierstrass substitution + `sympy`
  polynomial root-counting).
- For opening 2 (no interior critical point), a Gröbner/resultant
  elimination of the 2×2 system `∂Tgt/∂A=0, ∂Tgt/∂B=0` intersected with the
  domain-inequality polynomials, in the spirit of the population's existing
  Positivstellensatz/resultant machinery (`n1,n2,n4` domain encodings from
  the `-sos` sibling could plausibly be reused/adapted here).

### Knowledge-base entries to use
- No problem-specific KB entry found beyond generic IVT/continuity and
  Weierstrass-substitution techniques already in use by this population;
  `knowledge_base.md`'s general algebraic-elimination and monotonicity
  entries (as already cited by sibling approaches) remain the relevant ones —
  I did not find a new KB entry beyond what's already being used.

### Analogous past problems (cruxes)
- The crux corpus has no geometry-domain entries for this problem (per
  established repo finding since round 1) and this specific gap (global
  minimality of a trig-polynomial target over a curvilinear 2D domain
  bounded by two transcendental curves meeting at a corner) does not map
  cleanly onto a listed subtopic I could productively query — consistent with
  round 1's finding, not re-queried this round since no new angle suggests a
  different subtopic would help. None found.

### Prior progress (unchanged from round 14, reconfirmed here)
- `Tgt(π/3,π/3) = (9/4)D2(π/3,π/3)² ≈ 1.5741` exactly, `D2(π/3,π/3) ≤ -0.8`
  proved via a self-contained rational Taylor+Archimedes bound (New result 7).
- `(π/3,π/3)` is a proved STRICT LOCAL minimum via a tangent-cone/directional-
  derivative argument (New results 8-9), margins ≥3.5 on the directional
  derivative.
- GLOBAL minimality remains open — this round's numerics (independent
  re-derivation, larger/cleaner sweeps) strengthen but do not close it.

### Dead ends (do not retry)
- Do NOT scan the `B=(π-A)/2` boundary curve without also enforcing
  `X0(A,B)<cos²β0(A)` — gives spurious sub-corner values that vanish once the
  full domain membership is enforced (see Cheap-kill candidates above).
- Global SOS/Positivstellensatz certificate for Tgt itself is dead (already
  established population-wide, round 6/11 for the closely related sibling
  target — Tgt/Ψ-family targets are not globally positive off-domain, only a
  domain-restricted argument can work).

### Small-case / intuition notes (all numeric, labeled conjecture)
- **Conjecture, strong numeric support**: Tgt has no critical point inside the
  interior of D (checked via 2000 fsolve restarts, only 3 critical points of
  the unconstrained function found, all outside D).
- **Conjecture, strong numeric support**: Tgt restricted to `𝒞_lo` (the
  implicit `X0=cos²B` curve) is monotonically decreasing in A toward the
  corner over its whole domain-valid range — the cleanest single lever if
  provable.
- **Conjecture, moderate numeric support, TIGHT margin (~0.0008)**: Tgt
  restricted to `𝒞_hi` (`B=C`) attains its minimum at the end nearest the
  corner (not monotone throughout — has an interior local max around A≈0.8);
  the margin between this curve's minimum (≈1.57498 at A≈1.04696) and the
  exact corner value (1.57414) is much tighter than every other numeric
  finding in this population's history on this route — flagged as worth an
  independent, higher-precision (mpmath) re-verification before any round
  invests heavily in a symbolic proof assuming a comfortable margin here.
- Global minimum over the whole 2D domain, from both a 3M-point domain-
  correct random scan and 300 penalized-Nelder-Mead restarts, is attained
  only at (π/3,π/3) to 8 significant figures — no other local minimum found.
