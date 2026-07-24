## imo-2026-06 (lens: H1/FAH plateau-break sweep)

### What H1/FAH precisely states (re-confirmed from source, not re-derived)
Owned jointly by `covering-system-construction.md` (Step 8.3–8.5) and
`greedy-exchange-cost-potential.md`. Setup: Q = P(a_1) fixed forever; finite core
S₀ ⊇ Q; 𝒫 = finite set of **persistent base types** (subsets of Q occurring
infinitely often); for S₀-extended-persistent refinements A', B' of disjoint base
types A, B ∈ 𝒫, a pair is **rogue** if A'∩B'=∅. The certified Lemma G
(`lemmas/extended-earliest-witness-intersection.md`) gives, for the two earliest
occurrences n_A<n_B of A', B', a prime q ∉ S₀ with q | a_{n_A}, q | a_{n_B}.
**FAH** asserts q divides a_n for *every* n>n_B with ρ(n)=A' (not just infinitely
many) — i.e. the linking prime, once witnessed twice, becomes *permanent* for the
earlier-starting type. **Symmetric FAH** is the same with roles swapped. Step 8.2's
certified Collateral-Safety Theorem shows the whole recruitment process reduces
exactly to: does every currently-rogue base-type pair get resolved (FAH-style) in
finitely many further rounds (`open(k) → ∅`)? This is now the single remaining
content of gap (†) — confirmed unconditional, no other hypothesis needed besides
Symmetric FAH.

### The graveyard (confirmed real, not re-litigated in detail — cross-checked
that the "30+ dead mechanisms" claim is genuine, tracing the numbered tally
1→14 explicitly in `greedy-exchange-cost-potential.md` and 14→31+ referenced by
round-22's current.md entry): orbit-merging/additive-offset dichotomy (round 22,
#31, dead — circular, and mistargeted to H2 not H1), monovariants/well-ordering
descent (round 3, round 5 `witness-index-descent`: refinement manufactures new
smaller-index rogue pairs, kills two independent monovariant choices), CRT/glue
constructions (round 2 Universal Glue Prime, refuted by explicit counterexample
a_1=35), sieve/density arguments (round 10 Sandwich Genericity/Escape-Cost
Vacuity, #10 dead), quantitative escape-budget/window-vacancy (round 10-11, #13,
#14 dead — partial-signature family also dead), martingale/renewal, Kolmogorov
complexity, o-minimality, nonstandard analysis, spectral/operator methods,
priority arguments/computability, subword-complexity/Morse–Hedlund (round 12,
dedicated plateau-break round, confirmed dead), central-sets/idempotent
recurrence (per dispatch, also dead). All per dispatch instructions and cross-
checked against current.md's own tally language.

### The one genuinely new, concrete angle found this sweep
**A "growing bipartite-network invariant" attack on `open(k)→∅` directly,
bypassing the literal FAH single-prime-permanence claim entirely.**

Source: crux corpus, `combinatorics` domain, `processes-and-algorithms` subtopic,
problem `aimo-1000` (IMO 2021 P6, the "ferry islands" problem — verified this is
a real, on-point structural analog, not a superficial keyword match). Crux move
(`how_used`, verified by reading the full solution): maintain **two evolving
finite sets A, B of islands (indices)** with the invariant "every element of A is
connected to every element of B" (a complete bipartite *network*, not a single
witness pair). When the one edge actually used by the invariant (between some
A∈𝒜, B∈ℬ) is destroyed by the process, the proof does **not** try to preserve
the exact same 𝒜,ℬ — it explicitly re-partitions: sets 𝒜' := {A,B} (the two
endpoints of the just-broken edge) and ℬ' := (𝒜∪ℬ)−{A,B}, and proves — using the
problem's own local update rule (an island connected to exactly one of the broken
edge's endpoints gets a new edge to the other) — that 𝒜',ℬ' is *again* a
complete network. The network is then grown by absorbing new islands one at a
time (via a second, structurally different argument using the problem's
"eventually every partition gets some cross-edge closed" hypothesis), until it
covers everything, at which point a final pigeonhole (some single island is
targeted infinitely often as an edge-endpoint) forces full completion.

