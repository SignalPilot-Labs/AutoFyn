## imo-2026-05

Target (whole problem): prove the full characterization — every `f: R_{>0} -> R_{>0}` satisfying
`sqrt((x² + f(y)²)/2) >= (f(x)+y)/2 >= sqrt(x f(y))` for all `x,y>0` is exactly `f(x) = x + c` for some constant `c >= 0`.

Shared cheap kill (used by every approach, recorded here once): the diagonal specialization `x = f(y)` collapses the QM-AM-GM sandwich (the pair `(x, f(y))` becomes equal, so QM=AM=GM) and forces, with no computation,
`(C1)  f(f(y)) = 2f(y) - y  for all y>0.`
Writing `g(y) := f(y) - y` (the displacement), this is `g(f(y)) = g(y)`; iterating, `f^n(y) = y + n·g(y)` and `g` is constant on each forward orbit. Positivity of every forward iterate (`f^n(y) ∈ R_{>0}`) forces
`(C2)  g(y) >= 0  for all y>0  (else y + n·g(y) < 0 for large n).`
So `f(y) >= y` everywhere. This much is FORCED and FREE; it is necessary, not sufficient (nonconstant orbit-invariant `g` satisfy C1+C2 but fail the full inequality). The whole open problem is the **global constancy of `g`**.

Construction (shared, already rigorous): for `f(x) = x + c`, `c >= 0`, the middle term `A = (x+y+c)/2` is the AM of the pair `(x, y+c)`; the left inequality is QM>=AM and the right is AM>=GM on that pair, both holding since `x>0, y+c>0`. `c >= 0` is forced by the codomain (`f(x) = x+c > 0` for all `x>0` iff `c >= 0`). Verified. So **once `g` is constant, the problem is solved.**

---

### diagonal-diophantine-kill: new
Technique: SOS sign-decomposition of the two squared inequalities producing a single master bound, then a two-forward-orbit Diophantine kill (Dirichlet density for irrational displacement ratios, exact-zero Frobenius construction for rational ratios).
Skeleton:
  1. Square both inequalities: `L := 2(x²+f(y)²) - (f(x)+y)² >= 0`, `R := (f(x)+y)² - 4x f(y) >= 0`. — by algebra / completing the square.
  2. Compute the two identities `L+R = 2(x - f(y))²` (trivial square) and `L−R = 2(g(y) − g(x))·(x + f(y) + f(x) + y) = 2(g(y)−g(x))·(2x+2y+g(x)+g(y))`. — direct expansion, using `f(t)=t+g(t)`.
  3. Since both `L,R >= 0`, their sum and difference are bounded: obtain the master bound `(★)  (x − y − g(y))² >= |g(x) − g(y)|·(2x + 2y + g(x) + g(y))` for all `x,y>0`. — because `L,R>=0` iff `|L−R| <= L+R`, i.e. `2|g(y)−g(x)|·(S) <= 2(x−f(y))²`.
  4. Apply the cheap kill (C1)+(C2) to get `g>=0` and orbit-invariance `g(y + n·g(y)) = g(y)` for all `n>=0`. — by the shared diagonal collapse.
  5. Suppose `g` is not constant; pick `a,b` with `0 <= d1 := g(a) < d2 := g(b)`. Evaluate `(★)` at `x = a + n·d1`, `y = b + m·d2` (both on their forward orbits, so `g(x)=d1, g(y)=d2`). LHS `= (a − b + n·d1 − (m+1)·d2)²`, RHS `= (d2−d1)·(2(a+nd1) + 2(b+md2) + d1 + d2) ~ (d2−d1)·(2n·d1 + 2m·d2)`.
  6. Irrational case `d1/d2 ∉ Q`: `{n·d1 − (m+1)·d2 : n,m >= 0}` is dense in R (Kronecker/Dirichlet), so along a sequence with `n,m → ∞` the LHS stays bounded (near `(a−b)²`) while RHS → ∞. Contradiction with `(★)`. — by Dirichlet simultaneous approximation.
  7. Rational case `d1/d2 = p/q` (lowest terms, `p<q`): take `n = kq, m = kp−1` (valid since `p>=1`); then `n·d1 − (m+1)·d2 = 0` exactly, LHS `= (a−b)²` constant, RHS grows linearly in `k`. Contradiction for large `k`. — by the Frobenius/exact-zero lattice point.
  8. Edge case `d1 = 0 < d2`: a coarse parabola bound (sum the two orbit parabolas; `(★★)  2(x+y)(d2−d1) <= (d1+d2)(5d1−3d2)/4` gives RHS < 0 < LHS) kills it directly. — by bounding the quadratic-minus-linear growth. [GAP: verify the (★★) bound rigorously — explorer states it; needs a clean derivation.]
  9. All cases contradict, so no two unequal displacements coexist: `g` is constant. Finish with the shared construction.
