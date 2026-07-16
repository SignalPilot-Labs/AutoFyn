# Approach: descending-chain

## Status
solved

## Approaches tried
- Round 1 (outline): three-phase strategy (grind / ignition / descent) for sufficiency + closed-family invariant for necessity — skeleton verified numerically (exact rational arithmetic, n = 2,…,10, 12, 15, 20).
- Round 2 (outline review): the Phase-D monovariant "largest multiple of θ present drops by θ each cut" was **refuted** (counterexample θ = 15°, T = (75°, 60°, 45°): cutting the 75° vertex with s = θ and companion 60° returns the same triangle (45°, 60°, 75°)). Do not revive it. Replaced by strong induction on the multiple index (Lemma A1 below) — companion-independent.
- Round 2 (build, this file): all gaps H0–H8 closed with the reviewer's fixes 1–3 applied; four-case closure lemma proved inline (per the shared-lemma condition; import `lemmas/safe-piece-exists.md` only after certification). Adversarial exact-rational simulation of the finished strategy: bound n−1 (n ∈ {2,3}) and 2n−4 (4 ≤ n ≤ 12) holds with 0 failures on 400 random triangles per n, all cut-validity assertions passing; closure lemma checked for θ ∈ {40°, 72°, 120°, 7/3°, 170°} on 2000 random safe triangles and random cuts each, 0 failures. (Checks are sanity only; the proof below is self-contained.)
- Recorded dead ends (keep): binary-halving descent (write-up complexity, no gain); doubling-orbit invariant {2^k θ} for necessity (not closed under the cut algebra; counterexample θ = 40°, T = (120°, 25°, 35°)).

## Current best
Complete proof of the full characterization, both directions, below. No open gaps.

## Full proof

**Answer.** Mulan can guarantee victory in finitely many steps **exactly for θ = 180°/n, n an integer ≥ 2**, i.e. for θ ∈ {90°, 60°, 45°, 36°, 30°, …}. Equivalently: exactly when 180/θ is an integer (θ ∈ (0°, 180°) then forces 180/θ ≥ 2).

Tools used (knowledge_base.md, "General Proof Methods"): strong **Induction**; **Casework / exhaustion**; **Invariant / monovariant** (the safety invariant in Direction B, the decreasing smallest angle in the grind); **Extremal principle** (cutting to the largest / smallest angle).

Throughout, angles are measured in degrees and a triangle is identified with the multiset of its three angles (positive reals summing to 180°). We restate the protocol: at the start of each iteration, if the current triangle T has an angle equal to θ the game stops and Mulan wins; otherwise Mulan chooses a point P on the perimeter of T, distinct from the vertices — so P lies in the interior of exactly one side — and cuts along the segment from P to the vertex opposite that side, producing two triangles; Shan-Yu chooses which one survives.

### Notation: congruence, multiples, safety

For real α, β write **α ≡ β (mod θ)** iff (α − β)/θ ∈ ℤ. This is an equivalence relation compatible with addition and subtraction (ℤ is closed under ±): if α ≡ α′ and β ≡ β′ then α ± β ≡ α′ ± β′ (mod θ).

Call α a **positive multiple of θ** if α = kθ for an integer k ≥ 1. For α ∈ (0°, 180°) — as every angle of every triangle in play is — we have: *α is a positive multiple of θ iff α ≡ 0 (mod θ)*. (If α ≡ 0 then α = kθ with k ∈ ℤ, and α > 0 with θ > 0 forces k ≥ 1; the converse is trivial.)

Call a triangle **safe** if none of its three angles is a positive multiple of θ, and **unsafe** otherwise. Since θ = 1·θ is itself a positive multiple, a safe triangle never triggers the stop-check.

### Lemma 0 (Cut formula and realizability)

*Let T have vertices U, V, W with angles u, v, w (u + v + w = 180°). Then:*

*(a) The legal cuts of T with P on side UW are in bijection with the parameters s ∈ (0, v) via s = ∠UVP; each such s is realized by a unique interior point P of segment UW.*

