# Proof review — imo-2026-01, round 1

Two candidates built this round; both claimed `solved`. I attacked each independently:
re-derived the load-bearing algebra from scratch, checked all case splits and edge cases
(entries equal, valuations zero, all-ones terminal board), and ran independent numerical
verification (400 random boards × 3 runs; 5000 random overlap triples; 2000 random moves).
No gaps found in either. Both verdicts: APPROVE.

---

## 1. per-prime-gcd-invariant — VERDICT: APPROVE (Status: solved)

**Scores.** Correctness 10/10. Completeness/rigor 10/10. Progress: full solution of (a)+(b).

**Load-bearing step re-derived.** The whole proof rests on two facts: (i) the move acts at
every prime as (a,b) ↦ (min(a,b), |a−b|) on valuations, and (ii) g_p := gcd of all 2026
valuations is conserved because {a,b} and {min(a,b), |a−b|} have identical common-divisor sets.
I re-derived both independently: (i) from v_p(gcd)=min, v_p(lcm)=max, and integrality of
lcm/gcd; (ii) is Euclidean subtraction, valid including all zero cases (and the multisets are
all-zero simultaneously since a=b=0 iff min=|a−b|=0, so the gcd(∅-of-positives)=0 convention
never desynchronizes). Both reproduce the proof's claims exactly.

**Termination check.** Delta S = −Omega(gcd(m,n)) re-computed: per prime the pair contribution
goes a+b → max(a,b), a drop of min(a,b); summing gives −Omega(gcd). Case split
gcd>1 / gcd=1 is exhaustive and disjoint; the m=n edge case correctly lands in Case 1
(outputs (m,1)); in Case 2 outputs are (1, mn) with mn>1 so C drops by exactly 1. Lex
well-foundedness (Lemma 3) proved correctly inline. Numerically: strict lex descent held at
every one of thousands of moves across 1200 random runs.

**Part (a) completion.** All-ones terminal board correctly ruled out via g_p ≥ 1 for a prime p
dividing a_1, versus g_p = 0 on all-ones. Terminal shape argument ("move possible iff two
entries > 1 in different places") matches the problem statement.

**Part (b).** g_p(B*) = v_p(M) verified in both subcases (v_p(M)=0 and >0, using every integer
divides 0). Formula M = prod_p p^{gcd(v_p(a_i))} matched the simulated terminal value on all
400 random boards under 3 independent random schedules each. Answer_type is `none`; the
problem asks proof only, and both parts are established.

**Circularity / hidden gaps.** None found. Every "similarly/symmetrically" (Lemma 1(2),
Lemma 4 WLOG) covers a genuinely symmetric case. No appeal to crux moves or external problems;
only FTA and the invariant method, both named and in knowledge_base.md.

**Promotable lemmas — certified (all three):** move-valuation, euclid-subtraction-with-zeros,
lex-wellfounded-NxN → written to `results/imo-2026-01/lemmas/`.

**Outcome recorded:** verified-milestone.

---

## 2. newman-confluence — VERDICT: APPROVE (Status: solved)

**Scores.** Correctness 10/10. Completeness/rigor 10/10. Progress: full independent solution
of (a)+(b) (uniqueness of the entire terminal multiset, without computing M).

**Load-bearing step re-derived.** The crux is Lemma 5 Case 3 (overlapping moves on m,n,k with
shared place m): the join identity E₁ = E(mn/d², dk/t²) = E(en/t², mk/e²) = E₂. I re-derived it
independently: at each prime with α,β,γ the four valuations are |α−β|, |min(α,β)−γ|,
|min(α,γ)−β|, |α−γ|, and gcd(|α−β|, |min(α,β)−γ|) = gcd(|α−β|, |α−γ|) via the divisor-set
argument α−γ = (α−β)+(β−γ), with the zero-pair condition of Fact D checked (it holds: each
pair is zero iff the other is). Confirmed on 5000 random triples (m,n,k) — E₁ = E₂ always,
and t | d, t | k, t | e, t | n integrality claims held throughout.

**Legality bookkeeping.** The "formal move" device (Lemma 3) is sound: a move touching a 1
fixes the multiset {1,y} ↦ {1,y}, so deleting fixing steps projects any formal path to a real
path. This cleanly handles d=1 or intermediate 1s in the joining schedules — the potential gap
I hunted hardest for, and it is closed.

**Other components.** Lemma 1 monovariant N = 2027P + C: re-derived (P′ = P/g; g=1 gives exact
C drop of 1), checked on 2000 random moves. Lemma 2 (prime support persists) covers both the
a=b and a≠b subcases correctly — this rules out the all-ones terminal board for (a). Lemma 4
(pair collapse): termination by strong induction on the product, all three cases (contains 1 /
g>1 / g=1) exhaustive; endpoint identified via the Fact E invariant with gcd(0,b)=b. Lemma 5's
three overlap cases (|π₁∩π₂| = 2, 0, 1) are exhaustive; Case 2's disjoint-places commutation
is genuinely order-independent. Lemma 6 is a correct inline proof of Newman's lemma by strong
induction on N(B), with the empty-path base cases handled explicitly — no citation-without-
proof of Newman.

**Circularity / hidden gaps.** None found. The per-prime computations only identify endpoints
of fixed integer move schedules, so the flagged per-prime-coupling trap is genuinely avoided.

**Promotable lemmas — certified (all four):** pair-collapse, formal-projects-to-real,
overlap-joining, move-monovariant → written to `results/imo-2026-01/lemmas/`.

**Outcome recorded:** verified-milestone.

---

## current.md

Created `results/imo-2026-01/current.md` with `## Status: solved` and the Full proof
(primary: per-prime-gcd-invariant, which additionally yields the explicit formula
M = prod_p p^{gcd(v_p(a_1),...,v_p(a_2026))}; newman-confluence recorded as an independent
second complete proof).

## Goal Progress

Status: **solved**. Both slugs live and APPROVED (per-prime-gcd-invariant: solved;
newman-confluence: solved). The run's goal is met — imo-2026-01 is solved with two
independent, reviewer-verified complete proofs of parts (a) and (b).

Note: the dispatch described this run as targeting a hard problem, but imo-2026-01 is marked
`difficulty_level: medium`, `difficulty_rating: 5` in problems.jsonl. Reviewed as dispatched.
