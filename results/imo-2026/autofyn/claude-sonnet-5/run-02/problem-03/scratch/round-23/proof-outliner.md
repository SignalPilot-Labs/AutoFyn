# Round 23 outline — imo-2026-03

Read: `results/imo-2026-03/current.md` (through round 22), the three live
approach files (`greedy-halving-adversary.md`, `rank-pigeonhole-budget.md`,
`lp-duality-certificate.md`), `.ranking.json`, and both round-23 explorer
reports (`/tmp/round-23/math-explorer-front1-upper-bound.md`,
`/tmp/round-23/math-explorer-front2-vertex-eval.md`). Elo via
`sample_approaches`: `rank-pigeonhole-budget` 1789 (Claim A APPROVE,
otherwise stale), `greedy-halving-adversary` 1699 (stale), `lp-duality-
certificate` 1543 (stale) — all three top the field and are all `stale:
true` (last outcome not yet re-ranked this round).

## Where the problem actually stands

Status remains `partial`. Two genuinely distinct residual fronts, both
identified precisely (not vaguely) by round 22 + this round's explorers:

1. **The Case-(b) "v≥a" branch** (`greedy-halving-adversary`, Theorem 36 /
   round-22 Insert-Element Identity): target collapses exactly to
   $A(B)\ge f(n)$ for $B=\{b\}\cup T'$, $T'$ any legal $\le(n-4)$-cut
   refinement of the tail. **Structurally proved** (Insert-Element
   Identity) that no one-sided lower bound on $A(T')$ can ever close this
   — the sign is wrong, for every technique, continuum or discrete. Do
   not resubmit any "bound $A(T')$ from below" plan under any name.
2. **Case (b2)'s general-$n$ upper bound** (`lp-duality-certificate`,
   Chamber-Vertex Theorem): infrastructure (Lemma R22.1/Thm R22.2, items
   1–2) is sound and general; the finite vertex enumeration/evaluation
   that would actually close it has not been carried out beyond one
   hand-worked $n=3$ chamber. Item 3's "compactness fix" Corollary is
   **overclaimed** for $n\ge4$ (contradicts the same file's own scoping
   elsewhere) and needs a scope correction, not new mathematics.

These are different objects (front 1 is a lower-bound branch inside Claim
B; front 2 is the general upper bound $c(n)\le a_n$) — correctly kept as
separate slugs, not a shared-gap situation requiring a new far-away
approach yet. `rank-pigeonhole-budget`'s own open item (§7.6, general-$n$
closure of $(\sharp')$/$(\Diamond')$) is the *discrete* restatement of
front 1's identical wall (per round 20's cross-cutting finding) — it is
governed by the same Insert-Element-Identity sign obstruction, since that
obstruction is about the algebraic shape of the identity, not about which
proof technique (continuum vertex vs. discrete pigeonhole) is used to try
to bound the pieces.

**Correction to front 1's framing, flagged before it gets built on:** the
explorer's §1 says "$a$ is the larger of $R'$'s two top-piece fragments."
Cross-check against `greedy-halving-adversary.md` Theorem 35/36: this
matches the file's own convention ($a\ge b$, $a+b=p_3$) — confirmed
consistent, not an error. No redirect needed there.

## No re-attempts of dead mechanisms (checked against both files + current.md)

