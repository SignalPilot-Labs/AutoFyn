## imo-2026-06

- Distinct openings:
  1. **Refined minimality conjecture (main finding this round).** Rather than attacking
     (†) in its fully general "any two disjoint extended-persistent types intersect"
     form, attack the much sharper and empirically very clean statement: *let p\* be
     the smallest prime not in Q = P(a_1) (when 2 ∉ Q, p\* = 2). Then for all
     sufficiently large n, p\* | a_n whenever τ(n) ⊊ Q (i.e. whenever the base type is
     a PROPER subset of Q).* If true, this trivially closes (†): any two disjoint base
     types A, B are automatically proper subsets of Q (they can't both equal Q since
     they're disjoint and Q ≠ ∅), so both their extended-persistent refinements
     contain p\*, hence intersect through the single fixed prime p\* — no case analysis
     over refinements needed at all. This turns (†) from an abstract combinatorial
     consistency claim into a concrete "one universal glue prime" claim, which is the
     kind of statement a minimality/greedy argument is well suited to attack directly
     (see numerical evidence below — it is essentially 100% confirmed on every seed
     tested).
  2. **Case split on whether 2 ∈ Q.** The numerics show the two regimes behave
     completely differently: if 2 ∈ Q, ALL persistent types (not just proper subtypes)
     empirically contain 2 — in fact every large-n term becomes even, so there ARE no
     disjoint persistent base types with a genuine linking problem (Q's own structure
     already reconciles everything, since 2 is shared by every type). If 2 ∉ Q,
     disjoint proper-subtype pairs occur, and 2 is recruited as the universal glue.
     This suggests the outline should split the top-level proof into these two cases,
     with the 2∈Q case being nearly free (all terms eventually even ⟹ trivially
     pairwise linked) and the 2∉Q case reducing to opening 1's conjecture.
  3. **A "why 2 wins" mechanism worth formalizing:** among candidates for a_{n+1} of a
     given required Q-type A ⊊ Q, being additionally even is "free" in the following
     sense — half of all integers of any residue class are even, so an even candidate
     satisfying the Q-constraints is typically encountered no later than (and often
     much sooner than) an odd candidate that has to separately reconcile with every
     disjoint-from-A persistent type using distinct odd primes. This is exactly the
     "greedy prefers the cheap universal glue" intuition the reviewer flagged. The
     concrete monovariant candidate: compare, for large n, the smallest even number
     ≡ (valid Q-pattern) exceeding a_n against the smallest odd number satisfying the
     full compatibility requirement, and show the even one is always smaller once the
     persistent-type structure has stabilized. This is a genuine, attackable
     quantitative comparison (not just an appeal to "clearly cheaper") — it has NOT
     been carried out rigorously by either approach or by this exploration; it is the
     natural next target.
  4. **Bypass framing (independent of 1–3):** even without proving "2 is forced,"
     one could try to show directly that S (finite core theorem's set) already
     contains a single prime common to every element of 𝒫 (not just 𝒫' refinements) —
     this is a strictly stronger and cleaner target than (†) as stated, and matches
     what's actually observed numerically (a single universal prime, not merely
     pairwise-intersecting families).

- Candidate technique(s): minimality/greedy-smallest-candidate comparison (an explicit
  size comparison between an "even" candidate and an "odd, ad-hoc-linked" candidate);
  combine with the already-certified Bounded Gap Lemma and Bounded Witness
  Lemma/Finite Core Theorem (`knowledge_base.md` "Pigeonhole / extremal principle",
  "Modular arithmetic, CRT", "Invariants & monovariants" — the last is the right KB
  entry name for the "why would greedy ever introduce a fresh prime" argument).

- Cheap-kill candidates: parity/case-split on 2 ∈ Q vs 2 ∉ Q is a genuine structural
  reduction, not just a heuristic — cheaply split the whole proof into these two
  regimes before doing anything else; the 2 ∈ Q regime looks close to free based on
  the numerics (every persistent type observed already contains 2, so no disjoint
  pair ever arises to reconcile).

- Knowledge-base entries to use: "Pigeonhole / extremal principle", "Modular
  arithmetic, CRT" (already used by both live approaches), and "Invariants &
  monovariants" (not yet invoked by either live approach — this is the natural entry
  for the "smallest prime not in Q becomes forced" argument the reviewer asked to
  explore).

- Analogous past problems (cruxes): `aimo-0421` (number_theory,
  divisibility-and-gcd) — crux "gcd of a fixed element with a varying one is always a
  divisor of that fixed element, hence takes only finitely many values over an
  infinite family" is essentially the same mechanism as the already-certified Bounded
  Witness Lemma / Finite Core Theorem (not new, but confirms those lemmas are the
  standard move, so the remaining gap (†) is genuinely the novel difficulty, not a
  standard pigeonhole one likely to have an off-the-shelf crux). No crux in the
  corpus targets the specific "one universal glue prime gets recruited" phenomenon
  found here — nothing closely analogous was found for that part; do not force a
  match.

- Prior progress: see `results/imo-2026-06/current.md` — Free Facts, Bounded Gap
  Lemma, Persistent-Type Pigeonhole, Bounded Witness Lemma, and Finite Core Theorem
  are all certified and correct (in `lemmas/`). Both live approaches
  (`amortized-charging-budget`, `covering-system-construction`) are stuck on
  essentially the same gap (†) / Core Lemma: whether disjoint-base extended-persistent
  types must intersect. Neither has identified or tested the sharper "p\* = smallest
  prime outside Q is a universal glue" conjecture — that is new this round.

- Dead ends (do not retry): the "naive charging/recruitment" argument in
  `amortized-charging-budget` Section 5 (tries to bound ∪ p(i,A) directly without
  identifying which prime is doing the work) — confirmed by this round's numerics to
  be the wrong level of generality: it treats the witness prime as potentially
  different for every (i,A) pair, when in fact (empirically) it is almost always the
  SAME single prime (2, or more generally the smallest prime not in Q) across all
  pairs simultaneously. Do not retry the fully general "witness map could be
  unbounded" framing without first testing whether it collapses to a single universal
  prime, since that appears to be exactly what happens.

- Small-case / intuition notes (all conjectural, verified only numerically):
  - a_1 = 6, 10, 12 (Q = {2,3}, {2,5}, {2,3}): 2 ∈ Q in all three; persistent base
    types found were {2} and {2,3} (or {2},{2,5}) — never disjoint from each other,
    consistent with opening 2's claim that 2 ∈ Q trivializes the disjoint-pair issue.
  - a_1 = 15 (Q={3,5}, 2 ∉ Q): persistent base types {3}, {5}, {3,5} (disjoint pair
    {3},{5} exists). Checked extended refinements over a window of 800 terms deep in
    a length-1500 sequence: type {3} → extended type {2,3} in 400/400 = 100% of
    occurrences; type {5} → {2,5} in 200/200 = 100%; only the FULL type {3,5} (not
    disjoint from anything) splits 50/50 into {2,3,5} and {3,5}. This exactly matches
    opening 1's conjecture (proper subtypes are 100% glued via 2; the full type,
    having no disjoint partner, is free to vary).
  - a_1 = 105 (Q={3,5,7}, 2∉Q), checked on a window of 5000 terms deep in a
    length-8000 sequence: ALL SIX proper-subset persistent base types — {3},{5},{7},
    {3,5},{3,7},{5,7} — were divisible by 2 in EXACTLY 100.0% of their tail
    occurrences (n = 2069, 1034, 689, 518, 345, 173 samples respectively, zero
    exceptions). Only the full type {3,5,7} (172 samples) split close to 50/50
    (0.500) between even and odd. This is a strikingly clean confirmation of opening 1
    across a case with three disjoint singleton types simultaneously present.
  - a_1 = 30, 210 (Q ⊇ {2,3,5} resp. {2,3,5,7}, so 2 ∈ Q): every persistent type
    observed in the tail (all types with frequency > 20 in a 2000–3000 term window)
    contained 2 — in fact for a1=210 100% of ALL sampled tail terms (regardless of
    type) were even. No disjoint pair of persistent base types was observed to exist
    at all in these seeds, again consistent with opening 2.
  - Caveat: this is small-case/numerical evidence only (finite windows, ~10-30
    persistent types checked across 6 seeds), not a proof, and does not yet explain
    WHY 2 (rather than some other prime, or no single prime) is always the one
    recruited — only that empirically it always is, and always with frequency
    essentially 1 rather than merely "positive density." The rigorous content still
    needed: (a) prove the greedy rule forces evenness for proper-subtype terms once
    the process has stabilized (the actual minimality/monovariant argument, not yet
    attempted here), and (b) handle the 2 ∈ Q case, where the analogous claim would
    presumably be about a different distinguished prime (untested — no seed with
    2 ∈ Q but a genuine disjoint-type pair was found in this session; worth
    constructing one, e.g. by searching for a_1 divisible by 2 but with a large
    enough Q to force two disjoint persistent subtypes, to see what prime — if any —
    plays the analogous role there).
