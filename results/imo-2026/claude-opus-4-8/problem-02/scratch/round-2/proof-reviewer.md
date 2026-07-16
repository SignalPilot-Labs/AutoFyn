# Proof-reviewer — imo-2026-02 (IMO 2026 P2), Round 2

Two approaches built this round. Verdicts are independent.

---

## Approach 1 — `complex-reality-conditions`

**Builder claimed: solved. Reviewer verdict: CHANGES REQUESTED. True Status: partial (closest — one non-degeneracy step from complete).**

### What I verified (all pass)

**§3 — the geometry→algebra translation (the round-1 gap) is now genuinely rigorous.** I re-derived every step independently:
- **Signed-area / side-of-line dictionary (SIDE).** WLOG CCW (`Im(b̄c)>0`) via the reflection `z↦z̄`; correct. `z` on `C`-side of `AB ⟺ Im(b̄z)>0`, `z` on `B`-side of `AC ⟺ Im(c̄z)<0` — both correct (they are `2[A,B,z]`, `2[A,C,z]` with the reference vertices `C`, `B`).
- **Interior facts (K1) `Im(b̄k)>0`, (L1) `Im(c̄l)<0`, (L2) `Im(b̄l)>0`.** Each is a correct one-line consequence of "interior of the named triangle" (edge on line `AB`/`AC`, opposite vertex fixes the side; (L2) via both `N`,`C` strictly on the `C`-side and a convex-combination argument). Correct.
- **Lemma 2 (reality hinge).** Airtight: both directed angles in `(0,π)` ⟹ each equals its unsigned value ⟹ `θ₁=θ₂` as reals; `arg(z₁/z₂) ≡ θ₁−θ₂ (mod 2π)` with `θ₁−θ₂∈(−π,π)` and principal value in `(−π,π]` forces equality, so `arg(z₁/z₂)=0`, `z₁/z₂>0`. The supplementary branch is correctly killed. I re-derived the `mod 2π ⇒ equal` collapse myself — correct.
- **C1, C2, C3.** For each I recomputed the ray-ratio quotient and confirmed it equals `C_i` (with the midpoint artifacts `L−N=(2l−c)/2`, `K−M=(2k−b)/2` used correctly), and I re-derived every `θ,β,γ ∈ (0,π)` sign fact:
  - `θ₁: [B,K,A]=½Im(b̄k)>0` (K1); `θ₂: [C,A,L]=−½Im(c̄l)>0` (L1);
  - `β₂: Im(c/(2l−c))>0 ⟺ Im(cl̄)>0 ⟺ Im(c̄l)<0` (L1) — note `cl̄ = conj(c̄l)`, sign flips, handled correctly;
  - `β₁` (K inside ∠LBA): (L2) gives `[B,L,A]>0` so `φ=∠(BL→BA)∈(0,π)`; K in the convex sector ⟹ `β₁∈(0,φ)⊂(0,π)`. Valid.
  - `γ₂: Im((2k−b)/b)>0 ⟺ Im(kb̄)>0 ⟺ Im(b̄k)>0` (K1) — here `kb̄=b̄k` (commutative), sign does NOT flip; handled correctly and distinguished from the `β₂` case.
  - `γ₁` (L inside ∠ACK): reuses `θ₂=∠(CA→CL)∈(0,π)`; L interior forces `∠(CA→CK)∈(θ₂,π]`, so `γ₁=∠(CA→CK)−θ₂∈(0,π−θ₂)`. The convex-sector betweenness (CK must be CCW because the interior ray CL sits at `+θ₂`) is correct.
  The two "inside-angle" hypotheses are used correctly and are the genuine problem hypotheses. `check_s3.py` re-run: every sign and `arg C_i=0` confirmed (sanity only).

**§4–§6 — algebraic core is intact and correct.** `repro.py` re-run: each `E_i` is affine in `(k̄l̄,k̄,l̄)`; `detA=bb̄cc̄·P4`; the two exact identities **(I)** `Rnum=(b−k)(c−l)·G` and **(II)** `num=qN·G` both return `True` (deg G = 10). The logic detA≠0 ⟹ unique Cramer solve ⟹ `k̄=Y_s,l̄=Z_s` ⟹ consistency `Rnum=0` ⟹ `G=0` (since `b≠k,c≠l`) ⟹ `num=0` ⟹ `TN=0` ⟹ `OM=ON` is sound.

### The one remaining gap (why NOT solved)

**Removal of the `detA=0` locus (§6, final paragraph) is rigorous only for the audited triangle.** The main argument proves OM=ON only where `detA≠0`. The continuity paragraph removes `detA=0` by claiming, for an arbitrary admissible triangle, that `detA(α)` is real-analytic and "not identically zero (it is nonzero at the audited value)", plus real-analyticity of the α-branch "confirmed numerically." For a *general* triangle the audited value is not in its α-family, so "`detA(α)≢0`" and the branch-analyticity are **asserted / numerically confirmed, not derived**. A priori some special admissible triangle could have its whole 1-parameter family inside `{detA=0}`; the proof does not exclude this.

