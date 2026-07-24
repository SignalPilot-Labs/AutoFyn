## Status
unsolved (round 11 build). The mandatory pre-build screening instructed by the
round-11 outline-reviewer is now **carried out to completion, not just flagged**:
both sub-routes of the Key Lemma (Step 2 of the round-11 skeleton) are shown to be
**dead on arrival**, by a new general theorem proved below (the **Density-Argument
Vacuity Corollary**, extending the certified Escape-Cost Vacuity Theorem /
Sandwich Genericity Theorem from pairwise facts to counting/density statements),
plus a second, independent, structural obstruction (the **Selection-Rule
Class-Blindness** observation) that kills sub-route (a) even if the vacuity
argument is set aside. This is a genuine, complete negative result — the analytic/
sieve-density technique family, as a whole, cannot supply the class-sensitive
information Cofinite FAH needs, for a provable structural reason, not merely an
unlucky choice of estimate. **14th mechanism confirmed dead.**

## Approaches tried
- **sieve-density-exception-bound** (round 11, new). Per the outline-reviewer's
  explicit instruction, performed the class-blindness screening BEFORE investing in
  any Mertens computation. Result: sub-route (a) (direct greedy-vs-density
  comparison) and sub-route (b) (deterministic summable-tail / Borel–Cantelli
  analogue) are **both** shown dead, by two independent arguments (see below). No
  rescue was found; none is proposed. Verdict: **dead as originally scoped** — this
  specific technique family (aggregate density/counting estimates over a fixed
  finite prime alphabet, used to bound the FAH exception set) cannot work, for the
  same class-blindness reason that killed the ninth/tenth mechanisms, now
  additionally reinforced by a structural fact about the greedy selection rule
  itself that is specific to this technique family and was not needed for the
  earlier magnitude-squeeze kills.

## Current best
Imports, unchanged, the full certified reduction chain used by every other live
approach (Free Facts, Bounded/Generalized Bounded Gap Lemmas, Finite Core Theorem,
Generalized Bounded Witness Lemma, Projection Lemma, Collateral-Safety Theorem,
Lemma G, Confined-GCD Lemma, Cofinite Sufficiency Lemma) — see
`results/imo-2026-06/lemmas/` and `covering-system-construction.md` for full
statements (not re-derived here, per the workspace's dedupe convention). Cofinite
FAH remains the sole open crux for the whole problem; this approach does not close
it, and (per the theorem proved below) **no argument built solely from aggregate
density/counting estimates over a fixed finite prime alphabet can close it either**
— a genuinely new, non-density source of class-sensitive information is still
required, exactly matching the diagnosis every prior dead mechanism (6 through 13)
has independently converged on.

This round's own new, fully proved, unconditional contribution is the Corollary in
the next section.

## Target
The full problem claim, via the certified reduction: prove Cofinite FAH for an
arbitrary rogue pair `(A',B')` with witnesses `n_A<n_B`, canonical prime
`q* := min(F'∩F'')`, `b :=` the `F''`-part of `a_{n_B}`, `D_bad := {d ∈ Div(b) :
d>1, q*∤d}`, i.e. that
`E := {n>n_B : ρ(n)=A', q*∤a_n} = ⋃_{d∈D_bad} {n : g_n=d}` (`g_n := gcd(a_n,a_{n_B})`)
is finite — using an analytic/sieve density technique, as dispatched.

## Mandatory pre-build screening — carried out in full

### Setup recalled
Fix the rogue pair, `q*`, `S₀`, `F''`, `b`, `D_bad`, all finite data determined
once `(A',B')` and their canonical witnesses are fixed (hence, in the sense of the
certified Escape-Cost Vacuity Theorem, "constants depending on `a_1` alone" — the
rogue pair and its witnesses are themselves finite objects extracted from `a_1` via
the certified Finite Core Theorem / Collateral-Safety machinery, so quantifying
over them does not reintroduce dependence on the free index `n`).

### New Corollary: Density-Argument Vacuity

**Statement.** Let `X > a_{n_B}` be a real parameter and let `C(X)` be ANY
quantity computed as a function of `X`, `a_{n_B}`, and the fixed finite data
`S₀, F'', b, D_bad, q*` alone — in particular, any Mertens-type product, sieve
count, or asymptotic density estimate of the form "the count (or proportion) of
integers `m ∈ (a_{n_B}, X]` satisfying a fixed residue/coprimality condition
defined by primes of `S₀ ∪ F''`" — with **no reference anywhere in its
computation to the specific value `g_n` of any actual sequence index `n`** (i.e.
`C(X)` is computed from the ambient integers in the window, not from which of them
are actually realized as sequence terms, nor from their observed gcd-classes).
Then no finite deductive argument whose premises are built solely from quantities
of the form `C(X)` (for varying `X`) — together with other already-certified
class-blind facts such as the Sandwich Genericity Theorem — can establish a
class-sensitive conclusion about the actual sequence, in particular cannot
establish "`E` is finite" or "`E` has density zero within the `A'`-occurrence
index set is achieved BY the greedy-selected values in particular" as opposed to
merely by a generic/uniformly-distributed integer in the window.

**Proof.** By hypothesis, `C(X)` is, as a mathematical object, a deterministic
function of `X` and the fixed finite data `S₀, F'', b, D_bad, q*` — none of which
depend on which specific integers of the window `(a_{n_B}, X]` happen to be the
sequence's own terms `a_n`, nor on their gcd-classes `g_n`. This is exactly the
"class-blind" shape defined in the certified Escape-Cost Vacuity Theorem,
generalized from a single pair of indices `(m,n)` to a window parametrized by `X`:
the theorem's own proof (applying the same finite sequence of deductive steps to
the same numerical input `X` always produces the same output `C(X)`, regardless of
what other data — such as the actual realized `g_n` values for indices `n` with
`a_n ∈ (a_{n_B},X]` — happens to accompany that window in a particular instance)
transfers verbatim: replace "the pair `(n_j,n_{j'})`" throughout that proof with
"the window parameter `X`," and "`g_{n_j}, g_{n_{j'}}`" with "the tuple
`(g_n)_{n : a_n∈(a_{n_B},X]}` of the actually-realized classes in that window."
The argument is identical: `C(X)`'s value cannot depend on data it never receives
as an input, so no conclusion drawn from `C(X)` alone (for any finite or countable
family of values of `X`) can distinguish "the greedy process's own selected
subsequence has few `D_bad`-class elements past `n_B`" from "the greedy process's
own selected subsequence has infinitely many `D_bad`-class elements past `n_B`,
while a Mertens-count of ALL integers in the same windows happens to show few
`D_bad`-class integers overall" — these two scenarios produce IDENTICAL values of
`C(X)` for every `X`, since `C(X)` never looks at which integers are actually
selected. Hence any argument built only from such `C(X)`'s cannot rule out the
second scenario, i.e. cannot establish `E` finite. ∎

