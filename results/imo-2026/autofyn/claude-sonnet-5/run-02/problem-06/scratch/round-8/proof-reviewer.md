# Round 8 proof-reviewer report — imo-2026-06

Two approaches built this round: `covering-system-construction` (revised) and
`seed-coupling-induction` (new). Both independently re-verified from scratch
(re-derivation of the load-bearing step + independent Python reimplementation of
every numerical claim, not just re-reading the prose).

## 1. covering-system-construction — Verdict: CHANGES REQUESTED (Status: partial)

### The dispatched mechanism (Step 8.9, Fixed-Witness Divisor-Chain)

Setup: rogue pair (A', B') at core S₀ with Lemma-G witnesses n_A < n_B, F' :=
P(a_{n_A})\S₀, F'' := P(a_{n_B})\S₀, q* := min(F'∩F''). For A'-type n > n_A define
d_n := gcd(a_{n_A}, a_n). The outline dispatched: pigeonhole d_n over the finite
divisor set of a_{n_A} to find an alternate constant prime r ≠ q* dividing
infinitely many exceptional (q*-not-dividing) A'-type terms, then rule this out via
the dichotomy "(a) r ∈ S₀ ⟹ contradicts rogueness, or (b) r ∉ S₀, subject to a
canonicality sub-question [already flagged by the outline-reviewer]."

**Divisor-Chain Well-Definedness** (d_n ∈ Div(a_{n_A})\{1}, a finite set) — I
re-derived this myself from the definitions: it is immediate from gcd(a_{n_A},a_n)
dividing a_{n_A}, plus Free Facts giving d_n > 1. Correct, trivial, unconditional.

**The core claim to verify: branch (a) of the outline's dichotomy is FALSE.** I
re-derived this independently, without looking at the builder's proof first, then
compared. If r ∈ S₀ and r | a_{n_A}, then since ρ(n_A) = A' by definition of n_A as
A''s witness, r ∈ P(a_{n_A}) ∩ S₀ = A'. That is ALL that "r ∈ S₀" gives you: r is
simply an ordinary element of the set A'. It says nothing about r's relationship to
B'. Rogueness of the pair is exactly "A' ∩ B' = ∅" — a claim that must be violated
by finding a SHARED element of A' and B', not merely any old element of A' in
isolation. So "r ∈ A'" is entirely compatible with A' ∩ B' = ∅ (i.e., with rogueness
persisting) — there is no contradiction. My independent re-derivation matches the
builder's proof exactly. **This is a correct, genuine, and more basic gap than the
canonicality question** the outline-reviewer flagged for branch (b): branch (a)
fails before r's outside-vs-inside-S₀ status even becomes the live question, because
the claimed contradiction in branch (a) itself never materializes. I looked for a
way to patch this (e.g. forcing r ∉ A' via some other certified lemma) and, like the
builder, found none in the current stack (Free Facts, the Bounded-Witness-Lemma
family, Divisor-Restricted Pigeonhole, Critical Prime Dichotomy) — none of these
forces the pigeonholed prime to lie outside A'.

**Certified byproduct: Singleton-Side FAH.** If F'' = {q} is a singleton, then by a
direct, one-line application of the already-certified Generalized Bounded Witness
Lemma (with witness m := n_B), every A'-type n > n_B has a_n divisible by an element
of F'' = {q}, i.e. by q — with literally zero exceptions (the cited lemma already
gives "for ALL such n," not merely infinitely many, so no further pigeonhole is
needed). This is genuinely unconditional, non-circular, and does not depend on any
open hypothesis — I checked the cited lemma's statement (`generalized-bounded-
witness-lemma.md`) and the substitution is exactly correct.

**Independent recomputation of the supporting numerics.**
- a_1 = 187: I regenerated the greedy sequence and Q = {11,17} from scratch; a_5 =
  231 = 3·7·11, a_6 = 462 = 2·3·7·11·... F' = F'' = {7}, both singleton — matches the
  file's claim exactly.
- a_1 = 4807: I regenerated the sequence from scratch (Q = {11,19,23} — note 4807 =
  11·19·23). At the un-recruited core S₀ = Q, using n_A = 6, n_B = 7 (a_6 = 4845 =
  3·5·17·19, a_7 = 4862 = 2·11·13·17 — this matches the round-6 audit-trail record
  for this seed exactly, confirming my sequence generator agrees with all prior
  independent implementations in this workspace), F' = {17,3,5}, F'' = {17,2,13} —
  NEITHER a singleton. I ran my own from-scratch simulation out to N = 3000 terms
  and found 74/1200 later {19}-type occurrences (past n_B = 7) divisible by 17
  (≈6.2%), matching the builder's reported 50/801 (≈6.2%) essentially exactly
  (different sample window, same rate). This independently confirms: (i) the
  general |F'|, |F''| ≥ 2 case genuinely fails cofinite divisibility (not "not yet
  proved," but actually false at this un-recruited core), and (ii) the workspace's
  prior positive computational evidence (a_1 = 187, 209) never engaged this regime,
  since both are singleton cases fully covered by Singleton-Side FAH alone.

### Assessment

The builder's self-reported Status (`partial`) is accurate — Joint FAH remains open
in general, and the file does not overclaim. This round's real content: (1) a more
precise diagnosis of exactly where the dispatched mechanism fails (prior to, not
merely deeper than, the previously known gap), fully verified by independent
re-derivation; (2) one genuine new certified lemma (Singleton-Side FAH) plus one
trivial bookkeeping lemma (Divisor-Chain Well-Definedness); (3) independently
reproduced numerical confirmation that the hard regime (|F'|,|F''| ≥ 2) is where the
real difficulty is, and that it genuinely fails simple cofinite-divisibility at an
un-recruited core (not merely "unresolved"). No overclaim, no hand-waving, no
circularity found. This is genuine, if incremental, forward progress.

**Verdict: CHANGES REQUESTED.**

## 2. seed-coupling-induction — Verdict: RETHINK (Status: unsolved as a mechanism, though correctly self-reported as `partial` for the workspace as a whole)

The approach set up an induction on ω(a_1) = |Q(a_1)| via removing one prime p from
the seed to get a_1' with Q' = Q\{p}, and posited a Seed-Coupling Lemma: an
eventually order-preserving injective correspondence between the reduced sequence's
indices and the original sequence's "Q'-visible" indices (those n with
P(a_n) ∩ Q' ≠ ∅), matching Q'-level types with only a bounded-frequency exception
set.

**Independent re-verification.** I reimplemented the entire check from scratch (own
greedy-sequence generator built directly from the problem's rule, own type-tracking
and comparison routine — not reusing or reading the builder's script before writing
mine) and reproduced every reported number:

- a_1 = 105, remove p = 7 (Q' = {3,5}): mismatch density stabilizes at ≈55.0% from
  N=100 up to N=8000 in my own run (I obtained 55.02% at N=8000, matching the
  builder's reported number to 4 significant figures).
- Limiting type frequencies genuinely differ between the two sequences (25/50/25%
  reduced vs. 16.0/56.0/28.0% original-skeleton for a_1=105,p=7) — I recomputed
  this myself and got identical numbers. This is decisive: since a correspondence
  preserving type-equality for a density-1 set of indices would have to preserve
  limiting frequencies exactly, no re-indexing (however clever) can repair this.
- I re-ran all reported |Q|=3 seed/removal combinations (30, 70, 42, 165, 385, each
  with all three single-prime removals) in my own implementation and reproduced the
  exact pattern: 0 mismatches whenever 2 ∈ Q' (checked up to N=8000 for one case,
  a_1=30/p=3, genuinely zero, not merely small), and a large, stable, nonzero
  mismatch density (24%–68%) whenever 2 ∉ Q' — matching the builder's table across
  every one of the 14 reported cases.

**Logical conclusion.** Since any seed with 2 ∉ Q has NO single-prime removal that
can introduce 2 into Q' (removing one prime from a set not containing 2 cannot make
2 appear), and the failure is empirically total in exactly this regime (8/8 tested
cases across 6 different seeds and 3 different |Q| values), this is a genuine
structural obstruction to the induction as scoped, not an artifact of a poor choice
of which prime to remove. The two natural weakenings (non-literal correspondence;
canonical largest-prime-removal choice) were both checked and both also fail on the
same data — I agree with this: the frequency-mismatch argument already rules out any
re-indexed correspondence, and the two largest-prime-removal spot checks (165, 385)
were reproduced by me with matching densities (57.0%, 68.3%).

This is a genuine, reproducible falsification (not a coding artifact — two
completely independent implementations agree to within rounding on every reported
number). The approach's core mechanism cannot work as scoped for any seed lacking 2
in its prime set — a structurally common case, not an edge case. **Verdict:
RETHINK.** The builder's own "Promotable lemmas: None" is correct (nothing positive
was established; the |Q|=1 base case reused was already certified elsewhere, not
new content from this file).

## Lemma certification this round

- **Certified** `results/imo-2026-06/lemmas/singleton-side-fah.md` — unconditional,
  non-circular, one-line corollary of the already-certified Generalized Bounded
  Witness Lemma; independently re-derived and its two supporting numerical examples
  independently reproduced.
- **Certified** `results/imo-2026-06/lemmas/divisor-chain-well-definedness.md` —
  elementary, unconditional, correct; a clean reusable building block for any future
  divisor-pigeonhole attack on FAH.
- **NOT certified**: "r ∈ S₀ does not contradict rogueness" — correct as a
  diagnostic, but (matching the round-3 Lemma F / round-6 Lemma I / round-7
  Canonicalization-Lemma precedent) it is a meta-statement about one specific
  dichotomy attempt's flaw, not a portable standalone mathematical fact; recorded as
  in-file guidance in `current.md` instead.

## current.md updated

Added a Round 8 `## Status` summary at the top (retaining all prior rounds' text
below it for the audit trail), two new `## Approaches tried` bullets, a full
`## ROUND 8` section (mechanism analysis, independent verification detail, both
approach verdicts), a `## Lemma certification this round (round 8)` section, and
`## Next-round guidance (current, round 8)`. No `## Full proof` section added —
Status remains `partial`; the problem is not solved.

## Bottom line

Both verdicts are per-approach, independent, and mixed (normal per CLAUDE.md):
- `covering-system-construction`: **CHANGES REQUESTED** — real progress (one new
  certified lemma, a sharper/more-basic gap diagnosis, independently reproduced
  numerics), Joint FAH still open.
- `seed-coupling-induction`: **RETHINK** — genuine, independently reconfirmed
  falsification; the induction-on-ω(a_1) framing via single-prime removal cannot
  work as scoped and needs a fundamentally different reduction step if revived.

The workspace's overall Status remains `partial`. The sole open crux (FAH /
Symmetric FAH, equivalently Joint FAH for q* := min(F'∩F'')) is unchanged in
substance but the field of attempted proof mechanisms that are now confirmed dead
has grown by one more (Fixed-Witness Divisor-Chain, as dispatched), while a genuine
new sub-case (singleton F'/F'') is now fully and permanently closed off, correctly
narrowing where future effort should go: exclusively the |F'|,|F''| ≥ 2 regime.
