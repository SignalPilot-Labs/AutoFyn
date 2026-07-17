## imo-2026-05

### Statement recap
Find all f: R_{>0} -> R_{>0} with, for all x,y>0:
  sqrt((x^2+f(y)^2)/2) >= (f(x)+y)/2 >= sqrt(x f(y)).
Squared (both sides of each inequality are positive, so squaring is reversible/valid):
  (L) 2(x^2 + f(y)^2) >= (f(x)+y)^2
  (R) (f(x)+y)^2 >= 4x f(y)

### IMPORTANT — the expected-answer shape is probably wrong if you assume "f = id only"
I verified **rigorously (symbolically, via sympy `factor`/`simplify`, and independently by hand)** that for
**every constant c >= 0**, f(x) = x + c satisfies BOTH (L) and (R) for ALL x,y > 0, with equality
exactly on the line x - y = c:
- (L): `2(x^2+(y+c)^2) - (x+c+y)^2 = (x-y-c)^2 >= 0` always.
- (R): `(x+c+y)^2 - 4x(y+c) = (x-y-c)^2 >= 0` always (same square!).
Both reduce to the *same* perfect square `(x-y-c)^2`. Numerically confirmed with 200k random
(x,y) trials per c in {0, 0.5, 1, 3, 10}: min slack -> 0 (equality locus), never negative.
c < 0 is inadmissible only because f(x)=x+c would go non-positive for small x (domain violation),
not because the inequality fails.

**Conclusion: the true answer is the whole one-parameter family f(x) = x + c, c >= 0 — NOT
just the identity.** Any approach/outline that sets out to "prove f(x)=x for all x" as the target
claim is proving the wrong (too strong / false) statement and must be corrected to the family.
This is the single most important structural fact for the outliner to build the target claim
around; flag it loudly.

### The crux algebraic move: substitute x = f(y)
Plugging **x = f(y)** (valid since f(y) > 0 is in the domain) into the ORIGINAL sandwich collapses
the outer sqrt terms because f(y)=f(y):
- Left inequality at x=f(y): `sqrt((f(y)^2+f(y)^2)/2) = f(y) >= (f(f(y))+y)/2`
  => `f(f(y)) <= 2f(y) - y`.
- Right inequality at x=f(y): `(f(f(y))+y)/2 >= sqrt(f(y)*f(y)) = f(y)`
  => `f(f(y)) >= 2f(y) - y`.
Combining: **f(f(y)) = 2f(y) - y exactly, for all y > 0.** This is unconditional, rigorous, no
continuity/monotonicity assumed — the single cleanest fact extractable from the problem, and it
is EXACTLY the equation that constant shifts satisfy (f(f(y))=y+2c=2(y+c)-y ✓), so it's necessary
but (as shown above) far from sufficient — don't mistake "derived f∘f=2f-id" for "done."

