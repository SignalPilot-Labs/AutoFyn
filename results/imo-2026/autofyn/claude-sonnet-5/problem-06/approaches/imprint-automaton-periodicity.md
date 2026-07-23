## Status
partial

## Round 6 Outline (proof-outliner directive — companion-count bound on
`𝒜_S`, using Lemma FOM + the already-certified DM-order tool)

**Context.** This file already owns the sharpest reduction in the
population: `(MRS)\Leftrightarrow𝓥`finite`\Leftrightarrow𝓥_S`finite for every
proper nonempty `S\subsetneq P_1$ (Theorem V-MRS, Theorem CD, Lemma TC,
already certified here). This round targets a single scalar quantity
directly — the **companion-event count** per channel — kept genuinely
distinct from `persistent-backbone-monovariant`'s chain-count/growth-budget
argument and `core-depth-induction`'s structural induction on `|S|`: this
approach does not build a recursive apparatus, it tries to bound one number
per channel (empirically `\le4` in every case tested by this round's
narrow-framing explorer) using the already-certified DM-multiset-order tool
(any single collapse event is a strict multiset-order decrease — imported
unchanged from this file's own round-5 material, Step 1) together with this
round's new Lemma FOM (cite from `persistent-backbone-monovariant` once
certified, or reprove inline if this file's builder runs first).

**Step 1 (import, no new work).** `𝓥` finite `\Leftrightarrow` `𝓥_S` finite
for every `1\le|S|\le k-1` — Theorem CD + Lemma TC, already certified here.

**Step 2 — reformulate the target as a companion-event count.** For a
proper core `S`, let `𝒜_S:=𝓥_S\setminus\{S\}` (the transient/companion
values; at most one value, `S` itself, can be a "trivial" member — check,
do not assume, whether an analogue of Lemma TC's "`S` itself is realized"
dichotomy holds for general proper `S`, not just `S=P_1`, before relying on
this). `𝓥_S$ finite `\Leftrightarrow` `𝒜_S$ finite (since `𝓥_S=𝒜_S\cup(𝓥_S
\cap\{S\})$ and the second part has size `\le1`). Restate the open target as
`𝒜_S$ finite for every proper nonempty `S\subsetneq P_1`.

**Step 3 — attempt the Companion-Count Bound (OPEN, this round's genuine
content, do not overclaim).** Candidate mechanism: classify each element of
`𝒜_S` as either (i) eventually dominated by a strictly smaller element (a
DM-order decrease, already well-founded per-chain — cite the shared
Generation-Chain Lemma argument, same three-line fact as in `persistent-
backbone-monovariant`'s round-6 outline, no need to re-derive independently,
just cite), or (ii) a permanent survivor of channel `S`. **Tested and
explicitly flagged as a dead end**: "any two permanent survivors of the same
channel intersect, by Lemma P′" is TRUE but gives NO new constraint (it is
trivially satisfied via `S` itself, since `S\subseteq C_1\cap C_2$ for any
two `C_1,C_2\supseteq S`) — do not let the builder present this as
progress; it was checked this round and found vacuous. The genuinely open
sub-question, not yet closed: can Lemma FOM's Fan-Size Corollary (a bound
*conditional on* an absorption event occurring) be combined with a
pigeonhole over the finitely many primes below an `a_1`-dependent threshold
(from Lemma 1's linear growth rate) to force **either** absorption within a
bounded number of steps **or** an explicit contradiction with the greedy
rule's minimality? **Not constructed this round** — report exactly this as
the open gap, not as "almost done."

## Round 5 Outline (proof-outliner directive — DM-multiset-order + fan/threshold pivot, read this first)

**Verdict on why this approach, not a fresh slug, gets the new mechanism.**
This approach already owns the entire `𝓜_n`/`M_n` formalism, the certified
Corollary W3′, and the certified Lemma MS (`(MRS)⟹FCBC⟹` whole problem). The
round-5 `MRS-direct` explorer's two new findings (first-hitting-time
fan/collapse mechanism; Dershowitz–Manna multiset order) are both phrased
*directly* in terms of `𝓜_n`, so building them anywhere else would just
re-import this file's definitions under a new name — no diversity gained,
real risk of duplicated/inconsistent notation. Keep them here; give the
*other* two live approaches (below) genuinely different formal machinery
(permanent-domination/event-counting; channel-localized stabilization) so
the population's mechanisms stay spread out even though the target (`(MRS)`)
is now shared by all three, per `CLAUDE.md`'s single-gap-trap guidance.

