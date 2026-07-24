# Outline review — imo-2026-03 (IMO 2026 P3), first ranking round

## Validation done (Bash)
- **Answer c(n)=2^n/(2^{n+1}−1) confirmed.** Brute-force minimax: n=1 → exactly 2/3.
- **greedy=odd-ranked reduction (shared G1) is a standard, correct theorem** (alternating pick-to-maximize is zero-sum on the difference; sort-descending greedy is optimal for both, first player takes odd-ranked elements). Using it, the n=1 minimax matches 2/3 exactly.
- **LB geometric construction validated for n=2.** LB marks at 1/7, 3/7 (pieces 1/7, 2/7, 4/7); against a fine XY best-response grid (up to 2 XY marks) LB's guaranteed odd-sum is exactly 4/7. This confirms both the answer and the lower-bound construction that all three approaches share.

The shared spine (answer + G1 + geometric LB marks + dominance identity) is sound. The common hard core across all three is the **XY upper bound** — proving XY can hold LB to ≤ c(n) against *every* LB marking. Flagging this as a field-wide shared wall (see Diversity note).

## direct-constructive — APPROVE
Technique is right and the most self-contained of the three.
- Step 1 (G1): standard, provable by exchange argument. Sound. Candidate shared lemma once certified.
- Steps 2–3 (LB lower bound): the dominance identity P_j = Σ_{i<j}P_i + 1/D is a real, exact fact; the easy sub-case (XY spares P_n) is airtight; the hard sub-case (G2: XY cuts P_n) is numerically confirmed to still yield ≥ 2^n/D for n=2. G2 is a genuine, attackable gap with a stated mechanism (charging/interleaving-optimality), not a bare label.
- Step 4 (G3, XY upper bound against ALL markings): the hardest, most global step. The interleaving lemma (owner of B > ΣS forces claimer to get exactly B) is a concrete, correct mechanism. The remaining risk is the "halving" half — showing interleave+halve minimax value is *exactly* 2^n/D against the worst LB marking is asserted, not yet derived. Build note: G3 is where effort should concentrate; treat the interleave+halve value computation as the load-bearing sub-lemma and derive it, don't assert it. Watch the a_1 = Σ(smaller) boundary and the ε→0 (sup-not-attained) argument.

## induction-recursion — APPROVE (build, but front-load the H2 check)
Genuinely distinct route (induction on n via the Möbius recursion), so it earns a slot for diversity.
- Step 1 (recursion ⇒ closed form) is airtight algebra; base c(0)=1 correct.
- The crux is H2, the **game-separation lemma**: the claiming phase ranks ALL pieces globally, so "reduce to an (n−1)-subgame" is NOT free — it is exactly where naive induction on n dies. The outliner honestly flags this as the single-gap trap (if H2 is false, both the LB and XY inductions die together). The stated mechanism ("geometric spacing prevents value-changing cross-boundary interleaving") is currently a hope, not a justification.
- **Required before filling (CHANGES-level condition inside the build):** verify H2 concretely on n=2 by hand/computation FIRST. If cross-boundary ranks do change the odd-sum, the separation must be reformulated (e.g. track only top pieces) or the approach goes back to the outliner. Do not write "reduce to (n−1)" as a step until H2 is proven for the general step. This is an attackable gap, not a fatal flaw, so APPROVE — but the builder must not skip the H2 sanity check.

## potential-duality — REGISTER but DEFER (not in build set)
Real framing diversity (invariant/certificate rather than strategy), but the load-bearing lemma P2 is currently a **wish, not a mechanism**: "the value function exists by backward induction" is true and worthless; the entire value of the approach is an *explicit* closed-form Φ, and the outline offers only a guess (Φ = (1/D)Σ2^{ρ(i)} over an unspecified matching ρ). That is an unverified hand-off — exactly the kind of bare-labelled crux to push back on. The outliner itself flags high vacuity risk. Its engine (dyadic-redistribution Möbius map v↦2v/(2v+1)) also overlaps the induction approach's engine, so it is somewhat less far-apart than advertised.
- Verdict: registered for population breadth (Elo 1469, ranked third), but **not worth a builder's full effort this round**. Gate it: before it ever gets a build slot, someone must run the n≤3 Φ falsification check and produce an explicit Φ that reduces to the true odd-sum at terminals. If that check passes next round, promote it; if no clean Φ materialises, it collapses to backward induction and should be cut.

## Diversity note (for the orchestrator)
All three approaches ultimately converge on the **same hardest sub-problem**: the XY upper bound (G3 / H3b / P3a — "XY holds LB to ≤ c(n) against any marking"), and all three lean on the same dyadic/Möbius identity. Method diverges (explicit interleave+halve strategy vs induction reduction vs monovariant certificate), which is real diversity, but the field could stall together on the XY upper bound. If the two built approaches both bottom out on that step next round, the orchestrator should commission an explorer on a genuinely different framing of the *upper bound specifically* (e.g. an adversary/adaptive-argument or a direct potential on XY's spare marks) rather than another variation on interleave+halve.

## Ranking (registered + ranked this round)
1. direct-constructive — Elo 1531 (most self-contained; LB side validated numerically)
2. induction-recursion — Elo 1500 (clean recursion, but crux H2 unproven)
3. potential-duality — Elo 1469 (conjectural Φ, vacuity risk, deferred)

build set: direct-constructive, induction-recursion
