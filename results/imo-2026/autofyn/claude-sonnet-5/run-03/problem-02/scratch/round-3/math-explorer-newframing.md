## imo-2026-02

### Setup used
Reused/extended round-2's `explore.py` parametrization (A=(0.3,2.7), B=(-1.5,0),
C=(2.2,0.1); K on ray from B at angle θ=∠KBA to BA, L on ray from C at angle
θ=∠ACL to CA — hypothesis 1 built in; rK,rL solved from hyps 2,3 via `fsolve`
at xtol=1e-13; filtered by all four containment conditions), giving 100+ valid
family members over θ∈[5°,80°]. Re-verified OM=ON to 1e-14 throughout (sanity
check on the reused setup). All numeric code in `/tmp/round-3/probe.py`,
`probe2.py`, `probe3.py`.

### Distinct openings
None of the genuinely-new auxiliary-construction ideas tested this round
survive contact with numerics — every one either reduces to the known target
or is outright false. **This round's real contribution is negative but
strong**: it closes off essentially the whole "different auxiliary circle /
inversion" search space, reinforcing (via independent numeric confirmation
using a different triangle and a different parametrization than round 2's
spiral-lens) that the AKLQ-concyclic identity is not an artifact of one
framing but a structural bottleneck. Concretely tested and REFUTED as
distinct routes (all false to ~1e-3–1e-2 relative residual, calibrated
against known-true facts at ~1e-16, so these are genuine failures, not
numerical noise):
1. **Inversion at A**: K\*,L\*,B\*,C\* concyclic — false. M\*,N\*,K\*,L\*
   concyclic — false. K\*,B\*,M\* collinear / L\*,C\*,N\* collinear (testing
   whether the circle-through-A-implicit hypotheses become clean lines under
   inversion) — false, and moreover the two residuals are *equal and opposite
   in sign* at every θ tested (col(K\*,B\*,M\*) = −col(L\*,C\*,N\*) to 3–4
   digits), which is a real but so-far unexplained sign-symmetric relation —
   possibly connected to the certified σ-symmetry (`lemmas/sigma-symmetry.md`)
   but not pursued further; flagging as a curiosity, not a lead.
2. **Direct alternate concyclicities** (no inversion): B,K,L,C concyclic —
   false. K,L,M,N concyclic — false.
3. **Radical-axis idea**: is O on the radical axis of circumcircle(ABC) and
   the circle with diameter MN? Tested `pow(O,circABC) − pow(O,circ-diam-MN)`
   across the family — NOT constant (varies from −2.29 to −3.17 over the
   sampled range), so O is not simply characterized this way. Dead end.
4. **"Power of A wrt circle(K,B,M) is family-invariant"** — initially looked
   like a strong new invariant (constant to 10 decimal places across the
   whole family!), but this is a RED HERRING: it is a trivial consequence of
   A, M, B being collinear (M is the midpoint of AB), so pow(A, any circle
   through B and M) = AM·AB (signed) regardless of the third point K on the
   circle — true for every point K, not just the hypothesis-satisfying ones.
   Confirmed algebraically (secant-line power-of-a-point through collinear
   A,M,B), not a genuine discovery. Do not re-propose this.
5. **Line KL fixed direction / fixed point**: the normal vector of line KL
   drifts slowly (0.0264 → 0.0270 in the a-coefficient over θ∈[5°,50°]) — not
   exactly constant, so KL does not stay parallel to a fixed direction, and
   plotting the family shows no common point of concurrency. Not pursued
   further (the drift, while small, is well above the 1e-13 numerical floor,
   so it is a genuine — if slow — variation, not an exact fact).

### spiral-similarity-bootstrap's one-angle circle-membership idea (dispatch item 1)
Round 2's spiral-lens explorer (`/tmp/round-2/math-explorer-spiral.md`) already
tested this exhaustively: 8 distinct one-angle directed-angle identity
candidates meant to place K or L on an auxiliary circle through 2 of
{B,C,M,N,Q} without invoking the other free point — **all failed** except the
two that are algebraically identical to the AKLQ-concyclic target itself. I
independently re-tested a disjoint set of candidates this round (inversion-
based membership, B/K/L/C, K/L/M/N) and found the same pattern: no shortcut,
only the same target or outright falsity. **Verdict confirmed and now doubly
independently corroborated**: the one-angle circle-membership idea is not a
distinct route — it secretly reduces to (or is strictly weaker than) the same
AKLQ-concyclic identity, or is simply false. Do not revive
`spiral-similarity-bootstrap.md` as outlined; its only surviving content is
the trivial homothety fact in step 6 (already noted in round 2 as
insufficient alone).

