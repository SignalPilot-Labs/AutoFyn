## Lens

crux-descent — scout routes to **prove Lemma 4 directly** (the non-consecutive case), i.e. for all i<j, P(a_i)∩P(a_j)∩Q_R ≠ ∅ with R:=rad(a_1), Q_R:={primes ≤ R}. The consecutive case (j=i+1) is already proved (gap bound ⟹ shared prime ≤ R). The open case is non-consecutive pairs. No proof is attempted here; only terrain is scouted.

## The crux, restated

**Lemma 4 (crux).** *Every pair of terms a_i, a_j (i<j) shares a prime ≤ R = rad(a_1).*

Three equivalent restatements, each suggesting a different attack:

- **(F-intersection)** The stabilized type family F_∞ = {τ(a_i) : i≥1} ⊆ 2^{Q_R} \ {∅} (τ(x):=P(x)∩Q_R) is **pairwise intersecting**: no two types in F are disjoint. (Disjoint types S,T ∈ F ⟺ ∃ terms of those types sharing no small prime ⟺ Lemma 4 fails.)
- **(E-finite)** The essential-prime set E ⊆ Q_R is finite (E = primes that are the *unique* shared prime of some pair). Lemma 4 ⟹ E ⊆ Q_R (uniqueness forces the small shared prime to BE the essential one). This is the form the whole field needs.
- **(free-rider dichotomy)** No large prime q>R is ever the *unique* shared prime between two terms — every large-prime link comes with a small-prime link. Equivalently, the "free-rider co-occurrence" observed numerically (essential-monovariant builder's obstruction) is a theorem, not just an empirical fact.

**Confirmed numerically (conjecture, NOT proof):** Lemma 4 holds for a_1 ∈ {6,10,15,35,77,105,1001} over 60–120 terms (all C(n,2) pairs checked); E ⊆ Q_R in every case; F is pairwise intersecting in every case. The stabilized family F is genuinely pairwise-intersecting on Q_R — BUT note the family restricted to *only* P(a_1) is **NOT** pairwise intersecting (e.g. a_1=15 has types {3} and {5} on P(a_1), disjoint). So the proof genuinely uses Q_R (primes ≤ R), not just P(a_1). This rules out a "restrict to a_1's primes" shortcut.

## Candidate routes

### Route A — Minimal-counterexample descent on (i,j), aimo-0030 spirit

**What it would prove.** Lemma 4 directly, by contradiction: assume a minimal counterexample pair (a_i, a_j), i<j-1, sharing only primes >R, and manufacture a smaller counterexample (or an admissible integer in (a_{j-1}, a_j) contradicting greedy minimality).

**What it needs.**
- Minimality witness: by induction on (j-i), the pair (a_i, a_{j-1}) shares a small prime u ≤ R (gap j-1-i < j-i). Lemma 3 gives a small prime t ≤ R shared by a_{j-1}, a_j.
- The "strip" step: build an integer x ∈ (a_{j-1}, a_j) that is admissible against a_1,…,a_{j-1} using only small primes ≤ R — then greedy minimality of a_j is contradicted.
- Candidate x = a_{j-1} + t (next multiple of t above a_{j-1}, since t | a_{j-1}). This shares t with a_{j-1} (and a_j), but is **not guaranteed admissible** against a_1,…,a_{j-2}: those may share only a large prime with a_{j-1}, hence with x. THIS IS THE WALL the essential-monovariant builder already hit.

**Where it likely breaks.** The natural candidates (a_{j-1}+r, a_j−s) each share a small prime with TWO terms but not with ALL intermediate terms. The aimo-0030 descent sidesteps this by stripping b to its small-prime-only part and using the game-move structure (n→x coprime, x good) — P6 has no such "move" structure, so the descent does not port mechanically. The descent *spirit* (strip to small-prime-only witness) is right, but the P6-native "strip" operation is not obvious.

**Verdict: multi-round bet.** The structural analogy is the strongest in the corpus, but the descent step needs a P6-native construction of a smaller admissible witness that has not yet been found.

### Route B — Stabilized intersecting family (Route A in type language)

**What it would prove.** That F_∞ is pairwise intersecting, i.e. Lemma 4.

**What it needs.**
- F stabilizes at some finite N (already standard: F_n monotone-increasing on finite 2^{Q_R}, crude-reduced-type proves this).
- After N, every new term a_{n+1} (n≥N) has τ(a_{n+1}) ∈ F and is admissible against a_1..a_n. For Lemma 4 we need: τ(a_{n+1}) is a transversal of F (hits every type in F). This is EXACTLY Lemma 4 restricted to (a_{n+1}, a_i) for all i — circular as a proof of Lemma 4.
- A non-circular mechanism: if S,T ∈ F are disjoint, the greedy's "min admissible in window of length R" rule should forbid T from ever appearing after S (or vice versa). Concretely: once a term of type S has appeared, the next term of type T would need to share a large prime with the S-term; but the window (a_{n}, a_n+R] should contain an integer of type (S ∩ T) ∪ {small prime of T} that is admissible — contradiction.

**Where it likely breaks.** Same wall: "the window contains an admissible integer of a desired type" is a sieve-density claim, and the density of type-T integers in a length-R window can be very low (type T uses several primes, density ∏ 1/p). Route B is Route A in type language; no independent engine.

**Verdict: multi-round bet.** Cleanest REFORMULATION of Lemma 4, but proves nothing on its own. Useful as the target statement for another route to hit.

### Route C — The "multiples of R are universally admissible" engine + descent

**What it would prove.** A KEY structural fact (not yet recorded as a lemma): **a_j is a multiple of R = rad(a_1) for many j, and whenever a_j is a multiple of R, Lemma 4 holds for (a_i, a_j) automatically** (because a_j is divisible by every prime of a_1, and a_i has a prime of a_1 by Lemma 1 — so they share that prime ≤ R). This is a partial-result lemma the outliner should certify and park.

**The engine (already proved, restated).** Multiples of R are admissible against every prefix (Lemma 2's proof: a multiple of R is divisible by every prime of a_1; every term shares a prime of a_1 by Lemma 1; hence the multiple shares that prime with every term). So the next multiple of R above a_n is admissible and lies in (a_n, a_n+R].

**New observation (conjecture, label as such).** If (a_i, a_j) is a counterexample to Lemma 4 (shares only large primes), then **a_j is NOT a multiple of R**. Proof sketch: if a_j = m·R, then a_j is divisible by every prime of a_1; by Lemma 1, a_i has a prime q ∈ P(a_1) ⊆ Q_R; q | R | a_j, so q | a_i and q | a_j — shared small prime, contradiction. So counterexample pairs require a_j NOT divisible by R. This NARROWS the counterexample search: a_j mod R ≠ 0.

**What it needs.** To close: show that if a_j mod R ≠ 0 and a_j shares only large primes with some a_i (i<j-1), the next multiple of R above a_{j-1} (call it M', which is admissible and ≤ a_{j-1}+R) lands strictly between a_{j-1} and a_j — contradicting greedy minimality of a_j. This requires: M' < a_j. We have M' ≥ a_j (a_j is the min admissible, M' is admissible). So M' ≥ a_j, i.e. M' = a_j (a_j mult of R — excluded) or M' > a_j. So in the counterexample case M' > a_j, no contradiction. **Route C narrows but does not close.**

**Where it likely breaks.** The "next multiple of R" is admissible but might land strictly above a_j (a_j is a smaller admissible integer not divisible by R). No contradiction from this engine alone. Needs a SECOND admissible integer in (a_{j-1}, a_j) — but the only universal one is the multiple of R, which is above a_j.

**Verdict: cheap partial result this round.** The observation "a_j mult of R ⟹ Lemma 4 holds for (a_i,a_j)" is a real lemma worth certifying into `lemmas/` — it handles a positive-fraction subcase for free. But it does not close the general case. Combine with Route A: the counterexample case is precisely "a_j mod R ≠ 0", which gives the descent a concrete starting constraint.

### Route D — Sieve density / Jacobsthal on the gap window

**What it would prove.** That every window (a_n, a_n+R] contains an admissible integer of a *specific* small-prime type, forcing the greedy min to share a small prime.

**What it needs.** Jacobsthal-style: the window has length R; integers coprime to a_1 (i.e., missing every prime of a_1) are sparse within it (the next multiple of R is the universal admissible anchor). For a counterexample pair (a_i,a_j) sharing only large primes, the integers in (a_{j-1}, a_j) must ALL be inadmissible — each is coprime to some a_k. Show this covering is impossible by density: the "bad" sets {m : gcd(m,a_k)=1} cannot cover a length-R interval once the small-prime types are accounted for.

**Where it likely breaks.** Density is too weak: the bad sets ARE large (each a_k rules out a 1/p fraction for each prime p|a_k, but a_k may have few small primes). Covering a length-R interval by such sets is plausible; Jacobsthal bounds the gap between integers coprime to a fixed modulus M by ~2^ω(M), which for M = ∏_{p≤R} p is exponential in π(R) — far larger than R. So the universal Jacobsthal bound does NOT force an admissible integer in every length-R window above and beyond what Lemma 2 already gives. The crux is sharper than generic Jacobsthal.

**Verdict: likely dead end this round.** Generic sieve density gives bounds too weak to close. A *targeted* sieve using the actual type family F (not all small primes) might work, but that's Route B in sieve clothing.

### Route E — Direct "free-rider dichotomy" via stabilized transversal

**What it would prove.** That after stabilization (n ≥ N), every term a_{n+1} has τ(a_{n+1}) ∈ H_∞ (the transversal family of F), i.e. τ(a_{n+1}) hits every type in F — equivalently Lemma 4 for pairs involving a_{n+1}.

**What it needs.** The stabilized transversal family H = {S ⊆ Q_R : S∩T ≠ ∅ ∀ T∈F} is fixed. The claim: τ(a_{n+1}) ∈ H for n ≥ N. The crude-reduced-type approach needs exactly this for its Step 7 (free-rider wall). The mechanism: a_{n+1} is admissible, so it shares *a* prime with every a_i; we need that prime to be SMALL. If the shared prime is large (q>R), it's a free-rider; we need to show a free-rider cannot be the unique connection to any earlier term.

**Where it likely breaks.** This IS the crux, restated in transversal language. No new engine; same wall.

**Verdict: restatement, not a new route.** Useful as the target for Routes A/C.

## Corpus hits

1. **aimo-0030** (number_theory, size-bounding-and-descent) — **THE central match.**
   - *Crux move:* "Strengthen a 'two special objects share some forbidden-class prime' statement to a 'they share an allowed-class prime' statement by minimal-counterexample descent: take the smallest violating pair and use a legal move out of an auxiliary blocked object to manufacture a strictly smaller violating pair."
   - *Why analogous:* The problem is LITERALLY "two good numbers share a prime" → strengthen to "share a small prime (≤k)". P6's Lemma 4 is "two terms share a prime" (greedy) → strengthen to "share a small prime (≤R)". Identical logical shape.
   - *P6 analogues of aimo-0030's three claims:*
     - Claim 1 (n good ⟹ multiples of n good) ↔ **multiples of an admissible number are admissible** (P6: ✓, this is Lemma 2's engine, ALREADY PROVED).
     - Claim 2 (rs bad ⟹ r²s bad) ↔ **rs inadmissible ⟹ r²s inadmissible** (P6: ✓, trivial — a_i coprime to r and to s ⟹ coprime to r² and s ⟹ coprime to r²s).
     - Claim 3 (p>k prime, n bad ⟹ np bad) ↔ **p>R prime, n inadmissible ⟹ np inadmissible** — THIS is the crux; aimo-0030 proves it by descent on a minimal counterexample, stripping the large prime. P6 has the analogues of Claims 1, 2 for free, but Claim 3's descent uses the game's "move" structure (n → x coprime, x good), which P6 lacks.
   - *Adaptability:* MEDIUM. The three-claim scaffold and the "strip to small-prime-only witness" spirit port; the descent's specific mechanics rely on the game-move structure that P6 does not have. The P6-native replacement for the "move" is the greedy's min-admissible rule — but the descent needs to manufacture a smaller COUNTEREXAMPLE PAIR, not just a smaller admissible integer. This gap is the open problem.
   - *Recommendation:* field as the skeleton of a NEW approach `crux-descent` (or as a revision of essential-monovariant), explicitly importing the "multiples of admissible are admissible" + "rs inadmissible ⟹ r²s inadmissible" lemmas (both free) and attempting the Claim-3 descent as the gap.

2. **aimo-0643** (number_theory, diophantine-and-factoring) — Jacobsthal/sieve-density.
   - *Crux move:* "Encode coprimality as 'lattice point in none of the bad sublattices p·Z²'; show a region isn't covered by summing ∑ 1/p² for small primes (converges to < 1) and bounding large-prime contributions separately by calibrating region size ~ log r."
   - *Adaptability:* LOW for the crux directly. The P6 window has length R (fixed), not a growing region; generic sieve density gives Jacobsthal bounds exponential in π(R), far larger than R. Could only help if combined with the specific type family F (Route B/D hybrid). Do not field as a standalone approach.
   - *Use:* cite as the source of the "bad sublattices don't cover" intuition, but the bounds are too weak for P6's window length.

3. **aimo-0799** (combinatorics, induction-and-construction) — cross-intersecting set families.
   - *Crux move:* "Force cross-intersection between two set families by a containment-vs-hitting relation on a shared block partition."
   - *Adaptability:* LOW. The block-partition mechanism (partition {1,…,n} into k blocks of size m; S = transversals of blocks, T = sets containing a full block) does not map to P6's prime-type setting. The abstract lesson ("two set families that must cross-intersect can be forced to do so by a shared structure") is mild moral support for Route B, but no concrete move.

No other corpus hits are genuinely analogous. The "intersecting family" combinatorics cruxes (aimo-0488 intervals, aimo-0799 block partition) are about geometric/set families with different structure. The number-theory descent cruxes (aimo-0031 denominator descent, aimo-0313 Vieta jumping, aimo-0813 addition-closed-set descent) are about Diophantine equations, not greedy sequences.

## Recommendation to outliner

**Field one new approach `crux-descent` (or revise `essential-monovariant` to absorb it)** whose skeleton is the aimo-0030 three-claim scaffold ported to P6:

1. **Lemmas (free, prove immediately):**
   - "Multiples of an admissible integer are admissible" (P6-Claim-1; already the engine of Lemma 2).
   - "rs inadmissible ⟹ r²s inadmissible" (P6-Claim-2; trivial).
   - **NEW partial result (conjecture, prove this round):** "If a_j is a multiple of R, then (a_i, a_j) satisfies Lemma 4 for every i<j." Proof: a_j mult of R ⟹ every prime of a_1 divides a_j; by Lemma 1 a_i has a prime q ∈ P(a_1) ⊆ Q_R; q | a_j; shared small prime. ✓ — this handles the "a_j ≡ 0 mod R" subcase for free. Certify into `lemmas/`.
   - **Corollary:** any counterexample to Lemma 4 has a_j mod R ≠ 0. This is the descent's starting constraint.

2. **The crux gap (P6-Claim-3):** "p>R prime, n inadmissible ⟹ np inadmissible." Attempt the aimo-0030 descent: given n inadmissible (witnessed by a_i coprime to n) and p>R prime with np ADMISSIBLE (counterexample), strip the large prime from the witness to manufacture a smaller counterexample. The P6-native "move" replacing aimo-0030's game move is the greedy minimality: a smaller admissible integer in (a_{j-1}, a_j) contradicts a_j's choice. Leave as [GAP] but with the three-claim scaffold and the new partial lemma as certified progress.

3. **Inherit the periodicity machinery** from `essential-monovariant` (Theorem, conditional on Lemma 4 — already proved). So `crux-descent` completes the whole problem iff its Claim-3 gap closes.

**Diversity note:** `crux-descent` is genuinely closer to `essential-monovariant` than to `crude-reduced-type` (both attack Lemma 4 directly, not the transversal-family stabilization). To avoid the single-gap trap, the outliner should consider `crux-descent` a **revision of essential-monovariant** (replacing its stalled "free-rider co-occurrence" induction with the aimo-0030 descent scaffold) rather than a fifth independent approach — UNLESS the builder can articulate a P6-native "strip" operation that differs structurally from essential-monovariant's failed induction (e.g., operating on the term's value rather than its type). If fielded as new, keep it the SOLE crux-attack slot and route the other builder slots to genuinely different framings (per the outline-reviewer's round-1 warning).

**Likely outcome this round:** the three free lemmas + the "a_j mult of R ⟹ Lemma 4" partial result certify as real progress (promote to `lemmas/`), narrowing the counterexample case to "a_j mod R ≠ 0". The Claim-3 descent gap likely stays open — it is the 9/10 crux and the aimo-0030 mechanics do not port verbatim. Honest target: **partial → partial with sharper gap**, not solved.

## Small-case / intuition notes (conjectures, NOT proofs)

- Lemma 4 verified for a_1 ∈ {6,10,15,35,77,105,1001}, 60–120 terms, all C(n,2) pairs — no counterexample. F pairwise-intersecting in every case.
- E (essential primes) stabilizes by n≈3–8 and never grows; E ⊆ Q_R in every case; max essential prime ≤ R always.
- F restricted to P(a_1) is **NOT** pairwise intersecting (types {3} and {5} coexist for a_1=15) — so the proof genuinely needs Q_R, not just P(a_1). The crude modulus L_0 = ∏_{p≤R} p is necessary, not just sufficient.
- Free-rider co-occurrence (essential-monovariant's observation) confirmed: for a_1=105, prime 317>R first appears in a_{497}=1902=2·3·317 (carries small primes 2,3); the candidate 5·7·317=11095 (which would share only 317 with 1902) is inadmissible — coprime to the {2,3}-type early terms. This is the empirical signature of Lemma 4 but NOT a proof.
- The "a_j mult of R" subcase is non-vacuous: in examples, a positive fraction of terms are multiples of R, and for those Lemma 4 is free. The hard case is terms with a_j mod R ≠ 0, which carry only a SUBSET of a_1's primes.
