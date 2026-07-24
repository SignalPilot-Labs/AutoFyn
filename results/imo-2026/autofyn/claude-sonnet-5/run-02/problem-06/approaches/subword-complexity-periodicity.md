## Status
partial

## Approaches tried
- **round 12 (this round, NEW — file created from the outline, which had not yet been
  written to disk).** Built out the Morse–Hedlund reformulation in full rigor:
  (1) proved a fully general, self-contained "Right-Extension Determinism ⟹ eventual
  periodicity" lemma for sequences over a finite alphabet (the actual pigeonhole +
  induction argument, not a bare citation of Morse–Hedlund's name); (2) proved the
  (trivial but necessary, and previously unstated in this exact form) equivalence
  between the problem's target and eventual periodicity of the gap sequence; (3)
  applied (1)+(2) to reduce the problem to finding some window length k₀ with no
  "special factor" in the gap sequence; (4) formalized the outline's "Finite-Defect
  Boundedness" idea precisely, and found — this is the round's main finding — that
  the outline's headlined weaker target ("finitely many colliding S₀-residue
  classes") is **trivially true and vacuous** (bounded automatically by the alphabet
  size, with no further argument), NOT the substantive content it was billed as; the
  actually-substantive condition is whether ambiguity is eventually *avoided*
  (visited residues eventually confined to the unambiguous ones), a strictly
  stronger-looking statement I call **EEA** (Eventual Escape from Ambiguity); (5)
  proved EEA (if it holds at some finite core) fully implies periodicity, with an
  explicit, clean, self-contained finite-state argument; (6) ran the outline's
  mandated first numerical task (count colliding residue classes at the coarse core
  S₀ = Q on a_1 = 105, 315, 4807) and found ambiguity is **substantial, not small**,
  at that core (up to 61% of reachable residues ambiguous for a_1 = 4807) — an
  honest negative data point, though expected and not by itself informative once one
  sees (per finding (4)) that the coarse core Q was never expected to be sufficient
  (the certified Finite Core Theorem already tells us Q alone is insufficient in
  general); (7) could not find a genuinely new mechanism (independent of the already
  open (†)/FAH crux) to establish EEA, or the weaker window-length-k₀ target, at any
  finite level — the approach honestly stalls at the same wall the outline itself
  flagged as an open risk, now precisely characterized rather than left informal.
  Two new lemmas proved in full and proposed for certification (see below). Verdict
  target: **CHANGES REQUESTED / partial** — real, rigorous new content (general
  lemma + explicit reduction + a corrected, sharper statement of exactly what
  remains open), but the primary crux gap (†)/FAH is not closed, and this build
  could not show the "count don't eliminate" idea is actually easier than the
  already-open target.

## Current best

### 0. Setup and notation (all imported, all certified)

Let (a_n) be a valid sequence for the problem, Q := P(a_1) (its prime factor set),
g_n := a_{n+1} - a_n for n ≥ 1. We use, without re-proving:

