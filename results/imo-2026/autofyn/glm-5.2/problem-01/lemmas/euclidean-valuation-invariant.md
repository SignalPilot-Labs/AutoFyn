# Lemma: Euclidean valuation invariant (D_p invariant)

## Statement

Let a board hold N positive integers x_1, …, x_N. A **move** picks two
entries m, n > 1 (in distinct positions) and replaces them by
gcd(m, n) and lcm(m, n)/gcd(m, n). For each prime p, define

  D_p := gcd( v_p(x_1), v_p(x_2), …, v_p(x_N) ),

with the conventions gcd(x, 0) = x and gcd(0, …, 0) = 0 (so positions
where p does not divide the entry are invisible, and an all-zero list
has gcd 0). Then **D_p is invariant under every move**.

Engine: under the move, the p-valuation pair (α, β) = (v_p(m), v_p(n))
is sent to (min(α, β), |α − β|) (since v_p(gcd) = min(α, β) and
v_p(lcm/gcd) = max(α, β) − min(α, β) = |α − β|), and the Euclidean
identity gcd(min(α, β), |α − β|) = gcd(α, β) holds for all nonneg
α, β (subtractive Euclidean step: assume α ≥ β, then
gcd(β, α − β) = gcd(β, α) = gcd(α, β)).

## Proof

See `approaches/per-prime-euclidean-invariant.md`, Lemmas 1–4 (also
proved independently in `approaches/integer-termination-invariant-pin.md`,
Lemmas 8–10, and used in `approaches/confluence-unique-normal-form.md`,
fact (F3) + Lemma P). The proof is sorry-free and from scratch: the
move on valuations, the Euclidean identity (case split α ≥ β), and
list-gcd preservation by associativity of gcd.

## Reviewer certification

Certified APPROVED (round 1). Statement is correct and no stronger than
what is proved; sorry-free; proved from scratch. Promotable to any
approach needing the part-(b) pin or the per-prime invariant.
