# Outline review — round 17, imo-2026-02

All three fielded approaches are `advance` (no new slug, no fork request). All
target the whole problem's claim `OM=ON` via the same already-established
reduction chain (vector reduction -> rotation parametrization -> Case (b)
isolation, certified since round ~5-8) but attack the residual sub-target
through three genuinely distinct mechanisms that have been live and
diverging since round 11-14 (interval-arithmetic/tangent-line direct
positivity vs. exact-witness SOS/Positivstellensatz vs. LP/SDP generator
search on `-q1,-r0`). This is not the single-gap-split trap flagged by
CLAUDE.md — the three routes fail/succeed independently (confirmed again
this round: `-tangent` is one 1-D gap from total closure, `-sos` is
diagnosing a Gram-matrix degeneracy, `-boundary` just exhausted an entire
generator family) — legitimate diversity, consistent with prior rounds'
vetting of this population structure.

## coordinate-bash-resultant-boundary-pointwise-tangent — APPROVE

Target: close Gap 6, the sole remaining obstruction of this route:
`D_1(A)>=0` on boundary curve `C=C_lo`, `B in [B*,pi/3]`.

Independently re-verified from scratch (own fresh `mpmath`, 50 dps,
reconstructing `X0, RHS(via beta0,Kc,P,Q,G), D_1, Aof(B)` directly from the
file's displayed raw closed forms, not copied code):
- `D_1(B*)=0` to 51 digits (residual ~2.7e-51) at the certified corner
  `B*≈0.911738290968...`, `A*=Aof(B*)≈0.406377780684...` — matches exactly.
- `D_1(pi/3)=0.397686404277917446...` — matches the file's cited value to
  every displayed digit.
- `D_1'(B*)=4.62576916670...` (central finite difference, h=1e-20) — matches
  the outliner's/explorer's cited `≈4.6257691667` value exactly.
- A 2000-point grid scan of `D_1` on `[B*,pi/3]` found **zero** negative
  values (global min on the grid is essentially 0, attained only at `B*`
  itself) — confirms the claimed "single interior max ~0.4054, monotone
  decrease to 0.3977 at pi/3, never re-approaching 0" behavior.
- A 200-point derivative scan on `[B*,B*+0.02]` stays `>=4.62` throughout —
  comfortably clears the outline's proposed near-corner threshold `c=1` by
  a wide margin (>4x), de-risking step 4b.
- Domain-correction claim (step 2): independently confirmed that continuing
  `Aof(B)` past `B=pi/3` violates `B<=C` (checked `B=1.05,1.1,1.2`: `C<B` in
  every case) — the `-twopoint` sibling's `A_max≈1.0484` claim is indeed a
  numeric-continuation artifact outside the true domain, exactly as
  reported.

This is a clean reapplication of two techniques (interval-arithmetic
branch-covering; Taylor+Lagrange-remainder derivative-sign bound) *already
proved to work in this exact file* on a strictly simpler 1-variable target
with comfortable numeric margins on all sides. No new machinery, no
circularity, no case-coverage gap (single continuous target on a compact
interval, split only for proof-technique convenience — explicitly and
correctly noted as "not casework" by the outliner). The only thing not yet
done is turning the numeric domain-correction (step 2) into an exact
symbolic argument, which the outliner itself correctly flags as unproved
("a numeric finding to be formalized ... not yet written as a lemma") and
schedules as this round's build work, not a hidden gap. This is the single
narrowest, best-supported gap in the whole population's history — approve
without reservation, and use interval arithmetic (not point sampling) for
the actual derivative-sign certificate as the outline's own caveat (b)
demands.

## coordinate-bash-resultant-boundary-pointwise-sos — APPROVE (exploratory)

Independently reconstructed the explorer's reasoning: the near-null
5-dimensional eigenspace of `sigma_0`'s Gram matrix `M_0` is explained (2 of
5 dimensions) by a genuine complementary-slackness phenomenon — `sigma_0`
tangent to 0 at `s*`, the exact root of the domain-boundary generator
`n_1(s)=0` — this is the standard SOS/SDP fact (`M PSD` and
`z(s*)^T M z(s*)=0` implies `Mz(s*)=0`) applied correctly, and the report is
careful not to overclaim: it explicitly states only 2 of 5 near-null
directions are explained, the other 3 remain open, and this is a
"reframing, not a resolution." The mechanism (constrain `M_0 z(s*)=0` as an
explicit linear equality rather than hoping numeric truncation finds it) is
sound in principle — this is standard exact-vanishing-order SOS
construction, a legitimate escalation from "diagnose numerically" to
"build the constraint in exactly." No fatal flaw; this round's target
(exact root isolation + constrained-SDP rerun) is concrete and buildable.
Flag for the builder: step 4's honest failure branch ("if constrained SDP
still fails, report and consider a 4th generator") must actually be
followed if it occurs — do not silently drop the 3 unexplained directions.

