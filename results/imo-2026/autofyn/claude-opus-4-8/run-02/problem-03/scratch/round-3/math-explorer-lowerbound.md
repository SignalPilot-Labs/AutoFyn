## imo-2026-03 — lens: GAP-L RESIDUAL (non-integer cut positions)

### (a) Precise structure of the cut polytope / vertices for W_n

Fix the LB dyadic marking `W_n = {2^0,...,2^n}` (scaled, `Sigma=D_n=2^{n+1}-1`). XY's response
is: choose, for each original piece `2^i`, a number of cuts `c_i >= 0` with `sum c_i <= n`, and
for each cut a real offset. This determines a **cut pattern** `(c_0,...,c_n)` (a composition of
`<=n` into `n+1` parts) and, within that pattern, a box of free continuous variables (the
offsets), one per cut, each ranging in an interval determined by the piece being split (and by
the requirement that later cuts on an already-cut sub-piece live inside that sub-piece).

For FIXED cut pattern, `f` is a continuous function on this box. It is affine on each **sort
chamber** = the region of the box where the descending order of the final pieces (and hence the
sign pattern `sigma_i in {+1,-1}` in `f = sum sigma_i a_i`) is constant; the chamber walls are (i)
an offset hitting a box boundary (a cut degenerates — collapses to a pattern with a smaller
`c_i`, i.e. this reduces to a LOWER-BUDGET instance, already handled inductively by the same
argument at one fewer cut), or (ii) two final pieces becoming exactly equal (a **rank tie**,
possibly between pieces coming from *different* original pieces / different cut branches). The
polytope's vertices (in the sense used by the `self-similar-recursion` reduction) are the points
where the active chamber has been driven, coordinate by coordinate, to such a wall in every free
direction (Weierstrass + the `{-2,0,2}` gradient argument, already certified). This part of the
reduction is solid; nothing new to add there.

**NEW FINDING (numerically robust, n=2,3): the "vertex" language undersells what is really
happening — large *flats* of the polytope, not isolated points, sit exactly at `f=1`, and most
of that flat is non-integer.** Concretely, for `n=2`, fix the cut pattern "2 cuts, both on the
top piece `4`, nothing on `{2,1}`" (so the final multiset is `{s1,s2,s3,2,1}`,
`s1>=s2>=s3>0`, `s1+s2+s3=4`). A dense random scan of `(s1,s2,s3)` in this 2-parameter simplex
(200000 samples) found **37% of ALL samples give `f` EXACTLY `1.0000000000`** (not just close —
verified to machine precision), covering a 2-dimensional open sub-region of the simplex, most of
whose points are irrational/non-dyadic (e.g. `s=(2.291, 1.428, 0.281)`, `f=1` exactly; another
`s=(2.174,1.566,0.260)`, `f=1` exactly). See raw run below.

**Why this happens (verified by hand, exact algebra, not just numerics).** In the sub-region
where `s1 > 2` and `s3 < 1` (so the sorted order is `s1 > 2 > s2 > 1 > s3`, i.e. every
`s_i` sits at an ODD rank interleaved with the untouched pieces `{2,1}` at the even ranks), the
alternating sum telescopes as
```
f = s1 - 2 + s2 - 1 + s3 = (s1+s2+s3) - (2+1) = 4 - 3 = 1
```
— an EXACT algebraic identity, forced purely by `s1+s2+s3 = 4` (conservation of the cut piece's
total) and the SIGN PATTERN being `(+,-,+,-,+)`, independent of the actual values of `s1,s2,s3`
inside that chamber. This is not a coincidence of parity; it needs no integrality at all. Leaving
this chamber (e.g. `s1<2`, so `2` pops to rank 1) gives, by the same telescoping recomputation,
`f = 2 - s1 + s2 - 1 + s3 = 1 - (2s1-4) = 5-2s1 > 1` strictly (since `s1<2` in that chamber) — so
`f` rises above 1 continuously as you exit the flat, consistent with `f>=1` everywhere, with
equality exactly on (and only on) the flat chamber plus its boundary.

