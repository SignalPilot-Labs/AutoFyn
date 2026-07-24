## imo-2026-06

covering-system-construction: revise
Target: There exist positive integers T, L such that a_{n+T} = a_n + L for every n
(full problem claim, via the extended-type/S₀ machinery already built in
`results/imo-2026-06/approaches/covering-system-construction.md`).
Technique: Explicit constructive induction on the core prime pool S₀, finished by
CRT + cyclic pigeonhole (Step 5, unchanged and already correct). This round's revision
narrows gap (†) using two newly-found unconditional lemmas instead of re-attacking the
raw abstract statement.
Skeleton (only the changed tail; Steps 1–3, 5 are unchanged, already certified):
  1. (unchanged) Free Facts, Persistent-Type Pigeonhole, Bounded Witness Lemma, Finite
     Core Theorem (Steps 1–3) — certified.
  2. (unchanged) Extended types ρ(n) = P(a_n) ∩ S₀, 𝒫' the extended-persistent family
     (Step 4) — certified.
  3. **NEW Step 4d — Canonical-Refinement Lemma** (write up and certify the monovariant
     explorer's Opening 1 as a lemma): for disjoint base types A, B ∈ 𝒫 with canonical
     witnesses m_A, m_B (from the Finite Core Theorem's construction), the canonical
     refinements A'_can := ρ(m_A), B'_can := ρ(m_B) satisfy: every extended-persistent
     refinement A' of A meets B'_can, and every extended-persistent refinement B' of B
     meets A'_can. Mechanism: F_{A,B} = P(a_{m_B}) \ Q ⊆ S ⊆ S₀ by definition of S, and
     P(a_{m_B}) ∩ S₀ = B ∪ F_{A,B} = B'_can exactly (no strict containment, since every
     prime of P(a_{m_B}) outside Q is by definition in F_{A,B} ⊆ S₀, so intersecting
     P(a_{m_B}) with S₀ recovers exactly Q-part B plus the S-part F_{A,B}). Combined with
     the already-certified Step 4 deduction (A' ∩ F_{A,B} ≠ ∅ for every extended-
     persistent A'), this gives A' ∩ B'_can ⊇ A' ∩ F_{A,B} ≠ ∅. This closes (†) for EVERY
     pair where at least one side is its own base type's canonical refinement — a purely
     mechanical corollary of already-certified lemmas, zero new hypotheses.
  4. **NEW Step 4e — F_{A,B} ∩ F_{B,A} ≠ ∅ lemma** (certify the closure explorer's
     finding): for disjoint persistent base types A, B, gcd(a_{m_A}, a_{m_B}) > 1 (Free
     Fact 2) forces a shared prime p; p ∉ Q since Q-membership would put p in A ∩ B = ∅;
     hence p ∈ F_{A,B} ∩ F_{B,A}. Record explicitly (per the monovariant/closure
     explorers' verified finding) that this does NOT by itself finish (†): it only shows
     the two canonical-witness-derived sets overlap, not that an arbitrary non-canonical
     A' contains p. State this limitation in-file so the builder does not present it as
     more than it is.
  5. **Residual gap, sharply localized:** (†) is now needed ONLY for pairs A', B' ∈ 𝒫'
     of disjoint base types where BOTH A' ≠ A'_can and B' ≠ B'_can (both non-canonical
     refinements). Attempt to close this residual via a minimal-counterexample argument
     (aimo-0077 style, adapted from the monovariant explorer's technique suggestion):
     suppose a non-canonical × non-canonical violating pair (A', B') exists; among all
     such violating pairs across the whole finite family 𝒫' × 𝒫', pick one minimizing
     some well-founded quantity (candidate: the sum of the indices of the earliest
     witnesses realizing A' and B' respectively, or |A'| + |B'| as a coarser fallback);
     apply the Generalized Bounded Witness Lemma's Corollary to this extremal pair to
     recruit a forced new prime q, and argue q's recruitment either (a) contradicts
     minimality by producing a "smaller" violating pair, or (b) shows q was already
     forced into A' or B' by an earlier, already-canonical-covered mechanism — NEITHER
     direction is yet proved; this is the open gap the builder must resolve, not assumed.
Key lemmas (claim + mechanism):
  - Canonical-Refinement Lemma — because P(a_{m_B}) ∩ S₀ = B ∪ F_{A,B} exactly (S₀ ⊇
    F_{A,B} makes the intersection lose nothing), so the canonical witness's own
    extended type already contains the linking prime by construction.
  - F_{A,B} ∩ F_{B,A} ≠ ∅ — because gcd(a_{m_A}, a_{m_B}) > 1 (Free Fact 2) forces a
    shared prime, and Q-membership is ruled out by A ∩ B = ∅.
Open gaps: the non-canonical × non-canonical residual of (†) (Step 5 above); the
minimal-counterexample mechanism to close it is proposed but not proved. Secondary:
extending periodicity to n = 1 literally.
Cases to cover: none new (the |Q|=1 case remains fully resolved and unaffected).
Watch out for: do NOT claim the Canonical-Refinement Lemma closes (†) in general — it
provably only covers pairs with at least one canonical side; the closure explorer found
the naive strengthening "F_B ⊆ every refinement" is FALSE (85–100% failure rate across
8 seeds) — do not let the builder smuggle that back in as a shortcut for the residual.

greedy-exchange-cost-potential: advance
Target: same full problem claim, via the integer cost/witness-prime pigeonhole framing
already in `results/imo-2026-06/approaches/greedy-exchange-cost-potential.md`.
Technique: bound a per-term "cost" quantity (count of extra load-bearing primes beyond
Q needed to reconcile a term with all disjoint persistent types) using pigeonhole on
witness primes, distinct in framing from covering-system-construction's set-language
even though both now converge on the same residual gap.
Skeleton: unchanged Steps proving Generalized Bounded Gap Lemma, Single-Witness-Prime
Pigeonhole Refinement, Extended Persistent-Type Pigeonhole, and the resolved |Q|=1 case
(all certified). This round: import the Canonical-Refinement Lemma and F_{A,B}∩F_{B,A}
lemma (once certified via covering-system-construction) and re-attempt the stalled
"combine lemmas to close (†)" step using the cost-potential language: define
cost(A') := minimum number of non-canonical "extra" primes a non-canonical refinement
A' needs beyond what its base type's canonical refinement already supplies, and try to
show cost(A') is bounded by a fixed constant (not growing with |𝒫'|) via a direct
counting/exchange argument (the "rogue refinement" exchange idea from the closure
explorer's Opening 3: a refinement lacking a common prime with some partner would have
to be systematically skippable by the greedy minimality rule, contradicting a_n being
the actual smallest legal choice).
Key lemmas (claim + mechanism):
  - (import) Canonical-Refinement Lemma, F_{A,B}∩F_{B,A}≠∅ — as above.
  - Cost-boundedness conjecture (NOT yet proved) — because the Bounded Gap Lemma
    guarantees a nearby p*-multiple candidate exists cheaply, so if the actual chosen
    a_n needed strictly more "expensive" reconciliation than that candidate, greedy
    minimality would have preferred the cheaper one — this exchange mechanism has not
    been carried through rigorously and is the genuine gap.
Open gaps: same residual as covering-system-construction (non-canonical × non-canonical
pairs), attacked here via the exchange/minimality mechanism instead of the extremal-
pair mechanism — worth running both in parallel since they may succeed independently.
Cases to cover: none new.
Watch out for: this approach already once mistakenly conjectured "cost(n) ≤ 1" and
"cost(n) ≤ |𝒫|−1" and both were refuted (a_1=35 counterexample, cost(153)=2 with an
irrelevant junk prime 13) — do not resurrect either bound; the exchange argument must
produce a genuine fixed constant with an explicit proof, not an unproved guess.

witness-depth-bound: new
Target: same full problem claim, but via a genuinely different top-level reduction:
instead of proving the S₀-recruitment process terminates, prove directly that every
prime which is ever "load-bearing" (needed infinitely often by the Bounded Witness
Lemma's mechanism to reconcile some disjoint persistent-type pair) is bounded by an
explicit numeric constant B = B(a_1), making finiteness of the core pool immediate
(finitely many primes ≤ B) with no round-counting or recruitment language at all.
Technique: bound witness INDEX DEPTH first (an explicit function of |Q| alone, not of
n), then convert to a prime-size bound via the already-certified Generalized Bounded
Gap Lemma (a_{n+1} ≤ a_n + a_1·p for any prime p dividing every element of Q, giving
a_m ≤ a_1 + m·(a_1·p_max) type bounds once m is capped).
Skeleton:
  1. Reuse Free Facts, Persistent-Type Pigeonhole, Bounded Witness Lemma, Finite Core
     Theorem verbatim (certified) — these already give a finite S with an EXPLICIT bound
     in terms of the witnesses m_B, B ∈ 𝒫; the open question the freshframing explorer
     isolated is whether m_B itself (the witness's index) can be bounded a priori by a
     function of |Q| alone, independent of how the sequence actually behaves.
  2. **Key new claim (open, to be attacked by the builder):** for each persistent type
     B ∈ 𝒫, the FIRST occurrence index of B is bounded by an explicit function f(|Q|)
     (e.g. via a pigeonhole argument on the first window of length 2^{|Q|}·(something)
     terms: since there are only 2^{|Q|}−1 possible types and Free Fact 1 forces every
     term to already have SOME type from step 2 on, a short initial window must already
     realize every type that is EVER going to be persistent, by an argument bounding how
     long a "new" persistent type can be first-avoided). Mechanism to attempt: show that
     if a type B is not realized within the first N terms for N large relative to 2^{|Q|}
     and the Bounded Gap Lemma's gap constant, then some OTHER already-realized type must
     recur so densely (by pigeonhole on 2^{|Q|}−1 slots over N/gap-bound trials) that B
     can never legally recur either — this needs to be made rigorous, it is NOT yet
     proved; the natural pigeonhole bound (2^{|Q|}−1 types, so SOME type recurs within
     any window of 2^{|Q|} consecutive terms) bounds when a type recurs, not when it
     FIRST occurs, which is the actually needed direction and is harder.
  3. If Step 2's depth bound is established, apply it to bound m_B for all B ∈ �phi
     simultaneously, giving an a priori numeric bound on every prime in S = ⋃ F_{A,B} via
     the Generalized Bounded Gap Lemma (a_{m_B} is bounded, hence has boundedly many,
     boundedly large prime factors) — this would make the WHOLE core-pool question a
     finite, explicit-constant computation with no recruitment or termination language,
     potentially bypassing gap (†) entirely rather than closing it head-on.
  4. Finish via Step 5's CRT + cyclic pigeonhole (shared building block, unchanged).
Key lemmas (claim + mechanism):
  - Witness-depth bound (OPEN, not proved) — because only finitely many types exist
    (2^{|Q|}-1) and the Bounded Gap Lemma bounds consecutive gaps, a first-occurrence
    index for any EVENTUALLY-persistent type intuitively cannot be deferred
    arbitrarily far, but the freshframing explorer's own numerical check (a_1=35) shows
    RECONCILIATION (not first occurrence) can be deferred hundreds of terms deep even
    with both needed primes {2,3} present early — so this lemma must be stated
    carefully about FIRST OCCURRENCE of a type, not about when reconciliation/pairing
    with another type happens; conflating the two is the likely failure mode.
Open gaps: the entire witness-depth bound (Step 2) is unproved and may be false as
loosely stated — this is a genuine gamble on a fresh framing, explicitly flagged as
speculative by the explorer; if it fails cleanly (a builder finds a counterexample or a
structural obstruction) that is still valuable population diversity per CLAUDE.md.
Cases to cover: none yet, since Step 2 is unresolved.
Watch out for: do not conflate "prime size stays small" (weakly supported numerically)
with "witness depth stays small" (the actually needed and much less clear claim) — the
a_1=35 data is a specific warning that these can diverge sharply.

minimal-counterexample-glue: new
Target: same full problem claim, closing (†) — now in its Canonical-Refinement-Lemma-
localized form (import covering-system-construction's Step 4d once certified) — via a
genuinely different PROOF STYLE: extremal/minimal-counterexample argument on the whole
family 𝒫' at once, rather than an iterative forward-recruitment process. This is a
framing difference (well-ordering + contradiction vs. constructive induction), directly
addressing the round-3 dispatch's diversity requirement since the field has shared the
recruitment-process framing for 2 straight rounds.
Technique: assume, for contradiction, that (†)'s non-canonical × non-canonical residual
fails for some pair; among ALL disjoint-base-type pairs (A,B) ∈ 𝒫×𝒫 that admit at least
one violating non-canonical extended-refinement pair, and among all such violating
refinement pairs, choose one that is EXTREMAL by a well-founded quantity — candidate:
minimize |A'| + |B'| (total extended-type "signature size"; well-founded since these are
nonnegative integers bounded above by |S₀|), breaking ties by minimizing the smaller of
the two witnesses' first-occurrence indices. Use minimality plus the Generalized Bounded
Witness Lemma's Corollary to derive a contradiction: the recruited prime q forced by the
Corollary, once adjoined, produces a STRICTLY SMALLER violating instance (by the chosen
well-founded measure) unless the violation is already resolved — this is the aimo-0077-
style mechanism the monovariant explorer flagged as untried.
Skeleton:
  1. Import Free Facts through Extended Persistent-Type Pigeonhole and the Canonical-
     Refinement Lemma verbatim (certified / to-be-certified from covering-system-
     construction). Localize to the non-canonical × non-canonical residual as in that
     approach's Step 5.
  2. Define the well-founded measure μ(A',B') := |A'| + |B'| on violating non-canonical
     pairs (A', B' both non-canonical refinements of disjoint base types, A' ∩ B' = ∅).
     If no violating pair exists, (†) holds — done. Otherwise pick (A'_0, B'_0) minimizing
     μ over all violating pairs (exists by well-ordering of ℕ, since μ takes values in
     {2, ..., 2|S₀|}, finitely many possibilities, and the finite family 𝒫' × 𝒫' means
     "all violating pairs" is itself a finite, nonempty set — direct minimum exists, no
     induction on an unbounded set needed).
  3. **Core open step:** apply the Generalized Bounded Witness Lemma's Corollary to
     (A'_0, B'_0) to recruit a forced prime q ∉ S₀ dividing infinitely many A'_0-type
     terms. Form the refined type A''_0 := A'_0 ∪ {q} (at the enlarged S₀ ∪ {q} level).
     Attempt to show: (a) A''_0 ∩ B'_0 ≠ ∅ is forced by minimality applied one level down
     (since A''_0 is "more refined," i.e., has a different, possibly smaller effective
     signature relative to some canonical comparison) — NOT yet shown, this is the actual
     gap; or (b) derive an outright contradiction from q's simultaneous membership
     requirements across ALL of A'_0's disjoint partners at once (a genuinely new
     "simultaneous multi-way pigeonhole," per the closure explorer's Opening 1) forcing
     q to already have been in S₀, contradicting q ∉ S₀ from the Corollary.
  4. If Step 3 succeeds, (†) is fully closed (not just localized); proceed to Step 5's
     CRT + cyclic pigeonhole finish (shared, unchanged).
Key lemmas (claim + mechanism):
  - μ-minimal violating pair exists — because 𝒫' × 𝒫' is finite (𝒫' itself finite by the
    Extended Persistent-Type Pigeonhole), so the set of violating pairs, if nonempty, is
    a nonempty finite set of nonnegative integers under μ and has a minimum by the
    well-ordering principle — trivial but must be stated since it's the backbone of the
    contradiction structure.
  - Recruited-prime contradiction (OPEN, not proved) — because the Generalized Bounded
    Witness Lemma's Corollary is unconditional and always fires on a genuine violation,
    giving concrete new data (the prime q) to reason about; whether this data forces a
    strictly smaller violation or an outright contradiction is exactly the content still
    missing, and is the same underlying difficulty as the recruitment process's
    termination question, now approached via well-ordering instead of forward
    induction — a different proof style may find a leverage point induction did not
    (e.g. minimality lets you assume NO smaller violation exists, a hypothesis the
    forward process never gets to use).
Open gaps: Step 3's core contradiction is entirely open; this is a fresh attempt at the
same underlying difficulty from a different angle, explicitly not a rehash of the
recruitment-process framing.
Cases to cover: none new.
Watch out for: this approach's target and the covering-system-construction's residual
are THE SAME underlying mathematical fact (†) restricted to non-canonical ×
non-canonical pairs — if one builder closes it, the other approach should import the
result rather than re-deriving; do not treat a success here as requiring
covering-system-construction to redo the same work independently.
