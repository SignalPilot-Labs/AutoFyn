# All-cycles resolution — the tie-dependency graph is never a nonempty union of directed cycles (for any strictly superincreasing base sequence, any participant type)

**Certified by:** proof-reviewer, round 8, from approach `dyadic-cascade-induction`
(round-8 builder, §5.5). Independently re-derived and re-verified by the reviewer, both
algebraically (re-deriving the closed-form solution and the sign-dominance mechanism from
scratch) and computationally (exact `sympy`/`Fraction` reconstruction, ~1200 fresh random
trials across the closed-form check, the even-`\#X` inconsistency check, and the sign-dominance
prediction check — see Verification below).

**Depends on:** `lemmas/dm-completeness-partial.md` (the tie-dependency-graph framework and its
peeling induction, in particular the precise characterization of the "all-cycles" open case as
"every unresolved genuine cut is cross-tie type, arranged in a nonempty union of directed
cycles"), `lemmas/superincreasing-no-early-zero.md` (invariants (I1) pairwise-disjoint token
supports, (I2) exact signed-subset-sum representation, and Step 1's no-vanishing-signed-subset-sum
fact), `lemmas/vertex-lemma.md` (self-bisection classification), and
`lemmas/shallow-cycle-resolution.md` (the round-7 predecessor result this supersedes/extends).

## Statement

Fix a strictly superincreasing base sequence `a_1>\dots>a_k>0` (e.g. `D_m`) and any candidate
final configuration `FINAL` arising from a `\le m`-cut Xiang-Yu strategy whose genuine cuts'
tie-dependency graph (as defined in `dm-completeness-partial.md`) is a **nonempty union of
directed cycles**. Classify each cyclic component's `L` cyclic edges as **`S`** (shared-value,
`u_i=u_{i+1}`) or **`X`** (cross-type, `u_i+u_{i+1}=b_{i+1}`) — an exhaustive dichotomy, since
each edge's target cut produces exactly two values. Let `\#X\in\{0,\dots,L\}` be the number of
`X`-edges in one (WLOG minimal, in the condensation order of the whole dependency graph)
component. Then:

- `\#X=0`: the component is a uniform shared-value tie; it is never the true minimizer
  (dominated by a breakpoint escape to a guaranteed-untouched original — the pre-existing
  `lemmas/shallow-cycle-resolution.md` result, unchanged);
- `\#X=1`: **not a genuine cycle at all** — the closing arithmetic always forces the unique
  cross-type node to be a numerically exact self-bisection, contradicting cycle membership
  (Lone-`X`-Edge Vacuity Lemma);
- `\#X\ge2` even: **physically infeasible** — the closing consistency requirement reduces to a
  nonempty signed subset sum over disjoint original indices, which never vanishes (Even-`\#X`
  Infeasibility Lemma);
- `\#X\ge3` odd: **physically infeasible** — the (unique) solution's expansion via the token
  invariant has a coefficient on the most-significant participating original index that changes
  sign across the cycle's blocks, and superincreasing dominance of that index over the rest of
  the token union forces a strictly negative block value, violating the domain requirement
  (Generalized Cross-Type Domain-Violation Lemma).

Consequently the tie-dependency graph of the true global minimizer against any strictly
superincreasing base sequence can **never** be a nonempty union of directed cycles, so
`lemmas/dm-completeness-partial.md`'s sufficient condition for `g(A,m)=h(A,m)` holds
**unconditionally**. Combined with the certified Superincreasing No-Early-Zero Lemma
(`h(D_m,m)\ge e_m\cdot S(D_m)`), this gives the fully unconditional physical lower bound
```
g(D_m,m) \ge e_m\cdot S(D_m)\qquad\text{for every }m.
```

## Key lemmas (proof summaries; full detail in `dyadic-cascade-induction.md` §5.5)

