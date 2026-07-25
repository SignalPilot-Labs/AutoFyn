# Gap 6 scouted: EXACT closed-form identity found — `G_curve = -8 sin(u) cos^2(u) · h`

**Status: this is a genuine symbolic proof sketch, not just numerics. A builder should be able to write this up directly.** I did not attempt the final proof write-up (that's the builder's job), but the hard algebra is done and verified two independent ways (`sympy.simplify` to exact `0`, and 40-digit `mpmath` residual checks at 5 points including `A^*` itself).

## 1. Exact definitions used (rebuilt from scratch from the raw formulas in `coordinate-bash-resultant-boundary-pointwise-tangent.md` and `lemmas/d1-nonnegative-on-boundary-curve.md`)

$$X_0(A,B):=\frac{\sin B\cos A}{2\sin(A+B)},\qquad \beta_0(A):=\frac{\pi-A}{3},$$
$$K_c(A,B):=2\sin A\sin(A+B),\quad P(A,B):=\tfrac12\sin(A-B)+\tfrac32\sin(A+B),\quad Q(A,B):=-\sin A\sin B,$$
$$G(\beta;A,B):=K_c(A,B)-P(A,B)\sin\beta-Q(A,B)\cos\beta.$$

The two target functions (both single-variable, in `A` alone):
$$G_{\mathrm{curve}}(A):=G(\beta_0(A);A,\beta_0(A)),\qquad h(A):=X_0(A,\beta_0(A))-\cos^2\beta_0(A).$$

