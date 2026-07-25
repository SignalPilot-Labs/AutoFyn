# Outline-reviewer report — imo-2026-02, round 4

## Context read
`proof-outliner.md` (round 4), `current.md`, all three approach files
proposed for the build set (`coordinate-bash-resultant-boundary.md`,
`coordinate-bash-resultant.md`, `ptolemy-trig-identity.md`), and the three
math-explorer reports (`F2lens`, `acutelens`, `ptolemylens`). Independently
re-derived, from scratch, the two load-bearing numerical/symbolic claims
flagged for spot-check (see below) rather than trusting the reports as
written.

## Independent verification of this round's key claims

### 1. `F2 = 0 ⟺ β = ∠ACB` — CONFIRMED, exactly, symbolically

Re-solved the file's own `F2 = -2ab·u + a·cc·u² - a·cc + 2b²u + 2cc²u` for
`u` in a fresh `sympy` session and evaluated `tanβ = 2u/(1-u²)` at both
roots:
```
tan β |_{F2=0} = a·cc / (b² + cc² - a·b)
```
Independently computed `tan(∠ACB)` via the signed cross/dot formula on
`CA = -C`, `CB = B-C`:
```
tan(∠ACB) = cross(CA,CB)/dot(CA,CB) = a·cc / (b² + cc² - a·b)
```
Exact match, byte-for-byte with the explorer's report. Combined with
tan-injectivity on `(0,π)` (the identical argument already certified for
`F1 ⟺ β=∠B`), **`F2=0 ⟺ β=∠ACB` is a genuinely proved, general fact**, not
a numerical coincidence. This is solid ground for
`coordinate-bash-resultant-boundary` to build on this round.

### 2. Acute-angle-bound refutation — CONFIRMED, counterexample reproduced independently

Reconstructed the explorer's first counterexample from scratch (own
script, `a=0.9959, b=2.0302, cc=1.1413, t1=0.1522, t2=1.2001, β≈9.72°`),
building `K,L` directly from the rotation parametrization and computing all
four angles plus both containments with an independent signed-area test:

```
angle LBK  = 95.18°   (claimed ≈95.18°) — matches angle LNC = 95.18° (hyp2 holds)
angle LCK  = 4.23°    matches angle BMK = 4.22° (hyp3 holds, to rounding of the truncated inputs)
K inside BMC: True
L inside BNC: True
```

This reproduces the reported obtuse (95°) genuine solution independently,
with both hypothesis-angle pairs matching (confirming it isn't a
mismatched/spurious root) and both containments holding with real margin,
not a boundary artifact. **The acute-angle conjecture is soundly refuted**
— retiring it is the correct call, and the `coordinate-bash-resultant`
redirect (away from that dead sub-route, toward the isosceles lemma) is
justified.

### 3. Isosceles-case "free proof" — real progress, but NOT yet a certified lemma; flag the gap explicitly

The mirror-symmetry argument (§(b) of `ptolemylens`) is structurally sound
*conditional on* `ψ=φ` being forced when `B=C`, which is itself conditional
on the two decoupled equations (III)/(IV) having a **unique** root in the
valid bracket (so "both become the same equation" implies "both have the
same unique solution," not just "some solution of one equals some solution
of the other"). The explorer's own report flags this precisely and honestly
does *not* claim it as proved — only that it "looks easy" via monotonicity
of each side on the relevant sub-interval. This is the correct level of
honesty; the outliner's build task for `coordinate-bash-resultant` correctly
keeps this as an explicit required step ("needs an explicit
existence/uniqueness argument... should be confirmed, not assumed") rather
than waving it through. **This is not yet a hidden gap that slipped past
review — it is already surfaced — but the build set assignment must not
let the builder skip it and certify the lemma anyway.** Flagging this
explicitly so the routing below is conditioned on it.

One more precision issue worth flagging for the builder: the isosceles
argument as sketched needs `A,K,L` non-collinear (so circle(AKL) exists),
which the explorer notes follows from the same genericity/containment
assumption used elsewhere — fine, but this should be an explicit cited
step in the write-up, not "clearly" waved through (per CLAUDE.md's
no-hand-waving rule), since collinearity is exactly the kind of edge case
that bites in a symmetric configuration.

## Field ranking

Both the outliner's routing and its factual basis check out. Ranking
applied (`update_ranking`, three pairwise comparisons this round,
anchored on round-3 outcomes plus this round's independently re-verified
progress):

1. **`coordinate-bash-resultant-boundary`** (Elo 1544.98 → 1575.54) — the
   strongest live route. Its missing piece (`F2=∠ACB`) is now independently
   confirmed general and correct; its remaining task (range-connectedness
   via the monotone ray-sweep, `F3` deferred as a stretch goal) is a clean,
   well-posed synthetic target, not a re-run of a dead lever.
2. **`ptolemy-trig-identity`** (Elo 1501.75 → 1506.75) — independent,
   genuinely different-framing route with real new narrowing this round
   (the cot-identity reduction is sympy-verified and collapses a 4-variable
   comparison to a 2-variable one). Still has an unclosed inequality but is
   making steady, non-repetitive progress.
3. **`coordinate-bash-resultant`** (Elo 1570.68 → 1535.12) — its own
   branch-selection sub-route (acute-angle bound) is now conclusively
   refuted (confirmed above), so it drops relative to the other two on its
   original mechanism; redirected this round to the isosceles lemma, a
   valuable but different (population-wide-reusable, not gap-2-closing)
   contribution. Ranking reflects that its primary lever died, not that the
   redirected task lacks value.

No approach is cut outright: all three build-set members have live, honest
tasks (not "keep pushing a refuted idea"). `fixed-point-concyclic`,
`coordinate-bash`, `power-of-point-secants` correctly held (no new
information bears on them this round; `fixed-point-concyclic`'s `Q=A`
degeneracy will be superseded once the isosceles lemma is certified, at
which point it should be revisited). `spiral-similarity-bootstrap` remains
an unbuilt outline, not prioritized — two live, genuinely distinct framings
(algebraic IVT vs. trigonometric Ptolemy) already occupy the build set, so
CLAUDE.md's shared-gap-plateau trigger is not active.

No new approaches to register or copy this round (all three build-set
slugs already exist in the ranker).

## Instructions to carry into the build set

- `coordinate-bash-resultant-boundary`: build the monotone ray-sweep
  argument for range-connectedness exactly as scoped by the outliner; write
  up `F2=∠ACB` as `lemmas/branch-crossing-locus-equals-angle-C.md` (builder
  should re-derive it, not just cite the explorer's numbers, per population
  norms — confirmed independently here so this is a safe re-derivation, not
  a risk).
- `coordinate-bash-resultant`: write the isosceles-case lemma, but must
  include a genuine existence/uniqueness argument for the (III)/(IV) root
  under `B=C` (monotonicity of each side on the sub-interval) before
  certifying `ψ=φ` — do not certify `lemmas/isosceles-case-symmetry.md` with
  this step merely asserted. Also state the `A,K,L` non-collinearity input
  explicitly, citing where it comes from.
- `ptolemy-trig-identity`: pursue the `b,c`-monotonicity-of-ψ,φ argument via
  the cot-identity reduction; if unresolved, isolate precisely which
  monotonicity sub-claim resists proof (per the outliner's instruction) —
  do not present the ~90-configuration numeric confirmation as a
  substitute for a proof.

build set: coordinate-bash-resultant-boundary, coordinate-bash-resultant, ptolemy-trig-identity
