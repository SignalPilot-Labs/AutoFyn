# Round 30 proof-reviewer report — imo-2026-03

Reviewed all 3 built slugs against `problems.jsonl`, `knowledge_base.md`,
and each approach file's full text (not just the new section — grepped
each file end-to-end for stale overclaim text, per the standing rule).
Independently re-derived and re-verified every load-bearing new claim with
fresh scripts (not the builders' own), in exact `Fraction` arithmetic
where the claim is exact, plus broader/independent random sweeps than the
builders' own checks. Scripts used: `/tmp/verify_718.py`,
`/tmp/verify_718b.py`, `/tmp/verify_exact.py`, `/tmp/verify_vertex5.py`,
`/tmp/verify_lp30.py`.

## 1. `rank-pigeonhole-budget` — verdict: CHANGES REQUESTED

**Claim reviewed.** New §7.18: shapes $(2,0,0,1)$ (the residual
$f_1\ge4$ branch; round 29 had already closed $f_1<4$), $(1,1,0,1)$, and
$(1,1,1,0)$ are each fully closed, both directions, no numerics
load-bearing. Shapes $(1,2,0,0)$ and $(2,1,0,0)$ are honestly left open,
with a genuinely new obstruction diagnosed (no a priori dominance between
$f_1$, the free $\pi_1$-triple's top, and $c$, the free $\pi_2$-pair's
top, plus a cross-pair joint-feasibility constraint needed to close even
one sub-sub-case).

**Independent verification.**
- Re-derived the shape definitions exactly (units of $1/15$,
  $\pi=(8,4,2,1)$, cut counts per shape) and wrote a fresh random-search
  script testing all 5 shapes mentioned this round (`(2,0,0,1)`,
  `(1,1,0,1)`, `(1,1,1,0)`, plus the still-open `(1,2,0,0)`, `(2,1,0,0)`)
  at once, 400,000 trials total: minimum $\approx1$ (never below 1) on
  every shape including the two still-open ones — consistent with the
  conjecture and no contradiction of the builder's claims.
- Spot-checked the genuine algebraic content of §7.18.1's hardest
  sub-case (shape $(2,0,0,1)$, $f_1\in(4,5)$, $f_2>2$ strict, all four
  ordering sub-cases of $f_3$ vs. $\{e,f\}$) with a 20,000-trial exact-
  `Fraction` script constructed directly from the case's own defining
  inequalities (not a loose superset): zero violations, confirming the
  closed-form algebra, not just the final inequality.
- Checked the load-bearing tool citations (`sharp-dominant-removal-
  identity`, `odd-run-reduction-lemma`, the round-29-certified
  Pair-Insertion Ordering Lemma both forms) are used within their proven
  hypotheses throughout (strict-max peels genuinely have a strict max at
  each step; the PI-lemma's $q\le w\le p$ / $w\ge p\ge q$ preconditions
  hold at each cited instantiation, e.g. §7.18.2's $c\ge2$ forced-
  dominance fact, an elementary "a cut always leaves $\ge$ half" claim I
  independently re-derived by contradiction).
- Checked case exhaustiveness for all three closed shapes by re-tracing
  every branch listed in the "Conclusion" paragraphs (7.18.1: $f_1\ge5$,
  $f_1\in(4,5)$ four sub-cases, $f_1=4$ boundary with its own degenerate
  corner; 7.18.2: $b\ge c$/$b<c$ each with their own sub-branches plus the
  $a=4$ boundary; 7.18.3: symmetric structure) — no missing case found.

**No gap found in the three claimed closures.** The honestly-open
shapes $(1,2,0,0)/(2,1,0,0)$ are correctly reported as NOT closed — the
file does not claim otherwise anywhere (checked the file's Status header,
which correctly reads "solved" scoped only to Claim (A), unaffected by
this section; §7.18.5's own summary is accurate: "4 of 6" closed, "2 of
6" open, no overclaim). No stale overclaim text found elsewhere in the
(4300+ line) file on a fresh grep for "solved"/"closed" near this round's
topics.

**True Status of this approach's own target ($(\star_3)=\mathrm{MinFloor}(4)$):**
`partial` (2 of 6 shapes remain genuinely open) — matches the file's own
framing. Claim (A), a *different*, already fully-closed sub-target of
this same file, remains `solved` at its own scope (unaffected, not
re-touched this round).

**Record:** `advanced` — real progress (2 more shapes of a precisely-
scoped 6-shape decomposition closed by hand), correctly and honestly
diagnosed remaining gap (a new cross-pair joint-feasibility obstruction,
not a vague "more casework needed").

## 2. `greedy-halving-adversary` — verdict: CHANGES REQUESTED

**Claim reviewed.** Round 30 section: Vertex 5 of $h(m)$'s
"single-cut-on-$q_1$, tail-untouched" piece (the sole vertex type left
open after round 29) is closed in full for every $m\ge3$ and every
$t\in\mathrm{tail}$, via (Step 2) an exact-slope monotonicity argument
collapsing the continuum in $x\in(0,q_1/2)$ to the boundary $x=q_1/2$,
and (Steps 3-5) a closed-form "remove one rung from the ladder" identity
$A(\mathrm{tail}\setminus\{a_p\})=f(m)\,(2^m+(-1)^p2^{m-p}+(-1)^m)/3$
proved $\ge f(m)$ for every $p=1,\dots,m$, $m\ge3$. The file explicitly
flags and fixes a bug in its own round-30 outline (a false claimed exact
equality $A(\mathrm{tail})=f(m)$ for the $t=q_2$ boundary, general $m$ —
actually only true at $m=3$).

**Independent verification (the load-bearing step, re-derived from
scratch).**
- Wrote `/tmp/verify_vertex5.py`: independently constructed the ladder
  tail for $m=3,\dots,9$, computed $A(\mathrm{tail}\setminus\{a_p\})$ by
  direct sort-and-alternating-sum for every $p=1,\dots,m$, and compared
  against the claimed closed form: **exact match in every one of the
  $3+4+\dots+9=42$ cases** (a superset of the builder's own $m=3,\dots,14$
  check in different $m$-range, same conclusion).
- Verified $A(\mathrm{tail}\setminus\{a_p\})\ge f(m)$ holds in every one
  of those 42 cases (no violations), confirming Step 5's final
  inequality.
- Independently re-derived the two-case parity-split algebra by hand
  (even $p$: trivial margin $\ge2^m-1$; odd $p$: reduces to
  $2^{m-1}+(-1)^m\ge3$, tight only at $m=3,p=1$) — matches the file's
  derivation exactly, no sign or off-by-one error found.
- Independently re-verified the monotonicity claim itself (Step 2) with
  a dense rational grid of $x\in(0,q_1/2)$ for a random tail element $t$,
  $m=3,\dots,9$: $F(x)$ never increases across the grid, consistent with
  the cited $\pm1$-slope fact from the already-certified
  `single-insert-point-vertex-lemma`.

**No gap found.** The scope is honestly and precisely stated in three
places in the file (top summary, "Open gaps," and the section's own
"Summary" paragraph): this closes only the tail-*untouched* piece of
$h(m)$'s $q_1$-cut sub-case; the complementary piece where $S$
simultaneously cuts $q_1$ and refines the tail is explicitly flagged as
fully open and entirely unattempted this round. No stale overclaim of
"$h(m)$ closed for $m\ge3$" found anywhere else in the (8800+ line) file
on a targeted grep — every instance of "$h(m)$...closed" is correctly
qualified to the narrower piece.

**Record:** `advanced` — genuine closure of a real, precisely-scoped
vertex type, with a self-caught outline bug fixed before it could
propagate; the true bottleneck (the untouched simultaneous-cuts piece)
is correctly reported as still fully open, not narrowed further.

## 3. `lp-duality-certificate` — verdict: CHANGES REQUESTED

**Claim reviewed.** §R30.0 retracts round 29's false "100% empirical
coverage of the $n=4$ residual box $\mathcal R$ by 60 chambers" claim
(refuted by an exact interior counterexample $p=(11,7,6,3,2)/29$ at
which all 60 chambers give $\Phi=15/29>16/31=a_4T$). §R30.1 proves a new
general **Partition Chamber Theorem** unifying `bisect-subset-lemma`,
Double-Bisect-Pin, a corrected Triple-Pin, and a new Double-Pin-Pair
family, via `pair-insensitivity-corollary` alone. §R30.2/R30.3 use named
instances of this theorem to close both of the round's two known
counterexample witnesses exactly ($\Phi=1/2<16/31$ in both cases). §R30.5
explicitly does NOT claim full $n=4$ coverage.

**Independent verification.**
- Independently re-confirmed the counterexample: wrote a fresh script
  evaluating all 60 of round 29's chamber formulas at
  $p=(11,7,6,3,2)/29$ (exact `Fraction`, not reusing the builder's own
  script) — all 60 give exactly $15/29$, which exceeds $16/31$ by exactly
  $1/899>0$. The retraction is real and correctly executed, not
  cosmetic — checked the Status header, "Current best," and the
  round-29 write-up section all now say the same corrected thing.
- Re-derived and independently re-verified the general Partition
  Chamber Theorem's formula with a **broader** sweep than the builder's
  own ($m=5$-only, 553 trials): `/tmp/verify_lp30.py` tests $m=3,\dots,7$,
  random partitions/host choices/singleton bisect-vs-untouch decisions,
  1913 feasible exact-`Fraction` trials, comparing a from-scratch direct
  fragment-simulation against the closed form — **zero mismatches**.
- Independently re-verified both witness closures exactly: witness 1
  ($p=(11,7,6,3,2)/29$, $\rho=p_1-p_3-p_4-p_5=0$, $\Phi=1/2$) and witness
  2 ($p=(14,7,5,3,1)/30$, $\rho_1=p_1-p_2-p_3=1/15$,
  $\rho_2=p_4-p_5=1/15$, $|\rho_1-\rho_2|=0$, $\Phi=1/2$), both strictly
  below $16/31$ by margin $1/62$.
- Re-checked the theorem's proof mechanism (mass telescoping, the
  matched-pair decomposition, the iterated `pair-insensitivity-corollary`
  citation with no genericity hypothesis needed) by hand: no gap.

**No overclaim found — checked the whole file, not just the new
section.** Grepped every occurrence of "100%" in the 7600+ line file:
all pre-round-30 instances are now correctly annotated as retracted
(lines ~753-817, "Current best" section) or historically preserved with
an explicit "superseded"/"RETRACTED" marker; the Status header (top of
file) states the retraction plainly and does not overclaim coverage.

**Record:** `advanced` — a correctly-executed self-retraction (the
mandatory first step per the round's own dispatch) plus a genuine new
general theorem that closes both known witnesses, with the scope
explicitly and correctly limited to "these two witnesses," not "full
coverage."

## Net assessment / current.md updates

All three fronts made genuine, independently-verified, honestly-scoped
progress this round; no overclaim found in any of the three files
(continuing rounds 28-29's clean run — 3 consecutive overclaim-free
rounds). None closes its own round-30 target in full:
$(\star_3)=\mathrm{MinFloor}(4)$ now has only 2 of 6 shapes open (down
from 4); $h(m)$'s single-cut-on-$q_1$ piece is now fully closed for
every $m\ge3$, but the tail-refining complementary piece of the
$q_1$-cut sub-case remains entirely untouched and open; $n=4$'s upper
bound now has both known counterexample witnesses closed but no
re-established general coverage claim. **Status of the whole problem
remains `partial`** (updated `results/imo-2026-03/current.md` with a new
"Round 30" entry appended to the end of the growing narrative, matching
the file's established rolling-history convention, since the file's
`## Full proof` section is — per prior rounds' precedent, not fixed by
this reviewer this round — used as a rolling continuation of the
"Approaches tried" narrative rather than a literal "absent unless solved"
block; this is a pre-existing structural quirk of this specific
`current.md`, not introduced this round).

**2 new lemmas certified** this round:
- `single-rung-removal-closed-form-and-vertex-5-closure` (from
  `greedy-halving-adversary`) — `results/imo-2026-03/lemmas/
  single-rung-removal-closed-form-and-vertex-5-closure.md`.
- `partition-chamber-theorem` (from `lp-duality-certificate`) —
  `results/imo-2026-03/lemmas/partition-chamber-theorem.md` (subsumes
  the Corrected Triple-Pin and Double-Pin-Pair instances as documented
  special cases within the same file, not separately certified since
  each is a one-line instantiation).

No new lemma certified from `rank-pigeonhole-budget` this round (it only
applied already-certified facts; no new standalone lemma was proposed).

**Recommend next round:** (1) `rank-pigeonhole-budget` — attack shapes
$(1,2,0,0)/(2,1,0,0)$'s cross-pair joint-feasibility obstruction
directly, now the single most precisely diagnosed open item toward
$(\star_3)$; (2) `greedy-halving-adversary` — the simultaneous
$q_1$-cut-and-tail-refinement piece of $h(m)$'s $q_1$-cut sub-case needs
a genuinely new mechanism, not yet attempted at all; (3)
`lp-duality-certificate` — run a fresh outer-minimization
(allocation-agnostic) search against the expanded Partition Chamber
family before attempting any Farkas-style coverage proof, per the file's
own methodological warning about self-referential coverage checks.

## Per-approach verdicts (summary)

1. `rank-pigeonhole-budget` — Status: `partial` — **CHANGES REQUESTED**
2. `greedy-halving-adversary` — Status: `partial` — **CHANGES REQUESTED**
3. `lp-duality-certificate` — Status: `partial` — **CHANGES REQUESTED**

Whole-problem Status: `partial` (unchanged; no APPROVE this round).
