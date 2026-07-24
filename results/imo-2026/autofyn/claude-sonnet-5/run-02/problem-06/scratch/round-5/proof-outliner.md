## imo-2026-06

**Governing correction this round.** Round 4's "V=∅ always / zero further recruitment
rounds ever needed" target is FALSE: math-explorer-singleton-hypothesis found 4 fresh,
transparently-computed, correct-minimal-witness counterexamples (a_1 = 187, 209, 247,
385), each needing exactly one recruitment round, each resolved by a Singleton F'
(|F'|=1). Do NOT direct any builder to "prove V=∅ always" in any form. The correct
target reverts to the original recruitment-PROCESS framing (start from S₀, find a
rogue pair, recruit a forced prime via the certified Generalized Bounded Witness
Lemma's Corollary / Lemma G, repeat) — prove this process terminates in finitely many
rounds. Two load-bearing open sub-claims, both still genuinely open:
(a) the Singleton Hypothesis (|F'|=1) holds in general, not just case-by-case;
(b) either a bound on total rounds, or the stronger "one recruited prime resolves ALL
currently-rogue pairs simultaneously" (seen in every tested instance so far: a_1=209's
7 resolves all 6 rogue pairs, a_1=247's 3 resolves all 14).

All four approaches below build on the fully certified, unconditional lemma stack in
`results/imo-2026-06/lemmas/` (Free Facts, Bounded Gap Lemma, Generalized Bounded Gap
Lemma, Persistent-Type Pigeonhole, Bounded Witness Lemma, Single-Witness-Prime
Pigeonhole, Finite Core Theorem, Generalized Bounded Witness Lemma + Recruitment
Corollary, Extended Persistent-Type Pigeonhole, Canonical-Refinement Lemma, F_A∩F_B≠∅,
Lemma G / Extended Earliest-Witness Intersection) and do not re-derive them.

---

### covering-system-construction: revise
Target: the whole problem — there exist T, L with a_{n+T} = a_n + L for all n
(eventual periodicity of the gap sequence), literally from n=1 if achievable.
Technique: recruitment-process induction (finite pigeonhole + Bounded Gap Lemma
CRT/cyclic-pigeonhole finish), now correctly re-scoped to the reopened process-
termination target instead of round 4's falsified "zero rounds" shortcut.

Skeleton:
  1. Build S₀ from the Finite Core Theorem's literal minimal (earliest-occurrence)
     witnesses; compute 𝒫' and V (rogue pairs, both sides non-canonical) — already
     certified machinery, restate but do not re-derive.
  2. If V = ∅, done (this covers e.g. a_1=1001, 2431, and the 18 seeds from round 4 —
     but is NOT assumed in general per this round's correction).
  3. If V ≠ ∅, pick a rogue pair, apply the certified Recruitment Corollary
     (`generalized-bounded-witness-lemma.md`) to force a new prime q ∉ S₀, set
     S₁ := S₀ ∪ {q}, recompute 𝒫'₁, V₁ at the new level. Repeat.
  4. **New Step (this round's target): prove the process halts.** Attempt the
     "simultaneous resolution" upgrade: show that a single round's recruited prime q
     resolves EVERY pair currently in V, not just the witnessed pair — i.e. after one
     round, V_{k+1} = ∅ whenever V_k ≠ ∅, so the process needs at most ONE round ever
     (matching all 5 known nonzero-round instances: 187, 209, 247, 385, and
     retroactively 175 with 0 rounds). Mechanism to attempt: q ∈ F' = P(a_{n_B}) \ S₀
     is forced to recur infinitely often in the WITNESSED side by the Recruitment
     Corollary's pigeonhole (already certified); the new claim needed is that q ALSO
     recurs (or already recurs) as a member of every OTHER currently-rogue extended
     type's persistent set, via a shared-witness argument: if the same index n_B (or a
     bounded finite set of indices) supplies the recruited prime for every current
     rogue pair simultaneously — because n_B is by construction the earliest
     occurrence of a persistent type formed from a SMALL prime subset, its own factor
     set F' is small and shared structurally across pairs whose canonical witnesses
     are "close" to n_B — then one recruitment round suffices. This is NOT yet proved;
     it is the key new lemma to attempt.
  5. Fallback if Step 4's one-round claim fails: bound total rounds by |𝒫'| (finite,
     ≤ 2^{|S₀|}−1 at each stage) via a monovariant that strictly decreases with each
     round even though |S₀| strictly increases — e.g. track the number of rogue pairs
     |V_k| and attempt to show it strictly decreases (not just that the witnessed pair
     is removed) using the Recruitment Corollary's pigeonhole applied to ALL rogue
     pairs at once rather than one at a time.
  6. Given process termination (Step 4 or 5), CRT + cyclic-pigeonhole finish
     (unchanged from round 1): L := ∏_{p∈S₀^final} p, G := eligible residues mod L,
     T := |G|.
  7. Secondary gap: extend periodicity to n=1 literally (still completely open, all
     approaches; see fresh-framing report's Part 2 — not attempted here, left as an
     explicit open item this approach does not claim to close).

Key lemmas (mechanism):
  - Recruitment Corollary already certified — because gcd(a_n,a_m)>1 (Free Facts) and
    any common prime in S₀ would violate the pair's disjointness, forcing a new prime.
  - NEW (unproved) Simultaneous Resolution Lemma: the recruited prime q from one rogue
    pair's earliest witness resolves every other currently-rogue pair too — because
    (conjectured mechanism) the earliest-occurrence witnesses of small-support
    persistent types cluster at small indices (empirically m_B = 1–4 in all tested
    seeds) making their extra-prime sets F' overlap.
Open gaps: Step 4 (Simultaneous Resolution Lemma) is the crux, entirely open — has
strong but small-sample empirical support (2/2 multi-pair instances: a_1=209, 247,
where all rogue pairs share ONE recruited prime). Step 5 fallback also open. Step 7
(n=1 literal) untouched.
Cases to cover: V=∅ at S₀ (trivial, done); V≠∅ needing exactly one round (main new
target); the theoretical possibility of 2+ rounds (no example seen yet — flag as an
open case, do not assume it cannot happen).
Watch out for: reusing any pre-round-4 "V=∅ always" numeric claim (falsified, do not
cite); recompute every example from scratch with the literal minimal-witness
convention per the certified caution note on Lemma G.

---

### greedy-exchange-cost-potential: revise
Target: same whole problem, via the Round Resolution Lemma / Singleton Hypothesis
machinery already partially built (certified Lemma G; conditional Round Resolution
Lemma proved assuming |F'|=1).
Technique: pigeonhole + magnitude-bound argument to promote the Singleton Hypothesis
from case-checked to a general theorem, using the certified Generalized Bounded Gap
Lemma to control the SIZE (hence prime-factor count) of the witness term a_{n_B}.

Skeleton:
  1. Restate Lemma G and the Round Resolution Lemma exactly as certified/proved in
     rounds 3–4 (no re-derivation).
  2. Correct the empirical citation: drop a_1=175 as "Singleton support" (it needs 0
     rounds under the corrected S₀, so is not a Singleton-Hypothesis test case at all)
     and replace with the 4 freshly, correctly re-verified instances from this round's
     explorer report (a_1 = 187, 209, 247, 385 — all confirmed |F'|=1 with full witness
     data reported transparently).
  3. **New attempt at proving the Singleton Hypothesis in general.** For a rogue pair
     with n_A < n_B (WLOG), F' := P(a_{n_B}) \ S₀. Use the Generalized Bounded Gap
     Lemma to bound a_{n_B} in terms of a_{n_A} and the modulus formed by S₀'s primes:
     a_{n_B} ≤ a_{n_A} + a_1 · (∏ small S₀ primes) — NOT immediately enough to bound
     |F'| by itself (a bound on a_{n_B}'s SIZE bounds the number of DISTINCT prime
     factors only logarithmically, not to exactly 1). The real content needed: use
     MINIMALITY of n_B as the earliest occurrence of its extended type — any prime
     factor of a_{n_B} outside S₀ that recurred at an earlier index would already have
     been absorbed into S₀ or into an earlier-occurring type, by the greedy rule's
     "smallest legal candidate" property. Attempt to show any q, q' ∈ F' with q ≠ q'
     forces a strictly smaller legal candidate than a_{n_B} itself (contradicting
     minimality of a_{n_B} as an earliest occurrence) — i.e. adapt the greedy-
     minimality "smallest candidate" argument from a per-term exchange to a per-
     witness exchange, a genuinely new use of minimality not previously tried in this
     approach (rounds 2–3's exchange attempts used minimality of the SEQUENCE's actual
     term choice at index n_B itself for magnitude bounds only; this uses minimality
     of n_B as an INDEX, i.e. that no earlier index has the same extended type).
  4. If Step 3 succeeds unconditionally, the Round Resolution Lemma becomes
     unconditional, resolving one rogue pair per round with a single specific prime;
     combine with covering-system-construction's process-termination argument (Step 4
     or 5 there) for the full finish — cross-reference, do not duplicate.
  5. If Step 3 only partially succeeds (e.g. bounds |F'| ≤ k for explicit small k
     rather than exactly 1), record the partial result honestly and hand off to
     covering-system-construction's fallback framing, since a bounded-but-not-1 F' set
     still supports a (weaker, multi-branch) pigeonhole recruitment argument.

Key lemmas (mechanism):
  - Singleton Hypothesis attempt: because n_B is the EARLIEST occurrence of its
    extended type, any candidate integer with strictly fewer non-S₀ prime factors than
    a_{n_B} that is still legal (satisfies gcd>1 with all prior terms) would have been
    chosen by the greedy rule instead, UNLESS no such smaller legal integer exists —
    the gap in the argument is showing such a smaller integer's legality, which is not
    yet established; this is the honest, precise open step, not hand-waved.
Open gaps: Step 3 (Singleton Hypothesis, general proof) is entirely open — this is the
approach's crux target this round. Step 5 fallback (bounded, not singleton) untested.
Cases to cover: n_A < n_B and n_B < n_A are symmetric by relabeling — Lemma G already
handles this symmetrically, no separate casework needed.
Watch out for: do not reintroduce the retracted a_1=175 "Singleton" citation; do not
conflate "F' is the recruited-prime candidate set for the witnessed pair" with "F'
resolves the whole base type" (already separately falsified, round 4).

---

### witness-index-descent: new
Target: same whole problem — prove the recruitment process (equivalently V=∅ after
finitely many rounds, hence T, L exist) via a minimal-counterexample / well-ordering
descent on the pair of witness indices (n_A, n_B) of a rogue pair, instead of forward
induction on rounds.
Technique: extremal principle / minimal-counterexample descent, adapted from crux
`aimo-0030`'s Claim 5 (which upgrades "any two good numbers share a common prime" to
"...share a common SMALL prime" via a stripping-construction descent on a minimal
witness). Our adaptation cannot use aimo-0030's free "stripping construction" (a_n is
not freely constructible, it is whatever the greedy process outputs) — the engineering
gap flagged by the extremal-witness explorer — so this approach must find an intrinsic
substitute using the greedy sequence's own structure (earlier occurrences of related
types) rather than a manufactured integer.

