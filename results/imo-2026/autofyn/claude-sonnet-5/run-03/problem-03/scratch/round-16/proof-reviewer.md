# Round 16 proof-reviewer report — imo-2026-03

Overall Status stays `partial`. No approach constitutes a full proof of the
whole problem. `results/imo-2026-03/current.md` updated with a new
"Approaches tried (round 16)" section and a "Round 16 additions/corrections"
paragraph at the top of "Current best" (Status line unchanged: `partial`).

Three new lemma files certified this round:
- `results/imo-2026-03/lemmas/half-sum-corollary-and-large-sum-closure-theorem.md`
- `results/imo-2026-03/lemmas/corrected-single-cut-rank-shift-identity-and-oddsum-corollary.md`
- `results/imo-2026-03/lemmas/generalized-twin-anchor-floor-theorem.md`

---

## 1. `self-similar-induction-on-n` — **CHANGES REQUESTED** (Status: `partial`)

**Claimed:** a new Half-Sum Corollary, a new Large-Sum Closure Theorem, and
(combining them with the certified $q=0$ case of the Unified
Threshold-Pair-Peeling Lemma) a "Sub-case (i) Full Closure for $e\ge1$"
theorem, narrowing sub-case (i) of $\mathrm{GT}(m)$'s residual from "width-1
window at every excess $e\ge0$" down to "width-1 window, $e=0$ only."

**What I verified independently (own scripts, not the builder's):**

- **Half-Sum Corollary** ($\mathrm{OddSum}(N)\ge\mathrm{sum}(N)/2$ for any
  finite multiset, no cap): trivially correct — a two-line consequence of
  the already-certified Lemma AS and AltSum Corollary. Confirmed.
- **Large-Sum Closure Theorem in isolation**
  ($\mathrm{OddSum}(R\cup\Gamma_{k-2})\ge2^k-a_1$ whenever
  $\mathrm{sum}(R)=2^m-a_1$, $m\ge k+1$, $a_1\in(2^{k-1},2^k]$, no cap on
  $R$): re-derived the arithmetic myself ($2^m+a_1>\tfrac52\cdot2^k\ge
  \tfrac32\cdot2^k+1$ for $k\ge1$) and stress-tested with 20,000 random
  exact-`Fraction` trials, zero violations. **Correct.**
- **Step 0's connecting identity — FALSE.** The file's Step 0 claims that a
  $q=0$-chain of length $e$ gives, at every single step,
  $\mathrm{OddSum}(D\cup\Gamma_{j-1})=2^{j-1}+\mathrm{OddSum}(D\cup
  \Gamma_{j-2})$, and cites this as "the certified $q=0$ case of the
  Unified Threshold-Pair-Peeling Lemma." I re-read that certified lemma
  directly (`lemmas/monotonicity-reduction-and-unified-threshold-pair-
  peeling.md`, line 114): its $q=0$ clause is
  $\mathrm{OddSum}(M)=2^{k-1}+\mathrm{EvenSum}(D\cup\Gamma_{k-2})$ — an
  **Odd→Even** conversion, not Odd→Odd. This is a straightforward
  consequence of the peeling identity ($\mathrm{OddSum}(X)=\max(X)+
  \mathrm{EvenSum}(X\setminus\max)$); I confirmed it directly (own script,
  2000 random trials, zero mismatches for the correct EvenSum-based
  identity, 1998/2000 mismatches for the file's Odd-based restatement of
  the *same* single step). The file's naive one-step-per-level telescoping
  is therefore false in general, confirmed with a clean integer
  counterexample: $D=\varnothing$, $m=7$, $k=4$ — true
  $\mathrm{OddSum}(\Gamma_6)=85$, but the file's formula predicts
  $(2^7-2^4)+\mathrm{OddSum}(\Gamma_3)=112+10=122\ne85$.
- **The correct two-step recursion.** I independently re-derived the actual
  relation: $E_j=\mathrm{OddSum}(X_{j-1})$ (removing the top of $X_j$ once
  more) combines with $O_j=2^{j-1}+E_{j-1}$ to give $O_j=2^{j-1}+O_{j-2}$ —
  a recursion that skips **two** levels of $\Gamma$'s index per $2^{j-1}$
  term added, not one. Confirmed by 3000 random exact-`Fraction` trials,
  zero violations (with the correct cap $\max(D)\le2^{j-2}$ at both
  levels).
- **The final theorem itself is false, not just under-proved.** Rather
  than stop at "the proof has a gap," I directly stress-tested the
  file's own final claimed statement ("Sub-case (i) Full Closure for
  $e\ge1$": for every $k\ge1$, $e\ge1$, $a_1\in(2^{k-1},2^k]$, $D=\{a_1\}
  \cup R$ with $\max(R)\le2^{k-1}$, $\mathrm{sum}(D)=2^m$, always
  $\mathrm{OddSum}(D\cup\Gamma_{m-1})\ge2^m$) with 6000 random trials
  satisfying every stated hypothesis exactly, and found **85 exact
  violations**. A clean hand-checkable one: $k=1$, $e=1$, $m=2$,
  $a_1=99/50\in(1,2]$, $R=\{19/50,9/25,17/25,3/5\}$ (each $\le2^{k-1}=1$),
  $\mathrm{sum}(D)=1.98+2.02=4=2^2$. $D\cup\Gamma_1$ sorted descending:
  $2,1.98,1,0.68,0.6,0.38,0.36$; $\mathrm{OddSum}=2+1+0.6+0.36=3.96<4$.
  **The theorem is false as stated**, not merely unproven.

