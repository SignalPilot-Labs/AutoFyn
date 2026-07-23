## imo-2026-06

### Scope of this route
Attacked the cross-bucket-domination / escape-recursion-depth gap directly
(the sole remaining content of `forced-primes-well-ordering`'s §G, independent
of whatever the sibling "bundle-counting" explorer finds). Goal: find a
well-founded quantity, distinct from `|S|` and bundle size `|Q|` (both
foreclosed), that bounds escape-recursion depth. All numerics below are fresh
(own generator, `/tmp/round-8/gen_fast.py`, cross-validated term-for-term
against the existing cached sequences before trusting any extension —
`a_1=2747` matched the cached `/tmp/round-7/seq_2747.json` exactly on the
first 500 terms, `a_1=21528751` matched `/tmp/round-7/seq_21528751_30k.json`
exactly on the first 2000 terms). Extended `a_1=2747` to `n=40000` and
`a_1=21528751` to `n=60000` (well past the two documented depth-3 points at
`n=19617`/`n=30017`), plus fresh runs on `a_1=1517=37·41`, `a_1=4087=61·67`,
`a_1=4199=13·17·19` (5 distinct `a_1` total, satisfying the dispatch's "≥3
more diverse" requirement). Independently reconfirmed both documented
depth-3 escapes exactly: `a_2747_{19617}=1{,}100{,}274=2·3·7·17·23·67` and
`a_21528751_{30017}=25{,}781{,}784=2^3·3·7·19·41·197` — exact match to
`current.md`'s corrected numbers, both confirmed with fresh `sympy.factorint`.

### Distinct openings
1. **Tested, and refuted, the most natural "root the Recruiter-Alignment
   pattern in an already-certified finite object" candidate**: identify the
   empirical depth-bounding set `W` (from `forced-primes-well-ordering`'s
   §G Step 3, `d=3-|κ∩W|`) with `D_S\P_1` — the object made finite by the
   already-certified **Single-Companion Finiteness Lemma**
   (`lemmas/lemma-lambda-S-reduction-and-single-companion-finiteness.md`,
   `D_S:=⋂_{j∈J_S}rad(a_j)`, `J_S` = S-*avoiding* indices). Computed `D_S`
   directly for the two documented hard cores (`a_1=2747,S={67}`;
   `a_1=21528751,S={197}`) using the *full* available `J_S` (19203 and
   31295 members respectively, far beyond any prior round's sample):
   **`D_S\P_1=∅` (trivial) in both cases** — not `{2,3,7}` as the recruiter
   pattern would need. This candidate is **refuted by direct computation**,
   not merely unconfirmed.
2. **Found the correct already-certified object instead: the "extended
   imprint" `S^+:=⋂_{i∈I_S}rad(a_i)`** (self-intersection over the core's
   *own* matching class, not the avoiding class `J_S`) — this is **not new**;
   it is the exact object from round 3's Generalized Lemma C file
   (`lemmas/lemma-C-generalized-subsequence.md`), already proved finite
   (whenever `I_S` is infinite) by the identical Generalized Lemma C
   stabilization mechanism already certified for `D_S`. Its previously
   recorded use (`S^+∩S'^+≠∅` as a direct FCBC covering witness) was
   **refuted** in round 3 on `a_1=247` — but that is a *different, stronger*
   claim than the one tested here.
3. **New (not previously stated) elementary consequence of `S^+`, verified
   numerically to be the real driver of the Recruiter-Alignment pattern**:
   since `S⊆rad(a_i)` and `S^+⊆rad(a_i)` for **every** `i∈I_S` by
   definition, any bare value `C` **exactly** realized as some `a_i`,
   `i∈I_S`, automatically satisfies `C⊇S^+` (one line: `C=\mathrm{rad}(a_i)
   ⊇S^+`). So `S^+\P_1` is a **rigorous necessary lower bound** on what any
   escape-recursion dominator must contain — a genuinely different,
   already-certified-machinery-backed candidate from both the refuted `D_S`
   guess and the unproven/refuted global `W(a_1)` (Hypothesis (GW)).
4. **Stress-tested this across 8 core/bucket-family instances spanning all
   5 `a_1` values**: computed `S^+\P_1` directly (fresh code,
   `/tmp/round-8/analyze_dsat.py` + inline scripts) and compared against the
   actual extra primes recruited by the minimal realized dominator of every
   populated coarse bucket:

   | `a_1` | `S` | `\|I_S\|` | `S^+\setminus P_1` | matches observed recruits? |
   |---|---|---|---|---|
   | 2747 | {67} | 777 | {2,3,7} | **exact**, 4/4 buckets, depths 1,2,2,3 |
   | 21528751 | {197} | 1017 | {2,3,7} | **exact**, 4/4 buckets, depths 1,2,2,3 |
   | 1517 | {37} | 1684 | {2,3} | **exact**, 4/4 buckets, depths 0,1,1,2 |
   | 4199 | {13} | 2326 | {2} | **exact**, matches |
   | 4199 | {19} | 1515 | {2,3} | **exact**, matches |
   | 21528751 | {1061} | 19 | {2,3,7} | **partial**: `S^+` correctly predicted as a *subset* of every dominator, but both of the 2 populated buckets needed one *extra* prime (`11`) beyond `S^+\P_1` — depth exceeds the `S^+`-only prediction by exactly 1 in both cases |

   7 of 8 tested instances match `S^+\P_1` **exactly** (as a tight
   explanation, not just a lower bound); the 8th (`S={1061}`, the sparsest
   class tested, only 19 realized members in 60000 terms) shows `S^+`
   correctly as a *necessary* subset but **not sufficient** — an honest,
   real gap, not a computational error (double-checked the dominator
   factorizations by hand: `a_?` with radicals `{2,3,7,11,1061}` and
   `{2,3,7,11,19,1061}`, both containing `S^+={2,3,7}∪{1061}` properly plus
   the extra `11`).
5. **This refines, rather than repeats, the already-refuted global
   Hypothesis (GW)**: `S^+` is *per-core*, not per-`a_1` — it happens to
   equal `{2,3,7}` for **both** `S=197` and `S=1061` in `a_1=21528751`
   here, but there is no proof it must coincide across cores in general
   (only 3 singleton cores exist for `a_1=21528751`'s `P_1={103,197,1061}`,
   and the third, `S={103}`, could not be tested this round — no
   disjoint-companion witness pair found for it even at `n=60000`, exactly
   the `S={103}`/`S={61}`/`S={41}`-style structural degeneracy already known
   from round 6/7).

### Candidate technique(s)
The `S^+` (extended imprint) necessary-condition lemma above is a genuine,
cheap, already-provable (3 lines from the already-certified Generalized
Lemma C, applied to `I_S` instead of `J_S` — a substitution not previously
made explicit for this purpose) new fact, **but it does not close the depth
gap**: it gives a lower bound on dominator content, matches exactly in 7/8
tested instances, but the 8th shows genuine extra recruitment beyond `S^+`
can and does occur. **Recommend**: certify the one-line "`S^+`-necessity"
observation as a cheap new lemma (near-zero additional proof burden, reuses
100% certified machinery), but do **not** claim it bounds depth — report
honestly as a partial explanatory mechanism, precisely mirroring this
workspace's history of partial-but-not-closing findings. The natural next
question (not attempted this round, flagged for the outliner) is: is the
*extra* recruitment beyond `S^+` (the `S={1061}` phenomenon) itself bounded
by a second-order finite object — e.g. `S^{++}` := the extended imprint of
the coarse-bucket-*restricted* subclass (only `I_S` members whose radical
also contains the specific bucket `κ`)? Not tested this round due to time;
worth a focused follow-up given the strength of the 7/8 match.

### Cheap-kill candidates
- **`D_S` (avoiding-index self-intersection) as the recruiter set: killed
  outright by direct computation** (finding 1 above) — do not resurrect for
  this purpose. `D_S` remains valid for its *original* purpose
  (Single-Companion Finiteness), just does not explain escape depth.
- **König's-lemma / compactness framing (per dispatch's suggestion,
  checked)**: does not give a shortcut. To use König's lemma productively
  one needs "the confinement-branching tree has no infinite path" as an
  *input*; `forced-primes-well-ordering`'s own §G Step 4 already
  demonstrated the **full** branching tree (branching on every offered
  prime, not just the realized one) does **not** visibly terminate to depth
  6 on a concrete instance (new large, unrelated primes introduced at every
  level). König's lemma cannot supply the missing "no infinite path" fact
  without already assuming what is to be proved — same status as the
  already-certified Pool Lemma (`lemmas/lemma-W4-pool-lemma-tree-Pi.md`,
  proved an *equivalence* to FCBC, not a simplification). Re-confirmed this
  framing offers no independent leverage here.