Do not resubmit, under any name: for front 1's target — any one-sided
lower-bound-on-$A(T')$ plan, naive tail-refinement monotonicity, odd-run-
reduced-size induction, coarse band/matching invariants (all explicitly
refuted, see explorer §2). For case (b2) — the 9 confirmed-dead
mechanisms (`peel-zero-slack`, `bisect-containment`, convex-combination-
of-primal-values, boundary-continuity-across-chambers, Danskin/concavity,
surrogate-argmax-tail majorization, constraint-side LP duality, and
`box-corner-tail-vertex-decomposition-refuted`, plus a 9th — check
`current.md` round 20/21 entries directly for its exact name before
building). `claiming-order-invariant` framing (Stackelberg one-shot, no
invariant loop) stays dead everywhere in this project.

## Proposed field for round 23

### `greedy-halving-adversary` — ADVANCE (front 1's main target)

Apply the already-certified, fully general **Vertex-Minimum Theorem**
(`lemmas/vertex-minimum-theorem.md`) directly to $B=\{b\}\cup T'$ as a
*whole object*, instead of decomposing $A(B)$ via the Insert-Element
Identity and bounding pieces separately. Concretely:

- Treat $b$ (fixed, 0 further cuts) and the tail $\{p_4,\dots,p_{n+1}\}$
  (with the residual $\le(n-4)$-cut budget) as a genuine instance of the
  theorem's setup — a Liu-Bang-style configuration with a fixed
  composition. The theorem (proved fully generally, no ladder-specific
  assumption in its hypotheses) then gives: $\min_{T'} A(B)$ is attained
  at a vertex pinned by exactly $d$ independent tight constraints, each
  either a degenerate cut (some $T'$-fragment $=0$) or an exact tie
  (fragment of $T'$ equals $b$, or two $T'$-fragments tied).
- Evaluate $A(B)$ at each such vertex type via the certified
  `odd-run-reduction-lemma` (already used successfully for the same
  program in Claim A's Case I closure and the interior-cross-tie family
  — reuse, don't re-derive).
- **The actual hard step, to be identified explicitly as a gap if not
  closed this round:** show the resulting finite vertex family is small
  enough to check, and that $A(B)\ge f(n)$ at every member — likely via
  the tail's own self-similar ladder structure (the tail
  $\{p_4,\dots,p_{n+1}\}$ is itself a rescaled copy of a ladder one level
  down, so `general-cross-level-rescaling-lemma` may let a vertex-level
  evaluation reduce to $(\star_{n-4})$ or similar, rather than to
  $(\star_{n-2})$ — track exactly what induction hypothesis (if any)
  each vertex type needs, and report honestly if some vertex type needs
  something not yet available).
- Do **not** re-attempt bounding $A(T')$ or $A(T'_{>b})$ one-sidedly and
  recombining — that mechanism is structurally dead per the Insert-Element
  Identity diagnosis, independent of which lemma supplies the bound.
- Secondary, cheap, bundled into this slug's build (not a separate slug):
  audit whether Theorems 33/34/35/36 jointly and exhaustively cover every
  case at $n=3$ and $n=4$ with no silent drop. If confirmed, upgrade
  $(\star_3)$/$(\star_4)$ from "used conditionally" to certified
  unconditional theorems — this is bookkeeping only (no new math) but
  removes the "conditional on $(\star_{n-2})$" qualifier from Corollary
  36c and others at $n=5,6$ for free. Report this as a clearly separated
  item so the reviewer can check it independently of the vertex-B work.

### `rank-pigeonhole-budget` — ADVANCE, but genuinely distinct sub-target

Its own Claim (A) stays `solved`/untouched. Its live gap is §7.6's
general-$n$ closure of $(\sharp')$ (equivalently, per §7.7's proved
biconditional, of $(\Diamond')$) — the discrete-counting restatement of
front 1's identical wall. Since the Insert-Element Identity's obstruction
is technique-agnostic, **do not** re-attempt a discrete one-sided-bound
argument here either (it would hit the same wall in different notation).
Instead: use this slug's native discrete/pigeonhole toolbox to
**independently evaluate** the same vertex family greedy-halving-adversary
identifies (once available this round or next) via per-level cut-budget
counting, as a genuinely different verification/derivation route to the
same finite check — valuable as an independent cross-check (this project's
practice of two independent derivations of the Vertex-Minimum Theorem in
round 3 is the precedent) rather than a duplicate. If greedy's vertex
enumeration isn't ready yet this round, this slug's builder should instead
spend the round making precise (not vague) exactly which discrete
"tie/degenerate-cut" configurations correspond to §7.6's own $v_1,v_2$
parametrization, laying groundwork for the cross-check next round —
explicitly flagged as a gap-mapping exercise, not a claimed closure.

### `lp-duality-certificate` — ADVANCE, two concrete items

1. **Scope-correction (cheap, do first):** rewrite item 3 of
   `lemmas/p-space-chamber-vertex-theorem.md` to state plainly: the
   $p_2\le T/D_n$ wall (case (b1)) is unconditionally closed for every
   $n$; the $p_1\ge T/2$ wall is unconditionally closed only for $n\le3$;
   case (a) closure is conditional on the standing strong-induction
   hypothesis. The compactness-fix Corollary itself is therefore
   conditional for $n\ge4$, not general. This is a citation-consistency
   fix, not new mathematics — flag clearly as a correction, and do not
   claim it closes anything new.
2. **Real progress target — exhaustive $n=3$ chamber enumeration for case
   (b2), fully unconditional.** At $n=3$ all three Box walls are
   genuinely unconditional (per the corrected scope above), so the
   compactness-fix Corollary applies with zero caveats. Enumerate all
   full types $(\mathbf c,\tau,\pi)$ whose chamber meets case (b2)'s box
   at $n=3$ (small, finite — one is already worked out in §R22.1.1;
   estimate the rest is "a dozen or so" per the explorer, confirm this
   count explicitly rather than assuming it), evaluate $g$ at every
   vertex via the same closed-form technique, and check $g\ge0$
   everywhere. This would be a genuine, complete, non-numeric closure of
   case (b2) at $n=3$ specifically — a real milestone, independent of
   general-$n$.
3. **Secondary, if time permits:** finish Route A's already-reduced
   finite $(X,q)$ optimization (§A.3) symbolically for the restricted
   "cut only $p_1$, tail untouched" sub-family — reuses only certified
   lemmas (`odd-run-reduction-lemma`, `pair-cancellation-identity`), no
   new machinery. Either outcome (closes $\le T/D_n$ for this restricted
   family, or finds a counterexample showing tail-cutting is necessary)
   is informative; report honestly either way.
   Do **not** attempt item 3's alternative "restate as inductive-step
   lemma using $P(n-1)$ directly" reframing this round — it's a bigger,
   vaguer rewrite of the whole compactness-fix mechanism with unclear
   payoff versus the two concrete, boundable items above; defer it unless
   both above stall.

## New slug

**None opened this round.** The field already has three approaches with
genuinely different toolboxes (continuum/measure-theoretic vertex
evaluation, discrete pigeonhole counting, LP-polytope/chamber-vertex
certificate), and both explorer reports this round found concrete,
previously-untried, non-dead-mechanism next steps for the two live gaps —
this is not yet a 3+-round plateau on one identical step calling for a
deliberately-distant new approach. **Flag for next round:** if case
(b2)'s $n=3$ exhaustive enumeration (lp-duality-certificate item 2) also
stalls or dies, that front will have exhausted essentially every natural
LP/vertex mechanism (9 dead + this one) and should trigger opening a
genuinely distant new approach to the upper bound specifically (not
another vertex/polytope variant).

## Summary instruction to outline-reviewer

- `greedy-halving-adversary`: ADVANCE — vertex-minimum-theorem applied
  directly to $B=\{b\}\cup T'$, plus bundled cheap $n=3/n=4$ case-split
  audit.
- `rank-pigeonhole-budget`: ADVANCE — cross-check/gap-mapping of the
  identical wall via its discrete toolbox, not a fresh one-sided-bound
  attempt.
- `lp-duality-certificate`: ADVANCE — scope-fix item 3, then exhaustive
  $n=3$ case-(b2) chamber enumeration (headline target), Route-A $(X,q)$
  symbolic optimization as secondary.
- No new slug this round; reassess after this round's case-(b2) result.
