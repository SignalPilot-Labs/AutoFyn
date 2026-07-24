## imo-2026-06

Round 1, empty population. Three NEW rival approaches, all attacking the exact claim (∃T,L: a_{n+T}=a_n+L for every n≥1). All three share ONE deep crux — **only finitely many primes are ever load-bearing (essential)** — which is honest: this problem has essentially one hard nucleus. They are kept far apart in (i) overall route/framing and (ii) how they deliver EXACTNESS (no pre-period), which is the second, mandatory subtlety. I flag the shared finiteness gap explicitly so the reviewer can judge; the diversity is in the framing and the exactness mechanism, per the brief.

Cheap structural kill established for ALL approaches (no gap): **every multiple of R:=rad(a_1) exceeding a_n is admissible** — because each term a_i (i≥2) shares a prime with a_1, so a multiple of R (divisible by all of supp(a_1)) meets every prior term. Gives a_{n+1}-a_n ≤ R and a_n=Θ(n) with a one-line argument. Numerically de-risked: exact periodicity from n=1 confirmed (a_1=15→(T,L)=(8,30); 105→(58,210); 143→(64,858=2·3·11·13); 65→(58,390=2·3·5·13)) — note recruited primes 2,3 ∉ supp(a_1), and L is a product of a finite prime set = the essential set S.

---

admissible-set-periodicity: new  [PRIMARY — cleanest; exactness for free]
Target: ∃T,L with a_{n+T}=a_n+L for every n≥1.
Technique: static reformulation. A := {x>1 : gcd(x,a_i)>1 ∀i}. Show (a_n) = increasing enumeration of A∩[a_1,∞), and A∩[a_1,∞) is EXACTLY periodic mod L=∏S for a finite essential prime set S. Enumeration of an exactly-periodic set has exactly-periodic differences ⇒ result for all n≥1, no pre-period. CRT + hitting-set algebra.
Skeleton:
  1. Pairwise gcd(a_m,a_n)>1 (defining condition, symmetric) ⇒ every a_n∈A.
  2. a_{n+1}=min(A∩(a_n,∞)): greedy-least-satisfying-finite-condition = least in A, since A⊆{finite condition} and all terms ∈A. ⇒ sequence enumerates A∩[a_1,∞).
  3. Multiples of R∈A ⇒ gaps ≤R, a_n=Θ(n). [cheap kill]
  4. [CRUX] ∃ finite S⊇supp(a_1): A∩[a_1,∞)=A_S∩[a_1,∞), A_S={x:∀i, x hits S∩supp(a_i)}.
  5. A_S = {x: hits every set of the finite family 𝒯={S∩supp(a_i)}} depends only on x mod L=∏S ⇒ A_S exactly L-periodic (CRT).
  6. Increasing enumeration of exactly-L-periodic A∩[a_1,∞) ⇒ a_{n+T}=a_n+L, T=|A∩[a_1,a_1+L)|, for every n≥1. ∎
Key lemmas:
  - Enumeration lemma — because greedy min over the finite condition coincides with min over A (all terms lie in A, A is stronger).
  - Bounded gaps — because multiples of rad(a_1) hit every prior term (each shares a prime with a_1).
  - CRUX finiteness — a prime p is essential if some x∈A connects to some a_i ONLY via p; both x,a_i are terms (∈A) divisible by p; by a_n=Θ(n), p divides ≤O(window/p) terms; Σ over large p converges (aimo-0447 interval counting) ⇒ finitely many essential primes ⇒ A=A_S.
Open gaps: Step 4/finiteness (the whole difficulty); Step 2 induction (minor).
Cases to cover: none (uniform).
Watch out for: exactness must reach DOWN to a_1 (Steps 4–5 periodic from a_1, not just tail) — eventual periodicity is insufficient and would falsify the claim; S ≠ supp(a_1) (recruited primes 2,3); L may exceed the tail minimal period.

---

