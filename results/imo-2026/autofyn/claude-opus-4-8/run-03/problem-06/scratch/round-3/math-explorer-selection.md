## imo-2026-06 — lens: selection / choice dynamics

### Scope note
Both live approaches (`redundant-constraint-antichain`, `monovariant-witness-descent`)
agree the whole problem reduces to one crux (Finite Alphabet / equivalently "every
prime in a ⊆-minimal support is ≤ a₁"), and both are stuck there. My job was to look
at the actual greedy *choices* `a_n` — not just the admissible set `A_n` — since the
certified Obstruction Lemma (`lemmas/monovariants-and-obstruction.md`) proves no
`A_n`-only statistic can close the crux. Below: one important **clarifying/negative
finding** (the "dynamics" angle mostly collapses back to statics, contrary to what one
might hope) and one **new empirical pattern** (early-recruitment) that is a
genuinely different target from a direct size bound `q ≤ a₁`.

### Distinct openings

**(S1) Clarification: greedy *order* carries no extra information beyond E1 — a
negative/scoping result, but an important one.** I tried to use "t is the *smallest*
admissible value exceeding a_{n-1}" as a lever: does minimality of choice forbid a
large private-witness prime q from ever entering a minimal support? It does not, and
here is why, precisely: by the certified **E1 (Enumeration)**, `{a_n} = A ∩ [a₁,∞)`
— *every* element of the fixed set `A` eventually gets realized as a term, in
increasing order, with none skipped. So "is `G` a permanent ⊆-minimal support"
reduces to a purely **static** question about `A` (does any `c ∈ A` have `F(c) ⊊ G`?)
— it does **not** depend on the *order* in which elements of `A` are visited. Greedy
minimality only ever matters for *which set `A` is* (via the forward self-consistent
generation from `a₁`), not for which elements of a *already-fixed* `A` become
"locked in." Concretely: there is no smaller-value competitor argument available,
because once `m ≥ a₁` is known to lie in `A`, it is guaranteed to appear as some term
`a_l` (E1) — it is never "pre-empted" by a smaller admissible value, since that
smaller value would just be an earlier term, not a competitor that removes `m` from
the sequence. **Conclusion: "selection dynamics" reduces to E1+E2+E3 (already
certified); it does not supply a genuinely new lever beyond what both live approaches
already have.** This should save the outliner from expecting a "greedy minimality
forces q small" argument in the naive form — I looked for one and it does not exist
in this shape. Verified by direct definition-chasing above, not by search failure
alone.

**(S2) NEW empirical pattern: persistent large-prime recruitment happens almost
immediately after a₁, not late (the "Early Recruitment Window" conjecture).** Where
dynamics genuinely *does* matter is in the causal, forward-in-time construction of
`A` itself (a fixed point: `A` depends on all terms, terms depend on `A`). I computed,
for the two confirmed-converged "M-exceedance" cases on record (`a₁=375→L∋19`,
`a₁=9375→L∋67`, both verified converged at 900 / 3000 terms respectively — matching
round-2's numbers), the **first term at which the eventually-persistent large prime
first appears in ANY support** (not necessarily yet minimal):
- `a₁=375`: prime 19 first appears at term index **3** (value 380, i.e. only `a₁+5`,
  `(t−a₁)/M = 0.33`).
- `a₁=9375`: prime 67 first appears at term index **3** (value 9380, i.e. only
  `a₁+5`, `(t−a₁)/M = 0.33`).
In both cases the persisting large prime is "born" essentially immediately — within
the first handful of terms, while the sequence is still within `O(M)` of `a₁` — even
though the *companion* witness pair that ultimately privately-witnesses it (E3) can
form much later (for `9375`, the private-witness partner support `{3,67}` isn't
realized until term index 906, `(t−a₁)/M ≈ 273`). This is a **new candidate
reformulation of the crux**, structurally different from the size bound `q ≤ a₁`
that both approaches are stuck on:
> **(Conjecture, Early Recruitment Window).** Every prime `q` that ends up in
> `Π = ⋃𝓐_∞` (permanently, i.e. in the true limiting antichain) already appears as a
> factor of some term within a *bounded, `a₁`-determined* initial window (empirically
> `O(1)·M` past `a₁`, in both confirmed cases within `+5`). Equivalently: **no prime
> first introduced "late" (once the sequence is already far past `a₁`) can ever
> survive into `𝓐_∞`.**

This reduces the crux to bounding how many primes can appear in the *first* `O(M)`
integers admissible past `a₁` (a **fixed, finite, `a₁`-computable window**, not an
asymptotic count) — a genuinely different top-level target from either (a) a direct
size bound `q ≤ a₁` (redundant-constraint-antichain's target) or (b) any `A_n`-global
monovariant (already proved impossible). If provable, it would immediately give
`Π ⊆ {primes dividing some c ∈ [a₁, a₁ + K·M]}` for an explicit small `K`, which is
manifestly finite — closing the Crux without ever bounding `q` by `a₁` directly.
**Caveat (be honest): this is based on only 2 confirmed-converged data points** (a
wider scan at only 250 terms produced many false "excess primes" that are transient,
not-yet-dominated artifacts — confirming round-2's warning that under-converged runs
are misleading; I did not have budget to re-run the scan at sufficient depth (~3000+
terms per seed) to get a larger confirmed sample). Flag as a promising but
thin-evidence conjecture, not a load-bearing claim.

**(S3) Mechanism note (structural, not new but sharpened): late-forming small-only
competitors, not late-forming large primes, drive the churn.** Looking at the
transient antichain evolution for `a₁=9375` (before convergence at term 906), the
*churn* — elements entering and leaving `𝓐_k` — is almost entirely driven by
`{3,7,q}`-shaped elements for many different primes `q` cycling through (each
persisting only until a term with support exactly `⊆{3,7}` appears and dominates
*all* of them at once). This matches §8.3 of `redundant-constraint-antichain`
("small companion never activated") exactly, and sharpens it: **domination, when it
happens, dominates a whole family of large-prime supports simultaneously** (one
`{3,7}`-support term kills every `{3,7,q}` for every `q` seen so far in one stroke) —
so churn-counting arguments (D3 in `/tmp/round-2/math-explorer-descent.md`) should
track "does the small-companion set `S` ever get exactly realized" per **distinct
companion set `S`**, not per prime `q`; the number of distinct possible small
companions `S` (subsets of small primes, itself finite once one grants Π's
small-prime part is finite) is the right thing to bound, and this is a smaller,
more tractable combinatorial target than bounding individual large primes directly.

### Candidate technique(s)
- No new named KB technique beyond what's already flagged (pigeonhole, CRT/periodicity,
  invariants/monovariants). The Early Recruitment Window conjecture (S2), if pursued,
  would likely need an explicit finite-window admissibility computation (a
  **constructive/bounded-search** argument, cf. KB "Constructive vs. existence" and
  "Casework/exhaustion" entries) rather than an asymptotic density or size-bound
  argument — a genuinely different proof *shape* (bounded verification over an
  a₁-computable window) from anything the other approaches have tried.

### Cheap-kill candidates
- None that resolve the crux. One useful pruning fact from S1: **do not look for a
  "greedy minimality forces small q" argument in the naive form** — by E1, order
  never pre-empts membership in `A`; this rules out a whole class of naive attacks
  the outliner might otherwise try.
- From S3: track domination **per small-companion-set `S`**, not per large prime `q`
  — cuts the combinatorial bookkeeping since many large primes die in one stroke.

### Knowledge-base entries to use
- **Pigeonhole / extremal principle** (already in use via Anchor + P finite).
- **Constructive / incremental** and **Casework / exhaustion** entries — candidate
  proof shape for S2 if the window bound is pursued (bounded verification, not
  asymptotic counting).
- **Modular arithmetic / CRT** — still the natural tool for formalizing "A is
  eventually periodic," independent of which route closes the Crux.
- No KB entry directly supplies an "early recruitment / bounded window" lemma —
  this would need to be built from scratch if S2 is pursued.

### Analogous past problems (cruxes)
Re-checked `crux_moves_documentation.md`'s subtopic list with this dynamics-specific
lens (searched `processes-and-algorithms`, `pigeonhole`, `invariants-and-monovariants`
again, plus greedy-sequence keyword search). I concur with both prior round reports:
**no crux in the corpus is a genuine analogue of this problem's greedy covering-system
structure.** `aimo-0678` (already used as the seed for `monovariant-witness-descent`)
remains the closest *problem-shape* analogue (greedy/recursive integer sequence,
eventual-periodicity target) but its closing move (an algebraic gcd+lcm freeze
identity) has already been shown not to transplant (per that approach's own R1/R2
notes) — I did not find a different corpus entry that helps the selection-dynamics
angle specifically. No new match to report.

### Prior progress
Unchanged from `current.md`: full reduction to the Crux (Finite Alphabet), sharpened
to `q ≤ a₁` by E1–E3, is certified. This report adds no proof progress; it is
reconnaissance only.

### Dead ends (do not retry)
- **"Greedy minimality (smallest-value selection) directly forbids large q in a
  minimal support"** — checked carefully (S1) and shown to reduce to nothing beyond
  E1: once `m ∈ A`, `m` is guaranteed to appear as a term regardless of what else is
  admissible near it; there is no competitor/pre-emption mechanism to exploit. Do not
  retry this exact framing.
- (Inherited, still valid) **M-threshold confinement** `p|L⇒p≤M` — FALSE, do not
  retry (already certified refuted).
- (Inherited) **No `A_n`-only monovariant can close the crux** — certified obstruction;
  confirms my finding in S1 from a different angle (both show "the state set `A_n`
  alone, or its limit `A`, doesn't encode enough to forbid `q` large — you need either
  the forward-generation history (S2) or the realization mechanics (E1–E3), not a
  snapshot").

### Small-case / intuition notes (all conjectural)
- **(S2, thin evidence, 2 confirmed data points)**: the eventually-persistent large
  "exceedance" prime is recruited essentially immediately (within `~5` of `a₁`, both
  cases at term-index 3) — suggesting a bounded-window reformulation of the Crux is
  more tractable than a direct size bound. Needs a larger confirmed-converged sample
  (≥1000s of terms per seed) to be trusted further; I did not have budget to extend
  the earlier under-converged 250-term scan to convergence for enough seeds. Flag to
  next round's explorer/outliner as worth a dedicated, patient (large-N) numerical
  sweep before building a proof attempt on it.
- **(S3, moderate evidence)**: domination events are per-small-companion-set, not
  per-large-prime — kills whole families of transient large-prime supports at once.
  Consistent across both `375` and `9375` runs' churn traces.
