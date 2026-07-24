# Round 25 proof review — imo-2026-03

Reviewed all 3 built slugs against the problem, `knowledge_base.md`'s and
`CLAUDE.md`'s rigor rules, and `/tmp/round-25/proof-outliner.md` /
`outline-reviewer.md`. Every load-bearing new claim below was
independently re-derived with fresh scripts (not the builders' own):
`/tmp/round-25/verify_theorem39.py`, `/tmp/round-25/verify_farkas.py`,
`/tmp/round-25/verify_coverage2.py`.

## 1. greedy-halving-adversary

**Verdict: CHANGES REQUESTED. True Status: partial** (file's own header
already says `partial`, correctly).

**What's genuinely correct and new, independently verified:**
- **Proposition 39** (Mass-Conservation Obstruction): proves the
  outline's "h(m) as a disguised corollary of $(\star_{n-4})$ via literal
  substitution" idea is false, via a clean injectivity argument (total
  mass of $\{c\}\cup S$ is strictly increasing in $c$, but any fixed
  target ladder has fixed total mass, so at most one $c$ can match). Also
  correctly diagnoses the unique exception ($c=q_1$, Claim (II)'s
  vertex). Elementary, hand-checked, no gap.
- **Theorem 39**: full unconditional closure of $h(2)\ge f(2)$
  (extending the "$T'$-cuts-$p_4$" sub-case from $n=5$ to $n=6$) by a
  direct, exhaustive, piecewise-linear-in-$c$ sweep over the whole
  interval $c\in(0,4]$, across each of the 4 exhaustive branches of $S$'s
  single available cut ($q_1$-, $q_2$-, $q_3$-split, untouched). I
  independently re-derived every one of the closed-form pieces by hand
  and re-checked them against 6000+ dense random exact-`Fraction` samples
  inside each open sub-interval (zero mismatches), plus a 40,000-trial
  randomized search confirming the reported minima ($1$ for $q_2$-split,
  $3-2z$ for $q_3$-split). Crucially, Theorem 39's technique is a *full
  continuum sweep*, not a vertex-restricted argument, so it is not
  subject to the "deep-tie" gap that plagues Theorem 37 — a real,
  qualitatively stronger closure than a naive vertex enumeration would
  give.

**The overclaim (real, not cosmetic).** The file's "Open gaps" section
states: "Combined with Theorem 37 (unconditional for $n\le6$), Case (b)'s
whole 'v≥a' branch is now fully, unconditionally closed at $n=6$ as well
as $n=5$." This is **exactly** the overclaim the round-24 proof-reviewer
already found and downgraded for $n=5$ (see `current.md`'s round-24
entry): Theorem 37 (which covers the complementary "$T'$-untouched"
sub-case, $b=p_4$) explicitly states in its own text that it establishes
only *one* vertex of that sub-case's family and does not rule out $b$
tied to a non-maximal element of $T''$ being the true global minimizer.
That gap is unaddressed by this round's work (which focused entirely on
the disjoint "$T'$-cuts-$p_4$" sub-case). The file simply repeats the
identical combined claim, now extended to $n=6$, without fixing Theorem
37's own gap. This is a genuine repeat of a flaw already on record, not a
new discovery — flagging again so it is not silently re-approved.

**Action taken:** certified Theorem 39 and Proposition 39 as standalone
lemmas (`lemmas/theorem-39-h2-closure.md`,
`lemmas/proposition-39-mass-conservation-obstruction.md`), each with an
explicit scope warning that they do **not** license the "whole branch
closed" claim. `current.md` updated to downgrade that specific claim
again (n=6, not just n=5) and to recommend Theorem 37's own gap as next
round's actual target for this slug.

## 2. lp-duality-certificate

**Verdict: CHANGES REQUESTED. True Status: partial**, despite the file's
own header claiming `solved` (scoped to "n=3"). This is a real overclaim
that must be corrected, not just noted.

