# Round 18 proof-reviewer report — imo-2026-03

All three round-18 builds independently re-derived from scratch (own
`sympy` symbolic scripts, own exact-`Fraction` combinatorial scripts,
own `scipy` constrained-optimization scripts — none of the builders'
own scripts reused for verification).

## 1. `self-similar-induction-on-n` — CHANGES REQUESTED (Status: partial, correct)

**Claims checked:**

(a) *Sharper residual-range derivation.* The file claims that the
already-certified Claim B (odd-excess) formula
$\mathrm{LB}_{\mathrm{odd}}-T_{\mathrm{odd}}=\tfrac{2^k}6+\tfrac{2^m}6-
\tfrac{a_1}2-\tfrac12$ holds for the *whole* range $a_1\in(2^{k-1},2^k]$
(not just the window), and specializing at $m=k+1$ ($e=1$) gives
$\tfrac{2^k-a_1-1}2\ge0\iff a_1\le2^k-1$. **Independently re-derived
both the general identity and its specialization with a fresh `sympy`
script** — exact match in both cases. This genuinely narrows the true
open residual to $a_1\in(2^k-1,2^k]$ (a width-1 window at the *top* of
the range), correcting the previously-believed-open range
$[2^{k-1}+1,2^k]$. **Correct, certified.**

(b) *$k=2$ instance of the Cardinality-Constrained Half-Sum Lemma.*
Claim: for $\max(R)\le2$, $|R|\le3$, $\mathrm{sum}(R)=S\in[4,5)$,
$\mathrm{OddSum}(R\cup\{2,1\})\ge(S+4)/2$. The proof's case split is
$n:=|R|\in\{2,3\}$ (exhaustive: $n\le1$ is infeasible since one element
$\le2$ can't reach $S\ge4$, and $|R|\le3$ is $\mathrm{GT}(m)$'s own
cardinality cap). Traced every sub-case by hand:
  - $n=2$: forces $S=4$, $a=b=2$ exactly — correct, no gap.
  - $n=3$, $a=2$ (tie): the "remove a tied pair from the top preserves
    parity of every lower rank" step is a standard, correct rank-shift
    fact (verified: removing an even number of top elements shifts
    every remaining rank by an even amount, preserving parity). The
    three-way split on $b,c$ vs. $1$ is exhaustive and each branch's
    algebra checks out **except one incidental remark**: the
    "$b\ge1>c$" branch asserts the $S=4$ equality boundary "is not
    attained... $c<1$ forces $b>2$" — **this is false**. Counterexample:
    $b=1.5,c=0.5$ satisfies $b\ge1>c$, $b+c=2=S-2$ at $S=4$, $b\le2$ (no
    contradiction), and gives $\mathrm{OddSum}(\{b,c,1\})=2=S/2$ exactly
    — a genuine second equality point, not excluded. **This does not
    invalidate the lemma**: the actual required inequality (weak, $\ge$)
    still holds in this branch; only the extraneous "strict/not attained"
    side-claim is wrong. Flagged, corrected, does not sink the result.
  - $n=3$, $a<2$ (non-tie): peeling $\Gamma_1$'s unique top via the
    certified Global-Max Peeling identity, then splitting on $a$ vs. $1$
    (with $a\le1$ correctly shown vacuous, since it forces $S\le3<4$):
    all sub-cases check out, strict inequality throughout.
  - **Independent numeric cross-check** (own `scipy.optimize.minimize`
    script, `LinearConstraint` for the exact sum-$=S$ constraint,
    `Bounds` $[0,2]$, multi-restart `SLSQP`, avoiding the
    "clip-after-rescale" optimizer artifact this file's own memory
    flags): minimum observed margin $\approx1.2\times10^{-12}$ (i.e.
    machine-precision zero), touching equality exactly as the hand
    proof predicts. **Confirmed correct.**

(c) *General Cardinality-Constrained Half-Sum Lemma (arbitrary $k$).*
Correctly and honestly presented as an **unproved conjecture**
(numerically verified to $\sim10^{-12}$ precision for $k=2,\ldots,6$ via
a correctly-constrained optimizer — the file explicitly flags and
avoids the round-16 unconstrained-optimizer artifact class) — **not**
certified, per the builder's own correct labeling. The diagnosis of why
the natural single-parameter induction on $k$ fails (the post-peel
residual keeps the *original* cap $2^{k-1}$ instead of shrinking to
$2^{k-2}$, so it's a smaller instance of the *same* phenomenon, needing
a two-parameter family) is precise and non-hand-wavy, not just "still
hard."

**Status:** `partial` is the correct self-report — real, certified
progress (narrower residual range + full $k=2$ closure), general case
and $e\ge3$ genuinely still open.

**Certified into `lemmas/`:**
`lemmas/sharper-odd-residual-and-k2-cardinality-half-sum.md` — both (a)
and (b) above, with the cosmetic error in (b) noted and corrected in
the certified writeup. The general conjecture (c) is explicitly **not**
certified.

**Verdict: CHANGES REQUESTED.**

## 2. `global-lp-vertex-sufficiency` — CHANGES REQUESTED (Status: partial, correct)

**Claims checked:**

(a) *Region-membership bug.* The file claims this round's dispatched
$n=2$ near-maximizer candidate ($p_1=0.4705,p_2=0.3363$) violates the
balanced region's own defining inequality $p_1-p_2>\gamma(2)=1/7$.
Independently recomputed exactly: $p_1-p_2=671/5000=0.1342$,
$\gamma(2)=1/7\approx0.142857$; $0.1342<0.142857$ — **confirmed, the
candidate point is genuinely outside the region.** This is a real,
correctly-diagnosed bug in the round's own dispatch premise.

