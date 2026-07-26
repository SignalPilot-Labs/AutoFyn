## imo-2026-06

Round 4 = 3rd round stalled on Gap A (finiteness of governing primes / B_∞ L-periodic). All three round-4 explorers (substitution/morphism, ergodic window-state, increment-induction) scouted DEAD — they collapse to Gap A. The wall now resists ~10 mechanisms: strip/cofactor, monovariant (MT-frontier, aimo-0134), density/covering-capacity, CRT-lift (aimo-0231), free-rider-type, modular residue-statistic, substitution/morphic, ergodic window-state, increment-window automaton, pure statics (syndetic-negative). The dispatch requires CHALLENGING THE GAP with a genuinely-new door, not a technique-variant.

I probed two candidate new doors computationally this round before deciding the field:
- **p-adic per-prime boundedness / periodicity** — DEAD ON ARRIVAL (verified a_1=385, 6000 terms): v_2(a_n) reaches 13 (not bounded by a constant, grows like log_p a_n); v_p patterns are NOT periodic with the main period T because L is squarefree (v_p(L) ≤ 1, so v_p(a_n + L) ≠ v_p(a_n) when v_p(a_n) ≥ 2). The p-adic boundedness door is closed; do NOT open it.
- **Minimal-criminal cofactor structure** — verified a_1=15, q=3: cofactors k_i = a_n/q have prime factors up to 199 (transient primes in a_n), so "k_i is P_1-smooth" is EMPIRICALLY FALSE. The Schur-style premise "k_i's prime set is fixed-finite" fails literally; the rescue requires separating TRANSIENT primes (each dies) from GOVERNING primes (≤ M_1), which is itself a non-cofactor finiteness claim — possibly as hard as Gap A. Honest: the contradiction is NOT pinned.

Crux corpus re-search (my own, broader subtopics: greedy sequences, Frobenius, Sylow, covering systems, weight/order, confinement, self-map, invariant set): the only confinement crux with the right shape is `aimo-0577` (IMO-SL 2022 N3, already the certified endgame analogue — its confinement step relies on a SINGLE modulus with gcd(a,d)=1; our greedy couples all P_1 primes simultaneously, so the complete-residue-system argument does NOT port — re-confirmed). `aimo-0727` (Netherlands) is a Schur-style "bounded cofactor ⇒ finite prime set ⇒ contradiction with infinite-prime-divisors" — structurally the right shape for the minimal-criminal contradiction, but in the WRONG direction (it proves a cofactor UNBOUNDED; we want to prove the cofactor BOUNDED). No crux supplies the missing confinement/finiteness bound. Honest verdict: no portable crux beyond `aimo-0577`'s endgame-structural match (already certified).

### Field of approaches (round 4)

**minimal-criminal-schur-contradiction**: NEW
Target: prove the whole theorem (a_{n+T} = a_n + L) end to end. Distinctive route: attack Gap A by contradiction via minimal-criminal on the smallest governing prime q > M_1 = rad(a_1), using only the local walk a_n mod q (steps ≤ M_1 < q, forced d_n at q-multiple steps) + greedy order + Schur-style cofactor-prime-finiteness (crux `aimo-0727`) — NOT the cofactor bound (circular, certified dead). Once Gap A closed, certified endgame (`cyclic-successor-bijection`, `greedy-equals-cyclic-successor`) closes the theorem.
Technique: minimal-criminal contradiction + Schur/aimo-0727 "finitely many prime divisors ⇒ sequence trivial" + local walk mod q.
Skeleton:
  1. Assume Gap A false; let q be the smallest governing prime > M_1 — by well-ordering.
  2. All primes in (M_1, q) are transient (not governing) — by minimality of q + governing/transient distinction.
  3. q | a_n for infinitely many n (q governing) — by `binfinity-divisibility-progression-structure`.
  4. Local walk: at each q-multiple term a_{n+1}, d_n = q - (a_n mod q) is FORCED, a_n mod q ∈ {q-M_1,…,q-1}; between consecutive q-multiples partial sums avoid 0 mod q, spacing ≥ ⌈q/M_1⌉ — by `linchpin-and-gap-bound` + arithmetic.
  5. Cofactor-transversal: for b_i = k_i q to be admissible, primefactors(k_i) transverses the prior non-q-multiple supports — by greedy admissibility + gcd.
  6. Linchpin: P_1 alone always transverses, so k_i COULD be P_1-smooth — by `linchpin-and-gap-bound`.
  7. THE CONTRADICTION (GAP, unproved): Candidate A (Schur) — if k_i's prime set is eventually fixed-finite (⊆ G ⊆ primes ≤ M_1, after transient primes die), Schur/aimo-0727 forces (k_i) trivial, contradicting k_i unbounded. The open sub-step: prove every TRANSIENT prime stops appearing in k_i after finitely many q-multiples — WITHOUT the cofactor bound. Candidate B (local-walk finite-state) — weak; the walk mod q is not a closed finite state. — by Schur + greedy dynamics.
  8. Endgame (certified, conditional on Step 7): no governing q > M_1 ⇒ Gap A closed ⇒ B_∞ L-periodic ⇒ a_{n+T} = a_n + L from n=1 — by `cyclic-successor-bijection` + `greedy-equals-cyclic-successor`.
