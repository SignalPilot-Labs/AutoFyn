# imo-2026-05 — tracking file (proof-reviewer owned)

## Status
solved

## Approaches tried
- `chain-lipschitz-squeeze` — **worked (APPROVED, round 1).** Chain inequality (*) from x = f(y₂), two-sided increment bounds f(z+t) − f(z) = t ± t²/(4f(z)), telescoping + Archimedean argument forces f(y+T) = f(y) + T, hence f = id + c, c ≥ 0. Complete and verified; canonical proof below.
- `orbit-forbidden-zone` — **worked (APPROVED, round 1).** Independent second proof: functional equation f∘f = 2f − id, AP orbits of h = f − id, h ≥ 0; the LEFT inequality in the form (x − f(y))² ≥ 2c(x + f(y)) + c² (c = h(x) − h(y)) kills two positive h-values by an orbit chase and kills the {0, a} range by a forbidden interval around each fixed point plus a supremum squeeze (ε = a/4). Complete and verified; see `approaches/orbit-forbidden-zone.md`.
- `right-spreading-fixed-points` — **worked (APPROVED, round 1).** Independent third proof: same FE/orbit base, then only the RIGHT inequality: an exact-expansion orbit chase (LHS − RHS = 4yₙ(a−b) + (s+a)² − 4sb < 0) kills two positive h-values, and a fixed-point spreading argument ([y₀, ∞) ⊆ F swallows the unbounded non-fixed orbit) kills the mixed case. Complete and verified; see `approaches/right-spreading-fixed-points.md`.

## Current best
Problem fully solved (three independently verified complete proofs). Answer: **f(x) = x + c for a constant c ≥ 0, and only these.** Certified lemma cache: `lemmas/fe-double-iterate.md`, `lemmas/orbit-invariance.md`, `lemmas/h-nonnegative.md`, `lemmas/chain-inequality.md`, `lemmas/increment-bounds.md`, `lemmas/onepos-right.md`.

## Full proof

*(Canonical proof: `chain-lipschitz-squeeze`. Two further independent complete proofs are in `approaches/orbit-forbidden-zone.md` and `approaches/right-spreading-fixed-points.md`.)*

**Problem.** Determine all functions f : R_{>0} → R_{>0} such that

  sqrt((x² + f(y)²)/2) ≥ (f(x) + y)/2 ≥ sqrt(x·f(y))  for all x, y > 0.  (†)

We call the first inequality in (†) the **left inequality** and the second the **right inequality**.

**Answer.** The solutions are exactly the functions f(x) = x + c, where c ≥ 0 is a constant.

Throughout we use the elementary fact (used at every squaring/unsquaring step): **for real numbers A, B ≥ 0, A ≥ B if and only if A² ≥ B²**, since the map s ↦ s² is strictly increasing on [0, ∞). We refer to this as the *squaring principle*. The chain (†) itself is the QM–AM–GM chain (knowledge_base.md: **Standard inequalities** — AM-GM, QM-AM) applied to the pair (x, f(y)) when f(x) + y = x + f(y); this observation motivates but is not used in the proof.

---

### Part 1: Verification — every f(x) = x + c with c ≥ 0 is a solution

Let c ≥ 0 and f(x) = x + c. First, f maps R_{>0} into R_{>0}: for x > 0 we have f(x) = x + c ≥ x > 0.

Fix x, y > 0. Note f(x) + y = x + y + c = x + f(y).

**Left inequality.** Both sides are nonnegative: the left side is a square root; the right side is (x + y + c)/2 > 0 since x, y > 0 and c ≥ 0. By the squaring principle it suffices to compare squares:

  (x² + (y + c)²)/2 − ((x + y + c)/2)²
  = [2x² + 2(y + c)² − (x + (y + c))²] / 4
  = [x² − 2x(y + c) + (y + c)²] / 4
  = (x − y − c)² / 4 ≥ 0.

