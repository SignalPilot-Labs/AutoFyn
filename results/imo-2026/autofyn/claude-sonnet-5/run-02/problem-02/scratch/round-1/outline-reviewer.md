## Outline review — imo-2026-02, round 1

### Shared Lemma 0 (used by all 5 approaches) — VERIFIED SOUND
`OM² − ON² = (2P−M−N)·(N−M)` type identity, applied at P=O and P=N9 (nine-point
center), gives `OM²−ON² = 2(O−N9)·(N−M)`; since MN is the midline of ABC,
`N−M ∥ C−B`, so **OM=ON ⟺ (O−N9)·(C−B)=0**. I re-derived this algebraically by
hand (`(a+b)·(a−b) = |a|²−|b|²` with `a=P−M, b=P−N`) — it is a correct,
unconditional vector identity, independent of the K,L conditions. N9M=N9N is
correct because M, N are both midpoints of sides, hence both lie on the
nine-point circle. This shared reduction is safe to reuse verbatim across all
approaches; no approach needs to re-derive it from scratch, but each must
still state it (already done).

I attempted an independent numerical spot-check of the underlying claim
(`O−N9 ⊥ BC` holding along the whole admissible K,L family) using
`scipy.optimize.fsolve` with unsigned `arccos`-based angle equations. This
converged to *spurious* branches (K, L landing far outside the required
triangles BMC/BNC, with `OM≠ON` and the perpendicularity failing) — this is
expected: unsigned angle equations have multiple solution branches, and
picking the one respecting the "K inside angle LBA," "L inside angle ACK"
containment hypotheses requires either directed angles with a fixed
orientation or explicit box constraints, exactly as the outline's "Watch out
for" notes on sign conventions warn. I could not, within the time budget,
reproduce the round-1 explorers' reported 1e-10–1e-14 residual confirmation
of the target identity on a correctly-branched solution. **This is not a
reason to reject the shared reduction (Lemma 0 is algebraically airtight
independent of K,L), but every builder must independently re-derive/re-check
the correct branch numerically before trusting any downstream symbolic work**
— flag this explicitly to all builders, especially complex-number-argument-bash
and nine-point-locus-two-position, whose entire route depends on the
1-parameter family being correctly identified.

### Per-approach verdicts

**complex-number-argument-bash — APPROVE.**
Right technique (complex bash with directed-angle-as-positive-real-ratio
dictionary is standard and sound; kb: Coordinates/complex, Synthetic
toolkit). Lemmas have genuine mechanisms, not just labels: "equal argument ⟺
positive real ratio" is a cited standard fact with a one-line proof; N9 as
circumcenter of the medial triangle is definitional, correctly justified.
The plan commits to full symbolic closure rather than hoping for a shortcut
— most likely to actually terminate in a checkable identity. Risks are
execution risks (sign convention, computational feasibility, spurious zero
denominators at the isosceles case), not soundness risks, and the outline
already flags all three explicitly with mitigation ("sanity check against
fsolve numerics before trusting symbolic algebra," "treat vanishing
denominators by continuity"). No missing cases (single generic symbolic
sweep, degenerate sub-cases explicitly flagged for separate handling).