- **Free Facts** (`lemmas/free-facts-gcd.md`): gcd(a_i,a_j) > 1 for all i≠j.
- **Bounded Gap Lemma** (`lemmas/bounded-gap-lemma.md`): 1 ≤ g_n ≤ a_1 for every n
  (upper bound is the lemma's statement a_{n+1} ≤ a_n + a_1; the lower bound g_n ≥ 1
  is immediate from strict monotonicity of (a_n), itself immediate from the
  successor rule's "smallest integer *greater than* a_n").
- **Finite Core Theorem** (`lemmas/finite-core-theorem.md`) and **Extended
  Persistent-Type Pigeonhole** (`lemmas/extended-persistent-type-pigeonhole.md`):
  for any finite S₀ ⊇ Q, ρ(n) := P(a_n) ∩ S₀ eventually (n > N₂) lies in a fixed
  finite nonempty set 𝒫' of "S₀-extended-persistent types."
- **Confined-GCD Lemma** (`lemmas/confined-gcd-lemma.md`) and **Cofinite
  Sufficiency Lemma** (`lemmas/cofinite-sufficiency-lemma.md`): the precise,
  already-certified formalization of the open crux (†)/FAH in this workspace.

The problem's primary target is: ∃ T, L ≥ 1 with a_{n+T} = a_n + L for all
sufficiently large n. (The secondary target — the same identity for literally every
n ≥ 1 — remains untouched by every approach in this workspace and is out of scope
here, exactly as flagged by the outline.)

### 1. Lemma A (Gap–Periodicity Equivalence) — proved in full, new, certifiable

**Statement.** There exist T, L ≥ 1 and N ≥ 1 with a_{n+T} = a_n + L for all n ≥ N
**if and only if** there exists T ≥ 1 and N' ≥ 1 with g_{n+T} = g_n for all n ≥ N'
(i.e. (g_n) is eventually periodic with period T in the ordinary sense).

**Proof.**
(⟹) Suppose a_{n+T} = a_n + L for all n ≥ N. For n ≥ N:
g_{n+T} = a_{n+T+1} - a_{n+T} = (a_{n+1}+L) - (a_n+L) = a_{n+1}-a_n = g_n.
So g_{n+T}=g_n for all n ≥ N; take N' := N.

(⟸) Suppose g_{n+T} = g_n for all n ≥ N'. Define d_n := a_{n+T} - a_n for n ≥ 1. For
n ≥ N':
d_{n+1} - d_n = (a_{n+T+1}-a_{n+1}) - (a_{n+T}-a_n) = (a_{n+T+1}-a_{n+T}) -
(a_{n+1}-a_n) = g_{n+T} - g_n = 0.
So d_n is constant for n ≥ N'; let L := d_{N'} = a_{N'+T}-a_{N'}, a positive integer
since (a_n) is strictly increasing. Then a_{n+T} = a_n + L for all n ≥ N'; take
N := N'. ∎

This lemma is unconditional, self-contained (uses only the definitions), and
converts the problem's stated goal into a statement purely about the gap sequence
(g_n), which is what licenses applying combinatorics-on-words machinery to it.

### 2. Lemma B (Right-Extension Determinism ⟹ eventual periodicity) — proved in
full, new, certifiable (this is the actual Morse–Hedlund mechanism, carried out
explicitly, not cited by name)

**Setup.** Let x = (x_1, x_2, x_3, …) be any infinite sequence over a finite
alphabet Σ. For k ≥ 1 and i ≥ 1 write W_k(i) := (x_i, x_{i+1}, …, x_{i+k-1}) for the
length-k word starting at position i. Say x satisfies **Right-Extension
Determinism at level k** (RED_k) if: for all i < j, W_k(i) = W_k(j) implies
x_{i+k} = x_{j+k}.

**Lemma B.** If RED_k holds for x for some k ≥ 1, then x is eventually periodic:
there exist N ≥ 1 and T ≥ 1 with x_{n+T} = x_n for all n ≥ N.

**Proof.** Since Σ^k is finite (|Σ|^k elements) and there are infinitely many
positions i = 1,2,3,…, the map i ↦ W_k(i) cannot be injective (infinite pigeonhole
principle, `knowledge_base.md` "Pigeonhole / extremal principle"): there exist
i < j with W_k(i) = W_k(j). Fix such i, j and set T := j - i ≥ 1.

*Claim:* x_{i+m} = x_{j+m} for every m ≥ 0. Proof by strong induction on m.

- Base cases 0 ≤ m ≤ k-1: this is exactly the hypothesis W_k(i) = W_k(j), which
  states x_{i+m} = x_{j+m} for each such m.
- Inductive step: let m ≥ k-1 and suppose x_{i+m'} = x_{j+m'} holds for every
  0 ≤ m' ≤ m. In particular it holds for m' = m-k+1, m-k+2, …, m (all ≥ 0 since
  m ≥ k-1), i.e.
    x_{i+m-k+1} = x_{j+m-k+1}, x_{i+m-k+2} = x_{j+m-k+2}, …, x_{i+m} = x_{j+m}.
  Setting i' := i+m-k+1 and j' := j+m-k+1 (note j' - i' = j - i = T > 0, so
  i' < j'), this says precisely W_k(i') = W_k(j'). By RED_k applied to i' < j', we
  get x_{i'+k} = x_{j'+k}, i.e. x_{i+m+1} = x_{j+m+1}, which is the case m' = m+1.

