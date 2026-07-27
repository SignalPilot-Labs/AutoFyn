## imo-2026-01

Route: per-prime valuation / vector-Euclidean framing (whole problem, both parts).

### Distinct openings (within this route)
1. **Global lex potential (W, c).** W = ∑ over positions Ω(value) = ∑_p ∑_positions v_p(value) (nonneg integer). c = #{positions with value>1}. Show a move strictly decreases (W,c) in lex order: when gcd(m,n)>1 (and m≠n), W drops by Ω(gcd(m,n))≥1, c unchanged; when gcd=1, W unchanged, c drops by 1; when m=n, both drop. ℕ² lex is well-founded ⟹ finite termination. Handles the prime-coupling automatically because W is additive over primes. **Cleanest opening.**
2. **Global lex potential (P, c) with P = ∏ values.** Product of the two new numbers equals lcm(m,n) = mn/gcd(m,n), so P_new = P_old / gcd(m,n): strictly decreases (integer division by gcd≥2) when gcd>1, unchanged when gcd=1. So (P,c) lex also terminates. Simpler to state than W, but disconnected from the per-prime invariant story (P is multiplicative, doesn't pin v_p(M) directly). Good as a rival termination argument, but part (b) still needs the g_p invariant.
3. **Per-prime Euclidean-termination + merge.** For each prime p alone, the chosen pair's valuations go (a,b)→(min(a,b),|a−b|), a Euclidean step; per-prime the valuation multiset "converges." BUT the chosen position pair is global and shared across all primes, so you cannot terminate each prime independently — the coupling is a genuine obstacle. This opening is fragile; flag it as the weak alternative. The global W (opening 1) sidesteps the coupling by summing over primes.

### Candidate technique(s)
- Invariant + monovariant (two-pronged): invariant g_p pins the answer (part b); lex monovariant (W,c) gives termination (part a). The Euclidean identity gcd(min(a,b),|a−b|)=gcd(a,b) is the engine of the invariant.
- p-adic valuation bookkeeping: decompose every number by prime factorization and track valuations positionwise.

### Cheap-kill candidates
- The invariant g_p = gcd of all positionwise p-valuations (with gcd(a,0)=a) is preserved by the move because the move replaces (a,b) by (min(a,b),|a−b|) and gcd(min(a,b),|a−b|)=gcd(a,b). This single identity nearly settles part (b) once termination is known. Cheap.
- "c never reaches 0": since some number >1 initially, some prime p has g_p≥1; this is invariant; if c hit 0 then all valuations 0 so all g_p=0, contradiction. Hence terminal c=1 (process halts iff c≤1). Cheap.

### Knowledge-base entries to use
- "Invariants & monovariants" (Combinatorics section) and "Invariant / monovariant" (General Proof Methods) — the lex monovariant for termination.
- "Divisor analysis / gcd structure, consecutive-integer coprimality (gcd(k,k+1)=1)" and the divisibility-and-gcd tools (v_p(gcd)=min, v_p(lcm)=max) — standard p-adic facts underpinning L1/L2.
- (Vieta/descent not needed.)

### Analogous past problems (cruxes)
- aimo-0236 (combinatorics, invariants-and-monovariants): "Reduce a two-player termination question to a single p-adic threshold; when the added constant's valuation strictly exceeds each token's, the addition preserves every valuation, so the total-valuation sum is a strict monovariant under the halving move." Same flavor — p-adic valuation sum as a termination monovariant in a replacement game. Genuinely analogous in spirit (p-adic monovariant ⟹ termination), though the game mechanics differ.
- aimo-0324 (number_theory, invariants-and-monovariants): "Assign each board position the squarefree part of its number and use it as a one-sided monovariant." Weaker analogue — squarefree-part-as-monovariant for a game; the gcd/lcm replacement here uses full p-adic valuations, not just squarefree part.
No crux in the corpus matches the gcd/lcm-replacement move directly; the matches are thematic (p-adic monovariant for termination), not mechanical.

### Prior progress
None (round 1; current.md unsolved, no approaches).

### Dead ends (do not retry)
None yet.

### Sub-lemmas the outliner would need to prove
- L1: v_p(gcd(m,n))=min(v_p(m),v_p(n)), v_p(lcm)=max, so v_p(lcm/gcd)=|v_p(m)−v_p(n)|. (Standard; cite divisibility-and-gcd.)
- L2: The move sends valuation pair (a,b)→(min(a,b),|a−b|); gcd(min(a,b),|a−b|)=gcd(a,b) ⟹ the per-prime gcd-of-all-valuations is preserved.
- L3: g_p := gcd of all positionwise p-valuations (gcd(a,0)=a) is an invariant of the whole process.
- L4: W:=∑Ω(value)=∑_p∑_pos v_p; ΔW = −Ω(gcd(m,n)) when gcd>1, ΔW=0 when gcd=1. (Additivity over primes + L1.)
- L5: c:=#{value>1}; case analysis: gcd>1 & m≠n ⟹ Δc=0; gcd=1 (so m≠n) ⟹ Δc=−1; m=n ⟹ Δc=−1. (The m=n edge makes lcm/gcd=1 — must be explicit.)
- L6: (W,c) strictly decreases in lex order every move; ℕ² lex well-founded ⟹ termination.
- L7: g_p≥1 for some p (invariant, L3) ⟹ c≥1 always (else all valuations 0); terminal c≤1 ⟹ c=1.
- L8 (part b): terminal board = one M>1 + 1's; v_p(M)=gcd(v_p(M),0,…,0)=g_p (invariant) ⟹ M=∏_p p^{g_p}, determined by initial data ⟹ independent of choices.
- (P-route alt: L4': P_new=P_old/gcd(m,n); (P,c) lex terminates.)

### Hard steps / likely gaps / weak points (honest)
- The (W,c) lex argument is airtight as far as I can see; the only "weakness" is that it is standard/clean (problem is rated difficulty 5/medium). No real gap found. Verified by simulation on [6,10,15]→30, [4,8,16]→2, [2×8]→2, [6,6,6]→6, [2,3,5,7,11,13]→30030, [12,18,24,30]→30 — all M = ∏ p^{g_p}, all g_p preserved to terminal.
- **Coupling subtlety (opening 3):** the per-prime Euclidean processes are coupled (same position pair drives all primes simultaneously). You cannot prove termination prime-by-prime and merge; the global additive W is what makes it work. Do not let an approach rely on "each prime's Euclidean algorithm terminates independently" — that step is unjustified under coupling.
- **Edge case m=n:** produces (m,1), i.e., lcm/gcd=1. Must be handled in the c-change case analysis (it makes c drop even though gcd>1). Easy but easy to miss.
- **Edge case all numbers share one prime** (e.g. all powers of 2): every move has gcd>1, W strictly decreases each move; eventually M = p^{g_p}. Works; no special handling needed beyond the general argument, but worth a sanity line.
- **well-foundedness rigor:** ℕ² lex has no infinite strictly decreasing chain — standard, but the outliner should justify (first component drops finitely often by ≥1 and is ≥0; between drops the second is bounded below by 0 and strictly decreases). Don't hand-wave "obviously terminates."
- The "exactly one >1" needs both halves: termination gives c≤1; invariant g_p≥1 gives c≥1; together c=1. Either half alone is partial.

### Small-case / intuition notes (conjecture, verified only computationally)
- M = ∏_p p^{g_p} where g_p = gcd of initial positionwise p-valuations. Conjecture confirmed on 6 small examples (above). This is the explicit closed form for the invariant answer; not a proof but strong evidence the route is correct end-to-end.
- Intuition: the move "extracts" the common prime-power part of a pair into the gcd slot and pushes the "difference" into the lcm/gcd slot; iterating peels all shared structure into a single survivor while the leftover coprime multiplications collapse to 1's. The survivor's p-valuation is exactly the gcd of the original p-valuations (the part common to ALL positions, in the gcd sense).
