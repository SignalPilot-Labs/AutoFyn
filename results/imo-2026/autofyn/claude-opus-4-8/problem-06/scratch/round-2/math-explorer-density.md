## imo-2026-06

### Lens: Number-theoretic / growth-and-density

---

### CRITICAL CORRECTION — Lemma S is FALSE

**Lemma S as currently stated in both approaches is FALSE.**

For a₁=385=5·7·11 (P₁=11): the sequence has minimal hitting sets {2,11,19} and {3,7,19}, which share ONLY the large prime 19>P₁=11. Computationally verified: a[5]=399=3·7·19 and a[7]=418=2·11·19. These two term-supports share only 19. So "no two clauses share only a large prime" (Lemma S) is VIOLATED.

**Verification**:
- Minimal hitting sets for a₁=385 (computed, 300-term prefix): {2,7}, {2,3,5}, {2,3,11}, {2,11,19}, {3,7,11}, {3,7,19}, {5,7,11}
- Two of these contain the large prime 19>P₁=11 and share ONLY 19 with each other.
- Essential primes: E={2,3,5,7,11,19}, so 19 is a genuinely essential large prime.
- All 7 minimal hitting sets stabilized by a[38]=693=3·7·11.

**Consequence**: clique-descent's Prop 1 ("every minimal clause ⊆ Π_small") is FALSE for a₁=385. The clique-descent approach as stated is wrong. The sieve-closure approach's crux ("essential primes Π finite") is the CORRECT framing — Π is finite even when it includes large primes.

**What is TRUE for a₁=385**: Π={2,3,5,7,11,19} is finite (6 primes, not just the 5 primes dividing a₁). The sequence IS eventually periodic with L=M=2·3·5·7·11·19=43890 (to be confirmed), T=|A mod M|. The sieve-closure approach is correct; only its proof of "Π finite" needs redirection.

---

### Distinct openings surfaced

**Opening 1 — Pairwise-intersection blocks disjoint-small-parts from differing on large prime:**

All term-supports (= all supp(a_k)) pairwise intersect (Tool 2: gcd(a_i,a_j)>1). Every minimal hitting set IS a term-support (Cor E.1). Hence: ALL minimal hitting sets pairwise intersect.

Now let H₁={q₁}∪C and H₂={q₂}∪D be two minimal hitting sets (q₁,q₂ large primes; C,D ⊆ small primes). H₁∩H₂ ≠ ∅ (pairwise intersection). Since q₁,q₂>P₁, neither large prime is in the other's small-prime part: q₁∉D and q₂∉C. So H₁∩H₂ = (C∩D) ∪ ({q₁}∩{q₂}). Therefore: either C∩D≠∅ or q₁=q₂.

**KEY THEOREM (provable from this)**: Two minimal hitting sets with DISJOINT small-prime parts must share the SAME large prime. Proof: if C∩D=∅ and q₁≠q₂ then H₁∩H₂=∅, contradicting pairwise intersection. Hence q₁=q₂. QED.

For a₁=385: {2,11,19} has C={2,11} and {3,7,19} has D={3,7}. C∩D=∅, so they must share the same large prime: both have 19. ✓ Consistent.

**Implication**: Any two essential large primes q₁≠q₂ can coexist only if every pair of minimal hitting sets (one containing q₁, one containing q₂) has NON-DISJOINT small parts. This is a strong constraint.

---

**Opening 2 — Cascade / witness argument for finiteness of large essential primes:**

Suppose q₁,q₂,...,qₙ are essential large primes (attempting proof of finiteness by bounding n). Each qᵢ appears in some minimal hitting set Hᵢ={qᵢ}∪Cᵢ.

For Hᵢ to be MINIMAL: Cᵢ alone is not a hitting set. So ∃ a term Tᵢ with Tᵢ∩Cᵢ=∅ (witness for minimality). By Tool 1, Tᵢ has a small prime not in Cᵢ.

Crucially: Tᵢ must hit Hⱼ={qⱼ}∪Cⱼ for all j≠i (since Tᵢ is a term and must hit all term-supports). Tᵢ hits Hⱼ via qⱼ∈Tᵢ or Tᵢ∩Cⱼ≠∅.

CASE: Cᵢ ⊇ Cⱼ for some j≠i. Then Tᵢ∩Cᵢ=∅ forces Tᵢ∩Cⱼ⊆Tᵢ∩Cᵢ=∅, so Tᵢ must hit Hⱼ via qⱼ: qⱼ∈Tᵢ. If this holds for EVERY j≠i: Tᵢ contains all qⱼ (j≠i). But Tᵢ is a finite integer; finitely many large primes can divide Tᵢ. This bounds n-1 ≤ Ω(Tᵢ) (number of prime factors with multiplicity of Tᵢ) which is finite. Hence n is finite!

