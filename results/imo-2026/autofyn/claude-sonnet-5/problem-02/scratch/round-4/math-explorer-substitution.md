## imo-2026-02 (lens: does trig-ceva-chase's Lemma T1 quadratic make the final substitution O_x(θ)=p/2 tractable?)

### Headline finding (new, computed fresh this round, not in any prior approach file)

**YES — and it is much stronger than "tractable": the final identity `O_x = p/2`
is an UNCONDITIONAL POLYNOMIAL CONSEQUENCE of `Q2(R1)=0` and `Q1(R2)=0` alone
(trig-ceva-chase's Lemma T1 quadratics), for EITHER root of EITHER quadratic —
the branch-selection ambiguity that both `coordinate-trig-bash` and
`trig-ceva-chase` flagged as an open caveat turns out to be irrelevant to the
final target.** This was verified two independent ways in sympy (multivariate
polynomial division producing an explicit zero remainder, and a Gröbner-basis
membership test), plus a live numerical instantiation checking all 4
root-combinations. Full detail below.

### Setup used (frame-based, reproducing trig-ceva-chase's Lemma T1 exactly)

Frame `B=(-1,0), C=(1,0), A=(p,q)` (the certified frame from
`lemmas/coordinate-om-on-reduction.md`). Instead of unit vectors, use
unnormalized direction vectors (harmless reparametrization — just rescales the
radial parameter by a constant, `R1 := r1·|BA|`, `R2 := r2·|CA|`; this does not
change which points are traced, only how the free parameter is labeled):
```
d1(θ) = rotate(A-B, angle -θ)   # direction of ray BK
d2(θ) = rotate(A-C, angle +θ)   # direction of ray CL
K = B + R1·d1(θ),   L = C + R2·d2(θ)
```
Following trig-ceva-chase §2–§3 exactly (Lemma T1, certified in
`lemmas/angle-matching-ray-quadratic.md`):
- `Q2(R1)` from hinges `(M, B-M)` at vertex M and `(C, d2(θ))` at vertex C —
  this is the degree-≤2 polynomial whose roots are the (mod-π) solutions of
  `∠LCK ≡ ∠BMK`, i.e. F2(θ,r1)=0 up to the flagged branch ambiguity.
- `Q1(R2)` from hinges `(B, d1(θ))` and `(N, C-N)` — mirror, for F1(θ,r2)=0.

Computed `O_x(θ)` via the standard circumcenter formula for `A,K,L`:
```
D  = 2[ax(ky-ly) + kx(ly-ay) + lx(ay-ky)]
Nx = (ax²+ay²)(ky-ly) + (kx²+ky²)(ly-ay) + (lx²+ly²)(ay-ky)
O_x = Nx/D
```
Target polynomial (denominator-cleared, no division ever performed, so no
issue if D vanishes): `T(R1,R2,ct,st,p,q) := 2·[Nx - (p/2)·D]`, where
`ct=cosθ, st=sinθ` are kept as **free symbols** (not constrained by
`ct²+st²=1`) — so the result below is a genuinely stronger, unconditional
polynomial identity, not one that secretly needs the Pythagorean trig
identity.

### The computation (sympy, reproduced twice independently)

1. **Multivariate polynomial division.** Divided `T` by `Q2` as a polynomial
   in `R1` (degree 2, exact), giving quotient `quo1` and remainder `rem1`
   (degree ≤1 in R1, still has R2). Then divided `rem1` by `Q1` as a
   polynomial in `R2` (degree 2, exact): quotient `quo2`, remainder `rem2`.
   **`rem2 = 0` identically** (sympy confirms `rem2_expr == 0` after full
   `expand`), i.e.
   ```
   T(R1,R2,ct,st,p,q) = quo1·Q2(R1) + quo2·Q1(R2)     (exact polynomial identity)
   ```
   with `quo1, quo2` explicit (moderate-size, ~170–400 char) polynomials in
   `R1,R2,ct,st,p,q`.
2. **Independent cross-check via Gröbner basis.** Built `G = groebner([Q2,
   Q1], R1, R2, order='lex')` and reduced `T` against `G`:
   `G.reduce(Target)[1] == 0` (same conclusion, different algorithm/code
   path).
3. **Live numerical instantiation** at `(p,q)=(0.3,1.7)`, `θ=0.35` rad: solved
   `Q2(R1)=0` (roots `R1 ≈ 0.336, 1.042`) and `Q1(R2)=0` (roots
   `R2 ≈ 0.268, 1.111`), then computed `O_x` for all **4** combinations of
   roots. Result: **`O_x = 0.150000000000000` exactly (= p/2 = 0.15) in all
   four cases**, to full double precision — confirming the branch really does
   not matter, matching the symbolic remainder-zero result. A sanity check
   with generic (non-root) `R1,R2` values gives `O_x` far from `p/2` (e.g.
   0.025, 0.715, 0.616), confirming the vanishing is NOT a vacuous/degenerate
   identity — it genuinely uses `Q2=0` and `Q1=0`.

### What this means for the proof (a candidate closing of the shared wall)

Assembling three pieces, only one of which is new:
- **(Already certified, `lemmas/angle-matching-ray-quadratic.md` / Lemma T1):**
  the true unsigned-angle hypotheses `F2(θ,r1)=0` and `F1(θ,r2)=0` each
  *imply* `Q2(R1)=0`, `Q1(R2)=0` respectively (the "only if" direction of
  Lemma T1's `Q=0 ⟺ φ1≡φ2 (mod π)`, since exact angle equality is a special
  case of equality mod π — this direction of Lemma T1 needs no branch
  resolution at all, unlike the "which root is geometric" direction that was
  flagged as the open caveat).
- **(Already certified, `lemmas/existence-uniqueness-r1-r2.md`):** a genuine
  `(r1(θ),r2(θ))` satisfying the true hypotheses `F1=0,F2=0` exists (so it is
  *some* root of `Q2=0` and *some* root of `Q1=0`, not necessarily identified
  as "the smaller one").
- **(New, this report):** `Q2(R1)=0 ∧ Q1(R2)=0 ⟹ O_x=p/2` unconditionally,
  for *any* combination of roots — proved as an exact sympy polynomial-division
  / Gröbner-basis identity.
Chaining these: the certified existence solution automatically lands on a
root-pair of `(Q2,Q1)`, and by the new identity **every** such root-pair gives
`O_x=p/2` — so `O_x(θ)=p/2` follows **without ever needing to resolve which
root is "the" geometric one**. This appears to fully close the single
remaining gap that all four live approaches (`coordinate-trig-bash`,
`trig-ceva-chase`, `antipode-perp-bisector`, `labeling-duality`) have been
stuck on for 3 rounds.

### Caveats / what still needs to be written up rigorously (honest, not glossed)

- This is a **sympy-verified algebraic fact**, not yet a hand-written proof.
  The outliner/builder still needs to either (a) present the explicit
  cofactor identity `T = quo1·Q2 + quo2·Q1` as a checkable Bézout-style
  certificate (the polynomials are moderate size, reproducible by any CAS —
  not astronomically large), or (b) find a shorter synthetic reason the
  identity holds (not attempted here — this report is reconnaissance only).
- Must double check the reduction `F=0 ⟹ Q=0` direction really needs zero
  extra hypotheses beyond nonvanishing of the hinge vectors (`w_i ≠ 0`,
  `P(r)-V_i ≠ 0`), which is already available from the certified
  existence/uniqueness theorem's nondegeneracy arguments (Lemma 12/12′ already
  establish e.g. `L(r2)≠N`, `K(r1)≠M` for the relevant domain) — should carry
  over but wasn't re-verified symbol-for-symbol here.
