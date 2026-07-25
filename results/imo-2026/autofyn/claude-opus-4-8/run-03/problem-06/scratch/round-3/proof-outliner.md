## imo-2026-06

Field of 3, kept far apart in framing. All three now read the greedy CHOICES `a_n`
(the axis the certified Obstruction Lemma demands), but via three *disjoint* mechanisms
and even different top-level targets, so they do not share a gap:
- **order-theory / size-bound** (antichain) — target `q ≤ K·M` window formation → Π finite.
- **extremal-descent-on-VALUES / cycle-pin** (value-stream-double-freeze) — target gap-word
  periodicity directly, Π-finite as by-product.
- **recruitment-descent-on-COMPANIONS** (monovariant-witness-descent) — target Π finite by
  counting distinct pending small companions.
Shared reduction (all certified, all three inherit): whole problem ⇔ Π finite; no-transient
gives `a_{n+1}=s(a_n)` from n=1; endgame gives `T=|ρ(A)|, L=∏Π`. E1/E2/E3, L1–L4, Lemma B free.

---

redundant-constraint-antichain: advance
Target: ∃ T,L with a_{n+T}=a_n+L ∀n≥1 (the whole theorem; complete given the Crux).
Technique: order-theoretic transversal reduction (§1–§5 complete) + Early-Recruitment-Window
  choice-reading closure of §9.4, reading which terms actually FORM via E1.
