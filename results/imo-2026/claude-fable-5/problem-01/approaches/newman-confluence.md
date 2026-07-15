# Approach: newman-confluence

## Status
unsolved

## Approaches tried
- (round 1) Skeleton opened by proof-outliner; not yet built.

## Current best
Skeleton only. Termination engine identified; the local-confluence lemma (the heart) is open.

## Route (one paragraph)
An abstract-rewriting route that proves part (b) WITHOUT computing M and without the per-prime gcd invariant: treat boards (multisets of 2026 positive integers) as states of a rewriting system whose rewrite is the move; prove termination (part (a), via a monovariant) and LOCAL confluence (any two moves from the same board can be continued to a common board), then invoke Newman's lemma: a terminating, locally confluent system is confluent, hence every state has a UNIQUE normal form. The normal form of the initial board is {M, 1, …, 1} with a unique M — part (b). This is the crux move of aimo-0003 ("reduce invariance under all orderings to invariance under adjacent/overlapping swaps, verified locally") adapted to a rewriting system. Genuinely different from the invariant routes: if the g_p-invariant line had a hidden flaw, this route survives. Its own risk is concentrated in one hard lemma (overlapping-pair joinability).

## Proof body (skeleton with gaps)

**Setup.** States: multisets of 2026 positive integers. Rewrite B → B′: choose entries m, n > 1 of B, replace by gcd(m,n), lcm(m,n)/gcd(m,n). B is a normal form iff it has at most one entry > 1.

**Step 1 (Termination).** W = N + T with N = #{entries > 1}, T = Σ Ω(xᵢ) strictly decreases at every rewrite (three-case analysis: m = n; gcd = 1, m ≠ n; gcd > 1, m ≠ n — as in the prime-gcd-invariant skeleton, Step 3). W is a non-negative integer, so every rewrite sequence is finite. **Gap:** the full three-case W computation (ΔT = −Ω(gcd(m,n))).

**Step 2 (Normal forms reachable from the start have exactly one entry > 1).** Lemma A: for m, n > 1 the outputs are never both 1 (gcd = 1 ⇒ other output mn > 1; gcd > 1 ⇒ gcd output > 1). So N drops by at most 1 per move and never goes from ≥ 2 to 0; starting from N = 2026, every normal form reached has N = 1. This gives part (a) with Step 1. **Gap:** case check of Lemma A; the N-walk argument.

**Step 3 (Commuting case of local confluence).** If B → B₁ and B → B₂ use disjoint entry pairs, then applying the other move to each of B₁, B₂ yields the same board C (the two rewrites touch different entries). So B₁ → C ← B₂. **Gap:** multiset bookkeeping (entries at "different places"; identical values at different places are distinct board positions — state this convention once).

**Step 4 (Overlapping case of local confluence — THE hard lemma).** Suppose the two moves share one entry: B contains m, n, r (positions distinct; values may coincide), μ₁ acts on (m,n) giving B₁ ⊇ {gcd(m,n), lcm(m,n)/gcd(m,n), r}, μ₂ acts on (m,r) giving B₂ ⊇ {gcd(m,r), n, lcm(m,r)/gcd(m,r)}. Claim: there are rewrite sequences B₁ →* C and B₂ →* C for some common board C.
Proposed mechanism: work on the 3-entry sub-board. Per prime p with exponent triple (a,b,c) = (v_p(m), v_p(n), v_p(r)), both B₁ and B₂ carry Euclid-modified triples; the natural common target is the triple concentrated as (gcd(a,b,c), and the two "reduced" residues) — candidate C: run each of B₁, B₂ by an explicit finite schedule of moves within the three affected positions until the sub-board becomes {M₃, 1, 1} where M₃ is the terminal of the 3-entry game; then C = {M₃, 1, 1} ∪ (rest). But "the 3-entry game has a unique terminal" is itself an instance of the theorem (circularity risk!). Non-circular repair options for the builder, in order of preference:
  (i) Strengthen the induction: prove confluence by well-founded induction on W (the standard PROOF of Newman's lemma) and, inside the overlapping case, only exhibit joinability of the two ONE-STEP reducts using further single steps whose correctness is checked directly by gcd/lcm identities — e.g. verify that applying μ₂' = (move on positions holding gcd(m,n) and r) to B₁ and μ₁' = (move on positions holding gcd(m,r) and n) to B₂, followed by at most a bounded number of explicit further moves, produces literally equal multisets, via per-prime identities on (a,b,c) such as gcd/min/|·| algebra. This is a finite identity-verification, possibly with sub-cases for which of the intermediate entries equal 1 (an entry equal to 1 cannot be moved — legality!).
  (ii) Prove the 3-entry unique-terminal lemma separately by strong induction on its own W-value (a self-contained miniature of the theorem, allowed since it is proved before being used).
**Gap (major):** carry out (i) or (ii) rigorously, handling the legality constraint (intermediate 1s restrict which joins are playable) and the case where an intended join move is illegal because an intermediate entry is 1 — must show the join can be rerouted or is unnecessary (if an entry is 1 the sub-board is already smaller). This is the make-or-break step; if it resists, this approach dead-ends (the invariant rivals do not depend on it).

**Step 5 (Newman's lemma).** The system is terminating (Step 1) and locally confluent (Steps 3–4); by Newman's lemma (proved from scratch by well-founded induction on →, since we cite no external text: if B → B₁ →* N₁ and B → B₂ →* N₂ with N₁, N₂ normal, join B₁, B₂ to C, take a normal form N of C, and apply the induction hypothesis at B₁ and B₂ to get N₁ = N = N₂), every board has a unique normal form. **Gap:** write the well-founded induction cleanly (induction on W-value of B).

**Step 6 (Conclusion).** The initial board's unique normal form is a specific multiset {M, 1, …, 1} (Step 2), so every play ends with the same single entry M > 1 — parts (a) and (b). (This route does not produce the closed form M = ∏ p^{g_p}; the problem does not ask for it.)

## Open gaps (builder's list)
1. Step 1: W three-case analysis.
2. Step 2: Lemma A + N-walk.
3. Step 3: disjoint-commute bookkeeping.
4. Step 4 (MAJOR): overlapping-pair joinability, non-circular, legality-aware.
5. Step 5: Newman's lemma proof by well-founded induction.

## Cases to cover
Disjoint vs overlapping move pairs; within overlapping: gcd patterns among (m,n,r) and intermediate entries equal to 1; the m = n coincidences.

## Watch out for
- Circularity: do not prove the 3-entry join by "both terminate at the unique terminal" unless the 3-entry uniqueness is proved first as a standalone lemma by its own induction.
- Legality: entries equal to 1 cannot be selected; every joining sequence must consist of legal moves only.
- Newman needs TERMINATION; local confluence alone is not enough (no shortcut).
- Positions vs values: two equal values at different places are different positions; the rewrite relation is on multisets — fix the convention once.
