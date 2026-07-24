# Math-explorer report — round 22 — lens: the ε-bridge front (greedy-halving-adversary + rank-pigeonhole-budget)

## 1. Is the Theorem 35b fix genuinely one-line?

**Yes — confirmed by re-derivation, no other consequences found.**

Theorem 35b's proof (greedy-halving-adversary.md, lines ~4024–4048) derives,
via the standing induction hypothesis $(\star_{n-3})$ applied to
$T'/\lambda$ (a legal response to the unit $(n-3)$-ladder):
$$A(T')\ \ge\ \lambda\cdot f(n-3) = f(n)\cdot D_{n-3}\cdot f(n-3).$$
Since $f(m):=1/(2^{m+1}-1)$ and $D_{n-3}:=2^{n-2}-1$ is exactly the
denominator of $f(n-3)$ ($f(n-3)=1/D_{n-3}$), the product
$D_{n-3}\cdot f(n-3)=1$ **identically**, not $2^{n-3}$ as the file
currently states (the file's algebra error: it substitutes
$f(n-3)=2^{n-3}/D_{n-3}$, which is wrong — $f(n-3)$ has numerator $1$, not
$2^{n-3}$). So the correct conclusion is simply
$$A(T')\ \ge\ f(n)\cdot 1 = f(n),$$
with **no further factor**, established with *less* algebra than the file
currently uses (the "cross-level identity" invocation is unnecessary — the
fix is not just replacing $2^{n-3}$ by $1$ but *deleting a step*).

**Downstream check.** I grepped every citation of Theorem 35b's conclusion
in the file (lines 673, 4159, and the round-21 approaches-tried summary at
line 32). In **every** citing location the text already says explicitly
"the actually-needed weaker bound $A(T')\ge f(n)$" — i.e. no downstream
step anywhere in the file actually uses the false $\ge f(n)\cdot2^{n-3}$
strength; they all only ever needed $\ge f(n)$. I also checked Theorem 34's
own structurally-analogous cross-level-identity use (lines 3773–3780,
"one level up"): it correctly gets $s\cdot f(n-2)=f(n)$ exactly (no
extraneous $2^{n-2}$ factor), confirming the bug is local to Theorem 35b's
one instance and is not a systemic error in `tail-self-similarity` itself.

**Verdict: genuinely a one-line fix (in fact a one-line deletion), safe to
apply immediately, zero downstream consequences.** Recommend next round's
builder apply it as a trivial cleanup while working on something else in
the same file.

## 2. Is $(\star_{n-3})$ itself a real obstruction for Theorem 35a$'$'s sub-range 2?

**Not an obstruction in principle — it is the ordinary strong-induction
hypothesis of a level-by-level tower, and it is currently satisfiable for
small $n$ but genuinely unresolved for larger $n$ because the tower itself
is incomplete, not because of any circularity.**

Concretely, $(\star_{n-3})$ at level $n$ requires the **full** theorem
(all of Theorem 35: both Case (a) and Case (b), $\Diamond$ or ideally
$\Diamond'$) to already hold at level $n-3$:
- $n=3$: needs $(\star_0)$ — vacuous, trivially true.
- $n=4$: needs $(\star_1)$ — true unconditionally ($c(1)$ fully closed,
  round 1).
- $n=5$: needs $(\star_2)$ — true unconditionally ($c(2)$ fully closed,
  round 1–2).
- $n=6$: needs $(\star_3)$ — requires the **full** Theorem 35 at $n=3$,
  including Case (b) (vacuous at $n=3$, so fine) **and** Theorem 35b's own
  range $v\ge p_3$ **with the $\epsilon$-correction** (i.e. $(\Diamond')$,
  not just $(\Diamond)$) at $n=3$ — this is exactly the "step 4" item this
  round's dispatch left untouched, so $(\star_3)$ for the *true* target
  $(\Diamond')$ is **not yet established**, even though the weaker
  $(\Diamond)$-only version of level 3 is presumably fine.
- $n\ge8$ needs $(\star_5)$, which needs Case (b) at $n=5$ — **open**
  (Theorem 36 only reaches $n=4$; round-20's own note flags $n\ge5$ as
  needing the "reframe as a level-$(n-2)$ ladder response" induction route,
  not yet built).

So: **sub-range 2 cannot be "pushed to unconditional" by any local trick**
— it is inherently a statement about level $n-3$, and per the definition of
strong induction it should stay conditional on $(\star_{n-3})$ as a
*hypothesis available at that level*, discharged globally once the tower is
built floor-by-floor for all $n$. The actionable framing for next round is
**not** "eliminate $(\star_{n-3})$ from Theorem 35a$'$" but "complete the
tower rungs it depends on" — concretely: (a) finish the $\epsilon$-bridge
for Theorem 35b's own range $v\ge p_3$ (currently unexamined, "step 4"),
and (b) extend Theorem 36 (Case (b), $p_3$ cut) past $n=4$ using the
induction-tower route the round-20 note already sketches (reframe
$R'=\{a,b\}\cup T'$ as a legal response to a rescaled $(n-2)$-ladder one
level up, invoking $(\star_{n-2})$). Both (a) and (b) are pre-existing,
explicitly flagged open items — this exploration did not find any new
obstruction inside $(\star_{n-3})$ itself, only confirmed it is exactly as
strong as advertised (no hidden circularity, no missing base case for the
levels currently needed).

## 3. Central finding: rank-pigeonhole-budget's §7.6 general-$n$ gap and greedy-halving-adversary's Theorem 35b/36 open ranges are **the same target**, not two independent obstructions

This is the most important thing found this round, and it changes the
recommended next-step mechanism.

**Evidence of identification.** Both files study the identical quantity
$\Delta(n,v):=A(R')-2A(R'_{>v})$ for $R'$ a legal $\le(n-3)$-cut refinement
of $\{p_3,\dots,p_{n+1}\}$ (greedy-halving-adversary calls it $R'$, uses
$v$; rank-pigeonhole-budget calls it $\tau$, uses $v_2$ — same object, same
formula). `rank-pigeonhole-budget` §7 explicitly cites
`greedy-halving-adversary`'s **Theorem 33/34 by name** (line 660: "the
domain ... of Theorem 33/34's sub-case (b)") as the reduction that produces
its own target $(\sharp)/(\sharp')$, and §7.5.3 states outright that its
$n=3$ closure of $(\sharp')$ "establishes exactly the sufficient inequality
`greedy-halving-adversary`'s own file records as needed but 'not verified'
for the $\epsilon(v)=1$ case" — i.e. the two files' authors already know
$(\sharp')=(\Diamond')$ at $n=3$; this exploration confirms the
identification is not an $n=3$ coincidence but structural: rearranging
rank-pigeonhole-budget's $(\sharp')$,
$$\Delta(n,v_2)\le s-(v_1-v_2)-2v_2\epsilon(v_2),$$
using the identity $s-p_2=-f(n)$ (Lemma 24) at the hardest $v_1\to p_2^-$,
gives **exactly** $\Delta(n,v_2)\le v_2-f(n)-2v_2\epsilon(v_2)$ — this is
$(\Diamond')$ verbatim (greedy-halving-adversary line 3918, $(\Diamond')$'s
own definition), for every $n$, not just $n=3$. The $n=3$ "domain-bound
summing trick" ($v_1<p_2$, $v_2<p_3$, sum to $v_1+v_2<p_2+p_3$) is simply
this same substitution *specialized* to the case where $\Delta(n,v_2)$ is a
single closed-form constant (true only at $n=3$, where the cut budget
$n-3=0$ leaves zero freedom in $R'$) — it is not a technique that evades
vertex enumeration in general; it works at $n=3$ only because there is no
polytope to enumerate at all.

**Consequence.** §7.6's "cross-piece tie-vertex enumeration obstruction"
(rank-pigeonhole-budget's own exchange-smoothing attempt, lines 949–998)
is **not a separate, second obstruction** requiring new machinery — it is
the *same* open range as Theorem 35b's own $v\ge p_3$ branch and Theorem
36's Case (b) ($p_3$ cut) for $n\ge5$, attacked with a *different, weaker*
technique (direct vertex/exchange-smoothing enumeration of the joint
per-piece polytope) than the one that has actually been working on this
target (Theorem 35's route: Fact 1 alternating-sum-nonnegativity +
`truncated-alternating-sum-floor` + strong induction — an algebraic
*floor* bound that never needs to characterize or enumerate the vertex
maximizing $A(R')$). This explains *why* §7.6's attempt re-encountered the
project's oldest obstruction while Theorem 35a/35a$'$/35b succeeded on
formally the same object: vertex enumeration is the wrong tool for this
particular target; the induction-plus-alternating-sum-floor route sidesteps
it entirely by only ever needing a lower bound on $A(T')$, never an exact
value or a full case-enumeration of the maximizer.

**Recommended next-step mechanism (most promising, concrete):** do **not**
dispatch further effort at rank-pigeonhole-budget's §7.6 vertex-enumeration
route. Instead, close the shared target by finishing greedy-halving-
adversary's own two flagged-open pieces using its already-successful
technique:
1. **Theorem 35b's own range $v\ge p_3$, $\epsilon$-corrected.** Apply the
   Band-Parity Fact (already certified, round 21) to locate
   $\epsilon(v)$ on $[p_3,s)$ exactly as was done for Theorem 35a$'$'s
   sub-range 2 (where $\epsilon(v)=1$ throughout once $v>s'$) — likely a
   short, structurally similar argument to sub-range 2, since Theorem 35b
   already reduces to the single inequality $A(T')\ge f(n)$ and the
   $\epsilon$-correction only adds a $-2v\epsilon(v)$ term that a
   comparable slack analysis (as in sub-ranges 1–2) should absorb, given
   $A(T')\ge f(n)\cdot D_{n-3}f(n-3)$-style room once the bug fix (item 1
   above) is applied.
2. **Theorem 36 Case (b) for $n\ge5$**, via the induction-tower reframing
   already sketched in the round-20 note (view $R'=\{a,b\}\cup T'$ as a
   legal response to a rescaled $(n-2)$-ladder, invoking $(\star_{n-2})$)
   — this is a genuinely different, not-yet-attempted piece of work, but
   it reuses the same alternating-sum-floor toolbox rather than vertex
   enumeration.

If both close (even conditionally on the induction tower, per item 2
above), **rank-pigeonhole-budget's §7.6 closes as a free corollary via the
identification proved in this section** — no new mechanism specific to
the multi-piece polytope is needed. This should be flagged explicitly to
the outliner: the two approaches are not really "two fronts" any more on
this specific sub-target; they are the same target proved from two angles,
and the winning angle is greedy-halving-adversary's algebraic-floor route,
not rank-pigeonhole-budget's vertex-enumeration route.

## 4. Numerics

I did not build a fresh general-$n$ simulator this round (the existing
scripts already cited in both files — `/tmp/check_middle3.py`,
`/tmp/check_sharp_prime_n3.py`, `/tmp/round-20/check_case_b_n4.py` — already
give zero violations for $(\sharp)$/$(\sharp')$/$(\Diamond)$ at $n=3$–$7$
with the corrected $n-3$ cut cap, which is the numeric evidence base this
report leans on). Given the analytic identification in §3 above (which is
an exact algebraic substitution, not a numeric conjecture), further
simulation would only re-confirm what is already known numerically; the
higher-value use of a future round's numeric budget is a **targeted**
check of item 3's mechanism #1 (the $\epsilon$-corrected Theorem 35b) at
$n=4,5$ specifically, once that sub-proof is drafted — to catch the same
class of algebra slip (the false $2^{n-3}$ factor) before it is cited
further.

## Summary of distinct viable next-step mechanisms

1. **Trivial**: apply the Theorem 35b one-line fix (delete the false
   $2^{n-3}$ factor). Zero risk, unblocks nothing new by itself but removes
   a latent citation hazard.
2. **Main recommendation**: finish Theorem 35b's own range ($v\ge p_3$)
   for the true $(\Diamond')$ target via Band-Parity Fact, mirroring
   Theorem 35a$'$'s sub-range-2 argument. This is the single highest-value
   next step — it is both the last piece of Case (a)'s $\epsilon$-bridge
   *and*, per §3's identification, effectively also closes rank-pigeonhole-
   budget's §7.6 gap in the range it corresponds to.
3. Extend Theorem 36 (Case (b), $p_3$ cut) past $n=4$ via the induction-
   tower reframing (already sketched, not yet built) — larger, separate
   piece of work, needed regardless of the $\epsilon$-correction.
4. **Redirect, don't continue**: rank-pigeonhole-budget's §7.6 vertex/
   exchange-smoothing route should be deprioritized — it is attacking an
   already-identified-as-identical target with a technique that has
   already failed on it (re-encountering the project's central
   obstruction), while a sibling technique on the same target has been
   succeeding. Continuing §7.6 independently risks duplicated, wasted
   effort; instead its §7.5 machinery (Band-Parity-Fact-based $\epsilon$
   location) could be *imported into* Theorem 35b's own proof for
   mechanism #2 above, since §7.5 already worked out the $\epsilon$
   location pattern once (at $n=3$) and Theorem 35a$'$ reused it
   successfully at general $n$ for sub-range 2.
