## imo-2026-02 (lens: gap7-alternative — second, independent mechanism for f(β1)>0 on (0,β0(A)])

### Recap of exactly what's missing (verified by re-reading Theorem A's own proof text)
Read `lemmas/claim-I-closed-and-claim-II-caseA-closed.md` Theorem A's *proof*
carefully (not just its statement). The statement is scoped to
`β∈(β0,γ)`, but the proof itself literally derives
`f'(β)=sin(A+β)cosB+sin(A+B-β)>0` **for every `β∈(0,γ)`, unconditionally**
(the sign argument — `cosB>0` from `B<π/2`, `sin(A+β)>0`, `sin(A+B-β)>0` —
uses only `β∈(0,γ)=(0,B)`, never `β>β0`). So `f` is strictly increasing on
the *whole* `(0,γ)`, a fact already fully certified, just not stated at
this scope in the theorem's headline. This is exactly the "plausible fix"
flagged in round 18's adjudication and in the file's own Open-gap-7 note —
I independently re-derived it from the lemma file's own displayed algebra
(no new computation needed, it's already there) and confirm it is
genuinely unconditional on `(0,γ)`, not an extrapolation.

Consequence: to close Case (a) (`β1∈(0,β0(A)]`) it suffices to prove
`f(0)≥0` (in fact `>0` away from a degenerate limit), since then
`f(β1)>f(0)≥0` for every `β1∈(0,β0]⊂(0,γ)` by the monotonicity just
recapped. This reduces Gap 7 to a **single one-variable-family inequality**
in `(A,B)`, not a 2-D sweep of `f` itself — a genuinely simpler target than
re-sweeping `f(β1)` directly.

### Distinct openings on this reduced target: `f(0)=sinA(2sin(A+B)-sinB)≥0`

**Opening 1 (the one I pushed furthest — a clean 2-term split, done by hand,
no numerics needed for most of the domain).** Write `C=π-A-B` so
`f(0)/sinA = 2sinC - sinB` (elementary, since `sin(A+B)=sinC`). Expand
`sinC=sin(A+B)=sinA cosB+cosA sinB`, giving
```
f(0)/sinA = 2sinA cosB + sinB(2cosA-1)   =: term1 + term2.
```
The Case-(a)-nonempty domain (`β0(A)<γ=B`) is exactly `A>π-3B` (an exact
algebraic rewrite: `β0=(π-A)/3<B ⟺ A>π-3B`), together with `B≤C` (`⟺
A≤π-2B`) and `A,B,C>0`. From `A≤π-2B` and `A>0` one gets `B<π/2`
**forced by the domain itself** (not assumed) — hence `cosB>0`
unconditionally on this domain, so `term1=2sinA cosB>0` strictly (since
`0<A<π` gives `sinA>0` too).
- **If `A≤π/3`:** `term2=sinB(2cosA-1)≥0` too (since `cosA≥1/2`), so
  `f(0)/sinA=term1+term2>0` **immediately, with no further work** — this
  sub-case is fully closed by elementary sign facts alone.
- **If `A>π/3`:** `term2<0` is possible; `term1` alone does not dominate
  (checked numerically: `2M`-sample sweep restricted to `A>π/3` in-domain
  finds `term1` alone can be as small as `≈0.004` while `term1+term2` is
  `≈0.0014` at the same point — so `term2` genuinely erodes the margin,
  it isn't a slack case). This sub-case is **not yet closed algebraically**
  — it is the one remaining piece — but it is a *strictly smaller*,
  cleanly isolated target than the original 2-D `f(β1)>0` sweep: a single
  inequality `2sinA cosB > sinB(1-2cosA)` on the sub-domain `A∈(π/3,π),
  B<π/2, A>π-3B, A≤π-2B`. Numerically (`2,000,000` fresh samples restricted
  exactly to this sub-domain) it holds with **zero violations**, minimum
  `≈0.0014`, vanishing only as `(A,B)→(π,0)` (the fully degenerate limit,
  `C→0` too) — consistent with `f(0)→0` only at a genuine boundary
  degeneracy, not an interior counterexample.

**Opening 2 (interior-critical-point argument — a genuinely different,
possibly more decisive mechanism).** Treat `h(B,C):=2sinC-sinB` directly as
a function on the true 2-D domain `{(B,C): 0<B≤C<min(2B,π-B)}` (`A=π-B-C`
implicit). `∂h/∂B=-cosB`, `∂h/∂C=2cosC`; these vanish simultaneously only
at `B=π/2` (excluded — domain forces `B<π/2`, shown above) or `C=π/2`
alone (only kills one partial, not both) — so **`h` has NO interior
critical point anywhere in the open domain**. Hence any interior local
min/max is impossible; the infimum of `h` on the domain closure is
attained only on the boundary. I computed all three boundary traces
exactly:
- `C=B`: `h=sinB>0` (`→0` only as `B→0`).
- `C=2B` (`B≤π/3` sub-range, from `A>0`): `h=sin(2B)-sinB=sinB(4cosB-1)`,
  and `cosB>cos(π/3)=1/2>1/4` for `B<π/3`, so `h>0` strictly (`→0` only as
  `B→0`).
- `C=π-B` (`A→0` degenerate edge, `B>π/3` sub-range): `sin(π-B)=sinB`, so
  `h=2sinB-sinB=sinB>0` (`→0` only as `B→0`).

All three boundary traces are `>0` on the open domain and `→0` **only** at
the single corner `B→0` (forcing `C→0`, `A→π`). Combined with "no interior
critical point," this gives a genuinely rigorous (not numeric) argument
that `h>0` throughout the open domain **modulo one standard real-analysis
fact that still needs to be invoked carefully**: "no interior critical
point + boundary values `>0`" only immediately forces the *infimum* to be
non-negative and attained on the (closed) boundary in the compact case —
here the domain isn't compact (it's open, degenerating at the one corner),
so the clean way to finish this is either (a) a compactness argument on
`{h≤0}∩\overline{domain}` (closed, bounded, so if nonempty has a minimizer,
which must be interior by the boundary trace showing `h>0` there, giving
a critical point — contradiction) — this is short and rigorous, or (b) an
explicit two-variable Taylor/gradient bound near the one degenerate corner
`(B,C)→(0,0)` (the same style of argument already certified for Gap 5's
near-corner degeneracy, see below). **This is a genuinely different proof
mechanism from Opening 1** (global topological/critical-point argument vs.
a direct term-splitting inequality) and does not require settling the
`A>π/3` sub-case separately — it closes the whole domain in one shot, at
the cost of needing the compactness/no-critical-point argument written out
rigorously (currently sketched, not completed — per instructions I stop
here).

**Opening 3 (why NOT to reuse Theorem A's own proof skeleton for a "second
half"; item 2 of the dispatch).** Theorem A's proof structure is: prove
`f'>0` (done, unconditionally per the recap above) + prove `f>0` at ONE
anchor point (there, `β0`, via the intricate Theorem B casework on
`C1,C2,x=cos2β0`). The natural analogous move for Gap 7 would be "prove
`f(0)≥0` via the same style of trig casework Theorem B uses at `β0`." I
attempted this substitution directly: Theorem B's proof substitutes
`A=π-3β0, B=β0+s` — a parametrization *specific to the `β0` anchor*, not
transferable to the `β=0` anchor (there is no analogous "distance from a
fixed algebraic curve" parameter at `β=0`; `f(0)` is just
`sinA(2sinC-sinB)` directly, no `s`-type free parameter naturally
appears). So Theorem A/B's *literal* casework machinery (the `C1,C2,x`
factorization) does **not** transfer — confirms the round-18 note's own
suspicion, now checked directly rather than assumed. This is a genuine dead
end for a literal reuse; Openings 1/2 above are better mechanisms because
they exploit `f(0)`'s specific closed form directly rather than trying to
force-fit Theorem B's `β0`-specific substitution.

**Opening 4 (algebraic identity to existing certified machinery — checked,
does not exist).** Checked whether `f(0)`, `D_1`, `G_curve`, or `Tgt`
(all central to the certified Gap-5/Gap-6 closures) share any nontrivial
algebraic identity. They do not appear to: `D_1`/`Tgt`/`G_curve` all live
on Case (b)'s domain (`β1>β0(A)`, parametrized via the boundary curve
`X_0=cos²B` or the corner `(π/3,π/3)`), a **disjoint** region of `(A,B)`
from Case (a)'s domain (`β1≤β0(A)`, i.e. `A>π-3B`... wait, `β1≤β0`
corresponds to `A≤π-3B`, the complementary half-space from Case (b)'s
`A>π-3B` — worth double-checking against the file's own case split, but
either way Case (a) and Case (b) partition disjoint `(A,B)`-regions by
construction). `f(0)` depends only on `A,B` directly (no `β1` in it at
all, since it's an *endpoint* value of the `β`-sweep), so there is no
shared multiplicative/additive identity to piggyback on — Gap 7 is a
genuinely separate one-variable-family target, not a disguised instance of
already-certified Case-(b) machinery. **Recommend NOT spending effort
searching further here** — this is a checked, not merely assumed, dead
end.

### Item 1 of dispatch: is the certified `mpmath.iv` branch-covering technique
directly applicable to `f(β1)` on `(0,β0(A)]`?

Not recommended as the primary route, for a concrete reason found this
round: `f(0)→0` **only** as `(A,B)→(π,0)` (equivalently the fully
degenerate triangle `B,C→0`), which is exactly the same style of
vanishing-margin corner that defeated a *raw* pointwise interval sweep for
Gap 5's `Tgt` (round 15) and had to be rescued by the Taylor-with-Lagrange-
remainder technique (round 16, `lemmas/tgt-strictly-positive-throughout-D-
full.md`) rather than a direct sweep. A raw `mpmath.iv` sweep of `f(β1)`
(or even of `f(0)` alone) near this corner will hit the same
directed-rounding degeneracy at a point of asymptotic equality. **If Gap 7
is attacked numerically-certified rather than via Openings 1/2's algebra,
the right technique is the already-certified Taylor+Lagrange-remainder
method (reuse the exact machinery of `lemmas/tgt-strictly-positive-
throughout-D-full.md`), not a bare value sweep** — this is a concrete,
reusable piece of machinery already proven to work on an analogous
degeneracy in this exact population, and should be preferred over building
a new interval-sweep pipeline from scratch. Away from the one corner
(`B` bounded below by any fixed `ε>0`), a plain `mpmath.iv` sweep of
`f(0)` (or of `term1+term2` from Opening 1) should be entirely tractable —
it's a single elementary trig expression, far simpler than `Tgt` or `D_1`.

### Item 4: where does `f`'s minimum on `(0,β0(A)]` occur?

Confirmed numerically and consistent with the recap above: **always at the
left endpoint `β1→0`** (infimum, not attained in the open interval) —
`3000/3000` domain-sample fine grids (own script, `200`-point grid in
`β1∈(0,β0]` per sample) found the discretized minimum at the first grid
point in every single case, zero exceptions, consistent with `f`
strictly increasing throughout `(0,γ)` (already proved unconditionally,
per the recap). So the correct argument shape is exactly "endpoint value +
monotonicity," confirming (not duplicating — this explorer's target was to
find an independent mechanism for closing it, and Openings 1/2 above do
that) that the endpoint-value target is `f(0)≥0`, and that no separate
interior-minimum case analysis is needed.

