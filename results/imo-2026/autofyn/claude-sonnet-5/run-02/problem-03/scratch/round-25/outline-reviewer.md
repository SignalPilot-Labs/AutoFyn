## imo-2026-03 — outline review, round 25

Reviewed `/tmp/round-25/proof-outliner.md` (revisions to all 3 live slugs:
`rank-pigeonhole-budget`, `greedy-halving-adversary`, `lp-duality-certificate`),
cross-checked against `current.md`, the three approach files' certified
lemma citations, and `/tmp/round-25/math-explorer-covering-family.md`.

### rank-pigeonhole-budget: revise — APPROVE (with the outline's own caveats kept intact)

Target: inequality (7.9.1), $A(T''')\le c_1-f(n)$, the last of 4 candidate
vertex types in the T'-cuts-p4 sub-case.

- The proposed **Restriction Lemma** (single-element concentration: the
  A-maximizer over legal $\le(n-5)$-cut refinements of the tail
  $\{p_5,\dots,p_{n+1}\}$ can be taken with all spare cuts on one element)
  is the load-bearing new claim and is honestly flagged as unproved this
  round ("Open gaps": "new and unproved... the load-bearing new step the
  builder must actually construct, not assume"). I independently stress-
  tested this numerically (fresh script, not the explorer's/builder's):
  at $n=8$, tail $\{p_5,\dots,p_9\}$ (5 elements), budget $k=3$, an
  exhaustive search over every cut-distribution partition $(c_1,\dots,c_5)$
  of $k=3$ across the 5 tail elements (each partition stress-tested with
  2000-5000 random split-ratio trials in exact `Fraction` arithmetic) found
  the unique maximum $15/511$ attained ONLY at the fully-concentrated
  distribution $(0,3,0,0,0)$ — every genuinely spread distribution (e.g.
  three distinct elements each bisected once) topped out strictly lower
  ($37269/1277500\approx0.0292 < 15/511\approx0.0294$). This is real,
  independent corroborating evidence the Restriction Lemma's *direction* is
  correct — good, since the outline correctly does not claim it as proved,
  only as the target to build.
- The fallback in step 4 ("if the Restriction Lemma resists a quick proof,
  apply the tie-vertex argument directly to the full multi-element
  polytope") is well-posed as an escape hatch, not a silent skip.
- The "Watch out for" section correctly separates this sub-target from
  greedy-halving-adversary's own overlapping target (see cross-approach
  note below) rather than collapsing them into one slug.
- No circularity: step 5's evaluation cites `odd-run-reduction-lemma`
  (already certified) on a finite tie-vertex family produced by step 4 — a
  standard evaluate-the-vertex step, not an assumption of the conclusion.

Verdict: **APPROVE**. Sound skeleton, correctly scoped, genuinely new
mechanism (dualized 1-dimensional tie-vertex + a new exchange/concentration
argument), numerically corroborated before build.

### greedy-halving-adversary: revise — APPROVE (with one dependency check flagged, already required by the outline itself)

Target: $h(m)$ (Theorem 38's own induction quantity), attacked via
"is $\{b\}\cup T'$ literally a legal Xiang-Yu response to the $(n-4)$-ladder,
so the standing IH $L(n-4)$ applies by direct substitution."

- This is legitimate strong induction (invoking $L(n-4)$, the general lower
  bound one level down, $n-4<n$), **not** circular — it does not invoke
  $h(m)$'s own statement or the not-yet-proved general-$n$ result at level
  $n$. Confirmed by re-reading step 3/4's literal wording: it substitutes
  into $L(n-4)$, a smaller instance of the standing induction, exactly the
  pattern already used throughout this project (e.g. rounds 8, 22 IH usage).
- Step 3's literal identification (does the $a/b$ split of $p_4$, plus $T'$,
  actually arise as a legal full response to the smaller ladder) is
  correctly flagged as **unverified** and to be checked *first*, cheaply,
  before further case-by-case work — good triage, matches the explorer's
  own recommendation.
- Step 4's fallback path (diagnose precisely where the identification fails,
  try a weaker max-direction substitution) and step 6's final fallback
  (hand-enumerate $m=2$'s remaining branches only, explicitly NOT general
  $m$, since general-$m$ enumeration is confirmed intractable by the
  explorer) are both honest, bounded, non-circular escape hatches.
- Correctly reiterates the already-certified dead end (do not re-attempt
  Cross-Level Rescaling Lemma applied directly to $\{c\}\cup S$) and does
  not violate it.

Verdict: **APPROVE**.

### lp-duality-certificate: revise — APPROVE, contingent on the outline's own exact-arithmetic requirement (do not accept a numeric/floating-point deliverable as closing)

Target: n=3 case (b2)'s box, via the round-25 explorer's 5-chamber
sub-family {Bisect{1,4}, Bisect{1,2}, DS-Above, Triple-Pin, R22.1.1} and a
6-branch case split.

- **This is explicitly sampling/floating-point evidence from the explorer
  stage, not a proof** — the explorer report says so in its own words
  ("I did not complete a rigorous proof... the LP infeasibility findings
  above are floating-point `scipy.optimize.linprog` results with a
  numerical margin, corroborating but not yet a certified exact-arithmetic
  proof"). The outline correctly does NOT present this as already
  established: step 4 explicitly says "This upgrades the explorer's
  floating-point scipy result... to a rigorous exact-arithmetic certificate
  — do this in Fraction/Rational LP or by hand Farkas-lemma-style
  combination... not floating point," and "Open gaps" repeats: "the
  exact-arithmetic infeasibility proof for each of the 6 branches is NOT
  yet done... this is the actual remaining work." "Watch out for" repeats
  the warning a third time. **This satisfies the dispatch instruction: the
  outline scopes this as "prove rigorously," not "assume proven."** No
  fix needed here — flagging explicitly in case the builder is tempted to
  submit the numeric result as a closure; the builder must not report
  "case (b2) closed" on the strength of the $10^6$-trial / grid sampling
  alone, only on an actual exact-arithmetic (or hand) infeasibility
  argument for all 6 branches plus the boundary-vertex disposal.
- **One real, fixable citation issue found**: step 5's boundary-vertex
  disposal cites `unconditional-p2-threshold-closure` as (part of) the
  machinery closing the vertex $p=(2/5,4/15,1/5,2/15)$, which sits on
  $p_2=4/15=a_3T/2$ (case (a)'s own defining wall, $p_2\ge a_nT/2$). I
  checked the cited lemma file directly: `unconditional-p2-threshold-
  closure`'s actual statement is for the **opposite** wall, $p_2\le
  T/D_n$ (case (b1)'s wall) — it does not apply here. The correct
  mechanism is "Theorem B" (the recursive `generalized-peel-identity`
  sufficient condition for case (a), $p_2\ge a_nT/2$), which the outline
  does also list (step 5: "Theorem C'/Theorem B at $n\le3$") — so the
  right citation is present but bundled with a wrong one. This mirrors a
  pre-existing mislabeling already in the approach file itself (line
  ~698, "Case (a) closure... via ... `unconditional-p2-threshold-
  closure`" — a citation error from an earlier round, not introduced this
  round). Since at $n=3$ Theorem B's recursion bottoms out at an
  already-closed base case (no live IH dependency), the underlying
  closure is genuinely available; only the citation needs cleaning up.
  **Instruct the builder**: cite `generalized-peel-identity`/"Theorem B"
  (case (a)'s own recursive closure, unconditional at $n\le3$) for the
  boundary vertex, not `unconditional-p2-threshold-closure` (which is
  for the disjoint $p_2\le T/D_n$ wall and does not apply to this point).
- The 6-branch case-split (on $p_1$ vs $p_2+p_3$, and R22.1.1's 2-inequality
  feasibility trichotomy) matches the explorer's own case-split exactly;
  no gap in the exhaustiveness claim was introduced beyond what the
  explorer already flagged as needing exact re-verification.

Verdict: **APPROVE**, with the citation fix above passed to the builder
(non-blocking — a one-line correction, not a rebuild).

### Cross-approach overlap: rank-pigeonhole-budget's (7.9.1) vs greedy-halving-adversary's Claim-B/h(m)

Both target overlapping content this round (the $T'$-cuts-$p_4$, $b=c_2$
vertex value). This is **not** the single-gap trap (splitting one proof
across sibling slugs): the two mechanisms are genuinely different —
rank-pigeonhole-budget attacks via a new Restriction Lemma + dualized
1-dimensional tie-vertex evaluation; greedy-halving-adversary attacks via
literal substitution into the standing general induction $L(n-4)$. Per
the standing rule (memory rule #3: independent mechanisms on the same
hard direction is acceptable diversity, not a forced merge), this is fine
as two parallel approaches, not one target duplicated. The outline
explicitly instructs the builder to cross-check and cite whichever closes
first rather than silently duplicate — this is the right instruction given
both builders run in parallel this round without live communication; the
proof-reviewer should reconcile any actual overlap in the results
afterward (as happened in prior rounds, e.g. round 23's convergent
Theorem-37 finding from two angles).

### Small-case sanity performed this round
- Restriction Lemma direction (single-element concentration maximizes
  A(T''')): verified numerically via exhaustive partition search, exact
  `Fraction` arithmetic, n=8 (see above). Consistent with the claim.
- Citation of `unconditional-p2-threshold-closure`: read the lemma file
  directly, confirmed statement is for $p_2\le T/D_n$, not $p_2\ge
  a_nT/2$ — mismatch found and flagged above.

### No RETHINK issued.
All three revisions are sound in mechanism, correctly scoped (no
overclaiming of unproved numeric evidence as proof), diverge from each
other in genuine technique even where their targets overlap, and do not
repeat any recorded dead end. Registered slugs unchanged (all three
already in the population); no new approach to register this round, no
copy needed.

## Ranking

Anchored the field to last-round outcomes: greedy-halving-adversary and
lp-duality-certificate were APPROVE last round (round 24, real progress,
strongest live); rank-pigeonhole-budget fixed its flagged direction bug
and narrowed to one clean inequality (also live, comparable strength).
Compared against the broader population (parked/dead-end slugs) to anchor
newcomers' ratings are not at stake here since no new slugs this round —
just clearing `stale` flags and light reordering among the 3 live leaders.

build set: greedy-halving-adversary, lp-duality-certificate, rank-pigeonhole-budget
