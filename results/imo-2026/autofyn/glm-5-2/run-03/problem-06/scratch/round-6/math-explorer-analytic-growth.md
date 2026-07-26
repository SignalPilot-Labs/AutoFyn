# imo-2026-06 — analytic / growth-rate / prime-density lens

## 1. The route (mechanism sketch)

**Engine.** Use the certified linear growth `a_n ≤ a_1 + (n-1)·M_1` (so `a_n = O(n)`), together with the **forced-increment identity** (round-5 mount): whenever `a_{n+1}` is a multiple of a prime `q`, then `d_n = a_{n+1}-a_n = q - (a_n mod q)`; since `d_n ≤ M_1` (`linchpin-and-gap-bound`), this is possible only when `a_n mod q ∈ W_q := {q-M_1,…,q-1}` (the *approach window*). For `q > M_1`, `|W_q| = M_1 < q` (a strict minority of residues); for `q ≤ M_1`, `W_q =` all residues (no constraint — exactly the conjectural boundary).

**Hoped mechanism.** Suppose `q > M_1` is governing. The walk `a_n mod q` (steps `d_n ∈ {1,…,M_1}`, irreducible on `Z/qZ` since `1∈` step-set) is *empirically equidistributed* (see §4). Hence the frequency of visits to `W_q` is `≈ M_1/q`, and each visit *can* produce a `q`-multiple. Consecutive `q`-multiples are ≥ `q/M_1` steps apart (spacing), so the density of `q`-multiples among `{a_n}` is `≤ M_1/q` (the certified spacing upper bound, sound). To derive a **contradiction** one would need a matching **lower bound** on the `q`-multiple density that *governing* forces and that exceeds `M_1/q` (or exceeds what linear growth can sustain).

## 2. Why this is NOT in the 13-dead / 4-fence list — and where it actually lands

- Not strip/cofactor, not Schur, not monovariant, not CRT-lift, not substitution/morphic, not ergodic-window, not p-adic, not coincidence-doubling, not deviation-descent, not `f(M_1)`-bounded finite-statistic (T-unbounded fence): the engine is a *global* counting/walk-density estimate using `a_n = O(n)`, not a local cofactor bound and not a finite pigeonhole state.

**BUT it collapses to two fences nonetheless:**

- **(Collapse to cofactor fence.)** The forced-increment identity is only the *availability* of a `q`-multiple at distance `d_n ∈ {1,…,M_1}`. The `q`-multiple `q·k` is actually *taken as* `a_{n+1}` iff it is **admissible** — i.e. iff `S(qk) = {q} ∪ S(k)` hits every minimal support, i.e. iff `primefactors(k)` transverses the `q`-free minimals. **That is exactly the certified-circular cofactor-bound step** (`window-uniqueness-reduces-to-cofactor`, `lemma-C-strip-no-go`, `schur-cofactor-premise-fails-in-periodic-regime`). The analytic walk tells you *when a `q`-multiple is geometrically available*; whether it is *admissible* is Gap A.

- **(Collapse to density/covering-capacity fence.)** The contradiction needs a **lower bound** on the `q`-multiple density from "governing." The only candidate lower bound is "governing ⟹ `q` must keep re-appearing to hit new supports" = the **covering-capacity of `T\{q}`** argument, certified **circular** (`witness-density-recurrence`, round-2 rule: covering capacity is unbounded for pairwise-intersecting families; transient primes give unbounded capacity compatibly with Gap A). Equidistribution of `a_n mod q` supplies the *matching* upper bound `M_1/q`, not a lower bound, so it cannot close the gap.

The distinguishing question the dispatch posed — "does it secretly reduce to bounding `primefactors(k)`?" — answers **yes**: the admissibility gate on the `q`-multiple is the cofactor bound. The "global growth rate" half is genuine (spacing upper bound), but the contradiction half is not.

## 3. The hard step (load-bearing and unproved)

> *Claim needed:* "If `q > M_1` is governing, the density of `q`-multiples among `{a_n}` is bounded below by a function `f(q, M_1) > M_1/q` (or by any positive function incompatible with `a_n = O(n)` jointly over all governing `q`)."

This claim is **false in the available data** (§4): transient primes `q > M_1` already realize density `≈ (M_1/q)·(small)` with `a_n mod q` equidistributed, so equidistribution + linear growth is *compatible* with `q` being transient; symmetrically nothing in the walk distinguishes a governing `q` from a transient one *except* the admissibility (cofactor) structure. No Mertens/PNT/sieve inequality supplies a non-circular lower bound, because "governing" (whether `∪MT(F_∞)` or "divides infinitely many terms") entails **no positive density floor** — a prime may divide infinitely many terms at arbitrarily low density.

