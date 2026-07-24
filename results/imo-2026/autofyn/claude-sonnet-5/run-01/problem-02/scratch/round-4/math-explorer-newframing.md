## imo-2026-02

### Distinct openings (new framings, far from the existing field)

**Opening 1 (primary, verified structurally, genuinely new): A-centered inversive
swap σ, turning circle(AKL) into a computable LINE whose direction pins down AO.**

Define σ := ρ∘ι, where ι is inversion centered at A with power k := AB·AC, and
ρ is reflection across the internal bisector of ∠BAC. This is the classical
"inversive similarity that swaps B and C" (I verified numerically, 4 triangle
shapes: σ(B)=C, σ(C)=B exactly, to machine precision). None of the six existing
approaches (coordinate-trig-bash, labeling-duality, antipode-perp-bisector,
trig-ceva-chase, nine-point-link, complex-circle-power, two-step-spiral-chain)
use this map — it is a structurally different lever: instead of parametrizing
K, L or chasing angles around the antipode A* of Γ=circumcircle(AKL), it maps
Γ itself (which passes through the inversion center A) to a **line**.

Concretely (I derived and numerically verified each fact below, first with
random non-hypothesis-satisfying K,L to keep the fact hypothesis-free and
general, using Python/numpy — perpendicularity and distance checks all
matched to 1e-14–1e-16 across multiple random trials):

1. **Classical fact** (pure inversion ι, no reflection yet): since A lies on
   Γ (center O, radius R = AO), ι(Γ) is a line ℓ perpendicular to AO, at
   distance k/(2R) from A. (Standard inversive-geometry fact — "a circle
   through the center of inversion maps to a line perpendicular to the
   diameter through that center"; citable directly, easy from-scratch proof
   via the inversion-distance formula |P*Q*| = k|PQ|/(AP·AQ).)
2. Composing with the isometry ρ (which swaps B,C by construction, verified
   numerically): ℓ_Γ := σ(K)σ(L) = ρ(ℓ) is a line **perpendicular to ρ(AO)**,
   at the same distance k/(2R) from A. (Reflections preserve perpendicularity
   and distances from the fixed point A — I re-verified this directly with a
   controlled test after catching and fixing a bug in an earlier ad hoc
   check; confirmed to 1e-16 on multiple trials.)
3. σ(M) and σ(N) are also cleanly computable: since M is the midpoint of AB
   (at distance AB/2 from A on ray AB) and ι has power k=AB·AC, σ(M) lands on
   ray AC (because ρ swaps the two rays) at distance AB·AC/(AB/2) = 2AC from
   A — i.e. **σ(M) is the point on ray AC with C as its own midpoint of
   A·σ(M)** (AC extended beyond C by its own length). Symmetrically, σ(N) is
   on ray AB with B as the midpoint of A·σ(N). (Verified numerically exactly,
   4 configurations.)

**Why this is a genuinely different top-level target:** OM=ON is normally
attacked either by computing O directly (coordinate-trig-bash), by a
power-of-a-point identity (labeling-duality), or by chasing the antipode A*
of A on Γ (antipode-perp-bisector). This opening instead reconstructs O's
**direction from A** (via a computable line through the inversive images of
K and L, i.e. two points the hypotheses directly constrain) and its
**magnitude** (R = circumradius of AKL, obtainable from the Law of Sines in
triangle AKL, e.g. 2R = AK/sin∠ALK), without ever computing O as an
intersection of two perpendicular bisectors or as an explicit (x,y) pair.
This turns "prove O is equidistant from M,N" into "prove the direction of AO
(reconstructed via σ(K),σ(L)) and its magnitude place O on the specific line
perpendicular-bisector(M,N)" — a genuinely different computational route.

**Status of this opening: NOT carried through to a proof or even to a full
sub-target statement — this is exploratory scouting, stopped deliberately at
the point where the outliner can pick it up.** What's rigorously established
(as general, hypothesis-free classical facts, so no risk of numerical
coincidence): the perpendicularity/distance relations in (1)-(2), and the
explicit images of M,N in (3). What remains completely open: translating the
three angle hypotheses (∠KBA=∠ACL=θ, ∠LBK=∠LNC, ∠LCK=∠BMK) into a
description of the *direction* of line σ(K)σ(L) (this requires expressing
∠(σ(K)−A, σ(L)−A)-type quantities via the standard inversion-angle formula,
which is a genuine new sub-computation, not yet attempted), and then closing
the loop to OM=ON. This could plug directly into the certified
`lemmas/antipode-reduction.md` (A*=2O−A) since knowing O's direction+distance
from A gives A* directly (A*=2O−A), potentially giving a cleaner route to
`A*B=A*C` (the same target antipode-perp-bisector is stuck on) that never
needs the still-open L1/L2 angle formulas.

**Cheap-kill check to try immediately next round (before deep development):**
express ∠(σ(K)−A,σ(L)−A) via the standard formula relating inversive angles
to original angles (inversion is conformal — angles at points OTHER than
the center are preserved up to orientation reversal by ρ∘ι restricted... but
angles AT A itself, i.e. ∠KAL vs ∠σ(K)Aσ(L), need the direct formula since A
is the singular point of ι). If this reduces immediately to ∠KAL (a natural
angle at A, itself expressible from the hypotheses via the inscribed-angle
theorem in Γ: ∠KAL = 180°−∠KOL/2 type relation, or directly via known
sub-angles), that would be a strong, cheap sign this opening is tractable in
1–2 more steps; if it instead reintroduces the full (r1,r2) parametrization
data, this is a bypass-that-isn't (same failure mode trig-ceva-chase
honestly reported in round 3) and should be reported as such, not forced.

