# Outline review — round 6 — imo-2026-06

Read: `/tmp/round-6/proof-outliner.md`, `results/imo-2026-06/current.md`, all
`results/imo-2026-06/approaches/*.md` (round-6 sections), `results/imo-2026-06/lemmas/`,
`CLAUDE.md`, `knowledge_base.md`. Cross-checked file mtimes (all 5 nominated approach
files modified 01:44–01:48 UTC, consistent with the outliner report timestamp — no
repeat of round 2's "report not persisted to disk" failure) and spot-ran the naive
majorization candidate numerically (below).

## 1. renormalization-induction-on-seed — revise — APPROVE

New general Lemma "a_2 = a_1 + p, p := min R(a_1), for every a_1 > 1" is a clean
3-line minimality argument (checked: for 1 ≤ t < p no prime factor of a_1 can divide
t since all prime factors are ≥ p > t, so gcd(a_1+t,a_1)=gcd(t,a_1)=1, invalid; a_1+p
is a genuine multiple of p, valid; minimality gives a_2 = a_1+p). Correct and a real
generalization of the existing squarefree-two-prime Lemma 4.1. The corollary (odd a_1
⟹ a_2 even, forcing 2 into the active set at index 2) is immediate and correct.

The "two covering agents" mechanism (step 3, proving 2 stays a valid covering agent
against the WHOLE growing prefix, not just a_1,a_2) is honestly flagged as the open
technical step, not asserted. The outline correctly requires BOTH branches (lock
succeeds forever vs. lock eventually fails) be covered — no missing case. The
"2 | L whenever lock fails" conjecture is explicitly labeled conjecture (26/26
numerically resolved, no proof claimed) — no overclaiming. Dead ends (naive
permanent-locking, bounded-lookahead, single-congruence classifiers) correctly
excluded per the Rules. Sound, no circularity, real forward step (a strictly more
general free lemma plus a sharper, honestly-scoped open target). No issues.

## 2. active-set-stabilization — revise — APPROVE

The Bounded-Witness-Index Conjecture reframes "is Nec finite" (existential, about an
infinite process) as "is there an explicit computable N(a_1) bounding the first-witness
index" (a statement about a finite prefix) — this is a genuine sharpening, not a
relabeling: it changes the proof strategy from abstract compactness to strong
induction on a bounded prefix, using already-certified facts (Multiple-of-R
Realization, Same-Class-Free reduction) as raw material. Correctly distinguishes this
from the round-5/6-refuted "per-class-pair O(1) contribution" mechanism (the a_1=35
and a_1=194287 data honestly show per-pair contributions are unbounded, so any valid
bound must live on the index j, not a per-pair count — this refutation is stated
precisely and does not overreach into claiming the index-bound approach itself is
refuted, correctly). The a_1=20735 outlier (witness index 69) is flagged as a
diagnostic instance, not yet explained — appropriately left open, not asserted solved.
No circularity (the induction is on the bounded prefix index j, not on any assumed
eventual period). Sound.

## 3. state-compactness-pigeonhole — advance (hand-trace mechanism) — APPROVE

Correctly targets the same shared central gap as active-set-stabilization via a
genuinely different, complementary mechanism (bottom-up hand-tracing of the a_1=20735
outlier vs. top-down abstract induction) — this is legitimate mechanism-diversity on a
shared hard lemma per CLAUDE.md's guidance (memory rule: not every shared-gap
convergence is a same-framing collapse if the mechanisms differ). Verified the
underlying sequence for a_1=20735 numerically myself (first 10 terms match: 20735,
20740, 20745, 20748, 20750, 20755, 20760, 20770, 20775, 20780 — consistent with the
outline's setup); did not re-verify the full witness-index-69 claim (expensive,
previously reviewer-checked per explorer report) but the setup is internally
consistent. Explicitly cross-checking against 2-3 fast seeds (a_1=385, 194287) before
generalizing guards against overfitting to one outlier — good discipline, correctly
required. No claim of a closed-form or proof yet; correctly scoped as
instance-diagnosis feeding a future general claim. Sound.

## 4. scalar-difference-pigeonhole — revise (Morse-Hedlund reformulation) — APPROVE, with one required fix

