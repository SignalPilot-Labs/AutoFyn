# unified-residual-budget-induction

## Status
partial

## Approaches tried
- **Round 8 (this round, NEW slug):** Strong induction on cut count `N` via removal of a
  BF-invisible (even-multiplicity) tie-block, aiming to close Gap A′ (deg≥3 cycle-piece), Gap B
  (μ=3 even leaf) and the dual Budget Lemma at once through a single `f(P)=f(complement)≥1` peel.
  - **PROVED (clean, new, promotable): measure-form BF-invisibility.** Removing any even block
    (`2m` equal copies of any value `v`) from a multiset preserves `f` *exactly*, via the
    layer-cake identity `f = M := measure{t : #{pieces>t} is odd}`: adding/removing `2m` copies of
    `v` changes `#{pieces>t}` by an even number for every `t`, so the *parity* of `#{pieces>t}` is
    unchanged at every `t`, hence the set `{t : #{pieces>t} odd}` and its measure `M=f` are
    unchanged. This is strictly more general and far cleaner than the certified telescoping
    `odd-block-formula`/`symmetric-odd-block-move` (it needs no block-adjacency, no rank ordering,
    no distinct-powers hypothesis). Verified 0 failures / 20000 random cases (`f=M` and invariance).
  - **RESOLVED the reviewer's G2 tension — as a NEGATIVE structural fact (the decisive finding).**
    The complement peel does NOT type-check as an induction over `W_m`-refinements, AND inducting
    over the natural broader class is circular. Precise statement below (Current best). This kills
    the approach as a *finisher* in its outlined form; it is recorded honestly, not papered over.
  - **Outcome:** honest `partial`. One reusable lemma (measure-form BF-invisibility) to promote; the
    load-bearing G2 gap is shown to be an *equivalence*, not a reduction — the peel relocates the
    difficulty without shrinking it. Status stays `partial`; the approach cannot close the residual
    as designed. (Keep as population member: the measure-form lemma is a genuine tool and the G2
    negative characterization redirects the field.)

## Current best

### The proven engine (new this round)

**Lemma UBI-1 (measure-form BF-invisibility).** For any finite multiset `P` of positive reals, let
`f(P)=Σ_i(-1)^{i}a_i` (values sorted descending, `i=0,1,2,…`) be the alternating sum, and let
`M(P)=measure\{t>0 : #\{x∈P : x>t\}\text{ is odd}\}`. Then `f(P)=M(P)` (certified
`layer-cake-alt-sum`), and for every value `v>0` and every even integer `2m≥2`,
`f(P ∪ \{v\}^{2m}) = f(P)`.

*Proof.* Write `g_P(t)=#\{x∈P:x>t\}`. Adding `2m` copies of `v` gives
`g_{P'}(t)=g_P(t)+2m·𝟙[t<v]`, which differs from `g_P(t)` by an even number for every `t`. Hence
`g_{P'}(t)≡g_P(t) (mod 2)` for all `t`, so `\{t:g_{P'}(t)\text{ odd}\}=\{t:g_P(t)\text{ odd}\}` and
`M(P')=M(P)`. With `f=M` this gives `f(P')=f(P)`. ∎

This is the exact formalisation of "even tie-blocks contribute `0` to `f`", with the cleanest
possible proof. It removes *any* even-multiplicity value, whether or not it is a within-piece
bisection pair or a value shared across several dyadic pieces.

