# Clique Valid Set Stabilization

## Target
Prove there exist positive integers T, L such that a_{n+T} = a_n + L for every positive integer n.

## Technique
Show the valid set V_n = {x > a_n : gcd(x, a_i) > 1 for all i <= n} eventually becomes a "clique" (any two elements share a prime), after which it stabilizes. A periodic clique on a finite prime base gives shift-periodic greedy traversal.

## Outline

1. **V_n is decreasing.** V_{n+1} subset V_n (adding constraints only shrinks the valid set).

2. **The sequence forms a clique.** By construction, gcd(a_i, a_j) > 1 for all pairs i < j (since a_j must share a prime with every a_i, i < j). So {a_1, a_2, ...} is a pairwise non-coprime sequence (a "gcd-clique").

3. **Claim: V_n eventually becomes a clique.** Define V_n as a clique if for all x, y in V_n with x != y, gcd(x, y) > 1. We show this holds for n >= N_0 for some finite N_0.

4. **Mechanism for clique formation.** Suppose x, y in V_n with gcd(x, y) = 1 and x < y. When the greedy reaches x (i.e., a_m = x for some m > n), we require gcd(y, x) > 1 for y to remain valid. But gcd(x, y) = 1, so y is excluded at step m. Every coprime pair (x, y) in V_n is "resolved" when the smaller element is visited: the larger is excluded. Since V_n is a countable set ordered by <, coprime pairs are eventually resolved.

5. **Once V_N is a clique, V_m = V_N for all m > N.** If V_N is a clique and a_{m} in V_N (for m > N), then for any x in V_N, gcd(x, a_m) > 1 (since V_N is a clique). So the constraint from a_m is automatically satisfied by all elements of V_N, meaning V_{m} = V_N.

6. **Clique on finite prime base is L-periodic.** Let S = {primes p : p | x for some x in V_N that's below some bound}. Since V_N is eventually the valid set and is a clique, any x in V_N shares a prime with every other element. This forces V_N to be periodic mod L = lcm(S) for some finite S.

7. **Count residues and conclude.** T = number of valid residues in V_N mod L. The greedy cycles through them with period T and shift L.

## Gaps

- **Gap A (All coprime pairs resolve in finite time):** The critical gap. Must show that the coprime pairs in V_0 are ALL resolved (the smaller element visited) in finite time. The issue: V_0 is infinite, so there are infinitely many coprime pairs. But the greedy visits elements in increasing order, so at each step the "unresolved" coprime pairs have their smaller element > a_n (current term). As a_n -> infinity, fewer coprime pairs remain unresolved below any fixed bound. Need to show this stabilizes.

- **Gap B (Finite prime base S):** Must prove S is finite. Candidate argument: S subset of primes dividing a_1 * a_2 * ... * a_K for some finite K (the constraint-determining terms).

- **Gap C (Periodicity of a clique valid set):** Once V_N is a clique, show it's L-periodic for L = product of the relevant primes. This follows from CRT if the clique condition translates to "divisible by at least one prime from each constraint set."

## Status
unsolved
