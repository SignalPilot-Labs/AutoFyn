## imo-2026-03

Answer (all three explorers + my exact-Fraction checks agree): **c(n) = 2^n / (2^{n+1} − 1)**.
Confirmed: greedy == brute-force minimax on 300 random multisets; grid-min of LB's share against
the geometric config = exactly c(n) for n=1,2,3; maximin over LB configs for n=2 = 4/7.

Shared foundation for ALL approaches — **Lemma G (greedy optimality of the claiming game)**, proved
in full in the approach files (elementary; propose to `lemmas/greedy-optimality.md`): with sorted
pieces p_1≥…≥p_k, taking the largest each turn is optimal and LB = Σ_odd, XY = Σ_even. Crux is the
sorted-pairing identity Σ_odd(L_j) ≥ Σ_odd(L_1) (removing the largest minimizes the remainder's
odd-index sum). This makes both bounds well-defined; it is the first thing the builder should lock.

---

### Resolution of the n-vs-(n−1) cut tension (flagged in dispatch)
**No contradiction — XY has multiple optimal responses; the value is identical.** Against LB's
geometric config for n=2: XY with 1 cut → pieces {2,2,2,1}/7, LB = 4/7; XY with 2 cuts (full
replica) → {2,2,1,1,1}/7, LB = 4/7. For n=3: XY with 2 cuts → {4,4,3,2,1,1}/15, LB = 8/15; XY with 3
cuts → {4,4,2,2,1,1,1}/15, LB = 8/15. Both hit c(n) exactly. The computation lens's "extra cuts
increase LB" is imprecise — I could not reproduce it; extra cuts are neutral here. **Rule for every
approach: state XY uses AT MOST n cuts and never rely on the exact count.** (Recorded to role memory.)

---

geometric-selfsimilar: new
Target: c(n)=2^n/(2^{n+1}−1); lower bound (LB guarantees ≥c(n)) AND upper bound (XY forces ≤c(n)).
Technique: Lemma G reduces to the claiming game; then induction on n via the self-similar geometric
structure (each piece 2× the previous; largest > sum of the rest). Explicit XY = concentrate all cuts
on LB's largest piece and split it into a replica.
Skeleton:
  1. Lemma G (greedy) — sorted pieces, LB = Σ_odd. [proved in file]
  2. LB plays geometric g_i=2^i/D, D=2^{n+1}−1; dominance g_i > Σ_{j<i} g_j.
  3. Lower bound, induct on n: base n=1 (median=1 forces LB=2); Case 1 XY spares largest ⇒ LB takes
     it ≥ c(n); Case 2 XY cuts largest ⇒ self-similar recursion to G(n−1). [GAP L2]
  4. Upper bound: XY concentrates n cuts on A_1, splits to push each smaller piece to an even
     (XY) position; induction/self-similarity caps LB ≤ c(n) for arbitrary configs. [GAP U1,U2]
