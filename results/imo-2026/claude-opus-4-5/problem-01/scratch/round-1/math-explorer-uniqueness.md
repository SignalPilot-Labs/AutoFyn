## imo-2026-01

- Distinct openings:

  1. **Prime-by-prime p-adic invariant (main route).** The move (m,n) → (gcd(m,n), lcm(m,n)/gcd(m,n)) acts on each prime p's valuation independently: (v_p(m), v_p(n)) → (min(v_p(m), v_p(n)), |v_p(m) - v_p(n)|). This is exactly one step of the subtractive Euclidean algorithm. For each prime p, the multiset gcd I_p = gcd(v_p(x_1), ..., v_p(x_{2026})) is invariant (because gcd(min(a,b), |a-b|) = gcd(a, b) — the fundamental Euclidean property). In the terminal state M,1,...,1, we have v_p(M) = gcd(v_p(M), 0,...,0) = v_p(M) = I_p. So M = Π_p p^{I_p} is uniquely determined by the initial board. This directly gives part (b) and confirms the formula M = Π_p p^{gcd_i v_p(x_i)}.

  2. **Monovariant for termination and "exactly one" (part a).** Define T = Σ_i Ω(x_i) (total prime factors with multiplicity across all board numbers). Under the move, T decreases by Ω(gcd(m,n)) ≥ 0. When gcd(m,n) = 1, T is unchanged but N (count of elements > 1) strictly decreases by 1 (since one output is 1). When gcd(m,n) > 1, T strictly decreases by ≥ 1. So the lexicographic pair (T, N) strictly decreases at each step and has a lower bound, giving termination. To see exactly one M > 1 survives: the terminal N cannot be ≥ 2 (we'd still make a move); it cannot be 0 (for any prime p dividing some initial x_i, I_p = gcd(v_p values) ≥ 1 > 0 = gcd(0,...,0) since gcd(0, a) = a > 0, forcing v_p(M) = I_p ≥ 1, so M ≥ 2, contradicting all numbers being 1). Hence N = 1 at termination.

  3. **Subtractive Euclidean algorithm interpretation.** Think of the process as running the subtractive Euclidean algorithm simultaneously on all pairs of numbers and across all primes. The process terminates because sum of valuations is bounded (standard GCD algorithm terminates). The terminal state for each prime p's multiset has all zeros except one value equal to I_p = gcd of the initial multiset. This is a clean termination argument without needing the full lexicographic monovariant: since T is a non-negative integer and decreases whenever gcd > 1 (strictly), and gcd = 1 moves are bounded in number (each decreases N), the whole process terminates in at most T_init · N_init steps.

  4. **Alternative: product / log monovariant.** The product Π x_i changes as: new product = gcd(m,n) · lcm(m,n)/gcd(m,n) · (rest) = lcm(m,n) · (rest) ≤ mn · (rest) = old product. Product is non-increasing; strictly decreasing when gcd > 1. When gcd = 1, product unchanged but N decreases. This gives an alternative monovariant formulation using log(product).

- Candidate technique(s): **p-adic valuation analysis** (prime-by-prime decomposition), **Euclidean algorithm / gcd invariant**, **monovariant** for termination. The core technique is that gcd(min(a,b), |a-b|) = gcd(a, b), which makes the per-prime gcd of the multiset an invariant. This is labeled "Invariants & monovariants" in knowledge_base.md.

- Cheap-kill candidates: The p-adic gcd invariant is itself a structural kill that immediately identifies what M must be: M = Π_p p^{gcd(v_p(x_1),...,v_p(x_{2026}))}. No heavy computation needed. Verified computationally across multiple random boards and paths with 3-5 elements.

- Knowledge-base entries to use:
  - **"Invariants & monovariants"** (combinatorics section): exact fit — a quantity preserved or strictly monotone across moves.
  - **"p-adic valuation"** (number theory section): the v_p representation is the backbone of the uniqueness argument.
  - **"Divisibility and gcd"** (number theory section): gcd(min(a,b), |a-b|) = gcd(a,b) is a standard Euclidean identity.
  - **"Direct proof"** / **"Induction"** (general methods): the per-prime argument is a direct computation with a clean invariant.

- Analogous past problems (cruxes):
  - **aimo-0477** (number_theory, `divisibility-and-gcd`): tracks gcd(a_1, a_n) = d_n as a non-decreasing chain of divisors of a_1. Crux: "v_p(d_n) = min(v_p(a_1), v_p(a_n)) is nondecreasing for every p." Analogy: our problem also uses per-prime gcd of a multiset as an invariant, and stabilization = reaching the terminal state. Similar in flavor but our problem requires gcd of the WHOLE multiset (not just a pair) and a full invariance argument.
  - **aimo-0324** (number_theory, `invariants-and-monovariants`): squarefree part of a board number as monovariant in a two-player game. Crux: "S(n^k) = S(n) for odd k, = 1 for even k." Analogy: using a multiplicative function of board numbers as an invariant. Weaker match than the direct p-adic approach.
  - No closer match found in the corpus — this problem's specific structure (gcd(min,|diff|) = gcd identity applied to valuations of a whole multiset) does not appear directly.

- Prior progress: none (first round, no existing approaches).

- Dead ends (do not retry): none yet.

- Small-case / intuition notes (all labeled as verified conjecture from computation):
  - **Verified formula:** M = Π_p p^{gcd(v_p(x_1),...,v_p(x_{2026}))} is confirmed correct for all tested boards [4,6], [4,6,10], [12,18], [8,4], [4,6,10,15], [36,13,100], [35,72,31,26], [10,22,99,77,7] across multiple randomly chosen move orderings.
  - **The key identity:** gcd(min(a,b), |a-b|) = gcd(a,b) verified for all a,b in {0,...,7}.
  - **Per-prime independence:** the move decouples across primes — the valuation tuple for each prime evolves independently of other primes.
  - **Termination monovariant:** Σ_i Ω(x_i) is non-increasing and N is non-increasing; the pair (T,N) is a strict lex monovariant (conjecture from analysis, not separately numerically tested, but follows immediately from Ω(gcd) ≥ 0 and gcd=1 forces N to drop).
  - **Note on gcd(0,...,0) = 0 vs gcd(0,...,k,...,0) = k:** critical distinction. If only one x_i has a prime factor p (others not divisible by p), the gcd of p-valuations is still k > 0 (since gcd(0,...,0,k,0,...,0) = k). This ensures M > 1 whenever any initial number > 1 exists.
