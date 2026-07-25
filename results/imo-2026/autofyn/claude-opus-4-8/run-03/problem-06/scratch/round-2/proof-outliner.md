## imo-2026-06

Situation: whole problem certified-reduced to ONE crux — Finite Alphabet (𝓐_∞ finite ⇔ primes(L)
finite). Both live approaches stall on this exact wall (shared-gap plateau). Per CLAUDE.md plateau
rule the field below puts TWO genuinely-different framings on the table alongside the advance:
one that changes the TOP-LEVEL TARGET (prove A periodic, strictly weaker than 𝓐_∞ finite), one
that changes the METHOD (extremal/monovariant descent, no order theory at all). All three are
complete rival attempts at the whole theorem; each inherits the certified no-transient +
Reduction lemmas so any of them, on closing its gap, yields a_{n+T}=a_n+L for ALL n≥1.

---

redundant-constraint-antichain: advance
Target: the full theorem — ∃ T,L with a_{n+T}=a_n+L ∀n≥1, via 𝓐_∞ (⊆-minimal prime-supports) finite.
Technique: order-theoretic antichain reduction (certified) + contradiction/pigeonhole on P + a
small-companion-domination argument to bound the alphabet. (See §8 just added to the approach file.)
Skeleton (crux attack; §1–§7 already certified/conditional-complete):
  1. Assume 𝓐_∞ infinite. Pigeonhole on finite P=primes(a_1): a fixed p*∈P lies in ∞-many minimal
     supports ⇒ an infinite ⊆-antichain all ∋ p* ⇒ arbitrarily large primes q_k∈ minimal G_k∋p*.
     — by L1 + finiteness of P (certified §7c).
  2. No large prime is a singleton minimal support: a bare {q} would force q|a_n ∀n, contradicting
     L3 (q ≤ |a_i−a_j|, bounded, vs. indices →∞). So G_k = S_k ⊔ {q_k,…}, small companion S_k≠∅. — L3.
  3. G minimal ⟺ no term has support ⊆ S (small companion never "activated"). — by Lemma 5 redundancy.
  4. [HARD STEP / open gap] For all but finitely many G_k, a term with support ⊆ S_k must eventually
     appear ⇒ contradiction with persistence ⇒ 𝓐_∞ finite.
  5. 𝓐_∞ finite ⇒ §4–§5 (certified conditional) give the theorem, T=|ρ(A)|, L=∏Π.
Key lemmas (claim + mechanism):
  - No-singleton-large-prime — because a persistent bare {q} demands q | every term, but L3 caps
    q by any index-distance, and distances are unbounded (a_n→∞). Forces the small-companion shape.
  - Minimality ⟺ companion never activated — because the ⊆-minimal cover of G is dominated exactly
    by a term whose primes all lie in the small companion S (any such term has support ⊊ G).
Open gaps: Step 4 — the "pure-S term must eventually be chosen." The obstruction is that a pure-S
integer is *selected* only if it meets EVERY minimal support, not just G; the real content is a
quantitative bound on the number of minimal-support companions *simultaneously active* in one
length-M window, independent of n. (Naive per-window factor-count log₂(a_n) grows with n and does
NOT close it — density explorer. Need an n-independent window bound, or refute it.)
Cases to cover: none beyond the single contradiction argument.
Watch out for: the §7b counterexample proves intersecting+anchor structure ALONE never forces
finiteness — Step 4 MUST use the greedy dynamics (which integers get chosen), not just set theory.
Do NOT reintroduce any p≤M threshold (refuted 375→19, 9375→67).

---

a-periodic-sole-witness: new
Target: the full theorem, via the STRICTLY WEAKER sufficient statement "A is periodic" (a finite
union of residue classes mod some L) — NOT 𝓐_∞ finite. (Approach file written.)
Technique: reframe the crux onto A itself; characterize periodicity of A by finiteness of the set
Q of "sole-witness" primes; bound Q by a density-loss (monovariant) argument on A_n↓A.
Skeleton:
  1. Whether c∈A depends only on {p∈Q : p|c}, where prime p is *relevant* iff p∈Q (Q = sole-witness
     primes: ∃ c∈A, F∈𝓐_∞ with F(c)∩F={p}). — definition-chase (dropping p ejects c iff p sole witness).
  2. Q finite ⇒ A periodic mod L=∏_{p∈Q}p. — Step 1 makes membership a function of c mod L.
  3. [HARD STEP] Q is finite: density(A_n) is non-increasing (A_n↓A, more constraints) and ≥1/M>0
     (certified); each NEW sole-witness prime forces a genuine, non-maskable density loss ε_p, and
     Σε_p ≤ 1−1/M ⇒ finitely many. — the monovariant is density(A_n), the novelty is sole-witness
     rigidity making the loss real.
  4. A periodic mod L ⇒ Lemmas 9–11 + no-transient (certified) ⇒ a_{n+T}=a_n+L ∀n≥1.
