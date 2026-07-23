# Vertex Lemma — piecewise linearity of a single cut, and the joint-optimum corollary

**Certified by:** proof-reviewer, round 4, merging two independently-derived write-ups of the
same underlying fact: `dyadic-cascade-induction` §3 (round 2/3, the base single-cut
statement) and `elementary-exchange-smoothing` Step A + Corollary (round 2, the single-cut
proof plus the iterated/joint-optimum extension). Both builders proved this independently,
in different rounds, with slightly different framing — agreement between them is itself
cross-validation. This file supersedes both slugs' own copies; cite this file going forward,
not either slug.

**Depends on:** the definition `e(M) := Σ_i (-1)^{i+1} m_i` (equivalently, `L := Σ_{odd
ranks}`, `e = 2L - S`) for a sorted descending multiset `M`. General-purpose: no reference to
this problem's specific numbers, to `n=2`, or to any specific `m`.

## Statement

**Lemma (single-cut piecewise linearity).** Fix a finite multiset of "background" piece
values and consider replacing one background piece of length `ℓ` by two new pieces
`(t, ℓ-t)`, `t ∈ (0,ℓ)`, with every other current piece held fixed. Let `L(t)` (equivalently
`e(t)`, an affine reparametrization, `e = 2L-S`) denote the resulting value. Then:
(a) `L(t)` (and `e(t)`) is continuous and piecewise linear on `(0,ℓ)`, with breakpoints
exactly at the values of `t` where `t` or `ℓ-t` crosses another current piece's value, or
where `t = ℓ-t` (i.e. `t=ℓ/2`);
(b) consequently, the infimum of `L` (or `e`) over `t∈(0,ℓ)` is attained at a critical value
— either `t=ℓ/2` (self-bisection, a "D-type" point) or `t` (or `ℓ-t`) exactly equals some
other current piece's value (a "tie", an "M-type" point) — or in the degenerate limit
`t→0,ℓ` (an unused cut).

**Corollary (joint optimum).** For a player placing several cuts simultaneously (any finite
number, not just two), holding all cuts but one fixed, the Lemma applies to the remaining
free cut. Hence **at a joint optimum, every one of the player's cuts individually sits at a
tie (with a current background piece, or with another of the player's own new pieces) or a
self-bisection, or is degenerate** (an unused cut, in the limit).

## Proof

**Lemma.** As `t` varies over an interval not containing any breakpoint, the sorted rank of
every piece (including the two new pieces `t` and `ℓ-t`) among the whole multiset is
constant, because the only way two elements can swap relative order as `t` varies
continuously is for their values to cross, and the only elements whose values change with `t`
are the two new pieces themselves (values `t` and `ℓ-t`, both linear in `t` with slopes `+1`
and `-1` respectively). A crossing between these two new pieces happens only at `t=ℓ/2`; a
crossing between a new piece and a fixed background value `a_j` happens only where `t=a_j` or
`ℓ-t=a_j`. Away from all such points, every piece's rank (hence its sign in the alternating
sum defining `e`, or its odd/even-rank membership defining `L`) is locally constant, so on
each sub-interval, `L` (or `e`) is affine in `t` (a fixed linear combination of `t` and
`ℓ-t`, each with locally-constant sign). There are finitely many other piece-values, so
finitely many breakpoints, proving piecewise linearity with the stated breakpoints. A
continuous piecewise-linear function on a closed interval attains its extrema at an endpoint
or a breakpoint (each linear piece's extrema are at its own endpoints), giving (b). ∎

**Corollary.** Standard coordinate-wise fact for joint optimization: if `(t_1,…,t_k)` jointly
minimizes a function, then for each `i`, `t_i` minimizes the function restricted to varying
only the `i`-th coordinate, holding the rest fixed at their optimal values. Apply the Lemma to
each coordinate `t_i` in turn, with "every other current piece" now including both the
original background pieces and the other cuts' already-placed values `t_j` (`j≠i`) — the
Lemma's proof never assumed the "other pieces" were unmodified originals, only that they are
held fixed while `t_i` varies, which holds here. This proves every individual cut, at a joint
optimum, is itself a tie/bisection/degenerate point of the single-cut Lemma. ∎ (This includes,
as a special non-exceptional case, "richer" combinatorial patterns such as one piece being
split with two ties in succession, or a match-then-bisect-remainder pattern — these are simply
two ordinary single-cut vertex conditions applied to two different cuts, not a phenomenon
outside the Lemma's scope.)

**Caveat (honestly recorded, from both source files).** The Corollary shows every cut
*individually* sits at a vertex condition when every *other* cut is held fixed at its own
optimal value — it does **not** by itself enumerate which combination of tie/bisect choices
is the actual joint global minimizer among the (generally many) configurations satisfying this
necessary condition; that requires comparing the finitely many candidate values directly
(done case-by-case in `dyadic-cascade-induction`'s Case (i)/(ii) closures and
`elementary-exchange-smoothing`'s Step B enumeration for `n=2`). A full joint-vertex
enumeration for general `k` (number of pieces) and general cut budget is not carried out here
and remains part of the open casework in sibling approaches.

## Verification

The single-cut piecewise-linearity argument (part (a)/(b) of the Lemma) is elementary and was
checked by the proof-reviewer against both source write-ups (`dyadic-cascade-induction` §3,
`elementary-exchange-smoothing` Step A) for consistency — both give the identical breakpoint
characterization (tie / bisection / degenerate), proved independently by two different
builders in two different rounds, which is itself strong corroborating evidence. No numerical
counterexample search is applicable (this is a structural/qualitative statement about
piecewise linearity, not a numeric inequality); the proof is a direct, elementary
case-tracking argument with no gaps identified.

## Reusable by

Any approach reasoning about XY's (or any player's) optimal single or joint cut placement —
already used by `dyadic-cascade-induction` (§5.1's Branch B case split into bisect/match),
`potential-weighting-upper-bound` (the D/M operation reformulation's restriction to
bisect/match "vertex" move types), and `concavity-minimax-duality` (§8's Step 8.2, the
existence of a global minimizer and its vertex-type classification, used to prove partial
D/M-completeness for the lower-bound direction — see `lemmas/dm-completeness-partial.md`).
Cite this file, not `elementary-exchange-smoothing` (retired as an independent slug, round 4 —
its content is fully absorbed here) or `dyadic-cascade-induction`'s own §3 copy (kept in that
file for self-containedness but this is now the canonical citable source).
