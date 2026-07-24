## imo-2026-06

a1-13q-subfamily-theorem: new
Target: For every prime q>13, q∉Bad(13)={17,19,23,47}, a_1=13q gives
a_n=13(q+n-1) for all n≥1 (literal T=1,L=13 periodicity from n=1).
Technique: Direct strong induction, instantiating the certified p-uniform
machinery (Generalized K_0-Boundedness, gcd-difference Witness Lemma,
Legendre Sieve Gap Bound, Primorial Floor Bound, Universal Look-Back
Witness Identity r=1 corollary) at p=13 — exact mirror of the certified
a1-5q/a1-7q/a1-11q closures. No new tool needed.
Skeleton:
  1. Setup, base case, P(a_1)={13,q} — direct definition.
  2. a_n+1 illegal — consecutive-integer coprimality.
  3. Case (a)/(b) split for j=2..12 — certified gcd-difference Witness Lemma.
  4. Build the 132-cell (j,r,s_0,K_0) table (s_0=j·r^{-1} mod 13) — direct
     computation, independently reproduced twice this round already.
  5. Close k=0, r=1 (12 cells) for free — Universal Look-Back r=1 corollary.
  6. Close k=0, r=2..12 (120 cells): threshold Q_1(j,r), 116 below-threshold
     candidates, 111 witnessed, 5 no-witness = 4 genuine exceptions
     ({17,19,23,47}) + 1 MOOT duplicate ((j,r)=(12,6) at q=19, n_0=3, vacuous
     because q=19 already deviates at the smaller n_0=2 band (6,6)).
  7. Verify the 4 genuine exceptions are permanent (every smaller candidate
     illegal at the deviation index) — direct factorization, 4 cases.
  8. Close k≥1 (residual band k=1..11 via the s*=5 threshold analog
     (s+1)!≥25+(13/17)2^{s+1}(s+2)): 29 below-threshold quadruples, 19 moot,
     10 non-moot, all witnessed — Legendre Sieve Gap Bound + Primorial Floor
     Bound at p=13.
  9. Assembly into the strong induction.