Key lemmas (claim + mechanism):
  - The `(L+R, L−R)` identities — because expanding `(f(x)+y)²` and collecting by `g(x), g(y)` makes the cross term `g(x)−g(y)` factor out of `L−R` while `L+R` is the pure square `2(x−f(y))²`. This is the actual crux: two inequalities become one signed identity.
  - Irrational-ratio density on the nonneg grid — because the additive semigroup `{n·d1 − m·d2 : n,m >= 0}` with `d1/d2` irrational is dense in R (Kronecker in one dimension).
  - Rational-ratio exact zeros — because at `d1/d2 = p/q` the lattice point `(n,m) = (kq, kp−1)` lands the linear combination exactly on 0, freezing LHS while RHS grows.
  - Positivity-forced `g>=0` — because `f^n(y) = y + n·g(y)` must stay positive for all `n`, impossible if `g(y)<0`.
Open gaps: the edge-case parabola bound `(★★)` needs a clean proof; the density-on-`Z_{>=0}^2` claim (irrational case) needs the precise Kronecker reference (not full multidimensional, just 1-D inhomogeneous approximation, but the nonneg restriction on `n,m` must be checked — it is fine because the approximation can be taken with arbitrarily large positive coefficients); the (★★) coarse bound must not silently assume `d1>0`.
Cases to cover: (i) `0 < d1 < d2`, `d1/d2` irrational; (ii) `0 < d1 < d2`, `d1/d2 = p/q` rational; (iii) `d1 = 0 < d2`.
Watch out for: the nonneg-restriction on `n,m` in the density argument (use the version of Kronecker that produces arbitrarily large positive coefficients — standard); the `p=0` impossibility (p<q lowest terms with p>=1 since d1>0 in case (ii)); the master bound (★) being applied with `g(x)=d1, g(y)=d2` exactly, which holds only on the orbit points — make sure `x = a+nd1, y = b+md2` are indeed orbit points carrying `g=d1, d2` (true by C1 invariance).

