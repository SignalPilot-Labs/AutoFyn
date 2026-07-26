## imo-2026-06 — SIEVE / COVERING-SYSTEM & eventual-periodicity route

### The real claim & the greedy reframing

`a_{n+1}` = smallest `m > a_n` with `gcd(m, a_i) > 1` for **every** `i ≤ n`. Equivalently `m` is **not coprime to any** prior term. Reframe as a sieve:

- For a fixed term `a_i` with prime set `S_i`, `{m : gcd(m, a_i) = 1}` = the unit classes mod `rad(a_i)` = complement (in `Z`) of `∪_{p ∈ S_i} pZ`.
- So the **allowed set** at stage `n` is
  `A_n := ∩_{i≤n} ∪_{p | a_i} pZ` = integers hitting every `S_i`,
  and `a_{n+1} = min(A_n ∩ {m > a_n})`.
- `A_n` is periodic mod `R_n := rad(∏_{i≤n} a_i)` (product of all distinct primes seen so far). It is an **intersection of finite unions of arithmetic progressions** (multiples of primes) — a covering-system / complement-of-covering object.

The "smallest > a_n" greedy means: `a_{n+1} − a_n` = gap to the next allowed residue class. Once `A_n` is periodic mod a fixed `L` and `a_n mod L` is in the periodic regime, the gap depends only on `a_n mod L`; the residue walk on `Z/LZ` is a deterministic map on a finite set, hence eventually periodic; lifting gives `a_{n+T} = a_n + L`. **That is the skeleton this route hands the outliner.** The whole difficulty is the word "once".

### Distinct openings this route suggests (rival approaches for the outliner)

1. **Covering-system stabilization mod L (the core sieve route).** Show `A_n mod L` stabilizes to a fixed union of residue classes for some `L`, despite `R_n → ∞`. Key sub-lemma needed: only **finitely many primes are essential**; every prime `q` appearing late has its constraint "`m` hits `q`" already implied mod `L` (because `q` co-appears with an essential prime, or its residue class is already forbidden). Then the residue walk on `Z/LZ` is eventually periodic.
2. **Finite-state / pigeonhole without naming L.** Pick `M = rad(a_1)·(product of "forced" primes)` and define a finite state = `(a_n mod M, recent residue tuple mod M)`; show the greedy transition is a deterministic function of state (next valid `m` lives in a bounded window above `a_n`, so `a_n mod M` determines it). Pigeonhole ⇒ a state repeats ⇒ `a_{n+T} ≡ a_n (mod M)` ⇒ lift to `a_{n+T}=a_n+L`. The crux is bounding the next-valid window and picking `M` rich enough.
3. **Translation self-similarity (constructive, from-start).** Numerics (see below) suggest periodicity often holds **from `n=1`**, so guess `T, L` and prove the greedy rule commutes with `m ↦ m+L`: verify `{a_1,…,a_T}` and `L` satisfy that the allowed-set-above-`a_T` is exactly `L` + (allowed-set-above-`a_1`, restricted). Then induction carries it forever. Needs an explicit self-similarity equation for `L` in terms of the seed.
4. **Anchor-prime AP sub-case + reduction to the hard case.** Cheap kills first: if `2 | a_1` then `L=2, T=1` (one-line proof, verified); if `a_1 = p^k` then `L=p, T=1`. More generally if some prime divides **every** term, done. So WLOG reduce to `a_1` odd, squarefree, ≥2 prime factors, and **no prime divides all terms**. This is where the real covering-system machinery is needed; the reduction prunes ~half the casework.
5. **Monovariant on the "essential prime set".** Track `E_n = {primes whose removal changes A_n mod (current candidate L)}`. Conjecturally `E_n` is non-decreasing then constant (stabilizes), giving the finite essential set. A monotone-bounded set ⟹ stabilization ⟹ periodic regime.

### Candidate technique(s)
- Covering systems / complement of a union of arithmetic progressions; periodicity of a finite union of residue classes.
- Deterministic finite-state walk on `Z/LZ` ⟹ eventual periodicity (pigeonhole).
- CRT / reduction mod `rad`-products; `gcd`-structure of consecutive integers (`gcd(k,k+1)=1`) for window bounds.
- Invariant: translation-equivariance of the greedy rule once `A_n` stabilizes mod `L`.

