## imo-2026-05

### IMPORTANT — the expected answer in run_state.md / current.md is likely INCOMPLETE
`run_state.md` says "expected answer f(x)=x", but symbolic + numeric evidence (below) strongly
suggests the true answer is the **whole family f(x) = x + c for any constant c ≥ 0**, not just
c = 0. The outliner should target proving f(x) = x + c (c ≥ 0 fixed) is forced, not f(x) = x.
Flag this to the outliner explicitly so the "solved" bar is set correctly — otherwise a proof of
only f(x)=x will be incomplete (misses the c>0 members) and a proof that stops at "f(x)-x is
bounded/nonneg" without pinning constancy is also incomplete.

### The load-bearing substitution found: x = f(y)
Plug x = f(y) into the double inequality
  sqrt((x²+f(y)²)/2) ≥ (f(x)+y)/2 ≥ sqrt(x f(y)).
- Left radicand becomes (f(y)²+f(y)²)/2 = f(y)², so LHS = f(y) exactly.
- Right radicand becomes f(y)·f(y) = f(y)², so RHS = f(y) exactly.
So the sandwich collapses: f(y) ≥ (f(f(y))+y)/2 ≥ f(y), forcing **equality**:
  **f(f(y)) = 2f(y) − y  for all y > 0.**   (call this (★))
This is clean, exact, and load-bearing — it converts the inequality problem into an honest
functional equation. Verified symbolically (sympy) and it matches f(x)=x (f(f(y))=y=2y-y ✓)
and f(x)=x+c (f(f(y))=y+2c = 2(y+c)-y ✓).

### Consequences of (★) — cheap kills already extracted
1. **Injectivity of f.** If f(a)=f(b), apply f to both sides: f(f(a))=f(f(b)) ⟹ 2f(a)-a =
   2f(b)-b ⟹ (since f(a)=f(b)) a=b. So f is injective — free, from (★) alone.
2. **f(x) ≥ x for all x (lower bound).** Fix y, let y_n = f^n(y) (n-th iterate, well-defined
   since f: R>0→R>0). From (★), y_{n+1} = 2y_n − y_{n-1} for n≥1, i.e. the sequence (y_n) has
   constant first difference: y_n − y_{n-1} = y_1 − y_0 = f(y) − y =: d for all n. Hence
   y_n = y + n·d. Since every y_n must stay positive (f maps into R>0), if d < 0 then y_n → −∞
   and eventually y_n ≤ 0, contradiction. So **d ≥ 0, i.e. f(y) ≥ y for every y.**
   This is a genuine proved bound (not conjecture), modulo double-checking the iterate telescoping
   in the outline (straightforward induction on (★)).
3. **d(f(y)) = d(y)** where d(y):=f(y)−y: from (★), f(f(y))−f(y) = f(y)−y, i.e. d is constant
   along each forward orbit of f. This is the natural handle for the remaining gap (see below).

### The gap this route reaches (hand to outliner)
Substitution x=f(y) alone only pins f along diagonal-type arguments; it shows d(y)=f(y)-y is
≥0 and orbit-invariant, but does NOT by itself show d is a single global constant across
different orbits (different y could a priori have different d(y), unless orbits interact).
**Need a second, cross substitution** using the *general* (x,y) inequality (not x=f(y)) to link
d(x) and d(y) for x,y in different orbits and force d(x)=d(y) for all x,y — i.e. show d is
constant. This is the natural next lemma to target; I did not chase it further (out of scope
for scouting), but candidate moves to hand off:
  - Plug the general right inequality at (x,y) and its swap (y,x) and combine (AM-GM style,
    cf. crux from aimo-0552 below).
  - Try y = x + t (or x = y + t) and expand f(x)=x+d(x) symbolically to get a relation between
    d(x) and d(y) forced by the squared inequality difference (I verified symbolically that for
    f(x)=x+c the two squared differences both collapse to exactly (x−y−c)²/4 ≥ 0 — suggesting
    that in general (x − y − d(y))² type expressions, or similar, are the right object to isolate
    and force d(x)=d(y) via a sharper substitution, e.g. y chosen as x − d(x) or similar).
  - Alternatively use monotonicity: from f(y)≥y and injectivity, try to show f is strictly
    increasing (cf. the aimo-0552 "Lemma 2: f is decreasing" style argument, adapted), then use
    monotonicity + (★) to pin d constant via a squeeze as x,y range over an interval.

### Sub-opening: x=y substitution is a dead end (no info)
Plugging x=y into the original inequality gives exactly the QM(x,f(x)) ≥ AM ≥ GM(x,f(x)) chain,
which is TRUE for every positive x and f(x) unconditionally (standard QM-AM-GM). This yields
**zero constraint on f** — verified symbolically. Do not waste effort here; note it only to warn
future approaches not to expect anything from x=y.

### Sub-opening: y=f(x) substitution — also trivial/tautological
Plugging y=f(x) (mirror of the useful one) makes the *outer* bounds not collapse to a single value
(unlike x=f(y)); working it out symbolically gives, after using x=f(y)-style algebra, the identity
(f(x)²−x²)² ≥ 0, i.e. a tautology — no new information. (This is the "combine (A) and (B)" case
mentioned in scratch computation — always collapses to a perfect square ≥ 0.) Do not pursue this
substitution as primary; x=f(y) is the correct direction, y=f(x) is not.