Skeleton:
  1. Define the well-ordering: among ALL rogue pairs (A', B') ever occurring at any
     recruitment stage (not fixing S₀ in advance — quantify over the whole eventual
     process), order by min(n_A, n_B) where n_A, n_B are the EXTENDED type's earliest
     occurrences (as in Lemma G), and suppose for contradiction a rogue pair exists;
     take one with min(n_A,n_B) minimal. WLOG n_A < n_B (relabel).
  2. **New sub-lemma to attempt first (from the extremal-witness explorer, unproven):**
     min(n_A,n_B) ≥ max(m_A,m_B), where m_A, m_B are the CANONICAL (base-type) earliest
     witnesses. Mechanism: canonical witnesses are always very early (empirically
     m_B = 1–4 in every tested seed) because they are literally the first occurrence of
     their base Q-type, which by the Bounded Gap Lemma must appear within a bounded
     window of n=1; a non-canonical (rogue) extended-type witness requires an EXTRA
     prime factor beyond the canonical refinement, which (by minimality of the greedy
     rule) can only first appear after the canonical type has already stabilized S at
     that base type, i.e. after m_A, m_B. Attempt to prove this rigorously via the
     Canonical-Refinement Lemma: since A' ≠ A_can, A' is a strict variant of the
     canonical refinement, and any occurrence of A' before m_B would make B (not yet
     witnessed) irrelevant to A's factor content, so the Bounded Witness Lemma applied
     to the CANONICAL side already fixes a_{m_A}, a_{m_B}'s prime content before any
     rogue divergence can occur.
  3. Given Step 2, at the minimal rogue pair, both a_{m_A}, a_{m_B} (canonical
     witnesses) are already fixed and, by the Canonical-Refinement Lemma, ALREADY
     intersect (a_{m_A}, a_{m_B} share a canonical-level prime, since m_A, m_B are
     canonical). Use this shared canonical prime as an anchor: any legal candidate for
     a_{n_A} (n_A minimal among rogue witnesses) must be compatible with a_{m_B}
     (already placed, index < n_A by Step 2) — apply Free Facts to force
     gcd(a_{n_A}, a_{m_B}) > 1 via a prime already forced to lie in the canonical
     core (not a genuinely new prime), contradicting that A' is a NON-canonical
     refinement disjoint from B' (since the shared prime with a_{m_B} would then need
     to be a member of A' by definition of extended type, forcing A' ∩ B'_can ≠ ∅,
     which combined with an attempt to show B'_can ⊆ B' or a compatible refinement
     argument aims for the contradiction). This final step (turning "shares a prime
     with a_{m_B}" into "contradicts rogueness of the minimal pair") is NOT fully
     worked out — it is the genuine open engineering gap the aimo-0030 stripping
     construction doesn't directly hand us; state it honestly as the descent's missing
     step for the builder to attempt, with the above as the concrete direction.
  4. If the descent succeeds, V = ∅ is proved not "always" (avoiding round 4's false
     claim) but rather "eventually, after finitely many forced recruitment rounds,
     with the descent itself supplying the termination argument" — i.e. this approach
     directly targets process termination, not the (falsified) zero-round claim.
  5. CRT + cyclic-pigeonhole finish, as in covering-system-construction Step 6.

Key lemmas (mechanism):
  - Ordering sub-lemma (Step 2): canonical witnesses are forced early relative to rogue
    witnesses — because rogue-ness requires deviation from the canonical refinement,
    which structurally cannot occur before the canonical type itself is witnessed.
  - Descent contradiction (Step 3): NOT fully derived; flagged honestly as the open
    engineering gap, with a concrete partial argument and the specific missing link
    named (turning a shared-prime fact into a contradiction of A'/B' disjointness).
Open gaps: Step 2 (ordering sub-lemma) — plausible, empirically checked in 2 seeds by
the explorer, not proved. Step 3 (descent contradiction) — the crux, genuinely
unfinished; explorer explicitly could not complete it. This is a higher-risk, higher-
diversity approach (different proof STYLE — well-ordering/descent vs. forward
induction — from both approaches above) and should be judged on whether the builder
makes real progress on Steps 2–3, not expected to close in one round.
Cases to cover: the WLOG n_A<n_B relabeling; the case min(n_A,n_B) could equal some
m_B exactly (boundary case, needs explicit handling, not just "generically greater").
Watch out for: do NOT reuse round 3's failed |A'|+|B'| size-measure descent (documented
dead end — a genuinely different measure, witness-index, is used here); do not assume
the ordering sub-lemma (Step 2) without proof even though empirically clean in 2/2
tested seeds — small sample.

