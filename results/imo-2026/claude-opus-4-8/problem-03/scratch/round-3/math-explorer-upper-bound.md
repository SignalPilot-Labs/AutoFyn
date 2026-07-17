## imo-2026-03 — Upper Bound (U1) Terrain Report

### Problem and Setup

c(n) = 2^n / D, D = 2^{n+1}−1. By Lemma R2 (certified), O ≤ c(n) ⟺ μ{N(t) odd} ≤ 1/D. After LB's n marks create pieces a_1 ≥ … ≥ a_{n+1} (at most n+1 pieces, sum = 1), XY places n more cuts. U1: prove XY can always achieve O ≤ c(n).

The current approach (direct-constructive) uses "interleave+halve": if a_1 > 1/2 use Lemma I (n cuts in a_1 → O = a_1), if a_1 > c(n) halve first. Budget accounting fails when halvings and interleaving are both required. This is the field-wide wall.

---

### Distinct Opening A — N(t) Parity Surgery (explicit, computable)

**Mechanism.** Each cut of piece L into {L_min, L_max} (L_min ≤ L_max) changes μ{N odd} by the exact formula:

Δμ{N odd} = (μ{[0,L_min): N even} − μ{[0,L_min): N odd}) + (μ{[L_max,L): N even} − μ{[L_max,L): N odd})

This gives +L_min (worst: both target intervals entirely "wrong" parity) to −2·L_min (best: both entirely "right" parity).

**Verified for geometric LB n=2 (D=7):** ANY cut of the 4/7-piece reduces μ{N odd} by exactly 2/7 regardless of cut location, because the N(t) structure of the geometric config has the special "canceling-parity" property in both affected intervals. Proved directly: for cut 4/7 → {L_min, L_max}, the [0,L_min) interval has equal even/odd sub-measure (cancels to 0 net) and the [L_max, 4/7) interval is entirely odd (contributes −2/7). Verified for n=3 as well: cuts of 8/15-piece at alpha ≠ 0.1, 0.9 all give Δ = −2/15 = −2/D.

**Sanity (n=1):** LB pieces {a_1, a_2} with a_1 > 2/3. N_LB odd region = (a_2, a_1). XY halves a_1: Δμ = (2a_2 − a_1/2) + (−a_1/2) = 2 − 3a_1 < 0 for a_1 > 2/3. New μ = (2a_1−1) − (3a_1−2) = 1−a_1 ≤ 1/3 = 1/D. ✓

**Where it breaks for U1:** For general LB configs, Δμ per cut is NOT always −2/D; it depends on what N(t) looks like in the affected intervals. A budgeted lower bound on the cumulative Δ is needed. No clean per-cut bound exists for arbitrary configs.

**Assessment:** Most promising for the geometric LB config (where each cut of the top piece gives −2/D exactly), giving a direct proof of one specific direction. For the upper bound on ALL LB configs, requires coupling with a structural argument.

---

### Distinct Opening B — "Halve-n-Largest" Strategy + Clean Formula (NEW, NOT in current approach)

**Strategy:** XY halves each of the n largest LB pieces once (n cuts total), leaving the smallest piece a_{n+1} intact.

**Theorem (proved computationally to machine precision for n=1,2,3,4, with clean proof):**  
For any sorted LB pieces a_1 ≥ … ≥ a_{n+1} with sum 1, the "halve n largest" strategy produces 2n+1 pieces with:

**O = 1/2 + a_{n+1}/2**

