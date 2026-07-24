# imo-2026-04 — Mulan's Triangle Game (IMO 2026 P4)

## Status
solved

## Approaches tried
- residue-invariant (mod-θ algebra in ℝ/θℤ) — **solved / APPROVE**. Necessity via the "good
  triangle" residue invariant (Lemma A), sufficiency via alignment cut (Lemma B) + θ-peel (Lemma C).
- geometric-forcing-extremal (raw-degree arithmetic, independent of the quotient group) —
  **solved / APPROVE**. Necessity via fixed-sum covering (Lemma D) + independent non-obtuse
  invariant for θ>90, sufficiency via extremal alignment from the largest vertex (Lemma E) + peel (Lemma F).

Both approaches independently reach and rigorously prove the same characterization. Reviewer
re-derived every load-bearing step and confirmed by numerical minimax: necessity invariant holds
in 200000/200000 trials; Mulan's explicit strategy wins from all random starts for n=2..12 against
adversarial Shan-Yu, including near-equilateral (n=3) and near-right (n=2) boundaries.

## Current best
Complete two-directional proof (below).

## Full proof

**Answer.** Mulan can guarantee victory in finitely many steps **iff θ = 180°/n for some integer
n ≥ 2**, equivalently iff θ divides 180° (180/θ ∈ ℤ). Since 0° < θ < 180°, every such θ satisfies
θ ≤ 90°: the winning set is {90°, 60°, 45°, 36°, 30°, …} = {180/n : n ≥ 2}.

Throughout, a triangle is an unordered triple of positive angle-measures summing to 180; the game
stops (Mulan wins) the instant some angle equals θ.

### 0. Move algebra
Cut from apex A (angle α) to point P on the open opposite side BC (base angles β at B, γ at C,
α+β+γ=180). Put x = ∠BAP; as P sweeps the open side, x ranges over all of (0, α), each value once.
The two children are
  T₁ = {x, β, 180−β−x},   T₂ = {α−x, γ, β+x}   (using β = 180−α−γ).
The two cut-point angles ∠APB = 180−β−x and ∠APC = β+x are **supplementary** (sum 180). As x
ranges over (0,α), ∠APB ranges over the open interval (γ, 180−β) of length α.

### 1. Necessity: θ ∤ 180 ⟹ Shan-Yu survives forever
Work modulo θ. Call a triangle **good** if no angle is ≡ 0 (mod θ) (no angle a positive multiple
of θ); a good triangle has no angle equal to θ, so the game has not stopped.

**Lemma A (residue survival).** If a triangle is good and θ ∤ 180, then every cevian leaves at
least one good child.
*Proof.* With residues a≡α, b≡β, c≡γ (all ≠ 0), and t≡x: T₁ is bad ⟺ t ≡ 0 or t ≡ 180−b (since
b≠0); T₂ is bad ⟺ t ≡ a or t ≡ −b (since c≠0). Both bad requires {0, 180−b} ∩ {a, −b} ≠ ∅, i.e.
one of: 0≡a (⇒a≡0), 0≡−b (⇒b≡0), 180−b≡a (⇒ 180≡a+b ⇒ c≡0), 180−b≡−b (⇒ 180≡0 ⇒ θ∣180). All
four are excluded by goodness and θ∤180. So the two bad-residue sets are disjoint; no single x makes
both children bad. By symmetry this holds for every apex. ∎

A good initial triangle exists (e.g. isosceles (t,t,180−2t) with t avoiding the finitely many bad
values in (0,90)). Shan-Yu opens with it and always discards a bad child, keeping a good one (Lemma
A). By induction the position stays good forever; no angle ever equals θ, so Mulan never wins. This
covers every θ with 180/θ ∉ ℤ (both θ≤90 and θ>90). ∎

*(Independent confirmation for θ>90: from the equilateral start Shan-Yu maintains "all angles ≤ 90"
— of the two supplementary cut-point angles at most one exceeds 90, so he keeps the non-obtuse child;
θ>90 never appears.)*

### 2. Sufficiency: θ = 180/n (integer n ≥ 2) ⟹ Mulan wins
Now 180 = nθ, and the positive multiples of θ in (0,180) are exactly θ, 2θ, …, (n−1)θ. From any
live triangle (no angle = θ):

**Lemma B (alignment).** There is a legal cevian after which **both** children carry a positive
multiple of θ.
*Proof.* By supplementarity (§0), it suffices to make one cut-point angle a multiple kθ; then the
other is 180−kθ = (n−k)θ, also a multiple. Cut from a **largest**-angle apex A (α ≥ β,γ); ∠APB
fills the open interval (γ, 180−β) of length α (endpoints γ and −β both non-multiples).
- θ ≤ 60 (n ≥ 3): α ≥ 60 ≥ θ, and α = θ would force θ = 60 and an equilateral triangle (angle = θ,
  excluded); so α > θ, an open interval of length > θ contains a multiple of θ.
- θ = 90 (n = 2): the two non-largest angles β,γ are < 90 (at most one angle, the max α, exceeds 90),
  so 90 ∈ (γ, 180−β): the altitude from A makes both cut-point angles 90 = θ. ∎

After alignment, whichever child Shan-Yu keeps has an angle mθ, 1 ≤ m ≤ n−1. If m = 1 it equals θ
(win). Else:

**Lemma C (θ-peel).** A triangle with an angle mθ (2 ≤ m ≤ n−1, none yet = θ) is forced to an angle
θ in finitely many moves.
*Proof.* Take that vertex as apex and cut x = (m−1)θ ∈ (0, mθ). Then
  T₁ = {(m−1)θ, β, 180−β−(m−1)θ},   T₂ = {θ, γ, β+(m−1)θ}.
T₂ carries θ. If m = 2 then T₁ = {θ, β, 180−β−θ} also carries θ (double fork) — Mulan wins whatever
Shan-Yu keeps. If m ≥ 3, Shan-Yu must keep T₁ (keeping T₂ loses at once), whose apex angle is
(m−1)θ; the peel value drops by 1. After ≤ m−2 forced steps it reaches 2, then the double fork wins.
∎

So from any live triangle Mulan wins in at most n−1 moves. ∎

### 3. Conclusion
θ ∤ 180 ⟹ Shan-Yu survives (§1); θ = 180/n, n ≥ 2 ⟹ Mulan wins (§2). Hence Mulan can guarantee
victory in finitely many steps **iff θ = 180°/n for an integer n ≥ 2**. ∎
