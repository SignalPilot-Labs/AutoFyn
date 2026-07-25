## imo-2026-03

### Global note on this round's pivot
Two independent explorers this round (lemmaX, freshframing) found explicit
numeric counterexamples to **Lemma X′ as literally stated** ("dual
Group-Domination": $\mathrm{EvenSum}(S')\ge T'/2\Rightarrow
\mathrm{EvenSum}(A'\cup S')\ge T'$ for arbitrary positive multisets). **Do
not attempt to prove Lemma X′ in this general form — it is false, doubly
confirmed.** Any replacement must exploit the actual geometric/dyadic
structure of the tail (it is not an arbitrary multiset), not a bare scalar
EvenSum bound. Also confirmed dead this round: the "merging top fragments /
reducing $j$ only helps LB" exchange shortcut (false, explicit
counterexample at $m=4$) — do not retry that specific monotonicity claim
either. Below, all four approaches are revised or advanced to route around
these two confirmed dead ends using the concrete new leads the explorers
found (cut-reallocation/top-only tractability, the Perfect-Pairing /
bisect-everything corollary, and recursive-depth peeling), while keeping
the population's four routes genuinely distinct: (1) recursive-depth
induction on the geometric hierarchy, (2) exact-tail top-only peeling, (3)
a cut-reallocation monovariant/exchange argument, (4) a pairing/parity
argument for the upper bound.

---

self-similar-induction-on-n: revise
Target: $c(n)=2^n/(2^{n+1}-1)$, lower-bound direction: for every $n$, LB's
geometric partition $\Gamma_n$ guarantees $\mathrm{OddSum}\ge 2^n$
(unnormalized) against **every** XY response using $\le n$ cuts (full
$T(n)$, all $j$ simultaneously — not just $j\le1$).
Technique: **Induction loading (Pólya) — build the two-sidedness into the
recursive object itself ("$\Gamma_m$-with-a-hole" family), not into an
abstract dual sum lemma.** This directly implements opening (b) from the
`lemmaX` explorer report and abandons the dead Lemma X′ entirely.

Skeleton:
  1. Recall the certified $j=0$ (Fact 2) and $j=1$ (Step 1, this file,
     already certified) cases — keep as-is, they do not depend on X′.
  2. **New key idea:** instead of peeling by raw global sorted rank (which
     is what forced Lemma X′), peel **by depth in the geometric hierarchy**.
     Concretely: when XY splits the top piece $2^m$ into $j+1$ fragments
     $A=\{a_1,\dots,a_{j+1}\}$ and spends its remaining $\le m-j$ cuts on the
     tail $\Gamma_{m-1}$, track explicitly how many of those cuts land on
     the tail's *own* top piece $2^{m-1}$ (call this count $j'\le m-j$).
     **Observation (the fix for the lemmaX counterexample's failure mode):**
     if $j'=0$ (the tail's own top piece $2^{m-1}$ is untouched), then after
     peeling $a_1$ (when $a_1\ge 2^{m-1}$, which holds whenever $a_1\ge T/2$)
     the *next* global max is exactly $s_1=2^{m-1}$, a **known, unrefined**
     value — not an arbitrary tail element — so peeling it costs exactly
     $+2^{m-1}$ and leaves $\{a_2,\dots,a_{j+1}\}\cup S'$ with $S'$ a
     refinement of $\Gamma_{m-2}$ using $\le m-1-j$ cuts, to which $T(m-2)$
     applies **directly and honestly** (no dual bound needed — this is the
     *same* one-sided inductive hypothesis, just invoked one level deeper).
     If instead $j'\ge1$ (the tail's own top piece is itself split), recurse
     the identical argument one level further down the hierarchy (compare
     against $2^{m-2}$, etc.) — the recursion bottoms out because the
     hierarchy has only $m$ levels and each recursive step strictly
     decreases both the remaining budget and $m$.
  3. State this as an explicit strong induction with a **doubly-indexed**
     hypothesis $T(m,k)$ (already defined) proved by simultaneous strong
     induction on $m$, where the inductive step for $T(m,k)$ (all $j$ at
     once) is discharged by recursing into $T(m-1-j',k')$ for the deepest
     untouched-top-piece level $j'$ actually reached — never by an abstract
     sum inequality on an arbitrary sub-multiset.
  4. Verify the recursion terminates and covers every allocation: since XY's
     cuts are finite and the geometric hierarchy has depth $m$, the "depth
     of the first untouched top piece" is always well-defined and $\le m$;
     induct on this depth (equivalently, on $m$) rather than on $j$ alone.

