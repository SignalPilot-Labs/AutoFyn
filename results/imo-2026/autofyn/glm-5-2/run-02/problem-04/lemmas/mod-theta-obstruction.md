# Lemma: mod-θ four-case obstruction (Shan-Yu's defense)

## Statement

Let θ ∈ (0°, 180°) with 180°/θ ∉ ℤ, and let r := 180° mod θ ∈ (0, θ). Define the invariant **(I)** on a triangle T = (X, Y, Z): *"no angle of T is a θ-multiple"* (equivalently X, Y, Z ≢ 0 mod θ).

**(I) is preserved under every Mulan move.** That is: if T satisfies (I), then for any choice of split vertex and any γ ∈ (0, X), at least one of the two children also satisfies (I). Consequently Shan-Yu can keep a child satisfying (I) forever, preventing any angle from ever equaling θ.

## Proof

Relabel so Mulan splits angle X with γ adjacent to Y. By the **angle-triple transform** (see below), the children are:
- child 1 = (γ, Y, 180° − Y − γ);
- child 2 = (X − γ, Z, Y + γ).

Assume (I): X ≢ 0, Y ≢ 0, Z ≢ 0 (mod θ). Suppose for contradiction that **both** children contain a θ-multiple. In child 1 the slot Y is nonzero mod θ by (I), so the θ-multiple is in slot γ or slot (180° − Y − γ). In child 2 the slot Z is nonzero by (I), so the θ-multiple is in slot (X − γ) or slot (Y + γ). The 2 × 2 = 4 disjoint, exhaustive combinations (all congruences mod θ):

1. γ ≡ 0 ∧ (X − γ) ≡ 0 ⇒ X ≡ γ + (X − γ) ≡ 0, contradicting X ≢ 0.
2. γ ≡ 0 ∧ (Y + γ) ≡ 0 ⇒ Y ≡ (Y + γ) − γ ≡ 0, contradicting Y ≢ 0.
3. (180° − Y − γ) ≡ 0 ∧ (X − γ) ≡ 0 ⇒ (Y + γ) ≡ 180° ≡ r and γ ≡ X, so Y + X ≡ r; but X + Y + Z ≡ 180° ≡ r, hence Z ≡ 0, contradicting Z ≢ 0.
4. (180° − Y − γ) ≡ 0 ∧ (Y + γ) ≡ 0 ⇒ (Y + γ) ≡ r and (Y + γ) ≡ 0, so r ≡ 0, contradicting r ∈ (0, θ).

All four fail; hence no γ makes both children carry a θ-multiple. At least one child satisfies (I); Shan-Yu keeps it. ∎

## Auxiliary lemma used

**Angle-triple transform.** Triangle (X, Y, Z), X + Y + Z = 180°. Splitting angle X with γ ∈ (0, X) adjacent to Y gives child 1 = (γ, Y, 180° − Y − γ) and child 2 = (X − γ, Z, Y + γ); the two P-angles (180° − Y − γ) and (Y + γ) sum to 180° (supplementary pair). *Proof:* direct angle chase — child 1's P-angle = 180° − γ − Y; child 2's P-angle = 180° − (X − γ) − Z = Y + γ (using X + Y + Z = 180°).

## Where proved
`results/imo-2026-04/approaches/mod-theta-descent.md`, §II.3 (and §0 for the transform).

## Status
**Certified** by proof-reviewer, round 1. Statement is correct (no stronger than proved: it claims preservation of (I) under arbitrary Mulan moves, which is exactly what §II.3 of `mod-theta-descent.md` proves). Independently re-derived and numerically verified: zero escapes across 13 θ values (rational {72,100,50,7,13,40,135,36.5,60.0001,17.5,170}° and irrational {180/π, 50√2}°), 5000 γ-steps each. The four cases are exhaustive by the distributive law (disjunction of 4 conjunctions covers "both children contain a θ-multiple"); cases need not be disjoint. Importable by any approach needing Shan-Yu's defense.