Skeleton (new part, §10):
  1. Replace size bound "q≤a₁" by the window target (ERW): every q∈Π divides a term
     ≤ a₁+K·M for an a₁-computable K — by finiteness of [a₁,a₁+K·M] ⇒ Π finite ⇒ theorem.
  2. Witness-pair localization: E3 gives closest realized pair (t,t') sharing only q, q≤|t−t'|;
     reduce to |t−t'|≤K·M — by E1 (terms = A∩[a₁,∞), q-multiples recur), take smallest realizers.
  3. First-formation bound: least m≥a₁ with support-exactly-B is a term (E2 realize + E1),
     m<a₁+∏B — a squarefree multiple occurs within a gap-bound window.
Key lemmas (claim + mechanism):
  - ERW window K exists — because a large ∏(G) forces its private witness far, and E1 would then
    have realized a smaller-support term in between, violating ⊆-minimality (loop-closure = the gap).
  - q≤|t−t'|≤K·M with K≈2 (NOT K=1) — L3+E3; honest: 19∈Π at a₁=375 needs K≥2 since 19>M=15.
Open gaps: the uniform window constant K (§9.4 restated as |closest witness pair|≤K·M) — the
  §8.4 per-window-independence fact, now aimed at FORMATION TIME not alphabet size.
Cases to cover: |P|=1 prime-power (Π={p}, trivial); |P|≥2 general; verify vs 105→T=58,L=210.
Watch out for: do NOT bound q by M=rad(a₁) (refuted, 19>15); state K≈2 honestly; do NOT use naive
  "minimality forces small q" (explorer S1: order adds nothing beyond E1 — the lever is formation
  time via E1, not pre-emption); track domination per small-companion-set S, not per prime (S3).

---

value-stream-double-freeze: new
Target: ∃ T,L with a_{n+T}=a_n+L ∀n≥1 (the whole theorem, targeted DIRECTLY — bypasses "Π finite").
Technique: aimo-0678 two-stage well-ordering freeze transplanted onto the chosen VALUES a_n:
  Stage-1 value monovariant freezes; Stage-2 finer invariant exactly constant post-freeze ⇒ the
  bounded-alphabet gap-word d_n=a_{n+1}−a_n is eventually periodic ⇒ linear-shift periodicity.
Skeleton:
  1. Reduce theorem to gap-word periodicity: (d_n) eventually periodic (period T, sum L) ⇒
     a_{n+T}=a_n+L; no-transient upgrades eventual⇒all-n — by telescoping + certified fixed-successor.
  2. Stage 1: freeze a value statistic w_n (seed = certified Lemma B max-gap Γ*, a genuine
     finite-time freeze) — by well-ordering of a bounded monotone integer sequence.
  3. Stage 2: window-state W_n=(a_n mod M ; 𝒮_n active supports binding in (a_n,a_n+Γ*]) ranges over
     a FINITE set once frozen ⇒ n↦W_n is a finite-automaton orbit ⇒ eventually periodic — pigeonhole.
  4. Conclude via step 1; Π finite falls out as a by-product (only period's primes occur).
Key lemmas (claim + mechanism):
  - K1 gap-word⇒theorem — a_{n+T}−a_n=Σd; no-transient makes eventual period a period from n=1.
  - K2 Stage-1 freeze — bounded monotone integer sequence stabilizes (Lemma B certified for Γ*).
  - K3 (LOAD-BEARING) bounded active supports per window: ≤ a₁-computable B minimal supports can
    bind in any length-Γ* window — because a large prime q divides ≤1 integer per window and L3
    spreads q-terms ≥q apart, so only distinct SMALL companions (subsets of primes ≤Γ*≤M, finite
    pool) bind repeatedly ⇒ W_n finite-state.
Open gaps: PRIMARY = K3 per-window bound B is n-independent (same quantitative fact as antichain
  §8.4, but used to build a gap-word automaton, not a size bound). SECONDARY = confirm s(a_n) is a
  function of W_n alone post-freeze (no outside-window large prime becomes binding).
Cases to cover: |P|=1 (T=1,L=p sanity); |P|≥2 general; by-product Π-finite matches 105→{2,3,5,7}.
Watch out for: W_n must be a BOUNDED window + BOUNDED support pool (else re-enters the certified
  A_n obstruction); K3 must use realized value geometry (L3+Γ* window), NOT intersecting/anchor
  structure alone (§7b family is intersecting+anchored yet infinite Π); do NOT use the R1-DEGENERATE
  witness w_n=min{t:a_n+t∉A} (constant 1 on 375). Honest: aimo-0678 dynamics far simpler — transplant
  is structural not literal; steps 2–3 are the speculative heart, not yet proved.

---

monovariant-witness-descent: advance
Target: ∃ T,L with a_{n+T}=a_n+L ∀n≥1 (whole theorem; Π finite ⇒ endgame, certified).
Technique: descent on the greedy CHOICES via the S3 per-small-companion-set structure — count
  distinct PENDING small companions, not primes; a term with support ⊆S kills the whole {S,·} family.
Skeleton:
  1. Split each minimal support G=S(G)⊔L(G), S(G)=G∩{primes≤M}≠∅ (§8.2 certified).
  2. Φ_n = #distinct pending companions S (companion of a seen minimal support, not yet realized by a
     term with F(a_j)⊆S). Recruitment adds S (bounded pool); domination removes S and kills {S,·} (S3).
  3. Show finite companion pool + every pending S realized in bounded time ⇒ Φ_n freezes at 0 ⇒
     finitely many distinct large primes ⇒ Π finite ⇒ theorem.
Key lemmas (claim + mechanism):
  - K-real (WALL): every pending companion S is realized — a pure-S power m=(∏S)^k≥a₁ is a term
    (E1) iff it meets every OTHER minimal support; finite companion pool + L3 spreading large-q
    supports out forces a realizing window.
  - descent: finite pool + bounded realization ⇒ Φ_n→0, the freeze density/max-gap could not give.
Open gaps: K-real — (i) companion pool ⊆ 2^{primes≤M} is CONJECTURE (check no companion has prime
  >M across 375,385,9375,15015 before relying), (ii) the realizing-window quantitative bound from L3.
Cases to cover: |P|=1 (no large primes, Π=P); |P|≥2 with a large-prime companion.
Watch out for: Φ_n must read CHOSEN terms (which F(a_j)⊆S occurred), NOT A_n (certified obstruction);
  L3 gives a distance not a count — the realizing-window step is the honest gap, no hand-wave. Kept
  DISTINCT from value-stream-double-freeze: counts recruitments to bound Π (not cycle-pinning).

---

Not on the build table this round: anomaly-count-terminates (DEAD, M-threshold refuted).

Diversity check (plateau rule): field spans three disjoint mechanisms/targets — order-theory size
bound, value-stream cycle-pin, companion-descent — no two share a gap. Antichain §8.4 per-window
fact reappears in double-freeze K3 but aimed at a different target (periodicity vs Π-finite), so a
refutation of one does not sink the other. Recommend build all three; if reviewer judges
value-stream-double-freeze and monovariant-witness-descent too close (both extremal-on-choices),
prioritise value-stream-double-freeze (the genuinely new pole per the far-framing explorer) and the
antichain advance.

build set: redundant-constraint-antichain, value-stream-double-freeze, monovariant-witness-descent
