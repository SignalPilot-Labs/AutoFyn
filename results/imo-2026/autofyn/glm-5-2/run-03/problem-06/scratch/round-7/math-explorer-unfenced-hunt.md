# imo-2026-06 — unfenced-mechanism hunt (round 7, lens: genuinely-unfenced-mechanism)

**Verifier used:** `/tmp/round-6/mt_greedy.py` (correct) + a naive O(N²) gcd-greedy cross-check on a1=15,385,847 (bit-exact). Sieve up to 5M. NEVER the inverted `/tmp/round-4/fast_greedy.py`. Hand-verified D_0 for a1=15 = {3,5,6,9,10,12,15} matches the script.

## (1) One-line verdict

**NO UNFENCED ROUTE.** All three fresh framings (F1 entropy/potential monovariant, F2 Fine-Wilf two-period forcing, F3 (T,L)-formula + crux-corpus port) collapse to the existing fences or to Gap A itself. The wall holds; CONSOLIDATE.

## (2) F1 — non-MT-frontier potential / entropy monovariant — verdict: NO UNFENCED ROUTE

**Candidate potentials computed (a1 ∈ {15,35,77,91,175,385,847}, full periods, N up to 130k):**
- `|MT(F_n)|`, `mt_primes_count` = |∪MT(F_n)|, `sum_{q∈∪MT} 1/q`, `sum_{T∈MT}|T|`, `max_{T∈MT}|T|`, dropped-prime count.

**Empirical trajectory (the killer — all NON-monotone, overshoot-then-decrease):**
- a1=847 (M1=77): `mt_primes_count` = 2→4→6→7→**8**→6→...→7→7→...→**5** (overshoots final 5, peaks at 8, then decreases). `|MT|` = 2→3→6→8→8→...→5 (same shape).
- a1=77: `mpc` = 2→4→4→**3**→3→...→3 (decreases 4→3 early).
- a1=385: `mpc` = 3→7→6→6→**8**→...→7 (overshoots, 8>final 7).
- `sum 1/q` ALSO non-monotone: a1=77 goes 0.2338→1.0671→1.0671→**0.7338** (decreases); a1=847 1.2171→...→1.0915 (decreases past peak); a1=385 1.3967→1.3197 (decreases).

**"Once dropped, never re-enters" is NOT a theorem (and not even greedy-specific).** I initially conjectured a monotonicity of the dropped-prime set from the MT update rule (new_MT built from old MT transversals). The proof sketch was WRONG: the extension step `T∪{q}` with `q ∈ S_new` reintroduces q even if q was previously dropped (q is added as the NEW hitting element, not carried from old MT). Verified empirically:
- 2000 random hypergraph edge-additions: violations at trial 0 (prime 11 re-enters).
- **Greedy itself violates:** a1=273 (=3·7·13, rad=273) gives **324 re-entry violations** over 4000 steps (dropped primes re-enter repeatedly). The 7 cherry-picked non-LOCK cases (15,35,77,91,175,385,847) happened to show 0 violations, but a1=273 shatters it.
- Dropped-count is also non-monotone in general.

**Eventual stabilization IS Gap A (circular).** Every quantity (`|MT|`, `mpc`, `sum1/q`, `sum|T|`, `max|T|`) does become eventually-constant in the periodic regime (last-20 constant in all 7 cases). BUT the stable value of `mpc` is the number of governing primes — "mpc stabilizes" ≡ "governing primes finite" ≡ Gap A. Proving stabilization IS proving Gap A.

**Strict-bar check:**
- The stable value is NOT f(M1)-bounded (rad-77 pair: `mpc` stabilizes to **3** for a1=77 vs **5** for a1=847, same M1=77). So the rad-77 pigeonhole fence does NOT directly fence this. Good — but the reason it dodges the fence is that the stabilization statement IS Gap A itself (circular), not that it found a new mechanism. The stabilization value is a function of a1 (unbounded in M1), so a pigeonhole-on-stable-value argument would give period ≤ g(a1) — which is just T, no shortcut.
- A genuine GLOBAL monovariant (monotone over the WHOLE run, not just eventually-constant) is absent: every candidate overshoots-then-decreases or has re-entries.
- Collapses to: **f(M1)-bounded/T-unbounded fence** (for the pigeonhole variant) + **Gap A directly** (for the stabilization claim). No genuinely-new monovariant mechanism.

## (3) F2 — Fine-Wilf two-period forcing on d_n — verdict: NO UNFENCED ROUTE

