## imo-2026-06 — analogy & corpus route

### Terrain (known-analogy shape + how this problem differs)

This is a **greedy gcd sequence** problem, kin to the EKG sequence / Yellowstone permutation family, but with a *much* stronger coupling: each new term must share a prime factor with **every** prior term, not just the previous one. That stronger condition is what makes the sequence eventually an arithmetic progression (EKG/Yellowstone are only conjectured/known to be permutations, not APs — the contrast is the whole point).

Empirically (computed, **conjecture not proof**):
- `a_1` **even** ⇒ `a_n = a_1 + 2(n−1)` for all `n` (T=1, L=2). *Proof is a clean one-line induction* (see Openings).
- `a_1 = p^k` a prime power (p odd) ⇒ `a_n = a_1 + p(n−1)` (T=1, L=p).
- `a_1` odd with ≥2 prime factors ⇒ genuinely periodic differences after a short preperiod. Examples (period pattern, T, L):
  - `a_1=15=3·5`: diffs cycle `[3,2,4,6,6,4,2,3]`, T=8, L=30.
  - `a_1=35=5·7`: T=34, L=210.
  - `a_1=77=7·11`: T=18, L=154.
  - `a_1=105=3·5·7`: T=58, L=210.
  - `a_1=315=3²·5·7`: period > 2000 (long, but max diff still ≤ 6).
- In **every** sampled case the **maximum difference `max_n d_n = 2·p_min(a_1)`** when `a_1` is odd (e.g. 15→6, 35→10, 77→14, 105→6). This is the tight empirical bound.
- A looser but **cleanly provable** bound: `d_n ≤ M_1 := lcm(primes(a_1))`. Mechanism: candidate `m = a_n + M_1` is a multiple of every prime factor of `a_1`, and every `a_i` is divisible by some prime factor of `a_1` (since `a_i` must share a prime with `a_1`), so `m` shares a factor with every `a_i`. ✓ (verified computationally on many starts).

**Key structural fact (verified): every `a_n` is divisible by some prime factor of `a_1`** (call this set `P_1`). This is the load-bearing invariant: it means future candidates can always hit any `a_i` via a prime in `P_1` (a *small* prime), so large prime factors that appear in late `a_n` (e.g. `975 = 3·5²·13`) are **never the unique way to share** — the small P_1-factor of `975` (namely 3 or 5) always suffices. This is what makes the "governing prime set" finite even though "primes appearing" is infinite.

How this differs from EKG/Yellowstone: those require sharing only with the *previous* term, so the binding constraint is local and one prime at a time suffices — the sequence roams. Here the binding constraint is *global* (hit every prior term), which forces a finite hitting-set of small primes and hence finite state.

### Retrieval hits (concrete crux moves / knowledge_base entries)

**Crux corpus (number_theory, filtered then scanned):**

- **`aimo-0678` (IMO-SL 2015 N4)** — *best analogy.* Statement: coupled `a_{n+1}=gcd(a_n,b_n)+1`, `b_{n+1}=lcm(a_n,b_n)−1`; prove `(a_n)` eventually periodic. Three crux moves that ARE the standard proof shape:
  1. Find an invariant/monovariant to **bound one coordinate** (monovariant = least integer `≥ a_n` not dividing a frozen sum; never increases).
  2. Once bounded, **reduce the other coordinate mod `M = lcm` of bounded values** — the state pair becomes a deterministic map on a finite set.
  3. Finitely many states ⇒ eventually periodic.
  *Direct adaptation target:* our `d_n` is the bounded coordinate; reduce `a_n mod M` for a fixed `M` and argue the next move is a function of the residue.
- **`aimo-0503` (IMO-SL 2008 N3)** — "Bound the gap between two consecutive terms from below by their gcd, since the gcd divides their positive difference." Adapts to: bound `d_n` *above* by exploiting that the candidate must be a multiple of some small prime hitting each `a_i`.
- **`aimo-0520` (USA-TST 2015 2)** — CRT to satisfy a family of divisibility constraints simultaneously; "extend a coprimality-structured construction by appending a brand-new prime." Hint for the hitting-set / modulus `M = lcm(P)` construction.
- **`aimo-0171` (Germany-TST 2018)** — periodic walk mod `n`: "iteratively jump to the nearest later index that closes a zero-residue window, step length bounded by the period"; pigeonhole on `n+1` chain positions mod `n`. The modular-walk + pigeonhole skeleton is the same skeleton we need.
- **`aimo-0727` (IMO-SL 2023 N5)** — "for an integer sequence that can rise by at most 1 each step yet is unbounded, take the smallest index where it first reaches a target value N." Minimal-counter / descent flavor; adaptable for pinning the periodic regime.

None of these is a literal match — our condition (share with *all* prior terms) is stronger than any of them — but `aimo-0678` is a genuine structural sibling (bound-then-reduce-mod-M-then-pigeonhole).

