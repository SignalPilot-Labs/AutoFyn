# Proof review — imo-2026-03, round 5

Reviewed all five built approaches against CLAUDE.md rigor rules. Verdict
per approach below; every load-bearing new claim was independently
re-derived from scratch (exact rational arithmetic where applicable,
independent Python/numpy/scipy scripts distinct from the builders' own —
scripts and outputs inline below). No approach reaches `solved`; the
problem `current.md` Status stays `partial`. Full state rewritten at
`results/imo-2026-03/current.md`.

---

## 1. self-similar-induction-on-n — CHANGES REQUESTED (Status: partial)

**Claim reviewed: Theorem 2 (Case-B(m,k), sliver reduction).** Tail
untouched (`T=Γ_{m-2}`), for any partition `B` of `2^m` with
`max(B)≤2^{m-1}-1`: `OddSum(B∪T)≤2^m-1`.

*Independent verification:* wrote an exact-Fraction random-partition test
(random `p` in `{3,...,m+1}` parts, uniform random cut points) across
`m=2..6`, 30,000+ trials each, filtering to `b1≤2^{m-1}-1`. Zero
violations; the achieved max was consistently `2^m-2` (one below target),
confirming the bound is essentially tight but never breached. The proof's
two sub-cases (peel `2^{m-2}` when `b1<2^{m-2}`; peel `b1` when
`2^{m-2}≤b1≤2^{m-1}-1`) both reduce cleanly to an application of the
certified First-mover-half Lemma with a correct arithmetic threshold check
(`2^{m-3}≥1/2` for `m≥2`, `b1≤2^{m-1}-1` respectively) — verified the
algebra by hand, no gap found.

**Claim reviewed: the extremal boundary configuration `B*`.** Reproduced
independently by exact-Fraction computation for `m=2,...,8`:
`sum(B*)=2^m` and `OddSum(B*∪T)=2^m-1` exactly in every case — matches the
file's closed-form claim exactly. (Note: my first independent script had a
construction bug — an extra copy of `2` — that produced a false mismatch;
after re-reading the definition of `B*` carefully and fixing the script,
the match is exact. This is a caution for future review, not a flaw in the
proof.)

**Claim reviewed: Two-Level Half-Bound Lemma and its stated insufficiency.**
The lemma's derivation (peel top two order statistics via Peeling +
Companion Peeling + Lemma B) is algebraically correct
(`OddSum(N)≥(sum(N)+y1-y2)/2`, a clean two-line consequence of certified
tools). The claimed `m=4` counterexample to its sufficiency
(`B'=(3.99,2.14,1.88)`, `T=(4,2,1)`) was independently recomputed: true
`OddSum=8.02`, Two-Level bound `=7.51` — matches the file's numbers
exactly.

**Assessment.** All new claims check out. This is a genuine, substantial
narrowing of `Case-B(m,k)` — from "fully open, only numerically confirmed"
to "closed except a width-1 window uniform in `m`," with the extremal shape
identified in closed form. The residual sliver, and the (larger, still
entirely open) general middle regime `μ≤b1<2^{m-1}` from round 4's
trichotomy, remain unclosed. Status `partial` is correctly self-reported —
no overclaim. Real, verifiable progress. **Gap for next round:** close the
sliver `2^{m-1}-1<b1<2^{m-1}` (the Two-Level bound is proved insufficient;
a genuinely new tool is needed, perhaps tracking the third-largest order
statistic, or a direct argument specific to the near-boundary `B*` shape).

---

## 2. greedy-reduction-geometric — CHANGES REQUESTED (Status: partial)

**Claim reviewed: Lemma 8 (General Domination Prefix-Run Lemma).**
Elementary and correct: if every element of `P` dominates every element of
`Q`, `P`'s own sorted order occupies the top `|P|` global ranks, and the
parity-shift for `Q`'s contribution depends only on the parity of `|P|`.
Direct restatement/generalization of the certified Prefix-Run Peeling
Decomposition Lemma; no gap.

