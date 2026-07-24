# Scouting report — Case (b) "v ≥ a" branch's upper-bound obstruction

Lens: what upper-bound technique (if any, in KB / crux corpus / by analogy
with certified lemmas) could supply the missing bound this branch needs,
and whether closing $(\star_{n-2})$ is a cheaper win than attacking the
branch directly.

## 1. The precise open target

Setting (from `approaches/greedy-halving-adversary.md`, Theorem 36 /
round 22 additions): fix $n\ge5$. Theorem 35/36's object is a legal
refinement $R'$ of the ratio-2 tail $\{p_3,\dots,p_{n+1}\}$ using $\le
n-3$ cuts. **Case (b)** is the sub-case where $R'$'s own top piece $p_3$
is itself cut: $R'=\{a,b\}\cup T'$ with $a\ge b>0$, $a+b=p_3$, and $T'$ a
legal refinement of $\{p_4,\dots,p_{n+1}\}$ using the remaining budget.
The target is $(\Diamond)$: $\Delta(n,v):=A(R')-2A(R'_{>v})\le v-f(n)$ for
every $v\in(0,s)$ ($s=\mathrm{Total}(R')$).

Round 22 (Corollary 36c) closed the sub-range $v\in(0,\min(R'))$
conditionally on $(\star_{n-2})$. **`a` is the larger of $R'$'s two
top-piece fragments** ($a\ge b$, $a+b=p_3$), and "$v\ge a$" is literally
the sub-range where $v$ is at least the largest element of $R'$, so
$R'_{>v}=\varnothing$ and $\Delta(n,v)=A(R')=a-A(B)$ where $B:=\{b\}\cup
T'$ (via the certified `dominant-element-removal-identity`, since $a\ge
p_3/2\ge\max(T')$ makes $a$ dominant). The target collapses to
**$A(B)\ge f(n)$, for every legal $T'$** — this is the precise open
statement, restated exactly by the Insert-Element Identity:
$$A(B)=2A(T'_{>b})-A(T')+(-1)^{j}b\ \ge\ f(n),\qquad j:=|T'_{>b}|.$$

**Why the existing toolkit can't reach it (already diagnosed, do not
re-derive):** every fact this file's induction supplies anywhere
($(\star_m)$ for any $m$, Fact 1 nonnegativity, Theorem 36b) is a **lower**
bound on some $A(\cdot)$. Since $-A(T')$ enters with a minus sign, a lower
bound on $A(T')$ moves the inequality the wrong way. This is proved
structurally (not just checked case-by-case) in `insert-element-identity`
— **do not re-attempt "bound $A(T')$ below and hope"; that mechanism is
provably insufficient by the identity's exact algebraic shape, for every
relative position of $b$ against $T'$.**

## 2. What has already been tried/ruled out (do not repeat)

- Round 20's three routes into $p_1<T/2$/case-(b2)-style attacks (checked
  "$b$ dominant" and "$b$ non-dominant" separately) — superseded by the
  round-22 structural diagnosis above, which covers every configuration
  at once.
- `refutation-of-tail-refinement-monotonicity`: "refining the tail can
  only weakly increase $A$" is **false** in general (explicit
  counterexample, $n=2$). Any argument assuming naive monotonicity in the
  refinement is dead.
- `parity-coincidence-and-zero-iff-dead-end`: induction on $\ell(S)$ (the
  odd-run-reduced size) cannot escape the same obstruction — ruled out as
  an induction variable for this kind of gap.
- `splitting-monotonicity-refuted-dead-end`, `greedy-top-two-matching-
  insufficiency`, `band-invariance-conjecture-refuted-dead-end` — generic
  monotonicity/band/matching shortcuts, all refuted with exact
  counterexamples. Do not re-propose a coarse invariant of this flavor.
- `box-corner-tail-vertex-decomposition-refuted` (9th confirmed-dead
  mechanism, round 22, for the *separate* case-(b2) upper-bound-on-$c(n)$
  front — different object from this branch, but the same family of
  "restrict to a sub-polytope and hope it dominates" idea; also dead
  there).

## 3. What `star_{n-2}` actually is, and whether it's a cheap win

$(\star_m)$ is **not** a small side lemma — it is literally the *whole
project's general lower bound*, Claim B in full, restated one level down:
"every legal Xiang-Yu response using $\le m$ cuts to the unit $m$-ladder
has $A\ge f(m)$." Theorem 36b/Corollary 36c invoke $(\star_{n-2})$, so for
$n=5,6$ this needs $(\star_3),(\star_4)$ — i.e. Claim B closed *in full*
at levels 3 and 4, not merely Claim A (which *is* already fully closed for
every $n$ by `rank-pigeonhole-budget`/`claim-a-full-closure`).

**This is not a cheaper target in general** — closing $(\star_m)$ for
general $m$ *is* the open problem. But there is a genuinely cheap,
narrowly-scoped audit worth doing this round: Theorem 33 + Theorem 34 +
Theorem 35(a,b) + Theorem 36 together purport to be an exhaustive case
split of Claim B (by the position of $v_1$/the split value against
$p_2,p_3$, and by Case (a)/(b) of whether $p_3$ is touched), and Theorem
36 explicitly closes Case (b) **unconditionally at $n=3$ (vacuous) and
$n=4$ (direct finite computation, all ten sub-ranges including the "$v\ge
a$"-type breakpoint)**. If a careful audit confirms the union of Theorems
33/34/35/36 is genuinely exhaustive and gap-free at $n=3$ and $n=4$
specifically (no case silently dropped), then **$(\star_3)$ and
$(\star_4)$ become fully certified, unconditional theorems** — which would
immediately upgrade Corollary 36c (and every other "conditional on
$(\star_{n-2})$" result in the file, e.g. Theorem 34(b), Proposition 22,
Proposition 24) from conditional to **unconditional at $n=5,6$** for free,
with zero new mathematics. This audit is cheap (bookkeeping, not proof)
and should be dispatched alongside — but not instead of — direct work on
the "$v\ge a$" branch, since it does not touch the branch's actual content
at all (it only removes the "conditional on $(\star_{n-2})$" qualifier at
two specific levels, and doesn't help general $n\ge7$ at all, which needs
$(\star_5),(\star_6),\dots$, an infinite regress that this audit alone
never resolves).

## 4. Promising directions for the actual upper-bound gap

**(a) Reframe as a direct vertex-minimization on the whole object $B$,
not as separate bounds on its pieces.** The Insert-Element Identity's
diagnosis is about decomposing $A(B)$ into $A(T'_{>b})$ and $A(T')$ and
bounding each one-sidedly — but $B=\{b\}\cup T'$, with $b$ fixed and $T'$
ranging over all legal $\le(n-4)$-cut refinements of $\{p_4,\dots,
p_{n+1}\}$, is *exactly* an instance of the shape the already-certified,
fully general **Vertex-Minimum Theorem** (`vertex-minimum-theorem`,
round 3) was built for: "for any fixed reference multiset and any fixed
cut-allocation composition, the min of $\Phi$ (equivalently of $A$) over
the continuum of legal responses is attained at a pinned/tied vertex."
Here the reference is $\{b\}$ (plus the untouched ladder skeleton) and the
continuum is $T'$. This sidesteps the sign problem entirely — it doesn't
decompose $A(B)$ into a lower bound minus an upper bound at all, it
directly characterizes the minimizer of the *whole* quantity $A(B)$ as a
finite, evaluable vertex family via `odd-run-reduction-lemma`, the same
program already used successfully for Claim A's Case I closure
(`exchange-smoothing-vertex-maximization`, `case-i-closure-theorem`) and
for the interior-cross-tie family (`interior-cross-tie-evaluation-
formula`). **This is the most promising and lowest-new-machinery route**:
no new lemma needs to be invented, only the existing vertex/tie-evaluation
program needs to be pointed at $B=\{b\}\cup T'$ specifically and its
finite vertex family enumerated/bounded for this exact reference set.
This has not yet been attempted for this specific branch (round 22's
`insert-element-identity` diagnosis stopped at "one-sided bounds don't
work," it did not try the vertex-exchange route on $B$ itself).

**(b) Cheap first pass: `max-domination-lemma`** ($A(S)\le\max(S)$,
fully general, IH-free, certified round 13) gives $A(T')\le\max(T')\le
p_4$ instantly (cutting only ever produces pieces $\le p_4$). Plugged into
the Insert-Element Identity: $A(B)\ge2A(T'_{>b})-p_4+(-1)^jb$. This alone
is too crude (as the file's own diagnosis anticipates: it only helps when
$j$ is even and $b$ large), but it is a genuinely different, never-yet-
applied-here tool (it currently lives only in the sibling
`lp-duality-certificate` approach's upper-bound-on-$c(n)$ work, never
imported into `greedy-halving-adversary`'s Case (b) machinery) and costs
nothing to try combined with a matching *lower* bound on $A(T'_{>b})$ —
e.g. via `truncated-alternating-sum-floor` or a rescaled $(\star_{n-4})$-
type argument on $T'_{>b}$ if it can be shown to itself contain a
recognizable sub-ladder structure (worth checking: is $T'_{>b}$ always a
prefix of the ladder $\{p_4,\dots\}$ when $T'$'s cuts are all "below" $b$?
if so it may inherit ladder structure directly, unlike the fully general
Insert-Element setting).

**(c) Attack the joint quantity via the crux corpus's "geometric/dyadic
domination" pattern.** The `games-and-strategy` subtopic crux "Assign the
played values as a two-sided geometric (dyadic) sequence so that the
single largest value strictly exceeds the sum of all others" is the same
idea already embedded in `general-ladder-dominance`/ladder doubling — not
new content, but it suggests checking whether $B=\{b\}\cup T'$, viewed
*as its own multiset* (forgetting which piece is which), can be shown to
satisfy a **sum-dominance** property relative to $f(n)$ directly (i.e.
$b>\mathrm{Total}(T')-f(n)$ or similar), which combined with
`max-domination-lemma`-style regrouping might give $A(B)\ge f(n)$ as a
direct mass inequality rather than a rank-by-rank one — worth a quick
numeric check across the round-22 witness values before investing proof
effort, since if it's false at even one sampled configuration this route
dies immediately and cheaply.

## 5. Recommendation for next round's dispatch

Prioritize (a) — pointing the certified vertex-minimum-theorem /
odd-run-reduction machinery directly at $B=\{b\}\cup T'$ — as the
structurally cleanest route, since it reuses machinery already proved
general and correct elsewhere in this project and explicitly avoids the
one-sided-bound trap the Insert-Element Identity rules out. Run (b) as a
cheap parallel sanity check (it may fail fast, which is still useful
information). Separately, dispatch a **lightweight audit** (not a new
proof) of whether Theorems 33/34/35/36 jointly and exhaustively establish
$(\star_3)$ and $(\star_4)$ unconditionally — if so, several existing
"conditional" results upgrade for free at $n=5,6$, though this does not
touch the "$v\ge a$" branch's actual content and does not scale to general
$n$.
