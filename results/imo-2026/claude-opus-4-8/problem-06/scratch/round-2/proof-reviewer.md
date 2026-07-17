# Proof-reviewer report — round 2 — imo-2026-06

Two approaches reviewed independently. Headline: **descent-shared-prime is complete and correct — the problem is SOLVED.**

---

## 1. descent-shared-prime — VERDICT: APPROVE — Status: solved

**Builder's claimed Status (solved) is CORRECT.** I re-derived every load-bearing step from scratch and stress-tested the crux computationally.

**Scores:** Correctness 10/10 · Completeness/rigor 10/10 · Progress: closes the sole round-1 gap → full solution.

### What I checked

**Reduction (imported).** Tools 1–2, Sub-lemma E/Cor E.1, finish package are the reviewer-certified round-1 lemmas (`lemmas/bounded-gaps-and-clique.md`); imported correctly, not re-derived. Legitimate.

**Prop 1′ (Lemma S′ ⇒ minimal clause ⊆ G).** Sound. C minimal ⇒ σ(C)≠∅ (Tool 1); Lemma S′ makes σ(C) hit every clause; Cor E.1 makes σ(C) a clause; minimality forces σ(C)=C⊆G. Finiteness of 𝓜, periodicity of A mod M, and A_n=A for n≥N all follow correctly, and the certified finish package delivers a_{n+T}=a_n+L for **every** n. No gap.

**Lemma S4 (the novel construction) — re-derived independently.** For a clause S_j with a big prime and σ(S_j)≠∅, x=p₀ⁿR satisfies supp(x)=σ(S_j) and a₁≤x<a_j. The two-sided bound is valid: Rq | a_j gives Rq≤a_j (⋆); n=0 ⇒ x=R≤a_j/q<a_j; n≥1 ⇒ x<p₀a₁≤Ra₁<Rq≤a_j via p₀≤R, a₁<q, (⋆). Every inequality (strict/non-strict) is correct. **Verified empirically** across a₁∈{15,35,143,385,2310,4199}: 0 failures on all terms with a big prime factor.

**Lemma S′ descent (the load-bearing move) — re-derived from scratch.** Minimum-height violating pair (S_j,S_k). (2a) j≥2 & S_j has a big prime — correct (S₁⊆G blocks index 1). (2b) σ(S_j)∩S_k=∅ — correct. Case A (x a term): m<k since a_m=x<a_j<a_k, Tool 2 forces S_m∩S_k≠∅ contradicting σ(S_j)∩S_k=∅ — airtight, and m≠k is properly established. Case B (x not a term): x>a₁ so x∉A (Sub-lemma E); s with a_s<x<a_{s+1}, 1≤s≤j−1 correctly located; x∉A_s by minimality of a_{s+1}; least t with supp(x)∩S_t=∅, t≤s<k; {S_t,S_j} shown violating of height j<k (any shared prime is big, else it lands in σ(S_j)∩S_t=∅) — contradiction with minimum height. Both cases genuinely close. No circularity, no "clearly", every case disjoint and settled.

**Corrected threshold (a₁ vs P₁).** Confirmed the round-1 false Lemma S used threshold P₁ (falsified at a₁=385, prime 19>P₁=11). S′ uses threshold a₁, and Lemma S4's bound (a₁<q) genuinely requires it. **Computationally verified 0 violations of S′ and all minimal clauses ⊆{primes≤a₁} for a₁∈{15,35,77,143,210,255,385,1001,2310,4199}** — including a₁=385 where 19≤385 is small.

**Verdict.** Complete, rigorous, answers the actual `proof_only` claim (existence of T,L with a_{n+T}=a_n+L for every n). Recorded to `current.md` (Status solved + Full proof). Certified Lemma S4, Lemma S′, Prop 1′ into `lemmas/shared-small-prime.md`.

---

## 2. clique-descent — VERDICT: CHANGES REQUESTED — Status: partial

**Builder's claimed Status (partial) is CORRECT and honest.**

**Scores:** Correctness 10/10 (of what's proved) · Completeness/rigor: partial, gap honestly flagged · Progress: retargeted off the round-1 false Lemma S; three correct new structural lemmas.

- **Lemma 1 (self-blocking clutter):** correct — clauses = transversals of 𝓜 (Cor E.1 + Tool 2 + every clause ⊇ a minimal one), so 𝓜=b(𝓜).
- **Proposition 2 (finite-ground-set reduction):** correct — Q finite ⇒ every minimal clause ⊆ Π∪Q finite ⇒ 𝓜 finite. This is the sound, non-circular replacement of the retracted false round-1 Prop 1 (survives a₁=385).
- **Lemma 3 (mutual witness):** correct — each q∈Q sits in two minimal clauses meeting in exactly {q} with disjoint nonempty shadows; Φ:Q→disjoint shadow-pairs has finite image; Q finite ⟺ Φ finite fibers.

**Gap (honestly stated):** "Q finite" / "Φ has finite fibers." The §4 conditional bound (via Lemma T = "≤1 large prime per minimal clause") is admitted as unproven, with a candid note that shallow primorial simulations may overcount minimal clauses. No overclaim.

Note: this gap is now **closed independently** by descent-shared-prime's Lemma S′ (every minimal clause ⊆ {primes ≤ a₁} ⇒ 𝓜 finite ⇒ Q finite). As its own standalone framing, clique-descent remains partial. Its Lemmas 1–3 are correct and reusable — certified into `lemmas/clutter-and-reconciliation.md`. Route: CHANGES REQUESTED (or retire in favor of the solved approach; keep for framing diversity).

---

## Outcomes recorded (via ranker internal record_outcome logic)
- descent-shared-prime → **verified-milestone** (Lemma S′ closes the whole problem).
- clique-descent → **partial** (self-blocking clutter + Prop 2 + Lemma 3; Q-finite gap open).

## Lemmas certified
- `lemmas/shared-small-prime.md` — Lemma S4, Lemma S′, Prop 1′ (from descent-shared-prime). PASS.
- `lemmas/clutter-and-reconciliation.md` — Lemma 1, Prop 2, Lemma 3 (from clique-descent). PASS.

## current.md
Updated by reviewer: Status = solved; Full proof written.
