## imo-2026-03

self-similar-induction-on-n: revise
Target: the whole problem's lower-bound direction — Liu Bang's geometric
partition achieves $\ge c(n)=2^n/(2^{n+1}-1)$ against every refinement —
via the multiset-minimax reduction (`lemmas/reduction-to-multiset-minimax.md`)
reduced to $T(n)$/OddSum peeling induction. This revision targets the one
remaining open piece: $\mathrm{GT}(m)$ for $m\ge4$ (hence gap (a) of the
Branch-I.A-restricted window for $\ell\ge5$).
Technique: strong induction on $m$ via the certified Peeling/Rank-Shift
machinery (Monotonicity Reduction Lemma + Unified Threshold-Pair-Peeling
Lemma, `lemmas/monotonicity-reduction-and-unified-threshold-pair-peeling.md`),
now sharpened per this round's explorer into a single generalization:
replace the fixed target $2^k$ by a **variable target $V\le2^k$**
throughout Result 2's case split, and separately close the two named
residual sub-cases via a **filler-insertion reduction**.
Skeleton:
  1. Recall (certified): the case split on $q:=\#\{a_i\in D: a_i>2^{k-1}\}$
     collapses to $q=0,1,\ge2$; $q\ge2$ already closes unconditionally for
     *any* target $\le2^k$ (its bound $2^{k-1}\lceil q/2\rceil$ exceeds any
     such target with no change to the proof) — by the certified Rank-Shift
     Identity.
  2. **Prove the elementary corollary $0\le\mathrm{AltSum}(N)\le\max(N)$**
     for any multiset $N$ — immediate induction from the certified Peeling
     Lemma ($\mathrm{AltSum}(N)=\max(N)-\mathrm{AltSum}(\mathrm{rest})$, so
     $\mathrm{AltSum}(N)\ge0$ by induction forces $\mathrm{AltSum}(N)\le
     \max(N)$ too). Certify as its own one-paragraph lemma — it is the
     elementary fact the filler-insertion step needs and is not yet stated
     anywhere in `lemmas/`.
  3. **Filler-insertion reduction for sub-case (ii) (small-sum mirror),
     not-full-count instance ($|D|<m+1$).** Given $D$ with
     $\mathrm{sum}(D)<2^m$, $|D|\le m$: insert $f:=2^m-\mathrm{sum}(D)>0$ to
     form $D'':=D\cup\{f\}$, still with $|D''|\le m+1$ — so the
     already-certified boundary case of $\mathrm{GT}(m)$ ($m\le3$; general
     $m$ once step 5 below closes) applies directly, giving
     $\mathrm{OddSum}(D''\cup\Gamma_{m-1})\ge2^m$. By the certified
     Single-Insertion Lemma plus step 2's corollary,
     $\mathrm{OddSum}(D\cup\Gamma_{m-1})\ge\mathrm{OddSum}(D''\cup\Gamma_{m-1})-f
     \ge2^m-f=\mathrm{sum}(D)$ — closing this instance essentially for
     free, **conditional on the boundary case at the same $m$**, not
     circularly on the open case.
  4. **Full-count instance of (ii)** ($|D|=m+1$, no free slot for a
     filler): this is the ONE sub-sub-case with no known reduction to an
     already-closed regime. This round's explorer found strong numeric
     slack here (margins $1.04,2.58,5.66$ at $m=3,4,5$, vs. margin $\to0$
     exactly in the not-full-count case) — a genuine, non-tight residual,
     supporting a **direct** argument via the generalized (variable-$V$)
     Result 2 applied with $V=\mathrm{sum}(D)<2^m$ throughout its own
     $q=0,1,\ge2$ split (not a filler reduction): re-derive the $q=0$ and
     $q=1$ branches of the Unified Threshold-Pair-Peeling Lemma with the
     target $V$ threaded through the recursion in place of the fixed
     $2^k$.
  5. **Sub-case (i) ($q=1$, excess $e\ge1$, target $2^k-a_1$)**: covered by
     the SAME variable-$V$ generalization of step 4 (target
     $V=2^k-a_1<2^{k-1}$ this time) — steps 4 and 5 are literally one
     corollary of one generalized lemma, not two separate proofs. If the
     bare variable-$V$ recursion falls short by a small structured margin
     (as round 4's Case-A circularity did for fixed $V$), adapt the
     crux-corpus move from `aimo-0377` (strong induction on $m$ carrying a
     simultaneously-established companion bound, there $|g(n)|\le1$) —
     track an explicit companion slack bound through the induction rather
     than trying to close the bare inequality alone.
  6. Conclude $\mathrm{GT}(m)$ for all $m$; corollary: gap (a) of the
     shared window closes for all $\ell$, completing the lower-bound
     direction's Branch-I.A-restricted window in full generality.
Key lemmas (claim + mechanism):
  - $0\le\mathrm{AltSum}(N)\le\max(N)$ — because AltSum's own peeling
    identity ($\mathrm{AltSum}(N)=\max(N)-\mathrm{AltSum}(\text{rest})$)
    makes both bounds a joint induction on $|N|$.
  - Filler-insertion closes not-full-count small-sum instances for free —
    because inserting exactly the deficit $f$ reaches the sum-$2^m$
    boundary case (already certified for $m\le3$, targeted for general $m$
    here), and the Single-Insertion Lemma bounds the OddSum change by $f$
    itself, which cancels exactly against $f$ in the target inequality.
  - Variable-$V$ Rank-Shift Identity — because the $q\ge2$ branch's proof
    bound $2^{k-1}\lceil q/2\rceil$ never used $V=2^k$ specifically, only
    $V\le2^k$; only the $q=0,1$ branches' arithmetic (currently written
    assuming $V=2^k$ exactly) needs re-deriving with $V$ as a free
    parameter $\le2^k$.
