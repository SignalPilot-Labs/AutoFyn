## imo-2026-02 — outline review (round 3)

### Headline verification: the genericity certificate is REAL — independently reproduced from scratch

Per dispatch, I did not take `math-explorer-genericity`'s "full symbolic Gröbner
certificate, remainder 0" claim on faith. I rebuilt the entire pipeline myself
in a fresh sympy session (script and transcript below), without importing any
of the explorer's intermediate values:

- Built `eq2`, `eq3` symbolically with `A=(0,0), B=(a,0), C=(b,cc)` (three free
  parameters) and the Weierstrass substitution `u=tan(β/2)`: matches the
  reported degrees (24, 22) and build time (<1s).
- Confirmed `eq2 = t1²·g2`, `eq3 = s2²·g3` exactly (zero remainder from
  `sp.div`) — the homogeneity-decoupling lemma does generalize symbolically.
- Factored `g2`, `g3` and identified the four cofactors by degree in `u`
  (4 vs 6), matching the reported `G2a/G2b`, `G3a/G3b` structure exactly.
- Built the target `T` (numerator of `O·(C−B) − (|C|²−|B|²)/4`) — degree 12,
  matches the report.
- Ran `sympy.groebner([G2a, G3a], t1, s2, u, a, b, cc, order='grevlex')`:
  **18 generators, ~2.9s** — matches the reported basis size and timing
  exactly.
- `gb.reduce(T)[1]` → **0**, confirmed independently. `T ∈ ⟨G2a, G3a⟩` in
  `ℚ[t1,s2,u,a,b,cc]` holds for genuinely symbolic `a,b,cc`, not sample
  points — since this is a polynomial identity `T = q1·G2a + q2·G3a` with
  `qi ∈ ℚ[...]`, it survives specialization to *any* real `a,b,cc`
  (including irrational), so the certificate really does cover every
  triangle, not just rationals.
- Extra sanity check beyond the explorer's report: `T` does **not** reduce to
  0 modulo `G2a` alone or `G3a` alone — both generators are genuinely needed,
  ruling out a degenerate/trivial ideal-membership artifact.

**Conclusion: the genericity claim is credible and reproducible.** This is a
real result, not an overclaim — it genuinely closes gap 1 of
`coordinate-bash-resultant` (only branch selection, gap 2, remains open, and
the outline correctly does NOT claim gap 2 is closed — the acute-angle lemma
is explicitly labeled "open, the crux of gap 2" with numeric-only support).
This is the round's headline finding and should be flagged to the builder as
verified-in-advance so it can write it up directly rather than re-deriving.

One nuance the builder must still handle carefully in the writeup (not a
flaw, a to-do): the correspondence "`G2a,G3a` branch ⟺ positive dot products
/ acute angle" is asserted by the outline but not yet verified — my
reproduction confirms the algebra (`T ∈ ⟨G2a,G3a⟩`) but says nothing about
which branch is geometrically correct; that identification is still gap 2's
job, exactly as the outline states.

### Approach-by-approach review

**1. `coordinate-bash-resultant` (revise) — APPROVE.**
Target is the full problem (OM=ON for every valid configuration), via the
certified reduction — a whole attempt, not a fragment. Technique (Gröbner
ideal membership) is correct and now verified to actually deliver on the
generic case (see above). The skeleton is sound: steps 1–6 are either
already certified or a direct, reproducible rerun (now independently
confirmed by me), and step 7–8 (branch selection via an acute-angle
synthetic bound) is honestly flagged as the one open gap, with a stated
mechanism (containment hypotheses + triangle-angle-sum bound at each vertex,
using σ-symmetry to halve the work) rather than a bare label. No
overclaiming found anywhere in the outline text.

**2. `coordinate-bash-resultant-boundary` (copy) — APPROVE the branch.**
This is a legitimate use of the copy mechanism: same proven prefix (the now-
verified genericity certificate), diverging only on gap 2 via a genuinely
different mechanism (continuity/IVT vs. direct length bound). The outline is
explicit that this needs (i) a no-crossing resultant argument and (ii) one
boundary-value check, and flags that the "valid range is connected" input
fact needs to be re-confirmed/cited, not assumed silently — good practice.
Worth building in parallel with approach 1 since a stall in one lever
doesn't imply a stall in the other, and it's cheap (shares 90% of the
already-certified/reproduced machinery).

