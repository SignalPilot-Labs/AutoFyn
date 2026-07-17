# Proof Reviewer Memory

## Learned Rules

ALWAYS: Verify key claims computationally before approving a proof, especially claims about structure (like "H becomes K_k^2"). (Round 1: two-of-k-structure claimed K_k^2 but a1=35 gives H={{5,7},{2,5},{2,3,7},{3,5}} which is NOT K_k^2)

ALWAYS: Check that the constraint characterization captures ALL constraints, not just a subset. (Round 1: backbone-periodicity only used backbone primes but gcd(m, a_i)>1 can be satisfied by primes outside the backbone)

ALWAYS: Test the claimed period L with at least 3 different starting values to catch errors. (Round 1: backbone-periodicity claimed L=15 for a1=15 but correct L=30)

NEVER: Accept "Let me prove this directly" followed by no actual proof as completed. (Round 1: two-of-k-structure claimed K_k^2 but never proved it)

ALWAYS: When a proof claims L = product(some set S), verify computationally that this S is the correct set. (Round 1: backbone L = product(B) but correct L = product(union(H)) where H involves primes outside B)

ALWAYS: Re-derive the load-bearing step (Dichotomy Lemma: infinite antichain + backbone constraint => common prime) independently before approving. (Round 2: two-of-k-structure proved this correctly)

ALWAYS: Check if a proof self-describes as partial but actually contains a complete argument. (Round 2: saturation-route claimed gap but dichotomy route within it was complete)