Key lemmas (claim + mechanism):
  - No governing prime q > M_1 exists — because (Candidate A) transient primes die, leaving k_i's prime set eventually ⊆ G ≤ M_1 (fixed-finite), whence Schur forces k_i trivial, contradicting q governing. THE transient-death step is the unproved crux; must NOT use the cofactor bound.
  - Local walk mod q has forced d_n at q-multiple steps — because d_n ≤ M_1 < q and a_n ≡ -d_n (mod q).
  - Cofactor-transversal structure — because k_i q admissible ⇒ every prior non-q-multiple a_j shares a prime with k_i (gcd).
Open gaps: Step 7 (THE CONTRADICTION) unproved. The Schur premise "k_i's prime set eventually fixed-finite" requires transient-prime death, itself a non-cofactor finiteness claim possibly as hard as Gap A. Builder must pin the transient-death step with a greedy-dynamic argument, OR find a different contradiction, OR certify the framing dead with a negative lemma explaining why no Schur-style contradiction works.
Cases to cover: LOCK (certified `lock-lemma`); |P_1|=2 NON-LOCK (smallest base — extra levers `two-entry-lemma`, `P1-minimal-transversal-lemma`); |P_1|≥3 NON-LOCK (general).
Watch out for: do NOT re-derive the cofactor bound (circular, dead); the Schur premise is empirically FALSE as stated (k_i has large transient prime factors, verified a_1=15 q=3: primes up to 199) — the rescue must separate transient from governing primes; the walk mod q is NOT a closed finite state (do not argue finite-state ⇒ periodic mod q); `syndetic-divisible-closed-not-periodic` guardrail (contradiction must use greedy-dynamics, not pure statics).

**primal-minimal-support-stabilization**: NEW
Target: prove the whole theorem end to end. Distinctive route: attack Gap A in the PRIMAL — prove the inclusion-minimal term-supports of {S(a_i)} stabilize to a finite antichain with primes ≤ M_1, using ONLY the greedy rule (smallest admissible next term), NOT the cofactor bound. Honest: EQUIVALENT to Gap A (primal = dual, per round-4 increment-induction explorer); the hope is the primal admits a direct greedy-minimality argument the dual MT does not. EXPLICIT FALLBACK: if it founders, certify a negative lemma "primal ≡ Gap A" fencing off future primal retries.
Technique: direct greedy-minimality on the primal antichain (NOT cofactor-bound descent, NOT pure statics, NOT aimo-0134 monovariant).
Skeleton:
  1. Define MS_n = inclusion-minimal term-supports of {S(a_i): i≤n}; B_n = ∩_{S∈MS_n} ∪_{p∈S} pZ — by set-inclusion duality (S redundant iff ⊆ another).
  2. MS_n evolves under adding terms (can add AND remove); family of distinct supports ever appearing is well-defined — by `mt-depends-on-set-system` (dual).
  3. New minimal support ms enters MS_{n+1} iff ms incomparable to all current minimals; the carrying term a_{n+1}=m is the SMALLEST m > a_n with S(m) hitting every current minimal — by greedy rule + incomparability.
  4. GREEDY-MINIMALITY FORCES ms's PRIMES ≤ M_1 (THE LOAD-BEARING LEMMA, GAP): a_{n+1}=a_n+d_n ≤ a_n+M_1; for p ∈ ms with p > M_1, p | m and p > M_1 ≥ d_n so p ∤ d_n; [THE GAP: complete the argument to force p ≤ M_1 without cofactor-bound circularity]. Candidate sub-step: a prime q > M_1 dividing m requires m ≡ 0 (mod q) with m in a window [a_n+1, a_n+M_1] of size M_1 < q ⇒ at most ONE q-multiple in the window ⇒ the q-multiple is uniquely determined by a_n mod q; greedy-minimality then asks whether that unique q-multiple is ADMISSIBLE (transversal structure, link to `minimal-criminal-schur-contradiction` Step 5) AND smallest; if not, greedy picks a smaller m avoiding q. PIN THIS. — by `linchpin-and-gap-bound` + greedy order.
  5. MS_∞ stabilizes finite with primes ≤ M_1 (conditional on Step 4): union of primes ⊆ {primes ≤ M_1} finite; MS_∞ antichain in finite Boolean lattice ⇒ finite — by Step 4 + finiteness.
  6. B_∞ L-periodic: MS_∞ finite with primes ⊆ G ⊆ primes ≤ M_1; B_∞ = ∪_{T∈MT} rad(T)Z finite union with rad(T) | L — by `binfinity-divisibility-progression-structure` + Step 5.
  7. Endgame (certified): a_{n+T} = a_n + L from n=1 — by `cyclic-successor-bijection` + `greedy-equals-cyclic-successor`.
