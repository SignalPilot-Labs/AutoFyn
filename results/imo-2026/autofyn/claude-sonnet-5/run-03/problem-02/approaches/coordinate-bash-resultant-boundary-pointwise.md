## Status
partial

## Approaches tried

### Round 11 (this round) — Hessian check dispatched as first step of the
degenerate-limit/width-Taylor plan for `(\star)`: check performed, refutes
the outline's "interior PSD critical point" premise (gradient nonzero at
the corner, which is in fact an unconstrained local MAXIMUM), and
identifies the corner as a domain-boundary CUSP instead — the Case-(b)
sub-region of `(A,B)` is empty for `A\le A^*` and only opens up for
`A>A^*` (new, verified finding), plus a striking unproved 40-digit exact-
root coincidence between the domain-threshold equation and the already-
certified `G_{\mathrm{curve}}(A^*)=0`. `(\star)` itself is NOT closed this
round — see the full Round 11 entry below for details, and Promotable
lemmas for the three reusable findings.

### Round 7 (this round) — testing transfer of the resultant-ratio-cancellation
trick to Lemma P1/P2's quartic; a structural unification and one genuinely
new (proved) lemma, plus one newly-identified sub-gap

**Dispatch task**: test whether this round's resultant-ratio-cancellation
trick (`math-explorer-sturmlens.md`, certified via
`lemmas/g2b-true-supplementary-parity.md`'s sibling result — the fact that
the unknown factor `Y:=2a(u^2-1)^2-b(u^2+1)^2` cancels in the ratio
`\mathrm{Res}(G_{2b},D_K)/\mathrm{Res}(G_{2b},D_N)`) transfers to close
Lemma P1/P2's "exactly one survivor" claim, currently numeric-only (552
samples, round 6).

**Step 0 (new structural fact, fully proved, not previously recorded in
this file or any certified lemma): Lemma P1's quartic `(Q)` IS
`G_{2a}\cdot G_{2b}` up to an explicit nonvanishing constant.** I built `(Q)`
directly from the vector definitions (`V_1=L-B,V_2=d(\beta),V_3=L-N,V_4=C-N`,
exactly as in Lemma P1) in a fresh `sympy` session and divided by `G_{2a}`
(the already-certified quadratic factor):
$$(Q)=\frac{-(b^2+cc^2)^2(u^2+1)}{16(u^2+1)^6}\cdot G_{2a}(s_2)\cdot G_{2b}(s_2),$$
with the quotient (after clearing the always-positive denominator) matching
`math-explorer-sturmlens.md`'s independently-displayed `G_{2b}` **term for
term** (I re-derived it completely independently, from the raw vector
definitions used in this file, not by copying sturmlens's or the sibling's
polynomial). This is a genuine, useful unification: **Lemma P1/P2's
"quartic with four joint conditions" is not merely analogous to the
sibling `coordinate-bash-resultant-boundary`'s `G_{2a}/G_{2b}` apparatus —
it is literally the same polynomial**, and moreover:
- Condition (4) (`\mathrm{cross}(d(\beta),L-B)<0`) is exactly the sibling's
  `L_1<0` test (Theorem 11.8), same numerator.
- Condition (2) (matched sign, `\mathrm{sign}(V_1\cdot V_2)=\mathrm{sign}
  (V_3\cdot V_4)`) is **exactly** the sibling's "true vs. supplementary"
  criterion `W(s_2):=\mathrm{dot}(BL,BK)\cdot\mathrm{dot}(NL,NC)>0` from
  `lemmas/g2b-true-supplementary-parity.md` — since `\mathrm{dot}(BL,BK)
  \propto t_1(V_1\cdot V_2)` and `\mathrm{dot}(NL,NC)=V_3\cdot V_4` exactly,
  and `t_1>0` doesn't affect sign, `W(s_2)\propto (V_1\cdot V_2)(V_3\cdot
  V_4)`, so `W(s_2)>0\iff` condition (2). Concretely `W\propto D_K\cdot D_N`
  (the sibling's already-defined affine numerators).
- Condition (3) (containment `L\in\triangle BNC`) is, on the `G_{2a}` branch,
  exactly what the already-certified `lemmas/magnitude-bound-and-sign-
  coincidence.md` (§12) fully closes together with condition (4).

**Consequence.** Lemma P1's "exactly one survivor among `(Q)`'s roots"
claim decomposes cleanly, along the `G_{2a}`/`G_{2b}` split, into exactly
the two sub-questions the sibling approach already has open or partially
open — **plus one genuinely new sub-question this round identifies**,
described next. This is not a new gap invented from nothing: it is a
precise, checked identification that the two approaches' remaining work is
the *same* algebra, not merely similarly-shaped.

**New Lemma (fully proved this round, not previously in any certified
file): on `G_{2a}`'s own two roots, `W(r_1)W(r_2)\le0` always — i.e.
`G_{2a}` ALSO splits into one "true" (matched-sign) root and one
"supplementary" root, mirroring `G_{2b}`'s already-certified parity
property.**

*Proof.* Independently computed, via `sympy.resultant` (fresh session,
`G_{2a}` and `D_K,D_N` built from the exact closed forms already certified
in `lemmas/cross-product-sign-selection-G2a.md` and
`lemmas/g2b-true-supplementary-parity.md`):
$$\mathrm{Res}_{s_2}(G_{2a},D_K)=(u^2+1)^3F_2\cdot Y,\qquad
\mathrm{Res}_{s_2}(G_{2a},D_N)=4u(b^2+cc^2)^2(u^2+1)\cdot Y,$$
where `Y=2a(u^2-1)^2-b(u^2+1)^2` is the same unknown-sign factor from the
sibling's `G_{2b}` work (confirmed by direct symbolic comparison — the
displayed cofactor of `Res(G_{2a},D_K)` expands to exactly `Y`). By the
standard quadratic-vs-linear resultant-value formula `\mathrm{Res}(f,g)=
\mathrm{lc}(f)\cdot g(r_1)g(r_2)` (`f=G_{2a}` quadratic, `g` linear),
$$D_K(r_1)D_K(r_2)=\frac{(u^2+1)^3F_2Y}{A_2},\qquad
D_N(r_1)D_N(r_2)=\frac{4u(b^2+cc^2)^2(u^2+1)Y}{A_2},$$
where `A_2` is `G_{2a}`'s leading coefficient. Hence
$$W(r_1)W(r_2)=D_K(r_1)D_K(r_2)\cdot D_N(r_1)D_N(r_2)
=\frac{4u(b^2+cc^2)^2(u^2+1)^4F_2\,Y^2}{A_2^2}.$$
Since `u>0`, `(b^2+cc^2)^2(u^2+1)^4\ge0`, `Y^2\ge0`, `A_2^2>0` (as `A_2\ne0`,
already certified `A_2<0` throughout the valid range), and `F_2<0`
(already certified, `lemmas/branch-crossing-locus-equals-angle-C.md` +
Lemma 11.6), the whole expression is `\le0`. So `W(r_1)W(r_2)\le0`: a real
product of two real numbers that is `\le0` forces the two values to have
opposite sign (or one to be exactly zero, a measure-zero degenerate case
consistent with the rest of the population's genericity conventions).
`\blacksquare`

**Why this matters — a previously-unrecognized gap, honestly flagged.**
Theorem 11.8 (`L_1<0`) and §12's magnitude bound (`lemmas/magnitude-bound-
and-sign-coincidence.md`) together pin down a UNIQUE root of `G_{2a}`
satisfying conditions (3) and (4) of Lemma P1. **Neither of these
certified results addresses condition (2)** (matched sign / "is this root
actually a solution of hypothesis 2's true, unsquared equation, or only of
the squaring artifact's supplementary alternative?"). The new lemma above
shows this is a real, nontrivial question for `G_{2a}` too (not just
`G_{2b}`) — `G_{2a}`'s two roots do NOT both satisfy condition (2); exactly
one does. **It has not, until this round, been verified that the
(3)-and-(4)-selected root is the SAME root as the (2)-selected ("true")
root.** If it is not — i.e. if the geometrically/containment-selected root
of `G_{2a}` turns out to be the "supplementary" one — then the entire
population's central genericity certificate (`T\in\langle G_{2a},
G_{3a}\rangle`, valid "on the branch `G_{2a}=G_{3a}=0`") would not actually
apply to the genuine geometric configuration at all, since a supplementary
root does not correspond to a valid hypothesis-2 solution. This is a
genuine, if previously implicit, correctness dependency of the *whole*
population's strongest result, now made explicit for the first time.

**Numerical resolution attempt (strong support, not a proof).** Extending
the check-script used for condition (4) alone, I tested, on 377 fresh
independent (triangle, `β`) samples (own script, not reusing round-6's
code), whether the `L_1<0` root of `G_{2a}` (with `s_2>0`) always has
`W>0`: **377/377 (100%)** — no exceptions. So the correlation the
population has implicitly relied on is empirically robust, but this round's
attempt to prove it symbolically via the natural extension of the
resultant-ratio technique **did not succeed**, and the reason is
structural, not a matter of more compute:

**Why the ratio-cancellation trick does not directly transfer to this
specific correlation (an honest, precise diagnosis).** The trick that
closed `D_K(r_1)D_K(r_2)`-vs-`D_N(r_1)D_N(r_2)` (and, this round, the
analogous `W(r_1)W(r_2)\le0` fact on `G_{2a}`) works because it compares
**products over both roots of a single test function pair** — a
"both-roots" quantity, computable via `\mathrm{Res}(G_{2a},f)/A_2 = f(r_1)
f(r_2)` for any single affine `f`, with no need to know which literal root
is which. But the correlation needed here — "the specific root with
`L_1<0` also has `W>0`" — is a **same-root** (not both-roots-product)
statement, and requires actually identifying which of the two abstract
roots is which, which resultants of this shape do not directly supply. I
attempted the natural next tool: reducing the degree-3 polynomial `L_1(s)
\cdot W(s)` modulo `G_{2a}(s)` (degree 2) to extract the symmetric sum
`S:=L_1(r_1)W(r_1)+L_1(r_2)W(r_2)` via the standard "polynomial remainder
= trace formula" (`f\equiv \alpha+\beta s\pmod{G_{2a}}\implies\sum_if(r_i)=
2\alpha+\beta(r_1+r_2)`). This IS computable (I did compute it, fully
symbolically) but the resulting closed form is a degree-20-in-`u` polynomial
in `a,b,cc` (over the denominator `2(u^2+1)^4(-2bu+cc\,u^2-cc)^3=2(u^2+1)^4
F_1^3\cdot(1+u^2)^{-3}`-type factor) that **does not factor into recognizable
pieces** (`sympy.factor` returns it as one irreducible block, confirmed by a
90-second computation) — even establishing this quantity's SIGN would
require a fresh sign-determination argument on a much higher-degree object
than anything else this population has closed by hand, and even then, `S`'s
sign alone (a symmetric same-index sum, mixing both roots) does **not**
directly resolve "is the specific `L_1<0` root's `W`-value positive," only a
combination of both roots' `L_1\cdot W` values — it would need to be
combined with the already-known individual products `L_1(r_1)L_1(r_2)<0`
and `W(r_1)W(r_2)\le0` via a further (nontrivial) algebraic elimination step
that was not completed this round. **This is reported as a genuine,
precisely-scoped negative finding**: the specific resultant-ratio trick
that worked for both-roots-product correlations does not, by itself, extend
to same-root correlations between two DIFFERENT test functions — a new
tool (e.g. an explicit closed-form for the individual roots via the
quadratic formula, with a careful sign analysis of the discriminant-times-
slope terms, as sketched but not completed) would be needed, and this is a
concrete, well-defined target for a future round, not a dead end.

**Net assessment for this round's dispatch question.** The
resultant-ratio-cancellation trick **partially transfers**: it produces one
genuinely new, fully proved lemma (`W(r_1)W(r_2)\le0` on `G_{2a}`, exactly
mirroring the certified `G_{2b}` template) and a valuable structural
unification (Lemma P1's quartic IS `G_{2a}G_{2b}`, and its four conditions
map exactly onto the sibling's already-defined test functions
`L_1,D_K,D_N`, and the §12 containment machinery). It does **not** close
the uniqueness-of-survivor claim, and in the process of testing it I
identified a genuinely new sub-gap (the `G_{2a}`-side same-root correlation
between conditions (2) and (3)-(4)) that had not been explicitly flagged by
any prior round of this population, despite being load-bearing for the
correctness of the population's single strongest certified result (the
genericity certificate). This sub-gap is reported honestly here, alongside
the pre-existing `G_{2b}` 3-way exclusion gap (which, per the structural
unification above, is now known to be the *same* algebraic object as the
`(Y,B_2,Z)` classification problem `coordinate-bash-resultant-boundary`
is separately attacking) — so this file's remaining work is now precisely:
(i) the `G_{2a}`-side same-root correlation (new this round, numeric-only,
377/377), and (ii) the `G_{2b}`-side full exclusion (pre-existing, shared
verbatim with the sibling approach's open `(Y,B_2,Z)` sign classification).

### Round 6 — pointwise (non-continuity) branch-selection architecture, tested at scale

This is a fork of `coordinate-bash-resultant-boundary` (registered via
`copy_approach`, per the outline-reviewer's round-6 note), sharing its
Steps 1–4 (reduction, rotation parametrization, symbolic genericity
certificate, Theorem 11.8/11.10 cross-product-sign selection) verbatim, but
committing to a **different closing architecture** for gap 2 (branch
selection): instead of the sibling's continuity/IVT plan (track which
branch is "genuine" as `β` varies, worrying about crossings of the shared
resultant factors `F_1,F_2,F_3,F_3'`), this approach tries to prove branch
selection **pointwise** — independently, at each fixed `β`, with no
reference to neighbouring `β` values at all — by testing every real
candidate root against the *full* hypothesis set at once. If this succeeds,
the sibling's still-open "does the genuine branch survive an `F_3=0`
crossing" question (§9 of the sibling, open since round 4) becomes
**irrelevant**, not merely resolved: there is no "tracking a branch across
`β`" step to disturb in the first place.

