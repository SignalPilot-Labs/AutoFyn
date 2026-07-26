# Outline review — imo-2026-05 (round 1)

**Shared prefix (verified).** I confirmed the load-bearing algebraic identities with sympy:
- `L + R = 2(x − f(y))²` — correct.
- `L − R = 2(g(y) − g(x))(2x + 2y + g(x) + g(y))` — correct.
The factor `2x+2y+g(x)+g(y) = x + f(x) + y + f(y) > 0` unconditionally (no need for `g >= 0`), so the master bound
`(★)  |g(x)−g(y)|·(2x+2y+g(x)+g(y)) <= (x−y−g(y))²`
is valid *before* the cheap kill. The cheap kill `(C1) f(f(y))=2f(y)−y` + `(C2) g>=0` is forced and free (verified). The construction `f(x)=x+c, c>=0` is rigorous. So the *entire* open problem is global constancy of `g`, as the outliner states.

**Naive `f(x)/x >= f(y)/y` chain.** Confirmed excluded: it appears only in approach 3's "Watch out for" as an INVALID dead end. No approach builds on it.

---

## 1. `diagonal-diophantine-kill` — CHANGES REQUESTED (register; build)

**Technique sound.** The `(L+R, L−R)` → `(★)` decomposition is algebraically verified. The Diophantine kill is sound in its two main cases:
- **Irrational `d1/d2`:** `{n·d1 − (m+1)·d2 : n,m >= 0}` dense in `R` (1-D Kronecker with nonneg coefficients — standard; the inhomogeneous shift `(m+1)` is harmless since `m` ranges over `Z_{>=0}`). LHS bounded near `(a−b)²`, RHS `~ (d2−d1)(2n·d1+2m·d2) → ∞`. Contradiction. OK.
- **Rational `d1/d2 = p/q`, `p<q`, `p>=1`:** `(n,m)=(kq, kp−1)` gives exact zero on the LHS linear combination, RHS grows linearly. `m = kp−1 >= 0` for `k>=1` since `p>=1` (forced by `d1>0`). OK.

**Gap (fixable, not fatal) — the edge case `d1 = 0 < d2`.** I checked directly: with `g(a)=0` the orbit of `a` is the singleton `{a}` (zero displacement ⇒ no forward motion), so only `m` varies. Then at `x=a, y=b+m·d2`:
LHS `(d2)(2a+2b+d2+2m·d2)` grows **linearly** in `m`, RHS `(a−b−(m+1)d2)²` grows **quadratically** — so the master bound is *satisfied* for large `m` and the Diophantine kill does **not** fire. The outliner's proposed `(★★) 2(x+y)(d2−d1) <= (d1+d2)(5d1−3d2)/4` is flagged unverified; I could not derive it and the form looks suspicious (RHS negative for `d1=0, d2>0` since `5·0−3d2 = −3d2 < 0` — so it would read `2(x+y)d2 <= −3d2²/4 < 0`, false). The (★★) bound as written is **wrong**.

**How to fix (for the builder):** the edge case needs a different mechanism. Two live options: (i) perturbation — `g(a)=0` plus the master bound at `y=a` gives `g(x)(2x+2a+g(x)) <= (x−a)²`, so `g(x) -> 0` as `x->a`; pick `x` near `a` with `0 < g(x) =: d1' < d2` small (exists unless `g ≡ 0` on a neighbourhood, which itself propagates), then run the `0 < d1' < d2` kill; (ii) if `g ≡ 0` on an interval around `a`, every point of that interval is a fixed point, giving a *continuum* of `x`-choices and a clean quadratic-in-`m`/linear-in-fixed-`x` contradiction. The builder must write one of these cleanly. This is the single hardest sub-gap of the approach; it is fillable but not yet filled.

**Other gaps to close while building:** cite the precise 1-D Kronecker theorem producing arbitrarily large positive coefficients; confirm `x=a+nd1, y=b+md2` carry `g=d1,d2` by C1 invariance (true, but state it).

**Verdict:** technique right, mechanism verified in the main cases, one genuinely open edge case with a plausibly fillable fix. **CHANGES REQUESTED.**