---

### reversible-transition-map: new
Target: same whole problem — a genuinely different top-level route that sidesteps the
type-intersection question (gap †) entirely, potentially closing BOTH the primary gap
and the secondary "periodicity from n=1 literally" gap at once.
Technique: reversibility/bijectivity of a finite-state transition map, adapted from
crux `aimo-0514` (its crux move: encode a deterministic process as a bijection on a
finite state space — forward AND backward determined — so every orbit decomposes into
disjoint cycles, forcing PURE periodicity with no transient, with no separate
"which classes intersect" argument needed).

Skeleton:
  1. Fix M := L_candidate, a sufficiently large modulus divisible by every prime that
     will ever recur infinitely often (this itself needs the Bounded Gap Lemma /
     eventual-regime machinery to pin down — state as an explicit hypothesis to
     discharge, not assumed for free). Define the state of index n as
     σ(n) := (a_n mod M, {p ≤ B : p | a_n}) for a fixed bound B ⊇ all of S₀'s primes.
     The state space is finite (M · 2^{|S₀|} possibilities).
  2. Show the forward map σ(n) ↦ σ(n+1) is well-defined and deterministic once n is
     large enough that legality reduces to a residue/prime-membership condition (this
     needs the SAME eventual-regime facts as the existing approaches — Persistent-Type
     Pigeonhole, Finite Core Theorem — reused, not re-derived).
  3. **New target, the crux of this approach:** prove the forward map is INJECTIVE on
     its eventual image, i.e. σ(n) is recoverable from σ(n+1) alone. Attempt mechanism:
     the greedy rule picks a_{n+1} as the SMALLEST legal integer > a_n; if two distinct
     states σ, σ' both mapped to the same successor state τ, then (working backward)
     there would be two distinct smallest-legal-candidate computations landing on
     values congruent mod M with the same small-prime membership but arising from
     different predecessor legality constraints (different a_1,...,a_{n} histories) —
     attempt to derive a contradiction from the fact that "smallest legal candidate
     greater than X" is a strictly increasing, hence injective, function of X within
     any fixed legality class. This is NOT yet proved — the open step is showing that
     the map "smallest legal successor" is injective as a function of the FULL state
     (not just of a_n's raw value, since two different a_n with the same state could in
     principle have different legality histories through a_1,...,a_{n-1} which the
     state σ(n) may not fully capture) — i.e. whether σ(n) as defined actually
     determines legality relative to ALL prior terms (this is essentially a restatement
     of gap † in disguise if σ doesn't capture enough information, or a genuinely new,
     smaller obligation if it does; the builder must check which).
  4. If Step 3 succeeds: bijection on finite state space ⟹ union of cycles ⟹ every
     orbit purely periodic ⟹ since σ(1) is a fixed, well-defined state (state space
     finiteness applies from n=1 immediately, no "eventually" needed once M, B are
     fixed), the periodicity a_{n+T} = a_n + L holds from n=1 literally — closing BOTH
     the primary and secondary gaps at once, the two-birds payoff that motivates this
     approach's inclusion.
  5. If Step 3 stalls or reduces to gap † in disguise (flagged as a real risk in the
     skeleton itself, not hidden), fall back to reporting the reduction honestly:
     "reversibility here requires exactly the same fact gap † requires," which would
     still be useful negative information for the population (rules out this framing
     as a genuine bypass) rather than a wasted round.

