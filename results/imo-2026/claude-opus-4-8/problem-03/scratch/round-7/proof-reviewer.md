# Proof-reviewer — round 7 (imo-2026-03, IMO 2026 P3)

Three approaches reviewed independently. All three builders honestly reported `partial`; none claimed
`solved`. I independently re-derived the load-bearing step of each certification candidate. Verdict:
**CHANGES REQUESTED × 3**. Three lemmas CERTIFIED. Status stays **partial**.

---

## 1. upper-vertex-reduction (NEW) — Verdict: CHANGES REQUESTED. Status: partial.

Framing: recast Case-B hard-regime IH(q) (all q) as max over compact polytope K_q of
f(b) = min-over-≤q−1-cuts A. Reduces IH(q) for all q to a single statement (V): f attains its max on
K_q at a vertex.

**Load-bearing check — VertexFace (§B): VALID.** I re-derived the polytope combinatorics from scratch:
K_q ⊂ ℝ^q is q-dimensional, cut by q+1 constraints (q−1 gaps, bottom β, sum σ); a vertex has ≥ q
independent active constraints ⟹ ≤ 1 inactive ⟹ some gap or β active. If neither gap nor β active,
only σ could be active (≤ 1 < q), contradiction. Independently exact-enumerated all vertices for
q = 2,3,4,5: 3/4/5/6 vertices, **0 off-face**. On a gap-face certified Reduction 2 gives A = d* ≤ 1/D;
on the bottom-face certified Lemma H gives A = a_p = 1/D. Both imports apply (q = n+1 pieces, q−1 = n
cuts, all pieces positive/strictly-decreasing). So f(v) ≤ 1/D at every vertex — rigorous.

**§A f-continuous-attained: VALID.** Berge Maximum Theorem + Weierstrass over finitely many cut
patterns. The builder's phrase "product of simplices" is loose (the position domain is a nested region
because later cut bounds depend on earlier positions), but the domain is compact and continuously
varying, so Berge/Weierstrass still give continuity + attainment. Conclusion correct.

**(V) honestly OPEN, not smuggled.** The reduction IH(q) ⟸ (V) is genuinely valid (f(v) ≤ 1/D at all
vertices + max-at-vertex ⟹ f ≤ 1/D). (V) requires f piecewise-linear; the builder correctly refutes the
outline's "marginal of a PL function is PL" (false without joint convexity; A = min-over-strategies is
non-convex, so the lower-bound DyadicLower vertex spine does NOT transfer). No overclaim — this is real,
promotable structural progress. **CERTIFIED: VertexFace, f-continuous-attained.**

Scores — Correctness 9/10, Completeness 5/10 (V open), Progress 7/10 (whole upper bound reduced to one
convex-analytic statement; every vertex disposed of).

## 2. upper-general-cascade — Verdict: CHANGES REQUESTED. Status: partial.

**Arithmetic overclaim CONFIRMED and CORRECTED.** I re-derived: 1 − 2(a_2+a_3) < (2^{n−1}−1)/D ⟺
a_2+a_3 > (2^{n+1}−2^{n−1})/(2D) = 3·2^{n−2}/D. The old threshold 2^{n−1}/D was too small by a factor
3/2 — a genuine overclaim, now fixed. Geometric config a_2+a_3 = 2^{n−1}/D + 2^{n−2}/D = 3·2^{n−2}/D
sits exactly on the corrected threshold (non-strict/boundary), so the double-cancel entry covers strictly
less than claimed. The extra hypothesis a_1−a_2 ≥ a_3 (to place the 2nd cut) is now stated. Correct.

**GreedyCascade: VALID.** I re-derived the cascade by hand and simulated it (XOR evaluation, 3000 exact
configs n=2..7, b_1 ≥ 1/2): A = 2b_1 − 1, **0 failures**. Legality r_j = b_1 − (b_2+…+b_j) ≥ b_{j+1}
follows from b_1 ≥ 1/2 ≥ 1−b_1 = b_2+…+b_p ≥ b_2+…+b_{j+1}. Final multiset pairs each b_j (j≥2) twice
(intact + fragment) ⟹ XOR-cancels ⟹ only [0, 2b_1−1] survives ⟹ A = 2b_1 − 1. With b_1 ≤ c(n),
A ≤ 2c(n)−1 = 1/D (verified 2c(n)−1 = 1/D for n=2..6). **Closes B2-large (1/2 ≤ a_1 ≤ c(n)) for ALL n**
with an explicit closed-form n-cut strategy — not a q-induction, immune to the r6 fixed-point obstruction.
Boundary b_1 = 1/2 handled (A = 0, one fewer cut). **CERTIFIED: GreedyCascade.**

