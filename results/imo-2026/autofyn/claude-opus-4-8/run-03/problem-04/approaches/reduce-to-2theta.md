# Approach: reduce-to-2theta

## Status
partial

## Claim (answer)
Same answer as lattice-invariant-180 — Mulan wins iff θ | 180 — but reached by a
DIFFERENT framing: collapse the whole game to a single reachability question ("can
Mulan force an angle exactly 2θ?"), then resolve THAT by a residue/potential argument.
This is a rival route: if the covering step of the invariant approach has a hidden
error, this framing's potential-function bookkeeping is an independent check.

## Spine
1. **One-move-win exhaustion (Lemma 0).** For θ ≠ 90, the only cut making BOTH children
   carry θ is bisecting a vertex of angle exactly 2θ. (Same 6-sub-case exhaustion as the
   sibling approach.) Consequence: for θ ≠ 90, *Mulan's game = the game "force an angle
   equal to 2θ, then bisect."* The θ=90 case is separate (altitude, one move).
2. **Residue potential.** Track Φ(T) = "does the angle-multiset of T meet the lattice
   θℤ?" (boolean). Mulan wins ⟺ she can force Φ from false to true AND then walk the
   lattice down to 2θ. Two facts:
   (a) **Descent on the lattice.** If Φ(T)=true with a lattice angle mθ (2 ≤ mθ < 180),
       the forced θ-plant sends mθ → (m−1)θ deterministically; iterate to 2θ, bisect,
       win. So Φ=true (with a multiple ≥ 2θ) ⟹ Mulan wins.
   (b) **Flipping Φ.** Starting from Φ=false (all angles ∉ θℤ), a single cut of vertex a
       makes BOTH children meet θℤ iff θ | 180 (the 4-case covering computation, mod θ:
       both-bad forces a≡0, b≡0, c≡0, or 180≡0; the first three are excluded by Φ=false,
       leaving θ|180). If θ∤180 Shan-Yu always keeps a Φ=false child, so Φ stays false
       forever and 2θ (∈θℤ) is never reached ⟹ Mulan loses. If θ|180 Mulan flips Φ in
       one move (x ≡ −b mod θ) then descends by (a) ⟹ Mulan wins.

## Key lemmas (claim + mechanism)
- **Lemma 0 (reduction):** for θ≠90 the sole double-θ cut is a=2θ — because the two
  cut-point angles are supplementary (sum 180), so both equalling θ forces θ=90, and the
  only other pairing forces a−x=x=θ i.e. a=2θ. Mechanism: exhaust {x,b,180−x−b} vs
  {a−x,c,x+b} slot-equalities.
- **Descent lemma:** forced θ-plant at angle mθ keeps ((m−1)θ, c, b+θ) — mechanism: the
  discarded child (θ,b,180−θ−b) contains θ so Shan-Yu must avoid it; a−θ=(m−1)θ stays a
  θ-multiple. Monovariant m ↓ terminates at 2θ.
- **Flip lemma:** both children meet θℤ ⟺ θ|180 (given parent has no lattice angle) —
  mechanism: the same 4-case mod-θ covering; 180≡0 is the unique escape and needs θ|180.

## Open gaps
- H1: full slot-pairing proof of Lemma 0 (6 sub-cases; b=θ/c=θ already-won excluded).
- H2: prove the flip move's x ≡ −b (mod θ) lies in (0,a) and yields non-degenerate
  children (share G2 with sibling; can import once certified).
- H3: bound the descent length (≤ 180/θ forced moves) and confirm the 2θ→bisect finish.
- H4: the Φ=false ⟹ stays-false induction (necessity) — identical covering as sibling;
  keep as a shared lemma `lemmas/lattice-covering.md` once proved.

## Cases to cover
θ=90 (altitude); θ|180, θ<90 (flip+descend+bisect); θ∤180 (Φ invariant, includes θ>90).

## Watch out for
- This approach's novelty is FRAMING the win as a boolean potential Φ + a monovariant m,
  making the finiteness of Mulan's strategy explicit (≤ 180/θ + O(1) moves) — state that
  bound, since the rigor rules demand a finite explicit strategy, not mere existence.
- Do not conflate "a child CONTAINS θ" (not a win — discarded) with "both children
  contain θ" (a win). Lemma 0 is exactly about the latter.
</content>