**nine-point-locus-two-position — CHANGES REQUESTED.**
Technique (moving-point / two-special-position argument via an affine
reparametrization, modeled on IMO SL 2023 G5) is legitimate and can yield a
short, elegant proof if it works — correctly borrowed as inspiration, not
cited as a shortcut (per CLAUDE.md crux-corpus rule). However, **Lemma B
("O(θ) is affine in some reparametrization t(θ)") is stated with no
mechanism at all** — only an analogy to a different problem ("this is
exactly the mechanism in aimo-1007... must be re-derived from scratch
here"). A lemma this load-bearing needs at least a plausibility argument
specific to *this* configuration (e.g., why the circumcenter-of-three-points
rational formula should collapse to affine here) before a builder invests
real effort chasing it. **Required change:** before doing the full symbolic
derivation, the builder must run a **cheap numerical check** analogous to
what the spiral-similarity approach is required to do first — sample O(θ) at
several θ values (correctly branched, respecting containment) and check
whether O(θ) is genuinely affine in *some* natural parametrization (plot / co
llinearity check on 3+ points), before committing to Lemma A's closed-form
derivation. If the numerical check fails to show affineness in any natural
parametrization, this approach should fast-fail back to the outliner rather
than forcing a symbolic derivation of a lemma that isn't true. This is not a
fatal flaw (worth trying, given the strong crux analogy) but the outline
currently asks the builder to commit real algebra effort before checking the
central premise — that ordering must be reversed.

**symmetric-vector-decomposition-sigma — CHANGES REQUESTED (bounded effort only).**
The σ-invariance-of-the-system claim (step 1) is correct bookkeeping and
easy to verify clause-by-clause. But **step 3, the actual load-bearing claim
("the BC-component of O−N9 is an antisymmetric expression that telescopes to
0 via (ii),(iii)"), is asserted with no mechanism whatsoever** — it is a
hope about how a dot-product expansion might behave, not a stated identity
or substitution. This is precisely the kind of "lemma named without its
mechanism" the review criteria warn against — it should not be handed to a
builder as if it were a proof step; it is closer to a research question. The
outline itself admits this ("if the builder cannot make step 4 concrete
within reasonable effort, this approach should be marked stuck"), which is
the right caveat, so I am not sending this to RETHINK, but it must be built
with a hard time-box: verify the isosceles sanity check (step 4) first
(cheap), and if the general antisymmetric cancellation isn't visible after
that, report back rather than continuing.

**homothety-doubling-target — CHANGES REQUESTED / deprioritize.**
Technique is sound bookkeeping (homothety centered at A, ratio 2, correctly
verified: `O'=2O−A` is circumcenter of `A,K',L'`; `K'−B=2(K−M)` is a direct
correct computation). But this approach **is not a genuinely different
framing** — it is the same Lemma-0-style algebraic identity, just phrased in
a B,C-relative frame instead of an M,N,N9-relative frame. The outline itself
admits this ("essentially an affine change of frame... do NOT let the
builder believe steps 1-3 constitute progress on the hard part... should be
abandoned if step 4 turns out no easier"). Given CLAUDE.md's explicit warning
against approaches that only differ in technique/framing and hit the same
wall together, and that this field already has two other computational
routes (complex-number-argument-bash, nine-point-locus-two-position) working
essentially the same reduction, this approach adds limited diversity value.
Not fatal — keep registered for the population, but do not spend build
budget on it this round.

**spiral-similarity-radical-axis — CHANGES REQUESTED (fast-fail probe, correctly scoped).**
This is the most genuinely different framing in the field (synthetic
concyclicity + radical axis vs. everyone else's algebra/coordinates) —
valuable for diversity per CLAUDE.md's "push for diversity of thought"
directive. Correctly scoped as a bounded existence-check probe: the outline
explicitly requires numerically verifying the concyclicity claim to ≤1e-9
precision on ≥2 triangles BEFORE any synthetic argument is trusted, and
explicitly instructs abandoning (RETHINK) if the check fails. This ordering
(cheap numeric check first) is exactly right and should be the template the
nine-point-locus outline is revised to follow (see above). No fatal flaw at
the outline stage; the mechanism ("radical axis of two equal circles is the
perpendicular bisector of their centers") is a standard, correctly-stated
fact.

### Diversity assessment (for the orchestrator)

3 of 5 approaches (nine-point-locus-two-position, complex-number-argument-bash,
homothety-doubling-target) are variations on one framing: reduce via Lemma 0
to a perpendicularity target, then close it by algebra/coordinates in some
frame or parametrization. If this framing's underlying identity turns out to
be algebraically intractable (e.g. the residual equation after eliminating
one of K, L is genuinely high-degree with no clean simplification), all
three die together — the "single-gap trap" CLAUDE.md warns about. Only
symmetric-vector-decomposition-sigma (structural/symmetry) and
spiral-similarity-radical-axis (synthetic concyclicity) are mechanistically
distinct. Both of those are currently under-developed (their central claims
have no demonstrated mechanism yet, only hope), so the field's genuine
diversity is currently unproven, not just unbalanced. Recommend: if both
symmetric-vector-decomposition-sigma and spiral-similarity-radical-axis fail
their first bounded probes next round, the outliner should be pushed to find
a *third*, different non-computational framing (e.g. an inversion-based or
projective/cross-ratio route) rather than doubling down on the computational
cluster.

### Build set rationale

Prioritize the two strongest-scoped approaches (complex-number-argument-bash
has the cleanest mechanism-backed lemmas and highest odds of terminating;
nine-point-locus-two-position offers the most elegant potential proof and is
a legitimate crux-inspired technique, but must be re-ordered to numerically
test Lemma B's affineness before the algebra), plus one genuine
diversity probe (spiral-similarity-radical-axis) to start testing whether the
field's synthetic alternative is viable, per the orchestrator's diversity
mandate. symmetric-vector-decomposition-sigma and homothety-doubling-target
are held back this round (registered, ranked, available to resample) —
homothety for redundancy, symmetric-vector-decomposition for being the least
developed with the weakest-stated mechanism; both can return in later rounds
if the build-set approaches stall.

build set: complex-number-argument-bash, nine-point-locus-two-position, spiral-similarity-radical-axis
