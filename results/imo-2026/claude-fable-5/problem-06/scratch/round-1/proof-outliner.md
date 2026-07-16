## imo-2026-06

Round 1 field: four new rival approaches, files created under `results/imo-2026-06/approaches/`.

**Headline discovery (proved in outline, not yet reviewer-certified):** the problem admits a very strong exact reduction. Let V = {m ≥ a_1 : gcd(m, a_k) > 1 for all k ≥ 1}. Then the sequence is EXACTLY the increasing enumeration of V (both inclusions are two-line arguments: pairwise sharing is definitional, and any m ∈ V above a_n is a candidate at step n+1 so the greedy lands on it). Moreover the family H* of prime-set "types" of terms equals the family of ALL finite prime sets hitting every term's prime set (realization: for any hitting set X = {p_1..p_r}, the numbers p_1^j·p_2···p_r are in V, hence are terms). So H* is a maximal intersecting (identically self-blocking) family, and the WHOLE problem is equivalent to one statement: **M := {inclusion-minimal types} has finite union E.** Given that, L = ∏_{p∈E} p, T = |V ∩ [a_1, a_1+L)|, and a_{n+T} = a_n + L holds for ALL n ≥ 1 with no separate pull-back argument (the "for all n" subtlety dissolves because the sequence IS the sorted periodic set from its first element). Also proved in outline: bounded gaps (every window of length g = ∏A, A a minimum-size member, contains a term), a CRT "dodging lemma" (terms avoiding any finite set of primes > g exist), the witness lemma (Y ∈ M, y ∈ Y ⟹ ∃W ∈ M with W ∩ Y = {y}), and a sunflower argument killing every infinite bounded-size subfamily of M with fixed small-prime trace. The one open crux across the field: finiteness of M in the unbounded-size case. Approaches 1–3 attack that crux by three different mechanisms; approach 4 hedges the reduction itself.

Cheap kill considered and rejected: single-prime domination ("some prime divides all terms from some point", T=1 style) — false for a_1 = 15 (no prime divides all terms); recorded in explorer data.

---

valid-set-sunflower-core: new
Target: full claim — ∃ T, L positive integers with a_{n+T} = a_n + L for all n ≥ 1.
Technique: sorted-valid-set identity + extremal set theory (Erdős–Rado infinite sunflower lemma, trace pigeonhole).
Skeleton:
  1. Any two terms share a factor — by definition of the greedy rule.
  2. {terms} = V — greedy minimality both ways (proved).
  3. H* = {types of terms} = {all finite hitting sets}; realization via p_1^j·p_2···p_r (proved). M = minimal elements; every X ∈ H* contains a member (finite descent).
  4. Bounded gaps (multiples of g = ∏A are terms), CRT dodging lemma, witness lemma (all proved).
  5. M finite — trace pigeonhole over E₀ = {p ≤ g}; infinite sunflower kills any bounded-size infinite subfamily with fixed trace (proved); unbounded-size case = GAP 1, with a proved β-extraction recursion as the lead.
  6. E = ∪M finite ⟹ any two terms share an E-prime ⟹ V is +L-periodic on [a_1, ∞) ⟹ a_{n+T} = a_n + L for all n (proved).
Key lemmas (claim + mechanism):
  - {terms} = V — because any element of V above a_n is a candidate at step n+1, and the greedy is minimal, so it cannot be skipped.
  - Realization — because p_1^j·p_2⋯p_r has type exactly X and lies in V for large j.
  - Sunflower kill — because the sunflower core is a proper subset of a minimal member, hence non-hitting, and its witness must meet infinitely many disjoint petals, impossible for a finite set.
  - GAP 1 (open): no infinite chain of "big primes" β_1, β_2, ... each lying in infinitely many minimal members.
Open gaps: GAP 1 only. Everything else is finished prose.
Cases to cover: none (not case-based); antichain edge cases (unique member with empty big part) flagged in file.
Watch out for: infinite sunflower lemma must be proved inline (not in knowledge base); Δ_n guardrail — minimal member sizes can be arbitrarily large in finite instances, so no universal size bound may be assumed.

crt-window-small-prime-lockin: new
Target: full claim, same statement.
Technique: same reduction + number-theoretic small-prime lock-in via CRT dodging windows and greedy first-appearance analysis. STRONGER core claim: ∪M ⊆ {primes ≤ g} — greedy dynamics forbid big primes from ever being essential.
Skeleton:
  1. Shared reduction R1–R6 (proved, same as sunflower file).
  2. Suppose ρ > g lies in a minimal member Y with witness W, W ∩ Y = {ρ} — two constraints whose only common resource is a big prime.
  3. Contradiction via: first term whose validity is certified only through ρ vs. the multiple of g available in the same window (greedy minimality); maximal ρ-sunflower collections F_1..F_r bounded by disjoint E₀-traces (r ≤ |E₀|, proved); dodging-window terms forced to hit W through W ∩ E₀. GAP A.
  4. E₀ finite core ⟹ finale R7 (proved).
