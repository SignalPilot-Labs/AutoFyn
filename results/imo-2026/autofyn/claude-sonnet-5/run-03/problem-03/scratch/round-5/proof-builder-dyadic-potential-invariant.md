# proof-builder report — dyadic-potential-invariant, round 5

Task: prove the "Tie-or-zero LP-vertex Lemma" per the round-5 outline, using
the LP-vertex/compactness tool (`knowledge_base.md` line 47), and attempt
an existence-style closure of the balanced-region upper-bound gap.

## Result: Status stays `partial`, but a real positive tool is now proved

Full write-up in `results/imo-2026-03/approaches/dyadic-potential-invariant.md`.

**Proved in full (Sections 0–4 of the file):**
1. **Closure Lemma** — XY's inner minimization (`inf` over legal, positive-
   fragment responses) is a genuine attained minimum, and is witnessed by
   an honest response, handling the recurring "`≤n` cuts vs `=n` cuts /
   zero-length vs strictly-positive fragments" subtlety fully rigorously
   (memory rule #14's exact failure mode from round 3), by showing zero
   coordinates can always be discarded without changing `OddSum` and
   without leaving the legal-response space.
2. **Linearity on sort-order regions** — `OddSum` restricted to a fixed
   total-order region of the split-fragment polytope is a fixed 0/1-
   weighted linear functional; proved directly from the definition, with
   the tie-boundary consistency check tied explicitly to the already-
   certified Tie-neutrality Lemma.
3. **LP-vertex-attains-minimum fact** — proved *from scratch* (not cited as
   a black box) via a Krein–Milman-style argument: every nonempty compact
   convex set has an extreme point (induction on dimension via supporting
   hyperplanes), and the arg-min set of a linear functional over a compact
   polytope is itself such a set, so the minimum is attained at a vertex
   of the original polytope.
4. **Vertex Pinning Lemma** — the actual key new result: at a vertex of the
   relevant polytope, the number of active "pinning" conditions (a
   fragment `=0`, or two elements of the final multiset exactly tied) is
   at least the codimension `N-k = Σm_i` (total cuts used), proved via a
   linear-independence/null-space argument on the active-constraint
   gradients (piece-sum equalities have disjoint-support, hence
   independent, gradients; zero and tie inequality-gradients are standard
   basis differences).

**Found and proved FALSE (Section 5), a genuine correction to the round's
working conjecture:** the *literal, stronger* claim proposed by this
round's outline and math-explorer — "every individual optimal fragment is
0-or-tied" — is false in general. Exact, hand-verified counterexample:
`k=3`, `(p1,p2,p3)=(0.6,0.3,0.1)`, split `p1→(0.5,0.1)` (one cut). Resulting
multiset `{0.5,0.3,0.1,0.1}`, `OddSum=0.6=p1` exactly. This is a genuine
vertex (indeed the whole interval of splits from `a=0.1` to `a=0.3` is an
optimal face, since `OddSum` is constant `=p1` there whenever exactly one
other fixed element separates the two fragments in sort order) — at the
chosen vertex, the fragment `0.5` is neither `0` nor tied with anything;
only the fragment `0.1=p3` accounts for the codimension-1 pinning budget.
The *correct* general fact is the weaker counting form (item 4 above), not
the per-fragment form. This distinction is exactly the kind of thing a
numeric survey (which only samples specific optima) can miss, and is
recorded as a companion negative result alongside the positive lemma so no
other approach mis-cites the stronger false form.

**Attempted (Section 6), honestly scoped as incomplete:** using the Vertex
Pinning Lemma toward an existence-style closure of the balanced-region gap.
For a *fixed* LB partition, the lemma gives a genuine finite-search
reduction (finite allocations × finite sort orders × finite choice of which
`≥Σm_i` pinning conditions are active, each choice solvable as a linear
system). This does *not*, by itself, close the gap for LB's *outer*
maximization over the continuum of partitions — I checked explicitly
whether the counting fact alone gives a partition-independent bound and
found it does not (the *specific* pairing of which elements tie is
load-bearing, e.g. it determines whether the achieved value is `0.505` vs
`0.515` in round 4's own counterexample), which is exactly why
`universal-halving-adversary`'s explicit matching-rule construction and
`lp-duality-split-polytope`'s necessity/duality argument (both building in
parallel this round) are the right complementary next steps — this file
does not duplicate either.

## Promotable lemma

**Vertex Pinning Lemma for the split-multiset polytope**, with its
companion negative result (the false stronger per-fragment form, with
counterexample) — both fully proved, in the "Promotable lemmas" section of
`results/imo-2026-03/approaches/dyadic-potential-invariant.md`. Recommend
the proof-reviewer certify this to `results/imo-2026-03/lemmas/` (the
positive counting lemma and the negative companion result together, so
future approaches cannot cite the false stronger form).

## Files touched
- `results/imo-2026-03/approaches/dyadic-potential-invariant.md` — full
  rewrite this round (kept prior rounds' history under "Approaches tried").
- `/tmp/memory/proof-builder.md` — appended one new rule about testing
  degenerate constant-along-a-face instances before trusting a numeric
  "every optimal X has property P" survey.
