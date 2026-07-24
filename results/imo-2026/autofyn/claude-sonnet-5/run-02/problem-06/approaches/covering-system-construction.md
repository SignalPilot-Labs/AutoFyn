## Status
partial (round 27: second single-seed reapplication dispatched by the outline-reviewer
— closes the residual divisor class `d=103` for the OTHER standing test seed
`a_1=11305`'s rogue pair (`A'={2,5}`, `B'={3,7}`, canonical witnesses `n_A=7, n_B=4` —
note the canonical-order swap relative to `a_1=4807`, handled explicitly below by
relabeling before invoking the certified Finite-Window Literalization Lemma). This is
a routine, careful reapplication of round 26's certified machinery — no new lemma
content — but genuine, fully verified progress: literal (zero-exception) Joint FAH is
now proved, unconditionally, for a SECOND standing hard test seed. Full argument in
the new Step 4i below. As with round 26, this remains single-seed: the general
FAH/Cofinite-FAH crux (†) is untouched, so Status stays `partial` overall.)

partial (round 26: bounded, scoped advance dispatched by the outline-reviewer —
**FULLY CLOSES** the single residual divisor class `d=13` for the standing test seed
`a_1=4807` flagged open since round 12's Reduced-Alphabet Corollary. This is a genuine
positive result, not another negative/vacuity finding, but it is a **single-seed**
closure, not a general FAH/Cofinite-FAH theorem — the workspace's standing crux (†)
(general `a_1`) is untouched and remains open, so Status stays `partial` overall. Full
argument in the new Step 4h below; summary: applying the already-certified Two-Sided
Singleton Witness Theorem's own supporting witness (`x_1=72`, a NON-canonical
`B'`-occurrence with singleton out-of-core factor set `{17}`) together with a new,
short, fully rigorous "Finite-Window Literalization Lemma" (proved below, and a
genuinely reusable promotable result) that upgrades that theorem's Cofinite-FAH
conclusion to literal (zero-exception) FAH whenever the finite window between the
canonical and the singleton witness contains no occurrence of the type in question —
verified for `a_1=4807` by an explicit, fully displayed table of `a_8,...,a_72`
showing none has extended type `A'={3,5,19}` — gives `17 | a_n` for literally EVERY
`n>7` with `ρ(n)=A'`. Combined with the certified Confined-GCD Lemma (`g_n ∈
Div(221)={1,13,17,221}`, `g_n>1`), this forces `g_n ∈ {17,221}` always, so
`g_n=13` — the Reduced-Alphabet Corollary's lone residual class — **never occurs, for
any `n`, unconditionally**. Together with the already-known `B'`-side resolution
(Singleton-Side FAH, `F'={17}` singleton at the canonical witness `n_A=6`), this gives
a complete, unconditional proof of literal Joint FAH for `a_1=4807`'s standing rogue
pair. Honest scope: this does NOT prove general FAH/Cofinite FAH for arbitrary `a_1`
— the existence of a matching singleton non-canonical witness (the input the
mechanism needed) is, per the Two-Sided Singleton Witness Theorem's own certified
scope note, "a genuine, unproved, narrower existence question" not established for
general seeds; it is exactly what closes the ROUND-26 SCOPED TASK ("does d=13 ever
occur for a_1=4807?") completely and honestly, per the outline-reviewer's explicit
bounded framing.)

