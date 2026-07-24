## imo-2026-06 — Sunflower / Δ-system lens

---

### CRITICAL BUG: Lemma S is FALSE in general

**Lemma S as stated ("no two clauses share only a large prime") is false for a₁ = 385 = 5·7·11.**

Computation (500 terms):
- a₅ = 399 = 3·7·19, clause {3, 7, 19}
- a₇ = 418 = 2·11·19, clause {2, 11, 19}
- Shared primes: {19} only; 19 > P₁ = 11. **Lemma S is violated.**

This means **Proposition 1** ("every minimal clause ⊆ {primes ≤ P₁}") is also false for a₁ = 385:
the minimal clauses {19, 3, 7} and {19, 2, 11} each contain the large prime 19 > P₁ = 11.

The current clique-descent and sieve-closure approaches are both chasing a false lemma. The outliner must revise the crux target.

The sequence for a₁ = 385 IS still eventually periodic — the minimal clauses stabilize at stage 38 to the finite family: {2,7}, {2,3,5}, {2,3,11}, {3,7,11}, {3,7,19}, {5,7,11}, {2,11,19} (7 clauses). Essential primes = {2,3,5,7,11,19}, M = 43890. So periodicity holds, but by a different route.

---

### Correct crux

**The true crux is: the family of minimal clauses is finite (equivalently, the essential prime set is finite).** This is strictly weaker than Lemma S. It does NOT require all minimal clauses to lie in {primes ≤ P₁}; it only requires finitely many minimal clauses in total. Lemma S ⟹ correct crux, but the correct crux does not ⟹ Lemma S.

Both existing approaches establish: "finite minimal clause family ⟹ A is periodic ⟹ sequence satisfies a_{n+T} = a_n + L." That finish is correct and reusable. Only the route to finiteness must be rebuilt.

---

### Sunflower / Δ-system terrain

**What the computation reveals for a₁ = 385:**

The minimal clauses with the large prime 19 are exactly {19, 3, 7} and {19, 2, 11}. These form a **2-sunflower with core {19}** and petals {3,7} and {2,11}:
- Core: {19}
- Petals: the petal small-prime sets {3,7} and {2,11} are **pairwise disjoint** subsets of Π_small = {2,3,5,7,11}

**Mutual-witness structure:** The two large-prime minimal clauses witness each other's minimality:
- {3,7} (= {19,3,7}\{19}) misses the clause {2,11,19} → so {19,3,7} can't shrink to {3,7}
- {2,11} (= {19,2,11}\{19}) misses the clause {3,7,19} → so {19,2,11} can't shrink to {2,11}
Each is minimal BECAUSE the other exists. This is a 2-element self-supporting system.

**Why no third large-prime-19 clause:** A third minimal clause {19, S} would need S to hit all 7 existing minimal clauses but not contain any as a subset. The only 2-element sets {19,p,q} achieving this are {19,2,11} and {19,3,7} (verified exhaustively). The set {19,2,7} hits all clauses but fails minimality because {2,7} ⊊ {19,2,7} and {2,7} is already a minimal clause.

