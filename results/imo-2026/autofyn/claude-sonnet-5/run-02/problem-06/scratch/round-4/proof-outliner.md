## imo-2026-06

### Context this round
All three approaches with real content (`covering-system-construction`,
`greedy-exchange-cost-potential`) bottom out at the same crux: residual set
V ("rogue pairs," both sides non-canonical S₀-refinements of disjoint base
types). Two prior well-ordering attacks failed for a documented reason:
recruitment only ever GROWS the ambient signature (never shrinks it), and the
Corollary's pigeonhole only certifies the recruited prime's recurrence on the
side being reconciled, never the fixed witness side. This round's three
explorers converged on one precise missing ingredient across all three lenses:
a JOINT/SIMULTANEOUS fact across a whole occurrence-family, not a
single-witness pigeonhole — specifically, strong (but unproved) evidence that
(a) recruiting one prime resolves ALL currently-rogue pairs at once, and (b) a
base type is, from its FIRST occurrence, a superset of a small fixed prime
core relative to each disjoint partner. NEITHER has a proof mechanism yet;
this round's job is to supply one, not add more computation. Do NOT re-open
"zero further recruitment rounds" (falsified, a_1=175/385) or the mod-M
finite-automaton framing (confirmed by fresh-framing explorer to collapse into
the existing Step 5 CRT finish).

---

covering-system-construction: revise
Target: the full problem claim — a_{n+T} = a_n + L for all n — via the
existing S₀/extended-type/CRT architecture (Steps 1–5, already largely
proved), with this round's revision aimed squarely at closing gap (†) via a
NEW key lemma.
Technique: direct greedy-minimality / exchange argument on individual terms
(not a global well-ordering on a static size measure — that already failed,
Step 4f), using the certified Generalized Bounded Gap Lemma's "any multiple of
a_1·p is automatically legal against every earlier term" fact as the engine.
Skeleton:
  1. (already proved, reuse) Steps 1–4e: Free Facts, Bounded Witness Lemma,
     Finite Core Theorem, Generalized Bounded Witness Lemma + Recruitment
     Corollary, Canonical-Refinement Lemma, F_A∩F_B≠∅.
  2. NEW — **Persistent Uniform Core Lemma (PUCL)**: for each persistent base
     type A ∈ 𝒫, there is a fixed nonempty finite set C_A ⊆ S (S from the
     Finite Core Theorem) such that EVERY occurrence of type A, from its
     FIRST occurrence n_A onward (not just eventually, not just infinitely
     often), is divisible by at least one prime of C_A — by strong induction
     on n: suppose the claim holds for all earlier A-type occurrences
     m < n (τ(m)=A ⟹ some prime of C_A divides a_m, where C_A is fixed at the
     first occurrence n_A as C_A := P(a_{n_A}) \ Q intersected with S).
     Inductive step: consider the greedy choice at step n. By the
     Generalized Bounded Gap Lemma, for the specific prime p_0 ∈ C_A used at
     n_A, some multiple of a_1·p_0 exceeding a_{n-1} is automatically legal
     against every earlier term (since a_1·p_0 shares a Q-prime with every
     earlier term via a_1, by Free Fact 1/2) AND divisible by p_0 ∈ C_A ⊆ S.
     This gives an explicit UPPER BOUND on the smallest legal type-A candidate
     that uses p_0. The crux to actually prove: show the greedy process's true
     choice a_n, if it is type A, cannot "skip" this p_0-multiple in favor of
     a smaller candidate using a genuinely different prime of S \ C_A — i.e.
     show the p_0-multiple candidate is in fact ≤ any competing legal
     candidate NOT divisible by any element of C_A. This is the exact
     technical content the retracted Step 4b ("Universal Glue Prime") tried
     and failed at the WRONG scope (one prime for ALL types); PUCL restates it
     CORRECTLY scoped (one small fixed set PER base type, not one prime
     globally) — the builder must attempt the comparison-of-candidates
     argument Step 4b sketched but never completed, now at the right scope.
  3. Corollary of PUCL: if A, B ∈ �𝒫 disjoint, then C_A and C_B are each fixed
     finite sets; either (a) C_A ∩ (any B-type occurrence's own C_B-witness)
     ≠ ∅ by F_A∩F_B≠∅-style reasoning at the C-level (needs proof: C_A ∩ C_B
     ≠ ∅, analogous mechanism to Step 4e), giving A' ∩ B' ⊇ (a fixed prime of
     C_A∩C_B) for EVERY extended-persistent refinement A', B' of A, B — this
     would close V = ∅ completely and unconditionally, since PUCL gives
     uniformity from the first occurrence (bypassing the canonical/
     non-canonical distinction entirely — PUCL, if proved, subsumes the
     Canonical-Refinement Lemma).
  4. Feed into Step 5's CRT + cyclic pigeonhole finish (already proved,
     unconditional given (†)) using S₀ := Q ∪ ⋃_A C_A in place of S.
