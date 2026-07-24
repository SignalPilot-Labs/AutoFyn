## imo-2026-03 — n=4 generalization scouting (lens: does the n=3 chamber-family technique scale?)

### Summary verdict
The n=3 upper-bound proof (`lp-duality-certificate`, now fully closed:
$c(3)\le8/15$, no numerics load-bearing, round 27 APPROVE-at-own-scope) is
**not one monolithic n=3-specific argument** — it is a mosaic of (i) several
fully general-$n$ lemmas/theorems that transplant to n=4 "for free," and
(ii) one genuinely n=3-specific finite chamber census (case (b2), the middle
$p_2$-strip / $p_1<T/2$ regime) that took ~15 rounds (13→27) to close and
whose own internal signals (chamber-density growth 28%→64% between n=3 and
n=4 samples, an already-observed need for *sub-splitting* single chambers
into families) point to real combinatorial growth, not a routine repeat.
**There is a genuine, cheap, nearly-mechanical partial win available first**
(see "Free bootstrap" below) before the expensive part is attempted.

### What is already n-agnostic (transplants to n=4 with ~zero new proof)
Read from `lp-duality-certificate.md` §1–§4 and the "Promotable lemmas"
blocks:
- **Case (b1)** ($p_2\le T/D_n$, $D_n=2^{n+1}-1$): closed by
  `unconditional-p2-threshold-closure`, proved and certified **for every
  $n\ge1$** (built from `bisect-top-identity` + `max-domination-lemma` +
  `telescoping-threshold-identity`, all general-$n$). At $n=4$, $D_4=31$,
  so this handles $p_2\le T/31$ immediately, zero new work.
- **Case (a)** ($p_2\ge a_nT/2$): closed by the certified **Corollary**
  (Theorem B recursive sufficient condition) reducing to a 3-element
  instance $S'=\{p_1-p_2,p_3,p_4,\dots\}$ (in general, the tail after
  peeling $p_2$), discharged by the *general* $n=2$ upper-bound lemma
  `n2-upper-bound-lp-argument`. The file explicitly flags this as a
  **noted bootstrap**: "Case (a) *does* bootstrap for free one level up
  ($n=4$'s case (a), $p_2\ge a_4T/2$, closes by the identical Corollary
  mechanism with $m=5$, since `n2-upper-bound-lp-argument` still discharges
  the same reduced-triple hypothesis)" — stated but **not yet built** (round
  26 deferred it deliberately). This is a genuine, essentially-free
  sub-target for round 28.
- **The $p_1\ge T/2$ regime as a whole** (broader than case (a) alone): §3–4
  give an *independent*, structurally cleaner route via Theorem C′ + Theorem
  A, which needs only "$P(n-1)$ fully closed for an arbitrary tail" as
  induction hypothesis. Since round 27 makes $P(4)$ (the full $n=3$ upper
  bound, both regimes, every marking) **completely closed for the first
  time**, the file's own §4 argument (which closed $n=3$'s $p_1\ge T/2$ half
  using the then-already-complete $P(3)$ = general $n=2$ bound) can now be
  **repeated verbatim one level up**: $P(5)$'s (i.e. $n=4$'s) $p_1\ge T/2$
  half closes by (i) Theorem A directly for $T/2\le p_1<a_4T$, (ii) Theorem
  C′ + full $P(4)$ as IH for $p_1\ge a_4T$. This is explicitly the pattern
  the file itself diagnosed as blocked past $n=3$ *only because* $P(4)$'s
  $p_1<T/2$ half wasn't closed yet ("§5... Since $P(4)$'s $p_1<T/2$ half is
  not established, the induction cannot be pushed past $n=3$ using this
  mechanism alone") — **that blocker is now removed by round 27.** This
  bootstrap is broader than case (a) alone (it covers ALL $p_1\ge T/2$, not
  just $p_2\ge a_nT/2$), and it is close to mechanical: re-run §4's proof
  with $n=3\to n=4$, citing the now-complete round-27 theorem as $P(4)$.
- General multiset machinery used throughout the chamber work — `odd-run-
  reduction-lemma`, `pair-cancellation-identity`, `cross-term-reduction-
  theorem`, the new `pair-insensitivity-corollary` — are all stated and
  proved for **arbitrary $n$/arbitrary multisets**, so the *tools* used to
  derive n=4 chamber closed forms carry over; only the *enumeration of which
  chambers exist and that they cover the residual region* is n=4-specific.

