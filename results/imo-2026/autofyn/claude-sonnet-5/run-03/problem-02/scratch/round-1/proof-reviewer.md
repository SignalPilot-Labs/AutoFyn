# Round 1 proof-review — imo-2026-02 (IMO 2026 P2)

Build set reviewed: `fixed-point-concyclic.md`, `coordinate-bash.md`,
`power-of-point-secants.md` (all three self-reported Status `partial`).
`spiral-similarity-bootstrap.md` exists in the directory but was not built
this round (self-reported `unsolved`, outline only) — noted for context, not
adjudicated as a build.

Problem: prove OM=ON where O = circumcenter(AKL), M,N midpoints of AB,AC,
under the stated hypotheses on K,L. `proof_only`, `answer_type: none` — no
numeric answer to verify.

## Method
For each file I re-derived the load-bearing identity from scratch
independently (not trusting the write-up), using `python3`/`sympy` for
algebra and a fresh numerical instance, then checked every named lemma's
proof for gaps, checked the claimed containments/degenerate cases, and
checked the Status against what is actually proved.

## 1. fixed-point-concyclic.md — verdict: CHANGES REQUESTED, true Status: partial

**What I verified independently.**
- Lemma 1 (Q = t(C−B), t = (C−B)·(C+B)/(2|C−B|²), A at origin): recomputed
  both via this closed form and via a direct "reflect A in the perpendicular
  bisector of MN" construction on a fresh instance — they agree exactly
  (`Q via formula [0.27839416 2.69941606]` = `Q via reflection
  [0.27839416 2.69941606]`). Correct.
