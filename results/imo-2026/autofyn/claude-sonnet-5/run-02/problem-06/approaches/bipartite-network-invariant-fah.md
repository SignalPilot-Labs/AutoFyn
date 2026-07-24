## Status
unsolved (round 29 — corrected Step-1 disambiguation check run rigorously per
the outline-reviewer's mandate; it collapses to already-certified-but-
insufficient machinery / the already-open H2 termination question, and the
crux's actual load-bearing mechanism has no arithmetic analog. RETHINK, fast,
per the round-5 `reversible-transition-map` precedent — no iteration.)

## Approaches tried

- (round 29, first build.) Ran the outline-reviewer's **corrected** Step-1
  disambiguation check (NOT the outline's original, trivially-true "does some
  linking prime exist" question — that was already flagged vacuous by the
  reviewer, mirroring the round-9 Same-Type Free Facts Vacuity trap one level
  up) in full: "does the pool of linking primes used across network repairs
  stay bounded, and does the aimo-1000 repair *mechanism* (not just the
  existence of a repair prime) actually transplant?" **Outcome: the corrected
  question, worked through rigorously in both of its two possible
  formalizations, adds zero new leverage — see Propositions A–D below.
  RETHINK.**

## Current best

Nothing beyond the already-certified stack is established. What follows is
the disambiguation check itself, run to completion, which is the valuable
deliverable of this round per the dispatch: a precise, checked, honest
negative result — the 32nd confirmed-dead FAH mechanism variant (after the
30+ already on record; see `current.md`'s graveyard and
`lemmas/witness-discontinuity-obstruction.md`,
`lemmas/same-type-free-facts-vacuity.md`,
`lemmas/density-argument-vacuity-corollary.md` for the closest relatives).

### Setup recap (shared notation, all already certified)

Fix a finite core `S₀ ⊇ Q = P(a_1)`. For `n ≥ 1` write `ρ(n) := P(a_n) ∩ S₀`.
Two `ρ`-types `A', B' ⊆ S₀` (each occurring infinitely often) are the two
sides of a "rogue pair" if `A' ∩ B' = ∅` (fails the pairwise-intersection
condition (†) needed for FAH at this core level) but `A'` and `B'` come from
disjoint base types. The certified **Generalized Bounded Witness Lemma**
(`lemmas/generalized-bounded-witness-lemma.md`) is the single fact this whole
approach's disambiguation reduces to; restate it precisely because both
Propositions below depend on reading its exact quantifiers:

> Fix **any single** index `m` with `ρ(m) = B'`. Then **every** `n > m` with
> `ρ(n) = A'` has `a_n` divisible by some prime of the *fixed* finite set
> `F'_{A',B'} := P(a_m) \ S₀`.

Two things to note about this exact statement, both load-bearing below: (i)
the conclusion holds for **every** `n > m`, not just infinitely many — there
is no "failure event" at fixed `S₀` for this guarantee to ever need repairing;
(ii) the finite set `F'_{A',B'}` is fixed **once `m` is fixed** and does not
grow — it is already the tightest bound the current certified stack supplies.

### The corrected Step-1 question, formalized two ways

The outline-reviewer's corrected question ("does the pool of linking primes
used across network repairs stay bounded, not just does one exist somewhere")
is ambiguous between two readings, and the disambiguation check's actual job
is to show **both** readings collapse to already-understood territory.

**Reading α (fixed core, "repair" = re-choosing which prime of a bounded set
links a given occurrence).** At fixed `S₀`, is the set of primes that ever
serve as the link between an `A'`-occurrence and the `B'`-side bounded, as we
range over all `n > m`?

**Reading β (growing core, "repair" = enlarging `S₀` when the current
reference prime's coverage is judged insufficient and a fresh prime is
recruited, mirroring aimo-1000's edge-loss-then-repartition step).** As the
core is enlarged through a sequence `S₀ ⊆ S₁ ⊆ S₂ ⊆ ...` of successive
repair/recruitment events (each triggered by wanting to shrink the pool
toward a single dominant prime), does the total set of primes ever recruited
across all repairs stay bounded?

### Proposition A (Reading α is answered "yes," but by an already-certified,
already-known-insufficient fact — zero new leverage)

