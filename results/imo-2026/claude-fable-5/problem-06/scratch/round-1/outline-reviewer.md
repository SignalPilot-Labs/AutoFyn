# Outline review — imo-2026-06, round 1

## Independent verification performed

- **The shared reduction (Steps 1–4, 6 of valid-set-sunflower-core.md) was checked line by line and is correct.** In particular: Step 2 (sequence = sorted V, both inclusions), Step 3 (H* = hitting sets, realization via p_1^j·p_2···p_r), the corollary (M identically self-blocking, every H*-member contains an M-member by finite descent), 4a–4c (bounded gaps, CRT dodging, witness lemma — the Y = {ρ} degenerate case of 4c works since Y∖{ρ} = ∅ ∉ H*), and Step 6 (finite E ⟹ x↦x+L bijects V onto V∩[a_1+L,∞) ⟹ a_{n+T} = a_n + L for ALL n ≥ 1, T = |V∩[a_1,a_1+L)| ≥ 1). The "for all n" requirement — the usual killer for eventual-periodicity routes — genuinely dissolves here.
- **Empirical re-check (independent code, sympy):** a_1=15 gives (T,L)=(8,30); a_1=35 gives (34,210); a_1=77 gives (18,154); periodicity holds from n=1 in all cases (300 terms). Observed minimal types: {15: {2,3},{2,5},{3,5}}, {35: {2,5},{3,5},{5,7},{2,3,7}}, {77: {2,7},{2,11},{7,11}} — in every case ∪M ⊆ {p ≤ g}, supporting the lock-in claim. Also confirmed the a_1 = 2·101 style case: V collapses to the evens, M = {{2}} — big primes in early terms are junk, as the files predict.
- Cheap-kill check: single-prime domination correctly rejected (a_1 = 15 has no universal prime).
- The three live gaps (GAP 1, GAP A, GAP B) attack one statement ("M finite" / stronger) by three mechanistically disjoint routes. This is NOT the single-line trap: each slug targets the full claim end to end, the shared prefix is short, elementary, and now independently verified, and the routes through the crux are genuinely rival mechanisms (extremal set theory / number-theoretic dynamics / pure clutter induction).

## Verdicts

### valid-set-sunflower-core — APPROVE
Sound skeleton; the most proved content in the field. The reduction and Steps 5a–5b (trace pigeonhole, sunflower kill of the bounded-size case) are correct as written; 5c (β-extraction) is a valid mechanism with the contradiction still open (GAP 1). Builder notes (non-blocking):
- Prove the infinite sunflower (Δ-system) lemma inline, exactly the version used (infinite family of finite sets of size ≤ s contains an infinite sunflower with pairwise disjoint petals); it is not in knowledge_base.md.
- Write out the antichain justifications flagged in the file ("at most one member with empty big part", petals nonempty).
- In 5c, when iterating, state explicitly that the fresh witness avoids σ ∪ {β_1..β_m} (it intersects the current member only in the fresh big prime) — the file gestures at this; make it airtight.
- First builder should also extract the shared foundation into `lemmas/` (terms-equal-valid-set, dodging-and-witness, finite-core-implies-periodicity) for reviewer certification, so the rivals can import instead of restating.

### crt-window-small-prime-lockin — CHANGES REQUESTED
The stronger target (∪M ⊆ E₀, empirically true in all tests) is a legitimate rival route, and if GAP A closes, GAP 1 closes too. One conceptual flaw to fix before/while building, plus notes:
- **Lead 3(a) as phrased is at risk of vacuity.** Once Step 2 (sequence = sorted V) is certified, there is no "greedy choice" left — a_K is simply the K-th smallest element of the fully determined set V. Arguments of the form "the greedy would have preferred the cheaper multiple of g" prove nothing, because the greedy takes EVERY element of V, including the multiple of g AND the ρ-divisible term. The first-appearance analysis must be recast statically: the object to interrogate is the constraint types P_k themselves (which term t has a type whose minimality forces ρ, i.e., which P_k satisfies P_k ∩ Y = {ρ} in the witness derivation), not a counterfactual greedy step. Leads 3(b) (maximal ρ-collections, X_r = ∪(F_i∖{ρ}) ∈ H*) and 3(c) (disjoint E₀-traces force r ≤ |E₀|) are static and sound — make them the spine, with (a) rebuilt on top only in static form.
- The Y = {ρ} case handling is correct (then ρ ∈ A so ρ ≤ g); keep the check that the main argument assumes ρ ∉ A.
- Verify in prose that the maximality argument in 3(b) really yields X_r ∈ H*: "any G ∈ M missing X_r and containing ρ would extend the collection" needs G ∩ F_i = {ρ} for all i, which requires G ∩ (F_i ∖ {ρ}) = ∅ — that is exactly G ∩ X_r = ∅ plus ρ ∈ G; and a G ∈ M with G ∩ X_r = ∅ but ρ ∉ G would violate intersecting-ness with... nothing immediately — this sub-step has a real hole to close (a member missing X_r need not contain ρ). State and fix it.