---

## 2. `lipschitz-connectedness` — CHANGES REQUESTED (register; build)

**Distinct from #1?** Yes. Shares the *verified* prefix `(★)` with #1, but diverges to an **analytic/topological** close (continuity → limit-at-∞ → connectedness) versus #1's **discrete/Diophantine** close. This is not a single-gap trap: the shared lemma `(★)` is *proven* (not a guess), so the two do not die together on a shared unverified step; their risk lives in their *different* close-steps. Both framings are legitimate rival routes.

**Soundness.** The logic is valid in principle: continuity + value-set-in-`{0,L}` + connectedness of `(0,∞)` ⇒ `g` constant. The limit-at-∞ via Dirichlet nearest-integer (orbit point `b+m·β` within `β/2` of `a`, growing denominator `~4a` crushes `|g(a)−β|`) is a standard and sound move.

**Gaps (the load-bearing ones):**
- **Continuity at a nonzero point `a` (`g(a)=α>0`).** The outliner asserts a two-sided squeeze from `(★)` and the symmetric `(★)` but leaves the `ε-δ` unwritten. This is the *single hardest gap of this framing*; the builder must produce a real `ε-δ` proof, not a paraphrase. Sanity-check the mechanism: from `(★)` with `y=a`, `|g(x)−α|(2x+2a+g(x)+α) <= (x−a−α)²`. For `x` near `a`, the RHS is `(x−a−α)² ≈ α²` (a *nonzero* constant, since `α>0`!), not `O((x−a)²)`. So the bound at a nonzero point does **not** give `g(x) → α` by a naive `h²/4a` argument — the numerator is `~α²`, yielding only local *boundedness*, not continuity. **The squeeze as sketched is insufficient; the continuity-at-nonzero step is harder than the outline suggests and may require combining `(★)` with the symmetric bound and the orbit structure in a non-obvious way.** Flag this prominently for the builder — it is the make-or-break step.
- **Branch `g ≡ 0`** (no nonzero value exists): must be handled before step 4's "fix `b` with `g(b)=β>0`". The outline notes this; just ensure it's an explicit terminal branch.
- **Side condition `y <= a` vs `y > a`** in the nearest-integer approximation: the square bound `|a−y−β| <= β/2` holds regardless of sign (square), so this is fine — confirm in writing.

**Verdict:** right technique, valid skeleton, but the load-bearing continuity-at-nonzero gap is harder than outlined and is the real risk. **CHANGES REQUESTED.**

---

## 3. `swap-cross-inequalities` — CHANGES REQUESTED (register; build)

**Genuinely different framing** — the only candidate that does *not* pass through the master bound `(★)`. Builds on the interval-intersection logic of the two swapped sandwiches. Keep for diversity.

**Gaps (serious, stacked):**
- **Gap (a): the cross-inequality `2x·f(y) <= y² + f(x)²` is not yet derived, and a naive derivation is circular.** I checked: the swapped QM bound `(f(y)+x)² <= 2(y²+f(x)²)` gives only `2x·f(y) <= 2y² + 2f(x)² − f(y)² − x²`, which is *weaker* than the desired `2x·f(y) <= y² + f(x)²`. Closing the gap between them requires `(f(x)²−x²) >= (f(y)²−y²)` for all `x,y` — i.e. that `f(t)²−t²` is constant, which is essentially the conclusion in disguise. So the cross-inequality does **not** drop out of the four bounds by pure algebra; it needs the genuine interval-intersection logic (nonemptiness of `I₁∩I₂` containing *both* `A` and `B`), and the builder must write that derivation without falling into the "two lower bounds on the same quantity" fallacy. If the derivation cannot be made non-circular, this approach dies here.
- **Gap (b): the SOS/rearrangement forcing `g(x)=g(y)`.** Even if the cross-inequality is derived, the outline does not close the step that turns `2x·f(y)+2y·f(x) <= x²+y²+f(x)²+f(y)²` into `g(x)=g(y)`. The "manifest nonnegative" rearrangement is asserted, not produced. The orbit-amplification fallback (step 7) is also open.