**Claim.** Reading α's pool is bounded, and in fact IS `F'_{A',B'}`, the
finite set from the Generalized Bounded Witness Lemma. No growth or "repair"
step of any kind is ever required to establish this — it is already true, for
free, for every `n > m` simultaneously, given a single fixed witness `m`.

**Proof.** By the Lemma's statement above, for every `n > m` with `ρ(n)=A'`,
some prime of `F'_{A',B'}` divides `a_n` and links it to `a_m` (hence to the
`B'`-side, since `ρ(m)=B'`). Since `F'_{A',B'}` is a single fixed finite set
independent of `n`, "the pool of primes used across all these links" is by
definition a subset of `F'_{A',B'}`, hence bounded (size `≤ |P(a_m)\S₀|`). No
`n > m` can ever fail to have such a linking prime (the Lemma's conclusion is
universal in `n`, not existential-in-the-limit), so there is no analog of an
"edge closing" that a repair step needs to fix: the bipartite network between
the `A'`-occurrences after `m` and the fixed witness `m` (hence the `B'`-side)
is complete from the start, with a pool of size `≤ |F'_{A',B'}|`. ∎

**This is not new.** It is a direct, one-line corollary of a lemma certified
in round 2 of this workspace and used continuously since (it is literally the
mechanism underlying `covering-system-construction`'s entire Reduced-Alphabet
program). Concretely, on the workspace's own standing hard test seed
`a_1 = 4807` (rogue pair `A' = {3,5,19}`, `B' = {2,11}`, core
`S₀ = {2,3,5,11,19,23}`, canonical witnesses `n_A=6, n_B=7` — data from
`covering-system-construction.md` §"Step 4" / round 26), the pool is exactly
`F' = P(a_7) \ S₀ = {13,17}`, size 2 — already known, already on record since
round 4 of this workspace, long before this round's approach existed.

### Proposition B (Reading α's bounded pool does not, by itself, give
Cofinite FAH — the exact dead wall already on record)

**Claim.** Boundedness of the Reading-α pool is strictly weaker than what is
needed: it forces (via finite pigeonhole, already spelled out in the Lemma's
own certified Corollary) that **some** prime of `F'_{A',B'}` links `a_n` to
the `B'`-side for **infinitely many** `n`, but does **not** force this for
**cofinitely many** `n` — other elements of the same bounded finite set can
also each recur infinitely often, splitting the index set among finitely many
classes with no further information about relative density.

**Proof / evidence.** The certified Corollary of the Generalized Bounded
Witness Lemma states this precisely: "there is a specific prime
`q ∉ S₀` such that `q | a_n` for infinitely many `n` with `ρ(n)=A'`" — the
word "infinitely many," not "cofinitely many" or "all but finitely many," is
the exact and complete strength of the pigeonhole step, and the Lemma's own
`Status` line records explicitly: *"Does NOT by itself close gap (†)."* This
is precisely the wall documented as dead across multiple rounds: the round-9
`cofinite-window-capacity-bound` / `density-argument-vacuity-corollary`
graveyard entries record that "some class is infinite" from an
infinite-pigeonhole argument never upgrades to "the wanted class is cofinite"
without a genuinely separate mechanism. On the concrete `a_1=4807` seed, this
is not hypothetical: `F' = {13,17}` is a bounded pool of size 2 (confirming
Reading α is "bounded" there), yet resolving which of the two classes is
cofinite for the residual divisor `d = 13` required an entirely separate,
seed-specific, ad hoc argument — the round-26 **Finite-Window Literalization
Lemma** (`lemmas/finite-window-literalization-lemma.md`), which works by
finding a *non-canonical* singleton witness and checking a finite window by
hand, not by any bound on the pool size. That closure is real and certified,
but it is explicitly single-seed (and its round-27 twin for `a_1=11305`'s
`d=103` likewise single-seed) — it does not follow from, or generalize via,
Reading-α pool-boundedness itself. So: Reading α's "yes, bounded" answer is
correct but supplies **zero additional leverage** beyond what the workspace
already has and has already found insufficient for a general theorem.

### Proposition C (Reading β is not a new question — it IS the open H2
termination question, already on record and already unresolved)

**Claim.** "Does the pool of primes recruited across repeated core-enlarging
repair events stay bounded" is, definitionally, the same question as H2's
core-growth termination criterion, already isolated and left open at round 15.