*Proof:* The 2n+1 pieces are {a_1/2, a_1/2, a_2/2, a_2/2, …, a_n/2, a_n/2, a_{n+1}}. The n pairs (a_i/2, a_i/2) contribute 0 to the alternating sum (each pair's contribution is a_i/2 − a_i/2 = 0). The singleton a_{n+1} sits at rank 2k+1 (ODD) in the sorted order, where k = #{i : a_i/2 ≥ a_{n+1}} counts the pairs above it. (Exactly 2k items precede a_{n+1} in sorted order.) So the alternating sum A = a_{n+1}, and O = (1+A)/2 = 1/2 + a_{n+1}/2. ∎

**Corollary (immediate):** O ≤ c(n) ⟺ a_{n+1} ≤ 1/D.

**CASE A resolved:** If a_{n+1} ≤ 1/D: "halve n largest" gives O = 1/2 + a_{n+1}/2 ≤ c(n). This is a COMPLETE PROOF for Case A. Equality holds at the geometric LB config (a_{n+1} = 1/D).

**CASE B (a_{n+1} > 1/D, the remaining gap):** "Halve n largest" gives O = 1/2 + a_{n+1}/2 > c(n). This accounts for ≈30–50% of random LB configs (numerically). A different XY strategy is needed. Note: in Case B, ALL n+1 pieces are > 1/D (since the smallest is). For n=1: Case B means a_2 > 1/3, but then a_1 ≤ 2/3 = c(1), so O_initial ≤ c(1) and XY doesn't cut at all. ✓ For n ≥ 2 in Case B: more work needed.

**Key structural fact for Case B:** All pieces > 1/D and sum = 1, so a_1 ≤ 1 − n/D = (D−n)/D. For n=1: a_1 ≤ c(1) (no cuts needed). For n=2: a_1 ≤ 5/7; since c(2)=4/7, a_1 can exceed c(n). For n ≥ 2: Case B requires active cutting.

**Case B strategy candidates (explored numerically, all work):**
- Equal-piece config {1/(n+1), …}: XY puts n cuts in ONE piece to make n+1 fragments with one ≈ 0. O ≈ 1/2 < c(n). ✓
- {3/7, 2/7, 2/7} (n=2 Case B): ONE cut of a_1=3/7 in half → {3/14,3/14,2/7,2/7}; O=2/7+3/14=7/14=1/2 < 4/7. ✓
- General Case B: numerical search confirms XY always achieves O ≤ c(n) (0/100 failures in greedy search for n=3).

**Assessment:** Case A is completely proved. Case B is unresolved but heavily constrained: must find a Case B strategy that handles all configs with a_{n+1} > 1/D.

---

### Distinct Opening C — Geometric Config as Minimax Saddle Point (Schur-type argument)

**Observation:** For the geometric LB config, Lemma I (all n cuts in the top piece) gives O = a_1 = c(n) exactly. For any other LB config, numerical evidence shows XY_min < c(n) strictly.

**Claim (unproved, but testable):** XY_min(a_1,…,a_{n+1}) is maximized over all sorted piece configs with sum 1 at the geometric distribution. Equivalently, the geometric config majorizes all others in the "hardest for XY" sense.

**Why plausible:** The geometric config has a_1 = c(n) = max possible a_1 for which Lemma I gives O exactly c(n). Any other config with a_1 < c(n) allows XY to achieve O = a_1 < c(n) via Lemma I. Configs with a_1 > c(n) let XY use halvings to reduce O below c(n). The geometric config sits at the exact balance point a_1 = c(n) where Lemma I is tight.

**Sanity check n=2:**
- Geometric {4/7,2/7,1/7}: XY_min = 4/7. ✓
- Equal {1/3,1/3,1/3}: XY_min ≈ 1/2 < 4/7. ✓
- Extreme {0.9,0.05,0.05}: XY_min ≈ 1/2 < 4/7. ✓
- Near-geometric {0.543,0.265,0.134,0.058} (n=3): XY_min = 0.529 < 8/15. ✓

**Approach:** Prove Schur-concavity — perturbing LB pieces toward equality (reducing the Schur-dominance of the config) can only decrease XY_min. Combined with the fact that among all n+1-piece configs with sum 1, the geometric config uniquely satisfies both a_1 = c(n) and a_1 > Σ_{i≥2} a_i (Lemma I applicable with equality), it would follow that all other configs give XY_min ≤ c(n).

**Where it breaks:** Proving Schur-concavity of XY_min requires showing that "equalizing two pieces" cannot increase the minimax, which is a nontrivial monotonicity claim about the optimization.

---

### Distinct Opening D — Parity-Neutral Two-Case Proof

Combines Openings B and C into a direct two-case proof:

**CASE A (a_{n+1} ≤ 1/D):** "Halve n largest" → O = 1/2 + a_{n+1}/2 ≤ c(n). Complete.

**CASE B (a_{n+1} > 1/D, i.e., all pieces > 1/D):**  
Sub-case B1 (a_1 > 1/2, a_1 > c(n)): exists only for n ≥ 2. In this sub-case, bound a_1 ≤ (D−n)/D. Try "one cut of a_1 to halve, then apply Case A to the resulting n+2-piece config with n−1 cuts." After halving a_1: new smallest piece among the resulting 4 pieces is a_{n+1} > 1/D still. Problem: one halving doesn't escape Case B.

Sub-case B2 (a_1 ≤ 1/2): all pieces ≤ 1/2. Lemma I inapplicable. Key: all pieces are in (1/D, 1/2]. With n cuts in a_1 creating n+1 fragments {s_1,…,s_{n+1}}: choose s_1 ≈ a_2, s_2 ≈ a_3, …, s_n ≈ a_{n+1}, s_{n+1} ≈ 0. The fragments interleave with a_2,…,a_{n+1}, forcing them to even ranks. O = sum of fragments = a_1 ≤ c(n)?? Only if a_1 ≤ c(n). But in Case B2, a_1 > 1/D and could be ≤ or > c(n).

**Identified gap:** Case B requires a strategy that works when the smallest piece is "too large." This is genuine and unresolved.

---

### Distinct Opening E — Continuous Exchange / Balancing

**Framing:** Think of N(t) as a histogram to be "balanced." XY's goal: make N(t) even except on measure ≤ 1/D. Each cut is a "redistribution" that shifts mass from level t=L (high) to level t=L_min (low). The target: distribute mass so each level has even N.

**Elegant version of the halving observation:** After halving all n largest pieces, each "stack" at threshold t gets 1 extra unit from both halves of each cut piece (for t < L_min). The net effect: N(t) becomes even in almost all regions. The only "odd" region is the thin layer around a_{n+1} (the uncut piece). This gives μ{N odd} = a_{n+1} (matching the formula O = 1/2 + a_{n+1}/2, since A = a_{n+1}).

**Extension idea:** After one halving of a_{n+1} (Case B), the uncut piece contributes μ{N odd} = a_{n+1}/2 which might be ≤ 1/D if a_{n+1} ≤ 2/D. But a_{n+1} could be > 2/D. Multiple halvings of a_{n+1} alone don't help because each creates a pair (a_{n+1}/2^k, a_{n+1}/2^k) at even ranks and the next smallest piece becomes the "odd singleton."

**Sanity check (n=1):** LB has 2 pieces {a_1 ≥ 1/2, a_2 = 1−a_1}. XY halves a_1 → {a_1/2, a_1/2, a_2}. Singleton is a_2 at odd rank 3. O = a_1/2 + a_2 = 1−a_1/2 ≤ c(1) = 2/3 iff a_1 ≥ 2/3. For a_1 ∈ [1/2,2/3): O_initial = a_1 ≤ 2/3 = c(1) already. ✓ No cut needed. This shows the two cases match perfectly for n=1.

---

### Candidate Technique(s)

Primary: **Invariants + Monovariants** (track μ{N odd} per cut, the halving formula O = 1/2 + a_{n+1}/2 is the key invariant). Secondary: **Schur-convexity/majorization** (to argue geometric config is hardest). Tertiary: **Double counting / layer-cake** (Lemma R2, already proved, underpins everything).

---

### Cheap-Kill Candidates

For U1 in particular:

1. **Halve-n-largest + Case A:** O = 1/2 + a_{n+1}/2 ≤ c(n) when a_{n+1} ≤ 1/D. This is a CHEAP KILL for roughly 50–70% of LB configs. Proves a substantial portion of U1 completely.

2. **n=1 Case B reduction to free win:** For n=1 and any LB config (p ≤ 2 pieces), if a_2 > 1/3 = 1/D then a_1 ≤ 2/3 = c(1), so O_initial ≤ c(1) with 0 cuts. Case B for n=1 is vacuous.

3. **Lemma I for Case A with a_1 ≤ c(n) and a_1 > 1/2:** Lemma I already in the approach file — XY's n cuts in a_1 give O = a_1 ≤ c(n). This handles the sub-case within Case A where a_1 > 1/2.

---

### Knowledge-Base Entries to Use

- **Invariants & monovariants** (Combinatorics section): the halving formula O = 1/2 + a_{n+1}/2 is a monovariant for XY's strategy.
- **Extremal principle** (Combinatorics): the geometric config as extremal LB config (Schur-concavity direction).
- **Pigeonhole / size bounds** (General): in Case B, all n+1 pieces > 1/D implies a_1 ≤ (D−n)/D.
- **Induction (General Proof Methods):** Case A is n=1 base + Case A induction. Case B for n=1 is trivial.

---

### Analogous Past Problems (Cruxes)

1. **aimo-0117 (dyadic game):** "Assign played values as a two-sided geometric sequence so the largest strictly exceeds all others." Crux: maintaining the invariant "largest power of two is in the black box." ANALOGOUS because: LB's geometric construction is exactly a dyadic sequence where the largest piece strictly dominates all others. XY's response (Lemma I) mirrors Jesse's "defer commitment until the opponent's move" strategy. Adaptable: the "interleave fragments" is Jesse's "play next dyadic power into the freed slot."

2. **aimo-0262 (Cinderella, capacity game):** "Hand the defender a self-reproducing invariant family." Crux: Cinderella maintains "two adjacent buckets empty, flanking ≤ 1, last ≤ 1." ANALOGOUS because: XY needs a similar self-reproducing invariant on the piece config (O ≤ c(n)) that survives LB's arbitrary marking. The "two disjoint sub-collections average below threshold" technique (used to find which pair Cinderella empties) is analogous to the Case A/B split on a_{n+1}.

3. **aimo-0019 (covering game, dyadic intervals):** "Bound cumulative resource by a constant times progress via a linear potential." Crux: "B keeps invariant (i): ink spent on [0,x_r] is at most 3x_r." ANALOGOUS because: XY's mark budget accounting for U1 is exactly a "linear potential bounds cumulative resource" argument — each XY mark must simultaneously handle multiple "odd" regions of N(t), analogous to covering dyadic intervals.

---

### Prior Progress

All from direct-constructive approach:
- Fully proved: G1 (greedy = odd-ranked), R1/R2 (odd-sum rewritings, μ{N odd} equivalence), LB geometric construction + dominance identity, Easy lower-bound case (XY spares R_n), Lemma I (interleaving), base cases n=1,2 (both bounds), identity (‡) localizing L1.
- Open: L1 (confined-case Fragments Lemma), L2 (confine-to-R_n reduction), U1 (XY upper bound for all LB configs and all n).

---

### Dead Ends (Do Not Retry)

- **Induction n → n−1 via game separation:** REFUTED in Round 2. The recursion c(n) = 2c(n−1)/(2c(n−1)+1) is a NUMBER COINCIDENCE, not a game decomposition. XY's mark budget doesn't decrement to n−1, and the odd-sum is global.
- **"Halve repeatedly until a_1 ≤ c(n), then interleave":** Budget fails for large n. After h halvings of a_1 (using h marks), the resulting 2^h copies plus p−1 others exceed n+1 total pieces; Lemma I no longer applies (a_1/2^h ≤ sum of rest for h ≥ 1 when a_1 ≤ 1).
- **Per-rank bound r_{2j} ≤ 2^{n−j}:** Explicitly false (counterexample n=3, fragments {3,2.5,2.5} give r_4 = 2.5 > 2).
- **"Halve n largest" strategy for Case B:** Gives O = 1/2 + a_{n+1}/2 > c(n) when a_{n+1} > 1/D. Fails roughly 30–50% of the time. Need different strategy for Case B.

---

### Small-Case / Intuition Notes

1. **Formula O = 1/2 + a_{n+1}/2 is exact** (machine precision, 100% confirmed n=1,2,3,4). This is the MOST IMPORTANT NEW FACT: it reduces Case A of U1 to the single condition a_{n+1} ≤ 1/D.

2. **Geometric LB is the unique hardest config for XY** (conjecture, confirmed numerically n=1,2,3): For all non-geometric LB configs, XY_min < c(n) strictly. The geometric config is the minimax saddle point.

3. **Case B is "nearly trivial" for small n but hard for large n** (conjecture): For n=1, Case B never binds (any LB config in Case B has O_initial ≤ c(1) already). For n=2, Case B configs (all 3 pieces > 1/7) have a_1 ≤ 5/7 and ONE halving of a_1 brings it to ≤ 5/14 < 4/7 = c(2) (actually: 5/14 < 4/7 iff 5 < 8 ✓), then if a_2 ≤ 1/7 the new config is in Case A. If a_2 > 1/7: second cut needed.

4. **"Put all cuts in ONE piece" gives O = a_j** (Lemma I, confirmed): For any piece a_j with a_j > Σ_{i≠j} a_i, XY's n cuts all in a_j give O = a_j. This handles the "dominant piece ≤ c(n)" case cleanly. The geometric config is the tightest such case.

5. **XY's optimal strategy distributes cuts across multiple pieces in Case B** (confirmed n=3): For configs like {0.375,0.357,0.219,0.049}, XY halves each of the 3 large pieces separately (not all cuts in one piece) achieving O ≈ 0.508 < c(3). The "distribute cuts" strategy is NOT captured by any single lemma currently.

---

### Summary for the Outliner

The MOST PROMISING new direction for U1 is:

**Two-case proof using the halving formula:**

- **Case A (a_{n+1} ≤ 1/D):** FULLY PROVED via the new Lemma H (halving formula O = 1/2 + a_{n+1}/2 with singleton-at-odd-rank argument).
- **Case B (a_{n+1} > 1/D):** Needs a new idea. The best current candidate: show that in Case B, XY can achieve O ≤ c(n) by using the n cuts non-uniformly (some on the large pieces, some to create a "tiny" piece that acts as the singleton).

The key GAP for Case B: find an explicit strategy (not just numerical confirmation) that handles all configs with all pieces > 1/D. The "halve-all approach" fails; a MIXED strategy (some halvings, one asymmetric cut to create a tiny fragment) likely works but needs budget accounting.

The Case A proof (O = 1/2 + a_{n+1}/2) is the major new contribution and should be added to the approach file as a proved sub-lemma immediately.
