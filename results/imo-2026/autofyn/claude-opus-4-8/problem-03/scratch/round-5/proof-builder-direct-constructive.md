# Proof-builder report — direct-constructive, Round 5

Status: **partial** (advanced both gaps substantially; two precise residuals remain).

## LOWER bound (★) — Descent Lemma: essentially CLOSED (one degenerate face residual)
Wrote §4.2.7. min_R A attained at a cell-complex vertex; the mass-transfer directional derivative is
A′₊(e_a−e_b) = (−1)^{G(g_a)} + (−1)^{Geq(g_b)} (G=#pieces>, Geq=#pieces≥). A (receiver=G-odd,
positive donor=Geq-odd) pair gives A′=−2, forbidding an interior min.

Fully rigorous parts:
- **Receiver always exists** — parity/i′-range argument (no-receiver forces i′ to increase by ≥1
  across n+1 distinct fragment levels within a range of only n−1). Numerics: 0 failures / ~1.5·10^5
  a=0 configs at n=3,4,5.
- **Boundary g_i=2^{n−1}**: A≥1 by continuity from the certified a=1 cascade.
- **Boundary g_i=0**: fewer-fragment induction (base = 2 fragments forced to 2^{n−1}).
- **No-donor interior branch**: the key clean discovery — if every positive fragment has Geq even,
  the smallest-value level is non-fragment, so ALL fragments >1; then intact 1 sits at the bottom
  odd rank contributing +1, and A = A′+1 ≥ 1 (A′ = sorted alternating sum ≥ 0). Verified: 0
  exceptions (every donor-absent config has min fragment >1).

Residual (minor, honest): the degenerate branch (ii) where a single fragment is simultaneously the
sole receiver and sole donor (fragment value sits exactly on an intact 2^s). Handled by a FLAT
transfer (A′₊=0 both directions) that moves to the boundary/reduces fragment count; I argued
termination via finiteness of the cell complex but did not write a fully formal termination
certificate. This is the only formal loose end in the lower bound.

## UPPER bound U1 — corrected IH(q) relative-threshold reduction (~94% closed)
Wrote §6.2. Valid one-step reduction to IH(q−1) exists iff **S − max(b_1, 2b_2) < (2^{q−1}−1)/D**
via halve-b_1 OR cut-b_1-at-b_2 (pair cancels, residual singleton stays >1/D since gaps >1/D).
Confirmed the reviewer's refutations: absolute threshold b_1>2^{q−2}/D insufficient; plain Euclidean
cascade fails ~30%. The ~6% flat residual (needs the two-cut cascade, base = certified IH(3)
doubly-hard leaf) and sub-case B2 (a_1≤1/2, no dominant piece) remain GAP U1 — marked explicitly,
not overclaimed.

## Promotable lemmas (for certification)
1. Descent Lemma (a=0 lower bound engine).
2. Receiver-existence parity lemma.
3. Corrected IH(q) relative-threshold reduction (upper bound engine).
All stated in the approach file's Promotable section with proof locations (§4.2.7, §6.2).

## Spec concerns
None on the problem statement. The answer c(n)=2^n/(2^{n+1}−1) is unchanged and small-n verified.
The lower bound is now one formal-termination lemma away from complete; the upper bound hard-regime
flat residual + B2 remain the field-wide open core (as expected — the field has collapsed to this
one framing, and these are its genuine walls).
