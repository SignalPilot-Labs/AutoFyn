# Proof review — imo-2026-05, round 1

## Problem

Determine all $f:\mathbb R_{>0}\to\mathbb R_{>0}$ with, for all $x,y>0$,
$$\sqrt{\tfrac{x^2+f(y)^2}{2}} \ge \tfrac{f(x)+y}{2} \ge \sqrt{xf(y)}.$$
`task = compute_and_prove`, `answer_type = characterization`: solved requires both a
proven necessity bound (every solution has form ...) AND explicit sufficiency
verification of every claimed member.

## Method of review

For each proof I independently re-derived the load-bearing algebraic identities with
sympy (not just re-read the write-up):
1. Equality-forcing substitution $x=f(y)$ collapsing (A),(B) to $f(f(y))=2f(y)-y$.
2. The KEY-bound expansion identity
   $(x+y+2S_x)^2-4(x+S_x)(y+S_y) = (x-y)^2+4(x+S_x)(S_x-S_y)$.
3. Sufficiency: $2x^2+2(y+c)^2-(x+y+c)^2 = (x-y-c)^2$ and $(x+y+c)^2-4x(y+c)=(x-y-c)^2$.

All three checked out exactly (sympy `simplify(lhs-rhs)==0` for each). I then manually
traced the orbit/AP argument (Step 2), the subdivision/telescoping argument (Step 5/7),
and the case analysis ($x<y$/$x=y$/$x>y$ symmetry, general real ratios not just
rational/dense special cases), and the "name your theorems" citations against
`knowledge_base.md` lines 33–35 ("Standard inequalities: equality cases pin down the
extremal configuration"; "Functional equations: test special values, check
injectivity/surjectivity").

## Verdict 1: `quadratic-difference-chaining` — APPROVE (Status: solved)

**Correctness.** Every step checked and holds:
- Step 0 (squaring the sandwich) is valid since all quantities are positive, $t\mapsto
  t^2$ increasing on $[0,\infty)$.
- Step 1 (equality-forcing substitution $x=f(y)$) correctly derives
  $f(f(y))=2f(y)-y$ by combining (A') and (B') into an equality of squares of positive
  quantities, then taking nonnegative square roots. Verified.
- Step 2 (orbit is an exact AP, $f(y)\ge y$) is a correct and complete argument:
  positivity of every iterate $y_n>0$ (by induction, using $f$'s codomain) rules out
  negative common difference $d=f(y)-y$ (else $y_n\to-\infty$). No gap.
- Step 3 (injectivity) is correctly derived and explicitly flagged as unused — honest
  bookkeeping, not padding.
- Step 4 (KEY bound). The substitution of $X=f(x)$ into (B) and the resulting
  expansion is algebraically correct — I independently reproduced the exact identity
  $(x+y+2S(x))^2-4(x+S(x))(y+S(y)) = (x-y)^2+4f(x)(S(x)-S(y))$ with sympy, it matches
  term for term. The companion (swapped) bound is likewise correct (structurally
  identical derivation with $x,y$ interchanged — genuinely symmetric, not a hidden gap).
- Step 5 (subdivision forces global constancy). This is the step I scrutinized hardest
  per the dispatch brief. The argument: subdivide $[\min(x,y),\max(x,y)]$ into $n$
  **equal real-valued** steps $t_i = x+i(y-x)/n$ for *arbitrary* $n\in\mathbb N$ — this
  works for every $x,y>0$ (including irrational ratios; nothing in the construction
  requires $y/x$ rational), not merely a dense set or a special sequence. Each $t_i\ge
  m:=\min(x,y)>0$, so $f(t_i)\ge t_i\ge m$ by Step 2, uniformly bounding every
  denominator in (KEY) from below by $m$. The pairwise bound
  $|S(t_i)-S(t_{i+1})|\le \Delta^2/(4m)$ is then correctly telescoped via the triangle
  inequality to $|S(x)-S(y)|\le (y-x)^2/(4mn)\to0$. Since the left side is independent
  of $n$, $S(x)=S(y)$ for *every* pair $x,y>0$ — this is genuinely global constancy,
  not constancy restricted to a subset. The $x=y$ case is trivial and $x>y$ is handled
  by a real (not hand-waved) symmetry: (KEY) itself is symmetric under $x\leftrightarrow
  y$ relabeling, so the same argument runs verbatim. No gap here.
- Step 6/7 (necessity conclusion, sufficiency). Sufficiency is checked by direct
  algebraic computation reducing both (A) and (B) to the single perfect square
  $(x-y-c)^2\ge0$; I re-verified this with sympy and it is exact. The codomain
  constraint $c\ge0$ is correctly derived both from necessity (Step 2) and
  independently re-justified in the sufficiency direction (if $c<0$, $f$ would map some
  $x\in(0,-c]$ to a nonpositive value, violating the codomain) — this is the correct
  and complete boundary check for "$c\ge0$" rather than "$c\in\mathbb R$".

**Rigor rule compliance.** No skipped cases; no "clearly/obviously" hiding a step (every
non-trivial claim is expanded); both bound (necessity) and construction (sufficiency)
present, matching the "find all $f$" requirement. Minor stylistic note: the file
narrates the "equality case pins the extremal configuration" mechanism in prose but
does not explicitly write "(knowledge_base.md, Standard inequalities)" the way the
sibling file does — this is a citation-formatting nitpick, not a mathematical gap
(the step is fully proved from scratch regardless); I added the explicit citation when
copying this proof into `current.md`.

**Verdict:** solved, no gap found. **APPROVE.**

## Verdict 2: `monotonicity-first` — APPROVE (Status: solved)

Shares the identical core mechanism with the sibling (equality-forcing substitution,
orbit-AP argument, KEY bound, subdivision/telescoping) — I re-verified the same three
algebraic identities independently for this file's version of the derivation (its
KEY-bound expansion path differs slightly in intermediate bookkeeping — "cancel
$4yS(x)$ from both sides" vs. the sibling's factor-then-subtract order — but both reduce
to the same sympy-checked identity). All steps hold for the same reasons as above; the
subdivision argument (Step 7) is the same fully general, arbitrary-real-ratio,
$x=y$/$x>y$/$x<y$-complete argument.

**Extra content, genuinely checked.** This file also contains a real negative/structural
result not present in the sibling: an attempt to prove $f$ strictly increasing *before*
reaching the KEY bound, with three sub-attempts each shown insufficient by an explicit
counterexample or algebraic tautology, rather than by "we couldn't find it":
- Attempt A (cross-substitution of (B) alone at $(x_2,x_1)$ and $(x_1,x_2)$): the
  witness $x_1=1,x_2=2,a=10,b=9$ satisfies both derived inequalities (I),(II) while
  $a>b$, $x_1<x_2$ — I recomputed this by hand: (I) $10^2=100\ge4\cdot2\cdot10=80$
  ✓, (II) $12^2=144\ge4\cdot1\cdot9=36$ ✓, both hold — confirms the sub-attempt is
  genuinely insufficient as claimed.
- Attempt B (same-pair mixing of (A),(B)): correctly reduces to the tautology
  $2(x-f(y))^2\ge0$, a routine algebraic check (subtracting (B) from (A) at the same
  pair does trivially give $2x^2+2f(y)^2-4xf(y)=2(x-f(y))^2$) — this is correctly
  identified as carrying zero cross-variable information.
- Attempt C (orbit-disjointness combinatorics): the explicit numeric witness
  ($p_n=1+n/3$, $q_m=1.05+m/2$, disjoint since $2n-3m=0.3\notin\mathbb Z$) correctly
  demonstrates two APs with different common differences can be disjoint, so
  disjointness alone can't force $S(x_1)=S(x_2)$ — correct and honest.

This negative result is honestly scoped ("this quadruple need not itself extend to an
actual solution $f$ — it only shows the inequalities alone don't encode enough
information") and does not overclaim; it correctly motivates falling back on the KEY
bound, which is then fully and correctly re-derived.

**Rigor rule compliance.** Same as sibling: no skipped cases, theorems cited (explicitly,
"(KB: ...)" inline, better citation discipline than the sibling), necessity + sufficiency
both present and verified.

**Verdict:** solved, no gap found. **APPROVE.**

## Overall

Both approaches independently arrive at a complete, correct, rigorous proof of
$f(x)=x+c$, $c\ge0$, verified via: (a) independent sympy re-derivation of every
load-bearing algebraic identity (equality-forcing identity, KEY-bound expansion,
both sufficiency reductions — all confirmed exact), (b) a careful trace of the
subdivision/telescoping argument confirming it forces *global* constancy of $S$ on all
of $\mathbb R_{>0}$ (arbitrary real $x,y>0$, not a dense subset or special sequence),
(c) confirmation that injectivity, while derived, is correctly flagged as unused so no
circular dependency exists, and (d) confirmation that sufficiency is checked for the
full family with the boundary case $c\ge0$ correctly justified from both directions.

`results/imo-2026-05/current.md` has been created (reviewer-owned; did not exist
before this round) with `## Status: solved` and the `quadratic-difference-chaining`
proof (cleaner citation formatting) copied into `## Full proof`, with `## Approaches
tried` crediting both slugs' independent verification and `monotonicity-first`'s extra
negative-result content.

Certified 4 promotable lemmas into `results/imo-2026-05/lemmas/`:
- `equality-forcing-identity.md`
- `orbit-forces-f-ge-id.md`
- `key-quadratic-bound-and-constancy.md`
- `S-constant-along-orbit.md` (the genuinely new lemma from `monotonicity-first`)

Ranker outcomes recorded: both slugs `verified-milestone` for round 1.

## Verdicts summary

- `quadratic-difference-chaining` — **APPROVE** — Status: solved
- `monotonicity-first` — **APPROVE** — Status: solved

The run's goal (a complete rigorous solution to imo-2026-05) is met.