Hence sqrt((x² + f(y)²)/2) ≥ (f(x) + y)/2.

**Right inequality.** Both sides are nonnegative: the left side is (x + y + c)/2 > 0; the right side is a square root (its argument x(y + c) is positive). By the squaring principle it suffices to compare squares:

  ((x + y + c)/2)² − x(y + c)
  = [(x + (y + c))² − 4x(y + c)] / 4
  = [x² − 2x(y + c) + (y + c)²] / 4
  = (x − y − c)² / 4 ≥ 0.

Hence (f(x) + y)/2 ≥ sqrt(x·f(y)). So every f(x) = x + c with c ≥ 0 satisfies (†).

---

### Part 2: Uniqueness — every solution is f(x) = x + c with c ≥ 0

Let f : R_{>0} → R_{>0} satisfy (†).

#### Step 2.1 — The chain inequality (*)

Fix y₁, y₂ > 0. Since f(y₂) > 0, the number x = f(y₂) is a valid first argument for (†).

**Left inequality at (x, y) = (f(y₂), y₂):**

  sqrt((f(y₂)² + f(y₂)²)/2) ≥ (f(f(y₂)) + y₂)/2.

The left side equals sqrt(f(y₂)²) = |f(y₂)| = f(y₂), since f(y₂) > 0. Multiplying by 2 (a positive constant, so the inequality direction is preserved) and rearranging:

  (L) f(f(y₂)) ≤ 2f(y₂) − y₂.

**Right inequality at (x, y) = (f(y₂), y₁):**

  (f(f(y₂)) + y₁)/2 ≥ sqrt(f(y₂)·f(y₁)).

Multiplying by 2 and rearranging:

  (R) f(f(y₂)) ≥ 2·sqrt(f(y₁)·f(y₂)) − y₁.

Chaining (R) ≤ f(f(y₂)) ≤ (L):

  2·sqrt(f(y₁)·f(y₂)) − y₁ ≤ 2f(y₂) − y₂,

that is,

  **(*) 2·sqrt(f(y₁)·f(y₂)) ≤ 2f(y₂) + y₁ − y₂  for all y₁, y₂ > 0.**

(Here sqrt(f(y₁)·f(y₂)) is well defined and positive since f(y₁), f(y₂) > 0.)

#### Step 2.2 — Two-sided increment bounds

Fix z > 0 and t > 0. Write q = sqrt(f(z)) and p = sqrt(f(z + t)); both are positive since f takes positive values.

**(A) Upper bound.** Apply (*) with y₁ = z + t, y₂ = z:

  2·sqrt(f(z + t)·f(z)) ≤ 2f(z) + (z + t) − z, i.e. 2pq ≤ 2q² + t.

Dividing by 2q > 0 (direction preserved):

  (A1) p ≤ q + t/(2q), equivalently p − q ≤ t/(2q).

Both sides of (A1) are positive (the right side is a sum of positive terms; p > 0). By the squaring principle,

  p² ≤ (q + t/(2q))² = q² + t + t²/(4q²),

that is,

  **(A) f(z + t) − f(z) ≤ t + t²/(4f(z)).**

**(B) Lower bound and strict monotonicity.** Apply (*) with y₁ = z, y₂ = z + t:

  2·sqrt(f(z)·f(z + t)) ≤ 2f(z + t) + z − (z + t), i.e. 2pq ≤ 2p² − t.

Rearranging: t ≤ 2p² − 2pq = 2p(p − q). Since t > 0 and 2p > 0, dividing by 2p > 0 gives

  (B1) p − q ≥ t/(2p) > 0.

In particular p > q, i.e. f(z + t) = p² > q² = f(z) (squaring principle for the positive numbers p > q). Since z > 0 and t > 0 were arbitrary:

  **f is strictly increasing on R_{>0}.**

