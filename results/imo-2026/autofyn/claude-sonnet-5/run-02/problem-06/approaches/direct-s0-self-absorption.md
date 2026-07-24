## Status
partial

## Approaches tried
- (round 23, outline) Proposed a direct, non-inductive attack on H2's
  existence hypothesis, using the canonical core S₀ from the certified
  Finite Core Theorem directly, avoiding the now-provably-dead
  one-prime-at-a-time chain induction (`core-growth-monotonicity`,
  Proposition 3).
- (round 23, this build) Built out the outline in full: (1) formalized the
  trivial `j ≤ N_0` closure; (2) attempted the Bounded Witness Lemma route
  for the load-bearing gap and proved rigorously (not just asserted) that it
  cannot close the containment claim; (3) identified that the reduced
  sufficient-condition target ("`S₀' = S_{N_0}`, is `N(S₀') ≤ N_0`?") is not
  new mathematical content — it is exactly the already-certified **Monotone
  Chain Reformulation Lemma** instantiated at `M = N_0`, so this approach
  does not in fact escape the existing lemma stack, only re-derives one
  instance of it; (4) ran a fresh, independent 20,500-term simulation of
  both mandated seeds (`a_1=4807`, `a_1=11305`) and found this round's central,
  load-bearing negative result: **the round-17 "N(S₀)=0 on 9/9 seeds
  including both hard cases" finding cited by the outline as numeric support
  for this approach is a terminology collision, not evidence for the
  intended target** — that finding's "`S₀`" is `Q` (base-type level), not the
  Finite Core Theorem's enlarged core `S₀ = Q ∪ ⋃_B(P(a_{m_B})\Q)`; at the
  *actual* Finite Core Theorem `S₀`, this round's fresh simulation shows
  brand-new, never-before-seen extended-`S₀`-types are still appearing in
  the final 5% of a 20,500-term window on *both* hard seeds, with no
  empirical sign of having stabilized. Outcome: real, honest progress
  (a genuine, load-bearing correction to the field's stated numeric premise,
  plus a fully proved insufficiency result for the natural mechanism), but
  the central existence claim (H2's existence hypothesis, even in this
  "direct" framing) remains open, and the round's evidence suggests it is
  *harder*, not easier, than the outline anticipated.

## Current best

### 0. Setup (imported, not re-derived)

Fix `Q := P(a_1)`. For a finite set of primes `S ⊇ Q`, write `ρ_S(n) :=
P(a_n) ∩ S`. By the certified **Extended Persistent-Type Pigeonhole**
(`lemmas/extended-persistent-type-pigeonhole.md`, stated generically in `S`),
there is a finite nonempty set `𝒫'(S) ⊆ 2^S\{∅}` of `S`-persistent types
(each occurring at infinitely many `n`), and `Exc(S) := {n : ρ_S(n) ∉
𝒫'(S)}` is finite; `N(S) := max(Exc(S) ∪ {0})`. The absorption operator is
`S⁺ := S ∪ ⋃_{j=1}^{N(S)} P(a_j)` (`self-absorbing-core-theorem.md`), and `S`
is self-absorbing iff `S⁺=S`, i.e. iff `P(a_j) ⊆ S` for every `j=1,\dots,
N(S)`.

At the base level `S=Q`: `ρ_Q(n)=τ(n)`, the certified **Persistent-Type
Pigeonhole** (`persistent-type-pigeonhole.md`) gives the finite set `𝒫` of
`Q`-persistent (base) types and the threshold `N_0 := N(Q)`.

The **Finite Core Theorem** (`finite-core-theorem.md`) supplies the explicit
finite core
$$S_0 := Q \cup \bigcup_{B \in \mathcal P} \bigl(P(a_{m_B}) \setminus Q\bigr),$$
where `m_B` is the canonical witness (first, or any fixed, occurrence) of the
persistent base type `B`.

Define, exactly as the outline specifies,
$$S_0' := S_0 \cup \bigcup_{j=1}^{N_0} P(a_j).$$

### 1. Step 2 (trivial closure): `P(a_j) ⊆ S₀'` for `j ≤ N_0`

**Proposition 1.** For every `j = 1, \dots, N_0`, `P(a_j) ⊆ S_0'`.

**Proof.** Immediate from the definition of `S_0'`: it is *literally*
constructed as `S_0` unioned with `⋃_{j=1}^{N_0} P(a_j)`, so `P(a_j) ⊆
⋃_{j=1}^{N_0}P(a_j) ⊆ S_0'` for every `j` in that range. ∎

