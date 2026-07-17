## Status
partial

## Approaches tried
- **upper-vertex-reduction** (NEW, round 7) — LIVE (CHANGES REQUESTED). Genuinely different upper
  framing: recast the whole Case-B hard-regime IH(q) (all q, incl. IH(q≥5)) as max over the compact
  polytope K_q of f(b) = min-over-≤q−1-cuts A. Proved rigorously and CERTIFIED this round:
  **Lemma f-continuous-attained** (§A, Berge + Weierstrass: f continuous, min attained ⟹ achievability),
  and **Lemma VertexFace** (§B: every vertex of K_q lies on a gap-face or bottom-face; certified
  Reduction 2 / Lemma H give f(v) ≤ 1/D at every vertex — reviewer re-verified the polytope combinatorics
  AND enumerated all vertices q=2..5, 0 off-face). §C tightness f(geometric)=1/D confirmed. Net: **IH(q)
  for all q ⟸ (V): f attains its max on K_q at a vertex.** (V) is HONESTLY OPEN (not smuggled): the
  marginal-PL principle is false without joint convexity, and A = min-over-strategies is non-convex, so
  the lower-bound vertex spine does NOT transfer. Reduction is valid; (V) is the sole gap. No overclaim.
- **caseB-matching** — DEAD-END as framed (RETHINK, round 4). Its distinctive mechanism, the
  finite **matching menu** (each LB piece cut ≤ once: "cut larger at smaller" + halve + keep,
  "Lemma M" claiming the best menu forces A ≤ 1/D), is **REFUTED**: reviewer-verified exact
  n=3 counterexample a=(5144,2787,1386,683)/10000 (all pieces and all consecutive gaps > 1/15)
  where every menu strategy gives A ≥ 683/10000 > 1/15 but a fragment cascade gives 288/10000 ≤ 1/15.
  So the menu is the wrong strategy class; the hard regime needs fragment (cascade) cuts, which is
  direct-constructive's Lemma I route — this approach collapses onto the same U1 wall. SALVAGED and
  now **certified**: Lemma X (XOR/parity evaluator + cut toggle), Reduction 1 (halve-all ⟹ Case B
  reduces to p=n+1), Reduction 2 (close consecutive gap d*≤1/D ⟹ A=d*≤1/D). These reduce the
  Case-B upper bound to the single **hard regime** (p=n+1, all pieces AND all consecutive gaps
  > 1/D) for all n. Files: `lemmas/X-xor-evaluator.md`, `lemmas/CaseB-reductions.md`.
- **direct-constructive** — LIVE (CHANGES REQUESTED, round 4). Explicit optimal strategies
  both sides. Fully proven and reviewer-verified: reduction to the odd-sum marking game via
  Lemma G1; odd-sum rewritings R (turning both bounds into measure statements
  μ{N odd} vs 1/D); the LB geometric construction + dominance identity; the easy lower-bound
  case (XY spares R_n); interleaving Lemma I (in its regime); base cases n=1 (both bounds)
  and n=2 (lower confined + construction). NEW (round 3, certified): **Lemma H** — XY halves
  the p−1 largest LB pieces and spares a_p ⟹ O = 1/2 + a_p/2, so a_p ≤ 1/D ⟹ O ≤ c(n),
  **closing Case A of the upper bound for all n** (rigorous pair-cancellation + odd-rank
  singleton, continuity extension; machine-verified). Also certified: fragment-count bound
  N_F(2^{n−j}) ≤ 2^j−1, exact interleaving value = 2^n, rank-swap Lemma S (interleaving is a
  local min), top-fragment cascade (case a=1 of G-L1). Gaps remain: **L1** confined-case
  lower bound, case a=0 only (global-min / clustering step); **L2** confine-to-R_n exchange;
  **U1 = Case B** upper bound for LB configs with all pieces > 1/D (B1 with a_1 > c(n), and
  B2 with a_1 ≤ 1/2). The old circular integral reduction ‡ is DROPPED (it is identically
  2^n − O, a rename not a reduction) and is NOT load-bearing.
