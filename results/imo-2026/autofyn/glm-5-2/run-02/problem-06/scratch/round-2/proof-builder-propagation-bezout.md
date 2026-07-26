# Build report — propagation-bezout (round 2)

## Deliverable status: BOUNDED TASK COMPLETE. Status: partial.

## What was done
1. **Skeleton (Steps 1–5) written.** Lemmas 1, 2, 3 inherited (cited to essential-monovariant.md §1–§3, not reproved). Consecutive seed stated (Lemma 3). Step 3 (extremal-forces-equality) stated as a sub-lemma with its mechanism and the aimo-0648 (ii) port explained. Step 4 (Bezout-propagation) stated as the gap. Step 5 inherits essential-monovariant's Theorem.

2. **Circularity pinned to an exact sub-step.** The propagation's shift algebra is the residue-walk map φ : V → V (cyclic successor on V). Circularity chain:
   - V := { r mod L_0 : τ(r) ∈ H_∞ } — defined via the transversal family H_∞ of F_∞ = {τ(a_i)}.
   - The claim "a_{n+1} mod L_0 ∈ V for every n" (= free-rider irrelevance) is the Claim in essential-monovariant §5, whose direction "a_{n+1} has transversal type" **invokes Lemma 4** to assert a_{n+1} shares a Q_R-prime with every a_i (not just earlier ones).
   - So φ presupposes Lemma 4; propagating Lemma 4 via φ^k is circular. **Exact sub-step: 4b in the approach file.**

3. **Pre-Lemma-4 shift algebra attempted, honest failure.** The only shift-invariant pre-Lemma-4 ingredient is Lemma 2 (gap bound). Provable fact: shift-k pairs share a prime ≤ k·R (growing bound, NOT fixed R). Sharpening k·R → R is exactly Lemma 4. Bezout composition fails because "shares-a-small-prime" is NOT transitive along index shifts (concrete: (a_i,a_{i+1}) shares r, (a_{i+1},a_{i+2}) shares s, r≠s ⇒ no forced small share for (a_i,a_{i+2})). The shift-1 → shift-2 wall is the concrete obstruction (R < p ≤ 2R case has no lever).

4. **Partial extracted (subsumed by Lemma 1, NOT promotable).** For every j ≥ 2, (a_1, a_j) shares a prime ≤ R: by Lemma 1, a_j is divisible by some q ∈ P(a_1) ⊆ Q_R, and q | a_1. This is a direct corollary of the already-certified Lemma 1 — adds nothing new, so no lemma is proposed for certification into lemmas/.

5. **Honest verdict.** Status partial. The route is circular as filed; no promotable lemma arises. The route stays live in the ranker as a registered third mechanism (propagation), but does not advance the crux. Next round: if the orchestrator wants a propagation route to actually attack Lemma 4, it must find a pre-Lemma-4 transitivity mechanism for "shares-small-prime" — none is visible in the greedy rule (the decision depends on the full prime-factorization history, not a fixed recurrence).

## Numerical check (conducted, not a proof step)
For a_1 ∈ {15, 21, 35}, first 25 terms: shift-2 pairs do share a prime ≤ R in every case (consistent with Lemma 4 being true), but the gap-bound argument only ever proves ≤ 2R. The truth of the fixed-R bound is the crux; the gap-bound window cannot reach it.

## File written
- /home/agentuser/repo/results/imo-2026-06/approaches/propagation-bezout.md (Status: partial)

## Promotable lemmas
(none — the only partial is subsumed by Lemma 1.)
