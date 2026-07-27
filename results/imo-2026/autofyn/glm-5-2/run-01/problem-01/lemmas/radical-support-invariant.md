# Lemma: Radical-support invariance (valuation-free "P > 1 forever")

## Statement

On a board of N positive integers with total product
P = ∏_i x_i, the **set of prime divisors of P** (the radical support) is
invariant under every move (m, n) ↦ (gcd(m, n), lcm(m, n)/gcd(m, n)).

Consequence (when all initial entries are > 1): the radical support is
nonempty initially, hence nonempty forever, so P > 1 forever; therefore
the board never becomes all 1's, i.e. c = #{x_i > 1} ≥ 1 at all times.
This supplies the lower bound c ≥ 1 needed for the "exactly one > 1"
clause of termination.

## Proof

A move on (m, n) = (g x, g y) with g = gcd(m, n), gcd(x, y) = 1,
replaces the pair (whose product is m·n = g²·x·y) by (g, x·y) (whose
product is g·x·y = lcm(m, n)). A prime divides g²·x·y iff it divides g
or x·y (squaring g does not change its prime support), iff it divides
g·x·y. So the pair's prime support is unchanged; the other entries are
untouched, so the prime support of P is unchanged. See
`approaches/integer-termination-invariant-pin.md`, Lemma 5, and
`approaches/confluence-unique-normal-form.md`, Lemma A4.

## Reviewer certification

Certified APPROVED (round 1). Correct, sorry-free, proved from scratch.
Promotable to any approach needing a valuation-free lower bound on c.
