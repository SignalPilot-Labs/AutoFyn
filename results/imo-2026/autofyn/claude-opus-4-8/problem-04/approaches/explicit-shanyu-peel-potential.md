## Status
partial

## Approaches tried
- **explicit-shanyu-peel-potential (round 2).** Set out to close the shared crux (Shan-Yu survival
  for θ<90, θ∉winning-set) with an explicit child-choice rule + discrete potential, building on the
  outline's target answer **{90/n}**. **Outcome: the target answer {90/n} is FALSE.** While
  constructing the potential I found (and verified with exact rational arithmetic, by hand) that
  **θ=60° is winnable in 2 moves**, yet 90/60 = 3/2 ∉ ℤ. This refutes the characterization every
  approach in the field was built on. The correct winning set is strictly larger than {90/n}. I
  re-derived the generator structure and obtained a corrected **conjecture: Mulan wins ⇔ θ ≤ 90° and
  90/θ is a dyadic rational** (denominator a power of 2). I prove rigorously: the construction for the
  subfamily {90/n} (S1), the explicit θ=60 win, and the full impossibility for θ>90 (S2). The two
  hard halves (construction for all dyadic θ; Shan-Yu survival for non-dyadic θ) remain open — the
  potential/valuation is set up but its preservation is not proven. Status partial.

## Current best
**The furthest rigorous progress (all proven below in the Partial results):**
1. **Normal form** for a move (cevian angle formula). *(Proven.)*
2. **S1 — construction:** for every positive integer n, θ = 90°/n is winnable in ≤ n moves
   (universal 90°-fork + θ-peel). *(Proven, complete.)*
3. **Refutation of {90/n}:** θ = 60° is winnable in exactly 2 moves (injection of 180°−θ = 120° = 2θ,
   then the 2θ-device), and 60° ∉ {90/n}. Hence the field's target answer is wrong. *(Proven,
   complete, exact-arithmetic verified.)*
4. **S2 — impossibility for θ > 90°:** Mulan can never force θ > 90°; Shan-Yu survives from any start
   avoiding θ. *(Proven, complete.)*
5. **Corrected conjecture** (strong generator-level mechanism, NOT fully proven): Mulan wins **iff
   θ ≤ 90° and 90/θ is a dyadic rational** (i.e. 90/θ = m/2^k; equivalently, writing θ/90 = p/q in
   lowest terms, p is a power of 2). Includes all 90/n (n odd or even) and e.g. 60 = 90·2/3, 72 = 90·4/5,
   80 = 90·8/9, but excludes 50, 54, 75.

**Open gaps (the whole remaining difficulty):**
- **(G1) Construction completeness:** show every θ ≤ 90 with 90/θ dyadic is winnable (the generator
  chain reaches θ subject to angle-positivity/neighbour-availability constraints). Verified only for
  the {90/n} subfamily and θ=60.
- **(G2) Survival for non-dyadic θ:** an explicit Shan-Yu strategy + potential (an odd-prime valuation
  of θ/90) that never reaches θ. Set up below but preservation unproven — this is the crux.

## Partial results (rigorous)

Throughout, an angle is a positive real; a *triangle* is an unordered triple (A,B,C) of positive
reals with A+B+C = 180. "T contains θ" means some coordinate equals θ. The game ends (Mulan wins) the
instant the current triangle contains θ.

### 0. Normal form of a move (Proven)

**Lemma 0 (cevian split).** Let T have angles A, B, C at vertices V_A, V_B, V_C. A legal move is: pick
a vertex (say V_A) and a point P strictly interior to the opposite side V_B V_C, and cut along
segment P V_A. Writing x ∈ (0, A) for the part of angle A on the V_B side, the two resulting triangles
are
  child1 = { x, B, 180−x−B }  (triangle V_A V_B P),
  child2 = { A−x, C, x+B }    (triangle V_A V_C P).