*(b) For that cut, the piece containing U is p₁ = (u, s, 180° − u − s) and the piece containing W is p₂ = (w, v − s, u + s); both are nondegenerate triangles.*

*(c) (Relabeling.) Swapping the roles of U and W replaces s by v − s and swaps p₁ ↔ p₂. Hence "cut to V with companion U and parameter s" — meaning the piece containing U receives the part s of the angle v — is a choice available to Mulan for every vertex V, every choice of companion among the other two vertices, and every s ∈ (0, v).*

**Proof.** (a) A point P on the perimeter, distinct from the vertices, lies in the interior of exactly one side; the cut goes to the opposite vertex. Fix the side UW, so the cut vertex is V. Parametrize P(t) = (1 − t)U + tW, t ∈ [0, 1], and set f(t) = ∠UVP(t), with f(0) = 0 and f(1) = ∠UVW = v. The function f is continuous: V does not lie on line UW, so the vectors U − V and P(t) − V are nonzero and depend continuously on t, and f(t) = arccos of their normalized inner product. It is strictly increasing: for 0 ≤ t₁ < t₂ ≤ 1, if t₁ = 0 then f(t₁) = 0 < f(t₂); if t₁ > 0 then P(t₁) is an interior point of segment U P(t₂), so (V being off line UW) the ray V P(t₁) lies strictly inside the angle ∠U V P(t₂), and angle addition gives ∠UVP(t₁) < ∠UVP(t₁) + ∠P(t₁)VP(t₂) = ∠UVP(t₂), both summands positive. A continuous strictly increasing function maps [0, 1] bijectively onto [f(0), f(1)] = [0, v] (Intermediate Value Theorem plus injectivity), so each s ∈ (0, v) corresponds to exactly one t ∈ (0, 1), i.e. one interior point P.

(b) In triangle UVP: the angle at U is ∠VUP = ∠VUW = u, because P lies on segment UW so ray UP equals ray UW; the angle at V is s by definition; the angle at P is 180° − u − s. In triangle PVW: the angle at W is ∠VWP = ∠VWU = w (same reason); the angle at V is ∠PVW = v − s by angle addition at V; the angle at P is 180° − w − (v − s) = u + s, using u + v + w = 180°. All six angles are strictly positive: u, w > 0; s, v − s ∈ (0, v) are positive; 180° − u − s = w + (v − s) > 0; u + s > 0. So both pieces are nondegenerate. (Consistency check: the two angles at P, namely 180° − u − s and u + s, sum to 180°, as supplementary angles at an interior point of segment UW must.)

(c) Immediate from (b) with the substitution s ↦ v − s; and Mulan chooses P, hence chooses s. ∎

---

## Direction A (sufficiency): θ = 180°/n with n ∈ ℤ, n ≥ 2 ⟹ Mulan wins

Standing hypothesis for this direction: **nθ = 180°**. Every angle in play lies in (0°, 180°), so the positive multiples of θ that can occur as angles are exactly kθ with 1 ≤ k ≤ n − 1.

### Lemma A1 (Descent)

*For every integer k with 1 ≤ k ≤ n − 1: if the current triangle has an angle equal to kθ, then Mulan can force the game to stop (with her victory) after at most k − 1 further cuts, whatever Shan-Yu does.*

**Proof.** Strong induction on k.

*Base k = 1.* The triangle has an angle θ, so the stop-check at the start of the iteration ends the game: 0 further cuts.

*Step k ≥ 2.* Assume the statement for all k′ with 1 ≤ k′ < k. Let V be a vertex of the current T with angle v = kθ, and let u, w be the other two angles. Mulan cuts to V with parameter s = θ; this is valid by Lemma 0 since θ ∈ (0, kθ) (here k ≥ 2 gives θ < kθ, and both inequalities are strict, so P is a non-vertex perimeter point). By Lemma 0(b) the pieces are

