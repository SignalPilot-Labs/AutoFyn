## imo-2026-03 — Round 12 outline review

Both approaches keep their existing slugs (no new approach registration needed).
I independently re-verified the two flagged risk points with fresh exact-`Fraction`
scripts (not reusing any prior builder/explorer script) before approving anything.

---

### greedy-halving-adversary — CHANGES REQUESTED

**Target:** close sub-case (c) of the ℓ(F)=2 branch of restricted Claim (B),
i.e. inequality (‡): A({v2}∪G') ≤ (p1−v2) − f(n).

**Step 1 (reduce to P=∅) — sound, but fix an overclaim in the wording.**
I checked the arithmetic: ℓ(F)=2 with P nonempty actually forces c≥3 (two
residual fragments v1,v2 plus at least 2 more fragments forming one pair in
P ⇒ ≥4 fragments ⇒ ≥3 cuts), not merely c≥2 as the outline states — but
this only *strengthens* the outline's conclusion (budget ≤ n−3 ≤ n−2), so
the reduction step itself is not broken. However, the phrase "already
inside the **closed** (†)-regime" is a real overclaim: (†) (the v<p2-cut
budget-≤n−2 case Proposition 21 reduces to) is only *partially* closed —
Proposition 22 is conditional (unconditional only for n≤4), Proposition 25
closes one branch unconditionally, and the "v<s" case plus the general
"G′ cuts p2" complement are still open per the approach file's own §
"Open gaps". Calling the nonempty-P reduction "already closed" risks the
builder skipping open sub-branches. **Fix:** state it as "reduces to the
already-on-file, still-partially-open v<p2 machinery (Propositions
22/24/25 and their listed open branches) — no new leverage needed, but
none gained either."

