## imo-2026-01

### Headline finding: the "sorting network / min,max" framing in the dispatch is WRONG — but the corrected framing (Euclidean-subtraction on exponents) gives an essentially complete proof, verified against 1000 random simulations.

**The valuation transform is NOT (min,max).** For a move on positions i,j with values m,n, and a fixed prime p, let x=v_p(m), y=v_p(n). Then:
- v_p(gcd(m,n)) = min(x,y)  — correct, this part is a sort.
- v_p(lcm(m,n)/gcd(m,n)) = v_p(lcm) − v_p(gcd) = max(x,y) − min(x,y) = **|x−y|**, NOT max(x,y).

So the pair (x,y) is replaced by **(min(x,y), |x−y|)** — this is exactly one step of the *subtractive* Euclidean algorithm applied to the exponent pair, not a compare-and-swap into sorted order. I verified this numerically is essential: simulating the actual process and comparing to the naive guess "M = ∏ p^{max_i v_p(a_i)}" (what the min/max sorting-network lens predicts) FAILS on multiple test boards (e.g. board {12,18,20}: naive guess gives 180, actual simulated result is always 30; board {8,27,25,6}: naive guess 5400, actual is 150). So the 0-1 principle / sorting-network machinery does **not** directly apply, and any approach built on "each prime's valuation vector gets sorted" is a dead end — do not pursue it.

### The corrected invariant (verified, essentially proves both (a) and (b))

**Key lemma (per-prime gcd invariance).** For any prime p, define g_p = gcd(v_p(a_1),...,v_p(a_2026)) over the *initial* board (standard convention gcd(0,x)=x). Claim: g_p is invariant under every move. Proof: only two coordinates x,y change per move, to (min(x,y),|x−y|). The one-line number-theory fact gcd(x,y) = gcd(min(x,y), |x−y|) (the Euclidean subtraction identity) plus associativity of gcd — gcd(G', x, y) = gcd(G', gcd(x,y)) where G' is the gcd of all other (unchanged) coordinates — shows the overall gcd across all 2026 positions is unchanged. This is a completely elementary, rigorous one-paragraph proof, no case-heavy machinery needed.

**Monovariant for termination.** Let Ω(board) = Σ_i Ω(a_i) (total prime factors with multiplicity, summed over the whole board) and C(board) = #{i : a_i > 1}. For a move on m,n with g=gcd(m,n), r=lcm(m,n)/gcd(m,n): the identity v_p(g)+v_p(r) = min(x_p,y_p)+|x_p−y_p| = max(x_p,y_p) for every p gives Ω(g)+Ω(r) = Σ_p max(x_p,y_p) ≤ Σ_p(x_p+y_p) = Ω(m)+Ω(n), with equality iff gcd(m,n)=1 (no shared prime). Casework on m,n:
- gcd(m,n)=1: new pair (1, mn); Ω unchanged, C strictly decreases by 1 (one slot becomes 1).
- m=n (so gcd=m=n>1): new pair (m,1); Ω strictly decreases (Ω(m)+Ω(1) < 2Ω(m)), C decreases by 1.
- m≠n, gcd=d>1: new pair (d,r), and one can show r=m'n' where m=dm',n=dn',gcd(m',n')=1,m'≠n' — this is always >1, so C is unchanged, but Ω strictly decreases (strict inequality above since some prime has min(x_p,y_p)>0).

So the lexicographic pair (Ω, C) — both nonnegative integers — strictly decreases at every move (Ω decreases in cases 2,3; in case 1, Ω is flat but C strictly decreases). This is a well-founded descent, hence the process **terminates** in finitely many moves. This gives finiteness cleanly without needing to touch the sorting-network 0-1 principle at all.