Open gaps: full-count instance of (ii) (step 4) and sub-case (i) (step 5)
— both reduce to ONE not-yet-derived variable-$V$ generalization of
Result 2's $q=0,1$ branches; the `aimo-0377`-style companion-bound fallback
is untried if the bare version falls short.
Cases to cover: $q=0$, $q=1$ (both under variable $V$); $q\ge2$ already
closed for any $V$ (no new work needed there).
Watch out for: do NOT attempt "merge the two smallest elements of a
full-count $D$" as a bridge to the not-full-count case — numerically
refuted this round (20000 trials, ~10% of cases move the wrong direction,
no uniform sign). Re-verify the variable-$V$ Rank-Shift Identity's $q\ge2$
branch really is $V$-independent before citing it (don't just assume the
old fixed-$V$ proof transfers verbatim — check the inequality direction
explicitly for $V<2^k$).

global-lp-vertex-sufficiency: revise
Target: the whole problem's upper-bound direction — no partition beats
$c(n)$, i.e. $V(p)\le c(n)$ for all $p$ — via the LP/compactness +
finite-hyperplane-arrangement reduction (Global Vertex Lemma, Lipschitz
continuity, Finite-Cell Affine-Vertex Reduction, all certified) reducing
the Existence Theorem to checking $V(q)\le c(n)$ at a finite candidate
vertex set $Q=Q_{\mathrm{region}}\cup\Sigma$-shapes. $Q_{\mathrm{region}}$
is fully closed; this revision targets the residual $\Sigma$-shape part
via a **re-scoped, weaker, n-dependent construction target**, per this
round's explorer's key correction to round 11's premise.
Technique: explicit multi-piece fragment-vs-fragment tying construction,
n-dependent in size (not a fixed bounded tool), directly clearing $c(n)$
at the hard vertices (starting from $e_0$, the already-numerically-hardest
point) — reframing the target from "does a bounded/named construction
family suffice" (refuted, Mass-Constraint Theorem) to "does SOME
explicit, closed-form, $n$-dependent construction suffice" (NOT yet
refuted — this is the load-bearing correction this round).
Skeleton:
  1. **State the corrected target explicitly** (mandatory first step, a
     textual/scoping fix before new math, per the round-11 rule about
     putting a found inconsistency first): the Mass-Constraint Theorem
     (round 11) and this round's independent numeric re-confirmation
     (minimal clearing split-count $s^*$ grows with $n$, $s^*\sim n/2$)
     rule out only a FIXED, $n$-independent $s_0$ — they say nothing
     about whether an explicit construction whose size legitimately grows
     with $n$ (using up to $n$ cuts, the full budget) can close the
     Existence Theorem for every $n$. Revise Section 4.5/4.6.5's framing to
     state this explicitly as the real remaining target, not a
     "deprioritized, soft-negative-signal" lead.
  2. **Cheap-kill / mandatory numeric gate**: before any proof effort, test
     the "pairwise-tie chain" construction (chain-tie fragments of
     DIFFERENT split pieces to each other in a cycle, using $\sim n/2$
     cuts) against $V(p)$ at the genuinely hard interior points (not just
     $e_0$, which is a region vertex already closed) for $n=3,\ldots,6$ —
     per the explorer's own recommended cheap-kill and the repo's
     mandatory-numerical-stress-test rule. If it fails broadly, do not
     write it up as a lemma attempt; report as a negative finding and try
     the next natural fragment-vs-fragment family (e.g. tie each split
     piece's smaller fragment to the next split piece's larger fragment,
     descending).
  3. If a chain-tie (or similar) construction survives the cheap-kill:
     **generalize the certified Singleton-Interleaving Lemma
     (`lemmas/singleton-interleaving-and-k-anchor-merge.md`) to chain-tie
     fragments from different split pieces to each other** (not to whole
     untouched pieces, so the Mass-Constraint obstruction's hypothesis
     genuinely does not apply) — derive an exact closed-form OddSum value
     for the chain construction as a function of $n$ and the tie pattern.
  4. Prove the closed form is $<c(n)$ (or $\le c(n)$, matching the
     Existence Theorem's non-strict direction) for all $n$ and all points
     $p$ in the balanced region — likely via the same rank-shift/AltSum
     peeling machinery already certified for the lower-bound side (a
     cross-approach import: an explicit chain construction's OddSum is
     itself a $D\cup\Gamma$-shaped multiset sum, amenable to the same
     Peeling Lemma family self-similar-induction-on-n uses).
  5. Conclude: for every $n$ and every $p$ in the residual $\Sigma$-shape
     region, the explicit construction proves $V(p)\le c(n)$, completing
     the Existence Theorem and hence the whole upper-bound direction.
Key lemmas (claim + mechanism):
  - $Q_{\mathrm{region}}$ closed, only $\Sigma$-shapes remain — already
    certified (Region-Vertex Classification + Boundary Continuity +
    $k$-Anchor-Merge), imported unchanged.
  - Chain-tie construction avoids the Mass-Constraint obstruction —
    because that theorem's hypothesis (split fragment tied to a WHOLE
    untouched piece, forcing $\ge1/2$ mass) simply does not apply when
    fragments are tied to OTHER fragments; the growing-$s^*$ numeric
    finding is consistent with, not contradictory to, an $n$-dependent
    construction using the full $n$-cut budget.
