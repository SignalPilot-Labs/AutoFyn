# Round 14 Proof Review — imo-2026-03

Reviewed both built slugs: `greedy-halving-adversary` and
`lp-duality-certificate`. Problem status remains `partial` — neither slug
closes the full problem; both made genuine, verified progress with no
overclaims found.

## 1. `greedy-halving-adversary`

**Verdict: CHANGES REQUESTED** (Status: `partial`, correctly self-reported).

### Theorem 29 (Half-Dominance Split Bound) + Lemma 29a (Symmetry Lemma)

Claim: fully closes the `p2-Pinned-Dominance Lemma` in one shot, superseding
round 13's Proposition 28 (which only closed the dominant-fragment branch).

**Verified correct, no gap found.**

- **Lemma 29a** (for any multiset $F_2$ with total $M$, $\int_0^{M/2}u_{F_2}
  \ge\int_{M/2}^\infty u_{F_2}$): I independently re-derived the two-case
  argument from scratch. Case (i) ($g_1<M/2$): trivial, $b=0$. Case (ii)
  ($g_1\ge M/2$): the parity identity $u_{F_2}(x)=1-u_{\mathrm{Rest}}(x)$ on
  $[0,g_1)$ is correctly derived (since $N_{F_2}(x)=1+N_{\mathrm{Rest}}(x)$
  there), and the final inequality $a-b=\mathrm{Total}(\mathrm{Rest})-
  A(\mathrm{Rest})\ge0$ follows from the elementary $A(S)\le
  \mathrm{Total}(S)$ bound. The two cases are exhaustive and disjoint (no
  skipped sub-case). I wrote a fresh, independent exact-`Fraction` script
  (`/tmp/round-14/verify_thm29.py`, 20,000 trials, random multisets size
  1–6): **zero violations.**
- **Theorem 29** (for $\max(R)\le M/2$, any split $F_2$ of $M$: $A(F_2\cup
  R)\le M-A(R)$): re-derived the proof independently — the cross-term
  identity (Lemma 8) reduces the claim to a pointwise algebraic inequality
  ($u_{F_2}v_R\ge v_R-(1-u_{F_2})$, checked directly for both values of
  $u_{F_2}\in\{0,1\}$ — correct), which combined with Lemma 29a gives the
  bound. Independently re-verified with a fresh 20,000-trial script over
  generic $M,F_2,R$ satisfying $\max(R)\le M/2$: **zero violations.**
- **Scope/ladder-specificity claim**: verified honest — the theorem itself
  is fully general (no ladder assumption anywhere in its statement or
  proof); the ladder only enters via the Corollary's hypothesis
  $\max(R)\le p_2/2$, supplied by `safe-window-lemma` one level down +
  Lemma 23's $p_2=2p_3$ identity (both already certified). Cross-checked
  against the on-file non-ladder counterexample $\tau=\{49,2/5\}$,
  $m=203/4$: $\max(\tau)=49>m/2=203/8$, so the hypothesis genuinely fails
  there — confirms the theorem does not overreach into the false generic
  statement. **This is a correct, honest, non-overclaimed closure.**
- Full end-to-end simulation on the actual ladder (n=5, random $F_2$ splits
  of $p_2$, random legal tail refinements $R$) confirms the Corollary
  directly: zero violations.

**Genuinely supersedes Proposition 28**: Theorem 29 requires no case split
on $F_2$'s shape, so it correctly closes both the dominant-fragment branch
(Prop 28's old scope) and the previously-open no-dominant-fragment branch in
one proof. Combined with the pre-existing recursive-depth bookkeeping
(unchanged), this closes $(\dagger)$'s entire $p_2$-cut complement — real,
verified progress on restricted Claim (B), at the same recursion depth
already used elsewhere (no new conditioning introduced).

### Proposition 29b ($\ell(F)=2$, $P\ne\varnothing$ sub-case)

Claim: widens the closure threshold from the outline's anticipated
$\tau_P\le f(n)$ to $\tau_P<p_3=p_2/2$, via `sharp-dominant-removal-
identity` (the strict-max version, not the standard total-mass version).

**Verified correct, no gap found, and honestly scoped.**

- Verified the "$P$'s exact pairs are parity-invisible even when unioned
  with an extra reference set $G$" fact (a straightforward, transparent
  generalization of the already-certified `single-residual-indicator`
  mechanism — not hand-waved, the underlying reasoning is that exact pairs
  contribute an even count to $N(x)$ for every $x$, regardless of any other
  set unioned in): fresh 20,000-trial script, zero mismatches.