### What is genuinely n=3-specific and must be redone at n=4
Case (b2) (the middle $p_2$-strip, further split at $p_1<T/2$ vs
$p_1\ge T/2$) was closed only via an ad hoc finite covering family: a
5-chamber family (round 25, Farkas-certified) for $p_1<T/2$, plus a
4-chamber Gap-Filler family (round 27, Farkas-certified) for $p_1\ge T/2$.
Each chamber is a specific cut-allocation "type" (e.g. Bisect$\{1,4\}$,
Triple-Pin, Double-Sandwich) whose closed form and feasibility region were
hand-derived and whose *joint covering* of the residual polytope required
an explicit nonnegative-combination (Farkas) certificate per case. None of
this machinery is stated for general $n$ — every chamber formula and every
covering certificate is n=3-specific arithmetic (uses $a_3=8/15$, $D_3=15$
explicitly). At n=4 this is a **fresh enumeration problem**, not a
corollary.

**Concrete scale-up signal already on file** (from the round ~20-24 `p`-
space Chamber-Vertex Theorem work): a sampling test of "how many distinct
tie-vertex compositions occur" found **28% of sampled compositions at n=3
vs 64% at n=4** are distinct/non-reducible — the file itself calls this "a
genuine amber flag for whether a [uniform closed-form] mechanism ... can
close case (b2) in general." Separately, round 23-24 found that even within
n=3 case (b2), single "template" chambers are individually insufficient (no
one chamber's own feasibility region avoids failure points) and a *family*
of 5, then a further 4, chambers with explicit Farkas certificates was
needed just to cover one $n=3$ residual region. At n=4 with 5 pieces
$p_1,\dots,p_5$ and up to 4 cuts to allocate, the composition space (how
many cuts land on each of the 5 pieces, subject to budget $\le4$, further
refined by tie-patterns among resulting fragments) is substantially larger
than n=3's 4-piece/3-cut space — the number of distinct chamber "types"
plausibly grows combinatorially (rough estimate: n=3 needed ~9+ chamber
types across all regimes by round 27; if growth tracks the observed 28%→64%
density more than doubling, n=4 could plausibly need on the order of 2-4x
as many distinct chamber types, i.e. roughly 20-35+, though this is only a
rough extrapolation, not a proof of the count).

### Is there a shared induction that avoids re-enumeration?
Partial, not full. The Theorem C′/Theorem A mechanism gives a genuine,
reusable **inductive step for the $p_1\ge T/2$ half only**: "if $P(n-1)$ is
fully closed (both regimes), then $P(n)$'s $p_1\ge T/2$ half closes for
free." This is now unlocked one more level (n=3→n=4) by round 27's closure.
But it does **not** touch the $p_1<T/2$ half at all — that half's closure
at each level has so far always required a fresh finite chamber census
specific to that level's threshold $a_n$ (the file's own diagnosis: "the
two regimes are not independent halves ... Theorem C′'s regime consumes the
*other* regime's result one level down as a prerequisite" — i.e. the
$p_1<T/2$ half is exactly the piece induction cannot reach). So the
technique gives a **half-free, half-must-redo** pattern at every level: each
new $n$ gets its $p_1\ge T/2$ half for free (via the completed $P(n-1)$),
but must pay the full chamber-census cost again for $p_1<T/2$. No
telescoping shortcut for the hard half was found on file, and this
explorer found none either — the case-(b2) chamber machinery is inherently
tied to $n$'s specific ladder ratio $a_n$ and piece count.

### Recommended first sub-target at n=4 (in order of cheapness)
1. **Build the $p_1\ge T/2$ closure at $n=4$** by literally repeating §4's
   proof one index up, citing round 27's now-complete $P(4)$ (general $n=3$
   upper bound) as the induction hypothesis for Theorem C′. This is close
   to a copy-paste-and-reindex exercise (Theorem A already general-$n$;
   Theorem C′ already general-$n$; the Corollary's threshold algebra
   already general-$n$ via the Telescoping Threshold Identity) — a cheap,
   real, non-trivial extension that should be attempted before any new
   chamber work. This alone would leave only $p_1<T/2$ open at $n=4$,
   narrowing the target precisely (mirroring exactly what happened at n=3
   after §4 closed).
2. Separately, **case (a) at n=4** ($p_2\ge a_4T/2$) can be written up as
   its own explicit corollary too (redundant with step 1 above since it's
   a subset of $p_1\ge T/2$, but cheap to state for the record / cross-
   check against the p2-partition framing used in rounds 26-27).
