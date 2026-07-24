## imo-2026-03 (n=4 general upper bound — outer-minimization coverage check)

### What I did
Built an independent, from-scratch exact enumeration of the *full* general
Partition Chamber Theorem (R30.1 of `approaches/lp-duality-certificate.md`)
at $m=5$ ($n=4$), not just the previously-tried named sub-families
(Bisect-Subset 30 + Double-Bisect-Pin 30 + Triple-Pin 20 + Double-Pin-Pair
30 = 110ish, or the earlier "60-chamber" set). I enumerated **every** set
partition of $\{0,\dots,4\}$ into blocks, every choice of host per block of
size $\ge2$, and every choice of bisect/leave-untouched for singleton
blocks, subject to the true legality constraint (total cuts $=\sum(|B|-1)+
\#\text{bisected singletons}\le4$) — **536 distinct structural chamber
specs** (before per-instance feasibility filtering on $p$). This is a
genuine widening beyond every named sub-family on file, since e.g. it
includes "4-block host + untouched (not bisected) singleton," a variant of
Triple-Pin the file never separately named or coverage-tested (R30.2 only
analyzed the bisected-singleton version and explicitly showed a related
"$p_d$-untouched" special case can fail — but that was for one ad hoc
target formula, not this fully general per-point best-of-all-chambers
check).

I first validated the enumeration against known results: both round-30
witnesses $p=(11,7,6,3,2)/29$ and $p=(14,7,5,3,1)/30$ reproduce the exact
reported `best_phi = 1/2`, margin $-1/62$ against $a_4T=16/31$ — exact
match to the file's own hand computation, confirming my code is a faithful
independent re-implementation, not a bug-prone guess.

### Search 1 — continuous global optimization over the residual box
Parametrized $p=(1,p_2,p_3,p_4,p_5)$ (WLOG $T$ scaled via $p_1=1$),
restricted to the residual $\mathcal R=\{p_1<T/2,\ T/31<p_2<8T/31\}$, and
searched for a point where $\min_{\text{chambers}}\Phi(p) > a_4T$ (a
violation) using: 300,000 uniform random samples, 6 independent
`differential_evolution` runs (global, nonsmooth-tolerant) with polish, and
1000+ `Nelder-Mead` local restarts from random starts. **No violation was
found anywhere.** The best (least-covered) value found — $\min_{\text{ch}}
\Phi(p)-a_4T$, floats — stayed strictly negative throughout, converging
repeatedly (independently, from different search methods/seeds) to values
around $-0.002$ to $-0.02$, at points whose coordinates cluster near dyadic
ratios $(p_1:p_2:p_3:p_4:p_5)\approx(1:\tfrac12:\tfrac14:\tfrac3{16}:
\tfrac18)$-type vectors sitting near (but strictly inside) the $p_2\to
8T/31^-$ boundary of $\mathcal R$.

### Search 2 — exact confirmation at a near-worst point
Converted the best float candidate to the exact rational
$p=(16,8,4,3,2)/33$ ($T=33$) and re-checked with exact `Fraction`
arithmetic (not floats): membership confirmed ($p_1/T=16/33<1/2$,
$p_2/T=8/33\in(1/31,8/31)$); the winning chamber is the partition
$\{\{1\}(p_2\text{ untouched}),\ \{0,2,3,4\}(\text{host }p_1)\}$ — i.e.
match $p_1$ against $p_3,p_4,p_5$ exactly (residual $\rho=16-4-3-2=7$),
leave $p_2=8$ untouched (only 3 of the 4 cuts used) — giving
$\Phi=(33+|8-7|)/2=17$ exactly, vs. $a_4T=528/31\approx17.032$: margin
$\bf-1/31$, i.e. **covered**, by a small but strictly negative exact
margin. This is a genuinely different chamber than either round-30 witness
used (an *untouched*-singleton Pin variant, not a bisected one).

### Search 3 — exhaustive exact sweep over small integer markings
Ran a fully exhaustive (not sampled) integer sweep over every sorted
5-tuple $(p_1,\dots,p_5)$ with $\sum p_i=D$ for $D=5,\dots,25$ landing in
$\mathcal R$ (399 exact points checked, all denominators $\le25$,
`/tmp/round-31/exhaustive_small.py`), each checked against all 536
chambers exactly. **Zero violations.** The worst cases here are the
symmetric all-equal markings ($p_i\equiv D/5$), which are covered by a
comfortable exact margin of $-1/62$ relative to $T$ (i.e. $-D/62$
absolute) — far from the danger zone; the truly close-to-tight points
found by the continuous search (margin $\sim-1/(31\cdot33)$ relative) have
larger, non-small-integer denominators and were not hit by this $D\le25$
integer sweep, consistent with why round 29's naive 20k/30k random samples
also missed them until specifically targeted.

### Conclusion (honest scope — this is strong evidence, not a proof)
Across three independent and much broader verification methods (a true
outer-minimization search — not family-restricted, not a fixed small
chamber list, but the literal full general Partition Chamber Theorem's
536-way legality-and-feasibility-filtered enumeration — plus an exact
small-integer exhaustive sweep), **no counterexample to $n=4$'s residual
region $\mathcal R$ coverage was found.** This is meaningfully stronger
evidence than round 29's retracted claim (which checked only 60 named
chambers against 20–30k random samples and missed two real
counterexamples that a *targeted* search later found) — here the full
536-chamber structural family was checked, and the search explicitly
targeted near-worst points via optimization rather than uniform sampling
alone. **This does NOT constitute a proof.** It does not rule out: (a) a
genuine counterexample at an even more extreme/adversarial rational point
my optimizer did not find (nonsmooth global optimization is not
exhaustive); (b) the theoretical possibility that the *true* worst case
needs more than 4 cuts' worth of partition-chamber structure entirely
(i.e., is not a Partition Chamber instance at all — recall $n=3$'s own
history, where 4 successive named families each had to be superseded
before the true covering set was found).

