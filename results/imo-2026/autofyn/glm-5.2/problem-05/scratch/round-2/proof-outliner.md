## imo-2026-05 (founding field, round 2)

The workspace `results/imo-2026-05/approaches/` was empty after round 1; this is
the founding field. Four rival approaches opened, each a whole attempt at the
full characterization $f(x)=x+c,\ c\ge0$ (exhibit + uniqueness), far apart in
**framing and route**. All four share three derived-theorem lemmas (the builder
re-derives each from scratch; do not treat as assumed): orbit invariance
$g(f(y))=g(y)$; $g\ge0$ (orbit forward-positivity); and the **master squeeze**
$|g(x)-g(y)|(g(x)+g(y)+2x+2y)\le(x-f(y))^2$ — a single-inequality reduction of
BOTH original inequalities via the SOS identity $U+L=(x-f(y))^2/2$,
$U-L=-(g(x)-g(y))(g(x)+g(y)+2x+2y)/2$ (verified symbolically). The master
squeeze is approach `master-sos-identity`'s certifiable lemma; the other three
import it. The approaches differ in how they cross from "pinned/continuous on
image points" to "globally constant" — the shared hard wall.

---

### orbit-monotonicity-sandwich: new
Target: full characterization (exhibit + uniqueness).
Technique: orbit/iterate identity + monotonicity trapping sandwich (aimo-0234
template). Pin $g$ on each arithmetic orbit $\{y+n g(y)\}$ via $g\circ f=g$;
prove $f$ is monotone nondecreasing; trap every point between consecutive
orbit lattice points (which carry constant $g$); squeeze error to zero; cross
the gap region $(0,M]$ via an orbit launched from a small point.
Skeleton:
  1. Exhibit family $f(x)=x+c$ — by direct substitution (classical QM-AM-GM chain for $(x,y+c)$).
  2. Derive orbit invariance, $g\ge0$, master squeeze — by $x=f(y)$ tight point + SOS.
  3. Prove $f$ monotone nondecreasing — by squeeze + $g\ge0$ (KEY GAP).
  4. Trap every point between orbit lattice points — by monotonicity sandwich; orbit carries constant $g=\alpha$.
  5. Cross gap region $(0,M]$ — by small-$y$ orbit descent + squeeze + monotonicity (GAP).
  6. Conclude $g\equiv c\ge0$ — by global constancy.
  7. Verify family — by substitution.
Key lemmas:
  - Orbit invariance $g(f(y))=g(y)$ — because the window collapses to a point at $x=f(y)$, forcing the middle to equal the AM.
  - $g\ge0$ — because $g(y)<0$ makes the orbit $y+n g(y)$ eventually negative, contradicting $f>0$.
  - Monotonicity of $f$ (UNPROVED) — because the squeeze forces local agreement near image points and $g\ge0$ rules out inversions.
  - Lattice trap — because the orbit is an AP carrying constant $g$ and a monotone $f$ pins intermediate points.
Open gaps: step 3 (monotonicity — load-bearing); step 5 (gap region crossing).
Cases: $c=0$ (zero-mesh orbit, fixed point); $c>0$ (positive-mesh AP); gap region.
Watch out for: $f\ge\mathrm{id}$ alone does NOT imply monotone; the squeeze must drive it; orbit mesh may be large so check squeeze constants.
Nomination: new (founding). Primary structural route.

### density-contradiction: new
Target: full characterization; proves uniqueness by contradiction.
Technique: Kronecker equidistribution of incommensurate arithmetic orbits —
GENUINELY DIFFERENT framing (number-theoretic/dynamical, avoids monotonicity and
global continuity). Assume two points with $g(a)=\alpha\ne\beta=g(b)$; their
forward orbits are APs with incommensurate (or commensurate) steps; density
forces one orbit into the quadratic-squeeze neighborhood of an image point of
the other, where $g$ is pinned, contradicting distinct values.
Skeleton:
  1. Exhibit family — by substitution.
  2. Derive orbit invariance, $g\ge0$, master squeeze, local continuity at image points — by tight point + SOS.
  3. Assume nonconstant $g$; pick witnesses $g(a)=\alpha\ne\beta=g(b)$ — by contradiction hypothesis.
  4. Irrational $\alpha/\beta$: Kronecker density makes the $B$-orbit land near $A$-image points where squeeze forces $g=\alpha$, contradicting $g=\beta$ on $B$ — by Kronecker/Weyl equidistribution (KEY GAP, main case).
  5. Rational $\alpha/\beta=p/q$: commensurate cosets — separate kill via squeeze-forced intermediate $g$-value producing an irrational third orbit, reducing to case 4 (KEY SUB-GAP).
  6. Conclude $g$ constant $=c\ge0$ — by contradiction (cases 4–5 exhaustive).
  7. Verify family — by substitution.
