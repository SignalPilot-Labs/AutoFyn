## Box-Corner $\times$ Tail-Chamber-Vertex Decomposition — Refuted (round 22, negative result)

**Context.** Case (b2) of the general upper bound (the region $p_1<T/2$,
$T/D_n<p_2<a_nT/2$, the sole remaining open region of $c(n)\le a_nT$) has
resisted eight prior mechanism families (peel/bisect/recurse,
weighted-combination, boundary-continuity, Danskin/concavity,
surrogate-adversary/majorization, constraint-side LP duality,
probabilistic-method wrapper, and the round-21 rank-pigeonhole-style
worst-tail mechanism / convex-combination futility). Round 22's numeric
scan of near-worst witnesses noted that the two on-file near-tight
witnesses (round 14, $n=3,4$) both have $(p_1,p_2)$ fairly close to the
box's own corner ($p_1\to T/2^-$, $p_2\to a_nT/2^-$), suggesting a
dimension-reduction conjecture: **the worst case-(b2) witness has
$(p_1,p_2)$ pinned exactly at the box corner, with only the tail
coordinates $(p_3,\dots,p_m)$ contributing a genuine chamber-vertex
search** (reducing case (b2) to a search over the tail alone, via
`vertex-minimum-theorem`-style tie/pin constraints restricted to the tail
pieces).

**This lemma records that the conjecture is false**, refuted by direct
computation (floating point, then cross-checked with exact `Fraction`
arithmetic) at both $n=3$ and $n=4$.

### The required condition for the decomposition to hold

For the decomposition to be a valid dimension reduction, the margin
$a_nT-\Phi_{\min}(p)$ minimized over case (b2)'s whole box would need to
equal the margin minimized only along the corner slice
$\{p_1=T/2^-,\ p_2=a_nT/2^-\}$ (varying the tail alone). Equivalently: no
point of the box with $(p_1,p_2)$ strictly away from the corner may have a
smaller margin than every corner-slice point.

### Direct refutation: off-corner witnesses beat the corner slice

**Method.** `/tmp/round-22/b2_corner_decomposition_test.py`: for fixed $n$,
$\Phi_{\min}(p)$ is computed by exhaustively enumerating every legal cut
composition (finite for fixed $n$) and locally optimizing the continuous
fragment split within each composition via multi-restart Nelder–Mead
(reusing the established methodology of round 14's §R14.3 and round 20's
gates 5a/5b, re-implemented and independently re-verified rather than
assumed correct — see the exact cross-check below). Two samplers: an
unrestricted sampler over the whole open box, and a corner-restricted
sampler pinning $p_1=T/2-\varepsilon$, $p_2=a_nT/2-\varepsilon$
($\varepsilon=2\times10^{-3}$) with only the tail varying.

**Results.**

| $n$ | best margin, unrestricted box scan | best margin, corner-restricted scan |
|---|---|---|
| 3 | $0.020560$ (witness $\approx(0.468,0.253,0.170,0.109)$, comp $(1,1,0,0)$) | $0.031333$ (comp $(2,0,0,0)$, tail-independent) |
| 4 | $0.010345$ (witness $\approx(0.387,0.195,0.181,0.156,0.082)$, comp $(1,0,0,2,0)$) | $0.014129$ (comp $(3,0,0,0,0)$, tail-independent) |

At both $n$, the unrestricted search finds a **strictly smaller** margin
(a genuinely worse witness for the target inequality) than the best margin
achievable anywhere on the corner-restricted slice — directly contradicting
the conjecture, which requires the corner slice to contain the overall
worst case. Re-run with restarts increased from 4 to 10 at $n=3$
reproduces the same qualitative gap (unrestricted best $0.020533$ vs.
corner best $0.031287$–$0.031333$), ruling out optimizer noise as the
explanation.

**Exact-`Fraction` cross-check (independent of floating point).** The
$n=3$ unrestricted witness's own composition $(1,1,0,0)$ was independently
re-optimized by an exact rational $80\times80$ grid search over its two
free split parameters (no floating point):
$$p=(4682,2531,1696,1091)/10000,\qquad
\Phi_{\min}^{\text{grid}}=\frac{641}{1250}=0.5128,\qquad
\text{margin}=\frac{77}{3750}=0.02053\overline3,$$
matching the Nelder–Mead value to full precision. The same exact-grid
method, applied independently to the on-file round-14 near-tight witness
$p=(4468,2591,2251,691)/10001$ (composition $(1,0,1,0)$), gives exact
minimum $5159/10001$, margin $2623/150015=0.0174849\ldots$, again matching
the established value — validating the computational pipeline before
trusting its verdict on the corner-vs-off-corner comparison.

### Honest conclusion

The box-corner $\times$ tail-chamber-vertex decomposition is **false as
stated**: worse (smaller-margin) witnesses exist with $(p_1,p_2)$ strictly
away from the box corner, at both $n=3$ and $n=4$. This rules out the
specific dimension-reduction shortcut — it does **not** invalidate
`p-space-chamber-vertex-theorem` (unconditional, general-position) or any
other certified result; it only means a future attempt at the finite
extreme-point evaluation those theorems make well-posed must search the
*full* chamber-vertex family across the whole box, not a corner-restricted
slice. This is the ninth confirmed-dead route into case (b2) — should not
be re-attempted under a new name. (Note: `p-space-chamber-vertex-theorem`
is conditional, not unconditional-general-position as this sentence
originally implied — see that lemma's own reviewer correction note,
round 22.)

## Certification note (proof-reviewer, round 22)

**CERTIFIED.** Independently re-implemented the $n=3$ comparison from
scratch with a differently-parameterized continuous optimizer (sigmoid-
reparameterized split ratios, Nelder-Mead, 12 restarts per composition,
`/tmp/round-22/verify_lpd_r22b.py` -- not the builder's own script) and
the correct game quantity Phi_min = (alternating-sum + T)/2 (verified this
transform against the builder's own worked n=3 example, tau-star's closed
form, exact match): unrestricted-box witness Phi_min ~ 0.5128, margin ~
0.02053; corner-restricted witness Phi_min ~ 0.5020, margin ~ 0.03133 --
matching the builder's reported values to full precision and confirming
margin(unrestricted) < margin(corner), i.e. the corner is genuinely not
the worst case. Also independently re-verified the two cited exact-
`Fraction` values (641/1250 and 5159/10001) against a_3 = 8/15 by exact
rational arithmetic. No gap found; refutation is correct and honestly
scoped (explicitly limited to n=3,4, not claimed general).