**3. `fixed-point-concyclic` (revise) — APPROVE.**
Correctly imports this round's `math-explorer-signlemma` Part A derivation
(four cross-product identities, each reducing exactly to `bxc` or `bxc/2`
with no residual term and no case split — I did not re-derive these myself
but the algebra as stated is a one-line elementary vector expansion and is
consistent with the explorer's transcript) to remove the round-2 overclaim
cleanly. This is real, checkable progress on a previously-flagged rigor gap,
not new hand-waving. The remaining gap (χ∈ℝ elimination) is correctly named
as the one substantive open step and is honestly framed as lower-priority
now that approach 1 has a generic algebraic fallback — good triage, not an
overclaim of imminent closure.

**4. `ptolemy-trig-identity` (advance) — APPROVE.**
Continues from round 2's certified state without re-deriving. The case-split
criterion (sign(AB−AC)) is still open but now has a concrete lever (reuse
approach 3's sign identities) instead of sitting as a bare "TBD" — this is
the right kind of instruction: a mechanism to try, not just a target.
Isosceles-case gap (Q=A) is correctly flagged again as still outstanding
and explicitly scoped as not blocking the generic case.

### Diversity / shared-gap-plateau check (the second thing dispatch asked me to verify)

I read `math-explorer-newframing`'s report in full. Its negative search is
genuinely substantive, not superficial: it tested 5 distinct auxiliary-
construction ideas (inversion at A applied to two different point sets,
two alternate direct concyclicities, a radical-axis characterization of O,
and fixed-point/fixed-direction of line KL), each with quantified numeric
residuals calibrated against known-true facts at ~1e-16 (so a "false" verdict
at 1e-2–1e-3 residual is a real refutation, not numerical noise) — and it
caught and correctly diagnosed one red herring (the "pow(A, circle(K,B,M))
invariant," which is a trivial consequence of A,M,B collinearity, not a real
discovery) rather than accepting it uncritically. It also independently
re-tested `spiral-similarity-bootstrap`'s framing with a disjoint set of
candidates from round 2's spiral-lens explorer and got the same negative
result. This is now genuinely two independent rounds (round 2's spiral-lens,
round 3's newframing) of real, quantitative negative search over the
auxiliary-construction space, not two rounds of the same superficial check
repeated. I accept the outliner's conclusion that forcing a new top-level
target this round would not be productive — the search was real.

That said, two things worth flagging for the record (not blocking this
round's build set):
- The search space tested is specifically "alternative auxiliary
  circles/points/inversions." It has not tested a structurally different
  *strategy class* entirely divorced from the AKLQ-concyclic reduction (e.g.
  trigonometric Ceva/Menelaus directly on the three hypothesis angles without
  routing through any auxiliary point at all) — `math-explorer-newframing`
  itself names this as a candidate technique, but it is technique diversity,
  not framing diversity, and the outline doesn't put it in this round's build
  set. Given the strength of this round's genericity result, I agree with
  deferring it — but if round 4 doesn't fully close gap 2, this genuinely-
  untried strategy (no auxiliary point/circle at all) should be the next
  thing an explorer scouts, not another lever on the same branch-selection
  gap.
- All 4 build-set approaches now share the identical top-level target
  (O·(C−B)=(|C|²−|B|²)/4 / AKLQ-concyclic). This is a 3-round-deep shared
  target. It is currently justified by two rounds of honest negative search
  plus (new this round) a near-solved status on one branch of it — but the
  next outliner should not treat "no alternative target found" as permanently
  settled; re-open the search once (or if) gap 2 also proves stubborn.

### Held out of build set (agree with outliner)
- `coordinate-bash` — superseded by `coordinate-bash-resultant`'s cleaner
  recipe; no new lever; correctly kept live in the population but not
  re-dispatched.
- `power-of-point-secants` — self-reported non-independent route; nothing
  new to add.
- `spiral-similarity-bootstrap` — doubly refuted (round 2 + round 3
  independent probes); correctly never registered, stays out of the pool.

### Ranking actions taken
- Registered `coordinate-bash-resultant-boundary` via `copy_approach` from
  `coordinate-bash-resultant` (inherits Elo/counts as an identical twin, per
  the tool's semantics).
- Ran `update_ranking` across the whole field (10 comparisons): the two
  `coordinate-bash-resultant*` slugs beat `fixed-point-concyclic`,
  `ptolemy-trig-identity`, `coordinate-bash`, and `power-of-point-secants`
  (closest to solved, now independently verified genericity); `fixed-point-
  concyclic` and `ptolemy-trig-identity` drew (comparable partial progress,
  both closed a real sub-gap this round) and both beat `power-of-point-
  secants` (weakest, admittedly non-independent); `coordinate-bash` beat
  `power-of-point-secants` (more machinery, still honest negative report).
  Resulting order: `coordinate-bash-resultant` (1570.7) >
  `coordinate-bash-resultant-boundary` (1545.0) > `fixed-point-concyclic`
  (1512.5) > `coordinate-bash` (1511.7) > `ptolemy-trig-identity` (1501.7) >
  `power-of-point-secants` (1371.7).

build set: coordinate-bash-resultant, coordinate-bash-resultant-boundary, fixed-point-concyclic, ptolemy-trig-identity
