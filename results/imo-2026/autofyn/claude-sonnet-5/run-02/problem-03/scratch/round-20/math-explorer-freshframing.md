## imo-2026-03 (lens: front 2, general upper bound, case (b2): T/D_n < p2 < a_n*T/2)

### Context verified
Read `results/imo-2026-03/current.md`, `approaches/lp-duality-certificate.md` (rounds 14-19
sections), and the round-19 crux-gap note in `run_state.md`. Confirmed: 6 mechanism families
are on record as dead for case (b2) — (1) peel/bisect/recurse-plus-full-IH (exact zero-slack
thresholds proved to coincide with already-closed regions, `peel-and-bisect-ih-dead-ends.md`),
(2) weighted-combination (`convex-combination-futility-theorem` — a fully general, non-numeric
proof that ANY weighting of a finite family of explicit primal strategies certifies no more than
their plain pointwise min), (3) naive boundary-continuity, (4) Danskin/concavity (g(t)=Φ_min as
a function of Liu Bang's own tail marking is provably non-concave — exact V-shaped interior
local min at p3=p1-p2, reproduced by two structurally different methods), (5) surrogate-
adversary/majorization (`surrogate-adversary-dead-end.md` — the argmax-tail ratio drifts
1.4-2.0 across case (b2)'s box, not a low-dimensional object), (6) constraint-side LP duality
(`Duality-Direction Impossibility Theorem` — weak duality structurally only certifies the wrong
inequality direction). No live mechanism remains for this front on file.

### Distinct openings (genuinely new top-level framings, not variants of the 6 dead families)

1. **Probabilistic method / randomized-strategy + derandomization.** Instead of exhibiting one
   deterministic explicit Xiang-Yu strategy (dead families 1, 3) or combining several explicit
   strategies by a weight (dead family 2), define a single RANDOMIZED cutting rule for Xiang Yu
   — e.g. sample the cut composition (how many of the n cuts land on p1 vs. the tail, and their
   positions) from a distribution parametrized by p2/(a_nT/2) or by p1/p2, calibrated so that
   `E[Φ(response)] <= a_n T` can be verified as a LINEAR (expectation) computation over the
   randomized construction, using linearity of expectation over the final multiset's pieces
   directly (no concavity of the min, no combination of already-fixed values — expectation is
   taken BEFORE minimizing, at the level of a single stochastic process, so `E[Φ]` is just a sum
   of `Pr[piece has odd rank]·length`, computable piece-by-piece). Then invoke the probabilistic
   method: since `E[Φ] <= a_n T`, some realization of the randomness gives an explicit
   (deterministic, still-legal) response with `Φ <= a_n T`, i.e. `Φ_min <= a_n T`. This is
   structurally different from all 6 dead families: it needs no concavity of `Φ_min` in Liu
   Bang's marking (dead family 4), no combining of several already-evaluated explicit values
   (dead family 2 — expectation over a joint distribution of RESPONSES is not the same object as
   weighting several fixed numeric bounds), and no LP dual certificate (dead family 6). The
   concrete design work (choosing the right distribution over cut compositions so `E[Φ]` comes
   out `<= a_nT` specifically in the T/D_n<p2<a_nT/2 band) is open and non-trivial, but the
   MECHANISM itself is untried on file.

2. **Amortized potential / monovariant over Xiang Yu's own cut SEQUENCE (not recursion on n).**
   Every dead-and-live mechanism to date reduces case (b2) via recursion in the level `n`
   (peel one piece, recurse at `n-1`/`n-2`; bisect-top; etc.) — a "shrink the instance" axis.
   A genuinely different axis: fix `n`, and analyze Xiang Yu's construction as a k-step ONLINE
   process (`k=0,...,n`, his cuts placed one at a time), defining a potential `Ψ_k` (e.g.
   `Ψ_k = a_n T - Φ(current partial-cut multiset viewed with remaining budget n-k)`) and proving
   a per-step amortized inequality `Ψ_k` is non-increasing (or bounded above by 0 once `k` cuts
   are spent optimally) via an elementary per-move argument — the classic
   invariant/monovariant technique (`knowledge_base.md` "General Proof Methods" /
   "Invariants & monovariants"; also the dominant flavor of the `games-and-strategy` crux
   subtopic, e.g. `aimo-0019`'s amortized-potential covering-game bound, `aimo-0262`'s
   self-reproducing-invariant bucket game). This differs from peel/bisect/recurse (dead family 1)
   in kind, not just in name: dead family 1's induction hypothesis is the FULL theorem one level
   of `n` down; this framing's induction hypothesis (if any) is only about the potential's own
   step behavior at fixed `n`, so it does not inherit the "zero-slack ceiling coincides with an
   already-closed region" obstruction that killed peel/bisect. Genuinely worth a from-scratch
   attempt, though the correct potential function for case (b2) specifically is not yet
   identified — this is a real design gap, not a proof.

3. **Direct explicit-strategy construction indexed by the CONTINUOUS ratio p2/(a_nT/2) or
   p1/p2, not by a discrete recursive step count.** All explicit constructions on file (Bisect-
   Top-k, Cross-Piece Sign-Assignment, Alternating Gap-Cross) are parametrized by an integer
   step-count `k` and built via pair-cancellation/peeling. A genuinely different construction:
   define Xiang Yu's cut positions as an EXPLICIT smooth (not integer-indexed) function of the
   real ratio `r = p2/(a_nT/2) \in (0,1)` within case (b2)'s band — e.g. splitting p1 into
   fragments whose *sizes* (not counts) are chosen via a closed-form function of `r` designed so
   the final Φ value is manifestly `<= a_n T` by direct algebraic simplification (not induction,
   not case-split by which of several fixed templates wins). This is close in spirit to idea 1
   but deterministic; flagged separately because it risks silently collapsing into the already-
   dead "weighted-combination" or "peel/bisect" families if the construction ends up being
   expressible as a convex combination of on-file strategies or a disguised recursive peel —
   any candidate here MUST be checked against `convex-combination-futility-theorem` before being
   trusted as new.

### Candidate technique(s) to name for the outliner
- **Probabilistic method** (`knowledge_base.md` "General Proof Methods" doesn't name it
  explicitly but the combinatorics subtopic list includes `probabilistic-method`, and the crux
  corpus has live cases of it) — the strongest fresh candidate (opening 1 above).
- **Invariants & monovariants / amortized potential** (`knowledge_base.md` "General Proof
  Methods" and "Combinatorics" both name this explicitly) — opening 2 above.
- Flag but do not over-invest in opening 3 without a concrete pre-check against the
  Convex-Combination Futility Theorem.

### Cheap-kill candidates
- Before designing a full randomized strategy (opening 1), do a CHEAP numeric check: pick a
  simple parametrized random rule (e.g. uniform over {bisect-top-k for k=0..n}, or a Beta-
  distributed split point) at the two on-file near-tight case-(b2) witnesses (n=3 flat-face,
  n=4 pinned-tie — both already closed by Cross-Piece Sign-Assignment, so use them only as a
  sanity check that E[Φ] computed for the trial rule is <= a_nT there) and at a few fresh random
  points drawn uniformly from case (b2)'s box — this is a 10-minute sympy/numpy check that can
  kill or promote the whole idea before committing a full-round build.
- For opening 2, cheap kill: compute `Ψ_k` numerically along the SPECIFIC cut sequences used by
  bisect-top-k and Cross-Piece Sign-Assignment at a case-(b2) witness and check whether *any*
  natural potential candidate (e.g. `A(current multiset)` itself, or `a_nT - Φ_partial`) is
  monotone step-by-step — if none is even monotone along KNOWN good strategies, the framing is
  probably not viable as stated and should be revised before a full build.

### Knowledge-base entries to use
- `knowledge_base.md` "General Proof Methods" — Invariants/monovariants, Induction (as contrast:
  explicitly NOT recursion-on-n here), Constructive vs. existence framing.
- `knowledge_base.md` "Combinatorics" — Invariants & monovariants entry; Pigeonhole/extremal
  principle entry (for opening 3's fallback if a construction needs a threshold argument).
- No entry in `knowledge_base.md` names probabilistic method explicitly with detail — the
  corpus subtopic tag `probabilistic-method` (combinatorics domain) is the resource, not the KB.

### Analogous past problems (cruxes)
- Searched `combinatorics/games-and-strategy` (39 cruxes) and keyword-matched
  minimax/polytope/vertex/duality/concavity/potential/majorization/compactness across the full
  2434-entry corpus. **No genuinely analogous problem found.** The games-and-strategy subtopic
  is dominated by discrete grid/pairing/coloring games (`aimo-0019` dyadic covering,
  `aimo-0115` domino pairing, `aimo-0461` knight-placement, `aimo-0663` no-consecutive-picks) —
  all finite discrete-state games with pairing/parity invariants, not continuous-interval
  Stackelberg minimax value problems like imo-2026-03. `aimo-0114`'s crux ("hand the adversary
  one specific extremal configuration and read a parity obstruction off it, to force a LOWER
  bound on a min-max quantity") is superficially close in shape (min-max value determination)
  but (a) it needs a LOWER bound on the min-max value via one adversary configuration, whereas
  case (b2) needs an UPPER bound on Φ_min holding for EVERY marking in a continuous band — the
  wrong direction and the wrong quantifier structure — and (b) it's a discrete parity argument
  on a fixed domino tiling, no continuous algebra. `aimo-0560` was already checked (round 19) and
  confirmed dead (its surrogate move is inseparable from multi-round replay). Consistent with
  round 1's original finding ("no strong direct analog") — this remains true after a fresh,
  wider keyword search. Do not force a match; treat this as a from-scratch construction problem.

### Prior progress
See run_state.md / current.md for the full state; front 2's frontier is exactly case (b2)
(`T/D_n < p2 < a_n*T/2`), unclosed, with the 6 dead mechanisms above. Front 1 (Claim B,
greedy-halving-adversary) is a separate, further-progressed front not in this lens's scope.

### Dead ends (do not retry)
The 6 confirmed-dead mechanism families listed above under Context — do not propose another
variant of peel/bisect/recurse, weighted-combination, boundary-continuity, Danskin/concavity,
surrogate-adversary/majorization, or constraint-side LP duality for case (b2).

### Small-case / intuition notes (conjectural, not proof)
- Numeric probing (round 18/19 builders, reused here for context, not re-run this round): the
  worst-tail argmax ratio for Xiang Yu's tail response drifts 1.4-2.0 across case (b2)'s box —
  i.e. there is genuinely no low-dimensional closed-form "worst configuration" to target with a
  single deterministic template, which is exactly why deterministic-template mechanisms (1,3,5)
  keep failing. This is suggestive (conjecture, not proof) that a mechanism which does NOT
  require pinning down one worst-case witness — i.e. probabilistic method (opening 1), whose
  argument works via expectation regardless of which realization is later shown to be "the"
  worst — may be structurally better suited to this front than any more deterministic
  candidate. I did not run a fresh numeric E[Φ] computation this round (time-boxed to scouting
  per the dispatch instructions); this is the natural next step for whichever approach the
  outliner opens on opening 1.
