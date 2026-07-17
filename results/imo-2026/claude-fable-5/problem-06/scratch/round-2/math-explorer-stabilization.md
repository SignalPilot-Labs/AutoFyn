## imo-2026-06 — Antichain Stabilization Subproblem

### The Core Subproblem

We must prove E_n (antichain of minimal prime sets of a_1,...,a_n under inclusion) eventually stabilizes. Once E_n = E* is fixed, the valid set V* is periodic mod L* = prod(primes in ∪E*), and the greedy sequence on a periodic set is arithmetic-periodic.

**Terminology clarification:**
- E_n = minimal elements of {P(a_i) : i ≤ n} under ⊆ (hardest constraints; smallest sets are hardest to hit)
- Valid m: P(m) hits every F ∈ E_n (i.e., m shares a prime with each "hardest" constraint)
- Dominated: P(m) ⊇ some F ∈ E_n (valid m whose prime set contains an entire constraint)
- E_n changes at step n+1 iff P(a_{n+1}) is non-dominated (P(a_{n+1}) does not contain any F ∈ E_n)

---

### Assessment of All Five Approaches

**Approach A — Density monovariant:**
PARTIALLY CORRECT but INSUFFICIENT on its own. Each non-dominated term strictly decreases the natural density d_n of V_n. However, d_n is a non-increasing sequence of positive rationals bounded ABOVE but NOT BELOW (d_n can approach 0 while V_n remains infinite — e.g., as a sparse but infinite set). No positive lower bound on d_n follows purely from the infinite sequence. The density argument is real evidence but cannot close the proof.

**Approach B — Dickson/WQO:**
THIS IS THE CORRECT APPROACH, but requires care. The key is NOT applying Dickson to E_n directly (the universe of prime sets is infinite, so antichains can be infinite). Instead:

**CORRECT WQO ARGUMENT (the crux):**

1. **Clique property**: Every pair (a_i, a_j) shares a prime (by definition of the sequence). Therefore every a_i is always valid: for any n and any i, gcd(a_i, a_k) > 1 for all k ≤ n (since either k ≤ i or k > i, and both cases are covered by the greedy construction). Hence P(a_i) hits all F ∈ E_n for ALL n.

2. **Domination lemma**: If P(a_i) ⊆ P(a_j) for some i < j, then a_j is dominated. *Proof*: P(a_i) is in the collection {P(a_k) : k ≤ j-1}. So E_{j-1} (minimal elements of this collection) contains some F ⊆ P(a_i) ⊆ P(a_j). Hence a_j is dominated by F. ✓

3. **Non-dominated terms form a bad sequence**: Among non-dominated terms a_{n_1}, a_{n_2}, ... (with n_1 < n_2 < ...), we cannot have P(a_{n_i}) ⊆ P(a_{n_j}) for any i < j (by step 2, that would make a_{n_j} dominated, contradicting non-dominated status). So the prime sets of non-dominated terms form a sequence with **no good pair** (no i < j with P(a_{n_i}) ⊆ P(a_{n_j})).

4. **Dickson's lemma concludes**: Finite subsets of N (or primes) under inclusion form a WQO (well-quasi-order). By WQO, every infinite sequence has an infinite increasing subsequence, equivalently no infinite "bad sequence" exists. The non-dominated terms form a bad sequence, so they are **finite**. QED.

**Obstacle for Approach B**: The WQO must be applied to the *non-dominated terms' prime sets*, not to E_n directly. The non-trivial insight is that step 2 (domination lemma) makes the non-dominated prime sets a bad sequence.