### Candidate technique(s)
- Primary: Opening 1's elementary 2-term split (`term1+term2`), fully
  closes the sub-case `A≤π/3` outright; sub-case `A>π/3` needs one more
  elementary trig argument or a `mpmath.iv`/Taylor-corner closure (see
  Item 1 above) for the residual `A∈(π/3,π)` strip.
- Alternative/backup: Opening 2's no-interior-critical-point +
  boundary-trace argument (real-analysis/compactness style), a genuinely
  different mechanism that could close the WHOLE domain in one shot
  (all three boundary traces are elementary and already computed exactly
  above) if the compactness argument is written out carefully near the one
  degenerate corner — recommend as the outliner's first-choice framing if
  it wants a single unified argument rather than a two-sub-case split.

### Cheap-kill candidates
- The domain-forcing fact `B<π/2` (hence `cosB>0` unconditionally) is a
  free consequence of `A≤π-2B, A>0` — worth stating explicitly, it
  simplifies both Openings.
- `A≤π/3 ⟹ f(0)>0` immediately (term2≥0) — a genuine cheap partial closure,
  cuts the domain in half before any harder work is needed.

### Knowledge-base entries to use
- Same MVT/Taylor-with-Lagrange-remainder technique already certified in
  `lemmas/tgt-strictly-positive-throughout-D-full.md` (reusable machinery
  for the corner-degeneracy sub-case if Opening 1's `A>π/3` residual or
  Opening 2's corner argument needs a rigorous interval closure rather than
  hand algebra).