Key lemmas: Lemma G (Σ_odd(L_j)≥Σ_odd(L_1)); Dominance (cutting can't beat the intact largest);
Self-similar reduction (remove largest, rescale ½ → G(n−1)); Replica/interleave split.
Open gaps: L2 (Case-2 inductive lower bound); U1/U2 (universal upper bound — hardest).
Cases to cover: lower {base, XY spares largest, XY cuts largest t=1..n}; upper {every LB config,
m<n+1 pieces, A_1>½ vs ≤½}.
Watch out for: distinct-points/attainment of c(n); XY uses ≤n cuts; tie-robustness of Lemma G.

alternating-sum-value: new
Target: same whole claim, via reformulation.
Technique: LB=(1+A)/2 with A=p_1−p_2+p_3−… (alternating sum of sorted pieces); reduce to proving the
alternating-sum game value A* = 1/D. New toolkit: telescoping bounds 0≤A≤p_1 and the equal-run
collapse of A, plus a Φ=A monovariant.
Skeleton:
  1. Lemma G + reformulation LB=(1+A)/2 (since Σ_odd−Σ_even=A, Σ_odd+Σ_even=1).
  2. A-bounds: A≥0, A≤p_1, even runs of equal pieces zero out A.
  3. Lower bound: geometric ⇒ A≥1/D; XY-spares-largest case direct (A≥2g_n−1=1/D); XY-cuts-largest
     by induction tracking A. [GAP AL]
  4. Upper bound: XY equalization/halving drives A down to the smallest piece; n cuts reduce any
     ≤(n+1)-piece spectrum to A≤1/D. [GAP AU]
Key lemmas: Reformulation (LB=(1+A)/2); A-bounds (sorted telescoping + equal-run collapse);
lower cut lemma (AL); XY equalization monovariant (AU).
Open gaps: AL (geometric lower bound in A); AU (universal A≤1/D via equalization).
Cases to cover: lower {spares vs cuts largest}; upper {every spectrum, even/odd piece count, A_1>½}.
Watch out for: A≤p_1 is weak — cancellation not max-shrinking is the mechanism; per-cut A-drop is
NOT uniform (one cut can drop A a lot); attainment; ties central (they zero A).

extremal-smoothing: new  (bypass approach — routes AROUND the shared hard gap)
Target: same whole claim, but the upper bound WITHOUT an explicit XY strategy for arbitrary configs.
Technique: prove LB's geometric config is the maximin MAXIMIZER by a smoothing/perturbation lemma +
compactness (Weierstrass); then value at geometric = c(n) gives both bounds. Only needs ONE explicit
XY response (against the single geometric config), not a universal strategy.
Skeleton:
  1. Lemma G; define V(A)=min over XY responses of LB's Σ_odd; maximin = c(n) is the goal.
  2. V(geometric)=c(n): ≥ by the geometric lower-bound induction; ≤ by the single replica response.
     [GAP S0, cheaper ≤ side]
  3. Smoothing lemma: any non-ratio-2 spectrum can be perturbed toward geometric with V weakly up.
     [GAP S1 — the bet]
  4. Compactness/u.s.c. ⇒ maximin attained at geometric ⇒ max V = c(n). Both bounds follow.
Key lemmas: value-at-geometric (S0); smoothing monotonicity (S1); semicontinuity+Weierstrass.
Open gaps: S0 (geometric lower bound — shareable with geometric-selfsimilar); S1 (novel, load-bearing).
Cases to cover: smoothing for too-flat / too-steep / boundary spectra; boundary attainment.
Watch out for: S1 could fail if V is not monotone toward geometric — verify perturbation sign on a
few explicit spectra first; V non-smooth (use subgradients); do NOT claim uniqueness of the maximizer
(grid found {1/14,3/14} also = 4/7); XY ≤ n cuts on the ≤ side.

---

### How the three differ (breadth, not one line split)
- geometric-selfsimilar and alternating-sum-value share the geometric LB construction and Lemma G but
  attack the UPPER bound with different machinery (explicit replica strategy vs alternating-sum
  equalization) and reframe the whole target differently (raw share vs value of A). Distinct routes.
- extremal-smoothing challenges the shared assumption that the upper bound needs an explicit XY
  strategy — it derives geometric as an extremal *conclusion*. If S1 holds it sidesteps U1/U2/AU
  entirely. This is the insurance against the whole field bottoming out on "construct XY for arbitrary
  configs."

### Build-set recommendation
Build **geometric-selfsimilar** and **alternating-sum-value** this round (the two most concrete; both
should first certify Lemma G to `lemmas/`, then attack lower bound — the accessible direction — before
the upper-bound gaps). Keep **extremal-smoothing** live as the bypass; build it if the two shared
upper-bound gaps (U1/U2, AU) stall across rounds. All three depend on Lemma G — certify it once and
share it.

Registered all three at Elo 1500 (`.ranking.json` written).
