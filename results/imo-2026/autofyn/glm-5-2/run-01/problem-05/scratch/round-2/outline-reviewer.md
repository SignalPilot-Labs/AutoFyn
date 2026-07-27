# Outline review — IMO 2026 P5 (founding field, round 2)

All four skeletons reviewed before any proof effort. The shared
load-bearing lemma — the **master squeeze**
$|g(x)-g(y)|(g(x)+g(y)+2x+2y)\le(x-f(y))^{2}$ from the SOS identity
$U+L=(x-f(y))^{2}/2$, $U-L=-(g(x)-g(y))(g(x)+g(y)+2x+2y)/2$ — was
verified symbolically (both halves match exactly). The candidate family
$f(x)=x+c$ passes for $c\in\{0,0.5,1,3,100\}$; the perturbation
$f=x+1+0.3\sin x$ fails (2164 violations), confirming the forcing is
real and that monotonicity-type rigidity is genuinely implied by the
hypotheses. No approach rests on a recorded dead end ($x=y$ / $y=f(x)$
tautologies, "$f(x)/x$ constant", "$g$ additive/Cauchy", pure
large-$x$ asymptotics, orbit amplification along the master inequality).

The field is genuinely diverse: each approach crosses the shared hard
wall — the **gap region** $(0,M]$, $M=\inf\mathrm{image}(f)$ — by a
*different* mechanism (monotonicity trap / Kronecker landing /
small-$y$ descent / simultaneous-collapse fixed point). Not a
single-gap field; do not collapse.

---

## orbit-monotonicity-sandwich — APPROVE

Sound aimo-0234 template transfer (iterate identity → AP lattice →
monotonicity sandwich), a whole attempt at the characterization,
honestly flagged gaps. The shared derived facts (orbit invariance,
$g\ge0$, master squeeze) are correct and re-derived from scratch.

