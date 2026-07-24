# Outline review — round 28, imo-2026-03

All three revisions checked against the actual approach-file text (not just
the outliner's paraphrase), the cited certified lemmas, and independent
numeric/symbolic re-derivation where load-bearing.

## 1. rank-pigeonhole-budget: CHANGES REQUESTED

Target: close $(\star_3)=\mathrm{MinFloor}(4)$ via 20-shape exhaustive
vertex enumeration on the 4-piece ladder, cheap-dispatching all but 2
shapes.

**Technique is sound and well-precedented.** The Vertex-Minimum Theorem
(certified, `lemmas/vertex-minimum-theorem.md`) genuinely collapses the
continuum optimization to a finite discrete case split, and this is the
identical method already used to close `MaxCeil(3)`/`MaxCeil(4)`
(§7.12–7.13). No objection to the technique itself.

**Real, fixable bug: the shape-count derivation as written is
self-contradictory.** Step 1 says: "Enumerate the 20 shapes exactly
(stars-and-bars over $\sum_{b=0}^{3}\binom{b+3}{3}$)". I evaluated this sum:
$\binom{3}{3}+\binom{4}{3}+\binom{5}{3}+\binom{6}{3}=1+4+10+20=35$, not 20. I
independently brute-forced all $(k_1,k_2,k_3,k_4)$ with $k_i\ge0$,
$\sum k_i\le3$ — confirms **35** shapes exist for the true legal space
("at most 3 cuts"). The correct source of "20" is $\binom{6}{3}=20$,
the count of compositions of **exactly** 3 into 4 nonnegative parts — a
different, narrower quantity than what the stated formula computes.

**However, restricting to the 20 exactly-3 shapes is mathematically
legitimate, just not derived/stated as such in the outline.** By the
Vertex-Minimum Theorem's own part 2 ("a vertex pinned by a fragment $=0$
belongs to the closure of a *lower* composition"), every shape with
$\text{sum}<3$ is a boundary/degenerate case of some shape with sum
exactly 3 (pad any coordinate's slack up to budget 3; the boundary where
that extra cut degenerates to a zero-length fragment reproduces the
lower-sum shape exactly). Since $A$ is continuous, the infimum over the
$\le3$-cut space equals the infimum over the closures of the 20
maximal (sum-exactly-3) shapes — so enumerating only the 20 does cover
the full legal space, PROVIDED each shape's free parameters are allowed to
range over their closed domain including the degenerate boundary. I
independently re-verified numerically (fresh script, 3000
trials/shape, all 35 shapes including sum$<3$): no shape's minimum drops
below $1/15$, and the sum$<3$ shapes' minima coincide with sub-shapes of
$(3,0,0,0)$/$(2,0,1,0)$, consistent with this closure argument. So the
underlying claim is fine — the outline's own formula and its silence on
*why* only 20 (not 35) shapes are needed are the actual defects.

**Required fix before/while building:** (a) correct the shape-count
formula to $\binom{6}{3}=20$ (compositions of exactly 3 into 4 parts), not
the stated sum-over-$b$ formula; (b) explicitly state and cite the
closure/subsumption argument (Vertex-Minimum Theorem part 2) as the reason
enumerating only the 20 maximal shapes, with boundary values included,
covers every legal $\le3$-cut response — this is currently asserted, not
derived, and a builder who tried to "re-derive by hand" the given formula
would get 35 and be confused about which 15 shapes to drop.

**The two "dangerous" shapes.** Numerically confirmed (independent
3000-trial-per-shape random search): $(3,0,0,0)$ and $(2,0,1,0)$ are the
only shapes whose random-search minimum reaches $1/15$; every other shape
(including sum$<3$ sub-shapes not already dominated by these two) stays
strictly above. This corroborates the outline's claimed severity ranking.
$(2,0,1,0)$ is genuinely new content (not reducible to Claim (A)'s
$\pi_1$-only optimum by symmetry) — correctly flagged as open work, not a
free corollary.

Everything else (cheap dispatch via `sharp-dominant-removal-identity` +
Facts 1/2, breakpoint sweep via Insert-Element-Identity +
`odd-run-reduction-lemma` for the two hard shapes, the ban on
rescaling-reduction of $(\star_3)$) is consistent with certified machinery
and the project's own established convention. Not fatal — build with the
two fixes above.

## 2. greedy-halving-adversary: CHANGES REQUESTED (real false-transfer risk)

Target: adapt the certified Theorem 40/41 rank-split mechanism to close
h(m)'s general-m deep-tie residual (the "$T'$-cuts-$p_4$" branch).

**Verified Theorem 40/41's actual mechanism (read both proofs in full,
lines 5788–6073).** The crucial ingredient is not "rank-split +
per-piece trivial bounds" in isolation — it is that $B=\{t^\ast\}\cup
T'=\{p_4\}\cup T''\cup\{t^\ast\}$ has an **external anchor** $p_4$ that
is *automatically* dominant over the entire residual set $T''$ being tied
into: $p_4>\max(T'')$ holds unconditionally because $T''$ only ever
refines pieces $p_5,\dots,p_{n+1}$, all $\le p_5=p_4/2<p_4$, and $p_4$
itself is never touched by $T''$'s cuts. This lets
`sharp-dominant-removal-identity` peel $p_4$ off *both* $T'$ and
$T'_{>t^\ast}$ to get an *exact* identity in terms of $A(H)$, $A(L)$ alone
(Step 3 of Theorem 41) — only after that exact identity is trivial bounds
applied. This two-level structure (untouched anchor above / strictly
smaller refined tail below) is baked into the original Case-(b)
"$T'$-untouched" sub-case, not a generic feature of "any deep-tie
residual."

