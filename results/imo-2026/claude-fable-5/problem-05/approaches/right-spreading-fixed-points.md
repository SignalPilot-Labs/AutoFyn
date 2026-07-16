# Approach: right-spreading-fixed-points

## Status
solved

## Approaches tried
- (round 1, outliner) Skeleton laid: same reduction to "h := f − id is constant" via the functional equation, but both kill arguments use only the RIGHT inequality: (a) two positive values die by an exact-expansion orbit chase; (b) fixed points coexisting with non-fixed points die by a spreading argument — the right inequality forces an interval around every fixed point to consist of fixed points, the fixed set spreads to cover a neighborhood of infinity, and an unbounded non-fixed orbit must enter it. No verdict yet — gaps open.
- (round 1, builder) Both gaps closed in full: GAP 1 (Step 2.5' chase) written with the explicit threshold on n (n ≥ max(0, ⌈(x₀−yₙ... )⌉) — precisely: n large enough that yₙ ≥ x₀ AND yₙ > a²/(b−a)), the chasing index m = ⌈(yₙ − x₀)/a⌉ shown to exist and to give s ∈ [0, a), and the exact expansion derived inline (avoiding the lossy crude bound). GAP 2 (Step 2.6' spreading) written with the reviewer-requested justifications: [y₀, S) ⊆ F proved as the union of nested intervals [y₀, s) over s ∈ A, and the chosen y shown to satisfy y > y₀ (so the radius comparison √(ay) > √(ay₀) is strict and the window (S − √(ay₀), S) lies inside (y₀, S) ⊆ F). Steps 2.1–2.3 proved in full here (no certified lemmas existed yet to import). All load-bearing identities re-verified in sympy. Outcome: complete proof, no gaps — proposed for review.

## Current best
Complete rigorous proof below: verification that f(x) = x + c (c ≥ 0) works, and uniqueness via the functional equation f∘f = 2f − id, AP orbits, and two right-inequality kill mechanisms (orbit chase for two positive values of h; fixed-point spreading for the mixed case). No open gaps.

## Full proof

**Problem.** Determine all functions f: ℝ_{>0} → ℝ_{>0} such that

  √((x² + f(y)²)/2) ≥ (f(x) + y)/2 ≥ √(x·f(y))    (†)

for every x, y > 0.

**Answer.** Exactly the functions f(x) = x + c, where c ≥ 0 is a constant.

Throughout, "the left inequality" means √((x² + f(y)²)/2) ≥ (f(x) + y)/2 and "the right inequality" means (f(x) + y)/2 ≥ √(x·f(y)). All quantities below are positive reals, so every squaring or square-root step performed is between positive numbers and hence an equivalence; we note this once here and again at each use.

---

### Part 1: Verification that f(x) = x + c (c ≥ 0) satisfies (†)

Let c ≥ 0 and f(x) = x + c. First, f maps ℝ_{>0} to ℝ_{>0}: for x > 0 we have f(x) = x + c ≥ x > 0.

**Right inequality.** We must show (x + c + y)/2 ≥ √(x(y + c)) for all x, y > 0. Both sides are positive (LHS > 0 since x, y > 0, c ≥ 0). Squaring (an equivalence for positive numbers), the claim is (x + y + c)² ≥ 4x(y + c). We compute the difference exactly:

  (x + y + c)² − 4x(y + c)
  = x² + y² + c² + 2xy + 2xc + 2yc − 4xy − 4xc
  = x² − 2x(y + c) + (y + c)²
  = (x − (y + c))² ≥ 0.

(This is the AM–GM inequality for the positive pair x and y + c; see `knowledge_base.md`, Standard inequalities / AM–GM.)

**Left inequality.** We must show √((x² + (y + c)²)/2) ≥ (x + c + y)/2. Both sides are positive; squaring, the claim is (x² + (y + c)²)/2 ≥ (x + y + c)²/4, i.e. 2x² + 2(y + c)² ≥ (x + (y + c))². The difference:

  2x² + 2(y + c)² − (x + (y + c))²
  = 2x² + 2(y + c)² − x² − 2x(y + c) − (y + c)²
  = x² − 2x(y + c) + (y + c)²
  = (x − (y + c))² ≥ 0.

