# Build report — direct-constructive (imo-2026-03), Round 6

Status: **partial** (advanced). No Spec concern — the plan works as set up, and in fact the
lower-bound closure is CLEANER than planned (the flagged "flat-move face" issue is fully eliminated
for the confined case, not merely tamed).

## What I closed this round

### LOWER bound — confined case FULLY closed (§4.2.7)
Replaced the round-5 refuted "receiver always exists" with the **dyadic two-case split**, and
closed the flat-move termination with an explicit well-foundedness weight. At the compact minimiser
v of A over the a=0 region R (max fragment w_1 ∈ (0, 2^{n-1}]):
- **Case 1 (w_1 ≤ 2^{n-2}):** v_2 = 2^{n-2}, so A ≥ v_1 − v_2 = 2^{n-1} − 2^{n-2} = 2^{n-2} ≥ 1.
  Direct, no receiver/donor. **Both round-5 counterexamples ({2,10/3,10/3,11/3,11/3},
  {2,7/2,7/2,7/2,7/2}) land here** (max frag 11/3, 7/2 ≤ 4 = 2^{n-2}), where A ≥ 4 = 5.
- **Boundary (w_1 = 2^{n-1}):** a=1 closure (cascade §4.2.4) + continuity ⇒ A ≥ 1.
- **Case 2 (2^{n-2} < w_1 < 2^{n-1}):** w_1 is a NAMED receiver, G(w_1) = 1 by piece-counting (only
  the intact 2^{n-1} is above it) — not an existence claim. Minimality of v forces
  A′₊(e_{w_1}−e_b) = −1 + (−1)^{Geq(b)} ≥ 0 ⇒ **Geq(b) even for every positive fragment b (no
  donor)** — this holds at tie-laden vertices, unlike the round-5 generic-density argument. Then:
  - N_tot = n+m odd ⇒ smallest fragment can't be the global min (would be a donor) ⇒ all fragments
    > 1 ⇒ intact 1 at bottom odd rank ⇒ A = A′ + 1 ≥ 1;
  - N_tot even, f_min > 1 ⇒ ruled out (flat-then-descent-past-intact-wall contradiction, or a=1);
  - N_tot even, f_min ≤ 1 ⇒ **flat move** e_{w_1}−e_{f_min} (A′₊ = 0) drives m ↦ m−1, flipping
    N_tot to odd — well-founded (m = #{positive fragments} strictly decreases, floor 2 = a=1
    boundary). The round-5 "degenerate flat-move face" loose end is **GONE**.

Verified: 0 failures (A ≥ 1) over 2·10^5+ random+clustered a=0 configs each n = 3,4,5,6.

### UPPER bound — IH(4) closed (§6.2)
Restated as **pure conditional lemmas** (no empirical %, per round-5 certification rule):
- **IH-reducible:** hard regime + S − max(b_1,2b_2) < (2^{q−1}−1)/D ⇒ one pair-cancel cut drops to
  a valid IH(q−1) instance (A preserved via certified Lemma X).
- **IH4-flat (NEW):** q=4 + S − max(b_1,2b_2) ≥ 7/D ⇒ b_2 < 4/D; 3-cut strategy gives A < 1/D
  (two exhaustive sub-cases b_2 ≶ b_3+b_4). Verified 0 fails, maxA < 0.99·(1/D), n=3,4,5.
- **IH(4) unconditional** = IH-reducible ∪ IH4-flat (complementary, exhaustive) ↦ IH(3) (proved).
  Case-B hard regime now closed **through q = 4**.

## Certification proposals (for the reviewer)
1. Dyadic two-case split + no-donor closer (confined a=0 lower bound). REPLACES the refuted round-5
   Descent/receiver-existence lemmas — those should be de-certified/marked refuted.
2. IH-reducible (pure conditional).
3. IH4-flat (pure conditional).

## Honestly still open
- **L2 (lower):** XY spending cuts OUTSIDE R_n (fragmenting an intact R_j). §4.4 reduces it to the
  same simplex but the exchange step (stray cut can't beat the confined optimum) is unwritten. This
  is the sole remaining lower-bound residual; the CONFINED case is fully closed.
- **Upper general n:** IH(q ≥ 5) flat residual + sub-case B2. Handed to sibling
  upper-general-cascade (did NOT duplicate).

## Note for orchestrator
The lower bound is now much closer to solved than the outline anticipated: the confined case has NO
loose end (the flat-move well-foundedness is written). Next round should route a builder at **L2**
(the exchange/confinement argument) to finish the lower bound entirely.

Proof written to results/imo-2026-03/approaches/direct-constructive.md (Status: partial)