- **upper-general-cascade** — LIVE (CHANGES REQUESTED, round 6/7). Copy-of direct-constructive that
  owns the general-n Case-B hard-regime upper bound. Round 6: proved **IH-reducible** and **IH4-flat**
  as pure conditionals (certified), giving **IH(q) for all q ≤ 4** (Theorem UB) — Case-B B1-large
  upper bound for n ≤ 4. Round 7: corrected the flagged **arithmetic overclaim** — the double-cancel
  IH(n−1) threshold is **3·2^{n−2}/D**, not 2^{n−1}/D (off by 3/2; geometric config sits exactly on
  the corrected threshold), and the double-cancel move needs the extra hypothesis a_1−a_2 ≥ a_3 — both
  now stated (reviewer-verified the algebra). PROVED and CERTIFIED **Lemma GreedyCascade** (dominant
  piece b_1 ≥ 1/2 ⟹ XY cascade forces A = 2b_1 − 1; b_1 ≤ c(n) ⟹ A ≤ 1/D), **closing B2-large
  (1/2 ≤ a_1 ≤ c(n)) for ALL n** with an explicit closed-form n-cut strategy (not a q-induction; immune
  to the r6 fixed-point obstruction). Residual honestly reduced to **B2-small (a_1 < 1/2)**, the adaptive
  fragment-cascade wall = same wall as the IH(q≥5) flat residual. Honestly **refuted** IH+(m) dual-bound
  (r6). Correctly partial; no overclaim.
- **induction-recursion** — DEAD-END engine (RETHINK, round 2). The n→(n−1) game separation
  (H2: isolate P_0, recurse on remainder) is refuted: (F1) XY's mark budget never decrements
  from n to n−1, so the (n−1) induction hypothesis is inapplicable; (F2) the odd-sum is a
  global functional of the merged sorted list with cross-boundary interleaving, so no
  independent (n−1)-subgame exists. Salvaged (both subsumed elsewhere): Step 1
  recursion⇔closed-form; AltSum reformulation (= R2). The induction-via-separation mechanism
  must be re-planned by the outliner.

## Current best
The answer is **c(n) = 2^n/(2^{n+1} − 1)** (write D = 2^{n+1} − 1), independently confirmed
by grid minimax at n=1 (2/3) and n=2 (4/7). The furthest rigorous progress (from
direct-constructive, reviewer-verified):

1. **Reduction to the odd-sum marking game (Lemma G1, certified).** In the alternating
   claim-to-maximise game, the first player collects exactly the odd-ranked pieces; greedy is
   optimal for both. So c(n) = max over LB's ≤ n marks of min over XY's ≤ n marks of the
   odd-sum O.
2. **Odd-sum rewritings (Lemmas R1/R2, certified).** O = ∫⌈N(t)/2⌉dt and
   O = 1/2 + (1/2)μ{N(t) odd}; hence O ≥ 2^n/D ⟺ μ{N odd} ≥ 1/D and O ≤ 2^n/D ⟺ μ{N odd} ≤ 1/D.
3. **LB construction + dominance identity.** LB marks x_k = (2^k−1)/D giving pieces
   P_j = 2^j/D; each P_j exceeds the sum of all strictly smaller LB pieces by exactly 1/D.
4. **Easy lower-bound case.** If XY places no cut in the largest LB piece R_n, then r_1 = 2^n/D
   and O ≥ 2^n/D.
5. **Interleaving Lemma I.** If a piece b exceeds the sum of the rest and the residual fits,
   its owner can, with p−1 cuts, force the odd-claimer to receive exactly b.
6. **Base cases** n=1 (both bounds fully) and n=2 (lower confined + construction).
7. **Lemma H (certified round 3).** XY halving the p−1 largest LB pieces and sparing a_p gives
   O = 1/2 + a_p/2; hence a_p ≤ 1/D ⟹ O ≤ c(n). This CLOSES Case A of the XY upper bound for
   all n (the first fully general slice of the field-wide upper-bound wall).

8. **Round-4 lower-bound reduction (direct-constructive, reviewer-verified).** The spare-R_n case
   now holds for EVERY XY placement (unique-max argument, certified as the Spare-R_n lemma). The
   confined lower bound A ≥ 1 is recast as minimising the continuous piecewise-affine A = μ{N odd}
   over the compact simplex Δ = {Σg_i = 2^n, g_i ≥ 0} of ≤ n+1 fragments; the min is attained at a
   vertex of the hyperplane-arrangement cell complex, so the lower bound is EQUIVALENT to the vertex
   inequality **(★): A(vertex) ≥ 1**. Closed within (★): the interleaving cell (A ≡ 1) and all a=1
   vertices (top-fragment cascade). L1 and L2 now merge into this single (★). Residual: a=0
   *clustered* vertices only.
