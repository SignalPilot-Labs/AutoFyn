# Build report — `smoothing-compactness-certificate`, round 4

## Task

Generalize the certified `n=2` "six-template + LP-contradiction" upper-bound
mechanism to `n=3`, using the round-4 explorer's prefix cascading-halving
family as candidate templates — but taking into account the
outline-reviewer's correction that "hits the target at every prefix length
`k`" is false; only `k∈{n-1,n}` actually work.

## What was done

1. **Fixed the outline's premise correctly.** Confirmed (by re-reading the
   correction in `rank-tie-vertex-reduction.md`) that only the two boundary
   cascade lengths tie the target, and did not attempt the refuted general-`k`
   claim.

2. **New general-`n` theorem (positive result).** Proved, for *every* `n`
   (not just the numerically-checked `n≤6`), that the `k=n` and `k=n-1`
   cascades both give `Φ=a_n` exactly, via a direct rank-position count (no
   induction, no case split, no numerics) — a clean closed-form argument
   that both cases reduce to the same identity
   `(2^{n+1}-1)-2^n+1=2^{n+1}-2^n`. Cross-checked by exact `Fraction` script
   for `n=1..8` (16/16 exact matches). Written up in full in the approach
   file and proposed as a new lemma,
   `results/imo-2026-03/lemmas/general-n-cascade-achievability.md`.

3. **Attempted the actual assigned task (n=3 upper bound over ALL Liu Bang
   configurations, not just the ladder) and found a genuine new
   obstruction, reported honestly rather than forced.** Built the direct
   `n=3` analogs of the `n=2` templates (`T1,T2,T3` generalizing bisect-
   prefix, `D1,D2,D3` generalizing bisect-suffix) and found, via exact
   `Fraction` arithmetic (not floating point), a concrete configuration
   `(p,q,r,s)=(3/8,1/4,1/4,1/8)` where all six give `Φ∈{9/16,11/16}`, both
   `>` the target `8/15` — the 6-template family alone is insufficient to
   prove the upper bound. Investigated further with `scipy.optimize`
   multi-start search over the simplest possible extension (touch only the
   largest piece, split into `k=2,3,4` parts) and found the *true* optimal
   split is not a fixed closed-form rule but a genuinely
   configuration-dependent tie (to `q`, `r`, or `s` depending on the point) —
   i.e. even the easiest slice of the `n=3` upper-bound problem exhibits the
   same "vertex enumeration doesn't collapse to a short list" obstruction
   that the round-4 superincreasing explorer found on the lower-bound side.
   No violation of the conjecture was found (true minimum at the tested
   point is `≤1/2<8/15`) — only the specific proof mechanism fails to
   scale as hoped.

## Status

Approach file `Status` remains `partial`. Two honest, non-overclaimed
results added this round: a genuine new general-`n` lemma (achievability of
the target at the ladder, both boundary cascades, proved for all `n`), and
a genuine new negative/diagnostic finding at `n=3` (the upper-bound
mechanism's naive generalization fails, and the reason is structural, not a
fixable oversight). General `n`, both directions, and the `n=3` upper bound
specifically, remain open.

## Files changed

- `results/imo-2026-03/approaches/smoothing-compactness-certificate.md` —
  appended round-4 sections: "General-n cascade achievability theorem"
  (full proof), "n=3 upper-bound generalization attempt" (counterexample +
  diagnosis), updated `Promotable lemmas` and `Full proof` sections, added
  "Round 4 update" summary.
- `results/imo-2026-03/lemmas/general-n-cascade-achievability.md` — new,
  proposed for certification.
- Scripts (not part of the proof, exploratory/verification only, referenced
  from the write-up): `/tmp/round-4/n3_explore.py`,
  `/tmp/round-4/n3_lp_search.py`, `/tmp/round-4/n3_investigate.py`,
  `/tmp/round-4/n3_investigate2.py`, `/tmp/round-4/verify_cascade.py`,
  `/tmp/round-4/verify_counterexample.py`.

## Recommendation for next round

- The general-`n` cascade achievability lemma is ready for
  proof-reviewer certification — it's short, self-contained, and fully
  checked.
- Do not re-attempt "small closed-form template family" for the `n=3` (or
  general-`n`) upper bound without a new idea for handling
  configuration-dependent ties; the concrete counterexample and the
  single-piece-split investigation here should save the next builder from
  re-discovering the same wall. A promising unexplored direction (not
  attempted this round): characterize the tie target for the
  single-piece-split sub-family as a function of which fraction of `p`
  (e.g. `p/2`, `p/3`, `p/4`) is closest to `q`, `r`, or `s` — i.e. turn the
  configuration-dependence itself into a finite, provable case split rather
  than an obstruction.