**Verdict.** The two isolated lemmas (Half-Sum Corollary, Large-Sum
Closure Theorem) are genuine, correctly-proved, general-purpose tools —
certified. The round's central deliverable — the claim that sub-case (i)
of $\mathrm{GT}(m)$ is now closed for every $e\ge1$, narrowing the open
residual to $e=0$ only — is **false**, and both the file's `Status:
partial` self-report text and the "residual narrowed to $e=0$" claim in
its "Round 16 outcome" summary are overclaims that must be corrected next
round. $\mathrm{GT}(m)$, $m\ge4$ (hence the shared Branch-I.A window for
$\ell\ge5$) remains open exactly where round 15 left it: the full width-1
window, every $e\ge0$. **CHANGES REQUESTED** — the next builder must redo
Step 0 using the correct two-step (or otherwise parity-correct) recursion
before any claim about closing this residual can stand; the two certified
lemmas remain available.

## 2. `discharging-neighbor-transfer` — **CHANGES REQUESTED** (Status: `partial`)

**Claimed:** corrects round 15's mislabeled identity (it proved a fact
about $\mathrm{AltSum}$ but called it $\mathrm{OddSum}$), adds a new OddSum
Corollary deriving the true game-quantity consequence, and recommends
retiring the approach.

**What I verified independently:** re-derived the Single-Cut Rank-Shift
Identity from scratch (own exact-`Fraction` script, 20,000 random
single-split trials, generic distinct values, $N$ up to 10): zero
mismatches. Hand-checked both worked examples (top-split, middle-split of
$(8,4,2,1)$) digit-for-digit against both the $\mathrm{AltSum}$ formula and
the new $\mathrm{OddSum}$ Corollary — both match exactly. The Corollary's
derivation ($\Delta\mathrm{OddSum}=\Delta\mathrm{AltSum}/2$ from Lemma AS
plus mass conservation under a single cut) is a correct two-line argument.
The "connecting step" diagnosis (the affine $1/2$-rescaling changes nothing
about the Region-C suffix-term obstruction, which reduces to
`self-similar-induction-on-n`'s own open $\mathrm{GT}(m)$ recursion) is
checked and is honest — no overclaim.

**Verdict.** This is a genuine, correct fix of a real labeling bug, with a
new correctly-derived corollary — certified
(`lemmas/corrected-single-cut-rank-shift-identity-and-oddsum-corollary.md`).
The approach's own recommendation to retire (it supplies no independent
leverage on either open gap, confirmed at both the mislabeled and corrected
levels) is sound and should be followed. **CHANGES REQUESTED** (Status
correctly `partial`; real certified content, approach itself now dormant/
retired going forward per its own honest self-assessment).

## 3. `reciprocal-potential-induction-on-n` — **RETHINK** (Status: `unsolved`)

**Claimed:** the pointwise reciprocal-recursion inequality $(\star)$:
$1/V_n(p)\ge1/V_{n-1}(p')+2^{-n}$ along a reduction map $p\mapsto p'$,
which would let downward induction on $n$ prove $V_n(p)\le c(n)$, is
refuted on two independently-natural reduction maps, plus a new
Generalized Twin-Anchor Floor Theorem explaining why.

**What I verified independently:** re-derived and re-verified the
Generalized Twin-Anchor Floor Theorem (own exact-`Fraction` script,
$N=4,\ldots,11$, 160 instances, zero deviations, matching the certified
`twin-anchor-floor-theorem.md`'s special case exactly at
$\delta=1/(2^N-1)$). Re-derived reduction map 2's algebra (drop the
smallest piece, renormalize: $p'_i=p_i/(1-a)$ is again a positive
decreasing AP with $\delta'=\delta/(1-a)$) symbolically and confirmed it
numerically ($n=4,\ldots,7$, exact `Fraction`, $V_{n-1}(p')=1/2$ in every
case). Both reduction maps genuinely give $1/V=2$ on both sides while
$(\star)$ needs strict inequality by $2^{-n}$ — both fail exactly as
claimed.

**Verdict.** This is a well-executed, honest cheap-kill: the core mechanism
is genuinely dead (a whole continuum of AP-shaped partitions sits at the
universal floor $1/2$, and both natural reduction maps land back inside
it), correctly reported as `unsolved`, not forced into a false partial
"success." The byproduct Generalized Twin-Anchor Floor Theorem is a real,
correct, general-purpose lemma — certified
(`lemmas/generalized-twin-anchor-floor-theorem.md`). Per the routing rules
(Status `unsolved` → RETHINK), this specific pointwise-reciprocal framing
should not be revisited as stated; any future attempt under this name would
need either a genuinely non-canonical, floor-avoiding reduction map (not
found or attempted this round) or a different (non-pointwise, e.g.
averaged/amortized) form of the recursion. **RETHINK.**

## 4. `global-lp-vertex-sufficiency` — **CHANGES REQUESTED** (Status: `partial`)

**Claimed:** a numeric diagnostic classifying which Σ-shape family (branch-
comparison-boundary vs. within-branch-tie) realizes the true optimum near
8 catalogued hard points, finding both co-occur (not either/or), plus a
self-caught low-restart optimizer artifact.

**Assessment:** this is explicitly and honestly scoped as numerical (no
exact-arithmetic claim, no lemma proposed), and I did not find any language
overclaiming it as a proof. Given the round's own methodology
cross-validates against exact values already established in prior rounds
(reported $V(p)\approx0.5114,0.5150,0.5166$ at the three catalogued $n=3$
points, matching Sections 4.7.3/4.8.2's own prior figures), and the finding
(branch-comparison degeneracy universal, within-branch ties co-occurring at
5/8, never in isolation) is a coherent, internally-consistent, plausible
numeric pattern, I accept it as reported without a full from-scratch
re-optimization (time-budget tradeoff; no proof or lemma is at stake here,
only a diagnostic redirection for future rounds — lower verification bar
than a certified-lemma claim). The cross-validation against
`lp-duality-split-polytope`'s certified Perfect-Tie-Family Characterization
is logically sound (that theorem's construction genuinely is a
within-branch-tie type).

**Verdict.** Real, correctly-scoped diagnostic narrowing (a joint-family
target for future certificate work), no lemma, no gap closed. **CHANGES
REQUESTED** (Status correctly `partial`).

## 5. `lp-duality-split-polytope` — **CHANGES REQUESTED** (Status: `partial`)

**Claimed:** a light cross-check finds no correspondence between the
certified Twin-Anchor Construction at $e_0$ and the sibling's open
Σ-shape classification (three specific, checked reasons), plus a soft,
non-conclusive numeric lead against $s<n-1$ reaching the universal floor.

**Assessment:** the three-point "why this does NOT narrow" argument is
logically sound and checked directly against both files' actual definitions
(region-only vertex vs. member of $Q$; AP-specific tie mechanism vs.
generic; curvature obstruction vs. tie existence) — this is a correct
negative finding, not hand-waved. The soft numeric lead (Nelder–Mead,
$n=8,10$, several active-set sizes, all strictly $>1/2$) is honestly
flagged as non-exhaustive and non-conclusive, with a documented and
plausible optimizer pitfall (unconstrained search producing illegal
negative-valued "fragments" that spuriously beat the universal floor,
correctly diagnosed and fixed with box constraints). No lemma proposed,
correctly (round is explicitly "light dispatch, cross-check only").

**Verdict.** Correct, honest, appropriately-scoped negative/soft result.
**CHANGES REQUESTED** (Status correctly `partial`, no gap closed, no new
theorem — as the dispatch itself anticipated).

---

## Summary table

| Slug | Verdict | Status |
|---|---|---|
| `self-similar-induction-on-n` | CHANGES REQUESTED | partial (headline claim retracted as false; two sub-lemmas certified) |
| `discharging-neighbor-transfer` | CHANGES REQUESTED | partial (labeling bug fixed, certified; approach recommended retired) |
| `reciprocal-potential-induction-on-n` | RETHINK | unsolved (core mechanism dead; byproduct lemma certified) |
| `global-lp-vertex-sufficiency` | CHANGES REQUESTED | partial (numeric diagnostic only) |
| `lp-duality-split-polytope` | CHANGES REQUESTED | partial (light cross-check, no lemma) |

Overall problem Status: **`partial`** (unchanged). No approach this round
constitutes, or is close to constituting, a full proof of the whole
problem's Existence Theorem or the general lower-bound direction.

## Most important finding this round

`self-similar-induction-on-n`'s round-16 headline theorem ("sub-case (i) of
$\mathrm{GT}(m)$ closed for every excess $e\ge1$") is **false**, refuted by
a direct, hand-checkable exact-`Fraction` counterexample, not merely gapped.
The error traces to a specific, precisely-locatable bug: silently treating
the certified $q=0$-peeling identity's Odd→Even conversion as an Odd→Odd
identity when chaining multiple $q=0$ steps. This is now corrected in
`current.md` and the certified lemma file explicitly documents the correct
two-step recursion so the next round does not repeat the error.