**Verdict:** structurally orthogonal and worth building for diversity, but the builder must treat gap (a) as a possible *dead end*: attempt the interval-intersection derivation; if it is circular or the cross-inequality does not follow, record the dead end and fall back to orbit-amplification. **CHANGES REQUESTED** with the strong warning above.

---

## 4. `infimum-supremum-squeeze` — RETHINK (do NOT register; do NOT build)

The route is framed as bypassing the orbit recurrence (C1), but the per-`y` optimization `inf_x (f(x)+y)²/(4x)` and `sup_x sqrt(...)` is over the *unknown function* `f` and cannot close without extra structure relating `f`-values at chosen `x` — the only available handle is C1, and once C1 is brought in the route collapses into approach #1's framework (the outliner itself flags this). The self-referential optimization (the minimizer is at `x` with `f(x)=y`, requiring surjectivity which is *not* assumed) does not go through. This is not a fixable gap; the technique as set up cannot produce the coincidence `inf = sup = y+c` from the inequality structure alone. **RETHINK.** Not registered — junk stays out of the pool. If the outliner wants to revisit, it must propose a genuinely different optimization (not "bypass C1").

---

## 5. `algebraic-sos-elimination` — CHANGES REQUESTED (register; do NOT build this round)

**Orthogonal framing** (pure algebra, no analysis, no density). The central question — does a nonneg combination of `{L, R, L(y,x), R(y,x)}` equal a strictly-positive multiple of `(g(x)−g(y))²`? — is open and may have a negative answer. I checked a natural obstruction: `[L(x,y)−R(x,y)] + [L(y,x)−R(y,x)] = 0` is an *identity* (holds for all `f`), so the four bounds are linearly dependent and any SOS identity must work around this. The fallback (equality-case intersection `x=f(y) ∧ y=f(x)`) is correctly flagged weak — the locus is measure-zero and pins `g` only on it. This is a genuine long shot.

**Why register but not build:** round 1 should build the highest-evidence distinct framings; #5 is the lowest-evidence, highest-risk bet. Registering keeps it in the population for a future round if #1–#3 stall; the builder can then either find the identity (cleanest possible proof) or record the dead end cleanly. **CHANGES REQUESTED**, registered, not in this round's build set.

---

## Framing diversity (field-level check)

The field is **diverse** across #1, #2, #3 (the three to build):
- #1: discrete / Diophantine (density + exact-zero lattice points).
- #2: analytic / topological (continuity + limits + connectedness).
- #3: algebraic / interval-intersection (no `(★)`).
These attack the constancy-of-`g` gap from genuinely different angles. The shared `(★)` between #1 and #2 is *verified*, so they are not a single-gap trap. #4 collapses to #1 (cut). #5 is orthogonal but premature. **No field-level stall risk in the build set.**

---

## Ranking (round 1, no prior outcomes — ranked by promise/evidence)

Registered (cold-start Elo 1500 each): `diagonal-diophantine-kill`, `lipschitz-connectedness`, `swap-cross-inequalities`, `algebraic-sos-elimination`. (`infimum-supremum-squeeze` NOT registered — RETHINK.)

Pairwise comparisons (anchored to evidence):
- `diagonal-diophantine-kill` > `lipschitz-connectedness` (both sound; #1's main cases numerically verified and mechanism complete except the single edge case `d1=0`; #2's load-bearing continuity-at-nonzero step is harder than outlined and unverified).
- `diagonal-diophantine-kill` > `swap-cross-inequalities` (#1 verified mechanism vs #3's two stacked unverified gaps, one of which risks circularity).
- `lipschitz-connectedness` > `swap-cross-inequalities` (#2 has a sound if hard close; #3's foundational cross-inequality is not yet derived non-circularly).
- `diagonal-diophantine-kill` > `algebraic-sos-elimination`.
- `lipschitz-connectedness` > `algebraic-sos-elimination`.
- `swap-cross-inequalities` > `algebraic-sos-elimination` (#3 at least has a derivable-if-noncircular target; #5's central identity may simply not exist).

---

build set: diagonal-diophantine-kill, lipschitz-connectedness, swap-cross-inequalities
