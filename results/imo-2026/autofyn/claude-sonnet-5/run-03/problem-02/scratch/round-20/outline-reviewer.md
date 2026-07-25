## imo-2026-02 — Round 20 outline review

### Independent re-verification of the three flagged claims

**(1) T-positivstellensatz explorer's corner claims — CONFIRMED, from scratch.**
Rebuilt `X0, Kc, P, Ac, Cc, E, Bc, T` from the raw definitions in a fresh
`mpmath` (dps=60) script (not reusing any file's code) and checked:
- `A* = 3·arcsin(√6/4) − π/2 = 0.4063777806843303293871746903293092626710…`,
  `B* = β0(A*) = 0.9117382909684876363584895643167312071754…`.
- `T(A*,B*) = 7.78×10⁻⁶² ≈ 0` — confirms exact vanishing at the corner.
- `X0(A*,B*) = 0.375000…` to 60 digits and `cos²(B*) = 0.375000…` to 60
  digits — confirms `X0 = cos²β0(A*) = 3/8` exactly, and hence that this
  is literally the same corner used to close `D1≥0`
  (`lemmas/d1-nonnegative-on-boundary-curve.md`, whose Step 0 needs exactly
  this fact for a *different* quantity, `X0(A*,B*)=cos²B*`). Same closed
  form for `A*`, same defining property — this is genuinely one corner, not
  a coincidental numerical match.
- Order of vanishing: swept `T(A*+ε, β0(A*+ε))/ε` for
  `ε∈{10⁻²,…,10⁻⁶}` along the active boundary curve itself (not the
  explorer's "re-minimize domain slice" method, an independent check) —
  ratio converges to `≈1.4774`, stable to 4 significant figures across 5
  orders of magnitude in `ε`. This **independently confirms linear (not
  quadratic) vanishing**, consistent with the explorer's own (differently
  computed) `1.87–2.14` estimate and, more importantly, with the shared
  qualitative conclusion: a nonzero one-sided directional derivative along
  the active boundary edge, not a tangential double root. The outline's
  instruction to build a directional-derivative-lower-bound + Lagrange-
  remainder argument (not a concavity/second-derivative argument) is
  correctly targeted.
Verdict: claim (1) is fully verified. This is a real, load-bearing
structural finding, not a numerical artifact, and it correctly explains
the SDP degeneracy diagnosed over rounds 16-18 without requiring any new
solver runs. The recommendation to NOT dispatch further SOS/SDP search on
`T`/`-sos` this round is well-supported and adopted below.

**(2) Ptolemy-Ψ vs. coordinate-bash-T independence — CONFIRMED by
structural argument, not literal computation (appropriately, since a
"prove they're different" claim is a negative existence statement).** The
explorer's dimension-count argument is sound and checks out against the
cited lemma files: `Ψ(τ,A,C)>0` must hold for every `θ∈(0,min(B,C))` at
*fixed* triangle shape `(A,C)` — i.e. 3 real degrees of freedom (θ free +
A,C shape) — whereas `T≥0`'s domain is `(A,B)` alone, with `β1` in this
sub-case *pinned* by `X0(A,B)` (not a free angle) — 2 real degrees of
freedom. A 3-parameter-family positivity statement cannot literally be the
same polynomial identity as a 2-parameter one; the `τ` name-collision
(`tanθ` vs. `sin²B`) is coincidental (checked: neither convention makes the
coefficient shapes align — Ψ retains transcendental dependence on A,C via
sin/cos, `q1,r0` are honest rational polynomials in `σ,τ` with no further
trig dependence). This is a legitimate, careful negative check, correctly
hedged (the explorer does not claim to have *proved* no possible
degenerate-slice correspondence exists, only that none is suggested by any
existing file and a substitution is structurally implausible given the
dimension mismatch). Verdict: treating them as genuinely independent
targets (not a shared disguised inequality) is justified and should stand.

**(3) Synthetic-concyclicity explorer's refutations — accepted on
methodological grounds, not independently re-derived end-to-end this
round.** I did not have time to fully reconstruct the H1/H2/H3-constrained
`fsolve` family from scratch to byte-for-byte reproduce all 5 refutations
(a full reconstruction of the branch/orientation conventions used by prior
rounds' constructions would take longer than the remaining budget allows).
However: (a) the methodology matches the population's own established,
previously-certified construction technique (constrained numeric solving
of H1-H3 + containment checks, cross-checked against 3 independent
triangles), which has been reliable across many prior rounds; (b) the
report's internal consistency checks are a good sign — e.g. the `BMCQ`
guess is correctly flagged as "not informative" because none of its four
points depend on `K,L,φ`, and the false general-lemma assignment to H1 is
shown to scale as *exactly* `2φ` (not a noisy near-fit), which is the kind
of clean, structured failure signature that indicates a real computation
was run, not a guess; (c) the new `Q` characterization (`Q` = (line through
`A` ∥ `BC`) ∩ (perp. bisector of `BC`), i.e. `QB=QC`) has an accompanying
correct elementary synthetic argument sketch (the perpendicular from
`O_ABC` to a line has direction ⟂ that line, which for the parallel-to-`BC`
line through `A` is exactly the `BC`-perpendicular-bisector direction) that
is checkable by inspection and is genuinely elementary — this part I
consider verified by direct reasoning, not just trusted numerics. Verdict:
accept the refutations as reported, with the caveat flagged above (not
independently re-run this round) — nothing in the report is internally
inconsistent or suspicious, and the finding that `Q` has a strictly simpler
characterization than either prior phrasing is real, useful progress
regardless of whether the concyclicity gap itself is closed this round.

### Approach-by-approach verdicts

**`coordinate-bash-resultant-boundary-pointwise-tangent` (advance) —
APPROVE.** Technique (local Taylor + certified Lagrange remainder near a
domain corner, glued to an interval sweep away from it) has already
succeeded twice on this *exact* corner (`Tgt`, round 16; `D1`, rounds
17-18); item (1) above independently confirms every numeric fact the
skeleton depends on (corner value 0, `X0=3/8`, linear vanishing). The
skeleton correctly identifies the needed shift from the prior
concavity/tangent-cone template (used for `Tgt`) to a directional-
derivative-lower-bound argument (matching `D1`'s style), per the explicit
memory-rule warning already baked into the outline. Load-bearing lemmas
are stated with mechanism (not bare labels): the corner value's exactness
is tied to an explicit `X0=3/8` identity claim (open but well-scoped,
analogous in style to already-solved `D1`-corner sub-lemmas), and the
order-of-vanishing claim is tied to the domain's own boundary-active
structure, not asserted without justification. No fatal flaw found.

**`coordinate-bash-resultant-boundary-pointwise-tangent-via-T` (copy) —
APPROVE, registered.** This is a genuine alternative *mechanism* for the
identical remaining gap (polynomial Taylor expansion of `q1,r0(σ,τ)`
directly vs. trigonometric expansion of `G(β1)`), matching the round-12
precedent for fielding a copy when two distinct untried levers exist for
the same closing obligation and it's unclear in advance which is more
tractable. It is NOT a fragment of the sibling's proof — both copies carry
the full chain from the certified Reduction Lemma through to `OM=ON`; they
diverge only in which local algebraic route closes the one open lemma.
Wrote the approach body file (`approaches/coordinate-bash-resultant-
boundary-pointwise-tangent-via-T.md`) since the outliner's skeleton was
detailed but no file existed yet (per the round-11 memory rule). Copied
via `copy_approach` from `coordinate-bash-resultant-boundary-pointwise-
tangent` (inherits Elo 1781, expanded=16, no outcome yet).

**`ptolemy-trig-identity` (advance) — APPROVE.** The Vieta-elimination
lever (substitute the certified closed-form roots `x=cotψ(p),y=cotφ(p)`
of the two certified quadratics `(III)′,(IV)′` directly into the boxed
`F(p,x,y)` identity) is concrete, cheap, and correctly scoped: Step 2 of
the skeleton correctly notes `F` has no `x²,y²` terms so the "substitute
the quadratic to eliminate squares" trick doesn't directly apply — the
actual lever is substituting the closed forms themselves, which is
honestly described as producing a possibly messy but genuinely 1-variable
(in `p`) target, not asserted to already be simplified. This is a
legitimate new mechanism, distinct from the exhausted `U=cotα` route, and
its outline explicitly flags the open risk (Step 3's sign determination on
whatever polynomial results, degree/domain unknown in advance) rather than
hand-waving it. Good diversity value: this is the only fielded route whose
top-level target (`Ψ>0`/concyclicity-free Ptolemy-equality construction)
is structurally different from both the coordinate-bash family and the
synthetic-concyclicity family.

**`spiral-similarity-bootstrap` (revise) — CHANGES REQUESTED, still
buildable this round.** Step 1 (rigorous write-up of the simpler `Q`
characterization, `Q`=(line through `A`∥`BC`)∩(perp. bisector of `BC`)) is
concrete, cheap, and essentially already sketched correctly (see item (3)
above) — build this first. The main gap-closing step (the angle chase at
`Q` using `QB=QC`, Steps 3-4) is NOT yet a fully specified mechanism: the
outline offers it alongside two alternative, wholly untried mechanisms
(inversion at `Q`; a systematic sweep of point assignments for the general
one-angle lemma vs. H1, of which only 1 of many was tested and it failed).
This is a legitimate "plan with real options, one open gap" outline, not a
research-direction hand-wave (each option has a concrete criterion for
success/failure), but it is fair to flag that the builder does not yet
have a single committed closing argument. Instruct the builder: (a) first
lock down Step 1 rigorously; (b) attempt the direct angle chase with
`QB=QC` as the primary path; (c) numerically pre-screen any new angle
relation for `φ`-independence (per this round's and prior rounds' memory
rule) before investing in a hand proof; (d) fall back to inversion-at-`Q`
or a systematic assignment sweep only if the direct chase stalls. Keep in
the build set — it is the population's only synthetic (non-coordinate-bash)
route and is making real incremental progress (new `Q` characterization),
satisfying the CLAUDE.md diversity requirement.

**`coordinate-bash-resultant-boundary-pointwise-sos` (advance, dormant, no
build slot) — correctly NOT fielded.** This round's `T`-positivstellensatz
finding (item (1) above) explains this route's own long-standing SDP
degeneracy as the same structural phenomenon (a Positivstellensatz target
that is exactly 0 at a genuine domain corner forces complementary-slackness
rank deficiency at any degree). No further SDP/SOS search should be
dispatched on it; if revived, it should adopt the same local-Taylor-near-
corner reframing, not another solver attempt. Agreed with the outliner:
no build slot this round.

### Diversity assessment
Three genuinely distinct top-level framings remain live: (i) coordinate-
bash / algebraic-boundary-corner (the `-tangent` pair — same route, two
closing mechanisms for the one shared gap, legitimate under the round-11/12
copy precedent, not a "split proof across slugs" violation since both carry
the full chain to `OM=ON`); (ii) Ptolemy-trig-identity (a wholly separate
global reduction); (iii) spiral-similarity-bootstrap (pure synthetic,
concyclicity-based). No shared-gap plateau across *distinct* framings this
round — the `-tangent` pair's shared gap is intentional (same route by
design), not a population-wide convergence. The `-sos` route sits dormant
for a principled, explained reason rather than being silently dropped.

### Ranking
Ranked via `update_ranking` (draws/wins anchored to last-recorded outcomes
and this round's independent verification):
- `coordinate-bash-resultant-boundary-pointwise-tangent` beats
  `spiral-similarity-bootstrap` and `ptolemy-trig-identity` (closest to a
  complete, certified chain; this round's independent checks confirm its
  remaining gap is well-understood and tractable by a twice-proven
  technique).
- `coordinate-bash-resultant-boundary-pointwise-tangent-via-T` (fresh copy,
  inherits sibling's standing) beats `ptolemy-trig-identity` and
  `spiral-similarity-bootstrap` for the same reason; drawn against its
  sibling `coordinate-bash-resultant-boundary-pointwise-tangent` (identical
  standing today, no independent outcome yet to separate them).
- `ptolemy-trig-identity` beats `spiral-similarity-bootstrap` (fully
  reduced to one polynomial-positivity target vs. spiral's still-open
  concyclicity mechanism).
- `coordinate-bash-resultant-boundary-pointwise-sos` loses to all three
  live routes (dormant, structurally explained degeneracy, no build slot).

Resulting Elo (best-first): `coordinate-bash-resultant-boundary-pointwise-
tangent` (1796.6) ≈ `…-tangent-via-T` (1793.3) >> `ptolemy-trig-identity`
(1516.4) ≈ `spiral-similarity-bootstrap` (1516.1) > `…-sos` (1492.8).

### Build set
Dispatch one proof-builder per slug: the two `-tangent` siblings (highest
value, both attacking the population's single most load-bearing remaining
gap with two independent, well-scoped mechanisms), `ptolemy-trig-identity`
(new cheap lever on its own long-stuck gap, good diversity), and
`spiral-similarity-bootstrap` (only synthetic route, real incremental
progress, clear next steps despite an unresolved final mechanism).
`coordinate-bash-resultant-boundary-pointwise-sos` is intentionally
excluded (dormant, no new technique to try).

build set: coordinate-bash-resultant-boundary-pointwise-tangent, coordinate-bash-resultant-boundary-pointwise-tangent-via-T, ptolemy-trig-identity, spiral-similarity-bootstrap
