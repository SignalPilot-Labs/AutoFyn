## imo-2026-05

**Conjectured answer (strong, with full verification):** `f(x) = x + c` for an arbitrary constant `c >= 0`. Both inequalities reduce to the identity `(x - y - c)^2 >= 0` (verified symbolically: `L_expr = R_expr = (x - y - c)^2`). `c >= 0` is forced by `f: R_{>0} -> R_{>0}` (positivity of all forward iterates; see below). The constant-family diagnostic and the global argument both close cleanly from the scaling/involution lens; the "involution" framing is a TRAP here (the iterate is a translation, not an involution, except at c=0).

### Distinct openings (each a different attack the outliner could build into a rival approach)

1. **The x = f(y) specialization (the kill-shot).** This is THE crux of the problem and the cleanest route. Setting `x = f(y)` makes BOTH inequalities tight simultaneously: the left gives `f(f(y)) <= 2f(y) - y`, the right gives `f(f(y)) >= 2f(y) - y`, forcing the iterate identity `f(f(y)) = 2f(y) - y`. This single substitution carries the whole problem (injectivity, the iterate recurrence, g >= 0, orbit invariance). The outliner should anchor one approach entirely on this specialization.

2. **The iterate-recurrence + positivity route.** From `f(f(y)) = 2f(y) - y`, the iterate `u_n = f^n(y)` satisfies `u_{n+2} = 2u_{n+1} - u_n` (characteristic `(r-1)^2`), so `f^n(y) = y + n(f(y) - y)`. Positivity of every forward iterate forces `g(y) := f(y) - y >= 0` (else `f^n(y) -> -inf`). Injectivity is free (`f(a)=f(b)` => `f(f(a))=f(f(b))` => `2f(a)-a = 2f(b)-b` => `a=b`). The iterate identity rewrites as `g(y + g(y)) = g(y)`: **g is constant on each forward orbit** `{y + n g(y)}`. This is the analogue of aimo-0010's "compute one higher iterate two ways."

3. **The algebraic-rearrangement / Lipschitz-bound route.** Write `L_expr = 2(x^2 + f(y)^2) - (f(x)+y)^2`, `R_expr = (f(x)+y)^2 - 4 x f(y)`, `S(t) = t + f(t) = 2t + g(t)`. Then:
   - `L_expr + R_expr = 2(x - f(y))^2` (trivial square — gives nothing alone);
   - `L_expr - R_expr = 2(g(y) - g(x))(S(x) + S(y))`.
   Since both `L_expr, R_expr >= 0`, we get the **key bound** `|g(x) - g(y)|(S(x) + S(y)) <= (x - f(y))^2 = (x - y - g(y))^2`, and symmetrically (evaluating at `(y,x)`) `<= (y - x - g(x))^2`. This is the load-bearing inequality for the global step.

4. **The continuity-then-connectedness route (closes the parametric-to-global gap).** Prove `g` is continuous:
   - At a zero `b` (`g(b)=0`): the bound with `y=b` gives `g(b+h) <= h^2/(4b) -> 0`.
   - At a non-zero `a` (`g(a)=alpha>0`): the bound with `y=a` gives local boundedness `g(a+h) in [alpha - alpha^2/(4a+alpha), alpha + ...]`, then the symmetric bound forces `g(a+h) -> alpha`.
   Then extract `lim_{a->inf} g(a) = L`: fix `b` with `g(b)=beta>0`, use `y = b + m*beta` (orbit point, `g(y)=beta`) in the key bound with `x=a`, choosing integer `m` so `y + beta ~ a` within `beta/2` (Dirichlet/AP-approximation). Then `|g(a) - beta|(S(a)+S(y)) <= (beta/2)^2`, and `S(a)+S(y) ~ 4a -> inf`, so `g(a) -> beta`. So `L = beta`.
   Finally: any `y0` with `g(y0)=delta>0` has orbit `-> inf` with `g=delta`, forcing `delta = L`. So `g` takes values in `{0, L}`. By continuity + connectedness of `R_{>0}` (level sets `{g=0}`, `{g=L}` are clopen), `g` is constant: `g equiv 0` or `g equiv L`. Done.