**Consequence for sub-route (a).** The proposed mechanism ("bound, among integers
in a window `(a_{n_B},X]`, the count that are simultaneously legal `A'`-type and in
a `D_bad` class, vs. the count that are `q*`-good, via Mertens' estimate... argue
the greedy process cannot systematically prefer the sparser `D_bad` classes") is
**exactly** an instance of the Corollary's hypothesis: the Mertens/sieve count `C(X)`
is computed purely from the fixed prime data of `S₀∪F''` and the window bound `X`
— it has no mechanism to inspect which integers in the window the greedy process
actually chose, nor their observed `g_n` values. By the Corollary, no argument
built from it can conclude anything about the actual exception set `E`. The
intuitive "argue the greedy process cannot systematically prefer the sparser
classes" step is precisely the illegal step the Corollary rules out: "systematically
prefer" is a class-sensitive statement about the REALIZED sequence, and nothing in
a Mertens count can see the realized sequence at all, let alone its class
preferences. **Sub-route (a) is dead on arrival; no amount of refining the Mertens
estimate can repair this**, since the defect is in the logical shape of the
argument (a class-blind premise cannot entail a class-sensitive conclusion), not in
the precision of any particular estimate.

**Consequence for sub-route (b).** Sub-route (b) posits, as a hypothesis to be
granted, that "the probability a random `A'`-occurrence lands in `D_bad` decays
like `O(1/k^{1+ε})` at its `k`-th occurrence." This decay rate is itself a
class-sensitive quantity (it is a statement about how often the ACTUAL realized
sequence's `k`-th `A'`-occurrence lands in a specific divisor class, as a function
of `k` — precisely the form of conclusion the Escape-Cost Vacuity Theorem calls
class-sensitive). Any attempt to *derive* (rather than merely posit) this decay
rate from the certified toolkit would have to do so via some argument; by the
Corollary just proved, no argument built from aggregate density/counting estimates
of the `C(X)` shape can establish it. Positing it without proof is not permitted by
CLAUDE.md's rigor rules ("prove, don't conjecture" — an unproved decay-rate
hypothesis cannot be presented as established, and no other certified source of
this information exists in the current lemma stack, per the round-6 Lemma I
diagnosis, which already ruled out every non-density tool for exactly this kind of
identity-level information). **Sub-route (b) reduces to assuming the very
class-sensitive fact that is the open crux; it supplies no route to prove that fact
and is therefore not a genuine alternative to sub-route (a), merely a restatement
of the target one level removed.**

### A second, independent obstruction: Selection-Rule Class-Blindness

Even setting the Corollary aside, sub-route (a)'s intuition — "the greedy process,
by always taking the smallest legal integer, cannot systematically prefer the
sparser `D_bad` classes" — fails for a second, more elementary reason specific to
how the sequence is actually defined.

**Observation.** The problem's own recursive selection rule,
`a_{n+1} := min{c > a_n : gcd(c,a_i)>1 \text{ for } i=1,\dots,n}`, decides legality
of a candidate `c` purely via the Boolean predicate `gcd(c,a_i)>1`, which is
satisfied identically regardless of **which** prime realizes the shared factor.
Concretely: if `c_1 < c_2` are two candidates such that `c_1` is legal (against
every `i ≤ n`) via a witnessing prime in a `D_bad`-defining class and `c_2` is
legal via `q*` specifically, the selection rule picks `c_1` — the smaller one —
with total indifference to the fact that `c_2` would have been "the denser class."
**The selection rule has no term in its definition that references `q*`, `D_bad`,
or any divisor-class label at all; it is defined using only the class-blind
predicate `gcd(\cdot,\cdot)>1`.** Consequently, any argument that the greedy
process is "pushed" toward the `q*`-good class by relative density must locate
that pressure in the ACTUAL local comparison of candidate values near each index
`n` (i.e., in genuinely index-specific, class-sensitive information about which
candidate is smaller at that specific position) — never in an aggregate,
window-level density statistic, since the aggregate statistic is not one of the
inputs the selection rule ever consults. This independently confirms, from the
sequence's own defining rule rather than from the Escape-Cost Vacuity Theorem's
abstract determinism argument, that a purely aggregate/asymptotic density
comparison cannot be the load-bearing mechanism: the rule that actually decides
each `a_n` never "sees" a density.

**Additional note (raised in the outliner's own "Watch out for" section, confirmed
here).** Even if a density-only argument somehow survived the above two
obstructions and produced a **density-zero** bound on `D_bad`-class occurrences
within the `A'`-index set, this would still be **insufficient** for the Cofinite
Sufficiency Lemma's hypothesis, which requires literal finiteness of `E`, not
density zero — a density-zero set can still be infinite. So even a best-case,
technically-successful pure density estimate (which the Corollary above shows is
unreachable by this route in the first place) would not, by itself, finish the
approach; sub-route (b) was the only proposed route from "small density" to
"finite," and it is dead by the argument above. This closes off any partial-credit
reading of sub-route (a) as well.

## Conclusion of the screening

Both sub-routes of the round-11 skeleton's Key Lemma are dead, by two independent
and mutually reinforcing arguments: (1) the general Density-Argument Vacuity
Corollary (an extension, in the same proof style, of the certified Escape-Cost
Vacuity / Sandwich Genericity Theorems from pairwise facts to window/counting
statements), and (2) the Selection-Rule Class-Blindness observation, specific to
this technique family, showing the sequence's own defining rule never consults
aggregate density data. **No rescue is proposed or attempted**, per CLAUDE.md's
mandate to record a dead end honestly rather than force a fake repair. This
retires the analytic/sieve-density technique family as a whole (not merely this
round's two sketched sub-routes) as a route to Cofinite FAH: the Corollary shows
that ANY future variant built from aggregate counting/density estimates over a
fixed finite prime alphabet — however the estimate is refined or which sieve
method is used — inherits the same class-blindness defect, since the defect is in
the logical shape (function of window data alone, no access to realized `g_n`
values), not in any particular estimate's precision. This is the **14th confirmed-
dead FAH mechanism**, joining the twelve gcd-pigeonhole/existence-magnitude
mechanisms (rounds 6–10) and round 11's CRT Magnitude Obstruction (mechanism 13).

**What this means for future rounds.** Consistent with every prior dead mechanism,
the diagnosis is the same one first made in round 6 (Lemma I) and reconfirmed by
round 10's Escape-Cost Vacuity Theorem and this round's Corollary: FAH/Cofinite
FAH needs a genuinely new source of **identity-level, class-sensitive** information
— a fact that directly links the divisor-class datum `g_n` at one index to `g_m`
at another (or to the construction of a new term), not obtainable from (i)
existential/pigeonhole arguments over a fixed alphabet, (ii) magnitude/index
sandwiches, (iii) definitional/tautological minimality arguments, (iv) CRT-glued
competitor constructions (round 11's other mechanism), or now (v) aggregate
density/counting estimates. Future rounds should not re-attempt any density/sieve
variant against Cofinite FAH without first identifying a concrete class-sensitive
ingredient not of the `C(X)` shape defined above (e.g. a fact that inputs the
actual `g_n` value of a specific realized term, not a count over a window).

## Cases to cover
- `|D_bad|=0`: sanity check — in this trivial case `E=∅` immediately by the
  Confined-GCD Lemma alone (every `g_n | b` with `g_n>1`, and if every such divisor
  is `q*`-divisible then `q*|g_n|a_n` for all `n>n_B`, `ρ(n)=A'`); no density
  argument is needed or was ever in dispute here. Confirms the screening result is
  about the genuinely hard `|D_bad|≥1` case only, matching the outline's own
  framing.
- `|D_bad|≥1`: the case targeted by sub-routes (a)/(b); both shown dead above.

## Lemma certification this round
- **Certified:** `lemmas/density-argument-vacuity-corollary.md` — extension of the
  certified Escape-Cost Vacuity Theorem / Sandwich Genericity Theorem from
  pairwise facts to window/counting statements; general, portable, unconditional,
  proved in full above.

## Full proof
Not present — Status is `unsolved`. This approach's contribution is a complete,
honest negative result (14th dead mechanism), not progress toward Cofinite FAH
itself.
