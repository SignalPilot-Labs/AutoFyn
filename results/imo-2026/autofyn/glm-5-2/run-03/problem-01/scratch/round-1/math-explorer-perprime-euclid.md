## imo-2026-01 (lens: per-prime exponent / Euclidean dynamics)

### The core reduction
Write each number as its prime-exponent vector. For a fixed prime p, if the two chosen numbers carry p-exponents (a,b), the move replaces them with
- gcd(m,n): p-exponent = min(a,b)
- lcm(m,n)/gcd(m,n): p-exponent = max(a,b) − min(a,b) = |a−b|

So per-prime the move is exactly **(a,b) → (min(a,b), |a−b|)** — one subtraction-step of the Euclidean algorithm on the pair of exponents. This is THE central identification; everything below flows from it.

### Distinct openings this framing gives

1. **Per-prime gcd-of-multiset invariant (gives (b) directly).** For each prime p let g_p = gcd of the multiset {e_{p,1}, …, e_{p,2026}} (with exponent 0 for the number 1; gcd(0,a)=a). The Euclidean step preserves gcd-of-multiset because gcd(min(a,b), |a−b|) = gcd(a,b), so G_new = gcd(G_rest, gcd(a,b)) = G_old. Hence g_p is invariant. In the terminal state (one number M, 2025 ones) the multiset for p is {e_p(M), 0,…,0}, whose gcd is e_p(M). Therefore **M = ∏_p p^{g_p}**, determined solely by the initial board — independent of Confucius's choices. This is a complete proof of part (b). Confirmed by simulation (5/5 random trials, n=8, range 2–100).

2. **Lexicographic monovariant (Ω, K) (gives (a)).** Let Ω = Σ_i Ω(n_i) (total prime-factor count with multiplicity) and K = number of entries > 1. Per move:
   - coprime pair (gcd=1): (m,n)→(1, mn). Ω unchanged, K drops by 1.
   - non-coprime, m≠n: (m,n)→(d, ab) with d>1, ab>1. Ω drops by Ω(d) ≥ 1, K unchanged.
   - m=n: (m,m)→(m,1). Both Ω and K drop.
   So (Ω, K) strictly decreases lexicographically and is bounded below → termination. At termination K<2; and K≥1 throughout because the invariant forces some g_p ≥ 1 (any prime dividing n_1 has g_p ≥ 1), so Ω_total ≥ Ω(M) ≥ 1. Hence exactly one M>1 remains. This proves (a) without even needing (b).

3. **"Per-prime terminal shape" sanity check on M>1.** g_p ≥ 1 iff at least one of the 2026 numbers is divisible by p (since gcd with a zero entry equals the nonzero entry). Since every n_i > 1, the product ∏ p^{g_p} over primes dividing some n_i is automatically > 1, so the invariant already rules out the "all become 1" degenerate end-state. No separate argument needed.

### The coupling subtlety (resolved)
Moves pick a pair of whole numbers, so the Euclidean step fires on all primes simultaneously — you cannot run each prime's Euclidean algorithm independently to (g_p, 0). **This threatens neither part:**
- For (b): the invariant g_p is preserved per-prime *independently* of coupling — the per-prime move on (a,b) preserves gcd-of-multiset regardless of what happens at other primes. Coupling is irrelevant to the invariant.
- For (a): termination is handled globally by (Ω, K), not by per-prime Euclidean termination, so the inability to drive each prime to (g,0) independently does not matter.

Coupling would only threaten a *constructive* argument ("exhibit moves reaching M"); that route is not needed here. Flag for the outliner: do NOT try to prove (a) by "run the Euclidean algorithm per prime to completion" — that's exactly the path coupling blocks. Use the global monovariant instead.