### lipschitz-connectedness: new
Technique: Read the master bound (★) as a pointwise Lipschitz/Hölder estimate for `g`; use it to prove `g` is continuous; extract the limit `L = lim_{t→∞} g(t)` via AP-approximation of `t` by an orbit point (Dirichlet spacing); finish by connectedness of `R_{>0}` once the value set is provably contained in `{0, L}`.
Skeleton:
  1. Derive the master bound `(★)  |g(x) − g(y)|·(2x+2y+g(x)+g(y)) <= (x − y − g(y))²` for all `x,y>0` — by the same `(L+R, L−R)` sign-decomposition as approach 1 (steps 1–3). [Shared lemma; can be imported once certified.]
  2. Apply the cheap kill (C1)+(C2) for `g>=0` and orbit-invariance. — shared diagonal collapse.
  3. Prove continuity of `g` at every point.
     - At a zero `b` (`g(b)=0`): put `y=b` in (★): `g(b+h)·(2(b+h)+2b+g(b+h)) <= h²`, hence `g(b+h) <= h²/(4b+h-b+...)` — in particular `g(b+h) <= h²/(4b)` for small `h`, so `g(b+h) → 0 = g(b)`. — by the bound with denominator `~ 4b`.
     - At a nonzero point `a` (`g(a)=α>0`): first local boundedness `g(a+h) ∈ [α − α²/(4a+α), α + ...]` from (★) with `y=a`; then the symmetric bound (★) with roles swapped forces `g(a+h) → α`. [GAP: the explorer asserts this; the rigging of the two-sided squeeze at a nonzero point is the delicate step — needs careful ε-δ.]
  4. Extract the limit at infinity. Fix `b` with `g(b)=β>0`; its orbit `b + m·β` (carrying `g=β`) is an AP of spacing `β`. For any large `a`, pick the orbit point `y = b + m·β` nearest to `a` (within `β/2`, by Dirichlet/nearest-integer). Apply (★): `|g(a) − β|·(2a + 2y + g(a) + β) <= (a − y − β)² <= (β/2)²` (since `|a − y| <= β/2` and `a − y − β` is within `β/2` of `−β`, bounded). As `a → ∞`, the factor `(2a + 2y + ...)` `~ 4a → ∞`, forcing `|g(a) − β| → 0`. So `lim_{a→∞} g(a) = β`. — by sending `a→∞` against a bounded numerator, Dirichlet nearest-integer for the orbit-point approximation. [GAP: if `g` has no nonzero value anywhere, then `g≡0` and we are done — handle that branch first.]
  5. Conclude the value set of `g` is contained in `{0, L}` where `L = lim_{∞} g`. Indeed any `y0` with `g(y0)=δ>0` has its orbit `y0 + n·δ → ∞` carrying `g=δ`, forcing `δ = L`. — by orbit-invariance + the limit just proved.
  6. Finish by connectedness: `g` is continuous (step 3) on the connected space `R_{>0}` and takes values in the discrete set `{0, L}`; hence `g` is constant (the level sets `g^{-1}(0)`, `g^{-1}(L)` are clopen). So `g ≡ 0` or `g ≡ L`. — by the clopen-partition characterization of connectedness.
  7. Apply the shared construction: `f(x) = x + c`, `c >= 0`.
Key lemmas (claim + mechanism):
  - Master bound (★) as a Lipschitz-type estimate — because the `(L+R, L−R)` decomposition turns "both inequalities hold" into "`|g(x)−g(y)|` times a positive factor is bounded by a square."
  - Continuity at a zero — because the denominator in (★) stays `~4b` while the numerator `(a−y−g(y))²` is `O(h²)`.
  - Limit at infinity — because Dirichlet nearest-integer approximates any large `a` by an orbit point within a fixed spacing, and the growing denominator `~4a` then crushes the residual `|g(a)−β|`.
  - Connectedness pins the value set — because a continuous map from a connected space to a discrete set is constant.
Open gaps: the continuity-at-a-nonzero-point two-sided squeeze (step 3, second bullet) is asserted by the explorer but not rigorously derived — this is the single hardest gap of this framing; the branch `g ≡ 0` (no nonzero value exists) must be handled before step 4's "fix `b` with `g(b)=β>0`"; the nearest-integer approximation must produce `y <= a` or handle the side condition in the numerator bound `(a − y − β)²` carefully (if `y > a` the sign flips but the square bound still holds within `β/2`).
Cases to cover: `g≡0` (trivial finish) vs. `g` has a nonzero value (run the limit argument).
Watch out for: the continuity-at-nonzero step is the load-bearing rig; the `L=0` case (`g≡0`) is a valid terminal branch — don't drop it; connectedness needs `R_{>0}` connected (it is, as `(0,∞)`).