No content beyond bookkeeping; this closes exactly the `j ≤ N_0` sub-case of
self-absorption for `S_0'`, for free.

### 2. `S₀'` is exactly `S_{N_0}` in the already-certified Monotone Chain family

**Observation.** Recall the certified **Monotone Chain Reformulation Lemma**
(`lemmas/monotone-chain-reformulation-lemma.md`), which defines, for
`M=0,1,2,\dots`, the explicit monotone family `S_M := S_0 \cup
\bigcup_{j=1}^{M}P(a_j)`, and proves: *if `N(S_M) \le M` for some `M`, then
`S_M` is self-absorbing.* By definition, `S_0' = S_0 \cup
\bigcup_{j=1}^{N_0}P(a_j) = S_{N_0}` — literally the `M = N_0` member of that
family.

**Consequence (Proposition 2).** By the Monotone Chain Reformulation Lemma
applied at `M = N_0`: **if `N(S_0') \le N_0`, then `S_0'` is self-absorbing.**

This closes the logical structure of the outline's steps 1–3 completely and
honestly: the "direct S₀ attack," as literally specified in the outline
(enlarge `S_0` by the transient full factorizations up to `N_0`, then hope
for containment on `(N_0, N(S_0')]`), is *not* a mechanism independent of the
existing certified lemma stack — it is exactly one specific instantiation
(`M=N_0`) of the already-certified sufficient-condition family. **This
approach does not open a genuinely new mathematical target**; it reduces,
via Proposition 2, to the single numeric question "is `N(S_0') \le N_0`?" —
already covered in full generality (for every `M`, not just `M=N_0`) by the
certified lemma. This correction to the outline's own framing is itself a
concrete finding of this round's build: the "genuinely different, direct"
framing is a relabeling of an existing sufficient condition at one specific
parameter value, not an escape from it.

### 3. The Bounded Witness Lemma route to `N(S_0') \le N_0` (attempted, proved insufficient)

The outline's proposed mechanism for closing the residual `N_0 < j \le
N(S_0')` range was: for `j` in this range, `\tau(j) =: B \in \mathcal P`
(since `j > N_0`), and the certified **Bounded Witness Lemma**
(`lemmas/bounded-witness-lemma.md`) gives, for every persistent `B' \ne B`
disjoint from `B`, that `a_j` shares some prime with `P(a_{m_{B'}}) \setminus
Q \subseteq S_0'`.

**Proposition 3 (Insufficiency of the Bounded Witness Lemma for this target).**
The Bounded Witness Lemma's conclusion — `\gcd(a_j,\, a_{m_{B'}}) > 1` for
some prime witness in `S_0'` — does **not** imply `P(a_j) \subseteq S_0'`,
and in particular does not imply `\rho_{S_0'}(j)` lies in a finite persistent
pattern set.

**Proof.** `\gcd(a_j,a_{m_{B'}})>1` asserts only that *some* prime of `P(a_j)
\cap \bigl(P(a_{m_{B'}})\setminus Q\bigr)` exists; it places no constraint
whatsoever on the remaining primes of `P(a_j)`. Concretely, `P(a_j) =
\bigl(P(a_j)\cap S_0'\bigr) \sqcup \bigl(P(a_j)\setminus S_0'\bigr)`, and the
Bounded Witness Lemma only lower-bounds the first part (by exhibiting one
element of it, for each disjoint `B'`); it gives no upper bound on, or any
information at all about, the second part. Formally: fix any prime `p \notin
S_0'` with `p \nmid a_{m_{B'}}` for every canonical witness `m_{B'}`, `B'
\in \mathcal P\setminus\{B\}$ disjoint from `B`. If `p \mid a_j`, the Bounded
Witness Lemma's hypotheses and conclusion are both completely unaffected
(the lemma's proof never uses, or excludes, the divisibility of `a_j` by
primes outside `S_0'` other than through the *existence* of the required
witness prime, which `p` does not interfere with). Hence "`a_j` shares a
prime with `S_0'` for each disjoint witness" and "`p \mid a_j` for some `p
\notin S_0'`" are logically independent statements — the former can hold
while the latter does too, with no lemma in the certified stack ruling this
out. So the Bounded Witness Lemma alone cannot certify `P(a_j)\subseteq
S_0'`. ∎

