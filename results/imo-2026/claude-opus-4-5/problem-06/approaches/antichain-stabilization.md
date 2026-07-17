# Antichain Stabilization

## Target
Prove there exist positive integers T, L such that a_{n+T} = a_n + L for every positive integer n.

## Technique
Track the "irredundant constraint antichain" H of minimal prime-sets. Show H stabilizes to a self-blocking intersecting antichain in finite time. Once stable, the valid set is periodic mod L = lcm(primes in H), giving shift-periodicity.

## Outline

1. **Define the constraint antichain.** For each term a_i, let P(a_i) = set of prime divisors of a_i. Define H_n = antichain of minimal sets among {P(a_1), ..., P(a_n)} (i.e., those not containing another as a proper subset). H_n encodes the "irredundant" gcd constraints.

2. **H_n is intersecting.** Any two elements of H_n share a prime (since gcd(a_i, a_j) > 1 for all i < j forces P(a_i) intersection P(a_j) non-empty). This is immediate from the problem's gcd condition.

3. **Define self-blocking (saturation) condition.** H is self-blocking if every transversal of H contains some element of H. Equivalently, b(H) (the blocker/dual hypergraph) equals H itself.

4. **Claim: H_n eventually becomes self-blocking.** When H_n is not self-blocking, there exists a set S that is a transversal of H_n but contains no element of H_n. The greedy sequence can then produce a term a_{n+1} with P(a_{n+1}) = S (or a superset), adding S as a new antichain element. Each addition increases |H| or adds new primes to the support. Since H is always intersecting, and intersecting antichains over a finite prime set are bounded (by Erdos-Ko-Rado type bounds), and the prime support is eventually bounded (KEY GAP), H must stabilize.

5. **Once H is self-blocking, constraints stabilize.** For any future term a_m (m > N), P(a_m) is a transversal of H_N (else gcd(a_m, a_j) = 1 for some j with P(a_j) in H_N). By self-blocking, P(a_m) contains some Q in H_N. But then the constraint from a_m is dominated by the constraint from the term corresponding to Q: any x sharing a prime with Q also shares a prime with a_m. So C_m = C_N for all m >= N.

6. **Periodic valid set.** Let S = union of all primes in H_N, and L = lcm(S) (= product since all primes are distinct). The constraint C_N = {x : x shares a prime with every Q in H_N} is a union of residue classes mod L, hence periodic mod L.

7. **Greedy on periodic set gives shift-periodicity.** Let T = number of valid residue classes in [0, L). Starting from any term a_n in the valid set, the greedy picks residues in increasing cyclic order, wrapping every T steps with a shift of L. Hence a_{n+T} = a_n + L for all n >= 1.

8. **Period holds from n=1.** Since a_1 is in the valid set (gcd(a_1, a_j) > 1 for all j > 1 by construction symmetry), the periodicity applies from the start.

## Gaps

- **Gap A (Prime support bounded):** Must prove that the set S = union of primes in H stabilizes in finite steps. The argument relies on showing no new prime enters S after some N_0. Candidate route: every prime in S must appear in some a_i with i <= N_0 (bounded since the greedy is deterministic and the first K terms have bounded values).

- **Gap B (Self-blocking achieved):** Must prove H eventually becomes self-blocking. Candidate argument: each step that adds to H strictly increases some finite measure (|H| bounded by antichain theory, or total prime count bounded). 

- **Gap C (Every transversal contains an antichain element):** This is the formal statement of self-blocking. Need to verify the mechanism: if P(a_{n+1}) is a transversal not containing any H-element, it becomes a new minimal element of the antichain. The greedy ensures P(a_{n+1}) is minimal among valid choices — but why minimal in the antichain sense?

## Status
unsolved
