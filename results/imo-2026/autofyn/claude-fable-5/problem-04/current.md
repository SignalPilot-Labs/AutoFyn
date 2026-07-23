# imo-2026-04 — Mulan's triangle game

## Status
solved

## Approaches tried
- **residue-divisibility-characterization** — worked (round 1). Complete correct proof: mod-θℤ cleanness invariant for necessity, fork-to-multiples + downward induction for sufficiency, θ = 90° routed through a direct one-cut win. Verified independently by the proof-reviewer (exact-geometry check of the cut model; exact-fraction search for the four-case invariant at θ = 55, 80, 100, 170, 179, 270/7; exhaustive-keep game-tree simulation of the strategy for n = 2..12, bound n−1 attained). One presentational nit only (Lemma 2 step omits the trivial remark that the triangle may already contain θ, in which case the game has stopped); this does not affect correctness. Serves as an independent verification of the certified proof below.
- **circle-group-quotient** — worked (round 1). The same mathematics organized through the quotient group G = ℝ/θℤ with σ = [180]; slightly cleaner write-up (its Lemma 4.2 handles the early-stop case explicitly, and all size/boundary bookkeeping is isolated in lifting lemmas). **Certified as the Full proof below.**
- (Field history) "Mulan wins iff θ ≤ 90°" — dead end; refuted by the residue invariant (θ = 80° is a Shan-Yu survival).

## Current best
Solved. **Answer: Mulan can guarantee victory in finitely many steps if and only if θ = 180°/n for some integer n ≥ 2** (equivalently, iff 180/θ ∈ ℤ); moreover for θ = 180°/n she wins within at most n − 1 cuts. Two independent complete proofs exist in `approaches/`; the certified one follows.

## Full proof

(Certified from `approaches/circle-group-quotient.md`, round 1; independently verified against `approaches/residue-divisibility-characterization.md` and by direct computation.)

Throughout, angles are measured in degrees and identified with real numbers; θ ∈ (0, 180) is fixed. A *state* of the game is the current paper triangle, recorded by its (unordered) triple of angles — three positive reals summing to 180. The game protocol, from the statement: Shan-Yu chooses the initial triangle; then, repeatedly, **at the start of each round** the stop-check is performed (if some angle of 𝒯 equals θ exactly, the game stops and Mulan wins); otherwise Mulan chooses a perimeter point distinct from the vertices, cuts to the opposite vertex, and Shan-Yu keeps one of the two resulting triangles. (Note the check also applies to the initial triangle.) Any prescribed triple of positive reals summing to 180 is realizable as a triangle, so Shan-Yu's initial choice is exactly a choice of such a triple.

### Section 0 — The cut model (geometry only)

**Lemma 0 (cut model).** Let 𝒯 have angles P, Q, R at vertices A, B, C respectively. Mulan's legal moves at 𝒯 are exactly the pairs (attacked vertex, split parameter): choosing a vertex — say C, with angle R — and a real t ∈ (0, R), producing the two children with angle triples
- C₁ = (P, t, Q + R − t) and C₂ = (Q, R − t, P + t),
both nondegenerate triangles (all angles positive). Shan-Yu then keeps C₁ or C₂ at his choice.

*Proof.* A perimeter point X distinct from the vertices lies in the interior of exactly one side; say X ∈ AB (interior), so the opposite vertex is C, and the cut is the segment XC. Since X is interior to AB, the segment XC lies inside 𝒯 and splits it into the genuine triangles AXC and BXC. Let t := ∠ACX. Since the ray CX lies strictly between the rays CA and CB, we have t ∈ (0, R), and ∠XCB = R − t. Triangle AXC has angles P (at A), t (at C), and 180 − P − t = Q + R − t (at X, using P + Q + R = 180); triangle BXC has angles Q (at B), R − t (at C), and 180 − Q − (R − t) = P + t (at X). This gives C₁, C₂ as stated; all six listed angles are positive since each is an angle of a nondegenerate triangle (explicitly: t > 0, R − t > 0, P, Q > 0, hence Q + R − t = Q + (R − t) > 0 and P + t > 0).

Conversely, every pair (C, t) with t ∈ (0, R) is realizable: draw the ray ρ from C making angle t with the ray CA on the same side as CB. Since 0 < t < R, ρ lies strictly between rays CA and CB, so by the Crossbar Theorem (elementary plane geometry) ρ meets the opposite side AB in a point X interior to AB; that X is a legal choice for Mulan realizing the split t. The same holds for the other two vertices by relabeling. ∎

From now on the game is played on angle triples with moves given by Lemma 0.