### swap-cross-inequalities: new
Technique: Swap `x ↔ y` in the original inequality and combine the four resulting bounds to extract the genuinely off-diagonal cross-inequalities `2x·f(y) <= y² + f(x)²` and `2y·f(x) <= x² + f(y)²`; then squeeze `g` constant directly from these cross-terms layered on top of (C1). This route does NOT pass through the `(L+R,L−R)` master bound (★) — it works purely by intersecting the two interval constraints.
Skeleton:
  1. The original gives `A := (f(x)+y)/2 ∈ [sqrt(x·f(y)), sqrt((x²+f(y)²)/2)]`. — by (R) and (L).
  2. Swapping `x↔y` gives `B := (f(y)+x)/2 ∈ [sqrt(y·f(x)), sqrt((y²+f(x)²)/2)]`. — by the same inequality with roles exchanged.
  3. Note `A` and `B` are linked: `A − B = (f(x) − x − (f(y) − y))/2 = (g(x) − g(y))/2`. The two intervals (one for `A`, one for `B`) must be simultaneously satisfiable for ALL `x,y`, and their widths are controlled by the same four quantities. — by algebra.
  4. Derive the off-diagonal cross-inequality `2x·f(y) <= y² + f(x)²`. Mechanism: `B = (x+f(y))/2` is the AM of the pair `(y, f(x))`, hence `B ∈ [sqrt(y·f(x)), ...]` upper part is automatic; the load-bearing constraint comes from requiring the upper bound of `B`'s interval to be compatible with `A`'s lower bound. Concretely, combine `A >= sqrt(x·f(y))` (a lower bound on A) with the AM `A <= (x+f(y))` and the requirement that `B`'s interval is nonempty and contains `B`. [GAP: the exact derivation of `2x·f(y) <= y² + f(x)²` from the four bounds is the crux — explorer asserts it but the chaining must be checked to avoid the INVALID "two lower bounds on the same quantity" fallacy flagged dead below.]
  5. Symmetrically derive `2y·f(x) <= x² + f(y)²`. — by swapping roles in step 4.
  6. Add the two cross-inequalities: `2x·f(y) + 2y·f(x) <= x² + y² + f(x)² + f(y)²`. Rewrite in `g`: `2x(y+g(y)) + 2y(x+g(x)) <= x²+y²+(x+g(x))²+(y+g(y))²`. Rearrange to isolate a nonnegative expression involving `(g(x)−g(y))`. [GAP: the algebraic rearrangement must yield a manifest nonneg quantity that forces `g(x)=g(y)` — explorer did not close this; the outliner leaves the precise SOS form as the open gap.]
  7. Alternatively, multiply the two cross-inequalities or compose them along an orbit (using C1) to amplify any displacement difference into a contradiction. [GAP: which composition closes?]
  8. If `g` constant follows, finish with the shared construction.
Key lemmas (claim + mechanism):
  - Cross-inequality `2x·f(y) <= y² + f(x)²` — mechanism to be pinned: it is the genuinely off-diagonal constraint (NOT pure AM-GM, which only gives `y² + f(x)² >= 2y·f(x)`); it must come from the interval-intersection logic of steps 1–3.
  - Symmetric cross-inequality — by the `x↔y` symmetry of the problem.
  - (C1) orbit invariance — shared, used to amplify along orbits in step 7 if needed.
Open gaps: the rigorous derivation of the cross-inequalities (step 4) without falling into the "two-lower-bounds" fallacy; the algebraic/SOS rearrangement (step 6) that is supposed to force `g(x)=g(y)` — this is the load-bearing gap of the framing and is NOT yet closed by exploration; if step 6 fails, the orbit-amplification variant (step 7) is the fallback, also open.
Cases to cover: none special; the cross-inequalities hold for all `x,y`.
Watch out for: the INVALID chain `f(x)/x >= f(y)/y ⇒ constancy` — explicitly dead (two lower bounds on the same quantity do not order); do NOT include any route that uses it. The cross-inequality derivation must use the interval structure, not a spurious ordering.