Key lemmas (claim + mechanism):
  - 132-cell table is exhaustive/correct — because s_0=j·r^{-1} mod 13 is
    the unique solution of a linear congruence, q-independent.
  - Bad(13)={17,19,23,47} exactly, q=19's second band is moot — because the
    sequence already leaves H(n) at the smaller n_0=2 window, so the
    premise for the (12,6) band never holds in the real sequence; verified
    no other of the 20 multi-band primes has this pathology.
  - k≥1 residual shrinks to {1,...,11} (smaller than a1-11q's {1,...,14})
    — because q_min=17>13 makes the linear term grow faster relative to
    the fixed sieve constants.
Open gaps: full table build, 116-candidate k=0 witness search (with the
moot-cell care point), and the 1452-combination k≥1 sweep are all unbuilt
(routine, but must be written out with every gcd shown, not asserted).
Cases to cover: r=1 (free); r=2..12 k=0 (116 candidates, 4 exceptions + 1
moot); all cells k=1..11 (29 quadruples, 19 moot/10 non-moot).
Watch out for: the q=19 double-band moot cell — must be explicitly proved
vacuous, not silently dropped or double-counted as a 5th exception.

bipartite-network-invariant-fah: new
Target: The full problem statement (existence of T,L with a_{n+T}=a_n+L for
all n), attacking the SAME certified open(k)→∅ reduction target (Step
8.2-8.3 of covering-system-construction.md) as the existing FAH-mechanism
approaches, via a structurally different route.
Technique: growing bipartite-network invariant with local repair-on-failure,
adapted from crux aimo-1000 (IMO 2021 P6 ferry islands, combinatorics/
processes-and-algorithms) — track evolving finite index sets A,B (not a
single witness pair) with invariant "every index in A shares a prime with
every index in B," repaired (not shrunk) on local failure via this
problem's own Free Facts/Bounded Witness Lemma stack, then grown by
absorption until a final pigeonhole finishes. This is the first pickup,
since round 3's Step 4f flag, of a "simultaneous/joint" object rather than
a single-pair monovariant or FAH restatement — genuinely far from the
30+-mechanism graveyard (confirmed via grep across all approach/lemma files
this round).
Skeleton:
  1. MANDATORY FIRST STEP — cheap disambiguation check (do this before any
     general lemma-writing): does a repair-prime always exist when a later
     A'-occurrence fails to share the original linking prime q with the
     network? Test directly on both known hard rogue-pair seeds (a_1=4807,
     11305) plus 2-3 fresh moderate seeds, using the certified Generalized
     Bounded Witness Lemma/Free Facts stack — NOT assumed, computed.
  2. If step 1 succeeds: formalize the growing network A_k,B_k and prove
     the repair operation preserves "complete bipartite network" under the
     actual greedy-gcd legality rule — direct construction + induction.
  3. Growth to cover all occurrences, via a structurally different second
     argument (not step 2's mechanism), using the certified Collateral-
     Safety Theorem's monotone-open-pair-count guarantee.
  4. Final pigeonhole giving Cofinite FAH — combine with the certified
     Cofinite Sufficiency Lemma (already shown to suffice for the existing
     CRT+cyclic-pigeonhole finish).
  5. Assembly into the Master Conditional Theorem's Step 8.2-8.5 chain.
Key lemmas (claim + mechanism):
  - Step 1's disambiguation question IS the crux of the whole approach —
    aimo-1000's repair step is bespoke to that problem's exact-one-of-two
    toggle rule; whether an arithmetic analog exists here must be
    established from the actual Bounded Witness Lemma guarantee (shared
    prime with EACH disjoint witness, NOT — per the round-23 recorded
    false-strengthening trap — a bound on total distinct primes used).
  - Network-count monotonicity (step 3), if reached, is importable for free
    from the already-certified Collateral-Safety Theorem, no re-derivation
    needed.
Open gaps: everything downstream of step 1. If step 1 fails, report a
precise negative and stop — do not force steps 2-5.
Cases to cover: none yet; emerges from step 1's answer.
Watch out for: do not conflate with the already-dead orbit-merging-
additive-offset-dichotomy (round 22, #31 dead, a scalar not a set-valued
invariant, and mistargeted to H2) — this tracks a genuinely different
set-valued joint object and targets H1's open(k)→∅ directly. If step 1's
disambiguation fails outright, RETHINK fast (round-5 reversible-
transition-map precedent) rather than iterating for multiple rounds.

a1-17q-subfamily-theorem: new (secondary/optional — only dispatch if the
round has spare builder capacity beyond a1-13q)
Target: For every prime q>17, q∉Bad(17)={19,23,29,31,37,43,61,67}, a_1=17q
gives a_n=17(q+n-1) for all n≥1.
Technique: identical p-uniform machinery instantiated at p=17; same
9-step skeleton as a1-13q with p=17 substituted (256-cell table instead of
132). Only the greedy-resimulation-level Bad(17) has been confirmed this
round (by the diversity-scout explorer); the full table/threshold/witness
verification (the load-bearing rigor step) has NOT yet been done, unlike
a1-13q which already has it from this round's explorer.
Key lemmas: same shape as a1-13q's — table is a q-independent linear
congruence; exceptions are the no-witness k=0 cells (needs explicit
verification, not yet done).
Open gaps: full table build, k=0/k≥1 witness searches, and an explicit
audit for duplicate-band moot cells (more likely with the larger 256-cell
table, not less) are all unbuilt.
Cases to cover: same shape as a1-13q, sizes TBD by the builder.
Watch out for: this file rests only on a numeric resimulation so far — do
not let a builder claim "solved" without doing the full table/witness work
that a1-13q already has independently double-verified this round. Lower
priority than a1-13q; dispatch only with spare capacity.

Advance: covering-system-construction (no file change needed this round) —
both known hard seeds (4807, 11305) remain fully closed single-seed; no new
work proposed for it this round (superseded in priority by the new
bipartite-network-invariant-fah approach targeting the same general H1
reduction from a genuinely different angle). Not included in the build set
unless the outline-reviewer judges spare capacity exists.

Advance: a1-pq-subfamily-theorem (no file change needed this round) — this
round's diversity-scout explorer found no new bookkeeping-free angle on
either the r=1 k≥1 residual or the general r≠1 k=0 closure; the one
concrete non-repeat next step (a finite r=1-restricted residual check for
one fixed small p) was flagged but not attempted. Recommend deprioritizing
this file next round in favor of a1-13q/a1-17q, which deliver guaranteed
new APPROVEs at bounded, known cost. Not included in this round's build set.

Do NOT revisit: any of the 30+ dead H1 mechanisms (orbit-merging, monovariant/
well-ordering descent, CRT-glue, sieve/density, martingale/renewal,
Kolmogorov complexity, o-minimality, nonstandard analysis, spectral/operator,
priority arguments/computability, subword-complexity, central-sets/
idempotent recurrence); a1-3qk m=4 (false, round 26); a1-p^2*q (refuted
round 19); a1=6q (already-solved even family in disguise) and a1=15q
(3-distinct-odd-prime-factor family, deviates immediately, no visible
pattern) — both confirmed dead this round by the diversity-scout explorer;
H2 N(S_0)=0 direct attack (foreclosed by round-19 Proposition 3).

Recommended build set (for outline-reviewer): a1-13q-subfamily-theorem
(near-certain 9th APPROVE), bipartite-network-invariant-fah (mandatory
plateau-break framing per CLAUDE.md, disambiguation-check-first), and
a1-17q-subfamily-theorem if capacity allows (secondary, lower priority,
needs its own table/witness work still).
