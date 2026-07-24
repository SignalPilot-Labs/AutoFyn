# Round 8 proof-reviewer report — imo-2026-03

Reviewed all four slugs built this round. Verdicts below are independent per
slug, as required. All numeric/algebraic re-derivations are my own
fresh scripts (not re-reads of the builders' own scripts), at
`/tmp/round-8/*.py`.

---

## 1. `rank-pigeonhole-budget` — Verdict: **APPROVE** (at its own declared
scope, Claim (A))

**Claim under review.** Claim (A): for every $n\ge1$, over every partition
$F$ of the ladder's top piece $p_1$ into $\le n$ cuts (tail $T$ completely
untouched), $A(F\cup T)\ge a_n:=1/(2^{n+1}-1)$, with an explicit $F^\ast$
attaining equality. The approach's own header explicitly scopes "solved"
to *this* claim, not the whole `imo-2026-03` problem, consistent with the
round-5-onward decomposition this project has used throughout.

**What is genuinely new this round.** §5, the "Case I Closure Theorem"
(every element of $F\le\tau_1=p_2$). This is the piece that had been open
since round 5/6/7 (isolated as sub-case $(\dagger)$ in round 7). The
mechanism is a full pivot away from every peel-induction attempt on file:
an **exchange-smoothing vertex-maximization** argument that reduces the
continuum optimization of $E(F\cup\tau)$ to a finite "pinned + one tied
group" family (§5.1), evaluated via `odd-run-reduction-lemma` (§5.4), then
closed by two new elementary facts (**Ratio-2 Spacing Lemma**, §5.3;
**Last-Element Bound**, §5.5) plus the already-certified `half-bound-lemma`
and its trivial dual $A\le\mathrm{Total}$, split across three exhaustively
covered sub-cases ($q$ even, §5.5; $q$ odd/box-bound-binds, §5.6; $q$
odd/domain-bound-binds, §5.7, itself split into $j=0,1,\text{even}\ge2,
\text{odd}\ge3$, all four covered).

**Independent re-derivation performed (the load-bearing step).** I
re-derived and re-checked every piece of §5 from scratch, not by re-reading
the builder's algebra:

1. **Continuum check, not just vertex check.** Wrote a coordinate-ascent
   numerical optimizer (`optimize_search.py`) that searches the *full*
   polytope (not restricted to the claimed vertex family) from many random
   starts, maximizing $E(F\cup\tau)$ directly. Across 3000 random
   $(m,\tau_1,s,k)$ instances, the best margin found ($R(\tau)-\max E$) was
   $\approx1.9\times10^{-8}$ — i.e. numerically zero, matching predicted
   equality, and never negative. This is independent evidence the
   *statement* (not just the vertex-restricted argument) is true and tight,
   which is the strongest external check available short of a from-scratch
   Lagrangian derivation.
2. **Exhaustive exact-`Fraction` re-derivation of all three §5 branches**
   (`verify_57.py`), $m=1,\dots,10$: 5120 configurations for the $q$-odd
   sub-case (a), 2046 for sub-case (b), 2036 for the $q$-even branch — **zero
   violations**, independently reproducing (with a different enumeration
   scheme) the builder's own reported 6655-configuration, zero-violation
   check.
3. **Ratio-2 Spacing Lemma and Last-Element Bound**, re-derived exhaustively
   for $m\le10$, every nonempty subset (`verify_lemmas.py`): both hold with
   zero exceptions.
4. **Identity $R(\tau)+\tau_m=2\tau_1$** (§5.5), re-checked for $m=1,\dots,8$:
   holds exactly.
5. **Achievability construction $F^\ast$** (§2), re-verified exactly for
   $n=1,\dots,9$ (`verify_achievability.py`): $A(F^\ast\cup T)=a_n$ exactly
   every time, **and** this independently confirmed a genuine correction the
   builder flagged: $F^\ast$ uses exactly $n$ cuts (Xiang Yu's whole
   budget), not $n-1$ as an earlier-round lemma file's prose stated. The
   underlying identity was never wrong, only the cut-count claim in the
   prose — this correction is now propagated to `claim-a-full-closure.md`.

