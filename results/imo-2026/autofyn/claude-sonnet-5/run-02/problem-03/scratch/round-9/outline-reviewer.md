# Outline review — round 9, imo-2026-03

## greedy-halving-adversary (Claim (B), ℓ(F)=1 generalization)

**Verdict: CHANGES REQUESTED (approved to build).**

Checked the skeleton against the actual certified machinery it claims to
reuse (`cross-term-identity-threshold`, `safe-window-lemma`,
`odd-run-reduction-lemma`, `half-window-vanishing-lemma`).

- Step 1 (single-residual indicator $u_F\equiv\mathbb1[x<v]$ for
  $F=\{v\}\cup P$, $A(P)=0$): a plausible, low-risk degeneration of the
  already-certified odd-run leftover formula. Not independently re-derived
  by me line-by-line, but it is the kind of fact the certified lemma is
  built to produce, and the outline correctly flags it as "same clean form
  as the two-fragment case," not a new mechanism. Fine to proceed.
- Step 3, case $v\ge p_2$: this reuses `half-window-vanishing-lemma`'s
  proof "verbatim." I checked its two stated prerequisites (clean 0/1
  indicator for $F$; Safe-Window bound on $G'$) are exactly what steps 1–2
  establish for the *general* $\ell(F)=1$ shape, not anything special to
  the old two-fragment $c_1=1$ case — this looks like a genuine, honest
  reuse, not a disguised assumption.
- Step 3, case $v<p_2$: correctly and explicitly flagged as **open**
  ("mechanism not yet fully worked out"), not smuggled in as solved. This
  is the one place a false claim could have hidden ("then it follows") and
  it does not — good.
- Step 5 (scope check for $\ell(F)\ge2$): honestly scoped as "numerically
  checked non-binding at $n=3$ only, not proved," with an explicit
  instruction to re-check at $n=4,5,6$ before trusting the pattern. This is
  the right level of caution — no case is silently dropped, the "Cases to
  cover" list matches what's actually closed vs. open.
- "Watch out for" correctly warns against over-generalizing the $n=3$
  witness $v=p_2$ into a structural fact, and against conflating
  $\ell(F)$ (odd-run of $F$ alone) with $\ell(S)$ for the whole multiset
  (the latter is what `parity-coincidence-and-zero-iff-dead-end` is about
  — reusing that dead-end's parity fact here without re-derivation would
  have been a real error; the outline correctly refuses to do so).

No hidden gap or false claim found: the "solved" part (case $v\ge p_2$) is
a legitimate reuse, and the genuinely new part (case $v<p_2$) is honestly
left open rather than asserted. This is real incremental progress, not a
fragment split off the whole problem — Claim (B) is still the target, only
the case being closed narrows.

**Requested for build:** write up steps 1–2 and case $v\ge p_2$ in full
(should be mechanical given the reuse), attempt case $v<p_2$ via
tail-self-similarity, and run the $\ell(F)\ge3$ numeric check at
$n=4,5,6$ before the write-up claims anything about that range.

## lp-duality-certificate (Theorem C′, $p_1\ge T/2$ regime)

**Verdict: APPROVE the mechanism, CHANGES REQUESTED on scope accuracy (approved to build).**

I independently verified the two load-bearing claims rather than trusting
"near mechanical":

1. **Theorem C′'s exact identity is sound**, and — importantly — sounder
   than the naive concern I initially had. `pair-cancellation-identity`
   (already certified, underlying Theorem C) states $A(S\cup\{v,v\})=A(S)$
   for *any* multiset $S$ and *any* value $v$, regardless of where the pair
   lands in sorted order (inserting a tied pair always shifts everything
   below it by 2 ranks, preserving parity — I confirmed this by hand and
   numerically). So bisecting $p_1$ and then applying *any* further
   strategy to the tail (not just leaving it untouched, as the old
   Theorem C did) still gives the exact identity
   $\Phi = p_1/2 + \Phi(\text{tail strategy})$ **even when $p_1/2 < p_2$**
   — I constructed exactly such a case
   ($p=(0.6,0.35,0.03,0.02)$, so $p_1/2=0.3<p_2=0.35$) and confirmed by a
   `scipy.optimize.differential_evolution` global search that Theorem C′'s
   strategy value (0.505) exactly matches the true global optimum, and
   both are $\le a_3=8/15\approx0.5333$. This was the one place I expected
   a hidden gap (interleaving between the bisected halves and the tail);
   there isn't one. The mechanism is genuinely valid, not a hand-wave.
2. **The threshold-match claim** ($p_1\ge a_nT$ makes Theorem C′'s bound
   $p_1/2+a_{n-1}(T-p_1)$ exactly meet $a_nT$, using the telescoping
   identity) — I recomputed this exactly with `Fraction` for $n=1,\dots,9$
   and confirmed the threshold solves to *exactly* $a_n$ every time, zero
   slack. This is a genuine algebraic pattern (not just small-$n$ luck)
   and the "needs a general-$n$ proof, not just $n\le8$" framing is
   correctly honest — the pattern is very likely provable by induction on
   the telescoping identity as claimed, but that proof still needs to be
   written, so it is correctly listed as an open item, not asserted done.

**Found one factual error to correct before build:** the outline claims
"both on-file hard witnesses live [in the $p_1<T/2$ regime]." I checked
both: $(3/8,1/4,1/4,1/8)$ has $p_1=3/8<T/2$ — correctly open. But
$(6,2,2,1)/11$ has $p_1=6/11\approx0.545 \ge T/2$ — it is **not** in the
open regime; it falls in the $p_1\ge a_3T$ sub-case, and I confirmed
numerically that Theorem C′ actually **closes** it exactly (recursive
value $6/11$, exact match with the global optimum found earlier for this
point). So this witness is resolved by this round's own new theorem, not
still-open as the outline states. This is a scoping/bookkeeping error, not
a fatal flaw — it doesn't affect the correctness of Theorem C′ or the
regime split — but the builder should correct the sentence and record that
only $(3/8,1/4,1/4,1/8)$ remains a live open witness for the $p_1<T/2$
regime.

The $p_1<T/2$ regime is correctly identified as genuinely open (Theorem D's
exact value resolves $(3/8,1/4,1/4,1/8)$ numerically per round-8 findings,
but no proven — as opposed to numerically-checked — sufficient condition
exists yet for that regime), consistent with prior rounds' honest
accounting. Theorem E / vertex-minimum-reuse are reasonable next
mechanisms to try, correctly ranked cheapest-first.

**Requested for build:** (a) formalize Theorem C′ and the general-$n$
threshold proof (algebra is confirmed correct pattern, needs a clean
induction write-up using the telescoping identity), (b) correct the
witness-classification sentence per above, (c) attempt Theorem E or the
vertex-minimum reuse for $p_1<T/2$.

## rank-pigeonhole-budget (no new work this round)

No changes; stays live/registered as Claim (A)'s certified closure home,
consistent with round 8. Nothing to review.

## rank-tie-vertex-reduction (not selected)

Correctly left out of the build set — outliner found no new mechanism
beyond what's already ruled out (peel/ℓ-induction). Agreed; not forcing a
build with no new idea is the right call. Stays registered/live in the
population at its current Elo.

## Diversity check

The two built approaches attack genuinely disjoint halves of the problem
(Claim (B) lower-bound case-closure vs. the general upper bound) using
different vocabularies (window-integral/cross-term vs. LP-style exact
identities + strong induction) — good framing diversity, not a
single-gap trap. Both are whole-problem attempts (each targets its named
half of the full $c(n)=2^n/(2^{n+1}-1)$ claim, not a sub-lemma split off
from a sibling), consistent with the "one slug = one whole attempt" rule.

## Ranking

Ranked the full field via `update_ranking`: `greedy-halving-adversary` and
`rank-pigeonhole-budget` (Claim A's full closure) remain the top two,
`lp-duality-certificate` and `rank-tie-vertex-reduction` close behind (all
four carry real, verified progress); the confirmed dead ends
(`bijective-mersenne-pairing`, `integer-lattice-reduction`,
`claiming-order-invariant`) and the still-thin `dyadic-band-occupancy` /
`exchange-argument-extremal-response` sit at the bottom, unchanged in
relative order from round 8 (no new evidence this round to reorder them
further).

build set: greedy-halving-adversary, lp-duality-certificate