9. **Round-4 upper-bound (direct-constructive + caseB-matching, reviewer-verified).** IH(1),IH(2),
   IH(3) of the B1-large pair-creation sub-game proved (residual singleton < 1/D from the sum bound;
   doubly-hard leaf machine-checked, 0 fails). Case-B **Reductions 1 & 2** (certified from
   caseB-matching) reduce Case B to the hard regime p=n+1, all pieces AND all gaps > 1/D.

Certified shared lemmas live in `lemmas/` (G1, R, H, **X**, **CaseB-reductions** incl. Spare-R_n,
round-6: **DyadicLower-confined**, **IH-reducible**, **IH4-flat**, and round-7: **GreedyCascade**
(B2-large closed all n), **VertexFace** (every K_q vertex ≤ 1/D), **f-continuous-attained** (Berge
achievability)).
The old integral identity ‡ is DROPPED: it equals 2^n − O identically (a rename, not a reduction).

**Open (field-wide hard core, after round 7):** **L2-a0** — the lower bound when XY spends cuts
*outside* R_n, now reduced to the single **augmented a = 0 closer** (§4.4; the CONFINED lower bound
A ≥ 1 is CLOSED, `lemmas/DyadicLower-confined.md`, and every other stray branch is closed by the
GDL(n) induction skeleton); **U1** = the single adaptive fragment-cascade wall shared by two faces:
the **IH(q≥5) flat residual** of B1-large AND **B2-small (a_1 < 1/2)**. Now CLOSED on the upper side:
Case A (Lemma H); easy Case-B sub-cases (Reductions 1–2); hard regime **through q = 4** (IH-reducible +
IH4-flat); and **B2-large 1/2 ≤ a_1 ≤ c(n) for ALL n** (`lemmas/GreedyCascade.md`, round 7). The whole
upper bound also REDUCES to the single statement **(V)** (upper-vertex-reduction: every vertex of K_q
is ≤ 1/D via `lemmas/VertexFace.md`; only vertex-attainment of the max is open). The dual-bound IH+(m)
route is refuted (fixed-point obstruction).

**Round-6 reviewer finding (confined lower bound NOW CLOSED; IH(4) closed; both approaches partial).**
Reviewer independently re-derived and verified the new work:

- **LOWER — confined case FULLY CLOSED (§4.2.7), replacing the refuted round-5 receiver-existence.**
  The round-5 "a receiver always exists" claim (rejected: FALSE at a=0 clustered configs, e.g. n=4
  frags {2,10/3,10/3,11/3,11/3}) is replaced by the **dyadic two-case split** on the max fragment w_1
  vs 2^{n−2}. Case 1 (w_1 ≤ 2^{n−2}): A ≥ 2^{n−1}−2^{n−2} = 2^{n−2} ≥ 1 directly — and *both* round-5
  counterexamples land here (A=5), so no receiver is asserted at clustered points. Case 2
  (2^{n−2}<w_1<2^{n−1}): w_1 is a **named receiver by counting** (G(w_1)=1, valid at ties — the fix);
  minimality forces no positive donor, then N_tot parity + a strictly-decreasing flat-move weight
  close it. Reviewer verified: the directional-derivative formula A′₊(e_a−e_b)=(−1)^{G}+(−1)^{Geq}
  holds even at tie-laden multisets (5·10^4 exact checks); min_Δ A = 1, 0 fails over 2·10^5 random +
  clustered a=0 configs n=3,4,5; each of (2a)/(2b)/(2c) exhaustive and closed. **CERTIFIED**:
  `lemmas/DyadicLower-confined.md`. The old Descent/receiver-existence lemmas are **REFUTED** (never
  entered `lemmas/`; DyadicLower is the corrected replacement). Remaining lower-bound gap: **L2** (XY
  cuts *outside* R_n) — §4.4 reduced but the exchange step is unwritten; honestly still open.