3. Only then attempt the hard part: enumerate n=4's case-(b2) chambers.
   Recommend starting from the **cheapest possible sub-slice** analogous to
   how n=3 built up incrementally (single-composition chambers first, e.g.
   "bisect $p_1$ only," "bisect $p_1,p_2$," before attempting full covering
   families) rather than attempting a full n=4 covering proof in one round
   — this is what let n=3 accumulate ~15 rounds of chamber lemmas before the
   Farkas covering closed it, and n=4 should expect comparable or greater
   effort per the density-growth signal.

### Cheap-kill candidates
None obvious for skipping the chamber census itself — the amber-flag signal
argues against expecting a shortcut. The one genuine cheap win is item 1
above (structural, not case-work): it is a real reduction in the size of
the n=4 problem (eliminates the $p_1\ge T/2$ half entirely) achievable in
well under a full round, essentially just re-citing already-general lemmas
with $n=4$ substituted and citing round 27's theorem as the new base case.

### Knowledge-base / crux corpus check
`knowledge_base.md` has no entries matching "chamber," "Farkas," "LP
duality," or polytope-vertex covering arguments — this machinery was built
entirely within the approach file, not imported from the KB. Queried the
crux corpus (`past_crux_moves_database.json`, `domain=combinatorics`,
`subtopic=games-and-strategy`, 39 entries) for a genuine analog to
"finite polyhedral-chamber covering via Farkas certificates for a
continuous cutting/marking game." None of the 39 entries resemble this
mechanism — the closest superficial matches (`aimo-0117`'s dyadic-sequence/
defer-commitment idea) were already tried and rigorously ruled out
(`claiming-order-invariant`, round 4, RETHINK — do not retry). **No
genuinely analogous crux found**; this project's chamber-covering machinery
appears to be a bespoke construction with no close precedent in the corpus,
consistent with this being an original IMO-P3/P6-difficulty combinatorial
game rather than a variant of a known competition problem.

### Dead ends (do not retry, confirmed from current.md / lemma files)
- `case-b2-n3-covering-closure`'s domain generalization to "no restriction
  on $p_1$" is **refuted** (counterexample $p=(3/5,9/40,29/200,3/100)$,
  round 26) — the $p_1<T/2$ restriction on the 5-chamber family is
  permanent; any n=4 analog must expect the same kind of split (the
  Gap-Filler 4-chamber family for $p_1\ge T/2$ was a genuinely separate
  mechanism, not a widening of the 5-chamber one).
- `claiming-order-invariant` (defer-commitment framing, aimo-0117-style):
  structural dead end, RETHINK verdict, do not re-attempt.
- Two round-6 framings (`integer-lattice-reduction`, `bijective-mersenne-
  pairing`) are unrelated to the chamber technique but remain project-wide
  dead ends.
- `simplex-exchange-smoothing-vertex-maximization` (round 10): statement
  has a real gap (missing $0$ in the pin set) — not certified as currently
  written; if reused for n=4 chamber vertex work, must first restate with
  pin set $\{0,\tau_1,\dots,\tau_r\}$ per the round-10/11 fix, not re-derive
  from scratch (the fix is already recorded in `lemmas/`).

### Small-case / intuition notes (conjecture, not proof)
- Given the 28%→64% density growth and the observed need to sub-split even
  single n=3 chambers into families, it is plausible (not proven) that
  closing n=4's case (b2) will require noticeably more than n=3's ~9
  chamber types and correspondingly more Farkas certificates — this project
  should budget several rounds for it, consistent with round 27's own
  recommendation to pivot to n=4 "now that n=3's upper bound is fully
  closed."
- The lower-bound/achievability direction at n=3 (Liu Bang's ladder forcing
  $\Phi\ge8/15T$) is **still completely open** — round 27's milestone is
  upper-bound only. A full n=3 solve (both directions) is arguably a
  cheaper near-term target than starting n=4's chamber census, since it
  reuses the already-large lower-bound toolkit (Claim A/B machinery,
  `case-ii-closure-theorem`, `sigma2-untouched-closure-theorem`, etc.)
  built up over rounds 4-27, rather than opening new n=4-specific
  combinatorics. This is an alternative next-round target worth weighing
  against n=4, per round 27's own dual recommendation ("pivot to $n=4$ ...
  or to the $n=3$ lower-bound/achievability direction to complete a
  genuinely full $n=3$ solve").
