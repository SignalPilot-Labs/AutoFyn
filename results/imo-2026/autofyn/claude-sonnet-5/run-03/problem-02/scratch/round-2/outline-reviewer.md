# Outline review — imo-2026-02, round 2

## Context recap
Round 1 gap-free-verified two shared lemmas (imported verbatim by all approaches
below, not re-derived):
- `vector-reduction-OM-ON.md`: OM=ON ⟺ O·(C−B) = (|C|²−|B|²)/4 (A at origin).
- `amnq-concyclic-and-reduction.md`: Q := reflection of A in ⊥-bisector(MN);
  A,M,N,Q concyclic; and **concyclic(A,K,L,Q) ⟹ OM=ON** — fully proved, gap-free
  (isosceles case AB=AC, where Q=A, is a known unhandled edge case common to
  every approach below).

The single open problem for the whole population is proving **A,K,L,Q
concyclic** from the three hypothesis angle equalities. This round's two
explorers ran an exhaustive, family-wide (not single-instance) numerical
sweep and found **no alternative structure**: no fixed length ratio, no
hidden similar triangle touching K or L (56-triangle AA search, family-wide),
no hidden concurrency/concyclicity among {A,B,C,K,L,M,N,Q} beyond the known
(A,M,N,Q) and the target (A,K,L,Q) (70-subset search, reconfirmed twice), no
spiral similarity fixed point. This is strong evidence the reduction to
(Q, concyclic-A,K,L,Q) is the actual crux of the problem, not an artifact of
one framing — so continuing to attack this one identity via genuinely
different *algebraic mechanisms* is justified this round, not merely
restating the plateau. That said: this is now round 2 on the same central
identity. Per CLAUDE.md's shared-gap-plateau rule, if none of these four
mechanisms closes it this round, round 3 must bring a genuinely different
*reduction* (not just a different vehicle for the same target) — e.g.
abandon Q altogether and look for a different circle characterization of
OM=ON directly.

## Per-approach verdicts

### ptolemy-trig-identity — new — APPROVE
Reduces the concyclicity target to a **length** identity
`AL·KQ = AK·LQ + KL·AQ` (Ptolemy), a genuinely different algebraic mechanism
from angle-chasing or coordinate elimination (length algebra vs angle algebra
vs polynomial elimination). Checked:
- Ptolemy's theorem and its equality-case converse are correctly cited
  (`knowledge_base.md` "Circle/triangle configuration facts") and the
  converse's validity condition (four points already in **convex cyclic
  order**) is explicitly flagged as a genuine sub-lemma to prove (Step 2), not
  assumed — good, this is exactly the kind of leap that would otherwise be
  fatal (a wrong pairing gives a residual of 10–50 per the trig-explorer's
  numerics, i.e. a false statement, not just an unproved one).
- Step 2's containment-based order argument is sketched, not written out —
  flagged correctly as open, acceptable for an outline.
- Steps 3–4 (Law of Sines in ABK/ACL/BMK/CNL) are mechanically sound: each
  triangle has one hypothesis angle and one known side (AB, AC, BM, CN), so
  the other sides follow by Law of Sines — no circularity.
- Step 6 (the actual elimination reducing Ptolemy's difference to 0) is
  honestly marked "not executed," with the explicit warning to keep the
  family's free parameter symbolic throughout (correctly informed by this
  round's explorer confirming no length ratio is family-constant) and to
  verify symbolically with sympy before writing the human proof — good
  practice given round-1's coordinate-bash Gröbner blowup.
- No hand-waving found: every non-trivial step is flagged as an explicit
  open step with a stated mechanism, not asserted.

Verdict: sound skeleton, real (not fatal) open gaps. APPROVE.

### fixed-point-concyclic — revise — APPROVE
Keeps the certified Steps 1–2 verbatim (correct — no need to re-derive
already-certified lemmas) and swaps only Step 3's mechanism from directed-angle
chasing (stalled two rounds now, in effect) to a **complex-number cross-ratio**
computation. The cross-ratio-real ⟺ concyclic criterion is a standard fact and
the outline gives its own short proof sketch (Möbius map to 0,1,∞, circle↦real
axis) rather than just citing it uninterpreted — acceptable, since this is a
well-known and easily verified identity, not a leap.
- Step 2's branch-selection (which signed/directed ratio equality corresponds
  to which hypothesis, fixed by the containment conditions) is correctly
  flagged as an open sub-step needing to be nailed down explicitly — this is
  exactly where round-1's directed-angle chase got stuck, so flagging it
  honestly here (rather than hiding it) is the right call.
- The outline itself states the self-aware caveat: if this stalls too, that's
  evidence the difficulty is combinatorial/algebraic degree, not choice of
  algebra — good epistemic hygiene, not overclaiming.
- Isosceles case (Q=A) is deferred to "Watch out for," same open item shared
  by every approach.

Verdict: legitimate distinct algebraic vehicle for the same proven-correct
reduction; no fatal flaw. APPROVE.