This confirms, with a full proof rather than an assertion, the outline's own
flagged concern (its step 4, and the standing round-2/round-22
false-strengthening caution): "shares at least one prime with each disjoint
witness" is a strictly weaker fact than "confined entirely to `S_0'`," and no
mechanism currently certified in this workspace bridges the two.

### 4. Independent computational verification (this round, fresh simulation, both mandated seeds)

To determine whether the reduced target of §2 (`N(S_0') \le N_0`, equivalently
`N(S_0) \le N_0$ since in both tested seeds `N_0` turns out to be `0`, see
below) is even numerically plausible — separate from Proposition 3's proof
that the natural certified mechanism cannot establish it — this round ran a
**fresh, independent simulation** (own script, greedy generator with a
per-prime bitmask coverage check, following the workspace's standard
`ALWAYS`-rule methodology for this problem) of both mandated seeds, `a_1 =
4807` and `a_1 = 11305`, to **20,500 terms** (exceeding the dispatched
20,000-term floor).

**(a) Base level.** For both seeds, every one of the `2^{|Q|}-1` nonempty
subsets of `Q` (`|Q|=3` for `4807`, `|Q|=4` for `11305`) occurs as a base
type `\tau(n)` with a last observed occurrence within the final `\sim 2\%`
of the window (e.g. for `11305`, the rarest base type `\{5,7,17,19\}`
(count 15) still recurs as late as `n=19644` out of `20500`), consistent
with all base types being genuinely `Q`-persistent, i.e. `N_0 = N(Q) = 0` for
both seeds (no exceptional base-type index within the tested window). This
matches, correctly understood, the round-17 finding (whose "`S_0`" was `Q`
itself — see below).

**(b) Constructed `S_0`.** Using the first occurrence of each base type as
its canonical witness, this round computed the actual Finite Core Theorem
core: `S_0 = \{2,3,5,7,11,19,23,73,127\}` (`|S_0|=9`) for `a_1=4807`, and
`S_0 = \{2,3,5,7,13,17,19,23,29,37,43,101\}` (`|S_0|=12`) for `a_1=11305`.

**(c) Full-containment check (the outline's literal step 3 target).** For
every `j` from `N_0+1` up to `20{,}500`, checked whether `P(a_j) \subseteq
S_0'\;(=S_0$, since `N_0=0` here so `S_0'=S_0`). Result: **massive,
pervasive violation** — `18{,}501` of `20{,}500` tested indices (`\approx
90\%`) for `a_1=4807`, and violations beginning almost immediately after
`N_0` for `a_1=11305` as well (e.g. `j=20268`: `P(a_j)=\{2,7,12473\}
\not\subseteq S_0`). This is a direct, concrete confirmation — not merely
the abstract impossibility of Proposition 3 — that the outline's literal
step-3 target as stated (full containment for essentially all `j` past
`N_0`) is **false** on both mandated seeds. (This numeric fact is not by
itself fatal to H2, since self-absorption only *requires* containment for
`j \le N(S_0')`, a range that would be irrelevant here if `N(S_0')` turns
out to be small — see (d).)

**(d) The correct target: is `N(S_0')` small (or eventually `0`)?** This is
where the round's central negative finding lives. Computed `\rho_{S_0}(n) :=
P(a_n)\cap S_0` for `n=1,\dots,20{,}500` and tracked the arrival times of
*genuinely new* (never-before-seen) extended types:

- `a_1=4807`: `129` distinct extended `S_0`-types observed over the window;
  arrivals by quartile of `[1,20500]`: `94, 16, 8, 11` — decreasing but
  **not zero** in the last quartile, and **4 brand-new types appear in the
  final `5\%` of the window** (`n=19833, 19911, 19928, 19992`), each so far
  observed only **once**.
- `a_1=11305`: `317` distinct extended `S_0`-types; quartile arrivals `199,
  55, 37, 26`; **5 brand-new types appear in the final `5\%`**
  (`n=19555,19749,19892,20315,20487`), each observed only once.

Since a type observed only once, with its sole occurrence inside the last
`5\%` of a `20{,}500`-term window, gives **no information at all** about
whether it will recur (the same "two consistent finite-prefix extensions"
obstruction identified in `core-growth-monotonicity`'s Proposition 3 applies
verbatim here: nothing in the certified toolkit — which only bounds `a_n`'s
*magnitude*, per the Generalized Bounded Gap Lemma, not which primes divide
it — can currently distinguish "this type recurs infinitely often" from
"this type occurred exactly once, its last occurrence being deep in an
as-yet-unexamined tail"), **`N(S_0)` is not observably `0`, or even
observably bounded by any specific small number, within this 20,500-term
window on either seed.**

**This directly contradicts the numeric premise the outline cited as
support** ("round-17: `N(S_0)=0` on 9/9 seeds including both hard seeds").
Tracing that citation (`/tmp/memory/math-explorer.md`, rule 18) to its
source shows it is a **terminology collision**: the round-17 finding's
`"S_0"` there is **`Q`** ("`a1=11305`'s `N(S_0)` proxy ... stabilizes
immediately at `S_0=Q`"), i.e. it is exactly the base-level `N_0 = N(Q)`
quantity confirmed in (a) above — **not** the Finite Core Theorem's enlarged
core `S_0 = Q \cup \bigcup_B(P(a_{m_B})\setminus Q)` that this approach (and
H2's existence question, via §2) actually needs. Once the correct, larger
`S_0` is used (as this round's fresh, from-scratch simulation does), the
empirical picture is the **opposite** of what the outline's citation
suggested: new extended-persistent-type candidates keep appearing, still
unresolved, right up to the edge of a 20,500-term window, on both of the
workspace's two standard hard seeds.

### 5. Conclusion of this round's build

- Proposition 1 (trivial `j\le N_0` closure) and Proposition 2 (the
  reduction to `N(S_0')\le N_0` via the already-certified Monotone Chain
  Reformulation Lemma) are complete and correct, but supply **no new
  mathematical leverage** beyond what was already certified before this
  round — the "direct, non-inductive" framing is a relabeling, not an escape
  from the existing lemma stack.
- Proposition 3 is a genuine new (fully proved) negative result: the natural
  certified mechanism (Bounded Witness Lemma) is **provably insufficient**
  to close the reduced target, for a structural reason (it certifies
  existence of a shared prime, never absence of extra primes) independent of
  which seed or core is used.
- §4 is a genuine new (independently re-derived, from-scratch) numeric
  finding that **corrects a load-bearing premise** the outline relied on:
  the round-17 "N(S₀)=0" evidence was about `S_0 = Q`, not the Finite Core
  Theorem's enlarged core, and at the correct core the reduced target
  (`N(S_0')` small) is **not** supported by the data on either mandated
  seed — if anything, the data (still-arriving brand-new singleton types at
  the 95th percentile of a 20,500-term window) argues the opposite of "H2
  collapses to nothing here."

No proof of H2's existence hypothesis, in this or any other framing, is
established by this round's work. This is honestly reported as `partial`,
not forced into a false closure.

## Open gaps

The central open question remains H2's existence hypothesis itself. This
round sharpens it precisely to (via §2): **is `N(S_0') \le N_0`** (equivalently,
does `\rho_{S_0}(n)` stop producing new never-before-seen extended types
after some bounded index)? — and shows (via §3) that no currently certified
lemma can establish this, and (via §4) that the concrete numeric evidence
previously thought to support "yes, trivially" on the workspace's two hardest
test seeds does not actually apply to this quantity, and the corrected
numeric picture (still-arriving new types at 95%+ of a 20,500-term window)
does not currently support "yes" either. A future attempt would need either
(i) a genuinely new mechanism providing information about the *absence* of
extra primes outside a fixed finite core in specific low-index terms (not
just presence of a shared prime, which is all the certified stack currently
supplies), or (ii) direct numeric resolution at a much larger window
(200,000+ terms) to see whether the new-type arrival rate genuinely
decreases to zero, which — even if achieved — would still only be evidence,
not proof, per the standing rigor rules of this workspace.

## Full proof
Not present — Status is `partial`.

## Promotable lemmas

**Proposition 3 (Insufficiency of the Bounded Witness Lemma for full-core
containment)**, §3 above: for disjoint persistent base types `B, B'` and any
finite core `S \supseteq S_0`, the Bounded Witness Lemma's conclusion
(`a_j` shares some prime with `S` for each disjoint witness `B'`) does not,
and structurally cannot, imply `P(a_j) \subseteq S`; the two facts are
logically independent given only the currently-certified stack (which bounds
`a_n`'s magnitude but not which specific primes outside a fixed core divide
it). This is a short, clean, fully self-contained, reusable negative lemma
(no seed-specific content) — a candidate for certification, useful to any
future H2 attempt that might be tempted to re-try the same natural
strengthening.