*Proof.* In triangle V_A V_B P the angle at V_A is x, at V_B is B, and the third angle is
180 − x − B. In triangle V_A V_C P the angle at V_A is A − x, at V_C is C, and the third angle is
180 − (A−x) − C = (180 − A − C) + x = B + x, using A+B+C = 180. Both are genuine triangles because
x ∈ (0,A) makes all six angles positive (the P-angles 180−x−B and x+B are positive since
0 < x+B < 180). The two P-angles satisfy (180−x−B) + (x+B) = 180: they are supplementary — the
straight-angle fact at P. ∎

Shan-Yu then keeps one child. So from T, **Mulan wins iff θ ∈ T, or she has a move for which BOTH
children are winning positions for her** (Shan-Yu will keep the worse one). This defines her winning
set as the least fixed point:

**Definition (AND–OR winning set).** W₀ = { T : θ ∈ T }; W_{k+1} = W_k ∪ { T : ∃ legal move with both
children ∈ W_k }; W(θ) = ∪_k W_k.

**Lemma 0′.** Mulan can force victory from T in finitely many steps ⇔ T ∈ W(θ).
*Proof.* By induction on k, "Mulan wins from T in ≤ k moves" = "T ∈ W_k": k=0 is θ∈T; and Mulan wins
in ≤ k+1 moves iff either she already won (T ∈ W_k) or she has a move after which, whichever child
Shan-Yu keeps, she wins in ≤ k moves — i.e. both children ∈ W_k. Taking the union over k gives the
claim, since a finite-step forced win uses some finite k. ∎

Shan-Yu freely chooses the initial triangle, so **Mulan wins the game for θ ⇔ W(θ) contains every
triangle** (equivalently, Mulan can force θ from every start). If some triangle avoiding θ lies
outside W(θ), Shan-Yu picks it and survives.

### 1. S1 — θ = 90°/n is winnable in ≤ n moves (Proven)

**(a) Universal 90°-fork.** From ANY triangle T = (A,B,C): a triangle has at most one non-acute angle,
so at least two angles are < 90°. Choose the split vertex to be one whose two neighbours are both
acute (if some angle is ≥ 90°, take that vertex; its two neighbours are the other two angles, both
< 90°; otherwise all are acute and any vertex works). Call the neighbours B, C (both < 90°) and the
split vertex angle A. Cut at x = 90° − B. Then x ∈ (0, A): x > 0 ⇔ B < 90° ✓, and x < A ⇔ 90°−B < A ⇔
A+B > 90° ⇔ 180°−C > 90° ⇔ C < 90° ✓. By Lemma 0,
  child1 = { 90°−B, B, 180−(90°−B)−B } = { 90°−B, B, 90° },
  child2 = { A−90°+B, C, 90° }.
Both children contain 90°. (Geometrically: the P-angle 90° means P is the foot of the altitude from
V_A, which lies strictly inside side V_B V_C exactly because both base angles B, C are acute — the
altitude-foot-inside-side fact, equivalent to x ∈ (0,A) above.) So regardless of Shan-Yu, the survivor
contains 90°. **90° is forceable from every triangle in one move.**

**(b) θ-peel.** Suppose the current triangle has a vertex angle A = mθ with integer m ≥ 2. Cut this
vertex at x = θ ∈ (0, mθ) = (0, A). By Lemma 0,
  child1 = { θ, B, 180−θ−B }  (contains θ),
  child2 = { (m−1)θ, C, θ+B }  (contains (m−1)θ).
