## imo-2026-06

**Population:** empty at start of round 1 (confirmed via `sample_approaches` — 0 approaches). All 5 below are NEW. Each is a complete end-to-end attempt at the whole claim (∃ T,L>0: a_{n+T}=a_n+L for all n), with its unproved steps left as explicit gaps.

**Shared terrain (from the 3 explorers — scouting, NOT proven):**
- DEAD framing: "stabilize the set of ALL primes appearing" — it is INFINITE (proven for a_1=15 via a_{8k+6}=6(6+5k)). Do not build any approach on it.
- Right invariant: the ESSENTIAL-prime set (primes that are the unique shared factor with some earlier term); free-rider cofactor primes are infinite but irrelevant.
- Cheap structural kill available to all: gcd(a_n,a_1)>1 ⟹ every a_n has a prime factor ≤ a_1 ⟹ reduced types live in a FINITE powerset.
- Crux analogue (adapt, do not cite): aimo-0678 (mod-lcm finite-state reduction + min-of-set monovariant).
- Load-bearing AMBIGUITY flagged for ALL approaches: the problem says "for every positive integer n" (a_{n+T}=a_n+L for ALL n≥1). Numerics: transient is 0 for many starts (15,35,77,105) but NOT for all (a_1=1001: no period in 1500 terms; 315·385: no period in 1100 terms). If a transient t>0 occurs, the builder must either absorb it (enlarge T,L) or argue the problem's quantifier allows the eventual tail. EVERY approach below lists this as an open gap; the reviewer should weight approaches that handle the transient cleanly.

---

### crude-reduced-type: new
**Framing:** finite-state on residues mod the CRUDE modulus L_0 = ∏_{p ≤ a_1} p (all primes ≤ a_1). Cheap bound ⟹ reduced types in finite 2^Q ⟹ transversal family stabilizes ⟹ fixed valid-residue set V_0 mod L_0 ⟹ deterministic residue walk ⟹ eventual periodicity ⟹ lift to translation.
**Technique:** invariants/monovariants (nested family on finite lattice) + pigeonhole finite-state mod L_0.
**Key load-bearing idea:** the FREE-RIDER WALL — once the family F of reduced types is frozen by the finite prefix {a_1,…,a_{N''}}, the set of primes that could ever serve as a "rescue" (let an otherwise-invalid candidate sneak in) is bounded by max(frozen prefix), hence finite; their finite-state effect is absorbed into V_0. So the valid-residue characterization mod L_0 is EXACT.
**Hard steps / likely gaps:**
- Step 7 (free-rider wall): the "rescue primes bounded by frozen prefix" argument. Subtle case: a LATE candidate m could share a free-rider prime with a LATE a_i (i>N'') whose reduced type IS in F. Must show: that late a_i's reduced type r_i∈F (stable), so hitting a_i reduces to hitting r_i, which is the reduced-type condition — no escape. This is the real subtlety; make it airtight.
- Step 10 (lift): gap-sum-equals-L_0 must telescope correctly (cycle wraps exactly once per period).
- Transient/"for all n" resolution (see shared note).
**Builds on:** experimental explorer opening A + structural explorer opening 4.
**Cases:** even a_1 / prime-power a_1 (T=1) auto-handled (V_0 collapses to one residue); generic case = odd squarefree ≥2 prime factors.
**Watch out for:** Q = primes ≤ a_1 (NOT primes dividing a_1 — too coarse, drops 2 for odd a_1). L_0 is astronomically large; finiteness is all that's needed.

---