Open gaps: steps 2-4 in full — the cheap-kill has not yet been run this
round (mandatory before any proof effort per repo rule); no closed form
has been derived yet for any chain-tie family.
Cases to cover: none yet (single construction family to test first); if
it fails, the two next candidate families are "descending fragment
chain" and a direct LP-duality certificate at $q$ (mentioned but untested
by this round's explorer) — try in that order if step 2 kills the first.
Watch out for: do NOT re-attempt any exchange-argument variant (region-side
or response-side, single-choice or existential) for the endpoint-inequality
bypass — confirmed dead at $n=3$ by two independent rounds (12, 13). Do NOT
treat the growing-$s^*$ finding as evidence against this revised target —
that finding only refutes a BOUNDED $s_0$, and $s^*\sim n/2$ is well within
the $n$-cut budget.

greedy-reduction-geometric: advance
Target: same lower-bound direction as self-similar-induction-on-n (the two
approaches share the closed Branch-I.A-restricted window at $\ell=1..4$
via the Window Reduction Theorem + GT(m) combination). All of this
approach's own residual work (gap (b), the window's monotonicity
direction) is fully closed; its only remaining open piece is identical to
self-similar-induction-on-n's GT(m), $m\ge4$ gap, via the proved Theorem N
equivalence (round 11). No new independent build needed this round beyond
standing by to cross-check self-similar-induction-on-n's variable-$V$
generalization once produced (the equivalence means a closure there is a
closure here too, and vice versa) — advance without new dispatched content
unless the builder finds an independent angle on the shared residual.
Skeleton: (unchanged from round 12-13; see approach file for the full
Window Reduction Theorem / Theorem N chain.)
Key lemmas: already certified (Window Reduction Theorem, Elementwise
Monotonicity, Theorem N equivalence to Branch-I.A window).
Open gaps: identical to self-similar-induction-on-n's GT(m), m>=4 gap (via
the proved Theorem N equivalence) — not a separate gap.
Cases to cover: none new.
Watch out for: do not duplicate build effort on GT(m) here AND on
self-similar-induction-on-n in the same round for the same sub-case —
if a builder is dispatched to this slug, have it look for an
independent angle (e.g. a direct greedy-side argument bypassing GT(m)
entirely) rather than re-deriving the identical variable-$V$ result.

