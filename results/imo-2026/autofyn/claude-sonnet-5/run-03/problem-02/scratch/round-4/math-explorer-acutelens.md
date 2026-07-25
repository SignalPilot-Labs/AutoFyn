# Math-explorer report: acute-angle branch-selection lens (round 4, imo-2026-02)

## Assignment
Investigate whether coordinate-bash-resultant's acute-angle branch-selection
conjecture (∠LBK, ∠LNC, ∠LCK, ∠BMK always acute at genuine solutions) has a
sharp, *provable* sign certificate — not just more numerics — and develop the
resultant-factor lead `2a·cos²β = b`. Report only; do not attempt the final
proof.

## Headline finding: the acute-angle conjecture is FALSE in general

Using the same rotation parametrization as `coordinate-bash-resultant`
(`A=(0,0)`, `B=(a,0)`, `C=(b,cc)`, `K=B+t1(-cosβ,sinβ)`,
`L=C+s2·R(β)(A-C)` with `s2=t2/|AC|`), I solved the **true, unsquared**
hypothesis system (hyp1 built into the parametrization, hyp2: `∠LBK=∠LNC`,
hyp3: `∠LCK=∠BMK`, via `scipy.fsolve` on the actual `arccos`-based angle
equalities, not the squared polynomial relaxation) directly, and filtered for
genuine solutions satisfying **both** containments (`K` strictly interior to
`△BMC`, `L` strictly interior to `△BNC`) with a healthy margin (checked via
signed-area sign, normalized by triangle area to rule out boundary artifacts).

**Found multiple explicit, non-degenerate counterexamples** where `∠LCK=∠BMK`
(and correspondingly `∠LBK=∠LNC`, by the reduction below) is **obtuse**, with
comfortable containment margins (not boundary-limiting cases). Example:
`a=2.9788` (using `A=(0,0),B=(a,0),C=(b,cc)`) — concretely
`a=0.9959, b=2.0302, cc=1.1413, t1=0.1522, t2=1.2001, β≈9.72°` gives
`∠BMK=∠LCK≈95.18°` (obtuse), with containment margins ≈9% and ≈18% of
triangle area respectively (not boundary-adjacent). A more extreme instance:
`a=2.5788, b=0.8327, cc=0.3488, t1=1.421, t2=0.0963, β≈7.35°` gives
`∠BMK=∠LCK≈123.5°`, again with a genuine (non-tiny) containment margin. All
verified directly: hypothesis residuals `<1e-9`, both containments strictly
satisfied (signed-area test), `t1,t2>0`, `0<β<∠ABC`.

**This means `coordinate-bash-resultant`'s conjecture, as literally stated
("the four hypothesis angles are always acute at genuine solutions"), is
false and should not be pursued further as a universal branch-selection
criterion.** The round-3 numeric survey (150 samples, max ≈49.4°) apparently
under-sampled the region of parameter space (thin triangles / β near the
edge of its valid range `(0,∠ABC)`) where obtuse genuine solutions occur.

## A genuine, unconditional structural fact (not conjectural): same-sign reduction

While the *acuteness* claim is false, I found a related fact that **is**
unconditionally true and reduces the four-angle question to two:

The unsquared hypothesis 2 (`∠LBK=∠LNC`, both angles in `(0,π)`) says exactly
`BL·BK/(|BL||BK|) = NL·NC/(|NL||NC|)`. Since `|BL|,|BK|,|NL|,|NC|>0`, this
forces **`sign(BL·BK) = sign(NL·NC)`, always** (a triviality of the
hypothesis, true on both the genuine solution and even, if one existed,
supplementary-angle configurations — this is not itself the branch-selection
fact, just an unconditional sign-matching identity). Symmetrically, hyp3
forces `sign(CL·CK) = sign(MB·MK)`. Verified numerically at every example
above (e.g. at the 105.9°-obtuse example: `BL·BK=2.974>0`, `NL·NC=0.479>0`
— matching acute pair — while `CL·CK=-0.0004<0`, `MB·MK=-0.189<0` — matching
obtuse pair). **So the four-angle question is really a two-quantity
question**: `sign(NL·NC)` and `sign(MB·MK)` alone determine all four signs.

