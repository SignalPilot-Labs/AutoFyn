# Round 7 proof-reviewer report — imo-2026-03

Reviewed three built slugs: `rank-tie-vertex-reduction`,
`lp-duality-certificate`, `rank-pigeonhole-budget`. All new claims were
independently re-derived by hand and/or re-verified with freshly-written
exact-`fractions.Fraction` scripts (never the builders' own scripts), per
the assignment. Scripts used: `/tmp/verify_round7_vertex.py`,
`/tmp/verify_round7_bound.py`, `/tmp/verify_lp.py`,
`/tmp/verify_pigeonhole.py`, `/tmp/verify_starstar.py`.

## 1. `rank-tie-vertex-reduction` — verdict: CHANGES REQUESTED

**Claims checked:**
- **Peel Decomposition Identity** ($A(\{z\}\cup G')=z+A(G')-2\int_0^{\min(z,r')}v$):
  a direct instantiation of the already-certified
  `cross-term-identity-threshold` at $F=\{z\}$ (singleton). Re-derived by
  hand: $u(t)=\mathbb1[t<z]$ for a singleton, $A(\{z\})=z$, and
  $\int_0^r uv=\int_0^{\min(z,r)}v$ since the integrand vanishes for
  $t\ge z$. No gap. **Correct.**
- **Case-II Exact Peel Identity** ($A(S)=z-A(G')$ when $z\ge p_2$): proof
  re-derived step by step (Lemma 1's "at most one fragment $\ge p_2$" case
  split; Steps 1–4 splitting the window integral at $p_2$ using the
  already-certified Half-Window Vanishing fact that no tail/foreign
  element exceeds $p_2$). Independently re-verified numerically with a
  freshly-written script: **10,138 random legal trials** (dominant-fragment
  regime, $n=2,\dots,7$, $c_1\in\{2,\dots,n\}$), **zero mismatches**. A
  control of 9,862 trials outside the hypothesis ($z<p_2$) found the
  identity fails in $\approx86\%$ of them (builder reported $\approx94.5\%$
  in their own control; different random distributions, same qualitative
  conclusion — $z\ge p_2$ is a genuine, non-technical boundary). Also
  independently verified $A(S)\ge f(n)$ held in every dominant-fragment
  trial (20,000-trial separate script), min slack found exactly $0$
  (consistent with an exact equality case). **Correct.**
- **Honest-gap claim** (the identity is exact, so "$A(S)\ge f(n)$" and
  "$A(G')\le z-f(n)$" are logically equivalent, not a genuine reduction):
  verified algebraically — checked by hand that the trivial universal
  bound $A(G')\le\mathrm{Total}(G')=w+r$ is indeed too weak (needs $w\le0$
  to match $z-f(n)=r-w$). This is an honest, correctly-argued non-closure,
  not hand-waved.
- **No-dominant-fragment case ($z<p_2$) genuinely outside reach:**
  confirmed by the same control run above (identity fails in the large
  majority of trials there).

**Verdict rationale.** Two new lemmas are correct and non-trivial
(certified below); the round's central claim — this does not close the
$c_1\ge2$ case, only sharpens what's missing — is honest and independently
verified rather than papered over. Status `partial` is accurate. No
overclaiming found anywhere in the file.

## 2. `lp-duality-certificate` — verdict: CHANGES REQUESTED

**Claims checked:**
- **Bounded certificate for $c_1=1$** ($(\star\star)$ as one Type-III atom
  + one exactly-zero Type-IV atom): this is algebraically identical to the
  already-certified Half-Window Vanishing Lemma's own proof, just relabeled
  into an atom vocabulary. Re-derived by hand — correct, but essentially a
  repackaging, not new mathematical content. Independently re-verified the
  underlying $(\star\star)$ with a fresh 5,000-trial script across
  $n=2,\dots,6$: **zero violations**.
- **$c_1=2$ counterexample to the mechanical extension** — independently
  recomputed from scratch (`/tmp/verify_lp.py`): $n=3$ ladder, $F=\{4,2,2\}/15$,
  $T=\{4,2,1\}/15$ untouched. Got exactly $A(F)=4$, $A(T)=3$,
  $\int_0^r uv=3$, $A(F\cup T)=1$ (all in units of $1/15$) — **matches the
  builder's numbers exactly**. The needed sufficient condition
  $\int uv\le A(F)/2=2$ fails (actual $3$), a genuine $50\%$ overage, while
  the true target $A(S)\ge f(3)\cdot D=1$ holds with equality. Confirmed
  the "floor vs. exact value" diagnosis: the inductive floor for $A(T)$ is
  $r\cdot(2a_2-1)=1$, strictly below the actual $A(T)=3$; substituting the
  floor instead of the actual value would give $4-6+1=-1<1$, genuinely
  failing. **The finding is correctly stated: this refutes the specific
  decoupled certificate strategy, not the theorem itself** — the file is
  careful about this distinction throughout and never claims otherwise.

**Verdict rationale.** No false claims found. The positive result (§6.2) is
minor (a repackaging); the negative result (§7) is a genuine, precisely
diagnosed obstruction, independently reproduced exactly. Status `partial`
is accurate.

## 3. `rank-pigeonhole-budget` — verdict: CHANGES REQUESTED

**Claims checked:**
- **$E=\mathrm{Total}-2E$ reformulation of Case I** ($A(F\cup\tau)\ge
  s-R(\tau)\iff E(F\cup\tau)\le R(\tau)$): trivial, correct bookkeeping
  identity via $A=O-E$, $\mathrm{Total}=O+E$.
- **Peel-the-global-minimum, Branch A** (all $k\le m+1$): re-derived the
  parity/rank-shift argument by hand for both the plain-induction
  sub-branch ($k\le m$) and the $k=m+1$ boundary (via the new Half-Bound
  Lemma plus the identity $R(\tau)+\tau_m=2\tau_1$, itself re-derived from
  the finite geometric sum and checked exactly). Both are unconditional,
  no gap. **Correct.**
- **Branch B, $N$ odd:** re-derived — removing the global minimum from an
  odd rank doesn't touch $E$, so the smaller-instance IH applies directly.
  **Correct.**
- **Branch B, $N$ even — the open sub-case $(\dagger)$:** correctly
  identified as NOT closed (the IH only gives $E(F'\cup\tau)\le R(\tau)$,
  not the needed $\le R(\tau)-\mu$). No overclaim.
- **Independent numeric re-verification** (fresh script,
  `/tmp/verify_pigeonhole.py`, 300,000 attempted / **113,074 legal Case-I
  trials**, $m=1,\dots,7$): **zero violations** of $E(F\cup\tau)\le R(\tau)$
  overall; tagged branch classification gives Branch A $\approx35.7\%$,
  Branch B-odd $\approx38.1\%$, Branch B-even (the open $(\dagger)$ case)
  $\approx26.2\%$ — the open sub-case is genuinely and substantially
  exercised (not a measure-zero corner), zero violations found there
  either, consistent with the builder's own $\sim\!27\%$/zero-violations
  report.
- **Splitting-monotonicity dead end:** independently recomputed the
  counterexample ($m=2$, $\tau=(14,7)$, $F=\{8.12\}\to\{3.8976,4.2224\}$):
  $E$ goes from $8.12$ to $10.8976$ — confirmed, genuine refutation.
- **"Neither sibling supplies an upper-bound tool" claim:** checked against
  the actual content of `lp-duality-certificate` and
  `rank-tie-vertex-reduction`'s round-7 sections — accurate; neither file
  in fact supplies a usable general upper bound on $A$ of a reduced
  instance.

**Verdict rationale.** This file makes the most surgically precise
progress of the round: two of three exhaustive branches of Case I are now
fully closed for every $m$, with the single remaining sub-case exactly
pinned down. No overclaiming. Status `partial` is accurate.

## Certification actions taken

Lemma files created/updated in `results/imo-2026-03/lemmas/`:
- `peel-decomposition-identity.md` — certification note added.
- `case-ii-exact-peel-identity.md` — certification note added.
- `bounded-certificate-for-half-window-vanishing.md` — new, certified.
- `half-bound-lemma.md` — new, certified.
- `peel-minimum-branch-closure.md` — new, certified as a **partial**
  result (Branch A + Branch B-odd only; $(\dagger)$ explicitly NOT
  certified as closed).
- `splitting-monotonicity-refuted-dead-end.md` — new dead-end record.
- `half-window-vanishing-lemma.md` — **backfilled**: this was declared
  certified in round 6's `current.md` narrative but no standalone lemma
  file had ever been written, despite round-7 builds (`case-ii-exact-peel-
  identity`) directly citing it as "the certified Half-Window Vanishing
  Lemma." Re-verified independently this round (fresh 5,000-trial script)
  before backfilling.
- `case-ii-closure-theorem.md` — **backfilled** for the same reason
  (Theorem GC($m$), round 6's Case-II closure of Claim (A); recommended
  for promotion in round 6 but never written as its own file).

`mcp__approach-ranker__record_outcome` called for all three slugs with
outcome `partial` and a note summarizing the independently-verified
findings.

`results/imo-2026-03/current.md` updated: new bullet under "Approaches
tried" (Round 7 summary), new paragraph in the "Full proof (absent)" lemma
inventory. **Status remains `partial`** — no slug this round reached a
complete end-to-end proof; this is correct and expected (CLAUDE.md's own
routing rules: a mixed CHANGES-REQUESTED result across all built slugs is
normal, not a failed round).

## Overall assessment

A clean, honest round: three genuinely different mechanisms (exact-identity
peeling, LP-dual certificate conversion, discrete peel-the-minimum
induction) converged independently on the same underlying obstruction —
an *exact-value* (not floor/trivial-bound) handle on a reduced tail or
foreign-mass instance — with no approach overclaiming and
`rank-pigeonhole-budget` producing the most precisely localized open item
in the project to date, $(\dagger)$ (Branch B, $N$ even, of Case I of
Claim (A)). Recommend round 8 focus explicitly on $(\dagger)$ (it is now a
single, self-contained, well-defined inequality, not an open-ended
regress) and/or on finding the "exact value vs. floor" upper-bound
ingredient that all three approaches this round identify as the shared
missing piece.