Now the increment. Using p² − q² = (p − q)(p + q) and (B1):

  f(z + t) − f(z) = (p − q)(p + q) ≥ (t/(2p))·(p + q) = t·(2p − (p − q))/(2p) = t − t·(p − q)/(2p).

Bound the deficit term t·(p − q)/(2p) using (A1) (p − q ≤ t/(2q)):

  t·(p − q)/(2p) ≤ t·(t/(2q))/(2p) = t²/(4pq).

Since p > q > 0 we have pq > q² = f(z), so 1/(4pq) < 1/(4f(z)) (taking reciprocals of positive numbers reverses the inequality). Hence the deficit is < t²/(4f(z)), and

  **(B) f(z + t) − f(z) ≥ t − t²/(4f(z)).**

**Uniform form.** Suppose m > 0 satisfies f(z) ≥ m. Then t²/(4f(z)) ≤ t²/(4m) (reciprocals of positive numbers), so (A) and (B) give together:

  **(AB) t − t²/(4m) ≤ f(z + t) − f(z) ≤ t + t²/(4m)  whenever z > 0, t > 0, and f(z) ≥ m > 0.**

#### Step 2.3 — Telescoping forces exact additivity

**Claim: f(y + T) − f(y) = T for all y > 0, T > 0.**

Fix y > 0 and T > 0, and set m := f(y) > 0. Let n be a positive integer, t := T/n > 0, and define the partition points

  z_k := y + k·t, k = 0, 1, …, n,

so z₀ = y, z_n = y + T, and each z_k ≥ y > 0 is a valid input. Since f is strictly increasing (Step 2.2(B)) and z_k ≥ y, we have f(z_k) ≥ f(y) = m for every k ∈ {0, 1, …, n} (with equality only at k = 0). Thus the hypothesis of (AB) holds at z = z_k with this m, for each k = 0, …, n − 1.

Telescoping the identity f(y + T) − f(y) = Σ_{k=0}^{n−1} [f(z_{k+1}) − f(z_k)] (a finite sum; each summand compares f at z_k and z_k + t = z_{k+1}) and applying (AB) to each summand:

- Upper: f(y + T) − f(y) ≤ Σ_{k=0}^{n−1} (t + t²/(4m)) = n·t + n·t²/(4m) = T + T²/(4mn),
  using n·t = T and n·t² = n·(T/n)² = T²/n.
- Lower: f(y + T) − f(y) ≥ Σ_{k=0}^{n−1} (t − t²/(4m)) = T − T²/(4mn).

Hence for **every** positive integer n:

  |f(y + T) − f(y) − T| ≤ T²/(4mn).

The left side is a fixed nonnegative real number D independent of n, and T²/(4m) is a fixed positive constant. If D > 0, choose a positive integer n > T²/(4mD) (possible by the Archimedean property of R); then T²/(4mn) < D, contradicting D ≤ T²/(4mn). Therefore D = 0, i.e.

  **f(y + T) = f(y) + T  for all y > 0, T > 0.**

#### Step 2.4 — Conclusion

Define g(y) := f(y) − y for y > 0. For any 0 < y < y′, apply Step 2.3 with T = y′ − y > 0:

  f(y′) = f(y + (y′ − y)) = f(y) + (y′ − y), so g(y′) = f(y′) − y′ = f(y) − y = g(y).

Thus g is constant on R_{>0}; set c := f(1) − 1, so that

  f(y) = y + c  for all y > 0.

It remains to show c ≥ 0. Suppose c < 0. Then −c > 0, so −c/2 > 0 is a valid input, and

  f(−c/2) = −c/2 + c = c/2 < 0,

contradicting f : R_{>0} → R_{>0}. Hence c ≥ 0.

Conversely, Part 1 showed that every f(x) = x + c with c ≥ 0 satisfies (†). Therefore the set of solutions is exactly

  **{ f : f(x) = x + c for all x > 0, where c ≥ 0 is a constant }.** ∎
