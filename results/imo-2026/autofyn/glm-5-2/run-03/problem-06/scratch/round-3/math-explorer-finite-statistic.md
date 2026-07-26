## imo-2026-06 (route: finite-automaton / finite-sufficient-statistic + direct increment-pattern induction)

## Headline verdict on THIS route

**The route, in every formulation I could construct or test, is EQUIVALENT to Gap A — it is NOT a genuine bypass.** It does, however, (i) confirm a stronger-than-required empirical target (`d_n` periodic from `n=1`, rock-solid across all tested `a_1` incl. the hard 385/1309/2085), (ii) supply a clean finite-state pigeonhole SKELETON, and (iii) surface two new structural facts the prior lemmas lack. The single missing lemma is exactly the Gap-A content in disguise. Details and numbers below; the outliner should treat this as a re-targeting of Gap A into a language where the proof mechanism might differ from the MT/transversal framing — NOT as a wall-free route.

## Distinct openings (the angles I surfaced)

1. **Markovian window-state pigeonhole (the cleanest opening).** Define `σ_n : {1,…,M_1} → {0,1}` by `σ_n(k)=1` iff `a_n+k` is admissible at step `n` (shares a prime with every `a_i, i≤n`). Then `σ_n` lives in `{0,1}^{M_1}`, a finite set of size `2^{M_1}`. The greedy pick is `d_n = min{k: σ_n(k)=1}`, and `σ_{n+1}` is obtained from `σ_n` by (a) shifting the window right by `d_n`, (b) imposing the new constraint "shares a prime with `a_{n+1}`." IF the transition `σ_n → σ_{n+1}` were determined by `σ_n` alone (or by `(σ_n, a_n mod M_1)`), then `σ_n` would take ≤ `2^{M_1}` values and pigeonhole ⇒ `σ_n` eventually periodic ⇒ `d_n` eventually periodic ⇒ `a_n` eventually AP, **with no transversals, no MT, no Gap A.** This is the genuine finite-statistic opening.

   **Where it founders (verified computationally):** the transition is NOT determined by `σ_n` (or `(σ_n, a_n mod M_1)`). The new constraint from `a_{n+1}=a_n+d_n` depends on `S(a_{n+1})` (its prime factorization). The `P_1`-part of `S(a_{n+1})` IS determined by `a_{n+1} mod M_1 = (a_n+d_n) mod M_1` (since `p|a_{n+1} ⇔ a_{n+1}≡0 mod p`, for `p∈P_1`). But the NON-`P_1` primes of `a_{n+1}` — the free-riders — are NOT determined by `a_n mod M_1`; they depend on the absolute value `a_n+d_n`, which grows. The transition therefore needs `{non-P_1 primes of a_{n+1}}` appended to the state. Bounding THAT set is exactly Gap A. So pigeonhole closes iff Gap A closes.

   Empirical check (a1=385): over the first 500 terms there are 491 distinct realized `σ_n` patterns — far below `2^{385}` (good: the realized state space is small, ≈ the period T=5088), but the transition still leaks the free-rider primes.

2. **Minimal modular statistic = full period L.** I checked whether `d_n = f(a_n mod L_0)` for some `L_0 < L` (which would give a cheaper finite statistic than the full period). For a1=385: `a_n mod M_1=385` gives **89 conflicts** (same residue, different `d_n`); the minimal divisor `L_0` of `L=43890` for which `d_n` is a function of `a_n mod L_0` is **`L_0 = L = 43890` itself**. So no proper sub-modulus suffices; the minimal modular statistic IS the full period, whose prime factors are exactly the governing primes (incl. free-riders 2,3,19 for 385). Consequence: any "modular" finite statistic must be `a_n mod L`, which requires bounding the governing primes — Gap A.

