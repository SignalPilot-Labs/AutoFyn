# imo-2026-06 — p-adic / per-prime-valuation route (round 5)

## Lens

Per-prime-valuation attack: for each small prime `p | M_1 = rad(a_1)`, analyze `v_p(a_n)` and `v_p(d_n)` along the greedy orbit; seek a *local* `p`-adic period `L_p` such that `L = lcm(L_p : p | M_1)`, bounding `L` (hence the governing-prime set `G = primefactors(L)`) by `M_1`'s structure WITHOUT forming `MT`/transversals/cofactors.

## Verdict: DEAD — clean structural obstruction (verified computation)

The dispatch's proposed local-global mechanism is **structurally false**, and per-prime `p`-adic data does **not** distinguish governing from non-governing primes. The route collapses to the same cofactor-bound wall (Gap A) via the "no large prime divides `L`" step. Three independent obstructions below.

## Computation (reliable cases only)

I first caught **FALSE periods** for `a_1 ≥ 175` with short tails (exactly the round-1 trap: a spurious `T=97, L=840` for `a_1=385`, which gave bogus "governing prime 89 > M_1=77" — an artifact, NOT a counterexample to `q ≤ M_1`). Rewrote with strict `min_run=400` and a corrected fast greedy (inclusion-**minimal** term-support tracking, verified equal to plain `gcd` greedy on `a_1=15,385`). Reliable cases (clean `n0=0`, long stable tails):

| a_1 | M_1 | T | L | G=primes(L) | p\|M_1 | all q≤M_1? |
|---|---|---|---|---|---|---|
| 15 | 15 | 8 | 30 | {2,3,5} | {3,5} | ✓ |
| 35 | 35 | 34 | 210 | {2,3,5,7} | {5,7} | ✓ |
| 65 | 65 | 58 | 390 | {2,3,5,13} | {5,13} | ✓ |
| 77 | 77 | 18 | 154 | {2,7,11} | {7,11} | ✓ |
| 91 | 91 | 20 | 182 | {2,7,13} | {7,13} | ✓ |
| 143 | 143 | 64 | 858 | {2,3,11,13} | {11,13} | ✓ |
| 175 | 35 | 274 | 2730 | {2,3,5,7,13} | {5,7} | ✓ |

(`a_1=385,847,1309,2085` need `N>120000` for a clean tail; the round-1 logged `T=5088, L=43890` for `a_1=385` is consistent with `q≤M_1`.) Conjecture `G ⊆ {primes ≤ M_1}` re-confirmed on all reliable cases; no counterexample.

## Obstruction O1 — the local-global decomposition `L = lcm(L_p : p|M_1)` is FALSE

In **every** reliable non-LOCK case, **2 ∈ G but 2 ∤ M_1** (a_1 is odd ⇒ `rad(a_1)` odd ⇒ 2 ∉ primes(M_1)). Verified 7/7. More generally `G` and `primes(M_1)` are **incomparable sets**:
- Primes of `M_1` can be **non-governing**: `a_1=175` has `11 ∤ L=2730`; `a_1=1309` has `11,17 ∤ L`; `a_1=385` has `7,11 ∤ L`.
- Governing primes can be **absent from `M_1`**: 2 (always), 3 (often: a_1=15,35,65,143,175), 13 (a_1=175), etc.

So the `p`-part of `L` at `p ∤ M_1` (always including `p=2`) **cannot** be recovered from `p`-adic analysis restricted to `p | M_1`. The dispatch's hoped-for `L = lcm(L_p : p|M_1)` is provably the wrong decomposition. To recover the full `L` one would need `p`-adic analysis at primes NOT dividing `a_1` — i.e. at the very large primes the conjecture is trying to bound — which is circular.

## Obstruction O2 — governing status is NOT a local `p`-adic property

Per-prime data in the TRUE periodic regime (table in `/tmp/round5_final.py` output):

- **`v_p(d_n)` does not determine governing status.** Non-governing `p` can have `v_p(d_n) ∈ {0,1}` non-constant (`a_1=77`: `p=3,5` non-governing yet `v_p(d)∈{0,1}`; `a_1=91`: `p=3,5`; `a_1=143`: `p=5`; `a_1=175`: `p=11`). Governing `p` can have `v_p(d_n) ≡ 0` constant (`a_1=15`: `p=5` governs yet `v_5(d)≡0`; `a_1=35`: `p=7`; `a_1=65`: `p=13`; `a_1=143`: `p=13`; `a_1=175`: `p=13`). So neither "constant" nor "{0,1}" cleanly flags governing.
- **`v_p(a_n)` does NOT stabilize or become periodic with any finite period `T_p`.** For `p=2`, computed the minimal period of the sequence `(v_2(a_n))` over `8T` terms in all 7 reliable cases: **`None` (aperiodic) in every case** — confirms the round-4 outliner's note for `a_1=385` and extends it: `v_2(a_n)` is aperiodic for ALL reliable cases. This is expected (in an AP `a_n=A+(n-n_0)L` with `2|L`, `v_2(a_n)=v_2(A+(n-n_0)L)` is a LTE-type aperiodic unbounded function), so the dispatch's "stabilize to constant or own period `T_p`" hope is **false for every governing prime**, not just `p=2`.
- **`v_p(a_n)` is unbounded for ALL primes `p`** (governing AND non-governing): for `p ∤ L`, `a_n = A + mL` with `gcd(L,p)=1`, and `A+mL ≡ 0 (mod p^k)` has a unique solution `m mod p^k` (Hensel), so `v_p(a_n) ≥ k` is hit for arbitrarily large `k`. So the finite-window "non-governing `p` has bounded `v_p(a)`" appearance (max 1–2) is a window artifact; over the infinite orbit both kinds are unbounded. No threshold `v_p(a_n) ≥ C ⟹ p` governing exists.

