## imo-2026-03

### (1) Plateau verdict: the two gaps are GENUINELY DIFFERENT obstructions, not the same wall

Re-confirming round 13/14/17/19's repeated finding, with a fresh structural check this round:

- **self-similar-induction-on-n's gap** (general Cardinality-Constrained Half-Sum
  Lemma / GT(m) sub-case (i)) lives entirely on the **lower-bound / achievability
  side** of the proof: it is a statement about `OddSum(R∪Γ_{k-1}) ≥ (S+2^k)/2`
  (equivalently `AltSum(R∪Γ_{k-1}) ≥ 1`) for LB's own **cut multiset**, feeding
  the "Liu Bang can guarantee ≥ c(n)" direction. Grep of the file confirms every
  occurrence of "lower bound" in this context refers to LB's guaranteed value,
  never to XY's response. The obstruction (documented in Step 3 of round 18/19)
  is a genuine **missing induction parameter**: the natural single-parameter
  induction on k does not shrink the cap `2^(k-1)` alongside the Γ-index, so a
  correct proof needs a two-parameter family `GCH(j, cap, b; S)` (fixed cap,
  decreasing Γ-index, decreasing count budget) — this is a *combinatorial
  vertex-enumeration* problem over a fixed finite polytope (Lemma LNI already
  shows minimizers have no two "free" opposite-parity coordinates, reducing the
  search to a finite set of tie/boundary multiplicity vectors per k).

- **global-lp-vertex-sufficiency's gap** (n=3 Existence Theorem witness) lives
  entirely on the **upper-bound side**: for a *fixed* partition p in the
  balanced region, exhibit an explicit XY cut-response whose resulting
  multiset has `OddSum ≤ c(n)`. The n=2 mechanism (Section 10.3–10.4 of the
  approach file) is now fully proved and hinges on a **parity fact specific to
  n=2**: splitting piece 1 into (p2, p1−p2) produces an **even-sized** (4
  element) multiset, so the algebraic identity `p3−(p1−p2)=1−2p1` pins the
  fragment's rank unconditionally via the single region hypothesis p1<1/2.
  At n=3 the natural 1-cut lift gives an **odd-sized** (5-element) multiset,
  and the fragment must be compared against *two* untouched pieces jointly
  (p3 and p4) — no single consecutive-gap hypothesis of B(3) pins this, and
  the file confirms numerically (87.6% failure rate, exact arithmetic,
  45,108 trials) that the naive lift genuinely fails, not marginally.

**Why these are not secretly the same wall.** They differ in every load-bearing
respect: (a) direction of the inequality (lower bound on LB's own value vs.
upper bound via an XY response), (b) the object being searched (an abstract
multiset R subject to a cap/count constraint, vs. a concrete finite family of
cut-response *shapes* at one fixed p), (c) the actual missing ingredient
(a second induction parameter that the k=2 proof accidentally hides, vs. a
genuinely new even-sized-multiset construction to replace the odd-sized lift).
The only thing they share is a *toolkit lineage* — both now routinely use
rank-parity/OddSum-AltSum affine-cell case analysis (Lemma BCF / Lemma LNI on
one side, the Flat/Kink Parity Lemma and rank-order identities on the other) —
but this is a shared *technique*, not a shared *obstruction*; each gap's
missing step is independently characterized and neither reduces to the other.
This matches (and extends with a concrete grep-verified check) round 13's,
round 14's, round 17's, and round 19's independent conclusions that these are
different obstructions. **No plateau-break is warranted this round.**

One soft signal worth flagging (not a plateau by itself): self-similar-
induction-on-n's specific sub-target (the general-k Half-Sum Lemma) has now
been the *live* residual for 3 consecutive rounds (18, 19, 20-pending) without
closing, while its *diagnosis* keeps sharpening (round 18: identified the
missing 2-parameter structure; round 19: proved achievability in closed form
for all k, isolated the matching lower bound as the sole remaining piece).
This is normal narrowing-without-closing on ONE approach's own internal
sub-lemma, not a field-wide collapse to one shared wall (the other approach
is working an unrelated gap) — so it does not trigger CLAUDE.md's
multi-approach plateau rule, but is worth a dedicated LP-vertex/enumeration
push next round given how sharply it is now diagnosed.

### (2) Fresh-framing search: crux corpus + knowledge_base.md

Searched `combinatorics` cruxes in subtopics `games-and-strategy`,
`extremal-principle`, `linear-algebra-method`, `invariants-and-monovariants`
(402+39 candidates scanned) for anything resembling (a) an alternating-claim
stick-cutting game, (b) rank-parity/alternating-sum extremal arguments, or
(c) LP-vertex enumeration over a capped, cardinality-bounded polytope.

