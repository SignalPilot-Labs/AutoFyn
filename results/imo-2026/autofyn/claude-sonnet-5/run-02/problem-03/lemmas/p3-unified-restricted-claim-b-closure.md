## Statement

For the $3$-ladder specifically, restricted Claim (B) at $\ell(F)\le2$
(Theorem $P(n)$ of `greedy-halving-adversary.md`, restricted to $n=3$) is
completely, unconditionally true: for every legal $F$ (Xiang Yu's split of
$p_1$, $\ell(F)\le2$) and every legal $G'$ refining the tail
$\{p_2,p_3,p_4\}$ with the remaining budget, $A(F\cup G')\ge f(3)=1/15$.

## Proof

See `results/imo-2026-03/approaches/greedy-halving-adversary.md`, "Base
case, precisely" (end of the Theorem $P(n)$ write-up, round 11). At $n=3$:
the $\ell(F)=0$ branch and $\ell(F)=1$'s closed sub-branches need only
$L(2)$/$L(1)$, both already fully certified (`n2-upper-bound-lp-argument`
and its lower-bound counterpart); the remaining nominally-open
$\ell(F)=1$ sub-branches ($v<s$, $w'<p_3$, $p_3$ cut, the $\ell(F)=1$-cut-$p_2$
complement) all require a further-refined sub-tail of size $\ge2$ below
$p_3$, which does not exist at $n=3$ (the tail below $p_3$ is just
$\{p_4\}$, a single piece with no further refinement structure to trigger
these sub-branches) — so they are vacuous at $n=3$.

## Certification note

**CERTIFIED, WITH A CORRECTION — proof-reviewer, round 11.** The overall
$P(3)$ conclusion is correct and independently reverified by the reviewer
with a fresh 200,000-trial continuum random search over every legal
$(F,G')$ pair with $\ell(F)\le2$ at $n=3$ (float-precision, not the
builder's own script): the minimum $A(F\cup G')$ found is $\approx0.06698$,
consistent with (and never below) the target $f(3)=1/15\approx0.06667$,
with no violations across ~100,000 qualifying trials
(`/tmp/round-11/p3_check.py`).

**However, the approach file's framing of one of $P(3)$'s cited branches —
"$\ell(F)=2$ sub-case (a): both residuals $\ge p_2$" — is corrected here.**
The reviewer found by direct algebra that sub-case (a) is **vacuous for
the ladder**, not merely "closed": since $p_1=2p_2$ exactly (the ladder's
own doubling identity, `general-ladder-dominance`) and $\mathrm{Total}(F)=
p_1$ with $P$ contributing $\ge0$, requiring both $v_1,v_2\ge p_2$ forces
$v_1+v_2\ge2p_2=p_1\ge v_1+v_2$, i.e. equality throughout, which forces
$v_1=v_2=p_2$ — contradicting $v_1>v_2$ (the defining condition for
$\ell(F)=2$; if $v_1=v_2$ the configuration actually has $\ell(F)=0$, not
$2$). Hence **no legal ladder configuration ever falls into sub-case (a)**;
its "closure" is a vacuously-true implication (an if-then with an
unsatisfiable hypothesis), not substantive new content, and it does *not*
constitute "a genuinely new closed sub-case, same depth as $\ell(F)=0$, no
new dependency" as the approach file's round-11 header describes it. This
does not affect $P(3)$'s truth (a vacuous branch trivially holds), but the
approach file's characterization of sub-case (a) as meaningful progress is
an overclaim that should be corrected in the next round's write-up — see
review for detail. **Certifying $P(3)$'s overall conclusion (fully checked
and independently reverified), while explicitly NOT certifying "sub-case
(a)" as a standalone reusable/meaningful lemma** — it is a vacuous
tautology specific to the ladder's doubling ratio, not a generalizable
fact.
