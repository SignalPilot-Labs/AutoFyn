## imo-2026-03

dyadic-cascade-induction: revise
Target: `c(n) = 2^n/(2^{n+1}-1)` — the whole theorem (both directions, all `n`). This round's
revision targets specifically the still-open lower-bound multi-cut gap (§5.2) at every `m`.
Technique: strong induction on `m` via the peel-`a_1` self-similar recursion (unchanged spine),
but §5.2's sub-mechanism is replaced: drop the physical-cut-*location* Branch A/B split in
favor of a pure D/M-operation-sequence reformulation (import certified Lemma D/M), closed via
a broadened induction class ("induction loading", crux `aimo-0292`) with a minimal-
counterexample fallback (crux `aimo-0287`/`aimo-0438`) for the one hard residual sub-claim.
Skeleton (new §5.2', full text now in the approach file):
  1. Restate the target purely in D/M-sequence language on `D_m` — by Lemma D/M (already
     certified, import, no re-derivation).
  2. New short lemma: independent D/M operations (touching disjoint active values) commute —
     by associativity of multiset replacement. Corollary: WLOG the first operation touching
     `a_1` is the sequence's first operation.
  3. True case split (by content, not location): first op is `D(a_1)` [reduces exactly to `R`,
     fully closed already by the level-`(m-1)` IH covering *every* continuation — closes for
     free] or `M(a_1,a_i)` [the genuine residual content: what if the leftover `\ell=a_1-a_i`
     is split again later?].
  4. Key lemma (new): broadened class `𝒟_j` of "dominant-tail" multisets (`M=\{c\}\cup T`,
     `T\in𝒟_{j-1}`, `c\ge2\max(T)`, recursively) — claim `e(\text{final})\ge e_j\cdot S(M)` for
     every `M\in𝒟_j` and every legal `\le j`-length D/M sequence on it (not just the single
     dyadic point). `D_m\in𝒟_m`; after `M(a_1,a_i)`, the residual is generally NOT `D_{m-1}`
     but should be `\in𝒟_{m-2}$-or-weaker — checking this dominance-preservation is the one
     hard open sub-claim (Step 4 in the file), with two concrete attack routes given (a relaxed
     dominance ratio, checked against existing numeric ties; or the minimal-counterexample
     fallback).
Key lemmas (claim + mechanism):
  - Commutativity of disjoint D/M operations — because multiset replacement on disjoint parts
    is associative; this is what licenses "WLOG `a_1`'s first touch is first" and, applied to
    branch `D(a_1)`, closes that whole branch for free (no separate multi-cut casework needed).
  - Dominant-tail class `𝒟_j` closure — because Fact 2 (`e(M)=x_1-e(\mathrm{rest})`, certified)
    recurses cleanly as long as the top element retains `\ge2\times` dominance over the tail;
    the open sub-claim is exactly whether `M(a_1,a_i)`'s leftover retains this after any further
    split, which the file narrows to a concrete, bounded, numerically-checkable question.
Open gaps: Step 4 (dominance-preservation under further splitting of `\ell`) is the only
mathematically hard step; Steps 1–3 should be closeable by the builder this round. Case (i)
beyond `m=3` (circular dependency on Case (ii)) and Case (ii) at general `m` (see
`potential-weighting-upper-bound` below) remain separately open — this revision only targets
the lower-bound §5.2 gap.
Cases to cover: within Step 4, distinguish `i=2` (degenerates to `D(a_1)`, already closed) vs.
`i\ge3` (the real content).
Watch out for: do not silently re-derive the falsified general "merging never increases `e`"
lemma inside Step 4(i)'s relaxed-dominance attempt — that lemma is false for *arbitrary* side
multisets; any surviving version here must lean on `D_m`'s specific numeric structure, not a
generic inequality.

potential-weighting-upper-bound: revise
Target: same whole theorem; this revision targets Case (ii) of the upper bound at general
`m\ge3` (Case (i) is already fully closed for every `m` via the sibling file's §2d).
Technique: induction loading (KB Pólya "generalize/strengthen the hypothesis") applied within
the already-certified Lemma D/M framework — strengthen the induction hypothesis itself (not
the choice of policy) so a 2-level-lookahead correction is carried automatically, rather than
searching for a single-step greedy rule (both natural single-step rules are conclusively
falsified and must not be re-proposed).
Skeleton:
  1. Diagnose precisely why the scalar IH bound is lossy: substituting `g(\text{residual},m-1)
     \le e_{m-1}\cdot S(\text{residual})` (a lossy upper bound) in place of the true recursive
     optimum `g(\text{residual},m-1)` throws away exactly the information (a near-tied pair
     deeper in the residual) that both counterexamples exploit — by direct comparison of the
     bound's prediction vs. the true optimal D/M sequence on both known counterexamples.
  2. Bounded diagnostic task (do first, 2 known data points, no new search): for each of the two
     falsified-rule counterexamples, tabulate what extra structural fact about the residual
     (e.g. `a_3-a_4`, or the ratio of that gap to `a_1-a_2`) the true optimal first move needed
     to "see" that neither Rule 1 nor Rule 2 tracked.
  3. Propose and test a first concrete richer-IH shape (Form E/E' in the file): bound
     `g(M,m-1)` not by the scalar `e_{m-1}\cdot S(M)` alone but by a `\min` against an explicit
     2-level-lookahead term (mirroring how Case (i)'s own closure, §2d, combined two IH forms
     via a `\min` rather than picking one a priori) — verify against both diagnostic examples
     before attempting any general-`m` write-up.
Key lemmas (claim + mechanism):
  - Lossiness diagnosis (already established this round, in the file) — because the IH's
    scalar bound and the true recursive optimum provably diverge exactly at the two known
    counterexamples; this is the concrete evidence motivating why a vector/richer IH, not a
    better single-step rule, is needed.
  - Candidate 2-level-lookahead refinement (Step 3) — because it generalizes the exact same
    "min of two IH-supplied bounds" mechanism that closed Case (i)'s form-A promotion (§2d) one
    level deeper, matching the structural diagnosis in Step 1.
Open gaps: the entire richer-IH shape is unverified — Step 2's diagnostic and Step 3's
candidate-testing are the concrete, bounded next tasks; no general-`m` proof exists yet.
Cases to cover: none beyond the two already-known counterexamples for calibration; general-`m`
casework (if any remains after the richer IH) is future work.
Watch out for: do not re-propose Rule 1 (top-two-ratio) or Rule 2 (smallest-gap match), or any
single-step rule that is a deterministic function of only the current top-`O(1)` ranks/gaps —
both are proven, permanent dead ends.

concavity-minimax-duality: revise (repurposed — new target/technique, old mechanism abandoned)
Target: same whole theorem; this repurposed slug targets the lower-bound direction (`D_m`
resists every XY response, for every `m`) — the SAME gap as `dyadic-cascade-induction`'s §5.2',
but via a structurally independent mechanism (a second, parallel line of attack on the shared
wall, not a variant of the induction-loading route).
Technique: global amortized potential / monovariant argument (KB "Invariants & monovariants"),
adapted from crux `aimo-0196` (adversary maintains a local potential no single opposing move
can push below a floor, using a "frozen this turn" trick) — a universal-over-all-responses
claim proved without ever naming XY's move, structurally different from both the case-split
induction (`dyadic-cascade-induction`) and the policy-search (`potential-weighting-upper-
bound`). Old mechanism (global concavity of the true value function `g`) is proven FALSE
(certified `lemmas/non-concavity-of-g-at-n2.md`) and is permanently abandoned, including the
narrower `a_1\ge1/2`-restricted variant (checked again this round by the altframing explorer,
`0/4329` violations — plausible but explicitly NOT this round's diversifying move per
CLAUDE.md, since it reuses the same piecewise-affine/edge-normal machinery every sibling
already has; recorded as a fallback fact only).
Skeleton (new §7 in the file):
  1. Import Lemma D/M, Fact 1, Fact 2 (all certified, no re-derivation) — restate XY's action
     against `D_m` as a length-`\le m` D/M-operation sequence.
  2. State the three properties a valid potential `\Phi(M,r)` must satisfy: (P1) normalization
     `\Phi(D_m,m)=e_m\cdot S(D_m)`; (P2) monovariance, no single legal operation can lower
     `\Phi`; (P3) `\Phi(M,0)\le e(M)` once budget is exhausted. Combining gives the whole lower
     bound in one shot, no case split.
  3. First concrete candidate to test (cheap, bounded): `\Phi(M,r):=S(M)/(2^{|M|}-1)`
     (motivated by the exact recursion `1/e_m=2^{m+1}-1`, so it reproduces `e_m` exactly at
     every dyadic point) — check it against the already-tabulated `m=2,3,4` intermediate-state
     numeric tie data in `dyadic-cascade-induction` §5.2 (not just endpoints). **Known caveat**:
     this candidate is false for arbitrary multisets (e.g. a tied pair gives `e=0<S/3`), so it
     can at best hold restricted to multisets actually reachable from `D_m` — the builder's job
     is to test, locate the failure if any, and correct (e.g. via a `𝒟_j`-style restriction,
     cross-checking against the sibling file's Step 4 before duplicating work).
  4. Fallback if Step 3's candidate fails outright: build `\Phi` directly from Fact 2's exact
     identity as a worst-case amortized recursive bound, using an explicit "just-split, so
     frozen this move" resource-freezing trick mirroring crux `aimo-0196` and cross-checking
     against `dyadic-cascade-induction`'s own commutativity finding (§5.2' Step 1).
Key lemmas (claim + mechanism): the (P1)-(P2)-(P3) potential-method reduction itself is the
key structural lemma — because once established, `e(\text{final})\ge\Phi(\text{final},0)\ge
\Phi(D_m,m)=e_m\cdot S(D_m)` is an immediate chain of inequalities requiring no case analysis
of XY's strategy at all.
Open gaps: no candidate `\Phi` has been verified to satisfy all three properties — this entire
skeleton is new and unproved; Step 3 is the concrete bounded first task.
Cases to cover: none prescribed by the skeleton itself (that's the point of the monovariant
method) — if Step 3's candidate needs restriction, the restriction's boundary cases become the
new casework, TBD.
Watch out for: do not let `\Phi:=e` itself be re-tested as the candidate — this is exactly the
already-falsified "merging never increases `e`" monotonicity lemma in disguise (dead end, do
not re-derive).

elementary-exchange-smoothing: retire (no build this round or beyond, absent a new target)
Target/Technique/Skeleton: unchanged from round 2 (local mass-shift smoothing near the dyadic
point in Case (ii), n=2) — not revised further; stalled since round 2, and its remaining goals
(global Case (ii) coverage, the `a_2/a_3=2` condition) are already fully and unconditionally
subsumed by `dyadic-cascade-induction` §2c's complete n=2 Case (ii) closure, so continuing
would not diversify the field. Recommend the reviewer certify a merged canonical
`lemmas/vertex-lemma.md` from this file's Step A (general, includes the iterated-cuts
corollary) and `dyadic-cascade-induction`'s §3 (base single-cut statement), retiring the
duplication. Step C's convex-hull gradient-certificate technique (`λ=(2/7,1/7,4/7)`) stays on
record as a reusable pattern, not separately certified.
Open gaps: none pursued further this round — this is a retirement, not an active skeleton.
Cases to cover: none (retired).
Watch out for: do not dispatch a builder to extend this slug's own Case (ii) global-coverage
gap — it is redundant with already-established, less-conditional results elsewhere in the
population.

---

Suggested build-set candidates (outline-reviewer makes the final call):
- `dyadic-cascade-induction` — close §5.2' Steps 1–3 (should be quick/mechanical) and attempt
  Step 4's dominance-preservation sub-claim (the hard part); real, concrete, bounded next task.
- `potential-weighting-upper-bound` — carry out the bounded 2-point diagnostic (Step 2) and
  test the 2-level-lookahead candidate (Step 3) against both known counterexamples; do not
  proceed to a general-`m` write-up until both pass.
- `concavity-minimax-duality` — test the `S(M)/(2^{|M|}-1)` candidate potential (Step 3)
  against the existing `m=2,3,4` intermediate-state numeric data; report where/whether it
  breaks and correct or fall back per Step 4.
- `elementary-exchange-smoothing` — no build; flag to the reviewer only for the recommended
  `lemmas/vertex-lemma.md` merge/certification (a lemma-cache housekeeping task, not a builder
  dispatch on the approach itself).

Files touched this round: `results/imo-2026-03/approaches/dyadic-cascade-induction.md`,
`results/imo-2026-03/approaches/potential-weighting-upper-bound.md`,
`results/imo-2026-03/approaches/concavity-minimax-duality.md`,
`results/imo-2026-03/approaches/elementary-exchange-smoothing.md`. No new slug opened (the
altframing explorer's top pick, crux `aimo-0196`'s global monovariant, was folded into the
repurposed `concavity-minimax-duality` rather than a fresh slug, since that slug was already
flagged RETHINK with no other salvageable forward plan — this keeps its Elo history attached to
a genuinely new mechanism rather than fragmenting the population further).
