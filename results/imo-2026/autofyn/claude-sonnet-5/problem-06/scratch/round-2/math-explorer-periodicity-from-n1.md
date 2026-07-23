## imo-2026-06 (lens: periodicity-from-n=1)

### CRITICAL CHECK — answered directly
The problem statement (`problems.jsonl`) reads: *"Prove that there exist positive
integers `T` and `L` such that `a_{n+T}=a_n+L` for every positive integer `n`."*
This is unambiguous: `n` ranges over **all** of `1,2,3,...`, so the claim is
literally "periodic from `n=1`," not "eventually periodic." **There is no cheap
reinterpretation that lets "eventually periodic" (holding only for `n\ge N_0`)
satisfy the statement as written.** Concretely:
- A sequence that is periodic only from some `N_0>1` (a genuine pre-period /
  "rho-shaped" orbit, in the language of iterating a map on a finite state space)
  does **not** become periodic-from-1 merely by enlarging `T` to a multiple of the
  eventual period — the terms `a_1,\dots,a_{N_0-1}` are fixed numbers; they satisfy
  `a_{n+T}=a_n+L` only if they *happen* to already fit the same affine pattern, which
  is a real (unproven) claim, not a formality of choosing `T` bigger.
- So if an approach only establishes "there is `N_0`, `T`, `L` with
  `a_{n+T}=a_n+L` for all `n\ge N_0`," it has **not** yet proved the theorem, full
  stop — the finitely many terms `n<N_0` need their own argument (either (i) show
  `N_0=1` is achievable, i.e. no pre-period, or (ii) directly verify, from the
  problem's own recursive definition, that the same `T,L` — or some other pair —
  also cover `n=1,\dots,N_0-1`, which in general is exactly as hard as (i)).
