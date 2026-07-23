# Proof-builder report — imo-2026-06 / clique-descent (round 1)

**Status: partial.** The entire problem is now rigorously reduced to a single clean, self-contained lemma (**Lemma S**), with every other step proved in full.

## What is fully proved (rigorous, no gaps)
- **Tool 1** (bounded gaps ≤ a₁, well-definedness, aₙ→∞, every term has a prime ≤ P₁).
- **Tool 2** (clauses pairwise intersect; every term ∈ A; supports-that-are-clauses ∈ A).
- **Sub-lemma E** (greedy takes every admissible value > a₁) + Corollary E.1 (a prime-set hitting every clause is a clause). This is the clean lever that upgrades "admissible" to "is a term."
- **Reduction (Prop 1):** *assuming Lemma S*, every minimal clause ⊆ Π = {primes ≤ P₁}. Proof is airtight: divide out the large prime q from the term; either T = C\{q} hits every clause (⇒ T is a clause ⊊ C by Cor E.1, contradicting minimality) or some clause meets C only in {q} (contradicting Lemma S).
- **Stabilization (§2):** finitely many minimal clauses ⇒ chain Aₙ stabilizes at a finite N (every later clause contains an already-present minimal clause ⇒ redundant). A is periodic mod M = ∏_{p∈E} p, E ⊆ Π.
- **Finish (§§3–4):** every term ∈ A (Tool 2), and aₙ₊₁ = min(A ∩ (aₙ,∞)) for ALL n (min-of-superset), so the sequence is the greedy enumeration of A from n=1; periodicity of A gives a_{n+T}=a_n+L for every n with L = M, T = |A mod M|. Verified: a₁=143 ⇒ minimal clauses {2,11},{3,11},{11,13},{2,3,13}, E={2,3,11,13}, and simulation gives exact period L=858 (T=64), consistent with M=2·3·11·13=858.

## The single GAP: Lemma S
**Lemma S:** any two terms sharing a prime share a prime ≤ P₁ (equivalently: no two clauses share only a large prime).
- Verified computationally with **zero violations** across 14 starts (prime powers, even, odd, up to 4 prime factors), 3000–6000 terms.
- Partial progress proved: the *first-appearance* clause of any large prime q is non-minimal (contains the clause S_{i(q)}\{q}), subject to a mild size condition b > a₁.
- Why it resists: a minimal clause with a large prime need not be a first appearance; step-local greedy minimality does not force a small shared prime, so a global descent on the pairwise-intersecting clause family is needed. This is the genuine hard core.

## Promotable lemmas (for certification)
Tool 1, Tool 2, Sub-lemma E (+ Cor E.1), and the "stabilization ⇒ conclusion" package (§§2–4). All proved in full and reusable by sieve-closure / any approach that establishes finiteness of minimal clauses (or periodicity of A).

## Spec concerns
- The outliner/reviewer target "essential primes ≤ maxpf(a₁)" is empirically true but is *not* the minimal sufficient statement. The clean sufficient crux is **Lemma S** (no two clauses share only a large prime). NB: minimal clauses can be numerous transiently — there can be 2000+ distinct clauses — but only finitely many *minimal* ones (all ⊆ Π); the essential-prime bound is a consequence, not the lever.
- Reviewer's note that step 3 (A-is-a-clique) is dead weight is correct and acted on: it is removed; the finish uses Tool 2 on minimal clauses only.
- For a genuinely different framing next round: Lemma S is a statement purely about the pairwise-intersecting ("sunflower") structure of the clause family with bounded core Π. An approach attacking Lemma S via sunflower/Δ-system or via a descent on the largest prime ever shared would be far from the current field and is the recommended diversification if this route stalls.
