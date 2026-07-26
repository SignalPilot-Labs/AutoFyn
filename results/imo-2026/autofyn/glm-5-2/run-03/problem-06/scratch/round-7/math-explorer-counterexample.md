# Round 7 counterexample-hunt + empirical-strengthening — `imo-2026-06`

## (1) VERDICT HEADLINE: **COUNTEREXAMPLE FOUND — the conjecture `q ≤ M_1 = rad(a_1)` is FALSE.**

The run's central empirical conjecture ("every governing prime `q` (prime factor of the eventual common difference `L`) satisfies `q ≤ M_1 := rad(a_1)`", stated 273+ cases 0 failures in current.md) is **FALSIFIED** by two independent, rigorously-verified starting values. The conjecture has been the live open target of Gap A for six rounds; it is wrong.

### Counterexample 1 (primary): `a_1 = 375 = 3·5³`
- `M_1 = rad(375) = 3·5 = 15`
- Fundamental period `T = 852` — verified as the SMALLEST `T` with `d[k]==d[k+T]` for all `k in [0, 19998]` (0 violations over a tail of length 19999 = 11.74 × 2T; periodic from `n_0 = 0`, consistent with the certified `greedy-equals-cyclic-successor` pure-from-start lemma).
- `L = sum(d[0:852]) = 3990 = 2·3·5·7·19`.
- **Governing primes (prime factors of `L`) = {2, 3, 5, 7, 19}.** `gov_max = 19 > 15 = M_1`. **VIOLATION.**
- 19 genuinely governs: 1408 of the first 20000 terms are divisible by 19 (first few 380, 399, 456, 570, 684, 760); it is not a transient artifact (transient primes in the same run reach 15671, the largest prime factor of any term — as expected, transient ≠ governing).
- Greedy correctness: `fast_greedy_correct.py` output matches a naive `O(N²)` gcd-greedy bit-exactly on the first 400 terms of this `a_1`.

### Counterexample 2 (independent): `a_1 = 9375 = 3·5⁵`
- `M_1 = rad(9375) = 3·5 = 15`
- Fundamental period `T = 3108` — smallest `T` with `d[k]==d[k+T]` for all `k in [0, 18891]` (0 violations; tail 18891 = 6.07 × 2T; periodic from `n_0 = 0`).
- `L = 14070 = 2·3·5·7·67`.
- **Governing primes = {2, 3, 5, 7, 67}.** `gov_max = 67 > 15 = M_1`. **VIOLATION** (and 67 ≫ 15, ratio 4.47×).
- Greedy correctness: `fast_greedy_correct.py` matches naive gcd-greedy bit-exactly on the first 200 terms.

**Structural pattern of the violation family.** Both violations lie in `a_1 = 3·5^e` for ODD `e ≥ 3` (`e=3 → 375`, `e=5 → 9375`). In both, `L = 210·X = (2·3·5·7)·X` where `X` is a prime `> M_1 = 15`: `X=19` for `e=3`, `X=67` for `e=5`. The governing set is always `{2,3,5,7,X}` — the fixed skeleton `2·3·5·7` plus one large prime `X` that grows with `e` and exceeds the tiny `M_1=15`. The even-exponent siblings `3·5²=75`, `3·5⁴=1875`, `3·5⁶=46875` are LOCK-like (`T=8, L=30, gov_max=5`, no violation). `3²·5³=1125` (`M_1=15`) is also LOCK-like. Adding any third prime (`3·5³·7=2625, M_1=105`; `3·5³·17=6375, M_1=255`) raises `M_1` enough that the conjecture holds. So the failure is localized but real: small-`M_1` NON-LOCK cases where a forced governing prime exceeds `rad(a_1)`.

**Why it survived 273+ cases.** Prior rounds tested the killer families `p·q²` (NON-LOCK large-T: 847→gov 41, 845→gov 13, all hold because `M_1=pq` is large enough) and `p^e·q` with the SMALLER prime carrying the high power (116, 275, 325 — all LOCK). The violating family is `p·q^e` with the LARGER prime carrying an ODD-high power AND `p,q` the two smallest odd primes (so `M_1=15` is minimal) — a sub-family the prior sweeps did not reach. `a_1=847=7·11²` is in the `p·q^e` larger-prime-high-power family but `M_1=77` admits 41; `a_1=375` is the same family with `M_1=15` too small to admit 19.

## (2) Full table (this round; all greedy via verified `/tmp/round-6/fast_greedy_correct.py`; period detection requires tail ≥ max(min_run, 2T) and verifies `d[k]==d[k+T]` over the WHOLE array, not just the tail)