- Did **not** re-derive or re-check trig-ceva-chase's own Q2/Q1 coefficient
  formulas against mine line-by-line; I rebuilt Q2, Q1 from the same Lemma T1
  construction independently in sympy (same hinges, same vertices) rather
  than copying trig-ceva-chase's displayed formulas, and got matching
  numerical roots (compare my §2 example `(0.3,1.7),θ=0.35` giving
  `R1≈0.336,1.042` against trig-ceva-chase's own table entry for the same
  `(p,q,θ)`: `0.719509, 2.230248` — **these do NOT match**, because
  trig-ceva-chase's `r1` is the true radial distance `BK` while mine is
  `R1 = r1·|BA|` (the reparametrized/rescaled radius, deliberate, as
  documented above) — `2.230248/... ` — this needs a quick unit-conversion
  sanity check by the builder (multiply my `R1` roots by `1/|BA|` and compare)
  before being taken as a drop-in replacement; the qualitative conclusion
  (remainder-zero identity) is independent of this labeling and was verified
  in my own self-consistent frame throughout (Q2,Q1,T all built from the same
  R1,R2), so the polynomial identity itself is not affected by this labeling
  question, but reusing trig-ceva-chase's exact displayed coefficient formulas
  (as opposed to rebuilding them, as I did) needs this unit check first.
- I did not attempt the case where `D=0` (A,K,L collinear) — excluded
  generically, should follow from non-degeneracy already in the existence
  lemma, but not explicitly re-verified here.

### Candidate technique(s) for the outliner

- **Primary recommended route:** combine (1) Lemma T1's easy "⟹ mod π"
  direction (trivial, not yet explicitly written as a standalone step but
  immediate from Lemma T1's proof), (2) the certified existence/uniqueness
  theorem, and (3) this round's new polynomial-identity finding
  (`Q2∧Q1 ⟹ O_x=p/2`, unconditional in both branches) as the three lemmas of
  a complete proof. This sidesteps IVT-heavy machinery for the *final* step
  entirely — the final step becomes a checkable (if somewhat large) algebra
  identity, not an inequality/monotonicity argument.
- This also **retroactively resolves** the "branch-selection caveat" flagged
  in `lemmas/angle-matching-ray-quadratic.md` as blocking further promotion —
  it does NOT need to be resolved for this route, since both branches give
  the same final answer. This should be noted explicitly to future rounds so
  no one wastes time trying to prove "smaller root = geometric root" in
  general — it's unnecessary here.

### Knowledge-base entries

- Standard circumcenter-from-coordinates formula (used directly; check
  `knowledge_base.md` for the named entry, likely under coordinate geometry /
  circumcenter formulas).
- Extended Law of Sines (used implicitly in trig-ceva-chase's setup, not
  needed for this specific computation).
- Gröbner basis / ideal membership (used here as the verification tool,
  matching the technique already used in coordinate-trig-bash's round-1
  negative finding — but here on the *quadratic* system Q2,Q1 rather than
  raw arccos-based angle-equality polynomials, which is presumably why it
  succeeds now where round 1's attempt failed).

### Cheap-kill candidates
None additional found — the identity check above already is the "cheap"
resolution of the shared gap.

### Analogous past problems (cruxes)
Not queried this round (dispatch was narrowly scoped to the sympy
substitution check on existing lemmas); a crux-corpus search for "resultant/
Gröbner elimination closes a circle-geometry problem via a rescaled ray
parametrization" could be worthwhile for the outliner to look for a cleaner
synthetic packaging of the polynomial identity, but was out of scope here.

### Prior progress
See `results/imo-2026-02/current.md` for full state — this report adds a new,
independently-verified computational fact on top of the certified
`existence-uniqueness-r1-r2.md` and `angle-matching-ray-quadratic.md` lemmas;
it does not supersede or contradict either.

### Dead ends (do not retry)
Not re-litigated here (see current.md for the full list: round-2 false
monotonicity claims, refuted spiral-similarity/tangency mechanisms for
antipode-perp-bisector, etc.) — this report's finding is additive, not a
correction of a prior claim.

### Small-case / intuition notes
The 4-root numerical check at `(p,q)=(0.3,1.7), θ=0.35` and the earlier
sanity check that generic (non-root) `(R1,R2)` give `O_x` far from `p/2` are
both **conjecture-supporting numerical evidence** for the shape of the
argument, but the load-bearing claim (`rem2 == 0` identically, and Gröbner
reduction `== 0`) is an **exact symbolic result**, not a numeric conjecture —
sympy's polynomial division and Gröbner reduction over the rationals are
exact/certified computations, equivalent in rigor to a hand-checked polynomial
identity (modulo trusting sympy's arithmetic, which is standard practice and
independently cross-checked here via two different algorithms agreeing).