- Lemma 3 (A,M,N,Q concyclic) and the reduction Lemma 5 (concyclic(A,K,L,Q)
  ⟹ OM=ON): the reflection argument ("center of ω on perp-bisector of a
  chord, reflection fixes ω and swaps chord endpoints") is standard and
  correctly applied; re-derived it myself and it holds. On the builder's own
  numerical instance (A=(0.3,2.7), B=(−1.5,0), C=(2.2,0.1), K,L given to 4
  decimals) I independently computed: A,M,N,Q concyclic to 4 decimal places
  (limited by input precision, not the argument), and A,K,L,Q concyclic to
  the same precision, consistent with OM≈ON to the same precision. No
  arithmetic or logical error found in Lemmas 1–5.
- The stated gap (Step 3: prove A,K,L,Q concyclic from the three angle
  hypotheses via a directed-angle chase) is real, precisely stated, and
  honestly not closed — the file explicitly separates "what is available"
  from "what is missing" and does not fudge a "clearly / by symmetry" step
  over it. This is the correct behavior per CLAUDE.md's no-hand-waving rule.

**Load-bearing step re-derived.** The reduction lemma (OM=ON ⟺ O on
perp-bisector of AQ = perp-bisector of MN) is exactly two facts: (i) O
equidistant from A,Q forces O on perp-bisector(AQ); (ii) perp-bisector(AQ) =
perp-bisector(MN) because Q is by definition the reflection of A across the
latter. Both are elementary and I confirmed them independently; no gap.

**Gaps found beyond what's flagged.**
- Lemma 2's uniqueness claim ("Q is the unique point with AQ∥BC, QB=QC")
  implicitly assumes AQ is a well-defined nonzero direction, which fails
  exactly when AB=AC (then Q=A). The file *does* flag the isosceles case as
  an unhandled degenerate case in its Remark — good, this is disclosed, not
  hidden — but it should be tracked as a second (smaller) open item, not
  folded silently into "the" gap. I have reflected this in current.md and in
  the certified lemma file's caveat.
- Citation of "directed-angle chasing and its concyclicity converse" to
  knowledge_base.md is reasonable (falls under the KB's general "angle
  chasing / power of a point" toolkit entry) even though the KB doesn't use
  the words "directed angle" verbatim — not a fatal citation gap.

**Verdict.** Real, correct, gap-free progress on a full sub-reduction; the
central difficulty of the problem (the concyclicity) is untouched. Matches
self-reported Status `partial`. CHANGES REQUESTED: close Step 3 (the
directed-angle chase to A,K,L,Q concyclic), and separately address the
AB=AC degenerate case.

## 2. coordinate-bash.md — verdict: CHANGES REQUESTED, true Status: partial

**What I verified independently.**
- The vector reduction OM=ON ⟺ O·(C−B) = (|C|²−|B|²)/4 (A at origin):
  re-derived from scratch by polarization identity — matches exactly.
- The σ-symmetry lemma (swap B↔C, K↔L, M↔N maps the hypothesis list to
  itself, swapping the two "cross" angle hypotheses and fixing the first):
  I re-checked every one of the seven clauses (4 containments + 3 angle
  equalities) by hand, substituting σ into each. All seven map correctly
  onto another clause of the same list (self-image for hypothesis 1, swap
  for hypotheses 2/3, and paired swaps for the four containments). This is a
  genuine, correctly proved, non-trivial structural fact — no gap found.
- Steps 1–2 (circumcenter of A,K,L via Cramer's rule): routine linear
  algebra, correct.
- Section 4 (rotation parametrization of K,L from hypothesis 1): the sign
  convention (which rotation direction places K on the triangle-interior
  side) is argued informally but correctly (single side-of-line-AB fact),
  and cross-checked against a numerical solve of the full hypothesis system
  — the parametrization reproduces K, L to the solver's precision. Adequate
  justification, not hand-waving over a real ambiguity.

**Gap.** Section 5's polynomial elimination (showing the target identity is
implied by the two remaining hypothesis-derived polynomial equations) is
explicitly not completed — the file states the Gröbner basis computation did
not finish, rather than claiming success. This is the same central identity
as fixed-point-concyclic's gap, reached by an independent (coordinate) route,
as the file itself acknowledges.

**Verdict.** Genuine new lemma (σ-symmetry) plus a correct but unfinished
computational route to the same central identity. Matches self-reported
Status `partial`. CHANGES REQUESTED: complete the elimination (or find a
smarter algebraic manipulation that avoids brute Gröbner basis).

## 3. power-of-point-secants.md — verdict: CHANGES REQUESTED, true Status: partial

**What I verified independently.**
- The power-of-a-point derivation (Steps 1–2, secants AB, AC of ω through A,
  arc-length parametrization) is internally consistent: I re-derived
  pow(M,ω) = (c²/2)(1/2−t), pow(B,ω) = c²(1−t), and the elimination of t
  giving pow(B,ω) − pow(C,ω) = (AB²−AC²)/2 — matches. (Note: the file's prose
  aside about "the direction vectors ... of squared length c² and b²" is
  worded confusingly against the unit-vector parametrization actually used
  in the formula, but the computation itself, using the factor "·1", is
  correct — a wording slip, not a mathematical error.)
- The claim that this reformulation is *literally* the same identity as
  O·(C−B) = (|C|²−|B|²)/4: I independently expanded pow(B,ω)−pow(C,ω) via
  pow(X,ω)=|X−O|²−R² and confirmed algebraically that it reduces to exactly
  this equation. Confirmed correct — not a new independent gap, exactly as
  the file (honestly) claims.
- The file explicitly reports failed searches for an alternative secant
  construction (through K/L, or a spiral similarity) that would reach a
  distinct target — reported as negative evidence, not hidden or spun as
  success.

**Verdict.** Correct derivation, correctly and honestly identified as
converging to the same wall as the other two approaches rather than an
independent line of attack. This is valuable negative information for
population diversity (per CLAUDE.md's anti-single-gap-trap guidance) and is
reported with appropriate humility. Matches self-reported Status `partial`.
CHANGES REQUESTED: either find a genuinely different secant/point
construction (as the file itself suggests as the next thing to try), or fold
into the shared central-gap effort.

## Cross-cutting observation
All three built approaches (plus the shared vector-reduction lemma) converge
on one identity: `O·(C−B) = (|C|²−|B|²)/4` (A at origin), equivalently
`concyclic(A,K,L,Q)` for Q = reflection of A in perp-bisector(MN),
equivalently `pow(B,ω) − pow(C,ω) = (AB²−AC²)/2`. This is now a triply
cross-validated reduction (independently re-derived by me in all three
forms) — reliable as the true target for next round. Per CLAUDE.md's
shared-gap-plateau guidance, since three of four live approaches have
independently landed on the same wall, next round should prioritize a
genuinely different framing (the unbuilt spiral-similarity-bootstrap, or a
new one) rather than a fourth variation on directed-angle-chase /
coordinate-bash / power-of-a-point.

## current.md
Updated at `/home/agentuser/repo/results/imo-2026-02/current.md`: Status
`partial`, Approaches tried (all four, with accurate per-approach summaries
and the true state of each gap), Current best (the cross-validated shared
identity, in all three equivalent forms, with a description of what's needed
next). No Full proof section (correctly, since Status is not `solved`).

## Lemmas certified (written to results/imo-2026-02/lemmas/)
- `vector-reduction-OM-ON.md` — the shared OM=ON ⟺ O·(C−B)=(|C|²−|B|²)/4
  identity. Certified, gap-free.
- `amnq-concyclic-and-reduction.md` — fixed-point-concyclic's Lemma 3 (A,M,N,Q
  concyclic) + Lemma 5 (concyclic(A,K,L,Q) ⟹ OM=ON). Certified, with an
  explicit caveat that the isosceles case AB=AC (where Q=A) is not covered by
  this argument and remains open.
- `sigma-symmetry.md` — coordinate-bash's B↔C,K↔L,M↔N symmetry of the full
  hypothesis list. Certified, gap-free, independently re-checked clause by
  clause.

Not certified: fixed-point-concyclic's Lemma 2 ("Q is the unique point with
AQ∥BC, QB=QC") as a standalone unconditional statement — its uniqueness proof
implicitly needs AQ to be a well-defined direction, which fails in the
isosceles case; it should be restated with an explicit "AB≠AC" hypothesis
before being certified as a shared lemma. Not certified: the power-of-a-point
reformulation as a *separate* lemma beyond vector-reduction-OM-ON, since it
was shown (by the builder and re-verified by me) to be literally the same
identity in different notation — certifying it separately would be
redundant/misleading about independence.

## Overall verdict summary
- fixed-point-concyclic: CHANGES REQUESTED (Status: partial)
- coordinate-bash: CHANGES REQUESTED (Status: partial)
- power-of-point-secants: CHANGES REQUESTED (Status: partial)

No approach is fatally broken (no RETHINK); no approach is complete (no
APPROVE). All self-reported Statuses were accurate — no overclaiming found.
