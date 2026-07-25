## imo-2026-03 (lens: general-k Cardinality-Constrained Half-Sum Lemma)

### Statement being scouted
GCH(k): for R a finite multiset with max(R) ≤ 2^{k-1} =: cap, |R| ≤ k+1,
sum(R) = S ∈ [2^k, 2^k+1), and Γ_{k-1} = {2^{k-1},...,2,1} (k elements):
OddSum(R ∪ Γ_{k-1}) ≥ (S+2^k)/2, equivalently AltSum(R ∪ Γ_{k-1}) ≥ 1.
Round 18 proved k=2 in full and left general k as a numerically-checked
(k=2..6) conjecture, diagnosing that plain induction-on-k fails because
one peel keeps cap=2^{k-1} fixed while the Γ-index drops (a smaller
instance of the *same* excess-1 phenomenon, not a smaller instance of
GCH itself).

### What I verified this round (new, beyond round 18)
Round 18's numeric check used unconstrained/lightly-restarted continuous
optimizers (SLSQP with 25-80 restarts), which I confirmed by direct
reproduction **gets stuck in bad local optima for this objective** — the
objective (OddSum after sorting) is piecewise-linear/non-smooth, so
gradient-based restarts routinely report a minimum that is NOT the true
global minimum (e.g. at k=2, S=4.5, SLSQP reported min=4.5 with x=[2,2,0.5],
margin 0.25 above target, when the true minimum is 4.25, exactly at
target). This means round 18's "verified to ~1e-12" claim, while not
wrong in its own restricted samples, is evidence from an optimizer that
can silently overstate the margin (never *understate* it dangerously
here, since it can only report values ≥ true min, so it cannot have
manufactured a false violation, but it also cannot certify tightness
reliably).

I replaced this with an **exact combinatorial LP method** (not gradient
descent): for fixed n=|R| and a fixed interleaving pattern of R's sorted
values against Γ_{k-1}'s (fixed) sorted values, OddSum is an exact linear
functional of x, and the interleaving-consistency constraints are linear;
so `scipy.optimize.linprog` (`method='highs'`) finds the *exact* global
optimum on each interleaving region, and taking the min over all
`C(n+k, n)` interleavings gives the *true* global minimum for that
(k,n,S) — no local-optimum risk. Ran this for k=2,3,4,5 (all n from 2 to
k+1) across several S = 2^k+ρ, ρ ∈ {0.0001, 0.3, 0.7, 0.999}, and for
k=6 at n up to 5 (partial, combinatorics grows fast).

**Result: the conjectured bound (S+2^k)/2 is matched EXACTLY (margin 0
to LP/machine precision, not ~1e-12 approximately) at every tested point
for k=2,3,4,5** — i.e. the Lemma is not just true but **tight everywhere
along the whole range S∈[2^k,2^k+1)**, not only at isolated symmetric
points. This is much stronger and more reliable evidence than round 18's
(exact LP global optimum vs. restart-heuristic local optimum), and it
also exposes the **exact extremal configuration**, which round 18 never
identified explicitly:

**Extremal structure (new finding).** The true minimizer of
OddSum(R∪Γ_{k-1}) subject to sum(R)=S=2^k+ρ, max(R)≤2^{k-1}, is
- for k≥3: R* = {2^{k-1}, 2^{k-2}, ..., 4} ∪ {r,r}, where the "chain"
  runs down from cap=2^{k-1} to 4 (i.e. exponents k-1,...,2; that's k-2
  elements), and r = (ρ+4)/2 (so 2r = ρ+4 = S − (2^k−4), using the
  telescoping chain-sum identity 2^{k-1}+2^{k-2}+···+4 = 2^k−4). Total
  |R*| = k (NOT k+1 — the cardinality cap has slack 1 at the true
  extremal witness).
- for k=2: R* = {2, r, r} with r=(2+ρ)/2 (the chain degenerates to just
  {cap} since cap=2<4); this matches the already-certified k=2 proof's
  named equality locus exactly.