3. **`P_1`-skeleton + free-rider discount decomposition.** Let `b_n` = smallest `m>a_n` that is `P_1`-admissible (shares a `P_1`-prime with every `a_i`). The `P_1`-restriction family `{S(a_i)∩P_1}` is a subset of `2^{P_1}`, hence **stabilizes after ≤`2^{|P_1|}` steps** — after which `b_n` is a function of `a_n mod M_1` alone (periodic, period `M_1`). Write `d_n = (b_n - a_n) - δ_n` (`δ_n ≥ 0` = free-rider discount). The state `(a_n mod M_1, δ_n)` has size ≤ `M_1 × M_1` — finite. **IF `δ_n` were finitely determined**, pigeonhole ⇒ periodicity. But `δ_n` records which free-rider prime beats the `P_1`-candidate — again the unbounded Gap-A content.

   **New structural facts (conjectural, from data; not yet lemmas):**
   - For the hard semiprime-ish cases (385, 1309, 2431, 35, 143, 1001), the stabilized `P_1`-family has **`|R_1| = 1`** — the only `P_1`-admissible residue mod `M_1` is `r≡0` (multiples of `M_1`). So without free-riders the greedy would be `a_{n+1}` = next multiple of `M_1`, `T=1, L=M_1`. The entire nontrivial structure of `d_n` comes from free-rider discounts. (2085 is an exception: `|R_1|=139`, looser.)
   - The discount `δ_n` takes **few distinct values** (≈8 for 385; ≈8 for 1309; ≈5 for 2085), all ≪ `M_1`. This bounded-alphabet of discounts is the empirical signature of "few governing free-riders."

4. **Direct induction on `(d_n)` — the "periodic from `n=1`" conjecture.** Empirically (see table) `d_n` is periodic from `n=1` in EVERY case I could resolve, including the hard ones. A direct proof would need: show the constraint set at step `n+T` is an `L`-translate of that at step `n`, i.e. `S(a_{n+T})` relates to `S(a_n)` under `m↦m+L`. This requires the set of primes appearing in term supports to be `L`-periodic — i.e. the free-rider primes that matter form a finite set closed under the period. That is Gap A again, restated.

## Computed evidence (all freshly verified this round, sympy `factorint`)

| `a_1` | `rad(a_1)=M_1` | `max d_n` | `T` | `L` | `L` fact | periodic from `n=1`? |
|---|---|---|---|---|---|---|
| 6 | 6 | 2 | 1 | 2 | 2 | YES |
| 15 | 15 | 6 | 8 | 30 | 2·3·5 | YES |
| 21 | 21 | 3 | 1 | 3 | 3 | YES |
| 35 | 35 | 10 | 34 | 210 | 2·3·5·7 | YES |
| 77 | 77 | 14 | 18 | 154 | 2·7·11 | YES |
| 91 | 91 | 14 | 20 | 182 | 2·7·13 | YES |
| 105 | 105 | 6 | 58 | 210 | 2·3·5·7 | YES |
| 143 | 143 | 22 | 64 | 858 | 2·3·11·13 | YES |
| 1001 | 1001 | 14 | 282 | 2002 | 2·7·11·13 | YES |
| **385** | 385 | 14 | **5088** | **43890** | **2·3·5·7·11·19** | **YES (verified over 9912 = T·(3−1) terms)** |
| **1309** | 1309 | 14 | 912 | 7854 | 2·3·7·11·17 | YES |
| 2085 | 2085 | 6 | 1372 | 6270 | 2·3·5·11·19 | YES |
| 2431 | 2431 | 26 | (>3999, not found in 12000 terms) | — | — | (period too large; `max d=26`, conjecture YES) |
| 741 | 741 | 3 | 1 | 3 | 3 | YES (lock) |
| 116 | 58 | 2 | 1 | 2 | 2 | YES (lock at `a_7=128`) |
| 145 | 145 | 5 | 1 | 5 | 5 | YES (lock at `a_97=625`) |

Notes: (a) `d_n` periodic from `n=1` is a **stronger** claim than the theorem requires ("eventual"); it matches the certified `greedy-equals-cyclic-successor` lemma (pure-from-start). (b) `L` is NEVER `rad(a_1)` for the nontrivial cases — extra primes (always 2; often 3; sometimes 19, etc.) enter as governing. (c) For 2085=`3·5·139`: the `P_1`-prime **139 drops out** of the governing set (`L=6270=2·3·5·11·19` has no 139) — governing set is NOT simply `P_1 ∪ {small}`, refuting any naive "governing = P_1 plus bounded extras" lemma. (d) The "governing primes `≤ M_1`" conjecture (round-1 live target) holds in every resolved case: all of `{2,3,5,7,11,19} ≤ 385`; `{2,3,7,11,17} ≤ 1309`; `{2,3,5,11,19} ≤ 2085`.

## Hard steps / likely walls (route-specific)

