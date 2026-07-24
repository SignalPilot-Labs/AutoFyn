# Proof review — imo-2026-06, round 2

Reviewed: `covering-system-construction.md`, `greedy-exchange-cost-potential.md`.
Also read `current.md` (pre-update), `lemmas/*.md`, `/tmp/round-2/outline-reviewer.md`.

## 1. Retraction verification (both files)

Independently re-simulated the a_1 = 35 sequence (python, `sympy`, brute-force greedy
construction). Confirmed:
- The persistent base type {5} (⊊ Q = {5,7}) recurs with ODD terms deep in the tail
  (e.g. an index ~154 term = 975 = 3·5²·13), a recurring pattern, not a finite set of
  early exceptions — matching the outline-reviewer's report almost index-for-index.
- The true eventual period is exactly T = 34, L = 210 = 2·3·5·7 (verified by direct
  simulation to 2000 terms and consistency-checked over the last 500 terms) — i.e. the
  reconciling core needs the TWO extra primes {2,3}, not a single "universal glue
  prime," and not a bounded cost of 1.

Both files' retractions are **genuine**:
- `covering-system-construction` clearly labels the retracted "Universal Glue Prime
  Lemma + sparse/dense split" (Step 4b) with a retraction notice at the top, keeps the
  retracted text only "for the record," and does not reintroduce the single-prime claim
  anywhere in the replacement content (Step 4c). The Step 4c "computational evidence"
  section proposes a *different*, correctly-labeled-as-conjectural claim ("S from Step 3
  needs zero further recruitment rounds") — this is NOT the same as the retracted claim
  (it is about the closed prime SET, not a distinguished single prime), so there is no
  smuggling-back.
- `greedy-exchange-cost-potential` retracts both the "cost(n) ≤ |𝒫|-1" bound (already
  retracted before this round) and the new "cost(n) ≤ 1 sparse regime" conjecture, with
  the same falsifying data reproduced explicitly (including the observation that a_153 =
  975 has a third, irrelevant "junk" prime 13 — a good, correct diagnostic that the raw
  cost quantity is not even the right invariant). No trace of the retracted claims
  survives into Lemmas A/B/C or the |Q|=1 case.

Both retractions pass. No hidden reintroduction found.

## 2. New lemma verification

**Generalized Bounded Witness Lemma (S₀-level)** (`covering-system-construction`,
Step 4c): re-derived independently. The proof is literally the certified Bounded
Witness Lemma's proof with Q → S₀ throughout; checked that the original proof never
used any property of Q beyond "fixed finite set intersected with P(a_n)" — confirmed,
it goes through verbatim. Correct, unconditional, no circularity (uses only Free Fact 2
and the definition of ρ). Its Corollary (Recruitment step) is a straightforward
infinite-pigeonhole application on top, also correct. **Certified** to
`lemmas/generalized-bounded-witness-lemma.md`.

**Lemma A (Generalized Bounded Gap fact)** (`greedy-exchange-cost-potential`):
re-derived independently — "smallest multiple of c exceeding a_n is ≤ a_n + c" is
correct (standard interval argument, including the boundary case a_n already a
multiple of c), and legality against every earlier index follows from Free Fact 2
exactly as claimed (each q_i ∈ Q dividing both a_i and a_1 also divides c, hence r).
Correct, unconditional. **Certified** to `lemmas/generalized-bounded-gap-lemma.md`.

**Lemma B (Single-Witness-Prime Pigeonhole Refinement)**: a direct, correct
application of the infinite pigeonhole principle to the certified Bounded Witness
Lemma's output (finite target set F_{A,B}, infinite domain of qualifying indices).
Correct, unconditional, and honestly disclosed as insufficient to close (†) (does not
extend to non-canonical witnesses without risking primes outside S₀). **Certified** to
`lemmas/single-witness-prime-pigeonhole.md`.

**Lemma C (Extended Persistent-Type Pigeonhole)**: identical mechanism to the
certified Persistent-Type Pigeonhole lifted to S₀ instead of Q — correct,
unconditional. Essentially the same content as `covering-system-construction`'s own
𝒫' construction in its Step 4 (both independently and correctly derived — not
circular, since neither depends on the other, and the mechanism is elementary
pigeonhole). **Certified once**, as the canonical shared statement, to
`lemmas/extended-persistent-type-pigeonhole.md`.

No circularity found in any of the four new lemmas: none of them assumes (†) or any
of its equivalents: they build only on the certified round-1 lemmas (Free Facts,
Bounded Witness Lemma, Finite Core Theorem, Persistent-Type Pigeonhole) plus the
infinite pigeonhole principle.

## 3. Is gap (†) actually closed by either approach? (adversarial hunt)

No. I looked hard for a hidden closing move in both files' "recruitment process" /
"Lemma B+C combination" sections, since both report getting close. In both cases the
stated obstruction is genuine, not just an unfinished write-up:

