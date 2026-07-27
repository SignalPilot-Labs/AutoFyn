# Approach: extremal-infimum

## Status
partial

## Target
Prove the full characterization: the solutions are exactly $f(x)=x+c$, $c\ge0$.
Route: let $m=\inf g\ge0$; prove $g\equiv m$ by splitting on whether the infimum
is attained; once $g$ is constant, the constant is automatically $\ge0$ and the
family $f(x)=x+m$ is exactly the candidate family (no separate pinning of $m$
needed, since the master inequality is automatic for $g\equiv m$).

## Technique
Extremal infimum / attainment argument (analysis + order). Uses the
infimum-of-$g$ descent: the squeeze propagates the minimal value to
neighborhoods of image points, and the orbit of a (near-)minimizer is cofinal,
covering a ray; then drag constancy across the gap region.

## Shared derived facts (builder re-derives)
- $g=f-\mathrm{id}$; $g(f(y))=g(y)$; $g\ge0$; orbits $y+n g(y)$ APs;
  master squeeze $|g(x)-g(y)|\le (x-f(y))^2/(2x+2y)$; $g$ continuous at every
  image point with value $g(y)$.

## Skeleton
1. **Exhibit the family** $f(x)=x+c$, $c\ge0$. — by direct substitution.
2. **Establish derived facts** (orbit invariance, $g\ge0$, master squeeze).
   — by tight-point substitution + SOS.
3. **Set $m=\inf_{\Rpos} g\ge0$.** $m$ exists (bounded below by $0$) and
   $m\ge0$. — by step 2 ($g\ge0$).
4. **Case (i): $m$ is attained at $y_*$.** Then $g(y_*)=m$, and the orbit
   $y_*+n m$ carries $g\equiv m$. For any $x$ near an orbit point
   $y_*+n m=f(y_*+nm\text{-predecessor})$ — wait, $f(y_*+n m)$... orbit point
   is $z_n=y_*+nm$, and $f(z_n)=z_n+m$ is the *next* orbit point, an image
   point where the squeeze forces $g\to m$ on a neighborhood. So every
   neighborhood of $z_{n+1}=f(z_n)$ has $g$ close to $m$. — by squeeze at image
   points of the $m$-orbit.
   - **If $m=0$**: $z_n=y_*$ for all $n$ (fixed point); the squeeze at
     $f(y_*)=y_*$ gives $g\to0$ near $y_*$; an open neighborhood of $y_*$
     has $g=0$; propagate by the same argument at each new zero-image point
     (connectedness / interval chaining) to get $g\equiv0$ on $\Rpos$.
   - **If $m>0$**: the orbit $\{y_*+n m\}$ is a cofinal AP with mesh $m$;
     squeeze neighborhoods around each orbit point cover
     $[y_*+\delta,\infty)$ for some $\delta$; $g=m$ on this union. Then extend
     to the gap region $(0,y_*]$.
5. **Case (ii): $m$ not attained.** (KEY GAP.) Take a sequence
   $g(y_n)\to m$. The image points $f(y_n)=y_n+g(y_n)$ have squeeze
   neighborhoods where $g\to g(y_n)\to m$. Need to show these neighborhoods
   cover all of $\Rpos$ (or at least a cofinal ray): use that $y_n+g(y_n)$
   can be chosen cofinal and the squeeze neighborhoods have nonvanishing radius.
   Mechanism: pick $y_n$ with $g(y_n)\to m$ and $y_n$ cofinal (possible since
   $g\ge0$ and orbits are cofinal); the squeeze at $f(y_n)$ gives $g=m$ on
   neighborhoods of arbitrarily large points; chaining yields $g\equiv m$ on a
   ray; then cross the gap region as in case (i). — by squeeze + cofinal
   sequence.