5. **Power-function diagnostic (cheap-kill confirmation, not a proof).** `f(x)=x^a` forces `a=1` from EACH inequality independently (asymptotics with `y = x^b`, all `b`). `f(x)=cx` forces `c=1` (right inequality automatic = `(cx-y)^2>=0`; left inequality's quadratic in `t=x/y` has discriminant `2(c^2-1)^2`, forcing `c=1`). `f(x)=ax+b` (general affine): left inequality's discriminant (as quadratic in `x`) has `y^2`-coefficient `8(a^2-1)^2 >= 0`, which is `>0` for `a != 1`, making the discriminant positive for large `y` — so `a=1`. With `a=1`, both inequalities become `(x-y-b)^2>=0`. So among affine/power maps, exactly `f=x+c, c>=0`. This is strong circumstantial evidence but NOT a proof for arbitrary `f`.

### Candidate technique(s)
- **Specialize the free variable to the image of the other** (`x = f(y)`) — turns a two-sided sandwich into a pair of equalities, pinning an iterate. This is the single load-bearing move.
- **Iterate-linear-recurrence + forward-orbit positivity** to get `g >= 0` and orbit invariance.
- **Algebraic sum/difference of the two squared inequalities** to extract a Lipschitz-type bound (the `L+R` trivial square + `L-R` factorization).
- **AP-approximation (Dirichlet) + limit at infinity** to upgrade a pointwise bound to a global limit.
- **Continuity + connectedness** to finish (value set provably finite => constant).

### Cheap-kill candidates
- **Power/affine ansatz plug-in** (done): immediately rules out everything except `f=x+c`, `c>=0`. Cheap and decisive as a *diagnostic*, but not a proof.
- **The `x = f(y)` substitution** itself is a one-move structural kill — it costs nothing and yields the iterate identity that drives the whole proof.
- **Sum `L_expr + R_expr`**: one-line observation that the sum is a trivial square, localizing all the content into the difference `L_expr - R_expr`.

### Knowledge-base entries to use
- **Functional equations** (Algebra & Polynomials): "test special values, check injectivity/surjectivity" — directly, `x=f(y)` is the special value; injectivity follows from the iterate identity.
- **Standard inequalities: AM-GM, Cauchy-Schwarz, QM-AM, Schur. Equality cases pin down the extremal configuration.** — the problem IS a QM-AM-GM sandwich; the solution family is exactly the equality-configurations of the chain `(x, f(y))` shifted.
- **SOS / completing the square** — `L_expr + R_expr = 2(x - f(y))^2` is the SOS rewrite that localizes the content.
- **Pólya heuristics: Specialize (plug in extreme/symmetric values); Introduce a substitution; Find a related problem.**
- **General Proof Methods: Contradiction / connectedness** for the final clopen-level-set step.

### Analogous past problems (cruxes)
- **`aimo-0253` (IMO-SL 2009 FRA, triangle inequality FE)** — crux: "Specialize the free variables so the triangle/inequality constraint pins a composite value to the identity, yielding an involution identity" (`f(f(z))=z`), then "iterate a contractive growth bound to contradict the involution for large arguments." THIS is the closest analog: same shape (specialize to make a sandwich tight => pin an iterate => derive growth bounds => force equality). Difference: there the iterate is an involution; here it is a translation `f(f(y))=2f(y)-y` (displacement `g(y)>=0`), so the "involution" target is wrong — the correct target is the iterate being a translation by the displacement.
- **`aimo-0234` (USAMO 2023, `f(xy+f(x))=xf(y)+2`)** — crux: "Sandwich a monotone unknown between floor/ceil step-functions from an additive shift relation" + "Substitute the approximate closed form back into the FE and drive a free variable to infinity so the bounded error is dominated, forcing the coefficient to vanish." Analogous to our step 6 (send `a -> inf` to kill `|g(a)-beta|` against the growing `S(a)+S(y)`).
- **`aimo-0008` (IMO-SL 2013, superadditive+submultiplicative FE)** — crux: "Amplify a lossy additive bound `f(x) > x-c` by feeding a power through and taking the n-th root, so the constant error becomes negligible" — the same "amplify a small error to a sharp bound by iterating/sending to infinity" spirit as our orbit-approximation + limit step.
- **`aimo-0010` (iterates FE on `Z`)** — crux: "Compute one higher iterate two ways and equate to collapse a composition into a shift-recurrence" + "Once an iterate equals translation by a constant, apply the base function to show it commutes with the shift." Directly analogous to deriving `f^n(y) = y + n g(y)` from `f(f(y)) = 2f(y) - y`.

### Prior progress
Round 1, no prior approaches. The exploration above establishes the full conjectured answer `f(x) = x + c, c >= 0` with a complete candidate proof structure (iterate identity -> g>=0 + orbit invariance -> key Lipschitz bound -> continuity + limit-at-infinity -> connectedness), all numerically and symbolically verified. No gaps remain that I can identify; the outliner should still rigorously verify the continuity-at-nonzero-point step and the connectedness/clopen argument.

### Dead ends (do not retry)
- **Involution framing** (`f(f(x)) = x`): FALSE for this problem. The iterate identity is `f(f(y)) = 2f(y) - y` (a translation by `g(y)`), which equals `y` only when `g(y)=0` (i.e., `c=0`). Building an approach around proving involution will fail for `c > 0`. (Confirmed: `f(x)=x+c` has `f(f(x)) = x+2c != x`.)
- **Scaling f(x) = cx**: only `c=1` survives (left inequality's discriminant forces it). So any approach asserting a homogeneous scaling family is wrong.
- **Power functions f(x) = x^a**: only `a=1`. Same lesson.
- **"Natural sufficient condition" trap**: the right inequality is automatic if `f(x)/x` is constant; the left if `f(x)-x` is constant. Both hold ONLY for `f=x`. But the actual family `f=x+c` satisfies NEITHER sufficient condition (for `c>0`), so the inequalities are genuinely weaker than the AM-GM/QM-AM equality conditions — do NOT assume equality-configuration is necessary.
- **Step-function / piecewise-constant `g`** (e.g. `g=0` near a point, `g=L` far away): numerically FAILS (worst violation grows with `L`); the continuity + connectedness argument rules them out. Don't try to construct non-constant `g`.

### Small-case / intuition notes (conjectures, labeled)
- `f(x)=x+c` (any `c>=0`) is a verified solution family (both inequalities = `(x-y-c)^2 >= 0`). CONJECTURE: this is the COMPLETE family.
- The problem has a **scaling symmetry** `g_k(x) = k·f(x/k)`: if `f` is a solution, so is `k·f(·/k)`. Under this, `f=x+c` maps to `x+kc`. So the family is one scaling-orbit plus the isolated fixed point `f=x` (`c=0`). Scaling CANNOT classify on its own (it fixes `c=0` and is transitive on `c>0`); the global argument is still needed.
- `x = f(y)` is the unique substitution that makes the sandwich tight (both bounds equalities); `y = f(x)` gives only the tautologies `(f(x)-x)^2 >= 0`. So `x = f(y)` is the load-bearing specialization, not `y = f(x)`.
- The iterate `f^n(y) = y + n·g(y)` means the forward orbit is an arithmetic progression with step `g(y)`; this is the structural reason AP-approximation (Dirichlet) enters the global step.
- Numerical probes of non-constant `g` (step, ramp, `sqrt`, `ln`, linear) all FAIL the original inequalities; only constant `g` survives. Evidence, not proof.

### Single hardest gap (now closed, but flag for outliner verification)
The parametric-to-global bridge. The cheap part: `x=f(y)` gives the iterate identity for free. The hard part: from "g constant on each forward orbit" to "g globally constant." The closure route is: (i) prove `g` continuous via the key bound, (ii) prove `lim_{a->inf} g(a) = L` via AP-approximation of `a` by an orbit point `b + m·beta` (Dirichlet spacing `<= beta/2`) and sending `a -> inf` so `S(a)+S(y) ~ 4a` kills the residual `|g(a)-beta|`, (iii) finish by connectedness of `R_{>0}` once `g` is continuous with value set `subseteq {0, L}`. The continuity-at-a-nonzero-point sub-step (boundedness from `(*)` then `(**)` forces `g(a+h)->alpha`) and the clopen-level-set connectedness argument are the two places the outliner must check rigor most carefully.

Report written to /tmp/round-1/math-explorer-scaling-involution.md