(This is the QM–AM inequality for the pair x, y + c; see `knowledge_base.md`, Standard inequalities / QM-AM.)

So both inequalities in (†) hold — indeed the whole chain is QM ≥ AM ≥ GM for the pair (x, y + c), with common squared margin (x − y − c)²/4 (sympy-checked; the two computations above are the proof). Hence every f(x) = x + c with c ≥ 0 is a solution. (For c < 0 the formula does not define a function into ℝ_{>0}: at x = −c/2 > 0 we would get f(x) = c/2 < 0; so no c < 0 arises. This remark is not needed for Part 1 but explains why the answer family is restricted to c ≥ 0.)

---

### Part 2: Uniqueness

Let f be any solution of (†). We prove f(x) = x + c for some constant c ≥ 0.

#### Step 2.1 — The functional equation f(f(y)) = 2f(y) − y

Fix y > 0 and substitute x = f(y) (legitimate: f(y) > 0) into both inequalities of (†).

*Left inequality at (x, y) = (f(y), y):*

  √((f(y)² + f(y)²)/2) ≥ (f(f(y)) + y)/2.

The left side equals √(f(y)²) = f(y), since f(y) > 0. Hence

  f(y) ≥ (f(f(y)) + y)/2, i.e. f(f(y)) ≤ 2f(y) − y.  (L₀)

*Right inequality at (x, y) = (f(y), y):*

  (f(f(y)) + y)/2 ≥ √(f(y)·f(y)) = f(y),

again using f(y) > 0. Hence

  f(f(y)) ≥ 2f(y) − y.  (R₀)

Combining (L₀) and (R₀):

  **f(f(y)) = 2f(y) − y for all y > 0.**  (FE)

#### Step 2.2 — Orbit structure: h := f − id is orbit-invariant and orbits are arithmetic progressions

Define h: ℝ_{>0} → ℝ by h(t) := f(t) − t. From (FE), for every y > 0:

  h(f(y)) = f(f(y)) − f(y) = (2f(y) − y) − f(y) = f(y) − y = h(y).  (INV)

Note f(y) > 0, so h(f(y)) is defined.

**Claim:** for every integer n ≥ 0 and every y > 0, the iterate fⁿ(y) (with f⁰ = id) is defined, lies in ℝ_{>0}, and

  fⁿ(y) = y + n·h(y)  and  h(fⁿ(y)) = h(y).  (ORB)

*Proof by induction on n.* Base n = 0: f⁰(y) = y = y + 0·h(y) ∈ ℝ_{>0} and h(f⁰(y)) = h(y). Inductive step: suppose (ORB) holds for n. Then fⁿ(y) ∈ ℝ_{>0}, so f^{n+1}(y) = f(fⁿ(y)) is defined and lies in ℝ_{>0} (codomain of f). Moreover

  f^{n+1}(y) = fⁿ(y) + h(fⁿ(y)) = (y + n·h(y)) + h(y) = y + (n+1)·h(y),

using the definition of h at the point fⁿ(y) and both parts of the inductive hypothesis. And by (INV) applied at the point fⁿ(y):

  h(f^{n+1}(y)) = h(f(fⁿ(y))) = h(fⁿ(y)) = h(y).

This completes the induction. ∎(Claim)

#### Step 2.3 — h ≥ 0

Suppose h(y) = −d < 0 for some y > 0. By (ORB), fⁿ(y) = y − nd for all n ≥ 0. Choose an integer n ≥ y/d (possible by the Archimedean property of ℝ). Then fⁿ(y) = y − nd ≤ y − (y/d)·d = 0, contradicting fⁿ(y) ∈ ℝ_{>0} from (ORB). Hence

  **h(y) ≥ 0 for all y > 0.**

#### Step 2.4' — The right inequality in exact expanded form

