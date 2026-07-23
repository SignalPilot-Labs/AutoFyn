## imo-2026-06 — Periodicity Route Scouting

### Setup

The greedy gcd-sequence forces every pair of terms to share a prime (CLIQUE LEMMA, immediate from definition: a_{n+1} is chosen to share a prime with every a_i for i ≤ n, so gcd(a_i, a_j) > 1 for all i < j).

The antichain E_n = minimal prime sets in {P(a_1), ..., P(a_n)} under inclusion captures the validity condition: m is valid at step n iff P(m) intersects every F ∈ E_n. Stabilization of E_n → E* is assumed here; we assess the periodicity argument given stabilization.

Let S = ∪E*, L = ∏_{p ∈ S} p, V_∞ = {m ≥ 1 : P(m) ∩ F ≠ ∅ for all F ∈ E*}, T = |V_∞ ∩ {1,...,L}|.

---

### Claim 1: V_∞ + L = V_∞

**Status: CORRECT and simple.** For any F ∈ E* and p ∈ F, we have p ∈ S, hence p | L. So p | m iff p | (m + L) (since m + L ≡ m mod p). Therefore P(m) ∩ F ≠ ∅ iff P(m+L) ∩ F ≠ ∅ for every F ∈ E*. Hence V_∞ + L = V_∞. ✓

Note: L need not be the MINIMAL period of V_∞; it suffices that V_∞ is L-periodic. The residues in {1,...,L} satisfying all hitting conditions give exactly T residues. Computationally verified: for a1=15 (T=8, L=30), for a1=35 (T=34, L=210).

---

### Claim 2: Global periodicity a_{n+T} = a_n + L for ALL n ≥ 1

**This requires two sub-arguments.**

**Sub-claim A: Every a_n lies in V_∞.**

This is the key insight. Proof: every F ∈ E* satisfies F = P(a_k) for some specific index k (because E_n is built from actual prime sets of terms — the antichain consists of prime sets of terms, not arbitrary sets). For any n, the clique property gives gcd(a_n, a_k) > 1, i.e., P(a_n) ∩ P(a_k) = P(a_n) ∩ F ≠ ∅. Since this holds for every F ∈ E*, we get a_n ∈ V_∞. QED.

Computationally confirmed: for a1=15 and a1=35, all computed terms lie in V_∞. Also confirmed: no element of V_∞ appears between consecutive terms a_n, a_{n+1}.

**Sub-claim B: The greedy choice from V_{n-1} equals the greedy choice from V_∞.**

Since E_∞ ⊆ E_{n-1} (the stable antichain is a refinement of any earlier antichain, meaning V_∞ ⊆ V_{n-1}):
- Every element of V_∞ is in V_{n-1}; so a_n = min(V_{n-1} ∩ (a_{n-1}, ∞)) ≤ m' := min(V_∞ ∩ (a_{n-1}, ∞)).
- But a_n ∈ V_∞ (Sub-claim A) and a_n > a_{n-1}, so a_n ≥ m'.
- Therefore a_n = m' = the greedy choice from V_∞.

This holds for ALL n, not just n > N. The entire sequence (a_n)_{n≥1} IS the greedy sequence on V_∞, starting from a_1.

**Conclusion:** Since the greedy sequence on V_∞ is determined solely by (a_n mod L), and V_∞ has T residues mod L cycling through in order, the sequence of gaps d_j = a_{j+1} - a_j is purely T-periodic: d_{j+T} = d_j for all j ≥ 1. Summing: a_{n+T} - a_n = sum_{j=n}^{n+T-1} d_j = (one full cycle of gaps) = L. QED.

**The problem asks "for all n ≥ 1"** — this is the global statement, not "eventually." The clique-lemma bridge (Sub-claim A → Sub-claim B) is exactly what makes it global rather than merely eventual.

---

### Claim 3: The greedy map on V_∞ is a pure cycle (T-cycle, no transient)

