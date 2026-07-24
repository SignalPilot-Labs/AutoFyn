# Negative Lemma: Recursive-Image-Escape Dead End (case (b2))

**Statement.** Fix $n\ge1$, $m=n+1$, a marking $p_1\ge\cdots\ge p_m>0$,
$T=\sum p_i$, with $p_1<T/2$ (in particular, any marking in case (b2),
§R13.3 of `lp-duality-certificate.md`: $p_1<T/2$, $T/D_n<p_2<a_nT/2$).
Apply one step of Theorem C′ (bisect $p_1$, tail $S'=\{p_2,\dots,p_m\}$,
$T'=T-p_1$) or Theorem B$_k$ (peel $p_1$ against $p_k$, tail
$S'=\{w_k\}\cup\{p_i:i\ne1,k\}$, $T'=T-2p_k$), producing an $(m-1)$-piece
instance $S'$ at level $n-1$. Suppose $S'$ is observed to satisfy case (a)
or case (b1) at level $n-1$ (i.e. $\Phi_{\min}(S';n-1)\le a_{n-1}T'$ is
established specifically via the case-(a)/(b1) mechanisms, not assumed as
an unrestricted induction hypothesis). **Then substituting this fact into
Theorem C′/B$_k$ supplies a sufficient condition for $\Phi_{\min}\le a_nT$
that is identical — the same exact, zero-slack threshold ($p_1\ge a_nT$ for
the bisect route, $p_k\ge a_nT/2$ for the peel route) — to the one already
derived in `bisect-containment-dead-end`/`peel-zero-slack-dead-end` from
the full (unrestricted) induction hypothesis. Consequently "the recursed
image lands in a solved case one level down" supplies literally zero
coverage of case (b2) beyond what those two already-certified dead-end
lemmas rule out, for every $n$.**

## Proof

**Step 1 (the substituted value is the same regardless of which case $S'$
satisfies).** Both Theorem C′'s and Theorem B$_k$'s recursive inequalities
($\Phi_{\min}\le p_1/2+\Phi_{\min}(S')$ resp. $\Phi_{\min}\le
p_k+\Phi_{\min}(S')$) use $\Phi_{\min}(S')$ only through whatever upper
bound on it is available. Case (a) at level $n-1$ (§R13.3, via Theorem
C′/B$_k$ applied one further level down, conditional on $P(n-2)$) and case
(b1) at level $n-1$ (via `unconditional-p2-threshold-closure`/
`bisect-top-k-lemma`, R13.2/R14.1, unconditional) are each *proofs that
$\Phi_{\min}(S')\le a_{n-1}T'$* — the identical numeric ceiling that a
literal, unrestricted appeal to "the full induction hypothesis $P(n-1)$"
already supplies (since $P(n-1)$, by definition, is exactly the statement
$\Phi_{\min}(S')\le a_{n-1}T'$ for *every* $(m-1)$-piece marking $S'$,
established piecewise via cases (a), (b1), and — where still open — case
(b2) itself one level down). Knowing *which* case $S'$ falls into changes
*how* the bound $a_{n-1}T'$ was proved, not *what* the bound's numeric
value is. Hence substituting "$S'$ is in case (a) or (b1)" into Theorem
C′/B$_k$ produces exactly the same inequality, in $p_1$ (resp. $p_k$), that
`bisect-containment-dead-end`/`peel-zero-slack-dead-end` already solved —
with the identical zero-slack threshold $p_1\ge a_nT$ (resp. $p_k\ge
a_nT/2$) derived there via the Telescoping Threshold Lemma (§2 of the
approach file).

**Step 2 (case (a)'s own ceiling is genuinely tight — no room to
substitute anything sharper).** The claim in Step 1 would fail to be a
dead end only if "$S'$ is in case (a)/(b1)" always licensed a bound
*strictly below* $a_{n-1}T'$ — i.e. if the ceiling $a_{n-1}T'$ were merely
a loose, improvable upper estimate whenever it arises from case (a)/(b1)
specifically. This is false: the ceiling is *attained with equality* by
genuine markings inside case (a)/(b1), at every level of the induction, by
construction of the induction itself:
- **Base case** ($m'=2$, i.e. level $0$ of the recursion into $P(2)$):
  $P(2)$ is fully closed, both directions (§3 of the approach file, no
  gap): for $p_1'\in[T'/2,a_1T']$, Theorem A gives $\Phi=p_1'$ **exactly**
  (not just an upper bound — with only $2$ pieces, no strategy improves on
  this, as the base case is fully closed both directions). At
  $p_1'=a_1T'$ specifically, $\Phi_{\min}=a_1T'$ exactly — a genuine
  equality case inside case (a) at the very first level.
- **Inductive step.** The Corollary "Theorem C′'s threshold, general $n$"
  (§2 of the approach file) explicitly computes, for every $n\ge1$: with
  $p_1=a_nT$ and the tail bound substituted at its ceiling $a_{n-1}T'$,
  $$\Phi_{\min}\le a_{n-1}T+a_nT(\tfrac12-a_{n-1}) = a_nT,$$
  "with the bound tight (zero slack) at $p_1=a_nT$" — i.e. the derivation
  itself shows the substituted-ceiling computation reaches $a_nT$ exactly,
  not with room to spare, whenever the tail's own bound $a_{n-1}T'$ is
  itself tight. Combined with the base case above (where the tail's ceiling
  bound $a_1T'$ is exact, not merely an upper estimate), induction on $n$
  shows: at every level, there is a genuine marking realizing case (a)
  (via the ladder of exact Theorem-A equalities descending through the
  recursion) for which $\Phi_{\min}$ equals the substituted ceiling exactly.
  Hence "case (a) holds for $S'$" can never be strengthened, in general, to
  "$\Phi_{\min}(S')<a_{n-1}T'$" — some case-(a) instances genuinely need the
  full ceiling value.

**Step 3 (conclusion).** Since (i) the value substituted into Theorem
C′/B$_k$ from "$S'$ lands in case (a)/(b1)" is exactly $a_{n-1}T'$ (Step 1),
and (ii) this ceiling cannot be improved upon merely from case membership,
since it is tight for genuine instances at every level (Step 2), the
resulting sufficient condition on the top-level marking is *exactly*
`bisect-containment-dead-end`'s threshold $p_1\ge a_nT$ (bisect route) or
`peel-zero-slack-dead-end`'s threshold $p_k\ge a_nT/2$ (peel route, $k=2$
case; the identical algebra transfers verbatim for $k\ge3$ via Theorem
B$_k$, since — as already noted in §R13.3 — the Corollary's derivation
never used $k=2$ specifically). Both thresholds are already proved (in the
cited lemmas) to be disjoint from case (b2) ($p_1<T/2<a_nT$ for the bisect
route; $p_2<a_nT/2$ by case (b2)'s own definition for the peel route, and
the $k\ge3$ generalization only *weakens* the threshold's reach since
$p_k\le p_2$ for $k\ge2$, so $p_k\ge a_nT/2$ is a *stronger* requirement on
a *smaller* value, never easier to satisfy inside case (b2)). Hence "the
recursed image escapes to a solved case one level down" supplies **zero**
coverage of case (b2), for any $n\ge1$ and any choice of peel/bisect
target $k$. $\blacksquare$

## What this does *not* rule out

This lemma applies only to the specific mechanism "case membership alone,
substituted as a ceiling." It does **not** rule out a genuinely different
recursive quantity — e.g. tracking the *exact* value $\Phi_{\min}(S')$
(not its case-membership ceiling) as a function of the *specific* joint
values $(p_1,p_2,p_3,T)$ that a case-(b2) top-level marking's recursion
produces, which is a strictly finer question already known (§5,
"$p_1<T/2$ regime at $n=3$," and the round 13-15 build sections of the
approach file) to resolve individual witnesses but not, so far, in closed
form for a general marking. That different, harder question remains open;
this lemma only closes off the specific "ceiling substitution via case
membership" shortcut.

## Certification note

Proved directly from already-certified facts (`peel-zero-slack-dead-end`,
`bisect-containment-dead-end`, the Telescoping Threshold Lemma, and the
tightness of Theorem A/`n2-upper-bound-lp-argument` at the case-(a)
boundary, all already in `lemmas/` or the approach file's certified
sections) — no new computational machinery, a pure algebraic reconciliation
answering the round-16 outline-reviewer's mandatory gate question before
any numeric diagnostic was to be run.

**Origin:** `results/imo-2026-03/approaches/lp-duality-certificate.md`,
round 16, Task 2 (the mandatory reconciliation step required by the
round-16 outline-reviewer before the "recursive-image escape" numeric
diagnostic).
