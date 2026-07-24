# Proof-reviewer — round 8 — imo-2026-03 (IMO 2026 P3)

Two approaches reviewed independently. Both are honest partials with rigorous new lemmas; neither
overclaims. Answer c(n) = 2^n/(2^{n+1}−1) unchanged and already established. Five new lemmas certified.

---

## Slug 1: upper-vertex-reduction

**Verdict: CHANGES REQUESTED. Status: partial (matches builder's recorded Status — correct).**

Scores — Correctness 10/10; Completeness/rigor 7/10 (one clean open slice); Progress 8/10 (killed the
round-7 open (V) with a certified spine, closed two new slivers).

### Load-bearing steps re-derived independently

1. **f-homogeneous (§B) — VALID.** The (cut-pattern, fractional-position ρ∈(0,1)) parametrisation is
   scale-free; a fraction-ρ cut sends x→(ρx,(1−ρ)x) and λx→λ(ρx,(1−ρ)x), so by induction every final
   part on λb is λ× the part on b. A depends only on the length multiset (Lemma X) and
   ⊕[0,λ·part] = λ·⊕[0,part], so A scales by λ; min over the common strategy set scales by λ. Correct.

2. **σ-migration (§C) — VALID; validly replaces (V).** For any K_q point with Σ=s<S, rescale by c=S/s>1:
   gaps c(b_i−b_{i+1}) ≥ c/D > 1/D, floor c·b_q > 1/D, sum = S — so b'∈Φ. f(b')=c·f(b) ≥ f(b) since
   f≥0 (A is a measure) and c>1. Hence max_{K_q} f = max_Φ f. Uses only 1-homogeneity + monotone
   rescaling — NO vertex-attainment, NO PL, NO convexity. This genuinely bypasses the false
   "marginal-of-PL-is-PL" trap that blocked (V). Real advance.

3. **TwoLevelCascade (§E1–E2) — VALID.** Re-derived by hand and machine-checked the thresholds:
   (S+1/D)/2 = 2^{q-1}/D and the c2a bound 2·2^{q-2}/D − S + 2^{q-1}/D = 1/D (both exact, verified in
   `python3`). c1 = generalized GreedyCascade (mass S): legality b_1≥S/2≥b_2+…+b_{j+1}, survivor
   2b_1−S ≤ 1/D. c2a = [halve b_1 (cancels); greedy b_2 over {b_3..b_q}]: legality b_2≥s'/2, survivor
   2b_2−(S−b_1) ≤ 1/D via b_2≤2^{q-2}/D, b_1≤2^{q-1}/D. XOR pair-cancellation (Lemma X) holds regardless
   of length coincidences (grouping equal pairs is valid). Both correct, q−1 cuts each.

### Honest gap verified (not overclaimed)

The sole open slice **c2b = {b_1 < S/2 AND b_2 < (S−b_1)/2}, q ≥ 5** is correctly flagged OPEN. The
builder's correction that **c2b is the BULK of the flat residual** (c1 and c2a are each ~1/(2D)-wide
slivers, since c1 needs b_1∈[S/2,(S+1/D)/2]) is CORRECT — I confirmed the window width. The 3-level
cascade provably overshoots (2b_3−s_3 has no dyadic cap). This is not near-closed; it is the genuine
adaptive-cascade crux, cleanly isolated. Nothing overclaimed; §E3 is candidly labelled OPEN.

### Certified this round: f-homogeneous, σ-migration, TwoLevelCascade

All three are self-contained proven facts (no reference to an open gap in their statements), pass the
full bar. Files written to `lemmas/`. VertexFace/f-continuous-attained unchanged (already certified r7).

### Next-round target
Close c2b (q≥5, both top pieces non-dominant) via a framing OTHER than greedy cascade (provably tops
out at 2 levels) — e.g. a global potential or matching argument on the σ-face flat interior.

---

## Slug 2: direct-constructive

**Verdict: CHANGES REQUESTED. Status: partial (matches builder's recorded Status — correct).**

Scores — Correctness 10/10; Completeness/rigor 7/10 (one open flat-move); Progress 7/10 (intrinsic
reformulation + two clean closers, plus a decisive refutation sharpening the residual).

### Load-bearing steps re-derived independently

1. **(‡) A ≥ 1 ⟺ E_F ≤ O_G (§4.4.5A) — VALID.** ΣG = O_G+E_G ⟹ E−ΣG = E_F−O_G (tie-break independent).
   ΣG = 2^n−1 = (D−1)/2, and A = D−2E, so A ≥ 1 ⟺ E ≤ (D−1)/2 = ΣG ⟺ E_F ≤ O_G. Machine-verified over
   ~9000 random sorted arrangements (n=3,4,5): A = D−2E, E−ΣG = E_F−O_G, and the equivalence all hold
   with 0 failures. Correct.

2. **All-F-odd sufficiency (B) — VALID.** E_F=0 ⟹ E_F ≤ O_G ⟹ A ≥ 1; then A = 1+2O_G. Immediate.

3. **Injection/majorisation (C) — VALID.** N_F ≤ N_G+1 ⟹ N ≤ 2N_G+1 ⟹ ⌊N/2⌋ ≤ N_G ⟹ (Lemma R)
   E = ∫⌊N/2⌋ ≤ ∫N_G = ΣG ⟹ A = D−2E ≥ D−2ΣG = 1. Clean layer-cake bound. Correct.

4. **Anchor branch (D) — VALID (uses certified DyadicLower derivative).** If smallest fragment b_0 has
   Geq odd then every fragment is at an odd rank ⟹ E_F=0 ⟹ A≥1 by (B). Closes T−β odd (in particular
   the pure-T-odd β=0 anchor). Relies on certified machinery; correctly a partial branch, not promoted.

### Honest finding verified (not overclaimed)

The builder's decisive finding — **the true minimiser has E_F > 0 with E_F ≈ O_G tight** — is correctly
reported. Consequently bypasses (B) all-F-odd and (C) N_F≤N_G+1 provably FAIL at the minimiser (F is
clustered), and (D)'s receiver move is tie-blocked. The residual correctly reduces to the confined-style
**within-group flat move on the tight face E_F = O_G**, NOT discharged. No overclaim; the Count-Lemma
"A>0 not A≥1" caveat from r7 is respected. This is a genuine sharpening (identifies exactly where the
minimiser sits and rules out the two tempting shortcuts), not a closure.

### Certified this round: EF-OG-reformulation (‡), injection-majorisation

Both self-contained, no open-gap reference. Files written to `lemmas/`. The anchor branch (D) and the
minimiser analysis remain in the approach file (reference the open residual, per the round-4 rule).

### Next-round target
The within-group flat-move monovariant on the tight face E_F = O_G — import the certified confined (2c)
termination weight and adapt the bottom-piece (tiny stray sub-piece) handling. Plateaued 3+ rounds;
consider a genuinely different a=0 framing per the shared-gap rule.

---

## Field-wide status
Status stays **partial**. Both bounds are reduced to a single clean open slice each:
- LOWER: within-group flat move on the tight face E_F = O_G (E_F>0 minimiser).
- UPPER: flat-residual slice c2b = {b_1<S/2, b_2<(S−b_1)/2}, q≥5 (both top pieces non-dominant).
Everything else on both bounds is closed and certified. 5 lemmas certified this round
(f-homogeneous, σ-migration, TwoLevelCascade, EF-OG-reformulation, injection-majorisation).