The target claim (round-17's Gap 6 base case, `X_0(A^*,B^*)=\cos^2(B^*)` given `G(\beta_0(A^*))=0`) is exactly **`G_curve(A^*)=0 \implies h(A^*)=0`**.

## 2. The key substitution: `u := A/3 + π/6`

This is the natural variable since `β_0(A)=(π-A)/3 = π/2 - u`. Substituting `A = 3u - π/2` and simplifying both functions with `sympy.simplify`/`expand_trig` collapses them to strikingly clean one-variable trig expressions:

$$\boxed{h(u) = \tfrac34 - 2\sin^2u}$$

$$\boxed{G_{\mathrm{curve}}(u) = (1-\cos2u)^2\sin u - 2\sin u + \tfrac34\sin3u - \tfrac54\sin5u}$$

(Both independently re-verified against the raw definitions via `sympy` — not copied from any prior file.)

## 3. The exact factorization (the whole gap, closed)

Expanding `sin3u = 3\sin u - 4\sin^3u`, `sin5u = 16\sin^5u-20\sin^3u+5\sin u` (classical multiple-angle formulas) and `\cos2u=1-2\sin^2u` (so `(1-\cos2u)^2=4\sin^4u`), collecting as a polynomial in `s:=\sin u` (verified by `sympy.expand`, exact rational coefficients, no floating point):

$$G_{\mathrm{curve}}(u) = 4s^5 - 2s + \tfrac34(3s-4s^3) - \tfrac54(16s^5-20s^3+5s) = -16s^5+22s^3-6s.$$

And, independently, expanding the target cofactor form directly:
$$-8\sin u\cos^2u\cdot h(u) = -8s(1-s^2)\bigl(\tfrac34-2s^2\bigr) = -16s^5+22s^3-6s.$$

**These two degree-5 polynomials in `s=\sin u` are identical term-by-term** (`sympy.expand` of their difference `=0` exactly) — a fully hand-checkable elementary trig identity, giving:

$$\boxed{G_{\mathrm{curve}}(A) \;=\; -8\sin(u)\cos^2(u)\cdot h(A),\qquad u:=\frac A3+\frac\pi6.}$$

**Verification performed (both independently confirmatory):**
- `sympy`: built `G_curve - (-8 sin(u)cos²(u)) · h` symbolically from the raw definitions (fresh derivation, not reusing any prior file's polynomials), called `sp.expand_trig` then `sp.simplify` → returns literal `0`.
- `mpmath` (40-digit precision): evaluated `G_curve(A)` and `-8\sin(u)\cos^2(u)h(A)` independently (not from the same symbolic expression — separate `lambdify` calls) at `A = 0.1, 0.30, 0.4063777806843303293871746903293092626710\ldots (=A^*), 0.90, 1.4`. Residual is `0` or at the `10^{-41}` floating-point noise floor at every point, including exactly at `A^*`.

This also **explains** round 17's "not proportional" finding precisely: the ratio `G_curve/h = -8\sin(u)\cos^2(u)` is a **genuine (non-constant) function of `A`**, not a constant — matching the reviewer's own numbers exactly: at `A=0.30`, `u=0.30/3+\pi/6\approx0.6236`, `-8\sin u\cos^2u\approx-3.0786` (reviewer reported `\approx-3.08`); at `A=0.90`, `u\approx0.8236`, `-8\sin u\cos^2u\approx-2.7104` (reviewer reported `\approx-2.71`). **Both match to 4 significant figures.** So the round-17 "not proportional" finding was correct (ratio isn't constant) but was the wrong test — the two functions are related by an exact *non-constant trigonometric cofactor*, not a constant multiple, and that cofactor is what needed to be found.

## 4. Why this closes the gap (proof sketch for the builder)

`G_curve(A) = -8\sin(u)\cos^2(u)\cdot h(A)` for `u=A/3+\pi/6`. If `\sin(u)\cos^2(u)\ne0`, then `G_curve(A)=0\iff h(A)=0` — an **iff**, not just an implication, and valid at *every* `A` with `\sin u\cos u\ne0`, not merely at the specific numeric point `A^*`.

**Non-vanishing of the cofactor on the relevant domain.** The population already has (round 11 of `coordinate-bash-resultant-boundary-pointwise.md`, reused throughout the `-tangent` file): on the Case-(b) domain `\mathcal D`, `0<A<\pi/2` (established: `X_0\ge0` forces `\cos A\ge0` whenever `\sin(A+B)>0`). For `A\in(0,\pi/2)`, `u=A/3+\pi/6\in(\pi/6,\pi/3)\subset(0,\pi/2)`, so `\sin u>0` and `\cos u>0` strictly — **unconditionally**, no case split, no need to know `A^*`'s numeric value at all. In particular this holds at `A=A^*\approx0.4064\in(0,\pi/2)`.

**Conclusion.** Since `A^*\in(0,\pi/2)` (already established/consistent with the certified 40-digit value), the cofactor `-8\sin(u^*)\cos^2(u^*)\ne0` at `u^*=A^*/3+\pi/6`, so
$$G_{\mathrm{curve}}(A^*)=0 \iff h(A^*)=0.$$
Given the already-certified `G_{\mathrm{curve}}(A^*)=0` (`lemmas/star-corner-is-boundary-cusp-not-critical-point.md`), this gives `h(A^*)=0`, i.e. `X_0(A^*,B^*)=\cos^2(B^*)` **exactly** — the fact `d1-nonnegative-on-boundary-curve.md`'s Step 0 needed and could only cite numerically. This should fully unblock that lemma's rejected Step 0, and hence (per the chain already laid out in `d1-nonnegative-on-boundary-curve.md` and the `-tangent` approach file) close Gap 6 in full, which per the standing note in `/tmp/memory/run_state.md` completes the entire problem via this route.

## 5. What the builder still needs to do (not done here — I'm an explorer)

1. **Write up §3's polynomial-in-`\sin u` identity as the primary proof** (it is already fully hand-checkable: both sides expand to the identical degree-5 polynomial `-16s^5+22s^3-6s` in `s=\sin u`, verified by `sympy.expand` and independently by direct hand arithmetic in this report) — this is stronger than citing a black-box `simplify`-to-`0`, since every coefficient is explicit and checkable by a human with the two classical multiple-angle formulas.
2. **State and cite `0<A<\pi/2` on `\mathcal D`** as the fact licensing `\sin u,\cos u>0` (already established elsewhere in the population, per round 11 of the `-pointwise` sibling file — just needs a clean citation, not new work).
3. **Splice into `lemmas/d1-nonnegative-on-boundary-curve.md`'s Step 0**, replacing the rejected citation to the unproved "two boundary curves meet at the corner" fact with this identity + the already-certified `G_curve(A^*)=0`.
4. Double check whether `B^*=\beta_0(A^*)` is needed *only* via `G_curve(A^*)=0` (yes, per the lemma file) — i.e. confirm no other place in the chain silently also assumed the old unproved fact (ii). A scan of `d1-nonnegative-on-boundary-curve.md` and the `-tangent` approach file's Reduction Lemma (`New result 1`, round 13) is warranted before declaring the whole gap closed.

## 6. Geometric/synthetic angle (scouted, negative — not needed given §3–4)

I looked briefly for a synthetic reason (degenerate triangle, `K=L`, orthocenter/circumcenter coincidence) the corner might force this identity, since the problem is originally a triangle-geometry statement. Given the clean algebraic closure found above, I did not pursue this further — the coordinate route is already a complete, short, exact proof, so a synthetic route is no longer needed to close the gap (though it might still be worth a future round's attention for a shorter overall writeup, out of scope here).

## Files consulted
- `results/imo-2026-02/approaches/coordinate-bash-resultant-boundary-pointwise-tangent.md` (rounds 11–13 for `X_0,\beta_0,K_c,P,Q,G,\mathrm{RHS}` raw definitions)
- `results/imo-2026-02/approaches/coordinate-bash-resultant-boundary-pointwise.md` (round-11 domain characterization, `0<A<\pi/2` fact)
- `results/imo-2026-02/lemmas/star-corner-is-boundary-cusp-not-critical-point.md` (definition of `A^*`, `G_curve`, certified `G_curve(A^*)=0`)
- `results/imo-2026-02/lemmas/d1-nonnegative-on-boundary-curve.md` (the rejected lemma, exact statement of what's needed and why it was rejected)