### infimum-supremum-squeeze: new
Technique: Fix `y`; treat (R) as a family of upper bounds on `f(y)` parameterized by `x`, and (L) as a family of lower bounds on `f(y)` parameterized by `x`. Compute the infimum of the upper bounds and the supremum of the lower bounds; show they coincide at `y + c` for a single `c` independent of `y`. This route DELIBERATELY bypasses the orbit recurrence (C1) and the master bound (★) — it attacks `g`-constancy directly from per-`y` optimization.
Skeleton:
  1. From (R): `(f(x)+y)² >= 4x·f(y)`, i.e. `f(y) <= (f(x)+y)²/(4x)` for every `x>0`. Hence `f(y) <= U(y) := inf_{x>0} (f(x)+y)²/(4x)`. — by treating (R) as a bound on `f(y)`.
  2. From (L): `2(x² + f(y)²) >= (f(x)+y)²`, i.e. (when the radicand is positive) `f(y) >= sqrt(((f(x)+y)² − 2x²)/2 + ... )` — carefully: `2f(y)² >= (f(x)+y)² − 2x²`, so `f(y) >= L(y) := sup_{x: (f(x)+y)² > 2x²} sqrt(((f(x)+y)² − 2x²)/2)`. — by treating (L) as a bound on `f(y)`.
  3. The sandwich `L(y) <= f(y) <= U(y)` holds for every `y`. — by combining steps 1–2.
  4. Compute `U(y)` explicitly. The minimizer of `(f(x)+y)²/(4x)` over `x` depends on the unknown `f`, so this is not a closed-form optimization in general — but use the orbit recurrence (C1) as auxiliary input to relate `f(x)` at chosen `x` to a single displacement value. [GAP: the minimizer is at `x` where `f(x) = y` (i.e. on the preimage of `y`) — but surjectivity is not assumed. Needs a substitute.]
  5. Compute `L(y)` similarly. [GAP.]
  6. Show `L(y) = U(y) = y + c` for a single `c` independent of `y`. — by the two computations agreeing. [GAP — the load-bearing step: the inf and sup coincide, and the coincidence value is affine in `y` with slope 1.]
  7. Finish with the shared construction (which also verifies `c >= 0`).
Key lemmas (claim + mechanism):
  - `f(y) <= inf_x (f(x)+y)²/(4x)` — because (R) holds for EVERY `x`, so `f(y)` is at most the infimum of the RHS family.
  - `f(y) >= sup_x sqrt(((f(x)+y)² − 2x²)/2)` — symmetric, from (L) for every `x`.
  - Coincidence `L(y) = U(y) = y + c` — mechanism to be pinned: the inf and the sup are attained (or approached) at the same extremal `x`, and that extremal configuration forces `f(x) − x = f(y) − y`. The "natural sufficient condition" (the AM of `(x, f(y))` equals the AM of `(y, f(x))`) is the equality case of this optimization.
Open gaps: step 4–6 are essentially the whole proof — the optimization over the unknown function `f` does not close without extra structure; the route needs (C1) as auxiliary to relate `f`-values at chosen `x` to displacements, and even then the coincidence of inf and sup at an affine function is the unproven crux. The outliner flags this as the highest-risk framing: it may collapse into approach 1 once (C1) is brought in.
Cases to cover: none.
Watch out for: surjectivity of `f` is NOT assumed — the minimizer `x` with `f(x)=y` may not exist; the "natural sufficient condition" trap (the right inequality is automatic if `f(x)/x` const, the left if `f(x)-x` const — these are sufficient, not necessary, and the actual family `f=x+c` with `c>0` satisfies NEITHER, so the equality case of the optimization is subtle); the radicand positivity in step 2.

