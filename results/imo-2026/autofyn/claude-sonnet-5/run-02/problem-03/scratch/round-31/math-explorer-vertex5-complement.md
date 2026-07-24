## imo-2026-03 — lens: "simultaneous q1-and-tail cuts" branch of h(m)

### Precise statement of the open branch

Recall (approach `greedy-halving-adversary`, round 24 definition):
$$h(m):=\inf\{A(\{c\}\cup S): c\in(0,q_1],\ S\text{ a legal }(\le m-1)\text{-cut
refinement of the unit }m\text{-ladder }q_1>\dots>q_{m+1}\},\qquad q_i=2^{m+1-i}f(m).$$
Rounds 28–30 fully closed: (a) the whole $q_1$-untouched sub-case (Theorem 42,
every $m\ge1$), and (b) the "single-cut-on-$q_1$, tail completely untouched"
piece of the $q_1$-cut sub-case ($S=\{x,q_1-x\}\cup\mathrm{tail}$, tail
$=\{q_2,\dots,q_{m+1}\}$ verbatim, $x\in(0,q_1/2]$) — Vertices 1–5, all closed,
every $m\ge3$.

**The precisely-scoped remaining open piece** (what round 30 flagged, and what
this lens targets) is the natural next layer: $S$ spends *one* cut on $q_1$
(giving fragments $x,q_1-x$, $x\in(0,q_1/2]$) **and** spends *some* of its
remaining $\le m-2$ cuts refining the tail, i.e.
$$S=\{x,q_1-x\}\cup S'',\qquad S''\text{ a legal }(\le m-2)\text{-cut
refinement of }\{q_2,\dots,q_{m+1}\},$$
and the target is $A(\{c\}\cup S)\ge f(m)$ for every $c\in[0,q_1]$, every
legal $S''$, every $x\in(0,q_1/2]$, every $m\ge3$ (nonvacuous exactly when
$m-2\ge1$, i.e. $m\ge3$). This is a genuinely larger family than the
tail-untouched piece (which is the special case $S''=$tail unrefined) and
was **not attacked at all** as of round 30. (Multi-cut splits of $q_1$ itself,
i.e. $\ge2$ cuts spent on $q_1$, are a *further* layer beyond even this one —
out of scope for what round 30 flagged, and I did not probe it.)

### Candidate mechanism found this round (the main deliverable)

By `single-insert-point-vertex-lemma` applied to $c$ against the fixed
$S=\{x,q_1-x\}\cup S''$, the same 5-type vertex enumeration as rounds 29–30
applies verbatim: $c\in\{0,\,q_1,\,x,\,q_1-x\}$ or $c$ tied to some element of
$S''$. Working each type with only certified tools:

- **$c=0$:** $A(S)\ge f(m)$ is exactly the outer $(\star_m)$ hypothesis — free,
  as always.