Verified: `f({8/3,8/3,8/3,8/3,2,4/3,1}) = f({2,4/3,1}) = 5/3` (the reviewer's example) and 0
failures / 20000 random even-block additions.

### The induction spine (valid as a schema)

For a `≤n`-cut refinement `P` of `W_n={2^0,…,2^n}` we want `f(P)≥1` (this single residual — `f≥1`
at the tied non-degenerate minimizer — is all that stands between the certified upper bound and a
full solve). By Lemma UBI-1, if `P` contains *any* value `v` of even multiplicity, deleting a pair
of copies preserves `f`; iterating deletes **every** even-multiplicity value down to odd
multiplicity, reaching a multiset `P_odd` with `f(P_odd)=f(P)` in which **every value has odd
multiplicity**. So:

> **Reduction (schema).** It suffices to lower-bound `f` on the *odd-multiplicity residuals* of
> `≤n`-cut refinements of `W_n`, i.e. `min f(P) = min\{f(Q) : Q=P_odd\text{ for some }P\}`.

This is a genuine structural simplification of the *object* (all Gap-A′/Gap-B/all-even blocks are
peeled to bare odd-multiplicity residuals). **It is not, however, a reduction of the difficulty** —
see the wall below.

### The load-bearing gap G2 — precise resolution of the reviewer's tension

The outline hoped to invoke `Claim(N−k)` on the complement `P'=P_odd`. The reviewer's decisive
observation is correct and I confirm it, then characterise it exactly:

**(i) The complement is not a `W_m`-refinement.** For the canonical Gap-B minimizer
`P^*=\{8/3,8/3,8/3,8/3,2,4/3,1\}` (`Σ=15=D_3`, `f=5/3`, a genuine `3`-cut refinement of `W_3`),
peeling the even block of four `8/3`'s gives `P'=\{2,4/3,1\}` with `f=5/3` **but** `Σ=13/3`, which
is not `D_m=2^{m+1}−1` for any `m`. So `P'` is outside the class over which `Claim` is stated.

**(ii) The only mass-conserving, in-class removal is a bisection pair — which is already certified,
and never the hard block.** A within-`W_n` removal that both conserves mass and stays a refinement
must correspond to *un-cutting*: merging `{v,v}` back into a single sub-piece `2v`. This requires the
two copies to be a **bisection pair** of one piece (`v=2^{k-1}`, piece `2^k→\{v,v\}`), which is
exactly the certified `matched-pair-invisibility` P1 move. The hard even blocks — a shared value `v`
that is **not a power of two** (Gap B's `v=2^k/3`; the deg≥3 cycle attachment; the dual Budget
Lemma's mult-`4` class) — cannot be un-cut, because un-cutting a shared block would merge copies
living in different dyadic pieces, violating the refinement structure. Reattaching the donor mass
instead (giving the donor `8/3` back so piece `4=\{4\}`) yields the genuine `W_2`-refinement
`\{4,2,1\}` (`Σ=7`) but `f=3≠5/3` — **BF is destroyed.** So for the hard blocks, (BF-preservation)
and (lands in a `W_m`-refinement) are mutually exclusive under any of the natural constructions.

**(iii) Inducting within the broader class is circular.** Let
`C=\{P_odd : P\text{ a }≤n\text{-cut refinement of }W_n\}` be the class of even-reduced
configurations (equivalently, the image of the refinement class under repeated even-block deletion).
By Lemma UBI-1, deletion **preserves `f`**, and the identity map (delete nothing) shows every
`≤n`-cut refinement lies in `C`. Therefore
`min_{Q∈C} f(Q) = min_{P\text{ refines }W_n,\,≤n\text{ cuts}} f(P)`. Consequently the statement
"`f≥1` on `C`" is **logically equivalent** to the original residual, not weaker. The cut-count
induction *does* strictly reduce `N` at the peel, but its **base case** — the elements of `C` with
no even-multiplicity value (all multiplicities odd), where no further peel is possible — is exactly
the object `\{2,4/3,1\}`-type residual: **tie-free, non-integral, `f=5/3`, and provably not a
minimizer of any `W_m`-refinement class**, so the certified `tiefree-minimizer-monochromatic`
(Lemma J, which gives integrality⇒`f≥1` only *at minimizers of the refinement class*) does **not**
apply. No certified lemma supplies a lower bound on `f` for these all-odd elements of `C`.

**Conclusion (honest).** The unified peel is an `f`-preserving *isomorphism of difficulty*: it maps
`{Gap A′ ∪ Gap B ∪ all-even blocks}` onto `{f≥1 for all-odd-multiplicity elements of the broader
class C}`, an equally hard (indeed equivalent) statement over a strictly larger domain. The reviewer's
G2 tension is therefore **not a fixable bookkeeping issue but a genuine wall**: to close it one must
prove a `f`-lower bound on `C` (or on its all-odd base) that is not implied by `f≥1` on
`W_n`-refinements — a strictly new inequality, which this approach does not supply.

### Secondary gap G1 (cut-cost), for the record

The outline's "a shared block of size `t` costs `≥t` cuts" is **imprecise as stated** and is not
needed once G2 is seen to be a wall. The correct, provable fragment: *if a value `v` is not a power
of two `2^k (0≤k≤n)`, then no copy of `v` is an uncut whole piece, so every dyadic piece containing
a copy of `v` is cut (has `≥2` sub-pieces).* Hence a value `v∉\{2^k\}` shared across `d≥2` pieces
forces `≥d` distinct cut pieces, i.e. `≥d` cuts, plus `μ_{leaf}−1` further cuts inside any piece
holding `μ_{leaf}≥2` copies. For Gap B (`v=2^k/3`, leaf holds `3` copies, `1` donor): `≥ 2` (trisect)
`+1` (donor split) `=3` cuts. This is correct but does **not** rescue G2 (the freed cuts land the
complement outside the `W_m` class, per (i)).

### Net position

- **Upper bound** `c(n)≤2^n/D_n` — CERTIFIED (imported; not re-derived here).
- **Answer** `c(n)=2^n/D_n`, `D_n=2^{n+1}−1` — pinned; `min f=1` confirmed `n≤4`.
- **Lower bound residual** `f≥1` — this approach reduces it (cleanly) to the all-odd-multiplicity
  case but proves, rigorously, that its intended finishing move (the complement peel) is an
  equivalence, not a reduction. The residual remains open along this route.

## Full proof
Not present — Status is `partial`. The residual `f≥1` at the tied non-degenerate minimizer is not
closed: the complement peel is shown (Current best, part (iii)) to be an `f`-preserving map into a
strictly larger class whose lower bound is equivalent to the original claim, so the approach cannot
finish as designed.

## Promotable lemmas

**Lemma UBI-1 (measure-form BF-invisibility).** For any finite multiset `P` of positive reals with
alternating sum `f(P)=Σ_i(-1)^i a_i` (descending) and layer-cake measure
`M(P)=measure\{t>0:#\{x∈P:x>t\}\text{ odd}\}`, one has `f(P)=M(P)`, and for every `v>0`, `m≥1`,
`f(P∪\{v\}^{2m})=f(P)`. *Proof:* adding `2m` copies of `v` shifts `g_P(t)=#\{x>t\}` by
`2m·𝟙[t<v]`, preserving `g_P(t) mod 2` for all `t`, hence preserving `\{t:g_P(t)\text{ odd}\}` and
`M=f`. (Proved in full above; verified 0/20000.) Strictly generalises and simplifies the certified
`odd-block-formula` and `symmetric-odd-block-move` (no adjacency/rank/distinct-power hypotheses).
Reusable across all three live routes as the definitive "even blocks are `f`-invisible" statement.

*(Negative, worth caching as a "do-not-retry" for the field, not a lemma to certify:)* the
complement peel over `W_n`-refinements is an `f`-preserving injection into the larger even-reduced
class `C` with `min_C f = min_{refinements} f`; so any induction that removes a non-power-of-two
shared even block and invokes `Claim` on the complement is circular unless accompanied by a strictly
new lower bound on `C`'s all-odd base.