p₁ = (u, θ, 180° − u − θ) and p₂ = (w, (k − 1)θ, u + θ).

Shan-Yu keeps one of them:
- If he keeps p₁, it has an angle equal to θ, so the stop-check of the next iteration ends the game. Total: 1 ≤ k − 1 cuts.
- If he keeps p₂, it has the angle (k − 1)θ with 1 ≤ k − 1 < k; by the induction hypothesis Mulan forces the stop within (k − 1) − 1 = k − 2 further cuts. Total: 1 + (k − 2) = k − 1 cuts.

Both of Shan-Yu's options are covered, so the bound k − 1 holds. ∎

**Remark (why not a monovariant).** The statement "the largest multiple of θ present drops by θ each cut" is false: for θ = 15°, T = (75°, 60°, 45°), cutting the 75° vertex with s = θ and companion the 60° vertex returns the piece (45°, 60°, 75°) — the same triangle. Lemma A1 avoids this: the induction hypothesis needs only that the kept piece has *some* angle k′θ with k′ < k, which holds for p₂ regardless of the companion choice and regardless of what other multiples are present.

### Lemma A2 (Ignition)

*Suppose the current T is safe and its smallest angle x satisfies x < θ. Then Mulan has a valid cut whose two pieces are*

p₁ = (x, θ − x, (n − 1)θ) and p₂ = (y, z − θ + x, θ),

*where x ≤ y ≤ z are the angles of T. In particular one piece contains θ and the other contains (n − 1)θ (for n = 2 both contain θ, since (n − 1)θ = θ).*

**Proof.** Label the angles x ≤ y ≤ z at vertices X, Y, Z (ties broken arbitrarily). Mulan cuts to Z with companion X and parameter s = θ − x (Lemma 0 with v = z, u = x, w = y).

*Validity: s ∈ (0, z).* First, s > 0 because x < θ. Second, s < z: since y ≤ z, we get 180° = x + y + z ≤ x + 2z, so z ≥ 90° − x/2; hence

z − s ≥ (90° − x/2) − (θ − x) = (90° − θ) + x/2 > 0,

because θ = 180°/n ≤ 90° for n ≥ 2 and x > 0. So 0 < s < z, and by Lemma 0(a) the cut is legal (P a non-vertex point of side XY).

*Pieces (Lemma 0(b)):*

p₁ = (x, s, 180° − x − s) = (x, θ − x, 180° − θ) = (x, θ − x, (n − 1)θ),

since 180° − x − (θ − x) = 180° − θ = (n − 1)θ (note the third angle is independent of y and z — this is what choosing the *smallest* angle as companion buys);

p₂ = (y, z − s, x + s) = (y, z − θ + x, θ).

All angles positive: for p₁, x > 0, θ − x > 0, 180° − θ > 0 (θ < 180°); for p₂, y > 0, z − s > 0 as shown, x + s = θ ∈ (0°, 180°). ∎

**Consequence A2′.** From a safe position with x < θ, Mulan wins within n − 1 cuts: she plays the Lemma A2 cut (1 cut). If Shan-Yu keeps p₂, it contains θ and the next check ends the game (total 1 ≤ n − 1). If he keeps p₁, it contains the angle (n − 1)θ; Lemma A1 with k = n − 1 finishes within n − 2 further cuts (for n = 2 this reads k = 1: p₁ contains θ and the game ends at once). Total ≤ 1 + (n − 2) = n − 1.

### Lemma A3 (Grind)

*Suppose the current T is safe and all its angles exceed θ (this forces n ≥ 4: the smallest angle x satisfies x ≤ 60° always, so x > θ requires θ < 60°, i.e. n > 3). Then Mulan has a valid cut such that one piece contains θ and the other piece is* safe *with smallest angle exactly x − θ.*

**Proof.** Let the angles be x ≤ y ≤ z at vertices X, Y, Z. Mulan cuts to X with companion Y and parameter s = x − θ (Lemma 0 with v = x, u = y, w = z).