**This file's own round-26 text already documents the failure mode when
this domination is assumed without re-derivation** ("Explicitly ruled out:
transfer to the sibling's item 2/(7.9.4)" — lines 5892–5906): the
c₂-anchor object has the same surface shape as Theorem 40's target but
"$c_2$ can be arbitrarily small, so $c_2>\max(T''')$ is not guaranteed,"
so Theorem 40 does not apply, and the round-26 text explicitly warns future
rounds "not to assume Theorem 40 transfers there without re-deriving the
domination hypothesis from scratch."

**$h(m)$'s object has exactly the structure this warning is about.**
$h(m):=\inf A(\{c\}\cup S)$ where $S$ is a legal $(\le m-1)$-cut refinement
of the *whole* $m$-ladder $q_1,\dots,q_{m+1}$ (including $q_1$ itself — $S$
is free to spend budget cutting $q_1$), and $c\in(0,q_1]$ is an arbitrary
free coordinate. There is no element playing $p_4$'s role in general: if
$S$'s budget cuts $q_1$, no single element of $\{c\}\cup S$ is guaranteed
to dominate the rest (unlike $T''$, whose refined pieces are ALL strictly
below the untouched $p_4$ by construction). The outline's step 4 — "using
the ladder's own doubling $q_i=2q_{i+1}$ to make the domination hypothesis
automatic (mirrors Theorem 40/41's use of $p_4=2p_5$)" — only actually
holds in the sub-case where $q_1$ remains untouched by $S$ (then $q_1$
genuinely plays $p_4$'s role, dominating the rest of $S$ by the same
level-separation argument). The outline's step 1 states the target for
"any deep-tie vertex $c=t^\ast$ in $S$" with no such restriction, so as
written it claims more than the mechanism (as understood from
Theorem 40/41's actual proof) can currently deliver.

This is the same false-transfer pattern the project has been burned by
twice before (round 23's rescaling-transfer, and this file's own round-26
c₂-anchor note) — a technique that "looks similar" (rank-split +
per-piece bound) but whose soundness depends on a domination hypothesis
that is not automatic outside the specific two-level structure it was
proved for.

**Required fix before/while building:** do not let the builder assume
step 4's domination is free. Either (a) explicitly restrict this round's
target to the sub-branch where $q_1$ is untouched by $S$ (where $q_1$
genuinely dominates, mirroring $p_4$) and prove *that* unconditionally,
leaving the $q_1$-cut branches honestly open; or (b) if attempting the
full deep-tie family, require the builder to first prove (not assume) that
some single element of $\{c\}\cup S$ dominates the rest at every candidate
vertex, before invoking `sharp-dominant-removal-identity`-style peeling. As
a cross-check, the round-28 explorer report
(`/tmp/round-28/math-explorer-hm-branch.md`, item 1) independently surfaces
a structurally different and more clearly justified idea — "if $S$ splits
$q_1$, the worst vertex reduces exactly to a smaller $h(m-1)$-shaped
object" (an actual induction on $m$, not a domination trick) — this is a
distinct, not-yet-attempted mechanism that should not be conflated with
the domination approach; if the domination route stalls on the $q_1$-cut
branches, this is the recommended fallback, not a retry of the same
mechanism with hand-waved domination.

Not a RETHINK: the target ($h(m)$ general closure) remains legitimate and
the $q_1$-untouched sub-case is genuinely closeable by the stated
mechanism with no changes. But building the outline as literally written
(no domination restriction stated) risks the builder reproducing exactly
the already-documented dead end.

## 3. lp-duality-certificate: APPROVE

Target: close $n=4$'s $p_1\ge T/2$ regime "for free" by re-running
Theorem A / Theorem C′ one index up, now that round 27 fully closed
$P(4)$ (= $c(3)\le8/15$, general marking, both regimes).

**Verified the prerequisite genuinely suffices, no smuggling.** Read
Theorem C′'s actual statement and proof (lines 1243–1263): stated and
proved for general $m\ge2$, using only `pair-cancellation-identity` on the
bisected pair $\{p_1/2,p_1/2\}$ — no $n=3$-specific arithmetic anywhere.
Read the Corollary (lines 1294–1314): proof only uses (i) $a_{n-1}>1/2$
(general $n$), (ii) the Telescoping Threshold identity
$a_{n-1}=a_n/(2(1-a_n))$ (already proved for general $n$, lines
1283–1292) — again no hardcoded $D_3=15$ or $a_3=8/15$ constants. The
sufficient condition Theorem C′ actually consumes is exactly "$P(n-1)$
fully closed for an *arbitrary* tail" (both regimes, every marking) — and
`current.md`'s standing rule already certifies $P(4)$ (the complete,
general-marking $n=3$ upper bound) at exactly that scope. The indexing is
consistent with the file's own established convention ($P(m)$ = the
$m$-piece, $(m-2)$-cut-budget theorem), matching the round-9 finding that
this coupling is real (not a formality) — the outline explicitly
re-flags and respects that coupling rather than re-litigating it.

**No unproven $n=4$-specific assumption is smuggled in.** Step 3's
"no gap, no overlap" claim between Theorem A's domain
$[T/2,a_4T)$ and Theorem C′'s domain $[a_4T,T)$ follows mechanically from
the already-general telescoping identity, reused not re-derived — this is
pure substitution.

**Correctly scoped.** The outline explicitly does not claim
$c(4)\le a_4$ in full — only the $p_1\ge T/2$ half — and flags the
$p_1<T/2$ regime as untouched and expected to be substantially harder
(density-growth signal from the explorer). This is honest, not an
overclaim risk.

No issues found. Sound, low-risk, mechanical extension — approve without
reservation.

## Diversity note

All three approaches remain on genuinely distinct fronts (Claim (B)'s
h(m) branch; Claim (A)'s $(\star_3)$ vertex census; the general
upper-bound induction) — no shared-gap collapse this round. The
greedy-halving-adversary flaw, if uncaught, would have been a *third*
instance of the same "assume domination transfers" trap already recorded
twice on file — worth logging as a recurring failure pattern for this
approach's mechanism family specifically.

## Ranking

`update_ranking` applied: lp-duality-certificate (clean APPROVE) ranked
above rank-pigeonhole-budget (fixable formula/citation gap) ranked above
greedy-halving-adversary (real domination-hypothesis gap requiring a
scope restriction before the mechanism is trustworthy). All three already
registered in the population; no new slugs opened, no copies needed this
round.

build set: rank-pigeonhole-budget, greedy-halving-adversary, lp-duality-certificate
