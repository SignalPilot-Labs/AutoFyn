## imo-2026-03

Answer (all three approaches target the same claim): **c(n) = 2^n / (2^{n+1} - 1)**.
Write D_n = 2^{n+1}-1. Checks: n=1 -> 2/3, n=2 -> 4/7, n=3 -> 8/15 (I verified n=1,2
exactly by adversary grid-search, and that the *self-similar XY attack* — pour all n
cuts into the largest piece re-imposing dyadic ratios — hits exactly 2^n/D_n for every
n up to 5). Each approach must deliver BOTH a matching LB construction and a matching
XY cap; one bound alone is `partial`.

Shared across all three: **Lemma 0 (endgame/greedy)** — for a fixed piece multiset the
alternating-claim value to the first mover is the sum of odd-ranked pieces (sorted
descending). Proof = induction on piece count + monotonicity sub-lemma. Should be
proved once and cached at `lemmas/endgame-greedy.md`, then imported by all approaches.
Recorded dead ends (do NOT re-propose): "LB marks n+1 equal pieces" (collapses to
~1/2, killed for n=2) and "XY equalizes to 2n+1 equal pieces / uses all n cuts blindly"
(false; XY does better surgically). Coarse numeric search over-reports LB's value.

The three framings are deliberately far apart so they do not share one wall: a
recursion-on-n, a one-shot majorization on the sorted vector, and a change-of-functional
to a threshold-integral potential. Their attacks on the common hard gap (XY caps EVERY
LB marking) are genuinely different (peel-the-largest induction / directed-majorization
smoothing / parity-toggle measure accounting).

---

self-similar-recursion: new
Target: c(n) = 2^n/D_n, both bounds.
Technique: strong induction on n exploiting that the dyadic largest piece is a scaled
copy of the (n-1)-problem (w_n = 2 w_{n-1}; the n smaller pieces are W_{n-1} scaled by
D_{n-1}/D_n) and that XY's worst attack pours all cuts into the largest piece.
Skeleton:
  1. Lemma 0 (endgame) — reduces game to odd-rank-sum.
  2. Lower bound by induction: LB plays dyadic W_n; XY budget split j/(n-j) between
     largest piece and scaled W_{n-1}; interleave + IH + w_n=2w_{n-1} => worst case
     j=n gives exactly 2^n/D_n.
  3. Upper bound by induction: XY "clones the leader" (bisect current max), residual is
     an (n-1)-problem; paired halves cancel LB's edge => cap 2^n/D_n for ALL LB markings.
  4. Combine; verify n=1,2,3.
Key lemmas: self-similar decomposition of W_n (because w_n=2w_{n-1} and the tail is a
scaled W_{n-1}); worst XY response = all cuts in the largest piece (exchange: cutting a
non-max piece only raises LB's total); clone-the-leader pairs off the top (equal halves
contribute 0 to the alternating sum).
Open gaps: G1 LB budget-split analysis (j=n is worst); G2 UB recursion bookkeeping for
ALL LB markings (the crux); G3 non-max-cut domination.
Cases to cover: both bounds; base n=0,1; XY budget j=0..n; fewer/coincident cuts.
Watch out for: UB must not secretly assume LB played dyadic; equal large pieces cancel
LB's edge (not an advantage); ties handled by Lemma 0.

majorization-smoothing: new
Target: c(n) = 2^n/D_n, both bounds.
Technique: one-shot majorization of the sorted-descending vector against an explicit
reference R_n (the self-similar-attack multiset) + a local smoothing lemma; NO induction
on n. Borrows aimo-0718's "maintain a majorization invariant one adversary-move at a
time" shape (each XY cut = one move).
Skeleton:
  1. Lemma 0.
  2. Smoothing lemma: Odd(a) is piecewise-linear in a single cut position with
     breakpoints at existing piece values; extrema at breakpoints; non-max cuts dominated.
  3. Upper bound: XY repeatedly bisects the max; final vector majorized by R_n, and Odd
     respects this along the taken path => Odd <= 2^n/D_n for every LB marking.
  4. Lower bound: LB plays W_n; exchange pushes every XY response toward R_n, floor
     Odd = 2^n/D_n.
  5. Conclude; verify n=1,2,3.
Key lemmas: smoothing lemma (Odd piecewise-linear per cut, KB piecewise-concavity
smoothing); DIRECTED majorization=>Odd bound only along the actual cut path (Odd is NOT
monotone under general majorization — key correction); paired-top cancellation.
Open gaps: G1 smoothing lemma statement/proof; G2 UB majorization-to-R_n + directed
monotonicity for ALL markings (crux); G3 LB exchange that R_n is the minimizer.
Cases to cover: both bounds; XY bisecting < n times (early stop); non-max cuts; ties.
Watch out for: the FALSE "Odd monotone under majorization" — stay on the explicit path;
reference R_n deliberately has matched pairs; no simulation as proof.

alternating-sum-threshold-potential: new
Target: c(n) = 2^n/D_n, both bounds.
Technique: change the target functional. LB total = (1+A)/2 with A the alternating sum
of sorted pieces, and A = integral_0^inf 1[c(t) odd] dt where c(t)=#{pieces > t}. So
LB total = (1+M)/2, M = measure{t: odd # pieces exceed t}; claim reduces to M* = 1/D_n.
(Both identities verified numerically to machine precision.) Genuinely far from the
sorted-vector framings — the object is a threshold integral / parity potential.
Skeleton:
  1. Lemma 0 => LB = (1+A)/2.
  2. Layer-cake identity A = integral 1[c(t) odd] dt (telescoping
     sum(-1)^{i+1}1[i<=c] = 1[c odd]).
  3. Lower bound: LB dyadic; each XY cut toggles c(t)-parity only inside the piece it
     cuts; dyadic gaps cap total destroyable odd-measure so M >= 1/D_n.
  4. Upper bound: XY bisects to make c(t) even on as much of [0,1] as possible; n cuts
     reduce odd-measure geometrically to residual 1/D_n for ANY LB marking (weighting
     inequality over threshold levels).
  5. Conclude M* = 1/D_n => c(n)=2^n/D_n; verify n=1,2,3.
Key lemmas: payoff identity LB=(1+M)/2 (layer-cake); single-cut parity action (a cut
flips c(t)-parity on the band below the smaller resulting part); dyadic gaps bound the
toggling (geometric band lengths, extremal at dyadic re-split).
Open gaps: G1 exact single-cut action on M; G2 LB "destroyable odd-measure <= 1-1/D_n"
inequality (crux); G3 UB residual <= 1/D_n weighting inequality for ALL markings (crux).
Cases to cover: both bounds; cuts in large vs small pieces; XY using < n cuts; ties
(measure zero).
Watch out for: off-by-one in the layer-cake parity identity; weight parity-toggles by
band length, not cut count; state single-cut action for all offsets not just bisections.

---

build set: self-similar-recursion, majorization-smoothing, alternating-sum-threshold-potential
