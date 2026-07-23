# Outline review — imo-2026-05, round 1

Shared background across all four approaches (equality-forcing substitution x=f(y)
giving f(f(y))=2f(y)-y; orbit-AP argument giving f(y)>=y; injectivity) was independently
re-derived and checked here — correct. Target answer f(x)=x+c, c>=0, and its
sufficiency check (both squared inequalities reduce to the identity (x-y-c)^2>=0) was
independently re-verified with sympy — correct, matches the outliner.

## quadratic-difference-chaining — APPROVE

This is not merely "strongest," it is essentially a complete proof already, verified
independently line-by-line:

- Step 5's algebra was checked with sympy: expanding (x+y+2S(x))^2 - 4f(x)f(y) gives
  exactly (x-y)^2 + 4f(x)(S(x)-S(y)), confirming (**) and, after the x<->y swap, the
  two-sided (KEY) bound -(x-y)^2/(4f(x)) <= S(x)-S(y) <= (x-y)^2/(4f(y)). No leap here:
  it is a direct, correct substitution of X=f(x) into the already-established
  inequality (B), combined with the exact identity (*). Sound mechanism, not a bare
  label.
- Step 6's subdivision/telescoping argument is a standard, fully elementary technique
  (no continuity or differentiability assumed): |S(x)-S(y)| <= (y-x)^2/(4·min(x,y)·n)
  -> 0 as n->infinity is a correct computation from (KEY) applied to n consecutive
  subintervals, using f(t_i)>=t_i>=min(x,y) from the f(y)>=y lemma. This closes the
  "single shared gap" (global constancy of S) that all explorers flagged — genuinely,
  not just plausibly.
- Sufficiency direction independently reverified (sympy): both (A) and (B) reduce
  exactly to (x-y-c)^2>=0 for f(x)=x+c.

No unjustified leaps, no circularity, right technique (equality-case squeezing +
elementary subdivision, not an ill-fitting rigidity theorem). The only remaining work
is transcription: writing steps 5-6 out with full epsilon/n bookkeeping instead of the
outline's condensed form. Approve without reservation; this is the approach the builder
should turn into the final writeup.

## monotonicity-first — CHANGES REQUESTED (real risk of RETHINK if step 2 stalls)

The shared background is fine (cross-cited correctly). The approach's own contribution
has two open lemmas, and one of them (step 2, f strictly increasing) is stated only as
a strategy sketch ("the precise chain needs the builder to work through the algebra")
with no contradiction actually exhibited — I attempted a quick derivation myself
(comparing (A) at x1 and (B) at x2 for assumed f(x1)>=f(x2)) and did not find an
immediate contradiction; it is not obviously false, but it is not obviously true either,
unlike quadratic-difference-chaining's fully-verified (KEY). Step 5 (reverse
monotonicity) is explicitly unresolved and the outline itself concedes it may have to
fall back to importing quadratic-difference-chaining's (KEY) lemma to finish — meaning
in the worst case this approach reduces to a weaker restatement of the approved
approach, contributing no independent proof if it can't close step 2 on its own.

This is legitimate framing diversity (order-theoretic vs. quadratic-estimate), not a
wrong technique outright, so it is worth one focused builder pass — but the builder
should be told: if step 2 does not close within one attempt via a genuine contradiction
(not an assumed one), mark this RETHINK/merge rather than patch with hand-waving, per
the outline's own guidance.

## cauchy-boundedness — RETHINK

The outline's own admission is decisive: "(KEY) is quadratic not linear... may not be
the right structural fit at all," and the core step (extracting an exact/approximate
additive Cauchy relation S(y+t)-S(y)=phi(t) independent of y) is not derived, only
gestured at, with the fallback plan being "reinterpret (KEY) in the h->0 limit" which
the outline itself flags requires an unjustified differentiability assumption to be
rigorous (explicitly called out under "Watch out for" as illustrative only, not valid).
There is no sound mechanism offered for extracting genuine additivity from a bound that
is intrinsically quadratic in (x-y), not linear — Cauchy rigidity is the wrong tool for
a quadratic-order estimate. Given the KEY bound is quadratic, forcing it into a Cauchy/
additive framework is trying to fit the wrong theorem to the estimate at hand: dead-end
by mismatch of technique, not a fixable gap. Cut; do not spend a builder round on it
while quadratic-difference-chaining already fully resolves the same gap with the
correct-order tool.

## extremal-supinf — RETHINK

The sup/inf extremal-principle framing is a real technique in general, but as applied
here it degenerates into exactly quadratic-difference-chaining's subdivision argument:
shrinking I_k=[x-1/k,x+1/k] to force (x_n-y_n)^2->0 in (KEY) is the same "shrink the
gap, use the quadratic bound" idea as the direct n-fold subdivision, just phrased with
extra sup/inf/sequence machinery that adds proof burden (inf may not be attained, needs
sequences, needs a second global-comparison step after establishing local constancy)
without adding power or diversity of *mechanism* — the outline itself twice concedes
"likely to converge to a more complicated restatement" and "if it does not simplify...
prefer marking this approach RETHINK." I agree: this does not open a genuinely
different route to the gap, it re-derives the same closed gap through more steps. Not
worth builder time this round.

## Diversity assessment

All four approaches share the same correct background chain and the same ultimate gap
(global constancy of S), which is fine at round 1 (this is not yet a multi-round
plateau). Of the two candidate "different mechanisms," monotonicity-first is a
genuinely distinct order-theoretic route (worth trying once), while cauchy-boundedness
and extremal-supinf are not real diversity — one reaches for a mismatched rigidity
theorem, the other re-derives the same subdivision idea with extra scaffolding. True
diversity of thought here would need a fifth angle attacking the problem from an
entirely different framing (e.g., a monovariant/potential-function argument not
via S at all, or working with 1/f or reciprocal-type substitutions) rather than more
variations on "bound the pairwise difference of S and force it to zero" — flag for next
round's outliner only if quadratic-difference-chaining's writeup somehow fails
verification; otherwise no plateau exists yet since the leading approach is essentially
solved.

## Ranking

Registered: quadratic-difference-chaining, monotonicity-first (both new, entering at
cold-start Elo 1500). cauchy-boundedness and extremal-supinf are RETHINK/cut and were
NOT registered — kept out of the population per the gate rule.
update_ranking: quadratic-difference-chaining beats monotonicity-first (1516 vs 1484) —
anchored on the independently-verified completeness of the former vs. the two open,
unresolved lemmas (one with no demonstrated contradiction) of the latter.

build set: quadratic-difference-chaining, monotonicity-first
