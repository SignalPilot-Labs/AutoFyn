## orbit-collision-clopen — APPROVE

This is a complete end-to-end classification route. The simultaneous equality at `x=f(y)` rigorously gives the arithmetic-orbit identity; positivity rules out negative displacement; the nearest-multiple comparison can force all positive orbit increments to agree; and the zero fiber can then be shown clopen without assuming continuity. Sufficiency covers the entire claimed family `f(t)=t+c`, `c>=0`.

Builder requirements:
- In Step 1, first retain the exact pair of squared slack formulas
  \[
  (x-y-g(y))^2\pm (g(x)-g(y))(2x+2y+g(x)+g(y))\ge0.
  \]
  The absolute-value form (D) with the second factor outside the absolute value is licensed only after Step 3 establishes `g>=0`. Avoid presenting this dependence in a circular order.
- In Step 2, compute both endpoint values explicitly at `x=f(y)` before forcing the middle equality. If injectivity is used, prove it from `f(f(t))=2f(t)-t` rather than merely asserting it.
- In Step 4, make the floor choice explicit. For large `n`, set `k=floor((u+na-v)/b)` and `m=k-1`; then `m>=0` and `0<=u+na-(v+(m+1)b)<b`. Also show `m->infinity`, so the coefficient on the left of (D) diverges, while the right side is bounded by `b^2`.
- In Step 5, give direct epsilon arguments. For closedness, apply (D) to `(z,z_n)` with `g(z_n)=0` and pass only through the resulting numerical inequality. For openness at `p` with `g(p)=0`, choose a concrete neighborhood where `(x-p)^2<c(2x+2p+c)`; do not appeal to continuity of `g`.
- State and verify the final characterization explicitly, as required for a compute-and-prove problem.

## lattice-envelope-amplification — APPROVE

This is also a sound whole attempt and is the strongest route in the field. Once one positive orbit of step `c` exists, its equality centers form a fixed-step lattice covering the tail. Applying (D) there gives a genuine uniform numerical estimate `|g(t)-c|=O(1/t)` without any regularity assumption on `g`. Evaluating that estimate on each exact positive-displacement orbit forces exact equality of increments. The remaining zero/positive dichotomy is correctly handled by connectedness, and the translation family is verified.

Builder requirements:
- Observe the same ordering issue for (D): derive the paired slacks first, obtain `g>=0` from the forced orbit, and only then use positivity of `2x+2y+g(x)+g(y)` to state (D).
- Quantify Step 3. For all sufficiently large `t`, choose `n>=0` with `|t-(v+(n+1)c)|<=c/2` (a one-sided floor choice with error `<c` also suffices). With `y=v+nc`, (D) has right side at most `c^2/4` (or `c^2`), while its coefficient is at least `2t`; this yields an explicit bound such as `|g(t)-c|<=c^2/(8t)` under the half-step choice.
- In Step 4, separate `g(u)=0` from `g(u)=a>0`. Only in the latter case does `u+na->infinity`; then the uniform tail estimate evaluated at these points, together with orbit invariance, gives `|a-c|<=C/(u+na)` for every large `n`, hence `a=c`.
- Supply the direct epsilon proofs that the zero locus is closed and open after the range has been reduced to `{0,c}`; no continuity of `f` or `g` may be inferred.
- Explicitly handle the initial no-positive-displacement case and verify both original unsquared inequalities for every `c>=0` using positivity and the two squared SOS slacks.

## swapped-order-rigidity — RETHINK

Step 3 is not an identified lemma with a working mechanism. Injectivity does not imply monotonicity, and the cited “forbidden-slope” analogy does not show that an auxiliary variable can realize the needed crossing under this inequality. No algebra is supplied that turns (S) into an order contradiction. Step 5 is a second independent load-bearing gap: “(S) should prevent a jump” is not a proof or a mechanism. The route therefore cannot presently be built without either proving a new monotonicity theorem from scratch or reverting to the already approved lattice argument. Do not register it. A viable revision would need an explicit inequality showing an assumed order reversal violates (S), before plateau propagation is considered.

## quadratic-zero-locus-propagation — RETHINK

The local quadratic estimate in Step 2 is correct, but it controls `g` only near the moving centers `f(y)`. Steps 3–4 require a competing label to remain at bounded transverse distance from those centers, and the outline explicitly has no mechanism guaranteeing this. Iterating one orbit does not make its fixed-step centers locally dense, nor does it control arbitrary fibers. Thus the claimed discreteness/singleton conclusion does not follow. Importing nearest-lattice comparison would turn this into `orbit-collision-clopen`, so this is not an independent buildable route. Do not register it. A revision must either prove a genuine neighborhood statement around every domain point from the centered estimate or choose a different global mechanism.

Ranking: `lattice-envelope-amplification` is ranked above `orbit-collision-clopen` because one fixed orbit yields a uniform tail estimate applicable to every point and avoids the extra two-index divergence bookkeeping. Both are sound and substantially closer to completion than the two rejected conditional routes.

build set: lattice-envelope-amplification, orbit-collision-clopen