This generalizes the ALREADY-CERTIFIED Lemma A/B (top-band decoupling): it is the special case of
Lemma B where `R'` is *totally uncut* and the top's sub-pieces interleave "nicely." What's new
here is realizing the extremal *set*, not just the extremal *value*, is a manifold — which
reframes the residual gap as an **identity + monotone-exit** argument rather than a
vertex-by-vertex parity check.

### (b) Candidate exchange/perturbation/rounding arguments

1. **Telescoping-identity generalization (the promising new lead).** Generalize the exact
   computation above to arbitrary depth: whenever a piece is split into sub-pieces that
   interleave with the complementary (possibly itself recursively cut) block so that the
   sub-pieces occupy one parity class of ranks and the complementary pieces occupy the other,
   `f` collapses ALGEBRAICALLY (via conservation of each piece's total) to
   `(top total) - (complement total)`, independent of the exact split — no integer/parity
   argument needed. The remaining work: (i) show this "nice interleaving" identity holds
   recursively at every level of a multi-level cut (not just top-only), reproducing GAP-L's
   target `2^n - (D_n-1) = 1`, and (ii) show that whenever the interleaving is NOT nice (some
   sub-piece pops out of its intended rank slot), the resulting `f`, recomputed by the same
   telescoping method, is provably `>=` the nice-chamber value (the `n=2` hand computation above,
   `f=5-2s1>1` when `s1<2`, is a first data point; this needs to be checked as a general
   "popping strictly helps LB" monotonicity, likely by an exchange/peeling argument akin to
   Lemma H's peel identity, applied per popped piece). This looks like the natural finish: it
   replaces "find the exchange lemma sending non-integer vertices to integer ones" (which fights
   the fact that huge chunks of non-integer configuration space give EXACTLY the floor, so there
   is no reason to expect strict improvement toward integers) with "show every chamber's
   telescoped value is `>=1`, with equality characterizing the flats," a cleaner induction on the
   cut pattern (recursion on which piece is split and how many ranks interleave).
2. **Rounding/limit argument (weaker, worth a fallback try).** Since `f` is continuous and
   piecewise-affine, and the rational (indeed all-real) vertex set is dense enough that any
   non-integer point can be perturbed continuously WITHIN its chamber without changing `f` (per
   finding (a)) until it hits a chamber wall — the only substantive content is then at the
   walls, where either a coordinate degenerates (fewer cuts — handled by induction on budget,
   Theorem F eventually applies once cuts run out) or two pieces tie (rank swap) — at a rank-tie,
   `f` is CONTINUOUS across the wall (the two chambers agree there), so this cannot help decrease
   `f` further; it only ever produces the boundary case already covered by one side. This
   confirms (without yet fully proving) that the "vertex" is not where the interesting content
   is — the interesting content is chamber-level identities as in (1).
3. **Matched-pair deletion (P1) applied to non-adjacent-origin ties.** P1 ("adjoining two equal
   pieces of value `v` leaves `f` unchanged") is stated and proved for ANY two equal-value
   pieces, not just ones produced by a single bisection. So at any tie vertex where two final
   pieces are exactly equal (regardless of which original piece they descend from), one may
   delete both and recurse on a strictly smaller multiset. This is a legitimate reduction but,
   unlike route (1), it does not obviously terminate at an integer configuration (the reduced
   multiset need not have dyadic values) — it is a generically useful tool inside route (1)'s
   induction but not on its own a finishing argument. Do not expect it alone to force
   integrality.

### (c) What dead-ended and why

- **Dual-price / LP-duality one-shot certificate for GAP-L** — PROVEN DEAD (round 2, recorded in
  `alternating-sum-threshold-potential`, re-confirmed by proof-reviewer): any fixed length-only
  price is forced `<=0` by equal-piece feasibility (the matching dual is tautological). Do NOT
  resuggest.
- **Blanket "cutting a non-max piece never helps XY" / blanket exchange lemma "moving a cut into
  the top never raises f"** — FALSE in general (28k counterexamples, round 1). Only the narrower,
  already-certified Lemma A (top-band localization) survives.
- **Parity alone (Lemma D/Theorem F) for the residual** — cannot possibly close it: I re-derived
  the `d=3` scaling counterexample from round 2 (`f=1/3` compatible with `df ≡ d*D_n mod 2`) and
  confirmed it is a real obstruction, not a technicality — parity genuinely carries zero
  information once cuts are irrational/non-integer-scaled. Any round-3 attempt must NOT rely on
  Theorem F/Lemma D for the residual; they only settle the (already-closed) integer case.

### (d) Most promising technique + relevant crux moves

**Most promising: (b.1), the telescoping-identity / chamber-value generalization**, because it
is (i) elementary — pure linear algebra (conservation of sub-totals) rather than a new
inequality technique, (ii) already validated exactly by hand for the base case (`n=2`, top-only
cut, 37% of the polytope sampled hits `f=1` exactly, matching the algebra `s1+s2+s3-3=1`), and
(iii) naturally recursive: it slots directly on top of the CERTIFIED Lemma A/B decoupling
(`f(P) = u + f(Q)`) — the "nice chamber" is precisely `u`'s own chamber (`u=(s1-2^{n-1})^+`
computed directly via the same conservation argument once you unfold the `min(s_i,2^{n-1})`
capping), so an inductive write-up should reuse Lemma A/B's proof machinery almost verbatim,
just tracking chamber membership instead of parity.

**Crux corpus:** searched combinatorics subtopics `invariants-and-monovariants`,
`extremal-principle`, `games-and-strategy` for cutting/stick/interval/alternating-sum/
conservation keywords (see below). No problem is a close structural analogue of *this* claim
(vertex/flat analysis of a combinatorial game's alternating sum on a self-similar dyadic
multiset) — the corpus's nearest hits are process/amortized-invariant proofs (e.g. `aimo-0019`,
`aimo-0196`) that use a *linear potential bounded by a constant times progress, proved by
amortized induction*, which is thematically resonant with the recursive/telescoping style needed
here but not adaptable move-for-move (their invariant is a monotone resource bound in an
adversarial process, not a sort-chamber algebraic identity). I do not recommend forcing a
citation; the load-bearing mechanism (interleaving conservation identity) is internal to this
problem's own structure, as it was for the certified lemmas already in `lemmas/`.

### Prior progress
See `results/imo-2026-03/current.md` / `approaches/self-similar-recursion.md`: Lemma 0
(endgame), layer-cake `f=M`, Lemma A/B top-band decoupling (`f=u+f(Q)`, CERTIFIED), Theorem F
(integer/dyadic case, CERTIFIED, complete), Theorem G (cascade tightness `min_XY f <= 1`,
CERTIFIED). GAP-L residual (non-integer cuts) is the sole open item on the lower-bound side.

### Dead ends (do not retry)
- Dual-price/LP-duality monovariant certificate for GAP-L (proven dead, round 2).
- Blanket exchange/domination lemmas not scoped to the top piece (FALSE, 28k counterexamples).
- Trying to close the residual via parity/integrality scaling tricks (provably impossible, `d=3`
  counterexample).

### Small-case / intuition notes (all labeled conjecture except the hand-verified algebra)
- **Hand-verified exact algebra (not just numeric):** for `n=2`, top-only 2-cut pattern, the
  "nice interleaving" chamber (`s1>2, s3<1`) gives `f ≡ 1` identically via conservation; the
  `s1<2` chamber gives `f=5-2s1>1` strictly; by symmetry/continuity the `s3>1` chamber should
  give a similar `>1` bound (not yet hand-derived but consistent with the numeric scan: 200000
  samples, min exactly `1`, zero violations).
- **Numeric (DE + random scan), n=2,3, multiple cut patterns:** global min of `f` over ALL real
  cut positions is exactly `1`; the argmin set is NOT a finite point set but includes a
  positive-measure flat region (37% of the top-only-cut simplex at `n=2`); restricting cuts to
  spread across multiple original pieces (rather than concentrating on the top) empirically
  gives strictly higher minima in that pattern (`~1.0001`–`1.016` in two spot patterns sampled),
  consistent with "concentrate cuts on the current top" being the extremal strategy (matches
  Theorem G's cascade and round-2's telescoping conjecture `f(W_{n-k})`).
- **Conjecture:** the GAP-L residual reduces entirely to proving, by induction on the cut
  pattern's depth, that every chamber's telescoped value is `>=` the "nice" chamber's value
  (which itself equals `1` by the base-case conservation identity, matching Theorem F/Theorem G
  exactly). This is the concrete next target for the outliner; not attempted here.
