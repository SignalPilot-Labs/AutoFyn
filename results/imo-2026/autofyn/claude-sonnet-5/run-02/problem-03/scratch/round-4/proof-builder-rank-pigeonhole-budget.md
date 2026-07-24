# Proof-builder report — slug `rank-pigeonhole-budget`, round 4

## What I did

Read `current.md`, the seeded outline in
`approaches/rank-pigeonhole-budget.md`, `knowledge_base.md`, and the
certified lemmas `vertex-minimum-theorem`, `odd-run-reduction-lemma`,
`cross-term-identity-threshold`, `dominant-element-removal-identity`,
`claiming-subgame-reduction`, `ladder-self-similarity-constant`, plus the
`aimo-0718` crux entries. Rather than executing the outline's literal
Steps 1–5 (cut-count-vector discretization + a direct `aimo-0718`
transplant), I found a sharper algebraic route into the same located gap
(Proposition 10's "Missing Inequality" in `greedy-halving-adversary.md`)
and pursued that instead, reporting explicitly where the literal
pigeonhole transplant fails (as the outline's "watch out for" section
asked).

## What's proved (new, this round)

1. **New general lemma** (`lemmas/sharp-dominant-removal-identity.md`,
   proposed for certification): for any multiset $T$ and $f_1>\max(T)$,
   $A(\{f_1\}\cup T)=f_1-A(T)$. Strictly generalizes the certified
   `dominant-element-removal-identity` (weaker hypothesis: $\max(T)$, not
   $\mathrm{Total}(T)$). Proved from scratch via the integral formula;
   verified by 20000 exact-`Fraction` trials, zero mismatches, including an
   explicit witness that the weaker hypothesis is genuinely needed.
2. Applying this lemma to Case A ($f_1>r$) of Proposition 10 collapses the
   entire cross-term analysis to one line: $A(F\cup G')=f_1-A(F'\cup G')$,
   with no unevaluated integral left over. This makes the "Missing
   Inequality" *equivalent* to a single clean statement
   $(\star)$: $A(F'\cup G')\le f_1-a_n$ — much simpler than Proposition
   10's original three-term cross-term formulation.
3. $(\star)$ verified numerically: 50000 random trials per $n=2,\dots,5$
   (correct combinatorial model — tail is the fixed ladder pieces, only
   ever subdivided, never freely reshaped), zero violations, strictly
   positive slack throughout.

## Honest negative finding

Attempted to reduce $(\star)$ to a pure discrete pigeonhole/majorization
statement (the outline's intended mechanism, "even-sorted-rank sum of the
merged multiset dominates one side's total") and found this **false** as
a generic multiset fact: counterexample $F'=\{10\}$,
$G'=\{1^{\times11}\}$, even-rank sum $=6<10=\mathrm{Total}(F')$. So the
`aimo-0718`-style transplant does not go through mechanically — the real
inequality must exploit that $G'$ refines the specific superincreasing
ladder tail, not an arbitrary multiset. This is reported explicitly in the
approach file rather than forced or hidden.

## What remains open

- $(\star)$ itself (Case A) — numerically bulletproof, not proved.
- Case B ($f_1\le r$): shown (numerically) to have its hard case exactly
  at $c=n$, which is the *same* obstruction already flagged and left open
  by round 3's `self-similar-bracketing` (Proposition B2) — not a new gap.
- General upper bound — untouched, not this slug's target.

## Status set to `partial`

(not `unsolved`, since a genuine new certified-quality lemma and a real
simplifying reduction were established; not `solved`, since the core
inequality is not proved for general $n$.)
