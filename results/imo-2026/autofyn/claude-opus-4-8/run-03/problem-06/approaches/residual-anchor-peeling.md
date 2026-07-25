# Approach: residual-anchor-peeling

## Status
partial

## Idea in one line
Prove the whole theorem by **partitioning the finite-alphabet crux over the finite anchor set
`P = primes(a₁)`**: assign each ⊆-minimal support `G∈𝓐_∞` to `α(G)=min(G∩P)` (well-defined by the
Anchor lemma), so `Π` is finite **iff** each of the `|P|` "anchor fibers" `𝓐_∞^{(p)}` uses finitely
many primes. This localizes the crux to a single fixed anchor `p*`, where all fiber members share
`p*` and (after a small-part pigeonhole) a common core `B={p*}∪S₀`, reducing the crux to a
per-anchor persistence bound. **The scaffold (partition + localization) is proved rigorously and is a
genuinely different, non-circular framing.** The quantitative closing step — bounding one fiber — is
shown below to reduce *verbatim* to the field-wide wall E5 (`sup|G|<∞`); this is reported honestly as
a shared gap, together with the exact reduction and a promotable new equivalent form of the crux.

## Approaches tried (this round R4 first, then history)
- **R4 residual-anchor-peeling (this file).** Built the finite anchor-partition scaffold (Partition
  Lemma, proved), the localization to one anchor (proved), and the small-part pigeonhole (proved,
  steps 1–4). Then attempted the per-anchor persistence contradiction (step 5). **Outcome: the
  quantitative step 5 collapses onto E4's chain-descent** — the common core `B={p*}∪S₀` is a proper
  sub-support of every fiber member, hence (certified E2⇒) **not** a transversal, and continuing the
  argument reproduces the E4 descent `B_1⊊B_2⊊…` verbatim, whose termination is exactly `sup|G|<∞`
  (E5). So this pole shares the field-wide wall, as the outline-reviewer flagged. **Delivered
  rigorously:** the Partition Lemma (a new, clean equivalent form of the crux — promotable) and a
  *proof* (not a heuristic) that the anchor localization collapses to E5, upgrading the reviewer's
  "shared-wall" diagnosis to a theorem. Also a methodological correction: minimal supports computed
  from a finite prefix **overcount** (spurious families collapse once their common core is realized).
- **(new skeleton, R4, superseded by the build above.)**

## Certified inputs (reused, not re-proved)
- **Anchor (L1):** every term, hence every `G∈𝓐_∞`, meets `P=primes(a₁)`. (`free-lemmas.md`)
- **Gap/growth (L2):** `a_{n+1}−aₙ ≤ M := rad(a₁)`; `aₙ=Θ(n)`. (`free-lemmas.md`)
- **Distance–prime (L3):** `q∣aᵢ, q∣aⱼ (i≠j) ⟹ q ≤ |aᵢ−aⱼ|`. (`free-lemmas.md`)
- **Pairwise-intersecting (L4):** `gcd(aᵢ,aⱼ)>1` for `i≠j`; members of `𝓐_∞` pairwise intersect.
  (`free-lemmas.md`)
- **E1 (Enumeration):** `{aₙ} = A ∩ [a₁,∞)`, `A={c : c meets every G∈𝓐_∞}`.
  (`enumeration-and-transversal.md`)
- **E2(⇒) / self-blocking:** every `G∈𝓐_∞` is a ⊆-minimal transversal of `𝓐_∞`; and (realization
  preliminary + E2⇐) every **finite** minimal transversal is realized as a term, hence is a member.
  (`enumeration-and-transversal.md`, `size-bound-reduction.md`)
- **E3 (private witness):** for `G∈𝓐_∞`, `p∈G` there is `G_p∈𝓐_∞` with `G∩G_p={p}`.
  (`enumeration-and-transversal.md`)
- **E4 (size-bound reduction):** `𝓐_∞` finite ⟺ `sup_{G∈𝓐_∞}|G|<∞`; and `𝓐_∞` infinite ⟹ minimal
  supports of *unbounded* cardinality. (`size-bound-reduction.md`)
