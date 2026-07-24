# Outline review — round 31 — imo-2026-03

Reviewed `/tmp/round-31/proof-outliner.md` (3 "revise"/"advance" outlines, no new
slugs proposed) against the live approach files and `current.md`'s round-30
status. All independent checks below were done with fresh exact-`Fraction`
Python, not by re-running any builder/outliner script.

## rank-pigeonhole-budget — verdict: CHANGES REQUESTED (approved to build)

Target sub-item: close $(\star_3)=\mathrm{MinFloor}(4)$'s last two shapes,
$(2,1,0,0)$ and $(1,2,0,0)$, of the 6-shape exhaustion.

**Focus check 1 — the "flat-equality identity for two simultaneously-split
parents."** Verified directly. On the equality face $d=0$ (so $c=4$), with
the claimed sorted order $f_1>c{=}4>f_2>\pi_3{=}2>f_3>\pi_4{=}1>0$, the full
7-element multiset is $\{f_1,f_2,f_3,4,0,2,1\}$. The alternating sum with
this sort order is
$$A(U)=f_1-4+f_2-2+f_3-1+0=f_1+f_2+f_3-7=8-7=1$$
(using $f_1+f_2+f_3=8$, the fixed total of $\pi_1$'s split). This is exactly
what the outline claims, and it is correct **for any** $(f_1,f_2,f_3)$
respecting that one fixed sort order — it is nothing more than the standard
sequential-peel identity (`peel-decomposition-identity`) applied along a
fixed rank pattern, so citing it as a mechanism is legitimate, not hand-wavy.
The outline is properly hedged: it states this only as verified on the
$d=0$ face and explicitly frames the general-$d$ extension as an "if this
generalizes..." hypothesis to test, not an asserted fact — no overclaim here.

**Focus check 2 — is $c\ge4-f_3$ smuggled in?** Confirmed this is a genuine
extra constraint, not implied by the two splits' own local orderings. Given
$f_1\ge f_2\ge f_3\ge0$, $\sum=8$ and $c\ge d\ge0$, $c+d=4$ (so $c\in[2,4]$),
there is no algebraic relation forcing $c\ge4-f_3$ (equivalently $d\le f_3$):
e.g. $c=2,d=2$ together with $f_3=0.1<c$ satisfies every "local" hypothesis
of the sub-case ($f_1\ge c,f_2\ge c,f_3<c$) yet violates $c\ge4-f_3$ (since
$4-f_3=3.9>2=c$). So both $c\ge4-f_3$ and its negation are realizable inside
the stated sub-case, confirming the outline is right to require it be
introduced as an **explicit hypothesis / extra case split**, not folded
silently into the derivation — exactly the discipline the round's own
"caught and fixed a spurious near-violation" note describes. No smuggling
found; the outline's Step 4 instruction is the correct fix.

The rest of the outline (vertex-enumeration via dualized
`exchange-smoothing-vertex-maximization` + `vertex-minimum-theorem`,
evaluation via `odd-run-reduction-lemma`) reuses only already-certified
tools correctly, and the open branch (the complementary $f_1<c$ branch) is
honestly flagged as untouched. **Sound, no fatal gap** — CHANGES REQUESTED
only in the trivial sense that real work (the full vertex enumeration) is
still to be done; nothing here should be sent back to rethink.

## greedy-halving-adversary — verdict: APPROVE (sound plan to build)

Target sub-item: $h(m)$'s "simultaneous $q_1$-cut and tail-refinement" piece,
5 vertex types, closing $c=q_1-x,c=q_1$ via a new $h(m-1)$-as-IH mechanism,
citing MaxCeil$(m)$ for $c=x$, and leaving $c=t\in S''$ open.

**Focus check — is "$c=x$ vertex $\equiv$ MaxCeil($m$)" a real identity, not
a numeric coincidence?** Traced both definitions directly in the files.
`rank-pigeonhole-budget`'s MaxCeil$(\ell)$ (§7.10–7.13) is: for a length-$\ell$
ratio-2 tail with top $\sigma_1$ and bottom $\sigma_\ell$, and **every** legal
$\le(\ell-2)$-cut refinement $S$ (any distribution of cuts, not restricted to
touching $\sigma_1$), $A(S)\le\sigma_1-\sigma_\ell$ — and this has been
**fully proved** (both the top-untouched branch via the Index-Chain Identity
to $(\star_{\ell-2})$, and the top-cut branch by hand) for $\ell\le4$.
`greedy-halving-adversary`'s $c=x$ vertex needs exactly $A(S'')\le q_2-f(m)$
for $S''$ a legal $\le(m-2)$-cut refinement of the length-$m$ tail
$\{q_2,\dots,q_{m+1}\}$ (top $q_2$, bottom $f(m)$). Matching $\ell=m$,
$\sigma_1=q_2$, $\sigma_\ell=f(m)$, budget $\ell-2=m-2$: this is **literally
the same statement**, term for term, not merely numerically similar. The
outline's numeric spot-check (tail max $=q_2-f(m)=2^{m-1}-1$ in $f(m)=1$
units, $m=3,\dots,6$) is corroborating evidence layered on top of a genuine
identity, not a substitute for one. So citing MaxCeil$(m)$ (certified for
$m\le4$, open for $m\ge5$ per rank-pigeonhole-budget's own Necessity
Theorem) to close $c=x$ for $m\le4$ and correctly leave $m\ge5$ open is
legitimate — this is real, useful cross-approach leverage, not a citation of
convenience.

