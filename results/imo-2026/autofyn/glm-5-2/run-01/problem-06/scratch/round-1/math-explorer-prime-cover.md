# IMO 2026 P6 — terrain report (prime-cover / factor-set-state lens)

## What the problem is

`a_{n+1}` = smallest integer `> a_n` with `gcd(a_{n+1}, a_i)>1` for **every** `i≤n`. Prove `∃ T,L>0` with `a_{n+T}=a_n+L` for all `n` (eventually "arithmetic up to a period": residues mod `L` cycle with period `T`). `proof_only`, no final answer. Domain `number_theory`, difficulty 9.

The condition is governed by **prime-factor sets**. Write `P(m)` = set of prime divisors of `m`. The rule is: `P(a_{n+1})` must be a **transversal** (hitting set) of the family `{P(a_1),…,P(a_n)}` — it must intersect each `P(a_i)`. Greedy picks the smallest `>a_n` integer whose prime-factor set is such a transversal.

## Distinct openings surfaced (each a whole-claim attack the outliner could build)

1. **Structural-prime stabilization → periodic greedy on residues.** Define a prime `p` to be *structural* (essential) once it is ever the *sole* satisfier of some past constraint at a greedy step (i.e. the greedy picked a number divisible by `p` because no combination of smaller structural primes hit some `a_j`). Conjecture: the structural set `S` is **finite and eventually constant**; after that point every `a_n` is divisible by some `p∈S`, every further prime factor is a *free rider* (a large prime `q` dividing a term that is *also* divisible by a structural prime, hence imposing no new constraint), and the greedy reduces to a deterministic walk on `Z/LZ`, `L=∏_{p∈S} p`. Finiteness of `S` is the load-bearing step; periodicity of the residue walk is then a finite-state argument.

2. **Covering-density / smooth-number bound (finiteness of `S` via density).** Each structural prime `p` "covers" density `1/p` of integers. As `S` grows, the set of `S`-smooth numbers divisible by enough `S`-primes to be a valid transversal becomes arbitrarily dense, so beyond some finite `S` the greedy always finds a valid candidate smaller than any number needing a new prime. Formalize with a counting bound (Mertens / `Σ 1/p`) to force `S` to stop growing. This is the natural partner to opening 1 but supplies the *reason* `S` stabilizes rather than assuming it.

