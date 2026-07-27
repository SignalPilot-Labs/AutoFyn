## Outline review — imo-2026-03 (toggle-pair / parity-integral outline)

### Verdict: APPROVE (with one mandatory textual fix and two builder instructions)

The strategy is sound on all three foci. The corrected toggle-pair mechanism is
right, the even-sum reformulation is algebraically correct, and the exhaustive
breakpoint fallback is a legitimate rigorous proof for fixed n. The builder may
proceed, subject to the items below.

---

### 1. Toggle-pair claim — CORRECT, but the n=1 verification text is wrong

Mechanism check (cut s → (m,M), m ≤ M, m+M = s): before the cut the piece s
contributes +1 to r(t)=#{pieces ≥ t} on (0,s]; after, m contributes +1 on (0,m]
and M contributes +1 on (0,M]. Hence Δr = +1 on (0,m], 0 on (m,M], −1 on (M,s].
Parity therefore toggles exactly on (0,m] and (M,s] (both length m), unchanged on
(m,M]. This matches the outline exactly. The earlier "r_final = r_0 + R" (Lead 1)
is indeed false — it omits the −1 on (M,s]; the correction is the right fix.

**Mandatory fix.** The outline's n=1 verification (proof-outliner.md line 8) states
the INITIAL parity of G_1 = (1,2) backwards: it says "r_0 parity odd on (0,1],
even on (1,2]". The true initial parity is r=2 (even) on (0,1] and r=1 (odd) on
(1,2], so D_0 = 1 comes from (1,2], not (0,1]. The final D=1 is still right
(toggling both intervals sends even→odd on (0,1] and odd→even on (1,2]), but the
builder must correct the stated initial parity, because the verification as
written is self-contradictory (its stated initial parity would make the *halving*
cut leave (1,2] odd, not (0,1]). Fix the text; the underlying lemma is sound.

### 2. Even-sum reformulation — CORRECT

D = Σ_odd − Σ_even and S_n = 2^{n+1}−1 = Σ_odd + Σ_even give
D ≥ 1 ⟺ S_n − 2Σ_even ≥ 1 ⟺ Σ_even ≤ (S_n−1)/2 = 2^n − 1, and equivalently
Σ_odd ≥ 2^n. Verified numerically (n=3: (S−1)/2 = 7 = 2^3−1). The Case-A
one-liner (2^n intact ⟹ odd-position 1st ⟹ every even-position piece is tail
⟹ Σ_even ≤ |tail| = 2^n−1) is valid. No change needed.

### 3. Fallback exhaustive-casework for L(2), L(3), U(2) — LEGITIMATE, with a coverage instruction

For fixed n, D is a continuous piecewise-linear function of the (≤ n) cut
positions; its regions are the cells of the arrangement "two piece-sizes
coincide", and each cell is a compact polytope (cut positions live in bounded
intervals). On each region D is a single linear form, whose minimum over the
closed polytope is attained at a vertex. Therefore checking D ≥ 1 (resp. D ≤
1/S_n) at every breakpoint/vertex of the arrangement is a rigorous proof —
**provided** the builder does all of:

- (a) Enumerate the COMPLETE breakpoint set: every equality of two piece-sizes
  (including fragments equal to fragments, fragments to original geometric
  pieces, and fragment = half-of-a-piece where that changes sorted order). The
  outline's "coincident-sorted-order" is the right primitive; the candidate-cut
  set {fragment = existing piece} ∪ {fragment = half a piece} used in the
  numeric search is a heuristic superset — the builder should either prove it
  contains all breakpoints or enumerate directly from "two piece-sizes equal".
- (b) Check the vertices, AND argue explicitly that the per-region minimum is at
  a vertex (the linear-form-on-compact-polytope principle). Do not only check
  breakpoints without stating why interiors need no separate check — the
  reviewer will flag a bare "we checked the breakpoints" as a gap otherwise.
- (c) Include boundary/degenerate vertices (a cut at 0 or at the full piece,
  coincidences of three or more pieces) so the polytope vertices are all closed.

This is a legitimate fixed-n proof. It does NOT prove the general case; the
outline correctly labels it as a fallback advancing n≤3 / U(2) only.

---

### Other notes for the builder

- The HARD Lemma (Case B general) remains a genuine hand-off: the stated
  mechanism ("staircase self-similarity + the +1 gap forces an unmatched parity
  unit") is plausible and the right *kind* of argument, but it is not a proof
  yet — the outline itself flags it as the load-bearing open step. The builder
  should either close it or, per the outline's own priority, fall back to the
  exhaustive casework for n=2,3 and mark the general case as a conjecture.
  Either is acceptable; do not present the general toggle lemma as established.
- Upper bound: the smoothing/Schur-maximisation lemma is correctly flagged as
  conjectural. Keep it stated, not claimed.
- Equality case (full halving, D=1) certification is in place; keep it.

### Summary of builder actions
1. Fix the n=1 verification's stated initial parity (even on (0,1], odd on (1,2]).
2. For exhaustive casework: prove/justify the breakpoint set is complete, invoke
   the vertex-min-of-linear-form principle explicitly, cover degenerate vertices.
3. Do not claim the general Case B (toggle) lemma or the smoothing lemma as proved.