**Proof.** A repair event in Reading β, by construction, enlarges the core:
`S_{k} \rightsquigarrow S_{k+1} = S_k \cup \{q_k\}` (or a finite batch) for
some newly-recruited prime `q_k \notin S_k`, exactly the operator underlying
the certified **Self-Absorbing Core Theorem** / **Termination Criterion
Lemma** (`lemmas/termination-criterion-lemma.md`) chain
`S_0 \subseteq S_1 \subseteq \cdots`, `S_{k+1} = S_k^{+} := S_k \cup
\bigcup_{j=1}^{N(S_k)} P(a_j)`. "The pool of ever-recruited primes stays
bounded across the whole repair process" is literally the statement
`\bigcup_k (S_{k+1}\setminus S_k)` is finite, i.e. the chain `(S_k)_k`
stabilizes at some finite `S_\infty`, i.e. the absorption process
**terminates** — exactly the left-hand side of the Termination Criterion
Lemma's iff, already certified equivalent to boundedness of the threshold
sequence `(N(S_k))_k`, and already flagged (round 15, "sibling sub-question")
as a genuinely open, unresolved pigeonhole-threshold-boundedness question with
no currently-known mechanism. Nothing in the bipartite-network/aimo-1000
framing supplies a new tool for this: the network's own growth (Reading β) is
driven by the SAME `S_k \to S_k^+` operator this workspace has already
isolated and left open, under a different name, for 14 rounds (rounds 15
through 29). Renaming it "the linking-prime pool across network repairs" does
not change its content or supply new leverage. ∎

**Corroborating evidence that repair events genuinely CAN recruit
uncontrolled, discontinuous new primes (so Reading β is not vacuously
"obviously bounded" either).** The certified **Witness Discontinuity
Obstruction** (`lemmas/witness-discontinuity-obstruction.md`, round 7,
`a_1=175`) is an explicit, hand-verified example where enlarging the core by
one recruited prime `q=2` (`S_0=\{5,7\}\to S_1=\{2,5,7\}`) shifts a type's
earliest witness from index `m=3` (`a_3=182`, divisible by `q`) to an
unrelated index `m'=4` (`a_4=189`, odd, NOT divisible by `q`) — i.e. the very
prime that triggered a repair is not guaranteed to remain relevant to the
repaired network's new witness. This is precisely the failure mode Reading β
would need to rule out to prove boundedness, and it is not ruled out by
anything in the current certified stack; it is a genuine open obstruction, not
a technicality.

### Proposition D (the crux's actual load-bearing mechanism has no arithmetic
analog here — a structural mismatch, not just an unresolved analogy)

Retrieved the exact `aimo-1000` (IMO 2021 P6, "ferry islands") crux moves from
the corpus (`past_crux_moves_database.json`, `problem_id="aimo-1000"`,
`domain=combinatorics`, `subtopic∈{invariants-and-monovariants,
processes-and-algorithms, extremal-principle}`) to check the actual
repair/growth mechanism, not just its label. The load-bearing move is a
**deterministic toggle rule** specific to that problem's rewrite operation:

> "When network edge `A-B` closes... take any `C ∈ 𝒜\{A}`: `C` is joined to
> `B` by the network property. If `C` was not joined to `A`, `C` is now
> adjacent to exactly one of `{A,B}`, so the rule adds `C-A`; if `C` was
> already joined to `A`, it stays. **Either way `C` ends joined to both.**"

This works because aimo-1000's underlying process has a rewrite rule that
*fires on every vertex adjacent to exactly one endpoint of a just-toggled
edge, and is guaranteed by the problem's own hypothesis to fire* — the repair
is not merely "some new edge probably exists somewhere," it is "every
previously-adjacent vertex simultaneously and deterministically gains exactly
the missing edge, by the problem's own stated rewrite rule."