### essential-monovariant: new
**Framing:** bound the TRUE essential-prime set S via a min-of-set integer monovariant (aimo-0678 style), then reduce mod L=∏S (the small true L, not the crude L_0). Distinct from crude-reduced-type by (a) using the genuine essential primes and (b) proving stabilization via a MONOVARIANT, not finite-lattice nesting.
**Technique:** monovariant (min-of-set, non-decreasing & bounded) + finite-state pigeonhole mod L.
**Key load-bearing idea:** a min-of-set quantity w_n (analog of aimo-0678's w_n = min{m≥a_n : m fails the frozen invariant}) is non-decreasing and bounded ⟹ the essential-prime universe stops growing ⟹ free-rider irrelevance follows (free riders outside E never the unique shared prime).
**Hard steps / likely gaps:**
- Step 3: the bound "E_n ⊆ primes ≤ a_1" is NOT obvious — the witness a_i for p's essentiality need not have p|a_1. Either find a correct bound (p ≤ max of frozen prefix) or let the monovariant give finiteness directly.
- Step 4: the PRECISE definition of w_n and its monotonicity is the central design problem — aimo-0678's exact construction must be adapted, not copied.
- Transient resolution.
**Builds on:** structural explorer opening 5 + experimental explorer opening B.
**Cases:** T=1 sub-cases auto-handled.
**Watch out for:** do NOT conflate "essential" with "divides a_1" (2 is essential for a_1=15 but 2∤a_1). The monovariant must be the genuinely distinct contribution, not a relabeling of finite-lattice stabilization.

---

### translation-self-similarity: new
**Framing:** bypass prime-bounding and free-rider irrelevance ENTIRELY by exhibiting a translation symmetry directly. Construct T,L so the greedy rule commutes with m↦m+L (the allowed set above a_T is L + the allowed set above a_1); induct from the seed. The INDUCTIVE LIFT (not finite-state pigeonhole) is the distinct mechanism.
**Technique:** construction + induction via a translation-equivariance (functional) equation for the greedy min.
**Key load-bearing idea:** if A_{T+n} = L + A_n (allowed sets are translates) AND a_{T+n}=a_n+L (base alignment), then min A_{T+n} = L + min A_n, i.e. a_{T+n+1}=a_{n+1}+L. Induct forever. The symmetry is the engine, not prime analysis.
**Hard steps / likely gaps:**
- Lemma A (prime-divisor preservation under +L): P(a_i+L)=P(a_i) is FALSE in general; must be WEAKENED to "the greedy DECISION is preserved" (old primes persist ⟹ a_i+L still hits everything a_i hit; new primes only ADD connections, never remove, so the greedy min is unaffected upward). The correct weakening is the crux.
- Step 6 (existence of the closing return for arbitrary a_1): may collapse back to finite-state pigeonhole — this approach is a HYBRID (finite-state for existence, self-similarity for the lift). That's acceptable; keep the lift distinct.
- From-seed induction FAILS for long-transient starts (a_1=1001); must allow EVENTUAL self-similarity (base at a_N, not a_1).
**Builds on:** sieve explorer opening 3 + crux spirit of aimo-0079.
**Cases:** T=1 sub-cases trivially satisfy self-similarity; long-transient starts need the eventual version.
**Watch out for:** don't assert the false Lemma A as stated; the weakening to "greedy decision preserved" is load-bearing.

---

### covering-system-redundancy: new
**Framing:** A_n = ∩_{i≤n} ∪_{p|a_i} pZ is the complement of a covering system. Prove late primes are REDUNDANT mod a fixed L (their forbidden residue classes are already covered by the essential primes). Distinct from crude-reduced-type by proving stabilization via COVERING-SYSTEM REDUNDANCY (a late prime's constraint adds nothing), not transversal-family lattice nesting.
**Technique:** covering systems / complement-of-cover + redundancy argument + finite-state pigeonhole mod L.
**Key load-bearing idea:** a late prime q divides a_n; a_n's reduced type (P(a_n)∩E) is already a transversal of the stabilized family (hits every earlier a_i via an E-prime); so q co-occurs with an E-prime in a_n, hence q's constraint ∪qZ is a subset of ∪_{p∈P(a_n)∩E} pZ — REMOVING q loses nothing. This is the covering-theoretic form of the free-rider dichotomy.
**Hard steps / likely gaps:**
- Step 4 / Lemma B: make the redundancy airtight — "q only ever appears alongside E-primes in the same term" must be shown (it follows from the free-rider dichotomy: a newly introduced prime divides no earlier term, so it can't be the unique shared prime, so it's always accompanied by an essential prime in the hitting relation).
- Lemma C (E finite): E ⊆ primes ≤ max(frozen prefix) — cleaner bound than crude-reduced-type's "primes ≤ a_1", because the frozen prefix is explicit and finite.
- Transient resolution.
**Builds on:** sieve explorer opening 1.
**Cases:** T=1 sub-cases auto-handled.
**Watch out for:** do NOT cite Mirsky–Newman or any covering-system theorem outside knowledge_base.md — re-prove every covering step. Distinguish from crude-reduced-type: the redundancy-of-late-primes argument is the distinct load-bearing contribution.

---

### windowed-state-pigeonhole: new
**Framing:** avoid naming/computing L entirely. Prove the greedy transition depends only on a finite TUPLE state (recent residues mod M) because the "next valid m" lives in a BOUNDED WINDOW above a_n (gcd(k,k+1)=1 structure). Pigeonhole on the finite state space ⟹ recurrence ⟹ exact translation. The state-tuple + window bound is the distinct framing (no V_0 stabilization, no essential-prime analysis).
**Technique:** pigeonhole/extremal on a finite-state tuple + gcd-structure window bound.
**Key load-bearing idea:** among any W consecutive integers above a_n, one is non-coprime to each of a fixed finite family of moduli simultaneously (CRT density). If W is bounded independent of n, the greedy window is state-determined ⟹ finite-state.
**Hard steps / likely gaps:**
- Lemma A (WINDOW BOUND — the likely FATAL wall): a_{n+1}−a_n ≤ W(a_1) independent of n. The naive CRT gives W = ∏ rad(a_i) (grows with n). Need a sharp bound. POTENTIAL CIRCULARITY: the window within a period is bounded by L, but L is what we're proving exists. This approach is a BET that a window bound independent of L can be proved via gcd-structure of consecutive integers + the fixed prime set P(a_1). If the bet fails, the approach collapses — but it is genuinely different and worth fielding.
- Lemma B ("far" terms captured by recent residues): may reduce to the same stabilization crux as the other approaches. Be honest about this.
- Transient resolution.
**Builds on:** sieve explorer opening 2.
**Cases:** T=1 sub-cases (window trivially W=2 or W=p).
**Watch out for:** the window-bound circularity is the central risk. Distinguish from crude-reduced-type: tuple-state + window, never stabilizing V_0.

---

## Diversity check (framings are far apart)

| Approach | How it bounds "essential primes" | How it gets periodicity | Distinct mechanism |
|---|---|---|---|
| crude-reduced-type | crude Q = primes ≤ a_1 (finiteness) | lattice stabilization of transversal family mod L_0 | free-rider absorbed into V_0 via frozen-prefix bound |
| essential-monovariant | min-of-set monovariant (aimo-0678) | finite-state mod true L | monovariant is the engine |
| translation-self-similarity | NONE (bypasses) | inductive translation symmetry | functional equation / lift by symmetry |
| covering-system-redundancy | redundancy of late primes in the cover | covering complement stabilizes mod L | covering-theoretic redundancy |
| windowed-state-pigeonhole | NONE (bypasses via window) | tuple-state pigeonhole | window bound on the greedy gap |

No two share both the bounding mechanism and the periodicity mechanism. crude-reduced-type and covering-system-redundancy both end in finite-state-mod-L but prove stabilization by DIFFERENT arguments (lattice nesting vs covering redundancy). essential-monovariant shares the finite-state tail but bounds the essential set by a monovariant (distinct). The two bypassers (translation-self-similarity, windowed-state-pigeonhole) avoid prime-bounding by different routes (symmetry vs window).

## Copy recommendation

**crude-reduced-type** has TWO viable fills for its free-rider wall (step 7):
- (a) DENSITY / pigeonhole on rescue primes (the frozen-prefix bound sketched in the file).
- (b) WITNESS CONSTRUCTION (experimental explorer opening D): for each essential prime p, exhibit a specific witness term a_i whose reduced type makes p unavoidable; then any candidate avoiding p must hit a_i via a prime > a_1 (large), bounding the candidate range.

Both are worth pursuing. Recommend the reviewer **copy** crude-reduced-type into a twin (slug `crude-reduced-type-witness`) with fill (b), so both paths run in parallel. (Do NOT split the proof — each twin is a complete attempt with a different gap-fill mechanism.) I have NOT pre-opened the twin; the reviewer's copy operation is the cleaner way to create it. If the reviewer prefers, the builder of crude-reduced-type can simply be told to pursue fill (a), and a separate builder can open the witness variant — but the copy mechanism is the sanctioned route.

## Build-set recommendation

Field all 5 new approaches to the outline-reviewer for ranking. Suggested build set (let the reviewer decide):
- crude-reduced-type (advance — the most concrete scaffold; closest to a complete proof)
- essential-monovariant (advance — the aimo-0678 adaptation is promising)
- translation-self-similarity (advance — genuinely different lift; the false-Lemma-A weakening needs a builder's attention)
- covering-system-redundancy (advance — the redundancy argument is clean and may be the most elegant)
- windowed-state-pigeonhole (advance — high-risk, high-reward; the window-bound circularity may kill it, but the bet is worth one builder round)

If the reviewer agrees with the copy recommendation, add `crude-reduced-type-witness` (copy-of crude-reduced-type) to the build set.
