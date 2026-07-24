# Lemma: Case (b2)'s box at $n=3$ is covered by the 5-chamber family (exact, non-numeric)

**Source:** `approaches/lp-duality-certificate.md`, round 25, §R25.1. A
round-26 attempt to drop the $p_1<1/2$ restriction was made and then
**REFUTED by the round-26 proof-reviewer** (see the "Round-26 correction"
note at the end of this file) — the $p_1<T/2$ restriction stands, restored.
Do not cite a $p_1\ge T/2$-inclusive version of this lemma.

**Statement.** Normalize $T=p_1+p_2+p_3+p_4=1$. For every
$(p_1,p_2,p_3)$ with $p_1\ge p_2\ge p_3\ge p_4=1-p_1-p_2-p_3>0$,
$p_1<1/2$, **and** $1/15<p_2<4/15$ (case (b2)'s box at $n=3$), at least one
of the five chambers
$$\{\mathrm{Bisect}\{1,4\},\ \mathrm{Bisect}\{1,2\},\ \mathrm{DS\text{-}Above},\
\mathrm{Triple\text{-}Pin},\ \mathrm{R22.1.1}\}$$
is simultaneously feasible and successful ($\Phi_\tau(p)\le\tfrac8{15}$).
Consequently $\Phi_{\min}(p)\le\tfrac8{15}T$ throughout this box.

**Proof.** Exhaustive 6-branch case split on (i) whether DS-Above/Triple-Pin
are feasible ($X$: $p_1\le p_2+p_3$ / $Y$: $p_1>p_2+p_3$, and if $Y$, both
of their own success inequalities fail) and (ii) which of R22.1.1's
feasibility/success conditions fails ($P1$: $p_1<2p_3$; $P2$:
$p_2>p_3+p_4$; $Q$: feasible but $g_{R22}<0$). Each of the 6 branches
$(X,P1),(X,P2),(X,Q),(Y,P1),(Y,P2),(Y,Q)$ is shown infeasible by an
explicit nonnegative rational combination of a small subset of its
defining (linear) inequalities collapsing term-by-term to the manifestly
false strict inequality $0<0$ — a standard Farkas-style infeasibility
certificate. See the approach file for the six certificates in full.

**Independent verification (this reviewer, round 25).**
1. Re-derived all five chambers' closed forms and re-verified, by exact
   `sympy.Rational` symbolic algebra, that all five stated
   failure/feasibility inequalities ($g_{14}<0$, $g_{12}<0$, DSA/TP
   feasibility, $g_{\mathrm{DSA}}<0$, $g_{\mathrm{TP}}<0$, R22.1.1
   feasibility, $g_{R22}<0$) are correct algebraic consequences of the
   chambers' $\Phi_\tau$ formulas at $a_3=8/15$.
2. Re-verified all six Farkas certificates symbolically from scratch
   (`/tmp/round-25/verify_farkas.py`): each combination's left-hand sides
   cancel to exactly $0$ and right-hand sides sum to exactly $0$, with at
   least one strict inequality receiving positive weight in each — all
   six confirmed to certify infeasibility correctly.
3. Independent random-sampling cross-check
   (`/tmp/round-25/verify_coverage2.py`): $23{,}880$ freshly-generated
   exact-`Fraction` random points inside the open box, zero points where
   all five chambers fail — corroborating (not substituting for) the
   exact proof.
4. Independently checked the boundary-vertex disposal claim: at
   $p^\ast=(2/5,4/15,1/5,2/15)$ (on the box's own excluded wall
   $p_2=4/15$), R22.1.1 is feasible and $g_{R22}(p^\ast)=0$ exactly —
   confirmed by direct substitution.

**Status.** Proved in full, exact rational arithmetic, no numeric margin,
no gap found. This lemma covers **only case (b2)'s own box** at $n=3$ —
see the reviewer's scope warning below for what it does **not** establish.

**Scope warning (important — added by reviewer, do not drop when citing).**
The approach file's own concluding claim ("this completes the general
upper bound $c(3)\le8/15$ for every legal Liu Bang marking at $n=3$...
Status upgraded to solved for the $n=3$ scope") is **not** established by
this lemma plus the cited "case (a)"/"case (b1)" regimes as written: the
approach file's final combination cites "case (a) ($p_1\ge T/2$)" and
"case (b1) ($p_2\le T/D_3$)," but a genuinely distinct fourth region —
"case (a)" in the file's own earlier, internally-inconsistent usage
(§ near line 100 and lines 2420-2431 of the approach file): $p_2\ge
a_3T/2$ *with* $p_1<T/2$ — is neither cited nor re-verified in the final
combination. This reviewer confirmed by direct random search
(500,000 trials) that the 5-chamber family here does **not** cover this
region on its own (many violations found, e.g. near
$(0.45,0.30,0.15,0.10)$) — it genuinely needs the separate
`generalized-peel-identity` (Theorem B$_k$, $k=2$) mechanism, conditional
on the already-fully-closed $c(2)=4/7$ bound, which *does* mathematically
cover it (reviewer spot-checked this independently) but was not actually
assembled/cited in the approach file's round-25 conclusion. Do not treat
"n=3's general upper bound is fully solved" as established until this
citation gap is fixed explicitly.

**Certified by:** proof-reviewer, round 25 (the covering closure itself,
scoped to case (b2)'s box only — not the broader "n=3 fully solved" claim).

**Round-26 correction (generalization attempted and REFUTED — restriction restored).**
This round's builder attempted to drop the $p_1<1/2$ restriction, arguing
the six Farkas certificates never explicitly reference $p_1$ vs. $T/2$.
**The round-26 proof-reviewer found this false**: the Triple-Pin chamber's
closed form $\Phi_\tau=T-p_1$ is derived under an ordering assumption
($v_3<p_4$) that is only guaranteed by $p_1<T/2$ (see the approach file's
own §R24.3 derivation, which explicitly invokes $p_1<T/2$ to pin this
order); for $p_1\ge T/2$ the ordering can flip and the chamber's stated
formula/success condition no longer applies as derived. The reviewer
exhibited a concrete counterexample: $p=(3/5,\,9/40,\,29/200,\,3/100)$
(so $p_1=0.6\ge1/2$, $p_2=0.225\in(1/15,4/15)$) at which **all five
chambers are either infeasible or fail** ($\Phi_\tau>8/15$ or infeasible
for each of Bisect{1,4}, Bisect{1,2}, DS-Above, Triple-Pin, R22.1.1),
confirmed by direct exact-`Fraction` computation. The builder's
"corroborating" random searches (`/tmp/round-26/check2.py`,
`/tmp/round-26/check3.py`) apparently did not sample this sub-region
densely enough to hit a violation — a reminder that non-exhaustive
sampling cannot substitute for the algebraic argument, which the reviewer
correctly re-examined and found wanting for exactly the chamber whose
derivation silently uses $p_1<T/2$. **The $p_1<T/2$ restriction is
restored** in the statement above; the sub-region $p_1\ge T/2$,
$T/15<p_2<4T/15$ (part of case (b2)'s box) remains **open** — it is
disjoint from "case (a)" as correctly redefined ($p_2\ge4T/15$) in the
round-26 approach-file section, so it is a genuine residual gap, not
covered by that section's Corollary either. No change to the
six certificates themselves.