lp-duality-split-polytope: advance
Target: same upper-bound direction as global-lp-vertex-sufficiency,
approached via the triangular-family / general fragment-vs-fragment tie
construction at $e_0$ specifically (a complementary, independent-technique
angle: exact-arithmetic brute force over active-set choices rather than
LP/hyperplane-arrangement machinery). Its Perfect-Tie-Family Exact
Characterization Theorem (certified) is a second, disjoint-technique
negative result confirming (independently of the Mass-Constraint Theorem)
that no fixed $s_0$ suffices at $e_0$ — directly corroborating this
round's reframe of global-lp-vertex-sufficiency's target as $n$-dependent.
Advance to attempt the general nonzero-residual fragment-vs-fragment
family (flagged open since round 12: "numeric hint that nonzero residual
helps but insufficient evidence yet") — this is a natural, disjoint
stepping stone toward the same chain-tie construction
global-lp-vertex-sufficiency is now targeting, worth pursuing in parallel
with its own exact-arithmetic toolkit (Integer-AltSum Lower Bound Lemma)
rather than duplicating the LP-vertex builder's numeric search.
Skeleton: (unchanged from round 12; see approach file.)
Key lemmas: Integer-AltSum Lower Bound Lemma, Perfect-Tie-Family Exact
Characterization Theorem (both certified).
Open gaps: general nonzero-residual fragment-vs-fragment family at $e_0$
— does more residual (non-perfect-tie) genuinely help, and by how much,
as a function of $n$?
Cases to cover: none yet enumerated; first task is the numeric
characterization of how residual size trades off against required $s$.
Watch out for: keep this exact-arithmetic route genuinely distinct from
global-lp-vertex-sufficiency's chain-tie numeric search — cross-check
results at the end of the round rather than merging the two builds.

## Decision on the proposed discharging/charge-conservation plateau-break

NOT opened this round. The plateau-fresh explorer's diagnosis (both
remaining gaps are "the same unbounded case-growth wall") is a real and
useful structural observation, but this round's other two explorers found
concrete, independently-verified, NEW mechanisms on each gap that had not
been tried before and are not obviously doomed by the same wall:
  - the GT(m) explorer found the two named sub-cases collapse to ONE
    variable-$V$ generalization of an already-certified lemma (not another
    case-split variant — a genuine architecture simplification with a
    concrete completion path), plus a decisive numeric finding
    (full-count residual has REAL slack, 1-5.7, unlike the knife-edge
    not-full-count case) suggesting this sub-case is not part of the
    "unbounded case growth" pattern at all;
  - the LP-vertex explorer found the "growing $s^*$" finding was being
    misread as a dead end when it is actually consistent with an
    untested, weaker, correctly-scoped target ($n$-dependent construction,
    not bounded $s_0$) — this is precisely a case where the perceived
    "wall" was a mis-scoped target, not a genuine obstruction, resolved by
    re-reading the existing evidence rather than needing a new mechanism.
Per the dispatch's own instruction to weigh the plateau argument against
real independent progress: both gaps saw genuine, verified NEW mechanisms
open up this round (not just narrower framings of the same closed door),
which cuts directly against "true 2+ round plateau with no viable next
move." The discharging idea itself is also flagged by its own author as
needing mandatory early numerical falsification and has two structurally
similar documented dead ends in its own family (Cut-Reallocation Exchange,
layer-cake per-cut additivity) — a real but not urgent lead. Recommendation:
hold the discharging approach in reserve. If BOTH of this round's two
concrete revisions above stall again next round (i.e. the variable-$V$
generalization and the chain-tie cheap-kill both fail), open it then as a
genuine third-mechanism plateau-break, with the numeric falsification of
a rank-scaled weight $w(v,s)=v\cdot2^{-|\log_2 v-s|}$ as its own mandatory
first step.

## Build set

self-similar-induction-on-n, global-lp-vertex-sufficiency, lp-duality-split-polytope

(greedy-reduction-geometric held out of this round's build set — its
residual gap is proved identical (Theorem N) to self-similar-induction-on-n's
GT(m) gap; re-dispatch it only if self-similar-induction-on-n's builder
reports the variable-$V$ generalization stalls and a fresh greedy-side
angle is worth trying independently.)
