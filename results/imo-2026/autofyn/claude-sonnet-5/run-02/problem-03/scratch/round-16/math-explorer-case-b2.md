# Explorer report: attacking case (b2) — round 16

Scope: `lp-duality-certificate`'s Open Gap 1, narrowed to case (b2)
($p_1<T/2$, $T/D_n<p_2<a_nT/2$). Assignment: (1) assess the Alternating
Gap-Cross Lemma's sign bug and whether a fix still adds meaningful
coverage; (2) scout genuinely different mechanisms. Exploration only, no
proof attempted.

## 1. The sign bug: is "$(-1)^{j'}$, $j'$ = actually-split pairs" the right fix, and is it worth fixing?

**The proposed fix is almost certainly the correct general statement.**
The round-15 reviewer's root-cause diagnosis is exactly right and it
generalizes cleanly: every *actually split* pair contributes 3 elements to
$M$ (an odd rank-shift), every *equal/untouched* pair contributes 2 elements
(an even rank-shift, hence parity-neutral). Rank-shift parity is exactly
what flips the sign of every subsequent term in an alternating sum, so the
tail prefactor must be $(-1)^{j'}$ where $j'=|\{i\le j: p_{2i-1}>p_{2i}\}|$,
*not* $(-1)^j$. This isn't a patch bolted onto a shaky mechanism — it's
literally re-deriving the same `cross-piece-sign-assignment-identity`
regrouping (Step 2 of that lemma) with the correct rank-count bookkeeping.
I re-derived it independently by hand on the $(45,45,31,27)$ counterexample
and on a second synthetic case with 3 equal-pairs + 2 split-pairs ($j=5$,
$j'=2$): the corrected formula reproduces the correct $A$ in both, while
the buggy $(-1)^j$ version is right only when $j'\equiv j\pmod2$ (i.e. an
even number of untouched/equal pairs — the sub-population round 15 already
identified as unaffected). So: **yes, easily fixable, and the fix is the
obviously-correct one** — a future round should expect essentially a
copy-paste re-derivation, not new mathematical content, plus a
re-verification pass.

**Does the fix add meaningful coverage? Almost certainly not.** Three
independent reasons converge:

- The feasibility test (`\gamma_{i-1}>\max(p_{2i},p_{2i-1}-p_{2i})`) is
  unaffected by the sign fix — it was already independently verified
  correct. Equal-pair legs *relax* the chain in one sense (no cut spent,
  $\gamma_{i-1}=+\infty$-like slack) but the identity's *value* is
  unchanged by fixing the sign — the fix only changes which of the
  already-enumerated feasible constructions get the *right* predicted
  $\Phi$, not which constructions are newly feasible. So the fixed lemma's
  reach over the marking simplex is identical in shape to the buggy
  version's reach; only the sign of some terms was wrong.
- Round 15's own coverage table already shows the *unbugged* sub-population
  (no equal pairs, or an even number of them) adds only 2.5 points at $n=3$
  and 0 at $n=4,5$ over Bisect-Top-$k$. The bug specifically affects
  constructions *with an odd count of equal/untouched pairs* — on
  **generic** (real-valued, no coincidental equalities) random markings,
  which is what the coverage sampler draws from, equal-value pairs
  essentially never occur (measure zero event for continuous random
  sampling) except when they are the untouched *tail* pieces the outline
  never proposed pairing this way. So the buggy sub-population that the fix
  actually changes is a **negligible slice of the coverage that was already
  negligible**. Concretely: fixing the bug should move the "7.5%" figure at
  $n=3$ by at most a fraction of a percentage point, and leave $n=4,5$
  unchanged, because those samples essentially never hit odd-equal-pair
  configurations to begin with.
- Structurally, the whole Alternating Gap-Cross family only ever bounds
  $A(\text{tail})$ by $\max(\text{tail})=p_{2j+1}$ (Max Domination) — the
  same crude bound Bisect-Top-$k$ already uses. The "gap sum" term is new,
  but it only helps when consecutive pieces $p_{2i-1},p_{2i}$ have a *small*
  gap (so the alternating gap-sum stays small) — on a generic random
  marking, consecutive order-statistic gaps are typically **not** small
  relative to $T/D_n$ for larger $n$ (order-statistic gaps shrink slower
  than $T/D_n=T/(2^{n+1}-1)$, which decays geometrically), which is exactly
  why the $n=4,5$ marginal coverage was already measured at 0%.

**Verdict: fix it (cheap, mechanical, and it removes a live "not certified
as written" flag blocking reuse), but do not expect it to move the case-(b2)
coverage needle. This mechanism (Max-Domination-bounded tail + gap-sum) is
fundamentally too coarse for case (b2) at $n\ge4$ — it was designed to hit
specific tuned near-tight witnesses, not to cover a positive-measure region.
Spending another round tuning this family further is low-value; treat it as
closed business (fix, certify, move on) rather than a live front.**

## 2. Candidate genuinely-different mechanisms for case (b2)

I looked for approaches that don't just re-bound $A(\text{tail})\le\max$,
since that crude step is the common bottleneck of every sufficient-condition
family on file (Bisect-Top-$k$, Alternating-Gap-Cross, the two certified
dead ends).

### (A) Induction on $n$ reusing `telescoping-threshold-identity` — MEDIUM confidence, best-supported candidate

The file's own diagnosis (R13.4, end of §R13.3) already names this as the
untried alternative: instead of hunting a single-step unconditional
construction that closes case (b2) directly, use **Theorem C′/B$_k$'s exact
recursive identities** (already proved for *every* $n$ and marking, no
restriction) and argue inductively that case (b2)'s *recursive sub-instance*
(the reduced $(m-1)$-piece tail after one peel/bisect step) itself lands in
case (a) or (b1) **one level down**, even though the top-level marking sits
in case (b2). This is different in kind from every mechanism tried so far:
those all tried to bound $A(\text{tail})$ or $\Phi(\text{tail})$ crudely in
one shot; this instead asks a *structural* question about where the
recursion's image lands.

Why this might work: case (b2)'s defining window $T/D_n<p_2<a_nT/2$ is
stated in terms of the *original* $n$-piece marking's $p_2$ and $T$. After
one Theorem-C′ bisection of $p_1$, the new instance is the tail
$\{p_2,\dots,p_m\}$ with its own total $T'=T-p_1$ and its own top piece
$p_2$ — i.e. the *same* $p_2$ becomes the *new* $p_1$ of a smaller problem
at level $n-1$. Case (b2) at level $n$ requires $p_2<a_nT/2$; the reduced
instance is in case (a) at level $n-1$ exactly when its own new-$p_2$ (i.e.
$p_3$ of the original marking) satisfies $p_3\ge a_{n-1}T'/2$. Since $T'<T$
and $a_{n-1}<a_n$ (the $a_k$ sequence is increasing), this is a genuinely
different threshold on $p_3$ than anything case (b2)'s own definition
constrains — so there is real room for a "case (b2) at level $n$ generically
implies case (a) or (b1) at level $n-1$" argument, especially since case
(b2)'s window width is only defined by $p_1,p_2,T$ and says nothing about
$p_3$.

**Concrete risk / what would need to be shown, and why it's not free:** the
telescoping identity makes the *threshold algebra* clean, but the actual
claim needed is a statement about the *joint distribution* of $(p_2,p_3,T)$
under the "still in case (b2) one level down" assumption — i.e. an
adversarial argument that Xiang Yu (or whoever picks the worst marking)
cannot keep the recursion inside case (b2) at every level simultaneously.
This is exactly the kind of "eventually escapes the bad region" argument
that R13.4 flags as "not attempted" — it requires either (i) a monovariant
showing case (b2)-ness strictly shrinks some measure of freedom each level
(a promising angle: the interval $(T/D_n,a_nT/2)$ scales geometrically with
$n$, so if one can show the *same* marking cannot satisfy the case-(b2)
inequality at two consecutive levels for generic reasons, that's a two-line
argument, not full case enumeration), or (ii) an explicit adversarial
family that stays in case (b2) at every recursive level (a potential
*negative* result narrowing further, symmetric to how round 6's Half-Window
Vanishing Lemma broke a plateau by finding the exact structural reason a
window vanishes). **This is speculative but is the most promising general
mechanism I found that isn't a variant of the already-exhausted
crude-tail-bound family.** Recommend a cheap first move: numerically check,
for random case-(b2) markings at $n=4,5$, whether the *recursive image*
after one Theorem-C′/B$_k$ step lands in case (a)/(b1) at level $n-1$, or
stays in (b2) — this is a fast (no proof) diagnostic that would tell round
17 in one script run whether this path has legs before investing proof
effort.

### (B) Evaluate the Per-Piece Vertex Decomposition Theorem's joint vertex family directly, restricted to case (b2)'s box — LOW-MEDIUM confidence

Round 11/12 already tried this in general and hit the diagnosed obstruction
"no tail-structure-agnostic replacement for the ladder-specific spacing
facts" (Ratio-2 Spacing Lemma / Last-Element Bound only work for the
specific ladder tail, not an arbitrary marking's tail). But that attempt was
over the **whole simplex**. Round 14 already showed a *restricted* search
(Nelder-Mead confined to case (b2)'s box specifically) is computationally
tractable where the whole-simplex search timed out. The natural next step —
not yet tried — is to run the **exact finite vertex enumeration** (not a
continuum optimizer) of the Per-Piece Vertex Decomposition Theorem, but
restricted to markings satisfying case (b2)'s box constraints, for small
$m$ (say $m=4,5$). Because the box is lower-dimensional and bounded (not the
full open simplex), the vertex family might be small enough to enumerate
exhaustively and check against $a_nT$ by direct algebra, level by level.
This doesn't dodge the R11.5/R12.5 diagnosed obstruction (still no general
tail-agnostic spacing lemma) but might let round 17 at least fully resolve
case (b2) for **fixed small $n$** (e.g. $n=3,4$) via brute-force-but-exact
vertex enumeration, converting "genuinely open in general" into "closed for
$n\le4$, open for larger $n$" — a real narrowing in the same spirit as the
existing $P(3)$/$n\le3$ closures elsewhere in this file. Confidence is
lower than (A) because it's more computational grunt work than new
mathematical content, and it inherits the known difficulty that the vertex
family's *size* grows with $m$, so it likely won't scale past small $n$.

### (C) "Replace the adversary with a strictly stronger surrogate" (crux corpus: aimo-0560) — LOW confidence but worth flagging

Queried the crux corpus (`domain=combinatorics`, subtopics
`games-and-strategy`/`extremal-principle`/`invariants-and-monovariants`) for
adversary/minimax techniques. The most structurally relevant hit is
`aimo-0560`: *"Replace the adversary with a strictly stronger surrogate
whose reply is pointwise at least as damaging, so a win against the
surrogate transfers down and the reply collapses to a finite per-region
menu."* Applied here: instead of bounding $\Phi_{\min}$ over Xiang Yu's
*actual* legal move space in case (b2) (a continuum, hence the
vertex-enumeration difficulty), construct a **strictly more powerful**
hypothetical Xiang Yu (e.g. one allowed to cut with a relaxed budget, or
allowed fractional/negative fragments in some auxiliary sense) whose best
response is provably $\ge$ the real Xiang Yu's best response pointwise, but
whose optimization collapses to a small, explicit finite menu (the "finite
per-region menu" the crux describes). If Liu Bang's bound against the
*surrogate* still meets $a_nT$, it transfers down to the real game for
free. This is a genuinely different framing from every mechanism on file
(all of which analyze the *actual* legal move space directly). I do **not**
have a concrete instantiation of what the surrogate would be here — this is
a scouting flag, not a worked-out plan — but it's the one technique in the
corpus that directly targets "continuum optimization is hard, collapse it
by strengthening the adversary" rather than "characterize the vertex family
of the real adversary," which is what every existing approach does. Low
confidence because instantiating a *useful* surrogate (one both provably
stronger and provably reducible to a small menu) for this specific
alternating-sum game is unclear; flagging for a future explorer/outliner to
consider, not recommending immediate build effort.

### (D) Dyadic/band-occupancy retry, restricted to case (b2) — NOT recommended

`dyadic-band-occupancy` (round 5) already rigorously refuted its own
coarse per-band count/mass invariant as insufficient in general. Nothing
about case (b2) specifically escapes that refutation (the counterexample
wasn't case-(b2)-specific but a general structural fact about fine
within-band position mattering) — re-attempting this family restricted to
case (b2) is not a new idea, just a narrower domain for an already-dead
mechanism. **Do not re-open.**

## Summary / recommendation for round 16 outline

1. **Sign-bug fix**: cheap, mechanical, should be done (removes a
   "not certified" flag), but explicitly **not** expected to move case (b2)
   coverage — don't budget serious effort or claim progress from it beyond
   certification hygiene.
2. **Best new lead**: (A), the induction-on-$n$ "case (b2) at level $n$
   generically escapes to case (a)/(b1) at level $n-1$" argument, reusing
   `telescoping-threshold-identity` and the already-certified Theorem
   C′/B$_k$ recursive identities. Recommend a cheap numeric diagnostic first
   (one script, no proof) to see whether the recursive image of case-(b2)
   markings actually tends to land outside case (b2) one level down, before
   committing outline/build effort to a full proof attempt.
3. Secondary, lower-priority: (B) exact vertex enumeration restricted to
   case (b2)'s box, for small fixed $n$ only (a narrowing, not a general
   closure).
4. Speculative flag, not yet actionable: (C) the "stronger surrogate
   adversary" framing from the crux corpus (`aimo-0560`) — genuinely
   different in kind from everything tried, but no concrete instantiation
   found yet; worth a dedicated explorer pass if (A) stalls.