Key lemmas (mechanism):
  - Injectivity attempt (Step 3): the greedy "smallest legal integer" selection rule is
    a strictly monotone function of the current value once the legality SET is fixed —
    the open question is whether the finite state σ(n) determines the legality set
    (equivalently, is a sufficient statistic for "which primes must divide the next
    term"), which is either a genuinely new, more tractable claim or an equivalent
    restatement of gap † — must be checked explicitly, not assumed favorable.
Open gaps: Step 1 (fixing M, B rigorously — depends on eventual-regime facts already
proved elsewhere, needs assembling not new content). Step 3 (injectivity) — entirely
open, explicitly flagged by the explorer as unattempted and possibly circular with gap
†; the builder's FIRST job should be determining whether Step 3 is genuinely easier
than gap † or a relabeling of it, before investing further.
Cases to cover: none additional beyond the general argument (a bijection argument does
not require casework by design — that is its appeal).
Watch out for: the round-4 memory NEVER-rule about a superficially similar "reduce a_n
mod fixed M to a finite-state automaton" framing that turned out to be isomorphic to
the existing Step-5 CRT+cyclic-pigeonhole finish — this approach differs from that by
targeting INJECTIVITY of the transition map as the proof mechanism (not just restating
the finish in automaton language); the builder must verify this distinction holds up
in practice (i.e. that Step 3 is not itself secretly Step 5 restated) before claiming
progress, per that same memory rule's spirit.

---

### Population notes
- **amortized-charging-budget, density-sieve-contradiction, hypergraph-transversal**:
  left untouched (stale, low Elo, no new mechanism surfaced this round that they alone
  would need); do not include in the build set.
- **witness-depth-bound**: RETHINK verdict from round 3 stands (proven scope
  observation: cannot close gap † as framed even if solved); not revised this round —
  no new information surfaced that changes this verdict.
- Recommended build set (for the outline-reviewer to confirm/adjust): all four above —
  covering-system-construction, greedy-exchange-cost-potential (both revisions of live,
  high-Elo approaches attacking the corrected process-termination target from
  complementary angles: simultaneous-resolution vs. Singleton-Hypothesis-in-general),
  plus witness-index-descent and reversible-transition-map (two genuinely new framings,
  different proof STYLES — well-ordering descent and bijectivity — from the existing
  forward-induction population, per CLAUDE.md's diversity rule and the memory rule
  about breaking shared-gap plateaus with a different mechanism, not a same-framing
  bypass).
