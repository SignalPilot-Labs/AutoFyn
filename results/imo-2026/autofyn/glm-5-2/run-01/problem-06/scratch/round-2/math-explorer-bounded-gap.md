# imo-2026-06 — bounded-gap (γ) lens

Scout of the γ framing (`bounded-gap-lcm-reduction`, currently empty held slug). The wall is `P_ess` finite. The post-stabilization machinery is DONE and certified (δ); I do not re-scout it.

## Distinct openings (each a different attack the outliner could build)

1. **mtp-monovariant route (sharpest form of the β gap bound).** Define `mtp(M_n) = min{∏_{p∈T} p : T transversal of M_n}` (min transversal *product*). Empirically this is the *exact* quantity bounding gaps, and it is a clean monovariant (see Candidate techniques). This is the genuinely different framing: it attacks finiteness via a *bounded monovariant on the family* rather than via density (α) or Bertrand-eviction (β) or ω-induction (ε). The target is "mtp bounded ⟹ gaps bounded ⟹ (via lcm reduction) P_ess finite."

2. **"Fixed-coordinate lcm reduction" route (the γ mechanism proper).** Once gaps `d_n ≤ G`, reduce `a_n mod L` with `L = lcm(1,…,G)`; the residue set is finite; argue the residue sequence is eventually periodic; periodicity ⟹ only finitely many primes ever appear ⟹ `P_ess` finite. This is the dispatch's proposed escape; the *transition-is-finite-state* sub-step is the load-bearing crux (see Small-case notes / honest obstruction).

3. **`{2,p}`-transversal route (structural, unconditional-ish).** In every non-collapsing example there is a prime `p` (often dividing `a_1`, sometimes a newcomer like 3) with `{2,p}` (or `{3,p}`) a transversal of the *stabilized* `M*`, giving `mtp = 2p` or `3p`. Proving "some small two-prime transversal persists forever" would bound `mtp` unconditionally. This failed as `2·pmax(a_1)` (see counterexample) but a weaker "some small-prime transversal always exists" may survive.

4. **greedy=cyclic-successor *during* transient (unconditional periodicity of residues mod mtp).** Even before `M` stabilizes, once `mtp` stabilizes at a value `G`, the residue `a_n mod G'` (for `G'` a multiple of the witness transversal product) may already follow a deterministic successor — because multiples of the witness transversal `T` are *always* valid candidates (they hit every current and future minimal that `T` hits). If `T` remains a transversal forever, gaps are ≤ `∏T` from that point on, giving a self-contained bounded-gap proof *without* first knowing `M` finite. This is the most promising single opening: identify a *permanent* small transversal.

## Candidate technique(s)
- **Monovariant + well-founded descent** (KB "Invariants & monovariants"): `mtp(M_n)` is integer-valued, monotone non-decreasing (PROVABLE from Lemma 3 — transversals shrink under refinement, so the min over a smaller set only grows). If bounded above, it stabilizes.
- **Finite-state / lcm reduction** (KB "Modular arithmetic, CRT"; KB "Order of an element, Fermat/Euler — eventual periodicity mod m"): bounded coordinate ⟹ reduce mod lcm ⟹ finite states ⟹ eventually periodic.
- **Pigeonhole / extremal** (KB "Pigeonhole / extremal"): only finitely many primes ≤ G; if a term has many prime factors, two collide — force structure by counting small primes (cf. aimo-0415 crux).

## Cheap-kill candidates
- **Monotonicity of mtp is a one-line corollary of Lemma 3** (transversals shrink under refinement) — no computation. Ship this immediately; it converts "gap bound at promotion" (β Lemma 5, circular-feeling) into a clean global monovariant `G_n := mtp(M_n)` with `d_n ≤ G_n ≤ G_{n+1}`.
- **`a_1` even ⟹ immediate collapse to `{2}`** (singleton-freeze): gaps = 2, trivial. The hard case is odd `a_1` with ≥ 2 distinct prime factors; even `a_1` and single-prime-power `a_1` are already solved by the freeze lemma. Prune these before any heavy work.
- Parity / 2-stickiness: in every nontrivial example `2 ∈ P_ess`. A cheap structural fact to prove: if `a_1` is odd with ≥2 prime factors, `2` enters by step 2 (next multiple of an odd factor is even). Whether `2` is *permanent* is the open sub-claim.

## Knowledge-base entries to use
- **Invariants & monovariants** (monovariant + descent template for `mtp`).
- **Modular arithmetic, CRT** (the lcm-reduction / free-rider-invisibility step, already used in δ).
- **Order of an element, Fermat/Euler** ("sequences are eventually periodic mod m" — the finite-state→periodicity step).
- **Pigeonhole / extremal principle** (small-prime counting).
- **Three-gap / Steinhaus theorem** — *possibly* relevant: the cyclic-successor gap structure on `R mod L` is a three-gap-type object; not load-bearing for the wall, skip unless the outliner wants the post-stabilization gap-shape (already DONE in δ).

