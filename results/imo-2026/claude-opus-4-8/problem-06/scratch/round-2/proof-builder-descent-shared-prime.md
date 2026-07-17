# Build report — descent-shared-prime (imo-2026-06, round 2)

**Status: SOLVED.** The approach is now a complete, rigorous, end-to-end proof. The sole
open gap (Lemma S′ via q-cofactor / minimal-counterexample descent) is closed.

## What was built
File: `results/imo-2026-06/approaches/descent-shared-prime.md` (full file-contract sections + Full proof + Promotable lemmas).

Structure:
1. **§0** imports the certified reduction (Tools 1–2, Sub-lemma E, Cor E.1, finish package) — not re-derived.
2. **§1 (Prop 1′ + finiteness):** Lemma S′ ⟹ every minimal clause ⊆ G={primes ≤ a₁} (via Cor E.1 + minimality) ⟹ finitely many minimal clauses ⟹ A periodic mod M, A_n=A eventually ⟹ certified finish ⟹ conclusion. Airtight (reviewer already verified this spine).
3. **§§2–4 (Lemma S′, the crux):** proved by **descent on the height (larger index) of a violating pair** — no leftover gap.

## How the open gap was closed (the key move)
The outline's step-4 worry (single-prime cofactor e leaves gcd(a_j,e)≠1 for multi-prime shared sets, and the b≤a₁ branch) is **sidestepped entirely**: instead of the cofactor e = a_k/q^{v}, I adapt **Claim 4 + Claim 5 of the IMO-2024-P5 (aimo-0030) second solution**.

- **Lemma S4 (§3, = Claim 4 analogue):** for a clause S_j with a big prime factor, construct a small-only integer x = p₀ⁿR with supp(x)=σ(S_j) (small shadow of a_j) and **a₁ ≤ x < a_j**. The size bound uses R·q | a_j (R = radical of small primes, q = a big prime of a_j): if n=0, x=R ≤ a_j/q < a_j; if n≥1, minimality gives x < p₀a₁ ≤ Ra₁ < Rq ≤ a_j. This handles both branches uniformly — the b≤a₁ case is no longer special because x is pinned into [a₁, a_j).
- **Descent (§4, = Claim 5 analogue):** take a minimum-height violating pair (S_j,S_k). Build x from S_j. Either (A) x is a term ⟹ supp(x)=σ(S_j) is a clause sharing a prime with S_k (Tool 2), contradicting σ(S_j)∩S_k=∅ (the violating property); or (B) x is not a term ⟹ x∉A (Sub-lemma E) and greedy minimality forces x∉A_s for the gap a_s<x<a_{s+1}, s≤j−1<k. The first clause S_t (t≤s<k) that x misses satisfies σ(S_j)∩S_t=∅, so (S_t,S_j) is a violating pair of **height j<k** — contradicting minimality. Both cases contradict, so no violating pair exists ⟹ Lemma S′.

The descent is on ℕ (height k), well-founded; each case ends in a genuine contradiction. The productive branch does **not** even use a_k (it contradicts minimality directly), and the term-branch uses only Tool 2 + the violating property. Only certified tools are invoked.

## Why this avoids the outline's flagged pitfalls
- **Multi-prime shared set:** irrelevant — x is built from S_j's small shadow, gcd(x,a_k)=1 is automatic from σ(S_j)∩S_k=∅ (2b), no prime-stripping of a_k needed.
- **b≤a₁ branch:** dissolved by Lemma S4's two-sided bound a₁ ≤ x < a_j; the value x is located strictly inside the term gaps, and greedy minimality (not Sub-lemma E's threshold) does the work.
- **aimo-0030 uses game moves we lack:** replaced "bad ⟹ move to good coprime" by "x∉A_s via greedy minimality ⟹ first missed clause S_t," a pure sequence argument.

## Verification (computational, sanity only — the proof stands alone)
- Lemma S′: **0 violations** for a₁ ∈ {15,35,77,143,210,255,385,1001,2310,4199}, depth 400.
- Prop 1′: **every minimal clause ⊆ {primes ≤ a₁}** in all cases (incl. the essential prime 19 ≤ 385 that broke round-1's P₁-Lemma S).
- Lemma S4's bound a₁ ≤ x < a_j: holds on **every** term with a big prime factor across tested a₁.

## Spec-concerns
None. The setup works; the reduction is the certified one; the crux is fully closed.

## Promotable lemmas (for certification into lemmas/)
- **Lemma S′** — any two clauses share a prime ≤ a₁. Proved §§2–4.
- **Prop 1′** — assuming S′, every minimal clause = its small shadow ⊆ {primes ≤ a₁}. Proved §1.
- **Lemma S4** — a clause with a big prime factor has a small-only companion x, supp(x)=σ(S_j), a₁ ≤ x < a_j. Proved §3.

## Recommendation
Route: **APPROVE** (Status solved). Suggest certifying Lemma S′ + Prop 1′ + Lemma S4 into `lemmas/` and promoting this proof into `current.md`.
