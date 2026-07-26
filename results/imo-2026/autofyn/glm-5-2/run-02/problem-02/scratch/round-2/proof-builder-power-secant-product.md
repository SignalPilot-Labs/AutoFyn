# proof-builder — power-secant-product (round 2)

## What was done

**Sign fix (mandate 1) — DONE, rigorous.** Re-derived `∠CAW` from scratch via inscribed-angle theorem + intersecting-chords interior-angle theorem, directed mod π (NOT acute-angle arccos picks). The arc `arc(QW) = −2(b+β)` (from `2·∠ANL = arc(AL)+arc(QW)` with `∠ANL = −β`, `arc(AL)=2b`) gives `∠CAW = ½·arc(QW) = −(b+β)`. Numerically `∠CAW = 40.393°` and `−(b+β) = 40.393°` (residual ~1e-10); the round-1 `b−β = −71.673°` does NOT match (mod π either). Corrected crux `(**)_corr` with `sin(b+β)` verified to ~1e-10 (the wrong `sin(b−β)` version is off by 0.06). The other three Step-4 lemmas (`∠ALV=γ−u`, `∠BAV=γ−a`, `∠AKW=−(w+β)`) re-confirmed correct.

**SUM-form external-angle theorem (mandate 2) — DONE, rigorous.** Proved `∡(Xn₁,Xn₂) = ½[arc(far₁,far₂)+arc(near₁,near₂)]` via the directed triangle angle sum in `△Xn₁n₂` + the directed inscribed-angle theorem at n₁, n₂ (ray-flip-by-π is invisible mod π). Verified numerically: B-side `½[arc(A,R)+arc(P,K)] = −22.402° = ∡(BA,BK)` (the round-1 DIFFERENCE form gives `−42.44°`, wrong). Derived the **α arc-sum** as a corollary: `2α = arc(R,A)+arc(K,P) = arc(A,S)+arc(Q,L)`, giving `arc(R,A)=2(α+u)`, `arc(A,S)=2(α−w)` (both verified to 1e-13).

**Bridge (mandate 2) — partially DONE, honest gap.**
- **Cross-ratio link `(A,P;R,V)=(A,P;B,M)` PROVED** (the load-bearing bridge piece the outline-reviewer flagged unproved): the perspectivity (pencil at K) projects line AB → Γ, sending A→A, P→P, B→R, M→V; perspectivities preserve cross-ratios. Verified numerically to 1e-15. C-side `(A,Q;S,W)=(A,Q;C,N)` proved identically.
- **Sine-of-arc form of the circle cross-ratio PROVED** (Step 8): `(z₁,z₂;z₃,z₄) = [sin½(θ₃−θ₁)sin½(θ₄−θ₂)]/[sin½(θ₃−θ₂)sin½(θ₄−θ₁)]` (real; sign by separation), from `z_k−z_j = 2iR e^{i(θ_k+θ_j)/2} sin((θ_k−θ_j)/2)`.
- The α-arc positions of R, S + the cross-ratio links + sine-of-arc form yield the B-side sine-arc equation `sin(α+u)sin(γ−a)/[sin(α+a)sin(γ−u)] = ±2|MP|/|PB|` and the C-side analogue. Eliminating `|AB|,|AC|` via the sine rule in △ABK, △ACL reduces the pair to trig equations in the angle variables alone.
- **Ptolemy turned out UNNECESSARY**: once the cross-ratio is in sine-of-arc form (Step 8), it is already a product-of-sines identity; Ptolemy would be redundant. The bridge reduces to a single directed-trig cancellation, not a Ptolemy identity. (Spec deviation from the outliner/explorer, who named Ptolemy as the algebraic closer — reported here.)

**Residual gap (honestly marked).** The final directed-trig cancellation that takes {B-side eq (B), C-side eq (C), △AKL angle-sum} to `(**)_corr` is NOT completed. Every individual link is verified numerically to ~1e-10 (cross-ratios 1e-15, α-arc-sum 1e-13, line-length substitutions 1e-10); α necessity+sufficiency confirmed by drop-test. But the symbolic directed-trig derivation — in particular resolving the `±` signs of (B), (C) by the directed-separation rule (mod π, NOT acute-angle picks — the numpy-sign-trap) and showing the resulting identity is `(**)_corr` — is open. Status: **partial**.

## Spec concerns
- The outline's named "Ptolemy on (A,V,P,K)/(A,W,Q,L)" closing mechanism appears redundant once the cross-ratio is in sine-of-arc form. The bridge is better described as "cross-ratio + sine-of-arc + α-arc-sum + triangle sine-rules ⟶ directed-trig cancellation", not "Ptolemy". Reported above; the approach file's Step 9 reflects this.
- The directed-sign bookkeeping in (B), (C) is exactly the failure mode the round-1/round-2 rules warn about (numpy acute-angle trap). I did NOT resolve it numerically by sign-picking; I left it as an explicit `±` and flagged the directed-separation resolution as the open rigorous step. A future round should close it with pure directed-angle reasoning (mod π throughout), or via a CAS field-reduction over the angle variables with `A+B+C=π` as the only incidence constraint.

## Files
- Approach file: `/home/agentuser/repo/results/imo-2026-02/approaches/power-secant-product.md` (Status: partial).
- Six promotable lemmas proposed for certification: power-secant reduction, corrected directed-angle lemmas (with `∠CAW=−(b+β)`), SUM-form external-angle theorem, α arc-sum, midpoint cross-ratio link, sine-of-arc circle cross-ratio form.