### Candidate technique(s)
- Convert inequality → exact functional equation via a collapsing substitution (x=f(y)), then
  solve the FE by iteration/telescoping (linear recurrence y_{n+1}=2y_n−y_{n-1} ⟹ arithmetic
  progression ⟹ positivity forces sign of common difference). This is essentially the technique
  "Bootstrap a functional equation into a global affine identity" seen in aimo-0010's cruxes
  (different problem, same iterate-linearization idea).
- AM-GM / QM-AM-GM equality analysis (standard inequalities entry in knowledge_base.md, line 33).
- Once d(x)=f(x)-x is shown ≥0 and orbit-invariant, likely need monotonicity of f + a second
  cross-substitution (general x,y, not the special x=f(y)) to force global constancy of d.

### Cheap-kill candidates
- x=y substitution: automatically satisfied, gives NO constraint — cheap to check, saves time.
- The x=f(y) substitution is the single highest-value cheap move in this whole problem: three
  lines of algebra yield injectivity + f(x)≥x + orbit-invariance of d, essentially for free.
- Perturbation numerics (see below) kill any non-affine candidate immediately — a fast sanity
  filter for any proposed closed form.

### Knowledge-base entries to use
- "Standard inequalities: AM-GM, Cauchy-Schwarz, QM-AM, Schur. Equality cases" (knowledge_base.md
  line 33) — directly the QM-AM-GM chain structure of the problem; equality-case analysis is
  central (the x=f(y) trick is essentially forcing the squeeze to equality).
- "Functional equations: test special values, check injectivity/surjectivity" (line 35) — matches
  exactly what worked here.

### Analogous past problems (cruxes)
- **aimo-0552** (algebra, functional-equations / inequalities-SOS-and-convexity subtopic) —
  "Find all f: R>0→R>0 s.t. for every x there's a UNIQUE y with xf(y)+yf(x) ≤ 2." Answer f(x)=1/x.
  Crux move: apply AM-GM to xf(y)+yf(x) ≥ 2√(xf(x)·yf(y)) to force the unique good pair to be
  x=y itself (equality case), then bootstrap xf(x)≤1 into f(x)=1/x via more substitutions. This
  is the closest structural analog in the corpus: same genre (positive-reals FE pinned via
  AM-GM/QM-AM equality-case forcing, answer determined by where an inequality chain collapses to
  equality). Worth reading in full for the "how do you go from a local equality condition to a
  global pinned function" playbook — but note our problem's equality is forced by construction
  (x=f(y) makes both outer bounds degenerate to the same value), which is a distinctively cleaner
  mechanism than aimo-0552's "uniqueness of good pair" argument, so don't over-copy the mechanics,
  just the overall strategy shape.
- No other close analogs found; searched algebra/functional-equations (263 cruxes) and
  algebra/inequalities-SOS-and-convexity (149 cruxes) subtopics — most hits are pure algebraic FE
  (no inequality-sandwich structure) or pure inequality problems (no unknown function on both
  sides of a squeeze). aimo-0552 is materially the best match; treat others as background only.

### Prior progress
None — this is round 1, current.md is empty/unsolved, no approaches exist yet.

### Dead ends (do not retry)
- x=y substitution (see above): gives the trivial QM-AM-GM chain, true for any f, no constraint.
- y=f(x) substitution (mirror of the useful one): collapses to a tautological perfect square,
  no new information — verified via direct algebra (see above).
- Assuming the answer is *only* f(x)=x (single function): numeric + symbolic evidence contradicts
  this; f(x)=x+c for c≥0 also satisfies both inequalities for ALL x,y (checked with sympy exact
  algebra AND 200,000-sample numeric sweep over x,y ∈ [1e-4,1e4], zero violations for c ∈
  {0,0.5,1,5,100}). Any approach targeting only f(x)=x as the answer will be an incomplete /
  wrong solution — flag prominently to the outliner.

### Small-case / intuition notes (labeled as conjecture except where marked proved)
- **Proved (symbolic):** for f(x)=x+c (c≥0), both inequality-differences reduce EXACTLY to
  (x−y−c)²/4 ≥ 0. This is an exact algebraic identity (sympy `expand` confirms LHS²−mid² and
  mid²−RHS² are both literally (x−y−c)²/4), not numeric-only — strong evidence this is the exact
  answer family, and explains *why* the whole family works: the double inequality is really "the
  same one gap-quantity (x−y−c) squared, twice."
- **Proved (via x=f(y) + telescoping):** f(x) ≥ x for all x, and f is injective.
- **Conjecture (numeric, strong):** f(x) = x + c, c ≥ 0, is the COMPLETE solution set — no other
  functions (verified perturbations of x+c, and multiplicative scalings 1.01x, 1.1x, 2x all fail
  the inequality somewhere in a 200k-sample sweep over 4 decades of x,y).
- Equality in the original double inequality (both QM-AM part and AM-GM part tight simultaneously)
  happens exactly when x − y = c = f(y) − y, i.e. **x = y + (f(y)−y)**, i.e. x = f(y) minus... let
  me restate cleanly: equality throughout ⟺ x − y − d = 0 where d is the (conjectured-constant)
  shift, i.e. x = y + d. This matches x=f(y)=y+d being exactly the collapsing substitution found
  above — consistent picture.