**Opening 2 (secondary, likely NOT new — flagging as probable collapse,
per the plateau-breaking instruction to test candidates honestly):**
complex numbers with Γ as the unit circle (A,K,L as unit complex numbers)
— this is exactly `complex-circle-power` (dormant since round 1, never
built). Re-reading its own file: it already derives, before any builder
touched it, that the target becomes `2Re(A(B̄−C̄)) = |C|²−|B|²` in the
"O at origin" frame, and explicitly flags this as algebraically matching
coordinate-trig-bash's `O_x=p/2` up to a frame-translation subtlety the
file itself hasn't resolved. Because the whole point of "O at origin" is
just a rotation+translation of the same circumcenter computation, and the
same three angle hypotheses have to be re-expressed as constraints on K,L's
arguments (i.e. re-deriving the same (r1,r2)-type data in a different
notation), I judge this does NOT constitute a genuinely different top-level
target — it is very likely to collapse into the same wall once built,
exactly like trig-ceva-chase did this round. I recommend NOT prioritizing
it as "new" — if pursued at all, pursue it only for the power-of-a-point
secant-identification idea in its step 4 (identifying line BK's second
intersection with Γ as a named point), which is a distinct sub-idea not
tried by any live approach, but this is a narrow shot, not a fresh framing.

### Candidate technique(s)
Inversive geometry: the classical "circle-through-inversion-center maps to a
line" fact, combined with the A-swaps-B,C inversive similarity (standard
configuration, appears in mixtilinear-incircle-style problems) — cite via
knowledge_base.md "Synthetic toolkit: ... inversion, spiral similarity" entry.
Combine with Law of Sines in triangle AKL for the magnitude R, and the
already-certified `lemmas/antipode-reduction.md` for the final hookup to
OM=ON via A*=2O−A.

### Cheap-kill candidates
- Before developing Opening 1 further: check whether ∠σ(K)Aσ(L) reduces to
  ∠KAL cheaply (see "cheap-kill check" above) — if it doesn't collapse to a
  clean angle-at-A expression in 1–2 lines, this opening carries real risk of
  reintroducing the same (r1,r2) computation in disguise; test this FIRST.
- Parity/pigeonhole: not applicable to this continuous-geometry problem.

### Knowledge-base entries to use
- "Synthetic toolkit: angle chasing, power of a point ..., inversion, spiral
  similarity, projective ideas" (knowledge_base.md line ~129-131) — cite the
  inversion sub-entry for Opening 1's core mechanism.
- The already-certified lemma cache: `lemmas/antipode-reduction.md` (hookup
  target), `lemmas/coordinate-om-on-reduction.md`, `lemmas/median-length-power-reduction.md`,
  `lemmas/radical-axis-form-of-TI.md` (all confirmed algebraically equivalent
  scalar targets — Opening 1's promise is that it might reach one of these
  via direction+magnitude reconstruction rather than direct computation).

### Analogous past problems (cruxes)
Per the run history note ("The crux corpus currently has zero geometry
entries"), and I did not find a geometry subtopic in the corpus consistent
with that prior finding — I did not re-run the query since round 1/2/3
explorers already established this and it's recorded as a standing fact in
`run_state.md` Rules. None expected; none found.

### Prior progress
See `results/imo-2026-02/current.md` — three live, mutually-equivalent
scalar-target reductions (O_x=p/2 / power-of-point / A*B=A*C), all
reviewer-certified as equivalent, none closed from the three angle
hypotheses. `antipode-perp-bisector`'s L1/L2 angle formulas remain the
sharpest open sub-target on the existing field; `coordinate-trig-bash`'s
existence/uniqueness of (r1,r2) is fully closed, only the final
substitution remains.

### Dead ends (do not retry)
All previously-recorded dead ends stand (see `run_state.md` Rules and
`current.md`): two-step-spiral-chain's spiral-similarity/concyclicity
mechanisms; antipode-perp-bisector's "270° identity," spiral-similarity-at-B
readings, tangency/secant shortcuts; trig-ceva-chase's final step (confirmed
not a bypass). I did not re-test any of these. My own numerical probe of the
FULL hypothesis system via fsolve (testing the σ-map's effect on M,N,O for
"solved" (K,L)) produced OM≠ON for the found roots — this is expected and
consistent with prior rounds' finding that raw fsolve on the angle equations
alone (without enforcing containment/orientation) lands on the wrong branch,
not a new counterexample or refutation of anything; I did not chase fixing
the containment constraints in this round (out of scope for a framing scout).

### Small-case / intuition notes
- (Conjecture, general theorem not tied to hypotheses) σ(K)σ(L) is a line
  perpendicular to ρ(AO) at distance k/(2R) from A — verified numerically to
  1e-14–1e-16 on 5 independent random (non-hypothesis-satisfying) triples
  (A,K,L); this is really a classical fact, not really a conjecture, just
  newly re-derived and confirmed here rather than found in the KB verbatim.
- σ(B)=C, σ(C)=B, σ(M)=point with AC extended beyond C by AC (i.e.
  A,C,σ(M) with C the midpoint), σ(N)=symmetric on ray AB — verified exactly
  (machine precision) on 4 triangle shapes.
- I did NOT verify any claim connecting this machinery to the actual
  hypothesis-satisfying (K,L) — that translation (turning the three angle
  hypotheses into a direction-of-ℓ_Γ statement) is the genuinely open part
  of this opening and is flagged as such, not glossed over.