Key lemmas (claim + mechanism):
  - PUCL: base type A is, from its first occurrence, always divisible by a
    fixed core C_A — because a competing p_0-multiple candidate (legal by the
    Generalized Bounded Gap Lemma) is always available and the builder must
    show the greedy process cannot prefer a smaller non-C_A candidate; this
    is the actual open mechanism, explicitly not yet supplied by any prior
    round.
  - C_A ∩ C_B ≠ ∅ for disjoint A, B — because pairwise gcd (Free Fact 2)
    applied to ANY two occurrences (not just canonical witnesses) forces a
    shared non-Q prime, and if PUCL holds this shared prime must lie in
    C_A ∩ C_B specifically (needs its own short argument once PUCL is fixed).
Open gaps: PUCL itself (the "cannot prefer a smaller non-C_A candidate" step)
is entirely unproved — this is the round's real target, not a formality.
Cases to cover: none beyond the existing |Q|=1 fully-solved case (Step 4,
already in the file).
Watch out for: this is exactly the shape of claim ("universal glue prime")
that was FALSIFIED in round 2 at the WRONG scope (single prime for ALL types
at once). PUCL is scoped per-base-type (C_A, not one global prime) — the
builder must explicitly re-verify PUCL survives the a_1=35 and a_1=175
counterexamples that killed the old claim (a_1=35: does {7}'s C_{7} = {2,3}
hold from n=3 onward with zero exceptions, per the joint-family explorer's
computation? a_1=175: does {2,7}'s C = {13} hold from n=3 onward, as the
joint-family explorer found?) before claiming a proof — if PUCL itself is
false in general (not just these lucky seeds), retract immediately rather
than patch.

---

