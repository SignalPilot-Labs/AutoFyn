## Lemma: Canonical-witness extra-prime sets intersect (F_A ∩ F_B ≠ ∅) (certified)

**Source.** Independently proved in both `covering-system-construction` (Step 4e) and
`greedy-exchange-cost-potential` ("Restated Lemma E"). Same content in different
notation; certified once here, crediting both files.

**Depends on (certified).** `free-facts-gcd.md`, `finite-core-theorem.md`
(for the definitions of m_A, m_B, F_A, F_B).

**Statement.** Let A, B ∈ 𝒫 be disjoint persistent (Q-level) base types, with canonical
witnesses m_A, m_B (Finite Core Theorem) and F_A := P(a_{m_A}) \ Q, F_B := P(a_{m_B}) \ Q.
Then F_A ∩ F_B ≠ ∅.

**Proof.** Since A ≠ B (disjoint, both nonempty) and τ(m_A) = A ≠ B = τ(m_B), m_A ≠ m_B;
WLOG m_A < m_B. By the Free Facts lemma (`free-facts-gcd.md`), gcd(a_{m_A}, a_{m_B}) > 1,
so some prime p divides both. If p ∈ Q, then p ∈ P(a_{m_A}) ∩ Q = τ(m_A) = A and
p ∈ P(a_{m_B}) ∩ Q = τ(m_B) = B, so p ∈ A ∩ B = ∅, contradiction. Hence p ∉ Q, so
p ∈ P(a_{m_A}) \ Q = F_A and p ∈ P(a_{m_B}) \ Q = F_B, giving p ∈ F_A ∩ F_B. ∎

**Scope.** This is strictly subsumed by the Canonical-Refinement Lemma
(`canonical-refinement-lemma.md`): since A_can = A ∪ F_A and B_can = B ∪ F_B, this Lemma
is exactly the statement A_can ∩ B_can ≠ ∅, i.e. the "both sides canonical" special case
of the Canonical-Refinement Lemma's Theorem. It gives NO new information about arbitrary
(non-canonical) extended-persistent refinements, and does not by itself close gap (†).

**Status.** Correct, complete, no gaps, unconditional; recorded as certified but
superseded in generality by the Canonical-Refinement Lemma (kept as a named lemma since
some approaches cite it directly and its proof is a useful standalone one-liner).
