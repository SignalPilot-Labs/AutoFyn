# Proof-outliner report — imo-2026-03, round 7

## 0. Key synthesis this round (drives all three approach choices below)

Re-reading `rank-tie-vertex-reduction.md` and `rank-pigeonhole-budget.md`
side by side turns up a fact neither file states explicitly, but which both
files' own certified lemmas already imply:

**`rank-pigeonhole-budget.md`'s Lemma 1 ("at most one fragment of $F$ exceeds
$p_2$", proved from $p_1=2p_2$ + positivity, completely general — no
restriction to a single cut) applies verbatim to *any* $c_1$, not just
$c_1\le1$.** So for *every* $c_1\ge0$, Xiang Yu's fragmentation of $p_1$ falls
into exactly the same two cases already named in `rank-pigeonhole-budget.md`:

- **Case II** (some fragment $f_1>p_2$): `rank-pigeonhole-budget.md`'s
  Theorem GC($m$) (§3, fully proved, round 6) *already closes this for every
  $c_1$* — GC($m$) allows $F$ to have up to $m+1$ arbitrary parts, not just
  the $2$-part case; the induction never assumed $c_1\le1$. The only gap for
  Case II is that GC($m$) is proved for $\tau$ = the **unrefined** ladder
  tail, not for an arbitrary **legal refinement** $G'$ of the tail. Closing
  that refinement gap is a concrete, bounded task (§2 below).
- **Case I** (every fragment $\le p_2$): this is *exactly*
  `rank-pigeonhole-budget.md`'s open Case I (§4 of that file), and it is
  *exactly* the residual `rank-tie-vertex-reduction.md`'s round-6 explorer
  hit when trying to extend Half-Window Vanishing to $c_1\ge2$ (the
  "origin-anchored window" failure in that report's §2 is the $c_1\ge2$,
  all-fragments-$\le p_2$ regime).

**Consequence: the general-$c_1\ge2$ gap in `rank-tie-vertex-reduction` and
Case I of Claim (A) in `rank-pigeonhole-budget` are the *same* open
inequality**, not two independent gaps. This changes the shape of this
round's work: instead of two separate pushes, we route both approaches at
the same target from two angles (a direct peel/induction angle from
rank-tie-vertex, a certificate angle from lp-duality), and make the
identification explicit in both files so a future round doesn't duplicate
effort under two names.

This is exactly the outline-reviewer's job to weigh, but it directly shapes
the build-set recommendation at the end: whichever slug makes real headway
on Case I this round effectively unblocks both files at once.

## 1. Approach: `rank-tie-vertex-reduction` (revise — peel-induction-on-$c_1$)

**Target (whole problem, lower-bound direction):** for the $n$-ladder, every
legal Xiang Yu response $S$ (any composition, any cut positions) satisfies
$A(S)\ge f(n)$.