3. **Invariant-ladder / monovariant on the lcm.** Track `M_n = lcm` of "essential" prime sets, or the quantity `L_n =` (product of primes that have appeared as sole-satisfiers). Show `L_n` is non-decreasing and **bounded above** (by something derived from `a_1`'s factor structure, or by a universal covering argument), hence eventually constant `=L`. Once `L_n=L` is constant, the constraint family modulo `L` has only finitely many possible "types" (subsets of `S`), so the sequence of types is eventually periodic by pigeonhole; lift types back to residues. This reframes stabilization as a **bounded-monovariant** argument.

(These three are genuinely far apart: #1 is "finite state machine on prime sets", #2 is "analytic density forces termination", #3 is "algebraic monovariant + pigeonhole". A proof-outliner could field them as rival slugs.)

## Candidate technique(s) (pointers, not a plan)

- **Covering systems / disjoint-cover lower bound** (Mirsky–Newman / aimo-0341 grid-by-CRT encoding): the period block is literally a finite set of residues covered by the structural primes. The bound `s ≥ 1 + Σ(n_i−1)` and the CRT-grid encoding of "every cell covered by a prime" are direct analogs.
- **Pigeonhole on a finite type set** (KB "Pigeonhole / extremal principle"; KB "Order of an element / eventual periodicity of products mod m"): once the relevant modulus is fixed, finite residue state ⇒ eventual periodicity.
- **Invariants & monovariants** (KB entry): a non-decreasing bounded quantity (lcm of essential primes, or "rank" of the constraint family) that must stabilize.
- **CRT / squarefree-modulus reduction** (KB "Modular arithmetic, CRT"): `L` is squarefree (conjectured), so residues mod `L` split cleanly across the structural primes.

## Cheap-kill candidates (structural pruning to try before heavy machinery)

- **Free-rider lemma (cheap, high value):** If a term `a_i` is divisible by a structural prime `p∈S`, then any prime `q|a_i` with `q∉S` imposes a constraint "divisible by `p` or `q`" that is *strictly weaker* than "divisible by `p`"; hence `q` never forces a future choice. So free riders are invisible to the greedy once `S` is fixed — prove this first, it makes the reduction to `S`-world rigorous. (Conjecture, supported by data: e.g. `a_1=15` tail contains terms divisible by 181, 173, … yet the period is unchanged.)
- **Squarefree-`L` check:** every computed `L` is squarefree `=∏ S`. Try to prove no prime power ever enters `L` (a prime `p` is either structural—contributing one factor—or a free rider—contributing none). This would pin `L` structurally.
- **Collapse detection:** if a single prime `p | a_1` has the property that the greedy can always reach a multiple of `p` before being forced to use another prime, the sequence collapses to `a_n ≡ 0 mod p`, `T=1, L=p` (data: `a_1∈{6,21,30,42,210,2310}` all collapse). Characterizing collapse vs. non-collapse cheaply bounds the case split.

## Knowledge-base entries to use

- "Modular arithmetic, CRT" (squarefree `L` splits across structural primes).
- "Order of an element, Fermat/Euler: eventual periodicity of products of a sequence mod m" — the eventual-periodic-mod-`m` framing.
- "Invariants & monovariants" (for opening #3).
- "Pigeonhole / extremal principle" (finite type set ⇒ periodicity; also the "take maximal structural set" extremal move).
- "Divisor analysis: `d(n)`, gcd structure, consecutive-integer coprimality `gcd(k,k+1)=1`" — useful for bounding skipped gaps between landings.
- (Not in KB but needed:) a Mertens-type / `Σ_{p≤x} 1/p` density estimate for opening #2; the outliner may have to prove a weak density lemma from scratch.

## Analogous past problems (cruxes)

- **aimo-0341** (combinatorics, "modular-arithmetic-and-CRT" + "induction-and-construction" cruxes): covering of `Z` by arithmetic progressions; encodes residues mod `n=∏ p_i^{α_i}` as a CRT grid, turns each AP into an axis-fixing subgrid, and proves the covering bound `s ≥ 1+Σ(n_i−1)` via a Hall/maximal-deficient-set argument. *Analogous because* our period block is exactly a finite covering of one period's residues by the structural primes, and the "prime `p` covers ≤ ⌈N/p⌉ cells" counting is the same shape as the free-rider/density argument. Crux move: **grid-by-CRT + Hall deficiency**.
- **aimo-0447** (number_theory, "divisibility-and-gcd" + "size-bounding-and-descent"): "`gcd(a+i,b+j)>1` for all `i,j` in an `N×N` grid ⟹ min(a,b) ≥ c·n²." Encodes each cell with a prime dividing the gcd, then bounds cells-per-prime by `⌈N/p⌉²` and sums `Σ1/p²<½` to force a large prime or large `a,b`. *Analogous because* it is the canonical "every pair must share a prime ⟹ only finitely many primes do real work, the rest are density-bounded" argument — exactly the engine for finiteness of `S`. Crux move: **prime-grid covering + `Σ1/p²` density bound**.
- **aimo-0680** (number_theory, "sequences-and-recurrences" / "orders-and-primitive-roots"): an iterate `f^y(a_x)=a_x+y·T_x` is shown to extend from an infinite subset to all indices by a divisibility + bounded-difference gap argument. *Thematic analog* (an iterate/sequence that becomes exactly arithmetic), but structurally remote — listed for the "eventual arithmetic" target shape, not the technique.

No crux in the corpus is a direct greedy-gcd-sequence match; aimo-0341 and aimo-0447 are the two to adapt.

## Prior progress

None — round 1, workspace empty (`current.md` status `unsolved`, no approaches, no lemmas).

## Dead ends (do not retry)

None yet (first round).

## Small-case / intuition notes (all CONJECTURE, labeled)

Computed (python, exact greedy up to `N=1500–4000`):

| `a_1` | `T` | `L` | structural `S` = primes(`L`) | `primes(a_1)` | notes |
|---|---|---|---|---|---|
| 6,10,30,42,66,70,210,2310 | 1 | 2 | {2} | various | collapse to mult. of 2 |
| 21 | 1 | 3 | {3} | {3,7} | collapse to mult. of 3 (7 drops out) |
| 231 | 1 | 3 | {3} | {3,7,11} | collapse to mult. of 3 |
| 15 | 8 | 30 | {2,3,5} | {3,5} | block [3,2,4,6,6,4,2,3]; 2 promoted |
| 45 | 8 | 30 | {2,3,5} | {3,5} | same `T,L` as 15 |
| 77 | 18 | 154 | {2,7,11} | {7,11} | block has 2 promoted; 3,5 appear as free riders but stay non-structural |
| 35 | 34 | 210 | {2,3,5,7} | {5,7} | 2 AND 3 promoted |
| 105 | 58 | 210 | {2,3,5,7} | {3,5,7} | 2 promoted; same `S,L` as 35 |
| 1001=7·11·13 | 282 | 2002 | {2,7,11,13} | {7,11,13} | 2 promoted |
| 143=11·13 | 64 | 858 | {2,3,11,13} | {11,13} | 2,3 promoted |
| 323=17·19 | 94 | 1938 | {2,3,17,19} | {17,19} | 2,3 promoted |
| 221=13·17 | 334 | 6630 | {2,3,5,13,17} | {13,17} | 2,3,5 promoted |
| 385=5·7·11 | no period by N=4000 | — | — | {5,7,11} | settles very slowly / huge period |
| 1155, 5005, 15015 | no period by N=3000–4000 | — | — | — | large; theorem says they settle eventually |

Empirical conjectures (NOT proved):
- **C1:** `L` is always squarefree and equals `∏_{p∈S} p` (the structural primes). Verified in every settled case.
- **C2:** `S` is finite and eventually constant; `S ⊆ {2,3,5,…}` (small primes) `∪ primes(a_1)`. Promoted primes are always *small* (2, then 3, then 5) — because small primes have the densest multiples, so the greedy (smallest-first) lands on them first and they get activated. No large prime was ever promoted in any run.
- **C3:** `T = |R|` where `R ⊆ {0,…,L−1}` is the set of residues the greedy visits mod `L`; the period block is the cyclic gap sequence of `R`. For `|S|=3` cases tested (15,45,77), `R = {r : ≥2 structural primes divide r}` (inclusion-exclusion matches exactly: e.g. `a_1=15` gives 8 = 5+3+2−2·1). **This formula FAILS for `|S|≥4`** (`a_1=35`: formula predicts 70, actual 34). So the residue characterization is subtler than "≥2 structural primes" — the binding structure has a *hierarchy* (e.g. for `a_1=35` one prime, 5, is a "backbone": pair-residues involving 5 are in `R`, pairs among `{2,3,7}` are not). Mapping the true rule for `R` is an open sub-question.
- **C4:** free-rider primes appear infinitely often in the tail (e.g. `a_1=15` tail has terms divisible by 181, 173, …) but never alter `T` or `L` — consistent with the free-rider lemma.
- **C5:** when `a_1` has a prime `p` whose multiples are "dense enough" that the greedy never needs another prime, the sequence collapses to `T=1, L=p`. Collapse is common; non-collapse requires at least two seed primes that "compete".

### Hard steps / gaps a proof via this route must close (as questions)

1. **Why is `S` finite?** Give a rigorous bound on the number (and size) of structural primes. The density argument (opening #2) is the natural engine but must be made constructive: show that once `S` contains enough small primes, the greedy always finds an `S`-transversal below the next "would-be new-prime" candidate. *This is the central gap.*
2. **Why does `S` stabilize (stop growing), not just be bounded?** Bounded + monotone (each promotion adds a prime) ⟹ stabilizes — so the real task is the monotone-bounded pairing: prove promotions can only *add* primes (never remove — true, since a structural prime stays structural) and that the total is bounded (gap 1).
3. **Free-rider lemma:** prove rigorously that a prime `q∉S` dividing a term that also has a structural factor never becomes the sole satisfier of a future constraint. (Looks direct: the constraint it contributes is weaker than the structural prime riding with it — but needs the inductive hypothesis that *all* its co-riders are structural.)
4. **Finite-state ⇒ periodicity:** once `S` is fixed, prove the greedy on residues mod `L=∏S` is eventually periodic. Finiteness of residue-state alone gives *eventual recurrence*; need that the recurrence is a clean *cycle* (deterministic greedy ⇒ the state graph is a functional digraph ⇒ tail + cycle; need tail length finite, which follows from finite state). State = the "active constraint family" reduced mod `L`; must show this family itself stabilizes (not just `S`).
5. **Characterize `R` (optional for the proof, needed for explicit `T`):** the theorem only asks existence of `T,L`, so a full characterization of `R` is *not required*. The route can stop at "some period exists" without naming `R`. Outliner may skip C3 entirely.
6. **`L` squarefree:** prove no prime power enters `L` (i.e. `v_p(L)≤1` for all `p`). Seems forced by "structural prime contributes one covering role", but needs proof.

## Bottom line for the outliner

The prime-cover lens predicts: **`L` = product of a finite stabilized structural-prime set `S`; `T` = size of the greedy's residue cycle mod `L`; periodicity follows once `S` stabilizes.** The single load-bearing, genuinely hard step is **finiteness/stabilization of `S`** (gap 1+2); the rest is finite-state machinery + a clean free-rider lemma. Three rival framings of *why `S` stabilizes* (state-machine, density, monovariant) are far enough apart to field as separate slugs. Do not waste rounds trying to characterize `R`/`T` explicitly — the theorem only needs existence.
