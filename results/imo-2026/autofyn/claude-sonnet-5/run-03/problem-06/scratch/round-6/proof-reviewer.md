# Proof review — round 6 — imo-2026-06

Reviewed all 5 built approach files (mtimes 01:52–01:58 UTC, consistent with
builder reports at `/tmp/round-6/proof-builder-*.md` — no report file exists
for `active-set-stabilization` or `scalar-difference-majorization` builds
specifically, but their content was reviewed directly in the approach files
and is internally consistent with the outline-reviewer's assigned targets).
Every hand-traced numeric claim across all 5 files was independently
re-simulated (exact-integer Python + `sympy`), not merely trusted from
prose. **All checked out exactly, no discrepancies found**, except one minor
labeling nit (see active-set-stabilization below) that does not affect any
load-bearing claim.

## 1. renormalization-induction-on-seed — CHANGES REQUESTED

**Status: partial (correct self-assessment).**

New content this round (§8): the General $a_2=a_1+p$ Lemma (fully general,
no hypothesis on $\omega(a_1)$) — re-derived from scratch and correct: for
$1\le t<p:=\min R(a_1)$, no prime factor of $a_1$ can divide $t$ (every
prime factor is $\ge p>t$), so $\gcd(a_1+t,a_1)=1$; $a_1+p$ is divisible by
$p$, hence valid; minimality gives $a_2=a_1+p$. Its odd-seed corollary
($2p\mid a_2$) is immediate.

The round-6 outline's "two covering agents" mechanism is **fully refuted**,
not merely left open, by the new **Odd-Anchor Lemma**: since $a_1$ odd
$\Rightarrow 2\notin R(a_1)$, parity of a candidate $m$ carries zero
information about $\gcd(m,a_1)>1$ (verified: $m=2$ is even & coprime to
$a_1$; $m=2p$ is even & shares $p$). This is a clean, correct, three-line
impossibility proof, not hand-waving.

Independently verified the new counterexample: $a_1=45$ gives
$45,48,50,54,60,66,70,72,75$ — I re-simulated this exactly (Python, exact
`gcd`) and it matches term-for-term, confirming $a_2,\dots,a_8$ all even but
$a_9=75$ odd, refuting the "stays even forever" fallback.

**No overclaiming.** The odd-seed extension of Step 2 (periodic activity of
$p=\min R(a_1)$ for odd $p$) remains genuinely open; the file says so
explicitly. This is real, non-circular narrowing (two mechanisms killed with
full proofs, not just numerics) on top of the already-solved even-seed
sub-case. Gap remaining: a mechanism for odd $\min R(a_1)$ that isn't
parity-based, bounded-lookahead, or naive locking (all three now dead).

## 2. active-set-stabilization — CHANGES REQUESTED

**Status: partial (correct self-assessment).**

New content (Contamination framework): the Contamination Dichotomy Lemma
(trivial dichotomy on singleton-vs-non-singleton intersection) and the
Reduction Proposition (localizes the Bounded-Witness-Index Conjecture to a
per-prime, per-reference-index search) are both correct — I re-derived both
from scratch; each is essentially a one-line consequence of definitions, but
genuinely useful bookkeeping (converts a global existential into an
independent family of search problems).

The $a_1=20735$ hand-trace was independently re-simulated in full: I
regenerated the sequence from the raw greedy definition and confirmed every
factorization claimed ($a_4=20748=2^2\cdot3\cdot7\cdot13\cdot19$,
$a_{13}=20805=3\cdot5\cdot19\cdot73$, $a_{27}=20900=2^2\cdot5^2\cdot11\cdot19$,
$a_{41}=20995=5\cdot13\cdot17\cdot19$, $a_{55}=21090=2\cdot3\cdot5\cdot19\cdot37$,
$a_{70}=21185=5\cdot19\cdot223$) and every claimed intersection with the
obstruction set $O=\{2,3,7,13\}$ — exact match, no discrepancy.

**One minor discrepancy found (non-load-bearing):** the file reports the new
adversarial instance $a_1=29315$ has largest witness index $32$; my
independent re-simulation over the first 40 terms found the witness index
for prime $17$ (the largest of $\{2,3,17,23\}$) is $33$, not $32$ (an
off-by-one, possibly from a different indexing convention or truncation
range). This is explicitly labeled as numerical evidence, not a proof step,
so it does not affect any certified claim — flagging it so the number is
corrected if cited again, but not grounds for downgrading the verdict.

The Bounded-Witness-Index Conjecture itself is **neither proved nor
refuted** this round, and the file says so honestly ("the obstruction to a
general proof... appears to require essentially the same kind of global
control... as the original central gap"). Central gap untouched.

## 3. state-compactness-pigeonhole — CHANGES REQUESTED

**Status: partial (correct self-assessment).**

New §13 is a complementary, bottom-up hand-trace of the same $a_1=20735$
outlier (obstruction-set-size heuristic), independently re-simulated by me
and confirmed exact (same factorizations as approach #2 above, cross-checked
independently against $a_1=385$ and $a_1=194287$). The heuristic
probability-of-avoidance argument is explicitly and correctly labeled
non-rigorous ("the sequence is fully deterministic... no proof that this
expectation-style bound holds in general").

This is legitimate mechanism-diversity on the shared central gap (bottom-up
instance diagnosis vs. active-set-stabilization's top-down localization
framework), not a redundant re-skin — the outline-reviewer's call that this
qualifies as genuine diversity is correct. No new certified lemma is
produced (builder correctly self-reports this); central gap untouched.

## 4. scalar-difference-pigeonhole — CHANGES REQUESTED

**Status: partial (correct self-assessment).**

The mandatory Step 0 fix (sums-vs-factors collision) is **fully and
correctly resolved**, refuting the round-6 outline's proposed Complexity
Bound Lemma. I independently re-derived the abstract collision (Claim 6.1.1:
$(2,4,2,\ldots,2)$ vs. $(3,3,2,\ldots,2)$, equal sum, distinct tuples — a
valid witness whenever $R\ge4,k\ge2$) and, more importantly, independently
re-simulated the realized-instance collision for $a_1=35$: regenerating the
full gap sequence $d_1,\ldots,d_{17}$ from scratch, I confirm
$(d_8,d_9)=(5,4)$ and $(d_{16},d_{17})=(4,5)$ exactly as claimed, both
summing to 9. I also independently computed $p(2)=16$ and $S(2)=8$ over an
extended (2999-term) simulation, exactly matching the file's claimed values.
This decisively kills the window-sum-counting mechanism as stated (no
patch is possible, since the failure is genuine non-injectivity on realized
factors, not a slack constant).

Theorem 6.2.2 (conditional: Unified Central Claim $\Rightarrow p(k)\le T$)
is a correct, free chaining of two already-certified lemmas
(`transient-free-finishing-theorem.md` + elementary periodic-word factor
counting) — re-derived from scratch, no gap. The honest report that the
converse direction needs two separate unresolved hurdles (Morse-Hedlund only
gives eventual, not full, periodicity; no transient-removal argument exists
independent of the $Q$-machinery) is correct and appropriately scoped.
Central gap untouched, but a specific dead mechanism (window-sum counting)
is now cleanly closed off — real progress in narrowing the search space for
this line.

## 5. scalar-difference-majorization — CHANGES REQUESTED

**Status: partial (correct self-assessment).**

This new fork (from `scalar-difference-pigeonhole`) proves the **Excess
Growth Rate Lemma**: for eventual periodicity $a_{n+T}=a_n+L$ ($n\ge n_0$)
and any fixed-rate affine candidate $\hat a_n=a_1+(n-1)c$, the excess
$e_n:=a_n-\hat a_n$ satisfies $e_{n+T}-e_n=L-Tc$ exactly. I re-derived this
from scratch (a three-line algebraic identity) — correct, no gap. Applied to
$a_1=35$ with the claimed true period $(T,L)=(34,210)$: I independently
verified this periodicity holds exactly for the tested range (checked
$n=1,\ldots,166$ at $T=34$ over a 200-term simulation, zero exceptions), and
independently re-derived the Lemma's prediction $e_6=0,e_{40}=40,e_{74}=80$
via direct simulation of $e_n=a_n-(35+(n-1)\cdot5)$ — exact match. This
decisively and rigorously kills the single-affine-rate majorization
mechanism (not just the naive candidate but any fixed-rate variant,
including one derived from the Positive-Density Upgrade's witnessed value,
via a genuine circularity argument: the correct rate $L/T$ is exactly the
theorem's unknown output). No repair is possible for this exact mechanism.
This is a clean, correctly-scoped negative result (a 10th dead mechanism for
the population, alongside window-sum counting as the 9th) — the file
correctly does not overclaim progress on the central gap itself.

## Cross-cutting notes

- **Diversity check confirmed.** The 5 approaches remain genuinely
  distinct in mechanism (Q/Nec localization via two independent hand-trace
  styles; parity-based induction-on-seed refutation; two independent
  scalar/prime-free framings). No collapse to a single shared wall this
  round, consistent with the plateau-break requirement.
- **No overclaiming detected anywhere.** Every builder correctly reported
  `partial` and did not claim to have closed the central gap. Two
  mechanisms (window-sum counting for factor-complexity; single-affine-rate
  majorization) are now proved dead with full rigor, joining the existing
  list of 8 dead mechanisms in the Rules — bringing the total to 10.
- **The central existence gap** (finiteness of $\mathrm{Nec}$ /
  self-sufficiency of $Q_{\min}$, equivalently existence of a finite
  self-sufficient $Q$) remains **completely open after 6 rounds**. No
  approach in the population has yet found a route around it; every fresh
  mechanism attempted this round (contamination localization, obstruction-
  set heuristics, parity arguments, factor-complexity reformulation,
  affine majorization) either narrows the search space or gets killed
  cleanly, but none closes it.
- **Certified 5 new lemmas** this round (all independently re-derived
  and/or re-simulated): `general-a2-formula.md`, `odd-anchor-lemma.md`
  (negative), `contamination-dichotomy-and-reduction.md`,
  `factor-complexity-basics.md` (includes a negative sub-result: window-sum
  counting does not bound factor complexity), `excess-growth-rate-lemma.md`
  (negative). Files written to `results/imo-2026-06/lemmas/`.
- **Updated `results/imo-2026-06/current.md`**: added a "Round 6 additions"
  section (Status remains `partial`); recorded all 5 outcomes via
  `record_outcome` (renormalization-induction-on-seed: advanced;
  active-set-stabilization: partial; state-compactness-pigeonhole: partial;
  scalar-difference-pigeonhole: advanced; scalar-difference-majorization:
  dead-end for its specific mechanism).

## Overall verdict summary

| Approach | Status | Verdict |
|---|---|---|
| renormalization-induction-on-seed | partial | CHANGES REQUESTED |
| active-set-stabilization | partial | CHANGES REQUESTED |
| state-compactness-pigeonhole | partial | CHANGES REQUESTED |
| scalar-difference-pigeonhole | partial | CHANGES REQUESTED |
| scalar-difference-majorization | partial | CHANGES REQUESTED |

No RETHINK (no approach's core mechanism was found unsound this round —
even the two "dead mechanisms" killed this round, window-sum counting and
single-affine-rate majorization, are specific sub-mechanisms within live
approaches that retain other unexhausted content, per the same convention
used in prior rounds for e.g. jacobsthal-covering-bound's dead sub-attempts).
No APPROVE (the central gap remains fully open; the IMO problem is not
solved this round). The run's overall Status remains `partial`.