Key lemmas (claim + mechanism):
  - **Recursive Depth Peeling Lemma (new, the crux, to be proved by the
    builder).** For any refinement of $\Gamma_m$ using $\le m$ cuts, let
    $d\ge0$ be the largest integer such that the pieces $2^{m-1},\dots,
    2^{m-d}$ (the top $d$ levels of the tail hierarchy) are all *untouched*
    by XY's cuts (so $d$ can range from $0$, if even $2^{m-1}$ is cut, up to
    the full tail depth). Then peeling the top fragment $a_1$ (if
    $a_1\ge2^{m-1}$) followed by the untouched values $2^{m-1},\dots,
    2^{m-d}$ **in that exact order** is forced by the global sort (because
    each is strictly larger than the next by the geometric ratio, and
    strictly larger than whatever refined pieces sit below level $m-d$,
    since a piece below level $m-d$ has been refined and hence every
    fragment of it is $<2^{m-d}$) — because splitting a piece into positive
    fragments never produces a fragment $\ge$ the parent (already
    certified, Step 1a's argument, reused verbatim). This converts the
    problem into a *fully determined* prefix of the peeling order, with no
    guessing about interleaving with tail refinements — the tail's exact
    known values do the work that the false Lemma X′ was trying (wrongly)
    to abstract away.
  - Reuses (already certified, imported unchanged): Peeling Lemma
    (`lemmas/dominant-piece-lower-bound.md`), Element Bound (Lemma E, this
    file), Step 1's $j=1$ theorem as the base case of the recursion.

Open gaps: the Recursive Depth Peeling Lemma's precise statement and
induction (step 2–4 above) is **not yet proved** — this round's job is to
formalize and check it, especially the case $a_1<2^{m-1}$ (top fragment
does *not* dominate the tail's own top piece), which the lemmaX explorer
flagged as under-examined; also the bookkeeping when $j\ge2$ fragments of
$A$ interleave *among themselves* above level $m-d$ (not just $A$ vs. the
tail) needs a clean sub-argument (likely: sort $A$ internally first, since
all of $A$'s own fragments are known exactly once XY's split of the top
piece is fixed — this part is NOT abstract, it's given numbers).
Cases to cover: $a_1\ge 2^{m-1}$ vs. $a_1<2^{m-1}$ (i.e. whether the top
fragment dominates the tail's own top piece); $j'=0$ vs $j'\ge1$ (whether
the tail's own top piece is itself split); the recursion's base case
$m=0,1$ (already fully certified).
Watch out for: do not re-derive or lean on Lemma X′ in any form (confirmed
false, twice). Do not attempt the "merge fragments / reduce $j$" shortcut
(confirmed false at $m=4$). The numeric evidence (lemmaX explorer) shows the
worst case has $a_1$ only *slightly* above $2^{m-1}$ and the tail's own top
piece $s_1=2^{m-1}$ untouched — build and test the Recursive Depth Peeling
Lemma against exactly this configuration first, since it's the empirically
tight case.

---

greedy-reduction-geometric: revise (Lower-bound Case 2, narrowed scope)
Target: full lower bound $\mathrm{OddSum}(M)\ge c(n)$ for LB's geometric
construction, restricted this round to the **top-only-splitting**
sub-problem (all of XY's $\le n$ cuts land on the single top piece $r_n$,
tail $=\Gamma_{n-1}$ completely untouched) — a genuinely tractable,
self-contained sub-target identified by the `freshframing` explorer
(numerically solved exactly for $n=2,3,4$; exact known tail, no dual bound
needed). This is a real narrowing, not a full solve of Case 2 — the general
cut-reallocation reduction (why top-only WLOG covers everything) is
deliberately left to `dyadic-potential-invariant` this round, to avoid two
approaches duplicating the same monovariant proof.
Technique: direct peeling induction on the number of top-piece fragments
$j+1$, using the **exact, closed-form, untouched tail** $\Gamma_{n-1}$
(known prefix sums $2^{n-1},2^{n-2},\dots,1$) — no arbitrary refined
sub-multiset ever appears, so neither Lemma X′ nor any dual bound is
needed.

Skeleton:
  1. Fix $n$, and restrict to responses where $r_0,\dots,r_{n-1}$ are
     completely untouched and $r_n=2^n/(2^{n+1}-1)$ (unnormalized: $2^n$) is
     split into $j+1$ positive fragments $a_1\ge\cdots\ge a_{j+1}$,
     $j\le n$.
  2. Merge $A=\{a_1,\dots,a_{j+1}\}$ with the **exact known** tail
     $\Gamma_{n-1}=\{2^{n-1},\dots,1\}$ (unnormalized) and compute
     $\mathrm{OddSum}$ of the merge directly: since the tail's values are
     an explicit geometric sequence, the number of tail elements exceeding
     any given fragment value $a_i$ is computable in closed form (it's
     exactly $\lfloor \log_2(2^{n-1}/a_i)\rfloor+1$-type counting, or more
     simply: since tail values are $2^{n-1}>2^{n-2}>\cdots$, "how many tail
     elements exceed $x$" is a step function with $n$ breakpoints at the
     tail's own values) — use this to get an exact formula for
     $\mathrm{OddSum}(A\cup\Gamma_{n-1})$ as a function of the split point
     values $a_1,\dots,a_{j+1}$, piecewise linear with breakpoints at ties
     with tail values (reuse "Piecewise-concavity smoothing",
     `knowledge_base.md`).
  3. Show the piecewise-linear objective's minimum over the simplex
     $\{a_i>0,\sum a_i=2^n\}$ is $\ge2^n$ everywhere, by checking it face by
     face (a finite set of breakpoint configurations, by piecewise-linearity
     the minimum of a piecewise-linear function on a polytope is attained
     at a vertex/breakpoint of the arrangement) — this reduces the general
     continuous claim to a **finite check**, tractable by direct
     enumeration for the induction step (this is exactly what the
     `freshframing` explorer's numerics already did informally for
     $n=2,3,4$; the builder's job is to make the finite-check argument
     rigorous and general in $n$, e.g. by an explicit induction on $j$
     using the Peeling Lemma at each breakpoint).
  4. Conclude: top-only-splitting responses can never beat $c(n)$ for LB, for
     every $n$ and every $j\le n$.

Key lemmas (claim + mechanism):
  - **Exact-tail closed form.** Since the tail is *literally* $\Gamma_{n-1}$
    unrefined, $\mathrm{OddSum}(A\cup\Gamma_{n-1})$ is a fully explicit,
    computable function of $(a_1,\dots,a_{j+1})$ — because merging a
    variable set $A$ into a *fixed, known* sorted sequence only requires
    counting how many fixed elements exceed each $a_i$, which is elementary
    once the tail values are concrete numbers (not an unknown refinement).
  - **Peeling + Element Bound induction on $j$.** For $j=0,1$ this is
    already fully certified (Fact 2, Step 1 of `self-similar-induction-on-n`,
    directly importable). For $j\ge2$, peel $a_1$ (Peeling Lemma) and reduce
    to the same problem one level down with $j-1$ fragments (using the
    *known* tail minus whatever it has already contributed) — because the
    tail is exact and fixed throughout, this recursion never needs a
    lower bound on an unknown sub-multiset's EvenSum; it only ever needs
    arithmetic on known geometric values.

Open gaps: the finite breakpoint enumeration (step 3) needs to be made
rigorous and uniform in $n$ (not just checked for $n\le4$) — this is the
main builder task. Also: this closes only the top-only-splitting
sub-problem, **not** general Case 2 (cuts split across top piece and tail
simultaneously) — that reduction is `dyadic-potential-invariant`'s job this
round; state this scope limitation explicitly in the write-up so it isn't
overclaimed as closing Case 2 in full.
Cases to cover: $j=0,\dots,n$ (all fragment counts); the tie/breakpoint
cases (fragment exactly equal to a tail value) via the certified
Tie-neutrality block lemma.
Watch out for: do not claim this closes Case 2 in general — only the
top-only-splitting sub-case. Do not re-attempt the static "Q-priority"
strategy (confirmed dead end, round 2) or the "merging fragments" exchange
shortcut (confirmed dead end, this round).

---

dyadic-potential-invariant: revise
Target: same claim, lower-bound direction — specifically, prove the
**general reduction** that lets the whole population restrict attention to
top-only-splitting XY responses against LB's geometric construction (i.e.
supply the missing link between `greedy-reduction-geometric`'s tractable
top-only result above and full Case 2). This activates the field's most
distant, previously-idle (expanded: 0) approach with a concrete,
numerically-supported crux claim, replacing the vague, untested "local
split monotonicity" scaffolding from round 1 with the specific
**Cut-Reallocation Exchange Lemma** identified by the `freshframing`
explorer this round.
Technique: **monovariant/exchange argument** ("moving one unit of XY's
cut-budget from any tail piece to a self-similar cascade continuation of
the top-piece split never decreases $\mathrm{OddSum}$") — this *is* a
potential-style argument (consistent with this approach's original design)
but now stated as a concrete, checkable exchange inequality instead of an
abstract, unverified $\Phi$.

Skeleton:
  1. **First step, mandatory before any proof attempt (per this file's own
     round-1 "Watch out for"):** numerically stress-test the Cut-Reallocation
     Exchange Lemma directly (the `freshframing` explorer already did a
     first pass — extend it: try adversarial allocations that split *both*
     a top fragment and a tail piece simultaneously at various depths, for
     $n=3,4,5$, looking specifically for a violation). If a violation is
     found, kill this approach immediately and report the counterexample
     (per this file's own "Watch out for" instruction) rather than forcing
     a proof.
  2. If it survives testing: state the Exchange Lemma precisely. Let $M$ be
     any refinement of $\Gamma_n$ using $\le n$ cuts where some cut $c$ is
     spent splitting a tail piece $r_i$ ($i<n$) that is *not* on the current
     "self-similar cascade path" from the top (i.e. some ancestor level
     between $i$ and $n$ is still unsplit). Let $M'$ be the refinement
     identical to $M$ except that cut $c$ is instead spent extending the
     cascade one level closer to the top (splitting the nearest unsplit
     piece on the path from $r_n$ down to $r_i$). Claim:
     $\mathrm{OddSum}(M')\le\mathrm{OddSum}(M)$ (moving the cut toward the
     top is weakly better for XY / weakly worse for LB) — this is a
     monovariant on the *specific* geometric structure (dyadic ratio $2{:}1$
     between adjacent levels), not the false abstract Lemma X′.
  3. Prove the single-exchange-step inequality by direct case analysis on
     how the two pieces (old split location vs. new) interleave in the
     global sort — this is now a **local, two-piece** comparison (not a
     global arbitrary-multiset bound), tractable via the Peeling Lemma and
     the exact geometric ratios, in the same spirit as
     `self-similar-induction-on-n`'s Step 1 algebra.
  4. Iterate the exchange finitely many times (one per cut) to conclude any
     allocation is weakly dominated by a top-only cascade allocation, hence
     $\min_{XY}\mathrm{OddSum}$ over all allocations equals the minimum over
     top-only allocations — handing off directly to
     `greedy-reduction-geometric`'s result (once proved) to conclude Case 2
     in full.

Key lemmas (claim + mechanism):
  - **Cut-Reallocation Exchange Lemma** (crux, stated above) — because the
    geometric sequence's ratio-2 self-similarity means a cut "wasted" low in
    the tail only ever removes a small, dominated piece, while the same cut
    spent extending the top cascade removes mass from the piece(s) closest
    to becoming the new global max — the mechanism is a local
    domination/exchange swap, checkable case-by-case on adjacent levels
    only (finite local case analysis, not an infinite family of
    counterexample-prone abstract multisets).

Open gaps: the Exchange Lemma itself is entirely unproved (crux); step 1's
numeric stress test has **not yet been run this round** (this is the very
first concrete, checkable thing to do — top priority for the builder,
before investing in the proof). If it fails numerically, report immediately
and mark the approach a dead end rather than attempting a doomed proof.
Cases to cover: the single-exchange-step case analysis (step 3) needs every
relative-position case of the two moved pieces in the global sort (at
least: new piece becomes the global max / does not; old piece was tied with
something / was not).
Watch out for: this approach has been idle for 3 rounds (expanded: 0) —
CLAUDE.md's diversity rule requires it be built this round, at minimum
through the numeric stress test in step 1, even if the full proof is not
completed. Do not silently let it sit idle a 4th round.

---

universal-halving-adversary: revise
Target: the general upper bound $c(n)\ge$ (XY can always force
$\mathrm{OddSum}\le c(n)$) for **every** LB partition, all $n$ — this round,
close the $k<n+1$ (slack-budget) case completely via the new
Perfect-Pairing corollary, and make concrete progress on $k=n+1$ via the
recursive bisect-or-match pattern the `upperbound` explorer found.
Technique: **parity/pairing argument** (Perfect-Pairing: a multiset where
every distinct value has even multiplicity forces $\mathrm{OddSum}=1/2$
exactly, by the already-certified even-length-block Claim inside the
Doubling Lemma) for the easy case, plus a **recursive greedy bisect-or-match
algorithm** for the hard case $k=n+1$.

Skeleton:
  1. **Certify the Bisect-Everything / Perfect-Pairing Corollary (should be
     quick — this is "free" from already-certified lemmas per the
     `upperbound` explorer).** If $k\le n$ (LB did not use its full
     $n+1$-piece budget), XY spends $k\le n$ of its $n$ cuts to bisect every
     one of LB's $k$ pieces exactly in half. The resulting multiset has
     every distinct value in an even-multiplicity block (each original
     piece contributes exactly 2 copies of its own half-value; distinct
     original pieces may coincidentally produce equal half-values, which
     only merges blocks and preserves evenness). By the Doubling-Lemma
     Claim (already certified, `lemmas/doubling-lemma-and-generalized-
     duplicate-the-rest.md`) every even-length block splits exactly half to
     each player regardless of starting rank parity, so
     $\mathrm{OddSum}=\mathrm{sum}/2=1/2\le c(n)$ for every $n\ge0$ (since
     $c(n)=2^n/(2^{n+1}-1)>1/2$). This fully closes $k\le n$ for **every**
     $p_1$ — no case split on $p_1$ needed at all.
  2. **Consequence:** restate the remaining open upper-bound target as: for
     every $n$ and every sorted $p_1\ge\cdots\ge p_{n+1}>0$ summing to $1$
     (the full-budget case $k=n+1$ only), XY has a $\le n$-cut response
     forcing $\mathrm{OddSum}\le c(n)$.
  3. Formalize the **recursive bisect-or-match algorithm** (found
     numerically by the `upperbound` explorer across 4+ instances): process
     $p_1,\dots,p_{n+1}$ from the top; at each step, given the current
     largest still-unresolved piece $p_i$ and remaining budget $b$ and
     remaining tail $p_{i+1},\dots,p_{n+1}$ (sum $S_i$), choose between (a)
     "bisect $p_i$" (cost 1 cut, contributes $p_i/2$ toward
     $\mathrm{OddSum}$, recurse on the tail with budget $b-1$) or (b) "match
     $p_i$ against the tail" (Theorem-2-style: cost = number of tail pieces
     matched, contributes exactly the matched amount, recurse on the
     leftover). State the exact decision rule as a function of $p_i$ vs.
     $S_i$ (conjecturally: match when $p_i\ge S_i$ per Theorem 2, bisect
     when $p_i<S_i$, i.e. the same threshold that already governs Theorem
     2's applicability) and prove by induction on $n+1-i$ (number of pieces
     remaining) that this recursive rule always achieves
     $\mathrm{OddSum}\le c(n)$.
  4. Handle the near-equal-partition sub-case explicitly (flagged by the
     `upperbound` explorer as the case where "bisect-all-but-smallest"
     badly fails): show the algorithm's rule from step 3 naturally reduces
     to "bisect just one piece" when all $p_i$ are within a factor of $2$
     of each other (since then $p_i<S_i$ persists all the way down, the
     match branch is never taken except possibly once), matching the
     numeric finding that a single bisection already reaches the $1/2$
     floor there.

Key lemmas (claim + mechanism):
  - **Perfect-Pairing / Bisect-Everything Corollary** (step 1) — proved in
    full above from already-certified lemmas; promote as a standalone
    certified lemma this round (it is a genuine new closed sub-case, not
    just a sketch).
  - **Recursive bisect-or-match optimality** (step 3, crux, NOT yet proved
    — only observed to work on 4 hand-checked instances) — because at each
    level the choice between "self-pair" (bisect, guaranteeing exactly half
    of $p_i$ via the degenerate Doubling Lemma case) and "cross-pair"
    (match against the tail via Theorem 2, exactly $p_i$) mirrors the two
    extremal moves already proven individually; the open task is showing
    the *threshold* between them (and the recursive bookkeeping of leftover
    budget) is always sufficient, not just correct on examples.

Open gaps: step 3's recursive rule is a **conjecture verified on 4
instances**, not a proof — the induction (on number of remaining pieces)
needs to be carried out rigorously, including proving the budget accounting
never runs out (does "match" ever cost more cuts than remain?) and that the
threshold rule $p_i$ vs. $S_i$ is truly always optimal (not just optimal on
the tested examples) — this is the main open task, expected to take real
work, not a quick close.
Cases to cover: $p_i\ge S_i$ (match) vs. $p_i<S_i$ (bisect) at every
recursion level; budget-exhaustion edge cases (what if $b=0$ before the
recursion terminates — does the residual automatically satisfy the bound
via First-mover-half, Lemma B?); the near-equal-partition case (step 4).
Watch out for: do not assume "bisect-all-but-smallest" is a safe rule — it
is **confirmed refuted** this round for near-equal partitions (numeric
counterexample, $n=2$, $(0.336,0.333,0.331)$ gives $0.665\gg c(2)$). Also:
the doc's previous claim "no single-piece response suffices" for
$p_1>c(n)$ is **not fully accurate** — a single piece's own *further*
subdivision (not just one cut on it) can suffice without touching other
pieces (explorer's re-check of the $(0.6,0.35,0.05)$ example); do not
propagate the stronger "must touch two distinct pieces" claim as
established.

---

Build set recommendation: build all four this round —
`self-similar-induction-on-n` (Recursive Depth Peeling Lemma),
`greedy-reduction-geometric` (top-only-splitting sub-problem, closed
scope), `dyadic-potential-invariant` (numeric stress test + Cut-Reallocation
Exchange Lemma — first real investment after 3 idle rounds), and
`universal-halving-adversary` (certify Perfect-Pairing corollary for $k\le
n$ — should close quickly — then push the recursive bisect-or-match
induction for $k=n+1$). All four routes are now genuinely distinct
(recursive-depth induction / exact-tail peeling / cut-reallocation
monovariant / pairing-parity argument) and none depends on the disproved
Lemma X′ or the disproved merge-monotonicity shortcut.