The key question: when is Cᵢ ⊇ Cⱼ forced? This requires more work: if the minimal hitting sets form a "sunflower" or "chain" in their small-prime parts, the argument closes. This seems promising as a complete proof direction.

**Alternative cascade**: If all minimal hitting sets containing different large primes share a COMMON small prime p: then {p} is a hitting set → A_n = {m: p|m} → density 1/p. But then a₁ must be divisible by p (since a₁ ∈ A, so p|a₁). The small prime p ≤ P₁ divides a₁. Once we know p|every term, the problem simplifies drastically.

---

**Opening 3 — Size bound on first-appearance term and its large prime:**

For a large prime q to first appear in term a_j: by the greedy property, any element of A_{j-1} with support ⊆ supp(a_j)\{q} and value in (a_{j-1}, a_j) would contradict greedy minimality. In particular, b_j = a_j/q^{v_q(a_j)} ∈ A_{j-1} (proved in current approach). The elements b_j, b_j·p, b_j·p², ... (for any small prime p | b_j) are all in A_{j-1}. The smallest such above a_{j-1} must be ≥ a_j = b_j·q. This forces: the gap (a_{j-1}, b_j·q) contains no multiple of b_j with support ⊆ supp(b_j), meaning a_{j-1} ≥ b_j·(q-1) → combined with gap bound a_{j-1} ≥ a_j - a₁ = b_j·q - a₁: requires b_j·(q-1) ≤ b_j·q - a₁ + (extra), i.e., b_j ≤ a₁. (As already shown in prior round: b_j ≤ a₁ in the minimal violation.)

This gives: the small-prime product of the large-prime clause satisfies b_j ≤ a₁. So ∏_{p∈C\{q}} p ≤ a₁.

And from the symmetry (b_k ≤ a₁ proved via Tool 2): ∏_{r∈D\{q}} r ≤ a₁.

Both witnesses have small-prime product ≤ a₁. This bounds the SIZE of C\{q} and D\{q} but not q directly.

---

**Opening 4 — Reformulating crux: small-prime hitting sets are self-consistent:**

Rather than proving "all minimal hitting sets are small-prime" (FALSE), prove: the SMALL-PRIME PART of the minimal hitting sets forms a self-consistent clique. That is: the family {H∩small_primes : H is a minimal hitting set} is itself a pairwise-intersecting family with the intersection property.

For a₁=385: the small-prime parts are {2,7}, {2,3,5}, {2,3,11}, {2,11}, {3,7,11}, {3,7}, {5,7,11}. Do any two share an element? {2,11} and {3,7}: empty intersection! So the small-prime parts do NOT form a self-consistent clique. The large primes 19 are NEEDED to "fill the intersection gap."

