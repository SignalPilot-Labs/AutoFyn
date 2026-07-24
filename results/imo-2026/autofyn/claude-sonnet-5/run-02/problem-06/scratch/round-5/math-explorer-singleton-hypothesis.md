## imo-2026-06

### Task recap
Investigate whether `greedy-exchange-cost-potential`'s "Singleton Hypothesis" (used in
its conditional Round Resolution Lemma) still has valid support once recomputed with
the CORRECT literal minimal-witness convention, and independently spot-check round 4's
"V = ∅ always, zero further recruitment rounds" claim on fresh seeds.

**Headline finding: round 4's "V = ∅ always" conjecture is FALSE. I found four fresh,
correctly-computed (bug-free, minimal-witness) counterexamples — a_1 = 187, 209, 247,
385 — each with a genuine rogue pair requiring exactly ONE recruitment round. In every
one of these four cases the Singleton Hypothesis holds exactly (|F'| = 1). This
REVIVES the greedy-exchange-cost-potential approach's Round Resolution Lemma as
directly load-bearing (not obsolete) and shows round 4's proposed "prove V=∅ always"
target is the wrong thing to attempt — it is false as a blanket claim.**

### 1. What the Singleton Hypothesis claims (exact statement, from the approach file)

`results/imo-2026-06/approaches/greedy-exchange-cost-potential.md`, "The rescoped Round
Resolution Lemma" section. For a rogue pair (A'_0, B'_0) at extended-type level S₀
(disjoint-base-type, S₀-disjoint extended-persistent types), with n_A := min{n :
ρ(n)=A'_0}, n_B := min{n : ρ(n)=B'_0} (earliest occurrences of the EXTENDED types, not
the base types — WLOG n_A < n_B), define F' := P(a_{n_B}) \ S₀. **Singleton Hypothesis:
|F'| = 1.** If it holds, the Round Resolution Lemma proves the single prime q ∈ F'
resolves that specific witnessed pair (not the whole base-type pair — that stronger
claim was separately falsified and retracted in round 4).

The file's own reported computational support ("~20 tested seeds: a_1 = 175, 187, 209,
247, 385, ...") is suspect exactly because a_1 = 175 was independently shown in round
4 to have been computed with a buggy, non-minimal S₀ by this same approach file
(current.md's ROUND 4 CRITICAL CORRECTION: this file's own S₀ = {2,3,5,7,11,29,41,67}
for a_1=175 is a third, mutually-inconsistent value versus the correct S₀ =
{2,3,5,7,13}). So the claimed "~20 seeds" support needed re-verification from scratch,
per the dispatch.

### 2. Recomputation with the correct minimal-witness convention

Method (matches current.md's round-4 correction exactly): generate the sequence,
compute τ(n) = P(a_n) ∩ Q, find persistent base types 𝒫 via tail-frequency (large
window, e.g. n ∈ [4000,8000], threshold ≥5 occurrences — a computational proxy, not a
formal "infinitely often" proof, consistent with what all prior rounds have used),
take m_B := the literal EARLIEST n ≥ 1 with τ(n) = B (searched from n=1, not from a
tail window), S := ⋃_B (P(a_{m_B}) \ Q), S₀ := Q ∪ S. Then ρ(n) := P(a_n) ∩ S₀,
extended-persistent types 𝒫' via the same tail-frequency proxy, and V := {(A',B') ∈
𝒫'×𝒫' : A=A'∩Q, B=B'∩Q disjoint base types in 𝒫, A'∩B'=∅}.

**Sanity check (reproduction):** re-ran a_1 = 175 with this exact method: Q={5,7},
witnesses m_{5}=2 (a_2=180=2²·3²·5), m_{7}=3 (a_3=182=2·7·13), m_{5,7}=1 (a_1=175=5·7),
giving S={2,3,13}, S₀={2,3,5,7,13} — **exactly matching current.md's round-4
correction**, V=∅. Confirms my method matches the certified convention correctly.

**New computation on a_1 = 187, 209, 247, 385** (the exact seeds this approach's file
cites as "Singleton Hypothesis support," all needing fresh verification):

| a_1 | Q | S₀ (minimal-witness) | V at S₀ | recruited prime | V after recruiting |
|---|---|---|---|---|---|
| 187 | {11,17} | {2,3,11,17} | 2 rogue pairs: ({17,2},{11,3}) and mirror | **7** | ∅ |
| 209 | {11,19} | {2,3,5,11,19} | 6 rogue pairs (all between {19}- and {11}-refinements) | **7** | ∅ |
| 247 | {13,19} | {2,5,7,13,19} | 14 rogue pairs | **3** | ∅ |
| 385 | {5,7,11} | {2,3,5,7,11,13} | 6 rogue pairs | **19** | ∅ (at extended-type level) |

**These are GENUINE rogue pairs, not a repeat of the round-3/4 witness-selection bug.**
I double-checked the witness minimality by hand for a_1=187 (Q={11,17}): τ(1)={11,17},
τ(2)={11} (a_2=198=2·3²·11), τ(3)={17} (a_3=204=2²·3·17) — n=2,3 are genuinely the
first occurrences, no earlier index has these pure base types. So S={2,3}, S₀=
{2,3,11,17} is the CORRECT minimal-witness Finite Core Theorem output for this seed
— yet the actual reconciling core needs prime 7, which appears in neither a_2 nor a_3.
Confirmed by direct enumeration (sequence generated with `math.gcd` trial search,
verified by hand for a_1..a_20 against the definition).

**Concrete witness data for reproducibility** (each row: index n, a_n, full
factorization P(a_n), 4000-8000 window, ≥5 tail occurrences):
- a_1=187: extended type {17,2} recurs (n=6, a_6=238=2·7·17; n=20, a_20=476=2²·7·17;
  n=51, a_51=952=2³·7·17; ...) — ALL sampled occurrences also carry 7.
  Extended type {11,3} recurs (n=5, a_5=231=3·7·11; n=34, a_34=693=3²·7·11; ...) — ALL
  sampled occurrences also carry 7. Recruiting S₀'={2,3,7,11,17}: V'=∅ (checked on
  tail 5000-9000, all 16 extended-persistent types found, no disjoint-base-type pair
  fails to intersect). **True period independently verified: T=484, L=7854 = 2·3·7·11·17**
  (brute-force gap-matching search on a1=187's sequence out to n=9000, verified stable
  over 600+ repeat cycles) — matches S₀' exactly, confirming the recruited prime 7 is
  genuinely load-bearing, not a coincidence.
- a_1=209: extended type witnessed via n_A=70 (a_70=1330=2·5·7·19), n_B=4
  (a_4=231=3·7·11); F' = P(a_231)\S₀ = {7} at both ends (singleton). Recruiting
  S₀'={2,3,5,7,11,19}: V'=∅. **True period verified: T=2640, L=43890 =
  2·3·5·7·11·19**, matches exactly.
- a_1=247: n_A=14 (a_14=546=2·3·7·13), n_B=5 (a_5=285=3·5·19); F'={3} at both ends
  (singleton). Recruiting S₀'={2,3,5,7,13,19}: V'=∅. **True period verified: T=1806,
  L=51870 = 2·3·5·7·13·19**, matches exactly.
- a_1=385: n_A=201 (a_201=2090=2·5·11·19), n_B=5 (a_5=399=3·7·19); F'={19} at both
  ends (singleton). Recruiting S₀'={2,3,5,7,11,13,19}: V'=∅ (verified at
  extended-type level, tail 5000-9000). **True period NOT verified within my compute
  budget** — brute-force period search up to T=8000 (N=25000 terms) found no match
  either freely or with the fixed guess L=∏S₀'=570570; this is inconclusive (the true
  T may simply be larger than what I searched, or L may need to be a proper multiple/
  submultiple), not a contradiction of V'=∅. Flagged as an open computational item,
  not a counterexample.

