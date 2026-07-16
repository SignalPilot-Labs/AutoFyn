# Build report — valid-set-sunflower-core (round 1)

## Status: partial

## What was done
1. **Shared foundation extracted and fully proved** as proposed lemma files (per outline-reviewer directive), ready for proof-reviewer certification:
   - `results/imo-2026-06/lemmas/terms-equal-valid-set.md` — (L1.1) pairwise sharing, (L1.2) {terms} = V, (L1.3) realization H\* = {types}, (L1.4) self-blocking/transversal equivalences, and a NEW (L1.5) **Locality Lemma**: m > a_1, m ∉ V ⟹ some term t < m with gcd(t,m) = 1. This is the greedy-dynamic constraint invisible to the pure clutter abstraction.
   - `results/imo-2026-06/lemmas/dodging-and-witness.md` — bounded gaps, CRT dodging, witness lemma, nonempty trace.
   - `results/imo-2026-06/lemmas/finite-core-implies-periodicity.md` — M finite ⟹ full problem claim with explicit T, L, valid for ALL n ≥ 1.
2. **All outline-review notes addressed** in the approach file: infinite sunflower lemma proved inline (induction on s, both cases); antichain edge cases ("at most one empty big part", "petals nonempty") written out; 5c β-extraction rebuilt as a clean induction where the fresh witness is chosen disjoint from σ ∪ {β_1..β_m} by (L1.4d), making the new-prime claim automatic (and the witness lemma is no longer needed there).
3. **New proved result — Theorem K (König transversal tree, Step 5d):** if M is infinite, there is an increasing chain (T_x) of minimal transversals of the truncated type systems Q(x) = {P(t) : t ≤ x}, each T_x ∉ H\*, each contained in infinitely many members, with elements ≤ x, sizes → ∞, small-prime trace frozen at σ\* (meeting A), covering every term at its own scale (K(vi)), plus a "preloading" corollary K2: any member dodging T_x carries a branch prime entering after level x. This subsumes 5c, re-localizes GAP 1 to one explicit infinite object, and is import-ready for both rival approaches.
4. **GAP 1 remains open** (sharpened: rule out the König branch). Honest partial; no overclaim.

## Failed attacks recorded (in `Approaches tried`, so they are not retried)
- Density/AP-covering: killed structurally by the intersecting property (any constructed AP of terms is covered for free by one shared prime).
- Self-referential CRT dodge of the branch's big primes: window position ~∏(primes) ≫ x escapes the scale at which K(vi) applies.
- Pure clutter finiteness ((P1)–(P3) alone): possibly false; refutation attempt is assigned to self-blocking-clutter-induction per the review.

## External resources
Tried to consult AoPS thread (c6h3866890) for the official solution idea — Cloudflare-blocked; search engines have nothing indexed. No external hint used; all content above is proved from scratch.

## Suggested next-round focus for this slug
Couple the Locality Lemma (L1.5) to Theorem K quantitatively: branch primes γ ∈ T_x are ≤ x and "needed" (minimality of T_x gives, for each γ, a term t ≤ x with P(t) ∩ T_x = {γ}, so t ≥ γ); the open question is whether the entry schedule of branch primes is compatible with K2's preloading plus bounded gaps. Alternatively a counting attack: quantify the dodging lemma to show infinitely many minimal types force V to miss long runs, contradicting (L2.1).

## Spec concerns
None.
