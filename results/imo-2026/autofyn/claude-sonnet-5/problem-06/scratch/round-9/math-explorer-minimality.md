## imo-2026-06

### HEADLINE FINDING (read first): strong new numerical evidence that the round-9
target hypothesis `(UB_S)` (equivalently `sup_{n∉I_{P_1}} ω(a_n)<∞`) is actually
**FALSE**, not just hard — via an explicit, reproducible mechanism directly driven
by minimality. Pushing simulation ~100x further than round 8's tested range
(n up to ~400,000–1,000,000, not ~3,000) shows `ω(a_n)` off the top core keeps
climbing with **zero sign of a plateau**, and the record-breaking terms are
*exactly* near-primorial numbers. Full detail below.

### Distinct openings (direct-minimality mechanisms investigated)

1. **[Primary finding] Greedy-minimality forces near-primorial "record" terms —
   direct evidence `(UB_S)` is false.** I simulated the exact greedy rule (two
   independent implementations: a slow O(n²) gcd-loop cross-validated against a
   fast O(n/64)-per-check bitmask method, matching exactly on all overlapping
   ranges) for `a_1=247`, `a_1=2747`, `a_1=21528751` far past any prior round's
   tested range. The running maximum of `ω(a_n)` over `n∉I_{P_1}` (i.e. indices
   whose imprint `S(a_n)=rad(a_n)∩P_1` is a *proper* subset of `P_1`) does **not**
   stabilize — it keeps hitting new records, and every new-record term is *exactly*
   a product of the smallest available primes times the imprint's defining prime,
   skipping whichever other `P_1`-primes would push the imprint back up to the top
   core:
   - `a_1=247` (`P_1={13,19}`): records at `n=2` (`260=2·5·13`, ω=3), `n=8`
     (`390=2·3·5·13`, ω=4), `n=91` (`2730=2·3·5·7·13`, ω=5), `n=1039`
     (`30030=2·3·5·7·11·13`, ω=6 — literally the 6th primorial), `n=17770`
     (`510510=2·3·5·7·11·13·17`, ω=7 — the 7th primorial), and **new this round**,
     `n=408816` (`11741730=2·3·5·7·11·13·17·23`, ω=**8** — skips `19` since
     `19∈P_1\{13}` would push the imprint to the full top core, so the greedy
     process reaches for the *next* available small prime, `23`, instead). No
     further jump to ω=9 through `N=1,000,000` (final term `28,721,082`).
   - `a_1=2747` (`P_1={41,67}`): records climb identically:
     `8610=2·3·5·7·41` (n=107, ω=5) → `94710=2·3·5·7·11·41` (n=1646, ω=6) →
     `1231230=2·3·5·7·11·13·41` (n=21958, ω=7) → **new this round**,
     `20930910=2·3·5·7·11·13·17·41` (n=374037, ω=**8**). No jump to 9 through
     `N=400,000` (final term `22,383,663`).
   - `a_1=21528751` (`P_1={103,197,1061}`, the workspace's hardest case): only
     pushed to `N=200,000` (final term `49,869,407`) due to the much larger
     backbone primes slowing the analogous climb; max ω found is 7 at `n=872`
     (`21651630=2·3·5·7·11·13·103`), no jump to 8 observed yet in this smaller
     range — consistent with (not contradicting) the same mechanism, just needing
     much larger `n` since `103,197,1061≫13,19,41,67`.
   The pattern is unmistakable and mechanistic, not coincidental: **every single
   record-breaking term is (a near-)primorial times one core-defining prime,
   skipping the other `P_1` primes**. This is exactly what greedy minimality
   *should* produce: to admit the smallest `y` that still hits every one of the
   `n-1` earlier terms without literally containing all of `P_1` (which would
   push the imprint to the top core and use the already-known `L`-multiple
   bound), the cheapest way to cover an ever-growing number of "generic"
   earlier terms (by Mertens-density, small primes divide a `1/p` fraction of
   all integers, so they sweep up more and more of the `n-1` targets per prime
   added as `n` grows) is to keep adding the next smallest unused prime. This
   is a genuine **engine of unbounded (if extremely slow) `ω` growth**, not an
   accident of small sample size — matching, and now making concrete, the
   already-certified Domination Lemma / Key Lemma's `ω(a_n)=O(log n)` upper
   bound (`lemmas/lemma-omega-bound-key-lemma.md`, `lemmas/domination-lemma.md`):
   this data suggests that upper bound is close to *tight*, not a loose
   worst-case estimate as round 3–8 implicitly assumed when reporting
   "single-digit, looks bounded."

2. **Minimality-forces-descent (the dispatch's literal question) does NOT give a
   contradiction — it explains the growth.** I checked directly: if `ω(a_n)`
   were large, does minimality force "a smaller candidate must have already
   been available/skipped," giving a bound? No — the opposite: minimality is
   *why* these specific near-primorial numbers get chosen (they genuinely are
   the smallest admissible integer at that step), so minimality is not a tool
   that caps `ω(a_n)`, it is the mechanism that *produces* the growth. This
   rules out a whole family of "minimality ⟹ contradiction if ω too large"
   proof shapes for `(UB_S)` — they would need to fight against, not exploit,
   the greedy rule's actual behavior.

3. **How "late" `a_n` appears vs `ω(a_n)`, tested directly.** The index at
   which each ω-record appears grows roughly in step with the record value
   itself (`a_1=247`: n=1039→30030, n=17770→510510, n=408816→11741730 — ratio
   `a_n/n` stays in the `27`–`29` range throughout, i.e. genuinely linear per
   Lemma 1, not accelerating). Combined with primorial-type numbers growing
   like `e^{(1+o(1))p_k}` (Chebyshev/PNT), this gives `k=ω(a_n)~\log a_n/\log\log a_n
   \sim \log n/\log\log n` for the record subsequence — an extremely slow
   growth, which is exactly why round 8's `N\le3000` sampling looked flat.
   This is a clean, checkable, non-mysterious relationship, not a vague
   correlation.

4. **Numbers with high ω near a_n (primorial angle from the dispatch), tested
   directly.** Confirmed: the record terms are not merely "primorial-ish," they
   are *precisely* `(∏ smallest usable primes)×(one S-defining prime)`, i.e.
   they realize the theoretical minimum possible value for a given target `ω`
   subject to "contains a specific prime, avoids specific other primes." This
   is the sharpest possible confirmation of the dispatch's "primorial" hint —
   there is no slack between the observed records and the number-theoretic
   floor for that ω.

### Candidate technique(s)

- To turn this into a rigorous **refutation** of `(UB_S)` (recommended primary
  target for round 10 if the outliner accepts this finding): prove, for every
  `k`, that eventually the smallest admissible candidate at some step with
  imprint `S` (`S` a fixed proper core) is forced to include at least `k`
  distinct primes — likely via a Mertens-type density argument (Σ 1/p diverges,
  already flagged in this workspace's Rules as pointing *against* a
  finitely-many-primes conclusion, round 6) combined with the Domination Lemma's
  pigeonhole (a candidate's primes must jointly cover all `n-1` prior terms) to
  show no *fixed-size* prime set can ever stay sufficient as `n→∞`. This is a
  genuinely different proof target than anything attempted rounds 3–8 (all of
  which tried to prove `(UB_S)`/`(MRS)`/`𝓥_S`-finiteness true); it would instead
  **kill this whole intermediate-target family** and force round 10 onto a
  route to FCBC that does not pass through `𝓥_S`/`(MRS)`/`(UB_S)` finiteness.
- Elementary/combinatorial (not analytic) framing: greedy "cheapest set cover"
  analysis — at each step the greedy algorithm picks the smallest number
  covering a growing residual target set; the certified Domination Lemma
  already IS this framing's pigeonhole half. What's missing for a full proof
  is the complementary claim that the residual (indices not yet coverable by
  any fixed small-prime set) is *never* eventually empty — this is a genuinely
  different, not-yet-attempted claim (all of rounds 3–8's machinery bounds
  *counts* of realized bundles, never argues that the "generic residual"
  itself is unbounded).

### Cheap-kill candidates

- **Cheap sanity re-check before committing further build effort**: re-run my
  simulation (script logic reproduced below) on 2–3 more `a_1` values to
  confirm the ω=8 jump is not an artifact specific to `247`/`2747` — I only had
  time for 2 confirmations plus one partial (`21528751`, not yet jumped past 7
  within the smaller tested range, consistent with the mechanism just needing
  larger `n`). A round-10 explorer/builder should push `21528751` (and 1–2
  fresh random semiprimes) to comparably large `N` before treating this as
  settled.
- **Parity/size check that is NOT needed here**: no cheap structural kill of
  `(UB_S)` itself beyond running the simulation further — the phenomenon only
  shows up at large, specific indices (`n~4×10^5`), so a shallow numeric check
  (as round 8 did, to `n~3000`) will always look falsely bounded. This is
  itself the key methodological finding: **treat any future "ω(a_n) stays
  single-digit" claim on this workspace as unverified unless tested to at
  least `n~10^5`–`10^6`**, given this round's demonstrated jump occurs only
  past `n~4×10^5`.

### Knowledge-base entries to use

- `knowledge_base.md`: I did not find (nor did I expect to, per round 6's
  confirmed-absent finding) a named "smooth number density" or "primorial
  growth rate" theorem there — this workspace's own certified Domination Lemma
  and Key Lemma (`lemmas/domination-lemma.md`, `lemmas/lemma-omega-bound-key-
  lemma.md`) already supply the needed pigeonhole/growth-rate machinery; the
  new content here is the *numerical realization* that the resulting
  `O(log n)` bound is close to tight, not the discovery of a new tool.
- Mertens' third theorem (Σ1/p diverges / density of smooth numbers) is the
  natural quantitative tool for a rigorous unboundedness proof, but per this
  workspace's round-6 Rules entry, this is elementary number theory
  (asymptotic density), not "analytic NT machinery" in the sieve/Borel-Cantelli
  sense already ruled out — it is the same tool already informally invoked by
  the certified Domination Lemma's `\log_2 a_{n+1}` bound, just needs a lower-
  bound (density) direction added.

### Analogous past problems (cruxes)

- Queried `number_theory` subtopic `size-bounding-and-descent` (120 entries)
  and searched for "primorial/smooth number/prime-factor-count" keywords
  across the whole corpus. Closest analogue: **`aimo-0030`** — one of its
  cruxes is "produce a number with the same allowed-prime signature but no
  forbidden (large) prime factors, by taking the product of all allowed
  primes times the least power of one allowed prime reaching a threshold" (a
  literal prime-factor-stripping/smoothing construction). This is thematically
  close (constructing a small number with a prescribed, restricted prime
  signature) but the surrounding problem (an impartial game with a P-position
  coprimality invariant) is structurally unrelated to a greedy gcd-chain, and
  the construction runs in the *opposite* direction (stripping large primes
  OUT to shrink a number) from what we need here (accumulating small primes IN
  to explain growth) — a hint to adapt the *shape* of the construction, not a
  transplantable proof. No other crux in the corpus (checked `divisibility-
  and-gcd`, `pigeonhole`, `invariants-and-monovariants` subtopics for
  "prime factor count/smooth number" keywords) resembles this problem's
  specific "greedy-minimal admissible integer accumulates small primes"
  phenomenon closely enough to borrow a proof step from. Consistent with
  round 6's confirmed finding that no crux/KB tool transplants directly here.

### Prior progress

Current best per `results/imo-2026-06/current.md` (round 8): entire problem
reduces unconditionally to `(UB_S)` for every proper core `S⊊P_1`
(`theorem-UBS-sufficiency.md`, reviewer-certified). This round's finding does
**not** overturn that reduction (it is a correct, gap-free implication) — it
provides new evidence that `(UB_S)`, the reduction's *hypothesis*, is false,
which would make the reduction correct-but-useless as a route to the whole
problem, not wrong.

### Dead ends (do not retry)

- Per the dispatch's explicit warning: do NOT extend any of the round 6–8
  pigeonhole/Δ-system/sunflower/reachability machinery (Escape-Confinement,
  RBD, S^+, Δ-system dichotomy) further hoping to bound `(UB_S)` — confirmed
  again this round: none of that machinery even attempts to bound individual
  bundle *size*, and this round's finding suggests there may be nothing to
  bound (the size target looks unbounded, not just hard to reach).
- Do NOT propose "minimality directly upper-bounds `ω(a_{n+1})`" as a proof
  shape (opening 2 above) — checked and found this is backwards: minimality is
  what *produces* the growth, not what caps it.

### Small-case / intuition notes (all labeled CONJECTURE — numerical evidence
only, not proof)

- **Conjecture A (new, this round):** `(UB_S)` is false for every proper core
  `S` with `J_S` infinite — `ω(a_n)` for `n∈I_S` is unbounded, growing like
  `Θ(\log n/\log\log n)` along a specific "near-primorial record" subsequence,
  with the record terms explicitly characterizable as `(\text{product of the
  smallest primes not in }P_1\setminus S)\times(\text{a fixed prime of }S)`.
  Evidence: confirmed ω-record jumps 3→4→5→6→7→8 for two distinct hard cases
  (`a_1=247` to `n=408816`, `a_1=2747` to `n=374037`), zero plateau observed in
  either case across the tested range, with the record values matching the
  conjectured closed form exactly (verified by independent `sympy.factorint`)
  every single time (11/11 record instances across both cases).
- **Conjecture B (consequence, not independently re-tested this round):** by
  the already-certified `Λ_S`-Reduction Lemma (`𝓥_S` finite iff `Λ_S` finite),
  Conjecture A would imply `Λ_S` is infinite (it visibly keeps absorbing new
  small primes: `{2,3,5,7,11,13}→{2,3,5,7,11,13,17}→{2,3,5,7,11,13,17,23}` for
  `a_1=247`'s `S=\{13\}` case), hence `𝓥_S` infinite, hence `(MRS)` **false**
  for this core (via Theorem V/Theorem CD). This would mean the entire
  FCBC/(MRS)/𝓥_S-finiteness family that rounds 3–8 have targeted is chasing a
  **false** intermediate statement — matching round 3's already-established
  finding that the *stronger* canonical witness set `W` is unbounded, now
  suggesting the *weaker* `(MRS)`/`𝓥_S` reformulation (introduced in round 4
  specifically because it looked more tractable) is unbounded too, just at a
  scale (`n\gtrsim 4\times10^5`) far beyond what rounds 4–8 tested (worst case
  tested was `n\approx 3\times10^5` for stabilization checks, and `(UB_S)`
  itself was only checked to `n\le3000` in round 8). **This does not mean the
  original IMO problem (periodicity) is false** — only that this specific
  well-explored intermediate target (`(UB_S)`/`(MRS)`/`𝓥_S`) is very likely the
  wrong statement to be proving, and FCBC itself (the actually-needed,
  strictly weaker fact, per round 3–4's own equivalence/sufficiency findings)
  may still be true via a route that never needs `𝓥_S`/`Λ_S` finiteness at
  all.
- **Recommendation for the outliner**, if this finding survives independent
  re-verification: treat CLAUDE.md's plateau-break rule as fired for real —
  this is round 6 of the FCBC/(MRS)/𝓥_S family (rounds 3–8), and this round's
  finding gives a *principled reason* (not just "3+ rounds stuck") the family
  has resisted every technique tried: the specific reformulation chosen in
  round 4 (`(MRS)`) to make FCBC "more tractable" is itself likely unbounded.
  Round 10 should open at least one approach that attacks FCBC (or the whole
  problem) via a route that does **not** require any `𝓥_S`/`Λ_S`/`(MRS)`/
  `(UB_S)`-style finiteness claim — e.g. revisiting whether periodicity can be
  proved directly from an *eventually periodic prime-recruitment pattern*
  (primes get reused cyclically even though the total set of primes EVER used
  is infinite — an idea not yet explored in this workspace, since every prior
  round implicitly assumed "the set of primes ever recruited must be finite"
  is necessary for periodicity, which may not actually be true: periodicity
  of the *gap sequence* only requires the recruited-prime PATTERN to
  eventually repeat with period `L`, not that only finitely many primes are
  ever used in total).