**General principle (sunflower bound on a fixed large prime):**
For a fixed large prime q > P₁, the minimal clauses containing q form a sunflower with core {q}. The petals are small-prime sets S₁, S₂, ... ⊆ Π_small that are:
1. Pairwise disjoint (S_i ∩ S_j = ∅ for i ≠ j, because if two clauses {q,Sᵢ} and {q,Sⱼ} share a small prime then they share a SMALL prime, so Sᵢ ∩ Sⱼ ≠ ∅ would give a small shared prime, contradicting the need for mutual large-prime witnesses — actually this requires more care; what IS true is that removing q from each must miss the other, so each Sᵢ misses {q,Sⱼ} for j≠i, which means Sᵢ ∩ Sⱼ = ∅ since q ∉ Sᵢ).
2. Each Sᵢ is a transversal of all OTHER minimal clauses not containing q (each hits all clauses not involving q, otherwise {q,Sᵢ} couldn't be a term/clause).
3. No Sᵢ contains any other minimal clause as a subset (else {q,Sᵢ} is non-minimal).

Pairwise disjoint nonempty subsets of Π_small number at most |Π_small| = π(P₁). So: the number of minimal clauses with a fixed large prime q is **at most π(P₁)** (the number of primes ≤ P₁). This is finite. 

**The remaining gap in the sunflower approach:**

The sunflower bound shows: for each fixed q, finitely many minimal clauses contain q. But we need finitely many total, which requires finitely many different large primes q to appear in minimal clauses. This is the open sub-problem. The sunflower argument does NOT bound the number of distinct large primes directly.

**Possible way to close it:** When a large prime q enters a minimal clause {q,S}, the petal S must be a transversal of all existing non-q minimal clauses, but NOT a transversal of some clause containing q. This means BOTH {q,S} and its "mutual witness" {q,T} (with S∩T=∅) must be admissible (have actual greedy terms). The GREEDY MINIMALITY of each term forces a size constraint: the product q · (product of S) is SMALLER than any admissible term composed only of primes from Π_small that hit the same constraints. Once the small-prime admissible set becomes dense enough (which happens once the small-prime minimal clause system matures), no "room" remains for a large prime q to sneak in below the small-prime minimum. This is the intuition, but making it rigorous requires bounding when the small-prime structure "closes off."

**Sunflower lemma (Erdős–Ko–Rado, 1960) relevance:**

The Sunflower Lemma states: any family of more than (p-1)^r · r! sets each of size ≤ r contains a p-sunflower. This is not directly applicable here because:
- Minimal clauses don't have bounded size in general
- We want to PROVE finiteness, not assume it
- Even if applicable, it would produce a sunflower structure, not a contradiction
- A sunflower with core {q} (large prime) is exactly what we SEE — it doesn't give a contradiction

The Δ-system (sunflower) structure is a **DESCRIPTION** of the minimal-clause family for fixed large q, not a tool for proving finiteness of distinct large primes.

---

### Distinct openings (new proof angles the outliner can develop)

1. **Small-prime closure approach:** Show that the small-prime minimal clauses (those in {primes ≤ P₁}) stabilize to a finite system M_small, and once M_small stabilizes, all subsequent terms have their support hitting every element of M_small via a small prime (so their small-prime part is already a transversal of M_small). Show this eventually prevents new large-prime minimal clauses from forming (the small-prime transversal always beats the large-prime-containing number in the greedy order).

2. **Descent on the large prime:** Given a minimal clause {q, S} with q large, show there is an earlier term a_j with supp(a_j) ⊆ S ∪ {primes ≤ P₁} (no large primes other than possibly q) that is smaller than the term inducing {q,S}. By greedy minimality, derive a contradiction. This is the spirit of the aimo-0030 descent but adapted to the greedy rather than game moves.

3. **Coloring / pigeonhole on small-prime residues:** Show that for any large prime q that could appear in a minimal clause, there exists a pure-small-prime number (divisible only by primes ≤ P₁) that is smaller AND admissible at the same stage. This would force the greedy to pick the small-prime number instead, preventing {q, S} from being a term.

4. **Contradicting the witness pair:** A minimal clause with large prime q requires a SECOND minimal clause with q (its mutual witness). Show that having TWO terms with the same large prime q in their support forces a common SMALL prime between them (via the greedy's minimality), giving a contradiction that no minimal clause can contain q.

5. **Direct greedy-minimality argument:** The greedy picks a_k = min(A_{k-1} ∩ (a_{k-1},∞)). If supp(a_k) contains a large prime q, show there is a smaller admissible number with support ⊆ {small primes} ∪ {q'} for q' < q (descent on the large prime, reaching a contradiction since q > P₁ means q is not a prime factor of a₁).

---

### Candidate technique(s)

- **Greedy minimality contradiction**: the core technique should exploit that a_k is the MINIMUM admissible integer, and that large primes in clauses can always be "beaten" by a smaller admissible number.
- **Finite intersecting antichains of sets over a fixed ground**: the small-prime clause system is an antichain in 2^{Π_small} (finite), giving a finite number of possible small-prime minimal clauses.
- **Mutual-witness structure bounding**: For each large prime q, the number of minimal clauses with q is ≤ π(P₁) (sunflower petal bound from pairwise disjointness in Π_small).

---

### Cheap-kill candidates

- **The case a₁ = prime power:** If a₁ = p^k, then S₁ = {p} and every clause must contain p. Any two clauses share p ≤ P₁. Lemma S holds trivially and all minimal clauses use only {p}. Periodicity is trivial (A = {multiples of p ≥ a₁}). 
- **The case S₁ = {p₁}** (single prime factor): same as above. Both existing approaches correctly handle this.
- **Parity kill for "large prime enters only once":** If q appears in EXACTLY ONE term's clause, that clause is non-minimal (S_k\{q} hits every clause seen before q first appeared — this is the partial progress already in §5 of clique-descent, the "first-appearance" result). The hard case is when q appears in TWO OR MORE clauses — this is precisely the mutual-witness structure.

---

### Knowledge-base entries to use

- **"Pigeonhole / extremal principle"** (Combinatorics): The key to bounding the number of pairwise-disjoint transversals of a finite set system is a simple pigeonhole/partition argument.
- **"Invariants & monovariants"** (Combinatorics): The number of essential primes is a monovariant-like quantity that can only grow; proving it's bounded is the key.
- **"Extremal principle"** (Combinatorics): Take the MINIMAL violating pair (if any large prime q appears in minimal clause) and derive a contradiction from greedy minimality.
- **"Divisor analysis"** (Number Theory): To show that a small-prime-only number can always beat a large-prime-containing number in the greedy order.
- **"Well-ordering / minimal counterexample"** (General): Standard descent on the violating term.

---

### Analogous past problems (cruxes)

1. **aimo-0030** (`number_theory/size-bounding-and-descent`): THIS IS THE SAME PROBLEM. The "good numbers" in aimo-0030 are exactly our greedy sequence (b₀ = k, b_{n+1} = min{m > b_n : gcd(m, bᵢ) > 1 ∀ i ≤ n}). The key lemma "any two good numbers share a small prime (≤ k)" is almost our Lemma S, but uses "prime ≤ k = a₁" rather than "prime ≤ P₁ = max prime factor of a₁". The crux move in aimo-0030 (Claim 5, Solution 2): take the SMALLEST violating pair; strip large primes from the smaller element to get a pure-small-prime number; show it's coprime to the larger element; derive a contradiction via the existence of a "move" to a good number. The adaptation to our problem is non-trivial because aimo-0030 uses a game structure (bad→good moves) not available in our greedy sequence. HOWEVER: the aimo-0030 proof for Claim 5 establishes "any two terms share a prime ≤ a₁ = k," which is NOT the same as Lemma S (which needs prime ≤ P₁ ≤ a₁ and which fails for a₁ = 385). The aimo-0030 proof would give: any two clauses share a prime ≤ a₁. For a₁ = 385, this means share a prime ≤ 385. The shared prime 19 ≤ 385 is consistent! So aimo-0030's conclusion HOLDS for a₁ = 385 even though Lemma S (share prime ≤ P₁ = 11) fails.

2. **aimo-0030** second crux (size-bounding-and-descent): "Strengthen 'two special objects share some forbidden-class prime' to 'they share an allowed-class prime' by minimal-counterexample descent." This directly suggests that the right formulation is "share a prime dividing a₁" (not just ≤ P₁) — but even "share a prime ≤ a₁" (aimo-0030's result) would NOT directly give finiteness of minimal clauses, since there are still infinitely many primes ≤ a₁.

3. **aimo-0488** (`combinatorics/extremal-principle`): Helly-style bound on intersecting interval family (cyclic). The crux is bounding a combinatorial structure by intersecting compatibility constraints. Less directly analogous but the "constraint intersection to bound size" technique is relevant.

---

### Prior progress

- CERTIFIED (do not re-prove): Tools 1–2, Sub-lemma E, Cor E.1, the stabilization-to-conclusion finish (§§2–4 of clique-descent), Lemma 1 and the finish of sieve-closure. All correct.
- PARTIAL (proved assuming Lemma S): Proposition 1. True in spirit but the conclusion should be "finitely many minimal clauses" rather than "all minimal clauses ⊆ {primes ≤ P₁}."
- FALSE (retract): Lemma S as stated. The correct crux is "finitely many minimal clauses" (no constraint on which primes they contain).

---

### Dead ends (do not retry)

- **Lemma S as stated**: False for a₁ = 385. Do not attempt to prove it. Retract and reframe.
- **"All minimal clauses ⊆ {primes ≤ P₁}"** (Proposition 1's conclusion): False for a₁ = 385. Do not target this.
- **Density monovariant alone (sieve-closure's Lemma 3)**: Correctly noted as insufficient in the approach file; still insufficient.
- **"First-appearance large prime is non-minimal"** (partial progress in clique-descent §5): True but doesn't handle the mutual-witness case (a large prime appearing in TWO clauses that witness each other).

---

### Small-case / intuition notes

- **Conjecture (strong):** For any a₁, the essential prime set is finite and equals the set of primes appearing in the greedy sequence's minimal clause system after stabilization. The essential primes CAN be larger than P₁ (as shown for a₁ = 385 where 19 > P₁ = 11).

- **Conjecture (weaker, what may be provable):** Every large prime q that appears in a minimal clause ALSO appears in at least ONE other minimal clause (the mutual-witness), and the number of minimal clauses with a given large prime q is bounded by π(P₁). Combined with a bound on how many distinct large primes can appear: this would give finiteness.

- **Key asymmetry:** The small-prime minimal clauses (in 2^{Π_small}) form a finite system with at most 2^{π(P₁)} elements. The large-prime minimal clauses are bounded per-prime but unbounded across different primes (potentially). The hard step is bounding the number of distinct large primes.

- **Greedy minimality constraint:** A term a_k with large prime q | a_k exists because a_k < (smallest admissible number with the same small primes but without q). This can only happen finitely many times as the admissible set becomes more constrained (conjecture; need proof).

- **For a₁ = 2310 = 2·3·5·7·11:** With 500 terms computed, many large primes appear in the essential set (up to ~1637). The sequence has NOT stabilized yet. The problem guarantees eventual stabilization, but the proof for large primorials (where the small-prime clause system takes long to mature) seems to require the deepest argument.