Key lemmas (claim + mechanism):
  - Dodging lemma — because primes > g have multiples spaced > g apart, CRT aligns a full window of length g avoiding them, and that window contains a term (a multiple of g).
  - Maximal ρ-collections force ∪(F_i∖{ρ}) ∈ H* — because a set missing it would extend the collection, contradicting maximality.
  - GAP A (open): big prime in a minimal member contradicts greedy minimality at its first load-bearing appearance.
Open gaps: GAP A. Note this claim is stronger than GAP 1; if GAP A closes, approach 1's gap closes too (not conversely).
Cases to cover: Y = {ρ} singleton (a_1 prime) — handled: then ρ ∈ A so ρ ≤ g, no conflict; must check the argument only targets ρ ∉ A.
Watch out for: junk primes in terms vs. primes in minimal types are different things; the a_1 = prime case makes "all essential primes are absolutely small" false — smallness is relative to g.

self-blocking-clutter-induction: new
Target: full claim, same statement.
Technique: same reduction + a pure combinatorics theorem: every identically self-blocking clutter of finite sets is finite; induction on τ = min member size with link/cross-blocking structure (no sunflowers, no CRT — independent mechanism).
Skeleton:
  1. Shared reduction (proved); M satisfies b(M) = M.
  2. τ = 1: M = {{a}} (proved).
  3. k = 2 model: all witnesses of M_{{a}}-members pass through b (proved) — cross-blocking link pair structure.
  4. Inductive step: cross-blocking pairs of link families are finite; trace recursion over ∅ ≠ I ⊆ A. GAP B.
  5. Finale R7 (proved).
Key lemmas (claim + mechanism):
  - Witnesses through b — because a witness avoids Y ∖ {y} ∋ a and must still meet A = {a,b}.
  - GAP B (open): the induction hypothesis must be a cross-pair statement (links of Δ_n are stars, so single-clutter self-blockingness does not pass to links).
Open gaps: GAP B.
Cases to cover: |I| = k gives M_A = {A} (antichain); all traces I covered by the recursion.
Watch out for: Δ_n guardrail again — |M| is NOT bounded by any function of τ; only infinitude is impossible. No ground-set counting allowed (ground is infinite).

finite-state-window-pullback: new
Target: full claim, same statement.
Technique: finite-state dynamics — effective-window stabilization + pigeonhole on a_n mod Λ + pull-back to n = 1 (crux analogies aimo-0514 reversibility, aimo-0678 modulus reduction). The only approach NOT using the sorted-V identity: the field's hedge.
Skeleton:
  1. Bounded increments via a finite locked prime pattern — GAP C1.
  2. Effective window stabilization (new constraints become inert on the moving window) — GAP C2.
  3. Finite-state pigeonhole ⟹ eventual a_{n+T₀} = a_n + L₀.
  4. Pull-back to n = 1 via reversibility or downward induction — GAP C3 (likely needs the rivals' core lemma; if so, mark dead rather than let it collapse into them).
Key lemmas: state s_n = a_n mod Λ determines the increment once windows stabilize — because the valid set on the window becomes a fixed union of residue classes.
Open gaps: C1, C2, C3 — all open; C3 flagged as probably fatal.
Cases to cover: none.
Watch out for: "primes dividing infinitely many terms" is an infinite set (all-evens example: every odd prime qualifies) — both the structure and analogy explorers' P*/S definitions are broken as stated; any state must use essential primes. Eventual periodicity is NOT enough — the claim is for all n ≥ 1.

---

Notes for the reviewer:
- Single-line risk: approaches 1–3 share the reduction (R1–R6). I judge that risk low — the reduction proofs are short, elementary, and written out in full in valid-set-sunflower-core.md; recommend the first builder formalize them and the proof-reviewer certify them as shared lemmas (`lemmas/terms-equal-valid-set.md`, `lemmas/finite-core-implies-periodicity.md`, `lemmas/dodging-and-witness.md`). Approach 4 hedges the residual risk.
- The three live cruxes (GAP 1, GAP A, GAP B) are logically related but mechanistically disjoint: sunflower/extremal, greedy/CRT-dynamic, clutter induction. GAP A ⟹ GAP 1. Closing ANY one solves the problem.
- Suggested build priority: valid-set-sunflower-core (most proved content, sharpest single gap), then crt-window-small-prime-lockin, then self-blocking-clutter-induction; finite-state-window-pullback is a low-cost hedge and can wait if builder slots are scarce.
- Empirical anchors (computation explorer, verified 200–400 terms): a_1=15: T=8, L=30; a_1=35: T=34, L=210; a_1=77: T=18, L=154; periodicity holds from n=1 in every test — consistent with the sorted-V reduction's prediction that no transient exists.
