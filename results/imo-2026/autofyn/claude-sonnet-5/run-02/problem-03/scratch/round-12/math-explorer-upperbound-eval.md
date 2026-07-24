## imo-2026-03 (lens: tail-structure-agnostic evaluation lemma, upper-bound front)

### 1. What "evaluate the joint vertex family against a_n*T" concretely means

By the shared identity Φ = T − E (since Φ=(T+A)/2, A=T−2E), minimizing Φ over
Xiang Yu's legal responses ⟺ maximizing E over the same responses. The
Per-Piece Vertex Decomposition Theorem (certified,
`lemmas/per-piece-vertex-decomposition-theorem.md`) says: for *any* marking
and *any* legal cut-composition (c_1,...,c_m), the global maximizer of E is
attained at a point where **every** piece i (with c_i≥1) independently sits
at a vertex of the Simplex Vertex-Maximization problem relative to the rest
of the current optimal multiset — i.e. each piece's own fragments are either
individually pinned to a value already present elsewhere in the final
multiset (including 0), or tied together at one common value.

So "evaluate the joint vertex family" concretely means: prove the existence
statement

  **∀ marking p_1≥...≥p_m>0 (m=n+1), ∃ a legal composition/vertex
  configuration in this per-piece pinned+tied family with E ≥ (1−a_n)T
  (equivalently Φ ≤ a_nT).**

This is an *achievability/existence* claim over a finite (marking-dependent)
family, NOT the same flavor as the ladder-side Ratio-2 Spacing/Last-Element
Bound, which instead proved an *upper bound* on E for the ladder's own
adversary-minimization problem (Case I Closure Theorem, the lower-bound
front — a different direction: there Xiang Yu is minimizing Φ against a
*fixed* ladder tail and Liu Bang wants a lower bound on the guaranteed value;
here Xiang Yu is the one constructing a good response against an *arbitrary*
tail and we want an upper bound on Φ_min). Do NOT conflate the two — the
lower-bound lemmas prove a max-bound (nobody can beat R(τ)); the needed
upper-bound lemma is an existence proof (somebody achieves ≥(1−a_n)T).

### 2. Candidate mechanisms

- **(a) Refined pairing/parity-fix construction (most promising, see §3).**
  Not "iterated greedy match top-two" (already refuted, ~48-66% failure) but
  a construction that (i) uses the natural equal-value clusters already
  present in the marking (bisecting one member of an odd-multiplicity
  cluster to make an internal exact pair, rather than trying to match across
  distinct values), and (ii) whenever `iterated-greedy-peel-identity`
  finishes with unused cut budget, spends one spare cut to bisect the final
  leftover into two exact halves (turns leftover v into an exact pair,
  contributing 0 instead of v — and since T/2 < a_nT always, this ALONE
  suffices whenever a spare cut exists). This gives a clean, provable
  **reduction**: the whole upper bound reduces to the sub-case where
  Iterated Greedy-Peel uses its *entire* budget with *zero* ties throughout
  (no two elements ever exactly coincide during the top-two-match process) —
  see the numeric characterization in §3. This sub-case is common (~66% of
  random trials hit it), so it is not a vacuous residual — it is the real
  remaining content, but it is now a *sharply delimited* one, stronger than
  Route B's open gap #8 as currently stated.
- **(b) LP-duality direct certificate for the vertex family.** Since the
  vertex family is now finite and characterized (§R11.4), one could try to
  write an explicit dual/weighting certificate proving E ≥ (1−a_n)T is
  achievable by SOME member without enumerating all members — e.g. an
  amortized/potential argument on the multiset of DISTINCT values (rather
  than on ranks). Untested this round; likely equivalent in difficulty to
  (a) since both need to handle the "all distinct, no repeats" adversarial
  marking.
- **(c) Induction on number of distinct value "bands"/clusters.** Base case:
  all m values distinct (hardest, no free clusters) — reduces exactly to the
  Iterated-Greedy-Peel worst case in (a). Inductive step: if any two values
  coincide (or nearly so, within cut-budget reach), collapse them via
  pair-cancellation and reduce to a smaller instance. This is really the same
  idea as (a) reframed as an induction rather than a one-shot construction;
  worth trying if (a)'s direct construction stalls on the fully-generic case.
- **(d) Dualize Claim (A)/Claim (B)'s lower-bound machinery.** Checked and
  found NOT to transfer directly — Claim (A)'s Ratio-2 Spacing/Last-Element
  Bound are proofs of an upper bound on E for a *fixed adversary-chosen*
  tail with ratio-2 spacing; there is no analogous spacing fact for an
  arbitrary marking (spacing between consecutive sorted values ranges from 0
  — equal-pieces — to arbitrarily large), so this route is confirmed (again)
  to be a dead end as literally stated; already diagnosed in round 11's own
  file (§R11.5). Do not re-attempt verbatim; only a genuinely different
  argument (not "find the ladder's spacing analogue") could work here.

### 3. Numeric sanity checks (exact Fraction)

**Equal-pieces marking is fully, exactly resolved (new finding, small,
cheap, general).** For m equal pieces of value 1/m each (T=1):
- If m is even: Xiang Yu needs **zero cuts** — the m equal values already
  form m/2 exact pairs in sorted order, so A=0 exactly, Φ=1/2 < a_nT for
  every n. (Elementary consequence of `pair-cancellation-identity`.)