- No new genuinely-analogous crux found beyond what prior rounds already
  surfaced (`aimo-0560` surrogate-adversary, round 2; `aimo-0119` cheap-kill
  analogue, round 17; `aimo-0091`/`aimo-0178` double-counting, round 18 —
  all already tried/exhausted per the current.md history). Scanned titles like
  `aimo-0117` (dyadic/geometric-sequence domination in a turn game — same
  flavor as the already-explored/subsumed dyadic-potential-invariant, not a
  new lead), `aimo-0596`/`aimo-0854` (pairing/involution strategies — same
  family as the already-refuted 4 bounded-tie-topology constructions for
  global-lp-vertex's Σ-shape gap, not applicable to the *n=3-specific*
  even/odd-multiset-size construction gap it actually has now).
- No top-level alternative framing (beyond the already-catalogued dead ends:
  dyadic-potential-invariant, layer-cake-parity-reframing, structured-
  randomization-upper-bound, reciprocal-potential-induction-on-n,
  discharging-neighbor-transfer) surfaced in `knowledge_base.md` either — I
  did not find a new named KB theorem (e.g. a general LP-duality /
  Farkas-type vertex theorem, or a discrete rearrangement inequality) that
  isn't already in use by the two live approaches. **Conclusion: no fresh
  top-level framing is currently available; the two live approaches remain
  the correct field.** This corroborates round 19's plateau-check finding.

### (3) Concrete unexploited lead surfaced by this check (not a new top-level approach — a within-approach idea)

global-lp-vertex-sufficiency's own file already proposes the mechanistically
correct next probe for n=3 (Section 10.8, "concrete next step"): split piece
1 into **three** fragments (using 2 of n=3's 3 cuts), tying one fragment to
p2 and a second to p3, leaving a third free fragment and p4 untouched — this
gives a 6-element (even-sized) multiset, matching the parity diagnosis. This
has been flagged but **not yet tested even numerically** — a cheap first
step before any proof effort (per CLAUDE.md's cheap-kill discipline) would be
an exact-Fraction sweep of this specific 2-cut/6-fragment shape across B(3)
to see if it clears c(3) uniformly, mirroring exactly how the n=2 witness was
found and verified before being written up.

## Cheap-kill candidates
- global-lp-vertex-sufficiency n=3: exact-Fraction sweep of the specific
  2-cut "tie fragment to p2 AND to p3" 6-element-multiset construction over
  B(3) BEFORE any proof attempt — cheap, well-motivated by the parity
  diagnosis, not yet tried.
- self-similar-induction-on-n general-k Half-Sum Lemma: no new cheap kill
  found this round beyond what's already certified (LNI); the remaining work
  is a genuine vertex-enumeration argument over the diagnosed two-parameter
  family, not amenable to a single cheap test.

## Knowledge-base entries to use
- No new entries beyond what the two live approaches already cite
  (greedy-optimality-oddsum, the various certified lemmas in
  `results/imo-2026-03/lemmas/`). No general-purpose KB theorem (LP duality,
  discrete rearrangement, extremal set theory) not already in use was found
  to be applicable.

## Analogous past problems (cruxes)
- None found this round beyond the already-catalogued and already-exhausted
  `aimo-0560`, `aimo-0119`, `aimo-0091`, `aimo-0178` — no new genuinely
  analogous crux surfaced despite a targeted search of `games-and-strategy`,
  `extremal-principle`, `linear-algebra-method`, `invariants-and-monovariants`
  subtopics in combinatorics.

## Prior progress
See current.md / run_state.md — n=2 Existence Theorem (upper bound) fully
closed and certified; GCH(k) achievability half fully closed for all k≥2;
matching lower bound for GCH(k) general k and n=3 Existence Theorem witness
both remain the two live open gaps, confirmed independent of each other.

## Dead ends (do not retry)
- All 5 previously-retired approaches (dyadic-potential-invariant,
  layer-cake-parity-reframing, structured-randomization-upper-bound,
  reciprocal-potential-induction-on-n, discharging-neighbor-transfer) —
  confirmed still dead, no new lead found reviving any of them.
- 4 bounded-tie-topology families for global-lp-vertex's Σ-shape gap
  (cyclic, linear-chain, descending-chain, star/tree) — irrelevant to the
  n=3 gap anyway (that gap is now about constructing ONE specific witness
  shape at n=3, not classifying the full Σ-shape candidate set).
- Naive 1-cut lift of the n=2 witness to n=3 — confirmed dead again this
  round by re-derivation of the parity argument (odd multiset size breaks
  the single-hypothesis rank-pinning identity).

## Small-case / intuition notes
- Conjectural (numeric, k=2..6, high precision, not proved): the general
  Cardinality-Constrained Half-Sum Lemma's bound is exactly tight for every
  k, strongly suggesting the two-parameter vertex-enumeration argument, once
  found, will be a clean equality-characterization theorem (not just an
  inequality with slack) — worth keeping equality-tracking in mind when
  building the general-k proof.
- Conjectural (numeric, 87.6% failure at n=3): the n=2→n=3 parity
  obstruction is real and large-margin, not a boundary effect — any n=3
  witness genuinely needs an even-sized resulting multiset, reinforcing that
  the 2-cut/6-fragment probe (not a 1-cut variant) is the right next shape
  to test.