- **Endgame:** `Π` finite ⟹ `a_{n+T}=aₙ+L` for all `n≥1`, `T=|ρ(A)|`, `L=∏Π`.
  (`no-transient-fixed-successor.md`)

Notation throughout: `F(x)=primes(x)`, `Fₙ=F(aₙ)`, `𝓕={Fₙ:n≥1}`, `𝓐_∞ = ⊆-minimal elements of 𝓕`
(**taken over the full infinite sequence**), `Π=⋃𝓐_∞`, `P=F(a₁)`, `M=rad(a₁)=∏_{p∈P}p`.

---

## What is proved (the scaffold, rigorous)

### Lemma A (Partition Lemma) — PROVED
*For `G∈𝓐_∞` set `α(G):=min(G∩P)`. This is a well-defined map `α:𝓐_∞→P`, and writing
`𝓐_∞^{(p)}:={G∈𝓐_∞ : α(G)=p}`, `Q_p:=⋃_{G∈𝓐_∞^{(p)}}G`, we have `𝓐_∞=⨆_{p∈P}𝓐_∞^{(p)}`,
`Π=⋃_{p∈P}Q_p`, and therefore:*
$$\Pi \text{ is finite} \iff Q_p \text{ is finite for every } p\in P \iff \mathcal A_\infty^{(p)} \text{ is finite for every } p\in P.$$

*Proof.* By the Anchor lemma L1 every term meets `P`, so every `G∈𝓐_∞` (being some `F(aᵢ)`) has
`G∩P≠∅`; as `G∩P` is a nonempty subset of the totally ordered finite set `P`, `min(G∩P)` exists and
is unique. Hence `α` is a well-defined function into `P`. Its fibers `𝓐_∞^{(p)}` partition `𝓐_∞`
(every element lands in exactly one fiber). Taking unions of supports, `Π=⋃_{G∈𝓐_∞}G
=⋃_{p∈P}⋃_{G∈𝓐_∞^{(p)}}G=⋃_{p∈P}Q_p`, a union over the **finite** index set `P`.

A finite union of sets is finite iff each set is finite, giving the first `⟺`. For the second `⟺`:
if `𝓐_∞^{(p)}` is finite it is a finite family of finite sets, so `Q_p` is finite; conversely if
`Q_p` is finite then every member of `𝓐_∞^{(p)}` is a subset of the finite set `Q_p`, and there are
only finitely many subsets of a finite set, so `𝓐_∞^{(p)}` is finite. ∎

**Value of Lemma A.** It decomposes the crux `Π` finite into `|P|=ω(a₁)` independent finite-fiber
statements, each attached to a *single fixed anchor prime* `p*`. This is a legitimate new equivalent
form of the crux (see Promotable lemmas). It differs from E4 in target: E4 bounds `sup|G|` globally;
Lemma A asks, per anchor, that only finitely many minimal supports pick `p*` as their least
`P`-prime. On every stabilized example the fibers are tiny (below), so the localization is real.

**Numerical illustration (stabilized `𝓐_∞`, verified by simulation).**
- `a₁=375`, `P={3,5}`, `M=15`: `𝓐_∞^{(3)}={\{2,3\},\{3,5\},\{3,7,19\}}`,
  `𝓐_∞^{(5)}={\{2,5,7\},\{2,5,19\}}`. Here `19>M` sits in one member of **each** fiber (a shared
  witness across anchors — permitted; `Q_3∩Q_5⊇\{19\}`), and `Π=\{2,3,5,7,19\}` is finite.
- `a₁=9375`, `P={3,5}`, `M=15`: `𝓐_∞^{(3)}={\{2,3\},\{3,5\},\{3,7\},\{3,67\}}`,
  `𝓐_∞^{(5)}={\{2,5,7,67\}}`; `Π=\{2,3,5,7,67\}` (67>M shared across fibers).

### Lemma B (Localization) — PROVED
*Fix `p*∈P`. Every `G∈𝓐_∞^{(p*)}` contains `p*`; `𝓐_∞^{(p*)}` is a ⊆-antichain whose members
pairwise intersect and each of which is a ⊆-minimal transversal of `𝓐_∞`.*