*Validity:* s = x − θ > 0 since x > θ, and s = x − θ < x since θ > 0; both strict, so s ∈ (0, x) and the cut is legal.

*Pieces (Lemma 0(b)):*

p₁ = (y, x − θ, 180° − y − (x − θ)) = (y, x − θ, z + θ), using 180° − y − x = z;

p₂ = (z, x − s, y + s) = (z, θ, y + x − θ).

p₂ contains θ. For p₁:

- *p₁ is safe.* Modulo θ its angles satisfy y ≡ y, x − θ ≡ x, z + θ ≡ z. Since T is safe, none of x, y, z is ≡ 0 (mod θ); hence none of p₁'s angles is ≡ 0 (mod θ). Each angle of p₁ lies in (0°, 180°) (three positive reals summing to 180° are each < 180°), so by the equivalence in the Notation section none is a positive multiple of θ: p₁ is safe.
- *p₁'s smallest angle is x − θ:* y ≥ x > x − θ and z + θ > z ≥ x > x − θ.

∎

**Remarks addressing the boundary bookkeeping.** (i) The value x − θ = θ (i.e. x = 2θ) cannot occur here, since T is safe. (ii) More importantly, safety of the kept piece p₁ means the next position re-enters case (II) or case (III) of the trichotomy below — never case (I) — so the grind never accidentally hands the play to the descent phase mid-grind, and its step count below is exact.

### Proposition A (Sufficiency, with explicit bounds)

*If θ = 180°/n with n an integer ≥ 2, then from every initial triangle Mulan forces a win within at most n − 1 cuts when n ∈ {2, 3}, and at most 2n − 4 cuts when n ≥ 4.*

**Proof.** Consider any position T at the start of an iteration at which the game has not stopped, i.e. no angle of T equals θ. Exactly one of the following holds:

- **(I)** T has an angle kθ with 2 ≤ k ≤ n − 1 (T unsafe);
- **(II)** T is safe and its smallest angle x satisfies x < θ;
- **(III)** T is safe and x > θ.

*Exhaustiveness:* if T is unsafe, some angle equals kθ with k ≥ 1; k = 1 is excluded (the game did not stop) and kθ < 180° = nθ forces k ≤ n − 1, so (I) holds. If T is safe then x is not a positive multiple of θ, in particular x ≠ θ, so (II) or (III) holds. *Disjointness* is clear. As noted in Lemma A3, case (III) is empty unless n ≥ 4.

Mulan's strategy and the count:

- **From (I):** apply Lemma A1 with the given k ≤ n − 1: the game stops in Mulan's favor within k − 1 ≤ n − 2 cuts. (For n = 2 this case is vacuous: k ≥ 2 would need kθ ≥ 180°.)
- **From (II):** by Consequence A2′, Mulan wins within n − 1 cuts.
- **From (III)** (so n ≥ 4): let x₀ be the smallest angle. Since y, z > θ, we get x₀ = 180° − y − z < 180° − 2θ = (n − 2)θ; since x₀ > θ and x₀ is not a multiple of θ (safety), x₀ ∈ (mθ, (m + 1)θ) for an integer m with 1 ≤ m ≤ n − 3. Mulan plays the Lemma A3 cut repeatedly. At each such cut, if Shan-Yu keeps the piece containing θ, the next check ends the game at once. Otherwise the kept piece is safe with smallest angle exactly θ smaller. So after j consecutive grind cuts with the game still running, the position is safe with smallest angle x₀ − jθ ∈ ((m − j)θ, (m − j + 1)θ). For j ≤ m − 1 this smallest angle exceeds θ: case (III) again, grind once more. At j = m it lies in (0°, θ): case (II). Hence within m ≤ n − 3 grind cuts the play either has already ended with Mulan's win or has reached case (II), from which Consequence A2′ wins within n − 1 further cuts. Total ≤ (n − 3) + (n − 1) = 2n − 4.

