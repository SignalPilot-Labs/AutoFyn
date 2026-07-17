# Outline review — imo-2026-06 (round 2)

Reviewed the outliner's revised field. The round-1 Lemma S was found FALSE (a₁=385: clauses {3,7,19},{2,11,19} share only 19 > P₁=11). Every revised approach now targets the CORRECTED finiteness crux. I independently verified the corrected threshold and the load-bearing structural claims before ranking — I did not take them on faith.

## Independent verification (computational)

1. **Corrected threshold a₁ (not P₁) is sound.** Ran the greedy sequence for 19 starting values (incl. all the outliner's a₁ set) to depth 400–800 and checked every clause pair. Lemma S′ ("any two clauses share a prime ≤ a₁") had **0 violations** everywhere, and it correctly reproduces the round-1 bug: at a₁=385 the S-violating pair shares 19, and 19 ≤ a₁=385, so S′ is satisfied. The threshold fix is exactly right and explains the false lemma.
2. **a₁ is a safe (generous) threshold, not a knife-edge.** max over pairs of the smallest shared prime was tiny (19, 43, 83 for a₁=385, 3311, 4199) — far below a₁. No sign of S′ ever being tight, let alone failing.
3. **The crux (finitely many minimal clauses) is robustly TRUE.** For a₁=2310 a shallow simulation (N≤800) shows 243 "minimal clauses"/239 large primes, but this is a **truncation artifact**: at N=1600, 3200 it collapses to **1 minimal clause, 0 large primes**. For a₁=385 and 4199 the count is stable at 7 clauses / 1 large prime from N=200 up. Genuine essential primes are few; the crux holds decisively.
4. **clique-descent's sunflower claim holds.** For every fixed large prime q, the minimal clauses containing q had pairwise-disjoint small-shadows: **0 overlap violations** across all tested a₁. Max clauses per large prime was ≤ 2.

## Reduction soundness (Prop 1′)

Prop 1′ is airtight **given S′**: for a minimal clause C, set C′ = C∩G (G = primes ≤ a₁). C′ ≠ ∅ by Tool 1 (every term has a prime factor ≤ P₁ ≤ a₁). For any clause D, S′ gives a shared prime ≤ a₁ in C∩D∩G ⊆ C′, so C′ hits every clause ⟹ C′ is a clause (Cor E.1); C′ ⊆ C + minimality ⟹ C′ = C ⊆ G. Finite G ⟹ finitely many minimal clauses ⟹ crux ⟹ conclusion. Non-circular and correct. No approach leans on the false Lemma S — all three retarget cleanly. The reduction §§0–4 remains certified and is imported, not re-derived.

## Per-approach verdicts

### descent-shared-prime (new) — APPROVE
Cleanest of the field. Steps 1–3 (import + Prop 1′ + finite-ground-set reduction) are airtight — I verified Prop 1′ and S′ above. The single genuine gap is step 4: the q-cofactor descent that proves S′. The mechanism is stated and plausible (strip the shared large primes from a_k to form e coprime to a_j while e still hits every earlier clause; Tool 2 forbids a coprime term). Two fixable specifics the builder must handle, both flagged honestly by the outliner:
- **Multi-prime shared case.** e = a_k / q^{v_q} removes only ONE prime; if S_j∩S_k has several large primes, gcd(a_j,e)≠1. The builder must do the descent on the full disjoint-shadow version: e = a_k stripped of ALL of S_j∩S_k. This still hits every S_l, l<j (the ≤a₁ prime from the non-violating pair (l,k) is not in S_j∩S_k, so it survives), and gives S_j∩supp(e)=∅ cleanly. This works — make it explicit.
- **e ≤ a₁ branch.** The minimality punch (a_j ≤ e) needs e > a_{j-1}. The b≤a₁ branch is the real open core; the builder must close it, not wave at it. This is the hard node.
Well-founded (lex-min violating pair in ℕ²), non-circular. Best corpus analogue (aimo-0030 / IMO-2024-P5, same sequence). Build.

### clique-descent (revise) — APPROVE
Retargets correctly from false Lemma S to "finitely many minimal clauses"; Prop 1 (P₁) retracted. The M_small bound and the per-large-prime sunflower bound (≤ π(P₁), verified 0 violations above) are sound. Sole gap is step 4: bounding the number of DISTINCT large essential primes via the disjoint-shadow-pair reconciliation map. This is a genuinely distinct wall (finitary count, no minimal-counterexample) — good for field diversity. Two cautions for the builder:
- Fibers of the map {large prime → reconciled disjoint shadow-pair} may be non-trivial; injectivity/per-pair cap is the real work, not decoration.
- **Compute GENUINE minimal clauses, not truncated ones** — my a₁=2310 test shows shallow simulation wildly overcounts. Structural claims must be about the infinite family. Build.

### sieve-closure (revise) — CHANGES REQUESTED (not in build set this round)
Framing is sound and genuinely distinct (witness absorption). Step 2 (witness T_i exists and q_i ∈ supp(T_i)) is correct. But the load-bearing step 3–4 rests on the nesting hypothesis C_i ⊇ C_j, which the outliner itself concedes "is not automatic" and whose derivation "is the wall for this framing." That is the weakest mechanism in the field, and the outliner flags a real risk it collapses into clique-descent's count. Keep it live for breadth, but it is not worth a builder this round over the two soundest walls. If built later, the builder must derive the nesting from the closure structure (Lemma 1) FIRST — without it, step 3 is a bare hand-off.

### finite-state-bijection — not nominated, leave as-is
Only repackages the certified finish and imports the crux; adds nothing to closing it. Ranks last.

## Diversity note for the orchestrator
All three live approaches ultimately hinge on controlling large essential primes / large-only shared primes — one shared crux, but attacked from three distinct walls: descent-shared-prime SIDESTEPS the count (proves S′ directly), clique-descent COUNTS (disjoint-shadow gaps), sieve-closure ABSORBS (witness cascade). This is acceptable diversity for round 2. **Shared-gap watch:** if descent-shared-prime stalls at its step-4 b≤a₁ branch AND clique-descent stalls at the distinct-large-prime bound, round 3 must open a genuinely 4th framing (e.g. a growth/size argument: a large prime q>a₁ in a minimal clause forces a term below the mature pure-small-prime admissible minimum). Flagging now so the orchestrator can act if both stall.

## Ranking (updated, stale cleared)
descent-shared-prime 1545.7 > clique-descent 1541.2 > sieve-closure 1485.5 > finite-state-bijection 1427.6.
Rationale: descent-shared-prime's reduction (Prop 1′) is the one I fully verified airtight, single honest gap, closest corpus analogue → edges clique-descent (partial R1, verified sunflower, harder count gap); both beat sieve-closure (weakest gap mechanism, unjustified nesting) and finite-state-bijection (adds nothing to the crux).

build set: descent-shared-prime, clique-descent