**What's genuinely correct and new, independently and rigorously
verified (the highest-value result this round):**
The 5-chamber family $\{\mathrm{Bisect}\{1,4\},\mathrm{Bisect}\{1,2\},
\mathrm{DS\text{-}Above},\mathrm{Triple\text{-}Pin},\mathrm{R22.1.1}\}$
provably covers case (b2)'s box at $n=3$, in exact rational arithmetic:
- Re-derived all five chambers' failure/feasibility inequalities from
  their $\Phi_\tau$ closed forms via `sympy.Rational` symbolic algebra —
  every one of the six stated equivalences ($g_{14}<0\iff\cdots$, etc.)
  checks out exactly.
- Re-verified all six Farkas-style infeasibility certificates
  independently from scratch: for each of the six branches
  $(X,P1),(X,P2),(X,Q),(Y,P1),(Y,P2),(Y,Q)$, the claimed nonnegative
  combination's left-hand sides cancel to exactly $0$ and right-hand
  sides sum to exactly $0$, with at least one strictly-weighted
  constraint in each — a valid, hand-checkable proof of infeasibility
  for all six (`/tmp/round-25/verify_farkas.py`). Two of the six
  certificates ($(Y,P1)$, $(Y,P2)$) turn out to prove something even
  stronger than needed (they don't even need $g_{14},g_{12}$), which is
  extra robustness, not an error.
- Fresh independent random sampling (23,880 valid exact-`Fraction`
  points inside the open box, `/tmp/round-25/verify_coverage2.py`): zero
  uncovered points, corroborating the exact proof.
- Directly verified the boundary-vertex resolution: at
  $p^\ast=(2/5,4/15,1/5,2/15)$, $p_1=2p_3$ and $p_2=p_3+p_4$ exactly, so
  R22.1.1 is feasible there with $g_{R22}=0$ exactly (a genuine tie, not
  a failure) — confirming no separate boundary disposal step is needed.

This is a genuine, complete, non-numeric proof of case (b2)'s covering
closure, and I certify it as `lemmas/case-b2-n3-covering-closure.md`.

**The overclaim (the reviewer's most significant finding this round).**
The file's own top-level conclusion states: "combined with the
already-closed case (a) ($p_1\ge T/2$) and case (b1) ($p_2\le T/D_3$)
regimes, this completes the general upper bound $c(3)\le8/15$ for every
legal Liu Bang marking at $n=3$" and upgrades Status to `solved` for the
$n=3$ scope. This is **not established as written**. The approach file
itself, in two other places (near line 100 and lines 2420-2431), defines
"case (a)" as a **different** region — $p_2\ge a_3T/2$ *with* $p_1<T/2$
— disjoint from and not subsumed by "$p_1\ge T/2$". R25.1's final
paragraph mislabels/conflates this with $p_1\ge T/2$ and never actually
cites or re-invokes the mechanism that closes it
(`generalized-peel-identity`/Theorem B$_k$, conditional on the
already-fully-closed $c(2)=4/7$ bound). I confirmed this is a real
uncovered gap in the region, not just semantics: a fresh 500,000-trial
random search over $\{p_2\ge a_3T/2,\ p_1<T/2\}$ found the 5-chamber
family fails at many points (e.g. near $(0.45,0.30,0.15,0.10)T$, all
five chambers fail or are infeasible there). I separately spot-checked
that Theorem B$_k$ ($k=2$) genuinely rescues this specific witness
(peeling $p_1$ against $p_2$ reduces to a 3-element tail whose
$\Phi\le\frac47\cdot\mathrm{Total}$ bound is already unconditionally
established by $c(2)=4/7$, giving $\Phi_{\mathrm{combined}}\le8/15$
there) — so the underlying mathematical claim is very likely still true,
but this round's write-up did not assemble or cite it. **The "n=3 fully
solved" claim must be downgraded; case (b2)'s own closure stands.**

**Action taken:** certified `case-b2-n3-covering-closure` with an
explicit scope warning; `current.md` NOT advanced to any "n=3 solved"
milestone; flagged the precise citation fix needed for next round.

## 3. rank-pigeonhole-budget

**Verdict: CHANGES REQUESTED. True Status: partial for the (7.9.1)
sub-target** (file header correctly says `solved`, but explicitly and
consistently scoped to Claim (A) alone — unchanged since round 8, no
overclaim found anywhere in this file this round).

**What's genuinely correct, independently checked:**
- Correctly diagnosed that the outline's proposed Restriction Lemma does
  not literally apply as a 1-dimensional reduction (which tail element
  ends up cut is exactly the open content, not something a single-element
  vertex polytope can decide in advance) — an honest, load-bearing
  correction to the outline rather than a forced attempt to make it work.
- New **MinFloor$(\ell)$/MaxCeil$(\ell)$ joint reduction**: (7.9.1) is
  shown exactly equivalent to MaxCeil$(m)$, $m=n-3$ (equivalently
  $E(S)\ge\sigma_1/2$, via the identity $A=Total-2E$ plus the
  already-certified ratio-2 identity $R(\sigma)+\sigma_\ell=2\sigma_1$ —
  I re-derived this identity directly, trivial geometric-series algebra,
  confirmed exact). MaxCeil$(\ell)$'s "top untouched" branch reduces
  exactly to MinFloor$(\ell-1)$; MinFloor$(\ell)$'s own "top untouched"
  branch is closed unconditionally for every $\ell\ge1$ via one line
  (the already-certified Fact 2, $A\le\mathrm{Total}$, plus the
  identity) — I re-checked this argument and it is correct and genuinely
  general.
- Caught and corrected its own direction/polarity error mid-round (an
  earlier draft tried to close MaxCeil's branch via Fact 2 directly and
  found it supplies the wrong-direction bound) — exactly the kind of
  self-correction this project's rigor rules ask for, done honestly
  before finalizing.
- Both quantities' "top element is cut" branches are honestly left open
  for general $\ell$ (only hand-verified consistent at $\ell\le3$, not
  proved) — matches the file's own Status text precisely, no discrepancy
  found.

**No overclaim found in this file this round.** (7.9.1) remains open;
this is real, honestly-scoped narrowing progress, not a closure.

## Certified lemmas (written to `results/imo-2026-03/lemmas/`)

- `theorem-39-h2-closure.md` (certified, with scope warning)
- `proposition-39-mass-conservation-obstruction.md` (certified)
- `case-b2-n3-covering-closure.md` (certified, with scope warning)

## `current.md` update

Updated `## Status` remains `partial` (unchanged — correct, since neither
the general upper bound nor the general lower bound is established).
Appended a full Round 25 entry recording: (1) the two certified
greedy-halving-adversary lemmas and the reiterated Theorem-37 gap; (2) the
case (b2) covering-closure milestone and the precise missing-citation gap
in the "n=3 fully solved" claim; (3) rank-pigeonhole-budget's honest
partial progress on (7.9.1). Explicit recommendations recorded for next
round on both open citation/gap items.

## Outcomes recorded via `record_outcome`

- `greedy-halving-adversary`: partial — "Theorem 39/Proposition 39
  correct and certified (h(2)≥f(2) fully closed, T'-cuts-p4 sub-case now
  closed at n=6); but file's 'whole v≥a branch closed at n=5/n=6' claim
  repeats round 24's already-flagged overclaim (Theorem 37's own
  non-maximal-tie gap still unaddressed)."
- `lp-duality-certificate`: partial — "6 Farkas certificates for case
  (b2)'s box at n=3 independently verified exact and correct (genuine
  milestone, first non-numeric n=3 sub-case covering-family closure); but
  file's 'n=3 fully solved' claim overclaims — omits/mislabels the
  distinct case-(a) region p2≥a3T/2∧p1<T/2, confirmed by fresh 500k-trial
  search that the 5-chamber family alone doesn't cover it."
- `rank-pigeonhole-budget`: partial — "(7.9.1) reduced to a clean
  MinFloor/MaxCeil joint statement; one full branch (MinFloor's top-
  untouched) closed unconditionally for every ℓ; both 'top element cut'
  branches honestly left open; no overclaim, self-corrected a polarity
  bug mid-round."
