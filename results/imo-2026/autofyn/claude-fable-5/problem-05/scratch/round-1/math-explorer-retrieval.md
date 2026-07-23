## imo-2026-05

### Distinct openings (retrieval + reformulation lens)

1. **The x = f(y) collapse (the crux move — verified rigorously, not just numerically).**
   Squaring both parts of the chain gives, for all x,y>0:
   `4x f(y) <= (f(x)+y)^2 <= 2(x^2+f(y)^2)`.
   Write A = x, B = f(y), M = f(x)+y, so the chain reads `4AB <= M^2 <= 2(A^2+B^2)`,
   i.e. `GM(A,B) <= M/2 <= QM(A,B)`. Substituting **x = f(y)** makes A = B = f(y), so
   `GM(A,B) = QM(A,B) = f(y)` exactly (QM = GM iff the two numbers are equal). The
   sandwich collapses `f(y) <= (f(f(y))+y)/2 <= f(y)`, forcing **equality**:
   `f(f(y)) = 2f(y) - y` for all y > 0.
   This is a clean, fully rigorous necessary condition — no case work, no calculus,
   just plugging a value that makes the two outer bounds coincide. It should be the
   backbone lemma of any approach.

2. **Iterating the collapse identity forces `f(y) >= y`.**
   `f(f(y)) = 2f(y) - y` means the sequence `y_0=y, y_1=f(y), y_2=f(f(y)),...`
   satisfies the linear recurrence `y_{n+1} = 2y_n - y_{n-1}` (char. root 1, double),
   so by induction `y_n = f^{(n)}(y) = y + n·d(y)` where `d(y) := f(y) - y`. Since
   every `y_n` must lie in `R_{>0}` (f maps into `R_{>0}`), and this must hold for
   **all** `n >= 0`, we need `d(y) >= 0` for every y (else `y_n -> -infty`).
   Conclusion so far: `f(y) >= y` for all y, and `f(f(y)) = 2f(y)-y` exactly.

3. **Sufficiency of the constant-shift family — verified algebraically, not just
   numerically.** For `f(x) = x + c` with constant `c >= 0` (needed for f(x)>0 on
   all x>0): compute `A = x`, `B = f(y) = y+c`, and notice `f(x) + y = x+c+y = A+B`
   exactly (this identity is special to constant shifts: `f(x)-x = f(y)-y = c`).
   Then:
   - Left inequality `<=> 2(A^2+B^2) >= (A+B)^2`, which is just `(A-B)^2 >= 0` —
     **always true**.
   - Right inequality `<=> (A+B)/2 >= sqrt(AB)`, the ordinary AM-GM on A,B — **always
     true** for A,B>0.
   So **every** `f(x)=x+c`, `c >= 0`, satisfies both original inequalities for
   *all* x,y — proved, not conjectured. This means the answer is **not** just
   `f=id`; it is (at least) the whole family `{x -> x+c : c >= 0}`. Numerically
   confirmed with 200000 random (x,y) trials for c ∈ {0,0.5,1,2,5}: zero
   violations (see intuition notes) — consistent with the algebraic proof.