- `covering-system-construction`'s Step 4c process is only shown to be well-defined
  per round; termination (finitely many rounds) is not established, and the three
  monovariant candidates tried (persistent-extended-type count, "reconciled pairs stay
  reconciled," growth-rate/ω(a_n) bound) are each shown, correctly, not to work — I
  checked the "reconciled pairs stay reconciled" argument myself: it is true that if
  A', B' already share a fixed prime p ∈ S₀^(k), every refinement in later rounds still
  shares p (refining only adds primes, never removes), so already-settled base-type
  pairs stay settled — but the gap the file identifies (a single round's recruitment
  need not settle ALL extended refinements of a base-type pair at once) is real: I
  could not construct a proof that one round always fully settles a whole base-type
  pair either, so this really is where the argument stalls, not a dressed-up version
  of something already provable.
- `greedy-exchange-cost-potential`'s Lemma B+C combination stalls precisely because
  the argument needs a witness realizing the SAME extended type B' as the one under
  consideration, and the only certified control on a witness's factorization
  (P(a_m)\Q ⊆ S) is established solely for the CANONICAL witness of the BASE type, not
  for an arbitrary witness of a specific EXTENDED refinement. I tried substituting the
  canonical witness m_B directly into the extended-level argument myself; it fails for
  the same reason the file gives — ρ(m_B) need not be the specific B' in question,
  since a single base type can be realized by several different extended refinements
  and the canonical witness only exhibits one of them. This is a genuine gap, not
  hand-waving dressed as one.

Both approaches converge on the identical underlying obstruction (an arbitrary
witness's full factorization is not controlled to avoid primes outside the current
finite core), described in two different vocabularies (recruitment-process halting vs.
witness-pigeonhole). This is strong independent confirmation that (†) — in whichever
of its now-several equivalent forms — is the genuine mathematical crux, not an
artifact of a particular framing's imprecision. I attempted no fewer than three
independent closing strategies myself in the time available (a monovariant on total
number of "settled" base pairs weighted by round; a direct argument that the canonical
witness's OWN extended type must already be extended-persistent by a secondary
pigeonhole; and a density/growth argument bounding total distinct recruited primes via
the O(N) growth of a_n) — none succeeded, each hitting the same wall the builders
report. I did not find a subtle closing move; (†) remains genuinely open.

## 4. Verdicts

### covering-system-construction — CHANGES REQUESTED
Status: **partial** (matches the file's self-report; not overclaimed). Real, certified,
unconditional new content this round (Generalized Bounded Witness Lemma S₀-level +
Corollary), a correct retraction of a falsified claim, and a sharper reformulation of
(†) as an exact halting question. Gap (†) itself remains open — precisely located as
"does the recruitment process of Step 4c terminate in finitely many rounds," with a
concrete, computationally-supported (but unproved) sharper conjecture ("zero further
rounds beyond the original S"). Recommend next round target this sharper conjecture
directly rather than general termination.

### greedy-exchange-cost-potential — CHANGES REQUESTED
Status: **partial** (matches the file's self-report). A genuinely different framing
that independently converges on the same crux — this is legitimate population
diversity, not a wasted slot, and its own unconditional deliverables (Lemma A, B, C,
and the fully resolved |Q|=1 case) are real and reusable. The correction this round
(retracting the false "C=1 sparse regime" conjecture with explicit falsifying data) is
honest and correctly executed. Gap (†) remains open for |Q| ≥ 2, at the same
underlying obstruction as the sibling approach.

Neither approach is fundamentally broken (no RETHINK): both retain valid, growing
certified content and correctly, precisely locate the remaining difficulty rather than
hand-waving past it.

## 5. Promotable lemmas certified this round

- `lemmas/generalized-bounded-witness-lemma.md` (from `covering-system-construction`) —
  certified, includes its Recruitment-step Corollary.
- `lemmas/generalized-bounded-gap-lemma.md` (from `greedy-exchange-cost-potential`,
  Lemma A) — certified.
- `lemmas/single-witness-prime-pigeonhole.md` (from `greedy-exchange-cost-potential`,
  Lemma B) — certified.
- `lemmas/extended-persistent-type-pigeonhole.md` (independently derived in both
  approaches with identical content — certified once as the canonical shared
  statement, noting both sources).

## 6. current.md

Rewritten (reviewer-owned) to merge all live approaches' non-overlapping unconditional
content, the reformulated gap (†) statement, the independent verification of both
retractions, and the three failed monovariant candidates (so a future round does not
re-try them). Status remains `partial`. No `## Full proof` section (not solved).

## Summary

Round 2 verdict for both built approaches: **CHANGES REQUESTED**, Status **partial**.
No approach reaches `solved`. Gap (†) — now reformulated as an exact halting question
for a rigorously-defined recruitment process — remains the genuine crux, independently
confirmed via my own closing attempts and via both approaches converging on the same
underlying obstruction from different vocabularies. Four new lemmas certified this
round as reusable, gap-free content. Both approaches' round-2 retractions of falsified
shortcut conjectures ("universal glue prime," "cost ≤ 1 sparse regime") were verified
genuine by independent simulation (a_1=35: true core {2,3}, T=34, L=210) and are not
secretly reintroduced.
