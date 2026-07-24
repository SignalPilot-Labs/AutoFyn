# Proof review — IMO 2026 P6 (`imo-2026-06`), round 1

Two approaches reviewed independently. Both are honest, correct **partial** reductions of the
whole problem to one finiteness nucleus. Neither is complete; neither overclaims. Verdict for
both: **CHANGES REQUESTED** (Status `partial` — matches builder self-assessment).

The load-bearing step (finite hitting set ⇒ exact periodicity from n=1) was re-derived
independently and verified numerically: greedy simulations reproduce the claimed (T,L) exactly —
a₁=15→(30,8), a₁=143→(858,64), a₁=1001→(2002,282), a₁=858→(2,1), a₁=105→(210,58) — with zero
period mismatches over the tested ranges (meaningful, non-vacuous checks).

---

## Approach `admissible-set-periodicity` — CHANGES REQUESTED, Status partial

**Scores:** Correctness 10/10 (everything stated is proven correct) · Rigor 9/10 (reduction
gap-free; only the P2 "log-bound" partial is loosely stated but explicitly labeled non-closing) ·
Progress: high — reduces the entire problem, exactness included, to a single clean statement.

**Reduction audit — airtight.**
- Lemma 1 (pairwise non-coprimality ⇒ every term ∈ A): correct.
- Lemma 2 (enumeration = increasing enumeration of A∩[a₁,∞), no element of A between consecutive
  terms): correct — the min/min sandwich (2.1)/(2.2) is valid.
- Lemma 3 (every multiple >1 of R∈A ⇒ gaps ≤ R, linear growth): correct.
- Lemma 4 (finite hitting set S ⇒ A∩[a₁,∞)=A_S∩[a₁,∞)): correct, including the i=k edge case
  (some prime of S divides each term, via any other pair).
- Lemma 5 (A_S is a union of residue classes mod L=∏S): correct — membership depends only on
  {p∈S : p|x}, hence on x mod L (L squarefree). CRT step sound.
- Lemma 6 / Corollary 5' (exact L-periodicity of E on [a₁,∞) ⇒ e_{n+T}=e_n+L from n=1):
  **the exactness-from-n=1 step is valid.** It works because E = (union of residue classes) ∩
  [a₁,∞) is periodic on the *whole* ray starting at a₁ (no pre-period), and a₁∈E; the shift-by-L
  order-preserving bijection E→E∩[a₁+L,∞) carries the T smallest elements cleanly. No hidden
  assumption. Verified numerically above.

**The single gap (correctly isolated, genuinely open):** (HS) — a finite hitting set exists /
the sole-connector set 𝒞 is finite. Partial progress (P1 Σ1/p² pair-density, P2 cross-class log
bound) is honestly flagged as NOT closing the gap: P1 bounds pair *density* but not the *number*
of distinct sole-connector primes; P2 grows like log i (unbounded). No overclaim. P2's pigeonhole
estimate is somewhat loose but is explicitly recorded as non-closing partial progress, so it does
not affect correctness of the reduction.

**No other hand-waves.** The finiteness nucleus is the only gap.

---

## Approach `essential-prime-counting` — CHANGES REQUESTED, Status partial

**Scores:** Correctness 10/10 · Rigor 10/10 (reduction gap-free; partial attack stated cleanly
and correctly, with the missing input honestly named) · Progress: high (same-strength reduction).

**Reduction audit — airtight**, and slightly cleaner than the sibling on one point: it takes
S = Π = {min(supp aᵢ ∩ supp aⱼ) : i<j}, which is **automatically** a hitting set (no separate
"𝒞 hits every pair" verification needed). So (★) "theorem ⇔ Π finite" is exact.
- Lemma A (gaps ≤ R, linear growth): correct.
- Lemma B (static set + enumeration, A∩[a₁,aₙ]={a₁,…,aₙ}): correct — clean induction.
- Lemma C (increasing enumeration of an L-periodic set, exact from a₁): correct — two increasing
  enumerations of one set agree termwise; the T≥1 argument is valid.
- Lemma D (finite pairwise-connecting S ⇒ exact periodicity from n=1): correct. Claim 1 (A∩[a₁,∞)
  = A_S∩[a₁,∞)) and Claim 2 (A_S = union of residue classes mod L via CRT, L squarefree) both
  sound; the reduction to 𝒯 = {supp(aᵢ)∩S} being a finite family of nonempty sets is valid.

**The single gap (correctly isolated, genuinely open):** MCL — Π finite. The interval-occupancy
bad-pair bound (#{K-bad pairs ≤ Y} < Y²/(2(K−1))) is rigorous, as is the "no two disjoint heavy
types" corollary (min(U_a,U_b) ≤ Y/√(K−1)). The honest gap is correctly identified: sparse
(density-zero) disjoint essential prime-families evade any pure pair-count, and excluding them
requires **greedy minimality** — correctly noted that a non-greedy pairwise-non-coprime sequence
CAN have infinitely many essential primes, so minimality is genuinely necessary. No overclaim.

**No other hand-waves.** The finiteness nucleus is the only gap.

---

## Cross-cutting note (for the orchestrator / outliner)

Both approaches share essentially the **same reduction spine** and have both bottomed out on the
**same nucleus** (HS/MCL finiteness), each defeated by the same wall (counting cannot bound the
*number* of essential primes). This is the single-gap trap forming already in round 1. Next round
should put ≥1 approach on a genuinely different framing that uses **greedy minimality** as the
active ingredient (e.g. a minimality/exchange argument bounding when a large prime can be the sole
connector), rather than another counting variation.

## Certified lemmas (promoted this round)
Both approaches' reduction lemmas hold to the full bar (sorry-free, statements match proofs). Admitted:
- `results/imo-2026-06/lemmas/enumeration-and-bounded-gaps.md` — Lemmas 1/2/3 (= A/B): every term
  admissible, enumeration of A∩[a₁,∞), bounded gaps ≤ R / linear growth.
- `results/imo-2026-06/lemmas/finite-hitting-set-periodicity.md` — the periodicity machine
  (Lemmas 4–6 / C–D): finite hitting set ⇒ exact L-periodicity ⇒ a_{n+T}=a_n+L from n=1.

`current.md` updated: Status partial, Current best = the certified reduction with the isolated
open nucleus.
