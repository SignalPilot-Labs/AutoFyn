## imo-2026-06 (lens: monovariant/termination-proof for the recruitment process)

- Distinct openings:
  1. **Canonical-Refinement Lemma (NEW, fully proved this round, not yet in any approach
     file).** Fix disjoint persistent base types A, B ∈ 𝒫, and the Finite Core Theorem's
     canonical witness m_B for B (so F_B := P(a_{m_B})\Q ⊆ S is fixed, depending only on
     B). Since S ⊇ F_B by definition of S = ⋃_{B∈𝒫} F_B, one gets P(a_{m_B}) ∩ S = F_B
     *exactly* (not just ⊇): any prime of a_{m_B} outside Q is in F_B by definition, and
     F_B ⊆ S already, so intersecting with S changes nothing. Hence the canonical
     witness's own extended type is ρ(m_B) = B ∪ F_B — call this the **canonical
     refinement** B'_can of B. Combining with the "what's already proved" step already
     in `covering-system-construction` Step 4 (every extended-persistent refinement A' of
     A meets F_{A,B} = F_B, by the Bounded Witness Lemma applied with witness m_B, valid
     for literally every n > m_B with τ(n) = A, hence in particular for every n in each
     infinite A'-subsequence): **every extended-persistent refinement A' of A intersects
     the canonical refinement B'_can of B**, and symmetrically **every extended-persistent
     refinement B' of B intersects the canonical refinement A'_can of A.** This is a
     genuinely new, fully rigorous, unconditional partial result — it closes (†) for
     every pair where AT LEAST ONE side is its base type's canonical refinement, using
     zero extra recruitment (pure consequence of the already-certified Finite Core
     Theorem + Bounded Witness Lemma, no new lemma needed beyond re-deriving this
     corollary). The ONLY case left open is when BOTH A' ≠ A'_can and B' ≠ B'_can
     simultaneously (both "non-canonical" refinements of their respective base types).
     This is a strictly smaller, better-localized residual gap than the raw (†) or the
     abstract "recruitment process" framing — recommend the outliner state (†) as this
     sharper "non-canonical × non-canonical" residual, not the undifferentiated original.
  2. **Zero-round conjecture, now MUCH more strongly evidenced.** Extended the round-2
     computational check from 10 seeds to 13, up to |Q| = 7 (a_1 = 4849845 =
     3·5·7·11·13·17·19), and — critically — specifically isolated and separately counted
     "non-canonical × non-canonical" pairs (the only case Opening 1 leaves open): **zero
     violations found among 200–450+ such pairs per seed**, across all 13 seeds. This is
     the most targeted test of the actual residual gap done so far (prior rounds checked
     aggregate violations only, not this specific stratification) and gives strong
     additional confidence the zero-round conjecture is true, though still only
     empirical.
  3. **Falsified a natural strengthening — do not pursue.** Tested computationally
     whether F_B (the canonical witness's extra-prime set) is a *subset* of every
     extended-persistent refinement of B, which would trivially finish (†) via Opening 1
     with zero further work. This is FALSE: across 8 seeds, 20–29 (base type, refinement)
     pairs checked each, the overwhelming majority (≈85–100%) of non-canonical
     refinements do NOT contain F_B as a subset. So whatever mechanism makes
     non-canonical × non-canonical pairs intersect (confirmed empirically in Opening 2),
     it is not simply "every refinement inherits the canonical witness's extra primes" —
     it must be a genuinely different, case-by-case shared prime each time. Record this
     as a falsified sub-conjecture so no future round re-tries it.
  4. **Termination-proof-technique scouting from the crux corpus (see below)** — no
     directly-transplantable analog found, but two structural templates are worth having
     in mind: (a) "assume the process runs forever, extract a repeating/minimal
     configuration, derive a contradiction from minimality" (aimo-0077's extremal
     principle); (b) "encode the relevant data as a state in a FIXED finite state space,
     note the state-to-state map is well-defined/deterministic, invoke pigeonhole to get
     recurrence" (aimo-0678 Solution 2, aimo-0514). Neither adapts directly here because
     our "state" (the extended-type space 2^{S₀^(k)}) is not fixed in advance — it grows
     with each recruitment round, which is exactly the obstruction to a naive pigeonhole
     termination argument. A genuine adaptation would need to bound the SIZE that S₀ can
     ever reach a priori (independent of how many rounds occur), turning the recruitment
     process into search over a fixed finite space — this is not yet done by anyone.
  5. **Re-examined whether the original Finite Core Theorem's S is a red herring /
     "recruitment" framing solves a nonexistent problem.** No — the Finite Core Theorem
     genuinely only proves a weaker statement (Caveat, `finite-core-theorem.md`): "for
     each n and each disjoint B, SOME prime of S divides a_n" — it explicitly does NOT
     establish that a single FIXED extended type captures this uniformly for all n of a
     given persistent type. Opening 1 above shows this gap is smaller than previously
     framed (only non-canonical × non-canonical pairs are actually open), but it is real:
     the raw Finite Core Theorem alone, without Opening 1's extra derivation, is not
     sufficient, and the recruitment-process reformulation is still the right target — my
     scouting narrows rather than eliminates it.

- Candidate technique(s): pigeonhole/pairing arguments already dominate and remain the
  right toolkit (Generalized Bounded Witness Lemma's Corollary). The genuinely missing
  piece is either (a) a direct proof that non-canonical × non-canonical pairs intersect
  by finding a THIRD common reference point (e.g., show any two extended-persistent
  refinements of DIFFERENT base types both must intersect some FIXED reference prime
  set determined jointly by the whole family 𝒫, via a stronger double-witness/double-
  pigeonhole argument that considers linking through an intermediate persistent type),
  or (b) an extremal/minimal-counterexample argument in the style of aimo-0077: assume a
  non-canonical × non-canonical violating pair exists, is chosen to be "extremal" in some
  sense (e.g., minimizing the sum of indices of witnesses used, or minimizing |S₀|
  needed to detect it), and derive a contradiction with that minimality via the
  Generalized Bounded Witness Lemma's own Corollary applied to the extremal instance.

- Cheap-kill candidates: none obvious for out-right refuting the conjecture; the
  falsified "F_B ⊆ every refinement" idea (Opening 3) was the natural cheap check and it
  failed, so no further cheap structural pruning is apparent — the remaining gap seems
  to genuinely require a real argument, not a shortcut.

- Knowledge-base entries to use: "Pigeonhole / extremal principle" (used repeatedly, and
  the likely home of any minimal-counterexample termination argument); "Modular
  arithmetic, CRT" (for the Step-5 finish once (†) closes). No other knowledge_base.md
  entry looks newly relevant to the termination question specifically.

- Analogous past problems (cruxes):
  - `aimo-0678` (number_theory, modular-arithmetic-and-CRT / sequences-and-recurrences) —
    already the field's standing analog; its Solution 1's monotone potential (w_n)
    doesn't transplant (our sequence is unbounded, not bounded-then-cyclic), but Solution
    2's mechanism — reduce to a *fixed* finite state (a_n, b_n mod M) and invoke
    determinism + pigeonhole for eventual periodicity — is the right *shape* of argument
    IF we can first pin down a fixed-in-advance modulus/state space, which is exactly
    what (†) is trying to establish. Not directly usable until (†) is closed, but
    confirms the eventual finish (Step 5, CRT + cyclic pigeonhole) is the standard
    template once the state space is fixed.
  - `aimo-0077` (combinatorics, extremal-principle) — "assume nontermination forces a
    repeating state/cycle, take the minimal-index object acted on in that cycle, show
    restoring it needs a forbidden smaller action" — a genuinely different *proof style*
    (minimal-counterexample / extremal-principle termination, not pigeonhole-on-a-fixed-
    space) worth trying on the recruitment process directly: assume infinitely many
    rounds occur, take the round that recruits the "smallest" new prime (well-ordering of
    primes), and try to derive a contradiction from minimality using the structure of the
    Corollary. Not yet attempted by anyone; flagged as a concrete next avenue, not a
    solved transplant.
  - `aimo-0514` (combinatorics, processes-and-algorithms/invariants) — "deterministic +
    reversible ⇒ state graph is a union of cycles ⇒ purely periodic, not just eventually
    periodic" — relevant to the SECONDARY open gap (periodicity holding from n=1
    literally, not just eventually), flagged in current.md's Next section, but not to
    the primary termination question; keep in mind for whichever round closes (†) first.

- Prior progress: `current.md`'s full stack (Free Facts, Bounded Gap Lemma, Persistent-
  Type Pigeonhole, Bounded Witness Lemma, Finite Core Theorem, Generalized Bounded Gap
  Lemma, Single-Witness-Prime Pigeonhole Refinement, Extended Persistent-Type Pigeonhole,
  Generalized Bounded Witness Lemma + Corollary, |Q|=1 fully resolved) — all certified,
  unconditional, reusable. Plus this round's new (not yet certified — needs a builder to
  formalize and a reviewer to check) **Canonical-Refinement Lemma** (Opening 1 above),
  which is a straightforward, essentially mechanical corollary of already-certified
  lemmas (Finite Core Theorem + Bounded Witness Lemma) and should be easy for a builder
  to write up rigorously and get certified — it is real, unconditional progress that
  strictly localizes (†) to the non-canonical × non-canonical case.