### algebraic-sos-elimination: new
Technique: Combine the four squared bounds — `L(x,y)`, `R(x,y)`, and their swapped counterparts `L(y,x)`, `R(y,x)` — seeking a pure sum-of-squares identity that manifestly expresses `g(x) − g(y)` (or `(g(x)−g(y))²`) as a combination of the given nonnegative quantities, forcing `g(x) = g(y)` with NO analysis (no continuity, no density, no limits). This is the "pure algebra" framing — a long shot, but genuinely orthogonal in route.
Skeleton:
  1. Write the four nonnegative quantities:
     `L(x,y) = 2(x²+f(y)²) − (f(x)+y)² >= 0`,
     `R(x,y) = (f(x)+y)² − 4x·f(y) >= 0`,
     `L(y,x) = 2(y²+f(x)²) − (f(y)+x)² >= 0`,
     `R(y,x) = (f(y)+x)² − 4y·f(x) >= 0`.
  2. Substitute `f(t) = t + g(t)` throughout and expand each as a quadratic form in `g(x), g(y)` (with `x,y` as parameters). — by algebra.
  3. Known identities: `L(x,y)+R(x,y) = 2(x−f(y))² = 2(x−y−g(y))²`; `L(x,y)−R(x,y) = 2(g(y)−g(x))(2x+2y+g(x)+g(y))`; and the two swapped analogues. — direct expansion.
  4. Seek a nonnegative linear combination `α·L(x,y) + β·R(x,y) + γ·L(y,x) + δ·R(y,x)` (with `α,β,γ,δ` functions of `x,y` allowed, or a clever multiplicative combination) that equals a manifest nonnegative multiple of `(g(x)−g(y))²` (or of `|g(x)−g(y)|` times a positive factor that is also bounded below). [GAP: does such an identity exist? The explorers did not find one; this is the framing's central question.]
  5. If found, the four summands being `>= 0` forces the combination `>= 0`, hence `g(x) = g(y)` (when the multiplier is strictly positive). — by the SOS identity.
  6. Fallback (still algebraic): intersect the equality conditions of all four bounds simultaneously — the equality case of `L,R` is `x = f(y)` (both zero), and of the swapped pair is `y = f(x)`; requiring both equalities at the same `(x,y)` gives `x = f(y)` AND `y = f(x)`, i.e. `g(x) = g(y) = 0` on the intersection. Argue that the universal quantifier forces this intersection to be nonempty/dense enough to pin `g` everywhere. [GAP: the equality cases are a measure-zero locus; their intersection does not directly pin `g` off the locus — this fallback is weak and needs an additional idea.]
  7. Finish with the shared construction.
Key lemmas (claim + mechanism):
  - The four-quantity SOS identity (if it exists) — mechanism: an algebraic combination of the four bounds that is identically a nonnegative multiple of `(g(x)−g(y))²`. The existence is the open question.
  - Equality-case intersection — because `L=R=0` iff `x=f(y)` (the pair-equal collapse), and the swapped version iff `y=f(x)`; simultaneously they give `g(x)=g(y)=0`.
Open gaps: the existence of the SOS identity (step 4) is the whole framing — it may not exist, in which case this approach dies (record the dead end); the fallback equality-case intersection (step 6) is too weak on its own. The outliner nominates this framing precisely because, if the identity exists, it gives the cleanest proof with zero analytic machinery — but it is the highest-risk bet.
Cases to cover: none.
Watch out for: a putative SOS identity must be checked to actually have a strictly positive multiplier on `(g(x)−g(y))²` for ALL `x,y>0` (a multiplier that vanishes somewhere is useless); the fallback is genuinely weak — do not present it as the main route.

---

Field summary (5 approaches, all NEW, diverse framings):
- **diagonal-diophantine-kill** — sign-decomposition + two-orbit Dirichlet/Frobenius. Highest-evidence framing (numerically verified, both rational and irrational cases).
- **lipschitz-connectedness** — analytic: continuity + limit-at-infinity + connectedness. Strong, but the continuity-at-nonzero step is a real rig.
- **swap-cross-inequalities** — swap x↔y, derive off-diagonal cross-inequalities, squeeze. The cross-inequality derivation and the forcing SOS are both open.
- **infimum-supremum-squeeze** — per-y optimization over x, bypassing orbits. Highest-risk; may collapse into the first framing once C1 is invoked.
- **algebraic-sos-elimination** — pure-algebra long shot; seeks an SOS identity for `(g(x)−g(y))²` from the four bounds. May die cleanly (record as dead end if so).

Shared certified-lemma candidate (propose to certifier once any approach proves it): the master bound `(★) |g(x)−g(y)|·(2x+2y+g(x)+g(y)) <= (x−y−g(y))²` from the `(L+R, L−R)` decomposition — used by approaches 1 and 2, importable to cut duplication. The diagonal collapse `(C1)+(C2)` (`f(f(y))=2f(y)−y`, `g>=0`, orbit-invariance) is shared by all five and should be certified as a lemma immediately — it is forced and free.