- `backbone-existence-crt.md`'s framing is correct on this point, and its citation
  check on crux `aimo-0648` is also correct (verified independently below): that
  crux's own **problem statement** only asks to prove "eventually constant," and
  its published solution explicitly discards the pre-period ("discard initial
  terms... we will consider all indices modulo `T` from now on") — it never
  eliminates the pre-period, because the problem it solves doesn't require it. This
  is a real structural difference between IMO-2026-P6 and its closest crux-corpus
  analogue: **P6 asks for a strictly stronger conclusion than the typical
  "eventually periodic/constant" olympiad problem**, so techniques calibrated to
  produce only "eventually" results (including the finite-state-pigeonhole-from-
  `N_0` skeleton implicit in all three round-1 approaches) are not, by themselves,
  sufficient — an extra idea is needed regardless of which approach supplies
  backbone finiteness.

### New computational finding (this round) — strong evidence the gap is real but not a wall
I simulated the greedy process (Python, exact `gcd`-based, no simplifying
assumptions) for every Case-II example on record (`a_1\in\{15,35,77,105,143,65\}` —
confirmed by direct computation that **none** of these has a single prime dividing
every term, so all are genuinely Case II, not Case I) and searched, for each, for
the *smallest* `T` such that `diffs[i]=diffs[i+T]` for **every** `i=0,\dots,n-T-1`
(i.e. checking periodicity of the difference sequence starting at the very first
term, not just eventually):

| `a_1` | `T` (from `n=1`) | `L` |
|---|---|---|
| 15 | 8 | 30 |
| 35 | 34 | 210 |
| 77 | 18 | 154 |
| 105 | 58 | 210 |
| 143 | 64 | 858 |
| 65 | 58 | 390 |

In **every single case where periodicity was found at all**, it held with **zero
pre-period** — i.e. `a_{n+T}=a_n+L` for literally every `n\ge1`, not just eventually.
I searched explicitly for `i` starting at index 0 (i.e. `n=1`), so this is not an
artifact of only checking a tail. (`a_1=247`, the known hard stress case, still
shows no periodicity within 8000 terms — that is the separate, still-fully-open
"backbone finiteness" gap the sibling explorer is scouting, not a counterexample to
the pre-period-freeness pattern; I could not test whether *its* eventual period,
once/if found, would have a pre-period, since no period was found at all.)

This is only **numerical evidence** for 6 data points — not a proof, and not even a
theorem candidate yet — but it is a meaningful data point: it suggests "no
pre-period" is very likely a **true, provable structural feature** of this
specific greedy process (not a coincidence requiring delicate injectivity of an
opaque finite-state map), and that the gap is a genuine missing argument, not a
sign the claim itself might be false or need qualification.

### Distinct openings
1. **(Recommended framing shift) Prove backbone-finiteness + periodicity by a single
   direct strong induction from `n=1`, not via "eventual periodicity by pigeonhole
   from `N_0`, then bootstrap backward."** This is exactly how the two *already
   solved* sub-cases work: Lemma Q and Lemma S′ (`lemmas/lemma-Q-...`,
   `lemmas/lemma-S-prime-saturation-AP.md`) never invoke pigeonhole or a
   finite-state map at all — they strong-induct on `n` starting at the trivial base
   case `n=1`, and periodicity-from-1 falls out for free because the induction
   itself starts at 1. There is no separate "injectivity" step in either proof. If
   Case II's covering/backbone construction can be phrased the same way — i.e. as
   an invariant `I(n)` provable by strong induction from `n=1` that simultaneously
   pins down `rad(a_n)`'s relevant structure AND directly forces the periodic
   recursion — then "periodicity from `n=1`" is not a separate gap to close at all;
   it is automatic. This reframes the periodicity-from-1 sub-gap as **not an
   independent problem**, but as a symptom of choosing a proof strategy
   (pigeonhole-first) that structurally cannot deliver more than "eventually." I
   recommend the outliner treat this as the primary lead for this sub-gap: redesign
   Case II's construction to be a direct induction from `n=1`, mirroring Lemma
   S′'s architecture, rather than trying to patch a pigeonhole-based argument
   after the fact.
2. **(Fallback, if a pigeonhole/finite-state argument is unavoidable) Injectivity /
   permutation route**, as `backbone-existence-crt.md` states it: once a finite
   state space `S` and deterministic transition `F:S\to S` valid **from `n=1`**
   (not `n\ge N_0`) are constructed, showing `F` is injective (equivalently
   bijective, since `S` is finite) immediately gives periodicity from the very
   first state, because every point of a finite set under an injective self-map
   lies on a cycle (no "rho tail"). This is a clean, standard finite-combinatorics
   fact (not found verbatim in the crux corpus for this exact use, see below) but
   its hypothesis — injectivity of `F` — has not been proved or refuted for any
   candidate `F` in this problem. Caution flagged in the source approach file: even
   defining a state space that is valid uniformly from `n=1` (not just eventually)
   is itself unresolved work, since the state would need to encode not just "residue
   mod `L^*`" but a capped record of unmet obligations against specific earlier
   indices (see finding 3 below) — this is a nontrivial state-space design problem,
   not just an injectivity check on an already-agreed state space.
3. **(Diagnostic, not a solution) The `a_1=33` trace shows per-index bookkeeping is
   real, even in solved cases.** In `intersecting-family-covering-construction.md`'s
   own trace: the candidate `44` between `a_4=42` and the next multiple of 3 (`45`)
   is inadmissible **not** because it fails the "obvious" constraint `\gcd(x,a_1)>1`
   (`\gcd(44,33)=11>1`, so it actually *passes* that one) but because it fails
   against `a_3=39` specifically (`\gcd(44,39)=1`). So even in Case I (a single
   saturating prime `p=3`), the *proof* that `a_{n+1}=a_n+p` needs the induction
   hypothesis "all of `a_1,\dots,a_n` are multiples of `p`" (not just `a_1`) to rule
   out intermediate candidates — i.e. it already implicitly uses "periodicity/
   pattern holds for all indices up to `n`," which is exactly why strong induction
   from `n=1` (opening 1) is the natural tool, and why a "state = just current
   residue" Markov reduction is too lossy in general: admissibility genuinely
   depends on the full history of which primes have appeared, not a bounded window.
   This is evidence *for* opening 1 (build the invariant to directly carry the
   "all prior terms fit pattern `P`" fact forward) and evidence *against* trying to
   compress state further before proving something is periodic.

### Candidate technique(s)
- Strong induction from `n=1` with an invariant strong enough to (a) pin down
  `\mathrm{rad}(a_n)`'s relationship to a fixed finite backbone `H` and (b) directly
  force the recursive step `a_{n+1}=a_n+d` for the right periodic `d`, mirroring
  Lemma Q / Lemma S′'s architecture (KB: no named external theorem here — this is
  the problem's own recursive structure, exploited directly, as those two lemmas
  already do).