- **UPPER — IH(4) closed; IH-reducible and IH4-flat now PURE conditionals.** Reviewer re-derived both:
  **IH-reducible** (S−max(b_1,2b_2)<(2^{q−1}−1)/D ⟹ one cut to a valid IH(q−1) instance) — verified the
  reduced active sum equals min(S−b_1,S−2b_2) and lands below the exact IH(q−1) boundary; the reduced
  instance needs no gap condition (IH(q−1) is gap-free), so the gap-preservation worry is moot.
  **IH4-flat** (S−max ≥ 7/D ⟹ b_2<4/D, 3-cut → A<1/D, two sign sub-cases) — both sub-cases and the
  δ-choice re-derived correct. Full IH(4) closure (reducible ∪ flat, exhaustive) verified 0 fails,
  worst A·D ≤ 1 over 8·10^4 exact configs at D=15,31,63,127. **CERTIFIED**: `lemmas/IH-reducible.md`,
  `lemmas/IH4-flat.md`. Both carry **no empirical percentage** (fixes the round-5 rejection). Case-B
  hard-regime upper bound now closed **through q = 4** (n ≤ 4, B1-large).

- **upper-general-cascade honestly refuted the outline's IH+(m) dual-bound route** (fixed-point
  obstruction: any pair-cancel move on a flat residual leaves active sum ≥ (2^{q−1}−1)/D, at/above the
  IH(q−1) boundary; the geometric config is a fixed point of halve-max, A=1/D throughout). Reviewer
  confirms this refutation is sound. IH(q ≥ 5) flat residual + B2 remain the genuine open core; status
  correctly **partial** (not overclaimed).

**Round-7 reviewer findings (3 approaches, all CHANGES REQUESTED; 3 lemmas certified).**

- **upper-vertex-reduction (NEW) — VertexFace + f-continuous-attained CERTIFIED; (V) open.** Reviewer
  independently re-derived the polytope combinatorics (a vertex of the q-dim K_q has ≥ q of q+1
  constraints active ⟹ ≤ 1 inactive ⟹ some gap or bottom active) and exact-enumerated all vertices for
  q = 2..5 (0 off-face). Both face bounds (Reduction 2 on gap-face, Lemma H on bottom-face) are correct
  imports. §A Berge/Weierstrass achievability is standard and correct (the position domain is a nested
  region, not a literal product — noted in the lemma, does not affect the conclusion). The reduction
  IH(q) ⟸ (V) is VALID and (V) is honestly open — the marginal-PL principle genuinely fails (A non-convex),
  so it is not smuggled. Real, promotable structural progress even with (V) open.

- **upper-general-cascade — arithmetic overclaim CONFIRMED and CORRECTED; GreedyCascade CERTIFIED.**
  Reviewer re-derived the threshold: 1 − 2(a_2+a_3) < (2^{n−1}−1)/D ⟺ a_2+a_3 > 3·2^{n−2}/D — the old
  2^{n−1}/D was too small by 3/2 (an overclaim, now fixed; geometric config sits exactly on the corrected
  threshold, a_2+a_3 = 3·2^{n−2}/D). GreedyCascade re-derived by hand (legality r_j ≥ b_{j+1} from
  b_1 ≥ 1/2 ≥ b_2+…+b_{j+1}; final multiset pairs each b_j twice ⟹ XOR-cancels ⟹ A = 2b_1 − 1) and
  machine-checked (0 fails / 3000 exact configs). Closes B2-large for all n. The claim "near-equality
  does NOT force a gap ≤ 1/D" is correct (hard-regime gaps are > 1/D by hypothesis; closers use genuine
  fragment cuts). Residual honestly = B2-small (a_1 < 1/2).

- **direct-constructive — L2 reduced, NOT closed; single residual honestly flagged.** Reviewer verified
  the reformulation (†) A = D − 2E ⟺ E ≤ ΣG = 2^n − 1 (correct algebra), the augmented vertex reduction,
  and the closed branches (a=1 R_{n−1}-uncut cascade→GDL(n−1); v_1=2^{n−1},v_2≤2^{n−2} top-gap; Count
  Lemma gives A > 0 only, NOT A ≥ 1 — correctly not overclaimed). The **augmented a = 0 closer** (donors
  restricted to a fixed-sum cut-group; bottom piece a tiny stray sub-piece rather than the intact 1) is
  genuinely open and load-bearing — honestly flagged, not hidden. GDL(n) skeleton references this open
  residual, so it is NOT certified as a closed lemma (kept in the approach file per the round-4 rule).

**Round-8 reviewer findings (both approaches CHANGES REQUESTED / partial; 5 lemmas certified).**

