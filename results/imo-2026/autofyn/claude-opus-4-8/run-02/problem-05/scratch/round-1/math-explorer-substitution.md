## imo-2026-05 (substitution & plug-in route)

### Setup recap
Chain: sqrt((x^2+f(y)^2)/2) >= (f(x)+y)/2 >= sqrt(x f(y))  for all x,y>0.
Call the left inequality (A): 2(x^2+f(y)^2) >= (f(x)+y)^2, and the right (B): (f(x)+y)^2 >= 4x f(y).
No prior approaches exist in `results/imo-2026-05/` yet (workspace empty) — this is fresh terrain.

### KEY FINDING (verified algebraically with sympy, not just numerically): the exact functional equation
Trivial substitutions first: **x=y gives nothing** — (A) at x=y is just QM≥AM `sqrt((x^2+f(x)^2)/2)>=(x+f(x))/2`, always true; (B) at x=y is just AM≥GM `(f(x)+x)/2>=sqrt(x f(x))`, always true. Do not waste outline steps on x=y; it's vacuous.

The load-bearing substitution is **x = f(y)** (valid since f(y)>0, so it's a legal choice of x for the given y). Plugging x=f(y) into the *whole chain at once*:
- (A) becomes: sqrt((f(y)^2+f(y)^2)/2) = f(y) >= (f(f(y))+y)/2, i.e. **f(f(y)) <= 2f(y) - y**.
- (B) becomes: (f(f(y))+y)/2 >= sqrt(f(y)·f(y)) = f(y), i.e. **f(f(y)) >= 2f(y) - y**.

Both come from the *same* substitution x=f(y) applied to the *same* chain, so they hold simultaneously ⟹ **equality is forced**:
> **f(f(y)) = 2f(y) − y for all y > 0.**  (★)

This is an exact identity, not an inequality — a strong, clean reduction. (Verified by direct algebra above; also sanity-checked numerically that no other cheap substitution like y=f(x) gives anything beyond consistency — see below.)

### Consequence 1: f(y) ≥ y for all y (cheap-kill, rigorous)
(★) lets you substitute y → f(y) into itself (legal, f(y)>0): f(f(f(y))) = 2f(f(y)) − f(y) = 2(2f(y)−y) − f(y) = 3f(y) − 2y. By induction, for every integer n ≥ 0:
> f^(n)(y) = y + n·(f(y) − y).
(Induction step: apply (★) with y replaced by f^(n)(y), which is positive since it's a value of f.) Since f^(n)(y) must be a positive real for every n (it's f applied n times, landing in R_{>0}), if f(y) − y < 0 then f^(n)(y) → −∞, a contradiction for large n. Hence **f(y) ≥ y for all y > 0**. This is a genuine proved fact, not conjecture, and it's cheap (pure algebra from (★), no case work).

Iterating further (e.g. plugging x = f(f(y)) into the original chain) only reproduces consistency — it collapses to `(g(y))^2 ≥ 0`-type trivialities where g=f−id (checked by hand, e.g. x=f(f(y)) into (B) gives `0.25 g(y)^2 ≥ 0`). **Dead end**: don't expect more mileage from iterating the FE alone along a single orbit — you need a substitution that connects *two different points* not on the same f-orbit.

### Consequence 2 / candidate answer: f(x) = x + c, c ≥ 0, and it is EXACTLY the extremal family
Guess from (★) (which is satisfied by any affine f(x)=x+c, any real c, since f∘f(y)=y+2c=2f(y)-y automatically): test f(x)=x+c in the *original* two inequalities directly (not just the FE). Sympy-verified identities:
```
2(x^2+f(y)^2) - (f(x)+y)^2 = (x - y - c)^2   ≥ 0   [condition (A), always true, any real c]
(f(x)+y)^2 - 4x f(y)       = (x - y - c)^2   ≥ 0   [condition (B), always true, any real c]
```
So **f(x) = x + c satisfies the full original chain for every real c**, with equality (both inequalities tight) exactly when x = y + c. The only extra constraint is the codomain: f: R_{>0} → R_{>0} needs x + c > 0 for ALL x > 0, forcing **c ≥ 0**. So the conjectured answer is:
> **f(x) = x + c for some constant c ≥ 0** (this is my best-guess FULL answer; matches Consequence 1's f(y)≥y bound exactly at the boundary c=0).

This is strong numerical + symbolic evidence for the answer, but it is only the *construction* half — the *uniqueness* half (ruling out non-affine f) is NOT yet done.

### Consequence 3 (important negative result / dead-end warning): the FE (★) alone is NOT sufficient — need the full inequality
I built a piecewise f satisfying (★) exactly: f(y)=y for y≤1, f(y)=y+1 for y>1 (check: for y≤1, f(f(y))=f(y)=y=2y−y ✓; for y>1, f(y)=y+1>1 so f(f(y))=y+2=2(y+1)−y ✓). Numerically this f **violates the original chain badly** (found A-gap ≈ −0.50, B-gap ≈ −0.41 near x,y≈1, the "seam" of the piecewise definition). **Conclusion: any proof strategy that derives (★) and then tries to solve the FE alone (ignoring the original inequality for the rest of the argument) is a dead end** — it will under-constrain f and admit spurious jump-discontinuous "solutions." The outline must keep using the *original two inequalities* (not just (★)) to rule out non-affine / discontinuous f, e.g. to show g(x) := f(x) − x is the *same* constant for all x (not just constant along each f-orbit, which is all (★) gives via g∘f=g).

### Other substitutions tried (recorded so no one repeats them)
- **y = f(x)** into the chain: (A) gives x^2+f(f(x))^2 ≥ 2f(x)^2, (B) gives f(x)^2 ≥ x f(f(x)); substituting (★) into both reduces each to `(x−f(x))^2 ≥ 0`, i.e. trivially true, **no new information** — consistent but useless as a next step.
- **Swap (x,y)→(y,x)** and add to the original squared (A): produces `(x−f(y))^2+(y−f(x))^2 ≥ 0`, again trivial — adding the two squared inequalities cancels all the content. **Do not use naive add-and-cancel; it destroys the info.** A smarter combination (e.g. subtracting, or comparing (A)/(B) at (x,y) against (B)/(A) at (y,x) without summing) is untried and worth exploring next round — this is exactly where a genuinely new substitution (not sum) could pin g(x)=g(y) for arbitrary x,y, finishing uniqueness.
- **x → f(f(y))** (second iterate) into chain: collapses via (★) to `0.25(f(y)-y)^2 ≥ 0` — trivial, confirms consistency only.

### What a proof along this route would still need
1. The exact FE (★) f(f(y)) = 2f(y) − y (done, rigorous).
2. f(y) ≥ y (done, rigorous, via the iterate formula + positivity of codomain).
3. **The missing piece**: a substitution or argument (not from (★) alone, since (★) permits jump functions per Consequence 3) that shows g(x) = f(x) − x is the SAME constant for every x — i.e., some cross-substitution mixing two independent x, y values in the ORIGINAL inequality (A) or (B), not merely along one f-orbit. Candidates to try next round: plug x = y + t for general t and treat as an inequality in (g(x), g(y)) directly; or use monotonicity — first show f is non-decreasing (should follow from B: (f(x)+y)^2 ≥ 4x f(y), fixing y and sending x→ some comparison) then combine with (★) and the orbit formula to rule out non-constant g by a squeezing/continuity argument.
4. Verification write-up: f(x)=x+c, c≥0 satisfies both inequalities (already symbolically verified above as `(x-y-c)^2 ≥ 0` for both) — ready to drop into the "Full proof" verification section once uniqueness is closed.

### Candidate technique(s)
- Functional-equation "plug in f(y) for x" trick (self-referential substitution) — the crux move here.
- Iterate/orbit analysis of an FE to a linear recurrence (characteristic root 1, double) — standard for FEs of shape f(f(y))=2f(y)-y.
- SOS / perfect-square factoring to verify candidate families exactly (used above, `(x-y-c)^2`).
- Still needed: an injectivity/monotonicity argument or a second independent substitution to kill non-constant-g solutions.

### Knowledge-base entries to use
- **Functional equations**: "test special values, check injectivity/surjectivity" (knowledge_base.md, Algebra & Polynomials) — directly the method used for x=f(y).
- **Standard inequalities: AM-GM, Cauchy-Schwarz, QM-AM** — needed to recognize the trivial content of x=y and to write the verification cleanly.
- **Sum of squares (SOS) / completing the square** — used to verify f(x)=x+c gives exact `(x-y-c)^2` residuals for both inequalities.
- **Meta-strategy: "Prune before you compute"** — the x=y trivial check and the piecewise-f counterexample are exactly this kind of cheap structural probe.

### Analogous past problems (cruxes)
Filtered crux corpus by domain=algebra, subtopic ∈ {functional-equations, symmetric-functions-and-substitution}. Best matches:
- **aimo-0010** — "Compute one higher iterate of the unknown function two ways... to collapse the awkward triple composition into a clean shift-recurrence," then "Once an iterate equals translation by a constant, apply the base function to that relation," finally "Bootstrap a functional equation into a global affine identity h^N(n)=n+c." Very close in spirit to what's needed here: our (★) is already a clean shift-type recurrence (f(f(y))=2f(y)-y), and aimo-0010's playbook for turning an iterate relation into a genuine affine/translation identity (and then pinning the additive constant by summing displacement over a residue system) is the template to adapt for closing the "g constant" gap.
- **aimo-0097** — "Swap the two variables in a symmetric-looking two-variable identity and equate the two forms to extract a proportionality constraint forcing linearity." This is precisely the kind of swap-and-compare move that our naive sum-of-squares swap attempt failed to produce useful info from; aimo-0097's version subtracts/compares more cleverly rather than summing — worth reading in full before the outliner designs the swap step.
- **aimo-0008** — "Convert a one-sided bound into equality by sandwiching against a known exact value at a large point, splitting that point additively and letting the superadditive inequality force each summand to be tight." Analogous flavor to Consequence 1's "orbit must stay positive forever ⟹ can't decrease" argument, and could help with tightening g to an exact constant via an additive/multiplicative amplification trick.

### Prior progress
None (results/imo-2026-05/ was empty before this round).

### Dead ends (do not retry)
- x=y substitution: vacuous (recovers QM-AM / AM-GM tautologies).
- Solving the FE (★) alone without re-invoking the original chain: admits spurious non-affine (piecewise/jump) "solutions" — counterexample constructed and numerically confirmed violates the original inequality. Any approach that stops at (★) and claims f is affine is not rigorous.
- Naive "sum the swapped inequality with the original and simplify": telescopes to a trivial sum-of-squares ≥0, no info extracted. Need a subtraction/comparison move instead (cf. aimo-0097 crux).
- Iterating x=f^(n)(y) for n≥2: only reconfirms (★) is consistent, adds nothing new.

### Small-case / intuition notes (conjecture, not proof)
- Strong conjecture: the full answer is **f(x) = x + c for constants c ≥ 0** (verified symbolically that this family exactly satisfies both inequalities with equality iff x = y + c; and independently derived f(y) ≥ y as a necessary condition, consistent with c ≥ 0).
- No evidence found for any non-affine solution; the one natural non-affine candidate compatible with the derived FE was numerically falsified against the full original inequality.
