## imo-2026-02 — outline review, round 7

### Independent verification performed
I rebuilt, from scratch (own sympy session, not the outliner's or explorer's
code), the load-bearing new algebraic claim behind
`coordinate-bash-resultant-boundary`'s planned step 2 (sturmlens's
resultant-ratio cancellation):

- Reconstructed `F1 = 2au-2bu+cc u²-cc` and `F2 = -2ab u+a cc u²-a cc+2b²u+2cc²u`
  (already-certified, taken from the approach file's own §4/§11).
- Reconstructed `D_K`, `D_N` (numerators, §13) and `L_1`, `\tilde N_2` (§11)
  exactly as displayed in `coordinate-bash-resultant-boundary.md`.
- Took `G_2b` exactly as displayed in `math-explorer-sturmlens.md` (first
  time this polynomial has been written out fully); confirmed its leading
  coefficient matches the file's independently-reported `B_2`.
- Computed `sympy.resultant(G2b, D_K_num, s2)`, `sympy.resultant(G2b, D_N_num, s2)`,
  `sympy.resultant(G2b, L1, s2)`, `sympy.resultant(G2b, tildeN2, s2)` and
  factored each. Results, exactly matching sturmlens's report:
  - `Res(G2b,D_K) = (u²+1)⁴·F2·Y`, `Y = 2a(u²-1)²-b(u²+1)²` (confirmed `Y`
    expands to exactly the second factor found).
  - `Res(G2b,D_N) = -4u(b²+cc²)²(u²+1)²·Y`.
  - Ratio `Res(G2b,D_K)/Res(G2b,D_N) = -(u²+1)²F2/(4u(b²+cc²)²)` — confirmed
    exactly, `Y` cancels. Since `u>0` and `F2<0` on the valid range
    (already certified, Lemma 11.6), this ratio is strictly positive, so
    `D_K(r1)D_K(r2)` and `D_N(r1)D_N(r2)` always share sign. **This new
    lemma is genuinely correct, not a numerics artifact.**
  - `Res(G2b,L1) = -4u(u²+1)⁴F1F2` — confirmed exactly, matching both
    sturmlens's report and the approach file's own §11 aside.
  - `Res(G2b,\tilde N2) = -8u(u²+1)²·F2·Z` — confirmed exactly (Z the
    reported degree-3-in-u polynomial), matching sturmlens's claim.

This is a solid, independently-reproduced result: the entire G2b
3-way-exclusion question really does reduce to the signs of exactly three
explicit polynomials `Y, B2, Z` (plus already-known `F1,F2<0`), and one of
the four candidate resultant pairs (`D_K` vs `D_N`) is now provably
`Y`-independent. Good, real progress to hand to the builder — approve
importing it.

I did not have time to independently re-derive `G_2b` itself from the raw
vector/dot-product definitions (sturmlens did, but I trusted their derived
polynomial and only checked internal consistency via the leading-coefficient
match against the file's independently-reported `B_2` — this matched
exactly, a good sanity check but not a full from-scratch geometric rebuild).
Flag this for the builder: re-derive `G_2b` from the raw vector definitions
as the first step (cheap, and the population's established practice), not
just trust the displayed polynomial.

I spot-checked the `paritylens`/`orthogonallens` reports for internal
consistency (the elementary "opposite-sign-in-one-column forces odd total"
counting argument in paritylens's step, and orthogonallens's Finding 1
sharper conjecture) — both are logically sound as stated and honestly
labeled as unproven/numeric-only where they are. No red flags found; I did
not re-run their 3000/20000/40000-sample sweeps myself (time-budget
tradeoff), but the case-count arithmetic underlying paritylens's
sufficiency claim is elementary and checks out by hand (product<0 ⟹ exactly
one factor >0; product>0 ⟹ 0 or 2 factors >0; odd+even=odd).

### Per-approach verdicts

**`coordinate-bash-resultant-boundary` (advance) — APPROVE.**
Technique (resultant-ratio cancellation, continuing the certified §12/§13
machinery) is sound and now independently verified for the one concrete new
lemma it plans to import (step 2). The skeleton's step 5 "cheap-kill" check
(test whether `(Y,B2,Z)=(+,+,+)` is algebraically forbidden) is a legitimate
low-cost probe before the full 7-case sweep. Step 6's up-to-7-way case split
is honestly scoped as heavy, not claimed as a one-lemma closer — no
overclaiming in the outline. Watch-out about the refuted fixed-threshold-
ordering approach is correctly flagged (sturmlens's 17-distinct-orderings
finding is real, confirmed by reading the report; not independently
re-run, but the finding is a straightforward sampling result, low risk of
error). No fatal flaw. Approve as written.

**`ptolemy-trig-identity` (advance) — APPROVE, with one required
sharpening.** The skeleton's step 3 ("logical-sufficiency" case-count
argument) is elementary and I verified it by hand — sound. Step 5's
single-radical-clearing plan (`a²≠b²Δ2`) is a well-defined, concrete next
computation, correctly flagged by paritylens as "not yet computed" — an
honest open item, not a hidden gap. One thing to flag for the builder: the
outline's step 4 needs BOTH non-vanishing of `Ξ(V1)·Ξ(V2)` on all of `D`
AND a base-point sign — the outline states this correctly (step 4(a),(b))
but should make explicit that "non-vanishing everywhere" is itself the hard
part (radical clearing gives an inequality, `a²≠b²Δ2`, which still needs a
sign-definiteness argument, not just "≠0" — a strict inequality of one sign
throughout `D`, not just nonzero). Not a fatal flaw, just tighten the
target statement when building.

**`ptolemy-trig-identity-parity-decomposition` (copy) — APPROVE as a
genuine second mechanism, not a same-framing duplicate.** orthogonallens's
Finding 1 gives a materially different, sharper target (exactly cell
`(U1,V1)` exceeds, via two independent "linear-form-at-both-roots"
sub-lemmas) that reuses the g2b-true-supplementary-parity resultant
TEMPLATE but requires proving DIFFERENT resultants (`Res_V(q2,L_{U2})`,
`Res_U(q1,L_{V2})`) than the sibling's `Ξ(V1)·Ξ(V2)` route — this is a real
branch, not a rename. Correctly registered via `copy_approach` (inherits
sibling's Elo/counts, diverges on real outcomes going forward). One
concrete thing the outline is right to flag as load-bearing and NOT yet
closed: Lemma A/B need the sign PINNED (not just same-sign), which is a
strictly bigger ask than the already-certified template's "same sign"
conclusion — correctly identified as the open gap, not glossed over.
Approve.

**`fixed-point-concyclic` (revise) — APPROVE, this is the plateau-breaking
approach the population has needed.** This route is genuinely orthogonal
(no root-counting, no polynomial sign case-split) to the other four, and
the population's own memory rules have been flagging a 3-round shared-gap
convergence in shape — reviving this dormant route with the untried "explicit
rational-function-of-H1,H2,H3" lever satisfies CLAUDE.md's plateau-breaking
requirement without re-litigating the already-exhaustive top-level-target
search (round 3). The outline is honest that this may produce a negative
result (no clean closed form exists) — that would still be valuable,
precisely-diagnosed information, consistent with this approach's history.
The skeleton's step 3 gives a concrete elimination procedure (solve for χ
in terms of H1,H2,H3,B,C by eliminating K,L using their own defining
equations) that is a genuinely different operation from the round-5-retired
"adjoin ideal generators" lever — I checked the outline's own distinction
(§ "Watch out for") and it correctly explains why this isn't the same
retired technique (substituting concrete real values vs. adjoining abstract
polynomial generators). No fatal flaw; legitimate exploratory revival.

**`coordinate-bash-resultant-boundary-pointwise` (advance) — APPROVE.**
The plan (test transfer of this round's ratio-cancellation technique to the
sibling's quartic/four-joint-condition setting) is a reasonable, low-risk
next step building on real machinery, honestly scoped as "test transfer,
report negative result precisely if it fails" rather than asserting success
in advance. No fatal flaw.

### Diversity / shared-gap-plateau check
Per the standing memory rule (three routes converged in *shape* — each a
"sign/parity pattern over polynomial roots" claim — for round 6): this
round's field genuinely responds to that flag. `fixed-point-concyclic`'s
revival is the one approach in the build set with a mechanism NOT of that
shape (an explicit algebraic-identity construction, zero root-counting
content) — correctly satisfies CLAUDE.md's requirement to bring a
genuinely different framing when a plateau persists. The other four remain
in the "root-sign-pattern" shape, but they are demonstrably still making
real, verifiable progress round over round (this round: two new
independently-confirmed resultant identities on the coordinate side, one
sharper reformulation on the Ptolemy side) — not stalled restatement, so
continuing to fund them alongside the new orthogonal approach is justified,
not a rubber-stamp of a stuck plateau.

### Registration / ranking actions taken
- `copy_approach(imo-2026-02, source=ptolemy-trig-identity,
  new=ptolemy-trig-identity-parity-decomposition)` — new slug copied,
  inherits sibling's Elo/counts as required.
- No other new slugs to register (all other build-set approaches already
  in the population).
- `update_ranking` run with 6 comparisons anchoring the new copy against
  established siblings and re-ordering the field by last-round outcome
  (advanced > partial, dormant `fixed-point-concyclic` ranked below the
  three actively-progressing coordinate/Ptolemy approaches but the field
  gap is not large, since its revival this round is exactly the diversity
  move the population needs). Resulting order (best-first, post-update):
  `coordinate-bash-resultant-boundary` (1637.9) > `ptolemy-trig-identity`
  (1577.0) > `coordinate-bash-resultant-boundary-pointwise` (1574.9) >
  `ptolemy-trig-identity-parity-decomposition` (1560.3) >
  `fixed-point-concyclic` (1473.5).

### Verdict summary
All five approaches in the outliner's proposed field: **APPROVE**. No
RETHINK, no CHANGES REQUESTED beyond the minor sharpening noted for
`ptolemy-trig-identity` (not fatal, just a clarity note for the builder).
This is a strong round: two of the field's key claimed algebraic identities
were independently reproduced from scratch with exact match, one genuinely
orthogonal approach was revived to address the standing shared-gap-plateau
flag, and one legitimate two-mechanism branch was registered.

build set: coordinate-bash-resultant-boundary, ptolemy-trig-identity, ptolemy-trig-identity-parity-decomposition, fixed-point-concyclic, coordinate-bash-resultant-boundary-pointwise
