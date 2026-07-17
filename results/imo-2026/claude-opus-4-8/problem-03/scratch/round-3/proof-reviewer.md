# Proof review — imo-2026-03, approach `direct-constructive` (round 3)

**Verdict: CHANGES REQUESTED. True Status: partial.** Builder's recorded Status (`partial`) is
correct and honest — no overclaim.

## Answer
c(n) = 2^n/(2^{n+1}−1), D = 2^{n+1}−1. Consistent with round-2 grid minimax (n=1→2/3, n=2→4/7).
Answer stated explicitly. Not yet a `solved` proof (upper and lower bounds incomplete).

## Load-bearing new step re-derived independently: Lemma H — CORRECT and RIGOROUS
Claim: XY halves each of the p−1 largest LB pieces (p−1 ≤ n cuts, since p ≤ n+1) and spares
a_p ⟹ O = 1/2 + a_p/2.

I re-derived from scratch. Pieces = p−1 exact pairs {a_i/2, a_i/2} + singleton a_p.
- **Pair cancellation.** On the generic set (a_i mutually distinct, a_i/2 ≠ a_p) each equal
  pair occupies two consecutive ranks r, r+1; opposite signs in A = Σ(−1)^{ρ+1}r_ρ give a net
  0 contribution, wherever the pair sits. ✓
- **Singleton rank.** Exactly 2k pieces (k = #{i: a_i/2 > a_p}) exceed a_p, so a_p sits at
  rank 2k+1 (odd), contributing +a_p. Both copies of any pair lie on the same side of a_p, so
  the "2k" count is exact. ✓ Hence A = a_p, O = (1+A)/2 = 1/2 + a_p/2.
- **Continuity extension.** The genericity is only on the LB vector (a_i); the pairs are exact
  by construction for EVERY (a_i). O and 1/2 + a_p/2 are both continuous in (a_i), equal on the
  dense generic set, hence equal everywhere. This is airtight (the coordinate a_p is continuous
  and the pair structure persists off the generic set). ✓
- **Machine check.** I ran 2·10^5 random configs (p ≤ 6): max |O − (1/2 + a_p/2)| = 1.1·10^{-16}.

**Corollary (Case A).** a_p ≤ 1/D ⟹ O = 1/2 + a_p/2 ≤ 1/2 + 1/(2D) = (D+1)/(2D) =
2^{n+1}/(2D) = 2^n/D = c(n). Algebra verified (D+1 = 2^{n+1}). Since XY only needs one strategy
achieving ≤ c(n), this **closes Case A of the upper bound for all n** — a genuine, general new
slice of the field-wide upper-bound wall. This is the round-3 breakthrough and I certify it
(see `lemmas/H-halve-largest.md`).

## Circular integral ‡ — correctly NOT reintroduced
§4.2 explicitly DROPS the old reduction ∫⌊(N_F−N_I)/2⌋dt ≤ 0, noting it is identically 2^n − O
(a rename, not a reduction). It is not load-bearing anywhere in the round-3 proof. Confirmed.
(The stale current.md still cited ‡ as "progress"; I have rewritten current.md to remove it.)

## Other new claims — checked
- **G-L1(n)** [I_n = {2^0..2^{n−1}}, |F| ≤ n+1, ΣF ≤ 2^n ⟹ E ≤ 2^n−1]: 4·10^5 random configs
  (n ≤ 5), zero violations. The **case a=1 cascade** (top fragment + top intact deleted,
  parities preserved, recurse to G-L1(n−1)) is rigorous and correct.
- **Fragment-count bound** N_F(2^{n−j}) ≤ 2^j−1: correct (m·2^{n−j} < 2^n ⟹ m < 2^j).
- **Interleaving value = 2^n**: correct (fragments at odd ranks, intacts at even ranks).
- **Rank-swap Lemma S** ΔO = (−1)^{r+1}(y−x): correct; establishes interleaving is a LOCAL min
  only — the builder does not overclaim it as global.
- **Base cases.** n=1 both bounds: correct (upper: L > 2/3 ⟹ halve ⟹ O = 1−L/2 < 2/3). n=2
  confined lower bound: I brute-forced min O = 4.0 (units, target 4). ✓

## Open gaps — honestly flagged, NOT overclaimed
- **L1** (confined lower bound): reduced by the cascade to case a=0 (all fragments ≤ 2^{n−1});
  Lemma S gives only local minimality; global-min / clustering step OPEN. Correctly flagged.
- **L2** (confine XY's optimum to R_n): exchange mechanism stated, numerics only, no rigorous
  re-optimisation comparison. OPEN. Correctly flagged.
- **U1 = Case B** (all LB pieces > 1/D): B0 (n=1) vacuous ✓, B1 with a_1 > 1/2 and a_1 ≤ c(n)
  closed by Lemma I ✓; B1 with a_1 > c(n) and B2 (a_1 ≤ 1/2) OPEN. This is the field-wide wall.
  Correctly flagged; U1 is genuinely NOT closed.

The Assembly (§8) correctly states the proof establishes the bounds only "in the cases proved"
and lists the open gaps. No case is silently skipped; no gap is presented as established.

## Scores
- Correctness: 9.5/10 — every written step I checked is valid; Lemma H independently reproduced.
- Completeness/rigor: 5/10 — three real gaps (L1 case a=0, L2, U1=Case B) block `solved`.
- Progress vs prior best: strong — Lemma H closes Case A of the upper bound for ALL n, the
  first fully-general slice of the previously monolithic field-wide wall; plus certified
  fragment-count bound, interleaving value, Lemma S, and the a=1 cascade.

## Actions taken
- Certified and wrote **Lemma H** to `results/imo-2026-03/lemmas/H-halve-largest.md`.
- Rewrote `results/imo-2026-03/current.md` (Status partial; round-3 progress; removed stale
  circular ‡ from Current best; recorded Lemma H closing Case A).
- Recorded outcome: `advanced` (elo 1531 → 1558.3).

## Gap the next builder must close (for CHANGES REQUESTED routing)
1. **U1 = Case B** (highest priority, field-wide wall): explicit XY strategy with O ≤ c(n) for
   every LB config with all pieces > 1/D — specifically B2 (a_1 ≤ 1/2, no dominant piece) and
   B1 with a_1 > c(n). The reviewer-suggested route: mixed halvings + one asymmetric cut giving
   odd-layer measure ≤ 1/D (Lemma R target μ{N odd} ≤ 1/D), with a rigorous ≤ n mark budget.
2. **L1 case a=0**: promote Lemma S local-min to a global min / bound fragment clustering per
   dyadic gap using the count bound; the naive per-rank bound r_{2j} ≤ 2^{n−j} is FALSE
   (recorded — do not retry term-by-term).
3. **L2**: rigorous exchange confining XY's optimum to R_n.

---
**Verdict: CHANGES REQUESTED (Status: partial).**
**Goal Progress:** direct-constructive advanced (elo 1531→1558, live). Lemma H certified —
Case A of the XY upper bound now CLOSED for all n (first general slice of the field-wide wall).
Overall Status stays `partial`; open: L1 (case a=0), L2, U1=Case B (B1-large, B2).