The vocabulary shift to factor-complexity p(k) and citing Morse-Hedlund by name is
legitimate and correctly distinguished from the already-killed windowed-epsilon
mechanism (Morse-Hedlund only needs SOME k with p(k) ≤ k, not a fixed small window —
genuinely weaker/different requirement, not re-attempting a dead mechanism). However
the outline's own step 1 self-flags an unresolved subtlety that must be treated as a
mandatory fix, not an optional nicety: the "Complexity Bound Lemma" as stated bounds
the number of distinct SUMS g_n(k) can take, not the number of distinct length-k
FACTORS p(k) — since two different factors can sum to the same value, p(k) could a
priori exceed the number of distinct sums. The outline does flag this itself ("state
carefully whether the bound is on sums or factors, and fix the argument if it only
bounds the former") — good, but this needs to be elevated to a required first
deliverable for the builder (per memory rule: a self-flagged gap must be resolved
before investing in dependent steps), not left as one bullet among several. Also
correctly requires the even-a_1 sanity check (p(k)=1 constant sequence) before
extending. No case-coverage issue (case-free reformulation). One fix required:
builder must resolve the sums-vs-factors gap as step 0 before attempting to sharpen
the bound toward ≤k.

## 5. scalar-difference-majorization (new copy of scalar-difference-pigeonhole) — APPROVE, registered via copy_approach

Registered as a copy of scalar-difference-pigeonhole (inherits Elo/counts per
CLAUDE.md's copy semantics — a genuine second, independent mechanism for the same
open syndeticity gap, not a split of one proof: majorization/domination is a
structurally different technique from Morse-Hedlund complexity). I ran the outline's
own mandatory first numerical check myself (a_1=35, naive candidate â_n = a_1+(n-1)·5):

```
n=1:  a_n=35   â_n=35   diff=0
n=6:  a_n=60   â_n=60   diff=0
n=11: a_n=90   â_n=85   diff=5
n=21: a_n=160  â_n=135  diff=25
n=31: a_n=220  â_n=185  diff=35
n=40: a_n=270  â_n=230  diff=40
```

This confirms the outline's own prediction exactly: the excess grows roughly linearly
once the lock breaks (true eventual rate L/T=210/... exceeds p=5), so the naive
candidate is NOT boundedly-majorized — the outline correctly anticipates this as the
likely outcome and does not claim otherwise; it directs the builder to fall back to
the relaxed real-valued affine majorant using the Positive-Density Upgrade's witnessed
rate. This is honest, testable, and appropriately scoped as possibly a negative
result ("if no candidate is numerically bounded, report as a genuine negative result
rather than force a proof") — exactly the right epistemic posture for a brand-new,
entirely-open mechanism. No issues.

## Cross-cutting checks

- **Diversity**: the field spans 4 genuinely distinct top-level framings — Q/Nec
  set-existence (active-set-stabilization, state-compactness-pigeonhole, same shared
  gap but different mechanisms), induction-on-seed-structure
  (renormalization-induction-on-seed), and prime-free scalar framing
  (scalar-difference-pigeonhole / scalar-difference-majorization, two independent
  mechanisms on one shared sub-gap). This satisfies CLAUDE.md's plateau-break
  requirement — the Q/Nec line has been open 4 rounds (8 dead mechanisms) but the
  population is not collapsed to it.
- **No dead-end repeats**: none of the 5 nominated approaches re-attempt any of the 8
  dead mechanisms logged in run_state.md's Rules (checked each outline's "watch out
  for" section against the Rules list — all consistent).
- **No fragment-of-one-proof issue**: each of the 5 approaches targets the full IMO
  claim end to end (T,L existence), none is a sub-lemma masquerading as a whole
  attempt.
- Deprioritized/dead approaches (jacobsthal-covering-bound, frozen-invariant-
  monovariant, bounded-link-invariant, growth-rate-contradiction) correctly excluded
  from this round's nominated field per current Rules; still ranked below for Elo
  anchoring purposes only, not proposed for build.

## Ranking

Registered `scalar-difference-majorization` via `copy_approach` (source
scalar-difference-pigeonhole). Ran `update_ranking` anchoring the new fork and all
five nominated approaches against the established/dead members of the population
(14 comparisons: established beats deprioritized/dead in 6 pairs; new fork anchored
against both a dead sibling — wins — and its live source/near-peers — draws, since it
has produced no result of its own yet; top three re-confirmed against each other).
Post-update Elo: state-compactness-pigeonhole ~1668 (highest), active-set-stabilization
~1598, renormalization-induction-on-seed ~1546, scalar-difference-majorization ~1543,
scalar-difference-pigeonhole ~1532, frozen-invariant-monovariant ~1478 (deprioritized),
bounded-link-invariant ~1397 (dead), jacobsthal-covering-bound ~1381 (deprioritized).

## Build set

All 5 nominated approaches pass review (APPROVE, one with a required-fix note for
scalar-difference-pigeonhole). Build all 5 in parallel — each owns a distinct
mechanism/file, no collisions, and per-round routing lets each be judged
independently next round regardless of this round's Elo ordering.

build set: renormalization-induction-on-seed, active-set-stabilization, state-compactness-pigeonhole, scalar-difference-pigeonhole, scalar-difference-majorization