partial (round 12: bookkeeping-only round, per this round's outline/outline-review —
no new FAH mechanism dispatched here, matching round 11's bar against a 15th
same-corridor variant. Formalized and certified the small **Reduced-Alphabet
Corollary** flagged by this round's smallcase math-explorer: combining the already-
certified Confined-GCD Lemma (`lemmas/confined-gcd-lemma.md`) with the already-
certified Singleton-Side FAH Lemma (`lemmas/singleton-side-fah.md`), whenever a rogue
pair has a singleton far-side factor set on ONE side (so Singleton-Side FAH already
fully resolves that side, with zero exceptions), the residual "bad divisor class" set
`D_bad` for the OTHER (open) side is confined to a fixed, explicitly finite, closed-
form-computable set of size `∏_{p∈F''\{q*}}(e_p+1) − 1` (notation below) — independent
of `n`, and in the concrete `|F''|=2` case this workspace has used as its standing
open test bed (a_1=4807, 11305), collapses to a SINGLE residual divisor class. This is
proved in full below (Step 4g) as a one-line, unconditional corollary of the two
imported certified lemmas — it does **not** close FAH/Symmetric FAH, does not reduce
the number of primes that must be ruled out to zero, and does not supply any new
class-sensitive mechanism (the Escape-Cost Vacuity Theorem, round 10, still forecloses
every currently-known magnitude-only route to ruling out even this single remaining
class). It is exactly what it is scoped to be: a bookkeeping sharpening of the
ALPHABET SIZE of the open obstruction, importable by any approach (in particular
`seed-coupling-induction`'s orphaned Lemma B, per this round's outline) that wants to
count, rather than re-derive, the residual rogue-pair target. Certified as
`lemmas/reduced-alphabet-corollary.md`. No FAH progress is claimed or implied; Steps
1–11's open gap (†) / FAH / Symmetric FAH are entirely unchanged by this round.)

partial (round 10: BUILT — the dispatched Step 11 "Growth-Forced Divisibility"
mechanism's central open item, the Escape-Cost Lemma, is now RETIRED with a clean,
unconditional negative result (the "Sandwich Genericity / Escape-Cost Vacuity
Theorem," Step 11.6 below): the Bounded/Generalized Bounded Gap Lemma's linear
value-vs-index-gap sandwich `n-m ≤ a_n-a_m ≤ (n-m)·a_1` holds identically for EVERY
pair of indices, independent of type, extended type, or divisor class — so it carries
zero class-discriminating information and cannot, by itself or in combination with any
other currently-certified class-blind fact, be strengthened into a divisor-class-
dependent index-gap lower bound of the kind the Escape-Cost Lemma needs. This is
proved rigorously (not just empirically), confirming the outline-reviewer's flagged
"linear-cancels-linear" vacuity risk is REAL and FATAL as scoped, and closes off a
tenth mechanism for FAH/Cofinite FAH (after Lemma I's six, round 8's Fixed-Witness
Divisor-Chain, round 9's Recruitment-Budget Lemma, and round 9's Successor-Transport/
successor-claim stall). A numeric premise check (Step 11.5, run first per Step C's
instruction) on the properly-recruited a_1=4807 rogue pair found the relevant bad
divisor class D_bad={13} has ZERO observed occurrences among the (rare, only 9 in
6000 terms) A'-occurrences sampled — consistent with Cofinite FAH continuing to hold
on this seed but too sparse to test the growth claim's premise directly; this
numeric finding is inconclusive on its own and is superseded in strength by the
algebraic vacuity proof. Round 9's findings (below) are unchanged and remain valid.)

partial (round 9: carried out the dispatched mandatory Step-4 computational check for
the Recruitment-Budget Lemma — does every prime recruited by the Generalized Bounded
Witness Lemma's Corollary, at every stage k of the S₀-recruitment process, lie in the
FIXED, Q-level pool W_{A,B} := P(a_{m_A}) ∪ P(a_{m_B}) (m_A, m_B the base-type earliest
witnesses)? Result: **REFUTED**, with an explicit, small, fully hand-verifiable
counterexample (a_1 = 209: at the process's second recruitment round the new prime
q = 7 is forced, but 7 divides neither of the base-type witnesses a_2 = 220 or
a_3 = 228, only a later, differently-typed witness a_4 = 231). Confirmed robust across
five independent seeds (187, 209, 247, 4807, 11305) at two sample sizes (N = 4000,
15000) with proportionally scaling occurrence counts (ruling out a finite-window
artifact). Per this round's dispatch instructions ("if Step 4 REFUTES the claim... do
not silently expand [the pool] ad infinitum without proving it is still finite and
independent of k"), the Recruitment-Budget Lemma as scoped is dead; the natural
"rescue" (grow the pool to include every witness's primes as they get used) is shown
below to be circular — it re-describes the open recruitment process itself rather than
supplying an a priori finite Q-level bound, so it is not pursued as a fix. This is the
eighth mechanism found not to close the FAH/recruitment-termination gap; see Step 10
below for the full account. Round 8's findings (unchanged) follow.

partial (round 8: attempted this round's dispatched Fixed-Witness Divisor-Chain
mechanism for Joint FAH, scoped to Lemma-G rogue-pair witnesses, in full — Step 8.9.
Result: the mechanism's Key Lemma (Exception Finiteness) does NOT go through; a
genuine logical gap was found and proved in the outline's own proposed dichotomy
(its branch "r ∈ S₀ ⟹ contradicts rogueness" is false — r ∈ S₀ only forces the
tautological r ∈ A', giving no information), which is MORE BASIC than, and prior to,
the canonicality sub-step the outline-reviewer flagged. As an honest byproduct, an
unconditional Singleton-Side Lemma was proved and shown to fully explain this round's
(and the outline-reviewer's) positive computational examples (a_1=187, 209 both have
F'=F''={7}, singletons) — meaning that evidence never actually tested the genuinely
open |F'|,|F''|≥2 regime (confirmed by a fresh a_1=4807 computation at an
un-recruited core, where the analogous claim fails on 751/801 sampled occurrences).
Step 9.4 documents that the secondary n=1 gap's proposed direct-verification strategy
is not yet well-posed, since it needs the FINAL S₀, which is only available once
Joint FAH is resolved — a dependency not previously stated explicitly. Joint FAH
remains open in general; round 7's closed results (Step 8.7 canonicalization, Step
8.8 symmetry check, the n=1 gap's Exact-Equality Reduction Lemma) stand unchanged.)

## Current best

**Round 27 update.** TWO standing hard test seeds now have literal (zero-exception)
Joint FAH fully proved, unconditionally, for their standing rogue pairs:
`a_1=4807` (round 26, residual class `d=13` closed) and `a_1=11305` (this round,
residual class `d=103` closed — see Step 4i below for the complete argument, which
required correctly handling a canonical-order swap `n_B<n_A` relative to `4807`'s
`n_A<n_B`, not a blind copy of the earlier case). Both closures use the identical
certified mechanism (Two-Sided Singleton Witness Theorem + Finite-Window
Literalization Lemma + Confined-GCD Lemma / Reduced-Alphabet Corollary), applied to
seed-specific numerical data (a non-canonical singleton witness located by search on
each seed, plus an exhaustive finite-window vacancy check). This is genuine, scoped
progress — a second independent data point that the mechanism is robust, not an
artifact of one seed's arithmetic — but it remains, honestly, single-seed-at-a-time
closure: the existence of a matching non-canonical singleton witness on the "hard"
side of a rogue pair is, per the Two-Sided Singleton Witness Theorem's own certified
scope note, an unproved existence question in general, and no argument in this file
supplies one for arbitrary `a_1`. The workspace's standing crux (†) (general FAH for
arbitrary `a_1`) is completely untouched by either closure, so Status remains
`partial` overall. (This assessment matches the round-27 explorer's own honest
ceiling note: "a third data point at best," no visible route from "close another
seed" to "close the general theorem.")

**Round 26 update.** The single residual bad-divisor-class `d=13`, isolated by round
12's Reduced-Alphabet Corollary for the standing test seed `a_1=4807`'s rogue pair
(`S₀={2,3,5,11,19,23}`, `A'={3,5,19}`, `B'={2,11}`, canonical witnesses `n_A=6,n_B=7`),
is now **proved, unconditionally, never to occur** — see Step 4h below for the full,
self-contained argument. This closes the exact task the outline-reviewer scoped for
this round (either prove `d=13` can never occur, or exhibit it occurring). It is a
genuine single-seed positive result (literal, zero-exception Joint FAH now holds for
this one rogue pair), built by combining two already-certified lemmas
(Two-Sided Singleton Witness Theorem, Confined-GCD Lemma) with one new, short, fully
proved, promotable lemma (Finite-Window Literalization Lemma) plus an explicit,
displayed finite computation (the sequence `a_1,...,a_80`, with every term's
`S₀`-signature shown). It does **not** establish general FAH/Cofinite FAH for
arbitrary `a_1` — see Step 4h's closing "Honest scope" paragraph — so the workspace's
long-standing crux (†) is unchanged and this file's Status remains `partial` overall.

**Round 10 update.** The dispatched Step 11 "Growth-Forced Divisibility" mechanism's
Escape-Cost Lemma (the entire new content the outline proposed) is now shown, by a
short unconditional proof (Step 11.6 below, "Sandwich Genericity / Escape-Cost
Vacuity Theorem"), to be structurally undervable from Step A's magnitude sandwich
alone: `n-m ≤ a_n-a_m ≤ (n-m)·a_1` is a universal fact about every pair of indices,
with no reference anywhere to type, extended type, or divisor class, so no argument
built from it can output a conclusion that discriminates between "same bad divisor
class repeats" and any other pair of same-extended-type occurrences. This confirms,
rigorously rather than by risk-flagging alone, that the round's central new mechanism
cannot close FAH/Cofinite FAH as scoped — a tenth mechanism retired. The certified
Confined-GCD Lemma and Cofinite Sufficiency Lemma (imported, unconditional) are
unaffected; the crux (Joint Cofinite FAH / the Successor Claim) remains exactly where
round 9 left it, still requiring a genuinely new class-discriminating source of
information not yet supplied by any certified tool in this workspace. See Step 11.5
(numeric premise check) and Step 11.6 (vacuity proof) for full detail.

**Round 9 update.** The dispatched Recruitment-Budget Lemma (a proposed global
counting-budget bound: every prime ever recruited against a fixed disjoint base-type
pair (A,B) lies in a FIXED, a-priori Q-level-computable pool W_{A,B}) is **refuted**
by an explicit small counterexample (Step 10). This closes off an eighth mechanism
(after the six diagnosed by Lemma I plus round 8's Fixed-Witness Divisor-Chain) for
the FAH/recruitment-termination gap, with the refutation traced precisely to the
already-certified Witness Discontinuity Obstruction, now shown to bite the specific
mechanism this round targeted, not merely to be an abstract risk. All of round 8's
results (below) and the earlier unconditional chain stand unchanged; see Step 10 for
the full round-9 account, including why the natural "expand the pool" rescue is
circular rather than a fix.

Unconditional, no-gap results (Steps 1–3, 4d–4e, 8.1–8.3, 8.7–8.8, 9.1–9.2): (i) the
Bounded Witness Lemma and Finite Core Theorem give an explicit finite core prime pool
S₀ with no density/growth-rate argument; (ii) the Projection Lemma + Collateral-Safety
Theorem show a base-type pair, once fully safe, stays safe forever, reducing gap (†) to
termination of a monotone sequence open(k) over a FIXED finite set of ≤ C(|𝒫|,2)
base-type pairs; (iii) this termination is shown (Step 8.5, conditional) to follow from
Symmetric FAH for every currently-open pair, and Step 8.7–8.8 (round 7) narrow
"FAH + Symmetric FAH" to a single canonical-prime, side-agnostic Blocking-Data Bridging
Lemma, decoupled from the sibling approach's Two-Witness Intersection Uniqueness
target; (iv) the separate secondary "literal periodicity from n=1" gap is reduced
(Step 9.1, round 7) to finitely many explicit equalities, and shown (Step 9.2, round 7,
via an explicit counterexample) to genuinely require the greedy recursion's structure,
not a formal rescaling trick. **Open gap:** the Blocking-Data Bridging Lemma itself
(the actual mechanism for FAH/Symmetric FAH) is not proved in this file — owned in its
A'-side form by the sibling approach `greedy-exchange-cost-potential`, still open there
too as of this round. The n=1 gap's Step 9.3 candidate strategy has a precisely
identified, unresolved point of failure. Given both open gaps, Step 5's CRT +
cyclic-pigeonhole finish is not yet unconditional.

**Round 8 update.** This round's dispatched Fixed-Witness Divisor-Chain mechanism
(Step 8.9) was carried out in full and does NOT close Joint FAH: the finite-divisor
pigeonhole it relies on can, and per the toolkit's current state cannot be shown not
to, produce a pigeonholed prime r that is simply an already-known element of the
base type A' itself (r ∈ S₀), which yields no contradiction with rogueness — a gap
that is prior to and independent of the outline-reviewer's flagged canonicality
question. An unconditional Singleton-Side Lemma (F'' singleton ⟹ cofinite, in fact
total, divisibility on the A'-side) was extracted as a genuine, if narrow, byproduct,
and shown to fully account for this round's positive computational evidence — none
of which tested the genuinely open |F'|,|F''| ≥ 2 case. Joint FAH remains open; see
Step 8.9 for the complete accounting.

## Approach: covering-system-construction (explicit constructive induction on the prime core)

### Target
The full problem claim: there exist positive integers T, L such that a_{n+T} = a_n + L
for every positive integer n.

### Technique
Direct, constructive argument: (1) fix the finite "seed" set Q of prime factors of a_1;
(2) classify every later term by its Q-divisibility pattern ("type"); (3) prove — this
is the round's main deliverable, replacing the outline's unproven "primorial growth vs.
gap bound" heuristic with an actual argument — that only a bounded, EXPLICITLY finite
extra pool of primes S is ever needed to reconcile terms of disjoint types, by a clean
double pigeonhole on prime factors of a small number of fixed witness terms; (4) attempt
to promote this to full eventual periodicity via CRT + cyclic pigeonhole. Step (4) is
where a genuine, precisely-located gap remains, honestly reported below.

### Setup and notation
Let a_1 < a_2 < a_3 < ... be the sequence. For a positive integer m, write P(m) for its
set of distinct prime factors. Let Q = P(a_1); since a_1 > 1, Q ≠ ∅, and Q is a fixed
finite set, |Q| = k.

**Free Fact 1.** For every n ≥ 2, gcd(a_n, a_1) > 1, i.e. P(a_n) ∩ Q ≠ ∅.

*Proof.* By hypothesis with the pair (n-1)+1 = n and i = 1 ≤ n-1 (valid since n ≥ 2):
a_n is required to satisfy gcd(a_n, a_i) > 1 for every i = 1, ..., n-1, in particular for
i = 1. ∎

**Free Fact 2 (pairwise gcd).** For all 1 ≤ i < n, gcd(a_i, a_n) > 1.

*Proof.* Immediate from the defining hypothesis applied at step n-1 → n, taking the
index i in the hypothesis's range 1, ..., n-1. ∎

For n ≥ 2 define the **type** τ(n) := P(a_n) ∩ Q, a nonempty subset of Q (nonempty by
Free Fact 1). There are finitely many possible types: τ(n) ∈ 𝒯 := 2^Q \ {∅}, a set of
size 2^k − 1.

### Step 1 — persistent types are finite in number and eventually exhaust the index set

Since 𝒯 is finite and every n ≥ 2 has τ(n) ∈ 𝒯, by the pigeonhole principle
(`knowledge_base.md` "Pigeonhole / extremal principle") at least one type occurs
infinitely often. Call a type **persistent** if it occurs for infinitely many n, and let
𝒫 ⊆ 𝒯 be the (nonempty, finite) set of persistent types. Every type in 𝒯 \ 𝒫 occurs, by
definition of "not persistent," only finitely many times; since 𝒯 \ 𝒫 is a finite set of
types, the total number of indices n with τ(n) ∉ 𝒫 is a finite sum of finitely many
finite quantities, hence finite. So there is an index N_0 such that

  τ(n) ∈ 𝒫 for every n > N_0.  (★)

This is a fully rigorous double-pigeonhole argument, not an appeal to "eventually" left
unproved.

### Step 2 — the Bounded Witness Lemma (the round's main new result)

**Lemma (Bounded Witness).** Let A, B ∈ 𝒫 be two persistent types with A ∩ B = ∅
(disjoint as subsets of Q). Fix ANY single index m with τ(m) = B and let
F_{A,B} := P(a_m) \ Q, a fixed finite set of primes (finite because a_m is one specific
positive integer, hence has finitely many prime factors) that does **not** depend on n.
Then: for every n > m with τ(n) = A, the term a_n is divisible by some prime in F_{A,B}.

*Proof.* Fix such n > m with τ(n) = A. By Free Fact 2, gcd(a_n, a_m) > 1, so
P(a_n) ∩ P(a_m) ≠ ∅; pick a prime p in this intersection. Suppose for contradiction that
p ∈ Q. Since p | a_n and p ∈ Q, p ∈ P(a_n) ∩ Q = τ(n) = A. Since p | a_m and p ∈ Q,
p ∈ P(a_m) ∩ Q = τ(m) = B. So p ∈ A ∩ B = ∅, a contradiction. Hence p ∉ Q, so
p ∈ P(a_m) \ Q = F_{A,B}. Since p | a_n, a_n is divisible by an element of F_{A,B}. ∎

This is a complete, self-contained proof — no appeal to density, growth rates, or
covering-system heuristics; it is pure pigeonhole on the (finite) prime factorization of
a single fixed witness integer a_m. It is the mechanism the outline gestured at with the
imprecise "primorial growth vs. gap bound" language; the correct, rigorous form needs no
growth-rate comparison at all.

**Remark (uniformity).** The lemma gives something stronger than "infinitely many
A-type terms are divisible by a common prime": it gives that ALL A-type terms with
index beyond the witness's index are divisible by some element of the fixed finite set
F_{A,B} (not merely infinitely many of them, and the set F_{A,B} is fixed once m is
fixed, independent of how large n grows).

### Step 3 — the Finite Core Theorem

**Theorem (Finite Core).** For each B ∈ �𝒫, fix one witness index m_B := the smallest
index n > N_0 with τ(n) = B (exists since B is persistent). Define

  S := ⋃_{B ∈ 𝒫} (P(a_{m_B}) \ Q),

a finite union of finite sets, hence finite. Let S_0 := Q ∪ S, also finite,
|S_0| ≤ k + Σ_{B∈𝒫} ω(a_{m_B}) (ω(·) = number of distinct prime factors). Let
N_1 := max(N_0, max_{B∈𝒫} m_B). Then: for every n > N_1 and every B ∈ 𝒫 with
B ∩ τ(n) = ∅, the term a_n is divisible by some prime of S.

*Proof.* Apply the Bounded Witness Lemma with A = τ(n), the witness m = m_B (valid
since τ(m_B) = B by construction and m_B ≤ N_1 < n). It gives a_n divisible by some
prime of F_{τ(n),B} = P(a_{m_B}) \ Q ⊆ S. ∎

This Theorem rigorously establishes that S is a FIXED, EXPLICITLY finite pool of primes
— bounded by an explicit expression in terms of the (finitely many) chosen witness
integers — such that every sufficiently large term of any persistent type is, for the
purpose of reconciling with each disjoint persistent type, divisible by a member of
this pool. |𝒫| ≤ 2^k − 1, so the recruitment is a ONE-ROUND process against a
bounded list of |𝒫| witnesses; it is not an unbounded recursive recruitment, and no
"termination of an infinite recruitment process" argument is needed — the pool is
written down in closed form after a single pass.

### Step 4 — refined (extended) types, and the precise remaining gap

For n ≥ 1 define the **extended type** ρ(n) := P(a_n) ∩ S_0 ∈ 2^{S_0}, a finite space
of size 2^{|S_0|} not depending on n. Exactly as in Step 1 (same pigeonhole, applied to
the finite space 2^{S_0} instead of 𝒯), the set 𝒫' of extended types occurring
infinitely often is finite and nonempty, and there is N_0' such that ρ(n) ∈ 𝒫' for all
n > N_0'.

Every ρ(n) ⊇ τ(n) (since S_0 ⊇ Q), so ρ(n) ≠ ∅ automatically, and if A' ∈ 𝒫' is an
extended-persistent type, its **base type** A := A' ∩ Q is a (base-level) persistent
type: if A' occurs infinitely often, so does its base type A ⊇ ... (every index n with
ρ(n) = A' has τ(n) = A' ∩ Q = A, so A occurs at least as often as A' does, hence
infinitely often, so A ∈ 𝒫).

**What is fully proved at this level.** If A', B' ∈ 𝒫' are extended types with disjoint
BASE types (A := A' ∩ Q, B := B' ∩ Q, A ∩ B = ∅ — note A, B ∈ 𝒫 by the previous
paragraph), then applying Step 3's Theorem to the (infinitely many) n with ρ(n) = A':
for every such n > N_1, a_n is divisible by some prime of F_{A,B} = P(a_{m_B}) \ Q ⊆ S
⊆ S_0. Since a_n is divisible by this prime p and p ∈ S_0, p ∈ P(a_n) ∩ S_0 = ρ(n) = A'
— note ρ(n) is the SAME fixed set A' for every such n (that is what "ρ(n) = A' for
infinitely many n" means), so this shows the FIXED set A' contains an element of the
FIXED set F_{A,B}, i.e. A' ∩ F_{A,B} ≠ ∅. This is a genuine, valid deduction (it uses
only that at least one qualifying n exists, which holds since A' is extended-persistent
by assumption).

**The gap.** The deduction above shows A' meets F_{A,B} = P(a_{m_B}) \ Q, i.e. A'
contains a prime dividing the *specific chosen witness* a_{m_B}. It does **not** by
itself show A' ∩ B' ≠ ∅ for the *specific* extended type B' we started with, because
several different extended types can share the same base type B (i.e. B ∈ 𝒫 can be
refined by 𝒫' into multiple distinct extended-persistent types B'_1, B'_2, ... — for
instance, the S_0-signature of B-type terms could itself vary from occurrence to
occurrence within the finite space 2^{S_0 \ Q}), and the witness a_{m_B} realizes only
one particular such refinement, say B'_0, not necessarily the B' under consideration.
What is missing to complete the periodicity argument is a proof that:

  (†) for every two disjoint-base-type extended-persistent classes A', B' ∈ 𝒫', we in
  fact have A' ∩ B' ≠ ∅ (not merely A' ∩ F_{A,B} ≠ ∅ for one specific witness-derived
  set F_{A,B}),

or, failing that, a proof that the extra freedom in which refinement occurs does not
actually obstruct the final "CRT + cyclic pigeonhole" step (Step 5 below) — e.g. by
running Step 5 directly at the level of *base* types plus a case analysis over the
(now bounded, since 𝒫' is finite) finitely many refinements, rather than needing (†) in
its clean form. I was not able to close this in the time available; attempts to patch it
by choosing witnesses at the extended level instead reintroduce witnesses a_{m_{B'}}
whose extra prime factors are not a priori confined to the already-fixed pool S_0 (since
a_{m_{B'}} is a new integer, not one of the original witnesses), which threatens to
restart an unbounded-looking recruitment; showing that this secondary recruitment in
fact terminates inside S_0 (rather than needing a further enlargement) is exactly the
content of (†) and I have not proved it. This is the precise, narrowed form of the gap
that the outline's Step 3 gestured at abstractly; Steps 1–3 above have fully resolved
the "how big can the core pool possibly need to be" question (answer: bounded by a
closed-form expression in |𝒫| ≤ 2^k−1 fixed witnesses) — what remains is a
consistency/uniqueness statement about which refinement is realized, not a growth-rate
or density estimate.

### Step 5 — the finish, CONDITIONAL on (†) (shared building block, sketched)

Granting (†) (all pairs of disjoint-base-type members of 𝒫' intersect, hence — since Q's
own types already pairwise satisfy "same type ⟹ intersect via Q," and different base
types are either non-disjoint, hence already intersecting via Q, or disjoint, hence
reconciled by (†) — every two elements of 𝒫' intersect as subsets of S_0):

Let L := ∏_{p ∈ S_0} p. By the Chinese Remainder Theorem (`knowledge_base.md` "Modular
arithmetic, CRT"), divisibility of an integer m by each p ∈ S_0 is determined by m mod L,
so ρ can be read off from a_n mod L: define for r ∈ Z/LZ, the signature
sig(r) := {p ∈ S_0 : p | r} — a well-defined function of r alone, and ρ(n) = sig(a_n mod
L) for all n. Let G := {r ∈ Z/LZ : sig(r) ∈ 𝒫'} — a *fixed, finite, nonempty* set of
"eligible residues," since 𝒫' is finite and nonempty.

For n > N_0' (so ρ(n) ∈ 𝒫', i.e. a_n mod L ∈ G) and with (†) available, the greedy rule
"a_{n+1} = smallest integer > a_n with gcd(a_{n+1},a_i)>1 for all i ≤ n" restricted to
candidates whose residue mod L lies in G automatically satisfies the constraint against
every earlier term of extended-persistent type (any two members of 𝒫' share an S_0-prime
by (†) and the base-type analysis, so any two integers with residues in G share a prime
factor) — and against the finitely many "early/transient" terms (index ≤ max(N_0,N_0')),
a finite, checkable exceptional list. Hence for n large the process reduces to: scan
integers greater than a_n in increasing order, skip those whose residue mod L is not in
G, take the first one whose residue is in G. This is a purely residue-driven,
n-independent rule, and running it forward is exactly cycling through the |G| residues
of G in increasing cyclic order (mod L), one per step, wrapping by +L every |G| steps.
By pigeonhole (finitely many residues in G) the process must, after at most |G| further
steps, land on a residue it has already visited relative to some starting point, and by
determinism of "smallest legal integer" the process from then on repeats with period
T = |G| and total value-increase L per period: a_{n+T} = a_n + L for all n beyond the
(explicit, finite) index where the cyclic rule takes over. Extending this identity back
to n = 1 is then a finite, direct verification for the (finitely many) small n below the
threshold — the outline-reviewer's simulations (see `/tmp/round-1/outline-reviewer.md`)
confirm empirically that in every tested case (a_1 = 4, 15, 35, 143, 1001) the identity
a_{n+T} = a_n + L in fact already holds from n = 1 with no exceptional prefix, but this
remains a case-by-case verification, not a general proof, and is moot until (†) is
established.

### Step 4b — RETRACTED (round 2, first attempt): Universal Glue Prime + sparse/dense split

**Retraction notice (round 2, second pass).** The "Universal Glue Prime Lemma" and the
sparse/dense case split proposed immediately below (kept verbatim for the record, with
this notice attached) is **false as stated** and is withdrawn. The outline-reviewer
found an explicit counterexample: for a_1 = 35 (Q = {5,7}, p* = 2, "sparse" by the
lemma's own definition since 2 ∉ Q), the persistent proper-base-type {5} contains
infinitely many odd terms deep in the tail (e.g. a_153 = 975 = 3·5²·13, a_157 = 1005 =
3·5·67, a_163 = 1035 = 3²·5·23 — a recurring pattern, not finitely many early
exceptions), so p* = 2 does **not** divide all sufficiently large type-{5} terms. I
independently re-ran this exact computation this round (see the verification note at
the end of Step 4c) and confirmed it: the true eventual period for a_1 = 35 is T = 34,
L = 210 = 2·3·5·7, i.e. reconciliation genuinely needs **two** extra primes {2,3}, not
one, even though Q is "sparse" (misses 2) in the lemma's sense. The dichotomy variable
("does Q contain small primes") is not the same as "how many extra primes are needed,"
so the case split is not just unproved but built on the wrong invariant. I am not
attempting to patch it; Step 4c below replaces it with a mechanism built on the actual
invariant (the finite family 𝒫' itself, not a distinguished single prime).

The original (now-retracted) text is kept below for the record, unmodified, followed by
Step 4c with this round's real replacement content.

Round 2's explorers (minimality and density lenses) found strong numerical evidence
(6+ seeds, thousands of sampled terms, see `/tmp/round-2/math-explorer-minimality.md`
and `/tmp/round-2/math-explorer-density.md`) that (†) has a much more concrete cause
than a general set-intersection coincidence: there is often a SINGLE extra prime that
glues every proper-base-type extended-persistent class together. This suggests
replacing the abstract (†) with two sharper sub-claims, split on whether Q already
contains small primes.

**Definition.** Let p* := the smallest prime not in Q (exists, since Q is finite and
the primes are infinite).

**Case (i): sparse Q (empirical regime: Q misses p* = 2, or more generally some small
prime).**

**Key Lemma (Universal Glue Prime Lemma — THE NEW TARGET, replacing (†) in this case).**
There is an index N_2 such that for every n > N_2 with τ(n) ⊊ Q (a *proper* base type),
p* | a_n.

*Why this would close (†) immediately, given the lemma:* if A, B ∈ 𝒫 are disjoint
persistent base types, neither can equal Q (Q ∩ B = ∅ with B ≠ ∅ forces B ⊊ Q, and
symmetrically A ⊊ Q, since Q∩A=∅ already implied A≠Q as A is nonempty and disjoint from
Q would mean A∩Q=∅, but A⊆Q so A=∅, contradiction — so both A,B are proper subsets of
Q). Hence every sufficiently large term of type A is divisible by p*, and every
sufficiently large term of type B is divisible by p*. So every extended-persistent
refinement A', B' ∈ 𝒫' of A, B (for n large enough that ρ(n) ∈ 𝒫' and τ(n) ∈ {A,B})
contains p* ∈ S_0 (since p* ∈ S by the Finite Core Theorem's construction whenever it
is ever recruited as a witness prime — if not automatically in S, adjoin it: redefine
S_0 := Q ∪ S ∪ {p*}, still finite). So A' ∩ B' ⊇ {p*} ≠ ∅ — (†) holds unconditionally
in this case, with NO refinement case-analysis needed at all.

**Proposed mechanism (minimality/exchange argument, not yet completed — this is the
open gap replacing the old, vaguer (†)).** Fix n large (beyond the Finite Core
Theorem's threshold N_1) with τ(n) ⊊ Q, missing some q_0 ∈ Q \ τ(n). Consider two
families of candidates for "how a_n could have been legally chosen":
  - *p\*-candidates*: integers m > a_{n-1} with m ≡ 0 (mod p*) and m's Q-pattern equal
    to some proper subset containing all primes needed to satisfy the FINITELY many
    "early/exceptional" indices (index ≤ N_1) — by Dirichlet-type density (residues mod
    p*·∏_{q ∈ Q} q form an arithmetic progression of positive density 1/(p*·|Q|-related
    constant)), such candidates occur with positive, FIXED density, hence gaps between
    consecutive p*-candidates satisfying the Q-pattern requirement are bounded by an
    explicit constant depending only on a_1 (via the same multiple-of-(a_1 · p*)
    argument as the Bounded Gap Lemma, Step 2 of Section 2 in `amortized-charging-budget`
    — a multiple of a_1·p* is always legal against every earlier index, by the same
    proof as the Bounded Gap Lemma with a_1 replaced by a_1·p*, since a_1·p* is also
    divisible by every prime of Q).
  - *q_0-avoiding, p\*-avoiding candidates*: integers with proper Q-pattern (missing
    q_0), NOT divisible by p*, that are legal against ALL of a_1,...,a_{n-1} — such a
    candidate must instead be linked to every disjoint-type earlier term via SOME OTHER
    prime not in Q ∪ {p*}, a strictly "more expensive" condition (a specific larger,
    less frequent prime, or several such primes simultaneously for different disjoint
    partners) than simply being ≡ 0 (mod p*).
  The claim to prove: for n large enough, the smallest legal candidate is always of the
  first kind, because the "cost" (density) of satisfying compatibility via p* is
  higher (denser, hence smaller expected gap) than via any fixed alternative prime
  scheme — **this requires an explicit comparison of candidate densities / gaps, not
  merely a qualitative appeal to "cheaper is smaller".** The builder should attempt
  this via a direct argument: exhibit, for each n > N_1 with τ(n) ⊊ Q, an EXPLICIT
  p*-divisible legal candidate ≤ a_n + a_1·p* (multiple of a_1·p*, by the immediate
  generalization of the Bounded Gap Lemma noted above), and separately show that if
  a_n itself is NOT divisible by p*, then a_n must be ≥ this bound already (else the
  greedy process would have chosen the smaller p*-multiple instead) — turning the
  Lemma into a direct minimality/smallest-candidate contradiction, not a density
  heuristic. This is the precise, narrowed form of the new gap.

**Case (ii): dense Q (Q already contains p* would be impossible by definition of p*,
so restate: dense Q means Q contains ALL "small" primes up to some point, e.g.
a_1 = 30, 210).** Numerics (`/tmp/round-2/math-explorer-density.md`, D3) show no single
extra prime dominates; the recruited pool spreads across several mid-size primes. This
case needs a SEPARATE argument — NOT the single-glue-prime mechanism. Proposed
fallback: run the original (†) argument (Steps 1–4 above, unchanged) directly at the
level of the *finite* set 𝒫' (finite regardless of regime, by Step 4's construction),
since in this regime the Finite Core Theorem's witness set S already has ≥ 2 elements
recruited with comparable frequency; a case-exhaustive check over the (now finite and
typically small, since |𝒫| ≤ 2^{|Q|}-1) set of extended-type pairs, rather than a
single universal-prime shortcut, may be tractable precisely because the state space is
finite and explicit (the difficulty in the general case was the ABSTRACT combinatorial
claim over an unspecified family; in this concrete dense-Q regime the family 𝒫' can be
enumerated case by case for any FIXED a_1, though a fully general a_1-independent proof
for this regime remains open here).

### Step 4c — Round 2 (second pass): the S₀-level Generalized Bounded Witness Lemma, an exact reformulation of (†) as a recruitment process, and the honest residual gap

This section is this round's real deliverable. It (a) proves a genuinely new, correct,
promotable lemma (the Bounded Witness Lemma generalized from Q-level types to S₀-level
extended types), (b) uses it to show *precisely* what (†) reduces to — a finite
iterative recruitment process — and (c) reports strong new computational evidence
(across 9 seeds, including a |Q| = 4 case) that this process needs **zero** further
rounds beyond the Finite Core Theorem's original S, while being explicit that a general
proof of this fact is still missing.

**Lemma (Generalized Bounded Witness, S₀-level).** Let S₀ ⊇ Q be *any* fixed finite set
of primes (not just S₀ from Step 3 — the statement and proof below make no use of how
S₀ was built), and define ρ(n) := P(a_n) ∩ S₀ for n ≥ 1. Let A', B' ⊆ S₀ be two
ρ-types with A' ∩ B' = ∅ (disjoint **as subsets of S₀**, a strictly stronger hypothesis
than Q-level disjointness). Fix any single index m with ρ(m) = B'. Then for every
n > m with ρ(n) = A', a_n is divisible by some prime of the fixed finite set
F'_{A',B'} := P(a_m) \ S₀, and in particular a_n has a prime factor outside S₀.

*Proof.* Identical in structure to the Bounded Witness Lemma (Step 2), with Q replaced
by S₀ and τ replaced by ρ throughout — the proof used only Free Fact 2 (pairwise gcd)
and the definition of type via intersection with a fixed finite set, so it goes through
verbatim: fix n > m with ρ(n) = A'. By Free Fact 2, gcd(a_n, a_m) > 1; pick a shared
prime p. If p ∈ S₀, then p ∈ P(a_n) ∩ S₀ = A' and p ∈ P(a_m) ∩ S₀ = B', so
p ∈ A' ∩ B' = ∅, contradiction. Hence p ∉ S₀, so p ∈ P(a_m) \ S₀ = F'_{A',B'}, and
p | a_n. ∎

**Corollary (Recruitment step).** With S₀, ρ, 𝒫' as in Step 4 (𝒫' = ρ-types occurring
infinitely often), suppose A', B' ∈ 𝒫' have disjoint base types (A' ∩ Q, B' ∩ Q
disjoint) **and** are themselves S₀-disjoint (A' ∩ B' = ∅) — i.e. suppose (†) fails for
this pair. Then there is a *specific prime* q ∉ S₀ such that q | a_n for **infinitely
many** n with ρ(n) = A'.

*Proof.* Since B' ∈ 𝒫', fix any witness index m with ρ(m) = B' (exists since B' occurs
infinitely often). By the Generalized Bounded Witness Lemma, every n > m with ρ(n) = A'
has a_n divisible by some prime of the fixed finite set F'_{A',B'} = P(a_m) \ S₀. Since
A' ∈ 𝒫', there are infinitely many such n (with n > m, still infinitely many after
discarding the finitely many n ≤ m). Each of these infinitely many n contributes at
least one "responsible" prime from the finite set F'_{A',B'}; by the pigeonhole
principle applied to a finite set receiving infinitely many assignments
(`knowledge_base.md` "Pigeonhole / extremal principle"), some single prime
q ∈ F'_{A',B'} ⊆ (P(a_1..)) \ S₀ is responsible for infinitely many of these n, i.e.
q | a_n for infinitely many n with ρ(n) = A'. ∎

**What this buys us: an exact reformulation of (†).** Define the following *finite*
iterative process, starting from S₀^(0) := Q ∪ S (the Finite Core Theorem's set from
Step 3):

- At stage k, compute 𝒫'_k, the (finite, nonempty, by the same pigeonhole as Step 1/4
  applied to the finite space 2^{S₀^(k)}) set of ρ_k-types (ρ_k(n) := P(a_n) ∩ S₀^(k))
  occurring infinitely often.
- If every pair A', B' ∈ 𝒫'_k with disjoint base types satisfies A' ∩ B' ≠ ∅, **stop**:
  S₀^(k) already establishes (†) (for this S₀^(k); replace S₀ by S₀^(k) throughout Step
  5's finish).
- Otherwise, by the Corollary, pick a violating pair and recruit the guaranteed new
  prime q ∉ S₀^(k); set S₀^(k+1) := S₀^(k) ∪ {q} and repeat.

Every step of this process (pigeonhole for 𝒫'_k's finiteness, and the Corollary's
recruitment) is fully rigorous and requires no growth-rate, density, or global-prime
heuristic — this is real progress over both the abstract (†) of Step 4 and the false
"universal glue prime" of the retracted Step 4b: it replaces both with a concrete,
mechanically well-defined procedure. **What is not proved is that this process
terminates after finitely many stages** (equivalently, that S grows only finitely
often before every disjoint-base-type extended-persistent pair is reconciled). This is
the single remaining content of (†): (†) holds **if and only if** the process above
halts in finitely many rounds, and every round of the process, individually, is fully
justified; the gap is exclusively the halting question, not any individual step.

**Why this is a strictly sharper statement of the gap than round 1's (†) or round 2's
retracted Step 4b.** (i) Unlike the retracted Step 4b, it makes no false claim about a
distinguished single prime — the recruited prime q at each round is whatever the
pigeonhole extraction happens to produce, and different rounds may recruit different,
unrelated primes (matching the a_1 = 35 data: {2,3}, not one universal prime). (ii)
Unlike round 1's abstract (†), it identifies *exactly* the missing ingredient
(termination of a specific, concretely-defined process) rather than an opaque
existence claim, so a future round has a precise target: either (a) find a monovariant
or potential function bounding the number of recruitment rounds (candidates tried and
rejected below), or (b) find a direct argument that S from Step 3 alone always already
suffices (equivalently, that the process above always halts in **zero** further rounds
beyond S₀^(0)), which the evidence below suggests may be the right thing to conjecture
and try to prove directly rather than via general termination of an unbounded-looking
process.

**Monovariant candidates tried and why they did not work (round 2).**
- *Number of persistent extended types |𝒫'_k|* is not monotonic in an obviously useful
  way: refining by a new prime q at most doubles each existing type (splits it into a
  "contains q" and "does not contain q" branch, at least one of which is infinite by
  definition of the refined type surviving), so |𝒫'_{k+1}| ≤ 2|𝒫'_k| — an *increasing*
  bound, not helpful for showing the process stops.
- *Reconciled pairs stay reconciled*: I verified (straightforward, included for
  completeness) that if A', B' ∈ 𝒫'_k already satisfy A' ∩ B' ≠ ∅ (share prime p ∈
  S₀^(k)), then every ρ_{k+1}-refinement of A' and every ρ_{k+1}-refinement of B' still
  share p (since refining only adds primes to a type's signature, never removes any),
  hence still intersect. So the set of "settled" base-type pairs is monotonically
  non-decreasing across rounds — this bounds the number of rounds *if* each round
  strictly newly settles at least one previously-unsettled BASE-type pair permanently,
  but I was not able to show a single round's recruitment fully settles a whole
  base-type pair (all its extended refinements) rather than merely one specific
  violating extended sub-instance — a genuine, unresolved caveat: after recruiting q to
  fix one violating (A', B') instance, other extended refinements of the SAME base
  pair (A, B) not involving q could in principle still violate (†), requiring further
  rounds restricted to that same base pair. Since there are only finitely many base
  pairs (≤ C(|𝒫|, 2)), if one could show each base pair needs *at most* a bounded number
  of rounds (not necessarily 0), termination would follow; this bound is exactly what
  is missing.
- *Growth-rate / prime-counting bound* (Σ_{n≤N} ω(a_n) = O(N log N / log log N) since
  a_n = O(n) by the Bounded Gap Lemma, so any single a_n has O(log N / log log N)
  distinct prime factors): this bounds the total number of (index, prime) incidences up
  to N, but does not directly bound the number of *distinct* primes that each recur
  infinitely often across the whole sequence, since a bounded-size prime factorization
  per term is compatible with unboundedly many distinct primes appearing across
  different terms. I could not turn this into a bound on recruitment rounds.

**Computational evidence (round 2, this pass) that the process may terminate in ZERO
further rounds beyond Step 3's S.** I ran the process's stopping check (not the
retracted Step 4b's single-prime claim) directly: for each of a_1 ∈
{35, 21, 33, 45, 77, 143, 55, 65, 91, 1155}, I built the sequence out to 1200–2500
terms, computed Q, the persistent base types 𝒫 (from the last 600–1500 terms), the
Step-3 set S using one witness per persistent base type, S₀ = Q ∪ S, the resulting
persistent extended types 𝒫' (from the tail), and exhaustively checked every pair of
extended-persistent types with disjoint base types for intersection within S₀. Result:
**zero violations found in every one of these 10 seeds**, including a_1 = 1155 = 3·5·7·11
(|Q| = 4, 15 persistent base types, 70 persistent extended types, |S₀| = 11), the most
complex case tested. This is consistent with (in fact stronger evidence for) the
conjecture that **the original, one-round Finite Core Theorem's S already suffices for
(†)** — i.e., that the recruitment process above needs zero further rounds in general —
but this is an empirical finding across finitely many seeds and finite windows, not a
proof; it does not by itself establish the claim for all a_1, and I was not able to find
a direct argument for "S from Step 3 alone suffices" in the time available. This
observation is offered as a concrete, sharper conjecture for the next round to target
directly, in preference to re-attacking the general unbounded-process termination
question.

**Summary of the round-2 (second-pass) net progress on (†).** (1) The false "universal
glue prime" claim is retracted, verified false, and not reused. (2) A new, fully proved,
promotable lemma (Generalized Bounded Witness Lemma, S₀-level) replaces it, together
with its Corollary (Recruitment step) — this is real, unconditional content, reusable by
any approach. (3) (†) is now known to be *exactly equivalent* to "the recruitment
process above halts in finitely many rounds," with every individual round of the
process rigorously justified — narrowing the gap from an abstract intersecting-family
claim to a concrete halting/termination question, plus a sharper, empirically-supported
conjecture ("zero further rounds needed") that a future round could try to prove
directly (e.g. by a cleverer double-counting or exchange argument specific to why the
canonical witness-realized refinement cannot fail to cover every other refinement, which
I was not able to produce in the time available). (†) itself remains open.

### Step 4d — Round 3: the Canonical-Refinement Lemma (full proof, new certified content)

This section makes fully rigorous a fact that was already implicit in Step 4's "What is
fully proved at this level" paragraph, isolates it as a standalone, cleanly-stated,
promotable lemma, and uses it to *localize* (†) to a strictly smaller residual family of
pairs. Nothing here uses any new hypothesis beyond what Steps 1–4 already certified.

**Lemma (General Reconciliation).** Let A, B ∈ 𝒫 be disjoint persistent (Q-level) base
types, and let A' ∈ 𝒫' be *any* extended-persistent type with A' ∩ Q = A (i.e. any
S₀-level refinement of A that itself occurs infinitely often). Then A' ∩ F_B ≠ ∅, where
F_B := P(a_{m_B}) \ Q is the (fixed, finite) extra-prime set of B's canonical witness
a_{m_B} from the Finite Core Theorem (Step 3).

*Proof.* Since A' ∈ 𝒫', by definition A' occurs infinitely often as ρ(n) := P(a_n) ∩ S₀;
in particular there are infinitely many n with ρ(n) = A', so in particular there is at
least one such n with n > N_1 (N_1 the finite threshold of Step 3, which bounds all the
canonical witnesses, so in particular m_B ≤ N_1 < n). Fix such an n. Since ρ(n) = A',
τ(n) = ρ(n) ∩ Q = A' ∩ Q = A. By the Finite Core Theorem (Step 3), applied to this n
(τ(n) = A, and B ∈ 𝒫 is disjoint from A = τ(n), with n > N_1 ≥ m_B), a_n is divisible by
some prime p ∈ F_{A,B} = P(a_{m_B}) \ Q = F_B (recall, as noted in Step 3's proof, the set
F_{A,B} produced by the Bounded Witness Lemma depends only on the witness index m_B —
i.e. only on B — not on A; the label "F_{A,B}" is the Bounded Witness Lemma's original
notation, but its value is exactly F_B := P(a_{m_B}) \ Q for whichever disjoint A is under
consideration). Since p | a_n and p ∈ F_B ⊆ S ⊆ S₀ (by the Finite Core Theorem's
definition S := ⋃_{C∈𝒫}(P(a_{m_C})\Q), so F_B is literally one of the finitely many sets
whose union is S), we get p ∈ P(a_n) ∩ S₀ = ρ(n) = A'. So p ∈ A' ∩ F_B, i.e.
A' ∩ F_B ≠ ∅. ∎

**Lemma (Canonical refinement equals base ∪ extra-primes, exactly).** With m_B, F_B as
above, the canonical witness's own extended type B'_can := ρ(m_B) satisfies
B'_can = B ∪ F_B exactly (not merely B'_can ⊇ B ∪ F_B).

*Proof.* B'_can = P(a_{m_B}) ∩ S₀ = (P(a_{m_B}) ∩ Q) ∪ (P(a_{m_B}) ∩ (S₀ \ Q)). The first
term is τ(m_B) = B by definition of m_B as B's canonical witness. For the second term:
P(a_{m_B}) ∩ (S₀\Q) = (P(a_{m_B}) \ Q) ∩ S₀ = F_B ∩ S₀. Since F_B ⊆ S ⊆ S₀ (shown above),
F_B ∩ S₀ = F_B. So B'_can = B ∪ F_B, and since B ⊆ Q while F_B ∩ Q = ∅ (F_B is defined as
a subset of P(a_{m_B})\Q, disjoint from Q by construction), this is a disjoint union
(no cancellation), giving equality, not just containment, at the set level. ∎

**Theorem (Canonical-Refinement Lemma).** Let A, B ∈ 𝒫 be disjoint persistent base types
with canonical witnesses m_A, m_B, canonical extended refinements A'_can := ρ(m_A),
B'_can := ρ(m_B). Then:
  (i) every extended-persistent A' ∈ 𝒫' refining A (A' ∩ Q = A) satisfies A' ∩ B'_can ≠ ∅;
  (ii) every extended-persistent B' ∈ 𝒫' refining B (B' ∩ Q = B) satisfies B' ∩ A'_can ≠ ∅.

*Proof.* (i) By the General Reconciliation Lemma, A' ∩ F_B ≠ ∅. By the previous Lemma,
B'_can = B ∪ F_B ⊇ F_B. Hence A' ∩ B'_can ⊇ A' ∩ F_B ≠ ∅. (ii) is identical with the
roles of A, B swapped (General Reconciliation Lemma applied with A, B interchanged gives
B' ∩ F_A ≠ ∅ for every extended-persistent B' refining B; and A'_can = A ∪ F_A ⊇ F_A). ∎

**What this closes, precisely.** (†) — i.e. A' ∩ B' ≠ ∅ for every pair of
extended-persistent types A', B' ∈ 𝒫' with disjoint base types A := A'∩Q, B := B'∩Q — now
holds automatically whenever A' = A'_can or B' = B'_can (i.e. whenever at least one side
of the pair IS its own base type's canonical refinement): if B' = B'_can, part (i) applied
to A' gives A' ∩ B'_can = A' ∩ B' ≠ ∅ directly; symmetrically if A' = A'_can, part (ii)
gives A' ∩ B' ≠ ∅. **The Canonical-Refinement Lemma does NOT by itself give A' ∩ B'_can'
for an arbitrary OTHER canonical-type comparison, nor does it say anything when BOTH A'
and B' are non-canonical** (A' ≠ A'_can and B' ≠ B'_can simultaneously) — in that case
part (i) only guarantees A' meets B'_can, a set possibly disjoint from the actual B'
under consideration, and part (ii) only guarantees B' meets A'_can, similarly not directly
about B'. This is exactly the honest scope claimed by the outline; I do not overclaim
this lemma resolves the general case.

### Step 4e — Round 3: F_A ∩ F_B ≠ ∅ (full proof, new certified content)

**Lemma.** For any two disjoint persistent base types A, B ∈ 𝒫 with canonical witnesses
m_A, m_B and extra-prime sets F_A := P(a_{m_A})\Q, F_B := P(a_{m_B})\Q, we have
F_A ∩ F_B ≠ ∅.

*Proof.* m_A ≠ m_B (distinct witnesses of distinct nonempty disjoint types A ≠ B, since if
m_A = m_B then τ(m_A) = A and τ(m_A) = B would force A = B, contradicting A ∩ B = ∅ and
A, B ≠ ∅). WLOG m_A < m_B (the argument is symmetric otherwise). By Free Fact 2 applied
with i = m_A < n = m_B, gcd(a_{m_A}, a_{m_B}) > 1, so there is a prime p dividing both.
Suppose p ∈ Q. Then p ∈ P(a_{m_A}) ∩ Q = τ(m_A) = A and p ∈ P(a_{m_B}) ∩ Q = τ(m_B) = B,
so p ∈ A ∩ B = ∅, a contradiction. Hence p ∉ Q, so p ∈ P(a_{m_A})\Q = F_A and
p ∈ P(a_{m_B})\Q = F_B, i.e. p ∈ F_A ∩ F_B. ∎

**Explicit scope limitation (must be stated, per the outline's caution).** This Lemma by
itself gives no new information beyond the Canonical-Refinement Lemma: since
A'_can = A ∪ F_A and B'_can = B ∪ F_B (Step 4d), F_A ∩ F_B ≠ ∅ literally says
A'_can ∩ B'_can ≠ ∅, which is already a special case (both sides canonical) of Step 4d's
Theorem. It says **nothing** about A' ∩ B' for a non-canonical A' or B' — in particular it
does NOT show that an arbitrary extended-persistent refinement of A contains any element
of F_B beyond what the General Reconciliation Lemma already gives (meeting F_B, not
containing all of it, and F_A ∩ F_B ≠ ∅ does not upgrade "meets F_B" to "meets F_A" for a
refinement of A that avoids the specific shared prime of F_A ∩ F_B). I record this
explicitly so this lemma is not mistaken for more than it is.

### Step 4f — Round 3: the localized residual gap, and the minimal-counterexample attack (attempted, does not close)

**Precise localization of (†) after Steps 4d–4e.** Combining Step 4d's Theorem with its
own converse reading: (†) — A' ∩ B' ≠ ∅ for every disjoint-base-type pair A', B' ∈ 𝒫' —
now needs to be checked ONLY for pairs where **both** A' ≠ A'_can and B' ≠ B'_can (both
non-canonical refinements of their respective disjoint base types). All other pairs (at
least one side canonical) are unconditionally settled by Step 4d. Define

  V := { (A', B') ∈ 𝒫' × 𝒫' : A := A'∩Q, B := B'∩Q ∈ 𝒫, A ∩ B = ∅, A' ∩ B' = ∅,
         A' ≠ A'_can, B' ≠ B'_can }

the (finite, since 𝒫' is finite) set of "residual violating pairs." (†) holds if and only
if V = ∅.

**Minimal-counterexample attempt (as directed by this round's dispatch).** Suppose, for
contradiction, V ≠ ∅. Since μ(A',B') := |A'| + |B'| takes values in the finite set
{2, 3, ..., 2|S₀|} (nonnegative integer sizes of subsets of the finite set S₀, at least 1
each since A', B' are nonempty — nonempty because A' ⊇ A ≠ ∅, B' ⊇ B ≠ ∅), and V is a
finite nonempty set, μ attains a minimum on V; fix (A'_0, B'_0) ∈ V with μ(A'_0, B'_0)
minimal among all elements of V.

Apply the Generalized Bounded Witness Lemma's Corollary (`generalized-bounded-witness-lemma.md`,
certified) to (A'_0, B'_0): since A'_0, B'_0 ∈ 𝒫' have disjoint base types and are
themselves S₀-disjoint (A'_0 ∩ B'_0 = ∅, since (A'_0,B'_0) ∈ V), the Corollary produces a
specific prime q ∉ S₀ such that q | a_n for infinitely many n with ρ(n) = A'_0. Restricting
to S₀^(1) := S₀ ∪ {q} and ρ_1(n) := P(a_n) ∩ S₀^(1), every one of these infinitely many n
satisfies ρ_1(n) = A'_0 ∪ {q} exactly (since S₀^(1) \ S₀ = {q} and q | a_n for these n), so
A'_0 ∪ {q} is itself S₀^(1)-persistent.

**Where the attempt genuinely stalls (documented honestly, not papered over).** I checked
both directions the outline proposed for turning this into a contradiction, and neither
goes through:

1. *Direct μ-decrease.* The natural candidate "smaller" pair would need to live in the
   SAME finite family 𝒫' × 𝒫' that μ was defined over (subsets of the fixed S₀). But the
   object produced, A'_0 ∪ {q}, is a subset of the STRICTLY LARGER set S₀^(1) = S₀ ∪ {q},
   not of S₀ — it is not even an element of 𝒫' (it lives one refinement-level down, in
   𝒫'_1, the S₀^(1)-persistent family). So there is no pair in 𝒫' × 𝒫' produced by this
   construction to compare against μ(A'_0, B'_0) at all: the size |A'_0 ∪ {q}| =
   |A'_0| + 1 is even LARGER than |A'_0|, so even if one tried to compare "one level down,"
   the natural measure goes up, not down — this is the same failure mode already
   catalogued in Step 4c's "monovariant candidates tried and why they did not work" for
   |𝒫'_k| (refinement only ever grows the ambient signature size; it never shrinks it).
   Minimality of (A'_0, B'_0) is therefore never contradicted by this route.

2. *Forcing q into B'_0 to get an outright intersection.* The witness m' used by the
   Corollary (any index with ρ(m') = B'_0) does satisfy q | a_{m'} (q ∈ F' :=
   P(a_{m'}) \ S₀ by the Corollary's own construction, and q is by definition a prime
   factor of a_{m'}), so THIS ONE occurrence of B'_0 does carry q: ρ_1(m') = B'_0 ∪ {q}.
   If this were true of *every* occurrence of B'_0 (i.e. if B'_0 ∪ {q} were itself
   S₀^(1)-persistent, matching the full infinite family B'_0 witnesses, not just this one
   instance), the two S₀^(1)-persistent types A'_0∪{q} and B'_0∪{q} would trivially
   intersect via q, and — if that intersection could be pulled back down to show
   A'_0 ∩ B'_0 ≠ ∅ directly, or at least that the ORIGINAL pair could not have been a
   genuine violation — this would close the gap. But I could not establish that
   B'_0 ∪ {q} is S₀^(1)-persistent: the Corollary only produces a SINGLE index m' at
   which B'_0 co-occurs with q; the infinitely many other occurrences of B'_0 (which are
   what make B'_0 itself persistent) could in principle each carry a DIFFERENT
   S₀^(1)\S₀-signature (recall Step 4d already showed, and the round-3 computational
   check below confirms, that a single base type can have many distinct extended
   refinements with no common prime forced across all of them beyond what the General
   Reconciliation Lemma already supplies) — there is no argument in hand that q recurs
   across infinitely many occurrences of B'_0 specifically (only that q recurs across
   infinitely many occurrences of A'_0, which is what the Corollary actually proves).
   This is precisely the obstruction Step 4c's round-2 catalogue flagged under
   "reconciled pairs stay reconciled... I was not able to show a single round's
   recruitment fully settles a whole base-type pair" — the same obstruction reappears
   here in the well-ordering framing, not just the forward-induction framing, confirming
   it is a structural feature of the problem's difficulty and not an artifact of either
   proof style.

**Conclusion: the minimal-counterexample attack, as set up by this round's dispatch, does
NOT close the residual gap.** Both of its two candidate contradiction routes fail for a
documented, specific reason (not merely "not yet tried"): route 1 fails because the
natural measure is monotonically non-decreasing under the only refinement operation
available (recruitment always adds a prime, never removes one, so any "smaller"
witnessing object is not comparable within the fixed ambient S₀); route 2 fails because
the Corollary's pigeonhole only certifies recurrence of q against the SIDE being
reconciled (A'_0), not against the fixed witness side (B'_0), and I have no argument
forcing the latter. This mirrors, and slightly sharpens, round 2's finding under a
different proof style, which the outline itself flagged as the value of trying: it shows
the well-ordering approach hits the identical wall as the forward-recruitment approach,
which is itself informative (it means the missing ingredient is not "which proof
technique," but a genuinely new fact — likely about how MULTIPLE disjoint occurrences of
the SAME base type interact, e.g. a joint/simultaneous pigeonhole across all of a base
type's infinitely many occurrences at once, rather than a single-witness argument — that
neither this round's nor round 2's mechanisms supply).

**Computational check, round 3 (extended scope, no violations found).** I re-ran the
Step 3–4 construction (S built from one canonical witness per persistent base type, S₀ =
Q ∪ S, 𝒫' computed from a long tail of the simulated sequence) and exhaustively checked
V for a_1 ∈ {35, 21, 33, 45, 77, 143, 55, 65, 91, 1155, 210, 105, 165, 231, 15015},
including two |Q| = 4 cases and one |Q| = 5 case (a_1 = 15015 = 3·5·7·11·13, 25 persistent
base types, 51 persistent extended types, |S₀| = 25). **Zero elements of V were found in
every one of these 15 seeds** — extending round 2's 10-seed check to |Q| = 5 and to
explicitly marking canonical vs. non-canonical refinements (round 2's check did not
distinguish canonical from non-canonical pairs; this round's check does, and every
disjoint-base-type pair checked intersects regardless of canonical status). I also
checked, for a_1 = 35 and a_1 = 1155, the full list of distinct S-part signatures realized
by each base type's extended-persistent refinements (data recorded for the next round):
for a_1 = 1155 every single refinement of every base type happens to contain the prime 2;
for a_1 = 35 this uniform-prime pattern does NOT hold (base type {5}'s refinements include
both {2}-containing and {3}-containing, but not both-simultaneously, signatures), yet
every disjoint pair still intersects — evidence that the true mechanism is NOT "a single
universal prime shared by all refinements of a type" (already refuted, Step 4b) but some
subtler, still-unidentified joint constraint across the WHOLE finite family 𝒫' at once,
consistent with route 2's diagnosis above. This is strong evidence (†) is TRUE, but
remains empirical, not a proof, across these seeds and finite windows.

**Honest status of (†) after this round.** (†) is now precisely localized to the residual
set V (pairs where both sides are non-canonical refinements); the Canonical-Refinement
Lemma and F_A∩F_B≠∅ lemma are fully proved, unconditional, promotable results that strictly
shrink the space of pairs requiring further argument (in every seed tested, ALL pairs are
in fact settled by Step 4d already — the non-canonical residual has never been observed
to be non-empty, i.e. every disjoint-base-type violation checked computationally involves
only canonical-vs-canonical or already-covered pairs). The minimal-counterexample attack
does not close V = ∅ in general; the obstruction is specific and documented (routes 1 and
2 above), not a vague "did not have time." This is genuine forward progress (narrower gap,
two new certified lemmas, a sharper diagnosis of exactly what extra fact is missing) but
(†) itself remains open.

### Step 6 — Round 4: the Persistent Uniform Core Lemma (PUCL) tested rigorously;
falsified in its literal form; and a structural proof that no rescue of it can close
the residual gap V

This round's dispatch asked me to attempt PUCL — a proposed fixed per-base-type
"hitting core" C_A, uniform across all of A's occurrences from the first one — as a
possible route to closing (†)/V, but explicitly warned that the outline's proposed
Corollary (Step 3 of the outline's PUCL skeleton, "C_A ∩ C_B ≠ ∅ ⟹ every pair of
extended-persistent refinements A', B' intersects") is already directly falsified by
the outline-reviewer and must not be built as an unconditional finish. I pursued
exactly this: I (a) tested PUCL's literal construction (C_A anchored at the type's
FIRST occurrence) computationally and found it FALSE in general, with a small,
completely hand-checkable counterexample; (b) isolated a trivial/generous form of
PUCL (C_A := S, the whole Finite Core Theorem pool) that IS true but adds no content
beyond what is already certified; (c) proved, with an exact minimal witness pair, WHY
the Corollary can never be rescued regardless of which valid choice of cores is used —
not merely re-citing the outline-reviewer's finding, but re-deriving it here from
scratch with the smallest possible witnesses and explaining the general mechanism
(Free Fact 2 guarantees a shared prime between ANY two terms, but gives no control
over whether that guaranteed shared prime lies inside or outside the fixed finite
pool S₀ — this "possible leakage outside S₀" is exactly, and only, what (†) is about,
and no purely disjunctive per-type covering statement can control it). All work below
is original computation and proof done this round, using the standard trial-division
factorization and the exact greedy rule of the problem statement.

**Setup for this section.** Take a_1 = 175 = 5²·7, so Q = {5,7}. Generating the
sequence by the problem's exact greedy rule (a_{n+1} := smallest integer > a_n with
gcd(a_{n+1},a_i) > 1 for every i ≤ n) gives, for the first six terms (independently
computed and checked by hand below):

  a_1=175=5·5·7,  a_2=180=2²·3²·5,  a_3=182=2·7·13,  a_4=189=3³·7,
  a_5=195=3·5·13,  a_6=210=2·3·5·7.

*Hand-check of a_2, a_3, a_4, a_5 (small enough to verify directly, not merely
trust a script).* a_2: every integer strictly between 175 and 180 must be checked
against gcd(·,175)>1, i.e. must share a factor with 5 or 7 — 176=2⁴·11 (no factor
5 or 7, gcd(176,175)=1, rejected), 177=3·59 (rejected), 178=2·89 (rejected),
179 prime (rejected); 180=2²·3²·5 has gcd(180,175)=5>1, and there is only one
earlier term (a_1) to check, so 180 is legal and is the first legal candidate — a_2=180.
✓. a_3: candidates 181 (prime, gcd with 175 and 180 both 1, rejected), 182=2·7·13:
gcd(182,175)=7>1, gcd(182,180)=2>1 — legal against both earlier terms, and no
smaller candidate worked, so a_3=182. ✓. a_4: 183=3·61 (gcd(183,175)=1, rejected),
184=2³·23 (gcd(184,175)=1, rejected), 185=5·37 (gcd(185,175)=5>1, but
gcd(185,180)=5>1, gcd(185,182)=1 — 182 has factors {2,7,13}, gcd(185,182)=1 since
185=5·37 shares none of {2,7,13} — rejected), 186=2·3·31 (gcd(186,182)=2>1,
gcd(186,180)=6>1, gcd(186,175)=1 — rejected, fails against a_1), 187=11·17
(gcd(187,175)=1, rejected), 188=2²·47 (gcd(188,175)=1, rejected), 189=3³·7:
gcd(189,175)=7>1, gcd(189,180)=9>1, gcd(189,182)=7>1 — legal against all three
earlier terms, so a_4=189. ✓ (I omit the fully identical style of check for a_5=195
and a_6=210 for space; both were independently verified by direct trial-division
script, matching this hand-computation for a_1..a_4 exactly, so I trust the script
for the remainder of this section.)

**Base types of these terms.** Q = {5,7}. τ(2)=P(180)∩Q={5}. τ(3)=P(182)∩Q={7}
(182 is not divisible by 5). τ(4)=P(189)∩Q={7} (189 is not divisible by 5).
τ(5)=P(195)∩Q={5,7}... wait: 195 = 3·5·13, is 195 divisible by 7? 195/7 is not an
integer, so τ(5) = {5} only, not {5,7}. (Corrected from an initial mis-scan — I
double-checked 195 = 3·5·13 exactly, 7∤195.) So a_3 and a_4 are consecutive
occurrences of the SAME base type {7} (a_3 is in fact the type's first occurrence,
since a_2 has type {5} and a_1 is excluded from the type indexing by convention —
τ is only defined for n≥2). a_5 has base type {5}.

**Step 6a — PUCL's literal construction is FALSE, witnessed at the very second
occurrence of a type.** The outline's PUCL, as stated, defines C_A by fixing it at
A's first occurrence: C_A := P(a_{n_A}) \ Q (intersected with S, but here we check
even without that intersection, i.e. the most generous literal reading). For base
type A = {7}, n_A = 3 (a_3 = 182 is the first occurrence of type {7}), giving
C_{7} := P(182) \ Q = {2,13}.

**Claim.** a_4 = 189, the very NEXT occurrence of type {7}, is divisible by neither
2 nor 13.

*Proof.* 189 = 3³·7 (verified directly above by hand: 189 = 27·7). P(189) = {3,7}.
{3,7} ∩ {2,13} = ∅. ∎

So the literal PUCL construction — "fix C_A at the type's first occurrence, then
every later occurrence of A is divisible by some element of C_A" — is **false**,
and fails already at the second occurrence, with no need to look deep into the tail
or invoke any density/growth argument. This is the exact same failure mode as the
already-retracted "Universal Glue Prime Lemma" (Step 4b), reproduced here at the
smaller, per-type scope PUCL was designed to fix — confirming the outline-reviewer's
warning ("if PUCL itself is false in general... retract immediately") applies to
the literal construction as written. I retract the literal PUCL construction; it
must not be built as stated in any future round.

**Step 6b — a generous, TRUE form of PUCL exists but adds no new content.** Define
instead C_A := S, the FULL Finite Core Theorem pool (Step 3 above), rather than a
type-specific small set. Then:

**Fact.** For n > N_1 (the Finite Core Theorem's threshold) with τ(n) = A, if A has
at least one disjoint persistent partner B ∈ 𝒫 (A∩B=∅), then a_n is divisible by
some element of S.

*Proof.* Immediate from the Finite Core Theorem (Step 3, certified): a_n is
divisible by some prime of F_{A,B} = P(a_{m_B})\Q ⊆ S. ∎

This is a completely true, "uniform core" statement (C_A = S works for every A with
a disjoint partner, from a single explicit threshold N_1 onward, not merely
"eventually" in an unspecified sense) — but it is **not new**: it is a direct,
one-line corollary of the already-certified Finite Core Theorem, stated in language
closer to PUCL's. It does not, by itself, buy anything beyond what Step 3 (Finite
Core Theorem) already gives; in particular it says nothing about which SPECIFIC
element of S a given occurrence realizes, which is exactly the missing information
Step 6c below shows is unavoidably needed.

**Step 6c — Theorem: PUCL's proposed Corollary (Step 3 of the outline's skeleton) is
false for the SAME reason regardless of which valid choice of cores is used, with an
exact minimal witness pair.** Take S₀ = {2,3,5,7,11} (Q ∪ S with S = {2,3} from the
usual Finite Core Theorem construction for this seed — 2,3 are the extra primes of
a_2=180 (witness for type {5}) and a_4... — I use S = {2,3}, matching the
outline-reviewer's independently verified computation for this exact seed). Define,
for n ≥ 1, ρ(n) := P(a_n) ∩ S₀.

Consider the two specific, already-computed terms:
  - n = 3: a_3 = 182 = 2·7·13, τ(3) = {7}, ρ(3) = P(182) ∩ S₀ = {2,7} (13 ∉ S₀).
  - n = 5: a_5 = 195 = 3·5·13, τ(5) = {5}, ρ(5) = P(195) ∩ S₀ = {3,5} (13 ∉ S₀).

**Fact 1.** τ(3) = {7} and τ(5) = {5} are disjoint (base types).

**Fact 2.** ρ(3) = {2,7} and ρ(5) = {3,5} are disjoint AS SUBSETS OF S₀: {2,7} ∩
{3,5} = ∅.

**Fact 3 (Free Fact 2 is still satisfied, as it must be — the guaranteed shared
prime just lies outside S₀).** By Free Fact 2 (certified, `free-facts-gcd.md`),
gcd(a_3, a_5) = gcd(182, 195) > 1 is REQUIRED. Direct computation: 182 = 2·7·13,
195 = 3·5·13, gcd(182,195) = 13 > 1. ✓ — consistent with Free Fact 2, but the
witnessing shared prime is 13, and 13 ∉ S₀.

**What this shows, precisely.** Both a_3 (type {7}) and a_5 (type {5}) individually
satisfy the "generous PUCL" disjunctive-hitting property of Step 6b with respect to
the SAME two-element candidate core {2,3} (2 ∈ {2,7} = ρ(3), and 3 ∈ {3,5} = ρ(5)),
and {2,3} ∩ {2,3} ≠ ∅ trivially (in fact C_{7} = C_{5} = {2,3} in the sense the
outline-reviewer numerically verified for this seed — I independently re-derived the
SAME finding for base types {5} and {7} individually below, Step 6d). **Yet the
actual extended types realized by THESE SPECIFIC terms, ρ(3) and ρ(5), are disjoint.**
This is not a defect of this particular pair of witnesses (a_3, a_5 could be replaced
by any other pair realizing the same phenomenon — I verified computationally, in the
setup script referenced below, that this pattern recurs: e.g. a_22 = 364 = 2²·7·13
again has ρ = {2,7}, and a_43 = 585 = 3²·5·13 again has ρ = {3,5}, again disjoint,
again with shared prime 13 outside S₀) — it is a structural fact about WHY the
Corollary cannot hold: each occurrence of a persistent type realizes only ONE (or
some proper subset) of the elements available in its disjunctive core, not
necessarily the same element every time and not necessarily the SAME element that a
disjoint-type occurrence it is being compared against also realizes. Free Fact 2
guarantees SOME shared prime always exists between a_3 and a_5 (13, in this
instance) — that is an absolute, unconditional fact about the sequence — but it
gives no control whatsoever over WHETHER that guaranteed shared prime happens to lie
inside the fixed finite pool S₀ or outside it. **This is exactly, and only, what
(†) is asking**, and no purely per-type disjunctive covering statement (PUCL, in any
of the forms above) can settle it, because disjunctive coverage is a statement about
each SIDE separately ("a_3 hits {2,3}", "a_5 hits {2,3}") and never pins down that
the two sides hit the SAME element of the shared core — which is precisely the
extra ingredient the Corollary silently assumes.

**Step 6d — independent re-verification of the "generous" per-type cores for this
seed, and a check of whether a single universal prime per type (a weaker rescue
attempt) survives.** Running the same trial-division script referenced by earlier
rounds (available on request; algorithm: greedy generation per the exact problem
statement, trial-division factorization, tabulated over the first 1600 terms), I
independently confirmed: base type {5} has ZERO occurrences, among 490 sampled in
this window, failing to be divisible by at least one of {2,3}; base type {7}
likewise has ZERO misses among 654 sampled occurrences for the SET {2,3} — matching
the outline-reviewer's finding and Step 6b's generous-PUCL fact (both {2,3} ⊆ S, so
this is consistent with, and a special case of, the trivial S-level fact, using a
strictly smaller-than-S set that happens to already suffice for these two base
types specifically in this seed). I then checked whether either type is covered by
a SINGLE universal prime (a stronger, "PUCL with |C_A|=1" rescue attempt, which
WOULD suffice to fix Step 6c's problem if it held for both sides of every disjoint
pair, since a shared single prime forces literal intersection): prime 3 alone
covers all 490 sampled occurrences of type {5} with zero misses, but for type {7},
prime 3 alone MISSES 47 of 654 occurrences and prime 2 alone misses 304 of 654 — so
type {7} has NO single-prime universal core in this window, only the two-element
core {2,3}. Since type {7} genuinely needs both elements of its core and does not
always use the same one (confirmed directly by a_3, a_4 above: a_3=182 uses 2 [and
not 3], while other type-{7} occurrences such as a_9... — omitted for space, full
list available in the referenced script output — use 3 and not 2), the
single-universal-prime rescue is also unavailable for this seed, for the same
reason Step 4b's global version was refuted in round 2.

**Conclusion of Step 6.** PUCL, tested rigorously in every form investigated this
round (literal first-occurrence-anchored, generous S-level, and single-prime-per-type),
either (i) is false as stated (Step 6a), (ii) is true but adds no content beyond the
already-certified Finite Core Theorem (Step 6b), or (iii) fails to rescue the
Corollary needed to close (†) for a documented structural reason with an exact
minimal witness pair (Step 6c, Step 6d). **PUCL alone is insufficient to close gap
(†).** This matches, and gives a from-scratch, independently-verified confirmation
of, the outline-reviewer's warning; it also sharpens WHY the corollary fails (not
merely "there exists a counterexample" but "the failure mode is that disjunctive
per-type coverage never controls WHICH element of the shared core a specific
occurrence realizes, and Free Fact 2's unconditionally-guaranteed shared prime
between any two terms can and does land outside S₀ for genuine, recurring instances,
not just isolated flukes"). Per the dispatch's own framing, gap (†) genuinely needs
the recruitment-process termination argument (Step 4c) on top of any PUCL-style
local statement — a purely local/disjunctive per-type argument, no matter how it is
phrased, cannot by itself supply the missing global, simultaneous-across-all-
occurrences ingredient that round 3's Step 4f already identified as the likely
correct target. I did not find that global argument this round; it remains the
single open item for gap (†), now with one more (and, I believe, conclusive) reason
to stop looking for it via local per-type cores and instead pursue the joint/
simultaneous mechanism flagged in Step 4f and the outline-reviewer's own
recommendation.

### Step 7 — Round 5: the Simultaneous Resolution Lemma, proved conditionally, plus an
unconditional Monotonicity Lemma

**Governing correction, independently reconfirmed.** Round 4's claim "V = ∅ always
(zero further recruitment rounds needed)" is FALSE — this round's outline-reviewer
independently reconfirmed math-explorer-singleton-hypothesis's four fresh
counterexamples (a_1 = 187, 209, 247, 385), each genuinely needing exactly one
recruitment round. This is settled and is not re-litigated here; the target reverts to
proving the recruitment PROCESS (defined in Step 4c above) terminates, and this
section's dispatch specifically asks for a **Simultaneous Resolution Lemma**: one
recruited prime resolves *every* currently-rogue pair at a round, not merely the one
witnessed pair.

**Setup for this section.** Fix any finite S₀ ⊇ Q (in practice S₀ = Q ∪ S from the
Finite Core Theorem, Step 3, though nothing below uses that specific construction).
Let ρ(n) := P(a_n) ∩ S₀, 𝒫' the (finite, nonempty) set of extended-persistent types.
For A' ∈ 𝒫', let n_{A'} := min{n : ρ(n) = A'} (exists, finite — the earliest
occurrence) and F'_{A'} := P(a_{n_{A'}}) \ S₀ (a fixed, finite, possibly-empty... in
fact nonempty exactly when A' has a rogue partner, shown below — set of primes outside
S₀ dividing A''s own earliest witness). Define
  V := {(A',B') ∈ 𝒫' × 𝒫' : A := A'∩Q, B := B'∩Q ∈ 𝒫, A∩B = ∅, A'∩B' = ∅}
the set of rogue (disjoint-base-type, S₀-disjoint) pairs — this is the process-level V
of Step 4c, not the round-3 residual restricted to non-canonical sides; the argument
below applies uniformly to all of V.

**Lemma (Monotonicity of Resolution) — new, fully proved, unconditional.** Let
S₀ ⊆ S₁ be finite sets of primes with Q ⊆ S₀, and let ρ, ρ₁ be the corresponding
extended-type maps. If A', B' ∈ 𝒫' (S₀-persistent) satisfy A' ∩ B' ≠ ∅, then every
pair of S₁-extended-persistent types A'', B'' with A'' ∩ S₀ = A' and B'' ∩ S₀ = B'
satisfies A'' ∩ B'' ≠ ∅ as well.

*Proof.* Since S₀ ⊆ S₁, for every n, ρ(n) = P(a_n) ∩ S₀ = (P(a_n) ∩ S₁) ∩ S₀ =
ρ₁(n) ∩ S₀. Hence A'' ∩ S₀ = A' means: for every n with ρ₁(n) = A'', we have
ρ(n) = ρ₁(n) ∩ S₀ = A'' ∩ S₀ = A'. Fix p ∈ A' ∩ B' (exists by hypothesis, p ∈ S₀ since
A', B' ⊆ S₀). Since A' = A'' ∩ S₀, p ∈ A' ⊆ A''; since B' = B'' ∩ S₀, p ∈ B' ⊆ B''.
So p ∈ A'' ∩ B'' ≠ ∅. ∎

*Why this matters.* It shows resolution, once achieved for a pair at some stage of the
recruitment process, is **permanent**: it cannot be undone by any later recruitment
round, no matter how S₀ grows further. This makes rigorous what round 2's Step 4c only
verified informally ("reconciled pairs stay reconciled... straightforward, included
for completeness") — it is stated and proved here as a standalone lemma because the
rest of this section leans on it explicitly.

**The Singleton Hypothesis (imported as an explicit, currently-open hypothesis, not
proved here).** For A' ∈ 𝒫', say A' is **singleton** (relative to S₀) if |F'_{A'}| = 1.
Say the **Universal Singleton Hypothesis** holds (for S₀, 𝒫') if every A' ∈ 𝒫' that has
at least one rogue partner (i.e. (A',B') ∈ V for some B') is singleton. This is
precisely a restatement, at the level of individual types rather than pairs, of the
Singleton Hypothesis studied by the sibling approach `greedy-exchange-cost-potential`:
for a rogue pair (A',B'), its F' (defined there via the witness on whichever side is
being reconciled) is literally F'_{A',B'} = P(a_{n_B}) \ S₀ = F'_{B'} — a set depending
only on B', not on the partner A' — so "the pair (A',B')'s F' is a singleton" is
identical to "B' is singleton" in the notation here. I do not re-derive the Singleton
Hypothesis in this file; it is owned by the sibling approach, and I import it here only
as an explicit hypothesis to build on, exactly as this round's dispatch instructs
("Fallback if Step 3 fails..." / "combine with covering-system-construction's process-
termination argument"). Every claim below that uses it says so explicitly.

**Theorem (Conditional Single-Pair Permanent Resolution).** Let (A',B') ∈ V be a rogue
pair, and suppose both A' and B' are singleton (F'_{A'} = {q_{A'}}, F'_{B'} = {q_{B'}}
for specific primes q_{A'}, q_{B'} ∉ S₀). Then q_{A'} = q_{B'} =: q, and setting
S₁ := S₀ ∪ {q}: A' ∪ {q} and B' ∪ {q} are both S₁-extended-persistent, and
(A' ∪ {q}) ∩ (B' ∪ {q}) ⊇ {q} ≠ ∅. By the Monotonicity Lemma, this specific pair — and
every further refinement of it at every later recruitment stage — is permanently
resolved.

*Proof.* By the certified Lemma G (Extended Earliest-Witness Intersection,
`lemmas/extended-earliest-witness-intersection.md`), applied to A', B' with their
earliest occurrences n_{A'}, n_{B'}: there is a prime q with q | a_{n_{A'}},
q | a_{n_{B'}}, q ∉ S₀. Since q | a_{n_{A'}} and q ∉ S₀, q ∈ P(a_{n_{A'}}) \ S₀ =
F'_{A'} = {q_{A'}} (singleton hypothesis on A'), so q = q_{A'}. Symmetrically,
q ∈ F'_{B'} = {q_{B'}}, so q = q_{B'}. Hence q_{A'} = q_{B'} = q.

Now apply the certified Generalized Bounded Witness Lemma
(`lemmas/generalized-bounded-witness-lemma.md`) with witness m := n_{B'} (so ρ(m) = B'):
for EVERY n > n_{B'} with ρ(n) = A', a_n is divisible by some prime of the fixed finite
set F'_{A',B'} := P(a_{n_{B'}}) \ S₀ = F'_{B'} = {q} (singleton, by the previous
paragraph — note this is the KEY use of singleton: the Lemma's conclusion "some prime
of a finite set" collapses to "the one prime q" when that finite set has exactly one
element, with no pigeonhole needed at all). Hence q | a_n for **every** n > n_{B'} with
ρ(n) = A' — not merely infinitely many via a pigeonhole extraction, but literally every
one of them. Since A' is extended-persistent, all but finitely many (namely those with
index ≤ n_{B'}) of its infinitely many occurrences satisfy n > n_{B'}, so infinitely
many n have ρ(n) = A' and q | a_n simultaneously; for each such n, ρ₁(n) = ρ(n) ∪ {q} =
A' ∪ {q} (since S₁ \ S₀ = {q} and q | a_n). Hence A' ∪ {q} occurs for infinitely many n,
i.e. is S₁-extended-persistent.

By the symmetric argument (Generalized Bounded Witness Lemma with witness m := n_{A'},
roles of A', B' swapped, using F'_{B',A'} := P(a_{n_{A'}}) \ S₀ = F'_{A'} = {q}),
B' ∪ {q} is likewise S₁-extended-persistent. Both contain q, so
(A' ∪ {q}) ∩ (B' ∪ {q}) ⊇ {q} ≠ ∅. The Monotonicity Lemma (applied with this S₀ ⊆ S₁,
A' ∩ B' replaced by q ∈ (A'∪{q}) ∩ (B'∪{q})) then gives permanence under every further
refinement. ∎

**This is the precise repair of round 3's "route 2" obstruction (Step 4f).** Round 3
documented exactly this failure: "the Corollary's pigeonhole only certifies the new
prime's recurrence on the side being reconciled, not the fixed witness side." The proof
above shows this obstruction disappears entirely once BOTH sides are singleton: the
Generalized Bounded Witness Lemma's conclusion is a "for every n" statement to begin
with, and pigeonhole (which is what discarded the witness-side information in round 3)
is only needed to extract a single recurring prime out of a set of size > 1 — with a
singleton set there is nothing to discard. Lemma G (certified since round 4, not
available to round 3's attempt) is what supplies the *shared* prime q_{A'} = q_{B'} in
the first place; without it, round 3 had no way to know the two sides' recruited primes
would coincide even under a one-sided singleton hypothesis.

**Theorem (Conditional Simultaneous Resolution).** Suppose the Universal Singleton
Hypothesis holds for S₀ and 𝒫' (every A' ∈ 𝒫' with a rogue partner is singleton). Let
R := {A' ∈ 𝒫' : (A',B') ∈ V for some B'} (finite, since 𝒫' is finite). Then the finite
set of primes Q_R := {q_{A'} : A' ∈ R} (well-defined, q_{A'} the unique element of
F'_{A'}) has size at most |R| ≤ |𝒫'|, and setting S₁ := S₀ ∪ Q_R (one finite
recruitment round, recruiting possibly several primes at once): **every** pair
(A',B') ∈ V is resolved simultaneously at S₁ — i.e. A' ∪ {q_{A'}} and B' ∪ {q_{B'}} are
both S₁-extended-persistent and intersect (in q_{A'} = q_{B'}) — and by the
Monotonicity Lemma this resolution of every pair in V is permanent.

*Proof.* Immediate from the Conditional Single-Pair Theorem applied to each
(A',B') ∈ V in turn: each application only requires S₁ ⊇ S₀ ∪ {q_{A'}, q_{B'}}, and
S₁ = S₀ ∪ Q_R ⊇ S₀ ∪ {q_{A'}, q_{B'}} for every (A',B') ∈ V since A', B' ∈ R (each has
a rogue partner, namely each other) and Q_R contains q_{A'} for every A' ∈ R. So every
pair's resolution goes through simultaneously within this single, one-step enlargement
S₀ → S₁. ∎

**Relation to the outline's exact dispatched target.** The outline asked for "one
recruited prime resolves ALL currently-rogue pairs, not just the one witnessed pair."
The theorem above proves a close but more careful version: **at most one prime per
connected component of the "has a rogue partner with" relation on R is needed, and
these primes coincide across every pair sharing a type** — because q_{A'} is defined
purely from A''s own witness a_{n_{A'}}, independent of which rogue partner is under
consideration, so if A' has several rogue partners B'_1, B'_2, ..., the SAME q_{A'}
resolves all of them simultaneously (the Theorem's proof of q_{A'} = q_{B'_i} for each i
individually already gives this, since q_{A'} does not depend on i). If, in addition,
the "rogue partner" relation graph on R is connected (every two types in R are linked
by a chain of rogue-partnerships), the Theorem's chain of equalities q_{A'_1} = q_{B'} =
q_{A'_2} = ... forces ALL of Q_R to collapse to a single prime, exactly matching the
outline's strongest form ("one recruited prime"). **I verified this connectivity holds,
and Q_R is a genuine singleton, in every one of the four fresh counterexample seeds**
(a_1 = 187: Q_R = {7}; a_1 = 209: Q_R = {7}; a_1 = 247: Q_R = {3}; a_1 = 385: Q_R = {19}
— recomputed independently this round with a fresh from-scratch script, matching the
outline's and outline-reviewer's reported values exactly). I do not have a general
proof that R's rogue-partner graph is always connected (this is a separate, so-far-
unexamined combinatorial question about V's structure, not attempted here in the time
available); without connectivity, the Theorem above still gives the slightly weaker but
still fully sufficient conclusion (a *bounded finite batch* of primes, one per
component, in one round) for the purpose of Step 6's finish below, since Step 6 only
needs S₀ to grow to a fixed finite S₁ within finitely many steps — a single round
recruiting a bounded finite set of primes is exactly as good as recruiting one prime for
that purpose.

**What remains open, precisely.** (1) The Universal Singleton Hypothesis itself is NOT
proved here — it is the sibling approach's target, and this section's theorems are
honestly conditional on it, exactly as instructed by this round's dispatch. (2) If the
Universal Singleton Hypothesis fails for some type A' ∈ R (|F'_{A'}| ≥ 2), the argument
above does not apply to A': the Generalized Bounded Witness Lemma's Corollary still
gives SOME recurring prime on A''s side via pigeonhole, but (exactly as round 3's
Step 4f documented) there is no guarantee this pigeonholed prime coincides with the one
forced on any specific rogue partner's side, and Lemma G only guarantees the shared
prime for a_{n_{A'}}, a_{n_{B'}} lies in F'_{A'} ∩ F'_{B'} — a set that could have more
than one element when singleton fails, leaving genuine ambiguity about which element is
"the" resolving prime for the whole persistent class rather than just the two specific
witness indices. This is the same wall as before, now localized exactly to the failure
locus of the Singleton Hypothesis, and it is the reason Status remains `partial`.
(3) The bounded-total-rounds fallback (this round's dispatch Step 5): if the Universal
Singleton Hypothesis fails at S₀, one can still ask whether finitely many further
rounds always suffice even without it. I attempted this and it reduces to the same
open question: the natural monovariant "number of base-type pairs not yet permanently
resolved" (finite, ≤ C(|𝒫|,2), by the Monotonicity Lemma) would give a bound on total
rounds PROVIDED each round permanently resolves at least one previously-unresolved
base-type pair in FULL (all its extended refinements, at every future stage, not merely
the one witnessed instance) — but proving this for a non-singleton type requires
exactly the same missing "joint pigeonhole across all of a base type's infinitely many
occurrences at once" ingredient flagged in round 2 (Step 4c) and round 3 (Step 4f); I
was not able to supply it this round, and record this explicitly as the fallback's
open gap rather than assume it away.

**Given the Conditional Simultaneous Resolution Theorem, Step 6's finish (below)
applies unchanged** with S₀ replaced by the finite S₁ = S₀ ∪ Q_R it produces (or, if the
Universal Singleton Hypothesis fails, with whatever finite S₀^(final) the — currently
unproved — general termination of the recruitment process would produce).

### Step 8 — Round 6: the Projection Lemma, the unconditional Collateral-Safety
Theorem, and the reduction of the whole remaining gap to the sibling approach's
Full-Absorption Hypothesis

**Governing correction, again, stated up front so it cannot be missed.** This round's
math-explorers and outline-reviewer independently reconfirmed (from scratch, with a
fresh implementation) that the Universal Singleton Hypothesis used in round 5's
Conditional theorems is FALSE in general: a_1 = 4807 gives a rogue pair with
F' = {13,17} (|F'| = 2), a_1 = 11305 gives F' = {11,103} (|F'| = 2). **Nothing in this
section uses |F'| = 1 anywhere.** Round 5's Conditional Single-Pair/Simultaneous
Resolution Theorems remain exactly as conditional as stated there (on the now-false
Universal Singleton Hypothesis) and are not re-derived or re-used below; Step 8 is
entirely independent of them.

#### Step 8.1 — the Projection Lemma (new, fully proved, unconditional)

**Setup.** Throughout, S₀, S₁ range over finite sets of primes with Q ⊆ S₀ ⊆ S₁ (Q is
always contained in every S₀ we ever consider, by construction — S₀ = Q ∪ S in the
Finite Core Theorem, and every later enlargement only adds primes, never removes Q).
Write ρ(n) := P(a_n) ∩ S₀ and ρ₁(n) := P(a_n) ∩ S₁.

**Lemma (Projection).** Suppose A'' ⊆ S₁ is S₁-extended-persistent (i.e. ρ₁(n) = A''
for infinitely many n). Then:
  (i) A' := A'' ∩ S₀ is S₀-extended-persistent;
  (ii) A' ∩ Q = A'' ∩ Q (the base type is unchanged by projection).

*Proof.* Since S₀ ⊆ S₁, for every index n, ρ(n) = P(a_n) ∩ S₀ = (P(a_n) ∩ S₁) ∩ S₀ =
ρ₁(n) ∩ S₀ — this is a pure set-theoretic identity, using only S₀ ⊆ S₁ (∩ distributes:
if S₀ ⊆ S₁ then for any set X, X ∩ S₀ = (X ∩ S₁) ∩ S₀). Now fix any n with ρ₁(n) = A''.
Then ρ(n) = ρ₁(n) ∩ S₀ = A'' ∩ S₀ = A' — the SAME fixed set A' for every such n (A' does
not depend on n; it is defined once, from A'' and S₀ alone). Since A'' is
S₁-extended-persistent, there are infinitely many n with ρ₁(n) = A'', and every one of
these has ρ(n) = A'; hence there are infinitely many n with ρ(n) = A', i.e. A' is
S₀-extended-persistent. This proves (i).

For (ii): A' ∩ Q = (A'' ∩ S₀) ∩ Q = A'' ∩ (S₀ ∩ Q). Since Q ⊆ S₀, S₀ ∩ Q = Q. So
A' ∩ Q = A'' ∩ Q. ∎

**Remark.** This is the identical one-line mechanism already used, without being
isolated as a standalone statement, inside the certified Monotonicity of Resolution
Lemma's proof (`lemmas/monotonicity-of-resolution.md`: "ρ(n) = ρ₁(n) ∩ S₀ for all n")
and inside Step 4's base-type-invariance remark ("every index n with ρ(n) = A' has
τ(n) = A' ∩ Q = A"). Step 8.1 is not a new proof technique — it is the same pigeonhole/
restriction mechanism as the certified Persistent-Type Pigeonhole family, isolated here
as its own citable lemma because Step 8.2 below needs it applied in the "downward"
direction (S₁-persistent ⟹ S₀-persistent), the opposite direction from how
Monotonicity uses it (S₀-persistent ⟹ some S₁-refinement persistent), so the two
lemmas are logically independent restatements of the same identity ρ(n) = ρ₁(n) ∩ S₀,
not one subsuming the other.

**Recommended for certification** (no gap, ≤1 page, exactly as this round's outliner
and outline-reviewer both anticipated).

#### Step 8.2 — the Collateral-Safety Theorem (new, fully proved, unconditional)

**Definition (fully safe).** Let A, B ∈ 𝒫 be disjoint persistent base types. Say the
pair (A,B) is **fully safe at S₀** if every pair of S₀-extended-persistent types A',B'
with A' ∩ Q = A, B' ∩ Q = B satisfies A' ∩ B' ≠ ∅. (Equivalently: (A,B) has no rogue
extended-persistent refinement pair at S₀, in the terminology of Step 4c/Step 7's set
V — "(A,B) fully safe at S₀" means no pair (A',B') with these base types lies in V at
level S₀.)

**Theorem (Collateral-Safety).** If (A,B) is fully safe at S₀, then (A,B) is fully safe
at every S₁ ⊇ S₀ (S₁ finite, Q ⊆ S₀ ⊆ S₁).

*Proof.* Let A'', B'' be any pair of S₁-extended-persistent types with A'' ∩ Q = A,
B'' ∩ Q = B. By the Projection Lemma (Step 8.1) applied to A'': A' := A'' ∩ S₀ is
S₀-extended-persistent, with A' ∩ Q = A'' ∩ Q = A. Likewise B' := B'' ∩ S₀ is
S₀-extended-persistent with B' ∩ Q = B. Since (A,B) is fully safe at S₀ (hypothesis)
and A', B' are exactly a pair of S₀-extended-persistent refinements of A, B, we get
A' ∩ B' ≠ ∅.

Now apply the certified Monotonicity of Resolution Lemma (`lemmas/monotonicity-of-
resolution.md`) to A', B' (S₀-extended-persistent, A' ∩ B' ≠ ∅ just shown) and to A'',
B'' (S₁-extended-persistent, with A'' ∩ S₀ = A' and B'' ∩ S₀ = B' — this is literally
the definition of A', B' just given, so the Lemma's hypothesis "A'' ∩ S₀ = A', B'' ∩ S₀
= B'" is satisfied by construction, not merely plausible): the Lemma concludes
A'' ∩ B'' ≠ ∅.

Since A'', B'' were an arbitrary pair of S₁-extended-persistent refinements of A, B,
(A,B) is fully safe at S₁. ∎

**This closes round 5's "collateral rogue pairs" gap completely and unconditionally.**
No hypothesis beyond Q ⊆ S₀ ⊆ S₁ (always true in this framework) and the two lemmas
combined (Projection, certified here; Monotonicity, already certified round 5) is
used. In particular this holds regardless of whether the Universal Singleton
Hypothesis, the Full-Absorption Hypothesis, or any other unproved hypothesis is true —
it is a structural fact about the recruitment process itself.

**Corollary (base-type pairs are fixed forever).** Since Q = P(a_1) never changes
(fixed from the problem's very first term) and 𝒫, the set of persistent BASE types, is
defined purely at the Q-level (Step 1), 𝒫 and the finite list of disjoint base-type
pairs {(A,B) : A,B ∈ 𝒫, A∩B=∅} — of which there are at most C(|𝒫|,2) ≤ C(2^k−1, 2) —
are fixed once and for all at round 0 of the recruitment process (Step 4c). Refinement
(enlarging S₀) only ever changes which EXTENDED refinements A',B' of a fixed base pair
(A,B) exist and whether they intersect; it never creates or destroys a base-type pair.
This is immediate from Step 1's definition of 𝒫 (a subset of 2^Q \ {∅}, and Q is fixed)
and needs no further proof.

#### Step 8.3 — the reduction: base-type-pair-level termination is the entire
remaining content of gap (†)

Recall the recruitment process of Step 4c: S₀^(0) := Q ∪ S (Finite Core Theorem), and
at stage k, if some rogue extended-persistent pair exists (disjoint base types A,B ∈ 𝒫
with S₀^(k)-extended-persistent refinements A',B', A'∩B'=∅), a new prime is recruited
(via the Generalized Bounded Witness Lemma's Corollary) to form S₀^(k+1).

Define, for each stage k, open(k) := {(A,B) : A,B ∈ 𝒫 disjoint, (A,B) is NOT fully
safe at S₀^(k)} ⊆ the fixed finite list of base-type pairs from Step 8.2's Corollary.

**Proposition (monotone shrinking).** open(k+1) ⊆ open(k) for every k.

*Proof.* Contrapositive of the Collateral-Safety Theorem: if (A,B) ∉ open(k), i.e.
(A,B) is fully safe at S₀^(k), then by Collateral-Safety it is fully safe at
S₀^(k+1) ⊇ S₀^(k), i.e. (A,B) ∉ open(k+1). ∎

So (open(k))_{k≥0} is a non-increasing sequence of subsets of a FIXED finite set (of
size ≤ C(|𝒫|,2), independent of k, by Step 8.2's Corollary). Consequently:

**Proposition (termination criterion).** The recruitment process reaches open(k*) = ∅
for some finite k* — and hence Step 5's CRT + cyclic-pigeonhole finish applies verbatim
at S₀^(k*), completing the whole problem — **if and only if** every round of the
process that recruits against some currently-open pair strictly removes at least one
pair from open(·) within a bounded number of further rounds (equivalently: no base-type
pair remains in open(k) for all k, i.e. no base-type pair requires infinitely many
distinct recruitment rounds before becoming fully safe).

*Proof.* If every open pair is eventually removed within a bounded number of rounds,
then since open(k) is non-increasing and starts with ≤ C(|𝒫|,2) elements, after at most
C(|𝒫|,2) "successful" rounds (each removing ≥1 pair, by hypothesis) open(k) = ∅; more
precisely, if each pair (A,B) ∈ open(0) is removed by some finite round r_{A,B}, then
at k* := max_{(A,B)∈open(0)} r_{A,B} (a finite max over a finite set), open(k*) = ∅ by
monotonicity. Conversely, if open(k) = ∅ for some finite k*, every pair is trivially
removed by round k* (a degenerate case of "bounded"). ∎

**This is an exact, honest restatement of the residual gap: it is now located entirely
at the level of the ≤ C(|𝒫|,2) fixed base-type pairs, not at the level of an
unboundedly-growing family of extended-type refinements.** This is a strictly sharper
localization than round 5 achieved (round 5 worked at the extended-type level, where
the number of currently-rogue extended pairs is not obviously bounded independent of k,
since 𝒫'_k can grow with k). Whether every base-type pair is in fact removed in finitely
many rounds is precisely the question of "full absorption" — does recruiting a prime
against one witnessed rogue extended instance in fact make the WHOLE base-type pair
fully safe (removing it from open(·) permanently, by Step 8.2's Corollary), rather than
merely resolving that one witnessed instance while other extended refinements of the
same base pair remain unreconciled? This is exactly the sibling approach
`greedy-exchange-cost-potential`'s Full-Absorption Hypothesis (FAH) target. I import it
as a black box below and show precisely what it buys.

#### Step 8.4 — importing FAH: precise statement as used here

I use the sibling approach's FAH (owned by `greedy-exchange-cost-potential`, NOT proved
in this file) in the following precise form, matching this round's outliner/
outline-reviewer specification, together with an explicit **symmetric strengthening**
flagged honestly as an additional needed ingredient (see the caveat at the end of this
subsection):

**FAH (as defined by the sibling approach; imported, not proved here).** Fix a rogue
pair of S₀-extended-persistent types A', B' with disjoint base types, and, by the
certified Lemma G (`lemmas/extended-earliest-witness-intersection.md`), let
n_A := min{n : ρ(n)=A'}, n_B := min{n : ρ(n)=B'} (WLOG n_A < n_B), and let q ∉ S₀ be a
prime with q | a_{n_A}, q | a_{n_B} (Lemma G guarantees existence of such q). FAH
asserts: q | a_n for **every** n > n_B with ρ(n) = A' (not merely infinitely many).

**Symmetric FAH (the strengthening I need for the argument below; flagged as an
additional gap, NOT established by the sibling approach as literally stated — see Step
8.6).** The same conclusion with the roles of A', B' exchanged: q | a_n for every
n > n_A with ρ(n) = B'. (Lemma G's construction is itself already symmetric in A', B'
— it produces a single prime q dividing BOTH a_{n_A} and a_{n_B} — so it is natural to
conjecture FAH holds symmetrically too, and the outliner's Step 2 proof sketch for FAH
does not obviously favor one side over the other; but the sibling approach's file, as I
have read it, states and targets only the one-sided form. I do not assume the symmetric
form is already proved — I mark it explicitly as imported alongside FAH, an additional,
not-yet-established half of the hypothesis needed for Step 8.5.)

#### Step 8.5 — the rigorous implication: FAH-symmetric (for every currently-rogue
extended pair) ⟹ base-type-pair-level termination in one further round

**Theorem (conditional, on Symmetric FAH).** Fix a stage S₀ = S₀^(k) of the recruitment
process, and suppose Symmetric FAH holds for every rogue extended-persistent pair at
this stage (there are finitely many such pairs, since 𝒫'_k, the set of
S₀-extended-persistent types, is finite by the same pigeonhole argument as Step 1/4).
Let {(A'_i, B'_i)}_{i=1}^{r} enumerate all rogue pairs at stage S₀ (finite list, r ≥ 0;
if r = 0 then open(k) is already empty and there is nothing to prove), with associated
Lemma-G primes q_1, ..., q_r (not necessarily distinct) given by Symmetric FAH applied
to each. Set S₁ := S₀ ∪ {q_1, ..., q_r} (one finite recruitment round). Then every
base-type pair (A,B) that is open at stage k is fully safe at S₁, hence open(k') = ∅ at
k' := (the stage reached after this one round), i.e. the recruitment process terminates
in exactly one further round from stage k.

*Proof.* Fix an open base-type pair (A,B) at stage k. I must show every pair of
S₁-extended-persistent refinements A'', B'' with A''∩Q = A, B''∩Q = B satisfies
A''∩B''≠∅.

By the Projection Lemma (Step 8.1), A' := A''∩S₀ is S₀-extended-persistent with
A'∩Q = A, and B' := B''∩S₀ is S₀-extended-persistent with B'∩Q = B.

*Case 1: (A',B') is NOT a rogue pair at S₀, i.e. A'∩B'≠∅ already.* Then by the
Monotonicity of Resolution Lemma (applied with S₀ ⊆ S₁, A''∩S₀=A', B''∩S₀=B'),
A''∩B''≠∅ directly.

*Case 2: (A',B') IS one of the enumerated rogue pairs, say (A'_i,B'_i), with Lemma-G
prime q_i ∈ S₁.* By Symmetric FAH applied to (A'_i,B'_i): q_i | a_n for every
n > n_{B_i} with ρ(n) = A'_i, AND q_i | a_n for every n > n_{A_i} with ρ(n) = B'_i.

Consider A''. Every n with ρ₁(n) = A'' has, by the Projection Lemma's proof mechanism
(ρ(n) = ρ₁(n)∩S₀ = A''∩S₀ = A' = A'_i), ρ(n) = A'_i. Since A'' is S₁-extended-
persistent, there are infinitely many such n, so in particular infinitely many with
n > n_{B_i} (only finitely many indices are ≤ n_{B_i}). For every such n (n > n_{B_i}
and ρ(n)=A'_i), Symmetric FAH gives q_i | a_n; since q_i ∈ S₁, q_i ∈ P(a_n)∩S₁ = ρ₁(n)
= A''. This holds for every one of these infinitely many n, and A'' is a FIXED set (the
same for all n with ρ₁(n)=A''), so q_i ∈ A''.

By the identical argument applied to B'' (using Symmetric FAH's B'-side conclusion,
q_i | a_n for every n > n_{A_i} with ρ(n)=B'_i), q_i ∈ B''.

Hence q_i ∈ A''∩B'', so A''∩B'' ≠ ∅.

Since A', B' must fall into Case 1 or Case 2 (every S₀-extended-persistent refinement
pair of a base pair either is or is not one of the finitely many enumerated rogue
pairs, by definition of the enumeration as ALL rogue pairs at stage k), every pair
A'',B'' of S₁-refinements of (A,B) satisfies A''∩B''≠∅, so (A,B) is fully safe at S₁.

Since (A,B) was an arbitrary open pair at stage k, and the already-safe pairs remain
safe at S₁ by Collateral-Safety (Step 8.2) regardless, EVERY base-type pair is fully
safe at S₁, i.e. open(k') = ∅ where S₀^(k') := S₁. ∎

**Corollary (finish).** Under the hypothesis of the Theorem (Symmetric FAH for every
rogue extended pair at the current stage — in particular, if Symmetric FAH holds
universally, this applies already at stage 0, i.e. S₀ = Q∪S from the Finite Core
Theorem), the recruitment process terminates after exactly one further round, at
S₀^(final) = S₀ ∪ {q_1,...,q_r}, a finite, explicitly describable set. Step 5's CRT +
cyclic-pigeonhole finish then applies verbatim at S₀^(final), completing the proof of
the whole problem (existence of T, L with a_{n+T} = a_n + L for all n).

**Why this is a strictly rigorous implication, not a restatement of the hope.** Every
step above either (a) cites an already-certified unconditional lemma (Projection,
Monotonicity, Lemma G, Generalized Bounded Witness — for the rogue-pair enumeration
being finite), or (b) is a direct, checked deduction from the imported hypothesis
(Symmetric FAH) with no additional unstated assumption. In particular, note precisely
WHERE Symmetric FAH is used and why the one-sided form alone (as literally stated by
the sibling approach) does not suffice for Case 2 above: the one-sided FAH only forces
q_i ∈ A'' (from the A'-side "every occurrence" claim); to get q_i ∈ B'' as well
(needed for A''∩B''≠∅) the argument needs the SAME "every occurrence, not just
infinitely many" strength on B''s side too — a single witnessed co-occurrence (which
Lemma G alone gives, with no help from one-sided FAH) is not enough, because B'' could
in principle be witnessed by indices n > n_{A_i} with ρ(n) = B'_i where q_i fails to
divide a_n, if only "infinitely many, not all" B'_i-occurrences carried q_i — exactly
the "route 2" obstruction round 3 (Step 4f) and round 5 (Step 7) already identified as
the crux difficulty of the one-sided pigeonhole mechanism.

#### Step 8.6 — honest accounting of what remains open after this round

**Closed unconditionally this round (Step 8.1–8.3):**
- The Projection Lemma (Step 8.1) — complete, no gap.
- The Collateral-Safety Theorem (Step 8.2) — complete, no gap, and its Corollary
  (base-type pairs fixed forever) — complete, no gap.
- The exact reduction of gap (†) to base-type-pair-level termination (Step 8.3,
  "open(k) monotone, terminates iff every pair eventually leaves open(·)") — complete,
  no gap; this is a genuine sharpening of round 5's extended-type-level framing to a
  FIXED finite index set of pairs.

**Left open, explicitly, as imported black-box gaps (NOT proved in this file):**
1. **FAH itself** (one-sided, as stated by `greedy-exchange-cost-potential`) — owned
   and targeted by that approach; not attempted here.
2. **Symmetric FAH** (the two-sided strengthening Step 8.5's proof actually needs) —
   this is a genuinely separate, slightly stronger claim than the sibling approach's
   literal one-sided statement, flagged here for the first time as a precise
   requirement. I have NOT verified it computationally or attempted a proof of it in
   this file; a future round (either this approach or the sibling one) should either
   (a) prove Symmetric FAH directly — plausible, since Lemma G's construction is
   already symmetric in A', B', so the same joint-pigeonhole mechanism the sibling
   approach's Step 2 sketch proposes for the A'-side has no evident reason to fail on
   the B'-side — or (b) find a different route to Case 2 of Step 8.5's proof that only
   needs the one-sided form (e.g. by choosing the enumeration of rogue pairs so that
   the "witness side" is always the side needing the weaker one-sided property,
   though I do not see how to remove the need for the OTHER side's strength this way,
   since both A'' and B'' need q_i for the intersection — this is worth a dedicated
   attempt next round, not assumed solvable here).
3. Whether the enumerated set of rogue pairs at stage 0 (S₀ = Q∪S, Finite Core
   Theorem) already accounts for ALL rogue pairs that could ever arise, or whether
   Step 8.5's Theorem needs to be applied iteratively at several stages (if, e.g.,
   recruiting {q_1,...,q_r} at stage 0 were to somehow re-open a previously-safe pair)
   — this does NOT actually happen, by Collateral-Safety (Step 8.2) applied to the
   already-safe pairs directly, so Step 8.5's one-round argument is genuinely
   sufficient once Symmetric FAH holds at stage 0; I flag this only to record that I
   checked it, not because it is unresolved.

**What this round's result buys, precisely, stated without overclaiming.** Given (1)
and (2) above (both currently open, owned partly by the sibling approach and partly
newly identified here), the whole problem is solved by Step 8.5's Corollary + Step 5's
finish. Without them, the process is known (Step 8.3) to be governed by a monotone
non-increasing sequence over a FIXED finite index set of size ≤ C(|𝒫|,2) — a strictly
better-understood object than round 5's unbounded-looking extended-type-level picture
— but termination itself is not yet established unconditionally. Status remains
`partial`; the collateral-safety half of round 5's gap is now closed for good, and the
remaining half is precisely pinned to FAH (and its symmetric strengthening), not to any
defect in the recruitment/CRT machinery, which (Steps 1–8.3) is now fully unconditional
up to that one imported hypothesis.

#### Step 8.7 — round 7: decoupling the Step 8.5 finish from the sibling's "Two-Witness
Intersection Uniqueness" target, via a canonical choice of witness prime

This round's outliner dispatched the sibling approach `greedy-exchange-cost-potential`
to attempt **Two-Witness Intersection Uniqueness** (|F' ∩ F''| = 1, where
F' := P(a_{n_B})\S₀, F'' := P(a_{n_A})\S₀) as a stepping stone toward FAH/Symmetric FAH,
and asked this file to mirror the sibling's mechanism onto the B'-side. Before doing so
I first check, rigorously, whether my Step 8.5 argument actually *needs* uniqueness at
all — this was left implicit in Step 8.4's statement and is worth pinning down exactly,
independently of whatever the sibling's round-7 build produces (the outline-reviewer
flagged Two-Witness Uniqueness as at serious risk of being a repackaged instance of the
already-dead "Lemma H branch analysis" mechanism — see `/tmp/round-7/outline-reviewer.md`
§1 — so I do not want this file's progress to be contingent on that specific claim if it
can honestly be avoided).

**Claim: Step 8.5's Theorem, exactly as proved above, only requires — for each rogue pair
(A'_i,B'_i) — the existence of ONE prime q_i ∈ F'_i ∩ F''_i for which BOTH the A'-side
full-absorption property (FAH) and the B'-side full-absorption property (Symmetric FAH)
hold; it never uses that q_i is the unique element of F'_i ∩ F''_i.**

*Verification.* Re-reading the proof of Case 2 in Step 8.5: the argument fixes a single
prime q_i (produced, abstractly, "by Symmetric FAH applied to (A'_i,B'_i)") and shows
q_i ∈ A'' using the A'-side full-absorption conclusion for q_i, then q_i ∈ B'' using the
B'-side full-absorption conclusion for THE SAME q_i, concluding q_i ∈ A''∩B''. At no
point does the proof invoke that q_i is the only prime in F'_i∩F''_i, or compare it to
any other candidate prime. Hence the claim is verified by direct inspection: what Step
8.5 needs is exactly the *joint* existential statement "∃ q ∈ F'∩F'' such that q
full-absorbs BOTH sides" — call this **Joint FAH** — not "|F'∩F''| = 1" and not two
*separately*-quantified existentials "∃q₁ full-absorbing A'-side" and "∃q₂ full-absorbing
B'-side" (which, if q₁ ≠ q₂, would NOT suffice for Case 2: q_i ∈ A''∩B'' genuinely needs
the same prime on both sides). This is a real subtlety worth flagging explicitly, since
the sibling approach's FAH statement (Step 8.4, "let q ∉ S₀ be A prime with q|a_{n_A},
q|a_{n_B}... FAH asserts q|a_n for every n>n_B with ρ(n)=A'") is itself only about *some*
q produced by Lemma G, not a canonically fixed one — so "FAH holds" and "Symmetric FAH
holds" as bare existential statements do not automatically combine into Joint FAH unless
the same q witnesses both.

**Fix: canonicalize the witness prime, making "same q" automatic by definition rather
than by proving uniqueness.** Define, for each rogue pair (A'_i,B'_i) with n_A<n_B,
**q*_i := min(F'_i ∩ F''_i)** (well-defined: F'_i∩F''_i is a finite, nonempty set of
primes by the certified Lemma G, so it has a unique minimum). Restate FAH and Symmetric
FAH, for the purposes of this file's Step 8.5, as being specifically about this
canonically chosen q*_i (not an arbitrary or existentially-quantified element of
F'_i∩F''_i):

- **FAH (canonical form).** q*_i | a_n for every n > n_{B_i} with ρ(n) = A'_i.
- **Symmetric FAH (canonical form).** q*_i | a_n for every n > n_{A_i} with ρ(n) = B'_i.

If BOTH of these (about the literal same prime q*_i by construction) are proved, Joint
FAH holds trivially for q_i := q*_i, and Step 8.5 goes through exactly as written with no
further work. **This removes any dependency on Two-Witness Intersection Uniqueness**:
proving |F'_i∩F''_i| = 1 would have been one (sufficient, not necessary) way to force
"same q on both sides" for granted, but canonicalizing the choice (taking the minimum)
achieves the same effect for free, by fiat, regardless of whether |F'_i∩F''_i| is 1 or
larger. I record this as a genuine simplification of what this round's build actually
needs: **the sibling approach's Two-Witness Intersection Uniqueness target, even if it
stalls (as the outline-reviewer judges likely), does not block this file's finish** —
what remains needed is FAH and Symmetric FAH specifically for the prime q*_i :=
min(F'_i∩F''_i), which is exactly the "arbitrary/fixed q ∈ F'∩F''" fallback version the
outline-reviewer already flagged as buildable independent of uniqueness (§1 of
`/tmp/round-7/outline-reviewer.md`, "the builder should note whether step 4's argument
can proceed with an ARBITRARY q ∈ F'∩F''"). I take q*_i as that fixed choice.

**Honest caveat.** This is a bookkeeping simplification, not a proof of FAH or Symmetric
FAH themselves — the "Blocking-Data Bridging Lemma" (the actual proof mechanism for
either canonical-form statement above) remains open, owned in its A'-side form by the
sibling approach and unattempted in this file beyond the symmetry check below (Step 8.8).
What this step buys is precise and narrow: it shows the two open targets (FAH,
Symmetric FAH) can be stated about the SAME, canonically-defined prime with zero extra
proof burden, so a future round proving Blocking-Data Bridging for the canonical q*_i on
the A'-side and (by the mirror argument of Step 8.8) on the B'-side closes Step 8.5
completely, without any separate uniqueness lemma.

#### Step 8.8 — round 7: checking the one place symmetry could break in the mirrored
Blocking-Data Bridging mechanism

Per this round's outliner dispatch, I check explicitly whether the sibling's proposed
Blocking-Data Bridging mechanism (outline, `greedy-exchange-cost-potential` revise,
step 4) transfers to the B'-side (Symmetric FAH, canonical form) without modification, or
whether it hits a genuine asymmetric obstruction.

**The mechanism, as proposed (A'-side).** For a hypothetical n > n_B with ρ(n) = A' and
q*∉P(a_n) (i.e. q* fails to divide a_n), consider the smallest multiple of q* exceeding
a_{n-1} that is also legal against a_1,...,a_{n-1}; if such a legal multiple c < a_n
exists, greedy minimality of a_n is directly violated (contradiction, ruling out this
case); if no such legal multiple below a_n exists, every q*-multiple in (a_{n-1},a_n) is
blocked by some specific earlier index, and these blocking indices/factorizations are to
be analyzed via the Finite Core Theorem's explicit construction to derive a contradiction
with the pigeonhole recurrence of q* on D(n) (Divisor-Restricted Pigeonhole, Step 3 of
the sibling's outline).

**Symmetry check.** This entire mechanism, as stated, is about a SINGLE fixed index n
(here an A'-occurrence) and its OWN predecessors a_1,...,a_{n-1} and its OWN greedy
minimality defining equation. Nowhere does the argument reference n_B specifically, or
any minimality property of n_B as the *earliest* B-occurrence — it only uses (i) that n
is large enough that a_{n-1}, a_n, ..., a_1 are already-existing terms of the sequence
(true for any n > n_B, in particular), and (ii) the Finite Core Theorem's construction of
S₀ (which is symmetric in A', B' — S₀ is a single fixed finite set built once, not
separately per side). Applying the identical argument with "A'-occurrence n > n_B" replaced
by "B'-occurrence m > n_A" (equivalently, since every B'-occurrence already satisfies
m ≥ n_B > n_A, replaced by "B'-occurrence m > n_B", the same cutoff as the A'-side,
per the reformulation below) uses exactly the same two facts (i)-(ii), now with the
roles of a_1,...,a_{m-1} and D'(m) := P(a_m)∩F'' playing the roles of a_1,...,a_{n-1}
and D(n) := P(a_n)∩F'. Since q* ∈ F'∩F'' by construction (Step 8.7), the pigeonhole step
(Divisor-Restricted Pigeonhole) is available verbatim on the B'-side using F'' in place
of F'. **I find no structural obstruction distinguishing the two sides**: the mechanism's
only load-bearing external input is the Finite Core Theorem's finished, side-agnostic S₀,
not any property specific to n_B's status as B's earliest occurrence. This is different
from — and does not resurrect — the genuinely-flagged risk in the SIBLING approach's
step 2 (Two-Witness Intersection Uniqueness), which explicitly DOES use n_B's own
minimality (the joint-Lemma-H argument the outline-reviewer criticized); Step 8.7 above
shows my finish does not need that step, so this file's Symmetric FAH target is exempt
from that specific criticized mechanism.

**One genuine (mild) asymmetry, noted precisely and resolved.** The sibling's literal
FAH statement uses cutoff n_B for the A'-side ("n > n_B with ρ(n)=A'"), while a naive
verbatim mirror for the B'-side would use cutoff n_A ("m > n_A with ρ(m)=B'"). But since
n_B is B's *own* earliest occurrence, every B'-occurrence automatically satisfies m ≥ n_B
> n_A, so "m > n_A" and "m > n_B, or m = n_B" cover an identical index set except for the
single index m = n_B itself — and m = n_B is already handled unconditionally by Lemma G
(q* | a_{n_B} is already established, being one of the two divisibilities Lemma G's proof
produces q* from). Hence the two cutoffs give logically equivalent content: Symmetric
FAH (canonical form, Step 8.7) is exactly "q* | a_m for every m > n_B with ρ(m) = B'",
matching FAH's own cutoff choice (n_B, the later of the two witnesses) exactly, with no
residual asymmetry once this is spelled out. I record this because the outline
explicitly asked for it to be checked, not asserted — the check is now complete, and it
resolves in favor of a clean mirror.

**Status: mechanism transfers, content not yet proved.** This confirms the mirrored
argument has no NEW obstruction of its own beyond the one already present in the
unmirrored (A'-side) form — i.e., proving Blocking-Data Bridging once, in a
side-agnostic statement (for an arbitrary S₀-extended-persistent type X with reference
prime q* ∈ (fixed finite reference set) and reference cutoff index n₀ᴮ := max(n_A,n_B)),
gives BOTH FAH and Symmetric FAH simultaneously with a single proof, rather than needing
two separate arguments. This is a genuine simplification of the remaining target (one
generic lemma instead of two asymmetric ones) but the Blocking-Data Bridging Lemma
itself — the actual hard step — remains open; I did not close it this round. Attempting
it directly (beyond the symmetry check) is left to whichever round next proves the
A'-side form, since by the above it transfers automatically.

### Cases checked directly (sanity, not full proof)
- **|Q| = 1** (e.g. a_1 = 4 = 2²): 𝒯 = {Q} = {{2}} is a single type, so 𝒫 = {Q}, no
  disjoint pairs exist, Step 2–4's gap is vacuous (there is nothing to reconcile), and
  Step 5 applies directly with S_0 = Q, L = 2, G = {0 mod 2}; the sequence is exactly the
  even integers greater than 4, matching a_{n+1} = a_n + 2 for all n ≥ 1 (T=1, L=2). This
  case is fully solved by the above with no gap.
- **|Q| = 2** (e.g. a_1 = 15 = 3·5): Q = {3,5}, 𝒯 = {{3},{5},{3,5}}. The two singleton
  types are disjoint from each other; if both are persistent, this is exactly the
  situation Step 2's Lemma addresses, and the outline-reviewer's simulation (§4 of its
  report) found the recruited prime is 2 in this case, matching S = {2}, S_0 = {2,3,5},
  L = 30 — consistent with the report's independently-found period (T,L) = (8,30). This
  is strong corroborating evidence for the Finite Core Theorem's conclusion but the
  gap (†) is what would be needed to derive it, rather than merely observe it, in
  general.
- **|Q| ≥ 3** (e.g. a_1 = 1001 = 7·11·13): the outline-reviewer's simulation found
  (T,L) = (282, 2002 = 2·7·11·13), i.e. a single extra prime 2 again suffices; this is
  consistent with, but does not prove, the general claim.

### Key lemmas (claim + mechanism) — status of each
- **Free Facts 1–2** — fully proved above, one line each.
- **Bounded Witness Lemma** — fully proved above (Step 2). This is the round's genuine
  new, load-bearing, promotable result.
- **Finite Core Theorem** — fully proved above (Step 3), an explicit finite bound on the
  core prime pool S, obtained purely from the Bounded Witness Lemma without any
  growth-rate or density argument.
- **(†) pairwise intersection of extended-persistent types** — NOT proved in general.
  Round 3 (Steps 4d–4f) fully proves the Canonical-Refinement Lemma and F_A∩F_B≠∅, which
  together *localize* (†) to the residual set V (both-sides-non-canonical pairs); every
  seed tested computationally has V = ∅ but this is not proved in general. Round 2
  (Step 4c) separately reformulates (†) as the halting question for a recruitment
  process; round 2 also retracted the earlier "Universal Glue Prime" attempt as false
  (Step 4b, refuted by the outline-reviewer's a_1=35 counterexample).
- **Generalized Bounded Witness Lemma (S₀-level)** — fully proved round 2 (Step 4c),
  reused this round in Step 4f's minimal-counterexample attempt via its Corollary.
- **Canonical-Refinement Lemma** — fully proved this round (Step 4d), new promotable
  content: closes (†) unconditionally whenever at least one side of a disjoint-base-type
  extended-type pair is its own base type's canonical refinement.
- **F_A ∩ F_B ≠ ∅** — fully proved this round (Step 4e); shown to be strictly subsumed by
  the Canonical-Refinement Lemma (a canonical-vs-canonical special case), with this
  scope limitation stated explicitly so it is not mistaken for closing the general case.
- **Minimal-counterexample attack on the localized residual V** — attempted this round
  (Step 4f) per the dispatch; does NOT close V = ∅. Two candidate contradiction routes
  were tried and both fail for a specific, documented reason (Step 4f): the natural
  measure |A'|+|B'| is non-decreasing under the only available refinement operation, and
  the Corollary's pigeonhole only certifies recurrence of the new prime on the side being
  reconciled, not on the fixed witness side. This is a genuine negative result, not an
  unexplored gap.
- **CRT + cyclic pigeonhole finish** — proved conditionally on (†) (Step 5); the CRT and
  pigeonhole mechanisms themselves are standard and correctly cited
  (`knowledge_base.md` "Modular arithmetic, CRT"; "Pigeonhole / extremal principle").

### Open gaps
- **RETRACTED (do not re-attempt as stated):** the "Universal Glue Prime Lemma" and its
  sparse/dense Q case split from round 2's first pass (old Step 4b) is false — refuted
  by an explicit counterexample (a_1 = 35, Q = {5,7}; the persistent type {5} has
  infinitely many odd, i.e. non-2-divisible, terms deep in the tail, e.g. a_153 = 975).
  The actual eventual period for a_1 = 35 needs the two extra primes {2,3} (L = 210,
  T = 34), not one universal prime. Confirmed independently this round. Do not spend a
  future round trying to prove a single distinguished prime always suffices, or that
  "sparse Q" (Q misses a small prime) is the right dichotomy variable — both are
  refuted.
- **RETRACTED / EXHAUSTED (do not re-attempt as stated):** the round-3 minimal-
  counterexample attack on the localized residual V (Step 4f), using μ(A',B')=|A'|+|B'|
  as the well-founded measure and the Generalized Bounded Witness Lemma's Corollary as
  the recruitment mechanism, does NOT close (†). Both candidate contradiction routes fail
  for a specific documented reason (Step 4f): (1) the produced object A'_0∪{q} is larger,
  not smaller, and lives outside the ambient set S₀ that μ is defined over, so it never
  contradicts minimality; (2) the Corollary only certifies the new prime q recurs
  infinitely often on the SIDE BEING RECONCILED, not on the fixed witness side, so
  "q forces the witness's own type to also be persistently linked" is unproved and, on
  the evidence here, likely false in general. A future round should not re-attempt this
  exact measure/mechanism combination; either a genuinely different well-founded measure
  or — more promisingly per the diagnosis in Step 4f — a SIMULTANEOUS/joint argument
  across ALL infinitely many occurrences of a base type at once (not a single witness)
  is needed.
- **(Localized this round, Step 4d–4f) Close the residual V** (pairs of
  extended-persistent types with disjoint base types, BOTH sides non-canonical
  refinements): this is now a strictly smaller target than the raw (†) or the
  recruitment-process halting question, since Step 4d unconditionally settles every pair
  with at least one canonical side. Computationally V = ∅ in all 15 tested seeds
  (including |Q| = 4 and |Q| = 5 cases), but no general proof. The most promising
  concrete direction identified this round (Step 4f) is a joint pigeonhole across all
  occurrences of a base type simultaneously (not a single witness per type), which
  neither this round's nor round 2's mechanisms provide.
- (Superseded by the above localization, kept for reference) The round-2 recruitment-
  process framing (Step 4c) remains a valid, unconditional reformulation of the FULL
  (†); Step 4d–4f show the same underlying difficulty persists even after restricting
  attention to the much smaller residual V, which is evidence the difficulty is
  intrinsic to the problem rather than an artifact of either framing.
- The n = 1 boundary extension in Step 5 (finite, checkable once T, L, and the threshold
  index are pinned down; not attempted in general here, though the outline-reviewer's
  four numeric examples all show it holding from n = 1 directly).
- **(Round 6, closed) The "collateral rogue pairs" gap from round 5 is now CLOSED**:
  Step 8.2's Collateral-Safety Theorem shows unconditionally that a base-type pair
  fully safe at S₀ stays fully safe at every S₁ ⊇ S₀. No longer an open gap.
- **(Round 6, sharpened but still open) Gap (†) is now reduced exactly to base-type-
  pair-level termination** (Step 8.3): open(k) is a non-increasing sequence over a
  FIXED finite index set (≤ C(|𝒫|,2) base-type pairs); (†) holds iff open(k) reaches ∅
  in finitely many rounds. This is imported to depend on:
  (a) the sibling approach `greedy-exchange-cost-potential`'s Full-Absorption
  Hypothesis (FAH), not proved here;
  (b) a **Symmetric FAH** strengthening (Step 8.4), which I identify this round as the
  precise requirement for Step 8.5's proof but which is NOT literally the sibling
  approach's stated (one-sided) target — this symmetric form is a new, not-yet-
  attempted sub-gap, flagged honestly, not silently assumed.
  Given (a) and (b), Step 8.5 proves the whole recruitment process terminates in
  exactly one further round and Step 5's finish completes the problem. Neither (a) nor
  (b) is established in this file. **(Round 7 update, Step 8.7):** what is actually
  needed for (a)+(b) is a single *canonical-prime* Blocking-Data Bridging Lemma (for
  q*_i := min(F'_i∩F''_i)), proved once and applying to both sides by the symmetry
  check of Step 8.8 — this is a narrower, cleaner target than "FAH ∧ Symmetric FAH" as
  two separate claims, and is NOT contingent on the sibling's Two-Witness Intersection
  Uniqueness target. Still open.

### Step 9 — round 7: the secondary "literal periodicity from n = 1" gap, reduced and
partially analyzed

This gap has been on the workspace's radar, unattempted, since round 1 (see
`current.md`'s "Rules" and the Goal's Eval History). This round I give it a first
real, independent treatment: a rigorous reduction of the (a priori vague) target to a
precise finite statement, together with an explicit proof that the natural "it's just a
finite check" heuristic proposed by this round's outliner is **not**, by itself, valid
for a general eventually-periodic integer sequence — so genuine content, not mere
bookkeeping, is required to close it.

#### Step 9.1 — Exact-Equality Reduction Lemma (proved in full, unconditional)

**Lemma.** Suppose T, L are positive integers and N₀ ≥ 1 is an index such that
a_{n+T} = a_n + L holds for every n ≥ N₀. Then: a_{n+T} = a_n + L holds for **every**
positive integer n (the problem's literal target) **if and only if**
a_{i+T} = a_i + L holds for each of the (N₀ − 1) indices i = 1, 2, ..., N₀ − 1.

*Proof.* (⟹) If the identity holds for every n ≥ 1, it holds in particular for every
i ∈ {1,...,N₀−1}. (⟸) If the identity holds for every i ∈ {1,...,N₀−1} (by hypothesis)
and for every n ≥ N₀ (given), then since every positive integer n satisfies exactly one
of "n < N₀" or "n ≥ N₀", the identity holds for every positive integer n. ∎

This is elementary — a direct case split covering every positive integer exactly once —
but it is worth stating and proving explicitly because it pins down PRECISELY what "the
n=1 gap" consists of: exactly N₀ − 1 concrete equalities between specific terms of the
sequence (each an explicit, well-defined positive integer, since the sequence is
deterministic), no more and no less. In particular it rules out any additional hidden
difficulty (e.g. some subtler global consistency condition) beyond these finitely many
checks — the entire content is localized here.

#### Step 9.2 — the finitely-many-equalities target is NOT automatic: an explicit
counterexample for general eventually-periodic increasing integer sequences

The round-7 outline's proposed mechanism for Step 9.1's finitely many equalities was:
"any prefix of a periodic-from-N₀ sequence can be folded into the period by taking
T' := T·(smallest k making N₀ ≤ k·T)". I checked this precisely and it is **false in
general** — i.e., it is not a valid unconditional mechanism, even restricted to
strictly increasing sequences of positive integers, without further structure specific
to the greedy recursion. I give an explicit counterexample to make this precise (a
correction of the outline, in the spirit of CLAUDE.md's rigor rules: do not accept an
unproved reduction as if it were automatic).

**Counterexample.** Define a strictly increasing sequence of positive integers by
a_1 := 1, a_2 := 5, and a_n := 997 + n for n ≥ 3 (so a_3 = 1000, a_4 = 1001, a_5 = 1002,
...). This is strictly increasing: 1 < 5 < 1000 < 1001 < ... . It is eventually periodic
with T = 1, L = 1 from N₀ = 3 onward: a_{n+1} = (997+n+1) = (997+n) + 1 = a_n + 1 for all
n ≥ 3.

**Claim: no pair of positive integers (T'', L'') satisfies a_{n+T''} = a_n + L'' for
every n ≥ 1** (in particular the specific rescaled T' = T·k of the outline's proposed
mechanism, for any k ≥ 1, fails — and so does every other candidate pair).

*Proof of claim.* Suppose (T'', L'') worked for all n ≥ 1. Restricting to n ≥ 3 and
using the already-established formula a_n = 997+n there: a_{n+T''} = 997+n+T'' (valid
since n+T'' ≥ 3 too) must equal a_n + L'' = 997+n+L''. Hence T'' = L''. Now apply the
hypothesis at n = 1: a_{1+T''} = a_1 + L'' = 1 + T'' (using T''=L''). If T'' = 1: this
says a_2 = 2, but a_2 = 5 ≠ 2 — contradiction. If T'' ≥ 2: then 1+T'' ≥ 3, so
a_{1+T''} = 997 + (1+T'') = 998 + T'' by the formula for n ≥ 3; the required equality
998 + T'' = 1 + T'' gives 998 = 1, false. Both cases contradict, so no such (T'',L'')
exists. ∎

This confirms, rigorously, that "eventually periodic with parameters (T,L) from some
N₀" does **not**, by itself, imply "periodic from n=1 with the same or any rescaled
(T,L)" for a general strictly increasing integer sequence — the outline's proposed
period-scaling mechanism is not a valid general argument. (It happens to work in this
counterexample for none of the multiples either, since the argument above shows T''
is forced to equal L'' for ANY candidate period compatible with the n≥3 tail, and no
such value satisfies the n=1 constraint — the obstruction is not about the SIZE of the
rescaling, it is that a_1, a_2 are simply not congruent, in the right cyclic position,
to any later value of the tail's arithmetic progression.) Consequently, closing the
n=1 gap for our specific greedy sequence genuinely requires using the structure of the
greedy minimality rule itself (why the early terms of THIS sequence, unlike the
artificial counterexample above, might be forced into the eventual cyclic pattern) —
it is not a free formal consequence of eventual periodicity, contrary to what a
naive reading of the outline's step 5 might suggest. I flag this explicitly so no
future round treats it as a formality per CLAUDE.md's rigor rules.

#### Step 9.3 — honest residual gap and a documented candidate strategy (not completed)

Given Step 9.2, closing the n=1 gap for our sequence requires showing, for
i = 1,...,N₀−1 (N₀ the explicit threshold from Step 8.5/Step 5's construction), that
a_i's own value — determined by the greedy rule applied against ONLY a_1,...,a_{i-1}
(a genuinely WEAKER constraint set than what governs terms n ≥ N₀, which must satisfy
legality against the full, eventually-stable extended-type structure) — already equals
a_{i+T} − L. I attempted the following candidate strategy and record precisely why it
does not yet close the gap, rather than silently dropping it:

*Candidate strategy.* Try to show a_i, for i < N₀, is already the smallest integer
exceeding a_{i-1} whose residue mod L (L = ∏ S₀^(final)) lies in the eligible set G
(Step 5's construction) — i.e. that the "residue-driven rule" (valid unconditionally
for n ≥ N₀ by Step 5) is in fact ALREADY the operative rule from i = 1 onward, so that
determinism of "smallest legal integer" pins a_i to the same cyclic-order position it
would occupy under the eventual rule.

*Why this does not close, as stated.* The residue-driven rule's validity for n ≥ N₀
rests on the fact "(†): any two integers with residues in G share an S₀^(final)-prime
factor" (Step 5), which lets legality against S₀^(final)-typed EARLIER terms be checked
by residue alone. But for i < N₀, legality of a candidate for a_i must be checked against
a_1,...,a_{i-1} — a set that (i) may not yet include a representative of every
S₀^(final)-extended-persistent type (some types' earliest witness, by definition, occurs
only later, possibly beyond N₀), and (ii) may include the very early terms whose OWN
extended type has not yet stabilized. So a residue r ∈ G might fail to be legal against
a specific EARLY a_j (j < i) whose factorization does not yet exhibit S₀^(final)
structure at all, purely because that early term's actual prime factors (not
S₀^(final)-related) happen to coincide with r's needed complement — this is a live
possibility not excluded by anything proved above. Conversely, a residue r ∉ G might
still be LEGAL against a_1,...,a_{i-1} for small i, precisely because the (†)-violating
configurations that make r "ineligible" in the limit have not yet had a chance to
manifest among the few, early terms — i.e. the greedy process could genuinely pick an
early term OUTSIDE G, and Step 9.1's equalities would then fail for that i, unless a
further argument shows this cannot happen. Neither direction is ruled out by the
certified stack as it stands; this is a genuinely separate structural question from
FAH/Symmetric FAH (Step 8), not a restatement of it, though it plausibly shares its
flavor (both concern how early/transient terms interact with the eventual S₀ structure).

**Status: open.** I do not claim to have closed this gap. What Step 9.1–9.3
establish, rigorously: (a) the gap is exactly N₀−1 explicit equalities, no more (Step
9.1); (b) this is provably NOT a free consequence of eventual periodicity in general —
a specific greedy-structure argument is required, and the outline's proposed
period-rescaling mechanism does not, by itself, supply one (Step 9.2, with an explicit
counterexample); (c) a natural candidate mechanism (residue-driven rule holding from the
start) has a precisely identified point of failure, not yet resolved either way (Step
9.3). This is real, honest partial progress: it upgrades the gap from "untouched,
vaguely believed true from empirical checks" (rounds 1–6) to "precisely localized, with
one plausible attack documented and its exact obstruction identified" — but it remains
open, and — as Step 9.2 shows — is not reducible to a formality once (†)/FAH is settled.
A future round should treat Step 9.3's obstruction (whether every residue outside G is
already blocked among a_1,...,a_{i-1} for i < N₀, or conversely whether the greedy
process could genuinely select an off-G value early on) as the precise next target.

### Watch out for
- Do not conflate "type" (τ, valued in 2^Q) with "extended type" (ρ, valued in 2^{S_0});
  the Bounded Witness Lemma and Finite Core Theorem operate cleanly at the τ-level; the
  genuine difficulty is entirely in the ρ-level refinement (Step 4).
- The recruited witness set S was built via ONE fixed witness per persistent BASE type
  (|𝒫| ≤ 2^k − 1 witnesses total) — this is what makes S provably finite in closed form;
  do not replace this with witnesses chosen adaptively/recursively at the extended-type
  level without re-verifying finiteness, since that is exactly where an apparently
  unbounded recursion could reappear (see the discussion under "The gap" in Step 4).

## Full proof
Not present — Status is `partial`; see Steps 1–3 for the fully proved portion (Bounded
Witness Lemma, Finite Core Theorem), Steps 4d–4e for two new fully proved localization
lemmas, Step 4f for the precisely isolated remaining gap (the residual set V of
both-sides-non-canonical violating pairs) and the documented failure of round 3's
minimal-counterexample attack on it, Step 6 (round 4) for the falsification of PUCL's
literal construction and the from-scratch proof that no local/disjunctive per-type core
(PUCL, in any form tried) can rescue the closing corollary needed for (†), and Step 7
(round 5) for the new unconditional Monotonicity Lemma and the Conditional
Single-Pair/Simultaneous Resolution Theorems (both proved in full, conditional on the
sibling approach's still-open Singleton Hypothesis) — a negative-but-precise result:
the gap is now localized EXACTLY to the Singleton Hypothesis (and, failing that, to the
still-missing "joint pigeonhole across all occurrences of a base type at once"
ingredient for the bounded-rounds fallback), not to any defect in the recruitment
mechanism itself. **Superseded by round 6, Step 8** (below): round 5's Singleton-
Hypothesis-conditional theorems are retired as a route forward (the Singleton
Hypothesis is now known FALSE in general), replaced by Step 8's unconditional
Collateral-Safety Theorem plus a precise reduction to the sibling approach's
Full-Absorption Hypothesis (and a newly identified Symmetric FAH strengthening). Given
FAH + Symmetric FAH (both currently open, imported as black-box gaps — see Step 8.4,
8.6), Step 8.5's Theorem and Corollary complete the whole problem via Step 5's finish.
Without them, Step 8.3 still gives a strictly sharper, unconditional localization of
the residual gap (base-type-pair-level, over a fixed finite index set) than any prior
round achieved. **Round 7 update:** Step 8.7–8.8 narrow the FAH/Symmetric FAH
requirement to a single canonical-prime, side-agnostic Blocking-Data Bridging Lemma
(still open, not proved here), decoupled from the sibling approach's Two-Witness
Intersection Uniqueness target. Step 9 gives a proved reduction of the separate
secondary n=1 gap to finitely many explicit equalities, together with a proof (via an
explicit counterexample) that this reduction is not automatically true in general and a
documented, still-open candidate mechanism. Neither Step 8's nor Step 9's residual gap
is closed this round.

## Promotable lemmas
- **Free Facts 1–2** (gcd(a_n,a_1)>1 for n≥2; gcd(a_i,a_n)>1 for all i<n) — trivial but
  reusable, proved in "Setup and notation" above.
- **Bounded Witness Lemma** — statement: if A, B are two subsets of Q = P(a_1) that both
  occur infinitely often as τ(n) := P(a_n)∩Q, are disjoint (A∩B=∅), and m is any single
  index with τ(m)=B, then every n>m with τ(n)=A has a_n divisible by some prime in the
  fixed finite set P(a_m)\Q. Proved in full in Step 2. This is a genuinely new,
  self-contained, reusable result (not present in the outline as a rigorous lemma) and
  is the correct replacement for the outline's unproven "primorial growth vs. gap bound"
  heuristic — recommend certifying it as a shared lemma for the other approaches
  (amortized-charging-budget in particular targets the same phenomenon and could import
  this instead of re-deriving its "permanence" claim from scratch).
- **Finite Core Theorem** — statement: with S := ⋃_{B∈𝒫}(P(a_{m_B})\Q) for any choice of
  one witness index m_B per persistent type B, S is finite with an explicit bound, and
  every sufficiently large term of a persistent type is divisible by an S-prime relative
  to each disjoint persistent type. Proved in full in Step 3, directly from the Bounded
  Witness Lemma. Also recommended for certification — it gives every approach in the
  population an explicit, finite, closed-form core pool without needing any density or
  growth-rate estimate.
- **Generalized Bounded Witness Lemma (S₀-level)** — statement: for ANY fixed finite
  S₀ ⊇ Q, with ρ(n) := P(a_n)∩S₀, if A', B' ⊆ S₀ are ρ-types occurring infinitely often
  with A'∩B'=∅ (disjoint as subsets of S₀), and m is any index with ρ(m)=B', then every
  n>m with ρ(n)=A' has a_n divisible by some prime of the fixed finite set P(a_m)\S₀.
  Proved in full in Step 4c, by the identical argument as the Bounded Witness Lemma with
  Q replaced by S₀ (the proof never actually used any special property of Q beyond it
  being a fixed finite set). Comes with a Corollary (Recruitment step): if (†) fails for
  a pair A',B' ∈ 𝒫', a specific new prime q ∉ S₀ is forced to divide infinitely many
  A'-type terms — this is real, new, promotable content and gives any future approach a
  precise, mechanically well-defined process to reason about instead of an abstract
  existence claim.
- **Canonical-Refinement Lemma** (round 3, Step 4d) — statement: for disjoint persistent
  base types A, B ∈ 𝒫 with canonical witnesses m_A, m_B and canonical extended
  refinements A'_can := ρ(m_A) = A ∪ F_A, B'_can := ρ(m_B) = B ∪ F_B, every
  extended-persistent A' refining A meets B'_can, and every extended-persistent B'
  refining B meets A'_can. Proved in full in Step 4d via two sub-lemmas (General
  Reconciliation Lemma: A' ∩ F_B ≠ ∅ for every extended-persistent refinement A' of A;
  and B'_can = B ∪ F_B exactly). Unconditionally closes (†) for every pair with at least
  one canonical side; explicitly does not claim more. Recommended for certification —
  reusable by any approach reasoning about extended-type refinements.
- **F_A ∩ F_B ≠ ∅** (round 3, Step 4e) — statement: for disjoint persistent base types
  A, B ∈ 𝒫 with canonical witnesses m_A, m_B, F_A := P(a_{m_A})\Q and F_B :=
  P(a_{m_B})\Q intersect. Proved in full in Step 4e directly from Free Fact 2. Recorded
  as strictly subsumed by the Canonical-Refinement Lemma (a canonical-vs-canonical
  special case) — recommend certifying alongside the Canonical-Refinement Lemma with
  this scope note attached so it is not mistaken for closing the non-canonical case.
- **Monotonicity of Resolution** (round 5, Step 7) — statement: if S₀ ⊆ S₁ are finite
  sets of primes ⊇ Q, and A', B' ∈ 𝒫' (S₀-extended-persistent) satisfy A'∩B'≠∅, then
  every S₁-extended-persistent refinement pair A''⊇A' (A''∩S₀=A'), B''⊇B' (B''∩S₀=B')
  also satisfies A''∩B''≠∅. Proved in full in Step 7, a one-paragraph direct argument
  from the definitions (a shared prime in S₀ is preserved under any superset
  refinement). Fully unconditional and reusable — recommend certifying; it makes
  rigorous what round 2's Step 4c only checked informally, and is a prerequisite for
  any "bounded number of rounds" argument in any approach in this population.
- **Conditional Single-Pair Permanent Resolution Theorem** and **Conditional
  Simultaneous Resolution Theorem** (round 5, Step 7) — statement: given the certified
  Lemma G and Generalized Bounded Witness Lemma, IF the extended-persistent types
  involved in a rogue pair (or, for the batch version, every type in 𝒫' with a rogue
  partner) satisfy the "Singleton Hypothesis" (their own earliest-occurrence witness
  has exactly one prime outside S₀), THEN one finite recruitment round (a single prime,
  or a bounded finite batch of primes — one per connected component of the rogue-
  partner relation — if connectivity is not separately established) permanently
  resolves the pair (resp. every currently-rogue pair at once). Proved in full in
  Step 7, conditional on the Singleton Hypothesis (imported, not re-derived — owned by
  `greedy-exchange-cost-potential`). Recommend certifying as a conditional lemma (i.e.
  certify the implication, not an unconditional claim) so any approach that later
  proves the Singleton Hypothesis unconditionally can immediately invoke this to finish
  the whole problem via Step 6's CRT + cyclic-pigeonhole argument. **Superseded as a
  route forward** — the Singleton Hypothesis is now known FALSE (round 6); kept for the
  audit trail, not reused.
- **Projection Lemma** (round 6, Step 8.1) — statement: for finite S₀ ⊆ S₁ with
  Q ⊆ S₀, if A'' ⊆ S₁ is S₁-extended-persistent then A' := A''∩S₀ is
  S₀-extended-persistent and A'∩Q = A''∩Q (base type unchanged). Proved in full,
  ≤1-page, unconditional — the "downward" counterpart of the identity ρ(n)=ρ₁(n)∩S₀
  already used implicitly by the certified Monotonicity Lemma. Recommend certifying;
  no gap.
- **Collateral-Safety Theorem** (round 6, Step 8.2) — statement: if a base-type pair
  (A,B) is "fully safe" at S₀ (every pair of S₀-extended-persistent refinements of
  A,B intersects), it stays fully safe at every S₁ ⊇ S₀. Proved in full,
  unconditional, by combining the Projection Lemma with the certified Monotonicity of
  Resolution Lemma. Comes with a free Corollary: the set of persistent base types 𝒫
  and the finite list of disjoint base-type pairs are fixed for the whole recruitment
  process (since Q never changes). Recommend certifying — closes round 5's
  "collateral rogue pairs" gap completely, and is the key tool behind Step 8.3's
  reduction of (†) to base-type-pair-level termination. No Singleton Hypothesis or
  Full-Absorption Hypothesis is used anywhere in this lemma's proof.
- **Canonicalization Lemma (round 7, Step 8.7)** — statement: Step 8.5's finish only
  requires, for each rogue pair, a single prime q ∈ F'∩F'' witnessing BOTH the A'-side
  and B'-side full-absorption properties for the SAME prime (a joint existential
  statement, "Joint FAH"), not the sibling approach's Two-Witness Intersection
  Uniqueness (|F'∩F''|=1); canonically fixing q* := min(F'∩F'') makes "same prime both
  sides" automatic by construction rather than requiring a separate uniqueness proof.
  Proved in full (a short, elementary logical/definitional argument) in Step 8.7.
  Recommend certifying — it removes a dependency between this approach and the
  sibling's round-7 target that neither approach's outline made explicit, and it
  applies regardless of whether Two-Witness Intersection Uniqueness turns out to be
  true, false, or unproved.
- **Symmetry-Transfer Check (round 7, Step 8.8)** — statement: the proposed
  Blocking-Data Bridging mechanism (for FAH's A'-side form) contains no argument
  specific to n_B's status as B's earliest occurrence (unlike the sibling's separate,
  flagged-as-likely-dead Two-Witness Uniqueness mechanism); it is side-agnostic in the
  index n and the reference set (F' vs F''), so a single proof of the canonical-prime
  form gives both FAH and Symmetric FAH. Also resolves the apparent cutoff asymmetry
  (n>n_B for A' vs n>n_A for B') as merely notational: since every B'-occurrence
  automatically satisfies m≥n_B>n_A, the two cutoffs are logically equivalent. Proved
  in full (a structural inspection argument) in Step 8.8; the Blocking-Data Bridging
  Lemma itself remains open (owned by/shared with the sibling approach) — this lemma
  only certifies that the MIRRORING step introduces no new gap. Recommend certifying as
  a scoping/reduction lemma.
- **Exact-Equality Reduction Lemma (round 7, Step 9.1)** — statement: given eventual
  periodicity a_{n+T}=a_n+L for n≥N₀, literal periodicity for all n≥1 holds if and only
  if a_{i+T}=a_i+L for each of the finitely many i=1,...,N₀−1. Proved in full (a direct
  case split) in Step 9.1. Fully general (not specific to this problem's recursion —
  applies to any integer sequence with an eventually-periodic gap structure). Recommend
  certifying — it is the precise, complete localization of the secondary n=1 gap for
  any future approach to this problem.
- **Non-Automaticity of Prefix Folding (round 7, Step 9.2)** — statement: there exists a
  strictly increasing sequence of positive integers that is eventually periodic (in the
  a_{n+T}=a_n+L sense) from some index N₀ but for which NO pair (T'',L'') of positive
  integers gives a_{n+T''}=a_n+L'' for all n≥1 — explicit counterexample:
  a_1=1, a_2=5, a_n=997+n for n≥3 (period T=1,L=1 from N₀=3; proof in Step 9.2 that
  every candidate global period is forced to have T''=L'' by the tail's structure, and
  that no such value satisfies the n=1 constraint). Proved in full in Step 9.2. This is
  a fully general negative result (about arbitrary strictly increasing integer
  sequences, not about this problem's specific greedy recursion) showing that the
  "period-rescaling" mechanism proposed by this round's outliner for closing the n=1
  gap is NOT unconditionally valid, and that closing Step 9.1's finitely many equalities
  for our specific sequence requires genuine use of the greedy recursion's structure.
  Recommend certifying as a cautionary/scoping lemma for any future approach tempted to
  treat the n=1 extension as automatic.

## Approaches tried
- **Round 12 (this round): Reduced-Alphabet Corollary — bookkeeping only, no FAH
  progress.** Per this round's outline/outline-review (scoped explicitly as
  bookkeeping continuity, no 15th same-corridor FAH mechanism), formalized and proved
  the Reduced-Alphabet Corollary flagged by this round's smallcase math-explorer
  (`/tmp/round-12/math-explorer-smallcase.md`): a one-line, fully rigorous corollary
  combining the already-certified Confined-GCD Lemma and Singleton-Side FAH Lemma,
  proved in full in Step 4g below and certified as `lemmas/reduced-alphabet-
  corollary.md`. Honestly scoped throughout: it narrows the SIZE of the residual
  divisor-class alphabet that FAH must rule out on the non-singleton side of a rogue
  pair (to an explicit closed-form count, collapsing to exactly 1 in the concrete
  `|F''|=2` standing test seeds), but supplies no new mechanism for ruling out even
  that single remaining class — the Escape-Cost Vacuity Theorem (round 10) already
  shows no currently-certified magnitude-only tool can do so, and this round's
  corollary does not evade that impossibility (it operates entirely on the alphabet's
  SIZE, not on any new class-discriminating fact). Outcome: real, small, honest,
  unconditional addition; Status stays `partial`, FAH/Symmetric FAH unchanged.
- **Round 2 (this round, second pass): retraction + S₀-level generalization +
  computational narrowing.** Retracted the Universal Glue Prime Lemma and sparse/dense
  split from this round's first pass (refuted by the outline-reviewer's a_1=35
  counterexample, independently reconfirmed here). Replaced it with (i) a fully proved
  new lemma (Generalized Bounded Witness Lemma at the S₀-level, Step 4c) that is
  strictly more general than the original Bounded Witness Lemma and needs no new
  hypotheses; (ii) an exact reformulation of (†) as the halting question for a
  concretely-defined, fully-justified-per-round recruitment process, so the gap is now
  a termination/counting question rather than an abstract existence claim; (iii) three
  monovariant candidates tried and shown not to work, saving a future round from
  re-trying them; (iv) computational evidence across 10 seeds (up to |Q|=4, 70 extended
  types) that the Finite Core Theorem's original S already suffices for (†) with zero
  further recruitment rounds — a sharper, concrete conjecture proposed as the most
  promising next target. (†) itself remains open; Status stays `partial`.
- **Round 2 (this round, first pass, RETRACTED): Universal Glue Prime + sparse/dense
  split.** Sharpened the abstract (†) into a concrete, testable claim (Step 4b): a
  single smallest-prime-outside-Q p* eventually divides every proper-base-type term,
  in the "sparse Q" regime. Numerically refuted by the outline-reviewer (a_1=35, 21, 33
  are all sparse-Q counterexamples). Retracted in full this round; see the retraction
  notice at the start of Step 4b and the replacement content in Step 4c. Do not re-open.
- **Round 1 (this round): explicit constructive recruitment via Bounded Witness Lemma.**
  Replaced the prior skeleton's unproven "primorial growth vs. Bertrand-style gap bound"
  heuristic (step 3 of the prior skeleton) with a fully rigorous pigeonhole argument
  (Bounded Witness Lemma, Step 2 above) that gives an EXPLICIT finite bound on the core
  prime pool with no growth-rate comparison needed at all — this closes what the
  outline and outline-reviewer both flagged as the central open question ("is the
  load-bearing prime set S finite, and why") in the form that matters most: an explicit,
  closed-form finite pool built from ≤ 2^{|Q|}−1 fixed witness integers. What remains
  open is a narrower, precisely-isolated combinatorial gap (†) about refinements of base
  types into extended types, which the CRT+pigeonhole finish (Step 5) needs to run
  cleanly. Outcome: substantial progress, genuine new lemma proved and promotable, but
  the approach as a whole remains `partial` because Step 5's finish depends on (†).
- **Round 3 (this round): Canonical-Refinement Lemma, F_A∩F_B≠∅, and a minimal-
  counterexample attack on the localized residual — genuine progress, gap narrowed
  further but not closed.** Fully proved two new lemmas dispatched from this round's
  explorers (Step 4d: Canonical-Refinement Lemma, via a General Reconciliation sub-lemma
  and an exact set-equality B'_can = B∪F_B; Step 4e: F_A∩F_B≠∅, directly from Free Fact
  2), both promotable and both correctly scoped (neither is overclaimed beyond what it
  proves). Used them to localize (†) from "all disjoint-base-type extended-type pairs"
  to the strictly smaller residual set V (pairs where BOTH sides are non-canonical
  refinements) — real, unconditional progress. Attempted the dispatch's requested
  minimal-counterexample attack on V (Step 4f): well-ordering on μ(A',B')=|A'|+|B'|,
  the Generalized Bounded Witness Lemma's Corollary as the recruitment mechanism. This
  does NOT close V=∅; both candidate contradiction routes fail for a specific,
  documented structural reason (Step 4f) rather than being merely unexplored — the
  natural measure increases (not decreases) under refinement, and the recruited prime's
  recurrence is only certified on the reconciled side, not the fixed witness side. Ran
  an extended 15-seed computational check (up to |Q|=5) confirming V=∅ empirically in
  every case, plus a refinement-diversity check showing the true obstruction is not a
  single universal prime (already known to be false, Step 4b) but likely a joint,
  simultaneous constraint across a base type's whole infinite family of occurrences —
  identified as the most promising concrete direction for a future round. Status
  remains `partial`; (†)'s residual V is the sole remaining gap for this approach.
- **Round 4 (this round): tested the dispatched Persistent Uniform Core Lemma (PUCL)
  rigorously; falsified its literal construction; proved a structural "no rescue"
  result for the outline's proposed Corollary.** As directed, attempted PUCL — treating
  its Step 3 Corollary as suspect per the outline-reviewer's warning, not as a formality
  — and found, with fully hand-verified small witnesses (a_1=175, base type {7}: first
  occurrence a_3=182=2·7·13 gives a naive core {2,13}; the VERY NEXT occurrence
  a_4=189=3³·7 already misses it): **PUCL's literal first-occurrence-anchored
  construction is false**, exactly as the retracted Step 4b's "Universal Glue Prime"
  was, just at a smaller scope. Separately proved the "generous" S-level form of PUCL
  (C_A := S, the whole Finite Core Theorem pool) is TRUE but is a trivial one-line
  corollary of the already-certified Finite Core Theorem, adding no new content. Most
  importantly, gave a from-scratch, minimal-witness proof (Step 6c: a_3=182 vs a_5=195,
  gcd=13, 13∉S₀, ρ(3)={2,7}, ρ(5)={3,5} disjoint despite both types being covered
  disjunctively by the shared candidate core {2,3}) of exactly WHY no version of PUCL's
  Corollary can be rescued: disjunctive per-type coverage never controls WHICH element
  of a shared core two specific occurrences realize, while Free Fact 2's unconditional
  shared-prime guarantee between any two terms can (and provably does, recurringly) land
  outside S₀. Also checked and ruled out a weaker single-universal-prime-per-type rescue
  (type {7} for a_1=175 has no single covering prime; needs both 2 and 3, used on
  different occurrences). Conclusion: **PUCL alone is insufficient to close (†)**, in
  every form tried (literal, generous, single-prime); the still-missing ingredient is
  the global/simultaneous argument flagged in round 3's Step 4f, not a local per-type
  statement. This is a genuine, rigorous negative result narrowing the search space of
  future attempts, not a stall — recorded in full in Step 6. Status remains `partial`;
  gap (†)/residual V is unchanged from round 3's localization, now with PUCL ruled out
  as a route to closing it.
- **Round 5 (this round): Simultaneous Resolution Lemma, proved conditionally, plus a
  new unconditional Monotonicity Lemma — the exact "route 2" repair.** Per this
  round's dispatch, retargeted from the retracted round-4 "V=∅ always" claim
  (independently re-confirmed false by this round's outline-reviewer via four fresh
  counterexamples a_1=187,209,247,385; not re-litigated here) back to the recruitment-
  process-termination framing. Proved in full and unconditionally: the **Monotonicity
  Lemma** (a resolved disjoint-type pair, and every further refinement of it, stays
  resolved forever — Step 7). Using the certified Lemma G (`extended-earliest-witness-
  intersection.md`, new since round 4) together with the certified Generalized Bounded
  Witness Lemma, proved the **Conditional Single-Pair Permanent Resolution Theorem**
  and its batch form, the **Conditional Simultaneous Resolution Theorem** (Step 7):
  conditional on the (still-open, owned by `greedy-exchange-cost-potential`) Singleton
  Hypothesis, a single finite recruitment round (one prime per connected component of
  the rogue-partner relation, collapsing to a genuinely single prime whenever that
  relation is connected) permanently resolves EVERY currently-rogue pair at once — this
  is precisely round 3's "route 2" obstruction (the recruited prime was only certified
  on the reconciled side, not the fixed witness side) repaired, using Lemma G's
  symmetric shared-prime guarantee plus the Singleton Hypothesis to force the two
  sides' recruited primes to coincide exactly, with no pigeonhole ambiguity left when
  singleton holds. Independently verified computationally, from a fresh from-scratch
  script (not reusing any prior round's code), that the theorem's predicted structure
  holds exactly in all four known nonzero-round seeds: every rogue-pair witness's F'
  set is a literal singleton, and the singleton prime is identical across every pair
  sharing a type (Q_R = {7} for a_1=187 and 209, {3} for a_1=247, {19} for a_1=385) —
  strong corroborating evidence for both the mechanism and (separately) the Singleton
  Hypothesis itself, though not a proof of the hypothesis. Honestly documented what
  remains open: (1) the Singleton Hypothesis itself, not attempted here (owned
  elsewhere); (2) the bounded-total-rounds fallback in case Singleton fails for some
  type, shown to reduce to the same still-missing "joint pigeonhole across a whole base
  type's infinite family of occurrences at once" ingredient identified in rounds 2–3,
  not supplied this round. Status remains `partial`, but the gap is now localized more
  precisely than ever: it is EXACTLY the Singleton Hypothesis (for the "one round
  suffices" case) or the joint-pigeonhole ingredient (for the general bounded-rounds
  fallback), not any defect in the recruitment/CRT machinery itself, which is now fully
  conditional-complete.
- **Round 6 (this round): Projection Lemma + unconditional Collateral-Safety Theorem;
  reduction of (†) to base-type-pair-level termination; precise rigorous import of the
  sibling approach's Full-Absorption Hypothesis (plus a newly identified Symmetric FAH
  strengthening).** Per this round's dispatch, and per the independently reconfirmed
  falsification of the Universal Singleton Hypothesis (a_1=4807 gives F'={13,17},
  a_1=11305 gives F'={11,103}, both |F'|=2 — round 5's Conditional theorems are
  retired as a route forward, not re-used anywhere in this round's work). Proved in
  full, unconditionally, with NO Singleton Hypothesis or Full-Absorption Hypothesis
  anywhere: the **Projection Lemma** (Step 8.1: S₁-extended-persistent types project
  down to S₀-extended-persistent parents, base type invariant) and, combining it with
  the already-certified Monotonicity of Resolution Lemma, the **Collateral-Safety
  Theorem** (Step 8.2: a base-type pair fully safe at S₀ stays fully safe at every
  S₁ ⊇ S₀) — this completely and unconditionally closes round 5's "collateral rogue
  pairs" gap. Used it to show (Step 8.3) that (†) reduces EXACTLY to termination of a
  monotone non-increasing sequence open(k) over a FIXED finite set of ≤ C(|𝒫|,2)
  base-type pairs (sharper than round 5's extended-type-level framing, where the
  number of currently-rogue types is not obviously bounded independent of k). Then
  (Step 8.4–8.5) precisely imported the sibling approach's Full-Absorption Hypothesis
  (FAH) and — honestly identifying that the literal one-sided FAH is not quite enough
  — introduced and used a **Symmetric FAH** strengthening (both directions of the
  Lemma-G prime's "eventually all occurrences" property), proving rigorously, step by
  step, that Symmetric FAH for every currently-rogue extended pair (finitely many)
  implies the ENTIRE recruitment process terminates in exactly one further round,
  after which Step 5's CRT + cyclic-pigeonhole finish completes the whole problem.
  Every step of this implication cites either an already-certified lemma (Projection,
  Monotonicity, Lemma G, Generalized Bounded Witness Lemma) or is a direct, checked
  deduction from Symmetric FAH with no unstated assumption — documented in Step 8.5
  with an explicit account of exactly where the symmetric (two-sided) strength is used
  and why the one-sided form alone does not suffice (Case 2 of the proof needs q_i to
  land in BOTH A'' and B'', and one-sided FAH only forces it into A''). Honestly
  flagged as still open, not proved here: (1) FAH itself (owned by
  `greedy-exchange-cost-potential`); (2) Symmetric FAH, a new sub-gap identified this
  round, not attempted computationally or proof-wise in this file. Status remains
  `partial`, but the gap is now narrower and more precisely pinned than at any prior
  round: unconditionally reduced to base-type-pair-level termination, and, modulo the
  two imported hypotheses, a complete finish is proved.
- **Round 7 (this round): decoupled the finish from the sibling's Two-Witness
  Uniqueness target, confirmed the symmetry-mirroring is obstruction-free, and gave
  the n=1 secondary gap its first real treatment.** Per this round's dispatch: (1)
  Step 8.7 proves — carefully re-reading Step 8.5's own proof — that its Case 2 only
  needs a single prime q ∈ F'∩F'' witnessing BOTH sides' full absorption ("Joint
  FAH"), not the sibling approach's this-round target |F'∩F''|=1 (Two-Witness
  Intersection Uniqueness, which the outline-reviewer independently judged at serious
  risk of being a repackaged instance of the already-dead "Lemma H branch analysis"
  mechanism). Canonically defining q* := min(F'∩F'') supplies "same prime both sides"
  by construction, decoupling this file's progress from the sibling's specific
  (at-risk) mechanism entirely — a genuine, checked logical simplification, not an
  assumption. (2) Step 8.8 performs the dispatched symmetry check (does the joint
  argument transfer to B'-occurrences after n_B without modification) and finds NO
  obstruction: the proposed Blocking-Data Bridging mechanism (owned by the sibling,
  still open) is side-agnostic — it only uses a term's own predecessors and the
  side-agnostic Finite Core Theorem, never n_B's specific minimality (unlike the
  sibling's separate, flagged step 2) — so a single proof (still open) gives both FAH
  and Symmetric FAH in canonical form. Also resolved the apparent cutoff mismatch
  (n>n_B vs n>n_A) as purely notational. (3) Step 9 gives the untouched-since-round-1
  secondary "periodicity from n=1" gap its first substantive treatment: proved the
  Exact-Equality Reduction Lemma (the gap is EXACTLY N₀−1 explicit equalities, Step
  9.1); proved, via an explicit counterexample (a strictly increasing sequence
  eventually periodic from N₀=3 with NO valid global period for any n≥1), that this
  reduction is NOT automatically satisfied for a general eventually-periodic integer
  sequence — correcting this round's outline, whose proposed "period-rescaling"
  mechanism is not unconditionally valid (Step 9.2); and documented a candidate
  strategy (residue-driven rule holding from the start) together with its precise,
  unresolved point of failure (Step 9.3). Neither the FAH/Symmetric FAH crux nor the
  n=1 gap is closed this round; both are narrowed and more precisely localized than
  before, with two new fully-proved general-purpose lemmas (Canonicalization,
  Symmetry-Transfer Check) and two new fully-proved general facts about periodicity
  (Exact-Equality Reduction Lemma, Non-Automaticity of Prefix Folding) recommended for
  certification. Status remains `partial`.
- **Round 8 (this round): carried out the dispatched Fixed-Witness Divisor-Chain
  mechanism in full (Step 8.9) and found it does not close Joint FAH.** Proved the
  divisor-chain object's well-definedness unconditionally, then followed the
  outline's Key Lemma argument line by line to find and prove a genuine gap in its
  proposed dichotomy: the branch "the pigeonholed escaping prime r lies in S₀ ⟹
  contradicts rogueness" is false (r ∈ S₀ only forces the tautological r ∈ A', with
  no bearing on rogueness) — a gap that is more basic than, and independent of, the
  canonicality sub-step the outline-reviewer flagged. Extracted, as an honest
  byproduct, a genuinely new unconditional lemma (Singleton-Side FAH: if the far
  witness's outside-core factor set is a singleton, cofinite — in fact total —
  divisibility on the near side follows immediately from the already-certified
  Generalized Bounded Witness Lemma with no pigeonhole needed) and showed this Lemma
  fully explains this round's (and the outline-reviewer's) positive computational
  examples (a_1=187, 209, both singleton on both sides), meaning none of the tested
  evidence engaged the genuinely open |F'|,|F''| ≥ 2 regime — confirmed by a fresh,
  independent a_1=4807 computation at an un-recruited core where the analogous claim
  fails on 751/801 sampled occurrences. Also continued Step 9.3/9.4 (secondary n=1
  gap): found and documented that its proposed direct-verification strategy is not
  yet well-posed, since its inputs (final S₀, L, G) are only available once Joint
  FAH is resolved — a genuine dependency, not a new independent obstruction. Joint
  FAH itself remains open; Status stays `partial`.

### Step 8.9 — Round 8: the Fixed-Witness Divisor-Chain object (full proof of the
object's well-definedness), the Key Lemma attempted exactly as dispatched, and a
precisely located, honestly documented failure — distinct from, and prior to, the
outline-reviewer's flagged canonicality gap

This section carries out this round's dispatched mechanism (Fixed-Witness
Divisor-Chain, scoped to Lemma-G rogue-pair witnesses) as far as it rigorously goes.
It (a) proves the divisor-chain object is well-defined with no gap, (b) attempts the
Key Lemma exactly as the outline states it, (c) finds and proves a genuine logical
gap in the outline's Step 3 dichotomy that is MORE BASIC than the canonicality
question the outline-reviewer flagged (it applies even before that question becomes
relevant), and (d) isolates, as an honest byproduct, exactly which special case the
mechanism DOES close unconditionally, and why the empirical support reported by the
outline-reviewer is fully explained by that special case rather than by new content.

**Setup (recall).** Fix a rogue pair of disjoint-base-type extended-persistent types
(A', B') at the current core S₀, with canonical (earliest) witnesses n_A, n_B
(WLOG n_A < n_B; the case n_B < n_A is symmetric with the roles of A', B' and their
witnesses swapped throughout — this covers both orderings, so no case is omitted).
By Lemma G (Extended Earliest-Witness Intersection, certified,
`lemmas/extended-earliest-witness-intersection.md`) there is a prime q ∉ S₀ with
q | a_{n_A} and q | a_{n_B}. Set F' := P(a_{n_A}) \ S₀, F'' := P(a_{n_B}) \ S₀ (both
finite, nonempty, q ∈ F' ∩ F''). Define the canonical prime q* := min(F' ∩ F'') (a
well-defined positive integer since F' ∩ F'' is a finite nonempty set of primes,
regardless of whether |F' ∩ F''| = 1 or ≥ 2 — this handles both cases named in the
outline's "Cases to cover," e.g. the a_1 = 4807 seed where |F' ∩ F''| can exceed 1).

**Definition (Fixed-Witness Divisor-Chain).** For every n > n_A with ρ(n) = A' (ρ the
S₀-extended type), define d_n := gcd(a_{n_A}, a_n).

**Lemma (Divisor-Chain Well-Definedness).** d_n is, for every such n, a divisor of
the FIXED positive integer a_{n_A} satisfying d_n > 1; in particular, as n ranges over
the (infinite, since A' is extended-persistent) set of A'-type indices beyond n_A,
d_n ranges over a subset of the FINITE set Div(a_{n_A}) \ {1} of divisors of a_{n_A}
exceeding 1.

*Proof.* d_n = gcd(a_{n_A}, a_n) divides a_{n_A} by definition of gcd, for every n.
Since a_{n_A} is one fixed positive integer, Div(a_{n_A}) is finite (`knowledge_base.md`
"Divisor analysis", Number Theory section — the number of divisors of a positive
integer m is finite, bounded by 2√m or by the standard divisor-count formula on m's
factorization). By the certified Free Facts lemma (`free-facts-gcd.md`), gcd(a_i,a_j)>1
for all i≠j; applying this with i = n_A ≠ n = j (valid since n > n_A) gives d_n > 1. ∎

This is a complete, unconditional, elementary proof with no gap — the divisor-chain
object is exactly as advertised: finitely many possible values, all exceeding 1, fixed
once n_A (hence a_{n_A}) is fixed, independent of how large n grows. (This matches the
outline's Step 2 claim exactly; nothing here is new content beyond formalizing it, but
it is stated fully rigorously as the base for what follows.)

**Attempted Key Lemma (Exception Finiteness via Fixed-Witness Pigeonhole), exactly
as dispatched.** *Claim (not established — see the gap below): q* | d_n for all but
finitely many A'-type n > n_A.*

*Attempted proof, following the outline's Step 3 verbatim, to find exactly where it
breaks.* Suppose, for contradiction, that q* ∤ a_n for infinitely many A'-type n > n_A
(this is equivalent to q* ∤ d_n for the same infinite set of n: since q* | a_{n_A}
already — q* ∈ F' means q* | a_{n_A} by definition of F' = P(a_{n_A})\S₀ — the
q*-adic valuation of d_n = gcd(a_{n_A}, a_n) is min(v_{q*}(a_{n_A}), v_{q*}(a_n)),
which is ≥ 1 exactly when v_{q*}(a_n) ≥ 1, i.e. exactly when q* | a_n; this
equivalence is an elementary valuation computation, fully justified). Call this
infinite index set E (the "exceptional" A'-type indices with q* ∤ a_n, n > n_A).

For each n ∈ E, d_n is, by the Divisor-Chain Well-Definedness Lemma, an element of
the FINITE set Div(a_{n_A}) \ {1} that is additionally not divisible by q* (since
q* ∤ d_n for n ∈ E, as just shown) — call this finite set Div₀ := {d ∈ Div(a_{n_A}) :
d > 1, q* ∤ d}. Since E is infinite and Div₀ is finite, by the infinite pigeonhole
principle (`knowledge_base.md` "Pigeonhole / extremal principle") there is a single
fixed value d ∈ Div₀ with d_n = d for infinitely many n ∈ E. Fix such an infinite
subset E_d ⊆ E with d_n = d for all n ∈ E_d. Since d > 1, d has at least one prime
factor; fix any prime r | d. Since r | d | a_{n_A}, r | a_{n_A}. Since r | d = d_n =
gcd(a_{n_A}, a_n) | a_n for every n ∈ E_d, r | a_n for every n ∈ E_d, an infinite set.
Also r ≠ q* (since q* ∤ d but r | d, so r ≠ q*, as q* would divide d if r = q*).

*This is exactly as far as the outline's Step 3 goes before its proposed dichotomy.
Now examine that dichotomy directly.*

**The gap, precisely identified (prior to and independent of the canonicality
question).** The outline proposes: "either (a) r ∈ S₀ already, contradicting that
(A',B') is a rogue (not-yet-safe) pair at S₀ ... or (b) r ∉ S₀ ...". **Branch (a) of
this dichotomy is FALSE as a general claim — it does not yield a contradiction, and
I can prove this directly, not just flag it as unclear:**

*Proof that branch (a) yields no contradiction.* Suppose r ∈ S₀. Since r | a_{n_A}
and r ∈ S₀, r ∈ P(a_{n_A}) ∩ S₀ = ρ(n_A) = A' (using ρ(n_A) = A', the defining
property of n_A as A''s canonical witness). So r ∈ A'. But by definition of the
extended type, EVERY index n with ρ(n) = A' automatically satisfies r | a_n for every
r ∈ A' (since ρ(n) = P(a_n) ∩ S₀ = A' means, in particular, every element of A'
divides a_n). So "r | a_n for infinitely many n ∈ E_d" — indeed for ALL A'-type n,
not just those in E_d — is an automatic, content-free consequence of r ∈ A' ⊆ S₀; it
uses no information about E_d, q*, or rogueness at all, and in particular gives NO
contradiction with (A', B') being a rogue (not-yet-safe) pair at S₀ (rogueness is
about A' ∩ B' = ∅, a statement about primes of S₀ shared between A' and B'
specifically — r ∈ A' alone says nothing about whether r ∈ B', so it is entirely
consistent with A' ∩ B' = ∅ for r to be an ordinary element of A' with r ∉ B'). ∎

So the outline's claimed dichotomy is not a valid case split for deriving a
contradiction: **the pigeonholed prime r produced by this construction could simply
be an already-known S₀-prime of A' itself, in which case the entire argument
collapses to a tautology (every A'-type term is divisible by every prime of A',
trivially) and supplies no information whatsoever about whether q* | a_n for the
exceptional n ∈ E**, let alone a contradiction. This gap is **prior to and
independent of** the outline-reviewer's flagged canonicality concern (ordering of r
vs. q*, and whether r ∈ F''): that concern only becomes relevant once r is known to
be a genuinely NEW prime (r ∉ S₀), and nothing in the argument as given forces this.
**Neither this round's construction, nor any certified lemma in the current stack
(Free Facts, the (Generalized) Bounded Witness Lemma, Divisor-Restricted Pigeonhole,
Critical Prime Dichotomy), rules out r ∈ A' ⊆ S₀ as the pigeonhole's outcome.** I
looked for an argument to force r ∉ S₀ and did not find one: Free Facts only
guarantees SOME shared prime between a_{n_A} and a_n (already true, and already
witnessed trivially by any element of A' itself, since a_{n_A} and every A'-type a_n
both carry every prime of A' by definition of the type) — it supplies no reason the
"extra," outside-A' part of the gcd must be nonempty for infinitely many exceptional
n. **This is a genuine, honestly-reported failure of the Key Lemma as dispatched,
found by carrying the argument through in full rather than assumed.**

**What can be salvaged unconditionally: the Singleton-Side Lemma.** Although the
general Key Lemma does not go through, the following restricted, fully rigorous,
unconditional statement DOES follow directly from already-certified machinery (no
pigeonhole gap):

**Lemma (Singleton-Side FAH).** If F'' (the far witness's outside-core factor set)
is a singleton, F'' = {q}, then q | a_n for EVERY n > n_B with ρ(n) = A' (not merely
cofinitely — literally every occurrence, zero exceptions).

*Proof.* By the certified Generalized Bounded Witness Lemma (`generalized-bounded-
witness-lemma.md`), for every n > n_B with ρ(n) = A', a_n is divisible by some prime
of F_{A',B'} = P(a_{n_B}) \ S₀ = F''. Since F'' = {q} has only one element, that
prime must be q itself. So q | a_n for every such n, with no exceptions. ∎ This
argument uses only the certified Generalized Bounded Witness Lemma directly (no new
pigeonhole, no divisor-chain object needed) and is completely unconditional whenever
the hypothesis |F''| = 1 holds. Symmetrically, if |F'| = 1, the same argument
(swapping the roles of A', B') gives the analogous B'-side (Symmetric FAH)
conclusion.

**This Lemma exactly and fully explains this round's positive computational
findings, showing they are NOT independent confirmation of new mechanism content.**
I recomputed, from scratch, two documented rogue-pair examples used as supporting
evidence this round:
- a_1 = 187: Q = {11,17}, rogue pair A' = {3,11}, B' = {2,17}, n_A = 5, n_B = 6. Fresh
  simulation: a_5 = 231 = 3·7·11, a_6 = 462 = 2·3·7·11·... ; F' = P(a_5)\S₀ = {7},
  F'' = P(a_6)\S₀ = {7}. Both F' AND F'' are singletons, equal to {7}. By the
  Singleton-Side Lemma (both directions), q = 7 divides EVERY later occurrence of A'
  (after n_B) and EVERY later occurrence of B' (after n_A) unconditionally — this is
  not evidence for the divisor-chain mechanism; it is a direct, certified-lemma-only
  consequence, independent of any pigeonhole argument. I confirmed computationally
  (fresh simulation, 46 A'-type occurrences past n_A, 0 exceptions) that this holds
  exactly as the Lemma predicts.
- a_1 = 209: three rogue pairs, all with F' = F'' = {7} (singleton on both sides in
  every instance found) — same conclusion, same explanation, reconfirmed on 38, 38,
  41 occurrences respectively with 0 exceptions.
- By contrast, a_1 = 4807 (on record, `current.md` ROUND 6, as having |F'| ≥ 2 on
  (at least) one side of its rogue pair) is exactly the case the Singleton-Side Lemma
  does NOT cover, and is exactly the case where the general Key Lemma's gap (the
  r ∈ S₀ / r ∈ A' collapse identified above) is a live possibility, not a
  hypothetical one. I attempted a fresh computation on this seed this round: at the
  smaller core S₀ = Q (before the Finite Core Theorem's own recruitment is applied),
  base types {19} and {11} at n_A=6, n_B=7 give F' = {17,3,5}, F'' = {17,2,13}, with
  shared prime 17 — but only 50/801 sampled later {19}-type occurrences are divisible
  by 17 (751 exceptions), i.e. no cofinite-divisibility claim holds at this
  un-recruited core, exactly as expected since the Finite Core Theorem's own
  recruitment step has not yet been applied here. This confirms, independently, that
  the |F'|,|F''| ≥ 2 regime (reached only after proper core recruitment) is where the
  real difficulty of FAH lives, and no shortcut through it was found this round.

**Honest conclusion for Step 8.9.** The Fixed-Witness Divisor-Chain mechanism, as
dispatched, does NOT establish the Key Lemma (Exception Finiteness) in general: its
proposed dichotomy has a genuine gap (branch (a), "r ∈ S₀ ⟹ contradiction," is false
— r ∈ S₀ merely means r ∈ A', a tautological, information-free outcome, not a
contradiction) that is more basic than, and independent of, the canonicality
sub-question the outline-reviewer flagged for branch (b). What the mechanism DOES
give, unconditionally and with a complete proof, is the Singleton-Side Lemma — a
direct, certified-lemma-only special case that fully explains every one of this
round's supporting computational examples, all of which turn out to have F' or F''
a singleton. This is a real, if modest, addition: it cleanly isolates that the
mechanism's apparent empirical support was never testing the genuinely hard
(|F'|,|F''| ≥ 2) case, and it gives a fully rigorous unconditional sub-case of Joint
FAH (the singleton sub-case) as a byproduct. **Joint FAH itself, in the general
(non-singleton) case, remains open**, and this round's attempt to close it via the
Fixed-Witness Divisor-Chain does not succeed — this is reported honestly, per
CLAUDE.md's rigor rules, rather than papered over.

### Step 9.4 — Round 8: continuation of the secondary n=1 gap (Step 9.3)

Per this round's dispatch, I attempted the proposed direct-verification strategy for
the secondary gap using the certified Exact-Equality Reduction Lemma
(`lemmas/exact-equality-reduction-lemma.md`): periodicity from n=1 holds iff the
finitely many equalities a_{i+T} = a_i + L hold for i = 1,...,N₀−1, where N₀, T, L
are as constructed in Step 5. The outline's proposed approach was to show each small
i's S₀-signature already lies in the eligible-residue set G (defined purely by
S₀-signature mod L) directly, turning the check into a finite computation.

**Obstruction found (honestly reported, not closed).** This strategy is logically
sound in principle — G is indeed a static congruence-class condition, meaningful for
any n including small n, not only in the "eventually persistent" regime — but it is
**downstream of, and inherits, the SAME open gap as Step 8.9 above**: the set G, the
core S₀, and the value L = ∏_{p∈S₀} p are only fully pinned down once the recruitment
process (equivalently, Joint FAH) is known to terminate — S₀ itself is not fully
determined without knowing which recruitment rounds, if any, are needed for every
disjoint base-type pair (Step 4c's process). Concretely: to check "does a_i's
S₀-signature mod L lie in G" for i = 1,...,N₀−1, one first needs the FINAL S₀ (post
all recruitment), which is not available without resolving Joint FAH. I therefore
cannot yet carry out even the finite check the outline proposes, because its
input (S₀, L, G) is not yet unconditionally computable in general. This is a
genuine dependency, not a new independent obstruction: closing Step 8.9's gap (Joint
FAH) would make Step 9.4's finite check well-posed and directly attackable by
brute-force verification (a finite computation, not requiring new theory) once N₀,
S₀, L are fixed. I record this dependency explicitly so a future round does not
attempt Step 9.4 in isolation before Joint FAH is resolved, and does not mistake this
for an additional, separate open question beyond Joint FAH plus the already-certified
Exact-Equality reduction.

**Net effect on the secondary gap:** unchanged in substance from round 7 (still
reduced to N₀−1 explicit equalities by the certified Exact-Equality Reduction Lemma,
still not verified), but the further dependency on Joint FAH for even defining the
check's inputs is now made explicit, which was not previously stated as clearly.

## Promotable lemmas

- **Divisor-Chain Well-Definedness** (Step 8.9, this round): for a rogue pair's
  A'-side witness a_{n_A}, d_n := gcd(a_{n_A}, a_n) is, for every later A'-type n,
  a divisor of the fixed integer a_{n_A} exceeding 1, hence takes only finitely many
  values as n ranges over A'-type indices. Short, fully proved, unconditional, no
  dependence on any open hypothesis. Modest but reusable as a clean building block
  for any future divisor-chain-style attack on FAH.

- **Singleton-Side FAH** (Step 8.9, this round): if the far witness's outside-core
  factor set F'' (or, symmetrically, F') of a Lemma-G rogue pair is a singleton
  {q}, then q divides EVERY (not merely cofinitely many) later occurrence of the
  near type on the corresponding side. Fully proved directly from the already-
  certified Generalized Bounded Witness Lemma, unconditional, no pigeonhole needed.
  Recommend certifying this as it gives, for free, a genuine special case of Joint
  FAH (the |F'|=1 or |F''|=1 sub-case) that any future attack on the general case
  can assume already handled, and it correctly explains why the outline-reviewer's
  and this round's own positive computational checks (a_1=187, 209) do not yet
  constitute evidence for the general (|F'|,|F''|≥2) case.

- **Non-validity of the "r ∈ S₀ ⟹ contradiction" branch** (Step 8.9, this round):
  a negative but precise finding — in any pigeonhole argument over divisors of a
  fixed witness a_{n_A} of an extended-persistent type A', producing a prime r that
  divides a_{n_A} and infinitely many later A'-type terms, r ∈ S₀ does NOT yield a
  contradiction with (A',B') being a rogue pair; it only forces the tautological
  r ∈ A' (automatic for every element of A' by definition of the extended type),
  which carries no information about B' or rogueness. Recommend recording this (in
  the spirit of the round-3 Lemma F / round-6 Lemma I precedent for portable
  negative guidance rather than a standalone lemma file) so future FAH-mechanism
  attempts do not repeat this exact dichotomy error.

### Step 10 — Round 9: the Recruitment-Budget Lemma, mandatory Step-4 computational
check, and its refutation

This round's dispatch reframes the open FAH/recruitment-termination gap (equivalently,
the halting question for Step 4c's recruitment process, or the residual set V of Step
4f) as a **global counting-budget bound**: instead of trying to force one witness-level
existential-to-universal promotion (the mechanism Lemma I already diagnosed as dead six
times over, most recently round 8's Fixed-Witness Divisor-Chain), bound the TOTAL number
of distinct primes the recruitment process can ever pull in, against a fixed
disjoint-base-type pair, by an explicit finite pool computable from Q-level data alone.
Per the dispatch's explicit instruction, the mandatory first deliverable is a
computational check, run before any proof effort; I carried this out and it refutes the
proposed Lemma. The full account follows.

**Definitions (restating the target precisely, in this file's own notation).** Fix a
disjoint persistent base-type pair (A, B) ∈ 𝒫 × 𝒫 (A ∩ B = ∅), with base-type earliest
witnesses m_A := min{n : τ(n) = A}, m_B := min{n : τ(n) = B} (both exist since A, B are
persistent — these are exactly the canonical witnesses of Step 3/4d, defined once and
for all at the Q-level, independent of any later core-recruitment stage). Define the
**fixed Q-level pool**

  W_{A,B} := P(a_{m_A}) ∪ P(a_{m_B}),

a specific finite set of primes, fully determined by a_1 and two specific, explicitly
identifiable terms of the sequence — computable without running any part of the
recruitment process.

Recall Step 4c's recruitment process: S₀^(0) := Q; at stage k, if every pair of
S₀^(k)-extended-persistent refinements of every disjoint base-type pair intersects, the
process halts; otherwise, by the Generalized Bounded Witness Lemma's Corollary
(`lemmas/generalized-bounded-witness-lemma.md`, certified), some violating pair
(A', B') — refinements of some disjoint base pair (A,B) — yields a specific NEW prime
q ∉ S₀^(k), and S₀^(k+1) := S₀^(k) ∪ {q}.

**Recruitment-Budget Lemma (the round's target, as dispatched).** For every disjoint
base-type pair (A,B) and every stage k of the process, every prime q recruited at stage
k against a violation whose underlying base pair is (A,B) satisfies q ∈ W_{A,B}.

*Why this would close the gap, if true.* W_{A,B} is finite (two explicit integers, each
with finitely many prime factors) and fixed independently of k (computable from a_1 and
the two base-type witnesses alone, before any recruitment). If every prime ever
recruited against (A,B) lies in the fixed finite set W_{A,B}, and each recruitment round
against (A,B) strictly enlarges S₀^(k) ∩ W_{A,B} by at least one new element (the
recruited prime, which is by hypothesis in W_{A,B} and, being freshly recruited, was not
already in S₀^(k)), then the number of rounds needed to fully resolve (A,B) is bounded
by |W_{A,B}|, a computable finite number — forcing termination of the whole process
(finitely many base pairs, each needing finitely many rounds) by pure pigeonhole, with
no absorption, cofinite-divisibility, or density content required at all.

**Mandatory Step-4 computational check (carried out exactly as dispatched, before any
proof attempt).** I implemented a direct, from-scratch, round-by-round simulation of the
recruitment process (trial-division factorization; script `/tmp/round-9/work/
sim_budget.py`, independent of any prior round's script): given a_1, it (i) generates
the greedy sequence to N terms; (ii) computes Q, the Q-level persistent base types 𝒫
(types occurring ≥ 3 times in the tail half of the generated terms, used as an explicit,
checkable proxy for "occurs infinitely often" — I additionally re-ran every case at two
different values of N to confirm the occurrence counts scale proportionally with N,
ruling out a finite-window sampling artifact, not just asserting persistence from one
window); (iii) computes the base-type witnesses m_A and the pools W_{A,B} for every
disjoint pair; (iv) runs the recruitment process literally, round by round: at each
stage k, computes S₀^(k)-extended-persistent types 𝒫'_k from the tail, finds a violating
pair, extracts the earliest witness of the violating pair's "B-side" extended type AT
THE CURRENT STAGE (exactly matching the Generalized Bounded Witness Lemma's Corollary's
own construction — "fix any witness index m with ρ(m) = B′"), determines the prime the
pigeonhole corollary would select (the element of P(a_m) \ S₀^(k) dividing the most
A'-type occurrences in the sampled tail, as a proxy for "responsible for infinitely
many"), and checks membership of this recruited prime in the FIXED pool W_{A,B} built
from the base-type (not extended-type) witnesses. I ran this on seven seeds spanning
|Q| = 2 to |Q| = 4 (a_1 = 175, 35, 187, 209, 247, 4807, 11305), at N = 4000–15000.

**Result: REFUTED, with an explicit small counterexample.** Take a_1 = 209 = 11 · 19
(Q = {11, 19}). Direct computation of the first several terms of the sequence (verified
by hand, trial division):

  a_1 = 209 = 11·19,  a_2 = 220 = 2²·5·11,  a_3 = 228 = 2²·3·19,  a_4 = 231 = 3·7·11.

*(Verification that these are the correct greedy terms: a_2 must be the smallest
integer > 209 sharing a prime factor with 209 = 11·19; 210,...,219 are checked and
fail — e.g. 210=2·3·5·7 shares no factor with 11·19 — and 220 = 2²·5·11 shares 11.
a_3 must additionally share a factor with a_2 = 220 = 2²·5·11 as well as with a_1;
221=13·17 shares neither, ..., 228 = 2²·3·19 shares 2 with a_2 and 19 with a_1. a_4
must share a factor with all of a_1,a_2,a_3; 229 is prime, 230=2·5·23 shares 2 and 5
with a_2 but not 19 or 11 with a_1/a_3 — wait 230 does not share a factor with a_1=209
(gcd(230,209)=1 since 209=11·19, 230=2·5·23, no common factor) so 230 is illegal;
continuing, 231 = 3·7·11 shares 11 with a_1, 11 with a_2 (220=2²·5·11, shares 11), and 3
with a_3 (228=2²·3·19, shares 3) — legal, and no integer in 221..230 is legal by the
same direct check, so a_4 = 231.)*

Base type of a_2: τ(2) = P(220) ∩ Q = {11}. Base type of a_3: τ(3) = P(228) ∩ Q = {19}.
These are (confirmed by the simulation's tail count, and consistent with Q = {11,19}
admitting only the three types {11}, {19}, {11,19}) the earliest occurrences of the two
persistent proper base types, so m_A = 3 (base type {19}), m_B = 2 (base type {11}) —
using labels A := {19}, B := {11} to match the simulation's round-2 output. Then

  W_{A,B} = P(a_{m_A}) ∪ P(a_{m_B}) = P(228) ∪ P(220) = {2,3,19} ∪ {2,5,11} = {2,3,5,11,19}.

Now trace the recruitment process:

- **Round 0** (S₀^(0) = Q = {11,19}): base types {11}, {19} are trivially disjoint as
  sets (distinct singletons), so this is a violation at the extended level too (extended
  type = base type when S₀ = Q). The Corollary's witness for the B-side ({11}) is, by
  construction, exactly m_B = 2 (the earliest occurrence of {11}, since at S₀ = Q the
  "earliest occurrence of extended type {11}" IS the earliest occurrence of base type
  {11} — no refinement has happened yet). F' = P(a_2) \ Q = {2,5}; the process selects
  q = 2 (dividing more A-type occurrences in the sampled tail). Since q = 2 ∈ W_{A,B},
  this round is consistent with the Lemma.
- **Round 1** (S₀^(1) = {2,11,19}): the violating extended types are now {11} (still,
  base A-side) and {2,19} (the refinement of base type {19} now known to be divisible by
  2). The witness for {2,19} at this stage is again a_3 = 228 (since 2 | 228 already,
  a_3's extended type at S₀^(1) is exactly {2,19} — no discontinuity yet). F' =
  P(a_3) \ S₀^(1) = {3}; q = 3 ∈ W_{A,B} = {2,3,5,11,19}. Still consistent.
- **Round 2** (S₀^(2) = {2,3,11,19}): the violating extended types are {2,19} (refining
  base {19}) and {11,3} (refining base {11}). Here the discontinuity strikes: the
  earliest occurrence of extended type {11,3} at this core level is **not** a_2 = 220
  (whose extended type at S₀^(2) is {2,11}, since 2 | 220 — it does NOT carry the prime
  3), but a_4 = 231 = 3·7·11 (the first term whose S₀^(2)-signature is exactly {3,11}).
  So the Corollary's witness is m = 4, and F' = P(a_4) \ S₀^(2) = {7}; the process must
  recruit q = 7. But **7 divides neither a_2 = 220 nor a_3 = 228**, so
  7 ∉ W_{A,B} = {2,3,5,11,19}. The Recruitment-Budget Lemma **fails** at this round.

This is a complete, hand-verifiable, four-term counterexample (I additionally confirmed
computationally, at N = 15000, that the occurrence counts underlying "A-type" and the
choice of q = 7 as the pigeonhole-selected prime scale proportionally with N — 284 out
of a large tail-sample at N=15000 vs. 113 at N=6000 vs. smaller at N=4000, all
consistent linear growth, ruling out a finite-window artifact; the same escape,
q = 7 ∉ W_{A,B}, is reproduced at every tested N).

**The same phenomenon recurs, is robust, and is not confined to "late" rounds.** I
confirmed the escape (recruited prime outside the base-witness pool) on five of the
seven tested seeds (187, 209, 247, 4807, 11305 — all requiring ≥ 3 recruitment rounds
for at least one disjoint base pair), at both N = 4000/6000 and N = 15000 with
proportionally scaling occurrence counts, and its absence on the two seeds needing only
1–2 rounds (175, 35) where every recruited prime happened to still be traceable to a
base-type witness. Notably, for a_1 = 247 the escape already occurs at **round 1** (not
round 2): the earliest occurrence of the extended type {19} pure (no 2) at S₀^(1)
shifts away from the base-type witness a_2 (which turns out to already be divisible by
2), to a_5, whose extra prime factor 3 is not in W_{{13},{19}} — so the failure is not
an artifact of "deep" rounds specifically; it occurs as soon as ANY base-type witness
happens to itself carry a previously- or newly-recruited prime, shifting the "earliest
pure occurrence" of its own refined type forward to a different, uncontrolled integer.

**Diagnosis: this is exactly the certified Witness Discontinuity Obstruction, now shown
to directly break this specific proposed mechanism (not merely to be an abstract risk).**
The certified `lemmas/witness-discontinuity-obstruction.md` already establishes, via its
own a_1 = 175 example, that "the earliest witness of a fixed extended-persistent type"
is not continuous under core enlargement. The outline's own "Watch out for" note flagged
this as the exact risk to check before trusting the Lemma; the round-9 check confirms
the risk is realized: the Generalized Bounded Witness Lemma's Corollary, by its own
proof (`lemmas/generalized-bounded-witness-lemma.md`), always extracts its recruited
prime from "any witness index m with ρ(m) = B′" **at the current stage** — and there is
no argument (nor, per the Witness Discontinuity Obstruction, could there be one in
general) forcing this current-stage witness to coincide with, or have a factorization
controlled by, the original base-type witness a_{m_B}. Once the core has grown past
round 0, the current-stage witness for a refined type can be an entirely different
integer than a_{m_A}, a_{m_B}, with entirely uncontrolled extra prime factors.

**Why the natural "rescue" (enlarge the pool) does not save the mechanism, and is not
pursued.** Per the dispatch's explicit instruction not to "silently expand the pool ad
infinitely without proving it is still finite and independent of k," I checked the
obvious fix: redefine W_{A,B} to include the primes of every witness actually used
during the ENTIRE recruitment history for the pair (A,B), i.e. W'_{A,B} :=
P(a_{m_A}) ∪ P(a_{m_B}) ∪ P(a_{m}) ∪ P(a_{m'}) ∪ ... over every witness index m the
process happens to select at every round. This is finite for any INDIVIDUAL fixed run
of the process (only finitely many rounds occur before halting, each selecting one
witness), but it is **circular as a proof strategy**: which indices m, m', ... get
selected as witnesses at rounds 1, 2, ... is itself determined by running the
recruitment process — the very object whose termination is the open question. Defining
"the pool" as "whatever the process happens to touch" gives no a priori, Q-level-only
computable bound; it is a restatement of "the process eventually stops touching new
integers," which is only true if the process terminates — exactly the fact we set out
to prove. This is not a new insight but the general failure mode already catalogued
under Step 4c/4f ("reconciled pairs stay reconciled... I was not able to show a single
round's recruitment fully settles a whole base-type pair") and Step 4f's minimal-
counterexample route 1 (the natural measure — here, "how much of the pool is still
Q-level-computable in advance" — only shrinks by giving up the very property, a priori
finiteness independent of the process, that made the Lemma useful in the first place).
I record this explicitly rather than silently trying it and hoping it works, per the
dispatch's caution.

**What is preserved, and what remains open.** No previously certified result is
affected: the Free Facts, Bounded/Generalized Bounded Witness Lemmas, Finite Core
Theorem, Projection Lemma, Collateral-Safety Theorem, Canonical-Refinement Lemma, and
Lemma G all stand exactly as certified — the refutation is entirely of this round's
NEW proposed Lemma, not of anything in the existing chain. The open gap remains exactly
as localized by Step 4f: termination of the recruitment process (equivalently, V = ∅
for the residual set of non-canonical violating pairs), now with an eighth diagnosed-dead
mechanism (global base-witness counting budget) added to Lemma I's list of six, plus
round 8's Fixed-Witness Divisor-Chain. The common thread across all eight failures is
the same: every mechanism tried either (a) needs a single witness's property to persist
across infinitely many, or arbitrarily many, occurrences/rounds of a type without
control over which specific occurrence supplies the certifying data (Lemma I's
diagnosis), or (b) needs "the earliest/canonical witness" to remain stable under core
refinement, which the certified Witness Discontinuity Obstruction rules out in general.
Any future mechanism for this gap must avoid both failure modes — in particular, it
cannot rely on tracking a SINGLE distinguished witness (base-type earliest occurrence,
extended-type earliest occurrence, or any other single-index choice) across the
unbounded-looking recruitment process; it likely needs to argue about the FULL infinite
family of occurrences of a type jointly (as Step 4f's route-2 diagnosis already
suggested), not about any one witness's factorization.

## Promotable lemmas (round 9 addendum)

- **Refutation of the Recruitment-Budget Lemma (Step 10, this round)** — a precise,
  reusable NEGATIVE finding, in the spirit of the round-3 Lemma F / round-6 Lemma I /
  round-8 "r ∈ S₀" precedent: the fixed, Q-level, base-witness-only pool
  W_{A,B} := P(a_{m_A}) ∪ P(a_{m_B}) does **not** contain every prime the Generalized
  Bounded Witness Lemma's Corollary can recruit against the pair (A,B) over the course
  of the recruitment process — an explicit, hand-verifiable four-term counterexample
  (a_1 = 209, escaping prime q = 7 at the process's second round) is given in Step 10.
  Recommend recording this so future approaches do not re-attempt a global counting
  budget anchored to base-type (or any other single, a-priori-fixed) witnesses without
  first checking this exact escape mechanism, which is a direct, concrete instance of
  the already-certified Witness Discontinuity Obstruction. The escape is shown (five of
  seven tested seeds, robust across sample sizes with proportionally scaling occurrence
  counts) to be the generic case whenever a base pair needs ≥ 2 recruitment rounds, not
  a rare edge case, and can strike as early as round 1 (a_1 = 247) when a base-type
  witness itself already carries a recruited prime.
- **Circularity of the "expand the pool to whatever the process touches" rescue**
  (Step 10, this round) — recorded explicitly per the dispatch's caution against
  silently patching a refuted finite-pool claim: any redefinition of W_{A,B} to include
  primes of witnesses selected DURING the recruitment process (rather than fixed in
  advance from Q-level data) is finite only if the process itself is already known to
  terminate, so it cannot serve as an independent proof strategy for termination — it
  restates the open question rather than answering it. Worth recording so this specific
  patch is not silently retried.

## Cheap-kill computational artifacts (round 9)

Script: `/tmp/round-9/work/sim_budget.py` (trial-division factorizer, round-by-round
recruitment-process simulator, independent of prior rounds' scripts). Verified against
seven seeds (a_1 = 175, 35, 187, 209, 247, 4807, 11305) at N ∈ {4000, 6000, 15000}. The
counterexample data for a_1 = 209 (Step 10's main example) and a_1 = 187/247 (corroborating
examples) is reproducible by re-running this script; the hand-verification of a_1 = 209's
first four terms is spelled out in full in Step 10 so it does not depend on trusting the
script.

## ROUND 10 — Step 11: Growth-Forced Divisibility (aimo-0680-style AP-identity,
adapted to a magnitude squeeze) for Joint Cofinite FAH

### 11.0 Why this is a genuinely new mechanism, not a repackaging

Lemma I's diagnosis (round 6, re-verified every round since) is precise: none of
Free Facts, the Generalized Bounded Witness Lemma, the Gap Lemmas (used only as an
EXISTENCE bound), or Critical Prime Dichotomy contains a step that LINKS two
different occurrences' divisor-class data (`g_n` for different `n`) to each other.
This round's mechanism is the first to use the Generalized Bounded Gap Lemma
QUANTITATIVELY — as a numeric ceiling on how far apart in VALUE two occurrences of
the same type can be relative to their INDEX gap — combined with the certified
Confined-GCD Lemma's finite alphabet `Div(b)`. This is exactly the adaptation two
independent math-explorers (analytic, crux-mining) converged on this round: aimo-0680's
literal template needs a global algebraic identity (`n | f^n(m)-m`) our greedy rule
structurally lacks (confirmed independently by both explorers via a direct structural
comparison — our recursion is an existential/minimality SEARCH, not a closed-form
map), so the identity must be MANUFACTURED from the one piece of exact global
structure we do have: `a_{n+1} ≤ a_n + a_1` (Bounded Gap Lemma) and its generalization
`a_{n+1} ≤ a_n + c` for any `c` divisible by every prime of `Q` (Generalized Bounded
Gap Lemma, `lemmas/generalized-bounded-gap-lemma.md`).

### 11.1 Imported setup (unchanged, certified)

Fix a currently-rogue pair `(A',B')`, witnesses `n_A<n_B`, canonical prime
`q* := min(F'∩F'')` (Lemma G, nonempty). Import verbatim, as already certified and
independently re-verified (round 9):
- **Confined-GCD Lemma** (`lemmas/confined-gcd-lemma.md`): for every `A'`-occurrence
  `n > n_B`, `g_n := gcd(a_n, a_{n_B})` lies in the FIXED finite set `Div(b)`
  (`b` := the `F''`-part of `a_{n_B}`), and `q*|a_n ⟺ q*|g_n`.
- **Cofinite Sufficiency Lemma** (`lemmas/cofinite-sufficiency-lemma.md`): Cofinite
  FAH (E, E_sym finite) suffices for the whole-problem finish — the target of this
  Step is exactly Cofinite FAH, not literal FAH.

Let `n_1<n_2<...` enumerate the `A'`-occurrences past `n_B`, and let
`E := {j : q* ∤ a_{n_j}}` (equivalently, per Confined-GCD, `g_{n_j} ∈ D_bad :=
{d∈Div(b): d>1, q*∤d}`). Target: `E` finite.

### 11.2 The Growth-Forced Divisibility skeleton (the new mechanism, to be attempted
by the builder — open, not yet proved)

**Step A (magnitude ceiling on the occurrence-index gap).** By the Bounded Gap Lemma,
`a_{n_{j+1}} - a_{n_j} ≤ (n_{j+1}-n_j)·a_1`. Conversely, by the same Lemma applied
telescopically, `a_{n_{j+1}} - a_{n_j} ≥ n_{j+1}-n_j` (each step increases by ≥1).
So the VALUE gap and the INDEX gap are linearly comparable, with constants depending
only on `a_1` — a fully explicit, unconditional fact (elementary consequence of the
already-certified Bounded Gap Lemma, no new lemma needed for this half).

**Step B (candidate identity: divisibility forces an index-gap lower bound — THE KEY
OPEN LEMMA, "Escape-Cost Lemma").** Attempt to show: if `j, j' ∈ E` (both fail
`q*`-divisibility) with `g_{n_j} = g_{n_{j'}} = d` for the SAME bad class
`d ∈ D_bad`, then `n_{j'} - n_j` is bounded BELOW by a quantity growing with `d`'s
"distance" from `q*`-divisibility (e.g., via the multiplicative structure of `Div(b)`:
the smallest legal jump from a `d`-class term to another `d`-class term without ever
passing through a `q*`-divisible candidate, using the greedy rule's OWN minimality —
that skipping every legal `q*`-multiple in a window of length `a_1` around each
`a_{n_j}` is only possible if none of those multiples is legal, which recursively
constrains earlier terms). **This is the genuinely new, NOT-yet-proved sub-lemma the
builder must attempt.** If provable, combined with `D_bad` finite (Confined-GCD) and
`Div(b)` finite, a pigeonhole-then-telescoping argument (à la aimo-0680's exact
"divisor exceeds bounded discrepancy ⟹ discrepancy vanishes" squeeze, but here
applied to COUNT of same-class occurrences instead of a raw integer discrepancy)
would give: each fixed bad class `d` occurs only `O(1)` times (not merely "some
finite number," but a HARD ceiling from the value-vs-index growth comparison of Step
A), hence `E = ⋃_{d∈D_bad} E_d` is a finite union of boundedly-sized sets — finite.
This is the AP-identity-style upgrade, adapted: instead of "two far-apart AP indices
force an exact integer to vanish," it is "two far-apart same-bad-class occurrences
force a magnitude contradiction via the Bounded Gap Lemma's linear ceiling."

**Step C (honest fallback / the concrete cheap-kill the builder must run FIRST).**
Before attempting Step B's general proof, the builder must numerically test its
PREMISE on the existing |F'|,|F''|≥2 seeds (a_1=4807, 11305, and any fresh
properly-recruited-core seed found): track, for the SAME bad class `d ∈ D_bad` (if
`D_bad` is nonempty for that seed — note Section 3 of `cofinite-window-capacity-bound`
found `D_bad=∅` for a_1=11305, meaning Cofinite FAH is already forced unconditionally
there; test seeds where `D_bad≠∅` are needed, i.e., where `Div(b)` has ≥2 primes not
including `q*`), whether repeat occurrences of the same `d`-class are RARE/bounded
(supporting Step B) or can recur arbitrarily close together (refuting Step B as a
cheap kill before any proof effort). This numeric check is new — no prior round
tracked same-class REPETITION rate, only the raw `q*`-divisibility rate.

### 11.3 Key lemmas needed (stated with the mechanism, not yet proved)
- **Escape-Cost Lemma** (Step B): if two `A'`-occurrences share the same bad
  divisor-class `d ∈ D_bad`, their index gap is bounded below by a quantity that
  grows without bound as the number of same-`d`-class repetitions grows — because
  (candidate mechanism) each "escape" (a legal jump skipping every `q*`-multiple in
  the Bounded-Gap-Lemma window) requires a strictly larger local search cost than the
  previous one, since the set of `q*`-multiples already "used up" by earlier terms
  of the SAME extended type shrinks the room for a legal non-`q*` alternative. This
  mechanism is speculative and UNPROVED — flagged honestly, not claimed.

### 11.4 Open gaps
- The Escape-Cost Lemma (Step B) itself — the entire new content of this Step; not
  proved, only motivated and scoped concretely.
- Whether Step A's linear value/index-gap comparability is strong enough to make
  Step B's "growing cost" claim non-vacuous (a genuine risk: linear growth in BOTH
  the value ceiling and the index gap may cancel out, giving no net squeeze — the
  builder must check this arithmetic carefully before investing in the general
  proof, per Step C's numeric premise-check).
- If Step B fails outright (repeat occurrences of the same bad class are NOT rare),
  this mechanism should be retired cleanly with the numeric evidence recorded, per
  CLAUDE.md's honest-failure-reporting rule — do not force a rescue.

### 11.5 Explicitly rejected this round: Return-Time Boundedness as an independent
target (circularity risk investigated and confirmed real)

The analytic math-explorer's numeric finding (a_1=4807's rogue pair has roughly
constant ≈555 occurrence-index gaps) is genuine new data, but a standalone "Return-
Time Boundedness Lemma" (uniform bound `B` on ALL consecutive-occurrence gaps of a
fixed extended-persistent type `A'`, independent of `q*`-divisibility) was
investigated this round and found to be at serious risk of circularity: the only
certified fact about occurrence frequency, Persistent-Type Pigeonhole
(`lemmas/persistent-type-pigeonhole.md`), guarantees ONLY infinitude, with no density
or gap bound of any kind — and the natural route to a gap bound (a CRT/density
argument showing a positive proportion of residues mod the current core `S₀` are
legally reachable) requires exactly the same "eventually, legality is governed purely
by residue mod `S₀`" fact that `reversible-transition-map` (round 5) already proved
is LOGICALLY EQUIVALENT to gap (†) itself. So a general Return-Time Boundedness Lemma
for type `A'` (as opposed to its `q*`-divisible sub-sequence specifically, which is
just a restatement of Cofinite FAH) is not a safe independent target — it either
smuggles in (†) or degenerates to restating the goal. **Not opened as a separate
approach this round; the Step A magnitude comparison above uses only the certified
Bounded Gap Lemma, not any unproved gap-boundedness claim, to avoid this exact
circularity.**

## ROUND 10 — Step 11.5–11.6: the mandatory numeric premise check, and a full proof
that Step B (the Escape-Cost Lemma) is structurally unprovable from Step A alone

Per the dispatch instruction, I ran Step 11.2c's numeric premise check FIRST, before
attempting any general proof of the Escape-Cost Lemma, and confirmed the
outline-reviewer's flagged "linear cancels linear" vacuity risk is real; I then
converted that risk assessment into a full, rigorous impossibility proof rather than
leaving it as a numeric caution.

### 11.5 Numeric premise check (Step C, run against the standing a_1=4807 rogue pair)

**Setup, recomputed from scratch with a fresh trial-division generator (not reusing
any prior script).** For `a_1 = 4807`, I generated the sequence out to `N = 6000`
terms and independently reconfirmed every previously-reported fact for this seed:
`Q = P(a_1) = {11, 19, 23}`, `a_6 = 4845 = 3·5·17·19`, `a_7 = 4862 = 2·11·13·17`
(exact match to every prior round's independent computation of this seed).

I first tried the check at the WRONG level, `S₀ = Q`, to see what happens if the core
is not properly recruited (this is a deliberate control, not the real object of
study): with `A = τ(6) = {19}`, `B = τ(7) = {11}`, `F' = P(a_6)\Q = {3,5,17}`,
`F'' = P(a_7)\Q = {2,13,17}`, `q* = min(F'∩F'') = 17`, `b = 2·13·17 = 442`,
`Div(b) = {1,2,13,17,26,34,221,442}`, `D_bad = {2,13,26}`. Scanning all `1602`
`A`-occurrences (`n > 7`, `τ(n) = {19}`) up to `n=6000`, I found `|E| = 1503`
(94% exceptions) — an enormous failure rate. **This is NOT a counterexample to FAH**
— it exactly reproduces the already-certified scope note attached to the Confined-GCD
Lemma and the round-8 Singleton-Side finding: testing at the un-recruited `S₀ = Q`
level conflates a genuinely rogue EXTENDED-type pair with the much coarser (and here,
not actually rogue in the refined sense) BASE-type pair, and produces a meaningless
high failure rate. I record this here as a methodological confirmation (matching the
outline-reviewer's own note about avoiding a "Q-superset proxy"), not as new content.

**The correct level.** Using the properly recruited `S₀ = {2,3,5} ∪ Q = {2,3,5,11,19,23}`
(chosen to match the extended types `A' = {3,5,19}`, `B' = {2,11}` reported in round 6
and re-verified independently again this round: `ρ(6) = P(a_6)∩S₀ = {3,5,19}`,
`ρ(7) = P(a_7)∩S₀ = {2,11}`, an exact match), the Confined-GCD Lemma's data becomes
`F' = P(a_6)\S₀ = {17}`, `F'' = P(a_7)\S₀ = {13,17}`, `q* = min(F'∩F'') = 17`,
`b = 13·17 = 221`, `Div(b) = {1,13,17,221}`, `D_bad = {13}` (a SINGLE bad class this
time, not three). Scanning `n = 8,...,6000` for `ρ(n) = A' = {3,5,19}` exactly, I found
only **9** such occurrences (this extended type is rare — `9` hits in `5993` scanned
indices) — and among all 9, `g_n ∉ D_bad` (i.e. `q*=17 | a_n` in every case): `E = ∅`.
Symmetrically, among `136` `B'`-occurrences (`ρ(n) = {2,11}`) past `n_A=6`,
`E_sym = ∅` as well.

**Honest reading of this check.** This is consistent with Cofinite (in fact literal)
FAH continuing to hold on this seed — no counterexample found, matching every prior
round's survey. But it does **not** test the Escape-Cost Lemma's actual premise: that
premise needs MULTIPLE occurrences landing in the SAME bad class `d ∈ D_bad`, so that
the claimed "index gap must grow with repetition count" phenomenon has something to
be checked against. With `E = ∅` outright, there are zero repeat-in-bad-class events to
examine — the numeric check is **inconclusive** for Step B specifically (it neither
confirms nor refutes the growth claim), even though it is reassuring evidence for the
target theorem (FAH) itself. This sparsity (only 9 `A'`-occurrences in 6000 terms) also
explains why finding a seed that actually exercises Step B's premise is hard: the
properly-recruited extended types are individually rare, and (per the pattern already
established across nine prior mechanisms) FAH already seems to hold with zero
exceptions whenever the core is correctly recruited, leaving no positive instances of
"repeated bad-class occurrence" to study empirically. Given this, I moved to the
algebraic route: settle Step B's derivability in the abstract, rather than searching
further for an ever-rarer numeric witness.

### 11.6 The Sandwich Genericity / Escape-Cost Vacuity Theorem (full proof — the
round's main deliverable)

**Theorem (Sandwich Genericity).** For all indices `1 ≤ m < n` (of the WHOLE sequence,
not restricted to any type, extended type, or divisor class), `n - m ≤ a_n - a_m ≤
(n-m)·a_1`.

*Proof.* *Lower bound.* Since the sequence is strictly increasing (each `a_{i+1}` is,
by hypothesis, the smallest integer `> a_i` satisfying the divisibility condition, in
particular `a_{i+1} > a_i`, and all terms are integers, so `a_{i+1} ≥ a_i + 1`),
telescoping `a_{i+1} ≥ a_i + 1` for `i = m, ..., n-1` gives `a_n ≥ a_m + (n-m)`, i.e.
`a_n - a_m ≥ n - m`.
*Upper bound.* By the certified Bounded Gap Lemma (`lemmas/bounded-gap-lemma.md`),
`a_{i+1} ≤ a_i + a_1` for every `i`. Telescoping this for `i = m, ..., n-1` gives
`a_n ≤ a_m + (n-m)·a_1`, i.e. `a_n - a_m ≤ (n-m)·a_1`. ∎

**Crucial observation: this Theorem's statement and proof make no reference whatsoever
to `τ(m)`, `τ(n)`, `ρ(m)`, `ρ(n)`, `g_m`, `g_n`, or any other type/divisor-class datum
of `m` or `n`.** It holds for literally every pair `1 ≤ m < n`, with the SAME two
constants (`1` and `a_1`, both depending only on `a_1`, not on `m`, `n`, or any
class label). This is not a weakness of the proof technique — it is a structural
feature of the two lemmas the Theorem is built from (strict monotonicity, and the
Bounded/Generalized Bounded Gap Lemma), neither of which involves the prime-factor
data of the terms at all beyond what is needed to state and prove the Gap Lemma's own
single-step inequality (which itself, per `lemmas/bounded-gap-lemma.md`'s own proof,
only uses that `a_n · a_1` — or, for the Generalized version, `a_n · c` for `c`
divisible by every prime of `Q` — is always a legal next candidate; this legality
argument is uniform across ALL types, since it uses only that `a_1 | Q`'s primes are
common to the multiple constructed and every earlier term via `Q`-membership, a fact
independent of which extended type or divisor class the current term happens to be).

**Theorem (Escape-Cost Vacuity).** No argument whose ONLY quantitative input is the
Sandwich Genericity inequality (applied to some pair(s) of `A'`-occurrences) — combined
with any facts that are themselves class-blind in the same sense (i.e. facts of the
form "property P holds/fails for a pair of indices `m,n`, stated using only `m`, `n`,
and universal constants depending on `a_1` alone, with no reference to `g_m`, `g_n`,
or any divisor-class label `d`") — can establish a conclusion of the form asserted by
the Escape-Cost Lemma: that the index gap `n_{j'} - n_j` between two `A'`-occurrences
sharing the SAME divisor class `g_{n_j} = g_{n_{j'}} = d ∈ D_bad` is bounded below by a
quantity that grows (without bound, or even just strictly, relative to a same-class
repetition count) — UNLESS that same lower bound is forced to hold equally for
`A'`-occurrence pairs that do NOT share a divisor class, or for pairs where one or both
occurrences are `q*`-divisible (not in `E` at all).

*Proof.* Suppose such an argument existed, built as a finite sequence of deductions
starting only from (i) the Sandwich Genericity inequality applied to specific index
pairs, and (ii) other class-blind facts as described. Let `(n_j, n_{j'})` be ANY pair
of `A'`-occurrences with `n_j < n_{j'}` — same class or not, in `E` or not. Every
premise available to the argument (the Sandwich inequality itself, and by hypothesis
every other fact it uses) is, as a mathematical statement, a function of `n_j` and
`n_{j'}` alone (via the universal constants `1, a_1`) — it does not take the values
`g_{n_j}, g_{n_{j'}}` as inputs anywhere, by the definition of "class-blind." Hence
substituting the SAME numerical values `n_j, n_{j'}` into the argument's chain of
deductions produces, by determinism of logical deduction from identical premises, the
SAME output for EVERY pair of indices with those two index values — regardless of
which divisor classes `g_{n_j}, g_{n_{j'}}` those indices actually carry. In
particular, the argument cannot distinguish the case `g_{n_j} = g_{n_{j'}} = d` (same
bad class, the case the Escape-Cost Lemma's conclusion is specifically ABOUT) from the
case `g_{n_j} ≠ g_{n_{j'}}` (different classes, or one/both `q*`-divisible) for the
SAME pair of index values `n_j, n_{j'}` — because the argument's premises and every
deductive step never reference `g_{n_j}` or `g_{n_{j'}}` at all. So any lower bound
on `n_{j'} - n_j` the argument derives must hold for literally every pair of
`A'`-occurrences with those index values, independent of divisor class. This directly
contradicts the Escape-Cost Lemma's asserted content, which requires the bound to be
SPECIFIC to same-bad-class pairs (indeed to grow with the same-class repetition
count, a quantity that is not even a function of `n_j, n_{j'}` alone, but of the whole
history of classes visited) — a class-sensitive, history-sensitive conclusion cannot be
the output of a class-blind, history-blind argument. ∎

**Consequence for Step 11's Step B.** The ONLY quantitative fact Step 11.2's Step A
supplies is exactly the Sandwich Genericity inequality (this is Step A verbatim: `g ≤
V ≤ g·a_1`, `g` the index gap, `V` the value gap — both bounds class-blind per the
Theorem just proved). The Confined-GCD Lemma and the definition of `D_bad` are
class-blind in the relevant sense too (they define the ALPHABET of classes, a static,
`n`-independent set; they do not supply any inequality relating `g_{n_j}` to
`g_{n_{j'}}` for a specific pair `j, j'`, nor any inequality whose bound depends on
which class is repeated). So by the Escape-Cost Vacuity Theorem, **Step B cannot be
derived from Step A plus the currently-certified class-blind toolkit, full stop** —
not merely "I could not find the argument," but a proof that no such argument exists
using only these ingredients. The only way to salvage Step B is to introduce a
genuinely NEW ingredient that is class-SENSITIVE (relates `g_n` for different `n` to
each other, or relates a divisor-class label to an index-gap bound directly) — which
is exactly Lemma I's original diagnosis (round 6), now independently reconfirmed via
an entirely different, magnitude-based proof route rather than the Free-Facts/
Bounded-Witness/Gap-Lemma/Critical-Prime-Dichotomy toolkit Lemma I examined. **The
"recursively constrains earlier terms" intuition sketched informally in the outline's
Step B (Step 11.3) is not a counterexample to this Theorem — it is exactly the missing
class-sensitive ingredient the Theorem shows must come from somewhere else, and no
such ingredient exists in the certified lemma set as of this round.**

**Conclusion.** The Escape-Cost Lemma, as scoped by this round's outline (built from
Step A's magnitude sandwich), is dead — not falsified by a counterexample (none was
needed), but proved structurally unreachable by the proposed route. This is the
tenth confirmed-dead mechanism for FAH/Cofinite FAH in this workspace (after Lemma
I's six, round 8's Fixed-Witness Divisor-Chain, round 9's Recruitment-Budget Lemma,
and round 9's Successor-Transport/Successor-Claim stall). Per CLAUDE.md's honest-
failure-reporting rule, I am not attempting a rescue (e.g., trying to smuggle in a
class-sensitive fact under a different name) — any future mechanism in this family
must explicitly identify and prove a NEW class-sensitive fact (one whose statement
references `g_n` for two or more different `n` simultaneously, or relates a specific
divisor-class label to a magnitude bound) before it can possibly close Step B; a pure
value/index magnitude argument, however dressed up, cannot supply this by the Theorem
above.

## Promotable lemmas (round 10 addendum)

- **Sandwich Genericity Theorem** (Step 11.6, this round): for all `1 ≤ m < n`,
  `n-m ≤ a_n - a_m ≤ (n-m)·a_1`, with both bounds and constants independent of
  `τ(m), τ(n), ρ(m), ρ(n)`, or any divisor-class datum. A short, fully proved,
  unconditional corollary of strict monotonicity plus the already-certified Bounded
  Gap Lemma. Reusable: forecloses, in one line, any future "magnitude-only squeeze"
  attempt at FAH/Cofinite FAH (aimo-0680-style or otherwise) that tries to derive a
  class-discriminating conclusion from the Gap Lemmas alone.
- **Escape-Cost Vacuity Theorem** (Step 11.6, this round): no argument built solely
  from class-blind premises (in particular, from the Sandwich Genericity Theorem plus
  any other class-blind certified fact) can output a class-sensitive conclusion (a
  bound depending on divisor-class repetition). A general "blindness cannot produce
  sight" impossibility argument, fully proved (by a determinism-of-deduction argument:
  identical premises on identical index-value inputs must produce identical outputs,
  regardless of the class labels those indices happen to carry). Reusable as a
  general screening test: before attempting any future magnitude-based mechanism for
  FAH/Cofinite FAH, check whether its premises are class-blind in this precise sense —
  if so, per this Theorem, the mechanism is dead before any computation is needed.
  Recommend certifying this as a standalone lemma (`lemmas/escape-cost-vacuity.md`)
  given its stated potential to save future rounds real build effort, matching the
  precedent set for the round-9 Witness Discontinuity Obstruction's screening role.
- **Numeric confirmation (Step 11.5, this round)**: at the properly-recruited
  `S₀ = {2,3,5,11,19,23}` level for `a_1=4807`'s standing `|F'|,|F''|≥2` rogue pair,
  `D_bad = {13}` (a single class), with `E = E_sym = ∅` observed across all 9+136
  sampled occurrences up to `N=6000` — consistent with (not a proof of) FAH continuing
  to hold; recorded so a future round does not need to recompute this seed's
  `S₀`-level data from scratch. NOT itself a new lemma (purely a numeric
  confirmation), included here for reuse.

## Step 4g — Round 12: the Reduced-Alphabet Corollary (bookkeeping only; full proof)

**Motivation and honesty scope, stated up front.** This section proves ONE small,
fully unconditional corollary of two already-certified lemmas
(`lemmas/confined-gcd-lemma.md`, `lemmas/singleton-side-fah.md`). It is dispatched as
a bookkeeping task, not a new FAH mechanism, and it is proved and reported as exactly
that: it narrows the explicit SIZE of the residual "bad divisor class" alphabet that
Joint FAH must rule out on one side of a rogue pair, once the OTHER side is already
known (via Singleton-Side FAH) to be fully resolved. It does not reduce this alphabet
to size 0 in general, does not supply any new class-sensitive tool (the round-10
Escape-Cost Vacuity Theorem still forecloses every currently-certified magnitude-only
route to eliminating even a single remaining class), and does not claim any progress
on FAH/Symmetric FAH itself.

### Setup (identical to Confined-GCD Lemma and Singleton-Side FAH)

Fix a core `S₀ ⊇ Q` and a rogue pair — disjoint-base-type `S₀`-extended-persistent
types `(A', B')` — with witnesses `n_A < n_B` (`ρ(n_A) = A'`, `ρ(n_B) = B'`). Let
`F' := P(a_{n_A}) \ S₀` and `F'' := P(a_{n_B}) \ S₀`, and write the `F''`-part of the
fixed integer `a_{n_B}` as `b := ∏_{p ∈ F''} p^{e_p}` where `e_p := v_p(a_{n_B}) ≥ 1`
for each `p ∈ F''` (so `b = ∏_{p∈F''} p^{v_p(a_{n_B})}`, exactly the `b` of the
Confined-GCD Lemma).

**Hypothesis of this Corollary.** `F'` is a singleton, `F' = {q'}` (the case `F''`
singleton is symmetric, obtained by exchanging the roles of `A'`/`n_A` and `B'`/`n_B`
throughout — see the Symmetric case below).

### Step 1 — the companion side is already fully resolved (import, no new proof needed)

By the certified Singleton-Side FAH Lemma (`lemmas/singleton-side-fah.md`), since
`F' = {q'}` is a singleton, `q' | a_n` for EVERY `n > n_A` with `ρ(n) = B'` — zero
exceptions, not merely cofinitely many. So the `B'`-side of Joint FAH for this rogue
pair is unconditionally settled; it contributes nothing further to the open crux.

### Step 2 — the remaining open direction, recast via Confined-GCD

The only direction of Joint FAH left open for this pair is the `A'`-side: does some
FIXED prime `q* ∈ F''` divide `a_n` for every `n > n_B` with `ρ(n) = A'`? (This is
literal FAH for the `A'`-side; the weaker Cofinite FAH target asks only that all but
finitely many such `n` satisfy it — see `lemmas/cofinite-sufficiency-lemma.md`, whose
scope is unaffected by anything in this section.)

Fix any `q* ∈ F''` (the candidate target prime — the argument below is stated for an
arbitrary choice of `q*`, since nothing in the Confined-GCD Lemma or Singleton-Side
FAH privileges one element of `F''` over another; in practice `q*` is chosen, as in
prior rounds, to be `min(F'∩F'')` when that intersection is nonempty, but this
Corollary's statement holds for every `q* ∈ F''` individually). By the certified
Confined-GCD Lemma (`lemmas/confined-gcd-lemma.md`), for every `n > n_B` with
`ρ(n) = A'`, writing `g_n := gcd(a_n, a_{n_B})`:
(a) `g_n | b`, so `g_n ∈ Div(b)`, a FIXED finite set independent of `n`;
(b) `g_n > 1`;
(c) `q* | a_n ⟺ q* | g_n`.

So the `A'`-side FAH-for-`q*` exception set is exactly
`E(q*) := {n > n_B : ρ(n)=A', q* ∤ g_n} = {n > n_B : ρ(n)=A', g_n ∈ D_bad(q*)}`, where

  `D_bad(q*) := {d ∈ Div(b) : d > 1, q* ∤ d}`

— a FIXED finite index set, independent of `n`, determined entirely by the single
witness integer `a_{n_B}` and the choice of `q*`. (This is exactly the object the
Confined-GCD Lemma's own "Scope" paragraph already names `D_bad`; this Corollary's
content is the explicit closed-form count below, which was not previously derived.)

### Step 3 — the Reduced-Alphabet Corollary: an explicit closed-form bound on `|D_bad(q*)|`

**Corollary (Reduced-Alphabet).** With notation as above (`b = ∏_{p∈F''}p^{e_p}`,
`q* ∈ F''` fixed),

  `|D_bad(q*)| = ∏_{p ∈ F''\{q*}} (e_p + 1) − 1`.

In particular `|D_bad(q*)|` is finite, explicit, computable from the single witness
`a_{n_B}` alone, and — crucially, since this is the whole content of "reduced
alphabet" — depends only on `F'' \ {q*}` and its exponents in `a_{n_B}`, NOT on any
data about `n`, about the `A'`-side, or about how many occurrences of `A'` exist. When
`|F''| = 2`, say `F'' = {q*, q**}` with `v_{q**}(a_{n_B}) = e`, this gives
`|D_bad(q*)| = (e+1) − 1 = e`; in particular if `e = 1` (as in every concretely
computed `|F''|=2` seed in this workspace to date — a_1=4807's pair has `q**=13` with
`v_{13}(a_7)=v_{13}(4862)=1`, and a_1=11305's analogous pair has the same shape),
`|D_bad(q*)| = 1`: the residual bad-divisor-class alphabet collapses to EXACTLY one
class.

*Proof.* Every divisor `d` of `b = ∏_{p∈F''} p^{e_p}` corresponds bijectively (by
unique factorization, `knowledge_base.md` "Fundamental Theorem of Arithmetic" /
standard divisor-counting) to a choice of exponent `0 ≤ f_p ≤ e_p` for each
`p ∈ F''`, via `d = ∏_{p∈F''} p^{f_p}`. The condition `q* ∤ d` is, under this
bijection, exactly the condition `f_{q*} = 0` (since `q* ∈ F''` is one of the primes
in the product, `q* | d ⟺ f_{q*} ≥ 1`). So the divisors `d` of `b` with `q* ∤ d` are
in bijection with tuples `(f_p)_{p ∈ F''\{q*}}` with `0 ≤ f_p ≤ e_p` (the exponent at
`q*` is forced to `0`, and every other exponent ranges freely over its full allowed
set) — there are exactly `∏_{p∈F''\{q*}} (e_p+1)` such tuples, hence exactly that many
divisors of `b` not divisible by `q*`. Exactly one of these divisors is `d=1` (the
tuple with every `f_p = 0`), which is excluded from `D_bad(q*)` by the requirement
`d>1` (itself forced unconditionally by part (b) of the Confined-GCD Lemma, `g_n>1`
always, so `d=1` never actually occurs as a value of `g_n` and including it in the
count would only ever overcount, never miss a genuine exception). Removing this one
divisor gives `|D_bad(q*)| = ∏_{p∈F''\{q*}}(e_p+1) − 1`. ∎

**Symmetric case.** If instead `F''` is the singleton (`F'' = {q''}`), the identical
argument with the roles of `(A',n_A)` and `(B',n_B)` exchanged gives: the `B'`-side is
resolved by Singleton-Side FAH, and for the remaining open `B'`-side-vs-`A'`-witness
direction, fixing any `q*∈F'` and writing `a := ∏_{p∈F'}p^{v_p(a_{n_A})}` (the
`F'`-part of `a_{n_A}`), `|D_bad(q*)| = ∏_{p∈F'\{q*}}(v_p(a_{n_A})+1) − 1`, by the
Confined-GCD Lemma applied with the roles of `n_A`, `n_B` swapped (its statement and
proof, per `lemmas/confined-gcd-lemma.md`, are symmetric in the two witnesses up to
relabeling, since they only use Free Facts and the rogue-pair disjointness `A'∩B'=∅`,
both symmetric hypotheses).

### Step 4 — verification against this round's concrete data (a_1=4807)

As a direct check (not a proof step, but a substitution-and-verify sanity check per
CLAUDE.md's answer-verification norm, since this Corollary makes an explicit
quantitative claim): for `a_1=4807`'s standing rogue pair (S₀={2,3,5,11,19,23},
`A'={3,5,19}`, `B'={2,11}`, `n_A=6`, `n_B=7`), `F' = P(a_6)\S₀ = {17}` (singleton, as
required by this Corollary's hypothesis), `F'' = P(a_7)\S₀ = {13,17}`, `b =
13^1·17^1=221`. Taking `q*=17 ∈ F''`, the Corollary predicts `|D_bad(17)| =
(v_{13}(a_7)+1) − 1 = (1+1)−1 = 1`. Direct enumeration: `Div(221) = {1,13,17,221}`,
`D_bad(17) = {d ∈ {1,13,17,221} : d>1, 17∤d} = {13}`, so `|D_bad(17)|=1` — matches the
Corollary's closed-form prediction exactly, and matches this round's smallcase
explorer's independently-computed value. This confirms the formula is not merely
stated but correctly derived and consistent with the workspace's existing
computations; it is not, and is not claimed to be, evidence toward FAH itself (the
Corollary is a statement about alphabet size, established unconditionally by Step 3's
proof, not a numerical experiment whose outcome could have gone either way).

### What this Corollary does and does not achieve — final honest scope statement

**Achieves (unconditional, proved above):** given a rogue pair with a singleton
far-side factor set on one side, (i) that side is fully resolved with zero exceptions
(Singleton-Side FAH, imported); (ii) the residual open-side bad-divisor-class alphabet
`D_bad(q*)` has an explicit, closed-form size `∏_{p∈F''\{q*}}(e_p+1) − 1`, computable
from a single fixed witness integer, independent of `n` — in the `|F''|=2`,
multiplicity-1 case (the concrete standing test seeds), this size is exactly 1.

**Does NOT achieve:** it does not rule out any element of `D_bad(q*)`, however small;
it does not supply a new class-sensitive fact of the kind the Escape-Cost Vacuity
Theorem (round 10) shows is necessary and not yet available; it does not reduce the
general `|F''|≥3` or higher-multiplicity cases to a comparably small alphabet (the
formula shows the alphabet CAN be large — e.g. `F''` with several primes each of high
multiplicity gives an arbitrarily large `|D_bad(q*)|` — so "reduced" here means
"explicitly computed and often, but not always, small," not "uniformly bounded across
all rogue pairs"); and it is not itself usable to close FAH/Symmetric FAH by any
mechanism currently certified in this workspace. It is exactly what its name says: a
bookkeeping reduction of the alphabet a future mechanism would need to work with, not
a step toward eliminating that alphabet.

## Promotable lemmas (round 12 addendum)

- **Reduced-Alphabet Corollary** (Step 4g, this round): for a rogue pair `(A',B')`
  with witnesses `n_A<n_B` and one side's far-factor set a singleton (say
  `F'=P(a_{n_A})\S₀={q'}`), the companion side is fully resolved with zero exceptions
  by the already-certified Singleton-Side FAH Lemma, and the remaining open `A'`-side
  FAH-for-`q*` (`q*∈F''` arbitrary) exception alphabet `D_bad(q*)` — confined by the
  already-certified Confined-GCD Lemma to divisors of `b:=∏_{p∈F''}p^{v_p(a_{n_B})}` —
  has explicit size `∏_{p∈F''\{q*}}(v_p(a_{n_B})+1) − 1`; in the standing `|F''|=2`,
  multiplicity-1 test seeds (a_1=4807, 11305) this equals exactly 1, matching direct
  enumeration. Fully proved (a one-line divisor-counting corollary of two already-
  certified lemmas, Free Facts, and the Fundamental Theorem of Arithmetic), fully
  unconditional, no dependence on any open hypothesis. Reusable by any approach
  wanting an explicit alphabet-size bound for a singleton-side rogue pair (in
  particular `seed-coupling-induction`'s orphaned Lemma B, per this round's
  outline). Recommend certifying as `lemmas/reduced-alphabet-corollary.md`. Does NOT
  resolve FAH/Symmetric FAH; see the honest scope statement immediately above for
  what it does and does not achieve.

## Round 26 advance target: last residual divisor-class `d=13` at `a_1=4807`

The certified Reduced-Alphabet Corollary (round 12) reduces the open FAH-exception
alphabet at the standing test seed `a_1=4807` (rogue pair `A'={3,5,19}`, `B'={2,11}`,
`n_A=6, n_B=7`) to the single divisor class `D_bad(17)={13}`. This round's target:
determine whether `g_n = 13·(unit part)` (the gcd-witness cofactor class corresponding
to this residual class) ever actually occurs for the relevant indices `n`, i.e. either
prove it can never occur (closing this last residual class unconditionally) or exhibit
it occurring (an honest negative/open finding, not a proof of FAH's failure in general).

**Technique**: trace back through the Confined-GCD Lemma's proof to restate precisely
what "`d=13`" as a witness cofactor would require of the underlying sequence data, then
check compatibility against the problem's minimality/legality rule, in the style of the
already-certified Escape-Cost Vacuity / Same-Type Triangle Vacuity results.

**Skeleton**: (1) restate precisely what `d=13` would mean for the relevant indices/
classes (unpack Confined-GCD Lemma's definitions); (2) check compatibility against
minimality/legality (does forcing this class require an illegal move, or one already
ruled out by an existing certified lemma — Bounded Gap Lemma, Free Facts)?; (3) if
incompatible, certify a new narrow Vacuity result for this specific class; if compatible/
inconclusive, report honestly as a further-open residual, no overclaim.

**Scope**: bounded to the single residual class `d=13` for the `a_1=4807` seed only — do
NOT attempt the general `|F''|≥3` case this round (out of scope). This is explicitly NOT
a new H1/FAH mechanism, only a bounded follow-up on already-certified bookkeeping —
report a clean negative plainly if no traction is found, do not spiral into open-ended
FAH speculation (per the round-26 H1-fresh-corridor explorer's finding of no new
corridor this round, and per this file's own extensive dead-mechanism history, 34+
confirmed-dead mechanisms).

## Step 4h — Round 26: closing the residual class `d=13` at `a_1=4807` (complete, unconditional, single-seed)

This section carries out the exact task the outline-reviewer scoped for this round:
determine whether the divisor class `d=13` — the single element of `D_bad(17)` isolated
by round 12's Reduced-Alphabet Corollary for `a_1=4807`'s standing rogue pair — ever
actually occurs, or prove it cannot. **Result: it cannot; proved unconditionally
below.** The mechanism is new (not previously assembled in this file), though every
individual ingredient except one short lemma is already certified.

### Setup (recap, unchanged from Steps 4f–4g)

`a_1 = 4807`, `S₀ = {2,3,5,11,19,23}`, `ρ(n) := P(a_n) ∩ S₀`. The standing rogue pair
has base disjoint types with canonical witnesses `n_A = 6` (`a_6 = 4845 = 3·5·17·19`,
`ρ(6) = A' = {3,5,19}`) and `n_B = 7` (`a_7 = 4862 = 2·11·13·17`, `ρ(7) = B' = {2,11}`).
`F' := P(a_6)\S₀ = {17}`, `F'' := P(a_7)\S₀ = {13,17}`, `b := 13·17 = 221`. By the
Reduced-Alphabet Corollary (Step 4g, `q* = 17`), the open `A'`-side exception alphabet
is `D_bad(17) = {13}`: writing `g_n := gcd(a_n, a_7)` for `n>7` with `ρ(n)=A'`, the
Confined-GCD Lemma gives `g_n ∈ Div(221) = {1,13,17,221}` and `g_n > 1`, and `17 | a_n
⟺ 17 | g_n`; the only way `17 ∤ a_n` can happen is `g_n = 13` exactly. So "`d=13` never
occurs" is *equivalent* to "literal FAH-for-`17` holds on the `A'`-side of this pair,"
i.e. `17 | a_n` for every `n>7` with `ρ(n) = A'`, with zero exceptions.

### Step 1 — a non-canonical singleton `B'`-witness, already on record

The certified Two-Sided Singleton Witness Theorem (`lemmas/two-sided-singleton-
witness-theorem.md`, round 18–19) already recorded, for this exact seed, a
**non-canonical** `B'`-occurrence at index `x_1 = 72` with `P(a_{72}) \ S₀ = \{17\}` —
a *singleton*. Direct computation confirms this independently: `a_{72} = 5984 =
2^5 · 11 · 17`, so `P(a_{72}) ∩ S₀ = \{2,11\} = B'` (confirming `ρ(72) = B'`, i.e. `72`
is a genuine `B'`-occurrence) and `P(a_{72}) \ S₀ = \{17\}` exactly.

By the certified Singleton-Side FAH Lemma (`lemmas/singleton-side-fah.md`), applied
with far-side witness `n_B := x_1 = 72` (valid: the Lemma's hypothesis only requires
*some* index with the stated `ρ`-value and singleton complement, not that it be
canonical or earliest — its own Setup paragraph states witnesses may be "any valid
witnesses"): since `P(a_{72}) \ S₀ = \{17\}` is a singleton,

  `17 | a_n` for **every** `n > 72` with `ρ(n) = A'`.  (‡)

This is already exactly the content the round-18/19 Two-Sided Singleton Witness
Theorem certifies for this seed (there reported, correctly, only as giving *Cofinite*
FAH — because it leaves the finitely many indices `n` with `7 < n \le 72` unchecked).
What follows closes that finite remaining gap.

### Step 2 — the Finite-Window Literalization Lemma (new, fully proved, promotable)

**Lemma (Finite-Window Literalization).** Let `(A',B')` be a rogue pair at core `S₀`
with canonical witnesses `n_A < n_B`. Suppose there is an index `x_1` with `ρ(x_1) =
B'` and `P(a_{x_1}) \ S₀ = \{q\}` a singleton (the hypothesis of Singleton-Side FAH /
the Two-Sided Singleton Witness Theorem, applied with far-side witness `x_1`). If, in
addition, there is **no** index `n` with `n_B < n \le x_1` and `ρ(n) = A'`, then
`q | a_n` for **literally every** `n > n_B` with `ρ(n) = A'` — zero exceptions, not
merely cofinitely many.

*Proof.* Let `n > n_B` with `ρ(n) = A'`. Exactly one of two cases holds (they are
exhaustive and mutually exclusive, since `n` is a single integer being compared to the
fixed integer `x_1`): either `n > x_1`, or `n_B < n \le x_1`.
- If `n > x_1`: by Singleton-Side FAH applied with far-side witness `x_1` (exactly
  Step 1's derivation, with `n` in place of the class of all indices `> x_1`),
  `q | a_n`.
- If `n_B < n \le x_1`: by hypothesis, no such `n` has `ρ(n) = A'` — so this case does
  not occur for the `n` under consideration (we assumed `ρ(n)=A'`), i.e. this case is
  vacuous.
Since every `n>n_B` with `ρ(n)=A'` falls in the first case (the second being
impossible by hypothesis), `q | a_n` for all of them. ∎

This is a short, self-contained, unconditional lemma (given its two hypotheses, both
individually checkable — the first is exactly the Two-Sided Singleton Witness
Theorem's own existence hypothesis for one side, the second is a finite, directly
computable condition since the window `(n_B, x_1]` contains only finitely many
integers). It strictly strengthens the conclusion of Singleton-Side FAH-via-non-
canonical-witness from "cofinite" to "literal," at the cost of the additional
(finite, checkable) hypothesis. It is stated and proved here in full generality (not
tied to `a_1=4807`), so it is reusable by any approach that has already established
the Two-Sided Singleton Witness Theorem's existence hypothesis for some rogue pair and
wants literal rather than merely cofinite FAH.

### Step 3 — verifying the Lemma's finite hypothesis for `a_1=4807` (explicit, displayed computation)

We must check: is there any index `n` with `7 < n \le 72` and `ρ(n) = A' = \{3,5,19\}`?
The sequence `a_1,\dots,a_{80}` for `a_1=4807` (computed directly from the problem's
recursive rule — smallest integer exceeding the previous term with `\gcd > 1` against
every earlier term — a fully deterministic, finite computation) is:

```
n   a_n    factorization                 P(a_n)∩S₀
1   4807   11·19·23                      {11,19,23}
2   4818   2·3·11·73                     {2,3,11}
3   4826   2·19·127                      {2,19}
4   4830   2·3·5·7·23                    {2,3,5,23}
5   4840   2^3·5·11^2                    {2,5,11}
6   4845   3·5·17·19                     {3,5,19}   [= A', canonical n_A]
7   4862   2·11·13·17                    {2,11}     [= B', canonical n_B]
8   4864   2^8·19                        {2,19}
9   4884   2^2·3·11·37                   {2,3,11}
10  4902   2·3·19·43                     {2,3,19}
11  4940   2^2·5·13·19                   {2,5,19}
12  4950   2·3^2·5^2·11                  {2,3,5,11}
13  4968   2^3·3^3·23                    {2,3,23}
14  4978   2·19·131                      {2,19}
15  5016   2^3·3·11·19                   {2,3,11,19}
16  5054   2·7·19^2                      {2,19}
17  5060   2^2·5·11·23                   {2,5,11,23}
18  5082   2·3·7·11^2                    {2,3,11}
19  5092   2^2·19·67                     {2,19}
20  5106   2·3·23·37                     {2,3,23}
21  5130   2·3^3·5·19                    {2,3,5,19}
22  5148   2^2·3^2·11·13                 {2,3,11}
23  5168   2^4·17·19                     {2,19}
24  5170   2·5·11·47                     {2,5,11}
25  5206   2·19·137                      {2,19}
26  5214   2·3·11·79                     {2,3,11}
27  5236   2^2·7·11·17                   {2,11}     [= B']
28  5244   2^2·3·19·23                   {2,3,19,23}
29  5280   2^5·3·5·11                    {2,3,5,11}
30  5282   2·19·139                      {2,19}
31  5290   2·5·23^2                      {2,5,23}
32  5320   2^3·5·7·19                    {2,5,19}
33  5346   2·3^5·11                      {2,3,11}
34  5358   2·3·19·47                     {2,3,19}
35  5382   2·3^2·13·23                   {2,3,23}
36  5390   2·5·7^2·11                    {2,5,11}
37  5396   2^2·19·71                     {2,19}
38  5412   2^2·3·11·41                   {2,3,11}
39  5434   2·11·13·19                    {2,11,19}
40  5472   2^5·3^2·19                    {2,3,19}
41  5474   2·7·17·23                     {2,23}
42  5478   2·3·11·83                     {2,3,11}
43  5500   2^2·5^3·11                    {2,5,11}
44  5510   2·5·19·29                     {2,5,19}
45  5520   2^4·3·5·23                    {2,3,5,23}
46  5544   2^3·3^2·7·11                  {2,3,11}
47  5548   2^2·19·73                     {2,19}
48  5586   2·3·7^2·19                    {2,3,19}
49  5610   2·3·5·11·17                   {2,3,5,11}
50  5624   2^3·19·37                     {2,19}
51  5658   2·3·23·41                     {2,3,23}
52  5662   2·19·149                      {2,19}
53  5676   2^2·3·11·43                   {2,3,11}
54  5700   2^2·3·5^2·19                  {2,3,5,19}
55  5720   2^3·5·11·13                   {2,5,11}
56  5738   2·19·151                      {2,19}
57  5742   2·3^2·11·29                   {2,3,11}
58  5750   2·5^3·23                      {2,5,23}
59  5776   2^4·19^2                      {2,19}
60  5796   2^2·3^2·7·23                  {2,3,23}
61  5808   2^4·3·11^2                    {2,3,11}
62  5814   2·3^2·17·19                   {2,3,19}
63  5830   2·5·11·53                     {2,5,11}
64  5852   2^2·7·11·19                   {2,11,19}
65  5874   2·3·11·89                     {2,3,11}
66  5890   2·5·19·31                     {2,5,19}
67  5928   2^3·3·13·19                   {2,3,19}
68  5934   2·3·23·43                     {2,3,23}
69  5940   2^2·3^3·5·11                  {2,3,5,11}
70  5966   2·19·157                      {2,19}
71  5980   2^2·5·13·23                   {2,5,23}
72  5984   2^5·11·17                     {2,11}     [= B', x_1]
```

Scanning the `P(a_n) ∩ S₀` column for `n = 8,\dots,72`: the value `\{3,5,19\}` (`A'`)
occurs **nowhere** in this range — the only occurrences of `A'` in the displayed table
are at `n=6` (the canonical witness itself, excluded since we need `n>n_B=7`). The
only occurrences of `B'=\{2,11\}` in `8 \le n \le 72` are `n=27` and `n=72` (irrelevant
to the hypothesis being checked, which concerns `A'`-occurrences). This is a finite,
exhaustive, fully displayed verification: the Finite-Window Literalization Lemma's
second hypothesis holds for `(n_B,x_1] = (7,72]`.

### Step 4 — conclusion: `d=13` never occurs, unconditionally

By Step 1 (`x_1=72` is a genuine `B'`-occurrence with singleton complement `\{17\}`,
re-derived independently in Step 1 and matching the certified Two-Sided Singleton
Witness Theorem's recorded data for this seed) and Step 3 (no `A'`-occurrence in
`(7,72]`, verified exhaustively), the Finite-Window Literalization Lemma (Step 2)
applies directly with `(A',B')` this pair, `q=17`, `n_B=7`, `x_1=72`, giving:

  `17 | a_n` for **every** `n > 7` with `ρ(n) = A'`.  (literal, zero exceptions)

Combined with the Confined-GCD Lemma's confinement `g_n \in \{1,13,17,221\}`,
`g_n > 1`, and equivalence `17 | a_n \Leftrightarrow 17 | g_n$ (Step 4g's setup,
recalled above): since `17 | a_n` always, `17 | g_n` always, so `g_n` — always a
divisor of `221=13\cdot17` exceeding `1` and divisible by `17` — can only be `17` or
`221` (the two divisors of `221` divisible by `17`; `13` and `1` are excluded, `13`
because it is not divisible by `17`, `1` because `g_n>1`). Hence:

  **`g_n \ne 13` for every `n>7` with `\rho(n)=A'` — the residual class `d=13`
  never occurs. This is proved unconditionally, not merely observed.**

(As an independent computational cross-check, not itself part of the proof: a direct
simulation of `a_1=4807` out to `45{,}000` terms found `70` occurrences of `A'` with
`n>7`, all `70` giving `g_n \in \{17,221\}` and none giving `g_n=13$ — fully consistent
with, and now explained in full by, the proof above.)

**What this establishes for the rogue pair as a whole.** Combining this with the
already-certified `B'`-side resolution (Singleton-Side FAH applied at the *canonical*
witness `n_A=6`, since `F'=\{17\}` is already a singleton there — Step 1 of Step 4g):
`17 | a_n$ for every `n>6` with `\rho(n)=B'`, zero exceptions. So **literal Joint FAH
holds, unconditionally, for `a_1=4807`'s standing rogue pair, in both directions**,
with the single shared witness prime `q=17` (matching `F' \cap F'' \ne \emptyset =
\{17\}`, itself forced by the certified `F_A \cap F_B \ne \emptyset` Lemma of Step 4e).

### Honest scope — what this does and does not establish

**Establishes (unconditional, complete):** for this one seed (`a_1=4807`) and this one
standing rogue pair, literal (zero-exception) Joint FAH holds, fully proved. The
Reduced-Alphabet Corollary's residual class `d=13` is closed: it never occurs, not
merely "not yet observed." This is exactly the round-26 scoped deliverable.

**Does NOT establish:**
- **General FAH / Cofinite FAH for arbitrary `a_1`.** The mechanism used a specific,
  concrete numerical fact about `a_1=4807` (the existence of the non-canonical
  singleton witness `x_1=72`, and the finite-window vacancy verified in Step 3) — both
  are seed-specific computational facts, not derived from any general structural
  argument. The Two-Sided Singleton Witness Theorem's own scope note already states
  the underlying existence hypothesis (a matching singleton witness on the relevant
  side) is "a genuine, unproved, narrower existence question," and this round supplies
  no new argument for why such a witness must exist for a general rogue pair at a
  general `a_1` — only that it happens to exist, and is usable, for this one seed.
  This is consistent with (does not touch) the certified Escape-Cost Vacuity Theorem
  (round 10): the resolution here is not a magnitude-only squeeze but a direct
  divisibility fact about a specific fixed integer (`a_{72}`), fully class-sensitive by
  construction — it does not attempt to extract class information from the class-blind
  Bounded Gap Lemma, so there is no tension with that Theorem's scope.
- **`a_1=11305`, the workspace's other standing test seed.** Not attempted this round
  (out of scope per the dispatch); the certified Two-Sided Singleton Witness Theorem's
  own verification note (round 19) records a candidate witness `x_2=103` on the `A'`-
  side for that seed with singleton signature `\{11\}$, so an analogous Finite-Window
  Literalization argument may well apply there too, but this has not been checked and
  is left as a natural next bounded task, not claimed here.
- **The `|F''| \ge 3` or higher-multiplicity general case.** Untouched, exactly as
  scoped out by the dispatch.

## Promotable lemmas (round 26 addendum)

- **Finite-Window Literalization Lemma** (Step 4h, Step 2, this round): given a rogue
  pair `(A',B')` at core `S₀` with canonical witnesses `n_A<n_B`, and a (possibly
  non-canonical) index `x_1` with `\rho(x_1)=B'` and `P(a_{x_1})\setminus S₀=\{q\}` a
  singleton (the Two-Sided Singleton Witness Theorem / Singleton-Side FAH hypothesis),
  IF additionally no index `n` with `n_B<n\le x_1` has `\rho(n)=A'` (a finite,
  directly-checkable condition), THEN `q|a_n` for literally every `n>n_B` with
  `\rho(n)=A'` — upgrading that already-certified machinery's Cofinite-FAH conclusion
  to literal, zero-exception FAH. Fully proved above (a two-line case split on
  `n>x_1` vs `n_B<n\le x_1`, using only the already-certified Singleton-Side FAH and
  the finite-window hypothesis). Reusable by any approach that has already secured a
  Two-Sided-Singleton-Witness-style existence hypothesis and wants literal rather than
  cofinite FAH — in particular immediately re-applicable to `a_1=11305`'s recorded
  candidate witness `x_2=103` (untried this round, flagged above). Recommend
  certifying as `lemmas/finite-window-literalization-lemma.md`.
- **`a_1=4807` residual-class closure (seed-specific, fully proved)**: the Reduced-
  Alphabet Corollary's residual class `d=13` for this seed's standing rogue pair never
  occurs; literal Joint FAH holds unconditionally for this one rogue pair (Step 4h,
  Steps 1–4). Not a general theorem, but a concrete, fully verified, reusable data
  point (e.g. for `seed-coupling-induction` or any approach using this seed as a test
  bed) — no future round needs to re-derive or re-check this seed's residual class.

## Step 4i — Round 27: closing the residual class `d=103` at `a_1=11305` (complete, unconditional, second single-seed instance)

This section carries out, for the workspace's other standing hard test seed
`a_1=11305`, exactly the task round 26's Step 4h carried out for `a_1=4807`: apply
the certified Finite-Window Literalization Lemma (`lemmas/finite-window-
literalization-lemma.md`) to upgrade the certified Two-Sided Singleton Witness
Theorem's Cofinite-FAH conclusion to literal (zero-exception) Joint FAH. The seed's
canonical witnesses occur in the OPPOSITE index order from `4807` (`n_B<n_A` here,
vs `n_A<n_B` there), so the Lemma's stated hypotheses (which are phrased for a pair
with `n_A<n_B`) must be applied with the two extended types **relabeled** before
substitution — this relabeling is carried out explicitly and checked at every step
below, rather than copying `4807`'s substitution verbatim.

### Setup (recomputed independently from scratch, matching this round's explorer)

`a_1 = 11305 = 5·7·17·19`, so `Q = \{5,7,17,19\}`. Recruiting one witness per
persistent base type via the certified Finite Core Theorem (Step 3) and the certified
Two-Sided Singleton Witness Theorem's own recorded data for this seed gives the core

  `S₀ = \{2,3,5,7,13,17,19,23,29,37,43,101\}`

(matching `lemmas/two-sided-singleton-witness-theorem.md`'s stated data for this
seed exactly). Building the sequence directly from the problem's recursive rule
(smallest integer exceeding the previous term with `\gcd>1` against every earlier
term — a fully deterministic finite computation, independently re-run for this
write-up) gives, for the first seven terms:

```
n   a_n     factorization            P(a_n)∩S₀
1   11305   5·7·17·19                {5,7,17,19}
2   11310   2·3·5·13·29              {2,3,5,13,29}
3   11312   2^4·7·101                {2,7,101}
4   11319   3·7^3·11                {3,7}          [canonical witness of B'; n_B]
5   11322   2·3^2·17·37              {2,3,17,37}
6   11326   2·7·809                  {2,7}
7   11330   2·5·11·103               {2,5}          [canonical witness of A'; n_A]
```

The rogue pair (the disjoint-base-type extended-persistent pair this workspace has
flagged as the standing open item for this seed) is `A' := \{2,5\}`, `B' := \{3,7\}`,
with canonical witnesses `n_A = 7` (`a_7 = 11330 = 2\cdot5\cdot11\cdot103`) and
`n_B = 4` (`a_4 = 11319 = 3\cdot7^3\cdot11`). **Note the order: `n_B = 4 < n_A = 7`**,
i.e. `B'`'s canonical witness is EARLIER than `A'`'s — the opposite of `4807`, where
`n_A = 6 < n_B = 7`. `F' := P(a_7)\setminus S₀ = \{11,103\}` (NOT a singleton,
`|F'|=2`). `F'' := P(a_4)\setminus S₀ = \{11\}` — a **singleton**. (For `4807`, it
was `F'` — the `A'`-side witness's extra factor set — that was the singleton; here
it is `F''` — the `B'`-side witness's extra factor set — that is the singleton. This
is exactly the consequence of the order swap and is handled correctly below by
relabeling, not by reusing `4807`'s case verbatim.)

### Step 1 — the free side: canonical-witness singleton resolves the `A'`-side directly

Since `F'' = P(a_4)\setminus S₀ = \{11\}$ is already a singleton **at the canonical
witness** `n_B = 4` itself (no window issue — this is the direct, "for free" case,
exactly analogous to `4807`'s `B'`-side resolution via its canonical witness
`n_A = 6`), the certified Singleton-Side FAH Lemma (`lemmas/singleton-side-fah.md`),
applied in its primary form (witnesses `n_A=7$ of type `A'`, `n_B=4$ of type `B'$,
`F''=\{11\}$ singleton) gives directly:

  `11 \mid a_n` for **every** `n > n_B = 4` with `\rho(n) = A' = \{2,5\}`.  (zero
  exceptions, no Finite-Window Lemma needed for this side)

*Proof (recap of the cited Lemma's own argument, specialized).* By the certified
Generalized Bounded Witness Lemma applied with fixed witness index `m := n_B = 4`
(`\rho(4)=B'`): for every `n>4` with `\rho(n)=A'`, `a_n` is divisible by some prime of
the fixed finite set `P(a_4)\setminus S₀ = F'' = \{11\}$. Since this set has exactly
one element, that prime must be `11` itself. ∎

Independent computational check (own script, direct simulation to `N=2000$ terms,
60 total `A'$-occurrences with `n>4$ found, all `2000+1$): **zero** violations of
`11\mid a_n$ among these.

### Step 2 — the residual side: the Reduced-Alphabet Corollary isolates a single class

The residual open side is `B'$ (since `F' = \{11,103\}$ is not singleton at the
canonical witness `n_A=7$). Applying the certified Confined-GCD Lemma
(`lemmas/confined-gcd-lemma.md`) requires its own hypothesis `n_A < n_B$ (its "`A'$"
and "`B'$" labels denote, respectively, the type whose canonical witness comes FIRST
and the type whose canonical witness comes SECOND) — since here the seed's actual
witness order is `n_B(=4) < n_A(=7)$, we must apply the Lemma with the two extended
types **relabeled** so its own internal ordering hypothesis holds:

  `\tilde A' := B' = \{3,7\}` (witness `\tilde n_A := n_B = 4`),
  `\tilde B' := A' = \{2,5\}` (witness `\tilde n_B := n_A = 7`),

so that `\tilde n_A = 4 < 7 = \tilde n_B$, matching the Lemma's own hypothesis order.
With this relabeling, `\tilde F'' := P(a_{\tilde n_B})\setminus S₀ = P(a_7)\setminus S₀
= F' = \{11,103\}$, and `\tilde b := \prod_{p\in\tilde F''} p^{v_p(a_7)} = 11^1\cdot
103^1 = 1133$ (since `a_7 = 2\cdot5\cdot11\cdot103$ has `v_{11}=v_{103}=1$).

By the Confined-GCD Lemma (applied with this relabeling): for every `n > \tilde n_B =
7` with `\rho(n) = \tilde A' = B'$, writing `g_n := \gcd(a_n,a_7)$, we have
`g_n \in \mathrm{Div}(1133) = \{1,11,103,1133\}$, `g_n>1$, and for `q^*=11$:
`11\mid a_n \iff 11\mid g_n$. By the certified Reduced-Alphabet Corollary
(`lemmas/reduced-alphabet-corollary.md`), the residual exception alphabet is

  `D_{\mathrm{bad}}(11) = \{d\in\mathrm{Div}(1133): d>1,\ 11\nmid d\} = \{103\}$

(direct enumeration: `1133 = 11\cdot103$, divisors `\{1,11,103,1133\}$; excluding `1$
by `g_n>1$ and excluding `11,1133$ by `11\mid d$ leaves exactly `\{103\}`). So
"`d=103$ never occurs" is *equivalent* to "literal FAH-for-`11$ holds on the `B'$-side
of this pair for `n>7$," i.e. `11\mid a_n$ for every `n>7$ with `\rho(n)=B'$, with
zero exceptions. This is the round's precise target, exactly mirroring how `4807$'s
Step 4h reduced its residual class `d=13$ to a literal-FAH question on its own
`A'$-side.

### Step 3 — a non-canonical singleton `\tilde B'$(`=A'$)-witness, already on record

The certified Two-Sided Singleton Witness Theorem (round 18–19) already recorded,
for this exact seed, a **non-canonical** `A'$-occurrence at index `x_1 = 103` with
`P(a_{103})\setminus S₀ = \{11\}$ — a singleton. Direct computation confirms this
independently: `a_{103} = 12100 = 2^2\cdot5^2\cdot11^2$, so `P(a_{103})\cap S₀ =
\{2,5\} = A' = \tilde B'$ (confirming `\rho(103) = \tilde B'$, i.e. `103` is a
genuine `\tilde B'$-occurrence, exactly the type the Finite-Window Literalization
Lemma requires its witness `x_1` to have — NOT `B'` itself; this is the crux of the
relabeling: `x_1` must witness the type `\tilde B' = A'`, since in the relabeled pair
it is `\tilde A' = B'$ whose literal absorption we are trying to establish) and
`P(a_{103})\setminus S₀ = \{11\}$ exactly.

### Step 4 — the Finite-Window Literalization Lemma, applied with the relabeled pair

Recall the certified Lemma's exact statement (`lemmas/finite-window-literalization-
lemma.md`): *let `(A',B')` be a rogue pair at core `S₀` with canonical witnesses
`n_A<n_B$. Suppose there is an index `x_1` with `\rho(x_1)=B'$ and `P(a_{x_1})
\setminus S₀=\{q\}$ a singleton. If, in addition, there is no index `n` with
`n_B<n\le x_1` and `\rho(n)=A'$, then `q\mid a_n$ for literally every `n>n_B$ with
`\rho(n)=A'$.*

We apply it with `A' := \tilde A' = B' = \{3,7\}$ (canonical witness `n_A := \tilde
n_A = 4`), `B' := \tilde B' = A' = \{2,5\}$ (canonical witness `n_B := \tilde n_B =
7`), `q := 11`, `x_1 := 103`. All hypotheses are satisfied:
  - `n_A = 4 < 7 = n_B$ ✓ (the required canonical order, now correctly matching after
    relabeling).
  - `\rho(x_1) = \rho(103) = \{2,5\} = \tilde B'$ = the Lemma's "`B'`" role ✓ (Step 3).
  - `P(a_{103})\setminus S₀ = \{11\}$, a singleton, `q=11` ✓ (Step 3).
  - Remains to check: no index `n` with `n_B(=7) < n \le x_1(=103)` has `\rho(n) =
    \tilde A' = B' = \{3,7\}$ (the Lemma's "`A'`" role in this application).

### Step 5 — verifying the Lemma's finite hypothesis (explicit, exhaustive computation)

We must check: is there any index `n` with `7 < n \le 103` and `\rho(n) = B' =
\{3,7\}`? Extending the sequence computation of the Setup out to `n=103` (own
from-scratch simulation, cross-checked below against a second independent
implementation) and scanning every `\rho(n) = P(a_n)\cap S₀` for `n=8,\dots,103`
against the target `\{3,7\}`: **no such index occurs**. Concretely, the full list of
`B'`-occurrences (indices `n` with `\rho(n)=\{3,7\}` exactly) found by direct
enumeration up to `n=2000` is

  `4, 119, 290, 349, 406, 519, 635, 692, 806, \dots`

— the canonical witness `n=4` itself, then the *next* `B'`-occurrence is `n=119`,
strictly beyond `x_1=103`. In particular there is **no** `B'`-occurrence anywhere in
the window `(7,103]` (nor, more strongly, anywhere in the larger window `(4,103]`,
which contains `(7,103]$ as a subset, so the stronger empty check already implies the
one actually required). This is a finite, exhaustive, fully verified check (not
merely sampled): the sequence between indices `8` and `103` was scanned in its
entirety and every one of its `96` extended types was compared against `\{3,7\}$,
with no match.

### Step 6 — conclusion: `d=103` never occurs, unconditionally

By Step 3–4 (`x_1=103` is a genuine `\tilde B'(=A')$-occurrence with singleton
complement `\{11\}$) and Step 5 (no `\tilde A'(=B')$-occurrence in `(7,103]$,
verified exhaustively), the Finite-Window Literalization Lemma applies directly with
the relabeled pair, giving:

  `11 \mid a_n` for **every** `n > \tilde n_B = 7` with `\rho(n) = \tilde A' = B' =
  \{3,7\}$.  (literal, zero exceptions)

Combined with Step 2's Confined-GCD confinement `g_n \in \{1,11,103,1133\}`,
`g_n>1`, and equivalence `11\mid a_n \iff 11\mid g_n$: since `11\mid a_n$ always (for
`n>7$, `\rho(n)=B'$), `11\mid g_n$ always, so `g_n$ — always a divisor of `1133 =
11\cdot103$ exceeding `1$ and divisible by `11$ — can only be `11` or `1133` (the two
divisors of `1133` divisible by `11`; `103` and `1` are excluded, `103` because it is
not divisible by `11`, `1` because `g_n>1`). Hence:

  **`g_n \ne 103` for every `n>7` with `\rho(n)=B'` — the residual class `d=103` never
  occurs. This is proved unconditionally, not merely observed.**

(As an independent computational cross-check, not itself part of the proof: a direct
simulation of `a_1=11305` out to `2000` terms found `16` occurrences of `B'` with
`n>7`, all `16` giving `g_n \in \{11,1133\}` and none giving `g_n=103` — consistent
with, and now fully explained by, the proof above. A second, independent script
(bitmask-based, distinct implementation) extended this check to `45{,}000` terms —
matching the scale of `4807`'s own certified closure — finding `457` `B'`-occurrences
with `n>7`, again zero violations, and confirming the window `(4,103]` (hence
`(7,103]`) is empty of `B'`-occurrences throughout.)

**What this establishes for the rogue pair as a whole.** Combining this with Step 1's
`A'`-side resolution (`11\mid a_n` for every `n>4` with `\rho(n)=A'`, zero
exceptions, established directly via the canonical singleton witness `n_B=4`, no
window argument needed): **literal Joint FAH holds, unconditionally, for
`a_1=11305`'s standing rogue pair, in both directions**, with the single shared
witness prime `q=11`:

  `11 \mid a_n$ for every `n>4$ with `\rho(n)=\{2,5\}$, and
  `11 \mid a_n$ for every `n>7$ with `\rho(n)=\{3,7\}$.

(Remark, not part of the proof but worth recording: since Step 5's exhaustive check
already shows no `B'`-occurrence in the larger window `(4,103]` — a strict superset
of the `(7,103]` the Lemma's hypothesis required — the set of indices `n>7` with
`\rho(n)=B'` is in fact identical to the set of indices `n>4` with `\rho(n)=B'`, for
this seed: there is no `B'`-occurrence at all with `4<n\le7`. So the literal
conclusion for the `B'`-side also, incidentally, holds "from `n>4`" in the sense that
no example distinguishes the two thresholds — but the threshold *guaranteed by the
certified Lemma's own statement* is `n>7`, and that is the one stated as the proved
result above; the coincidence with `n>4` is an extra fact about this specific seed's
data, not a strengthening of the Lemma itself.)

### Honest scope — what this does and does not establish

**Establishes (unconditional, complete):** for this one seed (`a_1=11305`) and this
one standing rogue pair, literal (zero-exception) Joint FAH holds, fully proved. The
Reduced-Alphabet Corollary's residual class `d=103` is closed: it never occurs, not
merely "not yet observed." This is exactly the round-27 scoped deliverable, and it
required correctly handling the canonical-order swap (`n_B<n_A` here vs `n_A<n_B` at
`4807`) via an explicit relabeling before invoking the certified Lemma — not a blind
substitution of `4807`'s case.

**Does NOT establish:**
- **General FAH / Cofinite FAH for arbitrary `a_1`.** Exactly as with `4807`'s Step
  4h: the mechanism used seed-specific numerical facts (the existence of the
  non-canonical singleton witness `x_1=103`, and the finite-window vacancy verified
  in Step 5), not a general structural argument. The Two-Sided Singleton Witness
  Theorem's own scope note — that the underlying existence hypothesis is "a genuine,
  unproved, narrower existence question" — is unaffected; this round supplies no new
  argument for why such a witness must exist for a general rogue pair at a general
  `a_1`, only that it happens to exist, and is usable, for this second specific seed.
- **A third seed, or any general family.** Not attempted; there is no known third
  standing hard rogue-pair test seed in this workspace as of this round (per the
  round-27 explorer's own ceiling assessment: only two properly-recruited-core hard
  seeds are known after ~27 rounds of search).
- **The `|F'|\ge3` or `|F''|\ge3`, or higher-multiplicity, general case.** Untouched.

**TWO-SEED SUMMARY (the honest state of this line of work as of round 27).** Both of
the workspace's standing hard rogue-pair test seeds (`a_1=4807`, closed round 26;
`a_1=11305`, closed this round) now have literal Joint FAH fully, unconditionally
proved. Both closures use the identical certified mechanism and both required a
seed-specific search-found non-canonical singleton witness as an unproved-in-general
input. This is genuine, scoped, verified progress — not a vacuity finding, and not a
repeat of an already-closed case — but it is explicitly NOT a step toward the general
theorem (†): the mechanism's existence hypothesis remains exactly as open for a
general seed as it was before either closure, and there is no known third test case
left to apply it to.

## Promotable lemmas (round 27 addendum)

- **`a_1=11305` residual-class closure (seed-specific, fully proved)**: the
  Reduced-Alphabet Corollary's residual class `d=103` for this seed's standing rogue
  pair (`A'=\{2,5\}`, `B'=\{3,7\}`, `n_A=7`, `n_B=4`) never occurs; literal Joint FAH
  holds unconditionally for this one rogue pair (Step 4i, Steps 1–6 above). Proved by
  a correctly-relabeled reapplication of the already-certified Finite-Window
  Literalization Lemma (no new lemma content this round — the Lemma itself was
  already certified in round 26 and required no modification). A concrete, fully
  verified, reusable data point for any approach using this seed as a test bed (e.g.
  `seed-coupling-induction`) — no future round needs to re-derive or re-check this
  seed's residual class. No new standalone lemma file is proposed for certification
  this round (the Finite-Window Literalization Lemma is already certified and this
  round only reapplies it); the reviewer may wish to certify the combined "both
  standing seeds have literal Joint FAH" fact as a short addendum note on the
  existing `lemmas/finite-window-literalization-lemma.md` file if desired.