Only the right inequality of (†) is used from here on. For any x, y > 0, both sides of (f(x) + y)/2 ≥ √(x·f(y)) are positive, so squaring is an equivalence and the right inequality is equivalent to

  (f(x) + y)² ≥ 4x·f(y).  (R)

We will apply (R) at points where h is known, using the exact expansion derived inline in each of the two kill steps below (avoiding any lossy intermediate bound).

#### Step 2.5' — h takes at most one positive value

**Claim.** There do not exist x₀, y₀ > 0 with 0 < h(x₀) < h(y₀).

*Proof.* Suppose for contradiction that h(x₀) = a and h(y₀) = b with 0 < a < b.

By (ORB), for all integers m, n ≥ 0 the points

  xₘ := f^m(x₀) = x₀ + m·a  and  yₙ := fⁿ(y₀) = y₀ + n·b

lie in ℝ_{>0} and satisfy h(xₘ) = a, h(yₙ) = b. Thus {xₘ} is an unbounded increasing arithmetic progression of step a on which h ≡ a, and {yₙ} likewise with step b and h ≡ b.

**Threshold on n.** Choose an integer n satisfying both

  (T1) yₙ = y₀ + n·b ≥ x₀, i.e. n ≥ (x₀ − y₀)/b, and
  (T2) yₙ = y₀ + n·b > a²/(b − a), i.e. n > (a²/(b − a) − y₀)/b.

Such n exists: take n = max(0, ⌈(x₀ − y₀)/b⌉, ⌊(a²/(b − a) − y₀)/b⌋ + 1). (Both thresholds are finite real numbers; b > 0.)

**Existence of the chasing index m.** Since yₙ ≥ x₀ by (T1), the number (yₙ − x₀)/a is ≥ 0; set m := ⌈(yₙ − x₀)/a⌉, an integer ≥ 0. By definition of the ceiling,

  (yₙ − x₀)/a ≤ m < (yₙ − x₀)/a + 1,

so multiplying by a > 0 and adding x₀:

  yₙ ≤ xₘ = x₀ + m·a < yₙ + a.

Set x := xₘ and s := x − yₙ. Then

  0 ≤ s < a.  (CH)

**Exact expansion of (R) at (x, yₙ).** We have f(x) = x + h(x) = x + a and f(yₙ) = yₙ + h(yₙ) = yₙ + b. Inequality (R) at the pair (x, yₙ) reads

  (x + a + yₙ)² ≥ 4x(yₙ + b).

Substituting x = yₙ + s and expanding both sides exactly:

  LHS = (2yₙ + s + a)² = 4yₙ² + 4yₙ(s + a) + (s + a)²,
  RHS = 4(yₙ + s)(yₙ + b) = 4yₙ² + 4yₙ(s + b) + 4sb.

Hence (R) is equivalent to

  0 ≤ LHS − RHS = 4yₙ(a − b) + (s + a)² − 4sb.  (EXP)

(Identity (EXP) re-checked symbolically in sympy; the two displayed expansions constitute the proof.)

**Contradiction.** We bound the right side of (EXP) strictly below 0:

- Since 0 ≤ s < a, we have 0 < s + a < 2a, so (s + a)² < 4a².
- Since s ≥ 0 and b > 0, we have −4sb ≤ 0.
- Since b > a, the first term is 4yₙ(a − b) = −4yₙ(b − a) < 0.

Therefore

  4yₙ(a − b) + (s + a)² − 4sb < −4yₙ(b − a) + 4a².

By (T2), yₙ > a²/(b − a), so −4yₙ(b − a) + 4a² < −4·(a²/(b − a))·(b − a) + 4a² = 0. Combining,

  0 ≤ 4yₙ(a − b) + (s + a)² − 4sb < 0,

