## imo-2026-06 (route: corpus analogy & known-sequence structure)

### Headline empirical discovery (CONJECTURE, verified 8/8 cases — this is the load-bearing structural finding for this route)

Let `supp(x)` = set of prime divisors of x. For the greedy sequence, define:

- `P` = the **persistent primes** = `∪` over all minimal (under ⊆) members of `{supp(a_i)}`. Empirically **finite**.
- `L = ∏_{p∈P} p` (squarefree). Always matches the eventual additive period `L`.
- `M` = the finite antichain of **minimal supports** (minimal elements of `{supp(a_i)}` under inclusion).
- A residue `r mod L` occurs in the tail **iff** `{p∈P : p|r}` is a **transversal** (hitting set) of `M`.
- `T = |R|` (number of such transversal residues), and `a_{n+T} = a_n + L` holds **from n=1** (transient length 0 in every case where the minimal-support family has stabilized).

Verification table (computed, not proved):

| a1 | factorization | P | L | T=min-support-transversal-count | predicted & verified |
|----|----|----|----|----|----|
| 15 | 3·5 | {2,3,5} | 30 | 8 | ✓ a_{n+8}=a_n+30 from start |
| 35 | 5·7 | {2,3,5,7} | 210 | 34 | ✓ |
| 45 | 3·5 | {2,3,5} | 30 | 8 | ✓ |
| 65 | 5·13 | {2,3,5,13} | 390 | 58 | ✓ |
| 77 | 7·11 | {2,7,11} | 154 | 18 | ✓ |
| 91 | 7·13 | {2,7,13} | 182 | 20 | ✓ |
| 105 | 3·5·7 | {2,3,5,7} | 210 | 58 | ✓ |
| 143 | 11·13 | {2,3,11,13} | 858 | 64 | ✓ |
| **429** | 3·11·13 | {2,3,5,11,13} | **4290** | **908** | ✓ a_{n+908}=a_n+4290 from start (verified over 1092 terms) |

The `a1=429` case is the decisive test: a naive period search with `T<400` finds **nothing** (the period 908 and the transient-absorbing structure only appear once you predict `L,P,M` from the minimal supports and *then* verify). This makes the transversal framing a genuine structural theorem, not a fitting artifact. `L` is always squarefree (rad only); primes appearing in terms but not in any minimal support (e.g. 7,11,13,… for `a1=15`) drop out of P automatically.

### Why the transversal framing is forced (mechanism, not proof)