- **upper-vertex-reduction — statement (V) REPLACED by a certified spine; flat residual shrunk, not
  closed.** Reviewer independently re-derived and verified: **f-homogeneous** (f(λb)=λf(b) on the
  positive cone — scale-free (pattern, fraction) parametrisation scales every final part, hence A, by λ),
  **σ-migration** (max_{K_q} f = max_Φ f — rescale any Σ<S point up by S/Σ>1: gaps and floor scale UP
  staying ≥1/D, and f≥0 with c>1 gives f weakly larger; VALIDLY bypasses the false marginal-PL route to
  (V), with no vertex/PL/convexity), and **TwoLevelCascade** (c1: b_1≥S/2 ⟹ A=2b_1−S≤1/D generalized
  GreedyCascade; c2a: b_1<S/2, b_2≥(S−b_1)/2 ⟹ [halve b_1; greedy b_2] A=2b_2−(S−b_1)≤1/D — threshold
  algebra machine-verified). σ-face tiers (a),(b) → certified IH-reducible. **CERTIFIED**:
  `lemmas/f-homogeneous.md`, `lemmas/sigma-migration.md`, `lemmas/TwoLevelCascade.md`. **HONEST GAP
  (confirmed, not overclaimed):** the flat residual sub-slice **c2b = {b_1<S/2 AND b_2<(S−b_1)/2}, q≥5**
  is OPEN. The builder's correction is CORRECT: c1 and c2a are each only ~1/(2D)-wide slivers, so c2b is
  the BULK of the flat residual, not a thin remainder. The naive 3-level cascade provably overshoots
  (2b_3−s_3 unbounded, b_3 has no dyadic cap); the true optimum is adaptive with no closed form
  (min-A ≈ 0.16–0.47 ≪ 1, so a strategy exists but is unproven). Real structural advance; (V) killed.

- **direct-constructive — a=0 closer sharpened by an intrinsic parity reformulation; two clean bypasses
  proven but both FAIL at the true minimiser (honest).** Reviewer independently verified (0 failures over
  thousands of random arrangements n=3,4,5): the reformulation **(‡) A ≥ 1 ⟺ E_F ≤ O_G** (from
  E − ΣG = E_F − O_G, tie-break independent, ΣG = (D−1)/2); **all-F-odd sufficiency** E_F=0 ⟹ A≥1; and
  the **injection/majorisation lemma** N_F ≤ N_G+1 ⟹ A ≥ 1 (layer-cake ⌊N/2⌋ ≤ N_G ⟹ E ≤ ΣG). The
  minimiser receiver-move (D) closes the pure T−β-odd anchor (certified DyadicLower derivative).
  **CERTIFIED**: `lemmas/EF-OG-reformulation.md`, `lemmas/injection-majorisation.md`. **HONEST FINDING
  (confirmed, not overclaimed):** exact search shows the true minimiser has **E_F > 0 with E_F ≈ O_G
  tight**, so bypasses (B),(C) FAIL there and (D)'s receiver move is tie-blocked (increasable fragment
  tied to the G-piece directly above). The residual is the confined-style within-group flat move on the
  tight face **E_F = O_G** — NOT discharged. Sole remaining lower-bound gap.

**Field-wide open core after round 8.**
- **LOWER:** confined case CLOSED (DyadicLower-confined). L2 stray a=0 reduced to the **within-group
  flat-move on the tight face E_F = O_G** (E_F > 0 minimiser); the two majorisation bypasses provably do
  NOT reach it. PLATEAUED — next round needs the tight-face flat-move monovariant (import certified
  confined (2c) termination weight), or a genuinely different a=0 framing.
- **UPPER:** IH(q) for all q reduced — with NO vertex/PL/convexity (σ-migration) — to the single flat
  residual slice **c2b (q ≥ 5)** = both top pieces non-dominant. Closed through q=4 (IH4-flat), B2-large
  all n (GreedyCascade), tiers (a)(b) and slivers c1/c2a (TwoLevelCascade). c2b is the adaptive
  fragment-cascade crux; greedy cascades provably top out at two levels. Needs a different framing
  (global potential / matching) for the both-non-dominant flat case.

## Full proof
Not present — Status is partial (gaps: LOWER = within-group flat move on the tight face E_F = O_G;
UPPER = flat-residual slice c2b {b_1<S/2, b_2<(S−b_1)/2}, q≥5. Everything else on both bounds is closed
and certified).
