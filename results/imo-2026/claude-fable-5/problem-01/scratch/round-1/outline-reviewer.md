# Outline review — imo-2026-01, round 1

Field reviewed: three new whole-problem approaches (each targets parts (a) AND (b) end to end — no fragment/single-line-split violations). I verified the load-bearing claims computationally (3000 random boards x 5 random plays each; 400 overlapping-move triples):
- W = N + ΣΩ strictly drops on every move; lex (P, N) strictly drops; no move outputs two 1s; every play ends with exactly one entry > 1; the terminal value always equals ∏_p p^{g_p}.
- Overlapping one-step reducts of 3-entry boards are always joinable, and the maximum extra depth needed per side was 3 (relevant to newman-confluence Step 4).

## prime-gcd-invariant — APPROVE

Sound skeleton, correct technique, all the trap cases are already flagged as explicit gaps.
- The mechanism chain is verified: v_p(gcd) = min, v_p(lcm/gcd) = |a−b|; gcd(a,b) = gcd(min(a,b), |a−b|) with the zero cases; ΔT = −Ω(gcd) from min + |a−b| = max.
- Case coverage is complete: move cases m = n / coprime / gcd > 1 & m ≠ n are disjoint and exhaustive; exponent cases a = b, b = 0 named; "exactly one" is argued in both directions (N never hits 0 via Lemma A + stuck ⇔ N ≤ 1); the per-prime argument is correctly framed as identities under one GLOBAL move, never a per-prime move.
- No circularity; no recorded dead end repeated (fresh workspace).
Builder notes (not blockers, just enforce while building): (1) in Step 3 Case C, "both outputs > 1" needs lcm/gcd = 1 ⇔ m = n proved BEFORE it is used — order the lemmas accordingly; (2) state gcd-with-0 conventions once at the top of Step 5; (3) Step 6 must say why only finitely many primes have g_p > 0 (only primes dividing some initial entry).

## star-monoid-product-descent — APPROVE

A genuinely distinct packaging, not a split of the sibling: different termination engine (lex (P, N) vs W), different exactly-one argument (Φ ≥ 2 vs Lemma A's N-walk), different invariant bookkeeping (two-variable monoid identity vs 2026-entry multiset gcd). It shares the subtractive-Euclid identity at the core — disclosed, two-line classical, and computationally confirmed; acceptable shared risk because newman-confluence hedges it.
- The P-factor claim is verified: new P = P/gcd(m,n) exactly (gcd·lcm = mn), P stays a positive integer (gcd | m | P), and lex ℤ≥1 × ℤ≥0 is well-founded.
- The exactly-one argument via Φ(terminal) = Φ(initial) ≥ 2 is valid and elegant; N = 0 forces Φ = 1, contradiction.
Builder notes: (1) in Step 5, justify "gcd(m,n) = 1 forces m ≠ n" (m = n > 1 gives gcd = m > 1); (2) spell out lex well-foundedness concretely (P can drop only finitely often since P ≥ 1 halves each time; between drops N strictly decreases and is ≥ 0); (3) the fold-invariance bookkeeping in Step 3 must handle the multiset with multiplicity, and associativity/commutativity must be proved from exponent vectors, not asserted.

## newman-confluence — CHANGES REQUESTED (kept live, NOT in this round's build set)

The technique is capable of proving (b) without the invariant — this is the field's true hedge and the only route that survives if the Euclid-identity line hides a flaw. The skeleton is honest: Step 4 (overlapping joinability) is correctly identified as the make-or-break lemma, and the circularity trap ("both reach the unique 3-entry terminal") is pre-empted with two non-circular repair plans. Requested changes before this gets built:
1. Pin the Step 4 mechanism to plan (i) (explicit bounded schedules verified by per-prime identities). My computation shows joins always exist within ≤ 3 further moves per side on 3-entry sub-boards — so the schedule case analysis is finite and bounded, but the builder must derive the schedules symbolically (per-prime triples (a,b,c) with min/|·|/gcd algebra) and handle every intermediate-entry-is-1 legality sub-case. Plan (ii) as written does not actually escape the circle: proving the 3-entry unique terminal "by its own induction" needs 3-entry local confluence, which is the same overlapping problem again — drop (ii) or reformulate it.
2. Newman's Step 5 induction must be on the W-value of B (well-founded), and must use FULL confluence of the reducts obtained from the IH, not just local confluence — write the standard proof carefully.
Not worth a builder this round: the two invariant lines are near-complete and one should reach APPROVE quickly; spending a builder on Step 4's schedule casework is poor expected value while cheaper routes are live. It stays registered so it can be built if the invariant lines stall.

## Ranking

Registered all three (fresh population). Comparisons applied: prime-gcd-invariant > newman-confluence; star-monoid-product-descent > newman-confluence; prime-gcd-invariant = star-monoid-product-descent (draw — no evidence separates two near-complete skeletons yet).
Resulting Elo: star-monoid-product-descent 1516.8, prime-gcd-invariant 1514.5, newman-confluence 1468.7.
(The two leaders are effectively tied; the 2-point gap is an artifact of update ordering, not a judgment.)

## Build set rationale

Two builders, one per invariant approach — redundancy against write-up failure modes, which is where this problem's residual risk lives. No third builder: newman-confluence's open Step 4 is real work and the hedge only pays if both cheap routes fail.

build set: prime-gcd-invariant, star-monoid-product-descent