Both are valid triangles (all angles positive: (m−1)θ>0, and θ+B<180 since child1's 180−θ−B>0). If
Shan-Yu keeps child1 the game ends and Mulan wins; otherwise the survivor is child2, which contains
(m−1)θ for ANY B, C. **From a vertex mθ (m ≥ 2), one move forces a survivor containing (m−1)θ.**

**(c) Chain.** Let θ = 90°/n, n ∈ ℤ⁺, so nθ = 90°. If n = 1 then θ = 90° and the fork already wins.
If n ≥ 2: one fork move forces a survivor containing 90° = nθ; then apply the peel n−1 times,
nθ → (n−1)θ → ⋯ → θ. At every peel Shan-Yu either hands Mulan a child containing θ (immediate win) or
is pushed to the next lower multiple; after at most n−1 peels the survivor contains θ. Total ≤ n moves,
against every Shan-Yu strategy and every start. ∎

### 2. Refutation of the {90/n} answer: θ = 60° is winnable (Proven)

We exhibit a 2-move forced win for θ = 60°, and 90/60 = 3/2 is not a positive integer, so 60° ∉ {90/n}.

Shan-Yu must choose a start avoiding θ = 60°. Any non-equilateral triangle has minimum angle < 60°
(three angles summing to 180 with not all equal must have one below the mean 60°); the equilateral
triangle is (60,60,60), which already contains θ = 60° and loses instantly. **So every legal Shan-Yu
start has an angle strictly less than 60°.** Fix such a start; let m be an angle with m < 60°.

**Move 1 (inject 180°−θ = 120°).** Let the split vertex A have the small angle m as one neighbour
C := m and the other neighbour B. Cut at x = 180° − θ − B = 120° − B. This is legal:
x = 120°−B > 0 since B < 120°; and x < A ⇔ 120°−B < A ⇔ 120° < A+B = 180°−C ⇔ C < 60° ✓ (C = m < 60°).
By Lemma 0,
  child1 = { 120°−B, B, 180−(120°−B)−B } = { 120°−B, B, 60° }  (contains θ = 60°),
  child2 = { A−(120°−B), m, (120°−B)+B } = { A+B−120°, m, 120° } = { 60°−m, m, 120° },
using A+B = 180°−m, so A+B−120° = 60°−m > 0. Shan-Yu cannot keep child1 (it contains θ), and child2
does not contain 60° (60°−m ≠ 60° since m>0; m ≠ 60°; 120° ≠ 60°). **So the survivor is
{ 60°−m, m, 120° }, which contains 120° = 2θ.**

**Move 2 (2θ-device).** Split the 120° vertex at x = θ = 60°. With neighbours 60°−m and m, Lemma 0
gives (taking B = 60°−m, C = m):
  child1 = { 60°, 60°−m, 180−60−(60°−m) } = { 60°, 60°−m, 60°+m }  (contains 60°),
  child2 = { 120°−60°, m, 60°+(60°−m) } = { 60°, m, 120°−m }        (contains 60°).
Both children contain θ = 60°. So whichever Shan-Yu keeps, the survivor contains θ and Mulan wins.

Hence θ = 60° is winnable in 2 moves against every Shan-Yu play. Since 60° ∉ {90/n}, **the
characterization "Mulan wins iff θ = 90/n" is false.** (Verified independently with exact `Fraction`
arithmetic on several starts.) ∎

The mechanism is general: the "injection" move (P-angle threat, x = 180°−θ−B) forces the constant
180°−θ into the survivor whenever a neighbour < θ is available; for θ = 60° this constant is exactly
2θ, so a single 2θ-device finishes. For other θ, 180°−θ is a further seed to peel/halve.

### 3. S2 — θ > 90° is never winnable (Proven)

**Device-classification lemma.** Let T = (A,B,C) with no angle equal to θ, and consider splitting
vertex A at parameter x. Both children contain θ **iff** (θ = 90°) or (A = 2θ).

*Proof.* By Lemma 0, child1 = {x, B, 180−x−B}. It contains θ iff x = θ, or B = θ, or 180−x−B = θ.
Since T has no angle θ, B ≠ θ, so: x = θ or x = 180−θ−B. Likewise child2 = {A−x, C, x+B} contains θ
iff A−x = θ, or C = θ (excluded), or x+B = θ; so x = A−θ or x = θ−B. Both children contain θ iff some
value from {θ, 180−θ−B} equals some value from {A−θ, θ−B}. The four cases:
  • x=θ and x=A−θ ⇒ θ = A−θ ⇒ **A = 2θ**.
  • x=θ and x=θ−B ⇒ B = 0, impossible (B > 0).
  • x=180−θ−B and x=A−θ ⇒ 180−B = A ⇒ C = 0, impossible.
  • x=180−θ−B and x=θ−B ⇒ 180−θ = θ ⇒ **θ = 90°**.
So the only non-degenerate possibilities are A = 2θ or θ = 90°. Conversely each is realizable:
A = 2θ with x = θ ∈ (0,2θ) gives both children containing θ; θ = 90° is the fork of §1(a). By vertex
symmetry, splitting at B (resp. C) requires B = 2θ (resp. C = 2θ) or θ = 90°. ∎

**Induction.** Suppose θ > 90°. Then θ = 90° is out, and any angle equal to 2θ > 180° is impossible in
a genuine triangle. So no split of any triangle (none of whose angles is θ) has both children in W₀:
W₁ = W₀. Inductively, if W_k = W₀ then "both children ∈ W_k = W₀" again means both children contain θ,
impossible by the device lemma; so W_{k+1} = W₀. Hence W(θ) = W₀. Shan-Yu picks any start with no
angle θ (possible since θ ≠ 60° would already be avoided by, say, the equilateral triangle; and for
any θ there is a continuum of triangles avoiding it). That start is not in W(θ), so Mulan can never
force θ. **θ > 90° is never winnable.** ∎

(Side effect: no angle > 90° is ever forceable, so obtuse angles cannot even serve as intermediate
"gift" seeds.)

## The corrected conjecture and the explicit-strategy setup (the open crux)

### 4. Generator analysis → conjectured answer

Combining Lemma 0′ with the device lemma, the ONLY Shan-Yu-immune ways to force a *specific constant*
into the survivor from a generic start are:

- **Fork:** force 90° (both children carry 90°; §1a). [seed 90]
- **Bisection:** split a vertex 2v at x = v ⇒ both children carry v. [generator v ↦ v/2]
- **Peel/threat (x = θ at vertex v > θ):** survivor {v−θ, C, θ+B}. [generator v ↦ v−θ, and, when a
  neighbour is a controlled constant w, v ↦ w+θ, i.e. +θ]
- **Injection (x = 180°−θ−B, needs a neighbour < θ):** survivor {θ−C, C, 180°−θ}. [seed 180°−θ, and
  reflection w ↦ θ−w for w < θ]
- **2θ-device:** from a vertex 2θ, force θ (win).

Every forced constant therefore lies in the ℤ[1/2]-module M = 90·ℤ[1/2] + θ·ℤ[1/2] (closure of the
seeds 90, 180−θ under ±θ and halving; note 180−θ = 2·90 − θ ∈ M). Solving "θ reachable":
θ = 90/2^a + θ·r with r ∈ ℤ[1/2] ⇔ θ(1−r) = 90/2^a ⇔ **θ = 90 / (2^a(1−r))**, and 2^a(1−r) ranges over
all dyadic rationals. So (subject to achievability) θ is forceable ⇔ **90/θ is a dyadic rational.**

Sharper, via the module structure: if θ/90 is irrational, 90 and θ are ℚ-independent and no
combination 90/2^a + θr equals θ — Mulan cannot win. If θ/90 = p/q in lowest terms, then M = (90/q)ℤ[1/2]
and one checks θ is reachable ⇔ q/(p·2^a) ∈ ℤ[1/2] for some a ⇔ **p is a power of 2** ⇔ 90/θ = q/p is
dyadic. Combining with S2 (θ > 90 excluded):

> **Conjectured answer.** Mulan can force victory **iff θ ≤ 90° and 90/θ is a dyadic rational**
> (equivalently: writing θ/90 = p/q in lowest terms, p is a power of 2). This set strictly contains
> {90/n} (e.g. 60 = 90·2/3, 72 = 90·4/5, 80 = 90·8/9 are in it) and excludes e.g. 50, 54, 75.

Small-case computer search (exact arithmetic, AND–OR with threat/device/bisect candidate moves)
confirms winnability for 90, 45, 30, 60, 36, 18 (all dyadic); other cases exceeded the search budget
and are inconclusive either way.

### 5. Explicit Shan-Yu strategy + potential (setup; preservation is the GAP)

Fix θ ≤ 90 with 90/θ NOT dyadic. Then either θ/90 is irrational, or θ/90 = p/q with p having an odd
prime factor ℓ. Shan-Yu picks a start with angles A₀, B₀ algebraically independent (transcendental)
over ℚ(θ) and in (0,60), C₀ = 180−A₀−B₀ (all positive, none equal θ). Define a per-angle potential

  d(α) = ∞ if α is transcendental over ℚ(θ);
  d(α) = the ℓ-adic obstruction v_ℓ( (90/θ)-representation of α ) — precisely, if α ∈ M lies in the
         reachable constant lattice, d(α) measures how far α is from θ inside the ℓ-adic (or dyadic)
         valuation of its θ/90-coordinates; d(α) = ∞ when no finite generator chain from α reaches θ
  (finite only when 90/θ is dyadic).
Set Φ(T) = min_α d(α), and Shan-Yu's rule: **keep the child maximizing Φ, breaking ties toward a
child with a transcendental angle.** Generic start has Φ = ∞.

**Claim to be proven (GAP G2):** when 90/θ is non-dyadic, a single split cannot produce two children
both with Φ < ∞; hence Shan-Yu's kept child always has Φ = ∞, so no angle ever equals θ (which would
need d = 0). The stress test is Mulan's collapse move x = c − B (c ∈ ℚ(θ)): both children drop to
transcendence degree 1 and one can be handed the constant c (even c = θ or 180−θ); one must show the
OTHER child retains a transcendental angle and stays in the "no finite ℓ-adic chain to θ" region,
i.e. Φ = ∞. This preservation — that the reachable-constant lattice never contains θ when 90/θ is
non-dyadic (odd prime ℓ obstruction) and that Mulan cannot inject a finite-d constant into BOTH
children — is exactly the Guaranteed-Constant Lemma, and is **NOT proven here.**