Key lemmas (claim + mechanism):
  - A periodic ⇔ Q finite — because a prime irrelevant to A can be quotiented out; only sole
    witnesses change membership when their divisibility is toggled.
  - The p*-obstruction is HARMLESS here — because in the {{p*}∪{q}} family NO large q is ever a
    sole witness (every c meets {p*,q} via p*), so Q={p*} and A is periodic mod p* even though
    𝓐_∞ is infinite. This is exactly why the weaker target dodges the antichain wall.
Open gaps: Step 3's "each new sole-witness prime causes a non-maskable density loss ε_p with
Σε_p convergent ≤ 1−1/M." Naive additive per-prime density is DEAD (losses overlap in
multi-witness terms); the fix must exploit that a sole witness is the ONLY witness (c coprime to
F∖{p}), so its residues are genuinely ejected and not recoverable by another prime.
Cases to cover: none beyond the density accounting.
Watch out for: do NOT claim density(A_n)→0 (false, p*-family). Keep sole-witness quantified over
GLOBAL 𝓐_∞. Consistency check on a_1=375: Q must come out {2,3,5,7,19}, L=3990 — matches certified.

---

monovariant-witness-descent: new
Target: the full theorem, via eventual periodicity of the gap word (g_n)=(a_{n+1}−a_n)∈{1,…,M}.
Technique: EXTREMAL/MONOVARIANT DESCENT transplanted from aimo-0678 (IMO 2015 SL N4) — no prime
supports, no antichain, no density. Build an integer witness that is non-increasing along the
recursion and bounded below, hence eventually constant (well-ordering); constancy pins a finite
modulus and forces the cyclic repeat. (Approach file written.)
Skeleton:
  1. State = forward orbit of fixed successor s on fixed A (certified no-transient); gap g_n∈{1..M}.
  2. Secondary "freezing" invariant R_n (running relevant-prime modulus), non-decreasing, changing
     only at recruitment steps. — analog of aimo-0678's gcd·lcm-frozen s_n.
  3. First-failure witness w_n := min{t∈{1..M}: a_n+t∉A} (or aimo-0678-faithful min{m>a_n: m∉A_n}−a_n).
  4. [HARD STEP] w_n (correctly normalized against R_n, not a_n) is non-increasing and ≥1 ⇒
     eventually constant; only finitely many recruitments (descent).
  5. R frozen + w constant ⇒ g_n a function of a_n mod R (finite state) ⇒ pigeonhole+determinism ⇒
     gap word eventually periodic ⇒ (no-transient) a_{n+T}=a_n+L ∀n.
Key lemmas (claim + mechanism):
  - Between recruitments the active constraints are effectively fixed — because a new large-prime
    constraint q bites only ≥ q/M indices away (L3 + linear growth), so within a window the witness
    sees a fixed constraint set and freezes.
  - Stabilized witness ⇒ finite modulus — a non-increasing ℕ-valued witness stabilizes by
    well-ordering; its stable value caps which primes can still be recruited.
Open gaps (this is a research gamble taken for field diversity — flag honestly):
  - G1: construct the freezing invariant (aimo-0678 had an exact algebraic identity; ours may not).
  - G2: prove the witness is genuinely non-increasing under the right normalization.
  - G3: descent bound on # recruitments (= the crux in monovariant clothing; G1+G2 must deliver a
    strictly-decreasing integer at each recruitment).
Cases to cover: none beyond the descent.
Watch out for: the monovariant must NOT be density (p*-family recruits at zero density cost — DEAD)
— it must be a first-failure/extremal integer witness. No p≤M threshold. If the freezing partner
cannot be built after a build attempt, RETHINK.

---

Field diversity check: three FAR-APART routes — (i) order theory + domination on 𝓐_∞;
(ii) different TARGET (A periodic via sole-witness density) that provably dodges the p*-wall;
(iii) different METHOD (extremal monovariant descent, aimo-0678). They fail independently, not
together. anomaly-count-terminates stays DEAD (M-threshold refuted) — not on the table.

Candidate slugs for the reviewer to rank:
  - redundant-constraint-antichain (advance)
  - a-periodic-sole-witness (new)
  - monovariant-witness-descent (new)
