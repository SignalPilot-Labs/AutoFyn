## imo-2026-03 — outline review, round 10

Reviewed: `/tmp/round-10/proof-outliner.md` against
`results/imo-2026-03/approaches/greedy-halving-adversary.md`,
`results/imo-2026-03/approaches/lp-duality-certificate.md`, `current.md`,
`lemmas/*.md`, and both round-10 explorer reports. Both slugs are revisions
(no new slugs opened this round), so no branching/registration calls are
needed — both are already in the population.

### greedy-halving-adversary — revise — **APPROVE** (with one wording fix)

Target (Claim B, the still-open half of the general lower bound) and overall
route are unchanged from rounds 4–9 — a legitimate continuation, not a
fragment: the slug still targets the whole problem's Claim-B gap, only the
*sub-case decomposition* is new this round.

Checked against the four flagged risk patterns:

1. **p2-cut self-similarity (Sub-target 2).** The outline explicitly and
   correctly declines to treat this as a genuine reduction: step 3 states in
   plain terms that the recursive step "closes exactly one of its three
   branches" and that a full closure needs "a *simultaneous* strong
   induction over all branches at every level at once." This matches the
   explorer's own diagnosis (`math-explorer-claim-b.md` §2: "it is a
   reformulation, not a reduction to something easier"). No overclaim here —
   good.

2. **ℓ(F)-Collapse Lemma / 60,000+-trial finding (Sub-target 3).** The
   outline is explicit: "do NOT write up the ... numeric finding as a
   proof — it is not one," frames the Collapse Lemma as "conjecture (to
   attempt, not assume)," and gives an honest fallback ("report the numeric
   finding honestly as unresolved-but-supportive... do not promote it to
   'proved'"). Correctly scoped as evidence, not proof.

3. **p2-vs-own-tail dominance fact.** Verified independently: for the
   n-ladder, $p_2=2^{n-1}/D$ and $\mathrm{Total}(\{p_3,\dots,p_{n+1}\})=
   (2^{n-1}-1)/D$, so $p_2 > $ that total for every $n\ge2$ — the outline's
   claimed dominance fact is correct, and it correctly notes this is
   dominance over the *sub-tail only*, not the whole multiset (the outline
   never claims the stronger, false statement $p_2>1/2$).

