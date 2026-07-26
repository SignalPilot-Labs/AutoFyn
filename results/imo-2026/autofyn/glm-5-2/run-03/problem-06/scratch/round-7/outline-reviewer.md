# Round 7 outline-reviewer report — `imo-2026-06` (PIVOT ROUND)

Start: 2026-07-25 19:47 UTC. Pivot context (central conjecture `q ≤ rad(a_1)` REFUTED by `a_1=375`→gov 19, `a_1=9375`→gov 67; theorem still holds — both periodic) read from run_state + current.md. Per-role rules + 6 fences + 16 dead mechanisms applied with the corrected fence-scope (rad-77 fence is `f(rad)`-specific → does NOT fence `f(a_1)`-bounds; no-fixed-modulus fence is residue-specific → does NOT fence non-residue statistics).

I ran three independent computational probes (naive O(N²) gcd-greedy, the gold standard; NEVER the inverted `/tmp/round-4/fast_greedy.py`) before gating. Findings reported per-approach below.

---

## `f-of-a1-bounded-nonresidue-statistic` (new) — APPROVE / CHANGES REQUESTED

**Verdict: APPROVE for build.** This is, on the merits and on my independent computation, the most promising single line of attack surfaced in 7 rounds. The central empirical bet is CONFIRMED; the skeleton is sound; the fences are genuinely cleared.

**Independent verification of the load-bearing claim (Step 4, forward-determinism at finite k).** I computed the minimal forward-deterministic window-length `k_*` for the `D_n`-window `(D_{n-k+1},…,D_n) → d_{n+1}` (the NEXT increment, NOT the tautological `d_n = min D_n` — I caught and fixed that indexing trap in my own probe) against the fenced single-value `d_n`-window for comparison, with `N_check > T` per case:

| `a_1` | `M_1` | `T` | `D_n`-window `k_*` | `D_n`-window conflicts@`k_*` | `d_n`-window conflicts@k=5 |
|---|---|---|---|---|---|
| 15 | 15 | 8 | 1 | 0 | many (fenced, round-4) |
| 35 | 35 | 34 | 1 | 0 | many |
| 77 | 77 | 18 | 1 | 0 | many |
| 91 | 91 | 20 | 1 | 0 | many |
| **175** | **35** | **274** | **16** | **0** | many |
| **847** | **77** | **1744** | **1** | **0** | many |
| **375** (refutation witness) | 15 | 852 | 1 | 0 | many |

Key findings:
1. **The `D_n`-window is genuinely richer than the fenced `d_n`-window.** Where the single-value `d_n`-window has conflicts at every `k` up to 5 (reproducing the round-4 fence) for the hard cases, the set-valued `D_n`-window is forward-deterministic at `k=1` for {15,35,77,91,847,375} and at `k=16` for `a_1=175`. The distinction the outline draws is REAL, not verbal.
2. **The rad-77 pair (77 vs 847) both pass at `k=1`.** Same `M_1=77`, different `T` (18 vs 1744) — and `k_*` is the SAME (1) for both. The state space `2^{k_*·M_1} = 2^{77}` is astronomically larger than both `T` values, so there is NO contradiction with the rad-77 impossibility (which bites only when the realized state count is ~`T`). The route genuinely clears the rad-77 fence.
3. **The `a_1=175` exception is RESOLVED.** `k_*(175)=16`, finite. I traced the lone conflict: it sits at the FORCED step `n=234` where `D_{234}={21}` (singleton, `|D_n|=1`), which coincides with periodic forced steps `D_{25}=D_{46}=…={21}`; the singleton does not encode `a_n`'s value, so the successor `d_{n+1}` is not pinned by `D_n` alone. A window of length 16 captures enough backward context to separate the transient forced step from its periodic lookalikes. This is the `D_n`-slack fence (|D_n|≥2 almost everywhere) cutting the OTHER way: at the rare forced steps the slack is absent and a longer window is needed, but finitely so.
4. **`k_*` is NOT a function of `M_1`** (`a_1=175`, `M_1=35` → `k_*=16`; `a_1=847`, `M_1=77` → `k_*=1`), so it is at least consistent with an `f(a_1)`-bound (not `f(rad)`).