*Proof.* `p*=α(G)=min(G∩P)∈G`. `𝓐_∞^{(p*)}⊆𝓐_∞`, and `𝓐_∞` is a ⊆-antichain (it is the family of
⊆-minimal elements of `𝓕`), so any subfamily is too. Pairwise intersection: any two members share
`p*` (both contain it); more strongly they pairwise intersect by L4/E2⇒. Each member is a ⊆-minimal
transversal by certified E2(⇒). ∎

### Lemma C (Small-part pigeonhole) — PROVED (conditional shape)
*Suppose, for contradiction toward Lemma A, that some fiber `𝓐_∞^{(p*)}` is infinite. Then there is
a fixed finite prime set `S₀⊆{primes ≤ M}` and an infinite subfamily `𝓗⊆𝓐_∞^{(p*)}` such that every
`G∈𝓗` satisfies `G∩{primes ≤ M}=S₀`. Writing `B:={p*}∪S₀` (note `p*∈P` so `p*≤M`, hence
`B⊆{primes ≤ M}` and `B∩{primes≤M}=B`), every `G∈𝓗` satisfies `B⊆G`, and `𝓗` members differ only in
primes `>M`.*

*Proof.* For each `G`, the "small part" `S(G):=G∩{primes ≤ M}` is a subset of the finite set
`{primes ≤ M}` (there are `π(M)` such primes), so there are at most `2^{π(M)}` possible values of
`S(G)`. Since `𝓐_∞^{(p*)}` is infinite and the small part takes finitely many values, by the
Pigeonhole principle (`knowledge_base.md`, "Pigeonhole / extremal principle") some value `S₀` is
attained by an infinite subfamily `𝓗`. For `G∈𝓗`, `p*∈G` and `p*≤M`, so `p*∈S(G)=S₀`; thus
`B={p*}∪S₀=S₀⊆G`. Members of `𝓗` agree on all primes `≤M` (all equal `S₀`), so any two differ only
in primes `>M`. ∎

### Lemma D (Distinct large co-primes) — PROVED
*Under Lemma C, one may extract members `G₁,G₂,…∈𝓗` and primes `q₁<q₂<⋯` with `qₖ>M`, `qₖ∈Gₖ`,
`qₖ→∞`. Each `qₖ` has (E3) a private witness `Hₖ∈𝓐_∞` with `Gₖ∩Hₖ={qₖ}`.*

*Proof.* `𝓗` is infinite and is an antichain of finite sets all containing the fixed `B`. If only
finitely many primes `>M` occurred among `⋃_{G∈𝓗}G`, then `⋃_{G∈𝓗}G` would be finite, so `𝓗`
(a family of subsets of a finite set) would be finite — contradiction. Hence infinitely many distinct
primes `>M` occur. Enumerate them `q₁<q₂<⋯→∞`; for each `k` pick `Gₖ∈𝓗` with `qₖ∈Gₖ` (choosing the
`Gₖ` distinct is possible: each prime lies in at least one member, and by discarding members already
used and re-picking a fresh large prime — the pool of large primes is infinite — we obtain distinct
`Gₖ`). Each `qₖ∈Gₖ∈𝓐_∞`; E3 gives `Hₖ∈𝓐_∞` with `Gₖ∩Hₖ={qₖ}`. ∎

At this point the fiber-infinite hypothesis has produced exactly the empirically dominant obstruction
shape: infinitely many minimal supports `Gₖ={p*}∪S₀∪(\text{large primes, incl. }qₖ)`, common core
`B={p*}∪S₀`, distinct large primes `qₖ→∞`, each with a private witness `Hₖ` meeting `Gₖ` only in `qₖ`.

---

## Where it stops: step 5 collapses onto E5 (proved, reported honestly)

The remaining task is: **derive a contradiction from Lemmas C–D**, i.e. show a fiber cannot be
infinite. The honest finding of this build is that this step is *not* independent of the field-wide
wall.

### Proposition (Collapse) — PROVED
*The step "the common core `B={p*}∪S₀` forces a dominating term, contradicting minimality of the
`Gₖ`" cannot occur for a genuine infinite fiber; and pursuing the argument reproduces the certified
E4 chain-descent, whose termination is exactly `sup|G|<∞` (E5). Concretely:*

