## Lens: the "collateral rogue pairs" gap (surfaced round 5)

Scope per dispatch: does refining S₀ → S₁ = S₀ ∪ Q_R (recruiting primes to resolve
already-known rogue pairs V₀) spawn brand-new rogue pairs among base-type pairs that
were *previously safe* at S₀? Not a proof attempt — terrain report only.

### 1. What refinement does to ρ, and why the feared phenomenon can be ruled out

Refinement S₀ ⊆ S₁ acts on the extended-type map by restriction: for every n,
ρ₀(n) = P(a_n) ∩ S₀ = ρ₁(n) ∩ S₀. So every S₁-extended type A'' has a canonical
**S₀-projection** A' := A'' ∩ S₀, and — this is the fact that needs to be made
explicit, it is not yet a separately certified lemma but is a one-line argument of
exactly the same shape as the existing "base type of an extended type is persistent"
paragraph in `covering-system-construction` Step 4 — **if A'' is S₁-persistent then
A' is S₀-persistent**: every n with ρ₁(n)=A'' has ρ₀(n)=A' (fixed), so A' occurs at
least as often as A'', hence infinitely often. Call this the **Projection Lemma**
(not certified yet; recommend certifying it, it is trivial but load-bearing for the
argument below). Also note base type is invariant under projection: since Q ⊆ S₀,
A'' ∩ Q = (A''∩S₀) ∩ Q = A' ∩ Q, so A'' and its S₀-parent A' always have the *same*
base type.

Given the Projection Lemma, every S₁-level extended-persistent pair (A'',B'') with
disjoint base types has a well-defined S₀-level parent pair (A',B') with the *same*
disjoint base types, and exactly two cases arise:

- **Parent pair was safe at S₀** (A'∩B'≠∅): then the already-certified **Monotonicity
  of Resolution Lemma** (`lemmas/monotonicity-of-resolution.md`) applies *directly* —
  it is stated exactly at this level ("every pair of S₁-extended-persistent types A'',
  B'' with A''∩S₀=A', B''∩S₀=B' satisfies A''∩B''≠∅") and needs no extra hypothesis
  (not even the Singleton Hypothesis). So **no child of a safe parent pair can ever be
  a new rogue pair, unconditionally.**
- **Parent pair was rogue at S₀** ((A',B') ∈ V₀): Monotonicity says nothing (there is
  no shared prime to inherit), so this is the only place new rogue pairs could
  possibly appear — but these are not "collateral damage to previously-safe types,"
  they are refinements of pairs *already flagged and targeted* by the Conditional
  Single-Pair / Simultaneous Resolution Theorem.

**Conclusion of this analysis:** the specific fear in the round-5 gap statement — that
refining S₀→S₁ manufactures new rogue pairs among base-type pairs that were entirely
safe at S₀ — is not a live threat at all, *given* the Projection Lemma (trivial,
recommend certifying) plus the already-certified Monotonicity Lemma. What is **not**
yet fully closed is the narrower residual question: among the children of an
*already-rogue* S₀ pair (A',B') ∈ V₀, does the Simultaneous Resolution Theorem's
construction (recruiting Q_R via each type's own canonical witness) resolve *every*
S₁-child, or could some other, non-canonical S₁-child of A' or B' survive and pair up
badly with something? See point 3 below — computation suggests this doesn't happen
either, for a stronger reason than previously noted.

### 2. Computational experiments (literal minimal/earliest-witness convention)

Script logic (Python + sympy factorint, naive but exact greedy generation, checking
gcd against literally all previous terms — no shortcuts): generate a_1..a_N for
various seeds, N up to 1600, take a tail window to detect persistence
(threshold: type occurs > 4–5 times in the tail), compute Q, persistent base types 𝒫,
canonical witnesses m_B = earliest index with τ = B, Finite Core S = ⋃(P(a_{m_B})\Q),
S₀ = Q∪S, extended-persistent types 𝒫'₀ from ρ₀, then V₀ (rogue pairs, disjoint base
types, S₀-disjoint), then Q_R via the Simultaneous Resolution recipe (each rogue
type's own earliest-occurrence witness, singleton outside-core factor), S₁ = S₀∪Q_R,
recompute 𝒫'₁ and check base-type-pair status.

**Seeds 187, 209, 247, 385** (the four known round-5 rogue seeds): confirmed
S₀, Q_R, S₁ exactly matching current.md's reported values (e.g. a_1=187: S₀={2,3,11,17},
Q_R={7}; a_1=247: S₀={2,5,7,13,19}, Q_R={3}; a_1=385: S₀={2,3,5,7,11,13}, Q_R={19}).
For every base-type pair that was **fully safe at S₀** (every extended refinement of A
meets every extended refinement of B), status at S₁ remained fully safe — **zero
collateral new-rogue instances** across all four seeds.

**Broadened scan:** 78 fresh seeds built as products of 2–4 distinct primes from
{5,7,11,13,17,19,23} (e.g. 1001=7·11·13, 5005=5·7·11·13, 17017=7·11·13·17,
96577=17·19·13·23, etc.), N=1200, tail window 600–1200. This exercises many more
disjoint-base-type pairs per seed (up to 21 fully-safe pairs in a single |Q|=4 seed).
**Total: 646 fully-safe base-type pairs tested across all seeds, 0 collateral new-rogue
instances found.** (Two of the 78 seeds, 11305 = 17·19·5·7 and 13685 = 17·23·5·7, do
have a nonempty V₀ of size 2, both confirmed singleton — consistent with, not
contradicting, the pattern.)

**A sharper structural finding (new, not previously recorded):** for every rogue type
A' ∈ R checked (i.e. every S₀-persistent type with a rogue partner, across all four
seeds), I tabulated its full S₁-child distribution over the tail window. In every
single case, **A' has exactly one S₁-child, and every tail occurrence of A' falls into
it** — e.g. a_1=187: type {17,2} has 34/34 tail occurrences going to child
(2,7,17); type {11,3} has 28/28 going to (3,7,11). a_1=247: type {2,13} has all 191
tail occurrences going to (2,3,13), etc. This is a direct, checkable consequence of
the Conditional Single-Pair Theorem's proof (it shows q | a_n for *literally every*
n > n_{B'} with ρ(n)=A', via the Generalized Bounded Witness Lemma applied to a
singleton F', not merely infinitely many via pigeonhole) — but it had not been
explicitly flagged as "full absorption, not just one witnessed instance." This closes
the concern that some *other* S₁-child of a rogue A' (one not containing q) could
persist alongside A'∪{q} and cause trouble: empirically (and per the proof) there is
no such second child — only finitely many pre-n_{B'} exceptions remain unaccounted,
and those are already outside the persistent tail.

### 3. Candidate proof mechanisms (sketches, not complete)

1. **Certify the Projection Lemma** (trivial, one paragraph, pattern already used in
   Step 4/Step 1 of `covering-system-construction`) and combine it with the already-
   certified Monotonicity Lemma. Together these give an unconditional, complete proof
   of exactly the "no collateral damage to previously-safe base-type pairs" half of
   the round-5 gap — no new hypothesis needed, no case split on Singleton Hypothesis.
   This looks like a genuine, cheap, closeable sub-result for next round: a short
   "Collateral-Safety Theorem" stating: *if (A,B) is a disjoint base-type pair with
   every S₀-extended refinement pair intersecting, then every S₁-extended refinement
   pair intersects too, for any S₁ ⊇ S₀* — a direct corollary of Monotonicity +
   Projection, provable in under a page.

2. **Full-absorption lemma** (new structural observation, point above): under the
   Singleton Hypothesis, prove in general (not just spot-checked) that a rogue type
   A' has, past its recruiting witness's partner index n_{B'}, literally only ONE
   S₁-child (A'∪{q}) among persistent types — i.e., strengthen "the specific pair is
   resolved" to "the whole base-level equivalence class collapses, with no other
   surviving branch." This looks like a close reread/tightening of the existing
   Conditional Single-Pair Theorem's proof (the "for every n" clause is already
   there) rather than new machinery — mostly a matter of stating and certifying the
   corollary explicitly. This would fully answer "could some other child of a rogue
   type survive and misbehave" for the Singleton-Hypothesis case, at S₁.

3. **Induction on number of recruitment rounds / |S|:** given (1)+(2), an induction
   on stage k of the recruitment process becomes attractive: at each stage, the only
   possible new rogue pairs are children of stage-k rogue pairs (by (1) applied with
   S₀:=S₀^(k), S₁:=S₀^(k+1)), and (2) says each such rogue type fully collapses into
   one child (under Singleton Hypothesis at that stage) — so the "frontier" of
   still-open pairs is exactly the newly-formed pairs among the resolved children,
   which by construction already intersect (share q). This suggests the recruitment
   process, IF the Universal Singleton Hypothesis holds at every stage (still the
   main open item, priority 1 in current.md), has NO room to manufacture new rogue
   pairs at all beyond finitely many recruited primes — i.e. the "collateral rogue
   pairs" gap may collapse entirely once (1)+(2) are certified, leaving the Universal
   Singleton Hypothesis (at every stage, not just S₀) as the one real remaining
   target. This is a sketch, not a proof: it still needs (a) the Projection Lemma
   formally, (b) the full-absorption corollary formally, and (c) an argument that no
   *new* disjoint base-type pairs (not present at S₀ at all) can appear at S₁ — base
   types live at the Q level, fixed once and for all (Q = P(a_1) never changes), so
   this last point is actually free: the set of persistent BASE types 𝒫 is an S₀-
   independent, Q-level notion, so "new disjoint base-type pairs" cannot arise from
   refinement at all — only new EXTENDED refinements of already-existing base-type
   pairs, which is exactly what (1) and (2) already cover.

4. Monovariant candidates specific to this sub-gap: number of *still-open* base-type
   pairs (⊆ C(|𝒫|,2), a fixed finite bound depending only on Q) is non-increasing by
   (1) and strictly decreasing at any stage where a genuine rogue pair gets resolved
   by (2) — this is the natural monovariant round 2/round 5 already flagged as
   "the right kind of bound if each round permanently resolves a whole base-type pair
   in full" — and point (2)'s full-absorption finding is exactly the missing
   ingredient that was previously missing to make this monovariant argument go
   through (previously it was only known that the *witnessed instance* resolves, not
   the *whole* base-type pair).

### 4. Crux corpus techniques worth trying

Queried `past_crux_moves_database.json` filtered to
`invariants-and-monovariants` / `processes-and-algorithms` / `size-bounding-and-descent`
in number_theory and combinatorics for "stabilize / terminate / refine / partition /
invariant" language. No exact structural match (this is a fairly bespoke
partition-refinement setup), but two adaptable patterns:

- **aimo-0060** (combinatorics, invariants-and-monovariants): "upgrade a merely strict
  monovariant decrease into an additive drop of a fixed amount, so an infinite-descent
  argument still terminates for an infinite configuration" — same shape as the
  "number of open base-type pairs strictly drops by ≥1 per resolved pair" monovariant
  in point 3/4 above; the crux's technique of pinning down a *fixed* per-step decrease
  (not just "some" decrease) is the right template if a future round needs to bound
  the *total number of rounds* rather than just show monotonicity.
- **aimo-0156** (combinatorics, invariants-and-monovariants): "bound the count of
  moves that preserve a modular invariant by treating them as edges of a self-avoiding
  walk on that invariant class (at most |class|-1 of them)" — structurally close to
  the CRT-residue / extended-type-class bookkeeping already used in Step 5's finish;
  worth reusing its "self-avoiding walk on a finite invariant-class space" framing if
  the final CRT+cyclic-pigeonhole step (Step 5) needs tightening once (†) is closed,
  though it is not directly about the collateral-rogue-pair sub-gap itself.
- No crux was found that matches "prove a partition refinement cannot manufacture new
  cross terms" directly — this appears to be a genuinely bespoke structural fact of
  this problem's recruitment process, best handled by the direct Monotonicity+
  Projection argument in section 1 rather than an imported technique.

### Bottom line for next round

The "collateral rogue pairs among previously-safe types" half of the round-5 gap
looks **closeable now, cheaply, unconditionally** (no Singleton Hypothesis needed):
certify the Projection Lemma (S₁-persistent types project to S₀-persistent types,
trivial one-paragraph proof) and combine with the already-certified Monotonicity of
Resolution Lemma to get a "Collateral-Safety Theorem." Computationally: 0/650 tested
fully-safe base-type pairs across 82 seeds became rogue after refinement, and the
theoretical argument above explains *why* this must always be so, independent of any
open hypothesis. The remaining, genuinely open content is (a) the Universal Singleton
Hypothesis itself (current.md priority 1, untouched by this lens), and (b) whether,
under that hypothesis, the *full-absorption* property (section 3, point 2) can be
made a certified corollary of the existing Conditional Single-Pair Theorem's proof —
which the computation strongly supports (every rogue type's tail occurrences collapse
100% into one S₁-child in all cases checked) but which is not yet written down as a
separate, citable statement.