4. **Remaining gap: promote `d(y) := f(y)-y` from "≥0 pointwise, with
   `d(f(y))=d(y)`" to "constant across all y."** From step 1, `d(f(y)) = d(y)`
   (orbits of f carry a fixed difference). This alone permits non-constant `d`
   (e.g. constant on each orbit but different across orbits) — it does NOT yet
   force `d` to be one global constant. The x=f(y) substitution has been fully
   mined; further necessity must come from a **generic (x,y) substitution**, not
   one that collapses to the diagonal. Two half-worked reformulations for the
   outliner to pursue:
   - Expand the right inequality in x,y directly: `(x-y)^2 + 2(x+y)d(x) + d(x)^2
     >= 4x·d(y)` for all x,y>0 (derived by writing f(t)=t+d(t) in
     `(f(x)+y)^2 >= 4xf(y)`). This ties `d(x)` and `d(y)` together for *every*
     pair, not just orbit-mates — likely the route to constancy (e.g. fix x,
     let y range or vice versa, or take x,y in the same orbit vs different
     orbits and compare).
   - Symmetric add/swap: adding the right inequality at (x,y) and at (y,x) only
     reproduces `(f(x)-y)^2+(f(y)-x)^2 >= 0` (checked — trivial, no new info,
     a **dead end**, don't retry this specific combination).
   - Left inequality similarly expands to `x^2 + (y+d(y))^2 >= (x+d(x)+y)^2/2`,
     a second independent (x,y)-coupling of d(x), d(y) — combine with the right
     one above.

### Candidate technique(s)
- **Forced-equality-by-matching-bounds** (squeeze where two independently
  derived bounds are made to coincide by a clever substitution) — this is
  exactly what cracked the problem's core lemma in step 1 above, and is a
  recognized crux-corpus pattern (see aimo-0008 below).
- Linear recurrence / arithmetic-progression-of-iterates argument (step 2).
- AM-GM / QM-AM equality-case analysis (`(A-B)^2>=0`, `(A+B)/2>=sqrt(AB)`) —
  KB's "Standard inequalities" entry.

### Cheap-kill candidates
- The x=f(y) collapse (step 1) is itself the cheap kill: it converts an
  inequality problem into an honest functional equation `f(f(y))=2f(y)-y` in
  one substitution, with zero casework. Do this first in any approach.
- Positivity-of-codomain pigeonhole (step 2): iterating f forces `d(y)>=0`
  immediately, ruling out any solution with `f(y)<y` anywhere — a one-line
  elimination of a whole class of candidates (e.g. rules out `f(x)=x-c` for
  c>0, and rules out any f with f(y)<y at even one point).

### Knowledge-base entries to use
- **"Standard inequalities": AM-GM, Cauchy-Schwarz, QM-AM, Schur. Equality
  cases pin down the extremal configuration.** — directly used in steps 1, 3.
- **"Functional equations": test special values, check injectivity/
  surjectivity.** — the x=f(y) substitution is exactly this, sharpened by the
  "make the bound tight" idea.
- **"Linear recurrences": characteristic equation -> closed form.** — used in
  step 2 to solve `y_{n+1}=2y_n-y_{n-1}` and get the arithmetic-progression form
  of iterates.
- No geometry/NT/combinatorics entries apply; this is a pure algebra
  FE-plus-inequality problem.

### Analogous past problems (cruxes)
- **aimo-0008** (Bulgaria, `f(x)f(y)>=f(xy)`, `f(x+y)>=f(x)+f(y)`, prove
  `f=id` given one fixed point `f(a)=a`). Genuinely analogous: two functional
  *inequalities* (not equations) combine to pin down `f=id`, and the key move
  is constructing an argument (`a^n - x`) that makes an upper and lower bound
  coincide exactly, "sandwiching" a value to equality — the same shape of move
  as our x=f(y) collapse. Caution: their answer is a **unique** function under
  an extra hypothesis (`f(a)=a`, `a>1`); our problem has **no such anchor
  hypothesis** and (per step 3) genuinely has a **family** of solutions, so the
  proof will differ in the "now show f is exactly linear" phase — expect this
  problem needs its own family-parametrization argument, not a verbatim copy.
- **aimo-0902** (IMO Shortlist-style, determine smallest constant in
  `((x^{2N}+1)/2)^{1/N} <= a(x-1)^2+x`, answer `a=N/2`). Only tangentially
  related — same QM/root-mean flavor and equality-case-at-a-point technique,
  but it's a single-variable extremal-constant problem, not a two-variable FE.
  Not a strong match; mention only as a secondary source of "how QM identities
  linearize near equality" intuition.
- No stronger match found; searched `domain=algebra`, subtopics
  `functional-equations` and `inequalities-SOS-and-convexity` (263 + many
  cruxes scanned) for "sandwich/squeeze/AM-GM/mean inequality/equality case"
  keywords — nothing else matched the two-sided-QM-AM-GM-with-swapped-argument
  structure of this problem specifically.

### Prior progress
None — workspace was empty (round 1, no approaches yet).

### Dead ends (do not retry)
- Adding the right inequality at (x,y) and (y,x): collapses to the trivially
  true `(f(x)-y)^2+(f(y)-x)^2 >= 0`, carries no new information about f. Don't
  spend a round on this specific combination again.
- Substituting y=f(x) (the "dual" of the main collapse) into either
  inequality, after already knowing `f(f(y))=2f(y)-y`: both reduce to
  `(f(x)-x)^2 >= 0`, again trivial — it's consistent with, but does not extend,
  the step-1 lemma.

### Small-case / intuition notes
- **Numerically verified** (Python, 200000 uniform random (x,y) pairs in
  (0.001, 50) each): `f(x)=x+c` satisfies BOTH inequalities simultaneously for
  every tested `c in {0, 0.5, 1, 2, 5}`, and **fails** for `c=-0.1` only because
  positivity of f is violated for small x (not because the inequality itself
  fails on the sampled positive-image points) — consistent with the algebraic
  proof in step 3 that any `c>=0` works.
- **Conjectured final answer** (pending the necessity gap in step 4):
  `f(x) = x + c` for an arbitrary constant `c >= 0`. This is stronger than a
  single function — the outliner should build the approach as a genuine
  family/characterization proof (prove: (a) every such f works — done, see
  step 3; (b) no other f works — open, step 4 is the gap), not aim for
  "f = id only."