1. **`B` is not a transversal.** Each `G∈𝓗` has `B⊊G` (properly, since `G` contains a large prime
   `qₖ∉B`). If `B` were a transversal of `𝓐_∞`, then by certified **Lemma 11.0** (`size-bound-
   reduction.md`) `B⊇G₀` for some `G₀∈𝓐_∞`; but then every `G∈𝓗` satisfies `G⊇B⊇G₀`, and the
   antichain property forces `G=G₀`, so `𝓗⊆{G₀}` is finite — contradicting `𝓗` infinite. Hence `B`
   is **not** a transversal. Equivalently (certified E2⇒): a proper sub-support `B⊊G` of a minimal
   support `G` is never a transversal, so **the hoped-for "`B`-support term dominating the `Gₖ`" can
   never be realized** — its realization would make `B` a transversal (E2's realization preliminary),
   contradiction. This is exactly the outline-reviewer's flag: "preemption" of the fiber by a common
   sub-support is *logically equivalent to `B` being a transversal*, which never holds for an infinite
   fiber. So step (5a) as originally hoped is vacuous.

2. **The remaining route is the E4 descent, verbatim.** Since `B` is not a transversal, there is
   `W∈𝓐_∞` with `W∩B=∅`. Every `G∈𝓗` is a transversal (E2⇒), so meets `W`; as `G⊇B` and `W∩B=∅`,
   the shared prime lies in `W∖B`. `W` is finite and `𝓗` is infinite, so by Pigeonhole some
   `r∈W∖B` lies in infinitely many `G∈𝓗`; set `B':=B∪{r}` (a strictly larger common core) and
   `𝓗':={G∈𝓗:r∈G}` (infinite). This is **precisely one step of the certified E4 chain-descent**
   `B_1⊊B_2⊊⋯` with `𝓗_1⊇𝓗_2⊇⋯`, started from the anchored core `B` instead of a single pigeonholed
   prime. Iterating produces cores of size `|B|,|B|+1,\dots`, all contained in members of `𝓗`; the
   descent runs forever iff members of `𝓗` have unbounded cardinality. Thus **"the fiber
   `𝓐_∞^{(p*)}` is finite" is, through this argument, equivalent to `sup_{G}|G|<∞` — the certified
   E5 wall — with the anchor `p*` used only to seed the first core `B`, contributing no independent
   quantitative bound.**

*Proof.* Parts (1)–(2) are the arguments just given; they invoke only certified Lemma 11.0, E2(⇒),
the antichain property, and Pigeonhole. ∎

**Consequence (honest verdict).** Per the outline-reviewer's explicit instruction ("if step 5 reduces
verbatim to bound `sup|G|` with no use of `p*`, report collapse rather than re-deriving E5"), we
report: **the quantitative closing of this pole collapses onto E5.** The anchor `p*` cleanly seeds
and localizes the descent (a real structural simplification, Lemmas A–D), but supplies no new
arithmetic to terminate it. The load-bearing wall — "force a common non-transversal sub-support term,
or equivalently bound the depth of the sub-support descent" — is identical to the antichain pole's
E5. This upgrades the reviewer's heuristic "shared-wall" diagnosis to a *proof* that the two poles
share one wall, which is actionable for the orchestrator (see below).

### Why the naive persistence bounds also fail (recorded, so no re-attempt)
- **Sparsity alone (5b) is insufficient.** By L3, `qₖ∣uₖ` and `qₖ∣wₖ` give `qₖ≤|uₖ−wₖ|`, so
  `qₖ`-multiples among terms have index-density `O(M/qₖ)→0`; but a density-0 set can still be
  infinite. The certified obstruction family `{p*,q_k}` (`monovariants-and-obstruction.md`) is an
  infinite, arbitrarily-sparse anchored family, showing sparsity is combinatorially consistent with
  an infinite fiber. Only realizability (E2⇒ self-blocking) excludes it — and that is exactly the E5
  content, not a bypass. (Confirmed by the persistence explorer, R4.)
- **The E3 witness distance is too weak.** The minimal realizers `uₖ,wₖ` of two mutually-blocking
  supports can be `Θ(M)` apart, so `qₖ≤|uₖ−wₖ|` yields no `a₁`-only cap (recorded role-memory, R3).

### Methodological correction (used to keep the proof honest; verified numerically)
`𝓐_∞` must be the ⊆-minimal supports over the **entire infinite sequence**. Minimal supports computed
from a finite prefix **overcount**: for `a₁=9375`, a 600-term prefix shows a *spurious* infinite-looking
anchor-3 family `{3,17,67},{3,19,67},{3,47,67},{3,53,67},{3,59,67},…` (common core `{3,67}`), all of
which are **dominated and deleted** once the term of support `{3,67}` (realizer 13467) appears; the
true stabilized fiber is `𝓐_∞^{(3)}={\{2,3\},\{3,5\},\{3,7\},\{3,67\}}` (verified to 2800 terms,
`maxval≈22044`). This is the persistence mechanism made concrete: the spurious family's common core
`{3,67}` *is* a transversal (it meets `{2,3},{3,5},{3,7}` via 3 and `{2,5,7,67}` via 67), so by
Proposition (1) it becomes a realized member and collapses the family. An infinite *true* fiber would
require a common core that is *never* a transversal at any depth — the open E5 obstruction.

---

## Conclusion of the pole
Granting the crux (`Π` finite), Lemma A + the certified endgame give the theorem with explicit
`T=|ρ(A)|`, `L=∏Π` (as in the leader approach). This pole contributes: a rigorous, non-circular,
terminating **finite** decomposition of the crux (Lemma A), a clean localization (Lemmas B–D), and a
**proof** that the per-anchor persistence bound collapses onto E5. It does **not** close the crux.

## Open gaps
- **The single substantive gap = E5** (`sup_{G∈𝓐_∞}|G|<∞`, equivalently each anchor fiber finite),
  reached here through the anchor localization but shown (Proposition Collapse) to be the same wall as
  the antichain pole. **This pole shares the field wall.** Per the reviewer's plateau note, closing it
  needs a mechanism that does *not* route through "force a non-transversal common sub-support to be
  realized" — e.g. an aimo-0421 recursive-dichotomy on residual index sets, or an aimo-0447 `Σ1/p²`
  covering **restricted to minimal-support primes**, neither yet built.

## Cases to cover (status)
- `p*` over all of `P`: uniform, handled by Lemma A (finite `P`). ✓
- `S₀` over `2^{π(M)}` values: Pigeonhole, Lemma C. ✓
- Fiber finite (nothing to prove) vs infinite (Lemmas C–D reach the obstruction shape; contradiction
  is the open E5 gap). ✓ up to the gap.

## Promotable lemmas
- **Anchor-Partition equivalence (Lemma A).** *`α(G)=min(G∩P)` is a well-defined map `𝓐_∞→P`; it
  partitions `𝓐_∞=⨆_{p∈P}𝓐_∞^{(p)}`, and `Π` is finite ⟺ every fiber `𝓐_∞^{(p)}` is finite ⟺ every
  `Q_p=⋃𝓐_∞^{(p)}` is finite.* Proved in full above (uses only certified Anchor L1 + finiteness of
  `P`). This is a new, unconditional equivalent form of the Finite-Alphabet crux, decomposing it over
  the finite anchor set — reusable by any future per-anchor pole. Certify into `lemmas/`.
- **Sub-support non-transversality (Proposition, part 1).** *If `𝓗⊆𝓐_∞` is infinite with a common
  core `B` (`B⊆G` ∀`G∈𝓗`), then `B` is not a transversal of `𝓐_∞`; equivalently no proper
  sub-support of a minimal support is ever realized as a term.* Proved from certified Lemma 11.0 +
  antichain + E2's realization preliminary. This is the rigorous form of the "preemption is
  equivalent to E5" observation — useful as a *guardrail* certifying that any pole hoping to "force a
  dominating common sub-support term" is attacking E5 itself, not bypassing it. Certify into `lemmas/`.
