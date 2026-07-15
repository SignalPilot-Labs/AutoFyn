## oriented-determinant-elimination

**Verdict:** CHANGES REQUESTED  
**True Status:** partial  
**Builder's recorded Status:** correct (`partial`).

**Scores**
- Correctness: 6/10
- Completeness / rigor: 4/10
- Progress: 8/10

The approach does not prove the problem. Its load-bearing Step 5 is expressly left open: it gives neither the promised explicit expression of the determinant residual in terms of `q-F(delta)` and `q^{-1}-F(beta)` nor any other proof that the residual vanishes. This is not routine cleanup; it is the exact implication on which the coordinate route depends.

I independently re-derived the strongest displayed reduction. With the circle written as
`Y·Y-UY_x-VY_y=0`, its centre is `O=(U/2,V/2)`, while passage through `K,L` gives
`UK_x+VK_y=|K|^2` and `UL_x+VL_y=|L|^2`. Since `M=B/2`, `N=C/2`, expansion gives
`OM^2-ON^2=O·(C-B)+(1-q^2)/4`; hence equality is equivalent to
`O·(C-B)=(q^2-1)/4`. Solving the two circle equations by Cramer's rule reproduces
`2(|K|^2[C-B,L]+|L|^2[K,C-B])=(q^2-1)[K,L]`, with the stated determinant convention. I also independently checked symbolically the compression identity
`2 sin(alpha+t) sin(gamma+alpha+t)-sin t sin(gamma+2alpha+t)=cos gamma-cos t cos(gamma+2alpha+t)`.

However, the approach file only asserts that the ray formulas, sign conditions, scalar incidence equations, and nonvanishing of `[K,L]` were derived; it does not actually include those derivations. Thus these claims cannot be certified from the approach body merely because the builder report says they were established. Even granting those intermediate formulas, the decisive factorization remains absent.

**Precise required change:** write the ray-order/sign derivations and then a complete, line-by-line identity showing that the determinant residual is zero under the two incidence equations, with every cleared denominator proved nonzero. A CAS assertion or a statement that terms pair is insufficient.

**Outcome recorded:** `advanced` — the correct determinant and incidence reductions are genuine progress, but the decisive residual factorization and written derivations remain missing.

## antipode-quarter-turn

**Verdict:** CHANGES REQUESTED  
**True Status:** partial  
**Builder's recorded Status:** correct (`partial`).

**Scores**
- Correctness: 7/10
- Completeness / rigor: 4/10
- Progress: 7/10

The antipode reduction is valid and independently verified. If `X` is the antipode of `A` on the circle centered at `O`, then `X=2O-A`; the dilation of factor `2` about `A` sends `O,M,N` to `X,B,C`, so it sends the two distances `OM,ON` to `XB,XC`. Thus `OM=ON` is exactly equivalent to `XB=XC`. Also, because `AX` is a diameter, Thales' theorem gives `XK perpendicular AK` and `XL perpendicular AL`; in complex coordinates this yields the stated real-part circle equations without division by `lambda` or `mu`.

But the load-bearing quarter-turn telescoping lemma is wholly unproved. The file supplies no ordered equations, no multipliers, and no coefficient-by-coefficient cancellation of `r,s,w,u,v,h`. It merely records the intended endpoint. The builder report itself concedes that elimination reproduces the determinant residual from the first approach rather than an independent telescoping proof. Consequently, nothing in this slug currently derives
`Re(conj(x)(c-b))=(q^2-1)/2`, i.e. `XB=XC`.

As in the first slug, the approach body asserts six positive-parameter ray equations without displaying the branch/interiority proof. Those equations may be useful, but the unsupported assertion cannot count as a complete derivation. The treatment of `lambda=0` and `mu=0` is harmless only because no division by them has yet occurred; it does not fill the missing identity.

**Precise required change:** either exhibit and verify the exact telescoping identity, including where both midpoint scale factors enter, or openly reduce this route to the determinant residual and prove that residual. Without one of those two computations, the endpoint `XB=XC` is unsupported.

**Outcome recorded:** `advanced` — the antipode and Thales reductions are correct milestones, but the cancellation proving `XB=XC` is missing.

## sine-product-antipode

**Verdict:** CHANGES REQUESTED  
**True Status:** partial  
**Builder's recorded Status:** correct (`partial`).

**Scores**
- Correctness: 6/10
- Completeness / rigor: 3/10
- Progress: 5/10

The same antipode reduction `OM=ON iff XB=XC` is valid. Beyond that reduction, the advertised route is not established. The approach file never states the exact four sine-rule equations or their product, never derives the required directed angles, and never supplies the promised factor accounting. Therefore the claim that all non-midpoint factors cancel and leave
`(2BM/AB)(AC/2CN)=1` has no proof.

This omission is especially serious because the builder's own independent expansion found that the direct four-triangle product automatically cancels only `XK` and `XL`; it does **not** automatically produce or cancel `BK,BL,CK,CL`, and an additional residual angular identity remains. Thus the outline's proposed terminal cancellation cannot be accepted as a synthetic leap. Degenerate cases in which one of the four auxiliary triangles is collinear or a cosine/sine factor vanishes are also not handled, so quotient manipulations would require separate justification even after the generic identity is found.

**Precise required change:** state the exact directed sine-rule product for `XB/XC`, derive every angle and denominator from the hypotheses, and prove the remaining residual identity, with separate treatment of all zero-factor cases. If an unavoidable extra factor remains, the advertised sine-product mechanism should be abandoned rather than relabeled as cancellation.

This merits `partial`, rather than `unsolved`, because the exact antipode equivalence is a correct nontrivial reduction of the original claim. The sine-product mechanism itself, however, has not yet delivered additional certified progress.

**Outcome recorded:** `partial` — the antipode reduction survives, but the promised sine-product cancellation is neither displayed nor supported by the direct factor accounting.

## Promotable lemmas

No builder flagged a promotable lemma in any of the three approach files. No lemma is certified into `results/imo-2026-02/lemmas/` this round. The antipode equivalence is correct, but it was not submitted as a promotable lemma artifact and is already recorded in `current.md` as certified progress.

## Goal Progress:

Raw current status: `partial`.

Raw ranking after this review's `record_outcome` calls (Elo is still the pre-outcome Elo and all three reviewed entries are stale pending the next outline-reviewer update):
1. `oriented-determinant-elimination` — Elo `1516.0`; expanded `1`; stale `true`; last outcome `advanced`.
2. `antipode-quarter-turn` — Elo `1500.736306793522`; expanded `1`; stale `true`; last outcome `advanced`.
3. `sine-product-antipode` — Elo `1500.0338330211207`; expanded `1`; stale `true`; last outcome `partial`.
4. `inverted-circle-intercepts` — Elo `1483.2298601853572`; expanded `0`; stale `false`; no outcome.

Per-built-slug verdicts:
- `oriented-determinant-elimination`: CHANGES REQUESTED, Status `partial`.
- `antipode-quarter-turn`: CHANGES REQUESTED, Status `partial`.
- `sine-product-antipode`: CHANGES REQUESTED, Status `partial`.

The reviewer-owned `results/imo-2026-02/current.md` has been created with Status `partial` and the strongest certified antipode and determinant reductions. No `## Full proof` is included because no approach proves the target equality.
