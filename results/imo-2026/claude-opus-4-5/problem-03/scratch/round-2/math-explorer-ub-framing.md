## imo-2026-03 (Upper Bound — Alternative Framings)

**Lens:** Game-theoretic framings: minimax game trees, recursive structure, alternating-sum potential, duality.

---

### Status of prior work

Both `geometric-dominance.md` and `induction-on-n.md` have `Status: solved` in their approach files, but `current.md` correctly says `partial`. The upper-bound sections in both files are incomplete/wrong:

- The `induction-on-n.md` file itself computes (lines 296–486) that the "copy strategy" (XY halves the n largest pieces) gives LB **5/8 > 4/7 = c(2)** for LB marking {1/4, 1/4, 1/2} — directly showing the copy strategy is NOT universally XY-optimal. The file then argues XY should instead put both marks inside the 1/2 piece, but this contradicts the "copy strategy is optimal for all LB markings" claim it invokes.
- The `geometric-dominance.md` upper bound says "copy strategy is XY-optimal against geometric marking; any other LB response does worse" but never proves geometric marking is optimal for LB — that's exactly what the upper bound requires.

The self-defeating nature of these proofs is confirmed numerically: LB marking {1/3, 1/3, 1/3} with XY placing marks at (3/20, 3/10) limits LB to 31/60 ≈ 0.517 < 4/7, and separately the geometric marking (1/7, 3/7) achieves a guarantee of exactly 4/7 under XY's best response. The geometric marking IS optimal for LB (numerically confirmed to high precision), but this requires proof.

---

### Key diagnostic: what XY's optimal response actually looks like

For LB marking {1/5, 2/5, 2/5} (equal-top pieces), XY's optimal 2-mark response (found numerically) is to place BOTH marks inside the SMALLEST piece {1/5}, at positions 0.005 and 0.1. This:
- Leaves the two large {2/5} pieces completely untouched.
- Splits {1/5} into {0.005, 0.095, 0.1}.
- Final sorted pieces: {2/5, 2/5, 1/10, 0.095, 0.005}. LB gets 2/5 + 1/10 + 0.005 = 0.505 < 4/7.

This is the exact OPPOSITE of the "halve n largest" strategy. XY creates "noise" at the bottom that forces LB to take small pieces at odd positions. This means the upper bound proof must handle strategies very different from the copy/halve approach.

---

### Alternative framings for the upper bound

**Framing 1 (alternating-sum reduction).**

Define A = alternating sum of sorted final pieces. LB's share = (1+A)/2. So LB ≤ c(n) iff A ≤ 2c(n)−1 = t_n = 1/(2^{n+1}−1). The upper bound reduces to: for any LB n-piece marking, XY can place n marks to achieve A ≤ t_n. This is the cleanest formulation.

**Framing 2 (clean n=1 upper bound via case-split — PROVED).**

For n=1 with LB pieces {a_1 ≤ a_2}, a_1+a_2=1, XY has 1 mark:

- **Case a_1 < 1/3 (ratio a_2/a_1 > 2):** XY halves a_2. Pieces: {a_2/2, a_2/2, a_1}. Since a_2 ≥ 2a_1, we have a_2/2 ≥ a_1, so sorted {a_2/2, a_2/2, a_1}. A = a_1 < 1/3 = t_1. ✓

- **Case a_1 ≥ 1/3 (ratio a_2/a_1 ≤ 2):** XY marks inside a_2 creating {a_1, a_2−a_1}. Since a_1 ≥ 1/3, a_2−a_1 = 1−2a_1 ≤ 1/3 ≤ a_1, so sorted {a_1, a_1, a_2−a_1}. A = 1−2a_1 ≤ 1/3. ✓

Both cases give A ≤ 1/3 = t_1, with equality iff a_1 = 1/3, i.e., a_2/a_1 = 2 (the geometric ratio). This is a COMPLETE, RIGOROUS proof of the n=1 upper bound. The key: two strategies (halve if ratio > 2, clone the smaller piece if ratio ≤ 2). Also handles m=1 (LB uses 0 marks): XY halves to get A=0 < t_1.

**Framing 3 (inductive case-split extending n=1 — CONJECTURE, promising).**

For n≥2 with {a_1 ≤ ... ≤ a_{n+1}}:

XY's first mark decision is based on the ratio a_{n+1}/a_n:
- If a_{n+1}/a_n > 2: halve a_{n+1}. New pieces include {a_{n+1}/2, a_{n+1}/2}. The pair contributes 0 to A. Remaining pieces for n−1 more XY marks.
- If a_{n+1}/a_n ≤ 2: clone a_n inside a_{n+1} (mark at distance a_n from one end, creating {a_n, a_{n+1}−a_n}). New pieces include a_n appearing twice. Again a pair contributes 0 to A.

After the first mark, the residual problem has n−1 XY marks and up to n+2 pieces. The hope is that the residual A satisfies a recursive bound A ≤ t_{n−1}·something that implies A ≤ t_n overall.