**Why the survivor count is exactly 1, not 0.** Pick any prime p₀ dividing a₁ (exists since a₁>1). Then g_{p₀} > 0 by definition (it's the gcd of a multiset containing at least one strictly positive value, namely v_{p₀}(a₁)). By the invariance lemma, at every point in the process — in particular at termination — the gcd of the current board's v_{p₀} values equals g_{p₀} > 0. This forces at least one current board entry to have v_{p₀} > 0, i.e. at least one entry is still > 1, at all times. Combined with termination (which by definition happens only when < 2 entries are >1, since a move requires two entries >1), this pins the terminal state at **exactly 1** entry >1. This is part (a), fully.

**Part (b) falls out immediately.** At termination all entries are 1 except position k with value M. For every prime p, g_p (invariant, computed from the initial board) equals gcd of the *terminal* board's v_p values = gcd(0,...,0,v_p(M),...,0) = v_p(M). So v_p(M) = g_p for every p — a formula depending only on the initial board, not on Confucius's choices. Hence **M = ∏_p p^{gcd_i(v_p(a_i))}**, independent of play. This *is* part (b), given part (a).

### Verified numerically (1000/1000 random trials, multiple move orders each)
`M = ∏_p p^{gcd(v_p(a_1),...,v_p(a_n))}` matches the simulated terminal value exactly, across boards of size 2–8 with random composite entries and randomized move orders (Python script using `math.gcd` + `sympy.factorint`, see below). Contrast with the false conjecture `M = ∏_p p^{max_i v_p(a_i)}` which fails on several boards (e.g. {12,18,20} → predicted 180, actual 30; {8,27,25,6} → predicted 5400, actual 150). This is strong (but non-proof) confirmation that the invariant above is the right one, matching the elementary proof sketch above which I consider essentially rigorous already (it's short and elementary — no heavy machinery, no missing cases visible on inspection, though a formal writeup still needs to nail the r>1 sub-case algebra and the "board" vs "single prime" bookkeeping carefully).

### Distinct openings
1. **Global gcd-invariant + Euclid-subtraction identity** (main finding above) — gives both parts cleanly, essentially complete.
2. **Lexicographic (Ω, count>1) monovariant** for termination — independent of the invariant, needed regardless of which approach for (b) is used.
3. (Ruled out) Sorting-network / 0-1 principle on min,max — mathematically inapplicable since the actual transform is (min,|diff|), not (min,max). Do not pursue.
4. Possible alternative framing for (b): induction on number of moves showing the multiset {v_p(a_i)}_i is transformed by an operation that's a special case of the "n-pile subtractive Euclidean algorithm," a known classical process; but the direct invariant argument above is simpler and sufficient — no need for this.

### Candidate technique(s)
Invariants & monovariants (knowledge_base.md "Invariants & monovariants", "Invariant/monovariant" under General Proof Methods), p-adic valuation bookkeeping, elementary gcd identities (Euclidean algorithm one-step invariance). This is a clean, elementary, invariant/monovariant-based number theory problem — not sorting-network, not heavy machinery.

### Cheap-kill candidates
- v_p count / exponent-vector decomposition per prime is exactly the right structural reduction (confirmed, not a dead end).
- Parity/size bound: not needed here; the invariant argument is a direct kill.

### Knowledge-base entries to use
- "Invariants & monovariants" (Combinatorics section) — directly the technique used for both Ω/count descent and the gcd invariant.
- "Invariant / monovariant" under General Proof Methods — termination/uniqueness via monovariant, exactly this problem's shape.
- "Divisor analysis" (Number theory, line ~86-87) — gcd structure, consecutive coprimality flavor, loosely relevant but not load-bearing.
- No entry directly gives "Euclidean subtraction identity gcd(x,y)=gcd(min,|x-y|)" by name — this is elementary and should just be stated/proved inline (one line: gcd(a,b)=gcd(a,b-a) for a≤b, iterated).

### Analogous past problems (cruxes)
Searched crux corpus (`domain=number_theory`/`combinatorics`, subtopics `invariants-and-monovariants`, `p-adic-valuation`, `divisibility-and-gcd`, `processes-and-algorithms`) for "blackboard"/"replace two numbers with gcd/lcm" style processes. **None found that are genuinely analogous** — the corpus has many generic gcd/Euclidean-step cruxes (e.g. `aimo-0893`: "Run a Euclidean-algorithm step on a pair of linear forms... keeping the gcd value set unchanged" — same *flavor* of identity as used here, but on a different problem, polynomial coefficients not board processes) but nothing matching the specific "pairwise replace with (gcd,lcm/gcd), prove eventual unique survivor" structure. Report: no strong crux match; the elementary invariant argument above is self-contained and doesn't need to borrow a crux move.

### Prior progress
`results/imo-2026-01/current.md` currently empty/unsolved, no approaches filed yet (this is round 1 exploration).

### Dead ends (do not retry)
- **Sorting-network / 0-1 principle on min,max per prime**: mathematically incorrect premise — the actual per-move transform on exponents is (min(x,y), |x−y|), not (min(x,y), max(x,y)). Confirmed by direct computation of v_p(lcm/gcd) = max−min, and by numerical counterexample (boards where naive max-based prediction disagrees with simulated outcome). Any approach assuming valuations get "sorted into place" is unsound.

### Small-case / intuition notes (conjecture confirmed by 1000 random trials, not yet a from-scratch formal writeup)
- M = ∏_p p^{gcd_i v_p(a_i)}, i.e. M is the unique positive integer whose exponent at each prime p is the gcd of that prime's exponents across the initial board. This is strictly smaller (or equal) than the naive max-exponent guess, and strictly larger (or equal) than the plain gcd of the board's integers (e.g. board {6,10,15,4}: plain integer gcd = 1, but M = 30).
- Termination + exactly-one-survivor and the value of M are BOTH essentially proved by the elementary argument above (invariance lemma + lexicographic monovariant + "pick a prime dividing a₁" trick for non-vanishing). This looks like close to a complete, rigorous, short solution — recommend the outliner build directly on this rather than exploring alternate high-power techniques. Remaining rigor work for the builder: (i) write the r=m'n'>1 sub-case algebra precisely (already sketched above), (ii) handle the gcd(0,...,0)=0 boundary convention explicitly and note it never actually triggers for a prime dividing some a_i, (iii) state the well-foundedness of lexicographic (Ω,C) ordering on ℕ×ℕ formally, (iv) double check whether "2026" (n≥2) plays any special role — it does not; the argument works for any n≥2, 2026 is just flavor.