**Step 2 (boundary/continuity via Lemma 14) — legitimate direction, but the
Lemma-14 reuse is not obviously valid and must be independently re-derived,
not just cited.** Lemma 14 (single-cut perturbation identity) computes
A(S)−A(S′) when one element M is *split* into two fragments (multiset size
increases by 1). Step 2 wants d/dt[A({p2−t}∪G')], i.e. how A changes as
one *existing* coordinate is continuously perturbed (multiset size
unchanged). These are different operations; Lemma 14's proof does not
manifestly hand over a formula for the latter (there is no "byproduct" I
could find in the write-up — this needs a fresh, short derivation from the
rank/indicator definition of A directly, likely trivial, but must be done,
not assumed). The outline already hedges this ("check this applies before
assuming it") — good — but I want it explicit in the build instructions:
**do not cite Lemma 14 as already covering this; re-derive the
continuous-perturbation formula from scratch (it's probably a two-line
argument via the rank/indicator definition, but write it).**

**The t=0 boundary claim needs one more caveat.** Sub-case (c) requires
v2<p2 strictly; the limit v2→p2⁻ is not itself a legal ℓ(F)=2
configuration (as v1≥p2, v2=p2 forces v1=v2=p2 by p1=2p2, contradicting
v1>v2 — this is exactly the vacuity the round-11 reviewer already flagged
for sub-case (a)). So "t=0 is exactly Proposition 22's statement" is true
only as a *continuity/limit* anchor, not as an actual instance of sub-case
(c); and Proposition 22 itself covers v≥p2 (a different regime index) —
the match at the boundary needs an explicit continuity argument (A is an
integral, so plausible, but state it) rather than an identification of
cases. Minor fix, but should be in the outline text so the builder doesn't
conflate "boundary value" with "included case."

**Step 3 (exchange-smoothing import) — properly hedged, but flag a strong
precedent against it before the builder spends a whole round here.** The
outline is right to demand the hypothesis-level check (v2 is not a ladder
value) rather than asserting the transfer. I want to make explicit for the
builder: round 11's `lp-duality-certificate` already found, independently,
that the ladder-specific evaluation tools this machinery needs
(Ratio-2 Spacing Lemma, Last-Element Bound) do **not** transfer to
non-ladder-structured points (R11.5, "confirmed non-transferable"). v2 here
is exactly such a non-ladder point. This is not a proof that step 3 must
fail, but it is a strong, on-file negative precedent for the exact same
transfer the outline proposes — recommend the builder try step 2 first and
only invest in step 3 if step 2 genuinely stalls, reporting precisely which
hypothesis breaks if it does (per the per-role NEVER-assume rule).

**Verdict: CHANGES REQUESTED** (no fatal flaw; fix the "(†) already closed"
overclaim in wording, re-derive rather than cite Lemma 14 for step 2, note
the t=0 boundary caveat, and carry the step-3 precedent warning into the
build instructions).

---

### lp-duality-certificate — CHANGES REQUESTED, with a hard redirect

**Steps 1–2 (Equal-Pieces Closure, Spare-Cut Bisection Corollary) — sound,
approve as scoped.** These are genuine one-line formalizations of already
-established facts (m equal pieces cancel via `pair-cancellation-identity`;
a_n>1/2 via the certified telescoping identity). I checked: applying the
Spare-Cut Bisection Corollary to the round-10 equal-pieces n=4
counterexample (Iterated Greedy-Peel ends at v_final=1/5 using 0 of 4
cuts) immediately gives Φ=1/2<16/31=a_4 — so this really does dissolve that
exact on-file counterexample for free, confirming the outline's claimed
narrowing (from "~48-62% random failures" to one precisely-scoped
"full-budget, zero-tie" residual) is legitimate, not hand-waved.

**Step 3/4 (gap-closing pigeonhole selection rule) — I ran the legality
check the dispatch asked for, and it fails: this entire family of
strategies is insufficient, not just the naive top-two greedy.** I
implemented an exhaustive brute-force search over *every* possible
pair-selection order within the "repeatedly cut the larger of a chosen
pair down to the smaller, cancel the resulting exact pair" move family
(the family both step 3's literal "close one gap per cut" reading and its
step-4 fallback live inside), and computed, for each random n=3 (m=4,
pairwise-distinct) marking, the *best* Φ achievable over **all** orderings
— not just the greedy top-two rule:

```
n=3, 200 random distinct 4-tuples (exact Fraction): best-of-all-orderings
still exceeds a_3*T in 119/200 (~60%) of trials.
Concrete witness: (8/5, 35/3, 12/5, 31/10); T=563/30;
best achievable via this whole move family: Phi=35/3 ≈ 11.667
vs target a_3*T = 2252/225 ≈ 10.009  (target exceeded by ~17%).
```

I also checked the specific literal reading "one cut per gap forces ALL
values to a common value" (cut every element down to the global minimum in
one pass, n cuts total for m=n+1 values) — this is *not* what actually
happens: it leaves n leftover fragments (the excess above the minimum)
which are generically all distinct and do not cancel, so it is not "full
pairing" at all. Direct check (n=4, 2000 random distinct trials): fails to
meet a_4*T in 1989/1997 (~99.6%) of trials — essentially never works as a
mechanism. And the "reorder the greedy" reading collapses exactly onto
`iterated-greedy-peel-identity` (B.3), the already-certified-but-refuted
construction from round 10 — a brute-force search over *all* its possible
orderings (not just top-two) still fails 60% of the time at n=3, as shown
above. **Both literal readings of step 3's mechanism are dead**, and this
is exhaustive (not a single bad witness) — the whole "force a tie via
pairwise matching" strategy class is provably too weak in the majority of
cases, confirmed independently of any specific selection heuristic.
Step 4's stated fallback ("some selection rule forces a tie... using ≤n
cuts") is the *same* move family with a relaxed stopping condition, so it
inherits the identical insufficiency — my brute force already searches over
"reach a tie eventually," not just "one cut per gap," so step 4 is refuted
by the same computation, not just step 3.

This matches (and should be read together with) the outline's own
"Watch out for" paragraph, which already anticipated this exact failure
mode ("near-ties... may still admit a 'nudge to exact tie' argument
different from what the pigeonhole framing assumes") — my check confirms
the worry was justified and the pigeonhole framing as scoped cannot be
salvaged by a smarter selection rule within the same move family.

**Instruction for the builder:** build steps 1–2 only (write them up as
clean standalone lemmas, genuine value — this alone resolves the on-file
counterexample and sharpens the open residual, matching the outline's own
framing of "genuine narrowing"). Do **not** spend build time on step 3/4's
gap-closing construction as scoped — it is refuted by exhaustive search,
not merely unproven. Redirect the residual ("full-budget, zero-tie"
markings) toward a genuinely different move family: either non-tie-based
splits (the existing Theorem A–E bisection routes, which do not aim at
exact matches at all), or continue R11.5's marking-agnostic Per-Piece
Vertex Decomposition Theorem evaluation (the "single cleanest remaining
item" per round 11's own Next note) — do not re-attempt any variant of
"iteratively equalize pairs" for this residual.

**Verdict: CHANGES REQUESTED** (steps 1–2 approved and worth building;
steps 3–4 as scoped are a confirmed dead end by exhaustive brute-force
check — this is not a fatal flaw in the approach as a whole, since steps
1–2 are real progress and the approach's substantial prior certified
content stands, but the round's *new* planned content must be redirected
before any further build time goes into it).

---

### Diversity / plateau note

The two built approaches attack genuinely disjoint fronts (restricted
Claim (B)'s ℓ(F)=2 mixed regime vs. the general upper bound's zero-tie
residual) and use different mechanisms — no shared-gap collapse this
round. `rank-tie-vertex-reduction`'s general c1≥2 lower-bound gap remains
parked (last touched round 8, negative result only); still an independent
front, not currently competing for build slots. No RETHINK of a whole
slug this round — both approaches keep real, live, certified content; only
one round's *proposed new increment* on the upper-bound side needed a
redirect.

### Ranking

Ranked via `update_ranking` (comparisons anchored across the whole
population, not just the two newcomers-of-the-round):
- `greedy-halving-adversary` > `lp-duality-certificate` (this round's new
  content: greedy-halving-adversary's plan is sound modulo fixable wording
  and hedged-but-unverified steps; lp-duality-certificate's core new
  mechanism (steps 3–4) is refuted by exhaustive brute-force check).
- `rank-tie-vertex-reduction` > `lp-duality-certificate` (established,
  no new flaw this round, vs. a newly-found structural insufficiency).
- `rank-pigeonhole-budget` > `greedy-halving-adversary` (already has a
  fully closed, verified milestone — Claim (A) in full — vs. ongoing
  partial progress).

Updated Elo: `rank-pigeonhole-budget` 1669.2 > `rank-tie-vertex-reduction`
1642.0 > `greedy-halving-adversary` 1620.4 > `lp-duality-certificate`
1589.1 > `smoothing-compactness-certificate` 1565.8 (unchanged, not
compared this round) > others unchanged.

build set: greedy-halving-adversary, lp-duality-certificate