A secondary hoped inequality — *if `G` (governing primes `> M_1`) is infinite then `∑_{q∈G} 1/q = ∞`, forcing `∑ densities` to exceed `log n`* — also fails: (i) an infinite prime set may have convergent reciprocal sum; (ii) the actual `q`-multiple densities have **no lower bound**, so their sum is always `≤` (avg #prime factors per term) `≈ log n` trivially — an upper bound, not a contradiction.

## 4. Computational probe (naive-correct gcd-greedy, *not* the round-4 `fast_greedy.py`)

Reference: wrote a support-tracking fast greedy, **verified bit-exact against the naive `gcd`-greedy** on `a_1 ∈ {15,35,77}` (50–100 terms each). Bug watch: a first draft used `q|x` (bitwise OR, always truthy) — corrected to `x % q == 0`; the spacing/density numbers below are from the corrected count.

**Reliable small cases** (period found at `n0=0`, confirmed with `min_run=200`):

| `a_1` | `M_1` | `T` | `L` | governing primes (1 period) | all `≤ M_1`? |
|---|---|---|---|---|---|
| 15 | 15 | 8 | 30 | {2,3,5,7} | yes (max 7) |
| 35 | 35 | 34 | 210 | {2,3,5,7,11,13,17,19,23} | yes (max 23) |
| 77 | 77 | 18 | 154 | {2,3,5,7,11,13} | yes (max 13) |
| 91 | 91 | 20 | 182 | {2,3,5,7,11,13,17,19} | yes (max 19) |

Conjecture `q ≤ M_1` holds in all reliable cases. Asymptotic average increment `L/T ∈ {3.75, 6.18, 8.56, 9.10}`, all `≤ M_1` (consistent with `d_n ≤ M_1`).

**Equidistribution + spacing probe** (the analytic picture), `a_1 = 15, M_1 = 15`, transient primes `q > M_1` (these are *finite-multiplicity* primes — the opposite of governing):

| transient `q>M_1` | `M_1/q` | `freq(a_n mod q ∈ W_q)` | `density(q | a_n)` |
|---|---|---|---|
| 17 | 0.8824 | 0.8825 | 0.0587 |
| 19 | 0.7895 | 0.7895 | 0.0525 |
| 23 | 0.6522 | 0.6522 | 0.0435 |
| 29 | 0.5172 | 0.5190 | 0.0343 |
| 31 | 0.4839 | 0.4838 | 0.0320 |

( Same pattern for `a_1 ∈ {35,77,91}`: `freq(a_n mod q ∈ W_q) ≈ M_1/q` to 3 decimals, and `density(q|a_n) ≈ (M_1/q)·(small factor)` — much smaller than the spacing bound. )

**Interpretation (conjecture, not proof):**
- `a_n mod q` **is** equidistributed for these `q` (PNT/Kronecker-Weyl intuition confirmed empirically; for `a_1=15, q=7`, `a_n mod 7` is uniform to 0.1% over 4000 terms). This is a genuine positive observation about the greedy walk.
- The spacing upper bound `density(q|a_n) ≤ M_1/q` is **sound and tight in order** but the actual density is far below it (the `q`-multiple is usually *not* admissible even when the walk visits `W_q`).
- **The walk cannot distinguish governing from transient.** Transient primes `q > M_1` are *already* equidistributed-mod-`q`-visited at frequency `M_1/q` and divide only finitely many terms; a hypothetical governing `q > M_1` would look *identically* to the walk. The only thing separating them is the admissibility gate on `q·k` = the cofactor structure = Gap A.

**Spurious-period trap (re-confirmed).** `a_1 = 175` (`M_1=35`), `a_1=385`, `a_1=847` (`M_1=77`) at `N=6000–20000` return short false periods (`T=120, 120, 85`) with `n_0` near `N`, yielding bogus "governing primes `> M_1`" (e.g. `2851` for `a_1=175`). These are *transient primes captured in a non-repeating slice* — the same trap the round-5 rule flags (`a_1=385` spurious `T=97`, true `T=5088` needs `N>120000`; `a_1=847` true `T=1744` per the rad-77 impossibility). The conjecture `q ≤ M_1` is **only checkable on reliable small-period cases**; there it holds. Do NOT treat the short-tail "governing primes" lists as counterexamples — they are artifacts.

## 5. Verdict: NO-UNFENCED-ROUTE

The analytic / growth-rate / prime-density lens is genuinely orthogonal in its **upper-bound half** (the spacing bound `density ≤ M_1/q` and the equidistribution intuition are real, sound, and empirically confirmed), but it **collapses on its contradiction half**:

- The forced-increment identity gives *availability* of `q`-multiples; the **admissibility** of the `q`-multiple `q·k` is the cofactor bound (`primefactors(k)` must transverse the `q`-free minimals) — the certified-circular step (`window-uniqueness-reduces-to-cofactor`).
- A contradiction from "`q > M_1` governing" requires a **lower bound** on `q`-multiple density, and the only source is the covering-capacity argument — **certified circular** (round-2 rule).
- Equidistribution of `a_n mod q` is *empirically true* but **cannot distinguish governing from transient primes** (transients already realize the same `M_1/q` window frequency), so it supplies no inequality that `q > M_1` governing would violate.
- The sum-over-primes variant fails too: `∑_{q∈G} (density_q) ≤` (avg #prime factors per term) is an *upper* bound, always satisfiable; and an infinite governing set need not have divergent `∑ 1/q`.

**Honest conclusion.** No non-circular unfenced analytic mechanism exists on this lens. The route reduces to the **cofactor fence** (admissibility gate) for its hard step and to the **density/covering-capacity fence** for its would-be lower bound — both already certified dead. The one genuinely new *positive* deliverable is the empirical equidistribution `a_n mod q ≈ uniform` (with `freq(W_q) = M_1/q`) — a **conjecture about the greedy walk**, not a proof of `q ≤ M_1`, and it does not bypass Gap A.

**Recommendation.** Do not mount an analytic/growth-rate approach — it would re-walk the cofactor and covering-capacity fences. The partial-result consolidation (conditional endgame + LOCK + 28 lemmas + `q ≤ M_1` conjecture stated as open target) remains the correct round-6 deliverable. If a genuinely-unfenced mechanism is to be sought, it must come from a *different* lens than analytic/growth — none is on the table from this route.