- Verified `sharp-dominant-removal-identity` ($A(\{f_1\}\cup T)=f_1-A(T)$
  for $f_1>\max(T)$): fresh 20,000-trial script, zero mismatches.
- Verified the algebraic chain $t^*=p_2-\tau_P>p_3\ge\max(G')$ under
  $\tau_P<p_3$ — correct, using $p_2=2p_3$ (Lemma 23) and `safe-window-
  lemma` one level down.
- Ran a full end-to-end simulation directly on the $n=5$ ladder (random
  $F=\{v_1,v_2\}\cup P$ satisfying the sub-case-(c) constraints with
  $\tau_P<p_3$, random legal $G'$ with correctly-capped remaining cut
  budget): 3000 valid trials, zero violations of $A(F\cup G')\ge f(n)$.
- The complementary range $\tau_P\ge p_3$ is **correctly and honestly left
  open** — the file does not claim this range is closed; the "Open gaps"
  section states it precisely (same "$v<s$" obstruction as Proposition 24,
  one level down).

### Verdict rationale

No gap found in either new result; both are correctly scoped and neither
is overclaimed. The Status header (`partial`) is accurate — this closes a
real sub-branch of restricted Claim (B) but not the full lower bound (the
$\ell(F)\ge3$ splits of $p_1$, and $\tau_P\ge p_3$, remain open). This is
genuine progress ("CHANGES REQUESTED" in the routing sense — the approach
stays live, next target is $\tau_P\ge p_3$ or $\ell(F)\ge3$).

## 2. `lp-duality-certificate`

**Verdict: CHANGES REQUESTED** (Status: `partial`, correctly self-reported).

### Bisect-Top-$k$ Lemma

Claim: generalizes the certified `unconditional-p2-threshold-closure`
($k=1$) to arbitrary $k=0,\dots,n$, via a $k$-step chain of
`pair-cancellation-identity` applications plus `max-domination-lemma`.

**Verified correct, no gap found.** The chaining argument is valid: each
step of `pair-cancellation-identity` ($A(\{a,a\}\cup T)=A(T)$) requires only
$a>0$ and $T$ a finite multiset of positive reals — no ordering or
domination hypothesis between the injected pair and $T$ — so inserting the
$k$ pairs $\{p_j/2,p_j/2\}$ one at a time in any order is valid (multiset
union is commutative/associative, confirmed as a correct justification, not
hand-waving). I independently re-derived the full chain and re-verified
with a fresh 7000-trial exact-`Fraction` script (n=1..7, every k=0..n, 200
random markings per pair): zero violations of $\Phi\le(T+p_{k+1})/2$ and of
the resulting $a_nT$ threshold implication. The reported coverage of case
(b2) ($\approx10$–$26\%$) is honestly reported as partial, not a closure —
consistent with my own independent sampling logic.

### Two dead-end lemmas

Claim: two natural "peel/bisect + full induction hypothesis" mechanisms have
exact zero-slack thresholds ($p_2\ge a_nT/2$ and $p_1\ge a_nT$
respectively) that provably can never reach case (b2).

**Independently re-derived both threshold algebra chains from scratch**
(not just re-running the builder's script): solved
$p_2(1-2a_{n-1})+a_{n-1}T\le a_nT$ and $p_1(1/2-a_{n-1})+a_{n-1}T\le a_nT$
symbolically in exact `Fraction` arithmetic for $n=1,\dots,14$, confirming
$$\frac{a_n-a_{n-1}}{1-2a_{n-1}}=\frac{a_n}{2}\qquad\text{and}\qquad
\frac{a_n-a_{n-1}}{1/2-a_{n-1}}=a_n$$
exactly (not approximately) in every case tested — matching the claimed
zero-slack thresholds precisely. Given these exact thresholds, the
disjointness-from-case-(b2) conclusions follow immediately and correctly
from the definitions of case (a) and the $p_1\ge T/2$ region (both already
established/closed elsewhere in the project). **Both dead-ends are correct,
rigorous negative results** (proved algebraically, not merely refuted by a
numeric counterexample) — legitimate to certify so no future round wastes
effort "improving" either exact mechanism into case (b2).

### Vertex-restricted case-(b2) probe

Correctly and honestly reported as an incomplete, non-rigorous numeric
diagnostic (Nelder-Mead local search, not exhaustive, biased conservatively
toward *overestimating* $\Phi_{\min}$) — weak evidence of slack, explicitly
not promoted to a proof step. No overclaim.

### Verdict rationale

No gap found in either the Bisect-Top-$k$ Lemma or the two dead-end
derivations. Case (b2) itself remains genuinely open — neither lemma closes
it, and the file's own text does not claim otherwise. Status `partial` is
correct.

## Certified lemmas (new this round)

- `results/imo-2026-03/lemmas/symmetry-lemma-29a.md` — certified.
- `results/imo-2026-03/lemmas/half-dominance-split-bound.md` (Theorem 29 +
  ladder corollary) — certified.
- `results/imo-2026-03/lemmas/proposition-29b-partial-closure.md` —
  certified with its partial scope ($\tau_P<p_3$ only) explicitly preserved.
- `results/imo-2026-03/lemmas/bisect-top-k-lemma.md` — certified.
- `results/imo-2026-03/lemmas/peel-and-bisect-ih-dead-ends.md` (both
  negative lemmas) — certified as dead-end records.

## `current.md`

Updated with a new Round 14 entry summarizing both slugs' verified results,
and the reviewer's independent re-verification methodology. `## Status`
remains `partial` (the whole problem is not solved — general $n$ lower
bound and general upper bound both remain open); `## Full proof` remains
absent, as required.

## Outcomes recorded

- `greedy-halving-adversary`: `advanced` — "Theorem 29 (Half-Dominance
  Split Bound) + Symmetry Lemma 29a verified correct, no gap: fully closes
  p2-Pinned-Dominance Lemma (all of (dagger)'s p2-cut complement),
  superseding Prop 28; Prop 29b widens the ell(F)=2,P!=empty closure to
  tau_P<p3 but tau_P>=p3 honestly remains open."
- `lp-duality-certificate`: `partial` — "Bisect-Top-k Lemma (verified,
  generalizes k=1 case, covers only ~10-26% of case (b2)) and two dead-end
  lemmas (algebraically re-derived and confirmed exact zero-slack
  thresholds a_n/2 and a_n) both correct; case (b2) itself remains open,
  vertex-restricted probe stayed non-rigorous/incomplete."

## Scripts used (independent, not the builders' own)

- `/tmp/round-14/verify_thm29.py` — Lemma 29a + Theorem 29, 20,000+20,000
  trials, zero violations; counterexample-scope cross-check.
- `/tmp/round-14/verify_prop29b.py` — pair-invisibility generalization +
  sharp-dominant-removal-identity, 20,000+20,000 trials, zero violations.
- `/tmp/round-14/verify_e2e.py` — full end-to-end ladder simulation of
  Proposition 29b's conclusion at n=5, zero violations.
- `/tmp/round-14/verify_bisecttopk.py` — Bisect-Top-k Lemma, 7000 trials,
  zero violations.
- `/tmp/round-14/verify_deadends.py`, `/tmp/round-14/verify_deadend2.py` —
  exact symbolic re-derivation of both dead-end zero-slack thresholds,
  n=1..14, exact match in every case.
