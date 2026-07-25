## imo-2026-02 — route: coordinate-bash-resultant-boundary-pointwise-sos (near-singular-Gram / repeated-root investigation)

### Setup reconstructed exactly
The round-16 SDP is **univariate** at the fixed witness `(cosB,sinB)=(51/149,140/149)`
(`r=tan(B/2)=7/10`): `Num, n1, n2, n4sq` become plain univariate polynomials
in `u` (degrees 34, 10, 6, 6 resp.), affinely rescaled `u=s/10` for
conditioning. The 3-generator ansatz is
`Num(s) − t·[k=0] = σ0(s) + λ1(s)·n1(s) + λ2(s)·n2(s) + λ3(s)·n4sq(s)`,
half-degrees `(17,12,14,14)`, all four pieces represented by PSD Gram
matrices `M0(18×18), M1(13×13), M2(15×15), M3(15×15)`; `σ0(s)=z(s)^T M0
z(s)` with `z(s)=(1,s,…,s^17)`. So "the optimal residual polynomial" is
simply `σ0(s)` itself, reconstructed from `M0`'s antidiagonal sums — no
resultant/elimination needed to get a univariate slice; it already is one.
Reused round-16's saved artifacts directly: `/tmp/round-16/exact_point_data.pkl`
(exact rational `Num,n1,n2,n4sq` coefficients) and
`/tmp/round-16/sdp_numeric_result.pkl` (the converged numeric Gram
matrices `M0..M3`, `t*≈7.815546085608958`).

### Computation actually run (this round)
1. Confirmed `M0`'s eigenvalue spectrum exactly as round 16 reported: 5
   eigenvalues `{-3.6e-7,-2.5e-9,~0,~0,1e-10}`, spectral gap `0.01388` to
   the 6th eigenvalue `0.0139`.
2. Reconstructed `σ0(s)` from `M0` explicitly (`numpy.poly1d`, degree 34)
   and computed **all 34 roots**. Found a genuine near-double real root
   pair: `s = 0.8746635927156995` and `s = 0.8746869522465579`
   (separation `≈2.3×10⁻⁵`), flanked by 4 other real roots (`≈±13.4,
   ±23.2`, all far outside the relevant `s`-range) and 14 complex-conjugate
   pairs (none unusually close to the real axis, closest imaginary part
   `≈0.076`).
3. Scanned `σ0(s)` and its derivative near `s≈0.8747`: `σ0` and `σ0'` are
   **both simultaneously `≈0`** there (`σ0(0.87467)≈-2.7e-9`,
   `σ0'(0.87467)≈-2.6e-4`), and `σ0≥0` on both sides (`0.0146` at `s=0.85`,
   `0.0007` at `s=0.88`) — i.e. a genuine tangency to zero, not a sign
   change, exactly the signature of an SOS polynomial with a forced
   near-double real root.
4. **Key new finding (this round): identified exactly WHERE this root
   comes from.** Solved `n1(s)=0` exactly with `sympy.nroots` (`n1` is an
   exact degree-10 polynomial in `ℚ(√3)[s]`, fully known in closed form)
   and found a real root at `s* = 0.87467526959909686949…` — matching
   `σ0`'s near-double root to 5-6 significant figures, and lying in the
   only place a real root of `n1` sits inside the relevant range
   (`n1`'s other real roots: `-114.3,-25.4,-2.68,3.93,37.3`, all outside
   `s∈(0,2.679)=` the rescaled `u`-domain `(0,2−√3)`). Sign check confirms
   `n1(s)<0` for `s<s*` and `n1(s)>0` for `s>s*`: **`s*` is exactly the
   lower endpoint of the true `u`-domain (`n1≥0`) at this fixed `B`**, and
   the witness point `s0=0.93` sits just inside it (`n1(s0)=0.0667>0`).
5. Verified the algebraic mechanism directly: projected the exact
   monomial-evaluation vector `z(s*)=(1,s*,…,s*^17)` (normalized) onto the
   5-dimensional near-null eigenspace of `M0` — **captures 99.99999999996%
   of its norm** (cosine similarity essentially 1). This is exactly the
   textbook fact that if an SOS polynomial `σ0(s)=z(s)^TMz(s)` vanishes at
   a real point `s*`, PSD-ness of `M` forces `Mz(s*)=0`, i.e. `z(s*)` lies
   in `M`'s null space — confirmed numerically to the solver's own
   precision, not assumed.

