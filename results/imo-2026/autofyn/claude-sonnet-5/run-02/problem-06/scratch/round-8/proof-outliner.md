## imo-2026-06

Context: FAH/Symmetric FAH (equivalently, per covering-system-construction Step 8.7,
"Joint FAH" for the canonical prime q*:=min(F'∩F'')) has been the sole open crux for
3 straight rounds (6,7,8). Per CLAUDE.md's plateau rule, this round puts a genuinely
different top-level framing on the table (seed-coupling-induction) in addition to two
scoped revisions of the FAH mechanism itself (using this round's explorer findings),
plus the n=1 secondary gap gets an explicit continuation slot.

Rejected as insufficient (density lens, cheap-kill, do not dispatch a builder on this):
any mechanism whose deliverable is a bare density-1 (not cofinite) divisibility
statement about type-A terms divisible by q — FAH/Symmetric FAH are cofinite claims,
a density-1 set can still miss infinitely many terms, so this cannot close the gap by
itself. Also rejected: aimo-0680's literal "upgrade infinitely-often to everywhere via
an exact identity" template as a direct transplant — it depends on an index-divisibility
identity (n | f^n(m)-m) this problem has no analog of; only its top-level SHAPE could
matter, and no substitute identity was found this round, so it is not proposed as its
own approach (would just be a restatement of "find a new mechanism," not a concrete
skeleton).

---

covering-system-construction: revise
Target: there exist positive integers T, L with a_{n+T}=a_n+L for every positive
integer n (the whole problem, both the main claim and the n=1 literal-periodicity
refinement).
Technique: covering-system/CRT finish (unchanged) + a NEW mechanism for Joint FAH —
the Fixed-Witness Divisor-Chain, scoped specifically to Lemma-G rogue-pair witnesses
(mechanism-explorer's opening 1, adapted from crux aimo-0477's "d_n=gcd(a_1,a_n),
bounded divisor lattice" shape, itself scoped down from a blanket claim the explorer
falsified) — plus continuing Step 9.3 on the n=1 gap.
Skeleton:
  1. Reuse unconditionally: Free Facts, Bounded/Generalized Bounded Gap Lemmas,
     Persistent-Type Pigeonhole, Finite Core Theorem, Generalized Bounded Witness
     Lemma (S₀-level) + Recruitment Corollary, Extended Persistent-Type Pigeonhole,
     Canonical-Refinement Lemma, F_A∩F_B≠∅, Projection Lemma, Collateral-Safety
     Theorem — by the certified lemma files in results/imo-2026-06/lemmas/. These
     already reduce (†) exactly to base-type-pair-level termination, in turn reduced
     (Step 8.5/8.7) to Joint FAH: for a rogue pair (A',B') with canonical earliest
     witnesses n_A<n_B and q* := min(F'∩F''), does q* divide EVERY sufficiently large
     term of type A' AND of type B'.
  2. NEW Step 8.9 — Fixed-Witness Divisor-Chain object. Fix the earliest witness
     integer a_{n_A} (NOT the abstract prime alone). For every later A'-type
     occurrence n>n_A define d_n := gcd(a_{n_A}, a_n), a divisor of the FIXED integer
     a_{n_A}, hence one of only finitely many values (Divisor analysis,
     knowledge_base.md Number Theory). Do NOT claim d_n is constant / equal to
     a_{n_A} — the mechanism-explorer FALSIFIED that blanket claim on generic
     persistent types (e.g. a_1=175's type {2,3,5} shows non-constant gcd) even
     though it held cleanly for the actual recruited-prime-carrying types. Scope the
     claim to: "q* | d_n for all but finitely many A'-type n."
  3. Key Lemma — Exception Finiteness via Fixed-Witness Pigeonhole (the genuinely new,
     open content; mechanism: combine the Divisor-Restricted Pigeonhole (Lemma J) with
     the fixed-witness object). Suppose q* ∤ a_n for infinitely many A'-type
     occurrences n. By Free Facts, each such a_n shares SOME prime with a_{n_A}, i.e.
     d_n>1 for all of them, and d_n ranges over the FINITE set of divisors of a_{n_A}
     not divisible by q*. Pigeonhole (finitely many values, infinitely many n) forces
     an infinite subsequence with a CONSTANT gcd value d≠q*·(anything), hence a
     constant shared prime r | d, r≠q*, dividing infinitely many A'-type terms. Apply
     the Generalized Bounded Witness Lemma's Corollary to this r as if it were itself
     a candidate recruited prime for the SAME rogue pair (A',B'): either (a) r ∈ S₀
     already, contradicting that (A',B') is a rogue (not-yet-safe) pair at S₀ per
     Collateral-Safety's characterization, or (b) r ∉ S₀, so r is a genuine
     alternative candidate in F'∩F'' — but then canonicality (q* := MIN(F'∩F'')) does
     not immediately force r=q* unless r<q* is ruled out; this sub-step (ruling out a
     smaller alternative candidate r via the actual definition of F', F'' as sets of
     Lemma-G-eligible primes, not just any shared prime) is the precise remaining gap
     — flagged explicitly, not glossed.
  4. Given the Key Lemma (Joint FAH via cofinite q*-divisibility on both sides,
     Symmetric case by Step 8.8's side-agnosticity), Step 8.5's corollary gives
     base-type-pair-level termination in exactly one further recruitment round; (†)
     holds; Step 5's CRT/cyclic-pigeonhole finish gives explicit T, L (T = number of
     eligible residues mod L, L = ∏_{p∈S₀} p).
  5. Secondary gap (n=1 literal periodicity) — continue Step 9.3. Reuse the certified
     Exact-Equality Reduction Lemma (periodicity from n=1 iff finitely many explicit
     equalities a_{i+T}=a_i+L for i=1,...,N₀−1) and Non-Automaticity of Prefix Folding
     (rules out naive period-rescaling). NEW attempt: verify the N₀−1 early equalities
     directly by strong induction from i=1, using that Free Facts + Bounded Gap Lemma
     hold literally from n=1 (not just eventually) — show each small i's S₀-signature
     already lies in the "eligible residue" set G defining T (the set G is a property
     of the S₀-signature mod L, which is meaningful for small n too, not only in the
     persistent regime), so the finitely many equalities reduce to a finite direct
     computation rather than an asymptotic argument.
Key lemmas (claim + mechanism):
  - Exception Finiteness (Step 3 above) — because a_{n_A} has finitely many divisors
    (Divisor analysis) and Free Facts forces every A'-occurrence to share one of them,
    so infinitely many exceptions would pigeonhole into a genuine alternative
    recruited-prime candidate, which Collateral-Safety's rogue-pair characterization
    either places in S₀ (contradiction) or leaves as an open canonicality question
    (the actual remaining gap).
  - Small-index eligibility (Step 5) — because G is defined purely by S₀-signature mod
    L, a static congruence condition with no dependence on "eventually," so it can in
    principle be checked directly for i=1,...,N₀−1 rather than derived asymptotically.
Open gaps: the canonicality sub-step in Step 3 (ruling out r<q* as an alternative
Joint-FAH candidate — this is the precise place the mechanism could still fail); the
direct verification in Step 5 (whether small-i S₀-signatures actually land in G, not
yet checked on any seed).
Cases to cover: |F'∩F''| = 1 vs ≥2 (the a_1=4807 case) must both be handled by the
canonicality sub-step in Step 3 — do not assume |F'∩F''|=1.
Watch out for: do NOT re-derive the blanket "a_{n_A} | a_n" claim (falsified by the
mechanism explorer on generic persistent types on a_1=175/209) — the scoped claim is
only about q*-divisibility of d_n, not equality of d_n to a_{n_A}.

---

greedy-exchange-cost-potential: revise
Target: same as above (whole problem).
Technique: aimo-0611-style occurrence-order induction — induct on the ORDERED
OCCURRENCE INDEX k of a single fixed extended-persistent type A' (not on
recruitment/refinement stage, which is what all four Lemma-I-diagnosed dead
mechanisms and the dead scalar-well-ordering-lock-in used). This sidesteps the
certified Witness Discontinuity Obstruction, which specifically concerns
continuity of witness selection ACROSS recruitment stages — here the type A' never
changes and the core S₀ is held fixed throughout the induction; only k grows.
Skeleton:
  1. Reuse: Free Facts, Lemma G (Extended Earliest-Witness Intersection), Critical
     Prime Dichotomy (Lemma H), Divisor-Restricted Pigeonhole (Lemma J).
  2. Fix a rogue pair (A',B'), Lemma-G prime q for this pair, and enumerate ALL
     occurrences of extended type A' in increasing index order m_1<m_2<m_3<...
     (m_1 = n_A, the canonical witness).
  3. NEW Claim (Occurrence-Order Induction): q | a_{m_k} for all k ≥ some fixed k_0.
     Base case: q | a_{m_1} directly from Lemma G's own construction.
     Inductive step: assume q | a_{m_1},...,a_{m_k}. Consider a_{m_{k+1}}. By Free
     Facts, gcd(a_{m_{k+1}}, a_{m_j}) > 1 for every j ≤ k. If q ∤ a_{m_{k+1}}, then for
     each j the shared prime is some r_j ≠ q. By Divisor-Restricted Pigeonhole
     (Lemma J), the possible values of r_j are bounded (divisors of a_{m_{k+1}}
     itself, a FIXED finite integer for this step of the induction) — since k can be
     taken arbitrarily large (infinitely many occurrences, Extended Persistent-Type
     Pigeonhole), for large enough k pigeonhole forces some SINGLE prime r ≠ q shared
     with infinitely many earlier a_{m_j}. This r is then itself an alternative
     Lemma-G-style candidate for the same rogue pair. Rule this out via: either r ∈ S₀
     (contradicts rogue-pair status by Collateral-Safety) or r ∉ S₀ and canonicality
     (q := q* = min(F'∩F'')) must force r ≥ q or r = q — this is the SAME precise
     open sub-step as in the sibling approach's Step 3 (canonicality vs. an
     alternative candidate), approached here from the occurrence-order-induction
     angle instead of the fixed-witness-divisor-chain angle. Both siblings converge on
     needing this one canonicality lemma; whichever proves it first, the other should
     import it (per the workspace's existing convention of not duplicating a shared
     sub-lemma across sibling files).
  4. Symmetric argument (Step 8.8's side-agnosticity, already established) gives
     Symmetric FAH once FAH is proved this way.
  5. Given Joint FAH, import covering-system-construction's Step 8.5 finish verbatim
     (do not re-derive; cite).
Key lemmas (claim + mechanism):
  - Occurrence-Order Induction step (Step 3) — because Free Facts forces a shared
    prime with EVERY earlier same-type occurrence, not just one, so an infinite
    supply of "escape primes" r_j would have to collapse (by finiteness of divisors
    of any single a_{m_{k+1}}) to one fixed alternative prime, which is exactly the
    kind of existential-to-universal promotion Lemma I's diagnosis says needs a new
    ingredient — the new ingredient here is anchoring on ONE FIXED later integer
    a_{m_{k+1}}'s own finite divisor set, not the four already-diagnosed-insufficient
    tools alone.
Open gaps: same canonicality sub-step as covering-system-construction's Step 3 (do
NOT re-derive independently — coordinate with that approach once either resolves it);
verify Lemma J's exact statement actually supports being applied to bound {r_j} in
this way (Lemma J was proved for a different original purpose — check compatibility,
don't cite blindly).
Cases to cover: k_0 may depend on the pair; must show k_0 is finite (not that the
induction starts at k=1) — bounded by existing Finite Core Theorem machinery.
Watch out for: this is NOT a repeat of the dead "inductive chaining across successive
same-type occurrences" (Lemma I's 2nd dead recombination) — that attempt used ONLY
the four certified tools (Free Facts/Bounded Witness/Gap Lemmas/Critical Prime
Dichotomy) with no new object; here the induction step's content comes from anchoring
on the FIXED integer a_{m_{k+1}} and its finite divisor lattice (Lemma J), a
genuinely new ingredient not available to the dead attempt. If the canonicality
sub-step cannot be closed, this whole mechanism reduces to that same dead wall —
flag honestly if that happens rather than papering over it.

---

seed-coupling-induction: new
Target: whole problem, proved by strong induction on k := |Q| = ω(a_1) (number of
distinct prime factors of a_1) ACROSS THE FAMILY OF ALL VALID SEEDS — a genuinely
different top-level framing from every prior approach, none of which has attacked the
claim by varying the seed rather than analyzing one fixed instance's internal
recruitment process. This directly answers the plateau rule: it is not a reroute of
FAH/Symmetric FAH, it is a different reduction of the whole problem.
Technique: structural strong induction on ω(a_1), via a Seed-Coupling Lemma relating
the given sequence to a strictly-smaller-|Q| "reduced" sequence, with a documented
Plan-B fallback (minimal-counterexample ordered by the raw integer a_1) if the
coupling construction stalls.
Skeleton:
  1. Base case k=1: already fully solved and certified (`greedy-exchange-cost-
     potential`'s |Q|=1 special case) — a_{n+1}=a_n+q for all n, T=1, L=q, no gap,
     literal periodicity from n=1 included.
  2. Inductive hypothesis: every valid sequence with a seed a_1' satisfying
     |Q(a_1')| < k is eventually periodic (with explicit T', L').
  3. NEW Key Lemma — Seed-Coupling Lemma (the central open gap, must be proved from
     scratch; the mechanism explorer flags this as untried anywhere in the corpus or
     workspace). Fix a_1 with Q = {p_1,...,p_k}; pick p_k (any single prime of Q, e.g.
     the largest) and set a_1' := a_1 / p_k^{v_{p_k}(a_1)} (so Q' = Q\{p_k},
     |Q'| = k-1). Run the SAME greedy rule from seed a_1' to generate (a_n'). Claim:
     there is an eventually-defined injective "collapsing" correspondence n ↦ n'(n)
     between sufficiently large indices of the two sequences such that
     τ(n) ∩ Q' = τ'(n'(n)) (their Q'-level types agree) and a_n and a_{n'(n)}' differ
     only by an explicit correction term depending on the (eventually periodic, by a
     direct bounded-gap pigeonhole) 0/1 pattern of "is a_n divisible by p_k."
     Mechanism: Free Facts' gcd>1 requirement, restricted to the primes of Q', is
     identical for both sequences UNLESS a specific pair of terms relies on p_k as
     their ONLY common factor — bound the frequency of that event using the
     Generalized Bounded Gap Lemma (a term "needing" p_k can only occur when no
     smaller Q'-legal candidate exists, and such candidates recur with bounded gap
     ≤ a_1·p_k), giving a provably BOUNDED (not just finite-in-principle) rate of
     p_k-dependent exceptions.
  4. FIRST TASK for the builder (cheap-kill check, per the explorer's recommendation):
     hand-verify the coupling claim numerically on 2-3 small seeds before investing in
     the general proof — e.g. compare a_1=15 (Q={3,5}) against the reduced instance
     a_1'=5 (Q'={5}) or a_1'=3 (Q'={3}), checking whether the Q'-level type sequences
     actually correspond index-for-index (up to the claimed collapsing map). If the
     structures are unrelated on this cheap check, report RETHINK immediately rather
     than forcing the general lemma.
  5. Given the Seed-Coupling Lemma: the reduced sequence is eventually periodic
     (T',L') by the inductive hypothesis. Transport periodicity back: the p_k-
     divisibility 0/1 pattern along the ORIGINAL sequence is itself eventually
     periodic with some period c (bounded pigeonhole on a binary sequence with
     bounded recurrence gap, via the Generalized Bounded Gap Lemma with modulus
     a_1·p_k) — combine to get T := lcm(T', c) (or T'·c if independent) and an
     explicit L (L' plus the extra p_k-contribution accumulated over one full T-cycle,
     computed directly from the periodic 0/1 pattern). This step is itself open and
     must be carried out explicitly, not asserted.
  6. Plan B (documented fallback within this same approach, not a separate slug —
     from the fresh-lens explorer's Opening 2): if Step 3's coupling construction
     does not close, attempt instead a minimal-counterexample argument ordered by
     the RAW INTEGER a_1 (not an internal recruitment-stage measure, which is the
     specific failure mode that killed the round-3 size-measure and round-5
     witness-index descents — those measured complexity WITHIN one fixed sequence's
     recruitment history and were broken by refinement manufacturing new smaller
     witnesses; ordering by a_1 itself has no refinement step at all, so that
     specific failure mode cannot recur here). Assume a_1 is the SMALLEST integer
     whose greedy sequence is not eventually periodic. Attempt to produce a smaller
     "bad" instance by restricting to one persistent type's own occurrence-
     subsequence (identified via Persistent-Type Pigeonhole) and showing it is itself
     generated by a legitimate smaller seed satisfying the same greedy-type local
     rule. This reduction step (does non-periodicity propagate down to a
     sub-persistent-type sequence with strictly smaller data) is UNVERIFIED and is
     the precise open sub-question for Plan B — check by direct hand construction on
     one seed before committing further effort to it.
Key lemmas (claim + mechanism):
  - Seed-Coupling Lemma (Step 3) — because Free Facts' shared-prime condition
    restricted to Q'-primes is identical between the two instances except on a
    bounded-frequency set of p_k-dependent exceptions (Generalized Bounded Gap Lemma
    bounds how often a term can be FORCED to rely on p_k alone).
  - p_k-pattern periodicity (Step 5) — because a bounded-recurrence-gap 0/1 sequence
    over a fixed alphabet must be eventually periodic by pigeonhole on its recent
    history window (standard, but must be stated and applied correctly here, not
    assumed).
Open gaps: the entire Seed-Coupling Lemma (Step 3, untried anywhere in this
workspace or the crux corpus per the explorer's search) and its periodicity-transport
step (Step 5); Plan B's reduction step (Step 6) is a documented but unverified
fallback, not a proof.
Cases to cover: choice of which prime p_k to remove should not affect the argument's
validity (any single-prime removal strictly decreases |Q| by one) — but the builder
must verify at least one canonical choice works before generalizing to "any choice."
Watch out for: this is explicitly NOT a retry of the two dead well-ordering descents
(round 3's |A'|+|B'| size measure, round 5's witness-index measure) — both of those
ordered complexity WITHIN one fixed sequence's own recruitment process and were
broken by refinement manufacturing new smaller witnesses. This approach's ordering
(|Q| across different seed instances, or Step 6's ordering by raw a_1) has no
refinement operation at all, so that specific dead-end mechanism cannot directly
recur — but this must not be treated as proof the approach works; if the coupling
claim in Step 4's cheap-kill check fails on even one small seed, report RETHINK
honestly rather than forcing the induction.

---

recruitment-round-charging: do not advance (stays RETHINK/dead, per round 6/7 verdicts
— all three charging candidates confirmed dead-end or FAH-equivalent; no new angle
surfaced this round for it).

density-sieve-contradiction: do not advance — this round's density-lens explorer
confirmed bare density/counting arguments are structurally the WRONG STRENGTH of tool
for FAH's cofinite claim (a cheap-kill, not a route); no builder slot warranted unless
a future round finds a genuine exact-identity substitute for the aimo-0680 template
(none found this round).