**`knowledge_base.md` entries to use:**
- **Modular arithmetic, CRT** — the modulus `M = lcm(P)` construction and reducing the state mod `M`.
- **Order of an element, Fermat/Euler: periodicity of `a^n mod m`; eventual periodicity of products of a sequence mod `m`** — direct citation for "deterministic map on a finite residue set ⇒ eventually periodic."
- **Pigeonhole / extremal principle** — `n+1` states among `M` residues ⇒ repeat ⇒ period.
- **Invariants & monovariants** (combinatorics section) — for bounding `d_n` (analogous to `aimo-0678`'s monovariant).
- **Bertrand's postulate** — possibly useful to bound a "next prime enters" event, though the clean `M_1` bound probably supersedes it.

### The standard proof shape for "greedy gcd sequence ⇒ eventual AP" and its load-bearing lemmas

The shape (adapted from `aimo-0678`):

1. **(Cheap kill) Even `a_1`.** If `2 | a_1`, induction gives `a_n = a_1 + 2(n−1)`: `a_n+1` is odd so `gcd(a_n+1, a_n)=1` fails; `a_n+2` is even and shares factor 2 with every prior (all even). Done, T=1, L=2. *[Provable; trivial.]*
2. **Bound the step.** `d_n = a_{n+1} − a_n ≤ M_1 := lcm(P_1)`, `P_1 = primes(a_1)`. Mechanism: `a_n + M_1` is a multiple of every `p ∈ P_1`; every `a_i` is divisible by some `p ∈ P_1`; hence `a_n+M_1` is a valid candidate. *[Provable; clean.]* Tighter conjectured bound `d_n ≤ 2·p_min(a_1)` is the empirical crux.
3. **Finite governing set / state reduction mod M.** Take `M = lcm({primes ≤ M_1})` (or `M = lcm(1,2,…,M_1)`, a fixed constant). Show the smallest valid candidate `> a_n` depends only on `a_n mod M` (and the eventually-stabilized set of residues `{a_i mod M}`). **Crux gap:** prove large primes (`> M_1`) never govern — i.e., the smallest valid `m` equals the smallest `m` that hits every `a_i` via a prime `≤ M_1`. The mechanism: every `a_i` has a `P_1`-factor, so it can always be hit by a small prime; a candidate relying on a large prime `q > M_1` would need `q | m` with `m` within `M_1` of `a_n`, and simultaneously hit `a_1` (forcing a `P_1`-factor of `m`), making it no smaller than the small-prime candidate. (This is the load-bearing step that needs a rigorous proof — see Hard steps.)
4. **Residue set stabilizes.** `{a_i mod M : i ≤ n}` is a subset of the finite set `(ℤ/Mℤ)`, eventually constant once no new residue ever appears (pigeonhole + bounded step ⇒ only finitely many residues are ever hit; once all are hit, the set is fixed).
5. **Deterministic finite-state map ⇒ eventual periodicity.** Once the residue set `R` is fixed, `a_{n+1} mod M = F(a_n mod M; R)` for a deterministic function `F`. So `(a_n mod M)` follows a map on a finite set ⇒ eventually periodic with period `T`. Then `a_{n+T} ≡ a_n (mod M)` and `d_{n+T} = d_n`, so `a_{n+T} − a_n` is a constant `L` (multiple of `M`). ∎

Load-bearing lemmas in order of difficulty:
- **(Easy)** Every `a_n` has a prime factor in `P_1`.
- **(Easy)** `d_n ≤ M_1 = lcm(P_1)`.
- **(HARD — crux)** The smallest valid candidate is determined by small primes only (large primes never govern); equivalently, the next-move function is `mod M`-local. *This is the wall.*
- **(Medium)** Residue set stabilizes (follows from bounded step + finite residues + the "no new residue" argument).
- **(Easy)** Finite-state map ⇒ eventual periodicity mod `M` ⇒ eventual AP.

### Hard steps / gaps specific to adapting here

**Gap 1 (THE crux): large primes don't govern.** The clean bound `d_n ≤ M_1` lets `a_{n+1}` have large prime factors (e.g. `a_{25}=105=3·5·7` for `a_1=15`; later terms reach `975=3·5²·13`). For the mod-`M` finite-state argument to work, we need that the *smallest* valid candidate never relies on such a large prime. The attempted mechanism: every `a_i` is hit-able via a `P_1`-prime (≤ `p_max(a_1)` ≤ `M_1`), so a candidate using only primes ≤ `M_1` always exists within `M_1` of `a_n`; any candidate using a prime `q > M_1` must still hit `a_1` (forcing a `P_1`-factor, hence a multiple of `p·q > M_1·p`), so it cannot be *smaller* than the small-prime candidate. **This needs a rigorous proof** — the subtlety is that a candidate could use *several* large primes simultaneously (one per `a_i`), and the interplay isn't obviously bounded. Empirically safe (max `d_n = 2·p_min ≪ M_1`), but the clean argument is the open step.

**Gap 2: which primes survive as governing.** Even after Gap 1, the *set* of governing primes (`P_1` plus "discount" primes like 2, and possibly others ≤ `M_1`) and the modulus `M` must be pinned. Empirically `M = lcm(governing primes) = L` (the eventual step): `15→30`, `35→210`, `77→154`, `105→210`, `65→390`. The governing set is *not* just `P_1 ∪ {2}` (e.g. `a_1=65=5·13` gives `L=390=lcm(2,3,5,13)`, so 3 entered as a discount prime not in `P_1 ∪ {2}`). Characterizing the governing set is part of the proof — but for *existence* of `T,L` it may suffice to take `M = lcm(1,2,…,M_1)` (a safe over-modulus) and not identify the exact governing set.

**Gap 3: preperiod / stabilization.** Need an index `N` after which the residue set is stable. With `d_n ≤ M_1` and residues in `ℤ/Mℤ`, after at most `M` distinct residues the set is complete; but "no new residue ever" needs an argument that the deterministic map doesn't generate new residues. Bounded step + finite residues + pigeonhole gives eventual periodicity of the *trajectory* even without explicitly finding `N` — standard.

**Gap 4 (if pursuing the tighter bound): `d_n ≤ 2·p_min`.** Empirically exact, but I could not find a clean proof. Likely needs an invariant tracking which primes are "active." Optional — the `M_1` bound already suffices for the proof shape; the tight bound just gives a smaller `M`.

### Openings for the outliner (distinct approach skeletons)

**Opening A — "Bound-then-reduce-mod-M" (the `aimo-0678` route, safest).**
(i) Even case: trivial AP L=2. (ii) Odd case: prove `d_n ≤ M_1 = lcm(P_1)` via the `a_n + M_1` candidate (clean). (iii) Take `M = lcm(1,2,…,M_1)`. Prove the **crux lemma**: smallest valid candidate = smallest small-prime-hitting candidate (large primes `> M_1` never govern). (iv) Residue set in `ℤ/Mℤ` stabilizes; `(a_n mod M)` is a deterministic finite-state trajectory ⇒ eventually periodic; differences eventually periodic ⇒ `a_{n+T}=a_n+L`. *Risk: crux lemma (Gap 1) is the wall.*

**Opening B — "Active-prime monovariant" (tighter, riskier).**
Track the set `A_n` of "active/governing primes" (primes `p` such that some `a_i, i≤n` has `p | a_i` and `p ≤ 2·p_min(a_1)`). Conjecture: `A_n` is non-decreasing and stabilizes to a fixed set `A` (empirically `A ⊆ {primes ≤ 2·p_min}`); prove `d_n ≤ 2·p_min` via an invariant on `A_n`. Once `A` stable, `M = lcm(A)` and reduce mod `M` as in Opening A. *Risk: the `2·p_min` bound (Gap 4) is the wall; if it falls, this opening collapses to A.*

**Opening C — "Hitting-set / boolean formula on residues" (combinatorial reframe).**
Reframe: at step `n`, the candidate must satisfy a boolean formula `Φ_n(m) = ∧_{i≤n} (∨_{p | a_i} [p | m])`. Show `Φ_n` depends only on `m mod M` for a fixed `M` (because every clause has a `P_1`-literal, and small-prime literals suffice). Then `Φ_n` is eventually constant (as a boolean function on `ℤ/Mℤ`) since only finitely many such functions exist; once constant, the smallest `m > a_n` satisfying it is a function of `a_n mod M` ⇒ periodic. *This is Opening A phrased as a boolean-formula stabilization problem — same crux lemma, but the framing makes "finite boolean functions on `ℤ/Mℤ`" the pigeonhole target, which is clean.*

---

**Scout's summary for the outliner:**
- *Cheap kill first:* separate even `a_1` (trivial, one-line induction, L=2). For odd `a_1`, also handle prime-power `a_1 = p^k` separately (trivial, L=p).
- *Provable core:* `d_n ≤ lcm(P_1)` via the `a_n + lcm(P_1)` candidate — this is the entry lemma.
- *The wall:* "large primes never govern" (Gap 1). Three openings (A/B/C) all route through it; A is safest, C is the cleanest framing, B is the tightest but riskiest.
- *Endgame (once wall falls):* standard finite-state-mod-`M` → pigeonhole → eventual periodicity → AP. Cite `aimo-0678` as the structural sibling and the KB entries "Modular arithmetic, CRT" + "Order of an element… eventual periodicity of products of a sequence mod m" + "Pigeonhole/extremal."

**Prior progress:** none (round 1, workspace empty).
**Dead ends:** none yet.
**Small-case / intuition notes (all conjecture, labeled):** max `d_n = 2·p_min(a_1)` (odd `a_1`); `L = lcm` of the surviving governing primes (subset of primes ≤ `2·p_min`); period `T` can be large (≥2000 for `a_1=315`) but always exists.
