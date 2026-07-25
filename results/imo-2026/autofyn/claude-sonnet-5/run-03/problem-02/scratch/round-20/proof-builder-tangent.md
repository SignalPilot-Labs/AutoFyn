## imo-2026-02 — coordinate-bash-resultant-boundary-pointwise-tangent (round 20)

## Status: partial (unchanged at the top level, but with genuine new certified content)

### What was closed this round
Fully closed `T:=B_c^2X_0-E^2\ge0` (equivalently `G(\beta_1)\ge0`) on Case
(b)'s own exact residual sub-case `\mathcal D_b=\{0<A\le\pi/2,0<B\le C,
B>\beta_0(A),\cos^2B<X_0<\cos^2\beta_0(A),P>0,E<0\}`, using exactly the
dispatched technique:

1. **Exact corner-vanishing proof, `T(A^\ast,B^\ast)=0`** — by hand, via the
   `u=A/3+\pi/6` substitution and the already-certified `\sin^2u^\ast=3/8,
   \cos^2u^\ast=5/8` (reusing `lemmas/d1-nonnegative-on-boundary-curve.md`'s
   corner facts). Verified to 80 digits independently.
2. **Exact tangent-cone geometry** — the two boundary curves at the corner
   have exact slopes `2/9` (lower, `\mathcal C_{\mathrm{lo}}:X_0=\cos^2B`)
   and `3` (upper, `X_0=\cos^2\beta_0(A)`); both confirmed via `sympy`
   implicit differentiation and independently via high-precision secant
   convergence. Exact gradient of `T` at the corner:
   `\partial T/\partial A=14375\sqrt{15}/32768`,
   `\partial T/\partial B=5625\sqrt{15}/32768`. Domain is one-sided
   (`A>A^\ast` only).
3. **Near-corner closure (`\varepsilon_0=0.01`)** — certified `mpmath.iv`
   domain-safety bound (true `t`-range `\subset(0.2024,3.121)`) and Hessian
   bound (`|F_t''|\le35.67` over the relevant box), combined via Taylor's
   theorem with Lagrange remainder to give `T\ge1.6553\varepsilon>0` for
   `\varepsilon=A-A^\ast\in(0,0.01]`. This is the same style of argument
   that closed `D_1` (rounds 17-18) and `Tgt` (round 16) at this exact
   corner, adapted to the LINEAR (not quadratic) vanishing this round's
   explorer/outline-reviewer identified.
4. **Away-from-corner closure** — a certified `mpmath.iv` adaptive-quadtree
   sweep (branch-and-bound, directed rounding) with **0 unresolved boxes**
   across `A\in[A^\ast+0.005,\pi/2]` (352+150+206 boxes total, several
   ranges), including correctly resolving a second domain-shape pinch point
   near `A\approx0.537` (where the domain narrows to width 0 but `T` stays
   `\approx0.2465>0`, an unrelated geometric degeneracy).
5. Union of (3)+(4) covers the whole possible range `(A^\ast,\pi/2]`,
   giving `T\ge0` throughout `\mathcal D_b`, equality only at the corner.

This is a genuine new result: **the population's first unconditional proof
of `T\ge0`/`-q_1,-r_0\le0` on any nontrivial sub-domain**, after 10+ rounds
of failed SOS/SDP search on this exact target (now structurally explained
by this round's explorer as a forced complementary-slackness degeneracy at
a genuine domain corner — the local-Taylor technique correctly sidesteps
that degeneracy, exactly as it did for `D_1` and `Tgt`).

### Why this does NOT close Open gap 7 (the mandated full-chain check)

Per the round-20 dispatch's explicit instruction to trace the full
dependency chain before claiming `solved`, I checked whether this closes
Case (a) too, as round 19 believed and as the outline's Step 5 anticipated
("closing Open gap 7 for BOTH cases simultaneously"). **It does not, for a
more fundamental reason than expected.**

Case (a)'s domain (`\beta_1\le\beta_0(A)`) corresponds to `X_0(A,B)\ge
\cos^2\beta_0(A)` — the **complementary** region to `\mathcal D_b`
(`X_0<\cos^2\beta_0(A)`), not a subset of it. Checking `T`/`G(\beta_1)`
there (fresh 50-digit `mpmath`, raw definitions): at the ordinary,
non-degenerate witness `A=0.02,B=1.5` (`C=1.6216\ge B`), `X_0=0.4993>
\cos^2\beta_0(A)=0.2558` (genuinely Case (a)), `P=1.0001>0,E=-0.4990<0`
(same sign regime), yet
$$T=-0.249\ldots<0,\qquad G(\beta_1)=-0.654\ldots<0.$$
This is a **robust counterexample to `T\ge0`/`G(\beta_1)\ge0` in Case (a)'s
domain** — round 19's own witness, independently re-checked, also has
`T\approx-0.2487<0`. So round 19's claim that "Case (a)'s residual
coincides exactly with Case (b)'s `T\ge0` gap" is **incorrect**: `T<0` is
genuinely true there (not merely "not yet proved `\ge0`"). Proving `T\ge0`
therefore cannot possibly close Case (a) as a blanket statement.

This means the file's own Step 2 framing ("the target for every `\beta_1
\in(0,\gamma)` is `G(\beta_1)\ge0`, no case split in the target itself")
is not the correct universal statement for Case (a) — Case (a) needs either
a genuinely different reduction, or there is a missing constraint on
`(A,B)` (beyond `A\le\pi/2,B\le C`) not yet identified in this population's
20-round history that would exclude witnesses like `A=0.02,B=1.5` from
actually arising in the original geometric reduction (Steps 1-2, rounds
1-10 machinery, not re-derived from scratch this round). This is flagged
explicitly as the new, sharper, and more honest form of Open gap 7.

### Net assessment
- Genuine, certified, population-relevant new result: Case (b) of the
  whole problem is now closed by a second, independent, direct argument
  (this round's `T\ge0` proof), not requiring the file's own `\mathrm{Tgt}`/
  `D_1`/Reduction-Lemma machinery at all (though that machinery remains
  valid and gives the same conclusion via a different route).
- Case (a) is **not** closed, and — per the mandated dependency-chain
  trace — is now shown to need something genuinely different from what
  round 19 (and the round-20 outline) believed. This is caught and reported
  honestly, exactly as rounds 17-19 caught prior false/incomplete `solved`
  claims on this same file.
- **Status: partial**, not `solved`. The whole problem (`OM=ON`) is NOT
  proved by this route as it stands.

### Files updated
- `results/imo-2026-02/approaches/coordinate-bash-resultant-boundary-pointwise-tangent.md`:
  updated Status (top), new "Approaches tried" round-20 entry, new "Round
  20" full technical section (before "## Open gaps"), updated Open gap 7
  entry, updated "Full proof" Step 4/Conclusion-for-Case-(b) text, new
  "Promotable lemmas" round-20 entry.

### Recommendation for next round
Re-derive, from the original Steps 1-2 rotation/Cramer/MVT machinery
(rounds 1-10 of this population, not this file's own compressed
restatement), exactly what Case (a) needs to prove, and whether every
`(A,B)` with `A\le\pi/2,B\le C` is genuinely reachable by a valid
`K,L,O` configuration — or whether Case (a) implicitly requires a further
constraint (not yet stated anywhere in this file) that would exclude
counterexample-looking witnesses like `A=0.02,B=1.5`. This is a more
fundamental question than any prior round's diagnosis of Open gap 7, and
should be the top priority for whichever approach/round next attacks this
route.