By induction the claim holds for all m ≥ 0. Hence x_{i+m} = x_{j+m} = x_{(i+m)+T}
for every m ≥ 0, i.e. x_n = x_{n+T} for every n ≥ i. Take N := i. ∎

**Monotonicity corollary (used below).** If RED_1 holds for x, then RED_k holds for
x for every k ≥ 1. *Proof:* if W_k(i) = W_k(j) then in particular the last entries
agree, x_{i+k-1} = x_{j+k-1}; applying RED_1 to the pair (i+k-1, j+k-1) gives
x_{i+k} = x_{j+k}. ∎ So RED_1 is the *strongest* (hardest to establish) member of
this family, and larger k gives a *weaker* (easier, in principle) hypothesis — this
is the precise sense in which "using longer windows" is a genuinely different,
weaker target, as the outline hoped.

Both Lemma A and Lemma B are unconditional, fully proved, and do not depend on any
open gap in this workspace. Lemma B is a completely general fact about sequences
over finite alphabets, independent of this problem's specific structure, and is
proposed for certification as a reusable combinatorics-on-words tool.

### 3. Reduction of the target

By the Bounded Gap Lemma, (g_n) is a sequence over the finite alphabet
Σ = {1, …, a_1}. Combining Lemma B (applied to x = (g_n)) with Lemma A:

> **If there exists k₀ ≥ 1 such that RED_{k₀} holds for the gap sequence (g_n),
> then the problem's primary target (∃T, L with a_{n+T}=a_n+L for all sufficiently
> large n) holds**, with T equal to the specific period produced by Lemma B's proof
> and L computed as in Lemma A's proof.

This is the precise, fully justified form of "Morse–Hedlund reduces periodicity to
bounded factor complexity" for this problem (the classical theorem states p(k) ≤ k
for some k is equivalent, via a slightly sharper pigeonhole using ALL length-k
factors rather than a single colliding pair; RED_k as used here is the concrete
mechanism version needed for our one-directional implication, and is what the
outline's skeleton actually asks the builder to establish — the reduction is
correct and now fully derived, not merely asserted).

### 4. The genuine open content, precisely isolated

