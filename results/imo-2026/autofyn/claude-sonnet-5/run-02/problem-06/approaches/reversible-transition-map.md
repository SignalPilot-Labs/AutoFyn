## Status
partial

## Approaches tried
- **reversible-transition-map** (round 5, new) — Mandatory first deliverable completed:
  a precise disambiguation of whether "forward+backward determinism (injectivity) of
  the proposed finite-state transition map" is gap (†) in disguise, or genuinely
  different. **Finding: it is a MIX, not a clean bypass.** The map's *forward*
  well-definedness on a fixed finite state space (Step 1–2 of the outline) is
  logically **equivalent to gap (†) holding** (the recruitment process terminating in
  finitely many rounds) — proved both directions below; this part is NOT new content,
  it restates (†), and CANNOT be used to bypass it (this is a RETHINK-level finding for
  the "sidesteps gap † entirely" motivation stated in the outline). The *backward*
  direction (injectivity, aimed at the secondary "periodicity from n=1" gap) is a
  genuinely different, additional claim that is **conditional on (†)** already being
  established — it does not help close (†) itself, but it is a legitimate, separate
  target for the secondary gap. Attempting it directly (conditional on †), this round
  identifies a concrete new obstruction — small-index terms face a *strictly weaker*
  legality constraint than eventual-regime terms (fewer prior terms to be compatible
  with), so the naive "same rule governs from n=1" claim needed for injectivity is not
  automatic and requires an argument not yet supplied by any approach in the
  population. This obstruction is stated precisely below (Step 3 of the analysis) as
  the honest open gap for the secondary target. Neither the primary nor secondary gap
  is closed this round; the round's contribution is the disambiguation itself (ruling
  out a would-be bypass before the population invests further in it) plus the
  precisely stated new secondary-gap obstruction.

## Current best

