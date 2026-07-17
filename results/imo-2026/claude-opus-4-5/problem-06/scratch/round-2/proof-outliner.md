## imo-2026-06

greedy-on-vstable: revise two-of-k-structure
Target: Prove T, L exist such that a_{n+T} = a_n + L for all n >= 1
Technique: Show sequence = ordered enumeration of V_stable from n=1; V_stable is L-periodic with T valid residues; periodicity is immediate
Skeleton:
  1. Define H_stable = antichain of {P(a_i) : all i >= 1}, V_stable = {m : P(m) transverses H_stable} — by definition
  2. All pairs a_j, a_k share a prime (gcd > 1 by construction symmetry) — by the gcd condition (later term chosen to hit all earlier)
  3. Every a_n in V_stable — because each Q in H_stable is P(a_j) for some j, and P(a_n) intersect P(a_j) != empty by step 2
  4. V_stable subset V_{H_n} for all n — because H_stable is a refinement of H_n (each Q in H_stable has Q subset of some element of H_n)
  5. a_{n+1} = min V_stable > a_n for all n — by squeeze: a_{n+1} = min V_{H_n} > a_n, and V_stable subset V_{H_n}, and a_{n+1} in V_stable
  6. H_stable is finite (dichotomy: finite or all-multiples-of-p) — by pigeonhole on backbone primes: infinite H_stable forces common prime p | all terms
  7. L = product(support(H_stable)) and T = |valid residues mod L| — by CRT (V_stable is union of residue classes mod L)
  8. a_{n+T} = a_n + L for all n >= 1 — because greedy on L-periodic set V_stable cycles through T residues per period

Key lemmas (claim + mechanism):
  - Every pair a_j, a_k shares a prime — gcd > 1 from greedy rule (symmetry: j < k means a_k chosen to hit a_j; j > k means a_j chosen to hit a_k)
  - V_stable subset V_{H_n} — antichain refinement (H_stable has smaller or equal elements compared to H_n)
  - Dichotomy: H_stable finite OR p | all terms — backbone pigeonhole: if H_stable infinite, infinitely many {p, r_i} for fixed backbone p, forcing p | m for all valid m
  - Greedy on L-periodic set is shift-periodic with T = |residues| — deterministic cycling through residue classes

Open gaps:
  - Step 6: Must formally prove H_stable is finite (or reduce to all-multiples-of-p). The dichotomy argument from explorer alternative Opening C is the route.

Cases to cover:
  - Case 1: a_1 is a prime power => T=1, L=p (trivial, already proved)
  - Case 2a: Some a_n = p^e prime power enters later => all terms multiples of p, T=1, L=p (already proved in R1)
  - Case 2b: No prime power ever => H_stable is finite, use the greedy-on-V_stable argument

Watch out for: Proving finiteness of H_stable is the remaining gap; the backward extension is now trivial (step 3-5 handle it)

---