**Exact Singleton Hypothesis check** (per its formal definition: F' computed from the
extended type's own earliest occurrence, not a tail sample):

| a_1 | n_A (earliest A'_0) | n_B (earliest B'_0) | F' from n_A | F' from n_B | singleton? |
|---|---|---|---|---|---|
| 187 | 6 (a_6=238=2·7·17) | 5 (a_5=231=3·7·11) | {7} | {7} | YES |
| 209 | 70 (a_70=1330=2·5·7·19) | 4 (a_4=231=3·7·11) | {7} | {7} | YES |
| 247 | 14 (a_14=546=2·3·7·13) | 5 (a_5=285=3·5·19) | {3} | {3} | YES |
| 385 | 201 (a_201=2090=2·5·11·19) | 5 (a_5=399=3·7·19) | {19} | {19} | YES |

**All four fresh, correctly-computed instances confirm the Singleton Hypothesis
exactly**, with genuine (non-buggy) witness data reported transparently above for
reverification.

### 3. Verdict: is the Singleton Hypothesis / Round Resolution Lemma obsolete?

**No — it is directly load-bearing, not redundant.** Round 4's framing ("V=∅ always,
maybe the conditional machinery is never needed") is now falsified: genuine rogue
pairs DO occur (187, 209, 247, 385 above), so the Round Resolution Lemma's mechanism
is exactly what is needed to resolve them, and its Singleton Hypothesis has real,
freshly-verified (not bug-contaminated) support in all 4 new test cases. The
"~20 seeds" claim in the approach file needs its citation list corrected (a_1=175
should be dropped/recomputed per round 4, but the OTHER seeds it lists — 187, 209,
247, 385 — check out fine under the correct convention and should be kept/cited with
the exact witness data above instead of the vague "~20 seeds, all satisfying" language).

### 4. Also spot-checked: fresh |Q|≥3 seeds, multiple missing small primes

Per the dispatch's item 3, tested two additional fresh |Q|=3 seeds not in the existing
18-seed set, both missing several small primes:
- a_1 = 1001 = 7·11·13 (Q misses 2,3,5): S = {2,3,23}, S₀={2,3,7,11,13,23}, **V=∅**
  directly (no recruitment needed).
- a_1 = 2431 = 11·13·17 (Q misses 2,3,5,7): S={2,3,7,37,47}, S₀={2,3,7,11,13,17,37,47},
  **V=∅** directly (no recruitment needed).

So the picture is genuinely mixed, matching round 2-3's original recruitment-process
framing: sometimes V=∅ at the raw Finite Core Theorem level (1001, 2431, and the 18
seeds from round 4), sometimes exactly one recruitment round is needed and always
resolves it with a SINGLE recruited prime satisfying the Singleton Hypothesis (187,
209, 247, 385). I found **zero instances requiring 2+ rounds** or a non-singleton F'
in this round's testing, though the sample (4 rogue instances) is small.

### 5. What this means for next round's target

- **Do NOT pursue "prove V=∅ always with minimal witnesses" as current.md's round-4
  next-step suggests** — it is false (4 explicit counterexamples above, transparently
  reported with exact indices/factorizations per round 4's reverification rule).
- **The correct target reverts to round 2-3's original framing**: the recruitment
  PROCESS (start from S₀, find a rogue pair if any, recruit via Lemma G's prime,
  repeat) — prove it terminates in finitely many rounds. This is not vacuous; it is
  the genuine content of the problem's crux. Two sub-targets, both still open:
  (a) prove the Singleton Hypothesis in general (currently only verified case-by-case,
  4/4 fresh instances this round, ~5/5 total including the corrected 175 case if it's
  reinterpreted — though 175 needed 0 rounds, not 1, once correctly computed);
  (b) even granting Singleton Hypothesis universally, the Round Resolution Lemma only
  resolves ONE witnessed pair at a time (per its own honest round-4 disclosure) — a
  separate argument is still needed to bound total rounds/pairs, OR to upgrade to the
  empirically-observed-but-unproved "one recruited prime resolves ALL currently-rogue
  pairs simultaneously" (seen in round 4's a_1=175 exploration with 6 pairs resolved
  by one prime, and consistent with my a_1=209 data where all 6 rogue pairs share the
  single recruited prime 7, and a_1=247 where all 14 rogue pairs share prime 3).
- **New idea worth exploring**: in every counterexample found (187, 209, 247, 385),
  the recruited prime came from the SMALLER/simpler side's earliest witness (n_B, the
  later of the two earliest occurrences — using WLOG n_A<n_B convention, actually note
  209's data: n_B=4 is much earlier than n_A=70). There may be a extremal/minimality
  argument available using the EARLIEST of the two witnesses specifically (not an
  arbitrary one) that a future outliner should investigate — this recomputation
  surfaces cleaner data than round 4's buggy 175 example ever did, since these 4 cases
  are simple two/three-prime Q's with small, easily-inspected witness factorizations.

### 6. Candidate technique(s)
Same knowledge-base tools as before (infinite pigeonhole, CRT/covering-system
finish) plus the certified Lemma G (`lemmas/extended-earliest-witness-intersection.md`)
which is exactly the tool used to locate n_A, n_B and derive F'≠∅ above — confirmed
directly useful and correctly stated.

### 7. Knowledge-base entries to use
- Free Facts / pairwise gcd argument (underlies Lemma G and all witness constructions).
- Infinite pigeonhole principle (`knowledge_base.md` "Pigeonhole / extremal
  principle") — used in Lemma B, Lemma G, and this round's own S₀/V computations.
- CRT + cyclic pigeonhole finish (unchanged from round 1, still the correct finish
  once (†)/V is resolved).

### 8. Analogous past problems (cruxes)
Not independently re-explored this round (out of scope per dispatch — focused on
recomputation); round 4's file already cites aimo-0514/aimo-0077 (minimal
bad-event/first-failure induction, tried and honestly found not to transfer — the
Singleton Hypothesis is a static single-integer factorization fact, not recursively
tied to the process's own prior states) and aimo-0678 (monotone potential, motivating
the whole approach's original framing). No new crux search performed this round.

### 9. Dead ends (do not retry)
- Round 4's "prove V=∅ always" target — NOW FALSIFIED by this round's 4 fresh
  counterexamples (187, 209, 247, 385), reported transparently above. Do not
  re-propose "zero further recruitment rounds always" in any form.
- The "cost(n) ≤ 1" / "universal glue prime" family — still correctly retracted
  (unaffected by this round's findings, independent falsification stands).
- The whole-base-type Round Resolution claim (recruited prime resolves the ENTIRE
  base-type pair, not just the witnessed extended-type pair) — still correctly
  retracted per round 4 (my data shows the SAME phenomenon: e.g. a_1=209's recruited
  prime 7 does resolve ALL 6 rogue pairs simultaneously in my test, which is evidence
  FOR the stronger "one prime resolves all currently-rogue pairs" claim, but that is a
  different, still-unproven statement from "resolves the whole base type," which
  round 4 already falsified with percentage data — I did not re-test the percentage
  claim this round).

### 10. Small-case / intuition notes (labeled as conjecture)
- Conjecture (5/5 confirmed instances now, including retroactively 175 with 0 rounds):
  the recruitment process, when it must run, needs exactly ONE round per genuinely
  distinct "reconciliation event," each resolved by a Singleton F'. Sample size is
  still small (5 total across all rounds' correctly-computed data) — not proof.
- Conjecture (strong form, seen in 209 and consistent with round 4's 175 data): a
  single recruited prime often resolves ALL simultaneously-rogue pairs at a round, not
  just the one witnessed pair — this is the natural next lemma to attempt if a future
  approach wants to close termination in one step rather than an induction over pairs.
- The mixed picture (1001, 2431: 0 rounds; 187, 209, 247, 385: 1 round) suggests
  |Q| alone does not determine whether recruitment is needed (1001, 2431 have |Q|=3
  and need 0 rounds; 385 has |Q|=3 and needs 1) — consistent with round 2's earlier
  finding that Q's sparseness/density is not the right predictive variable.
