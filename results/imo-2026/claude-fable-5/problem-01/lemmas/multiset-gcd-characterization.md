# Lemma: multiset-gcd-characterization

**Status: certified (proof-reviewer, round 1)** — proved in full in `approaches/star-monoid-product-descent.md`, Step 2 (Lemmas 2 and 4 there). Statement checked against the proof — no overclaim; the strong induction (pair existence) and the |A|-induction (general existence, which also yields the recursion in part 5) verified step by step.

## Statement

Conventions: for d ∈ ℤ≥1 and a ∈ ℤ≥0, d | a means a = dc for an integer c (so every positive integer divides 0). D(a) := {d ∈ ℤ≥1 : d | a}, so D(0) = ℤ≥1 and, for a ≥ 1, D(a) is finite with largest element a. For a finite multiset A of non-negative integers, CD(A) := ⋂_{a∈A} D(a), with CD(∅) = ℤ≥1.

**Lemma.** For every finite multiset A of non-negative integers there is a **unique** g ∈ ℤ≥0 with CD(A) = D(g); write g = G(A). Moreover:
1. G(∅) = 0 and G({a}) = a.
2. G(A) = 0 iff every element of A is 0; in particular G(A) ≥ 1 as soon as A has a non-zero element.
3. G depends only on the multiset; if CD(A) = CD(B) then G(A) = G(B).
4. Pair conventions: G({a,0}) = a, G({0,0}) = 0, and for a, b ≥ 1, G({a,b}) = gcd(a,b) (ordinary greatest common divisor). One may write gcd(a,b) := G({a,b}) on ℤ≥0 — this is the convention gcd(k,0) = k, gcd(0,0) = 0.
5. (Splitting, Lemma 4 there) For any a, b ∈ ℤ≥0 and any finite multiset T: G({a,b} ⊎ T) = G({G({a,b})} ⊎ T). Hence the recursion G(A ⊎ {a}) = G({G(A), a}) holds, and the k-ary gcd is order-free/associative.

## Where proved

`results/imo-2026-01/approaches/star-monoid-product-descent.md`, Step 2 (Lemmas 2 and 4). Uniqueness via finiteness of D(g) for g ≥ 1; pair existence by strong induction on x + y with the subtractive Euclid step D(x) ∩ D(y) = D(x−y) ∩ D(y); general existence by induction on |A|; all zero/empty cases covered.

## Reuse notes

Gives, order-free, the multiset gcd needed for the invariant ∏_p p^{gcd of p-exponents} in both invariant approaches (star-monoid-product-descent and prime-gcd-invariant), including the 0-exponent conventions and generalized associativity, without any hand-waved "generalized gcd" step.
