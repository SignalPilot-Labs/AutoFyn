# proof-builder report — forced-primes-well-ordering, round 12

## Task
Per the outline-reviewer's scope correction: verify whether a_1=4199's pair
(S,S')=({13},{17}), specifically the {13}-side's nonempty-but-not-yet-
realized backbone {2}, could be leveraged by this approach's Local
No-Resurrection/Interval/Equivalence toolkit + Backbone Permanence + Lemma
UCR to close Conjecture (JW), as a second mechanism alongside
sunflower-bundle-closure's. 247:(13,19) confirmed out of scope (no
nonempty backbone on either side) and explicitly ceded to sunflower-
bundle-closure, not attempted here.

## What I did
1. Independently re-generated the a_1=4199 sequence from scratch (own
   smallest-prime-factor sieve to 6,000,000, own factorization, own greedy
   loop — no reuse of prior scripts) to N=12,000 terms, confirming the
   outline-reviewer's figures: {13}-class backbone = {2} (nonempty, 0/2791
   exact realizations); {17}-class backbone = ∅.
2. Rather than stopping at the empirical negative, derived a general
   **Sandwich Uniqueness Lemma**: for the Realized-Backbone/UCR mechanism to
   close (JW) via anchor core z, the covering set W is *forced* (by a
   2-line containment argument, no Backbone Permanence needed) to equal
   B_full(z), the TRUE full class intersection of comp() over all of I_z —
   not merely the observed finite-prefix stabilization value.
3. Applied this to BOTH possible anchors for the pair:
   - z={17}: B_full({17})=∅ proved directly and unconditionally from just
     two concrete terms (comp(a_3)={2,31}, comp(a_5)={3,83}, already
     disjoint) — no asymptotic argument needed.
   - z={13}: B_full({13}) is either {2} (if Backbone Permanence holds on
     this side) or ∅ (if it doesn't) — an exhaustive 2-case dichotomy that
     needs no resolution of Backbone Permanence itself. Case {2}: killed by
     the already-certified Lemma ERD-C (realized/blocked dichotomy) —
     κ={2,13} is blocked by witness a_5=4233 (radical {3,17,83}, disjoint
     from {2,13}), so κ is proved never realized at ANY index, by an
     already-certified lemma, not a fresh argument. Case ∅: fails
     immediately on nonemptiness, same as z={17}.
4. Result: a complete, gap-free, unconditional proof that this specific
   mechanism cannot close (JW) for 4199:(13,17) — stronger than what the
   dispatch anticipated (it doesn't even require resolving whether Backbone
   Permanence holds on the {13} side).

## Outcome
Status stays `partial` for the whole approach (unchanged — this is a
scoped sub-result, not the whole problem). This round's contribution is a
genuine, rigorous negative finding (not a stall, not an overclaim),
plus one new general-purpose lemma (Sandwich Uniqueness Lemma) proposed
for certification. No certified content from prior rounds is touched or
threatened. sunflower-inadmissibility-toolkit's disjoint Case A target and
sunflower-bundle-closure's independent Case B mechanism (which needs no
per-class backbone) are both unaffected.

## File updated
results/imo-2026-06/approaches/forced-primes-well-ordering.md — new
"Round 12 update" section + new §K (Sandwich Uniqueness Lemma, full
resolution of 4199:(13,17) for this mechanism), updated Approaches
tried / Current best / Open gaps / Promotable lemmas sections.

## Promotable lemma proposed
**Sandwich Uniqueness Lemma** (§K Step 1 of the approach file) — general,
fully proved, no dependency on any open hypothesis in this workspace.
