# Outline review — round 18, imo-2026-03

## Context check

Read `results/imo-2026-03/current.md` (round-17 log, "Rules"/"Next" sections in
`/tmp/memory/run_state.md`) and both target approach files' current on-file
state (round-17 build, latest sections: `greedy-halving-adversary.md`
§"Proposition 32"/"Theorem 32"/"Open gaps" lines 3294-3620ish; `lp-duality-
certificate.md` §"Round 17" Convex-Combination Futility Theorem). No slug in
this round's outline revives a recorded dead end: greedy-halving-adversary's
target (I1 band-floor for sub-case (b), v1∈(s,p2)) is exactly the round-15/16
crux, not a re-litigation of anything closed; lp-duality-certificate's Tail
Exchange Lemma / Danskin mechanism is new — distinct from the three families
already proven dead for case (b2) (peel/bisect/recurse via
`peel-and-bisect-ih-dead-ends.md` + `recursive-image-escape-dead-end.md`;
weighted-combination via `convex-combination-futility-theorem.md`; naive
p2-only boundary-continuity, refuted this round's explorer). Good — the
outline explicitly calls out and avoids all three in its "Watch out for"
section.

## greedy-halving-adversary — APPROVE

**Claimed reformulation verified.** The outline's "coupled I1 band-floor"
target is not a fresh guess — it is the outline's own restatement of exactly
what the approach file's Theorem 32/Step 4 already derived and left open
(lines 3396-3428 of the file): dropping the hypothesis $v_1\le s$ breaks the
Two-Threshold Floor's $I_2\le s-v_1$ bound (goes negative), and the file's own
algebra shows the residual reduces to a genuine *lower* bound on the
middle-band integral $I_1=\int_{v_2}^{v_1}u_{R'}$ — restated by the outline as
"$I_1\ge g(v_1,s,p_2)$, sharper than the flat $-(v_1-v_2)/2$ near $v_1=p_2$."
I checked the algebra: $I_1 = A(R'_{>v_2})-A(R'_{>v_1})$ does follow from the
`upper-truncation-identity`/integral-formula convention ($A(R'_{>v})=
\int_v^\infty u_{R'}$, and $v_1<v_2$'s ordering gives the telescoping
difference over $[v_2,v_1)$ correctly) — this restatement is faithful to the
file's own Step 1 formula, not a new claim requiring independent re-proof.

**Outline correctly flags the previously-failed constant as insufficient**
("the crude context-free ceiling is provably exactly $q_1$ ... too weak,
already known") and does *not* propose re-trying it — this matches the
file's own honest diagnosis (§Step 4) and the round-15/16 "single bottleneck"
framing (memory rule, round 17 log). The proposed new mechanism (per-cut
charging on the tail's own construction, bounding $I_1$ using $v_1$'s
position relative to $s$, not just raw band width) is a genuinely new lever
not yet tried on this specific quantity — every prior attempt used a single
flat/global bound, this is the first proposal to use $v_1$'s *position*.

**Soundness of the mechanism itself.** The charge/pairing scheme as sketched
(process tail cuts in rank order; each cut either straddles the band and
contributes a boundable signed charge, or lies wholly inside/outside and
contributes 0/boundable) is a standard style of argument (essentially a
refined interval-covering bound using the tail's actual cut structure instead
of a crude sup) — plausible in principle, no logical circularity: it does not
assume the conclusion, and it correctly reduces to a genuinely open
inequality rather than smuggling in an unproved fact as a "then it follows."
The outline is explicit that whether the charge bound is *sharp enough for
the whole range* is open (step 6 explicitly instructs "if not tight enough,
report the residual sub-range, don't force a claim of full closure") — this
is exactly the honest scoping CLAUDE.md's rigor rules require, not
overclaiming.

**One thing to flag for the builder (not fatal, minor):** the outline asserts
the context-free ceiling is "provably exactly $q_1$" as settled background —
this is stated as this round's explorer's finding, not independently
re-verified by me. It is used only as motivation ("too weak, don't retry
this route"), not as a step the proof depends on, so it is low-risk even if
imprecise; the builder should not need to re-cite it as a load-bearing
lemma. No case-coverage issue: the outline correctly restricts scope to
sub-case (b), $v_1\in(s,p_2)$ only, leaving $\ell(F)\ge3$ out, matching the
file's own current scope.

**Verdict: APPROVE.** Sound target, sound (if unproven) new mechanism,
honestly gapped, correctly scoped, no dead-end revival.

## lp-duality-certificate — APPROVE (ambitious, correctly hedged)

**Mechanism check (Tail Exchange Lemma + Danskin/envelope theorem).** The
setup — fix $p_1,p_2$ in case (b2)'s box, let Liu Bang optimize the tail
marking $(p_3,\dots,p_{n+1})$ over an $(n-2)$-simplex of fixed total $s$,
where $\Phi_{\min}(\text{marking})$ is itself a min over Xiang Yu's
already-certified-compact response polytope (`vertex-minimum-theorem`, cited,
not re-derived) — is a legitimate reduction: Liu Bang genuinely has
unconstrained freedom to choose any positive tail marking summing to $s$
(unlike Xiang Yu, whose moves must literally cut existing pieces), so a mass
transfer $p_i\to p_i+\epsilon,\ p_j\to p_j-\epsilon$ is a bona fide legal
alternative marking, not a hypothetical relaxation. I checked the stated
form of Danskin's theorem: for $f(x)=\min_{y\in Y}g(x,y)$ with $Y$ compact and
$g$ continuous, the one-sided directional derivative of $f$ at $x_0$ in
direction $d$ equals $\min_{y^*\in\arg\min}\, \partial_d g(x_0,y^*)$ — this is
the textbook *min*-of-derivatives form (not max), and the outline states it
correctly ("bounded by the min ... of the corresponding partial derivative").
The subsequent first-order-optimality argument (at a maximizer over tail
markings, every legal direction's one-sided derivative must be $\le0$, so
either an interior stationarity/tie condition holds or the maximizer sits on
a boundary face, $p_i\to0$) is a standard, non-circular KKT-style argument;
it does not assume the conclusion.

**This is a genuinely different mechanism from every previously-dead route
for case (b2)** — it operates on Liu Bang's own marking freedom (the
maximization variable), not on Xiang Yu's response space (already fully
smoothed by `vertex-minimum-theorem`) and not on combining/weighting
already-known primal strategy *values* (the route the Convex-Combination
Futility Theorem foreclosed). The outline's own "Watch out for" section
correctly enumerates and excludes all three previously-dead families
(peel/bisect/recurse, weighted-combination, naive boundary continuity) and
gives concrete reasons each is inapplicable here — this is not a relabeled
retry.

**Honesty of scoping.** The outline is explicit that step 4 (the exact
stationarity characterization — the actually hard, new content) is
*unsolved*, that this round's explorer's numeric evidence (worst tail ratio
$\approx1.8$, not the clean ladder ratio 2) is noisy and not yet the
condition itself, and gives an explicit cheap-kill gate: check first whether
even $n=3$'s single free tail parameter admits a clean closed-form
stationary point before attempting general $n$; if not, report the Exchange
Lemma (step 2) alone as this round's real, certifiable content rather than
force an incomplete step 4. This is a properly load-bearing lemma
description with a stated mechanism (Danskin/envelope + legality of the
transfer), not a bare label — good practice per CLAUDE.md.

**Risk flagged, not fatal.** This is the most ambitious single-round target
in the outline (an open-ended new smoothing argument with the hardest step
explicitly unsolved going in) — appropriate given case (b2) has now defeated
three full mechanism families over rounds 13-17. The outline itself
anticipates possible non-closure and instructs an honest partial report,
consistent with this project's established practice on ambitious pivots
(e.g. round 6's plateau-break). Not a reason to RETHINK — a reason to make
sure the builder does the cheap $n=3$ single-parameter sanity check *before*
sinking the round into a general-$n$ characterization, exactly as the
outline's own open-gaps section instructs.

**Verdict: APPROVE**, with the outline's own gating instruction (check $n=3$
closed-form stationarity first; report step 2 alone as sufficient progress if
step 4 doesn't close) treated as mandatory, not optional.

## rank-pigeonhole-budget — advance, no build needed

Correctly left un-built this round; Claim (A) is already a fully closed,
reviewer-certified milestone (round 8 APPROVE-at-own-scope). Kept live in the
population as the anchor for cited machinery (Theorem GC(m), Case I Closure
Theorem, exchange-smoothing-vertex-maximization). No action required.

## Diversity check

The two built slugs attack orthogonal halves of the theorem (Claim B lower
bound vs. Open Gap 1 upper bound case (b2)) via genuinely different
mechanisms this round (per-cut charging on a fixed reduced instance vs.
envelope-theorem optimization over Liu Bang's own marking freedom) — this is
not a shared-gap plateau; no diversity concern to flag this round.

## Ranking

Cleared staleness on both target slugs (last set round 17) by anchoring
against the established field: `rank-pigeonhole-budget` (verified-milestone,
fully closed Claim A) beats both `greedy-halving-adversary` and
`lp-duality-certificate` (still-open partial fronts); `greedy-halving-
adversary` beats `lp-duality-certificate` for round 17 (a concrete new
theorem, Theorem 32, closing a majority sub-range, vs. a purely negative
foreclosure result with zero new coverage); both beat the dormant/dead-end
comparators `smoothing-compactness-certificate` (inactive since round 4) and
`integer-lattice-reduction` (confirmed dead end). New Elo: rank-pigeonhole-
budget 1766.9 > greedy-halving-adversary 1623.9 > lp-duality-certificate
1592.5 > smoothing-compactness-certificate 1536.3 > integer-lattice-reduction
1386.0 (others unchanged, not compared this round).

No new slugs to register this round (both approaches keep their existing
slugs — revised in place, not copied/branched).

build set: greedy-halving-adversary, lp-duality-certificate
