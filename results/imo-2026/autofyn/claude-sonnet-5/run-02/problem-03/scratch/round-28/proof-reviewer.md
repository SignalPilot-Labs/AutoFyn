# Round 28 proof review — imo-2026-03

Note: the dispatched build-report paths
(`/tmp/round-28/proof-builder-rank-pigeonhole-budget.md`,
`-greedy-halving-adversary.md`, `-lp-duality-certificate.md`) do not exist
on disk (only `math-explorer-*.md`, `outline-reviewer.md`,
`proof-outliner.md` are present in `/tmp/round-28/`). Per the dispatch
instructions this review is based directly on the primary source — the
updated `results/imo-2026-03/approaches/*.md` files — which is the
authoritative artifact regardless.

All three claims were independently re-derived from scratch with fresh
exact-`Fraction` Python scripts (not the builders' own), not just
re-read. No overclaim was found in any of the three files this round —
a first in several rounds (rounds 24–27 each had at least one overclaim
the reviewer had to correct).

## 1. `rank-pigeonhole-budget` — new §7.16, target (star_3)=MinFloor(4)

**Verdict: CHANGES REQUESTED. True Status: partial (correctly reported
as such in the file's own scope note — see below).**

**Shape-count fix.** The outline's own stars-and-bars formula
$\sum_{b=0}^3\binom{b+3}{3}=1+4+10+20=35$ computes the correct count of
"$\le3$ cuts" compositions, but the outline's stated total was "$20$" —
a transcription slip. Independently confirmed by direct computation:
$\binom{7}{4}=35$ (compositions of $\le3$ into 4 parts, stars-and-bars
with a slack variable) and $\binom{6}{3}=20$ (compositions of *exactly*
$3$ into 4 nonnegative parts) are both correct, and are genuinely
different counts. The file's correction is right.

**Closure-clause justification.** The claim that closing only the 20
exactly-budget-3 shapes (on their closed domains) suffices to prove the
theorem for all 35 shapes rests on: every lower-budget shape's polytope
is contained in the closure of some exactly-budget-3 shape's polytope
(pad with a degenerate cut, fragment $\to0$), and this degenerate
boundary point is exactly a family-(I) ("fragment$=0$") tight vertex of
`vertex-minimum-theorem`. This is a standard, correctly-argued
topological closure/padding argument — no gap.

**Master Theorem I** (10 shapes, $\pi_1$ untouched): peel the untouched
$\pi_1$ (strict unique max since $\pi_1=8>4=\max(\pi_2,\pi_3,\pi_4)$) via
`sharp-dominant-removal-identity`, then bound the remainder by Fact 2
($A\le\mathrm{Total}$). I independently re-verified this with 2000 fresh
random trials per shape across all 10 shapes: zero violations.

**Master Theorem II** (3 shapes, one cut on $\pi_1$, $\pi_2$ untouched):
a clean 3-case peel cascade ($a\le3$: Fact 1 directly; $a\in(3,4)$: one
more peel + Fact 2 on the fixed-total-3 tail; $a=4$: `odd-run-reduction-
lemma` collapses the 3-fold tie). I independently re-verified with 2000
fresh trials per shape across all 3 shapes: zero violations. Note the
argument correctly uses only $\mathrm{Total}(V)=3$, never the tail's cut
count or distribution — genuinely reusable beyond this specific instance
(certified as a standalone lemma, see below).

**Shape $(3,0,0,0)$ closes by citation.** This shape is literally Claim
(A) of the same file at $n=3$; `claim-a-full-closure` (already certified,
round 8) applies directly. Confirmed the citation is exact (same tail
composition, same target constant $a_3=\pi_4=1$).

**Achievability on all 20 shapes.** For the 6 residual shapes
$(1,1,0,1),(1,1,1,0),(1,2,0,0),(2,0,0,1),(2,0,1,0),(2,1,0,0)$, I
independently re-verified all six explicit constructions realizing
$\{4,4,2,2,2,1\}\to\{2,1\}$ (odd-run reduction) with $A=1$: per-piece
arithmetic checks out ($4+4=8$, $2+2=4$, $4+2+2=8$, etc.), and direct
alternating-sum computation of each construction gives $A=1$ exactly, in
all 6 cases. Achievability on the full 20-shape family is genuinely
established.

**The 6-shape lower-bound residual is genuinely open, not silently
assumed.** The file explicitly shows Master Theorem II's peel-cascade
technique fails on a real sub-region ($f_1\in(3,4)$, with a second free
parameter $f_2$ or $g_1$ genuinely interacting) — a concrete boundary
computation is given where the crude Fact-2 bound yields $A\le5$ against
a needed $\le1$, i.e. the technique is not merely unproven but shown
insufficient there. I independently spot-checked this with a 200,000-
trial randomized search on shape $(2,0,1,0)$'s full parameter space:
zero violations of $A\ge1$, minimum found $\approx1.00004$ — corroborates
(does not prove) that the conjectured value $1$ is correct, exactly as
the file itself frames it (numeric support, not a substitute for the
missing hand proof). The file does not silently assume this residual
closed anywhere I could find — every downstream "Net status" and
"Current best" passage explicitly states "$(\star_3)$ is therefore NOT
closed this round."

**Status honesty check.** The file's `## Status` header reads "solved,"
but its scope note immediately qualifies this as scoped to Claim (A)
only — a target that was already fully closed in round 8 and is
unaffected by this round's separate §7.16 work. This is accurate, not
an overclaim: §7.16's new work targets a genuinely different statement
$(\star_3)$/MinFloor(4), which the file's own text repeatedly and
correctly reports as unclosed. No correction needed.

**1 new lemma certified:** `master-theorem-ii-single-split-untouched-
second-piece` (Master Theorem II — genuinely new, reusable beyond the
specific ladder instance). Master Theorem I is a special case of the
already-noted (but not separately certified as a standalone file in this
project) `minfloor-untouched-top-closure` general theorem; not
separately certified this round to avoid a duplicate/near-duplicate
lemma file.

## 2. `greedy-halving-adversary` — new Lemma A + Theorem 42

**Verdict: CHANGES REQUESTED. True Status: partial (file's own Status
header already correctly says `partial`).**

**Lemma A (General Anchored-Tie Bound).** Statement: for $w>0$, finite
multiset $X$ with $\max(X)<w$, $g:=w-\mathrm{Total}(X)$, and $t^\ast\in X$
of any multiplicity $\mu\ge1$, $A(\{t^\ast\}\cup\{w\}\cup X)\ge g+t^\ast$.
I re-derived the proof by hand: the odd-$\mu$ case is a direct
`sharp-dominant-removal-identity` + `odd-run-reduction-lemma` +
trivial-bound chain (matches the already-certified
`anchored-single-tie-deletion-bound` verbatim). The even-$\mu$ case
correctly generalizes the certified `even-multiplicity-non-maximal-tie-
closure` mechanism to abstract notation: split $X$ at $t^\ast$'s rank
into $H,L$; the Rank-Split Formula plus `odd-run-reduction-lemma`
(cancelling the even-multiplicity block against $L$) gives $A(X)=A(H)+
(-1)^kA(L)$; `insert-element-identity` plus two applications of
`sharp-dominant-removal-identity` (both legal since $w>\max(X)\ge\max(H)$)
substituted through gives an exact identity for $A(B)$ in terms of $g$,
$\mathrm{Total}(H)-A(H)\ge0$, $\mathrm{Total}(L)\pm A(L)\ge0$ (trivial
bound plus `alternating-sum-nonnegativity`), and $\mu t^\ast$; this
closes both parities of $k=|H|$, giving $A(B)\ge g+(\mu-1)t^\ast\ge
g+t^\ast$. I independently re-verified this with a fresh 50,000-trial
exact-`Fraction` script over arbitrary (non-ladder) $w,X,t^\ast$: zero
violations, minimum slack exactly $0$ (matching the proof's own tight
case). No gap found — the algebra is correct and genuinely general (no
ladder-specific fact used anywhere in the derivation).

**Theorem 42 instantiation.** $w=q_1$, $X=S''$ (legal tail refinement of
$\{q_2,\dots,q_{m+1}\}$). Domination fact ($\max(S'')\le q_2<q_1$) is
immediate from the ladder's strict descending order and the fact that
splitting never raises a fragment above its parent. Mass identity
$g=q_1-\mathrm{Total}(S'')=2^mf(m)-f(m)(2^m-1)=f(m)$ — I re-derived this
sum ($\sum_{i=2}^{m+1}2^{m+1-i}=2^{m-1}+\dots+1=2^m-1$) by hand and
confirms exactly. Combined with Theorem 38's Claims (I)/(II) for the
$c=0,q_1$ vertices (unchanged, cited not re-derived), the three-vertex
case split ($c=0$; $c=q_1$; $c=t^\ast\in S''$) is exhaustive for the
single free coordinate $c$ per `vertex-minimum-theorem`, and Lemma A
closes the new third vertex unconditionally. I independently re-verified
the full ladder claim ($A(\{c\}\cup\{q_1\}\cup S'')\ge f(m)$ for every
$c\in(0,q_1]$ and every legal $q_1$-untouched $S''$) with a fresh script
generating per-piece-respecting random legal refinements for $m=1,\dots,
5$: zero violations across 3000 trials per $m$. No gap found.

**Honest scoping of the q1-cut sub-case.** The file explicitly and
repeatedly states the "$S$ cuts $q_1$" branch is NOT addressed this
round, for every $m\ge3$ — it is not silently swept into Theorem 42's
closure. The file gives a specific, checked reason no domination anchor
was found there (as $q_1$'s split approaches $(q_1/2,q_1/2)$, no
fragment strictly dominates the rest, mirroring the already-documented
round-26 "$c_2$-anchor" failure mode) and reports this as "we looked and
did not find," not as a proven negative result — an appropriately
calibrated claim. $m=1$ (vacuous, no q1-cut branch exists) and $m=2$
(already closed by hand, Theorems 38+39) are correctly noted as
unaffected/subsumed. $h(m)$ for $m\ge3$ is correctly reported still open.

**1 new lemma certified:** `general-anchored-tie-bound` (Lemma A).

## 3. `lp-duality-certificate` — new §R28.0–R28.3, n=4 p1>=T/2 closure

**Verdict: CHANGES REQUESTED. True Status: partial (file's own Status
header already correctly says `partial`, correctly scoped).**

**Telescoping algebra (R28.1).** Claim $a_3=a_4/(2(1-a_4))$. I
independently recomputed with exact `Fraction`: $a_4=16/31$,
$1-a_4=15/31$, $a_4/(2(1-a_4))=(16/31)/(30/31)=16/30=8/15=a_3$. Confirmed
exactly. Also $a_4>1/2$ confirmed ($a_4-1/2=1/62>0$).

**Domain partition.** Sub-case boundaries $[T/2,a_4T)$ and $[a_4T,T)$: since
$a_4=16/31\in(1/2,1)$ (confirmed above), these two half-open intervals
partition $[T/2,T)$ exactly with no gap and no overlap — trivial once
$a_4\in(1/2,1)$ is established, which it is.

**Sub-case 1 ($T/2\le p_1<a_4T$).** Theorem A (`full-match-
achievability`, already certified general-$m$) gives $\Phi=p_1$ exactly
via a 4-cut construction matching $p_1$'s fragments to $p_2,\dots,p_5$
plus a leftover $v=2p_1-T\ge0$. I independently re-verified this
construction with 2000 fresh exact-`Fraction` trials (random $p_1\ge
T/2$ markings): the constructed final multiset's alternating-sum-game
value matches $p_1$ exactly in every trial. Since $p_1<a_4T$ in this
sub-case, the bound follows immediately.

**Sub-case 2 ($p_1\ge a_4T$).** Theorem C′ (`bisect-top-recursive-
identity`, already certified general-$n$) reduces to $\Phi_{\min}\le
p_1/2+\Phi_{\min}(\text{tail};3)$. The tail is an *arbitrary* 4-piece
marking (no regime restriction), so citing round 27's fully-general
$P(4)$ (the complete, both-regime $n=3$ upper bound,
`gap-filler-four-chamber-covering` combined with case (a)/(b1)/(b2),
already reviewer-APPROVEd) is the correct and sufficient hypothesis — I
re-checked this citation is to the *complete* $n=3$ theorem, not a
restricted regime, matching round 9's established finding that Theorem
C′'s induction genuinely needs the full theorem one level down (this
project's Rule "ALWAYS treat c(3)<=8/15 ... as fully proved"). The
resulting affine-in-$p_1$ bound, maximized at $p_1=a_4T$ (since
$a_3>1/2$ makes the coefficient of $p_1$ negative — re-confirmed:
$a_3=8/15>1/2$), gives $\Phi_{\min}\le a_3T+a_4T(1/2-a_3)$. I
independently recomputed the bracket
$a_3(1-a_4)+a_4/2$ with exact `Fraction`: equals $16/31=a_4$ exactly,
matching the claimed final bound $\Phi_{\min}\le a_4T$.

**Honest scoping.** The file's Status header and R28.3 both explicitly
state this covers only $p_1\ge T/2$ at $n=4$; the $p_1<T/2$ regime is
explicitly untouched and flagged (with the round-28 explorer's
density-growth signal $28\%\to64\%$ between $n=3$ and $n=4$'s chamber
census, correctly cited as a reason to expect it substantially harder).
No claim of $c(4)\le a_4$ in general anywhere in the file — confirmed by
grep of the whole "Round 28 build" section and the Status header.

**1 new lemma certified:** `p1-geq-half-closure-n4`.

## Summary table

| slug | verdict | true Status | key gap remaining |
|---|---|---|---|
| rank-pigeonhole-budget | CHANGES REQUESTED | partial (own target, (star_3)); Claim A remains solved | 6 shapes' 3-free-parameter residual sub-region, lower bound only |
| greedy-halving-adversary | CHANGES REQUESTED | partial | h(m)'s q1-cut sub-case, m>=3 |
| lp-duality-certificate | CHANGES REQUESTED | partial | n=4's p1<T/2 regime |

No RETHINK this round — all three approaches remain viable, each with a
precisely localized open item. `current.md` updated (`## Status` remains
`partial`, `## Approaches tried` appended with the round-28 entry
replacing the stub, `## Current best` and `## Full proof` unchanged
since no new top-level sub-target closed). 3 new lemma files certified:
`lemmas/general-anchored-tie-bound.md`,
`lemmas/master-theorem-ii-single-split-untouched-second-piece.md`,
`lemmas/p1-geq-half-closure-n4.md`.

## Verification scripts (this round, reviewer-authored, not builders')

- Master Theorem I/II random-trial re-derivation (2000 trials/shape,
  20000-trial extended check).
- 200,000-trial residual-region spot-check on shape $(2,0,1,0)$.
- 6-construction achievability re-verification (exact arithmetic).
- Shape-count re-derivation ($\binom{7}{4}=35$, $\binom{6}{3}=20$).
- Lemma A general abstract re-derivation (50,000 trials, arbitrary
  $w,X,t^\ast$).
- Theorem 42 ladder-instantiation re-derivation ($m=1,\dots,5$, 3000
  trials/$m$, per-piece-respecting legal refinements).
- Telescoping/bracket algebra re-derivation (exact `Fraction`).
- Theorem A construction re-verification (2000 trials).
