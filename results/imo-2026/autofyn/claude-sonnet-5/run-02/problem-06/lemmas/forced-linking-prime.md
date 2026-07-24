## Lemma: Forced-Linking-Prime Lemma (certified, but superseded)

**Source.** `amortized-charging-budget`, Lemma 4 (Section 4).

**Statement.** Fix any index i ≥ 1 and any persistent type A (in the sense of
`persistent-type-pigeonhole.md`) with A ∩ π(i) = ∅ (π(i) := P(a_i) ∩ Q). Then there is
a prime p = p(i,A) dividing a_i such that p | a_j for infinitely many indices j with
π(j) = A.

**Proof.** Let J_A = {j : π(j) = A}, infinite since A is persistent. For all but at
most one j ∈ J_A (namely j ≠ i), the Free Facts lemma gives gcd(a_i, a_j) > 1, so some
prime of the finite set P(a_i) divides a_j. By finite pigeonhole (P(a_i) finite, J_A \
{i} infinite), some single prime p ∈ P(a_i) divides a_j for infinitely many
j ∈ J_A \ {i}. ∎

**Status.** Correct, complete, no gaps, self-contained. HOWEVER: this lemma is
strictly weaker than `bounded-witness-lemma.md` (certified the same round), which gets
divisibility for a FIXED finite witness set F_{A,B} against ALL later same-type terms
from a SINGLE arbitrary witness, rather than "some prime, possibly depending on i,
dividing infinitely many A-terms" extracted via pigeonhole over an a priori unbounded
family of witnesses i. Any approach currently relying on this lemma should prefer
`bounded-witness-lemma.md` instead — it is a strict upgrade and removes exactly the
"could the witness prime vary unboundedly across i" ambiguity that made this lemma hard
to use in the finishing argument.