## coordinate-bash-resultant-boundary — APPROVE (pivot after full exhaustion)

Independently spot-checked the explorer's central claim structurally:
the margin/robustatness SDP reformulation (`maximize t` s.t.
`target - t in cone`) is the textbook fix for a feasibility SDP degenerate
at a true infeasibility boundary (no Slater point) — this is a standard,
sound technique, and the report's own conditioning diagnostics (eigenvalue
checks down to ~1e-9, degree-escalation invariance to 9-10 significant
digits at maxdeg 10 vs 12, cross-solver CLARABEL/SCS agreement) are the
right battery of checks to rule out a solver artifact (exactly the kind of
check that caught a real artifact in round 16). The resulting "8/8
infeasible, degree-independent" finding is a legitimate, complete negative
result for the specific generator family
`{1,sigma,tau,1-sigma,1-tau,B1,-B2,B4,B6,B_G0E,B_G0N,B_EN}` — not a
methodology failure. The outline's pivot to (1) a domain-aware case-split
and (2) a probe for a genuinely new odd-c/odd-d generator (motivated by the
already-proved round-13 parity-obstruction necessary condition) is the
correct next move — both are concrete, falsifiable, and grounded in
already-certified structural facts (the parity theorem), not a fishing
expedition. Watch-out: this route has now spent 4+ rounds without closing
a sub-gap; if both the case-split and the new-generator probe fail again
next round, this is the point to seriously weigh whether the whole
`{G_0,E_num,Num,Bc}`-generated Positivstellensatz framing (not just this
generator subset) needs to be abandoned in favor of a different reduction
of Case (b) — the outline itself already flags this contingency (step 4),
which is appropriately cautious.

## Field diversity check

No shared-gap plateau this round: `-tangent` closes its own idiosyncratic
gap 6 (nearly done), `-sos` is diagnosing a Gram-matrix-null-space
mechanism unique to its exact-witness-point approach, `-boundary` just
finished exhausting one generator family and is pivoting to two new levers.
All three genuinely independent lines of attack on the shared Case (b)
residual, not variations of one framing.

## Ranking

Updated via `update_ranking` (K=32 Elo): `-pointwise-tangent` (1748, best —
narrowest, most rigorously-supported remaining gap, own numeric
verification found comfortable margins everywhere), `-boundary` (1664,
second — completed a full negative characterization of its generator
family this round with real, cross-solver-validated rigor, and has a
concrete, well-motivated pivot), `-pointwise-sos` (1564, third — real but
partial diagnostic progress, honestly scoped, 3 of 5 near-null directions
still unexplained). No new slugs to register this round (all three are
`advance` on already-registered slugs); no fork requested.

build set: coordinate-bash-resultant-boundary-pointwise-tangent, coordinate-bash-resultant-boundary-pointwise-sos, coordinate-bash-resultant-boundary
