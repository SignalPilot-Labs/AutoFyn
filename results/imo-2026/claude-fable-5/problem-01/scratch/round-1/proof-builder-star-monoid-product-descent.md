# Build report — star-monoid-product-descent (imo-2026-01, round 1)

## Outcome
Status: **solved** (claimed). Complete rigorous proof of both (a) and (b) written to
`/home/agentuser/repo/results/imo-2026-01/approaches/star-monoid-product-descent.md`.

## What was built
All six skeleton gaps closed:

1. **Step 0–1 (foundations):** FTA conventions (FTA-1..4) stated; Lemma 1 proves the exponent laws v_p(mn) = a+b, divisibility ⟺ exponentwise ≤, v_p(gcd) = min, v_p(lcm) = max, gcd·lcm = mn, and v_p(lcm/gcd) = max−min = |a−b| — each derived, not asserted.
2. **Step 2 (multiset gcd):** Lemma 2 proves existence + uniqueness of G(A) with CD(A) = D(G(A)) for any finite multiset A ⊆ ℤ≥0 (uniqueness via finiteness of D(g) for g ≥ 1; pair existence by strong induction on x+y with the subtractive step; general case by induction on |A|). All zero/empty cases covered; conventions gcd(k,0)=k, gcd(0,0)=0 fall out. Lemma 3 = subtractive Euclid identity gcd(a,b) = gcd(min, |a−b|) with cases a≥b / a<b (symmetry), b=0, a=b. Lemma 4 = splitting G({a,b}⊎T) = G({gcd(a,b)}⊎T).
3. **Step 3 (monoid):** ⋆ well-defined (finite product, FTA-3); Lemma 5 proves commutativity, associativity (via Lemma 4, exponentwise), identity 1⋆n = n — from exponent vectors, per the outline-reviewer's note. Φ is defined ORDER-FREE via common-divisor sets (so multiset well-definedness is by construction, with multiplicity handled), and then shown to agree with the ⋆-fold.
4. **Step 4 (invariance + extremes):** Lemma 6 proves Φ(S′) = Φ(S) per prime via Lemma 4 → Lemma 3 → Lemma 4. Lemma 7: Φ ≥ 2 if any entry > 1; Φ(all-ones) = 1; Φ({M,1,…,1}) = M (computed from CD sets, not just asserted via identity axiom).
5. **Step 5 (termination):** Lemma 8: exhaustive disjoint move cases d ≥ 2 (includes m = n, where q = 1; P → P/d ≤ P/2, integrality via d | m | P) and d = 1 (forces m ≠ n since m = n > 1 gives d = m > 1; q = mn > 1; P fixed; N drops by exactly 1, other positions unchanged). Lemma 9: concrete well-foundedness — at most log₂ P(S₀) gcd≥2 moves, then N strictly descends to a contradiction; no abstract "lex on ℕ² is well-founded" hand-wave.
6. **Step 6–7 (conclusions):** stuck ⟺ N ≤ 1 both directions (Lemma 10); N = 0 excluded by Φ(S_f) = Φ(S₀) ≥ 2 vs Φ = 1; part (b) via Φ(terminal) = M with the explicit closed form M = ∏_p p^{G({v_p(x): x ∈ S₀})}; non-circularity of (b) w.r.t. (a) noted explicitly.

## Dispatch worry resolved
The dispatch flagged: "if entries are 2 and 3, gcd of exponent vectors gives Φ = 1 — CHECK THIS." Resolved: with gcd(k,0) = k (the multiset-gcd characterization, where every positive integer divides 0), zero exponents do NOT lower the gcd; Φ({2,3}) = 2^{gcd(1,0)}·3^{gcd(0,1)} = 6. In general one entry > 1 already forces Φ ≥ 2 (Lemma 7(1)). The Φ ≥ 2 route for "exactly one" stands exactly as the skeleton designed it; no fallback to the local "no two 1s output" argument was needed. A remark in the proof records this explicitly so the reviewer sees the trap is closed, and a 3000-board random simulation confirmed Φ-invariance, Φ ≥ 2, and terminal value = Φ(initial) on every play.

## Outline-reviewer notes addressed
1. "gcd = 1 forces m ≠ n" — proved in Lemma 8, Case d = 1.
2. Concrete lex well-foundedness — Lemma 9 (P at least halves finitely often; then N strictly descends, bounded by 0).
3. Multiset bookkeeping with multiplicity + monoid axioms from exponent vectors — Step 3 (order-free Φ definition; Lemma 5 proved exponentwise).

## Promotable lemmas (proposed, uncertified)
- `results/imo-2026-01/lemmas/multiset-gcd-characterization.md` (Lemma 2 + Lemma 4): unique G(A) with CD(A) = D(G(A)); zero conventions; splitting/associativity. Directly reusable by prime-gcd-invariant's 2026-entry gcd bookkeeping.
- `results/imo-2026-01/lemmas/euclid-identity-with-zeros.md` (Lemma 3): gcd(a,b) = gcd(min(a,b), |a−b|) on ℤ≥0, all zero cases.

## Remaining gaps
None known. Every skeleton gap is closed; the audit-trail section in the approach file lists the case coverage.

## Spec concerns:
- `problems.jsonl` lists imo-2026-01 with `"difficulty_level": "medium"` and `"difficulty_rating": 5`, while CLAUDE.md says runs target only `hard` problems. The run's problem choice is the orchestrator's; noting the mismatch only.
- The problem statement says "2026 integers"; the proof only uses "at least 2, finitely many" — no concern, just noting the constant 2026 is not load-bearing (kept in the text for fidelity to the statement).
