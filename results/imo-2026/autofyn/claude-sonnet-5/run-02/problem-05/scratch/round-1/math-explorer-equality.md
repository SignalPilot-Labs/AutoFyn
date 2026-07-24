## imo-2026-05

### Distinct openings

1. **[MAJOR FINDING] Equality-forcing substitution `x = f(y)`.** Plug `x = f(y)`
   into the original chain. Then `x^2 = f(y)^2`, so the QM term becomes
   `sqrt((f(y)^2+f(y)^2)/2) = f(y)` and the GM term becomes
   `sqrt(f(y)·f(y)) = f(y)`. The whole chain collapses to
   `f(y) >= (f(f(y))+y)/2 >= f(y)`, forcing **equality**:
   ```
   f(f(y)) = 2f(y) - y   for all y > 0.        (*)
   ```
   This is an *exact* necessary functional equation for every solution — not
   an inequality — obtained purely from the equality case of the sandwich.
   This is the single most useful fact found this round; it should be a
   first-class lemma in the outline.

2. **Orbit/arithmetic-progression consequence of (*).** Writing `y_0=y,
   y_1=f(y), y_2=f(y_1), …`, (*) gives `y_{n+1} = 2y_n - y_{n-1}` for `n>=1`
   (apply (*) at each `y_{n-1}`), i.e. the orbit is an **arithmetic
   progression**: `f^n(y) = y + n(f(y)-y)` for every integer `n>=0`. Since
   `f^n(y) > 0` must hold for *every* `n` (all iterates land in `R>0`), if
   `f(y) < y` the sequence `y + n(f(y)-y) → -∞`, contradiction. Hence:
   ```
   f(y) >= y   for every y > 0.                (necessary)
   ```
   Also from (*), `S(y) := f(y) - y` satisfies `S(f(y)) = S(y)` (S is
   invariant along its own orbit) — this is an *exact* identity, not just an
   inequality, and comes free from (*).

3. **[MAJOR — CORRECTS THE RUN-STATE CONJECTURE] The solution set is a whole
   one-parameter family, not just `f=identity`.** I checked `f(x) = x + c`
   for a *constant* `c >= 0` (not just `c=0`) directly in the original
   inequalities and it works for **every** `c >= 0`. Sympy-verified identity:
   ```
   2x^2 + 2f(y)^2 - (f(x)+y)^2 = (x - y - c)^2   [this is inequality "A" gap]
   (f(x)+y)^2 - 4x f(y)          = (x - y - c)^2   [this is inequality "B" gap]
   ```
   i.e. for the affine family both the QM-side gap and the GM-side gap equal
   the *same* nonnegative square `(x-y-c)^2`. So `f(x)=x+c` satisfies the full
   sandwich for **all** `x,y>0`, for **every** `c ∈ [0,∞)`. `c=0` is only one
   member. **The outliner must characterize `f(x)=x+c, c≥0`, not merely prove
   `f=id`.** (Sanity check `f(f(y))=y+2c=2f(y)-y=y+2c` ✓, `f(y)>=y` ✓ since
   `c>=0`.)

4. **Swap-and-combine (as directed by the lens) is largely vacuous.** Summing
   inequality A(x,y)+A(y,x), or B(x,y)+B(y,x), both collapse via algebra to
   the trivial identity `(x-f(y))^2+(y-f(x))^2 >= 0`, true for *any* function
   f whatsoever — no content. Likewise combining the "A-type" and "B-type"
   inequalities written in terms of `S(x)=f(x)-x, S(y)=f(y)-y` (see below)
   via a natural chain also collapses to a trivial square `((x-y)-S(y))^2>=0`.
   So naive swap+add/combine is a dead end for pinning down S further; the
   real leverage is substitution (opening 1), not symmetrization.

5. **Remaining gap: is S(y):=f(y)-y forced to be a single GLOBAL constant?**
   In terms of `S`, the two original inequalities become (sympy-expanded,
   `Sx=S(x), Sy=S(y)`):
   ```
   (I)  (x-y)^2 + 2Sy(Sy+2y)  >=  Sx(Sx+2x+2y)         [from QM-side]
   (II) (x-y)^2 + Sx(Sx+2x+2y) >= 4·Sy·x               [from GM-side]
   ```
   Combining (I) and (II) the "obvious" way only reproduces the trivial
   `((x-y)-Sy)^2 >= 0` — no new info (checked symbolically). So ruling out
   non-constant `S` needs a sharper argument than naive combination: e.g. an
   **extremal-principle** argument (take `y*` where `S` is minimal/maximal on
   a suitable range, or a supremum/infimum argument), or plugging `x` = a
   point on `y`'s orbit (from opening 2) into (I)/(II) with a *third*,
   unrelated point to cross-link different orbits. This is the actual
   remaining crux of the problem — everything else above is essentially free.