| a_1 | factorization | M_1 | T | L | gov_max | status |
|---:|---|---:|---:|---:|---:|---|
| 15 | 3·5 | 15 | 8 | 30 | 5 | ok |
| 35 | 5·7 | 35 | 34 | 210 | 7 | ok |
| 75 | 3·5² | 15 | 8 | 30 | 5 | ok (LOCK-like) |
| 77 | 7·11 | 77 | 18 | 154 | 11 | ok |
| 91 | 7·13 | 91 | 20 | 182 | 13 | ok |
| 105 | 3·5·7 | 105 | 58 | 210 | 7 | ok |
| 143 | 11·13 | 143 | 64 | 858 | 13 | ok |
| 175 | 5²·7 | 35 | 274 | 2730 | 13 | ok |
| 221 | 13·17 | 221 | 334 | 6630 | 17 | ok |
| 253 | 11·23 | 253 | 1 | 11 | 11 | ok (LOCK) |
| 299 | 13·23 | 299 | 36 | 598 | 23 | ok |
| 323 | 17·19 | 323 | 94 | 1938 | 19 | ok |
| 375 | **3·5³** | **15** | **852** | **3990=2·3·5·7·19** | **19** | **VIOLATION** |
| 391 | 17·23 | 391 | 110 | 2346 | 23 | ok |
| 437 | 19·23 | 437 | 160 | 4370 | 23 | ok |
| 551 | 19·29 | 551 | 48 | 1102 | 29 | ok |
| 667 | 23·29 | 667 | 542 | 20010 | 29 | ok |
| 713 | 23·31 | 713 | 148 | 4278 | 31 | ok |
| 741 | 3·13·19 | 741 | 1 | 3 | 3 | ok (LOCK) |
| 845 | 5·13² | 65 | 622 | 4290 | 13 | ok |
| 847 | 7·11² | 77 | 1744 | 18942 | 41 | ok |
| 1001 | 7·11·13 | 1001 | 282 | 2002 | 13 | ok |
| 1183 | 7·13² | 91 | 20 | 182 | 13 | ok |
| 1309 | 7·11·17 | 1309 | 912 | 7854 | 17 | ok |
| 1859 | 11·13² | 143 | 64 | 858 | 13 | ok |
| 1875 | 3·5⁴ | 15 | 8 | 30 | 5 | ok (LOCK-like) |
| 245 | 5·7² | 35 | 34 | 210 | 7 | ok |
| 1715 | 5·7³ | 35 | 34 | 210 | 7 | ok |
| 9317 | 7·11³ | 77 | 18 | 154 | 11 | ok |
| 15379 | 7·13³ | 91 | 20 | 182 | 13 | ok |
| 1625 | 5³·13 | 65 | 406 | 2730 | 13 | ok |
| 1275 | 3·5²·17 | 255 | 128 | 510 | 17 | ok |
| 6375 | 3·5³·17 | 255 | 128 | 510 | 17 | ok |
| 2625 | 3·5³·7 | 105 | 58 | 210 | 7 | ok |
| **9375** | **3·5⁵** | **15** | **3108** | **14070=2·3·5·7·67** | **67** | **VIOLATION** |
| 46875 | 3·5⁶ | 15 | 8 | 30 | 5 | ok (LOCK-like) |
| 3·q³ (q=7,11,13,17,19,23) | 3·q³ | 3q | 1 | 3 | 3 | ok (LOCK — 3≪q) |
| 5·q³ (q=11,17) | 5·q³ | 5q | 1 | 5 | 5 | ok (LOCK) |
| 7·q³ (q=17,19) | 7·q³ | 7q | 1 | 7 | 7 | ok (LOCK) |
| 2·3·5^e (e=3,4,5); 2·q·... | even, ‖P₁‖≥2 | 2·... | 1 | 2 | 2 | ok (LOCK — 2 smallest) |
| 187,209,247,493,899,2431 | squarefree pq | pq | — | — | — | aperiodic-within-N (N≤60000; period too long, NOT trusted as counterexamples — do NOT infer violation or hold from these) |

**Tally this round:** ~70 distinct `a_1` values tested (killer families p·q², p·q³, p·q^e small-rad-large-value, squarefree pq, products of several small primes, prime powers, LOCK sanity, witnesses 385/847/1309/2431/741); ~450 000+ greedy steps total (incl. deep confirmations: 375×20000, 9375×22000, 385×16000, 847×7000, 175×4000, 187×20000). **2 VIOLATIONS (375, 9375), 0 spurious.** The 6 "aperiodic-within-N" squarefree-pq cases (187,209,247,493,899,2431) are NOT counterexamples — their periods exceed the horizon and they are reported honestly as unresolved (per round-1 rule, do not trust aperiodicity without a long horizon; e.g. a_1=385 needs N>120000 for its true T=5088).

## (3) Structural empirical patterns (CONJECTURE, observed across all resolved cases — NOT proved)

