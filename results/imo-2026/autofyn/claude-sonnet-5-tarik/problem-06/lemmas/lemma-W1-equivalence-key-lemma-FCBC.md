# Lemma W1 (Equivalence Lemma: window Key Lemma ⟺ FCBC)

Notation: `P_m := rad(a_m)`. For `K≥1`, `H_K := ⋃_{m=1}^K P_m`. A finite set
of primes `H` is a *covering set* if `H∩P_i∩P_j≠∅` for every `i<j`. FCBC
asserts a covering set exists; the "Key Lemma" of the window-construction
approach asserts some `H_K` is a covering set.

**Statement.** FCBC holds if and only if the Key Lemma holds:

`∃ finite H, H∩P_i∩P_j≠∅ ∀i<j` `⟺` `∃K≥1, H_K∩P_i∩P_j≠∅ ∀i<j`.

**Proof.**

`(⇐)` `H_K` is itself a finite set of primes, so take `H:=H_K`.

`(⇒)` Suppose `H` is a finite covering set. Let `Π := ⋃_{i≥1}P_i` (all primes
ever dividing some term). `H' := H∩Π` is finite.

*Step 1.* `H'` is itself a covering set: for `i<j`, pick `p∈H∩P_i∩P_j`
(exists since `H` covers); then `p∈P_i⊆Π`, so `p∈H∩Π=H'`, giving
`p∈H'∩P_i∩P_j`.

*Step 2.* `H'` is nonempty: apply Step 1 to `(1,2)`.

*Step 3.* For each `p∈H'`, since `p∈Π`, `μ(p):=min{m≥1:p∣a_m}` is
well-defined (nonempty set of positive integers, well-ordering). Since `H'`
is finite and nonempty, `K:=max_{p∈H'}μ(p)` is a well-defined finite
positive integer.

*Step 4.* `H'⊆H_K`: for `p∈H'`, `μ(p)≤K` and `p∈P_{μ(p)}⊆H_K`.

*Step 5.* For `i<j`, by Step 1 `H'∩P_i∩P_j≠∅`; since `H'⊆H_K` (Step 4),
`H_K∩P_i∩P_j⊇H'∩P_i∩P_j≠∅`. So `H_K` is a covering set, witnessing the Key
Lemma with this explicit `K`. `∎`

**Discussion.** The window construction `H_K` loses no generality: it is
literally equivalent to FCBC, not a restricted special case. Byproduct: an
explicit recipe `K=max_{p∈H∩Π}μ(p)` converting *any* covering set `H`
(however produced) into an explicit window index.

**Source.** `results/imo-2026-06/approaches/explicit-window-backbone-construction.md`
(round 3).

**Certification.** Independently re-derived and checked step by step
(elementary, no numerical dependency, no circularity — `μ(p)` is
well-defined by well-ordering of `ℕ`, `H'` finite since `H` finite). No
gaps. Certified `solved`-quality (sorry-free), unconditional. Formally
unifies the three "Gap-1" approaches (`persistent-backbone-monovariant`,
`forced-primes-well-ordering`, `explicit-window-backbone-construction`) as
attacking the identical proposition.