### What a Farkas-style covering proof would need
1. **Vertex/tight-set identification.** My search's repeated convergence to
   dyadic-ratio-type points near the $p_2\to8T/31^-$ boundary (not at a
   round-30-style "$\rho=0$" degenerate vertex) suggests the *true* tight
   vertices of the covering arrangement are not the two already-found
   witnesses but a different family sitting near this boundary — a future
   round should treat this boundary strip as the priority region to
   characterize exactly (which specific chambers are tight there, as a
   function of $p_2/T\to8/31$).
2. Given 536 structural chamber types is too large for a by-hand
   case-by-case proof, the proof needs the same reduction round 29's
   `find_extra_pins.py`-style diagnostic did for the 60-chamber family
   (identify the small subset — likely $\ll536$ — of chambers that are
   *ever* the actual argmin somewhere in $\mathcal R$), then an exact
   algebraic case split (in the style of the already-certified $n=3$
   `gap-filler-four-chamber-covering`/`case-b2-n3-covering-closure`
   6-branch arguments) showing those chambers jointly cover $\mathcal R$.
3. Alternatively, a genuine LP-duality/Farkas certificate per sub-region
   (nonnegative combination of the chamber inequalities implying
   infeasibility of "all chambers exceed $a_4T$ simultaneously") — this is
   the literal target the approach's own name promises but has not yet
   been attempted at $n=4$ (only sampled/searched).

### Candidate technique(s)
- Push the R30.1 Partition Chamber Theorem's generality further: my search
  shows the *untouched*-singleton Pin variants (not just bisected) matter
  — worth formally adding these as named chambers alongside Triple-Pin,
  Double-Pin-Pair for future coverage bookkeeping.
- The dyadic-ratio near-worst family found here ($\approx(1,\tfrac12,
  \tfrac14,\tfrac3{16},\tfrac18)$-type) is worth checking against the
  $n=3$ project's own history: at $n=3$ the true worst case (R24-27) also
  turned out to sit near a specific corner of the case-(b2) box requiring
  an ad hoc 4th/7th chamber, not the naive dominant ones — a genuinely
  analogous pattern one level down.

### Knowledge-base / lemma entries used
- `bisect-subset-lemma`, `pair-insensitivity-corollary` (the mechanism
  underlying the entire Partition Chamber Theorem, R30.1), certified in
  `lemmas/`.
- `partition-chamber-theorem` (R30.1, certified round 30) — the object
  I exhaustively instantiated.
- No new crux-corpus entries consulted this pass (out of scope for this
  specific numerical-verification lens; see other explorers' reports for
  corpus analogues).

### Dead ends / cautions for the outliner
- Do **not** re-run naive random sampling alone (round 29's mistake) as
  "evidence of coverage" — my search shows the near-worst points sit in a
  narrow band that pure uniform sampling under-weights; any future
  coverage claim should specifically stress-test the $p_2\to(8T/31)^-$,
  $p_1\to(T/2)^-$ corner region with targeted (not just uniform) search
  before trusting a percentage.
- The 536-chamber structural enumeration is itself not exhaustive over
  *all* legal 4-cut strategies (it only covers "partition + host + bisect"
  shapes) — a truly adversarial worst-case marking could in principle need
  a strategy outside this template entirely (unproven either way).

### Small-case / intuition notes (conjecture, not proof)
- Numerically, the $n=4$ residual region $\mathcal R$ appears fully
  covered by the general Partition Chamber family, with the tightest
  margins (as fraction of $T$) occurring near $p_2/T\to8/31^-$ at
  dyadic-like ratios, not at the two previously-found "$\rho=0$" witnesses
  (which have larger margins, $-1/62$, i.e. are not actually the worst
  case, just the first counterexamples found to the *smaller* 60-chamber
  family).
- No new exact counterexample was found this round.