- **$c=q_1-x$** (even multiplicity 2, pair-cancels): $A(\{c\}\cup S)=A(\{x\}\cup
  S'')$. Observe $\{x\}\cup S''$ with $x\in(0,q_2]$ and $S''$ a legal
  $(\le m-2)$-cut refinement of the $(m-1)$-ladder $\{q_2,\dots,q_{m+1}\}$ is
  **literally an instance of $h(m-1)$ itself** (after the certified scaling
  $\lambda_1=f(m)/f(m-1)$, exactly Theorem 38 Claim (II)'s rescaling). So
  $A(\{x\}\cup S'')\ge\lambda_1\cdot h(m-1)$, and **if $h(m-1)\ge f(m-1)$ is
  already available (strong induction on $m$ itself, not just on the outer
  $n$-induction!), this closes immediately: $\lambda_1 f(m-1)=f(m)$.** This
  is a genuinely new observation — no prior round used $h(m)$ as its own
  inductive hypothesis on $m$; only the outer $(\star_{m'})$ induction was
  used. **This vertex is free given the $h(m-1)$ IH.**
- **$c=q_1$:** $A(\{q_1\}\cup S)=x+A(\{x\}\cup S'')$ (peel $q_1$ off $S$ via
  `sharp-dominant-removal-identity`, using $q_1>\max(S)$, then the identity
  $q_1-(q_1-x)=x$). By the same $h(m-1)$-instance fact above,
  $A(\{x\}\cup S'')\ge f(m)$ (given the IH), so $A(\{q_1\}\cup S)\ge x+f(m)>f(m)$
  trivially. **Also free given the $h(m-1)$ IH — easier than rounds 29's
  corresponding proof, which needed Theorem 42 one level down; here the
  bare $h(m-1)$ IH suffices.**
- **$c=x$ (even multiplicity 2, pair-cancels):** $A(\{c\}\cup S)=A(\{q_1-x\}
  \cup S'')$. Since $q_1-x\ge q_2\ge\max(S'')$, peel: $=(q_1-x)-A(S'')$. This
  needs an **upper** bound $A(S'')\le(q_1-x)-f(m)$ — the hard direction. By
  the certified `single-insert-point-vertex-lemma`/exact-slope argument (as
  in round 30's $F(x)$), the whole expression is monotone in $x$ so the
  binding case is $x=q_1/2$: need $A(S'')\le q_2-f(m)$.
- **$c=t\in S''$ (general fragment tie, the genuine "Vertex-5 analogue"):**
  pair-cancels to $A(\{x,q_1-x\}\cup(S''\setminus\{t\}))$, then peels $q_1-x$
  to $(q_1-x)-A(\{x\}\cup(S''\setminus\{t\}))$ — needs an upper bound on
  $A(\{x\}\cup(S''\setminus\{t\}))$, a strictly harder relative of the $c=x$
  case (one extra inserted element).

**Key finding: the $c=x$ boundary requirement is EXACTLY `rank-pigeonhole-
budget`'s own $\mathrm{MaxCeil}(m)$.** That approach's file (§7.10, certified
notation) defines, for a length-$\ell$ ratio-2 tail $\sigma$, $\mathrm{MaxCeil}
(\ell): A(S)\le\sigma_1-\sigma_\ell$ for every legal $(\le\ell-2)$-cut
refinement $S$ of $\sigma$. Instantiating with $\sigma=\{q_2,\dots,q_{m+1}\}$
(length $\ell=m$, top $\sigma_1=q_2$, bottom $\sigma_m=q_{m+1}=f(m)$, budget
$\le m-2=\ell-2$ cuts) gives **exactly** $A(S'')\le q_2-f(m)$ — precisely the
bound the $c=x$ vertex needs. This is not a coincidence of notation; I
verified it numerically (below) and algebraically: it is the *same* object.
So **the "simultaneous cuts" branch's $c=x$ vertex is not a new obstruction —
it is `rank-pigeonhole-budget`'s already-partially-closed $\mathrm{MaxCeil}(m)$
target**, which per `current.md`/that file's own record is closed for
$m\le4$ (rounds 25/26) and **open, with a proved Necessity Theorem that the
naive top-cut mechanism cannot extend, for $m\ge5$** (their §"Round 26"
material, lines ~2546–2666 of `rank-pigeonhole-budget.md`).

The deeper "$c=t\in S''$" vertex is a genuinely harder cousin of MaxCeil (an
"insert one extra element then bound above" variant, not literally
$\mathrm{MaxCeil}$ itself) — flagged here as needing either a fresh
generalization of MaxCeil's machinery or a separate argument (e.g. bounding
$A(\{x\}\cup(S''\setminus\{t\}))-A(S'')$ via an insert-bound-type corollary,
by analogy with how round 30 closed the tail-untouched Vertex 5).

### Numeric probing (exact `Fraction`, scouting only — conjecture, not proof)

- Random search (30,000 trials/level, $x$, $S''$ with 0 to $m-2$ random legal
  cuts spread over the tail, $c$ from all 5 vertex families or a random
  continuous value) found **zero violations** of $h(m)\ge f(m)$ for
  $m=3,4,5,6$ (worst ratio found $\to1$ as $m$ grows, consistent with
  tightness, script in this session, not saved to repo).
- Targeted check: splitting exactly one tail piece arbitrarily and testing
  $x=q_1/2$: for $m=3,4$ the true minimum over dense grids of split points and
  $x$ is **exactly** $f(m)$, attained only at the known boundary vertices
  ($c=0$ or $c=q_1$), never at an interior tie — consistent with (but not
  proving) the conjecture that the harder vertices ($c=x$, $c=t\in S''$) are
  never *strictly* binding once $m\le4$ (matching MaxCeil's own closed range).
- **Direct confirmation of the MaxCeil identification:** computed
  $\max_{S''}A(S'')$ by random search over legal $(\le m-2)$-cut refinements
  of the tail for $m=3,4,5,6$: found exactly $3,7,15,31$ respectively — which
  equal $q_2-f(m)=2^{m-1}-1$ **exactly** in each case (using $f(m)=1$ units),
  matching the bound the $c=x$ vertex needs with equality (tight, not just
  sufficient). E.g. at $m=4$: tail $=\{8,4,2,1\}$, splitting the piece $4$
  into $(x,4-x)$ for *any* $x\in(0,2)$ gives $A=8-x+2-(4-x)+1=7$ identically
  (the split parameter cancels exactly) — an exact plateau, not a numerical
  coincidence, confirming $\mathrm{MaxCeil}(4)$'s stated bound is achieved
  with equality by a whole one-parameter family, consistent with that
  approach's own report of a tight, non-strict inequality.

### Distinct openings

1. **Strong induction on $h(m)$ itself** (new): use $h(m-1)\ge f(m-1)$ as an
   inductive hypothesis (on top of, not replacing, the outer $(\star_{m'})$
   induction) to close the $c=q_1-x$ and $c=q_1$ vertices for free — this was
   not attempted in rounds 28–30, which only cited $(\star_m)/(\star_{m-1})$/
   Theorem 42, never $h(m-1)$ directly. Cheap, likely correct (verified by
   hand above); worth writing up formally first since it shrinks the residual
   from "4 nontrivial vertex types" to "2" ($c=x$ and $c=t\in S''$).
2. **Transplant `rank-pigeonhole-budget`'s $\mathrm{MaxCeil}(m)$ work
   directly.** The $c=x$ vertex *is* $\mathrm{MaxCeil}(m)$ verbatim (shown
   above) — so this file does not need to re-derive it: cite the sibling
   approach's certified $m\le4$ closure directly (closes $h(3)$'s and $h(4)$'s
   $c=x$ vertex for free), and for $m\ge5$ the exact same obstruction that
   approach has been fighting (their own "Necessity Theorem," their round-26
   material) is what blocks this vertex too — meaning **any future progress
   on $\mathrm{MaxCeil}(m\ge5)$ by that sibling approach directly closes part
   of this file's residual**, and vice versa: a proof found here would also
   close their target. This cross-approach identification is the main
   actionable finding of this scouting pass.
3. **Attack the deeper "$c=t\in S''$" vertex as a generalized/insert-variant
   of MaxCeil** (a fresh target, not yet named in either file): needs an
   upper bound on $A(\{x\}\cup(S''\setminus\{t\}))$, i.e. MaxCeil with one
   extra inserted element and one tail element removed. Candidate mechanism:
   adapt the Insert-Bound Corollary (`single-insert-point-vertex-lemma`'s
   $\pm1$-slope fact, already certified, used identically in round 29/30) to
   convert this into $A(S''\setminus\{t\})\pm x$ and then a MaxCeil-type bound
   on the punctured tail $S''\setminus\{t\}$ (length $m-1$) — structurally
   parallel to how round 30 closed the tail-untouched Vertex 5 via the exact
   "remove one rung" identity, but now for a *cut* tail rather than the
   pristine ladder, so the clean closed-form alternating-sum evaluation
   (round 30, Step 4) will not apply verbatim; a genuinely new bound on
   $A(S''\setminus\{t\})$ for arbitrary legal cuts is needed, not just an
   exact formula for the untouched case.

### Cheap-kill candidates

- None found that shortcuts the whole branch; but the induction-on-$h(m-1)$
  opening above is a cheap, low-risk closure of 2 of 4 vertex types before
  any heavier MaxCeil-transplant work — should be done first.
- Sanity check before building: confirm (by hand, one line) that
  `sharp-dominant-removal-identity`'s hypothesis $q_1-x>\max(S'')$ still holds
  when $S''$ is refined (not just when tail is untouched) — it does, since
  splitting a piece never increases its max fragment above the parent's
  value, so $\max(S'')\le q_2\le q_1-x$ for all $x\le q_1/2$; this was
  implicitly used above and should be stated explicitly in any writeup to
  avoid a citation-mismatch bug like the ones the outline-reviewer has
  caught before in this file.

### Candidate technique(s)

`single-insert-point-vertex-lemma` (vertex pinning, exactly as rounds 29–30),
`sharp-dominant-removal-identity` (peeling $q_1-x$), the pair-cancellation
special case of `odd-run-reduction-lemma`, `Lemma 9` (scaling) to identify
$\{x\}\cup S''$ with $h(m-1)$'s own object, and — for the hard vertices —
`rank-pigeonhole-budget`'s $\mathrm{MaxCeil}(\ell)$ machinery (Fact 2,
`pair-insertion-ordering-lemma`, their Necessity Theorem) as the transplant
target.

### Knowledge-base entries to use

No new generic `knowledge_base.md` entries beyond what's already cited
throughout this file (alternating-sum/odd-rank formalism, LP-vertex
optimization). This is entirely an internal-machinery problem at this point.

### Analogous past problems (cruxes)

Did not find a genuinely new corpus match this round beyond what prior
rounds already used (ratio-2/superincreasing-sequence extremal arguments);
this is a highly problem-specific combinatorial identity chain rather than a
transplant of an external contest crux. Recommend not spending outliner
budget on a fresh corpus query for this narrow sub-target — the internal
cross-approach transplant (opening 2 above) is the higher-value lead.

### Prior progress

Rounds 28–30 (see above) closed the $q_1$-untouched sub-case in full (every
$m\ge1$) and the "single-cut-on-$q_1$, tail-untouched" piece of the $q_1$-cut
sub-case in full (every $m\ge3$). The simultaneous-cuts piece scouted here
was entirely untouched before this round.

### Dead ends (do not retry)

- Do not re-attempt "the natural shortcut: worst $c$ is always $c=\max(S)$ or
  $c\in\{0,q_1\}$" for arbitrary legal $S$ — round 24 already found this false
  by direct counterexample search (deeper ties undercut the base trio in
  ~46% of arbitrary-$S$ trials, ~3.7% even on legal ladder refinements).
- Do not assume $\mathrm{MaxCeil}(m)$'s top-cut branch extends past $m=4$ by
  the same mechanism used for $m=3,4$ — `rank-pigeonhole-budget`'s own
  Necessity Theorem (their file, ~line 2592) already rigorously shows the
  natural extension fails past a certain regime; any attack on the $c=x$/
  $c=t\in S''$ vertices for $m\ge5$ should start from that diagnosis, not
  re-derive it.

### Small-case / intuition notes (conjecture, not proof)

- $h(m)=f(m)$ exactly, for every $m$ tested ($m\le6$), across every vertex
  family including the newly-probed simultaneous-cuts family — strong
  numeric support for the overall conjecture but no proof beyond $m\le2$
  (fully closed) and the specific vertex types closed in rounds 28–30.
- The $c=x$ vertex's required bound $A(S'')\le q_2-f(m)$ is tight (achieved
  exactly, not just approached) by simple one-cut configurations (e.g.
  splitting the tail's second piece), for $m=3,\dots,6$ — this is an exact
  algebraic identity (the split parameter cancels), not a numerical
  coincidence, and matches $\mathrm{MaxCeil}(m)$'s own claimed tightness
  exactly.