- **Global antichain membership check**: computed the *partial* (not yet
  frozen) global minimal-radical antichain union `H` for `a_1=21528751` at
  `n=32000`: `H\P_1={2,3,5,7,11,23,97}` — this **contains** both observed
  per-core recruiter sets (`{2,3,7}` for `S=197`, `{3,7,11}` for `S=1061`
  including the extra `11`). This confirms (a fresh, independent check) that
  recruited primes are drawn from the *same* evolving, only-empirically-known
  finite backbone the whole population has chased since round 1 — i.e. the
  escape-depth phenomenon **is not independent of** global FCBC/`(MRS)`, it
  is a local shadow of it, exactly as `forced-primes-well-ordering`'s own
  §G Step 4 concluded. No new leverage from this angle either — reported as
  a confirmed dead end for finding an *independent* well-founded quantity,
  though `S^+` (finding 3 above) is a genuine partial exception since it is
  provably finite *without* assuming FCBC.
- **No depth-4 instance found** despite pushing both documented depth-3
  cases 2–4× past their discovery index (`a_1=2747` to `n=40000`,
  double the discovery index `19617`; `a_1=21528751` to `n=60000`, double
  `30017`) — consistent with (but, per the round-7 "never trust small-sample
  timing" lesson, absolutely not proof of) depth staying `≤3`.

### Knowledge-base entries to use
None beyond what the workspace already cites (Generalized Lemma C, Lemma P′,
Permanent-Inadmissibility) — no new `knowledge_base.md` entry located this
round; this route is fully internal to already-certified project machinery.

### Analogous past problems (cruxes)
Ran a fresh, targeted keyword scan (`nested hitting set`, `confinement`,
`recursion depth`, `escape`, `hitting set`, `well-ordering`) across the full
2434-entry corpus (`past_crux_moves_database.json`), restricted to
`domain=number_theory`. 5 hits (`aimo-0179`, `aimo-0356`, `aimo-0360`,
`aimo-0577`, `aimo-0900`) — read all 5 `technique`/`how_used` summaries;
**none are genuinely analogous**: they concern involution pairing, a
divisor-quotient size bound, exhaustive divisor enumeration, a permutation
inversion on a finite invariant set, and a residue class closed under
operations — none has the "recursive/nested confinement-depth" shape this
gap needs. Confirms (a third independent time, per `current.md`'s own
tracking) that no external crux-corpus technique addresses this specific
gap shape.

### Prior progress
Unchanged in substance from `current.md`'s Round 7 update: Escape-Confinement
Lemma certified (`lemmas/lemma-escape-confinement.md`); real depth `≤2`
claim corrected to depth-3-confirmed (two instances); Recruiter-Alignment
pattern (`d=3-|κ∩W|`) verified empirically but conditional on an unproven `W`.
This round's contribution: identifies `W` (for the two originally-tested
cores) as the already-certified-finite `S^+\P_1` (extended imprint,
7/8 exact match across a broadened 5-`a_1` test), and finds the one
concrete instance (`S={1061}`) where this identification is incomplete,
narrowing — but not closing — what remains open.

