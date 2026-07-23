## imo-2026-06

antichain-stabilization: new
Target: Prove there exist T, L > 0 with a_{n+T} = a_n + L for all n >= 1.
Technique: Track irredundant constraint antichain H of minimal prime-sets; show H stabilizes to self-blocking state; once stable, valid set is L-periodic where L = lcm(union H).
Skeleton:
  1. Define H_n = antichain of minimal prime-sets among {P(a_1),...,P(a_n)} — by definition
  2. H_n is intersecting (any two elements share a prime) — by gcd(a_i,a_j) > 1
  3. Claim H stabilizes: bounded intersecting antichains over finite prime support — by Erdos-Ko-Rado bound
  4. Once H self-blocking, future constraints subsumed — by transversal containment
  5. Valid set V = {m : P(m) hits every Q in H} is L-periodic — by CRT, L = lcm(support)
  6. Greedy on L-periodic set gives shift-periodicity — by pigeonhole on residues
Key lemmas (claim + mechanism):
  - H stabilizes in finite steps — because prime support bounded by primes(a_1...a_K) and intersecting antichains on k primes have size O(2^k)
  - Self-blocking implies constraint domination — because every transversal of H contains an element of H, so new constraints are redundant
Open gaps: (A) prime support bounded; (B) self-blocking achieved; (C) minimal transversal structure
Cases to cover: prime power a_1 (trivial: all multiples of p)
Watch out for: new primes entering support indefinitely; antichain growing without bound

backbone-periodicity: new
Target: Prove there exist T, L > 0 with a_{n+T} = a_n + L for all n >= 1.
Technique: Reduce to "backbone types" T_i = primes(a_i) intersect B where B = primes(a_1). Show startup types are minimal transversals; future types contain a startup type; hence constraints stabilize over B.
Skeleton:
  1. Every a_n divisible by some prime in B = primes(a_1) — by gcd(a_n, a_1) > 1
  2. Define backbone type T_m = B intersection primes(m) — by definition
  3. Startup types T_1,...,T_K are minimal transversals of the hypergraph {T_1,...,T_K} — KEY CLAIM
  4. For n > K, T_n contains some T_i (i <= K) — by minimality of startup types
  5. Constraint from a_n subsumed by constraint from a_i — by T_i subset T_n
  6. Valid set V_K is L-periodic, L = lcm(B) — by CRT on primes in B
  7. Greedy cycles through T valid residues with shift L — by ordering
Key lemmas (claim + mechanism):
  - Startup types are minimal transversals — because greedy picks smallest valid integer, so no redundant backbone prime in T_i (removing it would give smaller valid number)
  - L = product of primes in B — because B = primes(a_1) is fixed and finite, L = lcm(B) = product (distinct primes)
Open gaps: (1) minimal transversal characterization; (2) K bounded; (3) extra primes don't affect backbone constraints
Cases to cover: a_1 prime power (B = {p}, all multiples of p)
Watch out for: extra primes outside B creating non-redundant constraints

clique-valid-set: new
Target: Prove there exist T, L > 0 with a_{n+T} = a_n + L for all n >= 1.
Technique: Show valid set V_n becomes a "clique" (any two elements share a prime). Once V_N is a clique, it stabilizes (new constraints auto-satisfied). Clique on finite prime base is L-periodic.
Skeleton:
  1. V_n decreasing: V_{n+1} subset V_n — by adding constraint
  2. Sequence is a clique: gcd(a_i, a_j) > 1 for all i < j — by definition
  3. Coprime pairs in V_n resolve when smaller element visited — by exclusion of larger
  4. Eventually V_N is a clique — by resolution of all coprime pairs in finite time (GAP)
  5. V_N stable: V_m = V_N for m > N — by clique property (new constraint auto-satisfied)
  6. V_N is L-periodic for L = lcm(prime base) — by CRT
  7. Greedy on periodic clique gives shift-periodicity — by cyclic traversal
Key lemmas (claim + mechanism):
  - Coprime pairs resolve in finite time — because greedy visits elements in increasing order, each coprime pair (x,y) with x < y is resolved when a_m = x excludes y
  - Clique valid set is periodic — because any element of the clique shares a prime with every constraint; this is a residue condition mod L
Open gaps: (A) all coprime pairs resolve in finite time; (B) finite prime base; (C) clique periodicity
Cases to cover: none beyond main argument
Watch out for: infinitely many coprime pairs in V_0 — need finite stabilization argument

two-of-k-structure: new
Target: Prove there exist T, L > 0 with a_{n+T} = a_n + L for all n >= 1.
Technique: Prove constraint antichain H = K_k^2 (all 2-element subsets of finite prime set S). Valid set = "divisible by >= 2 primes from S," which is explicitly periodic mod L = product(S).
Skeleton:
  1. Numerical evidence: H = K_k^2 for S = {small primes} in all cases — verified computationally
  2. H is intersecting antichain — by gcd condition
  3. H closes to all pairs: if {p,q}, {p,r} in H, eventually {q,r} in H — by greedy producing term divisible by q,r but not p (GAP)
  4. S finite, determined by early terms — by bounded growth of prime support
  5. Valid set = {m : m divisible by >= 2 primes from S} — by definition of K_k^2 constraint
  6. T = count of valid residues mod L, computable by inclusion-exclusion — by explicit formula
  7. Greedy yields a_{n+T} = a_n + L — by cyclic traversal
Key lemmas (claim + mechanism):
  - H = K_k^2 — because greedy eventually hits every pair of primes from S (forces missing pairs into H by producing coprime-to-p terms)
  - k=1 case: a_1 = p^j gives H = {{p}}, sequence = multiples of p
Open gaps: (1) H exactly K_k^2; (2) S finite and stabilizes; (3) k=1 degenerate case
Cases to cover: a_1 prime power (k=1); a_1 product of >= 2 distinct primes (k >= 2)
Watch out for: H being proper subset of K_k^2; S growing indefinitely