### Candidate technique(s)
Given the exhaustive negative results above, the outliner's best options for
a genuinely different top-level target are no longer "find a different
auxiliary circle/point" (that space is now heavily searched and empty) but
either (a) **push the direct algebraic/trig computation harder** — treat
OM², ON² (or equivalently the AKLQ-concyclic Ptolemy/cross-ratio identity) as
explicit trig functions of the single free parameter θ and grind out the
identity via sum-to-product / Weierstrass substitution (this is really what
`coordinate-bash-resultant` and `ptolemy-trig-identity` are already doing —
not a new framing, but the most promising *remaining* route per current.md's
own assessment), or (b) accept that AKLQ-concyclic is the true crux and try a
genuinely different **proof technique** for that one identity that isn't
coordinate bash: e.g. a **trigonometric Ceva/Menelaus** identity relating the
three hypothesis angles directly (knowledge_base.md's "trig cevians
(Ceva/Menelaus)" entry), or a clean **directed-angle chase culminating in
Ptolemy's inequality equality case** (knowledge_base.md's Ptolemy entry,
already partially used by `ptolemy-trig-identity` and certified in
`lemmas/general-ptolemy-equality-concyclic.md`) pushed to completion using
the σ-symmetry to halve the casework. Both of these are technique variations
on the SAME target, which CLAUDE.md's rule technically discourages as "too
close" — but given this round's exhaustive search found no viable
alternative top-level target, I flag this honestly: the population may
legitimately need to converge on proving this one identity by whichever
technique closes the remaining algebra, rather than keep searching for a
different target that likely doesn't exist for this problem's actual
difficulty (IMO P2, not P3/P6 — the intended solution plausibly IS a single
clean synthetic fact plus one computation, matching what 5 rounds of
independent approaches have converged on).

### Cheap-kill candidates
None found this round beyond what's already recorded. The σ-symmetry sign
relation noted in item 1 above (col(K\*,B\*,M\*) = −col(L\*,C\*,N\*)) is worth
a quick algebraic check next round as a possible small structural lemma, but
it is NOT a proof shortcut by itself.

### Knowledge-base entries to use
- Geometry / Synthetic toolkit: inversion (tested exhaustively this round —
  ruled out as a shortcut for this problem, worth recording so it isn't
  re-tried), radical axes & radical center (tested, ruled out), trig cevians
  (Ceva/Menelaus) — candidate technique for finishing the central identity,
  not yet tried by any approach.
- Ptolemy entry (already in use via `lemmas/general-ptolemy-equality-concyclic.md`).

### Analogous past problems (cruxes)
Did not re-query the crux corpus this round (per the recorded per-role rule
below and round-1/round-2's finding that geometry-domain crux entries are
sparse/absent); no new analogous crux found. If the outliner wants this
checked freshly, the corpus subtopic filter to try is geometry /
circle-configuration or geometry / concyclicity, per
`crux_moves_documentation.md`.

### Prior progress
Same central fact as current.md: all approaches reduce to proving A,K,L,Q
concyclic (Q = reflection of A in perp-bisector(MN)), equivalently
O·(C−B) = (|C|²−|B|²)/4. `coordinate-bash-resultant` has a complete,
reviewer-verified proof of this identity for ONE concrete rational triangle;
genericity to symbolic (a,c) is the open item. Nothing in this round's search
closes that gap or opens a different one — see below.

### Dead ends (do not retry)
- `spiral-similarity-bootstrap.md` as outlined (steps 1–5): doubly confirmed
  dead (round 2 spiral-lens + this round's independent probes). Only step 6
  (trivial homothety fact) survives and is insufficient alone.
- Inversion at A applied to {K,L,B,C} or {K,L,M,N}: does not produce
  concyclic/collinear images (this round, new negative result).
- B,K,L,C concyclic; K,L,M,N concyclic: both false (this round, new negative
  result).
- O on radical axis of circumcircle(ABC) and circle-with-diameter-MN: false,
  pow difference is not constant across the family (this round, new negative
  result).
- "pow(A, circle(K,B,M)) is a family invariant": true but TRIVIALLY so
  (A,M,B collinear) — not a real discovery, do not re-propose as a lead.
- Line KL passing through a fixed point / staying parallel to a fixed
  direction: numerically false (slow but genuine drift in the line's normal
  vector).

### Small-case / intuition notes
All labeled conjecture/numeric evidence only, single test triangle
A=(0.3,2.7), B=(-1.5,0), C=(2.2,0.1), θ∈[5°,80°], ~130 family members.
The exhaustive negative search this round is itself the main "intuition":
it suggests the problem genuinely has no shortcut auxiliary construction
bypassing AKLQ-concyclic — consistent with this being an IMO P2 (not P3/P6)
where the intended difficulty is likely concentrated in cleanly proving ONE
non-obvious identity (via a well-chosen trig/Ptolemy computation) rather than
requiring a totally different high-level idea. Recommend the outliner
treat "prove AKLQ-concyclic in general" as the problem's actual content and
diversify by PROOF TECHNIQUE for that one target (trig-Ceva vs. Ptolemy vs.
symbolic-genericity-extension of coordinate-bash-resultant) rather than by
top-level target, while still keeping at least one slot open in case a later
round's fresh eyes spot something this round's search missed.
