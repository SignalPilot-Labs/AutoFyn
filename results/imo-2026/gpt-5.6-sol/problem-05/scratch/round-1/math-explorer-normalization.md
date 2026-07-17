## imo-2026-05
- Distinct openings:
  1. **Displacement/cone rigidity (strongest normalization route).** Write \(a=f(x)-x\), \(b=f(y)-y\), square both inequalities (all quantities are positive), and denote the upper and lower residuals by \(U,L\). Exact algebra gives
     \[
     L=(f(x)+y)^2-4xf(y),\qquad U=2(x^2+f(y)^2)-(f(x)+y)^2,
     \]
     \[
     L-U=2(a-b)(a+b+2x+2y)=2(f(x)-f(y)-x+y)(f(x)+f(y)+x+y),
     \]
     and \(L+U=2(x-f(y))^2\). Since \(L,U\ge0\), this yields the global sharp bound
     \[
     |(f(x)-x)-(f(y)-y)|\le \frac{(x-f(y))^2}{x+y+f(x)+f(y)}.
     \]
     Swapping \(x,y\) supplies the analogous bound with \(y-f(x)\). A whole-problem route could classify the displacement \(g(x)=f(x)-x\) from these two constraints and show it is constant; every constant displacement \(f(x)=x+c\), \(c\ge0\), then works. The required hard lemma is precisely: these pairwise cone bounds force \(g\) constant and nonnegative, without assuming continuity, monotonicity, or surjectivity.
  2. **Interval-overlap / geometric route.** The original inequalities say the same scalar \(f(x)+y\) lies in
     \([2\sqrt{xf(y)},\sqrt{2(x^2+f(y)^2)}]\). These endpoints are the GM and RMS expressions for the vector \((x,f(y))\). In squared coordinates, \(L,U\ge0\) and \(L+U=2(x-f(y))^2\): the available slack is exactly the squared distance from the diagonal. Compare the constraint for \((x,y)\) with that for \((y,x)\); exact subtraction gives
     \[
     U(x,y)-L(y,x)=(x+y-f(x)-f(y))(x-y+f(x)-f(y)),
     \]
     while the swapped difference is its negative. Thus the two feasible intervals impose opposite ordering information on the same product. A viable complete route would interpret this as a cone/nonexpansive graph condition and classify graphs lying in all such cones as parallel translates of the diagonal. Required lemma: a purely metric two-point classification of such graphs; beware that ordinary Lipschitz/nonexpansive conclusions alone are too weak.
  3. **Normalize by ratios/logs.** Put \(r=y/x\), \(A=f(x)/x\), \(B=f(y)/y\). After division by \(x^2\), the pair gives
     \[
     (A+r)^2\ge4Br,\qquad (A+r)^2\le2(1+B^2r^2).
     \]
     Reversing \((x,y)\) gives the companion pair with \(A,B,r\) interchanged. For a homogeneous candidate \(f(x)=cx\), requiring the upper inequality for every \(r>0\) yields a quadratic whose discriminant is \(8(c-1)^2(c+1)^2\); hence the only homogeneous solution is \(c=1\). In log variables \(h(t)=\log(f(e^t)/e^t)\), the target family is not constant unless \(c=0\): it is \(h(t)=\log(1+ce^{-t})\). So logs may classify asymptotic slopes but do not linearize the actual family. A complete ratio route needs a lemma recovering the affine intercept from the coupled inequalities rather than incorrectly concluding homogeneity.
  4. **Quadratic-root collision.** For fixed \(x\), each squared inequality is quadratic in \(f(y)\), and for fixed \(y\), quadratic in \(f(x)\). Using two choices of the free variable may force the feasible root intervals to intersect only when \(f(t)-t\) has a common value. This is analogous to determining a function value from two independently generated quadratic candidate sets. Required lemma: choose comparison points so the two interval constraints collapse without continuity assumptions.
- Candidate technique(s): Squaring positive inequalities; completing the square/SOS; displacement substitution \(g=f-\mathrm{id}\); two-point cone or nonexpansive-graph classification; ratio normalization; quadratic discriminant/root-interval intersection. The likely characterization, strongly supported algebraically and numerically, is \(f(x)=x+c\) for arbitrary \(c\ge0\).
- Cheap-kill candidates: Square immediately. Subtract the two squared residuals before estimating them; this exposes displacement differences. Also compare \((x,y)\) and \((y,x)\). Test affine functions first: \(f(x)=x+c\) makes **both** squared residuals exactly \((x-y-c)^2\), so all \(c\ge0\) are genuine candidates. For \(f(x)=cx\), the discriminant calculation kills every \(c\ne1\). Positivity kills translations with \(c<0\) as globally defined maps into \(\mathbb R_{>0}\).
- Knowledge-base entries to use: **Sum of squares (SOS) / completing the square**; **Quadratic forms**; **Standard inequalities** (AM-GM and equality cases); **Functional equations: test special values, check injectivity/surjectivity** (but no regularity should be presumed); **Introduce a substitution / change of variables**; **Exploit symmetry / WLOG: normalize**; **Reformulate** (geometric cone interpretation); **Check the answer**.
- Analogous past problems (cruxes):
  - `aimo-0186` — genuinely analogous algebraic mechanism: regard the condition as a quadratic in one function value, derive a two-root candidate set, then collide candidate sets from different substitutions. Here the objects are feasible quadratic intervals rather than exact roots.
  - `aimo-0988` — analogous squared-expression cancellation: rewrite two shifted-square expressions so a shared term cancels and what remains is an ordered pair of squares. This supports prioritizing exact residual identities over coarse AM-GM estimates.
  - `aimo-0552` — analogous positive-real functional inequality where swapping variables and AM-GM convert pairwise feasibility into rigidity of the graph. Its exact uniqueness hypothesis is absent here, so only the symmetric-pair viewpoint transfers, not its proof.
  (`aimo-0939` is useful only for the mechanical move of clearing radicals and factoring; it is not structurally close enough to rank above these.)
- Prior progress: Workspace is absent and run state says unsolved. No prior approaches or certified lemmas exist. The exact candidate family discovered in this scouting is \(f(x)=x+c\), \(c\ge0\); direct symbolic substitution gives equality of both squared residuals to \((x-y-c)^2\), which verifies the family after noting all sides are positive.
- Dead ends (do not retry):
  - Do not guess only \(f(x)=x\): numerical and symbolic checks show every nonnegative translation works.
  - Pure homogeneity/ratio arguments erase the additive parameter and can at best isolate the slope \(1\); they need an intercept-recovery stage.
  - Logarithmic variables do not make the solution family affine: \(\log(f(e^t)/e^t)=\log(1+ce^{-t})\).
  - Coarse AM-GM/RMS comparison alone is tautological and loses the decisive relation between the two residuals.
  - Inferring continuity, monotonicity, injectivity, or surjectivity from the inequality without proof is unsafe; translations with \(c>0\) are not surjective onto all positive reals.
  - A single diagonal substitution \(x=y\) is too weak: the candidate residual is \(c^2\), not forced equality.
- Small-case / intuition notes: **Conjecture, supported by exact affine substitution and numerical searches:** all solutions are \(f(x)=x+c\), \(c\ge0\). Wide-grid tests reject \(1/x\), constants, powers \(x^k\) for sampled \(k\ne1\), \(\max(x,1)\), \(\sqrt{x^2+1}\), \(x+1/x\), and piecewise translations. Exact checks: for \(f=x+c\), both squared gaps are \((x-y-c)^2\); for \(f=cx\), all-ratio feasibility forces \(c=1\). The evidence suggests the invariant is additive displacement, not multiplicative ratio.