### Section 1 — Setup of the quotient

Let G := ℝ/θℤ, the quotient of the additive group ℝ by the subgroup θℤ = {kθ : k ∈ ℤ}, and let [x] ∈ G denote the class of x ∈ ℝ; thus [x] = [y] iff x − y ∈ θℤ. Set

σ := [180] ∈ G.

Project a state (P, Q, R) to the *multiset* π(P, Q, R) = {[P], [Q], [R]} of elements of G. The multiset (rather than an ordered triple) is the right quotient state because, by Lemma 0, a move is symmetric in the two untouched angles and the attacked angle may be any of the three.

Two one-line observations:

**(1a) Terminal states project onto [0].** If a triangle has an angle exactly θ, then that angle's class is [θ] = [0]; so every state at which the game stops (Mulan wins) has [0] among its projected elements.

**(1b) Sum invariant.** For any state, [P] + [Q] + [R] = [P + Q + R] = [180] = σ. In particular both children of any cut also have projected element-sum σ, since their angles also sum to 180. (Direct check from Lemma 0: [P] + [t] + [Q + R − t] = [P + Q + R] = σ and [Q] + [R − t] + [P + t] = [P + Q + R] = σ.)

Everything in Section 2 takes place in G; **no size information is used there**.

### Section 2 — The quotient dichotomy (algebra in G only)

Call a state *clean* if no element of its projection is [0], i.e. none of P, Q, R lies in θℤ.

**Lemma 2A (Shan-Yu closure when σ ≠ 0).** Suppose σ ≠ 0 in G. If a state (P, Q, R) is clean, then for every legal move of Mulan (any attacked angle, any split parameter t), at least one of the two children is clean.

*Proof.* By the symmetry of Lemma 0 — relabeling exchanges the two untouched angles, and the attacked angle is an arbitrary element of the triple — we may name the attacked angle R and the untouched pair P, Q; the argument below is invariant under swapping P and Q, so this single computation covers all three attack choices. Write τ := [t] ∈ G. The children project to

π(C₁) = {[P], τ, [Q] + [R] − τ}, π(C₂) = {[Q], [R] − τ, [P] + τ}.

Since the state is clean, [P] ≠ 0 and [Q] ≠ 0. Hence:
- C₁ fails to be clean iff τ = 0 or τ = [Q] + [R];
- C₂ fails to be clean iff [R] − τ = 0 or [P] + τ = 0, i.e. τ = [R] or τ = −[P].

If both children failed to be clean, then τ ∈ {0, [Q] + [R]} ∩ {[R], −[P]}, giving four exhaustive cases:
1. 0 = [R] — contradicts cleanness ([R] ≠ 0).
2. 0 = −[P], i.e. [P] = 0 — contradicts cleanness.
3. [Q] + [R] = [R], i.e. [Q] = 0 — contradicts cleanness.
4. [Q] + [R] = −[P], i.e. [P] + [Q] + [R] = 0; by (1b) this says σ = 0 — contradicts the hypothesis σ ≠ 0.

All four cases are impossible, so at least one child is clean. ∎

**Lemma 2B (the fork when σ = 0).** Suppose σ = 0 in G. If a state (P, Q, R) is clean, then for any choice of attacked angle — name it R — every t with [t] = −[P] makes **both** children contain the element [0] in their projections.

*Proof.* With τ = −[P]: in π(C₂) the element [P] + τ = 0; in π(C₁) the element [Q] + [R] − τ = [Q] + [R] + [P] = σ = 0 by (1b). ∎

Note Lemma 2B asserts nothing about the existence of a *legal* t (i.e. one in (0, R)) in the class −[P]; that is size information, deferred to Section 4.

### Section 3 — Necessity: if σ ≠ 0, Shan-Yu survives forever

Suppose σ ≠ 0, i.e. 180 ∉ θℤ, i.e. 180/θ ∉ ℤ. We give Shan-Yu a strategy under which the game never stops, so Mulan cannot guarantee victory in finitely many steps. Projection only forgets information, so the quotient obstruction lifts for free; the only thing to check with sizes is the existence of a clean initial triangle.

**Initial choice.** Shan-Yu picks the isoceles triple (ε, ε, 180 − 2ε) with ε ∈ (0, min(θ, 90)) chosen as follows. Such a triple is a valid triangle for every ε in that interval (all entries positive, sum 180, since ε < 90). It fails to be clean only if ε ∈ θℤ — impossible, as 0 < ε < θ — or if 180 − 2ε ∈ θℤ, i.e. ε = (180 − mθ)/2 for some integer m; since ε is confined to a bounded interval, only finitely many integers m yield a value in it, so the excluded set is finite. An open interval minus a finite set is nonempty; Shan-Yu picks any surviving ε and starts with a clean triangle.

