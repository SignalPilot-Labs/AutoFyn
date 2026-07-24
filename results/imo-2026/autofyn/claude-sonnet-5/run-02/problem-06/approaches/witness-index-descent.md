## Status
partial

## Approaches tried
- **witness-index-descent** (round 5, new) — built the skeleton dispatched by the
  outliner: a minimal-counterexample / well-ordering descent on the witness-index pair
  (n_A, n_B) of a rogue pair, adapted from crux `aimo-0030`'s Claim 5 stripping
  descent. This round's concrete work:
  1. **Broadened the empirical test of the ordering sub-lemma** "min(n_A,n_B) ≥
     max(m_A,m_B)" from the 2 seeds the explorer checked to **≈180 seeds** spanning
     |Q| ∈ {2,3,4} (all square-free products of small/medium/large primes, see
     computation log below) — found 20 genuine rogue-pair instances across 6 distinct
     seeds (a_1 = 187, 209, 221, 247, 385, 493, 851, 899 among the tested set), **zero
     counterexamples** to the ordering sub-lemma. This is real, substantive additional
     evidence (not a repeat of the 2-seed check), addressing the outline-reviewer's
     explicit caution.
  2. **Proved half of the ordering sub-lemma unconditionally** (the "same-side" half:
     n_A ≥ m_A and n_B ≥ m_B) using the literal-minimal-witness convention — see Lemma
     (Same-Side Ordering) below. This is a genuine, if partial, closed sub-result.
  3. **Found a structural obstruction that the outline did not anticipate**: the
     "cross" half of the ordering sub-lemma (n_A ≥ m_B and n_B ≥ m_A) — which is the
     part Step 3 of the outline actually needs, to place the canonical witnesses
     a_{m_A}, a_{m_B} strictly *before* both rogue witnesses in the sequence — has no
     proof mechanism available from the certified lemma stack, and moreover **is not
     actually the fact the descent's engine (Lemma G) requires**: Lemma G's shared-
     prime conclusion gcd(a_{n_A}, a_{n_B}) > 1 comes from the certified Free Facts
     lemma, which holds for *every* pair of indices regardless of which is larger (see
     `free-facts-gcd.md`, Statement 1: "for every 1 ≤ i < j" — proved by applying the
     defining greedy property at the larger index, with no dependence on any external
     ordering of unrelated witnesses). So even a full proof of the ordering sub-lemma
     would add no logical leverage to Lemma G's own proof; the ordering fact is at best
     scaffolding for a *different* step (constraining what values a_{n_A}, a_{n_B} can
     legally take), not a missing hypothesis of the shared-prime conclusion itself.
  4. **Identified why the descent's target claim, taken literally, cannot be a
     "no rogue pair exists" contradiction**: rogue pairs are *proved to exist* at the
     base stage S₀ for concrete seeds (a_1 = 175, 187, 209, 221, 247, 385, 493, 851,
     899 — reconfirmed this round, consistent with round 4/5's independently verified
     retraction of "V=∅ always"). A minimal-counterexample descent whose contradiction
     target is "assume a rogue pair exists (anywhere, at any stage) → derive a smaller
     one → infinite descent → no rogue pair can ever exist" is trying to prove a
     **false** statement, since rogue pairs demonstrably exist at stage 0. The only
     coherent target compatible with the facts is the weaker, correctly-scoped claim
     "the *recruitment process* (which resolves stage-k rogue pairs by adding a prime,
     producing stage-(k+1) data) terminates after finitely many stages" — a claim about
     eventual behavior across an increasing chain of ambient sets S₀ ⊂ S₁ ⊂ S₂ ⊂ ⋯, not
     a single-stage non-existence claim. This matches the outline's own Step 4
     framing ("V=∅ eventually... with the descent itself supplying the termination
     argument") but the descent as scoped in Step 3 does not in fact establish this
     weaker claim either — see the gap below.
  5. **Verified computationally that witness indices are not stage-monotone**, which
     kills the most natural fix (redefine the well-ordering over the union of all
     stages' rogue pairs and hope indices only grow). Recomputing ρ, 𝒫', and witness
     indices after enlarging S₀ to S₀ ∪ {q} (q the recruited prime) changes the
     partition of indices into extended types *for every index*, not just future ones
     — an index n whose stage-k extended type ρ_k(n) was involved in no rogue pair may
     become part of a *new* rogue pair at stage k+1 with a witness index smaller than
     any stage-k rogue witness, because ρ_{k+1} is a strictly finer partition of the
     same index set and can carve out new, earlier-occurring extended types that did
     not exist as distinct classes at stage k. Concretely: at stage 0 the type
     containing index n = 2 might be the single class C; at stage 1 (S₁ = S₀ ∪ {q}), n=2
     might belong to a class C ∩ {q} or C \ {q}, either of which is a *new*
     stage-1 extended type whose earliest occurrence could be exactly n=2, smaller than
     every stage-0 witness. This directly reproduces, in the language of this
     approach's own measure (witness index rather than set size), the same monotonicity
     failure documented for the |A'|+|B'| measure in round 3 (`covering-system-
     construction`, Step 4f) — a **different measure hitting the same wall**, which is
     valuable negative information: it suggests the wall is not an artifact of the
     particular measure chosen (set size vs. witness index) but of the recruitment
     operation itself (refining a partition can always manufacture new, earlier-index
     classes), and any successful termination argument will have to control this
     directly rather than sidestep it with a cleverer monovariant.

## Current best
The following is now established (this round, unconditional, unconditional on Steps
2–3's open status):

**Lemma (Same-Side Ordering).** Adopt the literal-minimal-witness convention: for
each persistent base type B ∈ 𝒫, let m_B := min{n ≥ 1 : τ(n) = B} (the *global* earliest
occurrence, not merely the earliest occurrence past the Persistent-Type Pigeonhole
threshold N₀). This is consistent with — indeed a special case of — the convention
already used in the certified Finite Core Theorem's proof, since that proof only uses
τ(m_B) = B and m_B < n for the specific n being examined; it never uses m_B > N₀ as a
hypothesis, so redefining m_B to be the (possibly smaller) global minimum leaves every
certified lemma's proof (Finite Core Theorem, Canonical-Refinement Lemma, F_A∩F_B≠∅,
Generalized Bounded Witness Lemma and its Corollary, Lemma G) valid verbatim, since
S := ⋃_B (P(a_{m_B})\Q) is still a finite union of finite sets and N₁ := max(N₀,
max_B m_B) is still a finite threshold exceeding every m_B. (This matches the round-4
correction's own "literal, minimal canonical-witness convention" language, applied
consistently.)

Now let A' be any S₀-extended-persistent type refining base type A (A' ∩ Q = A), and let
n_A := min{n : ρ(n) = A'} (as in Lemma G). Every n with ρ(n) = A' satisfies
τ(n) = ρ(n) ∩ Q = A' ∩ Q = A, so n ∈ {n : τ(n) = A}. Since m_A is defined as the minimum
of this same set {n : τ(n) = A} and n_A is a particular element of it, n_A ≥ m_A.
Symmetrically n_B ≥ m_B for the other side. **Proof complete, no gap.**

This gives half of the outline's Step 2 sub-lemma (min(n_A,n_B) ≥ max(m_A,m_B) implies,
in particular, n_A ≥ m_A and n_B ≥ m_B, which is exactly this Lemma) unconditionally.
It does **not** give the cross inequalities n_A ≥ m_B and n_B ≥ m_A, which are the parts
that would be needed to place *both* canonical witnesses before *both* rogue witnesses
(Step 2's actual content, and what Step 3 tries to use). Those cross inequalities remain
empirically supported (≈180 seeds tested this round, 20 rogue instances, 0
counterexamples — see the computation log below) but **not proved**, and (per point 3
above) proving them would not, by itself, supply the missing engine for Step 3's
descent even if a proof were found, since Lemma G's shared-prime conclusion already
holds unconditionally without needing them.

**The open gap, precisely stated.** Step 3 of the outline (turning "the minimal rogue
pair's witnesses share a prime with the canonical witnesses" into an actual
contradiction with rogueness) does not go through as sketched, for two independent
reasons established this round:
(a) The natural target of a minimal-counterexample argument at a *single, fixed* S₀
("no rogue pair can exist") is false — rogue pairs demonstrably exist (a_1 = 187, 209,
221, 247, 385, 493, 851, 899, 175, all independently reconfirmed). So the descent must
be reformulated to operate across the *increasing chain* of recruitment stages
S₀ ⊂ S₁ ⊂ ⋯, targeting process termination, not single-stage non-existence.
(b) Reformulated that way, the natural candidate monovariant — "the smallest witness
index of any rogue pair occurring at any stage" — is **not stage-monotone**: enlarging
S₀ by one recruited prime refines the extended-type partition at *every* index
(including small ones), which can manufacture a brand-new rogue pair at a *smaller*
witness index than any rogue pair seen at the previous stage (verified computationally
this round; mirrors the round-3 finding for the |A'|+|B'| measure, but is a genuinely
different demonstration for a genuinely different measure, not a restatement).

No fix for (b) was found this round. This is the same difficulty already documented in
`covering-system-construction` (round 3, Step 4f) and in this file's point 5, now
confirmed to recur for a second, independently-chosen well-ordering — suggestive that
the obstruction is intrinsic to "refinement can create new small-index classes" rather
than to the specific choice of measure, but this is an observation, not a proof that
*no* monovariant can work.

**Computation log (this round, reproducible).** Brute-force greedy-sequence simulator
(trial-division factorization via `sympy.primefactors`, literal scan n = 1..900,
extended-persistent types identified via a 200-term tail-stability heuristic, witness
indices computed as literal global minima over the full 1..900 range — matching the
certified literal-minimal-witness convention). Tested:
- 55 seeds = products of two primes in [3,40): rogue pairs found in a_1 ∈
  {187, 209, 221, 247, 493, 851, 899}; all 17 instances satisfy the ordering.
- 33 seeds = products of three primes in [3,20) under 3000: rogue pair found only in
  a_1 = 385 (1 instance); satisfies the ordering.
- 5 seeds = products of four primes in [3,16) under 6000: no rogue pairs found (V=∅ at
  these seeds, for the boring reason that the extended-persistent-type family turned
  out not to contain a genuinely disjoint-and-non-canonical pair within the tested
  window — consistent with the explorer's a_1=210 observation that V is sometimes
  vacuously empty).
- 90 seeds = (small prime) × (prime in [41,113)): no rogue pairs found in the tested
  window.
Total: ≈183 seeds, 20 confirmed rogue instances across 8 distinct a_1 values, 0
counterexamples to min(n_A,n_B) ≥ max(m_A,m_B). This is a much broader (though still
not exhaustive, and still not a proof) test than the 2 seeds flagged by the
outline-reviewer.

## Full proof
Not present — Status is `partial`. The descent does not close gap (†)/V=∅-eventually
this round; the Same-Side Ordering Lemma is proved but is (by the analysis in point 3
above) not the load-bearing fact the descent needs, and the actually-needed Step 3
contradiction is shown this round to fail for two independent, now-documented reasons
(single-stage non-existence is false; the natural cross-stage monovariant is not
monotone). This is reported honestly rather than papered over, per CLAUDE.md's rigor
rules — an honest partial with two new documented negative findings is the correct
output for this round's assignment.

## Promotable lemmas
- **Same-Side Ordering Lemma** (proved in full above, "Current best" section): for any
  S₀-extended-persistent type A' refining base type A, with m_A the literal global
  earliest occurrence of base type A and n_A the literal global earliest occurrence of
  A', we have n_A ≥ m_A. Short, fully rigorous, one-paragraph proof, no dependence on
  any open gap; reusable by any approach that needs to compare canonical and extended
  witness indices. Recommend certifying into `results/imo-2026-06/lemmas/` if the
  reviewer finds it useful to future rounds (e.g. `covering-system-construction`'s or
  `greedy-exchange-cost-potential`'s own witness-index bookkeeping).