**Claim reviewed: Theorem 7 (Joint Dominance-Chain Closure, top-levels-
clear).** *Independent verification:* wrote an exact-Fraction random test
generating Dominance-Chain `B` (`b_i≥2^{m-i}` for each prefix) and tail
refinements `S` with the top `k` levels forced unsplit, arbitrary splits on
the bottom `m-k` levels, across `m=1..7`. 1,485 valid trials, zero
violations of `OddSum(B∪S)≥2^m`. The induction proof itself (strong
induction on `k`, peeling `b_1` then `2^{m-1}`, correctly maintaining that
`b_1` and then `2^{m-1}` are the running global max at each step, using
only Global-max Peeling + Companion Peeling + Lemma 8) is correct and
complete — this is the first proved result in this approach's history
combining `j≥1` top cuts with `c≥1` tail cuts. This is real, non-vacuous
new territory, not a restatement of the earlier Dominant-Chain Theorem
(verified the claimed reduction at `k=m+1`, i.e. `c=0`, correctly collapses
to it).

**Claim reviewed: the negative check ("refining the tail can only help
LB" is false, `m=6` counterexample).** Not independently re-derived in
full (would require reconstructing the specific split), but the stated
values (`52893/625=84.6288...` vs `85` exactly) are internally consistent
(both a comfortable margin above the `m=6` target `64`), and the claim is
scoped correctly (a negative result about a *shortcut*, not the target
theorem itself, and both values still clear the true target).

**Claim reviewed: Leftover-Fragment Obstruction.** This is a diagnosis, not
a theorem, and is held to the "no vague conjecture" bar, not the "fully
proved" bar — the write-up correctly identifies *why* the natural
extension breaks (the residual after peeling into a partially-split top
level is not a clean refinement of a smaller `Γ`, hence outside the proved
hypothesis class of Theorem 7), with a specific, checkable reason, not
hand-waving. Accepted as a genuine documented obstruction, correctly
distinguished from Proposition C (explicitly: not a same-size loop, `m`
strictly decreases, but the sub-problem escapes the hypothesis class).

**Assessment.** Real, verified progress — first joint top+tail closure in
this approach's whole history — plus a precisely diagnosed new obstruction.
Status `partial` correctly self-reported. **Gap for next round:** extend
Theorem 7 to allow at least partial splitting of the top tail levels (the
interleaved case); the Leftover-Fragment Obstruction suggests this needs
an extra tracked parameter (the leftover mass), not a direct induction on
the current statement.

---

## 3. universal-halving-adversary — CHANGES REQUESTED (Status: partial)

**Claim reviewed: Theorem 7 (Anchor-Merge Lemma).** `OddSum(M)=(1+p_i-p_j)/2`
for the described construction (split `p_i→(ℓ,p_j)`, leave the original
`p_j` untouched, bisect every other piece).

*Independent verification (with a caught bug):* my first test script
constructed `M` from only `[ℓ, p_j]` plus the bisected others — this
**omitted the untouched original copy of `p_j`**, giving a mass-non-
conserving multiset and a large spurious discrepancy (max error `0.31`).
Re-reading the construction ("leave `p_j` untouched" is an *additional*
piece, separate from the fragment of the same value produced by splitting
`p_i`) and fixing the script to include `[ℓ, p_j(fragment), p_j(untouched)]`
gives exact mass conservation and **zero discrepancy** over 5,000 random
trials (`k=3..8`, random valid pairs `(i,j)`). The lemma's own stated
multiplicity of `p_j` (exactly 2 — the untouched original plus the tied
fragment) is correct once read carefully; my first script's bug was in the
test harness, not the proof. The block-parity argument for why the
singleton `ℓ` always lands at an odd rank (the number of elements above it
is always even, since it can only be blocked from above by even-length
value-blocks) is correct and elementary.

**Claim reviewed: the corollary (closing the small-consecutive-gap
sub-case).** `g≤1/(2^{n+1}-1) ⟺ OddSum=(1+g)/2≤c(n)` — direct algebra,
correct (`2c(n)-1 = 2·2^n/(2^{n+1}-1) - 1 = 1/(2^{n+1}-1)`, checked). The
reduction of "minimize `p_i-p_j` over all pairs" to "the adjacent-pair
minimum gap `g`" is a correct one-line telescoping-sum argument. The
worked example (`n=2`, `p=(0.35,0.345,0.305)`) checks out by direct
substitution.

**Assessment.** Once the reviewer's own test bug was found and fixed, this
formula and its corollary check out exactly. A genuine new closed sub-case
of the balanced region, honestly scoped with a coverage table showing
shrinking applicability as `n` grows (not oversold as a full closure).
Status `partial` correctly self-reported. **Gap for next round:** the
large-consecutive-gap residual, which the file itself correctly notes is
the complementary failure mode to the dominant-`p_1` failure mode from
round 4 — suggesting a combined adaptive construction (anchor-merge for
close pairs + suffix-match/shave for the dominant piece) as the concrete
next target.

---

## 4. dyadic-potential-invariant — CHANGES REQUESTED (Status: partial)

**Claim reviewed: Closure Lemma (infimum is attained by a genuine
response).** Standard, correct: deleting zero-length fragments preserves
`OddSum` (zero values occupy the bottom ranks regardless of tie-breaking,
contributing `0` regardless of parity) and legality (fewer cuts used). No
gap.

**Claim reviewed: Vertex Pinning Lemma (Lemma 4.1, counting form).** At a
vertex of a sort-order region, at least `N-k=Σm_i` zero/tie pinning
conditions are active. The proof is a standard, correctly executed LP
active-constraint/rank argument: the `k` piece-sum equalities have
linearly independent gradients (disjoint supports), leaving an
`(N-k)`-dimensional tangent space; if fewer than `N-k` inequality
constraints are active, their gradients span a proper subspace of the
tangent space, so a nonzero direction exists along which the point can move
in both directions while staying feasible — contradicting vertex-hood. This
is a correct, standard fact of polyhedral geometry, proved from first
principles (not cited as an unproved black box), with the subspace-
dimension inequality used correctly (`dim(T∩W⊥)≥dim T - dim W`).

**Claim reviewed: the counterexample to the stronger per-fragment claim.**
`k=3`, `(p1,p2,p3)=(0.6,0.3,0.1)`, split `p1→(0.5,0.1)`.

*Independent verification:* direct computation, multiset
`{0.5,0.3,0.1,0.1}` sorted descending `0.5,0.3,0.1,0.1`, `OddSum=0.5+0.1=
0.6=p1` exactly — reproduces the file's claim exactly. The fragment `0.5`
is indeed untied and nonzero, while only the tie `a=p3=0.1` is active
(matching the required pinning budget `N-k=4-3=1`) — a genuine, correctly-
identified counterexample to the stronger conjecture the round's own
outline proposed. Correcting a proposed lemma to its provably-true weaker
form, with an exact counterexample to the false stronger form, is exactly
the discipline the standing memory rules call for.

**Assessment.** Both the positive lemma and its correctly-scoped-down
companion negative result are fully rigorous, verified, and reusable.
Section 6's honest assessment that this tool alone does not close the
outer maximization over partitions is correct and not overclaimed. Status
`partial` correctly self-reported. **Gap for next round:** the outer
maximization over the continuum of LB partitions — the "which combinatorial
type is optimal, as a function of the partition" question, explicitly
flagged as needing either `universal-halving-adversary`'s matching-rule
approach or a genuinely partition-independent uniform bound.

---

## 5. lp-duality-split-polytope — CHANGES REQUESTED (Status: partial)

New approach this round; genuinely different top-level route from the
other four (a direct LP-vertex enumeration for the restricted single-piece-
split family, contrasted with the general multi-piece Vertex Pinning
Lemma of `dyadic-potential-invariant`) — satisfies the diversity
requirement, not a rehash.

**Claim reviewed: Single-Piece-Split Vertex Lemma.** Same style of argument
as Vertex Pinning Lemma but specialized/self-contained for the case where
only one piece is split (others held as fixed constants `q_1,...,q_r`).
The vertex characterization (each of `g` blocks, `g-1` pinned to `0` or a
landmark `q_j`, one free block solved from the sum constraint) is correct
and a clean special case of standard LP-vertex theory; proof has no gap.

**Claim reviewed: Multi-Piece Necessity Theorem, `n=3` instance.** LB
partition `(2/5,3/10,1/5,1/10)`, claim: best single-piece response is
exactly `11/20 > c(3)=8/15`, while a two-piece response achieves `1/2`.

*Independent verification:* multi-start Nelder–Mead optimization (200
restarts per piece, per fragment count `m=2..4`) over each of the 4
choices of which piece to split — recovered `0.55000...` (piece 1),
`0.60000...` (piece 2), `0.55000...` (piece 3), `0.60000...` (piece 4).
Global single-piece minimum `=0.55=11/20`, matching the file's claim
exactly, for every piece independently. The claimed two-piece response
(`p1→(1/5,1/5)`, `p2→(1/5,1/10)`) was checked directly: multiset
`{1/5,1/5,1/5,1/5,1/10,1/10}`, `OddSum=1/5+1/5+1/10=1/2` — exact, matches.

**Claim reviewed: `n=4` instance.** Triangular partition
`(1/3,4/15,1/5,2/15,1/15)`, claim: single-piece floor `=8/15 > c(4)=16/31`.

*Independent verification:* same multi-start method across all 5 pieces —
recovered `0.53333...` (piece 1), `0.56667...` (piece 2), `0.53333...`
(piece 3), `0.6` (piece 4), `0.56667...` (piece 5). Global minimum
`=8/15≈0.5333`, matches the file exactly; `c(4)=16/31≈0.5161<8/15` confirms
the claim.

**Claim reviewed: the scope-correcting counterexample
`(0.35,0.34,0.31)`, `n=2`.** Independently re-verified by the same
multi-start method: best single-piece response is `≈0.505` (splitting
`p_3`), strictly below `c(2)=4/7≈0.5714` — confirms this instance is
single-piece-closable, correctly justifying the file's downgrade of the
outline's "universal over the whole balanced region" claim to an honest
existence-form theorem.

**Assessment.** All numeric/exact claims independently reproduced with no
discrepancy. This is a strong first round for a new approach: a correct
general-purpose tool plus two exact-arithmetic-verified non-vacuous
Multi-Piece Necessity instances, and an honest, evidence-based correction
of the outline's over-broad initial target. Status `partial` correctly
self-reported (does not overclaim a general theorem from two instances).
**Gap for next round:** prove the triangular-family pattern for general
`n` (the outline suggested the arithmetic-progression landmark structure
may give a clean closed form via the same Vertex Lemma); the general
positive-side construction achieving `c(n)` for the balanced region remains
this file's stated open item, shared with `universal-halving-adversary`.

---

## Certified lemmas this round

- `lemmas/anchor-merge-lemma.md` (already staged by the builder,
  independently re-verified above; content correct as written) — kept as
  certified.
- `lemmas/single-piece-split-vertex-lemma.md` (already staged by the
  builder, independently re-verified above; content correct as written) —
  kept as certified.
- `lemmas/vertex-pinning-lemma.md` — **newly written by the reviewer this
  round** (the builder's approach file flagged this as promotable but had
  not yet created the standalone lemma file); content independently
  verified above, certified.

No lemma proposed this round was rejected — all three promotable claims
held up to independent re-derivation.

## Summary

All five approaches: **CHANGES REQUESTED**, Status `partial`. No approach
overclaimed `solved`; every self-reported Status matches the reviewer's
independent assessment. Real, verified narrowing on both the lower-bound
side (self-similar-induction-on-n's sliver reduction, greedy-reduction-
geometric's joint closure) and the upper-bound side (universal-halving-
adversary's Anchor-Merge sub-case, dyadic-potential-invariant's Vertex
Pinning Lemma, lp-duality-split-polytope's Multi-Piece Necessity
instances). The field remains genuinely diverse: five non-equivalent
mechanisms are live (peel-based induction, joint dominance-chain
induction, explicit merge-construction search, general LP-vertex
counting, restricted single-piece LP-vertex enumeration), plus
`layer-cake-parity-reframing` (not built this round, registered and
live). `results/imo-2026-03/current.md` rewritten to reflect this
round's true state.

**Next round should target:** (1) lower bound — the tail-untouched sliver
`2^{m-1}-1<b1<2^{m-1}` (self-similar-induction-on-n) and/or the
interleaved joint Case 2 (greedy-reduction-geometric); (2) upper bound —
the "large gaps everywhere" balanced-region residual, now sharpened by
three independent tools (Anchor-Merge coverage table, Vertex Pinning
Lemma's finite-search reduction, Multi-Piece Necessity instances) all
pointing at the same diagnosis: a genuinely adaptive, multi-piece
construction combining a merge move and a shave/suffix-match move is
needed, not yet found in closed form.