**Approach C — Structural constraint on new antichain elements:**
This is essentially the domination lemma of Approach B viewed from the other side. A non-dominated term a_{n+1} has P(a_{n+1}) incomparable to all F ∈ E_n (hits all F but doesn't contain any). The KEY BOUND: such a term's prime set can NEVER contain any earlier term's prime set (by the domination lemma), putting it in a bad sequence. Approach C correctly identifies the structural obstacle but the WQO conclusion from Approach B is what closes it.

**Approach D — Self-consistency is reached once every valid m is dominated:**
PARTIALLY USEFUL. Self-consistency of E* means every valid m is dominated. One characterizes self-consistency as: every minimal transversal (minimal hitting set) of E* is in E* (contains some element of E*). The earlier Round 1 claim "self-consistent = has a singleton" is **WRONG** — example refutation: E* = {{2,3},{2,5},{3,5}} has no singleton but IS self-consistent (every valid m is divisible by at least 2 of {2,3,5}, hence contains one of the 2-element sets). The correct criterion: E* is self-consistent iff every minimal transversal T of E* satisfies T ⊇ some F ∈ E*. This is equivalent to E_n stabilizing (once stable, it's automatically self-consistent). Approach D does not give a clean path to proving termination.

**Approach E — Finite primes first:**
The observation is correct: every F ∈ E_n must be hit by a_1 (always valid), so F ∩ P(a_1) ≠ ∅. Thus every element of E_n intersects the FIXED FINITE SET P(a_1). This is a useful structural fact but does NOT bound |E_n| or the primes in E_n (an antichain of sets each intersecting a fixed k-element set can still be infinite). Approach E alone is insufficient.

---

### The Complete Proof Sketch for Antichain Stabilization

**Theorem**: E_n eventually stabilizes.

**Proof**:
- By the clique property, every term a_i hits every F ∈ E_n for all n.
- If P(a_i) ⊆ P(a_j) for i < j: E_{j-1} has some F ⊆ P(a_i) ⊆ P(a_j), so a_j is dominated.
- The non-dominated terms have prime sets with no good pair under ⊆.
- By Dickson's lemma (finite prime subsets are WQO), the non-dominated terms are finite.
- After the last non-dominated term, E_n never changes. □

---

### OPEN GAP: Global vs. Eventual Periodicity

After E_n = E* stabilizes at step N, the greedy sequence is periodic with period T (index) and shift L (value) for n ≥ N. The problem requires a_{n+T} = a_n + L for ALL n ≥ 1, not just n ≥ N.

**Why this is non-trivial**: For n < N, the valid set V_n ⊋ V*, so the greedy picks from a LARGER valid set and may pick different (smaller) values than the greedy on V*. The early terms a_1,...,a_N may not fit the same T, L period.

**Possible resolution**: Since all terms a_1,...,a_n are in V* (clique property), the entire sequence is contained in V*. The sequence satisfies: for n ≥ N, a_{n+1} = min{m > a_n : m ∈ V*}. For n < N: a_{n+1} = min{m > a_n : m ∈ V_n} where V_n ⊇ V*. So a_{n+1} ≤ the V*-greedy choice. But also a_{n+1} ∈ V* so a_{n+1} ≥ min(V* ∩ (a_n, ∞)) = V*-greedy choice. Wait — this would make them EQUAL! Let me verify: a_{n+1} = min(V_n ∩ (a_n, ∞)) ≤ min(V* ∩ (a_n, ∞)) and a_{n+1} ∈ V*, so a_{n+1} ≥ min(V* ∩ (a_n, ∞)). Therefore **a_{n+1} = min(V* ∩ (a_n, ∞)) for ALL n ≥ 1** IF a_{n+1} ∈ V* always. And we showed a_{n+1} ∈ V* (since all pairs share primes). **This resolves the gap**: the ENTIRE sequence is the greedy sequence on V* from a_1, so the global arithmetic periodicity follows directly.

**This needs a precise verification**: The claim a_{n+1} ∈ V* requires: a_{n+1} hits all F ∈ E* (the stable antichain). Since a_{n+1} hits all F ∈ E_n ⊇ E* (the valid set is valid for all i ≤ n+1, and E* ⊆ E_n since constraints only get tighter... wait, E* is the EVENTUAL antichain which might be TIGHTER than E_n for small n. So E* ⊆ E_n is WRONG in general.

**Revised gap statement**: It's NOT obvious that all terms a_n satisfy a_n ∈ V*. An early term a_k (k ≤ N) was chosen to be min valid under E_{k-1} ⊆ E* (wait, E grows tighter, so E_{k-1} ⊆ E* under the set of constraints). Actually: E_n can have elements REMOVED as new tighter constraints come in. So E* might have DIFFERENT elements than E_n (not just more). The relationship between E_n and E* is not simply ⊆ or ⊇.

**CONCLUSION ON GAP**: The global periodicity is the key remaining open gap. The candidate resolution (a_{n+1} ∈ V* always) needs careful verification. If it holds, the entire sequence is the greedy sequence on V* and the global periodicity is immediate.

---

### Distinct Openings for the Outliner

1. **WQO via domination lemma** (Approach B, cleanest): Prove "non-dominated terms form a bad sequence → finite by Dickson" using the domination lemma as the key bridge. Then address global periodicity.

2. **Direct density argument with lower bound** (Approach A): If one can show d_n is bounded below by some ε > 0 (possibly using the greedy property to argue the minimum valid element stays ≤ a_1), then the finitely-many-values-of-d_n argument closes the problem.

3. **Structural: all terms ∈ V* from the start** (Approach D variant): If one can verify the greedy always chooses from V* (equivalently, V_n ∩ (a_{n-1},∞) intersects V*), then the problem reduces to periodicity of greedy sequence on periodic set — and global periodicity is automatic.

---

### Candidate Techniques
- **Dickson's Lemma / Higman's lemma** (WQO for finite sets under inclusion) — the key termination tool
- **Clique property** of the sequence (all pairs share a prime) — foundation for all arguments
- **Greedy domination lemma**: P(a_i) ⊆ P(a_j) for i < j → a_j dominated

### Knowledge-Base Entries
- "Divisor analysis" and "Dirichlet's theorem" (number theory section)
- "Invariants and monovariants" (the bad-sequence argument is a monovariant approach)
- WQO / Dickson's Lemma is not explicitly listed in knowledge_base.md but is closely related to the "size-bounding-and-descent" family

### Analogous Past Problems (cruxes)

From the crux corpus search, the closest analogues are:
- **aimo-0477**: "Track gcd(fixed term, current term) and show it divides the next one, producing a divisor-chain bounded by the fixed term that must stabilize." Crux: ascending divisor chain in a fixed bound → stabilizes. Analogous because our E_n changes correspond to divisibility chains, and Dickson-type reasoning terminates them. Problem ID: aimo-0477.
- **aimo-0212**: "Show every prime dividing a polynomial's values lies in a fixed finite set." Analogous because it bounds the essential primes appearing in a recursive structure. Problem ID: aimo-0212.

No crux was found specifically about antichain stabilization for greedy prime-sharing sequences — this problem appears genuinely novel in the corpus.

### Prior Progress
None (unsolved, first round of approaches).

### Dead Ends
- "Self-consistency requires a singleton in E_n" — WRONG. Example: E* = {{2,3},{2,5},{3,5}} is self-consistent with no singleton. Do not use this characterization.
- Pure density argument: d_n > 0 always but can approach 0; no positive lower bound follows from sequence being infinite alone.
- Applying Dickson directly to the sequence of antichains E_n or to all prime sets: doesn't bound E_n since the universe is infinite. Must apply Dickson to the SUBsequence of non-dominated prime sets specifically.
- "Primes in E_n are bounded by P(a_1)": E_n can gain new primes via non-dominated terms.

### Small-Case / Intuition Notes

Experimental insight (from Round 1): The valid set V mod M stabilizes quickly in examples (often within the first few terms), before the prime set stabilizes globally. The essential structure is captured by E_n becoming self-consistent, which via the WQO argument requires only finitely many non-dominated steps. This is a CONJECTURE verified experimentally; the WQO argument above provides the rigorous proof.

The minimum valid integer m_n = min(V_n) is non-decreasing (V_n shrinks) and bounded above by a_1 (always valid), so m_n stabilizes. This is a clean intermediate fact, but alone doesn't close the gap.

### Summary

**Most promising route**: WQO via domination lemma (Approach B). The proof is:
(i) Clique property → every a_i hits every F ∈ E_n; (ii) Domination lemma via collection minimality; (iii) Non-dominated terms = bad sequence in WQO → finite; (iv) E_n stabilizes; (v) V* is periodic; (vi) Greedy on periodic set is arithmetic-periodic; (vii) Global periodicity resolution (verify all a_n ∈ V*).

**Hardest remaining gap**: Step (vii) — showing the global periodicity (for all n ≥ 1) follows cleanly, specifically that the early terms (n ≤ N) satisfy the same T, L as the eventual period. The candidate resolution is: a_{n+1} = min(V* ∩ (a_n, ∞)) for ALL n (because a_{n+1} ∈ V* and a_{n+1} ≥ min(V* ∩ (a_n, ∞)) since V_n ⊇ V*). But this requires confirming a_{n+1} ∈ V* carefully — specifically, that every a_n hits all F ∈ E* (the stable eventual antichain). This may require tracking which F ∈ E* existed BEFORE step n, since E* ⊆ {eventual antichain} might require terms before step N to hit constraints added after N.