### Dead ends (do not retry)
- `D_S` (avoiding-class intersection) as the depth-bounding recruiter set —
  refuted by direct computation this round (finding 1).
- König's-lemma/compactness route to depth-boundedness without first
  resolving "does the confinement tree have an infinite path" — no
  shortcut exists; re-confirms `forced-primes-well-ordering`'s own §G
  Step 4 finding, from a different angle (dispatch-requested check).
- Global Hypothesis (GW) (a single `a_1`-wide recruiter set) — already
  refuted for nested cores (round 7); this round adds a second,
  independent data point at the *singleton*-core level (`S=1061` needs an
  extra prime `11` beyond `S=197`'s recruiter set, even though both cores'
  `S^+` values happen to coincide) — do not assume a single fixed `W(a_1)`
  works for every core, singleton or not.

### Small-case / intuition notes (all explicitly conjectural)
- Depth appears to stay `≤3` in every one of ~17 populated coarse buckets
  now checked across 5 `a_1` values (up from round 7's 13), including after
  pushing the two known-hardest cases 2–4× past their depth-3 discovery
  index — real but non-proof evidence.
- The `S^+` (extended-imprint) necessary-condition mechanism is the single
  most concrete, provable, *new* partial result from this route: it is
  cheap to certify, reuses only already-certified machinery, and explains
  7/8 tested recruiter sets exactly — but the workspace should not overclaim
  it as a depth bound; the `S=1061` counterexample to *tightness* (not to
  necessity) is real and should be reported honestly if this lemma is
  written up.
- Sparse classes (`|I_S|` in the tens, e.g. `S=1061`'s 19 members through
  `n=60000`) are exactly where `S^+`'s prediction becomes incomplete —
  plausibly because a genuinely *new* recruited prime (`11`) is not yet
  forced to appear in literally every class member (would need much more
  data, or a smarter argument, to know if `11` is "structural" or
  coincidental for this class) — worth flagging as the frontier case for
  next round's numerics if this route is pursued further.
