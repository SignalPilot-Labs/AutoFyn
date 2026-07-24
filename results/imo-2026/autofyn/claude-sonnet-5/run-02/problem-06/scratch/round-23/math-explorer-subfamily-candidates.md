## imo-2026-06

- Distinct openings (candidate 4th subfamilies, scouted purely numerically
  this round — none proved, all conjectural pending a real induction):

  **(A) `a_1 = 3*q^k`, prime `q>=7, q!=5`, any fixed `k>=1`** — TOP candidate.
  This is a literal strict generalization of the already-certified `a1-3q`
  theorem (`k=1` case). Numeric sweep (sympy.primerange, `math.gcd`-based
  greedy simulator, up to 80-120 terms):
    - `k=2` (`a_1=3q^2`): **zero exceptions** for every prime `q` in
      `[7,400)` except `q=5` (permanently excluded — same broken-pattern
      signature as `q=5` in the `k=1` theorem: messy period-6-ish gaps from
      `n=3` on). This is CLEANER than `k=1`, which needed hand-resolution at
      `q=7,11` — here `q=7,11` show ZERO exceptions.
    - `k=3` (`a_1=3q^3`): also zero exceptions for `q` in `[7,100)` (`q!=5`).
    - Conjecture: `a_1=3q^k` gives literal `T=1,L=3` periodicity
      (`a_n=3q^k+3(n-1)`) for every `q>=7,q!=5`, every `k>=1`, matching
      the already-proved `k=1` case exactly in shape.
    - *Why the toolkit transplants*: the whole `a1-3q` proof only used two
      facts about `a_1`: `3|a_1` (trivial, holds for any `k`) and `q|a_1`
      (also trivial, holds for any `k`, since `q|q^k`). The Case-(b) mod-`q`
      analysis (`a_n+2 \equiv 3n-1 \pmod q`, since `a_1\equiv0\pmod q`)
      is IDENTICAL for `a_1=3q` and `a_1=3q^k` — it never used more than
      `a_1\equiv0\pmod q`. So the Parity Witness Lemma
      (`gcd(a_n+2,a_n)=gcd(a_n+2,2)`) transplants verbatim, and the
      Legendre Sieve Gap Bound / Primorial Floor Bound machinery (Lemma A/B,
      both fully general — they only take a modulus `M` and its `ω(M)`, not
      anything specific to `a_1=3q`) applies unchanged to whatever modulus
      `M=qK` arises for `a_1=3q^k`'s own `K`-sequence. What genuinely needs
      re-deriving is only the **`k=0`-window / small-`k` exceptional-case
      table** (the specific numeric witnesses like `gcd(56,27)=1` used
      `a_3=3(q+2)=27` for `q=7` under `a_1=3q`; under `a_1=3q^2` the analogous
      `a_3=3(q^2+2)` is a different number) — but the numeric sweep suggests
      this table is EMPTY (no exceptions needed) for `k>=2`, i.e. likely
      *easier*, not harder, than the already-solved `k=1` case's residual
      table.

  **(B) `a_1 = 5q`, prime `q` avoiding a small finite bad set** — solid
  2nd-tier candidate, more casework but same toolkit. Numeric sweep
  (`q` prime in `[7,300)`): **clean `L=5` literal periodicity for every `q`
  except `q\in\{7,13,19\}`** (`q=2,5` excluded trivially/structurally, as
  those collapse into already-solved families). The three bad primes are
  NOT boundary artifacts — extending the simulation to 300 terms shows
  ~50% of terms mismatch the `L=5` pattern persistently (same qualitative
  signature as the workspace's known FAH-hard seeds, e.g. `a_1=187,209`),
  so they look genuinely FAH-hard, not resolvable by a finite hand-check —
  they must be *excluded* from the theorem statement (like `q=5` is excluded
  from `a_1=3q`), not resolved.
    - *Structural reduction found this round*: since `P(a_1)=\{5,q\}` and
      the induction hypothesis gives `5|a_n`, each of the THREE intermediate
      candidates `a_n+j` (`j=2,3,4`) satisfies `5\nmid(a_n+j)` automatically,
      so `a_n+j` is illegal via `i=1` whenever `q\nmid(a_n+j)` (a direct
      generalization of `a1-3q`'s "Case (a)"). For the residual
      `q|(a_n+j)` sub-case, the SAME algebraic identity used in the
      certified Parity Witness Lemma generalizes cleanly: writing
      `N:=a_n+j`, `\gcd(N,a_n)=\gcd(N,N-a_n)=\gcd(N,j)` — so whenever
      `\gcd(N,j)=1` (a fixed small modulus, `j\in\{2,3,4\}`), witness `i=n`
      is free, with NO case split on `q` or `k` — exactly the same shape as
      the certified lemma, just instantiated at `j=2,3,4` instead of only
      `j=2`. The genuinely hard residual (needing Legendre-sieve-style
      closure, analogous to `a1-3q`'s Case (b) `n` even `k>=1`) is now
      THREE separate bands (one per `j`) instead of one — roughly 3x the
      casework of the already-closed `a1-3q` gap, but structurally
      identical in shape (same two certified lemmas directly reusable,
      unchanged).

  **(C) `a_1 = 3^a*q^b` general — inconsistent, NOT recommended as a
  primary target.** Checked `a=2,b=1` (`a_1=9q`): FAILS at `q=11` (messy,
  persistent, FAH-hard-looking divergence from `n=5` on, ~40% of terms in
  80-term window mismatch) even though `a=1,b=1` (`3q`, already solved) and
  `a=1,b=2,3` (`3q^2,3q^3`, candidate A above) are clean. `a=2,b=2` (`9q^2`)
  ALSO fails at `q=11`, same signature. `a=3,b=1` (`27q`) is clean (zero
  exceptions, `q` in `[7,150)`). So the pattern is NOT simply "`a=1`
  required" — `a=1` and `a=3` are clean, `a=2` breaks (at least at `q=11`);
  no clean rule found. Given the more promising, cleaner, and more clearly
  motivated candidate A (`a=1`, arbitrary `b`) is available, this messier
  general family is not worth prioritizing; flag as a curiosity only.

- Candidate technique(s): the SAME strong-induction skeleton as the
  certified `a1-3q-subfamily-theorem` — illegality of `a_n+1` (consecutive
  integers), illegality of the intermediate candidates via a Case-(a)/
  Case-(b) split (direct `i=1` witness vs. a `q|`-residual needing a
  parity-type free witness plus, for the hard residual band, the certified
  **Legendre Sieve Gap Bound** (`lemmas/legendre-sieve-gap-bound.md`) and
  **Primorial Floor Bound** (`lemmas/primorial-floor-bound.md`) — both
  stated for a generic modulus `M`, hence directly reusable without
  re-proof — plus a small finite exceptional-`q`/exceptional-`k` table
  resolved by hand or explicit exclusion.

- Cheap-kill candidates: before committing a full build to `5q`, run the
  exceptional-prime search (`{7,13,19}`) out to a much larger window
  (e.g. 5000+ terms) to make sure no *fourth* bad prime is hiding beyond
  `q=300` (the search above only went to `q<300`); a single extra bad prime
  found beyond the table would not kill the approach (just enlarge the
  exclusion set) but should be checked before writing the theorem statement.
  For candidate A (`3q^k`), run the same broad sweep for `k=4,5` to confirm
  the "zero exceptions" pattern persists (only `k=2,3` were checked this
  round) — a cheap 5-minute check that would materially derisk the build.

- Knowledge-base entries to use: none new beyond what's already certified
  in this workspace — `lemmas/legendre-sieve-gap-bound.md`,
  `lemmas/primorial-floor-bound.md`, and the certified
  `lemmas/a1-3q-parity-and-k0-window-lemmas.md` (the Parity Witness Lemma
  generalizes directly to candidate B's `j=2,3,4` cases via the identical
  `gcd(N,a_n)=gcd(N,N-a_n)=gcd(N,j)` argument).

- Analogous past problems (cruxes): none newly relevant this round — this
  is pure in-workspace toolkit reuse/extension, not a fresh crux-corpus
  transplant. (Per rule 32/round-22-23 findings, the corpus has already been
  checked and has no genuinely closer analog for the Jacobsthal-type sieve
  content than what's already certified.)

- Prior progress: `a1-3q-subfamily-theorem` is the run's 3rd APPROVE
  (Status `solved` for `a_1=3q`, prime `q>=7,q!=5`, literal `T=1,L=3` from
  `n=1`), certified with `lemmas/legendre-sieve-gap-bound.md` and
  `lemmas/primorial-floor-bound.md`. This round's scouting is a direct
  extension attempt off that base, not yet built.

- Dead ends (do not retry): `a_1=p*q` general (refuted round 19, no clean
  monotone threshold — confirmed still true, not re-tested this round per
  explicit instruction). `a_1=2^a*q` (any `a>=1`) is NOT a new subfamily —
  it is already fully covered by the certified `2|a_1` theorem
  (`lemmas/even-seed-literal-periodicity-theorem.md`, unconditional for
  ANY even `a_1` regardless of other factors) — do not propose it as a
  "new" 4th family. `a_1=3^2*q` (and `3^2*q^2`) confirmed NOT clean (fails
  at `q=11`, FAH-hard-looking) — do not propose `9q` as a subfamily without
  first explaining the `a=2` anomaly.

- Small-case / intuition notes (all CONJECTURE, small-case evidence only,
  not proof):
  - `a_1=3q^k` (`k=2,3` tested): conjectured clean `T=1,L=3` literal
    periodicity for every prime `q>=7,q!=5`, every `k>=1`, with the residual
    exceptional-index table apparently EMPTY for `k>=2` (better than the
    `k=1` theorem's 2-entry hand-checked table) — strongest, most
    build-ready candidate found this round.
  - `a_1=5q`: conjectured clean `T=1,L=5` literal periodicity for every
    prime `q` except a small finite hard-excluded set `\{7,13,19\}` (found
    by direct search, `q<300`); the excluded primes show persistent,
    FAH-hard-looking non-periodic behavior (not boundary/onset artifacts),
    so the theorem's honest scope would need to state these as genuine
    exclusions (like `q=5` in `a1-3q`), not resolved cases.
  - `a_1=3^a q^b` general: no clean rule found; `a\in\{1,3\}` clean,
    `a=2` broken at `q=11` in both `b=1,2` tested — an unexplained
    parity-in-`a`-like anomaly, not investigated further (out of scope for
    a "distinct opening" this round — flagged as a curiosity, not a
    recommendation).

**Ranking for next build:**
1. **`a_1=3q^k`** (candidate A) — highest priority. Cleanest numeric
   evidence, most direct toolkit reuse (both certified lemmas apply
   unchanged; the Parity Witness Lemma's derivation is verbatim-identical),
   smallest expected residual casework (possibly even empty exceptional
   table, unlike the `k=1` theorem's need to hand-resolve `q=7,11`).
   Recommend running the `k=4,5` cheap-kill sweep first, then committing a
   build this round or next generalizing the existing `a1-3q` proof file
   directly (same induction skeleton, same case split, replace `3q` with
   `3q^k` throughout and re-derive the `n_0,K_0` formulas — which are
   identical in `q` since `a_1\equiv0\pmod q` regardless of `k` — and the
   small-`k`-band table, which numerics suggest is empty).
2. **`a_1=5q`** (candidate B) — solid second choice, ~3x the casework of
   the already-closed `a1-3q` gap but structurally identical (same two
   certified lemmas, same generalized parity-witness identity applied at
   `j=2,3,4`), with a slightly harder honest-exclusion story (3 known-bad
   primes to state and to argue are genuinely excludable, not just
   hand-resolvable) — a good target if candidate A's build stalls or if the
   outliner wants to run both in parallel as genuinely distinct approaches
   (different toolkit-instantiation shape: 1 residual band vs. 3).
3. **`a_1=3^a q^b` general** — do not build yet; the `a=2` anomaly is
   unexplained and would need its own dedicated diagnostic round before any
   proof attempt, and candidate A already covers the cleanest, most
   valuable slice of this family without that risk.
