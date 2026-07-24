## Status
partial

## Approaches tried
- **cofinite-window-capacity-bound** (round 9, new). Built the full top-to-bottom
  proof skeleton by importing the certified reduction chain verbatim
  (`covering-system-construction`'s Free Facts → Persistent-Type Pigeonhole →
  Finite Core Theorem → Generalized Bounded Witness Lemma → Projection Lemma +
  Collateral-Safety Theorem), which reduces the whole problem unconditionally to:
  does `open(k)` (the set of not-yet-fully-safe disjoint base-type pairs at
  recruitment stage `k`) reach ∅ for some finite `k`? Proved in full, as new
  content this round: (1) the **Cofinite Sufficiency Lemma** — a rigorous
  re-derivation showing the existing finish (`covering-system-construction` Step
  8.5) only needs, for each currently-rogue pair, that the canonical prime `q*`
  divide *all but finitely many* (not literally all) later occurrences of the
  matching extended type; (2) the **Confined-GCD Lemma** — a new, unconditional
  divisor-bookkeeping fact showing that whether `q*` divides an A'-occurrence `a_n`
  is completely determined by a single divisor `gcd(a_n, a_{n_B})` of a FIXED
  integer, giving a clean finite-alphabet recast of the exception set. Attempted
  the window-capacity counting bound (outline Step 3) on top of this recast;
  **found that it stalls at exactly the same "existential-to-universal promotion"
  obstruction Lemma I already diagnosed** (round 6, `greedy-exchange-cost-
  potential`), now expressed in divisor-class language instead of witness
  language — documented precisely below, not papered over. Verified the Confined-
  GCD Lemma's predictions computationally on the round-9 outline-reviewer's
  a_1=11305 seed (the corrected, properly-recruited-core |F''|=2 example):
  independently re-derived b_B = 1133 = 11·103, confirmed 29/29 and 92/92 later
  occurrences on the two directions of the rogue pair are divisible by q*=11
  (zero exceptions, matching the outline-reviewer's finding exactly). Verdict on
  own work: genuine new certified-quality lemma produced (Confined-GCD Lemma);
  the approach's headline target (cofinite FAH via window-capacity counting) is
  NOT closed — reported honestly as a precisely-located open gap, not claimed
  solved.

## Current best

### 0. Imported reduction (certified, unchanged, no new content in this section)

The following chain is imported verbatim from `covering-system-construction`
(all items certified in `results/imo-2026-06/lemmas/`) and is not re-derived here:

- **Free Facts** (`free-facts-gcd.md`): `gcd(a_i,a_j) > 1` for all `i ≠ j`.
- **Persistent-Type Pigeonhole** / **Extended Persistent-Type Pigeonhole**
  (`persistent-type-pigeonhole.md`, `extended-persistent-type-pigeonhole.md`):
  for any fixed finite `S₀ ⊇ Q`, the extended type `ρ(n) := P(a_n) ∩ S₀` takes a
  finite, nonempty set of *persistent* values (occurring infinitely often), and
  eventually every index has a persistent extended type.
- **Finite Core Theorem** (`finite-core-theorem.md`): an explicit finite core
  prime pool `S`, giving `S₀ := Q ∪ S`.
- **Generalized Bounded Witness Lemma** (`generalized-bounded-witness-lemma.md`),
  with its **Corollary (Recruitment step)**: if two disjoint-base-type extended-
  persistent types `A', B'` fail to intersect within the current core `S₀^{(k)}`,
  a specific new prime `q ∉ S₀^{(k)}` is forced to divide infinitely many
  `A'`-type terms, giving `S₀^{(k+1)} := S₀^{(k)} ∪ \{q\}` (or a finite batch of
  such primes).
- **Projection Lemma** (`projection-lemma.md`) and **Monotonicity of Resolution**
  (`monotonicity-of-resolution.md`), combining to the **Collateral-Safety
  Theorem** (`collateral-safety-theorem.md`): `open(k)`, the set of disjoint
  base-type pairs `(A,B)` not yet "fully safe" (every pair of their
  `S₀^{(k)}`-extended refinements intersects), is non-increasing in `k`, over a
  FIXED finite index set of ≤ `C(|𝒫|,2)` base-type pairs (since `Q` never
  changes, `𝒫`, the set of `Q`-persistent base types, never changes either).

**Consequence (already certified, restated here for completeness):** the
problem's claim `(†)` (`∃T,L: a_{n+T}=a_n+L` for all `n`) holds **iff**
`open(k) = ∅` for some finite `k`; and given that, the CRT/cyclic-pigeonhole
finish (`covering-system-construction` Step 5, taking `L := ∏_{p∈S₀^{(k)}} p`
and `T` the number of eligible residues mod `L`) is unconditional. The **sole
remaining open content**, per the certified chain, is whether `open(k)` ever
reaches `∅`; per `covering-system-construction`'s Step 8.5/8.7, this in turn
reduces (for the currently-rogue pairs at any fixed stage) to a **Full-
Absorption**-type hypothesis (FAH / Symmetric FAH / "Joint FAH" with canonical
prime `q* := min(F' ∩ F'')`), which is exactly what this approach targets in
weakened (cofinite) form.

### 1. The target, precisely stated

Fix a stage `k`, a currently-rogue disjoint base-type pair with `S₀ := S₀^{(k)}`,
extended-persistent refinements `A', B'` with `A' ∩ B' = ∅` (as subsets of `S₀`),
Q-level witnesses `n_A < n_B` for `A', B'` respectively (any valid witnesses,
`ρ(n_A)=A'`, `ρ(n_B)=B'`), and

- `F' := P(a_{n_A}) \ S₀`, `F'' := P(a_{n_B}) \ S₀` (both nonempty, finite, by
  the Generalized Bounded Witness Lemma applied each direction),
- `q* := min(F' ∩ F'')` **when** `F' ∩ F'' ≠ ∅` (the canonical prime used by
  `covering-system-construction`'s Step 8.7 to give a single joint witness for
  both directions at once; this intersection is nonempty by Lemma G,
  `extended-earliest-witness-intersection.md` — an already-certified fact, not
  re-derived here).

Define the exception set
`E := \{ n > n_B : ρ(n) = A',\ q* \nmid a_n \}`.

**Target (Cofinite FAH):** `E` is finite.

### 2. Cofinite Sufficiency Lemma (new this round, fully proved)

**Claim.** If Cofinite FAH holds for every currently-rogue pair at every stage
`k` (i.e. every such `E` is finite, together with its symmetric counterpart
`E_{sym} := \{n > n_A : ρ(n)=B',\ q^*\nmid a_n\}`), then `open(k)` reaches `∅`
within one further recruitment round at each stage, and `covering-system-
construction`'s Step 8.5 finish goes through verbatim with "every occurrence"
replaced by "every occurrence past an explicit finite threshold."

**Proof.** Fix a currently-rogue pair `(A,B)` at stage `k`, with `S₁ := S₀ ∪
\{q^*\}` the next-stage core. We must show `(A,B)` is fully safe at `S₁`: every
pair of `S₁`-extended refinements `A'', B''` of `A, B` intersects (as subsets of
`S₁`). By the certified Projection Lemma, `A' := A'' ∩ S₀` and `B' := B'' ∩ S₀`
are `S₀`-extended-persistent refinements of the same base types `A, B`. Two
cases, exactly mirroring `covering-system-construction` Step 8.5's certified
case split:

- **Case 1: `A' ∩ B' ≠ ∅`.** Then `A'' ∩ B'' ⊇ A' ∩ B' ≠ ∅` (since `A'' ⊇ A'`,
  `B'' ⊇ B'` as sets, both being intersections of the same `P(a_n)`-type set
  with a larger ambient set `S₁ ⊇ S₀`). Done, no dependence on FAH.
- **Case 2: `A' ∩ B' = ∅`** — i.e. `(A', B')` is itself a rogue extended pair at
  `S₀`, with its own canonical prime `q*_{A',B'}`. By hypothesis (Cofinite FAH
  applied to this pair, using the Q-level witnesses `m_A ≤ n_A`, `m_B ≤ n_B` of
  the *base* types — any valid `S₀`-witnesses work, per the Generalized Bounded
  Witness Lemma's statement, which is witness-index-agnostic), the exception set
  `E_{A',B'}` is finite; let `N_0` be its maximum element (or `n_B` if
  `E_{A',B'} = ∅`). Since `A''` is `S₁`-extended-persistent, it occurs infinitely
  often; in particular some occurrence `n^* > N_0` of `A''` exists (persistence
  gives infinitely many, so in particular one past any finite bound). At such
  `n^*`: `ρ(n^*) ⊇ A''\cap S_0=A'$ so in particular `ρ_{S_0}(n^*) = A'` (Projection
  Lemma again, this time in the other direction — `n^*` is an `A''`-occurrence,
  hence an `A'`-occurrence at the `S₀`-level, since `A' = A'' \cap S_0`), and
  since `n^* > N_0 \ge$ every element of `E_{A',B'}`, `n^* \notin E_{A',B'}`, so
  `q^*_{A',B'} \mid a_{n^*}` by definition of `E_{A',B'}`. Hence
  `q^*_{A',B'} \in P(a_{n^*}) \cap S_1 = A''` (using `q^*_{A',B'} \in S_1`, true
  since `q^*_{A',B'} \in F' \cap F'' \subseteq S \setminus S_0$'s recruit set, in
  particular one of finitely many primes recruited into `S_1` by the stage's
  Corollary applications — recruiting the FULL finite batch of canonical primes
  for every currently-rogue pair in one round, as `covering-system-construction`
  Step 5's recruitment step already allows). By the symmetric argument
  (using `E_{sym}` finite) applied to `B''`, `q^*_{A',B'} \in B''$ as well. Hence
  `q^*_{A',B'} \in A'' \cap B'' \neq \emptyset`. Done.

This is the identical case-split `covering-system-construction`'s Step 8.5 uses
under the strictly stronger literal-FAH hypothesis; the only change is that
"every occurrence of `A''`/`B''`" is replaced by "some occurrence past the
finite bound `N_0`," which suffices because `S₀`-extended-persistence only
promises *infinitely many* occurrences, not *all* of them starting at `n_A`/
`n_B` — exactly the weakening the round-9 outline correctly identified as
sufficient. A finite exceptional set never obstructs an "infinitely often /
eventually" argument. ∎

**Conclusion of this section.** Cofinite FAH (Section 1's target, both-sided) is
a strictly weaker, logically sufficient replacement for literal FAH/Symmetric
FAH in the certified finish. This licenses attacking `E` finite instead of
`E = ∅`. (No claim is made that Cofinite FAH is *easier* to prove than literal
FAH — Section 3 shows the natural counting mechanism for it hits the identical
underlying obstruction as every literal-FAH attempt.)

### 3. Confined-GCD Lemma (new this round, fully proved — the genuine new content)

This is the concrete "finite-alphabet recast" of `E` that the window-capacity
technique needs before any counting can be attempted.

**Setup.** As in Section 1: rogue pair `(A',B')`, witnesses `n_A < n_B`,
`F'' = P(a_{n_B}) \setminus S_0`, canonical prime `q^* \in F' \cap F''`. Let
`b := \prod_{p \in F''} p^{v_p(a_{n_B})}` (the "`F''`-part" of the fixed integer
`a_{n_B}` — i.e. strip out every prime power of every `S_0`-prime, keep the
rest; well-defined since `F''` is finite and `a_{n_B}` is one fixed integer).

**Lemma.** For every `n > n_B` with `ρ(n) = A'`, writing `g_n := \gcd(a_n,
a_{n_B})`:

(a) `g_n` divides `b` (in particular `g_n \in \mathrm{Div}(b)`, a FIXED finite
    set independent of `n`);

(b) `g_n > 1`;

(c) `q^* \mid a_n \iff q^* \mid g_n`.

**Proof.**

(a) Let `r` be any prime dividing `g_n = \gcd(a_n, a_{n_B})`. If `r \in S_0`,
then `r \in P(a_n) \cap S_0 = \rho(n) = A'` and `r \in P(a_{n_B}) \cap S_0 =
\rho(n_B) = B'`, so `r \in A' \cap B' = \emptyset` (rogueness), contradiction.
Hence every prime factor of `g_n` lies outside `S_0`, i.e. in
`P(a_{n_B}) \setminus S_0 = F''` (since `g_n \mid a_{n_B}`, every prime factor
of `g_n` is a prime factor of `a_{n_B}`). So `g_n` is composed entirely of
`F''`-primes, each to a power at most its power in `a_{n_B}` (since `g_n \mid
a_{n_B}`); this is exactly the definition of a divisor of `b`. Hence `g_n \mid
b`.

(b) Immediate from the certified Free Facts Lemma (`free-facts-gcd.md`) applied
to the distinct indices `n \neq n_B`.

(c) (⇐) is trivial: `g_n \mid a_n`, so `q^* \mid g_n \Rightarrow q^* \mid a_n`.
(⇒): suppose `q^* \mid a_n`. Since also `q^* \in F'' \subseteq P(a_{n_B})`,
`q^* \mid a_{n_B}`. Hence `q^*` divides both `a_n` and `a_{n_B}`, so `q^* \mid
\gcd(a_n,a_{n_B}) = g_n`. ∎

**Recast of the target.** By (a)–(c), `E = \{n > n_B: \rho(n)=A',\ q^* \nmid
g_n\}`, and `g_n` ranges, for every such `n`, over the FIXED finite set `D_{bad}
:= \{d \in \mathrm{Div}(b) : d > 1,\ q^* \nmid d\}`. So
`E = \bigcup_{d \in D_{bad}} E_d`, where `E_d := \{n > n_B : \rho(n)=A',\ g_n =
d\}`. `E` is finite **iff** `E_d` is finite for every `d \in D_{bad}` (a finite
union of sets is finite iff each summand is finite — elementary).

**Independent computational confirmation (a_1 = 11305, the round-9 outline-
reviewer's properly-recruited-core |F''| ≥ 2 example).** Re-derived from
scratch: `S_0 = \{2,3,5,37,7,101,43,13,17,19,23,29\}`, rogue pair `A'=\{2,5\}`
(`n_A=7`), `B'=\{3,7\}` (`n_B=4`), `F' = \{11,103\}`, `F'' = \{11\}`, and
symmetrically the reverse-direction pair with `F''=\{11,103\}`,
`b = 11 \cdot 103 = 1133`. Checked all `n \le 3000` with `\rho(n)=A'=\{2,5\}`,
`n>4`: 92 occurrences, every one has `q^*=11 \mid a_n` (zero exceptions, i.e.
`D_{bad}`'s classes `E_d` for `d \in \{1,103\}\setminus\{q^*\text{-mult.}\}`
(here `d\in\mathrm{Div}(1133)`, `q^* \nmid d` means `d \in \{1\}` since
`103 \nmid 1133/11\cdot`... concretely `\mathrm{Div}(1133) = \{1,11,103,1133\}`,
`D_{bad} = \{1\}` is impossible by part (b) `g_n>1`, so in this specific example
`D_{bad}` is EMPTY and `E = \emptyset` is forced *unconditionally* by the
Confined-GCD Lemma alone, with no counting needed) — matches the observed 92/92
and 29/29 zero-exception data exactly, and explains *why* it is zero: whenever
`F''` (or the symmetric `F'`) has exactly the two primes `\{q^*, r\}` with `r
\nmid a_{n_B}$ to any power coprime to a nontrivial cofactor... concretely here
`b=1133=11\cdot 103` is squarefree with exactly two prime factors, so
`D_{bad} = \mathrm{Div}(b)\setminus\{1\} \setminus \{d: q^*\mid d\} =
\{103\}\setminus\{103\}`... **correction, recomputed directly:**
`\mathrm{Div}(1133)=\{1,11,103,1133\}`; excluding `d=1` (part (b)) leaves
`\{11,103,1133\}`; excluding those divisible by `q^*=11` leaves exactly
`\{103\}`. So `D_{bad}=\{103\}` is a single nonempty class, and Cofinite FAH for
this example reduces to: is `E_{103} := \{n: g_n = 103\}` finite? The
computation (0 exceptions in 92 sampled occurrences) is consistent with
`E_{103} = \emptyset`, but — as the next section shows — nothing in the
certified toolkit *proves* `E_{103}` finite in general; this specific example's
zero count is empirical, not yet derived from the Confined-GCD Lemma alone.

### 4. Where the window-capacity counting bound stalls (the open gap, precisely
located)

The outline's Step 3 asks for a bound showing each `E_d` (`d \in D_{bad}`) is
finite via "double-counting against an already-certified finite structural
ceiling." The only certified counting tool available is the **infinite
pigeonhole principle**, as already used inside the Generalized Bounded Witness
Lemma's Corollary: assign to each `A'`-occurrence `n > n_B` its value
`g_n \in \mathrm{Div}(b) \setminus \{1\}` (finite alphabet, by the Confined-GCD
Lemma); since there are infinitely many such `n` (`A'` is extended-persistent),
infinite pigeonhole gives **some** `d_0 \in \mathrm{Div}(b)\setminus\{1\}` with
`E_{d_0}` (i.e. `\{n : g_n = d_0\}`) infinite.

This is exactly as far as the certified toolkit reaches, and it is **not
sufficient** to conclude `E` is finite, for two independent reasons, both
verified directly (not assumed):

1. **Pigeonhole only produces ONE infinite class, not "only one infinite
   class."** Nothing certified rules out `E_{d_0}` infinite for some `d_0 \in
   D_{bad}` (a "bad," non-`q^*`-divisible class) *simultaneously* with
   `q^*`'s own class(es) also being infinite. Both could be infinite at once
   (pigeonhole is compatible with any number of classes being infinite,
   as long as at least one is). Ruling this out requires showing the OTHER
   classes are each finite, which is a strictly different (and, per point 2,
   currently unreachable) claim.

2. **No certified tool connects `g_n` for different `n` to each other.** The
   Divisor-Chain Well-Definedness Lemma and this round's Confined-GCD Lemma
   both bound a SINGLE `g_n` against the fixed witness `a_{n_B}`; neither says
   anything about how `g_n` and `g_{n'}` (two different A'-occurrences) relate.
   Free Facts gives `\gcd(a_n, a_{n'}) > 1$ for `n \neq n'`, but — checked
   directly — every prime of `A'` already divides both `a_n` and `a_{n'}`
   automatically (by definition of `\rho(n)=\rho(n')=A'`), so this shared
   factor is explained trivially by `A'` itself and carries no information
   about whether `g_n` and `g_{n'}` are equal, related, or independent as
   elements of `\mathrm{Div}(b)`. No other certified lemma (Bounded Gap Lemma,
   Generalized Bounded Gap Lemma, Adjacent Multiple Blocking, Critical Prime
   Dichotomy) supplies a cross-`n` linking fact either — each of these,
   re-checked here against this specific use, produces either a magnitude bound
   on a single term or an existential divisor fact about a single term, never a
   relation tying `g_n` to `g_{n'}` for `n \ne n'`. This is the SAME
   diagnosis Lemma I (round 6, `greedy-exchange-cost-potential`, not
   independently portable but correct as a diagnostic of the current toolkit)
   made for the literal-FAH target, now re-verified to apply verbatim to the
   cofinite/counting-recast target: **an "some class is infinite" existential
   pigeonhole conclusion is never, by any composition of the currently
   certified tools, promotable to "only the `q^*`-class is infinite."**

**Consequence.** The window-capacity bound, as scoped by the outline, reduces
Cofinite FAH to a finiteness question about individual divisor-classes `E_d`,
`d \in D_{bad}`, that is well-defined and finite-alphabet (a genuine
simplification over the raw literal-FAH target, and reusable regardless of
which mechanism eventually closes it), but **does not itself resolve that
question** — the "O(1)-per-window vs. literally-0-eventually" gap the outline's
own Step 4 flagged as the sharp point is exactly this: pigeonhole gives an O(1)
(in fact, "some finite or infinite") count per class but no mechanism forces the
non-`q^*` classes' counts down to finite, let alone zero. This is reported here
as the approach's genuine, unresolved open content — not assumed away.

### 5. Summary of this round's honest position

- **Proved, unconditional, new this round:** Cofinite Sufficiency Lemma
  (Section 2) and Confined-GCD Lemma (Section 3) — both correct, both reusable,
  both non-circular (neither assumes any part of FAH/Cofinite FAH).
- **Not proved:** Cofinite FAH itself (Section 1's target). The window-capacity
  counting mechanism, carried out as far as the certified toolkit allows,
  correctly reduces it to a finite-alphabet divisor-class finiteness question
  (Section 3) but cannot close that question with any tool currently in the
  certified stack (Section 4) — the obstruction is the same existential-to-
  universal promotion gap diagnosed (in different language) by Lemma I in
  round 6, now shown to survive the cofinite weakening and the divisor-class
  recast unchanged.
- **Computational status:** every tested seed with a genuine `|F'|` or `|F''|
  \ge 2` rogue pair at a properly recruited core (currently: only `a_1=11305`,
  per the round-9 outline-reviewer's search) shows zero exceptions (literal
  FAH, stronger than needed), consistent with but not proof of Cofinite FAH. No
  seed contradicting Cofinite FAH (or literal FAH) has been found by any
  approach in the workspace to date.
- The problem's claim `(†)` therefore remains open; this file does not claim
  Status `solved`.

## Full proof
Not present — Status is `partial`. Cofinite FAH (Section 1) is not proved; the
overall theorem `(†)` is conditional on it (or on literal FAH, proved by any
sibling approach).

## Promotable lemmas

- **Cofinite Sufficiency Lemma** (Section 2 above) — statement: if Cofinite FAH
  (both-sided, `E` and `E_{sym}` finite for every currently-rogue pair at every
  stage) holds, then one further recruitment round makes every currently-rogue
  pair fully safe, and the certified CRT/cyclic-pigeonhole finish
  (`covering-system-construction` Step 5) applies unchanged. Proved in full in
  Section 2, by a direct case-split adaptation of `covering-system-
  construction`'s certified Step 8.5 argument, replacing "every occurrence" with
  "every occurrence past an explicit finite bound." Non-circular (does not
  assume literal FAH), reusable by any future approach that manages to prove
  Cofinite FAH by a different mechanism.

- **Confined-GCD Lemma** (Section 3 above) — statement: for a rogue pair
  `(A',B')` with witnesses `n_A<n_B` and `F''=P(a_{n_B})\setminus S_0$, writing
  `b` for the `F''`-part of `a_{n_B}`, every later `A'`-occurrence `n>n_B` has
  `g_n:=\gcd(a_n,a_{n_B})` a divisor of the fixed integer `b`, with `g_n>1`, and
  `q^*\mid a_n \iff q^*\mid g_n` for any `q^*\in F''`. Proved in full in Section
  3 from Free Facts and the definition of extended type alone (no dependence on
  any open hypothesis). Gives a clean finite-alphabet recast of any future
  FAH/Cofinite-FAH exception-counting attempt — genuinely new (extends, and is
  independent of, the already-certified Divisor-Chain Well-Definedness Lemma by
  additionally pinning every prime factor of the gcd to `F''` specifically, not
  merely bounding the gcd by `Div(a_{n_A})`).