**No arithmetic analog of this toggle exists in the greedy-gcd recursion.**
The only tool this problem supplies for producing a new "edge" (a shared
prime factor) is the **existential** Free Facts guarantee
(`lemmas/free-facts-gcd.md`) plus the Generalized Bounded Witness Lemma's
refinement of it — never a simultaneous, deterministic repair triggered by
one index's factorization. Concretely, the analog of "closing edge A–B" in
this problem is "enlarging the core by a newly recruited prime `q`," and the
Witness Discontinuity Obstruction shows this is the *opposite* of a toggle:
the very index/prime that triggered the enlargement is **not** guaranteed to
remain a witness or a divisor of the new witness — there is no rule forcing
every "vertex" (occurrence-index) that was linked via the old prime to become
linked via a new one; some are simply orphaned (as the round-7 example shows
literally, `a_4=189` inherits the type but not the recruited prime). The
crux's entire repair argument (all five listed moves) is a chain of
deterministic consequences of the toggle; without an analog of the toggle,
none of moves 2–5 (re-splitting, absorption-by-toggle, growth-to-cover-all,
final symmetric pigeonhole) transplant, because each explicitly invokes "the
toggle rule fires on `C`" as its justification step. This is a structural
mismatch (the mechanism this problem's rule actually supplies is strictly
weaker than what the crux's argument needs at every repair step), not merely
an unresolved case of an otherwise-matching template.

### Conclusion

Both readings of the outline-reviewer's corrected Step-1 question have now
been answered rigorously:

- Reading α: **yes, bounded** — but this is a one-line corollary of a lemma
  certified in round 2, already known to be insufficient for Cofinite FAH
  (Proposition B), and already the load-bearing mechanism of the
  22-round-plateaued `covering-system-construction` approach. No new content.
- Reading β: **not answerable by anything in the current stack** — it is,
  definitionally, the already-open H2 core-growth-termination question
  (Proposition C), for which the round-7 Witness Discontinuity Obstruction is
  a genuine, unconditional obstruction to any "obviously bounded" shortcut.
- The transplanted mechanism itself (Proposition D) does not survive contact
  with the actual problem: the crux's repair step is a deterministic toggle
  guaranteed by the ferry problem's own rewrite rule, and this problem
  supplies only an existential (never simultaneous, never deterministic)
  linking guarantee, so even a positive answer to Reading β would not
  reconstruct the crux's growth-to-cover-all-vertices argument (Steps 3–4 of
  the outline) without new machinery this round did not find.

**This approach is RETHOUGHT (not iterated further).** Per the round-5
`reversible-transition-map` precedent (a fast, honest RETHINK on a failed
disambiguation is preferred to belaboring a dead check), and per the
outline's own "Watch out for" instruction ("If step 1 disambiguation fails
outright, this approach should be reported RETHINK fast... do not iterate on
a dead disambiguation for multiple rounds"), Status is set to `unsolved`
here. This is the workspace's **32nd confirmed-dead FAH mechanism variant**
(joining `orbit-merging-additive-offset-dichotomy`,
`reversible-transition-map`, `witness-index-descent`,
`triangle-consistency-pigeonhole`'s sieve obstruction, and the 28+ others on
record in `current.md`), and it adds genuine value: it forecloses the entire
"structural graph/network-invariant transplant" family of approaches to
H1/FAH for this problem, not just this one instantiation, since Proposition D
identifies the mismatch (existential-only linking guarantee vs.
deterministic-toggle requirement) as a structural feature of the greedy-gcd
recursion itself, not an accident of this particular transplant attempt.

## Promotable lemmas

**Bipartite-Network Reduction Collapse (new, this round; recommend
certification).** *Statement:* For the greedy-gcd sequence's FAH problem, any
"growing bipartite index-set network with local repair on failure" mechanism
(in the sense of tracking evolving finite sets `𝒜_k, ℬ_k` of occurrence
indices with a complete-bipartite shared-prime-edge invariant, repaired by
enlarging the reference core `S₀` on edge failure) reduces, under its two
only possible formalizations, either (a) at fixed core, to the already
certified Generalized Bounded Witness Lemma's bounded-but-not-singleton
linking pool `F'_{A',B'}`, which is already known insufficient for Cofinite
FAH (finite-pigeonhole gives "some class infinite," not "cofinite"), or (b)
under core growth, to the already-open H2 core-growth-termination criterion
(`lemmas/termination-criterion-lemma.md`), for which the certified Witness
Discontinuity Obstruction is a genuine obstruction to easy resolution.
*Proof:* Propositions A–C above, in full. *Scope:* rules out this entire
mechanism family (not just one instantiation) as a route to closing H1/FAH,
until and unless H2's termination question is separately resolved — at which
point Reading β becomes moot anyway (H2 alone plus the existing Master
Conditional Theorem would already suffice, without needing the network
framing at all). This is a genuine, reusable, precisely-scoped negative
result parallel in kind to `lemmas/same-type-free-facts-vacuity.md` and
`lemmas/density-argument-vacuity-corollary.md`, and should stop any future
round from re-proposing a graph/network-invariant transplant for H1/FAH
without first resolving H2.
