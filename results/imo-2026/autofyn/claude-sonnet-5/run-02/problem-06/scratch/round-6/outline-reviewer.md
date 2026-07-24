# outline-reviewer report — round 6 — imo-2026-06

## Independent re-verification of the round-6 falsification (done from scratch, per
CLAUDE.md's mandate given rounds 3–5's witness-selection bug history)

I reimplemented the whole pipeline myself in fresh Python (naive trial-division
greedy generation via `math.gcd`, `sympy.factorint` only for analysis after
generation — no code shared with the singleton explorer's scripts), independently
computing: the sequence a_1..a_8000 for both seeds, Q = P(a_1), persistent base
types (tail-recurrence heuristic ≥3 hits in the second half), canonical earliest-
occurrence witnesses, S = ⋃(P(witness)\Q), S₀ = Q∪S, extended types ρ(n)=P(a_n)∩S₀,
persistent extended types, and all disjoint-base-type rogue pairs with their
literal-global-minimum witnesses n_A<n_B and F' = P(a_{n_B})\S₀.

**Result: the falsification is CONFIRMED, exactly as reported, bit-for-bit.**

- `a_1=4807` (Q={11,19,23}): my independent run gives S₀={2,3,5,7,11,19,23,73,127}
  (identical to the explorer's), rogue pair A'={3,5,19} (idx 6, a_6=4845=3·5·17·19),
  B'={2,11} (idx 7, a_7=4862=2·11·13·17), gcd(a_6,a_7)=17, **F'=P(a_7)\S₀={13,17},
  |F'|=2.** Exact match.
- `a_1=11305` (Q={5,7,17,19}): S₀={2,3,5,7,13,17,19,23,29,37,43,101} (identical),
  rogue pair A'={3,7} (idx 4), B'={2,5} (idx 7), gcd=11, **F'={11,103}, |F'|=2.**
  Exact match.

Both reproduced independently with a from-scratch implementation (not a re-run of
the explorer's scripts). **The Universal Singleton Hypothesis is definitively dead.
No approach may cite |F'|=1 in general going forward.**

## Independent verification of the Full-Absorption Hypothesis (FAH) — extended
beyond what any explorer checked

The singleton explorer only checked one side of one example (17 divides 151/151 =
100% of B'={2,11} occurrences in the 4807 seed; left the 11305 example and the
symmetric side undone). I completed this myself and extended it:

- `a_1=4807`, B'={2,11}, 151 exact-extended-type occurrences up to n=8000: prime
  **17 divides 151/151 (100%)**; prime 13 divides only 11/151 (7.3%).
- `a_1=11305`, B'={2,5}, 247 occurrences: prime **11 divides 247/247 (100%)**; prime
  103 divides only 4/247 (1.6%). (This is the side the explorer left unchecked —
  confirms the pattern holds there too.)
- I then ran a fresh scan (122 seeds: the 2 known counterexamples + 120 products of
  3–4 distinct primes < 60, N=1600) specifically hunting for MORE rogue pairs with
  |F'|≥2 to stress-test FAH beyond the two known instances. Found 3 more:
  `a_1=2065` (F'={11,19}, Lemma-G prime 11 → 100%/66 occurrences), `a_1=6851` two
  separate rogue pairs (F'={5,53} and F'={5,23}, Lemma-G prime 5 → 100% in both).
  **In every single instance found (5/5), the Lemma-G-guaranteed prime achieves
  exactly 100% recurrence on the rogue type's occurrences, while every other element
  of F' is a small minority.** No FAH violation found anywhere in this scan.

**Conclusion: FAH is not just "not yet falsified" — it now has broader, independently
gathered computational support than either explorer produced, including the one
side (11305) the original report left incomplete.** This substantially de-risks
Approach 2's redirection; still not a proof, but the empirical foundation is solid
so builder time should go to the proof attempt (Step 2 of the outliner's sketch),
not more verification.

## Spot-check of the Projection Lemma and Collateral-Safety Theorem

Read `lemmas/monotonicity-of-resolution.md` in full: the certified proof is exactly
"since S₀⊆S₁, ρ(n)=ρ₁(n)∩S₀ for all n; fix p∈A'∩B'⊆S₀; p∈A'⊆A'' and p∈B'⊆B'' since
A'=A''∩S₀, B'=B''∩S₀; so p∈A''∩B''." This is correct and matches the outliner's
citation precisely. The new Projection Lemma (A'' S₁-persistent ⟹ A':=A''∩S₀ is
S₀-persistent, using ρ(n)=ρ₁(n)∩S₀ so every A''-occurrence is an A'-occurrence) is
the same one-line mechanism already used in the certified Persistent-Type Pigeonhole
lemma family — no gap. Chaining Projection + Monotonicity to get the Collateral-
Safety Theorem ("(A,B) fully safe at S₀ ⟹ fully safe at every S₁⊇S₀") is a
straightforward, sound deduction — I verified the two-line chain myself (project
A'',B'' down to A',B', invoke fully-safe hypothesis to get A'∩B'≠∅, invoke
Monotonicity to get A''∩B''≠∅) and find no gap. The "base types are fixed once and
for all since Q=P(a_1) never changes" observation is also immediate and correct.
**This sub-result is sound and cheap to certify — approved as this round's easy win.**
I did not re-run the collateral explorer's 646-pair computational scan myself (the
theoretical argument is airtight and doesn't depend on the empirical count), but
spot-checked the reported S₀/Q_R values for two seeds (187, 4807-style reasoning)
against my own witness/S₀ computation logic and found no inconsistency.

## Verdict on the field

**Approve the outliner's field as proposed, with the empirical support above
strengthening confidence.** No approach needs cutting this round.

1. **`covering-system-construction` (revise)** — the Collateral-Safety Theorem
   (Projection Lemma + certified Monotonicity) is a genuine, cheap, unconditional
   closure of half of round 5's gap, verified sound above. Crux correctly relocated
   to base-type-pair-level termination, correctly deferring "full absorption" to
   Approach 2 as an imported black box rather than re-deriving it. **Approved,
   build.**
2. **`greedy-exchange-cost-potential` (revise)** — correctly retires the falsified
   Universal Singleton Hypothesis (confirmed dead above) and replaces it with FAH,
   a strictly weaker, precisely stated, and (per my extended verification) still
   unfalsified target. The proof sketch (Step 2: force p=q via joint pigeonhole
   across all A'-occurrences using Lemma H) is a legitimate, not-yet-tried angle.
   **Approved, build** — instruct the builder that FAH's empirical base is now
   broader (5/5 instances, both sides checked) so it should move straight to the
   proof attempt rather than re-verifying.
3. **`recruitment-round-charging` (new)** — registered at cold-start Elo 1500. This
   is an honest hedge with no working mechanism yet identified (per its own report),
   exactly the kind of genuinely-different framing (charging/potential on round-count
   vs. structural pair-safety vs. per-prime persistence) CLAUDE.md's plateau-breaking
   rule asks for. **Approved, build** — expect `unsolved` or thin `partial`; value is
   in testing candidate charging object 2 (the "batch resolution" idea) as an
   independent alternative to FAH, not a near-term close.
4. `witness-index-descent`, `reversible-transition-map`, `witness-depth-bound`,
   `amortized-charging-budget`, `density-sieve-contradiction`, `hypergraph-transversal`
   — no new idea this round, correctly left stale/retired, not nominated.

## Ranking

Registered `recruitment-round-charging` (cold-start 1500) and folded in 18 head-to-
head comparisons via `update_ranking`. Resulting order (best-first):

1. `covering-system-construction` — 1725.7 (drew with greedy-exchange-cost-potential,
   beat all 6 stale/dead approaches; slight edge for landing a clean, certified,
   unconditional theorem this round)
2. `greedy-exchange-cost-potential` — 1701.7 (drew with covering-system-construction,
   beat all 6 stale/dead; FAH target is real progress in framing even though the
   hard proof step remains open)
3. `recruitment-round-charging` — 1528.6 (new; beat the 3 confirmed dead-ends,
   below the two mature leaders as expected for an unstarted hedge)
4. `witness-index-descent` — 1487.6, `reversible-transition-map` — 1463.3,
   `witness-depth-bound` — 1414.6, `amortized-charging-budget` — 1413.6,
   `density-sieve-contradiction` — 1387.4, `hypergraph-transversal` — 1377.4
   (unchanged relative order, all below the live build set).

build set: covering-system-construction, greedy-exchange-cost-potential, recruitment-round-charging
