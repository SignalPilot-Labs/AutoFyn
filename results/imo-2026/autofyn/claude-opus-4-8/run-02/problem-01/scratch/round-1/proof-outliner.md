## imo-2026-01

Closed form (verified computationally, all move orders identical): **M = ∏_p p^{g_p}**, where
`g_p = gcd(v_p(x_1),…,v_p(x_2026))` (gcd of p-adic valuations, convention gcd(x,0)=x). NOT gcd(x_i)
and NOT lcm(x_i): board {4,6}→M=6 (gcd=2, lcm=12). The per-prime explorer's late claim "M=gcd(m,n)
for 2 numbers" is FALSE — {4,6}→6≠2, {8,4}→2≠4; the correct 2-number value is ∏_p p^{gcd(v_p(m),v_p(n))}.

Core fact underlying every route: a move sends each prime's touched valuation pair
`(a,b) ↦ (min(a,b),|a-b|)` (one subtractive-Euclidean step), simultaneously across all primes for the
one chosen position-pair. This gives the invariant `g_p` (⟹ b) and the monovariant `Ω_total` (⟹ a).

---

perprime-valuation: new  **(primary / frontrunner)**
Target: (a) exactly one M>1 after finitely many moves; (b) M choice-independent, = ∏_p p^{g_p}.
Technique: prime-by-prime valuation decomposition — ONE invariant (g_p) for (b) + ONE lex monovariant
  (Ω_total, C) for (a). KB: Invariants & monovariants; Divisor analysis.
Skeleton:
  1. Move = (a,b)↦(min(a,b),|a-b|) per prime — by v_p(gcd)=min, v_p(lcm/gcd)=max-min=|a-b|.
  2. (a) termination: (Ω_total=Σ_i Ω(x_i), C=#{>1}) strictly drops lexicographically each move —
     Ω_total falls by Ω(gcd(m,n)) (strict iff gcd>1); if gcd=1, pair→(1,mn) so C drops by 1.
  3. Terminal = no move ⇔ ≤1 entry >1.
  4. (b) invariant: g_p=gcd_i v_p(x_i) preserved, since gcd(min(a,b),|a-b|)=gcd(a,b) and
     gcd(rest,a,b)=gcd(rest,gcd(a,b)).
  5. Exactly one survivor: some prime has g_p≥1, invariance keeps a >1 entry ⇒ with ≤1 gives exactly 1.
  6. Value: terminal valuations (v_p(M),0,…,0) have gcd v_p(M)=g_p ⇒ M=∏_p p^{g_p}.
Key lemmas:
  - L1 move=subtractive Euclid — because lcm/gcd=∏_p p^{max-min}, valuation max-min=|a-b|.
  - L2 gcd invariant — gcd(a,b-a)=gcd(a,b) (WLOG a≤b); edges a=b→(a,0), a=0→(0,b); lift by associativity.
  - L3 Ω monovariant — min+|a-b|=max ≤ a+b, equality iff min=0 ⇒ ΔΩ_total=-Ω(gcd(m,n)).
  - L4 nonzero survivor — gcd of naturals not all zero is ≥1, invariance preserves a positive valuation.
Open gaps: G1 rigor of L1 over all primes at once; G2 gcd-with-0 conventions + multiset lift; G3 L3
  equality condition + summation bookkeeping; G4 gcd=1 subcase + lex well-foundedness; G5 step-5
  nonzero-survivor argument.
Cases to cover: move gcd>1 vs gcd=1; L2 valuation edges (a=b, a=0/b=0); prime dividing neither entry.
Watch out for: "exactly one" in (a) is NOT pure monovariant — it needs the (b) invariant (present both
  together); state gcd/valuation-with-0 conventions once; do NOT use the false "M=gcd(m,n)" 2-number
  shortcut.

---

confluence-newman: new  **(genuinely different framing — rival)**
Target: same whole claim (a)+(b).
Technique: Abstract Rewriting System + Newman's Lemma — termination (SN) + local confluence (WCR) ⇒
  unique normal form ⇒ M unique, WITHOUT computing the closed form.
Skeleton:
  1. States = size-2026 multisets of integers ≥1; rewrite = one move; normal form = ≤1 entry >1.
  2. SN via the same (Ω_total, C) monovariant.
  3. WCR by critical-pair analysis: disjoint pairs commute (clean); share-one-cell = the 3-entry
     critical pair (only nontrivial); same-pair trivial.
  4. Newman's Lemma ⇒ confluent ⇒ unique normal form ⇒ M unique (b).
  5. Exactly one survivor via g_p≥1.
Key lemmas: Newman's Lemma (NOT in KB — must prove from scratch by well-founded induction);
  disjoint-move commutation; 3-cell joinability.
Open gaps: G1 (**hardest**) local confluence on the 3-cell pair — {4,6,9}→{2,6,9} vs {3,4,6} do NOT
  meet at any intermediate state (only at the terminal form), so one-step WCR is FALSE; must prove
  multi-step joinability, realistically by importing the per-prime gcd invariant (perprime-valuation
  L2). G2 prove Newman's Lemma. G3 SN details.
Cases to cover: critical-pair overlap (disjoint / share-one / same); 3-cell size orderings (uniform).
Watch out for: no one-step diamond exists here — do not assert one-step local confluence; this route is
  heavier than the primary for the same crux (subtractive-Euclid gcd fact). Value = diversity + a
  uniqueness proof that never names the closed form.

---

descent-induction: new  **(route-B sibling of confluence, olympiad-idiomatic — lower priority)**
Target: same whole claim (a)+(b).
Technique: minimal-counterexample / well-founded induction on (Ω_total, C) — no ARS/Newman machinery,
  no closed form. Assume two plays give different M, take a minimal board, contradict via the two
  first moves.
Skeleton:
  1. Termination + terminal shape via the lex monovariant.
  2. Descent: first moves identical / disjoint (commute) / share-one-cell (3-cell joinability) — each
     routes both plays through a strictly smaller common board ⇒ minimality contradiction ⇒ M unique.
  3. Exactly one survivor via g_p≥1.
Key lemmas: disjoint-move commutation; 3-cell joinability (crux); g_p≥1.
Open gaps: G1 (**crux, SHARED with confluence-newman**) the 3-cell joinability — same {4,6,9} obstacle,
  likely must import perprime-valuation L2. G2 well-foundedness of descent. G3 termination details.
Cases to cover: first-move overlap identical / disjoint / share-one.
Watch out for: shares its crux with confluence-newman — the two die together on the 3-cell gap; build
  at most ONE of them alongside the primary. May not truly avoid the gcd invariant.

---

Field note for the reviewer/build set: perprime-valuation is the clear frontrunner (self-contained,
elementary, both parts). confluence-newman is the genuinely-different framing (route B, uniqueness
without the closed form) and is the recommended second build for diversity. descent-induction is a
route-B sibling sharing confluence's 3-cell crux — recommend it only as a copy-like backup, not
alongside confluence, to avoid two approaches dying on one wall. Suggested build set:
**perprime-valuation, confluence-newman** (add descent-induction only if a third slot is wanted).
</content>