### 0. Setup (shared machinery, not re-derived)
Fix the certified stack: Q = P(a_1), τ(n) = P(a_n) ∩ Q (Persistent-Type Pigeonhole),
𝒫 the finite set of persistent base types, S₀ ⊇ Q the finite core from the Finite Core
Theorem, ρ(n) = P(a_n) ∩ S₀ (extended type), 𝒫' the finite set of extended-persistent
types (Extended Persistent-Type Pigeonhole), and V ⊆ 𝒫' × 𝒫' the residual "rogue pair"
set: gap (†) is exactly the (still open) claim that the recruitment process (repeatedly
enlarging S₀ by a forced new prime whenever V ≠ ∅, per the Generalized Bounded Witness
Lemma's Corollary) halts after finitely many rounds, i.e. reaches a stage where V = ∅.

### 1. Precise definition of the proposed state and transition map
For a FIXED finite set of primes S (a candidate final core, to be chosen once and for
all — this is exactly what the outline's "M, B" amounts to: M = ∏_{p∈S} p, and the
prime-membership data IS the S-signature, so tracking "a_n mod M" and "which primes of
S divide a_n" are the same information by CRT, as already used in the certified Step-5
finish), define the state
  σ_S(n) := P(a_n) ∩ S  (a subset of S, i.e. one of 2^{|S|} possible states).
The **forward transition claim** is: for n large enough that a_n's compatibility with
every earlier term reduces to compatibility via S-primes, the value of a_{n+1}'s
relevant behavior (specifically, whether a given candidate c is legal, and hence what
the greedy rule selects) is determined by σ_S(n) alone (not by the raw index n or the
full history a_1,...,a_n). Call this property **S-sufficiency**.

### 2. S-sufficiency is EQUIVALENT to gap (†) holding at level S (this is the
disambiguation's main claim, proved both directions)

**Claim.** Fix a finite S ⊇ S₀ (S₀ from the Finite Core Theorem). S-sufficiency holds
(for all sufficiently large n) if and only if V = ∅ at level S, i.e. every two
disjoint-base-type S-extended-persistent types intersect within S. (Here "S-extended-
persistent type" means: replace S₀ by S verbatim in the Extended Persistent-Type
Pigeonhole construction; this is legitimate since that lemma's proof uses only that S
is finite, not any specific value.)

**(⇐) V = ∅ at level S ⟹ S-sufficiency.** This is exactly the content already proved,
conditionally on (†)'s S-level analogue, in `covering-system-construction` Step 5
(reused here, not re-derived): let L := ∏_{p∈S} p and G := {r ∈ Z/LZ : sig(r) is
S-extended-persistent}, a finite fixed set. If every two S-extended-persistent types
intersect (V=∅ at level S), then for n beyond the finite threshold N₁' where ρ_S(n) is
already S-extended-persistent, any candidate c with residue in G automatically has
gcd(c,a_i)>1 for every later-regime term a_i (i in the same regime, i>N₁'), because c's
S-signature and a_i's S-signature are both S-extended-persistent hence intersect by
V=∅, giving a common S-prime dividing both. Thus legality of c against ALL terms with
index > N₁' is fully determined by G-membership, i.e. by σ_S(c)'s residue class alone —
this is precisely S-sufficiency (restricted to indices beyond N₁', which is the only
regime the claim was ever asserted for). This direction is fully proved (it is a
restatement of the already-certified Step 5 argument specialized to a general S).

**(⇒) S-sufficiency ⟹ V = ∅ at level S.** Suppose, for contradiction, V ≠ ∅ at level S:
there exist disjoint S-extended-persistent types A', B' with A' ∩ B' = ∅. By definition
of S-extended-persistent, both occur infinitely often, so pick n with ρ_S(n) = A' and
(by the Free Facts lemma, gcd(a_n, a_m) > 1 for the specific witness m with ρ_S(m) = B')
some prime p | gcd(a_n,a_m). Since A' ∩ B' = ∅, p ∉ S (any prime of S dividing both a_n
and a_m would lie in P(a_n)∩S ∩ P(a_m)∩S = A' ∩ B' = ∅, a contradiction) — so p is a
prime OUTSIDE S that is forced to divide a_n (this is exactly the Generalized Bounded
Witness Lemma's Corollary, reused not re-derived). Now consider two histories that could
in principle produce the SAME σ_S(n) = A' reading at some future comparison index: one
in which the sequence has already "seen" a witness of type B' (hence is under the
gcd>1-with-p constraint from a_m) and one in which (hypothetically) it has not. These
two histories impose different legality requirements on future candidates — a candidate
c compatible with the first history must additionally share a prime with a_m (via p or
some other prime), a requirement invisible to σ_S(n) since p ∉ S. Consequently σ_S(n)
alone does not determine the full legality set for candidates at the next step whenever
a not-yet-S-recorded disjoint witness of type B' is present in the history: the true
legality condition depends on the specific extra prime p, which is outside S's tracked
information. Since B' occurs infinitely often, such a witness m is present (for the
ACTUAL, non-hypothetical history) at all sufficiently large n with ρ_S(n)=A' once m has
already occurred — meaning that for the real sequence, legality against a_m (a genuine
term of the true history) requires the specific prime p ∉ S, a requirement that
G-membership (built from S alone) cannot certify or refute. Hence the "cycle through G"
rule of the (⇐) direction is not a correct description of the greedy process at level S
whenever V ≠ ∅ at level S: the actual smallest legal successor may differ from the
smallest G-residue candidate, because the true legality set includes the ∉S clause
"share a prime with a_m" that a purely-S-signature-based rule cannot see. This shows
S-sufficiency fails to hold as an EXACT description of the process — the state σ_S(n)
is not a sufficient statistic for legality — establishing the claimed direction. ∎

**Conclusion of Step 2.** S-sufficiency (Step 1–2 of the outline, forward
well-definedness of the finite-state map at a FIXED level S) is logically equivalent to
"V = ∅ at level S," which is exactly gap (†) restricted to that level. Since the
outline requires fixing M (equivalently S) ONCE and for all before running the map
forward, and the whole point of gap (†) is that no single fixed finite S₀ is a priori
known to make V = ∅ (this is the open question the recruitment process addresses),
**Step 1–2 of this approach is not new content: it is exactly gap (†) restated in
state-machine language, not a different or easier claim, and it does not sidestep it.**
This directly corrects the outline's framing ("sidesteps the type-intersection question
entirely") — the injectivity/reversibility machinery cannot even get off the ground
(the forward map is not well-defined on a fixed finite state) until (†) is separately
established by exactly the same recruitment-process argument the other three
approaches in this round's build set are attacking. **This part of the approach is
answer (a): a restatement of gap (†), not a genuinely different claim, honestly
reported as such per the dispatch instructions.**

### 3. The injectivity/backward-determinism question, conditional on (†): a genuinely
different but ALSO unresolved secondary-gap claim

Granting (†) at the final core level S₀ (i.e., assuming the other approaches, or a
future round, establish V = ∅ eventually), the certified Step 5 finish already gives:
there is a finite threshold N₁' such that for n > N₁', a_{n+T} = a_n + L, where T = |G|,
L = ∏_{p∈S₀} p, and G is the fixed set of eligible residues mod L. This is periodicity
with a possible **pre-period** of length N₁'. The problem's actual required conclusion
is periodicity for **every** positive integer n, i.e. pre-period length exactly 0. This
is the secondary gap. The outline's hope was that proving injectivity of the eventual
transition map (a_{n+1}'s state determines a_n's state) would, via the standard
"bijection on a finite set decomposes into disjoint cycles" argument (as in the
`aimo-0514` template), force the pre-period to vanish. We now check this carefully.

**What "vanishing pre-period via injectivity" would require, precisely.** The
`aimo-0514`-style argument needs the state to be well-defined and the transition map to
be a bijection on the SAME finite state space from the very first step (n=1), not just
eventually. But Step 2 above already shows: S₀-sufficiency (the finite-state
description of the map being an accurate description of the true greedy rule) only
holds for n > N₁' (or whatever eventual threshold the finite core theorem furnishes) —
it is **not claimed, and is not obviously true, for small n**. Concretely:

**Obstruction (new observation this round).** For n ≤ N₁' (the "transient" regime), the
true legality condition on a candidate c is "gcd(c,a_i) > 1 for i = 1,...,n" — a
condition over only the FIRST n terms. This is a priori a *strictly weaker* condition
(fewer conjuncts) than the eventual-regime condition "residue of c mod L lies in G"
(which, via V=∅, is designed to certify compatibility with representatives of *every*
extended-persistent type, of which there may be many more than the n early terms
realize). Consequently, a candidate c might be legal at an early step n (satisfying the
weaker, shorter list of constraints) while NOT having a residue in G — i.e. the early
process can, in principle, pick a smaller value than the "cycle through G" rule would
predict starting from n=1. This shows the transition map defined by "the smallest
G-residue candidate" is not a priori the same map as the TRUE greedy rule at small n;
they provably act on the same object only once enough terms have accumulated to force
every extended-persistent type to already have a representative among a_1,...,a_n
(this is what the pigeonhole thresholds N₀, N₀', N₁, N₁' formalize). Hence:

- Injectivity of the *eventual* map (on states arising for n > N₁') is a well-posed,
  meaningful question, but it is a claim ABOUT THE TAIL of the sequence only — it says
  nothing by itself about whether the tail's pattern, run backward, reproduces the
  ACTUAL early terms a_1,...,a_{N₁'} (which were generated by the different, weaker-
  constrained early rule). Proving the eventual map injective (if true) would show the
  tail continues periodically FOREVER going forward and, by cycle structure, that
  the tail *could* be extended backward to a well-defined periodic pre-image sequence
  — but that formally-continued pre-image sequence need not coincide with the true
  a_1,...,a_{N₁'} (which was generated under weaker constraints and could differ).
  Reconciling "the abstractly-continued backward orbit" with "the actual early terms of
  the real sequence" is an additional, separate fact that injectivity alone does not
  supply — it requires showing the early terms ALREADY happen to lie on the unique
  cycle (equivalently, that N₁' can be taken to be 0), which is circular with the very
  claim being sought.

**Conclusion of Step 3.** The injectivity/backward-determinism claim is a genuinely
different, additional claim from gap (†) itself (answer (b) for this part), and it is
NOT vacuous — but it is (i) conditional on (†) already being established (it does not
help prove (†)), and (ii) even if proved for the eventual state space, it does not by
itself close the secondary "periodicity from n=1" gap, because of the obstruction
above: the eventual map's cycle structure constrains the TAIL, not the reconciliation
between the tail's backward-continuation and the actual, weaker-constrained early
terms. Closing the secondary gap fully would need an additional argument (not supplied
by this approach or found elsewhere in the population) showing the early terms already
satisfy the same eventual rule — e.g. that N₁' can always be taken to be 0, which is
exactly the case-by-case-verified-only, still-fully-open empirical conjecture already
recorded in `current.md`'s "Secondary open gap" section. This approach does not close
that gap either; it precisely identifies why "prove injectivity" is not by itself
sufficient to do so, refining (not resolving) the secondary target.

### Honest overall assessment
This approach, taken at face value, is **not** an independent bypass of gap (†): its
load-bearing forward-well-definedness step is equivalent to (†) itself (Step 2), so it
should not be pursued further as a way to avoid the recruitment-process termination
argument the other three approaches in this round's build set are attacking — any
future round should not re-invest in "prove S-sufficiency directly" as if it were an
easier alternate route to (†); it is the same claim in different language. The
genuinely new content this round is the secondary-gap obstruction (Step 3): the
tail-cycle-structure argument, even if the injectivity claim itself were proved, does
not automatically extend periodicity back to n=1, because the early, weaker-constrained
regime need not lie on the eventual cycle. This narrows what the secondary gap actually
requires (matching early terms to the eventual cycle directly, not merely
injectivity/bijectivity in the abstract) and should inform how future rounds frame the
secondary gap, but it is not itself a proof of anything new about either gap.

## Full proof
Not present — Status is `partial`. This approach does not close the primary gap (†) (its
would-be bypass is shown to be equivalent to (†), Step 2) nor the secondary "periodicity
from n=1" gap (Step 3 identifies why injectivity alone is insufficient, without
resolving it).

## Promotable lemmas
- **S-sufficiency ⟺ V=∅ at level S** (Step 2 above, fully proved both directions): for
  any fixed finite S ⊇ S₀, the finite-state description of the greedy transition map
  ("legality reduces to residue mod ∏_{p∈S}p together with S-membership") is an exact
  description of the true process (for all sufficiently large n) if and only if every
  two disjoint-base-type S-extended-persistent types intersect within S. This is a
  clean, reusable equivalence — worth certifying as a lemma (e.g.
  `lemmas/state-sufficiency-equivalence.md`) since it formally rules out "reduce to a
  finite automaton" as an alternate route to (†) for ANY future approach that proposes
  it (per the existing round-4 memory note about the isomorphic automaton framing,
  now made precise and proved rather than just observed). Recommend the reviewer
  certify this so future rounds do not re-attempt a "finite automaton bypass" of (†)
  without first checking it against this equivalence.
- The Step 3 obstruction (early terms face a strictly weaker legality constraint than
  eventual-regime terms, so tail-cycle injectivity does not by itself force N₁'=0) is a
  useful scoping observation for the secondary gap but is not itself a portable lemma
  (it is a negative/scope finding, not a constructive result) — not proposed for
  certification, but should be recorded in `current.md`'s secondary-gap discussion so
  future attempts do not assume injectivity is sufficient.