### Cheap-kill candidates
- **`2 | a_1` ⟹ `L=2, T=1`** (VERIFIED for all tested even `a_1`). Proof: `gcd(a_1+1,a_1)=1`; `gcd(a_1+2,a_1)=gcd(2,a_1)≥2` so `a_2=a_1+2`; then `a_1,a_2` both even ⟹ every constraint "gcd(m,a_i)>1" is met by any even `m` ⟹ `a_{n+1}=a_n+2` by induction. **This handles every even `a_1` in one paragraph.**
- **`a_1 = p^k` (odd prime power) ⟹ `L=p, T=1`** (verified: 9→3, 25→5, 27→3, 49→7, 121→11). Same argument: all terms multiples of `p`.
- **Anchor takes over:** if `a_1 = p·q` (odd primes, `p<q`) and the greedy never escapes multiples of `p`, then `L=p`. Verified for `(3,7)→3`, `(3,11)→3`, `(5,11)→5`, `(3,7,11)=231→3`, `(3,7,13)=273→3`. But the boundary is **path-dependent and non-trivial** (see below) — not a clean casework, so use only as a sub-lemma, not a full case split.
- A bounded-window injection: since multiples of `rad(∏_{i≤n} a_i)` are always allowed, `a_{n+1}` lies within `O(R_n)` of `a_n`; not sharp enough alone but bounds the search.

### Knowledge-base entries to use
- **Modular arithmetic, CRT** (periodicity mod `rad`-products; root/residue counts).
- **Order of an element, Fermat/Euler** / "sequences are eventually periodic mod `m`" (the finite-state residue walk).
- **Invariants & monovariants** (the essential-prime-set stabilization).
- **Pigeonhole / extremal** (state recurrence on `Z/LZ`).
- **Divisor analysis, gcd structure of consecutive integers** (window bounding via `gcd(k,k+1)=1`).
- *Mirsky–Newman / covering-system periodicity* is **not** in `knowledge_base.md` — flag for the outliner: the complement-of-covering structure points to it but cannot be cited; any covering-system step must be re-proved.

### Analogous past problems (cruxes)
**None truly analogous.** The crux corpus has no EKG/Yellowstone/greedy-non-coprime-sequence entry. Closest loose hints (adapt, do not cite):
- `aimo-0079` (NT, sequences-and-recurrences) — *"substitute `x=m−a` so `P(m−a)=m(m+(b−a))`; balanced for all large `m` forces `Ω`-parity periodic with a fixed shift."* Adaptable as the **translation self-similarity** idea: a functional equation under a fixed shift forces periodicity.
- `aimo-0134` (NT, sequences-and-recurrences) — *"recover an original term from consecutive partial-sum averages via a difference identity, transferring eventual-constancy back to the sequence."* Adaptable for the **lift from mod-`L` periodicity to `a_{n+T}=a_n+L`**.
- `aimo-0030` (NT, divisibility-and-gcd) — *"read losing positions off a coprime-game recursion as a non-adjacency class."* Loosely related (coprime structure ↔ recursion).

### Prior progress
None — round 1, workspace empty, no approaches/lemmas/ranking yet.

### Small-case / intuition notes (all CONJECTURE from numerics, not proof)

Strong conjecture, verified for `a_1 ∈ {2,3,…,20,21,22,25,27,33,35,49,55,65,77,91,105,143,165,210,231,273,1001}` with up to 200–1100 terms: **`a_{n+T}=a_n+L` holds, and in most cases from `n=1`** (no transient). Examples of `(a_1; T, L)`:
- `15 (3·5)`: `T=8, L=30 = 2·3·5`
- `35 (5·7)`: `T=34, L=210 = 2·3·5·7`
- `77 (7·11)`: `T=18, L=154 = 2·7·11`
- `91 (7·13)`: `T=20, L=182 = 2·7·13`
- `105 (3·5·7)`: `T=58, L=210`
- `143 (11·13)`: `T=64, L=858 = 2·3·11·13`
- `165 (3·5·11)`: `T=86, L=330 = 2·3·5·11`
- `1001 (7·11·13)`: `T=282, L=2002 = 2·7·11·13 = 2·a_1`
- even `a_1` or prime power: `T=1`, `L=2` resp. `L=p`.