Concrete proposal: prove the STRONGER claim that for any m ≤ n+1 pieces summing to σ, XY with n marks achieves A ≤ σ·t_n. This is scale-invariant and might admit cleaner induction.

**Framing 4 (exchange/variational — geometric is extremal).**

The geometric marking uniquely achieves min_X A = t_n with equality. For any other marking, XY can achieve A < t_n. Proof route: exchange argument showing if any adjacent ratio a_{k+1}/a_k ≠ 2, one can modify the LB marking towards geometric while only decreasing min_X A (equivalently, XY gets a strictly better response). The geometric configuration is then the unique maximizer of min_X A over all LB markings, and it equals t_n. This avoids constructing explicit XY strategies.

**Framing 5 (minimax theorem shortcut).**

The game G(L,X) has compact strategy spaces (marks are points in [0,1], continuous payoff function after small perturbations to resolve ties). By minimax theorem (or by the theorem on combinatorial games), V = max_L min_X G = min_X max_L G. The lower bound proves V ≥ c(n). An upper bound can be obtained from the dual: show there exists XY's strategy profile X* such that max_L G(L, X*) ≤ c(n). The challenge: X* must depend on L (it's adaptive), so this reduces to the constructive problem anyway. But the minimax theorem GUARANTEES X* exists; the proof needs only to exhibit it or argue from its properties.

---

### Dead ends (do not retry)

- **"Copy strategy is XY-optimal for all LB markings."** FALSE. Disproved by {1/4, 1/4, 1/2} example (copy strategy gives LB 5/8 > 4/7). The copy strategy is only optimal against the geometric marking specifically.
- **"Halving n largest pieces always works."** FALSE for same reason.
- **"Saddle-point condition (geometric, copy) proven directly."** The lower half is proved (geometric marking guarantees c(n) against all XY). The upper half (copy strategy limits all LB markings to c(n)) is FALSE — copy strategy is not XY-universal.

---

### Prior progress

The approach files' upper bound sections are incomplete. The TRUE state:
- **Lower bound:** Complete and rigorous (geometric marking analysis, all XY cases).
- **n=1 upper bound:** Provable cleanly via case-split (Framing 2 above).
- **n≥2 upper bound:** Open. The inductive extension of Framing 2 is the most promising route.

---

### Candidate techniques

- **Induction loading / strengthening the hypothesis** (KB: "Generalize — stronger statement easier to prove"): Prove A ≤ σ·t_n for any m ≤ n+1 pieces summing to σ.
- **Case-split on ratio a_{n+1}/a_n**: two strategies (halve if > 2, clone if ≤ 2), both cases of Framing 2.
- **Extremal principle**: Pin down why geometric maximizes LB's guarantee.

---

### Knowledge-base entries

- "Generalize / induction loading" (under combinatorics/induction section) — strengthen the hypothesis to m pieces summing to σ.
- "Pigeonhole / extremal principle" — for exchange argument showing geometric is extremal.

---

### Analogous past problems

No crux-corpus entries inspected (time constraint), but the structure of Framing 2 (ratio-split case analysis) is analogous to problems where the optimal strategy switches based on a threshold.

---

### Small-case / intuition notes

- **Conjecture:** XY's optimal strategy for general n is the recursive case-split from Framing 3: look at the ratio a_{n+1}/a_n and either halve or clone, then recurse. This exactly mirrors the n=1 proof.
- **Extremal observation (conjecture):** The geometric marking uniquely satisfies a_{k+1}/a_k = 2 for all k, placing it at the BOUNDARY between "halve" and "clone" strategies for every pair. This makes it hardest for XY: XY must use exactly 1 mark per piece at the threshold, achieving A = t_n exactly.
- Numerically verified (n=2, N=200 grid): geometric marking (1/7, 3/7) gives LB exactly 4/7 under XY's best response; no other LB marking does better.
- The n=1 case-split proof is complete and rigorous — it's a solid base case for induction. The outliner should build on this.

---

### Distinct openings

1. **Complete n=1 proof + induct**: Extend the clean n=1 case-split proof inductively. The inductive step: given {a_1,...,a_{n+1}}, XY applies one "ratio-based" split reducing to the n−1 problem. Needs a careful inductive hypothesis (possibly the σ·t_n version).

2. **Exchange/variational proof**: Show by an exchange argument that the geometric marking is the unique LB-optimal marking. Formalize: if any ratio a_{k+1}/a_k ≠ 2, LB can be modified to decrease its guarantee, contradicting optimality. The geometric marking then gives exactly c(n), establishing the upper bound.

3. **Minimax theorem route**: Invoke the theorem to guarantee V ≤ c(n) follows from V = c(n) (value exists + lower bound = c(n)). Then the upper bound is "free" given that the value equals the lower bound. To close this, show the game's value function is continuous and the lower bound is tight via compactness. This avoids constructing XY's strategy explicitly.
