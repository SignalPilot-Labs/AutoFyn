## imo-2026-05

### MAJOR CORRECTION TO run_state.md ASSUMPTION
`run_state.md` says "Likely answer: f(x)=x, to be proven." **This is wrong / incomplete.**
Algebra and numerics (below) show the true solution set is the whole family
**f(x) = x + c for every constant c ≥ 0** (f(x)=x is just the c=0 member). The
"characterization" answer_type fits a family, not a single function. Flag this to
the outliner immediately — do not let any approach target only f(x)=x as the answer.

### Setup / notation
Write the two given inequalities as:
- **L(x,y):** `x² + f(y)² ≥ (f(x)+y)²/2` (from `sqrt((x²+f(y)²)/2) ≥ (f(x)+y)/2`)
- **R(x,y):** `f(x) + y ≥ 2√(x f(y))` (from `(f(x)+y)/2 ≥ sqrt(x f(y))`)
both must hold for **all** x,y > 0.

### Distinct openings (this lens: structural bounds/shape)

1. **Exact hidden identity via the diagonal substitution x = f(y).**
   Plug `x := f(y)` into R: `f(f(y)) + y ≥ 2f(y)`, i.e. `f(f(y)) ≥ 2f(y) − y`.
   Plug `a := f(y), b := y` into L: `f(y)²+f(y)² ≥ (f(f(y))+y)²/2` ⟹ `2f(y) ≥ f(f(y))+y`,
   i.e. `f(f(y)) ≤ 2f(y) − y`.
   **Combined: `f(f(y)) = 2f(y) − y` exactly, for every y > 0.** This is a fully rigorous
   lemma (no affine assumption needed) — the single most valuable structural fact found.
   Consequence: with `e(y) := f(y) − y`, `e(f(y)) = e(y)` — e is **invariant along the
   forward orbit of f**, and by induction `fⁿ(y) = y + n·e(y)` for all n ≥ 0 (an exact
   arithmetic progression along each orbit).

2. **Bootstrap lower bound `f(y) ≥ y` for ALL y** (rigorous, not conjectural).
   From `f(f(y)) ≤ 2f(y) − y` and `f(f(y)) > 0`, get `f(y) > y/2` (base case).
   Inductive amplification: if `f(t) > c·t` holds for all t (c ∈ (0,1]), apply it at
   `t = f(y)`: `f(f(y)) > c·f(y)`; combine with `f(f(y)) ≤ 2f(y) − y` to get
   `f(y) > y/(2−c)`. This gives the recursion `c_{n+1} = 1/(2−c_n)`, `c_0 = 1/2`,
   which is strictly increasing with fixed point `c=1` (solves `(c−1)²=0`), so `c_n → 1`.
   Taking the limit over all n (each n gives a valid bound for every y simultaneously):
   **`f(y) ≥ y` for all y > 0.** This is the same "amplify a lossy bound by iterating it
   through itself" move as crux `aimo-0008` (see below) — direct structural analog.

3. **Algebraic verification that f(x) = x + c satisfies BOTH inequalities exactly, for
   every real c, wherever f stays positive.**
   Direct computation (verified by hand and by sympy/numeric check):
   `R-difference := (f(x)+y)² − 4x f(y) = ((x−y) − c)²` (always ≥ 0, equality iff y = x−c).
   `L-difference := x²+f(y)² − (f(x)+y)²/2 = ((x−y) − c)²/2` (same zero set).
   So **for every c, both inequalities hold with equality exactly on the line y = x − c**,
   and strictly elsewhere. The domain constraint `f: R_{>0} → R_{>0}` forces `x+c>0` for
   *all* x>0, i.e. **c ≥ 0** (c<0 fails only because of the codomain positivity
   requirement as x→0+, not because the inequality itself fails — confirmed numerically:
   plugging in c<0 and restricting x,y to a region where f stays positive still satisfies
   the inequality with margin ≈ 0, i.e. an exact identity, consistent with the algebra
   above holding for any real c). **This nails down the achievability half of the
   characterization: {f(x)=x+c : c ≥ 0} all work.**

4. **Numerical evidence that only constant shifts work (non-constant e(x) fails).**
   Tested `f(x) = x + [1 if x≤5 else 2]` (step shift), `f(x) = x + min(x,1)`, and
   `f(x) = x + √x` against both inequalities over random (x,y) in [0.001,50]²
   (300k trials each): **all three violate L** (found strictly negative margins, e.g.
   step shift violates L at x≈5.33, y≈4.33 with margin ≈ −0.5). This is strong
   (non-proof) evidence that `e(x) = f(x) − x` must be a GLOBAL CONSTANT, not merely
   constant along each orbit (which is all Lemma 1 by itself gives).

### Candidate technique(s)
- The **diagonal substitution `x=f(y)` fed into both given inequalities simultaneously**
  to squeeze an exact functional identity `f(f(y))=2f(y)−y` out of a pair of one-sided
  inequalities — this is the crux move to build on.