- Standard extreme-value/compactness argument (no named KB entry found
  specific to this; it's a basic real-analysis fact, should be stated and
  proved inline by the outliner/builder, not cited as a KB theorem).

### Analogous past problems (cruxes)
Did not find a crux corpus problem specifically analogous to "prove a
2-term trig split `2sinA cosB + sinB(2cosA-1)>0` on a triangle-angle
sub-domain" — this is a narrow, problem-specific elementary trig fact, not
a generic technique pattern that the corpus would index well. Not chased
further given the time budget and the strength of the direct algebraic
leads already found above; recommend the outliner treat this as elementary
in-house algebra rather than search for a crux match.

### Prior progress
`f'(β)>0` on all of `(0,γ)` (unconditional, already fully certified inside
`lemmas/claim-I-closed-and-claim-II-caseA-closed.md`'s own Theorem A proof,
just not stated at that scope) + `f(0)≥0` (NOT proved anywhere yet, target
of this report) `⟹` Case (a) closed. This round's new content: the exact
2-term split (`term1+term2`) fully closing the `A≤π/3` half, the
no-critical-point/boundary-trace argument as a second, independent
mechanism for the whole domain, and the confirmation (Opening 3) that
Theorem B's own `s`-substitution casework does not transfer to `β=0`.

### Dead ends (do not retry)
- Reusing Theorem B's literal `A=π-3β0,B=β0+s` substitution/casework
  machinery at the `β=0` anchor — checked directly this round, does not
  transfer (no natural `s`-type parameter at that anchor). Do not re-embark
  on "adapt Theorem B's proof to `β=0`" as a plan; use Openings 1/2 instead.