**CRITICAL FACT (verified, not conjecture): the prime set `P` is INFINITE.** For `a_1=15`, the sub-sequence `a_{8k+6} = 36 + 30k = 6(6+5k)` (verified `k=0..8`), and `6+5k` is unbounded ⟹ unbounded prime factors ⟹ `P` infinite. Same for the periodic sub-sequences of every tested non-trivial case. **Consequence: the naive framing "show `P` stabilizes" is DEAD — do not attempt it.** The periodicity must coexist with infinitely many primes appearing.

Observed structure of `L`: `L = 2 · (product of an "essential" prime subset)`, where the essential primes are `2` plus a path-dependent subset of `a_1`'s prime factors (and sometimes `3`, even when `3 ∤ a_1`, e.g. `a_1=35, 143`). No clean formula for `L` in terms of `a_1` was found — `L` is `2·rad(a_1)` only sometimes (`77, 91, 105, 1001`); `35` adds `3`, `143` adds `3`, `15` has `L=2·rad`. The outliner should **prove existence of `L` without computing it** (finite-state / pigeonhole route), or derive `L` from a self-similarity equation (route 3).

The "anchor takes over" boundary is path-dependent: `(5,13)=65` does NOT collapse to `L=5` (interleaving at `78=2·3·13` reintroduces `13`) whereas `(5,11)=55` does (because `66=2·3·11` fails to hit the prior term `65`). So no simple `q ≥ 2p`-type threshold — do not casework on `(p,q)`.

`a_1=315, 385`: period not found within 1100 terms (`T > 600` or a long transient) — so the outliner must prove **eventual** periodicity (what the problem asks), not assume from-start, even though from-start holds in the small cases.

### Dead ends (do not retry)
- **"Show the prime set `P` stabilizes"** — false, `P` is infinite (proven via the `a_{8k+6}=6(6+5k)` sub-sequence for `a_1=15`; same mechanism generalizes). Any approach whose first step is "stabilize `P`" collapses.
- **Characterize `L` by a simple function of `a_1`** — no clean formula; the essential-prime subset is path-dependent. Do not build a casework proof around predicting `L`.
- **`q ≥ 2p` threshold for "anchor takes over"** — fails at `(5,13)=65`. The interleaving depends on whether the candidate interposing number hits the *previous* term, which depends on the whole path so far.

### Hard steps the outliner must close
1. **Stabilization mod `L` despite infinite `P`.** Show that beyond a finite essential set `Q`, every new prime `q`'s constraint is redundant mod `L` (its residue classes are already covered, or `q` always co-appears with a prime in `Q`). This is the genuine crux of the sieve route.
2. **Finite-state determinism.** The greedy next-term depends on the *entire* prior list, not just `a_n mod M` — show the relevant information is captured by a finite state (recent residues mod `M` plus the stabilized essential structure). Pigeonhole then gives recurrence.
3. **Lift.** From `a_{n+T} ≡ a_n (mod L)` (residue periodicity) conclude `a_{n+T} = a_n + L` (exact translation), not `+ kL`. Needs a growth/monotonicity argument: the per-period increment is exactly `L` because each period advances `a` by the sum of gaps = `L`.
4. **Reduction to the hard case.** Dispose of even `a_1` and prime-power `a_1` (and ideally the single-anchor-takes-over sub-case) cleanly first, so the heavy machinery only faces odd squarefree `a_1` with ≥2 essential primes and no universal anchor.

### Distinct openings summary (one line each, for the outliner's rival-approach field)
- **Sieve-stabilization**: `A_n = ∩ ∪ pZ` stabilizes mod a fixed `L`; residue walk ⟹ periodic.
- **Finite-state pigeonhole**: don't compute `L`, prove a finite greedy-state recurs.
- **Translation self-similarity**: guess `T,L`, prove greedy commutes with `m↦m+L` from the seed.
- **Cheap-kill reduction**: even/prime-power/anchor-takes-over cases disposed first; hard case is odd squarefree ≥2 primes.
- **Essential-prime monovariant**: the set of primes that matter mod `L` is monotone-bounded ⟹ stabilizes.
