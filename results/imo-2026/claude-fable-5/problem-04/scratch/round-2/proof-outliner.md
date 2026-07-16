# Proof-outliner field — round 2

## imo-2026-04

Conjectured answer (all three explorers agree, verified computationally with exact rational arithmetic): **Mulan wins iff θ = 180°/n for some integer n ≥ 2.** Both approaches below target the full characterization — sufficiency (explicit Mulan strategy) AND necessity (Shan-Yu survival strategy) — end to end. Population was empty; both are new.

---

remainder-forcing: new
Target: Mulan guarantees victory in finitely many steps iff θ = 180°/n, n ∈ ℤ, n ≥ 2; if 180/θ ∈ ℤ she wins in ≤ n − 1 cuts, otherwise Shan-Yu survives forever.
Technique: arithmetic in ℝ/θℤ on the angle multiset ("safe" = no angle is a positive multiple of θ). One algebraic engine drives both directions: the two angles created at P are supplementary, so making both pieces unsafe forces 180 ≡ 0 (mod θ) — possible exactly when θ | 180.
Skeleton:
  1. Cut formula: cut to vertex A with t = ∠BAP ∈ (0, a) gives pieces (b, t, a+c−t) and (c, a−t, b+t) — by elementary angle sums + monotone-rotation realizability (GAP G0).
  2. Descent Lemma: an angle mθ (m ≥ 1) on the board loses for Shan-Yu in ≤ m − 1 cuts — by strong induction on m, cutting to the mθ vertex with t = θ (GAP G1).
  3. Forcing Lemma (crux of sufficiency): from a safe triangle, t = θ − r_b (residues r ∈ (0, θ)) makes b+t ≡ 0 AND a+c−t ≡ 0 (mod θ), because r_a + r_b + r_c ≡ 180 ≡ 0 when θ | 180 — both pieces get a positive multiple. Validity of t via largest-angle vertex; n = 2 sub-cases separately (GAP G2).
  4. Assemble Direction A: has-θ / has-multiple / safe trichotomy, ≤ n − 1 cuts total (GAP G3).
  5. Safe start exists for Direction B: isoceles family dodges the finite set of multiples (GAP G4).
  6. Safety Preservation Lemma (crux of necessity): both pieces unsafe forces one of four congruences; three contradict safety of T (a ≡ 0, b ≡ 0, c ≡ 0), the fourth gives 180 ≡ 0 (mod θ), impossible when 180/θ ∉ ℤ (GAP G5).
  7. Assemble Direction B + answer statement + substitution checks (GAPs G6–G7-level, routine).
Key lemmas (claim + mechanism):
  - Forcing Lemma — because the residues of the three angles sum to 180 mod θ = 0, one congruence class of t zeroes both P-angle slots simultaneously.
  - Safety Preservation — because the two P-angle slots (a+c−t) and (b+t) sum to 180°, so both being multiples forces (j+k)θ = 180°.
  - Descent Lemma — because t = θ splits mθ into θ (instant win if kept) and (m−1)θ.
Open gaps: G2 (forcing-cut validity, incl. θ = 90° acute/obtuse sub-cases) and G5 (exhaustive 4-case safety) are the hard ones; G0, G1, G3, G4, G6 routine.
Cases to cover: Direction A trichotomy; n ≥ 3 vs n = 2 inside G2; four cases (i)–(iv) inside G5.
Watch out for: "multiple" = positive integer multiple (angles > 0 make residue-0 ⇒ genuine multiple); t strictly interior (P not a vertex); companion-vertex asymmetry (B sits in T₁ — relabeling freedom is part of G2); θ > 90° needs no special case (falls under Direction B).
File: results/imo-2026-04/approaches/remainder-forcing.md
Recommendation: OPEN and put in the build set — this is the leanest complete route; the crux algebra is verified (I re-checked the forcing step with exact rationals for n = 2, 3, 5, 7, 12, 300 random triangles each — 100% success).

---