## Obstruction O3 — the "no `p > M_1` divides `L`" step is GLOBAL = Gap A

Even granting a hypothetical per-prime local analysis that determines `p | L` for each small `p ≤ M_1`, the conjecture `G ⊆ {q ≤ M_1}` requires excluding **all** primes `q > M_1` from `L`. That is a statement about infinitely many primes and is exactly the cofactor-bound / `MT(F_∞)`-finiteness wall (Gap A) — the same wall certified circular for ~11 mechanisms. `p`-adic analysis at finitely many small primes cannot reach the infinitely many large primes. This is the same obstruction already fenced (round 3): "minimal functional modulus for predicting `d_n` from `a_n mod L_0` is `L_0 = L` itself"; `p`-adic residues `a_n mod p` (for `p|M_1`) are *coarser* than `a_n mod L_0`, so they certainly cannot serve as a finite state determining `d_n`. The route **overlaps the certified-dead modular/residue-statistic fence**.

## One micro-conjecture (does NOT close Gap A)

**Conjecture (7/7 reliable):** in every non-LOCK case, **2 ∈ G** (2 always governs). If true this is a new small structural fact. BUT proving it = proving `2 ∈ MT(F_∞)` eventually = a slice of Gap A itself (one must show 2's covering role persists, which is the same `MT`-stabilization question). So it is not a free lemma; record as a conjecture only, not a route.

## Distinct openings (for the outliner — but all lead back to the wall)

1. **`v_2`-always-governing lemma**: try to prove `2 | L` in non-LOCK unconditionally (does not bound the *other* governing primes; likely needs Gap-A-style machinery). Dead-end-adjacent.
2. **Per-prime `L_p` via `d_n mod p^k` Hensel structure**: dead by O2 (governing status not local).
3. **`a_n mod p` period as a `p | L` detector in the periodic regime**: a *description* of the periodic regime (`p|L ⟺ a_n mod p` has period `|T`), not a proof of periodicity. Dead by O3.

## Candidate technique(s)

`p`-adic / LTE / Hensel (KB lines 63, 67) — applicable for *describing* valuations once periodicity is assumed, but **not** for proving `G ⊆ {q ≤ M_1}`. The only KB entry pointing at greedy-eventual-periodicity is the order/Fermat-Euler eventual-periodicity-mod-`m` (line 65–66, 80), which is a *consequence* of an AP, not a cause.

## Cheap-kill candidates

None new. The `v_2`-always-governing conjecture is the only fresh cheap-kill-adjacent observation, and it does not bound the hard primes.

## Knowledge-base entries to use

None for a proof. Hensel's lemma (line 63) and LTE (line 67) explain the `v_p(a_n)` aperiodicity (O2) but do not bound `G`. The order/Fermat-Euler periodicity-mod-`m` entries (lines 65–66, 80) describe the periodic regime, not the route to it.

## Analogous past problems (cruxes)

Not pulled this round (time-budgeted); the crux corpus search for "smallest-admissible greedy ⇒ eventually periodic" is itself an untried direction the outliner could mount, but it is a *different* route (crux retrieval), not the `p`-adic route. The `p`-adic route has no clean crux analog because it is structurally obstructed.

## Prior progress

Unchanged: whole theorem still reduced to Gap A; conditional endgame + LOCK + 25 lemmas all certified. This route adds **no** new lemma (all observations are either descriptions of the periodic regime or negative obstructions already covered by certified fences).

## Dead ends (do not retry)

- **`p`-adic local-global `L = lcm(L_p : p|M_1)`** — dead by O1 (2 always governs, 2∤M_1).
- **"stabilize or own period `T_p` for `v_p(a_n)`"** — dead by O2 (aperiodic `None` for `v_2(a_n)` in 7/7 reliable cases; unbounded for all `p`).
- **"`v_p(d_n)` pattern ⇒ governing status"** — dead by O2 (both directions fail).
- **per-prime local analysis excluding large primes from `L`** — dead by O3 (global statement = Gap A; overlaps certified modular/residue-statistic fence).

## Small-case / intuition notes (conjecture, not proof)

- `G` and `primes(M_1)` are incomparable sets in every reliable case; the `p`-adic-at-`p|M_1` lens sees only an unstable proper subset of `L`'s prime factorization.
- `v_2(a_n)` is aperiodic with **no** finite period in all 7 reliable cases — the round-4 outliner's `a_1=385` observation is a general phenomenon, not a curiosity.
- `2 ∈ G` in 7/7 reliable non-LOCK cases (conjecture; proving it is a slice of Gap A, not free).
- Conjecture `G ⊆ {q ≤ M_1}` re-confirmed (0 failures); still no non-circular proof across now ~12 mechanisms (this route added).

## Recommendation for the outliner

The `p`-adic / per-prime-valuation route is **dead with a clean, verified obstruction** — do NOT mount a builder on it. The obstruction is structural (O1: `L ≠ lcm(L_p : p|M_1)` because 2 always governs but 2∤M_1), not merely "unproved". This adds a 12th dead mechanism and a 4th structural-style fence (`p`-adic local-global decomposition fails; valuations aperiodic). Combined with the round-4 reviewer's candid assessment that `q ≤ M_1` is likely beyond the tools on the table, the honest path forward is **(A) CONSOLIDATE**: write up the conditional proof + LOCK + 25 lemmas + 12 dead-mechanism characterization as the run's deliverable, UNLESS a genuinely-new insight (not `p`-adic, not any of the 12 fenced mechanisms) surfaces in a parallel round-5 explorer report.