**Honest status of the potential.** The valuation d is only sketched, not made rigorous: I have not
defined the ℓ-adic chain-distance precisely on all of M, nor proven it is ∞ on the generic start, nor
proven non-collapse under the c−B move. These are the same difficulties the outline flagged, now
against the CORRECTED (dyadic) target rather than {90/n}. Correspondingly, the construction half (G1)
— realizing the generator chain as legal moves for every dyadic θ — is proven only for {90/n} and
θ=60. **The problem is not solved.**

## Spec concerns

- **The field's target answer is WRONG.** All three round-2 approaches (and current.md's intended
  answer) target **{90/n}**; θ = 60° is a rigorous 2-move counterexample (§2). The outline-reviewer's
  "S1 verified / S2 verified" is correct, but those only establish {90/n} ⊆ winning set and θ>90
  exclusion — they never verified the ⊆ direction "nothing outside {90/n} is winnable," which is false.
  **The orchestrator should retarget the whole run to the corrected conjecture** "θ ≤ 90 and 90/θ
  dyadic" (numerator of θ/90 in lowest terms is a power of 2). The three approaches' shared
  "Guaranteed-Constant Lemma / C(θ)" must be rebuilt with the dyadic lattice M = 90ℤ[1/2]+θℤ[1/2],
  not the (also-wrong) closure that yields {90/n}.
