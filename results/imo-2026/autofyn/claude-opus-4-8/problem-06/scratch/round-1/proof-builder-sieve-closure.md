# Proof-builder report — imo-2026-06, approach `sieve-closure` (round 1)

## Status: partial

## What I did
Filled the outline into a rigorous proof that is **complete modulo one crux**. Directly addressed the outline-reviewer's CHANGES-REQUESTED concerns:

1. **"Φ-monovariant must actually bound termination independently, or import the crux honestly."**
   I did NOT dress up a monovariant as escaping the crux. I proved a *genuine* strict density-drop monovariant (Lemma 3: every effective step lowers density by ≥ 1/M_{n+1}, density ≥ 1/a_1) and then stated explicitly and honestly that it does **not** bound the number of effective steps (per-step drops shrink as the modulus grows), and that the coprime-pair Φ needs a finite ambient modulus = the same essential-prime bound. The crux "essential primes finite" is left as a clearly-labeled GAP, imported (shared with clique-descent), not smuggled.

2. **"Do not smuggle the greedy-enumeration finish into the 'becomes self-consistent' step."**
   The vacuous-constraint / fixed-point lemma (Lemma 1) is proved as a clean *conditional* ("if A_n is self-consistent then it is fixed") using only that the next term lies in the clique — it does not invoke the enumeration finish. Reaching self-consistency is explicitly identified as the crux, not assumed.

## Fully proved (unconditional)
- T1 (gaps ≤ a_1), T2 (pairwise gcd > 1).
- Minimal-clause reduction; each A_n periodic mod M_n.
- Lemma 1 (self-consistent ⇒ fixed) — the closure fixed point. Novel to this approach.
- Lemma 2 (Reduction): finite essential primes ⇒ A_n is a descending chain of unions of residue classes mod a FIXED modulus ⇒ stabilizes. Clean order-theoretic formulation of the crux.
- Lemma 3 (strict density-drop monovariant) — rigorous, with quantitative drop.
- The complete FINISH (§3): every term ∈ A (T2); a_{n+1}=min(A∩(a_n,∞)) for EVERY n; sequence = increasing enumeration of A from a_1; hence a_{n+T}=a_n+L for every n with L=M=∏(essential primes), T=|A mod M|.

## The single open GAP (crux)
Essential primes Π are finite. This approach reduces it to a fixed-modulus descending chain and supplies two monovariants, but does not bound Π independently. Empirically Π ⊆ {primes ≤ maxpf(a_1)} (verified a_1 ∈ {6,9,15,35,77,105,143,221,1001,…}). This is exactly clique-descent's target; if certified as a shared lemma, §2–§3 here complete immediately.

## Verification (sympy)
Simulated a_1 ∈ {15,35,143,77,105,221,6,9,1001}: in every case A_n stabilizes, essential primes ≤ maxpf(a_1), maxgap ≤ a_1, the stable A is a genuine GCD-clique (self-consistent), density(A) ≥ 1/a_1, and a_{n+T}=a_n+M holds on the whole tail — confirming the framing and every proved lemma.

## Spec concerns
- **Single-shared-gap risk is real and confirmed.** All of sieve-closure, clique-descent, finite-state-bijection bottom out on "essential primes finite." My monovariants (density, Φ) genuinely do NOT crack it — they need the prime bound first. So this approach does not provide an independent escape; it provides a cleaner *reformulation* (fixed-modulus descending chain + closure fixed point) plus reusable lemmas.
- **Recommendation to orchestrator:** the density/order-theoretic levers are exhausted here. If clique-descent's number-theoretic domination also stalls next round, a genuinely different framing is needed for the crux (e.g. bounding the modulus M directly from bounded-gap dynamics without isolating minimal clauses), as the outline-reviewer's diversity flag warned.
- The finish, T1, T2, Lemma 1, Lemma 2, Lemma 3 are all certifiable as shared lemmas now.

## Promotable lemmas
T1, T2, Lemma 1 (vacuous-constraint/fixed-point), Lemma 2 (Reduction), Lemma 3 (density monovariant), and the Finish lemma — all proved in full this round; see the approach file's "Promotable lemmas" section.