## Analogous past problems (cruxes)
1. **`aimo-0678` (IMO-SL 2015, NT).** Crux: "Once one coordinate (`a_n`) of a coupled recurrence is bounded, reduce the other (`b_n`) modulo `M = lcm` of the bounded values; since `gcd(a_n,b_n)=gcd(a_n, b_n mod M)`, the pair `(a_n, r_n)` determines the next step ⟹ finite state ⟹ eventually periodic." **This is the exact γ template**: bound-the-coordinate → lcm-reduce → finite-state → periodic. *Adaptation:* "gap `d_n` bounded" plays "coordinate `a_n` bounded"; `L=lcm(1..G)` plays `M`; the state must encode enough of `M_n` to make the greedy successor a function of the state. *Where it breaks:* in 0678 the transition `b_{n+1}` is a *closed formula* in `(a_n,b_n)`, so reducing mod M is automatic; in P6 the greedy successor depends on the *whole history* via `M_n`, so "finite state determines next step" is NOT automatic — the outliner must show bounded gaps force `M_n` itself into a finite state (e.g. `M_n` determined by `a_n mod L` once `L` is divisible by every prime that can ever be essential — which is the conclusion, slightly circular). **Strong but partial analogy.**
2. **`aimo-0477` (IMO-SL 2018, NT).** Crux: "`d_n = gcd(a_1, a_n)` is nondecreasing and divides the fixed `a_1`, hence a divisor chain of a fixed integer ⟹ stabilizes." *Adaptation:* `mtp(M_n)` is monotone non-decreasing; IF one proves `mtp` is bounded above by a fixed integer (analogue of `a_1`), then it is a bounded monotone integer sequence ⟹ stabilizes. *Where it breaks:* in 0477 the bound `d_n | a_1` is *free* (gcd divides a fixed term); in P6 the bound on `mtp` is the open claim — there is no fixed integer a priori dividing `mtp`. So 0477 supplies the *template* (bounded monotone ⟹ stabilize) but not the bound. **Honest partial analogy — useful for the stabilization step, not the boundedness step.**
3. **`aimo-0415` (IMO-SL 2011, NT).** Crux: "only 8 primes below 20; if a product of 9 factors is 20-smooth, two factor-prime-powers share a prime — pigeonhole among the *small* primes forces a collision / large prime power." *Adaptation:* if `mtp ≤ G`, only primes ≤ G can appear in a witness transversal; a new essential prime `q > G` cannot be the unique connector because... (the dispatch's "unique connector" claim). *Where it breaks:* the 0415 pigeonhole is over a *fixed* set of small primes in a finite product; in P6 the "unique connector" argument does NOT obviously forbid `q > G` — a large prime `q` can be the unique connector between two minimals whose introducing terms are value-distance ≥ `q` apart, perfectly consistent with gaps ≤ `G < q` (terms between them are hit by the rest of the minimal). **Weak analogy — do not rely on "only primes ≤ G connect"; the dispatch's stated consequence is not automatic.**

## Prior progress
- δ `transversal-single-cycle-finish` — certified conditional theorem (DONE). γ is empty/held.
- β `bertrand-dickson-eviction` Lemma 5 (certified, unconditional, in `lemmas/gap-bound-at-promotion.md`): `a_i - a_{i-1} ≤ ∏_{p∈O} p` where `O = P(a_i) ∩ P_{ess,i-1}` is the old-essential transversal part. This is the *predecessor* of the mtp observation; γ's contribution is to take the **min** over all transversals (=`mtp`) and prove it is a **monotone bounded monovariant**, converting Lemma 5's `$a_{i-1}$-dependent` bound into a *global* one.
- The field has NOT yet registered γ. The `mtp` monovariant and its monotonicity-from-Lemma-3 are *new* findings (this report).

## Dead ends (do not retry)
- **Bertrand postulate evicts large primes** (β) — dead: no dyadic interval is forced to contain a new essential prime (β builder admitted).
- **Ever-minimal supports form an inclusion-antichain** (β) — dead: `a_1=30` gives `{2,3,5}∈M_1` then `{2}∈M_2`, refinement creates subset pairs (round 1, corrected).
- **Dickson/WQO on the support family** (β) — moot: conditional on a finite universe bound, which *is* the wall.
- **`mtp ≤ 2·pmax(a_1)` (unconditional in a_1's prime factors)** — **FALSE** (this report): `a_1=175=5²·7` gives `mtp_final = 21 = 3·7`, exceeding `2·pmax(a_1)=14`; the prime 3 enters during evolution. So a bound purely in `a_1`'s factor set is too naive; the bound (if it exists) must account for primes that enter (e.g. `mtp ≤ p_small · p_least_factor` for some small entering prime). Do not assert `2·pmax(a_1)`.

## Small-case / intuition notes (CONJECTURE unless marked PROVABLE)

**PROVABLE (from Lemma 3):** `mtp(M_n)` is monotone non-decreasing. (Refinement shrinks the transversal set; min over a smaller set is ≥.)

**PROVABLE (sharpened Lemma 5):** `d_n = a_{n+1}-a_n ≤ mtp(M_n)` for all `n`. (The witness `T` achieving `mtp` is a transversal; multiples of `∏T` are valid; smallest multiple above `a_n` is within `∏T = mtp`.)

**CONJECTURE 1 (bounded mtp):** `mtp(M_n)` is bounded above by a finite constant depending on `a_1` (and possibly small entering primes). Empirically `mtp` stabilizes in ≤ 6 steps to a small value (`6,10,14,21,22,26,34` across `a_1 ∈ {15,35,77,175,143,2431,323,4199}`); never grows unboundedly in any tested seed (40+ seeds, including `5005` with 28 essential primes → `mtp=10`).

**CONJECTURE 2 (permanent small transversal):** There is a small (size ≤ 2, product ≤ ~pmax) transversal `T*` of `M_n` for ALL sufficiently large `n` (often from `n` small). In every nontrivial example some `{p,q}` (small primes) is a transversal of the *stabilized* `M*`. If `T*` can be exhibited *without* knowing `M` finite (e.g. `{2, p}` where `p` is the smallest prime factor of `a_1` — works for 15,77,143,323,91, but FAILS for 175,385,4199,2431 where the needed second prime is a newcomer like 3 or 7), gaps are bounded unconditionally. **This is the crux of the γ framing.**

**CONJECTURE 3 (bounded-gap → P_ess finite):** IF gaps ≤ `G` for all `n`, THEN `P_ess` is finite. **HONEST OBSTRUCTION (do not hand-wave):** bounded gaps alone do NOT obviously forbid a large essential prime `q > G`. A new essential `q ∈ M` (minimal) forces another term `a_j` with `q | a_j` (else `M\{q}` would be a transversal and `M` non-minimal); `a_j - a_i ≥ q > G` is consistent with gaps ≤ G (many small-gap terms in between, all hit `M\{q}`). So the "unique connector" forbidding argument sketched in the dispatch is **not automatic**; the outliner must either (a) prove the transition `a_{n+1} mod L` is a function of a *finite* state that captures `M_n` (the 0678 template), or (b) find a different consequence of bounded gaps that pins `P_ess`. The cleanest path: bounded gaps ⟹ `a_n mod L` takes ≤ L values ⟹ two terms `a_i ≡ a_j (mod L)` with `a_j - a_i` a positive multiple of `L` ⟹ `a_j - a_i` divisible by every prime ≤ G ⟹ gcd-reuse; but converting this to "M_n stabilizes" still needs the finite-state-transition lemma. **Flag this as the real sub-gap inside γ.**

**Empirical max-gap values (CONJECTURE-bound, all stabilize quickly):**
| a_1 | max gap | mtp_final | notes |
|---|---|---|---|
| 15=3·5 | 6 | 6=2·3 | {2,3} permanent transversal |
| 77=7·11 | 14 | 14=2·7 | {2,7} |
| 143=11·13 | 22 | 22=2·11 | {2,11} |
| 323=17·19 | 34 | 34=2·17 | {2,17} |
| 35=5·7 | 10 | 10=2·5 | {2,5} |
| 175=5²·7 | **21** | 21=3·7 | {2,·} fails; {3,7} is the transversal; 3 enters |
| 385=5·7·11 | 14 | 14=2·7 | {2,7} |
| 429=3·11·13 | 6 | 6=2·3 | {2,3} |
| 5005 | 10 | 10=2·5 | {2,5}; 28 essential primes but tiny mtp |

**Bottom line for the outliner:** the γ framing's sharpest asset is the **`mtp` monovariant** (monotone by Lemma 3, bounds gaps by sharpened Lemma 5). The open work is (i) prove `mtp` bounded (CONJECTURE 1) — the `2·pmax(a_1)` guess is dead (175), so the bound must come from a *permanent small transversal* argument (CONJECTURE 2), which is the genuine new idea to develop; (ii) prove bounded-gap ⟹ `P_ess` finite (CONJECTURE 3) — NOT automatic, needs the 0678 finite-state-transition template adapted, and the "unique connector" shortcut should NOT be relied on. γ is viable and *far apart* from α/β/ε (it never invokes density, Bertrand, or ω-induction), but it has two real sub-gaps, not one.