(b) *Closed-form "always $>c(2)$ in-region" theorem.* For the specific
"pin-to-$p_2$/bisect-$p_3$" branch of shape $(1,0,1)$
($M=\{p_2,p_1-p_2,p_2,p_3/2,p_3/2\}$), the file claims: throughout the
true balanced region, $p_2>p_1-p_2>p_3/2$ (giving
$\mathrm{OddSum}(M)=p_1+p_3/2=\tfrac12+\tfrac{p_1-p_2}2$), and since
$c(2)=\tfrac12+\tfrac{\gamma(2)}2=4/7$ exactly (already-certified
identity from a prior round) and the region requires $p_1-p_2>\gamma(2)$
strictly, this branch's value always exceeds $c(2)$ in-region.
Independently re-derived both order-claim sub-proofs from the region's
two gap inequalities by hand (both correct, elementary chains of
inequalities) and **independently stress-tested with a fresh
exact-`Fraction` script**: $50{,}000$ random trials sampling genuine
points of the true balanced region (all three defining inequalities
enforced exactly in `Fraction` arithmetic) — the order claim and the
closed-form identity matched in every single trial, zero violations,
minimum margin over $c(2)$ shrinking towards (but never reaching) $0$ as
$p_1-p_2\to\gamma(2)$, exactly as claimed. **Confirmed correct.**

**Status:** `partial` correct. This closes one narrow branch's
inadequacy as a witness, but the Existence Theorem for $n=2$ (i.e.
$\sup_{\text{balanced}}V(p)\le c(2)$ over *all* $10$ cut-allocations) is
not established in exact arithmetic; $n=3$ shape not reached (honestly
flagged, not overclaimed).

**Certification:** the builder correctly declined to propose this as a
general-purpose promotable lemma (it's narrowly scoped to one branch of
one shape at $n=2$) — agreed, not certified into `lemmas/`.

**Verdict: CHANGES REQUESTED.**

## 3. `lp-duality-split-polytope` — CHANGES REQUESTED (Status: partial, unchanged — correct)

Light/optional dispatch, executed exactly as scoped. Checks whether the
crux corpus's `aimo-0091` (parallel-seam double-counting) or `aimo-0178`
(symmetry-driven triple-counting) mechanisms transplant to the $s\ge
n-1$ necessity conjecture. Read both cruxes' actual mechanisms from the
corpus (not guessed) and checked each against this problem's actual
structure: (a) the "sum over many independent sites" idea is exactly
what the already-certified Generalized Mass-Constraint Theorem already
does (so no new leverage), and its key parity-upgrade trick has no
analogue here (whether an untouched piece needs $1$ vs. $\ge3$ matching
fragments depends on the specific response chosen, not a positional
parity fact); (b) $e_0$'s active/untouched dichotomy over a strictly
monotone AP has no symmetry group to exploit (unlike the cube's
$3$-fold rotation). Both diagnoses are sound, qualitative structural
arguments, not numeric claims requiring independent computation — spot-
checked against the cited certified theorem's actual proof mechanism
(round 17 file) and against the already-certified $e_0$ coordinate
formula (strictly monotone AP, certified in a prior round) — both
checks confirm the file's claims. No new theorem or lemma proposed
(correct, nothing to certify). Status correctly unchanged `partial`.

**Verdict: CHANGES REQUESTED.**

## Ranking outcomes recorded

- `self-similar-induction-on-n`: **advanced** — real, certified narrowing
  of the residual plus a fully closed small case ($k=2$).
- `global-lp-vertex-sufficiency`: **advanced** — a genuine bug catch plus
  a real, independently-verified closed-form theorem (narrowly scoped,
  not certified as a reusable lemma per correct builder scoping).
- `lp-duality-split-polytope`: **dead-end** — light dispatch, purely
  negative/structural finding, no new lemma, no gap closed (per standing
  house rule: negative-only findings with no positive lemma/sub-case
  closed are recorded `dead-end`, not `advanced`).

## Lemma certification

Certified: `results/imo-2026-03/lemmas/sharper-odd-residual-and-k2-cardinality-half-sum.md`
(Lemma 1: sharper odd-residual range at $e=1$; Lemma 2: $k=2$ instance of
the Cardinality-Constrained Half-Sum Lemma — both from
`self-similar-induction-on-n`, both independently re-derived and
verified above, with one cosmetic non-load-bearing error in the source
noted and corrected). The general (arbitrary-$k$) Cardinality-
Constrained Half-Sum Lemma is explicitly **not** certified (unproved
conjecture, correctly labeled as such by the builder).

No lemma proposed or certified from `global-lp-vertex-sufficiency` or
`lp-duality-split-polytope` this round (both correctly declined to
propose one, or the round was purely negative/structural).

## `current.md` updated

Added a new "Approaches tried (round 18)" section at the top of the
history (reviewer-owned file), summarizing all three verdicts above.
Top-level `## Status` remains `partial` (correctly — $\mathrm{GT}(m)$
for $m\ge4$ remains open; the Existence Theorem for the LP-vertex
approach remains open at $n=2$; the necessity conjecture $s\ge n-1$
remains open).

## Net assessment

No approach reached `solved` this round. All three verdicts are
**CHANGES REQUESTED** — two genuine, independently-verified pieces of
progress (a narrower, partially-closed residual in the induction
approach; a bug catch plus a real narrow theorem in the LP-vertex
approach) and one honest negative scouting result (the duality
approach). No overclaims found; all three self-reported `Status:
partial` correctly match the true state after independent review.
