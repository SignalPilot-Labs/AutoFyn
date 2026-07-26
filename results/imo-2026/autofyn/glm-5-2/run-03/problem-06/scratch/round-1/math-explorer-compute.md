## imo-2026-06  (computational-experiment route)

## Terrain

The recurrence: `a_{n+1}` = smallest `m > a_n` with `gcd(m, a_i) > 1` for **every** `i ≤ n`
(equivalently, `m`'s prime-set is a *hitting set* of the family `{prime-set(a_1),...,prime-set(a_n)}`).
Verified my fast (prime-set-intersection) implementation against a naive gcd-based one and against
minimality (no admissible `m` strictly between `a_n` and `a_{n+1}`) for `a_1 ∈ {15,35,77,105,143,91}`.

Computations ran to 200–12000 terms across 45 starting values. The headline structural facts:

1. **(Trivial lemma, the linchpin)** Every term `a_n` is divisible by some prime **dividing `a_1`**.
   *Proof (one line):* the condition includes `i=1`, so `a_{n+1}` must share a factor with `a_1`;
   every prime factor of `a_1` is `≤ Q := max prime | a_1`. Verified for all 45 starting values
   (0 counterexamples in 200–12000 terms each). **This is the only genuinely easy fact in the
   problem** — but it does a lot: it bounds the active prime universe and the gaps.

2. **Gap bound (consequence):** gaps `d_n := a_{n+1}-a_n ≤ P := ∏_{p | a_1} p` (the radical of
   `a_1`). *Reason:* the smallest multiple of `rad(a_1)` greater than `a_n` is `≤ a_n + rad(a_1)`,
   is divisible by every prime of `a_1`, and (by lemma 1) shares a factor with every prior term —
   hence is admissible. So `a_{n+1}` is at most that. Empirically gaps are FAR smaller than this
   bound (e.g. `a_1=385`: max gap 14, `rad(385)=385`).

3. **`a_n` grows linearly** (slope `= L/T` in the eventual AP, ~8.66 for `a_1=385`).

## Data table (a sample; all verified gcd + minimality)

| `a_1` | primes(a_1) | pre-period | `T` | `L` | `L` fact | primes in tail-terms (sample) |
|---|---|---|---|---|---|---|
| 2,4,6,8,10,12,210,2310,30030 (any even `a_1`) | contains 2 | 0 | 1 | 2 | 2 | tail = `a_1, a_1+2, …` (all even) |
| 3,9,21,33,39,231 (a_1 divisible by 3, no 2) | contains 3 | 0 | 1 | 3 | 3 | multiples of 3 |
| 11,13,17,19,23 (`a_1` prime) | `{p}` | 0 | 1 | `p` | `p` | `a_n = n·p` |
| 15 = 3·5 | {3,5} | 4 | 8 | 30 | 2·3·5 | {2,3,5,7,11,13,…} |
| 35 = 5·7 | {5,7} | 0 | 34 | 210 | 2·3·5·7 | grows unboundedly |
| 77 = 7·11 | {7,11} | 0 | 18 | 154 | 2·7·11 | grows unboundedly |
| 91 = 7·13 | {7,13} | 0 | 20 | 182 | 2·7·13 | grows unboundedly |
| 105 = 3·5·7 | {3,5,7} | 0 | 58 | 210 | 2·3·5·7 | grows unboundedly |
| 143 = 11·13 | {11,13} | 0 | 64 | 858 | 2·3·11·13 | grows unboundedly |
| 1001 = 7·11·13 | {7,11,13} | 0 | 282 | 2002 | 2·7·11·13 | grows unboundedly |
| 385 = 5·7·11 | {5,7,11} | **≫12000** | — | — | — | **NOT periodic in 12000 terms** |
| 1309 = 7·11·17 | {7,11,17} | **≫12000** | — | — | — | NOT periodic in 12000 terms |
| 2431 = 11·13·17 | {11,13,17} | **≫12000** | — | — | — | NOT periodic in 12000 terms |

`T`/`L` for the "easy" rows obtained by *strict* detection (requiring two full periods to match);
the residue set `R := {a_n mod L : n in tail}` then has `|R| = T` exactly, and `a_{n+T} = a_n + L`.

## Structural observations (each labelled proved / conjecture-from-data)

- **(PROVED)** Every `a_n` divisible by some prime of `a_1` (lemma 1 above).
- **(PROVED)** Gaps bounded by `rad(a_1)`; `a_n` grows linearly.
- **(PROVED, when it applies)** *Hitting-set enumeration is periodic:* Suppose there is a finite
  "pinning" prime set `P*` and a finite family `F*` of subsets of `P*` (the `P*`-restrictions of
  the pinning historical terms) such that admissibility of `m` is equivalent to "`m`'s
  `P*`-restriction is a hitting set of `F*`". Then `a_{n+1}` = smallest `m > a_n` with
  `m mod M ∈ R`, where `M = ∏ P*` and `R = {r mod M : r's P*-prime-set hits F*}`. Enumerating
  these residues increasingly is periodic with `T = |R|`, `L = M`. ✓ verified for all "easy" rows:
  e.g. `a_1=15`, `F* = {{3,5},{2,3},{2,5}}`, `M=30`, `R={0,6,10,12,15,18,20,24}`, `T=8`, `L=30`.
  Same match for 35, 77, 91, 105, 143, 1001: the residues mod `L` are *exactly* the hitting-set
  residues, and `|R| = T`.
- **(CONJECTURE from data, the trap)** "The pinning family over `P := {primes dividing a_1} ∪
  {2,3}` (or similar small primes) stabilizes quickly, hence the sequence is periodic." — **THIS
  IS FALSE.** For `a_1=385`, the family of `P_Q`-restrictions (`P_Q = {2,3,5,7,11}`, all primes
  ≤ `Q=11`) **stabilizes by term 225 to 18 distinct patterns** and adds no new pattern through
  term 12000 — YET the diff sequence is **not periodic** in 12000 terms (no autocorrelation
  period `>0.95` for `T ≤ 3000`; 348 distinct residues mod 2310 in the last 4000 terms). So
  "F_P stabilizes ⇒ periodic" is genuinely insufficient; **large free-rider primes keep
  constraining**.
- **(CONJECTURE)** Large free-rider primes become redundant *eventually* — the mechanism the
  theorem needs but the data does not quickly exhibit for 385-class `a_1`. A prime `q` appearing
  in term `a_i` is *redundant* iff every hitting-set-pattern of the current `F` intersects
  `prime-set(a_i)`. For `a_1=15` every admissible pattern contains `2` or `3`, and every
  large-prime historical term (`42=2·3·7`, `66=2·3·11`, `78=2·3·13`, `102=2·3·17`, …) is hit via
  that `2`/`3`, so 7/11/13/17 never pin → fast stabilization. For `a_1=385`, the 18 stabilized
  patterns include `{2,11}` (no 3,5,7), so a historical term like `1995 = 3·5·7·19` is NOT hit by
  `{2,11}`-restricted candidates via small primes → 19 stays non-redundant → keeps constraining.
- **(OBSERVATION)** For semiprime `a_1 = p·q` (both odd, `p<q`): the pinning set is
  `P* = {2} ∪ {2,3}\{?} ∪ primes(a_1) \ {some}` — empirically `L = 2 · (product of a subset of
  primes(a_1)) · (maybe 3)`. E.g. `15→30=2·15`, `35→210=6·35`, `77→154=2·77`, `91→182=2·91`,
  `143→858=6·143`, `1001→2002=2·1001`. No clean closed form for which extra primes enter; **do
  not** assume `L = rad(a_1)` or `L = 2·rad(a_1)`.

## Surprises (facts a naive proof would miss)

1. **The "F over small primes stabilizes" step is the trap.** For `a_1 ∈ {385, 1309, 2431}` the
   `P_Q`-restriction family is **stable by term ~225** while the sequence is still **aperiodic at
   term 12000**. Any proof that stops at "the small-prime constraint family is finite, hence it
   stabilizes, hence periodic" is **wrong** — it misses large free-rider primes that remain
   non-redundant indefinitely (but finitely).
2. **Pre-period / period can be enormous.** `a_1=385` (smallest "hard" case, `Q=11`) has no
   period `≤ 3000` in 12000 terms; `a_1=2431` (`Q=17`) likewise. The proof must show eventual
   periodicity without producing a usable bound on when — pigeonhole on a finite state space is
   the natural tool, but the state must be chosen to actually be finite.
3. **`L` is NOT `rad(a_1)`** (e.g. `a_1=35` gives `L=210 = 6·rad`, `a_1=143` gives `858 = 6·rad`).
   The increment pulls in primes that do not divide `a_1` (always 2; sometimes 3). So the
   eventual AP modulus is *larger* than `rad(a_1)`.
4. **Tail terms have unboundedly many distinct prime factors** (e.g. `a_1=15` tail hits primes
   2,3,5,7,11,13,17,19,23,29,31,37,43,47,59,61,71,73,79,89,149,151,157,…). So one cannot frame
   the proof as "the set of primes appearing stabilizes" — it does **not**. Only the *constraint
   structure* (which primes are non-redundant) stabilizes.
5. **T=1 is the common case but not the only one.** Even `a_1=15` has `T=8`. Real periods `T>1`
   are the norm for odd semiprime `a_1`. The theorem's `T` is genuinely needed (not collapsible
   to a plain AP).

## Hard steps / gaps the data points to

- **(HARD, the crux)** Prove the *full* constraint family over all primes (not just primes ≤ Q)
  stabilizes to a finite relevant core — equivalently, that only finitely many primes are
  *non-redundant*, and after they are all pinned the admissibility of `m` depends only on `m mod M`
  for some finite `M`. The data shows this is true (theorem) but the stabilization is slow and
  non-obvious for 385-class inputs; a direct "F_P stabilizes in ≤ 2^{|P|} steps" argument fails.
- **(HARD)** Even after the relevant constraint core stabilizes, prove that the *true* smallest
  admissible `m` equals the smallest `m` whose small-prime-restriction hits the stabilized core.
  The gap between these two (large-prime-admissible candidates that are smaller) is exactly what
  makes 385 aperiodic for so long; the proof must show this gap vanishes eventually.
- **(MEDIUM)** Rigorize the periodic-enumeration lemma (the "PROVED, when it applies" block
  above) — this part is clean combinatorics once the finite core is established.
- **(EASY)** Lemma 1 (every term div by a prime of `a_1`) and the gap bound — already proved
  above; the outliner can cite them directly.

## Openings for the outliner (3 distinct routes the data motivates)

1. **Finite-state / pigeonhole on a bounded-gap sequence.** Gaps `d_n ∈ [1, rad(a_1)]` (finite
   alphabet), `a_n` grows linearly. Define a *finite* state capturing exactly the information
   needed to determine `d_{n+1}` from the past; show the state space is finite; pigeonhole gives
   a repeated state → deterministic future → periodicity. *The hard part is naming the finite
   state.* Candidate: `(a_n mod M, active-constraint-signature)` where the signature is the
   family of prime-sets of "recently non-redundant" terms restricted to a fixed small prime set.
   The data says the signature over small primes *does* stabilize fast (385: by term 225); the
   remaining work is to show large-prime non-redundancy also enters a finite, eventually-closed
   signature.

2. **Redundancy saturation (structural/hitting-set).** Frame everything as hitting-set
   dynamics on the family of prime-sets. A new term's prime-set `b` is *redundant* (does not
   shrink the hitting-set family) iff every current hitting set intersects `b`. Prove redundancy
   saturates: after finitely many non-redundant insertions, every subsequent term is redundant.
   Once saturated, admissibility is `m mod M ∈ R` for fixed `M, R` → periodic enumeration
   (cite the proved enumeration lemma). *This is the conceptually cleanest route* but the
   saturation proof is the load-bearing step and the data warns it can take a long time
   (385-class) — the proof must be non-constructive about *when*.

3. **Dual / modular-recurrence route.** Track `a_n mod M` for `M = rad(a_1) · K` (with `K` a
   power of 2 or a primorial extension to absorb pulled-in primes). Show `a_n mod M` is
   eventually periodic (finite residues, deterministic-enough transition). Lift mod-`M`
   periodicity to a true AP `a_{n+T} = a_n + L` by combining the gap bound (so the *lift* `L`
   is bounded and the cumulative offset over one residue-period is constant). This dodges naming
   the full constraint family but requires showing the mod-`M` transition is genuinely
   memory-finite — same subtlety as route 1 in disguise.

## Cheap-kill candidates (pruning before heavy computation)

- **Trivial small-prime lemma + gap bound** (above) — already kills the "infinite primes make it
  wild" worry and gives linear growth for free. Use these as the foundation of every approach.
- **T=1 reduction for even `a_1` or prime `a_1`:** if `2 | a_1`, then `a_n = a_1 + 2(n-1)` (all
  even, `L=2`, `T=1`) — one-line proof. If `a_1` is prime `p`, `a_n = n·p` (`L=p`, `T=1`). These
  are immediate special cases worth recording as certified lemmas.

## Knowledge-base entries to use
- **Divisor analysis / consecutive-integer coprimality** (gcd structure) — directly the recurrence.
- **Invariants & monovariants** — the hitting-set family is non-increasing (monotone) under
  constraint addition; eventual stabilization is a monovariant-on-finite-set argument.
- **Pigeonhole / extremal principle** — finite-state route (opening 1) is pigeonhole on the state
  space.
- **Bertrand's postulate / primorial bounds** — to control pulled-in primes and bound the gap
  alphabet (alternative to `rad(a_1)` if a sharper modulus is needed).
- General proof methods: **strong induction, contradiction (assume never periodic)**.

## Analogous past problems (cruxes)
- **None truly analogous.** The crux corpus has no "minimal-hitting-set sequence eventually
  periodic" problem. The closest in *spirit* (not statement):
  - `aimo-0030` (number_theory, divisibility-and-gcd): an impartial game where good positions
    are characterized by an "allowed-prime signature"; the crux strips large prime factors by
    replacing a number with a product of its *small* allowed primes that still clears the
    threshold — the same "large primes are redundant once small-prime coverage suffices" move
    that this problem's saturation step needs. Worth reading for the redundancy argument.
  - `aimo-0035` (number_theory): "smallest-prime-factor bounds a ratio parameter" — same flavor
    of using `spf`/prime-of-`a_1` to bound structure.
  The EKG sequence (OEIS A064413, *not* in corpus) is the nearest known cousin: `a(n)` = smallest
  *unused* number sharing a factor with `a(n-1)`. Our problem is different (shares with **all**
  prior, not just last; allows reuse; hence monotone, eventually AP rather than a permutation) —
  do not cite EKG results, but the "small primes govern the long-range structure" intuition
  transfers.

## Prior progress
None — round 1, empty workspace (`results/imo-2026-06/current.md` is `unsolved`, no approaches,
no lemmas).

## Dead ends (do not retry)
- (none yet — this is round 1. But the data itself flags one dead-end framing: **"stabilize the
  small-prime constraint family, conclude periodic" is insufficient** — see Surprises #1. Any
  approach the outliner builds on that framing will fail for `a_1=385`-class inputs; the proof
  must address large free-rider primes explicitly.)

## Small-case / intuition notes (all conjecture-from-data unless marked PROVED above)
- For `a_1` even or `a_1` prime: clean `T=1` AP (PROVED, one-line).
- For odd semiprime `a_1=pq` with `p,q` small-ish: clean periodic with `T=|R|`, `L=2·(subset
  of {2,3}∪{p,q})`, `R` = hitting-set residues mod `L`. Verified strictly for {15,35,77,91,143,1001}.
- For `a_1` with three or more odd prime factors including a "large-ish" one (385=5·7·11,
  1309=7·11·17, 2431=11·13·17): pre-period/period is **huge** (>12000 terms unsolved
  empirically); the theorem still holds but the proof must be non-constructive about the
  stabilization time.
- Gap distribution for `a_1=385` (12000 terms): `{2:1414, 3:156, 4:1399, 5:90, 6:1638, 7:617,
  8:1206, 10:1045, 12:1082, 14:3352}` — gaps ∈ {2,3,4,5,6,7,8,10,12,14}, all `≤ 14 ≪ rad(385)=385`.
  The gap 14=2·7 dominates; 7,5,3 appear as gaps too. This signature is what the eventual
  periodic pattern must reproduce.
