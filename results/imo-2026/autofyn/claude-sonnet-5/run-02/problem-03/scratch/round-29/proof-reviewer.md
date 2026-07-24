# Proof review — imo-2026-03, round 29

Reviewed all 3 built slugs against `results/imo-2026-03/current.md`, the
problem statement, `knowledge_base.md`'s rigor rules, and independent
from-scratch verification (fresh exact-`Fraction` Python scripts and
`sympy` symbolic checks — none reused from the builders' own scripts).

## 1. `rank-pigeonhole-budget`

**Verdict: CHANGES REQUESTED.** **True Status: `partial`** (matches the
approach file's own stated Status; no overclaim).

Task was to close as much of the 6-shape residual of $(\star_3)=
\mathrm{MinFloor}(4)$ as possible, and to fix the outline-reviewer's
flagged citation-mismatch bug (misapplying `single-insert-point-vertex-
lemma`, proved only for one free coordinate against a genuinely *fixed*
rest, to a mass-conserving coupled pair, which actually moves at slope
$\pm2$ not $\pm1$).

**What I independently re-verified:**
- **Pair-Insertion Ordering Lemma** ("between" and "above" forms): wrote
  a fresh script computing $A(\{x,p,q,w\})$ directly by sort-and-
  alternate-sum and comparing against both closed-form case formulas —
  200,000 random trials each, **zero mismatches**. This is a genuinely
  correct, elementary, from-scratch replacement for the invalid citation
  — the fix is real, not cosmetic.
- **Shape $(2,0,1,0)$, full closure claim.** Independently re-derived, via
  `sympy`, all 4 case-by-case polynomial simplifications
  ($T-(\text{lemma value})$ reduced to $2f_2-4$, $12-2f_1-2g_1$,
  $2f_2-2g_1-2$, $10-2f_1$ respectively) — **all match the file's claims
  exactly**, and each is manifestly $\ge0$ on the stated domain using only
  $f_1<4$ (plus, in the third case, the file's own sharper $f_3<1
  \Rightarrow f_2>3$ observation, which I confirmed algebraically). Also
  ran a fresh direct 300,000-trial check of $A(U)\ge1$ over the *entire*
  legal domain of shape $(2,0,1,0)$ (not going through the peels at all):
  zero violations, minimum exactly $1$ (consistent with the claimed
  tightness at $f_1=4,g_1=2,g_2=0$).
- **Shape $(2,0,0,1)$'s $f_1<4$ regime.** Same treatment: independently
  re-derived all 4 case polynomials via `sympy` ($2f_2-2e-2$,
  $10-2f_1-2e$, $2f_2-6$, $8-2f_1+2e$) — all match. Direct 300,000-trial
  check of the full domain (both $f_1<4$ and $f_1\ge4$): zero violations,
  min exactly $1$. This corroborates (not substitutes for) the file's own
  honest admission that the $f_1\ge4$ complementary regime is confirmed
  only numerically, not yet hand-derived — a real, correctly-scoped gap.

**No gap found** in what is claimed proved. The claimed scope is precise
and matches what is actually established: shape $(2,0,1,0)$ is fully
closed (both directions, no numerics load-bearing); shape $(2,0,0,1)$ is
half-closed (one regime by hand, one regime numerics-only); the other 4
shapes are honestly reported as untouched. $(\star_3)$ itself remains
open. This is real, verified progress, correctly not overclaimed as
`solved`.

**Lemma certified:** `pair-insertion-ordering-lemma` — both forms
verified independently (200,000 trials each), plus all 8 downstream
polynomial reductions re-derived via `sympy`. Certification note appended
to the lemma file.

## 2. `greedy-halving-adversary`

**Verdict: CHANGES REQUESTED.** **True Status: `partial`** (matches the
file's own Status; explicitly re-checked for the stale-overclaim pattern
this file has shown in past rounds — none found this round, continuing
round 28's clean run).

Task was to fix the outline-reviewer's two flagged gaps in the
"Anchor-Switching Lemma trichotomy" outline for $h(m)$'s $q_1$-cut
sub-case: (1) missing vertex-pinning justification before invoking an
anchored-tie bound on an arbitrary continuum $c$; (2) unaddressed
boundary sub-cases.

**What I independently re-verified:**
- **Gap (1) fix.** The file now correctly invokes the certified
  `single-insert-point-vertex-lemma` with the genuinely fixed rest
  $S=\{x,q_1-x\}\cup\text{tail}$ (this *is* the lemma's correct
  hypothesis, unlike the sibling `rank-pigeonhole-budget`'s earlier
  misuse on a coupled pair), correctly pinning the minimizer over
  $c\in[0,q_1]$ to exactly 5 candidate points before any further argument.
  This is a valid, non-circular application.
- **Insert-Bound Corollary** ($|A(\{y\}\cup T)-A(T)|\le y$): re-derived
  and re-verified with a fresh script, 200,000 trials, **zero
  violations**. A correct, elementary one-line consequence of the
  certified slope lemma.
- **Vertices 1-4** ($c=0,q_1,x,q_1-x$, plus the symmetric boundary
  $x=q_1/2$): wrote an independent, from-scratch script computing
  $A(\{c\}\cup S)$ directly (not via the file's intermediate identities)
  for $m=3,\dots,8$, sweeping $x$ densely over $(0,q_1/2]$ and every
  vertex type including all tail elements $t$ (i.e. also stress-testing
  the honestly-open Vertex 5): **zero violations across every case
  tested**, corroborating both the 4 closed vertex types and the
  numerically-only Vertex 5 claim. Vertex 4's geometric-series algebra
  ($A(\text{tail})=f(m)\cdot(2^m+(-1)^{m-1})/3$, reducing to
  $2^{m-1}\ge3+(-1)^{m-1}$) checks out exactly at $m=3,4$ by direct hand
  computation matching the file's own worked examples.
- **Vertex 5.** Correctly and honestly left open — the file names the
  precise obstruction (peeling loses a factor of $2x$ against a gain of
  only $t$) rather than hand-waving past it, and clearly labels its own
  3000-trial-per-$m$ check as corroboration, not proof.

**No gap found.** The claimed scope (4 of 5 vertex types closed
unconditionally for $m\ge3$, modulo only the pre-existing strong-induction
dependence already on file; Vertex 5 and the tail-refining complementary
piece both explicitly open) matches what is actually proved. This is a
genuine, correctly-scoped narrowing, not an overclaim.

**Lemma certified:** `insert-bound-corollary`.

## 3. `lp-duality-certificate`

**Verdict: CHANGES REQUESTED.** **True Status: `partial`** (matches the
file's own Status).

Task was to sequence free transplants for $n=4$'s upper bound, narrow the
residual, instantiate Bisect-Subset-Lemma at $n=4$, and measure coverage
before attempting new hand-derived chambers.

**What I independently re-verified:**
- **Three free transplants** ($p_2\le T/31$, $p_2\ge8T/31$, $p_1\ge T/2$):
  re-checked the threshold arithmetic by hand
  ($(a_3-a_4)T/(2a_3-1)=8T/31$ with $a_3=8/15,a_4=16/31$: matches
  $a_4T/2=8T/31$ exactly) — correct, pure instantiation of already-general
  lemmas, no new gap.
- **Double-Bisect-Pin Theorem** (the round's one genuinely new proved
  result): re-derived and re-verified the exact closed form
  $\Phi_{i,j;k,l}=(T+|p_k-p_l-p_r|)/2$ with a fresh script directly
  constructing the un-reduced 8-element fragment multiset and computing
  $\Phi$ by sort-and-take-odd-ranks, for 20,000 random 5-piece markings
  and random index choices $(i,j,k,l,r)$: **zero mismatches.** This is a
  correct, gap-free, general identity (relies only on the already-
  certified `pair-insensitivity-corollary`, applied 3 times to 3 distinct
  doubled values — a valid use since each of $p_i/2,p_j/2,p_l$ occurs
  exactly twice in the fragment multiset).
- **100% coverage claim.** The file is explicit and correct that this is
  **empirical only** (50,000+ exact-`Fraction` trials, zero violations)
  and that no Farkas-style exhaustive covering argument has been derived.
  This is exactly the right level of caution given this project's own
  documented rounds-24-26 lesson (a numerically-clean covering family can
  still hide a real exact counterexample) — correctly not claimed as a
  theorem.

**No gap found; no overclaim.** The one new proved theorem
(Double-Bisect-Pin) is genuinely established; the coverage claim built on
top of it is honestly and correctly flagged as unproved. $n=4$'s upper
bound is not closed.

**Lemma certified:** `double-bisect-pin-family-n4` — certification scoped
explicitly to the closed-form identity only (not the separate empirical
coverage claim, which remains open and is not part of what's certified).

## Net effect / current.md

All three approaches made genuine, independently-verified, honestly-
scoped progress; **no overclaim found in any of the three files this
round** (continuing round 28's clean run — a good sign the population has
internalized the project's repeated overclaim lessons). None closes its
own round-29 target in full. Updated `results/imo-2026-03/current.md`
with a new "Round 29" entry (Status remains `partial`) summarizing all
three fronts and recommending next steps (finish the remaining 4
$(\star_3)$ shapes; find a mechanism for Vertex 5 or prove it can't be
closed this way, plus the untouched tail-refining $q_1$-cut piece;
attempt the Farkas-style covering proof for the 60-chamber $n=4$ family).

## Outcomes recorded

- `rank-pigeonhole-budget` — `advanced` (closed 1 shape fully, 1 half, via
  a new certified lemma fixing a real citation bug).
- `greedy-halving-adversary` — `advanced` (closed 4 of 5 vertex types via
  a new certified corollary and a correct vertex-pinning fix).
- `lp-duality-certificate` — `advanced` (new proved Double-Bisect-Pin
  Theorem plus a precisely narrowed, though still empirical-only,
  residual for $n=4$'s upper bound).

## Lemmas certified this round

- `results/imo-2026-03/lemmas/pair-insertion-ordering-lemma.md`
- `results/imo-2026-03/lemmas/insert-bound-corollary.md`
- `results/imo-2026-03/lemmas/double-bisect-pin-family-n4.md` (identity
  only; the coverage claim built on it remains uncertified/open)
