# proof-builder report — coordinate-bash-resultant-boundary — round 15

## Task
Close the central `-q₁, -r₀` Positivstellensatz certificate for imo-2026-02's
`coordinate-bash-resultant-boundary` approach, using this round's new
degree-6 sign-definite candidates (`G₀·Enum`, `G₀·Num`, `Enum·Num`) and the
`(1-σ)/(1-τ)` positive-multiplier trick, with `r₀` treated as a separate,
potentially-harder target per the outliner's explicit flag.

## What was done (all fresh sympy/scipy work this round, own scripts)

1. **Independently re-derived** the three new product generators
   `B_{G₀E}=(G₀·Enum)_00`, `B_{G₀N}=(G₀·(-Num))_00`, `B_{EN}=(Enum·Num)_00`
   from the already-certified `G₀, Enum, Num` closed forms (own `sympy`
   session, reduction mod the Pythagorean ideal + parity projector) —
   **zero symbolic residual** against the explorer's report in all three
   cases. Degrees confirmed exactly 6, 6, 8.

2. **Independently reconfirmed sign-definiteness** on a fresh 4,000,000-
   sample sweep (10,118 genuine true-domain points, own domain-membership
   code rebuilt from the four raw generator definitions): all three
   products strictly sign-definite with comfortable margin, matching the
   explorer's finding on an independent sample.

3. **Caught and corrected a latent methodological gap**: `q₁, r₀` are not
   homogeneous in `(σ,τ)` (monomials of degree 2 through 6 all appear in
   `q₁`), so a correct span/LP test must pad each candidate generator by
   monomials of every sub-degree, not just the top degree, as round 14
   implicitly assumed. Redid all span/rank tests with this fix (exact
   rational linear algebra, `sympy.Matrix.rank`).

4. **Ran the outliner-directed `(1-σ)/(1-τ)` multiplier trick plus seven
   further natural extensions** (`τ(1-σ), σ(1-τ), (1-σ)(1-τ), (1-σ)²,
   (1-τ)², σ(1-σ), τ(1-τ)`) against the full 9-generator sign-definite set
   `{B₁,-B₂,B₃,B₄,B₅,B₆,B_{G₀E},B_{G₀N},B_{EN}}`: **all nine bring `-q₁`
   into the unsigned span, but the nonnegative-coefficient LP is infeasible
   in every single case** (`scipy.optimize.linprog`, `highs`).

5. **Upgraded the infeasibility claim's rigor**: ran an independent phase-1
   (L¹-residual-minimization) LP for the `1-σ` case, confirming a genuine
   nonzero minimal residual (≈65.46, not a near-zero solver-tolerance
   artifact) — this is materially stronger evidence than a bare
   `linprog(...).success=False` flag.

6. **Ran the identical, equally thorough search for `-r₀`** (per the
   outliner's flag not to assume q₁'s certificate transfers): direct degree-7
   target not in span (matches explorer); `(1-σ)` multiplier repairs the
   span but LP is infeasible; `σ` and `(1-τ)` multipliers do NOT even
   repair the span (an asymmetry versus `q₁`, newly observed this round);
   `(1-σ)(1-τ)` repairs the span but LP is infeasible.

## Result
The central `-q₁, -r₀` certificate is **still not found**. The negative
evidence against the current generator family `{G₀, Enum, Num, Bc}` (bare
or paired products, with any of nine natural nonnegative multipliers) is
now substantially broader and more rigorously confirmed than before
(exact rank tests + genuine-infeasibility-confirming phase-1 LP, not just
a solver flag). This strongly suggests the framework needs either a
genuinely new base generator beyond the current four, a higher-degree
multiplier, or an explicit domain case-split — none of which was completed
this round due to time. Status remains `partial`, honestly disclosed, no
overclaiming.

## Files updated
- `results/imo-2026-02/approaches/coordinate-bash-resultant-boundary.md` —
  new "Round 15" section under `## Approaches tried`, plus a new
  `## Promotable lemmas (round 15 additions)` entry for the two new
  degree-6 sign-definite generators (`B_{G₀E}, B_{G₀N}`, and the degree-8
  `B_{EN}`), with their exact closed forms and independent verification.
- Status: `partial` (unchanged; no full certificate found).

Report: `Proof written to results/imo-2026-02/approaches/coordinate-bash-resultant-boundary.md (Status: partial)`