No gap was found anywhere in §5.1–§5.8; the case split is complete ($q$
even / $q$ odd $\times$ sub-case (a)/(b), and within (a) every $j\ge0$), the
Vertex-maximization Proposition's exchange argument is a valid, correctly
adapted dualization of the already-certified `vertex-minimum-theorem`
mechanism (min $\to$ max; I checked no min-specific step survives — the
compactness/continuity argument is symmetric), and the "worst case at
minimal pins" reduction (§5.4) is justified separately and correctly for
both the $q$-even branch (trivially, since $A(S)=A(X)$ there does not
depend on pins/$v$ at all) and the $q$-odd branch (via the proved
Monotonicity Lemma, §5.7).

**Combined with the already-certified Case II Closure Theorem (round 6,
independently re-verified then), Claim (A) is fully closed for every
$n\ge1$, both directions, with no numerics substituting for any step.**

**Scoping check — this is the crux of the dispatch instruction.** The
approach file's own "Open gaps" section correctly states Claim (B) and the
general upper bound remain open and are sibling approaches' targets. *But*
its Status-header scope note says "Claim (B)... and the general upper bound
are proved by sibling approaches" — **this is false and I am correcting it**
in `current.md`: as of this round, Claim (B) is *not* proved in general
(`greedy-halving-adversary` proves it only for fully-paired $F$ with
leftover budget, and explicitly finds it is vacuous-but-not-established at
Claim (A)'s own tight optimum), and the general upper bound is *not* proved
(`lp-duality-certificate` explicitly stops short). I have written
`current.md` to state plainly: Claim (A) is a fully closed, certified
milestone; the whole `imo-2026-03` problem remains `partial`.

**Verdict: APPROVE at the approach's own declared scope (Claim (A)).** The
approach's Status field ("solved," scoped explicitly to Claim (A)) is
accurate and not an overclaim of the whole project. `current.md`'s
top-level Status stays `partial`, as instructed, since Claim (A) is only
one of the pieces (Claim (B), general upper bound) the whole theorem needs.

**Lemmas certified** (all held to full bar, `sorry`-free, statements no
stronger than proved): `exchange-smoothing-vertex-maximization.md`,
`ratio-2-spacing-lemma.md`, `last-element-bound.md`,
`case-i-closure-theorem.md`, `claim-a-full-closure.md` (this last one
states the scope caveat explicitly, per the reviewer correction above).

---

## 2. `rank-tie-vertex-reduction` — Verdict: **CHANGES REQUESTED**

**Claim under review.** General $c_1\ge2$ lower bound, attacked this round
via strong induction on $\ell(S)=|S'|$ (odd-run-reduced size) instead of
raw element count.

**Result: a genuine, rigorous negative result**, not a failed guess. Two
new lemmas, both re-verified by hand as correct elementary facts:
- **Parity Coincidence Lemma** ($\ell(S)\equiv|S|\pmod2$): a three-line
  double-counting argument, trivially correct — I re-derived it
  independently and it checks out exactly as stated.
- **Zero-Iff Lemma** ($\ell(S)=0\iff A(S)=0$): standard
  telescoping-positivity argument for the alternating sum of a strictly
  decreasing positive sequence — correct.

Together these *prove* (not merely suggest) that induction on $\ell$ faces
the identical even/odd case split, on the identical instances, as induction
on $N=|S|$ — so it cannot "decouple" from the parity obstruction that has
now stalled three independent peel mechanisms (`rank-pigeonhole-budget`'s
former peel-the-min, this file's own round-7 peel-the-max, and this round's
peel-on-$\ell$). The §7.3–7.4 case analysis (one-element peel odd/even,
two-element peel) is algebraically correct (standard rank-sign
bookkeeping, re-checked by hand) and the concrete witness verification
($n=3$, $F=\{4,2,2\}/15$) is arithmetically correct.

**Honest note on this negative result's real value.** It correctly and
usefully rules out an entire class of mechanisms (not just this specific
attempt), and — importantly — it *also* independently corroborates why
`rank-pigeonhole-budget`'s round-8 success worked: that approach's
exchange-smoothing mechanism structurally never removes a single element
and asks about resulting rank parity, exactly the escape route this file's
own §7.5 diagnoses as necessary. This cross-approach consistency is a good
sign neither result is spurious.

**What remains open:** general $c_1\ge2$ (the file's actual target) is not
closed; this negative result narrows the search space but does not itself
make progress toward a positive proof.

**Verdict: CHANGES REQUESTED.** Real, certifiable progress (a general
dead-end proof, not a vague failure), approach stays live targeting either
an upper-bound mechanism on the reduced foreign-mass instance, or reusing
`rank-pigeonhole-budget`'s newly-proved exchange-smoothing machinery for
the $c_1\ge2$ configurations that Claim (A)'s framework does not cover
(mixed cuts on $p_1$ and tail).

**Lemma certified:** `parity-coincidence-and-zero-iff-dead-end.md`.

---

## 3. `greedy-halving-adversary` — Verdict: **CHANGES REQUESTED**

**Claim under review.** Restricted Claim (B): refining Xiang Yu's tail cuts
can never push $A$ below Claim (A)'s value $a_n$, for $F$ at/near Claim
(A)'s optimum.

**New lemmas, both independently re-verified.**
- **Safe-Window Lemma** (Lemma 17): every legal tail refinement stays
  $\le p_2$. A straightforward induction on cut count; correct, and a
  legitimate standalone extraction of a fact already implicit in the
  certified `half-window-vanishing-lemma`.
- **Cross-Term Vanishing Lemma** (Lemma 18): if $F$ is fully-paired
  ($A(F)=0$), $A(F\cup G')=A(G')$ exactly for every legal tail refinement
  $G'$. I wrote a fresh, independent 3000-trial exact-`Fraction` script
  (`verify_greedy.py`, built without reference to the builder's own script)
  generating random fully-paired $F$'s (random $t\in\{1,2,3\}$, random
  positive pair-weights) and random tail refinements ($0$–$3$ random cuts):
  **zero mismatches**. The proof's case split ($t=1,a_1=p_2$ vs. every
  pair-value $<p_2$) and the cross-term-vanishing argument via
  `cross-term-identity-threshold` are correct.

**Honest and valuable negative/diagnostic finding.** The approach correctly
identifies that Claim (A)'s own optimal witness $F^\ast$ is (i) not
fully-paired, so the new lemma doesn't apply to it, and (ii) — independently
confirmed by my own re-derivation above — uses Xiang Yu's *entire* $n$-cut
budget, so restricted Claim (B) is vacuous exactly there (no tail-refinement
budget left). This correctly narrows Claim (B)'s genuinely open remainder
to $F$'s using fewer cuts on $p_1$, with an unpaired residual — the case
that actually determines the general lower bound's behavior when Xiang Yu
mixes his budget between $p_1$ and the tail.

**Verdict: CHANGES REQUESTED.** Two genuinely new, correct, general-purpose
lemmas plus an honest, precise diagnosis of what remains (not a vague
"still working on it"). Claim (B) in its useful generality (non-fully-paired
$F$, budget split between $p_1$ and tail) remains open.

**Lemmas certified:** `safe-window-lemma.md`, `cross-term-vanishing-lemma.md`.
(Proposition 16, being conditional on the same lower bound one level down,
is *not* certified as a standalone unconditional lemma — correctly flagged
as such in the approach file itself.)

---

## 4. `lp-duality-certificate` — Verdict: **CHANGES REQUESTED**

**Claim under review.** The general upper bound $c(n)\le a_n$ for arbitrary
Liu Bang markings (redirected target this round, a legitimate pivot from
the lower-bound obstruction, not a same-mechanism retry).

**New identities.** Four exact, unconditional closed-form strategies
(Theorem A Full-Match, B One-Step-Peel, C Bisect-Top, D
Bisect-Top-and-Bottom). I independently re-derived Theorems C and D's
closed forms against direct sort-and-sum computation on 2000 fresh random
markings (`verify_lpdual.py`, sizes $m=2,\dots,8$): **zero mismatches** —
both formulas are exactly correct as stated. (Theorem A and B are
straightforward applications of the already-certified `leftover-formula`/
`pair-cancellation-identity`; I did not re-derive these from scratch since
their mechanism is standard and already certified elsewhere, but spot-checked
the algebra of Corollary B's threshold derivation by hand and it is
consistent.)

**Honest, correctly-scoped stopping point.** The three proven (non-crude)
sufficient conditions combine into a rigorously proven sub-domain
$\mathcal D_m$ that the builder itself reports covers only
$\approx16$–$20\%$ of random configurations — an honest, not inflated,
number. The stronger claim (the *combined* min-of-four strategy always
achieves $\le a_nT$) is extensively numerically stress-tested (exhaustive
$n=2$ grid of 85,320 points, $150{,}000+$ random/adversarial trials up to
$n=6$, both known hard witnesses solved) but is explicitly and correctly
**not** claimed as proved — "no general-$n$ closed-form theorem... has been
proved this round" is stated plainly in the file, matching what is actually
established.

**Verdict: CHANGES REQUESTED.** Real new general-purpose machinery (four
exact identities, reusable independent of this approach), a genuinely
distinct half of the theorem (the upper bound) advanced with no overclaim.
The central gap (a from-scratch proof that the four-strategy combination
suffices for every $n$) remains.

**Lemmas:** the approach file proposes `one-step-peel-identity`,
`bisect-top-identity`, `bisect-top-bottom-identity`,
`full-match-achievability` for certification. I did not copy these to
`lemmas/` this round (Theorem A/B are close restatements of already-
certified `leftover-formula`/`pair-cancellation-identity` combined with
straightforward algebra rather than qualitatively new content; Theorems C/D
are new and reviewer-confirmed correct but I am leaving their formal
certification to a round that actually reuses them, to avoid lemma-file
sprawl for identities not yet load-bearing elsewhere — this is a judgment
call, not a rejection; a future round is free to certify them on reuse).

---

## current.md update

Updated `results/imo-2026-03/current.md`:
- Added a new "Round 8" entry to `## Approaches tried` documenting Claim (A)'s
  full closure as a major verified milestone (with the reviewer's own
  independent re-derivation summarized), the corrected scoping (Claim (B)
  and the general upper bound are *not* proved by siblings, contra the
  approach file's own header wording), and honest summaries of the other
  three slugs' real progress.
- `## Status` remains `partial` — the whole `imo-2026-03` problem (both
  bound directions, for all $n$, answer stated and verified) is not proved:
  Claim (B) in its useful generality and the general upper bound both
  remain open.
- `## Full proof` remains absent (correctly — Status is not `solved`).

## Lemmas certified this round

`exchange-smoothing-vertex-maximization.md`, `ratio-2-spacing-lemma.md`,
`last-element-bound.md`, `case-i-closure-theorem.md`,
`claim-a-full-closure.md`, `safe-window-lemma.md`,
`cross-term-vanishing-lemma.md`,
`parity-coincidence-and-zero-iff-dead-end.md` — all in
`results/imo-2026-03/lemmas/`.

## Verification scripts (all fresh, independent of builders' own scripts)

`/tmp/round-8/verify_caseI.py` (17,321 random Case-I interior trials, zero
violations), `/tmp/round-8/optimize_search.py` (coordinate-ascent continuum
maximizer, margin $\to0$, no violation), `/tmp/round-8/verify_lemmas.py`
(identity 5.4 + Last-Element Bound, exhaustive $m\le10$/$11$),
`/tmp/round-8/verify_57.py` (exhaustive §5.5–5.7 branch re-derivation,
$m\le10$, 9202 configs, zero violations), `/tmp/round-8/verify_greedy.py`
(Cross-Term Vanishing Lemma, 3000 trials, zero mismatches),
`/tmp/round-8/verify_lpdual.py` (Theorems C/D, 2000 trials, zero
mismatches), `/tmp/round-8/verify_achievability.py` (Claim (A) achievability
$F^\ast$, $n=1..9$, exact match + cut-count correction confirmed).