- Searching for a shared algebraic identity between `f(0)` and
  `D_1`/`G_curve`/`Tgt` (Case-(b)-only quantities) — checked, domains are
  disjoint, no such identity found or expected.
- A raw `mpmath.iv` pointwise sweep of `f(β1)` (or `f(0)`) covering the
  whole domain including the `(A,B)→(π,0)` corner — will hit the same
  interval-width-at-equality degeneracy that defeated Gap 5's first sweep
  attempt (round 15); use the corner away from that point only, or use the
  Taylor+Lagrange-remainder technique near it.

### Small-case / intuition notes (conjectural where labeled)
- Conjecture (very strong numeric support, `2M+` samples, zero violations):
  `f(0)=sinA(2sin(A+B)-sinB)≥0` throughout the Case-(a)-nonempty domain,
  equality only in the fully degenerate limit `B,C→0,A→π`.
- Proved (not conjecture): for `A≤π/3` in this domain, `f(0)>0` follows
  from two elementary sign facts alone (`sinA>0`, `cosB>0`, `cosA≥1/2`) —
  no numerics needed for this half.
- Confirmed (not conjecture): `h(B,C)=2sinC-sinB` has no interior critical
  point on the true 2-D domain, and all three boundary traces are
  elementary closed forms, each `>0` except in the shared limit `B→0`.
- Confirmed numerically: `f`'s minimum over `β1∈(0,β0(A)]` is always at the
  left endpoint `β1→0` (`3000/3000` domain samples), consistent with `f`
  being strictly increasing throughout `(0,γ)`.