finite-state-reversible: new  [dynamical; distinct EXACTNESS mechanism]
Target: same exact claim.
Technique: model the sequence as the orbit of a deterministic map Φ on a FINITE state (a_n mod L + a bounded window of recent S-prime patterns). Pigeonhole ⇒ eventual periodicity; then prove Φ is a BIJECTION (process reversible) ⇒ purely periodic from n=1 (aimo-0514). Exactness via reversibility — a different wall from admissible-set-periodicity's static periodicity.
Skeleton:
  1. Bounded gaps (multiples of R). 
  2. [GAP A] admissibility of x∈(a_n,a_n+R] decided by a BOUNDED window i∈[n-W,n]; old constraints auto-covered by a later term's S-pattern.
  3. [GAP B] finite state σ_n=(a_n mod L, window S-patterns); σ_{n+1}=Φ(σ_n) deterministic, finite space.
  4. Pigeonhole ⇒ eventual periodicity of gaps.
  5. [GAP C] Φ injective (back-map: largest admissible residue below a_{n+1} on the shifted window) ⇒ bijection ⇒ purely periodic from n=1.
Key lemmas: bounded gaps; finite S (SHARED crux with the other two — this route diversifies on EXACTNESS not finiteness); reversibility ⇒ exact (aimo-0514 bijective finite-state map has purely periodic orbits).
Open gaps: GAP D finite S (shared); GAP A bounded window; GAP B state well-defined; GAP C reversibility (this route's distinctive contribution).
Cases to cover: none.
Watch out for: "a_n mod L" alone is NOT a sufficient state (need the window); do not stop at eventual periodicity (Step 5 mandatory); reversibility valid only on the stabilized window (order lemmas after finite S/W).

---

essential-prime-counting: new  [counting-spine; attacks the crux head-on]
Target: same exact claim.
Technique: make the finiteness crux the headline, proved by an explicit sieve/interval-occupancy bound (aimo-0447): a prime p occupies ≤⌈W/p⌉ slots of a length-W window; Σ1/p^2 converges ⇒ only finitely many primes are ever sole connectors. Then a short CRT covering-system argument gives exact periodicity.
Skeleton:
  1. Bounded gaps ⇒ first N terms in [a_1,a_1+NR], a_n=Θ(n).
  2. Split primes small(≤P)/large(>P), P≈c·R.
  3. [CRUX] large primes are sole connectors only finitely often (counting Σ over large p) ⇒ essential set S finite.
  4. Admissibility ⇔ hit fixed finite family 𝒯={S∩supp(a_i)} ⇒ depends on x mod L=∏S.
  5. Exactly-periodic compatible set (down to a_1, using S over all of [a_1,∞)) ⇒ a_{n+T}=a_n+L for every n≥1.
Key lemmas: linear growth; CRUX counting bound (aimo-0447); covering⇒exact periodicity (CRT).
Open gaps: Step 3 counting (the deep crux, here explicit); Step 5 exact-upgrade needs the near-start exceptional primes finite (from Step 3 on all of [a_1,∞)).
Cases to cover: small/large prime threshold split.
Watch out for: rigor of the summation and choice of P; must rule out greedy exploiting a large prime to undercut a small-prime candidate; include near-a_1 essential primes (13 for a_1=143) so L' is the full essential product.

---

Note to reviewer: the three approaches share the "finitely many essential primes" nucleus. This is deliberate — it is the genuine heart of this IMO P6 and worth two-to-three independent attacks (structural set algebra, dynamical reversibility, and explicit counting). They diverge in framing and, critically, in the EXACTNESS-from-n=1 mechanism (static periodic set vs finite-state bijection vs covering-system-down-to-a_1). Recommend building admissible-set-periodicity first (shortest path, exactness free) and essential-prime-counting in parallel (supplies the counting lemma the other two can import as a shared lemma once certified).

build set: admissible-set-periodicity, essential-prime-counting, finite-state-reversible
