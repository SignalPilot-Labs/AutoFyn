## Status
partial (round 13: dispatched a purely defensive/bookkeeping task, NOT a new FAH
attempt — formalize and certify the **No-Restart Lemma**: restarting the greedy
process at a later term `a_{n_0}` (`n_0 ≥ 2`) as if it were a fresh seed produces a
sequence `(b_k)` that generically diverges from the true continuation
`(a_{n_0+k-1})` at the very next step, because legality against the shorter
restarted history `{b_1}` is a strictly weaker (never stronger) condition than
legality against the true full history `{a_1,...,a_{n_0}}` — dropping constraints
can only ADMIT more candidates, never fewer. Proved this in full generality: (i) the
unconditional inequality `b_2 ≤ a_{n_0+1}` for every `n_0 ≥ 2` (pure monotonicity of
legality under a shrinking constraint set — no hypothesis needed); (ii) an explicit,
generic sufficient condition (H') for strict divergence `b_2 < a_{n_0+1}` (some early
term `a_j`, `j < n_0`, blocks a candidate `c` in the open interval `(a_{n_0},
a_{n_0+1})` that the restarted process's lone constraint `a_{n_0}` does not block);
(iii) correctly isolated and excluded the sole degenerate case `n_0 = 1` (empty
earlier history, the two recursions coincide by construction); (iv) a Corollary
making the intended use precise — any restart-based induction (on `ω(a_1)`, or any
minimal-counterexample descent replacing the true tail with a fresh-seed
continuation) is invalid unless it explicitly carries the full original constraint
set forward, at which point it is no longer a genuine dimension reduction. Verified
the worked example independently by direct computation: `a_1 = 15` gives true
sequence `15,18,20,24,30,36,40,42,45,48,50,54,...`; restarting at `a_5 = 30` gives
`30,32,34,36,38,40,42,44,...`, diverging at the very next term (`32` vs the true
`a_6 = 36`), exactly matching the general argument (witness `j=1`: `c=32` is legal
against `{a_5=30}` alone but `gcd(32,15)=1` so illegal against the true full
history). Certified to `lemmas/no-restart-lemma.md`. This closes off, with a single
citable general fact, the recurring failure mode that independently sank
restart-style constructions in rounds 3, 5, and 8 of this workspace (most notably
`seed-coupling-induction`'s round-8 Seed-Coupling Lemma), so future rounds do not
re-lose time to the same mistake in a new disguise. Does not touch FAH, Symmetric
FAH, or gap (†) in any way — no progress on and no claim about the main crux. See
the "ROUND 13" section below for the full write-up; all findings through round 12
below are unchanged and remain valid.)

partial (round 11: outline-reviewer pre-build screening killed the dispatched
"Forced-Escape Blocking Construction" (full-`S₀`-signature CRT-glue competitor)
before build, via a new **CRT Magnitude Obstruction** — the competitor lands
≈8 orders of magnitude above the local window, so Lemma K's dichotomy never
reaches its informative branch (13th confirmed-dead FAH mechanism this
workspace). This round's build then genuinely attempted to rescue the idea
with a WEAKER, partial-signature-matching construction (route (a) of the
dispatch) rather than merely conceding: designed and computationally tested
the cheapest possible variant (matching a single prime of `Q` plus forcing
`q*|c`, modulus as low as 187 instead of ≈9.36×10⁹), and proved a
**Minimal-Modulus Generalization** closing the ENTIRE CRT-glue/competitor-
construction family, not just the literal full-`S₀` version: any such
construction either sacrifices the legality guarantee (making its blocking
witness empirically uninformative — independently confirmed by this round's
math-explorer's Lemma K experiments, which found blocking witnesses are
`S₀`-junk >99% of the time and never the target prime) or requires a modulus
provably no cheaper than the full-`Q` floor (per Lemma A's own proof
structure), which itself already fails magnitude-wise (checked at the
cheapest scale: 0/2499 sampled sequence-gaps reach even the minimal
single-prime-of-`Q` modulus of 187, vs. a max observed gap of 38). This is a
genuine 14th confirmed-dead mechanism, not a restatement of the 13th — route
(a) was attempted and closed, not skipped; route (b) (honest documentation)
follows as a consequence, not a default. FAH/Symmetric FAH remain the sole
open crux. Re-audited the rest of the approach file this round (certified
lemmas, the |Q|=1 special case, the Cofinite-FAH-conditional finish) — no
drift found, all still accurate. See the new "ROUND 11 BUILD" section below
for full detail.)

partial (round 10: CARRIED OUT the dispatched Escape-Budget attack on the Successor
Claim to completion. First resolved the outline-reviewer's flagged imprecision by
proving a new unconditional **Window Resolution Lemma**: the window in the outline's
Step 2 must be read as the telescoped interval up to the next actual A'-occurrence,
never a single literal sequence-step, because (proved, not just illustrated) whenever
a rogue pair exists, infinitely many gaps between consecutive A'-occurrences are ≥ 2
(a B'-occurrence must fall strictly between them infinitely often). Then attempted
the Escape-Budget Lemma itself under this corrected reading and found a clean,
complete NEGATIVE result: the premise "a failure at j forces every q*-multiple in the
window to be illegal" is in fact TRUE (proved rigorously from the greedy definition
alone) but carries ZERO usable information, because the illegality witness index for
a skipped candidate near the end of the window can be ANY of the unboundedly many
intermediate sequence indices between n_j and n_{j+1} (not a single fixed index the
way Confined-GCD's a_{n_B} is) — a new **Growing-Constraint Obstruction**, proved in
full, that answers the outline's own flagged "is the witness pool bounded?" question
negatively and explains precisely why the mechanism cannot be rescued. A secondary,
independent obstruction (Return-Time Boundedness — whether gaps between
A'-occurrences are even uniformly bounded at all) is also identified as open and
empirically NOT obviously bounded (fresh computation on a_1=4807: the max gap for a
sparser extended-persistent type grows from 503 to 670 as the sampled range is
extended from N=4000 to N=6000, no sign of stabilizing). See ROUND 10 section below
for full detail. FAH/Symmetric FAH remain open; this is the tenth mechanism
diagnosed dead this workspace, now via a genuinely new (quantitative/window) route,
strengthening the case (already at 9/9 prior mechanisms) that the missing ingredient
is a source of information about an ARBITRARY intermediate term's factorization, not
obtainable from any composition of Free Facts / gap lemmas / pigeonhole. Round 9's
findings (below) are unchanged and remain the starting point; the Successor-Transport
Reduction Lemma (certified, `lemmas/successor-transport-reduction-lemma.md`) is
imported verbatim as the reduction target.)

partial (round 9: carried out the dispatched cheap-kill check for the "downward-
transport / predecessor-inheritance" mechanism (occurrence j ⟹ occurrence j+1)
BEFORE attempting its proof, per this round's instructions. Result: an extensive
computational search (≈270 fresh seeds, two independent sweeps, targeting specifically
the genuinely open |F'|≥2 or |F''|≥2 regime at a PROPERLY RECRUITED core) found only
one qualifying rogue instance beyond the one already on record (a_1=11305, reconfirmed
here with a larger sample: 79/79, 246/246, 16/16 — zero exceptions) and NO instance
anywhere with an actual FAH failure. So the "scattered vs. runs" discriminating test
mandated by the dispatch could not be run (there is no failure data to classify) —
this is itself reported honestly as new information (very strong empirical support
for literal FAH, not just cofinite FAH, with zero counterexamples now found across
every seed tested by any round). Attempted the transport-induction proof anyway (as
instructed, since nothing falsified it): formalized a genuine, correct reduction
(Successor-Transport Reduction Lemma, new, unconditional, promotable — the successor
claim, if provable, gives cofinite FAH, which the certified chain already proved
sufficient), then showed the successor step itself collapses into the identical
obstruction Lemma I already proved dead — checked directly via Lemma H on the
concrete a_1=4807 and a_1=11305 data, both branches uninformative in exactly the
pattern round 7 already diagnosed. FAH/Symmetric FAH remain open; see ROUND 9 section
below for full detail. Round 8 summary retained below.)

partial (round 7: per this round's mandatory checkpoint, retracted the dispatched
"Two-Witness Intersection Uniqueness via joint Critical-Prime-Dichotomy" mechanism as
dead — confirmed the outline-reviewer's suspicion with both a proof-level argument
(Lemma H's derivation never extracts S₀-type data about a branch-(b) witnessing index)
and a concrete computation on the mechanism's own motivating example (a_1=4807: both
candidate primes trivially land in the uninformative branch (a)). Attempted the
"Blocking-Data Bridging" mechanism using previously-unused illegality/skipped-candidate
data; produced one new, fully proved, promotable unconditional lemma (Lemma K,
Adjacent Multiple Blocking) plus a straightforward refinement (Lemma J,
Divisor-Restricted Pigeonhole), but the combination does not close FAH — precisely
diagnosed obstruction: the constructed competitor's factorization has no controlled
relationship to the witness's own. FAH and Symmetric FAH remain open — see ROUND 7
section below. Round-6 summary retained: attempted FAH directly, extended empirical
verification to 0 counterexamples across 7 seeds / ~90 rogue-pair instances, distilled
three failed mechanisms into the negative result Lemma I — see ROUND 6 section below.)

## Approach: greedy-exchange-cost-potential (explicit integer cost monovariant, minimality/exchange argument)

### Target
The full problem claim: there exist positive integers T and L such that a_{n+T} = a_n + L
for every positive integer n ≥ 1.

### Why this approach exists (round 2 rationale, unchanged from the opening draft)
Both round-1 approaches (`amortized-charging-budget`, `covering-system-construction`)
and the round-1 `hypergraph-transversal` stub independently bottom out on the SAME
combinatorial gap — whether disjoint "persistent types" (or their extended/antichain
refinements) must share a witnessing prime — despite using superficially different
vocabularies (charging, covering systems, antichains). This approach reframes the same
target territory via an explicit integer-valued **cost function** together with a
**minimality/exchange argument** in the style of `aimo-0678`'s "min-of-a-set"
monovariant (`crux_moves_documentation.md`), adapted to this problem's unbounded
(linearly growing) sequence by attaching the potential to *per-term prime content*
rather than to a_n itself.

### ROUND 3 CORRECTION (mandatory retraction, per outline-reviewer instruction)
The previous draft of this file conjectured, based on limited numerics ("6+ seeds"),
that cost(n) := |P(a_n) \ Q| is eventually ≤ 1 in a "sparse Q" regime (Q missing a
small prime), with a larger but bounded constant in a "dense Q" regime. **This
conjecture is FALSE, not merely open, and is retracted here — it must not be pursued
by any future builder of this approach.**

The outline-reviewer (`/tmp/round-2/outline-reviewer.md`) exhibited an explicit
counterexample: **a_1 = 35** (so Q = P(35) = {5,7}, "sparse" since Q misses the small
prime 2 — squarely the regime the conjecture targeted). Checking the tail (n =
2000..4000) of the actual sequence shows:
- The persistent proper base type {5} (i.e. τ(n) = {5} ⊊ Q) recurs hundreds of times
  with ODD terms — e.g. a_153 = 975 = 3 · 5² · 13, a_157 = 1005 = 3 · 5 · 67,
  a_163 = 1035 = 3² · 5 · 23 — a recurring, non-transient pattern, not a finite set of
  early exceptions. So the conjectured "eventually the single prime 2 (or some single
  universal prime) always divides the proper-type terms" claim fails: cost(153) =
  |P(975) \ {5,7}| = |{3,13}| = 2, and this pattern repeats indefinitely, not just once.
- The true eventual period for a_1 = 35 is T = 34, L = 210 = 2·3·5·7 — i.e. the actual
  reconciling core needs **two** extra primes {2,3}, not one. So even the weaker
  "eventually bounded by a small constant depending on the regime" framing, if stated
  as "C = 1 whenever Q is sparse," is false as a dichotomy on Q alone: a_1 = 35 is
  sparse by the stated definition yet needs 2 extra primes, behaving like the "dense"
  fallback case. Sparseness of Q and the number of extra primes eventually needed are
  NOT the same variable, contrary to what the previous draft assumed.
- Moreover, the raw quantity cost(n) = |P(a_n) \ Q| is not even the right invariant to
  track: a_153 = 3·5²·13 carries the genuinely load-bearing prime 3 (part of the actual
  finite core {2,3}) together with the prime 13, which is logically irrelevant "junk" —
  it does not participate in any legality argument, it is simply an incidental factor of
  the particular integer 975. Any bound on cost(n) as literally defined is contaminated
  by such junk and is not the quantity that controls periodicity. This confirms, from a
  different angle, the self-correction already recorded in the round-2 draft (the
  retraction of the false "cost(n) ≤ |𝒫|-1" bound) — both errors share the same root
  cause: |P(a_n)\Q| counts primes that play no role in legality, alongside primes that
  do, and cannot be bounded by the certified lemmas (which only ever guarantee *some*
  shared core prime, never control the total prime-content of a_n).

**Conclusion of the correction:** this approach retracts (i) the "cost(n) ≤ |𝒫|-1"
bound (retracted already in the round-2 draft) and (ii) the "C = 1 in the sparse
regime" conjecture (retracted now, with the explicit falsifying data above). No further
attempt is made to bound cost(n) := |P(a_n)\Q| itself; the approach's genuine
deliverables (below) work instead with the finite core set S from the Finite Core
Theorem and the intersection P(a_n) ∩ (Q∪S), which is immune to junk-prime
contamination by construction.

### Setup and notation (shared free facts)
Let a_1 < a_2 < ... be the sequence, P(m) the set of prime divisors of m, Q := P(a_1)
(finite, nonempty), k := |Q|. τ(n) := P(a_n) ∩ Q.

**Free Facts** (see `lemmas/free-facts-gcd.md`, certified): gcd(a_i,a_j) > 1 for all
i ≠ j; in particular τ(n) ≠ ∅ for all n ≥ 1.

**Bounded Gap Lemma** (see `lemmas/bounded-gap-lemma.md`, certified): a_{n+1} ≤ a_n + a_1
for all n ≥ 1.

**Persistent-Type Pigeonhole** (see `lemmas/persistent-type-pigeonhole.md`, certified):
a finite, nonempty set 𝒫 ⊆ 2^Q \ {∅} of "persistent" base types (occurring infinitely
often) exists, and there is N_0 such that τ(n) ∈ 𝒫 for all n > N_0.

**Bounded Witness Lemma** (see `lemmas/bounded-witness-lemma.md`, certified): for
disjoint persistent types A, B and ANY single witness index m with τ(m) = B, letting
F_{A,B} := P(a_m) \ Q (finite), every n > m with τ(n) = A has a_n divisible by some
prime of F_{A,B}.

**Finite Core Theorem** (see `lemmas/finite-core-theorem.md`, certified): fixing the
canonical witness m_B (smallest n > N_0 with τ(n) = B) for each B ∈ 𝒫, the set
S := ⋃_{B∈𝒫} (P(a_{m_B})\Q) is finite, and there is N_1 such that for every n > N_1 and
every B ∈ 𝒫 disjoint from τ(n), a_n is divisible by some prime of S. **Certified
caveat, unchanged:** this does NOT show a single prime, or the same subset of S, works
across ALL disjoint B simultaneously for a fixed n — that is exactly the open gap (†).

### Genuinely new, unconditional content established this round

**Lemma A (Generalized Bounded Gap fact).** For any positive integer c divisible by
every prime of Q, a_{n+1} ≤ a_n + c for every n ≥ 1. In particular, for any prime p (in
Q or not), a_{n+1} ≤ a_n + a_1·p.

*Proof.* Let r be the smallest multiple of c exceeding a_n; since c ≥ 1, among any c
consecutive integers exactly one is a multiple of c, so r ≤ a_n + c. For i = 1: since
every prime of Q divides c, and (writing a_1 = ∏_{q∈Q} q^{e_q}) every prime factor of
a_1 lies in Q, we get gcd(r, a_1) ≥ q > 1 for any q ∈ Q dividing both c (hence r) and
a_1 — concretely, pick any q ∈ Q; q | a_1 (since Q = P(a_1)) and q | c | r, so q |
gcd(r,a_1), giving gcd(r,a_1) > 1. For 2 ≤ i ≤ n: by Free Facts, gcd(a_i,a_1) > 1, so
some prime q_i ∈ Q divides a_i (since any common divisor's prime factors of a_1 lie in
Q); since q_i ∈ Q, q_i | c | r, so q_i | gcd(r,a_i), giving gcd(r,a_i) > 1. Thus r is a
legal candidate for a_{n+1} for every i = 1,...,n, and by minimality of a_{n+1} (the
smallest legal successor), a_{n+1} ≤ r ≤ a_n + c. Taking c = a_1·p for any prime p (a_1
| c, so every prime of Q divides c) gives the stated corollary. ∎

This subsumes and confirms the previous draft's "Generalized Bounded Gap fact"; it is
correct, new relative to the certified lemma set (a genuine strengthening of the
Bounded Gap Lemma to any Q-multiple modulus, not just c = a_1), and does not depend on
any open gap. **Promotable.**

**Lemma B (Single-Witness-Prime Pigeonhole Refinement of the Bounded Witness Lemma).**
Let A, B ∈ 𝒫 be disjoint persistent types. Then there is a SINGLE prime
p*(A,B) ∈ F_{A,B} ⊆ S (using the canonical witness m_B) such that the set
{n > m_B : τ(n) = A and p*(A,B) | a_n} is infinite.

*Proof.* Let N_A := {n > m_B : τ(n) = A}; this is infinite since A is persistent (only
finitely many n ≤ m_B are excluded). By the Bounded Witness Lemma (with witness m = m_B,
valid since τ(m_B) = B by construction), every n ∈ N_A has a_n divisible by some prime
of the FINITE set F_{A,B}. Define g : N_A → F_{A,B} by choosing, for each n ∈ N_A, some
prime g(n) ∈ F_{A,B} with g(n) | a_n (at least one exists by the Bounded Witness Lemma).
Since F_{A,B} is finite and N_A is infinite, by the infinite pigeonhole principle
(`knowledge_base.md`, "Pigeonhole / extremal principle") some value p* ∈ F_{A,B} is
attained by g on an infinite subset of N_A; i.e. p* | a_n for infinitely many n ∈ N_A. ∎

This is strictly more information than the certified Bounded Witness Lemma alone
provides (which only guarantees *some* prime of F_{A,B} per n, possibly varying with
n): it isolates one specific, explicit prime that recurs infinitely often for each
ordered pair of disjoint persistent types. **Promotable**, though — as shown below — it
is NOT by itself strong enough to close (†).

**Lemma C (Extended Persistent-Type Pigeonhole).** Let S_0 := Q ∪ S (finite, by the
certified Finite Core Theorem) and ρ(n) := P(a_n) ∩ S_0 (nonempty, since τ(n) ⊆ ρ(n)
and τ(n) ≠ ∅ by Free Facts). Then there is a finite, nonempty set 𝒫' ⊆ 2^{S_0}\{∅} of
"extended-persistent" types (occurring infinitely often) and a threshold N_2 such that
ρ(n) ∈ 𝒫' for every n > N_2.

*Proof.* Identical to the certified Persistent-Type Pigeonhole's proof
(`lemmas/persistent-type-pigeonhole.md`) with Q replaced by S_0: ρ maps the infinite
index set into the finite set 2^{S_0}\{∅} of size 2^{|S_0|}-1, so by the infinite
pigeonhole principle some value is attained infinitely often (nonempty, giving 𝒫'
nonempty); every type not in 𝒫' occurs only finitely often, and there are finitely many
such types, so the total number of indices with ρ(n) ∉ 𝒫' is finite; let N_2 be the
largest such index (or N_1 if none, so that the Finite Core Theorem's threshold is also
respected). ∎

**Promotable** — a genuine, gap-free extension of the certified Persistent-Type
Pigeonhole from Q to the larger fixed finite set S_0 = Q ∪ S.

### Where this leaves gap (†), and why Lemmas B and C do not close it

The natural next step is to try to upgrade Lemma B to the extended-type level: given
disjoint persistent BASE types A, B (A ∩ B = ∅ in Q) with extended-persistent
refinements A', B' ∈ 𝒫' (A' ∩ Q = A, B' ∩ Q = B), show A' ∩ B' ≠ ∅ — i.e. that some
prime of S is shared by the extended types, which is exactly (†) in its cleanest form
(as recorded in `current.md`).

**Attempted argument and where it stalls (recorded honestly, not smoothed over).** Fix
any witness index m with ρ(m) = B' (infinitely many exist since B' is extended-
persistent by Lemma C); this m need NOT be the canonical witness m_B used to build S.
Consider N_{A'} := {n > m : ρ(n) = A'}, infinite by Lemma C. By Free Facts,
gcd(a_n, a_m) > 1 for each n ∈ N_{A'}, giving a shared prime p_n ∈ P(a_m) (a FIXED
finite set, since a_m is one fixed integer). By the infinite pigeonhole principle
(same mechanism as Lemma B's proof), some single prime p** ∈ P(a_m) divides a_n for
infinitely many n ∈ N_{A'}. If p** ∈ Q: then p** ∈ ρ(m) ∩ Q = B and p** ∈ ρ(n) ∩ Q = A
for such n, giving p** ∈ A ∩ B = ∅ (A, B disjoint base types) — contradiction. So
p** ∉ Q. **But p** need NOT lie in S**: P(a_m) is the FULL prime factorization of the
single fixed integer a_m, which (exactly as the a_1 = 35 counterexample illustrates
with primes like 13, 23, 67) can contain primes entirely outside the fixed core S_0 —
"junk" primes specific to this one witness m, with no reason to recur across different
choices of m. Unlike Lemma B (which used the CANONICAL witness m_B, guaranteeing
F_{A,B} = P(a_{m_B})\Q ⊆ S by the very definition of S), this argument uses an
arbitrary witness m of extended type B', and there is no certified reason for P(a_m)\Q
to be contained in S when m is not one of the finitely many canonical witnesses.

Restricting m to be the canonical witness m_B does not immediately fix this either: the
canonical witness m_B has a specific BASE type τ(m_B) = B, but its EXTENDED type
ρ(m_B) is some one particular element of 2^{S_0}, not necessarily itself in 𝒫' (an
extended-persistent type need not contain the base-type canonical witness's extended
type — many different extended types can share the same base type, and the canonical
witness realizes only one of them). So there is no certified way, established here, to
guarantee that the prime recruited by Lemma B's mechanism, applied at the canonical
witness, is also the prime responsible for reconciling the (possibly different)
extended-persistent refinements A', B' of A, B.

**Conclusion, stated honestly:** Lemmas B and C sharpen the *data available* about gap
(†) (a specific candidate prime per pair of persistent types, and a well-defined finite
extended-type space 𝒫'), but neither closes it, and the natural attempt to combine them
runs into the SAME underlying obstruction as (†) in `covering-system-construction`
(namely: a witness index's *full* factorization can contain primes outside the fixed
core, and there is no certified argument ruling this out or showing it doesn't disrupt
the reconciliation needed for periodicity). This is a genuinely different formulation
of the same crux — expressed here via witness-pigeonhole rather than via
antichain/intersecting-family language — not a resolution.

### Cases to cover (partial resolution)
- **|Q| = 1** (a_1 a prime power): 𝒫 = {Q} is the only possible type (τ(n) ⊇ Q always
  by Free Facts, and τ(n) ⊆ Q, so τ(n) = Q for all n ≥ 1). There are no two disjoint
  persistent types, so (†) is vacuously true and gap-free in this case: S = ∅ works
  (the Finite Core Theorem's set is empty since 𝒫 has no pair of disjoint types to
  reconcile), and the CRT + cyclic-pigeonhole finish (below) applies directly with
  L = a_1 itself (Q's product), no open gap remains here.
  *Verification finish for this case:* with L = the product of primes of Q (so that
  Q | L), Lemma A already gives a_{n+1} ≤ (next multiple of L exceeding a_n) for every
  n; and since every integer coprime to none of a_1's prime factors that is a multiple
  of some prime of Q is automatically legal by Free Facts + Lemma A's mechanism, one
  checks directly (by finite exhaustive comparison over residues mod L, since L is
  explicit) that the greedy choice is in fact always exactly the smallest legal
  candidate, which cycles with period T := (number of legal residues mod L) once n
  exceeds the point where τ(n) stabilizes to Q (i.e. from n = 1 itself when |Q| = 1,
  since Free Facts already forces τ(n) = Q always). This sub-case is fully resolved with
  no open gap and no dependence on (†), but is a narrow special case (it does not by
  itself give the full problem, since |Q| ≥ 2 remains open).
- **|Q| ≥ 2 with two or more persistent types**: gap (†) remains open, per the analysis
  above; Lemmas B and C provide new but insufficient structural information.

### Key lemmas (summary)
- Free Facts, Bounded Gap Lemma, Persistent-Type Pigeonhole, Bounded Witness Lemma,
  Finite Core Theorem — imported unchanged, certified, no gaps.
- **Lemma A (Generalized Bounded Gap fact)** — new, proved in full above, unconditional.
- **Lemma B (Single-Witness-Prime Pigeonhole Refinement)** — new, proved in full above,
  unconditional; strengthens Bounded Witness Lemma but does not by itself close (†).
- **Lemma C (Extended Persistent-Type Pigeonhole)** — new, proved in full above,
  unconditional; sets up the correct finite state space 2^{S_0} for the eventual
  CRT + cyclic-pigeonhole finish, but does not by itself determine which subsets of
  S_0 the extended-persistent types 𝒫' actually are, nor whether disjoint-base-type
  pairs among them intersect in S — that is (†).
- **|Q| = 1 case** — fully resolved (no gap), a genuinely complete sub-case of the
  problem, recorded above.

### Open gaps
- Gap (†) itself (do disjoint-base-type extended-persistent types necessarily share an
  S-prime), for |Q| ≥ 2 — NOT closed by this approach. The attempted upgrade of the
  Single-Witness-Prime Pigeonhole Refinement to the extended-type level stalls exactly
  where an arbitrary (non-canonical) witness's full factorization can carry primes
  outside the fixed finite core S_0, with no certified control over this.
- The n = 1 boundary extension (same as all sibling approaches): even conditional on
  (†) being resolved and periodicity established for n beyond some threshold, extending
  a_{n+T} = a_n + L back to n = 1 is not attempted here.

### Retracted claims (do not re-attempt as stated)
- "cost(n) := |P(a_n)\Q| ≤ |𝒫| - 1 eventually" — retracted in the round-2 draft (does
  not follow from the Finite Core Theorem, which only guarantees existence of some
  shared S-prime per disjoint type, not a bound on total distinct extra primes).
- "cost(n) ≤ 1 eventually when Q is 'sparse' (misses a small prime)" — **retracted this
  round, refuted by explicit counterexample** (a_1 = 35: Q = {5,7} sparse by this
  definition, yet the true core needs 2 extra primes {2,3}, and individual terms like
  a_153 = 975 have cost 2 with a THIRD incidental prime 13 as well). The sparse/dense
  dichotomy based on Q's content is not the right variable; the number of extra primes
  eventually needed does not correlate with whether Q contains small primes. No future
  builder of this approach should attempt to prove either retracted claim.

### ROUND 3: importing the Canonical-Refinement and F_{A,B}∩F_{B,A} lemmas, restated in
cost/witness language, and the "rogue refinement skippable" exchange attempt

This round imports two lemmas found by this round's explorers (certified via the sibling
`covering-system-construction` approach's Step 4d/4e) and restates them here in this
approach's own witness-prime vocabulary (rather than citing them as a black box), then
carries out the "rogue refinement must be skippable" exchange attempt sketched by the
outliner. **Conclusion in advance, stated honestly: the exchange attempt does NOT close
the residual gap; it identifies a precise structural reason (greedy minimality controls
only magnitude, not extended type) why the proposed mechanism cannot work as stated, and
this is recorded below rather than smoothed over.**

#### Restating the imports in this approach's own notation

Recall the notation already fixed above: for B ∈ 𝒫 with canonical witness m_B (the
Finite Core Theorem's fixed choice), write **F_B := P(a_{m_B}) \ Q** (dropping the
partner-type subscript, since — as shown below — this set does not actually depend on
which disjoint partner A it is used against; the two-index notation F_{A,B} used in the
Bounded Witness Lemma's statement was only ever a labeling convenience). Write
**B_can := B ∪ F_B = ρ(m_B)** for the canonical extended refinement of B (i.e. the
extended type actually realized by the fixed canonical witness itself).

**Restated Lemma D (Canonical-Refinement Lemma, in cost language).** Let A, B ∈ 𝒫 be
disjoint persistent base types. Then:
(i) B_can = B ∪ F_B *exactly* (not merely ⊇), and
(ii) every extended-persistent refinement A' of A (A' ∩ Q = A, A' ∈ 𝒫') satisfies
A' ∩ B_can ≠ ∅ — in fact A' ∩ F_B ≠ ∅, a strictly sharper statement since B_can ⊇ F_B.

*Proof.*
(i) By definition ρ(m_B) = P(a_{m_B}) ∩ S₀ where S₀ = Q ∪ S. Split the intersection:
P(a_{m_B}) ∩ S₀ = (P(a_{m_B}) ∩ Q) ∪ (P(a_{m_B}) ∩ S) = τ(m_B) ∪ (P(a_{m_B}) ∩ S) = B ∪
(P(a_{m_B}) ∩ S), using τ(m_B) = B by construction of the canonical witness. Now
P(a_{m_B}) \ Q ⊆ S by the very definition S := ⋃_{B'∈𝒫}(P(a_{m_B'})\Q) (a union that
includes the B-term of this union). Hence P(a_{m_B}) ∩ S ⊇ P(a_{m_B}) \ Q, and since
S ∩ P(a_{m_B}) ⊆ P(a_{m_B}) and every prime of S ∩ P(a_{m_B}) is either in Q or not — if
it is in Q it already counts inside the B-term above, so restricting to primes outside Q
gives exactly P(a_{m_B}) ∩ S \ Q = P(a_{m_B}) \ Q = F_B. So P(a_{m_B}) ∩ S = F_B exactly
(no prime of S ∩ P(a_{m_B}) is lost, and no prime is added, since S ∩ P(a_{m_B}) ⊆
P(a_{m_B}), and every prime of P(a_{m_B}) is either in Q, contributing to B, or outside
Q, in which case it is automatically in F_B ⊆ S so it survives the ∩ S). Thus ρ(m_B) =
B ∪ F_B = B_can, with equality (not just ⊇), as claimed.

(ii) Fix any n > N_2 with ρ(n) = A' (exists since A' ∈ 𝒫' is extended-persistent). Since
A' ∩ Q = A, in particular τ(n) = A. Since n and m_B both exceed N_1 (enlarging N_2 if
needed to also exceed N_1, which only removes finitely many more indices, harmless since
A' still occurs infinitely often), and B is disjoint from τ(n) = A, the certified Bounded
Witness Lemma (with witness m = m_B, valid since τ(m_B) = B) gives: a_n is divisible by
some prime p ∈ F_{A,B} = P(a_{m_B}) \ Q = F_B. Since p | a_n, p ∈ P(a_n); since p ∈ F_B ⊆
S ⊆ S₀, also p ∈ S₀; hence p ∈ P(a_n) ∩ S₀ = ρ(n) = A'. So p ∈ A' ∩ F_B, proving
A' ∩ F_B ≠ ∅, and a fortiori A' ∩ B_can ⊇ A' ∩ F_B ≠ ∅. ∎

Note explicitly what (ii) does NOT say: it does not say A' meets an arbitrary
non-canonical extended-persistent refinement B' ≠ B_can of B — only the one specific
canonical refinement B_can. This is the exact boundary of what the lemma proves.

**Restated Lemma E (F_A ∩ F_B ≠ ∅, in cost language).** For disjoint persistent base
types A, B ∈ 𝒫, F_A ∩ F_B ≠ ∅ (equivalently B_can ∩ A_can ⊇ F_A ∩ F_B ≠ ∅, so the two
CANONICAL refinements always intersect each other, consistent with (ii) applied twice).

*Proof.* By the Free Facts lemma, gcd(a_{m_A}, a_{m_B}) > 1, so some prime p divides
both a_{m_A} and a_{m_B}. If p ∈ Q, then p ∈ τ(m_A) ∩ τ(m_B) = A ∩ B = ∅ (disjoint base
types), contradiction. So p ∉ Q, hence p ∈ P(a_{m_A}) \ Q = F_A and p ∈ P(a_{m_B}) \ Q =
F_B, giving p ∈ F_A ∩ F_B. ∎

Both restatements are verified independently here (not merely copied): the proofs above
are self-contained, using only the certified Free Facts lemma, Bounded Witness Lemma,
and Finite Core Theorem, matching the mechanism attributed to `covering-system-
construction`'s Step 4d/4e and the outline's claims. **Both are correct as stated and
are genuinely not sufficient to close (†)** — as (ii)'s note above makes explicit, they
only ever pin one side of a pair to be the CANONICAL refinement.

**Sharply localized residual (restated in this approach's own terms).** Combining (ii)
with its A↔B mirror image: gap (†) is now needed only for pairs of extended-persistent
types A', B' ∈ 𝒫' with disjoint base types A = A'∩Q, B = B'∩Q, where **A' ≠ A_can AND
B' ≠ B_can simultaneously** (if either side equals its base type's canonical refinement,
(ii) already forces the intersection). Call such a pair a **rogue pair**.

#### The "rogue refinement must be skippable" exchange attempt

The proposed mechanism (outliner's sketch, Closure explorer's Opening 3): if A' is a
non-canonical extended-persistent refinement of A that fails to intersect some disjoint
persistent partner's extended type B', then infinitely many terms of extended type A'
occur; at each such occurrence n, greedy minimality (a_n is by definition the SMALLEST
integer exceeding a_{n-1} legal against every a_1,...,a_{n-1}) should have preferred a
smaller candidate of "safer" (canonical, reconciling) type, if one were available and
legal — and the claim to attempt is that such a smaller legal candidate is ALWAYS
available, contradicting the actual choice of a_n having the rogue type A'.

**Attempt.** Fix a rogue pair (A', B') and n > N_2 with ρ(n) = A' (infinitely many
exist). We seek to construct an explicit legal candidate c with a_{n-1} < c < a_n whose
existence would contradict minimality of a_n (i.e., c is legal against a_1,...,a_{n-1}
but smaller than the actual a_n — impossible since a_n is chosen minimal).

By the certified Generalized Bounded Gap Lemma (Lemma A above), fixing any single prime
q ∈ F_B and setting c₀ := (the smallest multiple of a_1·q exceeding a_{n-1}), Lemma A's
proof shows c₀ is legal against every a_1,...,a_{n-1} (indeed against a_1,...,a_{n} and
beyond, by the identical argument, since it only used gcd(a_i,a_1)>1 for i ≥ 2 together
with q | c₀), and c₀ ≤ a_{n-1} + a_1·q. This c₀ *is* a legal candidate exceeding a_{n-1}
and, being a multiple of a_1, has type τ = Q ⊇ A ∪ B entirely (the "maximally safe"
type), so ρ(c₀) ⊇ A_can ∪ B_can trivially reconciles with everything. **But this does
NOT give the needed contradiction**, for two independent reasons, both genuine
obstructions and not merely presentational:

1. **c₀ need not be smaller than a_n.** Lemma A only bounds a_n ≤ a_{n-1} + a_1·a_{...}
   from ABOVE; it gives no lower bound on a_n forcing a_n > c₀. If a_n < c₀ (which is the
   generic case — greedy minimality means the ACTUAL smallest legal integer is typically
   much smaller than the "safe" multiple-of-a_1 candidate, since legality against each
   a_i only needs ONE shared prime with EACH a_i individually, a far weaker requirement
   than being divisible by an entire prescribed prime), then c₀ is not a competitor at
   all — it is larger than a_n, so minimality of a_n says nothing about it, and there is
   no contradiction to derive. The a_1=35 data illustrates this concretely: the
   rogue-looking recurring type {5} with terms like a_153 = 975 = 3·5²·13 is (by
   definition of greedy) smaller than every other legal candidate at that step,
   including any "safe" multiple of a_1 = 35 exceeding a_152 — the existence of a safe
   candidate FURTHER OUT does not contradict a_153 being chosen, precisely because a_153
   is smaller.

2. **Even restricting to candidates strictly between a_{n-1} and a_n (there could be
   none), there is no certified way to show one of them has canonical-reconciling
   type.** The only handle available (Lemma A / Generalized Bounded Gap Lemma) produces
   candidates of the "maximally safe" type Q-multiple, whose gap from a_{n-1} is
   O(a_1 · q), generally far larger than the actual gap a_n − a_{n-1} (which the Bounded
   Gap Lemma only bounds by a_1, not by a finer quantity tied to reconciliation). There
   is no certified finer construction here (or anywhere in the certified lemma set) of a
   *smaller* safe candidate, i.e. one closer to a_{n-1} than a_n, with a controlled
   extended type. Constructing one would amount to a completely different argument, not
   an application of the currently certified lemmas.

**Diagnosis (the precise structural reason the mechanism fails, stated as a lemma so it
is not silently re-attempted).**

**Lemma F (Minimality bounds magnitude, not type).** The certified Generalized Bounded
Gap Lemma (Lemma A) and Bounded Gap Lemma bound a_{n+1} from ABOVE in terms of a_n and a
chosen modulus; neither they, nor any other lemma certified in this workspace, bound
a_{n+1} from BELOW in a way that constrains its extended type ρ(n+1). Consequently,
"a_n is the smallest legal successor" is a purely magnitude-based extremal condition: it
guarantees no smaller integer is legal, but places no constraint on which primes outside
Q the actual smallest legal integer happens to carry (Free Facts only forces, for each
i < n, that a_n share SOME prime with a_i — possibly a different, uncontrolled prime for
each i, and in particular possibly none of them lying in the fixed core S₀ at all,
consistent with the a_1 = 35 data where a_153 carries the load-bearing prime 3 alongside
the wholly incidental prime 13). Hence no exchange/skippability argument built solely
from an upper-bound gap lemma (Lemma A or the Bounded Gap Lemma) can force a_n to avoid a
rogue extended type, because such an argument would need a competing candidate that is
BOTH smaller than a_n AND of safe type — and the certified lemmas only ever produce safe
candidates that are large (multiples of a full modulus c ≥ a_1), not small ones.

*Proof.* Immediate from inspecting the two certified magnitude lemmas (Bounded Gap
Lemma, Generalized Bounded Gap Lemma): both proofs (see `lemmas/bounded-gap-lemma.md`
and Lemma A above) construct their legal candidate as "the smallest multiple of a fixed
modulus c exceeding a_n," a quantity with no freedom to be made small relative to a_n
other than via c itself, and c is bounded below by a_1 (any modulus divisible by every
prime of Q is a multiple of the LCM of Q's primes, which is ≥ the smallest prime of Q,
generally comparable to or larger than a_1's own scale) — so the constructed safe
candidate's gap from a_n is Θ(c) = Θ(a_1) or larger, not asymptotically smaller. No
certified lemma produces a legal candidate of controlled (safe) type at a gap smaller
than this. ∎

This is a genuine (if negative) structural finding: it explains, in a way consistent
with and sharpening the earlier retraction of the "cost(n) ≤ 1" conjecture, why *any*
future attempt in this approach's vocabulary to force rogue types to be "skipped" by
minimality must fail unless it first exhibits a SMALL safe candidate (gap o(a_1) or
better, ideally O(1)) — which no lemma here constructs, and which is not obviously
achievable, since Free Facts alone gives no control over which primes reconcile a
candidate with each individual earlier term.

**Conclusion of the round-3 attempt, stated honestly.** The exchange/minimality
mechanism suggested by the outliner does not close the rogue-pair residual of gap (†).
The obstruction is not a missing computation but a structural mismatch: the certified
toolkit (Free Facts, Bounded Gap Lemma, Generalized Bounded Gap Lemma) only ever
produces upper bounds on a_{n+1}'s magnitude via LARGE safe candidates, while the
mechanism needs a SMALL safe candidate to compete with the actual (smaller) rogue
choice — a fundamentally different and currently unavailable kind of lemma. This
mirrors, at a structural level, why the earlier "cost(n) ≤ 1" and "cost(n) ≤ |𝒫|-1"
conjectures failed: minimality/greediness in this problem controls size, not prime
content, and every attempt (this round's exchange idea included) to leverage minimality
to control prime content runs into the same wall.

### ROUND 4: the rescoped Round Resolution Lemma (pair-local, not whole-base-type),
Lemma G, and an honest report on where the first-bad-round induction stalls

**Mandatory rescoping (per outline-reviewer instruction).** The outliner's original
Round Resolution Lemma claimed a recruited prime q "permanently resolves the WHOLE
base-type pair (A,B)" — i.e. q divides every sufficiently large term of BASE type A
(all its extended refinements at once), not merely the specific witnessed
extended-persistent type A'_0 that triggered the recruitment. This is **falsified**
by the outline-reviewer's direct computation on a_1 = 175: the recruited prime 13
divides only ≈14% of ALL base-type-{7} occurrences (176/1226) and ≈14% of ALL
base-type-{5} occurrences (132/920), including in the confirmed-periodic tail. I
independently re-ran this exact check this round (see below) and confirm the
figures. **This approach does NOT reattempt the whole-base-type claim.** The target
proved in this section is the correctly rescoped, pair-local version: q resolves the
*specific* extended-persistent types A'_0, B'_0 that triggered the recruitment (not
their whole base types), and even this is established only *conditionally*, with the
residual hypothesis stated honestly (not smuggled in) and the search for a proof of
that hypothesis reported as a genuine, precisely-located stall.

**Independent verification of the falsifying data (this round).** Reproduced via
direct simulation (trial-division factorization, `gen_seq`/`P` as in prior rounds,
4000-6000 terms): for a_1 = 175, S₀ = {2,3,5,7,11,29,41,67} (Finite Core Theorem's
one-round pool), the recruitment process run on this S₀ finds a rogue pair
A'_0 = {3,5,11}, B'_0 = {2,7} at round 0, with earliest-witness computation giving a
SINGLE recruited prime q = 13 (F' = P(a_{m}) \ S₀ = {13} for the earliest witness m
of B'_0's canonical realization) that resolves ALL SIX rogue pairs present at round 0
simultaneously (not just the one witnessed pair — a strictly stronger empirical
phenomenon than what this round's Lemma below proves), and the recruitment process
halts after exactly 1 round. Restricting the check to the two specific rogue types
{2,7} and {3,5} (rather than the whole base types {7},{5}), 13 divides **every**
occurrence of both, 100% (97/97 and 72/72 respectively over the full 6000-term
window, and 100% even restricted to indices before the tail, from the first
occurrence: {2,7} first occurs at n=3, {3,5} first occurs at n=5) — confirming the
outline-reviewer's rescoped, narrower target is what the data actually supports, and
the broad base-type version is not.

#### New Lemma G (Extended Earliest-Witness Intersection)

**Statement.** Let S₀ ⊇ Q be any fixed finite set of primes, ρ(n) := P(a_n) ∩ S₀, and
let A', B' ⊆ S₀ be two S₀-extended-persistent types (each occurring for infinitely
many n) with A' ∩ B' = ∅. Let n_A := min{n : ρ(n) = A'} and n_B := min{n : ρ(n) = B'}
(both exist and are finite, since A', B' each occur at least once). Then there is a
prime q ∉ S₀ with q | a_{n_A} and q | a_{n_B} simultaneously.

*Proof.* Since n_A ≠ n_B (ρ(n_A) = A' ≠ B' = ρ(n_B), as A' ∩ B' = ∅ and both are
nonempty — nonempty because they are S₀-extended-persistent hence occur at all, and
an occurring ρ-type is P(a_n) ∩ S₀ which could in principle be empty only if a_n
shares no prime with S₀, but Free Facts already forces P(a_n) ∩ Q ≠ ∅ for n ≥ 2 and
Q ⊆ S₀, and n_A, n_B ≥ 1; if n_A = 1 or n_B = 1 the same holds since Q = P(a_1) ⊆ S₀
trivially gives ρ(1) ⊇ Q ≠ ∅ — so both A', B' are nonempty and distinct, giving
n_A ≠ n_B), the Free Facts lemma (`lemmas/free-facts-gcd.md`, certified) applies:
gcd(a_{n_A}, a_{n_B}) > 1, so some prime p divides both a_{n_A} and a_{n_B}. If
p ∈ S₀, then p ∈ P(a_{n_A}) ∩ S₀ = ρ(n_A) = A' and p ∈ P(a_{n_B}) ∩ S₀ = ρ(n_B) = B',
so p ∈ A' ∩ B' = ∅, a contradiction. Hence p ∉ S₀. Set q := p. ∎

This is proved completely and unconditionally from the certified Free Facts lemma
alone; it strictly generalizes the certified F_A∩F_B≠∅ lemma (Lemma E /
`lemmas/canonical-witness-intersection.md`) from the base-type canonical-witness
setting to arbitrary S₀-extended-persistent types using their own earliest
occurrences (a genuinely different, and for the purposes of this round's target,
more directly useful, pair of witness indices than the Finite Core Theorem's
canonical witnesses). **Promotable.**

#### The rescoped Round Resolution Lemma (conditional, hypothesis stated explicitly)

**Statement.** Let S₀ ⊇ Q be a fixed finite set of primes, ρ, 𝒫' as above, and let
A'_0, B'_0 ∈ 𝒫' be a rogue pair (disjoint-base-type, S₀-disjoint extended-persistent
types, i.e. a member of V, using n_A := min{n:ρ(n)=A'_0}, n_B := min{n:ρ(n)=B'_0} as
in Lemma G, WLOG n_A < n_B). Let F' := P(a_{n_B}) \ S₀ and F'' := P(a_{n_A}) \ S₀ (both
finite, nonempty by Lemma G — in fact Lemma G's q lies in both). **Assume the
Singleton Hypothesis for this pair: |F'| = 1 (equivalently F' = {q} for the q of
Lemma G, since q ∈ F' always by Lemma G's proof).** Then:
(i) q divides a_n for EVERY n > n_B with ρ(n) = A'_0 (not merely infinitely many);
(ii) consequently, at the refined level S₀^{(1)} := S₀ ∪ {q}, every occurrence of
A'_0 with index > n_B has ρ_1-signature exactly A'_0 ∪ {q}, so A'_0 ∪ {q} is itself
S₀^{(1)}-extended-persistent and no other S₀^{(1)}-refinement of A'_0 is persistent
using index range n > n_B (finitely many indices n_A ≤ ... ≤ n_B remain
un-analyzed, a finite exceptional set); and
(iii) A'_0 ∪ {q} and B'_0 (in its own S₀^{(1)}-refined form, which by construction of
q and Lemma G already contains q at index n_B, hence one persistent refinement of
B'_0 is B'_0 ∪ {q}) intersect via q — the specific witnessed instance is resolved.

*Proof.* (i) By the certified Generalized Bounded Witness Lemma
(`lemmas/generalized-bounded-witness-lemma.md`), using S₀, the two S₀-disjoint types
A'_0, B'_0 (A'_0∩B'_0=∅, since it's a rogue pair), and witness m = n_B (ρ(n_B)=B'_0):
for every n > n_B with ρ(n) = A'_0, a_n is divisible by some prime of
F'_{A'_0,B'_0} = P(a_{n_B}) \ S₀ = F'. By the Singleton Hypothesis, F' = {q}, so this
disjunction has exactly one disjunct: a_n is divisible by q. This holds for every
such n, not merely infinitely many, since the Generalized Bounded Witness Lemma's
own conclusion already quantifies over every n > m, not just an infinite subset (the
"infinitely many" language belongs only to the Corollary's separate pigeonhole
extraction, which is not invoked here — this proof uses the Lemma directly). (ii)
Immediate from (i): for n > n_B with ρ(n) = A'_0, ρ_1(n) = P(a_n) ∩ S₀^{(1)} =
(P(a_n)∩S₀) ∪ (P(a_n)∩{q}) = A'_0 ∪ {q} (using q | a_n from (i)). Since infinitely
many such n exist (A'_0 is S₀-extended-persistent), A'_0 ∪ {q} occurs infinitely
often at level S₀^{(1)}, i.e. is S₀^{(1)}-extended-persistent; and every n > n_B with
ρ(n) = A'_0 has ρ_1(n) = A'_0∪{q} exactly (no other refinement occurs for n > n_B),
so any other S₀^{(1)}-refinement of A'_0 that is extended-persistent would have to
draw all but finitely many of its occurrences from indices ≤ n_B, a finite set —
impossible for an infinite persistent type. Hence A'_0 ∪ {q} is the UNIQUE
S₀^{(1)}-extended-persistent refinement of A'_0, modulo the finite exceptional
prefix n ≤ n_B. (iii) q | a_{n_B} by Lemma G, so ρ_1(n_B) = B'_0 ∪ {q}; and
(A'_0∪{q}) ∩ (B'_0∪{q}) ⊇ {q} ≠ ∅. ∎

**What this proves and what it does not, stated with no gap smoothed over.** This is
a complete, gap-free proof of the rescoped target CONDITIONAL on the Singleton
Hypothesis |F'| = 1 for the specific pair. It is strictly narrower than both (a) the
outline's original whole-base-type claim (correctly retracted, falsified) and (b) an
unconditional pair-local claim (which I could not establish — see below). The
Singleton Hypothesis is a purely numerical fact about ONE fixed integer's
factorization (ω(a_{n_B}) restricted to primes outside S₀ equals 1) — it is not a
statement quantified over an infinite family, and no certified lemma in this
workspace (all of which are built from Free Facts' pairwise-gcd plus the infinite
pigeonhole principle) bounds the number of prime factors of a single fixed integer
outside a fixed finite set. Free Facts gives existence of a shared prime (≥1), never
an upper bound (=1).

#### Attempting the directed first-bad-round / time-ordered minimality induction to
remove the Singleton Hypothesis — genuinely stalls, documented precisely

Following the dispatch's instruction (model on aimo-0514/aimo-0077: "assume the
process never halts, take the FIRST bad event, contradict via what must already be
true one step earlier"), I attempted to organize a minimality induction on the
recruitment process's round index k to either (a) prove the Singleton Hypothesis
always holds at the round where a genuine rogue pair is first recruited against, or
(b) bypass it by finding a substitute argument that gets propagation to BOTH sides
without needing |F'| = 1.

**Attempt.** Suppose, for contradiction, that the recruitment process (as defined in
`covering-system-construction`'s Step 4c, reused here unconditionally) runs forever,
i.e. V ≠ ∅ at every stage S₀^{(k)}, k = 0, 1, 2, .... Let k* be the FIRST round (if
any) at which the round's chosen rogue pair (A'_0, B'_0) fails the Singleton
Hypothesis (|F'_{A'_0,B'_0}| ≥ 2, computed via the earliest-witness pair of Lemma G
at that round). The natural hope, mirroring aimo-0514/aimo-0077's structure, is to
use minimality of k* (every earlier round k < k* had a singleton, hence — by the
Lemma above — is FULLY resolved by round k*, in the strong sense that the recruited
prime at each earlier round uniquely pins down that round's A'-refinement per (ii))
to constrain the round-k* witnesses' factorizations. **This is exactly where the
attempt stalls, for a structural reason, not a missing computation:**

The quantity being minimized over rounds — |F'_{A'_0,B'_0}| at round k*, i.e. the
number of primes outside S₀^{(k*)} dividing ONE FIXED INTEGER a_{n_B} (the earliest
witness of B'_0 at that round) — is a static factorization fact about a_{n_B}, fully
determined the moment a_{n_B} is written down; it does not evolve or get constrained
by the outcome of EARLIER recruitment rounds in any way the certified toolkit
exposes. Earlier rounds' successful singleton resolutions (rounds < k*) only ever
tell us about DIFFERENT witness integers a_{n_B'} for DIFFERENT rogue pairs at
DIFFERENT (smaller) S₀-levels — there is no certified relation between the
factorization of one witness integer and another's, beyond the generic pairwise-gcd
fact (Free Facts), which only ever produces a LOWER bound (≥1 shared prime) on an
intersection, never an upper bound on a single integer's total factor count. Unlike
the aimo-0514/aimo-0077 crux (where the minimal bad event's index directly appears
inside an earlier, already-established relation via the recursive structure of the
process being analyzed — e.g., a cycle in a functional graph, where the "one step
earlier" state is literally determined by the process itself), this problem's
witness integers a_{n_B} at successive rounds are not related by any recursive
formula the certified lemmas expose: each a_{n_B} is just "the value of the greedy
sequence at some particular later index," and greedy minimality (per the
already-proved Lemma F, "Minimality bounds magnitude, not type," round 3) controls
only the SIZE of a_n relative to earlier terms, never which primes divide it beyond
guaranteeing at least one shared prime per earlier term. So there is no lever here
for a minimality argument to pull: reducing k* to "the first failure" produces no
new information about a_{n_B}'s factorization at round k*, because nothing about
ROUND k* is a numerical/size quantity that a well-ordering on k could organize
against a competing smaller object — it is a divisibility-count fact about one
integer, structurally disconnected from the round index.

**Secondary attempt: bypass the Singleton Hypothesis by using ALL of F' at once, not
just one prime.** If |F'_{A'_0,B'_0}| = r ≥ 2, one could try recruiting the ENTIRE
set F' (not just one prime) into S₀^{(k+1)} at once, hoping that the r-fold
refinement of A'_0 by all of F' simultaneously still resolves the specific rogue
pair. This does not obviously work either: the Generalized Bounded Witness Lemma
only guarantees each n > n_B with ρ(n) = A'_0 is divisible by SOME (possibly
different, occurrence-dependent) prime of F' — so refining by the whole set F' can
split A'_0 into as many as 2^r − 1 distinct new S₀^{(k+1)}-extended-persistent
sub-types (one for each nonempty subset of F' realized by at least one occurrence,
by the same finite-pigeonhole mechanism as the Persistent-Type Pigeonhole /
Extended Persistent-Type Pigeonhole, certified, applied to F' as the new refining
set), and there is no certified guarantee that EVERY one of these sub-types still
carries q or any other single prime shared with a B'_0-refinement — this simply
re-poses the identical rogue-pair question one level further down (now among the up
to 2^r − 1 refinements of A'_0 versus B'_0's own refinements), not a resolution of
it. I record this as a genuinely explored, honestly failed bypass, not a
computation I omitted.

**Conclusion of the round-4 attempt, stated without overclaiming.** The rescoped
Round Resolution Lemma (pair-local, not whole-base-type, matching the
outline-reviewer's correction) is proved here **completely and rigorously,
conditional on an explicit, isolated numerical hypothesis** (|F'_{A'_0,B'_0}| = 1
for the specific earliest-witness pair of the rogue instance) that I verified
computationally in every rogue-pair instance found across ~20 tested seeds
(a_1 = 175, 187, 209, 247, 385, and re-verified the two-round case a_1 = 247 where
BOTH successive rounds' witnesses independently satisfy the Singleton Hypothesis:
round 0 recruits q=5 with F'={5}, round 1 recruits q=7 with F'={7}, each with 100%
coverage on both the A'- and B'-sides from the earliest occurrence) but did NOT
prove in general. The directed first-bad-round/time-ordered minimality induction
does not close this hypothesis: I identified the precise structural reason
(the Singleton Hypothesis is a static factorization fact about one fixed integer,
not a quantity organized by the recruitment process's round order, so there is no
"earlier round" data for a minimality argument to leverage against it — unlike the
aimo-0514/aimo-0077 crux, where the minimal bad event's defining quantity IS
recursively tied to the process's own prior states).

#### Honest answer to the dispatch's scope question: sufficient for termination, or
only one pair at a time?

**Even granting the Singleton Hypothesis in full generality (i.e., treating it as
an additional unproved but assumed axiom), the rescoped Round Resolution Lemma by
itself does NOT give a global bound on the total number of recruitment rounds, for
two independent reasons, both worth recording precisely:**

1. **It resolves only the ONE witnessed instance, not the whole base-type pair (by
   design — the whole-base-type claim is exactly what was falsified and retracted).**
   Since a base-type pair (A,B) can have many disjoint extended-persistent
   refinement-pairs (A'_1,B'_1), (A'_2,B'_2), ..., resolving one such pair at one
   round says nothing about whether OTHER refinement-pairs of the SAME base types
   remain rogue and need FURTHER, separate rounds. `covering-system-construction`'s
   Step 4c already flagged exactly this gap ("I was not able to show a single
   round's recruitment fully settles a whole base-type pair... requiring further
   rounds restricted to that same base pair") — the rescoping in this round's
   dispatch confirms that gap is real (the whole-pair version is false, not just
   unproved) and this round's Lemma does not close it: proving termination would
   still require either (a) a SEPARATE argument bounding, for each of the finitely
   many (≤ C(|𝒫|,2)) base-type pairs, the number of DISTINCT refinement-pairs that
   can ever be rogue simultaneously or successively (not attempted here), or (b) an
   empirical fact (observed in every tested seed: one recruited prime resolves ALL
   currently-rogue pairs at once, not just the witnessed one — see the a_1=175 data
   above, six rogue pairs resolved by a single q=13) elevated to a proved lemma,
   which is a strictly stronger and different claim than the rescoped Round
   Resolution Lemma proved here, and which I did not attempt to prove (it does not
   obviously follow from Lemma G or the Generalized Bounded Witness Lemma applied
   to a single pair — it would require a joint argument across ALL simultaneously-
   rogue pairs at a given round, structurally the same "joint/simultaneous" gap this
   round's explorers flagged as still missing).
2. **Even resolving every currently-existing rogue pair at a round does not rule out
   NEW rogue pairs appearing as a side effect of the refinement itself** (S₀ grows
   every round, so previously-non-rogue extended-persistent types can split into
   finer sub-types, some of which could in principle newly violate disjoint-base-
   type intersection against types unaffected by the current round's recruitment).
   No lemma in this workspace (certified or proved here) rules this out; it was not
   observed in any tested seed (violations strictly decreased every round in all
   ~20 seeds checked) but this is empirical, not proved.

**Honest verdict on the dispatch's question:** the rescoped Round Resolution Lemma,
even if its Singleton Hypothesis were established in full generality, is **NOT by
itself sufficient to close gap (†)** — it resolves one witnessed pair at a time,
with no proved bound on how many rounds (or how many pairs per round) are needed in
total, and no proved guarantee against new violations arising from refinement. A
global termination proof would need at least one further ingredient beyond this
lemma: either the stronger "one round resolves ALL currently-rogue pairs
simultaneously" fact (empirically 100% supported across every tested seed but
entirely unproved) or a separate finite bound on refinements-per-base-pair. This is
recorded honestly as the next open target, not smoothed into a false "sufficient"
claim.

### ROUND 5: attempting the Singleton Hypothesis in general via minimality of the
earliest-occurrence index — a new, fully proved, unconditional dichotomy (Lemma H),
honestly shown insufficient to finish the proof

**Governing correction carried over from this round's outline-reviewer (independently
re-verified by that reviewer, not re-litigated here).** Round 4's "V = ∅ always with
minimal witnesses" is retracted again — genuinely, this time, not a repeat of the
round-3/4 witness-selection bug. Four fresh, independently double-checked
counterexamples (a_1 = 187, 209, 247, 385) each show a genuine rogue pair resolved by
exactly one recruitment round with a Singleton F′. This round's task, per the dispatch,
is to attempt the Singleton Hypothesis (|F′| = 1 at a rogue-pair witness) as a GENERAL
theorem, via minimality of the earliest occurrence of the extended-persistent type
carrying the witness — not more small-sample numerical checking.

#### Restating the target precisely

Fix any finite S₀ ⊇ Q at any stage of the recruitment process, and a rogue pair (A′,
B′) of S₀-extended-persistent types with disjoint base types, A′ ∩ B′ = ∅. By the
certified **Lemma G** (Extended Earliest-Witness Intersection,
`lemmas/extended-earliest-witness-intersection.md`), writing n_A := min{n : ρ(n)=A′},
n_B := min{n : ρ(n)=B′} (WLOG n_A < n_B by relabeling — the two cases n_A<n_B and
n_B<n_A are symmetric under swapping the names A′↔B′, so no separate casework is lost
by fixing this WLOG), there is a prime q ∉ S₀ with q | a_{n_A} and q | a_{n_B}. Define
**F′ := P(a_{n_B}) \ S₀** (the full set of primes outside S₀ dividing the LATER
witness's value; q ∈ F′ always, by Lemma G's own proof). The **Singleton Hypothesis**
is the claim |F′| = 1 for every such rogue-pair witness. This is exactly the residual
hypothesis of the certified (conditional) Round Resolution Lemma from round 4.

#### The attempted mechanism (per dispatch): exploit minimality of n_B as an INDEX

The dispatch's proposed mechanism is to use that n_B is the *earliest* index realizing
extended type B′ — not merely that a_{n_B} is the smallest legal successor of
a_{n_B−1} (that per-step magnitude minimality was already exhausted by the certified,
proved-insufficient **Lemma F**, "minimality bounds magnitude, not type," round 3).
Carrying this out rigorously (not the loose sketch in the outline) gives the following
genuinely new, fully proved lemma.

**Lemma H (Critical Prime Dichotomy).** Let n ≥ 2 be any index, and let q′ be any
prime with q′ | a_n and q′ ∉ S₀ (S₀ any fixed finite set of primes with Q ⊆ S₀). Let
e := v_{q′}(a_n) ≥ 1 (the exact power of q′ dividing a_n) and define c := a_n / q′^e
(a positive integer, since q′^e | a_n by definition of e). Then exactly one of the
following holds:
(a) c ≤ a_{n−1} (the candidate obtained by stripping every copy of q′ from a_n does not
exceed the previous term), or
(b) there is an index i ∈ {1, ..., n−1} such that P(a_i) ∩ P(a_n) = {q′} exactly — i.e.
a_i and a_n share EXACTLY the single prime q′ and no other common prime factor.

*Proof.* Write a_n = q′^e · c with gcd(c, q′) = 1 by definition of e; hence
P(c) = P(a_n) \ {q′} (c retains every OTHER prime factor of a_n with its original
multiplicity, since only the q′-part was removed, and c is coprime to q′ by
construction). In particular c < a_n (as q′^e ≥ 2).

Suppose (a) fails, i.e. c > a_{n−1}. Then c is an integer strictly between a_{n−1} and
a_n. By the problem's defining greedy rule, a_n is literally the SMALLEST integer
exceeding a_{n−1} with gcd(a_n, a_i) > 1 for every i = 1, ..., n−1; since c < a_n and
c > a_{n−1}, minimality of a_n forces c to be ILLEGAL, i.e. there exists some index
i ∈ {1,...,n−1} with gcd(c, a_i) = 1, i.e. P(c) ∩ P(a_i) = ∅.

Now, by the certified Free Facts lemma (`lemmas/free-facts-gcd.md`), gcd(a_n, a_i) > 1,
so P(a_n) ∩ P(a_i) ≠ ∅; fix any prime p ∈ P(a_n) ∩ P(a_i). Since P(c) ∩ P(a_i) = ∅ and
P(a_n) = P(c) ∪ {q′} (disjoint union, as q′ ∉ P(c)), every prime of P(a_n) other than
q′ lies in P(c); so if p ≠ q′ then p ∈ P(c) ∩ P(a_i) = ∅, a contradiction. Hence p = q′
is the ONLY possible common prime, so P(a_n) ∩ P(a_i) ⊆ {q′}, and since it is nonempty
(shown above) and q′ ∈ P(a_n) automatically, P(a_n) ∩ P(a_i) = {q′} exactly. This index
i witnesses (b). ∎

This is a complete, unconditional, self-contained proof using only the problem's own
greedy defining rule (no separate lemma needed beyond Free Facts, which is certified)
— genuinely new relative to the certified lemma set, and a materially different use of
minimality than round 3's Lemma F: Lemma F showed the certified UPPER-bound gap lemmas
cannot produce a smaller *safe* competing candidate; Lemma H instead directly strips a
single prime from the ACTUAL witness value a_n itself and analyzes the two exhaustive
outcomes. **Promotable.**

**Applying Lemma H to the Singleton Hypothesis.** Suppose, for contradiction with the
Singleton Hypothesis, that |F′| ≥ 2 for a rogue-pair witness a_{n_B}, and let q′ ∈ F′
be arbitrary (q′ ∉ S₀, q′ | a_{n_B}). By Lemma H (applied with n = n_B), either (a)
stripping q′ from a_{n_B} yields a value ≤ a_{n_B−1}, or (b) some earlier index i < n_B
shares EXACTLY the prime q′ with a_{n_B} (and no other common prime).

**Why this does not close the Singleton Hypothesis — stated honestly, not smoothed
over.** Lemma H produces a genuine dichotomy for EACH individual prime q′ ∈ F′
separately, but neither branch is self-contradictory, and neither branch depends on
how many OTHER primes are also in F′:
- Branch (a) says nothing wrong: a value obtained by removing one prime power can
  perfectly well fall below the previous term (e.g. if q′ is numerically large — recall
  the retracted "cost ≤ 1" conjecture's own falsifying data, a_153 = 975 = 3·5²·13 for
  a_1 = 35, where the incidental prime 13 is comparatively large relative to the term
  itself). There is no certified bound forcing branch (a) to fail, so it is fully
  consistent with |F′| ≥ 2.
- Branch (b) says q′ is "critical" for legality against one specific earlier term a_i —
  but this is again fully self-consistent for MULTIPLE distinct primes q′, q″ ∈ F′
  simultaneously, each critical for a DIFFERENT earlier index (q′ critical against a_i,
  q″ critical against a different a_{i′} ≠ a_i). Nothing in Free Facts, the Bounded Gap
  Lemma, or Lemma H itself prevents two distinct earlier terms from each demanding a
  DIFFERENT specific outside-S₀ prime for their own individual legality against a_n_B.
  In fact this is exactly the mechanism by which a legitimate integer could need two (or
  more) "junk" primes: if a_i and a_{i′} are two earlier terms whose ONLY prime in
  common with any S₀-multiple-scale candidate would have been different primes, the
  smallest integer simultaneously legal against both may need to borrow one prime from
  each, forcing |F′| ≥ 2 with no contradiction anywhere in the certified toolkit.

So Lemma H is a genuine, fully rigorous NECESSARY condition on each element of F′ (it
pins down exactly why q′ is present — either it drops the value below threshold if
removed, or it is the sole rescuer of some specific earlier term's legality) but it is
not, and cannot by itself become, a SUFFICIENT argument for |F′| = 1: nothing rules out
two or more primes each independently satisfying branch (b) for different specific
earlier indices, which remains entirely consistent with all certified lemmas.

**Attempted repair: could two DIFFERENT primes both satisfying branch (b) be shown
impossible?** I attempted to push further: if q′, q″ ∈ F′ both satisfy branch (b) via
witnessing indices i, i′ respectively (P(a_n_B) ∩ P(a_i) = {q′}, P(a_n_B) ∩ P(a_{i′}) =
{q″}), is there a reason i = i′ is forced (which would at least show the two primes
"compete" for the same slot, though still not literally force q′ = q″)? No such
argument is available: i and i′ are simply two indices among the (possibly many)
earlier terms a_1, ..., a_{n_B−1}, each independently constrained only by Free Facts
(pairwise gcd > 1 with a_{n_B}), and there is no certified relation between the prime
divisors used by DIFFERENT earlier terms to satisfy their own legality constraint
against a_{n_B} — this is precisely the same "no global control over an integer's total
outside-core prime count" obstruction already identified (round 3's Lemma F, round 4's
scope discussion): Free Facts and its descendants are existence statements about
PAIRWISE intersections, never statements bounding the total number of distinct primes
appearing across many such pairwise intersections for one fixed integer. I record this
attempted repair, and its failure, explicitly rather than silently declining to try it.

**Computational re-check with the corrected minimal-witness convention (this round,
independent of the explorer's/reviewer's data, using a from-scratch trial-division
implementation scanning the FULL index range from n = 1 for every candidate persistent
type — not a tail-window sample).** Re-ran the search on the 4 seeds already confirmed
this round (a_1 = 187, 209, 247, 385: all rogue-pair instances have |F′| = 1,
reconfirmed) plus 16 additional fresh seeds never tested before in this workspace,
including several with |Q| = 3 and |Q| = 4 (143, 221, 299, 323, 391, 493, 527, 551,
703, 899, 1073, 1147, 1001, 1155, 1365, 935, 715). Result: **every rogue-pair instance
found across all 20 seeds has |F′| = 1 exactly; zero instances of |F′| ≥ 2 were found**
(6 of the 20 seeds have no rogue pairs at all under their one-round S₀, consistent with
`covering-system-construction`'s "0 or 1 rounds usually needed" picture; the other 14
each have between 2 and 14 rogue pairs, every one singleton). This is consistent with,
but — per Lemma H's honest analysis above — does not amount to a proof of, the general
Singleton Hypothesis. (Full code and output available in the session transcript; not
re-included here since, per the rigor rules, a numerical check is not a proof step and
is not being offered as one.)

**Honest conclusion of this round's attempt.** The dispatch's proposed
minimality-of-earliest-occurrence mechanism, carried out rigorously rather than as a
sketch, produces a genuine new unconditional lemma (Lemma H) that correctly identifies
*why* each individual outside-core prime of a rogue witness is present (a real,
non-trivial structural fact, and a materially different kind of minimality argument
than round 3's Lemma F), but it does not — and by the argument above, cannot, without a
fundamentally new ingredient — rule out MULTIPLE such primes being simultaneously
"critical" for different earlier terms. The Singleton Hypothesis therefore remains open
as a general theorem; this round narrows *why* it is hard (the obstruction is now
precisely located at "no certified argument connects the critical-prime witnesses of
two different elements of F′ to force them to coincide or to force one of them into
branch (a)") rather than leaving it as an unstructured numerical coincidence. This is
real, if incremental, progress: Lemma H is a clean, reusable, unconditional building
block that any future attempt at the Singleton Hypothesis (or at a substitute argument
bounding |F′| by a small constant rather than exactly 1, per the outline's Step 5
fallback) should build from, since it is the sharpest fully-general handle on a
witness's outside-core factorization currently available in this workspace.

### ROUND 6: the Full-Absorption Hypothesis (FAH) — retiring the Universal Singleton
Hypothesis entirely, extended verification, and an honest, three-pronged proof attempt
that stalls at the same structural wall as Lemmas F and H

**Mandatory retraction (per this round's outline-reviewer, independently re-confirmed
by that reviewer from a from-scratch reimplementation — not re-litigated here).** The
Universal Singleton Hypothesis (|F′| = 1 for every rogue-pair witness) is **falsified,
unconditionally, in general**: `a_1 = 4807` gives a rogue pair with F′ = {13,17}
(|F′|=2), and `a_1 = 11305` gives F′ = {11,103} (|F′|=2). Both counterexamples were
independently reverified by the outline-reviewer via a fresh implementation. **The
round-4/5 rescoped Round Resolution Lemma, and its part (i) proof in particular, is
therefore no longer usable as an unconditional or generally-applicable tool** — its
proof literally used |F′|=1 to collapse the Generalized Bounded Witness Lemma's
disjunction ("a_n divisible by *some* prime of F′") to a single forced prime. That
collapse step is invalid whenever |F′| ≥ 2. The Lemma itself is kept in this file
(round 4 section, above) labeled as conditional on the now-false hypothesis, for the
audit trail only; it must not be cited as a general tool going forward.

#### Restating the target: the Full-Absorption Hypothesis (FAH), precisely

Fix any finite S₀ ⊇ Q, a rogue pair (A′,B′) of S₀-extended-persistent types with
disjoint base types (A′∩B′=∅ as subsets of S₀), and — WLOG by relabeling, per the
certified Same-Side Ordering Lemma's supporting convention (`lemmas/same-side-
ordering-lemma.md`) — n_A := min{n:ρ(n)=A′} < n_B := min{n:ρ(n)=B′}. By the certified
**Lemma G** (`lemmas/extended-earliest-witness-intersection.md`), some prime q ∉ S₀
divides both a_{n_A} and a_{n_B}; fix one such q. Write F′ := P(a_{n_B}) \ S₀ (finite,
q ∈ F′ by Lemma G's own proof).

**FAH.** q | a_n for **every** n > n_B with ρ(n) = A′ (not merely infinitely many —
the "infinitely many" case is already free, via the certified Generalized Bounded
Witness Lemma's Corollary, `lemmas/generalized-bounded-witness-lemma.md`, applied with
witness m = n_B: it gives *some* prime of the finite set F′ recurring on infinitely
many A′-occurrences via ordinary pigeonhole — the entire content of FAH is upgrading
"some prime of F′, infinitely often" to "this specific prime q, every single time").

FAH does **not** assert |F′| = 1 (it is compatible with the confirmed |F′| ≥ 2
instances) and is therefore a strictly different, not-yet-falsified claim, not a
repackaging of the retired Singleton Hypothesis.

#### Step 0: extending the empirical verification (both sides, more seeds, full
programmatic scan — not spot-checks)

Before attempting a proof, I independently reimplemented the whole pipeline from
scratch (trial-division greedy generation, `sympy.factorint` only for post-hoc
analysis) and ran it fresh — not reusing the outline-reviewer's or any explorer's
code — on all 7 seeds named in the dispatch (175, 187, 209, 247, 385, 4807, 11305)
plus additional fresh generation with N = 6000–8000 terms, computing Q, the
tail-recurrence persistent base types, canonical witnesses, S, S₀ = Q∪S, the extended
types 𝒫′, and **every** disjoint-base-type rogue pair (A′,B′) with its literal global-
minimum witnesses n_A < n_B, F′, and the Lemma-G prime set F′∩F″ (F″ := P(a_{n_A})\S₀).

For **every** rogue pair found in every seed, I checked, over the **full generated
index range** (not a tail sample): (i) every occurrence of A′ after n_B is divisible
by q, and (ii) every occurrence of B′ after n_B is divisible by q (the symmetric
"B′-side" check the dispatch specifically asked for). Result:

- `a_1=175`: 0 rogue pairs under its one-round S₀ (consistent with prior rounds'
  finding that this seed's S₀ already closes (†) with no residual — no FAH instance to
  check here).
- `a_1=187`: 2 rogue-pair records (A′={3,11}, B′={2,17}, q=7): A′-side 198/198
  occurrences after n_B divisible by q; B′-side 247/247. **0 failures.**
- `a_1=209`: 10 rogue-pair records, all with q=7: A′-side counts 162–178, B′-side
  counts 40–180, **every count 100%, 0 failures** across all of them.
- `a_1=247`: 23 rogue-pair records, all with q=3: A′-side counts up to 1421, B′-side
  counts up to 1433, **0 failures** anywhere.
- `a_1=385`: 10 rogue-pair records, all with q=19: **0 failures**, both sides.
- `a_1=4807`: 12 rogue-pair records, all with q=17 (the |F′|=2 seed, F′={13,17}):
  **0 failures**, both sides, including the specific instance the round-6 explorer and
  outline-reviewer already checked (confirms their number: 151/151 on the B′={2,11}
  side, here re-derived independently in a from-scratch script).
- `a_1=11305`: 42 rogue-pair records, all with q=11 (the other |F′|=2 seed,
  F′={11,103}): **0 failures**, both sides — including the B′={2,5} side (247/247)
  that the singleton-lens explorer had left unchecked and the outline-reviewer
  completed; reproduced independently here.

**Extra probe (new this round, not run by any prior agent): do the *other* elements
of F′ (besides q) ever divide A′-occurrences, and do they divide the earliest A′-
witness a_{n_A}?** For `a_1=4807` (r=13): divides only 1/10 of the A′-occurrences
sampled and does **not** divide a_{n_A} (a_6 = 4845 = 3·5·17·19, no 13). For
`a_1=11305` (r=103): divides 2/79 of A′-occurrences and does **not** divide a_{n_A}
(a_4 = ...). This confirms the qualitative picture already suspected: the non-q
elements of F′ are "incidental" to the specific integer a_{n_B} (branch (a) of Lemma H
in every spot-check performed by the outline-reviewer) and do **not** independently
recur — but, importantly, this is consistent with FAH (which only requires q to be
always present, not that other primes are never present), and it does **not** by
itself supply a mechanism forcing q's universal presence; see below.

**Conclusion of Step 0.** FAH survives a strictly more thorough test than anything run
so far in this workspace: 7 seeds, ~90 individual rogue-pair records, every one
checked on **both** sides over the full generated range, 0 counterexamples. This
substantially exceeds the empirical bar CLAUDE.md sets for treating a hypothesis as
"live," so the remainder of this section moves to the actual proof attempt, not more
numerics.

#### Step 1 (per the dispatch's outline): the easy reduction

Fix n > n_B with ρ(n) = A′. Since A′, B′ are disjoint at the S₀ level and ρ(n)=A′,
ρ(n_B)=B′, the certified **Generalized Bounded Witness Lemma**
(`lemmas/generalized-bounded-witness-lemma.md`), applied with S₀, witness m = n_B,
gives: a_n is divisible by **some** prime of F′ = P(a_{n_B}) \ S₀. This is not new (it
is exactly the Lemma cited by the retired Round Resolution Lemma); the entire content
still to be supplied is: show the witnessing prime can always be taken to be q
specifically, for literally every such n — not merely for a pigeonhole-selected
infinite subset (which the Lemma's own Corollary already supplies for free).

#### Step 2: three genuinely distinct attempts to force "the witnessing prime is q
every time," each carried out in full and each shown, honestly, to fail for the same
underlying reason

**Attempt 2a — direct Lemma H branch analysis on a hypothetical failure.** Suppose,
for contradiction, some n* > n_B has ρ(n*) = A′ and q ∤ a_{n*}. By Step 1, some prime
p ∈ F′ \ {q} divides a_{n*} (F′ \ {q} nonempty in this scenario, else no witnessing
prime would exist, contradicting Step 1). Apply the certified **Lemma H** (Critical
Prime Dichotomy, `lemmas/critical-prime-dichotomy.md`) to n = n*, q′ = p: either
(a) the p-stripped value c := a_{n*}/p^{v_p(a_{n*})} satisfies c ≤ a_{n*−1}, or (b)
some earlier index i < n* has P(a_i) ∩ P(a_{n*}) = {p} exactly. **Neither branch
yields a contradiction.** Branch (a) is not forbidden by anything certified — for n*
large, a_{n*} − a_{n*−1} is typically much smaller than a_{n*}/p for any prime p ≥ 2
of even moderate size (the Bounded Gap Lemma only bounds the gap **above** by a_1, it
gives no lower bound forcing the gap to be large enough to exclude branch (a); direct
inspection of the data confirms branch (a) is in fact the *generic* case for large n,
for essentially every prime dividing a_n, precisely because dividing a large integer
by any single prime factor typically drops it well below the previous, nearby term).
So Lemma H is nearly vacuous at large indices — it gives no information that
distinguishes q from any other prime factor of a_{n*}, let alone a contradiction.
Branch (b) says p is "critical" for one specific earlier index i, which is likewise
fully consistent with p ≠ q (nothing in Free Facts or Lemma H prevents a
*different* prime, for a *different* earlier index, from being critical at n* than
was critical at n_B). **This is exactly the same failure mode already identified and
proved insufficient for the Singleton Hypothesis in round 5** — Lemma H produces a
necessary condition on each prime individually, never an exclusion of alternatives.

**Attempt 2b — inductive "chaining" via successive B′ (or A′) occurrences.** Suppose q
divides a_m for some occurrence m ≥ n_B of type B′ (true for m = n_B, by Lemma G); let
m′ be the next occurrence of B′ after m. I attempted to show q | a_{m′} by induction,
hoping to transfer "q divides one occurrence" to "q divides the next," which combined
with a symmetric argument on the A′ side would give full absorption on both sides by
induction from the base case n_A, n_B. This does **not** work: the only certified tool
connecting m′ to earlier data is the Generalized Bounded Witness Lemma applied with
**some** earlier A′-witness (e.g. n_A), giving a_{m′} divisible by some prime of
F″ := P(a_{n_A}) \ S₀ (finite, and q ∈ F″ by Lemma G, but F″ can also have other
elements, exactly symmetric to F′). This produces the identical disjunction as Step 1,
now on the B′ side, with no additional leverage from having already established q |
a_m for a smaller m — the induction hypothesis is never actually used: nothing
certified propagates "q divided the previous occurrence" into "q divides the next
occurrence," because Free Facts between a_m and a_{m′} (both of type B′, hence
sharing some prime of B′ ⊆ S₀ trivially) supplies no information about primes outside
S₀ at all. **The induction has no engine — it is a restatement of Step 1 at a shifted
witness, not a new argument.**

**Attempt 2c — exchange/minimality argument at the specific failing index n*.**
Suppose again n* > n_B, ρ(n*) = A′, q ∤ a_{n*}, and (Step 1) p ∈ F′\{q} divides
a_{n*}. I attempted to construct a smaller legal candidate c* by replacing the
p-part of a_{n*} with a q-part (e.g. c* := q · (a_{n*}/p^{v_p(a_{n*})})) and derive a
contradiction with the minimality of a_{n*} (the greedy rule) if c* is legal and
c* < a_{n*}. This is **exactly the mechanism already proved impossible in round 3's
Lemma F** ("Minimality bounds magnitude, not type," see above): no certified lemma
controls the sign or size of c* − a_{n*} (q could be larger or smaller than p, with no
bound relating them), and no certified lemma establishes legality of c* against every
earlier term (legality of c* against a_i for i < n* would need gcd(c*, a_i) > 1 for
every i, a completely separate and uncertified fact — replacing one prime factor of
a_{n*} with another does not obviously preserve legality against arbitrary earlier
terms, and Free Facts gives no tool to check this for a *constructed*, non-greedily-
produced candidate). **This attempt fails for precisely the reason Lemma F already
proves must happen: the certified toolkit only ever produces gap bounds and existence
statements, never controlled small exchanges of specific prime content.**

#### Lemma I (Non-Exclusivity of Witness Recruitment) — the new proved negative result

Formalizing why all three attempts above fail by the same root cause, as a reusable
lemma so no future round re-attempts any of them without new machinery:

**Statement.** Let S₀ ⊇ Q be any fixed finite set of primes, A′, B′ disjoint
S₀-extended-persistent types, m any fixed index with ρ(m) = B′, and F′_m :=
P(a_m)\S₀ (finite, nonempty by the certified Generalized Bounded Witness Lemma's own
proof mechanism whenever some n > m with ρ(n)=A′ exists). Suppose |F′_m| ≥ 2. Then no
combination of (i) the certified Free Facts lemma, (ii) the certified Generalized
Bounded Witness Lemma (and its Corollary), (iii) the certified Bounded/Generalized
Bounded Gap Lemmas, and (iv) the certified Critical Prime Dichotomy (Lemma H),
applied in any composition, determines — for a specific n > m with ρ(n) = A′ — *which*
element of F′_m divides a_n, beyond the disjunctive fact that at least one does.

*Proof (by exhaustive inspection of the four certified tools' logical content).* (i)
Free Facts only asserts gcd(a_n,a_m) > 1 for the specific pair (n,m); since
A′∩B′=∅ ⊆ S₀, this forces a shared prime outside S₀, i.e. some element of F′_m — an
existential ("∃p ∈ F′_m: p|a_n"), never an assignment of a specific p. (ii) The
Generalized Bounded Witness Lemma's proof (`lemmas/generalized-bounded-witness-
lemma.md`) is verbatim the same existential argument as (i), specialized; its
Corollary strengthens this only via the *infinite* pigeonhole principle applied across
infinitely many indices n, which produces a single p* recurring on an **infinite
subset** of {n : ρ(n)=A′, n>m} — by construction of the pigeonhole argument (assigning
one witnessing prime per n, then finding a value hit infinitely often), it supplies no
information whatsoever about the **complementary, possibly infinite** set of indices
where a *different* element of F′_m was the (arbitrarily-chosen, when several work)
witnessing prime, nor does it exclude that complementary set from being infinite too.
(iii) The Bounded Gap Lemma and its generalization (Lemma A, this file) bound a_{n+1}
above by a_n plus a fixed modulus; this is a magnitude statement with no reference to
which primes outside S₀ divide the bounded value — already established as insufficient
for any type-forcing conclusion by the certified/proved Lemma F. (iv) Lemma H
(Critical Prime Dichotomy) analyzes a single already-fixed prime q′ | a_n in isolation,
producing a magnitude dichotomy (branch (a): stripping drops below a_{n-1}) or a
single-earlier-index divisibility fact (branch (b)); by inspection of its proof
(`lemmas/critical-prime-dichotomy.md`), neither branch references or excludes any
*other* prime of F′_m, and (per the Reviewer-corrected statement) the two branches are
not even mutually exclusive for a single q′, let alone comparative across two distinct
primes q′, q″ ∈ F′_m. Hence no composition of (i)–(iv) can single out one element of
F′_m over another for a specific occurrence n; each tool's conclusion is either purely
existential (∃) or purely magnitude-based, and neither kind of statement can produce an
identity claim ("the witnessing prime IS q′") that survives being applied to two
different candidate primes symmetrically. ∎

**Scope.** This is a genuine, if negative, structural fact: it shows that Attempts
2a–2c (and, by the same inspection, any future attempt built solely from the four
listed certified tools) cannot close FAH when |F′_m| ≥ 2 — precisely the case the
Universal Singleton Hypothesis's falsification guarantees now occurs in general.
Proving FAH (or even a weaker "some prime universally recurs" version) therefore
requires a **new certified tool** not currently in the workspace: something that
converts an *existential* per-occurrence divisibility fact into an *identity* claim
pinned to one specific prime, uniformly over an infinite family of occurrences. No
such tool exists in the certified lemma set as of round 6. **Promotable** as a
negative/scoping result, in the same spirit as Lemma F.

#### Honest conclusion of round 6

FAH is **not proved**. The empirical support is now stronger than any prior round's
(0 failures across 7 seeds, ~90 rogue-pair records, both sides, full index range,
independently reimplemented) but per CLAUDE.md's rigor rules this is evidence, not a
proof, and is reported as such. Three structurally different proof attempts (branch
analysis, inductive chaining, exchange/minimality) were carried out in full, not
sketched, and each is shown — via the new Lemma I — to fail for the identical root
cause: every certified tool in this workspace produces either an existential
divisibility fact or a magnitude bound, and no composition of these can promote
"some prime of a finite set works" to "this specific prime always works." This is the
same wall that blocked the Singleton Hypothesis (Lemmas F and H), now shown (Lemma I)
to block the strictly weaker FAH as well, for the same reason, generalizing the
diagnosis rather than repeating it. **FAH's precise statement (Step 0 restatement
above) is self-contained and ready for import by `covering-system-construction`'s
Collateral-Safety line IF a future round supplies the missing ingredient**, but that
ingredient — a way to convert existential witness statements into uniform identity
statements — does not exist yet in this workspace, and this round's honest contribution
is pinning down precisely what shape it would need to have (per Lemma I's proof: it
cannot be a further consequence of Free Facts, Generalized Bounded Witness, the Gap
Lemmas, or Critical Prime Dichotomy alone; it must come from a genuinely new
mechanism).

## Approaches tried
- **Round 2 (opened this round).** New top-level framing via an integer cost potential.
  Initial draft overclaimed "cost(n) ≤ |𝒫|-1" (self-corrected in-round) and then, after
  correction, still conjectured "C=1 in the sparse regime" based on limited numerics.
- **Round 3 (this round).** Retracted the "C=1 sparse regime" conjecture per the
  outline-reviewer's explicit counterexample (a_1=35, Q={5,7}, true core {2,3}, T=34,
  L=210) — documented above with the concrete falsifying data, not just a citation.
  Replaced the abandoned cost-bound target with three new, fully proved, unconditional
  lemmas: (A) Generalized Bounded Gap fact (any Q-multiple modulus c gives
  a_{n+1} ≤ a_n + c); (B) Single-Witness-Prime Pigeonhole Refinement of the Bounded
  Witness Lemma (a single specific prime, not just "some prime of a finite set," recurs
  infinitely often for each ordered pair of disjoint persistent types); (C) Extended
  Persistent-Type Pigeonhole (the finite extended-type state space over Q∪S is well
  defined, by the same pigeonhole mechanism as the base-type case). Fully resolved the
  |Q| = 1 special case (no dependence on (†)). Attempted to combine (B) and (C) to close
  (†) directly; documented in full, honest detail exactly where this attempt stalls (an
  arbitrary, non-canonical witness's full factorization is not certified to avoid primes
  outside the fixed finite core S_0) — this is a genuinely different formulation of the
  same underlying crux as `covering-system-construction`'s (†), not a resolution of it.
- **Round 3 (this round).** Imported and independently re-verified, in this approach's
  own cost/witness-prime vocabulary, the two lemmas found this round by the explorers:
  restated as Lemma D (Canonical-Refinement Lemma: B_can = B ∪ F_B exactly, and every
  extended-persistent refinement A' of A meets F_B, hence meets B_can) and Lemma E
  (F_A ∩ F_B ≠ ∅ for disjoint persistent base types A, B). Both proved here from scratch
  (not merely cited) directly from the certified Free Facts, Bounded Witness Lemma, and
  Finite Core Theorem. Localized the residual gap precisely to "rogue pairs" (both sides
  non-canonical refinements). Carried out the outliner's "rogue refinement must be
  skippable" exchange attempt in full: constructed the natural competing "safe" candidate
  from the Generalized Bounded Gap Lemma and showed it does NOT yield the needed
  contradiction, for two independent, explicitly identified reasons (the safe candidate
  is generically LARGER than the actual greedy choice, so minimality says nothing about
  it; and no certified lemma constructs a SMALL safe candidate of controlled type).
  Distilled this into a new proved structural lemma (Lemma F: minimality bounds
  magnitude, not extended type) explaining why this entire family of exchange arguments
  cannot close (†) with the currently certified toolkit — a genuine negative result,
  recorded so no future round re-attempts the same mechanism without first obtaining a
  fundamentally different kind of lemma (a small-gap safe-candidate construction, which
  does not currently exist in this workspace).
- **Round 4 (this round).** Rescoped the outliner's Round Resolution Lemma per the
  outline-reviewer's mandatory correction: dropped the falsified "resolves the whole
  base-type pair" claim (confirmed falsified again independently: recruited prime 13
  hits only ≈14% of base-type-{7}/{5} occurrences on a_1=175) and replaced it with the
  correctly-scoped pair-local target. Proved new Lemma G (Extended Earliest-Witness
  Intersection — a genuine, unconditional generalization of Lemma E to arbitrary
  extended-persistent types via their own earliest occurrences). Proved the rescoped
  Round Resolution Lemma in full, CONDITIONAL on an explicit, isolated "Singleton
  Hypothesis" (the earliest witness's extra-prime set F' has exactly one element) —
  verified computationally in every rogue-pair instance found across ~20 seeds
  (including a genuine two-round case, a_1=247) but not proved in general. Attempted
  the dispatch's directed first-bad-round/time-ordered minimality induction (modeled
  on aimo-0514/aimo-0077) to remove this hypothesis; identified and documented the
  precise structural reason it stalls (the Singleton Hypothesis is a static
  factorization fact about one fixed integer, not a quantity organized by the
  recruitment process's round order — unlike the crux's minimal-bad-event quantity,
  which is recursively tied to the process's own prior states). Also attempted and
  documented the failure of a secondary bypass (recruiting all of F' at once).
  Finally, answered the dispatch's scope question honestly: even granting the
  Singleton Hypothesis in full generality, the Lemma does NOT by itself bound the
  total number of recruitment rounds (it resolves one witnessed pair at a time, with
  no proof against new rogue pairs arising from refinement, nor a proof of the
  much stronger empirically-supported "one round resolves all currently-rogue pairs
  simultaneously" fact) — so this line of attack, even if completed, is not
  sufficient by itself to close (†); it would need a further, separate ingredient.
- **Round 5 (this round).** Carried out the dispatch's directed attempt to prove the
  Singleton Hypothesis in general via minimality of the earliest-occurrence index,
  rigorously (not as a sketch). Proved a new, fully unconditional **Lemma H (Critical
  Prime Dichotomy)**: for any index n and any prime q′ ∤ S₀ dividing a_n, either
  stripping all copies of q′ from a_n drops below a_{n−1}, or some specific earlier
  term shares EXACTLY q′ (and no other prime) with a_n. Applied this to the Singleton
  Hypothesis and showed, honestly, that it gives a genuine necessary condition on each
  element of F′ separately but no way to rule out two or more distinct primes each
  independently satisfying the "critical for a different earlier term" branch — so it
  does not close the hypothesis. Attempted and documented the failure of a natural
  repair (forcing the two witnessing earlier indices to coincide) — no certified
  mechanism connects the critical-prime witnesses of distinct elements of F′. Reran
  the computational search from scratch (independent implementation, minimal-witness
  convention scanning the full index range from n=1) on the 4 confirmed seeds plus 16
  fresh seeds (including |Q|=3,4 cases): 20/20 seeds with rogue pairs give |F′|=1 in
  every instance, 0 counterexamples found, but this is explicitly reported as
  supporting evidence, not a proof. Verdict: real, if incremental, progress (a new
  unconditional lemma sharply locating the exact remaining obstruction) but the
  Singleton Hypothesis itself remains open.
- **Round 6 (this round).** Retired the Universal Singleton Hypothesis entirely per
  the outline-reviewer's independently-reverified falsification (a_1=4807, F′={13,17};
  a_1=11305, F′={11,103}) and moved to the replacement target, the **Full-Absorption
  Hypothesis (FAH)**: the specific Lemma-G prime q divides EVERY sufficiently large
  A′-side occurrence, not just infinitely many. Extended the empirical verification
  well beyond any prior round's: from-scratch reimplementation, 7 seeds, ~90 rogue-pair
  records, both sides (A′ and B′) checked over the full generated index range, 0
  counterexamples. Made three genuinely distinct proof attempts — (2a) direct Lemma H
  branch analysis at a hypothetical failing index, (2b) inductive chaining across
  successive same-type occurrences, (2c) an exchange/minimality construction — and
  showed each fails for the same underlying reason. Proved this reason as a new
  unconditional negative result, **Lemma I (Non-Exclusivity of Witness Recruitment)**:
  every certified tool in the workspace (Free Facts, Generalized Bounded Witness Lemma,
  the Gap Lemmas, Critical Prime Dichotomy) produces either a purely existential
  divisibility fact or a purely magnitude-based bound, and no composition of these can
  promote "some prime of a finite set F′_m divides a_n" into "a specific fixed prime
  always divides a_n" once |F′_m| ≥ 2. This generalizes, rather than repeats, the
  round-3/5 diagnosis (Lemmas F and H) to the new FAH target. FAH is precisely stated
  and self-contained for import by `covering-system-construction` if a future round
  supplies a genuinely new mechanism (not a composition of the four listed tools);
  none is supplied this round. Verdict: real progress (sharper empirical base, a
  proved structural reason for the stall, three concretely-executed failed attempts
  recorded so they are not re-tried), FAH remains open.
- **Round 7 (this round).** Per the mandatory checkpoint, tested the dispatched
  "Two-Witness Intersection Uniqueness via joint Critical-Prime-Dichotomy" mechanism
  and retracted it as dead: Lemma H's own proof never extracts S₀-type information
  about a branch-(b) witnessing index (so the outline's missing link cannot be
  supplied from Lemma H itself), and a from-scratch reconstruction of the mechanism's
  own motivating example (a_1=4807, F′={13,17}∩F″={17}) shows both candidate primes
  trivially satisfy the uninformative branch (a), giving zero leverage — confirming
  the outline-reviewer's suspicion concretely, not just in the abstract. Attempted the
  "Blocking-Data Bridging" mechanism (using previously-unused illegality/skipped-
  candidate data): proved two new unconditional lemmas (J, Divisor-Restricted
  Pigeonhole; K, Adjacent Multiple Blocking — the first tool in this workspace built
  from negative/illegality data), but the combination stalls with a precisely
  diagnosed obstruction (Lemma K's constructed competitor has no controlled
  factorization relationship to the actual witness, unlike Lemma H's divisor-stripped
  competitor). FAH and Symmetric FAH remain open. Verdict: real progress (one dead
  mechanism definitively closed off with concrete evidence — narrowing the search
  space for future rounds — plus two new certified-quality lemmas), no closure of (†).
- **Round 9 (this round).** Carried out the dispatched cheap-kill check on the
  "downward-transport/predecessor-inheritance" mechanism BEFORE attempting its proof:
  searched ≈270 fresh seeds across two independent sweeps for a genuine FAH failure in
  the properly-recruited |F'|/|F''|≥2 regime; found zero exceptions anywhere (only one
  qualifying instance exists at all in the whole search, a_1=11305, reconfirmed with a
  larger sample: 79/79, 246/246, 16/16, zero failures). Since no failure data exists,
  the dispatch-mandated "scattered vs. runs" discriminator could not be run — reported
  honestly, and read as strong (not conclusive) evidence FOR literal FAH holding
  everywhere tested. Attempted the transport proof anyway per the dispatch's fallback
  instruction. Proved a new, correct, unconditional **Successor-Transport Reduction
  Lemma** (if the successor claim q*|a_{n_j} ⟹ q*|a_{n_{j+1}} holds for all
  sufficiently large j, cofinite FAH follows — genuinely new content, a clean formal
  reduction not previously stated). Showed the successor step itself is NOT provable
  with the current certified toolkit: applying Lemma H (Critical Prime Dichotomy) to a
  hypothetical failing occurrence collapses into the identical obstruction Lemma I
  already certified dead (branch (a) fires trivially/uninformatively for outside-core
  primes of this magnitude, checked directly on both available non-singleton data
  points, matching round 7's diagnosis for the unrelated Two-Witness mechanism).
  FAH/Symmetric FAH remain open. Verdict: real progress (new reduction lemma, larger
  and more targeted empirical sweep, precise diagnosis of why this genuinely different
  mechanism still hits the same wall), no closure of (†).
- **Round 10 (this round).** Carried out the dispatched Escape-Budget attack on the
  Successor Claim to completion. First resolved the outline-reviewer's flagged window
  imprecision with a new, fully proved, unconditional **Window Resolution Lemma**
  (infinitely many consecutive-A′-occurrence gaps exceed 1, so the window must be read
  as the telescoped interval to the next A′-occurrence, never a single sequence step —
  proved in general, not just illustrated numerically, though also confirmed on
  a_1=4807's 26 sampled extended types, all minimum gaps ≥ 5). Then proved BOTH halves
  of the Escape-Budget mechanism explicitly: the premise ("failure forces every
  q*-multiple in the window to be illegal") is proved TRUE directly from the greedy
  minimality definition, but a new **Growing-Constraint Obstruction** proves this
  premise is informationally vacuous — the illegality witness index for a skipped
  candidate ranges over an unboundedly growing pool of intermediate indices (not the
  single fixed index n_B that Confined-GCD Lemma controls), so no certified tool can
  exploit it. This negatively resolves the outline's own flagged "is the witness pool
  bounded" question (it is not) and avoids the outline's flagged circularity risk for
  a more basic reason (the mechanism dies one step before reaching any need for
  S₀-sufficiency). Also documented, honestly, that the secondary Return-Time
  Boundedness question is independently open and not obviously true (fresh
  a_1=4807 data: max observed gap for a sparse extended type grows from 503 to 670 as
  the sampled range extends from N=4000 to N=6000, no sign of stabilizing). FAH and
  Symmetric FAH remain open. Verdict: a complete, clean negative result — the tenth
  mechanism shown dead in this workspace, the first via a genuinely quantitative/
  telescoped-window route, reinforcing Lemma I's diagnosis via an independent
  technique — plus one genuinely new promotable positive lemma (Window Resolution).

## Current best
Unconditionally established, with no gaps: Free Facts, Bounded Gap Lemma,
Persistent-Type Pigeonhole, Bounded Witness Lemma, Finite Core Theorem (all certified,
imported), plus this round's three new lemmas — (A) Generalized Bounded Gap fact, (B)
Single-Witness-Prime Pigeonhole Refinement, (C) Extended Persistent-Type Pigeonhole —
and a full, gap-free resolution of the |Q| = 1 special case. The general case (|Q| ≥ 2)
still requires gap (†) (do disjoint-base-type extended-persistent types share an
S-prime), which this approach does not close; the specific point where the natural
attempt to close it via Lemmas B+C stalls is documented in full above (uncontrolled
junk primes in an arbitrary witness's factorization), providing a sharper, if still
open, target for the next round than the retracted cost-bound conjectures.

Round 3 adds, still unconditionally and gap-free: Lemma D (Canonical-Refinement Lemma,
restated and independently reproved), Lemma E (F_A∩F_B≠∅, restated and independently
reproved), and Lemma F (Minimality bounds magnitude, not type — a new proved negative
structural result). Together these localize the open part of gap (†) to exactly the
**rogue pairs** — extended-persistent refinements A', B' of disjoint persistent base
types A, B with A' ≠ A_can and B' ≠ B_can simultaneously — and rule out, with a proof
(not merely by failed experimentation), the specific "exchange/skippability via an
upper-bound gap lemma" mechanism as a way to close this residual. The gap itself remains
open: no lemma in this workspace (certified or proved in this file) shows rogue pairs
must intersect, nor exhibits a genuine rogue-pair counterexample to the full problem
claim — computational evidence in sibling files (e.g. a_1=35 eventually reaching a
finite period) is consistent with rogue pairs always intersecting in practice, but this
is not proved.

Round 4 adds, unconditionally: **Lemma G** (Extended Earliest-Witness Intersection —
proved in full, promotable). It also adds the rescoped **Round Resolution Lemma**,
proved in full but CONDITIONAL on an explicit "Singleton Hypothesis" per rogue pair
(the earliest witness's extra-prime set outside the current core has exactly one
element); this hypothesis is verified in every tested rogue-pair instance (~20 seeds,
including a two-round case) but not proved in general, and a directed attempt to prove
it via first-bad-round/time-ordered minimality induction is shown to stall for a
specific, documented structural reason (the hypothesis concerns a static
factorization fact about one fixed integer, not a quantity the recruitment process's
round order organizes). Round 4 also establishes, honestly, that even a full proof of
the conditional Lemma would NOT by itself bound the total number of recruitment
rounds — it resolves one witnessed pair per invocation, with no proof ruling out new
rogue pairs arising from later refinement, and no proof of the empirically-stronger
"one round resolves every currently-rogue pair simultaneously" phenomenon observed in
every tested seed. So this line of attack narrows and conditionally strengthens the
picture but does not (yet, even conditionally) close (†).

Round 5 adds, unconditionally: **Lemma H** (Critical Prime Dichotomy — proved in full,
promotable): for any index n and prime q′ ∉ S₀ with q′ | a_n, either removing every
copy of q′ from a_n drops the value to ≤ a_{n−1}, or some specific earlier term shares
with a_n EXACTLY the single prime q′. This is the sharpest fully-general, unconditional
structural fact about a witness's outside-core factorization proved anywhere in this
workspace to date, and it correctly and precisely locates the exact remaining
obstruction to the Singleton Hypothesis: nothing certified rules out two or more
distinct primes of F′ each independently satisfying the "critical for a different
earlier term" branch of Lemma H simultaneously, which remains fully consistent with
every certified lemma. The Singleton Hypothesis is not proved in general this round,
but Lemma H replaces the previous round's less structured "no lever here" diagnosis
with a concrete two-branch case analysis that pinpoints exactly where a future proof
attempt would need new content (a way to force two critical-prime witnesses to
coincide, or to rule out simultaneous distinct-prime criticality). A from-scratch
computational recheck (20 seeds, 16 new, including |Q|=3,4 cases) found 0
counterexamples to |F′|=1, reported honestly as supporting evidence only.

Round 6 adds: retirement of the Universal Singleton Hypothesis (confirmed false in
general — |F′|=2 in two independently-verified instances), replaced by the precisely
stated **Full-Absorption Hypothesis (FAH)** (q divides *every*, not just infinitely
many, later A′-occurrence). Extended empirical verification to 0 counterexamples
across 7 seeds / ~90 rogue-pair records / both sides / full index range (from-scratch
reimplementation). Three distinct proof attempts carried out in full and shown to
fail; the common failure reason is proved as **Lemma I (Non-Exclusivity of Witness
Recruitment)**: no composition of the certified tools (Free Facts, Generalized Bounded
Witness Lemma, the Gap Lemmas, Lemma H) can convert an existential "some prime of a
finite set works" fact into an identity "this specific prime always works" claim, once
that finite set has ≥2 elements. FAH remains open but is now precisely stated,
strongly evidenced, and its exact remaining obstruction is proved rather than merely
observed.

Round 9 adds: the certified (modulo the still-open Successor Claim it consumes)
**Successor-Transport Reduction Lemma**, converting a bare occurrence-to-occurrence
successor implication into cofinite FAH (already known sufficient for the finish).
Extended the empirical base with ≈270 freshly searched seeds targeting specifically the
open |F′|/|F″|≥2 regime at a properly recruited core (two independent sweeps),
confirming zero exceptions found ANYWHERE (not just on the seeds tested before) — the
strongest empirical support for literal FAH recorded in this workspace to date, though
still only evidence, not a proof. Checked, concretely on the available non-singleton
data, why the Successor Claim itself is not provable with the current toolkit: it
collapses via Lemma H into the same generic "branch (a) fires, carrying no information"
phenomenon Lemma I already certified as dead, and a direct Free-Facts route is shown to
be vacuous for a new, specific reason (same-type occurrences trivially share primes, so
Free Facts supplies no outside-core leverage when comparing two occurrences of one
fixed extended type). FAH remains open, but the search space for future mechanisms is
further narrowed by this round's precise diagnosis.

## Full proof
Not present — Status is `partial`. Gap (†), localized to rogue pairs, remains open in
the general (|Q| ≥ 2) case. This approach's round-3 contribution is: independent
re-derivation of the Canonical-Refinement and F_A∩F_B≠∅ lemmas in its own vocabulary: a
full, honest execution of the outliner's proposed exchange mechanism showing it fails;
and a new proved lemma (Lemma F) pinpointing exactly why — magnitude-based minimality
cannot, by itself, control extended type, so no argument built only from the certified
upper-bound gap lemmas can force rogue types to be avoided. Round 4 adds Lemma G
(unconditional) and the rescoped Round Resolution Lemma (conditional on the Singleton
Hypothesis, itself an open, precisely-isolated numerical gap not closed by the
directed minimality-induction technique, with the stall documented structurally), plus
an honest scope finding that this line, even completed conditionally, would not alone
bound the total recruitment-round count. Round 5 adds Lemma H (unconditional). Round 6
retires the Singleton Hypothesis (falsified), replaces it with the precisely-stated
FAH, and adds Lemma I (unconditional negative result pinpointing exactly why FAH
resists the currently certified toolkit). This is real progress (a narrower, more
precise open hypothesis than gap (†) itself, now known not to require |F′|=1, plus a
proved reason the natural proof techniques for it fail) but not a proof of (†) itself.

## Promotable lemmas
- **Window Resolution Lemma (new, round 10).** Statement and full proof given above
  under "ROUND 10 BUILD, Step 1"; proposed file `lemmas/window-resolution-lemma.md`.
  For any rogue pair (A′,B′), infinitely many consecutive-A′-occurrence gaps
  n_{j+1}−n_j exceed 1 (proved via the disjoint partner type B′ occurring infinitely
  often and hence falling strictly between infinitely many pairs of consecutive
  A′-occurrences). Proved from Free Facts and the rogue-pair definitions alone; no
  dependence on any open gap. Reusable to foreclose the false "single sequence-step"
  simplification of any future successor-style / windowed mechanism.
- **Successor-Transport Reduction Lemma (new, round 9).** Statement and full proof
  given above under "Step 2." For a rogue pair (A′,B′) with earliest occurrences
  n_A,n_B, any q* ∈ F′∩F″ (nonempty by the certified Lemma G), and n_1<n_2<... the full
  A′-occurrence sequence past max(n_A,n_B): if q*|a_{n_{j_0}} for at least one j_0
  (guaranteed unconditionally by the certified Generalized Bounded Witness Lemma's
  Corollary) and the Successor Claim (q*|a_{n_j} ⟹ q*|a_{n_{j+1}} for all j ≥ some
  finite J) holds, then q*|a_{n_j} for all sufficiently large j, i.e. cofinite FAH.
  Proved by a two-line finite induction. No dependence on any open gap beyond the
  Successor Claim it consumes; a clean, reusable decoupling of "prove one successor
  step suffices" from "cofinite FAH suffices for the finish" (the latter independently
  re-derived by this round's outliner/outline-reviewer, imported here without
  re-proof). Reusable by `cofinite-window-capacity-bound` or any future successor-style
  attempt at FAH.
- **Same-type Free Facts vacuity observation (new, round 9).** Statement and proof
  given above under "Step 3, Route (b)." For two occurrences n, n' of the SAME
  S₀-extended-persistent type A′, Free Facts' conclusion gcd(a_n,a_{n'})>1 is
  automatically witnessed by A′'s own S₀-primes and gives no outside-core (S ⊆ S₀ᶜ)
  information — unlike its use for DISJOINT types (Lemma G/Free Facts applied across
  types, where the shared prime is forced outside S₀). A small but genuine, checked
  structural fact: it precisely explains why comparing consecutive occurrences of one
  fixed type (rather than a fixed witness against a disjoint type) does not open a new
  Free-Facts-based route around Lemma I's diagnosis. Reusable as a standing caution for
  any future occurrence-to-occurrence mechanism.
- **Lemma K — Adjacent Multiple Blocking (new, round 7).** Statement and full proof
  given above under "New Lemma K." For n ≥ 2 and any prime q with q ∤ a_n, let
  c := q·⌊a_n/q⌋ (the largest multiple of q strictly less than a_n). Then either (a)
  c ≤ a_{n-1}, or (b) some j < n has gcd(c,a_j) = 1. Proved directly from the
  problem's own greedy defining rule (minimality of a_n) — if a_{n-1} < c < a_n, c
  must have been rejected by the greedy process for some legality reason. No
  dependence on any open gap; holds for ANY prime q, dividing a_n or not. The first
  tool in this workspace to construct a candidate from *illegality/skipped-candidate*
  data rather than a positive divisibility fact. **Documented limitation (recorded
  so it is not silently re-attempted, per this workspace's Lemma F/Lemma I
  precedent):** unlike Lemma H's divisor-stripped competitor (whose factorization is
  P(a_n) minus one prime, exactly), Lemma K's competitor c = a_n − (a_n mod q) has NO
  established factorization relationship to a_n, so branch (b)'s blocking prime
  (guaranteed to exist between c's blocker a_j and a_n by Free Facts) cannot be tied
  back to q or to any other specific prime — this is why Lemma K alone does not close
  the Full-Absorption Hypothesis (see the round-7 discussion above).
- **Lemma J — Divisor-Restricted Pigeonhole (new, round 7).** Statement and full
  proof given above under "New Lemma J." For a rogue pair (A′,B′) with witnesses
  n_A < n_B (WLOG), F′ := P(a_{n_B})\S₀, and D(n) := P(a_n)∩F′ for n > n_B with
  ρ(n)=A′: D(n) is always nonempty, and some fixed nonempty D* ⊆ F′ satisfies
  D(n) = D* for infinitely many such n. Proved directly from the certified
  Generalized Bounded Witness Lemma (nonemptiness) plus the infinite pigeonhole
  principle applied to the finite powerset 2^{F′}\{∅} (recurrence of D*). No
  dependence on any open gap. Strictly sharper than the certified Generalized Bounded
  Witness Lemma's Corollary (which only pigeonholes a single responsible prime per n,
  not the full intersection set).
- **Lemma I — Non-Exclusivity of Witness Recruitment (new, round 6, negative
  result).** Statement and full proof given above under "Lemma I." For any fixed
  finite S₀ ⊇ Q, disjoint S₀-extended-persistent types A′, B′, any witness index m
  with ρ(m)=B′, and F′_m := P(a_m)\S₀ with |F′_m| ≥ 2: no composition of the
  certified Free Facts lemma, Generalized Bounded Witness Lemma (+ Corollary), the
  Bounded/Generalized Bounded Gap Lemmas, or Critical Prime Dichotomy (Lemma H)
  determines which specific element of F′_m divides a given later A′-occurrence a_n,
  beyond the disjunctive fact that at least one does. Proved by exhaustive inspection
  of what each of the four certified tools' proof actually establishes (each is either
  a pure existential or a pure magnitude bound; neither kind can be composed into an
  identity claim). Reusable by any future approach attempting the Full-Absorption
  Hypothesis, or any similar "specific recruited prime persists universally" target,
  once |F′_m| ≥ 2 is in play (now known to occur in general, per the falsified
  Universal Singleton Hypothesis) — establishes that a genuinely new mechanism (not a
  composition of the four listed tools) is required, and pinpoints what shape it must
  have (converting existential per-occurrence facts into uniform identity claims).
- **Lemma G — Extended Earliest-Witness Intersection (new, round 4).** Statement and
  full proof given above under "New Lemma G." For any fixed finite S₀ ⊇ Q and two
  disjoint (A' ∩ B' = ∅) S₀-extended-persistent types A', B', with n_A, n_B their
  respective earliest occurrence indices, there is a prime q ∉ S₀ dividing BOTH
  a_{n_A} and a_{n_B}. Proved directly from the certified Free Facts lemma
  (pairwise gcd > 1) plus disjointness of A', B' as subsets of S₀; no dependence on
  any open gap. Strictly generalizes the certified F_A∩F_B≠∅ lemma (Lemma E /
  `lemmas/canonical-witness-intersection.md`) from base-type canonical witnesses to
  arbitrary extended-persistent types via their own earliest occurrences. Reusable by
  any future approach needing a symmetric (both-sides) witness pair for a rogue
  extended-type pair, rather than the asymmetric single-witness construction the
  certified Generalized Bounded Witness Lemma's Corollary uses.
- **Lemma A — Generalized Bounded Gap Lemma.** Statement and full proof given above
  under "Genuinely new, unconditional content established this round." For any positive
  integer c divisible by every prime of Q = P(a_1), a_{n+1} ≤ a_n + c for all n ≥ 1;
  hence a_{n+1} ≤ a_n + a_1·p for any prime p. Proved directly from Free Facts by the
  same "smallest multiple exceeds by at most the modulus" argument as the certified
  Bounded Gap Lemma, generalized from modulus a_1 to any Q-multiple modulus c. No
  dependence on any open gap.
- **Lemma B — Single-Witness-Prime Pigeonhole Refinement of the Bounded Witness
  Lemma.** Statement and full proof given above. For disjoint persistent types A, B
  and the canonical witness m_B, there is a single prime p*(A,B) ∈ F_{A,B} ⊆ S dividing
  a_n for infinitely many n with τ(n) = A (n > m_B). Proved by applying the infinite
  pigeonhole principle to the (finite) set F_{A,B} over the (infinite) index set
  {n > m_B : τ(n) = A}. No dependence on any open gap; strictly sharper information
  than the certified Bounded Witness Lemma alone.
- **Lemma C — Extended Persistent-Type Pigeonhole.** Statement and full proof given
  above. With S_0 := Q ∪ S (finite, from the certified Finite Core Theorem) and
  ρ(n) := P(a_n) ∩ S_0, there is a finite nonempty set 𝒫' of extended-persistent types
  and a threshold N_2 such that ρ(n) ∈ 𝒫' for all n > N_2. Proved by the identical
  pigeonhole mechanism as the certified Persistent-Type Pigeonhole, applied to S_0
  instead of Q. No dependence on any open gap.
- **Lemma D — Canonical-Refinement Lemma (independently re-derived, round 3).**
  Statement and full proof given above under "Restating the imports." For disjoint
  persistent base types A, B: (i) B_can := ρ(m_B) = B ∪ F_B exactly, where F_B :=
  P(a_{m_B}) \ Q; (ii) every extended-persistent refinement A' of A satisfies
  A' ∩ F_B ≠ ∅, hence A' ∩ B_can ≠ ∅. Proved directly from Free Facts, the Bounded
  Witness Lemma, and the definition of S in the Finite Core Theorem. No dependence on
  any open gap. (This is the same mathematical fact certified via
  `covering-system-construction`'s Step 4d; reproved here independently in this
  approach's own notation, not merely cited.)
- **Lemma E — F_A ∩ F_B ≠ ∅ (independently re-derived, round 3).** Statement and full
  proof given above. For disjoint persistent base types A, B, F_A ∩ F_B ≠ ∅. Proved
  directly from Free Facts (gcd(a_{m_A},a_{m_B})>1) plus disjointness of A, B in Q. No
  dependence on any open gap. (Same fact as `covering-system-construction`'s Step 4e;
  reproved independently here.)
- **Lemma F — Minimality bounds magnitude, not type (new, round 3).** Statement and
  full proof given above under "Diagnosis." No certified lemma in this workspace (the
  Bounded Gap Lemma or its generalization, Lemma A) constructs a legal candidate whose
  gap from a_n is smaller than Θ(a_1) while also having a controlled (safe/canonical)
  extended type; consequently no exchange/minimality argument built solely from these
  upper-bound gap lemmas can force a rogue extended type to be avoided by the greedy
  choice. Proved by direct inspection of the two certified magnitude lemmas' proofs. A
  genuine negative/structural result: it does not close (†), but it rules out an entire
  family of proof attempts with a proof, not just a failed experiment, and should be
  imported by any future approach considering an exchange-style argument for (†).
- **Lemma H — Critical Prime Dichotomy (new, round 5).** Statement and full proof given
  above under "ROUND 5." For any index n ≥ 2 and any fixed finite S₀ ⊇ Q, and any prime
  q′ ∉ S₀ with q′ | a_n: writing e := v_{q′}(a_n) and c := a_n/q′^e, either (a) c ≤
  a_{n−1}, or (b) some index i < n has P(a_i) ∩ P(a_n) = {q′} exactly. Proved directly
  from the problem's own greedy defining rule (minimality of a_n as the smallest legal
  successor of a_{n-1}) plus the certified Free Facts lemma; no dependence on any open
  gap, no dependence on S₀ being the Finite Core Theorem's specific set (holds for ANY
  fixed finite S₀ ⊇ Q). Genuinely different mechanism from Lemma F (round 3): Lemma F
  showed the certified upper-bound gap lemmas cannot produce a smaller competing safe
  candidate; Lemma H instead strips a single prime directly from the actual witness
  value and gives an exhaustive two-branch case analysis. Shown (in this round's
  discussion) to give a necessary but not sufficient condition for the Singleton
  Hypothesis — reusable by any future approach attempting to bound |F′| (exactly 1, or
  by any explicit constant) for a rogue-pair witness.

### ROUND 7: retraction of the joint-Lemma-H "Two-Witness Intersection Uniqueness"
mechanism (with a concrete falsifying computation on its own motivating example), a
new unconditional lemma using previously-unused NEGATIVE (illegality) data
("Adjacent Multiple Blocking"), and an honest, precisely-diagnosed stall of the
"Blocking-Data Bridging" mechanism aimed at the Full-Absorption Hypothesis (FAH)

**Dispatch and mandatory checkpoint (recap).** This round's outline
(`/tmp/round-7/proof-outliner.md`) proposed two new mechanisms for this approach: (a)
prove **Two-Witness Intersection Uniqueness** (|F′ ∩ F″| = 1, using Lemma G's two
symmetric witnesses n_A < n_B) via a "joint Critical-Prime-Dichotomy" argument applied
to *two* candidate primes against the fixed earliest witness a_{n_B}; (b) prove
**Blocking-Data Bridging** (upgrading "some prime of F′ works" to "the specific
Lemma-G prime q works, for every occurrence, not just infinitely many") using
illegality certificates of skipped candidates — data no certified tool currently
uses. The outline-reviewer (`/tmp/round-7/outline-reviewer.md`) flagged (a) as HIGH
RISK: it suspected the joint-dichotomy argument asserts, without any stated
mechanism, that a Lemma-H branch-(b) witnessing index must carry base type B — and
required this round to either produce that missing mechanism honestly or retract (a)
as unproven/likely-dead before building anything on top of it. This section carries
out that instruction.

#### (a) Two-Witness Intersection Uniqueness — retracted as a target for this
mechanism; the missing link genuinely does not exist in the certified toolkit, shown
both abstractly and by a concrete computation on the mechanism's own motivating
example

**Restating the proposed mechanism precisely.** Fix a rogue pair (A′, B′) with
witnesses n_A < n_B (Lemma G), F′ := P(a_{n_B}) \ S₀, F″ := P(a_{n_A}) \ S₀ (both
finite, nonempty, F′ ∩ F″ ≠ ∅ by Lemma G). Suppose p₁ ≠ p₂ ∈ F′ ∩ F″. Apply the
certified **Lemma H (Critical Prime Dichotomy)** to n = n_B with q′ = p₁: writing
e₁ := v_{p₁}(a_{n_B}), c₁ := a_{n_B}/p₁^{e₁}, either (a₁) c₁ ≤ a_{n_B−1}, or (b₁) some
i₁ < n_B has P(a_{i₁}) ∩ P(a_{n_B}) = {p₁} exactly. Symmetrically for p₂, giving
(a₂)/(b₂) with c₂, i₂.

**Where this can, in principle, produce a contradiction.** If both p₁, p₂ land in
branch (b) with the *same* witnessing index, i₁ = i₂ =: i, then P(a_i) ∩ P(a_{n_B})
would have to equal both {p₁} and {p₂} simultaneously — impossible since p₁ ≠ p₂. So
a contradiction is available in exactly one configuration: both primes hit branch
(b) via a common index. Everything else (both in branch (a); one in (a), one in (b);
both in (b) via *distinct* indices i₁ ≠ i₂) yields no contradiction from Lemma H
alone — this matches round 5's own conclusion, restated here for completeness. The
round-7 outline's proposed fix for the "distinct indices" case was to argue that a
branch-(b) witnessing index for a_{n_B} must itself carry base type B, so that (by
minimality of n_B as the *earliest* B′-occurrence) two distinct such indices below
n_B would force an earlier B-occurrence, contradicting n_B's minimality.

**The missing link, checked directly against the certified statement of Lemma H: no
such implication exists, and none can be extracted from the proof.** Lemma H's proof
(`lemmas/critical-prime-dichotomy.md`) derives branch (b) *only* from: c₁ > a_{n_B−1}
(so c₁ is a "skipped candidate" in (a_{n_B−1}, a_{n_B})) together with Free Facts
applied to c₁ and a_{i₁} — the single conclusion extracted is P(a_{i₁}) ∩ P(a_{n_B}) =
{p₁}, a fact purely about *S₀-external* shared structure (a prime-set intersection
fact between two specific integers). Nothing in this derivation touches ρ(i₁) or
τ(i₁) at all — the proof never inspects which S₀-primes (if any) divide a_{i₁}, only
which *external* (non-S₀) prime it shares with a_{n_B}. There is no route from "a_{i₁}
shares exactly {p₁} with a_{n_B} outside S₀" to "a_{i₁}'s S₀-signature is B." This
confirms, at the level of the proof itself (not just by inspection of the statement),
that the outline's proposed missing link is not merely unproved in this workspace —
it is not implied by anything Lemma H's own derivation produces, so proving it (if
even true) would require an entirely separate argument connecting a witness's
*external* prime content to its *S₀-internal* type, which no certified tool in this
workspace attempts.

**Concrete computational check on the mechanism's own motivating example (a_1 =
4807), confirming the mechanism is not merely inconclusive but degenerate.**
Independently re-derived, by direct computation, the exact rogue-pair instance used
in round 6 as supporting evidence for FAH/Symmetric FAH (`current.md` ROUND 6
section): generating the sequence for a_1 = 4807 term by term (trial-division
factorization, no shortcuts) gives a_2,...,a_7 = 4818, 4826, 4830, 4840, 4845, 4862,
with P(a_6) = {3,5,17,19}, P(a_7) = {2,11,13,17}, matching the round-6 report exactly.
Computing Q = P(4807) = {11,19,23} and, from the minimal canonical witnesses of the
three persistent base types ({11} at n=2, {19} at n=3, {23} at n=4), S =
(P(a_2)\Q) ∪ (P(a_3)\Q) ∪ (P(a_4)\Q) = {2,3,73} ∪ {2,127} ∪ {2,3,5,7} =
{2,3,5,7,73,127}, S₀ = Q ∪ S = {2,3,5,7,11,19,23,73,127}. With ρ(n) := P(a_n) ∩ S₀:
ρ(6) = {3,5,19} =: A′, ρ(7) = {2,11} =: B′ (13, 17 ∉ S₀), matching round 6's report
exactly and confirming n_A = 6, n_B = 7 are indeed the earliest occurrences of these
extended types among n = 1,...,7 (ρ(2) = {2,3,11,73}, ρ(3) = {2,19,127}, ρ(4) =
{2,3,5,7,23}, ρ(5) = {2,5,11} — none equal A′ or B′). So F′ = P(a_7) \ S₀ = {13,17},
F″ = P(a_6) \ S₀ = {17}, F′ ∩ F″ = {17} — the |F′| = 2 case the outline specifically
cites as its supporting evidence for the *conclusion* |F′∩F″|=1.

Now apply Lemma H to n = n_B = 7 with each candidate prime in F′:
- q′ = 13: e = 1, c = 4862/13 = 374. Is c > a_6 = 4845? **No** (374 ≪ 4845): branch
  (a) holds trivially, with enormous slack — c is not even close to the threshold.
- q′ = 17: e = 1, c = 4862/17 = 286. Is c > a_6 = 4845? **No** (286 ≪ 4845): branch
  (a) holds trivially as well, with the same enormous slack.

**Both candidate primes fall into branch (a), and branch (a) carries zero
information** (it only ever asserts c ≤ a_{n-1}, a magnitude fact with no bearing on
which witness p₁ vs p₂ actually recurs). So on the exact instance offered as
supporting evidence for the mechanism, Lemma H's dichotomy is entirely vacuous — it
gives no branch-(b) witnessing index for either candidate prime, hence no possible
route to the "common index" contradiction described above, and no purchase at all on
why 17 (not 13) is the prime that turns out to satisfy F′∩F″ = {17}. This is not a
coincidence of this one seed: stripping any prime factor ≥ 11 from a value on the
order of 4862 and comparing against the previous term a_6 = 4845 (only 17 less) will
essentially always land far below a_{n-1} whenever the stripped prime is a
non-negligible fraction of a_n's size — precisely the generic regime for outside-core
primes recruited by Lemma G (they are witnesses' *large* prime factors, not small
ones), so branch (a) firing trivially, rather than branch (b) firing informatively,
is the expected outcome, not an anomaly. This gives concrete, checked confirmation
(not just abstract suspicion) that the joint-Lemma-H mechanism has essentially no
engagement with the actual quantity (F′∩F″) it was proposed to control.

**Verdict on Two-Witness Intersection Uniqueness, stated honestly, per the mandatory
checkpoint.** The proposed joint-Critical-Prime-Dichotomy mechanism is **retracted as
a viable proof route** — not merely "still open," but shown, both by inspecting
Lemma H's proof (no S₀-type information is ever extracted about a branch-(b)
witnessing index) and by direct computation on its own supporting example (branch
(a) fires trivially for every candidate prime, so branch (b) — the only branch that
can ever produce a contradiction — never triggers), to carry no mechanism connecting
n_B's minimality to the outside-core intersection size. This confirms the
outline-reviewer's diagnosis: this is a 4th instance of the family Lemma I already
proved dead (composing existential, magnitude-only facts cannot promote "some prime
works" to "this specific prime works" or "exactly one prime works"). **Two-Witness
Intersection Uniqueness itself is NOT disproved** — round 6's empirical data (34/34,
0 counterexamples) is untouched by this section, and the fact remains plausible — but
this specific mechanism for proving it is dead, and per the "never re-attempt" list
convention, no future round should re-attempt joint-Lemma-H-branch analysis against a
fixed witness's own minimality (in this or the symmetric n_B<n_A form) as a route to
it. A genuinely different mechanism (not built from Free Facts + Generalized Bounded
Witness + Gap Lemmas + Critical Prime Dichotomy, per Lemma I's diagnosis) would be
needed, and none is proposed here.

#### (b) Blocking-Data Bridging — a new unconditional lemma using negative
(illegality) information, honestly shown insufficient by itself to prove FAH, with a
precise diagnosis of the obstruction

Since Two-Witness Intersection Uniqueness is not available, this section follows the
outline-reviewer's instructed fallback: proceed with FAH stated for an *arbitrary*
fixed q ∈ F′ ∩ F″ (guaranteed to exist, not necessarily unique, by the certified
Lemma G), rather than blocking on step (a).

**Restating the target precisely, and flagging a scope subtlety not previously
recorded.** FAH, as stated in `current.md`'s ROUND 6 section, says "the Lemma-G
prime q" divides every later A′-occurrence — implicitly treating q as canonically
determined. Since Two-Witness Intersection Uniqueness is unresolved (and, per part
(a), the specific mechanism for it is now dead), if |F′∩F″| ≥ 2 there may be *several*
candidate primes q, and FAH's statement should honestly be read as: *there exists* a
choice of q ∈ F′∩F″ (not necessarily every choice) for which the "every occurrence"
property holds. This scope subtlety was not previously flagged in any round's file
and is recorded here for precision; it does not by itself close or worsen the gap,
but any future proof of FAH must specify which q it is proving the property for.

**New Lemma J (Divisor-Restricted Pigeonhole) — fully proved, unconditional, no new
gap.** Let (A′,B′) be a rogue pair with witnesses n_A < n_B (WLOG; the mirror case
n_B < n_A is identical with A′,B′ and n_A,n_B swapped throughout — Lemma G and the
Generalized Bounded Witness Lemma are both stated symmetrically in the two types, so
no separate argument is needed, only the relabeling A′↔B′, n_A↔n_B). Let F′ :=
P(a_{n_B}) \ S₀ (finite, nonempty by Lemma G) and D(n) := P(a_n) ∩ F′ for n > n_B with
ρ(n) = A′. Then D(n) is nonempty for every such n, and there is a fixed nonempty
subset D* ⊆ F′ such that D(n) = D* for infinitely many such n.

*Proof.* Nonemptiness: by the certified Generalized Bounded Witness Lemma
(`lemmas/generalized-bounded-witness-lemma.md`), applied with S₀, the disjoint types
A′, B′, and witness m = n_B (ρ(n_B) = B′): every n > n_B with ρ(n) = A′ has a_n
divisible by some prime of F′_{A′,B′} = P(a_{n_B}) \ S₀ = F′; that prime lies in
P(a_n) ∩ F′ = D(n), so D(n) ≠ ∅. Recurrence: A′ ∈ 𝒫′ is S₀-extended-persistent, so
infinitely many n > n_B have ρ(n) = A′. For each such n, D(n) is a nonempty subset of
the fixed finite set F′, so D(n) ranges over the finite set 2^{F′} \ {∅} (of size
2^{|F′|} − 1) as n ranges over an infinite index set. By the infinite pigeonhole
principle (`knowledge_base.md`, "Pigeonhole / extremal principle"), some fixed
nonempty D* ⊆ F′ is attained by D(n) for infinitely many n. ∎

This differs from the certified Generalized Bounded Witness Lemma's Corollary (which
pigeonholes over *responsible primes*, one per n) by pigeonholing over the *entire*
intersection set D(n) at once — strictly more refined data (D* captures exactly which
combination of F′-primes recurs together, not just that some one of them does), fully
proved, no dependence on any open gap. **Promotable.**

**Attempting the Blocking-Data Bridging mechanism proper.** The target is: for the
fixed q ∈ F′∩F″ from Lemma G, q ∈ D(n) for *every* n > n_B with ρ(n) = A′ (not just
the infinitely-many n with D(n) = D* from Lemma J). Suppose, for contradiction, some
n > n_B with ρ(n) = A′ has q ∉ D(n), i.e. q ∤ a_n.

**New Lemma K (Adjacent Multiple Blocking) — fully proved, unconditional, genuinely
new (uses illegality/blocking data, not covered by Lemma I's diagnosis of the four
positive/existential tools).** Let n ≥ 2 and let q be any prime with q ∤ a_n. Let
c := q · ⌊a_n/q⌋ (the largest multiple of q strictly less than a_n; well-defined and
≥ 0, and c < a_n since q ∤ a_n means a_n mod q ∈ {1,...,q-1} ≠ 0, so a_n − c = a_n mod
q ≥ 1). Then either (a) c ≤ a_{n-1}, or (b) there is an index j < n with gcd(c,a_j) =
1 (i.e. c is illegal against a_j — a "skipped candidate" in the greedy sense).

*Proof.* If c ≤ a_{n-1}, (a) holds and there is nothing further to prove. Otherwise
c > a_{n-1}, and combined with c < a_n (shown above), a_{n-1} < c < a_n. Since a_n is,
by the problem's greedy defining rule, the *smallest* positive integer exceeding
a_{n-1} with gcd(·, a_i) > 1 for every i < n, and c is a positive integer strictly
between a_{n-1} and a_n, c cannot itself satisfy this legality condition for every
i < n — if it did, minimality of a_n would force a_n ≤ c < a_n, a contradiction. So
some j < n has gcd(c,a_j) = 1, giving (b). ∎

This is a genuinely new construction relative to every previously certified/proved
lemma in this workspace's family: Lemma H (Critical Prime Dichotomy) strips a prime
that *does* divide the witness, producing c = a_n/q′^e, a value whose full prime
factorization is controlled exactly (P(c) = P(a_n) \ {q′}); Lemma K instead rounds
a_n *down* to the nearest multiple of a prime q that does *not* divide a_n, producing
a value c = a_n − r (r := a_n mod q, 1 ≤ r < q) whose factorization has **no
established relationship to P(a_n)** beyond numerical proximity. **Promotable** as a
standalone unconditional lemma (it is correct and complete on its own terms), but —
as the next paragraph shows — this uncontrolled factorization is exactly why it fails
to close the target.

**Why Lemma K does not close Blocking-Data Bridging, stated precisely (the honest
stall).** Suppose q ∤ a_n as above and branch (b) of Lemma K fires: gcd(c,a_j) = 1 for
some j < n. By Free Facts, gcd(a_n,a_j) > 1 (j ≠ n), so some prime r divides both a_n
and a_j. The hoped-for next step would be to show r must be related to q (e.g. r = q,
or r forces a contradiction with q ∤ a_n) — but there is **no certified or provable
relationship between P(c) and P(a_n)** here: unlike Lemma H's construction (where
P(c) = P(a_n) \ {q′} is an exact, computable identity, letting "p ∈ P(a_n)∩P(a_j),
p ≠ q′" be excluded outright since such p would lie in P(c)∩P(a_j) = ∅), Lemma K's c
is a *different integer* from a_n (differing by 1 ≤ r < q, generically a "junk"
amount with an uncontrolled factorization of its own — exactly the same "junk prime
contamination" phenomenon this approach retracted in round 2 for the raw quantity
cost(n) = |P(a_n)\Q|). So P(c) ∩ P(a_j) = ∅ says nothing about which primes of
P(a_n) ∩ P(a_j) exist (P(a_n) and P(c) share no forced structural relationship at
all, since c is not a divisor of a_n), and in particular gives no way to rule out
r = q (which would refute the contradiction hypothesis, not confirm it) or to force
r to be anything specific. Concretely, on the a_1 = 4807 example: for a hypothetical
future occurrence n of A′ = {3,5,19} with, say, 13 | a_n but 17 ∤ a_n (i.e. q = 17
∉ D(n) with D(n) = {13}), Lemma K's construction c = 17·⌊a_n/17⌋ is some integer
within 16 of a_n whose own factorization bears no known relation to a_n's; even
granting branch (b) fires, the blocking index j's shared prime with a_n (guaranteed
to exist by Free Facts) could be 3, 5, 19 (already known, uninformative — those are
S₀-primes shared via A′ itself) or 13 (the very prime we were trying to rule out) or
some entirely unrelated "junk" prime — nothing forces it toward a contradiction
against q = 17 not dividing a_n. **The obstruction is structurally the same one
Lemma F (round 3) and Lemma I (round 6) already diagnosed for the other three tool
families: the certified/available construction produces a competitor integer with an
uncontrolled relationship to the actual witness's factorization, and no tool in this
workspace — now including this round's new negative-information construction —
supplies that missing control.** This is a precise, checked diagnosis, not a vague
restatement: the specific reason Lemma K fails is different in kind from Lemma F's
reason (Lemma F's competitors were too *large*/wrong-type by construction; Lemma K's
competitor is close in *magnitude* but has no controlled *factorization* relationship
to a_n at all, since it is not obtained by modifying a_n's own divisors).

**Conclusion of the round-7 attempt, stated without overclaiming.** Neither of this
round's two dispatched targets is proved. (a) Two-Witness Intersection Uniqueness's
proposed mechanism (joint Lemma-H branch analysis against a fixed witness's own
minimality) is retracted as dead, with both an abstract proof-level argument (Lemma
H's derivation never touches S₀-type data) and a concrete computation on its own
motivating example (a_1 = 4807: both candidate primes trivially satisfy branch (a),
giving zero leverage) — this matches and confirms the outline-reviewer's suspicion
precisely, not just "possibly." (b) Blocking-Data Bridging produces one genuinely new,
fully proved, promotable unconditional lemma (Lemma K, Adjacent Multiple Blocking —
the first tool in this workspace to use illegality/skipped-candidate data), plus the
straightforward Divisor-Restricted Pigeonhole (Lemma J), but the attempt to combine
them into a proof of FAH stalls for a precisely diagnosed reason: Lemma K's
constructed competitor c has no controlled factorization relationship to the actual
witness a_n, so Free Facts' guaranteed shared prime between c's blocking index and a_n
cannot be pinned to q. **FAH and Symmetric FAH remain open.** No new mechanism
surviving Lemma I's diagnosis (existential-to-identity promotion) has been found this
round; the search for one should continue, but not via joint-Lemma-H analysis
(now dead) nor via this specific "round down to nearest non-divisor multiple"
construction (shown insufficient, though its underlying Lemma K is real, reusable
content for a future, different combination).

#### Updated key lemmas (round 7)
- **Lemma J (Divisor-Restricted Pigeonhole)** — new, proved in full above,
  unconditional. Sharpens the certified Generalized Bounded Witness Lemma's Corollary
  by pigeonholing over the full intersection set D(n) rather than a single responsible
  prime. Does not by itself close FAH.
- **Lemma K (Adjacent Multiple Blocking)** — new, proved in full above, unconditional.
  The first tool in this workspace's toolkit to use negative/illegality
  (skipped-candidate) information rather than positive/existential divisibility facts.
  Does not by itself close FAH; the precise obstruction (uncontrolled factorization of
  the constructed competitor c relative to the witness a_n) is documented above and
  should not be silently re-attempted with cosmetic variants — any future use of
  illegality data would need a construction where the competitor's factorization has
  some certified relationship to a_n's own (which Lemma K's "round down" construction,
  unlike Lemma H's "strip a divisor" construction, does not provide).
- **Two-Witness Intersection Uniqueness (joint-Lemma-H mechanism)** — retracted as a
  dead route this round (see (a) above); the underlying fact itself remains an open,
  empirically-supported (34/34, unaffected by this section) but unproved conjecture,
  now known to require a genuinely different mechanism than any combination of
  Free Facts / Generalized Bounded Witness / Gap Lemmas / Critical Prime Dichotomy.

### ROUND 9: mandatory cheap-kill check on the "downward-transport/predecessor-
inheritance" mechanism, a new unconditional reduction lemma, and an honest stall
diagnosed precisely as the same wall Lemma I already certified

**Dispatch recap.** This round's outline (`/tmp/round-9/proof-outliner.md`) proposes a
third, genuinely distinct mechanism for the shared FAH/Symmetric FAH crux: an
occurrence-to-occurrence "predecessor inheritance" induction, adapted from crux
`aimo-0016`'s style of upgrading an infinitely-often relation to a for-all relation via
one-step successor propagation. The outline mandates, as a prerequisite before writing
any proof, a **cheap-kill check**: enumerate the FULL A′-occurrence index sequence
n_1 < n_2 < ... for a genuine rogue pair with |F′| or |F″| ≥ 2 at a properly recruited
core, and check whether the (canonical prime q*)-FAILURES among these occurrences are
*scattered* (isolated, no two consecutive) — which would falsify a one-step transport
lemma on its face — or come in *runs* (which would leave transport plausible). If no
rogue instance with actual failures can be found, this must be reported honestly rather
than silently invented.

#### Step 1 (mandatory): the cheap-kill check itself

**Reused/extended the outline-reviewer's corrected framing (round 9): a_1 = 4807
measured at S₀ = Q is NOT a valid instance of the open problem** (the reviewer showed
its properly-recruited core has zero rogue pairs at all — the Finite Core Theorem's own
recruitment already absorbs it). The one genuine instance on record, **a_1 = 11305**
(A′ = {3,7}, n_A = 4; B′ = {2,5}, n_B = 7; F′ = {11}, F″ = {11,103}, q* = 11 — a
genuinely open |F″| = 2 case), was reconfirmed here independently with a larger sample
(N = 8000, vs. the reviewer's N = 6000): **79 A′-occurrences past n_B, 0 failures; 246
B′-occurrences past n_A, 0 failures; 16 more via the alternate witness pair, 0
failures.** Literal (zero-exception) FAH holds on every check of this instance, not
merely a cofinite version.

To find a SECOND instance (needed to test scattered-vs-runs on independent data, and to
check whether a_1=11305 is a fluke), I ran two independent searches (script
`/tmp/round-9/search_rogue.py`, `/tmp/round-9/search_rogue2.py`, trial-division
factorizer, greedy sequence generator, same construction as the certified Finite Core
Theorem: earliest-occurrence base-type witnesses, one-round recruitment to build S₀,
Extended Persistent-Type Pigeonhole to find extended-persistent types, and the same
"rogue pair" test as `covering-system-construction`'s Step 4c):
- **Sweep 1**: 151 seeds a_1 ∈ {100,...,1200} with |Q(a_1)| ≥ 2 (random sample, N=4000
  terms each). Found rogue pairs on several seeds, but **every one had |F′| = |F″| = 1**
  (the already-certified Singleton-Side FAH regime) — zero instances in the genuinely
  open |F′| or |F″| ≥ 2 regime.
- **Sweep 2**: 120 seeds a_1 with |Q(a_1)| ≥ 3 (targeting a richer prime menu, since a
  larger Q makes a larger F′/F″ more likely), a_1 ∈ {1000,...,20000}, N=4000 terms each.
  **Zero rogue-pair instances at all with |F′| or |F″| ≥ 2** were found in this sweep
  either (all rogue pairs found, if any, were singleton on both sides).

**Conclusion of Step 1, stated honestly.** Across ≈270 freshly tested seeds (two
independent sweeps) plus the one instance already on record, the genuinely open
non-singleton regime is empirically *rare*, and — more importantly for the mandated
check — **not a single FAH failure (exception) was found anywhere**, singleton or not.
This means **the scattered-vs-runs discriminator the dispatch mandates cannot actually
be run**: there is no failure data on any tested seed to classify as "scattered" or "in
runs." This is reported here exactly as the dispatch instructs for this contingency: as
new, honest, informative evidence for the population, not smoothed into either a false
"scattered ⟹ transport is false" or a false "no failures ⟹ transport is proved"
conclusion. Per the dispatch's own framing, this result "weakens the case that a
one-step transport lemma is false on its face" and is "itself informative... it would
mean literal FAH may just be true and provable" — exactly the situation found. The
cheap kill does not refute the mechanism, so per the dispatch's instruction ("attempt
the transport-induction proof if it survives") the proof is attempted next.

#### Step 2: a new unconditional reduction — the Successor-Transport Reduction Lemma

Before attempting the successor step itself, it is worth isolating exactly what proving
it would buy, precisely and rigorously (this was not previously stated in this exact
form by any approach in the workspace).

**Successor-Transport Reduction Lemma (new, unconditional, promotable).** Let (A′,B′)
be a rogue pair (disjoint S₀-extended-persistent types refining disjoint base types)
with n_A, n_B their earliest occurrences (Lemma G) and q* ∈ F′∩F″ any fixed prime of
the (certified nonempty, Lemma G) intersection. Let n_1 < n_2 < ... enumerate all
indices n > max(n_A,n_B) with ρ(n) = A′ (an infinite sequence, since A′ is
S₀-extended-persistent). Suppose:
(i) q* | a_{n_{j_0}} for at least one j_0 (guaranteed unconditionally by the certified
Generalized Bounded Witness Lemma's Corollary — an infinite pigeonhole extraction, so
in fact infinitely many such j_0 exist), and
(ii) [**the Successor Claim**, the open target] there is J such that for all j ≥ J,
q* | a_{n_j} ⟹ q* | a_{n_{j+1}}.
Then q* | a_{n_j} for **all sufficiently large** j — i.e. cofinite FAH holds for this
pair and this q*.

*Proof.* By (i), the set D := {j : q*|a_{n_j}} is nonempty (in fact infinite, though
only nonemptiness is needed here). Let j_0 ∈ D with j_0 ≥ J (exists since D is
infinite and J is a fixed finite threshold, so D is not confined to indices below J).
By (ii), applied repeatedly: q*|a_{n_{j_0}} ⟹ q*|a_{n_{j_0+1}} ⟹ q*|a_{n_{j_0+2}} ⟹ ...
— a finite induction at each step, extending by ordinary mathematical induction on
k ≥ 0 to give q*|a_{n_{j_0+k}} for every k ≥ 0. Hence q*|a_{n_j} for every j ≥ j_0,
i.e. all but the finitely many j < j_0 satisfy the divisibility — cofinite FAH. ∎

This is a clean, fully rigorous, unconditional (modulo the stated hypothesis (ii))
reduction: it converts a bare "successor implication eventually" claim directly into
the *cofinite* FAH target that the sibling `cofinite-window-capacity-bound` approach
and this round's outline both certify (in the outline's preamble, independently
re-derived and re-checked here, not merely cited) as sufficient for the whole proof's
finish (`covering-system-construction`'s Step 8.5, via the "eventually" clause already
built into Extended Persistent-Type Pigeonhole). **This is a genuinely new, correct,
promotable lemma** — no prior round stated this precise successor-to-cofinite
reduction, which decouples "prove the successor step" from "re-derive why cofinite
suffices" (the latter already done by this round's outliner/outline-reviewer and
imported here without re-proof).

#### Step 3: attempting the Successor Claim — stalls at the identical obstruction
Lemma I already certified, checked directly and honestly, not merely asserted

**Attempt.** Fix j with q*|a_{n_j}, and suppose for contradiction q* ∤ a_{n_{j+1}}. By
the certified Generalized Bounded Witness Lemma (witness m = n_B, disjoint types
A′,B′), a_{n_{j+1}} is divisible by SOME prime of F″ (or F′, using whichever fixed
witness the pair's roles assign — using the a_1=11305 labelling, F″ = P(a_{n_B})\S₀ is
the menu for A′-occurrences); write this witnessing prime as p ≠ q* (p exists by that
Lemma, and p ≠ q* by the contradiction hypothesis). The goal is to derive a
contradiction using q*|a_{n_j} together with a_{n_j} and a_{n_{j+1}} being CONSECUTIVE
occurrences of the identical extended type A′ (a genuinely different relationship from
anything Lemma H, Lemma I, or Lemma K were checked against before, since those all
used a single fixed canonical witness or a single occurrence in isolation, not a pair
of *consecutive same-type* occurrences).

**Route (a): apply Lemma H (Critical Prime Dichotomy) to n = n_{j+1}, prime p.**
Writing e := v_p(a_{n_{j+1}}), c := a_{n_{j+1}}/p^e, either (branch a) c ≤ a_{n_{j+1}-1},
or (branch b) some index i < n_{j+1} has P(a_i) ∩ P(a_{n_{j+1}}) = {p} exactly.

- *Branch (a) checked directly on both available non-singleton data points, not
  assumed.* On a_1 = 11305 (the only genuine |F′|/|F″|≥2 instance on record — every
  occurrence here is already FAH-compliant so there is no actual failing n_{j+1} to
  test, but the check can still be run on the LARGEST available outside-core prime,
  103, at its one occurrence to see what branch fires generically for a
  "would-be-competitor" prime of this size): stripping 103 from any B′-occurrence
  divisible by it and comparing to the immediately preceding term shows c is always
  far below the preceding term (outside-core primes recruited by the Generalized
  Bounded Witness Lemma are, by construction, factors of ONE fixed witness integer
  a_{n_B}, hence typically a non-negligible fraction of that integer's own size, so
  stripping one from a DIFFERENT, later term a_{n_{j+1}} — generally much larger than
  a_{n_B} since the sequence is increasing — divides by a factor comparable to a_{n_B}
  itself, landing far below a_{n_{j+1}-1}). This exactly reproduces round 7's finding
  on a_1=4807 (both 13 and 17 landed trivially in branch (a): c=374, c=286, both ≪
  a_6=4845) — the SAME generic phenomenon, now confirmed on a structurally different
  data point (a large-prime menu element rather than the specific q* itself). **Branch
  (a) is generically the one that fires, and it carries zero information** (as Lemma
  I's diagnosis already established): it is a pure magnitude fact about c, with no
  bearing on which prime of the menu the actual witness carries.
- *Branch (b), if it fired instead*, would only ever give "some earlier index i shares
  EXACTLY {p} with a_{n_{j+1}}" — a fact about p and a_{n_{j+1}}'s relationship to a
  THIRD index i, with (exactly as round 5 and round 7 already proved for Lemma H in
  every prior application) **no certified route from this fact to any statement about
  q* or about a_{n_j} specifically**. Lemma H's proof extracts no information about
  ρ(i) or about which prime a_{n_j} (a specific, different, earlier index) shares with
  a_{n_{j+1}} — there is no forced relationship between the branch-(b) witnessing index
  i and n_j at all (i could equal n_j, but nothing certified forces this, and if i is
  some unrelated index, the fact is entirely uninformative about q*).

**Route (b): try Free Facts directly between a_{n_j} and a_{n_{j+1}}.** By Free Facts,
gcd(a_{n_j}, a_{n_{j+1}}) > 1, giving SOME shared prime r. Since ρ(n_j) = ρ(n_{j+1}) =
A′, every prime of A′ itself is automatically shared (trivially, both are divisible by
every prime of A′ by definition of ρ) — so this application of Free Facts, unlike its
use in Lemma G (where it was applied to DISJOINT types, forcing the shared prime
outside S₀), gives **no new information here**: the "some shared prime" conclusion is
already satisfied for free by A′'s own primes, and Free Facts supplies no mechanism to
force the shared prime to be specifically q* (or even outside S₀) when the two
integers' S₀-signatures already overlap by construction. This route is vacuous, not
merely inconclusive — a genuinely different (and more basic) failure mode than route
(a)'s.

**Diagnosis (stated as a precise, checked finding, not a repetition of Lemma I by
citation alone).** Both routes available to attack the Successor Claim collapse into
observations already proved dead: route (a) reproduces, on fresh data, the exact
generic-branch-(a)-fires phenomenon round 7 diagnosed for an unrelated mechanism
(Two-Witness Intersection Uniqueness), confirming this is not an artifact of that one
specific mechanism but a structural fact about Lemma H's dichotomy whenever the
stripped prime is a large, "recruited-scale" outside-core factor (as every prime
relevant to FAH necessarily is, by the very construction of F′/F″ via the Generalized
Bounded Witness Lemma). Route (b) is vacuous for a reason specific to this round's
NEW object (consecutive same-type occurrences): unlike every prior mechanism, which
compared a witness against a DIFFERENT, disjoint-typed index (where Free Facts forces
an outside-core shared prime), comparing two occurrences of the SAME extended type
trivially already shares primes (A′ itself), so Free Facts supplies no new leverage at
all — the "existential-to-identity promotion" Lemma I diagnoses as missing from the
toolkit is not just missing here, the relevant existential statement itself degenerates
to a tautology. **This is a genuinely new, if negative, structural finding**, distinct
from a restatement of Lemma I: it shows the "different object" the outliner correctly
identified (occurrence-to-occurrence within one fixed type, rather than core-refinement-
stage witness drift) does NOT open a new avenue for Free Facts to be useful, because
same-type occurrences share primes for a trivial (S₀-internal) reason that swamps any
potential outside-core signal.

#### Conclusion of the round-9 attempt, stated without overclaiming

The mandatory cheap-kill check (Step 1) was carried out honestly: no FAH failure was
found anywhere in ≈270 freshly searched seeds plus the one instance already on record,
so the mandated scattered-vs-runs discriminator could not be run — this is itself
valuable evidence (strong support for literal FAH, reported up per the dispatch's
instructions, not smoothed into a false conclusion either way). The transport proof was
then attempted per the dispatch's fallback instruction. A genuinely new, correct,
unconditional reduction lemma was proved (Successor-Transport Reduction Lemma: the
Successor Claim, if true, gives cofinite FAH, hence suffices for the whole proof's
finish). But the Successor Claim itself is **not proved**: both available routes to it
(Lemma H applied to the failing occurrence; Free Facts applied to the two consecutive
occurrences directly) were checked concretely, not merely cited, and both stall — one
by reproducing the exact "branch (a) fires generically, carrying no information"
phenomenon Lemma I already certified as dead (round 6/7), now confirmed on fresh data;
the other by a new observation specific to this round's object (same-type
comparison trivializes Free Facts' shared-prime guarantee). **FAH and Symmetric FAH
remain open.** This approach's genuinely different framing (occurrence-to-occurrence
rather than counting or per-occurrence absorption) has been fully explored per this
round's dispatch and, like every mechanism before it, has not found the missing
"existential-to-identity promotion" ingredient Lemma I shows is required — but it adds
a reusable reduction lemma and a precise, checked diagnosis (not previously recorded)
of why same-type consecutive occurrences do not open a new avenue for Free Facts.

#### Updated key lemmas (round 9)
- **Successor-Transport Reduction Lemma** — new, proved in full above, unconditional
  (conditional only on the still-open Successor Claim it is designed to consume): the
  Successor Claim, if proved for any q* ∈ F′∩F″ past some finite threshold J, implies
  cofinite FAH for that pair — which the round-9 outline (and this round's
  outline-reviewer, independently) certifies as sufficient for the whole proof's
  finish. Reusable by any future approach (this one or `cofinite-window-capacity-bound`)
  attempting a successor-style argument for FAH.
- **Same-type Free Facts vacuity observation** — new, proved in full above (Route (b)
  of Step 3): for two occurrences n, n' of the SAME S₀-extended-persistent type A′,
  Free Facts' conclusion gcd(a_n,a_{n'})>1 is automatically satisfied by A′'s own
  S₀-primes and supplies no outside-core information, unlike its use for DISJOINT
  types (Lemma G). This is a small but genuinely new structural fact, distinct from
  Lemma I, explaining precisely why the "different object" (occurrence-to-occurrence
  within a fixed type) does not evade Lemma I's diagnosis via a Free-Facts route.

## ROUND 10 — quantitative Escape-Budget attack on the Successor Claim

### Target (imported, certified, unchanged)
The Successor-Transport Reduction Lemma (`lemmas/successor-transport-reduction-lemma.md`)
reduces the whole crux to: does there exist `J` such that for all `j ≥ J`,
`q*|a_{n_j} ⟹ q*|a_{n_{j+1}}` (the **Successor Claim**), where `n_1<n_2<...`
enumerate the `A'`-occurrences past `n_B`. Round 9 showed the qualitative toolkit
(Critical Prime Dichotomy on the failing occurrence; Free Facts on the two same-type
occurrences, now explained by the certified Same-Type Free Facts Vacuity Observation)
cannot supply this. This round attempts a DIFFERENT, quantitative mechanism.

### Why this is genuinely new (not a repackaging of the round-9 dead mechanism)
Round 9's attempt used the Gap Lemmas only as an EXISTENCE bound (to guarantee some
occurrence exists) — never as a numeric ceiling relating value-gaps to index-gaps.
This round's mechanism uses the certified Generalized Bounded Gap Lemma
(`lemmas/generalized-bounded-gap-lemma.md`: `a_{n+1} ≤ a_n + c` for any `c` divisible
by every prime of `Q`) QUANTITATIVELY, following the "growth-forces-divisibility"
flavor of crux `aimo-0611` (flagged by this round's fresh-framing explorer) — a
strictly different tool-usage from anything in Lemma I's diagnosed-dead family.

### Skeleton

**Step 1 (import).** Confined-GCD Lemma gives `g_{n_j} ∈ Div(b)` for every
`A'`-occurrence past `n_B`; the Successor Claim fails at `j` iff `g_{n_j} ∈ D_bad`
(bad divisor classes not divisible by `q*`).

**Step 2 (Escape-Budget Lemma — THE NEW, UNPROVED, KEY TARGET).** Attempt: if
`g_{n_j} ∈ D_bad` (a "failure" at step `j`), then the NEXT occurrence's value
`a_{n_{j+1}}` must exceed `a_{n_j}` by strictly more than the "generic" per-occurrence
increment (empirically, per the analytic explorer's a_1=4807 data, consecutive
`A'`-occurrence value-gaps cluster tightly around one typical value, with occasional
EXACT doublings — i.e., a skipped occurrence). Candidate mechanism: minimality of the
greedy choice at every intermediate index between `n_j` and `n_{j+1}` means that IF a
`q*`-multiple of the right residue class existed within the Bounded-Gap-Lemma window
`(a_{n_j}, a_{n_j}+a_1]` and were legal, the greedy rule would have taken a smaller
term there (possibly of a different type) — so a "failure" at `j` requires every
`q*`-multiple in that window to be provably ILLEGAL (fails `gcd>1` with some earlier
term), which is itself a strong, checkable, currently-uninvestigated constraint tying
`a_{n_j}`'s failure to the factorization of specific EARLIER terms (a genuinely
different information source from anything Lemma I's four tools supply, since it
uses NEGATIVE/illegality data the way Lemma K did, but anchored to the NOW-CONTROLLED
finite alphabet `Div(b)` rather than an uncontrolled competitor — directly repairing
Lemma K's factorization-control gap per this round's dispatch).

**Step 3 (cheap-kill the builder must run first).** Numerically test, on a_1=4807 and
a_1=11305 (and any fresh |F'|,|F''|≥2 seed with `D_bad≠∅`, checked against the
`cofinite-window-capacity-bound` finding that a_1=11305 already has `D_bad=∅` and is
therefore vacuously done): for each failure `j∈E` (there may be none — 4807 has 0
observed failures in the sampled range; if so, this cheap-kill instead searches
harder or reports that no failure has ever been observed, sharpening the confidence
that `E` is finite/small, consistent with — but not proof of — the Successor Claim),
check whether every `q*`-multiple in the window `(a_{n_j}, a_{n_j}+a_1]` is indeed
illegal, and if so, WHICH earlier term blocks it. This is new data no prior round
collected (prior rounds tracked divisibility outcomes, never the illegality reason
for skipped `q*`-multiples specifically in this window).

### Key lemmas (claim + mechanism, both unproved — honestly flagged)
- **Escape-Budget Lemma**: a `D_bad`-class occurrence forces every `q*`-multiple in
  its Bounded-Gap-Lemma window to be illegal — because (candidate mechanism) legality
  requires sharing a prime with every earlier term, and the greedy rule's minimality
  means any LEGAL smaller candidate would have been chosen instead. UNPROVED: the
  step "every `q*`-multiple in the window is illegal" does not yet have a concrete
  mechanism showing WHY, only the tautological restatement that the greedy rule
  skipped it (this is the sharp, honestly-flagged open point, not to be waved past).
- **Summability corollary (if Escape-Budget Lemma holds)**: since each `D_bad`-class
  occurrence forces a specific earlier illegality witness (drawn from a finite pool
  of earlier terms up to index `n_j`, itself unboundedly growing — a genuine risk
  this corollary must address, not assumed away), a counting/telescoping argument
  might bound `|E|` — NOT attempted in this file, flagged for the builder.

### Open gaps
- The Escape-Budget Lemma itself (Step 2) — entirely new, unproved.
- Whether the "specific earlier illegality witness" pool is itself finite/bounded
  (needed for the Summability corollary) — a second, separate open question even if
  the Escape-Budget Lemma is proved.
- Risk of circularity: "why is the q*-multiple illegal" could itself unpack into
  needing S₀-sufficiency (equivalent to (†), per `reversible-transition-map`) —
  the builder must check this does not happen (i.e., that the illegality can be
  witnessed by a FINITE, already-certified fact — e.g. Free Facts against a single
  earlier term — rather than needing the full S₀-legality-sufficiency machinery).

### Cases to cover
None (single unified target across all rogue pairs); if the mechanism works for one
rogue pair's `q*`, it must be checked it generalizes uniformly (not seed-specific).

### Watch out for
The "greedy minimality ⟹ illegality of skipped candidates" step looks easy but is
exactly where Lemma K (round 7) died (uncontrolled factorization of the constructed
competitor) — this round's version is scoped narrowly to `q*`-multiples specifically
(not an arbitrary competitor), which is the intended fix, but the builder must verify
this narrowing is enough before claiming progress.

## ROUND 10 BUILD — the Escape-Budget attack, carried out to completion: a new
correct negative result (Growing-Constraint Obstruction), plus one genuine
promotable positive lemma (Window Resolution)

### Setup recap (imported, unchanged, certified)
Fix a rogue pair `(A',B')` — disjoint `S₀`-extended-persistent types refining
disjoint base types — with earliest witnesses `n_A < n_B` (Lemma G /
`extended-earliest-witness-intersection.md`), `F' := P(a_{n_A})\S₀`,
`F'' := P(a_{n_B})\S₀`, and `q* ∈ F'∩F''` fixed (nonempty by Lemma G). Let
`n_1 < n_2 < ...` enumerate all indices `n > max(n_A,n_B)` with `ρ(n) = A'`
(infinite, `A'` is extended-persistent). The **Successor Claim** (the open target,
per the certified Successor-Transport Reduction Lemma) is: `∃J` such that for all
`j ≥ J`, `q*|a_{n_j} ⟹ q*|a_{n_{j+1}}`.

### Step 1: resolving the outline-reviewer's flagged imprecision — the **Window
Resolution Lemma** (new, unconditional, proved in full, promotable)

**Statement.** For any rogue pair `(A',B')` as above, there are infinitely many
`j` with `n_{j+1} > n_j + 1`. Consequently the interval relevant to the Successor
Claim can never, in general, be replaced by the single-step Bounded-Gap-Lemma
window `(a_{n_j}, a_{n_j}+a_1]`; it must be read as the fully telescoped interval
`(a_{n_j}, a_{n_{j+1}})`, whose length `a_{n_{j+1}} - a_{n_j}` and whose "index
span" `n_{j+1} - n_j` are both, in general, unboundedly larger than `1` or `a_1`.

**Proof.** By hypothesis `(A',B')` is a rogue pair, so `A', B' ⊆ S₀` are both
`S₀`-extended-persistent and `A' ∩ B' = ∅`, with both sets nonempty (nonemptiness:
`ρ(n) ⊇ τ(n)`, and `τ(n) = P(a_n)∩Q ≠ ∅` for every `n` by the certified Free Facts
lemma applied with `i=1` [`gcd(a_n,a_1)>1` forces a shared prime of `Q = P(a_1)`],
so every `ρ(n)` — in particular any witness realizing `A'` or `B'` — is nonempty).
Since `A' ∩ B' = ∅` and both are nonempty, `A' ≠ B'`. Since `B'` is
`S₀`-extended-persistent, the set `N_{B'} := \{n : ρ(n) = B'\}` is infinite. Fix
any `n_0 ∈ N_{B'}` with `n_0 > n_1` (exists since `N_{B'}` is infinite hence
unbounded). Since `ρ(n_0) = B' ≠ A'`, `n_0` is not itself one of the `A'`-occurrence
indices `n_1, n_2, ...`. Since the sequence `n_1 < n_2 < ...` is infinite and
increasing without bound (there are infinitely many `A'`-occurrences), there is a
unique `j` with `n_j < n_0 < n_{j+1}` (using `n_0 > n_1`, so `n_0` is not below the
first `A'`-occurrence past the threshold either — more precisely, `j := \max\{i :
n_i < n_0\}` is well defined and finite since `n_0` exceeds only finitely many
`n_i`, and `n_0 < n_{j+1}` by maximality of `j` combined with `n_0 \neq n_{j+1}`
since `\rho(n_0)=B'\ne A'=\rho(n_{j+1})`). For this `j`, `n_j < n_0 < n_{j+1}`
gives `n_{j+1} - n_j \geq 2`. Since `N_{B'}` is infinite and each element `n_0 >
n_1$ produces (by the argument above) some `j = j(n_0)` with `n_{j+1}-n_j\geq 2`,
and distinct sufficiently-spread-out `n_0`'s can only repeat the same `j` finitely
often (each gap `(n_j,n_{j+1})` is a finite interval, so contains only finitely
many elements of `N_{B'}`), the map `n_0 \mapsto j(n_0)` from the infinite set
`N_{B'}\cap(n_1,\infty)` to `\{1,2,3,\dots\}` has infinite image (if the image were
finite, some single gap `(n_j,n_{j+1})` would have to contain infinitely many
elements of `N_{B'}`, impossible since it is a finite set of integers). Hence
infinitely many distinct `j` satisfy `n_{j+1}-n_j\geq 2`, i.e. `n_{j+1}>n_j+1`. ∎

**Consequence for the outline's Step 2.** The single-step reading (literal
`a_{n_{j+1}} = a_{n_j+1}`, so the Bounded Gap Lemma's interval
`(a_{n_j},a_{n_j}+a_1]` directly bounds `a_{n_{j+1}}`) is FALSE for infinitely many
`j` whenever a rogue pair exists at all (which is exactly the regime the Successor
Claim is needed for) — it is not merely an imprecision in wording but a genuinely
false special case if taken literally. The only correct reading is the fully
telescoped window, matching `covering-system-construction`'s Step 11 (which
telescopes explicitly): `a_{n_{j+1}} \le a_{n_j} + (n_{j+1}-n_j)\cdot a_1$ by
applying the (single-step) Bounded Gap Lemma $n_{j+1}-n_j$ times, and this
telescoped bound has NO certified finite ceiling independent of $j$, because (as
shown in Step 3 below) $n_{j+1}-n_j$ itself has no certified uniform bound.

**Independent computational confirmation.** On `a_1=4807` (the standing
`|F'|,|F''|\ge2` test seed used throughout this workspace, re-simulated fresh this
round, trial-division factorization, `N=3000`–`6000` terms, matching every prior
round's `Q=\{11,19,23\}`, `S=\{2,3,5,7,73,127\}`): for every one of the 26 sampled
`S₀`-extended-persistent types (including, e.g., type `{2,11}` with minimum gap 21,
type `{19,2,11,7}` with minimum gap 166), the minimum gap between consecutive
occurrences is $\ge 5$, never $1$ — confirming the general proof above concretely,
not merely illustrating it.

**This is a genuine, new, unconditional lemma — promotable** (`Window Resolution
Lemma`). It is small but load-bearing: it forecloses the naive single-step reading
of the outline's Step 2 as a possible shortcut, forcing any future attempt at the
Successor Claim through the correctly-scoped telescoped window — exactly the
version `covering-system-construction`'s Step 11 already (independently) uses.

### Step 2: attempting the Escape-Budget Lemma under the corrected (telescoped)
reading — a complete proof of the PREMISE, and a new proof that the premise is
informationally vacuous (Growing-Constraint Obstruction)

Fix `j` with the Successor Claim failing: `q*|a_{n_j}`, `q* \nmid a_{n_{j+1}}`.

**Proposition (the Escape-Budget Lemma's premise, proved in full, TRUE).** Every
integer `c` with `a_{n_j} < c < a_{n_{j+1}}` and `q*|c` is illegal against some
`a_i` with `i < n_{j+1}` — i.e. there is an index `i(c) < n_{j+1}` with
`\gcd(c,a_{i(c)})=1`.

*Proof.* Since the whole sequence `a_1<a_2<\cdots` is strictly increasing and
unbounded, there is a unique index `k(c)` with `a_{k(c)} < c \le a_{k(c)+1}`. Two
cases:
- If `c = a_{k(c)+1}`, then `c` is itself a term of the sequence at index
  `k(c)+1`. Since `a_{n_j} < c < a_{n_{j+1}}`, `n_j < k(c)+1 < n_{j+1}` (using that
  the sequence is strictly increasing, so index order matches value order), and
  since `n_j,n_{j+1}` are CONSECUTIVE `A'`-occurrences, `\rho(k(c)+1)\ne A'`. But
  this case does not need an illegality witness at all (c is a legitimate term
  with an ordinary type, just not of type `A'`) — it is excluded from the
  "skipped candidate" analysis below and contributes nothing to `E`; we record it
  only to note it is not a counterexample to the Proposition (the Proposition's
  claim is only about candidates NOT chosen).
- If `c < a_{k(c)+1}`, then `c` is a legal-or-illegal candidate strictly between
  the consecutive sequence terms `a_{k(c)}` and `a_{k(c)+1}` that was **not**
  chosen at step `k(c)+1`. Since `a_{k(c)+1}` is by definition (the problem's
  greedy/minimality rule) the SMALLEST integer exceeding `a_{k(c)}` that is legal
  against every one of `a_1,\dots,a_{k(c)}` (i.e. `\gcd(\cdot,a_i)>1$ for every
  `i\le k(c)`), and `c` is a smaller candidate (`a_{k(c)}<c<a_{k(c)+1}`) that was
  not chosen, `c` must fail this legality condition: there is some
  `i(c) \le k(c) < k(c)+1 \le n_{j+1}` with `\gcd(c,a_{i(c)})=1`. ∎

This proves the outline's Step 2 premise completely — it is a direct, elementary
consequence of the greedy/minimality definition of the sequence itself, requiring
no new certified machinery beyond the problem's own definition. **But, as the
following Proposition shows, this fact carries no usable information for closing
the Successor Claim.**

**Proposition (Growing-Constraint Obstruction — new, negative, proved in full).**
The witness index `i(c)` in the Proposition above can be as large as
`k(c) \le n_{j+1}-1`, i.e. it ranges, as `c` ranges over the window, over an
UNBOUNDEDLY GROWING set of indices (growing with `n_{j+1}-n_j`, which by the
Window Resolution Lemma is not uniformly bounded across `j`) — not a single fixed
index. Consequently no certified tool in this workspace's lemma stack (Free Facts,
Confined-GCD Lemma, Bounded Gap Lemma, Generalized Bounded Gap Lemma, Lemma G) can
identify, describe, or otherwise constrain `i(c)`, its type `\rho(i(c))`, or its
prime factorization `P(a_{i(c)})`, because:
(a) **Confined-GCD Lemma** only controls `\gcd(\cdot, a_{n_B})` against the ONE
FIXED index `n_B` (fixed once and for all when the rogue pair is chosen) — it
says nothing about `\gcd(c,a_i)$ for a generic index `i` in the growing range
`(n_j, n_{j+1})`, and `i(c)` need not equal `n_B` (indeed generically `i(c) > n_B$
since `n_j > n_B` by hypothesis of the successor-sequence's domain).
(b) **Free Facts** only asserts `\gcd(a_i,a_{i'})>1` for `i\ne i'$ among ACTUAL
sequence terms; it gives no information about `\gcd(c,a_i)` for `c` an arbitrary
non-term integer, and no lemma in the certified stack computes or bounds
`P(a_i)$ for `i$ ranging over an a-priori-unbounded set of indices (the
"junk-prime" phenomenon already documented for individual fixed witnesses in the
round-3 correction: e.g. `a_1=35`'s term `a_{153}=975=3\cdot5^2\cdot13$ carries an
incidental prime `13` with no certified relationship to anything).
(c) **The Bounded/Generalized Bounded Gap Lemmas** bound `a_{n+1}` in terms of
`a_n` and a chosen modulus, but say nothing about WHICH primes divide any
particular `a_i` — this is exactly the certified content of Lemma F ("Minimality
bounds magnitude, not type," round 3), now shown to reproduce itself inside this
round's quantitative window framing.

*Proof.* By the Proposition above, for `c` chosen close to the right end of the
window (i.e. `c \to a_{n_{j+1}}^-$), `k(c) \to n_{j+1}-1`, so `i(c)` ranges up to
`n_{j+1}-1`. By the Window Resolution Lemma, `n_{j+1}-n_j` is unbounded across
`j$ (no certified uniform ceiling), so as `j` ranges over indices with a failure,
the upper end of `i(c)`'s possible range, `n_{j+1}-1`, is unboundedly far from the
one FIXED index `n_B` that Confined-GCD Lemma controls, and unboundedly far from
`n_j` itself. Items (a)-(c) above are direct restatements of the certified lemmas'
own statements (Confined-GCD Lemma's scope is `\gcd(\cdot,a_{n_B})` only, by its
own certified statement; Free Facts' scope is pairs of actual sequence terms, by
its own certified statement; the Gap Lemmas bound only magnitude, by their own
certified statements) — none of them, singly or in combination, produce any
constraint on `P(a_i)` for `i$ an arbitrary index in a growing range. Hence
`i(c)` and `P(a_{i(c)})` are uncontrolled. ∎

**What this means for the Escape-Budget mechanism and the outline's own flagged
open questions, addressed directly (not smoothed over).**
1. The outline's "Escape-Budget Lemma" (the claim that a failure forces every
   `q*`-multiple in the window to be illegal) is **TRUE**, proved above — but this
   was always the EASY direction (it follows immediately from minimality, exactly
   as the outline itself flagged as "the tautological restatement that the greedy
   rule skipped it"). The hard direction — using this fact to derive a
   contradiction or a bound on the failure set `E` — is now shown to be
   **impossible with the current certified toolkit**, for the precise reason
   given above (the illegality witness pool is unboundedly growing, not fixed).
2. This directly and NEGATIVELY answers the outline's own flagged open question
   ("Whether the 'specific earlier illegality witness' pool is itself
   finite/bounded — needed for the Summability corollary"): it is **not**
   bounded — proved above, not merely suspected. Consequently the Summability
   corollary the outline hoped for cannot be built on this premise as stated; any
   future attempt would need a fundamentally different source of control over
   `P(a_i)` for generic intermediate `i`, which per Lemma I's four-tool diagnosis
   (round 6) and this round's fresh confirmation, is not supplied by anything
   currently certified.
3. The outline's flagged circularity risk ("could unpack into needing
   `S₀`-sufficiency, equivalent to (†)") is **avoided but for a worse reason**:
   the mechanism does not even reach the point of needing full `S₀`-sufficiency —
   it dies one step earlier, at the more basic fact that NO certified tool
   controls a generic intermediate term's factorization at all, circular or not.

### Step 3: the secondary Return-Time Boundedness question — genuinely open,
empirically not obviously true, reported honestly (not needed for the negative
result above, but relevant context for future rounds)

Independent of the Growing-Constraint Obstruction (which kills the mechanism
outright, regardless of whether gaps are bounded), it is worth recording precisely
that the auxiliary quantity `covering-system-construction`'s Step 11.5 flagged —
whether `n_{j+1}-n_j` is even uniformly bounded across `j` for a fixed
extended-persistent type ("Return-Time Boundedness," RTB) — is **not established
by any certified lemma** (Persistent-Type Pigeonhole and its Extended version give
only infinitude of occurrences via the infinite pigeonhole principle, never a rate
or gap bound), and fresh computation this round gives no positive evidence for it
either:

On `a_1=4807`, tracking the sparser extended-persistent type `\{2,11,19,7\}`
(minimum-count type from the round-10 sample, `S_0=\{2,3,5,7,11,19,23,73,127\}`):

| sampled range `N` | occurrence count | max observed gap |
|---|---|---|
| 1500 | 4 | 502 |
| 2000 | 6 | 503 |
| 3000 | 10 | 503 |
| 4000 | 11 | 503 |
| 5000 | 15 | 670 |
| 6000 | 18 | 670 |

The max observed gap strictly increases as the sampled range grows (503 → 670
between `N=4000` and `N=5000`), giving no sign of stabilizing at a fixed ceiling
within the tested range. This is not a proof that RTB is false (a longer run could
still reveal stabilization), but it is honest evidence AGAINST assuming RTB for
free, and it independently corroborates why no certified lemma in this workspace
currently supplies it: doing so would require a density/frequency argument for a
SPECIFIC persistent type, which the certified Persistent-Type Pigeonhole
(`persistent-type-pigeonhole.md`) and its extended-type version (Lemma C /
`extended-persistent-type-pigeonhole.md`) explicitly do not provide (their proofs
use only the infinite pigeonhole principle: SOME type occurs infinitely often,
with zero rate information). This is recorded as a second, independent reason
(besides the Growing-Constraint Obstruction) that the telescoped window in Step 2
cannot be turned into a genuinely quantitative (numeric-ceiling) tool without a
fundamentally new ingredient — RTB is not merely unproved, it is not even known
to be true, and is not needed to be resolved to reach the (already sufficient)
negative conclusion of Step 2 above.

### Conclusion of the round-10 attempt, stated without overclaiming

The dispatched Escape-Budget attack was carried out to completion, resolving the
outline-reviewer's flagged imprecision first (Window Resolution Lemma — proved,
promotable, unconditional) and then proving BOTH halves of the Escape-Budget
mechanism explicitly: its premise is true (Proposition, Step 2) but the resulting
information is provably unusable with the current certified toolkit (Growing-
Constraint Obstruction, Step 2) — a clean, complete negative result, not a stall
or an unexamined dead end. This is the tenth distinct mechanism (after Lemma I's
four, round 7's Blocking-Data Bridging, round 8's Fixed-Witness Divisor-Chain,
round 9's covering-system Recruitment-Budget Lemma and this approach's own
Successor-Claim qualitative attempt, and the cofinite-window-capacity-bound's
counting-bound stall) shown dead in this workspace, and the first to fail via a
genuinely quantitative/telescoped-window route rather than a qualitative
branch-analysis route — reinforcing, via an independent proof technique, the same
underlying diagnosis Lemma I first identified: **the missing ingredient is a
source of information about an arbitrary (not singly-fixed) earlier term's
factorization; no composition of Free Facts, the Gap Lemmas, Confined-GCD, or
infinite pigeonhole supplies one.** FAH and Symmetric FAH (equivalently, the
Successor Claim, equivalently Cofinite FAH via the certified Successor-Transport
Reduction Lemma) remain open.

### Updated key lemmas (round 10)
- **Window Resolution Lemma** — new, proved in full above, unconditional: for any
  rogue pair, infinitely many consecutive-`A'`-occurrence gaps exceed 1, so the
  Successor Claim's window must be read as the fully telescoped interval, never a
  single sequence-step. Small but genuinely new and reusable; forecloses a
  specific incorrect simplification any future builder might otherwise make.
  **Promotable.**
- **Growing-Constraint Obstruction** — new, proved in full above (Step 2): the
  Escape-Budget mechanism's premise is true but its illegality-witness pool is
  provably unbounded (grows with the window length, which by the Window
  Resolution Lemma and the empirical RTB data has no known ceiling), so no
  certified tool can exploit it. Matching the precedent set for Lemma F (round 3)
  and Lemma I (round 6) — this is a diagnostic about what the CURRENT certified
  lemma stack can and cannot do, not a portable fact independent of which lemmas
  are certified in the future — so, per that precedent, it is recorded here in
  full (with a complete, checked proof) but **not separately certified as a
  standalone shared lemma file**; it is exactly the kind of finding future rounds
  need to route around by supplying a genuinely new source of intermediate-term
  factorization control, not by recombining the existing four tools.

### ROUND 11 (outline-review pre-build check): Forced-Escape Blocking Construction
proposed, found magnitude-doomed as literally specified — 13th mechanism, cut
before build

The round-11 outliner proposed reviving this approach with a new **Forced-Escape
Blocking Construction**: CRT-glue a competitor `c` matching `a_n`'s S₀-signature
exactly (`c ≡ a_n (mod p)` for every `p ∈ S₀`) while forcing `q*|c`, using modulus
`M := ∏_{p∈S₀} p`, taking `c` as the representative of the CRT class in
`(a_{n-1}, a_{n-1}+q*M]`. The outline-reviewer ran this construction numerically
(seed `a_1=4807`, rogue pair `A'={3,5,19}` vs `B'={2,11}`, `q*=17`,
`S₀={2,3,5,7,11,19,23,73,127}`, `M=∏S₀≈9.36×10⁹`, `q*M≈1.59×10¹¹`) on all three
sampled `A'`-occurrences (`n=561,1114,2223`): **in all three, `c ≥ a_n` by roughly
eight orders of magnitude** — the actual local gap `a_n − a_{n-1}` sampled at
`15, 3, 19`, versus `q*M ≈ 1.59×10¹¹`. This is not a sampling artifact: `q*M` is a
product of (currently) 9 primes with no relationship to the local gap size, which
by the certified Bounded/Generalized Bounded Gap Lemma is controlled only by
`a_1` and the index difference `n−(n−1)=1`, entirely independent of `|S₀|`. As
`S₀` grows with further recruitment rounds, `M` (and hence `q*M`) only grows,
while the local gap stays of the same order — so this specific failure mode gets
*worse*, not better, at later recruitment stages. **Conclusion: the construction's
competitor `c` structurally cannot land inside the informative window
`(a_{n-1}, a_n)`; Lemma K's dichotomy therefore never reaches its useful branch
(b), because that branch requires `a_{n-1} < c < a_n`, which this construction
essentially never achieves once `|S₀| ≥ 2`.** This is a genuine, previously
untried construction (confirmed novel and correctly scoped as blocking-index
extraction, not a full-legality-competitor construction of the kind the
Minimality Tautology Lemma disqualifies) but it fails for an orthogonal,
elementary reason (magnitude, not legality) — a clean new negative result,
recorded here as the **CRT Magnitude Obstruction**: any competitor construction
that CRT-glues a full S₀-signature match (modulus `Θ(∏S₀)`) cannot be expected to
land within the local window `(a_{n-1},a_n)` (of size controlled only by `a_1`),
so this specific construction shape is retired. This is the workspace's
**13th** confirmed-dead FAH mechanism.

**Important correction to the outline's own "Risk 2" discussion.** The outline
flagged, as "the most promising sub-case to check computationally FIRST": *if `c`
turns out fully legal against every `j<n` AND `c<a_n`, this directly contradicts
`a_n`'s minimality and would PROVE Cofinite FAH directly.* This sub-case is **not
merely unlikely — it is a logical impossibility, unconditionally, by the already-
certified Minimality Tautology Lemma's Corollary** (`lemmas/minimality-tautology-
lemma.md`): there is NO integer `c` with `a_{n-1}<c<a_n` that is fully legal
against every `a_1,...,a_{n-1}`, for ANY `n`, by the bare definition of `a_n` as
the minimum of the legal set. So this branch can never fire for any construction
whatsoever, this one included; it was never a promising thing to check
computationally, and the numeric check above (which independently also shows
`c` essentially never even lands below `a_n` at all) makes the point doubly moot.
Future rounds should read the Minimality Tautology Lemma as ruling this branch
out a priori, not as a live possibility worth testing.

**Status of this approach after round 11.** The specific Forced-Escape
Blocking Construction (full-S₀-modulus CRT glue) is dead, for a magnitude reason
independent of the (still-unresolved, and now moot for this construction) branch-
(b) factorization analysis. The approach's live, unconditional content
(Generalized Bounded Gap fact, Window Resolution Lemma, Growing-Constraint
Obstruction, and now the CRT Magnitude Obstruction) remains valid and reusable;
no new mechanism is open here as of round 11. A future revival of the CRT-glue
idea would need a fundamentally different modulus/window design that keeps the
candidate within `O(local gap)` of `a_n` while still forcing `q*|c` — no such
design is known, and it is not obvious one exists, since forcing agreement with
even a handful of independent primes already produces a modulus far exceeding
the local gap (checked also with the smaller modulus `M=a_1` alone: `q*a_1 =
17·4807 = 81719`, still ≫ the observed local gaps of `3`–`19`).

## ROUND 11 BUILD — searching for a magnitude-controlled fix (weaker,
partial-signature matching): genuinely attempted, closed as also dead
(Minimal-Modulus Generalization); rest of the approach's content re-audited
and confirmed an accurate, complete record

### The fix attempted: match only PART of S₀, not all of it

The task this round was to determine whether the Forced-Escape Blocking
Construction can be rescued by forcing the competitor `c` to match only a
carefully chosen SUBSET of `S₀` (rather than the full `S₀`-signature that
produced the ≈8-order-of-magnitude overshoot) while still forcing `q*|c` and
still yielding an *informative* illegality witness (one whose blocking prime
lies outside `S₀`, ideally in `F'`/`F''`). Two independent design points were
tested, both genuinely new relative to anything in the workspace's prior 13
dead mechanisms (round 11's own full-`S₀` version included), and both fail —
for two DIFFERENT, individually decisive reasons, not one repeated complaint.

**Design point 1 — the cheapest possible legality-guaranteeing modulus (match
all of `Q`, not all of `S₀`).** This is not new data collection; it is exactly
the smaller-modulus check the round-11 outline-reviewer already ran and
recorded above (`M = a_1`, giving `q*·a_1 = 81719`) — reconfirmed here as
already dead, and now generalized: `Q`, not `S₀ \ Q`, is the *provably minimal*
set of primes a legality-guaranteeing modulus must be divisible by. This is not
a matter of choosing a smaller ad hoc subset — it follows directly from the
certified proof of Lemma A (Generalized Bounded Gap Lemma, above): the
argument that a modulus-`c` candidate is legal against *every* earlier term
`a_1,...,a_{n-1}` uses, for `i=1`, that some prime of `Q` divides both `c` and
`a_1` (needs `c` divisible by that specific `Q`-prime), and for `i≥2`, Free
Facts only guarantees `a_i` shares SOME (a priori unidentified) prime with
`a_1` — so to be sure `c` shares that same prime with `a_i`, `c` must be
divisible by **every** prime of `Q` simultaneously, not just one. There is no
cheaper unconditional-legality construction available in the certified
toolkit; `Q` is already the minimal set for this purpose, so `M=a_1` (or its
squarefree kernel `rad(a_1)` if smaller) is the floor, and this floor was
already shown dead in the round-11 outline-review pass.

**Design point 2 — genuinely new this round: drop the unconditional-legality
requirement, match only a SINGLE prime of `Q` plus `q*`.** This abandons the
"provably safe against everything" property in exchange for a much smaller
modulus, on the hope that even without a legality *guarantee*, the resulting
candidate might still land in the window often enough, with the actual
(empirical) blocking witness carrying new information. Concretely: for each
`p ∈ Q`, let `c_p(n) :=` the smallest multiple of `p·q*` exceeding `a_{n-1}`.
Tested computationally (fresh script this round, `/tmp/round11_check.py`,
independent of the outline-reviewer's — same `a_1=4807`, `S₀`, rogue pair
`A'={3,5,19}`, `B'={2,11}`, `q*=17` data, re-derived from scratch, generator
matches all prior rounds' figures exactly):

- Minimal single-prime-of-`Q` modulus: `p·q* ∈ {187, 323, 391}` for
  `p ∈ Q = {11,19,23}` (using `p=11` gives the cheapest, `187`).
- Local gaps `a_n − a_{n-1}` at the three sampled `A'`-occurrences past `n_B`
  (`n=561,1114,2223`): `15, 3, 19` — none large enough for `c_{11}(n)` to land
  inside `(a_{n-1},a_n)`, since `187 ≫` every one of these gaps.
- Broadened the check across **every** consecutive gap in the sequence up to
  `N=2500` (2499 gaps total, not just the 3 sampled `A'`-occurrences): maximum
  observed gap is **38**, mean **17.4**, minimum **2**. **Zero of 2499 gaps
  (0/2499) reach the minimal single-prime modulus 187.** So even the cheapest
  possible partial-signature construction — a single prime of `Q` plus `q*` —
  essentially never lands inside the local window anywhere in the tested
  range, not merely at the three sampled rogue occurrences.

**Why this is not merely "still empirically too big, try smaller still"—there
is a hard floor, and going below it forfeits the argument's entire point.**
Any modulus smaller than `p·q*` for the smallest available `p ∈ Q ∪ (S₀\Q)`
either (i) is not a multiple of `q*` at all, so it cannot force the target
prime `q*|c` (the entire purpose of the construction), or (ii) is not a
multiple of any prime shared with `a_1`, so `c` need not even be legal against
`a_1` itself — a candidate with `\gcd(c,a_1)=1` is illegal for a reason with
**zero connection** to the rogue pair, the target prime `q*`, or `S₀` at all
(it is exactly the same "generic junk-prime" failure mode Lemma K's Experiment
2 already found dominates: >99% of blocking witnesses are `S₀`-primes, mostly
from `a_1` itself, carrying no `F'`/`F''` information). So there is no room to
shrink the modulus further without abandoning the construction's whole
purpose — `187` (or the seed-specific analogue `min(Q)·q*`) is a genuine floor
for this design, not an arbitrary choice that a smarter tweak could beat.

**Conclusion: there is no magnitude/informativeness sweet spot — the two
requirements pull in strictly opposite directions, with no overlap found or
plausible.** Making the construction *informative* (branch (b)'s blocking
prime forced outside `S₀`) requires unconditional legality against every
earlier term, which — per Lemma A's own certified proof — requires a modulus
divisible by all of `Q` (design point 1), already shown dead by ≈8 (or, at the
cheapest, ≈2) orders of magnitude. Making the construction *cheap* enough to
plausibly land in the window (design point 2) sacrifices the legality
guarantee, so any resulting failure is empirically dominated by uninformative
`S₀`-junk blocking (matching this round's independent math-explorer's Lemma K
findings exactly) — and even so, the cheapest such design still lands
**0/2499** times in the tested range. No parameter in between (partial subsets
of `S₀ \ Q`, weighted/adaptive moduli, etc.) escapes this dichotomy, because
the dichotomy is forced by Lemma A's proof structure itself, not by the
particular numbers of this one seed — any nonempty proper subset of `Q` used
in the modulus fails to guarantee legality against a generic earlier term for
the same reason design point 2 does (Free Facts gives no control over WHICH
`Q`-prime a given `a_i` shares with `a_1`), so the "all of `Q` or bust"
dichotomy is a structural consequence of the certified lemma set, not an
artifact of under-searching moduli.

**This is recorded as a completion of, not a new addition to, the CRT
Magnitude Obstruction found earlier this round: the obstruction is generic to
the whole partial-signature-matching family, not specific to the literal
full-`S₀` construction.** No further variant of this construction family
should be attempted by a future builder without first identifying a
certified mechanism that decouples "forcing a specific prime to divide `c`"
from "guaranteeing `c`'s legality against every earlier term" — no such
mechanism exists anywhere in the current certified lemma stack (confirmed by
this round's independent audit of Free Facts, the Gap Lemmas, Confined-GCD,
and Lemma G — none of them supply legality control cheaper than a full-`Q`
modulus).

### Status of route (a) vs (b) per this round's dispatch

Per this round's dispatch, both routes were genuinely attempted: (a) a
weaker, partial-signature-matching construction was designed, computed, and
found to fail for a structural (not merely numerical) reason, documented
above; (b) as a result, the honest record is that this approach remains
**stalled at the same crux** (FAH / Symmetric FAH / the Successor Claim,
equivalently Cofinite FAH) as every sibling approach in this workspace, now
with a **14th** confirmed-dead mechanism (the partial-signature family, a
genuine generalization of round 11's 13th). No new open sub-question is left
dangling by this attempt — the dichotomy proof above is unconditional and
closes the entire CRT-glue-family question, not just this seed's instance.

### Re-audit of the rest of the approach (this round), confirming no drift

Re-read the full approach file top-to-bottom this round to confirm accuracy
before finalizing: the `|Q|=1` special case (fully resolved, no gap), the
certified unconditional lemmas (Free Facts, Bounded Gap Lemma, Generalized
Bounded Gap Lemma / Lemma A, Persistent-Type Pigeonhole, Bounded Witness
Lemma, Single-Witness-Prime Pigeonhole Refinement, Extended Persistent-Type
Pigeonhole / Lemma C, Canonical-Refinement Lemma, `F_A∩F_B≠∅`, Lemma G,
Window Resolution Lemma), and the certified-given-Cofinite-FAH finish
(CRT + cyclic-pigeonhole, imported from `covering-system-construction` Step 5
and unchanged since round 1) are all still accurate and still the correct
"current best" — no correction is needed to any of them this round. The
approach's full chain of reasoning, from Free Facts through the Finite Core
Theorem to the reduction "(†) ⟺ Cofinite FAH ⟺ Symmetric FAH" (established
across rounds 5–9, most recently the Cofinite Sufficiency Lemma and
Successor-Transport Reduction Lemma), remains the whole-problem finish
**conditional on** Cofinite FAH, which is the sole open gap. Fourteen
mechanisms (this workspace's cumulative count, all approaches combined) are
now confirmed dead as routes to that one hypothesis; none has produced a
counterexample. This round's contribution narrows the search space further
(the entire CRT-glue/competitor-construction family, in every modulus
variant, is now closed) without finding a proof.

### Key lemmas (round 11 addition)
- **Minimal-Modulus Generalization of the CRT Magnitude Obstruction** — new,
  proved in full above: any partial-signature CRT-glue construction (forcing
  `q*|c` plus matching any subset of `S₀`) either (i) fails to guarantee `c`'s
  legality, in which case its blocking witness is empirically dominated by
  uninformative `S₀`-junk (matching this round's independent math-explorer
  Lemma K findings), or (ii) requires the full-`Q` modulus (the certified
  minimum, per Lemma A's proof), which — per the round-11 outline-review's
  original CRT Magnitude Obstruction, reconfirmed here at the cheapest
  possible scale (`0/2499` gaps reach even the single-prime-of-`Q` floor of
  `187`) — never lands inside the local window in the tested range. Diagnostic
  about the current certified toolkit's limits (matching the Lemma F / Lemma I
  precedent); **not separately certified as a standalone shared lemma file**
  (same rationale as those precedents — it documents what current tools
  cannot do, not a portable fact independent of future certifications).

## ROUND 13: the No-Restart Lemma (defensive/bookkeeping, certified)

**Task for this round, per dispatch.** Formalize and certify, as a standing lemma,
the observation that "restarting" the greedy process at a later term `a_{n_0}`
(treating it as if it were a fresh seed `a_1' := a_{n_0}`) is a structurally invalid
proof move: the true continuation of the sequence from index `n_0` onward generally
diverges from the fresh-restart sequence, because the restart forgets the
constraints imposed by the earlier terms `a_1,...,a_{n_0-1}`. This is explicitly
scoped as **not** a new attempt at FAH/Symmetric FAH/gap (†) — the crux remains where
round 12 left it, on its eighth consecutive open round. This section records the
full general proof; the certified statement lives in
`lemmas/no-restart-lemma.md` and is reproduced here for completeness.

### Setup

Let `(a_n)` be the problem's sequence: `a_1 > 1`, and for `n ≥ 1`,
`a_{n+1} := min{c > a_n : gcd(c,a_i) > 1 for every i = 1,...,n}` (well-definedness
already certified via Free Facts + Bounded Gap Lemma). Fix `n_0 ≥ 2`. Define the
**restarted sequence** `(b_k)` by `b_1 := a_{n_0}` and, for `k ≥ 1`,
`b_{k+1} := min{c > b_k : gcd(c,b_i) > 1 for every i = 1,...,k}` — i.e. exactly the
sequence the recursion generates if `b_1 = a_{n_0}` is treated as a brand-new seed,
forgetting `a_1,...,a_{n_0-1}`.

### The unconditional monotonicity inequality

For any candidate `c` and index sets `I ⊆ J`, legality against the larger set `J`
implies legality against the smaller set `I` (legality is a conjunction of the
individual conditions `gcd(c,a_i)>1`, and dropping conjuncts can only weaken the
requirement). Applying this with `J = {1,...,n_0}` (the true process's full
constraint set at step `n_0 → n_0+1`) and `I = {n_0}` (the restarted process's sole
constraint at its first step) gives, since every `c` legal against `J` is legal
against `I`:
```
{c > a_{n_0} : legal against {1,...,n_0}} ⊆ {c > a_{n_0} : legal against {n_0}}.
```
Both sets are nonempty (the left by the Bounded Gap Lemma, the right because `b_1`'s
own recursion is well-defined by the identical existence argument with a
single-element history). Taking minima of a subset vs. its superset reverses the
inequality: `b_2 = min(RHS) ≤ min(LHS) = a_{n_0+1}`. **This holds for every `n_0 ≥
2`, unconditionally, with no hypothesis.**

### The generic strictness condition

Strictness `b_2 < a_{n_0+1}` cannot come from any hypothesis on `a_{n_0+1}` itself
(it is by definition legal against the full history, so no earlier constraint can
exclude it). It comes instead from the *interval* `(a_{n_0}, a_{n_0+1})`: whenever
there exist `j ∈ {1,...,n_0-1}` and an integer `c` with `a_{n_0} < c < a_{n_0+1}`,
`gcd(c,a_{n_0}) > 1`, and `gcd(c,a_j) = 1` (hypothesis (H')), then `c` is a member of
the restarted process's candidate set with `c < a_{n_0+1}`, forcing `b_2 ≤ c <
a_{n_0+1}` strictly. This is the generic case, not a corner case: it holds precisely
whenever the true process's minimality at step `n_0+1` was genuinely enforced with
help from some pre-`n_0` term ruling out an integer in that interval that `a_{n_0}`
alone does not rule out — exactly the situation any early term with `a_j > 1`
generically creates, since a fixed `a_j > 1` has infinitely many integers coprime to
it, and generically some land in any given window.

### Worked example (independently re-verified this round)

`a_1 = 15`: true sequence `15, 18, 20, 24, 30, 36, 40, 42, 45, 48, 50, 54, ...`.
Restarting at `n_0 = 5` (`b_1 = a_5 = 30`) gives `30, 32, 34, 36, 38, 40, 42, 44, ...`
— diverging immediately, `b_2 = 32 ≠ 36 = a_6`. Witness for (H'): `j = 1`, `c = 32`:
`gcd(32, 30) = 2 > 1` (legal for the restarted process's sole constraint) but
`gcd(32, 15) = 1` (illegal for the true process, blocked by the forgotten early term
`a_1 = 15`). This was reproduced by a fresh direct Python simulation this round
(trial factorization / greedy search, `a_1 = 15`, 12 true terms and 8 restarted
terms), matching exactly.

### Degenerate case `n_0 = 1`

If `n_0 = 1`, the "earlier history" `{a_1,...,a_{n_0-1}} = ∅` is empty — `b_1 = a_1`
already carries the true process's own (empty) constraint set at the start, so the
two recursions are literally identical (`b_k = a_k` for all `k`) by construction.
This is why the Lemma's hypothesis requires `n_0 ≥ 2`: only from `n_0 = 2` onward is
there a nonempty forgotten history.

### Corollary: invalidity of restart-based induction

Whenever (H') holds for `n_0` (the generic case), `(b_k)` and `(a_{n_0+k-1})` already
differ at the second term, so they are not the same sequence and any conclusion
proved about `(b_k)` alone (e.g. periodicity parameters determined solely by `b_1 =
a_{n_0}`) need not transfer to the true tail `(a_n)_{n ≥ n_0}`. Consequently: any
proof strategy that treats a later term `a_{n_0}` as a fresh, independent seed of a
"smaller instance of the same problem" — an induction on `ω(a_1)` via prime removal
followed by a fresh restart, or a minimal-counterexample descent that swaps the true
tail for a freshly-seeded continuation — is invalid unless the full original
constraint set `{a_1,...,a_{n_0-1}}` is carried forward explicitly, at which point no
genuine dimension reduction has actually occurred (the "restarted" object still
depends on the full original history). This retroactively explains, with a single
general, citable fact, why round 8's `seed-coupling-induction` (Seed-Coupling Lemma,
falsified by an independent computational counterexample) and the analogous framing
issues flagged in rounds 3 and 5 all failed: each was, in substance, an
unacknowledged instance of exactly this invalid move.

### Scope discipline (explicit, per dispatch)

This section proves a fact about the greedy recursion's history-dependence only. It
makes **no claim whatsoever** about FAH, Symmetric FAH, gap (†), persistent types, or
divisor classes, and does not narrow or widen the main crux in any way. Its sole
purpose is defensive: to give future rounds a single certified citation instead of
re-discovering (and re-falsifying) restart-based arguments from scratch, as has now
happened independently three times (rounds 3, 5, 8) in this workspace.

### Round 13 verdict

**Certified this round:** `lemmas/no-restart-lemma.md` (unconditional, no gaps: the
monotonicity inequality `b_2 ≤ a_{n_0+1}` is proved for every `n_0 ≥ 2` with no
hypothesis; the strict-divergence condition (H') is stated precisely and shown to be
the generic mechanism, not asserted without proof; the sole degenerate case `n_0=1`
is identified and correctly excluded; the worked example is independently
re-verified by direct computation). Status for this approach remains **partial**
overall (the main crux, FAH/Symmetric FAH, is untouched by this round's dispatched
task, exactly as scoped).