### Consequence 1 (rigorous): f(y) >= y for all y
`f(f(y)) = 2f(y)-y` means the orbit `a_0=y, a_1=f(y), a_2=f(f(y)), …` satisfies the linear
recurrence `a_{n+1} = 2a_n - a_{n-1}` (characteristic root 1, double), hence is an **exact
arithmetic progression**: `a_n = y + n*d(y)` where `d(y) := f(y) - y`. (Proved by induction using
the identity applied at each successive point of the orbit — each `a_n` is a positive real since
it's f applied to the previous positive real, so the whole orbit lies in R_{>0}.) If `d(y) < 0`,
`a_n -> -infinity`, so some `a_n <= 0`, contradicting `a_n in R_{>0}`. Hence `d(y) >= 0`, i.e.
**f(y) >= y for every y**. This is a genuine global lower bound, established with zero regularity
assumptions — safe to hand to the outliner as settled.

### Consequence 2: c(x) := f(x) - x cannot vary — decomposition identities
Writing `c(x) = f(x)-x >= 0` (well-defined by Consequence 1) and expanding (L),(R) in terms of
`cx=c(x), cy=c(y)` (verified symbolically):
- (L): `2(x^2+f(y)^2) - (f(x)+y)^2 = (x-y-cx)^2 + 2(cy-cx)(2y+cx+cy) >= 0`
- (R): `(f(x)+y)^2 - 4x f(y) = (x-y+cx)^2 + 4(y*cx - x*cy) >= 0`
Both must hold for **all** x,y>0, not just matched orbit points — this is the leverage beyond
Consequence 1. Setting `y = x - cx` (valid whenever `x > cx`, i.e. `f(x) < 2x`) kills the square
term in each:
- from (L) at y=x-cx: `cy - cx >= 0` i.e. `c(x-cx) >= c(x)`.
- from (R) at y=x-cx: (after simplification) `c(x-cx) <= c(x)`.
Together: **c(x - c(x)) = c(x) exactly**, whenever f(x) < 2x. This is a concrete, checkable lever
toward proving global constancy of c — I stopped here (this is outline territory), but it is a
genuine opening: iterate `x_{n+1} = x_n - c(x_n)` to get a strictly decreasing (while c(x_n)>0)
sequence of points all sharing the same c-value, and combine with a second, independent
substitution (not yet found) to force `c(x)=0` or force a global two-point equality `c(x)=c(y)`
for arbitrary unrelated x,y (needed to conclude a single GLOBAL constant, since the descent above
only links points within one "chain"). This is the main remaining gap.

### Numerical stress test: even smooth non-constant perturbations fail
- f(x) = x + 1 + 0.01*sin(x) (smooth, nearly-constant shift): **fails** — found (x,y) with left
  slack -0.0061 and right slack -0.0063 in 300k random trials over x,y in (0,50). So constancy is
  not just "convenient," it's necessary — even an O(0.01) continuous wobble breaks the sandwich.
- A crude two-class piecewise shift (f(x)=x if floor(1000x) even, x+1 otherwise): **fails badly**,
  slack about -0.5, found immediately.
These are strong (non-proof) confirmations that the final answer is exactly the family
`f(x)=x+c, c>=0`, no more, no less — good for cross-checking any outline's final claim.

### Dead-end / trap risks for the outliner
- **Setting x=y in the original inequalities is a dead end / gives zero information.** At x=y,
  the right inequality collapses to AM-GM(f(x),x) and the left to QM-AM(x,f(x)) — both are true
  for ANY positive a=f(x), b=x, regardless of what f is. Confirmed algebraically. Do not present
  "set x=y" as making progress; it's a trap that looks like it should force f(x)=x but does not.
- **Scaling family f(x)=kx**: right inequality holds for every k>0 (it's exactly AM-GM(kx,y)).
  Left inequality reduces (via a 2x2 quadratic-form / PSD-determinant check) to
  `-2(k^2-1)^2 >= 0`, forcing k=1 — but k=1 is just the c=0 member of the shift family, so scaling
  contributes NO solutions beyond the shift family; don't waste an approach slot re-deriving this
  as if it were a separate branch.
- Any approach whose target claim is "prove f = identity" is proving a **false** (too strong)
  statement — it will hit an unfixable contradiction (or worse, silently "succeed" via an invalid
  step) because f(x)=x+c genuinely satisfies the hypotheses for c>0. The correct target is
  "f(x)=x+c for some/any constant c>=0."

### Candidate technique(s)
- Substitution-chasing in functional inequalities (squeeze a two-sided inequality into an exact
  equation by choosing the argument that makes the outer bound and inner bound coincide) —
  this is exactly how `f(f(y))=2f(y)-y` was extracted (x=f(y)).
- Orbit/iterate analysis of a derived linear recurrence (`a_{n+1}=2a_n-a_{n-1}` -> arithmetic
  progression -> boundedness/positivity forces sign of common difference). Knowledge-base
  "Linear recurrences" (Number Theory section) and "Functional equations: test special values,
  check injectivity/surjectivity" (Algebra section) both apply generically; this problem needs a
  bespoke iterate argument beyond what's listed.
- SOS / perfect-square decomposition of a functional inequality (knowledge_base "Sum of squares
  (SOS) / completing the square") — directly used above to get the clean `(x-y-c)^2` and
  `(x-y-cx)^2 + 2(cy-cx)(...)` decompositions; likely the right lens for closing the "c is
  globally constant" gap too (find an SOS-style identity linking c(x), c(y) for arbitrary
  unrelated x,y, not just points in the same descent chain).
- AM-GM / QM-AM equality analysis (knowledge_base "Standard inequalities") — the whole problem is
  built from AM-GM and QM-AM; equality cases of these classical inequalities are the geometric
  meaning of `x = f(y)` type substitutions.

### Knowledge-base entries to use
- "Sum of squares (SOS) / completing the square" (Algebra & Polynomials).
- "Standard inequalities: AM-GM, Cauchy-Schwarz, QM-AM, Schur" (Algebra & Polynomials).
- "Functional equations: test special values, check injectivity/surjectivity" (Algebra &
  Polynomials) — generic pointer only; the specific iterate/recurrence trick here isn't in the KB
  and should probably be added as a new KB entry once proven ("derive an exact equation from a
  two-sided functional inequality by choosing the argument that saturates both sides
  simultaneously").
- "Linear recurrences" (Number Theory) — used for the `a_{n+1}=2a_n-a_{n-1}` arithmetic-orbit
  argument, even though this problem is algebra-domain.

### Analogous past problems (cruxes)
Filtered `past_crux_moves_database.json` by `domain=algebra`, `subtopic=functional-equations`
(263 entries) and cross-checked candidates against `past_problems_database.json`:
- **aimo-0089** (`Find all f:R->R satisfying [a two-sided weighted-average / convexity
  inequality]`): genuinely analogous in *kind* — it's one of the few crux problems built on a
  **functional inequality** (not equation) that must be squeezed to an exact identity (reframed
  as a supporting-line/supergradient bound, then differentiated into Jensen's equation). Same
  meta-move as ours: two-sided inequality -> forced exact structure. Worth reading in full for the
  squeeze technique, though the concrete algebra differs (ours is sqrt/AM-GM based, not convexity).
- **aimo-0010** (`f(f(f(n)))=f(n+1)+1` on nonnegative integers, IMO/Serbia): the crux move
  "compute one higher iterate two ways ... to collapse the awkward triple composition into a
  clean shift-recurrence" and "apply the base map to the whole functional equation to turn a fixed
  iterate into a unit-increment recurrence" is methodologically the closest analog to our
  `f(f(y))=2f(y)-y` -> arithmetic-orbit argument. Note aimo-0010's actual answer set is TWO
  functions (not one), a useful reminder that iterate-recurrence FEs often have richer answer sets
  than a single f=id — consistent with our finding of a whole family here.
- **aimo-0234** (`f(xy+f(x)) = x f(y)+2` over positive reals): same domain (R_{>0}->R_{>0}) and
  "drive one variable to infinity to force a coefficient to vanish, pinning the function exactly"
  — potentially useful pattern for the "prove c is globally constant" gap (taking x or y to
  infinity/0 in the decomposition identities above). Read for technique, not for a matching
  answer shape.
No crux was found that matches the exact sqrt/AM-GM sandwich structure of this problem; the above
three are the best available analogs for the *technique*, not the *statement*.

### Prior progress
None — this is round 1, workspace `results/imo-2026-05/` has empty `approaches/` and `lemmas/`.

### Dead ends (do not retry)
- "Set x=y to force f(x)=x": proves nothing (AM-GM/QM-AM equality tautology for any f).
- "f is linear/scaling f(x)=kx, general k": only k=1 survives, and that's already covered by the
  shift family at c=0 — not an independent case.
- "Target claim: f(x)=x is the unique solution": FALSE. Verified f(x)=x+c works for all c>=0.

### Small-case / intuition notes (conjecture unless marked rigorous)
- **[rigorous]** f(x)=x+c, c>=0, are all solutions (symbolic + numeric verified).
- **[rigorous]** f(f(y)) = 2f(y) - y for all y (derived by substitution x=f(y)).
- **[rigorous]** f(y) >= y for all y (from orbit-positivity of the arithmetic progression).
- **[conjecture, strongly evidenced]** These are ALL the solutions — i.e. f(x)-x must be a single
  global constant. Evidence: exact identity c(x-c(x))=c(x) on chains (rigorous but only proves
  constancy within a descent chain, not globally); numerical failure of any non-constant
  (piecewise or smooth-perturbed) candidate, even at amplitude 0.01. The remaining gap is a
  genuine global-constancy argument (linking c at two arbitrary unrelated points, not just points
  in the same orbit/chain) — this is the crux gap for the outliner to target, likely via a further
  clever pair of substitutions in identities (L)/(R) above, or via an extremal argument (sup/inf of
  c(x) over x, or of c(x)/x, forced to be attained and self-consistent).