**What this round establishes, precisely, and what remains open.** I
formulated the pointwise criterion in a form that does **not** require the
`G_{2a}`/`G_{2b}` polynomial factorization at all (a cleaner formulation than
the outline's original "test all 4 candidate roots of `G_{2a}$ and `G_{2b}`"
plan — see Lemma P1/P2 below, which work directly with the *un-factored*
squared-cosine quartic). I **proved rigorously** the exact translation of
the problem's hypotheses into this pointwise criterion (Lemma P1, an
elementary but new-to-this-population equivalence). I then **tested the
resulting criterion at scale, numerically**: 273 independent random
(triangle, `β`) samples for hypothesis 2's side and 279 for hypothesis 3's
side (552 total, 0 failures) — every single sample has **exactly one**
surviving candidate. This is substantially more numerical evidence than
anything previously in the population for this specific claim (previous
best: 16 points across 4 triangles). **What is not established**: a
symbolic, all-triangle, all-`β` proof that exactly one candidate always
survives. I attempted to extend Theorem 11.8's resultant/Vieta machinery to
cover this (Lemma P1's three joint conditions, not just the cross-product
sign test alone), and identify precisely why it does not immediately
transfer (the "matched-sign" condition, needed to pick out the genuine,
non-supplementary root of the *true* unsquared angle equation, is not a
polynomial condition — it is a strict-inequality condition on which side of
zero a certain dot product sits, and combining it correctly with the
already-proved sign-test and the full triangle-containment inequality
requires a joint case analysis that was not completed this round). Status
stays `partial` — this is real, precisely-scoped progress (a cleaner
target claim, a proved reduction lemma, and a much larger numerical
corroboration) but not a closed proof.

## Current best

### 1–4. Imported verbatim from the sibling (certified)
Exactly as in `approaches/coordinate-bash-resultant-boundary.md` §§1–4 /
`lemmas/symbolic-genericity-certificate.md` / `lemmas/homogeneity-decoupling-rotation-param.md`:
with `A=(0,0)`, `B=(a,0)`, `C=(b,cc)` (`a,cc>0`, CCW),
$$K=B+t_1(-\cos\beta,\sin\beta),\qquad L=C+t_2\cdot R(\beta)\frac{A-C}{|AC|}
=C+s_2R(\beta)(A-C)\quad(s_2:=t_2/|AC|),$$
`β=∠KBA=∠ACL` (hypothesis 1) the free parameter, and the target identity
$$OM=ON\iff O\cdot(C-B)=\frac{|C|^2-|B|^2}{4}$$
holds identically **on the correctly-selected branch**, for every triangle
(the symbolic genericity certificate, proved by Gröbner-basis
ideal-membership `T\in\langle G_{2a},G_{3a}\rangle`, independently
re-verified three times by the population). By the certified
homogeneity-decoupling lemma, hypothesis 2's true (unsquared) equation
`∠LBK=∠LNC` depends on `(β,s_2)` only (not `t_1`), and hypothesis 3's on
`(β,t_1)` only (not `s_2`) — the two remaining constraints are genuinely
decoupled once `β` is fixed.

### 5. Imported: Theorem 11.8/11.10 (certified `lemmas/cross-product-sign-selection-G2a.md`)
For every triangle and every `β` in the valid range `(0,\min(\angle B,\angle
C))`: given `L\in\triangle BNC`, "`K` inside angle `LBA`" is equivalent to
`\mathrm{cross}(d(\beta),L-B)<0` (`d(\beta)=(-\cos\beta,\sin\beta)`, the
direction of ray `BK`); and among the (at most two) real roots of `G_{2a}`
(the degree-4-in-`u` branch cofactor of hypothesis 2's polynomial), exactly
one satisfies this sign condition. Symmetrically for `G_{3a}` and "`L`
inside angle `ACK`" via `σ`-symmetry.

### 6. New this round: a pointwise, factorization-free reformulation of branch selection

**Setup.** Fix a triangle and `β` in the valid range. Define, exactly as in
the standard "unsigned angle equality ⟺ equal cosines" device (used
throughout this population, e.g. `coordinate-bash.md` §5, equation (†)):
$$V_1=L-B,\ V_2=d(\beta),\qquad V_3=L-N,\ V_4=C-N,$$
so hypothesis 2's true equation `∠LBK=∠LNC` (an equality of two angles, each
in `(0,\pi)`, since each is an angle between two rays from a vertex) is
equivalent to `\cos\angle(V_1,V_2)=\cos\angle(V_3,V_4)`, i.e. (since
`\cos\angle(U,W)=\dfrac{U\cdot W}{|U||W|}` and `|U|,|W|>0`)
$$\frac{V_1\cdot V_2}{|V_1||V_2|}=\frac{V_3\cdot V_4}{|V_3||V_4|}. \tag{$\star$}$$

**Lemma P1 (exact translation of hypothesis 2 + containment + "K inside
angle LBA" into three explicit conditions on `s_2`, no polynomial
factorization needed).** Given `β` in the valid range, a value `s_2>0`
(equivalently the point `L=C+s_2R(\beta)(A-C)`) is **the** value making `K,
L$ satisfy hypothesis 2 (`∠LBK=∠LNC`) **and** `L\in\triangle BNC` **and**
"`K` inside angle `LBA`" simultaneously **if and only if** all three of the
following hold:
1. **(Squared equation.)** `s_2` is a real root of
   $$(V_1\cdot V_2)^2|V_3|^2|V_4|^2-(V_3\cdot V_4)^2|V_1|^2|V_2|^2=0,\tag{Q}$$
   a polynomial of degree `4` in `s_2` (with `V_1,V_3` affine-linear in
   `s_2` and `V_2,V_4` independent of `s_2`) — this is `(V_1\cdot
   V_2)^2|V_3|^2|V_4|^2=(V_3\cdot V_4)^2|V_1|^2|V_2|^2`, i.e. the squared
   form of `(\star)`.
2. **(Matched sign.)** `\mathrm{sign}(V_1\cdot V_2)=\mathrm{sign}(V_3\cdot
   V_4)$ (both nonzero).
3. **(Containment.)** `L=C+s_2R(\beta)(A-C)\in\triangle BNC` (strictly).
4. **(Angle test, by §5/Theorem 11.8's already-certified reduction, valid
   given (3)).** `\mathrm{cross}(d(\beta),L-B)<0`.

*Proof.* Condition (1) is exactly $(V_1\cdot V_2)^2/(|V_1|^2|V_2|^2) =
(V_3\cdot V_4)^2/(|V_3|^2|V_4|^2)$ after clearing the (positive) denominators
$|V_1|^2|V_2|^2|V_3|^2|V_4|^2$ — a purely algebraic rearrangement of
`(\star)^2`, valid since $|V_i|>0$ for every `i` (each `V_i` is a nonzero
vector: $V_2=d(\beta)\ne0$ always; $V_4=C-N=C/2\ne0$ since `C\ne A$;
$V_1=L-B\ne0,V_3=L-N\ne0$ because $L$ is a genuine point of the
configuration distinct from $B,N$, a standing non-degeneracy assumption
shared by the whole population). Condition (1) is thus *equivalent* to
$\cos^2\angle(V_1,V_2)=\cos^2\angle(V_3,V_4)$, i.e. (since both angles lie
in $(0,\pi)$, where $\cos$ is injective up to sign, specifically
$\cos\theta_1=\pm\cos\theta_2\iff\theta_1=\theta_2$ or $\theta_1=\pi-\theta_2$)
to "`∠(V_1,V_2)=∠(V_3,V_4)`" **or** "`∠(V_1,V_2)=\pi-∠(V_3,V_4)`". These two
alternatives are distinguished exactly by the sign of $\cos\angle(V_1,V_2)$
versus $\cos\angle(V_3,V_4)$, i.e. by $\mathrm{sign}(V_1\cdot V_2)$ versus
$\mathrm{sign}(V_3\cdot V_4)$ (since $|V_1||V_2|,|V_3||V_4|>0$): the first
alternative (the genuine hypothesis-2 equation) holds exactly when these
signs match — condition (2). So (1)∧(2) $\iff$ hypothesis 2's true equation
$\angle LBK=\angle LNC$ holds. Condition (3) is literally the containment
hypothesis `L\in\triangle BNC`. Condition (4), by the already-certified
Theorem 11.8/`lemmas/cross-product-sign-selection-G2a.md` reduction
(Lemmas 11.1–11.4 there, which only use `L\in\triangle BNC`, not that `L`
solves any particular quadratic), is equivalent, **given (3)**, to "`K`
inside angle `LBA`." Conjoining (1)–(4) is therefore exactly the conjunction
of hypothesis 2, the containment `L\in\triangle BNC`, and "`K` inside angle
`LBA`" — the three hypotheses of the problem statement that involve `L`
(other than hypothesis 1, already used to fix `β`). $\blacksquare$

**Lemma P2 (mirror statement for `t_1`, via `σ`-symmetry, certified
`lemmas/sigma-symmetry.md`).** Given `β` in the valid range, a value
`t_1>0` is the value making `K,L` satisfy hypothesis 3 (`∠LCK=∠BMK`), `K\in
\triangle BMC`, and "`L` inside angle `ACK`" simultaneously if and only if
the mirror conditions (1')–(4') hold, with `B\leftrightarrow C`,
`K\leftrightarrow L`, `M\leftrightarrow N`, `s_2\leftrightarrow t_1`: writing
`W_1=L-C$ (a fixed direction, `s_2`-independent, since only its polar angle
matters for the angle test at `C`; concretely one may take
`W_1:=R(\beta)(A-C)`, any positive multiple of `L-C`), `W_2=K-C`, `W_3=B-M`,
`W_4=K-M`:
1'. `(W_1\cdot W_2)^2|W_3|^2|W_4|^2=(W_3\cdot W_4)^2|W_1|^2|W_2|^2` (degree
`2` in `t_1`, since `W_2,W_4` are affine-linear in `t_1` and `W_1,W_3` are
`t_1`-independent).
2'. `\mathrm{sign}(W_1\cdot W_2)=\mathrm{sign}(W_3\cdot W_4)`.
3'. `K=B+t_1d(\beta)\in\triangle BMC` (strictly).
4'. `\mathrm{cross}(W_1,K-C)>0` (the mirror sign convention; see the
    numerical note below on why the sign flips relative to (4)).

*Proof.* Identical to Lemma P1's proof, with the stated substitutions,
using the certified `σ`-symmetry to carry the hypothesis-3/angle-`ACK`
statement and Theorem 11.10's reduction across. $\blacksquare$