**Status: CORRECT.** V_∞ ∩ {1,...,L} = {r_1 < r_2 < ... < r_T}. The map σ: r_i ↦ r_{i+1} (with σ(r_T) = r_1 + L, but as residue: r_1) is the unique "next in V_∞" map. It visits all T residues before returning, so it IS a T-cycle (no proper subcycle exists a priori — but there could be if V_∞ has a smaller period L' | L). In any case, T is the MINIMAL period of the residue sequence. Sum of all T gaps = L (verified computationally: for a1=35, T=34 gaps sum to L=210). So: a_{n+T} = a_n + L for all n. ✓

There is no transient because the greedy map is "next element in V_∞," which is a bijection on the T residues. The orbit is purely periodic.

---

### Claim 4: V_∞ is nonempty

**Status: CLEAR.** The sequence is well-defined (there always exists a valid next term, since any product of one element from each F ∈ E* is a valid candidate). More directly: E* is a cross-intersecting antichain (any two elements intersect, by the clique property applied to the terms whose prime sets are the E* elements), so by a covering argument, elements m with P(m) ⊇ F for some F ∈ E* exist and lie in V_∞. V_∞ is infinite since it is nonempty and L-periodic.

---

### Claim 5: V_∞ is self-consistent (adding any m ∈ V_∞ to the sequence doesn't change E*)

**Status: REQUIRES CARE.** Self-consistency means: for every m ∈ V_∞, P(m) ⊇ some F ∈ E* (so P(m) is dominated by an existing antichain element, not a new minimal element). This is a STRONGER condition than m ∈ V_∞ (which only requires P(m) ∩ F ≠ ∅ for each F). A counterexample would have P(m) intersecting each F ∈ E* in exactly one prime but not containing any single F. Such an m would introduce a new minimal prime set, changing E*.

**This is the gap in the self-consistency argument.** The explorer notes: if m ∈ V_∞ but P(m) ⊄ F for any F ∈ E*, then adding m would potentially change E*. However: if E* is truly stable, any m the greedy algorithm would eventually pick from V_∞ must have P(m) ⊇ some F ∈ E*. The correct argument is: once E_n = E* (stable), any a_{n+1} chosen by the greedy from V_n = V_∞ has P(a_{n+1}) ⊇ some F ∈ E* (because otherwise E_{n+1} ≠ E_n, contradicting stability). This is a CONSEQUENCE of stability, not a precondition.

The actual stabilization argument must show: E_n eventually reaches a self-consistent state E* where every subsequent greedy term satisfies P(m) ⊇ some F ∈ E*. This is the hard part, and is separate from the periodicity argument.

---

### Alternative framing: finite-state machine

**Assessment.** One could argue: the sequence (a_n mod L) takes values in a finite set (the T residues in V_∞ ∩ {1,...,L}), the transition is deterministic (next residue = σ(current)), so the residue sequence is eventually periodic. Then lift: "eventually periodic" becomes "globally periodic" via the period-T, shift-L structure.

**Gap in this approach.** "Eventually periodic" in residue means a_{n+T} = a_n + L for n ≥ N (some N). To get ALL n ≥ 1, you need the SAME T, L from the start. This is equivalent to showing the sequence is on V_∞ from the beginning (Sub-claim A above). The finite-state-machine argument alone gives "eventually" but not "globally." The clique argument is still needed.

**Conclusion.** The finite-state-machine framing is useful for the "eventually periodic" reduction, but the clique-lemma argument (Sub-claim A: every a_n ∈ V_∞, hence greedy on V_{n-1} = greedy on V_∞) is the bridge to the global statement.

---

### What is solid vs. what is a gap

**Solid:**
- Claim 1 (V + L = V): clean algebraic argument. ✓
- Claim 2 Sub-claim A (every a_n ∈ V_∞): follows from clique + "E* consists of actual prime sets." ✓
- Claim 2 Sub-claim B (greedy on V_{n-1} = greedy on V_∞): follows from A + V_∞ ⊆ V_{n-1}. ✓
- Claim 3 (pure cycle, T steps advance by L): follows from V_∞ having T residues mod L. ✓
- Claim 4 (V_∞ nonempty): trivial from sequence being well-defined. ✓

**Gaps (not verified here — separate concerns):**
- E* stabilization: the hardest part. Needs a finite-bound argument showing the antichain E_n eventually stops changing. This is NOT addressed in the periodicity claims above — it must be proved separately.
- Self-consistency of E* (Claim 5): follows from stability, but proving stability in the first place is the challenge.
- "E* consists of P(a_k) for actual k" — true by construction of the antichain (it only contains prime sets of actual terms), but the outliner should make this explicit.

---

### Critical observation for the outliner

The GLOBAL statement (all n ≥ 1) vs. eventual statement requires the clique bridge: every a_n ∈ V_∞ (Sub-claim A). This is both the KEY INSIGHT and completely elementary once you see it. The argument is a two-line squeeze: a_n = greedy from V_{n-1} ≤ first element of V_∞ after a_{n-1} (since V_∞ ⊆ V_{n-1}), but a_n ∈ V_∞ (by clique), so equality. This makes the sequence IDENTICALLY equal to the greedy sequence on V_∞ from the very first term — no transient at all.
