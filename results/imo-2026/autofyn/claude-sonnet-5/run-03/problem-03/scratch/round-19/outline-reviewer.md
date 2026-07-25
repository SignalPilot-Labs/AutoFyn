## imo-2026-03 — outline review, round 19

### Independent spot-check: lp-vertex-maximizer's n=2 closed-form Existence Theorem claim

This was flagged by dispatch as the highest-risk claim this round (explorer numeric
findings previously had a scope bug in round 18 — the "near-maximizer" point that
turned out to violate the region's own defining inequality). I re-derived every
algebraic step from scratch, independent of the explorer's script, and additionally
ran my own 20,000-trial exact-`Fraction` sampler.

Region (confirmed against `global-lp-vertex-sufficiency.md`'s own Section 0
definition, lines ~3215-3226): p1+p2+p3=1, p1<1/2, d1:=p1-p2>γ(2)=1/7,
d2:=p2-p3>γ(2). Target c(2)=1/2+γ(2)/2=4/7.

- **Step 1** (p1=(1+2d1+d2)/3, hence p1>10/21): substituting p2=p1-d1, p3=p1-d1-d2
  into p1+p2+p3=1 gives 3p1-2d1-d2=1, i.e. p1=(1+2d1+d2)/3 — confirmed algebraically.
  d1,d2>1/7 forces 2d1+d2>3/7, giving p1>(1+3/7)/3=10/21. **Correct.**
- **Step 3** (rank-order equivalence p3>(p1-p2) iff p1<1/2): p3-(p1-p2) =
  (1-p1-p2)-(p1-p2) = 1-2p1. So p3>(p1-p2) exactly iff p1<1/2, which is one of the
  region's own hypotheses (no separate case needed). **Correct**, re-derived
  independently, matches.
- **Step 4** (OddSum(M)=1-p1, bound < c(2)): with order p2,p2,p3,(p1-p2), OddSum =
  rank1+rank3 = p2+p3 = 1-p1 (sum=1). Combined with p1>10/21: OddSum<11/21<12/21=c(2).
  **Correct, strict, unconditional throughout the region.**
- **Numeric cross-check** (own script, independent of explorer's): 20,000 valid
  sampled region points, zero violations of the order claim, zero mismatches between
  predicted `1-p1` and directly-computed OddSum of the actual multiset, zero
  violations of OddSum<c(2); max observed OddSum ≈0.52244, consistent with the
  ≈0.52381 (11/21) bound, both below c(2)≈0.57143.

**Verdict on this claim: solid.** Unlike round 18's SLSQP-numerics scope bug or the
(1,0,1)-branch near-maximizer that turned out to lie outside the region, this
construction is a direct algebraic identity built entirely from the region's own two
defining gap inequalities plus p1<1/2, with no external numeric witness needed to
locate a maximizer — the witness IS the closed form, and the bound follows in one
inequality chain. I found no crack. This can go into the build set as a genuine
closure of the n=2 Existence Theorem (upper-bound direction), not as a numeric
finding to be treated skeptically.

One scoping caveat to enforce on the builder (already flagged in the outline, worth
repeating): this proves n=2 only. The n=3 direct-lift failure (71/94 sampled
violations, unstable rank order of the leftover fragment) is real and the outline
correctly does NOT claim it generalizes — do not let the builder overclaim general n
from this closed form.

### self-similar-induction-on-n: revise → CHANGES REQUESTED

Target: general-k Cardinality-Constrained Half-Sum Lemma GCH(k) via an
extremal-principle/LP-vertex smoothing argument, replacing the confirmed-circular
induction-on-k.

- Technique is sound in principle: fixing an interleaving/rank pattern makes AltSum
  affine in the r_i (coefficient ±1 by parity), and a linear functional on a compact
  polytope (box ∩ hyperplane) does attain its extrema at a vertex — standard LP fact,
  correctly cited as needing a knowledge_base.md citation (builder must actually find
  and cite it, not just assert it).
- The mandatory cheap-kill (step 2 of the outline) is correctly gated BEFORE any
  proof writing — good discipline, keep it mandatory.
- Real gap: step 3 (the smoothing argument that any legal mass transfer within R is
  non-improving) is not yet proved, only evidenced by exact LP (k=2..5, tight
  equality along the whole range — a much stronger evidentiary bar than round 18's
  SLSQP check, correctly distinguished in the outline). Step 4 (enumerating vertex
  shapes and showing the "chain + tied pair" family dominates all others) is stated
  as a to-be-proved claim, not assumed — correctly flagged as unproved.
- Watch-outs are correctly stated and consistent with the record: avoids the
  confirmed-dead induction-on-k peel; correctly forbids re-using SLSQP; correctly
  forbids importing the sibling's vertex mechanism as a black box (re-derive on R's
  own polytope, per the standing Rule 20 in memory) — this is the right call, since
  the two polytopes (R's box-simplex vs. the Σ-shape cut-allocation polytope) are
  genuinely different objects; citing one as if it proves the other would be an
  unsanctioned cross-file dependency, not the sanctioned certified-lemma-cache route.

This is CHANGES REQUESTED, not RETHINK: the target lemma is correctly scoped (not a
sub-fragment split across slugs — it is still working toward the whole GT(m)
closure, GCH(k) is the one remaining named sub-lemma), the technique is legitimate,
and the open gaps are named with a mechanism attached (not a bare "then it follows").
Builder should treat steps 3-4 as the actual proof obligations, not restate the LP
evidence as if it were already a proof.

### global-lp-vertex-sufficiency: revise → APPROVE (scoped to n=2)

As verified above, the n=2 closed-form witness is correct end-to-end. The outline's
skeleton (steps 1-5) matches the verified math exactly, including honestly scoping
n=3 as open and stating precisely why the 1-cut lift fails there (not hand-waved).
One item to hold the builder to: step 4 says "cite the certified result" for the
lower-bound half (achievability of c(2)) to close the n=2 loop fully — builder must
actually locate and cite that certified result by name, not just assert it exists.
Also enforce: Status for the overall approach stays `partial` (general n still
open); only the n=2 sub-result can be described as closed in the write-up.

### lp-duality-split-polytope: advance (light/dormant) — no active build this round

Confirmed by this round's plateau-check explorer: no revival lead found, the
Mass-Constraint technique is proved to structurally cap below the s≥n-1 necessity
target, and the two crux transplant attempts (aimo-0091, aimo-0178) are confirmed to
fail for named structural reasons. Not doomed (its certified Perfect-Tie-Family
Characterization and Generalized Mass-Constraint Theorem remain valid, reusable
results, and the necessity conjecture itself is not refuted) — but there is no new
content to dispatch a builder on this round, and the outline itself says so
explicitly ("no revival lead found... recommend stand by"). To conserve builder
effort, I am NOT including it in this round's active build set — it stays live in
the population (not cut, not marked dead), just not dispatched.

### Diversity check

The two approaches selected for active build (self-similar-induction-on-n,
global-lp-vertex-sufficiency) target genuinely different sub-problems of the overall
proof (GT(m)'s general-k lemma vs. the Existence Theorem's Σ-shape closure) — this is
not a single-gap-trap split, both are named, independent load-bearing pieces of the
overall structure that the run has tracked as distinct since round ~11-13 (per
current.md and the plateau-check explorer's own re-confirmation that they remain
"genuinely different obstructions"). No collapse-to-one-framing concern this round.

### Ranking actions

No new approaches to register (all three outline slugs already in the population).
No branching requested this round. Folding comparisons below, anchoring the two
active slugs against the established leader (`greedy-reduction-geometric`) and
against the dormant/negative-result slug (`lp-duality-split-polytope`), and clearing
stale flags on the touched approaches, including two untouched-this-round slugs with
old evidence (`reciprocal-potential-induction-on-n` dead-end, `discharging-neighbor-transfer`
recommended-for-retirement) so their outcomes vs. this round's live field are
reflected.

build set: self-similar-induction-on-n, global-lp-vertex-sufficiency