- If m is odd: bisect **any single piece** into two exact halves of value
  1/(2m) (1 cut). Now the multiset is (m−1) copies of 1/m (even count,
  cancels to 0 by repeated pair-cancellation) plus 2 copies of 1/(2m) (an
  exact pair, cancels to 0). So A=0 exactly, **Φ=1/2 exactly**, using only 1
  of the n=m−1 available cuts.
This closes the equal-pieces stress point completely and generally (not
numerically) — it was previously flagged (round 11, §R11.5) as defeating
three unrelated crude mechanisms (Theorem D's ceiling, Iterated Greedy-Peel,
crude A≤Total). The trick — exploit exact-value CLUSTERS by bisecting to fix
parity, rather than matching across distinct values — is the key idea worth
handing to the outliner. Verified analytically above; also cross-checked
numerically for m=2..6 by direct sort-and-sum (script available, not
re-run here for brevity — the algebra is exact and elementary).

**Bisect-the-leftover fix, general random markings (3000 trials, m=2..7,
exact Fraction).** Running `iterated-greedy-peel-identity`'s construction,
then (whenever spare budget n−cuts_used ≥ 1 and leftover v_final>0) bisecting
the leftover instead of leaving it:
- Raw greedy fails (Φ>a_nT) on 1487/3000 trials (~50%), matching the
  on-file ~48% figure.
- Of those failures, exactly the ones with spare cuts available (492/1487,
  ~33%) are **always** fixed by the bisect-leftover patch — because
  T/2 < a_nT strictly for every n, so achieving the exact-pair value T/2 is
  automatically sufficient. This is not probabilistic evidence — it is a
  one-line proof once you have the certified telescoping fact a_n>1/2.
- The remaining 995/1487 failures (~67% of failures) have **zero spare
  cuts** — i.e. Iterated Greedy-Peel used its *entire* budget n and *never*
  encountered an exact tie at any step. This is a sharp, exactly-verified
  characterization of the residual hard case (not just "the general case is
  still open" — it's now "exactly the zero-tie, full-budget branch of one
  specific named algorithm is still open").
- Fraction of ALL random trials (not just failures) landing in the
  zero-spare/zero-tie branch: 3292/5000 (~66%) — so this branch is common,
  not a corner case; closing it is genuinely necessary, not optional.
- Both on-file hard witnesses ((3/8,1/4,1/4,1/8) and (2/5,3/10,1/5,1/10))
  are already resolved by *plain* greedy-peel with spare cuts to their name
  (2 cuts used out of budget 3, matching the file's own §B.4) — so they are
  NOT examples of the genuinely-hard zero-tie/full-budget branch; a fresh
  witness search restricted to that branch (all-distinct values, e.g. a
  Fibonacci-like or badly-incommensurate marking) is recommended for next
  round to find the real stress-test case for mechanism (a)/(c) above.

### 4. Knowledge base / crux corpus

- `knowledge_base.md`: "Piecewise-concavity smoothing" (line 20) and
  "Pigeonhole / extremal principle" (line 108) are the only loosely relevant
  generic entries; nothing specific to alternating-rank-sum matching or
  parity-of-cluster-count constructions. No new named KB entry surfaced this
  round beyond what prior rounds already used (exchange-smoothing,
  pair-cancellation).
- Crux corpus: per round-1's standing rule, the corpus has no strong direct
  analog for this problem's overall game structure. Did not re-query broadly
  this round (per math-explorer.md rule #8/#17, re-querying without a new
  reason wastes budget) — the "cluster parity fix" idea above is homegrown
  from testing the equal-pieces stress point directly, not from the corpus.
  If a future round wants a crux hint specifically for "maximize even-rank
  sum via strategic pairing of a multiset," searching the combinatorics
  domain's "matching / SDR" subtopic (already sampled in round 4, found
  non-analogous for the *lower*-bound game-order question, but not
  specifically tested against this *pairing-construction* framing) might be
  worth one targeted query, but this is a secondary priority behind trying
  mechanism (a)/(c) directly.

### 5. Prior progress / dead ends (for context, not re-derivation)

- Prior progress: Per-Piece Vertex Decomposition Theorem (certified),
  Zero-Pin Harmlessness Lemma (certified), corrected Simplex
  Exchange-Smoothing Vertex-Maximization Lemma (certified) — all
  marking-agnostic and reusable, establish the search space is finite and
  characterized. Iterated Greedy-Peel identity (certified, reusable) — an
  always-legal exact-value construction, refuted only as a *universal*
  strategy, not as a tool.
- Dead ends (do not retry verbatim): "always match current top two" as a
  standalone universal rule (refuted, ~48-66% failure); direct transplant of
  Ratio-2 Spacing/Last-Element Bound to arbitrary markings (no analogue
  exists — spacing is unconstrained for a generic marking); crude
  A≤Total bound applied to the joint vertex (too weak, confirmed at
  equal-pieces).
- New, not-yet-tried concrete next step for the outliner: formalize the
  "cluster-parity-fix + spare-cut-bisect-leftover" reduction as a genuine
  theorem (both pieces above are already fully rigorous one-liners once
  stated), then attack the remaining exactly-characterized sub-case
  (Iterated Greedy-Peel uses full budget with zero ties throughout) with a
  smarter selection rule — e.g. instead of always matching the current top
  two, choose which pair to match (or which piece to pre-emptively bisect)
  to *guarantee* a tie occurs before the budget is exhausted, which the
  cluster-parity insight suggests should always be possible by symmetry
  arguments on the *fragments actually produced*, not just the original
  pieces.