This is exactly a "key step confirmed only numerically" — which the rigor rules and my role memory forbid approving. It is a genuine, if minor, logical gap.

*Diligence:* I swept 5 fixed triangles + 486 random admissible configs; `|detA/(bb̄cc̄)| = |P4|` stays `≥ 0.82`, never near 0, and `|OM−ON| < 1e-10` everywhere. So the mathematical content is almost certainly complete — but numerics are not a proof.

**How to close (1-round fix):** either (a) prove `detA ≠ 0` for every admissible interior configuration (then the main argument alone suffices, no continuity needed), or (b) give a genericity/continuity argument valid for *all* triangles — e.g. connectedness + real-analyticity of the full configuration manifold, on which OM−ON vanishes on the nonempty open set `{detA≠0}` hence identically.

### Scores
- Correctness: 9.5/10 — everything written is valid; no wrong step found.
- Completeness/rigor: 8.5/10 — one non-degeneracy step under-justified for general triangles.
- Progress: very high — the round-1 §3 gap is fully closed; the residual is a standard degenerate-locus removal.

**Recorded outcome: `advanced`.** **Overclaim: builder's `solved` was wrong; corrected to `partial` in the approach file and current.md.**

---

## Approach 2 — `antipode-perp-bisector`

**Builder claimed: partial. Reviewer verdict: CHANGES REQUESTED. True Status: partial (correctly self-assessed).**

### Verified rigorous
- **Step 1 (antipode equivalence).** `OM=ON ⟺ A*B=A*C ⟺ A*·(c−b)=(|c|²−|b|²)/2 ⟺ A*` on perp-bisector of `BC`. I re-expanded both differences of squared distances; the `A*=2O` cancellation is exact. Correct. The antipode–power bridge `(X−A)·(X−A*)=pow_ω(X)` is also correct.
- **Step 2 (Thales location).** `A*K⊥AK, A*L⊥AL` since `A*` is the antipode of `A` on `⊙(AKL)`. Correct.

### Gap (as stated by builder, precise)
- **Step 3 / Lemma B, Lemma C** — `∠A*BK = 90°−C`, `∠A*CL = 90°−B` — the two α-independent invariants. **Only numerically certified (1e-8), unproven.** This is the load-bearing content of the route.
- Minor: **Step 4** additionally leans on "A* inside angle BAC" and the ray-betweenness ordering, which are asserted with numerical verification, not derived. So Step 4 is rigorous only *modulo* Lemma B/C **and** that placement.

The gap is stated precisely and the self-assessment `partial` is correct. Independent of the (★★)/(♦5) crux — a genuine breadth hedge.

### Scores
- Correctness: 9/10 (Steps 1,2 valid; Step 4 conditionally valid).
- Completeness/rigor: 4/10 — the entire crux (Lemma B/C) is unproven, only numeric.
- Progress: moderate — sharpened the crux from a vague "candidate mechanism" to two crisp symmetric invariants and proved the surrounding scaffold.

**Recorded outcome: `partial`.**

---

## Certified lemmas (round 2)
- **`lemmas/reality-hinge-directed-angle.md`** (Lemma 2 + (SGN)) — ADMITTED. Correct, reusable, no stronger than proved.
- **`lemmas/antipode-perp-bisector-equivalence.md`** (Step 1) — ADMITTED. Correct, reusable.
(Existing `circumcenter-of-0-k-l.md`, `product-to-sum-S.md` unchanged.)

---

## Goal Progress

Goal: proof-reviewer APPROVE (Status `solved`) on a complete rigorous proof of OM=ON. **Not yet met — Status remains `partial`, but materially closer.**

Ranking snapshot (Elo, pre-update; outline-reviewer will re-rank):
- complex-reality-conditions 1547.7 — **advanced** (round-1 §3 gap CLOSED; sole residual = detA≠0 nondegeneracy/continuity for all triangles). Clear leader, one step from solved.
- trig-decoupled-bash 1522.1 — partial (crux (★★)).
- power-of-point-balance 1514.0 — partial (same crux (★★)).
- antipode-perp-bisector 1416.2 — partial (crux Lemma B/C, numeric-only); independent route.

**Verdict per slug:**
- `complex-reality-conditions`: **CHANGES REQUESTED** (Status partial) — close the detA=0 removal for all triangles.
- `antipode-perp-bisector`: **CHANGES REQUESTED** (Status partial) — prove Lemma B/C.

Headline: the complex approach's geometry→algebra translation is now fully rigorous and reviewer-verified; only a standard degenerate-locus removal separates it from `solved`. Numerics (`|detA|≥0.82` over 486 configs) strongly indicate it will close next round.