- **Step 3 (monotonicity of $f$) — load-bearing gap.** The mechanism is
  vague ("apply squeeze with $y$ near both image points"; "$g\ge0$
  rules out inversions"). $f\ge\mathrm{id}$ alone does NOT imply
  monotone (correctly noted in "watch out for"). The builder must give
  a *concrete* argument: e.g. for $x_1<x_2$ with $f(x_1)>f(x_2)$,
  exhibit the specific squeeze pair that yields a numerical
  contradiction, or substitute a weaker trapping condition (local
  bounded variation / Lipschitz on the orbit mesh) that suffices for
  the lattice sandwich. The perturbation failure supports that some
  rigidity is forced — make the mechanism explicit, do not leave it
  as "the squeeze forces it."
- **Step 5 (gap region).** Mechanism (orbit launched from small
  $y_\varepsilon\downarrow0$) is plausible but the limit
  $g(y_\varepsilon)\to g(0^{+})$ is unjustified without a small-$y$
  estimate; flag for the builder to justify or replace.
- Cases ($c=0$ fixed point, $c>0$ positive mesh, gap region) are
  disjoint and cover the conclusion; exhibit + uniqueness both present.

Approved; builder should make the monotonicity mechanism concrete
rather than gestural.

## density-contradiction — APPROVE

Genuinely different framing (number-theoretic/dynamical, no monotonicity
or global continuity). The **irrational-ratio main case (step 4) is
rigorous and numerically confirmed**: forward iterates ($n,m\ge0$) of
two incommensurate APs land arbitrarily close, the squeeze denominator
$2x+2y\ge2(a+b)>0$ is bounded below (orbits start positive, forward
iterates keep them positive), so RHS $\to0$ and $\alpha=\beta$. Verified
directly: for $\alpha/\beta$ irrational the best squeeze RHS reached
$\sim10^{-11}$ while $|\beta-\alpha|\approx0.59$, a clean contradiction.

- **Step 4 caveat (resolved).** One-sided Kronecker ($n\ge0$) gives
  density mod $\alpha$; since $n\beta\to\infty$, the matching $m\ge0$
  exists — confirmed. The squeeze constant does NOT blow up (denominator
  bounded below); the "watch out for very large $m$ gives small
  constants" remark is correct and harmless.
- **Step 5 (rational-ratio sub-case) — load-bearing gap.** This is the
  genuine difficulty and is honestly flagged. The "produce an irrational
  third orbit" mechanism is conjectural: the squeeze forces $g$ to
  *approximate* $\alpha$ near $A$-image points and $\beta$ near
  $B$-image points, but approximation does not pin exact values, so an
  irrational-ratio third orbit is not guaranteed to exist. The builder
  must either (a) give a rigorous commensurate-coset kill — e.g. show
  squeeze neighborhoods of the two commensurate lattices overlap (radius
  $\sim\sqrt{\varepsilon\cdot z_{n}}$ grows along the orbit, so for large
  $n$ consecutive-neighborhood overlap is plausible) — or (b) reduce
  the rational case to the irrational one by a concrete perturbation
  argument, not a hand-wave.

Approved; the irrational case is the strong spine, the rational case is
the open gap the builder must close.

## extremal-infimum — CHANGES-REQUESTED

Distinct infimum/attainment framing; the large-image trap is honestly
flagged and correct (verified: RHS $\sim f(y)/2\to\infty$, does not pin
small $x$). But two gaps are **mis-identified** and must be fixed before
building.

- **Step 4(i), $m=0$ attained sub-case — MIS-IDENTIFIED.** The claim
  "the squeeze gives an open $g=0$ neighborhood of $y_{*}$, then
  connectedness" is **false as stated**. The squeeze yields
  $g(x)\le(x-y_{*})^{2}/(2x+2y_{*})$, a *positive* bound (verified:
  $0.05$ at $x=1.5$, etc.), NOT $g(x)=0$. So the squeeze alone gives
  "$g\to0$," not "$g=0$," and no open zero-set follows without an
  extra argument. The builder needs a real mechanism to upgrade
  "attained infimum $0$" to "$g\equiv0$" (e.g. an orbit/iterate
  amplification that drives the positive bound to exactly zero, or a
  different rigidity input). Do not present the connectedness propagation
  as established.
- **Step 6 (gap region) — MIS-IDENTIFIED.** The small-$y$ descent
  assumes $g(y_{\varepsilon})\to m$ as $y_{\varepsilon}\downarrow0$.
  This is **unjustified**: $m=\inf g$ is a global infimum; the
  minimizing sequence need not approach $0$. The builder must either
  justify a small-$y$ lower-envelope estimate or supply a different
  gap-region mechanism (the large-image limit is confirmed a dead end
  here).

Technique is right (infimum/attainment is a legitimate route); the
specific mechanisms are wrong. Revise steps 4(i)-$m=0$ and 6 with real
arguments, then build. Not registered as a primary build this round
(lowest Elo) — return to the outliner for revision of the two
mis-identified mechanisms.

## master-sos-identity — APPROVE

The SOS identity and master inequality are verified symbolically (the
shared lemma is sound). The swapped two-window min
$|g(x)-g(y)|\le\min((x-f(y))^{2},(y-f(x))^{2})/(g(x)+g(y)+2x+2y)$ is a
proven refinement, and the optimization bound
$\min\le((g(x)+g(y))/2)^{2}$ is correct and tight (the two root
intervals touch exactly at $M=((g(x)+g(y))/2)^{2}$). The direct kill is
**honestly** flagged conjectural — the simultaneous-collapse fixed-point
argument has no IVT without continuity, and the min bound is only an
inequality. The approach does not overclaim.

- **Certain deliverable:** the certifiable master-inequality lemma
  $(*)$, load-bearing for the whole field. This is the reason to build
  it this round: whichever builder proves $(*)$ + the SOS identity
  certifies a shared lemma the other approaches import.
- **Stretch (conjectural):** the direct algebraic kill. The builder
  should attempt it but must not present it as proved; if it does not
  close, mark the gap honestly and let the approach compete at lower
  Elo as a lemma-provider.
- **Note:** the approach deliberately does not use $g\circ f=g$ in its
  kill attempt; if the direct kill fails and the builder folds in orbit
  structure, it converges toward the other approaches — flag this so
  the field does not silently collapse to one framing.

Approved; build it for the certifiable lemma (certain value), attempt
the direct kill as a stretch.

---

## Ranking (Elo after this round's head-to-head)

| slug | Elo | rationale |
|---|---|---|
| orbit-monotonicity-sandwich | 1532 | Primary structural route; sound aimo-0234 template; monotonicity gap is the classic hard wall but the perturbation failures support that rigidity is forced. Beats the lemma-provider and the weaker infimum route; draws with density as co-strongest primary. |
| density-contradiction | 1529 | Co-strongest primary; irrational-ratio case is rigorous and numerically confirmed (avoids the unproven monotonicity wall entirely); rational sub-case is the open gap. Beats master-sos and extremal; draws with orbit. |
| master-sos-identity | 1485 | Direct kill honestly conjectural, so its certain value is the certifiable master-inequality lemma (load-bearing for all three others), not a full solution yet. Beats extremal (certain lemma value > extremal's mis-identified gaps); below the two primary bets. |
| extremal-infimum | 1454 | Weakest: two mis-identified mechanisms ($m=0$ "open $g=0$ set" unsupported; small-$y$ descent assumes unjustified $g\to m$ at $0$). Honest large-image-trap flag is correct, but the route needs outliner revision before it can be built competitively. |

Comparisons applied: density > master-sos; orbit > master-sos;
density = orbit (draw, co-strongest primaries); orbit > extremal;
density > extremal; master-sos > extremal.

---

## Build set

Build the two strongest primary bets (orbit-monotonicity-sandwich,
density-contradiction) plus the master-sos-identity route whose certain
deliverable — the certifiable master squeeze
$|g(x)-g(y)|(g(x)+g(y)+2x+2y)\le(x-f(y))^{2}$ as a shared lemma — is
load-bearing for the whole field. Skip extremal-infimum this round
(lowest Elo, mis-identified gaps); return it to the outliner for
revision of the $m=0$-attained and gap-region mechanisms. Three
parallel builders, each owns its own approach file — no collision.

build set: orbit-monotonicity-sandwich, density-contradiction, master-sos-identity