- Finite-state dynamics / functional-graph theory: "injective self-map of a finite
  set has no pre-period" (standard fact, not sourced from a specific KB entry or
  crux — flagged in `backbone-existence-crt.md` as the fallback target, still open).
- Bezout-combination backward propagation (crux `aimo-0648`'s third move) — **checked
  and confirmed inapplicable** to the pre-period-elimination question (it only
  propagates a property backward *within* an already-agreed periodic regime, and
  even its own source problem never eliminates the pre-period, matching this
  problem's `problems.jsonl` vs. crux corpus statement precisely).

### Cheap-kill candidates
None obvious for closing this particular sub-gap outright; it is genuine remaining
work. (The literal-reading check above **is** a cheap kill of the *hope* that this
sub-gap could be dissolved by re-reading the problem statement — confirmed that it
cannot: the statement really does demand `n=1,2,3,\dots` with no exception, and
"eventually periodic" is a strictly weaker, non-equivalent claim for this problem.)

### Knowledge-base entries to use
Nothing in `knowledge_base.md` was found specific to "eventual-to-full periodicity
bootstrapping" or "injective self-maps of finite sets have no pre-period" as a named
entry — this is elementary finite-combinatorics, not a named external theorem, so
any approach invoking it should state and prove it inline (one paragraph) rather
than cite a KB entry that doesn't exist for it. (Recommend the outliner not
instruct a builder to "cite KB X" here — there isn't one; it should be proved from
scratch as a two-line fact about maps on finite sets, if this route is taken.)

### Analogous past problems (cruxes)
- **`aimo-0648`** (number_theory, `sequences-and-recurrences` — bounded state via
  floor-average recurrence, finite-state pigeonhole ⟹ eventually periodic, then
  Bezout-combination of step sizes to force a max-value property backward *within*
  the periodic regime). Genuinely the closest structural analogue in the corpus
  (bounded/finite-state greedy-like recurrence ⟹ eventual periodicity), but **its
  own problem statement only demands "eventually constant"** and its official
  solution explicitly discards the pre-period rather than eliminating it — so its
  crux move does **not** transfer to this problem's stronger "periodic from `n=1`"
  requirement. Already flagged (and independently re-confirmed here) by
  `backbone-existence-crt.md`; do not resurrect this as a fix for the periodicity-
  from-1 gap.
- **`aimo-0134`** (number_theory, `sequences-and-recurrences` — recovering an
  original sequence's eventual constancy from an eventually-constant running
  average via a difference identity). Surface-level similarity ("transfer eventual
  behavior back to the original sequence") but on inspection this is a different
  mechanism (algebraic identity relating two sequences, not backward-propagation of
  periodicity across a genuine transient) and its target conclusion is also only
  "eventually constant." Not a genuine match; mentioning only to record it was
  checked and ruled out.
- **`aimo-0421`** (already in use by `intersecting-family-covering-construction.md`
  for Lemma R) — pigeonhole on a fixed gcd taking finitely many values. Relevant to
  backbone finiteness (the sibling gap), not to this periodicity-from-1 gap
  specifically.
- **`aimo-0678`** (IMO Shortlist 2015 N4 — flagged by a prior round's memory note as
  the closest structural sibling: two coupled sequences via `gcd`/`lcm`, a
  monovariant `w_n` forcing boundedness, then a finite-state
  `(a_n, b_n \bmod M)` pigeonhole argument for eventual periodicity). Checked its
  **exact problem statement** here: "there exist integers `N\ge0` and `t>0` such
  that `a_{n+t}=a_n` for all `n\ge N`" — i.e. this sibling problem *also* only
  demands eventual periodicity, not periodicity from `n=0`/`1`. Its official
  solution never removes the pre-period either (the monovariant `w_n` is merely
  shown non-increasing, hence eventually constant from some `N` on — the indices
  before `N` are simply never revisited). This is now the **second** independent
  confirmation (after `aimo-0648`) that "prove eventually periodic, don't worry
  about the transient" is the standard shape of this problem family in the corpus,
  and that IMO-2026-P6's literal demand for periodicity from `n=1` with no
  exception is the unusual, extra part — reinforcing that no existing crux
  technique in the corpus is a plug-in fix for this sub-gap; it needs a
  problem-specific argument (most promisingly, opening 1 above).
- No crux in the corpus was found that specifically bootstraps "eventually periodic"
  to "periodic from the very first index" for an unbounded, strictly-increasing,
  greedily-defined sequence. This absence is itself informative (see "CRITICAL
  CHECK" section above): it suggests this exact difficulty is a genuine, somewhat
  unusual feature of IMO-2026-P6 relative to typical corpus problems of this shape,
  not a routine technique that's merely missing from the sample.

### Prior progress
See `current.md` and `backbone-existence-crt.md` Section 6 (summarized above under
"CRITICAL CHECK"). No approach has closed this sub-gap. The furthest honest
statement of it: *"if a finite state space and transition map `F` valid from `n=1`
can be constructed, and `F` is injective on it, periodicity from `n=1` follows;
injectivity is neither proved nor refuted."*

### Dead ends (do not retry)
- Using crux `aimo-0648`'s Bezout-combination device to propagate periodicity
  backward across the transient into `n<N_0` — checked twice now (once by
  `backbone-existence-crt.md`, once independently here against the crux's own
  official solution text) and confirmed inapplicable: the device only works
  *within* an already-agreed periodic regime, and the source problem's own solution
  never removes its pre-period.
- Assuming "eventually periodic" as found via finite-state pigeonhole from some
  `N_0` already satisfies the problem statement — confirmed false by a literal
  reading of `problems.jsonl`'s statement (`n` ranges over all positive integers,
  no exception clause); any approach that stops at "eventually" has not proved the
  theorem regardless of how rigorous the eventual-periodicity argument is.

### Small-case / intuition notes (conjectural)
- Computed (this round, exact integer arithmetic, no shortcuts) for all 6 confirmed
  Case-II examples on record (`a_1\in\{15,35,77,105,143,65\}`): every one that
  exhibits periodicity at all exhibits it **with zero pre-period**, i.e. from `n=1`
  literally. This is 6/6 supporting evidence (labeled conjecture, not proof) for
  the belief that "no pre-period" is a genuine structural theorem about this
  process, reachable by a from-scratch argument (most plausibly the direct-
  induction-from-`n=1` route, opening 1 above) rather than a delicate injectivity
  fact about an a posteriori finite-state map.
- `a_1=247` still shows no detectable periodicity within 8000 simulated terms
  (consistent with prior rounds' report of no periodicity within 15000 terms) — this
  is the separate, still fully open "backbone finiteness" gap (growth of the prime
  set / non-concentration), not evidence against the pre-period-freeness pattern,
  since no period exists yet to check for a pre-period.
- The `a_1=33` trace (Case I, already solved) shows admissibility rejections can
  hinge on a *specific* earlier index other than `a_1` (e.g. `a_3`, not `a_1`),
  reinforcing that any direct-induction-from-`n=1` invariant for Case II will need
  to track more than "does `x` share a factor with `a_1`" — it needs the full
  inductive hypothesis "the pattern holds for all of `a_1,\dots,a_n`" — exactly the
  strength strong induction naturally provides, and exactly what a compressed
  "residue mod `L`" Markov state would lose.