**Maintenance.** At every round, the current state is clean by induction: it is clean initially, and whatever cut Mulan makes, Lemma 2A guarantees at least one clean child; Shan-Yu keeps a clean child. (Lemma 2A quantifies over all attacked angles and all τ ∈ G, hence in particular over all legal t ∈ (0, attacked angle) from Lemma 0.)

**Conclusion.** In a clean state no angle lies in θℤ; in particular no angle equals θ (whose class is [0], by (1a) applied in reverse: an angle equal to θ is in θℤ). So the stop-check never triggers: at every round the game continues, and Mulan always has a legal move (Lemma 0), so the game runs forever without Mulan winning. Hence for every Mulan strategy and every N ∈ ℕ, after N steps she has not won: Mulan cannot guarantee victory in finitely many steps. ∎ (necessity)

### Section 4 — Sufficiency: if σ = 0, Mulan wins within n − 1 cuts

Suppose σ = 0, i.e. 180 = nθ for some integer n; since 0 < θ < 180 we have n = 180/θ > 1, so n ≥ 2. This section contains the size arguments; residues enter only through the interface Lemma 4.1 and through the phrase "angle in θℤ", which here just means "angle equal to kθ for some integer k". Note that an angle x of a triangle satisfies 0 < x < 180 = nθ, so x ∈ θℤ iff x = kθ for a **unique** integer k with 1 ≤ k ≤ n − 1.

**Lemma 4.1 (Lift 1: sized representative).** Let x ∈ ℝ with x ∉ θℤ. Then the coset −x + θℤ has a unique representative t₀ in [0, θ), and t₀ ≠ 0; hence t₀ ∈ (0, θ), strictly at both ends.

*Proof.* Every coset of θℤ in ℝ meets [0, θ) in exactly one point (take t₀ = −x − θ⌊−x/θ⌋). If t₀ = 0 then −x ∈ θℤ, hence x ∈ θℤ, contradiction. And t₀ < θ by construction. ∎

**Lemma 4.2 (Lift 2: finishing from an exact multiple).** Let θ = 180/n, n ≥ 2. If the current triangle has an angle equal to kθ exactly, for an integer k with 1 ≤ k ≤ n − 1, then Mulan wins using at most k − 1 further cuts, no matter how Shan-Yu plays.

*Proof.* Strong induction on k.

*Base k = 1:* the triangle has an angle exactly θ, so at the round-start check the game stops and Mulan has won, with 0 further cuts.

*Step k ≥ 2:* if the triangle also has an angle equal to θ, the game stops as above (0 cuts). Otherwise, let the angle kθ sit at some vertex, and let A, B be the other two angles. Mulan attacks the vertex with angle kθ using split parameter t = θ. This is legal by Lemma 0: since k ≥ 2, we have 0 < θ < kθ. By Lemma 0 the children are

C₁ = (A, θ, B + kθ − θ) and C₂ = (B, kθ − θ, A + θ) = (B, (k−1)θ, A + θ),

both nondegenerate. C₁ contains the angle θ exactly; C₂ contains the angle (k−1)θ exactly, and 1 ≤ k − 1 ≤ n − 1. Whichever child Shan-Yu keeps: if C₁, the next round-start check stops the game (total: 1 cut ≤ k − 1 since k ≥ 2); if C₂, the induction hypothesis applied to k − 1 gives a win in at most k − 2 further cuts (total: 1 + (k − 2) = k − 1). ∎

**Lemma 4.3 (main fork, n ≥ 3).** Let θ = 180/n with n ≥ 3, and let the current triangle (P, Q, R) have no angle in θℤ. Then Mulan has a legal cut after which **both** children contain an angle that is an exact multiple kθ, 1 ≤ k ≤ n − 1.

*Proof.* Label R a largest angle of the triangle and P, Q the other two. Since 3R ≥ P + Q + R = 180, we have R ≥ 60. Since n ≥ 3, θ = 180/n ≤ 60. As P ∉ θℤ, Lemma 4.1 gives the representative t₀ ∈ (0, θ) of the coset −P + θℤ, i.e. P + t₀ ∈ θℤ. Then

0 < t₀ < θ ≤ 60 ≤ R,

