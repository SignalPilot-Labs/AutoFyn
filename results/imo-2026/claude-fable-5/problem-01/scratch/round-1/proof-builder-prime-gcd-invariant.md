# Build report — imo-2026-01, round 1, slug: prime-gcd-invariant

## Claim
Status: **solved** (builder's claim, pending proof-reviewer verification).

Full proof of both parts written to `results/imo-2026-01/approaches/prime-gcd-invariant.md` under `## Full proof`.

## What was built
All six skeleton gaps closed, in dependency order (outline-reviewer note 1 honored: Lemma 2, "lcm/gcd = 1 ⇔ m = n", is proved BEFORE it is used in Lemma 3 Case C / Lemma 5 Case C):

- **Setup:** valuation facts (V1)–(V4) from unique factorization; Ω defined; multiset-gcd defined via the common-divisor characterization (★) with existence (least positive linear combination + division algorithm) and uniqueness (two-case argument) proved; (G1) zeros inert, (G2) fold rule proved from (★). gcd-with-0 conventions stated once up front (note 2 honored).
- **Lemma 1:** v_p(gcd) = min, v_p(lcm) = max, gcd | lcm, v_p(lcm/gcd) = |a−b| — each direction from (V2). Explicit remark that moves are global and per-prime statements are identities under one global move.
- **Lemma 2:** lcm/gcd = 1 ⇔ m = n via (V3)/(V4).
- **Lemma 3:** a move never outputs two 1s; cases A (m = n), B (gcd = 1, forces m ≠ n; outputs (1, mn), mn ≥ 4), C (gcd > 1, m ≠ n; both outputs > 1) shown disjoint and exhaustive.
- **Lemma 4:** ΔT = −Ω(gcd(m,n)), from min + |a−b| = max per prime, finite sum justified.
- **Lemma 5 + termination:** W = N + T drops by ≥ 1 on every move (case A: ≥ 2; B: exactly 1; C: ≥ 1); well-ordering ⇒ ≤ W(B₀) moves.
- **Step 4 (exactly one):** legality ⇔ N ≥ 2; N never hits 0 (Lemma 3 walk, N_after ≥ N_before − 1 ≥ 1); stopping ⇔ N ≤ 1; hence terminal N = 1. Both directions of "exactly one" present.
- **Lemmas 6–7:** subtractive Euclid identity gcd(a,b) = gcd(min, |a−b|) with zero cases spelled out; invariance of g_p via fold–Euclid–fold chain.
- **Step 6:** terminal exponent multiset is (v_p(M), 0, …, 0) so g_p(B*) = v_p(M) by (G1); invariant gives v_p(M) = g_p(B₀); finiteness of relevant primes justified (note 3 honored); M = ∏_p p^{g_p(B₀)} by unique factorization — independent of choices. Non-circularity of (a)/(b) stated; formula independently reconfirms M > 1.

## Numerical verification (illustrative, not load-bearing)
300 random boards (2–8 entries, values 2–200) with random full plays: W strictly decreased at every move, all g_p invariant at every intermediate board, every play terminated with exactly one entry > 1 equal to ∏ p^{g_p}. The worked example in the proof ((12,18,10) → … → (1,1,30)) was machine-checked move by move.

## Promotable lemmas (proposed, uncertified)
- `results/imo-2026-01/lemmas/move-anatomy.md` — valuation formulas, lcm/gcd = 1 ⇔ m = n, no-two-1s case analysis.
- `results/imo-2026-01/lemmas/multiset-gcd-invariance.md` — multiset gcd via (★), fold rule, subtractive Euclid identity with zero cases, invariance of g_p.
Both are proved in full inside the approach file; the sibling star-monoid-product-descent could import either.

## Remaining gaps
None known to the builder.

## Spec concerns:
(none)
