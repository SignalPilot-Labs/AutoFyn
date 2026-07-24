# Proof-reviewer report — round 2 — IMO 2026 P6 (imo-2026-06)

Two approaches judged independently. One is a complete, correct solve; one is honestly partial.

---

## 1. `admissible-set-periodicity` — VERDICT: APPROVE — Status: solved

Builder recorded `solved`. **Confirmed.** This is a complete, rigorous, non-circular proof of the
whole problem. I re-derived the load-bearing step (SP, via the Step D descent) from scratch and
checked every subordinate step and every case.

**Scores:** Correctness 10/10 · Completeness/rigor 10/10 · Progress: closes the sole open gap → full solve.

### Independent verification of each load-bearing step
- **Bridge (★) / G3 (Step A).** For n ≥ a₁, n is a term ⇔ gcd(n,m) > 1 for all terms m < n. Forward
  = Lemma 1. Converse: n = a₁ trivially a term (vacuous hypothesis, a₁ is the least term); n > a₁ uses
  j = max{k : aₖ < n} (exists since aₖ → ∞), terms below n are exactly a₁…a_j, eligibility gives
  a_{j+1} ≤ n, maximality gives a_{j+1} ≥ n, hence = n. G3 is the exact contrapositive (gcd > 1 fails
  ⇔ gcd = 1, since gcd ≥ 1). **Valid.** This is the only use of greedy minimality beyond Lemmas 1–3 —
  correctly load-bearing, not counting-based (satisfies the run's "must use greedy minimality" rule).
- **Step B (small factor).** Correct: gcd(b,a₁) > 1 forces a common prime dividing a₁, hence ≤ a₁.
- **Step C (compression witness), all cases including flagged N=0.** α = product of distinct small
  primes of b (α | b, α ≤ b, supp = small primes of b). Case 1 (no big prime): x = b. Case 2: x = pᴺα.
  N=0 ⇒ x = α | b ≤ b (checked). N≥1 ⇒ p^{N−1}α < a₁ ⇒ x < p·a₁ ≤ α·a₁ < α·q ≤ b, each inequality
  justified (p ≤ α since p | α; a₁ < q since q big; αq | b since α squarefree over small primes and
  q ∉ supp α). **All cases valid; supp(x) = small primes of b, no big factor, a₁ ≤ x ≤ b.**
- **Step D (SP) minimal-counterexample descent.** Assume a violating pair (distinct terms sharing no
  prime ≤ a₁); pick one with minimal max b′ (well-ordering). Compression x of b is coprime to b′
  (all its primes are small primes of b, none dividing b′), a₁ ≤ x ≤ b < b′. x cannot be a term
  (would contradict Lemma 1 with b′), so G3 yields a term b* < x with gcd(b*,x) = 1. Then {b,b*} is a
  distinct pair (b* < b) with max b < b′; their shared prime r (Lemma 1) must be big, else r | b ⇒
  r | x contradicts gcd(b*,x)=1. So {b,b*} is violating with strictly smaller max — contradiction.
  **Descent is valid, terminating, and does NOT assume SP or any finiteness** (no circularity: b* comes
  from G3, the shared prime from Lemma 1 — both hold unconditionally).

### Circularity / gap hunt — clean
- No step assumes (HS)/(SP)/finiteness of any essential-prime set. The proof *sidesteps* the round-1
  wall entirely: it does not bound the number of sole connectors — it proves sole connectors are
  impossible (every pair shares a small prime). Nothing rests on Σ1/p² counting.
- Certified imports applied correctly: Lemmas 1–3 and the Periodicity Machine match the certified
  statements verbatim; S = {primes ≤ a₁} is a finite hitting set in exactly the machine's sense, and
  T, L ≥ 1 (2 ≤ a₁ ⇒ prime 2 ∈ S), so the conclusion is the required aₙ₊T = aₙ + L for all n ≥ 1.

### Numerical corroboration (non-vacuous, per role memory)
SP checked directly: 0 violations across 27 diverse a₁ (15, 143, 1001, 858, primes, prime powers
49/121/169/289, primorials 210/2310, products) up to 400 terms — every term pair shares a prime ≤ a₁.

**current.md updated to solved with the Full proof. Promotable lemmas A/G3, B, C, D certified into
`lemmas/spine-small-common-prime.md`** (statements match proofs, sorry-free, no stronger than proved).

---

## 2. `profile-class-recruitment` — VERDICT: CHANGES REQUESTED — Status: partial

Builder recorded `partial` with (REC) as an explicit open gap. **Confirmed accurate — no overclaim.**

**Scores:** Correctness 10/10 (of what is claimed) · Completeness 5/10 (nucleus open) · Progress:
a clean, rigorous reduction of (HS) to the both-infinite disjoint-profile types.

- **Step B, Step 2 (finite profile alphabet), Step 3 (gap-divides-difference), Step 4a** all verified
  rigorous. Step 4a correctly disposes of any type where one profile occurs finitely often (that
  finite set's supports form a finite hitting set for those cross pairs). The reduction "(REC) ⇒ (HS)
  ⇒ theorem" is sound.
- **Step 4b (REC): honestly flagged as an unproved conjecture**, not hand-waved as closed — the write-up
  explicitly states the cheapest-patch monovariant and the recurrence assumption are *not established*.
  This is the correct, honest partial.

Now superseded by the `admissible-set-periodicity` solve (SP gives (HS) directly). Its promotable
lemmas (profile-alphabet reduction, connector bound) are correct but no longer needed for the solve.

---

## Outcomes recorded
- `admissible-set-periodicity`: **verified-milestone** (Elo 1571.6).
- `profile-class-recruitment`: **partial** (Elo 1515.4).

## Bottom line
IMO 2026 P6 is **SOLVED**. The complete proof is in `results/imo-2026-06/current.md` (Status: solved,
Full proof). The key move: every pair of terms shares a prime ≤ a₁ (spine SP), proved by a
greedy-minimality descent — so S = {primes ≤ a₁} is a finite hitting set and the certified periodicity
machine finishes.