- Dead ends (do not retry):
  - The three round-2 monovariants already recorded in current.md (persistent-extended-
    type count |𝒫'_k| — not monotonic the right way; "reconciled pairs stay reconciled"
    — doesn't bound rounds since one round need not fully settle a whole base pair;
    growth-rate/ω(a_n) bound — doesn't control the count of distinct recurring primes).
  - **NEW this round:** "F_B (the canonical witness's extra-prime set) is a subset of
    EVERY extended-persistent refinement of B" — computationally falsified (≈85–100%
    failure rate across 8 seeds); do not use this as a shortcut to finish the Canonical-
    Refinement Lemma's remaining non-canonical × non-canonical case.
  - Same-base-type pairwise intersection of refinements is a trivial, uninformative
    check (they always intersect via the shared base type through Q itself) — not a
    useful direction, confirmed but not novel.

- Small-case / intuition notes (all conjecture, not proof):
  - The zero-round conjecture (S from the Finite Core Theorem already suffices for (†),
    with no further recruitment) now has support from 13 seeds, |Q| up to 7, and —
    newly — a stratified check confirming zero violations specifically among the
    "hardest" non-canonical × non-canonical pairs (200–450+ such pairs checked per seed).
    This is strong evidence the true theorem needs NO unbounded recruitment argument at
    all, and that a direct combinatorial argument (extending the Canonical-Refinement
    Lemma to cover non-canonical refinements too) should exist and close (†) outright,
    rather than requiring an abstract termination/monovariant proof for a
    possibly-unbounded process. Recommend the outliner prioritize extending Opening 1's
    proof technique over hunting for an abstract monovariant, since the process appears
    empirically to need literally zero rounds beyond the very first, well-understood
    step.