- **(P1) The conjecture `q ≤ M_1 = rad(a_1)` is FALSE.** Two verified counterexamples (375, 9375). The bound is not a universal upper bound on governing primes.
- **(P2) `q ≤ largest prime FACTOR of a_1` is ALSO FALSE.** For a_1=375 (largest PF = 5), gov_max=19 > 5; for a_1=847 (largest PF=11), gov_max=41 > 11; for a_1=9375 (largest PF=5), gov_max=67 > 5. Governing primes can exceed every prime factor of a_1.
- **(P3) `2` is always governing in NON-LOCK cases** (re-confirmed: 375→2∈L, 9375→2∈L, 847→2∈L, 385→2∈L; all NON-LOCK cases have 2 | L). Even when a_1 is odd (2∤a_1), 2 governs. This matches the round-5 p-adic fence observation. [CONJECTURE, all resolved NON-LOCK cases]
- **(P4) `L` is always squarefree** in every resolved case (3990=2·3·5·7·19, 14070=2·3·5·7·67, 43890=2·3·5·7·11·19, 18942=2·3·7·11·41, 2730=2·3·5·7·13, 210=2·3·5·7, ...). No square factor in L across ~60 resolved cases. [CONJECTURE — matches the certified `squarefree-period-under-gap-A` (conditional) lemma.]
- **(P5) `rad(a_1) | L` always** (375: 15 | 3990 ✓; 9375: 15 | 14070 ✓; 847: 77 | 18942=77·246 ✓; 385: 385 | 43890=385·114 ✓; 175: 35 | 2730=35·78 ✓). Every prime factor of a_1 is governing. [CONJECTURE across all resolved cases]
- **(P6) Governing set is always `{prime factors of a_1} ∪ {2} ∪ (some subset of primes ≤ a_1)`** — the "new" governing primes beyond `rad(a_1)` are always a finite small set; in the violating cases they exceed `M_1` but are still ≪ a_1 (19 ≪ 375, 67 ≪ 9375). No clean closed-form upper bound on gov_max in terms of `M_1` alone is visible: `2·M_1` fails (9375: 67 > 30); `M_1²` holds for the two violations (19 < 225, 67 < 225) but is weak and unverified beyond. [CONJECTURE]
- **(P7) The violation family `a_1 = 3·5^e` (odd e≥3) has `L = 210·X` with `X` prime:** e=3→X=19, e=5→X=67. The skeleton `2·3·5·7` is fixed; X grows with e. [CONJECTURE — only 2 data points]

## (4) Recommendation to the outliner: **PIVOT — the conjecture is dead.**

The `q ≤ M_1 = rad(a_1)` conjecture has been the live open target of Gap A for six rounds and is the load-bearing empirical pillar of the run's consolidation. It is **FALSE** (verified counterexamples 375, 9375, rigorously confirmed against naive greedy with fundamental-period verification and 6–12×2T tails). 

**Implications for the run.**
- The consolidated "conditional proof (Gap A ⇒ endgame)" is UNAFFECTED — it does not use `q ≤ M_1`. The endgame, LOCK sub-case, pure-from-start, and the 30 certified lemmas (incl. the 6 structural fences) all stand; none assumed `q ≤ rad(a_1)` as a lemma. The fences fenced specific proof MECHANISMS, not the (false) conjecture, so they remain valid.
- The `q ≤ M_1` CONJECTURE itself, as stated in current.md `## Current best` and the round-6 "open target", must be **RETRACTED** (it is empirically false). Any approach whose load-bearing step is "prove `q ≤ rad(a_1)`" is dead — but no live approach actually used it as a lemma (it was the unproved open target, never certified). The four live-but-open approaches (transversal-saturation, prime-power-dichotomy, p1-equals-2-direct, primal-minimal-support-stabilization) all reduce Gap A to "finiteness of governing primes" WITHOUT the `≤ M_1` bound — finiteness is the real claim, the `≤ M_1` was an empirical strengthening that over-reached.
- **The REAL Gap A is just FINITENESS of governing primes** (factors of L), NOT "≤ M_1". Finiteness is still empirically true in every resolved case (no aperiodicity confirmed in any genuine case; even 375 and 9375 are periodic with FINITE governing sets). So the theorem to prove — eventual AP — remains intact; the route "prove finiteness of governing primes" is still viable, just without the `≤ M_1` strengthening.

**Concrete next-round suggestion for the outliner.** Open ONE approach targeting **finiteness of governing primes WITHOUT a `≤ rad(a_1)` bound**: the empirical pattern (P5)+(P6) suggests governing primes are always a finite subset of `{primes of a_1} ∪ {2} ∪ {small set}`, bounded by something depending on a_1 (not rad(a_1)). The cleanest live target is "the governing set is finite" itself — re-cast Gap A as finiteness, abandon the `≤ M_1` strengthening, and look for a finiteness mechanism (the 6 fences fenced specific mechanisms, not finiteness-as-such). The violation family `3·5^e` gives a sharp stress test for any new finiteness-bound candidate: any bound `q ≤ f(a_1)` must satisfy `19 ≤ f(375)` and `67 ≤ f(9375)` while still being small enough to prove finiteness. Do NOT mount any approach whose target is `q ≤ rad(a_1)` — it is refuted.