antichain-monovariant: revise antichain-stabilization
Target: Prove T, L exist such that a_{n+T} = a_n + L for all n >= 1
Technique: Use monovariant f(H) = sum_{Q in H} 2^{-|Q|} to prove H stabilizes in finite steps; once stable, apply the V_stable enumeration argument
Skeleton:
  1. Define H_n = antichain of {P(a_1), ..., P(a_n)} — by definition
  2. H_n is intersecting (any Q, Q' in H_n share a prime) — by gcd > 1 condition
  3. f(H_n) = sum_{Q in H_n} 2^{-|Q|} is non-decreasing — case analysis on H_n changes: (a) element replaced by strict subset increases f, (b) new incomparable element increases f
  4. f(H_n) < 1 for all n — for an intersecting antichain, f(H) <= 1 with equality iff H = {{p}} (Bollobas-type bound)
  5. If H_n changes at step n, f increases by at least 2^{-k} where k = max|Q| over Q in H_n — discrete jump
  6. Once any 2-element set {p,q} enters H, k <= max(original sizes, 2), bounding total changes — finite steps to stabilization
  7. H stabilizes to H_stable; all a_n in V_stable (by pairwise gcd argument) — from greedy-on-vstable skeleton steps 2-5
  8. V_stable is L-periodic, greedy cycles through T residues, a_{n+T} = a_n + L for all n — CRT + greedy enumeration

Key lemmas (claim + mechanism):
  - f(H) non-decreasing — replacement by strict subset: delta f = 2^{-|P|} - 2^{-|Q|} > 0 for P subset Q; new element: delta f = 2^{-|P|} > 0
  - f(H) <= 1 for intersecting antichains — counting argument or Bollobas inequality (intersecting family has bounded weight)
  - Finite H-changes — discrete increase >= 2^{-k} with f bounded => at most 2^k changes

Open gaps:
  - Proof that f(H) <= 1 for intersecting antichains (need explicit argument, likely via Bollobas or direct double-counting)
  - Bound on max element size k (show 2-element sets enter quickly, bounding k)

Cases to cover: same as greedy-on-vstable

Watch out for: The f(H) <= 1 bound for intersecting antichains is the key technical lemma; without it, finiteness doesn't follow

---

saturation-route: new
Target: Prove T, L exist such that a_{n+T} = a_n + L for all n >= 1
Technique: Show H becomes "saturated" (every valid m has P(m) superset some Q in H) in finite steps; once saturated, H is frozen
Skeleton:
  1. Define saturated antichain: H is saturated iff for every transversal P of H, P superset some Q in H — by definition
  2. If H_n saturated, then H_m = H_n for all m >= n — any a_{m+1} has P(a_{m+1}) transversing H_n, hence containing some Q; so P(a_{m+1}) doesn't add new minimal element
  3. 2-element sets {p,q} in H never leave (can only be replaced by 1-element = prime power => Case 2a) — in Sub-case 2b, 2-element sets are permanent
  4. Greedy eventually generates all necessary 2-element {p_i, p_j} for essential primes — Dirichlet: products of 2 primes appear with positive density in any valid residue class
  5. Once all essential pairs in H, H is saturated — case analysis: any valid m divisible by p_i, p_j for some pair, hence P(m) superset {p_i, p_j} in H
  6. Apply greedy-on-V_stable argument for periodicity — from greedy-on-vstable skeleton steps 7-8

Key lemmas (claim + mechanism):
  - Saturated => frozen — new term's prime set contains existing minimal set, doesn't change antichain
  - 2-element sets are permanent (Sub-case 2b) — no 1-element proper subset exists (that would be prime power = Case 2a)
  - Saturation via pairs — once H contains {{p_i,p_j} : all pairs from essential primes}, every transversal contains a pair

Open gaps:
  - Prove essential primes are finite (backbone suffices: every term shares prime with a_1)
  - Prove saturation happens (all essential pairs enter H)

Cases to cover: same as greedy-on-vstable

Watch out for: The "essential primes" set must be shown to be exactly the support of the final H_stable; need to prove primes outside this don't matter

---

backbone-periodicity: dead-end
Reason: Uses T(a_i) = P(a_i) intersect B (backbone types) but actual constraints involve all primes in P(a_i), not just backbone. For a1=15, gives wrong L=15 vs correct L=30. Fundamentally flawed constraint model. Cannot salvage without rewriting to use P(a_i) instead of T(a_i), which is exactly what the other approaches do.

---

clique-valid-set: dead-end
Reason: Outline-reviewer cut it in Round 1 for fatal gap in coprime-pair resolution. The approach tries to show V becomes a "clique" but the mechanism is unclear and the coprime-pair argument doesn't work.

---

## Build set recommendation

1. **greedy-on-vstable** (REVISE of two-of-k-structure): Primary approach. The backward extension is now trivial (pairwise gcd + antichain refinement). Main gap is proving H_stable finite (dichotomy argument).

2. **antichain-monovariant** (REVISE of antichain-stabilization): Alternative mechanism for proving stabilization. Uses monovariant f(H) instead of direct finiteness. Different gap profile (needs f <= 1 bound).

3. **saturation-route** (NEW): Third mechanism using saturation concept. Exploits permanence of 2-element sets and saturation via pairs. Most concrete combinatorial route.

All three share the greedy-on-V_stable enumeration step for the final periodicity, but differ in HOW they prove H stabilizes. This is good diversity: if one mechanism fails, the others might succeed.

## Verdict Summary

| Slug | Verdict | Note |
|------|---------|------|
| greedy-on-vstable | REVISE two-of-k-structure | Remove K_k^2, use pairwise gcd for backward extension, add dichotomy for finiteness |
| antichain-monovariant | REVISE antichain-stabilization | Close gaps via monovariant f(H) |
| saturation-route | NEW | Third mechanism via saturation and pair permanence |
| backbone-periodicity | DEAD-END | Wrong constraint model |
| clique-valid-set | DEAD-END | Fatal gap in coprime-pair resolution |

Build set: greedy-on-vstable, antichain-monovariant, saturation-route