- **Iterative/bootstrap amplification** of a weak bound into a tight one by feeding the
  bound back through itself (matches `aimo-0008`'s technique exactly).
- **Orbit/displacement invariant** `e(f(y))=e(y)` plus a cross-orbit argument (comparing
  `e` at two different starting points, e.g. via L or R evaluated at non-diagonal pairs
  `(y1, y2)` from different orbits) is very likely the remaining gap to close: showing
  `e` is the SAME constant across all orbits, not just within one. This is where the
  proof still needs work — no clean closed-form cross-orbit argument was found in this
  pass; candidates to try next round: monotonicity of f (if provable) forces orbits to
  be order-preserving, and two orbits with different slopes `e1 ≠ e2` would eventually
  cross or diverge in a way that contradicts `f` being single-valued/order-consistent —
  sketch only, not verified.

### Cheap-kill candidates
- **x=y substitution gives NO information** — both L(x,x) and R(x,x) reduce to
  QM-AM and AM-GM of `x` and `f(x)`, which are unconditionally true for any positive
  reals, so setting x=y never constrains f. Flag as a dead end so no approach wastes a
  round on it.
- **Combining L(x,y) and R(x,y) directly at the same (x,y) is a tautology.**
  Squaring R and comparing to L's rearrangement gives `4x f(y) ≤ (f(x)+y)² ≤ 2(x²+f(y)²)`,
  which reduces exactly to `(f(y)−x)² ≥ 0` — always true, no constraint on f. Real
  information only comes from substitutions where the two inequalities are evaluated at
  *different* linked points (e.g. the diagonal `x=f(y)` trick above).

### Knowledge-base entries to use
- **Standard inequalities (AM-GM, QM-AM)** — knowledge_base.md "Algebra & Polynomials":
  used to recognize the two given inequalities as disguised QM-AM (L) and AM-GM (R) with
  equality iff the two entries are equal; explains why x=y is always satisfied.
- **Functional equations: test special values, injectivity/surjectivity** — general
  heuristic entry, applies to the `x=f(y)` substitution.
- **Meta-Strategy: check small cases / specialize** — informed the numeric family search.

### Analogous past problems (cruxes)
- **`aimo-0008`** (Bulgaria, functional inequality on Q>0: `f(x)f(y)≥f(xy)`,
  `f(x+y)≥f(x)+f(y)`, `f(a)=a` for some rational `a>1` ⟹ `f=id`). **Best analog found.**
  Crux move: "amplify a lossy additive bound `f(x) > x−c` by feeding a power of the
  argument through the same bound and taking the n-th root, so the constant error
  shrinks to 0," and "convert a one-sided bound into equality by sandwiching against a
  known exact value at a large point." Directly mirrors the bootstrap `c_n → 1`
  amplification found here (opening 2), and the general "squeeze two one-sided bounds
  from two different hypotheses into an exact identity at a well-chosen point" pattern
  (opening 1). Note aimo-0008's answer is a genuinely UNIQUE function (`f=id`) despite a
  similar-looking inequality skeleton — the extra hypothesis `f(a)=a` for one point is
  what kills the multi-parameter family there; our problem has no such extra hypothesis,
  consistent with our finding of a whole family of solutions instead of a single one.
- **`aimo-0010`** (Serbia, `f(f(f(n)))=f(n+1)+1`) and **`aimo-0051`** (nested iterate
  displacement `Δ(m,n)`): both use an "orbit / iterate displacement is invariant or
  grows" style argument analogous to our `e(f(y))=e(y)` orbit-invariance (opening 1's
  consequence), but on integer domains via induction on iterate depth — less directly
  transferable to our continuous domain, but worth reading if the outliner wants to
  adapt the "iterate the identity to get an arithmetic progression, then derive a
  contradiction from unboundedness" pattern.
- No crux found that produces a **multi-parameter family** answer for a two-sided
  sandwich inequality exactly like this problem — the "prove f = x+c family" half
  (showing e is globally constant) has no close analog in the sampled corpus; this is
  likely genuinely novel casework for the outliner to construct directly from openings
  1–4 above.

### Prior progress
None — round 1, empty population (`results/imo-2026-05/approaches/` and `lemmas/` both
empty, no `current.md` yet).

### Dead ends (do not retry)
- Setting x=y in either inequality: gives only AM-GM/QM-AM tautologies, no information
  about f (see Cheap-kill candidates above).
- Directly combining L(x,y) and R(x,y) at the same generic (x,y): collapses to
  `(f(y)−x)²≥0`, a tautology — do not present this as if it were progress.
- Do NOT let any approach aim to prove uniquely `f(x)=x` — this is FALSE per opening 3;
  the correct target is the family `f(x)=x+c, c≥0`.

### Small-case / intuition notes (labeled conjecture except where proven above)
- **Proven:** `f(f(y)) = 2f(y) − y` for all y (opening 1).
- **Proven:** `f(y) ≥ y` for all y (opening 2, via bootstrap limit argument).
- **Proven (algebra + confirmed numerically):** `f(x)=x+c` satisfies both inequalities
  exactly for every real c on the domain where `f>0`; codomain positivity forces `c≥0`.
- **Conjectured (strong numeric evidence, not proven):** these constant shifts are the
  ONLY solutions — i.e. `e(x)=f(x)−x` is forced to be a single global constant. Tested
  three qualitatively different non-constant shift functions (step, min-clamped, sqrt);
  all three violate the L inequality somewhere. The remaining gap for the outliner is a
  rigorous cross-orbit argument forcing `e` constant (see "Candidate technique(s)" above
  for a monotonicity-based idea, unverified).
- The answer_type field is `characterization`, consistent with a parametrized family
  rather than a single function — further supports that {f(x)=x+c : c≥0} (not just
  f(x)=x) is the problem's actual intended answer.