**Gates for the builder (carried as CHANGES REQUESTED, not blocking):**
- **Step 0 (mandated by the outline):** extend the `k_*` table to `a_1 ∈ {9375, 385, 715, 2085, 145}` and to MORE `3·5^e` family members (`e=7,9`), with `N > 2·T` per case. Confirm `k_*` stays finite and does not blow up with `a_1`. (My probe covered the rad-77 pair and both refutation witnesses — the critical fence-clearing cases — but not the full stress set.)
- **Step 4 (the PROOF — the load-bearing open gap):** the forward-determinism is empirically robust but UNPROVEN. The builder must exhibit a greedy-dynamic mechanism showing `D_n`-window determines `d_{n+1}` from the local structure (gap bound `d_n ≤ M_1`, window-multiple counting), WITHOUT assuming finiteness of the governing-prime set. **Circularity test (the outline's own worry):** if the only proof that "`k_*` is finite" passes through "the governing-prime set is finite" (Gap A), the route is circular — declare dead. The promising sign: my `a_1=175` trace shows the obstruction is concrete (forced-step ambiguity resolved by finite backward context), not a global-finiteness dependency — but that is evidence, not a proof.
- **Do NOT** use a variational/tie-break argument (`D_n`-slack-obstruction fence, round 6). Use ONLY pigeonhole + forward-determinism + `aimo-0907-coincidence-criterion` part A (one self-coincidence of a single-valued forward-deterministic map ⇒ eventual periodicity — this part is trivial and sound, no finiteness assumption on the state space beyond "finite `k_*` ⇒ finite alphabet `2^{k_*·M_1}`").

**Strict-bar check:** NOT in the 16-dead/6-fence list. Non-residue (clears no-fixed-modulus). `f(a_1)`-bounded state space `2^{k·M_1}` with `M_1 ≤ a_1` (clears rad-77, which is `f(rad)`-specific). Targets finiteness, not `q ≤ rad`. PASS.

---

## `parametric-recruitment-family` (new) — APPROVE / CHANGES REQUESTED

**Verdict: APPROVE for build (sound skeleton, hard step identified, cofactor-collapse gate explicit).**

**Independent verification.** I confirmed the bedrock: `a_1=375=3·5³`, `M_1=rad=15`, naive greedy gives `T=852`, `L=3990=2·3·5·7·19`, governing set exactly `{2,3,5,7,19}` (5 primes; gov `19 > 15 = rad`). Recruitment terminated after 5 primes — empirically, the skeleton `G={2,3,5,7,19}` is closed. The concrete terrain (the `3·5^e` family with `L=210·X(e)`) is genuinely new and was invisible pre-refutation.

**Gating cautions (the outliner's flagged risks, which I judge REAL but not skeleton-fatal):**
- **Cofactor-collapse (Step 4, the load-bearing step).** I traced the mechanism. The "no-new-holes" invariant asks: when a new prime `q` is recruited, does it open holes at residues previously covered? The hole-coverage check on a `G`-smooth candidate `m=a_n+d` requires `gcd(m, a_i)>1 ∀i≤n`; since `m` is `G`-smooth, this asks whether `m`'s `G`-primes hit each `a_i`'s `G`-prime-set. For `a_i` with prime factors OUTSIDE `G`, the hit must come through a `G`-prime dividing `a_i` — which is structural (a `G`-membership fact), NOT a cofactor factorization. This is genuinely different from the cofactor-bound step (which bounds `primefactors(k)` for the `q`-multiple `qk`). HOWEVER, the "recruitment strictly shrinks the hole-set" sub-lemma — proving the recruited `q`-multiple is admissible at the TRIGGERING step — is given by construction (the greedy picked it), so that half does not need cofactor bounding. The risk is in the "does NOT open new holes elsewhere" half, which depends on the greedy's future dynamics. The builder must prove this without cofactor bounding; if it collapses, declare dead (the negative lemma "hole-patching reduces to cofactor-bound" would itself be a useful fence).
- **Generalization beyond `3·5^e` (serious).** Step 3 is family-specific; Steps 4–5 must hold for ARBITRARY `a_1`. If the generalization fails, this approach only solves the special case `a_1=3·5^e` (the refutation-witness family) — still genuine progress on the hardest sub-case, but not the whole theorem. Flag: the builder must either generalize or honestly declare a partial result.
- **Selective recruitment.** `G={2,3,5,7,19}` — not all primes `≤ M_1=15` are recruited (11, 13 are NOT). The mechanism must explain selectivity, not assume "all small primes recruited." (Confirmed by my computation: 357 distinct primes appear in `a[0..2999]` for `a_1=375`, but only 5 govern.)

**Strict-bar check:** NOT in the 16-dead/6-fence list. Structural-covering (not cofactor/residue/monovariant/variational/Schur/primal-dual/syndetic). Targets finiteness. PASS. Per the deep-stall rule (accept a genuinely-new approach with an explicit negative-lemma fallback even if its crux is open), this is approved with the cofactor-collapse fallback mandated.

---

## `p1-equals-2-direct` (revise) — APPROVE / CHANGES REQUESTED

**Verdict: APPROVE for build (revise).** Dropping the refuted `r ≤ M_1` target is correct and verified: `a_1=375` IS a `|P_1|=2` case (`P_1={3,5}`, `M_1=15`) with governing prime `19 > 15`, so any `≤ M_1` target is dead in this approach's own regime. The re-target to finiteness via the certified `cofactor-P1-divisibility` lever is sound.

**Gating cautions:**
- **`r ≤ a_1` is TRIVIAL unless sharpened.** The witnesses satisfy `19 ≤ 375`, `67 ≤ 9375` — but `r ≤ a_1` is a vacuous bound for finiteness (it doesn't bound the NUMBER of governing primes, only their individual size, and even that is the trivial observation that the first `r`-multiple has cofactor `k ≥ 1` so `r ≤ a_{n_1} ≤ a_1 + (n_1-1)M_1`). The framing must aim at a NON-TRIVIAL finiteness argument: the slot-counting must show that finitely many "large-prime + small-cofactor" slots exist per period (bounded by `O(a_1)`), so infinitely many distinct large `r`-values cannot all be accommodated. The outline's candidate `r ≤ C·a_1` is a size bound; what's actually needed is a CARDINALITY bound on `G ∩ (M_1, ∞)`. The builder must clarify which is being argued.
- **Cofactor-bound collapse (Step 4).** `cofactor-P1-divisibility` is a certified LEMMA (every `r`-multiple cofactor `k` carries `p` or `q`). USING it to bound `r` might re-invoke the cofactor-bound circularity if Step 4 needs the FULL factorization of `k` (not just the `p`/`q`-divisibility). The distinction: the lemma bounds `k` to carry `p` or `q` (a `|P_1|`-structural fact); the full factorization is what's fenced. The builder must keep Step 4 at the `p`/`q`-divisibility level.
- **Do NOT re-walk Schur Step 7** (`schur-cofactor-premise-fails-in-periodic-regime` — the cofactor-prime-finiteness premise is provably false in the periodic regime). The mount Steps 1–6 are reusable; Step 7 is not.

**Strict-bar check:** NOT in the dead/fence list. Re-targets finiteness (not `q ≤ rad`). The `cofactor-P1-divisibility` lever is certified and survives the pivot. PASS.

---

## `transversal-saturation` (advance / hold) — hold as live lemma-source

Not actively built this round (the outliner holds it as the certified conditional-proof + lemma source). The 30 lemmas, conditional endgame, LOCK sub-case, and 6 fences are all UNAFFECTED by the pivot (none used `q ≤ rad` as a certified lemma). Rank-preserved at the top of the field. The finiteness wall is now attacked by the three approaches above.

---

## Diversity-of-thought assessment

The three buildable approaches are GENUINELY DIVERSE in framing/route, not costumes of one idea:
- `f-of-a1` — pigeonhole/finite-state on a set-valued non-residue window statistic (deterministic-dynamical).
- `parametric-recruitment` — structural covering/hole-patching on the recruitment mechanism (combinatorial-covering).
- `p1-equals-2-direct` — minimal-criminal + cofactor-structural lever specialized to `|P_1|=2` (number-theoretic/structural).

They do NOT share a single gap: `f-of-a1`'s crux is forward-determinism-of-`D_n`-window; `parametric-recruitment`'s is hole-closure-without-cofactor; `p1-equals-2-direct`'s is slot-counting-without-full-cofactor-factorization. If one dies, the others are unaffected. This is the first round since round 1 where the field is framing-diverse rather than collapsed to one wall.

**The single most encouraging signal:** my independent computation CONFIRMS `f-of-a1`'s central bet (`k_*` finite across 6 cases incl. the rad-77 fence-pair and BOTH refutation witnesses). This is the first approach in 7 rounds whose load-bearing empirical claim has survived my direct verification on the fence-clearing and refutation cases. It is the priority build.

---

## Ranking (K=32 Elo, head-to-head, anchored to last outcomes)

Registered at cold-start 1500: `parametric-recruitment-family`, `f-of-a1-bounded-nonresidue-statistic`. `p1-equals-2-direct` revised keeps its slug (stale outcome cleared by ranking). The two round-5 dead-ends (`two-coincidence-periodicity`, `deviation-index-descent`) kept low. Newcomers compared head-to-head against established approaches (not just each other) so their ratings anchor to real opponents.

Post-round-7 field (best-first):
1. `transversal-saturation` 1680 (top lemma-source, certified conditional proof)
2. `prime-power-dichotomy` 1614 (lemma-source)
3. `f-of-a1-bounded-nonresidue-statistic` 1596 (NEW — highest-ranked newcomer; my probe confirms the central bet on the fence-clearing pair + refutation witnesses)
4. `crt-period-lifting` 1582 (lemma-source)
5. `p1-equals-2-direct` 1549 (revised; stale cleared)
6. `parametric-recruitment-family` 1526 (NEW — sound skeleton, less empirically verified than `f-of-a1`)
7. `minimal-criminal-schur-contradiction` 1524 (mount alive, Schur step dead)
8. `two-coincidence-periodicity` 1448 (dead-end, round 5)
9. `deviation-index-descent` 1445 (dead-end, round 5)
10. `primal-minimal-support-stabilization` 1434 (fenced ≡ Gap A)

`f-of-a1` ranks above the round-4 `p1-equals-2-direct` (certified-lemma + revised) on the strength of direct empirical confirmation of its load-bearing claim; it draws just below `transversal-saturation` (which carries the certified conditional proof — a different, already-delivered contribution). `parametric-recruitment` ranks below the lemma-sources (certified deliverables) and above the dead-ends, reflecting a sound-but-unverified skeleton.

---

## Build set

build set: f-of-a1-bounded-nonresidue-statistic, parametric-recruitment-family, p1-equals-2-direct

Confirms the outliner's suggestion. Priority order: `f-of-a1` (strongest empirical signal — the builder's Step 0 is to extend my `k_*` table to the full stress set, then attack the Step 4 forward-determinism PROOF with the circularity test explicit); `parametric-recruitment` (build the hole-patching skeleton on the `3·5^e` bedrock, gate on cofactor-collapse); `p1-equals-2-direct` (revised — re-target finiteness via `cofactor-P1-divisibility`, keep Step 4 at the `p`/`q`-divisibility level).