**New top-level route (replaces "generalize Half-Window Vanishing directly",
confirmed dead by this round's c1-extension explorer):**

**Step 0 (already proved, reuse verbatim).** `rank-pigeonhole-budget`'s
Lemma 1: at most one fragment of $F$ (Xiang Yu's fragmentation of $p_1$,
any $c_1$) exceeds $p_2$. Case split:
- Case II: some $f_1>p_2$.
- Case I: all fragments of $F$ are $\le p_2$.

**Step 1 (Case II, general tail refinement — the concrete, bounded gap).**
Import Theorem GC($m$) (`rank-pigeonhole-budget.md` §3) but for $\tau=$ an
arbitrary **legal refinement** $G'$ of the tail $T$, not the unrefined
ladder. Concretely: state and prove
$$\text{GC}'(m):\quad A(F\cup G')\ \ge\ s - A(G')_{\text{floor}}
\qquad\text{whenever } F \text{ has a fragment} >\tau_1,$$
where the floor for $A(G')$ comes from the inductive hypothesis on $n-1$
(`tail-self-similarity`, exactly as `rank-tie-vertex-reduction.md` §5.1
already does for $c_1=1$) rather than from $R(\tau)$ directly. **Concrete
plan:** redo the GC($m$) strong induction on tail length with $\tau$
replaced by $G'$ at every step, checking exactly where the original proof
used $\tau_i=2\tau_{i+1}$ (the ratio-2 fact) — this is used only to bound
$s'<\tau_1=2\tau_2$ in the inductive step. For a refined $G'$, the analogous
bound needed is on the *second-largest* value appearing in $G'$, which no
longer has a clean closed form. **Gap to fill:** either (a) show the peeled
inductive step still goes through using only "every element of $G'$ other
than the one exceeding $\tau_1$ is bounded by half of what's left" (a weaker,
possibly sufficient substitute for the ratio-2 fact), or (b) find a genuine
counterexample showing refinement breaks GC($m$) and the case needs a
different route. Either outcome is real progress (positive: closes Case II
in full generality; negative: precisely locates why refinement is special).

**Step 2 (Case I — the shared wall, do not reinvent from scratch).**
Explicitly identical to `rank-pigeonhole-budget`'s open Case I (§4 of that
file): reduces (via the same rank-shift peel, with $\tau_1$ now playing the
role of the dominant element from the *tail* side since no $F$-fragment
dominates) to needing an **upper bound** on $A$ of a smaller same-shape
instance (inequality (4.1) in that file). **Do not re-derive this reduction
independently in this file** — cite `rank-pigeonhole-budget.md` §4 directly
and treat it as one shared gap. This approach's job for Case I is to try the
**peel-induction-on-$c_1$ idea** (this round's c1-extension explorer, §3) as
an alternative route into the *same* inequality: peel at the unique real cut
point $i^*$ where the cumulative fragment sum crosses $p_1/2$ (such a point
always exists among the $c_1$ actual cuts, since partial sums go from $0$ to
$p_1$ in positive steps — this existence claim is easy and should be proved
formally, not just asserted), splitting $F$ into a "big" contiguous group
(sum $\ge p_1/2$) and a "small" group (sum $\le p_1/2$, itself composed of
$\le c_1-1$ further fragments already resolved by Xiang Yu's actual cuts).
**Key gap, flagged honestly, not resolved by this outline:** the "big" side
in general consists of *more than one* actual fragment once $i^*>1$, so it
is **not** literally the 2-fragment $\{x,p_1-x\}$ split the Cross-Term
Reduction Theorem assumes — that theorem's machinery does not apply
verbatim to a multi-element "big" side. The builder's job is to determine
whether the Cross-Term Reduction Theorem generalizes to "$F$ splits into a
big sub-multiset (sum $\ge p_1/2$) and everything else," or whether this
route collapses back into needing the same upper bound as Step 2's direct
citation. **If it collapses (likely, given the c1-extension explorer's
finding that this is the same wall), report that clearly as a negative
result** rather than forcing a proof.

**What NOT to attempt (per this round's explorer, confirmed dead end):**
direct window-by-window generalization of Half-Window Vanishing to
$c_1\ge2$ without routing through the Case I/II split above — concrete
counterexample on file (round-6 explorer report) shows the naive per-window
sufficient condition fails by 50% at a genuine $n=3$ vertex.

## 2. Approach: `lp-duality-certificate` (revise — certify $(\star\star)$/Half-Window-Vanishing itself)

**Target (whole problem, lower-bound direction, same as above, via the
certificate framing.)**

Per this round's lp-duality explorer's recommendation (strongly seconded):
stop sampling more $n=3$/$n=4$ compositions by hand (cell counts explode,
diminishing returns, already documented). Instead:

**Step 1.** Take the certified Half-Window Vanishing Lemma / Cross-Term
Reduction Theorem (the $c_1=1$ closure of $(\star\star)$ in
`rank-tie-vertex-reduction.md` §5.2) and attempt to write its **conclusion**
— $A(F\cup G')\ge f(n)$ for every legal tail refinement $G'$, $F=\{x,p_1-x\}$
— as a single certificate $\Phi - a_n\cdot\mathrm{Total}=\sum_k\lambda_k g_k$
in this approach's own Type-I/Type-II/Sym vocabulary, with $g_k$ ranging
over a **term count that does not grow with the size or structure of
$G'$** (i.e. genuinely bounded, not "one term per tail piece touched").

**Step 2.** The natural candidate decomposition, reading directly off the
Half-Window Vanishing proof: $\Phi-a_n\cdot\mathrm{Total}$ should decompose
as (i) a Type-I/Sym term for the trivial bound on the window's left half
($v\le 1$, giving the $\Delta/2$ contribution) plus (ii) a term expressing
"no element of $G'$ exceeds $p_2$" (Type II, but stated once, about the
*tail as a whole* relative to the fixed constant $p_2$, not fragment-by-
fragment) plus (iii) the inductive-hypothesis floor on $A(G')$ itself
(imported, not re-derived, exactly as the Cross-Term Reduction Theorem
already does). **The test:** does this 3-term shape actually reproduce the
proof algebraically (not just conceptually), for a genuine multi-cut tail
refinement $G'$ (not just the untouched-tail boundary case already checked)?

**Step 3 (the decisive test, per the explorer's own recommendation).** If
Step 2 succeeds cleanly with a term count independent of how many pieces
$G'$ touches, that is strong positive evidence the certificate framework can
absorb arbitrary tail refinements — direct ammunition for attacking Step 1
of the rank-tie-vertex approach above (Case II with refined tail) via a
certificate instead of a re-run induction. If it requires a term for *each*
piece $G'$ touches (mirroring the "$(1,1,1,0)$ thin cell needs $n$ terms"
finding from this round's report), **write this up explicitly as the
negative result the approach file already flags as an acceptable outcome**:
the certificate framing re-encounters $(\star\star)$'s content in new
notation rather than avoiding it, and the project should stop iterating this
framing on the general lower bound (per the file's own §"Recommendation").

**Do not** re-attempt further hand-sampled $n=3$/$n=4$ compositions beyond
what's needed for Step 2/3 above — this round's explorer already did that
broadly (`(2,0,0,0)`, `(1,1,1,0)`, `(2,1,0,0)`) and found diminishing
returns; the certificate-sparsity conjecture (stated in the approach file)
is exactly as hard as the theorem itself unless this direct $(\star\star)$
conversion succeeds.

## 3. Approach: `rank-pigeonhole-budget` (revise — Case I, using the synthesis)

**Target: close Case I of Claim (A)**, now explicitly identified (§0 above)
as the single shared wall for the whole project's lower bound.

Given the honest diagnosis already on file (§4 of that approach: Case I's
natural peel needs an *upper* bound (4.1) on $A(F\cup\tau'')$, an ingredient
no lower-bound machine on file supplies), this round's concrete plan is:

**Step 1.** Wait on / consume whichever of the two approaches above makes
progress this round (§1's peel-induction or §2's certificate test) — if
either produces *any* new tool that bounds $A$ from *above* on a smaller
same-shape instance, plug it directly into inequality (4.1); this is a
one-line finish once the ingredient exists, per the file's own account.

**Step 2 (do this regardless of Step 1's outcome, as independent progress).**
Attempt Case I directly for the smallest nontrivial un-closed instances by a
different, elementary route not yet tried on file: **strengthen the
inductive hypothesis** rather than trying to bound $A(F\cup\tau'')$ in
isolation. Concretely, try proving the *joint* statement "$A(F\cup\tau)\ge
s-R(\tau)$ **and** $A(F\cup\tau)\le$ [some explicit closed-form upper
envelope, e.g. $s+R(\tau)-2\tau_m$ or similar, matching the two extremes
already computed by hand in `rank-tie-vertex-reduction`'s worked examples]"
simultaneously by strong induction on $m$, so that the induction's own
upper-bound half supplies exactly the ingredient (4.1) needs at the next
level down, instead of importing it from outside. This mirrors the standard
"strengthen the induction hypothesis" technique (flagged generically in
`knowledge_base.md`'s induction section) but applied concretely to this
problem's specific recursion for the first time. **Gap to fill:** find the
correct explicit closed form for the matching upper envelope (test against
the extensive exact-`Fraction` data already gathered on file for Case I,
$m=1,\dots,7$, before attempting a general proof) — this is a bounded,
checkable task, not a re-opening of the whole problem.

**What NOT to re-attempt:** the generic-multiset pigeonhole restatement
(refuted round 4) and a bare re-verification of Case II by more numerics
(already fully closed, no further work needed there).

## Build set

`rank-tie-vertex-reduction`, `lp-duality-certificate`, `rank-pigeonhole-budget`

All three target the same shared residual wall (Case I / general-$c_1$
domination) from three different angles — a direct peel/induction argument,
a certificate-conversion test, and a strengthened-induction-hypothesis
attempt — consistent with the plateau-breaking guidance (real cracks
forming, not a new framing needed this round). No new framing is opened this
round; judgment call is that the three live cracks above are more valuable
than a fourth speculative framing at this stage.