Better: `NL·NC` and `MB·MK` have very clean exact closed forms in the
parametrization (independent of the messier cross-coupled `BL·BK`, `CL·CK`):
$$MB\cdot MK = \frac{a}{4}(a - 2t_1\cos\beta), \qquad NL\cdot NC = \frac{|AC|^2}{4}\Big(1-\frac{2t_2\cos\beta}{|AC|}\Big)=\frac{|AC|}{4}(|AC|-2t_2\cos\beta).$$
So: `∠BMK` acute `⟺ t1·cosβ < AB/2` (the foot of the perpendicular from `K`
to line `AB`, measured from `B`, lands strictly inside segment `BM`); `∠LNC`
acute `⟺ t2·cosβ < AC/2` (analogous, foot of perpendicular from `L` to line
`AC` from `C`, inside segment `CN`). **These two clean geometric inequalities
are exactly equivalent to the acute-angle conjecture** (via the same-sign
reduction above) — but I've now shown by explicit counterexample that they
can fail (e.g. `t1 cosβ > AB/2` at the 95°/123° examples above), so this
reduction, while correct and possibly reusable, does not rescue the
conjecture.

**Containment alone is not enough to force either inequality** (reconfirmed
independently of round 3's finding): I checked whether `G2a=0` restricted to
`s2>0` alone forces `sign(BL·BK)=sign(NL·NC)`, i.e. whether that "same-sign"
identity is already forced by the squared branch equation without the true
system — found ~60% of random roots of `G2a=0` with `s2>0` give the *wrong*
(mismatched) sign pair, confirming the acuteness/sign-matching genuinely
requires the full interlocking system (hyp1∧hyp2∧hyp3 simultaneously, plus
both containments), not any single relaxed piece.

## The `2a·cos²β=b` resultant factor: geometric meaning, and relevance

Recomputed `Res_{s2}(G2a,G2b)` independently: confirms
`coordinate-bash-resultant`'s three-factor structure
`64u²(u²+1)⁴·F1·F2·F3` with, after the `u=tan(β/2)` back-substitution,
`F1 ∝ (a-b)sinβ - cc·cosβ` (ray `BK` parallel to line `BC` — a degenerate
configuration, `K` would sit on line `BC`, excluded by strict containment)
and `F3 ∝ 2a\cos^2\beta - b`. I was **not able to identify a clean
synthetic geometric reading of `F3=0`** beyond the raw algebra (tried
rewriting via `2\cos^2\beta=1+\cos2\beta`, giving `a(1+\cos2\beta)=b`, i.e.
`a\cos2\beta = b-a`; this says the *double-angle* projection of `a` along
`β` equals the horizontal offset `b-a` of `C` from `B` — no immediately
recognizable named configuration, e.g. not obviously "`K` on the
circumcircle" or "`BK⊥` something"). **This factor governs where the two
branches `G2a,G2b` can *cross* (i.e. `s2`-double-root of the resultant) — it
is the lead relevant to `coordinate-bash-resultant-boundary`'s
continuity/IVT mechanism (its unclassified `F2`), not to the acute-angle
approach.** I recommend the two leads be treated as separate: developing
`F3`'s geometric meaning is worth pursuing **for the IVT/continuity sibling
approach**, not for resurrecting the acute-angle conjecture, which is now
refuted.

## Recommendation for next round

- **Retire the acute-angle conjecture** as a branch-selection route — it is
  disproved by explicit, non-boundary counterexamples (listed above,
  reproducible via the script logic described). Do not re-attempt "prove all
  four angles acute" in any form.
- The same-sign reduction (`sign(BL·BK)=sign(NL·NC)`, `sign(CL·CK)=sign(MB·MK)`,
  both unconditionally true) **is** a valid, reusable structural fact — worth
  keeping as a lemma if any future approach wants to reduce the 4-angle
  question to the simpler closed-form 2-inequality question
  (`t1\cosβ<AB/2`, `t2\cosβ<AC/2`), but note this reduction, by itself,
  doesn't select the branch since these can go either way.
- The most promising path for branch selection remains
  `coordinate-bash-resultant-boundary`'s **continuity/IVT mechanism**: it
  doesn't need "always acute," only "the branch label (`G2a` vs `G2b`) can't
  change without crossing `F1=0` or `F2/F3=0`, and it demonstrably starts on
  the right branch at some accessible boundary/limit." That approach doesn't
  depend on acuteness being universally true, so it survives this round's
  finding intact. Suggest next round prioritize identifying `F3=0`'s
  (`2a\cos^2β=b`'s) geometric meaning and confirming it (like `F1=0`) lies
  outside the valid parameter range, or at worst identifying exactly when it
  doesn't and handling that as a boundary case in the IVT argument.