### self-blocking-clutter-induction — APPROVE (with a directive)
Base case τ = 1 and the k = 2 witness-through-b structure are correct. The skeleton is honest about the crux (GAP B: links are not self-blocking — Δ_n's links are stars — so the induction hypothesis must be a cross-pair statement). Directive for the builder:
- **Before investing in the general induction, spend a bounded effort trying to REFUTE the pure theorem** ("every identically self-blocking clutter of finite sets on a countable ground set is finite"). It is not in the literature as far as this field knows, and if it is false, every purely combinatorial closing of GAP 1/GAP B is impossible and the whole field must route number-theoretic input (the dodging lemma — which IS pure-clutter-false-looking extra structure) into the crux. Either outcome is decisive information: a proof solves the problem; a counterexample redirects all three approaches. Note the witness lemma is derivable purely (Y∖{ρ} contains no member ⟹ not a transversal ⟹ some W with W∩Y={ρ}), so the pure setting retains it.
- Respect the Δ_n guardrail: no bound |M| ≤ f(τ) can exist; only infinitude is to be excluded.

### finite-state-window-pullback — RETHINK (cut, not registered)
Fatal structural problem, not a fixable gap:
- **C3 is the rivals' core lemma in disguise, and it is unavoidable.** Any pull-back from eventual quasi-periodicity to "for all n ≥ 1" needs the forward implication m ∈ V ⟹ m + L ∈ V down to m = a_1, which requires that every pair of terms shares a prime dividing L — i.e., the finite core E. Likewise C1 ("every term has a prime factor from a fixed finite set") IS the finite-core statement, and step 3's "increment is a function of a_n mod Λ" presupposes it. All three gaps are the same crux; the approach has no independent mechanism, only different vocabulary.
- Its stated raison d'être — hedging the sorted-V reduction — is now void: this review verified the reduction directly (see above), so the hedge insures against a risk that has been discharged. Nothing in this file is proved beyond Step-1 facts.
- If the outliner wants a fourth line later, it should be a genuinely different mechanism for the finiteness of M (e.g., a density/counting attack: infinitely many minimal types force V to miss arbitrarily long runs, contradicting bounded gaps — quantify the dodging lemma), not a dynamics reformulation of periodicity.

## Ranking

Registered: valid-set-sunflower-core, crt-window-small-prime-lockin, self-blocking-clutter-induction (round-1 cohort; no established field to anchor against). Comparisons applied:
- valid-set-sunflower-core > self-blocking-clutter-induction (most proved content, sharpest single gap vs. a target theorem that may be false as a pure statement)
- valid-set-sunflower-core > crt-window-small-prime-lockin (bounded-size case already killed vs. a spine with a known sub-hole in 3(b))
- crt-window-small-prime-lockin > self-blocking-clutter-induction (number-theoretic resources available + empirical support for the stronger claim vs. a deliberately restricted toolset)

Post-update Elo: valid-set-sunflower-core 1531, crt-window-small-prime-lockin 1501, self-blocking-clutter-induction 1468. finite-state-window-pullback cut (never registered).

## Build instructions

One builder per slug below. The sunflower builder additionally formalizes the shared foundation as `lemmas/` files for proof-reviewer certification (single source; the other two import by reference).

build set: valid-set-sunflower-core, crt-window-small-prime-lockin, self-blocking-clutter-induction
