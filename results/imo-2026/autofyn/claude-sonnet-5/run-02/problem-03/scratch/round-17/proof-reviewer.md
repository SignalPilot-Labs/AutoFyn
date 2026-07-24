# Round 17 Proof Review — imo-2026-03

Reviewed independently and adversarially. Both builds verified with fresh,
independently-written exact-`Fraction` Python scripts (not the builders'
own), following the project's established house rules.

## Slug 1: greedy-halving-adversary — Proposition 32 / Theorem 32

**Verdict: CHANGES REQUESTED**
**True Status: partial** (matches builder's self-reported Status)

### What was claimed
Theorem 32: for the $n$-ladder, $F=\{v_1,v_2\}\cup P$ with $\ell(F)=2$,
$v_2<v_1<p_2$ (sub-case (b)), $v_1\le s$ (where $s=\mathrm{Total}(\{p_3,
\dots,p_{n+1}\})$), and $G'=\{p_2\}\cup R'$ with $R'$ any legal refinement
of the tail below $p_2$ (any cut budget), $A(F\cup G')\ge f(n)$
unconditionally, no induction hypothesis. The complementary range
$v_1\in(s,p_2)$ is left open, diagnosed as reducing to the standing
round-15/16 crux (an upper bound on $A(R'_{>v})$).

### Verification performed
1. **Re-derived Step 1's algebraic substitution from scratch.** Starting
   from Lemma 25 ($A(F\cup G)=A(G)+A(F_1\cup G)-A(F_2\cup G)$) and
   Proposition 30's exact identity ($A(F_i\cup G')=p_2-v_i+A(R')-2A(R'_{>v_i})
   +2v_i\epsilon(v_i)$) substituted at $v_1,v_2$, I independently expanded
   and simplified by hand, using the certified `upper-truncation-identity`
   to convert $A(R'_{>v_i})-v_i\epsilon(v_i)$ into the integral $I_2$ (or
   $I_1+I_2$ depending on whether $v\le s$). This reproduces the claimed
   formula $A(F\cup G')=p_2-A(R')-(v_1-v_2)+2\int_{v_2}^{v_1}u_{R'}$
   **exactly**, and — importantly — I confirmed this formula holds
   generally, for both $v_1\le s$ and $v_1>s$ (the file's own "derivation
   detail" parenthetical correctly handles both cases with the interval-
   capping convention).
2. **Re-derived the Two-Threshold Floor lemma.** Trivial 4-line elementary
   fact; confirmed the hypothesis $v_1\le T$ is genuinely load-bearing
   (the bound $I_2\le T-v_1$ is literally false, not just non-tight, once
   $v_1>T$, since $I_2\ge0>T-v_1$ in that regime).
3. **Fresh numeric verification of the final conclusion.** Two independently
   written scripts (`/tmp/verify_thm32_legal2.py` and a variant), enforcing
   full game legality (mass conservation $v_1+v_2+\mathrm{Total}(P)=p_1$,
   correct cut-budget coupling between $F$'s own cuts and $R'$'s remaining
   budget, and per-piece boundary respect for the tail refinement):
   8596 trials, $n=3,\dots,7$, $v_1$ enforced $\le s$: **zero violations**,
   minimum margin found $\approx1.1\times10^{-3}\times f(n)$. A second,
   deliberately unconstrained variant (no mass conservation on $F$, no
   cut-budget cap on $R'$) also found zero violations once the correct
   target constant was used (see the process note below). A third script
   probing the **open** range $v_1\in(s,p_2)$ (8596 trials, full legality
   enforced) also found zero violations — consistent with, though not a
   proof of, the file's own honest claim that this range is not yet closed.

### A significant process detour (worth recording)
My first independent check used $f(n):=p_1=c(n)=2^n/(2^{n+1}-1)$ as the
target for $A(F\cup G')$ and found **every single trial** (tens of
thousands) violating the claimed bound, often by a huge margin
($\approx0.47\times$ the claimed target). This looked like a fatal,
systemic bug. Tracing it down: the correct target for $A(\cdot)$ of the
**entire** final multiset (total mass $1$) is $f(n)=2c(n)-1$, not $c(n)$
itself, because $\Phi=(\mathrm{Total}+A)/2$ and $\mathrm{Total}=1$, so
$\Phi\ge c(n)\iff A\ge 2c(n)-1$. Algebraically $2c(n)-1=2\cdot2^n/D-1=
(2^{n+1}-D)/D=1/D$ (with $D=2^{n+1}-1$) — which is **exactly** the
"$f(n)=1/(2^{n+1}-1)$" convention used throughout Lemma 12, Lemma 24, and
every downstream proposition in this file. Once I corrected my own script
to use this (the file's own, internally consistent) target, all violations
disappeared. **This is a reviewer-process finding, not a builder error**:
the file's $f(n)$ convention is correct and consistent throughout; my
first-draft script conflated $A$'s target with $\Phi$'s target. Recording
this so future reviewer passes on this file don't repeat the detour.

### Assessment
- The load-bearing hypothesis $v_1\le T$ (equivalently $v_1\le s$ in the
  application) is genuinely necessary, not decorative — confirmed both
  algebraically (the elementary bound is literally false without it) and
  by the file's own reported counterexample when mass conservation is
  additionally dropped.
- The diagnosis that $v_1>s$ reduces to the standing round-15/16 crux (an
  upper bound on $A(R'_{>v})$, equivalently on $A(F_2\cup G')$) is
  algebraically well-motivated from my own independent re-derivation of
  Step 1 — the missing ingredient really is a **lower** bound on the
  middle-band integral $I_1$, which the elementary one-sided bounds used
  in Step 2 structurally cannot supply once $v_1>s$. This is not a new
  unproven claim dressed as a diagnosis; it is a genuine reduction, traced
  through the same algebra as everything else in the theorem, honestly
  reported as unresolved.
- No overclaim found. The Status header (`partial`) and Open Gaps section
  accurately reflect what is and is not closed.

**Gap remaining for the next round:** the range $v_1\in(s,p_2)$ of
sub-case (b), and Target B ($\ell(F)=2$, $P\ne\varnothing$, $\tau_P\ge
p_3$) — both reduce to the same still-open fact: an upper bound on
$A(R'_{>v})$ (equivalently on $A(F_2\cup G')$) for $R'$ a legal
$(n-2)$-ladder response.

---

## Slug 2: lp-duality-certificate — Convex-Combination Futility Theorem

**Verdict: CHANGES REQUESTED**
**True Status: partial** (matches builder's self-reported Status)

### What was claimed
For any fixed finite family of explicit, legal Xiang-Yu strategy values
$\Phi_1(p),\dots,\Phi_k(p)$ and any weights $\lambda_i\ge0$ summing to $1$
(fixed or adaptively chosen, however derived), $\sum_i\lambda_i\Phi_i(p)
\le\theta(p)\iff\min_i\Phi_i(p)\le\theta(p)$. Consequence: no weighted
combination of a fixed finite family of already-exhibited primal
strategies can ever certify a marking beyond what the plain pointwise
minimum of that family already certifies — this forecloses the entire
"weighted-combination certificate" mechanism for case (b2)'s upper bound.

### Verification performed
Independently re-derived the proof from scratch (it is genuinely
elementary): the "$\Rightarrow$" direction is the trivial degenerate-weight
case (put all mass on the minimizer). The substantive "$\Leftarrow$"
direction is a one-line contrapositive: if every $\Phi_i(p)>\theta(p)$,
then for any nonnegative weights summing to $1$ (so at least one weight is
strictly positive), $\sum_i\lambda_i(\Phi_i(p)-\theta(p))>0$ term-by-term
(nonnegative $\times$ nonneg, strictly positive at the index with positive
weight), hence $\sum_i\lambda_i\Phi_i(p)>\theta(p)$. This is a standard,
correct fact about convex combinations (a convex combination of numbers is
never below their minimum) — I confirmed no hidden case is skipped: the
argument works for any $k\ge1$, any real-valued $\Phi_i(p)$, any weight
vector on the simplex, with no continuity/measurability assumption needed
since it's a finite sum.

### Assessment
- **Not vacuous.** It is a genuine, useful negative result: it rules out
  an entire class of future attempts (any convex-combination-of-exhibited-
  primal-values scheme, not just the one $(\Phi_A,\Phi_B)$ pair the
  builder numerically tested with an LP grid search over $\lambda\in[0,1]$
  at $n=3$, which — consistent with the theorem — found no $\lambda$
  beating the pointwise minimum, margin $\approx-0.033$ at best).
- **Correctly scoped.** The file's "Honest conclusion" (R17.3) explicitly
  states case (b2) remains open and does not claim any new marking is
  certified — the theorem is presented, correctly, as foreclosing a
  mechanism, not as progress toward the upper bound itself.
- **Structural diagnosis is sound.** The accompanying explanation — that
  $\Phi_{\min}$ is defined as a minimum over legal responses, so an upper
  bound on it is witnessed by one strategy, not averaged over several, and
  that genuine LP-duality weighting is naturally suited to *lower* bounds
  (Claim (B)) rather than upper bounds on a min — is mathematically
  correct and a useful redirection for the approach.
- No overclaim found; the certified lemma file matches the proof exactly,
  with an appropriately broad "Scope" note (applies to any finite family,
  any weighting rule, not just the tested pair).

**Net effect:** genuine negative progress (narrows the search space for
future rounds on this slug), but case (b2)'s upper bound itself is not
advanced this round — no new marking certified.

---

## Lemma certification

Both new lemma files are held to the full bar (no `sorry`, statement
matches what was proved, no overclaim) and are **admitted as certified**
(they were already correctly written to `results/imo-2026-03/lemmas/` by
the builders; no changes needed):

- `lemmas/two-threshold-truncated-alternating-sum-floor.md` — **certified**,
  independently re-derived and re-verified (see above). Scope note in the
  file (does not by itself close sub-case (b) in general, only $v_1\le s$)
  is accurate and retained.
- `lemmas/convex-combination-futility-theorem.md` — **certified**,
  independently re-derived and re-verified (see above). Correctly labeled
  a negative/dead-end result for the mechanism it forecloses, not a
  positive closure.

## current.md

Updated `results/imo-2026-03/current.md`: appended a Round 17 entry to the
"Approaches tried" narrative (Status remains `partial`, unchanged — neither
build's top-level target closed). No change to the `## Status` field
(still `partial`) or the (absent) `## Full proof` section, since neither
slug reached `solved`.

## Outcomes recorded

- `greedy-halving-adversary`: `advanced` — Theorem 32 closes a genuinely
  large, precisely-scoped sub-range of $\ell(F)=2$ sub-case (b)
  unconditionally; the residual range is honestly diagnosed as the
  standing crux, not a new gap.
- `lp-duality-certificate`: `dead-end` — the Convex-Combination Futility
  Theorem correctly and permanently forecloses the weighted-combination
  mechanism this slug had been probing; genuine, verified negative result,
  but adds zero new coverage of case (b2) this round.

## Files referenced
- `/home/agentuser/repo/results/imo-2026-03/approaches/greedy-halving-adversary.md` (Proposition 32 / Theorem 32, lines ~3294–3438; Open gaps ~3554–3583)
- `/home/agentuser/repo/results/imo-2026-03/lemmas/two-threshold-truncated-alternating-sum-floor.md`
- `/home/agentuser/repo/results/imo-2026-03/approaches/lp-duality-certificate.md` (R17.1–R17.3, lines ~3258–3428)
- `/home/agentuser/repo/results/imo-2026-03/lemmas/convex-combination-futility-theorem.md`
- `/home/agentuser/repo/results/imo-2026-03/current.md` (updated)
- Independent verification scripts written this round: `/tmp/verify_thm32.py`, `/tmp/verify_thm32_massconserv.py`, `/tmp/verify_thm32_legal.py`, `/tmp/verify_thm32_legal2.py`