`a_{n+1}` must satisfy `gcd(a_{n+1},a_i)>1 ∀i` ⟺ `supp(a_{n+1})` hits (intersects) every `supp(a_i)` ⟺ it hits every **minimal** support `M`. Restrict attention to primes in `P`: divisibility by `p∉P` is irrelevant (those primes never appear in a minimal support, so they're never the *sole* connector needed). Thus the admissibility of `a_{n+1}` depends only on its residue mod `L` (which primes of `P` divide it). The greedy rule "smallest `>a_n` whose residue mod `L` lies in `R` (the transversal set)" is then a **finite-state machine on `a_n mod L ∈ R`** → residue sequence is periodic → differences are periodic, with period-sum = `L` (because over a full pass through `R` the running value advances by exactly `L`: the residues are a complete residue structure).

### Distinct openings for the outliner (each a different framing — pick ≥1, they are far apart)

1. **Covering-system / residue-class finite-state framing** (closest to the corpus analogue aimo-0678 sol 2). Target: (a) prove `P` finite (only finitely many primes can sit in a minimal support — because each minimal support is a *finite* prime set and antichains of finite subsets of ℕ are... not automatically finite; needs the greedy/monotone argument: a prime `q` appears in a minimal support only if some `a_i` has `q` as an essential connector, and large primes get outbid by small composites), (b) prove `M` stabilizes, (c) reduce to the finite-state map `a_n mod L ↦ a_{n+1} mod L` on `R`, pigeonhole → periodic residues, (d) lift residue-periodicity to `a_{n+T}=a_n+L`. **Where the analogy with aimo-0678 breaks:** there the sequence is *bounded* (`a_n ≤ w_0`), so "finitely many values → finite state" is free; here the sequence is *strictly increasing and unbounded*, so the finite state must come from **residues mod `L`**, and `L`/`P`/`M` must first be shown finite and stabilizing. That extra step is the heart of the problem.

2. **Minimal-support / hitting-set (dual) framing.** Forget residues; work directly with the family `M` of minimal supports. Prove: `M` is a finite antichain; the greedy term `a_{n+1}` is the least integer `>a_n` whose support is a transversal of `M`; among numbers with a fixed P-divisibility pattern the least `>a_n` advances by a fixed amount once the pattern repeats; the patterns (transversals of `M`) are finite and the greedy cycles through them in a fixed order. This is the "pure order-theoretic" route — no CRT, just transversals and the well-ordering of the integers. It needs a lemma that the *order* in which transversals are visited is forced (the greedy always picks the smallest residue `> current`, and residues are taken in increasing value mod `L` — need to show this produces a single cycle, not several).

3. **Dickson's-lemma / well-quasi-order framing.** View `supp(a_n)` as a `0/1`-vector over the primes. The set of supports has finitely many **minimal** elements by Dickson's lemma *if* we bound the ambient prime set — but the prime set is infinite. The move: show only primes `≤ a_1` (or `≤` some bound derived from `a_1`) can be persistent, because any prime `q` larger than the smallest composite transversal of the existing minimal supports is never the unique connector (a smaller composite beats it). This bounds `P` → finite antichain → Dickson applies → `M` finite. Then route 1 or 2 finishes. This is the "kill the ambient-infiniteness" route and is likely a necessary sub-lemma for routes 1–2 anyway.

(A 4th, more speculative, framing — **Bertrand/large-prime eviction**: show directly that a prime `q` not dividing any of the first-few transversals is permanently evicted, using Bertrand to plant a small composite transversal below any `q`-forced candidate. Probably folds into route 3.)

### Candidate techniques (KB entries to use)

- **Order of an element / Fermat-Euler; eventual periodicity of products mod `m`** (KB "Number Theory") — the residue map is the engine.
- **Modular arithmetic, CRT** (KB) — `L = ∏P` squarefree, so residues mod `L` factor via CRT across the primes of `P`; the transversal set `R` decomposes coordinatewise.
- **Pigeonhole / extremal** (KB General Methods + Combinatorics) — finite-state pigeonhole on `R` for periodicity of residues.
- **Invariants & monovariants** (KB Combinatorics) — `M` (minimal-support family) is a monotone object (supports only get added; minimal elements can only be *removed* as a new minimal sub-support appears, and there are finitely many once `P` is bounded). A monovariant descent: the antichain shrinks → stabilizes.
- **Bertrand's postulate** (KB NT) — to evict large primes from `P` (route 3/4).
- **Comparability / divisibility graphs** (KB Combinatorics) — supports as a poset; minimal elements are the essential constraints.

### Corpus analogues (crux moves to adapt)

1. **`aimo-0678` (IMO-SL 2015, France) — STRONGEST analogue.** A coupled gcd/lcm recurrence `a_{n+1}=gcd(a_n,b_n)+1`, `b_{n+1}=lcm(a_n,b_n)−1`; prove `(a_n)` eventually periodic. **Crux move (sol 2, `modular-arithmetic-and-CRT`):** "Once one coordinate is bounded, reduce the other modulo the lcm of the bounded coordinate's attainable values, turning the state pair into a deterministic map on a finite set." → finite-state pigeonhole. **Adapt:** our "bounded coordinate" is the *residue mod L* (not a value), and the deterministic map is `a_n mod L ↦ a_{n+1} mod L` on `R`. **Where it breaks:** aimo-0678's sequence is bounded (so finite values free); ours is unbounded — the finite-state reduction via residues is the extra work, and the conclusion is stronger (`a_{n+T}=a_n+L`, not bare periodicity).

2. **`aimo-0680` (IMO-SL 2015, Singapore) — STRONG conclusion-analogue.** A function `f` with `(f^n(m)−m)/n ∈ ℤ_{>0}` and finite complement; **prove `f(n)−n` is periodic.** Same *conclusion shape* (periodic differences / eventual arithmetic). **Crux move (`size-bounding-and-descent`):** "When finitely many rows are known arithmetic progressions, subtract their predictable per-window element counts from each `lcm`-window `T=lcm(T_i)` to show constant positive density, pinning linear growth." → the `lcm`-window / covering-count technique. **Adapt:** the `lcm`-window (here `L=∏P`) counting of transversals is the analogue of "predictable per-window element counts." **Where it breaks:** aimo-0680 assumes the AP rows; we must *derive* the residue structure (the transversal set) from the greedy rule.

3. **`aimo-0421` (Germany TST 2022) — gcd-of-infinite-set pigeonhole.** Infinite set `S`, force a 3-tuple with prescribed gcd pattern. **Crux move (`divisibility-and-gcd`):** "Since `gcd(a, ·)` takes only finitely many values (divisors of `a`), pigeonhole an infinite subfamily with constant gcd; in the branch where a prime `p` divides infinitely many elements, normalize and split." **Adapt:** the "finitely many gcd-values → pigeonhole" + "a prime dividing infinitely many terms" dichotomy is the *exact* move for proving `P` finite / identifying persistent primes (route 1/3 sub-lemma). **Where it breaks:** aimo-0421 is existence of one triple; we need the *entire* minimal-support family to stabilize.

4. **`aimo-0628` (USA TSTST 2015) — sparse/non-sparse residue dichotomy.** **Crux move:** "Partition by residue mod a forbidden modulus; flag classes with only finitely many members (sparse); finitely many sparse classes." **Adapt:** a prime `q∉P` is "sparse" (appears in only finitely many minimal supports) — evict it. Supports the "large primes drop out" sub-lemma.

5. **`aimo-0648` (USA TSTST 2011) — bounded-interval → eventual-constant.** Floor recurrence, eventually constant. **Crux:** bounded-in-interval ⇒ eventually periodic (finite state); then "max propagates backward via Bézout (gcd of lags =1)" forces constancy. **Adapt:** the "bounded ⟹ eventually periodic via finite state" is the same engine; the Bézout-back-propagation has no direct analogue here (our conclusion is periodic-differences, not constant).

Weaker / surface-only analogues (do not model on these): `aimo-0503` (IMO-SL 2008, consecutive-gcd-greater-than-previous — proves `a_n≥2^n`, a *growth lower bound*, opposite direction; not a periodicity result), EKG / Yellowstone / Recamán (NOT in corpus; the difference is decisive: EKG uses "unused + shares with ONLY the previous term", here it is "greater than previous + shares with ALL previous" — monotone, so the EKG "visits every number" machinery is irrelevant).

### Cheap-kill candidates (structural pruning before heavy work)

- **Minimal-support reduction:** "hit every support ⟺ hit every minimal support" is a one-line pruning that collapses the infinite constraint family to a finite antichain — do this first.
- **Residue-mod-L reduction:** admissibility depends only on residue mod `L` (CRT over squarefree `L`) — collapses unbounded greedy to finite-state.
- **Bertrand eviction of large primes:** a prime `q` exceeds the smallest composite transversal ⇒ never persistent (one Bertrand call). Likely gives `P ⊆ primes ≤ C·a_1` cheaply.

### Knowledge-base entries to use (named)

`Modular arithmetic, CRT`; `Order of an element, Fermat/Euler` (eventual periodicity mod m); `Bertrand's postulate`; `Pigeonhole / extremal`; `Invariants & monovariants`; `Comparability / divisibility graphs`; `Divisor analysis` (gcd structure). (Dickson's lemma is *not* in KB as a named entry — if route 3 is taken, the outliner must state/prove it; it is standard and short.)

### Prior progress

None — population empty (round 1). This report is the first reconnaissance; the transversal conjecture above is the furthest correct (empirical) progress and the natural skeleton for the outliner's first approaches.

### Dead ends (do not retry)

(none yet — round 1.) But warn the outliner against the **single-gap trap**: routes 1–3 above all pass through the *same* shared sub-lemma — "P is finite and M stabilizes" — so if the outliner builds several approaches that all route through that lemma, they share one wall. The 4th (Bertrand-eviction) framing and a genuinely different *direct* construction (exhibit T,L explicitly from M without going through finite-state periodicity) should be kept as a rival to avoid collapse.

### Small-case / intuition notes (all CONJECTURE, labeled)

- `L` is always **squarefree** (= product of persistent primes) — verified 8/8. Conjectural.
- The relation `a_{n+T}=a_n+L` holds **from n=1** (transient 0) in every stabilized case — verified 8/8 including the hard `a1=429` (T=908, L=4290). Conjectural that transient is always 0 once M is stable; the problem statement's "for every positive n" supports this, but a proof of eventual-periodicity + a separate "transient absorbed" argument may be the safer target than proving periodicity-from-the-start outright.
- `T = |R|` = number of transversal residues of `M` mod `L` — verified 8/8. Striking: the period equals the *count* of admissible residue classes. Conjectural.
- `P` (persistent primes) is generally **larger** than `primes(a_1)` (e.g. `a_1=35=5·7` → `P={2,3,5,7}`, gaining 2,3) but never includes primes that only appear in non-minimal supports. The primes entering via the first few greedy steps (esp. 2, via the first even term) are usually persistent.
- For single-prime or "2 enters and kills everything" starts (`a_1∈{6,7,8,10,12,21,30,42,70,210,2310,…}`), `T=1` and the sequence becomes a pure AP (`a_n=a_1+L(n−1)`-ish) — the minimal-support family collapses to a single singleton `{p}`, `L=p`, `R={0}`. These are the degenerate (easy) regime; the proof must not assume them.
