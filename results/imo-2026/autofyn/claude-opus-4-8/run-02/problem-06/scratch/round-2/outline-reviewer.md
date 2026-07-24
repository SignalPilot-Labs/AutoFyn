# Outline Review — Round 2, IMO 2026 P6 (imo-2026-06)

Context: whole problem certified-reduced to the single open finiteness statement (HS) — a finite
prime hitting set ⇒ exact periodicity from n=1 (via certified Lemmas 1-6). Round 1 proved pure
counting/density (Σ1/p²) insufficient. Two approaches reviewed.

## admissible-set-periodicity (revise) — APPROVE

The revision grafts a **complete, non-counting proof of (HS)** onto the certified reduction. It rests
on greedy minimality (Lemma 2), exactly the load-bearing input the counting wall lacked. I checked
both the logic and the numerics; it holds.

**Numerical verification (all pass, no exceptions):**
- The target spine theorem **(SP)** — *any two terms share a prime ≤ a₁* — holds with **0 violating
  pairs** across a₁ ∈ {15,143,1001,858,105,30,210,77,91,6,2310}, 120 terms each. Note this is the
  right threshold: the weaker "share a prime dividing a₁" FAILS heavily (thousands of pairs), so the
  ≤ a₁ (not | a₁) formulation is essential and correct.
- **Step C (compression witness):** the constructed x satisfies supp(x) = {small primes of b},
  no big factor, a₁ ≤ x ≤ b — **0 failures** across all tested a₁.
- **(★) bridge:** for every n in [a₁, max term], "n is a term ⟺ n shares a common prime with every
  smaller term" — **0 failures**.

**Logic audit of the two flagged steps:**
- **(★) ⟸ (the bridge):** sound and non-circular. With j maximal s.t. a_j < n, the terms below n are
  exactly a₁..a_j, so the hypothesis gives F_j(n); Lemma 2 forces a_{j+1} ≤ n, maximality forces
  a_{j+1} ≥ n, hence a_{j+1} = n. Uses only the certified greedy characterization, no assumption of
  the conclusion. Edge case n=a₁ correctly flagged (term trivially; no smaller term, so ⟸ vacuous).
  G3 (contrapositive) is a clean consequence.
- **(SP) descent (Step D):** sound and genuinely descending. Minimal-max violating pair {b,b'},
  b'>b (forced by Step B's small prime p|b, p∤b'). Compression x of b is coprime to b' (all its primes
  are small primes of b, which b' avoids), x≥a₁ and x≤b; x is not a term (else x,b' coprime terms
  contradict Lemma 1); G3 yields term b*<x coprime to x. Then {b,b*}: share a prime (Lemma 1), and
  every common prime is big (a small common prime r would divide α|x, contradicting gcd(b*,x)=1) — so
  it is a violating pair with max b < b'. Contradiction with minimality. No circularity, no missing
  case, and it descends on max(pair) which is well-ordered.

**Case coverage:** Step C's two cases (b has / lacks a big prime factor) both handled — the N=0
subcase gives x=α|b ⇒ x≤b by divisibility (the p·a₁ size chain is only needed for N≥1); builder must
state this split explicitly. Reduction Lemmas 1-6 are certified — reuse verbatim, do not re-prove.

This is, as far as I can verify, a complete and correct proof of the whole problem. Builder should
render Steps A-D fully rigorous prose. Watch-points for the builder:
- Step C size chain: separate N=0 (x=α|b) from N≥1 (x<p·a₁≤α·a₁<α·q≤b); justify α·q|b via
  distinct-prime-product (α squarefree = radical of small part, q big ⇒ q∉supp α).
- Step D(iv): show the common prime r is big BEFORE calling {b,b*} a violating pair, and confirm
  {b,b*} shares a prime (Lemma 1) so it is a genuine pair.
- (★) ⟸: handle n=a₁ separately.

## profile-class-recruitment (new) — CHANGES REQUESTED (register as diversity hedge)

A genuinely different framing of (HS): finite S₀-profile alphabet + gap|difference size bound +
monovariant over disjoint-profile obligation class-pairs. Steps 1-3 are rigorous (finite alphabet is
correct — profiles ⊆ fixed S₀ via certified Step B; connector bound p|(a_j−a_i)≤(j−i)R is the certified
bounded-gap fact). No counting-wall reliance, no circularity, valid whole attempt (targets the full
theorem via the certified reduction). It shares only the greedy-minimality *input* with the descent
route, not its machinery, so it satisfies anti-collapse and is a legitimate hedge if a builder-level
flaw surfaces in the descent.

**Open nucleus (Step 4, recruitment termination):** the "once a small prime r is recruited, greedy
minimality forbids any fresh large sole connector for that obligation" lemma is stated with a
mechanism but not closed — it is the same hard nucleus in different dress. Honestly flagged by the
outliner as the hedge, not the expected closer. Builder should push Step 4 toward: for a
disjoint-profile obligation occurring infinitely often, exhibit the recruited small prime and show a
smaller admissible candidate divisible by it lies in the ≤R window, blocking a fresh large connector.
Do NOT reintroduce Σ1/p² density.

## De-prioritized (not nominated, per outliner and round-1 findings)
- `essential-prime-counting` — Σ1/p² interval-occupancy is the reviewer-confirmed dead counting wall
  (cannot exclude sparse density-zero disjoint families); no new mechanism.
- `finite-state-reversible` — its reversibility attacks exactness-from-n=1, already delivered free by
  the certified static machine; does not attack (HS) finiteness.

## Ranking (Elo after this round)
admissible-set-periodicity 1571.6 (complete descent proof, leader) >
profile-class-recruitment 1515.4 (new, live hedge, open nucleus) >
essential-prime-counting 1484.8 (dead counting wall) >
finite-state-reversible 1428.1 (attacks the wrong part).

## Diversity note for the orchestrator
The field is NO LONGER collapsed to one framing: descent (extremal minimal-counterexample +
compression witness) and recruitment (finite profile alphabet + monovariant) are far apart in route,
sharing only greedy minimality. If the descent proof is certified next round, the problem is solved.

build set: admissible-set-periodicity, profile-class-recruitment