4. **Threshold-v Decomposition Lemma wording.** One genuine imprecision,
   not fatal: the outline says to "apply the ... identity at threshold
   r=v instead of at p2," but `cross-term-identity-threshold`'s $r$ is
   *defined* as $\mathrm{Total}(G')$ (fixed by $G'$, not a free parameter
   you substitute). I independently derived what actually happens: since
   `safe-window-lemma` already forces $v_{G'}\equiv0$ for $x\ge p_2$
   regardless of $r$, and Lemma 19 gives $u_F=\mathbb1[x<v]$ for *any* $v$,
   the cross-term collapses to $\int_0^{\min(v,p_2)}v_{G'}\,dx$ — for
   $v<p_2$ this is $\int_0^v v_{G'}\,dx$, a genuinely *partial* integral,
   not $A(G')$. I confirmed by exact-`Fraction` computation ($n=3$,
   $F=\{p_3\}$, $G'=\{p_2,p_3/2,p_3/2,p_4\}$) that Proposition 20's closed
   form $v-A(G')$ indeed **fails** here ($A(F\cup G')=2/5$ vs.
   $v-A(G')=-1/5$) — so the outline's caution ("it may not collapse to
   'v-A(G'')' the way Prop 20 did") is correct and load-bearing. The
   substance of the outline is right; only the phrase "apply at threshold
   r=v" is misleading about *how* the lemma is invoked (r is not chosen,
   the $[0,v)$ cutoff falls out of Lemma 19's indicator, not from
   re-parametrizing $r$). **Change requested:** builder should replace
   "instantiate the identity at threshold r=v" with "use Lemma 19's
   pointwise indicator plus safe-window-lemma to show the cross-term
   integral truncates at $\min(v,p_2)$" — same conclusion, correct
   mechanism. This is a clarity fix, not a rethink; nothing in the outline
   depends on the false reading.

Case coverage for Claim B stated honestly: $\ell(F)=0$ (closed,
`cross-term-vanishing-lemma`), $\ell(F)=1,v\ge p_2$ (closed,
Props 20–22 minus the p2-cut branch), $\ell(F)=1,v<p2$ (open, Sub-target 1
this round), $\ell(F)\ge2$ (open, numeric only, Sub-target 3). No case
silently dropped.

### lp-duality-certificate — revise — **APPROVE**

Target (general upper bound, $p_1<T/2$ regime) unchanged; still targets the
whole problem's remaining upper-bound gap.

1. **Ladder-specific lemma reuse guard.** The outline explicitly and
   correctly bars reuse of `half-window-vanishing-lemma`,
   `ratio-2-spacing-lemma`, `last-element-bound` for Route A step 3 ("all
   three are one-line consequences of the ladder identity $p_1=2p_2$...a
   genuinely new evaluation argument is required"). Matches the explorer's
   finding #4 exactly. Good — the marking-agnostic reduction lemmas
   (`exchange-smoothing-vertex-maximization`, `vertex-minimum-theorem`,
   `leftover-formula`, `pair-cancellation-identity`) are confirmed
   marking-agnostic by direct reading of their certified lemma files (no
   ratio-2/ladder hypothesis anywhere in their statements or proofs) —
   Route A step 2's reuse is legitimate, not an overclaim.

2. **"Both known witnesses solved by perfect pairing" (Route B).** The
   outline treats this correctly as scouting evidence only: step 4 calls
   the two witnesses "test cases the construction must reproduce, not as
   proof," and the Watch-out section repeats this in stronger language
   ("exactly two-and-a-half data points... not a proof or even strong
   statistical evidence at this scale"). No overclaim — this matches the
   explorer's own framing verbatim.

Route A step 3 and Route B step 3 are both honestly flagged as the entire
open content of the routes ("neither route is close to a finished
general-n proof"). Case coverage: $p_1\ge T/2$ correctly cited as already
closed for $n\le3$ (not re-derived), $p_1<T/2$ is the sole target. Both
routes are genuinely different mechanisms (vertex characterization vs.
matching/construction), acceptable diversity within one slug's revision
(not a same-wall repeat — this is the first round to try either).

### Diversity check
The two live slugs attack disjoint halves of the theorem (lower bound
Claim B vs. general upper bound) via different mechanisms — no shared-gap
risk this round. rank-tie-vertex-reduction, rank-pigeonhole-budget,
smoothing-compactness-certificate remain parked (not built this round);
no action needed on them, ranking below reflects their last certified
state, unchanged.

### Registration
No new slugs opened this round — nothing to register. Both approaches keep
their existing slugs.

### Ranking
Anchoring both live slugs against the strongest parked approaches (all
"stale" flags on greedy-halving-adversary and lp-duality-certificate from
round 9's outcomes get cleared by this round's comparisons):
- rank-pigeonhole-budget (verified-milestone, Claim A fully closed) is the
  strongest single result on file — beats every currently-partial slug.
- greedy-halving-adversary and lp-duality-certificate are both live,
  actively narrowing real gaps (round 9: 4 new lemmas / Theorem C′ +
  telescoping identity respectively) — rank them close to but below
  rank-pigeonhole-budget, and above the parked/lower-momentum approaches.
- rank-tie-vertex-reduction (advanced, closed (★★) for c_1=1) stays
  ahead of the parked approaches with older/weaker last outcomes
  (smoothing-compactness-certificate, self-similar-*, dyadic-band-occupancy,
  exchange-argument-extremal-response) which have not moved in several
  rounds.
- dead-ends (bijective-mersenne-pairing, integer-lattice-reduction,
  claiming-order-invariant) stay at the bottom.

build set: greedy-halving-adversary, lp-duality-certificate
