# Halving / k-descent lemma (Mulan's triangle game)

**Statement.** Suppose the current triangle has an angle equal to kθ for some integer k ≥ 1 (and θ=180°/n for an integer n≥2, so 180°=nθ). Then Mulan can force a win in at most k−1 further moves.

**Proof (strong induction on k).**

*Base k=1:* the angle θ is already present; the game stops at the next check; 0 = k−1 further moves.

*Inductive step k≥2:* Place the angle kθ at vertex A; write the other two angles as b,c (kθ+b+c=180°). Mulan cuts at vertex A with parameter α=θ (legal: 0<θ<kθ since k≥2). By the cut-geometry lemma the children are
  △ABP = (θ, b, (k−1)θ+c),   △ACP = ((k−1)θ, c, b+θ).
Both are valid triangles (positivity: θ>0, b>0, (k−1)θ+c>0; (k−1)θ>0, c>0, b+θ>0; sums check to 180°). The first child contains θ: if Shan-Yu keeps it, the game stops and Mulan wins. To postpone defeat, Shan-Yu must keep △ACP, which contains the angle (k−1)θ. By the inductive hypothesis (with k→k−1 ≥ 1), Mulan then wins in at most (k−1)−1 = k−2 further moves. Total: at most 1+(k−2) = k−1 moves. ∎

**Certified by:** proof-reviewer, round 1 (all three approaches proved it from scratch, identically). **Source:** approaches/lattice-coset-descent.md §5 (Lemma D), approaches/altitude-halving.md §2 (Lemma 2), approaches/safe-unsafe-pairing.md §II.1.
