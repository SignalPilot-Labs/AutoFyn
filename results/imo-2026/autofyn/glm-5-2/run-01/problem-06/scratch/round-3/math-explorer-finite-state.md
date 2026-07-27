## imo-2026-06  (finite-state lens)

**Framing scouted:** reduce a_n to a FINITE STATE directly — prove a_n eventually lives in a fixed finite residue system mod some M=M(a1), which would force P_ess finite and periodicity at once, WITHOUT first isolating M finite. The goal was to test whether this BYPASSES the wall.

### Bottom line
**The finite-state route does NOT bypass the wall; it reduces back to it.** The greedy's smallest-first pick depends on ENTERING primes (unbounded, e.g. 17, 29, 97, 181, 337 for various seeds), so no finite modulus M(a1) captures the decision state. Periodicity still requires M finite (= the wall). HOWEVER, the lens surfaced a genuinely new, empirically robust structural CONJECTURE (min(M)≤p*) that, if proven, closes γ's GAP-1 cleanly. Route dead for bypassing; one new lemma candidate harvested.

### Distinct openings (each a different attack the outliner could build)
1. **The min(M)≤p* structural lemma (NEW, strongest find).** CONJECTURE (280 seeds: 251 small + 29 large-p*, 0 violations): every minimal support M ever appearing in any M_n satisfies `min(M) ≤ p* := min(P(a_1))`. In every seed `max_n min(M_n_member) == p*` exactly. Mechanism intuition: the greedy's smallest-first pick always lands on a number carrying a prime ≤ p* (multiples of small primes are densest; a p*-rough pick would be beaten by a smoother valid candidate). CONSEQUENCE (conditional on the conjecture): the set `S_n = P_ess,n ∩ {primes ≤ p*}` is a transversal of M_n at every n (each M has an element in S_n), so `mtp(M_n) ≤ ∏ S_n ≤ R(a_1) := ∏{p prime : p ≤ p*}`, a FINITE function of a_1. This **closes γ's GAP-1** (mtp bounded) with an explicit bound R(a_1). Proof of the conjecture is itself the hard part (it is "the greedy never introduces a p*-rough minimal") — closely tied to the wall but a cleaner, sharper statement than "mtp bounded."
2. **mtp≤a_1 (unconditional gap bound, CONJECTURE).** 138 seeds (123 fast + 15 slow, no fallback triggered): `mtp(M_n) ≤ a_1` at EVERY step, hence `a_{n+1}-a_n ≤ a_1` for all n. Tighter empirically than the R(a_1) bound. max_gap == mtp_final in 100% of seeds (re-confirms γ's monovariant is sharp). This is G(a_1)=a_1, but PROVING mtp≤a_1 is essentially GAP-1 again (no structural proof found).
3. **All "slow" seeds eventually stabilize (no counterexample to the wall).** 30 seeds that did not stabilize in 200 terms (|M| transiently 40–84, |P_ess| up to 83) were run to 2000 terms: ALL stabilize — most freeze to a singleton {small prime} (e.g. a1=511=7·73: |M| peaks at 49 then collapses to {7}, maxgap=7; a1=867, 1587, 2047, 9251 similar), a few saturate at |M|=3–5 with small final P_ess (a1=2023→|M|=5 maxgap=14; a1=26071=29²·31→|M|=5 maxgap=62). NO seed with unbounded gap exists in the sample. The large-prime transient always resolves: large primes (97 for a1=1001, 181 for a1=8303, 337 for a1=19549) enter minimals {small, large} then get refined away when a pure power of the small co-prime appears. This refinement is exactly the wall mechanism.

### Why the finite-state route is blocked (killing evidence)
- **Large primes enter minimals transiently.** a1=1001: primes 23,73,47,37,41,79,43,83,53,89,29,59,61,97,31 each enter a minimal {2/7/11/13, large} and later leave; final M=[[7,11,13],[2,13],[2,7],[2,11]], mtp_final=14. a1=19549=113·173: prime 337 enters {2,23,337}; final P_ess={2,3,5,7,11,13,29,59,89,97,101,113,173} (≤109 except 173). The gap stays bounded (=mtp_final) throughout, BUT M_n ranges over families with large primes during the transient.
- **The greedy's smallest-first pick DEPENDS on entering/large primes.** Direct test (a1=175,2023,15341,19549): at the greedy's own pick, hitting every minimal via a prime ≤ p* FAILS in 266/399, 15/399, 176/399, 75/399 steps respectively — the pick hits some minimal only via a prime > p* (either another factor of a_1, or an entering prime like 17, 29, 97, 173). Hence the decision `a_{n+1}` is NOT determined by `a_n mod L` for any L built from primes ≤ p* (or even from P(a_1): entering primes exceed max P(a_1) too, e.g. 337 > 173 for a1=19549).
- **No finite modulus M(a_1) captures the state.** The state (a_n mod M, M_n) is infinite: M_n contains unbounded primes during the transient, and the greedy's pick depends on a_n mod q for those q. The (a_n mod L, M_n^small) "effective state" does NOT determine a_{n+1} (large-prime hits at small offsets j beat the small-prime hits). So the `aimo-0678` lcm-reduction template's load-bearing "bounded coordinate divides the reduction modulus" step has NO analogue: the bounded coordinate is the gap, but validity depends on the unbounded prime set.
- **Residue periodicity = post-stabilization (needs M finite).** a_n mod rad(a_1) does become periodic, but only AFTER M stabilizes, with possibly huge period T (a1=429 has T=908; a1=1001's period exceeds L=2·7·11·13=2002). Confirmed: short-period search returns None for most seeds not because non-periodic but because T is large (post-stabilization theorem). No EARLY residue stabilization before M-finiteness was found.

### Candidate technique(s)
- **Invariants & monovariants** (KB): the mtp monovariant (certified) + the new min(M)≤p* conjecture as a second monovariant-style bound on the family.
- **Pigeonhole/extremal** (KB): the min(M)≤p* conjecture is an extremal statement on minimal supports; a pigeonhole/smooth-number-covering proof (a p*-rough candidate is always beaten by a smoother valid one within the mtp window) is the natural attack.
- **Modular arithmetic / CRT** (KB) + **Three-gap/Steinhaus** (KB): the residue-set V mod L is governed by transversal residues; but this is the post-stabilization machinery (DONE, δ), not a bypass.
- KB entries: *Invariants & monovariants*, *Pigeonhole/extremal principle*, *Modular arithmetic CRT*, *Order of an element / Fermat-Euler* (eventual periodicity mod m).

### Cheap-kill candidates
- **mtp ≤ a_1** as an unconditional gap bound (CONJECTURE, 138 seeds): if a one-line structural argument shows `mtp(M_n) ≤ min(P(a_1))·(something)` or ≤ a_1, GAP-1 closes without the full min(M)≤p* conjecture. Worth the outliner attempting a direct proof. No proof found this round.
- **p* anchor (the min(M)≤p* conjecture itself)** is the cheapest structural kill: it is a single extremal statement whose proof would close GAP-1. The outliner should commission a focused proof attempt (pigeonhole/smooth-covering) as a rival approach.
- None of: parity, pure size/pigeonhole on |M|, injection, v_p/multiplicity gave a one-move kill in probing — the family is pairwise-intersecting so LLL/union bounds are vacuous (already known).

### Knowledge-base entries to use
- *Invariants & monovariants* (mtp monotone — already certified; min(M)≤p* would be a second).
- *Pigeonhole / extremal principle* (the min(M)≤p* attack; smooth-number density of multiples of small primes).
- *Modular arithmetic, CRT* + *Order of an element, Fermat/Euler* (the eventual-periodicity-mod-m fact, used by δ's post-stabilization theorem — already done).
- *Three-gap/Steinhaus* and *Kronecker/Weyl* — NOT applicable (the gap sequence is not a Kronecker-type rotation).

### Analogous past problems (cruxes)
- **aimo-0678** (NT, modular-arithmetic-and-CRT): crux = "form the sum s_n=a_n+b_n as invariant; in the divisibility regime a_n|b_n the sum freezes while a_n climbs by 1, giving a fixed target." Analogue: the mtp monovariant "freezes" (stabilizes) once bounded, and the min(M)≤p* conjecture would give the cap. BUT the aimo-0678 lcm-reduction "bounded coordinate divides the modulus" step has NO direct analogue here (the bounded coordinate is the gap, not a term value; the greedy depends on the unbounded prime family) — so the template does NOT transfer wholesale, only the "find the regime where a monovariant freezes" spirit does.
- **aimo-0728** (NT, modular-arithmetic-and-CRT): crux = "reduce a branching recurrence mod a small prime to show every term inherits a residue in {0,1} mod 3, bounding attainable residues." This is the closest finite-state crux in spirit (bound attainable residues via a small-prime invariant), but P6's "recurrence" is the greedy over an adaptive prime family, not a linear recurrence — the small-prime residue bound would BE the min(M)≤p* conjecture (primes ≤ p* always suffice to hit every minimal). Adaptation is non-trivial and is itself the wall.
- **aimo-0193 / aimo-0264** (combinatorics, invariants-and-monovariants): "prove a process terminates by exhibiting a strictly-increasing integer monovariant CAPPED by an invariant." This is the canonical termination-monovariant template; P6's mtp is the monotone quantity and min(M)≤p* (or mtp≤a_1) would be the cap. The cap is the wall.
No crux is a true match (P6's adaptive prime-family greedy is genuinely harder); the closest are the termination-monovariant cruxes and the small-prime-residue-bound crux (aimo-0728).

### Prior progress
- δ conditional theorem (M finite ⟹ periodicity): DONE, certified.
- α freeze regime: SOLVED end-to-end.
- γ mtp monovariant + global gap bound d_n≤mtp(M_n): certified, unconditional, sharp (max_gap==mtp_final confirmed on 138 seeds this round).
- This round's NEW contribution from the finite-state lens: the **min(M)≤p* conjecture** (280 seeds, 0 violations), which would close γ's GAP-1 with bound R(a_1)=∏{p≤min P(a_1)}; and the **mtp≤a_1** gap-bound conjecture (138 seeds). Neither proven; both are sharp empirical invariants the outliner can hand to a builder for a focused proof attempt.

### Dead ends (do not retry)
- **Finite-state bypass via "bounded gaps ⟹ a_n mod lcm(1..G) is finite-state ⟹ periodicity":** DEAD. The state (a_n mod L, M_n) is NOT finite because M_n contains unbounded entering primes during the transient, and the greedy's smallest-first pick depends on those primes (a_n mod q). Confirmed by direct test: the greedy hits minimals via primes > p* (and > max P(a_1)) at a large fraction of steps. GAP-3 stands.
- **"Only small primes enter minimals" as a LITERAL statement:** FALSE. Large primes (97, 181, 337) DO enter minimal supports {small, large} transiently. The correct statement is "only small primes PERSIST in the final M" — which is the wall (proving they all leave).
- **"Every minimal contains a prime ≤ G for small constant G (independent of a_1)":** the threshold is p*=min P(a_1), which can be large (113 for a1=19549). No universal small constant G works; the bound depends on a_1.
- **Residue-stabilization-before-M-stabilization:** not found. Residue periodicity coincides with M-stabilization (post-stabilization theorem); no early finite-state.

### Small-case / intuition notes (all CONJECTURE, evidence not proof)
- CONJECTURE: `mtp(M_n) ≤ a_1` for all n (138 seeds, 0 fallbacks). Implies `a_{n+1}-a_n ≤ a_1` unconditionally.
- CONJECTURE: `min(M) ≤ min(P(a_1))` for every minimal M ever (280 seeds incl. large-p* stress, 0 violations). Implies `mtp(M_n) ≤ R(a_1) = ∏_{p ≤ min P(a_1)} p`, closing GAP-1.
- CONJECTURE: max_gap == mtp_final (γ's monovariant is tight); 138 seeds.
- CONJECTURE: for a_1 = p·q (odd semiprime, p<q), mtp_final = 2·q in the close-prime regime, or 2·p in others; ratio mtp/a_1 → 0 as a_1 grows (extremal ratio 0.40 at a_1=15, dropping to 0.012 at a_1=19549).
- CONJECTURE: every seed eventually stabilizes (wall is TRUE); no counterexample in ~280 seeds. The freeze regime dominates for "lopsided" a_1 (one small prime factor); the saturated regime appears for "balanced" multi-prime a_1.
- The "all-large" minimals seen (e.g. {113,173} for a1=19549, {29,31} for a1=26071) are always exactly P(a_1) itself re-entering — never a {large, large} pair disjoint from P(a_1). This is consistent with min(M)≤p* but does not alone prove it.