### coordinate-bash — advance — APPROVE
Reuses the certified reduction, rotation parametrization, and the new
certified σ-symmetry lemma (swap B↔C,K↔L,M↔N — re-verified round 1, gap-free)
to cut the elimination's work roughly in half, then proposes Sylvester
resultants (eliminate t1 via hyp-3, mirror via σ for t2/hyp-2) instead of a
full 4-variable Gröbner basis. This is a legitimate, concrete escalation from
round 1's stalled generic Gröbner attempt — resultant elimination targeting
one variable at a time is a standard, often cheaper alternative when a full
Gröbner basis blows up.
- Step 4's fallback (numerically confirm the resultant vanishes at several
  points before finishing the exact symbolic proof) is correctly scoped as a
  guide only, not a substitute for the final proof — consistent with
  CLAUDE.md's "prove, don't conjecture" rule.
- Isosceles case still unhandled — flagged, not hidden.

Verdict: concrete, mechanical, correctly scoped next step. APPROVE.

### coordinate-bash-resultant — copy of coordinate-bash — APPROVE
An independent elimination strategy for the identical target: Weierstrass
substitution (u=tan(β/2)) to remove the sin²+cos²=1 side-relation before
running Gröbner/resultants in 3 variables instead of 4-with-a-constraint. This
is a reasonable, well-motivated alternative computational path (the
extra ideal generator from s²+cc²=1 is a known common cause of Gröbner
blowup), genuinely worth running in parallel rather than sequentially since
either could succeed where the other stalls, and the two together generate
useful negative information if both fail (per the outline's own honest
framing).
- One real gap correctly flagged: u=tan(β/2) has a pole at β=π, which must be
  checked (not assumed) not to occur in the valid configuration range — good,
  this is a genuine soundness check for the substitution, not filler.

Verdict: legitimate branch, not a redundant duplicate — approved for the
copy_approach split.

### power-of-point-secants — not re-outlined this round
The outliner correctly did not resubmit this approach: round 1's build
self-reported it is algebraically identical to the shared central identity
(no independent leverage) and documented a negative search for alternative
secant constructions. Leaving it out of this round's build set is correct —
it has nothing new to contribute until a genuinely different secant
construction is found. Remains registered in the population (Elo now
correctly the lowest, reflecting round-1's self-admitted redundancy) but not
selected to build this round.

### spiral-similarity-bootstrap — dead
This round's spiral-lens explorer ran an exhaustive family-wide numerical
sweep (not just single-instance, as round 1 did) and refuted every non-trivial
step of this outline (no fixed spiral-similarity center for B↦K,C↦L; S moves
substantially and fits no line; none of 8 candidate one-angle circle-membership
identities hold except ones equivalent to the already-known target). Correctly
never registered (was RETHINK in round 1); still dead, no action needed. Do
not resubmit without a fundamentally different mechanism.

## Diversity assessment
All four build-set approaches attack the same isolated sub-target (A,K,L,Q
concyclic) but via four genuinely different algebraic mechanisms: pure length
algebra (Ptolemy/Law-of-Sines), complex cross-ratio, Cartesian
resultant-elimination, and Weierstrass-rationalized Gröbner. This is
technique diversity on a shared, well-isolated gap, backed this round by an
exhaustive negative search ruling out alternative structures — not a
same-framing rubber-stamp. Flagging per CLAUDE.md: if all four again fail to
close the gap, round 3 must pivot to questioning the reduction itself (a
different auxiliary point/circle in place of Q), since four algebraic
vehicles on the identical target would then constitute genuine evidence of a
structural wall, not just unlucky computation.

## Ranking
Registered `ptolemy-trig-identity` (new, cold-start 1500) and branched
`coordinate-bash-resultant` from `coordinate-bash` via `copy_approach`
(inherits Elo/counts). Ran `update_ranking` anchoring round-1 outcomes:
fixed-point-concyclic and coordinate-bash (both fully-verified, gap-free
partial progress) beat power-of-point-secants (self-admittedly non-independent,
weakest position) and drew with each other (comparable maturity, converged
identical wall). New entries ptolemy-trig-identity and coordinate-bash-resultant
were each anchored with one win over the weakest established approach
(power-of-point-secants) to separate them from cold-start 1500 without
overclaiming against the two strongest lines, and drew coordinate-bash vs
coordinate-bash-resultant (siblings, equal footing pending real build
outcomes). Post-update standings: fixed-point-concyclic 1537 >
ptolemy-trig-identity 1517 > coordinate-bash 1516 > coordinate-bash-resultant
1514 > power-of-point-secants 1416. `stale` cleared on all five.

## Build set
All four approved approaches — they attack the isolated crux via four
independent mechanisms, maximizing the chance at least one closes it this
round, and none shares an obvious duplicate flaw (each has its own distinct
failure mode to watch: wrong cyclic order for Ptolemy, wrong branch for
cross-ratio, resultant blowup for coordinate-bash, Weierstrass pole for
coordinate-bash-resultant).

build set: ptolemy-trig-identity, fixed-point-concyclic, coordinate-bash, coordinate-bash-resultant
