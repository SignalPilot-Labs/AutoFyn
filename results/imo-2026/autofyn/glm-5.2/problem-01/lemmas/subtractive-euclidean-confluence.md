# Lemma: Subtract-Euclidean multiset confluence (Lemma P)

## Statement

Consider the rewrite system on finite MULTISETS of non-negative
integers where a move picks two POSITIVE entries u, v and replaces them
by (min(u, v), |u − v|). This system is confluent, with the **unique
normal form {d, 0, …, 0}** where d = gcd of all entries of the starting
multiset (with gcd(x, 0) = x).

## Proof sketch (full proof in source)

- Termination: the weight W = Σ (sum of all entries) strictly drops by
  min(u, v) ≥ 1 at every move (since min(u,v) + |u − v| = max(u, v)
  = u + v − min(u, v)). W is a nonneg integer, so the system terminates.
- Invariant: the gcd of all entries is preserved by the Euclidean
  identity gcd(min(u, v), |u − v|) = gcd(u, v).
- Unique normal form: a normal form admits no move, so at most one
  entry is positive; if one entry x is positive and the rest 0, the gcd
  is x, so x = d; if all 0, d = 0. Uniquely {d, 0, …, 0}.
- Confluence: a terminating system in which every element has a unique
  normal form is confluent (extend any divergence to normal forms; both
  equal the unique normal form of the source).

## Source

`approaches/confluence-unique-normal-form.md`, Lemma P. Proved from
scratch; sorry-free. Used to lift the board's overlapping critical pair
to local confluence (Lemma C) via per-prime projection.

## Reviewer certification

Certified APPROVED (round 1). Correct, no stronger than proved,
sorry-free. Promotable to any approach using Newman's lemma / per-prime
confluence on this kind of subtractive system.