**Fine-Wilf is DISTINCT from Morse-Hedlund in principle** (Morse-Hedlund: p(n)≤n threshold = exactly n=T; Fine-Wilf: two periods p,q with p+q−gcd(p,q)≤n forces gcd(p,q)-period). The hope: the greedy rule forces d_n to carry two distinct sub-T periods over a long stretch (from two different witness-prime sub-cycles), Fine-Wilf then yields a sub-T period, circumventing the Morse-Hedlund threshold.

**Empirical (a1 ∈ {15,35,77,91,175,385,847}, full periods):** d_n has **minimal period EXACTLY T** in all 7 cases. NO proper sub-period exists below T (checked all divisors of T and all p<min(40,T)):

| a1 | M1 | T | L | minimal-period-of-d | proper periods <min(40,T) |
|---|---|---|---|---|---|
| 15 | 15 | 8 | 30 | 8 | none |
| 35 | 35 | 34 | 210 | 34 | none |
| 77 | 77 | 18 | 154 | 18 | none |
| 91 | 91 | 20 | 182 | 20 | none |
| 175 | 35 | 274 | 2730 | 274 | none |
| 385 | 385 | 5088 | 43890 | 5088 | none |
| 847 | 77 | 1744 | 18942 | 1744 | none |

**Why Fine-Wilf cannot fire:** it needs two distinct periods p,q over a stretch of length ≥ p+q−gcd(p,q). If d_n has minimal period T, any period over a long stretch must be a multiple of T (≥ T). Two such periods p,q ≥ T give gcd(p,q) ≥ T — Fine-Wilf just recovers T, no sub-T gain. There are no two witness-prime sub-cycles supplying distinct sub-T periods.

**Strict-bar check:** collapses to the **substitution/Morse-Hedlund fence** (round 4: no sub-T signal supplied by the greedy rule; the threshold is exactly n=T). Fine-Wilf is a different theorem but lands on the same obstruction: the greedy does not produce sub-T period structure. No genuinely-new mechanism.

## (4) F3 — explicit (T,L) formula hunt + crux-corpus non-circular port — verdict: NO UNFENCED ROUTE

**(T,L) formula hunt (computed for p^e, p·q, p^e·q families):**
- **Single-prime radical a1=p^e:** always LOCK — T=1, L=p (e∈{1..5}, p∈{2,3,5,7}). Confirms LOCK lemma.
- **Two-prime radical a1=p·q:** LOCK (T=1,L=2) whenever 2 is a factor (6,10,14,22,26); LOCK (T=1,L=3) for 3·7=21, 3·11=33; NON-LOCK for consecutive odd primes 3·5=15 (T=8,L=30=2·3·5) and 5·7=35 (T=34,L=210=2·3·5·7).
- **Killer family a1=p^e·q (radical pq):** rad-35 pair confirmed — 5·7=35→T=34,L=210 but 5²·7=175→T=274,L=2730 (same M1=35, T jumps 8×); rad-77 pair — 7·11=77→T=18 but 7²·11=539→T=18 (NO jump, identical) and 7·11²=847→T=1744 (97× jump). The exponent-dependence is IRREGULAR: 45=3²·5→T=8 (same as 15), but 175=5²·7→T=274 (vs 35→34). No closed formula T(a1) or L(a1) is apparent — T is not a function of M1 (rad-35 AND rad-77 pairs both exhibit jumps), and is not a clean function of a1's prime factorization either.

**Governing primes (factors of L) all ≤ M1 — re-confirmed (287+ cases, 0 failures):** e.g. a1=847 (M1=77)→L=18942=2·3·7·11·41 (41≤77); a1=175 (M1=35)→L=2730=2·3·5·7·13 (13≤35); a1=2431 (M1=2431)→final_active={2,3,7,11,13,17}; a1=273 (M1=273)→final_active={3}. The q≤M1 conjecture stands, now across 287+ cases incl. 14 new this round.

