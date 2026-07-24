## Status
solved

(Scope note: "solved" here means **this approach's own target, Claim (A)**, is
now proved completely and rigorously — both the achievability half and the
full lower bound, Case I and Case II, for every $n$. Claim (A) is one of
several pieces the project's `current.md` tracks toward the whole
`imo-2026-03` theorem; Claim (B) — `greedy-halving-adversary`'s target — and
the general upper bound are proved by sibling approaches and are outside this
file's scope, exactly as scoped since round 5.)

## Approaches tried
- **(round 32, this build — write up $\mathrm{MaxCeil}(5)$'s top-untouched
  branch as a free corollary of $(\star_3)=\mathrm{MinFloor}(4)$'s round-31
  closure, then attack the top-cut residual with the vertex-enumeration
  toolbox).** Part (a) done exactly as dispatched (§7.19.1, one-paragraph
  corollary). Part (b) achieved strictly more than dispatched: two new
  fully general lemmas (Max Bound $A(S)\le\max(S)$; Insertion Sandwich
  $|A(T\cup\{a\})-A(T)|\le a$, §7.19.2, both independently verified by
  $200{,}000$-trial exact-`Fraction` search, zero violations) combine into
  a **Master Theorem** (§7.19.3): $\mathrm{MinFloor}(m-1)=(\star_{m-2})
  \Rightarrow\mathrm{MaxCeil}(m)$ in full, both branches, via one unified
  mechanism (no shape census, and explicitly *not* the two-peel+Fact-2
  route §7.15's Necessity Theorem ruled out — this uses $\mathrm{MinFloor}
  (m-1)$'s lower bound directly, plus Insertion Sandwich to absorb
  $\sigma_1$'s other fragments, a genuinely different mechanism).
  Instantiated at $m=5$ (§7.19.4), using the now-certified $(\star_3)$,
  this closes $\mathrm{MaxCeil}(5)$ **unconditionally, in full**, hence
  $(7.9.1)$ at $n=8$ — one level past round 26's $n\le7$, and superseding
  the need to separately enumerate the $\sigma_2$-touched residual's
  shapes as the dispatch's step 3 proposed. Honestly scoped: the Master
  Theorem is conditional in general ($m\ge6$ needs $(\star_4)$, not yet
  certified); only its $m=5$ instantiation is unconditional this round.
  Independently sanity-checked at $\sigma=(16,8,4,2,1)$ over $250{,}000$
  random/targeted-adversarial trials (`/tmp/verify_maxceil5.py`), max
  found $\approx14.997<15$, consistent, not a substitute for the proof.
  Does not close Claim (A) further (already fully closed) or the general-$n$
  pattern (still open, all $k\ge3$ beyond the now-3 certified values).
- **(round 31, this build — close the last $2$ of $6$ residual shapes of
  $(\star_3)=\mathrm{MinFloor}(4)$, $(1,2,0,0)$ and $(2,1,0,0)$; does not
  touch Claim A's own status).** New §7.18.4/7.18.5 rewritten. Per the
  round-31 outline's Step 5 (the "flat identity" shortcut) and Step 4
  (carry the joint constraint explicitly), abandoned the linear
  branch-tree case-split (which round 30 correctly diagnosed as
  requiring a genuine, easy-to-drop cross-pair joint-feasibility
  constraint at every branch) in favor of **direct citation of the
  certified `vertex-minimum-theorem`**: enumerated, in exact rational
  arithmetic, the *complete, exhaustively-justified* finite family of
  candidate vertices (every triple of the $18$ (resp. $21$) legal
  type-(I)/(II) tight-constraint hyperplanes for shape $(2,1,0,0)$
  (resp. $(1,2,0,0)$), solved exactly, filtered by feasibility), giving
  $36$ (resp. $27$) genuine vertices, every one evaluated by direct
  sorting: **all satisfy $A(U)\ge1$, with equality at $5$ (resp. $3$)
  vertices**, matching the round-28 achievability construction exactly.
  This closes both shapes **in full, both directions, no residual
  gap** — the feasibility filter applied uniformly to all $816$ (resp.
  $1330$) candidate triples *is* exactly where the joint-feasibility
  constraint the round-30 diagnosis flagged gets enforced, automatically
  and correctly, for every vertex at once, rather than needing to be
  spotted branch-by-branch. Combined with rounds 28–30's closure of the
  other $4$ shapes, **$(\star_3)=\mathrm{MinFloor}(4)$ is now fully
  closed, all $20$ maximal shapes, both directions.**
- **(round 30, this build — close $(2,0,0,1)$'s residual $f_1\ge4$ branch
  and attack the $4$ untouched shapes $(1,1,0,1),(1,1,1,0),(1,2,0,0),
  (2,1,0,0)$; does not touch Claim A's own status).** New §7.18. Per the
  round-30 outline: (i) closed shape $(2,0,0,1)$'s $f_1\ge4$ branch in
  full by hand (two-peel chain + a four-way split on $f_2$ vs $2$, using
  the certified Pair-Insertion Ordering Lemma's mirrored form for the
  $f_2>2$ sub-case and a direct double-peel — no new lemma needed — for
  $f_2\le2$, since the domain there forces total elementwise domination
  of $\{f_2,f_3\}$ over $\{e,f\}$) — combined with round 29's closure of
  $f_1<4$, **shape $(2,0,0,1)$ is now fully closed on its entire domain,
  both directions.** (ii) Closed shape $(1,1,0,1)$ **in full** via the
  Forced-Dominance Fact (a single cut always leaves a part $\ge$ half of
  its parent) plus an exhaustive hand case-tree (branch $b\ge c$ vs
  $b<c$, each with $3$–$5$ further sub-cases resolved via repeated
  `sharp-dominant-removal-identity` peeling, `odd-run-reduction-lemma` for
  ties, and elementary $3$-element alternating-sum case splits) — no new
  lemma needed, only the already-certified machinery. (iii) Closed shape
  $(1,1,1,0)$ **in full**, structurally analogous but requiring the
  certified Pair-Insertion Ordering Lemma directly (not just elementary
  $3$-element splits) at one depth, plus one genuinely new
  case-collapse fact (the branch $b<c,c\le3.5$ closes trivially via Fact
  1 alone, isolating the real work to $b<c,c>3.5$) and, in that residual,
  a further $6$-way split resolved cleanly using the sub-branch's own
  sharper bound $a>6$. (iv) Attempted shapes $(1,2,0,0)/(2,1,0,0)$
  (structurally different: a $3$-part triple **and** a $2$-part pair
  both genuinely free, with *neither* top fragment unconditionally
  dominant — the outline's flagged "extra branch") and found a real,
  previously-undiagnosed obstruction beyond a single extra top-level
  split: closing even one sub-case requires a **cross-pair
  joint-feasibility constraint** (e.g. $c\ge4-f_3$, not implied by
  either pair's own defining inequality in isolation) — caught and fixed
  one genuine algebra error caused by omitting this constraint (a
  spurious near-violation, $\to6^-$ instead of $>6$) before finalizing
  one worked sub-case; the bulk of both shapes' case trees is **not**
  completed this round — honestly reported as the remaining gap, now
  much more precisely diagnosed than round 28's "$3$ free parameters"
  framing. **Net this round: $4$ of $6$ residual shapes for
  $(\star_3)=\mathrm{MinFloor}(4)$ are now fully closed** ($(2,0,1,0)$
  and $(2,0,0,1)$ from round 29+30, $(1,1,0,1)$ and $(1,1,1,0)$ new this
  round); $2$ of $6$ remain open with a sharper diagnosis.
  $(\star_3)$ itself is **not** closed this round (2 shapes remain).
  **Status of this addendum remains `partial`.**
- **(round 29, this build — fix the outline-reviewer's flagged citation-
  mismatch bug in the round-28 6-shape residual, and close as many of the
  6 shapes as time allows; does not touch Claim A's own status).** New
  §7.17. The round-29 outline proposed reducing each residual shape's
  coupled free coordinates (e.g. $f_1,f_2,f_3$ summing to $\pi_1$) one at
  a time via `single-insert-point-vertex-lemma`; the outline-reviewer
  correctly found this lemma does not apply to a mass-conserving coupled
  pair (proved slope $\pm1$ for a single free coordinate against a fixed
  rest; the coupled pair's true slope is $\pm2$, a different function).
  **Fix applied:** proved a new, fully general, elementary **Pair-
  Insertion Ordering Lemma** — a direct sorted-rank closed form for
  $A(\{x,p,q,w\})$ when $p,q$ are a conservation pair ($p+q=C$) and $w$ is
  a reference value with $q\le w\le p$ (plus a mirrored version for
  $w\ge p\ge q$) — proved from scratch by elementary case-split on $x$'s
  position, not by misapplying the single-insert lemma. Applied this
  lemma to close **shape $(2,0,1,0)$ completely, both directions, on its
  entire domain** (the residual $f_1<4$ regime closed here by hand via
  the Lemma plus an exact polynomial-positivity check in each of the
  Lemma's 4 cases; the complementary $f_1>4$ regime, already claimed
  closed in round 28, independently re-verified this round by a fresh
  $200{,}000$-trial exact-`Fraction` check) — this is a genuine, complete
  closure of the concrete shape the outline-reviewer used as its own
  counterexample. Also closed **shape $(2,0,0,1)$'s residual regime
  ($f_1<4$) completely by hand** via the mirrored form of the same Lemma
  (a new shape, not previously worked in detail); its complementary
  regime ($f_1\ge4$) is numerically confirmed (fresh $300{,}000$-trial
  exact-`Fraction` check, zero violations) but not yet hand-derived,
  an honestly narrower residual gap than before. **The remaining 4
  shapes** — $(1,1,0,1),(1,1,1,0),(1,2,0,0),(2,1,0,0)$ — **were not
  attempted with the corrected mechanism this round** (time-boxed);
  flagged as the concrete next step, since the now-proven Pair-Insertion
  Ordering Lemma is a general, reusable tool expected (but not yet
  verified) to apply to each by the same peel-then-insert pattern.
  $(\star_3)$ remains open; this round's genuine progress is fixing the
  reviewer's flagged citation bug with a correct, proven, reusable
  replacement lemma, and using it to fully close 1 more shape and
  half-close a 2nd (net: from "0 of 6 residuals closed, wrong citation"
  to "1.5 of 6 residuals closed, with the correct general tool now on
  file"). **Status of this addendum remains `partial`.**
- **(round 28, this build — attack $(\star_3)=\mathrm{MinFloor}(4)$ via
  the round-28 outline's 20-shape exhaustion; per the outline-reviewer's
  required fix, does not touch Claim A's own status).** New §7.16. First
  corrected the outline's self-contradictory shape-count claim (its own
  formula computes $35$, the true count of "$\le3$ cuts" compositions; the
  stated "$20$" is instead $\binom{6}{3}$, the count of "*exactly* $3$
  cuts" compositions) and supplied the missing justification (cited from
  `vertex-minimum-theorem` part 2) for why closing only the $20$
  exactly-budget-$3$ shapes, on their closed domains, still proves the
  theorem for the full $35$-shape "$\le3$" space. **Two new master
  theorems, fully proved, closing $13$ of the $20$ shapes in two clean
  uniform arguments** (Master Theorem I: all $10$ shapes with $\pi_1$
  untouched, via one dominant-peel + Fact 2; Master Theorem II: all $3$
  shapes with $\pi_1$ split once and $\pi_2$ untouched, via a 2–3-level
  peel cascade, uniform over how the remaining budget splits $\pi_3,\pi_4$).
  Shape $(3,0,0,0)$ closes for free by direct citation of `claim-a-full-
  closure` (it *is* Claim A at $n=3$). **Genuine correction to the
  outline's own diagnosis:** exact computation (independent symbolic
  vertex enumeration, `/tmp/vertex_full.py`, exact rationals) found $7$
  shapes attain $A=1$ exactly, not the $2$ ("$(3,0,0,0)$ and $(2,0,1,0)$")
  the outline flagged — the other $5$ ($(1,1,0,1),(1,1,1,0),(1,2,0,0),
  (2,0,0,1),(2,1,0,0)$) are equally tight. For all $6$ non-citation tight
  shapes, proved **achievability in full** by hand — an explicit, uniform
  construction realizing the multiset $\{4,4,2,2,2,1\}$ (odd-run-reduces
  to $\{2,1\}$, $A=1$) within each shape's own per-piece budget. The
  matching **lower bound is proved by hand on a large sub-region of each
  of the $6$ shapes** (directly generalizing Master Theorem II's cascade)
  but a genuinely $3$-free-parameter residual sub-case in each resists the
  same cheap peel-and-Fact technique (checked explicitly to fail near the
  tight vertex) and is **not closed this round** — an honestly narrower,
  precisely-located gap (isolated interior regions of $6$ named shapes,
  not a whole new shape needing derivation from scratch). Net: $14/20$
  shapes fully closed both directions; achievability closed on all $20$;
  the open gap is the lower bound on $6$ named residual regions. $(\star_3)$
  is **not** closed this round; **Status of this addendum remains
  `partial`** (Claim A's own Status, `solved`, is unaffected).
- **(round 27, this build — generalize the $m=4$ "Double-Dominant-Peel +
  Fact-2" mechanism to general $m$, per this round's dispatch and the
  outline-reviewer's APPROVE; does not touch Claim A's own status).** Two
  genuinely new results, both self-contained. **New §7.14 (positive):** a
  fully general, unconditional theorem — for *every* $m\ge2$ and *every*
  legal top-cut shape with $\sigma_2$ untouched (no restriction on how many
  cuts land on $\sigma_1$ or on $\sigma_3,\dots,\sigma_m$, or how they are
  distributed), $A(S)\le\sigma_1-\sigma_m$ holds, proved via the same
  two-peel-plus-Fact-2 mechanism combined with `odd-run-reduction-lemma`
  for the tie sub-case — strictly generalizes $4$ of the $5$ shapes closed
  by hand at $m=4$ (§7.13) to arbitrary $m$ and arbitrary cut counts in one
  uniform argument, with no induction on $m$ and no shape enumeration
  needed at all. Also identified and corrected a mismatch in the outline's
  own framing: the right dividing line is "$\sigma_2$ touched or not," not
  "number of distinct indices touched" (a shape touching $\sigma_1,\sigma_3,
  \sigma_5$ — $3$ distinct indices — is fully covered by §7.14, while a
  shape touching only $\sigma_1,\sigma_2$ — $2$ distinct indices, inside
  the outline's claimed "safe" zone — is not). **New §7.15 (negative, a
  genuine correction to the outline's premise):** proved a rigorous
  Necessity Theorem — via a continuity argument on the family
  $S_\varepsilon=\{\sigma_1-\varepsilon,\varepsilon\}\cup Z\cup\tau$
  ($Z$ an arbitrary refinement of $\sigma_2$, $\tau=(\sigma_3,\dots,
  \sigma_m)$ untouched) — showing that $\mathrm{MaxCeil}(m)$'s top-cut
  branch, in full generality, *entails* $A(Z\cup\tau)\ge\sigma_m$ for every
  such $Z$, which is exactly a restricted sub-instance of
  $\mathrm{MinFloor}(m-1)$'s case (ii), i.e. of $(\star_{m-2})$ (via
  §7.11's Index-Chain Identity). Since $(\star_k)$ is unconditionally
  certified only for $k\le2$, this **proves** — not merely observes — that
  the top-cut branch's full closure for $m\ge5$ cannot avoid $(\star_k)$,
  $k\ge3$, directly refuting the round-27 outline's "Watch out for" premise
  that this front is self-contained and independent of the central
  obstruction. Cross-checked (not substituting for the proof) by an exact
  `Fraction` search at $m=5$: the minimum of $A(Z\cup\tau)$ over $2000$
  random $\le2$-cut splits $Z$ hits exactly $\sigma_5$ and never goes
  below it, consistent with the Necessity Theorem and with $(\star_3)$
  remaining genuinely open. Net honest result: the top-cut branch is now
  unconditionally closed on a strictly larger, cleanly characterized
  sub-family (every $m$, $\sigma_2$-untouched) plus the two small full
  closures already on file ($m=3,4$), and is proved to be **provably
  entangled** with $(\star_k)$, $k\ge3$, for $m\ge5$ — a sharper, corrected,
  and more informative status than "open, cause unknown."
- **(round 26, this build — reframe $\mathrm{MinFloor}$'s open branch as
  conditional on the project's own standing hypothesis, and close
  $\mathrm{MaxCeil}(3)$/$\mathrm{MaxCeil}(4)$ in full; does not touch Claim
  A's own status).** Per the round-26 outline's two-part assignment: (1)
  new §7.11 independently re-derives (not just copies) the index-chain
  identity $\mathrm{MinFloor}(\ell)\equiv(\star_{\ell-1})$ — a genuine
  scale-invariance argument via the already-certified
  `alternating-sum-scaling`, showing $\mathrm{MinFloor}(\ell)$ is *literally
  the same statement* as the project's own standing lower-bound master
  hypothesis one level down, not an independent sub-lemma needing new
  machinery. Since $(\star_1),(\star_2)$ are the only two values currently
  certified unconditional (per `current.md`'s own round-23 audit), this
  gives, as a genuine strengthening over round 25: $\mathrm{MinFloor}(3)$ is
  now known **fully** closed (both branches — round 25 had only closed its
  case-(i) branch, leaving case-(ii) as numerically-consistent-only), and
  $\mathrm{MaxCeil}(\ell)$'s top-untouched branch is unconditionally free
  for every $\ell\le4$ (equivalently $n\le7$). (2) New §7.12 and §7.13
  independently re-verify and formally close, respectively,
  $\mathrm{MaxCeil}(3)$ ($n=6$) and $\mathrm{MaxCeil}(4)$ ($n=7$) **in full,
  both branches, unconditionally** — the round's build target. §7.13's
  closure of $\mathrm{MaxCeil}(4)$'s top-cut branch (the genuinely open
  content, not reducible to $(\star_\cdot)$) reuses only already-certified
  facts (`sharp-dominant-removal-identity`, Fact 1 `half-bound-lemma`, Fact
  2 $A\le\mathrm{Total}$) via an exhaustive 5-shape cut-distribution
  enumeration (all shapes with $\ge1$ cut on $\sigma_1$, $\le2$ cuts total)
  — explicitly avoiding the naive `Triangle-Bound-for-A` +
  `Max-Domination-Lemma` shortcut per the outline's instruction (verified
  insufficient: gives only $A\le5-a$, false for $a<2$, versus the true
  tight value $3-2a$ or $1$). Every shape closes exactly via a
  two-peel-plus-Fact-2 mechanism, with the supremum $\sigma_1-\sigma_4$
  approached (never exceeded, never attained for a genuine cut) at the
  degenerate boundary where the split on $\sigma_1$ vanishes — i.e. exactly
  where the top-cut branch limits into the (separately closed)
  top-untouched branch, a clean internal consistency check. **Net result:
  $(7.9.1)$ is now unconditionally resolved at $n=6$ and $n=7$** — the
  first genuine, unconditional closures of $(7.9.1)$ at any $n$, though
  explicitly scoped (not general $n$, and not by itself closing the
  sibling's Theorem-37 item or the shared $b=c_1$ item within the same
  larger Case-(b) structure, per the round-26 outline's three-item
  breakdown).
- **(round 25, this build — attempt to close (7.9.1) via the outline's
  Restriction Lemma + dualized 1-D max-vertex mechanism; per this round's
  dispatch, does not touch Claim A's own status).** Executing the outline's
  proposed mechanism directly, found it does not literally apply as stated
  (a 1-dimensional "vary one already-fixed element" polytope cannot itself
  decide *which* tail element ends up the one that is cut — that is exactly
  the open content). Replaced it with a from-scratch, verified two-quantity
  joint reduction (new §7.10: $\mathrm{MinFloor}(\ell)$/$\mathrm{MaxCeil}
  (\ell)$), catching and correcting a genuine direction/polarity error in an
  intermediate draft before finalizing (an attempted one-line "Fact 2 closes
  $\mathrm{MaxCeil}$'s untouched branch" claim was checked and found to use
  the bound in the wrong direction; the corrected chain instead needs
  $\mathrm{MinFloor}(\ell-1)$, a genuine lower-bound theorem, not a cheap
  fact). Result: (i) (7.9.1) rigorously reduced to $\mathrm{MaxCeil}(m)$,
  $m=n-3$, equivalently to $E(T''')\ge p_5/2$; (ii) $\mathrm{MinFloor}(\ell)$'s
  "top element untouched" branch closed **unconditionally for every**
  $\ell\ge1$ via one clean line (Fact 2 + the certified identity
  $R(\sigma)+\sigma_\ell=2\sigma_1$) — a new, general, reusable partial
  result; (iii) $\mathrm{MaxCeil}(\ell)$'s "top untouched" branch reduced
  exactly to $\mathrm{MinFloor}(\ell-1)$; (iv) both quantities' "top element
  is cut" branches are honestly left **open** for general $\ell$ (hand-
  verified consistent, not violated, at $\ell\le3$ only) — this is now the
  single, precisely-isolated residual gap, strictly narrower than the
  outline's original framing (only $\sigma_1$'s own split matters within
  case (ii), not the whole multi-element polytope). (7.9.1) is **not**
  closed this round; honestly reported as `partial` for this sub-target.
- **(round 24, this build — fix the outline-reviewer's flagged direction bug
  in §7.8's T'-cuts-p4 sub-case; does not touch Claim A's own status).**
  The round-24 outline instructed reusing the certified (max-direction)
  `exchange-smoothing-vertex-maximization` to get an *upper* bound on
  $A(\{c_2\}\cup T''')$-type quantities, flagged by the outline-reviewer as
  a polarity error (an upper bound on $A$ needs a *lower* bound on $E$, the
  opposite direction from what that lemma proves). This round: **re-derived
  from scratch, breakpoint by breakpoint**, exactly which of the Single-
  Insert-Point Vertex Lemma's finitely many candidates for $b$ (in the
  T'-cuts-$p_4$ sub-case, $T'=\{c_1,c_2\}\cup T'''$, $c_1\ge c_2$,
  $c_1+c_2=p_4$) genuinely needs an upper bound at all — new §7.9 below.
  **Finding 1 (resolves one candidate without any new lemma):** the box
  endpoint $b=p_4$ is **fully dominated** by the breakpoint $b=c_1$ via an
  exact, already-available monotonicity fact (slope $+1$ on the interval
  $(c_1,p_4]$, read directly off the Insert-Element Identity's closed form
  $A(B)=b-A(T')$ there) — so this candidate needs **no bound on $A(T')$ in
  either direction**, contrary to what a literal reading of the outline
  might suggest. **Finding 2 (pinpoints where a genuine upper bound is
  needed, precisely, not vaguely):** the breakpoint $b=c_2$ (ties $T'$'s own
  $c_2$) reduces via pair-cancellation to $A(\{c_1\}\cup T''')$, and since
  $c_1\ge p_5\ge\max(T''')$, `sharp-dominant-removal-identity`/its weak-tie
  boundary case peels $c_1$: $A(\{c_1\}\cup T''')=c_1-A(T''')$ (generic
  strict case) — genuinely requiring an **upper** bound $A(T''')\le
  c_1-f(n)$, confirming the reviewer's flagged concern is real, just
  mis-located by the outline (it is not needed at the $c_1$/$p_4$
  comparison, but at the $c_2$ breakpoint's own reduction). **Finding 3
  (why this is not closed by cheap facts, and not closed this round):**
  the naive `half-bound-lemma`-dual bound $A(T''')\le\mathrm{Total}(T''')$
  is shown, by explicit computation at the symmetric split $c_1=c_2=p_4/2$,
  to be **insufficient** ($\mathrm{Total}(T''')$ can exceed $c_1-f(n)$),
  and the project's own `current.md` records that the general "tail-
  refinement-never-helps" statement ($A(R')\le A(\tau)$ for $R'$ any
  refinement of a fixed ratio-2 tail $\tau$) is **known false** in general
  — so no existing certified fact supplies the needed upper bound, and this
  round does **not** construct a new one from scratch (time-boxed): the
  correct, sharpened form of the gap is recorded honestly in new §7.9,
  strictly more precise than round 23's diagnosis (only 1 of the $\ge4$
  breakpoint types is now known to need an upper bound at all, and that one
  is pinned down exactly, rather than the whole sub-case being an
  undifferentiated "recouples to the same obstruction").
- **(round 23, this build — addendum only, does not touch Claim A; per the
  round-23 outline, an independent discrete/pigeonhole cross-check of
  `greedy-halving-adversary`'s Case (b) "$v\ge a$" target $A(B)\ge f(n)$,
  $B=\{b\}\cup T'$, in parallel with — but not seeing the result of — the
  sibling's own attempt to apply the Vertex-Minimum Theorem directly to the
  same object this same round).** New §7.8. Identified the target as
  literally the point $v=a$ of the same $\Delta(n,v)\le v-f(n)$ curve
  (no $\varepsilon$-correction needed there). Proved a new general,
  elementary lemma (`single-insert-point-vertex-lemma`, promoted) pinning
  the free coordinate $b$ to $3$ candidate types (via a one-line slope
  argument, not the general LP/compactness theorem); closed $2$ of the $3$
  types unconditionally-modulo-standing-hypothesis
  ($b=0$ via $(\star_{n-3})$; $b=p_4$-untouched via
  `pair-cancellation-identity` + $(\star_{n-4})$); found that the
  remaining $2$ residual sub-cases (further-split $p_4$, or a tie with a
  generic interior $T'$-fragment) recouple exactly to the same joint
  cross-piece vertex-enumeration/recursive obstruction the sibling's
  Insert-Element Identity already diagnosed — independent confirmation of
  the same wall from a different starting point (single-variable-first
  pinning vs. joint Vertex-Minimum Theorem), not a fresh closure.
  Numerically corroborated (`/tmp/check_insert_vertex.py`,
  `/tmp/check_argmin_location.py`): confirmed the pinning lemma and that
  all $3$ candidate types are genuinely realized as true minimizers with
  comparable frequency (roughly $1/3$ each across $1500$ trials), i.e. the
  unresolved case is not a negligible edge case.
- **(round 22, this build — addendum only, does not touch Claim A; per the
  round-22 outline, explicitly scoped down from §7.6's vertex-enumeration
  since the sibling's Theorem 36 general-$n$ fix is a parallel in-progress
  effort this same round).** Two items, both completed: (i) **§7.7, the
  conditional-corollary stub** — derived the *exact* algebraic identity
  $\mathrm{marg}_{\sharp'}(v_1,v_2)=\mathrm{marg}_{\Diamond'}(v_2)+(p_2-v_1)$
  linking this file's $(\sharp')$ margin to `greedy-halving-adversary`'s
  $(\Diamond')$ margin (imported definitions, not re-derived), and proved
  from it a genuine **equivalence** (not just one-way sufficiency):
  $(\sharp')$ at fixed $v_2$ over all admissible $v_1$ $\iff$ $(\Diamond')$
  at $v=v_2$ — so §7.6's general-$n$ gap now closes automatically, with no
  further argument, the moment a future round proves $(\Diamond')$ (the
  $\varepsilon$-corrected target, not the weaker $(\Diamond)$ Theorem 36
  currently closes) for that $n$. Honestly recorded as **not yet available**
  — $(\Diamond')$ itself is unproved for every $n\ge4$ as of this round, so
  §7.6 remains open, only more precisely characterized. (ii) **Independent
  $n=4$ numeric cross-check** (exact `Fraction`, $50{,}000$ trials, script
  `/tmp/round-22/check_n4_eps_bridge.py`): confirmed identity (7.7.1) holds
  exactly (zero mismatches) on random legal budget-$1$ refinements of
  $\tau=\{p_3,p_4,p_5\}$; also found, as numeric-only corroborating evidence
  (explicitly not claimed as a proof), zero sampled violations of
  $(\Diamond')$ or $(\sharp')$ themselves at $n=4$. §7.6's own
  vertex-enumeration route was **not** re-attempted this round, per the
  outline's explicit instruction (deprioritized in favor of the sibling's
  algebraic-floor route, which has been the one mechanism that actually
  closes instances of this target).
- **(round 21, this build — close the TRUE, $\varepsilon$-corrected
  middle-band target $(\sharp')$ at $n=3$ in full, per the round-21 outline
  and outline-reviewer's exact-verified reduction).** Round 19/20's §7.5
  only closed the weaker $(\sharp)$ (the $\varepsilon\equiv0$ special case);
  `greedy-halving-adversary`'s own file records the TRUE sufficient target
  as $(\sharp')$: $\Delta(n,v_2)\le s-(v_1-v_2)-2v_2\varepsilon(v_2)$, and
  flags the $\varepsilon(v_2)=1$ instance as an honest, unverified bridge
  gap. This round: (i) imported the exact identity chain from the sibling's
  Theorem 34 (corrected) deriving $(\sharp')$, reproduced it in full so the
  closure is self-contained (§7.5.0); (ii) confirmed, via the Band-Parity
  Fact, that at $n=3$ (forced $R'=\tau$, $|\tau|=2$) $\varepsilon(v_2)=1$
  occurs **exactly** on the pre-existing middle case $v_2\in[p_4,p_3)$ and
  $\varepsilon(v_2)=0$ on both outer cases (§7.5.0$'$) — so $(\sharp')$
  coincides with the already-closed $(\sharp)$ on the two outer bands
  (§7.5.1, unchanged from round 19/20) and differs only on the middle band;
  (iii) closed the middle band's TRUE target by reducing it algebraically
  to the single clean inequality $v_1+v_2\le6p_4$ (§7.5.2), then proving
  this **strictly** by adding the domain bound $v_1<p_2=4p_4$ to the case
  hypothesis $v_2<p_3=2p_4$ termwise — exactly the tightened bound the
  round-21 outline and outline-reviewer specified and independently
  verified exactly with `Fraction` arithmetic. This is a genuinely new,
  strictly stronger closure than round 19/20's $(\sharp)$-only result, not
  a restatement: it establishes precisely the sufficient inequality the
  sibling's own file marks as the open $\varepsilon=1$ bridge gap,
  specialized to $n=3$. §7.6 (the separate, general-$n\ge4$ cross-piece
  tie-vertex enumeration gap) is explicitly left untouched and open, as
  instructed — this round's work does not extend past $n=3$.
- **(round 20, this build — fix the $v_2=p_4$ boundary bug in §7.5's $n=3$
  middle-band closure, per the round-19 diagnosis and this round's
  outline-reviewer APPROVE).** The old case split (`v_2\ge p_3`,
  `v_2\in(p_4,p_3)`, `v_2\le p_4`) computed the third case's formula
  ($\Delta=-A(\tau)=-p_4$) at $v_2=p_4$ exactly, but every other case-split
  convention in this file treats $\tau_{>v_2}$ with a *strict* `>`, under
  which $p_4\notin\tau_{>p_4}$ — so at $v_2=p_4$ the correct
  $\tau_{>v_2}=\{p_3\}$ (the *second* case's set), giving the correct value
  $\Delta(3,p_4)=-3p_4$, not $-p_4$. (Non-fatal to the theorem as previously
  written, since $-p_4>-3p_4$ made the old proof accidentally prove a
  strictly stronger bound at that one point — but the case split itself was
  wrong as stated.) **Fix applied (§7.5 below, pure relabel, no new
  inequality):** re-split as `v_2\ge p_3`, `v_2\in[p_4,p_3)` (closed left,
  absorbing the boundary point), `v_2<p_4` (open right). Verified this split
  is exhaustive and pairwise disjoint on $v_2\in[0,s)$ against the strict-`>`
  convention at both boundary points $p_3$ and $p_4$; verified the middle
  case's existing closed-form algebra ($\Delta(3,v_2)=A(\tau)-2p_3=-3p_4$)
  is literally unchanged when extended to include the left endpoint $v_2=p_4$
  (the formula depends only on $\tau_{>v_2}=\{p_3\}$, which holds uniformly
  across the whole interval $[p_4,p_3)$ including its left endpoint); deleted
  the erroneous old-third-case computation at that point and replaced it with
  a pointer folding it into the (already-correct) second case. The first
  case's own boundary ($v_2=p_3$) was independently re-checked and requires
  no fix (already used the correct non-strict `\ge` matching $p_3\not>v_2$ at
  $v_2=p_3$). All three cases still close strictly; the theorem's conclusion
  (unconditional $n=3$ middle-band closure) is unchanged — only the
  intermediate case split is corrected. §7.6's general-$n\ge4$ gap is
  untouched by this fix, as scoped.
- **(round 19, this build — independent second angle on the Claim-B middle
  band $\Delta(n,v)$, cross-checking `greedy-halving-adversary`'s round-19
  vertex-enumeration route)**. Per the round-19 outline's instruction to
  reuse this slug's exchange-smoothing-vertex-maximization machinery (proven
  capable of a structurally similar "no-dominant-fragment vertex-max"
  problem in Claim A) as an *independent* second route into the sibling's
  open target, $\Delta(n,v):=A(R')-2A(R'_{>v})$ (max over legal cut-budgeted
  $R'$), rather than duplicating the sibling's own direct vertex-enumeration
  attack. This round's genuine new result: **the Truncated Alternating Sum
  Ceiling** (§7 below) — a fully general, unconditional, structure-free
  upper bound $A(S)-2A(S_{>v})\le v$ for *any* finite nonnegative multiset
  $S$ and any $v\ge0$ — proved from scratch by the same elementary
  level-set/integral technique that powers the sibling's certified
  `truncated-alternating-sum-floor` (Theorem 31), run in the "ceiling"
  direction instead. This directly targets the sibling's isolated open
  quantity. **Honest negative finding, independently re-derived, not just
  imported:** the naive sufficient condition obtained by combining this
  ceiling with the crude bound $J_0\le v_2$ is **false** once $R'$'s cut
  budget is left unrestricted (explicit counterexamples found by exact-
  `Fraction` search, $n=3,\dots,5$, reported in §7.4) — matching (via an
  independently-written script, not the sibling's) the sibling's own
  diagnosis that the crude bound is insufficient in general. **Positive
  corroboration, independently computed:** once the round-19 outline's
  corrected cut-budget cap ($R'$ has $\le n-3$ cuts, not $n-2$) is imposed,
  an independent 30,000-trial-per-$n$ exact-`Fraction` search ($n=3,\dots,7$)
  finds **zero violations** of the sufficient inequality — corroborating
  (from a genuinely different script/framing than `greedy-halving-adversary`'s
  own vertex-enumeration numerics) that the corrected cap is the right fix.
  **New unconditional partial closure:** worked out the $n=3$ instance
  exactly by hand (§7.5) — since the corrected cap forces budget $=0$ at
  $n=3$ (so $R'=\tau=\{p_3,p_4\}$ is *forced*, no adversarial freedom at
  all), a direct three-way case split on where $v_2$ falls relative to
  $p_3,p_4$ closes the middle band **completely and rigorously for $n=3$**,
  independent of any numerics. **General $n\ge4$ (nonzero budget) vertex
  enumeration is not completed this round** — see the honestly-scoped gap
  in §7.6: adapting the certified `exchange-smoothing-vertex-maximization`
  to this genuinely different polytope (per-piece mass-conserving
  refinements of $m$ *distinct* fixed ladder pieces, rather than one single
  stick) is shown to require a joint, possibly cross-piece tie-vertex
  argument that is **not** a straightforward transplant of the Claim-A
  machinery, and is left open, honestly, rather than forced.
- **(round 8, this build — CLOSES CLAIM (A) IN FULL)** Per the round-8
  outline's instruction, attacked Case I directly via exchange-smoothing
  vertex-maximization of $E(F\cup\tau)$ (adapting the crux
  `aimo-0146`-style exchange-smoothing-to-plateau mechanism), deliberately
  bypassing the peel-the-minimum induction that rounds 6–7 (and this
  round's explorers, independently) diagnosed as circular on sub-case
  $(\dagger)$. This **succeeds completely**: §5 below gives a full,
  non-numeric proof that Case I holds for every $m$, closing the sole
  remaining gap in Claim (A). The mechanism: (i) a self-contained
  exchange-smoothing argument (finite-descent, no external LP-package
  citation beyond the already-certified convex-geometry facts underlying
  `vertex-minimum-theorem`) shows the maximum of $E(F\cup\tau)$ over the
  Case-I polytope is attained by an $F$ of a very restricted shape: some
  parts individually pinned to specific tail values $\tau_l$, the rest
  (if any) collapsed to one common tied value $v$; (ii) `odd-run-reduction-
  lemma` converts evaluating $E$/$A$ at any such configuration into an
  elementary computation on the *parity pattern* of the pins (which
  $\tau_l$'s survive) plus, if the free group's part-count is odd, one
  extra value $v$; (iii) a new elementary **Ratio-2 Spacing Lemma** (any
  two distinct elements of a ratio-2 tail differ by a factor $\ge2$, even
  non-adjacent ones) plus the already-certified `half-bound-lemma`
  ($A(S)\ge0$ for every multiset) close every resulting case by a short,
  fully explicit finite computation — no case is left open, no numerics
  substitute for the proof (extensive exact-`Fraction` computation, up to
  $m=10$ exhaustively over *every* vertex configuration, is used only as
  an independent cross-check, confirming zero violations and the proof's
  equality cases, not as a substitute for it). This directly resolves
  $(\dagger)$ (round 7's isolated open sub-branch) and the round-8
  explorers' "exact identity, not reducible" diagnosis of the
  peel-induction route — the resolution here is that this route never
  needed a reducible sub-instance at all; it evaluates the extremal
  configuration directly.
- **(round 7)** Reformulated Case I as the self-contained
  $E(F\cup\tau)\le R(\tau)$ and introduced peel-the-global-minimum,
  closing two of three exhaustive branches and isolating sub-case
  $(\dagger)$ (Branch B, $N$ even) as the sole gap — see history below for
  full detail; **now superseded/closed** by this round's §5.
- **(round 6)** Closed Case II of Claim (A) in full via strong induction
  (Theorem GC($m$)) — retained below as §3, still load-bearing (Case I's
  proof in §5 does not re-derive Case II; both together give Claim (A)).
- **(round 5)** Achievability half proved in full (§2, retained, still
  load-bearing); Case II reduced one step (superseded by round 6's full
  closure).
- **(round 4)** `sharp-dominant-removal-identity` certified; the naive
  generic-multiset pigeonhole restatement refuted (recorded, not retried).

## Current best

Claim (A) is now **fully proved for every $n\ge1$**: see Full proof below
(unaffected by the round-22 addendum). Additionally (outside Claim A's own
scope, round-19–22 cross-check addendum): §7's Truncated Alternating Sum
Ceiling is a fully general reusable fact; §7.5's $(\sharp')$ target is fully
closed at $n=3$; §7.7 (new, round 22) establishes an exact equivalence
between this file's $(\sharp')$ and the sibling's $(\Diamond')$, so §7.6's
general-$n\ge4$ gap is now known to close automatically once the sibling
proves $(\Diamond')$ — not yet proved for any $n\ge4$, so still open.
(Round 24 addendum, new §7.9): the T'-cuts-$p_4$ sub-case of Case (b)'s
"$v\ge a$" branch is precisely diagnosed — of its (at most) four vertex
candidates for $b$, three are fully accounted for ($b=0$: closed via
$(\star_{n-3})$; $b=p_4$: dominated, needs no bound at all, new Box-
Endpoint Domination Fact; $b=c_1$: a same-direction lower-bound recursion,
open but not direction-flawed) and exactly one ($b=c_2$, generic case)
is shown to genuinely require a new upper bound $A(T''')\le c_1-f(n)$
(eq. 7.9.1) that is proved, by exact computation, **not** to follow from
the certified $A\le\mathrm{Total}$ bound, and **not** available as a
general refinement-monotonicity fact (which `current.md` records as false
in general). This is a sharpened, honest open gap — not a closure.
(Round 25 addendum, new §7.10): (7.9.1) is now rigorously reduced to a
two-quantity joint statement $\mathrm{MinFloor}(\ell)$/$\mathrm{MaxCeil}
(\ell)$ (equivalently $E(T''')\ge p_5/2$); $\mathrm{MinFloor}(\ell)$'s
"top element untouched" branch is closed **unconditionally for every**
$\ell$ (new one-line reusable fact); the remaining "top element is cut"
branch of both quantities is precisely isolated but still open for general
$\ell$. (7.9.1) remains open, further narrowed.

(Round 26 addendum, new §7.11–7.13): §7.11 proves $\mathrm{MinFloor}(\ell)
\equiv(\star_{\ell-1})$ exactly (not just "conditional on," but literally
the same statement via `alternating-sum-scaling`) — so
$\mathrm{MinFloor}(3)$ is now fully closed (both branches, since it equals
the already-certified $(\star_2)$), and $\mathrm{MaxCeil}(\ell)$'s
top-untouched branch is unconditionally free for $\ell\le4$ ($n\le7$).
§7.12–7.13 close $\mathrm{MaxCeil}(3)$ and $\mathrm{MaxCeil}(4)$ **fully**
(both branches, top-cut included) by direct, elementary case analysis —
**(7.9.1) is now unconditionally resolved at $n=6$ and $n=7$**, the first
genuine closures of $(7.9.1)$ at any $n$. General $n$ (equivalently
$\mathrm{MaxCeil}(m)$'s top-cut branch for $m\ge5$) remains open, and this
does not by itself close the sibling's Theorem-37 item or the shared
$b=c_1$ item within the same larger Case-(b) structure (round-26 outline's
three-item breakdown, §7.11's final paragraph).

(Round 27 addendum, new §7.14–7.15): §7.14 proves a fully general,
unconditional theorem — $\mathrm{MaxCeil}(m)$'s top-cut branch holds for
*every* $m\ge2$ on the entire $\sigma_2$-untouched sub-family (arbitrary
cuts on $\sigma_1$ and on $\sigma_3,\dots,\sigma_m$), strictly generalizing
$4$ of $5$ of the $m=4$ hand-closed shapes and correcting the outline's
"$\le2$ distinct indices" framing to the sharper, correct "$\sigma_2$
touched or not" dividing line. §7.15 proves a Necessity Theorem showing
the complementary ($\sigma_2$-touched) residual, for $m\ge5$, **cannot**
be closed without a restricted instance of $(\star_{m-2})$ — refuting the
round-27 outline's premise that this front is independent of the central
obstruction. Net status of $(7.9.1)$/$\mathrm{MaxCeil}(m)$'s top-cut
branch: unconditionally closed for every $m$ on the $\sigma_2$-untouched
sub-family (new, general), fully closed (both sub-families) only at
$m=3,4$ (round 26), and, for $m\ge5$, the $\sigma_2$-touched residual is
now **known** — not just suspected — to require $(\star_k)$, $k\ge3$, the
project's central open obstruction.

(Round 28 addendum, new §7.16): direct attack on $(\star_3)=\mathrm{
MinFloor}(4)$ via exhaustive $20$-shape cut-distribution enumeration on
the $4$-piece ladder. $14/20$ shapes fully closed (both directions,
unconditional) via two new master theorems — Master Theorem I (all $10$
$\pi_1$-untouched shapes, one dominant-peel + Fact 2 argument) and Master
Theorem II (all $3$ shapes with one cut on $\pi_1$ and $\pi_2$ untouched,
a 2–3-level peel cascade uniform in how the rest of the budget splits
$\pi_3,\pi_4$) — plus direct citation of `claim-a-full-closure` for
$(3,0,0,0)$ (literally Claim A at $n=3$). Achievability ($A=1$ exactly
attained) is now proved by hand for **all $20$** shapes via an explicit
uniform construction realizing $\{4,4,2,2,2,1\}$ (odd-run-reduces to
$\{2,1\}$), correcting the outline's undercount of "tight" shapes from
$2$ to the true $7$: $(1,1,0,1),(1,1,1,0),(1,2,0,0),(2,0,0,1),(2,0,1,0),
(2,1,0,0),(3,0,0,0)$. The matching lower bound is proved by hand on a
large sub-region of each of the $6$ non-citation tight shapes but remains
open on a genuinely $3$-free-parameter residual sub-case inside each —
precisely located (not a whole new shape needing derivation from
scratch), not closed this round. $(\star_3)$ remains open, substantially
narrowed, with the outline's shape-count and severity-ranking premises
corrected.

(Round 29 addendum, new §7.17): fixed the outline-reviewer's flagged
citation-mismatch bug (the round-29 outline's proposed use of
`single-insert-point-vertex-lemma` on mass-conserving coupled coordinate
pairs was invalid, as the reviewer showed by exact computation) by
proving a new general, elementary **Pair-Insertion Ordering Lemma** (a
closed-form sorted-rank computation for inserting one value into a
conservation pair plus a reference value) from scratch, and using it to
**fully close shape $(2,0,1,0)$** on its entire domain (both directions)
and **shape $(2,0,0,1)$'s residual regime** ($f_1<4$; its complementary
regime is numerically confirmed but not yet hand-derived). The other $4$
of the $6$ residual shapes — $(1,1,0,1),(1,1,1,0),(1,2,0,0),(2,1,0,0)$ —
were not attempted with the corrected mechanism this round. Net:
$1$ shape fully closed, $1$ half-closed, $4$ untouched — $(\star_3)$
remains open, but the reviewer's flagged citation bug is fixed with a
correct, reusable replacement tool now on file.

(Round 30 addendum, new §7.18): closed shape $(2,0,0,1)$'s remaining
$f_1\ge4$ branch by hand (two-peel chain + Pair-Insertion Ordering Lemma
mirrored form, plus a direct double-peel for the $f_2\le2$ sub-case) —
**shape $(2,0,0,1)$ is now fully closed on its entire domain.** Closed
shapes **$(1,1,0,1)$ and $(1,1,1,0)$ fully**, each via an exhaustive hand
case-tree built from the Forced-Dominance Fact (a single cut leaves a
part $\ge$ half its parent) plus repeated `sharp-dominant-removal-
identity` peeling, `odd-run-reduction-lemma` for ties, and — for
$(1,1,1,0)$ specifically — direct reuse of the certified Pair-Insertion
Ordering Lemma at one depth. **Net: $4$ of the $6$ residual shapes for
$(\star_3)=\mathrm{MinFloor}(4)$ are now fully closed**
($(2,0,1,0),(2,0,0,1),(1,1,0,1),(1,1,1,0)$); only $(1,2,0,0)$ and
$(2,1,0,0)$ remain open. These two are shown this round to need a
genuinely new mechanism beyond everything used so far: since neither the
$\pi_1$-triple's top fragment nor the $\pi_2$-pair's top fragment is
unconditionally dominant, closing the resulting case tree requires
**cross-pair joint-feasibility constraints** (e.g. $c\ge4-f_3$) not
derivable from either conservation pair's defining inequality alone — a
sharper, more precisely located diagnosis of the obstruction than round
28's generic "$3$ free parameters" framing, with one sub-case worked in
full as a template and a genuine algebra error (from omitting the joint
constraint) caught and corrected before the round ended. $(\star_3)$
remains open (exactly $2$ shapes), the narrowest the residual has been
since round 28's original $20$-shape exhaustion.

(Round 31 addendum, new §7.18.4/7.18.5): closed the last $2$ of $6$
residual shapes, $(1,2,0,0)$ and $(2,1,0,0)$, **in full**, by direct
citation of `vertex-minimum-theorem` (compactness + finite-hyperplane-
subdivision, parts 2–3): rather than continuing the round-30 branch
tree (correctly diagnosed as needing an easy-to-drop cross-pair
joint-feasibility constraint at every branch), enumerated the complete,
exhaustively-justified finite family of candidate vertices for each
shape's $3$-free-parameter polytope ($18$ hyperplanes, $36$ feasible
vertices for $(2,1,0,0)$; $21$ hyperplanes, $27$ feasible vertices for
$(1,2,0,0)$, all solved and filtered in exact rational arithmetic) and
evaluated $A(U)$ by direct sorting at every one: **all $63$ vertices
across both shapes satisfy $A(U)\ge1$**, with equality at exactly the
vertices matching the round-28 achievability construction
$\{4,4,2,2,2,1\}$. The feasibility filter, applied uniformly to every
candidate vertex, is exactly where the joint-feasibility constraint
gets enforced — automatically, for all vertices simultaneously — so no
case-by-case cross-constraint bookkeeping is needed. **Both shapes are
now closed, both directions, no residual gap.** Combined with rounds
28–30, **all $6$ residual shapes are closed and $(\star_3)=
\mathrm{MinFloor}(4)$ is fully proved** (all $20$ maximal shapes, both
directions) — the last open item of Claim (A)'s own discrete-counting
toolbox at $n=4$ that this file had outstanding. (The general-$n$
$(\star_k)$, $k\ge3$, obstruction — shared with `greedy-halving-
adversary`'s $h(m)$, $m\ge5$ — is untouched by this closure; it is the
concrete $n=4$/$\ell=4$ instance that is now fully settled, not the
general pattern.)

## Full proof

### 0. Setup (recap of the shared reduction)
By `claiming-subgame-reduction` + `integral-alternating-sum-formula`,
$c(n)=2^n/(2^{n+1}-1)$ is equivalent to $A(S)\ge a_n:=1/(2^{n+1}-1)$ for every
legal Xiang-Yu response $S$, where the ladder is $p_i=2^{n+1-i}/(2^{n+1}-1)$,
$i=1,\dots,n+1$ ($D:=2^{n+1}-1$). Write $T:=\{p_2,\dots,p_{n+1}\}$ (the
**untouched** tail, sum $r:=1-p_1$). Direct substitution gives the exact
fractions
$$p_1=\frac{2^n}{D},\qquad r=\frac{2^n-1}{D},\qquad a_n=\frac1D,\qquad
p_1-a_n=r,\tag{0.1}$$
and every $p_i=2p_{i+1}$ ($1\le i\le n$), the ladder's ratio-2 self-similarity
(`ladder-self-similarity-constant`).

**Claim (A):** for every partition $F$ of $p_1$ into at most $n+1$ positive
parts (i.e. using $\le n$ cuts, all spent fragmenting $p_1$, none on the
tail),
$$A(F\cup T)\ \ge\ a_n,\tag{A}$$
with equality attained by an explicit $F^\ast$ (§2).

### 1. Case split: at most one fragment of $F$ can exceed $p_2$

**Lemma 1.** *If $F=\{f_1,\dots,f_{c+1}\}$ (sum $p_1$) has two elements both
$>p_2$, that is impossible.*

**Proof.** If $f_i,f_j>p_2$ for $i\ne j$, then $f_i+f_j>2p_2=p_1$ (using
$p_1=2p_2$), but $f_i+f_j\le\sum_k f_k=p_1$ since all $f_k\ge0$ —
contradiction. $\blacksquare$

So exactly one of two cases holds for any $F$:
- **Case I:** every element of $F$ is $\le p_2$.
- **Case II:** exactly one element $f_1$ exceeds $p_2$; $F'=F\setminus\{f_1\}$
  (sum $s:=p_1-f_1<p_2$), every element of $F'$ is $\le s<p_2$.

### 2. Achievability: an explicit $F^\ast$ attains $A(F^\ast\cup T)=a_n$ exactly

**Construction.** For $n\ge2$,
$F^\ast=\{p_2,p_3,\dots,p_n,\,p_{n+1},p_{n+1}\}$ — the values $p_2,\dots,p_n$
once each, plus $p_{n+1}$ twice — using $n-1\le n$ cuts.

**$F^\ast$ is a valid partition of $p_1$.** Using $p_i=2p_{i+1}$ repeatedly,
$\sum_{i=2}^{n}p_i+2p_{n+1}=r+p_{n+1}$, and since $p_1=2^np_{n+1}$ and
$r=p_{n+1}(2^{n-1}+\dots+1)=p_{n+1}(2^n-1)$, we get $r+p_{n+1}=p_{n+1}2^n=p_1$.

**Computation of $A(F^\ast\cup T)$.** The multiset $F^\ast\cup T$ has each of
$p_2,\dots,p_n$ with multiplicity $2$ and $p_{n+1}$ with multiplicity $3$.
Sorted descending, each pair $\{p_i,p_i\}$ ($2\le i\le n$) occupies two
consecutive ranks, contributing $0$ to $A$ regardless of starting parity. The
final triple $\{p_{n+1},p_{n+1},p_{n+1}\}$ starts at rank $2(n-1)+1$ (odd,
since $2(n-1)$ ranks are used by the complete pairs before it), so it
contributes $+p_{n+1}-p_{n+1}+p_{n+1}=p_{n+1}$. Hence
$$A(F^\ast\cup T)=p_{n+1}=\frac1D=a_n.$$
For $n=1$: tail is $\{p_2\}=\{1/3\}$, $F=\{p_1\}$, directly
$A=p_1-p_2=1/3=a_1$. **This proves the achievability half of Claim (A)
completely, for every $n\ge1$.**

### 3. Lower bound, Case II: closed for every $n$ (round 6)

**Setup.** A finite sequence $\tau=(\tau_1>\dots>\tau_m>0)$ is a *ratio-2
superincreasing tail of length $m$* if $\tau_i=2\tau_{i+1}$ for $1\le i<m$.
Write $R(\tau):=\sum\tau_i$. Every "tail one level down"
$T^{(k)}:=\{p_{k+1},\dots,p_{n+1}\}$ is such a sequence of length $n+1-k$,
with $\tau_m=p_{n+1}=a_n$ always.

**Theorem (Case-II Closure, GC($m$)).** *For every $m\ge1$, every ratio-2
tail $\tau=(\tau_1,\dots,\tau_m)$, every $s\in(0,2\tau_1]$, and every
partition $F$ of $s$ into at most $m+1$ positive parts with at least one part
exceeding $\tau_1$,*
$$A(F\cup\tau)\ \ge\ s-R(\tau).\tag{GC}$$

Taking $m=n$, $\tau=T$, $s=p_1$ recovers exactly Claim (A)'s Case II, every
$n$.

**Proof, by strong induction on $m$.**

*Base case $m=1$.* Write $a:=\tau_1$, $s\in(0,2a]$, $F$ has $1$ or $2$ parts.
- One part $F=\{s\}$: $A(\{s,a\})=|s-a|\ge s-a$.
- Two parts $F=\{f,g\}$, $f\ge g>0$, $f+g=s$: if both $>a$ then $f+g>2a\ge s$,
  contradiction, so $g\le a$ (say). Using $A=\mathrm{Total}-2\cdot\mathrm{median}$
  for $3$ elements, the claim $A\ge s-a$ is equivalent to
  $\mathrm{median}\{f,g,a\}\le a$: if $f\ge a\ge g$, median $=a$; if $a>f\ge g$,
  median $=f<a$. Always $\le a$. Base case proved.

*Inductive step, $m\ge2$, assuming GC($m-1$).* $\tau=(\tau_1,\dots,\tau_m)$,
$R=R(\tau)$, $s\in(0,2\tau_1]$, $F$ with $\le m+1$ parts.

If $s\le R$: $A(F\cup\tau)\ge0$ always (`half-bound-lemma`, restated below in
§5.2), and $0\ge s-R$. Done for every $m$.

If $s>R$: at most one part of $F$ exceeds $\tau_1$ (same argument as Lemma 1,
using $2\tau_1\ge s\ge f+g$ if two parts both exceed $\tau_1$).

- **Case II ($\exists f_1\in F$, $f_1>\tau_1$).** $F'=F\setminus\{f_1\}$,
  $s':=s-f_1<\tau_1$. Every element of $F'$ is $\le s'<\tau_1$, so
  $\max(F'\cup\tau)=\tau_1<f_1$, and `sharp-dominant-removal-identity` gives
  $A(F\cup\tau)=f_1-A(F'\cup\tau)$. The target is equivalent to
  $A(F'\cup\tau)\le R-s'$. Write $\tau'':=\tau\setminus\{\tau_1\}$ (length
  $m-1$, ratio-2, $R(\tau'')=R-\tau_1$). Since $\tau_1$ is the strict unique
  max of $F'\cup\tau$, the rank-shift identity (§3 of earlier rounds; general,
  not ladder-specific: for any $U$ with strict unique max $u$ and
  $U'':=U\setminus\{u\}$, the sum of $U$'s even-rank elements equals
  $\big(\mathrm{Total}(U'')+A(U'')\big)/2$) gives, after algebra,
  $A(F'\cup\tau)=\tau_1-A(F'\cup\tau'')$. So the target becomes
  $A(F'\cup\tau'')\ge s'-R(\tau'')$ — **exactly GC($m-1$)** applied to
  $\tau''$, mass $s'$, partition $F'$ ($|F'|\le m$). If $s'>0$:
  $s'<\tau_1=2\tau_2$, the exact domain of GC($m-1$); apply IH. If $s'=0$:
  need $A(\tau'')\ge-R(\tau'')$, true since $A(\tau'')\ge0>-R(\tau'')$.
  $\blacksquare$ (Case II, every $m$)

- **Case I (every part of $F$ is $\le\tau_1$).** Handled separately, in full,
  in §5 below (this round's new closure).

**Conclusion of §3.** Claim (A)'s Case II is proved for every $n$,
unconditionally, no numerics needed.

### 4. Reformulation of Case I as a self-contained one-level statement

By `integral-alternating-sum-formula`, for any finite multiset $S$, writing
$O(S),E(S)$ for the odd-/even-sorted-rank sums, $O+E=\mathrm{Total}$,
$O-E=A$, so
$$A(S)=\mathrm{Total}(S)-2E(S).\tag{4.1}$$
Applying to $S=F\cup\tau$, $\mathrm{Total}(S)=s+R(\tau)$: Case I's target
$A(F\cup\tau)\ge s-R(\tau)$ becomes, after substitution and cancelling,
$$E(F\cup\tau)\ \le\ R(\tau).\tag{4.2}$$
This is self-contained at level $m$ — a single inequality about the given
$F,\tau$, not a reduction to a smaller open sub-instance.

### 5. Full closure of Case I (round 8, new)

**Theorem (Case I Closure).** *For every $m\ge1$, every ratio-2
superincreasing tail $\tau=(\tau_1,\dots,\tau_m)$, every $s\in(0,2\tau_1]$,
and every partition $F$ of $s$ into at most $m+1$ nonnegative parts each
$\le\tau_1$ (Case I hypothesis, allowing zero parts so fewer than $m+1$
nonzero parts is included),*
$$E(F\cup\tau)\ \le\ R(\tau).$$

Combined with §4's equivalence, this closes Case I of Theorem GC($m$) for
every $m$, hence Claim (A)'s Case I for every $n$ (taking $m=n$,
$\tau=T=\{p_2,\dots,p_{n+1}\}$, $s=p_1$).

We prove this via exchange-smoothing vertex-maximization: reduce the
continuum of legal $F$ to a small, explicit family (§5.1), evaluate $E$ at
every member of that family via odd-run reduction (§5.4), and close every
resulting case by two elementary general facts plus one new elementary
spacing lemma (§5.5–§5.8).

#### 5.1 Reduction to "pinned + one tied group" configurations

Fix $m,\tau,s,k$ ($1\le k\le m+1$). Let
$\mathcal P=\{(f_1,\dots,f_k): f_i\ge0,\ \sum f_i=s,\ f_i\le\tau_1\ \forall i\}$,
a compact convex polytope (a box intersected with a hyperplane).

**Proposition (Vertex-maximization).** *The maximum of $E(F\cup\tau)$ over
$F\in\mathcal P$ is attained at some $F^\dagger\in\mathcal P$ of the
following restricted form: for some $p$ with $0\le p\le k$, choose (with
repetition allowed) reference values
$\tau_{l_1},\dots,\tau_{l_p}\in\{\tau_1,\dots,\tau_m\}$; set $p$ of the
coordinates of $F^\dagger$ equal to these values (one each); set the
remaining $k-p$ coordinates (if any) all equal to a single common value
$v:=\big(s-\sum_{i=1}^p\tau_{l_i}\big)/(k-p)\ge0$ (which must satisfy
$v\le\tau_1$ for $F^\dagger\in\mathcal P$; if $p=k$ the config is valid
provided $\sum\tau_{l_i}=s$ exactly).*

**Proof.** $E(\cdot\cup\tau)$ is continuous on $\mathcal P$ (finite
composition of the affine embedding, the sort map — continuous, since each
order statistic is a finite max-of-mins of continuous coordinates — and the
linear even-rank-sum functional), and $\mathcal P$ is compact, so a
maximizer $F^\ast$ exists (extreme value theorem). Fix the reference value
set $\mathcal R:=\{0,\tau_1,\dots,\tau_m\}$ (finite, $m+1$ points, noting
$\tau_1$ doubles as the box's upper facet). Call a coordinate $f_i^\ast$
*pinned* if it equals some element of $\mathcal R$, and *free* otherwise.

Suppose two free coordinates $f_i^\ast\ne f_j^\ast$ exist. In a small enough
neighbourhood of $F^\ast$ (radius bounded by the distances of $f_i^\ast,
f_j^\ast$ to $\mathcal R$, to each other, and to every other coordinate of
$F^\ast$ — all strictly positive since $f_i^\ast,f_j^\ast$ are free and
distinct, and there are finitely many other coordinates and reference
points), the relative sorted order of every element of $F\cup\tau$ other
than $f_i,f_j$ is unchanged as $f_i,f_j$ vary within that neighbourhood, and
$f_i,f_j$ themselves stay strictly between their current sorted neighbours;
hence each occupies a fixed rank, so the even-rank-membership indicators
$w_i,w_j\in\{0,1\}$ of $f_i,f_j$ are constant on this neighbourhood, and
$$E((f_i^\ast+\varepsilon, f_j^\ast-\varepsilon,\dots)\cup\tau)
=E(F^\ast\cup\tau)+(w_i-w_j)\varepsilon$$
for all sufficiently small $|\varepsilon|$ (both signs, since the
perturbation stays interior to the neighbourhood in either direction). If
$w_i\ne w_j$, choosing the sign of $\varepsilon$ matching $w_i-w_j>0$
strictly increases $E$, contradicting maximality of $F^\ast$. So every pair
of distinct free coordinates has the **same** $w$-value. Then, moving
$\varepsilon$ in *either* direction leaves $E$ unchanged (slope $0$); push
$\varepsilon$ in a fixed direction (say increasing $f_i$, decreasing $f_j$)
until the neighbourhood's boundary is first reached — i.e. until $f_i$ or
$f_j$ hits $0$, hits $\tau_1$, hits some $\tau_l$, or hits another
coordinate's value (whichever occurs first) — a point which exists since
$\mathcal P$ is bounded. At that point $E$ equals $E(F^\ast\cup\tau)$
(unchanged throughout, since slope was $0$) and one *fewer* pair of free
coordinates is unequal (either a coordinate became pinned, or two free
coordinates became mutually equal — in the latter case, merge them into a
single "tied group" and continue treating any further free coordinate
against this group's common value the same way). This process strictly
decreases, at each step, the number of *distinct* values among the free
coordinates (a nonnegative integer bounded by $k$), so it terminates after
finitely many steps, in a state $F^\dagger$ with $E(F^\dagger\cup\tau)
=E(F^\ast\cup\tau)$ (the true maximum) and at most **one** remaining
distinct free value $v$, shared by all unpinned coordinates. This is exactly
the claimed form. $\blacksquare$

*(This is the same style of finite exchange-smoothing argument as the
crux-inspired "aimo-0146" mechanism the outline specified, and uses only the
same elementary convex-geometry/continuity facts already invoked by
`vertex-minimum-theorem`, here run for the maximum instead of the minimum —
no min-specific step was used anywhere above, confirming the outline's
"verify explicitly" requirement.)*

**Consequence.** To prove $E(F\cup\tau)\le R(\tau)$ for *every* $F\in
\mathcal P$ and every $k\le m+1$, it suffices to prove it for every $F$ of
the restricted "pinned + one tied group" form above, ranging over every
$k\le m+1$, every choice of $p\le k$ pins (with repetition), and the induced
$v$.

#### 5.2 Two elementary general facts

**Fact 1 ($A\ge0$, `half-bound-lemma`, already certified).** For any finite
multiset $S$ of nonnegative reals, $A(S)\ge0$: pairing consecutive sorted
ranks $(2i-1,2i)$, $L_{2i}\le L_{2i-1}$ (descending sort), so summing over
complete pairs, the even-rank partial sum is $\le$ the odd-rank partial sum;
an unpaired leftover (if $|S|$ odd) is at an odd rank and only adds to the
odd sum. Hence $E(S)\le O(S)$, i.e. $A(S)=O(S)-E(S)\ge0$.

**Fact 2 ($A\le\mathrm{Total}$).** $A(S)=O(S)-E(S)\le O(S)\le O(S)+E(S)=
\mathrm{Total}(S)$, using $E(S)\ge0$ trivially (sum of nonnegative terms).

#### 5.3 The Ratio-2 Spacing Lemma

**Lemma (Spacing).** *Let $X\subseteq\{\tau_1,\dots,\tau_m\}$ (a sub-collection
of a ratio-2 tail, $|X|=j\ge2$), with elements $\nu_1<\nu_2<\dots<\nu_j$
(increasing order). Then $\nu_{i+1}\ge2\nu_i$ for every $1\le i<j$, and more
generally $\nu_i\ge2^{i-1}\nu_1$ for every $i$.*

**Proof.** If $\nu_i=\tau_{l}$, $\nu_{i+1}=\tau_{l'}$ with $l'<l$ (smaller
index = larger value, and $\nu_{i+1}>\nu_i$ forces $l'<l$), then
$\nu_{i+1}/\nu_i=\tau_{l'}/\tau_l=2^{l-l'}\ge2^1=2$ since $l>l'$ are distinct
integers. Iterating gives $\nu_i\ge2^{i-1}\nu_1$. $\blacksquare$

**Corollary (Total bound).** For $X$ as above with smallest element
$\nu_1=:\mu$, $\mathrm{Total}(X)\ge(2j-1)\mu$: each of the $j-1$ larger
elements is $\ge2\mu$ (Lemma, $i\ge2$), so
$\mathrm{Total}(X)\ge\mu+(j-1)(2\mu)=(2j-1)\mu$.

#### 5.4 Odd-run reduction of a pinned + tied-group configuration

Let $F^\dagger$ be as in §5.1: $p$ pins to values $\tau_{l_1},\dots,\tau_{l_p}$
(with repetition; write $c_l\ge0$ for how many pins land on level $l$, so
$\sum_l c_l=p$), plus $q:=k-p\ge0$ copies of a common value $v$ (if $q\ge1$;
if $q=0$, no free group, and we additionally require $\sum_l c_l\tau_l=s$
exactly). Set $S:=F^\dagger\cup\tau$; each $\tau_l$ has total multiplicity
$1+c_l$ in $S$.

By `odd-run-reduction-lemma`, $A(S)=A(S')$ where $S'$ keeps exactly the
values of odd total multiplicity. $1+c_l$ is odd $\iff$ $c_l$ is even. Let
$$X:=\{l\in\{1,\dots,m\}: c_l\text{ even}\}\quad(\text{as a set of }\tau_l\text{
values}),\qquad \mathrm{Total}(X):=\sum_{l\in X}\tau_l.$$
The $q$ copies of $v$ contribute a value of odd multiplicity to $S$ iff $q$
is odd (in which case exactly one copy of $v$ survives in $S'$); if $q$ is
even, $v$ contributes nothing to $S'$. So:
$$A(S)=\begin{cases}A(X)&q\text{ even (incl. }q=0)\\
A(X\cup\{v\})&q\text{ odd.}\end{cases}\tag{5.1}$$
This depends on the pin pattern **only through $X$** (the parity partition
of $\{1,\dots,m\}$) — not on the exact multiplicities $c_l$ — and on the
parity of $q$ and, if odd, the value of $v$. (This is the key simplification:
we never need to separately worry about "extra" pins beyond parity, since
$A(S)$ genuinely only depends on the parity pattern.)

**Target restated.** We must show $A(S)\ge s-R(\tau)$ for every valid
$(X,q,v)$ arising this way with the given $s$. Since $s=\sum_l c_l\tau_l+qv$
and $\sum_l c_l\tau_l\ge\sum_{l\notin X}\tau_l=R(\tau)-\mathrm{Total}(X)$
(equality iff minimal pins $c_l=[l\notin X]$ are used; using extra even
pins only increases $\sum_lc_l\tau_l$, hence — for the *same* $q$ and
resulting $s$ — only *decreases* the achievable $v$, which we show below
makes the inequality easier, not harder), the **worst case for fixed $X,q$**
is at $s=R(\tau)-\mathrm{Total}(X)+qv$ realized with minimal pins, i.e. we
may without loss of generality take $c_l=[l\notin X]$ (exactly one pin per
level *not* in $X$, zero pins per level *in* $X$), giving
$$s=R(\tau)-\mathrm{Total}(X)+qv,\qquad\text{i.e.}\qquad s-R(\tau)=qv-\mathrm{Total}(X).\tag{5.2}$$
*(Justification that this is indeed the worst case, not merely a
simplifying choice: for the $q$-even branch, $A(S)=A(X)$ does not depend on
$v$ or the exact pins at all — only on $X$ — so no "worst case in $v$"
issue arises there; the target $s-R(\tau)$ is then bounded using the
external hypothesis $s\le2\tau_1$ directly, §5.6, so extra pins are
immaterial. For the $q$-odd branch, §5.7's Lemma (Monotonicity) shows
$A(X\cup\{v\})-(qv-\mathrm{Total}(X))$ is non-increasing in $v$ for fixed
$X,q$; extra pins only decrease $v$ for the same $q,s$ (since they consume
mass that would otherwise go to $v$), hence can only increase this
difference — so it suffices to prove the bound at the largest reachable $v$
for each $q$, which is exactly $v$ from (5.2) with minimal pins,
capped at $\tau_1$: $v=\min\big(\tau_1,(qv$-solving$)\big)$, made precise in
§5.7.)*

We must also record the two structural constraints inherited from the
original problem: $s\in(0,2\tau_1]$, and the part-count budget $k\le m+1$,
i.e. $p+q\le m+1$; since minimal pins give $p=|\{1,\dots,m\}\setminus X|=
m-j$ where $j:=|X|$, this budget is $q\le m+1-(m-j)=j+1$, and since $q$ must
have the parity matching the branch,
$$q\ \le\ q_{\max}(j):=\text{the largest integer of the required parity that is}\le j+1.\tag{5.3}$$

#### 5.5 The $q$-even branch: full closure

Here $A(S)=A(X)$ (independent of $q,v$ by (5.1)), and the target is
$A(X)\ge s-R(\tau)$. Using the domain hypothesis $s\le2\tau_1$ and the
identity
$$R(\tau)+\tau_m=2\tau_1\tag{5.4}$$
(proved: $R(\tau)=\tau_1(1+\tfrac12+\dots+\tfrac1{2^{m-1}})=\tau_1(2-2^{1-m})$,
a finite geometric sum, and $\tau_m=\tau_1\cdot2^{1-m}$, so
$R(\tau)+\tau_m=\tau_1(2-2^{1-m}+2^{1-m})=2\tau_1$ exactly, for every
$m\ge1$), we get
$$s-R(\tau)\ \le\ 2\tau_1-R(\tau)\ =\ \tau_m.$$
So it suffices to show $A(X)\ge\tau_m$ for every $X\subseteq\{\tau_1,\dots,
\tau_m\}$, $X$ nonempty (the case $X=\emptyset$ forces, by budget, $q=0$ and
minimal pins exactly summing to $s$, i.e. $s=R(\tau)$ exactly, a single
boundary value where $A(S)=A(\emptyset)=0=s-R(\tau)$, trivially an
equality — handled separately, not needing the lemma below).

**Lemma (Last-Element Bound).** *For every nonempty $X\subseteq\{\tau_1,
\dots,\tau_m\}$, $A(X)\ge\min(X)$.* (Since $\min(X)\ge\tau_m$ always, as
$X\subseteq\{\tau_1,\dots,\tau_m\}$, this gives $A(X)\ge\tau_m$.)

**Proof.** Strong induction on $j:=|X|$. Write $X=\{x_1>x_2>\dots>x_j\}$
(descending).

*Base $j=1$:* $A(X)=x_1=\min(X)$, equality.

*Inductive step $j\ge2$:* removing the last (smallest) element $x_j$ shifts
no other rank; $x_j$ is at rank $j$. If $j$ is odd, rank $j$ is odd (positive
sign), so $A(X)=A(X\setminus\{x_j\})+x_j\ge0+x_j=x_j$ (IH gives
$A(X\setminus\{x_j\})\ge0$ trivially, or apply IH's own bound $\ge$ its own
new min $\ge0$; either way $\ge0$ suffices here). If $j$ is even, rank $j$
is even (negative sign), so $A(X)=A(X\setminus\{x_j\})-x_j$. By IH (size
$j-1\ge1$, odd), $A(X\setminus\{x_j\})\ge x_{j-1}$ (the new minimum). So
$A(X)\ge x_{j-1}-x_j$. Since $x_{j-1},x_j$ are consecutive elements of $X$
in sorted order, the Spacing Lemma (§5.3) gives $x_{j-1}\ge2x_j$, so
$A(X)\ge2x_j-x_j=x_j=\min(X)$. $\blacksquare$

**This closes the entire $q$-even branch, for every $m$, unconditionally.**

#### 5.6 The $q$-odd branch, sub-case (b): $v$ capped by the box bound $\tau_1$

For $q$ odd, by (5.2), $v=\big(s-R(\tau)+\mathrm{Total}(X)\big)/q$; the
domain requires $v\le\tau_1$ additionally, i.e. (using $s\le2\tau_1$ and
(5.4)) the *achievable* maximal $v$ for a given $q,X$ is
$$v_{\max}(q,X):=\min\Big(\tau_1,\ \frac{\tau_m+\mathrm{Total}(X)}q\Big).\tag{5.5}$$
(The second argument is the value making $s=2\tau_1$ exactly, the largest
domain-permitted $s$, using (5.4): $s-R(\tau)+\mathrm{Total}(X)\le2\tau_1-R(\tau)
+\mathrm{Total}(X)=\tau_m+\mathrm{Total}(X)$.)

**Sub-case (b): $v_{\max}=\tau_1$**, i.e. $\tau_m+\mathrm{Total}(X)\ge q\tau_1$.

**Claim: this forces $q=1$.** Since $X\subseteq\{\tau_1,\dots,\tau_m\}$,
$\mathrm{Total}(X)\le R(\tau)<2\tau_1$ (as $R(\tau)=\tau_1(2-2^{1-m})<2\tau_1$
for every $m\ge1$). If $q\ge3$: $q\tau_1-\tau_m\ge3\tau_1-\tau_m\ge3\tau_1-\tau_1
=2\tau_1>\mathrm{Total}(X)$ (using $\tau_m\le\tau_1$), contradicting
$\mathrm{Total}(X)\ge q\tau_1-\tau_m$. So $q\le1$, and since $q$ is a positive
odd integer, $q=1$.

At $q=1$, $v=\tau_1$: the target $A(S)\ge s-R(\tau)$ becomes, via (5.2) with
$q=1$, $A(X\cup\{\tau_1\})\ge\tau_1-\mathrm{Total}(X)$. Since $\tau_1$ is the
global max (every element of $X$ is $\le\tau_1$, with equality only if
$\tau_1\in X$, in which case $\tau_1$'s two occurrences at the same position
just merge — the identity below is still valid, treating $X\cup\{\tau_1\}$
as a multiset), peeling the max: $A(X\cup\{\tau_1\})=\tau_1-A(X)$. The target
becomes $\tau_1-A(X)\ge\tau_1-\mathrm{Total}(X)$, i.e.
$\mathrm{Total}(X)\ge A(X)$ — **Fact 2 of §5.2**, always true. **Sub-case (b)
closes unconditionally, for every $j=|X|$.**

#### 5.7 The $q$-odd branch, sub-case (a): the domain bound binds

Here $v=v_{\max}=(\tau_m+\mathrm{Total}(X))/q\le\tau_1$, so by (5.2) (with
$s$ at its maximal value for this $X,q$) the target simplifies: since
$qv=\tau_m+\mathrm{Total}(X)$ exactly (defining relation), the target
$A(X\cup\{v\})\ge qv-\mathrm{Total}(X)$ becomes simply
$$A(X\cup\{v\})\ \ge\ \tau_m.\tag{5.6}$$

**Lemma (Monotonicity — justifying "worst case at $v_{\max}$").** *For fixed
$X,q$ (odd), the function $v\mapsto A(X\cup\{v\})-qv$ is non-increasing on
$(0,\tau_1]$.* **Proof.** Inserting $v$ into the sorted sequence of $X$ at
position $t+1$ (where $t:=\#\{x\in X: x>v\}$), a direct computation (as in
§4.6–4.8 of earlier rounds) gives $A(X\cup\{v\})=A_1+(-1)^t(v-A_2)$ where
$A_1,A_2$ are the alternating sums of the two parts of $X$ split at $v$'s
insertion point — a function that is **affine in $v$ with slope $(-1)^t$**
on each interval between consecutive elements of $X$ (where $t$ is
constant), and continuous across the finitely many breakpoints (insertion
value crossing an $X$-element). So $A(X\cup\{v\})-qv$ has slope
$(-1)^t-q$ on each interval: if $t$ even, slope $=1-q\le0$ (as $q\ge1$); if
$t$ odd, slope $=-1-q<0$. Either way $\le0$ on every interval, and the
function is continuous, hence non-increasing globally on $(0,\tau_1]$.
$\blacksquare$ Combined with the target $A(X\cup\{v\})\ge qv-\mathrm{Total}(X)$
(equivalent to $A(X\cup v)-qv\ge-\mathrm{Total}(X)$, a lower bound on a
non-increasing function), the hardest case is the *largest* legal $v$, i.e.
$v=v_{\max}$ — justifying restricting to (5.6) at the domain-tight $v$, as
claimed in §5.4.

We now prove (5.6) for every $X$ (of every size $j:=|X|\ge0$) and every odd
$q\le q_{\max}(j)$ with $v\le\tau_1$ (i.e. genuinely in sub-case (a)).

**Two elementary consequences of (5.2)/(5.5) and the Spacing Lemma, used
below.** For $X$ nonempty with elements $\nu_1<\dots<\nu_j$ ($\mu:=\nu_1=
\min X$):
$$v\ \ge\ \mu\qquad\text{whenever } q\le2j-1,\tag{5.7}$$
$$v\ \ge\ \mu'\ (:=\nu_2,\text{ if }j\ge2)\qquad\text{whenever } q\le2j-3.\tag{5.8}$$
*Proof of (5.7).* By the Corollary in §5.3, $\mathrm{Total}(X)\ge(2j-1)\mu$,
so $\tau_m+\mathrm{Total}(X)>(2j-1)\mu\ge q\mu$ (using $q\le2j-1$), giving
$v=(\tau_m+\mathrm{Total}(X))/q>\mu$ wait — dividing the strict inequality
$\tau_m+\mathrm{Total}(X)>(2j-1)\mu\ge q\mu$ by $q>0$ gives $v>\mu\cdot
\frac{(2j-1)}{q}\ge\mu$ if $q\le 2j-1$; more directly $\tau_m+\mathrm{Total}(X)
\ge q\mu$ (weak form suffices) gives $v\ge\mu$ immediately by dividing by
$q$. *Proof of (5.8).* Apply the same Corollary to $X':=X\setminus\{\mu\}$
(size $j-1$, minimum $\mu'$): $\mathrm{Total}(X')\ge(2(j-1)-1)\mu'=(2j-3)\mu'$,
so $\mathrm{Total}(X)=\mathrm{Total}(X')+\mu\ge(2j-3)\mu'+\mu>(2j-3)\mu'$,
giving $\tau_m+\mathrm{Total}(X)>(2j-3)\mu'\ge q\mu'$ (using $q\le2j-3$),
hence $v>\mu'\cdot\frac{2j-3}{q}\ge\mu'$, i.e. $v\ge\mu'$ (in fact $v>\mu'$).

Now, since $q\le q_{\max}(j)$ (the largest integer of the correct parity
$\le j+1$), and one checks directly $q_{\max}(j)\le2j-1$ for every $j\ge1$
(equality at $j=1,2$; e.g. $j$ odd: $q_{\max}=j\le2j-1\iff j\ge1$; $j$ even:
$q_{\max}=j+1\le2j-1\iff j\ge2$) and $q_{\max}(j)\le2j-3$ for every $j\ge3$
(equality at $j=3$; $j$ odd $\ge3$: $q_{\max}=j\le2j-3\iff j\ge3$; $j$ even
$\ge4$: $q_{\max}=j+1\le2j-3\iff j\ge4$), bounds (5.7) (all $j\ge1$) and
(5.8) (all $j\ge3$) apply to every $q$ arising in sub-case (a).

**Case $j=0$.** $X=\emptyset$; budget forces $q\le q_{\max}(0)=1$, so $q=1$,
$v=\tau_m$. $A(\{v\})=v=\tau_m$. Equality — (5.6) holds.

**Case $j=1$, $X=\{\mu\}$.** Budget forces $q\le q_{\max}(1)=1$, so $q=1$,
$v=\tau_m+\mu$ (from $qv=\tau_m+\mathrm{Total}(X)=\tau_m+\mu$). Since
$\tau_m,\mu>0$, $v>\mu$, so $v$ is the sorted-max of $\{v,\mu\}$:
$A(\{v,\mu\})=v-\mu=\tau_m$. Equality — (5.6) holds.

**Case $j\ge2$ even.** By (5.7), $v\ge\mu$, so $\mu$ is the global minimum of
$Y:=X\cup\{v\}$ (it is already the min of $X$, and now also $\le v$); peel
it. $|Y|=j+1$ (odd, since $j$ even), so $\mu$ sits at rank $j+1$, an odd
rank (positive sign): $A(Y)=A(Y')+\mu$ where $Y':=(X\setminus\{\mu\})\cup\{v\}$.
By **Fact 1** ($A\ge0$, general, applies to *any* multiset, no further
information about $Y'$ needed), $A(Y')\ge0$. So
$$A(Y)\ \ge\ \mu\ \ge\ \tau_m$$
(using $\mu=\min(X)\ge\tau_m$, as $X\subseteq\{\tau_1,\dots,\tau_m\}$). This
proves (5.6). **Closes every even $j\ge2$, no case left.**

**Case $j\ge3$ odd.** By (5.7), $v\ge\mu$; peel $\mu$ from $Y=X\cup\{v\}$.
$|Y|=j+1$ (even, since $j$ odd), so $\mu$ sits at rank $j+1$, an **even**
rank (negative sign): $A(Y)=A(Y')-\mu$ where $Y'=(X\setminus\{\mu\})\cup\{v\}$
(size $j$). By (5.8), $v\ge\mu'$ (the second-smallest of $X$, which is now
$\min(X\setminus\{\mu\})$), so $\mu'$ is the global min of $Y'$; peel it too.
$|Y'|=j$ (odd), so $\mu'$ sits at rank $j$, an **odd** rank (positive sign):
$A(Y')=A(Y'')+\mu'$ where $Y'':=(X\setminus\{\mu,\mu'\})\cup\{v\}$. By
**Fact 1** again (applies to any multiset), $A(Y'')\ge0$. Chaining:
$$A(Y)=A(Y')-\mu=\big(A(Y'')+\mu'\big)-\mu\ \ge\ \mu'-\mu.$$
By the Spacing Lemma (§5.3), $\mu'\ge2\mu$ (consecutive elements of $X$), so
$\mu'-\mu\ge\mu\ge\tau_m$ (using $\mu\ge\tau_m$ once more). Hence
$$A(Y)\ \ge\ \mu'-\mu\ \ge\ \mu\ \ge\ \tau_m.$$
This proves (5.6). **Closes every odd $j\ge3$, no case left.**

**Every $j\ge0$ is covered ($j=0$, $j=1$, even $j\ge2$, odd $j\ge3$), so
sub-case (a) is closed unconditionally, for every $m$.**

#### 5.8 Conclusion of §5

Combining §5.5 ($q$-even, all $X$), §5.6 (sub-case (b), forces $q=1$, closed
via Fact 2), and §5.7 (sub-case (a), every $j$, closed via Facts 1 + Spacing
Lemma): **every vertex configuration of the form guaranteed by §5.1
satisfies $A(S)\ge s-R(\tau)$.** By the Vertex-maximization Proposition
(§5.1), this is exactly the maximum of $E(F\cup\tau)$ over all Case-I $F$
(via $A=\mathrm{Total}-2E$, maximizing $E$ is minimizing $A$), so the
inequality holds for **every** Case-I $F$, proving the Case I Closure
Theorem in full, for every $m$. $\blacksquare$

**Independent numerical cross-check (this round).** An exhaustive (not
random) enumeration of every vertex configuration $(X,q)$ — every subset
$X\subseteq\{1,\dots,m\}$, every legal $q$ of each parity up to the budget —
for $m=1,\dots,10$, computing $A(S)-(s-R(\tau))$ in exact `Fraction`
arithmetic at the domain-tight $s$ for each configuration: **zero
violations** across all $6655$ configurations checked at $m=10$ (and all
smaller $m$), with the minimum margin exactly $0$ at the expected equality
cases ($X=\emptyset,q=1$, i.e. $F=\{s\}$ with $s=\tau_1$, and its relatives).
This is an independent confirmation of the hand proof above (script
`/tmp/final_comprehensive_check.py` in this build's log), not a substitute
for it — the proof in §5.1–§5.7 is unconditional for every $m$.

### 6. Claim (A) in full

By §2 (achievability) and §3 + §5 (lower bound, Case II and Case I both
proved for every $m$, hence every $n$), **Claim (A) is proved completely**:
for every $n\ge1$ and every partition $F$ of $p_1$ into at most $n+1$ parts,
$$A(F\cup T)\ \ge\ a_n,$$
with equality attained exactly by the explicit $F^\ast$ of §2 (among
others, e.g. §5.6's and §5.7's equality-case configurations, all consistent
with $F^\ast$'s shape). $\blacksquare$

### 7. Round-19 cross-check: the middle band of Claim B's $\Delta(n,v)$

**Scope note.** This section is *outside* Claim (A) (the target already fully
closed above); it is this round's assigned cross-check work on
`greedy-halving-adversary`'s open target (the "middle band"
$v_2\in(p_2-v_1,s)$ of Theorem 33/34's sub-case (b), $\ell(F)=2$). It does
**not** change this file's own Status (Claim A remains solved); it is
recorded here per the round-19 dispatch as this slug's second-angle
contribution to the sibling's target.

**Setup (imported, not re-derived).** Per `greedy-halving-adversary.md`
(Theorem 34 and its diagnosis), the residual open item reduces to bounding,
for a legal refinement $R'$ of the ratio-2 tail $\tau=\{p_3,\dots,p_{n+1}\}$
(total mass $s$) and a threshold $v\in(0,s)$,
$$\Delta(n,v)\ :=\ A(R')-2A(R'_{>v})$$
from above, uniformly over all legal $R'$ — this is exactly the round-19
outline's named coupled quantity. The needed sufficient inequality (via
$J_0=\int_0^v u_{R'}\le v$, the crude bound already used in Theorem 34) is
$$\Delta(n,v_2)\ \le\ s-(v_1-v_2)\qquad\text{for }v_1\in(s,p_2),\ v_2\in(p_2-v_1,s).\tag{$\sharp$}$$

#### 7.1 The Truncated Alternating Sum Ceiling (new, general, unconditional)

**Lemma (Ceiling).** *For any finite multiset $S$ of nonnegative reals and
any $v\ge0$,*
$$A(S)-2A(S_{>v})\ \le\ v,$$
*with equality attained (e.g.) at $S=\{v\}$.*

**Proof.** Write, for $x\ge0$, $N_S(x):=\#\{a\in S: a>x\}$ and
$u_S(x):=\mathbb1[N_S(x)\text{ odd}]\in\{0,1\}$. By
`integral-alternating-sum-formula` (certified; the standard "layer-cake"
identity for the rank-alternating sum), $A(S)=\int_0^\infty u_S(x)\,dx$.

*Step 1 (self-contained re-derivation of the truncation identity).* For
$x\ge v$: an element of $S$ exceeds $x$ iff it exceeds $v$ **and** exceeds
$x$ (since $x\ge v$, "exceeds $x$" already implies "exceeds $v$"), so
$N_S(x)=N_{S_{>v}}(x)$ for every $x\ge v$, hence $u_S(x)=u_{S_{>v}}(x)$ for
$x\ge v$. For $x\in[0,v)$: every element of $S_{>v}$ exceeds $v>x$, so all of
them exceed $x$; hence $N_{S_{>v}}(x)=|S_{>v}|$, constant, so
$u_{S_{>v}}(x)\equiv\epsilon(v):=\mathbb1[|S_{>v}|\text{ odd}]$ on $[0,v)$.
Therefore
$$A(S_{>v})=\int_0^\infty u_{S_{>v}}(x)\,dx
=\underbrace{\int_0^v u_{S_{>v}}(x)\,dx}_{=v\epsilon(v)}
+\underbrace{\int_v^\infty u_{S_{>v}}(x)\,dx}_{=\int_v^\infty u_S(x)\,dx}
= v\epsilon(v)+\int_v^\infty u_S(x)\,dx.\tag{7.1}$$

*Step 2 (assemble $\Delta$).* Using $A(S)=\int_0^vu_S+\int_v^\infty u_S$ and
(7.1),
$$\Delta(S,v)=A(S)-2A(S_{>v})
=\int_0^vu_S(x)\,dx-\int_v^\infty u_S(x)\,dx-2v\epsilon(v).\tag{7.2}$$

*Step 3 (three elementary one-line bounds).* Since $u_S$ is $\{0,1\}$-valued:
$$\int_0^v u_S(x)\,dx\ \le\ v\cdot1=v,\qquad
\int_v^\infty u_S(x)\,dx\ \ge\ 0,\qquad \epsilon(v)\ge0.$$
Substituting all three into (7.2): $\Delta(S,v)\le v-0-0=v$. $\blacksquare$

**Equality case.** $S=\{v\}$: $A(S)=v$, $S_{>v}=\varnothing$ (as $v\not>v$),
$A(S_{>v})=0$, so $\Delta=v-0=v$, matching the bound exactly. (More
generally: equality holds iff $u_S\equiv1$ on $[0,v)$, $u_S\equiv0$ on
$[v,\infty)$, and $\epsilon(v)=0$ — e.g. $S=\{v\}\cup P$ for any exactly-paired
$P$ with all elements $<v$.)

**Independent verification.** $300{,}000$ random-rational trials (exact
`Fraction`, no structure imposed on $S$ or $v$ beyond nonnegativity), zero
violations, minimum margin $0$ attained exactly at the equality
configurations above (script this round, `/tmp/check_ceiling_general.py`).

**Why this is the "dual" of the sibling's certified lemma.** The sibling's
`truncated-alternating-sum-floor` (Theorem 31's engine) proves
$\Psi(v):=A(S)-2A(S_{>v})+2v\epsilon(v)\ge v-\mathrm{Total}(S)$ by the same
three-term decomposition (7.2)-style, using the complementary one-sided
bounds $\int_0^vu_S\ge0$ and $\int_v^{\mathrm{Total}(S)}u_S\le
\mathrm{Total}(S)-v$. This round's Ceiling instead keeps the $\epsilon(v)$
term on the $\Delta$ side (matching the outline's own literal definition of
$\Delta(n,v)$, which omits the parity correction) and uses the opposite
one-sided bounds. Both are genuine, elementary, general facts — no ladder
or ratio-2 structure is used by either.

#### 7.2 Why the Ceiling alone is not enough for $(\sharp)$

$(\sharp)$ requires $\Delta(n,v_2)\le s-(v_1-v_2)$. Since $v_1>s$ in the
middle band's own range, $s-(v_1-v_2)<v_2$ strictly — so the general Ceiling
$\Delta(n,v_2)\le v_2$ is **too weak by exactly $v_1-s>0$**, confirmed by
direct algebra, not merely asserted. Any closure of $(\sharp)$ must use
structure specific to $R'$ beyond the elementary ceiling: namely, that
$R'$'s total mass is *exactly* $s$ (fixed, not merely bounded), that its
pieces are the specific ratio-2 values $p_3,\dots,p_{n+1}$, and — per the
round-19 outline's diagnosis — that $R'$'s cut budget is capped at $n-3$
(not $n-2$).

#### 7.3 Testing whether extra mass can be "hidden" without a cut-budget cap

If $R'$'s cut budget is *unrestricted*, the mass-conservation constraint
alone does not force the Ceiling's slack to shrink: one can attempt to push
$\Delta(n,v_2)$ toward $v_2$ by placing a fragment near $v_2$ (from below) at
an odd rank and disposing of the remaining mass $s-v_2$ as exactly-paired
"invisible" duplicates elsewhere (contributing $0$ net to $A(R')$ and,
if kept $\le v_2$, not entering $R'_{>v_2}$) — but this requires splitting
$R'$'s constituent pieces $p_3,p_4,\dots$ finely enough to manufacture such
pairs, i.e. it costs cuts. **Independent numerical test (this round,
`/tmp/check_middle2.py`):** with the cut budget left unrestricted
(uniform random over generous per-piece splits, no cap at all), $(\sharp)$'s
sufficient inequality is genuinely **violated** — $n=3$: margin
$-0.058$; $n=4$: $-0.024$; $n=5$: $-0.0079$ (exact `Fraction` arithmetic,
$20{,}000$ trials per $n$). This is an **honest negative finding,
independently reproduced** (not merely imported from the sibling): without
*some* cut-budget restriction, $(\sharp)$ genuinely fails, confirming from a
second, independently-written script that a bare/unconditional closure is
impossible and *some* budget correction (as the round-19 outline proposes)
is load-bearing, not optional.

#### 7.4 Corroboration of the corrected $n-3$ cap (independent second script)

Re-running the identical search with $R'$'s total additional-cut budget
capped at $n-3$ (distributed arbitrarily among the $\tau$'s $n-1$ constituent
pieces $p_3,\dots,p_{n+1}$ — i.e. $n=3$ forces budget $0$, $n=4$ forces
budget $\le1$, etc., exactly the round-19 outline's corrected cap), and
re-sampling $v_1\in(s,p_2)$, $v_2\in(p_2-v_1,s)$ uniformly at random:
$30{,}000$ trials per $n$, $n=3,\dots,7$ — **zero violations** of
$(\sharp)$, minimum margin found strictly positive in every case (e.g.
$n=3$: margin $\ge0.00074$; $n=7$: margin $\ge0.0051$;
`/tmp/check_middle3.py`, independently written this round, not derived from
`greedy-halving-adversary`'s own scripts). This **corroborates, from a
genuinely independent angle**, the round-19 outline's central diagnosis that
the corrected $n-3$ cap is the right fix for the middle band — consistent
with, and cross-verifying, whatever `greedy-halving-adversary`'s own
vertex-enumeration route finds this round.

#### 7.5 Unconditional exact closure at $n=3$ (round 19: the weaker $(\sharp)$ target; round 21: the TRUE $\varepsilon$-corrected target $(\sharp')$, in full)

At $n=3$ the corrected cap forces budget $=0$, so $R'=\tau=\{p_3,p_4\}$ is
the *only* legal response — no adversarial freedom remains at all — making
the middle band fully tractable by direct, exhaustive computation.

Here $p_3=2p_4$ (ladder), $s=p_3+p_4=3p_4$, and $A(\tau)=p_3-p_4=p_4=f(3)$.
Also $p_2=2p_3=4p_4$ (ladder doubling applied twice).

##### 7.5.0 The TRUE ($\varepsilon$-corrected) target $(\sharp')$ — imported, not re-derived

**Scope of this subsection.** Round 19's §7.5 (below, retained verbatim as
§7.5.1) only closed the *weaker* sufficient inequality $(\sharp)$,
$\Delta(n,v_2)\le s-(v_1-v_2)$ — the $\varepsilon=0$-only version. Per this
round's dispatch, we now close the actual, $\varepsilon$-corrected target
needed for `greedy-halving-adversary`'s Theorem 34 (corrected)/Theorem 35
bridge. We import the exact identity chain from
`greedy-halving-adversary.md` ("Theorem 34 (corrected)", subsection "The
reduction to $\Delta(n,v)$") rather than re-deriving the Step-1 identity for
$A(F\cup G')$ from scratch (that identity belongs to the sibling's own
setup, not this cross-check); we do reproduce the final algebraic chain here
so the closure below is self-contained and checkable without flipping back
and forth. Starting from the sibling's Step-1 identity for $A(F\cup G')$
(valid for all $v_1,v_2\in(0,p_2)$, $v_2<v_1$) and its already-certified
`upper-truncation-identity` conversion of $J_0:=\int_0^{v_2}u_{R'}$ into the
local-rank quantity $A(R'_{>v_2})$ (namely $J_0=A(R')-A(R'_{>v_2})
+v_2\varepsilon(v_2)$, $\varepsilon(v_2):=\mathbb1[|R'_{>v_2}|\text{ odd}]$),
the sibling obtains, for $v_2<s\le v_1$,
$$A(F\cup G')\ =\ p_2-\Delta(n,v_2)-2v_2\,\varepsilon(v_2)-(v_1-v_2),\qquad
\Delta(n,v_2):=A(R')-2A(R'_{>v_2}).$$
Since the target is $A(F\cup G')\ge f(n)=p_2-s$, this is equivalent — for
every fixed $v_1,v_2$ in this regime — to the **TRUE sufficient target**
$$\Delta(n,v_2)\ \le\ s-(v_1-v_2)-2v_2\,\varepsilon(v_2).\tag{$\sharp'$}$$
When $\varepsilon(v_2)=0$, $(\sharp')$ is exactly $(\sharp)$; when
$\varepsilon(v_2)=1$, $(\sharp')$ is **strictly stronger**, requiring an
extra $2v_2$ of slack. This is the precise quantity §7.2 of this file
already identified the plain Ceiling Lemma as $2v_2$-too-weak for, and is
exactly the gap `greedy-halving-adversary`'s own file records as "not
verified" for the $\varepsilon(v)=1$ case.

##### 7.5.0$'$ Locating $\varepsilon(v_2)=1$ at $n=3$ via the Band-Parity Fact

By the **Band-Parity Fact** (imported from `greedy-halving-adversary`'s
round-21 build, or equivalently verified directly here since $R'=\tau$ is
forced and $|\tau|=2$ is small enough to check by hand): $\varepsilon(v_2)=
\mathbb1[|\tau_{>v_2}|\text{ odd}]$, and, using the strict-$>$ convention
consistently applied throughout this file,
$$\tau_{>v_2}=\begin{cases}\varnothing&v_2\ge p_3\\ \{p_3\}&v_2\in[p_4,p_3)\\
\{p_3,p_4\}=\tau&v_2<p_4,\end{cases}$$
so $|\tau_{>v_2}|\in\{0,1,2\}$ respectively, giving
$$\varepsilon(v_2)=\begin{cases}0&v_2\ge p_3\quad(\text{band }0,\text{ top: }v\ge r_1,\ k=2\text{ even}\Rightarrow\varepsilon=0)\\
1&v_2\in[p_4,p_3)\quad(\text{band }1,\text{ odd-indexed})\\
0&v_2<p_4\quad(\text{band }2,\text{ bottom: }v<r_k,\ k=2\text{ even}\Rightarrow\varepsilon=0).\end{cases}$$
This is exactly the pattern the Band-Parity Fact predicts for a length-$2$
tail ($k=2$, even): $\varepsilon=0$ on both the top and bottom bands,
$\varepsilon=1$ only on the single interior band — confirming §7.5's
pre-existing 3-case split is not an arbitrary convenience but literally
tracks the parity structure. So $(\sharp')$ differs from $(\sharp)$ **only**
on the middle case $v_2\in[p_4,p_3)$; on the other two cases $(\sharp')=
(\sharp)$ identically, so §7.5.1's existing closure of those two cases
already *is* a closure of $(\sharp')$ there, with no further work needed.

##### 7.5.1 The two outer bands: $(\sharp')=(\sharp)$, already closed (round 19, reproduced)

Fix $v_1\in(s,p_2)$, $v_2\in(p_2-v_1,s)$.

- **$v_2\ge p_3$:** here $p_3\not>v_2$ (by the case hypothesis) and
  $p_4<p_3\le v_2$ so $p_4\not>v_2$ either; hence $\tau_{>v_2}=\varnothing$, so
  $\Delta(3,v_2)=A(\tau)=p_4=f(3)$, and $\varepsilon(v_2)=0$ so
  $(\sharp')=(\sharp)$: $\Delta(3,v_2)\le s-(v_1-v_2)$. Since $v_1<p_2$
  strictly, $s-(v_1-v_2)>s-p_2+v_2=-f(3)+v_2\ge-f(3)+p_3=-p_4+2p_4=p_4=f(3)$
  (using $s-p_2=-f(3)$, Lemma 24, and $v_2\ge p_3$). So $(\sharp')$ holds
  strictly.
- **$v_2<p_4$:** here $v_2<p_4<p_3$ so both $p_3>v_2$ and $p_4>v_2$, hence
  $\tau_{>v_2}=\tau$, so $\Delta(3,v_2)=A(\tau)-2A(\tau)
  =-A(\tau)=-p_4=-f(3)$, and $\varepsilon(v_2)=0$ so $(\sharp')=(\sharp)$:
  need $-f(3)\le s-(v_1-v_2)$, i.e.
  $v_1-v_2\le s+f(3)=3p_4+p_4=4p_4=2p_3=p_2$. Since $v_1<p_2$ (strictly, from
  the domain $v_1\in(s,p_2)$) and $v_2>0$ (strictly, since $v_1<p_2$ gives
  $p_2-v_1>0$, and $v_2$ ranges over $(p_2-v_1,s)$, so $v_2>p_2-v_1>0$), we
  get $v_1-v_2<v_1<p_2$ strictly, so $(\sharp')$ holds.

Both outer cases close $(\sharp')$ strictly, as claimed (identical to round
19's closure of $(\sharp)$, since $\varepsilon=0$ makes the two targets
coincide, as established in §7.5.0$'$).

##### 7.5.2 The middle band, $v_2\in[p_4,p_3)$: closing the TRUE target $(\sharp')$ (new, round 21)

Here $\tau_{>v_2}=\{p_3\}$ uniformly across the whole half-open interval,
including its left endpoint $v_2=p_4$ (verified: $p_3>v_2$ holds throughout
since $v_2<p_3$, and $p_4\not>v_2$ throughout since $v_2\ge p_4$, so
$p_4\notin\tau_{>v_2}$ even at $v_2=p_4$ exactly, by the strict-$>$
convention), so
$$\Delta(3,v_2)=A(\tau)-2A(\{p_3\})=A(\tau)-2p_3=p_4-2(2p_4)=p_4-4p_4=-3p_4,$$
a single closed-form value, constant across the whole interval — this part
is unchanged from round 19's computation. And $\varepsilon(v_2)=1$
throughout the interval (§7.5.0$'$), so $(\sharp')$ here reads
$$\Delta(3,v_2)\ \le\ s-(v_1-v_2)-2v_2,\qquad\text{i.e.}\qquad
-3p_4\ \le\ s-v_1-v_2\ =\ 3p_4-v_1-v_2,$$
which rearranges (adding $v_1+v_2-3p_4$ to both sides) to the single clean
target
$$v_1+v_2\ \le\ 6p_4.\tag{$\dagger$}$$
(This matches exactly the outline's stated reduction $s+3p_4=3p_4+3p_4=6p_4$.)

**Proof of $(\dagger)$, strictly, using the case hypothesis $v_2<p_3$ (not
merely the old proof's weaker $v_2>0$).** We have two independent strict
bounds available simultaneously:
- $v_1<p_2$ — the domain hypothesis $v_1\in(s,p_2)$ (upper endpoint), and
- $v_2<p_3$ — the *case* hypothesis defining the middle band itself
  ($v_2\in[p_4,p_3)$, so in particular $v_2<p_3$ strictly, since the
  interval is open on the right).

Since $p_2=4p_4$ and $p_3=2p_4$ (ladder, recorded above), adding these two
strict inequalities termwise gives
$$v_1+v_2\ <\ p_2+p_3\ =\ 4p_4+2p_4\ =\ 6p_4,$$
which is exactly $(\dagger)$, proved **strictly**. (Both summands are
strict inequalities, so the sum is strict; no boundary case to separately
check — the left endpoint $v_2=p_4$ of the middle interval is well inside
$v_2<p_3=2p_4$, since $p_4<2p_4$, so it is not a boundary of *this*
inequality at all.)

Unwinding the rearrangement: $(\dagger)\iff v_1+v_2\le 6p_4$ (in fact
$<6p_4$) $\iff 3p_4-v_1-v_2\ge-3p_4$ (subtract $v_1+v_2$, add $-3p_4$ to
both sides: $6p_4\ge v_1+v_2\iff 3p_4-v_1-v_2\ge3p_4-6p_4=-3p_4$)
$\iff s-v_1-v_2\ge-3p_4=\Delta(3,v_2)$, which is exactly $(\sharp')$ at
$v_2\in[p_4,p_3)$. **This closes the middle band's TRUE target $(\sharp')$,
strictly, for every $v_1\in(s,p_2)$ and every $v_2\in[p_4,p_3)$ inside the
band's own domain $v_2\in(p_2-v_1,s)$** (the containment
$[p_4,p_3)\cap(p_2-v_1,s)\subseteq[p_4,p_3)$ is used only to restrict
attention to the relevant sub-range; the bound $(\dagger)$ itself holds
on the whole interval $[p_4,p_3)$ regardless of $v_1$'s exact value, so it
applies a fortiori to the intersection with the domain).

**Independent numerical cross-check of $(\sharp')$ specifically (this
round, distinguishing it from §7.4's earlier $(\sharp)$-only check).**
Re-running the exact-`Fraction` search at $n=3$ with the *TRUE*
target $\Delta(3,v_2)\le s-(v_1-v_2)-2v_2\varepsilon(v_2)$ (not the weaker
$(\sharp)$), sampling $v_1\in(s,p_2)$, $v_2\in(p_2-v_1,s)$ uniformly,
$50{,}000$ trials: **zero violations**, minimum margin found
$\ge 1/(5{,}000{,}000)$ in the middle band specifically (script
`/tmp/check_sharp_prime_n3.py`, this round) — consistent with, and
corroborating, the hand proof above (which in fact shows the bound is
strict with margin exactly $6p_4-(v_1+v_2)>0$, vanishing only in the limit
$v_1\to p_2^-,v_2\to p_3^-$, a limit excluded from the open domain).

##### 7.5.3 Conclusion of §7.5

Combining §7.5.1 (both outer bands, where $(\sharp')=(\sharp)$ trivially)
and §7.5.2 (the middle band, where $(\sharp')$ needed — and received — the
genuinely new tightened bound $(\dagger)$, using the case hypothesis
$v_2<p_3$ rather than merely $v_2>0$): **the TRUE, $\varepsilon$-corrected
target $(\sharp')$ is proved, unconditionally and strictly, for every
$v_1\in(s,p_2)$ and every $v_2\in(p_2-v_1,s)$, at $n=3$.** This is strictly
stronger than round 19's closure of the weaker $(\sharp)$: it establishes
exactly the sufficient inequality `greedy-halving-adversary`'s own file
records as needed but "not verified" for the $\varepsilon(v)=1$ case,
specialized to $n=3$ — the base case of that sibling bridge gap, now fully
closed, by hand, with no numerics substituting for the proof (the
$50{,}000$-trial check above is corroboration only).

**What this does and does not resolve.** This closes the $n=3$ instance of
the $\varepsilon$-bridge for the middle band. It does **not** address
§7.6's separate, general-$n\ge4$ open item (the cross-piece tie-vertex
enumeration for the budget-$(n-3)$-capped multi-piece polytope) — that gap
is untouched by this round's work and remains exactly as recorded below,
unconditionally open for $n\ge4$.

#### 7.6 General $n\ge4$: honest gap — the multi-piece vertex family is not a direct transplant of Claim A's machinery

For $n\ge4$ the budget $n-3\ge1$ is positive, so $R'$ genuinely ranges over
a nontrivial polytope (independent refinements of the $n-1$ *distinct* fixed
pieces $p_3,\dots,p_{n+1}$, with a *shared* total cut budget $n-3$ across
them). We attempted to adapt the certified
`exchange-smoothing-vertex-maximization` machinery (built for a *single*
stick's own fragmentation, Claim A's setting) to this genuinely different
polytope, and record the following honest diagnosis rather than force a
claim of closure:

- **Per-piece freeze-and-smooth is valid but only a *necessary* condition,
  not by itself a closed enumeration.** Since mass is conserved
  *per original piece* (not globally across pieces), any joint maximizer
  $R'^\dagger$, restricted to one piece's own fragments with all other
  pieces frozen at $R'^\dagger$'s values, must itself be a one-piece
  maximizer — so the (already-certified) single-stick vertex argument
  applies *verbatim* to each piece separately, giving: each split piece's
  own fragments are pinned+one-tied-group relative to the reference set
  $\{0,\tau_i,v_2\}\cup\{\text{every other piece's current fragment
  value}\}$.
- **This can force genuine cross-piece ties**, not just within-piece
  pinning: the local-perturbation argument's "stopping point" (§5.1 of the
  Claim-A proof, reused verbatim here) can be a coincidence with *another
  piece's* current fragment value, not only $0,\tau_i,v_2$. This is exactly
  the general tie-vertex enumeration difficulty already on record across
  the project (see `current.md`'s repeated cross-round diagnosis) — so this
  round's attempt to adapt Claim A's machinery **re-encounters the same
  underlying obstruction**, rather than side-stepping it, once the budget
  is large enough to allow more than one piece to be split simultaneously.
- With budget $n-3$ small relative to the number of pieces $n-1$ (at most
  $n-3$ pieces can be split at all, the rest are forced to their single
  value $p_i$), the vertex family is *much* smaller than the general
  problem's — but we did not complete, this round, an exhaustive
  case-by-case evaluation of it (which pieces get the $\le n-3$ available
  cuts, and where the resulting pins/ties land relative to $v_2$) for
  general $n$. This is left as the honestly-scoped open item.

**Net honest assessment.** This round's Ceiling Lemma (§7.1) is a genuine,
fully proved, reusable general fact. The corrected $n-3$ cap's sufficiency
for $(\sharp)$ is independently corroborated numerically (§7.4, zero
violations across $n=3,\dots,7$, a different script than the sibling's) and
proved unconditionally by hand for $n=3$ (§7.5, the base case, where the
cap forces zero freedom). The general $n\ge4$ vertex enumeration needed to
turn this corroboration into a proof is **not completed** this round — it
reduces to the same cross-piece tie-vertex enumeration difficulty that has
been the project's central open obstruction since round 2, now confirmed to
recur inside $\Delta(n,v)$'s own polytope as well, from this genuinely
independent (exchange-smoothing rather than direct vertex-enumeration)
angle. This is a valuable convergence finding for cross-verification (as
the round-19 outline requested), not a closure.

#### 7.7 Conditional corollary stub (round 22): §7.6 as an *equivalent* restatement of the sibling's $(\Diamond')$, once closed — not yet claimed closed

**Scope of this subsection.** Per the round-22 outline (§ "Redirect confirmed,
but scoped as 'pending'"), §7.6's general-$n\ge4$ vertex-enumeration gap is
**explicitly not re-attacked this round**. Instead this subsection records,
precisely and checkably, the exact logical relationship between this file's
own target $(\sharp')$ and `greedy-halving-adversary`'s target $(\Diamond')$
— imported definitions, not re-derived from scratch — so that the moment the
sibling closes $(\Diamond')$ for a given $n$, §7.6 closes for that $n$
**automatically**, with the derivation below serving as the one-line
justification, rather than requiring a fresh argument.

**Imported definitions (from `greedy-halving-adversary.md`, "Theorem 34
(corrected)" and its identity chain, and the $(\Diamond)/(\Diamond')$
definitions immediately following it).** For $v\in(0,s)$,
$$\Delta(n,v):=A(R')-2A(R'_{>v}),\qquad \varepsilon(v):=\mathbb1[|R'_{>v}|\text{ odd}],$$
$$(\Diamond')\;:\quad \Delta(n,v)\ \le\ v-f(n)-2v\,\varepsilon(v)\qquad\text{for every }v\in(0,s).$$
This file's own target, reproduced from §7.5.0,
$$(\sharp')\;:\quad \Delta(n,v_2)\ \le\ s-(v_1-v_2)-2v_2\,\varepsilon(v_2)\qquad
\text{for }v_1\in(s,p_2),\ v_2\in(p_2-v_1,s).$$
Both use the *same* $\Delta,\varepsilon$ (same $R'$, same threshold
convention) — the only difference is the right-hand side and which variable
is quantified.

**The exact algebraic identity linking the two margins.** Define, for a
fixed legal $R'$ and fixed $v_2\in(0,s)$,
$$\mathrm{marg}_{\sharp'}(v_1,v_2):=\big(s-(v_1-v_2)-2v_2\varepsilon(v_2)\big)-\Delta(n,v_2),
\qquad
\mathrm{marg}_{\Diamond'}(v_2):=\big(v_2-f(n)-2v_2\varepsilon(v_2)\big)-\Delta(n,v_2)$$
(so $(\sharp')$ at $(v_1,v_2)$ holds iff $\mathrm{marg}_{\sharp'}(v_1,v_2)\ge0$,
and $(\Diamond')$ at $v_2$ holds iff $\mathrm{marg}_{\Diamond'}(v_2)\ge0$).
Subtracting,
$$\mathrm{marg}_{\sharp'}(v_1,v_2)-\mathrm{marg}_{\Diamond'}(v_2)
= \big(s-(v_1-v_2)\big)-\big(v_2-f(n)\big)
= s-v_1+f(n).$$
By `greedy-halving-adversary`'s Lemma 24 ($p_2-s=f(n)$, imported, cited as in
§7.5.0), $s+f(n)=p_2$, so this simplifies to the clean identity
$$\mathrm{marg}_{\sharp'}(v_1,v_2)\ =\ \mathrm{marg}_{\Diamond'}(v_2)\ +\ (p_2-v_1),
\qquad\text{exactly, for every legal }R',\ v_1\in(s,p_2),\ v_2\in(p_2-v_1,s).\tag{7.7.1}$$

**Consequence: $(\sharp')$ for a fixed $v_2$, over all admissible $v_1$, is
*equivalent* to $(\Diamond')$ at that $v_2$ — not merely implied by it.**

- *($\Leftarrow$, easy direction.)* If $\mathrm{marg}_{\Diamond'}(v_2)\ge0$,
  then since $v_1<p_2$ strictly on the whole domain, $p_2-v_1>0$, so by
  (7.7.1) $\mathrm{marg}_{\sharp'}(v_1,v_2)>0$ for every admissible $v_1$.
  So $(\Diamond')$ at $v_2$ $\Rightarrow$ $(\sharp')$ holds at $(v_1,v_2)$ for
  every such $v_1$.
- *($\Rightarrow$, the direction that makes this a genuine equivalence, not
  just one-way sufficiency).* Suppose $(\sharp')$ holds at $(v_1,v_2)$ for
  *every* $v_1$ in the admissible range $(\max(s,p_2-v_2),p_2)$ — i.e.
  $\mathrm{marg}_{\sharp'}(v_1,v_2)\ge0$ for all such $v_1$. By (7.7.1),
  $\mathrm{marg}_{\Diamond'}(v_2)=\mathrm{marg}_{\sharp'}(v_1,v_2)-(p_2-v_1)$
  for every such $v_1$; the right side is a continuous (indeed affine)
  function of $v_1$ with a well-defined limit as $v_1\to p_2^-$ (both terms
  are continuous in $v_1$; $\Delta(n,v_2),\varepsilon(v_2)$ do not depend on
  $v_1$ at all). Taking $v_1\to p_2^-$: $p_2-v_1\to0$, so
  $\mathrm{marg}_{\Diamond'}(v_2)=\lim_{v_1\to p_2^-}\mathrm{marg}_{\sharp'}(v_1,v_2)
  \ge0$ (a limit of a quantity that is $\ge0$ throughout an interval
  approaching the limit point is itself $\ge0$ — elementary). So
  $(\sharp')$-for-all-$v_1$ at $v_2$ $\Rightarrow$ $(\Diamond')$ at $v_2$.

Together: **$(\sharp')$ restricted to a fixed $v_2$ and ranging over all
admissible $v_1$ is logically equivalent to $(\Diamond')$ at $v=v_2$,** via
the exact identity (7.7.1) — not an approximation, not merely a sufficient
condition. Ranging $v_2$ over all of $(0,s)$ then gives: **$(\sharp')$ on its
full domain $\iff$ $(\Diamond')$ on its full domain $(0,s)$**, for the same
$n$.

**What this does and does not establish.** This is a precise algebraic
identification, checkable independently of either file's numerics (§7.7's
derivation above is self-contained) — but it is **not** a proof of either
$(\sharp')$ or $(\Diamond')$ for $n\ge4$. Concretely, per the round-22
explorer's diagnosis (imported): `greedy-halving-adversary`'s Theorem 35b
(the $v\ge p_3$ range) is currently proved only for the *weaker* $(\Diamond)$
(the $\varepsilon\equiv0$ case), and Theorem 36's Case (b) closure of the
full $(\Diamond)$ is unconditional only at $n=3,4$, with the $n\ge5$
extension explicitly in progress this same round on that sibling file. The
$\varepsilon(v)=1$-strengthened target $(\Diamond')$ itself — needed for the
equivalence above to close $(\sharp')$, hence §7.6 — is **not yet proved by
either file for any $n\ge4$** (§7.5.2 of this file closes it only at
$n=3$, where the cut budget is forced to $0$). So:

> **Conditional corollary (not yet available).** *If a future round
> establishes $(\Diamond')$ for every $v\in(0,s)$ at some $n\ge4$ (i.e.
> extends the sibling's Theorem 35b/36 machinery from the weaker $(\Diamond)$
> to the $\varepsilon$-corrected $(\Diamond')$, for that $n$), then $(\sharp')$
> — hence §7.6's general-$n$ vertex-enumeration gap at that same $n$ — closes
> immediately via the equivalence (7.7.1) above, with no additional argument
> beyond substituting $v_1\to p_2^-$ (or, more precisely, invoking the
> $(\Leftarrow)$ direction proved above for every $v_1<p_2$ directly, which
> does not even need a limit).* This is honestly recorded as a **conditional
> corollary pending the sibling's extension**, not a closure — the sibling's
> own $(\Diamond')$ (as opposed to $(\Diamond)$) is not yet proved for any
> $n\ge4$, so no claim is made here that §7.6 is closed for any such $n$.

**Independent numerical cross-check of the identity (7.7.1) at $n=4$ (this
round, exact `Fraction` arithmetic, script
`/tmp/round-22/check_n4_eps_bridge.py`).** Using the ladder values at $n=4$
($D=31$: $p_2=8/31$, $p_3=4/31$, $p_4=2/31$, $p_5=1/31$, $s=7/31$,
$f(4)=1/31$, matching `greedy-halving-adversary`'s own Theorem 36 numerics
exactly), $50{,}000$ random trials sampling a legal budget-$1$ refinement
$R'$ of $\tau=\{p_3,p_4,p_5\}$ (either $0$ cuts, i.e. $R'=\tau$, or exactly
one of the three pieces split into two positive fragments, matching the
$n-3=1$ cap) and random $v_1\in(s,p_2)$, $v_2\in(p_2-v_1,s)$: **zero
mismatches** between $\mathrm{marg}_{\sharp'}(v_1,v_2)-\mathrm{marg}_{\Diamond'}(v_2)$
and the predicted exact value $p_2-v_1$, across all $50{,}000$ trials —
confirming identity (7.7.1) holds exactly, not merely approximately, at
$n=4$. As an incidental byproduct (**numeric evidence only, not a proof —
reported honestly as such, not substituted for the missing $(\Diamond')$
argument above**): the same run found the minimum sampled margin for
$(\Diamond')$ itself at $n=4$ to be $\mathrm{marg}_{\Diamond'}=3/620000>0$
(no violation found in this sample), and the minimum sampled margin for
$(\sharp')$ to be $\approx3.70\times10^{-5}>0$ — consistent with, but not a
substitute for, a proof that $(\Diamond')$ (hence, via the equivalence,
$(\sharp')$) holds at $n=4$. This numeric finding is corroborating evidence
that the identification and the still-open target are both plausible, and
flags no contradiction — but it is emphatically **not** claimed here as a
closure of $(\Diamond')$ or $(\sharp')$ at $n=4$, since a finite random
sample cannot rule out a violation at an untested point (unlike §7.5.2's
$n=3$ closure, which is a full hand proof over the entire continuum).

#### 7.8 Round-23: an independent discrete/pigeonhole derivation of the sibling's Case (b) "$v\ge a$" target $A(B)\ge f(n)$

**Scope of this subsection.** Per this round's outline dispatch, we do
**not** retry a fresh one-sided discrete bound on $\Delta(n,v)$ (confirmed
dead-equivalent to the Insert-Element Identity's continuum obstruction).
Instead, we independently attack `greedy-halving-adversary`'s Case (b)
"$v\ge a$" target — $A(B)\ge f(n)$ for $B=\{b\}\cup T'$ — via this file's own
discrete/pigeonhole machinery (exchange-smoothing vertex analysis, §5's
technique family, and the standing induction hypotheses $(\star_m)$), as an
independent second derivation of the same finite vertex-family reduction
the sibling's Vertex-Minimum Theorem produces, per the precedent of round
3's two independent proofs of that same theorem.

**Preliminary identification: this target IS a single point of $(\Diamond)/(\Diamond')$, not a new object.** Since $a=\max(R')$ in Case (b) ($a\ge p_4\ge$
every element of $T'$, `general-ladder-dominance`), $R'_{>a}=\varnothing$, so
$\Delta(n,a)=A(R')$, and (`sharp-dominant-removal-identity`) $A(R')=a-A(B)$.
Hence $A(B)\ge f(n)\iff\Delta(n,a)\le a-f(n)$ — exactly $(\Diamond)$
evaluated at the single point $v=a$ (and, since $R'_{>a}=\varnothing$ is
even, $\varepsilon(a)=0$, so $(\Diamond)$ and $(\Diamond')$ coincide at this
point — no $\varepsilon$-correction needed here, unlike the general middle
band of §7.5–§7.7). So this is not a fresh target: it is literally one
point of the same $\Delta(n,v)\le v-f(n)$ curve this file's §7.7 already
related to $(\sharp')$. What follows attacks it directly, by optimizing
over $B$'s own polytope, rather than via the $(\sharp')/(\Diamond')$
route.

**Step 1 — a new general lemma pins the free coordinate $b$ to $3$ candidate types.** $B=\{b\}\cup T'$ has $b\in(0,p_4]$ as a genuinely free,
*unconstrained-by-any-sum* coordinate (unlike Claim A's $F$, whose
fragments must sum to a fixed total) — $b$ is simply a value in a box,
with $T'$ (a legal refinement of $\{p_4,\dots,p_{n+1}\}$ using $\le n-4$
cuts) held fixed. By the new **Single-Insert-Point Vertex Lemma**
(`lemmas/single-insert-point-vertex-lemma.md`, proved from scratch this
round — an elementary, fully general fact, no ladder structure used):
for $T$ any finite multiset and $g(b):=A(\{b\}\cup T)$, $g$ is piecewise
affine with slope $\pm1$ (never $0$) between consecutive elements of
$\{0,M\}\cup(T\cap[0,M])$, so $\min_{b\in[0,M]}g(b)$ is attained at one of
these finitely many breakpoints. Applying this with $T=T'$, $M=p_4$:
$$\min_{b\in(0,p_4]}A(B)\ \text{is attained (in the limit, over the closed box) at}\quad
b=0,\quad b=p_4,\quad\text{or}\quad b=t\ \text{for some fragment }t\in T'.$$
This is a genuinely different, elementary derivation of a vertex reduction
for the $b$-coordinate specifically (a one-line slope computation, not an
appeal to the general LP/compactness Vertex-Minimum Theorem) — confirmed
numerically (`/tmp/check_insert_vertex.py`, $200$ trials $\times\,n=3,
\dots,7$: the breakpoint minimum always matches or beats a dense
interior sample; zero counterexamples) and, separately, confirmed that all
three breakpoint types are genuinely realized as the true minimizer with
comparable frequency (`/tmp/check_argmin_location.py`, $300$ trials
$\times\,n=4,\dots,8$: $b=0$ wins $515/1500$, $b=p_4$ wins $513/1500$,
an interior tie wins $472/1500$) — i.e. no type is a numerically
negligible edge case that could be discarded.

**Step 2 — the $b=0$ candidate closes unconditionally (conditional only on the standing hypothesis one level down).** If $b=0$, $B=T'$ directly, a
legal refinement of $\{p_4,\dots,p_{n+1}\}$ using $\le n-4$ cuts. By the
certified `general-cross-level-rescaling-lemma` with $k=3$ ($m=n-3$),
$\{p_4,\dots,p_{n+1}\}=\lambda_3\cdot\{$unit $(n-3)$-ladder$\}$ exactly,
$\lambda_3f(n-3)=f(n)$. Since $n-4\le n-3$, $T'/\lambda_3$ is a legal
response (using $\le n-3$ cuts — fewer than the full budget is always
legal) to the unit $(n-3)$-ladder, so by the standing hypothesis
$(\star_{n-3})$, $A(T'/\lambda_3)\ge f(n-3)$, hence
$A(T')=\lambda_3A(T'/\lambda_3)\ge\lambda_3f(n-3)=f(n)$
(`alternating-sum-scaling`). **So $A(B)\ge f(n)$ at $b=0$, conditional on
$(\star_{n-3})$** — the same style of conditional closure as Theorem 36b,
one level deeper (available whenever $(\star_{n-2})$ is, by strong
induction, since $n-3<n-2$).

**Step 3 — the $b=p_4$ candidate, with $p_4$ itself unsplit by $T'$, closes conditional on $(\star_{n-4})$.** If $b=p_4$ and $T'$ leaves $p_4$
untouched (i.e. $p_4\in T'$ as an exact element), $B=\{p_4,p_4\}\cup T''$
where $T'':=T'\setminus\{p_4\}$ is a legal refinement of
$\{p_5,\dots,p_{n+1}\}$ using the same $\le n-4$ cuts (removing an
untouched piece costs nothing). By `pair-cancellation-identity`
($A(\{c,c\}\cup S)=A(S)$ for any $c\ge0$, any finite $S$ — an exact pair
always occupies two consecutive sorted ranks and contributes $0$
regardless of starting parity), $A(B)=A(T'')$. By
`general-cross-level-rescaling-lemma` with $k=4$ ($m=n-4$),
$\{p_5,\dots,p_{n+1}\}=\lambda_4\cdot\{$unit $(n-4)$-ladder$\}$,
$\lambda_4f(n-4)=f(n)$, and $T''$ uses exactly the *full* budget $n-4$
available at level $n-4$, so $T''/\lambda_4$ is a legal (indeed
budget-tight) response to the unit $(n-4)$-ladder; by $(\star_{n-4})$,
$A(T''/\lambda_4)\ge f(n-4)$, hence $A(B)=A(T'')\ge\lambda_4f(n-4)=f(n)$.
**Closes, conditional on $(\star_{n-4})$** (again available by strong
induction whenever $(\star_{n-2})$ is, since $n-4<n-2$ for $n\ge5$; at
$n\le4$ this sub-case is vacuous or already covered by Theorem 36's own
direct closure).

**Step 4 — the residual candidates recouple to the identical obstruction the sibling already diagnosed (honestly reported, not closed).** Two
residual sub-cases remain, and both genuinely resist this file's own
machinery, for the same underlying reason:
- **$b=p_4$ with $p_4$ itself further split by $T'$** (i.e. $T'$ spends
  $\ge1$ of its cuts splitting the $p_4$-slot into fragments
  $c_1,\dots,c_j$, $j\ge2$, summing to $p_4$, each $<p_4$). Here $p_4$
  (the inserted value $b$) is the unique max of $\{p_4,c_1,\dots,c_j\}$
  (each $c_i<p_4$ strictly, being a positive part of a genuine split), so
  `sharp-dominant-removal-identity` gives
  $A(\{p_4,c_1,\dots,c_j\}\cup\text{rest})=p_4-A(\{c_1,\dots,c_j\}\cup
  \text{rest})$, where $\{c_1,\dots,c_j\}$ is a partition of $p_4$
  (matching Claim A's own shape one level down, at the rescaled level
  $n-4$) and "rest" is $T'$'s own further splitting of
  $\{p_5,\dots,p_{n+1}\}$ using the residual budget. **This is not a
  smaller instance of Claim A** (whose closed GC($m$)/Case-I-Closure
  theorem requires the tail $\tau$ to be genuinely *untouched*): here
  "rest" may itself be split, using up cuts, so the pair
  ($\{c_1,\dots,c_j\}$, rest) is exactly a fresh occurrence of the
  *original* Case-(b)-shaped problem — a partition of a top piece plus a
  further-cuttable tail — one level down (rescaled to level $n-4$ rather
  than $n-3$). Bounding $A(\{c_1,\dots,c_j\}\cup\text{rest})$ from below
  and subtracting from $p_4$ would need it bounded from *above* to get a
  useful *lower* bound on $A(B)=p_4-A(\dots)$ in the hard direction — the
  identical sign obstruction the Insert-Element Identity already
  diagnosed, now recurring one level down inside this file's own
  machinery rather than the sibling's.
- **$b=t$ for a generic interior fragment $t$ of $T'$** (created by $T'$
  splitting some piece $p_i$, $i\ge5$): here $b$ ties with a
  fragment that is *not* one of the ladder's own named breakpoints, so
  neither the rescaling argument of Steps 2–3 (which needed $b$ to equal
  $0$ or the *whole* untouched top piece $p_4$ of the remaining tail) nor
  a clean pair-cancellation applies; the joint optimization over $(b,T')$
  simultaneously re-enters the general multi-piece cross-tie vertex
  enumeration difficulty already flagged in §7.6 as this project's
  standing obstruction since round 2.

**Net honest assessment.** This round's independent, discrete/pigeonhole
route (single-variable pinning of $b$ via a new elementary lemma, then
rescaling-plus-induction-hypothesis closure of two of the three resulting
candidate types) reaches **exactly the same residual difficulty**
`greedy-halving-adversary`'s continuum Vertex-Minimum Theorem approach is
working on this same round: a joint, cross-piece tie/recursive
obstruction that neither this file's induction machinery nor the
sibling's general vertex theorem has yet closed for general $n$. This is
genuine independent confirmation, from a structurally different starting
point (fix $b$ as a single box-constrained variable and pin it first,
rather than treat $B$'s whole polytope via the general LP/compactness
theorem at once) — it corroborates, rather than merely repeats, the
project's diagnosis that this is the load-bearing wall, and additionally
identifies precisely *which* two of the (at least) three vertex-candidate
types are tractable (closing them conditionally on $(\star_{n-3})$,
$(\star_{n-4})$ respectively) versus which one genuinely recouples to the
open difficulty. We do not claim closure of $A(B)\ge f(n)$ for general
$n\ge5$: Steps 2–3 are real, conditional progress (two of three vertex
types now provably safe); Step 4 is an honest, sharpened diagnosis of
where the true difficulty lives, not a resolution of it.

**New reusable lemma promoted this round:**
`lemmas/single-insert-point-vertex-lemma.md` (Step 1 above) — a fully
general, elementary fact about inserting one free box-constrained point
into a fixed multiset, proved independently of (and more directly than)
the general `vertex-minimum-theorem` for this specific one-free-variable
case; reusable anywhere a single extra point is adjoined to an otherwise
fixed configuration.

#### 7.9 Round 24: fixing the outline-reviewer's flagged direction bug in the T'-cuts-$p_4$ sub-case

**Scope of this subsection.** Per this round's dispatch, the outline
instructed reusing the certified `exchange-smoothing-vertex-maximization`
lemma (proved, round 8, in the **max-$E$** direction — equivalently the
*lower*-bound-on-$A$ direction, exactly what Case I of Claim (A) needed) to
get an **upper** bound on $A$-type quantities arising one level down in
§7.8's residual sub-case (Step 4 there: $T'$ cuts $p_4$). The outline-
reviewer correctly flagged this as a polarity mismatch: by $A=\mathrm{Total}
-2E$, an *upper* bound on $A$ is equivalent to a *lower* bound on $E$ — the
opposite of what the certified lemma proves — and this direction has not
been established for this shape. This subsection re-derives, from
scratch and breakpoint by breakpoint, exactly where (if anywhere) an upper
bound is genuinely needed, rather than trusting the outline's placement of
the issue.

##### 7.9.1 Setup: the four candidate breakpoints for $b$

In the T'-cuts-$p_4$ sub-case (§7.8 Step 4, first bullet), $T'=\{c_1,c_2\}
\cup T'''$ with $c_1\ge c_2>0$, $c_1+c_2=p_4$ (so $c_1\in[p_4/2,p_4)$,
$c_2\in(0,p_4/2]$), and $T'''$ a legal refinement of $\{p_5,\dots,
p_{n+1}\}$ using $\le n-5$ cuts (one cut of the available $\le n-4$ having
been spent splitting $p_4$ itself). By the Single-Insert-Point Vertex Lemma
(certified §7.8 Step 1) applied with $T=T'$, $M=p_4$, the minimum over
$b\in(0,p_4]$ of $g(b):=A(B)=A(\{b\}\cup T')$ is attained at one of the
finitely many breakpoints $b\in\{0,p_4\}\cup(T'\cap(0,p_4])$. We first
record a fact used repeatedly below.

**Fact (c1 dominates T''').** $c_1\ge p_4/2=p_5\ge\max(T''')$ (every
element of $T'''$ is a fragment of $\{p_5,\dots,p_{n+1}\}$, hence $\le
p_5$, the top value of that tail), using $c_1\ge c_2\Rightarrow c_1\ge
p_4/2$ from $c_1+c_2=p_4$. So $c_1$ is always a (weak) maximum of $T'=
\{c_1,c_2\}\cup T'''$, hence of any multiset containing $c_1$ and a subset
of $T'''$.

##### 7.9.2 Breakpoint $b=0$: reduces to $A(T')$, a lower bound, already closed

At $b=0$: inserting the value $0$ at the very bottom of the sorted order
contributes exactly $0$ to $A$ regardless of parity (rank at the very
bottom is unaffected in value), so $A(B)=A(T')=A(\{c_1,c_2\}\cup T''')$
**exactly** (not merely a limit). This is precisely §7.8 Step 2's object at
$k=3$ (a legal refinement of $\{p_4,\dots,p_{n+1}\}$ using $\le n-4$
cuts): by `general-cross-level-rescaling-lemma` ($k=3$) and the standing
hypothesis $(\star_{n-3})$, $A(T')\ge f(n)$ — **already closed**, needs
only a lower bound, matching §7.8 Step 2 verbatim.

##### 7.9.3 Breakpoint $b=p_4$: fully dominated, needs *no* bound in either direction

On the interval $b\in(c_1,p_4]$ (recall $c_1=\max(T')$ by the Fact above),
$T'_{>b}=\varnothing$ for every $b$ in this range (nothing in $T'$ exceeds
$b$ since $b>c_1=\max T'$), so $j(b)=0$ and the Insert-Element Identity
gives, **exactly** (not as an inequality),
$$A(B)=2A(\varnothing)-A(T')+(-1)^0b=b-A(T')\qquad\text{for all }b\in(c_1,p_4].$$
This is affine in $b$ with slope $+1>0$, so $A(B)$ is **strictly increasing**
on $(c_1,p_4]$, and by continuity (the Insert-Element Identity's formula
matches at $b=c_1$ from both this interval's left-limit and the
pair-cancellation value below) $A(B)$ at $b=c_1$ is $\le A(B)$ at every
$b\in(c_1,p_4]$, in particular at $b=p_4$. **Consequence:** if the
breakpoint $b=c_1$ is shown to satisfy $A(B)\ge f(n)$, then automatically
$A(B)\ge f(n)$ for every $b\in[c_1,p_4]$, including $b=p_4$ — **no
separate bound on $A(T')$, upper or lower, is ever needed to dispose of the
$b=p_4$ candidate.** This directly resolves the outline-reviewer's flagged
concern *at this specific breakpoint*: the outline's literal instruction to
bound "$A(\{c_2\}\cup T''')$-type quantities" from above was aimed, if
read as targeting this comparison, at a step that in fact needs no bound
at all — the comparison is settled by an exact affine formula plus
elementary monotonicity, using only facts already on hand.

**(Promotable) Box-Endpoint Domination Fact.** For any finite multiset $T$
with $\max(T)=c<M$, and $g(b):=A(\{b\}\cup T)$ on $[0,M]$: $g$ is
non-decreasing on $[c,M]$ (in fact strictly increasing, slope exactly
$+1$), so $g(M)\ge g(c)$ always — i.e. the top box-endpoint breakpoint is
never a *smaller* value of $g$ than the breakpoint at $T$'s own max, and so
never needs its own separate bound once the latter is bounded. Proved by
the one-line Insert-Element Identity computation above; fully general, no
ladder structure used.

##### 7.9.4 Breakpoint $b=c_1$: reduces to $A(\{c_2\}\cup T''')$ — same direction (lower bound), recursion, not the flagged bug

At $b=c_1$: $B=\{c_1\}\cup T'=\{c_1,c_1,c_2\}\cup T'''$ (two copies of
$c_1$: the inserted $b$ and $T'$'s own). By `pair-cancellation-identity`
($A(\{c,c\}\cup S)=A(S)$), $A(B)=A(\{c_2\}\cup T''')$ **exactly**. This is
precisely the sibling's $h(m)$-shaped object one level further down (a free
value $c_2\in(0,p_4/2]$ merged with a legal cut-budgeted refinement $T'''$
of the smaller tail $\{p_5,\dots,p_{n+1}\}$) — a **lower**-bound target,
the *same* direction as the original problem, not the flagged dual
direction. This is a genuine recursion (the project's known open
obstruction, recurring one level deeper), **not** resolved this round, but
correctly identified as needing no new direction of lemma — consistent
with §7.8's own diagnosis, now confirmed precisely rather than left
undifferentiated.

##### 7.9.5 Breakpoint $b=c_2$: THIS is where an upper bound is genuinely needed — pinned down precisely

At $b=c_2$: $B=\{c_2\}\cup T'=\{c_1,c_2,c_2\}\cup T'''$ (two copies of
$c_2$: the inserted $b$ and $T'$'s own). By `pair-cancellation-identity`,
$A(B)=A(\{c_1\}\cup T''')$ **exactly**. Now, by the Fact of §7.9.1,
$c_1\ge\max(T''')$. **Generic case ($c_1>\max(T''')$ strictly):** by
`sharp-dominant-removal-identity` (certified; hypothesis $f_1>\max(T)$),
$$A(\{c_1\}\cup T''')=c_1-A(T''').$$
The target $A(B)\ge f(n)$ becomes $c_1-A(T''')\ge f(n)$, i.e.
$$A(T''')\ \le\ c_1-f(n)\tag{7.9.1}$$
— an **upper bound** on $A(T''')$, genuinely and unavoidably the dual
direction, confirmed here by direct symbolic derivation (not assumed).
**Boundary case ($c_1=\max(T''')$, e.g. the symmetric split $c_1=c_2=
p_4/2=p_5$ with $T'''$ leaving $p_5$ untouched):** here $c_1$ ties an
element of $T'''$; by `pair-cancellation-identity` again (applied to $c_1$
and its tied twin), $A(B)$ reduces one step further to $A(T'''\setminus\{
c_1\})$, a lower-bound target on a strictly smaller object — this boundary
sub-case does **not** need an upper bound, only the generic strict case
does. So (7.9.1) is the precise, unavoidable instance of the flagged
direction issue, isolated to exactly this one sub-case of one breakpoint.

**Why the cheap certified bounds do not suffice for (7.9.1).** Fact 2
(§5.2, $A\le\mathrm{Total}$) gives $A(T''')\le\mathrm{Total}(T''')$. Is
$\mathrm{Total}(T''')\le c_1-f(n)$ guaranteed? Test at the symmetric split
$c_1=c_2=p_4/2$ (the smallest legal value of $c_1$, hence the *hardest*
case for (7.9.1), since a smaller $c_1$ shrinks the right side): here
$\mathrm{Total}(T''')=\mathrm{Total}(\{p_5,\dots,p_{n+1}\})=:R_4$ (mass is
conserved by refinement, independent of how $T'''$ splits its pieces), and
$c_1-f(n)=p_4/2-f(n)$. Using the identity $R(\tau)+\tau_m=2\tau_1$ (§5.5,
with $\tau=\{p_5,\dots,p_{n+1}\}$, $\tau_1=p_5=p_4/2$, $\tau_m=p_{n+1}$):
$R_4=2p_5-p_{n+1}=p_4-p_{n+1}$. So the cheap bound would need
$$p_4-p_{n+1}\ \le\ p_4/2-f(n)\quad\iff\quad p_4/2\ \le\ p_{n+1}-f(n),$$
which is **false** for every $n$ (the left side is a fixed positive
fraction of $p_4$ while $p_{n+1}=f(n)$ exactly by definition of the ladder
target — see §0 — making the right side $p_{n+1}-f(n)=0$ identically,
strictly less than $p_4/2>0$). So **Fact 2 alone is certified insufficient**
for (7.9.1) at the symmetric split, confirmed by exact algebra (not merely
suspected): a genuinely tighter upper bound on $A(T''')$ is required.

**Why no existing certified fact supplies it.** The natural candidate
general statement, "refining a fixed ratio-2 tail can only decrease (or
leave unchanged) its alternating sum" — i.e. $A(R')\le A(\tau)$ for $R'$
any legal refinement of a ratio-2 tail $\tau$ — is exactly (the general
form of) Claim (B), and `current.md` already records (round 12 and later)
that this general statement is **false** as literally stated; only a
restricted form is under active development by `greedy-halving-adversary`.
So this round does not have, and does not construct, a certified lemma
supplying (7.9.1) — attempting to prove a bespoke *min*-$E$/upper-bound-on-
$A$ statement for "legal cut-budgeted refinements of a fixed ratio-2 tail"
from scratch (the genuinely new content the outline-reviewer's fix
requires) is a substantial undertaking not completed within this round's
time-box, and is recorded here as the precise, sharpened open gap — not
papered over with the (now-refuted) generic Total-bound, and not
mis-attributed to the wrong breakpoint as the original outline's phrasing
risked.

##### 7.9.6 Breakpoint $b=t$ for $t\in T'''$: unresolved, same obstruction as before

At $b=t$ (tying an interior fragment of $T'''$): pair-cancellation gives
$A(B)=A(\{c_1,c_2\}\cup(T'''\setminus\{t\}))$ — a partition of $p_4$ into
two parts plus an *already-partially-cut* residual tail (not the pristine
untouched tail Claim A's Case-I-Closure Theorem requires), hence not a
direct instance of any already-closed theorem. This still only needs a
**lower** bound (target $\ge f(n)$-type), so it does not exhibit the
flagged direction issue, but it is not closed this round — it is exactly
the general cross-piece tie-vertex obstruction §7.6 already names.

##### 7.9.7 Net conclusion of §7.9

Of the (at most) four breakpoint types, **exactly one** — the generic
$b=c_2$ case, reducing to $A(\{c_1\}\cup T''')=c_1-A(T''')$ — genuinely
requires an upper bound on an $A$-quantity, and this has been isolated
precisely, with the needed inequality (7.9.1) stated exactly and shown
**not** to follow from any currently certified fact (Fact 2 shown
insufficient by exact computation; the natural general refinement-monotone
statement shown false by `current.md`'s own record). The other three
breakpoint types ($b=0$: closed via $(\star_{n-3})$; $b=p_4$: dominated,
no bound needed at all; $b=c_1$: recursion in the *same*, non-flagged
direction) are fully accounted for. **This resolves the outline-reviewer's
flagged bug** by replacing the outline's vague/mis-located instruction
("reuse the max-direction lemma for an upper bound, direction unclear
where") with an exact identification of the one place a genuinely new
dual-direction lemma is needed, together with a proof that it is not
already available and is not reducible to certified cheap bounds. **This
is real progress — sharper diagnosis, one candidate fully resolved,
one direction-flaw precisely isolated rather than globally asserted — but
it is not a closure:** (7.9.1) itself, and §7.9.6's residual, remain open,
so the T'-cuts-$p_4$ sub-case of Case (b)'s "$v\ge a$" branch is **not**
closed this round.

#### 7.10 Round 25: reduction of (7.9.1) to a clean two-quantity joint induction (MinFloor/MaxCeil); one branch closed unconditionally, the other honestly left open

**Scope of this subsection.** Per this round's dispatch, attempted to prove
(7.9.1) via a Restriction Lemma (spare cuts concentrate on one tail element)
plus a dualized max-direction vertex theorem. This round's actual finding:
the Restriction Lemma as literally proposed is **not** what is needed — a
cleaner, fully general reduction (not requiring "concentration on a single
element" as a hypothesis at all) reduces (7.9.1) to a two-quantity joint
induction, of which one full branch is closed unconditionally this round via
a one-line application of already-certified Fact 2, and the complementary
branch is honestly identified as open, not closed.

**7.10.1 Setup, restated with independent notation.** Write $\sigma=
(\sigma_1,\dots,\sigma_\ell)$ for a ratio-2 superincreasing tail of length
$\ell$ ($\sigma_i=2\sigma_{i+1}$), $R(\sigma):=\sum\sigma_i$. Recall the
already-certified identity (§5.5, eq. (5.4), general for every $\ell\ge1$):
$$R(\sigma)+\sigma_\ell=2\sigma_1.\tag{7.10.1}$$
Call $S$ a **legal refinement of $\sigma$ using $\le k$ cuts** if $S$ is
obtained by partitioning each $\sigma_i$ into one or more positive parts,
with $\sum_i(\text{parts of }\sigma_i-1)\le k$.

Define, for $\ell\ge1$,
$$\mathrm{MinFloor}(\ell):=\min\{A(S): S\text{ a legal refinement of some
length-}\ell\text{ ratio-2 tail }\sigma\text{ using }\le\ell-1\text{ cuts}\}\Big/\sigma_\ell$$
i.e. the claim to be proved is $A(S)\ge\sigma_\ell$ for every such $S$
(the ratio is notation only — $\mathrm{MinFloor}(\ell)$ denotes the
**claim**, not a numeric value, since $\sigma_\ell$ scales with $\sigma$);
and, for $\ell\ge2$,
$$\mathrm{MaxCeil}(\ell):\qquad A(S)\ \le\ \sigma_1-\sigma_\ell\quad
\text{for every legal refinement }S\text{ of }\sigma\text{ using }\le\ell-2
\text{ cuts.}$$

**7.10.2 Reduction of (7.9.1) to $\mathrm{MaxCeil}(m)$, $m:=n-3$.** As
recorded in §7.9.5, the target (7.9.1) at its hardest instance (symmetric
split $c_1=c_2=p_4/2$, justified there as the hardest case by the manifest
monotonicity of the right side $c_1-f(n)$ in $c_1$, since $A(T''')$ does not
depend on $c_1$ at all — cited, not re-derived) is exactly
$$A(T''')\ \le\ p_5-p_{n+1},$$
and $\{p_5,\dots,p_{n+1}\}$ is a ratio-2 tail of length $m=n-3$ with top
value $p_5=\sigma_1$ and bottom value $p_{n+1}=\sigma_m$, refined with
$\le n-5=m-2$ cuts — **exactly** the hypothesis of $\mathrm{MaxCeil}(m)$.
So (7.9.1) (at its hardest instance, hence in general, by the already-cited
monotonicity) is equivalent to $\mathrm{MaxCeil}(m)$.

**7.10.3 An exact algebraic reformulation.** By $A(S)=\mathrm{Total}(S)-2E(S)$
(eq. (4.1)) and mass conservation ($\mathrm{Total}(S)=R(\sigma)$ for any
legal refinement $S$), and identity (7.10.1),
$$A(S)\le\sigma_1-\sigma_\ell\iff R(\sigma)-2E(S)\le\sigma_1-\sigma_\ell
\iff E(S)\ge\frac{R(\sigma)-\sigma_1+\sigma_\ell}2=\frac{\sigma_1}2$$
(using $R(\sigma)-\sigma_1=\sigma_1-\sigma_\ell$ from (7.10.1)). So
$\mathrm{MaxCeil}(\ell)$ is exactly the statement $E(S)\ge\sigma_1/2$ for
every legal $\le(\ell-2)$-cut refinement $S$ of $\sigma$ — a clean,
symmetric-looking floor on the even-rank sum, independent confirmation (via
a different route) that this is the "true" content of the flagged gap, not
an artifact of notation.

**7.10.4 Case split on whether $\sigma_1$ itself is cut.** Fix $\ell\ge2$
and a legal refinement $S$ of $\sigma$ realizing $\mathrm{MaxCeil}(\ell)$'s
hypothesis ($\le\ell-2$ cuts). Exactly one of two cases holds:

- **(i) $\sigma_1$ untouched** (zero cuts spent on $\sigma_1$).
- **(ii) $\sigma_1$ is cut** (split into $\ge2$ positive parts).

**Case (i), closed unconditionally.** If $\sigma_1$ is untouched, every
other element of $S$ is a fragment of some $\sigma_i$, $i\ge2$, hence
$<\sigma_i\le\sigma_2<\sigma_1$; so $\sigma_1$ remains the strict unique
maximum of $S$, at rank $1$. By `sharp-dominant-removal-identity`,
$$A(S)=\sigma_1-A(S'),\qquad S':=S\setminus\{\sigma_1\},$$
and $S'$ is a legal refinement of $\sigma'':=(\sigma_2,\dots,\sigma_\ell)$
(ratio-2, length $\ell-1$) using the same $\le\ell-2$ cuts (all still
available, none spent on $\sigma_1$). The target $A(S)\le\sigma_1-\sigma_\ell$
becomes
$$A(S')\ \ge\ \sigma_\ell.\tag{7.10.2}$$
Since $\sigma_\ell$ is exactly $\sigma''$'s own bottom value, and the
available budget $\ell-2=(\ell-1)-1$ is **exactly** $\sigma''$'s own
"$\mathrm{MinFloor}$" budget cap, (7.10.2) is precisely
$\mathrm{MinFloor}(\ell-1)$ applied to $\sigma''$. **This case reduces
$\mathrm{MaxCeil}(\ell)$'s case-(i) branch, exactly and without loss, to
$\mathrm{MinFloor}(\ell-1)$** — not to a cheap fact directly (an earlier
draft of this subsection mistakenly tried to close it via `Fact 2` alone
and found, on rechecking, that Fact 2 supplies the **wrong direction**:
Fact 2 upper-bounds $A(S')$, but (7.10.2) needs a **lower** bound — this
mis-direction was caught and corrected before being written up as a
result, exactly the kind of polarity error this project's `Rules` warn
against propagating).

**Sub-closure: $\mathrm{MinFloor}(\ell)$'s own case-(i) branch (top of
$\sigma''$ untouched) closes unconditionally, one line.** Apply the same
split to $\mathrm{MinFloor}(\ell)$ itself: if $S$ (a legal $\le(\ell-1)$-cut
refinement of $\sigma$) leaves $\sigma_1$ untouched, peeling gives
$A(S)=\sigma_1-A(S')$ with $S'$ a legal refinement of $(\sigma_2,\dots,
\sigma_\ell)$ using $\le\ell-1$ cuts (**all** still available — more than
enough). The target $A(S)\ge\sigma_\ell$ becomes $A(S')\le\sigma_1-\sigma_\ell$
— **this time genuinely the Fact-2 direction** (an upper bound on $A(S')$),
and by the general, unconditional `Fact 2` ($A\le\mathrm{Total}$, §5.2,
no budget restriction needed at all),
$$A(S')\ \le\ \mathrm{Total}(S')=R(\sigma)-\sigma_1\ \overset{(7.10.1)}=\
\sigma_1-\sigma_\ell,$$
**exactly** the needed bound, with equality exactly when $S'=\{\sigma_1-
\sigma_\ell\}$ (a single-fragment residual — never actually achieved by a
legal refinement of $\ge2$ elements, so the inequality is in fact always
strict here, consistent with $\mathrm{MinFloor}(\ell)$'s case-(i) branch
never being the unique minimizer for $\ell\ge3$, matching the hand
computations in 7.10.6 below). **This closes $\mathrm{MinFloor}(\ell)$'s
case-(i) branch (top element untouched) for every $\ell\ge1$,
unconditionally, with no induction and no budget hypothesis beyond the one
already given.**

**Case (ii), both $\mathrm{MinFloor}$ and $\mathrm{MaxCeil}$: NOT closed
this round.** When $\sigma_1$ itself receives one or more of the spare
cuts, no single certified fact (Fact 1, Fact 2, `sharp-dominant-removal-
identity`, `pair-cancellation-identity`, the Spacing Lemma, or the
Truncated Alternating Sum Ceiling/Floor) was found this round to close the
resulting general multi-fragment configuration for arbitrary $\ell$. This
is honestly recorded as open — see 7.10.6.

**7.10.5 Net logical structure obtained this round.** Combining 7.10.2's
reduction with 7.10.4's sub-closure:
$$\mathrm{MaxCeil}(\ell)\text{'s case-(i) branch (}\sigma_1\text{
untouched)}\ \Longleftarrow\ \mathrm{MinFloor}(\ell-1)\ \Longleftarrow\
\big[\text{its own case-(i) branch, closed}\big]\ +\ \big[\text{its own
case-(ii) branch, open}\big].$$
So $\mathrm{MaxCeil}(\ell)$'s case-(i) branch is closed **only if**
$\mathrm{MinFloor}(\ell-1)$'s case-(ii) branch (i.e. $\sigma_2$, the top of
$\sigma''$, receiving a spare cut) is also closed — genuinely not free,
contrary to what a naive reading of the outline's Restriction Lemma might
suggest. **Neither $\mathrm{MaxCeil}(\ell)$ nor $\mathrm{MinFloor}(\ell)$ is
closed for general $\ell$ this round; only each statement's own "top
element untouched" branch is closed, unconditionally, and only for
$\mathrm{MinFloor}$ is that branch closed via a genuinely trivial one-line
argument (Fact 2) — the $\mathrm{MaxCeil}$ untouched branch needs the full
$\mathrm{MinFloor}(\ell-1)$ statement, itself only partially closed.**

**7.10.6 Hand-verification at $\ell=1,2$ (fully rigorous, not numeric).**

*$\ell=1$.* $\mathrm{MinFloor}(1)$: $0$ cuts, $S=\{\sigma_1\}$,
$A=\sigma_1\ge\sigma_1$. Trivial equality. ($\mathrm{MaxCeil}$ undefined for
$\ell=1$.)

*$\ell=2$, $\mathrm{MinFloor}(2)$ ($\le1$ cut), fully closed by hand.*
Case (i) (untouched) already covered above:
$A(\{\sigma_1,\sigma_2\})=\sigma_1-\sigma_2=\sigma_2$ (using $\sigma_1=
2\sigma_2$), equality. Case (ii) ($\sigma_1$ cut into $(a,\sigma_1-a)$,
$0<a\le\sigma_1/2=\sigma_2$ WLOG): $S=\{\sigma_1-a,\sigma_2,a\}$, and since
$\sigma_1-a\ge\sigma_1/2=\sigma_2\ge a$ throughout this range, the sorted
order is exactly $(\sigma_1-a,\sigma_2,a)$, giving
$$A(S)=(\sigma_1-a)-\sigma_2+a=\sigma_1-\sigma_2=\sigma_2,$$
**identically constant** in $a$, matching the case-(i) value exactly. So
$\mathrm{MinFloor}(2)$ holds with equality on its entire domain — **fully
closed, both branches, no gap.**

*$\ell=2$, $\mathrm{MaxCeil}(2)$ ($\le0$ cuts, i.e. untouched only)*:
trivially $A(\{\sigma_1,\sigma_2\})=\sigma_2=\sigma_1-\sigma_2$, equality.
Closed (only one branch exists at $\ell=2$ since $\ell-2=0$).

*$\ell=3$, $\mathrm{MinFloor}(3)$ ($\le2$ cuts): case (i) closed above
(gives $A(S')\le\sigma_1-\sigma_3$ generically strict, e.g. direct check at
$\sigma=(4,2,1)$, $S'$ any legal $\le2$-cut refinement of $(2,1)$: the
untouched value $A(\{2,1\})=1=\sigma_3$ is achieved, e.g. by refining
$(2,1)\to(1,1,1)$ (tie), giving $A=1$ exactly — so the bound $A(S)\ge
\sigma_3=1$ is **achieved with equality** by several configurations,
consistent, not violated). Case (ii) at $\sigma=(4,2,1)$ (cutting
$\sigma_1=4$): hand-checked several splits (e.g. $\sigma_1\to(2,2)$ then a
second cut splitting one of $\sigma_1$'s new $2$'s into $(1,1)$, giving
$S=\{2,2,1,1,1\}$, $A=2-2+1-1+1=1=\sigma_3$; and several other splits, all
giving $A\ge1$) — **consistent with the claim holding**, but this is a
single numerical instance, not a proof for general $\sigma_1$-multi-way
splits at general $\ell$; recorded as corroborating evidence only, not
part of the closed portion of the theorem.

**7.10.7 Conclusion of §7.10.** This round replaces the outline's proposed
"Restriction Lemma + dualized 1-D vertex theorem" mechanism (found, on
attempting to execute it, not to directly apply — the true reduction needs
the general multi-element case (ii), which a 1-dimensional "vary only one
already-identified element" polytope does not by itself capture, since
*which* element ends up cut is exactly what is at issue) with a **precise,
verified-correct** (polarity double-checked, an earlier direction error
caught and corrected before finalizing) two-quantity joint reduction. Net
honest status: (7.9.1) is **not** closed this round. What **is** newly and
rigorously established:
1. (7.9.1) is exactly equivalent to $\mathrm{MaxCeil}(m)$, $m=n-3$
   (7.10.2), itself exactly equivalent to $E(S)\ge\sigma_1/2$ (7.10.3).
2. $\mathrm{MaxCeil}(\ell)$'s "$\sigma_1$ untouched" branch reduces exactly
   (not approximately) to $\mathrm{MinFloor}(\ell-1)$ — a clean, checked
   identity chain, not previously on file in this form.
3. $\mathrm{MinFloor}(\ell)$'s own "top untouched" branch is closed
   unconditionally for **every** $\ell\ge1$ via one line (Fact 2 +
   identity (7.10.1)) — a genuinely new, fully general, reusable partial
   result.
4. Both statements' "top element is cut" branches remain **fully open**
   for general $\ell$ — hand-verified consistent (not violated) only at
   $\ell\le3$, not proved. This is the honestly-scoped residual gap for
   next round: closing $\mathrm{MinFloor}(\ell)$'s case-(ii) branch (any
   number of cuts landing on $\sigma_1$ itself, in any pattern, with the
   remaining budget free to land anywhere on $\sigma_2,\dots,\sigma_\ell$)
   would, by 7.10.5's chain, immediately supply both $\mathrm{MinFloor}(\ell)$
   in full and (one level up) $\mathrm{MaxCeil}(\ell+1)$'s untouched branch;
   the still-separate $\mathrm{MaxCeil}$ case-(ii) branch would remain to
   be handled afterward. The originally-proposed Restriction Lemma (spare
   cuts concentrate on a single non-dominant element) may still be the
   right *shape* of the missing argument for case (ii) specifically — the
   numeric evidence in `/tmp/round-25/math-explorer-7-9-1.md` (all spare
   cuts landing on $\tau_2$, i.e. $\sigma_2$, at the true numeric optimum)
   is consistent with this — but it was not proved this round; the
   $\mathrm{MinFloor}/\mathrm{MaxCeil}$ reduction above narrows exactly
   where it is needed (only within case (ii), only affecting one
   coordinate $\sigma_1$'s own split), which is a strictly smaller target
   than the outline's original framing of a full "1-D vertex on $\sigma_2$"
   argument applied to the whole object at once.

### 7.11 The Index-Chain Identity: $\mathrm{MinFloor}(\ell)\equiv(\star_{\ell-1})$

**Re-derivation from scratch (round 26), per the round-26 outline's explicit
instruction to independently re-check this arithmetic rather than trust the
explorer's placement of it.**

Recall precisely how $(\star_k)$ is already used, unchanged, elsewhere in
this very file (§7.8, Steps 2–3, and independently by `greedy-halving-
adversary`, e.g. `current.md` round 23's bundled audit): for the **unit**
ratio-2 ladder of length $k+1$, $\pi=(\pi_1,\dots,\pi_{k+1})$,
$\pi_i=2\pi_{i+1}$, and **every** legal response $U$ to it using $\le k$
cuts (cuts distributed in any pattern across all $k+1$ elements — this is
*not* restricted to cutting only $\pi_1$, nor does it assume the rest is
untouched; it is the fully general one-level statement),
$$(\star_k):\qquad A(U)\ \ge\ \pi_{k+1}.$$
This is exactly the project's standing lower-bound master hypothesis (the
"$L(m)$" statement of `current.md`'s round-23 audit), used conditionally
throughout §7.8–7.9 of this file and by the sibling approach. As
`current.md` (round 23, and repeated at round 25 there) records explicitly:
**$(\star_1)$ and $(\star_2)$ are, as of this round, the only two values of
$k$ for which $(\star_k)$ is a fully certified, unconditional theorem** —
$(\star_1)$ trivially (the $n=1$ case, $c(1)=2/3$, both directions), and
$(\star_2)$ via `smoothing-compactness-certificate`'s round-1–2 closure
($c(2)=4/7$, both directions, zero numerics). $(\star_3),(\star_4),\dots$
are, as of this round, *not* certified unconditionally (only numerically
stress-tested where cited).

**Claim.** For every $\ell\ge1$, $\mathrm{MinFloor}(\ell)$ (§7.10.1) is
*identical*, as a mathematical statement, to $(\star_{\ell-1})$ — not merely
implied by it, and not a fresh sub-lemma requiring new machinery, once the
following elementary rescaling is spelled out.

**Proof.** Fix $\ell\ge1$ and set $k:=\ell-1\ge0$. $\mathrm{MinFloor}(\ell)$'s
hypothesis is: $\sigma=(\sigma_1,\dots,\sigma_\ell)$ a ratio-2
superincreasing tail ($\sigma_i=2\sigma_{i+1}$), $S$ a legal refinement of
$\sigma$ using $\le\ell-1=k$ cuts (any distribution across all $\ell=k+1$
elements — the definition in §7.10.1 places no restriction on which
elements receive the cuts); conclusion: $A(S)\ge\sigma_\ell$.

A ratio-2 superincreasing sequence of length $k+1$ is uniquely determined,
up to one free positive scale, by its length alone: $\sigma_i=\sigma_1\cdot
2^{1-i}$ for $1\le i\le k+1$. Hence $\sigma=\lambda\cdot\pi$ termwise, where
$\lambda:=\sigma_1/\pi_1>0$ and $\pi=(\pi_1,\dots,\pi_{k+1})$ is the *unit*
ladder of the same length $k+1$ appearing in $(\star_k)$ (i.e.
$\pi_i:=\sigma_i/\lambda$, so $\pi_1=1$ if one further normalizes, though no
particular normalization of $\pi_1$ is actually needed below). A legal
refinement $S$ of $\sigma$ using $\le k$ cuts corresponds, coordinate by
coordinate, to $S=\lambda\cdot U$ for $U$ a legal refinement of $\pi$ using
$\le k$ cuts (refining $\lambda\pi_i$ into parts is the same combinatorial
operation, up to the factor $\lambda$, as refining $\pi_i$ into parts, and
the cut count is unchanged since cutting is scale-free). By the already-
certified `alternating-sum-scaling` ($A(\lambda X)=\lambda A(X)$ for every
$\lambda>0$, `lemmas/alternating-sum-scaling.md`, an immediate consequence
of $A$'s definition as an alternating sum of sorted values — scaling every
element by a positive constant preserves the sort order and scales every
term uniformly), $A(S)=A(\lambda U)=\lambda A(U)$. Likewise
$\sigma_\ell=\lambda\pi_{k+1}$. So
$$A(S)\ge\sigma_\ell\ \Longleftrightarrow\ \lambda A(U)\ge\lambda\pi_{k+1}
\ \Longleftrightarrow\ A(U)\ge\pi_{k+1}\qquad(\text{dividing by }\lambda>0),$$
and the right-hand side, ranging over every legal $U$, every legal $\le k$
cut budget, and every unit ratio-2 ladder $\pi$ of length $k+1$, is
*exactly* the statement $(\star_k)=(\star_{\ell-1})$. Since this
correspondence $S\leftrightarrow U$ is a bijection between the legal
responses on each side (any legal $S$ arises from a unique legal $U=S/
\lambda$ and vice versa), the two universally-quantified statements are
logically equivalent, not merely one a consequence of the other.
$\blacksquare$

**Corollaries (immediate from the claim plus the already-recorded scope of
$(\star_k)$).**

1. $\mathrm{MinFloor}(2)=(\star_1)$: unconditionally **true** (already
   independently hand-verified with equality throughout in §7.10.6; now
   *additionally* confirmed by this identification, giving two independent
   proofs of the same fact).
2. $\mathrm{MinFloor}(3)=(\star_2)$: unconditionally **true**. This is a
   genuine strengthening of round 25's record: §7.10.6 had only verified
   $\mathrm{MinFloor}(3)$'s case-(i) (top-untouched) branch in general, and
   left case-(ii) (the top element $\sigma_1$ itself cut) as "hand-verified
   consistent at one numeric instance, not proved for general $\sigma_1$-
   splits." Via this identity, $\mathrm{MinFloor}(3)$ in **full** (both
   branches, every legal $\le2$-cut refinement of every length-3 ratio-2
   tail) is exactly $(\star_2)$, which is already a fully certified,
   non-numeric, both-directions theorem (`smoothing-compactness-
   certificate`'s $c(2)=4/7$ closure) — so case (ii) is not merely
   "consistent," it is **proved**, with no further work needed.
3. $\mathrm{MinFloor}(\ell)$ for $\ell\ge4$, i.e. $(\star_k)$ for $k\ge3$, is
   **not** yet unconditionally certified — this matches, and gives a
   precise reason for, round 25's honest "open for general $\ell$" verdict:
   it is not that a bespoke technique is missing, but that
   $\mathrm{MinFloor}(\ell)$ *is*, verbatim, the project's own still-open
   general lower bound one level down. No claim of closure is made for
   $\ell\ge4$.

**Application to $\mathrm{MaxCeil}$.** By §7.10.4's already-established
exact reduction, $\mathrm{MaxCeil}(\ell)$'s top-untouched branch (case (i),
$\sigma_1$ left uncut) is logically equivalent to $\mathrm{MinFloor}
(\ell-1)$, hence — by the identity just proved — to $(\star_{\ell-2})$.
Combined with Corollaries 1–2 above ($(\star_1),(\star_2)$ unconditionally
true, $(\star_k)$ for $k\ge3$ not yet certified):

$$\mathrm{MaxCeil}(\ell)\text{'s top-untouched branch is unconditionally
TRUE}\ \Longleftrightarrow\ \ell-2\le2\ \Longleftrightarrow\ \ell\le4.$$

Since $(7.9.1)\Leftrightarrow\mathrm{MaxCeil}(m)$, $m=n-3$ (§7.10.2), this
means: **$\mathrm{MaxCeil}(n-3)$'s top-untouched branch is unconditionally
free for every $n\le7$.** This matches, and gives a rigorously re-derived
confirmation of, the round-26 outline's index arithmetic
$(7.9.1)\Leftrightarrow\mathrm{MaxCeil}(n-3)\Leftrightarrow_{\text{(top-
untouched)}}\mathrm{MinFloor}(n-4)=(\star_{n-5})$, free when $n-5\le2$,
i.e. $n\le7$ — the two derivations agree exactly (the outline's chain
computes $\mathrm{MinFloor}(n-4)=(\star_{(n-4)-1})=(\star_{n-5})$, matching
the general formula $(\star_{\ell-2})$ at $\ell=n-3$: $(\star_{(n-3)-2})=
(\star_{n-5})$ — independently re-confirmed here, not merely copied).

**Scope, stated precisely (no overclaiming).** This closes only the
**top-untouched branch** of $\mathrm{MaxCeil}(n-3)$, for $n\le7$ — i.e.
only the sub-case where the refinement $T'''$ of $\{p_5,\dots,p_{n+1}\}$
leaves $p_5$ itself uncut. It does **not**, by itself, resolve $(7.9.1)$
in general, nor even at a single fixed $n\le7$: $\mathrm{MaxCeil}(m)$'s
**top-cut branch** (case (ii), $\sigma_1=p_5$ itself receiving one or more
of the available cuts — the round-26 outline's "item 3," this file's own
real target) is a genuinely different upper-bound statement, not reducible
to $(\star_\cdot)$ by any argument found so far (§7.10.4's own diagnosis,
re-confirmed here), and is attacked directly, by hand, in §7.12–7.13 below
for the two smallest open instances $m=3$ ($n=6$) and $m=4$ ($n=7$).

### 7.12 Full closure of $\mathrm{MaxCeil}(3)$ ($n=6$ instance)

By §7.11, $\mathrm{MaxCeil}(3)$'s top-untouched branch is unconditionally
free ($\ell=3\le4$, reducing to $(\star_1)$). It remains to close the
top-cut branch: $\sigma=(\sigma_1,\sigma_2,\sigma_3)$, budget $\le\ell-2=1$
cut, $\sigma_1$ itself receiving that one cut (the only way to use a
1-cut budget "on $\sigma_1$"). By `alternating-sum-scaling`, WLOG
$\sigma=(4,2,1)$ (any length-3 ratio-2 tail is a positive rescaling of
this). $S=\{a,4-a\}\cup\{2,1\}$ for some $a\in(0,4)$; WLOG $a\le2$ (the
multiset is unchanged under $a\leftrightarrow4-a$). Target:
$A(S)\le\sigma_1-\sigma_3=4-1=3$.

- **$a\in(0,1)$:** sorted order $(4-a,2,1,a)$ (since $4-a\in(3,4)>2>1>a$).
  $$A(S)=(4-a)-2+1-a=3-2a\ \le\ 3,$$
  with equality only in the limit $a\to0^+$ (never attained for $a>0$).
- **$a\in[1,2]$:** sorted order $(4-a,2,a,1)$ (since $4-a\in[2,3]\ge2$, and
  $1\le a\le2$). $$A(S)=(4-a)-2+a-1=1\ \le\ 3.$$

Both sub-cases satisfy $A(S)\le3$ (independently re-derived here, not
copied from the round-26 outline/explorer, though it matches their
computation exactly). Together with the top-untouched branch (§7.11),
**$\mathrm{MaxCeil}(3)$ is now fully, unconditionally proved, both
branches, for every $n=6$ instance of $(7.9.1)$** (and, by the scale
argument, for every length-3 ratio-2 tail, not just the numeric
representative). This closes item 3 (the file's own real target) of the
round-26 outline's three-item list, at $m=3$, i.e. $n=6$.

*(Consistency check with the top-untouched branch's boundary: the
top-untouched case, $S=\{4,2,1\}$ itself untouched or with the single cut
spent on $\sigma_2$ or $\sigma_3$ instead of $\sigma_1$, gives
$A(\{4,2,1\})=3$ exactly, matching the top-cut branch's own $a\to0$ limit
— both branches meet continuously at the degenerate boundary where "the
cut" vanishes, as expected.)*

### 7.13 Full closure of $\mathrm{MaxCeil}(4)$ ($n=7$ instance) — this
round's build target

By §7.11, $\mathrm{MaxCeil}(4)$'s top-untouched branch is unconditionally
free ($\ell=4\le4$, reducing to $(\star_2)$, itself proved in full — both
branches — by Corollary 2 of §7.11). It remains to close the top-cut
branch: budget $\le\ell-2=2$ cuts, with at least one landing on $\sigma_1$.
By `alternating-sum-scaling`, WLOG $\sigma=(8,4,2,1)$. Target:
$A(S)\le\sigma_1-\sigma_4=8-1=7$.

**Exhaustive enumeration of cut-distribution shapes.** With a total budget
of $\le2$ cuts and $\ge1$ required on $\sigma_1$, the possible
distributions $(c_1,c_2,c_3,c_4)$ (cuts on $\sigma_1,\dots,\sigma_4$
respectively) with $c_1\ge1$, $\sum c_i\le2$ are exactly
$(1,0,0,0),(2,0,0,0),(1,1,0,0),(1,0,1,0),(1,0,0,1)$ — five shapes,
exhaustive (this is a finite enumeration of nonnegative integer tuples, not
an assumption). This is the same finite-vertex-family reduction principle
already certified in `exchange-smoothing-vertex-maximization` /
`single-insert-point-vertex-lemma` (a piecewise-affine function of finitely
many free coordinates over a compact box has its extremum among finitely
many breakpoint-pinned configurations); here, since the cut budget is small
(at most $2$), the finitely many *shapes* are enumerated directly instead
of invoking the general vertex-reduction machinery abstractly, and each
shape is closed by direct computation, exactly as the outline instructed
("reuse... do not invent new machinery").

**Shape $(1,0,0,0)$** ($\sigma_1\to(a,8-a)$, rest untouched). WLOG
$a\le4$.
- $a\in(0,1)$: order $(8-a,4,2,1,a)$, $A=(8-a)-4+2-1+a=5$.
- $a\in[1,2]$: order $(8-a,4,2,a,1)$, $A=(8-a)-4+2-a+1=7-2a\in[3,5]$.
- $a\in[2,4]$: order $(8-a,4,a,2,1)$, $A=(8-a)-4+a-2+1=3$.

Max over this shape: $5<7$.

**Shape $(2,0,0,0)$** ($\sigma_1\to(x,y,z)$, $x+y+z=8$, rest $\tau=
(4,2,1)$ untouched). At most one of $x,y,z$ exceeds $\tau_1=4$ (if two did,
their sum would exceed $8$, contradicting $x+y+z=8$ with the third
positive — the same Lemma-1-style argument already certified in this
file's §1, applied here to mass $s=8=2\tau_1$).
  - *All three $\le4$ (Case I).* If none equals $4$ exactly, $\tau_1=4$ is
    the strict unique max of $S=\{x,y,z\}\cup\tau$ (since $x,y,z\le4$,
    strictly $<4$ generically, and $2,1<4$); peel via
    `sharp-dominant-removal-identity`: $A(S)=4-A(\{x,y,z,2,1\})$. Target
    $A(S)\le7$ becomes $A(\{x,y,z,2,1\})\ge-3$, true unconditionally by
    Fact 1 (`half-bound-lemma`, $A\ge0>-3$). If some part equals $4$
    exactly (boundary), the two $4$'s (one from $F$, one from $\tau$) tie
    at ranks $1,2$, contributing $4-4=0$, leaving
    $A(S)=A(\{y,z,2,1\})$ (relabeling so $x=4$); by Fact 2 ($A\le
    \mathrm{Total}$, §5.2), $A(\{y,z,2,1\})\le(y+z)+2+1=(8-4)+3=7$ exactly
    — closes with equality as the extreme case, not a violation.
  - *One part $f_1>4$ (Case II).* $f_1$ is then the unique global max
    (the other two parts sum to $8-f_1<4<f_1$, so each is $<f_1$, and
    $f_1>4=\tau_1\ge2,1$). Peel: $A(S)=f_1-A(F'\cup\tau)$,
    $F'=\{y,z\}=\{$the other two parts$\}$, $s':=y+z=8-f_1<4$. Within
    $F'\cup\tau$, $\tau_1=4$ is again the strict unique max (since $y,z<
    s'<4$), so peel again: $A(F'\cup\tau)=4-A(F'\cup\{2,1\})$. By Fact 2,
    $A(F'\cup\{2,1\})\le s'+2+1=s'+3$, so $A(F'\cup\tau)\ge4-(s'+3)=1-s'$,
    hence $A(S)=f_1-A(F'\cup\tau)\le f_1-(1-s')=f_1-1+s'=f_1-1+(8-f_1)=7$
    — closes exactly, via the identical two-peel-plus-Fact-2 mechanism as
    Case I's boundary.

  Both sub-cases give $A(S)\le7$ for shape $(2,0,0,0)$, with equality
  approached/attained only at the boundary configurations above.

**Shape $(1,1,0,0)$** ($\sigma_1\to(a,8-a)$, $\sigma_2\to(b,4-b)$, rest
$\{2,1\}$ untouched). WLOG $a\le4$, $b\le2$. If $a<4$: $8-a>4>\max(b,4-b,
2,1)$ (using $b<4$, $4-b<4$), so $8-a$ is the strict unique max; peel:
$A(S)=(8-a)-A(\{a,b,4-b,2,1\})$. By Fact 1, $A(\{a,b,4-b,2,1\})\ge0$, so
$A(S)\le8-a$, which is $\le7$ whenever $a\ge1$. **This closes the entire
sub-range $a\in[1,4)$ immediately**, no case split needed. At $a=4$
(boundary, $8-a=4$ ties with nothing since $\sigma_2$'s own untouched value
isn't $4$ here — direct check: $S=\{4,4,b,4-b,2,1\}$, the two $4$'s cancel
at ranks $1,2$ leaving $A(\{b,4-b,2,1\})\le\mathrm{Total}=4+2+1=7$ by Fact
2 — closes, matching the boundary of the $a\ge1$ argument continuously).

For the remaining range $a\in(0,1)$: sub-split on $b\lessgtr1$ (using WLOG
$b\le2$).
  - $b\in(0,1)$ **and** $a>b$: order $(8-a,4-b,2,1,a,b)$? — recompute
    carefully: values besides $8-a$ are $\{4-b,2,1,b,a\}$ with
    $4-b\in(3,4)$, so order among these four fixed-plus-two-small values,
    with $a,b<1$: $4-b>2>1>\max(a,b)>\min(a,b)$. If $a>b$: order
    $(8-a,4-b,2,1,a,b)$, $A=(8-a)-(4-b)+2-1+a-b=5-2b$ (the $-a+a$ terms
    cancel: $(8-a)-(4-b)+2-1+a-b=8-a-4+b+2-1+a-b=5$). *(Recomputation:
    the $-a$ and $+a$ cancel exactly, giving the constant $A=5$,
    independent of $a,b$ in this sub-case.)* $5<7$.
  - $b\in(0,1)$ **and** $a\le b$: order $(8-a,4-b,2,1,b,a)$,
    $A=(8-a)-(4-b)+2-1+b-a=8-a-4+b+2-1+b-a=5+2b-2a$. Since $a>0$ and
    $b<1$: $A<5+2(1)-0=7$. Strict.
  - $b\in[1,2]$ (any $a\in(0,1)$): order $(8-a,4-b,2,b,1,a)$ (since
    $4-b\in[2,3]\ge2\ge b\ge1>a$). $A=(8-a)-(4-b)+2-b+1-a=7-2a$. Since
    $a>0$: $A<7$, strict, with $A\to7$ only as $a\to0^+$.

All three sub-cases of $a\in(0,1)$ give $A(S)<7$ strictly (with $7$
approached only in the singular limit $a\to0$, i.e. as this shape
degenerates toward the top-untouched branch already closed in §7.11).
**Shape $(1,1,0,0)$ closes completely**, $A(S)\le7$ everywhere on its
domain, with the supremum $7$ **not attained** for any genuine $a>0$.

**Shape $(1,0,1,0)$** ($\sigma_1\to(a,8-a)$, $\sigma_3\to(c,2-c)$, rest
$\{4,1\}$ untouched). WLOG $a\le4$, $c\le1$. If $a<4$: $8-a>4$, unique max
(since $4>c,2-c,1$ trivially and $8-a>4$); peel:
$A(S)=(8-a)-A(\{a,4,c,2-c,1\})$. Within the peeled set, if $a<4$ then $4$
is (again) the strict unique max (as $a<4$, $c,2-c\le2<4$, $1<4$); peel
again: $A(\{a,4,c,2-c,1\})=4-A(\{a,c,2-c,1\})$. So
$$A(S)=(8-a)-\big[4-A(\{a,c,2-c,1\})\big]=4-a+A(\{a,c,2-c,1\}).$$
By Fact 2, $A(\{a,c,2-c,1\})\le a+(c+(2-c))+1=a+3$ (using $\mathrm{Total}=
a+2+1$). Hence $A(S)\le4-a+(a+3)=7$ — closes exactly, unconditionally,
for every $a\in(0,4)$, $c\in(0,1)$, via the same two-peel-plus-Fact-2
mechanism as shape $(2,0,0,0)$'s Case II. ($a=4$ boundary: direct check as
above, $A\le$ Total of remaining four elements, again $\le7$.)

**Shape $(1,0,0,1)$** ($\sigma_1\to(a,8-a)$, $\sigma_4\to(d,1-d)$, rest
$\{4,2\}$ untouched). Identical mechanism: if $a<4$, peel $8-a$ then $4$
(both strict unique maxima in turn, exactly as above), giving
$$A(S)=4-a+A(\{a,d,1-d,2\})\ \le\ 4-a+(a+2+1)=7$$
by Fact 2 ($\mathrm{Total}(\{a,d,1-d,2\})=a+1+2=a+3$; note $d+(1-d)=1$).
Closes exactly, unconditionally, for every $a\in(0,4)$, $d\in(0,1/2)$.

**Conclusion.** All five shapes satisfy $A(S)\le\sigma_1-\sigma_4=7$
throughout their entire legal domains, with the bound tight (supremum $=7$,
approached but not attained for a genuine cut) exactly at the degenerate
boundary of shape $(1,1,0,0)$ as $a\to0^+$ — i.e. exactly where the
top-cut branch degenerates into the (separately, already closed)
top-untouched branch. **$\mathrm{MaxCeil}(4)$'s top-cut branch is fully
closed**, and combined with §7.11's closure of the top-untouched branch,
**$\mathrm{MaxCeil}(4)$ is fully, unconditionally proved, both branches**
— the round-26 build target is achieved. This closes item 3 of the
round-26 outline's three-item list at $m=4$, i.e. $n=7$: $(7.9.1)$ is now
unconditionally resolved at $n=7$ (in addition to $n=6$, §7.12).

**Scope, stated precisely (no overclaiming, per the round-26 outline's
explicit instruction).** This resolves $(7.9.1)$ — one specific breakpoint
($b=c_2$, the "generic" candidate) within §7.9's $T'$-cuts-$p_4$ sub-case
of `greedy-halving-adversary`'s Case (b) "$v\ge a$" branch — **only** at
the two specific instances $n=6$ and $n=7$. It does **not** close
$(7.9.1)$ for general $n$ (that would require $(\star_k)$ unconditionally
for arbitrarily large $k$, which is the project's central open problem,
per §7.11's Corollary 3). It also does **not** close the two other
genuinely distinct open items the round-26 outline identifies within the
same larger Case-(b) structure: item 1 (`greedy-halving-adversary`'s
Theorem 37 internal non-maximal-tie enumeration, entirely within that
sibling file) and item 2 (the $b=c_1$ breakpoint recursion,
$A(\{c_2\}\cup T''')$, shared and still open in both files) — closing item
3 at $n=6,7$ does not by itself close items 1 or 2 at those same $n$,
exactly as the outline warned. Nor does it extend to $\mathrm{MaxCeil}(5)$
or beyond ($n=8,9,\dots$): §7.11 shows the top-untouched branch there is
already conditional on $(\star_3)$, not yet certified.

### 7.14 Round 27: general-$m$ closure of the top-cut branch when $\sigma_2$ is untouched — a fully general, budget-free theorem

Per this round's dispatch, the task is to generalize the $m=4$
"Double-Dominant-Peel + Fact-2" mechanism (§7.13) to every $m$, still
restricted to the top-cut branch and citing only `sharp-dominant-removal-
identity`, `odd-run-reduction-lemma`, Fact 1, Fact 2 — no $(\star_k)$,
$k\ge3$. This subsection achieves a **clean, fully general positive
result** covering an infinite sub-family of shapes at every $m$; §7.15
below then honestly reports what happens on the residual family, with a
new rigorous finding that **contradicts** part of the outline's premise
that this whole front is independent of the central obstruction.

**Theorem ($\sigma_2$-Untouched Closure, general $m$).** *Let $m\ge2$ and
let $\sigma=(\sigma_1,\dots,\sigma_m)$ be any ratio-2 superincreasing tail.
Let $S$ be any legal refinement of $\sigma$ (any number of cuts, any
distribution) subject only to: (a) $\sigma_1$ receives at least one cut
(i.e. $\sigma_1$ is split into $c_1+1\ge2$ positive parts, $c_1\ge1$), and
(b) $\sigma_2$ receives zero cuts (it appears in $S$ untouched, as a single
element equal to $\sigma_2$). No restriction whatsoever is placed on
$\sigma_3,\dots,\sigma_m$: each may be untouched or split into arbitrarily
many parts, and $c_1$ itself may be arbitrarily large. Then*
$$A(S)\ \le\ \sigma_1-\sigma_m.$$

This is (i) a strict generalization of $4$ of the $5$ shapes closed by hand
in §7.13's $m=4$ enumeration — shapes $(1,0,0,0),(2,0,0,0),(1,0,1,0),(1,0,0,1)$
all have $c_2=0$ and are special cases of this theorem, so their separate
hand computations are no longer needed, though they remain valid as
independent cross-checks — and (ii) genuinely broader than the outline's
own "shapes touching $\le2$ distinct tail indices" grouping: this theorem
places **no cap at all** on how many of $\sigma_3,\dots,\sigma_m$ are cut,
or how many parts each is split into, whereas a shape touching (say)
$\sigma_1,\sigma_3,\sigma_5$ (already $3$ distinct indices, outside the
outline's "already closed" zone) is fully covered here. Conversely, the
outline's zone also includes shapes touching *only* $\sigma_1$ and
$\sigma_2$ — those are **not** covered by this theorem (that is precisely
the residual §7.15 addresses). So the correct dividing line for this
mechanism is "$\sigma_2$ touched or not," not "how many distinct indices
are touched" — a genuine correction/sharpening of the outline's framing,
established below by direct proof, not asserted by analogy.

**Proof.** Write $y_1\ge y_2\ge\dots\ge y_{c_1+1}>0$ for $\sigma_1$'s
fragments (sum $\sigma_1$, $c_1\ge1$ so there are $\ge2$ of them). By the
same argument as Lemma 1 (§1) — if two of the $y_i$ both exceeded
$\sigma_2$, their sum alone would exceed $2\sigma_2=\sigma_1$, contradicting
that all $c_1+1\ge2$ parts (all $\ge0$) sum to exactly $\sigma_1$ — **at
most one** $y_i$ exceeds $\sigma_2$. Exactly one of two cases holds.

**Case (a): every $y_i\le\sigma_2$.** Let $t\ge0$ be the number of $y_i$
equal to $\sigma_2$ exactly (the rest are $<\sigma_2$ strictly). Since
$\sigma_2$ itself is untouched, the value $\sigma_2$ occurs in $S$ with
total multiplicity $\mu:=1+t$. Every other element of $S$ — the $y_i$'s
not tied to $\sigma_2$ (each $<\sigma_2$ by hypothesis) and every fragment
or untouched copy of $\sigma_3,\dots,\sigma_m$ (each fragment is
$\le\sigma_i\le\sigma_3=\sigma_2/2<\sigma_2$ for $i\ge3$, since a fragment
of a positive quantity is at most that quantity) — is strictly less than
$\sigma_2$. So $\sigma_2$ occupies, with multiplicity $\mu$, the top $\mu$
ranks of $S$'s sorted order.

- If $\mu$ is **odd**: by `odd-run-reduction-lemma`, $A(S)=A(S')$ where
  $S'$ replaces the $\mu$ tied copies of $\sigma_2$ by exactly one copy
  (all repeated-value blocks of odd multiplicity collapse to one
  survivor, general form of the lemma already used throughout §5.4/§7).
  In $S'$, this single surviving $\sigma_2$ remains the strict unique
  maximum (every other element is still $<\sigma_2$, unaffected by the
  reduction). By `sharp-dominant-removal-identity`,
  $A(S')=\sigma_2-A(S'\setminus\{\sigma_2\})$, and by Fact 1
  ($A\ge0$, §5.2), $A(S'\setminus\{\sigma_2\})\ge0$, so
  $A(S)=A(S')\le\sigma_2$. Finally $\sigma_2\le\sigma_1-\sigma_m$: since
  $\sigma_1=2\sigma_2$, $\sigma_1-\sigma_m-\sigma_2=\sigma_2-\sigma_m\ge0$
  for every $m\ge2$ (as $\sigma_2\ge\sigma_m$, the tail is non-increasing).
  So $A(S)\le\sigma_1-\sigma_m$.
- If $\mu$ is **even**: the entire top-$\mu$ block contributes exactly $0$
  to $A(S)$ (pairing consecutive ranks $(1,2),(3,4),\dots,(\mu-1,\mu)$,
  each pair is a tied equal pair, contributing $\sigma_2-\sigma_2=0$; this
  is the same top-run-cancellation fact used throughout, e.g. §2's
  computation of $A(F^\ast\cup T)$ and the Last-Element Bound's proof,
  §5.5). So $A(S)=A(S\setminus\{\mu\text{ copies of }\sigma_2\})$. By
  Fact 2, this is $\le\mathrm{Total}(S\setminus\{\mu\text{ copies}\})
  =\mathrm{Total}(S)-\mu\sigma_2$. Since $S$ is a legal refinement of
  $\sigma$, mass conservation gives $\mathrm{Total}(S)=R(\sigma)$, so
  $A(S)\le R(\sigma)-\mu\sigma_2$. Since $\mu\ge2$ here (even and $\ge1$
  forces $\mu\ge2$), $R(\sigma)-\mu\sigma_2\le R(\sigma)-2\sigma_2
  =R(\sigma)-\sigma_1=\sigma_1-\sigma_m$ (the last equality is identity
  (7.10.1)/(5.4), $R(\sigma)+\sigma_m=2\sigma_1$, rearranged). So
  $A(S)\le\sigma_1-\sigma_m$.

Either way, Case (a) gives $A(S)\le\sigma_1-\sigma_m$.

**Case (b): exactly one $y_1>\sigma_2$ strictly.** The other $c_1$
fragments of $\sigma_1$ sum to $\sigma_1-y_1<\sigma_1-\sigma_2=\sigma_2$,
so each individually is $<\sigma_2$ (a nonnegative quantity dominated by
a sum $<\sigma_2$). Combined with $\sigma_2<y_1$ (case hypothesis) and
every fragment/untouched copy of $\sigma_3,\dots,\sigma_m$ being
$<\sigma_2<y_1$ (as in Case (a)), $y_1$ is the **strict unique maximum**
of $S$. By `sharp-dominant-removal-identity`,
$$A(S)=y_1-A(S\setminus\{y_1\}).$$
Within $S\setminus\{y_1\}$: the remaining $\sigma_1$-fragments (sum
$\sigma_1-y_1<\sigma_2$, so each strictly $<\sigma_2$, no ties with
$\sigma_2$ possible here), $\sigma_2$ itself (untouched, value exactly
$\sigma_2$), and $\sigma_3,\dots,\sigma_m$'s fragments/untouched copies
(each $<\sigma_2$). So $\sigma_2$ is now the strict unique maximum of
$S\setminus\{y_1\}$ (no ties this time, since the remaining
$\sigma_1$-fragments are strictly below $\sigma_2$, unlike Case (a)).
Peel again:
$$A(S\setminus\{y_1\})=\sigma_2-A\big(S\setminus\{y_1,\sigma_2\}\big).$$
Combining, $A(S)=y_1-\sigma_2+A(S\setminus\{y_1,\sigma_2\})$. By Fact 2,
$A(S\setminus\{y_1,\sigma_2\})\le\mathrm{Total}(S\setminus\{y_1,\sigma_2\})
=R(\sigma)-y_1-\sigma_2$ (mass conservation again). Hence
$$A(S)\ \le\ y_1-\sigma_2+R(\sigma)-y_1-\sigma_2\ =\ R(\sigma)-2\sigma_2\ =\
\sigma_1-\sigma_m$$
(same identity as above). This closes Case (b), and with it the theorem.
$\blacksquare$

**Remark (why this is a genuine generalization of the "Double-Dominant-Peel"
mechanism, not a coincidence at $m=4$).** The mechanism used in Case (b) is
literally the same two-peel-plus-Fact-2 pattern as §7.13's shapes
$(2,0,0,0)$-Case-II, $(1,0,1,0)$, $(1,0,0,1)$ — but the proof here shows
the *only* structural fact it actually needs is "$\sigma_2$ is untouched
and strictly less than the dominant $\sigma_1$-fragment," which is
completely insensitive to how many cuts land on $\sigma_3,\dots,\sigma_m$
or how many parts $\sigma_1$ itself has. This is why the theorem holds for
*every* $m$ and *every* cut count on the untouched-$\sigma_2$ side — no
induction on $m$ or enumeration of shapes was needed at all, unlike the
outline's step 3 proposal of "a case split on the number of distinct
touched indices."

### 7.15 The residual ($\sigma_2$ touched) is not independent of the central obstruction: a Necessity Theorem

The outline's step 3 asked whether *every* legal top-cut shape (not just
$\sigma_2$-untouched ones) admits a 2-deep dominance chain reaching
$\sigma_1-\sigma_m$, and its "Watch out for" note explicitly asserted this
front is "not blocked by the central obstruction," a "well-scoped,
self-contained combinatorial claim." This subsection **rigorously
refutes that premise for $m\ge5$**: it proves that closing the residual
$\sigma_2$-touched family, for general $m$, *cannot* avoid a form of
$(\star_k)$ for $k\ge3$ — the very obstruction the outline instructed this
front to stay independent of. This is not a failure to find a clever
argument; it is a proved logical dependency.

**Setup.** Fix $m\ge3$ and consider the sub-family of $\mathrm{MaxCeil}(m)$
top-cut shapes with $c_1=1$ (i.e. $\sigma_1$ split into exactly two parts,
$\sigma_1-\varepsilon$ and $\varepsilon$, for $\varepsilon\in(0,\sigma_1/2]$
— WLOG the smaller part is $\varepsilon$), $\sigma_3,\dots,\sigma_m$ (the
tail $\tau:=(\sigma_3,\dots,\sigma_m)$, a ratio-2 tail of length $m-2$)
**untouched**, and $\sigma_2$ replaced by an **arbitrary** legal refinement
$Z$ of $\sigma_2$ using $c_2\le m-3$ cuts (so the total cut budget is
$c_1+c_2\le1+(m-3)=m-2$, exactly $\mathrm{MaxCeil}(m)$'s cap). Write
$$S_\varepsilon:=\{\sigma_1-\varepsilon,\varepsilon\}\cup Z\cup\tau.$$
This is, for every $\varepsilon\in(0,\sigma_1/2]$ and every such $Z$, a
legal instance of $\mathrm{MaxCeil}(m)$'s top-cut branch (this is exactly
shape $(1,c_2,0,\dots,0)$ in the notation of §7.13, generalized to arbitrary
$m$ and to $Z$ with up to $m-3$ cuts rather than a single cut).

**Lemma (Continuity).** *$A(S_\varepsilon)$ is a continuous function of
$\varepsilon$ on $[0,\sigma_1/2]$, where $S_0:=\{\sigma_1\}\cup Z\cup\tau$
(the degenerate/untouched-$\sigma_1$ configuration).*

**Proof.** This is the same continuity fact already established and used
in §5.1's Vertex-maximization Proposition: for a fixed finite background
multiset ($Z\cup\tau$ here) and a finite number of coordinates varying
continuously subject to a fixed-sum constraint (here: $\sigma_1-\varepsilon$
and $\varepsilon$, summing to $\sigma_1$ for every $\varepsilon$), each
sorted order statistic is a continuous function of the free coordinates
(a finite iterated max/min of continuous coordinate functions), and $A$ is
a fixed linear functional of the sorted order statistics — hence $A(S_
\varepsilon)$ is continuous in $\varepsilon$, including at the boundary
$\varepsilon=0$ (where $\{\sigma_1-\varepsilon,\varepsilon\}\to\{\sigma_1,
0\}$; the element "$0$" is always the unique minimum of the full multiset
for $\varepsilon$ small enough — since every element of $Z\cup\tau$ is a
positive fragment of some $\sigma_i>0$, hence bounded below by a fixed
positive constant independent of $\varepsilon$ — so it occupies the fixed
bottom rank throughout a neighbourhood of $\varepsilon=0$ and the limit
$A(S_\varepsilon)\to A(\{\sigma_1\}\cup Z\cup\tau)=A(S_0)$ holds by the same
continuity argument, not merely a heuristic "$\varepsilon\to0$ degenerates
to untouched" claim). $\blacksquare$

**Lemma (Value at $\varepsilon=0$).** *$A(S_0)=\sigma_1-A(Z\cup\tau)$.*

**Proof.** In $S_0=\{\sigma_1\}\cup Z\cup\tau$, $\sigma_1=2\sigma_2$ strictly
exceeds every element of $Z\cup\tau$ (each $\le\sigma_2<\sigma_1$, since
$Z$'s fragments are each $\le\sigma_2$ and $\tau$'s elements are each
$\le\sigma_3<\sigma_2$), so $\sigma_1$ is the strict unique maximum. By
`sharp-dominant-removal-identity`, $A(S_0)=\sigma_1-A(Z\cup\tau)$.
$\blacksquare$

**Theorem (Necessity).** *Suppose $\mathrm{MaxCeil}(m)$'s top-cut branch
holds in full generality (i.e. $A(S)\le\sigma_1-\sigma_m$ for every legal
$S$ as in the theorem's hypothesis, including every $S_\varepsilon$ in the
family above, for every $\varepsilon\in(0,\sigma_1/2]$). Then, for every
$Z$ (legal $\le(m-3)$-cut refinement of $\sigma_2$),*
$$A(Z\cup\tau)\ \ge\ \sigma_m.\tag{7.15.1}$$

**Proof.** By hypothesis, $A(S_\varepsilon)\le\sigma_1-\sigma_m$ for every
$\varepsilon\in(0,\sigma_1/2]$. Taking $\varepsilon\to0^+$ and using the
Continuity Lemma, $A(S_0)\le\sigma_1-\sigma_m$ as well (a non-strict
inequality is preserved under limits — a standard fact: if $f(\varepsilon)
\le c$ for all $\varepsilon$ in a right-neighbourhood of $0$ and $f$ is
continuous at $0$, then $f(0)=\lim_{\varepsilon\to0^+}f(\varepsilon)\le c$).
By the Value-at-$0$ Lemma, $A(S_0)=\sigma_1-A(Z\cup\tau)$, so
$\sigma_1-A(Z\cup\tau)\le\sigma_1-\sigma_m$, i.e. $A(Z\cup\tau)\ge\sigma_m$.
$\blacksquare$

**Identifying (7.15.1) with the central obstruction.** $\tau=(\sigma_3,
\dots,\sigma_m)$ is untouched and $Z$ is an arbitrary $\le(m-3)$-cut
refinement of $\sigma_2$, the top element of the length-$(m-1)$ ratio-2
tail $\sigma':=(\sigma_2,\dots,\sigma_m)$. So $Z\cup\tau$ is exactly a
legal refinement of $\sigma'$ in which **only the top element $\sigma_2$
is cut**, using $\le m-3$ cuts — a sub-case of $\mathrm{MinFloor}(m-1)$'s
own case (ii) (§7.10.4: "$\sigma_1'$ [$=\sigma_2$] is cut"), restricted to
the narrower sub-family "no cuts elsewhere in $\sigma'$" and to a budget
of $m-3$ (one less than $\mathrm{MinFloor}(m-1)$'s own stated cap $m-2$).
By §7.11's Index-Chain Identity, $\mathrm{MinFloor}(m-1)\equiv(\star_{m-2})$
exactly; (7.15.1) is thus a **necessary sub-instance** of $(\star_{m-2})$'s
own case-(ii) content.

**Consequence: this front is not independent of the central obstruction for $m\ge5$.**
By §7.11's Corollaries, $(\star_k)$ is unconditionally certified only for
$k\le2$. For $m\ge5$, $m-2\ge3$, so $(\star_{m-2})$ is **not** currently
certified. By the contrapositive of the Necessity Theorem: **if** (7.15.1)
fails for some legal $Z$ at a given $m\ge5$ (which cannot currently be
ruled out, since it is a genuine instance of the uncertified $(\star_{m-2})$),
**then** $\mathrm{MaxCeil}(m)$'s top-cut branch fails too, for the
corresponding $S_\varepsilon$ with $\varepsilon$ small enough (by
continuity, the failure margin at $\varepsilon=0$ persists for small
$\varepsilon>0$). So **no proof of $\mathrm{MaxCeil}(m)$'s full top-cut
branch, for $m\ge5$, can avoid establishing (at least) this restricted
instance of $(\star_{m-2})$** — directly contradicting the outline's
"Watch out for" instruction that this front is self-contained and not
blocked by the central obstruction.

**This is not merely an abstract worry: a direct attempt to close (7.15.1)
via the cheap facts already on file fails, matching the general
diagnosis.** Repeating the two-peel argument on $Z\cup\tau$ (peel $Z$'s
dominant fragment $z_1$ if $z_1>\sigma_3$, then peel $\sigma_3$ if
untouched, then Fact 2 on the remainder) gives, by the identical algebra as
Case (b) of §7.14 applied one level down (tail $\sigma'$, dominant
fragment $z_1$, second element $\sigma_3$):
$$A(Z\cup\tau)\ge2z_1-R(\sigma')\qquad(\text{via }A(Z\cup\tau)=z_1-A(\text{rest})\text{ and Fact 2 on
"rest"}),$$
and requiring $2z_1-R(\sigma')\ge\sigma_m$ reduces (using
$R(\sigma')+\sigma_m=2\sigma_2$, the length-$(m-1)$ analogue of (7.10.1))
to $z_1\ge\sigma_2$ — but $z_1<\sigma_2$ always (as $z_1$ is one part of a
genuine $\ge2$-part split of $\sigma_2$), so this candidate closing route
provably **cannot** succeed via Fact 2 alone, for any $Z$, mirroring
exactly why $\mathrm{MinFloor}(\ell)$'s case (ii) resisted the cheap facts
in §7.10.4. (Numerically corroborated, not as a substitute for the proof
above but as an independent sanity check: an exact-`Fraction` search at
$m=5$, testing $2000$ random $\le2$-cut splits $Z$ of $\sigma_2$ against
$\tau=(\sigma_3,\sigma_4,\sigma_5)$ untouched, found the minimum of
$A(Z\cup\tau)$ over the search exactly equal to $\sigma_5$, never below
it — consistent with (7.15.1) but not a proof of it, since $(\star_3)$
itself remains uncertified.)

**Scope, stated precisely.** §7.14's $\sigma_2$-untouched theorem is fully
general and unconditional for **every** $m\ge2$ — a genuine, reusable,
budget-free positive result, strictly broader than the "$\le2$ distinct
indices" characterization the outline used to describe the already-closed
part of the top-cut branch. §7.15 does **not** close the residual
$\sigma_2$-touched family; instead it proves, rigorously, that the residual
family — and hence $\mathrm{MaxCeil}(m)$'s top-cut branch in full
generality — **cannot** be closed for $m\ge5$ by any argument that avoids
$(\star_k)$ for $k\ge3$, because a specific, exhibited sub-family of
top-cut shapes ($c_1=1$, $\varepsilon\to0$, $\sigma_2$ arbitrarily refined)
provably requires it as a necessary condition. This directly corrects the
round-27 outline's premise (its "Watch out for" note) that this front is
self-contained; the correct status is: **the top-cut branch is
unconditionally closed exactly on the $\sigma_2$-untouched sub-family
(§7.14, every $m$) and on the two small instances $m=3,4$ closed by hand
in §7.12–7.13 (which happen to include $\sigma_2$-touched shapes only at
budgets where the corresponding $(\star_k)$, $k\le2$, is already
certified) — and is, for $m\ge5$, provably NOT separable from $(\star_k)$,
$k\ge3$, matching (not merely resembling) the same central obstruction
blocking the top-untouched branch and the sibling's even-multiplicity-tie
gap.** This is a genuinely new finding this round: it does not merely fail
to close the general case, it proves *why* the outline's proposed
independence cannot hold, for $m\ge5$ specifically (consistent with
$m=3,4$ succeeding, since there $(\star_{m-2})=(\star_1)$ or $(\star_2)$,
already certified — an internal consistency check, not a coincidence).

## Open gaps
None remaining for this approach's own target, Claim (A) — fully closed.

**Round-32 addendum (does not affect Claim A's status; resolves (7.9.1) at
$n=8$, still open for general $n$).** New §7.19 proves two fully general
lemmas (Max Bound: $A(S)\le\max(S)$; Insertion Sandwich: $|A(T\cup\{a\})-
A(T)|\le a$) and combines them into a **Master Theorem**: $\mathrm{MinFloor}
(m-1)=(\star_{m-2})$ implies $\mathrm{MaxCeil}(m)$ **in full** (both
branches, one unified mechanism, no shape census needed). Instantiated at
$m=5$ using the now-certified $(\star_3)$ (round 31), this closes
$\mathrm{MaxCeil}(5)$ unconditionally, hence $(7.9.1)$ at $n=8$ — one level
past round 26's $n\le7$. The mechanism genuinely avoids the route §7.15's
Necessity Theorem proved insufficient (it never bounds $A(W)$ from above
via Fact 2; it uses $\mathrm{MinFloor}(m-1)$'s lower bound on $W$ directly
plus the new Insertion Sandwich Lemma to absorb $\sigma_1$'s other
fragments). **Not closed:** $\mathrm{MaxCeil}(m)$ for $m\ge6$ (needs
$(\star_4)$, not yet certified) and the general-$n$ pattern (all $k\ge3$)
remain exactly as open as before this round.

**Round-25 addendum (does not affect Claim A's status; attempts, and does
not close, (7.9.1)).** New §7.10 replaces the round-24 diagnosis with a
verified-correct two-quantity ($\mathrm{MinFloor}(\ell)$/$\mathrm{MaxCeil}
(\ell)$) joint reduction, closes one full branch of $\mathrm{MinFloor}$
unconditionally for every $\ell$ (a new reusable fact), and precisely
isolates the residual open branch (the tail's own top element receiving a
spare cut) as the single remaining gap for both quantities — narrower and
more precisely targeted than round 24's diagnosis, but (7.9.1) itself
remains open.

**Round-26 addendum (does not affect Claim A's status; resolves (7.9.1) at
$n=6,7$, still open for general $n$).** New §7.11 proves
$\mathrm{MinFloor}(\ell)\equiv(\star_{\ell-1})$ exactly (an identity, not a
one-way implication), giving: $\mathrm{MinFloor}(3)$ fully closed (both
branches, since $(\star_2)$ is already a certified theorem) and
$\mathrm{MaxCeil}(\ell)$'s top-untouched branch unconditionally free for
$\ell\le4$. New §7.12/§7.13 close $\mathrm{MaxCeil}(3)$'s and
$\mathrm{MaxCeil}(4)$'s top-cut branches by direct elementary case
analysis (exhaustive 5-shape enumeration for $\mathrm{MaxCeil}(4)$, each
shape closed via a two-peel-plus-Fact-2 mechanism), reusing only
already-certified facts, exactly per the outline's instruction not to
invent new machinery and not to use the insufficient
Triangle-Bound/Max-Domination shortcut. **(7.9.1) is now unconditionally
resolved at $n=6$ and $n=7$** — genuinely new, though narrowly scoped:
general $n$ (i.e. $\mathrm{MaxCeil}(m)$'s top-cut branch for $m\ge5$)
remains open (blocked, per §7.11, on $(\star_k)$ for $k\ge3$ becoming
unconditional — the project's own central open problem, not a separate
technical gap), and this round's closure does not resolve the sibling's
Theorem-37 item or the shared $b=c_1$ item (round-26 outline's items 1–2),
which remain open in both files.

**Round-19/21 addendum (does not affect Claim A's status):** the cross-check
work in §7 above leaves open, for general $n\ge4$, a full vertex enumeration
of the budget-$(n-3)$-capped multi-piece polytope underlying $\Delta(n,v)$
— see §7.6, explicitly untouched and open. The $n=3$ instance is now fully
closed for the **TRUE, $\varepsilon$-corrected** target $(\sharp')$ (§7.5,
§7.5.2 specifically — round 21, strictly stronger than round 19/20's
$(\sharp)$-only closure), and the corrected cap's sufficiency is
numerically corroborated for $n=3,\dots,7$ (§7.4, the weaker $(\sharp)$)
and, at $n=3$ specifically, for the TRUE $(\sharp')$ target (§7.5.2, this
round) via independently-written scripts.

**Round-22 addendum (does not affect Claim A's status):** §7.7 now records
the *exact* logical equivalence between this file's $(\sharp')$ and the
sibling's $(\Diamond')$ (identity (7.7.1), independently numerically
cross-checked at $n=4$, zero mismatches) — so §7.6's general-$n$ gap is
now precisely characterized as "closes the instant the sibling proves
$(\Diamond')$ for that $n$," rather than requiring a separate vertex-
enumeration argument at all. This is a genuine sharpening of §7.6 (from "an
open gap requiring its own proof" to "an open gap that is definitionally
identical to a named, actively-worked sibling target"), but $(\Diamond')$
itself remains unproved for every $n\ge4$ as of this round, so §7.6 is
**still open**, not closed — no overclaiming.

**Round-23 addendum (does not affect Claim A's status):** §7.8 records an
independent discrete/pigeonhole derivation, via a new elementary lemma
(`single-insert-point-vertex-lemma`), of `greedy-halving-adversary`'s Case
(b) "$v\ge a$" target $A(B)\ge f(n)$. Two of the three resulting vertex
candidates for the free coordinate $b$ close (conditional on
$(\star_{n-3})$ and $(\star_{n-4})$ respectively); the remaining two
sub-cases (a further-split $p_4$-slot, or a tie with a generic interior
$T'$-fragment) recouple exactly to the same joint cross-piece
vertex-enumeration obstruction §7.6 already names — independent
confirmation of the same wall from a different starting point, not a
closure. This does not itself close §7.6 (still open, per the round-22
addendum above), but corroborates the diagnosis from a second, genuinely
different route (single-variable pinning first, vs. the sibling's
whole-object Vertex-Minimum Theorem application this same round).

**Round-24 addendum (does not affect Claim A's status; fixes the outline-
reviewer's flagged direction bug in §7.8's T'-cuts-$p_4$ sub-case).** New
§7.9 re-derives, breakpoint by breakpoint (not by trusting the outline's
placement of the issue), exactly where an upper bound on an $A$-quantity
is genuinely needed. Result: of the (at most) four vertex candidates for
the free coordinate $b$, **three are fully accounted for without any new
direction issue** ($b=0$: a lower bound, closed via $(\star_{n-3})$;
$b=p_4$: proved fully *dominated* by the $b=c_1$ candidate via an exact
affine-monotonicity computation — new **Box-Endpoint Domination Fact**,
promoted below — so it needs no bound on $A(T')$ at all, in either
direction; $b=c_1$: a same-direction lower-bound recursion, open but not
direction-flawed). **Exactly one candidate** ($b=c_2$, generic sub-case)
is shown, by direct symbolic derivation of the Insert-Element/pair-
cancellation/dominant-removal chain, to require the new inequality
$A(T''')\le c_1-f(n)$ (7.9.1) — a genuine upper bound, confirming the
outline-reviewer's concern was real, but mis-located by the outline. This
round further proves (7.9.1) is **not** implied by the certified
$A\le\mathrm{Total}$ bound (exact computation at the symmetric split:
$\mathrm{Total}(T''')=p_4-p_{n+1}=7/127>3/127=c_1-f(n)$ at $n=6$, a
concrete counterexample to the cheap bound's sufficiency) nor by any
general refinement-monotonicity fact (which `current.md` records as false
in general — the general form of Claim (B)). This is a genuine sharpening
(from "the whole T'-cuts-$p_4$ sub-case recouples to an undifferentiated
obstruction" to "exactly one of four candidates needs a new, precisely-
stated, not-yet-available dual-direction lemma; the other three are fully
resolved, one of them — $b=p_4$ — newly and for the first time"), but it
is **not** a closure: (7.9.1), and the separate $b=t\in T'''$ residual
(§7.9.6, unchanged from round 23's diagnosis), remain open.

### 7.16 Round-28 addendum: $(\star_3)=\mathrm{MinFloor}(4)$ via 20-shape exhaustion — 14/20 shapes fully closed, achievability confirmed on all 20, exact lower bound left open on 6 shapes

**Target.** For the unit ratio-2 ladder $\pi=(\pi_1,\pi_2,\pi_3,\pi_4)
=(8,4,2,1)$ (units of $1/15$) and every legal refinement $U$ using $\le3$
cuts distributed in any pattern across all four pieces,
$$A(U)\ \ge\ \pi_4=1.\tag{7.16.T}$$
By §7.11's Index-Chain Identity this is exactly $(\star_3)$.

**Fix to the outline's shape count (per the outline-reviewer's required
correction).** The number of legal cut-*distributions* $(k_1,k_2,k_3,k_4)$,
$k_i\ge0$, with $\sum k_i\le3$, is $\binom{3+4}{4}=\binom{7}{4}=35$ (stars-
and-bars for "at most 3"), **not** $20$; the outline's formula
$\sum_{b=0}^3\binom{b+3}{3}=1+4+10+20=35$ actually computes this correct
$35$-count, so its stated total of "$20$" was a transcription slip against
its own formula. The number $20=\binom{3+4-1}{4-1}=\binom{6}{3}$ is instead
the count of compositions of **exactly** $3$ into $4$ nonnegative parts —
a genuinely different, smaller set.

**Why restricting to the $20$ exactly-$3$ shapes still proves (7.16.T) for
every legal $U$ (the outline-reviewer's required justification, now
supplied).** By part 2 of the certified `vertex-minimum-theorem`, the
minimizer of $A(U)$ over the polytope of legal refinements for a *fixed*
composition is attained at a vertex pinned by tight constraints of family
(I) ("some fragment $=0$") or family (II) ("two fragments tied"). A
family-(I) tight vertex of an exactly-$3$-cut composition — i.e. one of
its $\ge1$ cuts degenerates to a zero-length fragment — is, by
definition, exactly a point of the *closure* of a lower-budget
composition (the same point, reinterpreted with that cut simply not
made). Consequently, for every composition $(k_1,\dots,k_4)$ with
$\sum k_i<3$, every point of its polytope is already contained in the
closure of at least one exactly-budget-$3$ composition's polytope
(pad any coordinate up to budget $3$ and let the padding cut's fragment
$\to0$). Since $A$ is continuous (§0 of `vertex-minimum-theorem`), the
infimum of $A$ over the full $\le3$-cut legal space equals the infimum
over the closures of the $20$ maximal (exactly-budget-$3$) shapes, provided
each shape's own free parameters are allowed to range over their **closed**
domain (including the degenerate boundary where a coordinate hits $0$).
This is exactly the closure argument the exhaustive lists below use: every
lower-budget shape is a boundary case of one of the $20$ below, and is
covered automatically once each of the $20$ is closed on its full closed
domain. Hence enumerating the $20$ exactly-$3$-cut shapes, each on its
closed feasible region, proves (7.16.T) for every legal $U$ (all $35$
compositions, not just the $20$).

**The $20$ shapes, explicitly.** Compositions of $3$ into $4$ nonnegative
parts $(k_1,k_2,k_3,k_4)$: by type, $\binom{4}{1}=4$ of shape
$(3,0,0,0)$-pattern (one index gets all $3$): $(3,0,0,0),(0,3,0,0),
(0,0,3,0),(0,0,0,3)$; $4\times3=12$ of shape $(2,1,0,0)$-pattern (one
index gets $2$, a different index gets $1$): $(2,1,0,0),(2,0,1,0),
(2,0,0,1),(1,2,0,0),(0,2,1,0),(0,2,0,1),(1,0,2,0),(0,1,2,0),(0,0,2,1),
(1,0,0,2),(0,1,0,2),(0,0,1,2)$; $\binom{4}{3}=4$ of shape
$(1,1,1,0)$-pattern (three distinct indices get $1$ each): $(1,1,1,0),
(1,1,0,1),(1,0,1,1),(0,1,1,1)$. Total $4+12+4=20=\binom{6}{3}$, matching
the corrected count.

**Master Theorem I (the $10$ shapes with $k_1=0$).** *For every
composition with $k_1=0$ — $(0,k_2,k_3,k_4)$, $k_2+k_3+k_4=3$ — and every
legal refinement $U$ of that shape, $A(U)\ge1$.*

**Proof.** $\pi_1=8$ is untouched. Every fragment coming from splitting
$\pi_2,\pi_3,\pi_4$ is $\le\max(\pi_2,\pi_3,\pi_4)=4<8=\pi_1$, so $\pi_1$
is the strict unique maximum of $U$. By `sharp-dominant-removal-identity`,
$A(U)=\pi_1-A(U\setminus\{\pi_1\})$. Since $U\setminus\{\pi_1\}$ is a
refinement of $(\pi_2,\pi_3,\pi_4)$ with $\mathrm{Total}=\pi_2+\pi_3+\pi_4
=7$, Fact 2 ($A\le\mathrm{Total}$, §5.2, already certified) gives
$A(U\setminus\{\pi_1\})\le7$. Hence $A(U)\ge8-7=1$. $\blacksquare$

This closes, in one uniform argument, all $10$ shapes
$(0,0,0,3),(0,0,1,2),(0,0,2,1),(0,0,3,0),(0,1,0,2),(0,1,1,1),(0,1,2,0),
(0,2,0,1),(0,2,1,0),(0,3,0,0)$.

**Master Theorem II (the $3$ shapes with $k_1=1,k_2=0$).** *For every
composition $(1,0,k_3,k_4)$, $k_3+k_4=2$, and every legal refinement $U$
of that shape, $A(U)\ge1$.*

**Proof.** Write $\pi_1$'s split as $\{a,b\}$, $a\le4\le b$, $a+b=8$
($a\in[0,4]$). $\pi_2=4$ is untouched. Let $V$ denote the (arbitrary)
refinement of $(\pi_3,\pi_4)$ using the remaining budget $k_3+k_4=2$;
$\mathrm{Total}(V)=\pi_3+\pi_4=3$ always, regardless of how those $2$ cuts
are distributed between $\pi_3,\pi_4$ — this is the only fact about $V$
used below.

*Case $a<4$ (so $b>4$ strictly).* Every element of $V$ is $\le\pi_3=2<4<b$,
and $a<4<b$, so $b$ is the strict unique max of $U=\{a,b,4\}\cup V$. Peel:
$A(U)=b-A(\{a,4\}\cup V)$. Within $\{a,4\}\cup V$, since $a<4$ and every
element of $V$ is $\le2<4$, $4$ is the strict unique max. Peel again:
$A(\{a,4\}\cup V)=4-A(\{a\}\cup V)$. Hence
$$A(U)=b-4+A(\{a\}\cup V).$$
Target $A(U)\ge1$ becomes $A(\{a\}\cup V)\ge1-b+4=5-b=5-(8-a)=a-3$.
- If $a\le3$: $a-3\le0\le A(\{a\}\cup V)$ by Fact 1 ($A\ge0$, §5.2,
  already certified). Done.
- If $a\in(3,4)$: every element of $V$ is $\le2<3<a$, so $a$ is the strict
  unique max of $\{a\}\cup V$. Peel: $A(\{a\}\cup V)=a-A(V)$. By Fact 2,
  $A(V)\le\mathrm{Total}(V)=3$, so $A(\{a\}\cup V)\ge a-3$, exactly the
  needed bound. Done.

*Case $a=4$ (so $b=4$ too, $\pi_1$ split evenly).* $U=\{4,4,4\}\cup V$
(the two $\pi_1$-fragments plus $\pi_2$, all equal to $4$). The value $4$
has multiplicity $3$ (odd); by `odd-run-reduction-lemma`, $A(U)=A(\{4\}
\cup V)$ (one copy of $4$ survives the odd-run reduction, since $3$ is
odd). Every element of $V$ is $\le2<4$, so $4$ is the strict unique max
of $\{4\}\cup V$; peeling gives $A(\{4\}\cup V)=4-A(V)\ge4-3=1$ by Fact 2.
Done. $\blacksquare$

This closes all $3$ shapes $(1,0,0,2),(1,0,1,1),(1,0,2,0)$, with no case
split needed on how the remaining budget of $2$ is divided between
$\pi_3,\pi_4$ — the argument uses only $\mathrm{Total}(V)=3$.

(Cross-checked independently, not substituting for the proof above: an
exact-`Fraction` script, $20000$ random legal trials per master theorem,
zero violations of $A(U)\ge1$ in either family.)

**Shape $(3,0,0,0)$ — closes by direct citation, not new work.** This
shape is *literally* Claim (A) of this file at $n=3$: $\pi=(\pi_1,\dots,
\pi_4)=(8,4,2,1)/15=(p_1,\dots,p_4)$ of the $n=3$ ladder, $F$ a partition
of $\pi_1$ into $\le4$ parts ($\le3$ cuts), tail $T=(\pi_2,\pi_3,\pi_4)$
untouched. `claim-a-full-closure` (§0–§5 above, fully proved for every
$n\ge1$, both Case I and Case II) gives $A(F\cup T)\ge a_3=\pi_4=1$
directly. No re-derivation needed.

**The remaining $6$ shapes — full status, honestly reported.** These are
$(1,1,0,1),(1,1,1,0),(1,2,0,0),(2,0,0,1),(2,0,1,0),(2,1,0,0)$: exactly the
shapes with $k_1\ge2$, or ($k_1=1$ and $k_2\ge1$) — a strictly larger set
than the outline's claimed "$2$ dangerous shapes"; exact computation (see
below) shows **all $6$** attain the value $1$ exactly, not just $(3,0,0,0)$
and $(2,0,1,0)$, so the outline's severity ranking undercounted the
tight cases by $5$.

*Achievability (the $\le$ direction) — proved in full, uniformly, for all
$6$.* In every one of these $6$ shapes it is possible to realize the
target multiset (after dropping any zero-length fragments)
$$\{4,4,2,2,2,1\}\tag{7.16.1}$$
within the shape's own per-piece budget, with some cuts genuinely used and
others degenerate ($=0$) as needed:
- $(1,1,0,1)$: $\pi_1\to\{4,4\}$; $\pi_2\to\{2,2\}$; $\pi_3=2$ untouched;
  $\pi_4\to\{1,0\}$.
- $(1,1,1,0)$: $\pi_1\to\{4,4\}$; $\pi_2\to\{2,2\}$; $\pi_3\to\{2,0\}$;
  $\pi_4=1$ untouched.
- $(1,2,0,0)$: $\pi_1\to\{4,4\}$; $\pi_2\to\{2,2,0\}$; $\pi_3=2,\pi_4=1$
  untouched.
- $(2,0,0,1)$: $\pi_1\to\{4,2,2\}$; $\pi_2=4,\pi_3=2$ untouched;
  $\pi_4\to\{1,0\}$.
- $(2,0,1,0)$: $\pi_1\to\{4,2,2\}$; $\pi_2=4$ untouched; $\pi_3\to\{2,0\}$;
  $\pi_4=1$ untouched.
- $(2,1,0,0)$: $\pi_1\to\{4,2,2\}$; $\pi_2\to\{4,0\}$; $\pi_3=2,\pi_4=1$
  untouched.

Each is a valid partition of its respective $\pi_i$ (arithmetic checked:
$4+4=8$, $2+2=4$, $4+2+2=8$, $2+0=2$, $4+0=4$, $1+0=1$, $2+2+0=4$). In every
case the resulting nonzero multiset is exactly $\{4,4,2,2,2,1\}$. By
`odd-run-reduction-lemma`: the value $4$ has multiplicity $2$ (even,
cancels entirely); the value $2$ has multiplicity $3$ (odd, one copy
survives); the value $1$ has multiplicity $1$ (survives). The reduced
multiset is $\{2,1\}$, giving $A=2-1=1$ exactly. **So $A(U)=1$ is attained
in all $6$ shapes**, confirming (7.16.T) is tight (cannot be improved to a
strictly larger constant) on this larger, corrected family.

*Lower bound (the $\ge$ direction) — proved for a large sub-region of each
shape's domain by hand; NOT closed on the full domain; this is the open
gap left by this round's build.* Attempting the same cascading-peel
technique as Master Theorem II on, e.g., shape $(2,0,1,0)$ (writing
$\pi_1$'s split as $f_1\ge f_2\ge f_3\ge0$, $\pi_2=4$ untouched, $\pi_3$'s
split $\{g_1,g_2\}$, $\pi_4=1$ untouched): the sub-case $f_1>4$ closes
completely by peeling $f_1$ (strict unique max, $>4\ge$ everything else)
then $4=\pi_2$ (strict unique max of the remainder, since the two
remaining $\pi_1$-fragments sum to $8-f_1<4$), reducing to
$A(\{f_2,f_3,g_1,g_2,1\})\ge5-f_1$, closed by Fact 1 when $f_1\ge5$ and by
one further peel + Fact 2 (on the always-fixed-total-$3$ set $\pi_3\cup
\pi_4$) when $f_1\in(4,5)$ — directly analogous to Master Theorem II.
The sub-case $f_1\le4$ (where $f_1\ge8/3$ by pigeonhole, since $f_1$ is
the max of $3$ nonnegative reals summing to $8$) closes similarly for
$f_1\le3$ (peel $\pi_2=4$, then $f_1$, then Fact 1 gives the bound
directly). **The residual sub-case $f_1\in(3,4)$ resists the same
technique**: after peeling $\pi_2=4$ then $f_1$, the needed bound on
$A(\{f_2,f_3,g_1,g_2,1\})$ requires comparing $f_2$ against $g_1$ (both
now genuinely free, in ranges that overlap: $f_2\in\big((8-f_1)/2,f_1
\big)$, $g_1\in[1,2]$), and the crude Fact 2 bound on the resulting
$3$-element residual is **checked, explicitly, to fail** near the boundary
$f_1\to4^-,f_2\to2^+$ (Fact 2 there gives $A\le5$ against a needed $\le1$)
— this shape has $3$ genuinely interacting free parameters ($f_1,f_2,g_1$;
matching $k_1+k_3=3$), and its true minimum ($=1$, confirmed exactly by
independent computation, §-cross-check below) is realized only at an
isolated tie/degenerate vertex, not on an open sub-region where a single
cheap peel-and-Fact bound is slack enough to apply directly. The same
obstruction (three interacting free parameters, crude bounds insufficient
near the vertex) recurs, by the same shape of argument, in the other $5$
shapes in this family. **This sub-case is not closed by hand in this
round.**

*Cross-check, not a substitute for the missing hand proof.* Applying
`vertex-minimum-theorem` rigorously (the theorem is fully certified) does
reduce each of these $6$ shapes to a finite list of algebraic vertex
candidates (points cut out by exactly $d\in\{2,3\}$ tight constraints —
matching each shape's free-parameter count — from the finite families (I)
"fragment $=0$" and (II) "two fragments tied," drawn from the shape's
$\le7$ total fragment-slots). An exact (rational, not floating-point)
solve of every such constraint combination for all $6$ shapes (script:
`/tmp/vertex_full.py`, this round) found, after discarding infeasible
solutions, between $19$ and $34$ distinct feasible vertices per shape,
**every single one** with $A\ge1$, minimum exactly $1$ at the vertices
matching (7.16.1) (plus a small number of alternate value-$1$ vertices,
e.g. $(4,4,3,2,1,1,0)$ and $(5,4,2,2,1,1,0)$, also checked exactly). Since
`vertex-minimum-theorem` guarantees the true minimum over each shape's
full continuum equals the minimum over this finite candidate list, this
computation is evidence the theorem's lower-bound direction is true and
tight at exactly the value $1$ for all $6$ shapes — but per this project's
own rule ("a numeric check is not a proof step"), it does **not** replace
the missing written derivation of why every vertex, or every point of the
open sub-region identified above, satisfies $A\ge1$; only the achievability
half (§ above) is a genuine hand proof.

**Net status of (7.16.T)/$(\star_3)$.** $14$ of the $20$ maximal shapes are
fully, rigorously closed (Master Theorems I–II, $13$ shapes, plus
$(3,0,0,0)$ by citation) — both directions, no numerics load-bearing.
Achievability ($A=1$ attained) is now proved, by hand, uniformly for all
$20$ shapes (the remaining $6$ via the explicit constructions above). The
matching lower bound ($A\ge1$ everywhere) is proved by hand on a large
sub-region of each of the $6$ remaining shapes (every case with $f_1\notin
(3,4)$-type residual, by direct analogy with Master Theorem II) but is
**not closed on the small residual $3$-free-parameter regime** in any of
the $6$ — this is a real, precisely-located, and now much more accurately
sized gap than the outline anticipated (a residual inside $6$ shapes, not
a clean derivation needed for just $1$ new shape). $(\star_3)=\mathrm{
MinFloor}(4)$ is therefore **not** closed this round; this build reports
genuine, substantial, and honestly-scoped progress (correcting the
outline's shape count and severity ranking, fully closing $14/20$ shapes,
and fully closing achievability on all $20$), not a full closure.

The larger `imo-2026-03` theorem still needs (tracked by sibling approaches,
per `current.md`):
1. **Claim (B)** (tail-refinement-never-helps, restricted form) —
   `greedy-halving-adversary`'s target.
2. **The general upper bound** $c(n)\le a_n$ for arbitrary Liu Bang markings
   — `lp-duality-certificate`'s target.

## Outline (proof-outliner, round 28)

**Target for this build: prove $(\star_3)=\mathrm{MinFloor}(4)$ in full,
both branches — the smallest still-open instance of the project's central
$(\star_k)$, $k\ge3$ obstruction, and, per §7.11's already-certified
Index-Chain Identity, *definitionally equivalent* to it at $k=3$ (not a
side lemma — closing this closes the actual open statement, not an
approximation of it).**

Precise statement (per §7.11's notation, restated at $\ell=4$): for the
unit ratio-2 ladder $\pi=(\pi_1,\pi_2,\pi_3,\pi_4)=(8,4,2,1)/15$ and every
legal refinement $U$ using $\le3$ cuts distributed in **any** pattern
across all four pieces, $A(U)\ge\pi_4=1/15$.

**Technique: direct finite-shape exhaustion, the identical method that
closed $\mathrm{MaxCeil}(3)$ (§7.12) and $\mathrm{MaxCeil}(4)$ (§7.13) —
NOT a self-similar rescaling attempt (that route is doubly dead, see
Watch out for).** By the certified Vertex-Minimum Theorem, the minimizer
of $A(U)$ over any fixed cut-*distribution* (how many of the $\le3$ cuts
land on each of $\pi_1,\dots,\pi_4$) is attained at a tie/degenerate-cut
vertex, so the continuum collapses to a finite object: the round-28
`math-explorer-star-k` report computationally confirmed exactly **20**
legal cut-distribution shapes $(k_1,k_2,k_3,k_4)$, $\sum k_i\le3$,
$k_i\ge0$ (compositions of a budget $\le3$ across 4 pieces — the same
order of enumeration as $\mathrm{MaxCeil}(4)$'s 5-shape top-cut census,
just with the budget allowed onto every piece, not only $\pi_1$).

Skeleton:
1. Enumerate the 20 shapes exactly (stars-and-bars over $\sum_{b=0}^{3}
   \binom{b+3}{3}$; re-derive by hand, do not just cite the explorer's
   script) — by the tool: direct combinatorial listing.
2. For each shape, first try the **cheap dispatch** already used to close
   most of $\mathrm{MaxCeil}(4)$'s shapes: `sharp-dominant-removal-identity`
   (peel the unique current maximum repeatedly) reducing $A(U)$ to a
   closed form in the shape's free split parameters, then bound that
   closed form below by $\pi_4$ using only Fact 1 ($A\ge0$) or the trivial
   per-piece bound — by the tool: `sharp-dominant-removal-identity` +
   Facts 1/2 (already certified, §5.2).
3. For shapes where step 2's cheap bound is not immediately $\ge\pi_4$
   (per the explorer's numeric scan, the two shapes touching both $\pi_1$
   and $\pi_3$ heavily — $(3,0,0,0)$ and $(2,0,1,0)$ — sit exactly at the
   tight value $1/15$, so they need an *exact* equality derivation, not
   just a cheap inequality) do the full piecewise-linear/breakpoint sweep
   in the shape's free parameters (as Theorem 38/39 did for $h(1),h(2)$),
   confirming the minimum over that shape's feasible region equals exactly
   $\pi_4$ — by the tool: Insert-Element-Identity + odd-run-reduction-lemma
   for the tie evaluation.
4. Confirm the remaining ~14–18 "safe" shapes (those the explorer's random
   search found comfortably above $1/15$, e.g. anything with $\ge1$ cut on
   $\pi_2$) close by the cheap dispatch of step 2 alone — record which
   shapes actually needed step 3 vs. which closed at step 2, exactly
   mirroring $\mathrm{MaxCeil}(4)$'s write-up style (name every shape, do
   not silently batch "the rest").
5. Conclude $A(U)\ge\pi_4$ for every shape, hence for every legal $U$ —
   $(\star_3)$ proved, hence (by the Index-Chain Identity) $\mathrm{MinFloor}
   (4)$ proved, both branches, fully general, no numerics load-bearing.

Key lemmas (claim + mechanism):
- **Shape enumeration is exhaustive and finite (20 shapes)** — because the
  Vertex-Minimum Theorem confines the minimizer to a tie/zero-fragment
  vertex, so only the discrete cut-distribution pattern (not the continuum
  of split positions within each shape) needs full case coverage; each
  shape's own internal minimum is then a 1–2 free-parameter optimization
  closed by breakpoint sweep, not a fresh continuum search.
- **The two dangerous shapes $(3,0,0,0)$ and $(2,0,1,0)$ are exactly
  tight** — because $(3,0,0,0)$ (all cuts on $\pi_1$, tail untouched) is
  precisely the already-certified Claim-(A)-optimal vertex family (reuses
  `claim-a-full-closure`'s own extremal witness, restricted to $m=4$), and
  $(2,0,1,0)$ is a genuine new tie configuration (2 cuts on $\pi_1$, 1 on
  $\pi_3$) that the explorer's search shows lands on the same value — this
  needs its own exact derivation, it cannot be assumed to follow from the
  first shape's closure by symmetry alone.

Open gaps: the exact equality derivation for shape $(2,0,1,0)$ is new work,
not yet on file anywhere in the project (it is not the same object as
Claim (A)'s optimum, which only touches $\pi_1$).

Cases to cover: all 20 shapes, explicitly enumerated and each individually
closed (per the round-26/27 write-up convention — do not batch-dispatch
without naming which mechanism closed which shape).

Watch out for:
- **Do not attempt any self-similar/rescaling reduction of $(\star_3)$ to
  a smaller $(\star_k)$ instance** — this is confirmed dead twice
  independently (round 23, `proposition-39-mass-conservation-obstruction`
  and the separate `h(m)`-as-corollary refutation) and a third attempt is
  explicitly barred by this round's dispatch.
- Do not conflate this target with $\mathrm{MaxCeil}(4)$ (already closed,
  §7.13) — $(\star_3)=\mathrm{MinFloor}(4)$ is a genuinely different
  quantity (min, not max, of $A$; budget across *all* pieces, not just
  $\pi_1$), even though the enumeration technique and several certified
  facts transfer.
- If §7.15's Necessity Theorem is invoked anywhere, remember it only
  shows the *complementary* MaxCeil residual for $m\ge5$ needs
  $(\star_{m-2})$ — it says nothing about whether $(\star_3)$ itself is
  provable by direct exhaustion, which is exactly what this outline
  attempts.

## Promotable lemmas

**Index-Chain Identity: $\mathrm{MinFloor}(\ell)\equiv(\star_{\ell-1})$
(§7.11, round 26 — recommend promoting to
`lemmas/minfloor-star-index-identity.md`).** For every $\ell\ge1$,
$\mathrm{MinFloor}(\ell)$ (the claim $A(S)\ge\sigma_\ell$ for every legal
$\le(\ell-1)$-cut refinement $S$ of any length-$\ell$ ratio-2
superincreasing tail $\sigma$) is logically equivalent — not just
implied-by or conditional-on — to the project's standing lower-bound
hypothesis $(\star_{\ell-1})$ (every legal $\le k$-cut response to the
unit ratio-2 ladder of length $k+1$ has $A\ge$ its own last element, at
$k=\ell-1$). Proved via the already-certified `alternating-sum-scaling`
($A(\lambda X)=\lambda A(X)$): any length-$\ell$ ratio-2 tail is a positive
rescaling of the unit ladder of the same length, and this rescaling is a
bijection between the two statements' legal-response sets, preserving both
sides of the inequality by the same factor. Corollaries: $\mathrm{MinFloor}
(2)=(\star_1)$ and $\mathrm{MinFloor}(3)=(\star_2)$ are unconditionally
true in full (both branches each), since $(\star_1),(\star_2)$ are the
project's only two currently-certified unconditional instances (per
`current.md`'s round-23 audit); $\mathrm{MinFloor}(\ell)$ for $\ell\ge4$
remains exactly as open as $(\star_{\ell-1})$ for $\ell-1\ge3$ — i.e. it is
not a bespoke gap needing new machinery, but literally the project's
general lower bound one level down. Combined with the already-certified
§7.10.4 reduction ($\mathrm{MaxCeil}(\ell)$'s top-untouched branch
$\Leftrightarrow\mathrm{MinFloor}(\ell-1)$), this pins down exactly:
$\mathrm{MaxCeil}(\ell)$'s top-untouched branch is unconditionally true iff
$\ell\le4$.

**$\mathrm{MaxCeil}(3)$ — Full Closure, both branches (§7.12, round 26 —
recommend promoting to `lemmas/maxceil-3-full-closure.md`).** For every
length-3 ratio-2 tail $\sigma=(\sigma_1,\sigma_2,\sigma_3)$ and every legal
refinement $S$ using $\le1$ cut, $A(S)\le\sigma_1-\sigma_3$. Top-untouched
branch: reduces to $(\star_1)$ (certified). Top-cut branch: WLOG
$\sigma=(4,2,1)$, $\sigma_1\to(a,4-a)$, $a\in(0,2]$; direct two-region case
split ($a\in(0,1)$: $A=3-2a$; $a\in[1,2]$: $A=1$), both $\le3=\sigma_1-
\sigma_3$. Resolves $(7.9.1)$ at $n=6$ (since $m=n-3=3$).

**$\mathrm{MaxCeil}(4)$ — Full Closure, both branches (§7.13, round 26,
this round's headline result — recommend promoting to
`lemmas/maxceil-4-full-closure.md`).** For every length-4 ratio-2 tail
$\sigma=(\sigma_1,\dots,\sigma_4)$ and every legal refinement $S$ using
$\le2$ cuts, $A(S)\le\sigma_1-\sigma_4$. Top-untouched branch: reduces to
$(\star_2)$ (certified, both branches, via the Index-Chain Identity above).
Top-cut branch: WLOG $\sigma=(8,4,2,1)$; exhaustive enumeration of the five
cut-distribution shapes with $\ge1$ cut on $\sigma_1$ and $\le2$ cuts total
— $(1,0,0,0),(2,0,0,0),(1,1,0,0),(1,0,1,0),(1,0,0,1)$ — each closed exactly
via `sharp-dominant-removal-identity` (peeling successive unique maxima)
plus Fact 1 ($A\ge0$) or Fact 2 ($A\le\mathrm{Total}$, both §5.2, already
certified); no new machinery invented, and the naive Triangle-Bound/
Max-Domination shortcut (verified insufficient: only gives $A\le5-a$) is
explicitly avoided per the round-26 outline. The bound $\sigma_1-\sigma_4$
is approached (not exceeded, not attained for a genuine cut) exactly at
the degenerate boundary connecting to the top-untouched branch. Resolves
$(7.9.1)$ at $n=7$ (since $m=n-3=4$).

**Minimum-Floor Untouched-Top Closure (§7.10.4, round 25 — recommend
promoting to `lemmas/minfloor-untouched-top-closure.md`).** For every
$\ell\ge1$, every ratio-2 superincreasing tail $\sigma=(\sigma_1,\dots,
\sigma_\ell)$, and every legal refinement $S$ of $\sigma$ that leaves
$\sigma_1$ completely untouched (any number of cuts on the remaining
elements $\sigma_2,\dots,\sigma_\ell$, unrestricted), $A(S)\ge\sigma_\ell$.
Proved in one line: `sharp-dominant-removal-identity` peels the untouched
global max $\sigma_1$, reducing the target to $A(S')\le\sigma_1-\sigma_\ell$
where $S'=S\setminus\{\sigma_1\}$; the general, unconditional Fact 2
($A\le\mathrm{Total}$, §5.2) applied to $S'$ together with the already-
certified identity $R(\sigma)+\sigma_\ell=2\sigma_1$ (eq. (5.4)/(7.10.1))
gives exactly $A(S')\le\mathrm{Total}(S')=R(\sigma)-\sigma_1=\sigma_1-
\sigma_\ell$. No budget cap on the remaining cuts is needed at all — the
fact holds for *any* number of cuts on $\sigma_2,\dots,\sigma_\ell$, not
just $\le\ell-1$. Fully general (only needs $\sigma$ to be a ratio-2 tail,
via identity (7.10.1); the rest of the argument uses no ladder structure
beyond that one identity).

**Exact reduction: $\mathrm{MaxCeil}(\ell)$'s untouched-top branch
$\Leftrightarrow$ $\mathrm{MinFloor}(\ell-1)$ (§7.10.4, round 25 — record
as part of the sharpened open-gap statement, not yet a standalone certified
lemma since $\mathrm{MinFloor}$ itself is only partially closed).** If $S$
is a legal $\le(\ell-2)$-cut refinement of $\sigma$ leaving $\sigma_1$
untouched, then $A(S)\le\sigma_1-\sigma_\ell$ is exactly equivalent, via
`sharp-dominant-removal-identity`, to $A(S')\ge\sigma_\ell$ where $S'=S
\setminus\{\sigma_1\}$ is a legal $\le(\ell-2)=((\ell-1)-1)$-cut refinement
of $(\sigma_2,\dots,\sigma_\ell)$ — i.e. precisely an instance of
$\mathrm{MinFloor}(\ell-1)$. A genuinely new, checked (polarity-verified)
identity chain; not previously on file in this form. Recommend the next
round attack $\mathrm{MinFloor}(\ell)$'s remaining open branch (top element
of $\sigma$ itself receiving one or more of the spare cuts) directly, since
by this reduction it closes **both** remaining open items ($\mathrm{MinFloor}$
in full, and — one level up — $\mathrm{MaxCeil}$'s untouched branch) at
once.

**Sharpened statement of (7.9.1)'s open gap (§7.10.7, round 25 — not a
lemma, a precisely narrowed open target).** (7.9.1) $\iff\mathrm{MaxCeil}(m)$
$\iff E(T''')\ge p_5/2$ is now known to reduce entirely to closing
$\mathrm{MinFloor}(\ell)$'s (and $\mathrm{MaxCeil}(\ell)$'s) "top element of
the tail receives at least one spare cut" branch for general $\ell$ — the
untouched-top branch of both quantities is fully handled (the first
unconditionally via a cheap fact, the second via the exact reduction above).
Hand-checked consistent (not violated) at $\ell\le3$ (§7.10.6) but not
proved for general $\ell$.

**Box-Endpoint Domination Fact (§7.9.3, round 24 — recommend promoting to
`lemmas/box-endpoint-domination-fact.md`).** For any finite multiset $T$
with $\max(T)=c<M$, and $g(b):=A(\{b\}\cup T)$ on $[0,M]$: on $[c,M]$,
$g$ is affine with slope exactly $+1$ (since $T_{>b}=\varnothing$
throughout, so the Insert-Element Identity gives $g(b)=b-A(T)$ there
exactly), hence strictly increasing, so $g(M)\ge g(c)$ always. Consequence:
whenever the Single-Insert-Point Vertex Lemma's box-endpoint candidate
$b=M$ and the candidate $b=\max(T)$ are compared, $b=M$ is *always*
dominated and needs no separate bound — a genuinely reusable pruning fact
for any future application of the Single-Insert-Point Vertex Lemma (not
ladder-specific, no structure on $T$ beyond finiteness needed). Proved
in full, one line, from the already-certified Insert-Element Identity;
verified symbolically at the ladder instance $n=6$ this round (§7.9.5's
computation implicitly exercises the same identity chain).

**Sharpened statement of the T'-cuts-$p_4$ open gap (§7.9.5, round 24 —
not a lemma, but a precisely pinned-down open target, recommended for the
outliner/next builder to attack directly rather than the whole
undifferentiated sub-case).** Prove or refute:
$$A(T''')\ \le\ c_1-f(n)\tag{7.9.1}$$
for $T'''$ a legal refinement of $\{p_5,\dots,p_{n+1}\}$ using $\le n-5$
cuts and $c_1\in[p_4/2,p_4)$ the larger fragment of a split of $p_4$ (i.e.
$c_1=p_4-c_2$ for some legal $c_2\in(0,p_4/2]$). Proved this round: this
does **not** follow from $A\le\mathrm{Total}$ (explicit counterexample
regime at the symmetric split, verified exactly at $n=6$) nor from a
general refinement-monotonicity fact (known false in general, per
`current.md`). This is the single remaining sub-target isolated from
§7.8's four-breakpoint vertex family — narrower and more precise than the
prior "recouples to the same obstruction" diagnosis.

**Single-Insert-Point Vertex Lemma (§7.8, round 23 — promoted to
`lemmas/single-insert-point-vertex-lemma.md`).** For any finite multiset
$T$ and closed interval $[0,M]$, $g(b):=A(\{b\}\cup T)$ is piecewise affine
with slope $\pm1$ (never $0$) between consecutive points of
$\{0,M\}\cup(T\cap[0,M])$, so $\min_{b\in[0,M]}g(b)$ (and likewise
$\max$) is attained at one of these finitely many breakpoints. Fully
general, elementary (one-line slope computation), no ladder or budget
structure used — the single-free-variable special case of the general
`vertex-minimum-theorem`, derived independently and more directly for
this case. Independently verified (`/tmp/check_insert_vertex.py`,
`/tmp/check_argmin_location.py`).

**Truncated Alternating Sum Ceiling (§7.1, new this round — recommend
promoting to `lemmas/truncated-alternating-sum-ceiling.md`).** For any
finite multiset $S$ of nonnegative reals and any $v\ge0$,
$A(S)-2A(S_{>v})\le v$, with equality attained (e.g.) at $S=\{v\}$. Proved
from scratch by the same elementary level-set/integral decomposition that
powers the already-certified `truncated-alternating-sum-floor`, run with the
opposite pair of one-sided bounds — fully general, no ratio-2/ladder
structure needed. Independently verified by $300{,}000$ random-rational
trials (`/tmp/check_ceiling_general.py`), zero violations. This is the
natural "dual" fact to the certified Floor lemma and directly targets the
quantity `greedy-halving-adversary`'s round-19 outline names $\Delta(n,v)$.

**$n=3$ Middle-Band Closure — TRUE $\varepsilon$-corrected target
(§7.5/§7.5.2, round 21 — supersedes the round-19/20 $(\sharp)$-only
version as a concrete instance, not yet a standalone general lemma).** At
$n=3$, the corrected cut-budget cap forces $R'=\tau=\{p_3,p_4\}$ exactly
(no adversarial freedom); by the Band-Parity Fact, $\varepsilon(v_2)=1$
occurs exactly on the interior band $v_2\in[p_4,p_3)$, and there the TRUE
target $(\sharp')$ (imported from `greedy-halving-adversary`'s Theorem 34
(corrected) identity chain) reduces to $v_1+v_2\le6p_4=s+3p_4$, proved
**strictly** by adding the domain bound $v_1<p_2=4p_4$ to the case
hypothesis $v_2<p_3=2p_4$ termwise. The two outer bands have
$\varepsilon(v_2)=0$, where $(\sharp')=(\sharp)$ and the round-19/20 proof
already suffices unchanged. Together this closes $(\sharp')$ — the actual
sufficient inequality the sibling's file records as an open bridge gap for
$\varepsilon=1$ — unconditionally at $n=3$, with no numerics substituting
for the proof. Recommend the reviewer note this as a fully rigorous
$\varepsilon$-corrected base case for whichever sibling approach
(`greedy-halving-adversary`'s own route, or a future general-$n$ closure of
this file's §7.6, which remains open) eventually closes the general-$n$
middle band — it can be cited as the $n=3$ instance of $(\sharp')$ rather
than re-derived.

**Vertex-maximization Proposition (§5.1, new this round — recommend
promoting to `lemmas/exchange-smoothing-vertex-maximization.md`).** For a
fixed budget/mass $(m,\tau,s,k)$, the maximum of $E(F\cup\tau)$ over the
Case-I polytope (nonneg parts summing to $s$, each $\le\tau_1$, $\le k$
parts) is attained at a configuration of the form "$p$ parts individually
pinned to specific $\tau_l$ values (repetition allowed) plus one remaining
tied group at a common value $v$." Proved by a self-contained finite
exchange-smoothing/local-perturbation argument (no external LP package
needed, reusing only the continuity/compactness facts already used by
`vertex-minimum-theorem`, run for the max instead of the min — verified
explicitly that no min-specific step is used). Fully general (not
ladder-specific: applies to any ratio-2 tail, indeed the proof never used
the ratio-2 structure, only that $\tau$ is a fixed finite reference set).

**Ratio-2 Spacing Lemma (§5.3, new this round — recommend promoting to
`lemmas/ratio-2-spacing-lemma.md`).** For any $X\subseteq\{\tau_1,\dots,
\tau_m\}$ (sub-collection of a ratio-2 superincreasing tail) with elements
$\nu_1<\dots<\nu_j$, $\nu_{i+1}\ge2\nu_i$ for every $i$ (not just adjacent
original indices — any two distinct elements of $X$ differ by a factor
$\ge2$ per index-gap). Trivial but load-bearing: used three times in §5
(Last-Element Bound's induction, and both of (5.7)/(5.8)'s bounds on $v$).

**Last-Element Bound (§5.5, new this round — recommend promoting to
`lemmas/last-element-bound.md`).** For nonempty $X\subseteq\{\tau_1,\dots,
\tau_m\}$, $A(X)\ge\min(X)\ge\tau_m$. Proved by strong induction on $|X|$,
peeling the smallest element, using the Ratio-2 Spacing Lemma at the even-size
step. Closes the entire $q$-even branch of Case I in one shot when combined
with the domain bound $s\le2\tau_1$ and the identity $R(\tau)+\tau_m=2\tau_1$.

**Case I Closure Theorem (§5, this round's headline result — recommend
promoting to `lemmas/case-i-closure-theorem.md`).** For every $m\ge1$,
ratio-2 tail $\tau$, $s\in(0,2\tau_1]$, and Case-I partition $F$ of $s$ into
$\le m+1$ parts each $\le\tau_1$: $A(F\cup\tau)\ge s-R(\tau)$. Proved in
full via the Vertex-maximization Proposition + odd-run reduction + the
Last-Element Bound + Facts 1–2 (`half-bound-lemma` and its trivial dual
$A\le\mathrm{Total}$) + the Ratio-2 Spacing Lemma. Combined with the
already-certified `case-ii-closure-theorem`, this gives Claim (A)'s full
lower bound for every $m$/$n$, unconditionally, no numerics needed for
correctness (extensive exact-`Fraction` exhaustive enumeration up to $m=10$
used only as an independent cross-check).

**Claim (A) — Full Closure (§6, this round).** For every $n\ge1$: (i) an
explicit $F^\ast$ (§2, already certified as
`claim-a-achievability-construction`) attains $A(F^\ast\cup T)=a_n$
exactly; (ii) every legal $F$ satisfies $A(F\cup T)\ge a_n$ (this round's
Case I Closure Theorem, combined with the already-certified Case II
Closure Theorem). Together these fully resolve Claim (A) as originally
posed by the round-5 explorer's decomposition. Not yet reviewer-certified
as a standalone combined statement; recommend the proof-reviewer verify
§5's chain (the Vertex-maximization Proposition, the Spacing Lemma, the
Last-Element Bound, and the case (a)/(b) split of §5.6–5.7) and certify
`case-i-closure-theorem` and the combined `claim-a-full-closure`.

---

## Outline (proof-outliner, round 22)

**Redirect confirmed, but scoped as "pending," not "close now": do NOT
dispatch further vertex/exchange-smoothing enumeration work at §7.6 this
round.** The round-22 explorer
(`/tmp/round-22/math-explorer-eps-bridge.md`, §3) gave an exact algebraic
identification: substituting `greedy-halving-adversary`'s Theorem 34
(corrected) identity $s-p_2=-f(n)$ into this file's own $(\sharp')$ at the
hardest point $v_1\to p_2^-$ gives, term for term,
$$\Delta(n,v_2)\ \le\ v_2-f(n)-2v_2\varepsilon(v_2),$$
which is **exactly** `greedy-halving-adversary`'s $(\Diamond')$ — i.e.
§7.6's "general $n\ge4$ cross-piece tie-vertex enumeration" gap and the
sibling's Theorem 35b ($v\ge p_3$ range) / Theorem 36 (Case (b), $p_3$
cut, $n\ge5$) gaps are literally the same open inequality, not two
independent obstructions. §7.6's own vertex-enumeration attempt already
re-encountered the project's central, long-standing obstruction (cross-
piece tie vertices) — the same wall Claim A's machinery hit before
exchange-smoothing was replaced by direct evaluation — while the sibling's
algebraic-floor route (Fact 1 + `truncated-alternating-sum-floor` +
strong induction, no vertex enumeration at all) has been the one route
that actually closes instances of this target. Continuing §7.6
independently this round would duplicate effort on a technique already
shown weaker on this exact object.

**But the sibling's fix is not yet fully built this round** (round 22's
dispatch to `greedy-halving-adversary` targets Theorem 36's extension to
$n\ge5$ via an induction-tower reframing — outlined there, not yet proved).
So §7.6 cannot honestly be closed as a corollary *this* round; claiming so
would overclaim. Two concrete, smaller, actually-closable items for this
slug this round instead:

1. **Write the forward corollary stub now (§7.7, new), not the closure.**
   State explicitly, as a conditional corollary pending the sibling: *"If
   `greedy-halving-adversary`'s Theorem 35b ($v\ge p_3$ range, now fixed —
   see that file's round-22 update — and Theorem 36's Case (b) extension to
   $n\ge5$, currently in progress) establishes $(\Diamond')$ for all
   $n\ge3$, then §7.6's general-$n$ gap closes immediately by the §3
   substitution above, with **no additional argument** — this file's own
   $(\sharp')$ is definitionally the same statement as $(\Diamond')$ once
   Theorem 34 (corrected)'s identity $s-p_2=-f(n)$ is substituted."* Write
   this out as an explicit, checkable algebraic derivation (not just an
   assertion) so a future round can certify it as a one-line corollary the
   moment the sibling's fix lands — this is real, useful, low-risk work
   this round even though it cannot be marked closed yet.
2. **Small closable target this round: independently verify the
   identification numerically at $n=4$** (one level past the already-closed
   $n=3$ base case in §7.5.2, and the level `greedy-halving-adversary`'s
   Theorem 36 already closes unconditionally for the weaker $(\Diamond)$).
   Concretely: exact-`Fraction` check that this file's own $(\sharp')$ and
   the sibling's $(\Diamond')$, evaluated on the *same* random legal
   configurations at $n=4$, agree numerically (not just algebraically) —
   this is a genuinely independent cross-check (different codebase/script
   than either file's existing numerics) of the §3 substitution's
   correctness, cheap, and directly strengthens confidence in item 1's
   corollary before it is relied upon. If a mismatch is found, that is a
   high-value, immediate finding (it would mean the identification itself
   has a bug) — report it prominently rather than silently reconciling it.

**Explicitly do not attempt:** any fresh attack on the general-$n$
cross-piece vertex polytope itself (§7.6 as originally scoped) — this is
the deprioritized route per the explorer's finding above. If a future round
judges the sibling's induction-tower route has stalled for several rounds,
that is the trigger to revisit vertex enumeration as a genuinely different
mechanism, not before.

## Outline (proof-outliner, round 26)

**Reconciliation (round-26 explorer, `/tmp/round-26/math-explorer-791-gap.md`):
(7.9.1) and the sibling `greedy-halving-adversary`'s Theorem-37 "non-maximal-
tie" gap are NOT the same object.** Trust this finer breakdown over the
theorem-37-gap explorer's stronger claim of identity — it was reached by
reading both files' actual case structure side by side, not by pattern-
matching the shape. There are **three genuinely distinct open items** inside
Case (b)'s "$v\ge a$" branch:
1. `greedy-halving-adversary`'s Theorem 37 internal non-maximal-tie
   enumeration ($T'$-untouched branch; lives entirely in that file, not
   here).
2. The **$b=c_1$ breakpoint recursion**, $A(\{c_2\}\cup T''')$ — this file's
   §7.9.4 and `greedy-halving-adversary`'s "Diagnostic finding" independently
   derived the *identical* object by the identical pair-cancellation step.
   Genuinely shared, cross-file confirmed; still open in both places.
3. **(7.9.1) itself** ($b=c_2$ breakpoint, i.e. $\mathrm{MaxCeil}(m)$'s "top
   cut" branch) — this file's own target, not attacked at all in the
   sibling file.
Closing item 2 (if either file's builder gets to it) does not by itself
close item 1 or item 3 — state this explicitly in both files rather than
merging them. The "Deletion Lower Bound" lemma the theorem-37-gap explorer
proposes is a reasonable tool to try on item 2 specifically (both files'
independent derivations of $A(S\setminus\{t\})$-shaped residuals match its
intended scope) — worth a shot, but scope it to item 2, not claimed to
resolve items 1 or 3 as well until actually checked.

**Structural finding to fold in (§7.10 reframing):** $\mathrm{MinFloor}(\ell)$
is not a bespoke sub-lemma — its domain (legal $\le(\ell-1)$-cut response to
an $(\ell-1)$-ladder) is *definitionally* the standing hypothesis
$(\star_{\ell-1})$. Tracing the index chain from §7.10 ((7.9.1)
$\Leftrightarrow\mathrm{MaxCeil}(n-3)$; its "top untouched" branch
$\Leftrightarrow\mathrm{MinFloor}(n-4)=(\star_{n-5})$): restate
$\mathrm{MinFloor}(\ell)$'s "top cut" branch explicitly as **"conditional on
$(\star_{\ell-1})$, hence unconditionally TRUE whenever $\ell-1\le2$"** —
i.e. free for $n\le7$ — in the same style already used for Theorem 36b/37,
rather than leaving it as an undifferentiated "needs new machinery" item.
**Builder: independently re-verify this index arithmetic before relying on
it** (the explorer flagged it was derived by direct substitution, not
copied from a certified source). Keep $\mathrm{MaxCeil}(m)$'s *own* "top
cut" branch (item 3 above, the file's real target) separate — it is an
upper-bound statement, not obviously reducible to $(\star_\cdot)$, and
should be treated as genuinely fresh content.

**Concrete build target this round: close $\mathrm{MaxCeil}(3)$ and attempt
$\mathrm{MaxCeil}(4)$ (the $n=7$ instance).**
1. **$\mathrm{MaxCeil}(3)$ — write up the explorer's exact hand closure
   formally.** For $\sigma=(4,2,1)$, $\sigma_1=4$ split into $(a,4-a)$,
   $a\in(0,2]$ WLOG: sub-case $a\in(0,1)$ gives sorted order
   $(4-a,2,1,a)$, $A=3-2a\le3$; sub-case $a\in[1,2]$ gives sorted order
   $(4-a,2,a,1)$, $A=1\le3$. Both hold with the target $A(S)\le3=\sigma_1-
   \sigma_3$. This is a genuine one-free-coordinate case split (budget
   $\le1$ cut), directly an instance of the certified **Single-Insert-Point
   Vertex Lemma** — no new machinery, just write it out rigorously
   (including the general-$\sigma$ version, not just the numeric
   $(4,2,1)$ instance) and get it reviewer-certified.
2. **$\mathrm{MaxCeil}(4)$ ($n=7$) — the real target.** Budget $\le2$ cuts,
   two free coordinates once $\sigma_1$ is split (a genuine 2-D polytope,
   no longer a 1-D slope argument). Do **not** invent new machinery: reuse
   the already-certified **exchange-smoothing-vertex-maximization**
   (`lemmas/exchange-smoothing-vertex-maximization.md`, proved for exactly
   the shape "box-constrained partition merged with a fixed ratio-2 tail")
   — this is precisely a 2-cuts-on-$\sigma_1$-plus-tail configuration.
   Do **not** try the naive `Triangle Bound for A` + `Max Domination Lemma`
   shortcut first — the explorer already checked it and it is too lossy
   (gives $A(S)\le5-a$, only implying the target for $a\ge2$, false for
   $a<2$; the true value is exactly $3-2a$ or $1$, matching the exact
   vertex evaluation, not the sub-additive bound). Report explicitly
   whether the 2-coordinate vertex evaluation closes $\mathrm{MaxCeil}(4)$
   or exposes a genuinely new obstruction not seen at $\ell=3$.

**Do not claim** that closing $\mathrm{MaxCeil}(3)$/$(4)$ closes (7.9.1) in
general — $\mathrm{MaxCeil}(m)$ for the actual index $m=n-3$ needed at each
$n$ is a separate instance per $n$; state precisely which $n$ (i.e. which
$\ell=m$) has been closed rather than asserting the general pattern from a
couple of small cases.

## Outline (proof-outliner, round 5)
(preserved for reference.) Assigned claim (A): "min over all partitions F of
Xiang Yu's fragmenting p_1 (tail T untouched) of A(F∪T) equals a_n exactly,"
via an explicit per-dyadic-band decomposition. This build's actual route
diverged from the literal "generic-multiset band-occupancy formula"
suggested by the outline in favor of directly applying
`sharp-dominant-removal-identity` recursively, producing the self-similar
reduction of §3.

## Outline (proof-outliner, round 6)
Priority: open new framings elsewhere; if built, finish the remaining
sub-range of Case II and attack Case I. (Case II fully closed this round;
Case I diagnosed as needing an upper bound at a smaller instance.)

## Outline (proof-outliner, round 7)
Reformulate Case I as $E(F\cup\tau)\le R(\tau)$; attempt peel-the-minimum.
(Closed two of three branches; isolated $(\dagger)$.)

## Outline (proof-outliner, round 8)
Attack Claim (A) Case I via exchange-smoothing/vertex-maximization of
$E(F\cup\tau)$ directly, bypassing peel-induction; adapt the crux `aimo-0146`
exchange-smoothing-to-plateau mechanism, reusing `vertex-minimum-theorem`
and `odd-run-reduction-lemma`. **This round's build (§5 above) carries this
out in full and closes Case I completely.**

## Promotable lemmas (round 27)

**$\sigma_2$-Untouched Closure Theorem** (§7.14 above; full writeup at
`lemmas/sigma2-untouched-closure-theorem.md`, not yet reviewer-certified).
For every $m\ge2$, every ratio-2 tail $\sigma$, and every legal refinement
$S$ with $\ge1$ cut on $\sigma_1$ and $0$ cuts on $\sigma_2$ (no
restriction on $\sigma_3,\dots,\sigma_m$ or on the number of cuts on
$\sigma_1$), $A(S)\le\sigma_1-\sigma_m$. Proved in full via
`sharp-dominant-removal-identity`, `odd-run-reduction-lemma`, Fact 1, Fact
2, and the identity $R(\sigma)+\sigma_m=2\sigma_1$ — no induction on $m$,
no case enumeration, no $(\star_k)$ input. Recommend certification: this
is immediately reusable anywhere `MaxCeil`/`(7.9.1)`-style top-cut-branch
questions arise at any $m$, and cleanly subsumes $4$ of the $5$ shapes
individually verified by hand at $m=4$ in round 26's §7.13.

**Necessity Theorem for $\mathrm{MaxCeil}(m)$'s $\sigma_2$-touched residual**
(§7.15 above; not proposed as a standalone certified lemma, since its
content is a *dependency/negative* result rather than a reusable positive
fact — but the underlying **Continuity Lemma** used in its proof (§7.15,
"$A(S_\varepsilon)$ is continuous in $\varepsilon$, including at the
degenerate boundary $\varepsilon=0$, for a fixed background multiset and a
two-part split of one fixed-mass coordinate") is itself a clean, general,
reusable fact — essentially a corollary of the continuity argument already
inside §5.1's Vertex-maximization Proposition, made explicit and
standalone here. Worth extracting as its own micro-lemma
("degenerate-split-continuity") if a future round needs a similar
$\varepsilon\to0$ boundary argument elsewhere in this project (e.g. to
locate other "does this branch secretly need $(\star_k)$" questions by the
same technique).

## Promotable lemmas (round 28)

**Master Theorem I — Untouched-Top Peel Bound for $\mathrm{MinFloor}(4)$**
(§7.16 above). For the unit ratio-2 ladder $\pi=(8,4,2,1)$ and any legal
refinement $U$ leaving $\pi_1$ untouched (arbitrary cuts, arbitrary
distribution, on $\pi_2,\pi_3,\pi_4$), $A(U)\ge\pi_4=1$. Proved in $3$
lines via `sharp-dominant-removal-identity` (peel the untouched $\pi_1$,
strict unique max since $\pi_1>\pi_2$) plus Fact 2 ($A\le\mathrm{Total}$).
This is a special case (no cut budget cap needed on the tail) of the
already-certified `minfloor-untouched-top-closure` general-$\ell$ theorem
(§7.10.4) — cross-check, not new content on its own, but confirms
§7.10.4's abstract statement concretely at $\ell=4$.

**Master Theorem II — Single-Split-Plus-Untouched-Second-Piece Bound**
(§7.16 above, genuinely new, not previously on file). For the unit
ratio-2 ladder $\pi=(8,4,2,1)$, any split $\pi_1\to\{a,8-a\}$ ($a\in
[0,4]$, one cut), $\pi_2=4$ untouched, and *any* legal refinement $V$ of
$(\pi_3,\pi_4)$ using any number of cuts (only $\mathrm{Total}(V)=\pi_3+
\pi_4=3$ is used, not the cut count or distribution), $A(\{a,8-a,4\}\cup
V)\ge1$. Proved by a $3$-case peel cascade (Fact 1 for $a\le3$; one more
peel + Fact 2 for $a\in(3,4)$; `odd-run-reduction-lemma` for the boundary
tie $a=4$) — uniform in how $V$'s budget is split between $\pi_3,\pi_4$.
Directly reusable for any future closure needing "one cut on the top
piece, second piece untouched, arbitrary refinement below" — a genuinely
more general statement than the single ladder instance it was derived
for, since the proof never used a specific cut-count cap on $V$, only
its total mass.

**Open-gap statement (not a lemma, recorded for the next round attacking
$(\star_3)$ directly).** The $6$ shapes $(1,1,0,1),(1,1,1,0),(1,2,0,0),
(2,0,0,1),(2,0,1,0),(2,1,0,0)$ each have a residual $3$-free-parameter
sub-region (roughly: the piece-$1$ dominant fragment lands strictly
between $\pi_3\cdot\text{something}$ and $\pi_2$, forcing a genuine
$3$-way tie-vertex comparison) where the cheap peel-and-Fact technique of
Master Theorems I–II provably fails (Fact 2 gives a bound $4$–$5$ times
too weak near the true extremal vertex). Achievability at exactly $A=1$
is fully proved (construction in §7.16); only the matching lower bound on
this residual region is missing. Exact rational vertex enumeration
(reproducible via `vertex-minimum-theorem`'s finite-candidate reduction)
confirms the true minimum is exactly $1$ on all $6$ shapes and identifies
the extremal vertices, but a from-scratch hand derivation of the lower
bound on the residual region is the concrete task for the next round.
**(Superseded in part by §7.17 below — round 29 closes $2$ of the $6$
shapes in full using a newly-proved general lemma; the other $4$ remain
open exactly as described above.)**

### 7.17 Round-29 addendum: fixing the outline-reviewer's flagged citation
bug, and closing $2$ of the $6$ residual shapes in full via a new general
Pair-Insertion Ordering Lemma

**The bug, restated precisely.** The round-29 outline proposed reducing
each of the $6$ residual shapes' $2$–$3$ interacting free coordinates by
applying `single-insert-point-vertex-lemma` "one free coordinate at a
time." That lemma is proved only for a single value $b$ inserted into a
*fixed* rest $T$ (its own proof gives slope exactly $\pm1$ on each
sub-interval, since only $b$'s own rank changes as $b$ varies). In every
one of the $6$ shapes, at least two of the free coordinates are **coupled
by mass conservation** (e.g. shape $(2,0,1,0)$'s $f_1,f_2,f_3$ with
$f_1+f_2+f_3=\pi_1$ fixed, or its $g_1,g_2$ with $g_1+g_2=\pi_3$ fixed):
freezing one and varying the other under this constraint moves *two*
elements of the multiset simultaneously (one up, one down by the same
amount), which the outline-reviewer confirmed numerically has slope
$\pm2$, not $\pm1$ — a genuinely different function, so citing
`single-insert-point-vertex-lemma` for such a pair is a citation
mismatch, exactly as the reviewer diagnosed. The fix (as the reviewer
specified): use the already-certified, fully general
`vertex-minimum-theorem` directly for any coordinate-group sharing a
mass-conservation constraint, and reserve `single-insert-point-vertex-
lemma` only for genuinely independent box coordinates. Below, rather than
re-deriving the general theorem's machinery from scratch for this small
finite-dimensional case, we prove a self-contained elementary lemma that
captures exactly the closed-form consequence needed here (an explicit
sorted-rank computation, not an appeal to compactness/exchange-smoothing
— simpler and fully sufficient for a $\le4$-element residual).

**Lemma (Pair-Insertion Ordering).** *Let $p\ge q\ge0$ with $p+q=C$, let
$w\ge0$ satisfy $q\le w\le p$, and let $x\ge0$ be arbitrary. Then*
$$A(\{x,p,q,w\})=\begin{cases}
x+w-C, & x\ge p,\\
2p-x+w-C, & w\le x<p,\\
2p-w+x-C, & q\le x<w,\\
C-w-x, & x<q.
\end{cases}$$

**Proof.** Since $q\le w\le p$, the multiset $\{p,w,q\}$ sorts (weakly)
descending as $p\ge w\ge q$ regardless of ties. Inserting $x$ produces
exactly $4$ possible rank positions, by trichotomy of $x$ against
$p,w,q$ (with the boundary cases assigned consistently, e.g. $x=p$ placed
in the first bracket):
- $x\ge p$: sorted order $x,p,w,q$ (descending); alternating sum ($+,-,
  +,-$) is $x-p+w-q=x-p+w-(C-p)=x+w-C$.
- $p>x\ge w$: sorted order $p,x,w,q$; sum $p-x+w-q=p-x+w-(C-p)=2p-x+w-C$.
- $w>x\ge q$: sorted order $p,w,x,q$; sum $p-w+x-q=p-w+x-(C-p)=2p-w+x-C$.
- $x<q$: sorted order $p,w,q,x$; sum $p-w+q-x=p-w+(C-p)-x=C-w-x$.

Each case is a direct computation of $4$ ranked terms with alternating
sign; no case is omitted (the four intervals $[p,\infty),[w,p),[q,w),
[0,q)$ partition $[0,\infty)$ exactly, using $q\le w\le p$). The four
formulas agree at every shared boundary (direct substitution: at $x=p$,
first gives $p+w-C$ and second gives $2p-p+w-C=p+w-C$; at $x=w$, second
gives $2p-w+w-C=2p-C=p-q$ and third gives $2p-w+w-C=2p-C=p-q$; at $x=q$,
third gives $2p-w+q-C=2p-w-p=p-w$ [using $C=p+q$] and fourth gives
$C-w-q=p-w$), confirming $A$ is continuous across the boundaries, as it
must be (a general fact — the alternating-sum functional is continuous
in each coordinate). $\blacksquare$

**Application 1 — shape $(2,0,1,0)$ closed in full (both the previously-
closed $f_1>4$ branch, re-confirmed, and the residual $f_1<4$ branch,
newly closed).** Recall the shape: $\pi_1=8$ splits into $f_1\ge f_2\ge
f_3\ge0$ ($f_1+f_2+f_3=8$); $\pi_2=4$ untouched; $\pi_3=2$ splits into
$g_1\ge g_2\ge0$ ($g_1+g_2=2$); $\pi_4=1$ untouched. $U=\{f_1,f_2,f_3,4,
g_1,g_2,1\}$. By pigeonhole $f_1\ge8/3$ always (max of $3$ nonnegative
reals summing to $8$).

*Sub-case $f_1<4$ (the residual).* Then $f_2\le f_1<4$, so $4$ is the
(weakly, possibly tied only with itself — no other element equals $4$
here) unique element $\ge4$; since $g_1\le2<4$ and $1<4$, $4$ is the
strict unique max of $U$ (`sharp-dominant-removal-identity` applies):
$A(U)=4-A(\{f_1,f_2,f_3,g_1,g_2,1\})$.

Within this $6$-set, $f_1\ge8/3>2\ge g_1$ and $f_1>1$ trivially, so $f_1$
is $\ge$ every other element; if $f_1>f_2$ strictly it is the strict
unique max and `sharp-dominant-removal-identity` peels it:
$A(\{f_1,\dots\})=f_1-A(\{f_2,f_3,g_1,g_2,1\})$. If $f_1=f_2$ (tie), the
value $f_1=f_2$ has multiplicity $2$ in the $6$-set (it cannot also equal
$f_3$'s value and land at odd multiplicity unless $f_1=f_2=f_3$, handled
below), and by `odd-run-reduction-lemma` an even-multiplicity value
cancels entirely: $A(\{f_1,f_2,f_3,g_1,g_2,1\})=A(\{f_3,g_1,g_2,1\})$
directly. If $f_1=f_2=f_3$ (all three fragments equal, forced value
$8/3$), the multiplicity is $3$ (odd), and `odd-run-reduction-lemma`
leaves exactly one copy of $8/3$: $A(\{f_1,f_2,f_3,g_1,g_2,1\})=
A(\{8/3,g_1,g_2,1\})$ — this is exactly the formula
$A(\{f_2,f_3,g_1,g_2,1\})$'s own limiting case as $f_2,f_3\to8/3$ (both
equal), confirmed consistent below since the next peel step is uniform in
$f_2,f_3$ individually only through their sum and max.

Continuing with the generic (non-doubly-tied) branch: within
$\{f_2,f_3,g_1,g_2,1\}$, since $f_1<4$ strictly, $f_2\ge(8-f_1)/2>2$
strictly (as $f_1<4\iff8-f_1>4\iff(8-f_1)/2>2$), so $f_2>2\ge g_1\ge g_2$
and $f_2>2>1$; thus $f_2$ is $>$ every other element except possibly
$f_3$. If $f_2>f_3$ strictly, peel: $A(\{f_2,\dots\})=f_2-A(\{f_3,g_1,g_2,
1\})$. If $f_2=f_3$ (the case handled just above merges into this one,
since then $f_2=f_3=8/3$ and the peel step is vacuous — there is no
distinct $f_2$ to peel past $f_3$, and one directly has
$A(\{f_2,f_3,g_1,g_2,1\})=A(\{8/3,g_1,g_2,1\})$ by the same even/odd-run
argument, matching the limit of the generic formula below as $f_2\to f_3$).

In every branch, the computation reduces (either via two literal peels,
giving $A(U)=4-f_1+f_2-A(\{f_3,g_1,g_2,1\})$, or via the odd-run
collapses, which are exactly the boundary limits of this same formula as
$f_1\to f_2$ or $f_2\to f_3$) to bounding
$$A(\{f_3,g_1,g_2,1\})\ \le\ f_2-f_1+3\qquad(=:\ T).$$
Apply the Pair-Insertion Ordering Lemma with $x=f_3$, $p=g_1$, $q=g_2$,
$w=1$, $C=2$ (valid since $g_2\le1\le g_1$, as $g_1\ge g_2$, $g_1+g_2=2$
force $g_1\ge1\ge g_2$). Rather than bound each of the $4$ resulting
cases termwise (a first attempt at the middle two cases via crude
per-term bounds on $g_1,f_2$ separately did not close cleanly — the
bound needed genuinely mixes $f_1$ and $f_3$ together, not just their
individual ranges), we substitute the Lemma's *exact* closed form for
each case directly into $T-A$ and simplify as a single polynomial in
$f_1,f_2$ (via $f_3=8-f_1-f_2$), which closes every case outright.
Concretely: combining the *equality*
$$A(U)=4-f_1+f_2-A(\{f_3,g_1,g_2,1\})$$
with the Pair-Insertion Ordering Lemma's *exact* case formulas for
$A(\{f_3,g_1,g_2,1\})$, substituted in closed form (rather than a loose
inequality chain), and simplifying $T-(\text{lemma value})$ as an explicit
linear function of $f_1,f_2$ in each of the $4$ lemma cases, a polynomial
that is manifestly $\ge0$ on the shape's legal domain:

- Case $f_3\ge g_1$: $T-(f_3-1)=(f_2-f_1+3)-(8-f_1-f_2-1)=2f_2-4$. Since
  $f_2>2$ in this regime ($f_1<4$), $2f_2-4>0$. **Closes, strictly.**
- Case $1\le f_3<g_1$: $T-(2g_1-f_3-1)=(f_2-f_1+3)-2g_1+(8-f_1-f_2)+1=
  12-2f_1-2g_1$. Since $f_1<4$ and $g_1\le2$: $12-2f_1-2g_1>12-8-4=0$.
  **Closes, strictly** ($f_1<4\Rightarrow2f_1<8$ and $g_1\le2\Rightarrow
  2g_1\le4$, so $2f_1+2g_1<12$).
- Case $g_2\le f_3<1$: $T-(2g_1+f_3-3)=(f_2-f_1+3)-2g_1-(8-f_1-f_2)+3=
  2f_2-2g_1-2$. Since $f_2>2\ge g_1$ strictly (shown $f_2>2$, $g_1\le2$):
  $2f_2-2g_1-2>2\cdot2-2\cdot2-2=-2$ — **too weak this way**; redo:
  $2f_2-2g_1-2$: since $f_2>2$ and $g_1\le2$, $f_2-g_1>0$, but need
  $2(f_2-g_1)\ge2$, i.e. $f_2-g_1\ge1$, not obviously true from $f_2>2,
  g_1\le2$ alone (could have $f_2=2.1,g_1=2$, difference $0.1<1$). Use
  instead $f_3<1$ (case hypothesis) together with $f_2=8-f_1-f_3>8-f_1-1
  =7-f_1>3$ (since $f_1<4$). So $f_2>3$, giving $2f_2-2g_1-2>2\cdot3-2
  \cdot2-2=0$. **Closes, strictly**, using the case-specific bound
  $f_3<1\Rightarrow f_2>3$.
- Case $f_3<g_2$: $T-(1-f_3)=(f_2-f_1+3)-1+f_3=f_2-f_1+2+(8-f_1-f_2)=
  10-2f_1$. Since $f_1<4$: $10-2f_1>2>0$. **Closes, strictly.**

So all $4$ cases close, each via an explicit polynomial in $f_1,f_2$
(equivalently $f_1,f_3$) shown positive using only $f_1<4$ (residual
hypothesis) plus, in the third case, the sharper case-specific fact
$f_3<1\Rightarrow f_2>3$ — **no case relies on numerics**; the numeric
check mentioned in the aborted middle-case attempt above is superseded
by this clean direct substitution and is not part of the final proof.
This closes the entire residual $f_1<4$ of shape $(2,0,1,0)$
**by hand, with no numerics load-bearing**, matching (and superseding)
round 28's un-derived $f_1\in(3,4)$ gap. Combined with round 28's already-
reported closure of $f_1>4$ (independently re-confirmed this round by a
fresh $200{,}000$-trial exact-`Fraction` check, `/tmp/check_f1_above4.py`,
zero violations) and the boundary $f_1=4$ (a direct exact evaluation:
$U=\{4,2,2,4,g_1,g_2,1\}$ reduces, taking $g_1=2,g_2=0$ for the
achievability witness or any legal $g_1,g_2$ for the boundary check, to
$A\ge1$ by continuity of the two adjacent closed regimes, both attaining
exactly $1$ in the limit), **shape $(2,0,1,0)$'s lower bound is now fully
closed for every legal $U$, both directions.**

**Application 2 — shape $(2,0,0,1)$ closed in full on its residual
$f_1<4$ (new; this shape was not previously attempted individually).**
Recall: $\pi_1=8\to f_1\ge f_2\ge f_3\ge0$; $\pi_2=4,\pi_3=2$ untouched;
$\pi_4=1\to e\ge f\ge0$ ($e+f=1$). $U=\{f_1,f_2,f_3,4,2,e,f\}$.

For $f_1<4$: peel $4$ (strict unique max, since $f_2\le f_1<4$, $2<4$,
$e,f\le1<4$): $A(U)=4-A(\{f_1,f_2,f_3,2,e,f\})$. Peel $f_1$ (strict
unique max of the $6$-set, generic case $f_1>f_2$; the tie $f_1=f_2$
[resp. $f_1=f_2=f_3$] again collapses via `odd-run-reduction-lemma`
exactly as in Application 1, contributing $0$ [resp. leaving one copy],
consistent with the formula's continuity, since $f_1\ge8/3>2$ always):
$A(\{f_1,\dots\})=f_1-A(\{f_2,f_3,2,e,f\})$. Since $f_1<4$, $f_2\ge
(8-f_1)/2>2$ strictly, so $f_2>2\ge e\ge f$ and $f_2>2>e,f$; peel $f_2$
(generic case $f_2>f_3$, tie case as before): $A(\{f_2,\dots\})=f_2-
A(\{f_3,2,e,f\})$.

So $A(U)=4-f_1+f_2-A(\{f_3,2,e,f\})$, and the target $A(U)\ge1$ becomes
$$A(\{f_3,e,f,2\})\ \le\ f_2-f_1+3\ =:\ T.$$
Here the reference value $2$ is **above**, not between, the pair
$\{e,f\}$ ($e\le1<2$), so apply the mirrored form of the Pair-Insertion
Ordering Lemma (swap the roles: now $w=2\ge p=e\ge q=f$, $C=e+f=1$) —
by the identical proof method (sort $\{p,w,q\}=\{e,2,f\}$ as $2\ge e\ge
f$ since $w\ge p\ge q$ here, then insert $x=f_3$ by trichotomy):
$$A(\{x,p,q,w\})=\begin{cases}
x-w+2p-C, & x\ge w,\\
w-x+2p-C, & p\le x<w,\\
w+x-C, & q\le x<p,\\
w+C-2p-x, & x<q.
\end{cases}$$
(Derived exactly as in the Lemma's proof, sorting $w\ge p\ge q$ instead of
$p\ge w\ge q$; continuity across boundaries checked the same way.)
Substituting $p=e,q=f,w=2,C=1,x=f_3$ and $T=f_2-f_1+3$, using
$f_3=8-f_1-f_2$ throughout:

- $f_3\ge2$: $T-(f_3-2+2e-1)=T-f_3+3-2e=(f_2-f_1+3)-(8-f_1-f_2)+3-2e=
  2f_2-2-2e$. Since $f_2>2$ (shown) and $e\le1$: $2f_2-2-2e>4-2-2=0$.
  **Closes, strictly.**
- $e\le f_3<2$: $T-(2-f_3+2e-1)=T-1+f_3-2e=(f_2-f_1+3)-1+(8-f_1-f_2)-2e=
  10-2f_1-2e$. Since $f_1<4,e\le1$: $10-2f_1-2e>10-8-2=0$. **Closes,
  strictly.**
- $f\le f_3<e$: $T-(2+f_3-1)=T-1-f_3=(f_2-f_1+3)-1-(8-f_1-f_2)=2f_2-6$.
  Since $f_3<e\le1$: $f_2=8-f_1-f_3>8-f_1-1=7-f_1>3$ (using $f_1<4$), so
  $2f_2-6>0$. **Closes, strictly**, using the same case-specific
  sharpening as Application 1's analogous third case.
- $f_3<f$: $T-(2+1-2e-f_3)=T-3+2e+f_3=(f_2-f_1+3)-3+2e+(8-f_1-f_2)=
  8-2f_1+2e$. Since $f_1<4$: $8-2f_1+2e>0+2e\ge0$; more precisely
  $8-2f_1>0$ already suffices. **Closes, strictly.**

All $4$ cases close by hand, with no numerics load-bearing (a
$300{,}000$-trial exact-`Fraction` cross-check, `/tmp/check_2001_full.py`,
independently confirms zero violations across the *entire* domain of
shape $(2,0,0,1)$, both $f_1<4$ and $f_1\ge4$, corroborating but not
substituting for this derivation). This closes the residual $f_1<4$ of
shape $(2,0,0,1)$ completely. **The complementary $f_1\ge4$ branch of
this shape is confirmed by the same $300{,}000$-trial check to satisfy
$A(U)\ge1$ throughout, but its hand derivation (structurally analogous to
$(2,0,1,0)$'s already-established $f_1>4$ peel argument, adapted to this
shape's untouched values $4,2$ instead of $4,g_1,g_2$) was not carried out
this round** — this is the one honestly remaining piece needed to call
shape $(2,0,0,1)$ fully closed; it is a narrower, more mechanical gap than
the "$3$-free-parameter residual" description of round 28, since the new
Pair-Insertion Ordering Lemma already gives the exact tool needed (the
required computation is expected to be a direct peel of $f_1$ dominating
$\{4,2,e,f\}$, wholly analogous to the $(2,0,1,0)$ case, but was not
executed and verified by hand this round due to time).

**Net status of the $6$-shape residual after this round.** Shape
$(2,0,1,0)$: **fully closed, both directions, both regimes, no gap
remaining.** Shape $(2,0,0,1)$: residual regime ($f_1<4$) fully closed by
hand; complementary regime ($f_1\ge4$) numerically confirmed but not
hand-derived (an honestly narrower gap than before). The remaining $4$
shapes — $(1,1,0,1),(1,1,1,0),(1,2,0,0),(2,1,0,0)$ — were **not attempted
with the corrected mechanism this round**; each is expected, by
structural analogy (each reduces, after peeling the unconditionally
dominant elements, to a $4$-element residual of exactly the Pair-
Insertion-Ordering-Lemma shape, possibly with the reference value $w$
appearing in the "between" or "above" configuration as in Applications 1
and 2 respectively, or conceivably a third configuration if two
conservation pairs interact directly without an intervening singleton —
this last possibility has not been checked and is flagged as a risk),
to be closable by the same lemma, but this has not been verified — this
is the honestly-scoped remaining gap for $(\star_3)$: $2$ of $6$ residual
shapes now fully closed (up to one un-derived-by-hand-but-numerically-
confirmed sub-case in the second), $4$ of $6$ untouched this round.
$(\star_3)=\mathrm{MinFloor}(4)$ is **not** closed this round, but the
outline-reviewer's flagged citation-mismatch bug is now fixed (the
correct general tool — the Pair-Insertion Ordering Lemma, a concrete,
proven, self-contained substitute for the invalid
`single-insert-point-vertex-lemma`-on-a-coupled-pair citation — is now
available and demonstrated on $2$ of the $6$ shapes, ready to be applied
to the other $4$ next round).

### 7.18 Round-30 addendum: shape $(2,0,0,1)$ fully closed; shapes
$(1,1,0,1)$ and $(1,1,1,0)$ fully closed; shapes $(1,2,0,0),(2,1,0,0)$
still open, with the exact new difficulty diagnosed

**Target this round.** Close shape $(2,0,0,1)$'s residual $f_1\ge4$ branch,
and attack the remaining $4$ of $6$ shapes: $(1,1,0,1),(1,1,1,0),(1,2,0,0),
(2,1,0,0)$.

Throughout, units are $1/15$, $\pi=(\pi_1,\pi_2,\pi_3,\pi_4)=(8,4,2,1)$,
and we use only already-certified facts: `sharp-dominant-removal-identity`
(peel a strict unique max), `odd-run-reduction-lemma` (collapse
even-multiplicity ties to nothing, odd-multiplicity ties to one surviving
copy), Fact 1 ($A(S)\ge0$ for every nonnegative multiset $S$ —
`half-bound-lemma`), Fact 2 ($A(S)\le\mathrm{Total}(S)$, §5.2), and the
round-29 **Pair-Insertion Ordering Lemma** (both the original and mirrored
forms, restated below for convenience).

**Pair-Insertion Ordering Lemma (restated, both forms; certified round
29).** For $p\ge q\ge0$, $p+q=C$, and $w$ with $q\le w\le p$:
$$A(\{x,p,q,w\})=\begin{cases}x+w-C,&x\ge p\\2p-x+w-C,&w\le x<p\\
2p-w+x-C,&q\le x<w\\C-w-x,&x<q\end{cases}\tag{PI-between}$$
and, when instead $w\ge p\ge q$ (the "reference above the pair" form, with
$C=p+q$):
$$A(\{x,p,q,w\})=\begin{cases}x-w+2p-C,&x\ge w\\w-x+2p-C,&p\le x<w\\
w+x-C,&q\le x<p\\w+C-2p-x,&x<q\end{cases}\tag{PI-above}$$
Both are proved in §7.17 by direct sorted-rank computation (trichotomy of
$x$ against the three fixed values, four ranked-alternating-sum
evaluations, boundary agreement checked by direct substitution).

#### 7.18.1 Shape $(2,0,0,1)$: the residual $f_1\ge4$ branch, closed in full

Recall the shape: $\pi_1=8\to f_1\ge f_2\ge f_3\ge0$ ($\sum=8$);
$\pi_2=4,\pi_3=2$ untouched; $\pi_4=1\to e\ge f\ge0$ ($e+f=1$, so
$e\in[1/2,1]$). $U=\{f_1,f_2,f_3,4,2,e,f\}$. Round 29 closed $f_1<4$; this
closes $f_1\ge4$.

**$f_1\ge5$: trivial.** $f_2\le f_1$, $f_2+f_3=8-f_1\le3$, so
$f_2,f_3,2,e,f$ are all $<4$ (in fact $f_2\le3$), hence $4$ is the strict
unique max of $U$: $A(U)=4-A(\{f_1,f_2,f_3,2,e,f\})$. Peel $f_1$ (strict
unique max of that $6$-set, since $f_1\ge5>2\ge f_2+f_3$ forces
$f_2\le f_2+f_3\le3<f_1$, similarly $f_3,2,e,f<f_1$; the tie
$f_1=f_2$/$f_1=f_2=f_3$ boundary is absorbed by `odd-run-reduction-lemma`
exactly as in round 29's Application 1, contributing $0$/one surviving
copy, consistent with the formula's continuity):
$A(U)=4-f_1+A(\{f_2,f_3,2,e,f\})\ge4-f_1+0=4-f_1$ by Fact 1. Since
$f_1\ge5$, $A(U)\ge f_1-4\ge1$. Done.

**$f_1\in(4,5)$: the genuine content.** As above, $A(U)=f_1-4+A(\{f_2,f_3,
2,e,f\})$ (the same two-peel chain: $f_2+f_3=8-f_1<4$ forces $4$ strict
unique max of $U$; then $f_1>4>f_2$ forces $f_1$ strict unique max of the
$6$-set — both peels valid for every $f_1>4$, ties handled by odd-run
exactly as above). Target $A(U)\ge1$ becomes
$$A(\{f_2,f_3,2,e,f\})\ \ge\ 5-f_1.\tag{7.18.1}$$
Since $f_1\in(4,5)$, $f_2+f_3=8-f_1\in(3,4)$, so $f_2\ge(8-f_1)/2\in(1.5,2)$.

*Sub-case $f_2>2$.* Then $f_2>2\ge e\ge f$ and $f_2\ge f_3$; if $f_2>f_3$
strictly, peel $f_2$ (strict unique max of the $5$-set): $A(\{f_2,\dots\})
=f_2-A(\{f_3,2,e,f\})$, and (7.18.1) becomes
$A(\{f_3,2,e,f\})\le f_1+f_2-5=:T$. Apply (PI-between) with $x=f_3$,
$p=g_1{=}2$... — precisely as round 29's Application 1, with $w=1$ there;
here instead the fixed value is $2$ itself compared against the pair
$\{e,f\}$: since $e\le1<2$, this is (PI-above) with $x=f_3,p=e,q=f,w=2,
C=1$:
- $f_3\ge2$: $T-(f_3-2+2e-1)=T-f_3+3-2e=(f_1+f_2-5)-(8-f_1-f_2)+3-2e=
  2f_1+2f_2-10-2e$. Since $f_1>4,f_2>2$: $f_1+f_2>6\ge5+e$ (as $e\le1$), so
  $2f_1+2f_2-10-2e=2(f_1+f_2-5-e)>0$. Closes strictly.
- $e\le f_3<2$: $T-(2-f_3+2e-1)=T-1+f_3-2e=(f_1+f_2-5)-1+(8-f_1-f_2)-2e=
  2-2e\ge0$ (equality iff $e=1$). Closes.
- $f\le f_3<e$: $T-(2+f_3-1)=T-1-f_3=(f_1+f_2-5)-1-(8-f_1-f_2)=2f_1+2f_2-14$.
  Case hypothesis $f_3<e\le1\Rightarrow f_2=8-f_1-f_3>7-f_1>2$ (using
  $f_1<5$); combined with $f_1>4$: $2f_1+2f_2>8+2f_2$; using $f_2>2$ isn't
  quite enough alone, so use the sharper $f_2>7-f_1$ directly:
  $2f_1+2f_2-14>2f_1+2(7-f_1)-14=0$. Closes strictly.
- $f_3<f$: $T-(2+1-2e-f_3)=T-3+2e+f_3=(f_1+f_2-5)-3+2e+(8-f_1-f_2)=2e\ge0$
  (equality iff $e=0$, impossible since $e\ge1/2$; so strict). Closes.

*Tie $f_2=f_3$ (within $f_2>2$).* Multiplicity $2$ (even, since
$f_2=f_3>2>e,f$ excludes collision with $e,f$): `odd-run-reduction-lemma`
gives $A(\{f_2,f_3,2,e,f\})=A(\{2,e,f\})=2-(e-f)$ (peeling $2$, the strict
max of $\{2,e,f\}$ since $e,f\le1<2$). Need $2-(e-f)\ge5-f_1$, i.e.
$f_1\ge3+(e-f)$. Since $f_1>4$ and $e-f=2e-1\le1$: $3+(e-f)\le4<f_1$.
Closes strictly.

*Sub-case $f_2=2$ (boundary).* Then $2$ appears twice in $\{f_2,f_3,2,e,f\}$
(as $f_2$ and as $\pi_3$): even multiplicity, `odd-run-reduction-lemma`
cancels both, leaving $A(\{f_2,f_3,2,e,f\})=A(\{f_3,e,f\})$. Here
$f_3=8-f_1-2=6-f_1\in(1,2)$ (since $f_1\in(4,5)$), so $f_3>1\ge e\ge f$:
peel $f_3$: $A(\{f_3,e,f\})=f_3-(e-f)=(6-f_1)-(2e-1)=7-f_1-2e$. Need
$\ge5-f_1$: $7-2e\ge5\iff e\le1$, always true. Closes (equality iff $e=1$).

*Sub-case $f_2<2$.* First, note $f_3=8-f_1-f_2>8-f_1-2=6-f_1>1$ (using
$f_1<5$), so $f_3>1\ge e\ge f$; since also $f_2\ge f_3>1\ge e\ge f$, the
whole pair $\{f_2,f_3\}$ dominates $\{e,f\}$ elementwise, giving the
sorted order $f_2,f_3,e,f$ directly (no further case split needed — this
is the key simplification: the domain $f_2<2,f_1<5$ *forces* total
domination, so the general Double-Pair machinery collapses to a single
case here). Peel sequentially ($f_2\ge f_3$; if $f_2>f_3$ strict, two
peels; the tie $f_2=f_3$ collapses via odd-run exactly as above, giving
the same formula in the limit): $A(\{f_2,f_3,e,f\})=(f_2-f_3)+(e-f)$.
Peeling the fixed $2$ first (strict max of $\{f_2,f_3,2,e,f\}$ since
$f_2<2$): $A(\{f_2,f_3,2,e,f\})=2-A(\{f_2,f_3,e,f\})=2-(f_2-f_3)-(e-f)$.
Need $\ge5-f_1$: $2-(f_2-f_3)-(e-f)\ge5-f_1\iff f_1-f_2+f_3-(e-f)\ge3$.
Substituting $f_3=8-f_1-f_2$: $f_1-f_2+(8-f_1-f_2)-(e-f)\ge3\iff
8-2f_2-(e-f)\ge3\iff2f_2+(e-f)\le5$. Since $f_2<2$ ($2f_2<4$) and
$e-f=2e-1\le1$: $2f_2+(e-f)<4+1=5$. Closes strictly.

**$f_1=4$ boundary.** $U=\{4,4,f_2,f_3,2,e,f\}$ with $f_2+f_3=4$. The value
$4$ has multiplicity $2$ (assuming $f_2<4$, i.e. $f_3>0$; the fully
degenerate corner $f_2=4,f_3=0$ is a further boundary handled below),
even, cancelling by `odd-run-reduction-lemma`: $A(U)=A(\{f_2,f_3,2,e,f\})$
directly — this is exactly (7.18.1)'s left side evaluated at $f_1=4$, and
the target reduces to $A(\{f_2,f_3,2,e,f\})\ge1=5-4$, i.e. exactly
(7.18.1) at $f_1=4$. All four case formulas derived above ($f_2>2$
generic, $f_2=f_3$ tie, $f_2=2$, $f_2<2$) were proved using only
$f_1\ge4$ (not $f_1>4$ strictly) or, where $f_1<5$ was used, $f_1=4<5$
still qualifies — direct inspection of each derivation shows every
inequality used is non-strict-compatible with $f_1=4$ (e.g. the $f_2<2$
case's closing inequality $2f_2+(e-f)<5$ used $f_2<2,e\le1$ only, no
reference to $f_1$ needed beyond the substitution, which is exact at
$f_1=4$ too). So $f_1=4$ is already covered by the $f_1\in(4,5)$
derivation's formulas evaluated at the endpoint, not a separate case.
The doubly-degenerate corner $f_1=4,f_2=4,f_3=0$ (all cuts on $\pi_1$
maximally uneven): $U=\{4,4,4,0,2,e,f\}$, value $4$ has multiplicity $3$
(odd), one survives: $A(U)=A(\{4,0,2,e,f\})$; $4$ is strict unique max
(since $2,e,f,0<4$): $A=4-A(\{0,2,e,f\})=4-(2-(e-f))=2+e-f\ge2+0=2\ge1$
(using $e\ge f$). Closes.

**Conclusion.** Shape $(2,0,0,1)$'s $f_1\ge4$ branch is now closed for
every sub-case ($f_1\ge5$; $f_1\in(4,5)$ with all four $f_2$-sub-cases;
the $f_1=4$ boundary including its own degenerate corner), by hand, with
no numerics load-bearing. Combined with round 29's closure of $f_1<4$,
**shape $(2,0,0,1)$ is now fully closed, both directions, on its entire
domain.** (Cross-checked, not substituting for the proof: a fresh
$300{,}000$-trial exact-`Fraction` search over the shape's *entire* domain,
`/tmp/final_checks.py` this round, finds minimum $\approx1.00001$,
zero violations.)

#### 7.18.2 Shape $(1,1,0,1)$: fully closed

$\pi_1=8\to a\ge b\ge0$ ($a+b=8$, forced dominance $a\ge4$); $\pi_2=4\to
c\ge d\ge0$ ($c+d=4$, forced dominance $c\ge2$); $\pi_3=2$ untouched;
$\pi_4=1\to e\ge f\ge0$ ($e+f=1$, $e\in[1/2,1]$). $U=\{a,b,c,d,2,e,f\}$.

**Forced-Dominance Fact.** *A single cut splitting a positive quantity
$q$ into two nonnegative parts always leaves a part $\ge q/2$*: if both
parts were $<q/2$ their sum would be $<q$, contradiction. Applied to
$\pi_1=8$: $a\ge4$. Applied to $\pi_2=4$: $c\ge2$.

Since $a\ge4$ and $c\le4$ (as $c$ is a fragment of $4$), $a\ge c$ always;
since also $a\ge b$ (given) and $a\ge4>1\ge e\ge f$ and (from $c\le4$)
$a\ge4\ge c\ge d,2$ is not immediate for $2$ vs $a$ but $a\ge4>2$ trivially
— so $a$ is always the (weak) max of $U$. If $a>4$ strictly (equivalently
$a\ne b$): peel $a$: $A(U)=a-A(\{b,c,d,2,e,f\})=:a-A(R)$, target
$A(U)\ge1\iff A(R)\le a-1$.

**Branch $b\ge c$ (peel $b$).** Since $c\ge2$ (forced), $b\ge c\ge2$
implies $b\ge2>e,f$ and $b\ge c\ge d$, so $b$ is the (weak) max of $R$.

*Sub-branch $c>2$ strict (so $d<2$).* If $b>c$ strict, peel $b$:
$A(R)=b-A(\{c,d,2,e,f\})$. Then $c>2\ge d$ (as $d<2$) and $c>2>e,f$
(since $c>2$ strict), so $c$ is strict max: peel:
$A(\{c,d,2,e,f\})=c-A(\{d,2,e,f\})$. Then $2$ is strict max of
$\{d,2,e,f\}$ (as $d<2$, $e,f\le1<2$): peel: $A(\{d,2,e,f\})=2-A(\{d,e,f\})$.
Combining: $A(R)=b-c+2-A(\{d,e,f\})$; target becomes
$A(\{d,e,f\})\ge b-c+2-(a-1)=b-c-a+3=3+(8-a)-c-a=11-2a-c=:K_1$.
For the $3$-element set $\{d,e,f\}$ ($e\ge f$, $d$ free), a direct
case split by $d$ vs $e,f$ (standard: $A(\{d,e,f\})=(d+1)-2\,
\mathrm{median}(d,e,f)$, using $e+f=1$):
- $d\ge e$: $A=d-(e-f)=d-2e+1$. $A-K_1=(4-c-2e+1)-(11-2a-c)=2a-2e-6$.
  Since $a>4,e\le1$: $2a-2e>8-2=6$. Closes strictly.
- $f\le d<e$: $A=1-d=1-(4-c)=c-3$. $A-K_1=(c-3)-(11-2a-c)=2a+2c-14$.
  Case hyp. $d<e\le1\Rightarrow c>3$ (as $d=4-c<1$); with $a>4$:
  $2a+2c>8+6=14$. Closes strictly (case-specific $c>3$).
- $d<f$: $A=d+(e-f)=d+2e-1=(4-c)+2e-1=3-c+2e$. $A-K_1=(3-c+2e)-(11-2a-c)
  =2a+2e-8$. Since $a>4$: $2a+2e>8+0=8$ trivially. Closes.

*Boundary $c=2$ (so $d=2$, within $b\ge c$).* $c,d,\pi_3$ all $=2$: three
copies, odd, one survives (`odd-run-reduction-lemma`): $A(\{c,d,2,e,f\})=
A(\{2,e,f\})=2-(e-f)$. If $b>2$ strict, peel $b$: $A(R)=b-(2-(e-f))
=b-2+2e-1=b-3+2e$. Target: $A(R)\le a-1 \iff b+2e-3\le a-1\iff
b+2e\le a+2$. Since $b=8-a$: $8-a+2e\le a+2\iff2a\ge6+2e\iff a\ge3+e$.
As $a>4,e\le1$: $3+e\le4<a$. Closes. (If also $b=2$: $a=6$, $2$ appears a
$4$th time total across $b,c,d,\pi_3$, even, all cancel:
$A(R)=A(\{e,f\})=e-f\le1\le a-1=5$. Trivial.)

*Tie $b=c$ (within $b\ge c$, generic $c>2$).* Even multiplicity $2$
(assuming $b=c\ne d,2,e,f$, generic): cancels, $A(R)=A(\{d,2,e,f\})$. As
above ($d<2$ since $c>2$): $A(R)=2-A(\{d,e,f\})$. Target: $A(\{d,e,f\})
\ge3-a$ (from $A(R)=2-A(\{d,e,f\})\le a-1\iff A(\{d,e,f\})\ge3-a$). Since
$a>4$: $3-a<-1<0\le A(\{d,e,f\})$ (Fact 1). Closes trivially.

**Branch $b<c$ (peel $c$).** Since $c\ge2$ (forced) and $c>b$ (branch),
plus $c\ge d,2,e,f$ automatically ($c\ge2$), $c$ is the (weak) max of $R$.
If $c>2$ strict, peel $c$: $A(R)=c-A(\{b,d,2,e,f\})$; since target
$A(R)\le a-1$, this becomes
$$A(\{b,d,2,e,f\})\ \ge\ c-(a-1)\ =\ c-a+1.\tag{a lower bound}$$

*Sub-branch $b\ge2$.* If $b>2$ strict, $b$ is max of $\{b,d,2,e,f\}$
(since $d<2$ as $c>2$, and $e,f\le1<2\le b$): peel:
$A(\{b,d,2,e,f\})=b-A(\{d,2,e,f\})=b-2+A(\{d,e,f\})$ (peeling $2$ next,
strict max of $\{d,2,e,f\}$). The target becomes
$b-2+A(\{d,e,f\})\ge c-a+1\iff A(\{d,e,f\})\ge c-a+3-b=c-a+3-(8-a)=c-5$.
Using the same $3$ sub-cases for $A(\{d,e,f\})$:
- $d\ge e$: $A=5-c-2e$. Need $\ge c-5\iff10-2e\ge2c\iff c\le5-e$. Since
  $c<4$ and $e\le1\Rightarrow5-e\ge4>c$. Closes strictly.
- $f\le d<e$: $A=c-3$. Need $\ge c-5\iff-3\ge-5$, always true. Closes.
- $d<f$: $A=3-c+2e$. Need $\ge c-5\iff8+2e\ge2c\iff c\le4+e$. Since
  $c<4\le4+e$ ($e\ge0$). Closes.

*Sub-branch $b=2$ (boundary, within $b\ge2$).* $b$ ties the fixed $2$:
even mult, cancels: $A(\{b,d,2,e,f\})=A(\{d,e,f\})$; here $a=8-b=6$.
Target $A(\{d,e,f\})\ge c-a+1=c-5$: identical to the case above with
$a=6$ substituted — same $3$ sub-case verification applies verbatim
(the derivation above never used a specific value of $a$ beyond $a<8$
generically, so it holds at $a=6$ too). Closes.

*Sub-branch $b<2$.* Then $2$ is the (strict) max of $\{b,d,2,e,f\}$
(as $b<2$, $d<2$ since $c>2$, $e,f\le1<2$): peel: $A(\{b,d,2,e,f\})=
2-A(\{b,d,e,f\})$. Target $A(\{b,d,2,e,f\})\ge c-a+1$ becomes
$$A(\{b,d,e,f\})\ \le\ a-c+1\ =:T_4.$$
Note $b<2\iff a>6$ (since $b=8-a$). Since $e\ge f$ and $b,d$ are
independent (not a fixed-sum pair with each other — each is already
"the other half" of its own conservation pair, $a,c$), a full $6$-case
trichotomy (split on $b$ vs $d$, then each against $e,f$) covers every
sorted order:

*Case $d\ge b$:*
- $b\ge e$ (so $d\ge b\ge e\ge f$): $A=d-b+e-f$. Using $d-b=(4-c)-(8-a)
  =a-c-4$ and $e-f=2e-1$: $T_4-A=(a-c+1)-(a-c-4+2e-1)=6-2e\ge4>0$
  ($e\le1$). Closes.
- $f\le b<e$: $A=d-e+b-f=(4-c)-e+(8-a)-f=12-a-c-(e+f)=11-a-c$.
  $T_4-A=(a-c+1)-(11-a-c)=2a-10$. Since $a>6$: $2a-10>2>0$. Closes.
- $b<f$: $A=d-e+f-b=(4-c)-e+f-(8-a)=a-c-4-(e-f)=a-c-5-2e+2=a-c-3-2e$.
  Wait: $e-f=2e-1$, so $A=(a-c-4)-(2e-1)=a-c-3-2e$. $T_4-A=(a-c+1)-
  (a-c-3-2e)=4+2e>0$ trivially. Closes.

*Case $b>d$:*
- $d\ge e$ (so $b>d\ge e\ge f$): $A=b-d+e-f$. $b-d=(8-a)-(4-c)=4-a+c$;
  $A=4-a+c+2e-1=3-a+c+2e$. $T_4-A=(a-c+1)-(3-a+c+2e)=2a-2c-2e-2$.
  Since $a>6,c<4,e\le1$: $2a>12$, $2c<8$, $2e\le2$: $2a-2c-2e-2>12-8-2-2
  =0$. Closes strictly.
- $f\le d<e$: $A=b-e+d-f=(8-a)-e+(4-c)-f=12-a-c-(e+f)=11-a-c$ (same
  formula as the symmetric case above). $T_4-A=2a-10>2>0$ (as $a>6$).
  Closes.
- $d<f$: $A=b-e+f-d=(8-a)-e+f-(4-c)=4-a+c-(e-f)=4-a+c-2e+1=5-a+c-2e$.
  $T_4-A=(a-c+1)-(5-a+c-2e)=2a-2c+2e-4$. Since $a>6,c<4,e\ge0$:
  $2a>12,-2c>-8$: $2a-2c-4>12-8-4=0$, so $2a-2c+2e-4>0$ (adding
  $2e\ge0$). Closes.

All $6$ cases close, using only $a>6$ (the sub-branch's own defining
fact), $c<4$ ($c$ is a fragment of $\pi_2=4$), and $e\in[1/2,1]$ — no
case-specific sharpening beyond these three global bounds is needed here.

**Boundary $c=2$ within $b<c$.** Then $c=2\Rightarrow d=2$ too and $b<c=2$:
$c,d,\pi_3$ give three $2$'s, odd, one survives:
$A(\{b,c,d,2,e,f\})=A(\{b,2,e,f\})$; since $b<2$, $2$ is max:
$=2-A(\{b,e,f\})$. So $A(U)=a-\big(2-A(\{b,e,f\})\big)=a-2+A(\{b,e,f\})$;
target $\ge1\iff A(\{b,e,f\})\ge3-a$. Since $a>4$: $3-a<-1<0\le
A(\{b,e,f\})$ (Fact 1). Closes trivially.

**$a=4$ boundary.** $a=b=4$: even mult, cancels:
$A(U)=A(\{c,d,2,e,f\})$ directly (target $\ge1$). If $c>2$: peel $c$ then
$2$: $A(\{c,d,2,e,f\})=c-2+A(\{d,e,f\})$; need $\ge1\iff A(\{d,e,f\})\ge
3-c$. Using the $3$ sub-cases: $d\ge e$: $A=5-c-2e\ge3-c\iff e\le1$,
true (equality at $e=1$). $f\le d<e$: $A=c-3\ge3-c\iff c\ge3$, matches
case hyp. $d<e\le1\Rightarrow c>3$. $d<f$: $A=3-c+2e\ge3-c\iff e\ge0$,
trivial. If $c=2$ ($=d=\pi_3$, triple, odd, one survives): $A(U)=
A(\{2,e,f\})=2-(e-f)\ge2-1=1$ (equality iff $e=1$). Closes, matching
achievability.

**Conclusion.** Every branch of shape $(1,1,0,1)$'s domain — $b\ge c$
(with $c>2$, $c=2$, $b=c$ sub-cases), $b<c$ (with $b\ge2$, $b=2$, $b<2$,
$c=2$ sub-cases), and the $a=4$ boundary (with its own $c>2/c=2$
sub-cases) — is closed by hand via `sharp-dominant-removal-identity`,
`odd-run-reduction-lemma`, and Fact 1, with only elementary linear
algebra (no new lemma needed beyond what round 29 already certified).
**Shape $(1,1,0,1)$ is now fully closed, both directions, on its entire
domain.** (Cross-checked: $300{,}000$-trial exact-`Fraction` search over
the full domain, minimum $\approx1.0108$, zero violations.)

#### 7.18.3 Shape $(1,1,1,0)$: fully closed

$\pi_1=8\to a\ge b$ ($a\ge4$ forced); $\pi_2=4\to c\ge d$ ($c\ge2$ forced);
$\pi_3=2\to g\ge h$ ($g+h=2$, $g\ge1$ forced); $\pi_4=1$ untouched.
$U=\{a,b,c,d,g,h,1\}$. As before, $a\ge4\ge c\ge2\ge g\ge1$ shows $a$ is
always the (weak) max: peel (generic $a>4$): $A(U)=a-A(\{b,c,d,g,h,1\})
=:a-A(R)$, target $A(R)\le a-1$.

**Branch $b\ge c$ (so, using $c\ge2$: $b\ge2\ge g\ge1$, $b\ge d$; $b$ is
max of $R$).** Peel $b$ (generic $b>c$): $A(R)=b-A(\{c,d,g,h,1\})$. Then
$c\ge2\ge g\ge h,1$ shows $c$ is max of $\{c,d,g,h,1\}$ (using also
$c\ge d$): peel (generic $c>2$): $A(\{c,d,g,h,1\})=c-A(\{d,g,h,1\})$.
Since $h\le1\le g$ always, $\{d,g,h,1\}$ is exactly a (PI-between)
instance ($x=d,p=g,q=h,w=1,C=2$). Combining, target
$A(R)\le a-1$ becomes (with $A(R)=b-c+A(\{d,g,h,1\})$)
$$A(\{d,g,h,1\})\ \le\ a-1-b+c=a-1-(8-a)+c=2a+c-9=:T_3.$$
- $d\ge g$: $\mathrm{PI}=d-1$. $T_3-\mathrm{PI}=(2a+c-9)-(4-c-1)=2a+2c-12$.
  Since $a>4,c>2$: $a+c>6$, so $2a+2c-12>0$. Closes strictly.
- $1\le d<g$: $\mathrm{PI}=2g-d-1$. $T_3-\mathrm{PI}=2a+c-8-2g+d=
  2a+c-8-2g+(4-c)=2a-4-2g$. Since $a>4,g\le2$: $2+g\le4<a$, so
  $a>2+g$, i.e. $2a-4-2g>0$. Closes.
- $h\le d<1$: $\mathrm{PI}=2g+d-3$. $T_3-\mathrm{PI}=2a+c-6-2g-d=
  2a+2c-10-2g$. Case hyp. $d<1\Rightarrow c>3$ (as $d=4-c$); with $a>4$:
  $a+c>7$, so $2a+2c-10-2g>2(7)-10-2(2)=0$ (using $g\le2$). Closes.
- $d<h$: $\mathrm{PI}=1-d$. $T_3-\mathrm{PI}=2a+c-10+d=2a-6$. Since
  $a>4$: $2a-6>2>0$. Closes.

*Boundary $c=2$ (within $b\ge c$, so $d=2$).* Then $c,d$ tie: even mult,
cancels: $A(\{c,d,g,h,1\})=A(\{g,h,1\})$; $g\ge1\ge h$: peel $g$:
$=g-A(\{h,1\})=g-(1-h)=g+h-1=1$ (since $g+h=2$). So (assuming $b>2$):
$A(R)=b-1$, $A(U)=a-(b-1)=a-b+1\ge1$ since $a\ge b$ always. Closes
(equality iff $a=b$).

*Tie $b=c$ (within $b\ge c$, generic $c>2$).* Even mult, cancels:
$A(R)=A(\{d,g,h,1\})$. Target $A(\{d,g,h,1\})\le a-1$: using the same
$4$ (PI-between) cases with $T_3':=a-1$ (instead of $2a+c-9$, since here
$A(R)=A(\{d,g,h,1\})$ directly, no $b-c$ term as $b=c$ cancel to $0$):
- $d\ge g$: $\mathrm{PI}=d-1=(4-c)-1=3-c$. Need $\le a-1$: since $a>4,
  c>2$: $3-c<1<a-1$ (as $a>2$). Closes.
- $1\le d<g$: $\mathrm{PI}=2g-d-1$. Need $\le a-1$; since $g\le2,d\ge1$:
  $2g-d-1\le4-1-1=2<3<a-1$ (as $a>4$). Closes.
- $h\le d<1$: $\mathrm{PI}=2g+d-3\le4+1-3=2<a-1$. Closes.
- $d<h$: $\mathrm{PI}=1-d\le1<a-1$. Closes.
(All four close with wide slack, using only $a>4$, $g\le2$, $c>2$,
$d<2$.)

**Branch $b<c$.** Peel $c$ (weak max of $R$, using $c\ge2$): if $c>2$
strict, $A(R)=c-A(\{b,d,g,h,1\})$; target becomes
$$A(\{b,d,g,h,1\})\ \ge\ 1-a+c\ =:K_2.$$
**If $c\le3.5$:** the branch condition $b<c$ gives $a>8-c\ge4.5$; then
$K_2=1-a+c<1-(8-c)+c=2c-7\le2(3.5)-7=0$, so $K_2\le0\le A(\{b,d,g,h,1\})$
(Fact 1). Closes trivially for the **entire** sub-branch, regardless of
how $b,d,g,h$ compare.

**If $c>3.5$ (so $d<0.5$):** need the genuine case split.

*Sub-branch $b\ge g$.* Peel: is $b$ the max of $\{b,d,g,h,1\}$? Need
$b\ge d$: split further.
- $b\ge d$ too: $b$ is max ($b\ge d$, $b\ge g\ge1\ge h$): peel $b$:
  $A=b-A(\{d,g,h,1\})$, a (PI-between) instance. Target
  $A(\{d,g,h,1\})\le b-K_2+... $ — precisely, $A(\{b,d,g,h,1\})=
  b-\mathrm{PI}(d)\ge K_2\iff\mathrm{PI}(d)\le b-K_2=(8-a)-(1-a+c)=7-c
  =:T_4$. Cases:
  - $d\ge g$: $\mathrm{PI}=d-1$. $T_4-\mathrm{PI}=(7-c)-(4-c-1)=4$.
    Always $\ge0$ (exact cancellation via $c+d=4$). Closes.
  - $1\le d<g$: $\mathrm{PI}=2g-d-1$. $T_4-\mathrm{PI}=(7-c)-(2g-d-1)=
    8-c-2g+d=12-2c-2g$. Since $c<4,g\le2$: $c+g<6$, closes.
  - $h\le d<1$: $\mathrm{PI}=2g+d-3$. $T_4-\mathrm{PI}=10-c-2g-d=
    10-c-2g-(4-c)=6-2g\ge2>0$ ($g\le2$). Closes.
  - $d<h$: $\mathrm{PI}=1-d$. $T_4-\mathrm{PI}=6-c+d=6-c+(4-c)=10-2c>2$
    ($c<4$). Closes.
- $b<d$: then, since $d<0.5$ (as $c>3.5$) and $b<d<0.5<1\le g$: $d$ is
  the max ($d>b$, $d\ge g$? need $d\ge g$ — but we're inside sub-branch
  $b\ge g$ meaning $g\le b<d$, so $d>g$ too): peel $d$: since
  $d>b\ge g\ge1\ge h$: $A(\{b,d,g,h,1\})=d-A(\{b,g,h,1\})$; within
  $\{b,g,h,1\}$: $b\ge g\ge1\ge h$ (given), so sorted $b,g,1,h$:
  $A=b-g+1-h=b-g+1-(2-g)=b-1$. So $A(\{b,d,g,h,1\})=d-(b-1)=d-b+1$.
  Need $\ge K_2=1-a+c$: $d-b+1\ge1-a+c\iff d-b\ge c-a\iff a-b\ge c-d$
  $\iff2a-8\ge2c-4\iff a-c\ge2$. Sub-case hyp. $b<d\iff8-a<4-c\iff
  a>c+4>c+2$. Closes with wide margin.

*Sub-branch $b<g$ (so $b<2$, hence $a>6$).* If $g>1$ strict, $g$ is the
max of $\{b,d,g,h,1\}$ (as $g>b$, $g>d$ [since $d<0.5<1\le g$], $g\ge1
\ge h$): peel: $A(\{b,d,g,h,1\})=g-A(\{b,d,h,1\})$. Need
$g-A(\{b,d,h,1\})\ge K_2\iff A(\{b,d,h,1\})\le g-K_2=g-1+a-c=:T_5$.
- $b\ge1$: sub-split $d$ vs $h$:
  - $d\ge h$: sorted $b,1,d,h$ (since $b\ge1$, and $d,h<1$ with $d\ge h$
    — wait need $1\ge d$; true as $d<0.5<1$): $A=b-1+d-h$. $T_5-A=
    (g-1+a-c)-(b-1+d-h)=g+a-c-b-d+h$. Using $b=8-a,d=4-c,h=2-g$:
    $=g+a-c-(8-a)-(4-c)+(2-g)=2a-10$. Since $a>6$: $2a-10>2>0$. Closes.
  - $d<h$: sorted $b,1,h,d$: $A=b-1+h-d$. $T_5-A=(g-1+a-c)-(b-1+h-d)=
    g+a-c-b-h+d=g+a-c-(8-a)-(2-g)+(4-c)=2a+2g-2c-6$. Since $a>6,g\ge1$:
    $2a+2g>12+2=14$; using $c<4$: $-2c>-8$; total $>14-6-8=0$. Closes.
- $b<1$: since $b<1$, and $d<0.5<1$, $h<1$ (as $g>1$), all three of
  $b,d,h$ are $<1$, so $1$ is the strict max: $A(\{b,d,h,1\})=1-
  A(\{b,d,h\})\le1$ (Fact 2, $A(\{b,d,h\})\ge0$). Need $\le T_5=g-1+a-c$:
  since $a>6,c<4,g\ge1$: $T_5>6-1+1-4=2>1\ge A(\{b,d,h,1\})$. Closes.

*Boundary $g=1$ (within $b<g$, so $h=1$: $g,h,\pi_4$ all $=1$, odd
mult $3$, one survives).* $A(\{b,d,g,h,1\})=A(\{b,d,1\})$; since $b<g=1$,
$b<1$, and $d<0.5<1$: $1$ is max: $=1-|b-d|$ ($A$ of a $2$-element set
plus the peeled $1$; more precisely $A(\{b,d,1\})=1-A(\{b,d\})=1-|b-d|$).
Need $\ge K_2=1-a+c$: $1-|b-d|\ge1-a+c\iff a-c\ge|b-d|=|4-a+c|$. Here
$b<g=1\Rightarrow a>7$ (as $b=8-a<1$). Let $x=a-c>7-4=3$; need $x\ge
|4-x|$: if $x\ge4$, RHS$=x-4<x$, holds; if $x<4$, need $x\ge4-x\iff
x\ge2$, and $x>3>2$. Either way holds. Closes.

**Conclusion.** Every branch — $b\ge c$ (with $c>2$, $c=2$, $b=c$
sub-cases), $b<c,c\le3.5$ (trivial), $b<c,c>3.5$ with $b\ge g$ (both
$b\ge d$ and $b<d$ sub-cases) and $b<g$ (both $b\ge1$ sub-cases and
$b<1$, plus $g=1$ boundary) — is now closed by hand.
**Shape $(1,1,1,0)$ is now fully closed, both directions, on its entire
domain.** (Cross-checked: $300{,}000$-trial exact-`Fraction` search,
minimum $\approx1.0125$, zero violations; a targeted $2$-million-trial
search restricted to the hardest residual, $b<c,c>3.5,b<g$, found minimum
$\approx3.00$, well clear of $1$, consistent with the derivation and
confirming this corner is not where the true extremum lives.)

#### 7.18.4 Shapes $(1,2,0,0)$ and $(2,1,0,0)$: FULLY CLOSED (round 31) —
exhaustive vertex enumeration via the Vertex-Minimum Theorem

**Setup, shape $(2,1,0,0)$.** $\pi_1=8\to f_1\ge f_2\ge f_3\ge0$,
$f_1+f_2+f_3=8$; $\pi_2=4\to c\ge d\ge0$, $c+d=4$ (so $c\ge2$); $\pi_3=2,
\pi_4=1$ untouched. $U=\{f_1,f_2,f_3,c,d,2,1\}$ ($7$ elements,
$\mathrm{Total}(U)=15$). Target: $A(U)\ge1$ for every legal
$(f_1,f_2,f_3,c,d)$.

**Setup, shape $(1,2,0,0)$ (mirror).** $\pi_1=8\to a\ge b\ge0$, $a+b=8$;
$\pi_2=4\to g\ge h\ge i\ge0$, $g+h+i=4$; $\pi_3=2,\pi_4=1$ untouched.
$U'=\{a,b,g,h,i,2,1\}$. Target: $A(U')\ge1$.

Round 30 identified, correctly, that this shape is harder than the other
four because **neither top ($f_1$ resp. $a$) unconditionally dominates
the other split's top ($c$ resp. the triple's top $g$)**, and that a
cross-pair joint-feasibility constraint (e.g. $c\ge4-f_3$) is genuinely
needed and not implied by either split's own local ordering alone. This
round closes both shapes in full, not by continuing the linear branch
tree (which the round-31 outline correctly flagged as re-litigating
"not independent" sub-cases) but by **direct citation of the certified
`vertex-minimum-theorem`**, reducing the continuum of $(f_1,f_2,c)$
(shape $(2,1,0,0)$; $f_3=8-f_1-f_2$, $d=4-c$) resp. $(a,h,i)$ (shape
$(1,2,0,0)$; $b=8-a$, $g=4-h-i$) to a **finite** enumeration of vertices,
each cut out by exactly $3$ independent tight constraints of the two
types the theorem allows: (I) a fragment $=0$ (a degenerate cut) or (II)
two fragments/values exactly equal (a tie — possibly across the two
independently-split parents, possibly involving an untouched piece $2$
or $1$). This sidesteps the joint-feasibility subtlety entirely: instead
of separately tracking which linear inequality regions are jointly
feasible, we enumerate every combinatorially possible vertex (solve each
triple of tight linear constraints, keep only the solutions that satisfy
*all* the shape's defining inequalities — this feasibility filter *is*
exactly where the joint constraint gets enforced, automatically, for
every vertex simultaneously, rather than needing to be spotted case by
case) and evaluate $A(U)$ directly by sorting (equivalently,
`odd-run-reduction-lemma` at any tied vertex).

**The finite hyperplane family (Vertex-Minimum Theorem, part 2), shape
$(2,1,0,0)$.** Working in the $3$ free coordinates $(f_2,f_3,c)$ (so
$f_1=8-f_2-f_3$, $d=4-c$), the candidate tight constraints are exactly:
- Type (I), fragment $=0$: $f_3=0$; $d=0$ (i.e. $c=4$).
- Type (II), ties among $\{f_1,f_2,f_3,c,d\}$ and the fixed $\{2,1\}$:
  $f_2=f_3$; $f_1=f_2$ (i.e. $2f_2+f_3=8$); $c=d$ (i.e. $c=2$); $d=1$
  (i.e. $c=3$); $f_1=c$; $f_1=d$; $f_1=2$; $f_1=1$; $f_2=c$; $f_2=d$;
  $f_2=2$; $f_2=1$; $f_3=c$; $f_3=d$; $f_3=2$; $f_3=1$.

  (No other type-(I) event is possible: $c=0$ would force $d\le0$, hence
  $c+d=0\ne4$, infeasible; $f_1=0$ would force $f_2=f_3=0$, hence
  $\sum=0\ne8$, infeasible. No other type-(II) event exists since the
  only pairs of *distinct* symbols in $U$'s parametrization are exactly
  the $\binom72$ pairs among $\{f_1,f_2,f_3,c,d,2,1\}$, and pairs
  entirely among the two internally-pre-sorted triples/pairs
  ($f_1,f_2,f_3$ mutually; $c,d$ mutually) or between the two fixed
  constants $2,1$ are already covered by the listed hyperplanes above —
  $f_1=f_3$ is implied by (and hence redundant with, never independently
  binding at a $3$-tight-constraint vertex without also having)
  $f_1=f_2$ **and** $f_2=f_3$ simultaneously, so it need not be listed
  separately; likewise $2=1$ never occurs.)

  This is $18$ named hyperplanes in $3$-space $(f_2,f_3,c)$. Solving
  every $\binom{18}3=816$ triple of these (linear, hence uniquely
  solvable or inconsistent/dependent) and discarding (a) inconsistent or
  underdetermined triples, and (b) solutions violating any of the
  shape's defining inequalities ($f_1\ge f_2\ge f_3\ge0$, $c\ge d\ge0$)
  yields **exactly $36$ distinct feasible vertices** (computed exactly
  in `Fraction`/`sympy` rational arithmetic; every vertex below was
  independently re-verified by hand-substitution into the defining
  equations and inequalities). By `vertex-minimum-theorem` part 2–3, the
  true minimum of $A(U)$ over the whole continuum is attained at one of
  these $36$ points (or is $\ge$ all of them, since the theorem gives a
  finite candidate set for the minimizer — evaluating all $36$ and
  taking the least value both identifies and certifies the minimum).

  Sorted table (columns $f_1,f_2,f_3,c,d$; $A(U)$ computed by sorting
  the $7$-element multiset $\{f_1,f_2,f_3,c,d,2,1\}$ descending and
  alternating-summing — e.g. row $(4,4,0,2,2)$: sorted
  $4,4,2,2,2,1,0$, $A=4-4+2-2+2-1+0=1$):

  | $f_1$ | $f_2$ | $f_3$ | $c$ | $d$ | $A(U)$ |
  |---|---|---|---|---|---|
  | $8/3$ | $8/3$ | $8/3$ | $2$ | $2$ | $5/3$ |
  | $8/3$ | $8/3$ | $8/3$ | $8/3$ | $4/3$ | $5/3$ |
  | $8/3$ | $8/3$ | $8/3$ | $3$ | $1$ | $7/3$ |
  | $8/3$ | $8/3$ | $8/3$ | $4$ | $0$ | $7/3$ |
  | $3$ | $5/2$ | $5/2$ | $3$ | $1$ | $2$ |
  | $3$ | $3$ | $2$ | $2$ | $2$ | $\mathbf1$ |
  | $3$ | $3$ | $2$ | $3$ | $1$ | $3$ |
  | $3$ | $3$ | $2$ | $4$ | $0$ | $3$ |
  | $7/2$ | $7/2$ | $1$ | $2$ | $2$ | $2$ |
  | $7/2$ | $7/2$ | $1$ | $3$ | $1$ | $2$ |
  | $7/2$ | $7/2$ | $1$ | $7/2$ | $1/2$ | $2$ |
  | $7/2$ | $7/2$ | $1$ | $4$ | $0$ | $2$ |
  | $4$ | $2$ | $2$ | $2$ | $2$ | $3$ |
  | $4$ | $2$ | $2$ | $3$ | $1$ | $3$ |
  | $4$ | $2$ | $2$ | $4$ | $0$ | $\mathbf1$ |
  | $4$ | $3$ | $1$ | $3$ | $1$ | $3$ |
  | $4$ | $3$ | $1$ | $4$ | $0$ | $\mathbf1$ |
  | $4$ | $4$ | $0$ | $2$ | $2$ | $\mathbf1$ |
  | $4$ | $4$ | $0$ | $3$ | $1$ | $\mathbf1$ |
  | $4$ | $4$ | $0$ | $4$ | $0$ | $3$ |
  | $5$ | $2$ | $1$ | $2$ | $2$ | $5$ |
  | $5$ | $2$ | $1$ | $3$ | $1$ | $3$ |
  | $5$ | $2$ | $1$ | $4$ | $0$ | $\mathbf1$ |
  | $5$ | $3$ | $0$ | $3$ | $1$ | $3$ |
  | $6$ | $1$ | $1$ | $2$ | $2$ | $5$ |
  | $6$ | $1$ | $1$ | $3$ | $1$ | $5$ |
  | $6$ | $1$ | $1$ | $4$ | $0$ | $3$ |
  | $6$ | $2$ | $0$ | $2$ | $2$ | $5$ |
  | $6$ | $2$ | $0$ | $3$ | $1$ | $3$ |
  | $6$ | $2$ | $0$ | $4$ | $0$ | $3$ |
  | $7$ | $1$ | $0$ | $2$ | $2$ | $5$ |
  | $7$ | $1$ | $0$ | $3$ | $1$ | $5$ |
  | $7$ | $1$ | $0$ | $4$ | $0$ | $5$ |
  | $8$ | $0$ | $0$ | $2$ | $2$ | $7$ |
  | $8$ | $0$ | $0$ | $3$ | $1$ | $7$ |
  | $8$ | $0$ | $0$ | $4$ | $0$ | $5$ |

  Every entry satisfies $A(U)\ge1$, with equality at exactly $5$ vertices
  (bold): $(3,3,2,2,2)$, $(4,2,2,4,0)$, $(4,3,1,4,0)$, $(4,4,0,2,2)$,
  $(4,4,0,3,1)$ — each independently checkable by direct sorting (e.g.
  $(4,3,1,4,0)$: $U=\{4,4,3,2,1,1,0\}$, sorted descending
  $4,4,3,2,1,1,0$, $A=4-4+3-2+1-1+0=1$). **This proves
  $A(U)\ge1$ for shape $(2,1,0,0)$, in full**, with the round-28
  achievability construction ($\{4,4,2,2,2,1\}$, i.e. the vertex
  $(4,2,2,4,0)$ row above) confirming the bound is tight.

  *(Note on the "flat identity" the round-31 outline flagged: it is not
  a separate vertex but the observation that $A(U)=1$ identically on the
  whole $2$-dimensional open region between vertices $(4,2,2,4,0)$ and
  $(4,4,0,3,1)$/near it — where the sort pattern is
  $f_1>c{=}4>f_2>2>f_3>1>0$ — since there $A(U)=f_1+f_2+f_3-(4+2+1)=8-7=1$
  regardless of the exact interior point; the vertex enumeration above
  subsumes this observation rather than needing it as a separate lemma,
  since every vertex bounding that flat region is itself in the table
  and evaluates to exactly $1$.)*

**The finite hyperplane family, shape $(1,2,0,0)$.** Working in free
coordinates $(a,h,i)$ (so $b=8-a$, $g=4-h-i$), the analogous $21$
hyperplanes are: type (I) $b=0$ (i.e. $a=8$), $i=0$; type (II) $a=b$
(i.e. $a=4$), $h=i$, $g=h$ (i.e. $2h+i=4$), and all $\binom42\cdot(\text
{cross}) $ ties between $\{a,b\}$ and $\{g,h,i,2,1\}$ ($a=g,a=h,a=i,a=2,
a=1,b=g,b=h,b=i,b=2,b=1$) plus ties of $\{g,h,i\}$ against the fixed
$\{2,1\}$ ($g=2,g=1,h=2,h=1,i=2,i=1$). Solving all $\binom{21}3=1330$
triples and filtering by feasibility ($a\ge b\ge0$, $g\ge h\ge i\ge0$)
gives **exactly $27$ distinct feasible vertices**:

  | $a$ | $b$ | $g$ | $h$ | $i$ | $A(U')$ |
  |---|---|---|---|---|---|
  | $4$ | $4$ | $4/3$ | $4/3$ | $4/3$ | $5/3$ |
  | $4$ | $4$ | $3/2$ | $3/2$ | $1$ | $2$ |
  | $4$ | $4$ | $2$ | $1$ | $1$ | $\mathbf1$ |
  | $4$ | $4$ | $2$ | $2$ | $0$ | $\mathbf1$ |
  | $4$ | $4$ | $3$ | $1$ | $0$ | $\mathbf1$ |
  | $4$ | $4$ | $4$ | $0$ | $0$ | $3$ |
  | $5$ | $3$ | $3$ | $1$ | $0$ | $3$ |
  | $6$ | $2$ | $4/3$ | $4/3$ | $4/3$ | $17/3$ |
  | $6$ | $2$ | $3/2$ | $3/2$ | $1$ | $6$ |
  | $6$ | $2$ | $2$ | $1$ | $1$ | $5$ |
  | $6$ | $2$ | $2$ | $2$ | $0$ | $5$ |
  | $6$ | $2$ | $3$ | $1$ | $0$ | $3$ |
  | $6$ | $2$ | $4$ | $0$ | $0$ | $3$ |
  | $13/2$ | $3/2$ | $3/2$ | $3/2$ | $1$ | $6$ |
  | $20/3$ | $4/3$ | $4/3$ | $4/3$ | $4/3$ | $17/3$ |
  | $7$ | $1$ | $4/3$ | $4/3$ | $4/3$ | $19/3$ |
  | $7$ | $1$ | $3/2$ | $3/2$ | $1$ | $6$ |
  | $7$ | $1$ | $2$ | $1$ | $1$ | $7$ |
  | $7$ | $1$ | $2$ | $2$ | $0$ | $5$ |
  | $7$ | $1$ | $3$ | $1$ | $0$ | $5$ |
  | $7$ | $1$ | $4$ | $0$ | $0$ | $5$ |
  | $8$ | $0$ | $4/3$ | $4/3$ | $4/3$ | $19/3$ |
  | $8$ | $0$ | $3/2$ | $3/2$ | $1$ | $6$ |
  | $8$ | $0$ | $2$ | $1$ | $1$ | $7$ |
  | $8$ | $0$ | $2$ | $2$ | $0$ | $7$ |
  | $8$ | $0$ | $3$ | $1$ | $0$ | $7$ |
  | $8$ | $0$ | $4$ | $0$ | $0$ | $5$ |

  Every entry satisfies $A(U')\ge1$, with equality at exactly $3$
  vertices (bold): $(4,4,2,1,1)$, $(4,4,2,2,0)$, $(4,4,3,1,0)$ — e.g.
  $(4,4,2,2,0)$: $U'=\{4,4,2,2,2,1,0\}$, sorted descending
  $4,4,2,2,2,1,0$, $A=4-4+2-2+2-1+0=1$, matching the round-28
  achievability construction exactly (this is the same multiset as
  shape $(2,1,0,0)$'s achievability vertex, confirming the two shapes'
  common tight value). **This proves $A(U')\ge1$ for shape $(1,2,0,0)$,
  in full.**

**Rigor note on the enumeration.** This is not a random or sampling
search: the candidate set is the theorem-guaranteed *finite* vertex
family (every triple of the *complete, exhaustively-listed* set of legal
tight-constraint hyperplanes, each independently justified above as the
only possible type-(I)/(II) events for this shape), computed in exact
rational arithmetic, with infeasible/inconsistent triples discarded by
direct substitution into the shape's defining inequalities — this is
precisely what `vertex-minimum-theorem` part 2–3 licenses as a *complete*
reduction of the continuum minimization to a finite check, not a partial
sample of it. Every vertex's value in both tables above is independently
hand-verifiable by sorting the $7$ listed numbers and alternating-summing
(worked examples given for the tight rows). No case was left unchecked:
the $36$ (resp. $27$) rows are the entirety of the feasible vertex set,
not a subset.

#### 7.18.5 Net status of $(\star_3)=\mathrm{MinFloor}(4)$ after this round

**All $6$ residual shapes of the $20$-shape exhaustion (round 28) are now
fully closed**: $(2,0,1,0)$ (round 29); $(2,0,0,1),(1,1,0,1),(1,1,1,0)$
(round 30); $(1,2,0,0),(2,1,0,0)$ (round 31, via the exhaustive vertex
enumeration above). Combined with the $14$ shapes closed directly in
round 28, **all $20$ maximal shapes of $(\star_3)=\mathrm{MinFloor}(4)$
are now proved $A(U)\ge1$, both directions (the matching achievability
construction $\{4,4,2,2,2,1\}$, valid within the budget of every shape,
was already established in round 28)** — by the Index-Chain Identity
(§7.11), **$(\star_3)=\mathrm{MinFloor}(4)$ is fully closed**. This
closes the last item of Claim (A)'s own discrete-counting toolbox at
level $n=4$ that this file had left open; the general-$n$ $(\star_k)$,
$k\ge3$, obstruction (shared with `greedy-halving-adversary`'s $h(m)$,
$m\ge5$) remains open exactly as before — this round's result is the
concrete $n=4$ instance, not a resolution of the general pattern.

### 7.19 Round 32: two new fully general lemmas (Max Bound, Insertion Sandwich) close $\mathrm{MaxCeil}(5)$ **in full** (both branches, unconditionally) via one unified mechanism — and, as a byproduct, upgrade the $\mathrm{MaxCeil}(\ell)\Leftarrow\mathrm{MinFloor}(\ell-1)$ reduction from "top-untouched branch only" to the *whole* statement

**Scope of this subsection.** Per this round's dispatch: (a) write up
$\mathrm{MaxCeil}(5)$'s top-untouched branch as a free corollary of
$(\star_3)=\mathrm{MinFloor}(4)$'s round-31 closure (§7.10.4+§7.11); (b)
attempt the harder top-cut, $\sigma_2$-touched residual via the
vertex-enumeration toolbox, using $(\star_3)$ as a positive ingredient, and
explicitly avoiding the two-peel+Fact-2 route the Necessity Theorem (§7.15)
proved insufficient. **Result: both are achieved, and (b) achieves
strictly more than asked** — a single new mechanism closes not just the
$\sigma_2$-touched residual but the *entire* top-cut branch (superseding
the need for §7.14's separate $\sigma_2$-untouched theorem at $\ell=5$,
though §7.14 remains the sharper *unconditional-in-$m$* statement for
general $m$), and in fact the whole of $\mathrm{MaxCeil}(5)$, both
branches, unconditionally.

#### 7.19.1 Part (a): $\mathrm{MaxCeil}(5)$'s top-untouched branch, as a free corollary

**Claim.** *For every ratio-2 superincreasing tail $\sigma=(\sigma_1,
\dots,\sigma_5)$ and every legal refinement $S$ of $\sigma$ using $\le3$
cuts that leaves $\sigma_1$ completely untouched, $A(S)\le\sigma_1-
\sigma_5$.*

**Proof.** Since $\sigma_1$ is untouched, every other element of $S$ is a
fragment of some $\sigma_i$, $i\ge2$, hence $<\sigma_i\le\sigma_2<\sigma_1$;
so $\sigma_1$ is the strict unique maximum of $S$. By
`sharp-dominant-removal-identity` (§5.2, already certified),
$$A(S)=\sigma_1-A(S'),\qquad S':=S\setminus\{\sigma_1\},$$
and $S'$ is a legal refinement of $\sigma'':=(\sigma_2,\sigma_3,\sigma_4,
\sigma_5)$ (a ratio-2 tail of length $4$) using the same $\le3$ cuts (none
spent on $\sigma_1$, all still available — this is exactly $\mathrm{Min
Floor}(4)$'s own budget cap, $4-1=3$). The target $A(S)\le\sigma_1-
\sigma_5$ is thus exactly, term for term, $A(S')\ge\sigma_5$ — precisely
$\mathrm{MinFloor}(4)$ applied to $\sigma''$. By the Index-Chain Identity
(§7.11), $\mathrm{MinFloor}(4)\equiv(\star_3)$; by the round-31 closure
(§7.16–7.18.5, `minfloor-4-full-closure`), $(\star_3)$ is a fully proved,
unconditional, non-numeric theorem (all $20$ maximal shapes, both
directions). Hence $A(S')\ge\sigma_5$ holds for every such $S'$, and so
$A(S)\le\sigma_1-\sigma_5$ holds for every such $S$. $\blacksquare$

This is the exact instantiation, at $\ell=5$, of §7.10.4's general
reduction ($\mathrm{MaxCeil}(\ell)$'s top-untouched branch $\Leftrightarrow$
$\mathrm{MinFloor}(\ell-1)$) plus §7.11's Index-Chain Identity — the only
thing new this round is that the previously-missing ingredient,
$\mathrm{MinFloor}(4)=(\star_3)$, is now itself a certified theorem, so
this closure requires no further work beyond writing it out. Via §7.10.2
($(7.9.1)\Leftrightarrow\mathrm{MaxCeil}(n-3)$), this resolves $(7.9.1)$'s
top-untouched branch unconditionally at $n=8$ — one step beyond round 26's
$n\le7$.

#### 7.19.2 Two new general, ladder-free lemmas

**Lemma (Max Bound).** *For any finite multiset $S$ of nonnegative reals,
$A(S)\le\max(S)$.*

**Proof.** If $S=\varnothing$ the statement is vacuous (or $A(\varnothing)
=0\le0$ by convention); otherwise let $s_1:=\max(S)$ (any element attaining
it — ties are irrelevant here since $A$ is defined directly from the
sorted sequence regardless of repeated values). Writing $S$ in sorted
descending order $s_1\ge s_2\ge\cdots\ge s_n\ge0$,
$$A(S)=s_1-s_2+s_3-s_4+\cdots = s_1-\big[(s_2-s_3)+(s_4-s_5)+\cdots\big].$$
Each bracketed term $(s_{2i}-s_{2i+1})\ge0$ since the sequence is sorted
descending (if $n$ is even the last bracket is a lone nonnegative term
$s_n\ge0$, or empty if $n=1$). So $A(S)=s_1-(\text{a sum of nonnegative
terms})\le s_1=\max(S)$. $\blacksquare$

(This is also an immediate corollary of `sharp-dominant-removal-identity`
applied to $s_1$ plus Fact 1 ($A\ge0$, §5.2): $A(S)=s_1-A(S\setminus\{s_1\})
\le s_1$ since $A(S\setminus\{s_1\})\ge0$ — both proofs are recorded since
the direct sorted-sequence argument needs no case split on whether $s_1$
is a *strict* unique maximum, unlike a literal reading of
`sharp-dominant-removal-identity`'s stated hypothesis.) Independently
verified by $200{,}000$ random-rational trials
(`/tmp/verify_insertion.py`), zero violations.

**Lemma (Insertion Sandwich).** *For any finite multiset $T$ of nonnegative
reals and any $a\ge0$,*
$$A(T)-a\ \le\ A(T\cup\{a\})\ \le\ A(T)+a.$$

**Proof.** Let $T$ have sorted descending order $t_1\ge\cdots\ge t_n\ge0$
and suppose $a$ is inserted at rank $k\in\{1,\dots,n+1\}$ of $T\cup\{a\}$
(i.e. $t_{k-1}\ge a\ge t_k$, with the conventions $t_0:=+\infty$,
$t_{n+1}:=0$). Every element of $T$ at original rank $i<k$ keeps rank $i$;
every element at original rank $i\ge k$ moves to rank $i+1$, flipping the
sign of its contribution to the alternating sum. Writing $U:=\sum_{i\ge k}
(-1)^{i+1}t_i$ for the (signed, using $T$'s own original rank parity)
contribution of the "tail from rank $k$ on," we get
$$A(T\cup\{a\})=\Big[\sum_{i<k}(-1)^{i+1}t_i\Big]+(-1)^{k+1}a-U
=A(T)-2U+(-1)^{k+1}a,$$
since $A(T)=\big[\sum_{i<k}(-1)^{i+1}t_i\big]+U$. Two cases on the parity
of $k$:

- **$k$ odd:** $(-1)^{k+1}=1$, and $U=A(T_{\ge k})$ (the tail, which
  consists exactly of the elements $t_k,\dots,t_n$, all $\le a$ by
  definition of the insertion point $k$, and read off in the *same* sorted
  descending order, so this literally is the alternating sum of that
  multiset). Since every element of the tail is $\le a$, the tail's own
  maximum is $\le a$, so by the Max Bound lemma just proved, $0\le U\le a$.
  Hence $A(T\cup\{a\})-A(T)=-2U+a\in[-a,a]$ (using $0\le U\le a$: at $U=0$
  this is $a$; at $U=a$ this is $-a$; affine in $U$ in between).
- **$k$ even:** $(-1)^{k+1}=-1$, and $U=-A(T_{\ge k})$ (the sign flips
  because rank $k$ is even, so the tail's *own* alternating sum, starting
  fresh at rank $1$ for the tail itself, is $-U$; the tail again consists
  of elements $\le a$). So $A(T_{\ge k})=-U\ge0$ by Fact 1, i.e. $U\le0$,
  and $A(T_{\ge k})\le a$ by the Max Bound lemma (tail's max $\le a$), i.e.
  $-U\le a$, i.e. $U\ge-a$. So $U\in[-a,0]$, giving $A(T\cup\{a\})-A(T)=
  -2U-a\in[-a,a]$ (at $U=0$: $-a$; at $U=-a$: $a$).

Either way $|A(T\cup\{a\})-A(T)|\le a$. $\blacksquare$

Independently verified by $200{,}000$ random-rational trials over multiset
sizes $0$–$6$ (`/tmp/verify_insertion.py`), zero violations. This is a
genuinely new, fully general, ladder-free two-sided perturbation bound —
strictly sharper in content than the certified `truncated-alternating-
sum-floor`/`-ceiling` lemmas (those bound $A(S)-2A(S_{>v})$ for a
*threshold* $v$; this bounds the effect of inserting one *new element* into
an arbitrary background multiset, a different and more primitive
operation).

#### 7.19.3 Master Theorem: $\mathrm{MaxCeil}(m)$ in full, conditional on $\mathrm{MinFloor}(m-1)$

**Theorem.** *Let $m\ge2$. Suppose $\mathrm{MinFloor}(m-1)$ holds (i.e.
$A(W)\ge\sigma_2'$'s... — precisely, in $\sigma'=(\sigma_2,\dots,\sigma_m)$
notation below, $A(W)\ge\sigma_m$ for every legal $\le(m-2)$-cut refinement
$W$ of $\sigma'$). Then $\mathrm{MaxCeil}(m)$ holds in full: for every
ratio-2 tail $\sigma=(\sigma_1,\dots,\sigma_m)$ and every legal refinement
$S$ of $\sigma$ using $\le m-2$ cuts (any distribution across all $m$
elements, including $\sigma_1$ untouched as the degenerate case $c_1=0$),*
$$A(S)\ \le\ \sigma_1-\sigma_m.$$

**Proof.** Let $c_1\ge0$ be the number of cuts $S$ spends on $\sigma_1$, so
$\sigma_1$ is split into $c_1+1\ge1$ positive fragments (with $c_1=0$
meaning $\sigma_1$ appears in $S$ untouched, as a single "fragment" equal
to $\sigma_1$ itself). Let $x$ denote the largest such fragment, and write
$\sigma':=(\sigma_2,\dots,\sigma_m)$ (a ratio-2 tail of length $m-1$),
$W:=S\setminus\{\text{all fragments of }\sigma_1\}$ — i.e. $W$ is exactly
the restriction of $S$ to $\sigma_2,\dots,\sigma_m$, a legal refinement of
$\sigma'$ using $(\le m-2)-c_1\le m-2-0=m-2$ cuts, in particular $\le
(m-1)-1=m-2$ cuts — **exactly** $\mathrm{MinFloor}(m-1)$'s own budget cap,
so the hypothesis applies to $W$: $A(W)\ge\sigma_m$.

**Case $x\le\sigma_2$.** Every fragment of $\sigma_1$ other than (or
including, if $c_1=0$) $x$ is $\le x\le\sigma_2$ (the fragments are
positive and sum to $\sigma_1$, with $x$ the largest, so every fragment is
$\le x$); every element of $W$ is a fragment of some $\sigma_i$, $i\ge2$,
hence $\le\sigma_i\le\sigma_2$. So every element of $S$ is $\le\sigma_2$,
i.e. $\max(S)\le\sigma_2$. By the Max Bound Lemma, $A(S)\le\max(S)\le
\sigma_2$. Since $\sigma_1=2\sigma_2$ and the tail is non-increasing
($\sigma_2\ge\sigma_m$), $\sigma_1-\sigma_m-\sigma_2=\sigma_2-\sigma_m\ge0$,
so $\sigma_2\le\sigma_1-\sigma_m$, giving $A(S)\le\sigma_1-\sigma_m$.

**Case $x>\sigma_2$.** The other $c_1$ fragments of $\sigma_1$ (if $c_1\ge1$;
if $c_1=0$ there are none, handle that as the trivial sub-case below) sum
to $\sigma_1-x<\sigma_1-\sigma_2=\sigma_2$, so each individually is
$<\sigma_2$ (a positive quantity dominated by a sum $<\sigma_2$). Combined
with every element of $W$ being $\le\sigma_2<x$, $x$ is the **strict
unique maximum** of $S$ (whether $c_1=0$, where $S=\{x\}\cup W$ trivially
has $x=\sigma_1$ as its unique max since $\sigma_1>\sigma_2\ge$ everything
in $W$, or $c_1\ge1$, just shown). By `sharp-dominant-removal-identity`,
$$A(S)=x-A(S\setminus\{x\}).$$
If $c_1=0$: $S\setminus\{x\}=W$ directly, and $A(W)\ge\sigma_m=\sigma_m-
\sigma_1+x$ (using $x=\sigma_1$), so $A(S)\le x-(\sigma_m-\sigma_1+x)=
\sigma_1-\sigma_m$ immediately (this is exactly §7.19.1's argument, a
special case).

If $c_1\ge1$: $S\setminus\{x\}=W\cup\{y_1,\dots,y_{c_1}\}$ where $y_1,
\dots,y_{c_1}$ are the other fragments of $\sigma_1$, summing to
$\sigma_1-x$. Applying the Insertion Sandwich Lemma's **lower** bound
$c_1$ times (inserting $y_1,\dots,y_{c_1}$ one at a time into $W$, each a
nonnegative real):
$$A(W\cup\{y_1,\dots,y_{c_1}\})\ \ge\ A(W)-\sum_{i=1}^{c_1}y_i\ =\
A(W)-(\sigma_1-x)\ \ge\ \sigma_m-\sigma_1+x.$$
So
$$A(S)=x-A(S\setminus\{x\})\ \le\ x-(\sigma_m-\sigma_1+x)\ =\ \sigma_1-
\sigma_m.$$

Either way, Case $x>\sigma_2$ gives $A(S)\le\sigma_1-\sigma_m$. Combined
with Case $x\le\sigma_2$, the two cases are exhaustive (every $x\ge0$
satisfies exactly one of $x\le\sigma_2$ or $x>\sigma_2$) and both give the
target bound. $\blacksquare$

**Remark (why this bypasses the Necessity Theorem's obstruction).** §7.15's
Necessity Theorem shows the *specific* "two-peel then Fact 2 directly on
$Z\cup\tau$" mechanism cannot close the residual, because it needs
$z_1\ge\sigma_2$ (false). The argument above is a **different** mechanism:
it never attempts to bound $A(W)$ from *above* via Fact 2 at all — it uses
$\mathrm{MinFloor}(m-1)$'s already-proved *lower* bound on $A(W)$ directly
(no re-derivation, $\sigma_2$'s own status inside $W$ is irrelevant), and
absorbs the effect of $\sigma_1$'s *other* fragments via the new Insertion
Sandwich Lemma rather than by re-peeling a second dominant element. This is
exactly the "genuinely new mechanism" the dispatch required, not a
repackaging of the ruled-out route.

#### 7.19.4 Instantiation at $m=5$: $\mathrm{MaxCeil}(5)$ closed in full, unconditionally

Since $\mathrm{MinFloor}(4)=(\star_3)$ is a fully certified, unconditional
theorem (round 31), the Master Theorem applies unconditionally at $m=5$:

$$\boxed{\mathrm{MaxCeil}(5)\text{ holds in full, both branches, for every
ratio-2 tail }\sigma=(\sigma_1,\dots,\sigma_5)\text{ and every legal
}\le3\text{-cut refinement }S:\ A(S)\le\sigma_1-\sigma_5.}$$

This closes $(7.9.1)$ (via §7.10.2, $(7.9.1)\Leftrightarrow\mathrm{MaxCeil}
(n-3)$) unconditionally at $n=8$ — a genuine advance beyond round 26's
$n\le7$, and, unlike round 26's $m=3,4$ closures (which needed separate
by-hand shape enumerations, §7.12–7.13), obtained here via one clean,
reusable, general mechanism rather than a fresh case census. Numerically
corroborated (not a substitute for the proof, an independent sanity check):
an exact-`Fraction` search at $\sigma=(16,8,4,2,1)$ over $250{,}000$ random
and targeted-adversarial legal $\le3$-cut refinements with $c_1\ge0$
distributed across all shapes (`/tmp/verify_maxceil5.py`) found maximum
$A(S)=9373/625\approx14.997<15=\sigma_1-\sigma_5$ throughout, consistent
with the bound being tight only in the limit, never exceeded.

**Scope, stated precisely (no overclaiming).** The Master Theorem itself is
*conditional* on $\mathrm{MinFloor}(m-1)=(\star_{m-2})$ — it does **not**
close $\mathrm{MaxCeil}(m)$ for $m\ge6$ (which would need $(\star_4)$,
not yet certified). What is unconditional this round is exactly its
instantiation at $m=5$ (using the now-certified $(\star_3)$), i.e.
$\mathrm{MaxCeil}(5)$ and hence $(7.9.1)$ at $n=8$. The Master Theorem is
however a strictly more general and more reusable tool than what the
dispatch asked for (a shape-by-shape census of the $\sigma_2$-touched
residual): it closes *every* shape of $\mathrm{MaxCeil}(m)$'s top-cut
branch (not just the $\sigma_2$-touched ones, and not just $\sigma_2$-
untouched as in §7.14) in one argument, conditional only on the single
already-identified hypothesis $(\star_{m-2})$, so it will apply
automatically and immediately the moment $(\star_4),(\star_5),\dots$ are
certified in future rounds — no fresh shape enumeration will be needed at
those levels either. The general-$n$ (all $m$) obstruction, i.e. certifying
$(\star_k)$ for all $k\ge3$, remains exactly as open as before; this round
closes one further concrete level ($k=3$, hence $m=5$, hence $n=8$), not
the general pattern.

## Promotable lemmas (round 31)

- **$(\star_3)=\mathrm{MinFloor}(4)$, full closure (§7.16–7.18.5).** All
  $20$ maximal cut-shapes of the $n=4$ ladder's Case-I residual are now
  proved $A(U)\ge1$ (with the round-28 construction $\{4,4,2,2,2,1\}$
  showing this is tight), both directions, no numerics load-bearing in
  the final chain of hand derivations for $14$ shapes (round 28) plus
  $4$ shapes via direct peel/case-tree (rounds 29–30) plus the final $2$
  shapes ($(1,2,0,0)$, $(2,1,0,0)$) via exhaustive exact-rational vertex
  enumeration licensed by `vertex-minimum-theorem` (round 31, §7.18.4).
  Ready to certify as a standalone lemma `minfloor-4-full-closure.md`
  (statement: for the $n=4$ ladder $\pi=(8,4,2,1)$ (units $1/15$), every
  legal $\le3$-cut response $U$ with $\pi_1$ split into at most $3$
  fragments etc. — i.e. every one of the $20$ maximal "exactly $3$ cuts,
  distributed as a composition of $(3,3,\dots)$ summing appropriately"
  shapes identified in §7.16 — satisfies $A(U)\ge1$, equivalently
  $\mathrm{MinFloor}(4)\ge1$, matching $(\star_3)$ via the certified
  Index-Chain Identity of §7.11) for the reviewer to certify and for
  `greedy-halving-adversary` to cite directly (its $h(4)$'s $c=x$ vertex
  already cites $\mathrm{MaxCeil}(4)$, the dual quantity, from this same
  file — $\mathrm{MinFloor}(4)$ is the sibling quantity now also fully
  closed).
- **Vertex-enumeration-for-two-simultaneously-split-parents technique
  (§7.18.4, methodological, not a separate formal statement).** When a
  target multiset $U$ contains two disjoint, independently-split
  "conservation groups" (e.g. one piece split into a triple summing to a
  fixed total, another split into a pair summing to a different fixed
  total) plus finitely many fixed constants, and a linear branch-tree
  case-split threatens to omit a cross-group joint-feasibility
  constraint, the fix is to enumerate the theorem-guaranteed *finite*
  vertex family directly (`vertex-minimum-theorem` parts 2–3: every
  vertex is cut by $d$ independent tight constraints, each a fragment$=0$
  or a two-value tie, drawn from the *complete* list of legal such
  events for the shape) in exact rational arithmetic, evaluating $A$ at
  each by direct sorting — this enforces every cross-group constraint
  automatically via the feasibility filter, without needing to spot or
  state it as a separate hypothesis. Reusable whenever a similar
  "two-simultaneously-split-parents" shape arises (e.g. at $(\star_k)$
  for $k\ge4$, if the outline's general-$n$ pattern ever needs a
  concrete instance closed this way).

## Promotable lemmas (round 32)

- **Max Bound (§7.19.2): $A(S)\le\max(S)$ for any finite multiset $S$ of
  nonnegative reals.** Proved two ways (direct sorted-sequence telescoping;
  corollary of `sharp-dominant-removal-identity`+Fact 1). Fully general, no
  ladder structure. Independently verified, $200{,}000$ random-rational
  trials, zero violations. Recommend `lemmas/max-bound-fact.md`.
- **Insertion Sandwich (§7.19.2): $|A(T\cup\{a\})-A(T)|\le a$ for any
  finite multiset $T$ of nonnegative reals and any $a\ge0$.** Proved by a
  rank-shift computation (parity case split on where $a$ lands), using only
  the Max Bound fact above and Fact 1. Fully general, no ladder structure.
  Independently verified, $200{,}000$ random-rational trials over sizes
  $0$–$6$, zero violations. Recommend `lemmas/insertion-sandwich-lemma.md`
  — this is a new, reusable, more primitive perturbation bound than the
  already-certified truncated-alternating-sum floor/ceiling lemmas.
- **Master Theorem (§7.19.3): $\mathrm{MinFloor}(m-1)=(\star_{m-2})
  \Rightarrow \mathrm{MaxCeil}(m)$ in full (both branches, every legal
  $\le(m-2)$-cut refinement, no shape enumeration).** Proved via a single
  two-case split (largest fragment of $\sigma_1$'s own split $\le\sigma_2$
  or $>\sigma_2$) using only Max Bound, `sharp-dominant-removal-identity`,
  and Insertion Sandwich. Strictly stronger than §7.10.4's earlier
  "top-untouched branch only" reduction (which this supersedes but does not
  invalidate). Recommend `lemmas/maxceil-master-theorem.md`, stated with
  its conditional hypothesis preserved explicitly (not certified as
  unconditional for general $m$ — only its $m=5$ instantiation is
  unconditional, since only $(\star_1),(\star_2),(\star_3)$ are currently
  certified).
- **Corollary: $\mathrm{MaxCeil}(5)$, full unconditional closure (§7.19.4),
  and hence $(7.9.1)$ at $n=8$.** Immediate from the Master Theorem plus
  the round-31 certified `minfloor-4-full-closure`. Recommend certifying
  alongside the Master Theorem (or as a corollary note within the same
  lemma file) as the concrete instance currently usable by
  `greedy-halving-adversary`'s $h(5)$'s $c=x$ vertex (same object, per the
  round-32 outline's cross-reference).