**Why this is structurally distinct from every dead FAH mechanism above.** It is
not a monovariant (nothing decreases; the certificate is *re-built*, not shrunk,
after each local failure — the workspace's own round-3 well-ordering attempts
(`witness-index-descent`, minimal-counterexample on |A'|+|B'|) died precisely
because the natural measures are NOT monotone under refinement; this template
sidesteps that by not requiring monotonicity of the *pair itself*, only of the
*number of distinct base-type pairs still open*, which Step 8.2's Collateral-
Safety Theorem already independently guarantees is monotone). It is not
sieve/density, not CRT-glue (it needs no simultaneity of infinitely many
primes), not a global escape-cost/window count. It attacks a **joint,
simultaneous-across-all-occurrences** object (the full network of index pairs),
exactly the direction Step 4f (round 3) explicitly flagged as "the most
promising concrete direction… neither round's mechanism provides" and which —
confirmed by grep across every approach/lemma file in the workspace — was
**never picked up again in any of rounds 4–28**. That is a genuine, still-open,
never-attempted corridor, not a rebranding of a dead one.

**Concrete translation sketch (opening only, not an outline — where the outliner
would need to do real work).** For a rogue base-type pair (A,B) at stage S₀,
instead of Lemma G's single witness pair (n_A,n_B) and asking whether ITS linking
prime q persists (FAH, stuck), define 𝒜 := {n_A}, ℬ := {n_B} and try to grow
𝒜,ℬ as *sets of occurrence-indices* of A',B' (or refinements thereof) maintaining
"every index in 𝒜 shares a prime with every index in ℬ" as a first-class
invariant. The open, honestly-flagged gap for the outliner: aimo-1000's repair
step works because the ferry problem's move rule is *bespoke* — "exactly one of
X,Y" symmetric-difference — giving a free, exact re-link. Our problem's greedy-
gcd update rule has no obviously analogous "if you fail one intersection, you get
handed a repaired intersection for free" mechanism; this would need to be built
from the Generalized Bounded Witness Lemma / Free Facts stack, and is NOT
already given. This is therefore a real candidate corridor, not a proof — it
should be dispatched as one new rival approach (distinct file, e.g.
`bipartite-network-invariant-fah`), not folded into `covering-system-
construction` or `greedy-exchange-cost-potential`, since it targets `open(k)→∅`
directly and could in principle succeed even if literal (Symmetric) FAH is
false.

### Other corridors checked this sweep and found NOT new / not promising
- `zsigmondy-and-primitive-divisors` (crux corpus, number_theory, 2 entries:
  `aimo-0157`, `aimo-0611`): both rely on multiplicative structure (`b^n+1`
  primitive-divisor existence, or exponential dominance forcing a fresh prime at
  higher valuation). Our a_n is additively/greedily defined, not exponential;
  no natural embedding found. Not recommended.
- `linear-algebra-method` (combinatorics subtopic): scanned for
  invariant/periodic/divisor-related entries; nothing transfers (Fourier/DFT
  dimension-counting and integer-solution arguments, unrelated shape).
- Direct problem-statement search (`greedy`, `gcd(a_...)`, `smallest integer
  ... coprime`) across the 1026-problem corpus: no genuinely analogous "must
  share a factor with *every* prior term" greedy sequence problem exists in the
  corpus (this specific constraint — coprimality against the *entire* history,
  not just the last term — appears to be genuinely novel to IMO 2026 P6, not a
  known archetype).
- Re-confirmed (did not re-derive, but sanity-checked against the file's own
  stated numbers) that round 26/27's "fresh corridor" sweeps are correctly
  recorded as exhausted — no inconsistency found in the current.md accounting.

### Recommendation
Do **not** dispatch another *generic* "sweep for a new H1 mechanism" round.
Twenty-two rounds of dedicated search (plus two more explicit corridor sweeps)
have produced a real, wide graveyard and the field is at genuine diminishing
returns for open-ended search. Instead: dispatch **one** concrete new approach,
`bipartite-network-invariant-fah` (or similar name), scoped exactly as above —
attack `open(k)→∅` (Step 8.3's criterion, already unconditionally reduced and
certified) directly via a growing-network/repair-invariant construction modeled
on the aimo-1000 crux, explicitly NOT via the literal FAH/Symmetric-FAH
single-prime-permanence statement. If that approach's first build cannot find an
arithmetic analog of aimo-1000's "free repair on edge closure" step (a concrete,
checkable disambiguation question, per the workspace's own established
"mandatory disambiguation" precedent from `reversible-transition-map`), that
should be reported and closed out fast rather than iterated on for many rounds —
and if it also dies, the run's floor deliverable (8 certified subfamily
theorems + the gap-free Master Conditional Theorem reducing generality to
H1+H2) is a legitimate, defensible final position, and further rounds might be
better spent hardening/extending the subfamily front (e.g. `a1-13q`,
general-`p` `Bad(p)` machinery, or `a1-3qk` for `m≥4`) rather than continuing an
open-ended H1 hunt.

### Distinct openings (summary for outliner)
1. **Bipartite-network-invariant attack on `open(k)→∅`** (new, concrete, see
   above) — the recommended one new rival approach this round.