**Residual honest.** B2-small (a_1 < 1/2) genuinely open (GreedyCascade's domination fails). The claim
"near-equality does NOT force a gap ≤ 1/D" is correct: hard-regime gaps are > 1/D by hypothesis, and the
closers use genuine fragment cuts (not whole-piece cancellation), so it does not reduce to Reduction 2.

Scores — Correctness 9/10 (overclaim now fixed), Completeness 6/10 (B2-small open), Progress 7/10
(B2-large closed for all n — first uniform slice of B2).

## 3. direct-constructive (L2) — Verdict: CHANGES REQUESTED. Status: partial.

**L2 reduced, NOT closed — honestly flagged.** I verified the reformulation (†): A = D − 2E and
O + E = D give A ≥ 1 ⟺ E ≤ (D−1)/2 = 2^n − 1 = ΣG (correct algebra). The augmented vertex reduction
(min of PL A over product-of-simplices at an arrangement vertex) is sound. Closed branches verified:
a=1 R_{n−1}-uncut cascade → GDL(n−1); v_1=2^{n−1}, v_2≤2^{n−2} top-gap A ≥ 2^{n−2} ≥ 1. The Count Lemma
correctly yields only A > 0 (at least one non-R_n piece at an odd rank when s ≥ 1), and the builder
explicitly does NOT overclaim A ≥ 1 from it.

**Residual load-bearing and honest.** The augmented a = 0 closer (donors restricted to a fixed-sum
cut-group; bottom piece a tiny stray sub-piece rather than the intact 1 contributing +1) is genuinely
open. Not hidden. The GDL(n) skeleton references this open residual, so per the round-4 rule it is NOT
certified as a closed lemma — it stays in the approach file.

Scores — Correctness 9/10, Completeness 4/10 (a=0 closer open, same clustering/parity wall as confined
a=0), Progress 6/10 (stray regime reduced to one residual; every other branch closed).

---

## Certification actions

CERTIFIED (written to `results/imo-2026-03/lemmas/`):
- **GreedyCascade.md** — b_1 ≥ 1/2 ⟹ A = 2b_1 − 1; closes B2-large all n. Pure conditional, no %.
- **VertexFace.md** — every vertex of K_q on a gap/bottom face ⟹ f(v) ≤ 1/D. Closed conditional-free
  fact; caveat that (V) is separate/open written into the file so IH(q) cannot be misread out of it.
- **f-continuous-attained.md** — Berge achievability of the strategy value.

NOT certified: GDL(n) reduction skeleton, Count Lemma, reformulation (†) — GDL references the open a=0
residual (round-4 rule: no reduction-to-open-gap as a closed lemma); (†)/Count kept in the approach file
(marginal standalone value, framing-specific).

## Goal Progress (ranking / status deltas)

- Status: **partial** (unchanged; no slug solved). No overclaim survived review.
- Ranking (advanced × 3): direct-constructive 1683, upper-general-cascade 1686, upper-vertex-reduction
  1642 (NEW, registered live). caseB-matching 1511 / induction-recursion 1331 (dead), potential-duality
  1419 (parked).
- Net progress: +3 certified lemmas (running total 11). Upper bound now closed on Case A, easy Case-B
  (Red 1–2), hard regime through q=4, AND B2-large all n (GreedyCascade); whole upper bound also reduced
  to single (V) via VertexFace. Lower bound: L2 reduced to single augmented a=0 closer.
- Two open cores remain: (upper) the adaptive fragment-cascade wall = IH(q≥5) flat residual / B2-small
  a_1<1/2 / the open (V) — the same wall from three angles; (lower) the augmented a=0 closer (3rd round
  on a=0 — shared-gap-plateau flag stands).
- Diversity: upper-vertex-reduction is the genuinely-different global-max reframe answering the round-6
  flag, but its novelty (V) is unproven. If neither (V) nor the a=0 closer nor B2-small moves next round,
  escalate for a new framing on the surviving wall.