### Candidate technique(s)
- **Equality-case forcing in a QM/AM/GM-type sandwich** (knowledge_base.md:
  "Standard inequalities... equality cases pin down the extremal
  configuration") — this is exactly opening 1, and it is the crux move.
- **Telescoping / arithmetic-progression-of-iterates + positivity bound**
  (opening 2) — directly analogous to the crux technique in `aimo-0710` (see
  below): use a forced recursion on iterates `f^n` together with positivity
  of the codomain to force a global identity.
- **Extremal principle** (knowledge_base.md "Pigeonhole / extremal
  principle"; Pólya "specialize") to finish opening 5: take sup/inf of `S`.
- Standard AM-GM/QM-AM equality analysis (knowledge_base.md "Standard
  inequalities").

### Cheap-kill candidates
- The substitution `x=y` in the original inequality is **completely
  vacuous**: it reduces to plain QM-AM and AM-GM applied to `(x, f(x))`,
  both always true regardless of `f`. Any approach relying on `x=y` alone
  gives zero information — flag this so no approach wastes a round there.
- `f(x) = c/x` fails immediately (checked `x=2,y=1,c=1`: GM bound
  `sqrt(x f(y)) = sqrt(2) ≈1.414 > middle = 0.75`), so this family is not a
  candidate — no need to re-derive.

### Knowledge-base entries to use
- "Standard inequalities: AM-GM, Cauchy-Schwarz, QM-AM, Schur. Equality cases
  pin down the extremal configuration." (Algebra & Polynomials section) —
  directly cites the equality-forcing move.
- "Functional equations: test special values, check injectivity/
  surjectivity." — the `x=f(y)` substitution is exactly this in sharpened
  form.
- "Induction / infinite descent" (General Proof Methods) — relevant to the
  arithmetic-progression-of-iterates argument (opening 2), which is an
  infinite-descent-flavored positivity bound.
- "Pigeonhole / extremal principle" — candidate tool to finish opening 5.

### Analogous past problems (cruxes)
- **`aimo-0710`** (algebra, functional-equations; ISL-style, "Belgium"):
  `x(f(x)+f(y)) >= (f(f(x))+y)f(y)` on `R>0`, answer `f(x)=c/x`. **Strongly
  analogous in technique**: the official solution derives `f(f(x)) <= x` from
  `y=x`, then a *shifted* substitution `x=f(y)` producing a one-step
  inequality on iterates, generalizes it to `f^n(y)-f^{n+2}(y) >= f^{n-1}(y)
  - f^{n+1}(y)` for all `n`, and telescopes a sum of `m` non-negative equal
  (or increasing) terms against the fixed bound `y > y - f^{2m}(y)` to force
  `m·(nonneg quantity) < y` for all `m`, hence the quantity is **exactly 0**.
  This is *precisely* the telescoping-positivity-forces-equality trick that
  proves our `f(y) >= y` bound (opening 2) is tight in spirit, though here we
  got equality (*) directly from a single substitution rather than needing
  the telescoping sum — worth double-checking whether the telescoping trick
  is still needed to finish opening 5 (ruling out non-constant `S`).
- Nothing else in the algebra/functional-equations or
  inequalities-SOS-and-convexity subtopics that I found genuinely resembles
  a *three-way sandwich of QM/AM/GM* forcing a functional identity; the rest
  of the `f(x)f(y)`-style browse (`aimo-0008`, `aimo-0552`, `aimo-0991`, etc.)
  are single-inequality (not sandwich) FE's with different mechanisms —
  listed but not close analogues.

### Prior progress
None — fresh workspace, first round.

### Dead ends (do not retry)
- **`x=y` substitution**: gives QM-AM / AM-GM on `(x,f(x))`, always true for
  any `f`, zero content. (Verified directly: both reduce to standard
  inequalities independent of the functional constraint.)
- **Summing A(x,y)+A(y,x) or B(x,y)+B(y,x)** (swap-and-add): both collapse
  algebraically to the trivial `(x-f(y))^2+(y-f(x))^2 >= 0`, true for any
  function `f: R>0 -> R` whatsoever (not even positivity needed). No content.
- **`f(x) = c/x`**: fails the GM-side inequality (numeric counterexample
  `x=2,y=1,c=1` above). Not a solution family.
- **Combining inequalities (I) and (II) above (in `Sx,Sy` form) via direct
  substitution**: collapses to `((x-y)-Sy)^2 >= 0`, trivial, no new
  constraint on `S`. A sharper combination (extremal, not algebraic-identity)
  is needed.

### Small-case / intuition notes (conjecture)
- **Numerically very strong evidence** (grid search over `x,y ∈
  [10^-4,10^4]`, `2000×2000` and geomspace grids) that the *only* solutions
  are `f(x) = x + c` for a single fixed constant `c >= 0` (uniform across all
  `x`): constant `S(y)=c` always gives `A=B=(x-y-c)^2>=0` exactly (verified
  symbolically, not just numerically). A **non-constant** `S` — tested as a
  step function (`S=1` for `y<5`, `S=3` for `y>=5`) and as a slowly
  increasing linear perturbation (`S(y)=1+0.001y`) — **numerically violates**
  inequality A (found `minA` strongly negative, e.g. `-56` for the step
  function at `(x,y)=(8,5)`, and `-0.083` even for the tiny linear slope
  `0.001`), i.e. even an arbitrarily small non-constant deviation appears to
  break the inequality somewhere. This is conjecture (numeric), but very
  strong — I recommend the outliner's target claim be **`f(x)=x+c` for an
  arbitrary constant `c ∈ [0,∞)`** (verify: works ⟺ `c>=0`; conjectured
  necessary, with (*) and `f(y)>=y` already *proved* necessary conditions,
  and "S constant" as the one remaining gap to close, likely via an
  extremal/sup-inf argument on `S` using inequalities (I)/(II) above at a
  near-extremal point, or by re-deriving the telescoping trick from
  `aimo-0710` applied to differences `S(x)-S(y)` instead of `y-f^2(y)`).
