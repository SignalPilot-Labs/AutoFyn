# Round 23 outline review — imo-2026-03

Read: `results/imo-2026-03/current.md` (full, through round 22),
`.ranking.json`, all three live approach files
(`greedy-halving-adversary.md`, `rank-pigeonhole-budget.md`,
`lp-duality-certificate.md`), `lemmas/vertex-minimum-theorem.md`,
`lemmas/p-space-chamber-vertex-theorem.md`, `/tmp/round-23/proof-outliner.md`,
and both explorer reports.

## Verdict: outline is sound. No RETHINK. All three ADVANCE as proposed.

### Check 1 — "Vertex-Minimum Theorem applied directly to B={b}∪T'" is a genuinely different mechanism, not a relabeling

Verified directly against `greedy-halving-adversary.md` lines ~4685–4914
(Insert-Element Identity + its diagnosis) and `vertex-minimum-theorem.md`.

The round-22 diagnosis is a **structural** claim about one specific proof
strategy: decompose $A(B)=2A(T'_{>b})-A(T')+(-1)^jb$ and try to close
$A(B)\ge f(n)$ by plugging in a **one-sided lower bound** on $A(T')$ (the
only kind of fact this file's induction machinery supplies anywhere).
Since $-A(T')$ carries a minus sign, any such lower bound moves the
inequality the wrong way — this is proved for *every* relative position
of $b$ against $T'$, not case-by-case, and is correctly not to be
re-attempted under any name.

The outliner's proposal does not decompose $A(B)$ via this identity at
all. It applies the fully general, already-certified Vertex-Minimum
Theorem (`vertex-minimum-theorem.md`, proved with zero ladder- or
game-specific assumptions, independently derived twice in round 3) to
the *whole object* $B=\{b\}\cup T'$ as a fixed-composition instance:
$b$ is a fixed reference point, $T'$ is the free continuum. The theorem
gives that $\min_{T'}A(B)$ is attained at a vertex pinned by tight
degenerate-cut/tie constraints — then $A(B)$ is evaluated **directly**
at each such vertex via `odd-run-reduction-lemma` (a closed-form sort-
and-alternate computation on the actual merged multiset, not a bound
built by combining a separate bound on $A(T')$ with anything). This is
the same program that already closed Claim A's Case I
(`exchange-smoothing-vertex-maximization` /
`case-i-closure-theorem`) and the interior-cross-tie family
(`interior-cross-tie-evaluation-formula`) — reused, not reinvented, and
structurally distinct from the ruled-out decomposition. Confirmed: this
is a genuinely new mechanism for this branch, not previously attempted
(round 20's three routes checked "$b$ dominant"/"non-dominant" cases of
the *same* decomposition; round 22's diagnosis only ruled out that one
decomposition, it never tried direct vertex-minimization on $B$ itself).
**Approved to build**, with the outliner's own honest caveat preserved:
the hard remaining step (bounding the finite vertex family) must be
reported as an open gap if not closed this round, not asserted.

### Check 2 — lp-duality-certificate's $n=3$ case-(b2) exhaustive enumeration: tractable and non-circular given the corrected scope

Verified directly against `lemmas/p-space-chamber-vertex-theorem.md`
(items 1–3 plus the round-22 reviewer correction appended in the same
file) and `current.md`'s round-22 entry.

The corrected item 3 states: of case (b2)'s three Box walls, only
$p_2\le T/D_n$ (case b1) is unconditionally general for every $n$; the
$p_1\ge T/2$ wall is unconditionally closed **only for $n\le3$**; case
(a) $p_2\ge a_nT/2$ is closed **conditional** on the standing strong-
induction hypothesis one level down. At $n=3$, "one level down" is
$P(2)$ — and `current.md` records $n\le2$ as fully closed in this
project (Claim A + Claim B both closed for $n\le2$). So at $n=3$
specifically, all three Box walls really are unconditional (the $p_1\ge
T/2$ wall directly, case (a) because its one-level-down hypothesis is
already an established fact, not an open conjecture) — the compactness-
fix Corollary applies at $n=3$ with **zero** open caveats. This is not
circular: it does not assume case (b2) at $n=3$ to prove case (b2) at
$n=3$; it assumes case (b2) is settled at $n\le2$ (already true) to
patch the boundary of $n=3$'s box. Confirmed correct — the outliner's
claim checks out.

Tractability: `p-space-chamber-vertex-theorem.md`'s own §R22.1.1 already
has one worked $n=3$ chamber (composition $(1,1,0,0)$, closed form
$\Phi_{\min}=p_1/2+p_3+p_4$, walls $p_1\ge2p_3$, $p_2\le p_3+p_4$). The
outliner's "a dozen or so" estimate for the rest is stated as an estimate
to be confirmed by the builder, not assumed — appropriately hedged, not
overclaimed. This is a legitimate, bounded, real milestone (a genuine
unconditional closure of case (b2) at one value of $n$), distinct from
and not blocked by the general-$n$ conditionality problem.

### Dead-mechanism cross-check

Checked the outline's three proposals against `current.md`'s full record
and both approach files' own "ruled out" sections directly (not just the
outliner's summary):

- `greedy-halving-adversary`: proposal is vertex-minimization on $B$ (new,
  see Check 1) plus a pure bookkeeping audit of Theorems 33–36's case
  coverage at $n=3,4$ — no proof content re-attempted, not a repeat of
  any of the four refuted generic mechanisms (`refutation-of-tail-
  refinement-monotonicity`, `parity-coincidence-and-zero-iff-dead-end`,
  `splitting-monotonicity-refuted-dead-end`, `greedy-top-two-matching-
  insufficiency`, `band-invariance-conjecture-refuted-dead-end`) nor the
  one-sided-bound-on-$A(T')$ mechanism itself.
- `rank-pigeonhole-budget`: proposal is a cross-check/gap-mapping of the
  same vertex family via its own discrete toolbox — explicitly told not
  to re-attempt a one-sided discrete bound (which would hit the identical
  wall per round 20's cross-cutting finding). Correctly scoped as either
  a cross-verification (if greedy's vertex family lands this round) or a
  gap-mapping exercise (if not) — neither re-attempts a dead mechanism.
- `lp-duality-certificate`: item 1 (scope fix) is pure citation
  correction, no math re-derived. Item 2 ($n=3$ exhaustive enumeration)
  is new — none of the 9 confirmed-dead mechanisms (peel-zero-slack,
  bisect-containment, convex-combination-of-primal-values, boundary-
  continuity-across-chambers, Danskin/concavity, surrogate-argmax-tail
  majorization, constraint-side LP duality, and the two round-20/21
  entries plus `box-corner-tail-vertex-decomposition-refuted`) is an
  exhaustive-vertex-enumeration-at-fixed-small-$n$ mechanism; this is
  genuinely different from all nine (confirmed by reading `current.md`'s
  round 14/18/19/20/21/22 entries directly, not taking the outliner's
  word). Item 3 (Route-A $(X,q)$ symbolic optimization) reuses only
  already-certified lemmas on an already-reduced finite problem — no
  new/dead mechanism involved.

No mechanism proposed this round duplicates anything on either dead list.

## Field ranking

All three approaches were `stale: true` (last outcome — round 22's three
CHANGES REQUESTED verdicts — not yet folded into Elo). Ranked head-to-head
on round-22 outcomes: `rank-pigeonhole-budget` (Claim A remains solved/
APPROVE, plus a correctly-proved conditional biconditional, no gaps found)
and `greedy-halving-adversary` (five new sound, gap-free results, most
concrete live front) both edge out `lp-duality-certificate` (sound core
theorem but a real overclaim was found and needed correction this round);
`rank-pigeonhole-budget` and `greedy-halving-adversary` treated as
roughly even (different fronts, both clean). Submitted via
`update_ranking`:
- greedy-halving-adversary beats lp-duality-certificate
- rank-pigeonhole-budget beats lp-duality-certificate
- rank-pigeonhole-budget draws greedy-halving-adversary

Resulting Elo (stale cleared on all three): `rank-pigeonhole-budget`
1786.15, `greedy-halving-adversary` 1717.18, `lp-duality-certificate`
1527.44.

## New approach

None registered — the outliner correctly declined to open a new slug this
round (both live gaps have concrete, non-dead, previously-untried next
steps; not yet a 3+-round plateau on one identical wall). Flag carried
forward: if lp-duality-certificate's $n=3$ case-(b2) enumeration also
stalls or dies next round, that front will have exhausted essentially
every natural LP/vertex mechanism and should trigger a genuinely distant
new approach to the general upper bound.

## Build-set instructions (unchanged from outliner, gate-approved)

- `greedy-halving-adversary`: apply Vertex-Minimum Theorem directly to
  $B=\{b\}\cup T'$, evaluate via `odd-run-reduction-lemma`; report the
  finite vertex family honestly (closed or flagged as gap). Bundle the
  cheap $n=3$/$n=4$ Theorem 33–36 exhaustiveness audit.
- `rank-pigeonhole-budget`: Claim A untouched; cross-check/gap-map the
  same vertex family via discrete pigeonhole toolbox — not a fresh
  one-sided bound attempt.
- `lp-duality-certificate`: fix item 3's scope (cheap, do first), then
  the $n=3$ case-(b2) exhaustive chamber enumeration (headline target);
  Route-A $(X,q)$ symbolic optimization as secondary if time permits.

build set: greedy-halving-adversary, rank-pigeonhole-budget, lp-duality-certificate