- The round-1 flag that a 2-adic invariant is "wrong" was itself half-right: a **dyadic/2-adic**
  condition IS the answer (90/θ dyadic), but as an obstruction via an ODD prime valuation of θ/90, not
  the naive "{90/2^k}". Do not discard 2-adic machinery — reframe it on 90/θ.
- Deep minimax search is not viable (branching + rational proliferation); do not rely on it to settle
  survival. The survival half needs the algebraic/valuation invariant.

## Promotable lemmas

- **Lemma 0 (cevian split normal form)** — proven in full (§0). Reusable by all approaches.
- **Lemma 0′ (AND–OR winning-set characterization)** — proven in full (§0). Reusable.
- **S1 construction lemma** (universal 90°-fork; θ-peel; ⇒ 90/n winnable in ≤ n moves) — proven in
  full (§1). Reusable.
- **Device-classification lemma** (both children of a split contain θ ⇔ θ=90° or split-vertex = 2θ) —
  proven in full (§3). Reusable; it is the engine of both S2 and the generator analysis.
- **S2 impossibility lemma** (θ>90° never winnable) — proven in full (§3). Reusable.
- **Refutation fact** (θ=60° winnable in 2 moves; {90/n} is not the answer) — proven in full (§2).
  Reusable and run-critical.