Finally, the initial position: if Shan-Yu's chosen T has an angle θ, the game stops immediately (0 cuts). Otherwise it falls into exactly one of (I), (II), (III) and the above applies. Every prescribed cut was verified legal in Lemmas A1–A3, and at every cut both of Shan-Yu's options were handled, so this is a complete winning strategy. The overall bounds: for n ∈ {2, 3}, case (III) is empty and max(n − 2, n − 1) = n − 1; for n ≥ 4, max(n − 2, n − 1, 2n − 4) = 2n − 4. In all cases the number of steps is bounded by a finite constant depending only on n, so Mulan guarantees victory in finitely many steps. ∎

*(Spot check, n = 2, θ = 90°: any triangle without a right angle has smallest angle x ≤ 60° < 90° and is automatically safe, so it is in case (II); the ignition cut gives pieces (x, 90° − x, 90°) and (y, z − 90° + x, 90°) — both contain 90°, so Mulan wins in exactly 1 = n − 1 cut. Spot check, n = 3, θ = 60°: case (III) is empty; case (I) means an angle of 120°, one descent cut; case (II) needs ≤ 2 = n − 1 cuts.)*

---

## Direction B (necessity): 180/θ ∉ ℤ ⟹ Mulan cannot guarantee victory

Standing hypothesis for this direction: **180/θ is not an integer**, i.e. 180° ≢ 0 (mod θ). This covers uniformly: θ > 90° (then 180/θ ∈ (1, 2)), rational θ that do not divide 180° (e.g. 40°, 72°, 120°), and irrational θ.

### Lemma B1 (Safe start)

*There exists a safe triangle.*

**Proof.** The positive multiples of θ lying in (0°, 180°) are kθ, 1 ≤ k < 180/θ — a finite set M with |M| ≤ 180/θ. Consider the isoceles family T_α = (α, α, 180° − 2α) for α ∈ (0°, 90°). T_α is unsafe iff α ∈ M or 180° − 2α ∈ M, i.e. iff α lies in the finite set M ∪ {(180° − μ)/2 : μ ∈ M} of at most 2|M| values. The interval (0°, 90°) is infinite, so some (indeed all but finitely many) α gives a safe T_α. ∎

### Lemma B2 (Closure — the safe-piece lemma, proved inline)

*Assume 180/θ ∉ ℤ. If T is safe, then for* every *legal cut of T — every choice of vertex and every parameter — at least one of the two pieces is safe.*

**Proof.** By Lemma 0 and its relabeling remark (c), an arbitrary legal cut is described by: a vertex V with angle v, a companion vertex U with angle u, the third angle w (u + v + w = 180°), and a parameter s ∈ (0, v), with pieces

p₁ = (u, s, 180° − u − s), p₂ = (w, v − s, u + s).

Since T is safe: u ≢ 0, v ≢ 0, w ≢ 0 (mod θ). Recall (Notation) that for angles in (0°, 180°), "positive multiple of θ" is equivalent to "≡ 0 (mod θ)", and every angle of p₁, p₂ lies in (0°, 180°).

Suppose toward a contradiction that both pieces are unsafe.

- p₁ unsafe means one of its angles is ≡ 0 (mod θ); its angle u is ≢ 0, so **s ≡ 0 or 180° − u − s ≡ 0**.
- p₂ unsafe means one of its angles is ≡ 0; its angle w is ≢ 0, so **v − s ≡ 0 or u + s ≡ 0**.

These two binary disjunctions give exactly four combinations; congruences may be added and subtracted (Notation):

1. **s ≡ 0 and v − s ≡ 0:** then v = s + (v − s) ≡ 0 (mod θ) — contradicts v ≢ 0.
2. **s ≡ 0 and u + s ≡ 0:** then u = (u + s) − s ≡ 0 (mod θ) — contradicts u ≢ 0.
3. **180° − u − s ≡ 0 and v − s ≡ 0:** then w = (180° − u − s) − (v − s) ≡ 0 (mod θ), using u + v + w = 180° — contradicts w ≢ 0.
4. **180° − u − s ≡ 0 and u + s ≡ 0:** then 180° = (180° − u − s) + (u + s) ≡ 0 (mod θ), i.e. 180/θ ∈ ℤ — contradicts the standing hypothesis.