with the second inequality strict, so t₀ ∈ (0, R): the cut (attack R, parameter t₀) is legal by Lemma 0. Its children are C₁ = (P, t₀, Q + R − t₀) and C₂ = (Q, R − t₀, P + t₀), both nondegenerate. Now check the exact multiples, using only that P + t₀ ∈ θℤ and P + Q + R = 180 = nθ:
- In C₂: the angle P + t₀ lies in θℤ; being an angle of a nondegenerate triangle it lies in (0, 180), hence equals kθ for a unique 1 ≤ k ≤ n − 1.
- In C₁: the angle Q + R − t₀ = 180 − P − t₀ = nθ − (P + t₀) ∈ θℤ; again it lies in (0, 180), hence equals k′θ for a unique 1 ≤ k′ ≤ n − 1. ∎

**Lemma 4.4 (θ = 90°, one-move universal fork).** Let θ = 90 (n = 2). From any triangle with no angle equal to 90, Mulan has a legal cut after which both children contain an angle of exactly 90; hence she wins with exactly 1 cut.

*Proof.* Let R be a largest angle, P, Q the others. Then P, Q < 90: if R ≥ 90 then P + Q = 180 − R ≤ 90 with P, Q > 0, so each is < 90; if R < 90 then P, Q ≤ R < 90. Mulan attacks R with t := 90 − P. Legality (Lemma 0): t > 0 since P < 90; and t < R ⟺ 90 − P < R ⟺ 90 < P + R = 180 − Q ⟺ Q < 90, which holds. The children are C₁ = (P, t, Q + R − t) with Q + R − t = Q + R − 90 + P = 180 − 90 = 90, and C₂ = (Q, R − t, P + t) with P + t = 90. Both contain 90; whichever Shan-Yu keeps, the next round-start check stops the game and Mulan wins. ∎

(For θ = 90, the angles in θℤ ∩ (0, 180) are exactly {90}, so "no angle equal to 90" is precisely the condition under which the round continues — Lemma 4.4 needs no cleanness hypothesis beyond that.)

**Assembly of sufficiency.** Let θ = 180/n, n ≥ 2. Mulan's strategy, from any current triangle (checked at round start):

- If some angle equals θ: the game has already stopped and she has won.
- Else, if n = 2: apply Lemma 4.4 — win after 1 cut. Total ≤ 1 = n − 1 cuts.
- Else (n ≥ 3), if some angle lies in θℤ: it equals kθ for a unique 2 ≤ k ≤ n − 1 (k = 1 is the first bullet); by Lemma 4.2, win in ≤ k − 1 ≤ n − 2 further cuts.
- Else (n ≥ 3, no angle in θℤ): apply the fork of Lemma 4.3. Whichever child Shan-Yu keeps contains an exact multiple kθ, 1 ≤ k ≤ n − 1; by Lemma 4.2 Mulan wins in ≤ k − 1 ≤ n − 2 further cuts. Total ≤ 1 + (n − 2) = n − 1 cuts.

The cases are exhaustive and disjoint, cover every possible initial triangle of Shan-Yu (including one already containing θ, one containing a higher multiple of θ, and the equilateral triangle — which for n = 3 has all angles 60 = θ, an immediate win, and for n ≥ 4 has angles 60 that may or may not be multiples of θ, both cases covered above), and every branch terminates in at most n − 1 cuts regardless of Shan-Yu's discards. So Mulan guarantees victory in finitely many (indeed ≤ n − 1) steps. ∎ (sufficiency)

### Section 5 — Conclusion and answer

By definition, σ = [180] = 0 in ℝ/θℤ ⟺ 180 ∈ θℤ ⟺ 180/θ ∈ ℤ; and since 0 < θ < 180 forces 180/θ > 1, this integer is some n ≥ 2. Section 3 shows Mulan cannot guarantee victory when σ ≠ 0; Section 4 shows she guarantees victory within n − 1 cuts when σ = 0. Therefore:

**Answer.** Mulan can guarantee victory in finitely many steps **exactly for θ = 180°/n, n an integer ≥ 2**, i.e. θ ∈ {90°, 60°, 45°, 36°, 30°, …} = {θ ∈ (0°, 180°) : 180/θ ∈ ℤ}.

*Verification of the answer against the two directions:* for θ = 90° (n = 2), Lemma 4.4 exhibits an explicit one-cut win from every start; for a non-member such as θ = 80° (180/80 = 9/4 ∉ ℤ), Section 3's strategy (start clean, e.g. (ε, ε, 180 − 2ε) with ε = 1, since 1, 178 ∉ 80ℤ; keep a clean child by Lemma 2A) lets Shan-Yu survive forever. ∎