Key lemmas (claim + mechanism):
  - Every prime entering a new minimal support ms is ≤ M_1 — because a_{n+1} = a_n + d_n is the smallest admissible m > a_n with d_n ≤ M_1, and [THE GAP: greedy-minimality forces ms's primes ≤ M_1]. Mechanism must be greedy-dynamic.
  - MS_∞ stabilizes finitely — because all its primes ≤ M_1 (finite) and it is an antichain in the finite Boolean lattice.
  - B_∞ L-periodic ⇐ MS_∞ finite with bounded primes — by `binfinity-divisibility-progression-structure`.
Open gaps: Step 4 (THE LOAD-BEARING LEMMA) unproved. Skeptic's note (round-4 explorer): the incomparable condition is PRECISELY where a new prime q > M_1 would enter, and bounding that prime's cofactor IS the circular step certified dead for witness-density / crt-period-lifting. Builder must exhibit a greedy-dynamic ingredient the cofactor-bound proofs LACKED.
Cases to cover: LOCK (certified); |P_1|=2 NON-LOCK (smallest, 2–3 supports — easiest first); |P_1|≥3 NON-LOCK (general).
Watch out for: do NOT present as a BYPASS of Gap A (it is EQUIVALENT); do NOT re-derive the cofactor bound (dead); `syndetic-divisible-closed-not-periodic` guardrail; EXPLICIT FALLBACK — if Step 4 founders, certify "primal ≡ Gap A" negative lemma and declare the wall impenetrable with current framings.

**p1-equals-2-direct**: ADVANCE
Target: shrink the theorem to |P_1| ≥ 3 by solving |P_1| = 2 NON-LOCK directly (the smallest open base case). Distinctive route: combine the certified |P_1|=2 lemmas (`two-entry-lemma`: 2 enters at n=2; `P1-minimal-transversal-lemma`: P_1 ∈ MT(F_∞) for |P_1|=2 NON-LOCK) with the minimal-criminal + Schur contradiction SPECIALIZED to |P_1| = 2 (where the structure is tightest: M_1 = p·q, two small primes, 2-density lever — though the 2-density mechanism itself is REFUTED for bounding cofactor, the |P_1|=2 setting is the smallest place to crack the cofactor bound r ≤ M_1).
Technique: minimal-criminal contradiction specialized to |P_1| = 2 (the `minimal-criminal-schur-contradiction` skeleton in the |P_1|=2 lens) + certified |P_1|=2 lemmas as foundation.
Skeleton (build on the certified foundation already in `p1-equals-2-direct.md`):
  1. Foundation (CERTIFIED): `two-entry-lemma` (2 enters at n=2 for |P_1|=2 NON-LOCK) + `P1-minimal-transversal-lemma` (both p, q ∈ P_1 are governing) — verified 8 NON-LOCK cases.
  2. Assume a governing prime r > M_1 = p·q exists (Gap A specialized, false). Let r be smallest such. — by well-ordering.
  3. Cofactor-transversal + local walk mod r (specialized to |P_1|=2): at each r-multiple term, d_n = r - (a_n mod r) forced; cofactor k_i = a_{n+1}/r; primefactors(k_i) transverses prior non-r-multiple supports. With |P_1|=2, P_1 = {p, q} is a 2-element transversal always available (linchpin). — by `linchpin-and-gap-bound` + arithmetic.
  4. THE CONTRADICTION (GAP): in the |P_1|=2 setting, the transversal structure is tighter — k_i must hit prior non-r-multiple supports using primes from {p, q} ∪ {transient primes in (M_1, r)} ∪ {r-multiple cofactor primes}. Schur-style: if k_i's prime set eventually ⊆ {p, q} (after transients die), (k_i) is p·q-smooth ⇒ grows sub-linearly in some sense ⇒ contradicts r governing (k_i unbounded). PIN THE TRANSIENT-DEATH STEP for |P_1|=2. — by Schur + greedy dynamics (same crux as `minimal-criminal-schur-contradiction` Step 7, specialized).
  5. Endgame (certified): no governing r > M_1 ⇒ Gap A closed for |P_1|=2 ⇒ a_{n+T} = a_n + L from n=1. — by certified endgame.
Key lemmas: reuse `two-entry-lemma`, `P1-minimal-transversal-lemma` (both certified). New load-bearing claim: the transient-death step (Step 4) in the |P_1|=2 setting.
Open gaps: Step 4 (the |P_1|=2-specialized contradiction) unproved. Even an UNCONDITIONAL |P_1|=2 solve shrinks the theorem (to |P_1| ≥ 3) — partial progress either way.
Cases to cover: |P_1| = 2 LOCK (certified `lock-lemma`); |P_1| = 2 NON-LOCK (the target).
Watch out for: the 2-density mechanism is REFUTED for bounding cofactor (a_1=15: a_9=45 odd, v_2 fluctuates {0..5}); do NOT revive it. The cofactor bound r ≤ M_1 is the open wall. Link this attempt to `minimal-criminal-schur-contradiction` Step 7 — they share the transient-death crux; if one cracks it, both benefit.

### Retirements / reclassifications (this round)

- **integer-monovariant-transfer**: RETIRE (was RETHINK, round 3). The `aimo-0134` mechanism is certified absent (constant gap bound, no shrinking range; `aimo-0134-obstruction`). Keep the certified sub-lemmas `block-index-advance` + `aimo-0134-obstruction` (negative) in the shared cache; do not re-attempt the aimo-0134 integer-monovariant template.
- **growing-modulus-descent, witness-density-recurrence, free-rider-type-replacement**: already retired (rounds 2–3); keep their negative lemmas (`monovariant-non-monotonicity`, `lemma-C-strip-no-go`, `gap-f-refuted`) certified in the cache.
- **transversal-saturation, prime-power-dichotomy, crt-period-lifting**: KEEP AS LEMMA SOURCES (not built this round). Their certified foundation/endgame/LOCK/dichotomy lemmas are importable by the two new approaches. The strip (aimo-0030) and the CRT-lift cofactor induction are dead — do NOT re-attempt. Mark stale-to-advance.

### No COPY recommended
No live approach has TWO clearly-viable gap-fills for the same gap. `p1-equals-2-direct` shares its crux (transient-death) with `minimal-criminal-schur-contradiction`; they are better kept as two distinct slugs (one base-case, one general) than copied, since the |P_1|=2 specialization is genuinely different in leverage.

### Candid assessment — is a breakthrough reachable this round?

**No — I do NOT believe a breakthrough is reachable this round, and the wall is likely genuinely impenetrable with the current arsenal of framings.** Concretely:
- The p-adic door (the dispatch's suggested (A)) is DEAD ON ARRIVAL (verified: v_p unbounded, not periodic with T).
- The minimal-criminal + Schur contradiction (the dispatch's suggested (A)) is genuinely new and the most promising door, BUT I could NOT pin the contradiction at the outline level. The Schur premise "cofactor k_i's prime set is fixed-finite" is EMPIRICALLY FALSE (k_i has transient primes up to 199 for a_1=15, q=3); the rescue requires proving transient primes DIE (stop appearing in k_i), which is itself a non-cofactor finiteness claim possibly equivalent to Gap A.
- The primal minimal-support stabilization (the dispatch's (B), the strongest rephrasing) is EQUIVALENT to Gap A by the explorer's own verdict; the hope (a greedy-minimality argument available in the primal but not the dual) is speculative, and the skeptic's note is that the incomparability condition is PRECISELY where the cofactor-bound circularity re-enters.
- No crux in the corpus (re-searched broadly) supplies the missing confinement/finiteness bound; `aimo-0577`'s confinement step requires a single modulus with gcd(a,d)=1 (absent here); `aimo-0727`'s Schur move is in the wrong direction (proves unboundedness).

The two new approaches are put up NOT because I expect them to solve the problem, but because (i) the stall rule requires challenging the gap with genuinely-new framings, and (ii) EACH has an explicit fallback that, if it founders, CERTIFIES A NEW NEGATIVE LEMMA fencing off the framing — sharpening the wall's characterization for future rounds. Even a non-solve that adds 2 negative lemmas (primal ≡ Gap A; Schur-premise-fails-via-transient-primes) is genuine progress on a problem where 10+ mechanisms are already dead.

If both new approaches founder AND `p1-equals-2-direct` does not crack |P_1|=2, the honest next-round recommendation is to declare the wall impenetrable with olympiad-accessible framings and consider whether the problem requires a genuinely-new olympiad idea not yet in our arsenal (or whether the empirical conjecture q ≤ M_1 = rad(a_1) — 100+ cases, 0 failures — admits a proof via a heavy/analytic mechanism beyond olympiad scope, e.g. a deep sieve or model-theoretic transfer).

build set: minimal-criminal-schur-contradiction, primal-minimal-support-stabilization, p1-equals-2-direct