6. **Cross the gap region** $(0,M]$, $M=\inf\mathrm{image}(f)$. (GAP, shared
   with orbit-monotonicity-sandwich.) Constancy is established on a ray
   $[R,\infty)$; extend to $(0,R)$. Mechanism: for any small $x>0$, pick $y$
   with $f(y)=y+g(y)$ large (orbit point) and apply the master squeeze with
   this $x$ and that $y$: $|g(x)-g(y)|\le (x-f(y))^2/(2x+2f(y))$; since
   $f(y)$ can be made arbitrarily large (cofinal orbit) the RHS $\to0$, forcing
   $g(x)=g(y)=m$. — by taking $f(y)\to\infty$ in the squeeze (large-image
   limit).
   - **This large-image limit may be the clean kill for the gap region**: as
     $f(y)\to\infty$, $(x-f(y))^2/(2x+2f(y))\sim f(y)/2\to\infty$ — WAIT, this
     GROWS, not shrinks. Re-examine: the bound grows with $f(y)$. So this
     naive limit does NOT pin $g(x)$. (GAP — the gap-region crossing is the
     real obstruction; the large-image limit is wrong-direction. Must use a
     different mechanism: small $y$ orbit, or the attained-minimizer orbit
     extended downward.)
7. **Conclude $g\equiv m\ge0$**, i.e. $f(x)=x+m$. — by cases 4–6.
8. **Verify.** — by substitution (step 1). Note: for $g\equiv m$, the master
   inequality $0\le(x-f(y))^2$ is automatic, so every $m\ge0$ is admissible —
   no need to pin $m$ further.

## Key lemmas (claim + mechanism)
- **$m=\inf g\ge0$ exists** — because $g\ge0$ on $\Rpos$.
- **The $m$-orbit (or near-$m$-orbit) carries $g\equiv m$ (or $\to m$)** —
  because $g(f(y))=g(y)$ makes $g$ constant on each forward orbit.
- **Squeeze propagates $g=m$ to neighborhoods of image points** — because
  $|g(x)-g(y)|\le(x-f(y))^2/(2x+2y)\to0$ as $x\to f(y)$, so $g(x)\to g(y)=m$.
- **Cofinal coverage (UNPROVED)** — because the orbit/near-minimizer image
  points are cofinal and squeeze neighborhoods have positive radius; the
  chaining to a full ray is the open step.
- **Gap-region crossing (UNPROVED)** — because the naive large-image limit
  gives a *growing* bound; a downward-extended orbit or a trapping argument is
  needed. Flagged honestly.

## Open gaps
- **Step 5 (non-attained case)**: ensuring the near-minimizer squeeze
  neighborhoods cover a cofinal ray with enough overlap to chain.
- **Step 6 (gap region)**: the naive large-image limit is wrong-direction
  (bound grows). Need a genuine mechanism to drag constancy down to $(0,M]$.
  Candidate: launch an orbit from an arbitrarily small $y_\epsilon\downarrow0$;
  $g(y_\epsilon)\ge m$ and the squeeze near its image points; let
  $y_\epsilon\to0$ and use $g(y_\epsilon)\to m$ (since $m=\inf g$) to pin
  $g$ on $(0,\delta)$, then chain up. This is the load-bearing sub-gap.

## Cases to cover
- $m$ attained (sub-case $m=0$ fixed point; sub-case $m>0$ positive-mesh AP).
- $m$ not attained (near-minimizer sequence).
- Gap region $(0,M]$.

## Watch out for
- The large-image limit is a TRAP: $(x-f(y))^2/(2x+2f(y))\sim f(y)/2\to\infty$.
  Do not claim it pins small-$x$ values — it does not. The gap-region crossing
  needs a different (small-$y$ / downward) mechanism.
- $m$ may be $0$ even if $g$ is not identically $0$ yet — attainment matters.
- No continuity is assumed globally; only at image points (via the squeeze).

## Approaches tried
- (round 2, founding) Extremal infimum / attainment. Open gaps: cofinal
  coverage in the non-attained case; gap-region crossing (the large-image limit
  is wrong-direction; need a small-$y$ descent).