a contradiction. ∎(Step 2.5')

(Note: the crude bound x + yₙ + a ≤ 2yₙ + 2a in place of the exact expansion would only produce a contradiction for b > 2a; the exact expansion (EXP) with the chase bound (CH) kills all b > a > 0.)

#### Step 2.6' — A value 0 and a value a > 0 cannot coexist

By Steps 2.3 and 2.5', the range of h is a subset of [0, ∞) containing at most one positive number. Suppose for contradiction that h attains both the value 0 and a value a > 0. Then the range of h is exactly {0, a}. Define

  F := h⁻¹(0) = {t > 0 : f(t) = t}  (the fixed points),
  P := h⁻¹(a),

so F ≠ ∅, P ≠ ∅, F ∩ P = ∅, and F ∪ P = ℝ_{>0}. By (ORB) with n = 1, both F and P are f-invariant, and for p ∈ P the orbit fᵐ(p) = p + m·a stays in P.

**(i) An explicit fixed-point neighborhood consists of fixed points.**

Let y₀ ∈ F and let y ∈ P be arbitrary. Apply (R) at the pair (x, y) = (y₀, y): since f(y₀) = y₀ (as y₀ ∈ F) and f(y) = y + a (as y ∈ P),

  (y₀ + y)² ≥ 4y₀(y + a).

Expanding exactly:

  (y₀ + y)² − 4y₀(y + a) = y₀² + 2y₀y + y² − 4y₀y − 4ay₀ = (y − y₀)² − 4a·y₀.

Hence every y ∈ P satisfies

  (y − y₀)² ≥ 4a·y₀, i.e. |y − y₀| ≥ 2√(a·y₀).  (ZONE)

(Identity re-checked in sympy; the displayed expansion is the proof.) Define the open interval

  J(y₀) := (y₀ − 2√(a·y₀), y₀ + 2√(a·y₀)).

By (ZONE), no point of P lies in J(y₀). Since F ∪ P = ℝ_{>0} (this is exactly where the two-valuedness from Step 2.5' is used — keep the order of steps),

  **J(y₀) ∩ ℝ_{>0} ⊆ F.**  (SPREAD)

In particular, since y₀ > 0, the half-open interval [y₀, y₀ + 2√(a·y₀)) ⊆ J(y₀) ∩ ℝ_{>0} ⊆ F.

**(ii) F spreads to a neighborhood of infinity: [y₀, ∞) ⊆ F for any fixed y₀ ∈ F.**

Fix y₀ ∈ F and write r₀ := √(a·y₀) > 0. Define

  A := {s > y₀ : [y₀, s) ⊆ F}.

By the last line of (i), s₁ := y₀ + 2r₀ satisfies [y₀, s₁) ⊆ F, so s₁ ∈ A and A ≠ ∅. Let

  S := sup A ∈ (y₀, ∞], with S ≥ s₁ = y₀ + 2r₀.

**Sub-claim: [y₀, S) ⊆ F.** Let t ∈ [y₀, S). If t = y₀ then t ∈ F by hypothesis. If t > y₀: since t < S = sup A, there exists s ∈ A with s > t; then t ∈ [y₀, s) ⊆ F. (Equivalently: the intervals {[y₀, s) : s ∈ A} are nested by inclusion as s grows, and their union is [y₀, S); every point below the supremum is below some element of A.) ∎(Sub-claim)

Suppose for contradiction S < ∞. Consider the window

  W := (S − r₀, S).

W is a nonempty open interval (length r₀ > 0). Moreover every y ∈ W satisfies y > y₀: indeed y > S − r₀ ≥ (y₀ + 2r₀) − r₀ = y₀ + r₀ > y₀. Also every y ∈ W satisfies y < S, so by the Sub-claim W ⊆ [y₀, S) ⊆ F. Pick any y ∈ W. Then:

- y ∈ F, so (i) applies at the fixed point y: [y, y + 2√(a·y)) ⊆ F. (The interval lies in ℝ_{>0} since y > 0.)
- Since y > y₀ and the map t ↦ √(a·t) is strictly increasing on ℝ_{>0} (a > 0), we get √(a·y) > √(a·y₀) = r₀, hence

    y + 2√(a·y) > y + 2r₀ > (S − r₀) + 2r₀ = S + r₀.

- Since y < S, the two F-subsets [y₀, S) and [y, y + 2√(a·y)) overlap on [y, S) ≠ ∅ (as y₀ ≤ y < S), so their union contains the full interval [y₀, y + 2√(a·y)) ⊇ [y₀, S + r₀).

Therefore [y₀, S + r₀) ⊆ F, so S + r₀ ∈ A, contradicting S = sup A (as S + r₀ > S). Hence S = ∞, and by the Sub-claim

  **[y₀, ∞) ⊆ F.**

**(iii) Orbit escape contradiction.**

Pick p ∈ P (nonempty by assumption). By (ORB), pₘ := fᵐ(p) = p + m·a ∈ P for every integer m ≥ 0. Choose m ≥ max(0, (y₀ − p)/a) (Archimedean property; a > 0). Then pₘ = p + m·a ≥ y₀, so pₘ ∈ [y₀, ∞) ⊆ F by (ii). But pₘ ∈ P and F ∩ P = ∅ — contradiction. ∎(Step 2.6')

#### Step 2.7' — Conclusion of uniqueness

By Step 2.3 the range of h is a nonempty subset R ⊆ [0, ∞). We show R is a singleton. Suppose |R| ≥ 2.

- If R contains two distinct positive values a < b, Step 2.5' gives a contradiction.
- Otherwise R contains at most one positive value; since |R| ≥ 2 and R ⊆ [0, ∞), R must contain 0 and exactly one positive value a, i.e. R = {0, a} with a > 0. Step 2.6' gives a contradiction.

These two cases are exhaustive for |R| ≥ 2 (a two-or-more-element subset of [0, ∞) either has two positive elements or consists of 0 and one positive element). Hence R = {c} for some c ≥ 0, i.e.

  h ≡ c, i.e. f(x) = x + c for all x > 0, with c ≥ 0.

#### Combining

Part 2 shows every solution is of the form f(x) = x + c with c ≥ 0; Part 1 verifies each such f is a solution. Therefore the solutions of (†) are exactly

  **f(x) = x + c, c ≥ 0 a constant.** ∎

---

## Promotable lemmas

Proved in full in this file this round (Steps 2.1–2.3 — shared base with `orbit-forbidden-zone`; the sibling builder may propose the identical statements, certify once):

1. **Lemma FE (functional equation).** Any solution f of (†) satisfies f(f(y)) = 2f(y) − y for all y > 0. *Proved in Step 2.1* (substitute x = f(y) into both inequalities; the QM and GM collapse to f(y)).
2. **Lemma ORB (orbit invariance / AP orbits).** For any solution f, the function h := f − id satisfies h(f(y)) = h(y), and for all integers n ≥ 0, fⁿ(y) = y + n·h(y) ∈ ℝ_{>0} with h(fⁿ(y)) = h(y). *Proved in Step 2.2* (induction).
3. **Lemma NONNEG (h ≥ 0).** For any solution f, h(y) = f(y) − y ≥ 0 for all y > 0. *Proved in Step 2.3* (otherwise the AP orbit exits ℝ_{>0}).

Approach-specific, also fully proved and possibly reusable by right-inequality routes:

4. **Lemma ONEPOS (at most one positive value).** For any solution f, h takes at most one positive value. *Proved in Step 2.5'* using only the right inequality (exact expansion (EXP) + within-one-step chase).

## Watch out for (retained notes)
- In 2.5', the exact expansion (EXP) is essential; the crude bound (x + y + a) ≤ 2y + 2a only kills b > 2a.
- In 2.6'(ii) the spreading radius 2√(a·y) grows with y — the argument needs only that it strictly exceeds 2√(a·y₀) for y > y₀.
- (i) constrains only elements of P; concluding J(y₀) ∩ ℝ_{>0} ⊆ F uses that h is two-valued, available only AFTER Step 2.5'. Keep the order.
- No continuity/monotonicity assumptions anywhere.
