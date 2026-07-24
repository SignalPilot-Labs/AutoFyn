## Status
unsolved

## Approaches tried
- (round 22, fresh skeleton — not yet built) See below.
- **(round 22, this build): mandatory disambiguation check, performed first
  as required by the outline-reviewer, per the round-5
  `reversible-transition-map` precedent.** Concrete finding, with both a
  computation and a proof: **the check FAILS.** Both natural formalizations
  of the outline's Step A "candidate offset object" collapse into content
  that is either already-confirmed-dead (the round 6–9 existential-to-
  universal promotion family) or is provably a *downstream consequence* of
  the very periodicity conclusion the whole problem seeks — not an
  independent stepping stone toward FAH, and in fact circular in a stronger
  sense than round 5's finding (round 5's forward map was equivalent to gap
  †; this object turns out equivalent to *full eventual periodicity of the
  sequence itself*, i.e. essentially the problem's conclusion). Additionally,
  and independently of the well-definedness question, **Step C is a real,
  unaddressed gap, not "relatively mechanical" as the outline hoped**: the
  offset object as defined only carries index/ordering information and
  structurally discards the prime-divisibility information that FAH's
  conclusion (`A'∩B'≠∅` within `S*`) is actually about, so there is no
  evident route from "offset well-defined" to "the two types share an
  `S*`-prime," even granting well-definedness for free. Full detail below.
  No new lemma is certified this round (the findings are negative/
  diagnostic, matching the existing workspace convention for such rounds,
  e.g. `reversible-transition-map.md`, `fah-counterexample-hunt.md` round
  21–22). **Recommendation to the outline-reviewer: this approach should not
  be advanced in its current form; Steps A–C need a genuinely different
  candidate object that references divisibility data directly (not just
  occurrence order), or the approach should be retired as a 31st dead
  mechanism in the same family diagnosed by the workspace's own recurring
  finding (`n1-periodicity-reconciliation.md` §4, "every attempt implicitly
  assumes an ensemble of possible continuations... no such ensemble exists
  without an explicit construction").**

## Current best

Nothing proved unconditionally toward FAH (H1) or the problem's claim. The
round's contribution is entirely diagnostic: a concrete disambiguation check
(mandated first deliverable) that rules out this approach's two natural
instantiations, plus an honest identification of a third, structural
obstruction (Step C) that would remain even if Step A/B were somehow
rescued. This is recorded in full below so no future round re-invests in
either instantiation without first reading this.

### 0. Setup (shared machinery, imported not re-derived)

Fix the certified stack, exactly as used throughout the workspace (see
`n1-periodicity-reconciliation.md` §0 for full citations): `Q = P(a_1)`,
`S₀` the Finite Core Theorem's core, `S*` a (hypothetical) terminal
self-absorbing core from the absorption chain, `𝒫'(S*)` the finite set of
`S*`-extended-persistent types with `ρ_{S*}(n) := P(a_n)∩S*`, each occurring
infinitely often for `n` beyond a finite threshold (Extended Persistent-Type
Pigeonhole). **(H1) FAH at `S*`**: every two disjoint-base-type
`A',B'∈𝒫'(S*)` satisfy `A'∩B'≠∅`.

Fix, for the remainder, a candidate rogue pair `A', B' ∈ 𝒫'(S*)` with
disjoint base types (the case FAH is actually about), and let
`n_1 < n_2 < ⋯` be the indices with `ρ_{S*}(n_i)=A'`, `m_1<m_2<⋯` the
indices with `ρ_{S*}(m_i)=B'` (both infinite by the Pigeonhole).

### 1. The mandatory disambiguation check — instantiation 1: single-prime divisibility split (outline's "more promising native alternative")

**The candidate object.** By Free Facts (`free-facts-gcd.md`),
`gcd(a_{n_1}, a_{m_1}) > 1`, giving a witness prime `q | gcd(a_{n_1},a_{m_1})`.
If `A'∩B' = ∅` (rogue case, the case FAH must rule out), then `q ∉ S*`
(any prime of `S*` dividing both `a_{n_1}` and `a_{m_1}` would lie in
`P(a_{n_1})∩S* ∩ P(a_{m_1})∩S* = A'∩B' = ∅`, contradiction) — this is exactly
the Generalized Bounded Witness Lemma's Corollary, reused not re-derived
(same mechanism used in `reversible-transition-map.md` §2, `⇒` direction).
Define `D_q(i) := 1` if `q | a_{n_i}`, else `0`, for the `A'`-occurrence
index sequence.

**Why this instantiation fails the check.** The only way this object could
feed Step C ("offset ⟹ FAH") is via a claim of the shape "`D_q(i) = 1` for
cofinitely many `i`" (q eventually divides every `A'`-occurrence). But two
independent problems kill this outright, and both were already diagnosed in
this workspace before this round:

  (a) **It is exactly the round 6–9 dead mechanism family.** Promoting a
  single existential witness (`q` divides *some* `A'`-occurrence, which is
  all Free Facts gives) to a cofinite/universal claim ("`q` divides *every*
  `A'`-occurrence") is verbatim the "existential-to-universal promotion"
  family catalogued as dead in `n1-periodicity-reconciliation.md` §4 (the
  round-7 Witness Discontinuity Obstruction gives a concrete counterexample,
  `a_1=175`, to the natural repair of this exact promotion). This round adds
  no new mechanism to escape that obstruction — the "pair with the
  non-dividing subsequence" framing is a relabelling of the same promotion
  question, not a new attack on it.

  (b) **Even if provable, it would not prove FAH.** Since `q ∉ S*` (shown
  above, for the rogue case that actually matters), "`q` divides every
  `A'`-occurrence" says nothing about a shared prime *within* `S*` — FAH's
  conclusion is `A'∩B'≠∅` as subsets of `S*` specifically. What "`q` gets
  absorbed" content of this kind *would* be relevant to is whether `q`
  belongs in an *enlarged* core (i.e. the absorption-chain recruitment
  process, `S* ↦ S*⁺`) — that is **H2/termination territory, not H1/FAH**,
  a distinct hypothesis per `n1-periodicity-reconciliation.md` §1 ("no
  reduction either way between H1 and H2 is known"). So this instantiation,
  even in the best case, targets the wrong open hypothesis.

  **Verdict on instantiation 1: FAIL the disambiguation check — dead by (a),
  and mis-targeted by (b) even setting (a) aside.**

### 2. The mandatory disambiguation check — instantiation 2: index-alignment offset between the two occurrence sequences

**The candidate object (the outline's primary suggestion).** For each
`A'`-occurrence index `n_i`, define the *nearest-neighbor offset*
`off(i) := m_j - n_i` where `m_j` is the `B'`-occurrence index nearest `n_i`
(the natural precise reading of "do the index sequences ... satisfy a fixed
additive shift"). **Well-definedness claim to test:** `off(i)` is eventually
constant, or eventually periodic in `i` with a fixed small period.

**Computation (this round, done before investing further effort, per the
outline-reviewer's requirement).** Simulated `a_1=385` (the workspace's
canonical hard seed, `Q={5,7,11}`, independently confirmed by
`fah-counterexample-hunt.md` round 21 to have exact period `(T,L)=(5088,43890)`
with zero violations over 5 periods) for 15300 terms (≈3 periods), using a
fresh from-scratch bitmask greedy generator (independent of both round-21
generators; cross-checked internally by confirming `a_{5088}-a_0 = 43890`
exactly, matching the certified period). Took `A = \{5\}`, `B = \{7\}` as
disjoint **base** types (a legitimate, simpler proxy for disjoint-base-type
extended types, since `\{5\},\{7\}\subseteq Q\subseteq S*` are themselves
disjoint-base-type by construction). Findings (script:
`/tmp/round-22/offset_test.py`):

  - **The literal same-rank pairing (`m_i - n_i`, pairing the `i`-th `A'`
    occurrence with the `i`-th `B'` occurrence) is not even bounded** — it
    drifts essentially linearly, from `+1` at `i=1` to `-7776` by `i=3427`
    (the full run). This is not a subtle failure: `A=\{5\}` occurs 3427
    times and `B=\{7\}` occurs 6977 times in the same 15300-term window (a
    genuinely different density, not a coincidence — this is forced by the
    two base types occurring different numbers of times *within a single
    period*, confirmed below), so same-rank pairing is not even a
    well-posed object to ask "eventually constant" about.
  - **The nearest-neighbor version is bounded** (`off(i) ∈ \{-2,-1,1,2\}` for
    all late `i`) **but not constant** — it genuinely oscillates among these
    four values, not settling to one.
  - **Diagnosing why:** directly verified that the `A'`-occurrence index
    sequence itself satisfies `n_{i+1140} = n_i + T` (`T=5088`) exactly, for
    every tested `i` past a short transient — i.e. `A` occurs **exactly
    1140 times per period**, and (by the identical argument) `B` occurs a
    different fixed count per period. The nearest-neighbor offset's bounded-
    but-non-constant, period-1140-repeating pattern is *exactly* the
    fingerprint of "two interleaved periodic sequences with different
    fixed within-period counts," i.e. **precisely what you get for free once
    the whole sequence is already known to be periodic with period `T`** —
    it is not additional information beyond that.

**Theorem (this round, proved from the computation's structure, not merely
observed).** *If the full sequence is eventually periodic (`a_{n+T}=a_n+L`
for `n≥N`), then for any two types `A,B` with fixed per-period occurrence
counts `k_A,k_B ≥ 1`, the nearest-neighbor offset between their occurrence-
index sequences is eventually periodic in `i` with period `k_A` (a bounded,
finite-valued, eventually-repeating pattern, matching the computation).*
*Proof.* Since `ρ_{S*}(n)` depends only on `a_n mod L` (`S*`-primes divide
`a_n` iff they divide `a_n mod L`, standard CRT fact already used
throughout, e.g. `self-absorbing-core-theorem.md` Step 1), and
`a_{n+T} ≡ a_n \pmod L` for `n≥N`, the label sequence `ρ_{S*}(n)` is itself
periodic with period `T` for `n≥N`. Hence the index set `\{n: ρ_{S*}(n)=A\}`
is, past `N`, a union of full periods' worth of a fixed within-period
pattern, giving `n_{i+k_A}=n_i+T` for large `i` (`k_A` := occurrences of `A`
in one period), and likewise for `B`. The nearest-neighbor map, applied to
two eventually-`T`-periodic index sets, is itself eventually periodic in `i`
with period `k_A` (advancing `i` by `k_A` advances `n_i` by exactly `T`,
which maps to the "same" nearest `B`-occurrence shifted by exactly `T`, i.e.
the same relative offset value repeats). `∎`

**Conclusion of instantiation 2's disambiguation check.** This theorem shows
the "offset is eventually periodic/bounded" claim is a **direct, mechanical
consequence of already knowing the whole sequence is eventually periodic**
— exactly the problem's own conclusion, restricted to two types. It supplies
NO independent leverage toward proving periodicity (equivalently, toward H1):
proving the offset well-defined **unconditionally, without first assuming
eventual periodicity**, is not evidently easier than proving eventual
periodicity itself directly, and no argument in this round (or found by
searching the certified stack) establishes the offset's well-definedness by
any route that does not already presuppose the periodic structure. This is a
strictly stronger circularity than round 5's finding (round 5's forward map
was equivalent to gap †, one specific open hypothesis; this object is
equivalent, in the direction that matters for well-definedness, to the
*conclusion of the whole problem* for the relevant types). **Verdict on
instantiation 2: FAIL the disambiguation check — not new content, and
strictly more circular than the round-5 precedent it was required to be
checked against.**

### 3. A further, independent obstruction found this round: Step C does not go through even if Step A/B were free

Separate from the circularity above: suppose, hypothetically, some future
round found a way to establish "the nearest-neighbor offset is eventually
periodic" **unconditionally** (not by first assuming full periodicity). The
outline's Step C claims this would be "a relatively mechanical consequence"
to turn into FAH (`A'∩B'≠∅`). This round finds that claim is false as
stated: the offset object, by construction, is built entirely from **which
indices carry which label** (an ordering/occurrence-count fact) — it never
references, and by the nearest-neighbor definition cannot recover, **which
prime** is shared between any `a_{n_i}` and any `a_{m_j}`, or whether one
even exists within `S*`. FAH's conclusion is specifically about a shared
`S*`-prime. There is no general principle (checked against the full
certified stack in `lemmas/`, none of which connects occurrence-order
statistics to shared-prime existence) taking "these two labels alternate in
an eventually periodic pattern" to "these two labels' underlying sets share
a fixed prime." (Concretely: one can imagine, in principle, two types whose
occurrences interleave in a perfectly rigid periodic pattern for reasons
having nothing to do with sharing a common `S*`-prime — e.g. if both were
forced into a periodic slot structure by a THIRD type's periodicity — so
periodic interleaving alone does not certify intersection.) This is an
independent reason (b), on top of reason (a) from §2, that this approach's
central dichotomy does not currently deliver a proof route to FAH, even
granting the most optimistic resolution of Step A/B.

### 4. Honest overall assessment

Per the round-22 dispatch's requirement, this is reported honestly rather
than as partial progress dressed up: **both natural formalizations of the
outline's Step A fail the mandated disambiguation check** — instantiation 1
(single-prime divisibility split) is the already-catalogued-dead round 6–9
existential-to-universal family, mistargeted at H2 territory even if it
worked; instantiation 2 (index-alignment offset) is not independent content,
being a direct downstream consequence of the problem's own conclusion, a
stronger circularity than the round-5 precedent this check was modeled on.
On top of both, §3 identifies that Step C's promised "mechanical" step from
offset-well-definedness to FAH has no evident proof even setting well-
definedness aside, because the offset object structurally discards
divisibility information. **This approach, in its current form, should not
receive further build effort** — it is not a bypass of the standing
FAH crux, and joins the workspace's dead-mechanism catalogue (as a 31st
entry, in the same "assumes an ensemble of possible continuations without
constructing one" diagnosis already recorded in
`n1-periodicity-reconciliation.md` §4) rather than opening a new corridor. A
genuinely different candidate object — one that references actual shared-
prime data between specific realized terms directly, not just occurrence
order — would be needed to revive this framing; none is proposed here.

### 5. Reproducibility

Script: `/tmp/round-22/offset_test.py` (self-contained, uses `sympy` for
prime factorization; regenerates `a_1=385` from scratch via an independent
bitmask greedy generator, verifies the known period `(T,L)=(5088,43890)`
inline via `a_{5087}, a_{5088}-a_0`, then computes both offset instantiations
and the periodic-block-size diagnostic reported above).

## Full proof
Not present — Status is `unsolved`. This round's deliverable is entirely the
mandated disambiguation check (§1–§2) plus the independent Step C
obstruction (§3), both negative findings; no proof progress toward FAH (H1)
or the problem's claim was made or is claimed.