greedy-exchange-cost-potential: revise
Target: the full problem claim, same architecture, via a DIFFERENT and
weaker-but-sufficient closing lemma than PUCL, in case PUCL proves too hard.
Technique: well-founded induction on the ROUND NUMBER of the recruitment
process (Step 4c) — a first-bad-round / time-ordered minimality argument,
structurally modeled on crux corpus aimo-0514 / aimo-0077 ("assume the
process never fully terminates; take the FIRST round at which a specific bad
event recurs; contradict via what must already have been true one round
earlier") — genuinely distinct from the two already-failed STATIC size-based
well-orderings (|A'|+|B'|, |𝒫'_k|) documented in Step 4f, since the induction
variable here is process time, not a set-theoretic size measure of a single
stage's objects.
Skeleton:
  1. (reuse) Steps 1–4c: the recruitment process is already exactly and
     rigorously defined (Step 4c); (†) holds iff it halts in finitely many
     rounds; "reconciled pairs stay reconciled" is already proved
     unconditionally (Step 4c, "Monovariant candidates tried," second bullet)
     — i.e. once A', B' intersect at stage k, every refinement at every later
     stage k' > k still intersects. This fact is REUSABLE and is the base
     case for the new induction.
  2. NEW — **Round Resolution Lemma**: when the recruitment process, at stage
     k, recruits prime q to resolve a specific rogue instance (A'_0, B'_0)
     with base types A, B, then q divides EVERY sufficiently large A-type
     term (not merely the infinitely many A'_0-type ones the Corollary
     already certifies) — equivalently, the recruitment PERMANENTLY resolves
     the WHOLE base-type pair (A, B), not just the witnessed instance. Proof
     attempt via first-bad-round minimality: suppose not — suppose some
     stage k is the FIRST at which a recruited prime q fails to achieve whole
     -pair resolution for its targeted (A,B) (i.e. some later stage k' > k
     still has a rogue instance with the same base-type pair (A,B)). Use
     minimality of k (no earlier stage had this failure) to constrain what
     the stage-k' rogue instance's witness data can be — the key move to
     supply: show the later rogue instance's own witness index is forced
     (by Free Fact 2 pairwise-gcd applied against the SAME index used at
     stage k) to already carry q, contradicting its being rogue at stage k'.
     This is the open technical content; it directly targets the exact
     obstruction Step 4f documented (Corollary only certifies the reconciled
     side, not the fixed witness side) by using TIME ORDER — "q was
     established at an earlier, hence available, stage" — as the missing
     lever, instead of a set-size comparison.
  3. Corollary: since there are only finitely many disjoint base-type pairs
     (≤ C(|𝒫|,2)), and (by Step 1's reuse + the Round Resolution Lemma) each
     recruitment round permanently removes at least one base-type pair from
     future violation, the recruitment process halts within ≤ C(|𝒫|,2)
     total rounds — giving (†) unconditionally, with an EXPLICIT bound on
     the final S₀, without needing the full per-term uniformity of PUCL.
  4. Feed into Step 5's CRT finish exactly as in `covering-system-construction`
     (import, do not re-derive).
Key lemmas (claim + mechanism):
  - Round Resolution Lemma — because the recruited prime q is forced, via
    Free Fact 2 applied at the specific witness index used to define q, to
    already appear at any LATER stage's would-be counterexample witness too,
    by first-bad-round minimality (the actual gcd argument connecting the two
    witnesses across stages is the open step).
  - Finite bound on total rounds ≤ C(|𝒫|,2) — because base-type pairs are
    finite in number and (given the Lemma) each is resolved at most once,
    permanently.
Open gaps: the Round Resolution Lemma's core step (forcing q into the later
stage's witness via minimality) is unproved — this is the round's target.
Cases to cover: none beyond existing.
Watch out for: do NOT re-derive "reconciled pairs stay reconciled" (already
proved, Step 4c) — import it. Do NOT reuse the |A'|+|B'| or |𝒫'_k| static
measures (Step 4f already shows these fail) — the induction variable here
MUST be the process's round index k, not a per-stage set size, or this
collapses into the already-failed Step 4f attempt under a new name.

---

uniform-core-direct-induction: new
Target: the full problem claim, via a structurally different top-level route
that bypasses the S₀/extended-type/V machinery entirely — a genuinely new
framing (per CLAUDE.md's diversity mandate), not a technique variant of the
above two.
Technique: direct strong induction on n proving a self-contained "each base
type reconciles itself against every disjoint type from its first occurrence"
statement, then a direct CRT finish over the union of these per-type cores —
skipping the Finite Core Theorem → extended types → recruitment-process
detour altogether.
Skeleton:
  1. Reuse (unconditional, do not re-derive): Free Facts 1–2, Persistent-Type
     Pigeonhole (𝒫 finite, τ(n) ∈ 𝒫 eventually).
  2. For each persistent base type A ∈ 𝒫, let n_A be its first occurrence
     after N_0 (Step 1's threshold). Define D_A := P(a_{n_A}) \ Q (finite,
     since a single integer). Claim: **by strong induction on n**, for every
     n > n_A with τ(n) = A, a_n is divisible by some element of D_A that is
     ALSO in the intersection ⋂_{B ∈ 𝒫, B∩A=∅} D̃_{A,B} for a to-be-defined
     stable subset — i.e. attack the SAME target as PUCL above but by
     induction that carries a growing invariant "every A-occurrence up to n
     has used only primes from D_A" as the thing being maintained, rather
     than trying to prove it in one shot from a fixed witness. The
     difference from `covering-system-construction`'s PUCL attempt: here the
     induction hypothesis at step n is used to directly bound a_n itself
     (via the Generalized Bounded Gap Lemma, a_n ≤ a_{n-1} + a_1·p for any
     p ∈ D_A), producing an explicit numeric UPPER bound for a_n assuming
     the invariant continues, then checking a_n cannot be smaller by
     exhibiting that any legal candidate not respecting the invariant is
     forced (by Free Fact 2 against the immediately preceding same-type
     occurrence, not an arbitrary witness) to be at least as large — a
     tighter, more local inductive comparison than PUCL's global one.
  3. If the induction closes: every base type A gets a FIXED finite core
     D_A ⊆ S (S from the Finite Core Theorem, reused) valid literally from
     n_A onward (no canonical/non-canonical split needed at all — this
     approach's target, if it succeeds, makes the entire V/rogue-pair
     apparatus moot, not just a special case of it).
  4. Direct finish: L := ∏_{p ∈ Q ∪ ⋃_A D_A} p; CRT residue-class argument
     exactly as Step 5 of `covering-system-construction` (import that
     step's mechanism, cite by reference, do not re-derive the CRT part).
Key lemmas (claim + mechanism):
  - Local invariant-preservation step (2) — because the Generalized Bounded
    Gap Lemma gives an explicit competing candidate at every step, and the
    inductive hypothesis (not a global witness comparison) is what must be
    shown to force the greedy choice to respect D_A; this is a genuinely
    different proof shape from both sibling approaches (local step-by-step
    vs. global witness-based).
Open gaps: the entire inductive step (2) is unproved — this is a from-scratch
attempt, higher risk, but a genuinely different route (bypasses extended
types altogether) per this round's diversity mandate; if the local induction
fails for the same reason PUCL might (greedy can still legally pick a
different, smaller prime at some step), this approach should report that
failure precisely (which specific step of the induction breaks) rather than
retreat silently — that failure mode itself would be a useful negative result
for the other two approaches.
Cases to cover: |Q|=1 (trivial, reuse existing resolution).
Watch out for: this approach's induction hypothesis must be checked against
the SAME two counterexample seeds (a_1=35, a_1=175) that killed the round-2
"Universal Glue Prime" claim — if this local induction also predicts a
single/universal set incompatible with those seeds' actual behavior, retract
immediately with the specific numeric mismatch recorded, exactly as Step 4b's
retraction was handled.

---

density-sieve-contradiction, hypergraph-transversal: no change (stale,
Elo lowest, no new content proposed this round; correctly left out of the
build set again).

build set: covering-system-construction, greedy-exchange-cost-potential, uniform-core-direct-induction