### Verdict: real lever, but reframes the finding, doesn't yet remove it
This is **not** an independent mysterious double root of `Num` itself —
`Num(s)` has no real root anywhere near `s≈0.87` (`Num(0.87)≈7.82`, no
sign change nearby; checked a dense scan `s∈[-2,2]`, only sign changes at
`s≈-1.357` and `s≈0.499`, both irrelevant/outside the domain-membership
window). Instead, **the degeneracy is a complementary-slackness
phenomenon exactly at the active domain-boundary constraint `n1=0`**: the
SDP's optimal `σ0` is forced (numerically, to a decisive precision) to
vanish to order 2 at the exact point where the domain generator `n1`
itself vanishes — the edge of the `u`-interval being certified over at
this `B`. This is a much more benign, structurally meaningful
explanation than "unexplained near-singularity": it says the certificate
degeneracy tracks the domain's own geometry, not solver noise or a
fundamental obstruction to feasibility.

**Practical implication (a lever for a future round, not developed
here):** round 16's rank-13 "discard the smallest 5 eigenvalues" attempt
failed decisively (`λ*≈-0.51`) because it discarded the *wrong* combination
of directions — 5 generic small-eigenvalue directions, not specifically
the 1 (or 2, for a double root) direction(s) tied to `z(s*),z'(s*)` at the
*exact algebraic* `s*` (a root of the known degree-10 polynomial `n1`, so
`s*∈` a specific number field, not merely "≈0.8747"). A future attempt
could explicitly build `σ0` to contain the exact factor
`(s−s*)²`-vanishing structure (or work in the quotient by the minimal
polynomial of `s*`) rather than eigen-truncating a numeric Gram matrix —
this is a genuinely different, more targeted construction than what was
tried, and is now backed by an exact algebraic target (`s*` is a concrete
root of a known rational/`ℚ(√3)` polynomial, extractable via `sympy` exact
root isolation / `RootOf`, not merely a float).

### Cheap-kill / sanity notes
- The other three real roots of `σ0`, `M0`'s remaining 3 near-zero
  eigenvalues, and the several near-real complex-conjugate pairs are
  **not yet explained** by this single finding — a genuine double root at
  `s*` only accounts for 2 of the 5 near-null dimensions of `M0`. Do not
  claim the full degeneracy is resolved; only the dominant, cleanest piece
  (the real near-double root) has been pinned down and matched to `n1=0`.
- This finding is **numeric-to-high-precision, not yet an exact symbolic
  proof** that `σ0` (at the true SDP optimum, not the floating-point
  approximate optimum) vanishes to order exactly 2 at `s*` — the true
  optimal `λ_i^*` are only known numerically; no closed form for them was
  derived this round.
- Whether this same "σ0 forced to vanish at the `n1=0` domain edge"
  pattern recurs at *other* witness `(cosB,sinB)` points was not checked
  this round (would need re-running the pointwise SDP at 2-3 more points
  and repeating this root-vs-n1-root comparison) — a natural, cheap
  next check before committing to the "build in the vanishing" fix.

### Candidate technique(s)
Same family as before (Putinar/Lasserre Positivstellensatz on
`{n1≥0,n2≥0,n4sq≥0}`), but now informed by the concrete complementary-
slackness structure found above; exact algebraic root isolation
(`sympy.RootOf` / working in the number field generated by `n1`'s real
root) is the natural tool for turning this into an exact construction.

### Knowledge-base entries
No new entries beyond what the approach file already cites (Positivstellensatz/
SOS machinery, Weierstrass substitution). Consider consulting KB entries on
complementary slackness / active-constraint behavior in SOS relaxations if
present (not checked exhaustively this round — time was spent on the
computation per the dispatch's explicit instruction to "actually run it").

### Analogous past problems (cruxes)
Not queried this round — out of scope per the specific dispatch (compute-only
task on an existing SDP artifact); no crux corpus search performed. Flag
for the outliner: if this becomes a live sub-approach, a corpus search on
subtopic "SOS/Positivstellensatz decomposition, active constraints" could
be worthwhile.

### Prior progress / dead ends
Unchanged from `current.md`'s round-16 record: 3-generator SDP converges
cleanly at exact rational witness points; naive round-and-project and naive
rank-13 truncation both fail (confirmed again not to have been re-tried
differently here). This round's finding is a genuine **refinement**, not a
reversal, of round 16's diagnosis: same phenomenon, now explained.