descending-chain: new
Target: same full characterization (θ = 180°/n, n ≥ 2), Mulan bound ≤ 2n − 2 cuts.
Technique: explicit geometric three-phase strategy with monovariants for sufficiency (no residue bookkeeping): Phase 0 "grind" (all angles > θ: shrink the smallest angle by θ per cut), Phase 1 "ignition" (smallest angle x < θ: cut to the largest vertex with s = θ − x, planting 180° − θ = (n−1)θ in the piece Shan-Yu must keep), Phase D "descent" (kθ → (k−1)θ, ending at k = 2 where both pieces get θ). Necessity via the closed family F = {no angle a positive multiple of θ} — the minimal Shan-Yu-closed family (closure under the cut algebra generates exactly the multiples semigroup).
Skeleton:
  1. Cut formula + realizability (GAP H0).
  2. Trichotomy: (I) has kθ, k ≥ 2 / (II) safe with smallest < θ / (III) safe with all angles > θ — exhaustive since x = θ ends the game and no multiple is < θ (GAP H1).
  3. Phase D handles (I) — monovariant: largest multiple present drops by θ (GAP H2).
  4. Phase 1 handles (II) — mechanism: with companion = smallest angle x and s = θ − x, the kept piece is (x, θ−x, 180°−θ) INDEPENDENT of the other two angles; validity z > θ − x via z ≥ 60° ≥ θ for n ≥ 3, middle-angle < 90° for n = 2 (GAP H3).
  5. Phase 0 handles (III) — monovariant: smallest angle drops by exactly θ per cut; ≤ n − 2 grinds reach (I)/(II) (GAP H4); note (III) nonempty only for n ≥ 4.
  6. Assembly of A: ≤ 2n − 2 cuts (GAP H5).
  7–8. Direction B: nonempty closed family F + Closure Lemma (four-case, same certified-lemma candidate as remainder-forcing G5 — prove once in lemmas/, import) + assembly (GAPs H6–H8).
Key lemmas (claim + mechanism):
  - Ignition — because the kept piece's third angle is 180° − x − (θ−x) = 180° − θ = (n−1)θ regardless of the triangle's other angles.
  - Grind monovariant — because cutting the smallest angle x with s = x − θ plants θ in the discardable piece and leaves smallest angle x − θ in the other.
  - Closure Lemma — same supplementary-pair mechanism as above.
Open gaps: H3 (ignition validity incl. n = 2), H4 (grind boundary case x − θ = θ), H7 (four-case closure — shared lemma) hard; H0–H2, H5, H6, H8 routine.
Cases to cover: trichotomy (I)/(II)/(III); n ≥ 3 vs n = 2; x − θ >/=/< θ; four unsafe-unsafe combinations.
Watch out for: label/companion bookkeeping in the cut formula (the ignition NEEDS companion = smallest angle); w + θ < 180° check in Phase 0's kept piece; do not switch to binary halving (recorded dead end for write-up complexity).
File: results/imo-2026-04/approaches/descending-chain.md
Recommendation: OPEN as the rival. Its sufficiency engine is genuinely different (extremal-vertex geometric phases + monovariants vs one-shot residue forcing); if remainder-forcing's G2 validity argument snags, this route's phase structure sidesteps it.

---

## Why no third approach

The only genuinely different third route on the table was the analogy explorer's doubling-orbit necessity invariant S = {2^k θ} ∩ (0°, 180°). **It is broken — do not open it.** Counterexample (verified numerically this round): θ = 40° (180/40 ∉ ℤ), T = (120°, 25°, 35°) has no angle in S = {40°, 80°, 160°}, yet cutting to the 120° vertex with t = 40° gives pieces (25°, 40°, 115°) and (35°, 80°, 65°) — BOTH contain an element of S. The invariant family must be closed under the sums/differences the cut algebra generates, and that closure of {θ} is exactly all positive multiples of θ — which is what both opened approaches use. Record this as a dead end under any future analogy-driven revival. The binary-halving descent is a variant of descending-chain's Phase D, not a rival (and is a recorded presentation dead end).

## Shared-lemma note for the reviewer/builders

The four-case safety/closure lemma (remainder-forcing G5 = descending-chain H7) is identical mathematics. Whichever builder proves it first should file it as `results/imo-2026-04/lemmas/safe-piece-exists.md` for certification; the other imports it. This is deliberate lemma-cache reuse, not proof-splitting — each slug still proves the whole claim, and the lemma's surface area is four lines of verified congruence algebra, so shared-line risk is minimal.

## Honest risk list (for the outline-reviewer's ranking)

- Both approaches' necessity direction rests on the same 4-case lemma; I re-derived it independently and it is tight, but it is the single shared line.
- remainder-forcing's real difficulty concentrates in G2 (which vertex admits the forcing t; the n = 2 obtuse case) — small but must be airtight.
- descending-chain has more moving parts (three phases, two monovariants, more boundary cases H3/H4) but each part is elementary; its risk is a missed boundary case, not a wrong idea.
- Realizability of the cut parameter (G0/H0) is easy but MUST appear explicitly — the problem's move is "choose P", not "choose t".

build set suggestion: remainder-forcing, descending-chain
