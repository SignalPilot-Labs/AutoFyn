## imo-2026-03 (lens: greedy-reduction-geometric Case 2 interleaving, + Lemma X' transfer, + population-diversity check)

### Distinct openings

1. **Cut-Reallocation / "cuts belong at the top" reduction (NEW, numerically strongly
   supported, not yet proved).** Rather than attacking the fully general
   interleaving of a split top piece with an arbitrarily-refined tail (which is
   where Lemma X' is needed), first prove an **exchange lemma**: for LB's
   geometric partition, moving one unit of XY's cut-budget from any tail piece to
   a "self-similar cascade" continuation of the top-piece split never decreases
   OddSum (i.e. is weakly worse for XY / weakly better for LB). If true, this
   lets you restrict attention, WLOG, to allocations where XY's cuts form a
   *nested self-similar refinement starting at the top* (split $2^n$, optionally
   recurse into one of its own fragments or into $2^{n-1}$, etc.) — never
   "wasting" a cut on a low tail piece while the top is still coarser than it
   could be. Crucially, in this restricted family the "tail" that remains
   genuinely *untouched* is always an exact, fully known suffix of the geometric
   sequence $(2^{n-1},\dots,1)$ (or a further such suffix), so its OddSum *and*
   EvenSum are both known in closed form — **no dual/two-sided inductive
   hypothesis (Lemma X′) is needed at all** for this restricted sub-problem. This
   is a genuinely different route around the Case-2 wall: instead of proving a
   two-sided bound on an arbitrarily-refined tail, you prove cuts on an
   arbitrarily-refined tail are never optimal for XY in the first place.

2. **Direct "top-only splitting" sub-problem (tractable, numerically solved
   exactly for $n=2,3,4$).** Restrict to allocations where *all* cuts land on
   the single top piece $2^n$ (tail completely untouched $=\Gamma_{n-1}$ exactly).
   Numerics (below) show $\min_{\text{split into }j+1} \mathrm{OddSum}$ is
   *strictly decreasing* in $j$ and hits exactly $2^n$ at $j=n$ (using all
   cuts) — and in fact already at $j=n-1$ for $n\ge3$ tested. This sub-problem
   has an exact, closed, known tail, so a peeling/induction argument on $j$
   should be directly tractable (each peel step needs only exact values of
   $\Gamma_{n-1}$'s prefix sums, not an inductive lower bound on a refined
   sub-multiset). This is very likely provable this round or next, and (per
   opening 1) may be *sufficient* to close Case 2 if the exchange lemma holds.

3. **Flat-minimum / tie-block face structure (confirms the outline's own
   diagnosis).** Direct numeric optimization shows the objective $\mathrm{OddSum}$
   as a function of the split parameters is piecewise linear with **whole faces
   of exact minimizers**, not isolated points — e.g. at $n=3$, allocation
   (1 cut on top, 1 cut on the second piece, tail $\{2,1\}$ untouched): setting
   $t_1=t_2=4$ (top split exactly in half) and $m_1\in[1,3]$ (any split of the
   second piece $4$ with both fragments in $[1,3]$) gives $\mathrm{OddSum}=8$
   exactly for *every* such $m_1$ — a 1-dimensional flat face of exact minimizers
   (verified exactly, see numerics below). This is precisely the "tie-block"
   phenomenon the outline called for and that Section 4b's failed Q-priority
   strategy could not capture (it assumed a single canonical split, not a face).
   The certified generalized Tie-neutrality lemma
   (`lemmas/tie-neutrality-and-first-mover-half.md`, Lemma A) is exactly the
   tool for reasoning about *why* the value is constant across such a face
   (ranks trade places but tied contributions cancel) — this is direct evidence
   the outline's tie-block approach is on the right track structurally, it's
   just not yet been executed to completion.

4. **Lemma X′ transfer (answered).** Yes — Lemma X′ as stated in
   `self-similar-induction-on-n.md` (dual Group-Domination: if
   $\mathrm{EvenSum}(S')\ge T'/2$ then $\mathrm{EvenSum}(A'\cup S')\ge T'$) is
   *structurally identical* to what `greedy-reduction-geometric`'s Case 2
   needs in its "$a_1$ dominates" sub-attempt (Section 4b / the $j\ge2$
   peeling attempt in `self-similar-induction-on-n.md` Step 3): both reduce
   to needing a lower bound on $\mathrm{EvenSum}$ of an arbitrarily-refined
   tail sub-multiset, which the one-sided hypothesis $T(m-1)$ (lower bound on
   $\mathrm{OddSum}$ of the *whole* tail) cannot supply. So a proof of Lemma
   X′ would directly transfer and very likely close (or substantially close)
   greedy-reduction-geometric's Case 2 too, via the identical peeling algebra
   — they are the same gap viewed from two approaches, not two different
   gaps. (This confirms the CLAUDE.md warning: two of three live approaches
   share one wall.)

   **Correction / important update:** I independently re-tested Lemma X′ as
   literally stated (for arbitrary finite multisets $A',S'$ of positive
   reals with $\mathrm{sum}(A')=T'$ and $\mathrm{EvenSum}(S')\ge T'/2$,
   claiming $\mathrm{EvenSum}(A'\cup S')\ge T'$) by random search and found
   an explicit counterexample in minutes (e.g. $A'=\{4.141,4.351\}$,
   $T'=8.492$; $S'=\{2.549,1.896,1.741,1.037,3.374\}$,
   $\mathrm{EvenSum}(S')=4.290\ge T'/2=4.246$; but
   $\mathrm{EvenSum}(A'\cup S')=8.432<T'=8.492$). **Lemma X′ as literally
   stated is FALSE in general** — this matches an independent finding already
   recorded in `/tmp/memory/math-explorer.md` (round-3 entry) by a parallel
   explorer this same round, so this is now doubly confirmed. Consequently:
   Lemma X′ **cannot** be used as-is to close either approach's Case 2 — any
   proof must use a *restricted* version tied to the problem's actual
   geometric/dyadic structure (bounded ratios between consecutive pieces, not
   arbitrary multisets), not the clean abstract statement as written. This
   makes **Opening 1/2 above (the cut-reallocation exchange lemma / top-only
   sub-problem, which never needs a dual EvenSum bound on an arbitrary
   refined tail at all) more valuable, not less** — it sidesteps the false
   lemma entirely rather than trying to patch it. I recommend the outliner
   drop Lemma X′ (in its current general form) from the population's target
   list and pursue Opening 1/2, or a version of X′ *restricted to
   multisets that are themselves refinements of a geometric/dyadic sequence*
   (untested — a natural next check).

### Candidate technique(s)
- Exchange/domination argument (opening 1) — a monovariant-style argument:
  "moving budget toward the top piece cannot help XY" (`knowledge_base.md`'s
  invariant/monovariant entry, line ~117/191).
- Direct peeling induction on $j$ for the top-only sub-problem (opening 2),
  reusing the certified Peeling Lemma (`dominant-piece-lower-bound.md`) and
  Element Bound (`self-similar-induction-on-n.md`'s Lemma E) — no new
  machinery needed, just careful bookkeeping with the *exact* known tail.
- Piecewise-concavity/breakpoint analysis (`knowledge_base.md` line 20,
  "Piecewise-concavity smoothing") is a directly relevant named KB entry for
  formalizing the flat-face phenomenon in opening 3: sort the merged multiset
  by all pairwise-tie breakpoints of the split parameters, note $\mathrm{OddSum}$
  is piecewise linear in those parameters between breakpoints, and argue
  minimality face-by-face.

### Cheap-kill candidates
- None found that kill the problem; but a useful **cheap sanity/pruning
  check** for future rounds: before attempting a general interleaving
  argument, first check numerically (as done here) whether the *specific*
  allocation under test is dominated by an "all-cuts-cascade-to-top"
  allocation — this is a fast filter (a few evaluations of OddSum) to decide
  whether a given XY response is even a plausible near-optimal candidate
  before spending proof effort on it.

### Knowledge-base entries to use
- **Piecewise-concavity smoothing** (`knowledge_base.md` line ~20) — directly
  applicable to formalize the flat-face / breakpoint structure in opening 3.
- **Invariants & monovariants** (`knowledge_base.md` lines ~117, ~191) — the
  right conceptual frame for the exchange lemma in opening 1 (show a
  potential/ordering monovariant under "move a cut toward the top").
- **Dyadic range / dyadic-bucket bound** (`knowledge_base.md` lines ~73, ~245)
  — relevant vocabulary for the geometric/dyadic piece-size structure
  already central to this problem; likely reusable in whichever approach
  formalizes "cuts belong at the top" (dyadic domination of prefix sums).

### Analogous past problems (cruxes)
Did not have time this round to query the crux corpus systematically by
subtopic field name (the dispatch's lens was primarily the numeric
interleaving structure); the one crux already on file
(**aimo-0117**, "Jesse en Tjeerd," cited in `dyadic-potential-invariant.md`)
remains the best-known analog for a potential/credit argument on a
dyadic/geometric dominance structure, and is worth the next explorer's or
outliner's attention specifically for opening 1's exchange-lemma framing
(the credit/potential idea is naturally suited to proving a monovariant
under cut-reallocation, which is exactly what opening 1 needs). No other
corpus entry was checked this round — flagging as unexplored rather than
claiming "none".

### Prior progress
- Case 1 (XY never touches LB's top piece): fully proved, all $n$.
- $n=0,1$: fully proved both directions.
- $j=1$ (XY spends exactly 1 cut on top piece, arbitrary tail refinement):
  fully proved for all $n$ (`self-similar-induction-on-n.md` Step 1), reusable
  by `greedy-reduction-geometric`.
- Upper-bound regime $p_1\in[1/2,c(n)]$: fully proved for arbitrary (not just
  geometric) LB partitions (`universal-halving-adversary.md`).
- Greedy-floor-against-arbitrary-opponent (Lemma 4): proved, but the natural
  "Q-priority" composite strategy built from it is a **confirmed dead end**
  (exact game-tree counterexample, $7/15<8/15$ at $n=3$).

### Dead ends (do not retry)
- **Static "Q-priority" LB strategy** (clear fragments of the split top piece
  before touching the rest): proven by exact game-tree computation to give
  only $7/15 < c(3)=8/15$ at $n=3$ — confirmed correct by re-derivation this
  round is unnecessary since it's an exact rational computation already
  independently verified by the round-2 reviewer; do not retry any
  static-priority-order variant.
- **Aggregate/weak bounds on the merge** ("top two elements of the merge sum
  to $\ge r_n$", or bounding via $\mathrm{OddSum}(\text{rest})\le R$ trivially):
  documented in `greedy-reduction-geometric.md` Section 4 as checked and
  false/insufficient (e.g. $n=3$ equal-split example: top two elements sum to
  $6/15<8/15=r_3$, yet the true OddSum is still $9/15>c(3)$ — the inequality
  survives by a different mechanism, so these aggregate shortcuts don't
  capture the real reason).
- **"Naive $U(m)=\mathrm{sum}$" as the missing upper bound for Lemma X′**:
  checked in `self-similar-induction-on-n.md`, trivially true but too weak.

### Small-case / intuition notes (all labeled CONJECTURE — numeric evidence only)
All computed via Nelder-Mead / random search in Python (script available on
request; not committed, exploratory only), so these are strong *numerical*
evidence, not proofs.

- **$n=2$** ($\Gamma_2=(4,2,1)$, target unnormalized $=4$): every cut
  allocation with budget $\le2$ tested gives $\min\mathrm{OddSum}\ge4$, with
  equality exactly at allocations that put cuts entirely at/near the top
  (`(2,0,0)`: split top into 3 self-similar fragments, exact min $=4$;
  `(1,1,0)`: 1 cut on top + 1 cut on second piece, exact min $=4$; `(1,0,0)`:
  1 cut on top alone, exact min $=4$). Any allocation spending a cut on the
  bottom piece "1" or spreading cuts without touching the top gives strictly
  more ($\ge4.5$).
- **$n=3$** ($\Gamma_3=(8,4,2,1)$, target $=8$): same pattern. All-cuts-on-top
  with self-similar-ratio split gives exactly $8$; `(1,1,0,0)` (1 cut top + 1
  cut on piece "4") also gives exactly $8$, and moreover the minimizers form
  a genuine flat 1-parameter face: $t_1=t_2=4$ (top split exactly in half)
  together with **any** split $m_1+m_2=4$, $m_1\in[1,3]$, of the second piece
  gives $\mathrm{OddSum}=8$ exactly (verified by direct computation over a
  grid of $m_1$ values: $8.0$ throughout $[1,3]$, rising to $8.5$–$8.9$ outside).
  Allocations spending cuts on the bottom two pieces (e.g. `(0,0,1,1)`,
  `(0,0,2,0)`) give strictly more ($9.5$–$10$).
- **$n=4$** ($\Gamma_4=(16,8,4,2,1)$, target $=16$): top-only splitting gives
  min OddSum $=21,18,17,16,16$ for $j=0,1,2,3,4$ respectively — strictly
  decreasing, hitting the target exactly at $j=3$ *and* $j=4$ (using all cuts
  is not strictly required; $n-1$ cuts on top alone already suffices once
  $n\ge3$ in the tested cases, i.e. the very top-heavy allocations are all
  tied for the minimum once close enough to full budget).
- These patterns together support Openings 1–2 above as the right next
  target: **conjecture** "the XY allocation minimizing OddSum against LB's
  geometric partition can always be taken to be a self-similar cascade
  concentrated at the top of the geometric sequence, and such allocations
  achieve exactly $c(n)$ with equality on a face (not a point) of the
  parameter space" — not proved, but the numerics (all cases $n\le4$, all
  cut allocations $\le n$, hundreds of optimizer restarts each) show no
  counterexample and a very clean, explicable pattern.

### Population-diversity flag (per CLAUDE.md instruction)
Sampled the ranker: 4 approaches exist. Three (`greedy-reduction-geometric`,
`self-similar-induction-on-n`, `universal-halving-adversary`) are all
"expanded: 2" and all independently converge on the *same* underlying wall
(a two-sided/dual EvenSum bound on an arbitrarily-refined tail — confirmed
above, this is genuinely the same gap under three names). This is exactly
the round-count/pattern CLAUDE.md flags as a signal to add real framing
diversity, not another bypass in the same framing. The fourth approach,
**`dyadic-potential-invariant`**, has **expanded: 0** — it has never been
built — despite being explicitly designed as "deliberately a different
top-level route" (a potential/credit argument run directly on the game tree,
rather than characterizing the game value combinatorially first). Its own
file already flags the crux unproven claim ("local split monotonicity") and
recommends killing it fast if that claim fails to hold even numerically. **I
recommend the outliner include `dyadic-potential-invariant` in this round's
build set** (or explicitly numerically test its "local split monotonicity"
claim before building) as the field's one genuinely-distant approach — it
has had zero rounds of investment despite being on the board since round 1
or 2, which itself is a diversity gap independent of the Case-2 wall.
Additionally, Opening 1 above (cut-reallocation exchange lemma) is *not* the
same framing as any of the three stuck approaches — it attacks by restricting
XY's strategy space rather than bounding OddSum for an arbitrary refined
multiset — and is a candidate for either a new approach slug or a genuinely
new sub-route within `greedy-reduction-geometric`.