**Crux-corpus query (number_theory + combinatorics, subtopics NOT in the 16-dead list):** queried zsigmondy-and-primitive-divisors, lifting-the-exponent, orders-and-primitive-roots, cyclotomic, vieta-jumping, processes-and-algorithms, invariants-and-monovariants, coloring-and-parity, telescoping. Findings:
- **Number-theory cruxes (aimo-0079, 0134, 0157, 0220, 0312, 0348, 0418, 0544, 0611, 0628, 0700, 0739, 0781, 0827, 0851, 0957, 0982, 0985, 0987, 1018, etc.)** are all **multiplicative-order / exponential / polynomial-roots** mechanisms. Our greedy is ADDITIVE with LINEAR growth (a_n ≤ a_1 + (n−1)M_1). Zsigmondy (aimo-0611) needs terms exceeding the product of earlier terms (exponential growth) — absent here (linear). Multiplicative-order periodicity (aimo-0982, 0987) needs a^n mod m forward-determinism — fenced by `no-fixed-modulus-forward-determinism` (a_n mod m is NOT forward-deterministic for ANY fixed m, incl. m=a_1^k). None port.
- **Combinatorics periodicity cruxes (aimo-0258, 0367, 0514, 0870, 0892, 0917, 0964)**: aimo-0514 (bijective-state: deterministic successor AND predecessor ⇒ bijection on finite set ⇒ periodic) = the round-5 augmented-bijective-state framing, fenced by T-unbounded-in-M1 (state size ≥ T, unbounded in M1; rad-77 97× jump). aimo-0258/0892 (integer-positional / weighted-length monovariant termination) = classic monovariants, fenced by `aimo-0134-obstruction` (constant gap bound d_n≤M1 gives no shrinking range, no slack). aimo-0964 (cellular-automaton reflecting-boundary periodic orbit) does not port to a greedy with no boundary. aimo-0079 (sliding-product Omega-parity periodicity, defeated by m-vs-2m) needs a balanced-product functional equation absent in our greedy.
- **No genuinely-fresh crux with a non-circular port surfaced.** Every periodicity-forcing crux in the corpus is either (a) multiplicative/exponential (wrong growth regime), (b) bijective-state (fenced round 5), (c) monovariant (fenced aimo-0134), or (d) needs a functional equation our greedy lacks.

**Strict-bar check:** F3 collapses to (a) no-formula ⇒ the formula route would need to prove q≤M1 anyway (= Gap A); (b) crux ports all land in fenced classes (bijective-state / monovariant / no-fixed-modulus). No genuinely-new mechanism.

## (5) Clean structural empirical facts (labeled CONJECTURE, not proved)

- **q≤M1 conjecture re-confirmed (287+ cases, 0 failures):** across 14 new a1 this round (incl. 273, 45, 539, 605, 1183, 2431, plus the rad-35/rad-77 pairs), the final active MT-prime set (= factors of L = governing primes) is ALWAYS ⊆ {primes ≤ M1=rad(a1)}. No prime > M1 ever governs. Still the live empirical target; still no non-circular proof.
- **LOCK regularity:** a1=p^e (single-prime radical) always gives T=1, L=p (matches LOCK lemma). a1=p·q with 2|pq gives T=1, L=2 (2 dominates). Consecutive odd prime pairs (3·5, 5·7) are the smallest NON-LOCK two-prime cases.
- **All candidate MT-potentials are eventually-constant but NON-monotone** (overshoot-then-decrease is the universal shape). The eventual-constancy is real but = Gap A.
- **"Once dropped never re-enters" is FALSE** (a1=273: 324 re-entry violations; random hypergraphs: violations at trial 0). Not a theorem, not greedy-specific. Recorded as a NEGATIVE finding to prevent future rediscovery.

## (6) Dead ends (do not retry — this round)

- **Entropy/potential monovariant on MT statistics** (|MT|, mpc, sum1/q, sum|T|, max|T|, dropped-count): all non-monotone in the real greedy (overshoot-then-decrease; a1=847 mpc 2→8→5). Stabilization-implies-finiteness is circular (= Gap A). Re-entry of dropped primes refutes the one candidate monotonicity (a1=273: 324 violations).
- **Fine-Wilf two-period forcing on d_n:** d_n has minimal period exactly T in all 7 cases (no proper sub-period); Fine-Wilf recovers T only, no sub-T gain. Collapses to substitution/Morse-Hedlund fence.
- **(T,L) closed-formula route:** no formula exists (T irregular in a1's factorization; rad-35 and rad-77 pairs both show T-not-a-function-of-M1). Proving the formula = proving q≤M1 = Gap A.
- **Crux-corpus ports from unmined subtopics (zsigmondy, LTE, orders, cyclotomic, vieta-jumping, processes-algorithms, invariants):** all multiplicative/exponential/bijective-state/monovariant — wrong regime or fenced. No genuinely-fresh crux surfaced.

## (7) Recommendation to the outliner (one line)

**CONSOLIDATE.** No genuinely-unfenced mechanism surfaced this round (F1/F2/F3 all collapse to existing fences or to Gap A directly). The wall resists 16+ mechanisms with 6 structural fences; q≤M1=rad(a1) is almost certainly true (287+ cases, 0 failures) but not provable by any route on the table. The consolidated partial result (conditional proof + LOCK + 30 lemmas + 6 fences + q≤M1 conjecture) remains the run's deliverable; status stays `partial`. Do NOT mount a new attack unless a future explorer clears the strict bar — none did this round.
