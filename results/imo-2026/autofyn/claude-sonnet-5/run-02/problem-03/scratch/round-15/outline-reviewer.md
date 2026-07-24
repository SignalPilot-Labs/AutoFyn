# Outline reviewer report — IMO-2026-03, round 15

## Verdict

Both round-15 outlines are technically sound in their proposed *techniques*
(no wrong theorem invoked, no circular reasoning), and neither relies on an
unverified numeric-only claim to justify a proof step. However, spot-checking
turned up one genuine, non-trivial logical gap in `greedy-halving-adversary`'s
framing (below) that could have wasted a full builder round if not caught
now. The `lp-duality-certificate` outline's central new claim checks out on
independent recomputation. No field-plateau found this round (both fronts
made independently-verified progress in round 14, matching the outliner's own
assessment) — **no new slugs opened**, per the outliner's recommendation.

## Spot-check 1: greedy-halving-adversary — "items 1 and 2(b) are the same
gap, closing v<s closes both for free"

**Finding: this claim is an overstatement as currently argued.** Verified by
tracing the algebra by hand (not trusting the outline's assertion):

Lemma 25 (certified, round 11) gives, exactly, for sub-case (b)
($v_1,v_2<p_2$, $F_1=\{v_1\}\cup P$, $F_2=\{v_2\}\cup P$):
$$A(F\cup G')=A(G')+A(F_1\cup G')-A(F_2\cup G').$$
Note the **minus sign** on $A(F_2\cup G')$. Item 1, as literally scoped
("$\ell(F)=1$, $v<s$: prove $A(F\cup G')\ge f(n)$"), is a proposal to prove
only a *lower* bound on this quantity, mirroring Proposition 24's final step
one level up. But two separate lower bounds — $A(F_1\cup G')\ge f(n)$ and
$A(F_2\cup G')\ge f(n)$ — do **not** combine into a lower bound on the
difference $A(G')+A(F_1\cup G')-A(F_2\cup G')$: knowing $A(F_2\cup G')$ is
at least $f(n)$ gives no control on how much larger it might be, which is
exactly the direction that matters since it is subtracted.

This is not a hypothetical worry: the approach file's **own round-12
analysis of sub-case (c)** (lines ~2391–2410 of the file) explicitly
diagnoses precisely this asymmetry for a structurally identical situation —
"Propositions 20–24... all prove *lower* bounds on this exact quantity...
never an *upper* bound... [sub-case (c)] needs a new, upper-bound-in-
direction fact about exactly the $\ell(F)=1$, $v<p_2$ family that the
existing machinery... does not supply." The round-15 outline's claim that
item 1's closure automatically finishes sub-case (b) "for free" ignores this
exact self-diagnosed precedent from three rounds ago in the same file.

There are two legitimate ways Target A could still work, and the outline
should have named which one it intends (it currently does neither
explicitly):
- **(i) Exact closed form.** Proposition 24 in fact derives an *exact*
  expression, $A(F\cup G')=p_2-v+A(R')$, before taking the final $\ge f(n)$
  step. If the $v<s$ extension likewise yields an exact expression in
  $v,s,A(R')$ (not just an inequality), substituting $v_1,v_2$ into it and
  subtracting via Lemma 25 could close sub-case (b) directly, no separate
  upper bound needed.
- **(ii) Explicit upper bound.** If the $v<s$ mechanism (as literally
  proposed — bounding the correction term via `max-domination-lemma` /
  `triangle-bound-for-a`, both two-sided facts) only ever yields an
  inequality, the builder must extract an **upper** bound on $A(F_2\cup G')$
  specifically, not merely reconfirm $A(F_2\cup G')\ge f(n)$.

I have added a reviewer correction note directly to
`approaches/greedy-halving-adversary.md` (appended after the Round 15
outline section) spelling this out, so the builder does not spend the round
proving item 1's literal lower-bound statement and then discover sub-case
(b) is still open. This does not kill Target A — it remains the
highest-leverage open item — but the outline as written needs this
correction before build.

Target B (item 3, triangle-bound route) and Target C (deferred) raise no
similar concern: Target B only ever needs a single-direction lower bound on
$A(F\cup G')$ directly (no Lemma-25-style signed decomposition involved), so
`triangle-bound-for-a` applied crudely is the right shape of tool there.

## Spot-check 2: lp-duality-certificate — Cross-Piece Sign-Assignment
Identity on the n=3 witness

**Finding: confirmed, by independent exact-Fraction reconstruction, not by
trusting the explorer's report.** Reconstructed the round-14 near-tight
witness $p\approx(0.4468,0.2591,0.2251,0.0691)$ as exact fractions (summing
to 1), then searched (independently, not using the explorer's own script)
for a split of $p_1\to\{a,b\}$, $p_3\to\{c,d\}$ realizing the claimed
sign pattern. Found (exact fractions):
$$a=\tfrac{2101077}{12500000},\ b=\tfrac{3483923}{12500000},\
c=\tfrac{817113}{12500000},\ d=\tfrac{1996637}{12500000},$$
sorted order $b>p_2>a>d>p_4>c$ — i.e. $p_1$'s two fragments ($a,b$) land on
odd ranks together with $p_4$, and $p_3$'s two fragments ($c,d$) land on
even ranks together with $p_2$, matching the claimed sign pattern
($p_1$:+, $p_4$:+, $p_2$:$-$, $p_3$:$-$). Direct computation of
$\Phi=\sum_{\text{odd rank}}$ value against the formula
$(T+p_1-p_2-p_3+p_4)/2$ gives **exact equality**
($2579/5000$ both sides). This corroborates the outline's claim is not
merely plausible but concretely verified on a genuine legal split (2 cuts,
well within an $n=3$ budget), and the target (formalize the general
identity from `pair-cancellation-identity` + `odd-run-reduction-lemma`,
then attack sign-vector feasibility) is a reasonable, well-motivated next
step — approved as stated, no correction needed.

## Ranking

`greedy-halving-adversary` (Elo 1605→1602 after clearing stale) and
`lp-duality-certificate` (Elo 1589→1592 after clearing stale) remain the
two live fronts on the whole-problem claim; recorded a draw comparison
between them via `update_ranking` to clear both `stale` flags, reflecting
that round 14 saw both make genuine, independently-verified,
no-gap-found progress with neither RETHINK — no rank-order change
warranted by round 14's outcomes alone. `rank-pigeonhole-budget` (Elo 1708)
remains highest but stays out of scope (Claim (A) already fully closed, not
a build target). No new slugs registered or copied this round; the field is
not plateaued (both fronts advanced independently in round 14 and again have
concrete, distinct new leads this round from two different explorers), so
per the outliner's own recommendation and CLAUDE.md's plateau rule, no
branching was forced.

## Round 15 dispatch

Proceed with the outliner's build set as originally proposed, with the
correction note now appended to `greedy-halving-adversary.md`'s Target A —
the builder for that slug must read the new "Round 15 reviewer correction"
section before starting.

build set: greedy-halving-adversary, lp-duality-certificate
