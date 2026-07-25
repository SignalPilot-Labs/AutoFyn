## imo-2026-06 — RE-PLAN (v2). Field of 3 rival approaches, all avoiding the refuted premise.

### Why the whole first field died (recorded, do not retry)
All three v1 approaches assumed "primes q > max(P) never change the greedy successor"
(as mod-M determinism / no-large-critical-prime / bounded memory). FALSE:
`a_1=385` → successor of `406` is `418 = 2·11·19`, beating `420`, because `19` is the
*sole* witness for the constraint of `399 = 3·7·19`. Large primes CAN be sole witnesses,
the memory window is unbounded, and `a_{n+1}` is NOT a function of `a_n mod M`.

### Two structural facts I verified this round that reshape everything
1. **"Recurrent primes" is the WRONG finite object — it is infinite.** For `a_1=105`
   (`T=58, L=210`), prime `11 ∤ 210` divides terms at ALL 58 phases → divides infinitely
   many terms. In general `q ∤ L ⇒ q | a_{j+kT}=a_j+kL` for one `k mod q`, so every prime
   ever appearing divides infinitely many terms. The ONLY finite object is `primes(L)`.
   Any approach targeting "primes dividing ∞ many terms" is dead on arrival.
2. **Periodicity is from `n=1` (pure, no transient)** in every stabilised case tested
   (105, 15, 45, 1155). The problem literally demands `∀n`, so a no-transient step is
   mandatory, not decorative.

### Free lemmas (correct, shared by all three — keep from v1's non-dead parts)
- Anchor: every term divisible by a prime of `P=primes(a_1)`.
- Gap bound: every multiple of `M=∏P` is admissible ⇒ `gap ≤ M`, `a_n=Θ(n)`.
- Distance–prime: `q|a_i, q|a_j ⇒ q ≤ |a_i−a_j|` (gcd | difference). Large shared
  primes force large index-distance — this is the new handle on large primes.

---

redundant-constraint-antichain: new
Target: ∃ T,L with a_{n+T}=a_n+L for all n≥1.
Technique: order-theoretic reduction to the antichain of minimal prime-supports →
  fixed periodic admissible set mod L → finite-state pigeonhole → reversibility.
Skeleton:
  1. Free lemmas.
  2. c admissible ⟺ c meets every ⊆-minimal support F_i (F_i⊇F_j makes i redundant).
  3. CRUX: the minimal-support antichain eventually uses only a finite prime set
     S=primes(L); a large-prime support {3,7,19} is DOMINATED by a later small-only
     support, never surviving as minimal in the stable regime.
  4. ⇒ admissible set = fixed residue-union U mod L=∏S; successor = min U above a_n.
  5. Pigeonhole on visited residues ⇒ eventual periodicity; period adds constant L.
  6. U fixed ⇒ successor map injective ⇒ bijection ⇒ periodicity from n=1.
Key lemmas: antichain reduction (support-inclusion domination); Crux-1 large supports
  get dominated (covering/gap forces a small-only support to recur); no-transient
  (fixed U ⇒ invertible map).
Open gaps: GAP-1 = finite prime alphabet of the antichain (the whole difficulty);
  GAP-2 = antichain stabilises to fixed U.
