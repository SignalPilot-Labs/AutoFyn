## Lemma: Universal Early Intersection Lemma — CERTIFIED, round 15

**Source.** `n1-periodicity-reconciliation`, round 15 build. Independently re-derived
and confirmed correct by the round-15 proof-reviewer (including a fresh independent
numerical sanity check — see Verification note below).

**Depends on.** Only the certified, unconditional Free Facts Lemma
(`free-facts-gcd.md`, part 1: gcd(a_i,a_k) > 1 for every pair of distinct indices
i, k — an immediate consequence of the problem's own recursive legality condition,
applied for arbitrary i < k and, by symmetry of gcd, for the pair in either order)
and the bare definition of "S-extended-persistent" (occurs at infinitely many
indices). Requires NO FAH hypothesis of any kind.

**Statement.** Let S* ⊇ Q be a finite set of primes for which the Extended
Persistent-Type Pigeonhole applies (giving 𝒫'(S*), N(S*)), and suppose S* is
**self-absorbing**, i.e. P(a_j) ⊆ S* for every j = 1,...,N(S*) (equivalently
S*⁺ = S*, per `self-absorbing-core-theorem.md`'s definition of the absorption
operator). Then for every j = 1,...,N(S*) and every B ∈ 𝒫'(S*):

  P(a_j) ∩ B ≠ ∅.

**Proof.** Fix j ∈ {1,...,N(S*)} and B ∈ 𝒫'(S*). By definition of S*-extended-
persistence, the index set {m ≥ 1 : ρ_{S*}(m) = B} is infinite; since {j} is a
single index, there exists m in this set with m ≠ j. By Free Facts applied to the
distinct indices j, m: gcd(a_j, a_m) > 1, so there is a prime p ∈ P(a_j) ∩ P(a_m).
Since j ≤ N(S*) and S* is self-absorbing, P(a_j) ⊆ S*, so p ∈ S*. Also p ∈ P(a_m)
and p ∈ S*, so p ∈ P(a_m) ∩ S* = ρ_{S*}(m) = B. Hence p ∈ P(a_j) ∩ B, proving
P(a_j) ∩ B ≠ ∅. ∎

(If N(S*) = 0 the statement is vacuously true — there is no j in the empty range
{1,...,0}.)

**Scope / what this does NOT do.** This is a purely structural fact about early
absorbed terms and persistent types at a self-absorbing core; it makes no claim
about FAH (whether two DISJOINT-base-type persistent types intersect each other) —
it only shows a single early term (fully contained in S* by self-absorption)
automatically intersects every persistent type, which is a strictly different (and
easier) statement than FAH itself. Do not cite this lemma as any form of progress
on FAH/Cofinite FAH; it is purely an n=1-gap tool, orthogonal to the primary crux.

**Verification note (round 15 proof-reviewer, CERTIFIED).** Independently
re-derived the proof from scratch (confirmed: Free Facts is unconditionally true
for every pair of distinct indices regardless of order, since for i<k it follows
directly from a_k's own legality-defining condition, and gcd is symmetric so the
statement transfers to the pair in either order; the "pick m≠j" step is valid since
an infinite index set minus one point is still nonempty). Also ran an independent
fresh Python simulation (a_1=175, 3000 terms, a generous self-absorbing-style proxy
core S0={2,3,5,7,11,13,17} from the first 20 terms' factorizations, "persistent-like"
types = those occurring in >1% of a long tail window) and reproduced the builder's
reported "480 checks, 0 violations" exactly. No gap found. **Certified.**
