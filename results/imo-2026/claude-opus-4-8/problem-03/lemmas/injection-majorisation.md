# Lemma injection-majorisation — Hall/layer-cake lower-bound closer (certified round 8)

**Setup.** Stray a=0 lower bound (see EF-OG-reformulation). N_F(x) = #{F-pieces > x},
N_G(x) = #{G-pieces > x}, N(x) = N_F(x) + N_G(x). By Lemma R (certified), E = ∫_0^∞ ⌊N(x)/2⌋ dx and
ΣG = ∫_0^∞ N_G(x) dx. D = 2^{n+1} − 1, ΣG = 2^n − 1.

**Statement.** If **N_F(x) ≤ N_G(x) + 1 for all x ≥ 0**, then **A ≥ 1**.

**Proof.** The hypothesis gives N(x) = N_F(x) + N_G(x) ≤ 2N_G(x) + 1, so for every x,
⌊N(x)/2⌋ ≤ ⌊(2N_G(x)+1)/2⌋ = N_G(x). Integrating, E = ∫⌊N/2⌋ ≤ ∫N_G = ΣG, hence
A = D − 2E ≥ D − 2ΣG = (2^{n+1}−1) − 2(2^n−1) = 1. ∎

**Interpretation.** N_F ≤ N_G+1 is the majorisation condition under which each even-rank fragment matches
a distinct ≥-large G-piece. Covers the non-clustered regime; genuinely different from the receiver/donor
machinery. Does NOT cover the true minimiser (where F is clustered, N_F can exceed N_G+1, and E_F > 0 —
the open tight-face residual). Layer-cake bound; reusable.
