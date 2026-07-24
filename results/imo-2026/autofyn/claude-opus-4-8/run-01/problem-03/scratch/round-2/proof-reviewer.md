# Proof-reviewer — imo-2026-03, round 2

Problem: IMO 2026 P3 (Chu–Han war stick game). Intended answer c(n) = 2^n/(2^{n+1}−1).
Independently confirmed by grid minimax: n=1 → 2/3, n=2 → 4/7 (both match). Answer is correct.

---

## Approach: direct-constructive — Verdict: CHANGES REQUESTED (Status: partial)

Scores: Correctness 9/10 · Completeness/rigor 6/10 · Progress high.

**What I independently verified (all hold):**
- **Lemma G1 (greedy = odd-ranked)** — load-bearing reduction. Re-derived the difference-game
  recursion V(q) = max_j[q_j − V(q∖q_j)] and the telescoping identity
  f(j)−f(j+1) = (q_j−q_{j+1})(1+(−1)^{j+1}) ≥ 0 from scratch, and brute-forced V(q) against
  the exact minimax for 2000 random multisets: V(q) = A(q) and first-player total = odd-sum,
  to 1e-9. **Correct and rigorous.** Certified to `lemmas/G1-greedy-odd-ranked.md`.
- **Lemmas R1/R2 (odd-sum rewritings)** — O = ∫⌈N/2⌉dt and O = 1/2 + (1/2)μ{N odd}. Verified
  numerically (3000 configs, 1e-9). **Correct.** Certified to `lemmas/R-oddsum-rewritings.md`.
- **Construction + dominance identity, easy lower-bound case (§4.1), Lemma I (§5) in its
  stated regime, base cases n=1 (both directions) and n=2 (lower confined + construction)** —
  all checked and rigorous. The identity (‡) E − ΣI = ∫⌊(N_F−N_I)/2⌋dt was independently
  verified (2000 confined-case configs).

**Real gaps that block `solved` (builder's Status `partial` is correct — not overclaimed):**
- **L1** — the confined-case Fragments Lemma (∫⌊(N_F−N_I)/2⌋dt ≤ 0 for all n and all ≤ n+1
  fragments summing to 2^n). Only n=1,2 done; general n is asserted "numerically" (n≤5), not
  proved. This is a genuine open step, not hand-waving disguised.
- **L2** — the reduction "XY's optimum confines all cuts to R_n" is stated as "expected but
  not written" (exchange argument). Open.
- **U1** — the entire XY upper bound for general n (interleave+halve mark-budget accounting).
  Proven only for n=1; for n≥2 the strategy is described but the budget bookkeeping and the
  a_1 ≤ 1/2 regime are unproved. This is the field-wide wall.

Note: §4.2 leans on "numerical minimax shows XY confines cuts to R_n" and §6/§7 lean on
"verified numerically for n≤5" — these are correctly flagged as gaps L1/L2/U1, not passed off
as proof. No overclaim: no gapped step is marked PROVED. The approach is right and has
substantial, correct, reusable progress → CHANGES REQUESTED; attack L1 (cleanest, now a 1-D
integral inequality) and U1.

Recorded: `advanced` — G1/R1-R2/construction/easy-case/base cases closed; L1,L2,U1 open.

---

## Approach: induction-recursion — Verdict: RETHINK (Status: unsolved via this route)

Scores: Correctness 8/10 (of what's written) · Completeness/rigor 3/10 (engine dead) · Progress low-medium.

**Engine (H2 game separation) is genuinely refuted — RETHINK is warranted.** I confirmed both
defects the builder reports:
- **F1 (budget non-decrement)** — real. The (n−1) induction hypothesis assumes ≤ n−1 XY marks
  on the remainder R, but XY may legally place all n marks in R. The IH cannot be invoked. The
  claimed tempting fact c(n−1)·|R| = c(n) is arithmetically true but does not license the step.
- **F2 (global re-ranking)** — real. Verified the n=3 optimal XY response (bisect 8/15→4,4 and
  cut 4/15→3,1, sorted {4,4,3,2,1,1}/15, OddSum = 8/15 = c(3)): sub-pieces from both sides of
  any boundary interleave in the sorted order, so the odd-sum is a global functional and there
  is no rank-invariant boundary yielding an independent (n−1)-subgame.
The separation is a numerical coincidence, not a decomposition. Skeleton Steps 2–4 rest on it
and cannot be written. The approach as set up (induction on n via big-piece separation) cannot
work → back to the outliner for a different mechanism (e.g. a monovariant on the merged sorted
list, or a fundamentally different upper-bound framing).

**Correct salvage (both subsumed by direct-constructive, so not independent progress):**
- Step 1 (recursion ⇔ closed form): r(n)=1/c(n)=2−2^{−n} ⟹ c(n)=2^n/(2^{n+1}−1). Correct.
- AltSum reformulation: OddSum = (1+AltSum)/2 — this IS Lemma R2 (A = alternating sum). Correct
  but redundant with the certified R1/R2; not promoted separately.

The builder's approach-file Status `partial` is defensible on the salvaged lemmas, but for
routing the approach's own engine is dead, so the correct verdict is RETHINK. I marked the
ranker outcome `dead-end` accordingly.

Recorded: `dead-end` — H2 separation refuted (F1,F2); Step 1 + AltSum salvaged but engine broken.

---

## Field status written to current.md
Status: partial. Current best = direct-constructive's verified chain (G1 reduction, R1/R2
measure rewritings, construction+dominance, easy case, Lemma I, base cases, identity ‡).
Answer c(n)=2^n/(2^{n+1}−1) stated and verified. Certified shared lemmas: G1, R1/R2.
Open hard core: L1, L2, U1 (U1 the field-wide wall).