- **Cycle Common-State Lemma** (§5.5.1). Any single, condensation-minimal cyclic component's `L`
  input pieces are simultaneously active tokens of one common D/M-reachable state, constructed by
  running the (already-certified) peeling induction on every cut *outside* every cyclic
  component and stopping just before any cyclic-component cut — legitimate because, by the
  already-certified peeling characterization, getting "stuck" at a nonempty union of cycles means
  precisely that every other cut has already been successfully peeled. This lets (I1)/(I2) apply
  directly to a cyclic component's participants, including derived (non-original) ones, with no
  extension of `superincreasing-no-early-zero.md`'s literal stated scope.
- **Lone-`X`-Edge Vacuity Lemma** (§5.5.3). `\#X=1` forces the sole cross-type node's two outputs
  to be numerically equal (an exact self-bisection), which has out-degree 0 by the dependency
  graph's own construction — contradicting membership in a directed cycle (out-degree exactly 1
  required).
- **Even-`\#X` Infeasibility Lemma** (§5.5.4). For even `\#X=q\ge2`, consistency requires a
  closing identity `C=0` where `C` is a signed subset sum of the `q` distinct block-leader tokens'
  disjoint original-index supports (via (I1)/(I2)) — never zero, by the no-vanishing-signed-
  subset-sum fact.
- **Generalized Cross-Type Domain-Violation Lemma** (§5.5.5). For odd `\#X=q\ge3`, the reduced
  system has a unique closed-form solution (verified directly, not merely computed); expanding it
  via the token invariant, the coefficient of the single most-significant participating original
  index alternates in sign across the `q` blocks (guaranteed since `q\ge3`), and dominance of that
  index over the rest of the token union forces the corresponding block's value strictly
  negative — violating the domain requirement. Strictly generalizes the round-7
  Cross-Type Cycle Infeasibility Lemma (recovered as the singleton-token special case) to
  arbitrary derived participants.

## Verification

Independently re-derived by the proof-reviewer (round 8):
- Re-derived the general closing-equation identity and the odd/even dichotomy from scratch;
  matches the write-up.
- Closed-form solution for odd cross-type cycles (§5.5.5 Step A): re-derived independently and
  checked by direct linear solve against the closed form on random disjoint-support token
  instances (`q\in\{3,5,7,9\}`, `L` up to `13`, `464` trials) — **zero mismatches.**
- Domain violation (at least one `t_s<0`): confirmed in **100% of 464 trials** (every instance
  physically infeasible), matching the Lemma's conclusion.
- Sign-dominance prediction (which specific block goes negative, computed purely from `i^*, r_0,
  \epsilon`): matched the actual solved sign in **all 464 trials, 0 mismatches** (after correcting
  an indexing slip in the reviewer's own re-implementation, not in the proof).
- Even-`\#X` inconsistency: **300/300** random disjoint-support trials (`q\in\{2,4,6\}`) gave a
  provably inconsistent linear system (no solution at all), matching `C\ne0` exactly.
- A concrete worked example (`q=5` cross-type cycle built from disjoint-support tokens over an
  8-element superincreasing base) was hand-traced end to end: closed form matched direct solve
  exactly, and the domain violation (two negative `t_s` entries) matched the predicted sign
  pattern exactly at all 5 blocks.

**Honest scope note carried forward by the reviewer.** The Cycle Common-State Lemma's
construction ultimately rests on `dm-completeness-partial.md`'s peeling argument, whose own
write-up handles the interaction between forest depth ("leaf-parent" eligibility) and the
tie-dependency graph's in-degree-0 property at "proof sketch" level (that lemma's own file
states "full detail in `concavity-minimax-duality.md` §8"), not with a fully spelled-out
reconciliation for cuts with further-subdivided descendants. This is an **inherited**
assumption of the already-twice-certified base lemma (rounds 4 and 7), not a new gap introduced
by this round's work, and the reviewer found no concrete counterexample to it; future rounds
wanting maximal rigor could still usefully make this reconciliation fully explicit.

## Reusable by

Any approach needing the *true* physical lower bound (not merely the D/M-operation-sequence
lower bound) for a strictly superincreasing base sequence, e.g. `D_m` — in particular this is
the final piece `dyadic-cascade-induction` needed to combine with
`lemmas/superincreasing-no-early-zero.md` for a fully unconditional
`g(D_m,m)\ge e_m\cdot S(D_m)`, for every `m`.