Key lemmas:
  - $g$ continuous at every image point with value $g(y)$ — because the master squeeze $\to0$ as $x\to f(y)$.
  - Each orbit carries a single $g$-value — because $g(f(y))=g(y)$ iterated.
  - Irrational-ratio orbits mutually dense (Kronecker) — because $\{n\beta\bmod\alpha\}$ is dense when $\alpha/\beta$ irrational.
  - Rational-ratio coset kill (UNPROVED) — because disjoint commensurate cosets must be broken by the squeeze forcing intermediate $g$-values.
Open gaps: step 4 (squeeze-neighborhood landing; ensure squeeze constant finite at the landing image point); step 5 (commensurate sub-case — conjectural mechanism).
Cases: irrational ratio (main); rational ratio (sub-case); one value $=0$ (zero-step orbit, still covered).
Watch out for: Kronecker density holds one-sided ($n\ge0$) — confirm; squeeze constant grows at very small image points; do NOT assume $g$ continuous everywhere — only at image points.
Nomination: new (founding). Genuinely different framing (no monotonicity needed).

### extremal-infimum: new
Target: full characterization.
Technique: extremal infimum / attainment argument (analysis + order). Let
$m=\inf g\ge0$; split on whether $m$ is attained; the squeeze propagates the
minimal value to neighborhoods of image points; the $m$-orbit is cofinal
covering a ray; then drag constancy across the gap region. Once $g\equiv m$,
the master inequality is automatic ($0\le(x-f(y))^2$), so every $m\ge0$ is
admissible — no separate pinning of $m$ needed.
Skeleton:
  1. Exhibit family — by substitution.
  2. Derive orbit invariance, $g\ge0$, master squeeze — by tight point + SOS.
  3. Set $m=\inf g\ge0$ — by $g\ge0$.
  4. Case $m$ attained at $y_*$: $m$-orbit carries $g\equiv m$; squeeze propagates $g=m$ to neighborhoods of each orbit image point; sub-case $m=0$ (fixed point, open-$g=0$ set + connectedness); sub-case $m>0$ (positive-mesh cofinal AP covers a ray).
  5. Case $m$ not attained: take $g(y_n)\to m$; squeeze at $f(y_n)$ propagates $g\to m$; chain cofinal neighborhoods (KEY GAP).
  6. Cross gap region $(0,M]$ — small-$y$ orbit descent: $y_\epsilon\downarrow0$, $g(y_\epsilon)\to m$, squeeze near $f(y_\epsilon)$ pins $g=m$ on $(0,\delta)$, chain up (LOAD-BEARING GAP; the naive large-image limit is a TRAP — bound grows, do not use).
  7. Conclude $g\equiv m\ge0$ — by cases 4–6.
  8. Verify family — by substitution.
Key lemmas:
  - $m=\inf g\ge0$ exists — because $g\ge0$.
  - $m$-orbit (or near-$m$-orbit) carries $g\equiv m$ (or $\to m$) — because $g$ is constant on forward orbits.
  - Squeeze propagates $g=m$ to neighborhoods of image points — because $|g(x)-g(y)|\le(x-f(y))^2/(2x+2y)\to0$ as $x\to f(y)$.
  - Cofinal coverage (UNPROVED) — orbit/near-minimizer image points cofinal + squeeze neighborhoods with positive radius chain to a ray.
  - Gap-region crossing (UNPROVED) — large-image limit is wrong-direction; small-$y$ descent is the candidate mechanism.
Open gaps: step 5 (non-attained cofinal coverage); step 6 (gap region — the large-image trap is explicitly flagged wrong; small-$y$ descent is load-bearing).
Cases: $m$ attained ($m=0$ fixed point; $m>0$ positive mesh); $m$ not attained; gap region.
Watch out for: the large-image limit $(x-f(y))^2/(2x+2f(y))\sim f(y)/2\to\infty$ is a TRAP — do not claim it pins small-$x$; $m=0$ does not imply $g\equiv0$ without attainment; no global continuity assumed.
Nomination: new (founding). Distinct route via infimum/attainment (no monotonicity, no density).