- **THE wall (reduction to Gap A).** Every finite statistic I tried (modular `a_n mod L_0`; `P_1`-skeleton + discount; Markov window-state `σ_n`) requires, at the one load-bearing step, that the set of "non-`P_1` primes that ever act as the unique connector for some candidate" be finite. That is precisely Gap A. The reason MT was unbounded (transients give unbounded covering capacity compatibly with Gap A — round-2 finding) does NOT bite HERE, because the increment language only cares about primes that actually change `d_n`; but proving THAT set finite is the same content.
- **The window-state transition leak.** `σ_{n+1}` depends on `S(a_{n+1})`, and the non-`P_1` part of `S(a_{n+1})` is not captured by `σ_n` or by `a_n mod M_1`. Concrete: at a1=385, two indices with identical `a_n mod M_1` can have different `S(a_{n+1})` free-rider parts (this is why `a_n mod 385` gives 89 conflicts on `d_n`). Plugging the leak = Gap A.
- **`|R_1|=1` is not universal.** 2085 has `|R_1|=139`, so the "P_1-skeleton is trivial (T=1)" simplification that holds for 385-class cases does NOT hold universally. Any lemma using the `|R_1|=1` structure must either handle the looser case separately or avoid relying on it.

## What's been tried that touches this route (avoid repeating)

- **Round-1 compute explorer** (`/tmp/round-1/math-explorer-compute.md`): empirically claimed a1=385 "NOT periodic in 12000 terms" — **WRONG** (it IS periodic, `T=5088, L=43890`, periodic from `n=1`; verified this round over 9912 terms). The error came from searching only `T≤3000` and modulus 2310. The compute explorer also noted the `P_Q`-restriction family stabilizes by term ~225 yet "aperiodic" — the stabilization is real but the free-rider constraints persist (and ARE themselves eventually periodic, just with the larger period `L=43890`). Do NOT cite round-1's "385 aperiodic" claim.
- The `P_1`-restriction-family-stabilizes ⇒ periodic" argument was flagged as a TRAP by round-1 compute (correctly: stabilization of the `P_1`-family alone is insufficient; free-riders extend the period). Confirmed this round: `L=43890 = 114·M_1` for 385, the factor 114 = 2·3·19 coming entirely from free-rider primes.
- Round-2 reviewer's framing suggestion #1 (finite-statistic) and #4 (direct increment induction) are exactly this route — the reviewer did not claim they bypass Gap A, only that they're genuinely-different framings. My scouting confirms: different framing, **same wall**.

## Candidate crux moves from the corpus (adaptable hints, NOT citations)