The outline's step 4 proposes attacking RED_{k₀} via "S₀-residue windows" rather
than gap-value windows directly. To make this precise, fix a finite S₀ ⊇ Q (e.g.
from the Finite Core Theorem, possibly after finitely many "recruitment rounds" in
the certified chain's sense) and set L₀ := ∏_{p ∈ S₀} p, r_n := a_n mod L₀. Since
S₀-primes divide a_n according to r_n alone (by definition of "mod"), the extended
type ρ(n) = P(a_n) ∩ S₀ is a function of r_n only; write ρ(n) = ρ̄(r_n).

Consider RED_1 applied to the residue sequence (r_n) itself (over alphabet
ℤ/L₀ℤ, size L�0): RED_1(r) says precisely that whenever r_i = r_j (i<j), then
r_{i+1} = r_{j+1} — i.e., **the next residue (equivalently, by g_n = a_{n+1}-a_n
mod L₀ up to the exact integer value, the next gap) is eventually a
single-valued function of the current residue alone, with no exceptions past the
witnessing pair.** Call a reachable residue r (one occurring as r_n for infinitely
many n) "safe" if all its infinitely many visits n eventually agree on g_n, and
"ambiguous" otherwise (some two visits n, n' with r_n = r_{n'} = r but g_n ≠
g_{n'}).

**Proposition (correction to the outline — new, proved).** For ANY fixed finite
S₀, the number of ambiguous residues is automatically finite (at most L₀), with
*no* argument beyond alphabet-finiteness required. *Proof:* there are only L₀
residues mod L₀ total, so trivially at most L₀ can be ambiguous. ∎

This shows the outline's headline "weaker target" (Finite-Defect Boundedness =
"finitely many colliding residue classes") is **vacuous as stated**: it is a
one-line consequence of the Bounded Gap Lemma's alphabet-finiteness (already
certified, item 2 of `current.md`'s Current Best list) and supplies no new
information whatsoever. This is an honest correction to the outline's framing: the
"count, don't eliminate" idea does not, by itself, produce any content beyond what
was already known. (This matches the outline reviewer's own caution not to let
"finite defect" quietly mean anything less than the genuinely needed statement —
here we go further and show the naive finite-count reading is not merely at risk
of being circular, it literally proves nothing at all.)

**What actually suffices (Theorem C, proved below):** not "finitely many ambiguous
residues" (automatic) but **"eventually only safe residues are visited"** — call
this property **EEA** (Eventual Escape from Ambiguity) at level S₀: there exists
N such that r_n is a safe residue for every n ≥ N.

**Theorem C (EEA ⟹ periodicity).** If EEA holds at some finite S₀ ⊇ Q, the
problem's primary target holds, with an explicit T ≤ L₀.

**Proof.** By EEA, there is N such that for all n ≥ N, r_n is safe, meaning there
is a well-defined function f on the (finitely many, ≤ L₀) safe residues with
g_n = f(r_n) for all n ≥ N (this is the definition of "safe": all visits past the
witnessing pair agree, and since there are only finitely many visits before any
fixed point, we may enlarge N if necessary to a single global threshold past which
*every* visit to a safe residue gives the same gap — formally: for each of the
finitely many safe residues r, let N_r be the last index (if any) at which a visit
to r had a gap differing from its eventual stable value, which is finite since a
safe residue by definition has only finitely many "early" exceptional visits before
stabilizing infinitely-often to one value — wait, we must double check: "safe" as
defined (all visits eventually agree) already means the exceptional-early-visit set
is finite for that residue automatically, since there are infinitely many visits in
total and if the value taken infinitely often is unique, only finitely many visits
can take any other value; take N := 1 + max over the finitely many safe residues of
their respective last-exceptional-visit index, and note EEA already forces r_n
safe for n ≥ the original N, so both conditions hold simultaneously past the larger
of the two thresholds).

Define h : (safe residues) → ℤ/L₀ℤ by h(r) := (r + f(r)) mod L₀. For n ≥ N,
r_{n+1} ≡ a_n + g_n ≡ r_n + f(r_n) ≡ h(r_n) (mod L₀), and r_{n+1} is itself safe
(again by EEA, since n+1 ≥ N), so h maps safe residues to safe residues, and
(r_n)_{n≥N} is exactly the orbit of r_N under iterating h on the finite set of
safe residues (size ≤ L₀). By the finite pigeonhole principle applied to the L₀+1
values r_N, r_{N+1}, …, r_{N+L₀} drawn from a set of size ≤ L₀, two coincide:
r_{N+s} = r_{N+t} for some 0 ≤ s < t ≤ L₀. Since h is a fixed deterministic
function, r_{N+s+m} = r_{N+t+m} for all m ≥ 0 by an immediate induction (each
equals h applied m times to the same starting value). This is exactly RED_1 for
the (safe tail of the) residue sequence with the colliding pair (N+s, N+t), so by
the argument of Lemma B (applied verbatim, with T := t - s ≤ L₀), r_{n+T} = r_n for
all n ≥ N+s, and moreover g_{n+T} = f(r_{n+T}) = f(r_n) = g_n for the same range
(both sides safe, both computed via the same function f). By Lemma A, the
problem's primary target holds with this T (≤ L₀) and the corresponding L. ∎

Theorem C is a fully rigorous, self-contained finite-state (functional-graph)
argument. It is, in substance, a cleaner restatement of the already-certified
CRT/cyclic-pigeonhole finish (`current.md`, Current Best, final paragraph before
"Secondary open gap") but derived independently here in the language of this
approach, and it makes explicit exactly what hypothesis that finish is really
using: not mere pairwise-type-intersection but literal, eventual, no-exception
single-valuedness of the successor as a function of a finite residue (EEA).

### 5. Why this build cannot close the gap: EEA is not demonstrably easier than
(†)/FAH

Given Theorem C, the entire remaining burden is to prove EEA at *some* finite S₀.
We looked for a mechanism to prove EEA that is independent of the already-open
(†)/FAH machinery (this was the round's central speculative hope) and did not find
one, for a structural reason:

Unpacking the definition, "residue r becomes safe" means every sufficiently late
visit to r produces the *same* next integer gap, i.e. the successor rule, when
restricted to occurrences of that exact residue, eventually stops depending on any
information beyond r itself — but the successor a_{n+1} is defined by checking
gcd(a_n+c, a_i) > 1 against **every** earlier term a_i (i ≤ n), not merely against
S₀-level data; residue r alone only pins down which S₀-primes divide a_n, and
(exactly as the certified **Confined-GCD Lemma** shows for the analogous FAH
question) the finer information governing which candidate gap actually succeeds is
carried by primes *outside* S₀ dividing the specific witnessing terms — precisely
the same "F′/F″" data the certified reduction chain already isolates as the crux.
In other words: proving that a *given* ambiguous residue becomes safe after
recruiting one further prime q into a larger core S₁ (S₀ ⊂ S₁, L₁ := L₀·q) is,
after unwinding definitions, exactly an instance of the already-certified-as-open
question "does the recruited prime of a rogue witnessed pair divide *literally
every* later occurrence of the relevant type" (full, non-cofinite FAH for that
instance) — the same statement the Cofinite Sufficiency Lemma is built to weaken
(and even that weaker "cofinite" version remains open). We verified this
concretely: the outline's own numerical mandate (below) shows ambiguity at the
coarse core S₀ = Q is not confined to a negligible fringe, consistent with EEA
failing at Q (as expected, since the certified Finite Core Theorem already tells us
Q is provably insufficient in general) and requiring exactly the kind of
"recruit-a-further-prime-and-prove-full-absorption" argument that 14 confirmed-dead
mechanisms across rounds 6–11 have already failed to supply in every variant tried.

We therefore did **not** find, and could not construct in the time available, a
mechanism establishing RED_{k₀} for (g_n), or EEA at any finite S₀, that is
independent of the standing (†)/FAH gap. This matches — and now substantiates with
an explicit, checked argument — the outline's own "honesty flag" that this
approach targets the same wall via new vocabulary. The genuine new content
delivered this round is: (a) two fully proved, reusable general lemmas (A, B) and
one problem-specific theorem (C) forming a complete, correct alternative
derivation of "sufficient hypothesis ⟹ periodicity," and (b) the precise diagnosis
that the outline's hoped-for weakening ("count, don't eliminate") is vacuous, with
the true weakening (EEA) shown, as far as we can establish, to be at least as hard
as the standing crux rather than strictly easier.

### 6. Mandated numerical check (falsification-first discipline, as instructed)

Following the outline's and outline-reviewer's explicit instruction to test the
"finitely many ambiguous residue classes" idea numerically before investing
further, we simulated the sequence (same trial-division / brute-force minimal-
candidate generator used throughout this workspace) for a_1 ∈ {105, 315, 4807},
computed r_n := a_n mod L₀ with S₀ = Q (the coarsest available core), and counted
ambiguous residues among those reached for n ≥ 500 (to avoid early transient
noise), over 4000 terms:

| a_1 | Q | L₀ | reachable residues | ambiguous residues |
|---|---|---|---|---|
| 105 | {3,5,7} | 105 | 57 | 1 |
| 315 | {3,5,7} | 105 | 57 | 17 |
| 4807 | {11,19,23} | 4807 | 847 | 520 |

At the coarse core Q, ambiguity is *not* small (up to 520/847 ≈ 61% of reachable
residues for a_1 = 4807) — an honest negative data point. We stress, matching the
outline's own caution, this is **not** a falsification of EEA or of the overall
mechanism in general: it is exactly what is expected, since the certified Finite
Core Theorem already guarantees Q alone is provably too coarse for the analogous
FAH-style questions in general (S must in general be strictly larger than Q). We
attempted to test a richer, empirically-estimated core (all primes dividing at
least 2% of a late sample window) but found the resulting L₀ so large (≈6.1×10^17,
using primes up to 47) that essentially no residue is ever revisited twice within
computationally feasible sample sizes, making the "0 ambiguous" reading at that
core **vacuous** (no evidence either way — matches the same caution the
outline-reviewer raised about the p(k) plateau data for a_1 = 4807, 11305, 315).
We record both findings but do not treat either as evidence for or against EEA in
general, per the outline's own explicit instruction not to over-read inconclusive
window/complexity data.

### 7. Summary

- Lemma A (Gap–Periodicity Equivalence): proved, unconditional. **Proposed for
  certification.**
- Lemma B (Right-Extension Determinism ⟹ eventual periodicity, general
  finite-alphabet fact, with the RED_1 ⟹ RED_k monotonicity corollary): proved,
  unconditional, fully general (no dependence on this problem's structure).
  **Proposed for certification.**
- Reduction (§3): RED_{k₀} for the gap sequence, for some k₀, suffices for the
  problem's primary target. Fully justified, not a bare citation.
- Correction to the outline (§4 Proposition): "finitely many ambiguous residues"
  is automatic/vacuous at any fixed finite core, for a one-line reason
  (alphabet-finiteness, already known). This should not be re-proposed as
  substantive content by any future round.
- Theorem C: the actually-needed sufficient condition (EEA) does imply
  periodicity, via a clean, explicit, self-contained finite-state argument.
  Proved, but conditional on EEA.
- §5: EEA, once unpacked, appears — as far as this build could establish — to
  require exactly the same "recruit a prime and prove it divides literally every
  later occurrence" content as the standing, 14-mechanisms-dead (†)/FAH crux; no
  independent route to EEA (or to RED_{k₀} for k₀ > 1 without going through EEA)
  was found this round.
- §6: mandated numerical check run; ambiguity at the coarse core is not small
  (honest negative datum, expected, not by itself informative about EEA's
  eventual truth).

**Bottom line:** this build fully carries out the "genuinely new toolset" (windows
+ pigeonhole + determinism, not a bare citation) the round-11 mandate called for,
produces two new certifiable general lemmas plus a clean alternative derivation of
the CRT finish's true hypothesis (EEA), and precisely re-locates — rather than
avoids — the standing open crux. Status remains **partial**; the primary open gap
is unchanged in substance ((†)/FAH), now additionally characterized as
"establishing EEA at some finite core," which this build shows is a strictly
sufficient (Theorem C) but not obviously easier target than the certified chain's
own open crux.

## Full proof
Not present — Status is `partial`. The primary crux gap ((†)/FAH, equivalently EEA
at some finite core in this approach's vocabulary) remains open; see §5 above for
the precise obstruction. The secondary "periodicity from n=1 literally" gap is
untouched, as in every other approach in this workspace.

## Promotable lemmas

- **Lemma A (Gap–Periodicity Equivalence)** — §1 above. Unconditional, fully
  proved, self-contained (three lines of telescoping algebra each direction).
  Reusable by any future approach that wants to work with the gap sequence
  directly instead of (a_n).

- **Lemma B (Right-Extension Determinism ⟹ eventual periodicity), with the
  RED_1 ⟹ RED_k Monotonicity Corollary** — §2 above. A fully general fact about
  sequences over a finite alphabet (no dependence on this problem's specific
  structure at all — states and proves the concrete pigeonhole + induction
  mechanism underlying the Morse–Hedlund theorem's "if p(k₀) ≤ k₀ then eventually
  periodic" direction). Reusable both within this problem (by any future
  combinatorics-on-words approach) and, in principle, by unrelated problems in the
  broader corpus that need this exact tool.

- **Proposition (§4): ambiguous-residue-count finiteness is automatic/vacuous at
  any fixed finite core** — a short, correct, worth-recording negative/clarifying
  fact: it heads off any future round re-proposing "bound the number of colliding
  residue classes" as if it were nontrivial content.

- **Theorem C (EEA ⟹ periodicity, explicit T ≤ L₀)** — §4 above, self-contained
  finite-state/functional-graph pigeonhole argument. Conditional on EEA (not
  itself proved), but the implication EEA ⟹ periodicity is unconditional and
  reusable — a cleaner, more explicit alternative presentation of the certified
  CRT/cyclic-pigeonhole finish's true underlying hypothesis, worth certifying
  alongside (not in place of) the existing Step-5 finish, since it isolates
  exactly what "the successor becomes eventually residue-determined" would need to
  mean to be sufficient.