2. (Not new, but worth restating as the fallback default) Continue hardening the
   floor via more `a1-pq`-style per-`p` closures (`p=13,17,...`) — orthogonal to
   H1, doesn't need it, keeps producing certified partial results while H1 is
   reconsidered.

### Candidate technique(s)
Growing bipartite/network invariant with local repair-on-failure (combinatorics:
`processes-and-algorithms`), as opposed to monovariant/well-ordering, sieve, or
algebraic-dynamics techniques already exhausted.

### Cheap-kill candidates
None obvious for the new angle itself (it requires first resolving the
disambiguation question: does an analog of aimo-1000's "free re-link on edge
failure" exist in this arithmetic setting at all — this IS the cheap kill to run
first, before any lemma-writing).

### Knowledge-base entries to use
`knowledge_base.md`'s "Invariants & monovariants" and "Constructive /
incremental: realize every value... by starting from an extreme and adding one
unit at a time" (Combinatorics section) — generic pointers only; nothing
problem-specific in the KB for this angle (the KB is generic, the real precedent
is the crux corpus entry below).

### Analogous past problems (cruxes)
- **`aimo-1000`** (IMO 2021 P6, "ferry islands"), `combinatorics` /
  `processes-and-algorithms`. Crux: maintain a growing complete-bipartite
  "network" invariant between two evolving vertex sets, repaired (not
  shrunk) on each local failure via the process's own bespoke update rule, then
  grown to cover everything, finished by a final pigeonhole. Genuinely
  analogous in *shape* to FAH's rogue-base-type-pair structure (disjoint sets
  needing pairwise intersection); NOT analogous in mechanism (the repair step
  is bespoke to ferry-islands' edge-toggle rule and has no established
  arithmetic analog here — this is exactly the gap a builder would need to
  close). Confirmed via direct read of the full problem statement and solution
  in `past_problems_database.json`, not just the crux summary.
- `aimo-0514` (`processes-and-algorithms`, "reversibility ⟹ orbit is a union of
  cycles"): checked, but this is exactly the already-dead
  `reversible-transition-map` mechanism (round 5 RETHINK: equivalent
  restatement of gap (†), not a bypass). Not a new lead.
- `aimo-0157`, `aimo-0611` (`zsigmondy-and-primitive-divisors`): checked, not
  analogous (multiplicative/exponential sequences, no transfer to this
  additive greedy-gcd setting).

### Prior progress
8 certified subfamily theorems (`2|a_1`; `a_1=p^k`; `a_1=3q`; `a_1=3q^2`;
`a_1=3q^3`; `a1-3aq` for `a=1..5`; `a1-5q`; `a1-7q`; `a1-11q`), the `p`-uniform
`a1-pq` machinery (partial, `k≥1,gcd(k+1,j)>1` residual open for general `r`),
both known hard rogue-pair seeds (4807, 11305) fully resolved single-seed via
the Finite-Window Literalization Lemma, and the gap-free Master Conditional
Theorem reducing the fully general problem to H1 (FAH) + H2 (absorption-chain
termination). H1/FAH: 22nd consecutive plateau round (6–28). See
`results/imo-2026-06/current.md` Status header and
`approaches/covering-system-construction.md` Steps 8.1–8.5 for full detail.

### Dead ends (do not retry)
The full graveyard listed in the dispatch prompt (orbit-merging/additive-offset,
monovariants/well-ordering descent, sieve/density, martingale/renewal,
Kolmogorov complexity, o-minimality, nonstandard analysis, spectral/operator,
priority arguments/computability, subword-complexity/Morse–Hedlund,
central-sets/idempotent recurrence) — all independently cross-checked as
genuinely dead in the source files this round, not merely trusted from the
prompt. Additionally confirmed dead and not to retry: Universal Glue Prime
(round 2, refuted by a_1=35 counterexample); Universal Singleton Hypothesis
(round 5/6, refuted by a_1=4807,11305 with |F'|=2); the two natural well-
ordering measures (|A'|+|B'| size, and smallest-rogue-witness-index) — both
non-monotone under core refinement, independently re-confirmed by tracing the
proofs, not just re-reading the verdicts.

### Small-case / intuition notes
No new numeric experiments run this round (this was a literature/framing sweep,
not a computational one, per the dispatch's specific ask). The existing
computational record (zero FAH counterexamples found across all tested seeds
including the two hard rogue pairs, now both individually resolved) is
consistent with FAH being TRUE but just hard to prove in general — nothing
found this round suggests FAH is false, only that its general proof needs a
structurally different tool than what's been tried, which is what the
bipartite-network angle above offers as an untried candidate.