Cases: |S|=1 (T=1) vs |S|≥2.
Watch out: a large prime CAN be minimal for many steps (399's {3,7,19}); must show it
  is eventually dominated, not absent — this is where it differs from the dead premise.

anomaly-count-terminates: new
Target: same.
Technique: quantitative monovariant — define "anomaly" = step where a prime q>M is a
  sole witness lowering the successor; prove anomalies are FINITE; after the last one,
  mod-K determinism + finite-state pigeonhole + reversibility.
Skeleton:
  1. Free lemmas + small-prime confinement (p|L ⇒ p≤M).
  2. Anomaly defined via sole large witness; non-anomalous step ⇒ successor is a
     function of a_n mod K, K=∏_{p≤M}p (rescues mod-determinism as EVENTUAL).
  3. CRUX: anomalies finite. Density-0 from counting large-prime coincidences
     (Σ_{q>M} V/q), UPGRADED to finite by rigidity: a persistent sole-witness q would
     satisfy q|a_n and q|a_{n+T}=a_n+L ⇒ q|L ⇒ q≤M, contradiction — so no anomaly
     survives into the periodic regime; plus a strict monovariant to end the transient.
  4. After last anomaly ⇒ deterministic finite-state map ⇒ eventual periodicity.
  5. Injective ⇒ bijection ⇒ periodicity from n=1.
Key lemmas: confinement p|L⇒p≤M (recurs within bounded distance ⇒ distance–prime);
  anomaly finiteness (density-0 + q|L rigidity + monovariant); no-transient.
Open gaps: GAP-1 = anomalies finite (turning density-0 into an actual finite count is
  the honest hard point); GAP-2 = confinement p|L⇒p≤M.
Cases: single-prime lock; 385-type (anomalies occur early) vs 105-type (none, N_0=1).
Watch out: density 0 ≠ finiteness — must produce a strictly decreasing potential.

reversible-state-bijection: new (far-out framing, plateau-breaker)
Target: same.
Technique: dynamical reversibility (borrow aimo-0577): confine to a finite state
  space, show the one-step map is a BIJECTION with explicit inverse ⇒ pure periodicity
  from n=1 in one stroke (no pigeonhole+patch).
Skeleton:
  1. Free lemmas + L-rigidity (q∤L ⇒ q hits 1/q of each phase; finite object=primes(L)).
  2. State Σ_n = a_n mod L, augmented by a BOUNDED, invertible record of recently-
     introduced large primes (each pairs with a term within a bounded backward window
     by distance–prime, then is discharged).
  3. Forward map F on the finite augmented state Σ̂.
  4. CRUX-B: F injective — predecessor is the unique largest value having a_{n+1} as
     its greedy successor; the bounded large-prime record is popped in reverse.
  5. Injective finite self-map ⇒ bijection ⇒ every orbit a cycle ⇒ a_{n+T}=a_n+L ∀n≥1.
Key lemmas: L-rigidity; Crux-A finite core S⊆{p≤M}, L=∏S; Crux-B explicit inverse
  (global-smallest-search predecessor + reversible large-prime pops via distance–prime).
Open gaps: GAP-A = finite core/modulus L exists with S⊆{p≤M}; GAP-B = backward-
  determinism / injectivity incl. reversibility of the bounded large-prime record.
Cases: L prime (T=1); multi-prime; steps with an active large prime (must be a
  reversible decoration popped in a bounded window, NOT part of the core cycle).
Watch out: the augmented state MUST be proven finite (the reviewer's exact refutation
  point — no smuggled "bounded memory"); the bound comes from distance–prime + bounded
  gaps and must be earned. Payoff: injectivity gives from-n=1 periodicity for free.

---

### Diversity check (why these three do NOT share one wall)
Distinct MECHANISMS confronting large primes three different ways:
- antichain: order-theoretic REDUNDANCY (large supports dominated by small ones).
- anomaly-count: analytic SPARSITY + rigidity monovariant (large shortcuts are finite).
- reversible-bijection: dynamical RIGIDITY (a prime in the core divides L, so is small)
  + explicit inverse — and it is the only one that gets from-n=1 periodicity for free.
They share only the three correct free lemmas and the common target. Their cruxes are
independent: GAP-1 (domination) vs GAP-1 (finiteness-of-anomalies) vs GAP-B (inverse).
If one crux falls the others are not automatically doomed.

### Honest status
None of the three cruxes is closed — this is a rating-9 problem and the crux IS the
problem. What each approach delivers is a correct, refutation-proof *reduction* of the
whole problem to one clearly-stated hard lemma, with the free structural lemmas proved.
The reversible-bijection route is the highest-risk / highest-reward (novel inverse) and
is the deliberate far-from-field plateau-breaker; the anomaly-count route has the most
concrete crux (a monovariant to find); the antichain route has the cleanest reduction.
All are worth building toward — a builder should push the free lemmas to full rigor and
attack the named crux; partial progress on any crux is real progress.

build set: redundant-constraint-antichain, anomaly-count-terminates, reversible-state-bijection
(All three survive as valid population members — each is a complete end-to-end attempt with
proved free lemmas and one honestly-stated open crux, none resting on the refuted premise.
Uncertain: every crux is open; the reviewer should rank by which reduction looks most
attackable, not expect a closed proof this round.)
