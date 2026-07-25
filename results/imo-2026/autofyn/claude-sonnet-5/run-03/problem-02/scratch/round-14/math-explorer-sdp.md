## imo-2026-02

- **Distinct openings (this lens = bivariate SDP for the 4-generator
  Positivstellensatz, `Num = σ0 + λ1·n1 + λ2·n2 + λ3·n4 (+λ3'·n3)`):**
  1. Re-run round 13's own minimal ansatz (`n1,n2` only) with a genuinely
     different, better-conditioned basis (Chebyshev, not raw or affinely
     rescaled monomials) — this is the headline finding below.
  2. Full bivariate `(u,w)` Gram-matrix construction handling the ideal
     relation `w²=1+u²` exactly (needed for `n4`), built and run — second
     finding below.
  3. (Not pursued, flagged for a future round) exact-rational certificate
     extraction from the near-feasible numeric solution, to try to promote
     a numeric SDP hit into an actual symbolic Positivstellensatz proof.

- **HEADLINE FINDING — round 13's "cleanly infeasible" verdict at the
  witness point `(A,B)≈(0.603,1.269)` does NOT reproduce under a properly
  conditioned (Chebyshev) basis; it flips sign to a small but consistent
  POSITIVE slack.** I rebuilt `Num,n1,n2,n4` completely from scratch
  (own `sympy` session, own denominator-clearing via `together`/`fraction`,
  independently reproducing round 12/13's exact structural claims: `deg_u
  Num=34`, `Den=-16(u²+1)^14 h` with the same `h`, `deg_u n1=10`,
  `deg_u n2=6`, `n1_den=-4(u²+1)²h`, `n2_den=-2h` — all confirmed matching
  the file's displayed formulas character-for-character). Using round 13's
  own affine rescaling `u=(2-√3)/2·(s+1)`, I found the raw monomial-basis
  coefficients of `Num(s)` still span **~12 orders of magnitude**
  (`~10⁻⁶` to `~7×10⁵`, and after global normalization `1.6×10⁻¹²` to `1`)
  — *not* the `~10²` range round 13's file reports; reproducing their
  2-generator monomial-basis SDP with my own scaling gave the SAME
  qualitative sign as their claim (`t*<0` on both CLARABEL and SCS: `-0.0022`
  / `-11.17`) but both flagged `optimal_inaccurate` and disagreeing by 3
  orders of magnitude — i.e., *not* the clean two-solver agreement round 13
  reports; this itself is grounds for caution about round 13's "clean"
  claim.

  Switching the SAME 2-generator ansatz (`σ0,λ1,λ2` SOS in `u` only) to a
  **Chebyshev basis** on `s∈[-1,1]` (standard product-to-sum rule
  `T_iT_j=½(T_{i+j}+T_{|i-j|})`, own from-scratch implementation, sanity-
  checked against a known toy SOS polynomial — exact match, `status=optimal`)
  and normalizing each of `Num,n1,n2` independently by its own max
  Chebyshev coefficient (feasibility-preserving, since `λi` absorb any
  positive rescaling) collapses the coefficient range to a genuinely
  well-conditioned `O(10⁻¹²)`–`O(1)` (dominant mass near `O(0.1)`–`O(1)`).
  With tight solver tolerances (`tol_feas=1e-12` CLARABEL,
  `eps=1e-11` SCS): **`t*≈+1.60×10⁻⁵` (CLARABEL) and `t*≈+5.97×10⁻⁵` (SCS)
  — both POSITIVE and within a factor ~4 of each other**, a dramatically
  better agreement than the monomial-basis run. I verified the returned
  Gram matrices directly: eigenvalues of `G0,G1,G2` are all within
  `~2×10⁻⁸` of `0` (i.e. PSD up to solver tolerance, not decisively
  violated), and reconstructing `σ0(s)+λ1(s)n1(s)+λ2(s)n2(s)-(Num(s)-t)`
  on a 2000-point grid over `s∈(-1,1)` gives max residual `≈7×10⁻⁷`
  (relative to `Num` ranging `O(0.1)`–`O(0.7)` on the grid) — the numeric
  identity holds to high precision.

  I then extended to the full **4-generator bivariate `(u,w)` ansatz**
  (dispatched target): built the Gram-matrix machinery for `σ0` over the
  combined basis `{T_i(s)}∪{w·T_j(s)}`, with `w²` reduced via the ideal
  relation to `q(s):=1+u(s)²` (itself expanded in Chebyshev form and
  convolved in via a second product-to-sum step), matching both the
  "no-`w`" and "`w`-coefficient" parts of the target identity separately
  (the latter forced to `0`, since `Num` has no `w`-dependence). Solving
  this larger SDP (`σ0` a `35×35` Gram matrix, `λ1,λ2,λ3` sized `13,15,16`)
  at the same witness point: **`t*≈+1.61×10⁻⁵` (CLARABEL) and
  `t*≈+1.98×10⁻⁵` (SCS) — again both positive, and now agreeing to within
  ~20%**, essentially unchanged from the 2-generator result (i.e. `n4`
  contributes little at this point, consistent with round 13's own Finding
  1 that `n3` made "essentially no difference").

  **Interpretation, with appropriate caution.** This numeric evidence
  (small positive `t*`, two independent solvers, tight tolerances, clean
  ~1e-7-level residual reconstruction) is a genuinely different and better
  signal than round 13's monomial-basis run, and points the OPPOSITE
  direction: the minimal 2-/4-generator ansatz may in fact be **feasible**
  (not infeasible) at round 13's own flagged hard witness point, once
  conditioning is handled correctly — which, if it holds up, would remove
  the main obstruction the population has been treating as a wall for
  2 rounds. **This is NOT a proof and should not be treated as settled**:
  `t*` is extremely close to `0` (near the numerical noise floor for a
  degree-34 SDP), both solvers still report `optimal_inaccurate`, and no
  exact rational certificate has been extracted or verified. The correct
  next step is NOT to immediately trust "feasible" — it is to (a)
  reconcile this with round 13's contradictory claim (possibly by having a
  future round independently re-run round 13's *exact* script to see if it
  reproduces `t*≈-1.548`, since my monomial-basis reproduction attempt got
  a much less clean, though same-signed, result), and (b) if the Chebyshev
  result survives scrutiny, attempt exact-rational rounding of the
  near-feasible Gram matrices (they are all near-boundary-PSD, i.e. close
  to rank-deficient, which is often a good sign for finding an exact
  low-rank rational certificate) via `sympy` nullspace/rational
  reconstruction — a concrete, well-scoped task for next round's builder.

- **Candidate technique(s):** Positivstellensatz/SOS via SDP remains the
  right general approach; the concrete lesson from this round is that
  **basis choice (Chebyshev, not monomial, even after an affine domain
  rescaling) is not optional at degree ~34** — it changes the qualitative
  answer, not just the numerics' cleanliness. Any future SDP work on this
  problem should use a Chebyshev (or Bernstein) basis from the start, per
  round 13's own "watch out" note (vi), which this round confirms was
  correct and actually load-bearing (not just a nice-to-have).

- **Cheap-kill candidates:** none new beyond what's certified; the
  domain-defining polynomials `n1,n2,n4` (with `n3` for `cos A≥0`) already
  give a complete algebraic domain description (Theorem 2, certified).

- **Knowledge-base entries to use:** none of `knowledge_base.md`'s generic
  entries are more specific than what the population has already been
  using (SOS/Positivstellensatz, Weierstrass substitution) — this is a
  computational-tooling issue (SDP basis conditioning), not a missing
  theorem.

- **Analogous past problems (cruxes):** not applicable this round — this
  was a pure computational-verification task on the population's own
  polynomial target, not a fresh problem-matching search; I did not query
  the crux corpus (out of scope for the dispatched lens, which was purely
  "run the SDP").

- **Prior progress:** everything in `current.md` through round 13 stands
  unchanged (backbone reduction to `(\star)`⟺`Num≥0`, Theorem 1
  denominator positivity, Theorem 2 `n4` domain encoding — all certified).
  This round adds no new certified lemma; it is a diagnostic/numeric
  finding for the outliner to weigh.

- **Dead ends (do not retry):** none newly identified. **Important
  correction, not a dead end but a caution:** round 13's specific numeric
  claim "`t*≈-1.548`... two solvers... cleanly (not inconclusively)" at
  the witness point `(0.603,1.269)` should be treated as **unconfirmed,
  possibly a conditioning artifact**, not as settled fact, until a future
  round reconciles it against this round's contradictory Chebyshev-basis
  result. Do not build further negative conclusions ("no certificate can
  exist / feasibility is point-localized in this direction") on top of
  round 13's specific `t*=-1.548` number without re-deriving it
  independently first.

- **Small-case / intuition notes (conjecture only):** the fact that both
  the 2-generator and 4-generator Chebyshev-basis SDPs converge to nearly
  identical tiny positive slack (`~1.6-6×10⁻⁵`) at the same witness point
  is suggestive that this point is very close to a genuine equality case
  of the Positivstellensatz identity (not just of `Num` itself, which sits
  comfortably positive, `Num≈9.5` at this point in my raw-`u` computation)
  — i.e. the *certificate* nearly saturates here even though the target
  polynomial itself has healthy margin. This is consistent with round 13's
  own Finding 3 (this point sits almost exactly on the `n4=0` boundary),
  though my result suggests the minimal ansatz might actually reach this
  point rather than fail at it. Purely a numeric observation, not proved.