### Cheap-kill candidates
- The identity gcd(min(a,b), |a−b|) = gcd(a,b) — single-line, kills (b).
- Ω(m)+Ω(n) − [Ω(gcd)+Ω(lcm/gcd)] = 2·Ω(gcd) ≥ 0, with equality iff gcd=1 — single-line monovariant for (a).
- lcm/gcd = mn/gcd²; when m≠n and gcd>1 this is >1 (write m=da, n=db, gcd(a,b)=1, ab≥2) — needed to confirm non-coprime moves keep K constant.

### Knowledge-base entries to use
- "Invariants & monovariants" (knowledge_base.md line 117) — the per-prime g_p invariant.
- "Invariant / monovariant" under General Proof Methods (line 191) — termination via monotone (Ω, K).
- p-adic valuation / exponent-tracking framing (line ~58 region, divisor analysis) — writing numbers as exponent vectors.
- Infinite descent is induction's dual (line 184) — flavor for the lex-decrease termination.

### Analogous past problems (cruxes)
- **aimo-0678** (number_theory, divisibility-and-gcd): a *coupled gcd/lcm recurrence* a_{n+1}=gcd(a_n,b_n)+1, b_{n+1}=lcm(a_n,b_n)−1; crux = "form the sum s_n=a_n+b_n as a candidate invariant" + a min-of-non-divisor monovariant w_n. Directly analogous in two ways: same gcd/lcm coupling, and the invariant+monovariant double-attack structure this problem needs. Adapt (don't cite): the invariant there is a sum; here it is a per-prime gcd.
- **aimo-0324** (number_theory, invariants-and-monovariants): "assign each board position the squarefree part S(n) = product of primes with odd exponent and use it as a one-sided monovariant." Same genre — a move-process on numbers whose termination/uniqueness is settled by a per-prime-exponent invariant. Adapt: squarefree part is too coarse here (we need the full exponent-gcd, not parity).
- No crux in the corpus matches a blackboard gcd/lcm *replacement* process exactly; the two above are the closest by structure (coupled gcd/lcm dynamics; per-prime-exponent monovariant on a move-game). Do not force a tighter match.

### Prior progress
None (round 1, no approaches yet).

### Dead ends (do not retry)
- (Anticipated) Trying to prove (a) by running a per-prime Euclidean algorithm to completion — blocked by prime coupling. Use global (Ω, K) instead.

### Small-case / intuition notes (CONJECTURE, verified numerically not proved here)
- Simulated 5 random boards of size 8, values in [2,100]: every run terminated with exactly one number M>1, and M equal to ∏_p p^{gcd of initial p-exponents} in all cases. Strong evidence the invariant is correct and complete. (A proof, not a computation, is still required for the reviewer.)
- The terminal M is the gcd of the multiset of numbers viewed prime-wise: equivalently M = gcd of all products? No — note M ≠ gcd(n_1,…,n_2026) in general (e.g. {2,3} gives M=6, while gcd=1). The per-prime gcd of *exponents*, not gcd of the numbers, is the right object. Flag for outliner: do not confuse g_p (gcd of exponents) with v_p(gcd of numbers) = min of exponents — the invariant is gcd-of-exponents, the min is the *upper* term not preserved.

### Hard steps a proof on this route must settle
1. Prove the per-prime move identity (a,b) → (min, |a−b|) and the gcd-preservation gcd(min,|a−b|)=gcd(a,b) — trivial but must be stated.
2. Prove the terminal-state identification e_p(M) = g_p rigorously, handling the 1's as exponent-0 entries (gcd(e,0,…,0)=e).
3. Prove Ω(m)+Ω(n) ≥ Ω(gcd)+Ω(lcm/gcd) with the equality case characterized (gcd=1), and the K-preserving lemma for non-coprime m≠n (lcm/gcd>1).
4. Establish the lex-decrease of (Ω, K) and the lower bound Ω_total ≥ 1 via the invariant (so terminal K=1, not 0).
5. State M explicitly as ∏_p p^{g_p} for the reviewer's "verify the invariant" check.
