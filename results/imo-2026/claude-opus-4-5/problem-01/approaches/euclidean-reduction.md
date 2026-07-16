# Approach: euclidean-reduction

## Target
Prove both parts: (a) the process terminates with exactly one M > 1; (b) M does not depend on choices.

## Technique
Prime-by-prime Euclidean algorithm. View the problem as running a parallel Euclidean algorithm on the valuation vector at each prime. This approach emphasizes the structural insight that the operation IS the Euclidean algorithm on exponents, making both termination and uniqueness follow from properties of the Euclidean algorithm.

## Skeleton

### The core structural insight

**Step 0.** Reframe the problem in terms of prime factorizations.
Write each a_i = product over primes p of p^{e_{i,p}}.
The board state is equivalent to the collection of valuation vectors (e_{1,p}, e_{2,p}, ..., e_{2026,p}) for each prime p.

**Step 1.** Analyze the operation on valuation vectors.
For a move on (m, n), the outputs are (gcd(m,n), lcm(m,n)/gcd(m,n)).
At prime p with v_p(m) = a, v_p(n) = b:
- v_p(gcd(m,n)) = min(a, b)
- v_p(lcm(m,n)/gcd(m,n)) = max(a,b) + min(a,b) - 2*min(a,b) = max(a,b) - min(a,b) = |a - b|

So the operation on p-coordinates is: (a, b) -> (min(a, b), |a - b|).

**Step 2.** Recognize this as the Euclidean subtraction step.
The map (a, b) -> (min(a,b), |a-b|) is exactly one step of the subtractive Euclidean algorithm.
Key property: gcd(a, b) = gcd(min(a,b), |a-b|).

### Part (a): Termination

**Step 3.** Termination at each prime.
For a fixed prime p, let (e_1, ..., e_n) be the current multiset of v_p values.
Each move applies the Euclidean step to two coordinates.
The sum e_1 + ... + e_n changes by: min(a,b) + |a-b| - a - b.
If a <= b: this is a + (b-a) - a - b = -2a + 2a - 2a = ... wait, let me recalculate.
Actually: min(a,b) + |a-b| = a + (b-a) = b when a <= b. So sum goes from a + b to a + (b - a) = b. Change is b - (a+b) = -a.
So the sum of v_p values decreases by min(v_p(m), v_p(n)) = v_p(gcd(m,n)) per move.

Let Sigma_p = sum of v_p(a_i) over all entries.
This is a nonnegative integer decreasing by v_p(gcd(m,n)) >= 0 each move.

**Step 4.** Global termination via total Omega.
S = sum over all primes p of Sigma_p = sum over all entries of Omega(a_i).
Each move decreases S by Omega(gcd(m,n)) >= 0.
When S stays constant (gcd = 1), the number of entries > 1 decreases.
Lexicographic (S, k) monovariant gives termination.

### Part (b): Uniqueness

**Step 5.** The gcd of the v_p multiset is invariant.
By the Euclidean identity, G_p = gcd(e_1, ..., e_n) is unchanged when we replace (a, b) by (min(a,b), |a-b|).
This is because the Euclidean algorithm computes gcd by repeated subtraction, and each step preserves the gcd.

**Step 6.** At termination, the board is {M, 1, ..., 1}.
For each prime p: the v_p multiset is (v_p(M), 0, 0, ..., 0).
G_p = gcd(v_p(M), 0, ..., 0) = v_p(M).

**Step 7.** M is determined.
v_p(M) = G_p = gcd(v_p(a_1), ..., v_p(a_{2026})) for all primes p.
Hence M = product of p^{G_p}.

### Connection to the Euclidean algorithm

**Step 8.** Analogy with aimo-0440.
In aimo-0440, a multiset of reals with a linear dependency a_1*r_1 + ... + a_n*r_n = 0 undergoes subtractions r_i <- r_i - r_j; the L1 norm |a_1| + ... + |a_n| is a monovariant, and the game terminates when some coefficient hits 0.

Our problem is similar: the v_p multiset undergoes Euclidean steps (a, b) -> (min(a,b), |a-b|). The sum of the multiset is the monovariant (it decreases by min(a,b)). The game terminates when all but one entry is 0, at which point the remaining entry equals the gcd.

**Step 9.** Single-prime special case.
If all a_i = p^{e_i} for a single prime p, then:
- The v_p multiset is (e_1, ..., e_{2026}).
- Each move applies (a, b) -> (min(a,b), |a-b|).
- Terminal state: (gcd(e_1, ..., e_{2026}), 0, 0, ..., 0).
- M = p^{gcd(e_1, ..., e_{2026})}.

This is the Euclidean algorithm on 2026 numbers.

## Key lemmas (claim + mechanism)

1. **Operation on valuations**: (a, b) -> (min(a,b), |a-b|) -- by direct calculation from gcd and lcm formulas.

2. **Euclidean step preserves gcd**: gcd(min(a,b), |a-b|) = gcd(a, b) -- the fundamental property of the subtractive Euclidean algorithm.

3. **Sum of valuations decreases**: Sigma_p decreases by min(a,b) each move -- because min(a,b) + |a-b| = max(a,b) < a + b when a, b > 0 with a != b, and = a when a = b.

4. **Terminal state has exactly one nonzero v_p entry**: After enough Euclidean steps on a multiset, all entries but one become 0, and the remaining entry is the gcd.

## Open gaps

- Gap 1: Prove that Euclidean steps on a multiset eventually reduce all but one entry to 0.
- Gap 2: Rigorously verify min(a,b) + |a-b| = max(a,b) in all cases.
- Gap 3: Connect the prime-by-prime analysis to the global termination (which depends on S = total Omega).

## Cases to cover

- Single-prime case: all a_i are powers of the same prime.
- Multi-prime case: entries have various prime factors.
- Coprime case: all initial entries are pairwise coprime.

## Watch out for

- The single-prime analysis shows termination at each prime separately, but global termination requires the total Omega or lexicographic argument because we can't terminate at all primes simultaneously until exactly one entry > 1 remains.
- The Euclidean connection is conceptual: we're not literally running the standard Euclidean algorithm, but a multi-number version of the subtraction step.