**Remark on the sign convention in (4').** Unlike (4), which uses
`\mathrm{cross}(d(\beta),L-B)<0`, the mirror test uses `>0` — this is not an
error but a genuine consequence of `σ` reversing orientation at the level of
this specific cross product (verified directly: substituting `B\leftrightarrow
C` into a cross product introduces an extra sign flip beyond a plain
relabeling, because `\mathrm{cross}(-V,W)=-\mathrm{cross}(V,W)$ and the
`σ`-image of `d(\beta)` is `-W_1$-proportional up to the rotation
direction). This was confirmed both by direct symbolic substitution and
independently by the numerical experiment below (Table 2): the genuine root
always has `\mathrm{cross}(W_1,K-C)>0`, never `<0`, across every sample
tested.

### 7. Numerical corroboration at scale (this round)

**Method.** For each of 300 independently sampled triangles `(a,b,cc)`
(`a\in(0.3,4)`, `b\in(-2,4)`, `cc\in(0.2,3)`, uniformly, filtered to
`\min(\angle B,\angle C)>0.1` rad) and one random `β\in(0.03,0.97)\cdot
\min(\angle B,\angle C)`, computed **exactly** (own `sympy` session, not
reusing `G_{2a}/G_{2b}` from any prior round's file — built condition (1)/(1')
directly from the vector definitions above, so this is an independent
re-derivation, not a re-check of the sibling's polynomials) the degree-4
polynomial (Q) in `s_2` (resp. the degree-2-times-something polynomial in
`t_1`, after clearing the trivial factor structure — concretely the
quartic-in-`t_1` analogue of (Q) for hypothesis 3), extracted all real
roots via `numpy.roots` on the exact symbolic coefficients evaluated at the
numeric `(a,b,cc,\beta)`, and tested conditions (2)–(4) (resp. (2')–(4'))
directly on the exact coordinates (not via any resultant/sign-lemma
shortcut — a fully independent numerical check of Lemma P1/P2's criterion).

**Results.**
- **Hypothesis 2 side**: 273 valid trials (27 discarded for `\min(\angle
  B,\angle C)\le0.1` rad, an artificial filter to avoid near-degenerate
  triangles, not a geometric restriction), **273/273 (100%) had exactly one
  surviving `s_2`** satisfying (1)–(4). The number of real roots of (Q)
  itself varied between 2 and 4 across trials (both cases occurred
  frequently), confirming this really is testing the full candidate set
  (not merely `G_{2a}`'s own two roots) and still finding uniqueness.
- **Hypothesis 3 side**: 279 valid trials, **279/279 (100%) had exactly one
  surviving `t_1`** satisfying (1')–(4') (after correcting the sign
  convention in (4') as noted above — an initial run with the naive
  `B\leftrightarrow C` relabeling of (4)'s sign gave 0/25, immediately
  diagnosed and fixed by direct inspection of the genuine root's actual
  cross-product sign; this negative-then-corrected result is reported
  honestly, not hidden, since it is informative about the σ-symmetry's
  precise action on this specific test).

This is **552 independent (triangle, `β`) samples total, 0 counterexamples**,
substantially more than any prior numerical corroboration in this
population for the branch-selection question (previous best: 16 points,
4 triangles, in the sibling's §5). Since Lemma P1/P2 is an *exact* logical
translation of the problem's own hypotheses (proved above, not itself
numerical), this experiment is a direct large-scale numerical test of the
population's central open conjecture ("the genuine geometric configuration
is pointwise unique for each `β`, for every triangle") — not a test of some
proxy or simplification.

### 8. What remains open, precisely

**The claim "exactly one candidate survives (1)–(4) [resp. (1')–(4')], for
every triangle and every `β` in the valid range" is NOT proved
symbolically.** It is supported by 552 numerical samples with zero
exceptions (§7), which is meaningfully more evidence than the population had
before this round, but is not a proof, and this approach explicitly does
**not** claim `solved`.

**Why the natural extension of Theorem 11.8's technique does not
immediately close it.** Theorem 11.8 handled exactly one binary sign test
(`\mathrm{cross}(BK,BL)<0`) among the roots of a *single* known quadratic
factor (`G_{2a}`), via a clean resultant/Vieta trick: compute
`\mathrm{Res}_{s_2}(G_{2a},L_1)`, factor it, and pin the sign of the ratio
`L_1(r_1)L_1(r_2)=\mathrm{Res}/A_2`. This worked because both `G_{2a}` and
the sign-test numerator `L_1` are **polynomials**, so the classical
resultant formula applies directly. Lemma P1's criterion has three
independent components acting jointly on the roots of the *full* degree-4
polynomial (Q) (not the already-factored `G_{2a}` alone):
- Condition (1) is polynomial (fine, resultants apply).
- Condition (3) (triangle containment) is **itself** a conjunction of three
  affine sign tests (the standard three-signed-areas test) — tractable in
  principle by the same technique (each is affine-linear in `s_2`, exactly
  Lemma 11.5's shape), but now **three** simultaneous sign conditions rather
  than one, multiplying the casework.
- Condition (2) (matched sign) is a condition on `\mathrm{sign}(V_1\cdot
  V_2)` — but `V_1\cdot V_2` is **not** a factor of (Q) (only its *square*,
  combined with other squared terms, is); pinning the sign of an
  unfactored dot product across all four roots of a quartic, as opposed to
  the sign of a value at the roots of a *given* quadratic factor, is a
  structurally harder resultant/Sturm-sequence problem (a "count sign
  changes among the roots of a quartic" question, not a single Vieta
  product).
- The round-5-established fact that `G_{2b}`'s own leading coefficient
  `B_2` does **not** have fixed sign across triangles (see
  `coordinate-bash-resultant-boundary.md` §11 end) means that whatever
  argument closes this must genuinely use *all three* of (2)-(4) jointly on
  `G_{2b}`'s roots — no single one of them suffices alone (confirmed: a
  quick check of `B_2`'s sign alone, without conditions (2)/(3), would not
  correctly predict survivorship, since `B_2`'s sign varies while the
  numerics above show a survivor is picked out consistently regardless).

None of these is a proof that the extension is impossible — they are a
precise diagnosis of why it is harder than Theorem 11.8's case, i.e. exactly
what remains to be done, not a dead end.

**A note on what this approach's success would and would not retire.** If
the pointwise uniqueness claim (§6–§7) is eventually proved symbolically,
it would make the sibling's outstanding F3/F3' harmless-crossing question
(open since round 4) **moot rather than resolved**: this approach's target
claim never refers to `\beta`-continuity or resultant-zero crossings at
all — uniqueness is asserted and (if proved) would be proved independently
at each fixed `\beta`. It would **not**, by itself, establish the
population's separate standing conjecture that the unique survivor always
coincides with the `G_{2a}=G_{3a}=0$ branch specifically (the genericity
certificate's branch) — but since Lemma P1/P2's survivor is *by
construction* the actual geometric solution (not merely "on some named
branch"), and the genericity certificate is exactly the statement that the
target identity holds on `G_{2a}=G_{3a}=0`, closing this approach's gap
would still require one final (short) step: confirming the survivor found
by Lemma P1/P2 always lands on `G_{2a}=G_{3a}=0`, not `G_{2a}=G_{3b}=0` or
some other combination — which the §7 numerics are consistent with
(evaluating `G_{2a}` at the surviving `s_2` gave residuals `<10^{-13}` at
every one of a spot-check of 30 of the 273 hypothesis-2 samples, an
additional independent check performed this round) but which was not
re-verified at all 552 points nor proved symbolically.

### 9. Round 7 update to Current best

**New structural fact (proved, round 7):** Lemma P1's quartic `(Q)` equals
`-(b^2+cc^2)^2(u^2+1)/[16(u^2+1)^6]\cdot G_{2a}\cdot G_{2b}` exactly, so
Lemma P1's four joint conditions decompose exactly along the sibling
`coordinate-bash-resultant-boundary`'s already-defined `G_{2a}`/`G_{2b}`
split and test functions (`L_1`, `D_K`, `D_N`, and the §12 containment
apparatus). This is not merely an analogy — the two approaches' remaining
algebra is now known to be literally identical where it overlaps.

**New lemma (proved, round 7):** `W(r_1)W(r_2)\le0` on `G_{2a}`'s own two
roots (mirroring the already-certified `G_{2b}` parity fact) — see the
Round 7 entry above for the full resultant-based proof. This reveals a
previously-unflagged sub-gap even on the "closed" `G_{2a}` branch: whether
the root selected by Theorem 11.8 + §12 (conditions 3–4) coincides with the
"true equation" (matched-sign, condition 2) root of `G_{2a}` — strongly
supported numerically (377/377, fresh independent samples) but **not
proved**. The resultant-ratio-cancellation technique, while it produced
this new lemma, was shown (by a concrete, completed attempt — see above) to
NOT directly extend to prove this specific same-root correlation; a
different technique (e.g. explicit root formulas via the quadratic formula
with a discriminant-sign argument) is needed and is the concrete open item
for a future round.

**The two precise remaining gaps for this approach, after round 7:**
1. (New this round) `G_{2a}`-side: does the `L_1<0`, containment-satisfying
   root of `G_{2a}` always also satisfy the matched-sign condition
   `W>0`? Numeric only (377/377).
2. (Pre-existing, now known to be the identical algebraic object as
   `coordinate-bash-resultant-boundary`'s open `(Y,B_2,Z)` 3-way
   `G_{2b}`-exclusion problem) `G_{2b}`-side: full exclusion of any
   `s_2>0`, `W>0`, containment-and-angle-test-passing root.

Neither gap is closed this round; both are now more precisely scoped than
before, and gap 2 is confirmed (not just suspected) to be shared verbatim
with the sibling approach, so progress by either approach on it transfers
directly to the other.

### Round 8 — the complex-affine "two lines in ℂ" reframing, verified and
pushed: closes "which root" unconditionally, narrows the remaining gap

**Dispatch task**: close the `G_{2a}` same-root correlation (does the
`L_1<0`-selected root of `G_{2a}` also satisfy `W=D_KD_N>0`?) using the
complex-affine reframing `L_1=\mathrm{Im}(\bar d\cdot v(s_2))`,
`D_K=\mathrm{Re}(\bar d\cdot v(s_2))`.

**Step 0 (independently re-verified before building on it, own fresh
`sympy` session).** With `d(\beta)=(-\cos\beta,\sin\beta)` (complex number
`d=-\cos\beta+i\sin\beta`) and `v(s_2):=L(s_2)-B` (complex-affine in
`s_2`), computed `\mathrm{cross}(d,v)` and `\mathrm{dot}(d,v)` **directly
from the raw vector definitions** (not copying any prior file's polynomial)
and compared against the certified closed forms
(`lemmas/cross-product-sign-selection-G2a.md`'s `L_1=P(u)+s_2Q(u)` and
`lemmas/g2b-true-supplementary-parity.md`'s `D_K(s_2)`). Result: **exact
equality, not merely proportionality** —
$$\bar d\cdot v(s_2) \;=\; D_K(s_2) \;+\; i\,L_1(s_2)$$
identically (both numerators, after clearing the same positive denominator
`(1+u^2)^2`, match the certified `D_K,L_1` polynomials term-for-term,
`sympy` symbolic difference `0`). This is the precise, verified form of the
outline's reframing: `L_1,D_K` are literally the imaginary/real parts of
**one** complex-affine function `W_1(s_2):=\bar d\cdot v(s_2)` of the real
parameter `s_2`. Since `v(s_2)=v_0+s_2v_1` is complex-affine (`v_0=C-B`,
`v_1=R(\beta)(A-C)`, both `s_2$-independent), `W_1(s_2)=\bar dv_0+s_2\bar
dv_1` is complex-affine in the real variable `s_2`: as `s_2` ranges over
`\mathbb R`, `W_1(s_2)` traces a straight line `\ell_1\subset\mathbb C`
with constant complex "velocity" `\bar dv_1=\mathrm{slope}(D_K)+i\cdot
\mathrm{slope}(L_1)`. Because `s_2` is a **single real parameter** (not a
free point of `\mathbb C$), this line's `\mathrm{Re}` and `\mathrm{Im}`
parts are each individually literally AFFINE (degree-1, not just
piecewise/interval) functions of `s_2` — so the "two lines in ℂ" question
reduces further, concretely, to comparing the zero-crossing points of two
degree-1-in-`s_2` real functions with the two roots of the quadratic
`G_{2a}(s_2)`, not an abstract quadrant/velocity argument. This is a
sharper, more computable reduction than the outline anticipated, and it is
what let this round make unconditional progress (below), not merely a
qualitative "same kind of question" restatement.

**New Lemma (fully proved, unconditional — no case split, no
Y-sign dependence): the `L_1<0`-selected root of `G_{2a}` is *always* the
algebraically smaller of the two roots, `r_{\mathrm{lo}}:=\min(r_1,r_2)`.**

*Proof.* `L_1(s_2)=P(u)+s_2Q(u)` is affine in `s_2$ with slope `Q(u)`. I
computed the trigonometric form of `Q(u)` (own `sympy` session, half-angle
substitution `u=\tan(\beta/2)`, dividing by the always-positive
`(1+u^2)^2`):
$$\frac{Q(u)}{(1+u^2)^2}=b\sin2\beta+cc\cos2\beta
=AC\cdot(\cos\angle A\sin2\beta+\sin\angle A\cos2\beta)=AC\sin(2\beta+\angle A)$$
(using `b=AC\cos\angle A,\ cc=AC\sin\angle A$, the standard identification
of `C`'s coordinates via the vertex angle at `A`; verified exactly by
`sympy`, symbolic difference `0` after expanding `\sin(2\beta+\angle A)`
via the angle-addition formula and matching term-for-term). Since `AC>0`,
`(1+u^2)^2>0`, `\mathrm{sign}(Q(u))=\mathrm{sign}(\sin(2\beta+\angle A))`.

**`\sin(2\beta+\angle A)>0` throughout the valid range, unconditionally.**
Since `0<\beta<\min(\angle B,\angle C)`, we have
`2\beta<2\min(\angle B,\angle C)\le\angle B+\angle C` (as `\min(x,y)\le
(x+y)/2` for any reals `x,y`), so
$$2\beta+\angle A<\angle B+\angle C+\angle A=\pi,$$
and trivially `2\beta+\angle A>\angle A>0`. So `2\beta+\angle A\in(0,\pi)`,
where `\sin>0$. Hence `Q(u)>0` unconditionally (for every scalene triangle
and every `\beta` in the valid range) — this is a genuinely new, clean,
fully general fact (a direct analogue of the sibling
`coordinate-bash-resultant-boundary`'s already-certified `\sin(A+\beta)>0`
lemma, but for the doubled angle `2\beta+\angle A`, arising from a
different vector pairing).

Now, `Q(u)>0` means `L_1(s_2)$ is **strictly increasing** in `s_2`.
Combined with the already-certified fact (Theorem 11.8,
`lemmas/cross-product-sign-selection-G2a.md`, item 3–4) that `L_1(r_1)
L_1(r_2)<0$ — i.e. `G_{2a}`'s two roots straddle `L_1`'s unique zero
`z_1:=-P(u)/Q(u)` — an increasing affine function is negative strictly
below its zero and positive strictly above it; since `r_{\mathrm{lo}}<z_1<
r_{\mathrm{hi}}` (both roots real and distinct, straddling `z_1`, already
certified), we get `L_1(r_{\mathrm{lo}})<0` and `L_1(r_{\mathrm{hi}})>0`
**directly**, with no need to identify which of `r_1,r_2$ is which by any
other means. So the `L_1<0` root is always `r_{\mathrm{lo}}$. `\blacksquare`

**Why this is real, useful progress (sharper than the pre-existing
Theorem 11.8).** Theorem 11.8 only asserted "exactly one of `G_{2a}`'s two
roots has `L_1<0`" — an existence/uniqueness statement, silent on which
root (algebraically) it is. This round's lemma identifies it explicitly as
the smaller root, **independent of any other data** (triangle shape,
`\beta`, or the sign of `Y`/any other case-defining quantity elsewhere in
the population's apparatus). This converts the remaining same-root
question from "is the `L_1<0` root (abstractly identified) also the `W>0`
root?" into the concrete, closed-form question "**is `W(r_{\mathrm{lo}})>0`
always**?" — a single-root evaluation question, not a same-root
correlation between two abstractly-labeled roots.

**Progress toward `W(r_{\mathrm{lo}})>0`, via the same slope/zero-crossing
method (partial — genuinely reduces the problem but does not close it this
round).** By the identical method as `D_K`'s and `D_N`'s certified
both-roots-products (`lemmas/g2a-true-supplementary-parity-and-quartic-identification.md`
part (b)):
$$D_K(r_1)D_K(r_2)\propto\mathrm{sign}(Y),\qquad
D_N(r_1)D_N(r_2)\propto-\mathrm{sign}(Y)$$
(`Y:=2a(u^2-1)^2-b(u^2+1)^2`, the sibling's already-certified branch-
selection factor, `lemmas/yb2z-trig-identification.md`). So **exactly one**
of `D_K,D_N`'s zeros lies strictly between `r_{\mathrm{lo}},r_{\mathrm{hi}}`
(the other's zero lies outside that interval, giving it a *constant* sign
on `[r_{\mathrm{lo}},r_{\mathrm{hi}}]`) — which one depends on
`\mathrm{sign}(Y)`:
- **If `Y<0`:** `D_K`'s zero is interior. By the identical slope/zero-
  crossing argument as above (using the trig form found this round,
  $$\mathrm{slope}(D_K)/(1+u^2)^2=b\cos2\beta-cc\sin2\beta=AC\cos(2\beta+\angle A)$$
  — verified exactly, own `sympy` session, same method as `Q(u)`'s
  identification), `\mathrm{sign}(D_K(r_{\mathrm{lo}}))=
  -\mathrm{sign}(\cos(2\beta+\angle A))`. `D_N`'s zero is then *exterior*,
  so `D_N` has one constant sign `\sigma_N` on the whole interval,
  requiring a separate evaluation (not resolved this round — see below).
- **If `Y>0`:** symmetric, `D_N`'s zero is interior:
  `\mathrm{slope}(D_N)=2(b^2+cc^2)(u^2-1)`, so
  `\mathrm{sign}(D_N(r_{\mathrm{lo}}))=-\mathrm{sign}(u^2-1)=
  \mathrm{sign}(1-u^2)`; `D_K` has one constant sign `\sigma_K` on the
  interval, also not yet resolved.

**Attempted resolution of `\sigma_K,\sigma_N` via the interval midpoint
(started, not completed this round).** Since `[r_{\mathrm{lo}},
r_{\mathrm{hi}}]$'s interior sign for the exterior-zero function equals its
sign at ANY interior point, in particular the midpoint `m_0=
-B_2^a/(2A_2)` (`B_2^a$ = the `s_2`-coefficient of `G_{2a}`, `A_2` its
leading coefficient — Vieta), I computed `D_N(m_0)` and `D_K(m_0)` in
closed form (own `sympy` session) and trig-identified the (positive, by the
already-certified `\sin(\beta+\angle A)>0$ lemma) common denominator:
$$2bu^3+2bu-cc\,u^4+cc=(1+u^2)^2\cdot AC\sin(\beta+\angle A)>0,$$
exactly matching (as a consistency cross-check) the sibling's already-
certified `\sin(A+\beta)>0` fact from a completely different derivation
route (this round's independent re-derivation of the same trig fact from a
different polynomial is a genuine corroboration, not a coincidence — both
arise as the "denominator" controlling a rotation-parametrization
non-degeneracy). Continuing, I trig-identified `D_N(m_0)`'s numerator
bracket exactly (own `sympy` session, fitted against a
`\sin(3\beta),\cos(3\beta),\sin\beta,\cos\beta` basis and confirmed the fit
by 20 independent numeric substitutions, `|{\rm error}|<10^{-14}$ in all
cases — not yet a from-scratch symbolic `sympy.simplify=0` confirmation,
which stalled on the mixed `\tan(\beta/2)` form; the numeric confirmation
is strong but this specific identity, unlike the others in this round's
work, is **not yet elevated to a certified symbolic identity**):
$$(u^2-1)B_2^a+2(1+u^2)\cdot(2bu^3+2bu-cc\,u^4+cc)
\;\stackrel{?}{=}\;(1+u^2)^3\Bigl[\tfrac32 b\sin\beta-\tfrac12cc\cos\beta
-\tfrac12(b\sin3\beta+cc\cos3\beta)\Bigr].$$
This shows `\sigma_N`'s sign reduces to the sign of a specific mixed
trig expression, of the same general shape as the sibling's still-open
`(Y,B_2,Z)` sign classification (in fact it visibly shares the
`b\sin3\beta+cc\cos3\beta` term with the sibling's already-identified
`B_2$ quantity) — **not yet resolved to a fixed sign**, and `\sigma_K`
(the `Y>0` case's analogous quantity) was not computed at all this round
due to time.

**Honest assessment of what this round closes and what remains.** This
round **fully closes and certifies** the "which root does `L_1<0` select"
question (unconditionally `r_{\mathrm{lo}}`, no case split) — a genuine
strengthening of Theorem 11.8, reusable independently of the rest of this
gap. It **narrows** the same-root correlation question to a concrete
two-case (`Y\gtrless0`) sign computation, in each case reducing to a single
constant-sign quantity (`\sigma_K$ or `\sigma_N`) evaluated at the interval
midpoint, with an explicit (numerically-confirmed, not-yet-symbolically-
certified) trig closed form for the `Y<0`-case's `\sigma_N$ quantity. It
does **not** close the correlation itself this round: neither `\sigma_K`
nor `\sigma_N`'s sign has been established (even conditionally) throughout
the valid range, and the `Y<0`-case's `D_K(r_{\mathrm{lo}})` sign
(`=-\mathrm{sign}(\cos(2\beta+\angle A))$, itself not fixed-sign since
`2\beta+\angle A\in(0,\pi)` straddles `\pi/2`) still needs to be combined
correctly with `\sigma_N`'s sign, which was not completed. This is real,
honestly-scoped progress — a strictly smaller, more concrete remaining
target than at the start of the round — not a closed proof.

**Net for this round.** The "two lines in ℂ" reframing is **verified
correct and sharper than anticipated**: because `s_2` is a single real
parameter, both "lines" are literally single affine real functions, letting
the monotone slope-sign argument directly pin `L_1<0\Rightarrow s_2=
r_{\mathrm{lo}}` unconditionally (a new certified-quality lemma). The
same method was pushed into the `D_K,D_N` sign question and produced a
concrete two-case reduction with one new (numerically-confirmed,
not-yet-symbolic) trig identity, but did not close `W(r_{\mathrm{lo}})>0`.
Status remains `partial`.

### Round 9 (this round) — full symbolic closure of `W(r_lo)>0`, both cases,
via a new "evaluate at the sibling's own zero" method that bypasses the
`Y<0` case's previously-uncertified trig-fit entirely

**Dispatch task**: close `W(r_lo)>0` (the last item needed for this
approach's own remaining gap), split `Y>0` (near-mechanical per the
outline) / `Y<0` (harder, reduces to `\mathrm{sign}(\cos(2\beta+\angle
A)\cdot\mathrm{num})\ge0`); also cross-check `num` against the sibling's
`f(\beta)-K`.

**Headline result: `W(r_{\mathrm{lo}})=D_K(r_{\mathrm{lo}})D_N(r_{\mathrm{lo}})>0`
is now proved unconditionally, in both cases, by a fully symbolic argument
(zero numeric-only steps in the final chain).** The key new idea, found
this round, is not to compare `D_K`'s or `D_N`'s zero to the *messy* Vieta
midpoint `m_0=-B_2^a/(2A_2)` (as round 8 attempted, stalling on an
uncertified triple-angle trig fit), but to evaluate each affine function at
**the OTHER function's own zero** — `z_N:=1/(2\cos\beta)` (`D_N`'s zero,
already known in closed form) and `z_K:=-P_K/Q_K` (`D_K`'s zero) — both of
which turn out to give dramatically simpler closed forms than the generic
midpoint `m_0`.

**Step 0 (re-derivation from scratch, own `sympy` session, not copying any
prior file's polynomials).** With `A=(0,0),B=(a,0),C=(b,cc)` (`a,cc>0`),
`N=C/2`, `d(\beta)=(-\cos\beta,\sin\beta)`, `L(s_2)=C+s_2R(\beta)(A-C)`, I
recomputed, directly from these raw vector definitions:
$$D_K(s_2)(1+u^2)^2=P_K(u)+s_2Q_K(u),\qquad D_N(s_2)=\tfrac{b^2+cc^2}4(1-2s_2\cos\beta),$$
$$P_K=-(1+u^2)\bigl[(a-b)(u^2-1)-2cc\,u\bigr],\quad
Q_K=b(u^4-6u^2+1)+4cc\,u(u^2-1)$$
(`u=\tan(\beta/2)`; `D_N`'s closed form matches the already-certified fact
from round 9's `math-explorer-complex-affine-transfer-lens.md`, re-verified
here independently from the raw vectors, exact zero-residual match). I
also re-derived the full squared-cosine quartic `(V_1\cdot
V_2)^2|V_3|^2|V_4|^2-(V_3\cdot V_4)^2|V_1|^2|V_2|^2` directly (Lemma P1's
`(Q)`, no shortcuts) and confirmed it factors as `-(b^2+cc^2)^2(u^2+1)^4/
(u^2+1)^6\cdot G_{2a}\cdot G_{2b}` with
$$G_{2a}(s_2)=A_2s_2^2+B_2^as_2+C_2,\quad A_2=2(1+u^2)\bigl(cc(u^2-1)-2bu\bigr),$$
matching the already-certified `A_2` formula of
`lemmas/cross-product-sign-selection-G2a.md`/§11.7 exactly (independent
re-derivation, zero residual) — confirming this quartic's first factor
genuinely is (up to the already-certified positive/negative constant) the
population's own `G_{2a}`, not a differently-normalized object. (One
transcription note, purely cosmetic, does not affect any downstream
computation: the `G_{2a}` formula as literally displayed in
`coordinate-bash-resultant.md` §2/line 201 has no `cc`-dependence at all,
which cannot be correct for a polynomial that must depend on `C`'s
`y`-coordinate; my independently re-derived `G_{2a}` does depend on `cc`
and its leading coefficient `A_2` matches the certified formula exactly, so
the *substantive* content already certified across the population is
unaffected — only that one specific old display in a non-canonical file is
flagged as stale, echoing the identical kind of cosmetic transcription slip
already found and corrected in round 2's history.)

**Step 1 (interior/exterior classification of both zeros, exact, both
cases at once).** Using the standard quadratic-sign fact (`G_{2a}(x)=
A_2(x-r_1)(x-r_2)`, so `\mathrm{sign}(G_{2a}(x))=-\mathrm{sign}(A_2)` for
`x` strictly between the two real roots and `=\mathrm{sign}(A_2)` outside;
`A_2<0` throughout the valid range, already certified, `lemmas/cross-
product-sign-selection-G2a.md`; both roots real, already certified via the
`L_1`-straddle argument), I computed, in a fresh `sympy` session:
$$G_{2a}(z_N)=\frac{u(u^2+1)}{(u^2-1)^2}\cdot Y,\qquad
G_{2a}(z_K)=\frac{(u^2+1)^3F_2}{Q_K^2}\cdot Y$$
(`Y:=2a(u^2-1)^2-b(u^2+1)^2`, the already-certified branch factor,
`lemmas/yb2z-trig-identification.md`; `F_2` the already-certified-negative
resultant cofactor, `lemmas/cross-product-sign-selection-G2a.md`/
`g2a-true-supplementary-parity...md` — independently reconfirmed `F_2<0`
here too, 20,000 fresh random samples, own script, 0 violations). Both
identities are **exact, zero-residual** (`sympy.factor`/`cancel`, not
numeric fits). Since `u(u^2+1)/(u^2-1)^2>0$ and `(u^2+1)^3/Q_K^2\ge0` (with
equality only at the measure-zero, excluded-by-genericity locus `Q_K=0`),
this gives:
$$\mathrm{sign}(G_{2a}(z_N))=\mathrm{sign}(Y),\qquad
\mathrm{sign}(G_{2a}(z_K))=\mathrm{sign}(F_2)\cdot\mathrm{sign}(Y)=-\mathrm{sign}(Y).$$
Combined with `A_2<0`: **`Y>0\Rightarrow z_N` interior, `z_K` exterior;
`Y<0\Rightarrow z_K` interior, `z_N` exterior** — an exact, symbolic
confirmation of the case split first observed (numerically, plus a partial
symbolic derivation for `z_N` alone) in round 9's explorer report, now
completed for `z_K` as well.

**Step 2 (`Y>0` case, fully closed, unconditionally, no residual case
split).**
- *`D_N(r_{\mathrm{lo}})>0`.* `D_N`'s slope is `-\tfrac{b^2+cc^2}2\cos\beta
  <0` always (`\cos\beta>0` throughout the valid range: `\beta<\min(\angle
  B,\angle C)\le(\angle B+\angle C)/2<\pi/2`, elementary, already used
  elsewhere in this population). So `D_N` is **strictly decreasing** in
  `s_2`. Since `z_N` is interior (`Y>0`, Step 1) — i.e. `r_{\mathrm{lo}}<
  z_N<r_{\mathrm{hi}}` by definition of "interior" for the ordered pair of
  real roots — and `D_N` decreasing with `D_N(z_N)=0`, we get
  `D_N(r_{\mathrm{lo}})>D_N(z_N)=0`, i.e. `D_N(r_{\mathrm{lo}})>0`,
  **unconditionally, with no reference to any trig sign at all.**
- *`D_K(r_{\mathrm{lo}})>0`.* Since `z_K` is exterior (`Y>0`, Step 1),
  `D_K` (affine, hence monotone) does not vanish on `[r_{\mathrm{lo}},
  r_{\mathrm{hi}}]`, so it has one constant sign there, equal to its sign
  at *any* interior point — in particular at `z_N` (interior, just used
  above). Direct computation (own `sympy` session, from the raw vectors,
  no Weierstrass substitution needed):
  $$D_K(z_N)=a\cos\beta-\frac{b}{2\cos\beta}=\frac{2a\cos^2\beta-b}{2\cos\beta}.$$
  By the already-certified identity `Y=(1+u^2)^2(2a\cos^2\beta-b)`
  (`lemmas/yb2z-trig-identification.md`, re-verified independently this
  round) and `\cos\beta>0`, this gives `Y=(1+u^2)^2\cdot2\cos\beta\cdot
  D_K(z_N)`, so `\mathrm{sign}(D_K(z_N))=\mathrm{sign}(Y)`. In the `Y>0`
  case this is `+`, so `D_K(z_N)>0`, hence `D_K(r_{\mathrm{lo}})=
  D_K(z_N)>0` (constant sign on the interval, just established).
- **Conclusion**: `W(r_{\mathrm{lo}})=D_K(r_{\mathrm{lo}})\cdot
  D_N(r_{\mathrm{lo}})=(+)\cdot(+)>0` in the `Y>0` case — a **complete,
  symbolic, unconditional proof**, no numeric step anywhere in the chain.

**Step 3 (`Y<0` case, fully closed, unconditionally — the harder case,
closed by a genuinely new argument, bypassing the previously-stuck
`\mathrm{sign}(\cos(2\beta+\angle A)\cdot\mathrm{num})` route entirely).**
- *`D_K(r_{\mathrm{lo}})`.* `z_K` is interior (`Y<0`, Step 1), so
  (`D_K` affine, straddled by the two real roots at `z_K`):
  `\mathrm{sign}(D_K(r_{\mathrm{lo}}))=-\mathrm{sign}(\text{slope of }D_K)
  =-\mathrm{sign}(Q_K)$ (an increasing affine function is negative below
  its zero, so the smaller root gives the opposite sign to the slope).
- *`D_N(r_{\mathrm{lo}})`.* `z_N` is exterior (`Y<0`, Step 1), so `D_N` has
  one constant sign on `[r_{\mathrm{lo}},r_{\mathrm{hi}}]`, equal to its
  value at any interior point — in particular at `z_K` (interior, just
  used above). Direct computation (own `sympy` session):
  $$D_N(z_K)=\frac{(b^2+cc^2)}{4}\cdot\frac{Y}{Q_K}$$
  (exact, zero-residual: the raw numerator of `D_N(z_K)` factors exactly as
  `(b^2+cc^2)(u^2+1)\cdot Y`, and the raw denominator as `4(u^2+1)Q_K`, so
  the `(u^2+1)` cancels exactly, leaving this clean closed form — no
  triple-angle expansion, no trig-fit, needed at all). Since `b^2+cc^2>0`,
  `\mathrm{sign}(D_N(z_K))=\mathrm{sign}(Y)\cdot\mathrm{sign}(Q_K)`. In the
  `Y<0` case this is `-\mathrm{sign}(Q_K)`.
- **Conclusion**: in the `Y<0` case,
  $$\mathrm{sign}(D_K(r_{\mathrm{lo}}))=-\mathrm{sign}(Q_K),\qquad
  \mathrm{sign}(D_N(r_{\mathrm{lo}}))=-\mathrm{sign}(Q_K),$$
  the **same** sign — so
  $$W(r_{\mathrm{lo}})=D_K(r_{\mathrm{lo}})D_N(r_{\mathrm{lo}})
  =\bigl(-\mathrm{sign}(Q_K)\bigr)^2>0$$
  **unconditionally, regardless of what `\mathrm{sign}(Q_K)` (equivalently
  `\mathrm{sign}(\cos(2\beta+\angle A))`) actually is** — the two unknown
  signs are forced equal and hence their product is always `+`. This is
  the round's key structural discovery: **the `Y<0` case's difficulty was
  illusory** — the earlier `\mathrm{sign}(\cos(2\beta+A)\cdot\mathrm{num})
  \ge0` target (round 9's explorer, from a *different*, messier
  `m_0`-based derivation) is not needed at all, because both factors of
  `W(r_{\mathrm{lo}})` reduce, via evaluation at the *other* factor's own
  zero, to `-\mathrm{sign}(Q_K)` **simultaneously**, so their product is a
  perfect square, positive by construction, with no residual sign
  determination left over.

**Step 4 (genericity/degenerate points, excluded consistently with the
rest of the population's conventions).** The argument requires: (i) both
roots of `G_{2a}` real (already certified, via the `L_1`-straddle argument,
`lemmas/cross-product-sign-selection-G2a.md`); (ii) `A_2\ne0`, in fact
`A_2<0` (already certified); (iii) `Y\ne0` (the `Y>0`/`Y<0` split is
exhaustive up to this measure-zero locus, consistent with every other
case-split in this population, e.g. `lemmas/yb2z-trig-identification.md`'s
own treatment); (iv) `Q_K\ne0` (needed only in the `Y<0` case, where `D_K`
is genuinely affine with an interior zero; if `Q_K=0`, `D_K` is constant
and the "interior zero" framing is vacuous — a further measure-zero
sub-locus of `Y<0`, excluded by the same genericity convention). None of
these introduces a new, previously-unused type of exclusion — all are
either already-certified population-wide facts or measure-zero loci of the
same codimension-1 kind already excluded elsewhere (e.g. `K\ne L$,
`A_2\ne0`).

**Cross-check performed (as dispatched): is this round's "`\mathrm{num}$"
quantity (or the earlier `D_N(m_0)`-based sign quantity) proportional to
the sibling `coordinate-bash-resultant-boundary`'s `f(\beta)-K` residual?**
Computed both explicitly (own `sympy` session): the round-9 explorer's
`\mathrm{num}=AC[\cos(2\beta+A)\sin\beta(1-2\cos\beta)+\sin(2\beta+A)
\cos2\beta]$ and my own directly-derived, algebraically-confirmed
`D_N(m_0)$-sign quantity `AC[\sin(\beta-A)-\cos(2\beta+A)\sin\beta]` (the
two do independently confirm the SAME previously-uncertified round-8 target
identity, now proved exactly via a clean sum-to-product derivation — see
Promotable lemmas) are **not** proportional to each other pointwise
(numeric ratio varies non-constantly, even changes sign, across 8 random
samples — a **negative** result, honestly reported); nor is either one
needed by the final proof above, which bypasses this whole family of
quantities via the cleaner `z_N`/`z_K`-evaluation method. I did not
complete a direct symbolic comparison against `coordinate-bash-resultant-
boundary`'s `f(\beta)-K` (time-limited this round) — this specific
cross-check is left open, but is now moot for closing `W(r_{\mathrm{lo}})
>0$, since that target is fully closed by Steps 2–3 without reference to
`\mathrm{num}` or `f(\beta)-K` at all.

**What this closes, precisely, and what remains open — an important,
honest correction to the outline's step-9 expectation.** This round
**fully, symbolically, unconditionally closes `W(r_{\mathrm{lo}})>0`** —
the entirety of this approach's own previously-open target (both the
`Y>0` case, reduced to two short confirmations by the outline, and the
harder `Y<0` case, closed here by a new argument rather than the
originally-planned `\mathrm{num}$-sign route). Combined with the
already-certified `L_1<0\Rightarrow s_2=r_{\mathrm{lo}}$
(`lemmas/complex-affine-L1-DK-and-r-lo-selection.md`) and Theorem
11.8/§12 (`lemmas/cross-product-sign-selection-G2a.md`,
`lemmas/magnitude-bound-and-sign-coincidence.md`), this proves: **on
`G_{2a}`'s own two roots, `r_{\mathrm{lo}}` is the UNIQUE root satisfying
all of Lemma P1's conditions (2)-(4)** (containment, "K inside angle LBA",
and now also the true/matched-sign hypothesis-2 equation) — a complete,
gap-free theorem about the `G_{2a}` branch specifically.

**However — re-examining the logical chain carefully, the outline's step 9
("`W(r_{\mathrm{lo}})>0`⟹branch selection closed⟹the whole problem is
solved") is NOT fully justified by this alone, and I do not claim it.**
Lemma P1 is a logical equivalence for a *given* candidate `s_2`
(`s_2` satisfies hyp2∧containment∧angle-test `\iff` (1)-(4) hold at that
`s_2`) — it does not, by itself, rule out a **second** value of `s_2`,
lying on `G_{2b}$ instead of `G_{2a}`, that *also* happens to satisfy
(2)-(4). To conclude that the **actual** geometric configuration's `s_2`
equals `r_{\mathrm{lo}}$ (not some `G_{2b}` root), one still needs the
**`G_{2b}` full exclusion** — showing no root of `G_{2b}` satisfies (2)-(4)
jointly — which is the pre-existing gap this file has repeatedly flagged as
identical (via `lemmas/g2a-true-supplementary-parity-and-quartic-
identification.md`'s structural unification) to `coordinate-bash-
resultant-boundary`'s own open `(Y,B_2,Z)` three-way classification. **This
round's work does not touch `G_{2b}` at all** (every identity above is
about `G_{2a}`'s two roots and their relationship to `D_K,D_N`'s zeros)
— so it is still honestly the case that **branch selection, and hence the
whole problem, is NOT yet fully closed.** What changes this round: this
approach's *own* previously-designated remaining target (`W(r_{\mathrm{lo}}
)>0`) is now completely, rigorously closed — the *sole* remaining gap for
the whole population is the `G_{2b}`-exclusion question, shared verbatim
with the sibling `coordinate-bash-resultant-boundary` (its `(Y,B_2,Z)`
three-way sign classification, still open there too as of this round).

### Round 10 (this round) — the MVT/degeneration mechanism, dispatched
independently of the sibling's algebraic 3-way case split: fully proves an
unconditional Lipschitz/MVT reduction chain, reduces the shared `G_{2b}`-
exclusion gap (equivalently Case (b) of Theorem 16.2, `Y(\gamma)<0`) to a
**single new, radical-free trig inequality in `(A,B)` alone** — strong
numeric evidence (global optimization, not just random sampling) that it is
true and tight exactly at the same degenerate corner as the target itself,
but **not closed symbolically this round**.

**Setup (shared with the sibling `coordinate-bash-resultant-boundary`,
certified `lemmas/claim-I-closed-and-claim-II-caseA-closed.md`).** WLOG
`\angle B\le\angle C` (`\gamma=\angle B`). Write
$$K_c=2\sin A\sin(A+B),\ P=\tfrac12\sin(A-B)+\tfrac32\sin(A+B),\ Q=-\sin
A\sin B,\qquad f(\beta)=K_c+P\sin\beta+Q\cos\beta,\quad G(\beta):=2K_c-f(\beta).$$
Certified facts reused verbatim, no re-derivation: `f'(\beta)=\sin(A+\beta)
\cos B+\sin(A+B-\beta)$; `f'(\beta)>0` on `(0,\gamma)` (so `G$ is strictly
decreasing there, `G'=-f'<0$, unconditionally, both cases); `\cos B>0`
(`B<\pi/2`, from `B\le C`). `\beta_0:=(\pi-A)/3`. The open sub-case is:
given `\cos^2\beta_1=X_0:=\dfrac{\sin B\cos A}{2\sin(A+B)}` (real, i.e.
`\cos A\ge0`, needed for `\beta_1` to exist at all), `\beta_1\in(\beta_0,
\gamma)` (Case (b): `\beta_1<\gamma`; corrected domain-nonemptiness,
established by this round's outliner/reviewer independently: `\beta_1>
\beta_0`) — prove `G(\beta_1)\ge0`.

**Step 0 (honest correction of an unverified claim in this round's outline
dispatch).** The dispatch instructed using "`G(\beta_0)>0` (already
established, Theorem 16.1's endpoint lemma)" as a starting point. **I
checked this directly and it is FALSE in general** — a fresh 2,000,000-
sample sweep over the full `(A,B)` domain (own script) gives `G(\beta_0)<0`
on `\approx23\%` of samples. The certified `lemmas/claim-I-closed-and-
claim-II-caseA-closed.md` Theorem B only proves `f(\beta_0)>0`, **not**
`2K_c-f(\beta_0)>0` — these are different quantities, and the outline's
dispatch conflated them. However, restricting to the genuine Case-(b) domain
(`\cos A\ge0`, `\beta_0<\beta_1<\gamma`, the actual hypothesis set this
approach needs), a fresh independent sweep (3,000,000 samples) found **zero**
violations of `G(\beta_0)>0`: this is the correct, narrower claim needed and
it holds — but I flag explicitly that it is **not yet symbolically proved**
in this round either (see "what remains open" below); it is used only as an
intermediate quantity in the reduction chain, and the final inequality below
subsumes it (does not need it proved as a separate lemma).

**Step 1 (fully proved, unconditional Lipschitz bound on `f'`).**
$$f'(t)=\sin(A+t)\cos B+\sin(A+B-t)\le\cos B+1\qquad\text{for every }t,$$
since `\sin(A+t)\le1`, `\cos B>0$ (so `\sin(A+t)\cos B\le\cos B`), and
`\sin(A+B-t)\le1`. No hypothesis on `t` needed beyond `\cos B>0` (already
certified). `\blacksquare`

**Step 2 (fully proved, exact MVT/integration bound, no gap).** Since `f` is
smooth and `f'\le1+\cos B` everywhere,
$$f(\beta_1)-f(\beta_0)=\int_{\beta_0}^{\beta_1}f'(t)\,dt\le(1+\cos B)
(\beta_1-\beta_0)\qquad(\beta_1>\beta_0).$$
Since `G=2K_c-f`, this gives, **unconditionally** (no case split, no sign
assumption beyond `\beta_1>\beta_0`, `\cos B>0`):
$$G(\beta_1)=G(\beta_0)-\bigl(f(\beta_1)-f(\beta_0)\bigr)\ \ge\ G(\beta_0)
-(1+\cos B)(\beta_1-\beta_0).\tag{MVT-1}$$
`\blacksquare` — an exact, rigorous, unconditional lower bound; the earlier
work in this file's Round 6–9 entries never needed calculus, so this is a
genuinely new technique for this population, not a restatement of prior
work.

**Step 3 (fully proved, a second exact bound eliminating `\beta_1` in favor
of `\cos\beta_1=\sqrt{X_0}` — no remaining trig-argument variable).** Since
`\cos` has derivative `-\sin`, and `[\beta_0,\beta_1]\subset(0,\pi/2)`
(`\beta_0>0` trivially since `A<\pi`; `\beta_1<\gamma<\pi/2` since `\gamma=B
<\pi/2`), `\sin` is **strictly increasing** on this interval, so `\sin(t)\ge
\sin(\beta_0)$ for `t\in[\beta_0,\beta_1]`:
$$\cos\beta_0-\cos\beta_1=\int_{\beta_0}^{\beta_1}\sin(t)\,dt\ \ge\ \sin(\beta_0)
(\beta_1-\beta_0)\quad\Longrightarrow\quad \beta_1-\beta_0\ \le\
\frac{\cos\beta_0-\cos\beta_1}{\sin\beta_0}\qquad(\sin\beta_0>0).\tag{MVT-2}$$
`\blacksquare` — exact, rigorous, no gap; `\sin\beta_0>0` since `\beta_0\in
(0,\pi/3)`.

**Step 4 (combining MVT-1, MVT-2 into a single radical-free target — fully
rigorous reduction, no gap).** Since `1+\cos B>0`, (MVT-2) gives `-(1+\cos B)
(\beta_1-\beta_0)\ge-(1+\cos B)\dfrac{\cos\beta_0-\cos\beta_1}{\sin\beta_0}`,
so combining with (MVT-1):
$$G(\beta_1)\ \ge\ G(\beta_0)-(1+\cos B)\frac{\cos\beta_0-\cos\beta_1}{\sin
\beta_0}.\tag{$\dagger$}$$
It therefore **suffices** to prove the right side of `(\dagger)` is `\ge0`,
i.e. (multiplying by `\sin\beta_0>0`, direction preserved):
$$\sin\beta_0\,G(\beta_0)\ \ge\ (1+\cos B)(\cos\beta_0-\cos\beta_1).\tag{$\ddagger$}$$
Writing `\mathrm{RHS}:=(1+\cos B)\cos\beta_0-\sin\beta_0\,G(\beta_0)` (a
function of `A,B` alone — `\cos\beta_0,\sin\beta_0,G(\beta_0)` are all
explicit closed forms in `A,B` via `\beta_0=(\pi-A)/3`, no `\beta_1`
anywhere), `(\ddagger)` is `(1+\cos B)\cos\beta_1\ge\mathrm{RHS}`. Since
`\cos\beta_1=\sqrt{X_0}\ge0` and `1+\cos B>0`, the left side is `\ge0`
always, so:
- **If `\mathrm{RHS}\le0`:** `(\ddagger)` holds trivially (`\text{LHS}\ge0\ge
  \mathrm{RHS}$). **Fully closed, no further computation.**
- **If `\mathrm{RHS}>0`:** both sides of `(1+\cos B)\sqrt{X_0}\ge\mathrm{RHS}`
  are `\ge0`, so squaring is valid and equivalent:
  $$\boxed{(1+\cos B)^2X_0\ \ge\ \mathrm{RHS}^2}\tag{$\star$}$$
  a **single-radical-free** (no `\sqrt{}` anywhere — `X_0` itself is a
  rational trig expression, `\mathrm{RHS}` a polynomial in `\sin,\cos$ of
  `A,B,\beta_0`, hence, after eliminating `\beta_0=(\pi-A)/3` via multiple-
  angle formulas, ultimately a rational/polynomial-in-`\sin(A/3),\cos(A/3)`
  expression in `A,B`) trig inequality with **only one squaring step**,
  compared to the sibling `coordinate-bash-resultant-boundary`'s
  `B_{\mathrm{coef}}^2X_0-E^2\ge0` target, which requires **two** squarings
  of a two-radical expression. This is a genuinely different (and
  structurally simpler, one fewer squaring) reduction of the same
  underlying gap, found via the boundary/MVT mechanism rather than direct
  algebraic isolation. `\blacksquare` (for the reduction itself — `(\star)`
  is the new open target, not yet proved.)

**Step 5 (extensive numerical testing of the final target `(\star)`, via
global optimization rather than random sampling — this round's strongest
evidence, not a proof).** I verified the full chain end-to-end numerically
first (500,000 random `(A,B)` samples restricted to the genuine Case-(b) +
domain-nonempty region, own script): `G(\beta_1)\ge G(\beta_0)-(1+\cos B)
(\beta_1-\beta_0)$ [(MVT-1)] holds with **zero** violations (min residual
`\approx2\times10^{-6}$, consistent with equality only in a limit); the
further bound via (MVT-2) also holds with zero violations (min residual
`\approx5\times10^{-11}`, i.e. (MVT-2) is extremely tight, essentially exact,
away from measure-zero). I then targeted `(\star)` directly with **global
optimization** (`scipy.optimize.differential_evolution` plus 80–150
Nelder-Mead restarts, not merely random sampling, specifically to hunt for
a hidden sign violation that a random sweep could miss): **the global
minimum of `(1+\cos B)^2X_0-\mathrm{RHS}^2` over the entire valid `(A,B)`
region (Case (b), domain-nonempty, `\mathrm{RHS}>0`) is `\approx1.5\times
10^{-9}$, i.e. numerically indistinguishable from `0` and never negative**,
attained at `A\approx0.4064,\ B\approx0.9117` — and direct evaluation shows
this **is exactly the degenerate corner** `\gamma-\beta_0\to0`
(`\gamma-\beta_0\approx-1.2\times10^{-9}`, i.e. numerically `\gamma=\beta_0`
to solver precision), the **same** corner this round's `sturm-sos-lens`
explorer independently identified as where `G(\beta_1)\to0`. This is a
strong structural confirmation that the MVT chain's two lossy steps (Step 1's
crude `f'\le1+\cos B` bound, Step 3's linear cos-difference bound) are, in
aggregate, **essentially tight exactly where the original inequality is
tight** — i.e. the reduction is not merely "safe/lossy in a way that happens
to still work," but appears asymptotically sharp at the one place that
matters. **I did not find a way to prove `(\star)` symbolically this round**:
substituting `\beta_0=(\pi-A)/3` produces genuine `\sin(A/3),\cos(A/3)`
(triple-angle) terms that resisted `sympy.simplify`/`factor` into a
recognizable SOS or product form in the time available (own attempt,
displayed but not resolved — see "what remains open").

**A sanity check that a cruder bound is NOT sufficient (important negative
finding, rules out an easier route).** I first tried bounding `\beta_1-
\beta_0` crudely by the **full domain width** `\gamma-\beta_0` (dropping the
dependence on `\beta_1` itself, i.e. testing `G(\beta_0)\ge(1+\cos B)
(\gamma-\beta_0)`): **this is FALSE** — global optimization finds a genuine
negative violation (`\approx-0.078`, at `A\approx0.488,B\approx1.137`, well
away from any degenerate corner). This confirms (per the outline's own
"watch out for" caution) that the argument genuinely needs the finer bound
via `\beta_1-\beta_0$ specifically (Steps 1–4 above), not merely "`G$
shrinks like the domain width" as a loose heuristic — the outliner's
degeneration description was directionally right but the naive
implementation of it does not work; the two-step MVT chain (via `\cos\beta_1`
rather than the raw domain width) is required and does work (Step 5).

**Honest assessment: what this round closes and what remains.** This round
**fully, rigorously proves** (Steps 1–4, zero gaps, unconditional, no case
split beyond the trivial `\mathrm{RHS}\lessgtr0` dichotomy which is itself
fully closed on the `\le0` side): `G(\beta_1)\ge0$ **follows from** the single
new radical-free trig inequality `(\star)` in `A,B$ alone. This is a genuine,
different-mechanism reduction of the shared `G_{2b}`-exclusion gap — one
squaring instead of the sibling's two, and derived via calculus (MVT/
Lipschitz) rather than direct algebraic isolation, exactly as dispatched.
It does **not** close the gap: `(\star)` itself is not proved symbolically,
only tested at extreme numerical scale (global optimization, not just
random sampling) with the infimum exactly `0` at precisely the same
degenerate corner as the original target — strong but not sufficient
evidence per CLAUDE.md's no-conjecture-as-established rule. **I have not
completed the whole-problem proof this round**: this remains an independent,
partially-reduced route to the same shared gap that both this approach and
`coordinate-bash-resultant-boundary` must still close (either one closing
its own remaining target — `(\star)` here, or `B_{\mathrm{coef}}^2X_0-E^2\ge0`
there — would finish the whole population's proof, since round 8's
structural-equivalence theorem shows the two are the same underlying gap,
approached via two different, non-identical algebraic reductions this
round).

### Round 11 (this round) — Hessian check performed as dispatched: it
REFUTES the outline's implicit premise (interior PSD critical point), and
identifies the true local mechanism as a first-order (gradient/domain-
boundary) tangency, not a second-order one — a precise, honest negative
finding that redirects the approach, plus one new exact-root coincidence
recorded for a future round.

**Dispatch task**: attack `(\star): (1+\cos B)^2X_0\ge\mathrm{RHS}^2` via a
degenerate-limit/width-Taylor expansion in `w=\gamma-\beta_0` around the
pinned corner `A^*\approx0.40638,B^*\approx0.91174`, with a local Hessian
check first and a tangent-line fallback if the Taylor route stalls.

**Step 0 (re-verification, own fresh `mpmath` session, 40-digit precision,
not reusing any prior round's script).** Re-solved the corner exactly:
`\mathrm{findroot}` on `G_{\mathrm{curve}}(A):=G(A,\beta_0(A),\beta_0(A))`
(with `\beta_0(A)=(\pi-A)/3$ and `G,K_c,P,Q,f` the already-certified closed
forms of `lemmas/mvt-lipschitz-reduction-case-b.md`) gives, to 40 digits,
$$A^*=0.4063777806843303293871746903293092626710\ldots,$$
matching the outline's reported value to all displayed digits. Confirmed
`\mathrm{star\_slack}(A^*,B^*):=(1+\cos B^*)^2X_0(A^*,B^*)-
\mathrm{RHS}(A^*,B^*)^2=1.97\times10^{-31}$ at this 40-digit precision — i.e.
genuinely `0` to the precision used, not a numerical artifact of a coarser
solver. `\blacksquare` (independent re-confirmation of the outline's corner
data.)

**Step 1 (the Hessian check, exactly as the outline's Step 2 dispatches —
performed via high-precision centered finite differences,
`h=10^{-6}`, `mpmath` 30-digit arithmetic, at the corner
`(A^*,B^*)`).**
$$\nabla(\mathrm{star\_slack})(A^*,B^*)\approx(1.7809,\,1.1205)\neq(0,0).$$
**This single computation is decisive and refutes the premise the outline's
Step 3 was conditioned on.** The outline's plan explicitly required
checking "whether it is a genuine smooth local minimum (PSD Hessian)... this
determines whether a plain local Taylor/PSD argument can possibly work
before committing to the symbolic version" — and the check *fails* at the
very first test: **the corner is emphatically not an unconstrained interior
critical point of `\mathrm{star\_slack}` as a function on `\mathbb R^2`** (a
critical point requires zero gradient; here the gradient has magnitude
`\approx2.10`, not small). So the entire "Taylor-expand around a PSD
critical point" mechanism envisioned in Step 3 of the outline **does not
apply as originally conceived** — there is no PSD-Hessian argument to be
made here, because the function is not stationary at the corner in the
first place. (For completeness, the raw, unconstrained-in-`\mathbb R^2`
Hessian was also computed: `\partial_{AA}\approx-2.7332,\
\partial_{AB}\approx1.8559,\ \partial_{BB}\approx-2.0478`, giving
`\det\approx2.153>0` and `\mathrm{tr}<0` — i.e. `\mathrm{star\_slack}`,
extended as an unconstrained smooth function of `(A,B)` past the actual
domain boundary, has a **local maximum**, not a minimum or saddle, at the
corner. This is consistent with — indeed explains — the nonzero gradient
finding: since the corner is a domain-boundary point, not an unconstrained
extremum, the function's behavior *within* the actual admissible region is
governed by the gradient (first order), with the corner being the point
where a shrinking sliver of the admissible region gets squeezed against the
level set `\mathrm{star\_slack}=0` from the side where the gradient points
into non-positive territory — a fundamentally different, and structurally
simpler in principle, mechanism than a PSD-Hessian argument, but the
outline's Step 3 as written does not cover it.)

**Step 2 (identifying the correct local structure: the corner is a
domain-boundary CUSP, not an interior point — a new structural finding,
established by direct computation of the true admissible `(A,B)` region,
not assumed).** Recall `\beta_1=\beta_1(A,B)` is defined by
`\cos^2\beta_1=X_0(A,B)`, `\cos\beta_1\ge0` (the branch used throughout this
population), and Case (b) is, by definition (per the certified reduction
this file inherits), exactly the sub-region where
$$\beta_0(A)<\beta_1(A,B)<B\qquad(\gamma=B\text{ throughout, WLOG }B\le C).$$
I scanned, for fixed `A`, the sign of `\beta_1(A,B)-\beta_0(A)` and of
`B-\beta_1(A,B)` as `B$ ranges over the triangle-valid interval
`(\beta_0(A),(\pi-A)/2]` (the upper limit being the `B\le C` boundary), own
fresh `mpmath` script, 30-digit precision, dense grids at
`A\in\{0.1,0.2,0.3,0.35,0.4,0.406,0.4064,0.41,0.42,0.45,0.5,0.6,0.7,0.9,1.1,
1.3\}$. **Result, exact and unambiguous, no borderline cases**: for every
tested `A\le0.4064$ (i.e. `A\le A^*` to 4 digits), the admissible interval
`\{B:\beta_0(A)<\beta_1(A,B)<B\}` is **empty** (checked directly, not
inferred: at `A=0.406` and `A=0.4064$, zero valid `B` were found among 300
random samples each in the triangle-valid range, matching zero among the
whole dense scan); for every tested `A\ge0.41`, the interval is **nonempty**
with strictly positive width, e.g. at `A=0.42$ the admissible window is
approximately `(0.9299,0.9526)` (width `\approx0.0227`), widening
substantially by `A=0.6$ (window `\approx(0.9531,1.062)`, width
`\approx0.11`, from the boundary-crossing data recorded in this round's raw
scan). **So the Case-(b) sub-case, as an actual region of the `(A,B)`
plane, is empty for `A\le A^*` and only becomes nonempty for `A>A^*$** —
this had not been explicitly identified or recorded by any prior round of
this population; all earlier numerics (the 552-, 300k-, 2M-, and
3M-sample sweeps cited in Rounds 6, 8, 9, 10) sampled the *already-known
nonempty* region without characterizing its lower boundary in `A` at all.

**Step 3 (a striking exact-root coincidence, verified to 40 digits — flagged
honestly as UNPROVED, not used as an established fact).** I checked whether
the threshold value of `A` found in Step 2 (where the admissible `B$-window
first opens, i.e. where the two boundary curves `\beta_1(A,B)=\beta_0(A)`
and `\beta_1(A,B)=B` meet) coincides with `A^*$ exactly. At the meeting
point the two boundary conditions force `B=\beta_0(A)` (since the window
shrinks to a point there) **and**, substituting `B=\beta_0(A)` into
`\beta_1(A,B)=\beta_0(A)`, this becomes the single-variable equation
$$\cos^2(\beta_0(A))=X_0(A,\beta_0(A)).\tag{$\dagger\dagger$}$$
Solving `(\dagger\dagger)` via `mpmath.findroot$ (own fresh session, 40-digit
precision, starting point `A=0.4`, independent of the `G_{\mathrm{curve}}$
solve in Step 0) gives
$$A=0.4063777806843303293871746903293092626710\ldots,$$
**identical to `A^*` from Step 0 to all 40 displayed digits.** This is a
genuine, numerically air-tight coincidence (not merely "close," but agreeing
to the full precision of two independently-formulated root-finding
problems), strongly suggesting `(\dagger\dagger)` and
`G_{\mathrm{curve}}(A)=0` share their unique relevant root **for a structural
reason** (plausibly: `\beta_1$ is `f`'s critical point, `f'(\beta_1)=0`, and
`\beta_0`'s definition via Theorem 16.1's endpoint lemma is itself tied to
where `f$ crosses a specific threshold — so the "window closes" condition
and the "`G$ changes sign at the endpoint" condition may be two views of one
critical-point coincidence event). **I checked directly whether the two
quantities `G_{\mathrm{curve}}(A)` and `\cos^2\beta_0(A)-X_0(A,\beta_0(A))`
are proportional as functions of `A`** (which would make the coincidence a
one-line algebraic corollary): computed the ratio at six sample points
(`A=0.1,0.3,0.5,0.7,1.0,1.3`) and found it **not constant**
(`\approx3.05,3.08,3.03,2.90,2.59,2.17$ respectively) — so the two
expressions are **not proportional**, and the shared root is a genuine,
nontrivial coincidence, not an immediate algebraic identity. **This
structural connection between the domain-nonemptiness threshold and the
existing certified boundary-lemma's zero is a new and potentially valuable
observation for a future round** (e.g. it may indicate both quantities
vanish simultaneously because they both encode "`f'(\beta_0)=0$" or a
related degenerate condition at the common point — this is a plausible
mechanism, consistent with `\beta_1$'s definition via `f'(\beta_1)=0` and
`\beta_0`'s appearance in the certified endpoint lemma, but **I did not
derive or verify this mechanism symbolically this round** — it is reported
honestly as an unproved, numerically-air-tight observation, not a
established fact, per CLAUDE.md's no-conjecture-as-established rule).

**Step 4 (honest assessment: why the outline's planned Step 3/Step 4 do not
directly close `(\star)` this round, and what the corrected picture
implies).** Because the corner is a domain-boundary cusp (Step 2) with
nonzero gradient (Step 1) rather than an interior PSD critical point, the
outline's envisioned mechanism — "expand in `w:=\gamma-\beta_0` at fixed
`\theta:=(\beta_1-\beta_0)/w`, show the zeroth-order term in `w` is `\ge0`
and vanishes only at `A=A^*`" — needs revision: **there is no well-defined
"zeroth-order-in-`w`" limit that is independent of `A` at fixed `\theta`,
because as `A\to A^*` the very domain (the range of valid `\theta$, i.e. the
admissible-`B` window) collapses to a point, not merely to a `w=0` slice at
fixed shape.** In other words, the outline's proposed two-variable
reparametrization `(w,\theta)` is well-defined away from the corner but
becomes singular exactly at the corner in a way that entangles `w\to0` and
`A\to A^*` (as the outline itself flagged as a risk — "any expansion must
hold `A\to A^*` and `w\to0` together, not treat them as independent
perturbations" — this round's Hessian/gradient computation shows *why*
concretely: the admissible-`\theta$ range shrinks to a single point at
`A=A^*`, so a naive "zeroth order in `w`, for each fixed `A`" expansion is
attempting to hold `\theta` fixed over a range that does not exist at the
limit). I attempted the tangent-line fallback (outline's Step 4) as an
alternative, linearizing `X_0(A,B)$ in `A` at `A=A^*` (fixed `B=B^*`): this
requires `X_0'(A^*,B^*)$ and a proof that `X_0(A,B^*)\ge X_0(A^*,B^*)+
X_0'(A^*,B^*)(A-A^*)` for all relevant `A` (a one-sided tangent-line bound),
but time did not permit completing and verifying this construction
end-to-end this round (only the derivative value was computed numerically,
`X_0'(A^*,B^*)\approx-0.216`, own finite-difference check — not yet used in
any completed inequality).

**Net assessment for this round's dispatch.** The Hessian check (dispatched
as the mandatory first step) **was performed and gives a clear, negative
answer to the specific question asked**: the corner is not a PSD (or any)
critical point of the unconstrained slack function — the outline's premised
"if PSD" branch does not apply, and the "if not PSD" branch (which the
outline left for "the builder must design") is now known to be the
*relevant* branch, with the true structure identified as a domain-boundary
cusp where the admissible sub-domain itself vanishes at `A=A^*` (Step 2, a
genuinely new and precisely verified characterization of Case (b)'s
`A`-range, not previously recorded), plus a striking unproved exact-root
coincidence (Step 3) that is a concrete, well-scoped target for a future
round (prove `(\dagger\dagger)$ and `G_{\mathrm{curve}}(A)=0$ share their
root without relying on 40-digit numerics — e.g. via a joint algebraic
manipulation of `f'(\beta_1)=0$ and the certified endpoint lemma). **`(\star)`
itself is NOT proved this round** — this round's contribution is a precise,
honest diagnosis of why the originally-dispatched mechanism does not apply
as planned, a corrected structural picture of the domain (new and
verified), and one concrete unproved lead for whichever future round
attempts the domain-boundary-cusp argument in full. Status remains
`partial`.

## Promotable lemmas

- **New finding (round 11, verified numerically to high precision, own
  fresh `mpmath` script; NOT yet a symbolic proof): the actual Case-(b)
  sub-region of the `(A,B)` plane is EMPTY for `A\le A^*` and nonempty
  (with a window in `B` of strictly positive width) for `A>A^*`, where
  `A^*\approx0.40638` is exactly the same root as the already-certified
  boundary curve's zero `G_{\mathrm{curve}}(A^*)=0`.** Established by
  direct computation of the admissible-`B` window
  `\{B:\beta_0(A)<\beta_1(A,B)<B\}` (`\beta_1$ defined by `\cos^2\beta_1=
  X_0(A,B)`) at 16 sample values of `A`, confirming emptiness below
  `A\approx0.406` and nonemptiness (explicit windows given) above
  `A\approx0.41`. This had not been recorded by any prior round (all prior
  numerical sweeps sampled only the already-known-nonempty region without
  characterizing its lower boundary). Reusable by any future approach that
  needs a precise description of Case (b)'s domain in `A` (not just in
  `\theta=(\beta_1-\beta_0)/(\gamma-\beta_0)$ at fixed `A`).
- **New observation (round 11, numerically air-tight to 40 digits but
  explicitly NOT proved symbolically — a concrete open target, not a
  claimed theorem): the domain-nonemptiness threshold equation
  `\cos^2(\beta_0(A))=X_0(A,\beta_0(A))` and the already-certified boundary
  curve's zero `G_{\mathrm{curve}}(A)=0` (`G_{\mathrm{curve}}(A):=
  G(A,\beta_0(A),\beta_0(A))`) share the identical unique root `A^*` to 40
  displayed digits, despite the two quantities NOT being proportional as
  functions of `A` (checked at 6 sample points, ratio varies
  non-constantly from `\approx3.08` to `\approx2.17`).** This suggests a
  nontrivial shared structural cause (plausibly both encoding a degenerate
  condition at `f`'s critical point `\beta_1=\beta_0=\gamma`) that was not
  derived this round. A future round proving this coincidence symbolically
  (e.g. via `f'(\beta_1)=0` combined with the certified endpoint lemma)
  would give a clean, corner-independent characterization of `A^*` useful
  for any tangent-line or cusp-based closing argument.
- **Negative finding (round 11, decisive, own high-precision finite-
  difference computation, `mpmath` 30-digit arithmetic,
  `h=10^{-6}`): the gradient of `\mathrm{star\_slack}:=(1+\cos B)^2X_0-
  \mathrm{RHS}^2` at the corner `(A^*,B^*)` is `\approx(1.781,1.121)\ne
  (0,0)`, and the corner is in fact a LOCAL MAXIMUM (not a minimum, saddle,
  or degenerate point) of `\mathrm{star\_slack}` extended as an
  unconstrained smooth function past the true domain boundary
  (Hessian `\approx\begin{pmatrix}-2.733&1.856\\1.856&-2.048\end{pmatrix}`,
  `\det\approx2.15>0`, `\mathrm{tr}<0`).** This refutes the premise of any
  argument that treats the corner as an interior PSD-Hessian critical point
  of the unconstrained function — the tightness of `(\star)` at this point
  is a domain-boundary (cusp) phenomenon, not a stationary-point phenomenon,
  and any future local-expansion argument must be built around the
  cusp/vanishing-admissible-window structure (see the finding above), not a
  Taylor-around-a-critical-point argument. Worth recording explicitly so no
  future round re-attempts a plain PSD-Hessian argument at this corner.
- **New lemma (round 10, fully proved, Steps 1-4 above): an MVT/Lipschitz
  reduction of the shared `G_{2b}`-exclusion gap (Theorem 16.2 Case (b)) to
  a single radical-free inequality `(\star)` in `A,B` alone.** Precisely:
  with `\beta_0=(\pi-A)/3`, `X_0=\sin B\cos A/(2\sin(A+B))`,
  `\mathrm{RHS}:=(1+\cos B)\cos\beta_0-\sin\beta_0\,G(\beta_0)` (`G(\beta_0)`
  an explicit closed form in `A,B`), if `\mathrm{RHS}\le0` then `G(\beta_1)
  \ge0` unconditionally; if `\mathrm{RHS}>0` then `G(\beta_1)\ge0` follows
  from `(1+\cos B)^2X_0\ge\mathrm{RHS}^2`. Proved via: (i) the unconditional
  Lipschitz bound `f'(t)\le1+\cos B` (elementary, `\sin\le1,\cos B>0`); (ii)
  the exact MVT/integration bound `G(\beta_1)\ge G(\beta_0)-(1+\cos B)
  (\beta_1-\beta_0)`; (iii) a second exact MVT bound `\beta_1-\beta_0\le
  (\cos\beta_0-\cos\beta_1)/\sin\beta_0` (from `\sin` increasing on
  `(\beta_0,\beta_1)\subset(0,\pi/2)`); (iv) combining and a trivial-vs-
  square case split on `\mathrm{sign}(\mathrm{RHS})`. No gap in this
  reduction itself (only the resulting `(\star)` remains open, numeric-only,
  see Current best for the extensive global-optimization evidence). Reusable
  by the sibling `coordinate-bash-resultant-boundary` as an independent,
  structurally different (one fewer squaring) route to the same shared gap
  than its own `B_{\mathrm{coef}}^2X_0-E^2\ge0` target.
- **Negative finding (round 10, fully checked): the cruder bound `G(\beta_0)
  \ge(1+\cos B)(\gamma-\beta_0)` (using the full domain width instead of
  `\beta_1-\beta_0`) is FALSE**, confirmed by global optimization (violation
  `\approx-0.078`, away from any degenerate corner) — rules out the naive
  "linear in domain width" implementation of the degeneration heuristic;
  the finer `\beta_1-\beta_0`-based bound (Steps 1-4 above) is necessary and
  (per Step 5's evidence) sufficient. Worth recording so no future round
  re-attempts the cruder version.
- **New lemma (round 9, full proof above, `W(r_{\mathrm{lo}})>0`
  unconditionally): on `G_{2a}`'s two real roots, the algebraically
  smaller root `r_{\mathrm{lo}}` always satisfies `W(r_{\mathrm{lo}})=
  D_K(r_{\mathrm{lo}})D_N(r_{\mathrm{lo}})>0`, for every triangle and every
  `\beta` in the valid range.** Proved via two new exact closed forms
  (own `sympy`, zero residual): `D_K(z_N)=(2a\cos^2\beta-b)/(2\cos\beta)`
  (`z_N=1/(2\cos\beta)$, `D_N`'s zero) and `D_N(z_K)=(b^2+cc^2)Y/(4Q_K)`
  (`z_K=-P_K/Q_K`, `D_K`'s zero; `Y=2a(u^2-1)^2-b(u^2+1)^2`), combined with
  `G_{2a}(z_N)\propto Y` and `G_{2a}(z_K)\propto F_2\cdot Y` (`F_2<0`
  certified) to classify which of `z_N,z_K` is interior/exterior to
  `[r_{\mathrm{lo}},r_{\mathrm{hi}}]` in each case
  (`Y>0`: `z_N` interior, `z_K` exterior; `Y<0`: reversed). In the `Y>0`
  case both factors are directly positive (`D_N` decreasing +interior
  zero; `D_K`'s constant sign `=\mathrm{sign}(Y)>0` via the `z_N`
  evaluation). In the `Y<0` case both factors independently reduce to
  `-\mathrm{sign}(Q_K)` (`D_K` via the interior-zero straddle argument,
  `D_N` via the `z_K` evaluation), so their product is a perfect square,
  positive regardless of the actual value of `\mathrm{sign}(Q_K)` — no
  residual trig-sign determination needed. Fully closes this approach's
  own designated remaining target (`W(r_{\mathrm{lo}})>0`, previously
  numeric-only at 20,000 samples). Does **not** by itself close the
  `G_{2b}`-exclusion question (still open, shared with the sibling
  `coordinate-bash-resultant-boundary`'s `(Y,B_2,Z)` classification).
- **New identity (round 9, full proof above, resolves round 8's
  "not yet certified" flagged item): the `G_{2a}`-midpoint `D_N`-numerator
  identity is TRUE and now proved via a clean sum-to-product derivation**
  (not the stalled `\tan(\beta/2)`-simplify route): with `AC:=\sqrt{b^2+
  cc^2}`, `A=\angle BAC`,
  $$16bu^3+cc(u^6-7u^4+7u^2-1)=AC(1+u^2)^3\bigl[\sin(\beta-A)-
  \cos(2\beta+A)\sin\beta\bigr]$$
  exactly (own `sympy` session, `\beta=2\arctan u` substitution, symbolic
  residual `0`). This is the quantity `D_N(m_0)`'s sign reduces to (`m_0`
  = the Vieta midpoint of `G_{2a}`'s two roots) — reusable for any future
  attempt that wants the messier `m_0`-based route rather than this
  round's cleaner `z_N`/`z_K`-evaluation method. Not used in the final
  proof above (superseded by the cleaner route) but recorded as a
  genuinely new, fully proved trig identity closing a previously-flagged
  open item.
- **New lemma (round 7, full proof above): `W(r_1)W(r_2)\le0` on `G_{2a}`'s
  two roots** (`W:=D_K\cdot D_N`, the matched-sign/"true-equation" test),
  proved via `\mathrm{Res}(G_{2a},D_K)=(u^2+1)^3F_2Y`,
  `\mathrm{Res}(G_{2a},D_N)=4u(b^2+cc^2)^2(u^2+1)Y`, giving
  `W(r_1)W(r_2)=4u(b^2+cc^2)^2(u^2+1)^4F_2Y^2/A_2^2\le0` using the
  already-certified `F_2<0`, `A_2<0`. Reusable by the sibling approach or
  any future attempt needing the full true/supplementary structure of
  `G_{2a}` (mirrors, and is proved by the same method as, the already-
  certified `lemmas/g2b-true-supplementary-parity.md`). No gap in this
  lemma's own proof.
- **New structural fact (round 7): Lemma P1's quartic `(Q)` equals a
  positive-constant multiple of `-G_{2a}\cdot G_{2b}`** (exact symbolic
  identity, independently re-derived from the raw vector definitions,
  matching `math-explorer-sturmlens.md`'s independently-displayed `G_{2b}`
  term-for-term). Reusable as the formal bridge unifying this approach's
  Lemma P1/P2 with the sibling `coordinate-bash-resultant-boundary`'s
  `G_{2a}/G_{2b}` apparatus — any progress on one directly transfers to the
  other via this identification.
- **Lemma P1 (round 6, full proof above): pointwise translation of
  hypothesis 2 + `L\in\triangle BNC` + "K inside angle LBA" into four
  explicit conditions on `s_2` alone (given `β`), with no reference to the
  `G_{2a}`/`G_{2b}` factorization.** Reusable by any future attempt at
  branch selection that wants to avoid the polynomial-factorization step
  entirely, or that wants an exact (non-numerical) statement of what
  "genuine solution" means at the level of a single real variable `s_2`.
  Proof is complete and elementary (an unsigned-angle-equality
  case-split + the already-certified Theorem 11.8 reduction); no gap.
- **Lemma P2 (mirror, via certified `σ`-symmetry): the `t_1`-side
  analogue.** Same status; includes an explicit, previously-undocumented
  observation that the sign convention for the mirrored cross-product test
  flips relative to the `s_2`-side (`>0` rather than `<0`), confirmed both
  symbolically (orientation-reversal of `σ` acting on this specific cross
  product) and by a numerical correction discovered and fixed in this
  round's own experiment (initial 0/25 → corrected 25/25, then 279/279 at
  scale) — worth recording explicitly so no future round repeats the same
  sign-convention mistake.
- **New lemma (round 8, full proof above): `\bar d\cdot v(s_2)=D_K(s_2)+i
  L_1(s_2)` exactly**, i.e. `L_1,D_K` are literally the imaginary/real parts
  of one complex-affine function of `s_2` — verified by direct symbolic
  recomputation of `\mathrm{cross}(d,v),\mathrm{dot}(d,v)` from the raw
  vector definitions, exact match (zero symbolic difference) against the
  independently-certified `L_1,D_K` closed forms, no proportionality
  constant needed (literal equality, not merely same-sign). Reusable
  as the exact justification for treating `(L_1,D_K)` as one complex-affine
  line for any future attempt at this or a structurally similar
  branch-selection problem.
- **New lemma (round 8, full proof above): the `L_1<0`-selected root of
  `G_{2a}` is always the algebraically smaller root, `r_{\mathrm{lo}}=
  \min(r_1,r_2)`, unconditionally (every scalene triangle, every `\beta` in
  the valid range, no case split on `\mathrm{sign}(Y)` or anything else).**
  Proved via: (i) `Q(u)$ (the `s_2`-coefficient of `L_1$) trig-identifies as
  `(1+u^2)^2\cdot AC\sin(2\beta+\angle A)` (exact, own `sympy` session); (ii)
  `\sin(2\beta+\angle A)>0` unconditionally since `2\beta+\angle A\in(0,\pi)`
  (from `\beta<\min(\angle B,\angle C)\le(\angle B+\angle C)/2`, so
  `2\beta+\angle A<\angle A+\angle B+\angle C=\pi$); (iii) `L_1` increasing
  plus the already-certified `L_1(r_1)L_1(r_2)<0` (roots straddle `L_1`'s
  zero) forces the smaller root to have the negative value. Strictly
  sharpens the pre-existing Theorem 11.8
  (`lemmas/cross-product-sign-selection-G2a.md`), which only asserted
  existence/uniqueness of the `L_1<0` root without identifying it. No gap in
  this lemma's own proof; reusable by the sibling approach and any future
  attempt at the `G_{2a}`/`G_{2b}` branch-selection apparatus.
- **New fact (round 8, exact, own `sympy` session, not yet built on
  further): the `s_2$-coefficient of `D_K` trig-identifies as
  `(1+u^2)^2\cdot AC\cos(2\beta+\angle A)`** (sign not fixed, since
  `2\beta+\angle A\in(0,\pi)` straddles `\pi/2`) — the natural "conjugate"
  fact to the `Q(u)$ identity above (real vs. imaginary part of the same
  complex-affine velocity `\bar dv_1`), reusable for any future attempt at
  the `D_K$-interior-zero (`Y<0`) case of the same-root correlation.
- **New fact (round 8, exact, own `sympy` session): the interval-midpoint
  denominator `2bu^3+2bu-cc\,u^4+cc=(1+u^2)^2\cdot AC\sin(\beta+\angle
  A)>0`** — an independent re-derivation (via a completely different
  polynomial, `G_{2a}`'s own Vieta midpoint construction) of the sibling
  `coordinate-bash-resultant-boundary`'s already-certified `\sin(A+\beta)>0`
  fact, serving as a genuine cross-corroboration of that lemma from an
  unrelated computation. Reusable as a nonvanishing/positivity fact for any
  future midpoint-evaluation argument on `G_{2a}`.
- **Not yet certified (round 8, numeric-only, 20-sample fit,
  `|\text{error}|<10^{-14}`, not yet a from-scratch symbolic
  `sympy.simplify=0` confirmation): the `G_{2a}`-midpoint `D_N$-numerator
  identity**
  $$(u^2-1)B_2^a+2(1+u^2)(2bu^3+2bu-cc\,u^4+cc)=(1+u^2)^3\Bigl[\tfrac32b
  \sin\beta-\tfrac12cc\cos\beta-\tfrac12(b\sin3\beta+cc\cos3\beta)\Bigr]$$
  (`B_2^a$ = `G_{2a}`'s `s_2`-coefficient). Flagged explicitly as
  NOT certified — a future round should first obtain a clean symbolic
  proof (e.g. by hand via sum-to-product, since the direct `sympy.simplify`
  route stalled on the mixed `\tan(\beta/2)` form) before relying on it,
  then use it to resolve the `Y<0`-case's `\sigma_N` sign and push toward
  closing the full same-root correlation.
