# Lemma: Lexicographic termination monovariant for the gcd/lcm blackboard

## Statement

On a board of N positive integers, define
  W := Σ_i Ω(x_i)  (total prime factors counted with multiplicity; Ω(1) = 0),
  c := #{ i : x_i > 1 }.
Order the pair Φ = (W, c) lexicographically with W primary. Then
**every move strictly decreases Φ**, and ℕ² under lexicographic order is
well-founded, so the process terminates after finitely many moves.

The move on the chosen pair (m, n) with g = gcd(m, n) splits into three
exhaustive disjoint cases:
- (A) m ≠ n and g > 1: new entries (g, xy) with xy ≥ 2, so c unchanged,
  W drops by Ω(g) ≥ 1.
- (B) g = 1 (so m ≠ n, since m = n > 1 ⇒ g = m > 1): new entries
  (1, mn), c drops by 1, W drops by Ω(1) = 0.
- (C) m = n: new entries (m, 1), c drops by 1, W drops by Ω(m) ≥ 1.
No move leaves both coordinates fixed.

## Variant

A valuation-free variant replaces W by the plain integer product
P = ∏_i x_i (P_new = P_old / g; strictly drops when g ≥ 2, unchanged
when g = 1), with the same secondary coordinate c and the same case
split. ℕ² lex is well-founded (P is a positive integer that can strictly
drop only finitely many times; once stable, c — a nonneg integer —
strictly drops finitely many times).

## Proof

See `approaches/per-prime-euclidean-invariant.md`, Lemmas 5–7 (the
(W, c) version), and `approaches/integer-termination-invariant-pin.md`,
Lemmas 1–4 (the (P, c) version), and `approaches/confluence-unique-
normal-form.md`, Lemmas A1–A3. All sorry-free and from scratch.

## Reviewer certification

Certified APPROVED (round 1). Correct, no stronger than proved, sorry-free.
Promotable to any approach needing termination of the gcd/lcm blackboard.