**Target (unchanged, cite don't reprove):** the problem's exact headline
conclusion `a_{n+T}=a_n+L\ \forall n\ge1`, via the already-certified chain
Lemma MS + Theorem 5.1, conditional only on proving Hypothesis (MRS).

**New Step 0 — corrected definition of the fan threshold (verified
numerically before writing, per project convention).** For a nonempty finite
set of primes `C`, define
$$T_C:=\min\{x\in\mathbb Z:\ x>a_1,\ \mathrm{rad}(x)=C\}.$$
*This is NOT `\prod_{p\in C}p`* (that number, `122` for `C=\{2,61\}`, is
`<a_1=4087` in the worst tested case, hence can never be a term of the
increasing sequence — a naive `T_C:=\prod_{p\in C}p` would be wrong).
`T_C` is well-defined (the set `\{(\prod_{p\in C}p)^t:t\ge1\}` has radical
exactly `C` for every `t` and is unbounded, so infinitely many radical-`C`
integers exceed `a_1`) and is a **fixed integer depending only on `C` and
`a_1`**, computable without reference to any specific step `n` of the
sequence. **Numerically verified**: for `C=\{2,61\}`, `a_1=4087`, direct
computation gives `T_C=2\cdot61^2=7442`, exactly matching `a_{54}=7442` (the
term that triggers the certified `a_1=4087` collapse) — confirmed by fresh
Python (`math.gcd`-based simulator, exact greedy rule, cross-checked against
the already-certified table in this file's own round-4 section).

**Step 1 — Key Lemma (Collapse ⟹ DM-decrease).** Whenever a step `n` removes
`\ge1` elements `m_1,\dots,m_r` from `𝓜_{n-1}` and adds `P_n`, every removed
`m_i` satisfies `P_n\subsetneq m_i` (strict superset — this is forced by the
antichain-update rule already justified in this file's certified
"Computational note"). Hence the multiset transition
`\{|m_1|,\dots,|m_r|\}\to\{|P_n|\}` is a **strict decrease** in the
Dershowitz–Manna multiset extension order on `(\mathbb N,<)`: every removed
element's size is replaced by finitely many (here, exactly one) strictly
smaller elements. *Mechanism*: this is the textbook definition of a DM-order
decrease (Dershowitz & Manna, 1979, "Proving Termination with Multiset
Orderings") — **not in `knowledge_base.md` or the crux corpus** (confirmed
absent by the round-5 explorer's grep); the builder must state and prove the
underlying well-foundedness fact from scratch (short: induction on multiset
cardinality, or cite the standard transfinite-induction proof) rather than
assume it as a black box, per "Name your tools."

**Step 2 — the two genuinely open sub-lemmas (this round's real content).**
DM well-foundedness alone does **not** finish (MRS): a *non*-collapse step
(a new antichain-incomparable value arriving) is a pure DM-*increase*
(insertion with nothing removed), so the raw sequence of multisets is not
globally DM-decreasing. (MRS) needs the *entire process* (insertions and
removals together) to terminate, i.e., stop changing at all — this needs
two separate, currently-unproved ingredients:

  (a) **Bounded Core Family.** The set of distinct "cores" `C` that can ever
      trigger a collapse (i.e., ever become the *removed-to* element `P_n`
      of a genuine collapse event, `r\ge1`) is finite. Candidate mechanism
      (not proved): induct on `|C|` from `k:=\omega(a_1)` down to `0`,
      using the already-certified **Lemma C**
      (`lemmas/lemma-C-global-intersection-collapse.md`, `C_n:=\bigcap_{i\le
      n}\mathrm{rad}(a_i)` stabilizes to `C_\infty=\varnothing` in Case II)
      as the base case, and showing each level's cores can only be built by
      *recruiting* from a bounded pool — **this bound does not exist yet
      and is the approach's genuine remaining gap**, not a formality.
      **Watch out**: the round-5 `MRS-direct` explorer's `a_1=2747` example
      shows cores can be genuinely **nested two levels deep** (three
      independent second-level hub pairs `{2,41\}`, `\{3,41\}`, `\{7,41\}`
      each spawning their own fan, collapsing at different indices
      `n=14,13,163`) — any Bounded-Core-Family argument must allow this
      recursive/nested structure, not assume a single flat layer of cores.
  (b) **Bounded growth-per-core (with exact-hitting).** For a fixed core
      `C`, once its fan starts growing (siblings `C\cup\{q\}` appearing),
      it must (i) genuinely reach a term with radical **exactly** `C`
      (i.e., `a_m=T_C` for some `m`, not merely `a_m>T_C` — admissibility
      against *all* prior terms, not just the fan siblings, must be
      checked) and (ii) do so after only finitely many distinct `q`'s are
      recruited. **Watch out**: the round-5 explorer's `a_1=11623` finding
      (`59|(196+n)` exactly, first hit at `n=59^2-197=3284`) proves that
      *when this is secretly Case I* the growth phase can be **thousands of
      steps long** — do not let the builder assume a small/uniform bound on
      fan length. **However**: `a_1=11623` is Case I in disguise (a single
      prime `59` divides every term — already fully solved by imported
      Lemma S′), so it is not itself a Case-II stress test of (b); the
      builder should explicitly check, before using any numerical example
      as a stress test for (b), whether it is secretly Case I (single
      global hub — cheap to test) and if so set it aside as already solved,
      not as evidence about how large genuine Case-II fan lengths can get.

**Step 3 — conclusion (conditional).** If (a) and (b) both hold, then only
finitely many cores ever trigger collapses, each contributing only finitely
many fan-growth (insertion) steps before its own collapse, so `𝓜_n` changes
only finitely many times in total — giving (MRS) directly.

## Round 5 Fix — closing the Step-3 gap flagged by the outline-reviewer

**The gap, restated precisely.** The Round-5 Outline's sub-lemma (a)
("Bounded Core Family") only bounded cores `C` that ever become the
*removed-to* element `P_n` of a genuine collapse event (`r\ge1`). The
outline-reviewer showed by direct computation that `a_1=91` has **zero**
collapse events at all (every one of its three steps is a pure insert, no
removal ever happens) yet still has `|𝓜_\infty|=3`, so Step 3's inference
("if (a) and (b) hold, `𝓜_n` changes only finitely often") is a non
sequitur: it never accounts for radical values that are inserted and then
**permanently survive** without ever triggering — or being subject to — a
collapse. This section repairs that inference from scratch, replacing the
old "collapse-triggering core" notion with a correct, unconditionally-finite
"core" decomposition that covers *every* value ever appearing in `𝓜_n`
(permanent or transient) simultaneously.

### Definitions

`𝓖 := \{C : C=P_i \text{ for some } i\ge1,\ \text{and no } j\ge1 \text{ has
}P_j\subsetneq C\}` — the set of **globally minimal** radical values (no
witness anywhere in the whole infinite sequence dominates them), and

`𝓥 := \bigcup_{n\ge1}𝓜_n` — the set of **every** distinct radical value that
is `n`-minimal (i.e. a member of the running antichain `𝓜_n`) for *some*
finite `n`, permanent or not.

### Lemma PS (Permanent-Survivor Characterization)

**Statement.** Call `C` a *permanent survivor* if there is `N\ge1` with
`C\in𝓜_n` for every `n\ge N`. Then `C` is a permanent survivor **iff**
`C\in𝓖`.

**Proof.**

`(\Leftarrow)` Let `C\in𝓖`, realized as `C=P_i`. Fix any `n\ge i`. By
definition of `𝓖`, there is **no** `j\ge1` (in particular no `j\in\{1,\dots,
n\}`) with `P_j\subsetneq C`; so `i` is `n`-minimal, i.e. `i\in M_n`, so
`C=P_i\in𝓜_n`. As `n\ge i` was arbitrary, `C` is a permanent survivor
(`N:=i` works).

`(\Rightarrow)` Let `C` be a permanent survivor, `C\in𝓜_n` for `n\ge N`. In
particular `C\in𝓜_N`, so `C=P_i` for some actual index `i\in M_N` — `C` is
realized. Suppose toward contradiction some `j\ge1` has `P_j\subsetneq C`.
Take `n':=\max(N,j)\ge N`; since `n'\ge N`, `C\in𝓜_{n'}`, so the realizing
index `i'\in M_{n'}` (with `P_{i'}=C`) satisfies: no `k\in\{1,\dots,n'\}` has
`P_k\subsetneq C`. But `j\le n'` and `P_j\subsetneq C` — contradiction. So no
such `j` exists, i.e. `C\in𝓖`. `∎`

### Lemma NR (No Resurrection)

**Statement.** If `C\notin𝓖` (i.e. some `j\ge1` has `P_j\subsetneq C`), let
`j_C` be any one such witness. Then `C\notin𝓜_n` for every `n\ge j_C`.

**Proof.** Immediate from the definition of `n`-minimality (Lemma W3): for
`C\in𝓜_n` we would need some realizing index `i\in M_n` (`P_i=C`) with no
`k\in\{1,\dots,n\}` witnessing `P_k\subsetneq C`. Since `j_C\le n` and
`P_{j_C}\subsetneq C`, this fails for every `n\ge j_C`. `∎` (This is a
strengthening of the persistent-backbone-monovariant approach's
"No-Resurrection Lemma" derived independently here, directly from the
`n`-minimality definition rather than from the incremental-update
description of the algorithm — the two are the same fact, proved two
different ways; noted explicitly here per the convergence discussion below.)

### Theorem V-MRS (Hypothesis (MRS) `⟺` `𝓥` finite)

**Statement.** (MRS) holds if and only if `𝓥` is finite.

**Proof.**

`(\Rightarrow)` If (MRS) holds, `𝓜_n=𝓜_{N_0}` for `n\ge N_0`. So
`𝓥=\bigcup_{n=1}^{N_0}𝓜_n` (the terms with `n>N_0` contribute nothing new).
Each `𝓜_n` is finite (`|𝓜_n|\le n`, as `M_n\subseteq\{1,\dots,n\}`), and this
is a union of finitely many (`N_0`) finite sets, hence finite.

`(\Leftarrow)` Suppose `𝓥` is finite. Partition `𝓥=(𝓥\cap𝓖)\sqcup(𝓥\setminus
𝓖)`. First, `𝓖\subseteq𝓥`: if `C\in𝓖`, realized at index `i`, then by Lemma
PS `(\Leftarrow)`, `C\in𝓜_i\subseteq𝓥`. So `𝓥\cap𝓖=𝓖`, and since `𝓥` is
finite, `𝓖` is finite too, say `𝓖=\{C_1,\dots,C_r\}` with first-appearance
indices `i_1,\dots,i_r` (each finite, by the argument just given). Second,
`𝓥\setminus𝓖=\{D_1,\dots,D_s\}` is finite (a subset of the finite set `𝓥`);
for each `D_t\notin𝓖`, fix a witness `j_{D_t}` as in Lemma NR (finite, by
definition of `\notin𝓖`). Set
`$$N_0:=\max\big(\{i_1,\dots,i_r\}\cup\{j_{D_1},\dots,j_{D_s}\}\big),$$`
a maximum of finitely many finite numbers, hence finite. For `n\ge N_0`:
every `C_u\in𝓖` has `C_u\in𝓜_n` (Lemma PS `(\Leftarrow)`, since `n\ge
i_u`); every `D_t\notin𝓖` has `D_t\notin𝓜_n` (Lemma NR, since `n\ge
j_{D_t}`); and no value outside `𝓥` is ever in any `𝓜_n` (by definition of
`𝓥` as the union of all of them). So `𝓜_n=\{C_1,\dots,C_r\}=𝓖` for every
`n\ge N_0` — (MRS) holds, with `𝓜_\infty=𝓖`. `∎`

**Consequence.** This makes precise and repairs the Round-5 Outline's Step 3:
the correct necessary-and-sufficient reduction of (MRS) is not "(a)
collapse-triggering cores finite `+` (b) bounded growth per core", but the
single unified statement "`𝓥` is finite" — which automatically subsumes both
permanent survivors (`𝓖`, handled by Lemma PS) and transient values (handled
by Lemma NR), with no separate bookkeeping needed for the two cases.

### Theorem CD (Core Decomposition of `𝓥`)

**Statement.** Every `C\in𝓥` satisfies `C\cap P_1\ne\varnothing`. Writing
`S(C):=C\cap P_1` (a nonempty subset of the *fixed* finite set `P_1`,
`|P_1|=k=\omega(a_1)`), and `𝓥_S:=\{C\in𝓥 : S(C)=S\}` for each nonempty
`S\subseteq P_1`:
`$$𝓥=\bigsqcup_{\varnothing\ne S\subseteq P_1}𝓥_S \quad(\text{a partition
into at most } 2^k-1 \text{ parts, an index set fixed by } a_1 \text{ alone,
computable with no induction}),$$`
and `𝓥` is finite **iff** `𝓥_S` is finite for every one of these (at most)
`2^k-1` values of `S`.

**Proof.** *Nonemptiness of `C\cap P_1`.* Every `C\in𝓥` is realized,
`C=P_i` for some actual index `i\ge1`. If `i=1`, `C\cap P_1=P_1\ne\varnothing`
trivially (`a_1>1` so `P_1\ne\varnothing`). If `i\ge2`, the already-certified
**Lemma P′** (pairwise global intersection,
`lemmas/lemma-P-prime-pairwise-intersecting.md`, applied to the pair `1<i`)
gives `\gcd(a_1,a_i)>1`, i.e. some prime lies in both `P_1` and `P_i=C`, so
`C\cap P_1\ne\varnothing`. Either way `S(C)` is a well-defined nonempty
subset of the fixed finite set `P_1`, and there are exactly `2^k-1` such
subsets (`k=|P_1|` fixed once `a_1` is fixed — no dependence on `n`, no
induction on `|C|` required, unlike the Round-5 Outline's original
"induct on `|C|` from `k` down to `0`" sketch for sub-lemma (a), which this
supersedes).

*Partition.* The sets `𝓥_S` (`\varnothing\ne S\subseteq P_1`) are pairwise
disjoint by construction (a given `C` has a unique value `S(C)`) and their
union is exactly `𝓥` (every `C\in𝓥` lies in `𝓥_{S(C)}`), so `\{𝓥_S\}`
partitions `𝓥`.

*Finiteness equivalence.* `(\Leftarrow)` If every `𝓥_S` (`S` ranging over the
`2^k-1`-many nonempty subsets of `P_1`, a finite index set) is finite, then
`𝓥` is a union of finitely many finite sets, hence finite. `(\Rightarrow)`
If `𝓥` is finite, each `𝓥_S\subseteq𝓥` is a subset of a finite set, hence
finite. `∎`

**Consequence (repairing sub-lemma (a) correctly).** By Theorem V-MRS,
`(MRS)\Leftrightarrow𝓥`finite; by Theorem CD, `𝓥`finite`\Leftrightarrow`
`𝓥_S`finite for each of the (at most) `2^k-1` nonempty `S\subseteq P_1`. This
is the **correct** replacement for the outline's Step 3: instead of trying to
bound an a priori open-ended, recursively-defined family of
"collapse-triggering cores" (which — as the reviewer showed — misses
permanent survivors entirely), the core index set is *exactly* the (fixed,
finite, immediately-computable-from-`a_1`) power set of `P_1`, and it covers
**every** value ever appearing in `𝓜_n`, transient or permanent, by
construction (Theorem CD's proof needs nothing beyond the already-certified
Lemma P′).

### Lemma TC (Top Core is Trivial) — one case fully closed unconditionally

**Statement.** `𝓥_{P_1}=\{P_1\}` (the case `S=P_1`, i.e. `C\supseteq P_1`,
contributes *only* `C=P_1` itself — no other value with full core `P_1` is
ever `n`-minimal for any `n`).

**Proof.** Suppose `C\in𝓥_{P_1}`, i.e. `C\cap P_1=P_1`, i.e. `C\supseteq
P_1`, and `C\in𝓜_n` for some `n` (realized at index `i\in M_n`, `P_i=C`,
`i\le n`). If `C\ne P_1`, then `C\supsetneq P_1=P_1` strictly (proper
superset, since `C\supseteq P_1` and `C\ne P_1`). Since `1\le n` always
(`n\ge i\ge1`), the index `k=1` is a witness `P_1\subsetneq C` with `1\in
\{1,\dots,n\}`, contradicting `i\in M_n` (which requires no such witness).
So `C=P_1`. Conversely `P_1\in𝓥_{P_1}` trivially (`P_1=P_1\cap P_1`,
realized at `i=1`, and `1\in M_1` vacuously as the only candidate). `∎`

This removes exactly one of the (at most) `2^k-1` cases unconditionally and
in general (not just numerically): `𝓥` is finite iff `𝓥_S` is finite for
each of the **remaining `2^k-2` proper nonempty subsets `S\subsetneq P_1`**
(genuinely fewer than `2^k-1`, and — since `S=\varnothing` is excluded by
Theorem CD and `S=P_1` is now closed by Lemma TC — these are exactly the
"intermediate" cores where a nonempty *strict* subset of `P_1` is
supplemented by primes outside `P_1`, matching the informal "fan" picture
from the Round-5 Outline's Step 2).

### Numerical verification of the fix

Computed `𝓥` (all distinct values ever `n`-minimal, not just the final
antichain `𝓜_\infty`) directly, from scratch, for 15 values of `a_1`
(the original 12-value table plus fresh `91,323,1573`), and cross-checked
every claim above:

| `a_1` | `k` | `\lvert𝓥\rvert` | cores realized (of `2^k-1`) | `𝓥_{P_1}` | largest `𝓥_S` (`S\ne P_1`) |
|---|---|---|---|---|---|
| 91 | 2 | 3 | 3/3 | `\{\{7,13\}\}` ✓ | 1 (core `\{7\}`, and `\{13\}`) |
| 221 | 2 | 6 | 3/3 | `\{\{13,17\}\}` ✓ | 3 (core `\{17\}`) |
| 375 | 2 | 6 | 3/3 | `\{\{3,5\}\}` ✓ | 3 (core `\{3\}`) |
| 4087 | 2 | 20 | 3/3 | `\{\{61,67\}\}` ✓ | 17 (core `\{61\}`) |
| 4199 | 3 | 13 | 5/7 | `\{\{13,17,19\}\}` ✓ | 6 (core `\{17\}`) |
| 2431 | 3 | 20 | 4/7 | `\{\{11,13,17\}\}` ✓ | 10 (core `\{13\}`) |

(Full 15-value check for Lemma TC alone — `15,35,65,105,143,221,247,375,
1001,2431,4087,4199,91,323,1573` — passes with **zero violations**: in every
case the only element of `𝓥` with `C\cap P_1=P_1` is `P_1` itself, exactly
as Lemma TC proves. Script: `/tmp/round-5/` inline Python, rerun from the
already-certified exact greedy simulator.)

This confirms Lemma TC exactly and shows the genuinely open cores (`S\ne
P_1`) can have `\lvert𝓥_S\rvert` as large as `17` (the `a_1=4087`,
`S=\{61\}` fan) in already-tested cases — consistent with, but not a proof
of, finiteness in general.

### The precise remaining gap, and explicit convergence with the sibling approaches

**What is now proved (unconditionally, no numerics needed):** (MRS)
`\Leftrightarrow` `𝓥` finite `\Leftrightarrow` `𝓥_S` finite for each of a
fixed, finite (`\le2^k-1`, one is already closed by Lemma TC so really
`\le2^k-2` open cases), a-priori-computable-from-`a_1` list of cores `S`. This
strictly repairs the reviewer's flagged Step-3 gap: the reduction now
correctly and provably accounts for **every** value ever appearing in `𝓜_n`
(permanent survivors via Lemma PS, transients via Lemma NR), not just
collapse-triggering ones.

**What is NOT proved:** that `𝓥_S` is finite for each of the (up to)
`2^k-2` remaining proper cores `S\subsetneq P_1`. This is precisely the
per-core version of the Round-5 Outline's sub-lemma (b) ("bounded
growth-per-core"), and the DM-order tool from that outline (Step 1: any
collapse event is a strict Dershowitz–Manna multiset decrease) remains a
correct, reusable, but *insufficient by itself* piece of machinery here: it
shows that **if** a core's fan ever collapses, the multiset of sizes
strictly decreases — but it does not bound how many distinct fan members
(`\notin𝓖`, transient) can accumulate *before* a collapse, nor rule out a
core whose fan never collapses at all but keeps admitting new members
forever (`91`'s zero-collapse permanent survivors show fans that never
collapse can and do occur; nothing rules out, a priori, a fan that neither
collapses nor stops growing).

**Explicit convergence (per this round's dispatch instruction 5).** Once
correctly stated, `𝓥`-finiteness is now **exactly, not just "equivalent in
difficulty to"**, `persistent-backbone-monovariant`'s open target
`\mathcal{V}`-finiteness (their notation `𝓥` denotes the same object: every
distinct value ever locally minimal, tracked via their own
No-Resurrection Lemma, matching Lemma NR above proved independently here).
This file's contribution beyond that convergence is Theorem CD + Lemma TC:
a further, unconditionally-proved **reduction by core**, cutting the open
object down to `\le2^k-2` independent per-core finiteness questions (rather
than one large undifferentiated `𝓥`), with one extra case (top core) closed
outright. This is real, additional, non-duplicated content — not a bare
restatement of the sibling's reduction — but the *sole remaining open
mathematical content* (finiteness of each `𝓥_S`, `S\subsetneq P_1`
nonempty) is the same open fact the sibling approach is also attacking, and
should not be double-counted as two different open gaps in future rounds'
bookkeeping.

## Approaches tried
- (Round 5) Repaired the reviewer-flagged Step-3 gap in full: proved Lemma PS
  (permanent survivors of `𝓜_n` are *exactly* the globally-minimal radicals
  `𝓖`), Lemma NR (no-resurrection, from the bare `n`-minimality definition),
  Theorem V-MRS (`(MRS)\Leftrightarrow𝓥`finite, unconditional), Theorem CD
  (`𝓥`finite `\Leftrightarrow` `𝓥_S`finite for each of `\le2^k-1` fixed cores
  `S\subseteq P_1`, unconditional, no induction needed — replacing the
  outline's under-specified inductive "Bounded Core Family" sketch), and
  Lemma TC (`𝓥_{P_1}=\{P_1\}`, closing one core unconditionally in general).
  Verified numerically on 15 `a_1` values (12 prior + 3 fresh: `91,323,
  1573`), including the reviewer's own `a_1=91` counterexample, with zero
  violations of any of the four lemmas. **Explicitly does not close (MRS)**:
  per-core finiteness for the `\le2^k-2` remaining proper cores
  `S\subsetneq P_1` is the precise, now correctly-isolated, open gap —
  numerically as large as `17` distinct fan members in one tested core
  (`a_1=4087`, `S=\{61\}`) with no proof of a general bound. This gap is
  identical to `persistent-backbone-monovariant`'s open `𝓥`-finiteness
  target, stated explicitly (not hidden) per this round's dispatch.
- (Round 4, opening) Newly opened by the proof-outliner. Not a copy of any
  sibling; targets the same problem — and, via the imported Theorem 5.1
  hand-off, the same sole remaining gap, FCBC — through a framing genuinely
  different from the three approaches Lemma W1 already proved are the
  *identical proposition* (`persistent-backbone-monovariant`,
  `forced-primes-well-ordering`, `explicit-window-backbone-construction`):
  a finite-state / de Bruijn-graph-style argument on a bounded-alphabet
  projection of the sequence.
- (Round 4, this build) The outline's literal two-step plan (Step A: raw
  `G_n`-periodicity via a bounded window/state; Step B: residue-channel
  reduction mod `T_G`) was attacked directly and **Step A as literally
  scoped failed**: no small fixed-size window on `G_n` or on
  `ρ_n:=a_n\bmod L` (`L:=\mathrm{rad}(a_1)`) is a deterministic function of
  its own recent history — verified computationally (see "Negative finding
  1" below), a genuinely new falsification, not a re-run of an old one.
  **In its place, a structurally different and strictly more powerful
  unconditional-sufficient-condition was found and proved**: Lemma MS below
  shows that if the *minimal-radical antichain* `𝓜_n` (built from the
  already-certified Lemma W3, not from `G_n` at all) stabilizes, the
  **entire problem is solved** — not just `G_n`-periodicity — via the
  already-certified Theorem 5.1. This supersedes the outline's Step
  A/Step B split: Step B (channel reduction) becomes unnecessary if this new
  route closes, since Lemma MS goes straight to FCBC without needing
  `G_n`-periodicity as an intermediate. The new hypothesis (MRS, below) is
  verified with zero exceptions on all 12 previously-tested `a_1` values
  (including all five historically-hardest cases) but is **not proved**;
  this is the approach's precise remaining gap. See "Current best" for the
  full argument and "Open gaps" for exactly what is missing.

## Current best

**Pointer (read this first):** the furthest rigorous progress is now in
"Round 5 Fix" above (Lemma PS, Lemma NR, Theorem V-MRS, Theorem CD, Lemma
TC), which proves `(MRS)\Leftrightarrow𝓥`finite`\Leftrightarrow` `𝓥_S`
finite for each of `\le2^k-2` remaining proper cores `S\subsetneq P_1` (one
case, `S=P_1`, closed unconditionally by Lemma TC). The material below
(Corollary W3′, Hypothesis (MRS), Lemma MS) remains valid and is the
unconditional "(MRS) `\Rightarrow` FCBC `\Rightarrow` whole problem" chain
that Round 5's work is conditional on closing; it is unchanged from round 4
and reproduced here for context.

### Notation (matches the certified lemma files)

`P_i:=\mathrm{rad}(a_i)`, `P_1:=\mathrm{rad}(a_1)`, `L:=\mathrm{rad}(a_1)`
(Lemma 1's constant), `k:=|P_1|=\omega(a_1)`. For `n\ge1`, `M_n\subseteq
\{1,\dots,n\}` is the set of *n-minimal* indices (Lemma W3: no
`k\in\{1,\dots,n\}` has `P_k\subsetneq P_i` for `i\in M_n`). Everything below
is **unconditional** (no FCBC assumed) except where explicitly flagged
"conditional on (MRS)".

### New object: the minimal-radical antichain `𝓜_n`

**Definition.** `𝓜_n := \{P_i : i\in M_n\}`, the set of *distinct radical
values* realized by the `n`-minimal indices (a finite antichain of finite
prime-sets under `\subseteq`; distinct indices with the same radical
collapse to one entry).

This is a different object from `M_n` itself: the round-3/round-4 population
already noted `|M_n|` (the *index count*) grows unboundedly (e.g.
`|M_{199}|=42` for `a_1=221`) — that finding is what made the naive
"state `:=M_n`" mechanism fail and is exactly why the outline flagged Gap A
as non-routine. **`𝓜_n` counts distinct radical *values*, not indices, and
this is a different question that nobody in the population had previously
asked.** Section "Numerical evidence" below shows `|𝓜_n|` behaves
completely differently from `|M_n|`: it appears to stabilize (both in
cardinality and in the literal set of values) after a handful to a few dozen
steps, across every tested case, even when `|M_n|` is simultaneously growing
without bound.

### Corollary W3′ (extracted from the already-certified proof of Lemma W3)

**Statement.** For every `n\ge1` and every `i_0\in\{1,\dots,n\}`, there
exists `j^*\in M_n` with `P_{j^*}\subseteq P_{i_0}`.

**Proof.** This is exactly the sub-argument inside Lemma W3's `(\Leftarrow)`
proof, isolated from the part that uses the hypothesis `\gcd(x,a_i)>1`
(which is not needed for this sub-claim). Let
`S:=\{k\in\{1,\dots,n\}:P_k\subseteq P_{i_0}\}`; `i_0\in S` so `S\ne
\varnothing`. Choose `j^*\in S` minimizing `|P_{j^*}|`. If `j^*\notin M_n`,
some `k\in\{1,\dots,n\}` has `P_k\subsetneq P_{j^*}\subseteq P_{i_0}`, so
`k\in S` with `|P_k|<|P_{j^*}|`, contradicting minimality of `j^*`. Hence
`j^*\in M_n`, and `P_{j^*}\subseteq P_{i_0}` by construction. `∎`

(No new hypothesis is used; this is a verbatim re-derivation of already
certified material, recorded here as a standalone corollary because the
next lemma needs it in a form not stated explicitly elsewhere.)

### Hypothesis (MRS) — Minimal-Radical Stabilization

**(MRS):** There exists `N_0\ge1` such that `𝓜_n=𝓜_{N_0}` for every
`n\ge N_0`. Write `𝓜_\infty:=𝓜_{N_0}` (automatically finite, being a
subset of `\{P_1,\dots,P_{N_0}\}`) and `H:=\bigcup_{S\in𝓜_\infty}S`
(finite, a union of finitely many finite sets).

**This hypothesis is not proved in this round** (see "Open gaps"). It is
the sole remaining content of this approach.

### Lemma MS (Minimal-Radical Stabilization ⟹ FCBC) — fully proved, unconditional given (MRS)

**Statement.** If (MRS) holds, then `H` (as just defined) satisfies the FCBC
covering property: `H\cap P_i\cap P_j\ne\varnothing` for **every** `1\le
i<j` of the whole infinite sequence (unrestricted quantification, exactly
hypothesis `(†')` of Theorem 5.1).

**Proof.**

*Step 1 (every index, not just late ones, is dominated by `𝓜_\infty`).*
Fix any `i\ge1`. Let `n:=\max(i,N_0)\ge N_0`, so `𝓜_n=𝓜_\infty` by (MRS).
Apply Corollary W3′ with this `n` and `i_0:=i` (valid since `i\le n`): there
is `j^*\in M_n` with `P_{j^*}\subseteq P_i`. Since `j^*\in M_n`,
`P_{j^*}\in 𝓜_n=𝓜_\infty`. So **every** `i\ge1` (no exception, including
`i<N_0`) has `P_i\supseteq S_i` for some `S_i\in𝓜_\infty`.

*Step 2 (`𝓜_\infty` is pairwise intersecting).* Each `S\in𝓜_\infty` equals
`P_k=\mathrm{rad}(a_k)` for some actual index `k` (by definition,
`𝓜_\infty=\{P_i:i\in M_{N_0}\}`). Given `S,S'\in𝓜_\infty` with `S=P_k`,
`S'=P_{k'}`: if `S=S'` then `S\cap S'=S\ne\varnothing` (radicals of
integers `>1` are nonempty). If `S\ne S'` then `k\ne k'`, and Lemma P′
(pairwise global intersection, already certified, applies to **every** pair
of indices of the infinite sequence) gives `\gcd(a_k,a_{k'})>1`, i.e.
`P_k\cap P_{k'}\ne\varnothing`, i.e. `S\cap S'\ne\varnothing`. So every two
elements of `𝓜_\infty` intersect.

*Step 3 (`H` covers every pair).* Fix `i<j` (arbitrary indices of the whole
infinite sequence). By Step 1, `P_i\supseteq S_i` and `P_j\supseteq S_j` for
some `S_i,S_j\in𝓜_\infty`. By Step 2, `S_i\cap S_j\ne\varnothing`; pick
`p\in S_i\cap S_j`. Then `p\in S_i\subseteq H` (by definition of `H`),
`p\in S_i\subseteq P_i`, and `p\in S_j\subseteq P_j`. So
`p\in H\cap P_i\cap P_j`, proving `H\cap P_i\cap P_j\ne\varnothing`. Since
`i<j` were arbitrary, this holds for every pair of the whole infinite
sequence. `∎`

**Corollary (MS + Theorem 5.1 ⟹ the entire problem, conditional only on
(MRS)).** If (MRS) holds, Lemma MS gives a finite set `H` satisfying `(†')`
exactly as required by the already-certified **Theorem 5.1**
(`lemmas/theorem-5.1-master-conditional-theorem.md`), which then gives
`a_{n+T}=a_n+L` for **every** `n\ge1`, with `T=|Good|`, `L=\mathrm{lcm}(H)`
— i.e. the problem's exact target conclusion, for the whole sequence, not
just eventually. **This also re-derives the round-4 explorer's original
target (`G_n`-periodicity) as a free corollary**: `a_{n+T}=a_n+L` for all
`n` immediately gives `a_{n+T}\equiv a_n\pmod L`, hence identical
divisibility by every `p\in P_1\subseteq \mathrm{primes dividing }L`, hence
`G_{n+T}=G_n` for all `n\ge1` — so (MRS) is a *strictly more direct* route
to the problem than the outline's original "prove `G_n`-periodicity, then
separately close the residue-channel Gap B" plan: it does not need
`G_n`-periodicity as an intermediate step at all, and it makes Gap B
(residue-channel reduction of `F_{S,S'}`) entirely unnecessary rather than
solving it separately.

**Honesty check — is (MRS) equivalent to FCBC, or only sufficient?** Only
sufficiency is proved here. The converse (FCBC `⟹` (MRS)) is not
established and is not needed for the corollary above; it is conceivable in
principle that some *other* finite covering set `H'`, unrelated to the
canonical minimal-radical antichain, satisfies `(†')` while `𝓜_n` itself
never stabilizes. This is flagged, not resolved, and should not be
conflated with FCBC in any future round without a separate argument.

**Computational note (so the numerics below faithfully match the formal
definition of `𝓜_n`, not just an implementation).** The simulator computes
`𝓜_n` incrementally (compare the new radical `P_n` only against the current
antichain, rather than recomputing minimal elements of `\{P_1,\dots,P_n\}`
from scratch each step). This is exact, not an approximation: if `P_n` is a
superset of some element already in `𝓜_{n-1}`, it is not minimal in
`\{P_1,\dots,P_n\}` either (that witness is still among the first `n-1`
terms), so it is correctly excluded; if `P_n` is *not* a superset of
anything in `𝓜_{n-1}`, then no `P_k` (`k<n`) can be a strict subset of
`P_n` either — such a `P_k`, if not itself minimal in `\{P_1,\dots,P_{n-1}\}`,
would be a superset of some `s\in𝓜_{n-1}`, giving `s\subseteq P_k\subsetneq
P_n`, i.e. `P_n` would be dominated by `s`, contradicting the assumption —
so `P_n` is genuinely minimal in the enlarged set, and any prior minimal
element that is now a strict superset of `P_n` is correctly dropped. Hence
the incremental computation exactly equals `\{P_i:i\in M_n\}` at every step.

### Numerical evidence for (MRS)

Verified with a from-scratch Python simulator (`gen_sequence` in
`/tmp/round-4/sim.py`, matching the certified exact greedy rule, already
cross-checked against Lemma 1's bound with zero violations by the round-4
explorer) on all 12 previously-tested `a_1` values, including all five
historically-hardest cases (`221,247,375,4087,4199`) and the required test
set (`15,221,247,375,4087,4199`). Two independent checks were run per case:
(1) the **domination check**: for every index `i` in the tested range, does
`P_i` contain some element of the *final* `𝓜_\infty` as a subset (this is
exactly Step 1 of Lemma MS's proof, checked directly rather than trusted);
(2) the **exhaustive pair check**: for every pair `1\le i<j\le N`
(`N=4000`–`6000`), is `H\cap P_i\cap P_j\ne\varnothing`, checked by brute
force with no shortcuts (not just the structurally-derived version) — this
is the literal FCBC covering property `(†')` restricted to a finite range.

| `a_1` | `k` | `P_1` | `\lvert𝓜_\infty\rvert` | last change at `n=` | `H` | domination-check range (fails) | exhaustive pair-check range (fails) |
|---|---|---|---|---|---|---|---|
| 15 | 2 | {3,5} | 3 | 3 | {2,3,5} | 1..6000 (0) | 1..6000 (0) |
| 35 | 2 | {5,7} | 4 | 4 | {2,3,5,7} | 1..6000 (0) | — |
| 65 | 2 | {5,13} | 4 | 5 | {2,3,5,13} | 1..6000 (0) | — |
| 105 | 3 | {3,5,7} | 4 | 16 | {2,3,5,7} | 1..6000 (0) | — |
| 143 | 2 | {11,13} | 4 | 13 | {2,3,11,13} | 1..6000 (0) | — |
| 221 | 2 | {13,17} | 5 | 6 | {2,3,5,13,17} | 1..6000 (0) | 1..4000 (0) |
| 247 | 2 | {13,19} | 7 | 7 | {2,3,5,7,13,19} | 1..6000 (0) | 1..4000 (0) |
| 375 | 2 | {3,5} | 5 | 26 | {2,3,5,7,19} | 1..6000 (0) | 1..4000 (0) |
| 1001 | 3 | {7,11,13} | 4 | 59 | {2,7,11,13} | 1..6000 (0) | — |
| 2431 | 3 | {11,13,17} | 7 | 64 | {2,3,7,11,13,17} | 1..6000 (0) | — |
| 4087 | 2 | {61,67} | 3 | 54 | {2,61,67} | 1..6000 (0) | 1..4000 (0) |
| 4199 | 3 | {13,17,19} | 7 | 92 | {2,3,13,17,19,83} | **1..400000 (0)** | 1..4000 (0) |

Every one of the 12 cases stabilizes **early** (worst case `n=92`, for the
same `a_1=4199` whose `G_n`-period is `105{,}250` — i.e. stabilization of
`𝓜_n` happens roughly 1000× earlier than the eventual `G_n`-period, a
striking gap between "when the mechanism locks in" and "when its periodic
consequences become externally visible"), and — for the hardest case —
verified unchanging over a range **four times the eventual period**, with
the domination property holding with **zero exceptions** across all
400,000 tested terms. Also spot-checked (not tabulated): on the `a_1=221`
and `a_1=375` traces used by the already-refuted Propositions ND1/ND2, the
`H` constructed here (`{2,3,5,13,17}` and `{2,3,5,7,19}` respectively)
**does** cover the exact pairs that broke the Domination-Lemma-based
mechanisms (`(2,4)` with witness prime `3`; `(3,7)` with witness prime
`19`) — a nontrivial cross-check that this is a genuinely different,
so-far-more-successful construction, not a relabeling of ND1/ND2's failed
mechanism.

### Negative finding 1 (kills the outline's originally-proposed Gap-A mechanism)

Tested directly whether `G_{n+1}` (or `ρ_{n+1}:=a_{n+1}\bmod L`) is a
deterministic function of a **bounded-length window** of its own recent
values — the outline's own proposed shape of argument ("exhibit an
auxiliary state `s_n` ... such that `G_{n+1}` is a deterministic function of
`s_n` alone"). Result: **false for every fixed window length tested**,
`W=1,\dots,40`, on `a_1=221,247,375`. E.g. for `a_1=221` (`\rho`-sequence,
`L=221`): `W=1` gives 29 distinct states with 18 non-deterministic (62%);
even `W=8` still has 9/322 non-deterministic (2.8%). For the `G_n`-sequence
directly (alphabet size 3): `a_1=221` needs `W=40` to reach **zero**
non-deterministic transitions, and at that point the number of distinct
length-40 windows observed (334) exactly equals the already-known period
`T_G=334` — i.e. the window only becomes "deterministic" once it is
already at least as long as the very period it would be used to establish,
which is circular as a *proof* method (the period is discovered by the
data, not derived independently of it). **Conclusion: no genuinely
bounded-independent-of-`n` window state on `G_n` or `\rho_n` works; this
mechanism is retired, not just "unverified" as the outline left it.**

### Negative finding 2 (why a naive monotone-descent proof of (MRS) fails)

The obvious strategy to prove (MRS) would mimic the already-certified
Lemma C (`C_n:=\bigcap_{i\le n}P_i` is non-increasing, hence stabilizes by
finite descent since `|C_n|\le k`). This does **not** transfer: `|𝓜_n|`
(and `H_n:=\bigcup_{S\in𝓜_n}S`, the "as-of-step-`n`" version of `H`) are
**not monotonic** in `n` — verified explicitly on `a_1=4087`: `|𝓜_n|`
climbs `1,2,3,4,4,5,\dots,17,17,17,17` through `n=53`, then **collapses to
`3` in one step at `n=54`** and never changes again (matching the table
above). The corresponding `H_n` simultaneously loses 14 of its 17 primes in
one step: `H_{53}=\{2,3,5,7,11,13,17,19,23,29,37,41,43,47,53,59,61,67\}`
(18 primes) `\to H_{54}=\{2,61,67\}` (3 primes). This single-step collapse
(a new term `a_{54}` whose radical happens to be a superset of one existing
minimal set, simultaneously dominating and removing over a dozen previously
"minimal" radicals at once) is a genuine structural phenomenon, not a bug
in the simulator (double-checked against Lemma 1's gap bound, no
violations). **Consequence: any future attempt to prove (MRS) must handle
this non-monotone collapse directly — a simple bounded-monovariant argument
in Lemma C's style will not work, and a proof (if one exists) needs to
explain why collapses like this are *guaranteed* to eventually stop
occurring, not merely observed to stop in every tested example.** This is
recorded so a future round does not re-attempt the Lemma-C-style approach
on `𝓜_n`/`H_n` without a genuinely new idea for handling non-monotonicity.

### Relationship to the outline's original Gap A / Gap B

- **Gap A** (raw `G_n`-periodicity via a bounded state) is **not closed**,
  and the one concrete candidate mechanism (fixed-length window on `G_n` or
  `\rho_n`) is now **verified false**, not merely "unverified" (Negative
  finding 1) — a real, if negative, contribution per the outline-reviewer's
  suggested honest outcome (b).
- **Gap B** (residue-channel reduction mod `T_G`, conditional on `G_n`
  periodicity) was **not separately attempted this round**. This is a
  deliberate scoping choice, not an oversight: the (MRS)-based route found
  this round, if it closes, bypasses the need for Gap B entirely (Lemma MS
  goes directly to FCBC without ever invoking `G_n`-periodicity or
  residue-channel reduction). Gap B remains a logically independent, valid
  target for a future round that wants to pursue the original
  `G_n`-periodicity route instead of (or in parallel with) (MRS); it is
  simply not the most promising route any more given this round's finding.
- **Net effect**: the approach's target has shifted from the outline's
  two-gap plan (A, then B) to a single sharper hypothesis, (MRS), which is
  *stronger* than raw `G_n`-periodicity (Lemma MS's corollary shows (MRS)
  `⟹` `G_n`-periodicity, not just conditionally-useful information about
  it) and *sufficient by itself* to finish the whole problem via
  already-certified machinery (Lemma W3, Lemma P′, Theorem 5.1). This is a
  genuine simplification of the remaining work, verified consistent with
  every numerical fact already on record in the workspace (ND1/ND2's
  counterexample pairs, the `4199` period, the `a_1=65` sharpness example
  used by Lemma C).

## Open gaps

0. **(Superseded by "Round 5 Fix" above — kept for history, do not re-read
   as current.)** Via the DM-multiset-order + fan/threshold mechanism, an
   earlier draft of this round's outline reduced (MRS) to two sub-lemmas,
   (a) "Bounded Core Family" and (b) "Bounded growth-per-core", but the
   outline-reviewer correctly showed (a), as stated, only accounted for
   collapse-triggering cores, not permanently-surviving inserted values
   (counterexample: `a_1=91`, zero collapses, three permanent survivors).
   **This is now fully repaired** — see "Round 5 Fix": Theorem CD replaces
   (a) with a provably-complete, unconditional, `\le2^k-1`-case core
   decomposition of `𝓥` (covering permanent and transient values alike), and
   Lemma TC closes one case (`S=P_1`) outright. Sub-lemma (b)'s content
   survives, correctly re-scoped as "is `𝓥_S` finite for each of the
   remaining `\le2^k-2` proper cores `S\subsetneq P_1`" — see item 1 below.
1. **Prove `𝓥_S` finite for every proper nonempty core `S\subsetneq P_1`**
   (equivalently, by Theorems V-MRS + CD + Lemma TC, this is now **exactly**
   hypothesis (MRS)). This is the **sole** open content of this approach,
   and (per Lemma MS's corollary) closing it would finish the **entire** IMO
   2026 P6 problem (Case I is already fully solved; Case II would follow via
   Theorem V-MRS/CD + Lemma MS + the already-certified Theorem 5.1).
   Verified with zero exceptions across 15 diverse `a_1` values that every
   `𝓥_S` tested is finite (max observed `17`, at `a_1=4087`, `S=\{61\}`),
   but no general bound is proved. **Not a routine pigeonhole exercise**:
   Negative finding 2 (still valid) shows the natural monotone-descent
   strategy (Lemma C's own technique, applied to `|𝓜_n|` or `|𝓥_S|`
   directly) fails outright, since these are not monotonic in `n`; a correct
   proof needs a genuinely new argument, and the DM-order tool (Round-5
   Outline Step 1) only shows individual collapses decrease a multiset
   order, not that fan growth or collapse-freeness is bounded. **This gap
   is identical to `persistent-backbone-monovariant`'s open `𝓥`-finiteness
   target** (see "Round 5 Fix", "Explicit convergence" — stated openly, not
   hidden, per this round's dispatch instructions).
2. **(Secondary, not required to finish the problem.)** Is (MRS) actually
   *equivalent* to FCBC, or strictly stronger? Not attempted; flagged
   explicitly in "Honesty check" above so no future round conflates the
   two without proof.

## Full proof
(Not present — Status is `partial`. Lemma MS above is a complete, gap-free,
unconditional proof of "(MRS) `⟹` FCBC `⟹` the whole problem" — reusable
immediately by any future round that closes (MRS). The hypothesis (MRS)
itself is open; see "Open gaps" for exactly what remains and why the
obvious proof strategies fail.)