All four cases are impossible, so at least one piece is safe. ∎

### Proposition B (Necessity)

*If 180/θ ∉ ℤ, then Shan-Yu has a strategy under which the game never stops. Consequently Mulan cannot guarantee victory in finitely many steps.*

**Proof.** Shan-Yu's strategy: choose an initial safe triangle T₀ (exists by Lemma B1); thereafter, whenever Mulan cuts, keep a safe piece (one exists by Lemma B2, applicable because the current triangle is safe by induction).

We verify by induction on the iteration number that the triangle at the start of every iteration is safe. Base: T₀ is safe. Step: if the current T is safe, then θ — being the positive multiple 1·θ, and θ ∈ (0°, 180°) — is not among its angles, so the stop-check does not fire and the game continues; Mulan makes some legal cut; by Lemma B2 at least one piece is safe, and Shan-Yu keeps it, so the next iteration also starts with a safe triangle.

Hence under this strategy the stop condition never holds, at any finite time: the game runs forever and Mulan never wins. In particular, no Mulan strategy guarantees victory in finitely many steps. ∎

---

## Conclusion and verification of the answer

For θ ∈ (0°, 180°): 180/θ ∈ ℤ ⟺ θ = 180°/n for an integer n, and θ < 180° forces n ≥ 2, while conversely every integer n ≥ 2 gives θ = 180°/n ∈ (0°, 90°] ⊂ (0°, 180°). Proposition A shows Mulan wins (within max(n − 1, 2n − 4) steps) for every such θ; Proposition B shows she cannot force a win for any other θ in (0°, 180°). Therefore

**Mulan can guarantee victory in finitely many steps exactly for θ ∈ {180°/n : n ∈ ℤ, n ≥ 2}.**

Verification by substitution (rigor rule):

- **θ = 90° (n = 2, in the set):** any triangle without a 90° angle has smallest angle x ≤ 60° < 90°; the ignition cut of Lemma A2 (to the largest angle z, companion x, s = 90° − x; valid since z − s ≥ (90° − 90°) + x/2 > 0) produces pieces (x, 90° − x, 90°) and (y, z − 90° + x, 90°) — *both* contain 90°, so Mulan wins in one cut, matching the bound n − 1 = 1.
- **θ = 40° (not in the set, 180/40 = 4.5):** Shan-Yu starts with (65°, 65°, 50°); 65/40 and 50/40 are not integers, so it is safe, and Lemma B2 lets him stay safe forever.
- **θ = 120° (not in the set, 180/120 = 1.5):** Shan-Yu starts with (50°, 50°, 80°); none of 50°, 80° is a positive multiple of 120°, so it is safe; same conclusion. ∎

## Promotable lemmas

- **Cut Formula** (Lemma 0 above, proved in full here): the parametrization of all legal cuts, the piece-angle formula p₁ = (u, s, 180° − u − s), p₂ = (w, v − s, u + s), realizability of every s ∈ (0, v) by a unique non-vertex P, and the companion-relabeling remark. Candidate file: `lemmas/cut-formula.md`. Used by both live approaches.
- **Descent Lemma** (Lemma A1 above, proved in full here; identical in content to remainder-forcing's G1): a triangle with an angle kθ (θ = 180°/n, 1 ≤ k ≤ n − 1) loses within k − 1 cuts. Candidate file: `lemmas/descent.md`.
- **Safe-piece / Closure Lemma** (Lemma B2 above, proved in full inline; = remainder-forcing's G5): when 180/θ ∉ ℤ, every cut of a safe triangle leaves a safe piece. The remainder-forcing builder is filing this as `lemmas/safe-piece-exists.md` this round; once certified, this file's inline copy may be replaced by an import.