The $h(m-1)$-as-IH mechanism (Step 3) for $c=q_1-x,c=q_1$ is a genuinely new
induction variable (on $m$ itself via the certified scaling Lemma 9/Theorem
38 Claim II), distinct from the outer $(\star_{m'})$ induction — no circular
reuse spotted (it invokes $h(m-1)$, a strictly smaller instance, as
hypothesis). Step 5 ($c=t\in S''$) is honestly flagged as the one genuinely
new, unclosed vertex with only a candidate mechanism (Insert-Bound Corollary
+ punctured-tail MaxCeil variant), not asserted solved. **Sound outline, no
fatal flaw** — APPROVE to build.

## lp-duality-certificate — verdict: APPROVE (sound anchor, correctly scoped)

Target sub-item: characterize the near-worst point in the $n=4$ upper-bound
residual box $\mathcal R$ ($p_1<T/2$, $T/31<p_2<8T/31$) and begin a Farkas-
style covering case-split, anchored at $p=(16,8,4,3,2)/33$ via a new
"Untouched-Singleton Pin" instance of the certified Partition Chamber
Theorem (R30.1).

**Focus check — is the Untouched-Singleton-Pin/anchor-point claim sound?**
Recomputed from R30.1's general formula directly (not trusting the outline's
one-line restatement): partition $B_1=\{p_1,p_3,p_4,p_5\}$ (host $p_1$),
$B_2=\{p_2\}$ (untouched singleton). Feasibility: $p_1\ge p_3+p_4+p_5$
($16\ge9$ ✓). $\rho_1=p_1-p_3-p_4-p_5=16-4-3-2=7$. $Q=\{\rho_1,p_2\}=\{7,8\}$,
$A(Q)=8-7=1$ (sorted-descending alternating sum). $\Phi=(T+A(Q))/2=(33+1)/2=
17$. Cut count: $|B_1|-1=3\le4$, legal. Comparing to $a_4T=\frac{16}{31}\cdot
33=\frac{528}{31}$: $17-\frac{528}{31}=\frac{527-528}{31}=-\frac1{31}$, i.e.
$\Phi=17<a_4T$ — **the chamber does close this point**, exactly matching the
outline's numbers. This is a correct, direct 1-line specialization of the
already-proved general theorem (verified by hand, not just re-run code) —
legitimate, not new unproved content.

Second, I checked whether "smaller margin than round-30's witnesses" is a
real (not backwards) claim, since $\frac1{31}>\frac1{62}$ as raw numbers
(which would make this point *easier*, not *harder*, to cover). The correct
comparison is scale-invariant: normalize margin by $T$. Round-30 witnesses
(normalized $T=1$) have margin $\frac1{62}\approx0.0161$; this point
($T=33$) has margin $\frac{1/31}{33}=\frac1{1023}\approx0.00098$ — over 16x
*smaller* once normalized by total stick length. So the outline's claim that
this point is closer to the true boundary is correct; my first pass without
normalizing was the wrong comparison, not the outline.

The outline is explicit and honest that the full Farkas covering proof for
$\mathcal R$ is **not** attempted this round — only the anchor point is
closed and the boundary-strip locus characterized — consistent with the
project's round 24–26 lesson (don't let numeric-only coverage stand in for
a proof). **Sound, correctly scoped** — APPROVE to build, no fatal flaw, but
flag for the builder: keep treating "the 536/60-chamber family is
exhaustive over all legal strategies" as unproven throughout, per the
outline's own Step 4/Open-gaps note.

## Diversity note

The three fronts remain genuinely distinct mechanisms (discrete pigeonhole/
vertex enumeration on the lower-bound side; vertex-pinning + induction-on-$m$
on the lower-bound side via a different vertex family; LP-duality/chamber
covering on the upper-bound side) — no shared-gap plateau this round; two
target Claim B's residual lower-bound vertices from different angles and one
targets the general-$n$ upper bound, so this is not a single-framing risk.

## No new slugs / no branching this round

The outliner proposed no new approaches and no branch-copy this round (all
three entries are "revise"/"advance" of already-registered slugs), so no
`register_approach` or `copy_approach` calls were needed. Ranking updated via
`update_ranking` reflecting round-30's recorded outcomes (all three
"advanced," no dead-ends): rank-pigeonhole-budget and greedy-halving-adversary
compared as a draw (both delivered comparable rigorous unconditional partial
closures — 4/6 shapes vs. Vertex 5 in full), both ranked above
lp-duality-certificate (real progress, but a self-correction + two witness
closures rather than a full closure of any sub-target this round).

build set: rank-pigeonhole-budget, greedy-halving-adversary, lp-duality-certificate