I explicitly confirmed (LP, k=3,4,5) that optimizing over n=k+1 gives
the *same* value as n=k (up to a vanishing extra element), i.e. **the
extremal witness never needs the full cardinality budget k+1 — it
achieves the min already at n=k.** This is a clean, checkable structural
fact that could become a genuine reduction lemma ("WLOG |R|≤k for the
minimizing R"), distinct from anything in the current file.

### Distinct candidate mechanisms (not developed into proofs)

1. **Extremal-principle / smoothing argument (new angle, most promising
   given the LP evidence).** Instead of induction-on-k via one recursive
   peel, fix (k,S,n) and argue directly about the *minimizer* of
   OddSum(R∪Γ_{k-1}): show any two-element mass transfer that keeps sum
   fixed either (a) is non-improving when it moves mass toward extremes
   (pins elements at 0 or cap, exactly the "vertex of a piecewise-linear
   functional on a polytope" fact my LP relies on), or (b) creates a tie
   with a Γ-value, both of which force the minimizer into the specific
   "chain + tied pair" shape found numerically above. This is a genuinely
   different top-level target than induction-on-k: it proves the Lemma
   directly for *all* k at once by characterizing extremal points of a
   fixed polytope family, sidestepping the "does the residual shrink the
   cap" circularity entirely. Crux-corpus analogue below.

2. **Two-parameter strengthened induction (per dispatch item (a)).**
   Define GCH2(L, cap, b; S) with L = chain-length, cap fixed at the
   *original* 2^{k-1} (not shrinking), Γ-index dropping by 1 and budget b
   dropping by 1 per peel — exactly the family round 18 already
   identified as necessary but did not attempt. My extremal-structure
   finding gives a candidate closed form for what this two-parameter
   family's own tight bound should be (peel exactly the elements matching
   the chain 2^{k-1},...,2^{k-1-j+1} together with Γ's matching top j
   values, leaving a residual instance with Γ-index k-1-j and the SAME
   cap 2^{k-1}, sum S − (2^k − 2^{k-j})). This is a concrete, checkable
   candidate recursion, but developing and proving it is out of scope for
   this scouting report.

3. **"WLOG |R|≤k" reduction lemma.** Since the LP evidence shows the true
   minimizer never uses the full cardinality budget k+1, a standalone
   lemma "any minimizing R can be assumed to have |R|≤k, at the cost of
   at most one degenerate (≈0) extra slot" could decouple the count bound
   from the induction variable k entirely, potentially removing the
   circularity dispatch flagged (the induction would then only need to
   track a fixed-size witness family, not a shrinking cardinality cap
   tied to k). Unverified as a general claim — only checked at k=3,4,5,
   a few S values.

### Cheap-kill candidates
- Re-verify round 18's numeric claim is not compromised: it is not wrong
  (the true min is always ≥ the reported approximate min, since SLSQP
  reports a value ≥ global min for a minimization it got stuck on) — so
  no violations were missed, but the "tightness to 1e-12" language should
  be corrected to "true equality, confirmed via exact LP" going forward.
- The essentiality of the cardinality cap (re-confirmed): relaxing n
  beyond k+1 breaks the bound (k=3,S=8.3,n=5 gives 7.65 < 8.15, matching
  round 18 exactly) — this remains a hard requirement, not removable.

### Knowledge-base entries to use
- Any convexity/majorization/rearrangement entry in `knowledge_base.md`
  applicable to piecewise-linear extremal problems on a simplex (check
  for an "extremal point of LP on polytope" or "rearrangement inequality"
  entry — I did not find a bespoke one but the general LP-vertex
  machinery already used elsewhere in this proof (`global-lp-vertex-
  sufficiency` approach) is directly transplantable to this sub-lemma:
  the same "affine functional extremized at a polytope vertex" argument
  that approach uses for the outer problem applies verbatim to R's
  polytope here).

### Analogous past problems (cruxes)
- `aimo-0119` (combinatorics, extremal-principle): "Pick the configuration
  minimizing the maximum part load, tie-broken by fewest parts attaining
  that maximum, so that any single-item transfer from the heaviest to the
  lightest part is non-improving." This is structurally the closest
  analogue found: a smoothing/extremal-principle argument on a minimizer
  of a load-type functional under a fixed-sum constraint, exactly the
  shape of mechanism (1) above. Worth adapting: define the minimizer of
  OddSum(R∪Γ_{k-1}) for fixed (k,S,n), and show any legal mass transfer
  between two R-elements that stays feasible (respects cap and positivity)
  is non-improving, forcing the extremal shape found numerically.
- `aimo-0666` (leximinimal/extremal tie-break) — same family (choose the
  extremal object under a tie-break, derive local structure) but for
  graph colorings; less directly transplantable (different object type),
  listed for completeness only.
- No crux found that solves a "cardinality-capped half-sum with geometric
  target" directly; nothing forces re-deriving from scratch is avoidable
  — these are hints for the *mechanism* (smoothing/extremal principle),
  not a solved analogue of this exact statement.

### Prior progress
- k=2 instance: fully proved and certified
  (`lemmas/sharper-odd-residual-and-k2-cardinality-half-sum.md`).
- Sharper residual range for e=1 (any k): proved in full, certified same
  file — true open range is a1 ∈ (2^k−1, 2^k].
- General-k GCH: conjecture only, NOT certified. This round strengthens
  the evidence considerably (exact LP equality at k=2..5, not just
  approximate near-1e-12) and, new this round, identifies the exact
  extremal witness family and the fact that it never needs the full
  count budget k+1 — genuinely new structural content not in the round-18
  file.

### Dead ends (do not retry)
- Plain single-parameter induction on k via "peel the tied cap element,
  recurse on GCH(k−1)": diagnosed by round 18 (correctly) as circular —
  the residual keeps cap=2^{k-1} while only the Γ-index drops, so it is a
  smaller instance of the *same* unproven excess-1 phenomenon, not a
  genuine smaller GCH instance. My LP data supports this diagnosis is
  correct (the true minimizer generalizes the k=2 proof's single-cap-peel
  step only weakly — the extremal chain has k−2 tied elements, not 1,
  confirming a single peel cannot reach the true extremal shape in one
  step).
- Unconstrained/lightly-restarted continuous optimizers (SLSQP-style) for
  this objective: shown this round to get stuck in bad local optima
  (non-smooth piecewise-linear objective) — future numeric checks on this
  Lemma should use the exact-LP-per-interleaving method above, not
  restart-heuristics, to avoid both false negatives (missed true minimum,
  as happened here) and to actually certify tightness rather than merely
  bound it.

### Small-case / intuition notes (labeled conjecture except where noted)
- **Conjecture, now on stronger footing**: GCH(k) holds with equality
  along the *entire* range S∈[2^k,2^k+1) (not just at isolated points),
  attained by the explicit chain-plus-tied-pair family described above.
  Verified exactly (LP) for k=2,3,4,5 at 3-4 values of ρ each; k=6 only
  partially checked (n up to 5, not the full n≤7).
- **Conjecture**: the minimizing R never needs |R|=k+1; |R|=k suffices.
  Verified (LP) for k=3,4,5 at 2 values of ρ each.
- These are still small-case numeric findings, not proofs — the outliner
  should treat the extremal-structure characterization as a *target* to
  prove (e.g. via mechanism 1, the smoothing/extremal-principle argument),
  not as an established fact.