### master-sos-identity: new (lower-confidence, lemma-provider fallback)
Target: full characterization via a direct algebraic kill from the master
inequality; honest fallback is the certifiable master-inequality lemma.
Technique: SOS / completing-the-square + direct algebraic manipulation. The two
gap squares satisfy $U+L=(x-f(y))^2/2$ and $U-L=-(g(x)-g(y))(g(x)+g(y)+2x+2y)/2$;
both $\ge0\iff |g(x)-g(y)|(g(x)+g(y)+2x+2y)\le(x-f(y))^2$ (master inequality
$(*)$). Attempt to show $(*)$ + $g\ge0$ alone force $g$ constant.
Skeleton:
  1. Exhibit family — by substitution (for $g\equiv c$, $(*)$ is $0\le(x-y-c)^2$, automatic).
  2. Establish $g\ge0$ — by orbit forward-positivity.
  3. Derive master inequality $(*)$ — by SOS identity (knowledge_base: SOS/completing-the-square).
  4. Direct-kill attempt (KEY CONJECTURAL GAP):
     (a) swapped two-window intersection: $|g(x)-g(y)|\le\min((x-f(y))^2,(y-f(x))^2)/(g(x)+g(y)+2x+2y)$ — PROVEN refinement.
     (b) simultaneous-small fixed-point: $x=f(y)$ AND $y=f(x)\iff g(x)=g(y)=0$; near-simultaneous collapse would force near-zero disparity (CONJECTURAL — no IVT without continuity).
     (c) optimization bound: min $\le((g(x)+g(y))/2)^2$ giving $|g(x)-g(y)|\le(g(x)+g(y))^2/(4(g(x)+g(y)+2x+2y))$ — bound, not kill.
  5. If kill closes: $g\equiv c\ge0$, done. If not: certifiable output is the master-inequality lemma $(*)$ (importable by the other three); compete at lower Elo.
  6. Verify family — by substitution.
Key lemmas:
  - Master SOS identity — by direct polynomial expansion of $U,L$ (verified symbolically).
  - Master inequality $(*)$ — because $U,L\ge0\iff U+L\ge|U-L|$; factor positive under $g\ge0$.
  - Swapped two-window min (PROVEN) — by applying $(*)$ to $(x,y)$ and $(y,x)$.
  - Direct kill from min/simultaneous collapse (CONJECTURAL) — existence of a parametric/fixed-point pair driving disparity to zero is unproved; no continuity for IVT.
Open gaps: step 4 (the direct algebraic kill — conjectural; the min bound is only an inequality; simultaneous collapse needs a fixed-point existence result without continuity).
Cases: $g\equiv0$; $g\equiv c>0$; nonconstant $g$ (kill target).
Watch out for: do NOT overclaim the direct kill (explorers conjectured but did not prove); orbit amplification GROWS the bound (forward orbit RHS $\sim n^2$) — do not use; honest value is the master-inequality lemma.
Nomination: new (founding). Lowest-confidence route but distinct (pure algebraic); its certifiable lemma feeds the others.

---

## Field summary for the outline-reviewer

Four founding approaches, each a whole solution to the characterization,
diverse in framing:

| slug | framing | load-bearing gap | confidence |
|---|---|---|---|
| orbit-monotonicity-sandwich | monotonicity + AP lattice trap (aimo-0234) | monotonicity of $f$; gap-region crossing | medium-high (primary structural route) |
| density-contradiction | Kronecker equidistribution (no monotonicity) | squeeze-neighborhood landing; commensurate sub-case | medium (genuinely different, handles commensurability hardest) |
| extremal-infimum | infimum/attainment descent | non-attained cofinal coverage; gap-region (large-image trap flagged) | medium |
| master-sos-identity | pure algebraic SOS direct kill | direct kill conjectural | low (but certifiable master-inequality lemma feeds the field) |

Shared wall (the single-gap trap to watch): all four ultimately need to cross
the **gap region** $(0,M]$, $M=\inf\mathrm{image}(f)$ — points not in
$\mathrm{image}(f)$ where the squeeze does not directly apply. Each approach
has a DIFFERENT mechanism for it (monotonicity trap / density landing /
small-$y$ descent / simultaneous-collapse fixed point), so they do NOT share
one wall — the field is genuinely diverse. If two or more collapse to the same
gap-region mechanism in a later round, the outliner should reframe.

Shared certifiable lemma (propose to the reviewer to certify once any builder
proves it): the **master squeeze** $|g(x)-g(y)|(g(x)+g(y)+2x+2y)\le(x-f(y))^2$,
derived from the SOS identity — load-bearing for all four approaches.

Dead ends already recorded (do not revisit): "$f(x)/x$ constant"; "$g$
additive/Cauchy"; $x=y$ and $y=f(x)$ substitutions; pure large-$x$ asymptotics;
orbit amplification along the master inequality (bound grows, useless).

Build set (suggestion for the outline-reviewer): all four are new founding
approaches; dispatch one builder per slug. The master-sos-identity builder
should prioritize deriving and certifying the master-inequality lemma (its
certain value) and attempt the direct kill as a stretch.