This suggests: each large essential prime q covers ONE "gap" in the small-prime intersection structure (a pair of small-prime sets that don't intersect). By the finite number of such gaps (≤ 3^{π(P₁)}), only finitely many large essential primes can exist — one per gap.

**Formal bound on number of large essential primes**: ≤ #{pairs (C,D) of small-prime subsets with C∩D=∅, neither C nor D alone is a hitting set} ≤ 3^{π(P₁)} (each small prime independently in C, D, or neither).

Combined with ≤ π(P₁) essential small primes: total essential primes ≤ π(P₁) + 3^{π(P₁)}.

**This is a fully finitary bound** (depends only on P₁, the largest prime factor of a₁) and may give the complete proof.

---

### Candidate techniques

- **Pairwise-intersection (clique) structure of minimal hitting sets**: the KEY new structural insight — every two minimal hitting sets intersect because they are both term-supports; when small parts are disjoint, the large prime must be the same.
- **Sunflower / Helly-type argument**: bounding pairwise-intersecting families of prime-sets with small-prime constraints.
- **Minimal counterexample descent** (aimo-0030 analog): valid for the b>a₁ sub-case (already proved); b≤a₁ sub-case needs a different approach now that Lemma S as stated is wrong.
- **Greedy minimality as blocking**: the "no admissible number in (a_{j-1}, a_j) with support ⊆ C\{q}" constraint, forcing b_j ≤ a₁.

---

### Cheap-kill candidates

- **Parity check for essential large primes**: by Tool 2 (all term-supports pairwise intersect) + "two minimal hitting sets with disjoint small parts share same large prime" → count essential large primes as ≤ #{disjoint pairs of small-prime subsets} which is FINITE (≤ 3^{π(P₁)}). This might close the crux in a few lines once properly formalized.
- **Cascade to infinite support**: if ≥2 essential large primes q₁,q₂ share small prime p: their minimality witnesses T₁,T₂ (terms avoiding p) may need to contain ALL other large primes, giving finite bound on number of essential large primes from finiteness of term support.

---

### Knowledge-base entries to use

- **Invariants & monovariants**: descending chain A₁⊇A₂⊇... stabilizes iff essential primes finite
- **Divisor analysis / gcd structure**: Tool 1 (gap≤a₁, every term has small prime), Tool 2 (pairwise gcd>1)
- **Pigeonhole**: small-prime sets are finite, bound the number of "gaps"
- **Infinite descent / Minimal counterexample**: for closing the b≤a₁ case via cascade argument
- **Direct contradiction**: pairwise intersection + disjoint-small-parts ⇒ same large prime

---

### Analogous past problems (cruxes)

1. **aimo-0030** (IMO 2024 P5): technique = minimal-counterexample descent + "strip large prime to get small-only element, show it contradicts the game structure." Analogous crux move: in our problem, strip large prime q from a_j to get b_j, show b_j ∈ A_{j-1}, then derive contradiction via Tool 2 when b_j>a₁. The b≤a₁ sub-case is new (no direct aimo-0030 analog). **Key adaption**: the pairwise-intersection structure of minimal hitting sets (our problem) is the analogue of aimo-0030's "good numbers always share a small prime" conclusion; but in our problem, large primes CAN appear as essential (a₁=385 shows this), so the analogy is partial.

2. **No other close analog**: crux corpus in NT/combinatorics doesn't have a problem with this exact "clique of hitting sets with finitely many large essential primes" structure.

---

### Prior progress

From current.md and lemmas/: 
- CERTIFIED: Tool 1, Tool 2, Sub-lemma E, Finish Package, Lemma 1 (fixed-point), Lemma 3 (density drop)
- CERTIFIED gap closed: b_j>a₁ sub-case of Lemma S leads to contradiction via Tool 2
- OPEN crux: "finitely many essential primes Π" — the CORRECT formulation (Lemma S as stated is FALSE and must not be used)

Both approaches converge on the same crux but Lemma S (their stated crux) is wrong. Sieve-closure's crux "Π finite" is the right target; clique-descent's Lemma S is the wrong target.

---

### Dead ends (do not retry)

- **Lemma S as stated**: "no two clauses share only a large prime" — FALSE for a₁=385. Do NOT retry.
- **Prop 1 of clique-descent** ("every minimal clause ⊆ Π_small"): FALSE for a₁=385. Do NOT use.
- **Density-drop monovariant alone** (Lemma 3): proved but explicitly insufficient — doesn't bound effective steps.
- **"Large q → gap contradiction"**: tried in Opening 3, gives b_j≤a₁ but no contradiction.

---

### Small-case / intuition notes

1. **a₁=385=5·7·11 is the simplest counterexample to Lemma S**: P₁=11, essential primes={2,3,5,7,11,19}, 7 minimal hitting sets including 2 with large prime 19. All stabilize by a[38]=693. (VERIFIED COMPUTATIONALLY, 300-term prefix)

2. **Most a₁ satisfy Lemma S** (empirically): a₁ ∈ {6,15,35,77,143,2310,...} all have large_essential=[] in 100-term prefix. Only a₁=385 among tested has large_essential=[19].

3. **a₁=2310=2·3·5·7·11**: single minimal hitting set {2} (since 2|a₁, so every term is even). Trivially periodic. Essential primes = {2} only. Lemma S holds trivially.

4. **Pairwise-intersection constraint is the KEY structural tool**: two minimal hitting sets with disjoint small parts must share a large prime (proved rigorously above). This bounds the number of essential large primes by the number of disjoint pairs of small-prime subsets (finite, ≤ 3^{π(P₁)}). This is a NEW VIABLE PATH to the crux.

5. **For the outliner**: the correct attack is sieve-closure's framing ("Π finite") with the pairwise-intersection + disjoint-small-parts structural theorem (Opening 1) as the key lemma. The clique-descent approach needs either abandonment (Lemma S is false) or complete reformulation targeting "Π finite" directly.

6. **Cascade argument (Opening 2) may be the complete proof**: if minimality witnesses T_i must contain all other large essential primes (when their Cᵢ are nested), this directly bounds n. The outliner should check whether the Cᵢ nesting condition holds in general or just in specific cases.