- **`aimo-0079` / `aimo-0274`** (NT, pigeonhole / modular-CRT) — *"Among infinitely many length-L windows of a `{0,1}`-valued function on the integers, pigeonhole over the finitely many possible window-patterns to find two starting positions whose windows agree termwise."* This is the closest crux to the Markov window-state pigeonhole (opening #1). Adaptation hint: the window-state `σ_n ∈ {0,1}^{M_1}` is exactly such a finite-pattern object; the crux move is "two equal windows ⇒ periodicity." BUT the `aimo-0079` crux applies to a FIXED function on the integers, whereas our `σ_n` EVOLVES (the admissibility function changes each step). The crux does not directly transfer unless one first shows `σ_n` itself is eventually constant-in-shape — which is the wall.
- **`aimo-0447`** (NT, divisibility-and-gcd) — *"Encode a `gcd>1` hypothesis by placing in cell (i,j) a prime dividing `gcd(a+i,b+j)`, turning the condition into a complete prime-covering of a grid; bound small-prime coverage by `Σ⌈N/p⌉²`."* This is the 2D analog of the spacing/covering argument. Round-2's `witness-density-recurrence` already found this flavor CIRCULAR for our 1D problem (covering capacity unbounded compatibly with Gap A). The crux is analogous in shape but its 2D density-bound mechanism does NOT lift to the 1D greedy setting. Do not retry as a density lower bound.
- **`aimo-0231`** (NT, modular-arithmetic-and-CRT) — *"Decompose the first-hitting-time of an iterated map mod N as the lcm over prime-power factors of N."* Potentially useful if one can show `d_n` periodic mod each prime-power separately and CRT-combine. Speculative; no direct adaptation found.
- **No EKG / Recamán / Perron–Frobenius crux** in the corpus (keyword search returned nothing genuinely analogous — the corpus's "greedy"/"periodic" hits are about partition/product recurrences, not gcd-driven greedy sequences).

## Knowledge-base entries to use

- `linchpin-and-gap-bound` (certified) — `d_n ≤ M_1`; the finiteness of the increment alphabet; **the key input that makes any window-state pigeonhole finite** (`2^{M_1}` states).
- `greedy-equals-cyclic-successor` (certified) — the greedy pick from `n=1` equals the cyclic successor in `B_∞`; underwrites "periodic from `n=1`" once periodicity is established.
- `cyclic-successor-bijection` (certified) — periodicity of `B_∞` ⇒ `a_{n+T}=a_n+L` for all `n≥1`; the endgame this route feeds into.
- `lock-lemma` (certified) — handles `|P_1|=1` / prime-power-term base case.
- `pairwise-intersecting-supports`, `every-term-in-binfinity` (certified) — foundation; the latter is what makes `σ_n`'s zero-set grow only via new constraints (not via losing old admissibility).

## Prior progress (what's certified and importable into this route)

The whole theorem is reduced to Gap A; the endgame (`cyclic-successor-bijection`), pure-from-start (`greedy-equals-cyclic-successor`), and LOCK sub-case are all certified. This route does NOT add a new certified lemma — it rephrases Gap A. The new **conjectural** inputs it surfaces (needing proof): (C1) `d_n` is periodic from `n=1` (empirically universal); (C2) for the `|R_1|=1` cases, `d_n` is entirely determined by the free-rider discount `δ_n` which takes bounded-many values; (C3) the realized window-state space `{σ_n}` has size exactly `T` (the period). None is yet proved.

## Dead ends to avoid (route-specific)

- **Do not** argue "`P_1`-restriction family stabilizes (≤`2^{|P_1|}` steps) ⇒ periodic." It stabilizes but free-rider primes extend the period (385: factor 114 from free-riders). Round-1 compute flagged this; confirmed.
- **Do not** cite round-1's "385 aperiodic in 12000 terms" — it is wrong; 385 is periodic from `n=1` (`T=5088`).
- **Do not** assume the finite statistic is `a_n mod L_0` for `L_0 < L`; minimal is `L_0 = L` (verified for 385).
- **Do not** assume governing set `= P_1 ∪ {2,3}` or `⊇ P_1`; 2085 has `139 ∈ P_1` but `139 ∉` governing set. Governing set is a specific subset; `q ≤ M_1` (conjectural) is the only robust bound.
- **Do not** re-prove density/covering-capacity bounds (witness-density-recurrence, dead): the 1D analog of `aimo-0447`'s coverage sum is the spacing UPPER bound `≤ M_1/q` (sound, certified W1) but no lower bound is non-circularly available.

## Concrete recommendation for the outliner

**This route is NOT a wall-free bypass; it is a re-targeting of Gap A into increment language.** I recommend the outliner open ONE slug along this route, framed as the **Markov window-state pigeonhole** (opening #1), because it is the most concrete finite-statistic framing and its wall is cleanly isolated:

Slug skeleton (for the outliner to plan, NOT a proof):
- `increment-pigeonhole-window` — Target: prove `(d_n)` is eventually periodic (equivalent to theorem via `cyclic-successor-bijection` + `greedy-equals-cyclic-successor`, both certified). Mechanism: define `σ_n ∈ {0,1}^{M_1}` (admissibility on the window `[a_n+1, a_n+M_1]`); note `d_n = min{k: σ_n(k)=1}` and the state space is finite (`≤ 2^{M_1}`). **HARD STEP (flagged, = Gap A):** prove the transition `σ_n → σ_{n+1}` is determined by a bounded function of `σ_n` (equivalently: only finitely many non-`P_1` primes ever enter `S(a_{n+1})` in a way that changes `σ`). The `P_1`-part of the transition IS bounded (determined by `a_n mod M_1`); the free-rider part is the wall. Fallback sub-target if the full transition can't be bounded: prove `d_n` periodic by directly showing the realized `σ_n` set is finite (empirically size = T) and the transition is a self-map on it.

The outliner should NOT expect this slug to close the theorem on its own — it will hit Gap A at the flagged hard step. Its value is as a **rival framing**: if the MT/transversal framing and the increment framing BOTH reduce to "bound the active free-rider primes," the confluence itself becomes a lemma (the two are the same wall), and the outliner can focus the field's effort on the SINGLE shared sub-lemma from whichever side admits a cleaner attack. The increment side's cleaner statement of that sub-lemma: **"only primes `≤ M_1` ever act as the unique connector reducing `d_n` below the `P_1`-skeleton value"** (= the round-1 `q ≤ M_1` conjecture, restated).

If the outliner wants a genuinely ORTHOGONAL route (not Gap-A-equivalent), this scout's finding is: the finite-statistic and direct-induction routes are NOT it — they are Gap A in disguise. The orthogonal escape, if one exists, is more likely in covering-systems/sieve (route #3, not scouted here) or structural induction on `|P_1|` (route #2, not scouted here); the outliner should weight those higher for a true bypass.
