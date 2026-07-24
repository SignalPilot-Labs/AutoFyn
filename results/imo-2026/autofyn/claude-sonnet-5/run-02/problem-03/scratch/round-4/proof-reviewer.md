# Round 4 proof-reviewer report — IMO-2026-03

Reviewed all 5 built slugs: `rank-pigeonhole-budget`, `rank-tie-vertex-reduction`,
`greedy-halving-adversary`, `smoothing-compactness-certificate`,
`claiming-order-invariant`. Also certified 5 newly-proposed lemma files.
All numeric/algebraic claims below were independently re-derived with exact
`Fraction`/`sympy` arithmetic (scripts run live in this review, not trusted
from the builders' own scripts) — see verification snippets embedded per
claim. Overall Status remains `partial`: n=1, n=2 fully closed both
directions; general n still open on both directions, but the field made
real, verified progress narrowing the remaining gap this round.

## Per-slug verdicts

### 1. rank-pigeonhole-budget — CHANGES REQUESTED
New "sharp dominant-removal identity" ($A(\{f_1\}\cup T)=f_1-A(T)$ whenever
$f_1>\max(T)$, strictly weaker hypothesis than the certified
`dominant-element-removal-identity`'s $f_1>\mathrm{Total}(T)$) is proved
correctly (integral-splitting argument, re-derived line by line) and
independently re-verified: 20000 random-trial exact-Fraction check, zero
mismatches; witness $T=\{1^{11}\}, f_1=10$ reproduced exactly
($A(T)=1$, $A(\{10\}\cup T)=9=10-1$). Used to collapse Proposition 10's
Case A to one inequality $(\star)$: $A(F'\cup G')\le f_1-a_n$.

Honest, verified negative finding: the natural "generic multiset /
even-rank-sum dominates total" pigeonhole restatement of $(\star)$ is FALSE.
Re-ran the counterexample independently: $F'=\{10\}$, $G'=\{1^{11}\}$,
merged+sorted even-rank sum $E=6 < 10=\mathrm{Total}(F')$ — confirmed
exactly. This is a real, useful negative result (rules out an entire class
of naive proof attempts), correctly not overclaimed as closing anything.

Case B ($f_1\le r$) is correctly identified as numerically coinciding with
the already-open $c=n$ minimality obstruction from `self-similar-bracketing`
(Prop. B2) — no new gap invented, no double-counting.

Gap remains: $(\star)$ itself is unproved for general $n$. Genuine partial
progress, real new lemma, honest reporting throughout. New lemma
`sharp-dominant-removal-identity` **CERTIFIED**.

### 2. rank-tie-vertex-reduction — CHANGES REQUESTED
Round-4 outline asked to prove "every prefix length $k\in\{0,\dots,n\}$ of
the cascading-halving family hits the target" — this build correctly
refuted that (exact-Fraction check before any proof attempt) and replaced
it with the true, narrower, fully proved **Cascading-Halving-Family
Theorem**: $D\cdot A(S_k) = T(L) = (2^{L+1}+(-1)^L)/3$ ($L=n-k$), so
$A(S_k)=f(n)$ iff $L\in\{0,1\}$ i.e. $k\in\{n-1,n\}$, strict inequality for
every $L\ge2$.

Independently re-derived and re-verified this closed form by direct
Fraction computation of $T(L)$ for $L=0,\dots,11$ against both the formula
and a from-scratch construction of $S_k$ for $n=1,\dots,8$ (all $k$) —
exact match throughout, including cross-checking the multiplicity
bookkeeping (Step 1) directly against the raw multiset rather than trusting
the Odd-Run-Reduction shortcut alone.

This is genuine new general-$n$, non-numeric progress (an infinite family
fully characterized in closed form), building correctly on round 3's
already-certified Vertex-Minimum Theorem and Odd-Run Reduction Lemma (both
re-inspected this round; no defects found, no re-certification needed as
their proofs were already checked in round 3). The general tie-vertex
enumeration (cross-ties, non-prefix subsets) remains open, honestly scoped.
New lemma `cascading-halving-family-characterization` **CERTIFIED**.

### 3. greedy-halving-adversary — CHANGES REQUESTED
Found and fixed a genuine, previously-unfilled gap in its own Proposition
10: the case $f_1\le r$ was promised but never written out. Lemma 10 fills
it via a direct instantiation of the certified `cross-term-identity-
threshold` (correct, no new hypothesis introduced).

New Lemma 11 (tail self-similarity: $\{p_2,\dots,p_{n+1}\}/r$ is exactly the
$(n-1)$-ladder) and Lemma 12 ($r\cdot f(n-1)=a_n$) are elementary
closed-form algebra — re-derived from scratch and independently
cross-checked by exact Fraction arithmetic for $n=1,\dots,8$: exact match.

Proposition 13 (symmetric $c=1$ split gives $\Phi\ge p_1$ against any legal
tail refinement, conditional on the same lower bound one level down): the
proof chain was re-derived step by step (equal-fragment parity cancellation
$\Rightarrow$ cross term vanishes $\Rightarrow$ reduces to bounding
$A(G')$ via the rescaled $(n-1)$-ladder). Independently re-verified the
$n=3$ conclusion with a 200,000-trial exact-Fraction random search over
legal tail refinements at the symmetric split: minimum $\Phi$ found was
exactly $8/15=p_1$, matching the theorem exactly and never violated. Since
$c(2)=4/7$'s lower bound is already fully certified (rounds 1-2, no
numerics), the $n=3$ instance of Proposition 13 is correctly claimed as
unconditional; for $n\ge4$ it is honestly scoped as a conditional recursive
reduction, not a new unconditional base case — this framing is accurate,
not overclaimed.

Honest negative finding on asymmetric $c=1$ splits: the natural
derivative-in-imbalance argument is shown (correctly) not to be
sign-definite, with a concrete localized numeric witness of the
cross-term/tail-suboptimality trade-off. Correctly flagged as evidence, not
proof.

New lemmas `tail-self-similarity` and `symmetric-split-c1-lower-bound`
**CERTIFIED**.

### 4. smoothing-compactness-certificate — CHANGES REQUESTED
General-$n$ Cascade Achievability Theorem: a fully general, non-numeric
proof (direct rank-position count, no induction) that the two boundary
cascading responses ($k=n-1,n$) achieve $\Phi=a_n$ exactly for every $n$.
Independently re-derived and re-verified for $n=1,\dots,8$ by direct
exact-Fraction sort-and-alternate-sum computation on the explicit
multisets — all 16 cases (both $k$ values, 8 values of $n$) match $a_n$
exactly. This is a genuinely different (and independently obtained) route
to essentially the same achievability fact `rank-tie-vertex-reduction`
reaches via the Odd-Run-Reduction Lemma — a valuable cross-check between
two independently-built approaches with an exact match on overlapping
claims.

Honest, verified negative finding: attempted to generalize the $n=2$
six-template + LP-contradiction upper-bound mechanism to $n=3$ and found a
concrete counterexample where the 6 direct-analog templates all fail. I
independently recomputed this exactly: at $(p,q,r,s)=(3/8,1/4,1/4,1/8)$,
templates T1,T2,T3,D2 give $\Phi=9/16$ and D1,D3 give $\Phi=11/16$ (both
$>8/15$, matching the file exactly), while trisecting $p$ equally gives
$\Phi=1/2<8/15$ (also matches exactly) — so there is no actual violation of
the upper bound at this point, but the 6-template family alone cannot
certify it, and further numerical search shows the true optimal split of
$p$ is configuration-dependent, not a fixed closed form. This is a real,
useful negative result, correctly scoped as "the upper-bound generalization
is genuinely open at $n=3$, harder than the round-3 sketch anticipated" —
not glossed over or hidden.

New lemma `general-n-cascade-achievability` **CERTIFIED**.

### 5. claiming-order-invariant — RETHINK
New slug (copied from `self-similar-potential-certificate`) attempting an
`aimo-0117`-style "defer commitment" claiming-order invariant. The approach
gives a genuinely structural (not just "we tried and failed") argument for
why this cannot work: `aimo-0117`'s mechanism needs a multi-round adaptive
loop (Jesse and Tjeerd alternate single moves over many rounds) to give the
invariant content; this problem's marking stage is a one-shot Stackelberg
game (Liu Bang commits all marks, then Xiang Yu commits all marks, no
further round), and the claiming stage — the only genuinely sequential part
— is already fully determined by the certified `claiming-subgame-reduction`
(greedy claim is forced, no strategic freedom left for an "order invariant"
to encode).

This diagnosis was confirmed by a concrete numeric check (re-traced by
hand): the outline's candidate invariant fails already at the very first
claim against the on-file $n=3$ vertex example ($4 < 4$ is false, not a
strict inequality), and even where it holds later, it is shown to be a
trivial consequence of the multiset already being sorted, unable to
distinguish an optimal $S$ from a non-optimal one. No repair is proposed,
which is correct given the structural diagnosis rules out any invariant of
this shape, not just the specific candidate tested.

This is Status `unsolved` in the approach's own file, correctly. Per the
routing rule, a framing shown to be structurally unable to work is a
RETHINK, not a CHANGES-REQUESTED-with-gap: there is no partial correct
progress to build on within this framing, only a valuable, well-argued
negative result recorded so it is not re-attempted. Recommend the outliner
not re-open a claiming-order framing; if the crux-corpus alt-framing idea
is pursued further, target invariants over the one-shot marking stage
instead (as the approach itself suggests, pointing at
`rank-pigeonhole-budget`).

## Lemma certifications this round

All 5 newly-proposed lemma files independently re-verified (proofs
re-derived by hand, numeric claims re-run with exact `Fraction` arithmetic,
not trusted from the builders' scripts) and **CERTIFIED**, with
certification notes appended to each file:
- `lemmas/sharp-dominant-removal-identity.md`
- `lemmas/tail-self-similarity.md`
- `lemmas/symmetric-split-c1-lower-bound.md`
- `lemmas/cascading-halving-family-characterization.md`
- `lemmas/general-n-cascade-achievability.md`

No defects found in any of the five; no false or overclaimed statements
detected in any of the round-4 write-ups. All negative/honest-gap findings
this round were independently re-verified and confirmed genuine (not
artifacts of a builder's bug).

## Outcomes recorded (mcp__approach-ranker__record_outcome)

- `rank-pigeonhole-budget` → advanced ("CHANGES REQUESTED", new certified
  lemma + honest counterexample)
- `rank-tie-vertex-reduction` → advanced ("CHANGES REQUESTED", new
  general-n closed-form theorem)
- `greedy-halving-adversary` → advanced ("CHANGES REQUESTED", gap fixed +
  new unconditional n=3 sub-case)
- `smoothing-compactness-certificate` → advanced ("CHANGES REQUESTED", new
  general-n achievability theorem + honest negative finding)
- `claiming-order-invariant` → dead-end ("RETHINK", structural
  impossibility argument)

## current.md updated

`results/imo-2026-03/current.md` updated: Status remains `partial`; added
round-4 notes to the `greedy-halving-adversary`, `rank-tie-vertex-
reduction`, and `smoothing-compactness-certificate` bullets, added new
bullets for `rank-pigeonhole-budget` and `claiming-order-invariant`,
expanded "Current best" with the round-4 results (cascading-halving-family
characterization, symmetric-c=1 lower bound, the sharp-dominant-removal
counterexample finding, and the claiming-order dead end), and updated the
"Full proof" file/lemma reference list.

## What remains open (unchanged in kind, narrower in scope)

1. The general-$n$ lower bound for $c\ge1$ (equivalently the full
   tie-vertex enumeration) — now narrowed to: (a) inequality $(\star)$ in
   Case A (`rank-pigeonhole-budget`), known to need ladder-specific
   structure beyond totals; (b) the $c=n$ minimality question
   (`self-similar-bracketing`/`rank-pigeonhole-budget` Case B); (c) the
   cascading-halving family is now fully characterized but the rest of the
   tie-vertex space (cross-ties, non-prefix subsets) is not.
2. The general upper bound for arbitrary Liu Bang markings — shown this
   round to be harder at $n=3$ than the $n=2$ template mechanism suggested
   (`smoothing-compactness-certificate`'s honest negative finding).
3. Asymmetric $c=1$ splits and $c\ge2$ splits in the lower-bound direction
   (`greedy-halving-adversary`).

No slug reached `solved` this round; no APPROVE issued. The field continues
to make genuine, independently-verified incremental progress from multiple
angles, with one framing (`claiming-order-invariant`) correctly retired.
